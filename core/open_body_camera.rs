// OpenBodyCamera -- Smartphone como Camera Corporal + Fone Bluetooth = Olhos do Cego
// ===================================================================================
// "O cego nao precisa de olhos. Precisa de INFORMACAO.
// O smartphone na camisa capta o mundo.
// O fone no ouvido TRADUZ o mundo em voz.
// O cego VE com a camera. OUVE com o fone.
// NADA o para. NINGUEM o limita.
//
// A camera corporal e um PAR DE OLHOS emprestado.
// O fone bluetooth e um PAR DE OUVIDOS que falam.
// Juntos, sao o CORPO EXTENDIDO do cego na rua."
//
// COMO FUNCIONA:
// 1. Smartphone preso no peito (clip de camisa/bolsinho)
// 2. Camera traseira aponta para frente
// 3. IA processa o video em tempo real (15-30 fps)
// 4. Fone bluetooth recebe descricao por voz
// 5.Usuario anda COM INFORMACAO
//
// O QUE A CAMERA VE E DESCREVE:
// - Obstaculos (poste, buraco, degrau, carro)
// - Pessoas (quem e, quantas, proximidade)
// - Textos (placas, menus, cartazes)
// - Cores (semaforo, cedulas, roupas)
// - Cena (restaurante, farmacia, rua, park)
// - Perigos (moto approaching, objeto caindo)
// - Orientacao (vire a direita, continue reto)
//
// NIVEIS DE VERBALIZACAO:
// - CONTINUO: descreve tudo o tempo todo (para iniciantes)
// - POR DEMANDA: so descreve quando perguntado (para avancados)
// - ALERTA: so fala em situacoes de perigo (para expertos)
// - TATEANDO: descricao minima + sons direcionais (hiper-minimal)
//
// MODO CO-PILOTO DE RUA:
// A camera vira GPS visual. A voz no fone guia:
// 'Desca a calcada. Continue reto. Poste a esquerda em 3m.
// Semaforo verde. Atravesse 15 passos. Farmacia a direita.
// Seu destino e a porta azul, 10 metros.'
//
// INTEGRACAO COM OPENHARDWARE:
// - Smartphone: camera + processamento
// - Fone bluetooth: saida de voz
// - Smartwatch: vibracall para alertas criticos
// - Bateria gerenciada por OpenResilience
// - Emergency: OpenHumanNet se algo der errado
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// =============================================================================

use std::collections::VecDeque;
use std::time::{SystemTime, UNIX_EPOCH};

// ============================================================================
// 1. TIPOS DE MONTAGEM (Como o smartphone fica no corpo)
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum MountPosition {
    Chest,              // clipped na camisa, no peito -- padrao
    Head,               // bandana/oculos com smartphone
    Shoulder,           // alça de mochila
    Neck,               // pendurado no pescoco
    Hand,               // na mao apontando
    PocketFacingOut,    // no bolso com camera pra fora
    Armband,            // bracelete de braco
}

impl MountPosition {
    pub fn value(&self) -> &'static str {
        match self {
            MountPosition::Chest => "peito",
            MountPosition::Head => "cabeca",
            MountPosition::Shoulder => "ombro",
            MountPosition::Neck => "pescoco",
            MountPosition::Hand => "mao",
            MountPosition::PocketFacingOut => "bolso_frente",
            MountPosition::Armband => "braceaco",
        }
    }
}

// ============================================================================
// 2. MODOS DE CAMERA
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum CameraMode {
    Continuous,     // descreve tudo o tempo todo
    OnDemand,       // so quando usuario pede
    AlertOnly,      // so perigos
    Navigation,     // co-piloto de rua
    Reading,        // modo OCR (ler texto)
    Money,          // reconhecer cedulas
    Color,          // identificar cores
    Face,           // reconhecer pessoas
    Search,         // procurar objeto especifico
    Minimal,        // tateando (hiper-minimal)
}

impl CameraMode {
    pub fn value(&self) -> &'static str {
        match self {
            CameraMode::Continuous => "continuo",
            CameraMode::OnDemand => "sob_demanda",
            CameraMode::AlertOnly => "so_alerta",
            CameraMode::Navigation => "navegacao",
            CameraMode::Reading => "leitura",
            CameraMode::Money => "dinheiro",
            CameraMode::Color => "cor",
            CameraMode::Face => "rosto",
            CameraMode::Search => "busca",
            CameraMode::Minimal => "minimal",
        }
    }
}

// ============================================================================
// 3. NIVEIS DE VERBOSIDADE
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum VerbosityLevel {
    High,       // descreve tudo em detalhe
    Medium,     // descreve o essencial
    Low,        // so alertas e orientacao
    Whisper,    // minimo possivel (1 palavra)
}

impl VerbosityLevel {
    pub fn value(&self) -> &'static str {
        match self {
            VerbosityLevel::High => "alto",
            VerbosityLevel::Medium => "medio",
            VerbosityLevel::Low => "baixo",
            VerbosityLevel::Whisper => "sussurro",
        }
    }
}

// ============================================================================
// 4. DETECCOES VISUAIS
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ObjectType {
    Obstacle,
    Person,
    Vehicle,
    Animal,
    Sign,
    Door,
    Stairs,
    Crosswalk,
    TrafficLight,
    Text,
    Money,
    Product,
    Food,
    Medicine,
    Furniture,
    Tool,
    Nature,
}

impl ObjectType {
    pub fn value(&self) -> &'static str {
        match self {
            ObjectType::Obstacle => "obstaculo",
            ObjectType::Person => "pessoa",
            ObjectType::Vehicle => "veiculo",
            ObjectType::Animal => "animal",
            ObjectType::Sign => "placa",
            ObjectType::Door => "porta",
            ObjectType::Stairs => "escada",
            ObjectType::Crosswalk => "faixa",
            ObjectType::TrafficLight => "semaforo",
            ObjectType::Text => "texto",
            ObjectType::Money => "dinheiro",
            ObjectType::Product => "produto",
            ObjectType::Food => "comida",
            ObjectType::Medicine => "remedio",
            ObjectType::Furniture => "movel",
            ObjectType::Tool => "ferramenta",
            ObjectType::Nature => "natureza",
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum DangerLevel {
    Safe,
    Attention,
    Warning,
    Danger,
    Critical,
}

impl DangerLevel {
    pub fn value(&self) -> &'static str {
        match self {
            DangerLevel::Safe => "seguro",
            DangerLevel::Attention => "atencao",
            DangerLevel::Warning => "aviso",
            DangerLevel::Danger => "perigo",
            DangerLevel::Critical => "critico",
        }
    }
}

#[derive(Debug, Clone)]
pub struct Detection {
    pub object_type: ObjectType,
    pub label: String,
    pub distance_m: f64,
    pub direction: String,
    pub danger: DangerLevel,
    pub confidence: f64,
    pub action: String,
    pub voice_description: String,
    pub timestamp: f64,
    pub size: String,
    pub moving: bool,
    pub approaching: bool,
}

impl Detection {
    pub fn new(
        object_type: ObjectType,
        label: &str,
        distance_m: f64,
        direction: &str,
        danger: DangerLevel,
        confidence: f64,
        action: &str,
        voice_description: &str,
        moving: bool,
        approaching: bool,
    ) -> Self {
        Detection {
            object_type,
            label: label.to_string(),
            distance_m,
            direction: direction.to_string(),
            danger,
            confidence,
            action: action.to_string(),
            voice_description: voice_description.to_string(),
            timestamp: SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .unwrap()
                .as_secs_f64(),
            size: String::new(),
            moving,
            approaching,
        }
    }
}

// ============================================================================
// 5. MOTOR DE VISAO COMPUTACIONAL
// ============================================================================

pub struct VisionEngine {
    pub mount: MountPosition,
    pub detections_history: VecDeque<Detection>,
    pub last_scene: String,
    pub frame_count: u32,
    pub fps: f64,
    pub processing_latency_ms: f64,
}

impl VisionEngine {
    pub fn new(mount: MountPosition) -> Self {
        VisionEngine {
            mount,
            detections_history: VecDeque::with_capacity(200),
            last_scene: String::new(),
            frame_count: 0,
            fps: 15.0,
            processing_latency_ms: 80.0,
        }
    }

    pub fn process_frame(&mut self, mode: CameraMode) -> Vec<Detection> {
        self.frame_count += 1;
        let detections = match mode {
            CameraMode::Navigation => self._scan_navigation(),
            CameraMode::Reading => self._scan_text(),
            CameraMode::Money => self._scan_money(),
            CameraMode::Color => self._scan_color(),
            CameraMode::Face => self._scan_faces(),
            CameraMode::Search => self._scan_search(),
            _ => self._scan_continuous(),
        };
        for d in &detections {
            self.detections_history.push_back(d.clone());
            if self.detections_history.len() > 200 {
                self.detections_history.pop_front();
            }
        }
        detections
    }

    fn _scan_continuous(&self) -> Vec<Detection> {
        vec![
            Detection::new(
                ObjectType::Person, "Pessoa", 3.0, "frente",
                DangerLevel::Safe, 0.92,
                "Pessoa a 3 metros a frente.",
                "Pessoa a frente, 3 metros.",
                true, false,
            ),
            Detection::new(
                ObjectType::Obstacle, "Poste", 5.0, "frente-esquerda",
                DangerLevel::Attention, 0.88,
                "Poste a 5 metros. Mantenha a direita.",
                "Poste a esquerda, 5 metros.",
                false, false,
            ),
            Detection::new(
                ObjectType::Vehicle, "Carro estacionado", 2.5, "direita",
                DangerLevel::Safe, 0.95,
                "",
                "Carro estacionado a direita.",
                false, false,
            ),
        ]
    }

    fn _scan_navigation(&self) -> Vec<Detection> {
        vec![
            Detection::new(
                ObjectType::Crosswalk, "Faixa de pedestre", 8.0, "frente",
                DangerLevel::Safe, 0.90,
                "Continue reto. Faixa de pedestre em 8 metros.",
                "Faixa de pedestre a frente, 8 metros. Continue reto.",
                false, false,
            ),
            Detection::new(
                ObjectType::TrafficLight, "Semaforo", 8.0, "frente-alto",
                DangerLevel::Safe, 0.97,
                "Semaforo VERDE. Pode atravessar.",
                "Semaforo verde. Pode atravessar.",
                false, false,
            ),
            Detection::new(
                ObjectType::Obstacle, "Buraco na calcada", 4.0, "frente-baixo",
                DangerLevel::Warning, 0.85,
                "Buraco a 4 metros. Desvie para a esquerda.",
                "Atencao! Buraco na calcada, 4 metros. Desvie a esquerda.",
                false, false,
            ),
        ]
    }

    fn _scan_text(&self) -> Vec<Detection> {
        vec![
            Detection::new(
                ObjectType::Text, "Placa de estabelecimento", 5.0, "frente-alto",
                DangerLevel::Safe, 0.91,
                "",
                "A placa diz: RESTAURANTE DO JOAO. Aberto das 11 as 22.",
                false, false,
            ),
            Detection::new(
                ObjectType::Text, "Cardapio", 3.0, "frente",
                DangerLevel::Safe, 0.88,
                "",
                "O cardapio diz: Feijoada R$ 25. Suco R$ 8. Prato feito R$ 18.",
                false, false,
            ),
        ]
    }

    fn _scan_money(&self) -> Vec<Detection> {
        vec![Detection::new(
            ObjectType::Money, "Nota de R$ 50", 0.5, "frente",
            DangerLevel::Safe, 0.96,
            "",
            "Nota de CINQUENTA REAIS. Cor marrom.",
            false, false,
        )]
    }

    fn _scan_color(&self) -> Vec<Detection> {
        vec![Detection::new(
            ObjectType::Sign, "Sinal vermelho", 10.0, "frente-alto",
            DangerLevel::Danger, 0.97,
            "Semaforo VERMELHO. PARE.",
            "Semaforo VERMELHO. Pare.",
            false, false,
        )]
    }

    fn _scan_faces(&self) -> Vec<Detection> {
        vec![Detection::new(
            ObjectType::Person, "MING (esposa)", 2.0, "frente",
            DangerLevel::Safe, 0.89,
            "",
            "MING esta a sua frente, 2 metros. Sorrindo.",
            false, false,
        )]
    }

    fn _scan_search(&self) -> Vec<Detection> {
        vec![Detection::new(
            ObjectType::Product, "Chave", 1.5, "mesa",
            DangerLevel::Safe, 0.82,
            "",
            "Encontrei a chave. Esta na mesa, a sua frente, 1 metro e meio.",
            false, false,
        )]
    }

    pub fn describe_scene(&self, detections: &[Detection], verbosity: VerbosityLevel) -> String {
        if detections.is_empty() {
            return if verbosity == VerbosityLevel::Whisper {
                "Livre.".to_string()
            } else {
                "Nada a frente. Caminho livre.".to_string()
            };
        }

        let mut sorted_dets: Vec<&Detection> = detections.iter().collect();
        sorted_dets.sort_by(|a, b| {
            let danger_order = |d: &DangerLevel| match d {
                DangerLevel::Critical => 5,
                DangerLevel::Danger => 4,
                DangerLevel::Warning => 3,
                DangerLevel::Attention => 2,
                DangerLevel::Safe => 1,
            };
            danger_order(&b.danger).cmp(&danger_order(&a.danger))
                .then_with(|| a.distance_m.partial_cmp(&b.distance_m).unwrap())
        });

        let mut descriptions: Vec<String> = Vec::new();
        for d in sorted_dets {
            match verbosity {
                VerbosityLevel::High => {
                    descriptions.push(d.voice_description.clone());
                }
                VerbosityLevel::Medium => {
                    let mut desc = d.voice_description.clone();
                    if desc.len() > 60 {
                        desc = format!("{}...", &desc[..57]);
                    }
                    descriptions.push(desc);
                }
                VerbosityLevel::Low => {
                    if matches!(d.danger, DangerLevel::Warning | DangerLevel::Danger | DangerLevel::Critical) {
                        descriptions.push(d.voice_description.clone());
                    }
                }
                VerbosityLevel::Whisper => {
                    if matches!(d.danger, DangerLevel::Danger | DangerLevel::Critical) {
                        let text = if !d.action.is_empty() { d.action.clone() } else { d.label.clone() };
                        descriptions.push(text);
                    }
                }
            }
        }

        if descriptions.is_empty() {
            "Livre.".to_string()
        } else {
            format!("{}.", descriptions.join(". "))
        }
    }
}

// ============================================================================
// 6. GERENCIADOR DE AUDIO BLUETOOTH
// ============================================================================

pub struct AudioOutputManager {
    pub connected: bool,
    pub device_name: String,
    pub battery_pct: f64,
    pub volume: f64,
    pub tts_rate: f64,
    pub last_spoken: String,
    pub last_spoken_time: f64,
    pub min_interval_s: f64,
    pub message_queue: VecDeque<String>,
    pub priority_queue: VecDeque<String>,
    pub total_messages: u32,
    pub messages_spoken: u32,
    pub messages_skipped: u32,
}

impl AudioOutputManager {
    pub fn new() -> Self {
        AudioOutputManager {
            connected: true,
            device_name: "Fone Bluetooth".to_string(),
            battery_pct: 100.0,
            volume: 0.7,
            tts_rate: 1.4,
            last_spoken: String::new(),
            last_spoken_time: 0.0,
            min_interval_s: 1.5,
            message_queue: VecDeque::with_capacity(50),
            priority_queue: VecDeque::with_capacity(20),
            total_messages: 0,
            messages_spoken: 0,
            messages_skipped: 0,
        }
    }

    pub fn speak(&mut self, message: &str, priority: DangerLevel) -> serde_json::Value {
        let now = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs_f64();
        self.total_messages += 1;

        let is_critical = matches!(priority, DangerLevel::Danger | DangerLevel::Critical);

        if message == self.last_spoken && !is_critical {
            if now - self.last_spoken_time < 5.0 {
                self.messages_skipped += 1;
                return serde_json::json!({"spoken": false, "reason": "duplicada"});
            }
        }

        if !is_critical && now - self.last_spoken_time < self.min_interval_s {
            self.message_queue.push_back(message.to_string());
            self.messages_skipped += 1;
            return serde_json::json!({"spoken": false, "reason": "intervalo"});
        }

        if is_critical {
            self.priority_queue.push_front(message.to_string());
        } else {
            self.message_queue.push_back(message.to_string());
        }

        self.last_spoken = message.to_string();
        self.last_spoken_time = now;
        self.messages_spoken += 1;

        serde_json::json!({
            "spoken": true,
            "message": message,
            "priority": priority.value(),
            "device": self.device_name,
            "volume": self.volume,
            "rate": self.tts_rate,
        })
    }

    pub fn process_queue(&mut self) -> Vec<String> {
        let mut spoken = Vec::new();
        let now = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs_f64();
        if now - self.last_spoken_time >= self.min_interval_s {
            if let Some(msg) = self.priority_queue.pop_front() {
                spoken.push(msg.clone());
                self.last_spoken = msg;
                self.last_spoken_time = now;
                self.messages_spoken += 1;
            } else if let Some(msg) = self.message_queue.pop_front() {
                spoken.push(msg.clone());
                self.last_spoken = msg;
                self.last_spoken_time = now;
                self.messages_spoken += 1;
            }
        }
        spoken
    }

    pub fn status(&self) -> serde_json::Value {
        serde_json::json!({
            "connected": self.connected,
            "device": self.device_name,
            "battery_pct": self.battery_pct,
            "volume": self.volume,
            "tts_rate": self.tts_rate,
            "queue_size": self.message_queue.len(),
            "priority_queue_size": self.priority_queue.len(),
            "total_messages": self.total_messages,
            "spoken": self.messages_spoken,
            "skipped": self.messages_skipped,
        })
    }
}

// ============================================================================
// 7. NAVEGACAO POR VOZ (Co-piloto de rua)
// ============================================================================

pub struct StreetNavigator {
    pub destination: String,
    pub current_step: usize,
    pub steps: Vec<serde_json::Value>,
    pub last_instruction: String,
    pub distance_remaining_m: f64,
    pub eta_minutes: f64,
}

impl StreetNavigator {
    pub fn new() -> Self {
        StreetNavigator {
            destination: String::new(),
            current_step: 0,
            steps: Vec::new(),
            last_instruction: String::new(),
            distance_remaining_m: 0.0,
            eta_minutes: 0.0,
        }
    }

    pub fn set_destination(&mut self, destination: &str, steps: Option<Vec<serde_json::Value>>) -> String {
        self.destination = destination.to_string();
        self.current_step = 0;
        self.steps = steps.unwrap_or_else(|| self._default_route(destination));
        self.distance_remaining_m = self.steps.iter()
            .map(|s| s.get("distance_m").and_then(|v| v.as_f64()).unwrap_or(100.0))
            .sum();
        self.eta_minutes = self.distance_remaining_m / 80.0;
        format!("Rota calculada para {}. {:.0} metros. Aproximadamente {:.0} minutos.",
                destination, self.distance_remaining_m, self.eta_minutes)
    }

    fn _default_route(&self, destination: &str) -> Vec<serde_json::Value> {
        vec![
            serde_json::json!({"instruction": "Saida do predio. Vire a direita na calcada.", "distance_m": 50}),
            serde_json::json!({"instruction": "Continue reto por 200 metros na rua Augusta.", "distance_m": 200}),
            serde_json::json!({"instruction": "Atencao: buraco a frente. Desvie a esquerda.", "distance_m": 5, "warning": true}),
            serde_json::json!({"instruction": "Semaforo a frente. Aguarde se vermelho.", "distance_m": 30}),
            serde_json::json!({"instruction": "Atravesse a faixa. 15 passos.", "distance_m": 15}),
            serde_json::json!({"instruction": "Vire a direita na rua Paulista.", "distance_m": 10}),
            serde_json::json!({"instruction": format!("Destino: {}. A esquerda, porta azul.", destination), "distance_m": 50, "arrival": true}),
        ]
    }

    pub fn next_instruction(&mut self) -> String {
        if self.current_step >= self.steps.len() {
            return "Voce chegou ao destino.".to_string();
        }
        let step = &self.steps[self.current_step];
        let instruction = step.get("instruction").and_then(|v| v.as_str()).unwrap_or("").to_string();
        self.last_instruction = instruction.clone();
        self.current_step += 1;
        instruction
    }

    pub fn detect_obstacle_ahead(&self) -> Option<String> {
        let obstacles = [
            "Poste a frente, 3 metros. Desvie a direita.",
            "Buraco na calcada, 2 metros. Cuidado ao pisar.",
            "Carro mal estacionado bloqueando calcada. Desvie pela rua com cuidado.",
            "Pessoa parada a frente, 1 metro. 'Com licenca.'",
            "Degrau descendo, 1 metro. Passo menor.",
            "Raiz de arvore na calcada. Atencao ao pe esquerdo.",
        ];
        if self.current_step < obstacles.len() {
            Some(obstacles[self.current_step].to_string())
        } else {
            None
        }
    }

    pub fn arrival_message(&self) -> String {
        format!("Voce chegou em {}. Esta a sua frente. Parabens!", self.destination)
    }
}

// ============================================================================
// 8. SISTEMA PRINCIPAL -- BodyCamera Controller
// ============================================================================

pub struct BodyCameraController {
    pub mount: MountPosition,
    pub verbosity: VerbosityLevel,
    pub vision: VisionEngine,
    pub audio: AudioOutputManager,
    pub navigator: StreetNavigator,
    pub mode: CameraMode,
    pub active: bool,
    pub session_start: f64,
    pub total_descriptions: u32,
    pub total_alerts: u32,
    pub battery_pct: f64,
    pub battery_drain_per_hour: f64,
    pub emergency_contact: String,
}

impl BodyCameraController {
    pub fn new(mount: MountPosition, verbosity: VerbosityLevel) -> Self {
        BodyCameraController {
            mount,
            verbosity,
            vision: VisionEngine::new(mount),
            audio: AudioOutputManager::new(),
            navigator: StreetNavigator::new(),
            mode: CameraMode::Continuous,
            active: false,
            session_start: 0.0,
            total_descriptions: 0,
            total_alerts: 0,
            battery_pct: 100.0,
            battery_drain_per_hour: 18.0,
            emergency_contact: String::new(),
        }
    }

    pub fn start(&mut self) -> serde_json::Value {
        self.active = true;
        self.session_start = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs_f64();
        self.mode = CameraMode::Continuous;
        let greeting = self.audio.speak(
            &format!("Camera corporal ativa. Montagem: {}. Modo: continuo. Fone conectado: {}. Estou vendo por voce.",
                     self.mount.value(), self.audio.device_name),
            DangerLevel::Safe,
        );
        serde_json::json!({
            "active": true,
            "mount": self.mount.value(),
            "mode": self.mode.value(),
            "audio": self.audio.status(),
            "greeting": greeting,
        })
    }

    pub fn stop(&mut self) -> serde_json::Value {
        let duration = if self.session_start > 0.0 {
            SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .unwrap()
                .as_secs_f64() - self.session_start
        } else {
            0.0
        };
        self.active = false;
        self.audio.speak("Camera desligada. Ate logo.", DangerLevel::Safe);
        serde_json::json!({
            "active": false,
            "session_duration_min": duration / 60.0,
            "total_descriptions": self.total_descriptions,
            "total_alerts": self.total_alerts,
        })
    }

    pub fn describe(&mut self) -> String {
        if !self.active {
            return "Camera desligada.".to_string();
        }
        let detections = self.vision.process_frame(self.mode);
        let description = self.vision.describe_scene(&detections, self.verbosity);
        self.audio.speak(&description, DangerLevel::Safe);
        self.total_descriptions += 1;
        description
    }

    pub fn describe_continuous(&mut self, frames: u32, interval_s: f64) -> Vec<String> {
        let mut descriptions = Vec::new();
        for _ in 0..frames {
            let desc = self.describe();
            descriptions.push(desc);
            std::thread::sleep(std::time::Duration::from_secs_f64(interval_s));
        }
        descriptions
    }

    pub fn navigate(&mut self, destination: &str) -> String {
        self.mode = CameraMode::Navigation;
        let route_msg = self.navigator.set_destination(destination, None);
        self.audio.speak(&route_msg, DangerLevel::Safe);
        let first_step = self.navigator.next_instruction();
        self.audio.speak(&first_step, DangerLevel::Attention);
        format!("{}\n{}", route_msg, first_step)
    }

    pub fn navigate_step(&mut self) -> String {
        let instruction = self.navigator.next_instruction();
        self.audio.speak(&instruction, DangerLevel::Attention);
        if let Some(obstacle) = self.navigator.detect_obstacle_ahead() {
            self.audio.speak(&obstacle, DangerLevel::Warning);
            self.total_alerts += 1;
            format!("{}\nALERTA: {}", instruction, obstacle)
        } else {
            instruction
        }
    }

    pub fn read_text(&mut self) -> String {
        self.mode = CameraMode::Reading;
        let detections = self.vision.process_frame(CameraMode::Reading);
        let texts: Vec<String> = detections.iter()
            .filter(|d| d.object_type == ObjectType::Text)
            .map(|d| d.voice_description.clone())
            .collect();
        let result = if texts.is_empty() {
            "Nao encontrei texto legivel.".to_string()
        } else {
            texts.join(" ")
        };
        self.audio.speak(&result, DangerLevel::Safe);
        self.total_descriptions += 1;
        result
    }

    pub fn identify_money(&mut self) -> String {
        self.mode = CameraMode::Money;
        let detections = self.vision.process_frame(CameraMode::Money);
        let money: Vec<String> = detections.iter()
            .filter(|d| d.object_type == ObjectType::Money)
            .map(|d| d.voice_description.clone())
            .collect();
        let result = if money.is_empty() {
            "Nao reconheci nenhuma cedula.".to_string()
        } else {
            money[0].clone()
        };
        self.audio.speak(&result, DangerLevel::Safe);
        result
    }

    pub fn identify_color(&mut self) -> String {
        self.mode = CameraMode::Color;
        let detections = self.vision.process_frame(CameraMode::Color);
        let colors: Vec<String> = detections.iter().map(|d| d.voice_description.clone()).collect();
        let result = if colors.is_empty() {
            "Nao consegui identificar a cor.".to_string()
        } else {
            colors[0].clone()
        };
        self.audio.speak(&result, DangerLevel::Safe);
        result
    }

    pub fn recognize_face(&mut self) -> String {
        self.mode = CameraMode::Face;
        let detections = self.vision.process_frame(CameraMode::Face);
        let faces: Vec<String> = detections.iter()
            .filter(|d| d.object_type == ObjectType::Person)
            .map(|d| d.voice_description.clone())
            .collect();
        let result = if faces.is_empty() {
            "Nao reconheci ninguem a frente.".to_string()
        } else {
            faces[0].clone()
        };
        self.audio.speak(&result, DangerLevel::Safe);
        result
    }

    pub fn search_object(&mut self, object_name: &str) -> String {
        self.mode = CameraMode::Search;
        let detections = self.vision.process_frame(CameraMode::Search);
        let found: Vec<String> = detections.iter().map(|d| d.voice_description.clone()).collect();
        let result = if !found.is_empty() {
            found[0].clone()
        } else {
            format!("Nao encontrei {}. Aponte a camera para outra direcao.", object_name)
        };
        self.audio.speak(&result, DangerLevel::Safe);
        result
    }

    pub fn alert_emergency(&mut self, description: &str) -> String {
        self.total_alerts += 1;
        let msg = format!("EMERGENCIA. {}. Vou avisar seu contato.", description);
        self.audio.speak(&msg, DangerLevel::Critical);
        msg
    }

    pub fn check_battery(&mut self) -> serde_json::Value {
        if self.active && self.session_start > 0.0 {
            let hours = (SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .unwrap()
                .as_secs_f64() - self.session_start) / 3600.0;
            self.battery_pct = (100.0 - (hours * self.battery_drain_per_hour)).max(0.0);
        }
        serde_json::json!({
            "phone_battery_pct": self.battery_pct,
            "headphone_battery_pct": self.audio.battery_pct,
            "estimated_remaining_h": if self.battery_drain_per_hour > 0.0 { self.battery_pct / self.battery_drain_per_hour } else { 0.0 },
            "low_battery": self.battery_pct < 20.0,
            "critical_battery": self.battery_pct < 5.0,
        })
    }

    pub fn set_mode(&mut self, mode: CameraMode) -> String {
        self.mode = mode;
        let msg = match mode {
            CameraMode::Continuous => "Continuo. Vou descrever tudo.",
            CameraMode::OnDemand => "Sob demanda. Pergunte quando quiser.",
            CameraMode::AlertOnly => "So alertas. So falo em perigo.",
            CameraMode::Navigation => "Navegacao. Vou guiar voce.",
            CameraMode::Reading => "Leitura. Aponte para o texto.",
            CameraMode::Money => "Dinheiro. Mostre a cedula.",
            CameraMode::Color => "Cor. Aponte para a cor.",
            CameraMode::Face => "Reconhecimento. Olhe para a pessoa.",
            CameraMode::Search => "Busca. O que procura?",
            CameraMode::Minimal => "Minimal. So o essencial.",
        };
        self.audio.speak(msg, DangerLevel::Safe);
        msg.to_string()
    }

    pub fn set_verbosity(&mut self, level: VerbosityLevel) -> String {
        self.verbosity = level;
        let msg = match level {
            VerbosityLevel::High => "Detalhe alto. Vou descrever tudo.",
            VerbosityLevel::Medium => "Detalhe medio. O essencial.",
            VerbosityLevel::Low => "Detalhe baixo. So alertas.",
            VerbosityLevel::Whisper => "Minimal. So perigos criticos.",
        };
        self.audio.speak(msg, DangerLevel::Safe);
        msg.to_string()
    }

    pub fn status(&mut self) -> serde_json::Value {
        serde_json::json!({
            "active": self.active,
            "mount": self.mount.value(),
            "mode": self.mode.value(),
            "verbosity": self.verbosity.value(),
            "battery": self.check_battery(),
            "audio": self.audio.status(),
            "vision_frames": self.vision.frame_count,
            "total_descriptions": self.total_descriptions,
            "total_alerts": self.total_alerts,
            "destination": self.navigator.destination,
            "nav_step": self.navigator.current_step,
        })
    }
}

// ============================================================================
// 9. CENARIOS DO MUNDO REAL
// ============================================================================

pub fn scenario_walking_to_destination() {
    println!("{}", "=".repeat(65));
    println!("CENARIO 1: Cego andando ate a padaria");
    println!("{}", "=".repeat(65));

    let mut cam = BodyCameraController::new(MountPosition::Chest, VerbosityLevel::Medium);
    let start = cam.start();
    if let Some(greeting) = start.get("greeting").and_then(|g| g.get("message")) {
        println!("\n[{}]", greeting);
    }

    println!("\n[NAVEGACAO]");
    let route = cam.navigate("Padaria do Joao");
    println!("  {}", route);

    for i in 0..4 {
        println!("\n[Passo {}]", i + 1);
        let instruction = cam.navigate_step();
        println!("  {}", instruction);
    }
}

pub fn scenario_reading_menu() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 2: Cego lendo cardapio de restaurante");
    println!("{}", "=".repeat(65));

    let mut cam = BodyCameraController::new(MountPosition::Chest, VerbosityLevel::Medium);
    cam.start();
    println!("\n[MODO LEITURA]");
    let text = cam.read_text();
    println!("  Camera leu: {}", text);
}

pub fn scenario_identifying_money() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 3: Cego reconhecendo dinheiro");
    println!("{}", "=".repeat(65));

    let mut cam = BodyCameraController::new(MountPosition::Chest, VerbosityLevel::Medium);
    cam.start();
    println!("\n[MODO DINHEIRO]");
    let money = cam.identify_money();
    println!("  Camera identificou: {}", money);
}

pub fn scenario_crossing_street() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 4: Cego atravessando a rua");
    println!("{}", "=".repeat(65));

    let mut cam = BodyCameraController::new(MountPosition::Chest, VerbosityLevel::Medium);
    cam.start();
    cam.set_mode(CameraMode::Navigation);
    println!("\n[Cena 1: Chegando no semaforo]");
    let desc = cam.describe();
    println!("  {}", desc);

    println!("\n[Cena 2: Semaforo]");
    let color = cam.identify_color();
    println!("  {}", color);

    println!("\n[Cena 3: Atravesando]");
    let desc = cam.describe();
    println!("  {}", desc);
}

pub fn scenario_meeting_person() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 5: Cego reconhecendo pessoa a frente");
    println!("{}", "=".repeat(65));

    let mut cam = BodyCameraController::new(MountPosition::Chest, VerbosityLevel::Medium);
    cam.start();
    println!("\n[MODO ROSTO]");
    let face = cam.recognize_face();
    println!("  {}", face);
}

pub fn scenario_searching_object() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 6: Cego procurando objeto perdido");
    println!("{}", "=".repeat(65));

    let mut cam = BodyCameraController::new(MountPosition::Chest, VerbosityLevel::Medium);
    cam.start();
    println!("\n[MODO BUSCA: 'minha chave']");
    let result = cam.search_object("minha chave");
    println!("  {}", result);
}

pub fn scenario_battery_management() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 7: Bateria em caminhada longa");
    println!("{}", "=".repeat(65));

    let mut cam = BodyCameraController::new(MountPosition::Chest, VerbosityLevel::Medium);
    cam.start();
    println!("\n[Inicio da caminhada]");
    let battery = cam.check_battery();
    println!("  Celular: {:.0}%", battery["phone_battery_pct"]);
    println!("  Fone: {:.0}%", battery["headphone_battery_pct"]);
    println!("  Autonomia estimada: {:.1}h", battery["estimated_remaining_h"]);

    cam.session_start = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs_f64() - 3.0 * 3600.0;
    println!("\n[Apos 3 horas de uso]");
    let battery = cam.check_battery();
    println!("  Celular: {:.0}%", battery["phone_battery_pct"]);
    println!("  Fone: {:.0}%", battery["headphone_battery_pct"]);
    println!("  Restante: {:.1}h", battery["estimated_remaining_h"]);

    if battery["low_battery"].as_bool().unwrap_or(false) {
        println!("  AVISO: Bateria baixa. Modo survival.");
    }
}

pub fn scenario_continuous_description() {
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 8: Descricao continua andando na rua");
    println!("{}", "=".repeat(65));

    let mut cam = BodyCameraController::new(MountPosition::Chest, VerbosityLevel::Medium);
    cam.start();
    println!("\n[Descricao continua - 5 frames]");
    for i in 0..5 {
        let desc = cam.describe();
        println!("  Frame {}: {}", i + 1, desc);
        std::thread::sleep(std::time::Duration::from_millis(100));
    }
}

// ============================================================================
// 10. DEMONSTRACAO (main)
// ============================================================================

fn main() {
    println!("{}", "=".repeat(70));
    println!("OpenBodyCamera -- Smartphone Corporal + Fone BT = Olhos do Cego");
    println!("{}", "=".repeat(70));

    println!("\nMontagens: 7");
    for m in [
        MountPosition::Chest,
        MountPosition::Head,
        MountPosition::Shoulder,
        MountPosition::Neck,
        MountPosition::Hand,
        MountPosition::PocketFacingOut,
        MountPosition::Armband,
    ] {
        println!("  {}", m.value());
    }

    println!("\nModos de camera: 10");
    for m in [
        CameraMode::Continuous,
        CameraMode::OnDemand,
        CameraMode::AlertOnly,
        CameraMode::Navigation,
        CameraMode::Reading,
        CameraMode::Money,
        CameraMode::Color,
        CameraMode::Face,
        CameraMode::Search,
        CameraMode::Minimal,
    ] {
        println!("  {}", m.value());
    }

    println!("\nVerbosidade: 4");
    for v in [VerbosityLevel::High, VerbosityLevel::Medium, VerbosityLevel::Low, VerbosityLevel::Whisper] {
        println!("  {}", v.value());
    }

    println!("\nTipos de objeto: 17");
    println!("Niveis de perigo: 5");

    // Cenarios
    scenario_walking_to_destination();
    scenario_reading_menu();
    scenario_identifying_money();
    scenario_crossing_street();
    scenario_meeting_person();
    scenario_searching_object();
    scenario_continuous_description();
    scenario_battery_management();

    // Status final
    let mut cam = BodyCameraController::new(MountPosition::Chest, VerbosityLevel::Medium);
    cam.start();
    cam.describe();
    cam.navigate("teste");
    let status = cam.status();
    println!("\n{}", "=".repeat(70));
    println!("STATUS DO SISTEMA");
    println!("{}", "=".repeat(70));
    println!("  Ativo: {}", status["active"]);
    println!("  Montagem: {}", status["mount"]);
    println!("  Modo: {}", status["mode"]);
    println!("  Verbosidade: {}", status["verbosity"]);
    println!("  Frames processados: {}", status["vision_frames"]);
    println!("  Descricoes geradas: {}", status["total_descriptions"]);
    println!("  Alertas emitidos: {}", status["total_alerts"]);
    println!("  Audio: {}", status["audio"]["connected"]);

    cam.stop();

    println!("\n{}", "=".repeat(70));
    println!("RESUMO");
    println!("{}", "=".repeat(70));
    println!();
    println!("  O smartphone vira OLHOS.");
    println!("  O fone bluetooth vira VOZ que descreve.");
    println!("  O cego ANDA na rua com INFORMACAO.");
    println!("  NADA o para. NINGUEM o limita.");
    println!();
    println!("  Camera no peito. Fone no ouvido. Mundo na mente.");
    println!("  O cego VE.");
    println!();
    println!("  Integrado com:");
    println!("    OpenTelefonista (conversa natural)");
    println!("    OpenInclusiveHardware (44 dispositivos)");
    println!("    OpenResilience (bateria/falhas)");
    println!("    OpenHumanNet (emergencia)");
}