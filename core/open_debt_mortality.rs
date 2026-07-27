// OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?
// ==========================================================
// "Cada R$ 1 bilhao pago em juros e:
// - 2 hospitais que nao foram construidos
// - 50 mil casas populares que nao foram entregues
// - 200 mil cestas de comida que nao foram distribuidas
// - 10 mil bolsas universitarias que nao foram concedidas
//
// E esses hospitais, casas, comidas e bolsas que NAO EXISTEM
// porque o dinheiro foi pro agiota -- essas sao as PESSOAS que morrem.
//
// O juros da divida MATA. MATA de forma invisivel.
// Nao e uma bala. E a AUSENCIA de um medico.
// Nao e uma faca. E a AUSENCIA de comida na mesa.
// Nao e um tiro. E a AUSENCIA de saneamento basico.
//
// Este modulo calcula, ano a ano, quantas pessoas MORREM
// no Brasil porque o dinheiro que deveria salvar suas vidas
// foi enviado para o agiota international como 'juros da divida'.
//
// METODOLOGIA:
// - Calcular juros pagos por ano (R$ bilhoes)
// - Calcular quanto disso deveria ir para saude, comida, saneamento
// - Calcular mortes evitaveis por falta de cada recurso
// - Comparar: se nao pagasse a divida, quantas vidas seriam salvas?
//
// AS MORTES NAO SAO ABSTRATAS. SAO NOMES. SAO CRIANCAS.
// Sao os 124 mil brasileiros que morrem por ano por causas evitaveis
// no SUS subfinanciado. Sao as criancas desnutridas no Nordeste.
// Sao os idosos sem atendimento na fila do SUS.
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// ============================================================================

use std::collections::HashMap;

// ============================================================================
// 1. CAUSAS DE MORTE EVITAVEIS (vinculadas a subfinanciamento)
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum PreventableDeathCategory {
    /// morreu na fila do SUS
    HealthcareShortage,
    /// bebe nao sobreviveu
    ChildMortality,
    /// mae morreu no parto
    MaternalDeath,
    /// morreu de fome
    Malnutrition,
    /// vacina/exame nao chegou
    PreventableDisease,
    /// sem programa social
    Violence,
    /// sem saude mental
    Suicide,
    /// agua contaminada
    Sanitation,
    /// estrada sem manutencao
    RoadDeath,
    /// sem teto/climatizacao
    HeatCold,
    /// sem tratamento
    DrugOverdose,
    /// fila de quimio
    CancerUntreated,
    /// sem UTI
    HeartUntreated,
    /// sem UTI neonatal
    Neonatal,
}

#[derive(Debug, Clone)]
pub struct DeathCost {
    pub category: PreventableDeathCategory,
    pub name: String,
    /// quanto custa prevenir UMA morte
    pub cost_to_save_one_life_brl: f64,
    /// mortes/ano no Brasil hoje
    pub deaths_per_year_brazil: i32,
    /// % que seria evitada com dinheiro
    pub pct_linked_to_underfunding: f64,
    pub description: String,
}

impl DeathCost {
    /// Mortes que DA pra evitar com investimento.
    pub fn deaths_preventable(&self) -> i32 {
        (self.deaths_per_year_brazil as f64 * self.pct_linked_to_underfunding) as i32
    }

    /// Quantas vidas R$ 1 bilhao salva nesta categoria.
    pub fn lives_saved_per_billion(&self) -> f64 {
        if self.cost_to_save_one_life_brl <= 0.0 {
            return 0.0;
        }
        1_000_000_000.0 / self.cost_to_save_one_life_brl
    }
}

// ============================================================================
// 2. TABELA DE MORTALIDADE (Dados baseados em OMS/IBGE/Datasus)
// ============================================================================

pub const DEATH_COSTS: [DeathCost; 12] = [
    DeathCost {
        category: PreventableDeathCategory::HealthcareShortage,
        name: String::from("Morte na fila do SUS"),
        cost_to_save_one_life_brl: 500_000.0,
        deaths_per_year_brazil: 124_000,
        pct_linked_to_underfunding: 0.60,
        description: String::from("Pessoas que morrem esperando cirurgia, exame, consulta, UTI."),
    },
    DeathCost {
        category: PreventableDeathCategory::ChildMortality,
        name: String::from("Mortalidade infantil (0-5 anos)"),
        cost_to_save_one_life_brl: 80_000.0,
        deaths_per_year_brazil: 40_000,
        pct_linked_to_underfunding: 0.70,
        description: String::from("Criancas que morrem antes dos 5 anos por falta de atendimento."),
    },
    DeathCost {
        category: PreventableDeathCategory::MaternalDeath,
        name: String::from("Morte materna (no parto)"),
        cost_to_save_one_life_brl: 50_000.0,
        deaths_per_year_brazil: 1_800,
        pct_linked_to_underfunding: 0.80,
        description: String::from("Maes que morrem no parto por falta de estrutura hospitalar."),
    },
    DeathCost {
        category: PreventableDeathCategory::Malnutrition,
        name: String::from("Desnutricao"),
        cost_to_save_one_life_brl: 15_000.0,
        deaths_per_year_brazil: 5_000,
        pct_linked_to_underfunding: 0.90,
        description: String::from("Pessoas que morrem de fome ou desnutricao grave no Brasil."),
    },
    DeathCost {
        category: PreventableDeathCategory::PreventableDisease,
        name: String::from("Doencas evitaveis (vacina/exame)"),
        cost_to_save_one_life_brl: 20_000.0,
        deaths_per_year_brazil: 50_000,
        pct_linked_to_underfunding: 0.65,
        description: String::from("Mortes por doencas que vacina ou exame precoce previniria."),
    },
    DeathCost {
        category: PreventableDeathCategory::Violence,
        name: String::from("Violencia / Homicidio"),
        cost_to_save_one_life_brl: 300_000.0,
        deaths_per_year_brazil: 47_000,
        pct_linked_to_underfunding: 0.40,
        description: String::from("Jovens mortos por violencia. Programa social reduz 40%."),
    },
    DeathCost {
        category: PreventableDeathCategory::Suicide,
        name: String::from("Suicidio (sem saude mental)"),
        cost_to_save_one_life_brl: 100_000.0,
        deaths_per_year_brazil: 14_000,
        pct_linked_to_underfunding: 0.55,
        description: String::from("Pessoas que se matam por falta de atendimento psicologico."),
    },
    DeathCost {
        category: PreventableDeathCategory::Sanitation,
        name: String::from("Doenças por falta de saneamento"),
        cost_to_save_one_life_brl: 40_000.0,
        deaths_per_year_brazil: 8_000,
        pct_linked_to_underfunding: 0.85,
        description: String::from("Mortes por diarreia, leptospirose, hepatite por agua suja."),
    },
    DeathCost {
        category: PreventableDeathCategory::RoadDeath,
        name: String::from("Morte no transito"),
        cost_to_save_one_life_brl: 2_000_000.0,
        deaths_per_year_brazil: 30_000,
        pct_linked_to_underfunding: 0.35,
        description: String::from("Acidentes em estradas sem manutencao ou sinalizacao."),
    },
    DeathCost {
        category: PreventableDeathCategory::CancerUntreated,
        name: String::from("Cancer sem tratamento a tempo"),
        cost_to_save_one_life_brl: 800_000.0,
        deaths_per_year_brazil: 35_000,
        pct_linked_to_underfunding: 0.50,
        description: String::from("Pessoas que morrem esperando tratamento de cancer no SUS."),
    },
    DeathCost {
        category: PreventableDeathCategory::HeartUntreated,
        name: String::from("Infarto sem atendimento"),
        cost_to_save_one_life_brl: 600_000.0,
        deaths_per_year_brazil: 100_000,
        pct_linked_to_underfunding: 0.30,
        description: String::from("Infartos que UTI/SAMU salvaria se chegasse a tempo."),
    },
    DeathCost {
        category: PreventableDeathCategory::Neonatal,
        name: String::from("Morte neonatal"),
        cost_to_save_one_life_brl: 120_000.0,
        deaths_per_year_brazil: 19_000,
        pct_linked_to_underfunding: 0.65,
        description: String::from("Bebe que morre nos primeiros 28 dias por falta de UTI neonatal."),
    },
];

// ============================================================================
// 3. SIMULACAO ANO A ANO
// ============================================================================

#[derive(Debug, Clone)]
pub struct YearMortality {
    pub year_label: i32,
    /// juros pagos no ano
    pub interest_paid_brl: f64,
    /// PIB do ano
    pub gdp_brl: f64,

    /// total de mortes evitaveis no ano
    pub total_preventable_deaths: i32,
    /// mortes por falta do dinheiro que foi pro juros
    pub deaths_linked_to_debt: i32,

    /// vidas que o juros salvaria se investido
    pub potential_lives_saved: i32,
    /// hospitais que nao foram construidos
    pub hospitals_not_built: i32,
    /// pessoas sem medico
    pub people_without_doctor: i32,
    /// criancas sem vacina
    pub children_not_vaccinated: i32,
    /// casas populares nao construidas
    pub houses_not_built: i32,
    /// refeicoes nao servidas
    pub meals_not_served: i32,

    /// mortes acumuladas pela divida
    pub cumulative_deaths_by_debt: i32,
}

pub struct DebtMortalitySimulator {
    pub start_year: i32,
    pub years: i32,
    pub initial_debt: f64,
    pub initial_gdp: f64,
    pub interest_rate: f64,
    pub gdp_growth: f64,
    pub population: f64,

    /// 40% do juros iria pra saude
    pub fraction_to_health: f64,
    /// 15% iria pra comida
    pub fraction_to_food: f64,
    /// 15% iria pra moradia
    pub fraction_to_housing: f64,
    /// 15% iria pra educacao
    pub fraction_to_education: f64,
    /// 15% iria pra infraestrutura
    pub fraction_to_infra: f64,

    pub simulations: Vec<YearMortality>,
}

impl DebtMortalitySimulator {
    pub fn new(start_year: i32, years: i32) -> Self {
        DebtMortalitySimulator {
            start_year,
            years,
            initial_debt: 6.0e12,
            initial_gdp: 10.0e12,
            interest_rate: 0.12,
            gdp_growth: 0.025,
            population: 215e6,
            fraction_to_health: 0.40,
            fraction_to_food: 0.15,
            fraction_to_housing: 0.15,
            fraction_to_education: 0.15,
            fraction_to_infra: 0.15,
            simulations: Vec::new(),
        }
    }

    /// Roda a simulacao ano a ano.
    pub fn simulate(&mut self) -> Vec<YearMortality> {
        self.simulations.clear();
        let mut debt = self.initial_debt;
        let mut gdp = self.initial_gdp;
        let mut cumulative_deaths = 0;

        for i in 0..=self.years {
            let year_label = self.start_year + i;

            let interest = debt * self.interest_rate;
            let money_for_health = interest * self.fraction_to_health;
            let money_for_food = interest * self.fraction_to_food;

            // Calcular vidas que poderiam ser salvas com o dinheiro da saude
            let mut potential_saved = 0;
            for dc in &DEATH_COSTS {
                let lives_saved = money_for_health * 0.3 / dc.cost_to_save_one_life_brl;
                potential_saved += lives_saved as i32;
            }

            // Total de mortes evitaveis no ano (base OMS)
            let total_preventable: i32 = DEATH_COSTS.iter().map(|dc| dc.deaths_preventable()).sum();

            // Mortes pela divida = o que NAO foi salvo por falta de dinheiro
            let deaths_by_debt = std::cmp::min(potential_saved, total_preventable);

            // O que mais nao foi feito
            let hospitals_not_built = (money_for_health / 50e6) as i32;
            let people_without_doctor = (money_for_health / 3_000.0) as i32;
            let children_not_vaccinated = (money_for_health / 50.0) as i32;
            let houses_not_built = ((interest * self.fraction_to_housing) / 80_000.0) as i32;
            let meals_not_served = (money_for_food / 3.0) as i32;

            cumulative_deaths += deaths_by_debt;

            let sim = YearMortality {
                year_label,
                interest_paid_brl: interest,
                gdp_brl: gdp,
                total_preventable_deaths: total_preventable,
                deaths_linked_to_debt: deaths_by_debt,
                potential_lives_saved: potential_saved,
                hospitals_not_built,
                people_without_doctor,
                children_not_vaccinated,
                houses_not_built,
                meals_not_served,
                cumulative_deaths_by_debt: cumulative_deaths,
            };
            self.simulations.push(sim);

            // Proximo ano
            debt = debt + interest - (gdp * 0.18 * 0.3);
            gdp = gdp * (1.0 + self.gdp_growth);
        }
        self.simulations.clone()
    }

    /// Total de mortes acumuladas em todos os anos simulados.
    pub fn total_deaths_by_debt(&self) -> i32 {
        if let Some(last) = self.simulations.last() {
            last.cumulative_deaths_by_debt
        } else {
            0
        }
    }

    /// Total de juros pagos em todos os anos.
    pub fn total_interest_paid(&self) -> f64 {
        self.simulations.iter().map(|s| s.interest_paid_brl).sum()
    }

    /// Mortes por R$ 1 trilhao de juros pagos.
    pub fn death_per_trillion_interest(&self) -> f64 {
        let total_int = self.total_interest_paid();
        if total_int == 0.0 {
            return 0.0;
        }
        self.total_deaths_by_debt() as f64 / (total_int / 1e12)
    }

    /// Resumo da simulacao.
    pub fn summary(&self) -> HashMap<String, f64> {
        let last = self.simulations.last();
        let mut map = HashMap::new();
        map.insert("years_simulated".to_string(), self.years as f64);
        map.insert("total_deaths_by_debt".to_string(), self.total_deaths_by_debt() as f64);
        map.insert("total_interest_paid_trillions".to_string(), self.total_interest_paid() / 1e12);
        map.insert("deaths_per_trillion_interest".to_string(), self.death_per_trillion_interest());
        map.insert("avg_deaths_per_year".to_string(), self.total_deaths_by_debt() as f64 / std::cmp::max(1, self.years) as f64);
        if let Some(l) = last {
            map.insert("final_year_hospitals_not_built".to_string(), l.hospitals_not_built as f64);
            map.insert("final_year_meals_not_served".to_string(), l.meals_not_served as f64);
            map.insert("final_year_children_not_vaccinated".to_string(), l.children_not_vaccinated as f64);
        }
        map
    }
}

// ============================================================================
// 4. QUEM O BRASIL PAGA (paises credores)
// ============================================================================

#[derive(Debug, Clone)]
pub struct CountryCreditor {
    pub country: String,
    /// quanto recebe por ano em juros
    pub amount_received_brl: f64,
    pub flag: String,
    pub description: String,
}

pub const COUNTRY_CREDITORS: [CountryCreditor; 10] = [
    CountryCreditor {
        country: String::from("Estados Unidos"),
        amount_received_brl: 180e9,
        flag: String::from("EUA"),
        description: String::from("Fundos de investimento e bancos americanos recebem bilhoes em juros."),
    },
    CountryCreditor {
        country: String::from("Reino Unido"),
        amount_received_brl: 80e9,
        flag: String::from("UK"),
        description: String::from("Londres e centro de vulture funds que lucram com divida alheia."),
    },
    CountryCreditor {
        country: String::from("Alemanha"),
        amount_received_brl: 50e9,
        flag: String::from("DE"),
        description: String::from("Bancos alemaes detem titulos brasileiros."),
    },
    CountryCreditor {
        country: String::from("Japao"),
        amount_received_brl: 40e9,
        flag: String::from("JP"),
        description: String::from("Fundos japoneses investem em divida soberana."),
    },
    CountryCreditor {
        country: String::from("Franca"),
        amount_received_brl: 35e9,
        flag: String::from("FR"),
        description: String::from("Bancos franceses (BNP, SocGen) detem titulos."),
    },
    CountryCreditor {
        country: String::from("Suica"),
        amount_received_brl: 30e9,
        flag: String::from("CH"),
        description: String::from("Centro de banca privada que lucra com juros."),
    },
    CountryCreditor {
        country: String::from("China"),
        amount_received_brl: 25e9,
        flag: String::from("CN"),
        description: String::from("Bancos chineses compraram titulos brasileiros."),
    },
    CountryCreditor {
        country: String::from("Holanda"),
        amount_received_brl: 20e9,
        flag: String::from("NL"),
        description: String::from("Centro financeiro (Amsterda) roteia investimentos."),
    },
    CountryCreditor {
        country: String::from("Luxemburgo"),
        amount_received_brl: 15e9,
        flag: String::from("LU"),
        description: String::from("Paraiso fiscal que abriga fundos especulativos."),
    },
    CountryCreditor {
        country: String::from("Outros"),
        amount_received_brl: 25e9,
        flag: String::from("??"),
        description: String::from("Outros paises e fundos internacionais."),
    },
];

// ============================================================================
// 5. RENDERIZACOES VISUAIS
// ============================================================================

/// Grafico ASCII: mortes por ano por causa da divida.
pub fn render_death_chart(simulations: &[YearMortality]) -> String {
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(70));
    lines.push("  MORTES POR ANO CAUSADAS PELA DIVIDA".to_string());
    lines.push("  (pessoas que morreriam VIVAS se o juros fosse investido em saude)".to_string());
    lines.push("=".repeat(70));
    lines.push(String::new());

    let max_deaths = simulations.iter().map(|s| s.deaths_linked_to_debt).max().unwrap_or(1).max(1);

    for s in simulations {
        let bar_len = ((s.deaths_linked_to_debt as f64 / max_deaths as f64) * 50.0) as usize;
        let bar = "#".repeat(bar_len.max(1));
        lines.push(format!("  {} |{:<50}| {:>8,} mortes", s.year_label, bar, s.deaths_linked_to_debt));
    }

    lines.push(String::new());
    lines.push(format!("  Cada # representa ~{} mortes", max_deaths / 50));
    if let Some(last) = simulations.last() {
        lines.push(format!("  TOTAL ACUMULADO: {:,} mortes", last.cumulative_deaths_by_debt));
        lines.push(format!("  em {} anos", simulations.len() - 1));
    }
    lines.push(String::new());
    lines.join("\n")
}

/// Mostra quanto cada pais credor recebe e quantas mortes causa.
pub fn render_country_deaths() -> String {
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(70));
    lines.push("  PARA QUEM O BRASIL PAGA -- E QUANTOS MORREM POR ISSO".to_string());
    lines.push("=".repeat(70));
    lines.push(String::new());

    let total_received: f64 = COUNTRY_CREDITORS.iter().map(|c| c.amount_received_brl).sum();

    for c in &COUNTRY_CREDITORS {
        let pct = (c.amount_received_brl / total_received) * 100.0;
        let deaths_caused = (c.amount_received_brl / 500_000.0) as i32;
        let bar_len = pct as usize;
        let bar = "$".repeat(bar_len);
        lines.push(format!(
            "  {:15} R$ {:>6.0} bi/ano [{}] {:>5.1}%  ~{} mortes",
            c.country, c.amount_received_brl / 1e9, bar, pct, deaths_caused
        ));
    }

    lines.push(String::new());
    lines.push(format!("  TOTAL ENVIADO AO EXTERIOR: R$ {:.0} bilhoes/ano", total_received / 1e9));
    lines.push(format!("  MORTES CAUSADAS: ~{} por ano", (total_received / 500_000.0) as i32));
    lines.push(format!("  Cada $ = R$ {:.0} bilhoes que sai do Brasil", total_received / 20.0 / 1e9));
    lines.push(String::new());
    lines.push("  Cada real enviado ao agiota international e uma vida".to_string());
    lines.push("  que NAO foi salva no Brasil.".to_string());
    lines.push(String::new());
    lines.join("\n")
}

/// Detalha as mortes por categoria.
pub fn render_category_breakdown() -> String {
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(70));
    lines.push("  MORTES EVITAVEIS NO BRASIL (por categoria, por ano)".to_string());
    lines.push("=".repeat(70));
    lines.push(String::new());

    let total_preventable: i32 = DEATH_COSTS.iter().map(|dc| dc.deaths_preventable()).sum();

    lines.push(format!("{:40} {:>12} {:>15} {:>12}", "CATEGORIA", "MORTES/ANO", "CUSTO/VIDA", "EVITAVEIS"));
    lines.push("-".repeat(80));

    for dc in &DEATH_COSTS {
        lines.push(format!(
            "  {:38} {:>10,} R$ {:>12,.0} {:>10,}",
            dc.name, dc.deaths_per_year_brazil, dc.cost_to_save_one_life_brl, dc.deaths_preventable()
        ));
    }

    lines.push("-".repeat(80));
    let sum_deaths: i32 = DEATH_COSTS.iter().map(|dc| dc.deaths_per_year_brazil).sum();
    lines.push(format!("  {:38} {:>10,} {:>15} {:>10,}", "TOTAL", sum_deaths, "", total_preventable));

    lines.push(String::new());
    lines.push(format!("  Total de mortes evitaveis/ano: {}", total_preventable));
    lines.push(format!("  Isso e {:.0} mortes POR DIA.", total_preventable as f64 / 365.0));
    lines.push(format!("  {:.0} mortes POR HORA.", total_preventable as f64 / 365.0 / 24.0));
    lines.push(format!("  {:.1} mortes POR MINUTO.", total_preventable as f64 / 365.0 / 24.0 / 60.0));
    lines.push(String::new());
    lines.push("  UMA PESSOA MORRE NO BRASIL A CADA MINUTO".to_string());
    lines.push("  POR ALGO QUE DINHEIRO RESOLVERIA.".to_string());
    lines.push(String::new());
    lines.push("  E o dinheiro? FOI PRA O AGIOTA.".to_string());
    lines.push(String::new());
    lines.join("\n")
}

/// O que NAO foi construido porque o dinheiro foi pro juros.
pub fn render_lost_infrastructure(simulations: &[YearMortality]) -> String {
    if simulations.is_empty() {
        return String::new();
    }
    let s = &simulations[0];
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(70));
    lines.push("  O QUE O BRASIL NAO CONSTRUIU EM UM ANO".to_string());
    lines.push(format!("  ({} -- R$ {:.0} bi em juros)", s.year_label, s.interest_paid_brl / 1e9));
    lines.push("=".repeat(70));
    lines.push(String::new());
    lines.push(format!("  Hospitais nao construidos:        {:>8,}", s.hospitals_not_built));
    lines.push(format!("  Casas populares nao entregues:    {:>8,}", s.houses_not_built));
    lines.push(format!("  Pessoas sem medico de familia:    {:>8,}", s.people_without_doctor));
    lines.push(format!("  Criancas nao vacinadas:            {:>8,}", s.children_not_vaccinated));
    lines.push(format!("  Refeicoes nao servidas:            {:>8,}", s.meals_not_served));
    lines.push(String::new());
    lines.push("  Em UM ano, o juros da divida pagou:".to_string());
    lines.push(format!("  - {} hospitais QUE NAO EXISTEM", s.hospitals_not_built));
    lines.push(format!("  - {} casas QUE NAO FORAM ENTREGUES", s.houses_not_built));
    lines.push(format!("  - {} refeicoes QUE NAO FORAM SERVIDAS", s.meals_not_served));
    lines.push(String::new());
    lines.push("  Cada hospital que nao existe = pessoas que morrem na fila.".to_string());
    lines.push("  Cada casa que nao foi entregue = familias na rua.".to_string());
    lines.push("  Cada refeicao que nao foi servida = criancas desnutridas.".to_string());
    lines.push(String::new());
    lines.join("\n")
}

/// Linha do tempo humanizada.
pub fn render_timeline_human(simulations: &[YearMortality]) -> String {
    let mut lines = Vec::new();
    lines.push(String::new());
    lines.push("=".repeat(70));
    lines.push("  LINHA DO TEMPO DA MORTE".to_string());
    lines.push("=".repeat(70));
    lines.push(String::new());

    for s in simulations {
        let deaths_per_day = s.deaths_linked_to_debt as f64 / 365.0;
        lines.push(format!("  {}:", s.year_label));
        lines.push(format!("    Juros pago: R$ {:.0} bilhoes", s.interest_paid_brl / 1e9));
        lines.push(format!("    Mortes causadas pela divida: {}", s.deaths_linked_to_debt));
        lines.push(format!("    Isso sao {:.0} mortes POR DIA", deaths_per_day));
        lines.push(format!("    Acumulado desde {}: {}", simulations[0].year_label, s.cumulative_deaths_by_debt));
        lines.push(String::new());
    }

    if let Some(last) = simulations.last() {
        lines.push(format!("  Em {} anos, a divida causou a morte de:", simulations.len() - 1));
        lines.push(format!("  {} PESSOAS.", last.cumulative_deaths_by_debt));
        lines.push(String::new());
        lines.push("  Isso e mais que a populacao de muitas cidades brasileiras.".to_string());
        lines.push("  Mais que todas as guerras do Brasil juntas.".to_string());
        lines.push("  Mais que todas as epidemias da historia recente.".to_string());
        lines.push(String::new());
        lines.push("  E nao foi uma bala. Foi um BOLETO.".to_string());
        lines.push(String::new());
    }
    lines.join("\n")
}

/// Narrativa para a Telefonista ler.
pub fn render_narrative(simulations: &[YearMortality]) -> String {
    if simulations.is_empty() {
        return String::new();
    }
    let s0 = &simulations[0];
    let last = simulations.last().unwrap();
    let total = last.cumulative_deaths_by_debt;

    let mut parts = Vec::new();
    parts.push("Vou te dizer algo que ninguem te conta.".to_string());
    parts.push(String::new());
    parts.push(format!("No ano {}, o Brasil pagou R$ {:.0} bilhoes", s0.year_label, s0.interest_paid_brl / 1e9));
    parts.push("apenas em JUROS da divida publica.".to_string());
    parts.push(String::new());
    parts.push("Esse dinheiro foi para bancos, fundos, paises estrangeiros.".to_string());
    parts.push("Nao foi para o SUS. Nao foi para a escola. Nao foi para a comida.".to_string());
    parts.push(String::new());
    parts.push(format!("No mesmo ano, {} brasileiros morreram", s0.deaths_linked_to_debt));
    parts.push("por causas evitaveis. Filas do SUS. Desnutricao. Falta de medico.".to_string());
    parts.push(String::new());
    parts.push(format!("Se o dinheiro dos juros tivesse ido para a saude,"));
    parts.push(format!("{} dessas pessoas poderiam estar VIVAS.", s0.potential_lives_saved));
    parts.push(String::new());
    parts.push(format!("Em {} anos, se nada mudar,", simulations.len() - 1));
    parts.push(format!("a divida tera causado a morte de {} pessoas.", total));
    parts.push(String::new());
    parts.push(format!("Sao {:.0} mortes por dia. A cada minuto, alguem morre", total as f64 / 365.0));
    parts.push("porque o dinheiro que salvaria sua vida foi para o agiota.".to_string());
    parts.push(String::new());
    parts.push("A divida nao e um numero. E um CEMITERIO.".to_string());
    parts.push("Cada parcela paga e uma cova que nao foi aberta.".to_string());
    parts.push("Cada juros pago e uma vida que nao foi salva.".to_string());
    parts.push(String::new());
    parts.push("A divida MATA.".to_string());
    parts.join(" ")
}

// ============================================================================
// 6. DEMONSTRACAO (main)
// ============================================================================

fn main() {
    println!("{}", "=".repeat(70));
    println!("OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?");
    println!("{}", "=".repeat(70));

    let mut sim = DebtMortalitySimulator::new(2024, 20);
    let simulations = sim.simulate();

    // Breakdown por categoria
    println!("{}", render_category_breakdown());

    // Para quem o Brasil paga
    println!("{}", render_country_deaths());

    // O que nao foi construido
    println!("{}", render_lost_infrastructure(&simulations));

    // Grafico de mortes por ano
    println!("{}", render_death_chart(&simulations));

    // Linha do tempo
    println!("{}", render_timeline_human(&simulations));

    // Narrativa
    println!("\n{}", "=".repeat(70));
    println!("NARRATIVA (para Telefonista ler)");
    println!("{}", "=".repeat(70));
    println!("{}", render_narrative(&simulations));

    // Resumo
    let summary = sim.summary();
    println!("\n{}", "=".repeat(70));
    println!("RESUMO");
    println!("{}", "=".repeat(70));
    println!("  Anos simulados: {}", summary["years_simulated"] as i32);
    println!("  Total de mortes pela divida: {}", summary["total_deaths_by_debt"] as i32);
    println!("  Total de juros pagos: R$ {:.1} trilhoes", summary["total_interest_paid_trillions"]);
    println!("  Mortes por R$ 1 trilhao de juros: {}", summary["deaths_per_trillion_interest"] as i32);
    println!("  Media de mortes/ano: {}", summary["avg_deaths_per_year"] as i32);

    println!("\n{}", "=".repeat(70));
    println!("VEREDICTO");
    println!("{}", "=".repeat(70));
    println!();
    println!("  A divida publica nao e apenas impossivel de pagar.");
    println!("  Ela e um ASSASSINO DE MASSA silencioso.");
    println!();
    println!("  Em {} anos:", summary["years_simulated"] as i32);
    println!("  {} brasileiros morreram", summary["total_deaths_by_debt"] as i32);
    println!("  porque R$ {:.1} trilhoes", summary["total_interest_paid_trillions"]);
    println!("  foram enviados ao agiota em vez de ir para saude, comida, vida.");
    println!();
    println!("  A divida MATA.");
    println!("  Cada juros pago e uma vida nao salva.");
    println!("  Nao renegociar. Nao alongar.");
    println!("  EXTINGUIR.");
    println!("  Pelas vidas que ainda podem ser salvas.");
    println!();
    println!("  'Nao existe pobreza, existe MISERIA.'");
    println!("  A divida e a maquina que PRODUZ a miseria.");
}