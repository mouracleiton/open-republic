// OpenHumanNet -- Chamar o Humano Autorizado Mais Proximo
// =========================================================
// "Quando tudo falha, a tecnologia so faz uma coisa util:
// CHAMAR UM HUMANO. Nao qualquer humano. O humano CERTO.
// O mais proximo. O autorizado. O que PODE ajudar.
//
// O cego esta perdido, bateria em 1%, GPS morto, TTS crashou.
// O sistema nao tenta se consertar. O sistema GRITE por ajuda.
// Mas nao um grito aleatorio -- uma chamada CIRURGICA:
//
// 'Ola, Andre? Aqui e a Iara, sistema da Republica.
// Cleiton esta na rua Augusta perto da numero 1500.
// Bateria em 1%. Ele e cego e pode precisar de ajuda.
// Voce e o humano autorizado mais proximo (400m).
// Pode ir ate la?'
//
// Se Andre nao atende em 30s, chama o proximo.
// E o proximo. E o proximo. Ate alguem responder.
//
// ESTRUTURA EM ANEIS (concentricos):
// Anel 0: Familia direta (esposa, pai, mae, irmao)
// Anel 1: Cuidador autorizado / vizinho de confianca
// Anel 2: Comunidade Republica (membros proximos)
// Anel 3: Profissionais (medico, enfermeiro, assistente social)
// Anel 4: Emergencia publica (190, 192, 193)
// Anel 5: Qualquer humano proximo (pedir ajuda a estranho)
//
// O sistema so para de chamar quando:
// 1. Um humano CONFIRMA que vai ajudar, OU
// 2. A situacao se resolve (usuario responde que esta bem), OU
// 3. Todos os aneis foram esgotados -> emergencia publica
//
// PRINCIPIO: A tecnologia NAO substitui o humano.
// A tecnologia CONECTA o humano certo no momento certo.
//
// Integrado com:
// - OpenResilience (dispara em SURVIVAL/EMERGENCY)
// - OpenTelefonista (faz a ligacao naturalmente)
// - OpenBodilyAutonomy (so chama se usuario autorizou ou esta incapacitado)
// - OpenAbsence (respeita se usuario pode se comunicar)
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// ============================================================================

use std::collections::{HashMap, VecDeque};
use std::time::{SystemTime, UNIX_EPOCH};
use rand::Rng;

// ============================================================================
// 1. ANEIS DE CONFIANCA (Concentric Trust Rings)
// ============================================================================

/// Aneis concentricos de confianca para chamada de ajuda.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, PartialOrd, Ord)]
pub enum TrustRing {
    Family = 0,      // familia direta
    Caregiver = 1,   // cuidador / vizinho de confianca
    Community = 2,   // membros da Republica proximos
    Professional = 3, // medico, enfermeiro, assistente social
    Emergency = 4,   // 190, 192, 193
    Bystander = 5,   // qualquer humano proximo (estranho)
}

/// Nivel de autorizacao do humano para receber alertas.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum AuthorizationLevel {
    Full,          // pode tomar decisoes por o usuario
    High,          // pode ajudar fisicamente, nao decidir
    Medium,        // pode verificar status e reportar
    Low,           // so recebe notificacao
    EmergencyOnly, // so chamado em emergencia real
}

/// Disponibilidade do humano no momento.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum HumanAvailability {
    Available,   // respondeu, pode ir
    Maybe,       // respondeu, verificando
    Busy,        // respondeu, nao pode
    Unreachable, // nao atendeu
    Offline,     // sem sinal / telefone desligado
    Unknown,     // ainda nao tentou
}

/// Como contatar o humano.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum ContactMethod {
    PhoneCall,     // ligacao telefonica
    Sms,           // mensagem de texto
    Whatsapp,      // mensagem de WhatsApp
    VideoCall,     // video chamada
    AppPush,       // push notification do app
    Smartwatch,    // vibracao no relogio
    HomeAssistant, // Alexa/Google Home
    PhysicalVisit, // alguem vai ate la pessoalmente
}

// ============================================================================
// 2. HUMANO AUTORIZADO
// ============================================================================

#[derive(Debug, Clone)]
pub struct AuthorizedHuman {
    pub human_id: String,
    pub name: String,
    pub phone: String,
    pub ring: TrustRing,
    pub authorization: AuthorizationLevel,
    pub relationship: String,           // "esposa", "pai", "vizinho", "medico"
    pub home_location: Option<(f64, f64)>, // (lat, lon)
    pub current_location: Option<(f64, f64)>,
    pub last_location_update: f64,
    pub preferred_contact: ContactMethod,
    pub languages: Vec<String>,
    pub skills: Vec<String>,            // "primeiros_socorros", "libras", etc
    pub available_hours: (String, String), // ("00:00", "23:59")
    pub response_timeout_s: u32,
    pub max_distance_km: f64,
    pub can_make_decisions: bool,
    pub medical_authorization: bool,
    pub photo_url: String,
    pub notes: String,
}

impl AuthorizedHuman {
    pub fn new(
        human_id: &str,
        name: &str,
        phone: &str,
        ring: TrustRing,
        authorization: AuthorizationLevel,
        relationship: &str,
        home_location: Option<(f64, f64)>,
    ) -> Self {
        Self {
            human_id: human_id.to_string(),
            name: name.to_string(),
            phone: phone.to_string(),
            ring,
            authorization,
            relationship: relationship.to_string(),
            home_location,
            current_location: None,
            last_location_update: 0.0,
            preferred_contact: ContactMethod::PhoneCall,
            languages: vec!["pt-BR".to_string()],
            skills: vec![],
            available_hours: ("00:00".to_string(), "23:59".to_string()),
            response_timeout_s: 30,
            max_distance_km: 50.0,
            can_make_decisions: false,
            medical_authorization: false,
            photo_url: String::new(),
            notes: String::new(),
        }
    }

    /// Distancia em km ate um ponto (haversine simplificado).
    pub fn distance_to(&self, lat: f64, lon: f64) -> f64 {
        let loc = self.current_location.or(self.home_location);
        match loc {
            Some((hlat, hlon)) => _haversine_km(hlat, hlon, lat, lon),
            None => 9999.0,
        }
    }

    /// Verifica se esta dentro do horario de disponibilidade.
    pub fn is_available_now(&self) -> bool {
        // Simplificado: sempre disponivel para demo
        true
    }
}

fn _haversine_km(lat1: f64, lon1: f64, lat2: f64, lon2: f64) -> f64 {
    /// Distancia em km entre dois pontos GPS.
    let r = 6371.0;
    let dlat = (lat2 - lat1).to_radians();
    let dlon = (lon2 - lon1).to_radians();
    let a = (dlat / 2.0).sin().powi(2)
        + lat1.to_radians().cos() * lat2.to_radians().cos() * (dlon / 2.0).sin().powi(2);
    let c = 2.0 * a.sqrt().atan2((1.0 - a).sqrt());
    r * c
}

// ============================================================================
// 3. EVENTO DE CHAMADA
// ============================================================================

/// Estados de chamada.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum CallStatus {
    Pending,   // ainda nao chamou
    Ringing,   // chamando
    Answered,  // humano atendeu
    Confirmed, // humano confirmou que vai ajudar
    Declined,  // humano nao pode
    Timeout,   // nao atendeu no tempo
    Failed,    // erro tecnico
    Cancelled, // situacao resolvida, cancelar
}

#[derive(Debug, Clone)]
pub struct CallAttempt {
    pub attempt_id: String,
    pub human: AuthorizedHuman,
    pub method: ContactMethod,
    pub status: CallStatus,
    pub called_at: f64,
    pub answered_at: Option<f64>,
    pub timeout_at: Option<f64>,
    pub message_sent: String,
    pub response_received: String,
    pub distance_km: f64,
    pub eta_minutes: f64,
}

impl CallAttempt {
    pub fn new(human: AuthorizedHuman, method: ContactMethod, distance_km: f64) -> Self {
        let now = current_time();
        Self {
            attempt_id: format!("CALL-{}-{}", human.human_id, now as u64),
            human,
            method,
            status: CallStatus::Pending,
            called_at: now,
            answered_at: None,
            timeout_at: None,
            message_sent: String::new(),
            response_received: String::new(),
            distance_km,
            eta_minutes: (distance_km * 3.0).max(1.0),
        }
    }
}

fn current_time() -> f64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs_f64()
}

// ============================================================================
// 4. MOTOR DE CHAMADA DE HUMANOS
// ============================================================================

#[derive(Debug)]
pub struct HumanNet {
    pub user_name: String,
    pub user_phone: String,
    pub registry: HashMap<String, AuthorizedHuman>,
    pub call_history: VecDeque<CallAttempt>,
    pub active_calls: HashMap<String, CallAttempt>,
    pub confirmed_helper: Option<AuthorizedHuman>,
    pub current_ring: Option<TrustRing>,
    pub user_location: Option<(f64, f64)>,
    pub user_disabilities: Vec<String>,
    pub situation_description: String,
    pub auto_call_enabled: bool,
    pub consent_given: bool,
}

impl HumanNet {
    pub fn new(user_name: &str, user_phone: &str) -> Self {
        Self {
            user_name: user_name.to_string(),
            user_phone: user_phone.to_string(),
            registry: HashMap::new(),
            call_history: VecDeque::with_capacity(500),
            active_calls: HashMap::new(),
            confirmed_helper: None,
            current_ring: None,
            user_location: None,
            user_disabilities: vec![],
            situation_description: String::new(),
            auto_call_enabled: true,
            consent_given: true,
        }
    }

    // -- Registro de humanos --

    pub fn register_human(&mut self, human: AuthorizedHuman) -> String {
        /// Registra um humano autorizado.
        let msg = format!(
            "{} registrado no anel {:?} ({}).",
            human.name, human.ring, human.authorization as u8
        );
        self.registry.insert(human.human_id.clone(), human);
        msg
    }

    pub fn remove_human(&mut self, human_id: &str) -> String {
        /// Remove um humano do registro.
        if let Some(h) = self.registry.remove(human_id) {
            format!("{} removido.", h.name)
        } else {
            "Humano nao encontrado.".to_string()
        }
    }

    pub fn list_humans(&self) -> HashMap<TrustRing, Vec<AuthorizedHuman>> {
        /// Lista humanos por anel.
        let mut by_ring: HashMap<TrustRing, Vec<AuthorizedHuman>> = HashMap::new();
        for h in self.registry.values() {
            by_ring.entry(h.ring).or_default().push(h.clone());
        }
        by_ring
    }

    // -- Atualizacao de localizacao --

    pub fn update_user_location(&mut self, lat: f64, lon: f64) {
        /// Atualiza localizacao do usuario.
        self.user_location = Some((lat, lon));
    }

    pub fn update_human_location(&mut self, human_id: &str, lat: f64, lon: f64) {
        /// Atualiza localizacao de um humano (via app/GPS).
        if let Some(h) = self.registry.get_mut(human_id) {
            h.current_location = Some((lat, lon));
            h.last_location_update = current_time();
        }
    }

    // -- Ranqueamento --

    pub fn rank_humans(
        &self,
        max_ring: TrustRing,
        required_auth: AuthorizationLevel,
    ) -> Vec<(AuthorizedHuman, f64)> {
        /// Ranqueia humanos por prioridade de chamada.
        if self.user_location.is_none() {
            return vec![];
        }
        let (ulat, ulon) = self.user_location.unwrap();

        let mut ranked: Vec<(AuthorizedHuman, f64)> = vec![];
        let auth_order = [
            AuthorizationLevel::Full,
            AuthorizationLevel::High,
            AuthorizationLevel::Medium,
            AuthorizationLevel::Low,
            AuthorizationLevel::EmergencyOnly,
        ];

        for human in self.registry.values() {
            if human.ring as u8 > max_ring as u8 {
                continue;
            }
            let auth_idx = auth_order.iter().position(|&a| a == human.authorization).unwrap();
            let req_idx = auth_order.iter().position(|&a| a == required_auth).unwrap();
            if auth_idx > req_idx {
                continue;
            }
            if human.ring != TrustRing::Emergency && !human.is_available_now() {
                continue;
            }
            let dist = human.distance_to(ulat, ulon);
            if dist > human.max_distance_km && human.ring != TrustRing::Emergency {
                continue;
            }
            ranked.push((human.clone(), dist));
        }

        ranked.sort_by(|a, b| {
            let ring_cmp = (a.0.ring as u8).cmp(&(b.0.ring as u8));
            if ring_cmp != std::cmp::Ordering::Equal {
                ring_cmp
            } else {
                a.1.partial_cmp(&b.1).unwrap()
            }
        });
        ranked
    }

    // -- Chamada --

    pub fn trigger_emergency_call(
        &mut self,
        situation: &str,
        user_lat: f64,
        user_lon: f64,
        severity: &str,
    ) -> serde_json::Value {
        /// Dispara cadeia de chamadas para humanos autorizados.
        if user_lat != 0.0 && user_lon != 0.0 {
            self.update_user_location(user_lat, user_lon);
        }
        self.situation_description = situation.to_string();
        self.confirmed_helper = None;
        self.active_calls.clear();

        if self.user_location.is_none() {
            return serde_json::json!({
                "success": false,
                "error": "Sem localizacao do usuario. Nao posso chamar ajuda.",
                "fallback": "Ligar para 190 diretamente."
            });
        }

        let max_ring = match severity {
            "catastrophic" => TrustRing::Emergency,
            "critical" => TrustRing::Professional,
            _ => TrustRing::Community,
        };
        let required_auth = if severity == "critical" || severity == "catastrophic" {
            AuthorizationLevel::Medium
        } else {
            AuthorizationLevel::Low
        };

        let ranked = self.rank_humans(max_ring, required_auth);
        if ranked.is_empty() {
            return self._call_emergency_services(situation);
        }

        let mut results: Vec<CallAttempt> = vec![];
        for (human, distance) in ranked {
            self.current_ring = Some(human.ring);
            let attempt = self._call_human(human, situation, distance);
            let confirmed = attempt.status == CallStatus::Confirmed;
            results.push(attempt.clone());

            if confirmed {
                self.confirmed_helper = Some(attempt.human.clone());
                return serde_json::json!({
                    "success": true,
                    "helper": attempt.human.name,
                    "phone": attempt.human.phone,
                    "ring": format!("{:?}", attempt.human.ring),
                    "distance_km": (distance * 100.0).round() / 100.0,
                    "eta_minutes": attempt.eta_minutes,
                    "method": format!("{:?}", attempt.method),
                    "message": format!("{} confirmou! Esta a {:.1}km. Chega em ~{} minutos.", attempt.human.name, distance, attempt.eta_minutes as u32),
                    "all_attempts": results.iter().map(|a| self._attempt_summary(a)).collect::<Vec<_>>()
                });
            }
        }

        let emergency_result = self._call_emergency_services(situation);
        serde_json::json!({
            "success": false,
            "error": format!("Nenhum dos {} humanos disponiveis confirmou.", results.len()),
            "all_attempts": results.iter().map(|a| self._attempt_summary(a)).collect::<Vec<_>>(),
            "escalated_to_emergency": true,
            "emergency_result": emergency_result
        })
    }

    fn _call_human(&mut self, human: AuthorizedHuman, situation: &str, distance: f64) -> CallAttempt {
        /// Tenta chamar um humano especifico (simulado).
        let mut attempt = CallAttempt::new(human.clone(), human.preferred_contact, distance);
        attempt.message_sent = self._build_message(&human, situation, distance);
        attempt.status = CallStatus::Ringing;
        self.active_calls.insert(attempt.attempt_id.clone(), attempt.clone());

        let response_chance: f64 = match human.ring {
            TrustRing::Family => 0.85,
            TrustRing::Caregiver => 0.70,
            TrustRing::Community => 0.50,
            TrustRing::Professional => 0.60,
            TrustRing::Emergency => 0.90,
            TrustRing::Bystander => 0.30,
        };

        let mut rng = rand::thread_rng();
        if rng.gen::<f64>() < response_chance {
            attempt.status = CallStatus::Confirmed;
            attempt.answered_at = Some(current_time());
            attempt.response_received = format!("{} confirmou que esta indo.", human.name);
        } else {
            attempt.status = CallStatus::Timeout;
            attempt.timeout_at = Some(current_time());
            attempt.response_received = format!("Sem resposta de {} em {}s.", human.name, human.response_timeout_s);
        }

        self.call_history.push_back(attempt.clone());
        if self.call_history.len() > 500 {
            self.call_history.pop_front();
        }
        attempt
    }

    fn _build_message(&self, human: &AuthorizedHuman, situation: &str, distance: f64) -> String {
        /// Constroi a mensagem natural para o humano.
        let disabilities_text = if !self.user_disabilities.is_empty() {
            format!(" Condicao: {}.", self.user_disabilities.join(", "))
        } else {
            String::new()
        };
        let (lat, lon) = self.user_location.unwrap_or((0.0, 0.0));
        format!(
            "Ola, {}? Aqui e a Iara, sistema da Republica. {} precisa de ajuda. Situacao: {}. Localizacao aproximada: {:.4}, {:.4}. Voce esta a {:.1}km.{}{} Pode ir ate la ou ligar para confirmar que esta bem?",
            human.name, self.user_name, situation, lat, lon, distance, disabilities_text,
            if disabilities_text.is_empty() { "" } else { " " }
        )
    }

    fn _call_emergency_services(&self, situation: &str) -> serde_json::Value {
        /// Chama servico de emergencia publica (190/192/193).
        let (service, service_type) = if situation.to_lowercase().contains("medica")
            || situation.to_lowercase().contains("coracao")
            || situation.to_lowercase().contains("machucad")
        {
            ("192 (SAMU)", "medica")
        } else if situation.to_lowercase().contains("incendio")
            || situation.to_lowercase().contains("fogo")
        {
            ("193 (Bombeiros)", "bombeiros")
        } else {
            ("190 (Policia)", "policia")
        };

        let msg = format!(
            "LIGACAO AUTOMATICA para {}. Usuario: {}. Localizacao: {:?}. Situacao: {}. Condicoes: {}. Nenhum contato pessoal respondeu.",
            service,
            self.user_name,
            self.user_location,
            situation,
            if self.user_disabilities.is_empty() { "nenhuma" } else { &self.user_disabilities.join(", ") }
        );

        serde_json::json!({
            "success": true,
            "service": service,
            "type": service_type,
            "message": msg,
            "note": "Emergencia publica acionada. Ajuda a caminho."
        })
    }

    pub fn cancel_emergency(&mut self, reason: &str) -> serde_json::Value {
        /// Cancela cadeia de emergencia (usuario recuperou, falso alarme).
        for attempt in self.active_calls.values_mut() {
            if matches!(attempt.status, CallStatus::Ringing | CallStatus::Pending) {
                attempt.status = CallStatus::Cancelled;
            }
        }
        self.confirmed_helper = None;
        serde_json::json!({
            "cancelled": true,
            "reason": reason,
            "message": format!("Emergencia cancelada. {}. Todos os contatos foram avisados.", reason)
        })
    }

    fn _attempt_summary(&self, attempt: &CallAttempt) -> serde_json::Value {
        serde_json::json!({
            "human": attempt.human.name,
            "ring": format!("{:?}", attempt.human.ring),
            "phone": attempt.human.phone,
            "method": format!("{:?}", attempt.method),
            "status": format!("{:?}", attempt.status),
            "distance_km": (attempt.distance_km * 100.0).round() / 100.0,
            "eta_minutes": (attempt.eta_minutes * 10.0).round() / 10.0,
            "response": attempt.response_received
        })
    }

    pub fn status(&self) -> serde_json::Value {
        /// Status atual da rede de humanos.
        let by_ring = self.list_humans();
        let mut humans_by_ring = serde_json::Map::new();
        for (r, v) in by_ring {
            humans_by_ring.insert(format!("{:?}", r), serde_json::json!(v.len()));
        }
        serde_json::json!({
            "user_name": self.user_name,
            "total_humans": self.registry.len(),
            "humans_by_ring": humans_by_ring,
            "confirmed_helper": self.confirmed_helper.as_ref().map(|h| h.name.clone()),
            "current_ring": self.current_ring.map(|r| format!("{:?}", r)),
            "active_calls": self.active_calls.len(),
            "total_calls_made": self.call_history.len(),
            "auto_call_enabled": self.auto_call_enabled,
            "user_location": self.user_location
        })
    }
}

// ============================================================================
// 5. PERFIS PRE-CONFIGURADOS
// ============================================================================

pub fn create_default_network(user_name: &str) -> HumanNet {
    /// Cria rede padrao do Cleiton com seus contatos.
    let mut net = HumanNet::new(user_name, "+5511****9999");
    net.user_disabilities = vec![];

    // Anel 0: Familia
    let mut ming = AuthorizedHuman::new(
        "ming", "MING", "+5511****8888",
        TrustRing::Family, AuthorizationLevel::Full, "esposa",
        Some((-23.5505, -46.6333)),
    );
    ming.preferred_contact = ContactMethod::PhoneCall;
    ming.skills = vec!["primeiros_socorros".to_string()];
    ming.can_make_decisions = true;
    ming.medical_authorization = true;
    ming.response_timeout_s = 20;
    ming.max_distance_km = 30.0;
    net.register_human(ming);

    let mut mae = AuthorizedHuman::new(
        "mae", "Mae", "+5511****7777",
        TrustRing::Family, AuthorizationLevel::Full, "mae",
        Some((-23.5600, -46.6400)),
    );
    mae.preferred_contact = ContactMethod::PhoneCall;
    mae.can_make_decisions = true;
    mae.medical_authorization = true;
    mae.response_timeout_s = 30;
    mae.max_distance_km = 50.0;
    net.register_human(mae);

    // Anel 1: Cuidador
    let mut andre = AuthorizedHuman::new(
        "andre", "Andre Castro", "+5511****6666",
        TrustRing::Caregiver, AuthorizationLevel::High, "parceiro",
        Some((-23.5450, -46.6300)),
    );
    andre.preferred_contact = ContactMethod::Whatsapp;
    andre.skills = vec!["gestao".to_string(), "primeiros_socorros".to_string()];
    andre.response_timeout_s = 45;
    andre.max_distance_km = 20.0;
    net.register_human(andre);

    // Anel 2: Comunidade
    let mut aveone = AuthorizedHuman::new(
        "aveone", "AveOne", "+5511****5555",
        TrustRing::Community, AuthorizationLevel::Medium, "equipe infra",
        Some((-23.5700, -46.6500)),
    );
    aveone.preferred_contact = ContactMethod::Sms;
    aveone.skills = vec!["tecnologia".to_string(), "infraestrutura".to_string()];
    aveone.response_timeout_s = 60;
    aveone.max_distance_km = 15.0;
    net.register_human(aveone);

    // Anel 3: Profissional
    let mut dr = AuthorizedHuman::new(
        "dr_silva", "Dr. Silva", "+5511****4444",
        TrustRing::Professional, AuthorizationLevel::High, "medico de familia",
        Some((-23.5400, -46.6200)),
    );
    dr.preferred_contact = ContactMethod::PhoneCall;
    dr.skills = vec!["medico".to_string(), "primeiros_socorros".to_string(), "cardiologia".to_string()];
    dr.medical_authorization = true;
    dr.available_hours = ("07:00".to_string(), "19:00".to_string());
    dr.response_timeout_s = 60;
    dr.max_distance_km = 10.0;
    net.register_human(dr);

    net
}

// ============================================================================
// 6. INTEGRACAO COM OPENRESILIENCE
// ============================================================================

pub struct ResilienceHumanBridge {
    pub net: HumanNet,
    pub triggered: bool,
    pub last_trigger_level: String,
}

impl ResilienceHumanBridge {
    pub fn new(human_net: HumanNet) -> Self {
        Self {
            net: human_net,
            triggered: false,
            last_trigger_level: String::new(),
        }
    }

    pub fn check_and_trigger(
        &mut self,
        degradation_level: &str,
        user_lat: f64,
        user_lon: f64,
        situation: &str,
    ) -> Option<serde_json::Value> {
        /// Verifica nivel de degradacao e chama humanos se necessario.
        let severity = match degradation_level {
            "sobrevivencia" => Some("critical"),
            "emergencia" | "morto" => Some("catastrophic"),
            _ => None,
        };

        if severity.is_none() {
            if self.triggered {
                let result = self.net.cancel_emergency("Sistema recuperado.");
                self.triggered = false;
                self.last_trigger_level.clear();
                return Some(result);
            }
            return None;
        }

        if self.triggered && self.last_trigger_level == degradation_level {
            return None;
        }

        self.triggered = true;
        self.last_trigger_level = degradation_level.to_string();

        let sit = if situation.is_empty() {
            format!("Sistema em nivel {}. Possivel falha multipla.", degradation_level)
        } else {
            situation.to_string()
        };

        Some(self.net.trigger_emergency_call(&sit, user_lat, user_lon, severity.unwrap()))
    }
}

// ============================================================================
// 7. CENARIOS DO MUNDO REAL
// ============================================================================

pub fn scenario_blind_lost_battery() {
    /// Cenario: cego perdido, bateria morrendo.
    println!("{}", "=".repeat(65));
    println!("CENARIO 1: Cego perdido -- bateria em 1%");
    println!("{}", "=".repeat(65));

    let mut net = create_default_network("Cleiton");
    net.user_disabilities = vec!["cegueira_total".to_string()];
    net.update_user_location(-23.5510, -46.6340);

    let result = net.trigger_emergency_call(
        "Cego na rua, bateria do smartphone em 1%. Pode perder contato.",
        -23.5510,
        -46.6340,
        "critical",
    );

    println!("\nResultado: {}", if result["success"].as_bool().unwrap_or(false) { "SUCESSO" } else { "FALHOU" });
    if result["success"].as_bool().unwrap_or(false) {
        println!("Ajudante: {} (anel {})", result["helper"], result["ring"]);
        println!("Distancia: {}km | ETA: {}min", result["distance_km"], result["eta_minutes"]);
        println!("Metodo: {}", result["method"]);
    } else {
        println!("Erro: {}", result.get("error").unwrap_or(&serde_json::json!("desconhecido")));
        if result.get("escalated_to_emergency").is_some() {
            println!("Escalacao: {}", result["emergency_result"]["service"]);
        }
    }

    println!("\nTentativas:");
    if let Some(attempts) = result.get("all_attempts").and_then(|a| a.as_array()) {
        for a in attempts {
            let status_icon = if a["status"] == "Confirmed" { "OK" } else { "X " };
            println!("  [{}] {:15} anel={:12} dist={}km status={}", status_icon, a["human"], a["ring"], a["distance_km"], a["status"]);
        }
    }
}

pub fn scenario_elderly_fall() {
    /// Cenario: idosa caiu, sem resposta.
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 2: Idosa caiu -- sem resposta em 30s");
    println!("{}", "=".repeat(65));

    let mut net = HumanNet::new("Dona Cecca", "+5511****3333");
    net.user_disabilities = vec!["idoso".to_string(), "osteoporose".to_string()];
    net.update_user_location(-23.5520, -46.6350);

    let mut filha = AuthorizedHuman::new(
        "filha", "Maria Filha", "+5511****1111",
        TrustRing::Family, AuthorizationLevel::Full, "filha",
        Some((-23.5480, -46.6310)),
    );
    filha.skills = vec!["primeiros_socorros".to_string()];
    filha.can_make_decisions = true;
    filha.medical_authorization = true;
    filha.response_timeout_s = 20;
    net.register_human(filha);

    let mut vizinha = AuthorizedHuman::new(
        "vizinha", "Dona Ana", "+5511****2222",
        TrustRing::Caregiver, AuthorizationLevel::High, "vizinha",
        Some((-23.5515, -46.6345)),
    );
    vizinha.skills = vec!["primeiros_socorros".to_string()];
    vizinha.response_timeout_s = 30;
    vizinha.max_distance_km = 2.0;
    net.register_human(vizinha);

    let result = net.trigger_emergency_call(
        "Idosa caiu. Deteccao de queda pelo smartwatch. Sem resposta ha 30s.",
        -23.5520,
        -46.6350,
        "catastrophic",
    );

    println!("\nResultado: {}", if result["success"].as_bool().unwrap_or(false) { "SUCESSO" } else { "FALHOU" });
    if result["success"].as_bool().unwrap_or(false) {
        println!("Quem vai: {} ({})", result["helper"], result["ring"]);
        println!("Distancia: {}km | ETA: {}min", result["distance_km"], result["eta_minutes"]);
    } else {
        println!("Escalacao: {}", result.get("escalated_to_emergency").unwrap_or(&serde_json::json!(false)));
    }

    println!("\nTentativas:");
    if let Some(attempts) = result.get("all_attempts").and_then(|a| a.as_array()) {
        for a in attempts {
            let status_icon = if a["status"] == "Confirmed" { "OK" } else { "X " };
            println!("  [{}] {:15} anel={:12} dist={}km", status_icon, a["human"], a["ring"], a["distance_km"]);
        }
    }
}

pub fn scenario_seizure() {
    /// Cenario: crise epileptica -- preciso de humano rapido.
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 3: Crise epileptica iminente");
    println!("{}", "=".repeat(65));

    let mut net = create_default_network("Pedro");
    net.user_disabilities = vec!["epilepsia".to_string()];
    net.update_user_location(-23.5530, -46.6360);

    let result = net.trigger_emergency_call(
        "Sinais pre-crise epileptica. Smartwatch detectou anomalia cardiaca + temperatura elevada.",
        0.0,
        0.0,
        "critical",
    );

    println!("\nResultado: {}", if result["success"].as_bool().unwrap_or(false) { "SUCESSO" } else { "FALHOU" });
    if result["success"].as_bool().unwrap_or(false) {
        println!("Ajudante: {} (anel {})", result["helper"], result["ring"]);
        println!("Distancia: {}km | ETA: {}min", result["distance_km"], result["eta_minutes"]);
    }
    println!("\nTentativas:");
    if let Some(attempts) = result.get("all_attempts").and_then(|a| a.as_array()) {
        for a in attempts {
            let status_icon = if a["status"] == "Confirmed" { "OK" } else { "X " };
            println!("  [{}] {:15} dist={}km status={}", status_icon, a["human"], a["distance_km"], a["status"]);
        }
    }
}

pub fn scenario_resilience_integration() {
    /// Cenario: OpenResilience detecta EMERGENCY -> HumanNet chama humano.
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 4: Integracao Resilience -> HumanNet");
    println!("{}", "=".repeat(65));

    let mut net = create_default_network("Cleiton");
    net.update_user_location(-23.5510, -46.6340);
    let mut bridge = ResilienceHumanBridge::new(net);

    println!("\n[Nivel: completo]");
    let r = bridge.check_and_trigger("completo", -23.5510, -46.6340, "");
    println!("  Resultado: {}", if r.is_none() { "Sem acao" } else { "disparou" });

    println!("\n[Nivel: degradado_1]");
    let r = bridge.check_and_trigger("degradado_1", -23.5510, -46.6340, "");
    println!("  Resultado: {}", if r.is_none() { "Sem acao -- sistema funcional" } else { "disparou" });

    println!("\n[Nivel: sobrevivencia] -> DISPARA HUMANOS");
    let r = bridge.check_and_trigger("sobrevivencia", -23.5510, -46.6340, "Bateria critica + GPS perdido. Usuario vulneravel.");
    if let Some(r) = r {
        if r["success"].as_bool().unwrap_or(false) {
            println!("  AJUDANTE: {} a {}km", r["helper"], r["distance_km"]);
            println!("  ETA: {} min", r["eta_minutes"]);
        } else {
            println!("  Escalado para emergencia publica");
        }
    } else {
        println!("  Nao disparou");
    }

    println!("\n[Nivel: completo novamente] -> CANCELA");
    let r = bridge.check_and_trigger("completo", 0.0, 0.0, "");
    if let Some(r) = r {
        println!("  {}", r.get("message").unwrap_or(&serde_json::json!("Cancelado")));
    }
}

pub fn scenario_ring_escalation() {
    /// Cenario: anel 0 nao atende -> sobe para anel 1 -> 2 -> etc.
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 5: Escalacao de aneis (ninguem atende)");
    println!("{}", "=".repeat(65));

    let mut net = HumanNet::new("Teste", "+5511****0000");
    net.update_user_location(-23.5500, -46.6300);

    let mut rng = rand::thread_rng();
    rng.gen::<f64>(); // seed simulation

    let mut h1 = AuthorizedHuman::new(
        "h1", "Familiar 1", "+55111",
        TrustRing::Family, AuthorizationLevel::Full, "irmao",
        Some((-23.5490, -46.6290)),
    );
    h1.response_timeout_s = 10;
    net.register_human(h1);

    let mut h2 = AuthorizedHuman::new(
        "h2", "Cuidador 1", "+5512",
        TrustRing::Caregiver, AuthorizationLevel::High, "cuidador",
        Some((-23.5480, -46.6280)),
    );
    h2.response_timeout_s = 10;
    net.register_human(h2);

    let mut h3 = AuthorizedHuman::new(
        "h3", "Comunidade 1", "+5513",
        TrustRing::Community, AuthorizationLevel::Medium, "vizinho Republica",
        Some((-23.5470, -46.6270)),
    );
    h3.response_timeout_s = 10;
    net.register_human(h3);

    let result = net.trigger_emergency_call(
        "Usuario incapacitado. Necessita assistencia fisica imediata.",
        0.0,
        0.0,
        "catastrophic",
    );

    if result["success"].as_bool().unwrap_or(false) {
        println!("\nAlguem atendeu: {}", result["helper"]);
    } else {
        println!("\nNinguem atendeu nos aneis pessoais.");
        if result.get("escalated_to_emergency").is_some() {
            let er = &result["emergency_result"];
            println!("Escalacao para emergencia publica: {}", er["service"]);
        }
    }

    println!("\nTentativas ({}):", result.get("all_attempts").and_then(|a| a.as_array()).map_or(0, |v| v.len()));
    if let Some(attempts) = result.get("all_attempts").and_then(|a| a.as_array()) {
        for a in attempts {
            let status_icon = if a["status"] == "Confirmed" { "OK" } else { "X " };
            println!("  [{}] anel={:12} {:15} dist={}km", status_icon, a["ring"], a["human"], a["distance_km"]);
        }
    }
}

pub fn scenario_child_lost() {
    /// Cenario: crianca perdida no shopping.
    println!("\n{}", "=".repeat(65));
    println!("CENARIO 6: Crianca perdida no shopping");
    println!("{}", "=".repeat(65));

    let mut net = HumanNet::new("Sophia (8 anos)", "+5511****0000");
    net.update_user_location(-23.5610, -46.6560);

    let mut pai = AuthorizedHuman::new(
        "pai", "Cleiton (Pai)", "+5511****9999",
        TrustRing::Family, AuthorizationLevel::Full, "pai",
        Some((-23.5505, -46.6333)),
    );
    pai.preferred_contact = ContactMethod::PhoneCall;
    pai.response_timeout_s = 15;
    pai.max_distance_km = 20.0;
    net.register_human(pai);

    let mut mae = AuthorizedHuman::new(
        "mae", "MING (Mae)", "+5511****8888",
        TrustRing::Family, AuthorizationLevel::Full, "mae",
        Some((-23.5505, -46.6333)),
    );
    mae.preferred_contact = ContactMethod::PhoneCall;
    mae.response_timeout_s = 15;
    mae.max_distance_km = 20.0;
    net.register_human(mae);

    let result = net.trigger_emergency_call(
        "Crianca de 8 anos separada dos pais no shopping. Sistema da Republica detectou saida de zona segura.",
        0.0,
        0.0,
        "critical",
    );

    if result["success"].as_bool().unwrap_or(false) {
        println!("\n{} confirmou! Esta a caminho.", result["helper"]);
        println!("Distancia: {}km | ETA: {}min", result["distance_km"], result["eta_minutes"]);
    } else {
        println!("\nEscalado para emergencia.");
    }
}

// ============================================================================
// 8. DEMONSTRACAO (main)
// ============================================================================

fn main() {
    println!("{}", "=".repeat(70));
    println!("OpenHumanNet -- Chamar o Humano Autorizado Mais Proximo");
    println!("{}", "=".repeat(70));

    let mut net = create_default_network("Cleiton");
    net.update_user_location(-23.5505, -46.6333);

    println!("\nUsuario: {}", net.user_name);
    println!("Localizacao: {:?}", net.user_location);
    println!("Humanos registrados: {}", net.registry.len());

    let humans_by_ring = net.list_humans();
    println!("\nRede por aneis:");
    for ring in [
        TrustRing::Family,
        TrustRing::Caregiver,
        TrustRing::Community,
        TrustRing::Professional,
        TrustRing::Emergency,
        TrustRing::Bystander,
    ] {
        let humans = humans_by_ring.get(&ring).map_or(&vec![], |v| v);
        println!("  Anel {} ({:?}): {} humano(s)", ring as u8, ring, humans.len());
        for h in humans {
            let dist = h.distance_to(-23.5505, -46.6333);
            println!(
                "    - {:15} ({:15}) auth={:15} dist={:.1}km",
                h.name, h.relationship, format!("{:?}", h.authorization), dist
            );
        }
    }

    // Cenarios
    scenario_blind_lost_battery();
    scenario_elderly_fall();
    scenario_seizure();
    scenario_resilience_integration();
    scenario_ring_escalation();
    scenario_child_lost();

    // Cobertura
    println!("\n{}", "=".repeat(70));
    println!("COBERTURA DO SISTEMA");
    println!("{}", "=".repeat(70));

    println!("\n  Aneis de confianca: 6");
    for r in [
        TrustRing::Family,
        TrustRing::Caregiver,
        TrustRing::Community,
        TrustRing::Professional,
        TrustRing::Emergency,
        TrustRing::Bystander,
    ] {
        println!("    Anel {}: {:?}", r as u8, r);
    }

    println!("\n  Niveis de autorizacao: 5");
    for a in [
        AuthorizationLevel::Full,
        AuthorizationLevel::High,
        AuthorizationLevel::Medium,
        AuthorizationLevel::Low,
        AuthorizationLevel::EmergencyOnly,
    ] {
        println!("    {:?}", a);
    }

    println!("\n  Metodos de contato: 8");
    for c in [
        ContactMethod::PhoneCall,
        ContactMethod::Sms,
        ContactMethod::Whatsapp,
        ContactMethod::VideoCall,
        ContactMethod::AppPush,
        ContactMethod::Smartwatch,
        ContactMethod::HomeAssistant,
        ContactMethod::PhysicalVisit,
    ] {
        println!("    {:?}", c);
    }

    println!("\n  Estados de chamada: 8");
    for s in [
        CallStatus::Pending,
        CallStatus::Ringing,
        CallStatus::Answered,
        CallStatus::Confirmed,
        CallStatus::Declined,
        CallStatus::Timeout,
        CallStatus::Failed,
        CallStatus::Cancelled,
    ] {
        println!("    {:?}", s);
    }

    println!("\n  FLUXO DE PRIORIDADE:");
    println!("    1. Sistema detecta falha (OpenResilience: SURVIVAL/EMERGENCY)");
    println!("    2. Pegar localizacao do usuario (GPS/ultima/triangulacao)");
    println!("    3. Ranquear humanos: anel -> distancia -> disponibilidade");
    println!("    4. Chamar Anel 0 (Familia) primeiro");
    println!("    5. Se familia nao atende -> Anel 1 (Cuidador)");
    println!("    6. Se cuidador nao atende -> Anel 2 (Comunidade)");
    println!("    7. Se comunidade nao atende -> Anel 3 (Profissional)");
    println!("    8. Se profissional nao atende -> Anel 4 (190/192/193)");
    println!("    9. PARAR quando humano CONFIRMA que vai ajudar");
    println!("   10. Se ninguem -> Anel 5 (estranho proximo via app)");

    println!("\n{}", "=".repeat(70));
    println!("A tecnologia NAO substitui o humano.");
    println!("A tecnologia CONECTA o humano CERTO no momento CERTO.");
    println!("\nTODO hardware falha. TODO software cai.");
    println!("O HUMANO e o sistema final. Ele nunca falha.");
}