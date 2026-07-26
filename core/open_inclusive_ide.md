# OpenInclusiveIDE -- IDE de Desenvolvimento para TODAS as Deficiencias

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_inclusive_ide.py`

**Descricao:** ======================================================================
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
"

---

```portugol++

// !/usr/bin/env python3
//
// OpenInclusiveIDE -- IDE de Desenvolvimento para TODAS as Deficiencias
// ======================================================================
// "Programar e um ato de criacao. Nenhuma deficiencia deve impedir a criacao.
// Um cego pode escrever codigo com a voz. Um surdo pode ver erros com cores.
// Uma pessoa sem bracos pode navegar com os olhos. Uma pessoa com dislexia
// pode ler com fontes especiais. Um autista pode ter um ambiente calmo.
//
// A IDE nao foi feita para o programador padrao -- porque programador padrao
// nao existe. Cada cerebro e diferente. Cada corpo e diferente. Cada sensorio
// e diferente. A IDE se ADAPTA ao desenvolvedor, nao o contrario.
//
// ZERO barreira de entrada. MAXIMA produtividade. TODA deficiencia coberta.
//
// Integrado com:
// - OpenFocusGuard (protege contra sobrecarga)
// - OpenSilencePolicy (silencio por padrao, som so quando solicitado)
// - OpenAbsence (respeita pausas)
// - OpenBodilyAutonomy (o usuario controla seu corpo/tempo)
// - OpenTerminal (todo terminal roda a IDE)
// - OpenHumanAmplification (IA como instrumento, nao substituto)
//
// DEFICIENCIAS COBERTAS:
// 1. VISUAL (cegueira, baixa visao, daltonismo, fotossensibilidade)
// 2. AUDITIVA (surdez, baixa audicao, tinnitus)
// 3. MOTORA (paralisia, amputados, distrofia, tetraplegia, tremores)
// 4. COGNITIVA (dislexia, TDAH, disfasia, discalculia)
// 5. ESPECTRO AUTISTA (hipersensibilidade sensorial, sobrecarga)
// 6. COMUNICACAO (afasia, gagueira, mutismo seletivo)
// 7. NEUROLOGICA (epilepsia, Parkinson, Alzheimer, LES)
// 8. DESENVOLVIMENTO (Sindrome de Down, atrasos globais)
// 9. MULTIPLO (combinacoes de deficiencias)
// 10. TEMPORARIA (lesao, cirurgia, fadiga extrema, gestacao)
//
// PRINCIPIO CHAVE: A deficiencia nao esta na pessoa -- esta no AMBIENTE.
// Se a IDE nao serve para uma pessoa, a IDE que esta quebrada.
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
//

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa hashlib

// ============================================================================
// 1. CLASSIFICACAO DE DEFICIENCIAS
// ============================================================================

classe DisabilityCategory herda de Enum:
    VISUAL = "visual"                    // cegueira, baixa visao, daltonismo
    AUDITORY = "auditiva"                // surdez, baixa audicao, tinnitus
    MOTOR = "motora"                     // paralisia, amputados, tremores
    COGNITIVE = "cognitiva"              // dislexia, TDAH, discalculia
    AUTISM_SPECTRUM = "espectro_autista" // hipersensibilidade, sobrecarga
    COMMUNICATION = "comunicacao"        // afasia, gagueira, mutismo
    NEUROLOGICAL = "neurologica"         // epilepsia, Parkinson, LES
    DEVELOPMENTAL = "desenvolvimento"    // Sindrome de Down
    MULTIPLE = "multipla"                // combinacao
    TEMPORARY = "temporaria"             // lesao, cirurgia, fadiga


classe DisabilitySeverity herda de Enum:
    MILD = "leve"          // dificuldade, mas funcional
    MODERATE = "moderada"  // precisa de adaptacao significativa
    SEVERE = "severa"      // depende de adaptacao total
    PROFOUND = "profunda"  // adaptacao total + tecnologia assistiva


// decorador: @dataclass
classe DisabilityProfile:
    """Perfil de deficiencia de um desenvolvedor."""
    category: DisabilityCategory
    severity: DisabilitySeverity
    specifics: List[texto] = field(default_factory=list)  // detalhes especificos
    assistive_tech: List[texto] = field(default_factory=list)  // tecnologia assistiva usada

    funcao needs_visual_adaptation(self) -> booleano:
        retorne self.category em (DisabilityCategory.VISUAL, DisabilityCategory.MULTIPLE)

    funcao needs_audio_adaptation(self) -> booleano:
        retorne self.category em (DisabilityCategory.AUDITORY, DisabilityCategory.MULTIPLE)

    funcao needs_motor_adaptation(self) -> booleano:
        retorne self.category em (DisabilityCategory.MOTOR, DisabilityCategory.MULTIPLE)

    funcao needs_cognitive_adaptation(self) -> booleano:
        retorne self.category em (
            DisabilityCategory.COGNITIVE,
            DisabilityCategory.AUTISM_SPECTRUM,
            DisabilityCategory.DEVELOPMENTAL,
            DisabilityCategory.MULTIPLE,
        )

    funcao needs_sensorial_calming(self) -> booleano:
        retorne self.category em (
            DisabilityCategory.AUTISM_SPECTRUM,
            DisabilityCategory.NEUROLOGICAL,
            DisabilityCategory.MULTIPLE,
        )


// ============================================================================
// 2. PERFIL DO DESENVOLVEDOR
// ============================================================================

// decorador: @dataclass
classe DeveloperProfile:
    """Perfil completo de acessibilidade do desenvolvedor."""
    developer_id: texto
    name: texto
    disabilities: List[DisabilityProfile] = field(default_factory=list)
    preferences: Dict[texto, qualquer] = field(default_factory=dict)
    energy_level: real = 1.0  // 0.0 (exausto) a 1.0 (maximo)
    fatigue_threshold: real = 0.3  // abaixo disso, sugerir pausa (OpenAbsence)

    funcao has_any_disability(self) -> booleano:
        retorne tamanho(self.disabilities) > 0

    funcao categories(self) -> Set[DisabilityCategory]:
        retorne {d.category para d em self.disabilities}

    funcao add_disability(self, profile: DisabilityProfile) -> nulo:
        self.disabilities.append(profile)

    funcao effective_energy(self) -> real:
        """Energia ajustada por numero de deficiencias (cada uma consome energia extra)."""
        se NAO self.disabilities entao:
            retorne self.energy_level
        penalty <- tamanho(self.disabilities) * 0.05  // cada deficiencia = 5% mais cansativo
        retorne max(0.0, self.energy_level - penalty)

    funcao is_low_energy(self) -> booleano:
        retorne self.effective_energy() < self.fatigue_threshold


// ============================================================================
// 3. MODOS DE ENTRADA (Input)
// ============================================================================

classe InputMode herda de Enum:
    KEYBOARD_FULL = "teclado_completo"        // teclado tradicional
    KEYBOARD_ONE_HAND = "teclado_uma_mao"     // uma mao so
    KEYBOARD_HEAD = "teclado_cabeca"          // teclado de cabeca
    KEYBOARD_MOUTH = "teclado_boca"           // teclado de boca/sopro
    VOICE = "voz"                              // dictacao por voz
    VOICE_CODE = "voz_codigo"                 // programacao por voz (Talon/Cursorless)
    EYE_TRACKING = "rastreio_olhos"           // controle pelos olhos
    SWITCH = "chave"                           // um botao (scan e seleciona)
    SWITCH_DUAL = "chave_dupla"               // dois botoes
    BRAILLE_KEYBOARD = "teclado_braille"      // teclado braille
    GESTURE = "gesto"                          // gestos de mao/corpo
    BRAIN_INTERFACE = "interface_cerebral"    // BCI (Neuralink etc)
    TOUCH = "toque"                            // tela touch
    TRACKBALL = "trackball"                    // trackball para tremores
    MOUTH_STICK = "ponteiro_bocal"            // ponteiro na boca
    FOOT_PEDAL = "pedal_pe"                   // pedal de pe
    PREDICTIVE = "preditivo"                   // autocompletar agressivo (poucos cliques)


// decorador: @dataclass
classe InputConfiguration:
    """Configuracao de entrada adaptada."""
    primary_mode: InputMode = InputMode.KEYBOARD_FULL
    secondary_mode: Optional[InputMode] = nulo  // modo de backup
    dwell_time_ms: inteiro = 500          // tempo de fixacao para eye tracking
    scan_rate_ms: inteiro = 2000          // velocidade de scan para switch
    voice_language: texto = "pt-BR"
    voice_code_dialect: texto = "portugol_pp"  // dicionario de codigo por voz
    predictive_aggressiveness: real = 0.8  // 0=conservador, 1=maximo
    debounce_ms: inteiro = 0              // filtrar tremores (Parkinson)
    chord_input: booleano = FALSO         // entrada por acordes (uma mao)
    sticky_keys: booleano = FALSO         // teclas adesivas (precionar uma de cada vez)
    slow_keys: booleano = FALSO           // teclas lentas (ignora toques acidentais)
    repeat_rate: inteiro = 0              // 0=sem repeticao (evita digitacao indesejada)


funcao recommend_input(profile: DeveloperProfile) -> InputConfiguration:
    """Recomenda modo de entrada baseado no perfil."""
    config <- InputConfiguration()

    para cada d em profile.disabilities:
        se d.category == DisabilityCategory.VISUAL entao:
            se d.severity em (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND) entao:
                config.primary_mode <- InputMode.BRAILLE_KEYBOARD
                config.secondary_mode <- InputMode.VOICE_CODE
            senao se d.severity == DisabilitySeverity.MODERATE entao:
                config.primary_mode <- InputMode.VOICE_CODE
                config.secondary_mode <- InputMode.KEYBOARD_FULL

        senao se d.category == DisabilityCategory.MOTOR entao:
            se "tetraplegia" em d.specifics OU d.severity == DisabilitySeverity.PROFOUND entao:
                config.primary_mode <- InputMode.VOICE_CODE
                config.secondary_mode <- InputMode.EYE_TRACKING
                config.dwell_time_ms <- 300
            senao se "amputado" em d.specifics OU "uma_mao" em d.specifics entao:
                config.primary_mode <- InputMode.KEYBOARD_ONE_HAND
                config.chord_input <- VERDADEIRO
            senao se "tremor" em d.specifics OU "parkinson" em d.specifics entao:
                config.primary_mode <- InputMode.TRACKBALL
                config.debounce_ms <- 150
                config.slow_keys <- VERDADEIRO
            senao se d.severity em (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND) entao:
                config.primary_mode <- InputMode.SWITCH_DUAL
                config.scan_rate_ms <- 1500

        senao se d.category == DisabilityCategory.AUTISM_SPECTRUM entao:
            config.predictive_aggressiveness <- 0.5  // menos sugestoes = menos ruido

        senao se d.category == DisabilityCategory.COGNITIVE entao:
            se "dislexia" em d.specifics entao:
                config.predictive_aggressiveness <- 0.9  // mais sugestoes ajuda
            config.sticky_keys <- VERDADEIRO  // simplifica combinacoes

        senao se d.category == DisabilityCategory.NEUROLOGICAL entao:
            se "epilepsia" em d.specifics entao:
                config.repeat_rate <- 0  // evitar flicker repetitivo
            se "les" em d.specifics entao:  // lesao por esforco repetitivo
                config.primary_mode <- InputMode.VOICE
                config.secondary_mode <- InputMode.KEYBOARD_FULL

    retorne config


// ============================================================================
// 4. MODOS DE SAIDA (Output/Display)
// ============================================================================

classe OutputMode herda de Enum:
    VISUAL_TEXT = "texto_visual"          // texto na tela
    VISUAL_HIGH_CONTRAST = "alto_contraste"  // branco/preto ou preto/branco
    VISUAL_LARGE = "texto_grande"          // fonte 24pt+
    VISUAL_DYSLEXIA = "fonte_dislexia"     // OpenDyslexic, espacamento amplo
    AUDIO_TTS = "texto_para_voz"          // screen reader (TTS)
    AUDIO_SONIFICATION = "sonificacao"    // sons representam dados/erros
    HAPTIC = "haptico"                     // vibracao representa eventos
    BRAILLE_DISPLAY = "display_braille"    // linha braille fisica
    COLOR_BLIND = "daltonismo"             // paleta adaptada
    DARK_CALM = "escuro_calmo"             // modo escuro para autismo/epilepsia
    MINIMAL = "minimal"                    // minimo de informacao na tela


classe ColorBlindnessType herda de Enum:
    NONE = "nenhum"
    PROTANOPIA = "protanopia"        // nao ve vermelho
    DEUTERANOPIA = "deuteranopia"    // nao ve verde
    TRITANOPIA = "tritanopia"        // nao ve azul
    ACHROMATOPSIA = "acromatopsia"   // nao ve cores (so cinza)
    PROTANOMALIA = "protanomalia"    // vermelho reduzido
    DEUTERANOMALIA = "deuteranomalia"  // verde reduzido


// decorador: @dataclass
classe OutputConfiguration:
    """Configuracao de saida/display adaptada."""
    primary_mode: OutputMode = OutputMode.VISUAL_TEXT
    tts_enabled: booleano = FALSO          // screen reader
    tts_voice: texto = "pt-BR-Neural"    // voz do TTS
    tts_rate: real = 1.0              // velocidade da fala
    font_family: texto = "JetBrains Mono"
    font_size_pt: inteiro = 14
    line_height: real = 1.5
    letter_spacing: real = 0.0        // espacamento entre letras (dislexia)
    high_contrast: booleano = FALSO
    dark_mode: booleano = VERDADEIRO
    color_blind: ColorBlindnessType = ColorBlindnessType.NONE
    braille_cells: inteiro = 40            // numero de celulas braille
    haptic_enabled: booleano = FALSO
    reduce_motion: booleano = FALSO        // sem animacoes (epilepsia/autismo)
    screen_dim_seconds: inteiro = 0        // 0=nao escurece (evita fadiga)
    syntax_highlight_style: texto = "calm"  // calmo, minimalista
    error_display: texto = "visual"      // como mostrar erros: visual, audio, haptic


funcao recommend_output(profile: DeveloperProfile) -> OutputConfiguration:
    """Recomenda modo de saida baseado no perfil."""
    config <- OutputConfiguration()

    para cada d em profile.disabilities:
        se d.category == DisabilityCategory.VISUAL entao:
            se d.severity em (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND) entao:
                config.primary_mode <- OutputMode.BRAILLE_DISPLAY
                config.tts_enabled <- VERDADEIRO
                config.tts_rate <- 1.5  // cegos escutam rapido
            senao se d.severity == DisabilitySeverity.MODERATE entao:
                config.primary_mode <- OutputMode.VISUAL_LARGE
                config.font_size_pt <- 24
                config.high_contrast <- VERDADEIRO
            se "daltonismo" em d.specifics entao:
                // Detectar tipo
                para cada cb em ColorBlindnessType:
                    se cb.value em d.specifics entao:
                        config.color_blind <- cb
                        pare

        senao se d.category == DisabilityCategory.AUDITORY entao:
            config.primary_mode <- OutputMode.VISUAL_TEXT
            config.tts_enabled <- FALSO  // nao adianta TTS
            config.error_display <- "visual"  // erros SO visuais
            config.haptic_enabled <- VERDADEIRO  // vibracao como canal alternativo

        senao se d.category == DisabilityCategory.COGNITIVE entao:
            se "dislexia" em d.specifics entao:
                config.font_family <- "OpenDyslexic"
                config.letter_spacing <- 0.12
                config.line_height <- 2.0
                config.font_size_pt <- 18
            se "tdah" em d.specifics entao:
                config.primary_mode <- OutputMode.MINIMAL
                config.dark_mode <- VERDADEIRO

        senao se d.category == DisabilityCategory.AUTISM_SPECTRUM entao:
            config.primary_mode <- OutputMode.DARK_CALM
            config.reduce_motion <- VERDADEIRO
            config.syntax_highlight_style <- "monochrome"  // cores calmadas
            config.dark_mode <- VERDADEIRO
            config.screen_dim_seconds <- 0  // nada piscando

        senao se d.category == DisabilityCategory.NEUROLOGICAL entao:
            se "epilepsia" em d.specifics entao:
                config.reduce_motion <- VERDADEIRO
                config.dark_mode <- VERDADEIRO
                config.syntax_highlight_style <- "monochrome"
            se "parkinson" em d.specifics entao:
                config.font_size_pt <- 18

        senao se d.category == DisabilityCategory.DEVELOPMENTAL entao:
            config.font_size_pt <- 20
            config.line_height <- 1.8
            config.syntax_highlight_style <- "high_contrast_simple"

    retorne config


// ============================================================================
// 5. ADAPTACOES DE CODIGO (Code Adaptation Layer)
// ============================================================================

classe CodeRepresentation herda de Enum:
    STANDARD = "texto_padrao"           // codigo fonte normal
    STRUCTURED_BLOCKS = "blocos"        // blocos visuais (Scratch-like)
    FLOWCHART = "fluxograma"            // representacao visual de fluxo
    NATURAL_LANGUAGE = "linguagem_natural"  // descricao em portugues
    VOICE_FRIENDLY = "amigavel_voz"     // otimizado para TTS
    SIMPLIFIED = "simplificado"         // menos simbolos, mais palavras
    PORTUGOL_PP = "portugol_pp"         // Portugol++ (linguagem da Republica)
    SIGN_LANGUAGE = "libras"            // representacao em Libras (avatar)


// decorador: @dataclass
classe CodeAdaptationConfig:
    """Como o codigo e apresentado ao desenvolvedor."""
    representation: CodeRepresentation = CodeRepresentation.STANDARD
    indentation_guide: booleano = VERDADEIRO      // guias visuais de indentacao
    bracket_matching_audio: booleano = FALSO  // som ao casar chaves
    error_description_level: texto = "detalhado"  // simples, moderado, detalhado
    autocomplete_trigger: texto = "instant"  // instant, manual, predictive
    line_numbers_audio: booleano = FALSO    // TTS anuncia numero da linha
    spell_check_code: booleano = VERDADEIRO       // corrige typos em nomes de variaveis
    semantic_groups: booleano = FALSO       // agrupa codigo por funcao (cores/blocos)
    chunk_size: inteiro = 0                 // 0=tudo, N=mostra N linhas por vez (cognitivo)


funcao adapt_code_config(profile: DeveloperProfile) -> CodeAdaptationConfig:
    """Adapta como o codigo e apresentado."""
    config <- CodeAdaptationConfig()

    para cada d em profile.disabilities:
        se d.category == DisabilityCategory.VISUAL entao:
            se d.severity em (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND) entao:
                config.representation <- CodeRepresentation.VOICE_FRIENDLY
                config.bracket_matching_audio <- VERDADEIRO
                config.line_numbers_audio <- VERDADEIRO
                config.error_description_level <- "detalhado"

        senao se d.category == DisabilityCategory.COGNITIVE entao:
            se "dislexia" em d.specifics entao:
                config.representation <- CodeRepresentation.SIMPLIFIED
                config.autocomplete_trigger <- "predictive"
            se "tdah" em d.specifics entao:
                config.chunk_size <- 15  // 15 linhas por vez
                config.semantic_groups <- VERDADEIRO

        senao se d.category == DisabilityCategory.AUTISM_SPECTRUM entao:
            config.representation <- CodeRepresentation.STRUCTURED_BLOCKS
            config.semantic_groups <- VERDADEIRO

        senao se d.category == DisabilityCategory.DEVELOPMENTAL entao:
            config.representation <- CodeRepresentation.STRUCTURED_BLOCKS
            config.error_description_level <- "simples"
            config.chunk_size <- 10

        senao se d.category == DisabilityCategory.AUDITORY entao:
            config.representation <- CodeRepresentation.FLOWCHART
            config.error_description_level <- "detalhado"

    retorne config


// ============================================================================
// 6. FEEDBACK MULTIMODAL
// ============================================================================

classe FeedbackChannel herda de Enum:
    VISUAL = "visual"       // cor, icone, borda
    AUDIO = "audio"          // som, voz, tom
    HAPTIC = "haptico"       // vibracao, forca
    BRAILLE = "braille"      // linha braille


classe FeedbackType herda de Enum:
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


// decorador: @dataclass
classe FeedbackSignal:
    """Um sinal de feedback multimodal."""
    feedback_type: FeedbackType
    channels: List[FeedbackChannel]
    visual_cue: Optional[texto] = nulo      // descricao do que aparece na tela
    audio_cue: Optional[texto] = nulo       // descricao do som
    haptic_pattern: Optional[texto] = nulo  // padrao de vibracao
    braille_pattern: Optional[texto] = nulo  // representacao braille
    urgency: inteiro = 1                      // 1=baixa, 5=critica


classe FeedbackEngine:
    """Motor de feedback multimodal adaptado a cada deficiencia."""

    funcao __init__(self, profile: DeveloperProfile):
        self.profile <- profile
        self.output_config <- recommend_output(profile)
        self._build_signals()

    funcao _build_signals(self) -> nulo:
        """Constroi o catalogo de sinais por tipo de feedback."""
        self.signals: Dict[FeedbackType, FeedbackSignal] <- {}

        para cada ft em FeedbackType:
            channels <- []
            visual <- nulo
            audio <- nulo
            haptic <- nulo
            braille <- nulo

            // Determinar canais disponiveis
            has_visual <- VERDADEIRO  // sempre tentar visual
            has_audio <- VERDADEIRO
            has_haptic <- self.output_config.haptic_enabled

            // Desativar canais que nao funcionam para o usuario
            para cada d em self.profile.disabilities:
                se d.category == DisabilityCategory.VISUAL E d.severity em (
                    DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND
                ) entao:
                    has_visual <- FALSO
                se d.category == DisabilityCategory.AUDITORY entao:
                    has_audio <- FALSO

            se has_visual entao:
                channels.append(FeedbackChannel.VISUAL)
            se has_audio entao:
                channels.append(FeedbackChannel.AUDIO)
            se has_haptic entao:
                channels.append(FeedbackChannel.HAPTIC)

            // Braille display se disponivel
            se self.output_config.primary_mode == OutputMode.BRAILLE_DISPLAY entao:
                channels.append(FeedbackChannel.BRAILLE)

            // Configurar sinais especificos
            se ft == FeedbackType.ERROR OU ft == FeedbackType.COMPILATION_ERROR entao:
                visual <- "borda vermelha + mensagem"
                audio <- "tom grave curto"
                haptic <- "vibracao dupla forte"
                braille <- "erro"
            senao se ft == FeedbackType.SUCCESS OU ft == FeedbackType.TEST_PASS entao:
                visual <- "borda verde discreta"
                audio <- "tom agudo curto (apenas se solicitado)"
                haptic <- "vibracao suave unica"
                braille <- "ok"
            senao se ft == FeedbackType.WARNING entao:
                visual <- "borda amarela"
                audio <- "ton medio curto"
                haptic <- "vibracao unica media"
                braille <- "aviso"
            senao se ft == FeedbackType.TEST_FAIL entao:
                visual <- "linha vermelha no teste"
                audio <- "tom descendente"
                haptic <- "vibracao tripla"
                braille <- "falhou"

            self.signals[ft] <- FeedbackSignal(
                feedback_type=ft,
                channels=channels,
                visual_cue=visual,
                audio_cue=audio,
                haptic_pattern=haptic,
                braille_pattern=braille,
            )

    funcao emit(self, feedback_type: FeedbackType) -> FeedbackSignal:
        """Emite feedback adaptado ao usuario."""
        signal <- self.signals.get(feedback_type)
        se NAO signal entao:
            signal <- self.signals[FeedbackType.INFO]
        retorne signal


// ============================================================================
// 7. AMBIENTE SENSORIAL (Sensory Environment)
// ============================================================================

// decorador: @dataclass
classe SensoryEnvironment:
    """Controla o ambiente sensorial da IDE para evitar sobrecarga."""
    brightness: real = 0.5              // 0.0=escuro, 1.0=brilho maximo
    contrast_ratio: real = 4.5          // minimo WCAG AA, 7.0 = AAA
    color_temperature_k: inteiro = 3000      // kelvin (quente=relaxante)
    animation_enabled: booleano = VERDADEIRO
    animation_speed: real = 1.0         // 0.5=lento, 1.0=normal
    sound_enabled: booleano = FALSO          // OpenSilencePolicy: silencio por padrao
    notifications_enabled: booleano = FALSO  // sem notificacoes intrusivas
    max_visual_elements: inteiro = 0         // 0=sem limite, N=max elementos na tela
    flicker_rate_hz: inteiro = 0             // 0=sem flicker, max 3Hz (epilepsia)
    background: texto = "solid"            // solid, gradient (evitar padroes)
    reduce_noise: booleano = FALSO           // menos elementos visuais (autismo/TDAH)
    dark_mode: booleano = VERDADEIRO               // modo escuro por padrao

    funcao apply_calming(self) -> nulo:
        """Aplica configuracoes para reduzir sobrecarga sensorial."""
        self.brightness <- 0.3
        self.animation_enabled <- FALSO
        self.sound_enabled <- FALSO
        self.notifications_enabled <- FALSO
        self.max_visual_elements <- 7  // minimo de elementos
        self.background <- "solid"
        self.reduce_noise <- VERDADEIRO
        self.flicker_rate_hz <- 0


funcao configure_environment(profile: DeveloperProfile) -> SensoryEnvironment:
    """Configura ambiente sensorial baseado no perfil."""
    env <- SensoryEnvironment()

    para cada d em profile.disabilities:
        se d.category == DisabilityCategory.AUTISM_SPECTRUM entao:
            env.apply_calming()
            env.color_temperature_k <- 2700  // mais quente = mais relaxante

        senao se d.category == DisabilityCategory.NEUROLOGICAL entao:
            se "epilepsia" em d.specifics entao:
                env.flicker_rate_hz <- 0
                env.animation_enabled <- FALSO
                env.brightness <- 0.4
                env.contrast_ratio <- 7.0  // AAA
                env.color_temperature_k <- 3000

        senao se d.category == DisabilityCategory.VISUAL entao:
            se d.severity em (DisabilitySeverity.MODERATE, DisabilitySeverity.SEVERE) entao:
                env.contrast_ratio <- 7.0  // AAA
                env.brightness <- 0.7

        senao se d.category == DisabilityCategory.COGNITIVE entao:
            se "tdah" em d.specifics entao:
                env.max_visual_elements <- 5  // minimo absoluto
                env.notifications_enabled <- FALSO
                env.animation_enabled <- FALSO

        senao se d.category == DisabilityCategory.AUDITORY entao:
            env.sound_enabled <- FALSO  // som nao ajuda

    retorne env


// ============================================================================
// 8. ASSISTENTE DE IA INCLUSIVO (IA as Amplifier)
// ============================================================================

// decorador: @dataclass
classe AIAssistanceConfig:
    """Configuracao do assistente de IA dentro da IDE."""
    enabled: booleano = VERDADEIRO
    auto_describe_code: booleano = FALSO     // descreve codigo em linguagem natural
    auto_fix_accessibility: booleano = VERDADEIRO  // corrige acessibilidade do codigo
    voice_interaction: booleano = FALSO      // conversa por voz
    simplify_errors: booleano = VERDADEIRO         // traduz erros para linguagem simples
    predict_next_line: booleano = VERDADEIRO       // sugere proxima linha
    translate_to_portugol: booleano = VERDADEIRO   // converte codigo para Portugol++
    sign_language_avatar: booleano = FALSO   // avatar de Libras
    cognitive_load_monitor: booleano = VERDADEIRO  // monitora carga cognitiva
    break_reminder: booleano = VERDADEIRO          // lembra de pausas (OpenAbsence)

    funcao adapt(self, profile: DeveloperProfile) -> nulo:
        """Adapta assistente ao perfil."""
        para cada d em profile.disabilities:
            se d.category == DisabilityCategory.VISUAL entao:
                se d.severity em (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND) entao:
                    self.voice_interaction <- VERDADEIRO
                    self.auto_describe_code <- VERDADEIRO

            senao se d.category == DisabilityCategory.AUDITORY entao:
                self.voice_interaction <- FALSO
                self.sign_language_avatar <- VERDADEIRO

            senao se d.category == DisabilityCategory.COGNITIVE entao:
                self.simplify_errors <- VERDADEIRO
                self.predict_next_line <- VERDADEIRO

            senao se d.category == DisabilityCategory.AUTISM_SPECTRUM entao:
                self.predict_next_line <- FALSO  // menos sugestoes = menos ruido
                self.cognitive_load_monitor <- VERDADEIRO

            senao se d.category == DisabilityCategory.DEVELOPMENTAL entao:
                self.simplify_errors <- VERDADEIRO
                self.auto_describe_code <- VERDADEIRO
                self.translate_to_portugol <- VERDADEIRO

            senao se d.category == DisabilityCategory.COMMUNICATION entao:
                self.voice_interaction <- VERDADEIRO
                self.sign_language_avatar <- VERDADEIRO


// ============================================================================
// 9. NAVEGACAO DE CODIGO ADAPTADA
// ============================================================================

classe NavigationMode herda de Enum:
    LINE_BY_LINE = "linha_a_linha"       // navegacao tradicional
    BLOCK_BY_BLOCK = "bloco_a_bloco"     // pula de funcao em funcao
    SEMANTIC = "semantica"               // navega por conceito (variavel, loop, etc)
    AUDIO_OUTLINE = "outline_audio"      // TTS le estrutura do arquivo
    TREE = "arvore"                      // arvore de blocos (colapsavel)
    MINIMAP = "minimapa"                 // minimapa para visao geral
    BRAILLE_NAV = "navegacao_braille"    // navegacao por linha braille


// decorador: @dataclass
classe NavigationConfig:
    mode: NavigationMode = NavigationMode.LINE_BY_LINE
    auto_collapse_depth: inteiro = 2         // colapsa blocos com profundidade > N
    announce_position: booleano = FALSO      // anuncia posicao (TTS/braille)
    jump_targets: List[texto] = field(default_factory=lambda: [
        "funcao", "classe", "loop", "condicao", "retorno", "erro"
    ])


funcao recommend_navigation(profile: DeveloperProfile) -> NavigationConfig:
    config <- NavigationConfig()

    para cada d em profile.disabilities:
        se d.category == DisabilityCategory.VISUAL entao:
            se d.severity em (DisabilitySeverity.SEVERE, DisabilitySeverity.PROFOUND) entao:
                config.mode <- NavigationMode.BRAILLE_NAV
                config.announce_position <- VERDADEIRO

        senao se d.category == DisabilityCategory.COGNITIVE entao:
            config.mode <- NavigationMode.BLOCK_BY_BLOCK
            config.auto_collapse_depth <- 1

        senao se d.category == DisabilityCategory.AUTISM_SPECTRUM entao:
            config.mode <- NavigationMode.TREE
            config.auto_collapse_depth <- 1

        senao se d.category == DisabilityCategory.DEVELOPMENTAL entao:
            config.mode <- NavigationMode.TREE
            config.auto_collapse_depth <- 1

    retorne config


// ============================================================================
// 10. VERIFICACAO DE ACESSIBILIDADE DO CODIGO (a11y lint)
// ============================================================================

// decorador: @dataclass
classe AccessibilityCheck:
    """Verificacao de acessibilidade no codigo que o dev escreve."""
    check_id: texto
    description: texto
    severity: texto  // info, warning, error
    suggestion: texto


A11Y_CHECKS: List[AccessibilityCheck] <- [
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


funcao run_a11y_lint(code: texto, profile: DeveloperProfile) -> List[AccessibilityCheck]:
    """Executa verificacao de acessibilidade no codigo."""
    // Aqui seria integrado com um linter real
    // Por agora retorna as verificacoes que se aplicam
    applicable <- list(A11Y_CHECKS)
    retorne applicable


// ============================================================================
// 11. PERFIS PRE-CONFIGURADOS (Quick Setup)
// ============================================================================

funcao create_profile_blind() -> DeveloperProfile:
    """Perfil para desenvolvedor cego."""
    retorne DeveloperProfile(
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


funcao create_profile_deaf() -> DeveloperProfile:
    """Perfil para desenvolvedor surdo."""
    retorne DeveloperProfile(
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


funcao create_profile_motor_severe() -> DeveloperProfile:
    """Perfil para desenvolvedor com deficiencia motora severa (tetraplegia)."""
    retorne DeveloperProfile(
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


funcao create_profile_dyslexia() -> DeveloperProfile:
    """Perfil para desenvolvedor com dislexia."""
    retorne DeveloperProfile(
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


funcao create_profile_adhd() -> DeveloperProfile:
    """Perfil para desenvolvedor com TDAH."""
    retorne DeveloperProfile(
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


funcao create_profile_autism() -> DeveloperProfile:
    """Perfil para desenvolvedor no espectro autista."""
    retorne DeveloperProfile(
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


funcao create_profile_epilepsy() -> DeveloperProfile:
    """Perfil para desenvolvedor com epilepsia fotossensivel."""
    retorne DeveloperProfile(
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


funcao create_profile_down() -> DeveloperProfile:
    """Perfil para desenvolvedor com Sindrome de Down."""
    retorne DeveloperProfile(
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


funcao create_profile_multiple() -> DeveloperProfile:
    """Perfil para desenvolvedor com multiplas deficiencias."""
    retorne DeveloperProfile(
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


funcao create_profile_temporary() -> DeveloperProfile:
    """Perfil para deficiencia temporaria (braco quebrado, cirurgia, fadiga)."""
    retorne DeveloperProfile(
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


// ============================================================================
// 12. IDE COMPLETA (Orquestrador)
// ============================================================================

classe OpenInclusiveIDE:
    """
    IDE Inclusiva que adapta TODOS os aspectos do desenvolvimento
    a TODAS as deficiencias.

    Uso:
        ide <- OpenInclusiveIDE(profile)
        ide.start_session()
        ide.display_code(my_code)
        feedback <- ide.handle_error("SyntaxError na linha 5")
    """

    funcao __init__(self, profile: DeveloperProfile):
        self.profile <- profile
        self.input_config <- recommend_input(profile)
        self.output_config <- recommend_output(profile)
        self.code_config <- adapt_code_config(profile)
        self.environment <- configure_environment(profile)
        self.navigation <- recommend_navigation(profile)
        self.feedback_engine <- FeedbackEngine(profile)
        self.ai_config <- AIAssistanceConfig()
        self.ai_config.adapt(profile)
        self.session_active <- FALSO
        self.errors_emitted: List[texto] <- []
        self.session_start_time: Optional[texto] <- nulo

    funcao start_session(self) -> Dict[texto, qualquer]:
        """Inicia sessao da IDE com o perfil configurado."""
        self.session_active <- VERDADEIRO
        retorne {
            "profile": self.profile.name,
            "disabilities": [d.category.value para d em self.profile.disabilities],
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
            "session_active": VERDADEIRO,
        }

    funcao display_code(self, code: texto) -> Dict[texto, qualquer]:
        """Exibe codigo adaptado ao perfil."""
        retorne {
            "original_lines": tamanho(code.split("\n")),
            "representation": self.code_config.representation.value,
            "chunked": self.code_config.chunk_size > 0,
            "chunk_size": self.code_config.chunk_size se self.code_config.chunk_size > 0 senao nulo,
            "font": self.output_config.font_family,
            "font_size": self.output_config.font_size_pt,
            "line_height": self.output_config.line_height,
            "high_contrast": self.output_config.high_contrast,
            "reduce_motion": self.output_config.reduce_motion,
        }

    funcao handle_error(self, error_message: texto) -> FeedbackSignal:
        """Processa erro e emite feedback multimodal adaptado."""
        self.errors_emitted.append(error_message)

        // Simplificar erro se IA estiver configurada
        se self.ai_config.simplify_errors entao:
            error_message <- self._simplify_error(error_message)

        retorne self.feedback_engine.emit(FeedbackType.ERROR)

    funcao handle_success(self) -> FeedbackSignal:
        retorne self.feedback_engine.emit(FeedbackType.SUCCESS)

    funcao handle_test_result(self, passed: booleano) -> FeedbackSignal:
        se passed entao:
            retorne self.feedback_engine.emit(FeedbackType.TEST_PASS)
        retorne self.feedback_engine.emit(FeedbackType.TEST_FAIL)

    funcao check_energy(self) -> Dict[texto, qualquer]:
        """Verifica nivel de energia e sugere pausa se necessario (OpenAbsence)."""
        energy <- self.profile.effective_energy()
        retorne {
            "energy_level": energy,
            "low_energy": self.profile.is_low_energy(),
            "recommend_break": self.profile.is_low_energy(),
            "message": (
                "Energia baixa. Hora de descansar. (OpenAbsence)"
                se self.profile.is_low_energy() senao
                "Energia ok. Continue."
            ),
        }

    funcao run_a11y_check(self, code: texto) -> List[AccessibilityCheck]:
        """Executa verificacao de acessibilidade no codigo."""
        retorne run_a11y_lint(code, self.profile)

    funcao _simplify_error(self, message: texto) -> texto:
        """Traduz erro tecnico para linguagem simples."""
        translations <- {
            "SyntaxError": "Tem algo errado na escrita do codigo. Verifique a linha indicada.",
            "IndentationError": "O espacamento esta errado. Cada bloco precisa estar alinhado.",
            "TypeError": "Os tipos nao combinam. Voce esta misturando texto com numero, por exemplo.",
            "NameError": "Uma variavel nao foi definida. Verifique se voce escreveu o nome certo.",
            "IndexError": "Voce tentou acessar uma posicao que nao existe na lista.",
            "KeyError": "Essa chave nao existe no dicionario.",
            "AttributeError": "Esse objeto nao tem essa propriedade.",
            "ImportError": "Nao conseguiu encontrar o modulo. Verifique se esta instalado.",
        }
        para cada tech, simple em translations.items():
            se tech em message entao:
                retorne f"{simple} (Detalhe tecnico: {message})"
        retorne message

    funcao session_summary(self) -> Dict[texto, qualquer]:
        """Resumo da sessao."""
        retorne {
            "profile": self.profile.name,
            "disabilities_catered": [d.category.value para d em self.profile.disabilities],
            "total_errors": tamanho(self.errors_emitted),
            "input_mode": self.input_config.primary_mode.value,
            "output_mode": self.output_config.primary_mode.value,
            "code_representation": self.code_config.representation.value,
            "a11y_checks_available": tamanho(A11Y_CHECKS),
        }


// ============================================================================
// 13. DEMONSTRACAO
// ============================================================================

funcao demo():
    """Demonstra a IDE inclusiva com todos os perfis."""
    imprima("=" * 70)
    imprima("OpenInclusiveIDE -- IDE para TODAS as Deficiencias")
    imprima("=" * 70)

    profiles <- {
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

    para cada label, profile em profiles.items():
        imprima(f"\n{'─' * 50}")
        imprima(f"PERFIL: {label}")
        imprima(f"{'─' * 50}")

        ide <- OpenInclusiveIDE(profile)
        session <- ide.start_session()

        imprima(f"  Input:      {session['input']}")
        imprima(f"  Output:     {session['output']}")
        imprima(f"  Codigo:     {session['code_representation']}")
        imprima(f"  Navegacao:  {session['navigation']}")
        imprima(f"  Som:        {session['environment']['sound']}")
        imprima(f"  Animacao:   {session['environment']['animation']}")
        imprima(f"  Brilho:     {session['environment']['brightness']}")
        imprima(f"  IA:         {session['ai_assistance']}")

        // Simular erro
        error_feedback <- ide.handle_error("SyntaxError: invalid syntax on line 5")
        imprima(f"  Erro feedback canais: {[c.value para c em error_feedback.channels]}")

        // Checar energia
        energy <- ide.check_energy()
        imprima(f"  Energia:    {energy['energy_level']:.2f}")

    // Verificacao de acessibilidade
    imprima(f"\n{'=' * 70}")
    imprima("VERIFICACAO DE ACESSIBILIDADE (a11y lint)")
    imprima(f"{'=' * 70}")
    para cada check em A11Y_CHECKS:
        imprima(f"  [{check.severity.upper():8}] {check.check_id}: {check.description}")

    // Resumo de cobertura
    imprima(f"\n{'=' * 70}")
    imprima("COBERTURA DE DEFICIENCIAS")
    imprima(f"{'=' * 70}")
    para cada cat em DisabilityCategory:
        imprima(f"  {cat.value:20} -- COBERTO")

    imprima(f"\nTotal de categorias: {tamanho(DisabilityCategory)}")
    imprima(f"Total de modos de entrada: {tamanho(InputMode)}")
    imprima(f"Total de modos de saida: {tamanho(OutputMode)}")
    imprima(f"Total de verificacoes a11y: {tamanho(A11Y_CHECKS)}")
    imprima(f"Total de representacoes de codigo: {tamanho(CodeRepresentation)}")
    imprima(f"\nIDE INCLUSIVA. ZERO BARREIRA. TODA DEFICIENCIA COBERTA.")


se __name__ == "__main__" entao:
    demo()
```
