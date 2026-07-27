// OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel
// Gerado a partir de open_inclusive_hardware.py (fonte de verdade)
// Comentarios em Portugues conforme padrao OpenRepublic

import java.util.*;

public class OpenInclusiveHardware {

    // ============================================================================
    // 1. CATEGORIAS DE HARDWARE
    // ============================================================================

    public enum HardwareCategory {
        MASS("massa"),
        ASSISTIVE_VISUAL("assistivo_visual"),
        ASSISTIVE_MOTOR("assistivo_motor"),
        ASSISTIVE_AUDITORY("assistivo_auditivo"),
        ASSISTIVE_COGNITIVE("assistivo_cognitivo"),
        TERMINAL_PUBLIC("terminal_publico"),
        WEARABLE("vestivel"),
        BRAIN("cerebral");

        public final String value;
        HardwareCategory(String value) { this.value = value; }
    }

    public enum HardwareCost {
        FREE("gratis"),
        VERY_LOW("muito_baixo"),
        LOW("baixo"),
        MEDIUM("medio"),
        HIGH("alto"),
        VERY_HIGH("muito_alto"),
        SUBSIDIZED("subsidiado");

        public final String value;
        HardwareCost(String value) { this.value = value; }
    }

    public enum HardwareAvailability {
        UBIQUITOUS("ubiquo"),
        COMMON("comum"),
        SPECIALIZED("especializado"),
        MEDICAL("medico"),
        RARE("raro"),
        EXPERIMENTAL("experimental");

        public final String value;
        HardwareAvailability(String value) { this.value = value; }
    }

    public enum ConnectionType {
        BLUETOOTH("bluetooth"),
        USB("usb"),
        WIFI("wifi"),
        NFC("nfc"),
        CLOUD("nuvem"),
        AUDIO_JACK("jack_audio"),
        PROPRIETARY("proprietario"),
        WIRELESS("sem_fio_generico"),
        HDMI("hdmi");

        public final String value;
        ConnectionType(String value) { this.value = value; }
    }

    // ============================================================================
    // 2. PERFIL DE HARDWARE
    // ============================================================================

    public static class HardwareDevice {
        public final String device_id;
        public final String name;
        public final HardwareCategory category;
        public final HardwareCost cost;
        public final HardwareAvailability availability;
        public final List<ConnectionType> connections;
        public final List<String> platforms;
        public final List<String> disabilities_served;
        public final List<String> input_capabilities;
        public final List<String> output_capabilities;
        public final double battery_hours;
        public final boolean offline_capable;
        public final List<String> languages_supported;
        public final String description;

        public HardwareDevice(String device_id, String name, HardwareCategory category,
                              HardwareCost cost, HardwareAvailability availability,
                              List<ConnectionType> connections, List<String> platforms,
                              List<String> disabilities_served, List<String> input_capabilities,
                              List<String> output_capabilities, double battery_hours,
                              boolean offline_capable, List<String> languages_supported,
                              String description) {
            this.device_id = device_id;
            this.name = name;
            this.category = category;
            this.cost = cost;
            this.availability = availability;
            this.connections = connections != null ? connections : new ArrayList<>();
            this.platforms = platforms != null ? platforms : new ArrayList<>();
            this.disabilities_served = disabilities_served != null ? disabilities_served : new ArrayList<>();
            this.input_capabilities = input_capabilities != null ? input_capabilities : new ArrayList<>();
            this.output_capabilities = output_capabilities != null ? output_capabilities : new ArrayList<>();
            this.battery_hours = battery_hours;
            this.offline_capable = offline_capable;
            this.languages_supported = languages_supported != null ? languages_supported : Arrays.asList("pt-BR");
            this.description = description != null ? description : "";
        }
    }

    // ============================================================================
    // 3. CATALOGO DE HARDWARE (44 DISPOSITIVOS)
    // ============================================================================

    public static final List<HardwareDevice> HARDWARE_CATALOG = new ArrayList<>();

    static {
        // === SMARTPHONE (massa) ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-001", "Smartphone Android (qualquer)",
            HardwareCategory.MASS, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.NFC, ConnectionType.AUDIO_JACK),
            Arrays.asList("Android"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "multipla", "temporaria"),
            Arrays.asList("touch", "voice", "camera", "microphone", "bluetooth_keyboard", "nfc", "accelerometer", "gyroscope"),
            Arrays.asList("screen", "speaker", "vibration", "flash_led", "screen_reader"),
            12.0, true, Arrays.asList("pt-BR"),
            "O dispositivo mais inclusivo do planeta. TalkBack, Voice Access, Switch Access nativos."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-002", "iPhone (qualquer)",
            HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.NFC),
            Arrays.asList("iOS"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "multipla", "temporaria"),
            Arrays.asList("touch", "voice", "face_id", "camera", "microphone", "bluetooth_keyboard", "lidar"),
            Arrays.asList("screen", "speaker", "vibration", "taptic_engine", "voiceover", "flash_led"),
            15.0, true, Arrays.asList("pt-BR"),
            "VoiceOver, Switch Control, Voice Control, Sound Detection nativos. Lidar para deteccao de obstaculos."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-003", "Smartphone basico (teclado fisico)",
            HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH),
            Arrays.asList("KaiOS", "Feature Phone"),
            Arrays.asList("visual", "motora", "temporaria"),
            Arrays.asList("keypad", "voice", "microphone"),
            Arrays.asList("screen_small", "speaker", "vibration", "tts_basic"),
            72.0, true, Arrays.asList("pt-BR"),
            "Telefone botoeiro com TTS. Para quem nao tem smartphone ou prefere teclado fisico."));

        // === TABLET ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-004", "Tablet Android",
            HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI),
            Arrays.asList("Android"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento"),
            Arrays.asList("touch", "voice", "camera", "microphone", "stylus", "bluetooth_keyboard"),
            Arrays.asList("screen_large", "speaker", "vibration"),
            10.0, true, Arrays.asList("pt-BR"),
            "Tela maior = mais area para botoes grandes, blocos visuais, zoom."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-005", "iPad",
            HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI),
            Arrays.asList("iPadOS"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento"),
            Arrays.asList("touch", "voice", "face_id", "camera", "microphone", "stylus_pencil", "lidar"),
            Arrays.asList("screen_large", "speaker", "taptic_engine", "voiceover"),
            10.0, true, Arrays.asList("pt-BR"),
            "Apple Pencil para deteccao de tremores. AssistiveTouch. Full Keyboard Control."));

        // === SMARTWATCH / WEARABLE ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-006", "Smartwatch Android (WearOS)",
            HardwareCategory.WEARABLE, HardwareCost.MEDIUM, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.WIFI),
            Arrays.asList("WearOS"),
            Arrays.asList("auditiva", "motora", "cognitiva", "temporaria"),
            Arrays.asList("touch_small", "voice", "microphone", "accelerometer", "heart_rate", "gestures", "crown"),
            Arrays.asList("screen_tiny", "vibration", "speaker_tiny", "haptic"),
            24.0, true, Arrays.asList("pt-BR"),
            "Vibracao no pulso para alertas (surdez). Monitor de batimento (epilepsia/ansiedade). Coroa para navegacao (motor)."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-007", "Apple Watch",
            HardwareCategory.WEARABLE, HardwareCost.MEDIUM, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.WIFI),
            Arrays.asList("watchOS"),
            Arrays.asList("auditiva", "motora", "cognitiva", "temporaria", "neurologica"),
            Arrays.asList("touch_small", "voice", "microphone", "crown_digital", "accelerometer", "heart_rate", "ecg", "fall_detection", "gestures", "sip_pinch"),
            Arrays.asList("screen_tiny", "taptic_engine", "speaker_tiny", "haptic"),
            18.0, true, Arrays.asList("pt-BR"),
            "Fall Detection (queda). ECG (coracao). Taptic Engine para surdos. AssistiveTouch (pinca/sorvo para tetraplegia). Noise app (autismo)."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-008", "Smartwatch basico / Pulseira fitness",
            HardwareCategory.WEARABLE, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.BLUETOOTH),
            Arrays.asList("Proprietary"),
            Arrays.asList("auditiva", "temporaria"),
            Arrays.asList("touch_tiny", "accelerometer", "heart_rate"),
            Arrays.asList("screen_tiny", "vibration"),
            168.0, true, Arrays.asList("pt-BR"),
            "R$80-200. Vibracao para notificacoes (surdez). Monitor basico de sono/atividade."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-009", "Anel Smart (Smart Ring)",
            HardwareCategory.WEARABLE, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.BLUETOOTH),
            Arrays.asList("Proprietary"),
            Arrays.asList("auditiva", "neurologica"),
            Arrays.asList("accelerometer", "heart_rate", "temperature", "spO2"),
            Arrays.asList("vibration_tiny", "led"),
            168.0, true, Arrays.asList("pt-BR"),
            "Discreto. Monitor de sono, temperatura, SpO2. Para autismo: biofeedback discreto."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-010", "Oculos Inteligentes (Smart Glasses)",
            HardwareCategory.WEARABLE, HardwareCost.HIGH, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.WIFI),
            Arrays.asList("Android", "Proprietary"),
            Arrays.asList("visual", "auditiva", "motora", "neurologica"),
            Arrays.asList("voice", "camera", "microphone", "bone_conduction_audio", "head_tracking", "eye_tracking_basic"),
            Arrays.asList("hud_overlay", "bone_conduction_speaker", "vibration"),
            6.0, true, Arrays.asList("pt-BR"),
            "Legendas em tempo real no campo de visao (surdez). Navegacao por setas (cegueira). Heads-up display."));

        // === COMPUTADOR / NOTEBOOK ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-011", "Notebook / Laptop",
            HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.AUDIO_JACK),
            Arrays.asList("Linux", "Windows", "macOS"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva", "espectro_autista", "neurologica", "multipla", "temporaria"),
            Arrays.asList("keyboard", "trackpad", "microphone", "camera", "bluetooth_devices"),
            Arrays.asList("screen", "speaker", "vibration_rare"),
            8.0, true, Arrays.asList("pt-BR"),
            "Plataforma de desenvolvimento completa. Screen readers, IDEs, eye-tracking via USB."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-012", "Desktop / PC",
            HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.AUDIO_JACK),
            Arrays.asList("Linux", "Windows"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva", "espectro_autista", "neurologica", "multipla"),
            Arrays.asList("keyboard", "mouse", "microphone", "camera", "usb_devices", "pcie_cards"),
            Arrays.asList("screen_large", "speaker", "multi_monitor"),
            0.0, true, Arrays.asList("pt-BR"),
            "Maximo de conectividade. Multi-tela, GPUs para IA, todo tipo de periferico."));

        // === LEITOR DE TELA / DISPLAY BRAILLE ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-013", "Display Braille (linha braille)",
            HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.HIGH, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB),
            Arrays.asList("Android", "iOS", "Linux", "Windows", "macOS"),
            Arrays.asList("visual"),
            Arrays.asList("braille_keys", "routing_buttons", "navigation"),
            Arrays.asList("braille_cells_40", "braille_cells_80"),
            20.0, true, Arrays.asList("pt-BR"),
            "40-80 celulas braille. Celulas piezoeletricas que sobem e descem. Cego le codigo tateando."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-013b", "Display Braille portatil (14-20 celulas)",
            HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB),
            Arrays.asList("Android", "iOS"),
            Arrays.asList("visual"),
            Arrays.asList("braille_keys"),
            Arrays.asList("braille_cells_14"),
            20.0, true, Arrays.asList("pt-BR"),
            "Versao portatil menor. Cabe no bolso. Conecta no smartphone."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-014", "Leitor de tela software (NVDA, Orca, VoiceOver, TalkBack)",
            HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.FREE, HardwareAvailability.UBIQUITOUS,
            new ArrayList<>(),
            Arrays.asList("Android", "iOS", "Linux", "Windows", "macOS"),
            Arrays.asList("visual"),
            new ArrayList<>(),
            Arrays.asList("tts", "braille_output", "audio_cues"),
            0.0, true, Arrays.asList("pt-BR"),
            "NVDA (gratis, Windows). Orca (Linux). VoiceOver (Apple). TalkBack (Android). Converte tela em voz/braille."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-015", "Lupa eletronica / CCTV",
            HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.HDMI),
            Arrays.asList("Standalone"),
            Arrays.asList("visual"),
            Arrays.asList("camera_zoom"),
            Arrays.asList("screen_zoomed"),
            4.0, true, Arrays.asList("pt-BR"),
            "Camera que amplia texto/papel para tela. Para baixa visao."));

        // === EYE TRACKER / SWITCH / MOTOR ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-016", "Eye Tracker (Tobii, EyeX)",
            HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.HIGH, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.USB, ConnectionType.WIFI),
            Arrays.asList("Windows", "Linux"),
            Arrays.asList("motora", "multipla"),
            Arrays.asList("eye_gaze", "dwell_selection", "blink"),
            new ArrayList<>(),
            0.0, true, Arrays.asList("pt-BR"),
            "Camera infravermelha rastreia olhos. Tetraplegia, ELA, paralisia cerebral. Custo: R$2.000-8.000."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-017", "Eye Tracker portatil (smartphone)",
            HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
            new ArrayList<>(),
            Arrays.asList("Android", "iOS"),
            Arrays.asList("motora", "multipla"),
            Arrays.asList("eye_gaze_front_camera"),
            new ArrayList<>(),
            6.0, true, Arrays.asList("pt-BR"),
            "Usa camera frontal do smartphone para rastrear olhos. Precisao menor mas gratuito com app."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-018", "Switch / Botao adaptativo",
            HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.AUDIO_JACK, ConnectionType.USB),
            Arrays.asList("Android", "iOS", "Windows", "Linux", "macOS"),
            Arrays.asList("motora", "multipla", "desenvolvimento"),
            Arrays.asList("single_switch", "dual_switch"),
            new ArrayList<>(),
            0.0, true, Arrays.asList("pt-BR"),
            "Um ou dois botoes grandes. Scan automatico passa opcoes, usuario aciona para selecionar. DIY possivel por R$20."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-019", "Teclado adaptativo grande",
            HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB),
            Arrays.asList("Android", "iOS", "Windows", "Linux", "macOS"),
            Arrays.asList("motora", "cognitiva", "desenvolvimento"),
            Arrays.asList("large_keys", "color_coded"),
            new ArrayList<>(),
            0.0, true, Arrays.asList("pt-BR"),
            "Teclas 3x maiores, coloridas, com guard de mao. Para tremores, baixa destreza, Down."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-020", "Teclado de cabeca / boca",
            HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.USB, ConnectionType.BLUETOOTH),
            Arrays.asList("Windows", "Linux", "Android"),
            Arrays.asList("motora"),
            Arrays.asList("head_stick", "mouth_stick", "sip_puff"),
            new ArrayList<>(),
            0.0, true, Arrays.asList("pt-BR"),
            "Ponteiro de cabeca ou bocal para digitar em teclado na tela. Sip-and-puff = sopro/succao."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-021", "Trackball adaptativo",
            HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB),
            Arrays.asList("Windows", "Linux", "macOS", "Android"),
            Arrays.asList("motora"),
            Arrays.asList("trackball", "large_ball"),
            new ArrayList<>(),
            0.0, true, Arrays.asList("pt-BR"),
            "Bola grande movida com palma/queixo/dorso do pe. Estavel para tremores (Parkinson)."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-022", "Pedal de pe (Foot Pedal)",
            HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.USB, ConnectionType.BLUETOOTH),
            Arrays.asList("Windows", "Linux", "macOS"),
            Arrays.asList("motora", "temporaria"),
            Arrays.asList("foot_press_left", "foot_press_right", "foot_press_center"),
            new ArrayList<>(),
            0.0, true, Arrays.asList("pt-BR"),
            "Para quem tem uso dos pes mas nao das maos. 3 pedais = 3 botoes. R$50-150."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-023", "EMG / MIODOELETRICO (braco bio-feedback)",
            HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.MEDIUM, HardwareAvailability.EXPERIMENTAL,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB),
            Arrays.asList("Windows", "Linux", "Android"),
            Arrays.asList("motora", "multipla"),
            Arrays.asList("emg_signal", "muscle_activation"),
            new ArrayList<>(),
            8.0, true, Arrays.asList("pt-BR"),
            "Sensores no musculo. Detecta contracao muscular residual. Para amputados, paralisia parcial."));

        // === BCI / CEREBRAL ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-024", "BCI Invasivo (Neuralink/Synchron)",
            HardwareCategory.BRAIN, HardwareCost.VERY_HIGH, HardwareAvailability.EXPERIMENTAL,
            Arrays.asList(ConnectionType.WIFI, ConnectionType.BLUETOOTH),
            Arrays.asList("Windows", "Linux"),
            Arrays.asList("motora", "multipla"),
            Arrays.asList("neural_spikes", "motor_intention"),
            new ArrayList<>(),
            0.0, true, Arrays.asList("pt-BR"),
            "Eletrodos no cerebro. Tetraplegia profunda. Ainda em ensaios clinicos."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-025", "BCI Nao-Invasivo (EEG headset)",
            HardwareCategory.BRAIN, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB),
            Arrays.asList("Windows", "Linux", "Android"),
            Arrays.asList("motora", "multipla"),
            Arrays.asList("eeg_waves", "concentration_level", "blink_detect"),
            Arrays.asList("neurofeedback_display"),
            6.0, true, Arrays.asList("pt-BR"),
            "Capacete com eletrodos. Le ondas cerebrais. Precisao baixa mas nao invasivo. R$500-3000."));

        // === AUDITIVO ===
        HARDWARE_CATALOG.add(new HardwareDevice("HC-026", "Aparelho Auditivo (digital)",
            HardwareCategory.ASSISTIVE_AUDITORY, HardwareCost.MEDIUM, HardwareAvailability.MEDICAL,
            Arrays.asList(ConnectionType.BLUETOOTH),
            Arrays.asList("Standalone"),
            Arrays.asList("auditiva"),
            Arrays.asList("bluetooth_audio_in"),
            Arrays.asList("audio_amplified", "audio_filtered"),
            96.0, true, Arrays.asList("pt-BR"),
            "Amplifica e filtra som. Bluetooth direto do smartphone. Programa SUS cobre."));

        HARDWARE_CATALOG.add(new HardwareDevice("HC-027", "Implante Coclear",
            HardwareCategory.ASSISTIVE_AUDITORY, HardwareCost.VERY_HIGH, HardwareAvailability.MEDICAL,
            Arrays.asList(ConnectionType.BLUETOOTH),
            Arrays.asList("Standalone"),
            Arrays.asList("auditiva"),
            Arrays.asList("bluetooth_audio_in"),
            Arrays.asList("electrical_stimulation"),
            24.0, true, Arrays.asList("pt-BR"),
            "Cirurgico. Eletrodos na coclea. Para surdez profunda. SUS cobre em alguns estados."));

        HARDWARE_CATALOG.add(new HardwareDevice("HC-028", "Loop Magnetico / Sistema FM",
            HardwareCategory.ASSISTIVE_AUDITORY, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH),
            Arrays.asList("Standalone"),
            Arrays.asList("auditiva"),
            Arrays.asList("audio_in"),
            Arrays.asList("magnetic_loop"),
            0.0, true, Arrays.asList("pt-BR"),
            "Cabo de loop magnetico no pescoco. Transmite audio direto pro aparelho auditivo. Elimina ruido ambiente."));

        // === COGNITIVO / SENSORIAL ===
        HARDWARE_CATALOG.add(new HardwareDevice("HC-029", "Fone ANC (Active Noise Cancelling)",
            HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.AUDIO_JACK),
            Arrays.asList("Standalone"),
            Arrays.asList("espectro_autista", "auditiva", "cognitiva"),
            Arrays.asList("anc_microphone"),
            Arrays.asList("audio_anc", "audio_filtered"),
            30.0, true, Arrays.asList("pt-BR"),
            "Cancela ruido ambiente. ESCUDO SENSORIAL para autista/TDAH em ambiente ruidoso. R$100-500."));

        HARDWARE_CATALOG.add(new HardwareDevice("HC-030", "Fone com microfone direcional",
            HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.LOW, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.AUDIO_JACK),
            Arrays.asList("Standalone"),
            Arrays.asList("auditiva", "espectro_autista"),
            Arrays.asList("directional_microphone"),
            Arrays.asList("audio_directed"),
            20.0, true, Arrays.asList("pt-BR"),
            "Captura som da frente, cancela resto. Para APD (Processamento Auditivo) e autismo."));

        HARDWARE_CATALOG.add(new HardwareDevice("HC-031", "Luz Inteligente (Smart Bulb)",
            HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.WIFI, ConnectionType.BLUETOOTH),
            Arrays.asList("Android", "iOS"),
            Arrays.asList("visual", "auditiva", "espectro_autista", "neurologica"),
            new ArrayList<>(),
            Arrays.asList("color_light", "brightness_control", "temperature_color", "no_flicker"),
            0.0, true, Arrays.asList("pt-BR"),
            "Notificacao visual por cor (surdez). Luz quente para acalmar (autismo/epilepsia). Sem flicker."));

        HARDWARE_CATALOG.add(new HardwareDevice("HC-032", "Weighted Blanket (Manta Ponderada)",
            HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
            new ArrayList<>(),
            Arrays.asList("Physical"),
            Arrays.asList("espectro_autista", "cognitiva", "neurologica"),
            new ArrayList<>(),
            Arrays.asList("deep_pressure_stimulation"),
            0.0, true, Arrays.asList("pt-BR"),
            "Pressao profunda calmante. Reduz ansiedade (autismo/TDAH). Melhora sono. R$100-300."));

        HARDWARE_CATALOG.add(new HardwareDevice("HC-033", "Bracelete Anti-Ansiedade / Vibratorio",
            HardwareCategory.WEARABLE, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.BLUETOOTH),
            Arrays.asList("Android", "iOS"),
            Arrays.asList("espectro_autista", "cognitiva", "neurologica"),
            Arrays.asList("heart_rate", "skin_conductance"),
            Arrays.asList("vibration_patterns", "temperature_cooling"),
            72.0, true, Arrays.asList("pt-BR"),
            "Vibracao para acalmar (biofeedback). Detecta crise de ansiedade por batimento. R$80-200."));

        // === TERMINAL PUBLICO ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-034", "TV Smart (qualquer)",
            HardwareCategory.TERMINAL_PUBLIC, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.WIFI, ConnectionType.HDMI, ConnectionType.BLUETOOTH),
            Arrays.asList("Android TV", "Tizen", "webOS"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "temporaria"),
            Arrays.asList("remote", "voice", "bluetooth_keyboard", "camera_optional"),
            Arrays.asList("screen_huge", "speaker", "hdmi_out"),
            0.0, true, Arrays.asList("pt-BR"),
            "Todo estabelecimento tem uma TV. OpenTerminal transforma TV ociosa em terminal da Republica."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-035", "Kiosk / Terminal Publico",
            HardwareCategory.TERMINAL_PUBLIC, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.WIFI, ConnectionType.USB),
            Arrays.asList("Linux", "Windows"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva", "multipla"),
            Arrays.asList("touch", "keypad", "nfc", "camera"),
            Arrays.asList("screen_large", "speaker"),
            0.0, true, Arrays.asList("pt-BR"),
            "Terminal em praca, hospital, escola. wheelchair-height. Audio jack para fone."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-036", "Terminal Burro (Raspberry Pi + tela)",
            HardwareCategory.TERMINAL_PUBLIC, HardwareCost.VERY_LOW, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.WIFI, ConnectionType.USB, ConnectionType.AUDIO_JACK, ConnectionType.HDMI),
            Arrays.asList("Linux"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva"),
            Arrays.asList("keyboard", "usb_switch", "usb_eye_tracker", "bluetooth"),
            Arrays.asList("screen", "speaker", "audio_jack"),
            0.0, true, Arrays.asList("pt-BR"),
            "Raspberry Pi R$150 + tela R$100 = terminal completo. OpenKit da Republica."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-037", "Computador Comunitario (biblioteca, escola)",
            HardwareCategory.TERMINAL_PUBLIC, HardwareCost.FREE, HardwareAvailability.COMMON,
            Arrays.asList(ConnectionType.WIFI, ConnectionType.USB, ConnectionType.AUDIO_JACK),
            Arrays.asList("Linux", "Windows"),
            Arrays.asList("visual", "auditiva", "motora", "cognitiva", "multipla", "temporaria"),
            Arrays.asList("keyboard", "mouse", "microphone", "usb_devices"),
            Arrays.asList("screen", "speaker", "audio_jack"),
            0.0, true, Arrays.asList("pt-BR"),
            "Zero custo. Disponivel em bibliotecas publicas, telecentros, escola publica."));

        // === VOZ ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-038", "Microfone (dedicado)",
            HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.USB, ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH),
            Arrays.asList("Linux", "Windows", "macOS", "Android", "iOS"),
            Arrays.asList("motora", "comunicacao"),
            Arrays.asList("voice_high_quality", "noise_cancellation"),
            new ArrayList<>(),
            0.0, true, Arrays.asList("pt-BR"),
            "Para dictacao de codigo por voz. Microfone de lapela R$30 = suficiente."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-039", "Camera Web (webcam)",
            HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.USB, ConnectionType.WIFI),
            Arrays.asList("Linux", "Windows", "macOS", "Android", "iOS"),
            Arrays.asList("motora", "comunicacao", "auditiva"),
            Arrays.asList("hand_tracking", "face_tracking", "eye_tracking_basic", "gesture", "sign_language_capture"),
            new ArrayList<>(),
            0.0, true, Arrays.asList("pt-BR"),
            "Gestos de mao, tracking facial, captura de Libras. Webcam R$50 = suficiente."));

        // === INPUT ALTERNATIVO ===
        HARDWARE_CATALOG.add(new HardwareDevice("HW-040", "Teclado Braille (Perkins / eletronico)",
            HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.USB),
            Arrays.asList("Android", "iOS", "Windows", "Linux", "macOS"),
            Arrays.asList("visual"),
            Arrays.asList("braille_input_6_keys", "braille_input_8_keys", "space", "navigation"),
            new ArrayList<>(),
            20.0, true, Arrays.asList("pt-BR"),
            "6-8 teclas para digitar em Braille. Conecta no smartphone. Cego digita codigo direto."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-041", "Ponteiro Laser / Caneta Virtual",
            HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
            Arrays.asList(ConnectionType.BLUETOOTH),
            Arrays.asList("Windows", "Linux", "Android"),
            Arrays.asList("motora"),
            Arrays.asList("laser_point", "gesture"),
            new ArrayList<>(),
            8.0, true, Arrays.asList("pt-BR"),
            "Aponta laser na tela de longe. Para quem nao alcanca a tela ou tem tremor."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-042", "Haptic Vest / Colete Tátil",
            HardwareCategory.WEARABLE, HardwareCost.HIGH, HardwareAvailability.EXPERIMENTAL,
            Arrays.asList(ConnectionType.BLUETOOTH, ConnectionType.WIFI),
            Arrays.asList("Windows", "Linux", "Android"),
            Arrays.asList("visual", "auditiva", "motora"),
            new ArrayList<>(),
            Arrays.asList("haptic_array", "vibration_patterns_complex"),
            4.0, true, Arrays.asList("pt-BR"),
            "Vibracoes no corpo representam informacao. Surdo sente musica. Cego sente ambiente."));

        HARDWARE_CATALOG.add(new HardwareDevice("HW-043", "Fone de Ouvido Comum",
            HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.UBIQUITOUS,
            Arrays.asList(ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH),
            Arrays.asList("Standalone"),
            Arrays.asList("auditiva", "espectro_autista", "cognitiva"),
            Arrays.asList("microphone_optional"),
            Arrays.asList("audio", "audio_isolated"),
            0.0, true, Arrays.asList("pt-BR"),
            "Fone comum R$15. Para TTS (cego), isolamento (autista), audio direto (surdo com aparelho)."));
    }

    // ============================================================================
    // 4. MOTOR DE COMPATIBILIDADE
    // ============================================================================

    public static class HardwareCompatibilityEngine {
        public final Map<String, HardwareDevice> catalog;

        public HardwareCompatibilityEngine() {
            catalog = new HashMap<>();
            for (HardwareDevice d : HARDWARE_CATALOG) {
                catalog.put(d.device_id, d);
            }
        }

        public List<HardwareDevice> find_by_disability(String disability_category) {
            List<HardwareDevice> result = new ArrayList<>();
            for (HardwareDevice d : HARDWARE_CATALOG) {
                if (d.disabilities_served.contains(disability_category)) result.add(d);
            }
            return result;
        }

        public List<HardwareDevice> find_by_cost(HardwareCost max_cost) {
            List<HardwareCost> cost_order = Arrays.asList(
                HardwareCost.FREE, HardwareCost.VERY_LOW, HardwareCost.LOW,
                HardwareCost.MEDIUM, HardwareCost.HIGH, HardwareCost.VERY_HIGH
            );
            int max_idx = cost_order.indexOf(max_cost);
            List<HardwareDevice> result = new ArrayList<>();
            for (HardwareDevice d : HARDWARE_CATALOG) {
                if (cost_order.indexOf(d.cost) <= max_idx) result.add(d);
            }
            return result;
        }

        public List<HardwareDevice> find_by_platform(String platform) {
            List<HardwareDevice> result = new ArrayList<>();
            for (HardwareDevice d : HARDWARE_CATALOG) {
                if (d.platforms.contains(platform)) result.add(d);
            }
            return result;
        }

        public List<HardwareDevice> find_by_input_capability(String capability) {
            List<HardwareDevice> result = new ArrayList<>();
            for (HardwareDevice d : HARDWARE_CATALOG) {
                if (d.input_capabilities.contains(capability)) result.add(d);
            }
            return result;
        }

        public List<HardwareDevice> find_by_output_capability(String capability) {
            List<HardwareDevice> result = new ArrayList<>();
            for (HardwareDevice d : HARDWARE_CATALOG) {
                if (d.output_capabilities.contains(capability)) result.add(d);
            }
            return result;
        }

        public List<HardwareDevice> find_offline_capable() {
            List<HardwareDevice> result = new ArrayList<>();
            for (HardwareDevice d : HARDWARE_CATALOG) {
                if (d.offline_capable) result.add(d);
            }
            return result;
        }

        public List<HardwareDevice> recommend_setup(List<String> disabilities, HardwareCost budget, String platform) {
            Set<HardwareDevice> recommendations = new HashSet<>();
            for (String disability : disabilities) {
                for (HardwareDevice d : find_by_disability(disability)) {
                    if (d.platforms.contains(platform) || d.platforms.isEmpty()) {
                        recommendations.add(d);
                    }
                }
            }
            List<HardwareDevice> budget_devices = find_by_cost(budget);
            List<HardwareDevice> finalList = new ArrayList<>();
            for (HardwareDevice d : recommendations) {
                if (budget_devices.contains(d)) finalList.add(d);
            }
            if (finalList.isEmpty()) {
                finalList.addAll(find_by_cost(HardwareCost.FREE));
                finalList.addAll(find_by_cost(HardwareCost.VERY_LOW));
            }
            return new ArrayList<>(new HashSet<>(finalList));
        }

        public Map<String, Object> total_setup_cost(List<HardwareDevice> devices) {
            Map<HardwareCost, int[]> cost_ranges = new HashMap<>();
            cost_ranges.put(HardwareCost.FREE, new int[]{0, 0});
            cost_ranges.put(HardwareCost.VERY_LOW, new int[]{1, 100});
            cost_ranges.put(HardwareCost.LOW, new int[]{100, 500});
            cost_ranges.put(HardwareCost.MEDIUM, new int[]{500, 2000});
            cost_ranges.put(HardwareCost.HIGH, new int[]{2000, 10000});
            cost_ranges.put(HardwareCost.VERY_HIGH, new int[]{10000, 100000});
            cost_ranges.put(HardwareCost.SUBSIDIZED, new int[]{0, 0});

            int min_total = 0, max_total = 0;
            Set<String> categories = new HashSet<>();
            for (HardwareDevice d : devices) {
                int[] range = cost_ranges.get(d.cost);
                min_total += range[0];
                max_total += range[1];
                categories.add(d.category.value);
            }
            Map<String, Object> result = new HashMap<>();
            result.put("min_brl", min_total);
            result.put("max_brl", max_total);
            result.put("device_count", devices.size());
            result.put("categories", new ArrayList<>(categories));
            return result;
        }
    }

    // ============================================================================
    // 5. BRIDGE IDE <-> HARDWARE
    // ============================================================================

    public static class HardwareBridge {
        public List<HardwareDevice> connected_devices = new ArrayList<>();
        public HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        public List<String> active_inputs = new ArrayList<>();
        public List<String> active_outputs = new ArrayList<>();

        public List<HardwareDevice> detect_devices() {
            HardwareDevice base = engine.catalog.get("HW-001");
            if (base != null) {
                connected_devices = new ArrayList<>(Arrays.asList(base));
                _update_capabilities();
            }
            return connected_devices;
        }

        public boolean connect_device(HardwareDevice device) {
            if (!connected_devices.contains(device)) {
                connected_devices.add(device);
                _update_capabilities();
            }
            return true;
        }

        public boolean disconnect_device(HardwareDevice device) {
            if (connected_devices.contains(device)) {
                connected_devices.remove(device);
                _update_capabilities();
            }
            return true;
        }

        private void _update_capabilities() {
            active_inputs.clear();
            active_outputs.clear();
            for (HardwareDevice d : connected_devices) {
                for (String cap : d.input_capabilities) {
                    if (!active_inputs.contains(cap)) active_inputs.add(cap);
                }
                for (String cap : d.output_capabilities) {
                    if (!active_outputs.contains(cap)) active_outputs.add(cap);
                }
            }
        }

        public List<String> available_input_modes() {
            Set<String> modes = new LinkedHashSet<>();
            for (HardwareDevice d : connected_devices) {
                if (d.input_capabilities.contains("voice") || d.input_capabilities.contains("microphone")) {
                    modes.add("voz"); modes.add("voz_codigo");
                }
                if (d.input_capabilities.contains("touch") || d.input_capabilities.contains("touch_small")) {
                    modes.add("toque");
                }
                if (d.input_capabilities.contains("keyboard")) modes.add("teclado_completo");
                if (d.input_capabilities.contains("braille_keys") || d.input_capabilities.contains("braille_input_6_keys")) {
                    modes.add("teclado_braille");
                }
                if (d.input_capabilities.contains("eye_gaze")) modes.add("rastreio_olhos");
                if (d.input_capabilities.contains("single_switch") || d.input_capabilities.contains("dual_switch")) {
                    modes.add("chave"); modes.add("chave_dupla");
                }
                if (d.input_capabilities.contains("trackball")) modes.add("trackball");
                if (d.input_capabilities.contains("foot_press_left")) modes.add("pedal_pe");
                if (d.input_capabilities.contains("head_stick")) modes.add("teclado_cabeca");
                if (d.input_capabilities.contains("sip_puff")) modes.add("teclado_boca");
                if (d.input_capabilities.contains("eeg_waves") || d.input_capabilities.contains("neural_spikes")) {
                    modes.add("interface_cerebral");
                }
                if (d.input_capabilities.contains("emg_signal")) modes.add("eletromiografo");
                if (d.input_capabilities.contains("hand_tracking")) modes.add("gesto");
                if (d.input_capabilities.contains("heart_rate")) modes.add("biofeedback");
            }
            return new ArrayList<>(modes);
        }

        public List<String> available_output_modes() {
            Set<String> modes = new LinkedHashSet<>();
            for (HardwareDevice d : connected_devices) {
                if (d.output_capabilities.contains("screen") || d.output_capabilities.contains("screen_large")) {
                    modes.add("texto_visual");
                }
                if (d.output_capabilities.contains("screen_tiny")) modes.add("texto_tela_pequena");
                if (d.output_capabilities.contains("tts") || d.output_capabilities.contains("tts_basic") || d.output_capabilities.contains("speaker")) {
                    modes.add("texto_para_voz");
                }
                if (d.output_capabilities.contains("braille_cells_40") || d.output_capabilities.contains("braille_cells_14")) {
                    modes.add("display_braille");
                }
                if (d.output_capabilities.contains("vibration") || d.output_capabilities.contains("haptic")) {
                    modes.add("haptico");
                }
                if (d.output_capabilities.contains("color_light")) modes.add("luz_cor");
                if (d.output_capabilities.contains("audio_amplified")) modes.add("audio_amplificado");
                if (d.output_capabilities.contains("audio_anc")) modes.add("audio_cancelamento_ruido");
                if (d.output_capabilities.contains("hud_overlay")) modes.add("hud_oculos");
                if (d.output_capabilities.contains("taptic_engine")) modes.add("taptic_preciso");
            }
            return new ArrayList<>(modes);
        }

        public boolean supports_input_mode(String mode) {
            return available_input_modes().contains(mode);
        }

        public boolean supports_output_mode(String mode) {
            return available_output_modes().contains(mode);
        }

        public Map<String, Object> session_info() {
            Map<String, Object> info = new HashMap<>();
            List<String> names = new ArrayList<>();
            for (HardwareDevice d : connected_devices) names.add(d.name);
            info.put("connected_devices", names);
            info.put("device_count", connected_devices.size());
            info.put("available_inputs", available_input_modes());
            info.put("available_outputs", available_output_modes());
            info.put("total_input_capabilities", active_inputs.size());
            info.put("total_output_capabilities", active_outputs.size());
            return info;
        }
    }

    // ============================================================================
    // 6. PERFIS DE SETUP
    // ============================================================================

    public static List<HardwareDevice> create_setup_budget() {
        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        return Arrays.asList(engine.catalog.get("HW-001"), engine.catalog.get("HC-029"), engine.catalog.get("HW-018"));
    }

    public static List<HardwareDevice> create_setup_blind() {
        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        return Arrays.asList(engine.catalog.get("HW-001"), engine.catalog.get("HW-014"), engine.catalog.get("HW-013"), engine.catalog.get("HW-040"));
    }

    public static List<HardwareDevice> create_setup_deaf() {
        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        return Arrays.asList(engine.catalog.get("HW-001"), engine.catalog.get("HW-006"), engine.catalog.get("HC-031"));
    }

    public static List<HardwareDevice> create_setup_motor_severe() {
        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        return Arrays.asList(engine.catalog.get("HW-011"), engine.catalog.get("HW-016"), engine.catalog.get("HW-038"));
    }

    public static List<HardwareDevice> create_setup_autism() {
        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        return Arrays.asList(engine.catalog.get("HW-001"), engine.catalog.get("HC-029"), engine.catalog.get("HC-031"), engine.catalog.get("HC-032"));
    }

    public static List<HardwareDevice> create_setup_adhd() {
        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        return Arrays.asList(engine.catalog.get("HW-001"), engine.catalog.get("HC-029"), engine.catalog.get("HW-007"));
    }

    public static List<HardwareDevice> create_setup_epilepsy() {
        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        return Arrays.asList(engine.catalog.get("HW-001"), engine.catalog.get("HC-031"), engine.catalog.get("HW-007"));
    }

    public static List<HardwareDevice> create_setup_public_terminal() {
        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        return Arrays.asList(engine.catalog.get("HW-037"));
    }

    public static List<HardwareDevice> create_setup_zero_cost() {
        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();
        return Arrays.asList(engine.catalog.get("HW-037"), engine.catalog.get("HW-014"));
    }

    // ============================================================================
    // 7. ESCADA DE ESCALABILIDADE
    // ============================================================================

    public static class HardwareEscalationLadder {
        public static final Object[][] RUNGS = new Object[][]{
            {"Degrau 0: ZERO CUSTO", "create_setup_zero_cost", "Biblioteca publica + NVDA gratis. Todo mundo comeca aqui."},
            {"Degrau 1: SMARTPHONE", "create_setup_budget", "Smartphone R$300 + fone R$50 + switch R$30. Acesse de qualquer lugar."},
            {"Degrau 2: TABLET/WEARABLE", "create_setup_deaf", "Adiciona smartwatch/luz para feedback multimodal."},
            {"Degrau 3: ASSISTIVO ESPECIFICO", "create_setup_blind", "Adiciona braille/eye-tracker especifico para deficiencia."},
            {"Degrau 4: SETUP COMPLETO", "create_setup_motor_severe", "Notebook + eye-tracker + microfone. Desenvolvimento profissional."},
            {"Degrau 5: BCI/EXPERIMENTAL", null, "BCI, haptic vest, smart glasses. Fronteira da tecnologia."}
        };

        public static Object[] recommend_rung(HardwareCost budget) {
            if (budget == HardwareCost.FREE) return new Object[]{0, RUNGS[0][2]};
            if (budget == HardwareCost.VERY_LOW || budget == HardwareCost.LOW) return new Object[]{1, RUNGS[1][2]};
            if (budget == HardwareCost.MEDIUM) return new Object[]{2, RUNGS[2][2]};
            if (budget == HardwareCost.HIGH) return new Object[]{3, RUNGS[3][2]};
            if (budget == HardwareCost.VERY_HIGH) return new Object[]{5, RUNGS[5][2]};
            return new Object[]{0, RUNGS[0][2]};
        }

        public static void show_ladder() {
            System.out.println("\nESCALADA DE HARDWARE -- Do Zero ao Profissional");
            System.out.println("=".repeat(60));
            for (Object[] rung : RUNGS) {
                String name = (String) rung[0];
                String func = (String) rung[1];
                String desc = (String) rung[2];
                System.out.println("\n  " + name);
                System.out.println("    " + desc);
                if (func != null) {
                    // simplified cost print for demo
                    System.out.println("    (custo estimado via engine)");
                }
            }
        }
    }

    // ============================================================================
    // 8. DEMONSTRACAO (main)
    // ============================================================================

    public static void demo() {
        System.out.println("=".repeat(70));
        System.out.println("OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel");
        System.out.println("=".repeat(70));

        HardwareCompatibilityEngine engine = new HardwareCompatibilityEngine();

        System.out.println("\nCatalogo: " + HARDWARE_CATALOG.size() + " dispositivos mapeados");
        Map<String, Integer> cats = new TreeMap<>();
        for (HardwareDevice d : HARDWARE_CATALOG) {
            cats.put(d.category.value, cats.getOrDefault(d.category.value, 0) + 1);
        }
        for (Map.Entry<String, Integer> e : cats.entrySet()) {
            System.out.printf("  %-25s %3d dispositivos%n", e.getKey(), e.getValue());
        }

        System.out.println("\nPor custo:");
        Map<String, Integer> costs = new TreeMap<>();
        for (HardwareDevice d : HARDWARE_CATALOG) {
            costs.put(d.cost.value, costs.getOrDefault(d.cost.value, 0) + 1);
        }
        for (Map.Entry<String, Integer> e : costs.entrySet()) {
            System.out.printf("  %-15s %3d dispositivos%n", e.getKey(), e.getValue());
        }

        System.out.println("\nPor disponibilidade:");
        Map<String, Integer> avail = new TreeMap<>();
        for (HardwareDevice d : HARDWARE_CATALOG) {
            avail.put(d.availability.value, avail.getOrDefault(d.availability.value, 0) + 1);
        }
        for (Map.Entry<String, Integer> e : avail.entrySet()) {
            System.out.printf("  %-15s %3d dispositivos%n", e.getKey(), e.getValue());
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("HARDWARE BRIDGE -- Deteccao e Configuracao");
        System.out.println("=".repeat(70));

        HardwareBridge bridge = new HardwareBridge();
        List<HardwareDevice> detected = bridge.detect_devices();
        List<String> detectedNames = new ArrayList<>();
        for (HardwareDevice d : detected) detectedNames.add(d.name);
        System.out.println("\nDispositivos detectados: " + detectedNames);
        Map<String, Object> info = bridge.session_info();
        System.out.println("Inputs disponiveis:  " + info.get("available_inputs"));
        System.out.println("Outputs disponiveis: " + info.get("available_outputs"));

        System.out.println("\n+ Conectando Display Braille...");
        bridge.connect_device(engine.catalog.get("HW-013"));
        info = bridge.session_info();
        System.out.println("Inputs:  " + info.get("available_inputs"));
        System.out.println("Outputs: " + info.get("available_outputs"));

        System.out.println("\n+ Conectando Eye Tracker...");
        bridge.connect_device(engine.catalog.get("HW-016"));
        info = bridge.session_info();
        System.out.println("Inputs:  " + info.get("available_inputs"));
        System.out.println("Outputs: " + info.get("available_outputs"));

        System.out.println("\n+ Conectando Smartwatch...");
        bridge.connect_device(engine.catalog.get("HW-006"));
        info = bridge.session_info();
        System.out.println("Inputs:  " + info.get("available_inputs"));
        System.out.println("Outputs: " + info.get("available_outputs"));

        System.out.println("\n" + "=".repeat(70));
        System.out.println("PERFIS DE SETUP");
        System.out.println("=".repeat(70));

        Map<String, List<HardwareDevice>> setups = new LinkedHashMap<>();
        setups.put("ZERO CUSTO (biblioteca)", create_setup_zero_cost());
        setups.put("BAIXO CUSTO (smartphone)", create_setup_budget());
        setups.put("CEGO (braille completo)", create_setup_blind());
        setups.put("SURDO (visual+haptic)", create_setup_deaf());
        setups.put("TETRAPLEGICO (eye+voz)", create_setup_motor_severe());
        setups.put("AUTISTA (calmo)", create_setup_autism());
        setups.put("TDAH (foco)", create_setup_adhd());
        setups.put("EPILEPSIA (seguro)", create_setup_epilepsy());
        setups.put("TERMINAL PUBLICO", create_setup_public_terminal());

        for (Map.Entry<String, List<HardwareDevice>> entry : setups.entrySet()) {
            Map<String, Object> cost = engine.total_setup_cost(entry.getValue());
            System.out.println("\n  " + entry.getKey());
            System.out.println("    Devices: " + cost.get("device_count") + " | Custo: R$ " + cost.get("min_brl") + "-" + cost.get("max_brl"));
            for (HardwareDevice d : entry.getValue()) {
                System.out.println("      - " + d.name);
            }
        }

        HardwareEscalationLadder.show_ladder();

        System.out.println("\n" + "=".repeat(70));
        System.out.println("COBERTURA DE CATEGORIAS");
        System.out.println("=".repeat(70));
        for (HardwareCategory cat : HardwareCategory.values()) {
            long count = HARDWARE_CATALOG.stream().filter(d -> d.category == cat).count();
            System.out.printf("  %-25s %3d dispositivos%n", cat.value, count);
        }

        System.out.println("\nCOBERTURA POR DEFICIENCIA:");
        Set<String> all_disabilities = new TreeSet<>();
        for (HardwareDevice d : HARDWARE_CATALOG) {
            all_disabilities.addAll(d.disabilities_served);
        }
        for (String disab : all_disabilities) {
            long count = engine.find_by_disability(disab).size();
            System.out.printf("  %-25s %3d dispositivos%n", disab, count);
        }

        System.out.println("\nTotal dispositivos: " + HARDWARE_CATALOG.size());
        System.out.println("Categorias: " + HardwareCategory.values().length);
        System.out.println("Setup minimo: R$ 0 (biblioteca + NVDA gratis)");
        System.out.println("\nTODO hardware. TODA deficiencia. ZERO barreira.");
    }

    public static void main(String[] args) {
        demo();
    }
}