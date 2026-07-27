# OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel

**Arquivo original:** `open-republic/core/open_inclusive_hardware.py`

**Descricao:** ================================================================
"O hardware certo transforma uma deficiencia em uma capacidade.
O cego tem o smartphone como olhos. O surdo tem o smartwatch como ouvidos.
O tetraplegico tem o eye-tracker como maos. O autista tem o fone como escudo.
A IDE nao escolhe o hardware. O HARDWARE DO USUARIO escolhe a IDE.
Se a pessoa tem um smartphone Android de R$300, a IDE funciona.
Se a pessoa tem um SmartWatch, a IDE funciona.
Se a pessoa tem um eye-tracker de R$15.000, a IDE funciona.
Se a pessoa NAO TEM NADA, a IDE funciona no terminal publico (OpenTerminal).
ZERO barreira de hardware. ZERO custo de entrada. MAXIMA adaptacao.
Integrado com:
- OpenInclusiveIDE (IDE se adapta ao hardware disponivel)
- OpenTerminal (todo terminal publico roda a IDE)
- OpenAbsence (hardware respeita pausas)
- OpenBodilyAutonomy (usuario controla seu dispositivo)
- OpenSilencePolicy (dispositivos respeitam o silencio)
HARDWARE MAPEADO (6 CATEGORIAS, 40+ DISPOSITIVOS):
1. MASSA (smartphone, tablet, smartwatch, notebook, desktop)
   - Disponivel em qualquer lugar, barato, ubiquo
2. ASSISTIVO VISUAL (leitor de tela, display braille, lupa eletronica)
   - Para cegos e baixa visao
3. ASSISTIVO MOTOR (eye-tracker, switch, teclado especial, BCI)
   - Para deficiencias motoras severas
4. ASSISTIVO AUDITIVO (implante coclear, aparelho auditivo, loop磁)
   - Para surdos e baixa audicao
5. ASSISTIVO COGNITIVO (fone ANC, luz inteligente, weighted blanket)
   - Para autismo, TDAH, epilepsia
6. TERMINAL PUBLICO (TV, kiosk, terminal burro, computador comunitario)
   - Para quem nao tem hardware proprio
PRINCIPIO CHAVE: O hardware NAO define o desenvolvedor.
O desenvolvedor define o hardware. A IDE se adapta.
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol

// !/usr/bin/env python3
// 
OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel
================================================================
"O hardware certo transforma uma deficiencia em uma capacidade.
O cego tem o smartphone como olhos. O surdo tem o smartwatch como ouvidos.
O tetraplegico tem o eye-tracker como maos. O autista tem o fone como escudo.

A IDE nao escolhe o hardware. O HARDWARE DO USUARIO escolhe a IDE.
Se a pessoa tem um smartphone Android de R$300, a IDE funciona.
Se a pessoa tem um SmartWatch, a IDE funciona.
Se a pessoa tem um eye-tracker de R$15.000, a IDE funciona.
Se a pessoa NAO TEM NADA, a IDE funciona no terminal publico (OpenTerminal).

ZERO barreira de hardware. ZERO custo de entrada. MAXIMA adaptacao.

Integrado com:
- OpenInclusiveIDE (IDE se adapta ao hardware disponivel)
- OpenTerminal (todo terminal publico roda a IDE)
- OpenAbsence (hardware respeita pausas)
- OpenBodilyAutonomy (usuario controla seu dispositivo)
- OpenSilencePolicy (dispositivos respeitam o silencio)

HARDWARE MAPEADO (6 CATEGORIAS, 40+ DISPOSITIVOS):

1. MASSA (smartphone, tablet, smartwatch, notebook, desktop)
   - Disponivel em qualquer lugar, barato, ubiquo
   
2. ASSISTIVO VISUAL (leitor de tela, display braille, lupa eletronica)
   - Para cegos e baixa visao
   
3. ASSISTIVO MOTOR (eye-tracker, switch, teclado especial, BCI)
   - Para deficiencias motoras severas
   
4. ASSISTIVO AUDITIVO (implante coclear, aparelho auditivo, loop磁)
   - Para surdos e baixa audicao
   
5. ASSISTIVO COGNITIVO (fone ANC, luz inteligente, weighted blanket)
   - Para autismo, TDAH, epilepsia
   
6. TERMINAL PUBLICO (TV, kiosk, terminal burro, computador comunitario)
   - Para quem nao tem hardware proprio

PRINCIPIO CHAVE: O hardware NAO define o desenvolvedor.
O desenvolvedor define o hardware. A IDE se adapta.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa hashlib


// ============================================================================
// 1. CATEGORIAS DE HARDWARE
// ============================================================================

classe HardwareCategory herda de Enum:
    MASS <- "massa"  // smartphone, tablet, smartwatch, notebook
    ASSISTIVE_VISUAL <- "assistivo_visual"  // leitor de tela, braille, lupa
    ASSISTIVE_MOTOR <- "assistivo_motor"  // eye-tracker, switch, BCI
    ASSISTIVE_AUDITORY <- "assistivo_auditivo"  // implante coclear, loop
    ASSISTIVE_COGNITIVE <- "assistivo_cognitivo"  // fone ANC, luz, blanket
    TERMINAL_PUBLIC <- "terminal_publico"  // TV, kiosk, terminal burro
    WEARABLE <- "vestivel"  // smartwatch, anel smart, Oculus
    BRAIN <- "cerebral"  // BCI, EEG, Neuralink


classe HardwareCost herda de Enum:
    // Custo de aquisicao do hardware.
    FREE <- "gratis"  // terminal publico, biblioteca
    VERY_LOW <- "muito_baixo"  // < R$ 100 (fone simples, switch DIY)
    LOW <- "baixo"  // R$ 100-500 (smartphone basico)
    MEDIUM <- "medio"  // R$ 500-2000 (tablet, smartwatch)
    HIGH <- "alto"  // R$ 2000-10000 (eye-tracker, braille)
    VERY_HIGH <- "muito_alto"  // > R$ 10000 (BCI, implante coclear)
    SUBSIDIZED <- "subsidiado"  // governo/seguro cobre


classe HardwareAvailability herda de Enum:
    // Disponibilidade no Brasil/mundo.
    UBIQUITOUS <- "ubiquo"  // em qualquer lugar (smartphone)
    COMMON <- "comum"  // lojas comuns (tablet, smartwatch)
    SPECIALIZED <- "especializado"  // lojas de acessibilidade
    MEDICAL <- "medico"  // prescricao medica (implante)
    RARE <- "raro"  // importacao, poucos fornecedores
    EXPERIMENTAL <- "experimental"  // pesquisa, ainda nao comercial


classe ConnectionType herda de Enum:
    BLUETOOTH <- "bluetooth"
    USB <- "usb"
    WIFI <- "wifi"
    NFC <- "nfc"
    CLOUD <- "nuvem"
    AUDIO_JACK <- "jack_audio"
    PROPRIETARY <- "proprietario"
    WIRELESS <- "sem_fio_generico"
    HDMI <- "hdmi"


// ============================================================================
// 2. PERFIL DE HARDWARE
// ============================================================================

// decorador: @dataclass
classe HardwareDevice:
    // Um dispositivo de hardware mapeado.
    device_id: str
    name: str
    category: HardwareCategory
    cost: HardwareCost
    availability: HardwareAvailability
    declare connections: List[ConnectionType]  <- field(default_factory=list)
    declare platforms: List[str]  <- field(default_factory=list)  // Android, iOS, Linux, Windows, etc
    declare disabilities_served: List[str]  <- field(default_factory=list)  // categories served
    declare input_capabilities: List[str]  <- field(default_factory=list)  // what it can provide
    declare output_capabilities: List[str]  <- field(default_factory=list)  // what it can display
    declare battery_hours: float  <- 0.0  // 0 = plugged in
    declare offline_capable: bool  <- VERDADEIRO  // works without internet
    declare languages_supported: List[str]  <- field(default_factory=lambda: ["pt-BR"])
    declare description: str  <- ""


// ============================================================================
// 3. CATALOGO DE HARDWARE (40+ DISPOSITIVOS)
// ============================================================================

declare HARDWARE_CATALOG: List[HardwareDevice]  <- [
    // === SMARTPHONE (massa) ===
    HardwareDevice("HW-001", "Smartphone Android (qualquer)",
        HardwareCategory.MASS, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.NFC, ConnectionType.AUDIO_JACK],
        platforms <- ["Android"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "multipla", "temporaria"],
        input_capabilities <- ["touch", "voice", "camera", "microphone", "bluetooth_keyboard", "nfc", "accelerometer", "gyroscope"],
        output_capabilities <- ["screen", "speaker", "vibration", "flash_led", "screen_reader"],
        battery_hours <- 12.0,
        description <- "O dispositivo mais inclusivo do planeta. TalkBack, Voice Access, Switch Access nativos."),

    HardwareDevice("HW-002", "iPhone (qualquer)",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.NFC],
        platforms <- ["iOS"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "multipla", "temporaria"],
        input_capabilities <- ["touch", "voice", "face_id", "camera", "microphone", "bluetooth_keyboard", "lidar"],
        output_capabilities <- ["screen", "speaker", "vibration", "taptic_engine", "voiceover", "flash_led"],
        battery_hours <- 15.0,
        description <- "VoiceOver, Switch Control, Voice Control, Sound Detection nativos. Lidar para deteccao de obstaculos."),

    HardwareDevice("HW-003", "Smartphone basico (teclado fisico)",
        HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        connections <- [ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH],
        platforms <- ["KaiOS", "Feature Phone"],
        disabilities_served <- ["visual", "motora", "temporaria"],
        input_capabilities <- ["keypad", "voice", "microphone"],
        output_capabilities <- ["screen_small", "speaker", "vibration", "tts_basic"],
        battery_hours <- 72.0,
        description <- "Telefone botoeiro com TTS. Para quem nao tem smartphone ou prefere teclado fisico."),

    // === TABLET ===
    HardwareDevice("HW-004", "Tablet Android",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI],
        platforms <- ["Android"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento"],
        input_capabilities <- ["touch", "voice", "camera", "microphone", "stylus", "bluetooth_keyboard"],
        output_capabilities <- ["screen_large", "speaker", "vibration"],
        battery_hours <- 10.0,
        description <- "Tela maior = mais area para botoes grandes, blocos visuais, zoom."),

    HardwareDevice("HW-005", "iPad",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI],
        platforms <- ["iPadOS"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento"],
        input_capabilities <- ["touch", "voice", "face_id", "camera", "microphone", "stylus_pencil", "lidar"],
        output_capabilities <- ["screen_large", "speaker", "taptic_engine", "voiceover"],
        battery_hours <- 10.0,
        description <- "Apple Pencil para deteccao de tremores. AssistiveTouch. Full Keyboard Control."),

    // === SMARTWATCH / WEARABLE ===
    HardwareDevice("HW-006", "Smartwatch Android (WearOS)",
        HardwareCategory.WEARABLE, HardwareCost.MEDIUM, HardwareAvailability.COMMON,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.WIFI],
        platforms <- ["WearOS"],
        disabilities_served <- ["auditiva", "motora", "cognitiva", "temporaria"],
        input_capabilities <- ["touch_small", "voice", "microphone", "accelerometer", "heart_rate", "gestures", "crown"],
        output_capabilities <- ["screen_tiny", "vibration", "speaker_tiny", "haptic"],
        battery_hours <- 24.0,
        description <- "Vibracao no pulso para alertas (surdez). Monitor de batimento (epilepsia/ansiedade). Coroa para navegacao (motor)."),

    HardwareDevice("HW-007", "Apple Watch",
        HardwareCategory.WEARABLE, HardwareCost.MEDIUM, HardwareAvailability.COMMON,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.WIFI],
        platforms <- ["watchOS"],
        disabilities_served <- ["auditiva", "motora", "cognitiva", "temporaria", "neurologica"],
        input_capabilities <- ["touch_small", "voice", "microphone", "crown_digital", "accelerometer", "heart_rate", "ecg", "fall_detection", "gestures", "sip_pinch"],
        output_capabilities <- ["screen_tiny", "taptic_engine", "speaker_tiny", "haptic"],
        battery_hours <- 18.0,
        description <- "Fall Detection (queda). ECG (coracao). Taptic Engine para surdos. AssistiveTouch (pinca/sorvo para tetraplegia). Noise app (autismo)."),

    HardwareDevice("HW-008", "Smartwatch basico / Pulseira fitness",
        HardwareCategory.WEARABLE, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.BLUETOOTH],
        platforms <- ["Proprietary"],
        disabilities_served <- ["auditiva", "temporaria"],
        input_capabilities <- ["touch_tiny", "accelerometer", "heart_rate"],
        output_capabilities <- ["screen_tiny", "vibration"],
        battery_hours <- 168.0,  // 7 dias
        description <- "R$80-200. Vibracao para notificacoes (surdez). Monitor basico de sono/atividade."),

    HardwareDevice("HW-009", "Anel Smart (Smart Ring)",
        HardwareCategory.WEARABLE, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.BLUETOOTH],
        platforms <- ["Proprietary"],
        disabilities_served <- ["auditiva", "neurologica"],
        input_capabilities <- ["accelerometer", "heart_rate", "temperature", "spO2"],
        output_capabilities <- ["vibration_tiny", "led"],
        battery_hours <- 168.0,
        description <- "Discreto. Monitor de sono, temperatura, SpO2. Para autismo: biofeedback discreto."),

    HardwareDevice("HW-010", "Oculos Inteligentes (Smart Glasses)",
        HardwareCategory.WEARABLE, HardwareCost.HIGH, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.WIFI],
        platforms <- ["Android", "Proprietary"],
        disabilities_served <- ["visual", "auditiva", "motora", "neurologica"],
        input_capabilities <- ["voice", "camera", "microphone", "bone_conduction_audio", "head_tracking", "eye_tracking_basic"],
        output_capabilities <- ["hud_overlay", "bone_conduction_speaker", "vibration"],
        battery_hours <- 6.0,
        description <- "Legendas em tempo real no campo de visao (surdez). Navegacao por setas (cegueira). Heads-up display."),

    // === COMPUTADOR / NOTEBOOK ===
    HardwareDevice("HW-011", "Notebook / Laptop",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.AUDIO_JACK],
        platforms <- ["Linux", "Windows", "macOS"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "neurologica", "multipla", "temporaria"],
        input_capabilities <- ["keyboard", "trackpad", "microphone", "camera", "bluetooth_devices"],
        output_capabilities <- ["screen", "speaker", "vibration_rare"],
        battery_hours <- 8.0,
        description <- "Plataforma de desenvolvimento completa. Screen readers, IDEs, eye-tracking via USB."),

    HardwareDevice("HW-012", "Desktop / PC",
        HardwareCategory.MASS, HardwareCost.MEDIUM, HardwareAvailability.COMMON,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB, ConnectionType.WIFI, ConnectionType.AUDIO_JACK],
        platforms <- ["Linux", "Windows"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "neurologica", "multipla"],
        input_capabilities <- ["keyboard", "mouse", "microphone", "camera", "usb_devices", "pcie_cards"],
        output_capabilities <- ["screen_large", "speaker", "multi_monitor"],
        battery_hours <- 0.0,  // plugged
        description <- "Maximo de conectividade. Multi-tela, GPUs para IA, todo tipo de periferico."),

    // === LEITOR DE TELA / DISPLAY BRAILLE ===
    HardwareDevice("HW-013", "Display Braille (linha braille)",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.HIGH, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB],
        platforms <- ["Android", "iOS", "Linux", "Windows", "macOS"],
        disabilities_served <- ["visual"],
        input_capabilities <- ["braille_keys", "routing_buttons", "navigation"],
        output_capabilities <- ["braille_cells_40", "braille_cells_80"],
        battery_hours <- 20.0,
        description <- "40-80 celulas braille. Celulas piezoeletricas que sobem e descem. Cego le codigo tateando."),

    HardwareDevice("HW-013b", "Display Braille portatil (14-20 celulas)",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB],
        platforms <- ["Android", "iOS"],
        disabilities_served <- ["visual"],
        input_capabilities <- ["braille_keys"],
        output_capabilities <- ["braille_cells_14"],
        battery_hours <- 20.0,
        description <- "Versao portatil menor. Cabe no bolso. Conecta no smartphone."),

    HardwareDevice("HW-014", "Leitor de tela software (NVDA, Orca, VoiceOver, TalkBack)",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.FREE, HardwareAvailability.UBIQUITOUS,
        connections <- [],
        platforms <- ["Android", "iOS", "Linux", "Windows", "macOS"],
        disabilities_served <- ["visual"],
        input_capabilities <- [],
        output_capabilities <- ["tts", "braille_output", "audio_cues"],
        battery_hours <- 0.0,  // software
        description <- "NVDA (gratis, Windows). Orca (Linux). VoiceOver (Apple). TalkBack (Android). Converte tela em voz/braille."),

    HardwareDevice("HW-015", "Lupa eletronica / CCTV",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.HDMI],
        platforms <- ["Standalone"],
        disabilities_served <- ["visual"],
        input_capabilities <- ["camera_zoom"],
        output_capabilities <- ["screen_zoomed"],
        battery_hours <- 4.0,
        description <- "Camera que amplia texto/papel para tela. Para baixa visao."),

    // === EYE TRACKER / SWITCH / MOTOR ===
    HardwareDevice("HW-016", "Eye Tracker (Tobii, EyeX)",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.HIGH, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.USB, ConnectionType.WIFI],
        platforms <- ["Windows", "Linux"],
        disabilities_served <- ["motora", "multipla"],
        input_capabilities <- ["eye_gaze", "dwell_selection", "blink"],
        output_capabilities <- [],
        battery_hours <- 0.0,
        description <- "Camera infravermelha rastreia olhos. Tetraplegia, ELA, paralisia cerebral. Custo: R$2.000-8.000."),

    HardwareDevice("HW-017", "Eye Tracker portatil (smartphone)",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        connections <- [],
        platforms <- ["Android", "iOS"],
        disabilities_served <- ["motora", "multipla"],
        input_capabilities <- ["eye_gaze_front_camera"],
        output_capabilities <- [],
        battery_hours <- 6.0,
        description <- "Usa camera frontal do smartphone para rastrear olhos. Precisao menor mas gratuito com app."),

    HardwareDevice("HW-018", "Switch / Botao adaptativo",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.AUDIO_JACK, ConnectionType.USB],
        platforms <- ["Android", "iOS", "Windows", "Linux", "macOS"],
        disabilities_served <- ["motora", "multipla", "desenvolvimento"],
        input_capabilities <- ["single_switch", "dual_switch"],
        output_capabilities <- [],
        battery_hours <- 0.0,
        description <- "Um ou dois botoes grandes. Scan automatico passa opcoes, usuario aciona para selecionar. DIY possivel por R$20."),

    HardwareDevice("HW-019", "Teclado adaptativo grande",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB],
        platforms <- ["Android", "iOS", "Windows", "Linux", "macOS"],
        disabilities_served <- ["motora", "cognitiva", "desenvolvimento"],
        input_capabilities <- ["large_keys", "color_coded"],
        output_capabilities <- [],
        battery_hours <- 0.0,
        description <- "Teclas 3x maiores, coloridas, com guard de mao. Para tremores, baixa destreza, Down."),

    HardwareDevice("HW-020", "Teclado de cabeca / boca",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.USB, ConnectionType.BLUETOOTH],
        platforms <- ["Windows", "Linux", "Android"],
        disabilities_served <- ["motora"],
        input_capabilities <- ["head_stick", "mouth_stick", "sip_puff"],
        output_capabilities <- [],
        battery_hours <- 0.0,
        description <- "Ponteiro de cabeca ou bocal para digitar em teclado na tela. Sip-and-puff = sopro/succao."),

    HardwareDevice("HW-021", "Trackball adaptativo",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.COMMON,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB],
        platforms <- ["Windows", "Linux", "macOS", "Android"],
        disabilities_served <- ["motora"],
        input_capabilities <- ["trackball", "large_ball"],
        output_capabilities <- [],
        battery_hours <- 0.0,
        description <- "Bola grande movida com palma/queixo/dorso do pe. Estavel para tremores (Parkinson)."),

    HardwareDevice("HW-022", "Pedal de pe (Foot Pedal)",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        connections <- [ConnectionType.USB, ConnectionType.BLUETOOTH],
        platforms <- ["Windows", "Linux", "macOS"],
        disabilities_served <- ["motora", "temporaria"],
        input_capabilities <- ["foot_press_left", "foot_press_right", "foot_press_center"],
        output_capabilities <- [],
        battery_hours <- 0.0,
        description <- "Para quem tem uso dos pes mas nao das maos. 3 pedais = 3 botoes. R$50-150."),

    HardwareDevice("HW-023", "EMG / MIODOELETRICO (braco bio-feedback)",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.MEDIUM, HardwareAvailability.EXPERIMENTAL,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB],
        platforms <- ["Windows", "Linux", "Android"],
        disabilities_served <- ["motora", "multipla"],
        input_capabilities <- ["emg_signal", "muscle_activation"],
        output_capabilities <- [],
        battery_hours <- 8.0,
        description <- "Sensores no musculo. Detecta contracao muscular residual. Para amputados, paralisia parcial."),

    // === BCI / CEREBRAL ===
    HardwareDevice("HW-024", "BCI Invasivo (Neuralink/Synchron)",
        HardwareCategory.BRAIN, HardwareCost.VERY_HIGH, HardwareAvailability.EXPERIMENTAL,
        connections <- [ConnectionType.WIFI, ConnectionType.BLUETOOTH],
        platforms <- ["Windows", "Linux"],
        disabilities_served <- ["motora", "multipla"],
        input_capabilities <- ["neural_spikes", "motor_intention"],
        output_capabilities <- [],
        battery_hours <- 0.0,  // implante
        description <- "Eletrodos no cerebro. Tetraplegia profunda. Ainda em ensaios clinicos."),

    HardwareDevice("HW-025", "BCI Nao-Invasivo (EEG headset)",
        HardwareCategory.BRAIN, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB],
        platforms <- ["Windows", "Linux", "Android"],
        disabilities_served <- ["motora", "multipla"],
        input_capabilities <- ["eeg_waves", "concentration_level", "blink_detect"],
        output_capabilities <- ["neurofeedback_display"],
        battery_hours <- 6.0,
        description <- "Capacete com eletrodos. Le ondas cerebrais. Precisao baixa mas nao invasivo. R$500-3000."),

    // === AUDITIVO ===
    HardwareDevice("HC-026", "Aparelho Auditivo (digital)",
        HardwareCategory.ASSISTIVE_AUDITORY, HardwareCost.MEDIUM, HardwareAvailability.MEDICAL,
        connections <- [ConnectionType.BLUETOOTH],
        platforms <- ["Standalone"],
        disabilities_served <- ["auditiva"],
        input_capabilities <- ["bluetooth_audio_in"],
        output_capabilities <- ["audio_amplified", "audio_filtered"],
        battery_hours <- 96.0,  // 4 dias
        description <- "Amplifica e filtra som. Bluetooth direto do smartphone. Programa SUS cobre."),

    HardwareDevice("HC-027", "Implante Coclear",
        HardwareCategory.ASSISTIVE_AUDITORY, HardwareCost.VERY_HIGH, HardwareAvailability.MEDICAL,
        connections <- [ConnectionType.BLUETOOTH],
        platforms <- ["Standalone"],
        disabilities_served <- ["auditiva"],
        input_capabilities <- ["bluetooth_audio_in"],
        output_capabilities <- ["electrical_stimulation"],
        battery_hours <- 24.0,
        description <- "Cirurgico. Eletrodos na coclea. Para surdez profunda. SUS cobre em alguns estados."),

    HardwareDevice("HC-028", "Loop Magnetico / Sistema FM",
        HardwareCategory.ASSISTIVE_AUDITORY, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH],
        platforms <- ["Standalone"],
        disabilities_served <- ["auditiva"],
        input_capabilities <- ["audio_in"],
        output_capabilities <- ["magnetic_loop"],
        battery_hours <- 0.0,
        description <- "Cabo de loop magnetico no pescoco. Transmite audio direto pro aparelho auditivo. Elimina ruido ambiente."),

    // === COGNITIVO / SENSORIAL ===
    HardwareDevice("HC-029", "Fone ANC (Active Noise Cancelling)",
        HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.AUDIO_JACK],
        platforms <- ["Standalone"],
        disabilities_served <- ["espectro_autista", "auditiva", "cognitiva"],
        input_capabilities <- ["anc_microphone"],
        output_capabilities <- ["audio_anc", "audio_filtered"],
        battery_hours <- 30.0,
        description <- "Cancela ruido ambiente. ESCUDO SENSORIAL para autista/TDAH em ambiente ruidoso. R$100-500."),

    HardwareDevice("HC-030", "Fone com microfone direcional",
        HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.LOW, HardwareAvailability.COMMON,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.AUDIO_JACK],
        platforms <- ["Standalone"],
        disabilities_served <- ["auditiva", "espectro_autista"],
        input_capabilities <- ["directional_microphone"],
        output_capabilities <- ["audio_directed"],
        battery_hours <- 20.0,
        description <- "Captura som da frente, cancela resto. Para APD (Processamento Auditivo) e autismo."),

    HardwareDevice("HC-031", "Luz Inteligente (Smart Bulb)",
        HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.LOW, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.WIFI, ConnectionType.BLUETOOTH],
        platforms <- ["Android", "iOS"],
        disabilities_served <- ["visual", "auditiva", "espectro_autista", "neurologica"],
        input_capabilities <- [],
        output_capabilities <- ["color_light", "brightness_control", "temperature_color", "no_flicker"],
        battery_hours <- 0.0,
        description <- "Notificacao visual por cor (surdez). Luz quente para acalmar (autismo/epilepsia). Sem flicker."),

    HardwareDevice("HC-032", "Weighted Blanket (Manta Ponderada)",
        HardwareCategory.ASSISTIVE_COGNITIVE, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        connections <- [],
        platforms <- ["Physical"],
        disabilities_served <- ["espectro_autista", "cognitiva", "neurologica"],
        input_capabilities <- [],
        output_capabilities <- ["deep_pressure_stimulation"],
        battery_hours <- 0.0,
        description <- "Pressao profunda calmante. Reduz ansiedade (autismo/TDAH). Melhora sono. R$100-300."),

    HardwareDevice("HC-033", "Bracelete Anti-Ansiedade / Vibratorio",
        HardwareCategory.WEARABLE, HardwareCost.VERY_LOW, HardwareAvailability.COMMON,
        connections <- [ConnectionType.BLUETOOTH],
        platforms <- ["Android", "iOS"],
        disabilities_served <- ["espectro_autista", "cognitiva", "neurologica"],
        input_capabilities <- ["heart_rate", "skin_conductance"],
        output_capabilities <- ["vibration_patterns", "temperature_cooling"],
        battery_hours <- 72.0,
        description <- "Vibracao para acalmar (biofeedback). Detecta crise de ansiedade por batimento. R$80-200."),

    // === TERMINAL PUBLICO ===
    HardwareDevice("HW-034", "TV Smart (qualquer)",
        HardwareCategory.TERMINAL_PUBLIC, HardwareCost.MEDIUM, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.WIFI, ConnectionType.HDMI, ConnectionType.BLUETOOTH],
        platforms <- ["Android TV", "Tizen", "webOS"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva", "espectro_autista", "desenvolvimento", "temporaria"],
        input_capabilities <- ["remote", "voice", "bluetooth_keyboard", "camera_optional"],
        output_capabilities <- ["screen_huge", "speaker", "hdmi_out"],
        battery_hours <- 0.0,
        description <- "Todo estabelecimento tem uma TV. OpenTerminal transforma TV ociosa em terminal da Republica."),

    HardwareDevice("HW-035", "Kiosk / Terminal Publico",
        HardwareCategory.TERMINAL_PUBLIC, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.WIFI, ConnectionType.USB],
        platforms <- ["Linux", "Windows"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva", "multipla"],
        input_capabilities <- ["touch", "keypad", "nfc", "camera"],
        output_capabilities <- ["screen_large", "speaker"],
        battery_hours <- 0.0,
        description <- "Terminal em praca, hospital, escola. wheelchair-height. Audio jack para fone."),

    HardwareDevice("HW-036", "Terminal Burro (Raspberry Pi + tela)",
        HardwareCategory.TERMINAL_PUBLIC, HardwareCost.VERY_LOW, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.WIFI, ConnectionType.USB, ConnectionType.AUDIO_JACK, ConnectionType.HDMI],
        platforms <- ["Linux"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva"],
        input_capabilities <- ["keyboard", "usb_switch", "usb_eye_tracker", "bluetooth"],
        output_capabilities <- ["screen", "speaker", "audio_jack"],
        battery_hours <- 0.0,
        description <- "Raspberry Pi R$150 + tela R$100 = terminal completo. OpenKit da Republica."),

    HardwareDevice("HW-037", "Computador Comunitario (biblioteca, escola)",
        HardwareCategory.TERMINAL_PUBLIC, HardwareCost.FREE, HardwareAvailability.COMMON,
        connections <- [ConnectionType.WIFI, ConnectionType.USB, ConnectionType.AUDIO_JACK],
        platforms <- ["Linux", "Windows"],
        disabilities_served <- ["visual", "auditiva", "motora", "cognitiva", "multipla", "temporaria"],
        input_capabilities <- ["keyboard", "mouse", "microphone", "usb_devices"],
        output_capabilities <- ["screen", "speaker", "audio_jack"],
        battery_hours <- 0.0,
        description <- "Zero custo. Disponivel em bibliotecas publicas, telecentros, escola publica."),

    // === VOZ ===
    HardwareDevice("HW-038", "Microfone (dedicado)",
        HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.USB, ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH],
        platforms <- ["Linux", "Windows", "macOS", "Android", "iOS"],
        disabilities_served <- ["motora", "comunicacao"],
        input_capabilities <- ["voice_high_quality", "noise_cancellation"],
        output_capabilities <- [],
        battery_hours <- 0.0,
        description <- "Para dictacao de codigo por voz. Microfone de lapela R$30 = suficiente."),

    HardwareDevice("HW-039", "Camera Web (webcam)",
        HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.USB, ConnectionType.WIFI],
        platforms <- ["Linux", "Windows", "macOS", "Android", "iOS"],
        disabilities_served <- ["motora", "comunicacao", "auditiva"],
        input_capabilities <- ["hand_tracking", "face_tracking", "eye_tracking_basic", "gesture", "sign_language_capture"],
        output_capabilities <- [],
        battery_hours <- 0.0,
        description <- "Gestos de mao, tracking facial, captura de Libras. Webcam R$50 = suficiente."),

    // === INPUT ALTERNATIVO ===
    HardwareDevice("HW-040", "Teclado Braille ( Perkins / eletronico)",
        HardwareCategory.ASSISTIVE_VISUAL, HardwareCost.MEDIUM, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.USB],
        platforms <- ["Android", "iOS", "Windows", "Linux", "macOS"],
        disabilities_served <- ["visual"],
        input_capabilities <- ["braille_input_6_keys", "braille_input_8_keys", "space", "navigation"],
        output_capabilities <- [],
        battery_hours <- 20.0,
        description <- "6-8 teclas para digitar em Braille. Conecta no smartphone. Cego digita codigo direto."),

    HardwareDevice("HW-041", "Ponteiro Laser / Caneta Virtual",
        HardwareCategory.ASSISTIVE_MOTOR, HardwareCost.LOW, HardwareAvailability.SPECIALIZED,
        connections <- [ConnectionType.BLUETOOTH],
        platforms <- ["Windows", "Linux", "Android"],
        disabilities_served <- ["motora"],
        input_capabilities <- ["laser_point", "gesture"],
        output_capabilities <- [],
        battery_hours <- 8.0,
        description <- "Aponta laser na tela de longe. Para quem nao alcanca a tela ou tem tremor."),

    HardwareDevice("HW-042", "Haptic Vest / Colete Tátil",
        HardwareCategory.WEARABLE, HardwareCost.HIGH, HardwareAvailability.EXPERIMENTAL,
        connections <- [ConnectionType.BLUETOOTH, ConnectionType.WIFI],
        platforms <- ["Windows", "Linux", "Android"],
        disabilities_served <- ["visual", "auditiva", "motora"],
        input_capabilities <- [],
        output_capabilities <- ["haptic_array", "vibration_patterns_complex"],
        battery_hours <- 4.0,
        description <- "Vibracoes no corpo representam informacao. Surdo sente musica. Cego sente ambiente."),

    HardwareDevice("HW-043", "Fone de Ouvido Comum",
        HardwareCategory.MASS, HardwareCost.VERY_LOW, HardwareAvailability.UBIQUITOUS,
        connections <- [ConnectionType.AUDIO_JACK, ConnectionType.BLUETOOTH],
        platforms <- ["Standalone"],
        disabilities_served <- ["auditiva", "espectro_autista", "cognitiva"],
        input_capabilities <- ["microphone_optional"],
        output_capabilities <- ["audio", "audio_isolated"],
        battery_hours <- 0.0,
        description <- "Fone comum R$15. Para TTS (cego), isolamento (autista), audio direto (surdo com aparelho)."),
]


// ============================================================================
// 4. MOTOR DE COMPATIBILIDADE
// ============================================================================

classe HardwareCompatibilityEngine:
    // Verifica quais dispositivos sao compativeis com cada deficiencia e necessidade.

    funcao __init__(self):
        self.catalog = {d.device_id: d for d in HARDWARE_CATALOG}

    funcao find_by_disability(self, disability_category: str) retorna List[HardwareDevice]:
        // Encontra dispositivos para uma categoria de deficiencia.
        retorne [d for d in HARDWARE_CATALOG if disability_category in d.disabilities_served]

    funcao find_by_cost(self, max_cost: HardwareCost) retorna List[HardwareDevice]:
        // Encontra dispositivos dentro de um orcamento.
        cost_order <- [
            HardwareCost.FREE,
            HardwareCost.VERY_LOW,
            HardwareCost.LOW,
            HardwareCost.MEDIUM,
            HardwareCost.HIGH,
            HardwareCost.VERY_HIGH,
        ]
        max_idx <- cost_order.index(max_cost)
        retorne [d for d in HARDWARE_CATALOG if cost_order.index(d.cost) <= max_idx]

    funcao find_by_platform(self, platform: str) retorna List[HardwareDevice]:
        // Encontra dispositivos para uma plataforma.
        retorne [d for d in HARDWARE_CATALOG if platform in d.platforms]

    funcao find_by_input_capability(self, capability: str) retorna List[HardwareDevice]:
        // Encontra dispositivos que oferecem uma capacidade de entrada.
        retorne [d for d in HARDWARE_CATALOG if capability in d.input_capabilities]

    funcao find_by_output_capability(self, capability: str) retorna List[HardwareDevice]:
        // Encontra dispositivos que oferecem uma capacidade de saida.
        retorne [d for d in HARDWARE_CATALOG if capability in d.output_capabilities]

    funcao find_offline_capable(self) retorna List[HardwareDevice]:
        // Dispositivos que funcionam sem internet.
        retorne [d for d in HARDWARE_CATALOG if d.offline_capable]

    def recommend_setup(self, disabilities: List[str], budget: HardwareCost = HardwareCost.LOW,
                        declare platform: str  <- "Android") -> List[HardwareDevice]:
        // Recomenda conjunto de hardware para um perfil.
        recommendations <- set()
        para cada disability em disabilities:
            devices <- self.find_by_disability(disability)
            para cada d em devices:
                se platform in d.platforms  OU  NAO  d.platforms entao:
                    recommendations.add(d)
        // Filtrar por orcamento
        budget_devices <- self.find_by_cost(budget)
        final <- [d for d in recommendations if d in budget_devices]
        se NAO  final entao:
            // Se nada no orcamento, retornar gratis/basico
            final <- self.find_by_cost(HardwareCost.FREE) + self.find_by_cost(HardwareCost.VERY_LOW)
        retorne list(set(final))

    funcao total_setup_cost(self, devices: List[HardwareDevice]) retorna Dict[str, Any]:
        // Estima custo total de um setup.
        cost_ranges <- {
            HardwareCost.FREE: (0, 0),
            HardwareCost.VERY_LOW: (1, 100),
            HardwareCost.LOW: (100, 500),
            HardwareCost.MEDIUM: (500, 2000),
            HardwareCost.HIGH: (2000, 10000),
            HardwareCost.VERY_HIGH: (10000, 100000),
            HardwareCost.SUBSIDIZED: (0, 0),
        }
        min_total <- 0
        max_total <- 0
        para cada d em devices:
            desempacote lo, hi <- cost_ranges[d.cost]
            min_total <- min_total + lo
            max_total <- max_total + hi
        retorne {
            "min_brl": min_total,
            "max_brl": max_total,
            "device_count": len(devices),
            "categories": list({d.category.value for d in devices}),
        }


// ============================================================================
// 5. BRIDGE IDE <-> HARDWARE
// ============================================================================

classe HardwareBridge:
    // 
    Ponte entre a OpenInclusiveIDE e o hardware fisico.
    Detecta dispositivos conectados e configura a IDE automaticamente.
    // 

    funcao __init__(self):
        self.connected_devices: List[HardwareDevice] = []
        self.engine = HardwareCompatibilityEngine()
        self.active_inputs: List[str] = []
        self.active_outputs: List[str] = []

    funcao detect_devices(self) retorna List[HardwareDevice]:
        // Detecta dispositivos conectados (simulado).
        // Em producao: escanear Bluetooth, USB, WiFi
        // Por agora: simula smartphone Android como base
        base <- self.engine.catalog.get("HW-001")
        se base entao:
            self.connected_devices = [base]
            self._update_capabilities()
        retorne self.connected_devices

    funcao connect_device(self, device: HardwareDevice) retorna bool:
        // Conecta um dispositivo ao setup.
        se device NAO  in self.connected_devices entao:
            self.connected_devices.append(device)
            self._update_capabilities()
        retorne VERDADEIRO

    funcao disconnect_device(self, device: HardwareDevice) retorna bool:
        // Desconecta um dispositivo.
        se device in self.connected_devices entao:
            self.connected_devices.remove(device)
            self._update_capabilities()
        retorne VERDADEIRO

    funcao _update_capabilities(self) retorna None:
        // Atualiza lista de capacidades ativas baseado nos dispositivos conectados.
        self.active_inputs = []
        self.active_outputs = []
        para cada d em self.connected_devices:
            para cada cap em d.input_capabilities:
                se cap NAO  in self.active_inputs entao:
                    self.active_inputs.append(cap)
            para cada cap em d.output_capabilities:
                se cap NAO  in self.active_outputs entao:
                    self.active_outputs.append(cap)

    funcao available_input_modes(self) retorna List[str]:
        // Lista modos de entrada disponiveis com hardware atual.
        modes <- set()
        para cada d em self.connected_devices:
            se "voice" in d.input_capabilities  OU  "microphone" in d.input_capabilities entao:
                modes.add("voz")
                modes.add("voz_codigo")
            se "touch" in d.input_capabilities  OU  "touch_small" in d.input_capabilities entao:
                modes.add("toque")
            se "keyboard" in d.input_capabilities entao:
                modes.add("teclado_completo")
            se "braille_keys" in d.input_capabilities  OU  "braille_input_6_keys" in d.input_capabilities entao:
                modes.add("teclado_braille")
            se "eye_gaze" in d.input_capabilities entao:
                modes.add("rastreio_olhos")
            se "single_switch" in d.input_capabilities  OU  "dual_switch" in d.input_capabilities entao:
                modes.add("chave")
                modes.add("chave_dupla")
            se "trackball" in d.input_capabilities entao:
                modes.add("trackball")
            se "foot_press_left" in d.input_capabilities entao:
                modes.add("pedal_pe")
            se "head_stick" in d.input_capabilities entao:
                modes.add("teclado_cabeca")
            se "sip_puff" in d.input_capabilities entao:
                modes.add("teclado_boca")
            se "eeg_waves" in d.input_capabilities entao:
                modes.add("interface_cerebral")
            se "neural_spikes" in d.input_capabilities entao:
                modes.add("interface_cerebral")
            se "emg_signal" in d.input_capabilities entao:
                modes.add("eletromiografo")
            se "hand_tracking" in d.input_capabilities entao:
                modes.add("gesto")
            se "heart_rate" in d.input_capabilities entao:
                modes.add("biofeedback")
        retorne sorted(modes)

    funcao available_output_modes(self) retorna List[str]:
        // Lista modos de saida disponiveis com hardware atual.
        modes <- set()
        para cada d em self.connected_devices:
            se "screen" in d.output_capabilities  OU  "screen_large" in d.output_capabilities entao:
                modes.add("texto_visual")
            se "screen_tiny" in d.output_capabilities entao:
                modes.add("texto_tela_pequena")
            se "tts" in d.output_capabilities  OU  "tts_basic" in d.output_capabilities  OU  "speaker" in d.output_capabilities entao:
                modes.add("texto_para_voz")
            se "braille_cells_40" in d.output_capabilities  OU  "braille_cells_14" in d.output_capabilities entao:
                modes.add("display_braille")
            se "vibration" in d.output_capabilities  OU  "haptic" in d.output_capabilities entao:
                modes.add("haptico")
            se "color_light" in d.output_capabilities entao:
                modes.add("luz_cor")
            se "audio_amplified" in d.output_capabilities entao:
                modes.add("audio_amplificado")
            se "audio_anc" in d.output_capabilities entao:
                modes.add("audio_cancelamento_ruido")
            se "hud_overlay" in d.output_capabilities entao:
                modes.add("hud_oculos")
            se "taptic_engine" in d.output_capabilities entao:
                modes.add("taptic_preciso")
        retorne sorted(modes)

    funcao supports_input_mode(self, mode: str) retorna bool:
        retorne mode in self.available_input_modes()

    funcao supports_output_mode(self, mode: str) retorna bool:
        retorne mode in self.available_output_modes()

    funcao session_info(self) retorna Dict[str, Any]:
        retorne {
            "connected_devices": [d.name for d in self.connected_devices],
            "device_count": len(self.connected_devices),
            "available_inputs": self.available_input_modes(),
            "available_outputs": self.available_output_modes(),
            "total_input_capabilities": len(self.active_inputs),
            "total_output_capabilities": len(self.active_outputs),
        }


// ============================================================================
// 6. PERFIS DE SETUP (Quick Configurations)
// ============================================================================

funcao create_setup_budget() retorna List[HardwareDevice]:
    // Setup minimo de baixo custo: smartphone + fone + switch.
    engine <- HardwareCompatibilityEngine()
    retorne [
        engine.catalog["HW-001"],   // Smartphone Android
        engine.catalog["HC-029"],   // Fone ANC
        engine.catalog["HW-018"],   // Switch
    ]


funcao create_setup_blind() retorna List[HardwareDevice]:
    // Setup para desenvolvedor cego.
    engine <- HardwareCompatibilityEngine()
    retorne [
        engine.catalog["HW-001"],    // Smartphone Android (TalkBack)
        engine.catalog["HW-014"],    // Leitor de tela (NVDA/TalkBack)
        engine.catalog["HW-013"],    // Display Braille 40 celulas
        engine.catalog["HW-040"],    // Teclado Braille Perkins
    ]


funcao create_setup_deaf() retorna List[HardwareDevice]:
    // Setup para desenvolvedor surdo.
    engine <- HardwareCompatibilityEngine()
    retorne [
        engine.catalog["HW-001"],    // Smartphone (alertas visuais)
        engine.catalog["HW-006"],    // Smartwatch (vibracao)
        engine.catalog["HC-031"],    // Luz inteligente (notificacao cor)
    ]


funcao create_setup_motor_severe() retorna List[HardwareDevice]:
    // Setup para tetraplegia (eye tracking + voz).
    engine <- HardwareCompatibilityEngine()
    retorne [
        engine.catalog["HW-011"],    // Notebook
        engine.catalog["HW-016"],    // Eye Tracker Tobii
        engine.catalog["HW-038"],    // Microfone (voz)
    ]


funcao create_setup_autism() retorna List[HardwareDevice]:
    // Setup para espectro autista.
    engine <- HardwareCompatibilityEngine()
    retorne [
        engine.catalog["HW-001"],    // Smartphone
        engine.catalog["HC-029"],    // Fone ANC (escudo sensorial)
        engine.catalog["HC-031"],    // Luz inteligente (ambiente calmo)
        engine.catalog["HC-032"],    // Manta ponderada
    ]


funcao create_setup_adhd() retorna List[HardwareDevice]:
    // Setup para TDAH.
    engine <- HardwareCompatibilityEngine()
    retorne [
        engine.catalog["HW-001"],    // Smartphone
        engine.catalog["HC-029"],    // Fone ANC
        engine.catalog["HW-007"],    // Apple Watch (pomodoro, lembrete)
    ]


funcao create_setup_epilepsy() retorna List[HardwareDevice]:
    // Setup para epilepsia.
    engine <- HardwareCompatibilityEngine()
    retorne [
        engine.catalog["HW-001"],    // Smartphone
        engine.catalog["HC-031"],    // Luz inteligente (no flicker)
        engine.catalog["HW-007"],    // Apple Watch (detecta crise)
    ]


funcao create_setup_public_terminal() retorna List[HardwareDevice]:
    // Setup para terminal publico (zero custo).
    engine <- HardwareCompatibilityEngine()
    retorne [
        engine.catalog["HW-037"],    // Computador comunitario
    ]


funcao create_setup_zero_cost() retorna List[HardwareDevice]:
    // Setup ZERO custo.
    engine <- HardwareCompatibilityEngine()
    retorne [
        engine.catalog["HW-037"],    // Computador comunitario (biblioteca)
        engine.catalog["HW-014"],    // NVDA (leitor de tela gratis)
    ]


// ============================================================================
// 7. OQUELMA DE ESCALABILIDADE
// ============================================================================

classe HardwareEscalationLadder:
    // 
    Escada de escalabilidade de hardware.
    Do zero custo ao setup profissional, cada degrau adiciona capacidade.
    // 

    RUNGS <- [
        ("Degrau 0: ZERO CUSTO", create_setup_zero_cost, "Biblioteca publica + NVDA gratis. Todo mundo comeca aqui."),
        ("Degrau 1: SMARTPHONE", create_setup_budget, "Smartphone R$300 + fone R$50 + switch R$30. Acesse de qualquer lugar."),
        ("Degrau 2: TABLET/WEARABLE", create_setup_deaf, "Adiciona smartwatch/luz para feedback multimodal."),
        ("Degrau 3: ASSISTIVO ESPECIFICO", create_setup_blind, "Adiciona braille/eye-tracker especifico para deficiencia."),
        ("Degrau 4: SETUP COMPLETO", create_setup_motor_severe, "Notebook + eye-tracker + microfone. Desenvolvimento profissional."),
        ("Degrau 5: BCI/EXPERIMENTAL", nulo, "BCI, haptic vest, smart glasses. Fronteira da tecnologia."),
    ]

    // decorador: @classmethod
    funcao recommend_rung(cls, budget: HardwareCost) retorna Tuple[int, str]:
        // Recomenda degrau baseado em orcamento.
        se budget == HardwareCost.FREE entao:
            retorne 0, cls.RUNGS[0][2]
        senao se budget in (HardwareCost.VERY_LOW, HardwareCost.LOW) entao:
            retorne 1, cls.RUNGS[1][2]
        senao se budget == HardwareCost.MEDIUM entao:
            retorne 2, cls.RUNGS[2][2]
        senao se budget == HardwareCost.HIGH entao:
            retorne 3, cls.RUNGS[3][2]
        senao se budget == HardwareCost.VERY_HIGH entao:
            retorne 5, cls.RUNGS[5][2]
        retorne 0, cls.RUNGS[0][2]

    // decorador: @classmethod
    funcao show_ladder(cls) retorna None:
        print("\nESCALADA DE HARDWARE -- Do Zero ao Profissional")
        print("=" * 60)
        for i, (name, func, desc) in enumerate(cls.RUNGS):
            se func entao:
                setup <- func()
                engine <- HardwareCompatibilityEngine()
                cost <- engine.total_setup_cost(setup)
                print(f"\n  {name}")
                print(f"    {desc}")
                print(f"    Custo: R$ {cost['min_brl']}-{cost['max_brl']}")
                print(f"    Devices: {cost['device_count']}")
            senao:
                print(f"\n  {name}")
                print(f"    {desc}")


// ============================================================================
// 8. DEMONSTRACAO
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel")
    print("=" * 70)

    engine <- HardwareCompatibilityEngine()

    // Catalogo
    print(f"\nCatalogo: {len(HARDWARE_CATALOG)} dispositivos mapeados")
    cats <- defaultdict(int)
    para cada d em HARDWARE_CATALOG:
        cats[d.category.value] += 1
    para cada (cat, count) em sorted(cats.items()):
        print(f"  {cat:25} {count:3} dispositivos")

    // Por custo
    print(f"\nPor custo:")
    costs <- defaultdict(int)
    para cada d em HARDWARE_CATALOG:
        costs[d.cost.value] += 1
    para cada (cost, count) em sorted(costs.items()):
        print(f"  {cost:15} {count:3} dispositivos")

    // Por disponibilidade
    print(f"\nPor disponibilidade:")
    avail <- defaultdict(int)
    para cada d em HARDWARE_CATALOG:
        avail[d.availability.value] += 1
    para cada (a, count) em sorted(avail.items()):
        print(f"  {a:15} {count:3} dispositivos")

    // Bridge demo
    print(f"\n{'=' * 70}")
    print("HARDWARE BRIDGE -- Deteccao e Configuracao")
    print(f"{'=' * 70}")

    bridge <- HardwareBridge()
    detected <- bridge.detect_devices()
    print(f"\nDispositivos detectados: {[d.name for d in detected]}")
    info <- bridge.session_info()
    print(f"Inputs disponiveis:  {info['available_inputs']}")
    print(f"Outputs disponiveis: {info['available_outputs']}")

    // Conectar braille display
    print("\n+ Conectando Display Braille...")
    bridge.connect_device(engine.catalog["HW-013"])
    info <- bridge.session_info()
    print(f"Inputs:  {info['available_inputs']}")
    print(f"Outputs: {info['available_outputs']}")

    // Conectar eye tracker
    print("\n+ Conectando Eye Tracker...")
    bridge.connect_device(engine.catalog["HW-016"])
    info <- bridge.session_info()
    print(f"Inputs:  {info['available_inputs']}")
    print(f"Outputs: {info['available_outputs']}")

    // Conectar smartwatch
    print("\n+ Conectando Smartwatch...")
    bridge.connect_device(engine.catalog["HW-006"])
    info <- bridge.session_info()
    print(f"Inputs:  {info['available_inputs']}")
    print(f"Outputs: {info['available_outputs']}")

    // Perfis de setup
    print(f"\n{'=' * 70}")
    print("PERFIS DE SETUP")
    print(f"{'=' * 70}")

    setups <- {
        "ZERO CUSTO (biblioteca)": create_setup_zero_cost(),
        "BAIXO CUSTO (smartphone)": create_setup_budget(),
        "CEGO (braille completo)": create_setup_blind(),
        "SURDO (visual+haptic)": create_setup_deaf(),
        "TETRAPLEGICO (eye+voz)": create_setup_motor_severe(),
        "AUTISTA (calmo)": create_setup_autism(),
        "TDAH (foco)": create_setup_adhd(),
        "EPILEPSIA (seguro)": create_setup_epilepsy(),
        "TERMINAL PUBLICO": create_setup_public_terminal(),
    }

    para cada (label, setup) em setups.items():
        cost <- engine.total_setup_cost(setup)
        print(f"\n  {label}")
        print(f"    Devices: {cost['device_count']} | Custo: R$ {cost['min_brl']}-{cost['max_brl']}")
        para cada d em setup:
            print(f"      - {d.name}")

    // Escada de escalabilidade
    HardwareEscalationLadder.show_ladder()

    // Cobertura
    print(f"\n{'=' * 70}")
    print("COBERTURA DE CATEGORIAS")
    print(f"{'=' * 70}")
    para cada cat em HardwareCategory:
        devices <- [d for d in HARDWARE_CATALOG if d.category == cat]
        print(f"  {cat.value:25} {len(devices):3} dispositivos")

    // Cobertura por deficiencia
    print(f"\nCOBERTURA POR DEFICIENCIA:")
    all_disabilities <- set()
    para cada d em HARDWARE_CATALOG:
        all_disabilities.update(d.disabilities_served)
    para cada disab em sorted(all_disabilities):
        devices <- engine.find_by_disability(disab)
        print(f"  {disab:25} {len(devices):3} dispositivos")

    print(f"\nTotal dispositivos: {len(HARDWARE_CATALOG)}")
    print(f"Categorias: {len(HardwareCategory)}")
    print(f"Setup minimo: R$ 0 (biblioteca + NVDA gratis)")
    print(f"\nTODO hardware. TODA deficiencia. ZERO barreira.")


se __name__ == "__main__" entao:
    demo()

```
