// OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel
// =================================================================
// "O hardware certo transforma uma deficiencia em uma capacidade.
// O cego tem o smartphone como olhos. O surdo tem o smartwatch como ouvidos.
// O tetraplegico tem o eye-tracker como maos. O autista tem o fone como escudo.
// A IDE nao escolhe o hardware. O HARDWARE DO USUARIO escolhe a IDE.
// Se a pessoa tem um smartphone Android de R$300, a IDE funciona.
// Se a pessoa tem um SmartWatch, a IDE funciona.
// Se a pessoa tem um eye-tracker de R$15.000, a IDE funciona.
// Se a pessoa NAO TEM NADA, a IDE funciona no terminal publico (OpenTerminal).
// ZERO barreira de hardware. ZERO custo de entrada. MAXIMA adaptacao.
// Integrado com:
// - OpenInclusiveIDE (IDE se adapta ao hardware disponivel)
// - OpenTerminal (todo terminal publico roda a IDE)
// - OpenAbsence (hardware respeita pausas)
// - OpenBodilyAutonomy (usuario controla seu dispositivo)
// - OpenSilencePolicy (dispositivos respeitam o silencio)
// HARDWARE MAPEADO (6 CATEGORIAS, 44 DISPOSITIVOS):
// 1. MASSA (smartphone, tablet, smartwatch, notebook, desktop)
// 2. ASSISTIVO VISUAL (leitor de tela, display braille, lupa eletronica)
// 3. ASSISTIVO MOTOR (eye-tracker, switch, teclado especial, BCI)
// 4. ASSISTIVO AUDITIVO (implante coclear, aparelho auditivo, loop)
// 5. ASSISTIVO COGNITIVO (fone ANC, luz inteligente, weighted blanket)
// 6. TERMINAL PUBLICO (TV, kiosk, terminal burro, computador comunitario)
// PRINCIPIO CHAVE: O hardware NAO define o desenvolvedor.
// O desenvolvedor define o hardware. A IDE se adapta.
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// ============================================================================
// 1. CATEGORIAS DE HARDWARE
// ============================================================================
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
enum HardwareCategory {
    MASS,              // smartphone, tablet, smartwatch, notebook
    ASSISTIVE_VISUAL,  // leitor de tela, braille, lupa
    ASSISTIVE_MOTOR,   // eye-tracker, switch, BCI
    ASSISTIVE_AUDITORY, // implante coclear, loop
    ASSISTIVE_COGNITIVE, // fone ANC, luz, blanket
    TERMINAL_PUBLIC,   // TV, kiosk, terminal burro
    WEARABLE,          // smartwatch, anel smart, Oculus
    BRAIN,             // BCI, EEG, Neuralink
}

#[derive(Debug, Clone, PartialEq, Eq, Hash, Copy)]
enum HardwareCost {
    FREE,        // gratis (terminal publico, biblioteca)
    VERY_LOW,    // < R$ 100 (fone simples, switch DIY)
    LOW,         // R$ 100-500 (smartphone basico)
    MEDIUM,      // R$ 500-2000 (tablet, smartwatch)
    HIGH,        // R$ 2000-10000 (eye-tracker, braille)
    VERY_HIGH,   // > R$ 10000 (BCI, implante coclear)
    SUBSIDIZED,  // governo/seguro cobre
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
enum HardwareAvailability {
    UBIQUITOUS,   // em qualquer lugar (smartphone)
    COMMON,       // lojas comuns (tablet, smartwatch)
    SPECIALIZED,  // lojas de acessibilidade
    MEDICAL,      // prescricao medica (implante)
    RARE,         // importacao, poucos fornecedores
    EXPERIMENTAL, // pesquisa, ainda nao comercial
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
enum ConnectionType {
    BLUETOOTH,
    USB,
    WIFI,
    NFC,
    CLOUD,
    AUDIO_JACK,
    PROPRIETARY,
    WIRELESS,
    HDMI,
}

// ============================================================================
// 2. PERFIL DE HARDWARE
// ============================================================================
#[derive(Debug, Clone)]
struct HardwareDevice {
    device_id: String,
    name: String,
    category: HardwareCategory,
    cost: HardwareCost,
    availability: HardwareAvailability,
    connections: Vec<ConnectionType>,
    platforms: Vec<String>,
    disabilities_served: Vec<String>,
    input_capabilities: Vec<String>,
    output_capabilities: Vec<String>,
    battery_hours: f64,
    offline_capable: bool,
    languages_supported: Vec<String>,
    description: String,
}

impl HardwareDevice {
    fn new(
        device_id: &str,
        name: &str,
        category: HardwareCategory,
        cost: HardwareCost,
        availability: HardwareAvailability,
        connections: Vec<ConnectionType>,
        platforms: Vec<&str>,
        disabilities_served: Vec<&str>,
        input_capabilities: Vec<&str>,
        output_capabilities: Vec<&str>,
        battery_hours: f64,
        offline_capable: bool,
        description: &str,
    ) -> Self {
        HardwareDevice {
            device_id: device_id.to_string(),
            name: name.to_string(),
            category,
            cost,
            availability,
            connections,
            platforms: platforms.into_iter().map(|s| s.to_string()).collect(),
            disabilities_served: disabilities_served.into_iter().map(|s| s.to_string()).collect(),
            input_capabilities: input_capabilities.into_iter().map(|s| s.to_string()).collect(),
            output_capabilities: output_capabilities.into_iter().map(|s| s.to_string()).collect(),
            battery_hours,
            offline_capable,
            languages_supported: vec!["pt-BR".to_string()],
            description: description.to_string(),
        }
    }
}

// ============================================================================
// 3. CATALOGO DE HARDWARE (44 DISPOSITIVOS)
// ============================================================================
static HARDWARE_CATALOG: &[HardwareDevice] = &[
    // === SMARTPHONE (massa) ===
    HardwareDevice::new("HW-001", "Smartphone Android (qualquer)",
        HardwareCategory::MASS, HardwareCost::LOW, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB, ConnectionType::WIFI, ConnectionType::NFC, ConnectionType::AUDIO_JACK],
        vec!["Android"],
        vec!["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "multipla", "temporaria"],
        vec!["touch", "voice", "camera", "microphone", "bluetooth_keyboard", "nfc", "accelerometer", "gyroscope"],
        vec!["screen", "speaker", "vibration", "flash_led", "screen_reader"],
        12.0, true,
        "O dispositivo mais inclusivo do planeta. TalkBack, Voice Access, Switch Access nativos."),
    HardwareDevice::new("HW-002", "iPhone (qualquer)",
        HardwareCategory::MASS, HardwareCost::MEDIUM, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB, ConnectionType::WIFI, ConnectionType::NFC],
        vec!["iOS"],
        vec!["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "multipla", "temporaria"],
        vec!["touch", "voice", "face_id", "camera", "microphone", "bluetooth_keyboard", "lidar"],
        vec!["screen", "speaker", "vibration", "taptic_engine", "voiceover", "flash_led"],
        15.0, true,
        "VoiceOver, Switch Control, Voice Control, Sound Detection nativos. Lidar para deteccao de obstaculos."),
    HardwareDevice::new("HW-003", "Smartphone basico (teclado fisico)",
        HardwareCategory::MASS, HardwareCost::VERY_LOW, HardwareAvailability::COMMON,
        vec![ConnectionType::AUDIO_JACK, ConnectionType::BLUETOOTH],
        vec!["KaiOS", "Feature Phone"],
        vec!["visual", "motora", "temporaria"],
        vec!["keypad", "voice", "microphone"],
        vec!["screen_small", "speaker", "vibration", "tts_basic"],
        72.0, true,
        "Telefone botoeiro com TTS. Para quem nao tem smartphone ou prefere teclado fisico."),
    // === TABLET ===
    HardwareDevice::new("HW-004", "Tablet Android",
        HardwareCategory::MASS, HardwareCost::MEDIUM, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB, ConnectionType::WIFI],
        vec!["Android"],
        vec!["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento"],
        vec!["touch", "voice", "camera", "microphone", "stylus", "bluetooth_keyboard"],
        vec!["screen_large", "speaker", "vibration"],
        10.0, true,
        "Tela maior = mais area para botoes grandes, blocos visuais, zoom."),
    HardwareDevice::new("HW-005", "iPad",
        HardwareCategory::MASS, HardwareCost::MEDIUM, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB, ConnectionType::WIFI],
        vec!["iPadOS"],
        vec!["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento"],
        vec!["touch", "voice", "face_id", "camera", "microphone", "stylus_pencil", "lidar"],
        vec!["screen_large", "speaker", "taptic_engine", "voiceover"],
        10.0, true,
        "Apple Pencil para deteccao de tremores. AssistiveTouch. Full Keyboard Control."),
    // === SMARTWATCH / WEARABLE ===
    HardwareDevice::new("HW-006", "Smartwatch Android (WearOS)",
        HardwareCategory::WEARABLE, HardwareCost::MEDIUM, HardwareAvailability::COMMON,
        vec![ConnectionType::BLUETOOTH, ConnectionType::WIFI],
        vec!["WearOS"],
        vec!["auditiva", "motora", "cognitiva", "temporaria"],
        vec!["touch_small", "voice", "microphone", "accelerometer", "heart_rate", "gestures", "crown"],
        vec!["screen_tiny", "vibration", "speaker_tiny", "haptic"],
        24.0, true,
        "Vibracao no pulso para alertas (surdez). Monitor de batimento (epilepsia/ansiedade). Coroa para navegacao (motor)."),
    HardwareDevice::new("HW-007", "Apple Watch",
        HardwareCategory::WEARABLE, HardwareCost::MEDIUM, HardwareAvailability::COMMON,
        vec![ConnectionType::BLUETOOTH, ConnectionType::WIFI],
        vec!["watchOS"],
        vec!["auditiva", "motora", "cognitiva", "temporaria", "neurologica"],
        vec!["touch_small", "voice", "microphone", "crown_digital", "accelerometer", "heart_rate", "ecg", "fall_detection", "gestures", "sip_pinch"],
        vec!["screen_tiny", "taptic_engine", "speaker_tiny", "haptic"],
        18.0, true,
        "Fall Detection (queda). ECG (coracao). Taptic Engine para surdos. AssistiveTouch (pinca/sorvo para tetraplegia). Noise app (autismo)."),
    HardwareDevice::new("HW-008", "Smartwatch basico / Pulseira fitness",
        HardwareCategory::WEARABLE, HardwareCost::LOW, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::BLUETOOTH],
        vec!["Proprietary"],
        vec!["auditiva", "temporaria"],
        vec!["touch_tiny", "accelerometer", "heart_rate"],
        vec!["screen_tiny", "vibration"],
        168.0, true,
        "R$80-200. Vibracao para notificacoes (surdez). Monitor basico de sono/atividade."),
    HardwareDevice::new("HW-009", "Anel Smart (Smart Ring)",
        HardwareCategory::WEARABLE, HardwareCost::MEDIUM, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::BLUETOOTH],
        vec!["Proprietary"],
        vec!["auditiva", "neurologica"],
        vec!["accelerometer", "heart_rate", "temperature", "spO2"],
        vec!["vibration_tiny", "led"],
        168.0, true,
        "Discreto. Monitor de sono, temperatura, SpO2. Para autismo: biofeedback discreto."),
    HardwareDevice::new("HW-010", "Oculos Inteligentes (Smart Glasses)",
        HardwareCategory::WEARABLE, HardwareCost::HIGH, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::BLUETOOTH, ConnectionType::WIFI],
        vec!["Android", "Proprietary"],
        vec!["visual", "auditiva", "motora", "neurologica"],
        vec!["voice", "camera", "microphone", "bone_conduction_audio", "head_tracking", "eye_tracking_basic"],
        vec!["hud_overlay", "bone_conduction_speaker", "vibration"],
        6.0, true,
        "Legendas em tempo real no campo de visao (surdez). Navegacao por setas (cegueira). Heads-up display."),
    // === COMPUTADOR / NOTEBOOK ===
    HardwareDevice::new("HW-011", "Notebook / Laptop",
        HardwareCategory::MASS, HardwareCost::MEDIUM, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB, ConnectionType::WIFI, ConnectionType::AUDIO_JACK],
        vec!["Linux", "Windows", "macOS"],
        vec!["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "neurologica", "multipla", "temporaria"],
        vec!["keyboard", "trackpad", "microphone", "camera", "bluetooth_devices"],
        vec!["screen", "speaker", "vibration_rare"],
        8.0, true,
        "Plataforma de desenvolvimento completa. Screen readers, IDEs, eye-tracking via USB."),
    HardwareDevice::new("HW-012", "Desktop / PC",
        HardwareCategory::MASS, HardwareCost::MEDIUM, HardwareAvailability::COMMON,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB, ConnectionType::WIFI, ConnectionType::AUDIO_JACK],
        vec!["Linux", "Windows"],
        vec!["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "neurologica", "multipla"],
        vec!["keyboard", "mouse", "microphone", "camera", "usb_devices", "pcie_cards"],
        vec!["screen_large", "speaker", "multi_monitor"],
        0.0, true,
        "Maximo de conectividade. Multi-tela, GPUs para IA, todo tipo de periferico."),
    // === LEITOR DE TELA / DISPLAY BRAILLE ===
    HardwareDevice::new("HW-013", "Display Braille (linha braille)",
        HardwareCategory::ASSISTIVE_VISUAL, HardwareCost::HIGH, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB],
        vec!["Android", "iOS", "Linux", "Windows", "macOS"],
        vec!["visual"],
        vec!["braille_keys", "routing_buttons", "navigation"],
        vec!["braille_cells_40", "braille_cells_80"],
        20.0, true,
        "40-80 celulas braille. Celulas piezoeletricas que sobem e descem. Cego le codigo tateando."),
    HardwareDevice::new("HW-013b", "Display Braille portatil (14-20 celulas)",
        HardwareCategory::ASSISTIVE_VISUAL, HardwareCost::MEDIUM, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB],
        vec!["Android", "iOS"],
        vec!["visual"],
        vec!["braille_keys"],
        vec!["braille_cells_14"],
        20.0, true,
        "Versao portatil menor. Cabe no bolso. Conecta no smartphone."),
    HardwareDevice::new("HW-014", "Leitor de tela software (NVDA, Orca, VoiceOver, TalkBack)",
        HardwareCategory::ASSISTIVE_VISUAL, HardwareCost::FREE, HardwareAvailability::UBIQUITOUS,
        vec![],
        vec!["Android", "iOS", "Linux", "Windows", "macOS"],
        vec!["visual"],
        vec![],
        vec!["tts", "braille_output", "audio_cues"],
        0.0, true,
        "NVDA (gratis, Windows). Orca (Linux). VoiceOver (Apple). TalkBack (Android). Converte tela em voz/braille."),
    HardwareDevice::new("HW-015", "Lupa eletronica / CCTV",
        HardwareCategory::ASSISTIVE_VISUAL, HardwareCost::MEDIUM, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::HDMI],
        vec!["Standalone"],
        vec!["visual"],
        vec!["camera_zoom"],
        vec!["screen_zoomed"],
        4.0, true,
        "Camera que amplia texto/papel para tela. Para baixa visao."),
    // === EYE TRACKER / SWITCH / MOTOR ===
    HardwareDevice::new("HW-016", "Eye Tracker (Tobii, EyeX)",
        HardwareCategory::ASSISTIVE_MOTOR, HardwareCost::HIGH, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::USB, ConnectionType::WIFI],
        vec!["Windows", "Linux"],
        vec!["motora", "multipla"],
        vec!["eye_gaze", "dwell_selection", "blink"],
        vec![],
        0.0, true,
        "Camera infravermelha rastreia olhos. Tetraplegia, ELA, paralisia cerebral. Custo: R$2.000-8.000."),
    HardwareDevice::new("HW-017", "Eye Tracker portatil (smartphone)",
        HardwareCategory::ASSISTIVE_MOTOR, HardwareCost::MEDIUM, HardwareAvailability::SPECIALIZED,
        vec![],
        vec!["Android", "iOS"],
        vec!["motora", "multipla"],
        vec!["eye_gaze_front_camera"],
        vec![],
        6.0, true,
        "Usa camera frontal do smartphone para rastrear olhos. Precisao menor mas gratuito com app."),
    HardwareDevice::new("HW-018", "Switch / Botao adaptativo",
        HardwareCategory::ASSISTIVE_MOTOR, HardwareCost::VERY_LOW, HardwareAvailability::COMMON,
        vec![ConnectionType::BLUETOOTH, ConnectionType::AUDIO_JACK, ConnectionType::USB],
        vec!["Android", "iOS", "Windows", "Linux", "macOS"],
        vec!["motora", "multipla", "desenvolvimento"],
        vec!["single_switch", "dual_switch"],
        vec![],
        0.0, true,
        "Um ou dois botoes grandes. Scan automatico passa opcoes, usuario aciona para selecionar. DIY possivel por R$20."),
    HardwareDevice::new("HW-019", "Teclado adaptativo grande",
        HardwareCategory::ASSISTIVE_MOTOR, HardwareCost::LOW, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB],
        vec!["Android", "iOS", "Windows", "Linux", "macOS"],
        vec!["motora", "cognitiva", "desenvolvimento"],
        vec!["large_keys", "color_coded"],
        vec![],
        0.0, true,
        "Teclas 3x maiores, coloridas, com guard de mao. Para tremores, baixa destreza, Down."),
    HardwareDevice::new("HW-020", "Teclado de cabeca / boca",
        HardwareCategory::ASSISTIVE_MOTOR, HardwareCost::LOW, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::USB, ConnectionType::BLUETOOTH],
        vec!["Windows", "Linux", "Android"],
        vec!["motora"],
        vec!["head_stick", "mouth_stick", "sip_puff"],
        vec![],
        0.0, true,
        "Ponteiro de cabeca ou bocal para digitar em teclado na tela. Sip-and-puff = sopro/succao."),
    HardwareDevice::new("HW-021", "Trackball adaptativo",
        HardwareCategory::ASSISTIVE_MOTOR, HardwareCost::LOW, HardwareAvailability::COMMON,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB],
        vec!["Windows", "Linux", "macOS", "Android"],
        vec!["motora"],
        vec!["trackball", "large_ball"],
        vec![],
        0.0, true,
        "Bola grande movida com palma/queixo/dorso do pe. Estavel para tremores (Parkinson)."),
    HardwareDevice::new("HW-022", "Pedal de pe (Foot Pedal)",
        HardwareCategory::ASSISTIVE_MOTOR, HardwareCost::VERY_LOW, HardwareAvailability::COMMON,
        vec![ConnectionType::USB, ConnectionType::BLUETOOTH],
        vec!["Windows", "Linux", "macOS"],
        vec!["motora", "temporaria"],
        vec!["foot_press_left", "foot_press_right", "foot_press_center"],
        vec![],
        0.0, true,
        "Para quem tem uso dos pes mas nao das maos. 3 pedais = 3 botoes. R$50-150."),
    HardwareDevice::new("HW-023", "EMG / MIODOELETRICO (braco bio-feedback)",
        HardwareCategory::ASSISTIVE_MOTOR, HardwareCost::MEDIUM, HardwareAvailability::EXPERIMENTAL,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB],
        vec!["Windows", "Linux", "Android"],
        vec!["motora", "multipla"],
        vec!["emg_signal", "muscle_activation"],
        vec![],
        8.0, true,
        "Sensores no musculo. Detecta contracao muscular residual. Para amputados, paralisia parcial."),
    // === BCI / CEREBRAL ===
    HardwareDevice::new("HW-024", "BCI Invasivo (Neuralink/Synchron)",
        HardwareCategory::BRAIN, HardwareCost::VERY_HIGH, HardwareAvailability::EXPERIMENTAL,
        vec![ConnectionType::WIFI, ConnectionType::BLUETOOTH],
        vec!["Windows", "Linux"],
        vec!["motora", "multipla"],
        vec!["neural_spikes", "motor_intention"],
        vec![],
        0.0, true,
        "Eletrodos no cerebro. Tetraplegia profunda. Ainda em ensaios clinicos."),
    HardwareDevice::new("HW-025", "BCI Nao-Invasivo (EEG headset)",
        HardwareCategory::BRAIN, HardwareCost::MEDIUM, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB],
        vec!["Windows", "Linux", "Android"],
        vec!["motora", "multipla"],
        vec!["eeg_waves", "concentration_level", "blink_detect"],
        vec!["neurofeedback_display"],
        6.0, true,
        "Capacete com eletrodos. Le ondas cerebrais. Precisao baixa mas nao invasivo. R$500-3000."),
    // === AUDITIVO ===
    HardwareDevice::new("HC-026", "Aparelho Auditivo (digital)",
        HardwareCategory::ASSISTIVE_AUDITORY, HardwareCost::MEDIUM, HardwareAvailability::MEDICAL,
        vec![ConnectionType::BLUETOOTH],
        vec!["Standalone"],
        vec!["auditiva"],
        vec!["bluetooth_audio_in"],
        vec!["audio_amplified", "audio_filtered"],
        96.0, true,
        "Amplifica e filtra som. Bluetooth direto do smartphone. Programa SUS cobre."),
    HardwareDevice::new("HC-027", "Implante Coclear",
        HardwareCategory::ASSISTIVE_AUDITORY, HardwareCost::VERY_HIGH, HardwareAvailability::MEDICAL,
        vec![ConnectionType::BLUETOOTH],
        vec!["Standalone"],
        vec!["auditiva"],
        vec!["bluetooth_audio_in"],
        vec!["electrical_stimulation"],
        24.0, true,
        "Cirurgico. Eletrodos na coclea. Para surdez profunda. SUS cobre em alguns estados."),
    HardwareDevice::new("HC-028", "Loop Magnetico / Sistema FM",
        HardwareCategory::ASSISTIVE_AUDITORY, HardwareCost::LOW, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::AUDIO_JACK, ConnectionType::BLUETOOTH],
        vec!["Standalone"],
        vec!["auditiva"],
        vec!["audio_in"],
        vec!["magnetic_loop"],
        0.0, true,
        "Cabo de loop magnetico no pescoco. Transmite audio direto pro aparelho auditivo. Elimina ruido ambiente."),
    // === COGNITIVO / SENSORIAL ===
    HardwareDevice::new("HC-029", "Fone ANC (Active Noise Cancelling)",
        HardwareCategory::ASSISTIVE_COGNITIVE, HardwareCost::LOW, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::BLUETOOTH, ConnectionType::AUDIO_JACK],
        vec!["Standalone"],
        vec!["espectro_autista", "auditiva", "cognitiva"],
        vec!["anc_microphone"],
        vec!["audio_anc", "audio_filtered"],
        30.0, true,
        "Cancela ruido ambiente. ESCUDO SENSORIAL para autista/TDAH em ambiente ruidoso. R$100-500."),
    HardwareDevice::new("HC-030", "Fone com microfone direcional",
        HardwareCategory::ASSISTIVE_COGNITIVE, HardwareCost::LOW, HardwareAvailability::COMMON,
        vec![ConnectionType::BLUETOOTH, ConnectionType::AUDIO_JACK],
        vec!["Standalone"],
        vec!["auditiva", "espectro_autista"],
        vec!["directional_microphone"],
        vec!["audio_directed"],
        20.0, true,
        "Captura som da frente, cancela resto. Para APD (Processamento Auditivo) e autismo."),
    HardwareDevice::new("HC-031", "Luz Inteligente (Smart Bulb)",
        HardwareCategory::ASSISTIVE_COGNITIVE, HardwareCost::LOW, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::WIFI, ConnectionType::BLUETOOTH],
        vec!["Android", "iOS"],
        vec!["visual", "auditiva", "espectro_autista", "neurologica"],
        vec![],
        vec!["color_light", "brightness_control", "temperature_color", "no_flicker"],
        0.0, true,
        "Notificacao visual por cor (surdez). Luz quente para acalmar (autismo/epilepsia). Sem flicker."),
    HardwareDevice::new("HC-032", "Weighted Blanket (Manta Ponderada)",
        HardwareCategory::ASSISTIVE_COGNITIVE, HardwareCost::VERY_LOW, HardwareAvailability::COMMON,
        vec![],
        vec!["Physical"],
        vec!["espectro_autista", "cognitiva", "neurologica"],
        vec![],
        vec!["deep_pressure_stimulation"],
        0.0, true,
        "Pressao profunda calmante. Reduz ansiedade (autismo/TDAH). Melhora sono. R$100-300."),
    HardwareDevice::new("HC-033", "Bracelete Anti-Ansiedade / Vibratorio",
        HardwareCategory::WEARABLE, HardwareCost::VERY_LOW, HardwareAvailability::COMMON,
        vec![ConnectionType::BLUETOOTH],
        vec!["Android", "iOS"],
        vec!["espectro_autista", "cognitiva", "neurologica"],
        vec!["heart_rate", "skin_conductance"],
        vec!["vibration_patterns", "temperature_cooling"],
        72.0, true,
        "Vibracao para acalmar (biofeedback). Detecta crise de ansiedade por batimento. R$80-200."),
    // === TERMINAL PUBLICO ===
    HardwareDevice::new("HW-034", "TV Smart (qualquer)",
        HardwareCategory::TERMINAL_PUBLIC, HardwareCost::MEDIUM, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::WIFI, ConnectionType::HDMI, ConnectionType::BLUETOOTH],
        vec!["Android TV", "Tizen", "webOS"],
        vec!["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "temporaria"],
        vec!["remote", "voice", "bluetooth_keyboard", "camera_optional"],
        vec!["screen_huge", "speaker", "hdmi_out"],
        0.0, true,
        "Todo estabelecimento tem uma TV. OpenTerminal transforma TV ociosa em terminal da Republica."),
    HardwareDevice::new("HW-035", "Kiosk / Terminal Publico",
        HardwareCategory::TERMINAL_PUBLIC, HardwareCost::MEDIUM, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::WIFI, ConnectionType::USB],
        vec!["Linux", "Windows"],
        vec!["visual", "auditiva", "motora", "cognitiva", "multipla"],
        vec!["touch", "keypad", "nfc", "camera"],
        vec!["screen_large", "speaker"],
        0.0, true,
        "Terminal em praca, hospital, escola. wheelchair-height. Audio jack para fone."),
    HardwareDevice::new("HW-036", "Terminal Burro (Raspberry Pi + tela)",
        HardwareCategory::TERMINAL_PUBLIC, HardwareCost::VERY_LOW, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::WIFI, ConnectionType::USB, ConnectionType::AUDIO_JACK, ConnectionType::HDMI],
        vec!["Linux"],
        vec!["visual", "auditiva", "motora", "cognitiva"],
        vec!["keyboard", "usb_switch", "usb_eye_tracker", "bluetooth"],
        vec!["screen", "speaker", "audio_jack"],
        0.0, true,
        "Raspberry Pi R$150 + tela R$100 = terminal completo. OpenKit da Republica."),
    HardwareDevice::new("HW-037", "Computador Comunitario (biblioteca, escola)",
        HardwareCategory::TERMINAL_PUBLIC, HardwareCost::FREE, HardwareAvailability::COMMON,
        vec![ConnectionType::WIFI, ConnectionType::USB, ConnectionType::AUDIO_JACK],
        vec!["Linux", "Windows"],
        vec!["visual", "auditiva", "motora", "cognitiva", "multipla", "temporaria"],
        vec!["keyboard", "mouse", "microphone", "usb_devices"],
        vec!["screen", "speaker", "audio_jack"],
        0.0, true,
        "Zero custo. Disponivel em bibliotecas publicas, telecentros, escola publica."),
    // === VOZ ===
    HardwareDevice::new("HW-038", "Microfone (dedicado)",
        HardwareCategory::MASS, HardwareCost::VERY_LOW, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::USB, ConnectionType::AUDIO_JACK, ConnectionType::BLUETOOTH],
        vec!["Linux", "Windows", "macOS", "Android", "iOS"],
        vec!["motora", "comunicacao"],
        vec!["voice_high_quality", "noise_cancellation"],
        vec![],
        0.0, true,
        "Para dictacao de codigo por voz. Microfone de lapela R$30 = suficiente."),
    HardwareDevice::new("HW-039", "Camera Web (webcam)",
        HardwareCategory::MASS, HardwareCost::VERY_LOW, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::USB, ConnectionType::WIFI],
        vec!["Linux", "Windows", "macOS", "Android", "iOS"],
        vec!["motora", "comunicacao", "auditiva"],
        vec!["hand_tracking", "face_tracking", "eye_tracking_basic", "gesture", "sign_language_capture"],
        vec![],
        0.0, true,
        "Gestos de mao, tracking facial, captura de Libras. Webcam R$50 = suficiente."),
    // === INPUT ALTERNATIVO ===
    HardwareDevice::new("HW-040", "Teclado Braille (Perkins / eletronico)",
        HardwareCategory::ASSISTIVE_VISUAL, HardwareCost::MEDIUM, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::BLUETOOTH, ConnectionType::USB],
        vec!["Android", "iOS", "Windows", "Linux", "macOS"],
        vec!["visual"],
        vec!["braille_input_6_keys", "braille_input_8_keys", "space", "navigation"],
        vec![],
        20.0, true,
        "6-8 teclas para digitar em Braille. Conecta no smartphone. Cego digita codigo direto."),
    HardwareDevice::new("HW-041", "Ponteiro Laser / Caneta Virtual",
        HardwareCategory::ASSISTIVE_MOTOR, HardwareCost::LOW, HardwareAvailability::SPECIALIZED,
        vec![ConnectionType::BLUETOOTH],
        vec!["Windows", "Linux", "Android"],
        vec!["motora"],
        vec!["laser_point", "gesture"],
        vec![],
        8.0, true,
        "Aponta laser na tela de longe. Para quem nao alcanca a tela ou tem tremor."),
    HardwareDevice::new("HW-042", "Haptic Vest / Colete Tátil",
        HardwareCategory::WEARABLE, HardwareCost::HIGH, HardwareAvailability::EXPERIMENTAL,
        vec![ConnectionType::BLUETOOTH, ConnectionType::WIFI],
        vec!["Windows", "Linux", "Android"],
        vec!["visual", "auditiva", "motora"],
        vec![],
        vec!["haptic_array", "vibration_patterns_complex"],
        4.0, true,
        "Vibracoes no corpo representam informacao. Surdo sente musica. Cego sente ambiente."),
    HardwareDevice::new("HW-043", "Fone de Ouvido Comum",
        HardwareCategory::MASS, HardwareCost::VERY_LOW, HardwareAvailability::UBIQUITOUS,
        vec![ConnectionType::AUDIO_JACK, ConnectionType::BLUETOOTH],
        vec!["Standalone"],
        vec!["auditiva", "espectro_autista", "cognitiva"],
        vec!["microphone_optional"],
        vec!["audio", "audio_isolated"],
        0.0, true,
        "Fone comum R$15. Para TTS (cego), isolamento (autista), audio direto (surdo com aparelho)."),
];

// ============================================================================
// 4. MOTOR DE COMPATIBILIDADE
// ============================================================================
struct HardwareCompatibilityEngine {
    catalog: HashMap<String, &'static HardwareDevice>,
}

impl HardwareCompatibilityEngine {
    fn new() -> Self {
        let mut catalog = HashMap::new();
        for d in HARDWARE_CATALOG.iter() {
            catalog.insert(d.device_id.clone(), d);
        }
        HardwareCompatibilityEngine { catalog }
    }

    fn find_by_disability(&self, disability_category: &str) -> Vec<&'static HardwareDevice> {
        HARDWARE_CATALOG.iter().filter(|d| d.disabilities_served.iter().any(|s| s == disability_category)).collect()
    }

    fn find_by_cost(&self, max_cost: HardwareCost) -> Vec<&'static HardwareDevice> {
        let cost_order = vec![
            HardwareCost::FREE,
            HardwareCost::VERY_LOW,
            HardwareCost::LOW,
            HardwareCost::MEDIUM,
            HardwareCost::HIGH,
            HardwareCost::VERY_HIGH,
        ];
        let max_idx = cost_order.iter().position(|c| *c == max_cost).unwrap_or(0);
        HARDWARE_CATALOG.iter().filter(|d| {
            cost_order.iter().position(|c| *c == d.cost).unwrap_or(usize::MAX) <= max_idx
        }).collect()
    }

    fn find_by_platform(&self, platform: &str) -> Vec<&'static HardwareDevice> {
        HARDWARE_CATALOG.iter().filter(|d| d.platforms.iter().any(|p| p == platform)).collect()
    }

    fn find_by_input_capability(&self, capability: &str) -> Vec<&'static HardwareDevice> {
        HARDWARE_CATALOG.iter().filter(|d| d.input_capabilities.iter().any(|c| c == capability)).collect()
    }

    fn find_by_output_capability(&self, capability: &str) -> Vec<&'static HardwareDevice> {
        HARDWARE_CATALOG.iter().filter(|d| d.output_capabilities.iter().any(|c| c == capability)).collect()
    }

    fn find_offline_capable(&self) -> Vec<&'static HardwareDevice> {
        HARDWARE_CATALOG.iter().filter(|d| d.offline_capable).collect()
    }

    fn recommend_setup(&self, disabilities: Vec<&str>, budget: HardwareCost, platform: &str) -> Vec<&'static HardwareDevice> {
        let mut recommendations: HashSet<&'static HardwareDevice> = HashSet::new();
        for disability in disabilities {
            for d in self.find_by_disability(disability) {
                if d.platforms.iter().any(|p| p == platform) || d.platforms.is_empty() {
                    recommendations.insert(d);
                }
            }
        }
        let budget_devices = self.find_by_cost(budget);
        let mut final_recs: Vec<_> = recommendations.into_iter().filter(|d| budget_devices.iter().any(|b| std::ptr::eq(*d, *b))).collect();
        if final_recs.is_empty() {
            final_recs = self.find_by_cost(HardwareCost::FREE);
            final_recs.extend(self.find_by_cost(HardwareCost::VERY_LOW));
        }
        final_recs
    }

    fn total_setup_cost(&self, devices: &[&HardwareDevice]) -> HashMap<String, String> {
        let cost_ranges: HashMap<HardwareCost, (i64, i64)> = [
            (HardwareCost::FREE, (0, 0)),
            (HardwareCost::VERY_LOW, (1, 100)),
            (HardwareCost::LOW, (100, 500)),
            (HardwareCost::MEDIUM, (500, 2000)),
            (HardwareCost::HIGH, (2000, 10000)),
            (HardwareCost::VERY_HIGH, (10000, 100000)),
            (HardwareCost::SUBSIDIZED, (0, 0)),
        ].into_iter().collect();
        let mut min_total = 0i64;
        let mut max_total = 0i64;
        for d in devices {
            if let Some((lo, hi)) = cost_ranges.get(&d.cost) {
                min_total += lo;
                max_total += hi;
            }
        }
        let mut result = HashMap::new();
        result.insert("min_brl".to_string(), min_total.to_string());
        result.insert("max_brl".to_string(), max_total.to_string());
        result.insert("device_count".to_string(), devices.len().to_string());
        result
    }
}

// ============================================================================
// 5. BRIDGE IDE <-> HARDWARE
// ============================================================================
struct HardwareBridge {
    connected_devices: Vec<&'static HardwareDevice>,
    engine: HardwareCompatibilityEngine,
    active_inputs: Vec<String>,
    active_outputs: Vec<String>,
}

impl HardwareBridge {
    fn new() -> Self {
        HardwareBridge {
            connected_devices: vec![],
            engine: HardwareCompatibilityEngine::new(),
            active_inputs: vec![],
            active_outputs: vec![],
        }
    }

    fn detect_devices(&mut self) -> Vec<&'static HardwareDevice> {
        if let Some(base) = self.engine.catalog.get("HW-001") {
            self.connected_devices = vec![*base];
            self._update_capabilities();
        }
        self.connected_devices.clone()
    }

    fn connect_device(&mut self, device: &'static HardwareDevice) -> bool {
        if !self.connected_devices.iter().any(|d| std::ptr::eq(*d, device)) {
            self.connected_devices.push(device);
            self._update_capabilities();
        }
        true
    }

    fn disconnect_device(&mut self, device: &'static HardwareDevice) -> bool {
        if let Some(pos) = self.connected_devices.iter().position(|d| std::ptr::eq(*d, device)) {
            self.connected_devices.remove(pos);
            self._update_capabilities();
        }
        true
    }

    fn _update_capabilities(&mut self) {
        self.active_inputs.clear();
        self.active_outputs.clear();
        for d in &self.connected_devices {
            for cap in &d.input_capabilities {
                if !self.active_inputs.contains(cap) {
                    self.active_inputs.push(cap.clone());
                }
            }
            for cap in &d.output_capabilities {
                if !self.active_outputs.contains(cap) {
                    self.active_outputs.push(cap.clone());
                }
            }
        }
    }

    fn available_input_modes(&self) -> Vec<String> {
        let mut modes = HashSet::new();
        for d in &self.connected_devices {
            if d.input_capabilities.iter().any(|c| c == "voice" || c == "microphone") {
                modes.insert("voz".to_string());
                modes.insert("voz_codigo".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "touch" || c == "touch_small") {
                modes.insert("toque".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "keyboard") {
                modes.insert("teclado_completo".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "braille_keys" || c == "braille_input_6_keys") {
                modes.insert("teclado_braille".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "eye_gaze") {
                modes.insert("rastreio_olhos".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "single_switch" || c == "dual_switch") {
                modes.insert("chave".to_string());
                modes.insert("chave_dupla".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "trackball") {
                modes.insert("trackball".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "foot_press_left") {
                modes.insert("pedal_pe".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "head_stick") {
                modes.insert("teclado_cabeca".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "sip_puff") {
                modes.insert("teclado_boca".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "eeg_waves" || c == "neural_spikes") {
                modes.insert("interface_cerebral".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "emg_signal") {
                modes.insert("eletromiografo".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "hand_tracking") {
                modes.insert("gesto".to_string());
            }
            if d.input_capabilities.iter().any(|c| c == "heart_rate") {
                modes.insert("biofeedback".to_string());
            }
        }
        let mut v: Vec<_> = modes.into_iter().collect();
        v.sort();
        v
    }

    fn available_output_modes(&self) -> Vec<String> {
        let mut modes = HashSet::new();
        for d in &self.connected_devices {
            if d.output_capabilities.iter().any(|c| c == "screen" || c == "screen_large") {
                modes.insert("texto_visual".to_string());
            }
            if d.output_capabilities.iter().any(|c| c == "screen_tiny") {
                modes.insert("texto_tela_pequena".to_string());
            }
            if d.output_capabilities.iter().any(|c| c == "tts" || c == "tts_basic" || c == "speaker") {
                modes.insert("texto_para_voz".to_string());
            }
            if d.output_capabilities.iter().any(|c| c == "braille_cells_40" || c == "braille_cells_14") {
                modes.insert("display_braille".to_string());
            }
            if d.output_capabilities.iter().any(|c| c == "vibration" || c == "haptic") {
                modes.insert("haptico".to_string());
            }
            if d.output_capabilities.iter().any(|c| c == "color_light") {
                modes.insert("luz_cor".to_string());
            }
            if d.output_capabilities.iter().any(|c| c == "audio_amplified") {
                modes.insert("audio_amplificado".to_string());
            }
            if d.output_capabilities.iter().any(|c| c == "audio_anc") {
                modes.insert("audio_cancelamento_ruido".to_string());
            }
            if d.output_capabilities.iter().any(|c| c == "hud_overlay") {
                modes.insert("hud_oculos".to_string());
            }
            if d.output_capabilities.iter().any(|c| c == "taptic_engine") {
                modes.insert("taptic_preciso".to_string());
            }
        }
        let mut v: Vec<_> = modes.into_iter().collect();
        v.sort();
        v
    }

    fn supports_input_mode(&self, mode: &str) -> bool {
        self.available_input_modes().contains(&mode.to_string())
    }

    fn supports_output_mode(&self, mode: &str) -> bool {
        self.available_output_modes().contains(&mode.to_string())
    }

    fn session_info(&self) -> HashMap<String, String> {
        let mut info = HashMap::new();
        info.insert("device_count".to_string(), self.connected_devices.len().to_string());
        info
    }
}

// ============================================================================
// 6. PERFIS DE SETUP
// ============================================================================
fn create_setup_budget() -> Vec<&'static HardwareDevice> {
    let engine = HardwareCompatibilityEngine::new();
    vec![
        engine.catalog["HW-001"],
        engine.catalog["HC-029"],
        engine.catalog["HW-018"],
    ]
}

fn create_setup_blind() -> Vec<&'static HardwareDevice> {
    let engine = HardwareCompatibilityEngine::new();
    vec![
        engine.catalog["HW-001"],
        engine.catalog["HW-014"],
        engine.catalog["HW-013"],
        engine.catalog["HW-040"],
    ]
}

fn create_setup_deaf() -> Vec<&'static HardwareDevice> {
    let engine = HardwareCompatibilityEngine::new();
    vec![
        engine.catalog["HW-001"],
        engine.catalog["HW-006"],
        engine.catalog["HC-031"],
    ]
}

fn create_setup_motor_severe() -> Vec<&'static HardwareDevice> {
    let engine = HardwareCompatibilityEngine::new();
    vec![
        engine.catalog["HW-011"],
        engine.catalog["HW-016"],
        engine.catalog["HW-038"],
    ]
}

fn create_setup_autism() -> Vec<&'static HardwareDevice> {
    let engine = HardwareCompatibilityEngine::new();
    vec![
        engine.catalog["HW-001"],
        engine.catalog["HC-029"],
        engine.catalog["HC-031"],
        engine.catalog["HC-032"],
    ]
}

fn create_setup_adhd() -> Vec<&'static HardwareDevice> {
    let engine = HardwareCompatibilityEngine::new();
    vec![
        engine.catalog["HW-001"],
        engine.catalog["HC-029"],
        engine.catalog["HW-007"],
    ]
}

fn create_setup_epilepsy() -> Vec<&'static HardwareDevice> {
    let engine = HardwareCompatibilityEngine::new();
    vec![
        engine.catalog["HW-001"],
        engine.catalog["HC-031"],
        engine.catalog["HW-007"],
    ]
}

fn create_setup_public_terminal() -> Vec<&'static HardwareDevice> {
    let engine = HardwareCompatibilityEngine::new();
    vec![engine.catalog["HW-037"]]
}

fn create_setup_zero_cost() -> Vec<&'static HardwareDevice> {
    let engine = HardwareCompatibilityEngine::new();
    vec![
        engine.catalog["HW-037"],
        engine.catalog["HW-014"],
    ]
}

// ============================================================================
// 7. ESCADA DE ESCALABILIDADE
// ============================================================================
struct HardwareEscalationLadder;

impl HardwareEscalationLadder {
    const RUNGS: [(&'static str, fn() -> Vec<&'static HardwareDevice>, &'static str); 6] = [
        ("Degrau 0: ZERO CUSTO", create_setup_zero_cost, "Biblioteca publica + NVDA gratis. Todo mundo comeca aqui."),
        ("Degrau 1: SMARTPHONE", create_setup_budget, "Smartphone R$300 + fone R$50 + switch R$30. Acesse de qualquer lugar."),
        ("Degrau 2: TABLET/WEARABLE", create_setup_deaf, "Adiciona smartwatch/luz para feedback multimodal."),
        ("Degrau 3: ASSISTIVO ESPECIFICO", create_setup_blind, "Adiciona braille/eye-tracker especifico para deficiencia."),
        ("Degrau 4: SETUP COMPLETO", create_setup_motor_severe, "Notebook + eye-tracker + microfone. Desenvolvimento profissional."),
        ("Degrau 5: BCI/EXPERIMENTAL", create_setup_zero_cost, "BCI, haptic vest, smart glasses. Fronteira da tecnologia."),
    ];

    fn recommend_rung(budget: HardwareCost) -> (usize, &'static str) {
        match budget {
            HardwareCost::FREE => (0, Self::RUNGS[0].2),
            HardwareCost::VERY_LOW | HardwareCost::LOW => (1, Self::RUNGS[1].2),
            HardwareCost::MEDIUM => (2, Self::RUNGS[2].2),
            HardwareCost::HIGH => (3, Self::RUNGS[3].2),
            HardwareCost::VERY_HIGH => (5, Self::RUNGS[5].2),
            _ => (0, Self::RUNGS[0].2),
        }
    }

    fn show_ladder() {
        println!("\nESCALADA DE HARDWARE -- Do Zero ao Profissional");
        println!("{}", "=".repeat(60));
        for (name, func, desc) in Self::RUNGS.iter() {
            let setup = func();
            let engine = HardwareCompatibilityEngine::new();
            let cost = engine.total_setup_cost(&setup);
            println!("\n  {}", name);
            println!("    {}", desc);
            println!("    Custo: R$ {}-{}", cost["min_brl"], cost["max_brl"]);
            println!("    Devices: {}", cost["device_count"]);
        }
    }
}

// ============================================================================
// 8. DEMONSTRACAO (main)
// ============================================================================
fn demo() {
    println!("{}", "=".repeat(70));
    println!("OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel");
    println!("{}", "=".repeat(70));

    let engine = HardwareCompatibilityEngine::new();
    println!("\nCatalogo: {} dispositivos mapeados", HARDWARE_CATALOG.len());

    // Bridge demo
    println!("\n{}", "=".repeat(70));
    println!("HARDWARE BRIDGE -- Deteccao e Configuracao");
    println!("{}", "=".repeat(70));

    let mut bridge = HardwareBridge::new();
    let detected = bridge.detect_devices();
    println!("\nDispositivos detectados: {:?}", detected.iter().map(|d| &d.name).collect::<Vec<_>>());

    println!("\n+ Conectando Display Braille...");
    bridge.connect_device(engine.catalog["HW-013"]);
    println!("\n+ Conectando Eye Tracker...");
    bridge.connect_device(engine.catalog["HW-016"]);
    println!("\n+ Conectando Smartwatch...");
    bridge.connect_device(engine.catalog["HW-006"]);

    // Perfis de setup
    println!("\n{}", "=".repeat(70));
    println!("PERFIS DE SETUP");
    println!("{}", "=".repeat(70));

    let setups = vec![
        ("ZERO CUSTO (biblioteca)", create_setup_zero_cost()),
        ("BAIXO CUSTO (smartphone)", create_setup_budget()),
        ("CEGO (braille completo)", create_setup_blind()),
        ("SURDO (visual+haptic)", create_setup_deaf()),
        ("TETRAPLEGICO (eye+voz)", create_setup_motor_severe()),
        ("AUTISTA (calmo)", create_setup_autism()),
        ("TDAH (foco)", create_setup_adhd()),
        ("EPILEPSIA (seguro)", create_setup_epilepsy()),
        ("TERMINAL PUBLICO", create_setup_public_terminal()),
    ];

    for (label, setup) in setups {
        let cost = engine.total_setup_cost(&setup);
        println!("\n  {}", label);
        println!("    Devices: {} | Custo: R$ {}-{}", cost["device_count"], cost["min_brl"], cost["max_brl"]);
        for d in setup {
            println!("      - {}", d.name);
        }
    }

    HardwareEscalationLadder::show_ladder();

    println!("\n{}", "=".repeat(70));
    println!("TODO hardware. TODA deficiencia. ZERO barreira.");
}

fn main() {
    demo();
}