// OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso
// =========================================================
// A Republica ABOLI a energia como mercadoria.
//
// Assim como a Revolucao Agraria extinguiu a propriedade da terra,
// a Revolucao Energetica extingue o conceito de "conta de luz".
//
// Energia nao se compra. Nao se vende. Nao se mede para cobrar.
// Nao gera divida. Nao corta. Nao raciona por dinheiro.
//
// ENERGIA E DIREITO. PONTO.
//
// PRINCIPIO: "Para todo e qualquer uso."
// A Republica nao pergunta PARA QUE voce precisa de energia.
// Assim como nao pergunta para que voce precisa de ar.
// Energia e condicao de vida moderna: cozinhar, aquecer, iluminar,
// comunicar, curar, estudar, trabalhar, criar.
//
// MAS COMO ISSO FUNCIONA SEM TRAGEDIA DOS COMUNS?
//
// A logica capital diz: se energia e gratis, todo mundo desperdica.
// Falso. A logica capital projeta o COMPORTAMENTO DO CAPITALISTA
// para dentro do cidadao. O capitalista desperdica porque desperdico
// e EXTERNO ao seu lucro. O cidadao da Republica SABE que a energia
// que ele desperdica e a que falta para o vizinho.
//
// A Republica nao resolve abundancia com ESCASSEZ ARTIFICIAL (preco).
// Resolve com GERACAO DISTRIBUIDA: cada comunidade gera a propria energia.
// Quanto mais gera, mais independente. Quanto mais eficiente, mais excedente
// para doar. Eficiencia nao economiza dinheiro -- LIBERTA capacidade.
//
// O UNICO MOMENTO DE ESCASSEZ (e como se resolve):
// Quando geracao nao cobre demanda (seca extrema, falha de infraestrutura),
// a assembleia decide alocacao -- NUNCA o preco. Hospitais e essenciais
// primeiro. Depois, rotacao democratica. Ninguem fica sem energia por dinheiro.
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1: Energia como mercadoria exclui quem nao tem dinheiro. Abolir = anti-elitismo.
// - P2: Autonomia energetica = autonomia corporal (corpo precisa de calor, comida, luz).
// - P3: Trabalho igual, diferenca so por impacto. Consumir energia nao e trabalho.
//   Quem consome mais NAO recebe mais credito por isso.
// - P4: Assembleia decide alocacao em escassez, nao o mercado.
// - P6: Acesso universal = energia e direito, como conhecimento.
//
// Author: OpenRepublic Team

use std::collections::HashMap;
use std::fmt;

// ============================================================================
// 1. ENUMS (modulo-level)
// ============================================================================

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum FonteEnergia {
    Solar,
    Eolica,
    Hidro,
    Geotermica,
    Biomassa,
    Mares,
    Nuclear,
    Fusao,
}

impl FonteEnergia {
    pub fn id(&self) -> &'static str {
        match self {
            FonteEnergia::Solar => "solar",
            FonteEnergia::Eolica => "eolica",
            FonteEnergia::Hidro => "hidro",
            FonteEnergia::Geotermica => "geotermica",
            FonteEnergia::Biomassa => "biomassa",
            FonteEnergia::Mares => "mares",
            FonteEnergia::Nuclear => "nuclear",
            FonteEnergia::Fusao => "fusao",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            FonteEnergia::Solar => "Solar fotovoltaica",
            FonteEnergia::Eolica => "Eolica (vento)",
            FonteEnergia::Hidro => "Hidroeletrica",
            FonteEnergia::Geotermica => "Geotermica",
            FonteEnergia::Biomassa => "Biomassa",
            FonteEnergia::Mares => "Das mars e correntes",
            FonteEnergia::Nuclear => "Nuclear (fissao)",
            FonteEnergia::Fusao => "Fusao nuclear (futura)",
        }
    }

    pub fn renovavel(&self) -> bool {
        match self {
            FonteEnergia::Solar => true,
            FonteEnergia::Eolica => true,
            FonteEnergia::Hidro => true,
            FonteEnergia::Geotermica => true,
            FonteEnergia::Biomassa => true,
            FonteEnergia::Mares => true,
            FonteEnergia::Nuclear => false,
            FonteEnergia::Fusao => true,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoConsumo {
    EssencialVida,
    Saude,
    Comunicacao,
    Educacao,
    Mobilidade,
    ProducaoAlimentos,
    InfraestruturaComum,
    ProducaoBens,
    CulturaLazer,
    PesquisaInovacao,
    ResidencialExcedente,
}

impl TipoConsumo {
    pub fn id(&self) -> &'static str {
        match self {
            TipoConsumo::EssencialVida => "essencial_vida",
            TipoConsumo::Saude => "saude",
            TipoConsumo::Comunicacao => "comunicacao",
            TipoConsumo::Educacao => "educacao",
            TipoConsumo::Mobilidade => "mobilidade",
            TipoConsumo::ProducaoAlimentos => "producao_alimentos",
            TipoConsumo::InfraestruturaComum => "infraestrutura",
            TipoConsumo::ProducaoBens => "producao_bens",
            TipoConsumo::CulturaLazer => "cultura_lazer",
            TipoConsumo::PesquisaInovacao => "pesquisa",
            TipoConsumo::ResidencialExcedente => "residencial_excedente",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoConsumo::EssencialVida => "Essencial a vida (cozinhar, aquecer, iluminar, agua)",
            TipoConsumo::Saude => "Saude (hospitais, clinicas, equipamentos medicos)",
            TipoConsumo::Comunicacao => "Comunicacao (internet, telefone, radio)",
            TipoConsumo::Educacao => "Educacao (escolas, bibliotecas, laboratorios)",
            TipoConsumo::Mobilidade => "Mobilidade (transporte publico, veiculos)",
            TipoConsumo::ProducaoAlimentos => "Producao de alimentos (irrigacao, processamento)",
            TipoConsumo::InfraestruturaComum => {
                "Infraestrutura comum (agua, esgoto, iluminacao publica)"
            }
            TipoConsumo::ProducaoBens => "Producao de bens (fabril, artesanal)",
            TipoConsumo::CulturaLazer => "Cultura e lazer (teatro, musica, esporte)",
            TipoConsumo::PesquisaInovacao => "Pesquisa e inovacao (laboratorios, computacao)",
            TipoConsumo::ResidencialExcedente => "Residencial excedente (alem do essencial)",
        }
    }

    pub fn prioridade(&self) -> i32 {
        match self {
            TipoConsumo::EssencialVida => 1,
            TipoConsumo::Saude => 1,
            TipoConsumo::Comunicacao => 1,
            TipoConsumo::Educacao => 2,
            TipoConsumo::Mobilidade => 2,
            TipoConsumo::ProducaoAlimentos => 2,
            TipoConsumo::InfraestruturaComum => 2,
            TipoConsumo::ProducaoBens => 3,
            TipoConsumo::CulturaLazer => 3,
            TipoConsumo::PesquisaInovacao => 3,
            TipoConsumo::ResidencialExcedente => 4,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoArmazenamento {
    BateriaLitio,
    BateriaSodio,
    BateriaFluxo,
    HidroBombeada,
    Gravidade,
    Hidrogenio,
    ArComprimido,
    Termico,
}

impl TipoArmazenamento {
    pub fn id(&self) -> &'static str {
        match self {
            TipoArmazenamento::BateriaLitio => "bateria_litio",
            TipoArmazenamento::BateriaSodio => "bateria_sodio",
            TipoArmazenamento::BateriaFluxo => "bateria_fluxo",
            TipoArmazenamento::HidroBombeada => "hidro_bombeada",
            TipoArmazenamento::Gravidade => "gravidade",
            TipoArmazenamento::Hidrogenio => "hidrogenio",
            TipoArmazenamento::ArComprimido => "ar_comprimido",
            TipoArmazenamento::Termico => "termico",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoArmazenamento::BateriaLitio => "Bateria de litio-ion",
            TipoArmazenamento::BateriaSodio => "Bateria de sodio (mais barato, menos denso)",
            TipoArmazenamento::BateriaFluxo => "Bateria de fluxo redox (escala grid)",
            TipoArmazenamento::HidroBombeada => "Hidroeletrica reversivel (bombeada)",
            TipoArmazenamento::Gravidade => "Armazenamento por gravidade (pesos)",
            TipoArmazenamento::Hidrogenio => "Hidrogenio verde (eletrolise)",
            TipoArmazenamento::ArComprimido => "Ar comprimido (CAES)",
            TipoArmazenamento::Termico => "Armazenamento termico (sal fundido, agua quente)",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum StatusCenario {
    Abundancia,
    Equilibrio,
    Atencao,
    Escassez,
    Emergencia,
}

impl StatusCenario {
    pub fn id(&self) -> &'static str {
        match self {
            StatusCenario::Abundancia => "abundancia",
            StatusCenario::Equilibrio => "equilibrio",
            StatusCenario::Atencao => "atencao",
            StatusCenario::Escassez => "escassez",
            StatusCenario::Emergencia => "emergencia",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            StatusCenario::Abundancia => "Abundancia: geracao supera demanda",
            StatusCenario::Equilibrio => "Equilibrio: geracao = demanda",
            StatusCenario::Atencao => "Atencao: margem baixa (<10%)",
            StatusCenario::Escassez => "Escassez: demanda supera geracao",
            StatusCenario::Emergencia => "Emergencia: deficit critico, assembleia decide",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum StatusInterconexao {
    Ilhado,
    Conectado,
    Exportando,
    Importando,
    Manutencao,
}

impl StatusInterconexao {
    pub fn id(&self) -> &'static str {
        match self {
            StatusInterconexao::Ilhado => "ilhado",
            StatusInterconexao::Conectado => "conectado",
            StatusInterconexao::Exportando => "exportando",
            StatusInterconexao::Importando => "importando",
            StatusInterconexao::Manutencao => "manutencao",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            StatusInterconexao::Ilhado => "Ilhado: microgrid autonomo (sem conexao externa)",
            StatusInterconexao::Conectado => "Conectado a rede regional",
            StatusInterconexao::Exportando => "Exportando excedente (doacao)",
            StatusInterconexao::Importando => "Importando (recebendo doacao)",
            StatusInterconexao::Manutencao => "Em manutencao",
        }
    }
}

// ============================================================================
// 2. STRUCTS (dataclasses)
// ============================================================================

#[derive(Debug, Clone)]
pub struct UnidadeGeracao {
    pub id: String,
    pub fonte: FonteEnergia,
    pub capacidade_kw: f64,
    pub producao_atual_kw: f64,
    pub comunidade_id: String,
    pub status: String,
    pub sustentabilidade_pct: f64,
}

#[derive(Debug, Clone)]
pub struct UnidadeArmazenamento {
    pub id: String,
    pub tipo: TipoArmazenamento,
    pub capacidade_kwh: f64,
    pub carga_atual_kwh: f64,
    pub comunidade_id: String,
    pub ciclos_vida: i32,
}

#[derive(Debug, Clone)]
pub struct ConsumoRegistrado {
    pub id: String,
    pub comunidade_id: String,
    pub tipo: TipoConsumo,
    pub consumo_kw: f64,
    pub timestamp: String,
    pub cidadao_ou_setor: String,
}

#[derive(Debug, Clone)]
pub struct Microgrid {
    pub id: String,
    pub nome: String,
    pub comunidade_id: String,
    pub unidades_geracao: Vec<String>,
    pub unidades_armazenamento: Vec<String>,
    pub interconexao: StatusInterconexao,
    pub autonomia_horas: f64,
    pub geracao_total_kw: f64,
    pub demanda_total_kw: f64,
    pub cenario: StatusCenario,
}

#[derive(Debug, Clone)]
pub struct AlocacaoEscassez {
    pub id: String,
    pub microgrid_id: String,
    pub deficit_kw: f64,
    pub tipos_priorizados: Vec<TipoConsumo>,
    pub tipos_rotacionados: Vec<TipoConsumo>,
    pub tipos_suprimidos: Vec<TipoConsumo>,
    pub duracao_estimada_h: f64,
    pub aprovado_em_assembleia: bool,
    pub justificativa: String,
}

// ============================================================================
// 3. ENGINE
// ============================================================================

pub struct EnergiaEngine {
    pub geracao: HashMap<String, UnidadeGeracao>,
    pub armazenamento: HashMap<String, UnidadeArmazenamento>,
    pub consumos: Vec<ConsumoRegistrado>,
    pub microgrids: HashMap<String, Microgrid>,
    pub alocacoes: HashMap<String, AlocacaoEscassez>,
    gen_id: i32,
    arm_id: i32,
    cons_id: i32,
    mg_id: i32,
    aloc_id: i32,
}

impl EnergiaEngine {
    pub fn new() -> Self {
        EnergiaEngine {
            geracao: HashMap::new(),
            armazenamento: HashMap::new(),
            consumos: Vec::new(),
            microgrids: HashMap::new(),
            alocacoes: HashMap::new(),
            gen_id: 0,
            arm_id: 0,
            cons_id: 0,
            mg_id: 0,
            aloc_id: 0,
        }
    }

    // -- IDs ---------------------------------------------------------------
    fn gen_novo_id(&mut self) -> String {
        self.gen_id += 1;
        format!("GEN-{:04}", self.gen_id)
    }

    fn arm_novo_id(&mut self) -> String {
        self.arm_id += 1;
        format!("ARM-{:04}", self.arm_id)
    }

    fn cons_novo_id(&mut self) -> String {
        self.cons_id += 1;
        format!("CON-{:04}", self.cons_id)
    }

    fn mg_novo_id(&mut self) -> String {
        self.mg_id += 1;
        format!("GRID-{:04}", self.mg_id)
    }

    fn aloc_novo_id(&mut self) -> String {
        self.aloc_id += 1;
        format!("ALOC-{:04}", self.aloc_id)
    }

    // -- cadastro ----------------------------------------------------------
    pub fn cadastrar_geracao(
        &mut self,
        fonte: FonteEnergia,
        capacidade_kw: f64,
        producao_atual_kw: f64,
        comunidade_id: &str,
        sustentabilidade_pct: f64,
    ) -> UnidadeGeracao {
        let u = UnidadeGeracao {
            id: self.gen_novo_id(),
            fonte,
            capacidade_kw,
            producao_atual_kw,
            comunidade_id: comunidade_id.to_string(),
            status: "operacional".to_string(),
            sustentabilidade_pct,
        };
        self.geracao.insert(u.id.clone(), u.clone());
        u
    }

    pub fn cadastrar_armazenamento(
        &mut self,
        tipo: TipoArmazenamento,
        capacidade_kwh: f64,
        carga_atual_kwh: f64,
        comunidade_id: &str,
        ciclos_vida: i32,
    ) -> UnidadeArmazenamento {
        let a = UnidadeArmazenamento {
            id: self.arm_novo_id(),
            tipo,
            capacidade_kwh,
            carga_atual_kwh,
            comunidade_id: comunidade_id.to_string(),
            ciclos_vida,
        };
        self.armazenamento.insert(a.id.clone(), a.clone());
        a
    }

    pub fn registrar_consumo(
        &mut self,
        comunidade_id: &str,
        tipo: TipoConsumo,
        consumo_kw: f64,
        cidadao_ou_setor: &str,
    ) -> ConsumoRegistrado {
        let timestamp = "2026-07-26T12:00:00Z".to_string();
        let c = ConsumoRegistrado {
            id: self.cons_novo_id(),
            comunidade_id: comunidade_id.to_string(),
            tipo,
            consumo_kw,
            timestamp,
            cidadao_ou_setor: cidadao_ou_setor.to_string(),
        };
        self.consumos.push(c.clone());
        c
    }

    pub fn criar_microgrid(
        &mut self,
        nome: &str,
        comunidade_id: &str,
        unidades_geracao: Vec<String>,
        unidades_armazenamento: Vec<String>,
        interconexao: StatusInterconexao,
    ) -> Microgrid {
        let mut mg = Microgrid {
            id: self.mg_novo_id(),
            nome: nome.to_string(),
            comunidade_id: comunidade_id.to_string(),
            unidades_geracao,
            unidades_armazenamento,
            interconexao,
            autonomia_horas: 0.0,
            geracao_total_kw: 0.0,
            demanda_total_kw: 0.0,
            cenario: StatusCenario::Equilibrio,
        };
        self.microgrids.insert(mg.id.clone(), mg.clone());
        self.atualizar_metricas_microgrid(&mg.id);
        mg
    }

    // -- calculo de equilibrio --------------------------------------------
    pub fn atualizar_metricas_microgrid(&mut self, mg_id: &str) {
        if let Some(mg) = self.microgrids.get_mut(mg_id) {
            let mut geracao = 0.0;
            for gid in &mg.unidades_geracao {
                if let Some(g) = self.geracao.get(gid) {
                    geracao += g.producao_atual_kw;
                }
            }
            let mut demanda = 0.0;
            for c in &self.consumos {
                if c.comunidade_id == mg.comunidade_id {
                    demanda += c.consumo_kw;
                }
            }
            mg.geracao_total_kw = (geracao * 100.0).round() / 100.0;
            mg.demanda_total_kw = (demanda * 100.0).round() / 100.0;

            if demanda == 0.0 {
                mg.cenario = StatusCenario::Abundancia;
                return;
            }
            let margem = (geracao - demanda) / demanda;
            mg.cenario = if margem >= 0.2 {
                StatusCenario::Abundancia
            } else if margem >= 0.0 {
                StatusCenario::Equilibrio
            } else if margem >= -0.1 {
                StatusCenario::Atencao
            } else if margem >= -0.3 {
                StatusCenario::Escassez
            } else {
                StatusCenario::Emergencia
            };

            let mut armazenamento_total = 0.0;
            for aid in &mg.unidades_armazenamento {
                if let Some(a) = self.armazenamento.get(aid) {
                    armazenamento_total += a.carga_atual_kwh;
                }
            }
            mg.autonomia_horas = if demanda > 0.0 {
                (armazenamento_total / demanda * 100.0).round() / 100.0
            } else {
                0.0
            };
        }
    }

    pub fn diagnosticar_microgrid(
        &mut self,
        mg_id: &str,
    ) -> (StatusCenario, HashMap<String, String>) {
        self.atualizar_metricas_microgrid(mg_id);
        if let Some(mg) = self.microgrids.get(mg_id) {
            let deficit = (mg.demanda_total_kw - mg.geracao_total_kw).max(0.0);
            let excedente = (mg.geracao_total_kw - mg.demanda_total_kw).max(0.0);

            let mut renovavel = 0.0;
            for gid in &mg.unidades_geracao {
                if let Some(g) = self.geracao.get(gid) {
                    if g.fonte.renovavel() {
                        renovavel += g.producao_atual_kw;
                    }
                }
            }
            let pct_renovavel = if mg.geracao_total_kw > 0.0 {
                (renovavel / mg.geracao_total_kw * 100.0 * 10.0).round() / 10.0
            } else {
                0.0
            };

            let mut info = HashMap::new();
            info.insert(
                "geracao_kw".to_string(),
                format!("{:.2}", mg.geracao_total_kw),
            );
            info.insert(
                "demanda_kw".to_string(),
                format!("{:.2}", mg.demanda_total_kw),
            );
            info.insert("deficit_kw".to_string(), format!("{:.2}", deficit));
            info.insert("excedente_kw".to_string(), format!("{:.2}", excedente));
            info.insert(
                "autonomia_h".to_string(),
                format!("{:.2}", mg.autonomia_horas),
            );
            info.insert("pct_renovavel".to_string(), format!("{:.1}", pct_renovavel));
            info.insert(
                "interconexao".to_string(),
                mg.interconexao.rotulo().to_string(),
            );

            (mg.cenario.clone(), info)
        } else {
            (StatusCenario::Equilibrio, {
                let mut m = HashMap::new();
                m.insert("erro".to_string(), "Microgrid nao encontrada".to_string());
                m
            })
        }
    }

    // -- alocacao democratica em escassez ---------------------------------
    pub fn propor_alocacao_escassez(
        &mut self,
        mg_id: &str,
        duracao_estimada_h: f64,
    ) -> Option<AlocacaoEscassez> {
        let mg = self.microgrids.get(mg_id)?.clone();
        self.atualizar_metricas_microgrid(mg_id);
        let mg = self.microgrids.get(mg_id)?;
        if mg.cenario != StatusCenario::Escassez && mg.cenario != StatusCenario::Emergencia {
            return None;
        }
        let deficit = mg.demanda_total_kw - mg.geracao_total_kw;
        if deficit <= 0.0 {
            return None;
        }

        let mut consumo_por_tipo: HashMap<TipoConsumo, f64> = HashMap::new();
        for c in &self.consumos {
            if c.comunidade_id == mg.comunidade_id {
                *consumo_por_tipo.entry(c.tipo.clone()).or_insert(0.0) += c.consumo_kw;
            }
        }

        let mut tipos_ordenados: Vec<_> = consumo_por_tipo.keys().cloned().collect();
        tipos_ordenados.sort_by_key(|t| t.prioridade());

        let mut geracao_disponivel = mg.geracao_total_kw;
        let mut priorizados = Vec::new();
        let mut rotacionados = Vec::new();
        let mut suprimidos = Vec::new();

        for tipo in tipos_ordenados {
            let consumo_tipo = *consumo_por_tipo.get(&tipo).unwrap_or(&0.0);
            if geracao_disponivel >= consumo_tipo {
                priorizados.push(tipo);
                geracao_disponivel -= consumo_tipo;
            } else if geracao_disponivel > 0.0 {
                rotacionados.push(tipo);
                geracao_disponivel = 0.0;
            } else {
                suprimidos.push(tipo);
            }
        }

        let aloc = AlocacaoEscassez {
            id: self.aloc_novo_id(),
            microgrid_id: mg_id.to_string(),
            deficit_kw: (deficit * 100.0).round() / 100.0,
            tipos_priorizados: priorizados,
            tipos_rotacionados: rotacionados,
            tipos_suprimidos: suprimidos,
            duracao_estimada_h,
            aprovado_em_assembleia: false,
            justificativa: format!(
                "Deficit de {:.1} kW. Geracao alocada por prioridade: essenciais garantidos, nao-essenciais em rodizio/corte. Ninguem fica sem energia essencial por dinheiro (P1).",
                deficit
            ),
        };
        self.alocacoes.insert(aloc.id.clone(), aloc.clone());
        Some(aloc)
    }

    pub fn aprovar_alocacao(&mut self, aloc_id: &str) -> bool {
        if let Some(a) = self.alocacoes.get_mut(aloc_id) {
            a.aprovado_em_assembleia = true;
            true
        } else {
            false
        }
    }

    // -- doacao de excedente (P2P) ----------------------------------------
    pub fn doar_excedente(&mut self, mg_origem_id: &str, mg_destino_id: &str) -> Option<f64> {
        self.atualizar_metricas_microgrid(mg_origem_id);
        self.atualizar_metricas_microgrid(mg_destino_id);

        let origem = self.microgrids.get(mg_origem_id)?.clone();
        let destino = self.microgrids.get(mg_destino_id)?.clone();

        let excedente = origem.geracao_total_kw - origem.demanda_total_kw;
        let deficit = destino.demanda_total_kw - destino.geracao_total_kw;
        if excedente <= 0.0 || deficit <= 0.0 {
            return None;
        }

        let doado = excedente.min(deficit);

        if let Some(origem_mut) = self.microgrids.get_mut(mg_origem_id) {
            origem_mut.interconexao = StatusInterconexao::Exportando;
            origem_mut.geracao_total_kw =
                ((origem_mut.geracao_total_kw - doado) * 100.0).round() / 100.0;
        }
        if let Some(destino_mut) = self.microgrids.get_mut(mg_destino_id) {
            destino_mut.interconexao = StatusInterconexao::Importando;
            destino_mut.geracao_total_kw =
                ((destino_mut.geracao_total_kw + doado) * 100.0).round() / 100.0;
        }

        self.atualizar_metricas_microgrid(mg_origem_id);
        self.atualizar_metricas_microgrid(mg_destino_id);
        Some((doado * 100.0).round() / 100.0)
    }

    // -- eficiencia como dever civico (kaizen) ----------------------------
    pub fn auditoria_eficiencia(&self, comunidade_id: &str) -> HashMap<String, String> {
        let consumos_com: Vec<_> = self
            .consumos
            .iter()
            .filter(|c| c.comunidade_id == comunidade_id)
            .collect();
        if consumos_com.is_empty() {
            let mut m = HashMap::new();
            m.insert("comunidade".to_string(), comunidade_id.to_string());
            m.insert("consumo_total_kw".to_string(), "0".to_string());
            m.insert("alertas".to_string(), "[]".to_string());
            return m;
        }

        let consumo_total: f64 = consumos_com.iter().map(|c| c.consumo_kw).sum();
        let mut consumo_por_tipo: HashMap<TipoConsumo, f64> = HashMap::new();
        for c in &consumos_com {
            *consumo_por_tipo.entry(c.tipo.clone()).or_insert(0.0) += c.consumo_kw;
        }

        let mut alertas = Vec::new();
        for (tipo, val) in &consumo_por_tipo {
            if *tipo == TipoConsumo::ResidencialExcedente && *val > consumo_total * 0.3 {
                alertas.push(format!(
                    "Consumo residencial excedente alto ({:.1} kW, {:.0}% do total). Lembrar: eficiencia liberta capacidade para a comunidade.",
                    val, val / consumo_total * 100.0
                ));
            }
            if *tipo == TipoConsumo::ProducaoBens && *val > consumo_total * 0.4 {
                alertas.push(format!(
                    "Producao de bens consome {:.1} kW. Otimizar processos = mais capacidade para saude e educacao.",
                    val
                ));
            }
        }

        let mut resultado = HashMap::new();
        resultado.insert("comunidade".to_string(), comunidade_id.to_string());
        resultado.insert(
            "consumo_total_kw".to_string(),
            format!("{:.2}", consumo_total),
        );
        let por_tipo: Vec<String> = consumo_por_tipo
            .iter()
            .map(|(t, v)| format!("{}: {:.1}", t.rotulo(), v))
            .collect();
        resultado.insert("consumo_por_tipo".to_string(), por_tipo.join("; "));
        resultado.insert("alertas_eficiencia".to_string(), alertas.join(" | "));
        resultado.insert("mensagem".to_string(), "Energia e gratuita. Eficiencia nao economiza dinheiro -- LIBERTA capacidade para quem precisa. E kaizen civico.".to_string());
        resultado
    }

    // -- scorecard global --------------------------------------------------
    pub fn scorecard(&self) -> HashMap<String, String> {
        let geracao_total: f64 = self.geracao.values().map(|g| g.producao_atual_kw).sum();
        let renovavel: f64 = self
            .geracao
            .values()
            .filter(|g| g.fonte.renovavel())
            .map(|g| g.producao_atual_kw)
            .sum();
        let demanda_total: f64 = self.consumos.iter().map(|c| c.consumo_kw).sum();
        let armazenamento_total: f64 = self.armazenamento.values().map(|a| a.carga_atual_kwh).sum();

        let mut sc = HashMap::new();
        sc.insert(
            "unidades_geracao".to_string(),
            self.geracao.len().to_string(),
        );
        sc.insert(
            "unidades_armazenamento".to_string(),
            self.armazenamento.len().to_string(),
        );
        sc.insert("microgrids".to_string(), self.microgrids.len().to_string());
        sc.insert(
            "geracao_total_kw".to_string(),
            format!("{:.1}", geracao_total),
        );
        sc.insert(
            "demanda_total_kw".to_string(),
            format!("{:.1}", demanda_total),
        );
        sc.insert(
            "excedente_kw".to_string(),
            format!("{:.1}", (geracao_total - demanda_total).max(0.0)),
        );
        sc.insert(
            "pct_renovavel".to_string(),
            if geracao_total > 0.0 {
                format!("{:.1}", renovavel / geracao_total * 100.0)
            } else {
                "0.0".to_string()
            },
        );
        sc.insert(
            "armazenamento_kwh".to_string(),
            format!("{:.1}", armazenamento_total),
        );
        sc.insert(
            "alocacoes_escassez".to_string(),
            self.alocacoes.len().to_string(),
        );
        let doacoes = self
            .microgrids
            .values()
            .filter(|mg| mg.interconexao == StatusInterconexao::Exportando)
            .count();
        sc.insert("doacoes_realizadas".to_string(), doacoes.to_string());
        sc
    }
}

// ============================================================================
// 4. DEMO (main)
// ============================================================================

fn main() {
    let mut e = EnergiaEngine::new();

    println!("{}", "=".repeat(70));
    println!("OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso");
    println!("{}", "=".repeat(70));

    // --- Comunidade 1: Solar Village (abundancia) ---
    println!("\n[CENARIO 1] Solar Village -- abundancia (geracao > demanda)");
    let g1 = e.cadastrar_geracao(FonteEnergia::Solar, 500.0, 480.0, "solar_village", 100.0);
    let g2 = e.cadastrar_geracao(FonteEnergia::Eolica, 300.0, 250.0, "solar_village", 100.0);
    let a1 = e.cadastrar_armazenamento(
        TipoArmazenamento::BateriaLitio,
        2000.0,
        1500.0,
        "solar_village",
        10000,
    );
    let a2 = e.cadastrar_armazenamento(
        TipoArmazenamento::BateriaFluxo,
        5000.0,
        4000.0,
        "solar_village",
        10000,
    );

    for (tipo, kw) in [
        (TipoConsumo::EssencialVida, 120.0),
        (TipoConsumo::Saude, 40.0),
        (TipoConsumo::Comunicacao, 30.0),
        (TipoConsumo::Educacao, 50.0),
        (TipoConsumo::CulturaLazer, 80.0),
        (TipoConsumo::ResidencialExcedente, 100.0),
    ] {
        e.registrar_consumo("solar_village", tipo, kw, "");
    }

    let mg1 = e.criar_microgrid(
        "Solar Village Grid",
        "solar_village",
        vec![g1.id.clone(), g2.id.clone()],
        vec![a1.id.clone(), a2.id.clone()],
        StatusInterconexao::Conectado,
    );
    let (cenario1, info1) = e.diagnosticar_microgrid(&mg1.id);
    println!(
        "  Geracao: {} kW | Demanda: {} kW",
        info1.get("geracao_kw").unwrap(),
        info1.get("demanda_kw").unwrap()
    );
    println!(
        "  Excedente: {} kW | Renovavel: {}%",
        info1.get("excedente_kw").unwrap(),
        info1.get("pct_renovavel").unwrap()
    );
    println!(
        "  Autonomia (ilhado): {}h",
        info1.get("autonomia_h").unwrap()
    );
    println!("  Cenario: {}", cenario1.rotulo());
    println!("  Energia para QUALQUER uso: sim, sem conta, sem medidor de cobranca.");

    // --- Comunidade 2: Vale Seco (escassez) ---
    println!("\n[CENARIO 2] Vale Seco -- escassez (seca reduziu hidro)");
    let g3 = e.cadastrar_geracao(FonteEnergia::Hidro, 400.0, 150.0, "vale_seco", 100.0);
    let g4 = e.cadastrar_geracao(FonteEnergia::Solar, 200.0, 180.0, "vale_seco", 100.0);
    let a3 = e.cadastrar_armazenamento(
        TipoArmazenamento::Hidrogenio,
        3000.0,
        800.0,
        "vale_seco",
        10000,
    );

    for (tipo, kw) in [
        (TipoConsumo::EssencialVida, 100.0),
        (TipoConsumo::Saude, 60.0),
        (TipoConsumo::Comunicacao, 20.0),
        (TipoConsumo::Educacao, 40.0),
        (TipoConsumo::ProducaoBens, 80.0),
        (TipoConsumo::CulturaLazer, 50.0),
    ] {
        e.registrar_consumo("vale_seco", tipo, kw, "");
    }

    let mg2 = e.criar_microgrid(
        "Vale Seco Grid",
        "vale_seco",
        vec![g3.id.clone(), g4.id.clone()],
        vec![a3.id.clone()],
        StatusInterconexao::Conectado,
    );
    let (cenario2, info2) = e.diagnosticar_microgrid(&mg2.id);
    println!(
        "  Geracao: {} kW | Demanda: {} kW",
        info2.get("geracao_kw").unwrap(),
        info2.get("demanda_kw").unwrap()
    );
    println!(
        "  Deficit: {} kW | Cenario: {}",
        info2.get("deficit_kw").unwrap(),
        cenario2.rotulo()
    );
    println!("  Autonomia: {}h", info2.get("autonomia_h").unwrap());

    // --- Alocacao democratica em escassez ---
    println!("\n[ALOCACAO DEMOCRATICA EM ESCASSEZ]");
    if let Some(aloc) = e.propor_alocacao_escassez(&mg2.id, 48.0) {
        println!("  Proposta {} (assembleia precisa aprovar):", aloc.id);
        println!(
            "  Deficit: {} kW | Duracao estimada: {}h",
            aloc.deficit_kw, aloc.duracao_estimada_h
        );
        let prior: Vec<_> = aloc.tipos_priorizados.iter().map(|t| t.rotulo()).collect();
        println!("  GARANTIDOS (prioridade): {:?}", prior);
        let rod: Vec<_> = aloc.tipos_rotacionados.iter().map(|t| t.rotulo()).collect();
        println!("  EM RODIZIO: {:?}", rod);
        let sup: Vec<_> = aloc.tipos_suprimidos.iter().map(|t| t.rotulo()).collect();
        println!("  SUPRIMIDOS: {:?}", sup);
        println!("  Justificativa: {}", aloc.justificativa);
        e.aprovar_alocacao(&aloc.id);
        println!("  Aprovado em assembleia: {}", aloc.aprovado_em_assembleia);
    }

    // --- Doacao P2P: Solar Village -> Vale Seco ---
    println!("\n[DOACAO P2P] Solar Village doe excedente para Vale Seco");
    if let Some(doado) = e.doar_excedente(&mg1.id, &mg2.id) {
        println!("  {:.1} kW doados (sem dinheiro, sem cobranca).", doado);
        let (_, info2_pos) = e.diagnosticar_microgrid(&mg2.id);
        println!(
            "  Vale Seco pos-doacao: geracao={} kW, deficit={} kW, cenario={}",
            info2_pos.get("geracao_kw").unwrap(),
            info2_pos.get("deficit_kw").unwrap(),
            info2_pos.get("interconexao").unwrap()
        );
    }

    // --- Auditoria de eficiencia (kaizen civico) ---
    println!("\n[AUDITORIA DE EFICIENCIA -- dever civico, nao economia]");
    let aud = e.auditoria_eficiencia("solar_village");
    println!("  Comunidade: {}", aud.get("comunidade").unwrap());
    println!(
        "  Consumo total: {} kW",
        aud.get("consumo_total_kw").unwrap()
    );
    if let Some(por_tipo) = aud.get("consumo_por_tipo") {
        for item in por_tipo.split("; ") {
            println!("    {}", item);
        }
    }
    if let Some(alertas) = aud.get("alertas_eficiencia") {
        if !alertas.is_empty() {
            for a in alertas.split(" | ") {
                println!("  ALERTA: {}", a);
            }
        }
    }
    println!("  {}", aud.get("mensagem").unwrap());

    // --- Scorecard global ---
    println!("\n{}", "=".repeat(70));
    println!("[SCORECARD ENERGETICO DA REPUBLICA]");
    println!("{}", "=".repeat(70));
    let sc = e.scorecard();
    for (k, v) in &sc {
        println!("  {:.<28} {}", k, v);
    }

    // --- Catalogo de fontes ---
    println!("\n[FONTES DE ENERGIA DA REPUBLICA]");
    for f in [
        FonteEnergia::Solar,
        FonteEnergia::Eolica,
        FonteEnergia::Hidro,
        FonteEnergia::Geotermica,
        FonteEnergia::Biomassa,
        FonteEnergia::Mares,
        FonteEnergia::Nuclear,
        FonteEnergia::Fusao,
    ] {
        let flag = if f.renovavel() {
            "renovavel"
        } else {
            "NAO-renovavel"
        };
        println!("  {:.<30} [{}]", f.rotulo(), flag);
    }

    // --- FILOSOFIA ---
    println!("\n{}", "=".repeat(70));
    println!("FILOSOFIA -- Por que energia e gratuita para todo e qualquer uso");
    println!("{}", "=".repeat(70));
    println!(
        r#"
ENERGIA NAO E MERCADORIA. E CONDICAO DE VIDA.
Cozinhar precisa de energia. Aquecer precisa de energia.
Curar precisa de energia. Comunicar precisa de energia.
Estudar precisa de energia. Criar precisa de energia.
Cobrar por energia e cobrar por EXISTIR.

O ARGUMENTO DA ESCASSEZ (e por que e falso):
O capitalismo diz: "se energia e gratis, todos desperdicam."
Falso. O capitalista desperdica porque o custo e EXTERNO ao lucro.
O cidadao da Republica SABE que a energia que desperdica falta para o vizinho.
Eficiencia nao economiza dinheiro -- LIBERTA capacidade para a comunidade.

A UNICA ESCASSEZ REAL (e como se resolve):
Quando a geracao nao cobre a demanda (seca, falha), a assembleia decide:
1. Essenciais (vida, saude, comunicacao) SEMPRE garantidos.
2. Nao-essenciais em rodizio democratico.
3. Ninguem fica sem energia por DINHEIRO. So por PRIORIDADE civica.
4. A solucao de longo prazo e GERAR MAIS, nao racionar.
O capitalismo raciona por preco (quem tem dinheiro usa, quem nao tem corta).
A Republica aloca por prioridade (todos tem o essencial, o resto e civico).

A REVOLUCAO ENERGETICA:
1. Cada comunidade gera a propria energia (geracao distribuida).
2. Excedente e DOADO, nao vendido (P2P, sem intermediario).
3. Armazenamento comunitario (baterias compartilhadas).
4. 100% renovavel (a Republica respeita o planeta que a sustenta).
5. Nucleo essencial garantido para TODOS, sem excecao, sem condicao.
6. "Para todo e qualquer uso" -- a Republica nao pergunta PARA QUE.
   Pergunta quanto voce PRECISA, e garante que tem.

A ENERGIA E O AR DA CIVILIZACAO.
Ninguem cobra pelo ar. Ninguem deve cobrar pela energia.
"#
    );
}
