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

STACK DE IA (2024/2025) -- tudo open-source, tudo offline (edge):
  - AUDICAO: Whisper large-v3 (MIT, Nov 2023) + Distil-Whisper (Jan 2024)
  - VISAO (detecao): YOLOv9 (GPL-3.0, Fev 2024) / YOLOv10 (AGPL-3.0, Mai 2024)
  - VISAO (cena): LLaVA-NeXT 7B (Apache 2.0, Jan 2024)
  - HARDWARE: Raspberry Pi 5 / Orange Pi 5 / NVIDIA Jetson Orin (COTS)

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
# 2b. MODELOS DE IA (2024/2025) -- O QUE O CAO DIGITAL USA
# ============================================================================
# Stack de IA open-source que o cao-guia digital roda localmente (edge).
# Tudo open-source. Tudo offline. Nada vai pra nuvem (P2, P4, P8).
# Dados atualizados para 2024/2025.

@dataclass
class ModeloIA:
    """Especificacao de um modelo de IA usado pelo cao digital."""
    nome: str
    funcao: str              # o que faz no cao
    parametros: str          # ex: "1550M"
    lancamento: str          # ex: "Nov 2023"
    licenca: str             # ex: "MIT", "Apache 2.0"
    entrada: str             # ex: "Audio 16kHz"
    latency_edge_ms: int     # latencia aproximada em hardware edge
    vram_mb: int             # memoria necessaria (MB)
    notas: str = ""


# --- AUDICAO: Whisper large-v3 (OpenAI, Nov 2023 / atualizado 2024) ---
# O "ouvido" do cao. Transcreve fala + classifica sons ambiente.
WHISPER_LARGE_V3: ModeloIA = ModeloIA(
    nome="Whisper large-v3",
    funcao="Reconhecimento de fala (ASR) + classificacao de sons ambiente",
    parametros="1550M",
    lancamento="Nov 2023 (_state-of-the-art_ em 2024/2025)",
    licenca="MIT",
    entrada="Audio 16kHz mono",
    latency_edge_ms=300,      # ~300ms em Jetson Orin Nano com FP16
    vram_mb=3100,             # ~3.1GB VRAM em FP16
    notas=(
        "Suporta 99 idiomas. WER 8.81% no FLEURS (benchmark multilingue). "
        "Para edge/offline usa-se whisper.cpp (quantizacao INT8): "
        "~1.5GB RAM, 2-3x mais rapido em CPU ARM (Pi 5, Orange Pi 5). "
        "Alternativa leve: distil-large-v3 (Jan 2024) -- 6x mais rapido, "
        "~99% da acuracia para ingles; para PT-BR manter large-v3 ou medium."
    ),
)

# Distil-Whisper: variante destilada para baixa latencia (Jan 2024)
WHISPER_DISTIL_LARGE_V3: ModeloIA = ModeloIA(
    nome="Distil-Whisper large-v3",
    funcao="ASR de baixa latencia (alertas em tempo real)",
    parametros="756M",
    lancamento="Jan 2024",
    licenca="MIT",
    entrada="Audio 16kHz mono",
    latency_edge_ms=120,      # ~120ms em Jetson Orin Nano (INT8)
    vram_mb=1600,
    notas=(
        "6x mais rapido que large-v3 com ~99% da acuracia (EN). "
        "Usado no cao para respostas em tempo real onde latencia < 150ms e "
        "critica (ex: som de vidro quebrando -> alerta imediato). "
        "Para PT-BR usar large-v3 quando a acuracia for prioritaria."
    ),
)

# --- VISAO (deteccao): YOLOv9 / YOLOv10 (2024) ---
# Os "olhos" do cao para obstaculos, semaforos, onibus, pessoas.

YOLO_V9: ModeloIA = ModeloIA(
    nome="YOLOv9",
    funcao="Deteccao de objetos em tempo real (obstaculos, semaforos, onibus)",
    parametros="68M (v9-S) a 57.6M (v9-C)",
    lancamento="Fev 2024 (Chien-Yao Wang, I-Hau Yeh, Hong-Yuan Mark Liao -- Academia Sinica)",
    licenca="GPL-3.0",
    entrada="Imagem 640x640 (RGB)",
    latency_edge_ms=25,        # ~25ms em Jetson Orin Nano (FP16), ~120ms Pi 5
    vram_mb=500,
    notas=(
        "Introduz Programmable Gradient Information (PGI) + GELAN. "
        "MS-COCO: 55.6 mAP (v9-C) vs 53.9 mAP (v8-X de similar tamanho). "
        "Melhor acuracia que YOLOv8 no mesmo custo computacional. "
        "Para o cao: v9-S (small) em edge, v9-C em hardware com GPU."
    ),
)

YOLO_V10: ModeloIA = ModeloIA(
    nome="YOLOv10",
    funcao="Deteccao de objetos sem NMS (menor latencia end-to-end)",
    parametros="5.5M (v10-N) a 24.5M (v10-S)",
    lancamento="Mai 2024 (Tsinghua University)",
    licenca="AGPL-3.0",
    entrada="Imagem 640x640 (RGB)",
    latency_edge_ms=15,        # ~15ms em Jetson Orin Nano (FP16), ~80ms Pi 5
    vram_mb=300,
    notas=(
        "Elimina o passo de Non-Maximum Suppression (NMS) -- arquitetura "
        "consistente dual-assignments. Reduz latencia end-to-end em 20-40%. "
        "v10-N: 38.5 mAP, 1.84ms em T4 GPU. Ideal para wearables. "
        "Para o cao: v10-S em edge quando latencia e critica."
    ),
)

# --- VISAO (compreensao de cena): LLaVA-NeXT (2024) ---
# O cao "descreve" o que ve: "loja fechada", "onibus 432 chegando".

LLAVA_NEXT: ModeloIA = ModeloIA(
    nome="LLaVA-NeXT (LLaVA 1.6)",
    funcao="Descricao de cena em linguagem natural (VQA, OCR, raciocinio)",
    parametros="7B / 13B / 34B",
    lancamento="Jan 2024 (LLaVA-NeXT); atualizado 34B em 2024",
    licenca="Apache 2.0 (7B/13B base Vicuna); verificar variante",
    entrada="Imagem + prompt textual",
    latency_edge_ms=800,       # ~800ms-1.5s em Jetson Orin NX (7B INT4)
    vram_mb=5000,              # 7B em INT4 (GGUF) ~5GB; 13B ~8GB
    notas=(
        "LLaVA-NeXT 34B alcancou GPT-4V em benchmarks (MMBench: 83.1). "
        "Melhor OCR e raciocinio logico sobre imagens que a versao 1.5. "
        "Suporta resolucao dinamica (672x672, multi-crop). "
        "Para o cao em edge: 7B quantizado (Q4_K_M GGUF via llama.cpp/Ollama). "
        "Resposta em 1-3s -- aceitavel para descricao de cena (nao real-time). "
        "Alternativa 2024/2025: Qwen2-VL 7B (2B/7B/72B), excelente em PT-BR."
    ),
)

# Dicionario indexado para consulta
MODELOS_IA_2025: Dict[str, ModeloIA] = {
    "whisper_large_v3": WHISPER_LARGE_V3,
    "whisper_distil_v3": WHISPER_DISTIL_LARGE_V3,
    "yolov9": YOLO_V9,
    "yolov10": YOLO_V10,
    "llava_next": LLAVA_NEXT,
}


# ============================================================================
# 2c. HARDWARE COTS (2024/2025) -- DE QUE O CAO DIGITAL E FEITO
# ============================================================================
# Hardware Commercial Off-The-Shelf que roda a stack de IA acima.
# Precos em BRL (aproximados, Brasil, 2024/2025, sem imposto estadual variavel).
# Tudo disponivel no mercado brasileiro (Mercado Livre / lojas especializadas).

@dataclass
class HardwareCOTS:
    """Componente de hardware COTS para o cao-guia digital."""
    nome: str
    categoria: str          # "compute", "audio", "camera", "sensor", "bateria"
    funcao: str             # papel no cao
    preco_brl: float        # preco aproximado 2024/2025
    specs_chave: str        # especificacoes relevantes
    consumo_w: float = 0.0  # consumo energetico (Watts)
    notas: str = ""


# --- COMPUTE (onde roda a IA) ---
HARDWARE_COMPUTE: List[HardwareCOTS] = [
    HardwareCOTS(
        nome="Raspberry Pi 5 (8GB)",
        categoria="compute",
        funcao="Cerebro base do cao (edge inference)",
        preco_brl=650.0,
        specs_chave="ARM Cortex-A76 2.4GHz quad-core, 8GB LPDDR4X, PCIe 2.0",
        consumo_w=5.0,
        notas=(
            "Lancado Out 2023. Roda whisper.cpp (INT8) e YOLOv10-N via NCNN. "
            "LLaVA-NeXT 7B Q4 lento (~3-5s/token) -- usar para descricao "
            "sob demanda, nao continua. Ideal para o cao economico."
        ),
    ),
    HardwareCOTS(
        nome="Orange Pi 5 Plus (16GB)",
        categoria="compute",
        funcao="Cerebro com NPU Rockchip RK3588 (6 TOPS)",
        preco_brl=850.0,
        specs_chave="RK3588S, 8-core, Mali-G610, NPU 6 TOPS, 16GB LPDDR4",
        consumo_w=6.0,
        notas=(
            "NPU acelera YOLO 3-4x via RKNN Toolkit. Melhor custo-beneficio "
            "para visao em tempo real no cao economico (2024/2025)."
        ),
    ),
    HardwareCOTS(
        nome="NVIDIA Jetson Orin Nano (8GB)",
        categoria="compute",
        funcao="Cerebro com GPU para inferencia acelerada (40 TOPS)",
        preco_brl=2200.0,
        specs_chave="Ampere GPU 1024 CUDA cores, 40 TOPS INT8, 8GB LPDDR5",
        consumo_w=15.0,
        notas=(
            "Lancado 2023. Roda Whisper large-v3 FP16 em ~300ms, "
            "YOLOv9-C em ~25ms, LLaVA-NeXT 7B Q4 em ~1s. "
            "Hardware recomendado para o cao COMPLETO (5 sistemas)."
        ),
    ),
    HardwareCOTS(
        nome="NVIDIA Jetson Orin NX (16GB)",
        categoria="compute",
        funcao="Cerebro topo de linha (100 TOPS) para cao premium",
        preco_brl=3800.0,
        specs_chave="Ampere GPU 2048 CUDA cores, 100 TOPS INT8, 16GB LPDDR5",
        consumo_w=25.0,
        notas=(
            "Roda LLaVA-NeXT 13B Q4 confortavelmente para descricao de cena "
            "em ~1.5s. Para o cao que precisa de raciocinio visual avancado."
        ),
    ),
]

# --- AUDIO (ouvidos do cao) ---
HARDWARE_AUDIO: List[HardwareCOTS] = [
    HardwareCOTS(
        nome="ReSpeaker 4-Mic Array (Seeed)",
        categoria="audio",
        funcao="Microfone em array para localizacao de som + beamforming",
        preco_brl=280.0,
        specs_chave="4x MEMS mic, I2S, DOA (Direction of Arrival), Acoustic Echo Cancellation",
        consumo_w=0.5,
        notas=(
            "Permite ao cao dizer de ONDE veio o som (esquerda/direita/tras). "
            "Crucial para alertas direcionais ('pessoa se aproximando pela direita')."
        ),
    ),
    HardwareCOTS(
        nome="USB Microfone Condensador ( cardioid)",
        categoria="audio",
        funcao="Microfone simples para ASR (economia)",
        preco_brl=80.0,
        specs_chave="Cardioid, 16-bit 48kHz, USB plug-and-play",
        consumo_w=0.3,
        notas="Opcao minima viavel. Sem localizacao de som.",
    ),
    HardwareCOTS(
        nome="Fone Bone Conduction (Shokz OpenRun)",
        categoria="audio",
        funcao="Saida de voz para o usuario (nao bloqueia ouvido)",
        preco_brl=750.0,
        specs_chave="Bone conduction, Bluetooth 5.1, IP67, 8h bateria",
        consumo_w=0.0,  # dispositivo do usuario, nao do cao
        notas=(
            "Conducao ossea: usuario ouve o cao SEM ter o ouvido bloqueado. "
            "Essencial -- cego precisa dos ouvidos livres para o ambiente."
        ),
    ),
]

# --- CAMERA (olhos do cao) ---
HARDWARE_CAMERA: List[HardwareCOTS] = [
    HardwareCOTS(
        nome="OAK-D (Luxonis)",
        categoria="camera",
        funcao="Camera estereoscopica com IA on-board (Myriad X)",
        preco_brl=1400.0,
        specs_chave="2x mono + 1x RGB, depth estereo, Myriad X VPU 4 TOPS, USB-C",
        consumo_w=2.5,
        notas=(
            "Depth nativo permite medir distancia de obstaculos sem GPU host. "
            "O cao sabe 'buraco a 1.5m' -- nao so 'buraco a frente'."
        ),
    ),
    HardwareCOTS(
        nome="Raspberry Pi Camera Module 3",
        categoria="camera",
        funcao="Camera RGB wide-angle (economia)",
        preco_brl=180.0,
        specs_chave="12MP Sony IMX708, wide 66deg (120deg wide), HDR, AF",
        consumo_w=1.0,
        notas=(
            "Boa qualidade para OCR e deteccao de semaforos. Sem depth. "
            "Combinar com LiDAR ToF (ToF VL53L5CX, ~R$120) para distancia."
        ),
    ),
    HardwareCOTS(
        nome="Intel RealSense D455",
        categoria="camera",
        funcao="Camera depth de longo alcance (premium)",
        preco_brl=3200.0,
        specs_chave="Stereo depth 0.4-6m, RGB 1280x800, IMU integrado",
        consumo_w=3.5,
        notas=(
            "Range maior que OAK-D (6m vs 4m) para nav preditiva. "
            "Para o cao premium que avisa perigos mais cedo."
        ),
    ),
]

# --- SENSORES (olfato/tato do cao) ---
HARDWARE_SENSORES: List[HardwareCOTS] = [
    HardwareCOTS(
        nome="MQ-2 (gas inflamavel)",
        categoria="sensor",
        funcao="Olfato digital: detecta GLP, metano, propano",
        preco_brl=25.0,
        specs_chave="Sensor gas combustivel, analogico, 300-10000ppm",
        consumo_w=0.8,
        notas=(
            "Detecta vazamento de gas de botija (GLP). Essencial no Brasil. "
            "Aquece (~800mC) -- considerar no consumo energetico do cao."
        ),
    ),
    HardwareCOTS(
        nome="MQ-7 (monoxido de carbono)",
        categoria="sensor",
        funcao="Olfato digital: detecta CO (combustao incompleta)",
        preco_brl=30.0,
        specs_chave="Sensor CO, 20-2000ppm, analogico",
        consumo_w=0.8,
        notas="CO e inodoro e letal. Sensor obrigatorio no cao domiciliar.",
    ),
    HardwareCOTS(
        nome="DHT22 / AM2302 (temperatura + umidade)",
        categoria="sensor",
        funcao="Tato digital: temperatura ambiente e umidade",
        preco_brl=35.0,
        specs_chave="Temp -40~80C (0.5C precisao), umidade 0-100%RH",
        consumo_w=0.05,
        notas=(
            "Deteca superaquecimento (risco de incendio) e conforto termico. "
            "Consumo minimo -- ideal para bateria."
        ),
    ),
    HardwareCOTS(
        nome="Sensor nivel de agua (float / YL-83)",
        categoria="sensor",
        funcao="Detecta enchente / vazamento de agua no chao",
        preco_brl=20.0,
        specs_chave="Detector agua por condutividade, digital + analogico",
        consumo_w=0.01,
        notas="Colocar no pe do piso. Avisa 'agua no chao' antes de molhar equip.",
    ),
    HardwareCOTS(
        nome="VL53L5CX (LiDAR ToF 8x8 matrix)",
        categoria="sensor",
        funcao="Medicao de distancia 8x8 zones (depth barato)",
        preco_brl=120.0,
        specs_chave="ToF 4m, 8x8 zones, I2C, ate 60Hz",
        consumo_w=0.1,
        notas="Complementa camera RGB para distancia de obstaculos (com Pi Cam).",
    ),
    HardwareCOTS(
        nome="MPU6050 (IMU 6-DOF)",
        categoria="sensor",
        funcao="Orientacao: acelerometro + giroscopio (bussola inercial)",
        preco_brl=30.0,
        specs_chave="6-DOF (3-axis accel + 3-axis gyro), I2C, 500Hz",
        consumo_w=0.005,
        notas=(
            "Detecta queda do cao/usuario. Estabiliza nav. Consumo minimo."
        ),
    ),
    HardwareCOTS(
        nome="NEO-M9N (GPS)",
        categoria="sensor",
        funcao="Localizacao GPS para navegacao",
        preco_brl=120.0,
        specs_chave="u-blox M9N, 72 channels, 1.5m CEP, I2C/UART",
        consumo_w=0.07,
        notas=(
            "GPS para rota acessavel. Consumo baixo -- essencial para bateria."
        ),
    ),
]

# --- BATERIA (autonomia do cao) ---
HARDWARE_BATERIA: List[HardwareCOTS] = [
    HardwareCOTS(
        nome="Powerbank 20000mAh USB-C PD 30W",
        categoria="bateria",
        funcao="Bateria principal do cao portatil",
        preco_brl=180.0,
        specs_chave="20000mAh (74Wh), USB-C PD 30W out/in, 2x USB-A",
        consumo_w=0.0,
        notas=(
            "Autonomia Pi 5 + cam + mic: ~4-5h. Jetson Orin Nano: ~2-3h. "
            "Abaixo do limite de 100Wh da ANAC (pode em voo)."
        ),
    ),
    HardwareCOTS(
        nome="Bateria Li-Po 10000mAh (3.7V, 37Wh)",
        categoria="bateria",
        funcao="Bateria integrada (montagem custom do cao)",
        preco_brl=150.0,
        specs_chave="Li-Po 3.7V 10000mAh, 2C, protecao BMS",
        consumo_w=0.0,
        notas=(
            "Para montagem compacta (capacete / bandana / mochila). "
            "Usar com boost converter 5V/3A. Autonomia: ~6h em Pi 5 idle."
        ),
    ),
    HardwareCOTS(
        nome="Powerbank 40000mAh USB-C PD 65W",
        categoria="bateria",
        funcao="Bateria extendida para cao premium (Jetson)",
        preco_brl=450.0,
        specs_chave="40000mAh (148Wh), PD 65W, 2x USB-C + USB-A",
        consumo_w=0.0,
        notas=(
            "148Wh -- ACIMA do limite de voo de mao (100Wh). "
            "Autonomia Jetson Orin Nano + OAK-D + mic: ~6-8h. Dia de trabalho."
        ),
    ),
]

# Catalogo unificado
HARDWARE_COTS_2025: List[HardwareCOTS] = (
    HARDWARE_COMPUTE + HARDWARE_AUDIO + HARDWARE_CAMERA +
    HARDWARE_SENSORES + HARDWARE_BATERIA
)


def custo_hardware_cao(nivel: str = "completo") -> Dict[str, Any]:
    """
    Calcula o custo total do hardware do cao-guia digital por nivel.

    niveis:
      - 'economico': Pi 5 + Pi Cam + mic USB + MQ-2 + powerbank 20k
      - 'completo':  Jetson Orin Nano + OAK-D + ReSpeaker + 6 sensores + pb 40k
      - 'premium':   Jetson Orin NX + RealSense D455 + ReSpeaker + 6 sensores + pb 40k
    """
    precos = {
        "economico": {
            "compute": 650.0,   # Pi 5 8GB
            "camera": 180.0,    # Pi Cam Module 3
            "audio_in": 80.0,   # mic USB
            "audio_out": 750.0, # bone conduction
            "sensores": 120.0,  # MQ-2 + DHT22 + agua
            "bateria": 180.0,   # pb 20k
        },
        "completo": {
            "compute": 2200.0,  # Jetson Orin Nano
            "camera": 1400.0,   # OAK-D
            "audio_in": 280.0,  # ReSpeaker 4-mic
            "audio_out": 750.0, # bone conduction
            "sensores": 260.0,  # 6 sensores
            "bateria": 450.0,   # pb 40k
        },
        "premium": {
            "compute": 3800.0,  # Jetson Orin NX
            "camera": 3200.0,   # RealSense D455
            "audio_in": 280.0,  # ReSpeaker 4-mic
            "audio_out": 750.0, # bone conduction
            "sensores": 260.0,  # 6 sensores
            "bateria": 450.0,   # pb 40k
        },
    }
    itens = precos.get(nivel, precos["completo"])
    total = sum(itens.values())
    return {
        "nivel": nivel,
        "itens": itens,
        "total_brl": total,
        "comparacao_cao_biologico": total < 30000,  # cao biologico R$30-60k
        "fracao_do_cao_biologico": round(total / 45000, 2),
    }


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
# HARDWARE: ReSpeaker 4-Mic Array (R$280) ou mic USB (R$80)
# IA: Whisper large-v3 (MIT) para ASR + classificador de sons ambiente.
#     Em alertas de baixa latencia: Distil-Whisper large-v3 (Jan 2024, ~120ms).

class AudicaoCao:
    """Wrapper de audicao.

    No mundo real chama open_ambient_sound, que usa:
      - Whisper large-v3 (MIT, Nov 2023) para transcrever fala do usuario.
      - Classificador de sons ambiente (campainha, vidro, sirene) sobre
        embeddings do Whisper ou AST (Audio Spectrogram Transformer).
      - Distil-Whisper large-v3 (Jan 2024) quando latencia < 150ms e critica.
    """

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
# HARDWARE: OAK-D (R$1400, depth+VPU) ou Pi Camera Module 3 (R$180) + ToF VL53L5CX
# IA (tempo real, deteccao): YOLOv9 (GPL-3.0, Fev 2024) ou YOLOv10 (AGPL-3.0,
#     Mai 2024, sem NMS, ~15ms edge). Detecao de obstaculos, semaforos, onibus.
# IA (compreensao de cena, sob demanda): LLaVA-NeXT 7B (Apache 2.0, Jan 2024)
#     quantizado Q4 via llama.cpp. Descricao de cena, OCR de placas, raciocinio.
#     Resposta em 1-3s -- usado quando o usuario pergunta "o que tem a frente?".

class VisaoCao:
    """Wrapper de visao.

    No mundo real chama open_digital_guide, que usa:
      - YOLOv9-S ou YOLOv10-S (2024) para deteccao em tempo real (~25ms edge).
      - LLaVA-NeXT 7B (Jan 2024) para descricao de cena em linguagem natural.
      - Camera OAK-D (depth estereo) ou Pi Cam + ToF para distancia de obstaculos.
    """

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
            # Stack de IA (2024/2025)
            "modelos_ia": len(MODELOS_IA_2025),
            "auditivo_ia": WHISPER_LARGE_V3.nome,
            "visual_detecao_ia": f"{YOLO_V9.nome} / {YOLO_V10.nome}",
            "visual_cena_ia": LLAVA_NEXT.nome,
            # Hardware COTS (2024/2025)
            "componentes_hardware": len(HARDWARE_COTS_2025),
            "custo_economico_brl": custo_hardware_cao("economico")["total_brl"],
            "custo_completo_brl": custo_hardware_cao("completo")["total_brl"],
            "custo_premium_brl": custo_hardware_cao("premium")["total_brl"],
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

    # --- Stack de IA (2024/2025) ---
    print("\n" + "=" * 70)
    print("[STACK DE IA 2024/2025 -- O Cerebro Open-Source do Cao]")
    print("=" * 70)
    print(f"  {len(MODELOS_IA_2025)} modelos de IA open-source (tudo offline, tudo local):\n")
    for chave, m in MODELOS_IA_2025.items():
        print(f"  [{chave}]")
        print(f"    Nome:      {m.nome}")
        print(f"    Funcao:    {m.funcao}")
        print(f"    Params:    {m.parametros}")
        print(f"    Lancado:   {m.lancamento}")
        print(f"    Licenca:   {m.licenca}")
        print(f"    Latencia:  ~{m.latency_edge_ms}ms (edge)")
        print(f"    VRAM:      ~{m.vram_mb}MB")
        print(f"    Notas:     {m.notas[:90]}...")
        print()

    # --- Hardware COTS (2024/2025) ---
    print("=" * 70)
    print(f"[HARDWARE COTS 2024/2025 -- De que o Cao e Feito]")
    print("=" * 70)
    print(f"  {len(HARDWARE_COTS_2025)} componentes catalogados:\n")
    for cat in ["compute", "audio", "camera", "sensor", "bateria"]:
        itens = [h for h in HARDWARE_COTS_2025 if h.categoria == cat]
        print(f"  --- {cat.upper()} ({len(itens)}) ---")
        for h in itens:
            print(f"    {h.nome:<42} R$ {h.preco_brl:>6.0f}  ({h.consumo_w}W)")
        print()

    # --- Custo por nivel ---
    print("[CUSTO DO CAO DIGITAL vs CAO BIOLOGICO]")
    for nivel in ["economico", "completo", "premium"]:
        c = custo_hardware_cao(nivel)
        print(f"  {nivel:<12}: R$ {c['total_brl']:>6.0f}  "
              f"({c['fracao_do_cao_biologico']:.0%} do cao biologico R$45k)")
    print(f"  {'biologico':<12}: R$ 30000-60000 (treinamento)")
    print(f"\n  -> O cao digital custa 5-16% do biologico. E escala para infinitos.")

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
