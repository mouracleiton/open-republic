// OpenDebtImpact -- Todos os Impactos da Divida na Vida Humana
// ================================================================
// "A divida nao so mata. Ela CASTRA.
// Castra a educacao. Castra a ciencia. Castra a moradia.
// Castra o futuro. Cada real pro agiota e um real roubado
// de cada area que faz a vida valer a pena."
//
// Este modulo simula o impacto da divida em TODAS as dimensoes
// da vida brasileira. Nao so mortes (OpenDebtMortality) -- mas
// tudo que a divida DESTRÓI silenciosamente:
//
// 1. EDUCACAO: escolas, professores, alfabetizacao
// 2. SAUDE MENTAL: depressao, ansiedade, suicidio
// 3. MORADIA: sem-teto, favelas, habitacao
// 4. SEGURANCA ALIMENTAR: fome, desnutricao
// 5. INFRAESTRUTURA: estradas, transporte, energia
// 6. SANEAMENTO: agua, esgoto, lixo
// 7. CIENCIA & TECNOLOGIA: pesquisa, inovacao, patentes
// 8. CULTURA & ARTE: museus, teatro, musica
// 9. DESIGUALDADE: renda, genero, raca
// 10. MEIO AMBIENTE: desmatamento, poluicao
// 11. SEGURANCA: policia, violencia
// 12. ESPORTE: educacao fisica, lazer
// 13. TRANSPORTES: metro, onibus, mobilidade
// 14. COMUNICACOES: internet, conectividade
// 15. INFANCIA: creches, primeira infancia
//
// Para cada area, calcula ano a ano:
// - Quanto foi ROUBADO pelo juros da divida
// - O que esse dinheiro teria construido
// - Quantas pessoas foram afetadas
// - O impacto cumulativo em 20 anos
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

use std::collections::HashMap;

// ============================================================================
// 1. AREAS DE IMPACTO
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum ImpactArea {
    Education,
    HealthMental,
    Housing,
    FoodSecurity,
    Infrastructure,
    Sanitation,
    ScienceTech,
    CultureArts,
    Inequality,
    Environment,
    Security,
    Sport,
    Transport,
    Connectivity,
    Childhood,
}

impl ImpactArea {
    pub fn value(&self) -> &'static str {
        match self {
            ImpactArea::Education => "educacao",
            ImpactArea::HealthMental => "saude_mental",
            ImpactArea::Housing => "moradia",
            ImpactArea::FoodSecurity => "seguranca_alimentar",
            ImpactArea::Infrastructure => "infraestrutura",
            ImpactArea::Sanitation => "saneamento",
            ImpactArea::ScienceTech => "ciencia_tecnologia",
            ImpactArea::CultureArts => "cultura_arte",
            ImpactArea::Inequality => "desigualdade",
            ImpactArea::Environment => "meio_ambiente",
            ImpactArea::Security => "seguranca",
            ImpactArea::Sport => "esporte",
            ImpactArea::Transport => "transporte",
            ImpactArea::Connectivity => "conectividade",
            ImpactArea::Childhood => "infancia",
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum SeverityLevel {
    Critical,
    Severe,
    High,
    Moderate,
    Low,
}

impl SeverityLevel {
    pub fn value(&self) -> &'static str {
        match self {
            SeverityLevel::Critical => "critico",
            SeverityLevel::Severe => "severo",
            SeverityLevel::High => "alto",
            SeverityLevel::Moderate => "moderado",
            SeverityLevel::Low => "baixo",
        }
    }
}

#[derive(Debug, Clone)]
pub struct AreaImpact {
    pub area: ImpactArea,
    pub name: String,
    pub severity: SeverityLevel,
    pub annual_budget_needed_brl: f64,
    pub annual_budget_actual_brl: f64,
    pub annual_budget_gap_brl: f64,
    pub pct_of_interest_that_should_go: f64,
    pub people_affected_per_year: i64,
    pub unit_cost_brl: f64,
    pub unit_name: String,
    pub units_not_delivered_per_year: i64,
    pub description: String,
    pub human_cost: String,
}

impl AreaImpact {
    pub fn budget_gap_percentage(&self) -> f64 {
        if self.annual_budget_needed_brl <= 0.0 {
            return 0.0;
        }
        (self.annual_budget_gap_brl / self.annual_budget_needed_brl) * 100.0
    }

    pub fn units_lost_per_billion(&self) -> f64 {
        if self.unit_cost_brl <= 0.0 {
            return 0.0;
        }
        1_000_000_000.0 / self.unit_cost_brl
    }
}

// ============================================================================
// 2. CATALOGO DE IMPACTOS (15 areas)
// ============================================================================

pub fn get_area_impacts() -> Vec<AreaImpact> {
    vec![
        AreaImpact {
            area: ImpactArea::Education,
            name: "Educacao Basica e Superior".to_string(),
            severity: SeverityLevel::Critical,
            annual_budget_needed_brl: 600e9,
            annual_budget_actual_brl: 180e9,
            annual_budget_gap_brl: 420e9,
            pct_of_interest_that_should_go: 0.15,
            people_affected_per_year: 50_000_000,
            unit_cost_brl: 5e6,
            unit_name: "escolas".to_string(),
            units_not_delivered_per_year: 84_000,
            description: "Educacao publica subfinanciada ha decadas.".to_string(),
            human_cost: "Criancas em escolas sem teto, sem merenda, sem professor. Universitarios sem bolsa. Analfabetismo funcional em 30% dos adultos.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::HealthMental,
            name: "Saude Mental".to_string(),
            severity: SeverityLevel::Severe,
            annual_budget_needed_brl: 80e9,
            annual_budget_actual_brl: 4e9,
            annual_budget_gap_brl: 76e9,
            pct_of_interest_that_should_go: 0.03,
            people_affected_per_year: 20_000_000,
            unit_cost_brl: 200_000.0,
            unit_name: "CAPS (centro de saude mental)".to_string(),
            units_not_delivered_per_year: 380_000,
            description: "Brasil tem 20 milhoes com transtorno mental. So 5% do orcamento necessario.".to_string(),
            human_cost: "Depressao nao tratada. Ansiedade cronica. Suicidios. Crack. Sem psicologo no SUS.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Housing,
            name: "Moradia Digna".to_string(),
            severity: SeverityLevel::Critical,
            annual_budget_needed_brl: 200e9,
            annual_budget_actual_brl: 15e9,
            annual_budget_gap_brl: 185e9,
            pct_of_interest_that_should_go: 0.10,
            people_affected_per_year: 8_000_000,
            unit_cost_brl: 80_000.0,
            unit_name: "casas populares".to_string(),
            units_not_delivered_per_year: 2_312_500,
            description: "Deficit habitacional de 8 milhoes de familias.".to_string(),
            human_cost: "Familias em favelas, ruas, corticos. Criancas sem endereco fixo. Sem-teto morrendo de frio.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::FoodSecurity,
            name: "Seguranca Alimentar (Fome)".to_string(),
            severity: SeverityLevel::Critical,
            annual_budget_needed_brl: 120e9,
            annual_budget_actual_brl: 35e9,
            annual_budget_gap_brl: 85e9,
            pct_of_interest_that_should_go: 0.08,
            people_affected_per_year: 33_000_000,
            unit_cost_brl: 3.0,
            unit_name: "refeicoes diarias".to_string(),
            units_not_delivered_per_year: 28_333_333_333,
            description: "33 milhoes de brasileiros passam fome. O pais da soja nao alimenta seu povo.".to_string(),
            human_cost: "Criancas desnutridas. Maes que pulam refeicoes. Idosos escolhendo entre comer e remedio.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Infrastructure,
            name: "Infraestrutura (Estradas, Energia)".to_string(),
            severity: SeverityLevel::Severe,
            annual_budget_needed_brl: 300e9,
            annual_budget_actual_brl: 60e9,
            annual_budget_gap_brl: 240e9,
            pct_of_interest_that_should_go: 0.12,
            people_affected_per_year: 215_000_000,
            unit_cost_brl: 20e6,
            unit_name: "km de rodovia".to_string(),
            units_not_delivered_per_year: 12_000,
            description: "Estradas esburacadas. Pontes caindo. Sem investimento em energia.".to_string(),
            human_cost: "Acidentes fatais em estradas sem manutencao. Apagoes. Logistica cara = comida cara.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Sanitation,
            name: "Saneamento Basico".to_string(),
            severity: SeverityLevel::Severe,
            annual_budget_needed_brl: 100e9,
            annual_budget_actual_brl: 12e9,
            annual_budget_gap_brl: 88e9,
            pct_of_interest_that_should_go: 0.05,
            people_affected_per_year: 100_000_000,
            unit_cost_brl: 12_000.0,
            unit_name: "ligacoes de agua/esgoto".to_string(),
            units_not_delivered_per_year: 7_333_333,
            description: "Metade do Brasil nao tem esgoto tratado. Doencas por agua contaminada.".to_string(),
            human_cost: "Criancas com diarreia. Dengue. Leptospirose nas enchentes. Agua nao potavel.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::ScienceTech,
            name: "Ciencia e Tecnologia".to_string(),
            severity: SeverityLevel::Severe,
            annual_budget_needed_brl: 80e9,
            annual_budget_actual_brl: 8e9,
            annual_budget_gap_brl: 72e9,
            pct_of_interest_that_should_go: 0.04,
            people_affected_per_year: 500_000,
            unit_cost_brl: 500_000.0,
            unit_name: "bolsas de pesquisa".to_string(),
            units_not_delivered_per_year: 144_000,
            description: "CNPq e Capes com orcamento destroicado. Cerebros fugindo do pais.".to_string(),
            human_cost: "Pesquisadores no rdar de UBER. Doutores desempregados. Laboratorios fechados. Patentes perdidas.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::CultureArts,
            name: "Cultura e Arte".to_string(),
            severity: SeverityLevel::High,
            annual_budget_needed_brl: 30e9,
            annual_budget_actual_brl: 3e9,
            annual_budget_gap_brl: 27e9,
            pct_of_interest_that_should_go: 0.02,
            people_affected_per_year: 10_000_000,
            unit_cost_brl: 100_000.0,
            unit_name: "producoes culturais".to_string(),
            units_not_delivered_per_year: 270_000,
            description: "Cultura tratada como luxo. Artistas sem renda. Museus fechados.".to_string(),
            human_cost: "Teatros fechados. Cinema nacional morto. Musicos sem espaco. Identidade cultural apagada.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Inequality,
            name: "Desigualdade de Renda".to_string(),
            severity: SeverityLevel::Critical,
            annual_budget_needed_brl: 500e9,
            annual_budget_actual_brl: 50e9,
            annual_budget_gap_brl: 450e9,
            pct_of_interest_that_should_go: 0.15,
            people_affected_per_year: 150_000_000,
            unit_cost_brl: 500.0,
            unit_name: "transferencias de renda/mes".to_string(),
            units_not_delivered_per_year: 900_000_000,
            description: "Brasil entre os 10 paises mais desiguais do mundo. Gini = 0.52.".to_string(),
            human_cost: "1% tem 50% da riqueza. Milhoes vivem com R$ 200/mes. Favelas ao lado de condominios.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Environment,
            name: "Meio Ambiente".to_string(),
            severity: SeverityLevel::Severe,
            annual_budget_needed_brl: 50e9,
            annual_budget_actual_brl: 5e9,
            annual_budget_gap_brl: 45e9,
            pct_of_interest_that_should_go: 0.03,
            people_affected_per_year: 215_000_000,
            unit_cost_brl: 100_000.0,
            unit_name: "km2 protegidos/fiscalizados".to_string(),
            units_not_delivered_per_year: 450_000,
            description: "Desmatamento da Amazonia acelerando. IBAMA sem orcamento.".to_string(),
            human_cost: "Amazonia queimando. Agua acabando. Temperatura subindo. Futuro climatico destruido.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Security,
            name: "Seguranca Publica".to_string(),
            severity: SeverityLevel::Severe,
            annual_budget_needed_brl: 150e9,
            annual_budget_actual_brl: 70e9,
            annual_budget_gap_brl: 80e9,
            pct_of_interest_that_should_go: 0.05,
            people_affected_per_year: 60_000_000,
            unit_cost_brl: 2e6,
            unit_name: "delegacias equipadas".to_string(),
            units_not_delivered_per_year: 40_000,
            description: "47 mil homicidios/ano. Mulheres mortas. LGBTQIA+ assassinados.".to_string(),
            human_cost: "Maes chorando filhos. Criancas sem pai. Medo de sair de casa. Violencia domestica.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Sport,
            name: "Esporte e Lazer".to_string(),
            severity: SeverityLevel::Moderate,
            annual_budget_needed_brl: 20e9,
            annual_budget_actual_brl: 2e9,
            annual_budget_gap_brl: 18e9,
            pct_of_interest_that_should_go: 0.01,
            people_affected_per_year: 40_000_000,
            unit_cost_brl: 300_000.0,
            unit_name: "quadras esportivas".to_string(),
            units_not_delivered_per_year: 60_000,
            description: "Esporte como ferramenta de resgate social destruido.".to_string(),
            human_cost: "Criancas sem quadra. Jovens sem esporte = sem alternativa ao crime. Talentos perdidos.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Transport,
            name: "Transporte Publico".to_string(),
            severity: SeverityLevel::Severe,
            annual_budget_needed_brl: 200e9,
            annual_budget_actual_brl: 30e9,
            annual_budget_gap_brl: 170e9,
            pct_of_interest_that_should_go: 0.08,
            people_affected_per_year: 100_000_000,
            unit_cost_brl: 100e6,
            unit_name: "km de metro/onetbus".to_string(),
            units_not_delivered_per_year: 1_700,
            description: "Metro sem expansao. Onibus lotados. Povo passa 3h/dia no transito.".to_string(),
            human_cost: "3 horas/dia no onibus lotado. Menos tempo com familia. Menos estudo. Mais estresse.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Connectivity,
            name: "Internet e Conectividade".to_string(),
            severity: SeverityLevel::High,
            annual_budget_needed_brl: 40e9,
            annual_budget_actual_brl: 5e9,
            annual_budget_gap_brl: 35e9,
            pct_of_interest_that_should_go: 0.02,
            people_affected_per_year: 70_000_000,
            unit_cost_brl: 5_000.0,
            unit_name: "conexoes de internet".to_string(),
            units_not_delivered_per_year: 7_000_000,
            description: "70 milhoes sem internet de qualidade. Exclusao digital.".to_string(),
            human_cost: "Criancas estudando no celular 3G. Sem telemedicina. Sem servicos publicos digitais.".to_string(),
        },
        AreaImpact {
            area: ImpactArea::Childhood,
            name: "Primeira Infancia (0-6 anos)".to_string(),
            severity: SeverityLevel::Critical,
            annual_budget_needed_brl: 80e9,
            annual_budget_actual_brl: 8e9,
            annual_budget_gap_brl: 72e9,
            pct_of_interest_that_should_go: 0.04,
            people_affected_per_year: 12_000_000,
            unit_cost_brl: 1e6,
            unit_name: "vagas em creches".to_string(),
            units_not_delivered_per_year: 72_000,
            description: "12 milhoes de criancas 0-6 sem creche. Desenvolvimento comprometido.".to_string(),
            human_cost: "Maes sem trabalhar porque nao tem creche. Criancas em casa sem estimulo. Futuro comprometido.".to_string(),
        },
    ]
}

// ============================================================================
// 3. SIMULACAO ANO A ANO (20 anos)
// ============================================================================

#[derive(Debug, Clone)]
pub struct YearImpact {
    pub year_label: i32,
    pub interest_paid_brl: f64,
    pub total_gap_brl: f64,
    pub total_people_affected: i64,
    pub area_details: HashMap<String, AreaDetail>,
    pub cumulative_gap_brl: f64,
    pub cumulative_people_affected: i64,
}

#[derive(Debug, Clone)]
pub struct AreaDetail {
    pub name: String,
    pub gap_brl: f64,
    pub people_affected: i64,
    pub units_not_delivered: i64,
    pub unit_name: String,
    pub severity: String,
    pub human_cost: String,
    pub gap_pct_of_interest: f64,
}

pub struct ImpactSimulator {
    pub start_year: i32,
    pub years: i32,
    pub initial_debt: f64,
    pub initial_gdp: f64,
    pub interest_rate: f64,
    pub gdp_growth: f64,
    pub simulations: Vec<YearImpact>,
}

impl ImpactSimulator {
    pub fn new(start_year: i32, years: i32) -> Self {
        ImpactSimulator {
            start_year,
            years,
            initial_debt: 6.0e12,
            initial_gdp: 10.0e12,
            interest_rate: 0.12,
            gdp_growth: 0.025,
            simulations: Vec::new(),
        }
    }

    pub fn simulate(&mut self) -> Vec<YearImpact> {
        self.simulations.clear();
        let mut debt = self.initial_debt;
        let mut gdp = self.initial_gdp;
        let mut cumulative_gap = 0.0;
        let mut cumulative_people: i64 = 0;
        let area_impacts = get_area_impacts();

        for i in 0..=self.years {
            let year_label = self.start_year + i;
            let interest = debt * self.interest_rate;

            let mut total_gap = 0.0;
            let mut total_people: i64 = 0;
            let mut area_details = HashMap::new();

            for ai in &area_impacts {
                let inflation_factor = 1.05_f64.powi(i as i32);
                let gap = ai.annual_budget_gap_brl * inflation_factor;
                let people = ai.people_affected_per_year;
                let units = (gap / ai.unit_cost_brl) as i64;

                total_gap += gap;
                total_people += people;

                area_details.insert(
                    ai.area.value().to_string(),
                    AreaDetail {
                        name: ai.name.clone(),
                        gap_brl: gap,
                        people_affected: people,
                        units_not_delivered: units,
                        unit_name: ai.unit_name.clone(),
                        severity: ai.severity.value().to_string(),
                        human_cost: ai.human_cost.clone(),
                        gap_pct_of_interest: if interest > 0.0 { (gap / interest) * 100.0 } else { 0.0 },
                    },
                );
            }

            cumulative_gap += total_gap;
            cumulative_people += total_people;

            let sim = YearImpact {
                year_label,
                interest_paid_brl: interest,
                total_gap_brl: total_gap,
                total_people_affected: total_people,
                area_details,
                cumulative_gap_brl: cumulative_gap,
                cumulative_people_affected: cumulative_people,
            };
            self.simulations.push(sim);

            debt = debt + interest - (gdp * 0.18 * 0.3);
            gdp = gdp * (1.0 + self.gdp_growth);
        }

        self.simulations.clone()
    }

    pub fn total_gap_all_years(&self) -> f64 {
        if let Some(last) = self.simulations.last() {
            last.cumulative_gap_brl
        } else {
            0.0
        }
    }

    pub fn total_interest_all_years(&self) -> f64 {
        self.simulations.iter().map(|s| s.interest_paid_brl).sum()
    }

    pub fn summary(&self) -> Summary {
        Summary {
            years_simulated: self.years,
            total_gap_trillions: self.total_gap_all_years() / 1e12,
            total_interest_trillions: self.total_interest_all_years() / 1e12,
            avg_gap_per_year_trillions: (self.total_gap_all_years() / self.years as f64) / 1e12,
            areas_impacted: get_area_impacts().len() as i32,
            total_people_per_year: if let Some(first) = self.simulations.first() {
                first.total_people_affected
            } else {
                0
            },
        }
    }
}

#[derive(Debug)]
pub struct Summary {
    pub years_simulated: i32,
    pub total_gap_trillions: f64,
    pub total_interest_trillions: f64,
    pub avg_gap_per_year_trillions: f64,
    pub areas_impacted: i32,
    pub total_people_per_year: i64,
}

// ============================================================================
// 4. RENDERIZACOES VISUAIS
// ============================================================================

pub fn render_area_chart(simulations: &[YearImpact]) -> String {
    if simulations.is_empty() {
        return String::new();
    }
    let s = &simulations[0];
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(75));
    lines.push(format!("  DEFICIT POR AREA -- {} (R$ bilhoes)", s.year_label));
    lines.push("=".repeat(75));
    lines.push(String::new());

    let mut areas_sorted: Vec<_> = s.area_details.iter().collect();
    areas_sorted.sort_by(|a, b| b.1.gap_brl.partial_cmp(&a.1.gap_brl).unwrap());

    let max_gap = areas_sorted.iter().map(|(_, v)| v.gap_brl).fold(0.0, f64::max).max(1.0);

    for (_, details) in &areas_sorted {
        let gap_bi = details.gap_brl / 1e9;
        let bar_len = ((details.gap_brl / max_gap) * 40.0) as usize;
        let bar = "X".repeat(bar_len.max(1));
        let sev = details.severity.to_uppercase()[..4.min(details.severity.len())].to_string();
        lines.push(format!(
            "  {:<35} R${:>7.0}bi [{:40}] {}",
            details.name, gap_bi, bar, sev
        ));
    }

    lines.push(String::new());
    lines.push("  X = deficit orcamentario (dinheiro que FOI PRO JUROS)".to_string());
    lines.push(format!("  TOTAL DEFICIT/ANO: R$ {:.0} bilhoes", s.total_gap_brl / 1e9));
    lines.push(format!("  PESSOAS AFETADAS/ANO: {}", s.total_people_affected));
    lines.push(String::new());
    lines.join("\n")
}

pub fn render_cumulative_chart(simulations: &[YearImpact]) -> String {
    if simulations.is_empty() {
        return String::new();
    }
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(70));
    lines.push("  DEFICIT ACUMULADO POR ANO (R$ trilhoes)".to_string());
    lines.push("=".repeat(70));
    lines.push(String::new());

    let max_val = simulations.last().unwrap().cumulative_gap_brl.max(1.0);

    for s in simulations {
        let val_t = s.cumulative_gap_brl / 1e12;
        let bar_len = ((s.cumulative_gap_brl / max_val) * 50.0) as usize;
        let bar = "#".repeat(bar_len.max(1));
        lines.push(format!("  {} |{:<50}| R$ {:.1}T", s.year_label, bar, val_t));
    }

    lines.push(String::new());
    lines.push(format!(
        "  Em {}: R$ {:.1} trilhoes ROUBADOS",
        simulations.last().unwrap().year_label,
        simulations.last().unwrap().cumulative_gap_brl / 1e12
    ));
    lines.push("  de educacao, saude, moradia, ciencia, cultura...".to_string());
    lines.push(String::new());
    lines.join("\n")
}

pub fn render_human_cost() -> String {
    let area_impacts = get_area_impacts();
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(70));
    lines.push("  O CUSTO HUMANO -- O QUE A DIVIDA DESTRÓI".to_string());
    lines.push("=".repeat(70));

    for ai in &area_impacts {
        lines.push(String::new());
        lines.push(format!("  {} [{}]", ai.name.to_uppercase(), ai.severity.value().to_uppercase()));
        lines.push(format!("  Deficit: R$ {:.0} bilhoes/ano", ai.annual_budget_gap_brl / 1e9));
        lines.push(format!("  Pessoas afetadas: {}/ano", ai.people_affected_per_year));
        lines.push(format!("  Nao entregue: {} {}/ano", ai.units_not_delivered_per_year, ai.unit_name));
        lines.push(format!("  CUSTO HUMANO: {}", ai.human_cost));
        lines.push("  ".to_string() + &"─".repeat(66));
    }

    lines.push(String::new());
    lines.join("\n")
}

pub fn render_equivalence_table() -> String {
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(70));
    lines.push("  O QUE R$ 100 BILHOES DE JUROS ROUBOU DO POVO".to_string());
    lines.push("  (equivalencia: se esse dinheiro ficasse no Brasil)".to_string());
    lines.push("=".repeat(70));
    lines.push(String::new());
    lines.push(format!("  {:<35} {:>15}", "RECURSO", "QTD"));
    lines.push("  ".to_string() + &"-".repeat(52));

    let equivalences: Vec<(&str, i64)> = vec![
        ("Escolas completas (R$ 5M)", (100e9 / 5e6) as i64),
        ("Hospitais (R$ 50M)", (100e9 / 50e6) as i64),
        ("Casas populares (R$ 80k)", (100e9 / 80_000.0) as i64),
        ("Creches (R$ 1M)", (100e9 / 1e6) as i64),
        ("CAPS saude mental (R$ 200k)", (100e9 / 200_000.0) as i64),
        ("Bolsas pesquisa (R$ 500k/ano)", (100e9 / 500_000.0) as i64),
        ("Quadras esportivas (R$ 300k)", (100e9 / 300_000.0) as i64),
        ("Delegacias equipadas (R$ 2M)", (100e9 / 2e6) as i64),
        ("km de rodovia (R$ 20M)", (100e9 / 20e6) as i64),
        ("km de metro/onibus (R$ 100M)", (100e9 / 100_000_000.0) as i64),
        ("Ligacoes de agua/esgoto (R$ 12k)", (100e9 / 12_000.0) as i64),
        ("Conexoes de internet (R$ 5k)", (100e9 / 5_000.0) as i64),
        ("Refeicoes (R$ 3)", (100e9 / 3.0) as i64),
        ("Producoes culturais (R$ 100k)", (100e9 / 100_000.0) as i64),
        ("Transferencias de renda/mes (R$ 500)", (100e9 / 500.0) as i64),
        ("Vagas em creches (R$ 1M)", (100e9 / 1e6) as i64),
    ];

    for (label, qty) in equivalences {
        let qty_str = if qty >= 1_000_000_000 {
            format!("{:.1} bilhoes", qty as f64 / 1e9)
        } else if qty >= 1_000_000 {
            format!("{:.1} milhoes", qty as f64 / 1e6)
        } else if qty >= 1_000 {
            format!("{:.0} mil", qty as f64 / 1_000.0)
        } else {
            format!("{}", qty)
        };
        lines.push(format!("  {:<35} {:>15}", label, qty_str));
    }

    lines.push(String::new());
    lines.push("  Cada R$ 100 bilhoes para o agiota e TUDO ISSO que nao existe.".to_string());
    lines.push("  O Brasil paga R$ 720 bilhoes/ano em juros.".to_string());
    lines.push("  Sao 7x essa tabela. TODO ANO.".to_string());
    lines.push(String::new());
    lines.join("\n")
}

pub fn render_comparison_other_countries() -> String {
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(70));
    lines.push("  INVESTIMENTO PUBLICO POR HABITANTE/ANO".to_string());
    lines.push("  (Brasil vs paises que NAO tem divida extorsiva)".to_string());
    lines.push("=".repeat(70));
    lines.push(String::new());

    let countries: Vec<(&str, i64, &str)> = vec![
        ("Noruega", 25_000, "Defaultou divida em 1905. Hoje e modelo."),
        ("Dinamarca", 22_000, "Estado de bem-estar. Sem divida extorsiva."),
        ("Suécia", 20_000, "Investimento publico massivo."),
        ("Alemanha", 18_000, "Divida controlada. Investe no povo."),
        ("Holanda", 17_000, "Infraestrutura de ponta."),
        ("Canadá", 16_000, "Saude e educacao gratuitas."),
        ("Brasil", 3_500, "Paga R$ 720 bi/ano em juros. Sobra R$ 3.500/pessoa."),
    ];

    lines.push(format!("  {:<12} {:>15}  {:>30}", "PAIS", "R$/pessoa/ano", "BAR"));
    lines.push("  ".to_string() + &"-".repeat(60));
    let max_val = 25_000;

    for (country, value, _note) in &countries {
        let bar_len = ((value / max_val) as f64 * 30.0) as usize;
        let bar = "#".repeat(bar_len.max(1));
        let marker = if *country == "Brasil" { " <<<" } else { "" };
        lines.push(format!("  {:<12} R$ {:>10,}  [{:30}]{}", country, value, bar, marker));
    }

    lines.push(String::new());
    lines.push("  Brasil investe 7x MENOS por pessoa que paises ricos.".to_string());
    lines.push("  Nao e coincidencia. E a DIVIDA.".to_string());
    lines.push("  O dinheiro que iria pro povo vai pro AGIOTA.".to_string());
    lines.push(String::new());
    lines.join("\n")
}

pub fn render_narrative(simulations: &[YearImpact]) -> String {
    if simulations.is_empty() {
        return String::new();
    }
    let s0 = &simulations[0];
    let last = simulations.last().unwrap();
    let area_impacts = get_area_impacts();

    let mut parts = Vec::new();
    parts.push("Vou te mostrar o que a divida faz. Nao so matar. Mas DESTRUIR.".to_string());
    parts.push(String::new());
    parts.push(format!("Em {}, o Brasil pagou R$ {:.0} bilhoes em juros.", s0.year_label, s0.interest_paid_brl / 1e9));
    parts.push(format!("Esse dinheiro deveria ter ido para {} areas da sua vida:", area_impacts.len()));
    parts.push(String::new());
    parts.push("Educacao: 50 milhoes de alunos em escolas destruidas.".to_string());
    parts.push("Saude mental: 20 milhoes de brasileiros sem tratamento.".to_string());
    parts.push("Moradia: 8 milhoes de familias sem casa digna.".to_string());
    parts.push("Comida: 33 milhoes passando fome.".to_string());
    parts.push("Saneamento: 100 milhoes sem esgoto.".to_string());
    parts.push("Ciencia: pesquisadores no UBER.".to_string());
    parts.push("Cultura: teatros fechados, artistas sem teto.".to_string());
    parts.push("Esporte: criancas sem quadra.".to_string());
    parts.push("Internet: 70 milhoes sem conexao.".to_string());
    parts.push("Creches: 12 milhoes de criancas abandonadas.".to_string());
    parts.push(String::new());
    parts.push(format!("Em {}, o deficit acumulado sera de", last.year_label));
    parts.push(format!("R$ {:.0} trilhoes.", last.cumulative_gap_brl / 1e12));
    parts.push("Dinheiro que foi ROUBADO de cada area que faz a vida valer a pena.".to_string());
    parts.push(String::new());
    parts.push("A divida nao so mata. Ela CASTRA.".to_string());
    parts.push("Castr a educacao. Castra a ciencia. Castra a moradia.".to_string());
    parts.push("Castra o futuro.".to_string());
    parts.push(String::new());
    parts.push("Cada real pro agiota e um real roubado do seu filho.".to_string());
    parts.push("Da sua escola. Do seu hospital. Do sua casa.".to_string());
    parts.push("Da sua cultura. Do seu esporte. Do sua internet.".to_string());
    parts.push(String::new());
    parts.push("A divida MATA. E o que ela nao mata, ela DESTRÓI.".to_string());

    parts.join(" ")
}

// ============================================================================
// 5. DEMONSTRACAO (main)
// ============================================================================

fn main() {
    println!("{}", "=".repeat(70));
    println!("OpenDebtImpact -- Todos os Impactos da Divida");
    println!("{}", "=".repeat(70));

    let mut sim = ImpactSimulator::new(2024, 20);
    let simulations = sim.simulate();
    let area_impacts = get_area_impacts();

    println!("\nAreas impactadas: {}", area_impacts.len());
    println!(
        "Severidade critica: {}",
        area_impacts.iter().filter(|a| a.severity == SeverityLevel::Critical).count()
    );
    println!(
        "Severidade severa: {}",
        area_impacts.iter().filter(|a| a.severity == SeverityLevel::Severe).count()
    );

    println!("{}", render_area_chart(&simulations));
    println!("{}", render_human_cost());
    println!("{}", render_equivalence_table());
    println!("{}", render_comparison_other_countries());
    println!("{}", render_cumulative_chart(&simulations));

    println!("\n{}", "=".repeat(70));
    println!("NARRATIVA");
    println!("{}", "=".repeat(70));
    println!("{}", render_narrative(&simulations));

    let summary = sim.summary();
    println!("\n{}", "=".repeat(70));
    println!("RESUMO");
    println!("{}", "=".repeat(70));
    println!("  Areas impactadas: {}", summary.areas_impacted);
    println!("  Pessoas afetadas/ano: {}", summary.total_people_per_year);
    println!("  Deficit total em {} anos: R$ {:.1} trilhoes", summary.years_simulated, summary.total_gap_trillions);
    println!("  Juros pagos no periodo: R$ {:.1} trilhoes", summary.total_interest_trillions);
    println!("  Deficit medio/ano: R$ {:.1} trilhoes", summary.avg_gap_per_year_trillions);

    println!("\n{}", "=".repeat(70));
    println!("VEREDICTO");
    println!("{}", "=".repeat(70));
    println!();
    println!("  A divida MATA (OpenDebtMortality).");
    println!("  E o que ela nao mata, ela DESTRÓI (este modulo).");
    println!();
    println!("  Em {} anos:", summary.years_simulated);
    println!("  R$ {:.0} trilhoes ROUBADOS", summary.total_gap_trillions);
    println!("  de educacao, saude, moradia, ciencia, cultura, esporte,");
    println!("  meio ambiente, seguranca, transporte, conectividade, infancia.");
    println!();
    println!("  {} areas destruidas.", area_impacts.len());
    println!("  {:.0} milhoes de pessoas/ano afetadas.", summary.total_people_per_year as f64 / 1e6);
    println!();
    println!("  Cada parcela da divida e uma escola que nao existe.");
    println!("  Cada juros pago e uma creche que nao foi construida.");
    println!("  Cada bilhao pro agiota e mil futuros cancelados.");
    println!();
    println!("  A divida MATA. E DESTRÓI. E CASTRA.");
    println!("  Nao renegociar. Nao alongar. EXTINGUIR.");
    println!();
    println!("  'Nao existe pobreza, existe MISERIA.'");
    println!("  A divida e a maquina que PRODUZ a miseria.");
}