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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// ============================================================================
// 1. OS AGIOTAS (Quem e o credor)
// ============================================================================

typedef enum {
    NATIONAL_BONDS,
    FOREIGN_BANKS,
    IMF,
    FOREIGN_BONDS,
    PENSION_FUNDS,
    SOVEREIGN_FUNDS,
    SPECULATORS,
    LOCAL_BANKS,
    SUPREME_COURT
} CreditorType;

const char* creditor_type_str(CreditorType t) {
    switch (t) {
        case NATIONAL_BONDS: return "titulos_publicos";
        case FOREIGN_BANKS: return "bancos_estrageiros";
        case IMF: return "fmi";
        case FOREIGN_BONDS: return "titulos_externos";
        case PENSION_FUNDS: return "fundos_pensao";
        case SOVEREIGN_FUNDS: return "fundos_soberanos";
        case SPECULATORS: return "especuladores";
        case LOCAL_BANKS: return "bancos_locais";
        case SUPREME_COURT: return "stf_judicial";
        default: return "unknown";
    }
}

typedef struct {
    char creditor_id[16];
    char name[128];
    CreditorType creditor_type;
    double amount_owed_brl;
    double owns_pct_of_total;
    char origin_country[64];
    double purchase_price_pct;
    char real_risk[32];
    char bluffs[4][128];
    int num_bluffs;
    char real_consequence[512];
    int can_punish;
} Creditor;

// ============================================================================
// 2. CATALOGO DE AGIOTAS (Quem sao, o que dizem, o que acontece)
// ============================================================================

Creditor CREDITORS[6] = {
    {
        .creditor_id = "CR-001",
        .name = "Mercado de Titulos Internos (Tesouro Direto)",
        .creditor_type = NATIONAL_BONDS,
        .amount_owed_brl = 4.2e12,
        .owns_pct_of_total = 70.0,
        .origin_country = "Brasil",
        .purchase_price_pct = 0.95,
        .num_bluffs = 3,
        .bluffs = {"Vai faltar dinheiro para tudo!", "O sistema financeiro vai colapsar!", "Ninguem vai mais emprestar pro Brasil!"},
        .real_consequence = "Titulos sao renegociados. Investidores institucionais absorvem perda. O contribuinte brasileiro que injetou o dinheiro para pagar juros absurdos nao e responsavel por bancar especulador.",
        .can_punish = 0
    },
    {
        .creditor_id = "CR-002",
        .name = "Fundos Especulativos (Vulture Funds)",
        .creditor_type = SPECULATORS,
        .amount_owed_brl = 300e9,
        .owns_pct_of_total = 5.0,
        .origin_country = "EUA/Reino Unido",
        .purchase_price_pct = 0.25,
        .num_bluffs = 4,
        .bluffs = {"Vamos bloquear seus ativos no exterior!", "Vamos processar na justica internacional!", "Vamos confiscares as reservas!", "Nenhum pais vai negociar com voce!"},
        .real_consequence = "Compraram a divida por 25 centavos de dolar. Querem 100 centavos. O Brasil pode pagar 25 centavos e fechar. Vulture funds sao parasitas. O mercado ja precifica default.",
        .can_punish = 0
    },
    {
        .creditor_id = "CR-003",
        .name = "FMI (Fundo Monetario Internacional)",
        .creditor_type = IMF,
        .amount_owed_brl = 0,
        .owns_pct_of_total = 0.0,
        .origin_country = "Internacional",
        .purchase_price_pct = 1.0,
        .num_bluffs = 3,
        .bluffs = {"Vamos impor austeridade!", "Vamos bloquear credito internacional!", "Vamos ditar sua politica economica!"},
        .real_consequence = "FMI nao e deus. E um banco politico. Argentina deu calote em 2001 e 2014. Ainda existe. Grecia renegociou em 2012. Ainda existe. Islandia deu calote em 2008. Hoje e modelo.",
        .can_punish = 0
    },
    {
        .creditor_id = "CR-004",
        .name = "Bancos Internacionais",
        .creditor_type = FOREIGN_BANKS,
        .amount_owed_brl = 500e9,
        .owns_pct_of_total = 8.0,
        .origin_country = "EUA/Europa",
        .purchase_price_pct = 1.0,
        .num_bluffs = 3,
        .bluffs = {"Vamos cortar linhas de credito!", "Vai faltar dolar para importar!", "Empresas estrangeiras vao fugir!"},
        .real_consequence = "Bancos internacionais perderam dinheiro com EUA em 2008. Perderam com Grecia, Argentina, Russia, Turquia. Sempre voltam a emprestar -- porque ganham com risco. Spreads cobrem risco de default.",
        .can_punish = 0
    },
    {
        .creditor_id = "CR-005",
        .name = "Fundos de Pensao Brasileiros",
        .creditor_type = PENSION_FUNDS,
        .amount_owed_brl = 600e9,
        .owns_pct_of_total = 10.0,
        .origin_country = "Brasil",
        .purchase_price_pct = 1.0,
        .num_bluffs = 2,
        .bluffs = {"Aposentados vao perder tudo!", "Os fundos vao quebrar!"},
        .real_consequence = "Fundos de pensao tem diversificacao. Renegociacao preserva o valor principal. Risco de nao receber juros extorsivos e diferente de perder tudo. O brasileiro aposentado ja perde com a inflacao que a divida causa.",
        .can_punish = 0
    },
    {
        .creditor_id = "CR-006",
        .name = "Fundos Soberanos (Paises)",
        .creditor_type = SOVEREIGN_FUNDS,
        .amount_owed_brl = 200e9,
        .owns_pct_of_total = 3.0,
        .origin_country = "China/Oriente Medio",
        .purchase_price_pct = 1.0,
        .num_bluffs = 2,
        .bluffs = {"Vamos parar de investir no Brasil!", "Vamos cortar relacoes comerciais!"},
        .real_consequence = "Paises investem por interesse, nao por amizade. Brasil tem commodities que o mundo precisa. China continua comprando soja independentemente de divida.",
        .can_punish = 0
    }
};

// ============================================================================
// 3. FASES DO DEFAULT (O Que Acontece Ano a Ano)
// ============================================================================

typedef enum {
    PRE_DEFAULT,
    ANNOUNCEMENT,
    PANIC,
    SHOCK,
    ADJUSTMENT,
    RECOVERY,
    GROWTH,
    PROSPERITY
} DefaultPhase;

const char* default_phase_str(DefaultPhase p) {
    switch (p) {
        case PRE_DEFAULT: return "pre_calote";
        case ANNOUNCEMENT: return "anuncio";
        case PANIC: return "panico";
        case SHOCK: return "choque";
        case ADJUSTMENT: return "ajuste";
        case RECOVERY: return "recuperacao";
        case GROWTH: return "crescimento";
        case PROSPERITY: return "prosperidade";
        default: return "unknown";
    }
}

typedef struct {
    int year;
    int year_label;
    DefaultPhase phase;
    double pay_debt_brl;
    double pay_interest_brl;
    double pay_public_investment_brl;
    double pay_gdp_brl;
    double pay_gdp_per_capita;
    double pay_health_budget;
    double pay_education_budget;
    double pay_inflation;
    double pay_unemployment;
    double pay_poverty_pct;
    double nopay_debt_brl;
    double nopay_interest_brl;
    double nopay_freed_money_brl;
    double nopay_public_investment_brl;
    double nopay_gdp_brl;
    double nopay_gdp_per_capita;
    double nopay_health_budget;
    double nopay_education_budget;
    double nopay_inflation;
    double nopay_unemployment;
    double nopay_poverty_pct;
    double gdp_gap;
    double cumulative_freed;
    char winner[16];
} YearSimulation;

// ============================================================================
// 4. MOTOR DE SIMULACAO DUAL
// ============================================================================

typedef struct {
    int start_year;
    int years;
    double initial_debt;
    double initial_gdp;
    double interest_rate;
    double gdp_growth_normal;
    double population;
    double revenue_pct_gdp;
    double health_pct_budget;
    double education_pct_budget;
    double investment_pct_gdp;
    double default_currency_drop;
    double default_inflation_spike;
    double default_recession;
    int default_recovery_start;
    double default_growth_boost;
    YearSimulation simulations[32];
    int num_simulations;
} DefaultSimulator;

void init_simulator(DefaultSimulator* ds, int start_year, int years) {
    ds->start_year = start_year;
    ds->years = years;
    ds->initial_debt = 6.0e12;
    ds->initial_gdp = 10.0e12;
    ds->interest_rate = 0.12;
    ds->gdp_growth_normal = 0.025;
    ds->population = 215e6;
    ds->revenue_pct_gdp = 0.18;
    ds->health_pct_budget = 0.04;
    ds->education_pct_budget = 0.06;
    ds->investment_pct_gdp = 0.02;
    ds->default_currency_drop = 0.40;
    ds->default_inflation_spike = 0.15;
    ds->default_recession = -0.04;
    ds->default_recovery_start = 2;
    ds->default_growth_boost = 0.05;
    ds->num_simulations = 0;
}

void simulate(DefaultSimulator* ds) {
    ds->num_simulations = 0;
    double pay_debt = ds->initial_debt;
    double pay_gdp = ds->initial_gdp;
    double nopay_debt = ds->initial_debt;
    double nopay_gdp = ds->initial_gdp;
    double cumulative_freed = 0.0;

    for (int i = 0; i <= ds->years; i++) {
        int year_label = ds->start_year + i;

        DefaultPhase phase;
        if (i == 0) phase = ANNOUNCEMENT;
        else if (i <= 1) phase = PANIC;
        else if (i <= 2) phase = SHOCK;
        else if (i <= 3) phase = ADJUSTMENT;
        else if (i <= 7) phase = RECOVERY;
        else if (i <= 15) phase = GROWTH;
        else phase = PROSPERITY;

        // CAMINHO A: CONTINUA PAGANDO
        double pay_interest = pay_debt * ds->interest_rate;
        double pay_revenue = pay_gdp * ds->revenue_pct_gdp;
        double pay_primary = pay_revenue * 0.3;
        double pay_investment = pay_gdp * ds->investment_pct_gdp;
        double pay_health = pay_gdp * ds->health_pct_budget;
        double pay_education = pay_gdp * ds->education_pct_budget;
        double pay_inflation = 0.045 + (pay_debt / pay_gdp) * 0.01;
        double pay_unemployment = 0.09 + (pay_debt / pay_gdp) * 0.02;
        double pay_poverty = 0.25 + (pay_interest / pay_gdp) * 0.1;

        if (i > 0) {
            pay_debt = pay_debt + pay_interest - pay_primary;
            pay_gdp = pay_gdp * (1 + ds->gdp_growth_normal);
        }

        // CAMINHO B: PAROU DE PAGAR
        double nopay_interest = 0, nopay_freed = 0, nopay_inflation = 0, nopay_unemployment = 0, nopay_growth = 0;
        if (i == 0) {
            nopay_interest = nopay_debt * ds->interest_rate;
            nopay_freed = nopay_interest;
            nopay_inflation = ds->default_inflation_spike * 0.3;
            nopay_unemployment = 0.09;
            nopay_growth = 0.0;
        } else if (i == 1) {
            nopay_interest = 0;
            nopay_freed = pay_interest;
            nopay_inflation = ds->default_inflation_spike;
            nopay_unemployment = 0.12;
            nopay_growth = ds->default_recession;
            nopay_debt = nopay_debt * 0.3;
        } else if (i == 2) {
            nopay_interest = 0;
            nopay_freed = pay_interest * 1.2;
            nopay_inflation = 0.08;
            nopay_unemployment = 0.10;
            nopay_growth = 0.01;
        } else if (i == 3) {
            nopay_interest = 0;
            nopay_freed = pay_interest * 1.5;
            nopay_inflation = 0.05;
            nopay_unemployment = 0.08;
            nopay_growth = ds->default_growth_boost * 0.6;
        } else if (i <= 7) {
            nopay_interest = 0;
            nopay_freed = pay_interest * 2.0;
            nopay_inflation = 0.04;
            nopay_unemployment = 0.06;
            nopay_growth = ds->default_growth_boost;
        } else if (i <= 15) {
            nopay_interest = 0;
            nopay_freed = pay_interest * 2.5;
            nopay_inflation = 0.035;
            nopay_unemployment = 0.04;
            nopay_growth = ds->default_growth_boost * 1.3;
        } else {
            nopay_interest = 0;
            nopay_freed = pay_interest * 3.0;
            nopay_inflation = 0.03;
            nopay_unemployment = 0.035;
            nopay_growth = ds->default_growth_boost * 1.5;
        }

        cumulative_freed += nopay_freed;
        if (i > 0) {
            nopay_gdp = nopay_gdp * (1 + nopay_growth);
        }

        double nopay_investment = nopay_gdp * ds->investment_pct_gdp + nopay_freed * 0.6;
        double nopay_health = nopay_gdp * ds->health_pct_budget + nopay_freed * 0.15;
        double nopay_education = nopay_gdp * ds->education_pct_budget + nopay_freed * 0.15;

        double nopay_poverty = 0.25 - i * 0.008;
        if (i <= 1) nopay_poverty = 0.27;
        if (nopay_poverty < 0.03) nopay_poverty = 0.03;

        double pay_per_capita = pay_gdp / ds->population;
        double nopay_per_capita = nopay_gdp / ds->population;
        double gdp_gap = nopay_gdp - pay_gdp;

        char winner[16];
        strcpy(winner, (nopay_gdp > pay_gdp) ? "nao_pagar" : "pagar");
        if (i == 0) strcpy(winner, "igual");

        YearSimulation sim = {
            .year = i, .year_label = year_label, .phase = phase,
            .pay_debt_brl = pay_debt, .pay_interest_brl = pay_interest, .pay_public_investment_brl = pay_investment,
            .pay_gdp_brl = pay_gdp, .pay_gdp_per_capita = pay_per_capita,
            .pay_health_budget = pay_health, .pay_education_budget = pay_education,
            .pay_inflation = pay_inflation, .pay_unemployment = pay_unemployment, .pay_poverty_pct = pay_poverty,
            .nopay_debt_brl = nopay_debt, .nopay_interest_brl = nopay_interest, .nopay_freed_money_brl = nopay_freed,
            .nopay_public_investment_brl = nopay_investment, .nopay_gdp_brl = nopay_gdp, .nopay_gdp_per_capita = nopay_per_capita,
            .nopay_health_budget = nopay_health, .nopay_education_budget = nopay_education,
            .nopay_inflation = nopay_inflation, .nopay_unemployment = nopay_unemployment, .nopay_poverty_pct = nopay_poverty,
            .gdp_gap = gdp_gap, .cumulative_freed = cumulative_freed
        };
        strcpy(sim.winner, winner);

        ds->simulations[ds->num_simulations++] = sim;
    }
}

int crossover_year(DefaultSimulator* ds) {
    for (int i = 0; i < ds->num_simulations; i++) {
        YearSimulation* s = &ds->simulations[i];
        if (s->year > 0 && s->nopay_gdp_brl > s->pay_gdp_brl) {
            return s->year_label;
        }
    }
    return 0;
}

void final_comparison(DefaultSimulator* ds, double* results) {
    YearSimulation* last = &ds->simulations[ds->num_simulations - 1];
    results[0] = ds->years;
    results[1] = crossover_year(ds);
    results[2] = last->pay_gdp_brl / 1e12;
    results[3] = last->nopay_gdp_brl / 1e12;
    results[4] = (last->nopay_gdp_brl - last->pay_gdp_brl) / 1e12;
    results[5] = ((last->nopay_gdp_brl / last->pay_gdp_brl) - 1) * 100;
    results[6] = last->pay_debt_brl / 1e12;
    results[7] = last->nopay_debt_brl / 1e12;
    results[8] = last->cumulative_freed / 1e12;
    results[9] = last->pay_poverty_pct * 100;
    results[10] = last->nopay_poverty_pct * 100;
    results[11] = last->pay_unemployment * 100;
    results[12] = last->nopay_unemployment * 100;
    results[13] = (last->nopay_gdp_brl > last->pay_gdp_brl) ? 1 : 0;
}

// ============================================================================
// 5. O QUE O AGIOTA DIZ vs O QUE ACONTECE
// ============================================================================

typedef struct {
    char ameaca[128];
    char realidade[256];
    char exemplos[256];
} Truth;

Truth TRUTHS[10] = {
    {"O sistema financeiro vai colapsar!", "Bancos brasileiros sobreviveram a Hyperinflacao (80s), Plano Real (94), crise 2008. Sobrevivem a default.", "Argentina (2001, 2014), Islandia (2008), Grecia (2012), Russia (1998), Equador (2008). Todos existem."},
    {"Vai faltar comida!", "Brasil e um dos maiores produtores de alimentos do mundo. Default nao queima plantacao.", "Argentina deu calote e continua exportando carne e soja."},
    {"O dolar vai disparar!", "Dolar dispara por 6-12 meses. Depois estabiliza. Exportacoes ficam mais compencivel. Industria nacional renasce.", "Islandia: coroa islandesa caiu 50% em 2008. Recuperou e hoje tem menor desigualdade da Europa."},
    {"Inflacao vai explodir!", "Inflacao sobe por 1-2 anos. Mas a divida extinta REMOVE pressao fiscal permanente. Sem juros extorsivos, inflacao estrutural CAI.", "Equador (Correa): defaultou, inflacao caiu, pobreza despencou."},
    {"Ninguem vai mais emprestar!", "Mercados tem memoria curta. Argentina defaultou 9 vezes. Ainda emprestam. Risco paga prêmio.", "Russia foi banida em 2022. Sao titulos deram 15% ao ano. Gente comprou."},
    {"Vao confiscar reservas!", "Reservas estao protegidas por imunidade soberana. Vulture funds litigam por decadas e recebem fracoes.", "Argentina vs Elliott Management: 15 anos de processo. Receve 75% a mais -- mas so depois de 15 anos."},
    {"A democracia vai cair!", "Default nao derruba democracia. AUSTERIDADE para pagar divida derruba. Greca eisende com Nazis (Aurora Dourada) por austeridade do FMI.", "Islandia: defaultou, PRESIDIU banqueiros, democracia mais forte."},
    {"Os pobres vao sofrer!", "Os pobres JA sofrem pagando R$ 500 bi/ano em juros. Default redireciona esse dinheiro para saude, educacao, moradia.", "Equador: pobreza caiu de 36% para 21% apos default de 2008."},
    {"As empresas vao falir!", "Empresas EXPORTADORAS ganham com moeda desvalorizada. Empresas ligadas a divida perdem. Mas o pais se reequilibra.", "Argentina: Mal do default e curto prazo. Em 3-5 anos, exportacao dispara."},
    {"O Brasil vai virar Venezuela!", "Venezuela quebrou por SANCOES, nao por default. Brasil tem reservas, producao, diversificacao. Analogia falsa.", "Equador, Islandia, Argentina -- nenhum virou Venezuela."}
};

// ============================================================================
// 6. SIMULACAO VISUAL
// ============================================================================

void render_comparison_chart(YearSimulation* sims, int n, char* out) {
    strcpy(out, "\n======================================================================\n");
    strcat(out, "  PIB: CONTINUA PAGANDO vs PARA DE PAGAR\n");
    strcat(out, "======================================================================\n\n");

    double max_gdp = 0;
    for (int i = 0; i < n; i++) {
        if (sims[i].pay_gdp_brl > max_gdp) max_gdp = sims[i].pay_gdp_brl;
        if (sims[i].nopay_gdp_brl > max_gdp) max_gdp = sims[i].nopay_gdp_brl;
    }
    int bar_width = 35;

    for (int i = 0; i < n; i++) {
        YearSimulation* s = &sims[i];
        int pay_len = (int)((s->pay_gdp_brl / max_gdp) * bar_width);
        int nopay_len = (int)((s->nopay_gdp_brl / max_gdp) * bar_width);
        if (pay_len < 1) pay_len = 1;
        if (nopay_len < 1) nopay_len = 1;

        char pay_bar[64] = {0}, nopay_bar[64] = {0};
        for (int j = 0; j < pay_len; j++) strcat(pay_bar, "P");
        for (int j = 0; j < nopay_len; j++) strcat(nopay_bar, "L");

        char marker[32] = "";
        if (s->phase == PANIC) strcpy(marker, " [PANICO]");
        else if (s->phase == SHOCK) strcpy(marker, " [CHOQUE]");
        else if (s->phase == RECOVERY) strcpy(marker, " [RECUPERANDO]");
        else if (s->phase == GROWTH) strcpy(marker, " [DISPARANDO]");
        else if (s->phase == PROSPERITY) strcpy(marker, " [PRÓSPERO]");

        char line[256];
        sprintf(line, "  %d PAGAR: [%s] R$ %.1fT\n", s->year_label, pay_bar, s->pay_gdp_brl/1e12);
        strcat(out, line);
        sprintf(line, "      LIVRE: [%s] R$ %.1fT%s\n\n", nopay_bar, s->nopay_gdp_brl/1e12, marker);
        strcat(out, line);
    }
    strcat(out, "  P = Continua pagando (escravo)\n");
    strcat(out, "  L = Para de pagar (livre)\n\n");
}

void render_poverty_chart(YearSimulation* sims, int n, char* out) {
    strcpy(out, "\n======================================================================\n");
    strcat(out, "  POBREZA (% DA POPULACAO): PAGAR vs NAO PAGAR\n");
    strcat(out, "======================================================================\n\n");

    for (int i = 0; i < n; i++) {
        YearSimulation* s = &sims[i];
        int pay_len = (int)(s->pay_poverty_pct * 50);
        int nopay_len = (int)(s->nopay_poverty_pct * 50);
        char pay_bar[64] = {0}, nopay_bar[64] = {0};
        for (int j = 0; j < pay_len; j++) strcat(pay_bar, "X");
        for (int j = 0; j < nopay_len; j++) strcat(nopay_bar, "O");

        char line[256];
        sprintf(line, "  %d PAGAR: [%s] %.1f%%\n", s->year_label, pay_bar, s->pay_poverty_pct*100);
        strcat(out, line);
        sprintf(line, "      LIVRE: [%s] %.1f%%\n\n", nopay_bar, s->nopay_poverty_pct*100);
        strcat(out, line);
    }
    strcat(out, "  X = Pobreza pagando divida (estagnada/alta)\n");
    strcat(out, "  O = Pobreza sem pagar divida (desabando)\n\n");
}

void render_truth_table(char* out) {
    strcpy(out, "\n======================================================================\n");
    strcat(out, "O AGIOTA DIZ vs O QUE REALMENTE ACONTECE\n");
    strcat(out, "======================================================================\n");

    for (int i = 0; i < 10; i++) {
        char block[512];
        sprintf(block, "\n  AMEACA %d: %s\n  REALIDADE: %s\n  PROVA: %s\n  ------------------------------------------------------------------\n",
                i+1, TRUTHS[i].ameaca, TRUTHS[i].realidade, TRUTHS[i].exemplos);
        strcat(out, block);
    }
    strcat(out, "\n  O agiota so tem poder se voce tiver MEDO.\n");
    strcat(out, "  O medo e a arma dele. A verdade e o antidoto.\n\n");
}

void render_creditors(char* out) {
    strcpy(out, "\n======================================================================\n");
    strcat(out, "QUEM E O AGIOTA?\n");
    strcat(out, "======================================================================\n");

    for (int i = 0; i < 6; i++) {
        Creditor* c = &CREDITORS[i];
        char block[1024];
        sprintf(block, "\n  %s\n  Tipo: %s\n  Valor: R$ %.0f bilhoes (%.0f%% da divida)\n  Comprou por: %.0f centavos de cada real\n  Pode punir de verdade? %s\n  O que diz: \"%s\"\n  O que acontece: %s\n",
                c->name, creditor_type_str(c->creditor_type), c->amount_owed_brl/1e9, c->owns_pct_of_total,
                c->purchase_price_pct*100, c->can_punish ? "SIM" : "NAO", c->bluffs[0], c->real_consequence);
        strcat(out, block);
    }
    strcat(out, "\n  O agiota comprou por 25 centavos. Quer 100.\n");
    strcat(out, "  Paga 25. Fecha o livro. Fim do agiota.\n\n");
}

void render_timeline(YearSimulation* sims, int n, char* out) {
    strcpy(out, "\n======================================================================\n");
    strcat(out, "LINHA DO TEMPO: O QUE ACONTECE APOS PARAR DE PAGAR\n");
    strcat(out, "======================================================================\n");

    for (int i = 0; i < n; i++) {
        YearSimulation* s = &sims[i];
        char block[512];
        sprintf(block, "\n  ANO %d (%d) -- FASE: %s\n", s->year, s->year_label, default_phase_str(s->phase));
        strcat(out, block);

        if (s->phase == ANNOUNCEMENT) {
            strcat(out, "    O Brasil anuncia: NAO VAMOS PAGAR.\n");
            strcat(out, "    Agiotas gritam. Midia apavora. Bolsa cai.\n");
            strcat(out, "    Povo pergunta: 'E agora?'\n");
            strcat(out, "    Resposta: 'O sol nasce amanha.'\n");
        } else if (s->phase == PANIC) {
            sprintf(block, "    PANICO. Dolar sobe. Inflacao %.0f%%.\n", s->nopay_inflation*100); strcat(out, block);
            sprintf(block, "    Desemprego sobe para %.0f%%.\n", s->nopay_unemployment*100); strcat(out, block);
            strcat(out, "    Agiotas processam. Midia diz 'Eu avisei!'.\n");
            sprintf(block, "    Mas: R$ %.0f bi ANTES iam pro agiota.\n", s->nopay_freed_money_brl/1e9); strcat(out, block);
            strcat(out, "    Agora vai para: saude, educacao, infraestrutura.\n");
        } else if (s->phase == SHOCK) {
            sprintf(block, "    AINDA DOLORIDO. Mas inflacao caindo: %.0f%%.\n", s->nopay_inflation*100); strcat(out, block);
            strcat(out, "    PIB voltando a crescer.\n");
            sprintf(block, "    Investimento publico: R$ %.0f bi\n", s->nopay_public_investment_brl/1e9); strcat(out, block);
            sprintf(block, "    (vs R$ %.0f bi se pagasse)\n", s->pay_public_investment_brl/1e9); strcat(out, block);
        } else if (s->phase == ADJUSTMENT) {
            strcat(out, "    NOVO EQUILIBRIO. Sem juros, dinheiro sobe.\n");
            sprintf(block, "    Inflacao: %.0f%% (normalizando)\n", s->nopay_inflation*100); strcat(out, block);
            sprintf(block, "    Desemprego: %.0f%% (caindo)\n", s->nopay_unemployment*100); strcat(out, block);
            if (i > 0) {
                double growth = ((s->nopay_gdp_brl / sims[i-1].nopay_gdp_brl) - 1) * 100;
                sprintf(block, "    PIB crescendo %.1f%%\n", growth); strcat(out, block);
            }
        } else if (s->phase == RECOVERY) {
            strcat(out, "    RECUPERANDO. PIB acelerando.\n");
            sprintf(block, "    Pobreza: %.1f%% (vs %.1f%% pagando)\n", s->nopay_poverty_pct*100, s->pay_poverty_pct*100); strcat(out, block);
            sprintf(block, "    Dinheiro liberado acumulado: R$ %.1f trilhoes\n", s->cumulative_freed/1e12); strcat(out, block);
            sprintf(block, "    Saude: R$ %.0f bi vs R$ %.0f bi\n", s->nopay_health_budget/1e9, s->pay_health_budget/1e9); strcat(out, block);
        } else if (s->phase == GROWTH) {
            strcat(out, "    DISPARANDO. Sem divida, sem juros.\n");
            sprintf(block, "    PIB: R$ %.1fT vs R$ %.1fT (pagando)\n", s->nopay_gdp_brl/1e12, s->pay_gdp_brl/1e12); strcat(out, block);
            sprintf(block, "    Desemprego: %.1f%% (vs %.1f%%)\n", s->nopay_unemployment*100, s->pay_unemployment*100); strcat(out, block);
            sprintf(block, "    Diferenca acumulada: R$ %.1f trilhoes a favor\n", s->gdp_gap/1e12); strcat(out, block);
        } else if (s->phase == PROSPERITY) {
            strcat(out, "    PROSPERO. Pais livre da divida.\n");
            sprintf(block, "    PIB: R$ %.1fT vs R$ %.1fT\n", s->nopay_gdp_brl/1e12, s->pay_gdp_brl/1e12); strcat(out, block);
            sprintf(block, "    Pobreza: %.1f%% vs %.1f%%\n", s->nopay_poverty_pct*100, s->pay_poverty_pct*100); strcat(out, block);
            strcat(out, "    VEREDICTO: nao pagar VALEU A PENA.\n");
        }
    }
    strcat(out, "\n");
}

// ============================================================================
// 7. DEMONSTRACAO (main)
// ============================================================================

int main() {
    printf("======================================================================\n");
    printf("OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota\n");
    printf("======================================================================\n");

    DefaultSimulator sim;
    init_simulator(&sim, 2025, 20);
    simulate(&sim);

    char buf[16384];
    render_creditors(buf); printf("%s", buf);
    render_truth_table(buf); printf("%s", buf);
    render_comparison_chart(sim.simulations, sim.num_simulations, buf); printf("%s", buf);
    render_poverty_chart(sim.simulations, sim.num_simulations, buf); printf("%s", buf);
    render_timeline(sim.simulations, sim.num_simulations, buf); printf("%s", buf);

    double comp[14];
    final_comparison(&sim, comp);
    int cross = crossover_year(&sim);

    printf("======================================================================\n");
    printf("RESULTADO FINAL APOS 20 ANOS\n");
    printf("======================================================================\n");
    printf("  CAMINHO A (continua pagando):\n");
    printf("    PIB final: R$ %.1f trilhoes\n", comp[2]);
    printf("    Divida final: R$ %.1f trilhoes\n", comp[6]);
    printf("    Pobreza: %.1f%%\n", comp[9]);
    printf("    Desemprego: %.1f%%\n", comp[11]);

    printf("\n  CAMINHO B (parou de pagar):\n");
    printf("    PIB final: R$ %.1f trilhoes\n", comp[3]);
    printf("    Divida final: R$ %.1f trilhoes\n", comp[7]);
    printf("    Pobreza: %.1f%%\n", comp[10]);
    printf("    Desemprego: %.1f%%\n", comp[12]);
    printf("    Dinheiro liberado (20 anos): R$ %.1f trilhoes\n", comp[8]);

    printf("\n  VANTAGEM DE NAO PAGAR:\n");
    printf("    PIB %.0f%% maior\n", comp[5]);
    printf("    Diferenca: R$ %.1f trilhoes\n", comp[4]);
    printf("    Crossover (ano em que ultrapassa): %d\n", cross);
    printf("\n  VENCEDOR: %s\n", comp[13] ? "NAO PAGAR" : "PAGAR");

    printf("\n======================================================================\n");
    printf("CONCLUSAO\n");
    printf("======================================================================\n\n");
    printf("  O agiota diz que e o fim do mundo se voce parar de pagar.\n");
    printf("  A simulacao mostra que em 3-5 anos o pais RECUPERA.\n");
    printf("  Em 10 anos, esta NA FRENTE.\n");
    printf("  Em 20 anos, e OUTRO PAIS.\n\n");
    printf("  O curto prazo doi. O longo prazo liberta.\n");
    printf("  Continuar pagando doi PARA SEMPRE.\n\n");
    printf("  O agiota so tem poder se voce tiver MEDO.\n");
    printf("  O medo e a arma. A verdade e o antidoto.\n\n");
    printf("  'O Ideal guia. O Executavel opera.'\n");

    return 0;
}