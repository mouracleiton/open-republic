// OpenInclusiveIDE -- IDE de Desenvolvimento para TODAS as Deficiencias -- gerado de Portugol++
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
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa hashlib

// ============================================================================
// 1. CLASSIFICACAO DE DEFICIENCIAS
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
enum DisabilityCategory {
    VISUAL = "visual",                    // cegueira, baixa visao, daltonismo
    AUDITORY = "auditiva",                // surdez, baixa audicao, tinnitus
    MOTOR = "motora",                     // paralisia, amputados, tremores
    COGNITIVE = "cognitiva",              // dislexia, TDAH, discalculia
    AUTISM_SPECTRUM = "espectro_autista", // hipersensibilidade, sobrecarga
    COMMUNICATION = "comunicacao",        // afasia, gagueira, mutismo
    NEUROLOGICAL = "neurologica",         // epilepsia, Parkinson, LES
    DEVELOPMENTAL = "desenvolvimento",    // Sindrome de Down
    MULTIPLE = "multipla",                // combinacao
    TEMPORARY = "temporaria",             // lesao, cirurgia, fadiga
}

#[derive(Debug, Clone, PartialEq)]
enum DisabilitySeverity {
    MILD = "leve",          // dificuldade, mas funcional
    MODERATE = "moderada",  // precisa de adaptacao significativa
    SEVERE = "severa",      // depende de adaptacao total
    PROFOUND = "profunda",  // adaptacao total + tecnologia assistiva
}

// decorador: @dataclass
#[derive(Debug, Clone)]
struct DisabilityProfile {
    category: DisabilityCategory,
    severity: DisabilitySeverity,
    specifics: Vec<String>,      // detalhes especificos
    assistive_tech: Vec<String>, // tecnologia assistiva usada
}

impl DisabilityProfile {
    fn new(category: DisabilityCategory, severity: DisabilitySeverity, specifics: Vec<String>, assistive_tech: Vec<String>) -> Self {
        Self { category, severity, specifics, assistive_tech }
    }
    fn needs_visual_adaptation(&self) -> bool {
        self.category == DisabilityCategory::VISUAL || self.category == DisabilityCategory::MULTIPLE
    }
    fn needs_audio_adaptation(&self) -> bool {
        self.category == DisabilityCategory::AUDITORY || self.category == DisabilityCategory::MULTIPLE
    }
    fn needs_motor_adaptation(&self) -> bool {
        self.category == DisabilityCategory::MOTOR || self.category == DisabilityCategory::MULTIPLE
    }
    fn needs_cognitive_adaptation(&self) -> bool {
        matches!(self.category, DisabilityCategory::COGNITIVE | DisabilityCategory::AUTISM_SPECTRUM | DisabilityCategory::DEVELOPMENTAL | DisabilityCategory::MULTIPLE)
    }
    fn needs_sensorial_calming(&self) -> bool {
        matches!(self.category, DisabilityCategory::AUTISM_SPECTRUM | DisabilityCategory::NEUROLOGICAL | DisabilityCategory::MULTIPLE)
    }
}

// ============================================================================
// 2. PERFIL DO DESENVOLVEDOR
// ============================================================================

// decorador: @dataclass
#[derive(Debug, Clone)]
struct DeveloperProfile {
    developer_id: String,
    name: String,
    disabilities: Vec<DisabilityProfile>,
    preferences: HashMap<String, String>,
    energy_level: f64,       // 0.0 (exausto) a 1.0 (maximo)
    fatigue_threshold: f64,  // abaixo disso, sugerir pausa (OpenAbsence)
}

impl DeveloperProfile {
    fn new(developer_id: String, name: String, disabilities: Vec<DisabilityProfile>, preferences: HashMap<String, String>, energy_level: f64, fatigue_threshold: f64) -> Self {
        Self { developer_id, name, disabilities, preferences, energy_level, fatigue_threshold }
    }
    fn has_any_disability(&self) -> bool {
        !self.disabilities.is_empty()
    }
    fn categories(&self) -> HashSet<DisabilityCategory> {
        self.disabilities.iter().map(|d| d.category.clone()).collect()
    }
    fn add_disability(&mut self, profile: DisabilityProfile) {
        self.disabilities.push(profile);
    }
    fn effective_energy(&self) -> f64 {
        if self.disabilities.is_empty() {
            return self.energy_level;
        }
        let penalty = self.disabilities.len() as f64 * 0.05;
        (self.energy_level - penalty).max(0.0)
    }
    fn is_low_energy(&self) -> bool {
        self.effective_energy() < self.fatigue_threshold
    }
}

// ============================================================================
// 3. MODOS DE ENTRADA (Input)
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
enum InputMode {
    KEYBOARD_FULL = "teclado_completo",
    KEYBOARD_ONE_HAND = "teclado_uma_mao",
    KEYBOARD_HEAD = "teclado_cabeca",
    KEYBOARD_MOUTH = "teclado_boca",
    VOICE = "voz",
    VOICE_CODE = "voz_codigo",
    EYE_TRACKING = "rastreio_olhos",
    SWITCH = "chave",
    SWITCH_DUAL = "chave_dupla",
    BRAILLE_KEYBOARD = "teclado_braille",
    GESTURE = "gesto",
    BRAIN_INTERFACE = "interface_cerebral",
    TOUCH = "toque",
    TRACKBALL = "trackball",
    MOUTH_STICK = "ponteiro_bocal",
    FOOT_PEDAL = "pedal_pe",
    PREDICTIVE = "preditivo",
}

// decorador: @dataclass
#[derive(Debug, Clone)]
struct InputConfiguration {
    primary_mode: InputMode,
    secondary_mode: Option<InputMode>,
    dwell_time_ms: i32,
    scan_rate_ms: i32,
    voice_language: String,
    voice_code_dialect: String,
    predictive_aggressiveness: f64,
    debounce_ms: i32,
    chord_input: bool,
    sticky_keys: bool,
    slow_keys: bool,
    repeat_rate: i32,
}

impl Default for InputConfiguration {
    fn default() -> Self {
        Self {
            primary_mode: InputMode::KEYBOARD_FULL,
            secondary_mode: None,
            dwell_time_ms: 500,
            scan_rate_ms: 2000,
            voice_language: "pt-BR".to_string(),
            voice_code_dialect: "portugol_pp".to_string(),
            predictive_aggressiveness: 0.8,
            debounce_ms: 0,
            chord_input: false,
            sticky_keys: false,
            slow_keys: false,
            repeat_rate: 0,
        }
    }
}

fn recommend_input(profile: &DeveloperProfile) -> InputConfiguration {
    let mut config = InputConfiguration::default();
    for d in &profile.disabilities {
        if d.category == DisabilityCategory::VISUAL {
            if matches!(d.severity, DisabilitySeverity::SEVERE | DisabilitySeverity::PROFOUND) {
                config.primary_mode = InputMode::BRAILLE_KEYBOARD;
                config.secondary_mode = Some(InputMode::VOICE_CODE);
            } else if d.severity == DisabilitySeverity::MODERATE {
                config.primary_mode = InputMode::VOICE_CODE;
                config.secondary_mode = Some(InputMode::KEYBOARD_FULL);
            }
        } else if d.category == DisabilityCategory::MOTOR {
            if d.specifics.iter().any(|s| s == "tetraplegia") || d.severity == DisabilitySeverity::PROFOUND {
                config.primary_mode = InputMode::VOICE_CODE;
                config.secondary_mode = Some(InputMode::EYE_TRACKING);
                config.dwell_time_ms = 300;
            } else if d.specifics.iter().any(|s| s == "amputado" || s == "uma_mao") {
                config.primary_mode = InputMode::KEYBOARD_ONE_HAND;
                config.chord_input = true;
            } else if d.specifics.iter().any(|s| s == "tremor" || s == "parkinson") {
                config.primary_mode = InputMode::TRACKBALL;
                config.debounce_ms = 150;
                config.slow_keys = true;
            } else if matches!(d.severity, DisabilitySeverity::SEVERE | DisabilitySeverity::PROFOUND) {
                config.primary_mode = InputMode::SWITCH_DUAL;
                config.scan_rate_ms = 1500;
            }
        } else if d.category == DisabilityCategory::AUTISM_SPECTRUM {
            config.predictive_aggressiveness = 0.5;
        } else if d.category == DisabilityCategory::COGNITIVE {
            if d.specifics.iter().any(|s| s == "dislexia") {
                config.predictive_aggressiveness = 0.9;
            }
            config.sticky_keys = true;
        } else if d.category == DisabilityCategory::NEUROLOGICAL {
            if d.specifics.iter().any(|s| s == "epilepsia") {
                config.repeat_rate = 0;
            }
            if d.specifics.iter().any(|s| s == "les") {
                config.primary_mode = InputMode::VOICE;
                config.secondary_mode = Some(InputMode::KEYBOARD_FULL);
            }
        }
    }
    config
}

// ============================================================================
// 4. MODOS DE SAIDA (Output/Display)
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
enum OutputMode {
    VISUAL_TEXT = "texto_visual",
    VISUAL_HIGH_CONTRAST = "alto_contraste",
    VISUAL_LARGE = "texto_grande",
    VISUAL_DYSLEXIA = "fonte_dislexia",
    AUDIO_TTS = "texto_para_voz",
    AUDIO_SONIFICATION = "sonificacao",
    HAPTIC = "haptico",
    BRAILLE_DISPLAY = "display_braille",
    COLOR_BLIND = "daltonismo",
    DARK_CALM = "escuro_calmo",
    MINIMAL = "minimal",
}

#[derive(Debug, Clone, PartialEq)]
enum ColorBlindnessType {
    NONE = "nenhum",
    PROTANOPIA = "protanopia",
    DEUTERANOPIA = "deuteranopia",
    TRITANOPIA = "tritanopia",
    ACHROMATOPSIA = "acromatopsia",
    PROTANOMALIA = "protanomalia",
    DEUTERANOMALIA = "deuteranomalia",
}

// decorador: @dataclass
#[derive(Debug, Clone)]
struct OutputConfiguration {
    primary_mode: OutputMode,
    tts_enabled: bool,
    tts_voice: String,
    tts_rate: f64,
    font_family: String,
    font_size_pt: i32,
    line_height: f64,
    letter_spacing: f64,
    high_contrast: bool,
    dark_mode: bool,
    color_blind: ColorBlindnessType,
    braille_cells: i32,
    haptic_enabled: bool,
    reduce_motion: bool,
    screen_dim_seconds: i32,
    syntax_highlight_style: String,
    error_display: String,
}

impl Default for OutputConfiguration {
    fn default() -> Self {
        Self {
            primary_mode: OutputMode::VISUAL_TEXT,
            tts_enabled: false,
            tts_voice: "pt-BR-Neural".to_string(),
            tts_rate: 1.0,
            font_family: "JetBrains Mono".to_string(),
            font_size_pt: 14,
            line_height: 1.5,
            letter_spacing: 0.0,
            high_contrast: false,
            dark_mode: true,
            color_blind: ColorBlindnessType::NONE,
            braille_cells: 40,
            haptic_enabled: false,
            reduce_motion: false,
            screen_dim_seconds: 0,
            syntax_highlight_style: "calm".to_string(),
            error_display: "visual".to_string(),
        }
    }
}

fn recommend_output(profile: &DeveloperProfile) -> OutputConfiguration {
    let mut config = OutputConfiguration::default();
    for d in &profile.disabilities {
        if d.category == DisabilityCategory::VISUAL {
            if matches!(d.severity, DisabilitySeverity::SEVERE | DisabilitySeverity::PROFOUND) {
                config.primary_mode = OutputMode::BRAILLE_DISPLAY;
                config.tts_enabled = true;
                config.tts_rate = 1.5;
            } else if d.severity == DisabilitySeverity::MODERATE {
                config.primary_mode = OutputMode::VISUAL_LARGE;
                config.font_size_pt = 24;
                config.high_contrast = true;
            }
            if d.specifics.iter().any(|s| s == "daltonismo") {
                for cb in [ColorBlindnessType::PROTANOPIA, ColorBlindnessType::DEUTERANOPIA, ColorBlindnessType::TRITANOPIA, ColorBlindnessType::ACHROMATOPSIA] {
                    if d.specifics.iter().any(|spec| spec == &format!("{:?}", cb).to_lowercase()) {
                        config.color_blind = cb;
                        break;
                    }
                }
            }
        } else if d.category == DisabilityCategory::AUDITORY {
            config.primary_mode = OutputMode::VISUAL_TEXT;
            config.tts_enabled = false;
            config.error_display = "visual".to_string();
            config.haptic_enabled = true;
        } else if d.category == DisabilityCategory::COGNITIVE {
            if d.specifics.iter().any(|s| s == "dislexia") {
                config.font_family = "OpenDyslexic".to_string();
                config.letter_spacing = 0.12;
                config.line_height = 2.0;
                config.font_size_pt = 18;
            }
            if d.specifics.iter().any(|s| s == "tdah") {
                config.primary_mode = OutputMode::MINIMAL;
                config.dark_mode = true;
            }
        } else if d.category == DisabilityCategory::AUTISM_SPECTRUM {
            config.primary_mode = OutputMode::DARK_CALM;
            config.reduce_motion = true;
            config.syntax_highlight_style = "monochrome".to_string();
            config.dark_mode = true;
            config.screen_dim_seconds = 0;
        } else if d.category == DisabilityCategory::NEUROLOGICAL {
            if d.specifics.iter().any(|s| s == "epilepsia") {
                config.reduce_motion = true;
                config.dark_mode = true;
                config.syntax_highlight_style = "monochrome".to_string();
            }
            if d.specifics.iter().any(|s| s == "parkinson") {
                config.font_size_pt = 18;
            }
        } else if d.category == DisabilityCategory::DEVELOPMENTAL {
            config.font_size_pt = 20;
            config.line_height = 1.8;
            config.syntax_highlight_style = "high_contrast_simple".to_string();
        }
    }
    config
}

// ============================================================================
// 5. ADAPTACOES DE CODIGO (Code Adaptation Layer)
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
enum CodeRepresentation {
    STANDARD = "texto_padrao",
    STRUCTURED_BLOCKS = "blocos",
    FLOWCHART = "fluxograma",
    NATURAL_LANGUAGE = "linguagem_natural",
    VOICE_FRIENDLY = "amigavel_voz",
    SIMPLIFIED = "simplificado",
    PORTUGOL_PP = "portugol_pp",
    SIGN_LANGUAGE = "libras",
}

// decorador: @dataclass
#[derive(Debug, Clone)]
struct CodeAdaptationConfig {
    representation: CodeRepresentation,
    indentation_guide: bool,
    bracket_matching_audio: bool,
    error_description_level: String,
    autocomplete_trigger: String,
    line_numbers_audio: bool,
    spell_check_code: bool,
    semantic_groups: bool,
    chunk_size: i32,
}

impl Default for CodeAdaptationConfig {
    fn default() -> Self {
        Self {
            representation: CodeRepresentation::STANDARD,
            indentation_guide: true,
            bracket_matching_audio: false,
            error_description_level: "detalhado".to_string(),
            autocomplete_trigger: "instant".to_string(),
            line_numbers_audio: false,
            spell_check_code: true,
            semantic_groups: false,
            chunk_size: 0,
        }
    }
}

fn adapt_code_config(profile: &DeveloperProfile) -> CodeAdaptationConfig {
    let mut config = CodeAdaptationConfig::default();
    for d in &profile.disabilities {
        if d.category == DisabilityCategory::VISUAL {
            if matches!(d.severity, DisabilitySeverity::SEVERE | DisabilitySeverity::PROFOUND) {
                config.representation = CodeRepresentation::VOICE_FRIENDLY;
                config.bracket_matching_audio = true;
                config.line_numbers_audio = true;
                config.error_description_level = "detalhado".to_string();
            }
        } else if d.category == DisabilityCategory::COGNITIVE {
            if d.specifics.iter().any(|s| s == "dislexia") {
                config.representation = CodeRepresentation::SIMPLIFIED;
                config.autocomplete_trigger = "predictive".to_string();
            }
            if d.specifics.iter().any(|s| s == "tdah") {
                config.chunk_size = 15;
                config.semantic_groups = true;
            }
        } else if d.category == DisabilityCategory::AUTISM_SPECTRUM {
            config.representation = CodeRepresentation::STRUCTURED_BLOCKS;
            config.semantic_groups = true;
        } else if d.category == DisabilityCategory::DEVELOPMENTAL {
            config.representation = CodeRepresentation::STRUCTURED_BLOCKS;
            config.error_description_level = "simples".to_string();
            config.chunk_size = 10;
        } else if d.category == DisabilityCategory::AUDITORY {
            config.representation = CodeRepresentation::FLOWCHART;
            config.error_description_level = "detalhado".to_string();
        }
    }
    config
}

// ============================================================================
// 6. FEEDBACK MULTIMODAL
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
enum FeedbackChannel {
    VISUAL = "visual",
    AUDIO = "audio",
    HAPTIC = "haptico",
    BRAILLE = "braille",
}

#[derive(Debug, Clone, PartialEq)]
enum FeedbackType {
    SUCCESS = "sucesso",
    ERROR = "erro",
    WARNING = "aviso",
    INFO = "info",
    COMPILATION_ERROR = "erro_compilacao",
    RUNTIME_ERROR = "erro_execucao",
    AUTOCOMPLETE_AVAILABLE = "autocomplete",
    SYNTAX_HIGHLIGHT = "sintaxe",
    BREAKPOINT_HIT = "breakpoint",
    TEST_PASS = "teste_passou",
    TEST_FAIL = "teste_falhou",
}

// decorador: @dataclass
#[derive(Debug, Clone)]
struct FeedbackSignal {
    feedback_type: FeedbackType,
    channels: Vec<FeedbackChannel>,
    visual_cue: Option<String>,
    audio_cue: Option<String>,
    haptic_pattern: Option<String>,
    braille_pattern: Option<String>,
    urgency: i32,
}

struct FeedbackEngine {
    profile: DeveloperProfile,
    output_config: OutputConfiguration,
    signals: HashMap<FeedbackType, FeedbackSignal>,
}

impl FeedbackEngine {
    fn new(profile: DeveloperProfile) -> Self {
        let output_config = recommend_output(&profile);
        let mut engine = Self { profile, output_config, signals: HashMap::new() };
        engine._build_signals();
        engine
    }

    fn _build_signals(&mut self) {
        for ft in [
            FeedbackType::SUCCESS, FeedbackType::ERROR, FeedbackType::WARNING, FeedbackType::INFO,
            FeedbackType::COMPILATION_ERROR, FeedbackType::RUNTIME_ERROR, FeedbackType::AUTOCOMPLETE_AVAILABLE,
            FeedbackType::SYNTAX_HIGHLIGHT, FeedbackType::BREAKPOINT_HIT, FeedbackType::TEST_PASS, FeedbackType::TEST_FAIL
        ] {
            let mut channels = vec![];
            let mut visual = None;
            let mut audio = None;
            let mut haptic = None;
            let mut braille = None;

            let mut has_visual = true;
            let mut has_audio = true;
            let has_haptic = self.output_config.haptic_enabled;

            for d in &self.profile.disabilities {
                if d.category == DisabilityCategory::VISUAL && matches!(d.severity, DisabilitySeverity::SEVERE | DisabilitySeverity::PROFOUND) {
                    has_visual = false;
                }
                if d.category == DisabilityCategory::AUDITORY {
                    has_audio = false;
                }
            }

            if has_visual { channels.push(FeedbackChannel::VISUAL); }
            if has_audio { channels.push(FeedbackChannel::AUDIO); }
            if has_haptic { channels.push(FeedbackChannel::HAPTIC); }

            if self.output_config.primary_mode == OutputMode::BRAILLE_DISPLAY {
                channels.push(FeedbackChannel::BRAILLE);
            }

            if ft == FeedbackType::ERROR || ft == FeedbackType::COMPILATION_ERROR {
                visual = Some("borda vermelha + mensagem".to_string());
                audio = Some("tom grave curto".to_string());
                haptic = Some("vibracao dupla forte".to_string());
                braille = Some("erro".to_string());
            } else if ft == FeedbackType::SUCCESS || ft == FeedbackType::TEST_PASS {
                visual = Some("borda verde discreta".to_string());
                audio = Some("tom agudo curto (apenas se solicitado)".to_string());
                haptic = Some("vibracao suave unica".to_string());
                braille = Some("ok".to_string());
            } else if ft == FeedbackType::WARNING {
                visual = Some("borda amarela".to_string());
                audio = Some("ton medio curto".to_string());
                haptic = Some("vibracao unica media".to_string());
                braille = Some("aviso".to_string());
            } else if ft == FeedbackType::TEST_FAIL {
                visual = Some("linha vermelha no teste".to_string());
                audio = Some("tom descendente".to_string());
                haptic = Some("vibracao tripla".to_string());
                braille = Some("falhou".to_string());
            }

            self.signals.insert(ft, FeedbackSignal {
                feedback_type: ft,
                channels,
                visual_cue: visual,
                audio_cue: audio,
                haptic_pattern: haptic,
                braille_pattern: braille,
                urgency: 1,
            });
        }
    }

    fn emit(&self, feedback_type: FeedbackType) -> FeedbackSignal {
        self.signals.get(&feedback_type).cloned().unwrap_or_else(|| self.signals[&FeedbackType::INFO].clone())
    }
}

// ============================================================================
// 7. AMBIENTE SENSORIAL (Sensory Environment)
// ============================================================================

// decorador: @dataclass
#[derive(Debug, Clone)]
struct SensoryEnvironment {
    brightness: f64,
    contrast_ratio: f64,
    color_temperature_k: i32,
    animation_enabled: bool,
    animation_speed: f64,
    sound_enabled: bool,
    notifications_enabled: bool,
    max_visual_elements: i32,
    flicker_rate_hz: i32,
    background: String,
    reduce_noise: bool,
    dark_mode: bool,
}

impl Default for SensoryEnvironment {
    fn default() -> Self {
        Self {
            brightness: 0.5,
            contrast_ratio: 4.5,
            color_temperature_k: 3000,
            animation_enabled: true,
            animation_speed: 1.0,
            sound_enabled: false,
            notifications_enabled: false,
            max_visual_elements: 0,
            flicker_rate_hz: 0,
            background: "solid".to_string(),
            reduce_noise: false,
            dark_mode: true,
        }
    }
}

impl SensoryEnvironment {
    fn apply_calming(&mut self) {
        self.brightness = 0.3;
        self.animation_enabled = false;
        self.sound_enabled = false;
        self.notifications_enabled = false;
        self.max_visual_elements = 7;
        self.background = "solid".to_string();
        self.reduce_noise = true;
        self.flicker_rate_hz = 0;
    }
}

fn configure_environment(profile: &DeveloperProfile) -> SensoryEnvironment {
    let mut env = SensoryEnvironment::default();
    for d in &profile.disabilities {
        if d.category == DisabilityCategory::AUTISM_SPECTRUM {
            env.apply_calming();
            env.color_temperature_k = 2700;
        } else if d.category == DisabilityCategory::NEUROLOGICAL {
            if d.specifics.iter().any(|s| s == "epilepsia") {
                env.flicker_rate_hz = 0;
                env.animation_enabled = false;
                env.brightness = 0.4;
                env.contrast_ratio = 7.0;
                env.color_temperature_k = 3000;
            }
        } else if d.category == DisabilityCategory::VISUAL {
            if matches!(d.severity, DisabilitySeverity::MODERATE | DisabilitySeverity::SEVERE) {
                env.contrast_ratio = 7.0;
                env.brightness = 0.7;
            }
        } else if d.category == DisabilityCategory::COGNITIVE {
            if d.specifics.iter().any(|s| s == "tdah") {
                env.max_visual_elements = 5;
                env.notifications_enabled = false;
                env.animation_enabled = false;
            }
        } else if d.category == DisabilityCategory::AUDITORY {
            env.sound_enabled = false;
        }
    }
    env
}

// ============================================================================
// 8. ASSISTENTE DE IA INCLUSIVO (IA as Amplifier)
// ============================================================================

// decorador: @dataclass
#[derive(Debug, Clone)]
struct AIAssistanceConfig {
    enabled: bool,
    auto_describe_code: bool,
    auto_fix_accessibility: bool,
    voice_interaction: bool,
    simplify_errors: bool,
    predict_next_line: bool,
    translate_to_portugol: bool,
    sign_language_avatar: bool,
    cognitive_load_monitor: bool,
    break_reminder: bool,
}

impl Default for AIAssistanceConfig {
    fn default() -> Self {
        Self {
            enabled: true,
            auto_describe_code: false,
            auto_fix_accessibility: true,
            voice_interaction: false,
            simplify_errors: true,
            predict_next_line: true,
            translate_to_portugol: true,
            sign_language_avatar: false,
            cognitive_load_monitor: true,
            break_reminder: true,
        }
    }
}

impl AIAssistanceConfig {
    fn adapt(&mut self, profile: &DeveloperProfile) {
        for d in &profile.disabilities {
            if d.category == DisabilityCategory::VISUAL {
                if matches!(d.severity, DisabilitySeverity::SEVERE | DisabilitySeverity::PROFOUND) {
                    self.voice_interaction = true;
                    self.auto_describe_code = true;
                }
            } else if d.category == DisabilityCategory::AUDITORY {
                self.voice_interaction = false;
                self.sign_language_avatar = true;
            } else if d.category == DisabilityCategory::COGNITIVE {
                self.simplify_errors = true;
                self.predict_next_line = true;
            } else if d.category == DisabilityCategory::AUTISM_SPECTRUM {
                self.predict_next_line = false;
                self.cognitive_load_monitor = true;
            } else if d.category == DisabilityCategory::DEVELOPMENTAL {
                self.simplify_errors = true;
                self.auto_describe_code = true;
                self.translate_to_portugol = true;
            } else if d.category == DisabilityCategory::COMMUNICATION {
                self.voice_interaction = true;
                self.sign_language_avatar = true;
            }
        }
    }
}

// ============================================================================
// 9. NAVEGACAO DE CODIGO ADAPTADA
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
enum NavigationMode {
    LINE_BY_LINE = "linha_a_linha",
    BLOCK_BY_BLOCK = "bloco_a_bloco",
    SEMANTIC = "semantica",
    AUDIO_OUTLINE = "outline_audio",
    TREE = "arvore",
    MINIMAP = "minimapa",
    BRAILLE_NAV = "navegacao_braille",
}

// decorador: @dataclass
#[derive(Debug, Clone)]
struct NavigationConfig {
    mode: NavigationMode,
    auto_collapse_depth: i32,
    announce_position: bool,
    jump_targets: Vec<String>,
}

impl Default for NavigationConfig {
    fn default() -> Self {
        Self {
            mode: NavigationMode::LINE_BY_LINE,
            auto_collapse_depth: 2,
            announce_position: false,
            jump_targets: vec!["funcao".to_string(), "classe".to_string(), "loop".to_string(), "condicao".to_string(), "retorno".to_string(), "erro".to_string()],
        }
    }
}

fn recommend_navigation(profile: &DeveloperProfile) -> NavigationConfig {
    let mut config = NavigationConfig::default();
    for d in &profile.disabilities {
        if d.category == DisabilityCategory::VISUAL {
            if matches!(d.severity, DisabilitySeverity::SEVERE | DisabilitySeverity::PROFOUND) {
                config.mode = NavigationMode::BRAILLE_NAV;
                config.announce_position = true;
            }
        } else if d.category == DisabilityCategory::COGNITIVE {
            config.mode = NavigationMode::BLOCK_BY_BLOCK;
            config.auto_collapse_depth = 1;
        } else if d.category == DisabilityCategory::AUTISM_SPECTRUM {
            config.mode = NavigationMode::TREE;
            config.auto_collapse_depth = 1;
        } else if d.category == DisabilityCategory::DEVELOPMENTAL {
            config.mode = NavigationMode::TREE;
            config.auto_collapse_depth = 1;
        }
    }
    config
}

// ============================================================================
// 10. VERIFICACAO DE ACESSIBILIDADE DO CODIGO (a11y lint)
// ============================================================================

// decorador: @dataclass
#[derive(Debug, Clone)]
struct AccessibilityCheck {
    check_id: String,
    description: String,
    severity: String,
    suggestion: String,
}

const A11Y_CHECKS: &[AccessibilityCheck] = &[
    AccessibilityCheck { check_id: "A11Y-001".to_string(), description: "Contraste de cores no output do programa".to_string(), severity: "warning".to_string(), suggestion: "Use contraste minimo 4.5:1 (WCAG AA)".to_string() },
    AccessibilityCheck { check_id: "A11Y-002".to_string(), description: "Texto alternativo em imagens/icones do programa".to_string(), severity: "error".to_string(), suggestion: "Todo elemento visual deve ter descricao para screen readers".to_string() },
    AccessibilityCheck { check_id: "A11Y-003".to_string(), description: "Navegacao por teclado no programa".to_string(), severity: "error".to_string(), suggestion: "Todo interativo deve ser acessivel por teclado (Tab/Enter)".to_string() },
    AccessibilityCheck { check_id: "A11Y-004".to_string(), description: "Nao use so cor para transmitir informacao".to_string(), severity: "warning".to_string(), suggestion: "Adicione texto ou icone junto com cor".to_string() },
    AccessibilityCheck { check_id: "A11Y-005".to_string(), description: "Tamanho de fonte minimo no output".to_string(), severity: "info".to_string(), suggestion: "Minimo 16px para texto, 14px para codigo".to_string() },
    AccessibilityCheck { check_id: "A11Y-006".to_string(), description: "Animacoes devem ter opcao de desativar".to_string(), severity: "warning".to_string(), suggestion: "prefers-reduced-motion deve ser respeitado".to_string() },
    AccessibilityCheck { check_id: "A11Y-007".to_string(), description: "Audio deve ter legenda/transcricao".to_string(), severity: "error".to_string(), suggestion: "Todo audio deve ter alternativa textual".to_string() },
    AccessibilityCheck { check_id: "A11Y-008".to_string(), description: "Forms devem ter labels".to_string(), severity: "error".to_string(), suggestion: "Todo input deve ter label associado".to_string() },
    AccessibilityCheck { check_id: "A11Y-009".to_string(), description: "Sem padroes que causam seizures".to_string(), severity: "error".to_string(), suggestion: "Nada que pisque mais que 3x por segundo (WCAG 2.3.1)".to_string() },
    AccessibilityCheck { check_id: "A11Y-010".to_string(), description: "Linguagem simples e clara".to_string(), severity: "info".to_string(), suggestion: "Prefira linguagem direta e simples no codigo e comentarios".to_string() },
];

fn run_a11y_lint(_code: &str, _profile: &DeveloperProfile) -> Vec<AccessibilityCheck> {
    A11Y_CHECKS.to_vec()
}

// ============================================================================
// 11. PERFIS PRE-CONFIGURADOS (Quick Setup)
// ============================================================================

fn create_profile_blind() -> DeveloperProfile {
    DeveloperProfile::new(
        "blind_dev".to_string(),
        "Dev Cego".to_string(),
        vec![DisabilityProfile::new(DisabilityCategory::VISUAL, DisabilitySeverity::PROFOUND, vec!["cegueira_total".to_string()], vec!["screen_reader".to_string(), "braille_display".to_string(), "talon_voice".to_string()])],
        HashMap::from([("tts_rate".to_string(), "2.0".to_string()), ("braille_cells".to_string(), "40".to_string())]),
        1.0, 0.3,
    )
}

fn create_profile_deaf() -> DeveloperProfile {
    DeveloperProfile::new(
        "deaf_dev".to_string(),
        "Dev Surdo".to_string(),
        vec![DisabilityProfile::new(DisabilityCategory::AUDITORY, DisabilitySeverity::PROFOUND, vec!["surdez_profunda".to_string()], vec!["visual_alerts".to_string()])],
        HashMap::new(),
        1.0, 0.3,
    )
}

fn create_profile_motor_severe() -> DeveloperProfile {
    DeveloperProfile::new(
        "motor_dev".to_string(),
        "Dev Tetraplegico".to_string(),
        vec![DisabilityProfile::new(DisabilityCategory::MOTOR, DisabilitySeverity::PROFOUND, vec!["tetraplegia".to_string()], vec!["eye_tracker".to_string(), "voice_control".to_string(), "switch".to_string()])],
        HashMap::new(),
        1.0, 0.3,
    )
}

fn create_profile_dyslexia() -> DeveloperProfile {
    DeveloperProfile::new(
        "dyslexia_dev".to_string(),
        "Dev Dislexico".to_string(),
        vec![DisabilityProfile::new(DisabilityCategory::COGNITIVE, DisabilitySeverity::MODERATE, vec!["dislexia".to_string()], vec![])],
        HashMap::new(),
        1.0, 0.3,
    )
}

fn create_profile_adhd() -> DeveloperProfile {
    DeveloperProfile::new(
        "adhd_dev".to_string(),
        "Dev TDAH".to_string(),
        vec![DisabilityProfile::new(DisabilityCategory::COGNITIVE, DisabilitySeverity::MODERATE, vec!["tdah".to_string()], vec![])],
        HashMap::new(),
        1.0, 0.3,
    )
}

fn create_profile_autism() -> DeveloperProfile {
    DeveloperProfile::new(
        "autism_dev".to_string(),
        "Dev Autista".to_string(),
        vec![DisabilityProfile::new(DisabilityCategory::AUTISM_SPECTRUM, DisabilitySeverity::MODERATE, vec!["hipersensibilidade_sensorial".to_string(), "sobrecarga".to_string()], vec![])],
        HashMap::new(),
        1.0, 0.3,
    )
}

fn create_profile_epilepsy() -> DeveloperProfile {
    DeveloperProfile::new(
        "epilepsy_dev".to_string(),
        "Dev Epileptico".to_string(),
        vec![DisabilityProfile::new(DisabilityCategory::NEUROLOGICAL, DisabilitySeverity::MODERATE, vec!["epilepsia_fotossensivel".to_string()], vec![])],
        HashMap::new(),
        1.0, 0.3,
    )
}

fn create_profile_down() -> DeveloperProfile {
    DeveloperProfile::new(
        "down_dev".to_string(),
        "Dev Down".to_string(),
        vec![DisabilityProfile::new(DisabilityCategory::DEVELOPMENTAL, DisabilitySeverity::MODERATE, vec!["sindrome_down".to_string()], vec![])],
        HashMap::new(),
        1.0, 0.3,
    )
}

fn create_profile_multiple() -> DeveloperProfile {
    DeveloperProfile::new(
        "multi_dev".to_string(),
        "Dev Multipla".to_string(),
        vec![
            DisabilityProfile::new(DisabilityCategory::VISUAL, DisabilitySeverity::MODERATE, vec!["baixa_visao".to_string()], vec![]),
            DisabilityProfile::new(DisabilityCategory::MOTOR, DisabilitySeverity::MODERATE, vec!["distrofia".to_string(), "tremor".to_string()], vec![]),
        ],
        HashMap::new(),
        1.0, 0.3,
    )
}

fn create_profile_temporary() -> DeveloperProfile {
    DeveloperProfile::new(
        "temp_dev".to_string(),
        "Dev Temporario".to_string(),
        vec![DisabilityProfile::new(DisabilityCategory::TEMPORARY, DisabilitySeverity::MODERATE, vec!["lesao_temporaria".to_string(), "fatiga_extrema".to_string()], vec![])],
        HashMap::new(),
        1.0, 0.3,
    )
}

// ============================================================================
// 12. IDE COMPLETA (Orquestrador)
// ============================================================================

struct OpenInclusiveIDE {
    profile: DeveloperProfile,
    input_config: InputConfiguration,
    output_config: OutputConfiguration,
    code_config: CodeAdaptationConfig,
    environment: SensoryEnvironment,
    navigation: NavigationConfig,
    feedback_engine: FeedbackEngine,
    ai_config: AIAssistanceConfig,
    session_active: bool,
    errors_emitted: Vec<String>,
    session_start_time: Option<String>,
}

impl OpenInclusiveIDE {
    fn new(profile: DeveloperProfile) -> Self {
        let input_config = recommend_input(&profile);
        let output_config = recommend_output(&profile);
        let code_config = adapt_code_config(&profile);
        let environment = configure_environment(&profile);
        let navigation = recommend_navigation(&profile);
        let feedback_engine = FeedbackEngine::new(profile.clone());
        let mut ai_config = AIAssistanceConfig::default();
        ai_config.adapt(&profile);
        Self {
            profile,
            input_config,
            output_config,
            code_config,
            environment,
            navigation,
            feedback_engine,
            ai_config,
            session_active: false,
            errors_emitted: vec![],
            session_start_time: None,
        }
    }

    fn start_session(&mut self) -> HashMap<String, String> {
        self.session_active = true;
        let mut result = HashMap::new();
        result.insert("profile".to_string(), self.profile.name.clone());
        result.insert("input".to_string(), format!("{:?}", self.input_config.primary_mode));
        result.insert("output".to_string(), format!("{:?}", self.output_config.primary_mode));
        result.insert("code_representation".to_string(), format!("{:?}", self.code_config.representation));
        result.insert("navigation".to_string(), format!("{:?}", self.navigation.mode));
        result.insert("ai_assistance".to_string(), self.ai_config.enabled.to_string());
        result.insert("session_active".to_string(), "true".to_string());
        result
    }

    fn display_code(&self, code: &str) -> HashMap<String, String> {
        let mut result = HashMap::new();
        result.insert("original_lines".to_string(), code.lines().count().to_string());
        result.insert("representation".to_string(), format!("{:?}", self.code_config.representation));
        result.insert("font".to_string(), self.output_config.font_family.clone());
        result.insert("font_size".to_string(), self.output_config.font_size_pt.to_string());
        result
    }

    fn handle_error(&mut self, error_message: &str) -> FeedbackSignal {
        self.errors_emitted.push(error_message.to_string());
        let msg = if self.ai_config.simplify_errors {
            self._simplify_error(error_message)
        } else {
            error_message.to_string()
        };
        self.feedback_engine.emit(FeedbackType::ERROR)
    }

    fn handle_success(&self) -> FeedbackSignal {
        self.feedback_engine.emit(FeedbackType::SUCCESS)
    }

    fn handle_test_result(&self, passed: bool) -> FeedbackSignal {
        if passed {
            self.feedback_engine.emit(FeedbackType::TEST_PASS)
        } else {
            self.feedback_engine.emit(FeedbackType::TEST_FAIL)
        }
    }

    fn check_energy(&self) -> HashMap<String, String> {
        let energy = self.profile.effective_energy();
        let low = self.profile.is_low_energy();
        let mut result = HashMap::new();
        result.insert("energy_level".to_string(), format!("{:.2}", energy));
        result.insert("low_energy".to_string(), low.to_string());
        result.insert("recommend_break".to_string(), low.to_string());
        result.insert("message".to_string(), if low { "Energia baixa. Hora de descansar. (OpenAbsence)".to_string() } else { "Energia ok. Continue.".to_string() });
        result
    }

    fn run_a11y_check(&self, code: &str) -> Vec<AccessibilityCheck> {
        run_a11y_lint(code, &self.profile)
    }

    fn _simplify_error(&self, message: &str) -> String {
        let translations: HashMap<&str, &str> = HashMap::from([
            ("SyntaxError", "Tem algo errado na escrita do codigo. Verifique a linha indicada."),
            ("IndentationError", "O espacamento esta errado. Cada bloco precisa estar alinhado."),
            ("TypeError", "Os tipos nao combinam. Voce esta misturando texto com numero, por exemplo."),
            ("NameError", "Uma variavel nao foi definida. Verifique se voce escreveu o nome certo."),
            ("IndexError", "Voce tentou acessar uma posicao que nao existe na lista."),
            ("KeyError", "Essa chave nao existe no dicionario."),
            ("AttributeError", "Esse objeto nao tem essa propriedade."),
            ("ImportError", "Nao conseguiu encontrar o modulo. Verifique se esta instalado."),
        ]);
        for (tech, simple) in translations {
            if message.contains(tech) {
                return format!("{} (Detalhe tecnico: {})", simple, message);
            }
        }
        message.to_string()
    }

    fn session_summary(&self) -> HashMap<String, String> {
        let mut result = HashMap::new();
        result.insert("profile".to_string(), self.profile.name.clone());
        result.insert("total_errors".to_string(), self.errors_emitted.len().to_string());
        result.insert("input_mode".to_string(), format!("{:?}", self.input_config.primary_mode));
        result.insert("output_mode".to_string(), format!("{:?}", self.output_config.primary_mode));
        result
    }
}

// ============================================================================
// 13. DEMONSTRACAO
// ============================================================================

fn demo() {
    println!("{}", "=".repeat(70));
    println!("OpenInclusiveIDE -- IDE para TODAS as Deficiencias");
    println!("{}", "=".repeat(70));

    let profiles: Vec<(&str, DeveloperProfile)> = vec![
        ("Cego", create_profile_blind()),
        ("Surdo", create_profile_deaf()),
        ("Tetraplegico", create_profile_motor_severe()),
        ("Dislexia", create_profile_dyslexia()),
        ("TDAH", create_profile_adhd()),
        ("Autista", create_profile_autism()),
        ("Epilepsia", create_profile_epilepsy()),
        ("Sindrome de Down", create_profile_down()),
        ("Multipla (baixa visao + motor)", create_profile_multiple()),
        ("Temporaria (lesao)", create_profile_temporary()),
    ];

    for (label, profile) in profiles {
        println!("\n{}", "-".repeat(50));
        println!("PERFIL: {}", label);
        println!("{}", "-".repeat(50));

        let mut ide = OpenInclusiveIDE::new(profile);
        let session = ide.start_session();

        println!("  Input:      {}", session.get("input").unwrap_or(&"".to_string()));
        println!("  Output:     {}", session.get("output").unwrap_or(&"".to_string()));
        println!("  Codigo:     {}", session.get("code_representation").unwrap_or(&"".to_string()));
        println!("  Navegacao:  {}", session.get("navigation").unwrap_or(&"".to_string()));
        println!("  IA:         {}", session.get("ai_assistance").unwrap_or(&"".to_string()));

        let error_feedback = ide.handle_error("SyntaxError: invalid syntax on line 5");
        println!("  Erro feedback canais: {:?}", error_feedback.channels.iter().map(|c| format!("{:?}", c)).collect::<Vec<_>>());

        let energy = ide.check_energy();
        println!("  Energia:    {}", energy.get("energy_level").unwrap_or(&"".to_string()));
    }

    println!("\n{}", "=".repeat(70));
    println!("VERIFICACAO DE ACESSIBILIDADE (a11y lint)");
    println!("{}", "=".repeat(70));
    for check in A11Y_CHECKS {
        println!("  [{:8}] {}: {}", check.severity.to_uppercase(), check.check_id, check.description);
    }

    println!("\n{}", "=".repeat(70));
    println!("COBERTURA DE DEFICIENCIAS");
    println!("{}", "=".repeat(70));
    // simplified for brevity in main demo
    println!("Total de categorias: 10");
    println!("Total de modos de entrada: 17");
    println!("Total de modos de saida: 11");
    println!("Total de verificacoes a11y: 10");
    println!("Total de representacoes de codigo: 8");

    println!("\nIDE INCLUSIVA. ZERO BARREIRA. TODA DEFICIENCIA COBERTA.");
}

fn main() {
    demo();
}
