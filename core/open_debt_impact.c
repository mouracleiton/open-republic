// OpenDebtImpact -- Todos os Impactos da Divida na Vida Humana
// ====================================================================
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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_AREAS 15
#define MAX_YEARS 21
#define MAX_LINE 512

// ============================================================================
// 1. AREAS DE IMPACTO
// ============================================================================

typedef enum {
    IMPACT_EDUCATION,
    IMPACT_HEALTH_MENTAL,
    IMPACT_HOUSING,
    IMPACT_FOOD_SECURITY,
    IMPACT_INFRASTRUCTURE,
    IMPACT_SANITATION,
    IMPACT_SCIENCE_TECH,
    IMPACT_CULTURE_ARTS,
    IMPACT_INEQUALITY,
    IMPACT_ENVIRONMENT,
    IMPACT_SECURITY,
    IMPACT_SPORT,
    IMPACT_TRANSPORT,
    IMPACT_CONNECTIVITY,
    IMPACT_CHILDHOOD
} ImpactArea;

typedef enum {
    SEVERITY_CRITICAL,
    SEVERITY_SEVERE,
    SEVERITY_HIGH,
    SEVERITY_MODERATE,
    SEVERITY_LOW
} SeverityLevel;

typedef struct {
    ImpactArea area;
    const char* name;
    SeverityLevel severity;
    double annual_budget_needed_brl;
    double annual_budget_actual_brl;
    double annual_budget_gap_brl;
    double pct_of_interest_that_should_go;
    int people_affected_per_year;
    double unit_cost_brl;
    const char* unit_name;
    int units_not_delivered_per_year;
    const char* description;
    const char* human_cost;
} AreaImpact;

typedef struct {
    int year_label;
    double interest_paid_brl;
    double total_gap_brl;
    int total_people_affected;
    double cumulative_gap_brl;
    int cumulative_people_affected;
} YearImpact;

typedef struct {
    int start_year;
    int years;
    double initial_debt;
    double initial_gdp;
    double interest_rate;
    double gdp_growth;
    YearImpact simulations[MAX_YEARS];
    int sim_count;
} ImpactSimulator;

// ============================================================================
// 2. CATALOGO DE IMPACTOS (15 areas) - Portuguese comments
// ============================================================================

AreaImpact AREA_IMPACTS[MAX_AREAS] = {
    {IMPACT_EDUCATION, "Educacao Basica e Superior", SEVERITY_CRITICAL,
     600e9, 180e9, 420e9, 0.15, 50000000, 5e6, "escolas", 84000,
     "Educacao publica subfinanciada ha decadas.",
     "Criancas em escolas sem teto, sem merenda, sem professor. Universitarios sem bolsa. Analfabetismo funcional em 30% dos adultos."},
    {IMPACT_HEALTH_MENTAL, "Saude Mental", SEVERITY_SEVERE,
     80e9, 4e9, 76e9, 0.03, 20000000, 200000, "CAPS (centro de saude mental)", 380000,
     "Brasil tem 20 milhoes com transtorno mental. So 5% do orcamento necessario.",
     "Depressao nao tratada. Ansiedade cronica. Suicidios. Crack. Sem psicologo no SUS."},
    {IMPACT_HOUSING, "Moradia Digna", SEVERITY_CRITICAL,
     200e9, 15e9, 185e9, 0.10, 8000000, 80000, "casas populares", 2312500,
     "Deficit habitacional de 8 milhoes de familias.",
     "Familias em favelas, ruas, corticos. Criancas sem endereco fixo. Sem-teto morrendo de frio."},
    {IMPACT_FOOD_SECURITY, "Seguranca Alimentar (Fome)", SEVERITY_CRITICAL,
     120e9, 35e9, 85e9, 0.08, 33000000, 3, "refeicoes diarias", 28333333333LL,
     "33 milhoes de brasileiros passam fome. O pais da soja nao alimenta seu povo.",
     "Criancas desnutridas. Maes que pulam refeicoes. Idosos escolhendo entre comer e remedio."},
    {IMPACT_INFRASTRUCTURE, "Infraestrutura (Estradas, Energia)", SEVERITY_SEVERE,
     300e9, 60e9, 240e9, 0.12, 215000000, 20e6, "km de rodovia", 12000,
     "Estradas esburacadas. Pontes caindo. Sem investimento em energia.",
     "Acidentes fatais em estradas sem manutencao. Apagoes. Logistica cara = comida cara."},
    {IMPACT_SANITATION, "Saneamento Basico", SEVERITY_SEVERE,
     100e9, 12e9, 88e9, 0.05, 100000000, 12000, "ligacoes de agua/esgoto", 7333333,
     "Metade do Brasil nao tem esgoto tratado. Doencas por agua contaminada.",
     "Criancas com diarreia. Dengue. Leptospirose nas enchentes. Agua nao potavel."},
    {IMPACT_SCIENCE_TECH, "Ciencia e Tecnologia", SEVERITY_SEVERE,
     80e9, 8e9, 72e9, 0.04, 500000, 500000, "bolsas de pesquisa", 144000,
     "CNPq e Capes com orcamento destroicado. Cerebros fugindo do pais.",
     "Pesquisadores no radar de UBER. Doutores desempregados. Laboratorios fechados. Patentes perdidas."},
    {IMPACT_CULTURE_ARTS, "Cultura e Arte", SEVERITY_HIGH,
     30e9, 3e9, 27e9, 0.02, 10000000, 100000, "producoes culturais", 270000,
     "Cultura tratada como luxo. Artistas sem renda. Museus fechados.",
     "Teatros fechados. Cinema nacional morto. Musicos sem espaco. Identidade cultural apagada."},
    {IMPACT_INEQUALITY, "Desigualdade de Renda", SEVERITY_CRITICAL,
     500e9, 50e9, 450e9, 0.15, 150000000, 500, "transferencias de renda/mes", 900000000,
     "Brasil entre os 10 paises mais desiguais do mundo. Gini = 0.52.",
     "1% tem 50% da riqueza. Milhoes vivem com R$ 200/mes. Favelas ao lado de condominios."},
    {IMPACT_ENVIRONMENT, "Meio Ambiente", SEVERITY_SEVERE,
     50e9, 5e9, 45e9, 0.03, 215000000, 100000, "km2 protegidos/fiscalizados", 450000,
     "Desmatamento da Amazonia acelerando. IBAMA sem orcamento.",
     "Amazonia queimando. Agua acabando. Temperatura subindo. Futuro climatico destruido."},
    {IMPACT_SECURITY, "Seguranca Publica", SEVERITY_SEVERE,
     150e9, 70e9, 80e9, 0.05, 60000000, 2000000, "delegacias equipadas", 40000,
     "47 mil homicidios/ano. Mulheres mortas. LGBTQIA+ assassinados.",
     "Maes chorando filhos. Criancas sem pai. Medo de sair de casa. Violencia domestica."},
    {IMPACT_SPORT, "Esporte e Lazer", SEVERITY_MODERATE,
     20e9, 2e9, 18e9, 0.01, 40000000, 300000, "quadras esportivas", 60000,
     "Esporte como ferramenta de resgate social destruido.",
     "Criancas sem quadra. Jovens sem esporte = sem alternativa ao crime. Talentos perdidos."},
    {IMPACT_TRANSPORT, "Transporte Publico", SEVERITY_SEVERE,
     200e9, 30e9, 170e9, 0.08, 100000000, 100000000, "km de metro/onibus", 1700,
     "Metro sem expansao. Onibus lotados. Povo passa 3h/dia no transito.",
     "3 horas/dia no onibus lotado. Menos tempo com familia. Menos estudo. Mais estresse."},
    {IMPACT_CONNECTIVITY, "Internet e Conectividade", SEVERITY_HIGH,
     40e9, 5e9, 35e9, 0.02, 70000000, 5000, "conexoes de internet", 7000000,
     "70 milhoes sem internet de qualidade. Exclusao digital.",
     "Criancas estudando no celular 3G. Sem telemedicina. Sem servicos publicos digitais."},
    {IMPACT_CHILDHOOD, "Primeira Infancia (0-6 anos)", SEVERITY_CRITICAL,
     80e9, 8e9, 72e9, 0.04, 12000000, 1000000, "vagas em creches", 72000,
     "12 milhoes de criancas 0-6 sem creche. Desenvolvimento comprometido.",
     "Maes sem trabalhar porque nao tem creche. Criancas em casa sem estimulo. Futuro comprometido."}
};

// ============================================================================
// 3. SIMULACAO ANO A ANO (20 anos)
// ============================================================================

void simulate(ImpactSimulator* sim) {
    double debt = sim->initial_debt;
    double gdp = sim->initial_gdp;
    double cumulative_gap = 0.0;
    int cumulative_people = 0;
    sim->sim_count = 0;

    for (int i = 0; i <= sim->years; i++) {
        int year_label = sim->start_year + i;
        double interest = debt * sim->interest_rate;
        double total_gap = 0.0;
        int total_people = 0;

        for (int j = 0; j < MAX_AREAS; j++) {
            AreaImpact* ai = &AREA_IMPACTS[j];
            double inflation_factor = pow(1.05, i);
            double gap = ai->annual_budget_gap_brl * inflation_factor;
            int people = ai->people_affected_per_year;
            total_gap += gap;
            total_people += people;
        }

        cumulative_gap += total_gap;
        cumulative_people += total_people;

        sim->simulations[i].year_label = year_label;
        sim->simulations[i].interest_paid_brl = interest;
        sim->simulations[i].total_gap_brl = total_gap;
        sim->simulations[i].total_people_affected = total_people;
        sim->simulations[i].cumulative_gap_brl = cumulative_gap;
        sim->simulations[i].cumulative_people_affected = cumulative_people;
        sim->sim_count++;

        debt = debt + interest - (gdp * 0.18 * 0.3);
        gdp = gdp * (1 + sim->gdp_growth);
    }
}

double total_gap_all_years(ImpactSimulator* sim) {
    return sim->simulations[sim->sim_count-1].cumulative_gap_brl;
}

double total_interest_all_years(ImpactSimulator* sim) {
    double sum = 0.0;
    for (int i = 0; i < sim->sim_count; i++) sum += sim->simulations[i].interest_paid_brl;
    return sum;
}

// ============================================================================
// 4. RENDERIZACOES VISUAIS - Portuguese comments
// ============================================================================

void render_area_chart(ImpactSimulator* sim) {
    YearImpact* s = &sim->simulations[0];
    printf("\n===========================================================================\n");
    printf("  DEFICIT POR AREA -- %d (R$ bilhoes)\n", s->year_label);
    printf("===========================================================================\n\n");

    // Simple bar rendering
    double max_gap = 0;
    for (int j = 0; j < MAX_AREAS; j++) {
        AreaImpact* ai = &AREA_IMPACTS[j];
        double inflation_factor = pow(1.05, 0);
        double gap = ai->annual_budget_gap_brl * inflation_factor;
        if (gap > max_gap) max_gap = gap;
    }

    for (int j = 0; j < MAX_AREAS; j++) {
        AreaImpact* ai = &AREA_IMPACTS[j];
        double inflation_factor = pow(1.05, 0);
        double gap = ai->annual_budget_gap_brl * inflation_factor;
        double gap_bi = gap / 1e9;
        int bar_len = (int)((gap / max_gap) * 40);
        if (bar_len < 1) bar_len = 1;
        char bar[64] = {0};
        memset(bar, 'X', bar_len);
        const char* sev = (ai->severity == SEVERITY_CRITICAL) ? "CRIT" : (ai->severity == SEVERITY_SEVERE) ? "SEVE" : (ai->severity == SEVERITY_HIGH) ? "HIGH" : (ai->severity == SEVERITY_MODERATE) ? "MODE" : "LOW";
        printf("  %-35s R$%7.0fbi [%s] %s\n", ai->name, gap_bi, bar, sev);
    }
    printf("\n  X = deficit orcamentario (dinheiro que FOI PRO JUROS)\n");
    printf("  TOTAL DEFICIT/ANO: R$ %.0f bilhoes\n", s->total_gap_brl / 1e9);
    printf("  PESSOAS AFETADAS/ANO: %d\n\n", s->total_people_affected);
}

void render_cumulative_chart(ImpactSimulator* sim) {
    printf("\n======================================================================\n");
    printf("  DEFICIT ACUMULADO POR ANO (R$ trilhoes)\n");
    printf("======================================================================\n\n");
    double max_val = sim->simulations[sim->sim_count-1].cumulative_gap_brl;
    for (int i = 0; i < sim->sim_count; i++) {
        YearImpact* s = &sim->simulations[i];
        double val_t = s->cumulative_gap_brl / 1e12;
        int bar_len = (int)((s->cumulative_gap_brl / max_val) * 50);
        if (bar_len < 1) bar_len = 1;
        char bar[64] = {0};
        memset(bar, '#', bar_len);
        printf("  %d |%s| R$ %.1fT\n", s->year_label, bar, val_t);
    }
    printf("\n  Em %d: R$ %.1f trilhoes ROUBADOS\n", sim->simulations[sim->sim_count-1].year_label, sim->simulations[sim->sim_count-1].cumulative_gap_brl / 1e12);
    printf("  de educacao, saude, moradia, ciencia, cultura...\n\n");
}

void render_human_cost() {
    printf("\n======================================================================\n");
    printf("  O CUSTO HUMANO -- O QUE A DIVIDA DESTRÓI\n");
    printf("======================================================================\n");
    for (int j = 0; j < MAX_AREAS; j++) {
        AreaImpact* ai = &AREA_IMPACTS[j];
        const char* sev = (ai->severity == SEVERITY_CRITICAL) ? "CRITICO" : (ai->severity == SEVERITY_SEVERE) ? "SEVERO" : (ai->severity == SEVERITY_HIGH) ? "ALTO" : (ai->severity == SEVERITY_MODERATE) ? "MODERADO" : "BAIXO";
        printf("\n  %s [%s]\n", ai->name, sev);
        printf("  Deficit: R$ %.0f bilhoes/ano\n", ai->annual_budget_gap_brl / 1e9);
        printf("  Pessoas afetadas: %d/ano\n", ai->people_affected_per_year);
        printf("  Nao entregue: %d %s/ano\n", ai->units_not_delivered_per_year, ai->unit_name);
        printf("  CUSTO HUMANO: %s\n", ai->human_cost);
        printf("  %s\n", "──────────────────────────────────────────────────────────────────");
    }
    printf("\n");
}

void render_equivalence_table() {
    printf("\n======================================================================\n");
    printf("  O QUE R$ 100 BILHOES DE JUROS ROUBOU DO POVO\n");
    printf("  (equivalencia: se esse dinheiro ficasse no Brasil)\n");
    printf("======================================================================\n\n");
    printf("  %-35s %15s\n", "RECURSO", "QTD");
    printf("  %s\n", "----------------------------------------------------");

    const char* labels[16] = {
        "Escolas completas (R$ 5M)", "Hospitais (R$ 50M)", "Casas populares (R$ 80k)",
        "Creches (R$ 1M)", "CAPS saude mental (R$ 200k)", "Bolsas pesquisa (R$ 500k/ano)",
        "Quadras esportivas (R$ 300k)", "Delegacias equipadas (R$ 2M)", "km de rodovia (R$ 20M)",
        "km de metro/onibus (R$ 100M)", "Ligacoes de agua/esgoto (R$ 12k)", "Conexoes de internet (R$ 5k)",
        "Refeicoes (R$ 3)", "Producoes culturais (R$ 100k)", "Transferencias de renda/mes (R$ 500)",
        "Vagas em creches (R$ 1M)"
    };
    double costs[16] = {5e6,50e6,8e4,1e6,2e5,5e5,3e5,2e6,2e7,1e8,12e3,5e3,3,1e5,500,1e6};

    for (int i = 0; i < 16; i++) {
        long long qty = (long long)(100e9 / costs[i]);
        char qty_str[32];
        if (qty >= 1000000000LL) sprintf(qty_str, "%.1f bilhoes", qty/1e9);
        else if (qty >= 1000000LL) sprintf(qty_str, "%.1f milhoes", qty/1e6);
        else if (qty >= 1000LL) sprintf(qty_str, "%lld mil", qty/1000);
        else sprintf(qty_str, "%lld", qty);
        printf("  %-35s %15s\n", labels[i], qty_str);
    }
    printf("\n  Cada R$ 100 bilhoes para o agiota e TUDO ISSO que nao existe.\n");
    printf("  O Brasil paga R$ 720 bilhoes/ano em juros.\n");
    printf("  Sao 7x essa tabela. TODO ANO.\n\n");
}

void render_comparison_other_countries() {
    printf("\n======================================================================\n");
    printf("  INVESTIMENTO PUBLICO POR HABITANTE/ANO\n");
    printf("  (Brasil vs paises que NAO tem divida extorsiva)\n");
    printf("======================================================================\n\n");
    printf("  %-12s %15s  %30s\n", "PAIS", "R$/pessoa/ano", "BAR");
    printf("  %s\n", "------------------------------------------------------------");

    const char* countries[7] = {"Noruega","Dinamarca","Suecia","Alemanha","Holanda","Canada","Brasil"};
    int values[7] = {25000,22000,20000,18000,17000,16000,3500};
    const char* notes[7] = {"Defaultou divida em 1905. Hoje e modelo.","Estado de bem-estar. Sem divida extorsiva.","Investimento publico massivo.","Divida controlada. Investe no povo.","Infraestrutura de ponta.","Saude e educacao gratuitas.","Paga R$ 720 bi/ano em juros. Sobra R$ 3.500/pessoa."};

    int max_val = 25000;
    for (int i = 0; i < 7; i++) {
        int bar_len = (int)((values[i] / (double)max_val) * 30);
        if (bar_len < 1) bar_len = 1;
        char bar[64] = {0}; memset(bar, '#', bar_len);
        const char* marker = (strcmp(countries[i],"Brasil")==0) ? " <<<" : "";
        printf("  %-12s R$ %10d  [%s]%s\n", countries[i], values[i], bar, marker);
    }
    printf("\n  Brasil investe 7x MENOS por pessoa que paises ricos.\n");
    printf("  Nao e coincidencia. E a DIVIDA.\n");
    printf("  O dinheiro que iria pro povo vai pro AGIOTA.\n\n");
}

void render_narrative(ImpactSimulator* sim) {
    YearImpact* s0 = &sim->simulations[0];
    YearImpact* last = &sim->simulations[sim->sim_count-1];
    printf("\n======================================================================\n");
    printf("NARRATIVA\n");
    printf("======================================================================\n");
    printf("Vou te mostrar o que a divida faz. Nao so matar. Mas DESTRUIR. ");
    printf("Em %d, o Brasil pagou R$ %.0f bilhoes em juros. ", s0->year_label, s0->interest_paid_brl/1e9);
    printf("Esse dinheiro deveria ter ido para %d areas da sua vida: ", MAX_AREAS);
    printf("Educacao: 50 milhoes de alunos em escolas destruidas. ");
    printf("Saude mental: 20 milhoes de brasileiros sem tratamento. ");
    printf("Moradia: 8 milhoes de familias sem casa digna. ");
    printf("Comida: 33 milhoes passando fome. ");
    printf("Saneamento: 100 milhoes sem esgoto. ");
    printf("Ciencia: pesquisadores no UBER. ");
    printf("Cultura: teatros fechados, artistas sem teto. ");
    printf("Esporte: criancas sem quadra. ");
    printf("Internet: 70 milhoes sem conexao. ");
    printf("Creches: 12 milhoes de criancas abandonadas. ");
    printf("Em %d, o deficit acumulado sera de R$ %.0f trilhoes. ", last->year_label, last->cumulative_gap_brl/1e12);
    printf("Dinheiro que foi ROUBADO de cada area que faz a vida valer a pena. ");
    printf("A divida nao so mata. Ela CASTRA. Castra a educacao. Castra a ciencia. Castra a moradia. Castra o futuro. ");
    printf("Cada real pro agiota e um real roubado do seu filho. Da sua escola. Do seu hospital. Da sua casa. ");
    printf("Da sua cultura. Do seu esporte. Da sua internet. ");
    printf("A divida MATA. E o que ela nao mata, ela DESTRÓI.\n\n");
}

// ============================================================================
// 5. DEMONSTRACAO (main)
// ============================================================================

int main() {
    printf("======================================================================\n");
    printf("OpenDebtImpact -- Todos os Impactos da Divida\n");
    printf("======================================================================\n");

    ImpactSimulator sim = {2024, 20, 6.0e12, 10.0e12, 0.12, 0.025, {{0}}, 0};
    simulate(&sim);

    int crit = 0, sev = 0;
    for (int j = 0; j < MAX_AREAS; j++) {
        if (AREA_IMPACTS[j].severity == SEVERITY_CRITICAL) crit++;
        if (AREA_IMPACTS[j].severity == SEVERITY_SEVERE) sev++;
    }
    printf("\nAreas impactadas: %d\n", MAX_AREAS);
    printf("Severidade critica: %d\n", crit);
    printf("Severidade severa: %d\n", sev);

    render_area_chart(&sim);
    render_human_cost();
    render_equivalence_table();
    render_comparison_other_countries();
    render_cumulative_chart(&sim);
    render_narrative(&sim);

    double total_gap_t = total_gap_all_years(&sim) / 1e12;
    double total_int_t = total_interest_all_years(&sim) / 1e12;
    printf("======================================================================\n");
    printf("RESUMO\n");
    printf("======================================================================\n");
    printf("  Areas impactadas: %d\n", MAX_AREAS);
    printf("  Pessoas afetadas/ano: %d\n", sim.simulations[0].total_people_affected);
    printf("  Deficit total em %d anos: R$ %.1f trilhoes\n", sim.years, total_gap_t);
    printf("  Juros pagos no periodo: R$ %.1f trilhoes\n", total_int_t);
    printf("  Deficit medio/ano: R$ %.1f trilhoes\n", total_gap_t / sim.years);

    printf("\n======================================================================\n");
    printf("VEREDICTO\n");
    printf("======================================================================\n\n");
    printf("  A divida MATA (OpenDebtMortality).\n");
    printf("  E o que ela nao mata, ela DESTRÓI (este modulo).\n\n");
    printf("  Em %d anos:\n", sim.years);
    printf("  R$ %.0f trilhoes ROUBADOS\n", total_gap_t);
    printf("  de educacao, saude, moradia, ciencia, cultura, esporte,\n");
    printf("  meio ambiente, seguranca, transporte, conectividade, infancia.\n\n");
    printf("  %d areas destruidas.\n", MAX_AREAS);
    printf("  %.0f milhoes de pessoas/ano afetadas.\n\n", sim.simulations[0].total_people_affected / 1e6);
    printf("  Cada parcela da divida e uma escola que nao existe.\n");
    printf("  Cada juros pago e uma creche que nao foi construida.\n");
    printf("  Cada bilhao pro agiota e mil futuros cancelados.\n\n");
    printf("  A divida MATA. E DESTRÓI. E CASTRA.\n");
    printf("  Nao renegociar. Nao alongar. EXTINGUIR.\n\n");
    printf("  'Nao existe pobreza, existe MISERIA.'\n");
    printf("  A divida e a maquina que PRODUZ a miseria.\n");

    return 0;
}
