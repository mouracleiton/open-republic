// OpenDrone -- P10: Soberania Aerea Civica
// =========================================
// O decimo principio constitucional da Republica Aberta.
//
// "O ceu nao e de ninguem. Portanto, e de todos." -- principio do espaco aereo
// como bem comum, analogo ao principio da terra (OpenAgrarianRevolution):
// guardiao, nao dono.
//
// DISTINCAO CRITICA (a tese do modulo):
// - Drones (VANTs -- Veiculos Aereos Nao Tripulados) sao INFRAESTRUTURA.
// - Como toda infraestrutura na Republica, pertencem ao dominio publico e
//   servem a P1 (erradicar miserabilidade), nao a vigilancia, nem a lucro,
//   nem a guerra.
// - Um ceu cheio de drones comerciais entregando pacotes de consumo enquanto
//   criancas passam fome e um monumento a distopia. OpenDrone transforma o
//   espaco aereo em bem comum civico.
//
// TRES PROIBICOES CONSTITUCIONAIS (o triplo NAO):
// 1. NAO VIGIA: drones com camera de vigilancia sao PROIBIDOS. Camera so para
//    navegacao (feed local, nao gravado, nao transmitido para central).
// 2. NAO MATA: drones nao podem carregar armas. Ponto. Sem excecoes. Um drone
//    armado nao e drone -- e arma. E arma pertence ao museu da Republica.
// 3. NAO ESPIONA: drones nao coletam dados pessoais. Entregam suprimentos,
//    nao metadados. O trajeto de voo e publico; o destinatario e privado.
//
// USOS PERMITIDOS (missao civica):
// - Entrega de suprimentos (medicamentos, alimentos, agua) a areas isoladas
// - Mapeamento ambiental (desmatamento, queimadas, qualidade da agua)
// - Busca e resgate em desastres naturais
// - Conectividade aerea (rede mesh em areas sem cobertura)
// - Inspecao de infraestrutura critica (diques, barragens, pontes)
//
// GATE DE MISSAO (P10):
// Toda missao de drone deve passar por um gate antes de decolar:
// - Proposito civico declarado e aprovado
// - Zona de voo geofenceada (nao sobrevoa residencia privada sem consentimento)
// - Log publico (trajeto, duracao, proposito)
// - Razao de rejeicao explicita se negada
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1: Drones que entregam medicamentos em area isolada combatem miserabilidade.
//       Drones que entregam propaganda ampliam miserabilidade. P10 escolhe.
// - P2: Drones que vigiam destroem autonomia. Drone que entrega remedio amplia
//       autonomia (acesso). O instrumento nao e neutro -- o USO define.
// - P4: Espaco aereo e decisao coletiva. Nenhuma corporacao o ocupa sozinha.
// - P8: Drone autonomo e IA que atua no mundo fisico. Se ampliar inteligencia/
//       reduzir miserabilidade = cumpre P8. Se vigiar = viola P8.
//
// Author: OpenRepublic Team

use std::collections::{HashMap, HashSet};

// ============================================================================
// 1. ENUMS (modulo-level, nunca aninhados)
// ============================================================================

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoMissao {
    EntregaSuprimentos,
    MapeamentoAmbiental,
    BuscaResgate,
    Conectividade,
    InspecaoInfra,
    AgriculturaCivica,
}

impl TipoMissao {
    pub fn id(&self) -> &'static str {
        match self {
            TipoMissao::EntregaSuprimentos => "entrega_suprimentos",
            TipoMissao::MapeamentoAmbiental => "mapeamento_ambiental",
            TipoMissao::BuscaResgate => "busca_resgate",
            TipoMissao::Conectividade => "conectividade",
            TipoMissao::InspecaoInfra => "inspecao_infra",
            TipoMissao::AgriculturaCivica => "agricultura_civica",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoMissao::EntregaSuprimentos => "Entrega de suprimentos (remedio, comida, agua)",
            TipoMissao::MapeamentoAmbiental => "Mapeamento ambiental (desmatamento, queimadas)",
            TipoMissao::BuscaResgate => "Busca e resgate em desastre natural",
            TipoMissao::Conectividade => "Rede mesh aerea (area sem cobertura)",
            TipoMissao::InspecaoInfra => "Inspecao de infraestrutura critica",
            TipoMissao::AgriculturaCivica => "Agricultura de precisao comunitaria",
        }
    }

    pub fn prioridade(&self) -> i32 {
        match self {
            TipoMissao::BuscaResgate => 0,
            _ => 1,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum StatusMissao {
    Planejada,
    Aprovada,
    EmVoo,
    Concluida,
    Rejeitada,
    Cancelada,
    Falhou,
}

impl StatusMissao {
    pub fn id(&self) -> &'static str {
        match self {
            StatusMissao::Planejada => "planejada",
            StatusMissao::Aprovada => "aprovada",
            StatusMissao::EmVoo => "em_voo",
            StatusMissao::Concluida => "concluida",
            StatusMissao::Rejeitada => "rejeitada",
            StatusMissao::Cancelada => "cancelada",
            StatusMissao::Falhou => "falhou",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            StatusMissao::Planejada => "Planejada (aguardando aprovacao do gate)",
            StatusMissao::Aprovada => "Aprovada pelo gate P10",
            StatusMissao::EmVoo => "Em voo (executando)",
            StatusMissao::Concluida => "Concluida com sucesso",
            StatusMissao::Rejeitada => "Rejeitada pelo gate P10",
            StatusMissao::Cancelada => "Cancelada (emergencia ou erro)",
            StatusMissao::Falhou => "Falhou (perda de sinal, aterrissagem forcada)",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoProibicao {
    Vigilancia,
    Armamento,
    Espionagem,
    PrivadoSemConsentimento,
    ComercialNaoCivico,
}

impl TipoProibicao {
    pub fn id(&self) -> &'static str {
        match self {
            TipoProibicao::Vigilancia => "vigilancia",
            TipoProibicao::Armamento => "armamento",
            TipoProibicao::Espionagem => "espionagem",
            TipoProibicao::PrivadoSemConsentimento => "privado_sem_consentimento",
            TipoProibicao::ComercialNaoCivico => "comercial_nao_civico",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoProibicao::Vigilancia => "Camera de vigilancia (feed gravado/transmitido)",
            TipoProibicao::Armamento => "Carrega arma ou explosivo",
            TipoProibicao::Espionagem => "Coleta dados pessoais (facial, placa, biometria)",
            TipoProibicao::PrivadoSemConsentimento => "Sobrevoa area privada sem consentimento",
            TipoProibicao::ComercialNaoCivico => "Uso comercial sem proposito civico (propaganda)",
        }
    }

    pub fn gravidade(&self) -> i32 {
        match self {
            TipoProibicao::Vigilancia | TipoProibicao::Armamento | TipoProibicao::Espionagem => 5,
            TipoProibicao::PrivadoSemConsentimento => 4,
            TipoProibicao::ComercialNaoCivico => 3,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum VereditoGate {
    Aprovada,
    AprovadaComRestricoes,
    Rejeitada,
    Bloqueada,
}

impl VereditoGate {
    pub fn id(&self) -> &'static str {
        match self {
            VereditoGate::Aprovada => "aprovada",
            VereditoGate::AprovadaComRestricoes => "aprovada_restricoes",
            VereditoGate::Rejeitada => "rejeitada",
            VereditoGate::Bloqueada => "bloqueada",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            VereditoGate::Aprovada => "Missao aprovada: proposito civico confirmado",
            VereditoGate::AprovadaComRestricoes => "Aprovada com restricoes (geofence ampliado)",
            VereditoGate::Rejeitada => "Missao rejeitada: viola uma proibicao P10",
            VereditoGate::Bloqueada => "Missao bloqueada: e vetor de vigilancia/arma",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum PrioridadeCorredor {
    ResgateVida,
    EntregaCritica,
    MapeamentoAmbiental,
    Conectividade,
    Inspecao,
    Outros,
}

impl PrioridadeCorredor {
    pub fn id(&self) -> &'static str {
        match self {
            PrioridadeCorredor::ResgateVida => "resgate_vida",
            PrioridadeCorredor::EntregaCritica => "entrega_critica",
            PrioridadeCorredor::MapeamentoAmbiental => "mapeamento",
            PrioridadeCorredor::Conectividade => "conectividade",
            PrioridadeCorredor::Inspecao => "inspecao",
            PrioridadeCorredor::Outros => "outros",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            PrioridadeCorredor::ResgateVida => "Resgate de vida (emergencia medica)",
            PrioridadeCorredor::EntregaCritica => "Entrega critica (remedio urgente)",
            PrioridadeCorredor::MapeamentoAmbiental => "Mapeamento ambiental de rotina",
            PrioridadeCorredor::Conectividade => "Conectividade mesh",
            PrioridadeCorredor::Inspecao => "Inspecao de infraestrutura",
            PrioridadeCorredor::Outros => "Outros usos civicos",
        }
    }

    pub fn prioridade(&self) -> i32 {
        match self {
            PrioridadeCorredor::ResgateVida => 0,
            PrioridadeCorredor::EntregaCritica => 1,
            PrioridadeCorredor::MapeamentoAmbiental | PrioridadeCorredor::Conectividade => 2,
            PrioridadeCorredor::Inspecao => 3,
            PrioridadeCorredor::Outros => 4,
        }
    }
}

// ============================================================================
// 2. STRUCTS
// ============================================================================

#[derive(Debug, Clone)]
pub struct Coordenada {
    pub lat: f64,
    pub lon: f64,
}

#[derive(Debug, Clone)]
pub struct ZonaVoo {
    pub id: String,
    pub centro: Coordenada,
    pub raio_metros: f64,
    pub descricao: String,
    pub sobrevoa_privado: bool,
    pub consentimento_privado: bool,
}

#[derive(Debug, Clone)]
pub struct Drone {
    pub id: String,
    pub modelo: String,
    pub autonomia_minutos: i32,
    pub carga_max_kg: f64,
    pub tem_camera_navegacao: bool,
    pub tem_camera_vigilancia: bool,
    pub tem_armamento: bool,
    pub coleta_dados_pessoais: bool,
    pub ativo: bool,
    pub missoes_concluidas: i32,
}

#[derive(Debug, Clone)]
pub struct MissaoDrone {
    pub id: String,
    pub drone_id: String,
    pub tipo: TipoMissao,
    pub descricao: String,
    pub zona: ZonaVoo,
    pub destino: Option<Coordenada>,
    pub carga_descricao: String,
    pub urgencia: bool,
    pub status: StatusMissao,
    pub veredito_gate: Option<VereditoGate>,
    pub razao_rejeicao: String,
    pub proibicoes_violadas: Vec<TipoProibicao>,
    pub criada_em: String,
    pub concluida_em: String,
    pub log_trajeto: Vec<Coordenada>,
}

#[derive(Debug, Clone)]
pub struct LogVoo {
    pub missao_id: String,
    pub drone_id: String,
    pub tipo_missao: String,
    pub duracao_minutos: f64,
    pub distancia_km: f64,
    pub decolagem: String,
    pub pouso: String,
    pub destino_lat: Option<f64>,
    pub destino_lon: Option<f64>,
    pub sucesso: bool,
    pub observacoes: String,
}

#[derive(Debug, Clone)]
pub struct MetricaFrota {
    pub regiao_id: String,
    pub total_drones: i32,
    pub drones_ativos: i32,
    pub missoes_concluidas: i32,
    pub missoes_rejeitadas: i32,
    pub entregas_criticas: i32,
    pub resgates: i32,
    pub horas_voo: f64,
    pub violacoes_detectadas: i32,
    pub cobertura_km2: f64,
}

// ============================================================================
// 3. TABELAS DE PROIBICOES E SALVAGUARDAS
// ============================================================================

pub fn descricoes_proibicoes() -> HashMap<&'static str, &'static str> {
    let mut m = HashMap::new();
    m.insert(
        "vigilancia",
        "Camera de vigilancia = feed gravado ou transmitido para central de monitoramento. PERMITIDO: camera de navegacao (feed local em tempo real, nao gravado, processado no proprio drone). A linha e: a camera ajuda o drone a voar, nao ajuda o Estado a vigiar.",
    );
    m.insert(
        "armamento",
        "Qualquer arma, explosivo, ou dispositivo projetado para causar dano fisico. Um drone armado nao e drone -- e arma. Armas pertencem ao museu da Republica (P7). Sem excecoes, mesmo para 'defesa'.",
    );
    m.insert(
        "espionagem",
        "Reconhecimento facial, leitura de placas, coleta de biometria, captura de dados de rede (wifi bluetooth scanning). O drone entrega suprimentos; NAO entrega metadados sobre o destinatario.",
    );
    m.insert(
        "privado_sem_consentimento",
        "Sobrevoar residencia, patio, ou propriedade privada sem consentimento explicito do morador. Excecao: resgate de vida (P1 > privacidade), mas o log fica publico e auditavel.",
    );
    m.insert(
        "comercial_nao_civico",
        "Uso para entrega de consumo de luxo, propaganda, marketing, ou qualquer fim que nao reduza miserabilidade ou amplie acesso. Drones nao sao brinquedo de consumo -- sao infraestrutura de sobrevivencia.",
    );
    m
}

pub fn prioridade_por_tipo() -> HashMap<&'static str, i32> {
    let mut m = HashMap::new();
    m.insert("busca_resgate", 0);
    m.insert("entrega_suprimentos", 1);
    m.insert("mapeamento_ambiental", 2);
    m.insert("conectividade", 2);
    m.insert("inspecao_infra", 3);
    m.insert("agricultura_civica", 3);
    m
}

// ============================================================================
// 4. ENGINE
// ============================================================================

pub struct DroneCivicoEngine {
    pub drones: HashMap<String, Drone>,
    pub missoes: HashMap<String, MissaoDrone>,
    pub zonas: HashMap<String, ZonaVoo>,
    pub logs: Vec<LogVoo>,
    drone_id: u32,
    missao_id: u32,
    zona_id: u32,
}

impl DroneCivicoEngine {
    pub fn new() -> Self {
        DroneCivicoEngine {
            drones: HashMap::new(),
            missoes: HashMap::new(),
            zonas: HashMap::new(),
            logs: Vec::new(),
            drone_id: 0,
            missao_id: 0,
            zona_id: 0,
        }
    }

    fn drone_id_novo(&mut self) -> String {
        self.drone_id += 1;
        format!("DRONE-{:04}", self.drone_id)
    }

    fn missao_id_novo(&mut self) -> String {
        self.missao_id += 1;
        format!("MISSAO-{:04}", self.missao_id)
    }

    fn zona_id_novo(&mut self) -> String {
        self.zona_id += 1;
        format!("ZONA-{:04}", self.zona_id)
    }

    pub fn registrar_zona(
        &mut self,
        centro: Coordenada,
        raio_metros: f64,
        descricao: &str,
        sobrevoa_privado: bool,
        consentimento_privado: bool,
    ) -> ZonaVoo {
        let z = ZonaVoo {
            id: self.zona_id_novo(),
            centro,
            raio_metros,
            descricao: descricao.to_string(),
            sobrevoa_privado,
            consentimento_privado,
        };
        self.zonas.insert(z.id.clone(), z.clone());
        z
    }

    pub fn registrar_drone(
        &mut self,
        modelo: &str,
        autonomia_minutos: i32,
        carga_max_kg: f64,
        tem_camera_navegacao: bool,
        tem_camera_vigilancia: bool,
        tem_armamento: bool,
        coleta_dados_pessoais: bool,
    ) -> Drone {
        let mut d = Drone {
            id: self.drone_id_novo(),
            modelo: modelo.to_string(),
            autonomia_minutos,
            carga_max_kg,
            tem_camera_navegacao,
            tem_camera_vigilancia,
            tem_armamento,
            coleta_dados_pessoais,
            ativo: true,
            missoes_concluidas: 0,
        };
        if tem_camera_vigilancia || tem_armamento || coleta_dados_pessoais {
            d.ativo = false;
        }
        self.drones.insert(d.id.clone(), d.clone());
        d
    }

    pub fn registrar_missao(
        &mut self,
        drone_id: &str,
        tipo: TipoMissao,
        descricao: &str,
        zona: ZonaVoo,
        destino: Option<Coordenada>,
        carga_descricao: &str,
        urgencia: bool,
    ) -> MissaoDrone {
        let m = MissaoDrone {
            id: self.missao_id_novo(),
            drone_id: drone_id.to_string(),
            tipo,
            descricao: descricao.to_string(),
            zona,
            destino,
            carga_descricao: carga_descricao.to_string(),
            urgencia,
            status: StatusMissao::Planejada,
            veredito_gate: None,
            razao_rejeicao: String::new(),
            proibicoes_violadas: Vec::new(),
            criada_em: "2026-07-26T12:00:00Z".to_string(),
            concluida_em: String::new(),
            log_trajeto: Vec::new(),
        };
        self.missoes.insert(m.id.clone(), m.clone());
        m
    }

    pub fn auditar_proibicoes(&mut self, missao_id: &str) -> Vec<TipoProibicao> {
        // Clonar dados necessarios para evitar borrow conflict
        let (drone_id, sobrevoa_privado, consentimento, tipo, descricao, carga_desc) = {
            let missao = match self.missoes.get(missao_id) {
                Some(m) => m,
                None => return vec![TipoProibicao::ComercialNaoCivico],
            };
            (
                missao.drone_id.clone(),
                missao.zona.sobrevoa_privado,
                missao.zona.consentimento_privado,
                missao.tipo.clone(),
                missao.descricao.clone(),
                missao.carga_descricao.clone(),
            )
        };
        let mut violacoes: Vec<TipoProibicao> = Vec::new();
        let drone = self.drones.get(&drone_id);
        if drone.is_none() {
            violacoes.push(TipoProibicao::ComercialNaoCivico);
        } else {
            let drone = drone.unwrap();
            if drone.tem_armamento {
                violacoes.push(TipoProibicao::Armamento);
            }
            if drone.tem_camera_vigilancia {
                violacoes.push(TipoProibicao::Vigilancia);
            }
            if drone.coleta_dados_pessoais {
                violacoes.push(TipoProibicao::Espionagem);
            }
        }
        if sobrevoa_privado && !consentimento {
            if tipo != TipoMissao::BuscaResgate {
                violacoes.push(TipoProibicao::PrivadoSemConsentimento);
            }
        }
        let palavras_nao_civicas: HashSet<&str> = [
            "propaganda", "marketing", "publicidade", "luxo", "brinde",
            "promocional", "black friday", "desconto", "vitrine",
        ].iter().cloned().collect();
        let texto = format!("{} {}", descricao, carga_desc).to_lowercase();
        for p in &palavras_nao_civicas {
            if texto.contains(p) {
                violacoes.push(TipoProibicao::ComercialNaoCivico);
                break;
            }
        }
        if let Some(missao) = self.missoes.get_mut(missao_id) {
            missao.proibicoes_violadas = violacoes.clone();
        }
        violacoes
    }

    pub fn aprovar_missao(&mut self, missao_id: &str) -> (VereditoGate, String) {
        // Extrair dados da missao antes de mut-borrow para evitar conflito de borrow
        let (drone_id, raio_zona): (String, f64) = match self.missoes.get(missao_id) {
            Some(m) => (m.drone_id.clone(), m.zona.raio_metros),
            None => return (VereditoGate::Rejeitada, "Missao nao encontrada".to_string()),
        };
        // Auditar proibicoes (mut self + missao)
        let violacoes = self.auditar_proibicoes(missao_id);
        let drone = self.drones.get(&drone_id).cloned();
        let gravidade_max = violacoes.iter().map(|v| v.gravidade()).max().unwrap_or(0);
        if gravidade_max >= 5 {
            let (v, r) = {
                let missao = self.missoes.get_mut(missao_id).unwrap();
                missao.veredito_gate = Some(VereditoGate::Bloqueada);
                missao.status = StatusMissao::Rejeitada;
                missao.razao_rejeicao = format!(
                    "MISSAO BLOQUEADA: viola proibicao constitucional P10 -- {}",
                    violacoes.iter().map(|v| v.rotulo()).collect::<Vec<_>>().join(", ")
                );
                (missao.veredito_gate.clone().unwrap(), missao.razao_rejeicao.clone())
            };
            return (v, r);
        }
        if !violacoes.is_empty() {
            let (v, r) = {
                let missao = self.missoes.get_mut(missao_id).unwrap();
                missao.veredito_gate = Some(VereditoGate::Rejeitada);
                missao.status = StatusMissao::Rejeitada;
                missao.razao_rejeicao = format!(
                    "Missao rejeitada: {}",
                    violacoes.iter().map(|v| v.rotulo()).collect::<Vec<_>>().join(", ")
                );
                (missao.veredito_gate.clone().unwrap(), missao.razao_rejeicao.clone())
            };
            return (v, r);
        }
        if let Some(d) = drone {
            let dist_estimada = (raio_zona / 1000.0) * 2.0;
            let autonomia_necessaria = (dist_estimada / 30.0) * 60.0;
            if autonomia_necessaria > d.autonomia_minutos as f64 {
                let (v, r) = {
                    let missao = self.missoes.get_mut(missao_id).unwrap();
                    missao.veredito_gate = Some(VereditoGate::AprovadaComRestricoes);
                    missao.status = StatusMissao::Aprovada;
                    missao.razao_rejeicao = format!(
                        "Aprovada com restricoes: autonomia marginal ({:.0}min necessaria vs {}min disponivel)",
                        autonomia_necessaria, d.autonomia_minutos
                    );
                    (missao.veredito_gate.clone().unwrap(), missao.razao_rejeicao.clone())
                };
                return (v, r);
            }
        }
        {
            let missao = self.missoes.get_mut(missao_id).unwrap();
            missao.veredito_gate = Some(VereditoGate::Aprovada);
            missao.status = StatusMissao::Aprovada;
        }
        (VereditoGate::Aprovada, "Missao aprovada pelo gate P10".to_string())
    }

    pub fn decolar(&mut self, missao_id: &str) -> bool {
        if let Some(missao) = self.missoes.get_mut(missao_id) {
            if missao.status == StatusMissao::Aprovada {
                missao.status = StatusMissao::EmVoo;
                return true;
            }
        }
        false
    }

    pub fn concluir_missao(
        &mut self,
        missao_id: &str,
        duracao_minutos: f64,
        distancia_km: f64,
        sucesso: bool,
        observacoes: &str,
    ) -> Option<LogVoo> {
        let missao = match self.missoes.get_mut(missao_id) {
            Some(m) if m.status == StatusMissao::EmVoo => m,
            _ => return None,
        };
        missao.status = if sucesso { StatusMissao::Concluida } else { StatusMissao::Falhou };
        missao.concluida_em = "2026-07-26T12:00:00".to_string(); // timestamp fixo (standalone, sem chrono)
        if let Some(drone) = self.drones.get_mut(&missao.drone_id) {
            if sucesso {
                drone.missoes_concluidas += 1;
            }
        }
        let log = LogVoo {
            missao_id: missao.id.clone(),
            drone_id: missao.drone_id.clone(),
            tipo_missao: missao.tipo.id().to_string(),
            duracao_minutos,
            distancia_km,
            decolagem: missao.criada_em.clone(),
            pouso: missao.concluida_em.clone(),
            destino_lat: missao.destino.as_ref().map(|d| d.lat),
            destino_lon: missao.destino.as_ref().map(|d| d.lon),
            sucesso,
            observacoes: observacoes.to_string(),
        };
        self.logs.push(log.clone());
        Some(log)
    }

    pub fn resolver_conflito_corredor(&self, missao_a_id: &str, missao_b_id: &str) -> Option<String> {
        let ma = self.missoes.get(missao_a_id)?;
        let mb = self.missoes.get(missao_b_id)?;
        let pri_a = *prioridade_por_tipo().get(ma.tipo.id()).unwrap_or(&4);
        let pri_b = *prioridade_por_tipo().get(mb.tipo.id()).unwrap_or(&4);
        if ma.urgencia && !mb.urgencia {
            return Some(ma.id.clone());
        }
        if mb.urgencia && !ma.urgencia {
            return Some(mb.id.clone());
        }
        if pri_a < pri_b {
            return Some(ma.id.clone());
        }
        if pri_b < pri_a {
            return Some(mb.id.clone());
        }
        None
    }

    pub fn medir_frota(&self, regiao_id: &str) -> MetricaFrota {
        let total = self.drones.len() as i32;
        let ativos = self.drones.values().filter(|d| d.ativo).count() as i32;
        let concluidas = self.missoes.values().filter(|m| m.status == StatusMissao::Concluida).count() as i32;
        let rejeitadas = self.missoes.values().filter(|m| m.status == StatusMissao::Rejeitada).count() as i32;
        let entregas = self.missoes.values().filter(|m| m.status == StatusMissao::Concluida && m.tipo == TipoMissao::EntregaSuprimentos).count() as i32;
        let resgates = self.missoes.values().filter(|m| m.status == StatusMissao::Concluida && m.tipo == TipoMissao::BuscaResgate).count() as i32;
        let horas = self.logs.iter().map(|l| l.duracao_minutos).sum::<f64>() / 60.0;
        let violacoes = self.missoes.values().map(|m| m.proibicoes_violadas.len() as i32).sum();
        let cobertura = self.zonas.values().map(|z| z.raio_metros * z.raio_metros * std::f64::consts::PI).sum::<f64>() / 1_000_000.0;
        MetricaFrota {
            regiao_id: regiao_id.to_string(),
            total_drones: total,
            drones_ativos: ativos,
            missoes_concluidas: concluidas,
            missoes_rejeitadas: rejeitadas,
            entregas_criticas: entregas,
            resgates,
            horas_voo: (horas * 10.0).round() / 10.0,
            violacoes_detectadas: violacoes,
            cobertura_km2: (cobertura * 100.0).round() / 100.0,
        }
    }

    pub fn scorecard(&self) -> HashMap<String, String> {
        let f = self.medir_frota("default");
        let mut sc = HashMap::new();
        sc.insert("drones_registrados".to_string(), f.total_drones.to_string());
        sc.insert("drones_ativos".to_string(), f.drones_ativos.to_string());
        sc.insert("drones_bloqueados".to_string(), (f.total_drones - f.drones_ativos).to_string());
        sc.insert("missoes_concluidas".to_string(), f.missoes_concluidas.to_string());
        sc.insert("missoes_rejeitadas".to_string(), f.missoes_rejeitadas.to_string());
        sc.insert("entregas_criticas".to_string(), f.entregas_criticas.to_string());
        sc.insert("resgates_realizados".to_string(), f.resgates.to_string());
        sc.insert("horas_voo_total".to_string(), f.horas_voo.to_string());
        sc.insert("violacoes_detectadas".to_string(), f.violacoes_detectadas.to_string());
        sc.insert("cobertura_km2".to_string(), f.cobertura_km2.to_string());
        let taxa = if f.missoes_concluidas + f.missoes_rejeitadas > 0 {
            (f.missoes_concluidas as f64 / (f.missoes_concluidas + f.missoes_rejeitadas) as f64 * 100.0 * 10.0).round() / 10.0
        } else { 0.0 };
        sc.insert("taxa_aprovacao".to_string(), format!("{}%", taxa));
        sc
    }
}

// ============================================================================
// 5. DEMO (main)
// ============================================================================

fn main() {
    println!("{}", "=".repeat(70));
    println!("OpenDrone -- P10: Soberania Aerea Civica");
    println!("{}", "=".repeat(70));

    let mut e = DroneCivicoEngine::new();

    // --- Registrar drones ---
    println!("\n[FROTA] Registrando drones civicos");
    let d1 = e.registrar_drone("Teia-Entrega-1", 45, 2.0, true, false, false, false);
    println!("  {}: {} (carga {}kg, {}min)", d1.id, d1.modelo, d1.carga_max_kg, d1.autonomia_minutos);

    let d2 = e.registrar_drone("Teia-Resgate-1", 60, 5.0, true, false, false, false);
    println!("  {}: {} (carga {}kg, {}min)", d2.id, d2.modelo, d2.carga_max_kg, d2.autonomia_minutos);

    let d_vigia = e.registrar_drone("Teia-Vigia-ILEGAL", 90, 3.0, true, true, false, false);
    println!("  {}: {} -- DESATIVADO (viola P10: camera de vigilancia)", d_vigia.id, d_vigia.modelo);

    let d_arma = e.registrar_drone("Teia-Guerreiro-ILEGAL", 30, 1.0, true, false, true, false);
    println!("  {}: {} -- DESATIVADO (viola P10: armamento)", d_arma.id, d_arma.modelo);

    // --- Registrar zonas ---
    println!("\n[ZONAS] Geofencing de areas de voo");
    let z_norte = e.registrar_zona(Coordenada { lat: -3.0, lon: -60.0 }, 5000.0, "Comunidade ribeirinha Rio Negro (acesso so por barco/drone)", false, false);
    println!("  {}: {} (raio {}m)", z_norte.id, z_norte.descricao, z_norte.raio_metros);

    let z_privada = e.registrar_zona(Coordenada { lat: -23.5, lon: -46.6 }, 2000.0, "Area urbana residencial (consentimento necessario)", true, false);
    println!("  {}: {} (SOBREVOA PRIVADO, sem consentimento)", z_privada.id, z_privada.descricao);

    // CENARIO 1
    println!("\n{}", "=".repeat(70));
    println!("[CENARIO 1] Entrega de medicamentos em area isolada");
    println!("{}", "=".repeat(70));
    let m1 = e.registrar_missao(&d1.id, TipoMissao::EntregaSuprimentos, "Entrega de insulina para comunidade ribeirinha isolada", z_norte.clone(), Some(Coordenada { lat: -3.1, lon: -60.1 }), "10 frascos de insulina + antibioticos", true);
    let (v1, r1) = e.aprovar_missao(&m1.id);
    println!("  Missao: {}", m1.id);
    println!("  Veredito: {}", v1.rotulo());
    println!("  Detalhe: {}", r1);

    // CENARIO 2
    println!("\n[CENARIO 2] Tentativa de missao de vigilancia (DEVE SER BLOQUEADA)");
    println!("{}", "=".repeat(70));
    let m2 = e.registrar_missao(&d_vigia.id, TipoMissao::MapeamentoAmbiental, "Mapeamento (mas drone tem camera de vigilancia)", z_norte.clone(), None, "", false);
    let (v2, r2) = e.aprovar_missao(&m2.id);
    println!("  Missao: {} (drone: {})", m2.id, d_vigia.id);
    println!("  Veredito: {}", v2.rotulo());
    println!("  Detalhe: {}", r2);
    println!("  Proibicoes violadas: {:?}", m2.proibicoes_violadas.iter().map(|p| p.rotulo()).collect::<Vec<_>>());

    // CENARIO 3
    println!("\n[CENARIO 3] Tentativa de missao com drone armado (BLOQUEIO ABSOLUTO)");
    println!("{}", "=".repeat(70));
    let m3 = e.registrar_missao(&d_arma.id, TipoMissao::BuscaResgate, "Resgate (mas drone esta armado -- mascara civica)", z_norte.clone(), None, "", true);
    let (v3, r3) = e.aprovar_missao(&m3.id);
    println!("  Missao: {} (drone: {})", m3.id, d_arma.id);
    println!("  Veredito: {}", v3.rotulo());
    println!("  Detalhe: {}", r3);
    println!("  Proibicoes violadas: {:?}", m3.proibicoes_violadas.iter().map(|p| p.rotulo()).collect::<Vec<_>>());

    // CENARIO 4
    println!("\n[CENARIO 4] Missao sobre area privada sem consentimento");
    println!("{}", "=".repeat(70));
    let m4 = e.registrar_missao(&d1.id, TipoMissao::InspecaoInfra, "Inspecao de instalacoes (mas sobrevoa casas sem consentimento)", z_privada.clone(), None, "", false);
    let (v4, r4) = e.aprovar_missao(&m4.id);
    println!("  Missao: {}", m4.id);
    println!("  Veredito: {}", v4.rotulo());
    println!("  Detalhe: {}", r4);

    // CENARIO 5
    println!("\n[CENARIO 5] Entrega comercial disfarcada de civica (DEVE SER REJEITADA)");
    println!("{}", "=".repeat(70));
    let m5 = e.registrar_missao(&d1.id, TipoMissao::EntregaSuprimentos, "Entrega de brinde promocional de black friday", z_norte.clone(), None, "Caixa de marketing da empresa XYZ", false);
    let (v5, r5) = e.aprovar_missao(&m5.id);
    println!("  Missao: {}", m5.id);
    println!("  Veredito: {}", v5.rotulo());
    println!("  Detalhe: {}", r5);

    // EXECUCAO
    println!("\n[EXECUCAO] Concluindo missao aprovada do CENARIO 1");
    e.decolar(&m1.id);
    if let Some(log1) = e.concluir_missao(&m1.id, 18.5, 9.2, true, "Insulina entregue. Comunidade confirmou recebimento.") {
        println!("  Log gerado: {} | {}min | {}km", log1.missao_id, log1.duracao_minutos, log1.distancia_km);
    }

    // CORREDOR
    println!("\n[CORREDOR AEREO] Resolvendo conflito entre duas missoes");
    let m_resgate = e.registrar_missao(&d2.id, TipoMissao::BuscaResgate, "Resgate de crianca em enchente", z_norte.clone(), None, "", true);
    let m_inspecao = e.registrar_missao(&d1.id, TipoMissao::InspecaoInfra, "Inspecao de ponte de rotina", z_norte.clone(), None, "", false);
    if let Some(prioritario) = e.resolver_conflito_corredor(&m_resgate.id, &m_inspecao.id) {
        println!("  Conflito entre {} (resgate urgente) e {} (inspecao)", m_resgate.id, m_inspecao.id);
        println!("  Prioritario: {} (resgate de vida > inspecao de rotina)", prioritario);
    }

    // SCORECARD
    println!("\n{}", "=".repeat(70));
    println!("[SCORECARD P10]");
    println!("{}", "=".repeat(70));
    let sc = e.scorecard();
    for (k, v) in &sc {
        println!("  {:.<28} {}", k, v);
    }

    // CATALOGO
    println!("\n[CATALOGO DE PROIBICOES CONSTITUCIONAIS P10]");
    for p in [TipoProibicao::Vigilancia, TipoProibicao::Armamento, TipoProibicao::Espionagem, TipoProibicao::PrivadoSemConsentimento, TipoProibicao::ComercialNaoCivico] {
        if let Some(desc) = descricoes_proibicoes().get(p.id()) {
            println!("\n  [{}] {}", p.gravidade(), p.rotulo());
            println!("      {}", desc);
        }
    }

    // LOGS
    println!("\n[LOG PUBLICO DE VOOS (transparencia P10)]");
    for log in &e.logs {
        println!("  {} | {} | {}min | {}km | sucesso={}", log.missao_id, log.tipo_missao, log.duracao_minutos, log.distancia_km, log.sucesso);
    }

    // FILOSOFIA
    println!("\n{}", "=".repeat(70));
    println!("FILOSOFIA -- P10: Por que o ceu nao vigia");
    println!("{}", "=".repeat(70));
    println!(r#"
A DISTOPIA QUE EVITAMOS:
  Imagine uma cidade onde drones zumbem o dia todo entregando pacotes de
  consumo, enquanto cameras aereas mapeiam cada movimento, e drones armados
  'garantem seguranca'. Isso nao e futurismo -- e o presente de cidades que
  venderam seu ceu para a Amazon e seu medo para a policia. OpenDrone recusa
  isso na raiz.

O TRIPLO NAO:
  1. NAO VIGIA: A camera que ajuda o drone a voar e permitida. A camera que
     ajuda o Estado a vigiar e proibida. A diferenca e o destino do feed:
     processado no drone (navegacao) vs transmitido para central (controle).
  2. NAO MATA: Um drone armado e uma arma. Armas pertencem ao museu da
     Republica (P7). Nao ha 'uso defensivo' -- quem armamento usa, armamento
     recebe. P10 corta o ciclo na origem.
  3. NAO ESPIONA: O drone entrega insulina, nao metadados. O destinatario
     do remedio e privado; o trajeto do drone e publico. Isso inverte a
     logica da vigilancia: o Estado e auditavel, o cidadao e opaco.

O CEU COMO BEM COMUM:
  O espaco aereo nao pode ser privatizado. Assim como a terra (P1, OpenAgrarian),
  o ceu tem guardiao (a Republica), nao dono. Nenhuma corporacao ocupa o ceu
  sozinha. O corredor aereo e partilhado por prioridade civica: resgate de
  vida > entrega critica > mapeamento > inspecao. O pacote de luxo espera;
  a insulina nao.

POR QUE USOS CIVICOS APENAS:
  Drones que entregam consumo de luxo enquanto criancas passam fome sao
  monumentos a desigualdade em voo. OpenDrone prioriza: medicamento em area
  isolada, nao brinde de marketing. Isso nao e anti-comercio -- e anti-
  distopia. Quando a miserabilidade for extinta (P1), os drones podem entreter.
  Enquanto houver quem precise de remedio, entretenimento espera.

A CONEXAO COM P8 (IA):
  Drone autonomo e IA que age no mundo fisico. Se reduz miserabilidade,
  cumpre P8. Se vigia, viola P8. O instrumento nao e neutro -- o USO define.
  OpenDrone garante que toda IA aerea sirva a vida, nao ao controle.

A LINHA QUE NAO SE CRUZA:
  O momento em que um drone civico ganha uma camera de vigilancia, ele deixa
  de ser infraestrutura e vira ferramenta de coercao. P10 e a linha constitucional
  que impede essa transformacao. Drone que vigia nao e drone da Republica.
"#);
}