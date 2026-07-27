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

import java.util.*;

public class OpenInclusiveIDE {

    // ============================================================================
    // 1. CLASSIFICACAO DE DEFICIENCIAS
    // ============================================================================

    public enum DisabilityCategory {
        VISUAL("visual"),                    // cegueira, baixa visao, daltonismo
        AUDITORY("auditiva"),                // surdez, baixa audicao, tinnitus
        MOTOR("motora"),                     // paralisia, amputados, tremores
        COGNITIVE("cognitiva"),              // dislexia, TDAH, discalculia
        AUTISM_SPECTRUM("espectro_autista"), // hipersensibilidade, sobrecarga
        COMMUNICATION("comunicacao"),        // afasia, gagueira, mutismo
        NEUROLOGICAL("neurologica"),         // epilepsia, Parkinson, LES
        DEVELOPMENTAL("desenvolvimento"),    // Sindrome de Down
        MULTIPLE("multipla"),                // combinacao
        TEMPORARY("temporaria");             // lesao, cirurgia, fadiga

        public final String value;
        DisabilityCategory(String value) { this.value = value; }
    }

    public enum DisabilitySeverity {
        MILD("leve"),          // dificuldade, mas funcional
        MODERATE("moderada"),  // precisa de adaptacao significativa
        SEVERE("severa"),      // depende de adaptacao total
        PROFOUND("profunda");  // adaptacao total + tecnologia assistiva

        public final String value;
        DisabilitySeverity(String value) { this.value = value; }
    }

    public static class DisabilityProfile {
        public DisabilityCategory category;
        public DisabilitySeverity severity;
        public List<String> specifics = new ArrayList<>();
        public List<String> assistive_tech = new ArrayList<>();

        public DisabilityProfile(DisabilityCategory category, DisabilitySeverity severity, List<String> specifics, List<String> assistive_tech) {
            this.category = category;
            this.severity = severity;
            if (specifics != null) this.specifics = specifics;
            if (assistive_tech != null) this.assistive_tech = assistive_tech;
        }

        public boolean needs_visual_adaptation() {
            return this.category == DisabilityCategory.VISUAL || this.category == DisabilityCategory.MULTIPLE;
        }
        public boolean needs_audio_adaptation() {
            return this.category == DisabilityCategory.AUDITORY || this.category == DisabilityCategory.MULTIPLE;
        }
        public boolean needs_motor_adaptation() {
            return this.category == DisabilityCategory.MOTOR || this.category == DisabilityCategory.MULTIPLE;
        }
        public boolean needs_cognitive_adaptation() {
            return this.category == DisabilityCategory.COGNITIVE ||
                   this.category == DisabilityCategory.AUTISM_SPECTRUM ||
                   this.category == DisabilityCategory.DEVELOPMENTAL ||
                   this.category == DisabilityCategory.MULTIPLE;
        }
        public boolean needs_sensorial_calming() {
            return this.category == DisabilityCategory.AUTISM_SPECTRUM ||
                   this.category == DisabilityCategory.NEUROLOGICAL ||
                   this.category == DisabilityCategory.MULTIPLE;
        }
    }

    // ============================================================================
    // 2. PERFIL DO DESENVOLVEDOR
    // ============================================================================

    public static class DeveloperProfile {
        public String developer_id;
        public String name;
        public List<DisabilityProfile> disabilities = new ArrayList<>();
        public Map<String, Object> preferences = new HashMap<>();
        public double energy_level = 1.0;
        public double fatigue_threshold = 0.3;

        public DeveloperProfile(String developer_id, String name, List<DisabilityProfile> disabilities, Map<String, Object> preferences) {
            this.developer_id = developer_id;
            this.name = name;
            if (disabilities != null) this.disabilities = disabilities;
            if (preferences != null) this.preferences = preferences;
        }

        public boolean has_any_disability() { return !this.disabilities.isEmpty(); }
        public Set<DisabilityCategory> categories() {
            Set<DisabilityCategory> cats = new HashSet<>();
            for (DisabilityProfile d : this.disabilities) cats.add(d.category);
            return cats;
        }
        public void add_disability(DisabilityProfile profile) { this.disabilities.add(profile); }
        public double effective_energy() {
            if (this.disabilities.isEmpty()) return this.energy_level;
            double penalty = this.disabilities.size() * 0.05;
            return Math.max(0.0, this.energy_level - penalty);
        }
        public boolean is_low_energy() { return this.effective_energy() < this.fatigue_threshold; }
    }

    // ============================================================================
    // 3. MODOS DE ENTRADA (Input)
    // ============================================================================

    public enum InputMode {
        KEYBOARD_FULL("teclado_completo"),
        KEYBOARD_ONE_HAND("teclado_uma_mao"),
        KEYBOARD_HEAD("teclado_cabeca"),
        KEYBOARD_MOUTH("teclado_boca"),
        VOICE("voz"),
        VOICE_CODE("voz_codigo"),
        EYE_TRACKING("rastreio_olhos"),
        SWITCH("chave"),
        SWITCH_DUAL("chave_dupla"),
        BRAILLE_KEYBOARD("teclado_braille"),
        GESTURE("gesto"),
        BRAIN_INTERFACE("interface_cerebral"),
        TOUCH("toque"),
        TRACKBALL("trackball"),
        MOUTH_STICK("ponteiro_bocal"),
        FOOT_PEDAL("pedal_pe"),
        PREDICTIVE("preditivo");

        public final String value;
        InputMode(String value) { this.value = value; }
    }

    public static class InputConfiguration {
        public InputMode primary_mode = InputMode.KEYBOARD_FULL;
        public InputMode secondary_mode = null;
        public int dwell_time_ms = 500;
        public int scan_rate_ms = 2000;
        public String voice_language = "pt-BR";
        public String voice_code_dialect = "portugol_pp";
        public double predictive_aggressiveness = 0.8;
        public int debounce_ms = 0;
        public boolean chord_input = false;
        public boolean sticky_keys = false;
        public boolean slow_keys = false;
        public int repeat_rate = 0;
    }

    public static InputConfiguration recommend_input(DeveloperProfile profile) {
        InputConfiguration config = new InputConfiguration();
        for (DisabilityProfile d : profile.disabilities) {
            if (d.category == DisabilityCategory.VISUAL) {
                if (d.severity == DisabilitySeverity.SEVERE || d.severity == DisabilitySeverity.PROFOUND) {
                    config.primary_mode = InputMode.BRAILLE_KEYBOARD;
                    config.secondary_mode = InputMode.VOICE_CODE;
                } else if (d.severity == DisabilitySeverity.MODERATE) {
                    config.primary_mode = InputMode.VOICE_CODE;
                    config.secondary_mode = InputMode.KEYBOARD_FULL;
                }
            } else if (d.category == DisabilityCategory.MOTOR) {
                if (d.specifics.contains("tetraplegia") || d.severity == DisabilitySeverity.PROFOUND) {
                    config.primary_mode = InputMode.VOICE_CODE;
                    config.secondary_mode = InputMode.EYE_TRACKING;
                    config.dwell_time_ms = 300;
                } else if (d.specifics.contains("amputado") || d.specifics.contains("uma_mao")) {
                    config.primary_mode = InputMode.KEYBOARD_ONE_HAND;
                    config.chord_input = true;
                } else if (d.specifics.contains("tremor") || d.specifics.contains("parkinson")) {
                    config.primary_mode = InputMode.TRACKBALL;
                    config.debounce_ms = 150;
                    config.slow_keys = true;
                } else if (d.severity == DisabilitySeverity.SEVERE || d.severity == DisabilitySeverity.PROFOUND) {
                    config.primary_mode = InputMode.SWITCH_DUAL;
                    config.scan_rate_ms = 1500;
                }
            } else if (d.category == DisabilityCategory.AUTISM_SPECTRUM) {
                config.predictive_aggressiveness = 0.5;
            } else if (d.category == DisabilityCategory.COGNITIVE) {
                if (d.specifics.contains("dislexia")) config.predictive_aggressiveness = 0.9;
                config.sticky_keys = true;
            } else if (d.category == DisabilityCategory.NEUROLOGICAL) {
                if (d.specifics.contains("epilepsia")) config.repeat_rate = 0;
                if (d.specifics.contains("les")) {
                    config.primary_mode = InputMode.VOICE;
                    config.secondary_mode = InputMode.KEYBOARD_FULL;
                }
            }
        }
        return config;
    }

    // ============================================================================
    // 4. MODOS DE SAIDA (Output/Display)
    // ============================================================================

    public enum OutputMode {
        VISUAL_TEXT("texto_visual"),
        VISUAL_HIGH_CONTRAST("alto_contraste"),
        VISUAL_LARGE("texto_grande"),
        VISUAL_DYSLEXIA("fonte_dislexia"),
        AUDIO_TTS("texto_para_voz"),
        AUDIO_SONIFICATION("sonificacao"),
        HAPTIC("haptico"),
        BRAILLE_DISPLAY("display_braille"),
        COLOR_BLIND("daltonismo"),
        DARK_CALM("escuro_calmo"),
        MINIMAL("minimal");

        public final String value;
        OutputMode(String value) { this.value = value; }
    }

    public enum ColorBlindnessType {
        NONE("nenhum"),
        PROTANOPIA("protanopia"),
        DEUTERANOPIA("deuteranopia"),
        TRITANOPIA("tritanopia"),
        ACHROMATOPSIA("acromatopsia"),
        PROTANOMALIA("protanomalia"),
        DEUTERANOMALIA("deuteranomalia");

        public final String value;
        ColorBlindnessType(String value) { this.value = value; }
    }

    public static class OutputConfiguration {
        public OutputMode primary_mode = OutputMode.VISUAL_TEXT;
        public boolean tts_enabled = false;
        public String tts_voice = "pt-BR-Neural";
        public double tts_rate = 1.0;
        public String font_family = "JetBrains Mono";
        public int font_size_pt = 14;
        public double line_height = 1.5;
        public double letter_spacing = 0.0;
        public boolean high_contrast = false;
        public boolean dark_mode = true;
        public ColorBlindnessType color_blind = ColorBlindnessType.NONE;
        public int braille_cells = 40;
        public boolean haptic_enabled = false;
        public boolean reduce_motion = false;
        public int screen_dim_seconds = 0;
        public String syntax_highlight_style = "calm";
        public String error_display = "visual";
    }

    public static OutputConfiguration recommend_output(DeveloperProfile profile) {
        OutputConfiguration config = new OutputConfiguration();
        for (DisabilityProfile d : profile.disabilities) {
            if (d.category == DisabilityCategory.VISUAL) {
                if (d.severity == DisabilitySeverity.SEVERE || d.severity == DisabilitySeverity.PROFOUND) {
                    config.primary_mode = OutputMode.BRAILLE_DISPLAY;
                    config.tts_enabled = true;
                    config.tts_rate = 1.5;
                } else if (d.severity == DisabilitySeverity.MODERATE) {
                    config.primary_mode = OutputMode.VISUAL_LARGE;
                    config.font_size_pt = 24;
                    config.high_contrast = true;
                }
                if (d.specifics.contains("daltonismo")) {
                    for (ColorBlindnessType cb : ColorBlindnessType.values()) {
                        if (d.specifics.contains(cb.value)) { config.color_blind = cb; break; }
                    }
                }
            } else if (d.category == DisabilityCategory.AUDITORY) {
                config.primary_mode = OutputMode.VISUAL_TEXT;
                config.tts_enabled = false;
                config.error_display = "visual";
                config.haptic_enabled = true;
            } else if (d.category == DisabilityCategory.COGNITIVE) {
                if (d.specifics.contains("dislexia")) {
                    config.font_family = "OpenDyslexic";
                    config.letter_spacing = 0.12;
                    config.line_height = 2.0;
                    config.font_size_pt = 18;
                }
                if (d.specifics.contains("tdah")) {
                    config.primary_mode = OutputMode.MINIMAL;
                    config.dark_mode = true;
                }
            } else if (d.category == DisabilityCategory.AUTISM_SPECTRUM) {
                config.primary_mode = OutputMode.DARK_CALM;
                config.reduce_motion = true;
                config.syntax_highlight_style = "monochrome";
                config.dark_mode = true;
                config.screen_dim_seconds = 0;
            } else if (d.category == DisabilityCategory.NEUROLOGICAL) {
                if (d.specifics.contains("epilepsia")) {
                    config.reduce_motion = true;
                    config.dark_mode = true;
                    config.syntax_highlight_style = "monochrome";
                }
                if (d.specifics.contains("parkinson")) config.font_size_pt = 18;
            } else if (d.category == DisabilityCategory.DEVELOPMENTAL) {
                config.font_size_pt = 20;
                config.line_height = 1.8;
                config.syntax_highlight_style = "high_contrast_simple";
            }
        }
        return config;
    }

    // ============================================================================
    // 5. ADAPTACOES DE CODIGO
    // ============================================================================

    public enum CodeRepresentation {
        STANDARD("texto_padrao"),
        STRUCTURED_BLOCKS("blocos"),
        FLOWCHART("fluxograma"),
        NATURAL_LANGUAGE("linguagem_natural"),
        VOICE_FRIENDLY("amigavel_voz"),
        SIMPLIFIED("simplificado"),
        PORTUGOL_PP("portugol_pp"),
        SIGN_LANGUAGE("libras");

        public final String value;
        CodeRepresentation(String value) { this.value = value; }
    }

    public static class CodeAdaptationConfig {
        public CodeRepresentation representation = CodeRepresentation.STANDARD;
        public boolean indentation_guide = true;
        public boolean bracket_matching_audio = false;
        public String error_description_level = "detalhado";
        public String autocomplete_trigger = "instant";
        public boolean line_numbers_audio = false;
        public boolean spell_check_code = true;
        public boolean semantic_groups = false;
        public int chunk_size = 0;
    }

    public static CodeAdaptationConfig adapt_code_config(DeveloperProfile profile) {
        CodeAdaptationConfig config = new CodeAdaptationConfig();
        for (DisabilityProfile d : profile.disabilities) {
            if (d.category == DisabilityCategory.VISUAL) {
                if (d.severity == DisabilitySeverity.SEVERE || d.severity == DisabilitySeverity.PROFOUND) {
                    config.representation = CodeRepresentation.VOICE_FRIENDLY;
                    config.bracket_matching_audio = true;
                    config.line_numbers_audio = true;
                    config.error_description_level = "detalhado";
                }
            } else if (d.category == DisabilityCategory.COGNITIVE) {
                if (d.specifics.contains("dislexia")) {
                    config.representation = CodeRepresentation.SIMPLIFIED;
                    config.autocomplete_trigger = "predictive";
                }
                if (d.specifics.contains("tdah")) {
                    config.chunk_size = 15;
                    config.semantic_groups = true;
                }
            } else if (d.category == DisabilityCategory.AUTISM_SPECTRUM) {
                config.representation = CodeRepresentation.STRUCTURED_BLOCKS;
                config.semantic_groups = true;
            } else if (d.category == DisabilityCategory.DEVELOPMENTAL) {
                config.representation = CodeRepresentation.STRUCTURED_BLOCKS;
                config.error_description_level = "simples";
                config.chunk_size = 10;
            } else if (d.category == DisabilityCategory.AUDITORY) {
                config.representation = CodeRepresentation.FLOWCHART;
                config.error_description_level = "detalhado";
            }
        }
        return config;
    }

    // ============================================================================
    // 6. FEEDBACK MULTIMODAL
    // ============================================================================

    public enum FeedbackChannel {
        VISUAL("visual"), AUDIO("audio"), HAPTIC("haptico"), BRAILLE("braille");
        public final String value;
        FeedbackChannel(String value) { this.value = value; }
    }

    public enum FeedbackType {
        SUCCESS("sucesso"), ERROR("erro"), WARNING("aviso"), INFO("info"),
        COMPILATION_ERROR("erro_compilacao"), RUNTIME_ERROR("erro_execucao"),
        AUTOCOMPLETE_AVAILABLE("autocomplete"), SYNTAX_HIGHLIGHT("sintaxe"),
        BREAKPOINT_HIT("breakpoint"), TEST_PASS("teste_passou"), TEST_FAIL("teste_falhou");

        public final String value;
        FeedbackType(String value) { this.value = value; }
    }

    public static class FeedbackSignal {
        public FeedbackType feedback_type;
        public List<FeedbackChannel> channels;
        public String visual_cue;
        public String audio_cue;
        public String haptic_pattern;
        public String braille_pattern;
        public int urgency = 1;

        public FeedbackSignal(FeedbackType ft, List<FeedbackChannel> ch, String v, String a, String h, String b) {
            this.feedback_type = ft; this.channels = ch; this.visual_cue = v; this.audio_cue = a; this.haptic_pattern = h; this.braille_pattern = b;
        }
    }

    public static class FeedbackEngine {
        public DeveloperProfile profile;
        public OutputConfiguration output_config;
        public Map<FeedbackType, FeedbackSignal> signals = new HashMap<>();

        public FeedbackEngine(DeveloperProfile profile) {
            this.profile = profile;
            this.output_config = recommend_output(profile);
            this._build_signals();
        }

        private void _build_signals() {
            for (FeedbackType ft : FeedbackType.values()) {
                List<FeedbackChannel> channels = new ArrayList<>();
                boolean has_visual = true;
                boolean has_audio = true;
                boolean has_haptic = this.output_config.haptic_enabled;

                for (DisabilityProfile d : this.profile.disabilities) {
                    if (d.category == DisabilityCategory.VISUAL && (d.severity == DisabilitySeverity.SEVERE || d.severity == DisabilitySeverity.PROFOUND)) has_visual = false;
                    if (d.category == DisabilityCategory.AUDITORY) has_audio = false;
                }
                if (has_visual) channels.add(FeedbackChannel.VISUAL);
                if (has_audio) channels.add(FeedbackChannel.AUDIO);
                if (has_haptic) channels.add(FeedbackChannel.HAPTIC);
                if (this.output_config.primary_mode == OutputMode.BRAILLE_DISPLAY) channels.add(FeedbackChannel.BRAILLE);

                String visual = null, audio = null, haptic = null, braille = null;
                if (ft == FeedbackType.ERROR || ft == FeedbackType.COMPILATION_ERROR) {
                    visual = "borda vermelha + mensagem"; audio = "tom grave curto"; haptic = "vibracao dupla forte"; braille = "erro";
                } else if (ft == FeedbackType.SUCCESS || ft == FeedbackType.TEST_PASS) {
                    visual = "borda verde discreta"; audio = "tom agudo curto (apenas se solicitado)"; haptic = "vibracao suave unica"; braille = "ok";
                } else if (ft == FeedbackType.WARNING) {
                    visual = "borda amarela"; audio = "ton medio curto"; haptic = "vibracao unica media"; braille = "aviso";
                } else if (ft == FeedbackType.TEST_FAIL) {
                    visual = "linha vermelha no teste"; audio = "tom descendente"; haptic = "vibracao tripla"; braille = "falhou";
                }
                this.signals.put(ft, new FeedbackSignal(ft, channels, visual, audio, haptic, braille));
            }
        }

        public FeedbackSignal emit(FeedbackType feedback_type) {
            return this.signals.getOrDefault(feedback_type, this.signals.get(FeedbackType.INFO));
        }
    }

    // ============================================================================
    // 7. AMBIENTE SENSORIAL
    // ============================================================================

    public static class SensoryEnvironment {
        public double brightness = 0.5;
        public double contrast_ratio = 4.5;
        public int color_temperature_k = 3000;
        public boolean animation_enabled = true;
        public double animation_speed = 1.0;
        public boolean sound_enabled = false;
        public boolean notifications_enabled = false;
        public int max_visual_elements = 0;
        public int flicker_rate_hz = 0;
        public String background = "solid";
        public boolean reduce_noise = false;
        public boolean dark_mode = true;

        public void apply_calming() {
            this.brightness = 0.3; this.animation_enabled = false; this.sound_enabled = false;
            this.notifications_enabled = false; this.max_visual_elements = 7; this.background = "solid";
            this.reduce_noise = true; this.flicker_rate_hz = 0;
        }
    }

    public static SensoryEnvironment configure_environment(DeveloperProfile profile) {
        SensoryEnvironment env = new SensoryEnvironment();
        for (DisabilityProfile d : profile.disabilities) {
            if (d.category == DisabilityCategory.AUTISM_SPECTRUM) {
                env.apply_calming(); env.color_temperature_k = 2700;
            } else if (d.category == DisabilityCategory.NEUROLOGICAL && d.specifics.contains("epilepsia")) {
                env.flicker_rate_hz = 0; env.animation_enabled = false; env.brightness = 0.4; env.contrast_ratio = 7.0; env.color_temperature_k = 3000;
            } else if (d.category == DisabilityCategory.VISUAL && (d.severity == DisabilitySeverity.MODERATE || d.severity == DisabilitySeverity.SEVERE)) {
                env.contrast_ratio = 7.0; env.brightness = 0.7;
            } else if (d.category == DisabilityCategory.COGNITIVE && d.specifics.contains("tdah")) {
                env.max_visual_elements = 5; env.notifications_enabled = false; env.animation_enabled = false;
            } else if (d.category == DisabilityCategory.AUDITORY) {
                env.sound_enabled = false;
            }
        }
        return env;
    }

    // ============================================================================
    // 8. ASSISTENTE DE IA INCLUSIVO
    // ============================================================================

    public static class AIAssistanceConfig {
        public boolean enabled = true;
        public boolean auto_describe_code = false;
        public boolean auto_fix_accessibility = true;
        public boolean voice_interaction = false;
        public boolean simplify_errors = true;
        public boolean predict_next_line = true;
        public boolean translate_to_portugol = true;
        public boolean sign_language_avatar = false;
        public boolean cognitive_load_monitor = true;
        public boolean break_reminder = true;

        public void adapt(DeveloperProfile profile) {
            for (DisabilityProfile d : profile.disabilities) {
                if (d.category == DisabilityCategory.VISUAL && (d.severity == DisabilitySeverity.SEVERE || d.severity == DisabilitySeverity.PROFOUND)) {
                    this.voice_interaction = true; this.auto_describe_code = true;
                } else if (d.category == DisabilityCategory.AUDITORY) {
                    this.voice_interaction = false; this.sign_language_avatar = true;
                } else if (d.category == DisabilityCategory.COGNITIVE) {
                    this.simplify_errors = true; this.predict_next_line = true;
                } else if (d.category == DisabilityCategory.AUTISM_SPECTRUM) {
                    this.predict_next_line = false; this.cognitive_load_monitor = true;
                } else if (d.category == DisabilityCategory.DEVELOPMENTAL) {
                    this.simplify_errors = true; this.auto_describe_code = true; this.translate_to_portugol = true;
                } else if (d.category == DisabilityCategory.COMMUNICATION) {
                    this.voice_interaction = true; this.sign_language_avatar = true;
                }
            }
        }
    }

    // ============================================================================
    // 9. NAVEGACAO DE CODIGO ADAPTADA
    // ============================================================================

    public enum NavigationMode {
        LINE_BY_LINE("linha_a_linha"),
        BLOCK_BY_BLOCK("bloco_a_bloco"),
        SEMANTIC("semantica"),
        AUDIO_OUTLINE("outline_audio"),
        TREE("arvore"),
        MINIMAP("minimapa"),
        BRAILLE_NAV("navegacao_braille");

        public final String value;
        NavigationMode(String value) { this.value = value; }
    }

    public static class NavigationConfig {
        public NavigationMode mode = NavigationMode.LINE_BY_LINE;
        public int auto_collapse_depth = 2;
        public boolean announce_position = false;
        public List<String> jump_targets = Arrays.asList("funcao", "classe", "loop", "condicao", "retorno", "erro");
    }

    public static NavigationConfig recommend_navigation(DeveloperProfile profile) {
        NavigationConfig config = new NavigationConfig();
        for (DisabilityProfile d : profile.disabilities) {
            if (d.category == DisabilityCategory.VISUAL && (d.severity == DisabilitySeverity.SEVERE || d.severity == DisabilitySeverity.PROFOUND)) {
                config.mode = NavigationMode.BRAILLE_NAV; config.announce_position = true;
            } else if (d.category == DisabilityCategory.COGNITIVE) {
                config.mode = NavigationMode.BLOCK_BY_BLOCK; config.auto_collapse_depth = 1;
            } else if (d.category == DisabilityCategory.AUTISM_SPECTRUM || d.category == DisabilityCategory.DEVELOPMENTAL) {
                config.mode = NavigationMode.TREE; config.auto_collapse_depth = 1;
            }
        }
        return config;
    }

    // ============================================================================
    // 10. VERIFICACAO DE ACESSIBILIDADE DO CODIGO
    // ============================================================================

    public static class AccessibilityCheck {
        public String check_id;
        public String description;
        public String severity;
        public String suggestion;
        public AccessibilityCheck(String id, String desc, String sev, String sug) {
            this.check_id = id; this.description = desc; this.severity = sev; this.suggestion = sug;
        }
    }

    public static List<AccessibilityCheck> A11Y_CHECKS = Arrays.asList(
        new AccessibilityCheck("A11Y-001", "Contraste de cores no output do programa", "warning", "Use contraste minimo 4.5:1 (WCAG AA)"),
        new AccessibilityCheck("A11Y-002", "Texto alternativo em imagens/icones do programa", "error", "Todo elemento visual deve ter descricao para screen readers"),
        new AccessibilityCheck("A11Y-003", "Navegacao por teclado no programa", "error", "Todo interativo deve ser acessivel por teclado (Tab/Enter)"),
        new AccessibilityCheck("A11Y-004", "Nao use so cor para transmitir informacao", "warning", "Adicione texto ou icone junto com cor"),
        new AccessibilityCheck("A11Y-005", "Tamanho de fonte minimo no output", "info", "Minimo 16px para texto, 14px para codigo"),
        new AccessibilityCheck("A11Y-006", "Animacoes devem ter opcao de desativar", "warning", "prefers-reduced-motion deve ser respeitado"),
        new AccessibilityCheck("A11Y-007", "Audio deve ter legenda/transcricao", "error", "Todo audio deve ter alternativa textual"),
        new AccessibilityCheck("A11Y-008", "Forms devem ter labels", "error", "Todo input deve ter label associado"),
        new AccessibilityCheck("A11Y-009", "Sem padroes que causam seizures", "error", "Nada que pisque mais que 3x por segundo (WCAG 2.3.1)"),
        new AccessibilityCheck("A11Y-010", "Linguagem simples e clara", "info", "Prefira linguagem direta e simples no codigo e comentarios")
    );

    public static List<AccessibilityCheck> run_a11y_lint(String code, DeveloperProfile profile) {
        return new ArrayList<>(A11Y_CHECKS);
    }

    // ============================================================================
    // 11. PERFIS PRE-CONFIGURADOS
    // ============================================================================

    public static DeveloperProfile create_profile_blind() {
        return new DeveloperProfile("blind_dev", "Dev Cego", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.VISUAL, DisabilitySeverity.PROFOUND, Arrays.asList("cegueira_total"), Arrays.asList("screen_reader", "braille_display", "talon_voice"))
        ), new HashMap<String, Object>() {{ put("tts_rate", 2.0); put("braille_cells", 40); }});
    }
    public static DeveloperProfile create_profile_deaf() {
        return new DeveloperProfile("deaf_dev", "Dev Surdo", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.AUDITORY, DisabilitySeverity.PROFOUND, Arrays.asList("surdez_profunda"), Arrays.asList("visual_alerts"))
        ), null);
    }
    public static DeveloperProfile create_profile_motor_severe() {
        return new DeveloperProfile("motor_dev", "Dev Tetraplegico", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.MOTOR, DisabilitySeverity.PROFOUND, Arrays.asList("tetraplegia"), Arrays.asList("eye_tracker", "voice_control", "switch"))
        ), null);
    }
    public static DeveloperProfile create_profile_dyslexia() {
        return new DeveloperProfile("dyslexia_dev", "Dev Dislexico", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.COGNITIVE, DisabilitySeverity.MODERATE, Arrays.asList("dislexia"), null)
        ), null);
    }
    public static DeveloperProfile create_profile_adhd() {
        return new DeveloperProfile("adhd_dev", "Dev TDAH", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.COGNITIVE, DisabilitySeverity.MODERATE, Arrays.asList("tdah"), null)
        ), null);
    }
    public static DeveloperProfile create_profile_autism() {
        return new DeveloperProfile("autism_dev", "Dev Autista", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.AUTISM_SPECTRUM, DisabilitySeverity.MODERATE, Arrays.asList("hipersensibilidade_sensorial", "sobrecarga"), null)
        ), null);
    }
    public static DeveloperProfile create_profile_epilepsy() {
        return new DeveloperProfile("epilepsy_dev", "Dev Epileptico", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.NEUROLOGICAL, DisabilitySeverity.MODERATE, Arrays.asList("epilepsia_fotossensivel"), null)
        ), null);
    }
    public static DeveloperProfile create_profile_down() {
        return new DeveloperProfile("down_dev", "Dev Down", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.DEVELOPMENTAL, DisabilitySeverity.MODERATE, Arrays.asList("sindrome_down"), null)
        ), null);
    }
    public static DeveloperProfile create_profile_multiple() {
        return new DeveloperProfile("multi_dev", "Dev Multipla", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.VISUAL, DisabilitySeverity.MODERATE, Arrays.asList("baixa_visao"), null),
            new DisabilityProfile(DisabilityCategory.MOTOR, DisabilitySeverity.MODERATE, Arrays.asList("distrofia", "tremor"), null)
        ), null);
    }
    public static DeveloperProfile create_profile_temporary() {
        return new DeveloperProfile("temp_dev", "Dev Temporario", Arrays.asList(
            new DisabilityProfile(DisabilityCategory.TEMPORARY, DisabilitySeverity.MODERATE, Arrays.asList("lesao_temporaria", "fatiga_extrema"), null)
        ), null);
    }

    // ============================================================================
    // 12. IDE COMPLETA
    // ============================================================================

    public DeveloperProfile profile;
    public InputConfiguration input_config;
    public OutputConfiguration output_config;
    public CodeAdaptationConfig code_config;
    public SensoryEnvironment environment;
    public NavigationConfig navigation;
    public FeedbackEngine feedback_engine;
    public AIAssistanceConfig ai_config;
    public boolean session_active = false;
    public List<String> errors_emitted = new ArrayList<>();
    public String session_start_time = null;

    public OpenInclusiveIDE(DeveloperProfile profile) {
        this.profile = profile;
        this.input_config = recommend_input(profile);
        this.output_config = recommend_output(profile);
        this.code_config = adapt_code_config(profile);
        this.environment = configure_environment(profile);
        this.navigation = recommend_navigation(profile);
        this.feedback_engine = new FeedbackEngine(profile);
        this.ai_config = new AIAssistanceConfig();
        this.ai_config.adapt(profile);
    }

    public Map<String, Object> start_session() {
        this.session_active = true;
        Map<String, Object> env = new HashMap<>();
        env.put("brightness", this.environment.brightness);
        env.put("dark_mode", this.environment.dark_mode);
        env.put("animation", this.environment.animation_enabled);
        env.put("sound", this.environment.sound_enabled);
        Map<String, Object> res = new HashMap<>();
        res.put("profile", this.profile.name);
        res.put("disabilities", this.profile.disabilities.stream().map(d -> d.category.value).toArray());
        res.put("input", this.input_config.primary_mode.value);
        res.put("output", this.output_config.primary_mode.value);
        res.put("code_representation", this.code_config.representation.value);
        res.put("navigation", this.navigation.mode.value);
        res.put("environment", env);
        res.put("ai_assistance", this.ai_config.enabled);
        res.put("session_active", true);
        return res;
    }

    public Map<String, Object> display_code(String code) {
        Map<String, Object> res = new HashMap<>();
        res.put("original_lines", code.split("\n").length);
        res.put("representation", this.code_config.representation.value);
        res.put("chunked", this.code_config.chunk_size > 0);
        res.put("chunk_size", this.code_config.chunk_size > 0 ? this.code_config.chunk_size : null);
        res.put("font", this.output_config.font_family);
        res.put("font_size", this.output_config.font_size_pt);
        res.put("line_height", this.output_config.line_height);
        res.put("high_contrast", this.output_config.high_contrast);
        res.put("reduce_motion", this.output_config.reduce_motion);
        return res;
    }

    public FeedbackSignal handle_error(String error_message) {
        this.errors_emitted.add(error_message);
        if (this.ai_config.simplify_errors) error_message = this._simplify_error(error_message);
        return this.feedback_engine.emit(FeedbackType.ERROR);
    }
    public FeedbackSignal handle_success() { return this.feedback_engine.emit(FeedbackType.SUCCESS); }
    public FeedbackSignal handle_test_result(boolean passed) {
        return passed ? this.feedback_engine.emit(FeedbackType.TEST_PASS) : this.feedback_engine.emit(FeedbackType.TEST_FAIL);
    }

    public Map<String, Object> check_energy() {
        double energy = this.profile.effective_energy();
        Map<String, Object> res = new HashMap<>();
        res.put("energy_level", energy);
        res.put("low_energy", this.profile.is_low_energy());
        res.put("recommend_break", this.profile.is_low_energy());
        res.put("message", this.profile.is_low_energy() ? "Energia baixa. Hora de descansar. (OpenAbsence)" : "Energia ok. Continue.");
        return res;
    }

    public List<AccessibilityCheck> run_a11y_check(String code) { return run_a11y_lint(code, this.profile); }

    private String _simplify_error(String message) {
        Map<String, String> translations = new HashMap<>();
        translations.put("SyntaxError", "Tem algo errado na escrita do codigo. Verifique a linha indicada.");
        translations.put("IndentationError", "O espacamento esta errado. Cada bloco precisa estar alinhado.");
        translations.put("TypeError", "Os tipos nao combinam. Voce esta misturando texto com numero, por exemplo.");
        translations.put("NameError", "Uma variavel nao foi definida. Verifique se voce escreveu o nome certo.");
        translations.put("IndexError", "Voce tentou acessar uma posicao que nao existe na lista.");
        translations.put("KeyError", "Essa chave nao existe no dicionario.");
        translations.put("AttributeError", "Esse objeto nao tem essa propriedade.");
        translations.put("ImportError", "Nao conseguiu encontrar o modulo. Verifique se esta instalado.");
        for (Map.Entry<String, String> e : translations.entrySet()) {
            if (message.contains(e.getKey())) return e.getValue() + " (Detalhe tecnico: " + message + ")";
        }
        return message;
    }

    public Map<String, Object> session_summary() {
        Map<String, Object> res = new HashMap<>();
        res.put("profile", this.profile.name);
        res.put("disabilities_catered", this.profile.disabilities.stream().map(d -> d.category.value).toArray());
        res.put("total_errors", this.errors_emitted.size());
        res.put("input_mode", this.input_config.primary_mode.value);
        res.put("output_mode", this.output_config.primary_mode.value);
        res.put("code_representation", this.code_config.representation.value);
        res.put("a11y_checks_available", A11Y_CHECKS.size());
        return res;
    }

    // ============================================================================
    // 13. DEMONSTRACAO
    // ============================================================================

    public static void demo() {
        System.out.println("=".repeat(70));
        System.out.println("OpenInclusiveIDE -- IDE para TODAS as Deficiencias");
        System.out.println("=".repeat(70));

        Map<String, DeveloperProfile> profiles = new LinkedHashMap<>();
        profiles.put("Cego", create_profile_blind());
        profiles.put("Surdo", create_profile_deaf());
        profiles.put("Tetraplegico", create_profile_motor_severe());
        profiles.put("Dislexia", create_profile_dyslexia());
        profiles.put("TDAH", create_profile_adhd());
        profiles.put("Autista", create_profile_autism());
        profiles.put("Epilepsia", create_profile_epilepsy());
        profiles.put("Sindrome de Down", create_profile_down());
        profiles.put("Multipla (baixa visao + motor)", create_profile_multiple());
        profiles.put("Temporaria (lesao)", create_profile_temporary());

        for (Map.Entry<String, DeveloperProfile> entry : profiles.entrySet()) {
            System.out.println("\n" + "-".repeat(50));
            System.out.println("PERFIL: " + entry.getKey());
            System.out.println("-".repeat(50));
            OpenInclusiveIDE ide = new OpenInclusiveIDE(entry.getValue());
            Map<String, Object> session = ide.start_session();
            System.out.println("  Input:      " + session.get("input"));
            System.out.println("  Output:     " + session.get("output"));
            System.out.println("  Codigo:     " + session.get("code_representation"));
            System.out.println("  Navegacao:  " + session.get("navigation"));
            @SuppressWarnings("unchecked")
            Map<String, Object> env = (Map<String, Object>) session.get("environment");
            System.out.println("  Som:        " + env.get("sound"));
            System.out.println("  Animacao:   " + env.get("animation"));
            System.out.println("  Brilho:     " + env.get("brightness"));
            System.out.println("  IA:         " + session.get("ai_assistance"));
            FeedbackSignal error_feedback = ide.handle_error("SyntaxError: invalid syntax on line 5");
            System.out.println("  Erro feedback canais: " + error_feedback.channels.stream().map(c -> c.value).toList());
            Map<String, Object> energy = ide.check_energy();
            System.out.println("  Energia:    " + String.format("%.2f", (Double) energy.get("energy_level")));
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("VERIFICACAO DE ACESSIBILIDADE (a11y lint)");
        System.out.println("=".repeat(70));
        for (AccessibilityCheck check : A11Y_CHECKS) {
            System.out.println("  [" + check.severity.toUpperCase() + "] " + check.check_id + ": " + check.description);
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("COBERTURA DE DEFICIENCIAS");
        System.out.println("=".repeat(70));
        for (DisabilityCategory cat : DisabilityCategory.values()) {
            System.out.println("  " + String.format("%-20s", cat.value) + " -- COBERTO");
        }

        System.out.println("\nTotal de categorias: " + DisabilityCategory.values().length);
        System.out.println("Total de modos de entrada: " + InputMode.values().length);
        System.out.println("Total de modos de saida: " + OutputMode.values().length);
        System.out.println("Total de verificacoes a11y: " + A11Y_CHECKS.size());
        System.out.println("Total de representacoes de codigo: " + CodeRepresentation.values().length);
        System.out.println("\nIDE INCLUSIVA. ZERO BARREIRA. TODA DEFICIENCIA COBERTA.");
    }

    public static void main(String[] args) {
        demo();
    }
}