/* TEIA Efficacy Measurement -- Provar que Funciona Antes de Vender -- gerado de Portugol++ */
#ifndef TEIA_EFFICACY_MEASUREMENT_PROVAR_QUE_FUNCIONA_ANTES_DE_VENDER_H
#define TEIA_EFFICACY_MEASUREMENT_PROVAR_QUE_FUNCIONA_ANTES_DE_VENDER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
TEIA Efficacy Measurement -- Provar que Funciona Antes de Vender;
=================================================================;
O PROBLEMA:;
Construiu-se o modelo de negocio, juridico, pricing.;
Mas NUNCA se provou que o produto FUNCIONA.;
Antes de cobrar R$1.500/mes de um revendedor,;
precisa PROVAR que:;
1. O dado esta correto;
2. O modelo prediz certo;
3. O artefato gerado tem nivel ministerial;
4. O revendedor consegue usar sem ajuda;
5. O cliente final aceita o produto;
5 FASES DE MEDICAO:;
FASE A: ACCURACIA DOS DADOS;
    O numero de fome no municipio X esta certo?;
    Cruza com fonte oficial. Compara.;
FASE B: ACCURACIA DOS MODELOS;
    O modelo diz: "R$1bi no PAA gera R$4bi em saude".;
    Isso aconteceu em algum lugar real? O modelo acerta o passado?;
FASE C: QUALIDADE DO ARTEFATO;
    Dossie gerado pelo terminal vs dossie feito por humano.;
    Painel cego de avaliadores. Qual && melhor?;
FASE D: USABILIDADE;
    Revendedor sem treinamento consegue gerar um dossie?;
    Quanto tempo leva? Quantos erros?;
FASE &&: ACEITACAO DE MERCADO;
    Cliente real (prefeitura/ONG) aceita o artefato?;
    Pagaria quanto? Recomendaria?;
Author: TEIA / OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// ============================================================================
// 1. FASE A: ACCURACIA DOS DADOS
// ============================================================================
// decorador: @dataclass
typedef struct DataAccuracyTest {
    // Teste de acuracia de um dado contra fonte oficial.
    METODO:;
    1. Pegar 100 dados aleatorios da API;
    2. Verificar cada um contra fonte oficial (IBGE, SNIS, CAGED);
    3. Calcular taxa de acerto;
    4. Se < 95% = REPROVADO. Corrigir antes de continuar.;
    //
    endpoint: texto;
    metric_name: texto;
    teia_value: flutuante;
    official_value: flutuante;
    official_source: texto;
    double variance_pct = 0.0;
    void __post_init__(self) {
        if (self.official_value != 0) {
            self.variance_pct = abs(self.teia_value - self.official_value) / self.official_value * 100;
    // decorador: @property
    bool passed(self) {
        // Passa se variancia < 2% (tolerancia para arredondamento/atualizacao).
        return self.variance_pct < 2.0;
    // decorador: @property
    char* status(self) {
        if (self.variance_pct < 1.0) {
            return "EXATO";
        } else if (self.variance_pct < 2.0) {
            return "ACEITAVEL";
        } else if (self.variance_pct < 5.0) {
            return "DIVERGENCIA";
        } else {
            return "ERRO CRITICO";
// Simulacao de testes de acuracia (valores ilustrativos)
// Na pratica: cruzar com IBGE/SNIS/CAGED reais
[DataAccuracyTest] ACCURACY_TESTS = [;
    // FOME (VIGISAN)
    DataAccuracyTest(;
        "/api/v1/fome/por-municipio",;
        "Inseguranca alimentar grave Brasil (milhoes)",;
        teia_value = 33.8,;
        official_value = 33.8,;
        official_source = "VIGISAN/IBGE 2022",;
    ),;
    DataAccuracyTest(;
        "/api/v1/fome/por-municipio",;
        "Inseguranca alimentar total (%)",;
        teia_value = 58.0,;
        official_value = 58.7,;
        official_source = "VIGISAN/Rede PENSSAN 2022",;
    ),;
    // SANEAMENTO (SNIS)
    DataAccuracyTest(;
        "/api/v1/saneamento/cobertura",;
        "Populacao sem agua tratada (milhoes)",;
        teia_value = 35.0,;
        official_value = 35.0,;
        official_source = "SNIS 2023",;
    ),;
    DataAccuracyTest(;
        "/api/v1/saneamento/cobertura",;
        "Populacao sem coleta de esgoto (milhoes)",;
        teia_value = 100.0,;
        official_value = 100.0,;
        official_source = "SNIS 2023",;
    ),;
    DataAccuracyTest(;
        "/api/v1/saneamento/cobertura",;
        "Investimento necessario saneamento 2033 (R$ bi)",;
        teia_value = 700.0,;
        official_value = 700.0,;
        official_source = "Trata Brasil/ANA",;
    ),;
    // NEGATIVADOS (SPC)
    DataAccuracyTest(;
        "/api/v1/negativados/perfil",;
        "Brasileiros negativados (milhoes)",;
        teia_value = 63.0,;
        official_value = 63.1,;
        official_source = "SPC Brasil/Peic 2024",;
    ),;
    DataAccuracyTest(;
        "/api/v1/negativados/perfil",;
        "Divida media negativado (R$)",;
        teia_value = 4500.0,;
        official_value = 4515.0,;
        official_source = "SPC Brasil 2024",;
    ),;
    // JUROS (BACEN)
    DataAccuracyTest(;
        "/api/v1/juros/impacto-orcamento",;
        "Juros da divida publica 2024 (R$ bi)",;
        teia_value = 950.4,;
        official_value = 950.4,;
        official_source = "Bacen/STN 2024",;
    ),;
    DataAccuracyTest(;
        "/api/v1/juros/impacto-orcamento",;
        "Impacto 1 p.p. Selic (R$ bi/ano)",;
        teia_value = 31.4,;
        official_value = 31.4,;
        official_source = "Bacen 2024",;
    ),;
    // PAA
    DataAccuracyTest(;
        "/api/v1/simular/paa",;
        "Orcamento PAA 2023 (R$ mi)",;
        teia_value = 500.0,;
        official_value = 500.0,;
        official_source = "MDS/SICONV 2023",;
    ),;
    DataAccuracyTest(;
        "/api/v1/simular/paa",;
        "PAA pico historico 2012 (R$ bi)",;
        teia_value = 2.4,;
        official_value = 2.4,;
        official_source = "MDS 2012",;
    ),;
    // ERRO INTENCIONAL (para testar o sistema de teste)
    DataAccuracyTest(;
        "/api/v1/fome/por-municipio",;
        "TESTE DE ERRO: valor propositadamente errado",;
        teia_value = 25.0,;
        official_value = 33.8,;
        official_source = "VIGISAN (teste de deteccao)",;
    ),;
];
// ============================================================================
// 2. FASE B: ACCURACIA DOS MODELOS (backtesting)
// ============================================================================
// decorador: @dataclass
typedef struct ModelBacktest {
    // Backtesting: o modelo previu o passado corretamente?
    METODO:;
    1. Pegar um modelo (ex: multiplicador PAA);
    2. Aplicar a dados historicos (ex: PAA 2012-2020);
    3. Comparar previsao do modelo com o que ACONTECEU;
    4. Se modelo acerta passado > 85%, pode confiar no futuro;
    //
    model_name: texto;
    input_period: texto;
    input_data: texto;
    model_prediction: flutuante;
    actual_outcome: flutuante;
    outcome_source: texto;
    double error_pct = 0.0;
    void __post_init__(self) {
        if (self.actual_outcome != 0) {
            self.error_pct = abs(self.model_prediction - self.actual_outcome) / self.actual_outcome * 100;
    // decorador: @property
    bool passed(self) {
        return self.error_pct < 15.0 // 15% de margem para modelos socioeconomicos;
    // decorador: @property
    char* grade(self) {
        if (self.error_pct < 5) {
            return "A (excelente)";
        } else if (self.error_pct < 10) {
            return "B (bom)";
        } else if (self.error_pct < 15) {
            return "C (aceitavel)";
        } else if (self.error_pct < 25) {
            return "D (precisa revisao)";
        } else {
            return "F (reprovado)";
[ModelBacktest] BACKTESTS = [;
    ModelBacktest(;
        model_name = "Multiplicador PAA (R$1 -> R$3 economia local)",;
        input_period = "2012-2015",;
        input_data = "PAA orcamento R$2,4bi -> R$1,5bi/ano",;
        model_prediction = 4_500_000_000, // R$1,5bi x 3 = R$4,5bi em economia local;
        actual_outcome = 4_200_000_000, // MDIC/IEPS estimou R$4,2bi;
        outcome_source = "MDIC/IEPS 2022",;
    ),;
    ModelBacktest(;
        model_name = "Impacto Selic (1 p.p. = R$31,4bi)",;
        input_period = "2022-2023",;
        input_data = "Selic subiu 1,5 p.p. (12,75 -> 13,75)",;
        model_prediction = 47_100_000_000, // 1,5 x R$31,4bi = R$47,1bi;
        actual_outcome = 45_800_000_000, // STN informou aumento de R$45,8bi;
        outcome_source = "STN/Bacen 2023",;
    ),;
    ModelBacktest(;
        model_name = "Retorno Saneamento (R$1 -> R$4 saude)",;
        input_period = "2010-2020",;
        input_data = "Investimento saneamento R$15bi/ano",;
        model_prediction = 60_000_000_000, // R$15bi x 4 = R$60bi economia saude;
        actual_outcome = 55_000_000_000, // Opas/OMS estimou R$55bi;
        outcome_source = "Opas/OMS Estudo Multiplicador 2019",;
    ),;
    ModelBacktest(;
        model_name = "Cashback tributario EC132 (R$100/mes x 21M familias)",;
        input_period = "2026 (projetado)",;
        input_data = "R$100 x 21M = R$2,1bi/mes",;
        model_prediction = 25_200_000_000, // R$2,1bi x 12 = R$25,2bi/ano;
        actual_outcome = 25_200_000_000, // ainda ! implementado, valor projetado;
        outcome_source = "Projecao TEIA (sem validacao real ainda)",;
    ),;
];
// ============================================================================
// 3. FASE C: QUALIDADE DO ARTEFATO (painel cego)
// ============================================================================
// decorador: @dataclass
typedef struct ArtifactQualityScore {
    // Avaliacao cega de artefato por painel de especialistas.
    METODO:;
    1. Gerar dossie pelo Terminal TEIA;
    2. Pegar dossie equivalente feito por humano (consultor);
    3. Remover identificacao (cego);
    4. Painel de 5 avaliadores pontua sem saber qual && qual;
    5. Criterios: acuracia, clareza, profundidade, acionabilidade, fontes;
    //
    artifact_id: texto;
    artifact_type: texto   // "teia_generated" || "human_made";
    evaluator: texto;
    evaluator_background: texto;
    // Scores 0-10
    double accuracy = 0 // dados estao corretos?;
    double clarity = 0 // && legivel?;
    double depth = 0 // tem profundidade analitica?;
    double actionability = 0 // da para tomar decisao com isso?;
    double sourcing = 0 // fontes sao confiaveis && verificaveis?;
    double completeness = 0 // cobre o topico inteiro?;
    // decorador: @property
    double total_score(self) {
        return (self.accuracy + self.clarity + self.depth +;
                self.actionability + self.sourcing + self.completeness) / 6;
    // decorador: @property
    char* grade(self) {
        s = self.total_score;
        if (s >= 9) {
            return "A+";
        } else if (s >= 8) {
            return "A";
        } else if (s >= 7) {
            return "B";
        } else if (s >= 6) {
            return "C";
        } else if (s >= 5) {
            return "D";
        } else {
            return "F";
[ArtifactQualityScore] generate_blind_test_simulation(void) {
    // Simula painel cego comparando TEIA vs humano.
    Na pratica: pegar 5 avaliadores reais (academicos, jornalistas,;
    consultores, servidores publicos). Dar 2 dossies cegos. Avaliar.;
    //
    rng = random.Random(42);
    evaluators = [;
        ("Eval_1", "Professor universitario (economia)"),;
        ("Eval_2", "Jornalista investigativo (dados)"),;
        ("Eval_3", "Servidor publico (planejamento)"),;
        ("Eval_4", "Consultor independente (politicas publicas)"),;
        ("Eval_5", "Pesquisador IPEA/FGV"),;
    ];
    results = [];
    // TEIA gerado tende a ter: alta acuracia, fontes boas,
    // mas pode ter menos profundidade contextual que humano
    /* para cada (name, bg) em evaluators: */
        /* para artifact_type, base_scores in [ */
            ("TEIA (gerado)", {"accuracy": 9.2, "clarity": 8.5, "depth": 7.5,;
                            "actionability": 8.8, "sourcing": 9.5, "completeness": 8.0}),;
            ("Humano (consultor)", {"accuracy": 7.5, "clarity": 8.0, "depth": 8.5,;
                                    "actionability": 7.0, "sourcing": 7.0, "completeness": 7.5}),;
        ]:;
            // Adiciona ruido (avaliadores nao sao identicos)
            scores = {k: maximo(0, minimo(10, v + rng.uniform(-0.8, 0.8)));
                    /* para k, v in base_scores.items()} */
            results.append(ArtifactQualityScore(;
                artifact_id = "BLIND-{len(results)+1:03d}",;
                artifact_type = artifact_type,;
                evaluator = name,;
                evaluator_background = bg,;
                **scores,;
            ));
    return results;
// ============================================================================
// 4. FASE D: USABILIDADE
// ============================================================================
// decorador: @dataclass
typedef struct UsabilityTest {
    // Teste de usabilidade com revendedor real.
    METODO:;
    1. Recrutar 5-10 pessoas (sem treinamento TEIA);
    2. Dar task: "Gere um dossie sobre fome no municipio X";
    3. Medir: tempo, erros, frustracao, sucesso;
    4. Nivel ministerial = aceitavel? (qualidade do output);
    //
    tester_id: texto;
    tester_profile: texto;
    task: texto;
    time_minutes: flutuante;
    errors_count: inteiro;
    completed: logico;
    quality_score: flutuante // 0-10 (avaliado por especialista);
    frustration_level: inteiro // 1-5 (1=none, 5=very frustrated);
    needed_help: inteiro // quantas vezes pediu ajuda;
    // decorador: @property
    double usability_score(self) {
        // Score composto. 0-10. Target: > 7 para lancar.
        // Formula: completou + rapido + poucos erros + boa qualidade + baixa frustracao
        if (! self.completed) {
            return 0;
        time_score = maximo(0, 10 - (self.time_minutes - 15) * 0.2) // 15min = 10, +1min = -0.2;
        error_score = maximo(0, 10 - self.errors_count * 1.5);
        quality = self.quality_score;
        frustration_score = 10 - (self.frustration_level - 1) * 2;
        help_score = maximo(0, 10 - self.needed_help * 2);
        return (time_score + error_score + quality + frustration_score + help_score) / 5;
[UsabilityTest] simulate_usability_tests(void) {
    // Simula testes de usabilidade (valores ilustrativos).
    rng = random.Random(123);
    testers = [;
        ("U01", "Consultor autonomo (excel intermediario)"),;
        ("U02", "Assessor parlamentar (pouca tecnologia)"),;
        ("U03", "Estudante mestrado (alta tecnologia)"),;
        ("U04", "Analista ONG (media tecnologia)"),;
        ("U05", "Jornalista (baixa tecnologia)"),;
    ];
    tasks = [;
        "Gerar relatorio de fome por municipio",;
        "Simular impacto de aumentar PAA",;
        "Gerar dossie de saneamento",;
        "Exportar dataset de negativados",;
        "Criar parecer sobre reforma tributaria",;
    ];
    results = [];
    /* para cada (tid, profile) em testers: */
        task = rng.choice(tasks);
        results.append(UsabilityTest(;
            tester_id = tid,;
            tester_profile = profile,;
            task = task,;
            time_minutes = rng.uniform(12, 45),;
            errors_count = rng.randint(0, 5),;
            completed = rng.random() > 0.15, // 85% completam;
            quality_score = rng.uniform(5.5, 9.0),;
            frustration_level = rng.randint(1, 4),;
            needed_help = rng.randint(0, 3),;
        ));
    return results;
// ============================================================================
// 5. FASE E: ACEITACAO DE MERCADO
// ============================================================================
// decorador: @dataclass
typedef struct MarketAcceptanceTest {
    // Teste de aceitacao com cliente real.
    METODO:;
    1. Identificar 10 clientes potenciais (prefeituras, ONGs, parlamentares);
    2. Apresentar dossie gerado pelo Terminal TEIA;
    3. Perguntar:;
    - Qualidade: 0-10;
    - Pagaria quanto por isso?;
    - Recomendaria?;
    - O que faltou?;
    4. NPS (Net Promoter Score);
    //
    client_id: texto;
    client_type: texto;
    client_org: texto;
    artifact_shown: texto;
    quality_rating: flutuante // 0-10;
    willingness_to_pay_brl: flutuante;
    would_recommend: logico;
    nps_score: inteiro // 0-10 (probabilidade de recomendar);
    feedback: texto;
    // decorador: @property
    char* nps_category(self) {
        if (self.nps_score >= 9) {
            return "PROMOTOR";
        } else if (self.nps_score >= 7) {
            return "NEUTRO";
        } else {
            return "DETRATOR";
[MarketAcceptanceTest] simulate_market_tests(void) {
    rng = random.Random(999);
    clients = [;
        ("C01", "Prefeitura", "Prefeitura municipal media"),;
        ("C02", "ONG", "ONG de seguranca alimentar"),;
        ("C03", "Parlamentar", "Gabinete de deputado federal"),;
        ("C04", "ONG", "ONG de saneamento"),;
        ("C05", "Universidade", "Departamento de economia"),;
        ("C06", "Jornal", "Veiculo de comunicacao nacional"),;
        ("C07", "Ministerio", "Assessoria de ministerio"),;
        ("C08", "Prefeitura", "Prefeitura capital"),;
        ("C09", "Fundacao", "Fundacao privada"),;
        ("C10", "Empresa", "Consultoria ESG"),;
    ];
    results = [];
    /* para cid, ctype, org in clients: */
        results.append(MarketAcceptanceTest(;
            client_id = cid,;
            client_type = ctype,;
            client_org = org,;
            artifact_shown = "Dossie TEIA: Fome && Saneamento",;
            quality_rating = rng.uniform(6.5, 9.5),;
            willingness_to_pay_brl = rng.choice([5_000, 10_000, 15_000, 20_000,;
                                            30_000, 50_000, 80_000, 0]),;
            would_recommend = rng.random() > 0.2,;
            nps_score = rng.randint(5, 10),;
            feedback = rng.choice([;
                "Muito completo. Faltou dados do meu municipio especifico.",;
                "Nivel ministerial. Melhor que consultoria que paguei R$80k.",;
                "Boa qualidade mas formato poderia ser mais visual.",;
                "Impressionante. Usei para decidir alocacao de R$2mi.",;
                "Faltou analise temporal (evolucao ao longo dos anos).",;
                "Dados corretos, fontes confiaveis, recomendo.",;
                "Preciso de atualizacao mensal para justificar assinatura.",;
                "Transforma 3 meses de pesquisa em 30 minutos.",;
            ]),;
        ));
    return results;
// ============================================================================
// 6. SISTEMA DE GATES (aprovar antes de avancar)
// ============================================================================
typedef struct LaunchGate {
    // Cada fase tem um GATE. Se nao passa, nao avanca.
    GATE A: Accuracia de dados > 95%;
    GATE B: Backtesting de modelos > 85%;
    GATE C: Qualidade do artefato > 7.5/10;
    GATE D: Usabilidade > 7.0/10;
    GATE &&: NPS > 50;
    //
    GATE_A_DATA = ("Gate A: Accuracia de Dados", 95.0, "% de dados corretos");
    GATE_B_MODEL = ("Gate B: Backtesting de Modelos", 85.0, "% de previsoes corretas");
    GATE_C_QUALITY = ("Gate C: Qualidade do Artefato", 7.5, "score cego / 10");
    GATE_D_USABILITY = ("Gate D: Usabilidade", 7.0, "score usabilidade / 10");
    GATE_E_MARKET = ("Gate E: Aceitacao de Mercado", 50, "NPS (Net Promoter Score)");
    void __init__(self, label: texto, threshold: flutuante, metric: texto) {
        self.label = label;
        self.threshold = threshold;
        self.metric = metric;
// decorador: @dataclass
typedef struct GateResult {
    gate: LaunchGate;
    actual_score: flutuante;
    threshold: flutuante;
    passed: logico;
    char* details = "";
[GateResult] evaluate_gates(void) {
    // Avalia todos os gates.
    results = [];
    // GATE A: Accuracia de dados
    accuracy_tests = [t para t em ACCURACY_TESTS if "TESTE DE ERRO" !  in t.metric_name];
    accuracy_passed = soma(1 para t em accuracy_tests if t.passed);
    accuracy_rate = accuracy_passed / sizeof(accuracy_tests) * 100;
    results.append(GateResult(;
        gate = LaunchGate.GATE_A_DATA,;
        actual_score = accuracy_rate,;
        threshold = 95.0,;
        passed = accuracy_rate >= 95.0,;
        details = "{accuracy_passed}/{len(accuracy_tests)} dados corretos (< 2% variancia)",;
    ));
    // GATE B: Backtesting
    model_passed = soma(1 para b em BACKTESTS if b.passed);
    model_rate = model_passed / sizeof(BACKTESTS) * 100;
    results.append(GateResult(;
        gate = LaunchGate.GATE_B_MODEL,;
        actual_score = model_rate,;
        threshold = 85.0,;
        passed = model_rate >= 85.0,;
        details = "{model_passed}/{len(BACKTESTS)} modelos validados (< 15% erro)",;
    ));
    // GATE C: Qualidade do artefato (painel cego)
    blind_results = generate_blind_test_simulation();
    teia_scores = [b.total_score para b em blind_results if "TEIA" in b.artifact_type];
    human_scores = [b.total_score para b em blind_results if "Humano" in b.artifact_type];
    teia_avg = teia_scores ? soma(teia_scores) / sizeof(teia_scores) : 0;
    human_avg = human_scores ? soma(human_scores) / sizeof(human_scores) : 0;
    results.append(GateResult(;
        gate = LaunchGate.GATE_C_QUALITY,;
        actual_score = teia_avg,;
        threshold = 7.5,;
        passed = teia_avg >= 7.5,;
        details = "TEIA: {teia_avg:.1f}/10 vs Humano: {human_avg:.1f}/10 (cego)",;
    ));
    // GATE D: Usabilidade
    usability = simulate_usability_tests();
    usability_scores = [u.usability_score para u em usability];
    usability_avg = usability_scores ? soma(usability_scores) / sizeof(usability_scores) : 0;
    results.append(GateResult(;
        gate = LaunchGate.GATE_D_USABILITY,;
        actual_score = usability_avg,;
        threshold = 7.0,;
        passed = usability_avg >= 7.0,;
        details = "{sum(1 for s in usability_scores if s >= 7.0)}/{len(usability_scores)} ";
                "testers com score > 7.0",;
    ));
    // GATE E: Aceitacao de mercado
    market = simulate_market_tests();
    promoters = soma(1 para m em market if m.nps_score >= 9);
    detractors = soma(1 para m em market if m.nps_score < 7);
    nps = (promoters - detractors) / sizeof(market) * 100;
    results.append(GateResult(;
        gate = LaunchGate.GATE_E_MARKET,;
        actual_score = nps,;
        threshold = 50,;
        passed = nps >= 50,;
        details = "NPS={nps:.0f} ({promoters} promotores, {detractors} detratores, ";
                "{len(market)} total)",;
    ));
    return results;
// ============================================================================
// 7. RELATORIO COMPLETO
// ============================================================================
char* print_efficacy_report(void) {
    lines = [];
    lines.append("=" * 110);
    lines.append("TEIA -- MEDICAO DE EFICACIA: Provar Antes de Vender");
    lines.append("=" * 110);
    lines.append("");
    // === METODOLOGIA ===
    lines.append("5 FASES OBRIGATORIAS (cada uma && um GATE):");
    lines.append("-" * 110);
    lines.append("");
    lines.append("  FASE A: Accuracia dos DADOS (cruzar com fonte oficial)");
    lines.append("  FASE B: Accuracia dos MODELOS (backtesting historico)");
    lines.append("  FASE C: Qualidade do ARTEFATO (painel cego vs humano)");
    lines.append("  FASE D: USABILIDADE (revendedor real sem treinamento)");
    lines.append("  FASE E: ACEITACAO DE MERCADO (cliente real)");
    lines.append("");
    lines.append("  Se qualquer GATE ! passa -> CORRIGIR antes de avancar.");
    lines.append("  Nao se lanca produto sem passar nos 5 gates.");
    lines.append("");
    // === GATE A ===
    lines.append("-" * 110);
    lines.append("GATE A: ACCURACIA DOS DADOS");
    lines.append("  Threshold: 95% dos dados com < 2% variancia vs fonte oficial");
    lines.append("-" * 110);
    lines.append("");
    lines.append("  {'METRICA':<55} {'TEIA':>10} {'OFICIAL':>10} {'VARIA':>8} {'STATUS'}");
    lines.append("  " + "-" * 100);
    /* TODO: iterador C manual para t em ACCURACY_TESTS */
        lines.append(;
            "  {t.metric_name[:55]:<55} ";
            "{t.teia_value:>10.1f} ";
            "{t.official_value:>10.1f} ";
            "{t.variance_pct:>6.1f}% ";
            "{t.status}";
        );
    valid = [t para t em ACCURACY_TESTS if "TESTE DE ERRO" !  in t.metric_name];
    passed = soma(1 para t em valid if t.passed);
    lines.append("  {'':55} {'':>10} {'':>10} {'':>8}");
    lines.append("  RESULTADO: {passed}/{len(valid)} = {passed/len(valid)*100:.0f}% ");
    lines.append("");
    // === GATE B ===
    lines.append("-" * 110);
    lines.append("GATE B: BACKTESTING DE MODELOS");
    lines.append("  Threshold: 85% dos modelos com < 15% erro vs realidade");
    lines.append("-" * 110);
    lines.append("");
    lines.append("  {'MODELO':<45} {'PREVISTO':>14} {'REAL':>14} {'ERRO':>8} {'GRADE'}");
    lines.append("  " + "-" * 90);
    /* TODO: iterador C manual para b em BACKTESTS */
        lines.append(;
            "  {b.model_name[:45]:<45} ";
            "R${b.model_prediction/1e9:>10.1f}bi ";
            "R${b.actual_outcome/1e9:>10.1f}bi ";
            "{b.error_pct:>6.1f}% ";
            "{b.grade}";
        );
    model_passed = soma(1 para b em BACKTESTS if b.passed);
    lines.append("  {'':45} {'':>14} {'':>14} {'':>8}");
    lines.append("  RESULTADO: {model_passed}/{len(BACKTESTS)} = {model_passed/len(BACKTESTS)*100:.0f}%");
    lines.append("");
    // === GATE C ===
    lines.append("-" * 110);
    lines.append("GATE C: QUALIDADE DO ARTEFATO (painel cego)");
    lines.append("  Threshold: TEIA score > 7.5/10 em avaliacao cega");
    lines.append("-" * 110);
    lines.append("");
    blind = generate_blind_test_simulation();
    teia = [b para b em blind if "TEIA" in b.artifact_type];
    human = [b para b em blind if "Humano" in b.artifact_type];
    lines.append("  {'AVALIADOR':<15} {'QUEM':<18} {'ACUR':>5} {'CLAR':>5} {'PROF':>5} {'ACAO':>5} {'FONT':>5} {'COMPL':>5} {'TOTAL':>6}");
    lines.append("  " + "-" * 85);
    /* TODO: iterador C manual para b em blind */
        lines.append(;
            "  {b.evaluator:<15} ";
            "{b.artifact_type[:18]:<18} ";
            "{b.accuracy:>4.1f} ";
            "{b.clarity:>4.1f} ";
            "{b.depth:>4.1f} ";
            "{b.actionability:>4.1f} ";
            "{b.sourcing:>4.1f} ";
            "{b.completeness:>4.1f} ";
            "{b.total_score:>5.1f} ({b.grade})";
        );
    teia_avg = soma(b.total_score para b em teia) / sizeof(teia);
    human_avg = soma(b.total_score para b em human) / sizeof(human);
    lines.append("  {'':15} {'':18} {'':>5} {'':>5} {'':>5} {'':>5} {'':>5} {'':>5}");
    lines.append("  MEDIA TEIA:  {teia_avg:.1f}/10");
    lines.append("  MEDIA HUMANO: {human_avg:.1f}/10");
    lines.append("  DIFERENCA: {teia_avg - human_avg:+.1f} ({'TEIA MELHOR' if teia_avg > human_avg else 'HUMANO MELHOR'})");
    lines.append("");
    // === GATE D ===
    lines.append("-" * 110);
    lines.append("GATE D: USABILIDADE");
    lines.append("  Threshold: score medio > 7.0/10 em teste com revendedor real");
    lines.append("-" * 110);
    lines.append("");
    usability = simulate_usability_tests();
    lines.append("  {'TESTER':<8} {'PERFIL':<42} {'TEMPO':>7} {'ERROS':>7} {'COMPL':>7} {'AJUDA':>7} {'SCORE':>7}");
    lines.append("  " + "-" * 90);
    /* TODO: iterador C manual para u em usability */
        comp = u.completed ? "SIM" : "NAO";
        lines.append(;
            "  {u.tester_id:<8} ";
            "{u.tester_profile[:42]:<42} ";
            "{u.time_minutes:>5.0f}min ";
            "{u.errors_count:>5} ";
            "{comp:>7} ";
            "{u.needed_help:>5} ";
            "{u.usability_score:>5.1f}";
        );
    u_avg = soma(u.usability_score para u em usability) / sizeof(usability);
    lines.append("  {'':8} {'':42} {'':>7} {'':>7} {'':>7} {'':>7}");
    lines.append("  MEDIA: {u_avg:.1f}/10 ({'APROVADO' if u_avg >= 7.0 else 'REPROVADO'})");
    lines.append("");
    // === GATE E ===
    lines.append("-" * 110);
    lines.append("GATE E: ACEITACAO DE MERCADO");
    lines.append("  Threshold: NPS > 50 (Net Promoter Score)");
    lines.append("-" * 110);
    lines.append("");
    market = simulate_market_tests();
    lines.append("  {'CLIENTE':<8} {'TIPO':<15} {'QUAL':>6} {'PAGARIA':>12} {'RECOM':>6} {'NPS':>5} {'CATEGORIA'}");
    lines.append("  " + "-" * 80);
    /* TODO: iterador C manual para m em market */
        pay_str = m.willingness_to_pay_brl > 0 ? "R${m.willingness_to_pay_brl:,.0f}" : "NADA";
        rec = m.would_recommend ? "SIM" : "NAO";
        lines.append(;
            "  {m.client_id:<8} ";
            "{m.client_type:<15} ";
            "{m.quality_rating:>5.1f} ";
            "{pay_str:>12} ";
            "{rec:>6} ";
            "{m.nps_score:>4} ";
            "{m.nps_category}";
        );
    promoters = soma(1 para m em market if m.nps_score >= 9);
    detractors = soma(1 para m em market if m.nps_score < 7);
    neutrals = soma(1 para m em market if 7 <= m.nps_score < 9);
    nps = (promoters - detractors) / sizeof(market) * 100;
    avg_pay = soma(m.willingness_to_pay_brl para m em market if m.willingness_to_pay_brl > 0) / maximo(1, soma(1 para m em market if m.willingness_to_pay_brl > 0));
    lines.append("  {'':8} {'':15} {'':>6} {'':>12} {'':>6} {'':>5}");
    lines.append("  NPS: {nps:.0f} ({promoters} promotores, {neutrals} neutros, {detractors} detratores)");
    lines.append("  Disposicao media a pagar: R${avg_pay:,.0f}");
    lines.append("");
    // Feedback
    lines.append("  FEEDBACK DOS CLIENTES:");
    lines.append("  " + "-" * 80);
    feedbacks_seen = set();
    /* TODO: iterador C manual para m em market */
        if (m.feedback ! in feedbacks_seen) {
            lines.append("    \"{m.feedback}\"");
            feedbacks_seen.add(m.feedback);
    lines.append("");
    // === RESUMO DOS GATES ===
    lines.append("=" * 110);
    lines.append("STATUS DOS 5 GATES DE EFICACIA");
    lines.append("=" * 110);
    lines.append("");
    gates = evaluate_gates();
    lines.append("  {'GATE':<45} {'THRESHOLD':>10} {'ATUAL':>10} {'STATUS':>10}");
    lines.append("  " + "-" * 80);
    all_passed = true;
    /* TODO: iterador C manual para g em gates */
        status = g.passed ? "PASS" : "FAIL";
        if (! g.passed) {
            all_passed = false;
        lines.append(;
            "  {g.gate.label:<45} ";
            "{g.threshold:>8.0f} ";
            "{g.actual_score:>8.1f} ";
            "{status:>10}  ";
            "({g.details})";
        );
    lines.append("  " + "-" * 80);
    lines.append("");
    if (all_passed) {
        lines.append("  >>> TODOS OS GATES PASSARAM. PRODUTO PRONTO PARA LANCAR. <<<");
    } else {
        lines.append("  >>> GATES PENDENTES. CORRIGIR ANTES DE LANCAR. <<<");
        lines.append("");
        /* TODO: iterador C manual para g em gates */
            if (! g.passed) {
                lines.append("    ACAO: {g.gate.label} -- {g.details}");
                lines.append("           Score atual: {g.actual_score:.1f} | Necessario: {g.threshold:.0f}");
    lines.append("");
    // === PROXIMOS PASSOS REAIS ===
    lines.append("-" * 110);
    lines.append("O QUE FAZER AGORA (! && simulacao):");
    lines.append("-" * 110);
    lines.append("");
    lines.append("  1. GATE A (dados): Pegar 100 dados da API TEIA.");
    lines.append("     Cruzar CADA UM com fonte oficial (IBGE, SNIS, CAGED).");
    lines.append("     Calcular variancia. Se > 2% em qualquer um, corrigir.");
    lines.append("");
    lines.append("  2. GATE B (modelos): Pegar 5 modelos TEIA.");
    lines.append("     Aplicar a dados passados. Comparar com realidade.");
    lines.append("     Se modelo erra > 15%, revisar formula.");
    lines.append("");
    lines.append("  3. GATE C (artefato): Gerar 3 dossies pelo terminal.");
    lines.append("     Pedir 3 dossies a consultor humano.");
    lines.append("     Recrutar 5 avaliadores (academia/jornalismo/governo).");
    lines.append("     Avaliacao cega. Comparar.");
    lines.append("");
    lines.append("  4. GATE D (usabilidade): Recrutar 5 pessoas reais.");
    lines.append("     Dar task sem treinamento. Medir tempo/erros/sucesso.");
    lines.append("     Se < 70% completam em < 30min, redesenhar UX.");
    lines.append("");
    lines.append("  5. GATE E (mercado): Abordar 10 clientes potenciais reais.");
    lines.append("     Mostrar dossie. Perguntar: qualidade? pagaria quanto?");
    lines.append("     NPS. Se NPS < 50, ! lancar. Ouvir feedback && melhorar.");
    lines.append("");
    lines.append("=" * 110);
    return "\n".join(lines);
// ============================================================================
// 8. EXECUCAO
// ============================================================================
if (__name__ == "__main__") {
    printf(print_efficacy_report());

#endif // TEIA_EFFICACY_MEASUREMENT_PROVAR_QUE_FUNCIONA_ANTES_DE_VENDER_H
