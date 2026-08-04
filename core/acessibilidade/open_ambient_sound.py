#!/usr/bin/env python3
"""
OpenAmbientSoundAI -- O SO Que Escuta o Mundo
================================================
"Cego nao ouve a campainha. O SO ouve por ele."

O computador tem microfone. O microfone capta o mundo.
Mas o SO hoje e SURDO para tudo que nao seja a voz do usuario.

Este modulo da OUVIDOS ao SO. Ele escuta o ambiente 24/7
e classifica sons em tempo real: campainha, sirene, choro
de bebe, batida na porta, alarme de incendio, telefone.

QUANDO DETECTA, AVISA:
  - Cego: Iara fala ("Alguem tocou a campainha.")
  - Surdo: tela pisca + texto ("CAMPAINHA") + vibracao no smartwatch
  - Tetraplegico: overlay aparece + voz
  - Idoso: voz alta + tela

COMO FUNCIONA (pipeline):

  Microfone -> Audio chunk (1 seg) -> Modelo de classificacao
  -> Som classificado -> Filtro de confianca
  -> Alerta (voz/visual/haptico)

O MODELO (atualizado 2024/2025):
  - YAMNet (AudioSet baseline): 521 classes, 3.6M params, CPU-friendly.
  - Recomendado principal: Audio Spectrogram Transformer (AST) ou PaSST (Patchout Spectrogram Transformer) fine-tuned no AudioSet.
  - Alternativa moderna local: BEATs (2023) ou EAT (2024) via transformers/onnx.
  - Para fallback de voz: faster-whisper (large-v3-turbo ou distil-whisper 2024) - mas classificacao de eventos e prioritaria.
  - Stack recomendado: torchaudio + transformers + onnxruntime (tudo offline).
  Tudo LOCAL. Sem nuvem. Privacidade radical (P2).

A ETICA DE OUVIR:

  O SO escuta o ambiente. Mas NAO GRAVA continuamente.
  Processa em chunks de 1 segundo. Descarta o audio apos classificar.
  So guarda o EVENTO: "campainha as 14:32". Nunca o audio.
  Privacidade radical (P2). O microfone ouve, mas NAO lembra.

OS 6 NIVEIS DE ALERTA:

  1. SILENCIOSO: so loga (usuario dormindo)
  2. LOG: registra no historico
  3. HAPTICO: vibra no smartwatch (surdo)
  4. VISUAL: tela pisca + texto grande (surdo)
  5. VOZ: Iara fala o que ouviu (cego)
  6. URGENTE: todos os canais + som alto (incendio, sirene)

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict, deque
from datetime import datetime, timedelta
import re


# ============================================================================
# 1. ENUMS
# ============================================================================

class CategoriaSom(Enum):
    """Categorias de sons ambiente que o SO reconhece."""
    CAMPAINHA = ("campainha", "Campainha / interfone")
    SIRENE = ("sirene", "Sirene (ambulancia, policia, bombeiro)")
    ALARME_INCENDIO = ("incendio", "Alarme de incendio / fumaca")
    CHORO_BEBE = ("choro", "Choro de bebe")
    BATIDA_PORTA = ("porta", "Batida / batida na porta")
    TELEFONE = ("telefone", "Telefone tocando (fixo)")
    ALARME_RELOGIO = ("relogio", "Alarme de relogio / celular")
    LATIDO = ("latido", "Cachorro latindo")
    ROBO_ASPIRADOR = ("aspirador", "Robo aspirador / eletrodomestico")
    AGUA_CORRENDO = ("agua", "Agua correndo (torneira, chuva)")
    RISADA = ("risada", "Risada / conversa (presenca humana)")
    VIDRO_QUEBRANDO = ("vidro", "Vidro quebrando (invasao)")
    TROVAO = ("trovao", "Trovao / tempestade")
    BUZINA = ("buzina", "Buzina de carro")
    Grito = ("grito", "Grito / pedido de socorro")
    ALARME_GAS = ("gas", "Alarme de gas / monoxido de carbono")
    PASSOS = ("passos", "Passos / aproximacao de pessoa")
    PORTA_ABRINDO = ("porta_abrindo", "Porta abrindo ou fechando")
    CHUVA = ("chuva", "Chuva forte / temporal")
    VENTO = ("vento", "Vento forte / rajada")
    MAQUINA_LAVAR = ("lavar", "Maquina de lavar / secadora")
    ASPIRADOR_ROBO = ("aspirador_robo", "Aspirador de po robo (modelo 2025)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelUrgencia(Enum):
    """Nivel de urgencia do som detectado."""
    INFORMATIVO = ("info", "Informativo: algo aconteceu, sem perigo", 0)
    ATENCAO = ("atencao", "Atencao: pode precisar de acao", 1)
    IMPORTANTE = ("importante", "Importante: acao provavelmente necessaria", 2)
    URGENTE = ("urgente", "Urgente: acao necessaria AGORA", 3)
    EMERGENCIA = ("emergencia", "Emergencia: PERIGO DE VIDA", 4)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def peso(self) -> int:
        return self.value[2]


class CanalAlerta(Enum):
    """Canais de alerta que o sistema usa."""
    VOZ_IARA = ("voz", "Voz: Iara fala o que ouviu (cego)")
    VISUAL_TELA = ("visual", "Visual: tela pisca + texto grande (surdo)")
    HAPTICO_WATCH = ("haptico", "Haptico: vibracao no smartwatch")
    OVERLAY = ("overlay", "Overlay: janela flutuante da Iara")
    SOM_ALTO = ("som", "Som alto: beep/sirene do proprio PC")
    LOG_SILENCIOSO = ("log", "Log: so registra, sem alertar")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class EstadoMicrofone(Enum):
    """Estado do microfone ambiente."""
    ATIVO = ("ativo", "Ativo: ouvindo o ambiente 24/7")
    PAUSADO = ("pausado", "Pausado: usuario pausou (privacidade)")
    MODO_SESSAO = ("sessao", "Modo sessao: so ouve em horario definido")
    DORMINDO = ("dormindo", "Dormindo: baixo consumo, so emergencias")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusAlerta(Enum):
    """Status de um alerta gerado."""
    GERADO = ("gerado", "Alerta gerado")
    ENTREGUE = ("entregue", "Alerta entregue ao usuario")
    CONFIRMADO = ("confirmado", "Usuario confirmou que viu/ouviu")
    IGNORADO = ("ignorado", "Usuario ignorou (descartou)")
    ESCALADO = ("escalado", "Escalado: sem resposta, avisar contato")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass
class SomConhecido:
    """Definicao de um som que o sistema reconhece."""
    categoria: CategoriaSom
    urgencia: NivelUrgencia
    descricao: str
    acao_recomendada: str
    frases_iara: List[str] = field(default_factory=list)
    # exemplos de como a Iara anuncia (varia para nao ser robotico)
    cooldown_segundos: int = 30  # nao repetir o mesmo alerta por N segundos


@dataclass
class EventoSonoro:
    """Um evento sonoro detectado (NAO guarda o audio)."""
    id: str
    categoria: CategoriaSom
    urgencia: NivelUrgencia
    confianca: float          # 0.0 a 1.0
    timestamp: str
    canais_disparados: List[CanalAlerta] = field(default_factory=list)
    status: StatusAlerta = StatusAlerta.GERADO
    # metadados (sem audio)
    duracao_segundos: float = 0.0
    volume_estimado: float = 0.0  # 0.0 a 1.0


@dataclass
class PerfilAudicao:
    """Perfil do usuario: como quer ser avisado."""
    usuario: str = "cidadao"
    cego: bool = False
    surdo: bool = False
    motora: bool = False
    idoso: bool = False
    # configuracoes
    microfone_estado: EstadoMicrofone = EstadoMicrofone.ATIVO
    horario_silencioso: Tuple[int, int] = (22, 7)  # 22h as 7h: so emergencias
    volume_voz_iara: float = 0.8
    vibracao_haptica: bool = True
    # limiar de confianca para alertar
    confianca_minima: float = 0.65
    # contatos de emergencia (para escalonamento)
    contatos_emergencia: List[str] = field(default_factory=list)


@dataclass
class ChunkAudio:
    """Um chunk de audio processado (metadados apenas, sem audio real)."""
    indice: int
    timestamp: str
    duracao_ms: int = 1000
    classificacoes: List[Tuple[CategoriaSom, float]] = field(default_factory=list)
    volume_rms: float = 0.0


# ============================================================================
# 3. DADOS: SONS CONHECIDOS
# ============================================================================

def _init_sons_conhecidos() -> Dict[CategoriaSom, SomConhecido]:
    """Define todos os sons que o sistema reconhece."""
    return {
        CategoriaSom.CAMPAINHA: SomConhecido(
            CategoriaSom.CAMPAINHA, NivelUrgencia.IMPORTANTE,
            "Alguem tocou a campainha ou interfone.",
            "Ir ate a porta ou ver quem e pela camera.",
            frases_iara=[
                "Alguem tocou a campainha.",
                "Campainha! Tem visita.",
                "Interfone tocando.",
                "Alguem na porta.",
            ],
            cooldown_segundos=20,
        ),
        CategoriaSom.SIRENE: SomConhecido(
            CategoriaSom.SIRENE, NivelUrgencia.URGENTE,
            "Sirene de emergencia proxima (ambulancia, policia, bombeiro).",
            "Ter cuidado ao sair. Verificar se e para voce.",
            frases_iara=[
                "Sirene de emergencia proxima.",
                "Ouvi uma sirene. Cuidado ao sair.",
                "Veiculo de emergencia passando.",
            ],
            cooldown_segundos=60,
        ),
        CategoriaSom.ALARME_INCENDIO: SomConhecido(
            CategoriaSom.ALARME_INCENDIO, NivelUrgencia.EMERGENCIA,
            "ALARME DE INCENDIO DETECTADO. PERIGO IMINENTE.",
            "SAIR IMEDIATAMENTE. Verificar saida de emergencia.",
            frases_iara=[
                "EMERGENCIA! Alarme de incendio!",
                "INCENDIO! Saia agora!",
                "Alarme de fumaca detectado. Saia imediatamente!",
            ],
            cooldown_segundos=5,
        ),
        CategoriaSom.CHORO_BEBE: SomConhecido(
            CategoriaSom.CHORO_BEBE, NivelUrgencia.IMPORTANTE,
            "Bebe chorando.",
            "Verificar o bebe: fralda, fome, desconforto.",
            frases_iara=[
                "O bebe esta chorando.",
                "Bebe chorando. Talvez precise de voce.",
                "Ouvi o bebe. Va verificar.",
            ],
            cooldown_segundos=30,
        ),
        CategoriaSom.BATIDA_PORTA: SomConhecido(
            CategoriaSom.BATIDA_PORTA, NivelUrgencia.ATENCAO,
            "Alguem bateu na porta.",
            "Ir atender ou verificar pela camera.",
            frases_iara=[
                "Alguem bateu na porta.",
                "Batida na porta.",
                "Tem pessoa batendo aí.",
            ],
            cooldown_segundos=15,
        ),
        CategoriaSom.TELEFONE: SomConhecido(
            CategoriaSom.TELEFONE, NivelUrgencia.IMPORTANTE,
            "Telefone fixo tocando.",
            "Atender ou verificar quem ligou.",
            frases_iara=[
                "Telefone tocando.",
                "Telefone! Alguem ligando.",
                "O fixo esta tocando.",
            ],
            cooldown_segundos=30,
        ),
        CategoriaSom.ALARME_RELOGIO: SomConhecido(
            CategoriaSom.ALARME_RELOGIO, NivelUrgencia.ATENCAO,
            "Alarme de relogio ou celular tocando.",
            "Verificar o alarme. Pode ser horario importante.",
            frases_iara=[
                "Seu alarme esta tocando.",
                "Alarme do celular.",
                "Despertou! Alarme tocando.",
            ],
            cooldown_segundos=10,
        ),
        CategoriaSom.LATIDO: SomConhecido(
            CategoriaSom.LATIDO, NivelUrgencia.ATENCAO,
            "Cachorro latindo.",
            "Verificar: pode ser visita ou intruso.",
            frases_iara=[
                "O cachorro esta latindo.",
                "Latido! Talvez tem alguem la fora.",
                "Cachorro alertando. Va ver.",
            ],
            cooldown_segundos=45,
        ),
        CategoriaSom.VIDRO_QUEBRANDO: SomConhecido(
            CategoriaSom.VIDRO_QUEBRANDO, NivelUrgencia.URGENTE,
            "Vidro quebrando. Possivel invasao ou acidente.",
            "VERIFICAR SEGURANCA. Pode ser invasao. Ligar 190 se necessario.",
            frases_iara=[
                "ATENCAO! Vidro quebrando!",
                "Ouvi vidro quebrar. Verifique a casa.",
                "Som de vidro quebrado. Pode ser invasao.",
            ],
            cooldown_segundos=10,
        ),
        CategoriaSom.TROVAO: SomConhecido(
            CategoriaSom.TROVAO, NivelUrgencia.ATENCAO,
            "Trovao. Tempestade proxima.",
            "Desconectar aparelhos sensiveis. Evitar janelas abertas.",
            frases_iara=[
                "Trovao. Tempestade chegando.",
                "Ouvi um trovao. Cuidado com a chuva.",
                "Tempestade proxima. Feche as janelas.",
            ],
            cooldown_segundos=120,
        ),
        CategoriaSom.BUZINA: SomConhecido(
            CategoriaSom.BUZINA, NivelUrgencia.ATENCAO,
            "Buzina de carro proxima.",
            "Atencao ao cruzar rua ou sair de garagem.",
            frases_iara=[
                "Buzina! Cuidado com carro.",
                "Carro buzinando perto.",
                "Atencao: buzina proxima.",
            ],
            cooldown_segundos=30,
        ),
        CategoriaSom.Grito: SomConhecido(
            CategoriaSom.Grito, NivelUrgencia.URGENTE,
            "Grito detectado. Possivel pedido de socorro.",
            "VERIFICAR ORIGEM. Ligar 190 se necessario.",
            frases_iara=[
                "ATENCAO! Ouvi um grito!",
                "Grito detectado. Pode ser socorro.",
                "Alguem gritou perto. Verifique!",
            ],
            cooldown_segundos=15,
        ),
        CategoriaSom.RISADA: SomConhecido(
            CategoriaSom.RISADA, NivelUrgencia.INFORMATIVO,
            "Risada ou conversa. Presenca humana detectada.",
            "Informativo: tem gente por perto.",
            frases_iara=[
                "Tem gente conversando ai.",
                "Ouvi risadas. Tem visita?",
                "Presenca humana detectada.",
            ],
            cooldown_segundos=60,
        ),
        CategoriaSom.AGUA_CORRENDO: SomConhecido(
            CategoriaSom.AGUA_CORRENDO, NivelUrgencia.INFORMATIVO,
            "Agua correndo. Torneira aberta ou chuva forte.",
            "Verificar se esqueceu torneira aberta.",
            frases_iara=[
                "Agua correndo. Torneira aberta?",
                "Ouvi agua. Verifique a torneira.",
                "Som de agua. Chuva ou torneira?",
            ],
            cooldown_segundos=90,
        ),
        CategoriaSom.ROBO_ASPIRADOR: SomConhecido(
            CategoriaSom.ROBO_ASPIRADOR, NivelUrgencia.INFORMATIVO,
            "Robo aspirador ou eletrodomestico ligado.",
            "Informativo: eletrodomestico funcionando.",
            frases_iara=[
                "Aspirador rodando.",
                "Eletrodomestico ligado.",
            ],
            cooldown_segundos=120,
        ),
        # --- Novos sons catalogados 2024/2025 ---
        CategoriaSom.ALARME_GAS: SomConhecido(
            CategoriaSom.ALARME_GAS, NivelUrgencia.EMERGENCIA,
            "Alarme de gas ou monoxido de carbono detectado.",
            "SAIR IMEDIATAMENTE. Ventilar area. Ligar 193/190.",
            frases_iara=[
                "EMERGENCIA! Alarme de gas!",
                "Perigo de gas. Saia agora!",
                "Alarme de monoxido detectado. Evacue!",
            ],
            cooldown_segundos=5,
        ),
        CategoriaSom.PASSOS: SomConhecido(
            CategoriaSom.PASSOS, NivelUrgencia.ATENCAO,
            "Passos ou aproximacao de pessoa detectada.",
            "Verificar camera ou quem se aproxima (privacidade).",
            frases_iara=[
                "Ouvi passos.",
                "Alguem se aproximando.",
                "Passos proximos detectados.",
            ],
            cooldown_segundos=45,
        ),
        CategoriaSom.PORTA_ABRINDO: SomConhecido(
            CategoriaSom.PORTA_ABRINDO, NivelUrgencia.ATENCAO,
            "Porta abrindo ou fechando.",
            "Verificar se foi intencional ou invasao.",
            frases_iara=[
                "Porta abrindo.",
                "Alguem abriu a porta.",
                "Porta se fechando.",
            ],
            cooldown_segundos=20,
        ),
        CategoriaSom.CHUVA: SomConhecido(
            CategoriaSom.CHUVA, NivelUrgencia.INFORMATIVO,
            "Chuva forte ou temporal.",
            "Fechar janelas se necessario.",
            frases_iara=[
                "Esta chovendo forte.",
                "Temporal comecando.",
            ],
            cooldown_segundos=180,
        ),
        CategoriaSom.VENTO: SomConhecido(
            CategoriaSom.VENTO, NivelUrgencia.INFORMATIVO,
            "Vento forte ou rajada.",
            "Cuidado com objetos soltos.",
            frases_iara=[
                "Vento forte.",
                "Rajada de vento.",
            ],
            cooldown_segundos=120,
        ),
        CategoriaSom.MAQUINA_LAVAR: SomConhecido(
            CategoriaSom.MAQUINA_LAVAR, NivelUrgencia.INFORMATIVO,
            "Maquina de lavar roupa ou secadora em funcionamento.",
            "Informativo: ciclo de lavagem.",
            frases_iara=[
                "Maquina de lavar ligada.",
                "Lavadora rodando.",
            ],
            cooldown_segundos=300,
        ),
        CategoriaSom.ASPIRADOR_ROBO: SomConhecido(
            CategoriaSom.ASPIRADOR_ROBO, NivelUrgencia.INFORMATIVO,
            "Aspirador robo autonomo em operacao.",
            "Informativo: limpeza automatica.",
            frases_iara=[
                "Aspirador robo funcionando.",
                "Robo aspirador em acao.",
            ],
            cooldown_segundos=180,
        ),
    }

# ============================================================================
# 3.5 HARDWARE RECOMENDADO (precos aproximados 2024/2025 - BRL/USD)
# ============================================================================

RECOMENDACOES_HARDWARE = {
    "microfone_usb_basico": {
        "nome": "Fifine K669B / Amcrest USB Microphone",
        "preco_usd_2025": 32,
        "preco_brl_2025": 175,
        "tipo": "USB plug-and-play, omnidirecional",
        "nota": "Melhor custo-beneficio para 24/7. Boa captura de ambiente.",
        "link_ref": "amazon.com / mercado-livre",
    },
    "microfone_usb_premium": {
        "nome": "Blue Yeti Nano / Rode NT-USB+ (2024/25 refresh)",
        "preco_usd_2025": 99,
        "preco_brl_2025": 520,
        "tipo": "Cardioide + padroes, gain control",
        "nota": "Recomendado para usuarios com multiplos ambientes ou alta fidelidade.",
    },
    "microfone_lav": {
        "nome": "BOYA BY-M1 / DJI Mic Mini (2024)",
        "preco_usd_2025": 25,
        "preco_brl_2025": 140,
        "tipo": "Lavalier com clip (para posicao proxima a fonte)",
        "nota": "Ideal para deteccao de voz/alarme proximo ao usuario.",
    },
    "array_mic": {
        "nome": "ReSpeaker 4-Mic Array / Seeed 2-Mic Pi HAT (2025)",
        "preco_usd_2025": 28,
        "preco_brl_2025": 155,
        "tipo": "Microfone array com beamforming (Raspberry Pi / SBC)",
        "nota": "Excelente para direcao de som + cancelamento de ruido. Recomendado para instalacao fixa.",
    },
    "kit_acessibilidade": {
        "nome": "Kit completo (mic USB + Raspberry Pi Zero 2W + case)",
        "preco_usd_2025": 85,
        "preco_brl_2025": 460,
        "nota": "Setup dedicado 24/7 para OpenAmbientSoundAI em hardware soberano.",
    },
}

def listar_hardware() -> None:
    """Imprime tabela de hardware recomendado com precos atualizados."""
    print("\n[RECOMENDACOES DE HARDWARE - precos 2024/2025]")
    for key, h in RECOMENDACOES_HARDWARE.items():
        print(f"  {key}:")
        print(f"    Nome: {h['nome']}")
        print(f"    Preco USD: ~${h['preco_usd_2025']} | BRL: R${h.get('preco_brl_2025', 'N/A')}")
        if 'tipo' in h:
            print(f"    Tipo: {h['tipo']}")
        print(f"    Nota: {h['nota']}")
        print()



# ============================================================================
# 4. MOTOR DE CLASSIFICACAO (simulado)
# ============================================================================

class ClassificadorSom:
    """
    Simula a classificacao de audio pelo modelo.
    Stack 2024/2025 recomendado (real implementation):
      - Audio event detection: transformers.ASTForAudioClassification (MIT/ast-finetuned-audioset-10-10-0.4593)
        ou PaSST / BEATs via HuggingFace + onnxruntime.
      - Alternativa leve: YAMNet via tf-lite ou yamnet-onnx.
      - Fallback ASR se necessario: faster-whisper (large-v3 ou distil-whisper-small 2024).
      - Captura: sounddevice ou pyaudio -> resample 16kHz mono -> model.
    Tudo offline. Aqui: simulacao deterministica para o demo e testes.
    """

    # simulacao de probabilidades por categoria
    @staticmethod
    def classificar_chunk(chunk_idx: int) -> List[Tuple[CategoriaSom, float]]:
        """
        Simula classificacao de 1 segundo de audio.
        Retorna lista de (categoria, confianca) ordenada por confianca.
        """
        import random
        random.seed(chunk_idx * 7 + 13)

        # 80% dos chunks: silencio ou ruido nao classificavel
        if random.random() < 0.80:
            return []

        # 20% dos chunks: algum som detectado
        categorias_disponiveis = list(CategoriaSom)
        num_sons = random.choices([1, 2], weights=[0.85, 0.15])[0]
        resultados = []
        for _ in range(num_sons):
            cat = random.choice(categorias_disponiveis)
            confianca = random.uniform(0.40, 0.98)
            resultados.append((cat, round(confianca, 3)))
        resultados.sort(key=lambda x: -x[1])
        return resultados


# ============================================================================
# 5. ENGINE
# ============================================================================

class AmbientSoundEngine:
    """Motor de escuta ambiente do SO."""

    def __init__(self) -> None:
        self.sons: Dict[CategoriaSom, SomConhecido] = _init_sons_conhecidos()
        self.eventos: List[EventoSonoro] = []
        self.historico_chunks: deque = deque(maxlen=3600)  # 1 hora de chunks
        self.perfil: PerfilAudicao = PerfilAudicao()
        self.classificador = ClassificadorSom()
        self._ultimo_alerta: Dict[CategoriaSom, datetime] = {}
        self._chunk_counter = 0
        self._frase_counter: Dict[CategoriaSom, int] = defaultdict(int)

    # -- configurar perfil -------------------------------------------------

    def configurar_perfil(
        self,
        usuario: str = "cidadao",
        cego: bool = False,
        surdo: bool = False,
        motora: bool = False,
        idoso: bool = False,
        contatos_emergencia: Optional[List[str]] = None,
    ) -> PerfilAudicao:
        """Configura o perfil de audicao do usuario."""
        self.perfil = PerfilAudicao(
            usuario=usuario,
            cego=cego, surdo=surdo, motora=motora, idoso=idoso,
            contatos_emergencia=contatos_emergencia or [],
        )
        return self.perfil

    # -- processar chunk ---------------------------------------------------

    def processar_chunk(self) -> Optional[EventoSonoro]:
        """
        Processa 1 chunk de audio (1 segundo).
        No mundo real: captura do microfone -> modelo.
        Aqui: simulacao.
        """
        if self.perfil.microfone_estado == EstadoMicrofone.PAUSADO:
            return None

        self._chunk_counter += 1
        agora = datetime.now()
        timestamp = agora.isoformat()

        # classificar
        classificacoes = self.classificador.classificar_chunk(self._chunk_counter)

        # registrar chunk (metadados apenas)
        chunk = ChunkAudio(
            indice=self._chunk_counter,
            timestamp=timestamp,
            classificacoes=classificacoes,
        )
        self.historico_chunks.append(chunk)

        if not classificacoes:
            return None

        # pegar o som com maior confianca
        cat_top, conf_top = classificacoes[0]

        # filtro de confianca
        if conf_top < self.perfil.confianca_minima:
            return None

        # verificar se e horario silencioso
        hora = agora.hour
        inicio_sil, fim_sil = self.perfil.horario_silencioso
        em_silencioso = False
        if inicio_sil <= fim_sil:
            em_silencioso = inicio_sil <= hora < fim_sil
        else:
            em_silencioso = hora >= inicio_sil or hora < fim_sil

        # em horario silencioso, so alerta emergencias
        som_info = self.sons.get(cat_top)
        if som_info is None:
            return None

        if em_silencioso and som_info.urgencia.peso < NivelUrgencia.URGENTE.peso:
            return None  # silencioso: so urgencia+

        # verificar cooldown
        ultimo = self._ultimo_alerta.get(cat_top)
        if ultimo and (agora - ultimo).total_seconds() < som_info.cooldown_segundos:
            return None  # muito recente, ignorar

        # gerar evento
        evento = EventoSonoro(
            id=f"SND-{self._chunk_counter:06d}",
            categoria=cat_top,
            urgencia=som_info.urgencia,
            confianca=conf_top,
            timestamp=timestamp,
            canais_disparados=self._decidir_canais(som_info.urgencia),
        )
        self._ultimo_alerta[cat_top] = agora
        self.eventos.append(evento)
        return evento

    # -- decidir canais de alerta ------------------------------------------

    def _decidir_canais(self, urgencia: NivelUrgencia) -> List[CanalAlerta]:
        """Decide quais canais disparar baseado no perfil e urgencia."""
        canais: List[CanalAlerta] = []

        if self.perfil.cego:
            canais.append(CanalAlerta.VOZ_IARA)
        if self.perfil.surdo:
            canais.append(CanalAlerta.VISUAL_TELA)
            canais.append(CanalAlerta.OVERLAY)
        if self.perfil.motora:
            canais.append(CanalAlerta.OVERLAY)

        if self.perfil.vibracao_haptica and urgencia.peso >= NivelUrgencia.ATENCAO.peso:
            canais.append(CanalAlerta.HAPTICO_WATCH)

        if self.perfil.idoso:
            canais.append(CanalAlerta.VOZ_IARA)
            canais.append(CanalAlerta.VISUAL_TELA)

        # emergencia: TODOS os canais
        if urgencia == NivelUrgencia.EMERGENCIA:
            canais = list(CanalAlerta)
            if CanalAlerta.LOG_SILENCIOSO in canais:
                canais.remove(CanalAlerta.LOG_SILENCIOSO)

        # se nao tem deficiencia especifica, alerta padrao
        if not canais:
            canais.append(CanalAlerta.OVERLAY)
            if urgencia.peso >= NivelUrgencia.URGENTE.peso:
                canais.append(CanalAlerta.VOZ_IARA)

        # remover duplicados
        seen = set()
        resultado = []
        for c in canais:
            if c.id not in seen:
                seen.add(c.id)
                resultado.append(c)
        return resultado

    # -- gerar fala da Iara ------------------------------------------------

    def gerar_fala_iara(self, evento: EventoSonoro) -> str:
        """Gera o texto que a Iara vai FALAR para o cego."""
        som_info = self.sons.get(evento.categoria)
        if som_info is None:
            return f"Som detectado: {evento.categoria.rotulo}."

        # variar a frase para nao ser robotico
        frases = som_info.frases_iara
        idx = self._frase_counter[evento.categoria] % len(frases)
        self._frase_counter[evento.categoria] += 1
        fala = frases[idx]

        # emergencia: prefixo urgente
        if evento.urgencia == NivelUrgencia.EMERGENCIA:
            fala = f"EMERGENCIA! {fala}"
        elif evento.urgencia == NivelUrgencia.URGENTE:
            fala = f"ATENCAO! {fala}"

        return fala

    # -- gerar alerta visual (texto) ---------------------------------------

    def gerar_alerta_visual(self, evento: EventoSonoro) -> str:
        """Gera o texto VISUAL para o surdo (tela pisca)."""
        som_info = self.sons.get(evento.categoria)
        if som_info is None:
            return evento.categoria.rotulo.upper()

        prefixo = {
            NivelUrgencia.INFORMATIVO: "",
            NivelUrgencia.ATENCAO: "ATENCAO: ",
            NivelUrgencia.IMPORTANTE: "IMPORTANTE: ",
            NivelUrgencia.URGENTE: "!!! URGENTE: ",
            NivelUrgencia.EMERGENCIA: "!!! EMERGENCIA !!! ",
        }.get(evento.urgencia, "")

        return f"{prefixo}{som_info.descricao.upper()}"

    # -- escalonamento (sem resposta) --------------------------------------

    def verificar_escalamento(self) -> List[str]:
        """
        Verifica se algum alerta URGENTE+ nao foi confirmado
        e precisa ser escalado para contato de emergencia.
        """
        escalacoes: List[str] = []
        agora = datetime.now()
        for evento in self.eventos:
            if evento.status != StatusAlerta.GERADO:
                continue
            if evento.urgencia.peso < NivelUrgencia.URGENTE.peso:
                continue
            # verificar tempo decorrido
            try:
                ts = datetime.fromisoformat(evento.timestamp)
            except (ValueError, TypeError):
                continue
            decorrido = (agora - ts).total_seconds()
            if decorrido > 60 and self.perfil.contatos_emergencia:
                evento.status = StatusAlerta.ESCALADO
                for contato in self.perfil.contatos_emergencia:
                    escalacoes.append(
                        f"Escalonar para {contato}: {evento.categoria.rotulo} "
                        f"as {ts.strftime('%H:%M:%S')}"
                    )
        return escalacoes

    # -- historico e estatisticas ------------------------------------------

    def eventos_por_categoria(self) -> Dict[CategoriaSom, int]:
        contagem: Dict[CategoriaSom, int] = defaultdict(int)
        for e in self.eventos:
            contagem[e.categoria] += 1
        return dict(contagem)

    def eventos_hoje(self) -> List[EventoSonoro]:
        hoje = datetime.now().date()
        return [
            e for e in self.eventos
            if datetime.fromisoformat(e.timestamp).date() == hoje
        ]

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sons_cadastrados": len(self.sons),
            "categorias_som": len(list(CategoriaSom)),
            "niveis_urgencia": len(list(NivelUrgencia)),
            "canais_alerta": len(list(CanalAlerta)),
            "eventos_totais": len(self.eventos),
            "chunks_processados": len(self.historico_chunks),
            "perfil_cego": self.perfil.cego,
            "perfil_surdo": self.perfil.surdo,
            "microfone_estado": self.perfil.microfone_estado.id,
        }


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo() -> None:
    e = AmbientSoundEngine()

    print("=" * 70)
    print("OpenAmbientSoundAI -- O SO Que Escuta o Mundo")
    print("=" * 70)

    # --- Catalogo de sons ---
    print(f"\n[CATALOGO DE SONS ({len(e.sons)})]")
    for cat in CategoriaSom:
        som = e.sons.get(cat)
        if som:
            urg = f"[{som.urgencia.id.upper()}]"
            print(f"\n  {urg} {cat.rotulo}")
            print(f"    Descricao: {som.descricao}")
            print(f"    Acao: {som.acao_recomendada}")
            print(f"    Cooldown: {som.cooldown_segundos}s")
            print(f"    Iara diz: \"{som.frases_iara[0]}\"")

    # --- Configurar perfil ---
    print("\n[PERFIL: Joao -- cego]")
    e.configurar_perfil("Joao", cego=True, contatos_emergencia=["Maria (esposa)", "Andre (vizinho)"])
    print(f"  Usuario: {e.perfil.usuario}")
    print(f"  Cego: {e.perfil.cego}")
    print(f"  Confianca minima: {e.perfil.confianca_minima}")
    print(f"  Horario silencioso: {e.perfil.horario_silencioso[0]}h-{e.perfil.horario_silencioso[1]}h")
    print(f"  Contatos emergencia: {e.perfil.contatos_emergencia}")

    # --- Simular 200 chunks (200 segundos) ---
    print("\n[SIMULACAO: 200 segundos de escuta ambiente]")
    print("  (80% silencio, 20% algum som detectado)")
    print()

    eventos_gerados = []
    for i in range(200):
        evento = e.processar_chunk()
        if evento:
            eventos_gerados.append(evento)
            fala = e.gerar_fala_iara(evento)
            visual = e.gerar_alerta_visual(evento)
            conf_pct = f"{evento.confianca:.0%}"
            print(f"  [{evento.id}] {evento.timestamp[11:19]} | "
                  f"{evento.urgencia.id.upper():<12} | "
                  f"{evento.categoria.rotulo:<25} | conf:{conf_pct}")
            print(f"    Iara diz: \"{fala}\"")
            if e.perfil.surdo or True:  # mostrar tambem
                print(f"    Tela mostra: \"{visual}\"")
            print()

    # --- Estatisticas ---
    print(f"\n[ESTATISTICAS]")
    sc = e.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    print(f"\n  Eventos por categoria:")
    contagem = e.eventos_por_categoria()
    for cat, n in sorted(contagem.items(), key=lambda x: -x[1]):
        print(f"    {cat.rotulo:<30} {n}")

    # --- Perfil surdo ---
    print("\n\n[PERFIL: Maria -- surda]")
    e2 = AmbientSoundEngine()
    e2.configurar_perfil("Maria", surdo=True)
    # forcar alguns eventos
    for i in range(50):
        ev = e2.processar_chunk()
        if ev:
            visual = e2.gerar_alerta_visual(ev)
            print(f"  [{ev.id}] {ev.categoria.rotulo:<25} | {ev.urgencia.id.upper()}")
            print(f"    Tela pisca: \"{visual}\"")
            print(f"    Canais: {[c.id for c in ev.canais_disparados]}")

    # --- Etica ---
    print("\n[ETICA -- O SO ouve, mas NAO lembra]")
    print("""
  O microfone capta audio continuamente. Mas:

  1. NAO GRAVA: processa em chunks de 1 segundo. Descarta o audio
     apos classificar. So guarda o EVENTO (categoria + timestamp).
     O audio nunca vai para o disco. Nunca vai para a nuvem.

  2. NAO TRANSCREVE: o modelo classifica SONS, nao fala.
     "Campainha" sim. "Joao disse X as 14:32" NUNCA.
     O microfono ouve sons, nao escuta conversas.

  3. NAO ENVIA: tudo local. Nenhum dado sonoro sai do dispositivo.
     O modelo roda no processador (AST/PaSST ou YAMNet ~3-80M params, CPU/GPU local).

  4. DESLIGAVEL: usuario pode pausar a escuta a qualquer momento.
     "Iara, parar de ouvir." O microfone fecha. Radical.

  5. LOG AUDITAVEL: cada evento e registrado. O usuario pode VER
     tudo que o sistema detectou. Transparencia radical (P4).
""")

    # --- Integracao ---
    print("[INTEGRACAO COM A IARA]")
    print("""
  CENARIO 1: Cego sozinho em casa
    [Microfone capta: DING-DONG]
    Modelo classifica: CAMPAINHA (confianca 92%)
    Iara fala: "Alguem tocou a campainha."
    Cego: "Iara, quem e?"
    Iara chama camera (se instalada): "Tem uma pessoa na porta."
    Cego decide: atender ou nao.

  CENARIO 2: Surdo trabalhando com fones
    [Microfone capta: WAAAH-WAAAH]
    Modelo classifica: CHORO DE BEBE (confianca 88%)
    Tela pisca: "BEBE CHORANDO"
    Smartwatch vibra
    Overlay Iara: "O bebe esta chorando."

  CENARIO 3: Idoso dormindo
    [Horario silencioso: so emergencias]
    [Microfone capta: BEEP-BEEP-BEEP]
    Modelo classifica: ALARME DE INCENDIO (confianca 95%)
    Iara (voz ALTA): "EMERGENCIA! Alarme de incendio! Saia agora!"
    Tela pisca vermelho: "INCENDIO! SAIA!"
    Smartwatch vibra forte
    Se sem resposta em 60s: escala para contato de emergencia

  CENARIO 4: Pessoa sem deficiencia
    [Microfone capta: campainha]
    Overlay discreto no canto: "Campainha (14:32)"
    Sem voz. Sem vibracao. So registro.
    Se a pessoa ja sabe (ouviu), ignora. Se nao soubia, ve o overlay.
""")

    # --- Filosofia ---
    print("=" * 70)
    print("FILOSOFIA -- O SO que ouve o mundo")
    print("=" * 70)
    print("""
A LACUNA MAIS PERIGOSA:

  Cego que usa a Republica ja controla o SO por voz.
  Ja audita rede. Ja programa na IDE inclusiva.
  Mas nao SABE que a campainha tocou.

  A tecnologia deu ao cego o controle do COMPUTADOR.
  Mas esqueceu de dar o controle da CASA.

  A campainha toca. O cego nao ouve.
  O bebe chora. O cego nao sabe.
  A sirene da ambulancia. O cego nao percebe.
  O vidro quebra. O cego nao reage.

  O computador, que TEM microfone, ficou SURDO.
  Surdo para tudo que nao seja a voz do usuario.

O MICROFONE QUE OUVE O MUNDO:

  Este modulo da OUVIDOS ao SO.
  O microfone, antes so para voz do usuario, agora escuta o AMBIENTE.
  Classifica sons. Alerta o usuario. Salva vidas.

  Nao e espionagem. E ACESSIBILIDADE.
  O cego precisa saber que a campainha tocou.
  O surdo precisa VER que o bebe chora.
  O idoso precisa ser ACORDADO se o alarme toca.

PRIVACIDADE RADICAL:

  O SO ouve o mundo. Mas NAO espiona.
  Processa em chunks de 1 segundo. Descarta o audio.
  Nao transcreve fala. Nao grava conversa.
  Nao envia nada para a nuvem.
  O microfone e uma ORELHA, nao uma testemunha.

A METAFORA DO CAO-GUIA:

  Um cao-guia ouve o mundo pelo dono.
  Late quando a campainha toca.
  Reage quando alguem se aproxima.
  Acorda o dono em emergencia.

  O OpenAmbientSoundAI e o CAO-GUIA DIGITAL.
  Ele ouve. Ele avisa. Ele protege.
  Mas, diferente do cao, ele:
  - Nao precisa ser alimentado.
  - Nao dorme.
  - Nao se distrai.
  - Escuta sons que o cao nao ouve (alarme de gas, por exemplo).

O PRINCIPIO:

  A acessibilidade nao termina na tela.
  A acessibilidade comeca na porta de casa.
  Se o cego nao sabe que a campainha tocou,
  toda a tecnologia do SO e inutil.
  Ele nao controla o COMPUTADOR. Ele controla a VIDA.
""")


if __name__ == "__main__":
    _demo()
