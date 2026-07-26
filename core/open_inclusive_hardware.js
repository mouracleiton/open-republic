// OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel
// Gerado a partir de open_inclusive_hardware.py (fonte de verdade)
// Comentarios em Portugues conforme padrao OpenRepublic

'use strict';

// ============================================================================
// 1. CATEGORIAS DE HARDWARE
// ============================================================================

const HardwareCategory = Object.freeze({
    MASS: "massa",
    ASSISTIVE_VISUAL: "assistivo_visual",
    ASSISTIVE_MOTOR: "assistivo_motor",
    ASSISTIVE_AUDITORY: "assistivo_auditivo",
    ASSISTIVE_COGNITIVE: "assistivo_cognitivo",
    TERMINAL_PUBLIC: "terminal_publico",
    WEARABLE: "vestivel",
    BRAIN: "cerebral"
});

const HardwareCost = Object.freeze({
    FREE: "gratis",
    VERY_LOW: "muito_baixo",
    LOW: "baixo",
    MEDIUM: "medio",
    HIGH: "alto",
    VERY_HIGH: "muito_alto",
    SUBSIDIZED: "subsidiado"
});

const HardwareAvailability = Object.freeze({
    UBIQUITOUS: "ubiquo",
    COMMON: "comum",
    SPECIALIZED: "especializado",
    MEDICAL: "medico",
    RARE: "raro",
    EXPERIMENTAL: "experimental"
});

const ConnectionType = Object.freeze({
    BLUETOOTH: "bluetooth",
    USB: "usb",
    WIFI: "wifi",
    NFC: "nfc",
    CLOUD: "nuvem",
    AUDIO_JACK: "jack_audio",
    PROPRIETARY: "proprietario",
    WIRELESS: "sem_fio_generico",
    HDMI: "hdmi"
});

// ============================================================================
// 2. PERFIL DE HARDWARE
// ============================================================================

class HardwareDevice {
    constructor(device_id, name, category, cost, availability,
                connections = [], platforms = [], disabilities_served = [],
                input_capabilities = [], output_capabilities = [],
                battery_hours = 0.0, offline_capable = true,
                languages_supported = ["pt-BR"], description = "") {
        this.device_id = device_id;
        this.name = name;
        this.category = category;
        this.cost = cost;
        this.availability = availability;
        this.connections = connections;
        this.platforms = platforms;
        this.disabilities_served = disabilities_served;
        this.input_capabilities = input_capabilities;
        this.output_capabilities = output_capabilities;
        this.battery_hours = battery_hours;
        this.offline_capable = offline_capable;
        this.languages_supported = languages_supported;
        this.description = description;
    }
}

// ============================================================================
// 3. CATALOGO DE HARDWARE (44 DISPOSITIVOS)
// ============================================================================

const HARDWARE_CATALOG = [
    // === SMARTPHONE (massa) ===
    new HardwareDevice("HW-001", "Smartphone Android (qualquer)",
        HardwareCategory.MASS, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.NFC, ConnectionType.AUDIO_JACK],
        ["Android"],
        ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "multipla", "temporaria"],
        ["touch", "voice", "camera", "microphone", "bluetooth_keyboard", "nfc", "accelerometer", "gyroscope"],
        ["screen", "speaker", "vibration", "flash_led", "screen_reader"],
        12.0, true, ["pt-BR"],
        "O dispositivo mais inclusivo do planeta. TalkBack, Voice Access, Switch Access nativos."),

    new HardwareDevice("HW-002", "iPhone (qualquer)",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.NFC],
        ["iOS"],
        ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "multipla", "temporaria"],
        ["touch", "voice", "face_id", "camera", "microphone", "bluetooth_keyboard", "lidar"],
        ["screen", "speaker", "vibration", "taptic_engine", "voiceover", "flash_led"],
        15.0, true, ["pt-BR"],
        "VoiceOver, Switch Control, Voice Control, Sound Detection nativos. Lidar para deteccao de obstaculos."),

    new HardwareDevice("HW-003", "Smartphone basico (teclado fisico)",
        HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        [ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH],
        ["KaiOS", "Feature Phone"],
        ["visual", "motora", "temporaria"],
        ["keypad", "voice", "microphone"],
        ["screen_small", "speaker", "vibration", "tts_basic"],
        72.0, true, ["pt-BR"],
        "Telefone botoeiro com TTS. Para quem nao tem smartphone ou prefere teclado fisico."),

    // === TABLET ===
    new HardwareDevice("HW-004", "Tablet Android",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI],
        ["Android"],
        ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento"],
        ["touch", "voice", "camera", "microphone", "stylus", "bluetooth_keyboard"],
        ["screen_large", "speaker", "vibration"],
        10.0, true, ["pt-BR"],
        "Tela maior = mais area para botoes grandes, blocos visuais, zoom."),

    new HardwareDevice("HW-005", "iPad",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI],
        ["iPadOS"],
        ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento"],
        ["touch", "voice", "face_id", "camera", "microphone", "stylus_pencil", "lidar"],
        ["screen_large", "speaker", "taptic_engine", "voiceover"],
        10.0, true, ["pt-BR"],
        "Apple Pencil para deteccao de tremores. AssistiveTouch. Full Keyboard Control."),

    // === SMARTWATCH / WEARABLE ===
    new HardwareDevice("HW-006", "Smartwatch Android (WearOS)",
        HardwareCategory.WEARABLE, HardwareCost.MEDIUM, HardwareAvailability.COMMON,
        [ConnectionType.BLUETOOTH, ConnectionType.WIFI],
        ["WearOS"],
        ["auditiva", "motora", "cognitiva", "temporaria"],
        ["touch_small", "voice", "microphone", "accelerometer", "heart_rate", "gestures", "crown"],
        ["screen_tiny", "vibration", "speaker_tiny", "haptic"],
        24.0, true, ["pt-BR"],
        "Vibracao no pulso para alertas (surdez). Monitor de batimento (epilepsia/ansiedade). Coroa para navegacao (motor)."),

    new HardwareDevice("HW-007", "Apple Watch",
        HardwareCategory.WEARABLE, HardwareCost.MEDIUM, HardwareAvailability.COMMON,
        [ConnectionType.BLUETOOTH, ConnectionType.WIFI],
        ["watchOS"],
        ["auditiva", "motora", "cognitiva", "temporaria", "neurologica"],
        ["touch_small", "voice", "microphone", "crown_digital", "accelerometer", "heart_rate", "ecg", "fall_detection", "gestures", "sip_pinch"],
        ["screen_tiny", "taptic_engine", "speaker_tiny", "haptic"],
        18.0, true, ["pt-BR"],
        "Fall Detection (queda). ECG (coracao). Taptic Engine para surdos. AssistiveTouch (pinca/sorvo para tetraplegia). Noise app (autismo)."),

    new HardwareDevice("HW-008", "Smartwatch basico / Pulseira fitness",
        HardwareCategory.WEARABLE, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.BLUETOOTH],
        ["Proprietary"],
        ["auditiva", "temporaria"],
        ["touch_tiny", "accelerometer", "heart_rate"],
        ["screen_tiny", "vibration"],
        168.0, true, ["pt-BR"],
        "R$80-200. Vibracao para notificacoes (surdez). Monitor basico de sono/atividade."),

    new HardwareDevice("HW-009", "Anel Smart (Smart Ring)",
        HardwareCategory.WEARABLE, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        [ConnectionType.BLUETOOTH],
        ["Proprietary"],
        ["auditiva", "neurologica"],
        ["accelerometer", "heart_rate", "temperature", "spO2"],
        ["vibration_tiny", "led"],
        168.0, true, ["pt-BR"],
        "Discreto. Monitor de sono, temperatura, SpO2. Para autismo: biofeedback discreto."),

    new HardwareDevice("HW-010", "Oculos Inteligentes (Smart Glasses)",
        HardwareCategory.WEARABLE, HardwareCost.HIGH, HardwareAvailability.SPECIALIZED,
        [ConnectionType.BLUETOOTH, ConnectionType.WIFI],
        ["Android", "Proprietary"],
        ["visual", "auditiva", "motora", "neurologica"],
        ["voice", "camera", "microphone", "bone_conduction_audio", "head_tracking", "eye_tracking_basic"],
        ["hud_overlay", "bone_conduction_speaker", "vibration"],
        6.0, true, ["pt-BR"],
        "Legendas em tempo real no campo de visao (surdez). Navegacao por setas (cegueira). Heads-up display."),

    // === COMPUTADOR / NOTEBOOK ===
    new HardwareDevice("HW-011", "Notebook / Laptop",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.AUDIO_JACK],
        ["Linux", "Windows", "macOS"],
        ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "neurologica", "multipla", "temporaria"],
        ["keyboard", "trackpad", "microphone", "camera", "bluetooth_devices"],
        ["screen", "speaker", "vibration_rare"],
        8.0, true, ["pt-BR"],
        "Plataforma de desenvolvimento completa. Screen readers, IDEs, eye-tracking via USB."),

    new HardwareDevice("HW-012", "Desktop / PC",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.COMMON,
        [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.AUDIO_JACK],
        ["Linux", "Windows"],
        ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "neurologica", "multipla"],
        ["keyboard", "mouse", "microphone", "camera", "usb_devices", "pcie_cards"],
        ["screen_large", "speaker", "multi_monitor"],
        0.0, true, ["pt-BR"],
        "Maximo de conectividade. Multi-tela, GPUs para IA, todo tipo de periferico."),

    // === LEITOR DE TELA / DISPLAY BRAILLE ===
    new HardwareDevice("HW-013", "Display Braille (linha braille)",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.HIGH, HardwareAvailability.SPECIALIZED,
        [ConnectionType.BLUETOOTH, ConnectionType.USB],
        ["Android", "iOS", "Linux", "Windows", "macOS"],
        ["visual"],
        ["braille_keys", "routing_buttons", "navigation"],
        ["braille_cells_40", "braille_cells_80"],
        20.0, true, ["pt-BR"],
        "40-80 celulas braille. Celulas piezoeletricas que sobem e descem. Cego le codigo tateando."),

    new HardwareDevice("HW-013b", "Display Braille portatil (14-20 celulas)",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        [ConnectionType.BLUETOOTH, ConnectionType.USB],
        ["Android", "iOS"],
        ["visual"],
        ["braille_keys"],
        ["braille_cells_14"],
        20.0, true, ["pt-BR"],
        "Versao portatil menor. Cabe no bolso. Conecta no smartphone."),

    new HardwareDevice("HW-014", "Leitor de tela software (NVDA, Orca, VoiceOver, TalkBack)",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.FREE, HardwareAvailability.UBIQUITOUS,
        [],
        ["Android", "iOS", "Linux", "Windows", "macOS"],
        ["visual"],
        [],
        ["tts", "braille_output", "audio_cues"],
        0.0, true, ["pt-BR"],
        "NVDA (gratis, Windows). Orca (Linux). VoiceOver (Apple). TalkBack (Android). Converte tela em voz/braille."),

    new HardwareDevice("HW-015", "Lupa eletronica / CCTV",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        [ConnectionType.HDMI],
        ["Standalone"],
        ["visual"],
        ["camera_zoom"],
        ["screen_zoomed"],
        4.0, true, ["pt-BR"],
        "Camera que amplia texto/papel para tela. Para baixa visao."),

    // === EYE TRACKER / SWITCH / MOTOR ===
    new HardwareDevice("HW-016", "Eye Tracker (Tobii, EyeX)",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.HIGH, HardwareAvailability.SPECIALIZED,
        [ConnectionType.USB, ConnectionType.WIFI],
        ["Windows", "Linux"],
        ["motora", "multipla"],
        ["eye_gaze", "dwell_selection", "blink"],
        [],
        0.0, true, ["pt-BR"],
        "Camera infravermelha rastreia olhos. Tetraplegia, ELA, paralisia cerebral. Custo: R$2.000-8.000."),

    new HardwareDevice("HW-017", "Eye Tracker portatil (smartphone)",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        [],
        ["Android", "iOS"],
        ["motora", "multipla"],
        ["eye_gaze_front_camera"],
        [],
        6.0, true, ["pt-BR"],
        "Usa camera frontal do smartphone para rastrear olhos. Precisao menor mas gratuito com app."),

    new HardwareDevice("HW-018", "Switch / Botao adaptativo",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        [ConnectionType.BLUETOOTH, ConnectionType.AUDIO_JACK, ConnectionType.USB],
        ["Android", "iOS", "Windows", "Linux", "macOS"],
        ["motora", "multipla", "desenvolvimento"],
        ["single_switch", "dual_switch"],
        [],
        0.0, true, ["pt-BR"],
        "Um ou dois botoes grandes. Scan automatico passa opcoes, usuario aciona para selecionar. DIY possivel por R$20."),

    new HardwareDevice("HW-019", "Teclado adaptativo grande",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
        [ConnectionType.BLUETOOTH, ConnectionType.USB],
        ["Android", "iOS", "Windows", "Linux", "macOS"],
        ["motora", "cognitiva", "desenvolvimento"],
        ["large_keys", "color_coded"],
        [],
        0.0, true, ["pt-BR"],
        "Teclas 3x maiores, coloridas, com guard de mao. Para tremores, baixa destreza, Down."),

    new HardwareDevice("HW-020", "Teclado de cabeca / boca",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
        [ConnectionType.USB, ConnectionType.BLUETOOTH],
        ["Windows", "Linux", "Android"],
        ["motora"],
        ["head_stick", "mouth_stick", "sip_puff"],
        [],
        0.0, true, ["pt-BR"],
        "Ponteiro de cabeca ou bocal para digitar em teclado na tela. Sip-and-puff = sopro/succao."),

    new HardwareDevice("HW-021", "Trackball adaptativo",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.COMMON,
        [ConnectionType.BLUETOOTH, ConnectionType.USB],
        ["Windows", "Linux", "macOS", "Android"],
        ["motora"],
        ["trackball", "large_ball"],
        [],
        0.0, true, ["pt-BR"],
        "Bola grande movida com palma/queixo/dorso do pe. Estavel para tremores (Parkinson)."),

    new HardwareDevice("HW-022", "Pedal de pe (Foot Pedal)",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        [ConnectionType.USB, ConnectionType.BLUETOOTH],
        ["Windows", "Linux", "macOS"],
        ["motora", "temporaria"],
        ["foot_press_left", "foot_press_right", "foot_press_center"],
        [],
        0.0, true, ["pt-BR"],
        "Para quem tem uso dos pes mas nao das maos. 3 pedais = 3 botoes. R$50-150."),

    new HardwareDevice("HW-023", "EMG / MIODOELETRICO (braco bio-feedback)",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.MEDIUM, HardwareAvailability.EXPERIMENTAL,
        [ConnectionType.BLUETOOTH, ConnectionType.USB],
        ["Windows", "Linux", "Android"],
        ["motora", "multipla"],
        ["emg_signal", "muscle_activation"],
        [],
        8.0, true, ["pt-BR"],
        "Sensores no musculo. Detecta contracao muscular residual. Para amputados, paralisia parcial."),

    // === BCI / CEREBRAL ===
    new HardwareDevice("HW-024", "BCI Invasivo (Neuralink/Synchron)",
        HardwareCategory.BRAIN, HardwareCost.VERY_HIGH, HardwareAvailability.EXPERIMENTAL,
        [ConnectionType.WIFI, ConnectionType.BLUETOOTH],
        ["Windows", "Linux"],
        ["motora", "multipla"],
        ["neural_spikes", "motor_intention"],
        [],
        0.0, true, ["pt-BR"],
        "Eletrodos no cerebro. Tetraplegia profunda. Ainda em ensaios clinicos."),

    new HardwareDevice("HW-025", "BCI Nao-Invasivo (EEG headset)",
        HardwareCategory.BRAIN, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        [ConnectionType.BLUETOOTH, ConnectionType.USB],
        ["Windows", "Linux", "Android"],
        ["motora", "multipla"],
        ["eeg_waves", "concentration_level", "blink_detect"],
        ["neurofeedback_display"],
        6.0, true, ["pt-BR"],
        "Capacete com eletrodos. Le ondas cerebrais. Precisao baixa mas nao invasivo. R$500-3000."),

    // === AUDITIVO ===
    new HardwareDevice("HC-026", "Aparelho Auditivo (digital)",
        HardwareCategory.ASSISTIVE_AUDITORY, HardwareCost.MEDIUM, HardwareAvailability.MEDICAL,
        [ConnectionType.BLUETOOTH],
        ["Standalone"],
        ["auditiva"],
        ["bluetooth_audio_in"],
        ["audio_amplified", "audio_filtered"],
        96.0, true, ["pt-BR"],
        "Amplifica e filtra som. Bluetooth direto do smartphone. Programa SUS cobre."),

    new HardwareDevice("HC-027", "Implante Coclear",
        HardwareCategory.ASSISTIVE_AUDITORY, HardwareCost.VERY_HIGH, HardwareAvailability.MEDICAL,
        [ConnectionType.BLUETOOTH],
        ["Standalone"],
        ["auditiva"],
        ["bluetooth_audio_in"],
        ["electrical_stimulation"],
        24.0, true, ["pt-BR"],
        "Cirurgico. Eletrodos na coclea. Para surdez profunda. SUS cobre em alguns estados."),

    new HardwareDevice("HC-028", "Loop Magnetico / Sistema FM",
        HardwareCategory.ASSISTIVE_AUDITORY, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
        [ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH],
        ["Standalone"],
        ["auditiva"],
        ["audio_in"],
        ["magnetic_loop"],
        0.0, true, ["pt-BR"],
        "Cabo de loop magnetico no pescoco. Transmite audio direto pro aparelho auditivo. Elimina ruido ambiente."),

    // === COGNITIVO / SENSORIAL ===
    new HardwareDevice("HC-029", "Fone ANC (Active Noise Cancelling)",
        HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.BLUETOOTH, ConnectionType.AUDIO_JACK],
        ["Standalone"],
        ["espectro_autista", "auditiva", "cognitiva"],
        ["anc_microphone"],
        ["audio_anc", "audio_filtered"],
        30.0, true, ["pt-BR"],
        "Cancela ruido ambiente. ESCUDO SENSORIAL para autista/TDAH em ambiente ruidoso. R$100-500."),

    new HardwareDevice("HC-030", "Fone com microfone direcional",
        HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.LOW, HardwareAvailability.COMMON,
        [ConnectionType.BLUETOOTH, ConnectionType.AUDIO_JACK],
        ["Standalone"],
        ["auditiva", "espectro_autista"],
        ["directional_microphone"],
        ["audio_directed"],
        20.0, true, ["pt-BR"],
        "Captura som da frente, cancela resto. Para APD (Processamento Auditivo) e autismo."),

    new HardwareDevice("HC-031", "Luz Inteligente (Smart Bulb)",
        HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.WIFI, ConnectionType.BLUETOOTH],
        ["Android", "iOS"],
        ["visual", "auditiva", "espectro_autista", "neurologica"],
        [],
        ["color_light", "brightness_control", "temperature_color", "no_flicker"],
        0.0, true, ["pt-BR"],
        "Notificacao visual por cor (surdez). Luz quente para acalmar (autismo/epilepsia). Sem flicker."),

    new HardwareDevice("HC-032", "Weighted Blanket (Manta Ponderada)",
        HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        [],
        ["Physical"],
        ["espectro_autista", "cognitiva", "neurologica"],
        [],
        ["deep_pressure_stimulation"],
        0.0, true, ["pt-BR"],
        "Pressao profunda calmante. Reduz ansiedade (autismo/TDAH). Melhora sono. R$100-300."),

    new HardwareDevice("HC-033", "Bracelete Anti-Ansiedade / Vibratorio",
        HardwareCategory.WEARABLE, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        [ConnectionType.BLUETOOTH],
        ["Android", "iOS"],
        ["espectro_autista", "cognitiva", "neurologica"],
        ["heart_rate", "skin_conductance"],
        ["vibration_patterns", "temperature_cooling"],
        72.0, true, ["pt-BR"],
        "Vibracao para acalmar (biofeedback). Detecta crise de ansiedade por batimento. R$80-200."),

    // === TERMINAL PUBLICO ===
    new HardwareDevice("HW-034", "TV Smart (qualquer)",
        HardwareCategory.TERMINAL_PUBLIC, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.WIFI, ConnectionType.HDMI, ConnectionType.BLUETOOTH],
        ["Android TV", "Tizen", "webOS"],
        ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "temporaria"],
        ["remote", "voice", "bluetooth_keyboard", "camera_optional"],
        ["screen_huge", "speaker", "hdmi_out"],
        0.0, true, ["pt-BR"],
        "Todo estabelecimento tem uma TV. OpenTerminal transforma TV ociosa em terminal da Republica."),

    new HardwareDevice("HW-035", "Kiosk / Terminal Publico",
        HardwareCategory.TERMINAL_PUBLIC, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        [ConnectionType.WIFI, ConnectionType.USB],
        ["Linux", "Windows"],
        ["visual", "auditiva", "motora", "cognitiva", "multipla"],
        ["touch", "keypad", "nfc", "camera"],
        ["screen_large", "speaker"],
        0.0, true, ["pt-BR"],
        "Terminal em praca, hospital, escola. wheelchair-height. Audio jack para fone."),

    new HardwareDevice("HW-036", "Terminal Burro (Raspberry Pi + tela)",
        HardwareCategory.TERMINAL_PUBLIC, HardwareCost.VERY_LOW, HardwareAvailability.SPECIALIZED,
        [ConnectionType.WIFI, ConnectionType.USB, ConnectionType.AUDIO_JACK, ConnectionType.HDMI],
        ["Linux"],
        ["visual", "auditiva", "motora", "cognitiva"],
        ["keyboard", "usb_switch", "usb_eye_tracker", "bluetooth"],
        ["screen", "speaker", "audio_jack"],
        0.0, true, ["pt-BR"],
        "Raspberry Pi R$150 + tela R$100 = terminal completo. OpenKit da Republica."),

    new HardwareDevice("HW-037", "Computador Comunitario (biblioteca, escola)",
        HardwareCategory.TERMINAL_PUBLIC, HardwareCost.FREE, HardwareAvailability.COMMON,
        [ConnectionType.WIFI, ConnectionType.USB, ConnectionType.AUDIO_JACK],
        ["Linux", "Windows"],
        ["visual", "auditiva", "motora", "cognitiva", "multipla", "temporaria"],
        ["keyboard", "mouse", "microphone", "usb_devices"],
        ["screen", "speaker", "audio_jack"],
        0.0, true, ["pt-BR"],
        "Zero custo. Disponivel em bibliotecas publicas, telecentros, escola publica."),

    // === VOZ ===
    new HardwareDevice("HW-038", "Microfone (dedicado)",
        HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.USB, ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH],
        ["Linux", "Windows", "macOS", "Android", "iOS"],
        ["motora", "comunicacao"],
        ["voice_high_quality", "noise_cancellation"],
        [],
        0.0, true, ["pt-BR"],
        "Para dictacao de codigo por voz. Microfone de lapela R$30 = suficiente."),

    new HardwareDevice("HW-039", "Camera Web (webcam)",
        HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.USB, ConnectionType.WIFI],
        ["Linux", "Windows", "macOS", "Android", "iOS"],
        ["motora", "comunicacao", "auditiva"],
        ["hand_tracking", "face_tracking", "eye_tracking_basic", "gesture", "sign_language_capture"],
        [],
        0.0, true, ["pt-BR"],
        "Gestos de mao, tracking facial, captura de Libras. Webcam R$50 = suficiente."),

    // === INPUT ALTERNATIVO ===
    new HardwareDevice("HW-040", "Teclado Braille (Perkins / eletronico)",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        [ConnectionType.BLUETOOTH, ConnectionType.USB],
        ["Android", "iOS", "Windows", "Linux", "macOS"],
        ["visual"],
        ["braille_input_6_keys", "braille_input_8_keys", "space", "navigation"],
        [],
        20.0, true, ["pt-BR"],
        "6-8 teclas para digitar em Braille. Conecta no smartphone. Cego digita codigo direto."),

    new HardwareDevice("HW-041", "Ponteiro Laser / Caneta Virtual",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
        [ConnectionType.BLUETOOTH],
        ["Windows", "Linux", "Android"],
        ["motora"],
        ["laser_point", "gesture"],
        [],
        8.0, true, ["pt-BR"],
        "Aponta laser na tela de longe. Para quem nao alcanca a tela ou tem tremor."),

    new HardwareDevice("HW-042", "Haptic Vest / Colete Tátil",
        HardwareCategory.WEARABLE, HardwareCost.HIGH, HardwareAvailability.EXPERIMENTAL,
        [ConnectionType.BLUETOOTH, ConnectionType.WIFI],
        ["Windows", "Linux", "Android"],
        ["visual", "auditiva", "motora"],
        [],
        ["haptic_array", "vibration_patterns_complex"],
        4.0, true, ["pt-BR"],
        "Vibracoes no corpo representam informacao. Surdo sente musica. Cego sente ambiente."),

    new HardwareDevice("HW-043", "Fone de Ouvido Comum",
        HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.UBIQUITOUS,
        [ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH],
        ["Standalone"],
        ["auditiva", "espectro_autista", "cognitiva"],
        ["microphone_optional"],
        ["audio", "audio_isolated"],
        0.0, true, ["pt-BR"],
        "Fone comum R$15. Para TTS (cego), isolamento (autista), audio direto (surdo com aparelho).")
];

// ============================================================================
// 4. MOTOR DE COMPATIBILIDADE
// ============================================================================

class HardwareCompatibilityEngine {
    constructor() {
        this.catalog = {};
        for (const d of HARDWARE_CATALOG) {
            this.catalog[d.device_id] = d;
        }
    }

    find_by_disability(disability_category) {
        return HARDWARE_CATALOG.filter(d => d.disabilities_served.includes(disability_category));
    }

    find_by_cost(max_cost) {
        const cost_order = [
            HardwareCost.FREE, HardwareCost.VERY_LOW, HardwareCost.LOW,
            HardwareCost.MEDIUM, HardwareCost.HIGH, HardwareCost.VERY_HIGH
        ];
        const max_idx = cost_order.indexOf(max_cost);
        return HARDWARE_CATALOG.filter(d => cost_order.indexOf(d.cost) <= max_idx);
    }

    find_by_platform(platform) {
        return HARDWARE_CATALOG.filter(d => d.platforms.includes(platform));
    }

    find_by_input_capability(capability) {
        return HARDWARE_CATALOG.filter(d => d.input_capabilities.includes(capability));
    }

    find_by_output_capability(capability) {
        return HARDWARE_CATALOG.filter(d => d.output_capabilities.includes(capability));
    }

    find_offline_capable() {
        return HARDWARE_CATALOG.filter(d => d.offline_capable);
    }

    recommend_setup(disabilities, budget = HardwareCost.LOW, platform = "Android") {
        const recommendations = new Set();
        for (const disability of disabilities) {
            for (const d of this.find_by_disability(disability)) {
                if (d.platforms.includes(platform) || d.platforms.length === 0) {
                    recommendations.add(d);
                }
            }
        }
        const budget_devices = this.find_by_cost(budget);
        let final = [...recommendations].filter(d => budget_devices.includes(d));
        if (final.length === 0) {
            final = [...this.find_by_cost(HardwareCost.FREE), ...this.find_by_cost(HardwareCost.VERY_LOW)];
        }
        return [...new Set(final)];
    }

    total_setup_cost(devices) {
        const cost_ranges = {
            [HardwareCost.FREE]: [0, 0],
            [HardwareCost.VERY_LOW]: [1, 100],
            [HardwareCost.LOW]: [100, 500],
            [HardwareCost.MEDIUM]: [500, 2000],
            [HardwareCost.HIGH]: [2000, 10000],
            [HardwareCost.VERY_HIGH]: [10000, 100000],
            [HardwareCost.SUBSIDIZED]: [0, 0]
        };
        let min_total = 0, max_total = 0;
        const categories = new Set();
        for (const d of devices) {
            const [lo, hi] = cost_ranges[d.cost];
            min_total += lo;
            max_total += hi;
            categories.add(d.category);
        }
        return {
            min_brl: min_total,
            max_brl: max_total,
            device_count: devices.length,
            categories: [...categories]
        };
    }
}

// ============================================================================
// 5. BRIDGE IDE <-> HARDWARE
// ============================================================================

class HardwareBridge {
    constructor() {
        this.connected_devices = [];
        this.engine = new HardwareCompatibilityEngine();
        this.active_inputs = [];
        this.active_outputs = [];
    }

    detect_devices() {
        const base = this.engine.catalog["HW-001"];
        if (base) {
            this.connected_devices = [base];
            this._update_capabilities();
        }
        return this.connected_devices;
    }

    connect_device(device) {
        if (!this.connected_devices.includes(device)) {
            this.connected_devices.push(device);
            this._update_capabilities();
        }
        return true;
    }

    disconnect_device(device) {
        const idx = this.connected_devices.indexOf(device);
        if (idx !== -1) {
            this.connected_devices.splice(idx, 1);
            this._update_capabilities();
        }
        return true;
    }

    _update_capabilities() {
        this.active_inputs = [];
        this.active_outputs = [];
        for (const d of this.connected_devices) {
            for (const cap of d.input_capabilities) {
                if (!this.active_inputs.includes(cap)) this.active_inputs.push(cap);
            }
            for (const cap of d.output_capabilities) {
                if (!this.active_outputs.includes(cap)) this.active_outputs.push(cap);
            }
        }
    }

    available_input_modes() {
        const modes = new Set();
        for (const d of this.connected_devices) {
            if (d.input_capabilities.includes("voice") || d.input_capabilities.includes("microphone")) {
                modes.add("voz"); modes.add("voz_codigo");
            }
            if (d.input_capabilities.includes("touch") || d.input_capabilities.includes("touch_small")) {
                modes.add("toque");
            }
            if (d.input_capabilities.includes("keyboard")) modes.add("teclado_completo");
            if (d.input_capabilities.includes("braille_keys") || d.input_capabilities.includes("braille_input_6_keys")) {
                modes.add("teclado_braille");
            }
            if (d.input_capabilities.includes("eye_gaze")) modes.add("rastreio_olhos");
            if (d.input_capabilities.includes("single_switch") || d.input_capabilities.includes("dual_switch")) {
                modes.add("chave"); modes.add("chave_dupla");
            }
            if (d.input_capabilities.includes("trackball")) modes.add("trackball");
            if (d.input_capabilities.includes("foot_press_left")) modes.add("pedal_pe");
            if (d.input_capabilities.includes("head_stick")) modes.add("teclado_cabeca");
            if (d.input_capabilities.includes("sip_puff")) modes.add("teclado_boca");
            if (d.input_capabilities.includes("eeg_waves") || d.input_capabilities.includes("neural_spikes")) {
                modes.add("interface_cerebral");
            }
            if (d.input_capabilities.includes("emg_signal")) modes.add("eletromiografo");
            if (d.input_capabilities.includes("hand_tracking")) modes.add("gesto");
            if (d.input_capabilities.includes("heart_rate")) modes.add("biofeedback");
        }
        return [...modes].sort();
    }

    available_output_modes() {
        const modes = new Set();
        for (const d of this.connected_devices) {
            if (d.output_capabilities.includes("screen") || d.output_capabilities.includes("screen_large")) {
                modes.add("texto_visual");
            }
            if (d.output_capabilities.includes("screen_tiny")) modes.add("texto_tela_pequena");
            if (d.output_capabilities.includes("tts") || d.output_capabilities.includes("tts_basic") || d.output_capabilities.includes("speaker")) {
                modes.add("texto_para_voz");
            }
            if (d.output_capabilities.includes("braille_cells_40") || d.output_capabilities.includes("braille_cells_14")) {
                modes.add("display_braille");
            }
            if (d.output_capabilities.includes("vibration") || d.output_capabilities.includes("haptic")) {
                modes.add("haptico");
            }
            if (d.output_capabilities.includes("color_light")) modes.add("luz_cor");
            if (d.output_capabilities.includes("audio_amplified")) modes.add("audio_amplificado");
            if (d.output_capabilities.includes("audio_anc")) modes.add("audio_cancelamento_ruido");
            if (d.output_capabilities.includes("hud_overlay")) modes.add("hud_oculos");
            if (d.output_capabilities.includes("taptic_engine")) modes.add("taptic_preciso");
        }
        return [...modes].sort();
    }

    supports_input_mode(mode) {
        return this.available_input_modes().includes(mode);
    }

    supports_output_mode(mode) {
        return this.available_output_modes().includes(mode);
    }

    session_info() {
        return {
            connected_devices: this.connected_devices.map(d => d.name),
            device_count: this.connected_devices.length,
            available_inputs: this.available_input_modes(),
            available_outputs: this.available_output_modes(),
            total_input_capabilities: this.active_inputs.length,
            total_output_capabilities: this.active_outputs.length
        };
    }
}

// ============================================================================
// 6. PERFIS DE SETUP
// ============================================================================

function create_setup_budget() {
    const engine = new HardwareCompatibilityEngine();
    return [engine.catalog["HW-001"], engine.catalog["HC-029"], engine.catalog["HW-018"]];
}

function create_setup_blind() {
    const engine = new HardwareCompatibilityEngine();
    return [engine.catalog["HW-001"], engine.catalog["HW-014"], engine.catalog["HW-013"], engine.catalog["HW-040"]];
}

function create_setup_deaf() {
    const engine = new HardwareCompatibilityEngine();
    return [engine.catalog["HW-001"], engine.catalog["HW-006"], engine.catalog["HC-031"]];
}

function create_setup_motor_severe() {
    const engine = new HardwareCompatibilityEngine();
    return [engine.catalog["HW-011"], engine.catalog["HW-016"], engine.catalog["HW-038"]];
}

function create_setup_autism() {
    const engine = new HardwareCompatibilityEngine();
    return [engine.catalog["HW-001"], engine.catalog["HC-029"], engine.catalog["HC-031"], engine.catalog["HC-032"]];
}

function create_setup_adhd() {
    const engine = new HardwareCompatibilityEngine();
    return [engine.catalog["HW-001"], engine.catalog["HC-029"], engine.catalog["HW-007"]];
}

function create_setup_epilepsy() {
    const engine = new HardwareCompatibilityEngine();
    return [engine.catalog["HW-001"], engine.catalog["HC-031"], engine.catalog["HW-007"]];
}

function create_setup_public_terminal() {
    const engine = new HardwareCompatibilityEngine();
    return [engine.catalog["HW-037"]];
}

function create_setup_zero_cost() {
    const engine = new HardwareCompatibilityEngine();
    return [engine.catalog["HW-037"], engine.catalog["HW-014"]];
}

// ============================================================================
// 7. ESCADA DE ESCALABILIDADE
// ============================================================================

class HardwareEscalationLadder {
    static RUNGS = [
        ["Degrau 0: ZERO CUSTO", "create_setup_zero_cost", "Biblioteca publica + NVDA gratis. Todo mundo comeca aqui."],
        ["Degrau 1: SMARTPHONE", "create_setup_budget", "Smartphone R$300 + fone R$50 + switch R$30. Acesse de qualquer lugar."],
        ["Degrau 2: TABLET/WEARABLE", "create_setup_deaf", "Adiciona smartwatch/luz para feedback multimodal."],
        ["Degrau 3: ASSISTIVO ESPECIFICO", "create_setup_blind", "Adiciona braille/eye-tracker especifico para deficiencia."],
        ["Degrau 4: SETUP COMPLETO", "create_setup_motor_severe", "Notebook + eye-tracker + microfone. Desenvolvimento profissional."],
        ["Degrau 5: BCI/EXPERIMENTAL", null, "BCI, haptic vest, smart glasses. Fronteira da tecnologia."]
    ];

    static recommend_rung(budget) {
        if (budget === HardwareCost.FREE) return [0, HardwareEscalationLadder.RUNGS[0][2]];
        if (budget === HardwareCost.VERY_LOW || budget === HardwareCost.LOW) return [1, HardwareEscalationLadder.RUNGS[1][2]];
        if (budget === HardwareCost.MEDIUM) return [2, HardwareEscalationLadder.RUNGS[2][2]];
        if (budget === HardwareCost.HIGH) return [3, HardwareEscalationLadder.RUNGS[3][2]];
        if (budget === HardwareCost.VERY_HIGH) return [5, HardwareEscalationLadder.RUNGS[5][2]];
        return [0, HardwareEscalationLadder.RUNGS[0][2]];
    }

    static show_ladder() {
        console.log("\nESCALADA DE HARDWARE -- Do Zero ao Profissional");
        console.log("=".repeat(60));
        for (const rung of HardwareEscalationLadder.RUNGS) {
            console.log(`\n  ${rung[0]}`);
            console.log(`    ${rung[2]}`);
        }
    }
}

// ============================================================================
// 8. DEMONSTRACAO (demo)
// ============================================================================

function demo() {
    console.log("=".repeat(70));
    console.log("OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel");
    console.log("=".repeat(70));

    const engine = new HardwareCompatibilityEngine();

    console.log(`\nCatalogo: ${HARDWARE_CATALOG.length} dispositivos mapeados`);
    const cats = {};
    for (const d of HARDWARE_CATALOG) {
        cats[d.category] = (cats[d.category] || 0) + 1;
    }
    for (const [cat, count] of Object.entries(cats).sort()) {
        console.log(`  ${cat.padEnd(25)} ${count.toString().padStart(3)} dispositivos`);
    }

    console.log("\nPor custo:");
    const costs = {};
    for (const d of HARDWARE_CATALOG) {
        costs[d.cost] = (costs[d.cost] || 0) + 1;
    }
    for (const [cost, count] of Object.entries(costs).sort()) {
        console.log(`  ${cost.padEnd(15)} ${count.toString().padStart(3)} dispositivos`);
    }

    console.log("\nPor disponibilidade:");
    const avail = {};
    for (const d of HARDWARE_CATALOG) {
        avail[d.availability] = (avail[d.availability] || 0) + 1;
    }
    for (const [a, count] of Object.entries(avail).sort()) {
        console.log(`  ${a.padEnd(15)} ${count.toString().padStart(3)} dispositivos`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("HARDWARE BRIDGE -- Deteccao e Configuracao");
    console.log("=".repeat(70));

    const bridge = new HardwareBridge();
    const detected = bridge.detect_devices();
    console.log(`\nDispositivos detectados: ${detected.map(d => d.name)}`);
    let info = bridge.session_info();
    console.log(`Inputs disponiveis:  ${info.available_inputs}`);
    console.log(`Outputs disponiveis: ${info.available_outputs}`);

    console.log("\n+ Conectando Display Braille...");
    bridge.connect_device(engine.catalog["HW-013"]);
    info = bridge.session_info();
    console.log(`Inputs:  ${info.available_inputs}`);
    console.log(`Outputs: ${info.available_outputs}`);

    console.log("\n+ Conectando Eye Tracker...");
    bridge.connect_device(engine.catalog["HW-016"]);
    info = bridge.session_info();
    console.log(`Inputs:  ${info.available_inputs}`);
    console.log(`Outputs: ${info.available_outputs}`);

    console.log("\n+ Conectando Smartwatch...");
    bridge.connect_device(engine.catalog["HW-006"]);
    info = bridge.session_info();
    console.log(`Inputs:  ${info.available_inputs}`);
    console.log(`Outputs: ${info.available_outputs}`);

    console.log("\n" + "=".repeat(70));
    console.log("PERFIS DE SETUP");
    console.log("=".repeat(70));

    const setups = {
        "ZERO CUSTO (biblioteca)": create_setup_zero_cost(),
        "BAIXO CUSTO (smartphone)": create_setup_budget(),
        "CEGO (braille completo)": create_setup_blind(),
        "SURDO (visual+haptic)": create_setup_deaf(),
        "TETRAPLEGICO (eye+voz)": create_setup_motor_severe(),
        "AUTISTA (calmo)": create_setup_autism(),
        "TDAH (foco)": create_setup_adhd(),
        "EPILEPSIA (seguro)": create_setup_epilepsy(),
        "TERMINAL PUBLICO": create_setup_public_terminal()
    };

    for (const [label, setup] of Object.entries(setups)) {
        const cost = engine.total_setup_cost(setup);
        console.log(`\n  ${label}`);
        console.log(`    Devices: ${cost.device_count} | Custo: R$ ${cost.min_brl}-${cost.max_brl}`);
        for (const d of setup) {
            console.log(`      - ${d.name}`);
        }
    }

    HardwareEscalationLadder.show_ladder();

    console.log("\n" + "=".repeat(70));
    console.log("COBERTURA DE CATEGORIAS");
    console.log("=".repeat(70));
    for (const cat of Object.values(HardwareCategory)) {
        const count = HARDWARE_CATALOG.filter(d => d.category === cat).length;
        console.log(`  ${cat.padEnd(25)} ${count.toString().padStart(3)} dispositivos`);
    }

    console.log("\nCOBERTURA POR DEFICIENCIA:");
    const all_disabilities = new Set();
    for (const d of HARDWARE_CATALOG) {
        for (const dis of d.disabilities_served) all_disabilities.add(dis);
    }
    for (const disab of [...all_disabilities].sort()) {
        const count = engine.find_by_disability(disab).length;
        console.log(`  ${disab.padEnd(25)} ${count.toString().padStart(3)} dispositivos`);
    }

    console.log(`\nTotal dispositivos: ${HARDWARE_CATALOG.length}`);
    console.log(`Categorias: ${Object.keys(HardwareCategory).length}`);
    console.log("Setup minimo: R$ 0 (biblioteca + NVDA gratis)");
    console.log("\nTODO hardware. TODA deficiencia. ZERO barreira.");
}

if (require.main === module) {
    demo();
}

module.exports = {
    HardwareCategory, HardwareCost, HardwareAvailability, ConnectionType,
    HardwareDevice, HARDWARE_CATALOG, HardwareCompatibilityEngine,
    HardwareBridge, create_setup_budget, create_setup_blind, create_setup_deaf,
    create_setup_motor_severe, create_setup_autism, create_setup_adhd,
    create_setup_epilepsy, create_setup_public_terminal, create_setup_zero_cost,
    HardwareEscalationLadder, demo
};