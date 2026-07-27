// OpenAntiPolarization -- P9: O Estado NAO Polariza
// ====================================================
// O nono principio constitucional da Republica Aberta.
//
// "Discordo de tudo que voce disse, mas darei minha vida para que voce possa
// dizer de novo." -- atribuido a Voltaire, encapsula o espirito deste modulo.
//
// DISTINCAO CRITICA (a tese do modulo):
// - Diversidade de opiniao e DIREITO (P2). E saudavel. E combustivel da democracia.
// - Polarizacao e DOENCA SISTEMICA. Nao e "opiniao diferente". E realidade
//   epistemica separada: duas tribos que nao so discordam, mas habitam mundos
//   de fato diferentes, com zero confianca mutua e identidade fundida na tribo.
//
// A Republica recusa o equivoco liberal de que "mais debate resolve polarizacao".
// Mais debate entre tribos epistemicamente separadas AMPLIFICA a polarizacao.
// O que resolve e: (a) chao de fato compartilhado, (b) deliberacao estruturada,
// (c) Estado que se recusa a ser vetor de divisao identitaria.
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1: Polarizacao recria elite. Sempre ha um lado que se beneficia da divisao.
// - P2: Identidade tribal captura autonomia. Quem so pensa pela tribo nao e livre.
// - P4: Democracia em assembleia polarizada nao e democracia -- e tirania de 51%.
// - P8: IA que amplifica polarizacao (engagement algorithms) VIOLA o principio
//   de ampliar inteligencia humana. Engenagement por furia e anti-P8.
//
// P9 -- ANTI-POLARIZACAO DE ESTADO:
// O Estado nao pode produzir, amplificar ou se beneficiar de divisao identitaria.
// Toda politica publica deve ser avaliada pelo seu POTENCIAL POLARIZANTE antes
// da votacao. E um GATE (como WCAG audita acessibilidade), nao um mod de censura.
//
// Author: OpenRepublic Team

use std::collections::{HashMap, HashSet};
use std::fmt;

// ============================================================================
// 1. ENUMS (modulo-level, nunca aninhados)
// ============================================================================

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum FatorPolarizacao {
    Religiao,
    Etnia,
    Regiao,
    Classe,
    Ideologia,
    Identidade,
    Lingua,
    Idade,
    Algoritmo,
    Cultura,
}

impl FatorPolarizacao {
    pub fn id(&self) -> &'static str {
        match self {
            FatorPolarizacao::Religiao => "religiao",
            FatorPolarizacao::Etnia => "etnia",
            FatorPolarizacao::Regiao => "regiao",
            FatorPolarizacao::Classe => "classe",
            FatorPolarizacao::Ideologia => "ideologia",
            FatorPolarizacao::Identidade => "identidade",
            FatorPolarizacao::Lingua => "lingua",
            FatorPolarizacao::Idade => "idade",
            FatorPolarizacao::Algoritmo => "algoritmo",
            FatorPolarizacao::Cultura => "cultura",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            FatorPolarizacao::Religiao => "Religiao / fe / espiritualidade",
            FatorPolarizacao::Etnia => "Etnia / raca / origem",
            FatorPolarizacao::Regiao => "Regiao / geografia (norte vs sul, urbano vs rural)",
            FatorPolarizacao::Classe => "Classe / origem economica (heranca do sistema antigo)",
            FatorPolarizacao::Ideologia => "Ideologia politica (heranca do sistema partidario)",
            FatorPolarizacao::Identidade => "Identidade de genero / sexual / expressao",
            FatorPolarizacao::Lingua => "Lingua / idioma / dialeto",
            FatorPolarizacao::Idade => "Geracional (jovens vs velhos)",
            FatorPolarizacao::Algoritmo => "Algoritmo de feed (captura narrativa externa)",
            FatorPolarizacao::Cultura => "Cultura / costumes / tradicao",
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum NivelPolarizacao {
    Saudavel,
    Baixo,
    Moderado,
    Alto,
    Critico,
    Ruptura,
}

impl NivelPolarizacao {
    pub fn id(&self) -> &'static str {
        match self {
            NivelPolarizacao::Saudavel => "saudavel",
            NivelPolarizacao::Baixo => "baixo",
            NivelPolarizacao::Moderado => "moderado",
            NivelPolarizacao::Alto => "alto",
            NivelPolarizacao::Critico => "critico",
            NivelPolarizacao::Ruptura => "ruptura",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            NivelPolarizacao::Saudavel => "Saudavel: dissenso produtivo, confianca preservada",
            NivelPolarizacao::Baixo => "Baixo: blocos incipientes, ainda deliberam",
            NivelPolarizacao::Moderado => "Moderado: blocos claros, deliberacao degrada",
            NivelPolarizacao::Alto => "Alto: votacao tribal, confianca em queda",
            NivelPolarizacao::Critico => "Critico: quase bloqueio assemblear",
            NivelPolarizacao::Ruptura => "Ruptura epistemica: realidades de fato separadas",
        }
    }

    pub fn gravidade(&self) -> i32 {
        match self {
            NivelPolarizacao::Saudavel => 0,
            NivelPolarizacao::Baixo => 1,
            NivelPolarizacao::Moderado => 2,
            NivelPolarizacao::Alto => 3,
            NivelPolarizacao::Critico => 4,
            NivelPolarizacao::Ruptura => 5,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum TaticaPolarizante {
    OutgroupDehumanization,
    FalseDichotomy,
    Whataboutism,
    FearMongering,
    IdentityBaiting,
    EpistemicBalkanization,
    BothSidesFallacy,
    Strawman,
    DogWhistle,
    VirtueSignaling,
}

impl TaticaPolarizante {
    pub fn id(&self) -> &'static str {
        match self {
            TaticaPolarizante::OutgroupDehumanization => "outgroup_dehumanization",
            TaticaPolarizante::FalseDichotomy => "false_dichotomy",
            TaticaPolarizante::Whataboutism => "whataboutism",
            TaticaPolarizante::FearMongering => "fear_mongering",
            TaticaPolarizante::IdentityBaiting => "identity_baiting",
            TaticaPolarizante::EpistemicBalkanization => "epistemic_balkanization",
            TaticaPolarizante::BothSidesFallacy => "both_sides_fallacy",
            TaticaPolarizante::Strawman => "strawman",
            TaticaPolarizante::DogWhistle => "dog_whistle",
            TaticaPolarizante::VirtueSignaling => "virtue_signaling",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TaticaPolarizante::OutgroupDehumanization => "Desumanizacao do outro lado",
            TaticaPolarizante::FalseDichotomy => "Falsa dicotomia (ou nos ou eles)",
            TaticaPolarizante::Whataboutism => "Whataboutism (desvia com 'mas eles tambem')",
            TaticaPolarizante::FearMongering => "Alarmismo / medo fabricado",
            TaticaPolarizante::IdentityBaiting => "Isca de identidade (forca tribalismo)",
            TaticaPolarizante::EpistemicBalkanization => "Balkanizacao epistemica (fatos tribais)",
            TaticaPolarizante::BothSidesFallacy => "Falsa simetria (os dois lados sao iguais)",
            TaticaPolarizante::Strawman => "Espantalho (deturpa para atacar)",
            TaticaPolarizante::DogWhistle => "Dog whistle (codigo tribal implicito)",
            TaticaPolarizante::VirtueSignaling => "Sinalizacao virtuosa (pertence vs exclui)",
        }
    }

    pub fn gravidade(&self) -> i32 {
        match self {
            TaticaPolarizante::OutgroupDehumanization => 5,
            TaticaPolarizante::FalseDichotomy => 4,
            TaticaPolarizante::Whataboutism => 3,
            TaticaPolarizante::FearMongering => 4,
            TaticaPolarizante::IdentityBaiting => 5,
            TaticaPolarizante::EpistemicBalkanization => 5,
            TaticaPolarizante::BothSidesFallacy => 3,
            TaticaPolarizante::Strawman => 2,
            TaticaPolarizante::DogWhistle => 4,
            TaticaPolarizante::VirtueSignaling => 2,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum StatusBloqueio {
    Nenhum,
    Alerta,
    DeliberacaoEstruturada,
    MediacaoObrigatoria,
    SuspenderVotacao,
    AssembleiaPausa,
}

impl StatusBloqueio {
    pub fn id(&self) -> &'static str {
        match self {
            StatusBloqueio::Nenhum => "nenhum",
            StatusBloqueio::Alerta => "alerta",
            StatusBloqueio::DeliberacaoEstruturada => "deliberacao_estruturada",
            StatusBloqueio::MediacaoObrigatoria => "mediacao_obrigatoria",
            StatusBloqueio::SuspenderVotacao => "suspender_votacao",
            StatusBloqueio::AssembleiaPausa => "assembleia_pausa",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            StatusBloqueio::Nenhum => "Nenhum: assembleia delibera normalmente",
            StatusBloqueio::Alerta => "Alerta: moderador sinaliza polarizacao",
            StatusBloqueio::DeliberacaoEstruturada => "Deliberacao estruturada obrigatoria",
            StatusBloqueio::MediacaoObrigatoria => "Mediacao obrigatoria antes de votar",
            StatusBloqueio::SuspenderVotacao => "Votacao suspensa (bloqueio ativo)",
            StatusBloqueio::AssembleiaPausa => "Pausa assemblear (resfriamento obrigatorio)",
        }
    }

    pub fn prioridade(&self) -> i32 {
        match self {
            StatusBloqueio::Nenhum => 0,
            StatusBloqueio::Alerta => 1,
            StatusBloqueio::DeliberacaoEstruturada => 2,
            StatusBloqueio::MediacaoObrigatoria => 3,
            StatusBloqueio::SuspenderVotacao => 4,
            StatusBloqueio::AssembleiaPausa => 5,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum VereditoAuditoria {
    Aprovada,
    AprovadaComRessalvas,
    Rejeitada,
    Bloqueada,
}

impl VereditoAuditoria {
    pub fn id(&self) -> &'static str {
        match self {
            VereditoAuditoria::Aprovada => "aprovada",
            VereditoAuditoria::AprovadaComRessalvas => "ressalvas",
            VereditoAuditoria::Rejeitada => "rejeitada",
            VereditoAuditoria::Bloqueada => "bloqueada",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            VereditoAuditoria::Aprovada => "Politica aprovada: baixo potencial polarizante",
            VereditoAuditoria::AprovadaComRessalvas => {
                "Aprovada com ressalvas (mitigacoes exigidas)"
            }
            VereditoAuditoria::Rejeitada => "Politica rejeitada: potencial polarizante alto",
            VereditoAuditoria::Bloqueada => "Politica bloqueada: e vetor de divisao identitaria",
        }
    }
}

// ============================================================================
// 2. STRUCTS (equivalente a dataclasses)
// ============================================================================

#[derive(Debug, Clone)]
pub struct VotoCidadao {
    pub cidadao_id: String,
    pub proposta_id: String,
    pub a_favor: bool,
    pub justificativa: String,
}

#[derive(Debug, Clone)]
pub struct PropostaAssembleia {
    pub id: String,
    pub titulo: String,
    pub descricao: String,
    pub fator_aparente: Option<FatorPolarizacao>,
    pub votacao_encerrada: bool,
}

#[derive(Debug, Clone)]
pub struct BlocoVotante {
    pub id: String,
    pub membros: Vec<String>,
    pub coesao: f64,
    pub fator_dominante: Option<FatorPolarizacao>,
}

#[derive(Debug, Clone)]
pub struct MetricaPolarizacao {
    pub assembleia_id: String,
    pub num_cidadaos: usize,
    pub num_blocos: usize,
    pub indice_divisao: f64,
    pub indice_tribalismo: f64,
    pub indice_ruptura_epistemica: f64,
    pub nivel: NivelPolarizacao,
    pub veredito: String,
}

#[derive(Debug, Clone)]
pub struct AuditoriaPolitica {
    pub politica_id: String,
    pub veredito: VereditoAuditoria,
    pub taticas_detectadas: Vec<TaticaPolarizante>,
    pub fatores_acionados: Vec<FatorPolarizacao>,
    pub score_polarizante: f64,
    pub mitigacoes: Vec<String>,
    pub justificativa: String,
}

// ============================================================================
// 3. TABELA DE SINAIS DE BALKANIZACAO EPISTEMICA
// ============================================================================

pub fn sinais_ruptura_epistemica() -> HashMap<&'static str, &'static str> {
    let mut m = HashMap::new();
    m.insert(
        "fontes_exclusivas",
        "Cada bloco cita fontes que o outro bloco considera falsas por principio",
    );
    m.insert(
        "vocabulario_incomum",
        "Cada bloco usa vocabulario que o outro nao entende ou rejeita",
    );
    m.insert(
        "desumanizacao",
        "Membros de um bloco descrevem o outro como inimigo, nao como cidadao",
    );
    m.insert(
        "voto_identidade",
        "Voto decidido por identidade tribal, nao por merito da proposta",
    );
    m.insert(
        "zero_trust",
        "Nenhuma afirmacao do outro lado e aceita mesmo quando factualmente correto",
    );
    m.insert(
        "purity_test",
        "Membros sao punidos por reconhecer merito em argumento do outro lado",
    );
    m.insert(
        "conspiracy_default",
        "Derrota politica e automaticamente atribuida a conspiracao",
    );
    m.insert(
        "violencia_normalizada",
        "Violencia contra o outro bloco e tratada como legitima",
    );
    m
}

// ============================================================================
// 4. ENGINE
// ============================================================================

pub struct AntiPolarizacaoEngine {
    pub propostas: HashMap<String, PropostaAssembleia>,
    pub votos: Vec<VotoCidadao>,
    pub blocos: HashMap<String, BlocoVotante>,
    pub auditorias: HashMap<String, AuditoriaPolitica>,
    prop_id: u32,
    bloco_id: u32,
}

impl AntiPolarizacaoEngine {
    pub fn new() -> Self {
        AntiPolarizacaoEngine {
            propostas: HashMap::new(),
            votos: Vec::new(),
            blocos: HashMap::new(),
            auditorias: HashMap::new(),
            prop_id: 0,
            bloco_id: 0,
        }
    }

    fn prop_id_novo(&mut self) -> String {
        self.prop_id += 1;
        format!("PROP-{:04}", self.prop_id)
    }

    fn bloco_id_novo(&mut self) -> String {
        self.bloco_id += 1;
        format!("BLOCO-{:04}", self.bloco_id)
    }

    pub fn registrar_proposta(
        &mut self,
        titulo: &str,
        descricao: &str,
        fator_aparente: Option<FatorPolarizacao>,
    ) -> PropostaAssembleia {
        let p = PropostaAssembleia {
            id: self.prop_id_novo(),
            titulo: titulo.to_string(),
            descricao: descricao.to_string(),
            fator_aparente,
            votacao_encerrada: false,
        };
        self.propostas.insert(p.id.clone(), p.clone());
        p
    }

    pub fn registrar_voto(
        &mut self,
        cidadao_id: &str,
        proposta_id: &str,
        a_favor: bool,
        justificativa: &str,
    ) -> VotoCidadao {
        let v = VotoCidadao {
            cidadao_id: cidadao_id.to_string(),
            proposta_id: proposta_id.to_string(),
            a_favor,
            justificativa: justificativa.to_string(),
        };
        self.votos.push(v.clone());
        v
    }

    pub fn registrar_votacao_em_lote(&mut self, votacoes: &[(String, String, bool)]) {
        for (cid, pid, fav) in votacoes {
            self.registrar_voto(cid, pid, *fav, "");
        }
    }

    pub fn encerrar_proposta(&mut self, proposta_id: &str) {
        if let Some(p) = self.propostas.get_mut(proposta_id) {
            p.votacao_encerrada = true;
        }
    }

    // -- deteccao de blocos ------------------------------------------------

    pub fn detectar_blocos(&mut self, num_propostas_min: usize) -> Vec<BlocoVotante> {
        self.blocos.clear();
        let mut assinaturas: HashMap<String, Vec<bool>> = HashMap::new();
        let mut prop_ids_ordenadas: Vec<String> = self.propostas.keys().cloned().collect();
        prop_ids_ordenadas.sort();

        for pid in &prop_ids_ordenadas {
            let mut votos_prop: HashMap<String, bool> = HashMap::new();
            for v in &self.votos {
                if v.proposta_id == *pid {
                    votos_prop.insert(v.cidadao_id.clone(), v.a_favor);
                }
            }
            for (cid, fav) in votos_prop {
                assinaturas.entry(cid).or_insert_with(Vec::new).push(fav);
            }
        }

        let cidadaos_validos: HashMap<String, Vec<bool>> = assinaturas
            .into_iter()
            .filter(|(_, s)| s.len() >= num_propostas_min)
            .collect();

        if cidadaos_validos.is_empty() {
            return vec![];
        }

        let mut grupos: HashMap<Vec<bool>, Vec<String>> = HashMap::new();
        for (cid, sig) in cidadaos_validos {
            grupos.entry(sig).or_insert_with(Vec::new).push(cid);
        }

        let mut blocos_criados: Vec<BlocoVotante> = Vec::new();
        for (sig, membros) in grupos {
            if membros.len() >= 2 {
                let b = BlocoVotante {
                    id: self.bloco_id_novo(),
                    membros: membros.clone(),
                    coesao: 1.0,
                    fator_dominante: None,
                };
                self.blocos.insert(b.id.clone(), b.clone());
                blocos_criados.push(b);
            }
        }

        if blocos_criados.len() == 2 {
            let mut tamanhos: Vec<usize> = blocos_criados.iter().map(|b| b.membros.len()).collect();
            tamanhos.sort();
            let razao = if tamanhos[1] > 0 {
                tamanhos[0] as f64 / tamanhos[1] as f64
            } else {
                0.0
            };
            if razao >= 0.4 {
                blocos_criados[0].fator_dominante = Some(FatorPolarizacao::Ideologia);
                blocos_criados[1].fator_dominante = Some(FatorPolarizacao::Ideologia);
            }
        }
        blocos_criados
    }

    // -- metricas ----------------------------------------------------------

    pub fn indice_divisao(&self) -> f64 {
        if self.propostas.is_empty() {
            return 0.0;
        }
        let mut prop_ids: Vec<String> = self.propostas.keys().cloned().collect();
        prop_ids.sort();
        let mut soma = 0.0;
        let mut count = 0;
        for pid in prop_ids {
            let votos_prop: Vec<bool> = self
                .votos
                .iter()
                .filter(|v| v.proposta_id == pid)
                .map(|v| v.a_favor)
                .collect();
            if votos_prop.is_empty() {
                continue;
            }
            let favor = votos_prop.iter().filter(|&&x| x).count();
            let contra = votos_prop.len() - favor;
            let total = votos_prop.len();
            let d = 1.0 - (favor as f64 - contra as f64).abs() / total as f64;
            soma += d;
            count += 1;
        }
        if count > 0 {
            (soma / count as f64 * 1000.0).round() / 1000.0
        } else {
            0.0
        }
    }

    pub fn indice_tribalismo(&mut self) -> f64 {
        let blocos = self.detectar_blocos(3);
        if blocos.is_empty() {
            return 0.0;
        }
        let mut cids_em_blocos: HashSet<String> = HashSet::new();
        for b in &blocos {
            for m in &b.membros {
                cids_em_blocos.insert(m.clone());
            }
        }
        let votos_tribais = self
            .votos
            .iter()
            .filter(|v| cids_em_blocos.contains(&v.cidadao_id))
            .count();
        let total_votos = self.votos.len();
        if total_votos > 0 {
            (votos_tribais as f64 / total_votos as f64 * 1000.0).round() / 1000.0
        } else {
            0.0
        }
    }

    pub fn indice_ruptura_epistemica(&self, sinais_observados: &[String]) -> f64 {
        if sinais_observados.is_empty() {
            return 0.0;
        }
        let sinais = sinais_ruptura_epistemica();
        let sinais_validos = sinais_observados
            .iter()
            .filter(|s| sinais.contains_key(s.as_str()))
            .count();
        let total_sinais = sinais.len();
        (sinais_validos as f64 / total_sinais as f64 * 1000.0).round() / 1000.0
    }

    pub fn classificar_nivel(&mut self, sinais_observados: Option<&[String]>) -> NivelPolarizacao {
        let div = self.indice_divisao();
        let trib = self.indice_tribalismo();
        let rupt = self.indice_ruptura_epistemica(sinais_observados.unwrap_or(&[]));
        if rupt >= 0.5 {
            return NivelPolarizacao::Ruptura;
        }
        if div >= 0.8 && trib >= 0.7 {
            return NivelPolarizacao::Critico;
        }
        if div >= 0.6 && trib >= 0.5 {
            return NivelPolarizacao::Alto;
        }
        if div >= 0.4 {
            return NivelPolarizacao::Moderado;
        }
        if div >= 0.2 {
            return NivelPolarizacao::Baixo;
        }
        NivelPolarizacao::Saudavel
    }

    pub fn medir_polarizacao(
        &mut self,
        assembleia_id: &str,
        sinais_observados: Option<&[String]>,
    ) -> MetricaPolarizacao {
        let blocos = self.detectar_blocos(3);
        let div = self.indice_divisao();
        let trib = self.indice_tribalismo();
        let rupt = self.indice_ruptura_epistemica(sinais_observados.unwrap_or(&[]));
        let nivel = self.classificar_nivel(sinais_observados);
        let mut cidadaos_unicos: HashSet<String> = HashSet::new();
        for v in &self.votos {
            cidadaos_unicos.insert(v.cidadao_id.clone());
        }
        let veredito = match nivel {
            NivelPolarizacao::Ruptura => "RUPTURA EPISTEMICA: realidades de fato separadas. Assembleia nao pode deliberar ate restaurar chao de fato compartilhado.".to_string(),
            NivelPolarizacao::Critico => "CRITICO: votacao tribal dominante. Mediacao obrigatoria antes de qualquer nova votacao.".to_string(),
            NivelPolarizacao::Alto => "ALTO: confianca em queda. Deliberacao estruturada exigida.".to_string(),
            NivelPolarizacao::Moderado => "MODERADO: blocos claros. Monitorar e facilitar dialogo.".to_string(),
            NivelPolarizacao::Baixo => "BAIXO: dissenso saudavel com sinal de alinhamento tribal incipiente.".to_string(),
            NivelPolarizacao::Saudavel => "SAUDAVEL: dissenso produtivo, confianca preservada.".to_string(),
        };
        MetricaPolarizacao {
            assembleia_id: assembleia_id.to_string(),
            num_cidadaos: cidadaos_unicos.len(),
            num_blocos: blocos.len(),
            indice_divisao: div,
            indice_tribalismo: trib,
            indice_ruptura_epistemica: rupt,
            nivel,
            veredito,
        }
    }

    // -- GATE P9: auditoria de politica ------------------------------------

    pub fn auditar_politica(
        &mut self,
        politica_id: &str,
        _titulo: &str,
        _descricao: &str,
        taticas_detectadas: &[TaticaPolarizante],
        fatores_acionados: &[FatorPolarizacao],
        sinais_ruptura: Option<&[String]>,
    ) -> AuditoriaPolitica {
        let taticas = taticas_detectadas.to_vec();
        let fatores = fatores_acionados.to_vec();

        let score_taticas: f64 = taticas
            .iter()
            .map(|t| t.gravidade() as f64 * 12.0)
            .sum::<f64>()
            .min(100.0);

        let fatores_identitarios: HashSet<FatorPolarizacao> = [
            FatorPolarizacao::Religiao,
            FatorPolarizacao::Etnia,
            FatorPolarizacao::Identidade,
            FatorPolarizacao::Cultura,
        ]
        .iter()
        .cloned()
        .collect();

        let penalidade_fator: f64 = fatores
            .iter()
            .map(|f| {
                if fatores_identitarios.contains(f) {
                    8.0
                } else {
                    4.0
                }
            })
            .sum();
        let mut score = (score_taticas + penalidade_fator).min(100.0);

        if let Some(sinais) = sinais_ruptura {
            let rupt = self.indice_ruptura_epistemica(sinais);
            score = (score + rupt * 30.0).min(100.0);
        }

        let mut mitigacoes: Vec<String> = Vec::new();
        if taticas.contains(&TaticaPolarizante::OutgroupDehumanization) {
            mitigacoes.push("Remover linguagem que desumaniza cidadaos do outro lado.".to_string());
        }
        if taticas.contains(&TaticaPolarizante::FalseDichotomy) {
            mitigacoes.push("Apresentar 3+ opcoes, nao binomio nos-vs-eles.".to_string());
        }
        if taticas.contains(&TaticaPolarizante::FearMongering) {
            mitigacoes.push("Substituir alarmismo por dados verificaveis e calmos.".to_string());
        }
        if taticas.contains(&TaticaPolarizante::IdentityBaiting) {
            mitigacoes.push(
                "Desacoplar a politica de identidade tribal (P9: Estado nao polariza).".to_string(),
            );
        }
        if taticas.contains(&TaticaPolarizante::EpistemicBalkanization) {
            mitigacoes.push(
                "Citar fontes reconhecidas por AMBOS os blocos (chao de fato compartilhado)."
                    .to_string(),
            );
        }
        if fatores.iter().any(|f| fatores_identitarios.contains(f)) {
            mitigacoes.push(
                "Reescrever sem apelar a divisao identitaria (religiao/etnia/identidade)."
                    .to_string(),
            );
        }
        if score >= 40.0 && score < 70.0 {
            mitigacoes.push("Submeter a deliberacao estruturada antes da votacao.".to_string());
        }
        if score >= 70.0 {
            mitigacoes.push("Politica deve ser fundamentalmente reformulada.".to_string());
        }

        let (veredito, justif) = if score >= 75.0 {
            (VereditoAuditoria::Bloqueada, "P9 VIOLADO: a politica e vetor de divisao identitaria. Reescrever do zero sem acionar tribo.".to_string())
        } else if score >= 50.0 {
            (
                VereditoAuditoria::Rejeitada,
                "Potencial polarizante alto. Rejeitada ate mitigacoes aplicadas.".to_string(),
            )
        } else if score >= 25.0 {
            (
                VereditoAuditoria::AprovadaComRessalvas,
                "Aprovada condicionalmente. Mitigacoes exigidas antes da votacao.".to_string(),
            )
        } else {
            (
                VereditoAuditoria::Aprovada,
                "Baixo potencial polarizante. Livre para votacao.".to_string(),
            )
        };

        let aud = AuditoriaPolitica {
            politica_id: politica_id.to_string(),
            veredito,
            taticas_detectadas: taticas,
            fatores_acionados: fatores,
            score_polarizante: (score * 10.0).round() / 10.0,
            mitigacoes,
            justificativa: justif,
        };
        self.auditorias.insert(politica_id.to_string(), aud.clone());
        aud
    }

    // -- protocolo de bloqueio assemblear ----------------------------------

    pub fn protocolo_bloqueio(&self, metrica: &MetricaPolarizacao) -> StatusBloqueio {
        match metrica.nivel {
            NivelPolarizacao::Ruptura => StatusBloqueio::AssembleiaPausa,
            NivelPolarizacao::Critico => StatusBloqueio::SuspenderVotacao,
            NivelPolarizacao::Alto => StatusBloqueio::MediacaoObrigatoria,
            NivelPolarizacao::Moderado => StatusBloqueio::DeliberacaoEstruturada,
            NivelPolarizacao::Baixo => StatusBloqueio::Alerta,
            NivelPolarizacao::Saudavel => StatusBloqueio::Nenhum,
        }
    }

    pub fn recomendacoes_mediacao(&self, metrica: &MetricaPolarizacao) -> Vec<String> {
        let mut recs: Vec<String> = Vec::new();
        match metrica.nivel {
            NivelPolarizacao::Saudavel => {
                recs.push("Manter: dissenso produtivo e saudavel (P2).".to_string());
            }
            NivelPolarizacao::Baixo | NivelPolarizacao::Moderado => {
                recs.push(
                    "Facilitar dialogo estruturado entre blocos (nao debate livre -- agrava)."
                        .to_string(),
                );
                recs.push(
                    "Identificar o chao de fato compartilhado antes de divergir.".to_string(),
                );
                recs.push(
                    "Rotular taticas polarizantes quando aparecerem (metacognicao assemblear)."
                        .to_string(),
                );
            }
            NivelPolarizacao::Alto | NivelPolarizacao::Critico => {
                recs.push("Mediador profissional obrigatoria (OpenCommunityLeaders).".to_string());
                recs.push("Votacao adiada ate confianca minima restaurada.".to_string());
                recs.push("Deliberacao em sub-grupos mistos (quebra de bloco tribal).".to_string());
                recs.push(
                    "Auditar algoritmos de feed que podem estar amplificando (P8).".to_string(),
                );
            }
            NivelPolarizacao::Ruptura => {
                recs.push("EMERGENCIA: assembleia em pausa. Nao votar.".to_string());
                recs.push(
                    "Restaurar chao de fato: comissao de verificacao (HumanKnowledge).".to_string(),
                );
                recs.push(
                    "Dialogo individual antes de coletivo (quebra de tribalismo).".to_string(),
                );
                recs.push(
                    "Investigar captura narrativa externa (algoritmo, ator malicioso).".to_string(),
                );
                recs.push(
                    "Considerar OpenWololo se a divisao for irreparavel (separar, nao subjugar)."
                        .to_string(),
                );
            }
        }
        recs
    }

    // -- scorecard ---------------------------------------------------------

    pub fn scorecard(&mut self) -> HashMap<String, i32> {
        let blocos = self.detectar_blocos(3);
        let mut bloqueadas = 0;
        let mut aprovadas = 0;
        for a in self.auditorias.values() {
            if a.veredito == VereditoAuditoria::Bloqueada {
                bloqueadas += 1;
            }
            if a.veredito == VereditoAuditoria::Aprovada
                || a.veredito == VereditoAuditoria::AprovadaComRessalvas
            {
                aprovadas += 1;
            }
        }
        let mut sc = HashMap::new();
        sc.insert(
            "propostas_registradas".to_string(),
            self.propostas.len() as i32,
        );
        sc.insert("votos_registrados".to_string(), self.votos.len() as i32);
        let cid_ativos = self
            .votos
            .iter()
            .map(|v| v.cidadao_id.clone())
            .collect::<HashSet<_>>()
            .len() as i32;
        sc.insert("cidadaos_ativos".to_string(), cid_ativos);
        sc.insert("blocos_detectados".to_string(), blocos.len() as i32);
        sc.insert(
            "indice_divisao".to_string(),
            (self.indice_divisao() * 1000.0) as i32,
        );
        sc.insert(
            "indice_tribalismo".to_string(),
            (self.indice_tribalismo() * 1000.0) as i32,
        );
        sc.insert(
            "politicas_auditadas".to_string(),
            self.auditorias.len() as i32,
        );
        sc.insert("politicas_bloqueadas".to_string(), bloqueadas);
        sc.insert("politicas_aprovadas".to_string(), aprovadas);
        sc
    }
}

// ============================================================================
// 5. DEMO (fn main equivalente)
// ============================================================================

fn main() {
    let mut e = AntiPolarizacaoEngine::new();

    println!("{}", "=".repeat(70));
    println!("OpenAntiPolarization -- P9: O Estado NAO Polariza");
    println!("{}", "=".repeat(70));

    // --- Cenario 1: assembleia saudavel ---
    println!("\n[CENARIO 1] Assembleia saudavel (dissenso produtivo)");
    let p1 = e.registrar_proposta(
        "Construir escola no norte",
        "",
        Some(FatorPolarizacao::Regiao),
    );
    let p2 = e.registrar_proposta("Ampliar enfermaria central", "", None);
    let p3 = e.registrar_proposta("Importar capoeira como educacao fisica", "", None);

    let votacoes1 = vec![
        ("cid_01".to_string(), p1.id.clone(), true),
        ("cid_02".to_string(), p1.id.clone(), true),
        ("cid_03".to_string(), p1.id.clone(), false),
        ("cid_04".to_string(), p1.id.clone(), true),
        ("cid_05".to_string(), p1.id.clone(), true),
        ("cid_01".to_string(), p2.id.clone(), true),
        ("cid_02".to_string(), p2.id.clone(), false),
        ("cid_03".to_string(), p2.id.clone(), true),
        ("cid_04".to_string(), p2.id.clone(), true),
        ("cid_05".to_string(), p2.id.clone(), true),
        ("cid_01".to_string(), p3.id.clone(), false),
        ("cid_02".to_string(), p3.id.clone(), true),
        ("cid_03".to_string(), p3.id.clone(), true),
        ("cid_04".to_string(), p3.id.clone(), false),
        ("cid_05".to_string(), p3.id.clone(), true),
    ];
    e.registrar_votacao_em_lote(&votacoes1);

    let m1 = e.medir_polarizacao("assembleia_norte_v1", None);
    println!(
        "  Divisao: {:.2} | Tribalismo: {:.2}",
        m1.indice_divisao, m1.indice_tribalismo
    );
    println!("  Nivel: {}", m1.nivel.rotulo());
    println!("  Veredito: {}", m1.veredito);
    println!("  Protocolo: {}", e.protocolo_bloqueio(&m1).rotulo());

    // --- Cenario 2: assembleia polarizada ---
    println!("\n[CENARIO 2] Assembleia polarizada (votacao tribal)");
    let mut e2 = AntiPolarizacaoEngine::new();
    let pa = e2.registrar_proposta("Politica A", "", Some(FatorPolarizacao::Ideologia));
    let pb = e2.registrar_proposta("Politica B", "", Some(FatorPolarizacao::Ideologia));
    let pc = e2.registrar_proposta("Politica C", "", Some(FatorPolarizacao::Ideologia));
    let pd = e2.registrar_proposta("Politica D", "", Some(FatorPolarizacao::Ideologia));

    let bloco_x: Vec<String> = (0..5).map(|i| format!("x_{:02}", i)).collect();
    let bloco_y: Vec<String> = (0..5).map(|i| format!("y_{:02}", i)).collect();

    for prop in [&pa, &pb, &pc, &pd] {
        for cid in &bloco_x {
            e2.registrar_voto(cid, &prop.id, true, "");
        }
        for cid in &bloco_y {
            e2.registrar_voto(cid, &prop.id, false, "");
        }
    }

    let sinais2 = vec!["voto_identidade".to_string(), "zero_trust".to_string()];
    let m2 = e2.medir_polarizacao("assembleia_polarizada", Some(&sinais2));
    println!(
        "  Divisao: {:.2} | Tribalismo: {:.2}",
        m2.indice_divisao, m2.indice_tribalismo
    );
    println!("  Ruptura epistemica: {:.2}", m2.indice_ruptura_epistemica);
    println!("  Nivel: {}", m2.nivel.rotulo());
    println!("  Veredito: {}", m2.veredito);
    println!("  Protocolo: {}", e2.protocolo_bloqueio(&m2).rotulo());
    println!("  Blocos detectados: {}", m2.num_blocos);
    println!("  Recomendacoes:");
    for r in e2.recomendacoes_mediacao(&m2) {
        println!("    - {}", r);
    }

    // --- Cenario 3: ruptura epistemica ---
    println!("\n[CENARIO 3] Ruptura epistemica (EMERGENCIA)");
    let mut e3 = AntiPolarizacaoEngine::new();
    for i in 0..5 {
        e3.registrar_proposta(&format!("Proposta {}", i), "", None);
    }
    let todos_sinais: Vec<String> = sinais_ruptura_epistemica()
        .keys()
        .map(|k| k.to_string())
        .collect();

    let prop_ids: Vec<String> = e3.propostas.keys().cloned().collect();
    for pid in prop_ids {
        for j in 0..6 {
            e3.registrar_voto(&format!("tribo_a_{}", j), &pid, true, "");
            e3.registrar_voto(&format!("tribo_b_{}", j), &pid, false, "");
        }
    }

    let m3 = e3.medir_polarizacao("assembleia_ruptura", Some(&todos_sinais));
    println!("  Ruptura epistemica: {:.2}", m3.indice_ruptura_epistemica);
    println!("  Nivel: {}", m3.nivel.rotulo());
    println!("  Protocolo: {}", e3.protocolo_bloqueio(&m3).rotulo());
    println!("  RECOMENDACOES DE EMERGENCIA:");
    for r in e3.recomendacoes_mediacao(&m3) {
        println!("    - {}", r);
    }

    // --- GATE P9: auditoria de politicas ---
    println!("\n{}", "=".repeat(70));
    println!("[GATE P9] Auditoria de politicas publicas");
    println!("{}", "=".repeat(70));

    let a1 = e.auditar_politica(
        "pol-escola",
        "Construir escola no norte",
        "Politica de infraestrutura educacional sem apelo identitario.",
        &[],
        &[FatorPolarizacao::Regiao],
        None,
    );
    println!(
        "\n  [{}] {} (score={})",
        a1.politica_id,
        a1.veredito.rotulo(),
        a1.score_polarizante
    );
    println!("    {}", a1.justificativa);

    let a2 = e.auditar_politica(
        "pol-saude",
        "Reforma do sistema de saude",
        "Politica com algum alarmismo na apresentacao.",
        &[TaticaPolarizante::FearMongering],
        &[],
        None,
    );
    println!(
        "\n  [{}] {} (score={})",
        a2.politica_id,
        a2.veredito.rotulo(),
        a2.score_polarizante
    );
    println!("    {}", a2.justificativa);
    for mit in &a2.mitigacoes {
        println!("    Mitigacao: {}", mit);
    }

    let a3 = e.auditar_politica(
        "pol-seguranca",
        "Lei de seguranca publica",
        "Politica apresentada com falsa dicotomia e alarmismo.",
        &[
            TaticaPolarizante::FalseDichotomy,
            TaticaPolarizante::FearMongering,
        ],
        &[FatorPolarizacao::Ideologia],
        None,
    );
    println!(
        "\n  [{}] {} (score={})",
        a3.politica_id,
        a3.veredito.rotulo(),
        a3.score_polarizante
    );
    println!("    {}", a3.justificativa);
    for mit in &a3.mitigacoes {
        println!("    Mitigacao: {}", mit);
    }

    let a4 = e.auditar_politica(
        "pol-identidade",
        "Declaracao sobre valores culturais",
        "Politica que aciona divisao religiosa e identitaria explicita.",
        &[
            TaticaPolarizante::IdentityBaiting,
            TaticaPolarizante::OutgroupDehumanization,
            TaticaPolarizante::EpistemicBalkanization,
        ],
        &[FatorPolarizacao::Religiao, FatorPolarizacao::Identidade],
        Some(&["zero_trust".to_string(), "purity_test".to_string()]),
    );
    println!(
        "\n  [{}] {} (score={})",
        a4.politica_id,
        a4.veredito.rotulo(),
        a4.score_polarizante
    );
    println!("    {}", a4.justificativa);
    for mit in &a4.mitigacoes {
        println!("    Mitigacao: {}", mit);
    }

    // --- Scorecard ---
    println!("\n{}", "=".repeat(70));
    println!("[SCORECARD P9]");
    println!("{}", "=".repeat(70));
    let sc = e.scorecard();
    for (k, v) in &sc {
        println!("  {:.<28} {}", k, v);
    }

    // --- Catalogo de taticas ---
    println!("\n[CATALOGO DE TATICAS POLARIZANTES AUDITADAS PELO ESTADO]");
    for t in [
        TaticaPolarizante::OutgroupDehumanization,
        TaticaPolarizante::FalseDichotomy,
        TaticaPolarizante::Whataboutism,
        TaticaPolarizante::FearMongering,
        TaticaPolarizante::IdentityBaiting,
        TaticaPolarizante::EpistemicBalkanization,
        TaticaPolarizante::BothSidesFallacy,
        TaticaPolarizante::Strawman,
        TaticaPolarizante::DogWhistle,
        TaticaPolarizante::VirtueSignaling,
    ] {
        println!("  [{}] {}", t.gravidade(), t.rotulo());
    }

    // --- Sinais de ruptura epistemica ---
    println!("\n[SINAIS DE RUPTURA EPISTEMICA (monitoramento continuo)]");
    for (chave, desc) in sinais_ruptura_epistemica() {
        println!("  {}: {}", chave, desc);
    }

    // --- FILOSOFIA ---
    println!("\n{}", "=".repeat(70));
    println!("FILOSOFIA -- P9: Por que o Estado nao pode polarizar");
    println!("{}", "=".repeat(70));
    println!(
        r#"
DISTINCAO FUNDAMENTAL:
  Diversidade de opiniao e DIREITO (P2). E saudavel. E combustivel da democracia.
  Polarizacao e DOENCA. Nao e "opiniao diferente". E realidade epistemica
  separada: duas tribos que nao so discordam, mas habitam mundos de fato
  diferentes, com zero confianca mutua e identidade fundida na tribo.

O ERRO LIBERAL:
  O liberalismo assume que "mais debate resolve polarizacao". Falso.
  Mais debate entre tribos epistemicamente separadas AMPLIFICA a polarizacao.
  O que resolve: (a) chao de fato compartilhado, (b) deliberacao estruturada,
  (c) Estado que se recusa a ser vetor de divisao identitaria.

POR QUE O ESTADO ESPECIFICAMENTE:
  O Estado tem monopolio da forca coercitiva. Se o Estado polariza, ele nao
  so reflete a divisao -- ele a INSTITUCIONALIZA. Politica publica que aciona
  tribo vira lei. Lei que aciona tribo perpertua a divisao por geracoes.
  P9 e a proibicao constitucional de o Estado ser vetor de divisao.

P9 NAO E CENSURA:
  P9 nao proibe discurso (isso violaria P2). P9 obriga o ESTADO a auditar
  suas proprias politicas quanto ao efeito polarizante. E um gate, como WCAG
  audita acessibilidade. Cidadao pode dizer o que quiser. O Estado nao pode
  GOVERNAR com divisao identitaria.

A CONEXAO COM P8 (IA):
  Algoritmos de feed que otimizam engajamento amplificam furia, nao verdade.
  Isso e a anti-tese do P8 (IA que amplia inteligencia humana). Engagement
  por furia e captura narrativa. P9 exige que o Estado audite algoritmos
  que afetam a assembleia -- nao para censurar, mas para nao ser capturado.

A UNICA SAIDA QUANDO A DIVISAO E IRREPARAVEL:
  Se duas comunidades habitam realidades epistemicas irrecuperavelmente
  separadas, a Republica nao as obriga a coexistir sob a mesma lei (isso
  recriaria coercicao). OpenWololo permite separar com dignidade -- duas
  assembleias, dois territorios, zero subordinacao. Melhor separar do que
  subjugar. Mas P9 trabalha para que isso seja ultimo recurso, nao rotina.
"#
    );
}
