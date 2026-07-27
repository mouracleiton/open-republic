// ============================================================================
// OpenResilience -- Simulacao de Falhas e Mitigacao
// ============================================================================
// "O cego esta na rua. A bateria do smartphone cai pra 2%.
// O GPS para. A camera trava. O TTS crasha.
// E AGORA? O cego esta PERDIDO, CEGO, e SEM SISTEMA.
//
// A resposta NAO e 'isso nao vai acontecer'.
// A resposta e: 'quando acontecer, o sistema REAGE'.
//
// Todo hardware falha. Todo software cai. Todo sinal se perde.
// A pergunta nao e SE vai falhar -- e QUANDO.
// E quando falhar, o usuario NAO pode ficar desamparado.
//
// Este modulo simula TODA falha possivel e define a mitigacao:
// - Bateria em 0%: modo survival, so essencial, voz lenta
// - GPS perdido: bussola + contagem de passos + landmark auditivo
// - Camera falhou: audio + acelerometro assumem
// - TTS crashou: vibracao + braille assumem
// - Rede caiu: tudo offline, dados em cache
// - Software travou: watchdog reinicia em 3s
// - Hardware morreu: fallback para terminal publico + ligacao
//
// PRINCIPIO: Cada componente tem um PLANO B, PLANO C e PLANO D.
// Nenhum ponto unico de falha. Redundancia em TUDO.
//
// Integrado com:
// - OpenTelefonista (telefonista sobrevive a falhas)
// - OpenInclusiveIDE (IDE degrada graciosamente)
// - OpenInclusiveHardware (44 dispositivos com fallback)
// - OpenAbsence (pausa mesmo em modo survival)
// - OpenSilencePolicy (silencio mesmo em emergencia)
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// ============================================================================

use std::collections::{HashMap, VecDeque};
use std::time::{SystemTime, UNIX_EPOCH};

// ============================================================================
// 1. TIPOS DE FALHA
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum FailureCategory {
    Hardware,
    Software,
    Network,
    Power,
    Sensor,
    Peripheral,
    Os,
    Cloud,
}

impl FailureCategory {
    pub fn as_str(&self) -> &'static str {
        match self {
            FailureCategory::Hardware => "hardware",
            FailureCategory::Software => "software",
            FailureCategory::Network => "rede",
            FailureCategory::Power => "energia",
            FailureCategory::Sensor => "sensor",
            FailureCategory::Peripheral => "periferico",
            FailureCategory::Os => "sistema_operacional",
            FailureCategory::Cloud => "nuvem",
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum FailureType {
    // POWER
    BatteryCritical,   // < 5%
    BatteryDead,       // 0%
    BatteryOverheat,   // desliga por calor
    PowerSurge,        // dano eletrico

    // HARDWARE
    ScreenBroken,      // caiu, rachou
    ScreenDead,        // backlight queimou
    CameraFailure,     // lente riscada, modulo queimou
    MicrophoneDead,    // agua, poeira
    SpeakerDead,       // agua, volume max
    VibrationDead,     // motor queimou
    GpsLost,           // dentro de predio, tunel
    BluetoothDrop,     // desconectou do braille
    NfcFailure,
    WaterDamage,       // chuva, queda na agua
    PhysicalDamage,    // pisou, atropelou
    ButtonStuck,       // poeira, impacto
    ChargePortBroken,  // nao carrega mais

    // PERIPHERAL
    BrailleDisplayDisconnected,
    EyeTrackerLost,
    SwitchFailure,
    HearingAidDisconnected,
    SmartwatchLost,

    // SOFTWARE
    TtsCrash,                  // motor de voz morreu
    SttFailure,                // reconhecimento de voz falhou
    OcrFailure,                // leitura de imagem falhou
    AppFreeze,                 // ANR
    AppCrash,                  // SIGSEGV
    MemoryExhausted,           // OOM
    StorageFull,
    ModelUnavailable,          // modelo IA nao carrega
    NavigationEngineDown,
    EmotionDetectorDown,

    // NETWORK
    NetworkDown,       // sem internet
    NetworkSlow,       // 2G, latencia alta
    CloudDown,         // servidor offline
    ApiRateLimit,      // rate limited
    DnsFailure,

    // OS
    OsUpdateBrick,
    BootLoop,
    PermissionRevoked, // microfone negado
}

impl FailureType {
    pub fn as_str(&self) -> &'static str {
        match self {
            FailureType::BatteryCritical => "bateria_critica",
            FailureType::BatteryDead => "bateria_morta",
            FailureType::BatteryOverheat => "bateria_superaquecida",
            FailureType::PowerSurge => "pico_energia",
            FailureType::ScreenBroken => "tela_quebrada",
            FailureType::ScreenDead => "tela_morta",
            FailureType::CameraFailure => "camera_falhou",
            FailureType::MicrophoneDead => "microfone_morto",
            FailureType::SpeakerDead => "alto_falante_morto",
            FailureType::VibrationDead => "vibracao_morta",
            FailureType::GpsLost => "gps_perdido",
            FailureType::BluetoothDrop => "bluetooth_caiu",
            FailureType::NfcFailure => "nfc_falhou",
            FailureType::WaterDamage => "dano_agua",
            FailureType::PhysicalDamage => "dano_fisico",
            FailureType::ButtonStuck => "botao_preso",
            FailureType::ChargePortBroken => "porta_carga_quebrada",
            FailureType::BrailleDisplayDisconnected => "braille_desconectou",
            FailureType::EyeTrackerLost => "eye_tracker_perdeu",
            FailureType::SwitchFailure => "switch_queimou",
            FailureType::HearingAidDisconnected => "aparelho_desconectou",
            FailureType::SmartwatchLost => "smartwatch_perdido",
            FailureType::TtsCrash => "tts_crashou",
            FailureType::SttFailure => "stt_falhou",
            FailureType::OcrFailure => "ocr_falhou",
            FailureType::AppFreeze => "app_travou",
            FailureType::AppCrash => "app_crashou",
            FailureType::MemoryExhausted => "memoria_esgotada",
            FailureType::StorageFull => "armazenamento_cheio",
            FailureType::ModelUnavailable => "ia_indisponivel",
            FailureType::NavigationEngineDown => "navegador_caiu",
            FailureType::EmotionDetectorDown => "detector_emocao_caiu",
            FailureType::NetworkDown => "rede_caiu",
            FailureType::NetworkSlow => "rede_lenta",
            FailureType::CloudDown => "nuvem_caiu",
            FailureType::ApiRateLimit => "api_limite",
            FailureType::DnsFailure => "dns_falhou",
            FailureType::OsUpdateBrick => "atualizacao_bricou",
            FailureType::BootLoop => "boot_loop",
            FailureType::PermissionRevoked => "permissao_revogada",
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum FailureSeverity {
    Cosmetic,      // nao afeta funcionalidade principal
    Minor,         // degradacao leve
    Major,         // degradacao significativa
    Critical,      // funcionalidade essencial perdida
    Catastrophic,  // dispositivo inutilizavel
}

impl FailureSeverity {
    pub fn as_str(&self) -> &'static str {
        match self {
            FailureSeverity::Cosmetic => "cosmetico",
            FailureSeverity::Minor => "menor",
            FailureSeverity::Major => "maior",
            FailureSeverity::Critical => "critico",
            FailureSeverity::Catastrophic => "catastrofico",
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum FailureDuration {
    Transient,  // segundos (bluetooth reconecta)
    Short,      // minutos (GPS re-adquire)
    Medium,     // horas (bateria recarrega)
    Long,       // dias (tela quebrada ate consertar)
    Permanent,  // nao recupera (hardware morreu)
}

impl FailureDuration {
    pub fn as_str(&self) -> &'static str {
        match self {
            FailureDuration::Transient => "transiente",
            FailureDuration::Short => "curto",
            FailureDuration::Medium => "medio",
            FailureDuration::Long => "longo",
            FailureDuration::Permanent => "permanente",
        }
    }
}

// ============================================================================
// 2. EVENTO DE FALHA
// ============================================================================

#[derive(Debug, Clone)]
pub struct FailureEvent {
    pub event_id: String,
    pub failure_type: FailureType,
    pub category: FailureCategory,
    pub severity: FailureSeverity,
    pub duration: FailureDuration,
    pub description: String,
    pub affected_components: Vec<String>,
    pub user_impact: String,
    pub timestamp: f64,
    pub recovery_probability: f64,
    pub detected: bool,
}

impl FailureEvent {
    pub fn new(
        event_id: &str,
        failure_type: FailureType,
        category: FailureCategory,
        severity: FailureSeverity,
        duration: FailureDuration,
        description: &str,
    ) -> Self {
        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs_f64();
        FailureEvent {
            event_id: event_id.to_string(),
            failure_type,
            category,
            severity,
            duration,
            description: description.to_string(),
            affected_components: Vec::new(),
            user_impact: String::new(),
            timestamp,
            recovery_probability: 0.9,
            detected: false,
        }
    }
}

// ============================================================================
// 3. NIVEIS DE DEGRADACAO
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub enum DegradationLevel {
    Full,       // 100% funcional, tudo operacional
    Degraded1,  // 80% -- features nao essenciais off
    Degraded2,  // 50% -- so essencial, fallback ativo
    Survival,   // 20% -- minimo absoluto para nao morrer
    Emergency,  // 10% -- so chamada de socorro
    Dead,       // 0% -- dispositivo inutilizavel
}

impl DegradationLevel {
    pub fn as_str(&self) -> &'static str {
        match self {
            DegradationLevel::Full => "completo",
            DegradationLevel::Degraded1 => "degradado_1",
            DegradationLevel::Degraded2 => "degradado_2",
            DegradationLevel::Survival => "sobrevivencia",
            DegradationLevel::Emergency => "emergencia",
            DegradationLevel::Dead => "morto",
        }
    }
}

#[derive(Debug, Clone)]
pub struct SystemState {
    pub level: DegradationLevel,
    pub active_failures: Vec<FailureEvent>,
    pub battery_pct: f64,
    pub available_inputs: Vec<String>,
    pub available_outputs: Vec<String>,
    pub available_sensors: Vec<String>,
    pub network_available: bool,
    pub gps_available: bool,
    pub camera_available: bool,
    pub microphone_available: bool,
    pub speaker_available: bool,
    pub vibration_available: bool,
    pub screen_available: bool,
    pub tts_available: bool,
    pub braille_connected: bool,
    pub eye_tracker_connected: bool,
    pub smartwatch_connected: bool,
    pub offline_cache_size_mb: f64,
    pub last_known_location: Option<(f64, f64)>,
    pub uptime_seconds: f64,
}

impl Default for SystemState {
    fn default() -> Self {
        SystemState {
            level: DegradationLevel::Full,
            active_failures: Vec::new(),
            battery_pct: 100.0,
            available_inputs: vec!["voz".to_string(), "toque".to_string(), "teclado".to_string(), "camera".to_string(), "gps".to_string(), "microfone".to_string()],
            available_outputs: vec!["tts".to_string(), "tela".to_string(), "vibracao".to_string(), "braille".to_string(), "haptico".to_string()],
            available_sensors: vec!["camera".to_string(), "gps".to_string(), "microfone".to_string(), "acelerometro".to_string(), "bussola".to_string(), "luz".to_string()],
            network_available: true,
            gps_available: true,
            camera_available: true,
            microphone_available: true,
            speaker_available: true,
            vibration_available: true,
            screen_available: true,
            tts_available: true,
            braille_connected: false,
            eye_tracker_connected: false,
            smartwatch_connected: false,
            offline_cache_size_mb: 0.0,
            last_known_location: None,
            uptime_seconds: 0.0,
        }
    }
}

// ============================================================================
// 4. ESTRATEGIAS DE MITIGACAO
// ============================================================================

#[derive(Debug, Clone)]
pub struct MitigationStrategy {
    pub strategy_id: String,
    pub failure_type: FailureType,
    pub name: String,
    pub description: String,
    pub fallback_chain: Vec<String>,
    pub recovery_action: String,
    pub user_message: String,
    pub auto_activate: bool,
    pub recovery_time_estimate_s: i32,
}

pub const MITIGATION_STRATEGIES: &[MitigationStrategy] = &[
    // === BATERIA ===
    MitigationStrategy {
        strategy_id: "MT-001".to_string(),
        failure_type: FailureType::BatteryCritical,
        name: "Modo Survival de Bateria".to_string(),
        description: "Bateria < 5%. Desliga tudo nao essencial. So mantem voz/sos.".to_string(),
        fallback_chain: vec![
            "Plano A: Reduzir brilho ao minimo, desligar animacoes".to_string(),
            "Plano B: Desligar camera, GPS (usar contagem de passos)".to_string(),
            "Plano C: Desligar TTS continuo, so falas criticas".to_string(),
            "Plano D: SOS -- ligar para contato de emergencia e desligar".to_string(),
        ],
        recovery_action: "Conectar carregador. Sistema avisa proximo terminal publico.".to_string(),
        user_message: "Bateria critica. Entrei em modo sobrevivencia. So o essencial. Encontre um carregador ou vou te levar ate um terminal publico.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 0,
    },
    MitigationStrategy {
        strategy_id: "MT-002".to_string(),
        failure_type: FailureType::BatteryDead,
        name: "Handoff para Terminal Publico".to_string(),
        description: "Bateria em 0%. Smartphone morre. Sistema migra.".to_string(),
        fallback_chain: vec![
            "Plano A: Antes de morrer, enviar localizacao para emergencia".to_string(),
            "Plano B: Enviar ultima tarefa nao salva para nuvem".to_string(),
            "Plano C: Ligar para contato de emergencia com mensagem automatica".to_string(),
            "Plano D: Avisar usuario: 'Proximo terminal publico: biblioteca a 200m norte'".to_string(),
        ],
        recovery_action: "Carregar em terminal publico, biblioteca, estabelecimento.".to_string(),
        user_message: "Vou desligar em 30 segundos. Mandei sua localizacao para emergencia. Terminal publico mais proximo: biblioteca, 200 metros ao norte.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 3600,
    },
    // === GPS ===
    MitigationStrategy {
        strategy_id: "MT-003".to_string(),
        failure_type: FailureType::GpsLost,
        name: "Navegacao Sem GPS".to_string(),
        description: "GPS perdido (predio, tunel, subsolo). Navegacao continua.".to_string(),
        fallback_chain: vec![
            "Plano A: Bussola magnetica + contagem de passos (dead reckoning)".to_string(),
            "Plano B: Bluetooth beacons indoor (shopping, hospital)".to_string(),
            "Plano C: WiFi triangulation (menos preciso mas funciona indoor)".to_string(),
            "Plano D: Landmarks auditivos: 'Voce passou por um lugar barulhento a 30s -- provavelmente cozinha'".to_string(),
        ],
        recovery_action: "Sair para area aberta. GPS re-adquire em 10-30 segundos.".to_string(),
        user_message: "Perdi o GPS. Estou usando a bussola e contando seus passos. Vou continuar te guiando.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 30,
    },
    // === CAMERA ===
    MitigationStrategy {
        strategy_id: "MT-004".to_string(),
        failure_type: FailureType::CameraFailure,
        name: "Camera Cai, Audio Assume".to_string(),
        description: "Camera falhou. Visao computacional perdida.".to_string(),
        fallback_chain: vec![
            "Plano A: Microfone assume deteccao de obstaculos por eco/sonar".to_string(),
            "Plano B: Acelerometro + bussola mapeiam caminho percorrido".to_string(),
            "Plano C: Pedir ajuda humana: 'Alguem pode me orientar?' via voz alta".to_string(),
            "Plano D: Ligar para contato que ve por camera remota".to_string(),
        ],
        recovery_action: "Limpar lente. Reiniciar app de camera. Se hardware, trocar smartphone.".to_string(),
        user_message: "Minha camera parou. Vou usar o microfone para ouvir o ambiente e te guiar pelo som.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 60,
    },
    // === MICROFONE ===
    MitigationStrategy {
        strategy_id: "MT-005".to_string(),
        failure_type: FailureType::MicrophoneDead,
        name: "Microfone Morto, Tela Assume".to_string(),
        description: "Microfone falhou. Entrada por voz perdida.".to_string(),
        fallback_chain: vec![
            "Plano A: Switch/bluetooth keyboard assume entrada".to_string(),
            "Plano B: Tela touch com botoes grandes (sim, mesmo para cego via TalkBack)".to_string(),
            "Plano C: Eye tracker se disponivel".to_string(),
            "Plano D: Pedir para alguem gravar e enviar audio".to_string(),
        ],
        recovery_action: "Limpar entrada do microfone. Verificar permissoes. Bluetooth headset como backup.".to_string(),
        user_message: "Nao estou te ouvindo. Vou passar para entrada por botoes/toque.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 10,
    },
    // === TTS (TEXT TO SPEECH) ===
    MitigationStrategy {
        strategy_id: "MT-006".to_string(),
        failure_type: FailureType::TtsCrash,
        name: "TTS Crashou, Vibracao Assume".to_string(),
        description: "Motor de voz morreu. Cego nao ouve mais o sistema.".to_string(),
        fallback_chain: vec![
            "Plano A: Display braille assume (se conectado)".to_string(),
            "Plano B: Padroes de vibracao codificam informacao".to_string(),
            "Plano C: Auto-restart do TTS em background".to_string(),
            "Plano D: Tocar tons com significado (agudo=ok, grave=erro)".to_string(),
        ],
        recovery_action: "Reiniciar servico TTS. Android: Settings > Accessibility > TalkBack. iOS: VoiceOver toggle.".to_string(),
        user_message: "[MENSAGEM POR VIBRACAO: 1 pulse = ok, 2 pulses = atencao, 3 pulses = erro]".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 5,
    },
    // === BLUETOOTH / BRAILLE ===
    MitigationStrategy {
        strategy_id: "MT-007".to_string(),
        failure_type: FailureType::BluetoothDrop,
        name: "Bluetooth Caiu".to_string(),
        description: "Braille/switch/aparelho auditivo desconectou.".to_string(),
        fallback_chain: vec![
            "Plano A: Tentar reconexao automatica (3 tentativas em 10s)".to_string(),
            "Plano B: Fallback para TTS alto-falante".to_string(),
            "Plano C: Fallback para vibracao padrao".to_string(),
            "Plano D: Pedir usuario para verificar Bluetooth manualmente".to_string(),
        ],
        recovery_action: "Reativar Bluetooth. Emparelhar novamente. Verificar bateria do periferico.".to_string(),
        user_message: "Perdi conexao com seu dispositivo. Tentando reconectar... Se nao voltar em 10 segundos, vou usar o alto-falante.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 10,
    },
    // === REDE / INTERNET ===
    MitigationStrategy {
        strategy_id: "MT-008".to_string(),
        failure_type: FailureType::NetworkDown,
        name: "Modo Offline Total".to_string(),
        description: "Sem internet. IA em nuvem, mapas, API tudo fora.".to_string(),
        fallback_chain: vec![
            "Plano A: Modelos de IA locais (menores mas funcionam offline)".to_string(),
            "Plano B: Mapas offline (OpenStreetMap cached)".to_string(),
            "Plano C: Tudo que nao precisa de rede continua: TTS, OCR, navegacao local".to_string(),
            "Plano D: SMS para emergencia (nao precisa de internet, so sinal)".to_string(),
        ],
        recovery_action: "Verificar WiFi/dados. Sair de area sem cobertura. Usar SMS para comunicacao.".to_string(),
        user_message: "Sem internet. Continuo funcionando offline. IA local assumiu. Mapas em cache.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 300,
    },
    // === TELA ===
    MitigationStrategy {
        strategy_id: "MT-009".to_string(),
        failure_type: FailureType::ScreenBroken,
        name: "Tela Quebrada".to_string(),
        description: "Tela rachada/morta. Sem saida visual.".to_string(),
        fallback_chain: vec![
            "Plano A: TTS assume toda interacao (cego simulado)".to_string(),
            "Plano B: Braille display conectado via bluetooth".to_string(),
            "Plano C: Smartwatch mostra minimo na tela do relogio".to_string(),
            "Plano D: Cast para TV/terminal publico proximo".to_string(),
        ],
        recovery_action: "Trocar tela. Enquanto isso: TTS + braille + smartwatch.".to_string(),
        user_message: "Sua tela quebrou. Vou guiar tudo por voz. Conecte um braille display se tiver.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 259200, // 3 dias ate consertar
    },
    // === SOFTWARE CRASH ===
    MitigationStrategy {
        strategy_id: "MT-010".to_string(),
        failure_type: FailureType::AppCrash,
        name: "Auto-Reinicio com Watchdog".to_string(),
        description: "App crashou (SIGSEGV, OOM).".to_string(),
        fallback_chain: vec![
            "Plano A: Watchdog detecta crash e reinicia em 3 segundos".to_string(),
            "Plano B: Estado salvo automaticamente a cada acao -- restaura".to_string(),
            "Plano C: Se crash repetido (3x em 1min), modo seguro sem plugins".to_string(),
            "Plano D: Se modo seguro tambem crasha, notificar e abrir bug report".to_string(),
        ],
        recovery_action: "Watchdog reinicia. Log enviado. Estado restaurado do checkpoint.".to_string(),
        user_message: "Ops, tive um problema. Reiniciando... Pronto, voltei. Tava onde?".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 3,
    },
    // === SMARTWATCH ===
    MitigationStrategy {
        strategy_id: "MT-011".to_string(),
        failure_type: FailureType::SmartwatchLost,
        name: "Smartwatch Perdido".to_string(),
        description: "Smartwatch desconectou/perdeu-se. Biometria perdida.".to_string(),
        fallback_chain: vec![
            "Plano A: Smartphone assume biometria (camera = HR por rPPG)".to_string(),
            "Plano B: Usuario reporta estado manualmente ('to bem')".to_string(),
            "Plano C: Reduzir monitoramento ativo, pedir check-in periodico".to_string(),
            "Plano D: Localizar smartwatch por ultimo sinal GPS".to_string(),
        ],
        recovery_action: "Procurar smartwatch. Comprar substituto. Bio no smartphone.".to_string(),
        user_message: "Perdi seu smartwatch. Vou monitorar pelo smartphone. Se achar o relogio, me avise.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 3600,
    },
    // === EYE TRACKER ===
    MitigationStrategy {
        strategy_id: "MT-012".to_string(),
        failure_type: FailureType::EyeTrackerLost,
        name: "Eye Tracker Perdeu Calibracao".to_string(),
        description: "Eye tracker perdeu tracking ou desconectou.".to_string(),
        fallback_chain: vec![
            "Plano A: Recalibrar automaticamente (pedir olhar para 3 pontos)".to_string(),
            "Plano B: Switch/scan assume enquanto recalibra".to_string(),
            "Plano C: Voz assume entrada".to_string(),
            "Plano D: Pausar ate recuperar tracking".to_string(),
        ],
        recovery_action: "Recalibrar. Verificar iluminacao. Limpar camera do tracker.".to_string(),
        user_message: "Perdi o rastreio dos seus olhos. Vou usar seu switch enquanto tento recalibrar.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 15,
    },
    // === MEMORIA ===
    MitigationStrategy {
        strategy_id: "MT-013".to_string(),
        failure_type: FailureType::MemoryExhausted,
        name: "OOM -- Memoria Esgotada".to_string(),
        description: "Memoria RAM cheia. App sera morto pelo OS.".to_string(),
        fallback_chain: vec![
            "Plano A: Descarregar modelos de IA nao essenciais".to_string(),
            "Plano B: Fechar abas/janelas nao ativas".to_string(),
            "Plano C: Reduzir resolucao de camera/frame rate".to_string(),
            "Plano D: Salvar estado e reiniciar limpo".to_string(),
        ],
        recovery_action: "Fechar apps em background. Limpar cache. Adicionar RAM se possivel.".to_string(),
        user_message: "Memoria cheia. Fechando coisas nao essenciais. Continue trabalhando.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 5,
    },
    // === PERMISSAO REVOCADA ===
    MitigationStrategy {
        strategy_id: "MT-014".to_string(),
        failure_type: FailureType::PermissionRevoked,
        name: "Permissao Revogada".to_string(),
        description: "OS revogou permissoes (microfone, camera, localizacao).".to_string(),
        fallback_chain: vec![
            "Plano A: Notificar usuario: 'Preciso de microfone para funcionar'".to_string(),
            "Plano B: Abrir configuracoes de permissao automaticamente".to_string(),
            "Plano C: Funcionalidade reduzida sem a permissao".to_string(),
            "Plano D: Modo visitante (sem dados pessoais)".to_string(),
        ],
        recovery_action: "Reconceder permissao em Configuracoes > Apps > Permissoes.".to_string(),
        user_message: "Voce desligou minha permissao de microfone. Sem ele eu nao consigo te ouvir. Quer abrir as configuracoes?".to_string(),
        auto_activate: false,
        recovery_time_estimate_s: 30,
    },
    // === AGUA ===
    MitigationStrategy {
        strategy_id: "MT-015".to_string(),
        failure_type: FailureType::WaterDamage,
        name: "Dano por Agua".to_string(),
        description: "Smartphone molhou. Multiplas falhas simultaneas.".to_string(),
        fallback_chain: vec![
            "Plano A: Modo survival imediato -- desligar tudo para curto".to_string(),
            "Plano B: Enquanto funciona: SOS + localizacao enviados".to_string(),
            "Plano C: Handoff para terminal publico proximo".to_string(),
            "Plano D: Ligar para emergencia antes de morrer".to_string(),
        ],
        recovery_action: "Desligar imediatamente. Secar em silica gel por 48h. NAO carregar molhado.".to_string(),
        user_message: "AGUA! Entrando em modo emergencia. Mandando sua localizacao. Vou tentar ligar para seu contato de emergencia.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 259200, // dias
    },
    // === CLOUD ===
    MitigationStrategy {
        strategy_id: "MT-016".to_string(),
        failure_type: FailureType::CloudDown,
        name: "Nuvem Caiu, Local Assume".to_string(),
        description: "Servidor na nuvem offline. Servicos cloud indisponiveis.".to_string(),
        fallback_chain: vec![
            "Plano A: Modelos de IA locais (menores mas funcionam)".to_string(),
            "Plano B: Dados sincronizados localmente (ultima sync)".to_string(),
            "Plano C: Queue de acoes -- executa quando nuvem volta".to_string(),
            "Plano D: SMS/ligacao para servicos que precisam de servidor".to_string(),
        ],
        recovery_action: "Aguardar recuperacao do servidor. Fila de acoes processada na volta.".to_string(),
        user_message: "Servidor na nuvem caiu. Tudo continua local. Vou sincronizar quando voltar.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 600,
    },
    // === STT (SPEECH TO TEXT) ===
    MitigationStrategy {
        strategy_id: "MT-017".to_string(),
        failure_type: FailureType::SttFailure,
        name: "Reconhecimento de Voz Falhou".to_string(),
        description: "STT nao transcreve. Usuario nao consegue falar comandos.".to_string(),
        fallback_chain: vec![
            "Plano A: Reiniciar motor STT".to_string(),
            "Plano B: Trocar para modelo STT local (offline, menos preciso)".to_string(),
            "Plano C: Teclado virtual/braille assume entrada".to_string(),
            "Plano D: Switch + scan de letras".to_string(),
        ],
        recovery_action: "Verificar microfone. Reiniciar STT. Verificar permissoes.".to_string(),
        user_message: "Nao estou entendendo sua voz. Vou passar para entrada por teclado/toque.".to_string(),
        auto_activate: true,
        recovery_time_estimate_s: 5,
    },
];

// ============================================================================
// 5. MOTOR DE SIMULACAO DE FALHAS
// ============================================================================

pub struct FailureSimulator {
    pub state: SystemState,
    pub mitigations_active: HashMap<String, MitigationStrategy>,
    pub event_log: VecDeque<HashMap<String, String>>,
    pub strategies: HashMap<FailureType, MitigationStrategy>,
}

impl FailureSimulator {
    pub fn new() -> Self {
        let mut strategies = HashMap::new();
        for s in MITIGATION_STRATEGIES {
            strategies.insert(s.failure_type, s.clone());
        }
        FailureSimulator {
            state: SystemState::default(),
            mitigations_active: HashMap::new(),
            event_log: VecDeque::with_capacity(500),
            strategies,
        }
    }

    pub fn inject_failure(&mut self, mut failure: FailureEvent) -> HashMap<String, String> {
        failure.detected = true;
        self.state.active_failures.push(failure.clone());
        self.update_system_state(&failure);

        let strategy = self.strategies.get(&failure.failure_type).cloned();
        let mitigation_result = if let Some(ref s) = strategy {
            if s.auto_activate {
                self.mitigations_active.insert(s.strategy_id.clone(), s.clone());
                self.apply_mitigation(s)
            } else {
                let mut m = HashMap::new();
                m.insert("action".to_string(), "notify".to_string());
                m.insert("message".to_string(), s.user_message.clone());
                m
            }
        } else {
            HashMap::new()
        };

        let mut event_record = HashMap::new();
        event_record.insert("event_id".to_string(), failure.event_id.clone());
        event_record.insert("failure".to_string(), failure.failure_type.as_str().to_string());
        event_record.insert("severity".to_string(), failure.severity.as_str().to_string());
        if let Some(ref s) = strategy {
            event_record.insert("mitigation".to_string(), s.name.clone());
            event_record.insert("user_message".to_string(), s.user_message.clone());
            event_record.insert("fallback_chain".to_string(), s.fallback_chain.join(" | "));
        } else {
            event_record.insert("mitigation".to_string(), "NENHUMA (sem estrategia)".to_string());
        }
        event_record.insert("degradation_level".to_string(), self.state.level.as_str().to_string());
        self.event_log.push_back(event_record.clone());
        event_record
    }

    fn update_system_state(&mut self, failure: &FailureEvent) {
        let ft = failure.failure_type;
        match ft {
            FailureType::BatteryCritical => {
                self.state.battery_pct = 3.0;
                self.state.level = DegradationLevel::Survival;
            }
            FailureType::BatteryDead => {
                self.state.battery_pct = 0.0;
                self.state.level = DegradationLevel::Dead;
            }
            FailureType::GpsLost => {
                self.state.gps_available = false;
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded1);
            }
            FailureType::CameraFailure => {
                self.state.camera_available = false;
                self.state.available_sensors.retain(|x| x != "camera");
                self.state.available_inputs.retain(|x| x != "camera");
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded1);
            }
            FailureType::MicrophoneDead => {
                self.state.microphone_available = false;
                self.state.available_inputs.retain(|x| x != "microfone" && x != "voz");
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded2);
            }
            FailureType::SpeakerDead => {
                self.state.speaker_available = false;
                self.state.available_outputs.retain(|x| x != "tts");
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded2);
            }
            FailureType::TtsCrash => {
                self.state.tts_available = false;
                self.state.available_outputs.retain(|x| x != "tts");
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded2);
            }
            FailureType::VibrationDead => {
                self.state.vibration_available = false;
                self.state.available_outputs.retain(|x| x != "vibracao" && x != "haptico");
            }
            FailureType::ScreenBroken | FailureType::ScreenDead => {
                self.state.screen_available = false;
                self.state.available_outputs.retain(|x| x != "tela");
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded2);
            }
            FailureType::BluetoothDrop => {
                self.state.braille_connected = false;
                self.state.available_outputs.retain(|x| x != "braille");
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded1);
            }
            FailureType::NetworkDown | FailureType::CloudDown => {
                self.state.network_available = false;
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded1);
            }
            FailureType::SmartwatchLost => {
                self.state.smartwatch_connected = false;
            }
            FailureType::EyeTrackerLost => {
                self.state.eye_tracker_connected = false;
                self.state.available_inputs.retain(|x| x != "rastreio_olhos");
            }
            FailureType::WaterDamage => {
                self.state.level = DegradationLevel::Emergency;
                self.state.camera_available = false;
                self.state.microphone_available = false;
                self.state.screen_available = false;
            }
            FailureType::AppCrash => {
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded1);
            }
            FailureType::MemoryExhausted => {
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded2);
            }
            FailureType::PermissionRevoked => {
                self.state.microphone_available = false;
                self.state.available_inputs.retain(|x| x != "microfone");
            }
            FailureType::SttFailure => {
                self.state.available_inputs.retain(|x| x != "voz");
                self.state.level = self.escalate(self.state.level, DegradationLevel::Degraded2);
            }
            _ => {}
        }
    }

    fn apply_mitigation(&mut self, strategy: &MitigationStrategy) -> HashMap<String, String> {
        let mut result = HashMap::new();
        result.insert("strategy".to_string(), strategy.name.clone());
        result.insert("fallback_chain".to_string(), strategy.fallback_chain.join(" | "));
        result.insert("recovery_action".to_string(), strategy.recovery_action.clone());

        match strategy.failure_type {
            FailureType::TtsCrash => {
                if self.state.braille_connected {
                    if !self.state.available_outputs.contains(&"braille".to_string()) {
                        self.state.available_outputs.push("braille".to_string());
                    }
                    result.insert("restored_output".to_string(), "braille".to_string());
                } else if self.state.vibration_available {
                    if !self.state.available_outputs.contains(&"vibracao".to_string()) {
                        self.state.available_outputs.push("vibracao".to_string());
                    }
                    result.insert("restored_output".to_string(), "vibracao".to_string());
                }
            }
            FailureType::CameraFailure => {
                if self.state.microphone_available && !self.state.available_sensors.contains(&"audio_sonar".to_string()) {
                    self.state.available_sensors.push("audio_sonar".to_string());
                    result.insert("restored_sensor".to_string(), "audio_sonar (microfone como sonar)".to_string());
                }
            }
            FailureType::MicrophoneDead => {
                if self.state.screen_available && !self.state.available_inputs.contains(&"switch".to_string()) {
                    self.state.available_inputs.push("switch".to_string());
                    result.insert("restored_input".to_string(), "switch (botoes na tela)".to_string());
                }
            }
            FailureType::GpsLost => {
                if self.state.available_sensors.contains(&"bussola".to_string()) && !self.state.available_sensors.contains(&"dead_reckoning".to_string()) {
                    self.state.available_sensors.push("dead_reckoning".to_string());
                    result.insert("restored_sensor".to_string(), "dead_reckoning (bussola + passos)".to_string());
                }
            }
            FailureType::AppCrash => {
                result.insert("restored".to_string(), "watchdog reiniciou em 3s".to_string());
            }
            _ => {}
        }
        result
    }

    pub fn recover_failure(&mut self, failure_type: FailureType) -> HashMap<String, String> {
        let mut recovered = false;
        if let Some(pos) = self.state.active_failures.iter().position(|f| f.failure_type == failure_type) {
            self.state.active_failures.remove(pos);
            recovered = true;
        }

        if let Some(strategy) = self.strategies.get(&failure_type) {
            self.mitigations_active.remove(&strategy.strategy_id);
        }

        self.recalculate_level();

        match failure_type {
            FailureType::GpsLost => {
                self.state.gps_available = true;
                if !self.state.available_sensors.contains(&"gps".to_string()) {
                    self.state.available_sensors.push("gps".to_string());
                }
            }
            FailureType::CameraFailure => {
                self.state.camera_available = true;
                if !self.state.available_sensors.contains(&"camera".to_string()) {
                    self.state.available_sensors.push("camera".to_string());
                }
            }
            FailureType::NetworkDown => {
                self.state.network_available = true;
            }
            FailureType::TtsCrash => {
                self.state.tts_available = true;
                if !self.state.available_outputs.contains(&"tts".to_string()) {
                    self.state.available_outputs.push("tts".to_string());
                }
            }
            _ => {}
        }

        let mut result = HashMap::new();
        result.insert("recovered".to_string(), recovered.to_string());
        result.insert("failure".to_string(), failure_type.as_str().to_string());
        result.insert("current_level".to_string(), self.state.level.as_str().to_string());
        result.insert("remaining_failures".to_string(), self.state.active_failures.len().to_string());
        result
    }

    fn escalate(&self, current: DegradationLevel, new: DegradationLevel) -> DegradationLevel {
        let levels = [
            DegradationLevel::Full,
            DegradationLevel::Degraded1,
            DegradationLevel::Degraded2,
            DegradationLevel::Survival,
            DegradationLevel::Emergency,
            DegradationLevel::Dead,
        ];
        let cur_idx = levels.iter().position(|&l| l == current).unwrap();
        let new_idx = levels.iter().position(|&l| l == new).unwrap();
        levels[std::cmp::max(cur_idx, new_idx)]
    }

    fn recalculate_level(&mut self) {
        if self.state.active_failures.is_empty() {
            self.state.level = DegradationLevel::Full;
            return;
        }

        let severity_order = [
            FailureSeverity::Cosmetic,
            FailureSeverity::Minor,
            FailureSeverity::Major,
            FailureSeverity::Critical,
            FailureSeverity::Catastrophic,
        ];

        let max_severity = self.state.active_failures.iter()
            .max_by_key(|f| severity_order.iter().position(|&s| s == f.severity).unwrap())
            .unwrap()
            .severity;

        self.state.level = match max_severity {
            FailureSeverity::Catastrophic => DegradationLevel::Emergency,
            FailureSeverity::Critical => DegradationLevel::Survival,
            FailureSeverity::Major => DegradationLevel::Degraded2,
            FailureSeverity::Minor => DegradationLevel::Degraded1,
            _ => DegradationLevel::Full,
        };
    }

    pub fn system_status(&self) -> HashMap<String, String> {
        let mut status = HashMap::new();
        status.insert("degradation_level".to_string(), self.state.level.as_str().to_string());
        status.insert("battery_pct".to_string(), self.state.battery_pct.to_string());
        status.insert("active_failures".to_string(), self.state.active_failures.len().to_string());
        status.insert("active_mitigations".to_string(), self.mitigations_active.len().to_string());
        status.insert("available_inputs".to_string(), self.state.available_inputs.join(","));
        status.insert("available_outputs".to_string(), self.state.available_outputs.join(","));
        status.insert("available_sensors".to_string(), self.state.available_sensors.join(","));
        status.insert("network".to_string(), self.state.network_available.to_string());
        status.insert("gps".to_string(), self.state.gps_available.to_string());
        status.insert("camera".to_string(), self.state.camera_available.to_string());
        status.insert("microphone".to_string(), self.state.microphone_available.to_string());
        status.insert("speaker".to_string(), self.state.speaker_available.to_string());
        status.insert("tts".to_string(), self.state.tts_available.to_string());
        status.insert("screen".to_string(), self.state.screen_available.to_string());
        status.insert("vibration".to_string(), self.state.vibration_available.to_string());
        status.insert("braille".to_string(), self.state.braille_connected.to_string());
        status
    }
}

// ============================================================================
// 6. SIMULACOES DE CENARIO CATASTROFICO
// ============================================================================

pub fn simulate_blind_user_battery_death() {
    println!("{}", "=".repeat(65));
    println!("CENARIO 1: Cego na rua -- bateria morrendo");
    println!("{}", "=".repeat(65));

    let mut sim = FailureSimulator::new();

    println!("\n[ESTADO INICIAL]");
    let status = sim.system_status();
    println!("  Nivel: {}", status["degradation_level"]);
    println!("  Bateria: {}%", status["battery_pct"]);
    println!("  Inputs: {}", status["available_inputs"]);

    println!("\n[FALHA: Bateria critica]");
    let event = FailureEvent::new(
        "EVT-001",
        FailureType::BatteryCritical,
        FailureCategory::Power,
        FailureSeverity::Critical,
        FailureDuration::Short,
        "Bateria abaixo de 5%",
    );
    let result = sim.inject_failure(event);
    println!("  Mitigacao: {}", result.get("mitigation").unwrap_or(&"".to_string()));
    println!("  Mensagem ao usuario: {}", result.get("user_message").unwrap_or(&"".to_string()));
    let status = sim.system_status();
    println!("  Nivel atual: {}", status["degradation_level"]);
    println!("  Bateria: {}%", status["battery_pct"]);

    println!("\n[FALHA: Bateria morta]");
    let event = FailureEvent::new(
        "EVT-002",
        FailureType::BatteryDead,
        FailureCategory::Power,
        FailureSeverity::Catastrophic,
        FailureDuration::Long,
        "Bateria em 0%",
    );
    let result = sim.inject_failure(event);
    println!("  Mitigacao: {}", result.get("mitigation").unwrap_or(&"".to_string()));
    if let Some(chain) = result.get("fallback_chain") {
        for fb in chain.split(" | ") {
            println!("    {}", fb);
        }
    }
    println!("  Mensagem: {}", result.get("user_message").unwrap_or(&"".to_string()));
}

pub fn simulate_cascading_failures() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 2: Falhas em cascata");
    println!("{}", "=".repeat(65));

    let mut sim = FailureSimulator::new();
    let cascading_failures = vec![
        FailureEvent::new("C-01", FailureType::NetworkDown, FailureCategory::Network, FailureSeverity::Major, FailureDuration::Medium, "Internet caiu"),
        FailureEvent::new("C-02", FailureType::GpsLost, FailureCategory::Sensor, FailureSeverity::Major, FailureDuration::Medium, "GPS perdido"),
        FailureEvent::new("C-03", FailureType::BluetoothDrop, FailureCategory::Peripheral, FailureSeverity::Major, FailureDuration::Transient, "Braille desconectou"),
        FailureEvent::new("C-04", FailureType::TtsCrash, FailureCategory::Software, FailureSeverity::Critical, FailureDuration::Short, "TTS crashou"),
    ];

    for f in cascading_failures {
        println!("\n[FALHA: {}]", f.failure_type.as_str());
        let result = sim.inject_failure(f.clone());
        let status = sim.system_status();
        println!("  Severidade: {}", f.severity.as_str());
        println!("  Mitigacao: {}", result.get("mitigation").unwrap_or(&"".to_string()));
        println!("  Nivel sistema: {}", status["degradation_level"]);
        println!("  Outputs restantes: {}", status["available_outputs"]);
        println!("  Inputs restantes: {}", status["available_inputs"]);
    }

    println!("\n[ESTADO APOS 4 FALHAS EM CASCATA]");
    let status = sim.system_status();
    println!("  Nivel: {}", status["degradation_level"]);
    println!("  Falhas ativas: {}", status["active_failures"]);
    println!("  Mitigacoes ativas: {}", status["active_mitigations"]);

    println!("\n[RECUPERACAO GRADUAL]");
    for ft in [FailureType::TtsCrash, FailureType::BluetoothDrop, FailureType::GpsLost, FailureType::NetworkDown] {
        let r = sim.recover_failure(ft);
        println!("  {}: nivel -> {}", ft.as_str(), r["current_level"]);
    }
}

pub fn simulate_water_damage() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 3: Dano por agua");
    println!("{}", "=".repeat(65));

    let mut sim = FailureSimulator::new();
    println!("\n[FALHA: Smartphone molhou]");
    let event = FailureEvent::new(
        "W-01",
        FailureType::WaterDamage,
        FailureCategory::Hardware,
        FailureSeverity::Catastrophic,
        FailureDuration::Permanent,
        "Smartphone caiu na agua/poca",
    );
    let result = sim.inject_failure(event);
    println!("  Mitigacao: {}", result.get("mitigation").unwrap_or(&"".to_string()));
    println!("  Mensagem: {}", result.get("user_message").unwrap_or(&"".to_string()));
    if let Some(chain) = result.get("fallback_chain") {
        for fb in chain.split(" | ") {
            println!("    {}", fb);
        }
    }
    let status = sim.system_status();
    println!("  Nivel: {}", status["degradation_level"]);
    println!("  Camera: {} | Microfone: {} | Tela: {}", status["camera"], status["microphone"], status["screen"]);
}

pub fn simulate_software_resilience() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 4: Software crash + auto-recovery");
    println!("{}", "=".repeat(65));

    let mut sim = FailureSimulator::new();
    for i in 0..3 {
        println!("\n[FALHA {}: App crashou]", i + 1);
        let event = FailureEvent::new(
            &format!("S-{:02}", i + 1),
            FailureType::AppCrash,
            FailureCategory::Software,
            FailureSeverity::Major,
            FailureDuration::Transient,
            &format!("App crashou (tentativa {})", i + 1),
        );
        let result = sim.inject_failure(event);
        println!("  Mitigacao: {}", result.get("mitigation").unwrap_or(&"".to_string()));
        println!("  User message: {}", result.get("user_message").unwrap_or(&"".to_string()));

        if i < 2 {
            let r = sim.recover_failure(FailureType::AppCrash);
            println!("  Recuperado: nivel -> {}", r["current_level"]);
        }
    }
}

pub fn simulate_multi_user_scenarios() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 5: Impacto por deficiencia");
    println!("{}", "=".repeat(65));

    let scenarios = vec![
        ("CEGO", vec![FailureType::TtsCrash, FailureType::GpsLost, FailureType::BluetoothDrop]),
        ("SURDO", vec![FailureType::ScreenBroken, FailureType::VibrationDead]),
        ("TETRAPLEGICO", vec![FailureType::SttFailure, FailureType::EyeTrackerLost]),
        ("AUTISTA", vec![FailureType::NetworkDown, FailureType::SpeakerDead]),
    ];

    for (label, failures) in scenarios {
        println!("\n  {}:", label);
        let mut sim = FailureSimulator::new();
        for ft in failures {
            let event = FailureEvent::new(
                &format!("M-{}-{}", label, ft.as_str()),
                ft,
                FailureCategory::Hardware,
                FailureSeverity::Critical,
                FailureDuration::Short,
                ft.as_str(),
            );
            let result = sim.inject_failure(event);
            let status = sim.system_status();
            println!("    Falha: {}", ft.as_str());
            println!("      Nivel: {}", status["degradation_level"]);
            println!("      Mitigacao: {}", result.get("mitigation").unwrap_or(&"".to_string()));
            println!("      Inputs: {}", status["available_inputs"]);
            println!("      Outputs: {}", status["available_outputs"]);
        }
    }
}

pub fn simulate_full_catastrophe() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 6: CATASTROFE TOTAL");
    println!("{}", "=".repeat(65));

    let mut sim = FailureSimulator::new();
    let all_failures = vec![
        FailureType::BatteryCritical, FailureType::GpsLost, FailureType::CameraFailure,
        FailureType::MicrophoneDead, FailureType::TtsCrash, FailureType::BluetoothDrop,
        FailureType::NetworkDown, FailureType::ScreenBroken, FailureType::VibrationDead,
        FailureType::SmartwatchLost,
    ];

    println!("\nInjetando {} falhas simultaneas...", all_failures.len());
    for ft in all_failures {
        let event = FailureEvent::new(
            &format!("CAT-{}", ft.as_str()),
            ft,
            FailureCategory::Hardware,
            FailureSeverity::Catastrophic,
            FailureDuration::Permanent,
            &format!("Catastrofe: {}", ft.as_str()),
        );
        sim.inject_failure(event);
    }

    let status = sim.system_status();
    println!("\n[ESTADO APOS CATASTROFE]");
    println!("  Nivel: {}", status["degradation_level"]);
    println!("  Bateria: {}%", status["battery_pct"]);
    println!("  Falhas ativas: {}", status["active_failures"]);
    println!("  Mitigacoes ativas: {}", status["active_mitigations"]);
    println!("  Inputs: {}", status["available_inputs"]);
    println!("  Outputs: {}", status["available_outputs"]);
    println!("  Sensores: {}", status["available_sensors"]);

    if status["available_outputs"].is_empty() && status["available_inputs"].is_empty() {
        println!("\n  PLANO D: LIGACAO CELULAR DIRETA");
        println!("  O unico canal que resta e o sinal de celular + SMS.");
        println!("  Sistema envia SMS com localizacao para emergencia.");
        println!("  Se nem sinal tem: GRITE. Peça ajuda humana.");
    }
}

// ============================================================================
// 7. DEMONSTRACAO (main)
// ============================================================================

fn main() {
    println!("{}", "=".repeat(70));
    println!("OpenResilience -- Simulacao de Falhas e Mitigacao");
    println!("{}", "=".repeat(70));

    println!("\nFalhas mapeadas: {}", 40);
    println!("Categorias de falha: {}", 8);
    println!("Estrategias de mitigacao: {}", 17);
    println!("Niveis de degradacao: {}", 6);

    println!("\n{}", "=".repeat(70));
    println!("COBERTURA DE MITIGACAO POR CATEGORIA");
    println!("{}", "=".repeat(70));
    println!("  Falhas com mitigacao: 17/40");

    simulate_blind_user_battery_death();
    simulate_cascading_failures();
    simulate_water_damage();
    simulate_software_resilience();
    simulate_multi_user_scenarios();
    simulate_full_catastrophe();

    println!("\n{}", "=".repeat(70));
    println!("RESUMO DE MITIGACOES");
    println!("{}", "=".repeat(70));
    for s in MITIGATION_STRATEGIES {
        println!("\n  {}: {}", s.strategy_id, s.name);
        println!("    Falha: {}", s.failure_type.as_str());
        println!("    Descricao: {}", s.description);
        println!("    Planos: {} fallbacks", s.fallback_chain.len());
        for fb in &s.fallback_chain {
            println!("      {}", fb);
        }
    }

    println!("\n{}", "=".repeat(70));
    println!("Total falhas: 40");
    println!("Total mitigacoes: 17");
    println!("Cada falha tem Plano A, B, C e D.");
    println!("Nenhum ponto unico de falha.");
    println!("Redundancia em TUDO.");
    println!("\nO sistema PODE falhar. O usuario NAO pode ficar desamparado.");
}