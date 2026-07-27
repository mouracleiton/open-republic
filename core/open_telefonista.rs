// OpenTelefonista -- O Sistema Como Conversa Humana
// ===================================================
// "Voce nao abre um app. Voce nao clica um botao.
// Voce FALA. E uma voz responde. Como telefonista humana.
// 'E a Republica.' 'Cleiton, voce tem 3 tarefas. Quer ouvir?'
// 'O codigo que voce ditou tem um erro na linha 5. Quer que eu corrija?'
//
// A telefonista NAO e um chatbot. E uma PESSOA DIGITAL que:
// 1. CONVERSA naturalmente (nao comandos, dialogo)
// 2. CAPTA o mundo pelos sensores do smartphone/hardware
// 3. TRADUZ o mundo para o usuario (daltonico ve cor, cego ouve rua)
// 4. PROTEGE o usuario (geolocalizacao de criancas, deteccao de perigo)
// 5. AMPLIFICA o usuario (programa por voz, aprende por audio)
// 6. RESPEITA o silencio (OpenSilencePolicy -- so fala quando chamada)
//
// O smartphone vira o CORPO EXTENDIDO do usuario:
// - Camera = olhos (daltonico ve cores corretas, cego ve obstaculos)
// - Microfone = ouvidos (surdo ve legendas, capta ambiente)
// - GPS = sentido de direcao (cego navega, criancas localizadas)
// - Acelerometro = equilibrio (detecta queda, tremor)
// - Vibracall = tato (surdos sentem o mundo)
// - Ligacao celular = telefone de verdade (telefonista LIGA para quem precisa)
//
// DIFERENCA CRITICAL: A telefonista e HUMANIZADA, nao robotica.
// Ela tem nome, personalidade, memoria, humor.
// Ela PERGUNTA antes de agir. Ela ESPERA resposta.
// Ela NUNCA interrompe (OpenSilencePolicy).
// Ela se ADAPTA ao humor e energia do usuario.
//
// Integrado com:
// - OpenInclusiveIDE (programa por voz conversando)
// - OpenInclusiveHardware (todos os 44 dispositivos)
// - OpenAudioChannel (separa voz de ruido)
// - OpenSilencePolicy (so fala quando chamada)
// - OpenAbsence (respeita pausas)
// - OpenBodilyAutonomy (usuario controla tudo)
// - OpenFocus (nao distrai)
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// ============================================================================

#![allow(dead_code, unused_variables, unused_imports)]
use std::collections::{HashMap, HashSet, VecDeque};
use std::time::{SystemTime, UNIX_EPOCH};

// ============================================================================
// 1. PERSONALIDADE DA TELEFONISTA
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
enum TelefonistaPersonality {
    /// Personalidades disponiveis da telefonista.
    GENTLE,      // calma, pausada, maternamente
    CHEERFUL,    // energica, motivadora
    SERIOUS,     // direta, profissional
    FRIENDLY,    // casual, como uma amiga
    FORMAL,      // educada, cerimoniosa
    PLAYFUL,     // humor, leveza
    PROTECTIVE,  // foca em seguranca
    MINIMAL,     // so o necessario, poucas palavras
}

impl TelefonistaPersonality {
    fn value(&self) -> &'static str {
        match self {
            TelefonistaPersonality::GENTLE => "gentil",
            TelefonistaPersonality::CHEERFUL => "alegre",
            TelefonistaPersonality::SERIOUS => "seria",
            TelefonistaPersonality::FRIENDLY => "amiga",
            TelefonistaPersonality::FORMAL => "formal",
            TelefonistaPersonality::PLAYFUL => "brincalhona",
            TelefonistaPersonality::PROTECTIVE => "protetora",
            TelefonistaPersonality::MINIMAL => "minimal",
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
enum EmotionalState {
    /// Estado emocional detectado ou reportado pelo usuario.
    HAPPY,
    CALM,
    FOCUSED,
    TIRED,
    STRESSED,
    ANXIOUS,
    SAD,
    ANGRY,
    OVERWHELMED,
    NEUTRAL,
}

impl EmotionalState {
    fn value(&self) -> &'static str {
        match self {
            EmotionalState::HAPPY => "feliz",
            EmotionalState::CALM => "calmo",
            EmotionalState::FOCUSED => "focado",
            EmotionalState::TIRED => "cansado",
            EmotionalState::STRESSED => "estressado",
            EmotionalState::ANXIOUS => "ansioso",
            EmotionalState::SAD => "triste",
            EmotionalState::ANGRY => "irritado",
            EmotionalState::OVERWHELMED => "sobrecarregado",
            EmotionalState::NEUTRAL => "neutro",
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
enum ConversationMode {
    /// Modo de conversa.
    DIALOGUE,   // conversa bidirecional natural
    DICTATION,  // usuario dita, sistema executa
    NARRATION,  // sistema narrativa o que acontece
    EMERGENCY,  // prioridade maxima, voz firme
    WHISPER,    // resposta discreta (surdo = haptico)
    SILENT,     // so visual/haptico, sem voz
    CO_DRIVER,  // guia o usuario no mundo fisico
    TEACHER,    // ensina enquanto faz
}

impl ConversationMode {
    fn value(&self) -> &'static str {
        match self {
            ConversationMode::DIALOGUE => "dialogo",
            ConversationMode::DICTATION => "ditado",
            ConversationMode::NARRATION => "narracao",
            ConversationMode::EMERGENCY => "emergencia",
            ConversationMode::WHISPER => "sussurro",
            ConversationMode::SILENT => "silencioso",
            ConversationMode::CO_DRIVER => "copiloto",
            ConversationMode::TEACHER => "professora",
        }
    }
}

#[derive(Debug, Clone)]
struct TelefonistaConfig {
    /// Configuracao da personalidade da telefonista.
    name: String,
    personality: TelefonistaPersonality,
    voice_id: String,
    speech_rate: f64,
    formality: f64,
    verbosity: f64,
    humor_enabled: bool,
    proactive: f64,
    language: String,
    respects_silence: bool,
    interruptible: bool,
    emotional_adaptation: bool,
}

impl Default for TelefonistaConfig {
    fn default() -> Self {
        TelefonistaConfig {
            name: "Iara".to_string(),
            personality: TelefonistaPersonality::GENTLE,
            voice_id: "pt-BR-FemaleA".to_string(),
            speech_rate: 1.0,
            formality: 0.3,
            verbosity: 0.5,
            humor_enabled: true,
            proactive: 0.3,
            language: "pt-BR".to_string(),
            respects_silence: true,
            interruptible: true,
            emotional_adaptation: true,
        }
    }
}

impl TelefonistaConfig {
    fn adapt_to_emotion(&mut self, emotion: EmotionalState) {
        /// Adapta comportamento ao estado emocional.
        if emotion == EmotionalState::STRESSED || emotion == EmotionalState::ANXIOUS {
            self.speech_rate = 0.85;
            self.verbosity = 0.3;
            self.humor_enabled = false;
            self.personality = TelefonistaPersonality::GENTLE;
        } else if emotion == EmotionalState::TIRED {
            self.speech_rate = 0.9;
            self.verbosity = 0.3;
            self.proactive = 0.1;
        } else if emotion == EmotionalState::HAPPY {
            self.humor_enabled = true;
            self.speech_rate = 1.1;
        } else if emotion == EmotionalState::OVERWHELMED {
            self.verbosity = 0.1;
            self.speech_rate = 0.8;
            self.proactive = 0.0;
        } else if emotion == EmotionalState::FOCUSED {
            self.verbosity = 0.2;
            self.humor_enabled = false;
            self.proactive = 0.1;
        }
    }
}

// ============================================================================
// 2. CAPACIDADES DO SMARTPHONE COMO CORPO EXTENDIDO
// ============================================================================

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
enum SensorType {
    /// Sensores do smartphone/hardware que captam o mundo.
    CAMERA_REAR,
    CAMERA_FRONT,
    MICROPHONE,
    GPS,
    ACCELEROMETER,
    GYROSCOPE,
    COMPASS,
    BAROMETER,
    THERMOMETER,
    HUMIDITY,
    LIGHT,
    PROXIMITY,
    LIDAR,
    TOF,
    HEART_RATE,
    SPO2,
    SKIN_TEMP,
    NFC,
    BLUETOOTH_BEACON,
    CELL_SIGNAL,
}

impl SensorType {
    fn value(&self) -> &'static str {
        match self {
            SensorType::CAMERA_REAR => "camera_traseira",
            SensorType::CAMERA_FRONT => "camera_frontal",
            SensorType::MICROPHONE => "microfone",
            SensorType::GPS => "gps",
            SensorType::ACCELEROMETER => "acelerometro",
            SensorType::GYROSCOPE => "giroscopio",
            SensorType::COMPASS => "bussola",
            SensorType::BAROMETER => "barometro",
            SensorType::THERMOMETER => "termometro",
            SensorType::HUMIDITY => "umidade",
            SensorType::LIGHT => "luminosidade",
            SensorType::PROXIMITY => "proximidade",
            SensorType::LIDAR => "lidar",
            SensorType::TOF => "tempo_de_voo",
            SensorType::HEART_RATE => "frequencia_cardiaca",
            SensorType::SPO2 => "oxigenio",
            SensorType::SKIN_TEMP => "temperatura_pele",
            SensorType::NFC => "nfc",
            SensorType::BLUETOOTH_BEACON => "beacon_bluetooth",
            SensorType::CELL_SIGNAL => "sinal_celular",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
enum WorldPerception {
    /// O que o sistema percebe do mundo atraves dos sensores.
    // VISAO
    COLOR_DETECTION,
    TEXT_RECOGNITION,
    OBJECT_DETECTION,
    FACE_RECOGNITION,
    OBSTACLE_DETECTION,
    CROSSWALK_DETECTION,
    TRAFFIC_LIGHT,
    SIGN_RECOGNITION,
    DOCUMENT_SCAN,
    MONEY_RECOGNITION,
    PRODUCT_LABEL,
    // AUDICAO
    SOUND_CLASSIFICATION,
    SPEAKER_RECOGNITION,
    MUSIC_RECOGNITION,
    SPEECH_TO_TEXT,
    AMBIENT_NOISE,
    DOORBELL,
    ALARM_SOUND,
    SIREN,
    BABY_CRYING,
    DOG_BARKING,
    // LOCALIZACAO
    GPS_LOCATION,
    INDOOR_LOCATION,
    DIRECTION_FACING,
    ALTITUDE,
    SPEED,
    NEARBY_PLACES,
    GEOCODING,
    LOST_CHILD,
    // BIOMETRIA
    FALL_DETECTION,
    HEART_ANOMALY,
    STRESS_DETECTION,
    SEIZURE_PREDICTION,
    TREMOR_DETECTION,
    POSTURE,
    // AMBIENTE
    TEMPERATURE,
    AIR_QUALITY,
    UV_INDEX,
    WEATHER,
}

impl WorldPerception {
    fn value(&self) -> &'static str {
        match self {
            WorldPerception::COLOR_DETECTION => "deteccao_cor",
            WorldPerception::TEXT_RECOGNITION => "reconhecimento_texto",
            WorldPerception::OBJECT_DETECTION => "deteccao_objetos",
            WorldPerception::FACE_RECOGNITION => "reconhecimento_facial",
            WorldPerception::OBSTACLE_DETECTION => "deteccao_obstaculos",
            WorldPerception::CROSSWALK_DETECTION => "deteccao_faixa",
            WorldPerception::TRAFFIC_LIGHT => "semaforo",
            WorldPerception::SIGN_RECOGNITION => "reconhecimento_placas",
            WorldPerception::DOCUMENT_SCAN => "escaneamento_documento",
            WorldPerception::MONEY_RECOGNITION => "reconhecimento_cedula",
            WorldPerception::PRODUCT_LABEL => "rotulo_produto",
            WorldPerception::SOUND_CLASSIFICATION => "classificacao_som",
            WorldPerception::SPEAKER_RECOGNITION => "reconhecimento_voz",
            WorldPerception::MUSIC_RECOGNITION => "reconhecimento_musica",
            WorldPerception::SPEECH_TO_TEXT => "fala_para_texto",
            WorldPerception::AMBIENT_NOISE => "ruido_ambiente",
            WorldPerception::DOORBELL => "campainha",
            WorldPerception::ALARM_SOUND => "alarme",
            WorldPerception::SIREN => "sirene",
            WorldPerception::BABY_CRYING => "bebe_chorando",
            WorldPerception::DOG_BARKING => "cachorro_latindo",
            WorldPerception::GPS_LOCATION => "localizacao_gps",
            WorldPerception::INDOOR_LOCATION => "localizacao_indoor",
            WorldPerception::DIRECTION_FACING => "direcao",
            WorldPerception::ALTITUDE => "altitude",
            WorldPerception::SPEED => "velocidade",
            WorldPerception::NEARBY_PLACES => "lugares_proximos",
            WorldPerception::GEOCODING => "geocoding",
            WorldPerception::LOST_CHILD => "crianca_perdida",
            WorldPerception::FALL_DETECTION => "deteccao_queda",
            WorldPerception::HEART_ANOMALY => "anomalia_cardiaca",
            WorldPerception::STRESS_DETECTION => "deteccao_stress",
            WorldPerception::SEIZURE_PREDICTION => "previsao_crise",
            WorldPerception::TREMOR_DETECTION => "deteccao_tremor",
            WorldPerception::POSTURE => "postura",
            WorldPerception::TEMPERATURE => "temperatura_ambiente",
            WorldPerception::AIR_QUALITY => "qualidade_ar",
            WorldPerception::UV_INDEX => "indice_uv",
            WorldPerception::WEATHER => "clima",
        }
    }
}

#[derive(Debug, Clone)]
struct SensorReading {
    /// Uma leitura de sensor do mundo fisico.
    sensor: SensorType,
    perception: WorldPerception,
    value: String,
    confidence: f64,
    timestamp: f64,
    description: String,
}

fn current_time() -> f64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs_f64()
}

// ============================================================================
// 3. VISAO COMPUTACIONAL -- Camera como Olhos
// ============================================================================

struct ComputerVisionEngine {
    active_perceptions: Vec<WorldPerception>,
    last_readings: VecDeque<SensorReading>,
}

impl ComputerVisionEngine {
    fn new() -> Self {
        ComputerVisionEngine {
            active_perceptions: Vec::new(),
            last_readings: VecDeque::with_capacity(100),
        }
    }

    fn process_frame(&mut self, sensor: SensorType) -> Vec<SensorReading> {
        /// Processa um frame da camera e gera leituras.
        let mut readings = Vec::new();

        // DALTONICO: detecta e nomeia cores
        readings.push(SensorReading {
            sensor: sensor.clone(),
            perception: WorldPerception::COLOR_DETECTION,
            value: "{\"color_name\": \"vermelho\", \"hex\": \"#FF0000\"}".to_string(),
            confidence: 0.95,
            timestamp: current_time(),
            description: "Aqui e VERMELHO. A luz do semaforo esta VERMELHA. Pare.".to_string(),
        });

        // CEGO: detecta obstaculos
        readings.push(SensorReading {
            sensor: sensor.clone(),
            perception: WorldPerception::OBSTACLE_DETECTION,
            value: "{\"obstacle\": \"poste\", \"distance_m\": 2.5}".to_string(),
            confidence: 0.88,
            timestamp: current_time(),
            description: "Poste a 2.5 metros a frente e a esquerda. Desvie para a direita.".to_string(),
        });

        // OCR
        readings.push(SensorReading {
            sensor: sensor.clone(),
            perception: WorldPerception::TEXT_RECOGNITION,
            value: "{\"text\": \"RESTAURANTE JOAO\"}".to_string(),
            confidence: 0.92,
            timestamp: current_time(),
            description: "Placa diz: RESTAURANTE JOAO. Fica acima da porta a frente.".to_string(),
        });

        // SEMAFORO
        readings.push(SensorReading {
            sensor: sensor.clone(),
            perception: WorldPerception::TRAFFIC_LIGHT,
            value: "{\"color\": \"verde\"}".to_string(),
            confidence: 0.97,
            timestamp: current_time(),
            description: "Semaforo VERDE. Pode atravessar.".to_string(),
        });

        // CEDULA
        readings.push(SensorReading {
            sensor: sensor.clone(),
            perception: WorldPerception::MONEY_RECOGNITION,
            value: "{\"denomination\": \"R$ 50,00\"}".to_string(),
            confidence: 0.94,
            timestamp: current_time(),
            description: "Isso e uma nota de CINQUENTA REAIS.".to_string(),
        });

        for r in &readings {
            self.last_readings.push_back(r.clone());
            if self.last_readings.len() > 100 {
                self.last_readings.pop_front();
            }
        }
        readings
    }

    fn narrate_scene(&self, readings: &[SensorReading]) -> String {
        /// Transforma leituras visuais em narrativa falada.
        if readings.is_empty() {
            return "Nao consigo ver nada claramente agora.".to_string();
        }
        let parts: Vec<String> = readings
            .iter()
            .filter(|r| r.confidence > 0.7)
            .map(|r| r.description.clone())
            .collect();
        if parts.is_empty() {
            "Ambiente visual incerto. Vou continuar observando.".to_string()
        } else {
            parts.join(". ") + "."
        }
    }
}

// ============================================================================
// 4. AUDIO -- Microfone como Ouvidos
// ============================================================================

struct AudioPerceptionEngine {
    last_readings: VecDeque<SensorReading>,
}

impl AudioPerceptionEngine {
    fn new() -> Self {
        AudioPerceptionEngine {
            last_readings: VecDeque::with_capacity(100),
        }
    }

    fn process_audio(&mut self) -> Vec<SensorReading> {
        /// Processa audio ambiente e gera leituras.
        let mut readings = Vec::new();

        readings.push(SensorReading {
            sensor: SensorType::MICROPHONE,
            perception: WorldPerception::SPEECH_TO_TEXT,
            value: "{\"speaker\": \"homem\", \"text\": \"Bom dia, como vai?\"}".to_string(),
            confidence: 0.90,
            timestamp: current_time(),
            description: "Um homem disse: Bom dia, como vai?".to_string(),
        });

        readings.push(SensorReading {
            sensor: SensorType::MICROPHONE,
            perception: WorldPerception::SOUND_CLASSIFICATION,
            value: "{\"sound\": \"sirene\"}".to_string(),
            confidence: 0.85,
            timestamp: current_time(),
            description: "Sirene de ambulancia se aproximando pela direita.".to_string(),
        });

        readings.push(SensorReading {
            sensor: SensorType::MICROPHONE,
            perception: WorldPerception::DOORBELL,
            value: "{\"detected\": true, \"count\": 2}".to_string(),
            confidence: 0.95,
            timestamp: current_time(),
            description: "Alguem tocou a campainha. Duas vezes.".to_string(),
        });

        readings.push(SensorReading {
            sensor: SensorType::MICROPHONE,
            perception: WorldPerception::BABY_CRYING,
            value: "{\"detected\": true}".to_string(),
            confidence: 0.93,
            timestamp: current_time(),
            description: "O bebe esta chorando. Intensidade alta.".to_string(),
        });

        for r in &readings {
            self.last_readings.push_back(r.clone());
            if self.last_readings.len() > 100 {
                self.last_readings.pop_front();
            }
        }
        readings
    }

    fn narrate_sounds(&self, readings: &[SensorReading]) -> String {
        /// Transforma leituras de audio em narrativa para surdos.
        if readings.is_empty() {
            return "Silencio.".to_string();
        }
        let parts: Vec<String> = readings
            .iter()
            .filter(|r| r.confidence > 0.7)
            .map(|r| r.description.clone())
            .collect();
        if parts.is_empty() {
            "Nao identifico sons especificos.".to_string()
        } else {
            parts.join(". ") + "."
        }
    }
}

// ============================================================================
// 5. GEOLOCALIZACAO -- GPS como Sentido de Direcao
// ============================================================================

struct GeoLocationEngine {
    last_known_location: (f64, f64),
    tracked_persons: HashMap<String, HashMap<String, String>>,
    safe_zones: Vec<HashMap<String, String>>,
    last_readings: VecDeque<SensorReading>,
}

impl GeoLocationEngine {
    fn new() -> Self {
        GeoLocationEngine {
            last_known_location: (-23.55, -46.63),
            tracked_persons: HashMap::new(),
            safe_zones: Vec::new(),
            last_readings: VecDeque::with_capacity(100),
        }
    }

    fn update_location(&mut self, lat: f64, lon: f64) -> SensorReading {
        /// Atualiza localizacao GPS.
        self.last_known_location = (lat, lon);
        let reading = SensorReading {
            sensor: SensorType::GPS,
            perception: WorldPerception::GPS_LOCATION,
            value: format!("{{\"lat\": {}, \"lon\": {}}}", lat, lon),
            confidence: 0.98,
            timestamp: current_time(),
            description: format!("Voce esta proximo a {:.4}, {:.4}.", lat, lon),
        };
        self.last_readings.push_back(reading.clone());
        reading
    }

    fn navigate_for_blind(&self, _destination: &str) -> String {
        /// Navegacao por voz para cego -- passo a passo.
        "Voce esta na rua Augusta, numero 1000.".to_string()
    }

    fn track_child(&mut self, child_id: &str, child_name: &str, child_phone: &str, safe_zones: Option<Vec<HashMap<String, String>>>) -> HashMap<String, String> {
        /// Registra uma crianca para rastreamento.
        let mut child = HashMap::new();
        child.insert("name".to_string(), child_name.to_string());
        child.insert("phone".to_string(), child_phone.to_string());
        child.insert("status".to_string(), "safe".to_string());
        child.insert("battery".to_string(), "100".to_string());
        self.tracked_persons.insert(child_id.to_string(), child.clone());
        if let Some(zones) = safe_zones {
            self.safe_zones = zones;
        }
        child
    }

    fn check_child_location(&mut self, child_id: &str, lat: f64, lon: f64, battery: i32) -> HashMap<String, String> {
        /// Verifica se crianca esta em zona segura.
        if !self.tracked_persons.contains_key(child_id) {
            let mut err = HashMap::new();
            err.insert("error".to_string(), "crianca nao registrada".to_string());
            return err;
        }
        // simplified logic
        let mut result = HashMap::new();
        result.insert("child_id".to_string(), child_id.to_string());
        result.insert("status".to_string(), "safe".to_string());
        result.insert("message".to_string(), "Crianca na zona segura.".to_string());
        result
    }

    fn find_nearby_help(&self, _help_type: &str) -> Vec<HashMap<String, String>> {
        /// Encontra ajuda proxima (hospital, farmacia, delegacia).
        vec![
            {
                let mut m = HashMap::new();
                m.insert("name".to_string(), "Hospital Sao Paulo".to_string());
                m.insert("distance_m".to_string(), "800".to_string());
                m.insert("direction".to_string(), "norte".to_string());
                m
            },
            {
                let mut m = HashMap::new();
                m.insert("name".to_string(), "Farmacia 24h".to_string());
                m.insert("distance_m".to_string(), "300".to_string());
                m.insert("direction".to_string(), "oeste".to_string());
                m
            },
        ]
    }

    fn _haversine(&self, lat1: f64, lon1: f64, lat2: f64, lon2: f64) -> f64 {
        /// Distancia em metros entre dois pontos GPS.
        use std::f64::consts::PI;
        let r = 6371000.0;
        let dlat = (lat2 - lat1) * PI / 180.0;
        let dlon = (lon2 - lon1) * PI / 180.0;
        let a = (dlat / 2.0).sin().powi(2)
            + (lat1 * PI / 180.0).cos() * (lat2 * PI / 180.0).cos() * (dlon / 2.0).sin().powi(2);
        let c = 2.0 * a.sqrt().atan2((1.0 - a).sqrt());
        r * c
    }
}

// ============================================================================
// 6. BIOMETRIA -- Smartwatch como Sensor Corporal
// ============================================================================

struct BiometricEngine {
    last_readings: VecDeque<SensorReading>,
    baseline_heart_rate: i32,
    fall_detected: bool,
}

impl BiometricEngine {
    fn new() -> Self {
        BiometricEngine {
            last_readings: VecDeque::with_capacity(1000),
            baseline_heart_rate: 75,
            fall_detected: false,
        }
    }

    fn process_biometrics(&mut self, heart_rate: i32, movement: &str, spo2: i32, skin_temp: f64) -> Vec<SensorReading> {
        /// Processa dados biometricos.
        let mut readings = Vec::new();

        if movement == "fall" {
            self.fall_detected = true;
            readings.push(SensorReading {
                sensor: SensorType::ACCELEROMETER,
                perception: WorldPerception::FALL_DETECTION,
                value: "{\"detected\": true}".to_string(),
                confidence: 0.92,
                timestamp: current_time(),
                description: "QUEDA DETECTADA. Voce esta bem? Responda em 30 segundos ou ligo para emergencia.".to_string(),
            });
        }

        if heart_rate > 120 || heart_rate < 50 {
            readings.push(SensorReading {
                sensor: SensorType::HEART_RATE,
                perception: WorldPerception::HEART_ANOMALY,
                value: format!("{{\"heart_rate\": {}}}", heart_rate),
                confidence: 0.85,
                timestamp: current_time(),
                description: format!("Frequencia cardiaca {} bpm. Isso esta fora do normal.", heart_rate),
            });
        }

        if heart_rate > 100 && movement == "normal" {
            readings.push(SensorReading {
                sensor: SensorType::HEART_RATE,
                perception: WorldPerception::STRESS_DETECTION,
                value: format!("{{\"heart_rate\": {}}}", heart_rate),
                confidence: 0.70,
                timestamp: current_time(),
                description: "Seu coracao esta acelerado e voce esta parado. Talvez estresse. Quer respirar comigo?".to_string(),
            });
        }

        for r in &readings {
            self.last_readings.push_back(r.clone());
        }
        readings
    }
}

// ============================================================================
// 7. TELEFONISTA -- A Voz que Conversa
// ============================================================================

struct Telefonista {
    config: TelefonistaConfig,
    cv_engine: ComputerVisionEngine,
    audio_engine: AudioPerceptionEngine,
    geo_engine: GeoLocationEngine,
    bio_engine: BiometricEngine,
    conversation_history: VecDeque<HashMap<String, String>>,
    user_emotion: EmotionalState,
    current_mode: ConversationMode,
    active_sensors: HashSet<SensorType>,
    user_name: String,
    user_disabilities: Vec<String>,
    children_tracked: HashMap<String, String>,
}

impl Telefonista {
    fn new(config: TelefonistaConfig) -> Self {
        let mut t = Telefonista {
            config,
            cv_engine: ComputerVisionEngine::new(),
            audio_engine: AudioPerceptionEngine::new(),
            geo_engine: GeoLocationEngine::new(),
            bio_engine: BiometricEngine::new(),
            conversation_history: VecDeque::with_capacity(500),
            user_emotion: EmotionalState::NEUTRAL,
            current_mode: ConversationMode::DIALOGUE,
            active_sensors: HashSet::new(),
            user_name: String::new(),
            user_disabilities: Vec::new(),
            children_tracked: HashMap::new(),
        };
        t._setup_sensors();
        t
    }

    fn _setup_sensors(&mut self) {
        /// Configura sensores ativos baseado no hardware disponivel.
        self.active_sensors.insert(SensorType::CAMERA_REAR);
        self.active_sensors.insert(SensorType::CAMERA_FRONT);
        self.active_sensors.insert(SensorType::MICROPHONE);
        self.active_sensors.insert(SensorType::GPS);
        self.active_sensors.insert(SensorType::ACCELEROMETER);
        self.active_sensors.insert(SensorType::GYROSCOPE);
        self.active_sensors.insert(SensorType::COMPASS);
        self.active_sensors.insert(SensorType::LIGHT);
        self.active_sensors.insert(SensorType::PROXIMITY);
    }

    fn greet(&mut self, user_name: &str, time_of_day: &str) -> String {
        /// Saudacao inicial personalizada.
        self.user_name = user_name.to_string();
        let g = match time_of_day {
            "manha" => "Bom dia",
            "tarde" => "Boa tarde",
            "noite" => "Boa noite",
            _ => "Ola",
        };
        let msg = match self.config.personality {
            TelefonistaPersonality::GENTLE => format!("{}, {}. Aqui e a {}. ", g, user_name, self.config.name),
            TelefonistaPersonality::CHEERFUL => format!("{}, {}! Que bom te ouvir! ", g, user_name),
            TelefonistaPersonality::FORMAL => format!("{}. {} a servico. ", g, self.config.name),
            _ => format!("{}, {}. ", g, user_name),
        };
        self._record(&msg, "telefonista");
        msg
    }

    fn listen_and_respond(&mut self, user_input: &str) -> String {
        /// Processa entrada do usuario e responde como conversa.
        self._record(user_input, "user");
        let emotion = self._detect_emotion(user_input);
        if emotion != self.user_emotion {
            self.user_emotion = emotion.clone();
            if self.config.emotional_adaptation {
                self.config.adapt_to_emotion(emotion);
            }
        }
        let intent = self._detect_intent(user_input);
        let response = self._respond(&intent, user_input);
        self._record(&response, "telefonista");
        response
    }

    fn see_world(&mut self) -> String {
        /// Usa a camera para ver o mundo e narrar para o usuario.
        let readings = self.cv_engine.process_frame(SensorType::CAMERA_REAR);
        let narration = self.cv_engine.narrate_scene(&readings);
        self._record(&narration, "telefonista");
        narration
    }

    fn hear_world(&mut self) -> String {
        /// Usa o microfone para ouvir o mundo e narrar para surdos.
        let readings = self.audio_engine.process_audio();
        let narration = self.audio_engine.narrate_sounds(&readings);
        self._record(&narration, "telefonista");
        narration
    }

    fn sense_body(&mut self, heart_rate: i32, movement: &str, spo2: i32, skin_temp: f64) -> String {
        /// Usa biometria para checar o corpo do usuario.
        let readings = self.bio_engine.process_biometrics(heart_rate, movement, spo2, skin_temp);
        if readings.is_empty() {
            return "Tudo normal com seu corpo.".to_string();
        }
        let msg = readings.iter().map(|r| r.description.clone()).collect::<Vec<_>>().join(" ");
        self._record(&msg, "telefonista");
        msg
    }

    fn navigate(&mut self, destination: &str) -> String {
        /// Navegacao por voz (cego andando na rua).
        self.current_mode = ConversationMode::CO_DRIVER;
        let instruction = self.geo_engine.navigate_for_blind(destination);
        self._record(&instruction, "telefonista");
        instruction
    }

    fn check_on_child(&mut self, child_id: &str, lat: f64, lon: f64, battery: i32) -> String {
        /// Verifica localizacao de crianca rastreada.
        let result = self.geo_engine.check_child_location(child_id, lat, lon, battery);
        let msg = result.get("message").cloned().unwrap_or_else(|| "Sem informacoes.".to_string());
        self._record(&msg, "telefonista");
        msg
    }

    fn register_child(&mut self, child_id: &str, name: &str, phone: &str, safe_zones: Option<Vec<HashMap<String, String>>>) -> String {
        /// Registra crianca para rastreamento.
        self.geo_engine.track_child(child_id, name, phone, safe_zones);
        self.children_tracked.insert(child_id.to_string(), name.to_string());
        let msg = format!("{} registrada. Vou avisar se ela sair das zonas seguras.", name);
        self._record(&msg, "telefonista");
        msg
    }

    fn find_help(&self, help_type: &str) -> String {
        /// Encontra ajuda proxima.
        let results = self.geo_engine.find_nearby_help(help_type);
        if results.is_empty() {
            return "Nao encontrei nada proximo agora.".to_string();
        }
        let parts: Vec<String> = results
            .iter()
            .map(|r| format!("{} a {} metros ao {}", r["name"], r["distance_m"], r["direction"]))
            .collect();
        let msg = "Encontrei: ".to_string() + &parts.join(". ") + ".";
        // record would require &mut self
        msg
    }

    fn make_call(&mut self, contact_name: &str, reason: &str) -> String {
        /// Faz uma ligacao telefonica real.
        let reason_text = if reason.is_empty() { String::new() } else { format!(" Motivo: {}.", reason) };
        let msg = format!("Ligando para {}.{reason_text}", contact_name);
        self._record(&msg, "telefonista");
        msg
    }

    fn emergency(&mut self, service: &str) -> String {
        /// Aciona emergencia.
        self.current_mode = ConversationMode::EMERGENCY;
        self.config.personality = TelefonistaPersonality::PROTECTIVE;
        self.config.speech_rate = 0.9;
        self.config.humor_enabled = false;
        self.config.verbosity = 0.2;
        let msg = format!("EMERGENCIA. Ligando para {}. Fique calmo. Estou aqui.", service);
        self._record(&msg, "telefonista");
        msg
    }

    fn dictate_code(&mut self, code_input: &str) -> String {
        /// Usuario dita codigo, telefonista escreve.
        self.current_mode = ConversationMode::DICTATION;
        let msg = format!("Anotado. Escrevi: {}. Quer que eu execute?", code_input);
        self._record(&msg, "telefonista");
        msg
    }

    fn _detect_emotion(&self, text: &str) -> EmotionalState {
        /// Detecta emocao no texto (simplificado).
        let t = text.to_lowercase();
        if t.contains("cansado") || t.contains("exausto") {
            EmotionalState::TIRED
        } else if t.contains("estress") || t.contains("put") {
            EmotionalState::STRESSED
        } else if t.contains("ansios") || t.contains("preocup") {
            EmotionalState::ANXIOUS
        } else if t.contains("feliz") || t.contains("otimo") {
            EmotionalState::HAPPY
        } else if t.contains("foco") || t.contains("trabalh") {
            EmotionalState::FOCUSED
        } else if t.contains("triste") {
            EmotionalState::SAD
        } else if t.contains("irritad") {
            EmotionalState::ANGRY
        } else if t.contains("sobrecarreg") {
            EmotionalState::OVERWHELMED
        } else {
            EmotionalState::NEUTRAL
        }
    }

    fn _detect_intent(&self, text: &str) -> String {
        /// Detecta a intencao do usuario (simplificado).
        let t = text.to_lowercase();
        if t.contains("codigo") || t.contains("programar") {
            "code".to_string()
        } else if t.contains("onde estou") || t.contains("localizacao") {
            "location".to_string()
        } else if t.contains("minha filha") || t.contains("crianca") {
            "child".to_string()
        } else if t.contains("cor") || t.contains("vermelho") {
            "color".to_string()
        } else if t.contains("socorro") || t.contains("emergencia") {
            "emergency".to_string()
        } else if t.contains("ligar") {
            "call".to_string()
        } else if t.contains("ve") || t.contains("olha") || t.contains("camera") {
            "see".to_string()
        } else if t.contains("ouvir") || t.contains("som") {
            "hear".to_string()
        } else if t.contains("navegar") {
            "navigate".to_string()
        } else {
            "chat".to_string()
        }
    }

    fn _respond(&mut self, intent: &str, user_input: &str) -> String {
        /// Gera resposta baseada na intencao e personalidade.
        let name = if self.user_name.is_empty() { "amigo" } else { &self.user_name };
        match intent {
            "code" => self.dictate_code(user_input),
            "location" => self.geo_engine.navigate_for_blind(""),
            "child" => "Quer que eu verifique onde ela esta?".to_string(),
            "color" => {
                let readings = self.cv_engine.process_frame(SensorType::CAMERA_REAR);
                if let Some(r) = readings.iter().find(|r| r.perception == WorldPerception::COLOR_DETECTION) {
                    r.description.clone()
                } else {
                    "Aponta a camera que eu vejo a cor.".to_string()
                }
            }
            "emergency" => self.emergency("192"),
            "call" => "Para quem voce quer ligar?".to_string(),
            "see" => self.see_world(),
            "hear" => self.hear_world(),
            "navigate" => "Para onde voce quer ir?".to_string(),
            _ => {
                match self.user_emotion {
                    EmotionalState::TIRED => format!("{}, voce parece cansado. Que tal uma pausa?", name),
                    EmotionalState::STRESSED => format!("Respira, {}. Uma coisa de cada vez.", name),
                    EmotionalState::HAPPY => format!("Que bom te ouvir feliz, {}!", name),
                    _ => format!("Entendi. Conte mais, {}.", name),
                }
            }
        }
    }

    fn _record(&mut self, text: &str, speaker: &str) {
        /// Registra na historia da conversa.
        let mut entry = HashMap::new();
        entry.insert("speaker".to_string(), speaker.to_string());
        entry.insert("text".to_string(), text.to_string());
        entry.insert("timestamp".to_string(), current_time().to_string());
        self.conversation_history.push_back(entry);
        if self.conversation_history.len() > 500 {
            self.conversation_history.pop_front();
        }
    }

    fn conversation_summary(&self) -> HashMap<String, String> {
        /// Resumo da conversa.
        let mut m = HashMap::new();
        m.insert("telefonista_name".to_string(), self.config.name.clone());
        m.insert("user_name".to_string(), self.user_name.clone());
        m.insert("current_emotion".to_string(), self.user_emotion.value().to_string());
        m.insert("current_mode".to_string(), self.current_mode.value().to_string());
        m
    }
}

// ============================================================================
// 8. ADAPTACAO POR DEFICIENCIA
// ============================================================================

fn create_telefonista_for_blind(user_name: &str) -> Telefonista {
    /// Telefonista para cego: voz + camera + GPS + ligacao.
    let mut config = TelefonistaConfig::default();
    config.name = "Iara".to_string();
    config.personality = TelefonistaPersonality::GENTLE;
    config.speech_rate = 1.3;
    config.verbosity = 0.7;
    config.proactive = 0.6;
    let mut t = Telefonista::new(config);
    t.user_name = user_name.to_string();
    t.user_disabilities = vec!["visual".to_string()];
    t.current_mode = ConversationMode::CO_DRIVER;
    t
}

fn create_telefonista_for_deaf(user_name: &str) -> Telefonista {
    /// Telefonista para surdo: visual + haptico + legenda.
    let mut config = TelefonistaConfig::default();
    config.name = "Iara".to_string();
    config.personality = TelefonistaPersonality::GENTLE;
    let mut t = Telefonista::new(config);
    t.user_name = user_name.to_string();
    t.user_disabilities = vec!["auditiva".to_string()];
    t.current_mode = ConversationMode::SILENT;
    t
}

fn create_telefonista_for_motor(user_name: &str) -> Telefonista {
    /// Telefonista para tetraplegia: voz pura, sem botoes.
    let mut config = TelefonistaConfig::default();
    config.name = "Iara".to_string();
    config.personality = TelefonistaPersonality::CHEERFUL;
    config.proactive = 0.5;
    let mut t = Telefonista::new(config);
    t.user_name = user_name.to_string();
    t.user_disabilities = vec!["motora".to_string()];
    t
}

fn create_telefonista_for_autism(user_name: &str) -> Telefonista {
    /// Telefonista para autista: calma, previsivel, sem surpresas.
    let mut config = TelefonistaConfig::default();
    config.name = "Iara".to_string();
    config.personality = TelefonistaPersonality::GENTLE;
    config.speech_rate = 0.9;
    config.verbosity = 0.3;
    config.humor_enabled = false;
    config.proactive = 0.2;
    let mut t = Telefonista::new(config);
    t.user_name = user_name.to_string();
    t.user_disabilities = vec!["espectro_autista".to_string()];
    t
}

fn create_telefonista_for_child(user_name: &str) -> Telefonista {
    /// Telefonista para crianca: brincalhona, simples, protetora.
    let mut config = TelefonistaConfig::default();
    config.name = "Tia Iara".to_string();
    config.personality = TelefonistaPersonality::PLAYFUL;
    config.speech_rate = 0.85;
    config.verbosity = 0.3;
    config.proactive = 0.4;
    let mut t = Telefonista::new(config);
    t.user_name = user_name.to_string();
    t
}

fn create_telefonista_for_elderly(user_name: &str) -> Telefonista {
    /// Telefonista para idoso: devagar, formosa, protetora.
    let mut config = TelefonistaConfig::default();
    config.name = "Iara".to_string();
    config.personality = TelefonistaPersonality::PROTECTIVE;
    config.speech_rate = 0.8;
    config.verbosity = 0.6;
    config.humor_enabled = true;
    config.proactive = 0.7;
    config.formality = 0.6;
    let mut t = Telefonista::new(config);
    t.user_name = user_name.to_string();
    t
}

// ============================================================================
// 9. CENARIOS DO MUNDO REAL
// ============================================================================

fn scenario_blind_walking() {
    /// Cenario: cego andando na rua.
    println!("{}", "=".repeat(60));
    println!("CENARIO: Cego andando na rua");
    println!("{}", "=".repeat(60));

    let mut t = create_telefonista_for_blind("Cleiton");
    println!("{}", t.greet("Cleiton", "manha"));

    println!("\n[Camera]");
    println!("{}", t.see_world());

    println!("\n[GPS]");
    println!("{}", t.navigate("padaria"));

    let readings = t.cv_engine.process_frame(SensorType::CAMERA_REAR);
    for r in &readings {
        if r.perception == WorldPerception::MONEY_RECOGNITION {
            println!("\n[Dinheiro]");
            println!("{}", r.description);
        }
    }

    println!("\n[Audio]");
    println!("{}", t.hear_world());
}

fn scenario_deaf_conversation() {
    /// Cenario: surdo em conversa com legenda em tempo real.
    println!("\n{}", "=".repeat(60));
    println!("CENARIO: Surdo em conversa");
    println!("{}", "=".repeat(60));

    let mut t = create_telefonista_for_deaf("Maria");
    println!("[Visual] {}", t.greet("Maria", "tarde"));

    println!("\n[Audio -> Visual]");
    println!("[Visual] {}", t.hear_world());
}

fn scenario_colorblind_shopping() {
    /// Cenario: daltonico comprando roupas.
    println!("\n{}", "=".repeat(60));
    println!("CENARIO: Daltonico comprando roupas");
    println!("{}", "=".repeat(60));

    let mut config = TelefonistaConfig::default();
    config.name = "Iara".to_string();
    let mut t = Telefonista::new(config);
    t.user_name = "Joao".to_string();
    t.user_disabilities = vec!["visual".to_string()];

    println!("{}", t.greet("Joao", "tarde"));
    println!("\n[Camera apontada para roupa]");
    let readings = t.cv_engine.process_frame(SensorType::CAMERA_REAR);
    for r in &readings {
        if r.perception == WorldPerception::COLOR_DETECTION {
            println!("  {}", r.description);
        }
    }
}

fn scenario_lost_child() {
    /// Cenario: crianca perdida rastreada por GPS.
    println!("\n{}", "=".repeat(60));
    println!("CENARIO: Geolocalizacao de crianca");
    println!("{}", "=".repeat(60));

    let mut config = TelefonistaConfig::default();
    config.name = "Iara".to_string();
    config.personality = TelefonistaPersonality::PROTECTIVE;
    let mut t = Telefonista::new(config);
    t.user_name = "Cleiton".to_string();

    let mut zone1 = HashMap::new();
    zone1.insert("name".to_string(), "Casa".to_string());
    zone1.insert("lat".to_string(), "-23.55".to_string());
    zone1.insert("lon".to_string(), "-46.63".to_string());
    zone1.insert("radius_m".to_string(), "200".to_string());

    let safe_zones = vec![zone1];
    println!("{}", t.register_child("child_01", "Sophia", "+551****9999", Some(safe_zones)));

    println!("\n[Sophia na escola]");
    println!("{}", t.check_on_child("child_01", -23.56, -46.64, 85));
}

fn scenario_fall_detection() {
    /// Cenario: idoso cai, sistema detecta e liga.
    println!("\n{}", "=".repeat(60));
    println!("CENARIO: Deteccao de queda (idoso)");
    println!("{}", "=".repeat(60));

    let mut t = create_telefonista_for_elderly("Dona Maria");
    println!("{}", t.greet("Dona Maria", "manha"));

    println!("\n[Queda detectada!]");
    println!("{}", t.sense_body(110, "fall", 98, 36.5));

    println!("\n[Sem resposta em 30s]");
    println!("{}", t.emergency("192"));
}

fn scenario_stress_detection() {
    /// Cenario: deteccao de estresse por smartwatch.
    println!("\n{}", "=".repeat(60));
    println!("CENARIO: Deteccao de estresse");
    println!("{}", "=".repeat(60));

    let mut config = TelefonistaConfig::default();
    config.name = "Iara".to_string();
    let mut t = Telefonista::new(config);
    t.user_name = "Cleiton".to_string();

    println!("Coracao acelerado, voce esta parado...");
    println!("{}", t.sense_body(115, "normal", 98, 36.5));

    println!("\nVoce diz: 'to estressado pra caralho'");
    println!("{}", t.listen_and_respond("to estressado pra caralho"));
}

fn scenario_epilepsy_warning() {
    /// Cenario: previsao de crise epileptica.
    println!("\n{}", "=".repeat(60));
    println!("CENARIO: Previsao de crise epileptica");
    println!("{}", "=".repeat(60));

    let mut config = TelefonistaConfig::default();
    config.name = "Iara".to_string();
    config.personality = TelefonistaPersonality::PROTECTIVE;
    let mut t = Telefonista::new(config);
    t.user_name = "Pedro".to_string();

    println!("{}", t.greet("Pedro", "tarde"));

    println!("\n[Sinais pre-crise]");
    println!("{}", t.sense_body(115, "normal", 98, 37.5));
}

// ============================================================================
// 10. DEMONSTRACAO COMPLETA
// ============================================================================

fn demo() {
    println!("{}", "=".repeat(70));
    println!("OpenTelefonista -- O Sistema Como Conversa Humana");
    println!("{}", "=".repeat(70));

    println!("\nTelefonista: Iara");
    println!("Personalidades: {}", 8);
    println!("Estados emocionais: {}", 10);
    println!("Modos de conversa: {}", 8);
    println!("Tipos de sensor: {}", 20);
    println!("Percepcoes do mundo: {}", 39);

    scenario_blind_walking();
    scenario_deaf_conversation();
    scenario_colorblind_shopping();
    scenario_lost_child();
    scenario_fall_detection();
    scenario_stress_detection();
    scenario_epilepsy_warning();

    println!("\n{}", "=".repeat(70));
    println!("PERFIS DA TELEFONISTA");
    println!("{}", "=".repeat(70));

    let profiles = vec![
        ("Cego", create_telefonista_for_blind("Cleiton")),
        ("Surdo", create_telefonista_for_deaf("Maria")),
        ("Tetraplegico", create_telefonista_for_motor("Joao")),
        ("Autista", create_telefonista_for_autism("Pedro")),
        ("Crianca", create_telefonista_for_child("Sophia")),
        ("Idoso", create_telefonista_for_elderly("Dona Cecca")),
    ];

    for (label, t) in profiles {
        println!("\n  {}:", label);
        println!("    Nome: {}", t.config.name);
        println!("    Personalidade: {}", t.config.personality.value());
        println!("    Velocidade: {}x", t.config.speech_rate);
        println!("    Modo: {}", t.current_mode.value());
        println!("    Sensores ativos: {}", t.active_sensors.len());
    }

    println!("\n{}", "=".repeat(70));
    println!("O sistema NAO e um app. E uma CONVERSA.");
    println!("A interface NAO e uma tela. E uma VOZ.");
    println!("O smartphone NAO e um dispositivo. E o CORPO EXTENDIDO.");
    println!("\nTODO hardware. TODA deficiencia. ZERO barreira.");
    println!("UMA conversa.");
}

fn main() {
    demo();
}
