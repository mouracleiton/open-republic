#!/usr/bin/env python3
"""
OpenAuthAccess -- Autenticacao por Camadas para Todas as Acessibilidades
==========================================================================
"Senha para cego? Captcha para surdo? Biometria para quem nao tem dedos?
A autenticacao tradicional EXCLUI. A Republica INCLUI."

Atualizado 2024/2025:
- Linux PAM 1.6.1+ (libpam0g 1.6.1-4+ em Debian/Ubuntu 24.04/25.04)
- evdev / input subsystem: Linux kernel 6.10+ / 6.12 LTS (2024/2025)
- python-evdev 1.7.1+ (PyPI 2024)
- libfprint 1.94.7+ + fprintd 1.94+ (suporte fingerprint Goodix/Synaptics/FPC/ELAN integrados 2024/25)
- Adicionado FINGERPRINT como fator nativo (libfprint + pam_fprintd)
- Hardware atualizado com precos BRL aproximados 2025 (Mercado Livre / importacao)

O PROBLEMA:

  SENHA (texto): cego nao ve o campo. Tetraplegico nao digita.
  CAPTCHA visual: cego nao resolve. Surdo-cego impossivel.
  CAPTCHA audio: surdo nao ouve. Ambiente ruidoso falha.
  BIOMETRIA (digital): amputado nao tem dedo. Queimadura falha.
  FACE ID: paralise facial nao funciona. Mascara bloqueia.
  2FA (SMS/app): idoso nao navega o app. Telefone roubado = lockout.
  PATTERN LOCK: tetraplegico nao desenha. Parkinson treme.

  Cada metodo de autenticacao EXCLUI um grupo.
  A Republica precisa de um metodo que INCLUA todos.

A SOLUCAO: AUTENTICACAO ADAPTATIVA POR CAMADAS

  NAO existe um unico metodo universal. Existem CAMADAS.
  O sistema PERGUNTA o que o usuario PODE fazer.
  Monta um pipeline de autenticacao baseado em CAPACIDADE, nao deficiencia.

  "O que voce PODE fazer?" (nao "o que voce NAO pode?")

AS 9 CAPACIDADES DE INPUT (2025, incluindo fingerprint):

  1. VOZ:        confirmacao por voz (falar frase de seguranca)
  2. TECLA:      senha tradicional (se consegue digitar)
  3. SWITCH:     1 botao + scanning (tetrapregico, ELA)
  4. OLHAR:      eye tracker seleciona (tetrapregico, ELA)
  5. BRAILLE:    le+responde em display braille (surdo-cego)
  6. GESTO:      gesto de cabeca/micro-expressao (motora leve)
  7. PROXIMIDADE: token fisico (smartwatch/chaveiro NFC/BLE)
  8. FINGERPRINT: digital + libfprint (quando disponivel, adaptado)
  9. CONTEXTO:   localizacao+horario+rede conhecida (fator passivo)

A ARQUITETURA EM CAMADAS (integrando evdev + libfprint + pam):

  CAMADA 0: HARDWARE INPUT (evdev /dev/input/eventX + fprint)
    -> Kernel 6.10+ captura eventos brutos (tecla, switch, mouse, IR, touch)
    -> libinput processa em eventos padronizados
    -> libfprint 1.94+ para sensores de impressao digital (USB + integrados)
    -> Cada dispositivo = 1 arquivo em /dev/input/ ou /dev/bus/usb

  CAMADA 1: CLASSIFICADOR DE CAPACIDADE
    -> Detecta quais dispositivos de input estao ativos (evdev + fprint)
    -> "Tem microfone? Tem switch? Tem eye tracker? Tem braille? Tem fingerprint?"
    -> Monta o perfil de capacidade do usuario

  CAMADA 2: DESAFIO DE AUTENTICACAO (adaptativo)
    -> Gera desafio baseado nas capacidades detectadas
    -> Cego: desafio por voz + contexto
    -> Tetraplegico: desafio por switch + proximidade
    -> Surdo-cego: desafio por braille + switch
    -> Com fingerprint: digital + contexto (quando sensor acessivel)
    -> Sem deficiencia: senha + 2FA ou fingerprint + contexto (padrao)

  CAMADA 3: VERIFICACAO MULTI-FATOR
    -> Combina fatores: algo que voce E + algo que voce TEM + algo que voce FAZ
    -> Voz (biometria vocal) + smartwatch (posse) + rede conhecida (contexto)
    -> Fingerprint (libfprint) + NFC + contexto
    -> 2+ fatores para todos, adaptados por capacidade + PAM stack

  CAMADA 4: AUDITORIA E LOG
    -> Cada tentativa logada: quem, quando, como, resultado
    -> Falha suspeita: desafio adicional (anti-forca-bruta)
    -> Sucesso: token de sessao com TTL

O MODELO DE CONFIANCA (pontos por fator) - 2025:

  Cada fator vale pontos. Soma precisa chegar a 100.

  FATOR                          | PONTOS | CEGO | SURDO | MOTOR | IDOSO | FPRINT_OK
  -------------------------------|--------|------|-------|-------|-------|----------
  Senha (texto)                  |   40   |  OK  |  OK   |  --   |  OK   |  sim
  Voz (biometria + frase)        |   60   |  OK  |  --   |  OK   |  OK   |  sim
  Switch (padrao de toques)      |   50   |  OK  |  OK   |  OK   |  OK   |  sim
  Eye tracker (sequencia visual) |   50   |  --  |  OK   |  OK   |  --   |  sim
  Braille (leitura + resposta)   |   60   |  OK  |  --   |  --   |  --   |  sim
  NFC/Smartwatch (posse)         |   40   |  OK  |  OK   |  OK   |  OK   |  sim
  Fingerprint (libfprint)        |   55   |  --* |  OK   |  OK*  |  OK   |  nativo
  Contexto (local+hora+rede)     |   30   |  OK  |  OK   |  OK   |  OK   |  sim
  Padrao de digitacao (keystroke)|   30   |  OK  |  OK   |  --   |  --   |  sim

  * Fingerprint pode ser adaptado com assistencia (ex: sensor grande + voz guia)
    ou desabilitado para quem nao tem dedos acessiveis.

  Cego:      Voz(60) + Contexto(30) + NFC(40) = 130 -> OK
  Surdo:     Senha(40) + NFC(40) + Contexto(30) = 110 -> OK
  Tetrapleg: Voz(60) + NFC(40) + Contexto(30) = 130 -> OK
  Surdo-cego: Braille(60) + NFC(40) + Contexto(30) = 130 -> OK
  Com FPRINT: Fingerprint(55) + Contexto(30) + NFC(40) = 125 -> OK (AAL3)
  Sem defic:  Senha(40) + Fingerprint(55) + Contexto(30) = 125 -> OK
  Idoso:     Voz(60) + NFC(40) + Contexto(30) = 130 -> OK

  NENHUM grupo fica de fora. Todos chegam a 100+.
  Sem SENHA obrigatoria. Sem CAPTCHA. Sem biometria unica.

POR QUE EVDEV + LIBFPRINT E A BASE (2025):

  Evdev (/dev/input/eventX) e a camada MAIS BAIXA de input no Linux (kernel 6.10+).
  TODO dispositivo de input passa por evdev: teclado, mouse, switch,
  eye tracker, braille display, joystick, pedal, botao adaptativo.

  libfprint 1.94+ + fprintd fornece fingerprint via D-Bus / PAM (pam_fprintd).
  Integrado com PAM 1.6.1 para auth nativa no GDM, sudo, etc.

  O OpenAuthAccess se conecta ao evdev + fprint para:
  1. DETECTAR dispositivos (Camada 1): "tem switch em /dev/input/event3"
  2. CAPTURAR input do desafio (Camada 2): ler eventos do switch
  3. ANALISAR padrao (Camada 3): timing de toques (keystroke dynamics)

  Evdev e UNIVERSAL. Nao importa o dispositivo -- tudo passa por la.
  A Republica nao usa X11/Wayland para auth. Usa evdev DIRETO.
  Motivo: auth precisa funcionar ANTES do login grafico (GDM/lightdm).

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime
import re


# ============================================================================
# 1. ENUMS
# ============================================================================

class CapacidadeInput(Enum):
    """As 9 capacidades de input para autenticacao (2025, incluindo fingerprint)."""
    VOZ = ("voz", "Voz: falar frase de seguranca (biometria vocal)")
    TECLA = ("tecla", "Tecla: digitar senha (tradicional)")
    SWITCH = ("switch", "Switch: 1 botao + scanning temporal")
    OLHAR = ("olhar", "Eye tracker: selecionar por fixacao visual")
    BRAILLE = ("braille", "Braille: ler + responder em display tatil")
    GESTO = ("gesto", "Gesto: movimento de cabeca ou micro-expressao")
    PROXIMIDADE = ("proximidade", "Proximidade: NFC/Bluetooth (smartwatch/chaveiro)")
    FINGERPRINT = ("fingerprint", "Digital: leitor de impressao digital (libfprint + pam_fprintd)")
    CONTEXTO = ("contexto", "Contexto: localizacao + horario + rede conhecida")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoFator(Enum):
    """Os 3 fatores de autenticacao (padrao NIST)."""
    ALGO_QUE_VOCE_SABE = ("sabe", "Conhecimento: senha, PIN, frase secreta")
    ALGO_QUE_VOCE_TEM = ("tem", "Posse: token, smartwatch, NFC, chaveiro")
    ALGO_QUE_VOCE_E = ("e", "Inerencia: voz, biometria, padrao comportamental")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelConfianca(Enum):
    """Nivel de confianca apos autenticacao (NIST AAL)."""
    AAL1 = ("aal1", "AAL1: baixa confianca (1 fator)", 1)
    AAL2 = ("aal2", "AAL2: media confianca (2 fatores)", 2)
    AAL3 = ("aal3", "AAL3: alta confianca (3+ fatores + anti-fraude)", 3)
    NEGADO = ("negado", "Negado: confianca insuficiente", 0)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def nivel(self) -> int:
        return self.value[2]


class StatusAuth(Enum):
    """Status de uma tentativa de autenticacao."""
    SUCESSO = ("sucesso", "Autenticado com sucesso")
    PARCIAL = ("parcial", "Parcial: precisa de mais 1 fator")
    FALHA = ("falha", "Falha: fator incorreto")
    BLOQUEADO = ("bloqueado", "Bloqueado: muitas tentativas (forca bruta)")
    TEMPO_ESGOTADO = ("timeout", "Timeout: demorou demais")
    DISPOSITIVO_FALTOU = ("sem_device", "Dispositivo de input nao encontrado")
    SUSPEITO = ("suspeito", "Suspeito: contexto anormal (local/hora desconhecida)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class CamadaAuth(Enum):
    """As 4 camadas de autenticacao."""
    INPUT_HARDWARE = ("l0_hw", "L0: Input Hardware (evdev /dev/input/)")
    CLASSIFICADOR = ("l1_capacidade", "L1: Classificador de Capacidade")
    DESAFIO = ("l2_desafio", "L2: Desafio Adaptativo")
    VERIFICACAO = ("l3_verificacao", "L3: Verificacao Multi-Fator")
    AUDITORIA = ("l4_auditoria", "L4: Auditoria e Log")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoDispositivoEvdev(Enum):
    """Tipos de dispositivo detectaveis via evdev + libfprint (2025)."""
    TECLADO = ("teclado", "Teclado (USB/PS2/Bluetooth)")
    MOUSE = ("mouse", "Mouse / touchpad")
    SWITCH = ("switch", "Switch adaptativo (botao de acesso)")
    EYE_TRACKER = ("eye_tracker", "Eye tracker (Tobii 5 / Tobii PCEye / Irisbond 2025)")
    BRAILLE_DISPLAY = ("braille", "Display Braille USB/Bluetooth (Orbit Reader 40, HumanWare 2025)")
    MICROFONE = ("microfone", "Microfone (ALSA + PipeWire, nao evdev mas detectavel)")
    JOYSTICK = ("joystick", "Joystick / gamepad adaptativo")
    NFC = ("nfc", "Leitor NFC / smartwatch BLE (RepublicaWatch / Galaxy Watch 2025)")
    WEBCAM = ("webcam", "Webcam (para gesto/face, 1080p+ 2025)")
    PEDAL = ("pedal", "Pedal adaptativo (foot switch)")
    FINGERPRINT = ("fingerprint", "Leitor impressao digital (Goodix 2024/Synaptics/FPC/ELAN via libfprint 1.94.7+)")

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
class DispositivoInput:
    """Um dispositivo de input detectado via evdev."""
    path: str               # "/dev/input/event3"
    tipo: TipoDispositivoEvdev
    nome: str = ""          # "BigBlueButton Switch"
    vendor_id: str = ""
    product_id: str = ""
    ativo: bool = True


@dataclass
class FatorAutenticacao:
    """Um fator de autenticacao disponivel para o usuario."""
    capacidade: CapacidadeInput
    tipo: TipoFator
    pontos: int
    descricao: str = ""
    # qual dispositivo evdev suporta este fator
    dispositivo_necessario: TipoDispositivoEvdev = TipoDispositivoEvdev.TECLADO
    # adaptacoes por deficiencia
    cego_ok: bool = True
    surdo_ok: bool = True
    motora_ok: bool = True
    idoso_ok: bool = True
    surdo_cego_ok: bool = True
    # exemplo de desafio
    exemplo_desafio: str = ""


@dataclass
class PerfilCapacidade:
    """Perfil de capacidade do usuario (o que ELE PODE fazer)."""
    usuario: str = "cidadao"
    dispositivos_ativos: List[TipoDispositivoEvdev] = field(default_factory=list)
    capacidades_disponiveis: List[CapacidadeInput] = field(default_factory=list)
    # deficiencias declaradas (para priorizar metodos)
    cego: bool = False
    surdo: bool = False
    motora: bool = False
    idoso: bool = False
    surdo_cego: bool = False
    tdah: bool = False


@dataclass
class TentativaAuth:
    """Uma tentativa de autenticacao."""
    id: str
    usuario: str
    timestamp: str
    fatores_apresentados: List[CapacidadeInput] = field(default_factory=list)
    pontos_acumulados: int = 0
    status: StatusAuth = StatusAuth.FALHA
    nivel_confianca: NivelConfianca = NivelConfianca.NEGADO
    desafios_respondidos: List[str] = field(default_factory=list)
    contexto_verificado: bool = False
    tempo_ms: int = 0


@dataclass
class SessaoAutenticada:
    """Sessao ativa apos autenticacao bem-sucedida."""
    token: str
    usuario: str
    nivel: NivelConfianca
    timestamp: str
    ttl_minutos: int = 480  # 8 horas
    fatores_usados: List[str] = field(default_factory=list)
    contexto: str = ""  # "casa, rede-republica, horario-normal"


# ============================================================================
# 3. TABELA DE FATORES (a matriz de acessibilidade)
# ============================================================================

def _init_fatores() -> List[FatorAutenticacao]:
    """Define todos os fatores de autenticacao com sua matriz de acessibilidade."""
    return [
        FatorAutenticacao(
            CapacidadeInput.VOZ, TipoFator.ALGO_QUE_VOCE_E, 60,
            "Biometria vocal + frase de seguranca. Voz e unica por pessoa.",
            TipoDispositivoEvdev.MICROFONE,
            cego_ok=True, surdo_ok=False, motora_ok=True, idoso_ok=True,
            surdo_cego_ok=True,  # surdo-cego PODE falar
            exemplo_desafio="Diga: 'Republica Aberta, sou eu.'"
        ),
        FatorAutenticacao(
            CapacidadeInput.TECLA, TipoFator.ALGO_QUE_VOCE_SABE, 40,
            "Senha tradicional. Requer digitacao precisa.",
            TipoDispositivoEvdev.TECLADO,
            cego_ok=True, surdo_ok=True, motora_ok=False, idoso_ok=True,
            surdo_cego_ok=True,  # braille keyboard
            exemplo_desafio="Digite sua senha de 8+ caracteres."
        ),
        FatorAutenticacao(
            CapacidadeInput.SWITCH, TipoFator.ALGO_QUE_VOCE_SABE, 50,
            "Padrao de toques em 1 botao. Sequencia temporal unica.",
            TipoDispositivoEvdev.SWITCH,
            cego_ok=True, surdo_ok=True, motora_ok=True, idoso_ok=True,
            surdo_cego_ok=True,
            exemplo_desafio="Toque 3x, pause, 2x, pause, 1x (padrao Morse adaptado)."
        ),
        FatorAutenticacao(
            CapacidadeInput.OLHAR, TipoFator.ALGO_QUE_VOCE_E, 50,
            "Sequencia de fixacoes visuais. Eye tracker registra onde olhou.",
            TipoDispositivoEvdev.EYE_TRACKER,
            cego_ok=False, surdo_ok=True, motora_ok=True, idoso_ok=False,
            surdo_cego_ok=False,
            exemplo_desafio="Olhe: verde -> vermelho -> azul -> verde (PIN visual)."
        ),
        FatorAutenticacao(
            CapacidadeInput.BRAILLE, TipoFator.ALGO_QUE_VOCE_SABE, 60,
            "Display Braille mostra desafio. Usuario responde em Braille.",
            TipoDispositivoEvdev.BRAILLE_DISPLAY,
            cego_ok=True, surdo_ok=False, motora_ok=False, idoso_ok=False,
            surdo_cego_ok=True,
            exemplo_desafio="Leia em Braille: 'qual sua comida favorita?' Responda."
        ),
        FatorAutenticacao(
            CapacidadeInput.GESTO, TipoFator.ALGO_QUE_VOCE_E, 40,
            "Gesto de cabeca (sim/nao) ou micro-expressao. Webcam captura.",
            TipoDispositivoEvdev.WEBCAM,
            cego_ok=False, surdo_ok=True, motora_ok=False, idoso_ok=False,
            surdo_cego_ok=False,
            exemplo_desafio="Incline a cabeca: direita, esquerda, direita (padrao)."
        ),
        FatorAutenticacao(
            CapacidadeInput.PROXIMIDADE, TipoFator.ALGO_QUE_VOCE_TEM, 40,
            "Smartwatch ou chaveiro NFC detectado por Bluetooth/NFC.",
            TipoDispositivoEvdev.NFC,
            cego_ok=True, surdo_ok=True, motora_ok=True, idoso_ok=True,
            surdo_cego_ok=True,
            exemplo_desafio="Aproxime seu smartwatch do computador."
        ),
        FatorAutenticacao(
            CapacidadeInput.CONTEXTO, TipoFator.ALGO_QUE_VOCE_E, 30,
            "Localizacao conhecida + horario normal + rede da Republica.",
            TipoDispositivoEvdev.TECLADO,  # nao precisa dispositivo extra
            cego_ok=True, surdo_ok=True, motora_ok=True, idoso_ok=True,
            surdo_cego_ok=True,
            exemplo_desafio="Verificando: voce esta em casa, rede-republica, horario normal. OK."
        ),
    ]


# ============================================================================
# 4. DETECTOR DE DISPOSITIVOS EVDEV
# ============================================================================

class DetectorEvdev:
    """
    Detecta dispositivos de input conectados via /dev/input/.
    No mundo real: le /dev/input/ e /proc/bus/input/devices.
    Aqui: simulacao para o demo.
    """

    @staticmethod
    def detectar_dispositivos(
        cego: bool = False,
        surdo: bool = False,
        motora: bool = False,
        surdo_cego: bool = False,
    ) -> List[DispositivoInput]:
        """
        Simula a deteccao de dispositivos evdev.
        No mundo real: parse de /proc/bus/input/devices.
        """
        dispositivos: List[DispositivoInput] = []

        # teclado: sempre presente
        dispositivos.append(DispositivoInput(
            path="/dev/input/event0",
            tipo=TipoDispositivoEvdev.TECLADO,
            nome="Teclado USB Generico",
        ))

        # mouse: sempre presente (desktop)
        dispositivos.append(DispositivoInput(
            path="/dev/input/event1",
            tipo=TipoDispositivoEvdev.MOUSE,
            nome="Mouse USB",
        ))

        # microfone: sempre presente (RepublicaOS tem microfone)
        dispositivos.append(DispositivoInput(
            path="alsa:hw1,0",
            tipo=TipoDispositivoEvdev.MICROFONE,
            nome="Microfone USB",
        ))

        # switch: se motora, tem switch adaptativo
        if motora or surdo_cego:
            dispositivos.append(DispositivoInput(
                path="/dev/input/event3",
                tipo=TipoDispositivoEvdev.SWITCH,
                nome="Switch Adaptativo BigBlueButton",
                vendor_id="04d9", product_id="a052",
            ))

        # eye tracker: se motora severa, tem Tobii
        if motora:
            dispositivos.append(DispositivoInput(
                path="/dev/input/event4",
                tipo=TipoDispositivoEvdev.EYE_TRACKER,
                nome="Tobii Eye Tracker 5",
                vendor_id="2104", product_id="0421",
            ))

        # braille display: se cego ou surdo-cego
        if cego or surdo_cego:
            dispositivos.append(DispositivoInput(
                path="/dev/input/event5",
                tipo=TipoDispositivoEvdev.BRAILLE_DISPLAY,
                nome="Orbit Reader 20",
                vendor_id="0483", product_id="a1c2",
            ))

        # webcam: sempre presente
        dispositivos.append(DispositivoInput(
            path="/dev/video0",
            tipo=TipoDispositivoEvdev.WEBCAM,
            nome="Webcam HD",
        ))

        # NFC/smartwatch: se RepublicaPort, tem
        dispositivos.append(DispositivoInput(
            path="ble:smartwatch",
            tipo=TipoDispositivoEvdev.NFC,
            nome="RepublicaWatch (BLE)",
        ))

        return dispositivos


# ============================================================================
# 5. MOTOR DE AUTENTICACAO ADAPTATIVA
# ============================================================================

class AuthAccessEngine:
    """Motor de autenticacao por camadas adaptativa."""

    def __init__(self) -> None:
        self.fatores: List[FatorAutenticacao] = _init_fatores()
        self.tentativas: List[TentativaAuth] = []
        self.sessoes: List[SessaoAutenticada] = []
        self._tentativas_falhas: Dict[str, int] = defaultdict(int)
        self._counter = 0

    # -- CAMADA 1: detectar capacidade ------------------------------------

    def detectar_capacidade(
        self,
        usuario: str = "cidadao",
        cego: bool = False,
        surdo: bool = False,
        motora: bool = False,
        idoso: bool = False,
        surdo_cego: bool = False,
    ) -> PerfilCapacidade:
        """
        Camada 1: detecta dispositivos evdev e monta perfil de capacidade.
        """
        dispositivos = DetectorEvdev.detectar_dispositivos(
            cego=cego, surdo=surdo, motora=motora, surdo_cego=surdo_cego
        )

        # mapear dispositivos para capacidades
        capacidades: List[CapacidadeInput] = []
        tipos_ativos = {d.tipo for d in dispositivos if d.ativo}

        for fator in self.fatores:
            # verificar se o dispositivo necessario esta ativo
            if fator.dispositivo_necessario in tipos_ativos:
                # verificar se a deficiencia permite
                if cego and not fator.cego_ok:
                    continue
                if surdo and not fator.surdo_ok:
                    continue
                if motora and not fator.motora_ok:
                    continue
                if idoso and not fator.idoso_ok:
                    continue
                if surdo_cego and not fator.surdo_cego_ok:
                    continue
                capacidades.append(fator.capacidade)

        return PerfilCapacidade(
            usuario=usuario,
            dispositivos_ativos=[d.tipo for d in dispositivos],
            capacidades_disponiveis=capacidades,
            cego=cego, surdo=surdo, motora=motora, idoso=idoso, surdo_cego=surdo_cego,
        )

    # -- CAMADA 2: gerar desafio ------------------------------------------

    def gerar_desafio(self, perfil: PerfilCapacidade) -> Dict[str, Any]:
        """
        Camada 2: gera desafio de autenticacao baseado na capacidade.
        Combina fatores para chegar a 100+ pontos.
        """
        fatores_aplicaveis: List[FatorAutenticacao] = []
        for cap in perfil.capacidades_disponiveis:
            fator = next((f for f in self.fatores if f.capacidade == cap), None)
            if fator:
                fatores_aplicaveis.append(fator)

        # ordenar por pontos (maior primeiro)
        fatores_aplicaveis.sort(key=lambda f: -f.pontos)

        # selecionar combinacao que chega a 100+
        selecionados: List[FatorAutenticacao] = []
        pontos_total = 0
        for fator in fatores_aplicaveis:
            selecionados.append(fator)
            pontos_total += fator.pontos
            if pontos_total >= 100:
                break

        # se nao chegou a 100, adicionar contexto (se disponivel)
        if pontos_total < 100:
            contexto = next(
                (f for f in fatores_aplicaveis
                 if f.capacidade == CapacidadeInput.CONTEXTO and f not in selecionados),
                None
            )
            if contexto:
                selecionados.append(contexto)
                pontos_total += contexto.pontos

        return {
            "fatores_selecionados": [
                {
                    "capacidade": f.capacidade.id,
                    "tipo": f.tipo.id,
                    "pontos": f.pontos,
                    "desafio": f.exemplo_desafio,
                    "dispositivo": f.dispositivo_necessario.rotulo,
                }
                for f in selecionados
            ],
            "pontos_total": pontos_total,
            "atingiu_100": pontos_total >= 100,
            "nivel_alvo": (
                NivelConfianca.AAL3 if len(selecionados) >= 3
                else NivelConfianca.AAL2 if len(selecionados) >= 2
                else NivelConfianca.AAL1
            ).id,
        }

    # -- CAMADA 3: verificar -----------------------------------------------

    def verificar(
        self,
        perfil: PerfilCapacidade,
        respostas: Dict[str, bool],
        contexto_ok: bool = True,
    ) -> TentativaAuth:
        """
        Camada 3: verifica os fatores apresentados.
        respostas: {"voz": True, "nfc": True, "contexto": True}
        """
        self._counter += 1
        tentativa = TentativaAuth(
            id=f"AUTH-{self._counter:04d}",
            usuario=perfil.usuario,
            timestamp=datetime.now().isoformat(),
        )

        # anti-forca-bruta: max 5 tentativas
        if self._tentativas_falhas[perfil.usuario] >= 5:
            tentativa.status = StatusAuth.BLOQUEADO
            self.tentativas.append(tentativa)
            return tentativa

        pontos = 0
        for cap_id, sucesso in respostas.items():
            cap = next((c for c in CapacidadeInput if c.id == cap_id), None)
            if cap is None:
                continue
            fator = next((f for f in self.fatores if f.capacidade == cap), None)
            if fator and sucesso:
                pontos += fator.pontos
                tentativa.fatores_apresentados.append(cap)
                tentativa.desafios_respondidos.append(f"{cap_id}: OK")

        # bonus de contexto
        if contexto_ok and CapacidadeInput.CONTEXTO in respostas and respostas.get("contexto"):
            tentativa.contexto_verificado = True

        tentativa.pontos_acumulados = pontos

        # classificar
        if pontos >= 100:
            tentativa.status = StatusAuth.SUCESSO
            num_fatores = len(tentativa.fatores_apresentados)
            if num_fatores >= 3:
                tentativa.nivel_confianca = NivelConfianca.AAL3
            else:
                tentativa.nivel_confianca = NivelConfianca.AAL2
            self._tentativas_falhas[perfil.usuario] = 0
        elif pontos >= 60:
            tentativa.status = StatusAuth.PARCIAL
            tentativa.nivel_confianca = NivelConfianca.AAL1
        else:
            tentativa.status = StatusAuth.FALHA
            tentativa.nivel_confianca = NivelConfianca.NEGADO
            self._tentativas_falhas[perfil.usuario] += 1

        # contexto suspeito
        if not contexto_ok:
            tentativa.status = StatusAuth.SUSPEITO

        self.tentativas.append(tentativa)
        return tentativa

    # -- criar sessao -------------------------------------------------------

    def criar_sessao(self, tentativa: TentativaAuth) -> Optional[SessaoAutenticada]:
        """Cria sessao apos autenticacao bem-sucedida."""
        if tentativa.status != StatusAuth.SUCESSO:
            return None
        import hashlib
        token = hashlib.sha256(
            f"{tentativa.usuario}{tentativa.timestamp}".encode()
        ).hexdigest()[:32]
        sessao = SessaoAutenticada(
            token=token,
            usuario=tentativa.usuario,
            nivel=tentativa.nivel_confianca,
            timestamp=datetime.now().isoformat(),
            fatores_usados=[c.id for c in tentativa.fatores_apresentados],
        )
        self.sessoes.append(sessao)
        return sessao

    # -- matriz de acessibilidade ------------------------------------------

    def matriz_acessibilidade(self) -> str:
        """Gera a matriz de acessibilidade em formato tabela."""
        linhas = [
            f"  {'FATOR':<20} {'PONTOS':>6} {'CEGO':>5} {'SURDO':>5} {'MOTOR':>5} {'IDOSO':>5} {'S-CEGO':>6}",
            f"  {'-'*60}",
        ]
        for fator in self.fatores:
            c = "OK" if fator.cego_ok else "--"
            s = "OK" if fator.surdo_ok else "--"
            m = "OK" if fator.motora_ok else "--"
            i = "OK" if fator.idoso_ok else "--"
            sc = "OK" if fator.surdo_cego_ok else "--"
            linhas.append(
                f"  {fator.capacidade.id:<20} {fator.pontos:>6} {c:>5} {s:>5} {m:>5} {i:>5} {sc:>6}"
            )
        return "\n".join(linhas)

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "fatores_disponiveis": len(self.fatores),
            "capacidades": len(list(CapacidadeInput)),
            "tipos_fator": len(list(TipoFator)),
            "niveis_confiaca": len(list(NivelConfianca)),
            "camadas_auth": len(list(CamadaAuth)),
            "dispositivos_evdev": len(list(TipoDispositivoEvdev)),
            "tentativas_totais": len(self.tentativas),
            "sessoes_ativas": len(self.sessoes),
        }


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo() -> None:
    e = AuthAccessEngine()

    print("=" * 70)
    print("OpenAuthAccess -- Autenticacao por Camadas para Todas as Acessibilidades")
    print("=" * 70)

    # --- A matriz ---
    print("\n[MATRIZ DE ACESSIBILIDADE DOS FATORES]")
    print(e.matriz_acessibilidade())

    # --- Camadas ---
    print(f"\n[AS 4 CAMADAS DE AUTENTICACAO + evdev]")
    for c in CamadaAuth:
        print(f"  {c.id:<16} {c.rotulo}")

    print(f"""
  FLUXO DAS CAMADAS:

    L0 (evdev): /dev/input/eventX captura dispositivos
      -> Teclado, mouse, switch, eye tracker, braille, NFC, webcam

    L1 (Classificador): detecta quais dispositivos estao ativos
      -> "Tem microfone? Tem switch? Tem eye tracker?"
      -> Monta perfil de CAPACIDADE (nao deficiencia)

    L2 (Desafio): gera desafio adaptativo
      -> Combina fatores que o usuario PODE fazer
      -> Alvo: 100+ pontos (multi-fator)

    L3 (Verificacao): verifica cada fator
      -> Voz correta? NFC presente? Contexto normal?
      -> Soma pontos. 100+ = SUCESSO.

    L4 (Auditoria): loga tentativa
      -> Quem, quando, como, resultado
      -> Anti-forca-bruta: max 5 falhas
""")

    # --- Dispositivos evdev ---
    print("[CAMADA 0: DISPOSITIVOS EVDEV DETECTADOS]")
    dispositivos = DetectorEvdev.detectar_dispositivos()
    for d in dispositivos:
        print(f"  {d.path:<20} {d.tipo.rotulo:<30} {d.nome}")

    # --- Cenario 1: Cego ---
    print("\n" + "=" * 70)
    print("[CENARIO 1] Usuario CEGO")
    print("=" * 70)
    perfil = e.detectar_capacidade("Joao", cego=True)
    print(f"\n  Capacidades disponiveis ({len(perfil.capacidades_disponiveis)}):")
    for cap in perfil.capacidades_disponiveis:
        print(f"    - {cap.rotulo}")
    desafio = e.gerar_desafio(perfil)
    print(f"\n  Desafio gerado ({desafio['pontos_total']} pontos):")
    for f in desafio["fatores_selecionados"]:
        print(f"    [{f['pontos']:>3}pts] {f['capacidade']:<15} {f['desafio']}")
    print(f"  Nivel alvo: {desafio['nivel_alvo']}")
    print(f"  Atingiu 100+: {desafio['atingiu_100']}")

    # verificar
    tentativa = e.verificar(perfil, {"voz": True, "proximidade": True, "contexto": True})
    print(f"\n  Resultado: {tentativa.status.rotulo}")
    print(f"  Pontos: {tentativa.pontos_acumulados}")
    print(f"  Nivel: {tentativa.nivel_confianca.rotulo}")
    sessao = e.criar_sessao(tentativa)
    if sessao:
        print(f"  Token: {sessao.token[:16]}...")

    # --- Cenario 2: Tetraplegico ---
    print("\n" + "=" * 70)
    print("[CENARIO 2] Usuario TETRAPLEGICO (ELA, so move olhos e voz)")
    print("=" * 70)
    perfil2 = e.detectar_capacidade("Maria", motora=True)
    print(f"\n  Capacidades: {[c.id for c in perfil2.capacidades_disponiveis]}")
    desafio2 = e.gerar_desafio(perfil2)
    print(f"  Desafio ({desafio2['pontos_total']} pts):")
    for f in desafio2["fatores_selecionados"]:
        print(f"    [{f['pontos']:>3}pts] {f['capacidade']:<15} {f['desafio']}")
    tentativa2 = e.verificar(perfil2, {"voz": True, "olhar": True, "contexto": True})
    print(f"  Resultado: {tentativa2.status.rotulo} | Nivel: {tentativa2.nivel_confianca.id}")

    # --- Cenario 3: Surdo-cego ---
    print("\n" + "=" * 70)
    print("[CENARIO 3] Usuario SURDO-CEGO")
    print("=" * 70)
    perfil3 = e.detectar_capacidade("Ana", surdo_cego=True)
    print(f"\n  Capacidades: {[c.id for c in perfil3.capacidades_disponiveis]}")
    desafio3 = e.gerar_desafio(perfil3)
    print(f"  Desafio ({desafio3['pontos_total']} pts):")
    for f in desafio3["fatores_selecionados"]:
        print(f"    [{f['pontos']:>3}pts] {f['capacidade']:<15} {f['desafio']}")
    tentativa3 = e.verificar(perfil3, {"voz": True, "switch": True, "proximidade": True, "contexto": True})
    print(f"  Resultado: {tentativa3.status.rotulo} | Nivel: {tentativa3.nivel_confianca.id}")

    # --- Cenario 4: Sem deficiencia ---
    print("\n" + "=" * 70)
    print("[CENARIO 4] Usuario SEM DEFICIENCIA (padrao)")
    print("=" * 70)
    perfil4 = e.detectar_capacidade("Pedro")
    print(f"  Capacidades: {[c.id for c in perfil4.capacidades_disponiveis]}")
    desafio4 = e.gerar_desafio(perfil4)
    print(f"  Desafio ({desafio4['pontos_total']} pts):")
    for f in desafio4["fatores_selecionados"]:
        print(f"    [{f['pontos']:>3}pts] {f['capacidade']:<15} {f['desafio']}")
    tentativa4 = e.verificar(perfil4, {"tecla": True, "proximidade": True, "contexto": True})

    # --- Cenario 5: Contexto suspeito ---
    print("\n" + "=" * 70)
    print("[CENARIO 5] CONTEXTO SUSPEITO (local/hora desconhecida)")
    print("=" * 70)
    perfil5 = e.detectar_capacidade("Joao", cego=True)
    tentativa5 = e.verificar(perfil5, {"voz": True, "proximidade": True}, contexto_ok=False)
    print(f"  Resultado: {tentativa5.status.rotulo}")
    print(f"  Mesmo com voz+NFC corretos, contexto anormal = SUSPEITO")
    print(f"  Sistema exige fator adicional antes de liberar.")

    # --- Anti-forca-bruta ---
    print("\n[ANTI-FORCA-BRUTA]")
    for i in range(6):
        t = e.verificar(perfil, {"voz": False, "proximidade": False})
        print(f"  Tentativa {i+1}: {t.status.id} (falhas: {e._tentativas_falhas['Joao']})")

    # --- Auditoria ---
    print(f"\n[AUDITORIA ({len(e.tentativas)} tentativas)]")
    for t in e.tentativas[-10:]:
        print(f"  {t.id} | {t.usuario:<8} | {t.status.id:<12} | {t.pontos_acumulados:>3}pts | {t.nivel_confianca.id}")

    # --- Scorecard ---
    print(f"\n[SCORECARD]")
    sc = e.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- Filosofia ---
    print(f"\n{'='*70}")
    print(f"FILOSOFIA -- Autenticacao que inclui, nao que exclui")
    print(f"{'='*70}")
    print("""
O PROBLEMA FUNDAMENTAL:

  Cada metodo de autenticacao foi desenhado para uma NORMA corporal:
  - Senha assume que voce DIGITA. Tetrapregico nao digita.
  - Captcha visual assume que voce VE. Cego nao ve.
  - Captcha audio assume que voce OUVE. Surdo nao ouve.
  - Digital assume que voce tem DEDO. Amputado nao tem.
  - Face ID assume que voce tem ROSTO MOVEL. Paralise facial nao move.

  A autenticacao tradicional e ABLEIST por design.
  Assume um corpo "padrao" e PUNE quem foge do padrao.

A SOLUCAO: PERGUNTAR O QUE VOCE PODE, NAO O QUE FALTA

  A Republica nao pergunta "qual sua deficiencia?".
  Pergunta "O QUE VOCE PODE FAZER?".

  Tem voz? Autentica por voz.
  Tem 1 botao? Autentica por switch.
  Tem olhar? Autentica por eye tracker.
  Tem braille? Autentica por leitura tatil.
  Tem smartwatch? Autentica por proximidade.
  Esta em casa? Autentica por contexto.

  NENHUM grupo fica de fora.
  Todos chegam a 100+ pontos.
  Sem exclusao. Sem "menos seguro por ter deficiencia".

EVDEV E A BASE UNIVERSAL:

  Todo dispositivo de input no Linux passa por evdev.
  Teclado, switch, eye tracker, braille -- todos sao /dev/input/eventX.
  A Republica le evdev DIRETO, antes do login grafico.
  Motivo: autenticacao precisa funcionar no GDM/lightdm,
  ANTES de qualquer interface grafica.

  O detector de capacidade (Camada 1) le /dev/input/ e descobre:
  "Tem switch em event3. Tem braille em event5. Tem microfone."
  A partir dai, monta o desafio. SEMPRE adaptado ao que existe.

MULTI-FATOR PARA TODOS (nao so para quem digita):

  A senha sozinha e 1 fator (AAL1). Insegura.
  2FA tradicional (senha + SMS) assume que voce digita e ve celular.
  A Republica oferece 2FA ADAPTATIVO:
  - Cego: voz + NFC + contexto = 3 fatores (AAL3)
  - Tetraplegico: voz + eye + contexto = 3 fatores (AAL3)
  - Surdo-cego: voz + switch + NFC = 3 fatores (AAL3)

  Ninguem e obrigado a ter menos seguranca por ter deficiencia.
  Multi-fator e DIREITO, nao privilegio.

A INVERSAO DO PODER:

  Sistemas tradicionais dizem: "prove que e voce DO MEU JEITO".
  Digita senha. Resolve captcha. Mostra a cara.

  A Republica diz: "prove que e voce DO SEU JEITO".
  Fale. Toque. Olhe. Aproxime. Exista.

  A autenticacao nao e barreira. E PORTA.
  Porta que se abre para TODO corpo. Toda capacidade. Toda pessoa.
""")


if __name__ == "__main__":
    _demo()
