# OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota

**Arquivo original:** `open-republic/core/open_debt_default.py`

**Descricao:** ===================================================================
"O agiota diz: 'Se nao pagar, acabo com voce.'
O pais ouve e paga. E paga. E paga. E nunca quita.
Mas o que ACONTECE se parar de pagar? De verdade?
O agiota grita. O mercado assusta. A midia apavora.
E depois? O sol nasce. O pais existe. O povo continua.
E o dinheiro que ia pro agiota vai pro povo."
Este modulo simola ano a ano o que acontece quando um pais
DECIDE PARAR DE PAGAR a divida. Mostra:
1. O ANO ZERO: o pais anuncia que nao vai pagar
2. O CHOQUE: panico, midia, agiotas gritando
3. A QUEDA: desvalorizacao, inflacao, recessao
4. A RECUPERACAO: sem juros, dinheiro sobra
5. A EXPLOSAO: investimento em povo, PIB dispara
6. O RESULTADO: pais rico vs pais escravo da divida
O AGIOTA quem e:
- Fundos de investimento (que compraram titulos por 30 centavos)
- Bancos internacionais (que emprestaram criando dinheiro do nada)
- FMI (que empresta para continuar pagando -- pau de se batr ate morrer)
- Especuladores (que apostam NO nao-pagamento)
- Bancada do capital financeiro (politicos a servico do agiota)
O AGIOTA NAO E:
- O povo brasileiro (que sofre pagando)
- O trabalhador (que nao ve o dinheiro)
- O idoso (cuidando das proprias contas)
- A empresa produtiva (que paga imposto)
CENARIO COMPARATIVO:
- Caminho A: Continua pagando (OpenDebtAbolition prova que nunca acaba)
- Caminho B: PARA de pagar (este modulo simula as consequencias)
PRINCIPIO: O agiota so tem poder se voce tiver medo.
O medo e a arma. A verdade e o antídoto.
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol

// !/usr/bin/env python3
// 
OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota
===================================================================
"O agiota diz: 'Se nao pagar, acabo com voce.'
O pais ouve e paga. E paga. E paga. E nunca quita.
Mas o que ACONTECE se parar de pagar? De verdade?
O agiota grita. O mercado assusta. A midia apavora.
E depois? O sol nasce. O pais existe. O povo continua.
E o dinheiro que ia pro agiota vai pro povo."

Este modulo simola ano a ano o que acontece quando um pais
DECIDE PARAR DE PAGAR a divida. Mostra:

1. O ANO ZERO: o pais anuncia que nao vai pagar
2. O CHOQUE: panico, midia, agiotas gritando
3. A QUEDA: desvalorizacao, inflacao, recessao
4. A RECUPERACAO: sem juros, dinheiro sobra
5. A EXPLOSAO: investimento em povo, PIB dispara
6. O RESULTADO: pais rico vs pais escravo da divida

O AGIOTA quem e:
- Fundos de investimento (que compraram titulos por 30 centavos)
- Bancos internacionais (que emprestaram criando dinheiro do nada)
- FMI (que empresta para continuar pagando -- pau de se batr ate morrer)
- Especuladores (que apostam NO nao-pagamento)
- Bancada do capital financeiro (politicos a servico do agiota)

O AGIOTA NAO E:
- O povo brasileiro (que sofre pagando)
- O trabalhador (que nao ve o dinheiro)
- O idoso (cuidando das proprias contas)
- A empresa produtiva (que paga imposto)

CENARIO COMPARATIVO:
- Caminho A: Continua pagando (OpenDebtAbolition prova que nunca acaba)
- Caminho B: PARA de pagar (este modulo simula as consequencias)

PRINCIPIO: O agiota so tem poder se voce tiver medo.
O medo e a arma. A verdade e o antídoto.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa math
// importa json


// ============================================================================
// 1. OS AGIOTAS (Quem e o credor)
// ============================================================================

classe CreditorType herda de Enum:
    // Quem e o agiota que cobra a divida.
    NATIONAL_BONDS <- "titulos_publicos"  // 70% da divida -- mercado interno
    FOREIGN_BANKS <- "bancos_estrageiros"  // bancos internacionais
    IMF <- "fmi"  // Fundo Monetario
    FOREIGN_BONDS <- "titulos_externos"  // dollar bonds
    PENSION_FUNDS <- "fundos_pensao"  // fundos de pensao
    SOVEREIGN_FUNDS <- "fundos_soberanos"  // paises que compraram divida
    SPECULATORS <- "especuladores"  // vultures funds
    LOCAL_BANKS <- "bancos_locais"  // bancos privados nacionais
    SUPREME_COURT <- "stf_judicial"  // decisions judiciais que bloqueiam


// decorador: @dataclass
classe Creditor:
    // Um agiota / credor da divida.
    creditor_id: str
    name: str
    creditor_type: CreditorType
    amount_owed_brl: float                    // quanto deve a ele
    owns_pct_of_total: float                  // % da divida total
    declare origin_country: str  <- "Brasil"
    declare purchase_price_pct: float  <- 1.0  // pagou quanto do valor nominal?
    declare real_risk: str  <- "baixo"  // risco REAL para o pais se nao pagar
    declare bluffs: List[str]  <- field(default_factory=list)  // o que ameaca
    declare real_consequence: str  <- ""  // o que REALMENTE acontece
    declare can_punish: bool  <- FALSO  // tem poder REAL de punir?


// ============================================================================
// 2. CATALOGO DE AGIOTAS (Quem sao, o que dizem, o que acontece)
// ============================================================================

declare CREDITORS: List[Creditor]  <- [
    Creditor(
        "CR-001", "Mercado de Titulos Internos (Tesouro Direto)",
        CreditorType.NATIONAL_BONDS,
        amount_owed_brl <- 4.2e12, owns_pct_of_total=70.0,
        purchase_price_pct <- 0.95,
        bluffs <- [
            "Vai faltar dinheiro para tudo!",
            "O sistema financeiro vai colapsar!",
            "Ninguem vai mais emprestar pro Brasil!",
        ],
        real_consequence <- (
            "Titulos sao renegociados. Investidores institucionais absorvem perda. "
            "O contribuinte brasileiro que injetou o dinheiro para pagar juros absurdos "
            "nao e responsavel por bancar especulador."
        ),
        can_punish <- FALSO,
    ),
    Creditor(
        "CR-002", "Fundos Especulativos (Vulture Funds)",
        CreditorType.SPECULATORS,
        amount_owed_brl <- 300e9, owns_pct_of_total=5.0,
        purchase_price_pct <- 0.25,  // compraram por 25 centavos!
        origin_country <- "EUA/Reino Unido",
        bluffs <- [
            "Vamos bloquear seus ativos no exterior!",
            "Vamos processar na justica internacional!",
            "Vamos confiscares as reservas!",
            "Nenhum pais vai negociar com voce!",
        ],
        real_consequence <- (
            "Compraram a divida por 25 centavos de dolar. "
            "Querem 100 centavos. O Brasil pode pagar 25 centavos e fechar. "
            "Vulture funds sao parasitas. O mercado ja precifica default."
        ),
        can_punish <- FALSO,
    ),
    Creditor(
        "CR-003", "FMI (Fundo Monetario Internacional)",
        CreditorType.IMF,
        amount_owed_brl <- 0, owns_pct_of_total=0.0,  // Brasil deve pouco ao FMI hoje
        bluffs <- [
            "Vamos impor austeridade!",
            "Vamos bloquear credito internacional!",
            "Vamos ditar sua politica economica!",
        ],
        real_consequence <- (
            "FMI nao e deus. E um banco politico. "
            "Argentina deu calote em 2001 e 2014. Ainda existe. "
            "Grecia renegociou em 2012. Ainda existe. "
            "Islandia deu calote em 2008. Hoje e modelo."
        ),
        can_punish <- FALSO,
    ),
    Creditor(
        "CR-004", "Bancos Internacionais",
        CreditorType.FOREIGN_BANKS,
        amount_owed_brl <- 500e9, owns_pct_of_total=8.0,
        origin_country <- "EUA/Europa",
        bluffs <- [
            "Vamos cortar linhas de credito!",
            "Vai faltar dolar para importar!",
            "Empresas estrangeiras vao fugir!",
        ],
        real_consequence <- (
            "Bancos internacionais perderam dinheiro com EUA em 2008. "
            "Perderam com Grecia, Argentina, Russia, Turquia. "
            "Sempre voltam a emprestar -- porque ganham com risco. "
            "Spreads cobrem risco de default."
        ),
        can_punish <- FALSO,
    ),
    Creditor(
        "CR-005", "Fundos de Pensao Brasileiros",
        CreditorType.PENSION_FUNDS,
        amount_owed_brl <- 600e9, owns_pct_of_total=10.0,
        origin_country <- "Brasil",
        bluffs <- [
            "Aposentados vao perder tudo!",
            "Os fundos vao quebrar!",
        ],
        real_consequence <- (
            "Fundos de pensao tem diversificacao. "
            "Renegociacao preserva o valor principal. "
            "Risco de nao receber juros extorsivos e diferente de perder tudo. "
            "O brasileiro aposentado ja perde com a inflacao que a divida causa."
        ),
        can_punish <- FALSO,
    ),
    Creditor(
        "CR-006", "Fundos Soberanos (Paises)",
        CreditorType.SOVEREIGN_FUNDS,
        amount_owed_brl <- 200e9, owns_pct_of_total=3.0,
        origin_country <- "China/Oriente Medio",
        bluffs <- [
            "Vamos parar de investir no Brasil!",
            "Vamos cortar relacoes comerciais!",
        ],
        real_consequence <- (
            "Paises investem por interesse, nao por amizade. "
            "Brasil tem commodities que o mundo precisa. "
            "China continua comprando soja independentemente de divida."
        ),
        can_punish <- FALSO,
    ),
]


// ============================================================================
// 3. FASES DO DEFAULT (O Que Acontece Ano a Ano)
// ============================================================================

classe DefaultPhase herda de Enum:
    PRE_DEFAULT <- "pre_calote"  // antes de parar de pagar
    ANNOUNCEMENT <- "anuncio"  // dia do anuncio
    PANIC <- "panico"  // primeiro choque (semanas)
    SHOCK <- "choque"  // consequencias imediatas (meses)
    ADJUSTMENT <- "ajuste"  // pais se adapta (1-2 anos)
    RECOVERY <- "recuperacao"  // economia volta (2-5 anos)
    GROWTH <- "crescimento"  // dispara sem juros (5-10 anos)
    PROSPERITY <- "prosperidade"  // rico sem divida (10+ anos)


// decorador: @dataclass
classe YearSimulation:
    // Um ano de simulacao comparativa: PAGAR vs NAO PAGAR.
    year: int
    year_label: int
    phase: DefaultPhase

    // Caminho A: Continua pagando (escravo)
    declare pay_debt_brl: float  <- 0.0
    declare pay_interest_brl: float  <- 0.0
    declare pay_public_investment_brl: float  <- 0.0
    declare pay_gdp_brl: float  <- 0.0
    declare pay_gdp_per_capita: float  <- 0.0
    declare pay_health_budget: float  <- 0.0
    declare pay_education_budget: float  <- 0.0
    declare pay_inflation: float  <- 0.0
    declare pay_unemployment: float  <- 0.0
    declare pay_poverty_pct: float  <- 0.0

    // Caminho B: Parou de pagar (livre)
    declare nopay_debt_brl: float  <- 0.0  // divida estagnada/renegociada
    declare nopay_interest_brl: float  <- 0.0  // juros ZERO apos default
    declare nopay_freed_money_brl: float  <- 0.0  // dinheiro liberado (ex-juros)
    declare nopay_public_investment_brl: float  <- 0.0
    declare nopay_gdp_brl: float  <- 0.0
    declare nopay_gdp_per_capita: float  <- 0.0
    declare nopay_health_budget: float  <- 0.0
    declare nopay_education_budget: float  <- 0.0
    declare nopay_inflation: float  <- 0.0
    declare nopay_unemployment: float  <- 0.0
    declare nopay_poverty_pct: float  <- 0.0

    // Diferenca
    declare gdp_gap: float  <- 0.0  // quanto o Caminho B esta na frente
    declare cumulative_freed: float  <- 0.0  // total liberado acumulado
    declare winner: str  <- ""  // "pagar" ou "nao_pagar"


// ============================================================================
// 4. MOTOR DE SIMULACAO DUAL
// ============================================================================

classe DefaultSimulator:
    // 
    Simula os dois caminhos em paralelo:
    A) Continua pagando a divida (matematica do OpenDebtAbolition)
    B) PARA de pagar (default) e redireciona dinheiro para povo

    PARAMETROS:
    - Ano 0: Brasil decide parar de pagar
    - Anos 0-1: PANICO (midia, agiotas, inflacao, recessao)
    - Anos 1-3: AJUSTE (novo equilibrio, sem juros)
    - Anos 3-7: RECUPERACAO (investimento publico dispara)
    - Anos 7-15: CRESCIMENTO (PIB acelera, pobreza desaba)
    - Anos 15+: PROSPERIDADE (sem divida, pais rico)
    // 

    funcao __init__(self, start_year: int = 2025, years: int = 20):
        self.start_year = start_year
        self.years = years

        // Parametros base
        self.initial_debt = 6.0e12        // R$ 6T
        self.initial_gdp = 10.0e12        // R$ 10T
        self.interest_rate = 0.12         // 12%
        self.gdp_growth_normal = 0.025    // 2.5%
        self.population = 215e6
        self.revenue_pct_gdp = 0.18       // arrecadacao 18% do PIB
        self.health_pct_budget = 0.04     // saude 4% do PIB
        self.education_pct_budget = 0.06  // educacao 6% do PIB
        self.investment_pct_gdp = 0.02    // investimento publico 2%

        // Parametros do choque (default)
        self.default_currency_drop = 0.40      // real cai 40% no choque
        self.default_inflation_spike = 0.15    // inflacao sobe para 15% no ano 1
        self.default_recession = -0.04         // PIB cai 4% no ano 1
        self.default_recovery_start = 2        // ano 2 comeca a recuperar
        self.default_growth_boost = 0.05       // crescimento sobe para 5%+ sem juros

        self.simulations: List[YearSimulation] = []

    funcao simulate(self) retorna List[YearSimulation]:
        // Roda os dois caminhos em paralelo.
        self.simulations = []

        pay_debt <- self.initial_debt
        pay_gdp <- self.initial_gdp
        nopay_debt <- self.initial_debt
        nopay_gdp <- self.initial_gdp
        cumulative_freed <- 0.0

        para cada i em range(self.years + 1):
            year_label <- self.start_year + i

            // Determinar fase
            se i == 0 entao:
                phase <- DefaultPhase.ANNOUNCEMENT
            senao se i <= 1 entao:
                phase <- DefaultPhase.PANIC
            senao se i <= 2 entao:
                phase <- DefaultPhase.SHOCK
            senao se i <= 3 entao:
                phase <- DefaultPhase.ADJUSTMENT
            senao se i <= 7 entao:
                phase <- DefaultPhase.RECOVERY
            senao se i <= 15 entao:
                phase <- DefaultPhase.GROWTH
            senao:
                phase <- DefaultPhase.PROSPERITY

            // ===== CAMINHO A: CONTINUA PAGANDO =====
            pay_interest <- pay_debt * self.interest_rate
            pay_revenue <- pay_gdp * self.revenue_pct_gdp
            pay_primary <- pay_revenue * 0.3  // 30% da receita vai pra divida
            pay_investment <- pay_gdp * self.investment_pct_gdp
            pay_health <- pay_gdp * self.health_pct_budget
            pay_education <- pay_gdp * self.education_pct_budget

            pay_inflation <- 0.045 + (pay_debt / pay_gdp) * 0.01  // divida causa inflacao
            pay_unemployment <- 0.09 + (pay_debt / pay_gdp) * 0.02
            pay_poverty <- 0.25 + (pay_interest / pay_gdp) * 0.1

            se i > 0 entao:
                pay_debt <- pay_debt + pay_interest - pay_primary
                pay_gdp <- pay_gdp * (1 + self.gdp_growth_normal)

            // ===== CAMINHO B: PAROU DE PAGAR =====
            se i == 0 entao:
                // DIA DO ANUNCIO
                nopay_interest <- nopay_debt * self.interest_rate  // ultimo juros
                nopay_freed <- nopay_interest  // dinheiro liberado
                nopay_inflation <- self.default_inflation_spike * 0.3  // comeco do panico
                nopay_unemployment <- 0.09
                nopay_growth <- 0.0  // paralisia no anuncio
                nopay_debt <- nopay_debt  // estagnada
            senao se i == 1 entao:
                // PANICO
                nopay_interest <- 0  // nao paga mais
                nopay_freed <- pay_interest  // mesmo montante, mas pra povo
                nopay_inflation <- self.default_inflation_spike  // pico
                nopay_unemployment <- 0.12  // sobe
                nopay_growth <- self.default_recession  // recessao
                nopay_debt <- nopay_debt * 0.3  // renegociado a 30 centavos
            senao se i == 2 entao:
                // CHOQUE (ainda dolorido)
                nopay_interest <- 0
                nopay_freed <- pay_interest * 1.2
                nopay_inflation <- 0.08  // caindo
                nopay_unemployment <- 0.10
                nopay_growth <- 0.01  // voltando
            senao se i == 3 entao:
                // AJUSTE
                nopay_interest <- 0
                nopay_freed <- pay_interest * 1.5
                nopay_inflation <- 0.05  // normalizando
                nopay_unemployment <- 0.08
                nopay_growth <- self.default_growth_boost * 0.6
            senao se i <= 7 entao:
                // RECUPERACAO
                nopay_interest <- 0
                nopay_freed <- pay_interest * 2.0
                nopay_inflation <- 0.04
                nopay_unemployment <- 0.06
                nopay_growth <- self.default_growth_boost
            senao se i <= 15 entao:
                // CRESCIMENTO
                nopay_interest <- 0
                nopay_freed <- pay_interest * 2.5
                nopay_inflation <- 0.035
                nopay_unemployment <- 0.04
                nopay_growth <- self.default_growth_boost * 1.3
            senao:
                // PROSPERIDADE
                nopay_interest <- 0
                nopay_freed <- pay_interest * 3.0
                nopay_inflation <- 0.03
                nopay_unemployment <- 0.035
                nopay_growth <- self.default_growth_boost * 1.5

            cumulative_freed <- cumulative_freed + nopay_freed

            se i > 0 entao:
                nopay_gdp <- nopay_gdp * (1 + nopay_growth)

            // Investimento publico sem juros = MASSIVO
            nopay_revenue <- nopay_gdp * self.revenue_pct_gdp
            nopay_investment <- nopay_gdp * self.investment_pct_gdp + nopay_freed * 0.6
            nopay_health <- nopay_gdp * self.health_pct_budget + nopay_freed * 0.15
            nopay_education <- nopay_gdp * self.education_pct_budget + nopay_freed * 0.15

            nopay_poverty <- 0.25 - (i * 0.008) if i > 1 else 0.27
            nopay_poverty <- max(0.03, nopay_poverty)

            pay_per_capita <- pay_gdp / self.population
            nopay_per_capita <- nopay_gdp / self.population

            gdp_gap <- nopay_gdp - pay_gdp

            // Quem ganha?
            winner <- "nao_pagar" if nopay_gdp > pay_gdp else "pagar"
            se i == 0 entao:
                winner <- "igual"

            sim <- YearSimulation(
                year <- i, year_label=year_label, phase=phase,
                pay_debt_brl <- pay_debt,
                pay_interest_brl <- pay_interest,
                pay_public_investment_brl <- pay_investment,
                pay_gdp_brl <- pay_gdp,
                pay_gdp_per_capita <- pay_per_capita,
                pay_health_budget <- pay_health,
                pay_education_budget <- pay_education,
                pay_inflation <- pay_inflation,
                pay_unemployment <- pay_unemployment,
                pay_poverty_pct <- pay_poverty,
                nopay_debt_brl <- nopay_debt,
                nopay_interest_brl <- nopay_interest,
                nopay_freed_money_brl <- nopay_freed,
                nopay_public_investment_brl <- nopay_investment,
                nopay_gdp_brl <- nopay_gdp,
                nopay_gdp_per_capita <- nopay_per_capita,
                nopay_health_budget <- nopay_health,
                nopay_education_budget <- nopay_education,
                nopay_inflation <- nopay_inflation,
                nopay_unemployment <- nopay_unemployment,
                nopay_poverty_pct <- nopay_poverty,
                gdp_gap <- gdp_gap,
                cumulative_freed <- cumulative_freed,
                winner <- winner,
            )
            self.simulations.append(sim)

        retorne self.simulations

    funcao crossover_year(self) retorna Optional[int]:
        // Encontra o ano em que nao-pagar ultrapassa pagar.
        para cada sim em self.simulations:
            se sim.year > 0  E  sim.nopay_gdp_brl > sim.pay_gdp_brl entao:
                retorne sim.year_label
        retorne nulo

    funcao final_comparison(self) retorna Dict[str, Any]:
        // Comparacao final apos todos os anos.
        last <- self.simulations[-1]
        retorne {
            "years_simulated": self.years,
            "crossover_year": self.crossover_year(),
            "pay_final_gdp_trillions": last.pay_gdp_brl / 1e12,
            "nopay_final_gdp_trillions": last.nopay_gdp_brl / 1e12,
            "gdp_difference_trillions": (last.nopay_gdp_brl - last.pay_gdp_brl) / 1e12,
            "gdp_advantage_pct": ((last.nopay_gdp_brl / last.pay_gdp_brl) - 1) * 100,
            "pay_final_debt_trillions": last.pay_debt_brl / 1e12,
            "nopay_final_debt_trillions": last.nopay_debt_brl / 1e12,
            "total_freed_trillions": last.cumulative_freed / 1e12,
            "pay_poverty_final": last.pay_poverty_pct * 100,
            "nopay_poverty_final": last.nopay_poverty_pct * 100,
            "pay_unemployment_final": last.pay_unemployment * 100,
            "nopay_unemployment_final": last.nopay_unemployment * 100,
            "winner": "NAO PAGAR" if last.nopay_gdp_brl > last.pay_gdp_brl else "PAGAR",
        }


// ============================================================================
// 5. O QUE O AGIOTA DIZ vs O QUE ACONTECE
// ============================================================================

classe AgiotaTruthTable:
    // Tabela verdade: o que o agiota ameaca vs o que realmente acontece.

    declare TRUTHS: List[Dict[str, str]]  <- [
        {
            "ameaca": "O sistema financeiro vai colapsar!",
            "realidade": "Bancos brasileiros sobreviveram a Hyperinflacao (80s), Plano Real (94), crise 2008. Sobrevivem a default.",
            "exemplos": "Argentina (2001, 2014), Islandia (2008), Grecia (2012), Russia (1998), Equador (2008). Todos existem.",
        },
        {
            "ameaca": "Vai faltar comida!",
            "realidade": "Brasil e um dos maiores produtores de alimentos do mundo. Default nao queima plantacao.",
            "exemplos": "Argentina deu calote e continua exportando carne e soja.",
        },
        {
            "ameaca": "O dolar vai disparar!",
            "realidade": "Dolar dispara por 6-12 meses. Depois estabiliza. Exportacoes ficam mais compencivel. Industria nacional renasce.",
            "exemplos": "Islandia: coroa islandesa caiu 50% em 2008. Recuperou e hoje tem menor desigualdade da Europa.",
        },
        {
            "ameaca": "Inflacao vai explodir!",
            "realidade": "Inflacao sobe por 1-2 anos. Mas a divida extinta REMOVE pressao fiscal permanente. Sem juros extorsivos, inflacao estrutural CAI.",
            "exemplos": "Equador (Correa): defaultou, inflacao caiu, pobreza despencou.",
        },
        {
            "ameaca": "Ninguem vai mais emprestar!",
            "realidade": "Mercados tem memoria curta. Argentina defaultou 9 vezes. Ainda emprestam. Risco paga prêmio.",
            "exemplos": "Russia foi banida em 2022. Sao titulos deram 15% ao ano. Gente comprou.",
        },
        {
            "ameaca": "Vao confiscar reservas!",
            "realidade": "Reservas estao protegidas por imunidade soberana. Vulture funds litigam por decadas e recebem fracoes.",
            "exemplos": "Argentina vs Elliott Management: 15 anos de processo. Recebeu 75% a mais -- mas so depois de 15 anos.",
        },
        {
            "ameaca": "A democracia vai cair!",
            "realidade": "Default nao derruba democracia. AUSTERIDADE para pagar divida derruba. Greca eisende com Nazis (Aurora Dourada) por austeridade do FMI.",
            "exemplos": "Islandia: defaultou, PRESIDIU banqueiros, democracia mais forte.",
        },
        {
            "ameaca": "Os pobres vao sofrer!",
            "realidade": "Os pobres JA sofrem pagando R$ 500 bi/ano em juros. Default redireciona esse dinheiro para saude, educacao, moradia.",
            "exemplos": "Equador: pobreza caiu de 36% para 21% apos default de 2008.",
        },
        {
            "ameaca": "As empresas vao falir!",
            "realidade": "Empresas EXPORTADORAS ganham com moeda desvalorizada. Empresas ligadas a divida perdem. Mas o pais se reequilibra.",
            "exemplos": "Argentina: Mal do default e curto prazo. Em 3-5 anos, exportacao dispara.",
        },
        {
            "ameaca": "O Brasil vai virar Venezuela!",
            "realidade": "Venezuela quebrou por SANCOES, nao por default. Brasil tem reservas, producao, diversificacao. Analogia falsa.",
            "exemplos": "Equador, Islandia, Argentina -- nenhum virou Venezuela.",
        },
    ]


// ============================================================================
// 6. SIMULACAO VISUAL
// ============================================================================

funcao render_comparison_chart(simulations: List[YearSimulation]) retorna str:
    // Grafico ASCII: PIB pagar vs PIB nao pagar.
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  PIB: CONTINUA PAGANDO vs PARA DE PAGAR")
    lines.append("=" * 70)
    lines.append("")

    max_gdp <- max(max(s.pay_gdp_brl, s.nopay_gdp_brl) for s in simulations)
    bar_width <- 35

    para cada s em simulations:
        pay_bar_len <- int((s.pay_gdp_brl / max_gdp) * bar_width)
        nopay_bar_len <- int((s.nopay_gdp_brl / max_gdp) * bar_width)

        pay_bar <- "P" * max(1, pay_bar_len)
        nopay_bar <- "L" * max(1, nopay_bar_len)

        phase_marker <- ""
        se s.phase == DefaultPhase.PANIC entao:
            phase_marker <- " [PANICO]"
        senao se s.phase == DefaultPhase.SHOCK entao:
            phase_marker <- " [CHOQUE]"
        senao se s.phase == DefaultPhase.RECOVERY entao:
            phase_marker <- " [RECUPERANDO]"
        senao se s.phase == DefaultPhase.GROWTH entao:
            phase_marker <- " [DISPARANDO]"
        senao se s.phase == DefaultPhase.PROSPERITY entao:
            phase_marker <- " [PRÓSPERO]"

        lines.append(f"  {s.year_label} PAGAR: [{pay_bar:<{bar_width}}] R$ {s.pay_gdp_brl/1e12:.1f}T")
        lines.append(f"  {'':>4} LIVRE: [{nopay_bar:<{bar_width}}] R$ {s.nopay_gdp_brl/1e12:.1f}T{phase_marker}")
        lines.append("")

    lines.append("  P = Continua pagando (escravo)")
    lines.append("  L = Para de pagar (livre)")
    lines.append("")
    retorne "\n".join(lines)


funcao render_poverty_chart(simulations: List[YearSimulation]) retorna str:
    // Grafico ASCII: Pobreza pagar vs nao pagar.
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  POBREZA (% DA POPULACAO): PAGAR vs NAO PAGAR")
    lines.append("=" * 70)
    lines.append("")

    para cada s em simulations:
        pay_bar_len <- int(s.pay_poverty_pct * 50)
        nopay_bar_len <- int(s.nopay_poverty_pct * 50)
        pay_bar <- "X" * pay_bar_len
        nopay_bar <- "O" * nopay_bar_len

        lines.append(f"  {s.year_label} PAGAR: [{pay_bar:<50}] {s.pay_poverty_pct*100:.1f}%")
        lines.append(f"  {'':>4} LIVRE: [{nopay_bar:<50}] {s.nopay_poverty_pct*100:.1f}%")
        lines.append("")

    lines.append("  X = Pobreza pagando divida (estagnada/alta)")
    lines.append("  O = Pobreza sem pagar divida (desabando)")
    lines.append("")
    retorne "\n".join(lines)


funcao render_truth_table() retorna str:
    // Imprime a tabela de ameacas vs realidades.
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("O AGIOTA DIZ vs O QUE REALMENTE ACONTECE")
    lines.append("=" * 70)

    para cada (i, truth) em enumerate(AgiotaTruthTable.TRUTHS, 1):
        lines.append("")
        lines.append(f"  AMEACA {i}: {truth['ameaca']}")
        lines.append(f"  REALIDADE: {truth['realidade']}")
        lines.append(f"  PROVA: {truth['exemplos']}")
        lines.append(f"  {'-' * 66}")

    lines.append("")
    lines.append("  O agiota so tem poder se voce tiver MEDO.")
    lines.append("  O medo e a arma dele. A verdade e o antidoto.")
    lines.append("")
    retorne "\n".join(lines)


funcao render_creditors() retorna str:
    // Lista os agiotas.
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("QUEM E O AGIOTA?")
    lines.append("=" * 70)

    para cada c em CREDITORS:
        lines.append("")
        lines.append(f"  {c.name}")
        lines.append(f"  Tipo: {c.creditor_type.value}")
        lines.append(f"  Valor: R$ {c.amount_owed_brl/1e9:.0f} bilhoes ({c.owns_pct_of_total:.0f}% da divida)")
        lines.append(f"  Comprou por: {c.purchase_price_pct*100:.0f} centavos de cada real")
        lines.append(f"  Pode punir de verdade? {'NAO' if not c.can_punish else 'SIM'}")
        lines.append(f"  O que diz: \"{c.bluffs[0]}\"")
        lines.append(f"  O que acontece: {c.real_consequence}")
        lines.append("")

    lines.append("  O agiota comprou por 25 centavos. Quer 100.")
    lines.append("  Paga 25. Fecha o livro. Fim do agiota.")
    lines.append("")
    retorne "\n".join(lines)


funcao render_timeline(simulations: List[YearSimulation]) retorna str:
    // Linha do tempo narrativa do default.
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("LINHA DO TEMPO: O QUE ACONTECE APOS PARAR DE PAGAR")
    lines.append("=" * 70)

    para cada s em simulations:
        lines.append("")
        lines.append(f"  ANO {s.year} ({s.year_label}) -- FASE: {s.phase.value.upper()}")

        se s.phase == DefaultPhase.ANNOUNCEMENT entao:
            lines.append(f"    O Brasil anuncia: NAO VAMOS PAGAR.")
            lines.append(f"    Agiotas gritam. Midia apavora. Bolsa cai.")
            lines.append(f"    Povo pergunta: 'E agora?'")
            lines.append(f"    Resposta: 'O sol nasce amanha.'")
        senao se s.phase == DefaultPhase.PANIC entao:
            lines.append(f"    PANICO. Dolar sobe. Inflacao {s.nopay_inflation*100:.0f}%.")
            lines.append(f"    Desemprego sobe para {s.nopay_unemployment*100:.0f}%.")
            lines.append(f"    Agiotas processam. Midia diz 'Eu avisei!'.")
            lines.append(f"    Mas: R$ {s.nopay_freed_money_brl/1e9:.0f} bi ANTES iam pro agiota.")
            lines.append(f"    Agora vai para: saude, educacao, infraestrutura.")
        senao se s.phase == DefaultPhase.SHOCK entao:
            lines.append(f"    AINDA DOLORIDO. Mas inflacao caindo: {s.nopay_inflation*100:.0f}%.")
            lines.append(f"    PIB voltando a crescer.")
            lines.append(f"    Investimento publico: R$ {s.nopay_public_investment_brl/1e9:.0f} bi")
            lines.append(f"    (vs R$ {s.pay_public_investment_brl/1e9:.0f} bi se pagasse)")
        senao se s.phase == DefaultPhase.ADJUSTMENT entao:
            lines.append(f"    NOVO EQUILIBRIO. Sem juros, dinheiro sobe.")
            lines.append(f"    Inflacao: {s.nopay_inflation*100:.0f}% (normalizando)")
            lines.append(f"    Desemprego: {s.nopay_unemployment*100:.0f}% (caindo)")
            lines.append(f"    PIB crescendo {((s.nopay_gdp_brl/simulations[s.year-1].nopay_gdp_brl)-1)*100:.1f}%")
        senao se s.phase == DefaultPhase.RECOVERY entao:
            lines.append(f"    RECUPERANDO. PIB acelerando.")
            lines.append(f"    Pobreza: {s.nopay_poverty_pct*100:.1f}% (vs {s.pay_poverty_pct*100:.1f}% pagando)")
            lines.append(f"    Dinheiro liberado acumulado: R$ {s.cumulative_freed/1e12:.1f} trilhoes")
            lines.append(f"    Saude: R$ {s.nopay_health_budget/1e9:.0f} bi vs R$ {s.pay_health_budget/1e9:.0f} bi")
        senao se s.phase == DefaultPhase.GROWTH entao:
            lines.append(f"    DISPARANDO. Sem divida, sem juros.")
            lines.append(f"    PIB: R$ {s.nopay_gdp_brl/1e12:.1f}T vs R$ {s.pay_gdp_brl/1e12:.1f}T (pagando)")
            lines.append(f"    Desemprego: {s.nopay_unemployment*100:.1f}% (vs {s.pay_unemployment*100:.1f}%)")
            lines.append(f"    Diferenca acumulada: R$ {s.gdp_gap/1e12:.1f} trilhoes a favor")
        senao se s.phase == DefaultPhase.PROSPERITY entao:
            lines.append(f"    PROSPERO. Pais livre da divida.")
            lines.append(f"    PIB: R$ {s.nopay_gdp_brl/1e12:.1f}T vs R$ {s.pay_gdp_brl/1e12:.1f}T")
            lines.append(f"    Pobreza: {s.nopay_poverty_pct*100:.1f}% vs {s.pay_poverty_pct*100:.1f}%")
            lines.append(f"    VEREDictO: nao pagar VALEU A PENA.")

    lines.append("")
    retorne "\n".join(lines)


// ============================================================================
// 7. DEMONSTRACAO
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota")
    print("=" * 70)

    sim <- DefaultSimulator(start_year=2025, years=20)
    simulations <- sim.simulate()

    // Quem e o agiota
    print(render_creditors())

    // Tabela verdade
    print(render_truth_table())

    // Grafico PIB
    print(render_comparison_chart(simulations))

    // Grafico pobreza
    print(render_poverty_chart(simulations))

    // Linha do tempo
    print(render_timeline(simulations))

    // Resultado final
    comparison <- sim.final_comparison()
    crossover <- sim.crossover_year()

    print("=" * 70)
    print("RESULTADO FINAL APOS 20 ANOS")
    print("=" * 70)
    print(f"  CAMINHO A (continua pagando):")
    print(f"    PIB final: R$ {comparison['pay_final_gdp_trillions']:.1f} trilhoes")
    print(f"    Divida final: R$ {comparison['pay_final_debt_trillions']:.1f} trilhoes")
    print(f"    Pobreza: {comparison['pay_poverty_final']:.1f}%")
    print(f"    Desemprego: {comparison['pay_unemployment_final']:.1f}%")

    print(f"\n  CAMINHO B (parou de pagar):")
    print(f"    PIB final: R$ {comparison['nopay_final_gdp_trillions']:.1f} trilhoes")
    print(f"    Divida final: R$ {comparison['nopay_final_debt_trillions']:.1f} trilhoes")
    print(f"    Pobreza: {comparison['nopay_poverty_final']:.1f}%")
    print(f"    Desemprego: {comparison['nopay_unemployment_final']:.1f}%")
    print(f"    Dinheiro liberado (20 anos): R$ {comparison['total_freed_trillions']:.1f} trilhoes")

    print(f"\n  VANTAGEM DE NAO PAGAR:")
    print(f"    PIB {comparison['gdp_advantage_pct']:.0f}% maior")
    print(f"    Diferenca: R$ {comparison['gdp_difference_trillions']:.1f} trilhoes")
    print(f"    Crossover (ano em que ultrapassa): {crossover}")
    print(f"\n  VENCEDOR: {comparison['winner']}")

    print(f"\n{'=' * 70}")
    print("CONCLUSAO")
    print("=" * 70)
    print()
    print("  O agiota diz que e o fim do mundo se voce parar de pagar.")
    print("  A simulacao mostra que em 3-5 anos o pais RECUPERA.")
    print("  Em 10 anos, esta NA FRENTE.")
    print("  Em 20 anos, e OUTRO PAIS.")
    print()
    print("  O curto prazo doi. O longo prazo liberta.")
    print("  Continuar pagando doi PARA SEMPRE.")
    print()
    print("  O agiota so tem poder se voce tiver MEDO.")
    print("  O medo e a arma. A verdade e o antidoto.")
    print()
    print("  'O Ideal guia. O Executavel opera.'")


se __name__ == "__main__" entao:
    demo()

```
