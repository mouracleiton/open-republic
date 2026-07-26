// OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota
// ===================================================================
// "O agiota diz: 'Se nao pagar, acabo com voce.'
// O pais ouve e paga. E paga. E paga. E nunca quita.
// Mas o que ACONTECE se parar de pagar? De verdade?
// O agiota grita. O mercado assusta. A midia apavora.
// E depois? O sol nasce. O pais existe. O povo continua.
// E o dinheiro que ia pro agiota vai pro povo."
//
// Este modulo simola ano a ano o que acontece quando um pais
// DECIDE PARAR DE PAGAR a divida. Mostra:
//
// 1. O ANO ZERO: o pais anuncia que nao vai pagar
// 2. O CHOQUE: panico, midia, agiotas gritando
// 3. A QUEDA: desvalorizacao, inflacao, recessao
// 4. A RECUPERACAO: sem juros, dinheiro sobra
// 5. A EXPLOSAO: investimento em povo, PIB dispara
// 6. O RESULTADO: pais rico vs pais escravo da divida
//
// O AGIOTA quem e:
// - Fundos de investimento (que compraram titulos por 30 centavos)
// - Bancos internacionais (que emprestaram criando dinheiro do nada)
// - FMI (que empresta para continuar pagando -- pau de se batr ate morrer)
// - Especuladores (que apostam NO nao-pagamento)
// - Bancada do capital financeiro (politicos a servico do agiota)
//
// O AGIOTA NAO E:
// - O povo brasileiro (que sofre pagando)
// - O trabalhador (que nao ve o dinheiro)
// - O idoso (cuidando das proprias contas)
// - A empresa produtiva (que paga imposto)
//
// CENARIO COMPARATIVO:
// - Caminho A: Continua pagando (OpenDebtAbolition prova que nunca acaba)
// - Caminho B: PARA de pagar (este modulo simula as consequencias)
//
// PRINCIPIO: O agiota so tem poder se voce tiver medo.
// O medo e a arma. A verdade e o antídoto.
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// ============================================================================

use std::collections::HashMap;

// ============================================================================
// 1. OS AGIOTAS (Quem e o credor)
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
pub enum CreditorType {
    NationalBonds,   // titulos_publicos -- 70% da divida -- mercado interno
    ForeignBanks,    // bancos_estrageiros -- bancos internacionais
    Imf,             // fmi -- Fundo Monetario
    ForeignBonds,    // titulos_externos -- dollar bonds
    PensionFunds,    // fundos_pensao -- fundos de pensao
    SovereignFunds,  // fundos_soberanos -- paises que compraram divida
    Speculators,     // especuladores -- vultures funds
    LocalBanks,      // bancos_locais -- bancos privados nacionais
    SupremeCourt,    // stf_judicial -- decisions judiciais que bloqueiam
}

impl CreditorType {
    pub fn value(&self) -> &'static str {
        match self {
            CreditorType::NationalBonds => "titulos_publicos",
            CreditorType::ForeignBanks => "bancos_estrageiros",
            CreditorType::Imf => "fmi",
            CreditorType::ForeignBonds => "titulos_externos",
            CreditorType::PensionFunds => "fundos_pensao",
            CreditorType::SovereignFunds => "fundos_soberanos",
            CreditorType::Speculators => "especuladores",
            CreditorType::LocalBanks => "bancos_locais",
            CreditorType::SupremeCourt => "stf_judicial",
        }
    }
}

#[derive(Debug, Clone)]
pub struct Creditor {
    pub creditor_id: String,
    pub name: String,
    pub creditor_type: CreditorType,
    pub amount_owed_brl: f64,      // quanto deve a ele
    pub owns_pct_of_total: f64,    // % da divida total
    pub origin_country: String,
    pub purchase_price_pct: f64,   // pagou quanto do valor nominal?
    pub real_risk: String,         // risco REAL para o pais se nao pagar
    pub bluffs: Vec<String>,       // o que ameaca
    pub real_consequence: String,  // o que REALMENTE acontece
    pub can_punish: bool,          // tem poder REAL de punir?
}

pub static CREDITORS: &[Creditor] = &[
    Creditor {
        creditor_id: "CR-001".to_string(),
        name: "Mercado de Titulos Internos (Tesouro Direto)".to_string(),
        creditor_type: CreditorType::NationalBonds,
        amount_owed_brl: 4.2e12,
        owns_pct_of_total: 70.0,
        origin_country: "Brasil".to_string(),
        purchase_price_pct: 0.95,
        real_risk: "baixo".to_string(),
        bluffs: vec![
            "Vai faltar dinheiro para tudo!".to_string(),
            "O sistema financeiro vai colapsar!".to_string(),
            "Ninguem vai mais emprestar pro Brasil!".to_string(),
        ],
        real_consequence: "Titulos sao renegociados. Investidores institucionais absorvem perda. O contribuinte brasileiro que injetou o dinheiro para pagar juros absurdos nao e responsavel por bancar especulador.".to_string(),
        can_punish: false,
    },
    Creditor {
        creditor_id: "CR-002".to_string(),
        name: "Fundos Especulativos (Vulture Funds)".to_string(),
        creditor_type: CreditorType::Speculators,
        amount_owed_brl: 300e9,
        owns_pct_of_total: 5.0,
        origin_country: "EUA/Reino Unido".to_string(),
        purchase_price_pct: 0.25, // compraram por 25 centavos!
        real_risk: "baixo".to_string(),
        bluffs: vec![
            "Vamos bloquear seus ativos no exterior!".to_string(),
            "Vamos processar na justica internacional!".to_string(),
            "Vamos confiscares as reservas!".to_string(),
            "Nenhum pais vai negociar com voce!".to_string(),
        ],
        real_consequence: "Compraram a divida por 25 centavos de dolar. Querem 100 centavos. O Brasil pode pagar 25 centavos e fechar. Vulture funds sao parasitas. O mercado ja precifica default.".to_string(),
        can_punish: false,
    },
    Creditor {
        creditor_id: "CR-003".to_string(),
        name: "FMI (Fundo Monetario Internacional)".to_string(),
        creditor_type: CreditorType::Imf,
        amount_owed_brl: 0.0,
        owns_pct_of_total: 0.0, // Brasil deve pouco ao FMI hoje
        origin_country: "Internacional".to_string(),
        purchase_price_pct: 1.0,
        real_risk: "baixo".to_string(),
        bluffs: vec![
            "Vamos impor austeridade!".to_string(),
            "Vamos bloquear credito internacional!".to_string(),
            "Vamos ditar sua politica economica!".to_string(),
        ],
        real_consequence: "FMI nao e deus. E um banco politico. Argentina deu calote em 2001 e 2014. Ainda existe. Grecia renegociou em 2012. Ainda existe. Islandia deu calote em 2008. Hoje e modelo.".to_string(),
        can_punish: false,
    },
    Creditor {
        creditor_id: "CR-004".to_string(),
        name: "Bancos Internacionais".to_string(),
        creditor_type: CreditorType::ForeignBanks,
        amount_owed_brl: 500e9,
        owns_pct_of_total: 8.0,
        origin_country: "EUA/Europa".to_string(),
        purchase_price_pct: 1.0,
        real_risk: "baixo".to_string(),
        bluffs: vec![
            "Vamos cortar linhas de credito!".to_string(),
            "Vai faltar dolar para importar!".to_string(),
            "Empresas estrangeiras vao fugir!".to_string(),
        ],
        real_consequence: "Bancos internacionais perderam dinheiro com EUA em 2008. Perderam com Grecia, Argentina, Russia, Turquia. Sempre voltam a emprestar -- porque ganham com risco. Spreads cobrem risco de default.".to_string(),
        can_punish: false,
    },
    Creditor {
        creditor_id: "CR-005".to_string(),
        name: "Fundos de Pensao Brasileiros".to_string(),
        creditor_type: CreditorType::PensionFunds,
        amount_owed_brl: 600e9,
        owns_pct_of_total: 10.0,
        origin_country: "Brasil".to_string(),
        purchase_price_pct: 1.0,
        real_risk: "baixo".to_string(),
        bluffs: vec![
            "Aposentados vao perder tudo!".to_string(),
            "Os fundos vao quebrar!".to_string(),
        ],
        real_consequence: "Fundos de pensao tem diversificacao. Renegociacao preserva o valor principal. Risco de nao receber juros extorsivos e diferente de perder tudo. O brasileiro aposentado ja perde com a inflacao que a divida causa.".to_string(),
        can_punish: false,
    },
    Creditor {
        creditor_id: "CR-006".to_string(),
        name: "Fundos Soberanos (Paises)".to_string(),
        creditor_type: CreditorType::SovereignFunds,
        amount_owed_brl: 200e9,
        owns_pct_of_total: 3.0,
        origin_country: "China/Oriente Medio".to_string(),
        purchase_price_pct: 1.0,
        real_risk: "baixo".to_string(),
        bluffs: vec![
            "Vamos parar de investir no Brasil!".to_string(),
            "Vamos cortar relacoes comerciais!".to_string(),
        ],
        real_consequence: "Paises investem por interesse, nao por amizade. Brasil tem commodities que o mundo precisa. China continua comprando soja independentemente de divida.".to_string(),
        can_punish: false,
    },
];

// ============================================================================
// 2. FASES DO DEFAULT (O Que Acontece Ano a Ano)
// ============================================================================

#[derive(Debug, Clone, PartialEq)]
pub enum DefaultPhase {
    PreDefault,   // pre_calote -- antes de parar de pagar
    Announcement, // anuncio -- dia do anuncio
    Panic,        // panico -- primeiro choque (semanas)
    Shock,        // choque -- consequencias imediatas (meses)
    Adjustment,   // ajuste -- pais se adapta (1-2 anos)
    Recovery,     // recuperacao -- economia volta (2-5 anos)
    Growth,       // crescimento -- dispara sem juros (5-10 anos)
    Prosperity,   // prosperidade -- rico sem divida (10+ anos)
}

impl DefaultPhase {
    pub fn value(&self) -> &'static str {
        match self {
            DefaultPhase::PreDefault => "pre_calote",
            DefaultPhase::Announcement => "anuncio",
            DefaultPhase::Panic => "panico",
            DefaultPhase::Shock => "choque",
            DefaultPhase::Adjustment => "ajuste",
            DefaultPhase::Recovery => "recuperacao",
            DefaultPhase::Growth => "crescimento",
            DefaultPhase::Prosperity => "prosperidade",
        }
    }
}

#[derive(Debug, Clone)]
pub struct YearSimulation {
    pub year: i32,
    pub year_label: i32,
    pub phase: DefaultPhase,

    // Caminho A: Continua pagando (escravo)
    pub pay_debt_brl: f64,
    pub pay_interest_brl: f64,
    pub pay_public_investment_brl: f64,
    pub pay_gdp_brl: f64,
    pub pay_gdp_per_capita: f64,
    pub pay_health_budget: f64,
    pub pay_education_budget: f64,
    pub pay_inflation: f64,
    pub pay_unemployment: f64,
    pub pay_poverty_pct: f64,

    // Caminho B: Parou de pagar (livre)
    pub nopay_debt_brl: f64,         // divida estagnada/renegociada
    pub nopay_interest_brl: f64,     // juros ZERO apos default
    pub nopay_freed_money_brl: f64,  // dinheiro liberado (ex-juros)
    pub nopay_public_investment_brl: f64,
    pub nopay_gdp_brl: f64,
    pub nopay_gdp_per_capita: f64,
    pub nopay_health_budget: f64,
    pub nopay_education_budget: f64,
    pub nopay_inflation: f64,
    pub nopay_unemployment: f64,
    pub nopay_poverty_pct: f64,

    // Diferenca
    pub gdp_gap: f64,           // quanto o Caminho B esta na frente
    pub cumulative_freed: f64,  // total liberado acumulado
    pub winner: String,         // "pagar" ou "nao_pagar"
}

// ============================================================================
// 3. MOTOR DE SIMULACAO DUAL
// ============================================================================

pub struct DefaultSimulator {
    pub start_year: i32,
    pub years: i32,

    // Parametros base
    pub initial_debt: f64,       // R$ 6T
    pub initial_gdp: f64,        // R$ 10T
    pub interest_rate: f64,      // 12%
    pub gdp_growth_normal: f64,  // 2.5%
    pub population: f64,
    pub revenue_pct_gdp: f64,    // arrecadacao 18% do PIB
    pub health_pct_budget: f64,  // saude 4% do PIB
    pub education_pct_budget: f64, // educacao 6% do PIB
    pub investment_pct_gdp: f64, // investimento publico 2%

    // Parametros do choque (default)
    pub default_currency_drop: f64,     // real cai 40% no choque
    pub default_inflation_spike: f64,   // inflacao sobe para 15% no ano 1
    pub default_recession: f64,         // PIB cai 4% no ano 1
    pub default_recovery_start: i32,    // ano 2 comeca a recuperar
    pub default_growth_boost: f64,      // crescimento sobe para 5%+ sem juros

    pub simulations: Vec<YearSimulation>,
}

impl DefaultSimulator {
    pub fn new(start_year: i32, years: i32) -> Self {
        DefaultSimulator {
            start_year,
            years,
            initial_debt: 6.0e12,
            initial_gdp: 10.0e12,
            interest_rate: 0.12,
            gdp_growth_normal: 0.025,
            population: 215e6,
            revenue_pct_gdp: 0.18,
            health_pct_budget: 0.04,
            education_pct_budget: 0.06,
            investment_pct_gdp: 0.02,
            default_currency_drop: 0.40,
            default_inflation_spike: 0.15,
            default_recession: -0.04,
            default_recovery_start: 2,
            default_growth_boost: 0.05,
            simulations: Vec::new(),
        }
    }

    pub fn simulate(&mut self) -> Vec<YearSimulation> {
        self.simulations.clear();

        let mut pay_debt = self.initial_debt;
        let mut pay_gdp = self.initial_gdp;
        let mut nopay_debt = self.initial_debt;
        let mut nopay_gdp = self.initial_gdp;
        let mut cumulative_freed = 0.0;

        for i in 0..=self.years {
            let year_label = self.start_year + i;

            // Determinar fase
            let phase = if i == 0 {
                DefaultPhase::Announcement
            } else if i <= 1 {
                DefaultPhase::Panic
            } else if i <= 2 {
                DefaultPhase::Shock
            } else if i <= 3 {
                DefaultPhase::Adjustment
            } else if i <= 7 {
                DefaultPhase::Recovery
            } else if i <= 15 {
                DefaultPhase::Growth
            } else {
                DefaultPhase::Prosperity
            };

            // ===== CAMINHO A: CONTINUA PAGANDO =====
            let pay_interest = pay_debt * self.interest_rate;
            let pay_revenue = pay_gdp * self.revenue_pct_gdp;
            let pay_primary = pay_revenue * 0.3; // 30% da receita vai pra divida
            let pay_investment = pay_gdp * self.investment_pct_gdp;
            let pay_health = pay_gdp * self.health_pct_budget;
            let pay_education = pay_gdp * self.education_pct_budget;

            let pay_inflation = 0.045 + (pay_debt / pay_gdp) * 0.01;
            let pay_unemployment = 0.09 + (pay_debt / pay_gdp) * 0.02;
            let pay_poverty = 0.25 + (pay_interest / pay_gdp) * 0.1;

            if i > 0 {
                pay_debt = pay_debt + pay_interest - pay_primary;
                pay_gdp = pay_gdp * (1.0 + self.gdp_growth_normal);
            }

            // ===== CAMINHO B: PAROU DE PAGAR =====
            let (nopay_interest, nopay_freed, nopay_inflation, nopay_unemployment, nopay_growth, mut nopay_debt_local) = if i == 0 {
                // DIA DO ANUNCIO
                let interest = nopay_debt * self.interest_rate;
                (interest, interest, self.default_inflation_spike * 0.3, 0.09, 0.0, nopay_debt)
            } else if i == 1 {
                // PANICO
                (0.0, pay_interest, self.default_inflation_spike, 0.12, self.default_recession, nopay_debt * 0.3)
            } else if i == 2 {
                // CHOQUE
                (0.0, pay_interest * 1.2, 0.08, 0.10, 0.01, nopay_debt)
            } else if i == 3 {
                // AJUSTE
                (0.0, pay_interest * 1.5, 0.05, 0.08, self.default_growth_boost * 0.6, nopay_debt)
            } else if i <= 7 {
                // RECUPERACAO
                (0.0, pay_interest * 2.0, 0.04, 0.06, self.default_growth_boost, nopay_debt)
            } else if i <= 15 {
                // CRESCIMENTO
                (0.0, pay_interest * 2.5, 0.035, 0.04, self.default_growth_boost * 1.3, nopay_debt)
            } else {
                // PROSPERIDADE
                (0.0, pay_interest * 3.0, 0.03, 0.035, self.default_growth_boost * 1.5, nopay_debt)
            };

            if i == 1 {
                nopay_debt = nopay_debt_local;
            }

            cumulative_freed += nopay_freed;

            if i > 0 {
                nopay_gdp = nopay_gdp * (1.0 + nopay_growth);
            }

            // Investimento publico sem juros = MASSIVO
            let nopay_revenue = nopay_gdp * self.revenue_pct_gdp;
            let nopay_investment = nopay_gdp * self.investment_pct_gdp + nopay_freed * 0.6;
            let nopay_health = nopay_gdp * self.health_pct_budget + nopay_freed * 0.15;
            let nopay_education = nopay_gdp * self.education_pct_budget + nopay_freed * 0.15;

            let mut nopay_poverty = if i > 1 { 0.25 - (i as f64 * 0.008) } else { 0.27 };
            if nopay_poverty < 0.03 { nopay_poverty = 0.03; }

            let pay_per_capita = pay_gdp / self.population;
            let nopay_per_capita = nopay_gdp / self.population;

            let gdp_gap = nopay_gdp - pay_gdp;

            let mut winner = if nopay_gdp > pay_gdp { "nao_pagar".to_string() } else { "pagar".to_string() };
            if i == 0 { winner = "igual".to_string(); }

            let sim = YearSimulation {
                year: i,
                year_label,
                phase,
                pay_debt_brl: pay_debt,
                pay_interest_brl: pay_interest,
                pay_public_investment_brl: pay_investment,
                pay_gdp_brl: pay_gdp,
                pay_gdp_per_capita: pay_per_capita,
                pay_health_budget: pay_health,
                pay_education_budget: pay_education,
                pay_inflation,
                pay_unemployment,
                pay_poverty_pct: pay_poverty,
                nopay_debt_brl: nopay_debt,
                nopay_interest_brl: nopay_interest,
                nopay_freed_money_brl: nopay_freed,
                nopay_public_investment_brl: nopay_investment,
                nopay_gdp_brl: nopay_gdp,
                nopay_gdp_per_capita: nopay_per_capita,
                nopay_health_budget: nopay_health,
                nopay_education_budget: nopay_education,
                nopay_inflation,
                nopay_unemployment,
                nopay_poverty_pct,
                gdp_gap,
                cumulative_freed,
                winner,
            };
            self.simulations.push(sim);
        }

        self.simulations.clone()
    }

    pub fn crossover_year(&self) -> Option<i32> {
        for sim in &self.simulations {
            if sim.year > 0 && sim.nopay_gdp_brl > sim.pay_gdp_brl {
                return Some(sim.year_label);
            }
        }
        None
    }

    pub fn final_comparison(&self) -> HashMap<String, f64> {
        let last = self.simulations.last().unwrap();
        let mut result = HashMap::new();
        result.insert("years_simulated".to_string(), self.years as f64);
        result.insert("crossover_year".to_string(), self.crossover_year().unwrap_or(0) as f64);
        result.insert("pay_final_gdp_trillions".to_string(), last.pay_gdp_brl / 1e12);
        result.insert("nopay_final_gdp_trillions".to_string(), last.nopay_gdp_brl / 1e12);
        result.insert("gdp_difference_trillions".to_string(), (last.nopay_gdp_brl - last.pay_gdp_brl) / 1e12);
        result.insert("gdp_advantage_pct".to_string(), ((last.nopay_gdp_brl / last.pay_gdp_brl) - 1.0) * 100.0);
        result.insert("pay_final_debt_trillions".to_string(), last.pay_debt_brl / 1e12);
        result.insert("nopay_final_debt_trillions".to_string(), last.nopay_debt_brl / 1e12);
        result.insert("total_freed_trillions".to_string(), last.cumulative_freed / 1e12);
        result.insert("pay_poverty_final".to_string(), last.pay_poverty_pct * 100.0);
        result.insert("nopay_poverty_final".to_string(), last.nopay_poverty_pct * 100.0);
        result.insert("pay_unemployment_final".to_string(), last.pay_unemployment * 100.0);
        result.insert("nopay_unemployment_final".to_string(), last.nopay_unemployment * 100.0);
        result.insert("winner".to_string(), if last.nopay_gdp_brl > last.pay_gdp_brl { 1.0 } else { 0.0 });
        result
    }
}

// ============================================================================
// 4. O QUE O AGIOTA DIZ vs O QUE ACONTECE
// ============================================================================

pub struct AgiotaTruthTable;

impl AgiotaTruthTable {
    pub const TRUTHS: [(&'static str, &'static str, &'static str); 10] = [
        (
            "O sistema financeiro vai colapsar!",
            "Bancos brasileiros sobreviveram a Hyperinflacao (80s), Plano Real (94), crise 2008. Sobrevivem a default.",
            "Argentina (2001, 2014), Islandia (2008), Grecia (2012), Russia (1998), Equador (2008). Todos existem.",
        ),
        (
            "Vai faltar comida!",
            "Brasil e um dos maiores produtores de alimentos do mundo. Default nao queima plantacao.",
            "Argentina deu calote e continua exportando carne e soja.",
        ),
        (
            "O dolar vai disparar!",
            "Dolar dispara por 6-12 meses. Depois estabiliza. Exportacoes ficam mais compencivel. Industria nacional renasce.",
            "Islandia: coroa islandesa caiu 50% em 2008. Recuperou e hoje tem menor desigualdade da Europa.",
        ),
        (
            "Inflacao vai explodir!",
            "Inflacao sobe por 1-2 anos. Mas a divida extinta REMOVE pressao fiscal permanente. Sem juros extorsivos, inflacao estrutural CAI.",
            "Equador (Correa): defaultou, inflacao caiu, pobreza despencou.",
        ),
        (
            "Ninguem vai mais emprestar!",
            "Mercados tem memoria curta. Argentina defaultou 9 vezes. Ainda emprestam. Risco paga premio.",
            "Russia foi banida em 2022. Sao titulos deram 15% ao ano. Gente comprou.",
        ),
        (
            "Vao confiscar reservas!",
            "Reservas estao protegidas por imunidade soberana. Vulture funds litigam por decadas e recebem fracoes.",
            "Argentina vs Elliott Management: 15 anos de processo. Recebeu 75% a mais -- mas so depois de 15 anos.",
        ),
        (
            "A democracia vai cair!",
            "Default nao derruba democracia. AUSTERIDADE para pagar divida derruba. Grecia quase caiu com Nazis (Aurora Dourada) por austeridade do FMI.",
            "Islandia: defaultou, PRESIDIU banqueiros, democracia mais forte.",
        ),
        (
            "Os pobres vao sofrer!",
            "Os pobres JA sofrem pagando R$ 500 bi/ano em juros. Default redireciona esse dinheiro para saude, educacao, moradia.",
            "Equador: pobreza caiu de 36% para 21% apos default de 2008.",
        ),
        (
            "As empresas vao falir!",
            "Empresas EXPORTADORAS ganham com moeda desvalorizada. Empresas ligadas a divida perdem. Mas o pais se reequilibra.",
            "Argentina: Mal do default e curto prazo. Em 3-5 anos, exportacao dispara.",
        ),
        (
            "O Brasil vai virar Venezuela!",
            "Venezuela quebrou por SANCOES, nao por default. Brasil tem reservas, producao, diversificacao. Analogia falsa.",
            "Equador, Islandia, Argentina -- nenhum virou Venezuela.",
        ),
    ];
}

// ============================================================================
// 5. SIMULACAO VISUAL
// ============================================================================

pub fn render_comparison_chart(simulations: &[YearSimulation]) -> String {
    let mut lines = Vec::new();
    lines.push("".to_string());
    lines.push("=".repeat(70));
    lines.push("  PIB: CONTINUA PAGANDO vs PARA DE PAGAR".to_string());
    lines.push("=".repeat(70));
    lines.push("".to_string());

    let max_gdp = simulations.iter().map(|s| s.pay_gdp_brl.max(s.nopay_gdp_brl)).fold(0.0, f64::max);
    let bar_width = 35;

    for s in simulations {
        let pay_bar_len = ((s.pay_gdp_brl / max_gdp) * bar_width as f64) as usize;
        let nopay_bar_len = ((s.nopay_gdp_brl / max_gdp) * bar_width as f64) as usize;

        let pay_bar = "P".repeat(pay_bar_len.max(1));
        let nopay_bar = "L".repeat(nopay_bar_len.max(1));

        let phase_marker = match s.phase {
            DefaultPhase::Panic => " [PANICO]",
            DefaultPhase::Shock => " [CHOQUE]",
            DefaultPhase::Recovery => " [RECUPERANDO]",
            DefaultPhase::Growth => " [DISPARANDO]",
            DefaultPhase::Prosperity => " [PRÓSPERO]",
            _ => "",
        };

        lines.push(format!("  {} PAGAR: [{}] R$ {:.1}T", s.year_label, format!("{:<width$}", pay_bar, width = bar_width), s.pay_gdp_brl / 1e12));
        lines.push(format!("  {:>4} LIVRE: [{}] R$ {:.1}T{}", "", format!("{:<width$}", nopay_bar, width = bar_width), s.nopay_gdp_brl / 1e12, phase_marker));
        lines.push("".to_string());
    }

    lines.push("  P = Continua pagando (escravo)".to_string());
    lines.push("  L = Para de pagar (livre)".to_string());
    lines.push("".to_string());
    lines.join("\n")
}

pub fn render_poverty_chart(simulations: &[YearSimulation]) -> String {
    let mut lines = Vec::new();
    lines.push("".to_string());
    lines.push("=".repeat(70));
    lines.push("  POBREZA (% DA POPULACAO): PAGAR vs NAO PAGAR".to_string());
    lines.push("=".repeat(70));
    lines.push("".to_string());

    for s in simulations {
        let pay_bar_len = (s.pay_poverty_pct * 50.0) as usize;
        let nopay_bar_len = (s.nopay_poverty_pct * 50.0) as usize;
        let pay_bar = "X".repeat(pay_bar_len);
        let nopay_bar = "O".repeat(nopay_bar_len);

        lines.push(format!("  {} PAGAR: [{}] {:.1}%", s.year_label, format!("{:<50}", pay_bar), s.pay_poverty_pct * 100.0));
        lines.push(format!("  {:>4} LIVRE: [{}] {:.1}%", "", format!("{:<50}", nopay_bar), s.nopay_poverty_pct * 100.0));
        lines.push("".to_string());
    }

    lines.push("  X = Pobreza pagando divida (estagnada/alta)".to_string());
    lines.push("  O = Pobreza sem pagar divida (desabando)".to_string());
    lines.push("".to_string());
    lines.join("\n")
}

pub fn render_truth_table() -> String {
    let mut lines = Vec::new();
    lines.push("".to_string());
    lines.push("=".repeat(70));
    lines.push("O AGIOTA DIZ vs O QUE REALMENTE ACONTECE".to_string());
    lines.push("=".repeat(70));

    for (i, (ameaca, realidade, exemplos)) in AgiotaTruthTable::TRUTHS.iter().enumerate() {
        lines.push("".to_string());
        lines.push(format!("  AMEACA {}: {}", i + 1, ameaca));
        lines.push(format!("  REALIDADE: {}", realidade));
        lines.push(format!("  PROVA: {}", exemplos));
        lines.push(format!("  {}", "-".repeat(66)));
    }

    lines.push("".to_string());
    lines.push("  O agiota so tem poder se voce tiver MEDO.".to_string());
    lines.push("  O medo e a arma dele. A verdade e o antidoto.".to_string());
    lines.push("".to_string());
    lines.join("\n")
}

pub fn render_creditors() -> String {
    let mut lines = Vec::new();
    lines.push("".to_string());
    lines.push("=".repeat(70));
    lines.push("QUEM E O AGIOTA?".to_string());
    lines.push("=".repeat(70));

    for c in CREDITORS {
        lines.push("".to_string());
        lines.push(format!("  {}", c.name));
        lines.push(format!("  Tipo: {}", c.creditor_type.value()));
        lines.push(format!("  Valor: R$ {:.0} bilhoes ({:.0}% da divida)", c.amount_owed_brl / 1e9, c.owns_pct_of_total));
        lines.push(format!("  Comprou por: {:.0} centavos de cada real", c.purchase_price_pct * 100.0));
        lines.push(format!("  Pode punir de verdade? {}", if !c.can_punish { "NAO" } else { "SIM" }));
        lines.push(format!("  O que diz: \"{}\"", c.bluffs[0]));
        lines.push(format!("  O que acontece: {}", c.real_consequence));
        lines.push("".to_string());
    }

    lines.push("  O agiota comprou por 25 centavos. Quer 100.".to_string());
    lines.push("  Paga 25. Fecha o livro. Fim do agiota.".to_string());
    lines.push("".to_string());
    lines.join("\n")
}

pub fn render_timeline(simulations: &[YearSimulation]) -> String {
    let mut lines = Vec::new();
    lines.push("".to_string());
    lines.push("=".repeat(70));
    lines.push("LINHA DO TEMPO: O QUE ACONTECE APOS PARAR DE PAGAR".to_string());
    lines.push("=".repeat(70));

    for (idx, s) in simulations.iter().enumerate() {
        lines.push("".to_string());
        lines.push(format!("  ANO {} ({}) -- FASE: {}", s.year, s.year_label, s.phase.value().to_uppercase()));

        match s.phase {
            DefaultPhase::Announcement => {
                lines.push("    O Brasil anuncia: NAO VAMOS PAGAR.".to_string());
                lines.push("    Agiotas gritam. Midia apavora. Bolsa cai.".to_string());
                lines.push("    Povo pergunta: 'E agora?'".to_string());
                lines.push("    Resposta: 'O sol nasce amanha.'".to_string());
            }
            DefaultPhase::Panic => {
                lines.push(format!("    PANICO. Dolar sobe. Inflacao {:.0}%.", s.nopay_inflation * 100.0));
                lines.push(format!("    Desemprego sobe para {:.0}%.", s.nopay_unemployment * 100.0));
                lines.push("    Agiotas processam. Midia diz 'Eu avisei!'.".to_string());
                lines.push(format!("    Mas: R$ {:.0} bi ANTES iam pro agiota.", s.nopay_freed_money_brl / 1e9));
                lines.push("    Agora vai para: saude, educacao, infraestrutura.".to_string());
            }
            DefaultPhase::Shock => {
                lines.push(format!("    AINDA DOLORIDO. Mas inflacao caindo: {:.0}%.", s.nopay_inflation * 100.0));
                lines.push("    PIB voltando a crescer.".to_string());
                lines.push(format!("    Investimento publico: R$ {:.0} bi", s.nopay_public_investment_brl / 1e9));
                lines.push(format!("    (vs R$ {:.0} bi se pagasse)", s.pay_public_investment_brl / 1e9));
            }
            DefaultPhase::Adjustment => {
                lines.push("    NOVO EQUILIBRIO. Sem juros, dinheiro sobe.".to_string());
                lines.push(format!("    Inflacao: {:.0}% (normalizando)", s.nopay_inflation * 100.0));
                lines.push(format!("    Desemprego: {:.0}% (caindo)", s.nopay_unemployment * 100.0));
                if idx > 0 {
                    let prev = &simulations[idx - 1];
                    let growth = ((s.nopay_gdp_brl / prev.nopay_gdp_brl) - 1.0) * 100.0;
                    lines.push(format!("    PIB crescendo {:.1}%", growth));
                }
            }
            DefaultPhase::Recovery => {
                lines.push("    RECUPERANDO. PIB acelerando.".to_string());
                lines.push(format!("    Pobreza: {:.1}% (vs {:.1}% pagando)", s.nopay_poverty_pct * 100.0, s.pay_poverty_pct * 100.0));
                lines.push(format!("    Dinheiro liberado acumulado: R$ {:.1} trilhoes", s.cumulative_freed / 1e12));
                lines.push(format!("    Saude: R$ {:.0} bi vs R$ {:.0} bi", s.nopay_health_budget / 1e9, s.pay_health_budget / 1e9));
            }
            DefaultPhase::Growth => {
                lines.push("    DISPARANDO. Sem divida, sem juros.".to_string());
                lines.push(format!("    PIB: R$ {:.1}T vs R$ {:.1}T (pagando)", s.nopay_gdp_brl / 1e12, s.pay_gdp_brl / 1e12));
                lines.push(format!("    Desemprego: {:.1}% (vs {:.1}%)", s.nopay_unemployment * 100.0, s.pay_unemployment * 100.0));
                lines.push(format!("    Diferenca acumulada: R$ {:.1} trilhoes a favor", s.gdp_gap / 1e12));
            }
            DefaultPhase::Prosperity => {
                lines.push("    PROSPERO. Pais livre da divida.".to_string());
                lines.push(format!("    PIB: R$ {:.1}T vs R$ {:.1}T", s.nopay_gdp_brl / 1e12, s.pay_gdp_brl / 1e12));
                lines.push(format!("    Pobreza: {:.1}% vs {:.1}%", s.nopay_poverty_pct * 100.0, s.pay_poverty_pct * 100.0));
                lines.push("    VEREDICTO: nao pagar VALEU A PENA.".to_string());
            }
            _ => {}
        }
    }

    lines.push("".to_string());
    lines.join("\n")
}

// ============================================================================
// 6. DEMONSTRACAO (main)
// ============================================================================

fn main() {
    println!("{}", "=".repeat(70));
    println!("OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota");
    println!("{}", "=".repeat(70));

    let mut sim = DefaultSimulator::new(2025, 20);
    let simulations = sim.simulate();

    // Quem e o agiota
    println!("{}", render_creditors());

    // Tabela verdade
    println!("{}", render_truth_table());

    // Grafico PIB
    println!("{}", render_comparison_chart(&simulations));

    // Grafico pobreza
    println!("{}", render_poverty_chart(&simulations));

    // Linha do tempo
    println!("{}", render_timeline(&simulations));

    // Resultado final
    let comparison = sim.final_comparison();
    let crossover = sim.crossover_year();

    println!("{}", "=".repeat(70));
    println!("RESULTADO FINAL APOS 20 ANOS");
    println!("{}", "=".repeat(70));
    println!("  CAMINHO A (continua pagando):");
    println!("    PIB final: R$ {:.1} trilhoes", comparison["pay_final_gdp_trillions"]);
    println!("    Divida final: R$ {:.1} trilhoes", comparison["pay_final_debt_trillions"]);
    println!("    Pobreza: {:.1}%", comparison["pay_poverty_final"]);
    println!("    Desemprego: {:.1}%", comparison["pay_unemployment_final"]);

    println!("\n  CAMINHO B (parou de pagar):");
    println!("    PIB final: R$ {:.1} trilhoes", comparison["nopay_final_gdp_trillions"]);
    println!("    Divida final: R$ {:.1} trilhoes", comparison["nopay_final_debt_trillions"]);
    println!("    Pobreza: {:.1}%", comparison["nopay_poverty_final"]);
    println!("    Desemprego: {:.1}%", comparison["nopay_unemployment_final"]);
    println!("    Dinheiro liberado (20 anos): R$ {:.1} trilhoes", comparison["total_freed_trillions"]);

    println!("\n  VANTAGEM DE NAO PAGAR:");
    println!("    PIB {:.0}% maior", comparison["gdp_advantage_pct"]);
    println!("    Diferenca: R$ {:.1} trilhoes", comparison["gdp_difference_trillions"]);
    println!("    Crossover (ano em que ultrapassa): {}", crossover.unwrap_or(0));

    println!("\n  VENCEDOR: {}", if comparison["winner"] > 0.5 { "NAO PAGAR" } else { "PAGAR" });

    println!("\n{}", "=".repeat(70));
    println!("CONCLUSAO");
    println!("{}", "=".repeat(70));
    println!();
    println!("  O agiota diz que e o fim do mundo se voce parar de pagar.");
    println!("  A simulacao mostra que em 3-5 anos o pais RECUPERA.");
    println!("  Em 10 anos, esta NA FRENTE.");
    println!("  Em 20 anos, e OUTRO PAIS.");
    println!();
    println!("  O curto prazo doi. O longo prazo liberta.");
    println!("  Continuar pagando doi PARA SEMPRE.");
    println!();
    println!("  O agiota so tem poder se voce tiver MEDO.");
    println!("  O medo e a arma. A verdade e o antidoto.");
    println!();
    println!("  'O Ideal guia. O Executavel opera.'");
}