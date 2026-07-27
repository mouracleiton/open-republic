// OpenAgrarianRevolution -- A Terra e de Quem a Cuida
// =====================================================
// A Revolucao Agraria da Republica Aberta vai alem da "reforma agraria" classica.
// Nao redistribui propriedade. ABOLI a propriedade da terra como mercadoria.
// A terra nao se compra, nao se vende, nao se herda, nao se acumula.
// A terra se CUIDA. Quem cuida, colhe o fruto. Quem abandona, devolve.
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1 (Anti-elitismo): Latifundio = mecanismo original de elite. Concentrar
//   terra = concentrar vida. A Republica extingue a raiz da desigualdade rural.
// - P2 (Autonomia corporal): Quem trabalha a terra tem direito ao fruto do
//   trabalho. Ninguem morre de fome cercando terra que nao cultiva.
// - P3 (Trabalho igual): Crislto vem de IMPACTO (alimentar gente), nao de
//   aluguel de terra. Latifundio improdutivo = roubo sistêmico.
// - P4 (Democracia radical): Assembleia local decide o uso da terra. Nao
//   existe "dono". Existe GUARDIAO com mandato revogavel.
//
// OS 5 PILARES DA REVOLUCAO AGRARIA:
// 1. ABOLICAO da propriedade privada da terra (ninguem "possui" hectares)
// 2. GUARDIAO em vez de dono (quem cultiva cuida, mandato revogavel)
// 3. FUNCAO SOCIAL obrigatoria (terra ociosa = devolvida)
// 4. COOPERATIVISMO (nenhuma familia sozinha; mutirao como padrao)
// 5. AGROLOGIA (agricultura que regenera o solo, nao que o exaure)
//
// Author: OpenRepublic Team

use std::collections::HashMap;

#[derive(Debug, Clone, PartialEq)]
pub enum TipoTenencia {
    GuardiaoFamiliar,
    Cooperativa,
    ComunidadeTradicional,
    AssentamentoColetivo,
    ReservaRegeneracao,
    UsoPublico,
}

impl TipoTenencia {
    pub fn id(&self) -> &str {
        match self {
            TipoTenencia::GuardiaoFamiliar => "guardiao_familiar",
            TipoTenencia::Cooperativa => "cooperativa",
            TipoTenencia::ComunidadeTradicional => "comunidade_tradicional",
            TipoTenencia::AssentamentoColetivo => "assentamento_coletivo",
            TipoTenencia::ReservaRegeneracao => "reserva_regeneracao",
            TipoTenencia::UsoPublico => "uso_publico",
        }
    }
    pub fn rotulo(&self) -> &str {
        match self {
            TipoTenencia::GuardiaoFamiliar => "Guardiao familiar",
            TipoTenencia::Cooperativa => "Cooperativa agricola",
            TipoTenencia::ComunidadeTradicional => "Comunidade tradicional (quilombo/ribeirinho/aldeia)",
            TipoTenencia::AssentamentoColetivo => "Assentamento coletivo da Republica",
            TipoTenencia::ReservaRegeneracao => "Reserva de regeneracao do solo (repouso)",
            TipoTenencia::UsoPublico => "Uso publico (escola, enfermaria, mercado)",
        }
    }
    pub fn familias_max(&self) -> i32 {
        match self {
            TipoTenencia::GuardiaoFamiliar => 1,
            TipoTenencia::Cooperativa => 5,
            TipoTenencia::ComunidadeTradicional => 10,
            TipoTenencia::AssentamentoColetivo => 8,
            TipoTenencia::ReservaRegeneracao => 0,
            TipoTenencia::UsoPublico => 0,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum UsoSolo {
    LavouraAlimentacao,
    LavouraDiversificada,
    PastagemRegenerativa,
    Agrofloresta,
    HortaComunitaria,
    Pomar,
    ReservaNativa,
    CulturaTradicional,
    Infraestrutura,
    Ocioso,
}

impl UsoSolo {
    pub fn id(&self) -> &str {
        match self {
            UsoSolo::LavouraAlimentacao => "lavoura_alimentacao",
            UsoSolo::LavouraDiversificada => "lavoura_diversificada",
            UsoSolo::PastagemRegenerativa => "pastagem_regenerativa",
            UsoSolo::Agrofloresta => "agrofloresta",
            UsoSolo::HortaComunitaria => "horta_comunitaria",
            UsoSolo::Pomar => "pomar",
            UsoSolo::ReservaNativa => "reserva_nativa",
            UsoSolo::CulturaTradicional => "cultura_tradicional",
            UsoSolo::Infraestrutura => "infraestrutura",
            UsoSolo::Ocioso => "ocioso",
        }
    }
    pub fn rotulo(&self) -> &str {
        match self {
            UsoSolo::LavouraAlimentacao => "Lavoura de alimentos basicos",
            UsoSolo::LavouraDiversificada => "Policultivo diversificado",
            UsoSolo::PastagemRegenerativa => "Pastagem rotativa regenerativa",
            UsoSolo::Agrofloresta => "Sistema agroflorestal (SAF)",
            UsoSolo::HortaComunitaria => "Horta comunitaria de bairro",
            UsoSolo::Pomar => "Pomar frutifero",
            UsoSolo::ReservaNativa => "Reserva de vegetacao nativa",
            UsoSolo::CulturaTradicional => "Cultivo tradicional ancestral",
            UsoSolo::Infraestrutura => "Infraestrutura (casa, galpao, escola)",
            UsoSolo::Ocioso => "Ocioso (sem funcao social)",
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum StatusReforma {
    Diagnostico,
    Notificacao,
    Desapropriacao,
    Assentamento,
    Regularizacao,
    Consolidado,
    Conflito,
}

impl StatusReforma {
    pub fn id(&self) -> &str {
        match self {
            StatusReforma::Diagnostico => "diagnostico",
            StatusReforma::Notificacao => "notificacao",
            StatusReforma::Desapropriacao => "desapropriacao",
            StatusReforma::Assentamento => "assentamento",
            StatusReforma::Regularizacao => "regularizacao",
            StatusReforma::Consolidado => "consolidado",
            StatusReforma::Conflito => "conflito",
        }
    }
    pub fn rotulo(&self) -> &str {
        match self {
            StatusReforma::Diagnostico => "Diagnostico fundiario em curso",
            StatusReforma::Notificacao => "Latifundio notificado (funcao social cobrada)",
            StatusReforma::Desapropriacao => "Desapropriacao decidida em assembleia",
            StatusReforma::Assentamento => "Familias assentadas como guardias",
            StatusReforma::Regularizacao => "Regularizacao cooperativa ativa",
            StatusReforma::Consolidado => "Territorio consolidado (auto-gestionario)",
            StatusReforma::Conflito => "Conflito fundiario ativo (grileiro/invasao)",
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum TipoConflito {
    Grilagem,
    InvasaoLatifundio,
    TrabalhoEscravo,
    Despejo,
    ConflitoFronteira,
    MineracaoIlegal,
    Agrotoxico,
    QueimadaCriminosa,
}

impl TipoConflito {
    pub fn id(&self) -> &str {
        match self {
            TipoConflito::Grilagem => "grilagem",
            TipoConflito::InvasaoLatifundio => "invasao_latifundio",
            TipoConflito::TrabalhoEscravo => "trabalho_escravo",
            TipoConflito::Despejo => "despejo",
            TipoConflito::ConflitoFronteira => "conflito_fronteira",
            TipoConflito::MineracaoIlegal => "mineracao_ilegal",
            TipoConflito::Agrotoxico => "agrotoxico",
            TipoConflito::QueimadaCriminosa => "queimada_criminosa",
        }
    }
    pub fn rotulo(&self) -> &str {
        match self {
            TipoConflito::Grilagem => "Grilagem (falsificacao de titulo)",
            TipoConflito::InvasaoLatifundio => "Trabalhador expulso por latifundio",
            TipoConflito::TrabalhoEscravo => "Trabalho analogo a escravidao",
            TipoConflito::Despejo => "Despejo de familia guardi",
            TipoConflito::ConflitoFronteira => "Disputa de fronteira entre comunidades",
            TipoConflito::MineracaoIlegal => "Mineracao/predacao ilegal em terra guardia",
            TipoConflito::Agrotoxico => "Contaminacao por agrotoxico vizinho",
            TipoConflito::QueimadaCriminosa => "Queimada criminosa / desmatamento",
        }
    }
    pub fn gravidade(&self) -> i32 {
        match self {
            TipoConflito::Grilagem => 4,
            TipoConflito::InvasaoLatifundio => 5,
            TipoConflito::TrabalhoEscravo => 5,
            TipoConflito::Despejo => 4,
            TipoConflito::ConflitoFronteira => 2,
            TipoConflito::MineracaoIlegal => 4,
            TipoConflito::Agrotoxico => 3,
            TipoConflito::QueimadaCriminosa => 4,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum TamanhoImovel {
    Minifundio,
    Pequeno,
    Medio,
    LatifundioDimensao,
    LatifundioExploracao,
}

impl TamanhoImovel {
    pub fn id(&self) -> &str {
        match self {
            TamanhoImovel::Minifundio => "minifundio",
            TamanhoImovel::Pequeno => "pequeno",
            TamanhoImovel::Medio => "medio",
            TamanhoImovel::LatifundioDimensao => "latifundio_dimensao",
            TamanhoImovel::LatifundioExploracao => "latifundio_exploracao",
        }
    }
    pub fn rotulo(&self) -> &str {
        match self {
            TamanhoImovel::Minifundio => "Minifundio (insuficiente, < 1 modulo)",
            TamanhoImovel::Pequeno => "Pequena area (1-4 modulos)",
            TamanhoImovel::Medio => "Media area (4-15 modulos)",
            TamanhoImovel::LatifundioDimensao => "Latifundio por dimensao (>15 modulos)",
            TamanhoImovel::LatifundioExploracao => "Latifundio por exploracao (ocioso/grilado)",
        }
    }
    pub fn area_min(&self) -> f64 {
        match self {
            TamanhoImovel::Minifundio => 0.0,
            TamanhoImovel::Pequeno => 50.0,
            TamanhoImovel::Medio => 200.0,
            TamanhoImovel::LatifundioDimensao => 750.0,
            TamanhoImovel::LatifundioExploracao => 0.0,
        }
    }
    pub fn area_max(&self) -> f64 {
        match self {
            TamanhoImovel::Minifundio => 50.0,
            TamanhoImovel::Pequeno => 200.0,
            TamanhoImovel::Medio => 750.0,
            TamanhoImovel::LatifundioDimensao => 99999.0,
            TamanhoImovel::LatifundioExploracao => 99999.0,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum FuncaoSocialStatus {
    Cumpre,
    Parcial,
    Descumpre,
}

impl FuncaoSocialStatus {
    pub fn rotulo(&self) -> &str {
        match self {
            FuncaoSocialStatus::Cumpre => "Cumpre funcao social",
            FuncaoSocialStatus::Parcial => "Cumpre parcialmente",
            FuncaoSocialStatus::Descumpre => "Descumpre funcao social",
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum PlanoAgrologia {
    PlantioDireto,
    AdubacaoVerde,
    Compostagem,
    RotacaoCulturas,
    CicloFechado,
    AgroflorestaSucessional,
    CaptacaoChuva,
    Bioinsumos,
    IntegracaoAnimal,
}

impl PlanoAgrologia {
    pub fn id(&self) -> &str {
        match self {
            PlanoAgrologia::PlantioDireto => "plantio_direto",
            PlanoAgrologia::AdubacaoVerde => "adubacao_verde",
            PlanoAgrologia::Compostagem => "compostagem",
            PlanoAgrologia::RotacaoCulturas => "rotacao_culturas",
            PlanoAgrologia::CicloFechado => "ciclo_fechado",
            PlanoAgrologia::AgroflorestaSucessional => "agrofloresta_sucessional",
            PlanoAgrologia::CaptacaoChuva => "captacao_chuva",
            PlanoAgrologia::Bioinsumos => "bioinsumos",
            PlanoAgrologia::IntegracaoAnimal => "integracao_animal",
        }
    }
    pub fn rotulo(&self) -> &str {
        match self {
            PlanoAgrologia::PlantioDireto => "Plantio direto (nao revolver solo)",
            PlanoAgrologia::AdubacaoVerde => "Adubacao verde (leguminosas)",
            PlanoAgrologia::Compostagem => "Compostagem comunitaria",
            PlanoAgrologia::RotacaoCulturas => "Rotacao de culturas",
            PlanoAgrologia::CicloFechado => "Ciclo fechado (zero insumo externo)",
            PlanoAgrologia::AgroflorestaSucessional => "Agrofloresta sucessional",
            PlanoAgrologia::CaptacaoChuva => "Captacao de agua de chuva",
            PlanoAgrologia::Bioinsumos => "Bioinsumos (proibido agrotoxico sintetico)",
            PlanoAgrologia::IntegracaoAnimal => "Integracao lavoura-pecuaria-floresta",
        }
    }
}

// ============================================================================
// 2. STRUCTS (dataclasses)
// ============================================================================

#[derive(Debug, Clone)]
pub struct ImovelRural {
    pub id: String,
    pub nome: String,
    pub area_hectares: f64,
    pub municipio: String,
    pub bioma: String,
    pub tipo_tenencia: TipoTenencia,
    pub usos_solo: Vec<UsoSolo>,
    pub familias_guardias: i32,
    pub funcao_social: FuncaoSocialStatus,
    pub produtividade_pct: f64,
    pub plano_agrologia: Vec<PlanoAgrologia>,
    pub status: StatusReforma,
    pub historico_antigo: String,
}

#[derive(Debug, Clone)]
pub struct FamiliaGuardia {
    pub id: String,
    pub nome_referencia: String,
    pub pessoas: i32,
    pub parcela_hectares: f64,
    pub cooperativa_id: Option<String>,
    pub chegada_de: String,
    pub conhecimento_tradicional: bool,
}

#[derive(Debug, Clone)]
pub struct ConflitoFundiario {
    pub id: String,
    pub tipo: TipoConflito,
    pub territorio_id: String,
    pub vitimas: i32,
    pub familias_afetadas: i32,
    pub descricao: String,
    pub resolucao_proposta: String,
    pub resolvido: bool,
}

#[derive(Debug, Clone)]
pub struct CooperativaAgricola {
    pub id: String,
    pub nome: String,
    pub familia_ids: Vec<String>,
    pub territorio_ids: Vec<String>,
    pub excedente_destino: String,
    pub ferramentas_compartilhadas: Vec<String>,
}

#[derive(Debug, Clone)]
pub struct DiagnosticoFundiario {
    pub territorio: String,
    pub total_area: f64,
    pub num_imoveis: i32,
    pub indice_gini: f64,
    pub pct_area_latifundio: f64,
    pub familias_sem_terra: i32,
    pub familias_guardias: i32,
    pub veredito: String,
}

// ============================================================================
// 3. ENGINE
// ============================================================================

pub struct ReformaAgrariaEngine {
    pub imoveis: HashMap<String, ImovelRural>,
    pub familias: HashMap<String, FamiliaGuardia>,
    pub cooperativas: HashMap<String, CooperativaAgricola>,
    pub conflitos: HashMap<String, ConflitoFundiario>,
    _im_id: i32,
    _fam_id: i32,
    _coop_counter: i32,
    _conf_id: i32,
}

impl ReformaAgrariaEngine {
    pub fn new() -> Self {
        ReformaAgrariaEngine {
            imoveis: HashMap::new(),
            familias: HashMap::new(),
            cooperativas: HashMap::new(),
            conflitos: HashMap::new(),
            _im_id: 0,
            _fam_id: 0,
            _coop_counter: 0,
            _conf_id: 0,
        }
    }

    // -- cadastro ----------------------------------------------------------

    fn _imovel_id(&mut self) -> String {
        self._im_id += 1;
        format!("TER-{:04}", self._im_id)
    }

    fn _familia_id(&mut self) -> String {
        self._fam_id += 1;
        format!("FAM-{:04}", self._fam_id)
    }

    fn _coop_id(&mut self) -> String {
        self._coop_counter += 1;
        format!("COOP-{:04}", self._coop_counter)
    }

    fn _conflito_id(&mut self) -> String {
        self._conf_id += 1;
        format!("CONF-{:04}", self._conf_id)
    }

    pub fn cadastrar_imovel(
        &mut self,
        nome: &str,
        area_hectares: f64,
        municipio: &str,
        bioma: &str,
        tipo_tenencia: TipoTenencia,
        usos_solo: Option<Vec<UsoSolo>>,
        familias_guardias: i32,
        funcao_social: FuncaoSocialStatus,
        produtividade_pct: f64,
        plano: Option<Vec<PlanoAgrologia>>,
        status: StatusReforma,
        historico_antigo: &str,
    ) -> String {
        let id = self._imovel_id();
        let im = ImovelRural {
            id: id.clone(),
            nome: nome.to_string(),
            area_hectares,
            municipio: municipio.to_string(),
            bioma: bioma.to_string(),
            tipo_tenencia,
            usos_solo: usos_solo.unwrap_or_default(),
            familias_guardias,
            funcao_social,
            produtividade_pct,
            plano_agrologia: plano.unwrap_or_default(),
            status,
            historico_antigo: historico_antigo.to_string(),
        };
        self.imoveis.insert(id.clone(), im);
        id
    }

    pub fn cadastrar_familia(
        &mut self,
        nome_referencia: &str,
        pessoas: i32,
        parcela_hectares: f64,
        cooperativa_id: Option<String>,
        chegada_de: &str,
        conhecimento_tradicional: bool,
    ) -> String {
        let id = self._familia_id();
        let f = FamiliaGuardia {
            id: id.clone(),
            nome_referencia: nome_referencia.to_string(),
            pessoas,
            parcela_hectares,
            cooperativa_id,
            chegada_de: chegada_de.to_string(),
            conhecimento_tradicional,
        };
        self.familias.insert(id.clone(), f);
        id
    }

    pub fn criar_cooperativa(
        &mut self,
        nome: &str,
        familia_ids: Vec<String>,
        territorio_ids: Vec<String>,
        excedente_destino: &str,
        ferramentas: Option<Vec<String>>,
    ) -> String {
        let id = self._coop_id();
        let c = CooperativaAgricola {
            id: id.clone(),
            nome: nome.to_string(),
            familia_ids: familia_ids.clone(),
            territorio_ids: territorio_ids.clone(),
            excedente_destino: excedente_destino.to_string(),
            ferramentas_compartilhadas: ferramentas.unwrap_or_default(),
        };
        self.cooperativas.insert(id.clone(), c);
        for fid in &familia_ids {
            if let Some(fam) = self.familias.get_mut(fid) {
                fam.cooperativa_id = Some(id.clone());
            }
        }
        id
    }

    pub fn registrar_conflito(
        &mut self,
        tipo: TipoConflito,
        territorio_id: &str,
        vitimas: i32,
        familias_afetadas: i32,
        descricao: &str,
    ) -> String {
        let id = self._conflito_id();
        let c = ConflitoFundiario {
            id: id.clone(),
            tipo,
            territorio_id: territorio_id.to_string(),
            vitimas,
            familias_afetadas,
            descricao: descricao.to_string(),
            resolucao_proposta: String::new(),
            resolvido: false,
        };
        self.conflitos.insert(id.clone(), c);
        id
    }

    // -- diagnostico -------------------------------------------------------

    pub fn classificar_tamanho(&self, area: f64, ocioso: bool) -> TamanhoImovel {
        if ocioso && area >= TamanhoImovel::Pequeno.area_min() {
            return TamanhoImovel::LatifundioExploracao;
        }
        for t in [
            TamanhoImovel::Minifundio,
            TamanhoImovel::Pequeno,
            TamanhoImovel::Medio,
            TamanhoImovel::LatifundioDimensao,
        ] {
            if t.area_min() <= area && area < t.area_max() {
                return t;
            }
        }
        TamanhoImovel::LatifundioDimensao
    }

    pub fn indice_gini_areas(&self) -> f64 {
        let mut areas: Vec<f64> = self.imoveis.values().map(|im| im.area_hectares).collect();
        areas.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let n = areas.len();
        if n == 0 {
            return 0.0;
        }
        let total: f64 = areas.iter().sum();
        if total == 0.0 {
            return 0.0;
        }
        let mut soma_pond = 0.0;
        for (i, a) in areas.iter().enumerate() {
            soma_pond += (i + 1) as f64 * a;
        }
        let gini = (2.0 * soma_pond) / (n as f64 * total) - (n as f64 + 1.0) / n as f64;
        (gini * 10000.0).round() / 10000.0
    }

    pub fn diagnosticar(&self, territorio: &str) -> DiagnosticoFundiario {
        let ims: Vec<&ImovelRural> = self
            .imoveis
            .values()
            .filter(|im| im.municipio == territorio)
            .collect();
        let total_area: f64 = ims.iter().map(|im| im.area_hectares).sum();
        let num = ims.len() as i32;
        if num == 0 {
            return DiagnosticoFundiario {
                territorio: territorio.to_string(),
                total_area: 0.0,
                num_imoveis: 0,
                indice_gini: 0.0,
                pct_area_latifundio: 0.0,
                familias_sem_terra: 0,
                familias_guardias: 0,
                veredito: "Territorio vazio no cadastro.".to_string(),
            };
        }
        let gini = self.indice_gini_areas();
        let area_lat: f64 = ims
            .iter()
            .filter(|im| {
                let ocioso = im.funcao_social == FuncaoSocialStatus::Descumpre;
                let tam = self.classificar_tamanho(im.area_hectares, ocioso);
                tam == TamanhoImovel::LatifundioDimensao || tam == TamanhoImovel::LatifundioExploracao
            })
            .map(|im| im.area_hectares)
            .sum();
        let pct_lat = if total_area > 0.0 {
            (area_lat / total_area * 100.0).round()
        } else {
            0.0
        };
        let familias_guardias: i32 = ims.iter().map(|im| im.familias_guardias).sum();
        let familias_sem_terra = if familias_guardias > 0 {
            ((pct_lat / 100.0) * familias_guardias as f64 / 4.0).max(0.0) as i32
        } else {
            0
        };
        let veredito = if gini > 0.7 || pct_lat > 50.0 {
            "CONCENTRACAO CRITICA: revolicao agraria URGENTE.".to_string()
        } else if gini > 0.4 || pct_lat > 25.0 {
            "CONCENTRACAO ALTA: notificar latifundios, cobrar funcao social.".to_string()
        } else if gini > 0.2 {
            "CONCENTRACAO MODERADA: regularizar e cooperativizar.".to_string()
        } else {
            "TERRITORIO EQUITATIVO: consolidar cooperativas.".to_string()
        };
        DiagnosticoFundiario {
            territorio: territorio.to_string(),
            total_area,
            num_imoveis: num,
            indice_gini: gini,
            pct_area_latifundio: pct_lat,
            familias_sem_terra,
            familias_guardias,
            veredito,
        }
    }

    // -- funcao social -----------------------------------------------------

    pub fn auditar_funcao_social(&mut self, imovel_id: &str) -> (FuncaoSocialStatus, Vec<String>) {
        if let Some(im) = self.imoveis.get_mut(imovel_id) {
            let mut faltas: Vec<String> = Vec::new();
            if im.produtividade_pct < 40.0 {
                faltas.push(format!("Produtividade baixa ({:.0}% do potencial).", im.produtividade_pct));
            }
            if im.plano_agrologia.is_empty() {
                faltas.push("Sem plano de agrologia (solo sendo exaurido).".to_string());
            }
            for conf in self.conflitos.values() {
                if conf.tipo == TipoConflito::TrabalhoEscravo
                    && conf.territorio_id == im.id
                    && !conf.resolvido
                {
                    faltas.push("Trabalho analogo a escravidao detectado (BLOQUEANTE).".to_string());
                    break;
                }
            }
            if im.familias_guardias == 0 && im.tipo_tenencia != TipoTenencia::ReservaRegeneracao {
                faltas.push("Nenhuma familia guardia: terra abandonada.".to_string());
            }
            if !faltas.is_empty() {
                im.funcao_social = if faltas.len() == 1 {
                    FuncaoSocialStatus::Parcial
                } else {
                    FuncaoSocialStatus::Descumpre
                };
            } else {
                im.funcao_social = FuncaoSocialStatus::Cumpre;
            }
            (im.funcao_social.clone(), faltas)
        } else {
            (FuncaoSocialStatus::Descumpre, vec!["Imovel nao encontrado.".to_string()])
        }
    }

    // -- revolucao (pipeline) ----------------------------------------------

    pub fn notificar_latifundio(&mut self, imovel_id: &str) -> Option<String> {
        let im = self.imoveis.get(imovel_id)?;
        let ocioso = im.funcao_social == FuncaoSocialStatus::Descumpre;
        let tam = self.classificar_tamanho(im.area_hectares, ocioso);
        if tam != TamanhoImovel::LatifundioDimensao && tam != TamanhoImovel::LatifundioExploracao {
            return Some(format!("{} nao e latifundio ({}).", im.id, tam.rotulo()));
        }
        let (status, faltas) = self.auditar_funcao_social(imovel_id);
        if let Some(im) = self.imoveis.get_mut(imovel_id) {
            if status == FuncaoSocialStatus::Cumpre {
                im.status = StatusReforma::Regularizacao;
                return Some(format!("{} cumpre funcao social -> regularizar como cooperativa.", im.id));
            }
            im.status = StatusReforma::Notificacao;
            let faltas_str = if faltas.is_empty() {
                "none".to_string()
            } else {
                faltas.join("; ")
            };
            Some(format!(
                "NOTIFICADO {} ({}), {:.0} ha). Faltas: {}. Prazo para regularizar.",
                im.id, tam.rotulo(), im.area_hectares, faltas_str
            ))
        } else {
            None
        }
    }

    pub fn desaproropriar(&mut self, imovel_id: &str, familias_assentar: Vec<String>) -> Option<String> {
        let im = self.imoveis.get(imovel_id)?;
        if im.status != StatusReforma::Notificacao && im.status != StatusReforma::Diagnostico {
            return Some(format!(
                "{} em status {} -- nao elegivel para desapropriacao agora.",
                im.id, im.status.rotulo()
            ));
        }
        if let Some(im) = self.imoveis.get_mut(imovel_id) {
            if im.historico_antigo.is_empty() {
                im.historico_antigo = im.nome.clone();
            }
            im.nome = format!("Territorio Livre {}", im.id);
            im.tipo_tenencia = TipoTenencia::AssentamentoColetivo;
            if !familias_assentar.is_empty() {
                let parcela = im.area_hectares / familias_assentar.len() as f64;
                for fid in &familias_assentar {
                    if let Some(fam) = self.familias.get_mut(fid) {
                        fam.parcela_hectares = (parcela * 100.0).round() / 100.0;
                        fam.chegada_de = "assentamento".to_string();
                    }
                }
                im.familias_guardias = familias_assentar.len() as i32;
            }
            im.status = StatusReforma::Assentamento;
            im.funcao_social = FuncaoSocialStatus::Parcial;
            Some(format!(
                "DESAPROPRIVADO {}: {} familias guardias assentadas, {:.0} ha sob cuidado coletivo.",
                im.id, familias_assentar.len(), im.area_hectares
            ))
        } else {
            None
        }
    }

    pub fn consolidar_cooperativa(
        &mut self,
        nome: &str,
        territorio_ids: Vec<String>,
        familias_ids: Vec<String>,
        excedente: &str,
        ferramentas: Option<Vec<String>>,
    ) -> String {
        let coop_id = self.criar_cooperativa(nome, familias_ids, territorio_ids.clone(), excedente, ferramentas);
        for tid in &territorio_ids {
            if let Some(im) = self.imoveis.get_mut(tid) {
                im.tipo_tenencia = TipoTenencia::Cooperativa;
                im.status = StatusReforma::Consolidado;
                im.funcao_social = FuncaoSocialStatus::Cumpre;
            }
        }
        coop_id
    }

    // -- resolucao de conflitos --------------------------------------------

    pub fn conflitos_por_gravidade(&self) -> Vec<&ConflitoFundiario> {
        let mut list: Vec<&ConflitoFundiario> = self.conflitos.values().collect();
        list.sort_by(|a, b| {
            let ga = a.tipo.gravidade();
            let gb = b.tipo.gravidade();
            gb.cmp(&ga).then_with(|| b.familias_afetadas.cmp(&a.familias_afetadas))
        });
        list
    }

    pub fn resolver_conflito(&mut self, conflito_id: &str, resolucao: &str) -> bool {
        if let Some(c) = self.conflitos.get_mut(conflito_id) {
            c.resolucao_proposta = resolucao.to_string();
            c.resolvido = true;
            true
        } else {
            false
        }
    }

    // -- metricas ----------------------------------------------------------

    pub fn area_total(&self) -> f64 {
        self.imoveis.values().map(|im| im.area_hectares).sum()
    }

    pub fn area_ociosa(&self) -> f64 {
        self.imoveis
            .values()
            .filter(|im| im.funcao_social == FuncaoSocialStatus::Descumpre)
            .map(|im| im.area_hectares)
            .sum()
    }

    pub fn familias_atendidas(&self) -> i32 {
        self.imoveis.values().map(|im| im.familias_guardias).sum()
    }

    pub fn pessoas_atendidas(&self) -> i32 {
        self.imoveis.values().map(|im| im.familias_guardias * 4).sum()
    }

    pub fn scorecard(&self) -> HashMap<String, String> {
        let mut sc = HashMap::new();
        sc.insert("imoveis_cadastrados".to_string(), self.imoveis.len().to_string());
        sc.insert("area_total_ha".to_string(), format!("{:.1}", self.area_total()));
        sc.insert("area_ociosa_ha".to_string(), format!("{:.1}", self.area_ociosa()));
        let pct = if self.area_total() > 0.0 {
            (self.area_ociosa() / self.area_total() * 100.0 * 10.0).round() / 10.0
        } else {
            0.0
        };
        sc.insert("pct_ociosa".to_string(), pct.to_string());
        sc.insert("familias_guardias".to_string(), self.familias_atendidas().to_string());
        sc.insert("cooperativas".to_string(), self.cooperativas.len().to_string());
        let conflitos_abertos = self.conflitos.values().filter(|c| !c.resolvido).count();
        sc.insert("conflitos_abertos".to_string(), conflitos_abertos.to_string());
        sc.insert("indice_gini".to_string(), self.indice_gini_areas().to_string());
        let consolidados = self
            .imoveis
            .values()
            .filter(|im| im.status == StatusReforma::Consolidado)
            .count();
        sc.insert("consolidados".to_string(), consolidados.to_string());
        sc
    }
}

// ============================================================================
// 4. DEMO (main equivalent)
// ============================================================================

fn main() {
    let mut e = ReformaAgrariaEngine::new();

    println!("{}", "=".repeat(70));
    println!("OpenAgrarianRevolution -- A Terra e de Quem a Cuida");
    println!("{}", "=".repeat(70));

    // --- Contexto: territorio "Sertao do Sao Francisco" ---
    let latif_id = e.cadastrar_imovel(
        "Fazenda Boa Vista (ex-latifundio)",
        2500.0,
        "Sertao do Sao Francisco",
        "caatinga",
        TipoTenencia::GuardiaoFamiliar,
        Some(vec![UsoSolo::PastagemRegenerativa, UsoSolo::Ocioso]),
        3,
        FuncaoSocialStatus::Descumpre,
        15.0,
        Some(vec![]),
        StatusReforma::Diagnostico,
        "Familia herdeira de titulo duvidoso",
    );

    let pequeno_a_id = e.cadastrar_imovel(
        "Sitio Aconchego",
        30.0,
        "Sertao do Sao Francisco",
        "caatinga",
        TipoTenencia::GuardiaoFamiliar,
        Some(vec![UsoSolo::LavouraAlimentacao, UsoSolo::Pomar]),
        1,
        FuncaoSocialStatus::Parcial,
        70.0,
        Some(vec![PlanoAgrologia::Compostagem, PlanoAgrologia::RotacaoCulturas]),
        StatusReforma::Diagnostico,
        "",
    );

    let reserva_id = e.cadastrar_imovel(
        "Reserva Caatinga Viva",
        800.0,
        "Sertao do Sao Francisco",
        "caatinga",
        TipoTenencia::ReservaRegeneracao,
        Some(vec![UsoSolo::ReservaNativa]),
        0,
        FuncaoSocialStatus::Cumpre,
        0.0,
        Some(vec![PlanoAgrologia::CicloFechado]),
        StatusReforma::Diagnostico,
        "",
    );

    // --- Diagnostico ---
    let diag = e.diagnosticar("Sertao do Sao Francisco");
    println!("\n[DIAGNOSTICO] {}", diag.territorio);
    println!("  Area total: {:.0} ha | Imoveis: {}", diag.total_area, diag.num_imoveis);
    println!("  Indice de Gini: {:.3} (0=igual, 1=concentrado)", diag.indice_gini);
    println!("  % area em latifundios: {:.1}%", diag.pct_area_latifundio);
    println!("  Familias guardias: {}", diag.familias_guardias);
    println!("  VEREDITO: {}", diag.veredito);

    // --- Notificar latifundio ---
    println!("\n[NOTIFICACAO]");
    if let Some(msg) = e.notificar_latifundio(&latif_id) {
        println!("  {}", msg);
    }

    // --- Auditar funcao social ---
    println!("\n[AUDITORIA DE FUNCAO SOCIAL]");
    for iid in [&latif_id, &pequeno_a_id, &reserva_id] {
        let (status, faltas) = e.auditar_funcao_social(iid);
        if let Some(im) = e.imoveis.get(iid) {
            println!("  {} ({}): {}", iid, &im.nome[..im.nome.len().min(30)], status.rotulo());
            for f in &faltas {
                println!("      - {}", f);
            }
        }
    }

    // --- Conflito: trabalho escravo detectado no latifundio ---
    let conflito_id = e.registrar_conflito(
        TipoConflito::TrabalhoEscravo,
        &latif_id,
        2,
        8,
        "Trabalhadores resgatados em condicoes analogas a escravidao.",
    );
    if let Some(conflito) = e.conflitos.get(&conflito_id) {
        println!("\n[CONFLITO REGISTRADO] {}: {}", conflito.id, conflito.tipo.rotulo());
        println!(
            "  Gravidade: {}/5 | Familias afetadas: {}",
            conflito.tipo.gravidade(),
            conflito.familias_afetadas
        );
    }

    // --- Desapropriar: assembleia decide ---
    println!("\n[DESAPROPRIACAO POR ASSEMBLEIA]");
    let fam1 = e.cadastrar_familia("Familia Maria das Dores", 5, 0.0, None, "despejado", false);
    let fam2 = e.cadastrar_familia("Familia Jose Pereira", 4, 0.0, None, "despejado", false);
    let fam3 = e.cadastrar_familia("Familia Ana Beatriz", 6, 0.0, None, "voluntario", false);
    let fam4 = e.cadastrar_familia("Familia Severino", 5, 0.0, None, "despejado", true);
    let fams = vec![fam1, fam2, fam3, fam4];
    if let Some(res) = e.desaproropriar(&latif_id, fams.clone()) {
        println!("  {}", res);
    }

    // Resolver o conflito de trabalho escravo
    e.resolver_conflito(
        &conflito_id,
        "Ex-dono removido; familias guardias assumem; recuperacao das vitimas via OpenPsychologyReparation.",
    );
    if let Some(conflito) = e.conflitos.get(&conflito_id) {
        println!("  Conflito {} resolvido: {}", conflito.id, conflito.resolucao_proposta);
    }

    // --- Consolidar cooperativa ---
    println!("\n[CONSOLIDACAO COOPERATIVA]");
    let coop_id = e.consolidar_cooperativa(
        "Cooperativa Terra Livre Sertao",
        vec![latif_id.clone()],
        fams,
        "mercado_aberto",
        Some(vec!["trator_compartilhado".to_string(), "casa_de_farinha".to_string(), "cisterna_coletiva".to_string()]),
    );
    if let Some(coop) = e.cooperativas.get(&coop_id) {
        println!("  {}: {}", coop.id, coop.nome);
        println!("  Familias: {} | Territorios: {}", coop.familia_ids.len(), coop.territorio_ids.len());
        println!("  Ferramentas compartilhadas: {}", coop.ferramentas_compartilhadas.join(", "));
    }

    // --- Plano de agrologia no novo territorio livre ---
    if let Some(latif) = e.imoveis.get_mut(&latif_id) {
        latif.usos_solo = vec![UsoSolo::Agrofloresta, UsoSolo::LavouraDiversificada, UsoSolo::Pomar];
        latif.plano_agrologia = vec![
            PlanoAgrologia::AgroflorestaSucessional,
            PlanoAgrologia::CaptacaoChuva,
            PlanoAgrologia::Bioinsumos,
            PlanoAgrologia::CicloFechado,
        ];
        latif.produtividade_pct = 65.0;
    }
    let (status_final, _) = e.auditar_funcao_social(&latif_id);
    if let Some(latif) = e.imoveis.get(&latif_id) {
        println!("\n[POS-REVOLUCAO] {} funcao social: {}", latif.id, status_final.rotulo());
        println!("  Status: {} | Tenencia: {}", latif.status.rotulo(), latif.tipo_tenencia.rotulo());
    }

    // --- Scorecard final ---
    println!("\n{}", "=".repeat(70));
    println!("[SCORECARD DA REVOLUCAO AGRARIA]");
    println!("{}", "=".repeat(70));
    let sc = e.scorecard();
    for (k, v) in &sc {
        println!("  {:.<28} {}", k, v);
    }

    // --- Conflitos ordenados por gravidade ---
    println!("\n[CONFLITOS POR GRAVIDADE]");
    for c in e.conflitos_por_gravidade() {
        let flag = if c.resolvido { "OK" } else { "ABERTO" };
        println!(
            "  [{}] {} {} (grav={}) vitimas={} familias={}",
            flag, c.id, c.tipo.rotulo(), c.tipo.gravidade(), c.vitimas, c.familias_afetadas
        );
    }

    // --- FILOSOFIA ---
    println!("\n{}", "=".repeat(70));
    println!("FILOSOFIA -- Por que a Republica ABOLI a propriedade da terra");
    println!("{}", "=".repeat(70));
    println!(
        r#"P1 (Anti-elitismo): O latifundio e o mecanismo ORIGINAL de elite.
   Antes do banco, antes da empresa, antes da midia: a TERRA.
   Quem cerca a terra cerca a VIDA de quem precisa dela pra comer.
   Abolir a propriedade da terra = extirpar a raiz da desigualdade.

P2 (Autonomia): Quem planta colhe. Quem cuida decide.
   Ninguem morre de fome vigiando cerca de terra que nao cultiva.
   O corpo que sua na roca e dono do fruto -- nao de hectares.

P3 (Trabalho = impacto): "Dono de terra" nao e trabalho. E RENDA.
   Renda de propriedade e extrativismo puro: tirar sem botar.
   A Republica so reconhece credito por IMPACTO (alimentar gente).
   Latifundio improdutivo e roubo sistemico, nao "investimento".

P4 (Democracia): A assembleia do territorio decide o uso da terra.
   Nao ha "dono" para negociar as escuras com madeireira/mineradora.
   O guardiao tem MANDATO REVOGAVEL: abandona, devolve.
   Ninguem herda hectares. Herda-se o oficio, nao a propriedade.

A REVOLUCAO AGRARIA NAO E "REFORMA". E ABOLICAO.
Reforma distribui propriedade. Abolicao extingue a categoria.
A terra volta a ser o que sempre foi: CONDICAO DE VIDA,
nao ativo no balanco patrimonial de ninguem."#
    );
}