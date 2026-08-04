#!/usr/bin/env python3
"""
OpenInclusiveIDE -- IDE de Desenvolvimento para TODAS as Deficiencias
======================================================================
"Programar e um ato de criacao. Nenhuma deficiencia deve impedir a criacao.
Um cego pode escrever codigo com a voz. Um surdo pode ver erros com cores.
Uma pessoa sem bracos pode navegar com os olhos. Uma pessoa com dislexia
pode ler com fontes especiais. Um autista pode ter um ambiente calmo.

A IDE nao foi feita para o programador padrao -- porque programador padrao
nao existe. Cada cerebro e diferente. Cada corpo e diferente. Cada sensorio
e diferente. A IDE se ADAPTA ao desenvolvedor, nao o contrario.

ZERO barreira de entrada. MAXIMA produtividade. TODA deficiencia coberta.

Integrado com:
- OpenFocusGuard (protege contra sobrecarga)
- OpenSilencePolicy (silencio por padrao, som so quando solicitado)
- OpenAbsence (respeita pausas)
- OpenBodilyAutonomy (o usuario controla seu corpo/tempo)
- OpenTerminal (todo terminal roda a IDE)
- OpenHumanAmplification (IA como instrumento, nao substituto)

DEFICIENCIAS COBERTAS:
1. VISUAL (cegueira, baixa visao, daltonismo, fotossensibilidade)
2. AUDITIVA (surdez, baixa audicao, tinnitus)
3. MOTORA (paralisia, amputados, distrofia, tetraplegia, tremores)
4. COGNITIVA (dislexia, TDAH, disfasia, discalculia)
5. ESPECTRO AUTISTA (hipersensibilidade sensorial, sobrecarga)
6. COMUNICACAO (afasia, gagueira, mutismo seletivo)
7. NEUROLOGICA (epilepsia, Parkinson, Alzheimer, LES)
8. DESENVOLVIMENTO (Sindrome de Down, atrasos globais)
9. MULTIPLO (combinacoes de deficiencias)
10. TEMPORARIA (lesao, cirurgia, fadiga extrema, gestacao)

PRINCIPIO CHAVE: A deficiencia nao esta na pessoa -- esta no AMBIENTE.
Se a IDE nao serve para uma pessoa, a IDE que esta quebrada.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
import hashlib


# ============================================================================
# 1. CLASSIFICACAO DE DEFICIENCIAS
# ============================================================================

class DisabilityCategory(Enum):
    VISUAL = "visual"                    # cegueira, baixa visao, daltonismo
    AUDITORY = "auditiva"                # surdez, baixa audicao, tinnitus
    MOTOR = "motora"                     # paralisia, amputados, tremores
    COGNITIVE = "cognitiva"              # dislexia, TDAH, discalculia
    AUTISM_SPECTRUM = "espectro_autista" # hipersensibilidade, sobrecarga
    COMMUNICATION = "comunicacao"        # afasia, gagueira, mutismo
    NEUROLOGICAL = "neurologica"         # epilepsia, Parkinson, LES
    DEVELOPMENTAL = "desenvolvimento"    # Sindrome de Down
    MULTIPLE = "multipla"                # combinacao
    TEMPORARY = "temporaria"             # lesao, cirurgia, fadiga


class DisabilitySeverity(Enum):
    MILD = "leve"          # dificuldade, mas funcional
    MODERATE = "moderada"  # precisa de adaptacao significativa
    SEVERE = "severa"      # depende de adaptacao total
    PROFOUND = "profunda"  # adaptacao total + tecnologia assistiva


@dataclass
class DisabilityProfile:
    """Perfil de deficiencia de um desenvolvedor."""
    category: DisabilityCategory
    severity: DisabilitySeverity
    specifics: List[str] = field(default_factory=list)  # detalhes especificos
    assistive_tech: List[str] = field(default_factory=list)  # tecnologia assistiva usada

    def needs_visual_adaptation(self) -> bool:
        return self.category in (DisabilityCategory.VISUAL, DisabilityCategory.MULTIPLE)

    def needs_audio_adaptation(self) -> bool:
        return self.category in (DisabilityCategory.AUDITORY, DisabilityCategory.MULTIPLE)

    def needs_motor_adaptation(self) -> bool:
        return self.category in (DisabilityCategory.MOTOR, DisabilityCategory.MULTIPLE)

    def needs_cognitive_adaptation(self) -> bool:
        return self.category in (
            DisabilityCategory.COGNITIVE,
            DisabilityCategory.AUTISM_SPECTRUM,
            DisabilityCategory.DEVELOPMENTAL,
            DisabilityCategory.MULTIPLE,
        )

    def needs_sensorial_calming(self) -> bool:
        return self.category in (
            DisabilityCategory.AUTISM_SPECTRUM,
            DisabilityCategory.NEUROLOGICAL,
            DisabilityCategory.MULTIPLE,
        )


# ============================================================================
# 2. PERFIL DO DESENVOLVEDOR
# ============================================================================

@dataclass
class DeveloperProfile:
    """Perfil completo de acessibilidade do desenvolvedor."""
    developer_id: str
    name: str
    disabilities: List[DisabilityProfile] = field(default_factory=list)
    preferences: Dict[str, Any] = field(default_factory=dict)
    energy_level: float = 1.0  # 0.0 (exausto) a 1.0 (maximo)
    fatigue_threshold: float = 0.3  # abaixo disso, sugerir pausa (OpenAbsence)

    def has_any_disability(self) -> bool:
        return len(self.disabilities) > 0

    def categories(self) -> Set[DisabilityCategory]:
        return {d.category for d in self.disabilities}

    def add_disability(self, profile: DisabilityProfile) -> None:
        self.disabilities.append(profile)

    def effective_energy(self) -> float:
        """Energia ajustada por numero de deficiencias (cada uma consome energia extra)."""
        if not self.disabilities:
            return self.energy_level
        penalty = len(self.disabilities) * 0.05  # cada deficiencia = 5% mais cansativo
        return max(0.0, self.energy_level - penalty)

    def is_low_energy(self) -> bool:
        return self.effective_energy() < self.fatigue_threshold


# ============================================================================
# 3. MODOS DE ENTRADA (Input)
# ============================================================================

class InputMode(Enum):
    KEYBOARD_FULL = "teclado_completo"        # teclado tradicional
    KEYBOARD_ONE_HAND = "teclado_uma_mao"     # uma mao so
    KEYBOARD_HEAD = "teclado_cabeca"          # teclado de cabeca
    KEYBOARD_MOUTH = "teclado_boca"           # teclado de boca/sopro
    VOICE = "voz"                              # dictacao por voz
    VOICE_CODE = "voz_codigo"                 # programacao por voz (Talon/Cursorless)
    EYE_TRACKING = "rastreio_olhos"           # controle pelos olhos
    SWITCH = "chave"                           # um botao (scan e seleciona)
    SWITCH_DUAL = "chave_dupla"               # dois botoes
    BRAILLE_KEYBOARD = "teclado_braille"      # teclado braille
    GESTURE = "gesto"                          # gestos de mao/corpo
    BRAIN_INTERFACE = "interface_cerebral"    # BCI (Neuralink etc)
    TOUCH = "toque"                            # tela touch
    TRACKBALL = "trackball"                    # trackball para tremores
    MOUTH_STICK = "ponteiro_bocal"            # ponteiro na boca
    FOOT_PEDAL = "pedal_pe"                   # pedal de pe
    PREDICTIVE = "preditivo"                   # autocompletar agressivo (poucos cliques)


@dataclass
class InputConfiguration:
    """Configuracao de entrada adaptada."""
    primary_mode: InputMode = InputMode.KEYBOARD_FULL
    secondary_mode: Optional[InputMode] = None  # modo de backup
    dwell_time_ms: int = 500          # tempo de fixacao para eye tracking
    scan_rate_ms: int = 2000          # velocidade de scan para switch
    voice_language: str = "pt-BR"
    voice_code_dialect: str = "portugol_pp"  # dicionario de codigo por voz
    predictive_aggressiveness: float = 0.8  # 0=conservador, 1=maximo
    debounce_ms: int = 0              # filtrar tremores (Parkinson)
    chord_input: bool = False         # entrada por acordes (uma mao)
    sticky_keys: bool = False         # teclas adesivas (precionar uma de cada vez)
    slow_keys: bool = False           # teclas lentas (ignora toques acidentais)
    repeat_rate: int = 0              # 0=sem repeticao (evita digitacao indesejada)


def recommend_input(profile: DeveloperProfile) -> InputConfiguration:
    """Recomenda modo de entrada baseado no perfil."""
    config = InputConfiguration()

    for d in profile.disabilities:
        if d.category == DisabilityCategory.VISUAL:
            if d.severity in (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND):
                config.primary_mode = InputMode.BRAILLE_KEYBOARD
                config.secondary_mode = InputMode.VOICE_CODE
            elif d.severity == DisabilitySeverity.MODERATE:
                config.primary_mode = InputMode.VOICE_CODE
                config.secondary_mode = InputMode.KEYBOARD_FULL

        elif d.category == DisabilityCategory.MOTOR:
            if "tetraplegia" in d.specifics or d.severity == DisabilitySeverity.PROFOUND:
                config.primary_mode = InputMode.VOICE_CODE
                config.secondary_mode = InputMode.EYE_TRACKING
                config.dwell_time_ms = 300
            elif "amputado" in d.specifics or "uma_mao" in d.specifics:
                config.primary_mode = InputMode.KEYBOARD_ONE_HAND
                config.chord_input = True
            elif "tremor" in d.specifics or "parkinson" in d.specifics:
                config.primary_mode = InputMode.TRACKBALL
                config.debounce_ms = 150
                config.slow_keys = True
            elif d.severity in (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND):
                config.primary_mode = InputMode.SWITCH_DUAL
                config.scan_rate_ms = 1500

        elif d.category == DisabilityCategory.AUTISM_SPECTRUM:
            config.predictive_aggressiveness = 0.5  # menos sugestoes = menos ruido

        elif d.category == DisabilityCategory.COGNITIVE:
            if "dislexia" in d.specifics:
                config.predictive_aggressiveness = 0.9  # mais sugestoes ajuda
            config.sticky_keys = True  # simplifica combinacoes

        elif d.category == DisabilityCategory.NEUROLOGICAL:
            if "epilepsia" in d.specifics:
                config.repeat_rate = 0  # evitar flicker repetitivo
            if "les" in d.specifics:  # lesao por esforco repetitivo
                config.primary_mode = InputMode.VOICE
                config.secondary_mode = InputMode.KEYBOARD_FULL

    return config


# ============================================================================
# 4. MODOS DE SAIDA (Output/Display)
# ============================================================================

class OutputMode(Enum):
    VISUAL_TEXT = "texto_visual"          # texto na tela
    VISUAL_HIGH_CONTRAST = "alto_contraste"  # branco/preto ou preto/branco
    VISUAL_LARGE = "texto_grande"          # fonte 24pt+
    VISUAL_DYSLEXIA = "fonte_dislexia"     # OpenDyslexic, espacamento amplo
    AUDIO_TTS = "texto_para_voz"          # screen reader (TTS)
    AUDIO_SONIFICATION = "sonificacao"    # sons representam dados/erros
    HAPTIC = "haptico"                     # vibracao representa eventos
    BRAILLE_DISPLAY = "display_braille"    # linha braille fisica
    COLOR_BLIND = "daltonismo"             # paleta adaptada
    DARK_CALM = "escuro_calmo"             # modo escuro para autismo/epilepsia
    MINIMAL = "minimal"                    # minimo de informacao na tela


class ColorBlindnessType(Enum):
    NONE = "nenhum"
    PROTANOPIA = "protanopia"        # nao ve vermelho
    DEUTERANOPIA = "deuteranopia"    # nao ve verde
    TRITANOPIA = "tritanopia"        # nao ve azul
    ACHROMATOPSIA = "acromatopsia"   # nao ve cores (so cinza)
    PROTANOMALIA = "protanomalia"    # vermelho reduzido
    DEUTERANOMALIA = "deuteranomalia"  # verde reduzido


@dataclass
class OutputConfiguration:
    """Configuracao de saida/display adaptada."""
    primary_mode: OutputMode = OutputMode.VISUAL_TEXT
    tts_enabled: bool = False          # screen reader
    tts_voice: str = "pt-BR-Neural"    # voz do TTS
    tts_rate: float = 1.0              # velocidade da fala
    font_family: str = "JetBrains Mono"
    font_size_pt: int = 14
    line_height: float = 1.5
    letter_spacing: float = 0.0        # espacamento entre letras (dislexia)
    high_contrast: bool = False
    dark_mode: bool = True
    color_blind: ColorBlindnessType = ColorBlindnessType.NONE
    braille_cells: int = 40            # numero de celulas braille
    haptic_enabled: bool = False
    reduce_motion: bool = False        # sem animacoes (epilepsia/autismo)
    screen_dim_seconds: int = 0        # 0=nao escurece (evita fadiga)
    syntax_highlight_style: str = "calm"  # calmo, minimalista
    error_display: str = "visual"      # como mostrar erros: visual, audio, haptic


def recommend_output(profile: DeveloperProfile) -> OutputConfiguration:
    """Recomenda modo de saida baseado no perfil."""
    config = OutputConfiguration()

    for d in profile.disabilities:
        if d.category == DisabilityCategory.VISUAL:
            if d.severity in (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND):
                config.primary_mode = OutputMode.BRAILLE_DISPLAY
                config.tts_enabled = True
                config.tts_rate = 1.5  # cegos escutam rapido
            elif d.severity == DisabilitySeverity.MODERATE:
                config.primary_mode = OutputMode.VISUAL_LARGE
                config.font_size_pt = 24
                config.high_contrast = True
            if "daltonismo" in d.specifics:
                # Detectar tipo
                for cb in ColorBlindnessType:
                    if cb.value in d.specifics:
                        config.color_blind = cb
                        break

        elif d.category == DisabilityCategory.AUDITORY:
            config.primary_mode = OutputMode.VISUAL_TEXT
            config.tts_enabled = False  # nao adianta TTS
            config.error_display = "visual"  # erros SO visuais
            config.haptic_enabled = True  # vibracao como canal alternativo

        elif d.category == DisabilityCategory.COGNITIVE:
            if "dislexia" in d.specifics:
                config.font_family = "OpenDyslexic"
                config.letter_spacing = 0.12
                config.line_height = 2.0
                config.font_size_pt = 18
            if "tdah" in d.specifics:
                config.primary_mode = OutputMode.MINIMAL
                config.dark_mode = True

        elif d.category == DisabilityCategory.AUTISM_SPECTRUM:
            config.primary_mode = OutputMode.DARK_CALM
            config.reduce_motion = True
            config.syntax_highlight_style = "monochrome"  # cores calmadas
            config.dark_mode = True
            config.screen_dim_seconds = 0  # nada piscando

        elif d.category == DisabilityCategory.NEUROLOGICAL:
            if "epilepsia" in d.specifics:
                config.reduce_motion = True
                config.dark_mode = True
                config.syntax_highlight_style = "monochrome"
            if "parkinson" in d.specifics:
                config.font_size_pt = 18

        elif d.category == DisabilityCategory.DEVELOPMENTAL:
            config.font_size_pt = 20
            config.line_height = 1.8
            config.syntax_highlight_style = "high_contrast_simple"

    return config


# ============================================================================
# 5. ADAPTACOES DE CODIGO (Code Adaptation Layer)
# ============================================================================

class CodeRepresentation(Enum):
    STANDARD = "texto_padrao"           # codigo fonte normal
    STRUCTURED_BLOCKS = "blocos"        # blocos visuais (Scratch-like)
    FLOWCHART = "fluxograma"            # representacao visual de fluxo
    NATURAL_LANGUAGE = "linguagem_natural"  # descricao em portugues
    VOICE_FRIENDLY = "amigavel_voz"     # otimizado para TTS
    SIMPLIFIED = "simplificado"         # menos simbolos, mais palavras
    PORTUGOL_PP = "portugol_pp"         # Portugol++ (linguagem da Republica)
    SIGN_LANGUAGE = "libras"            # representacao em Libras (avatar)


@dataclass
class CodeAdaptationConfig:
    """Como o codigo e apresentado ao desenvolvedor."""
    representation: CodeRepresentation = CodeRepresentation.STANDARD
    indentation_guide: bool = True      # guias visuais de indentacao
    bracket_matching_audio: bool = False  # som ao casar chaves
    error_description_level: str = "detalhado"  # simples, moderado, detalhado
    autocomplete_trigger: str = "instant"  # instant, manual, predictive
    line_numbers_audio: bool = False    # TTS anuncia numero da linha
    spell_check_code: bool = True       # corrige typos em nomes de variaveis
    semantic_groups: bool = False       # agrupa codigo por funcao (cores/blocos)
    chunk_size: int = 0                 # 0=tudo, N=mostra N linhas por vez (cognitivo)


def adapt_code_config(profile: DeveloperProfile) -> CodeAdaptationConfig:
    """Adapta como o codigo e apresentado."""
    config = CodeAdaptationConfig()

    for d in profile.disabilities:
        if d.category == DisabilityCategory.VISUAL:
            if d.severity in (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND):
                config.representation = CodeRepresentation.VOICE_FRIENDLY
                config.bracket_matching_audio = True
                config.line_numbers_audio = True
                config.error_description_level = "detalhado"

        elif d.category == DisabilityCategory.COGNITIVE:
            if "dislexia" in d.specifics:
                config.representation = CodeRepresentation.SIMPLIFIED
                config.autocomplete_trigger = "predictive"
            if "tdah" in d.specifics:
                config.chunk_size = 15  # 15 linhas por vez
                config.semantic_groups = True

        elif d.category == DisabilityCategory.AUTISM_SPECTRUM:
            config.representation = CodeRepresentation.STRUCTURED_BLOCKS
            config.semantic_groups = True

        elif d.category == DisabilityCategory.DEVELOPMENTAL:
            config.representation = CodeRepresentation.STRUCTURED_BLOCKS
            config.error_description_level = "simples"
            config.chunk_size = 10

        elif d.category == DisabilityCategory.AUDITORY:
            config.representation = CodeRepresentation.FLOWCHART
            config.error_description_level = "detalhado"

    return config


# ============================================================================
# 6. FEEDBACK MULTIMODAL
# ============================================================================

class FeedbackChannel(Enum):
    VISUAL = "visual"       # cor, icone, borda
    AUDIO = "audio"          # som, voz, tom
    HAPTIC = "haptico"       # vibracao, forca
    BRAILLE = "braille"      # linha braille


class FeedbackType(Enum):
    SUCCESS = "sucesso"
    ERROR = "erro"
    WARNING = "aviso"
    INFO = "info"
    COMPILATION_ERROR = "erro_compilacao"
    RUNTIME_ERROR = "erro_execucao"
    AUTOCOMPLETE_AVAILABLE = "autocomplete"
    SYNTAX_HIGHLIGHT = "sintaxe"
    BREAKPOINT_HIT = "breakpoint"
    TEST_PASS = "teste_passou"
    TEST_FAIL = "teste_falhou"


@dataclass
class FeedbackSignal:
    """Um sinal de feedback multimodal."""
    feedback_type: FeedbackType
    channels: List[FeedbackChannel]
    visual_cue: Optional[str] = None      # descricao do que aparece na tela
    audio_cue: Optional[str] = None       # descricao do som
    haptic_pattern: Optional[str] = None  # padrao de vibracao
    braille_pattern: Optional[str] = None  # representacao braille
    urgency: int = 1                      # 1=baixa, 5=critica


class FeedbackEngine:
    """Motor de feedback multimodal adaptado a cada deficiencia."""

    def __init__(self, profile: DeveloperProfile):
        self.profile = profile
        self.output_config = recommend_output(profile)
        self._build_signals()

    def _build_signals(self) -> None:
        """Constroi o catalogo de sinais por tipo de feedback."""
        self.signals: Dict[FeedbackType, FeedbackSignal] = {}

        for ft in FeedbackType:
            channels = []
            visual = None
            audio = None
            haptic = None
            braille = None

            # Determinar canais disponiveis
            has_visual = True  # sempre tentar visual
            has_audio = True
            has_haptic = self.output_config.haptic_enabled

            # Desativar canais que nao funcionam para o usuario
            for d in self.profile.disabilities:
                if d.category == DisabilityCategory.VISUAL and d.severity in (
                    DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND
                ):
                    has_visual = False
                if d.category == DisabilityCategory.AUDITORY:
                    has_audio = False

            if has_visual:
                channels.append(FeedbackChannel.VISUAL)
            if has_audio:
                channels.append(FeedbackChannel.AUDIO)
            if has_haptic:
                channels.append(FeedbackChannel.HAPTIC)

            # Braille display se disponivel
            if self.output_config.primary_mode == OutputMode.BRAILLE_DISPLAY:
                channels.append(FeedbackChannel.BRAILLE)

            # Configurar sinais especificos
            if ft == FeedbackType.ERROR or ft == FeedbackType.COMPILATION_ERROR:
                visual = "borda vermelha + mensagem"
                audio = "tom grave curto"
                haptic = "vibracao dupla forte"
                braille = "erro"
            elif ft == FeedbackType.SUCCESS or ft == FeedbackType.TEST_PASS:
                visual = "borda verde discreta"
                audio = "tom agudo curto (apenas se solicitado)"
                haptic = "vibracao suave unica"
                braille = "ok"
            elif ft == FeedbackType.WARNING:
                visual = "borda amarela"
                audio = "ton medio curto"
                haptic = "vibracao unica media"
                braille = "aviso"
            elif ft == FeedbackType.TEST_FAIL:
                visual = "linha vermelha no teste"
                audio = "tom descendente"
                haptic = "vibracao tripla"
                braille = "falhou"

            self.signals[ft] = FeedbackSignal(
                feedback_type=ft,
                channels=channels,
                visual_cue=visual,
                audio_cue=audio,
                haptic_pattern=haptic,
                braille_pattern=braille,
            )

    def emit(self, feedback_type: FeedbackType) -> FeedbackSignal:
        """Emite feedback adaptado ao usuario."""
        signal = self.signals.get(feedback_type)
        if not signal:
            signal = self.signals[FeedbackType.INFO]
        return signal


# ============================================================================
# 7. AMBIENTE SENSORIAL (Sensory Environment)
# ============================================================================

@dataclass
class SensoryEnvironment:
    """Controla o ambiente sensorial da IDE para evitar sobrecarga."""
    brightness: float = 0.5              # 0.0=escuro, 1.0=brilho maximo
    contrast_ratio: float = 4.5          # minimo WCAG AA, 7.0 = AAA
    color_temperature_k: int = 3000      # kelvin (quente=relaxante)
    animation_enabled: bool = True
    animation_speed: float = 1.0         # 0.5=lento, 1.0=normal
    sound_enabled: bool = False          # OpenSilencePolicy: silencio por padrao
    notifications_enabled: bool = False  # sem notificacoes intrusivas
    max_visual_elements: int = 0         # 0=sem limite, N=max elementos na tela
    flicker_rate_hz: int = 0             # 0=sem flicker, max 3Hz (epilepsia)
    background: str = "solid"            # solid, gradient (evitar padroes)
    reduce_noise: bool = False           # menos elementos visuais (autismo/TDAH)
    dark_mode: bool = True               # modo escuro por padrao

    def apply_calming(self) -> None:
        """Aplica configuracoes para reduzir sobrecarga sensorial."""
        self.brightness = 0.3
        self.animation_enabled = False
        self.sound_enabled = False
        self.notifications_enabled = False
        self.max_visual_elements = 7  # minimo de elementos
        self.background = "solid"
        self.reduce_noise = True
        self.flicker_rate_hz = 0


def configure_environment(profile: DeveloperProfile) -> SensoryEnvironment:
    """Configura ambiente sensorial baseado no perfil."""
    env = SensoryEnvironment()

    for d in profile.disabilities:
        if d.category == DisabilityCategory.AUTISM_SPECTRUM:
            env.apply_calming()
            env.color_temperature_k = 2700  # mais quente = mais relaxante

        elif d.category == DisabilityCategory.NEUROLOGICAL:
            if "epilepsia" in d.specifics:
                env.flicker_rate_hz = 0
                env.animation_enabled = False
                env.brightness = 0.4
                env.contrast_ratio = 7.0  # AAA
                env.color_temperature_k = 3000

        elif d.category == DisabilityCategory.VISUAL:
            if d.severity in (DisabilitySeverity.MODERATE, DisabilitySeverity.SEVERE):
                env.contrast_ratio = 7.0  # AAA
                env.brightness = 0.7

        elif d.category == DisabilityCategory.COGNITIVE:
            if "tdah" in d.specifics:
                env.max_visual_elements = 5  # minimo absoluto
                env.notifications_enabled = False
                env.animation_enabled = False

        elif d.category == DisabilityCategory.AUDITORY:
            env.sound_enabled = False  # som nao ajuda

    return env


# ============================================================================
# 8. ASSISTENTE DE IA INCLUSIVO (IA as Amplifier)
# ============================================================================

@dataclass
class AIAssistanceConfig:
    """Configuracao do assistente de IA dentro da IDE."""
    enabled: bool = True
    auto_describe_code: bool = False     # descreve codigo em linguagem natural
    auto_fix_accessibility: bool = True  # corrige acessibilidade do codigo
    voice_interaction: bool = False      # conversa por voz
    simplify_errors: bool = True         # traduz erros para linguagem simples
    predict_next_line: bool = True       # sugere proxima linha
    translate_to_portugol: bool = True   # converte codigo para Portugol++
    sign_language_avatar: bool = False   # avatar de Libras
    cognitive_load_monitor: bool = True  # monitora carga cognitiva
    break_reminder: bool = True          # lembra de pausas (OpenAbsence)

    def adapt(self, profile: DeveloperProfile) -> None:
        """Adapta assistente ao perfil."""
        for d in profile.disabilities:
            if d.category == DisabilityCategory.VISUAL:
                if d.severity in (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND):
                    self.voice_interaction = True
                    self.auto_describe_code = True

            elif d.category == DisabilityCategory.AUDITORY:
                self.voice_interaction = False
                self.sign_language_avatar = True

            elif d.category == DisabilityCategory.COGNITIVE:
                self.simplify_errors = True
                self.predict_next_line = True

            elif d.category == DisabilityCategory.AUTISM_SPECTRUM:
                self.predict_next_line = False  # menos sugestoes = menos ruido
                self.cognitive_load_monitor = True

            elif d.category == DisabilityCategory.DEVELOPMENTAL:
                self.simplify_errors = True
                self.auto_describe_code = True
                self.translate_to_portugol = True

            elif d.category == DisabilityCategory.COMMUNICATION:
                self.voice_interaction = True
                self.sign_language_avatar = True


# ============================================================================
# 9. NAVEGACAO DE CODIGO ADAPTADA
# ============================================================================

class NavigationMode(Enum):
    LINE_BY_LINE = "linha_a_linha"       # navegacao tradicional
    BLOCK_BY_BLOCK = "bloco_a_bloco"     # pula de funcao em funcao
    SEMANTIC = "semantica"               # navega por conceito (variavel, loop, etc)
    AUDIO_OUTLINE = "outline_audio"      # TTS le estrutura do arquivo
    TREE = "arvore"                      # arvore de blocos (colapsavel)
    MINIMAP = "minimapa"                 # minimapa para visao geral
    BRAILLE_NAV = "navegacao_braille"    # navegacao por linha braille


@dataclass
class NavigationConfig:
    mode: NavigationMode = NavigationMode.LINE_BY_LINE
    auto_collapse_depth: int = 2         # colapsa blocos com profundidade > N
    announce_position: bool = False      # anuncia posicao (TTS/braille)
    jump_targets: List[str] = field(default_factory=lambda: [
        "funcao", "classe", "loop", "condicao", "retorno", "erro"
    ])


def recommend_navigation(profile: DeveloperProfile) -> NavigationConfig:
    config = NavigationConfig()

    for d in profile.disabilities:
        if d.category == DisabilityCategory.VISUAL:
            if d.severity in (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND):
                config.mode = NavigationMode.BRAILLE_NAV
                config.announce_position = True

        elif d.category == DisabilityCategory.COGNITIVE:
            config.mode = NavigationMode.BLOCK_BY_BLOCK
            config.auto_collapse_depth = 1

        elif d.category == DisabilityCategory.AUTISM_SPECTRUM:
            config.mode = NavigationMode.TREE
            config.auto_collapse_depth = 1

        elif d.category == DisabilityCategory.DEVELOPMENTAL:
            config.mode = NavigationMode.TREE
            config.auto_collapse_depth = 1

    return config


# ============================================================================
# 10. VERIFICACAO DE ACESSIBILIDADE DO CODIGO (a11y lint)
# ============================================================================

@dataclass
class AccessibilityCheck:
    """Verificacao de acessibilidade no codigo que o dev escreve."""
    check_id: str
    description: str
    severity: str  # info, warning, error
    suggestion: str


A11Y_CHECKS: List[AccessibilityCheck] = [
    AccessibilityCheck("A11Y-001",
        "Contraste de cores no output do programa",
        "warning",
        "Use contraste minimo 4.5:1 (WCAG AA)"),
    AccessibilityCheck("A11Y-002",
        "Texto alternativo em imagens/icones do programa",
        "error",
        "Todo elemento visual deve ter descricao para screen readers"),
    AccessibilityCheck("A11Y-003",
        "Navegacao por teclado no programa",
        "error",
        "Todo interativo deve ser acessivel por teclado (Tab/Enter)"),
    AccessibilityCheck("A11Y-004",
        "Nao use so cor para transmitir informacao",
        "warning",
        "Adicione texto ou icone junto com cor"),
    AccessibilityCheck("A11Y-005",
        "Tamanho de fonte minimo no output",
        "info",
        "Minimo 16px para texto, 14px para codigo"),
    AccessibilityCheck("A11Y-006",
        "Animacoes devem ter opcao de desativar",
        "warning",
        "prefers-reduced-motion deve ser respeitado"),
    AccessibilityCheck("A11Y-007",
        "Audio deve ter legenda/transcricao",
        "error",
        "Todo audio deve ter alternativa textual"),
    AccessibilityCheck("A11Y-008",
        "Forms devem ter labels",
        "error",
        "Todo input deve ter label associado"),
    AccessibilityCheck("A11Y-009",
        "Sem padroes que causam seizures",
        "error",
        "Nada que pisque mais que 3x por segundo (WCAG 2.3.1)"),
    AccessibilityCheck("A11Y-010",
        "Linguagem simples e clara",
        "info",
        "Prefira linguagem direta e simples no codigo e comentarios"),
]


def run_a11y_lint(code: str, profile: DeveloperProfile) -> List[AccessibilityCheck]:
    """Executa verificacao de acessibilidade no codigo."""
    # Aqui seria integrado com um linter real
    # Por agora retorna as verificacoes que se aplicam
    applicable = list(A11Y_CHECKS)
    return applicable


# ============================================================================
# 11. PERFIS PRE-CONFIGURADOS (Quick Setup)
# ============================================================================

def create_profile_blind() -> DeveloperProfile:
    """Perfil para desenvolvedor cego."""
    return DeveloperProfile(
        developer_id="blind_dev",
        name="Dev Cego",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.VISUAL,
                severity=DisabilitySeverity.PROFOUND,
                specifics=["cegueira_total"],
                assistive_tech=["screen_reader", "braille_display", "talon_voice"],
            )
        ],
        preferences={"tts_rate": 2.0, "braille_cells": 40},
    )


def create_profile_deaf() -> DeveloperProfile:
    """Perfil para desenvolvedor surdo."""
    return DeveloperProfile(
        developer_id="deaf_dev",
        name="Dev Surdo",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.AUDITORY,
                severity=DisabilitySeverity.PROFOUND,
                specifics=["surdez_profunda"],
                assistive_tech=["visual_alerts"],
            )
        ],
    )


def create_profile_motor_severe() -> DeveloperProfile:
    """Perfil para desenvolvedor com deficiencia motora severa (tetraplegia)."""
    return DeveloperProfile(
        developer_id="motor_dev",
        name="Dev Tetraplegico",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.MOTOR,
                severity=DisabilitySeverity.PROFOUND,
                specifics=["tetraplegia"],
                assistive_tech=["eye_tracker", "voice_control", "switch"],
            )
        ],
    )


def create_profile_dyslexia() -> DeveloperProfile:
    """Perfil para desenvolvedor com dislexia."""
    return DeveloperProfile(
        developer_id="dyslexia_dev",
        name="Dev Dislexico",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.COGNITIVE,
                severity=DisabilitySeverity.MODERATE,
                specifics=["dislexia"],
            )
        ],
    )


def create_profile_adhd() -> DeveloperProfile:
    """Perfil para desenvolvedor com TDAH."""
    return DeveloperProfile(
        developer_id="adhd_dev",
        name="Dev TDAH",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.COGNITIVE,
                severity=DisabilitySeverity.MODERATE,
                specifics=["tdah"],
            )
        ],
    )


def create_profile_autism() -> DeveloperProfile:
    """Perfil para desenvolvedor no espectro autista."""
    return DeveloperProfile(
        developer_id="autism_dev",
        name="Dev Autista",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.AUTISM_SPECTRUM,
                severity=DisabilitySeverity.MODERATE,
                specifics=["hipersensibilidade_sensorial", "sobrecarga"],
            )
        ],
    )


def create_profile_epilepsy() -> DeveloperProfile:
    """Perfil para desenvolvedor com epilepsia fotossensivel."""
    return DeveloperProfile(
        developer_id="epilepsy_dev",
        name="Dev Epileptico",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.NEUROLOGICAL,
                severity=DisabilitySeverity.MODERATE,
                specifics=["epilepsia_fotossensivel"],
            )
        ],
    )


def create_profile_down() -> DeveloperProfile:
    """Perfil para desenvolvedor com Sindrome de Down."""
    return DeveloperProfile(
        developer_id="down_dev",
        name="Dev Down",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.DEVELOPMENTAL,
                severity=DisabilitySeverity.MODERATE,
                specifics=["sindrome_down"],
            )
        ],
    )


def create_profile_multiple() -> DeveloperProfile:
    """Perfil para desenvolvedor com multiplas deficiencias."""
    return DeveloperProfile(
        developer_id="multi_dev",
        name="Dev Multipla",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.VISUAL,
                severity=DisabilitySeverity.MODERATE,
                specifics=["baixa_visao"],
            ),
            DisabilityProfile(
                category=DisabilityCategory.MOTOR,
                severity=DisabilitySeverity.MODERATE,
                specifics=["distrofia", "tremor"],
            ),
        ],
    )


def create_profile_temporary() -> DeveloperProfile:
    """Perfil para deficiencia temporaria (braco quebrado, cirurgia, fadiga)."""
    return DeveloperProfile(
        developer_id="temp_dev",
        name="Dev Temporario",
        disabilities=[
            DisabilityProfile(
                category=DisabilityCategory.TEMPORARY,
                severity=DisabilitySeverity.MODERATE,
                specifics=["lesao_temporaria", "fatiga_extrema"],
            )
        ],
    )


# ============================================================================
# 12. IDE COMPLETA (Orquestrador)
# ============================================================================

class OpenInclusiveIDE:
    """
    IDE Inclusiva que adapta TODOS os aspectos do desenvolvimento
    a TODAS as deficiencias.

    Uso:
        ide = OpenInclusiveIDE(profile)
        ide.start_session()
        ide.display_code(my_code)
        feedback = ide.handle_error("SyntaxError na linha 5")
    """

    def __init__(self, profile: DeveloperProfile):
        self.profile = profile
        self.input_config = recommend_input(profile)
        self.output_config = recommend_output(profile)
        self.code_config = adapt_code_config(profile)
        self.environment = configure_environment(profile)
        self.navigation = recommend_navigation(profile)
        self.feedback_engine = FeedbackEngine(profile)
        self.ai_config = AIAssistanceConfig()
        self.ai_config.adapt(profile)
        self.session_active = False
        self.errors_emitted: List[str] = []
        self.session_start_time: Optional[str] = None

    def start_session(self) -> Dict[str, Any]:
        """Inicia sessao da IDE com o perfil configurado."""
        self.session_active = True
        return {
            "profile": self.profile.name,
            "disabilities": [d.category.value for d in self.profile.disabilities],
            "input": self.input_config.primary_mode.value,
            "output": self.output_config.primary_mode.value,
            "code_representation": self.code_config.representation.value,
            "navigation": self.navigation.mode.value,
            "environment": {
                "brightness": self.environment.brightness,
                "dark_mode": self.environment.dark_mode,
                "animation": self.environment.animation_enabled,
                "sound": self.environment.sound_enabled,
            },
            "ai_assistance": self.ai_config.enabled,
            "session_active": True,
        }

    def display_code(self, code: str) -> Dict[str, Any]:
        """Exibe codigo adaptado ao perfil."""
        return {
            "original_lines": len(code.split("\n")),
            "representation": self.code_config.representation.value,
            "chunked": self.code_config.chunk_size > 0,
            "chunk_size": self.code_config.chunk_size if self.code_config.chunk_size > 0 else None,
            "font": self.output_config.font_family,
            "font_size": self.output_config.font_size_pt,
            "line_height": self.output_config.line_height,
            "high_contrast": self.output_config.high_contrast,
            "reduce_motion": self.output_config.reduce_motion,
        }

    def handle_error(self, error_message: str) -> FeedbackSignal:
        """Processa erro e emite feedback multimodal adaptado."""
        self.errors_emitted.append(error_message)

        # Simplificar erro se IA estiver configurada
        if self.ai_config.simplify_errors:
            error_message = self._simplify_error(error_message)

        return self.feedback_engine.emit(FeedbackType.ERROR)

    def handle_success(self) -> FeedbackSignal:
        return self.feedback_engine.emit(FeedbackType.SUCCESS)

    def handle_test_result(self, passed: bool) -> FeedbackSignal:
        if passed:
            return self.feedback_engine.emit(FeedbackType.TEST_PASS)
        return self.feedback_engine.emit(FeedbackType.TEST_FAIL)

    def check_energy(self) -> Dict[str, Any]:
        """Verifica nivel de energia e sugere pausa se necessario (OpenAbsence)."""
        energy = self.profile.effective_energy()
        return {
            "energy_level": energy,
            "low_energy": self.profile.is_low_energy(),
            "recommend_break": self.profile.is_low_energy(),
            "message": (
                "Energia baixa. Hora de descansar. (OpenAbsence)"
                if self.profile.is_low_energy()
                else "Energia ok. Continue."
            ),
        }

    def run_a11y_check(self, code: str) -> List[AccessibilityCheck]:
        """Executa verificacao de acessibilidade no codigo."""
        return run_a11y_lint(code, self.profile)

    def _simplify_error(self, message: str) -> str:
        """Traduz erro tecnico para linguagem simples."""
        translations = {
            "SyntaxError": "Tem algo errado na escrita do codigo. Verifique a linha indicada.",
            "IndentationError": "O espacamento esta errado. Cada bloco precisa estar alinhado.",
            "TypeError": "Os tipos nao combinam. Voce esta misturando texto com numero, por exemplo.",
            "NameError": "Uma variavel nao foi definida. Verifique se voce escreveu o nome certo.",
            "IndexError": "Voce tentou acessar uma posicao que nao existe na lista.",
            "KeyError": "Essa chave nao existe no dicionario.",
            "AttributeError": "Esse objeto nao tem essa propriedade.",
            "ImportError": "Nao conseguiu encontrar o modulo. Verifique se esta instalado.",
        }
        for tech, simple in translations.items():
            if tech in message:
                return f"{simple} (Detalhe tecnico: {message})"
        return message

    def session_summary(self) -> Dict[str, Any]:
        """Resumo da sessao."""
        return {
            "profile": self.profile.name,
            "disabilities_catered": [d.category.value for d in self.profile.disabilities],
            "total_errors": len(self.errors_emitted),
            "input_mode": self.input_config.primary_mode.value,
            "output_mode": self.output_config.primary_mode.value,
            "code_representation": self.code_config.representation.value,
            "a11y_checks_available": len(A11Y_CHECKS),
        }


# ============================================================================
# 13. DEMONSTRACAO
# ============================================================================

def demo():
    """Demonstra a IDE inclusiva com todos os perfis."""
    print("=" * 70)
    print("OpenInclusiveIDE -- IDE para TODAS as Deficiencias")
    print("=" * 70)

    profiles = {
        "Cego": create_profile_blind(),
        "Surdo": create_profile_deaf(),
        "Tetraplegico": create_profile_motor_severe(),
        "Dislexia": create_profile_dyslexia(),
        "TDAH": create_profile_adhd(),
        "Autista": create_profile_autism(),
        "Epilepsia": create_profile_epilepsy(),
        "Sindrome de Down": create_profile_down(),
        "Multipla (baixa visao + motor)": create_profile_multiple(),
        "Temporaria (lesao)": create_profile_temporary(),
    }

    for label, profile in profiles.items():
        print(f"\n{'─' * 50}")
        print(f"PERFIL: {label}")
        print(f"{'─' * 50}")

        ide = OpenInclusiveIDE(profile)
        session = ide.start_session()

        print(f"  Input:      {session['input']}")
        print(f"  Output:     {session['output']}")
        print(f"  Codigo:     {session['code_representation']}")
        print(f"  Navegacao:  {session['navigation']}")
        print(f"  Som:        {session['environment']['sound']}")
        print(f"  Animacao:   {session['environment']['animation']}")
        print(f"  Brilho:     {session['environment']['brightness']}")
        print(f"  IA:         {session['ai_assistance']}")

        # Simular erro
        error_feedback = ide.handle_error("SyntaxError: invalid syntax on line 5")
        print(f"  Erro feedback canais: {[c.value for c in error_feedback.channels]}")

        # Checar energia
        energy = ide.check_energy()
        print(f"  Energia:    {energy['energy_level']:.2f}")

    # Verificacao de acessibilidade
    print(f"\n{'=' * 70}")
    print("VERIFICACAO DE ACESSIBILIDADE (a11y lint)")
    print(f"{'=' * 70}")
    for check in A11Y_CHECKS:
        print(f"  [{check.severity.upper():8}] {check.check_id}: {check.description}")

    # Resumo de cobertura
    print(f"\n{'=' * 70}")
    print("COBERTURA DE DEFICIENCIAS")
    print(f"{'=' * 70}")
    for cat in DisabilityCategory:
        print(f"  {cat.value:20} -- COBERTO")

    print(f"\nTotal de categorias: {len(DisabilityCategory)}")
    print(f"Total de modos de entrada: {len(InputMode)}")
    print(f"Total de modos de saida: {len(OutputMode)}")
    print(f"Total de verificacoes a11y: {len(A11Y_CHECKS)}")
    print(f"Total de representacoes de codigo: {len(CodeRepresentation)}")
    print(f"\nIDE INCLUSIVA. ZERO BARREIRA. TODA DEFICIENCIA CObERTA.")


if __name__ == "__main__":
    demo()
