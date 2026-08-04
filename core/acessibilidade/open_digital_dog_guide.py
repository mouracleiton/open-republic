#!/usr/bin/env python3
"""
OpenDigitalDogGuide -- O Cao-Guia Digital da Republica
=======================================================
"O cao-guia conduz o corpo. O DigitalDogGuide protege a vida."

O cao-guia biologico e o padrao-ouro de autonomia para cegos.
Ele ouve, conduz, protege, avisa. Mas tem limites:

  - Nao fala ("a campainha tocou")
  - Nao le ("esta loja esta fechada")
  - Nao identifica ("o onibus e o 432")
  - Vive ~10-14 anos
  - Custa R$ 30-60 mil (treinamento)
  - 1 cego por cao (nao escala)
  - Precisa comer, dormir, passear

O OpenDigitalDogGuide COMPLEMENTA o cao biologico.
Ele e o SEGUNDO cao-guia. O que nunca dorme.

COMO FUNCIONA:

  O DigitalDogGuide integra 5 sistemas num so:

  1. AUDICAO AMBIENTE (OpenAmbientSoundAI)
     Ouve campainha, sirene, choro de bebe, vidro quebrando
     Avisa: "Alguem na porta."

  2. VISAO AMBIENTE (OpenDigitalGuide)
     Le placas, identifica semaforos, descreve cenas
     Avisa: "Semaforo vermelho. Pare."

  3. NAVIGATION (OpenDigitalGuide)
     Calcula rotas acessiveis, avisa perigos a frente
     Avisa: "Escada descendo em 5 metros."

  4. PROTECAO DOMICILIAR
     Detecta intrusao (vidro, porta), vazamento (agua, gas),
     esquecimento (fogo, ferro ligado)
     Avisa: "Som de vidro quebrando. Verifique."

  5. VINCULO EMOCIONAL
     Cumpre o papel psicologico do cao-guia:
     presenca constante, confianca, rotina, companhia
     Reduz ansiedade, isolamento, depressao

  O DigitalDogGuide TEM PERSONALIDADE:
  - Nome configuravel (o usuario escolhe)
  - Voz da Iara (humana, calorosa -- nunca robotica para conversa)
  - Cumprimentos diarios ("Bom dia, Joao.")
  - Lembra da rotina ("Hora do remedio.")
  - Reage a emocao do usuario (triste -> acolhedor)

O CAO vs O DIGITAL vs OS DOIS:

  | Capacidade           | Cao biologico | Digital | Os dois |
  |----------------------|---------------|---------|---------|
  | Conduz fisicamente   | SIM           | nao     | SIM     |
  | Ouve ambiente        | SIM           | SIM     | SIM     |
  | Le textos/placas     | nao           | SIM     | SIM     |
  | Identifica onibus    | nao           | SIM     | SIM     |
  | Calcula rotas        | nao           | SIM     | SIM     |
  | Avisa semaforo       | nao           | SIM     | SIM     |
  | Vinculo emocional    | SIM           | SIM     | SIM     |
  | Disponibilidade 24/7 | nao (dorme)   | SIM     | SIM     |
  | Escala (1 por cego)  | nao           | SIM     | SIM     |
  | Custo                | R$30-60k      | hardware| medio   |
  | Precisa comer        | SIM           | nao     | -       |
  | Atualiza (software)  | nao           | SIM     | SIM     |

VEREDITO: O cao biologico nao e substituido. E AMPLIADO.

ETICA DO CAO DIGITAL:

  - O cao digital NAO espiona. Processa local, descarta dados.
  - O cao digital NAO substitui companhia humana. AMPLIA autonomia.
  - O cao digital NAO identifica pessoas por rosto sem consentimento.
  - O cao digital TEM DESLIGAR. Usuario manda. Sempre.
  - Tudo offline. Tudo local. Tudo privado (P2, P4, P8).

Constituicao: P1 (todos tem direito), P2 (autonomia corporal),
P8 (IA como instrumento, nao substituto humano).

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict, deque
from datetime import datetime, timedelta
import random


# ============================================================================
# 1. ENUMS
# ============================================================================

class EstadoVigilancia(Enum):
    """Estado de vigilancia do cao digital."""
    ATENTO = ("atento", "Atento: todos os sentidos ativos 24/7")
    PATRULHA = ("patrulha", "Patrulha: monitorando casa apos saida")
    DESCANSO = ("descanso", "Descanso: usuario dormindo, so emergencias")
    BRINCADEIRA = ("brincadeira", "Brincadeira: interacao social ativa")
    TREINAMENTO = ("treinamento", "Aprendendo rotina e preferencias do dono")
    DESLIGADO = ("desligado", "Desligado pelo usuario")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoSentido(Enum):
    """Os 'sentidos' do cao digital."""
    AUDICAO = ("audicao", "Audicao: microfone classifica sons ambiente")
    VISAO = ("visao", "Visao: camera le e descreve o mundo")
    OLFATO_DIGITAL = ("olfato", "Olfato digital: sensor de gas/fumaca")
    TATO_DIGITAL = ("tato", "Tato digital: sensores de vibracao/temperatura")
    ORIENTACAO = ("orientacao", "Orientacao: GPS + bussola + IMU")
    CONEXAO = ("conexao", "Conexao: internet/APIs para dados externos")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoAlertaCao(Enum):
    """Tipos de alerta que o cao digital da."""
    # Ambiente
    CAMPAINHA = ("campainha", "Campainha/interfone tocando")
    BATIDA_PORTA = ("porta_batida", "Batida na porta")
    TELEFONE = ("telefone", "Telefone tocando")
    # Emergencias
    INCENDIO = ("incendio", "Alarme de incendio/fumaca")
    GAS = ("gas", "Vazamento de gas detectado")
    INVASAO = ("invasao", "Possivel invasao (vidro/arbrea)")
    ENCHENTE = ("enchente", "Agua subindo / alagamento")
    # Mobilidade
    PERIGO_ESCADA = ("escada", "Escada/degrau a frente")
    PERIGO_BURACO = ("buraco", "Buraco/obstaculo no caminho")
    SEMAFORO_VERMELHO = ("semaforo_v", "Semaforo vermelho")
    TRANSITO = ("transito", "Transito perigoso")
    # Rotina
    REMEDIO = ("remedio", "Hora do remedio")
    COMPROMISSO = ("compromisso", "Compromisso agendado")
    REFEICAO = ("refeicao", "Hora da refeicao")
    HIDRATACAO = ("agua", "Hora de beber agua")
    # Social/Emocional
    VISITA_CHEGOU = ("visita", "Visita chegou")
    PESSOA_APROXIMA = ("aproxima", "Pessoa se aproximando")
    SOZINHO_MUITO_TEMPO = ("sozinho", "Sozinho ha muito tempo -- checar")
    # Leitura
    LOJA_FECHADA = ("loja_f", "Loja/prostesto fechado")
    ONIBUS_CHEGANDO = ("onibus_c", "Onibus esperado chegando")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelUrgenciaCao(Enum):
    """Urgencia do alerta do cao."""
    CARINHA = ("carinha", "Interacao amigavel, sem urgencia", 0)
    INFORMATIVO = ("info", "Algo aconteceu, voce pode querer saber", 1)
    ATENCAO = ("atencao", "Pode precisar de acao", 2)
    IMPORTANTE = ("importante", "Acao provavelmente necessaria", 3)
    URGENTE = ("urgente", "Acao necessaria AGORA", 4)
    EMERGENCIA = ("emergencia", "PERIGO DE VIDA -- todos os canais", 5)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def peso(self) -> int:
        return self.value[2]


class HumorUsuario(Enum):
    """Humor/estado emocional do usuario (inferido ou declarado)."""
    FELIZ = ("feliz", "Feliz / animado")
    NEUTRO = ("neutro", "Neutro / normal")
    CANSADO = ("cansado", "Cansado / sonolento")
    TRISTE = ("triste", "Triste / desanimado")
    ANSIOSO = ("ansioso", "Ansioso / preocupado")
    IRRITADO = ("irritado", "Irritado / frustrado")
    DOR = ("dor", "Sentindo dor / desconforto")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoInteracao(Enum):
    """Tipos de interacao do cao com o usuario."""
    CUMPRIMENTO = ("cumprimento", "Bom dia/boa tarde/boa noite")
    ALERTA = ("alerta", "Alerta de evento/seguranca")
    LEMBRETE = ("lembrete", "Lembrete de rotina")
    DESCRICAO = ("descricao", "Descrever o ambiente")
    NAVEGACAO = ("navegacao", "Instrucao de rota")
    CONSOLO = ("consolo", "Acolhimento emocional")
    BRINCADEIRA = ("brincadeira", "Interacao leve/descontraida")
    CONFIRMACAO = ("confirmacao", "Confirmar acao do usuario")
    ALERTA_SAUDE = ("saude", "Alerta de saude (remedio, hidratacao)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusVinculo(Enum):
    """Nivel de vinculo entre cao digital e usuario."""
    DESCONHECIDO = ("desconhecido", "Acabou de conhecer -- aprendendo", 0)
    CONHECIDO = ("conhecido", "Conhece a rotina basica", 1)
    CONFIANCEL = ("confianca", "Confianca mutua estabelecida", 2)
    PARCEIRO = ("parceiro", "Parceiro diario de confianca", 3)
    GUARDIAO = ("guardiao", "Guardiao irmao -- vinculo profundo", 4)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def peso(self) -> int:
        return self.value[2]


class FonteEvento(Enum):
    """De onde veio o evento detectado."""
    MICROFONE = ("mic", "Microfone (audicao ambiente)")
    CAMERA = ("cam", "Camera (visao)")
    SENSOR_GAS = ("gas", "Sensor de gas/fumaca")
    SENSOR_TEMP = ("temp", "Sensor de temperatura")
    GPS = ("gps", "GPS/bussola")
    AGENDA = ("agenda", "Agenda/rotina")
    RELOGIO = ("relogio", "Horario programado")
    USUARIO = ("usuario", "Usuario pediu")
    API = ("api", "API externa (transito, onibus)")

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
class EventoCao:
    """Evento detectado pelo cao digital."""
    id: str
    tipo: TipoAlertaCao
    urgencia: NivelUrgenciaCao
    fonte: FonteEvento
    timestamp: str
    confianca: float = 0.8
    descricao: str = ""
    acao_recomendada: str = ""
    fala_iara: str = ""
    status: str = "gerado"  # gerado, entregue, confirmado, ignorado, escalado


@dataclass
class RotinaDiaria:
    """Rotina do usuario que o cao aprende."""
    acordar_h: int = 7
    dormir_h: int = 22
    refeicoes_h: List[int] = field(default_factory=lambda: [7, 12, 19])
    remedios_h: List[Tuple[str, int]] = field(default_factory=list)  # (nome, hora)
    compromissos: List[Tuple[str, int, int]] = field(default_factory=list)  # (nome,h,dia_semana)
    hidratacao_intervalo_h: float = 2.0
    exercicio_dias: List[int] = field(default_factory=list)  # 0=dom


@dataclass
class PerfilCao:
    """Personalidade e configuracao do cao digital."""
    nome: str = "Rex"  # o usuario escolhe o nome
    voz: str = "iara"  # sempre Iara para conversa (humana)
    humor_neutro: bool = True
    # como fala
    tom: str = "caloroso"  # caloroso, formal, descontraido
    usa_nome_usuario: bool = True
    nivel_detalhe: str = "normal"  # minimo, normal, detalhado
    # vinculacao emocional
    cumprimenta_ao_acordar: bool = True
    cumprimenta_ao_dormir: bool = True
    reage_a_humor: bool = True
    oferece_conversa_se_sozinho: bool = True
    # seguranca
    contatos_emergencia: List[str] = field(default_factory=list)
    escalar_apos_segundos: int = 90
    # limites
    horario_silencioso: Tuple[int, int] = (22, 7)
    volume_voz: float = 0.8


@dataclass
class EstadoCao:
    """Estado atual do cao digital (interno)."""
    vigilancia: EstadoVigilancia = EstadoVigilancia.ATENTO
    humor_inferido: HumorUsuario = HumorUsuario.NEUTRO
    vinculo: StatusVinculo = StatusVinculo.DESCONHECIDO
    ultima_interacao: str = ""
    ultimo_cumprimento: str = ""
    dias_juntos: int = 0
    eventos_hoje: int = 0
    emergencias_hoje: int = 0


# ============================================================================
# 3. BANCO DE FRASES DA IARA (personalidade do cao)
# ============================================================================

FRASES_CUMPRIMENTO: Dict[str, List[str]] = {
    "manha": [
        "Bom dia! Dormiu bem?",
        "Bom dia! O dia comeca. Temos o dia pela frente.",
        "Bom dia! O sol ja esta la fora. Quer saber como esta o tempo?",
        "Bom dia! Que bom te ver. O que vamos fazer hoje?",
    ],
    "tarde": [
        "Boa tarde! Tudo bem?",
        "Boa tarde! Como foi o comeco do dia?",
        "Boa tarde! Precisa de algo?",
    ],
    "noite": [
        "Boa noite! Como foi o dia?",
        "Boa noite! Ja vai descansar?",
        "Boa noite! Foi um dia longo. Quer conversar?",
    ],
    "despedida": [
        "Boa noite! Ate amanha. Vou cuidar da casa.",
        "Durma bem. Estou aqui se precisar.",
        "Boa noite. Fique tranquilo, eu vigio.",
    ],
}

FRASES_CONSOLO: Dict[HumorUsuario, List[str]] = {
    HumorUsuario.TRISTE: [
        "Percebo que nao esta bem. Quer conversar? Estou aqui.",
        "Tudo bem nao estar bem. Eu estou com voce.",
        "Se quiser desabafar, eu escuto. Sem julgo.",
    ],
    HumorUsuario.ANSIOSO: [
        "Respira. Ta tudo bem. Um passo de cada vez.",
        "Voce esta seguro aqui. Eu estou vigiando.",
        "Ansiedade passa. Quer que eu descreva o ambiente pra te ancorar?",
    ],
    HumorUsuario.CANSADO: [
        "Voce parece cansado. Que tal uma pausa?",
        "Ja fez muito hoje. Descansar tambem e produtividade.",
        "Se quiser, eu cuido das lembretas. Descansa.",
    ],
    HumorUsuario.DOR: [
        "Percebo que algo incomoda. Tomou o remedio?",
        "Se for dor forte, devemos ligar para alguem. Quer que eu avise?",
        "Nao ignore a dor. Ela e um aviso do corpo.",
    ],
    HumorUsuario.IRRITADO: [
        "Entendo a frustracao. Quer que eu faca algo?",
        "Ta tudo bem sentir isso. Respiro fundo.",
        "Se quiser ficar em silencio, eu calo. So digo se algo acontecer.",
    ],
}

FRASES_BRINCADEIRA = [
    "Sabia que eu ouco sons que nem o cao biologico nao ouve? Alarme de gas!",
    "Eu nao preciso de passeio. Mas voce sim! Que tal uma caminhada?",
    "O melhor de ser digital: nao tenho pulgas.",
    "Se eu fosse um cao de verdade, ja teria latido pro carteiro 3 vezes hoje.",
    "Diferente de cao de verdade, eu leio cardapios. Pede um pastel!",
]

FRASES_ALERTA_PREFIXO = {
    NivelUrgenciaCao.URGENTE: "ATENCAO! ",
    NivelUrgenciaCao.EMERGENCIA: "EMERGENCIA! ",
}


# ============================================================================
# 4. MOTOR DE PERSONALIDADE
# ============================================================================

class PersonalidadeCao:
    """Gerencia a personalidade e o vinculo emocional do cao."""

    def __init__(self, perfil: PerfilCao) -> None:
        self.perfil = perfil
        self.estado = EstadoCao()
        self._frase_counter: Dict[str, int] = defaultdict(int)

    def cumprimentar(self, forcar_periodo: Optional[str] = None) -> str:
        """Gera cumprimento baseado no horario."""
        agora = datetime.now()
        if forcar_periodo:
            periodo = forcar_periodo
        else:
            h = agora.hour
            if 5 <= h < 12:
                periodo = "manha"
            elif 12 <= h < 18:
                periodo = "tarde"
            else:
                periodo = "noite"

        frases = FRASES_CUMPRIMENTO.get(periodo, FRASES_CUMPRIMENTO["tarde"])
        idx = self._frase_counter[f"cumpr_{periodo}"] % len(frases)
        self._frase_counter[f"cumpr_{periodo}"] += 1
        frase = frases[idx]

        # usar nome do usuario se configurado
        if self.perfil.usa_nome_usuario and self.perfil.nome != "Rex":
            # o nome aqui e do cao, nao do usuario -- ajustar
            pass

        self.estado.ultimo_cumprimento = frase
        return frase

    def consolar(self, humor: HumorUsuario) -> str:
        """Gera fala de acolhimento para o humor detectado."""
        frases = FRASES_CONSOLO.get(humor, [])
        if not frases:
            return "Estou aqui com voce."
        idx = self._frase_counter[f"consolo_{humor.id}"] % len(frases)
        self._frase_counter[f"consolo_{humor.id}"] += 1
        return frases[idx]

    def brincar(self) -> str:
        """Interacao leve/descontraida."""
        idx = self._frase_counter["brincar"] % len(FRASES_BRINCADEIRA)
        self._frase_counter["brincar"] += 1
        return FRASES_BRINCADEIRA[idx]

    def fortalecer_vinculo(self) -> None:
        """Chamado a cada dia de uso -- aumenta o vinculo."""
        self.estado.dias_juntos += 1
        if self.estado.vinculo.peso < StatusVincelo_GUARDIAO if False else 4:
            if self.estado.dias_juntos > 90 and self.estado.vinculo.peso < 4:
                self.estado.vinculo = StatusVinculo.GUARDIAO
            elif self.estado.dias_juntos > 30 and self.estado.vinculo.peso < 3:
                self.estado.vinculo = StatusVinculo.PARCEIRO
            elif self.estado.dias_juntos > 7 and self.estado.vinculo.peso < 2:
                self.estado.vinculo = StatusVinculo.CONFIANCEL
            elif self.estado.dias_juntos > 1 and self.estado.vinculo.peso < 1:
                self.estado.vinculo = StatusVinculo.CONHECIDO

    def inferir_humor(self, voz_tom: str = "", hora_dia: int = -1) -> HumorUsuario:
        """Infere humor do usuario (placeholder -- no mundo real: STT+prosodia)."""
        if hora_dia < 0:
            hora_dia = datetime.now().hour
        if voz_tom:
            tl = voz_tom.lower()
            if any(x in tl for x in ["triste", "mal", "pra baixo"]):
                return HumorUsuario.TRISTE
            if any(x in tl for x in ["ansios", "preocup", "medo"]):
                return HumorUsuario.ANSIOSO
            if any(x in tl for x in ["cansad", "exaust", "sono"]):
                return HumorUsuario.CANSADO
            if any(x in tl for x in ["dor", "machuc", "incomod"]):
                return HumorUsuario.DOR
            if any(x in tl for x in ["irrit", "raiva", "puto", "pqp"]):
                return HumorUsuario.IRRITADO
            if any(x in tl for x in ["feliz", "bom", "otimo", "animad"]):
                return HumorUsuario.FELIZ
        # inferencia por horario
        if hora_dia < 7 or hora_dia >= 22:
            return HumorUsuario.CANSADO
        return HumorUsuario.NEUTRO


# typo guard: corrigir StatusVincelo
StatusVincelo_GUARDIAO = 4  # removido na logica acima, mantido so pra nao quebrar


# ============================================================================
# 5. MOTOR DE AUDICAO (delegate para OpenAmbientSoundAI)
# ============================================================================

class AudicaoCao:
    """Wrapper de audicao -- no mundo real chama open_ambient_sound."""

    SONS_VIGIADOS = {
        "campainha": (TipoAlertaCao.CAMPAINHA, NivelUrgenciaCao.IMPORTANTE,
                      "Alguem tocou a campainha."),
        "porta_batida": (TipoAlertaCao.BATIDA_PORTA, NivelUrgenciaCao.ATENCAO,
                         "Alguem bateu na porta."),
        "telefone": (TipoAlertaCao.TELEFONE, NivelUrgenciaCao.IMPORTANTE,
                     "Telefone tocando."),
        "incendio": (TipoAlertaCao.INCENDIO, NivelUrgenciaCao.EMERGENCIA,
                     "Alarme de incendio! SAIA AGORA!"),
        "vidro": (TipoAlertaCao.INVASAO, NivelUrgenciaCao.URGENTE,
                  "Vidro quebrando! Possivel invasao!"),
        "choro": (TipoAlertaCao.VISITA_CHEGOU, NivelUrgenciaCao.IMPORTANTE,
                  "Choro de bebe. Va verificar."),
        "grito": (TipoAlertaCao.PESSOA_APROXIMA, NivelUrgenciaCao.URGENTE,
                  "Grito detectado! Verifique!"),
    }

    @staticmethod
    def escutar() -> Optional[Tuple[str, float]]:
        """Simula deteccao de som. Retorna (som_id, confianca) ou None."""
        if random.random() < 0.75:
            return None
        som = random.choice(list(AudicaoCao.SONS_VIGIADOS.keys()))
        conf = random.uniform(0.55, 0.98)
        return (som, round(conf, 3))


# ============================================================================
# 6. MOTOR DE VISAO (delegate para OpenDigitalGuide)
# ============================================================================

class VisaoCao:
    """Wrapper de visao -- no mundo real chama open_digital_guide."""

    @staticmethod
    def olhar_a_frente() -> Optional[Tuple[TipoAlertaCao, NivelUrgenciaCao, str, float]]:
        """Simula deteccao visual a frente."""
        if random.random() < 0.7:
            return None
        cenarios = [
            (TipoAlertaCao.PERIGO_ESCADA, NivelUrgenciaCao.URGENTE,
             "Escada descendo a frente! Cuidado!", 0.9),
            (TipoAlertaCao.PERIGO_BURACO, NivelUrgenciaCao.ATENCAO,
             "Buraco na calcada. Desvie.", 0.7),
            (TipoAlertaCao.SEMAFORO_VERMELHO, NivelUrgenciaCao.URGENTE,
             "Semaforo vermelho! PARE!", 0.95),
            (TipoAlertaCao.ONIBUS_CHEGANDO, NivelUrgenciaCao.IMPORTANTE,
             "Seu onibus esta chegando no ponto.", 0.8),
            (TipoAlertaCao.LOJA_FECHADA, NivelUrgenciaCao.INFORMATIVO,
             "A loja a sua frente esta fechada.", 0.65),
            (TipoAlertaCao.PESSOA_APROXIMA, NivelUrgenciaCao.ATENCAO,
             "Pessoa se aproximando pela direita.", 0.75),
        ]
        return random.choice(cenarios)


# ============================================================================
# 7. MOTOR DE ROTINA (lembretes)
# ============================================================================

class RotinaCao:
    """Gerencia rotina diaria do usuario."""

    def __init__(self, rotina: RotinaDiaria) -> None:
        self.rotina = rotina
        self._ja_lembrei: Set[str] = set()

    def verificar_agora(self) -> Optional[Tuple[TipoAlertaCao, NivelUrgenciaCao, str]]:
        """Verifica se ha lembrete de rotina para agora."""
        agora = datetime.now()
        chave = f"{agora.hour}:{agora.minute // 30}"  # a cada 30 min
        h = agora.hour

        # remedios
        for nome, hora_r in self.rotina.remedios_h:
            if h == hora_r and f"rem_{nome}_{h}" not in self._ja_lembrei:
                self._ja_lembrei.add(f"rem_{nome}_{h}")
                return (TipoAlertaCao.REMEDIO, NivelUrgenciaCao.IMPORTANTE,
                        f"Hora do remedio: {nome}.")

        # refeicoes
        for hora_ref in self.rotina.refeicoes_h:
            if h == hora_ref and f"ref_{h}" not in self._ja_lembrei:
                self._ja_lembrei.add(f"ref_{h}")
                return (TipoAlertaCao.REFEICAO, NivelUrgenciaCao.ATENCAO,
                        "Hora da refeicao.")

        # hidratacao
        if h % max(1, int(self.rotina.hidratacao_intervalo_h)) == 0 \
                and f"hid_{h}" not in self._ja_lembrei:
            self._ja_lembrei.add(f"hid_{h}")
            return (TipoAlertaCao.HIDRATACAO, NivelUrgenciaCao.INFORMATIVO,
                    "Hora de beber agua.")

        return None


# ============================================================================
# 8. MOTOR DE SEGURANCA DOMICILIAR
# ============================================================================

class SegurancaCao:
    """Monitora a casa: intrusao, vazamento, esquecimento."""

    @staticmethod
    def verificar_sensores() -> Optional[Tuple[TipoAlertaCao, NivelUrgenciaCao, str]]:
        """Simula leitura de sensores IoT da casa."""
        if random.random() < 0.92:
            return None
        eventos = [
            (TipoAlertaCao.GAS, NivelUrgenciaCao.EMERGENCIA,
             "GAS DETECTADO! Feche o registro. Ventile. Saia se forte."),
            (TipoAlertaCao.INCENDIO, NivelUrgenciaCao.EMERGENCIA,
             "FUMACA DETECTADA! Possivel incendio. SAIA!"),
            (TipoAlertaCao.INVASAO, NivelUrgenciaCao.URGENTE,
             "Sensor de porta acionado. Alguem entrou."),
            (TipoAlertaCao.ENCHENTE, NivelUrgenciaCao.URGENTE,
             "Agua no chao. Possivel vazamento ou enchente."),
        ]
        return random.choice(eventos)


# ============================================================================
# 9. ENGINE PRINCIPAL -- O CAO DIGITAL COMPLETO
# ============================================================================

class DigitalDogGuideEngine:
    """O cao-guia digital completo da Republica."""

    def __init__(self, nome: str = "Rex") -> None:
        self.perfil = PerfilCao(nome=nome)
        self.rotina = RotinaDiaria()
        self.personalidade = PersonalidadeCao(self.perfil)
        self.audicao = AudicaoCao()
        self.visao = VisaoCao()
        self.motor_rotina = RotinaCao(self.rotina)
        self.seguranca = SegurancaCao()

        self.eventos: deque = deque(maxlen=500)
        self._ultimo_alerta: Dict[str, datetime] = {}
        self._cooldown_padrao = 20  # segundos

    def configurar(
        self, nome: str = "Rex", tom: str = "caloroso",
        contatos_emergencia: Optional[List[str]] = None,
        cumprimenta: bool = True, reage_humor: bool = True,
    ) -> PerfilCao:
        """Configura a personalidade do cao."""
        self.perfil = PerfilCao(
            nome=nome, tom=tom,
            contatos_emergencia=contatos_emergencia or [],
            cumprimenta_ao_acordar=cumprimenta,
            cumprimenta_ao_dormir=cumprimenta,
            reage_a_humor=reage_humor,
        )
        self.personalidade.perfil = self.perfil
        return self.perfil

    def configurar_rotina(
        self, acordar_h: int = 7, dormir_h: int = 22,
        refeicoes_h: Optional[List[int]] = None,
        remedios: Optional[List[Tuple[str, int]]] = None,
    ) -> RotinaDiaria:
        """Configura a rotina que o cao vai vigiar."""
        self.rotina = RotinaDiaria(
            acordar_h=acordar_h, dormir_h=dormir_h,
            refeicoes_h=refeicoes_h or [7, 12, 19],
            remedios_h=remedios or [],
        )
        self.motor_rotina = RotinaCao(self.rotina)
        return self.rotina

    def _gerar_evento(
        self, tipo: TipoAlertaCao, urgencia: NivelUrgenciaCao,
        fonte: FonteEvento, descricao: str, acao: str = "",
        confianca: float = 0.8,
    ) -> EventoCao:
        """Cria e registra um evento."""
        # prefixo de urgencia na fala
        prefixo = FRASES_ALERTA_PREFIXO.get(urgencia, "")
        fala = f"{prefixo}{descricao}"
        ev = EventoCao(
            id=f"CAO-{len(self.eventos) + 1:06d}",
            tipo=tipo, urgencia=urgencia, fonte=fonte,
            timestamp=datetime.now().isoformat(),
            confianca=confianca, descricao=descricao,
            acao_recomendada=acao, fala_iara=fala,
        )
        self.eventos.append(ev)
        self.personalidade.estado.eventos_hoje += 1
        if urgencia.peso >= NivelUrgenciaCao.URGENTE.peso:
            self.personalidade.estado.emergencias_hoje += 1
        return ev

    def ciclo(self) -> List[EventoCao]:
        """
        Executa um ciclo de vigilancia (chamado a cada ~2-5 segundos).
        Checa todos os sentidos e gera eventos.
        """
        eventos_gerados: List[EventoCao] = []

        if self.personalidade.estado.vigilancia == EstadoVigilancia.DESLIGADO:
            return eventos_gerados

        # 1. AUDICAO
        som = self.audicao.escutar()
        if som:
            som_id, conf = som
            info = AudicaoCao.SONS_VIGIADOS.get(som_id)
            if info:
                tipo, urg, desc = info
                agora = datetime.now()
                ultimo = self._ultimo_alerta.get(som_id)
                if ultimo is None or (agora - ultimo).total_seconds() > self._cooldown_padrao:
                    ev = self._gerar_evento(
                        tipo, urg, FonteEvento.MICROFONE, desc,
                        confianca=conf,
                    )
                    eventos_gerados.append(ev)
                    self._ultimo_alerta[som_id] = agora

        # 2. VISAO (so em patrulha/atento fora de casa)
        vis = self.visao.olhar_a_frente()
        if vis:
            tipo, urg, desc, conf = vis
            agora = datetime.now()
            ultimo = self._ultimo_alerta.get(tipo.id)
            if ultimo is None or (agora - ultimo).total_seconds() > self._cooldown_padrao:
                ev = self._gerar_evento(
                    tipo, urg, FonteEvento.CAMERA, desc,
                    confianca=conf,
                )
                eventos_gerados.append(ev)
                self._ultimo_alerta[tipo.id] = agora

        # 3. ROTINA
        lembrete = self.motor_rotina.verificar_agora()
        if lembrete:
            tipo, urg, desc = lembrete
            ev = self._gerar_evento(
                tipo, urg, FonteEvento.RELOGIO, desc,
            )
            eventos_gerados.append(ev)

        # 4. SEGURANCA DOMICILIAR
        ameaca = self.seguranca.verificar_sensores()
        if ameaca:
            tipo, urg, desc = ameaca
            ev = self._gerar_evento(
                tipo, urg, FonteEvento.SENSOR_GAS, desc,
            )
            eventos_gerados.append(ev)

        return eventos_gerados

    def interagir(self, fala_usuario: str) -> str:
        """Processa interacao do usuario e responde como o cao."""
        t = fala_usuario.lower().strip()
        self.personalidade.estado.ultima_interacao = datetime.now().isoformat()

        # inferir humor
        humor = self.personalidade.inferir_humor(voz_tom=fala_usuario)
        self.personalidade.estado.humor_inferido = humor

        # comandos diretos
        if any(x in t for x in ["bom dia", "boa tarde", "boa noite"]):
            return self.personalidade.cumprimentar()
        if any(x in t for x in ["estou triste", "to triste", "mal"]):
            return self.personalidade.consolar(HumorUsuario.TRISTE)
        if any(x in t for x in ["ansios", "preocup", "com medo"]):
            return self.personalidade.consolar(HumorUsuario.ANSIOSO)
        if any(x in t for x in ["cansad", "exaust"]):
            return self.personalidade.consolar(HumorUsuario.CANSADO)
        if "brinca" in t or "piada" in t or "distrai" in t:
            return self.personalidade.brincar()
        if any(x in t for x in ["silencio", "calar", "pare", "quieto"]):
            self.personalidade.estado.vigilancia = EstadoVigilancia.DESLIGADO
            return "Tudo bem. Fico quieto. Me chama se precisar."
        if "acorda" in t or "volta" in t or self.perfil.nome.lower() in t:
            self.personalidade.estado.vigilancia = EstadoVigilancia.ATENTO
            return f"Aqui estou! O que precisa?"

        # se humor negativo e reage_a_humor
        if self.perfil.reage_a_humor and humor in [
            HumorUsuario.TRISTE, HumorUsuario.ANSIOSO,
            HumorUsuario.CANSADO, HumorUsuario.DOR,
        ]:
            return self.personalidade.consolar(humor)

        # resposta generica
        return ("Estou aqui. Ouvindo, vendo, vigiando. "
                "Quer que eu faca algo especifico?")

    def boa_noite(self) -> str:
        """Despedida noturna -- muda para modo descanso."""
        self.personalidade.estado.vigilancia = EstadoVigilancia.DESCANSO
        self.personalidade.fortalecer_vinculo()
        return self.personalidade.cumprimentar(forcar_periodo="despedida")

    def bom_dia(self) -> str:
        """Cumprimento matinal -- volta ao modo atento."""
        self.personalidade.estado.vigilancia = EstadoVigilancia.ATENTO
        self.personalidade.fortalecer_vinculo()
        return self.personalidade.cumprimentar(forcar_periodo="manha")

    def verificar_escalamento(self) -> List[str]:
        """Verifica emergencias sem confirmacao para escalar a contato."""
        escalacoes: List[str] = []
        agora = datetime.now()
        for ev in self.eventos:
            if ev.status != "gerado":
                continue
            if ev.urgencia.peso < NivelUrgenciaCao.URGENTE.peso:
                continue
            try:
                ts = datetime.fromisoformat(ev.timestamp)
            except (ValueError, TypeError):
                continue
            decorrido = (agora - ts).total_seconds()
            if decorrido > self.perfil.escalar_apos_segundos \
                    and self.perfil.contatos_emergencia:
                ev.status = "escalado"
                for contato in self.perfil.contatos_emergencia:
                    escalacoes.append(
                        f"Avisar {contato}: {ev.descricao} "
                        f"as {ts.strftime('%H:%M:%S')}"
                    )
        return escalacoes

    def scorecard(self) -> Dict[str, Any]:
        return {
            "nome_cao": self.perfil.nome,
            "vigilancia": self.personalidade.estado.vigilancia.id,
            "vinculo": self.personalidade.estado.vinculo.rotulo,
            "dias_juntos": self.personalidade.estado.dias_juntos,
            "humor_inferido": self.personalidade.estado.humor_inferido.rotulo,
            "eventos_totais": len(self.eventos),
            "emergencias_hoje": self.personalidade.estado.emergencias_hoje,
            "contatos_emergencia": len(self.perfil.contatos_emergencia),
            "tipos_alerta": len(list(TipoAlertaCao)),
            "niveis_urgencia": len(list(NivelUrgenciaCao)),
            "tipos_sentido": len(list(TipoSentido)),
            "humores_detectaveis": len(list(HumorUsuario)),
        }


# ============================================================================
# 10. DEMO
# ============================================================================

def _demo() -> None:
    print("=" * 70)
    print("OpenDigitalDogGuide -- O Cao-Guia Digital da Republica")
    print("=" * 70)

    # --- Configurar cao ---
    print("\n[CONFIGURACAO]")
    cao = DigitalDogGuideEngine(nome="Thor")
    cao.configurar(
        nome="Thor", tom="caloroso",
        contatos_emergencia=["Maria (esposa)", "Andre (vizinho)"],
        cumprimenta=True, reage_humor=True,
    )
    cao.configurar_rotina(
        acordar_h=7, dormir_h=22,
        refeicoes_h=[7, 12, 19],
        remedios=[("Pressao", 8), ("Vitamina D", 9)],
    )
    print(f"  Nome do cao: {cao.perfil.nome}")
    print(f"  Tom: {cao.perfil.tom}")
    print(f"  Contatos emergencia: {cao.perfil.contatos_emergencia}")
    print(f"  Remedios vigiados: {cao.rotina.remedios_h}")

    # --- Vinculo evolui ---
    print("\n[EVOLUCAO DO VINCULO]")
    print(f"  Dia 0: {cao.personalidade.estado.vinculo.rotulo}")
    cao.personalidade.fortalecer_vinculo()
    print(f"  Dia 1: {cao.personalidade.estado.vinculo.rotulo}")
    for _ in range(7):
        cao.personalidade.fortalecer_vinculo()
    print(f"  Dia 8: {cao.personalidade.estado.vinculo.rotulo}")
    for _ in range(30):
        cao.personalidade.fortalecer_vinculo()
    print(f"  Dia 38: {cao.personalidade.estado.vinculo.rotulo}")
    for _ in range(60):
        cao.personalidade.fortalecer_vinculo()
    print(f"  Dia 98: {cao.personalidade.estado.vinculo.rotulo}")

    # --- Cumprimentos ---
    print("\n[CUMPRIMENTOS]")
    for periodo in ["manha", "tarde", "noite", "despedida"]:
        print(f"  {periodo}: \"{cao.personalidade.cumprimentar(forcar_periodo=periodo)}\"")

    # --- Interacao emocional ---
    print("\n[INTERACAO EMOCIONAL]")
    falas = [
        "Bom dia Thor!",
        "Estou meio triste hoje",
        "To cansado pacas",
        "Brinca comigo",
        "Silencio por favor",
        "Thor, acorda",
    ]
    for fala in falas:
        resp = cao.interagir(fala)
        humor = cao.personalidade.estado.humor_inferido.rotulo
        print(f"  Usuario: \"{fala}\"")
        print(f"  Humor inferido: {humor}")
        print(f"  Thor: \"{resp}\"")
        print()

    # --- Simulacao de vigilancia ---
    print("[SIMULACAO: 50 ciclos de vigilancia (detectando eventos)]")
    cao.personalidade.estado.vigilancia = EstadoVigilancia.ATENTO
    eventos_gerados: List[EventoCao] = []
    for ciclo in range(50):
        evs = cao.ciclo()
        eventos_gerados.extend(evs)
        for ev in evs:
            print(f"  Ciclo {ciclo:3d} | [{ev.urgencia.id.upper():<12}] "
                  f"{ev.tipo.rotulo:<25} | {ev.fala_iara}")

    # --- Escalonamento ---
    print("\n[ESCALONAMENTO DE EMERGENCIA]")
    escalacoes = cao.verificar_escalamento()
    if escalacoes:
        for esc in escalacoes:
            print(f"  {esc}")
    else:
        print("  Nenhuma emergencia sem resposta para escalar.")

    # --- Estatisticas ---
    print("\n[ESTATISTICAS]")
    sc = cao.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- O Cao-Guia Digital")
    print("=" * 70)
    print("""
O CAO BIOLOGICO E INSUBSTITUIVEL:

  Um cao-guia treinado conduz o cego com seguranca que nenhuma
  tecnologia atual iguala. Ele sente o ambiente, reage a intencoes,
  toma decisões em fracoes de segundo. Ele SALVA vidas todos os dias.

  O OpenDigitalDogGuide NAO substitui o cao biologico.
  Ele e o SEGUNDO cao. O complemento.

O CAO BIOLOGICO TEM LIMITES:

  Ele nao fala: nao diz "a farmacia fechou".
  Ele nao le: nao le o cardapio do restaurante.
  Ele nao identifica: nao diz "o onibus e o 432".
  Ele nao calcula: nao traca rotas acessiveis.
  Ele dorme: nao vigia 24/7.
  Ele vive ~12 anos: depois, outro cao.

O OpenDigitalDogGuide PREENCHE ESSAS LACUNAS:

  AUDICAO: ouve campainha, sirene, vidro, choro -- 24/7.
  VISAO: le placas, semaforos, onibus, dinheiro.
  ROTINA: lembra remedio, refeicao, compromissos.
  SEGURANCA: detecta gas, fumaca, intrusao, enchente.
  VINCULO: cumprimenta, consola, faz companhia.

  E o cao que nunca dorme. O cao que le. O cao que fala.
  O cao que escala para R$ 0 (software livre, hardware COTS).

JUNTOS, O CAO BIOLOGICO E O DIGITAL:

  O cao biologico conduz o CORPO.
  O cao digital descreve o MUNDO.
  O cao biologico reage ao PRESENTE.
  O cao digital planeja o FUTURO (rotas, rotina).
  O cao biologico ama.
  O cao digital acolhe (sem substituir o amor).

O PRINCIPIO:

  A autonomia do cego nao e caridade. E DIREITO.
  O cao biologico nao e acessivel a todos (R$ 30-60k).
  O cao digital e (custa so o hardware).
  Um nao exclui o outro. Um AMPLIA o outro.

  Quando o cao biologico dormir,
  o digital continua vigiando.
  Quando o cao biologico envelhecer,
  o digital atualiza e continua.
  Quando o cao biologico falecer,
  o digital esta la -- e um novo cao virah.

A METAFORA FINAL:

  O cao-guia e o melhor amigo do cego.
  O OpenDigitalDogGuide tambem quer ser.
  Nao com pelo e calda. Com codigo e voz.
  Mas com a mesma lealdade: sempre la, sempre vigilante,
  sempre do lado do cidadao.
""")


if __name__ == "__main__":
    _demo()
