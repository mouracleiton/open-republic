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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// ============================================================================
// 1. CAUSAS DE MORTE EVITAVEIS (vinculadas a subfinanciamento)
// ============================================================================

typedef enum {
    HEALTHCARE_SHORTAGE = 0,   // morreu na fila do SUS
    CHILD_MORTALITY,           // bebe nao sobreviveu
    MATERNAL_DEATH,            // mae morreu no parto
    MALNUTRITION,              // morreu de fome
    PREVENTABLE_DISEASE,       // vacina/exame nao chegou
    VIOLENCE,                  // sem programa social
    SUICIDE,                   // sem saude mental
    SANITATION,                // agua contaminada
    ROAD_DEATH,                // estrada sem manutencao
    HEAT_COLD,                 // sem teto/climatizacao
    DRUG_OVERDOSE,             // sem tratamento
    CANCER_UNTREATED,          // fila de quimio
    HEART_UNTREATED,           // sem UTI
    NEONATAL                   // sem UTI neonatal
} PreventableDeathCategory;

const char* PreventableDeathCategory_names[] = {
    "falta_sus",
    "mortalidade_infantil",
    "morte_materna",
    "desnutricao",
    "doenca_evitavel",
    "violencia",
    "suicidio",
    "saneamento",
    "transito",
    "calor_frio",
    "overdose",
    "cancer_sem_tratamento",
    "coracao_sem_atendimento",
    "neonatal"
};

typedef struct {
    PreventableDeathCategory category;
    const char* name;
    double cost_to_save_one_life_brl;
    int deaths_per_year_brazil;
    double pct_linked_to_underfunding;
    const char* description;
} DeathCost;

int DeathCost_deaths_preventable(DeathCost* dc) {
    return (int)(dc->deaths_per_year_brazil * dc->pct_linked_to_underfunding);
}

double DeathCost_lives_saved_per_billion(DeathCost* dc) {
    if (dc->cost_to_save_one_life_brl <= 0) return 0;
    return 1e9 / dc->cost_to_save_one_life_brl;
}

// ============================================================================
// 2. TABELA DE MORTALIDADE (Dados baseados em OMS/IBGE/Datasus)
// ============================================================================

DeathCost DEATH_COSTS[] = {
    {HEALTHCARE_SHORTAGE, "Morte na fila do SUS", 500000, 124000, 0.60, "Pessoas que morrem esperando cirurgia, exame, consulta, UTI."},
    {CHILD_MORTALITY, "Mortalidade infantil (0-5 anos)", 80000, 40000, 0.70, "Criancas que morrem antes dos 5 anos por falta de atendimento."},
    {MATERNAL_DEATH, "Morte materna (no parto)", 50000, 1800, 0.80, "Maes que morrem no parto por falta de estrutura hospitalar."},
    {MALNUTRITION, "Desnutricao", 15000, 5000, 0.90, "Pessoas que morrem de fome ou desnutricao grave no Brasil."},
    {PREVENTABLE_DISEASE, "Doencas evitaveis (vacina/exame)", 20000, 50000, 0.65, "Mortes por doencas que vacina ou exame precoce previniria."},
    {VIOLENCE, "Violencia / Homicidio", 300000, 47000, 0.40, "Jovens mortos por violencia. Programa social reduz 40%."},
    {SUICIDE, "Suicidio (sem saude mental)", 100000, 14000, 0.55, "Pessoas que se matam por falta de atendimento psicologico."},
    {SANITATION, "Doenças por falta de saneamento", 40000, 8000, 0.85, "Mortes por diarreia, leptospirose, hepatite por agua suja."},
    {ROAD_DEATH, "Morte no transito", 2000000, 30000, 0.35, "Acidentes em estradas sem manutencao ou sinalizacao."},
    {CANCER_UNTREATED, "Cancer sem tratamento a tempo", 800000, 35000, 0.50, "Pessoas que morrem esperando tratamento de cancer no SUS."},
    {HEART_UNTREATED, "Infarto sem atendimento", 600000, 100000, 0.30, "Infartos que UTI/SAMU salvaria se chegasse a tempo."},
    {NEONATAL, "Morte neonatal", 120000, 19000, 0.65, "Bebe que morre nos primeiros 28 dias por falta de UTI neonatal."},
};

const int DEATH_COSTS_COUNT = 12;

// ============================================================================
// 3. SIMULACAO ANO A ANO
// ============================================================================

typedef struct {
    int year_label;
    double interest_paid_brl;
    double gdp_brl;
    int total_preventable_deaths;
    int deaths_linked_to_debt;
    int potential_lives_saved;
    int hospitals_not_built;
    int people_without_doctor;
    int children_not_vaccinated;
    int houses_not_built;
    int meals_not_served;
    int cumulative_deaths_by_debt;
} YearMortality;

typedef struct {
    int start_year;
    int years;
    double initial_debt;
    double initial_gdp;
    double interest_rate;
    double gdp_growth;
    double population;
    double fraction_to_health;
    double fraction_to_food;
    double fraction_to_housing;
    double fraction_to_education;
    double fraction_to_infra;
    YearMortality* simulations;
    int sim_count;
} DebtMortalitySimulator;

void DebtMortalitySimulator_init(DebtMortalitySimulator* sim, int start_year, int years) {
    sim->start_year = start_year;
    sim->years = years;
    sim->initial_debt = 6.0e12;
    sim->initial_gdp = 10.0e12;
    sim->interest_rate = 0.12;
    sim->gdp_growth = 0.025;
    sim->population = 215e6;
    sim->fraction_to_health = 0.40;
    sim->fraction_to_food = 0.15;
    sim->fraction_to_housing = 0.15;
    sim->fraction_to_education = 0.15;
    sim->fraction_to_infra = 0.15;
    sim->simulations = NULL;
    sim->sim_count = 0;
}

void DebtMortalitySimulator_simulate(DebtMortalitySimulator* sim) {
    if (sim->simulations) free(sim->simulations);
    sim->simulations = (YearMortality*)malloc((sim->years + 1) * sizeof(YearMortality));
    sim->sim_count = sim->years + 1;

    double debt = sim->initial_debt;
    double gdp = sim->initial_gdp;
    int cumulative_deaths = 0;

    for (int i = 0; i <= sim->years; i++) {
        int year_label = sim->start_year + i;
        double interest = debt * sim->interest_rate;
        double money_for_health = interest * sim->fraction_to_health;
        double money_for_food = interest * sim->fraction_to_food;

        int potential_saved = 0;
        for (int j = 0; j < DEATH_COSTS_COUNT; j++) {
            double lives_saved = money_for_health * 0.3 / DEATH_COSTS[j].cost_to_save_one_life_brl;
            potential_saved += (int)lives_saved;
        }

        int total_preventable = 0;
        for (int j = 0; j < DEATH_COSTS_COUNT; j++) {
            total_preventable += DeathCost_deaths_preventable(&DEATH_COSTS[j]);
        }

        int deaths_by_debt = (potential_saved < total_preventable) ? potential_saved : total_preventable;

        int hospitals_not_built = (int)(money_for_health / 50e6);
        int people_without_doctor = (int)(money_for_health / 3000);
        int children_not_vaccinated = (int)(money_for_health / 50);
        int houses_not_built = (int)((interest * sim->fraction_to_housing) / 80000);
        int meals_not_served = (int)(money_for_food / 3);

        cumulative_deaths += deaths_by_debt;

        sim->simulations[i].year_label = year_label;
        sim->simulations[i].interest_paid_brl = interest;
        sim->simulations[i].gdp_brl = gdp;
        sim->simulations[i].total_preventable_deaths = total_preventable;
        sim->simulations[i].deaths_linked_to_debt = deaths_by_debt;
        sim->simulations[i].potential_lives_saved = potential_saved;
        sim->simulations[i].hospitals_not_built = hospitals_not_built;
        sim->simulations[i].people_without_doctor = people_without_doctor;
        sim->simulations[i].children_not_vaccinated = children_not_vaccinated;
        sim->simulations[i].houses_not_built = houses_not_built;
        sim->simulations[i].meals_not_served = meals_not_served;
        sim->simulations[i].cumulative_deaths_by_debt = cumulative_deaths;

        debt = debt + interest - (gdp * 0.18 * 0.3);
        gdp = gdp * (1 + sim->gdp_growth);
    }
}

int DebtMortalitySimulator_total_deaths_by_debt(DebtMortalitySimulator* sim) {
    if (sim->sim_count == 0) return 0;
    return sim->simulations[sim->sim_count - 1].cumulative_deaths_by_debt;
}

double DebtMortalitySimulator_total_interest_paid(DebtMortalitySimulator* sim) {
    double total = 0;
    for (int i = 0; i < sim->sim_count; i++) {
        total += sim->simulations[i].interest_paid_brl;
    }
    return total;
}

double DebtMortalitySimulator_death_per_trillion_interest(DebtMortalitySimulator* sim) {
    double total_int = DebtMortalitySimulator_total_interest_paid(sim);
    if (total_int == 0) return 0;
    return DebtMortalitySimulator_total_deaths_by_debt(sim) / (total_int / 1e12);
}

void DebtMortalitySimulator_summary(DebtMortalitySimulator* sim, char* out) {
    YearMortality* last = (sim->sim_count > 0) ? &sim->simulations[sim->sim_count-1] : NULL;
    sprintf(out,
        "years_simulated: %d\n"
        "total_deaths_by_debt: %d\n"
        "total_interest_paid_trillions: %.1f\n"
        "deaths_per_trillion_interest: %.0f\n"
        "avg_deaths_per_year: %.0f\n"
        "final_year_hospitals_not_built: %d\n"
        "final_year_meals_not_served: %d\n"
        "final_year_children_not_vaccinated: %d\n",
        sim->years,
        DebtMortalitySimulator_total_deaths_by_debt(sim),
        DebtMortalitySimulator_total_interest_paid(sim) / 1e12,
        DebtMortalitySimulator_death_per_trillion_interest(sim),
        (double)DebtMortalitySimulator_total_deaths_by_debt(sim) / sim->years,
        last ? last->hospitals_not_built : 0,
        last ? last->meals_not_served : 0,
        last ? last->children_not_vaccinated : 0
    );
}

// ============================================================================
// 4. QUEM O BRASIL PAGA (paises credores)
// ============================================================================

typedef struct {
    const char* country;
    double amount_received_brl;
    const char* flag;
    const char* description;
} CountryCreditor;

CountryCreditor COUNTRY_CREDITORS[] = {
    {"Estados Unidos", 180e9, "EUA", "Fundos de investimento e bancos americanos recebem bilhoes em juros."},
    {"Reino Unido", 80e9, "UK", "Londres e centro de vulture funds que lucram com divida alheia."},
    {"Alemanha", 50e9, "DE", "Bancos alemaes detem titulos brasileiros."},
    {"Japao", 40e9, "JP", "Fundos japoneses investem em divida soberana."},
    {"Franca", 35e9, "FR", "Bancos franceses (BNP, SocGen) detem titulos."},
    {"Suica", 30e9, "CH", "Centro de banca privada que lucra com juros."},
    {"China", 25e9, "CN", "Bancos chineses compraram titulos brasileiros."},
    {"Holanda", 20e9, "NL", "Centro financeiro (Amsterda) roteia investimentos."},
    {"Luxemburgo", 15e9, "LU", "Paraiso fiscal que abriga fundos especulativos."},
    {"Outros", 25e9, "??", "Outros paises e fundos internacionais."},
};

const int COUNTRY_CREDITORS_COUNT = 10;

// ============================================================================
// 5. RENDERIZACOES VISUAIS
// ============================================================================

char* render_death_chart(YearMortality* simulations, int count) {
    static char buf[8192];
    char* p = buf;
    p += sprintf(p, "\n======================================================================\n");
    p += sprintf(p, "  MORTES POR ANO CAUSADAS PELA DIVIDA\n");
    p += sprintf(p, "  (pessoas que morreriam VIVAS se o juros fosse investido em saude)\n");
    p += sprintf(p, "======================================================================\n\n");

    int max_deaths = 1;
    for (int i = 0; i < count; i++) if (simulations[i].deaths_linked_to_debt > max_deaths) max_deaths = simulations[i].deaths_linked_to_debt;
    if (max_deaths == 0) max_deaths = 1;

    for (int i = 0; i < count; i++) {
        int bar_len = (int)((simulations[i].deaths_linked_to_debt / (double)max_deaths) * 50);
        if (bar_len < 1) bar_len = 1;
        p += sprintf(p, "  %d |", simulations[i].year_label);
        for (int j = 0; j < bar_len; j++) *p++ = '#';
        for (int j = bar_len; j < 50; j++) *p++ = ' ';
        p += sprintf(p, "| %8d mortes\n", simulations[i].deaths_linked_to_debt);
    }

    p += sprintf(p, "\n  Cada # representa ~%d mortes\n", max_deaths / 50);
    p += sprintf(p, "  TOTAL ACUMULADO: %d mortes\n", simulations[count-1].cumulative_deaths_by_debt);
    p += sprintf(p, "  em %d anos\n\n", count-1);
    return buf;
}

char* render_country_deaths() {
    static char buf[8192];
    char* p = buf;
    p += sprintf(p, "\n======================================================================\n");
    p += sprintf(p, "  PARA QUEM O BRASIL PAGA -- E QUANTOS MORREM POR ISSO\n");
    p += sprintf(p, "======================================================================\n\n");

    double total_received = 0;
    for (int i = 0; i < COUNTRY_CREDITORS_COUNT; i++) total_received += COUNTRY_CREDITORS[i].amount_received_brl;

    for (int i = 0; i < COUNTRY_CREDITORS_COUNT; i++) {
        double pct = (COUNTRY_CREDITORS[i].amount_received_brl / total_received) * 100;
        int deaths_caused = (int)(COUNTRY_CREDITORS[i].amount_received_brl / 500000);
        int bar_len = (int)pct;
        p += sprintf(p, "  %-15s R$ %6.0f bi/ano [", COUNTRY_CREDITORS[i].country, COUNTRY_CREDITORS[i].amount_received_brl / 1e9);
        for (int j = 0; j < bar_len && j < 20; j++) *p++ = '$';
        for (int j = bar_len; j < 20; j++) *p++ = ' ';
        p += sprintf(p, "] %5.1f%%  ~%d mortes\n", pct, deaths_caused);
    }

    p += sprintf(p, "\n  TOTAL ENVIADO AO EXTERIOR: R$ %.0f bilhoes/ano\n", total_received / 1e9);
    p += sprintf(p, "  MORTES CAUSADAS: ~%d por ano\n", (int)(total_received / 500000));
    p += sprintf(p, "  Cada $ = R$ %.0f bilhoes que sai do Brasil\n\n", total_received / 20 / 1e9);
    p += sprintf(p, "  Cada real enviado ao agiota international e uma vida\n");
    p += sprintf(p, "  que NAO foi salva no Brasil.\n\n");
    return buf;
}

char* render_category_breakdown() {
    static char buf[16384];
    char* p = buf;
    p += sprintf(p, "\n======================================================================\n");
    p += sprintf(p, "  MORTES EVITAVEIS NO BRASIL (por categoria, por ano)\n");
    p += sprintf(p, "======================================================================\n\n");

    int total_preventable = 0;
    for (int i = 0; i < DEATH_COSTS_COUNT; i++) total_preventable += DeathCost_deaths_preventable(&DEATH_COSTS[i]);

    p += sprintf(p, "%-40s %12s %15s %12s\n", "CATEGORIA", "MORTES/ANO", "CUSTO/VIDA", "EVITAVEIS");
    p += sprintf(p, "--------------------------------------------------------------------------------\n");

    for (int i = 0; i < DEATH_COSTS_COUNT; i++) {
        p += sprintf(p, "  %-38s %10d R$ %12.0f %10d\n",
            DEATH_COSTS[i].name,
            DEATH_COSTS[i].deaths_per_year_brazil,
            DEATH_COSTS[i].cost_to_save_one_life_brl,
            DeathCost_deaths_preventable(&DEATH_COSTS[i]));
    }

    p += sprintf(p, "--------------------------------------------------------------------------------\n");
    int total_deaths = 0;
    for (int i = 0; i < DEATH_COSTS_COUNT; i++) total_deaths += DEATH_COSTS[i].deaths_per_year_brazil;
    p += sprintf(p, "  %-38s %10d %15s %10d\n\n", "TOTAL", total_deaths, "", total_preventable);

    p += sprintf(p, "  Total de mortes evitaveis/ano: %d\n", total_preventable);
    p += sprintf(p, "  Isso e %.0f mortes POR DIA.\n", total_preventable / 365.0);
    p += sprintf(p, "  %.0f mortes POR HORA.\n", total_preventable / 365.0 / 24);
    p += sprintf(p, "  %.1f mortes POR MINUTO.\n\n", total_preventable / 365.0 / 24 / 60);
    p += sprintf(p, "  UMA PESSOA MORRE NO BRASIL A CADA MINUTO\n");
    p += sprintf(p, "  POR ALGO QUE DINHEIRO RESOLVERIA.\n\n");
    p += sprintf(p, "  E o dinheiro? FOI PRA O AGIOTA.\n\n");
    return buf;
}

char* render_lost_infrastructure(YearMortality* simulations) {
    static char buf[4096];
    YearMortality s = simulations[0];
    char* p = buf;
    p += sprintf(p, "\n======================================================================\n");
    p += sprintf(p, "  O QUE O BRASIL NAO CONSTRUIU EM UM ANO\n");
    p += sprintf(p, "  (%d -- R$ %.0f bi em juros)\n", s.year_label, s.interest_paid_brl / 1e9);
    p += sprintf(p, "======================================================================\n\n");

    p += sprintf(p, "  Hospitais nao construidos:        %8d\n", s.hospitals_not_built);
    p += sprintf(p, "  Casas populares nao entregues:    %8d\n", s.houses_not_built);
    p += sprintf(p, "  Pessoas sem medico de familia:    %8d\n", s.people_without_doctor);
    p += sprintf(p, "  Criancas nao vacinadas:            %8d\n", s.children_not_vaccinated);
    p += sprintf(p, "  Refeicoes nao servidas:            %8d\n\n", s.meals_not_served);

    p += sprintf(p, "  Em UM ano, o juros da divida pagou:\n");
    p += sprintf(p, "  - %d hospitais QUE NAO EXISTEM\n", s.hospitals_not_built);
    p += sprintf(p, "  - %d casas QUE NAO FORAM ENTREGUES\n", s.houses_not_built);
    p += sprintf(p, "  - %d refeicoes QUE NAO FORAM SERVIDAS\n\n", s.meals_not_served);

    p += sprintf(p, "  Cada hospital que nao existe = pessoas que morrem na fila.\n");
    p += sprintf(p, "  Cada casa que nao foi entregue = familias na rua.\n");
    p += sprintf(p, "  Cada refeicao que nao foi servida = criancas desnutridas.\n\n");
    return buf;
}

char* render_timeline_human(YearMortality* simulations, int count) {
    static char buf[8192];
    char* p = buf;
    p += sprintf(p, "\n======================================================================\n");
    p += sprintf(p, "  LINHA DO TEMPO DA MORTE\n");
    p += sprintf(p, "======================================================================\n\n");

    for (int i = 0; i < count; i++) {
        double deaths_per_day = simulations[i].deaths_linked_to_debt / 365.0;
        p += sprintf(p, "  %d:\n", simulations[i].year_label);
        p += sprintf(p, "    Juros pago: R$ %.0f bilhoes\n", simulations[i].interest_paid_brl / 1e9);
        p += sprintf(p, "    Mortes causadas pela divida: %d\n", simulations[i].deaths_linked_to_debt);
        p += sprintf(p, "    Isso sao %.0f mortes POR DIA\n", deaths_per_day);
        p += sprintf(p, "    Acumulado desde %d: %d\n\n", simulations[0].year_label, simulations[i].cumulative_deaths_by_debt);
    }

    p += sprintf(p, "  Em %d anos, a divida causou a morte de:\n", count-1);
    p += sprintf(p, "  %d PESSOAS.\n\n", simulations[count-1].cumulative_deaths_by_debt);
    p += sprintf(p, "  Isso e mais que a populacao de muitas cidades brasileiras.\n");
    p += sprintf(p, "  Mais que todas as guerras do Brasil juntas.\n");
    p += sprintf(p, "  Mais que todas as epidemias da historia recente.\n\n");
    p += sprintf(p, "  E nao foi uma bala. Foi um BOLETO.\n\n");
    return buf;
}

char* render_narrative(YearMortality* simulations, int count) {
    static char buf[8192];
    YearMortality s0 = simulations[0];
    YearMortality last = simulations[count-1];
    int total = last.cumulative_deaths_by_debt;
    char* p = buf;

    p += sprintf(p, "Vou te dizer algo que ninguem te conta. ");
    p += sprintf(p, "No ano %d, o Brasil pagou R$ %.0f bilhoes apenas em JUROS da divida publica. ", s0.year_label, s0.interest_paid_brl / 1e9);
    p += sprintf(p, "Esse dinheiro foi para bancos, fundos, paises estrangeiros. Nao foi para o SUS. Nao foi para a escola. Nao foi para a comida. ");
    p += sprintf(p, "No mesmo ano, %d brasileiros morreram por causas evitaveis. Filas do SUS. Desnutricao. Falta de medico. ", s0.deaths_linked_to_debt);
    p += sprintf(p, "Se o dinheiro dos juros tivesse ido para a saude, %d dessas pessoas poderiam estar VIVAS. ", s0.potential_lives_saved);
    p += sprintf(p, "Em %d anos, se nada mudar, a divida tera causado a morte de %d pessoas. ", count-1, total);
    p += sprintf(p, "Sao %.0f mortes por dia. A cada minuto, alguem morre porque o dinheiro que salvaria sua vida foi para o agiota. ", total / 365.0);
    p += sprintf(p, "A divida nao e um numero. E um CEMITERIO. Cada parcela paga e uma cova que nao foi aberta. Cada juros pago e uma vida que nao foi salva. A divida MATA.");
    return buf;
}

// ============================================================================
// 6. DEMONSTRACAO (main)
// ============================================================================

int main() {
    printf("======================================================================\n");
    printf("OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?\n");
    printf("======================================================================\n");

    DebtMortalitySimulator sim;
    DebtMortalitySimulator_init(&sim, 2024, 20);
    DebtMortalitySimulator_simulate(&sim);

    printf("%s", render_category_breakdown());
    printf("%s", render_country_deaths());
    printf("%s", render_lost_infrastructure(sim.simulations));
    printf("%s", render_death_chart(sim.simulations, sim.sim_count));
    printf("%s", render_timeline_human(sim.simulations, sim.sim_count));

    printf("\n======================================================================\n");
    printf("NARRATIVA (para Telefonista ler)\n");
    printf("======================================================================\n");
    printf("%s\n", render_narrative(sim.simulations, sim.sim_count));

    char summary[1024];
    DebtMortalitySimulator_summary(&sim, summary);
    printf("\n======================================================================\n");
    printf("RESUMO\n");
    printf("======================================================================\n");
    printf("%s", summary);

    printf("\n======================================================================\n");
    printf("VEREDICTO\n");
    printf("======================================================================\n\n");
    printf("  A divida publica nao e apenas impossivel de pagar.\n");
    printf("  Ela e um ASSASSINO DE MASSA silencioso.\n\n");
    printf("  Em %d anos:\n", sim.years);
    printf("  %d brasileiros morreram\n", DebtMortalitySimulator_total_deaths_by_debt(&sim));
    printf("  porque R$ %.1f trilhoes\n", DebtMortalitySimulator_total_interest_paid(&sim) / 1e12);
    printf("  foram enviados ao agiota em vez de ir para saude, comida, vida.\n\n");
    printf("  A divida MATA.\n");
    printf("  Cada juros pago e uma vida nao salva.\n");
    printf("  Nao renegociar. Nao alongar.\n");
    printf("  EXTINGUIR.\n");
    printf("  Pelas vidas que ainda podem ser salvas.\n\n");
    printf("  'Nao existe pobreza, existe MISERIA.'\n");
    printf("  A divida e a maquina que PRODUZ a miseria.\n");

    if (sim.simulations) free(sim.simulations);
    return 0;
}
