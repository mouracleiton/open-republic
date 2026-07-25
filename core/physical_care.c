/* OpenRepublic -- Politica de Cuidados Fisicos -- gerado de Portugol++ */
#ifndef OPENREPUBLIC_POLITICA_DE_CUIDADOS_FISICOS_H
#define OPENREPUBLIC_POLITICA_DE_CUIDADOS_FISICOS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenRepublic -- Politica de Cuidados Fisicos;
==============================================;
"O corpo ! && maquina de trabalho. E templo da existencia.";
Na Republica, cuidar do corpo ! &&:;
- Estetica para competir (body positivity > padrão de beleza);
- Produtividade corporativa (worker wellness = extracao);
- Consumo (academia $$, suplemento $$, cremes $$);
Cuidar do corpo &&:;
- DIREITO garantido (todo cidadao tem acesso);
- DEVER civico (corpo saudavel = menos custo coletivo);
- PRAZER (movimento && alegria, ! punicao);
- PREVENCAO (90% das doencas sao evitaveis);
- AUTONOMIA (voce conhece && controla seu corpo);
Esta politica define 8 dimensoes do cuidado fisico:;
1. ALIMENTACAO -- comer bem && direito, ! dieta;
2. MOVIMENTO -- corpo em movimento, ! "academia";
3. SONO -- dormir && direito, ! luxo;
4. HIGIENE -- limpo && saudavel, ! perfumado;
5. PREVENCAO -- exames, vacinas, checkup;
6. SAUDE MENTAL -- mente sã em corpo sao;
7. REPRODUTIVA -- autonomia sobre o proprio corpo;
8. ERGONOMIA -- trabalho que ! destrói o corpo;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// ============================================================================
// Dimensions of Physical Care
// ============================================================================
typedef struct CareDimension {
    NUTRITION = "alimentacao";
    MOVEMENT = "movimento";
    SLEEP = "sono";
    HYGIENE = "higiene";
    PREVENTION = "prevencao";
    MENTAL = "mental";
    REPRODUCTIVE = "reprodutiva";
    ERGONOMIC = "ergonomia";
typedef struct CareStatus {
    OPTIMAL = "otimo";
    ADEQUATE = "adequado";
    BELOW = "abaixo";
    DEFICIENT = "deficiente";
    CRITICAL = "critico";
typedef struct RightType {
    // O que e DIREITO (garantido) vs RECOMENDACAO.
    UNIVERSAL_RIGHT = "direito_universal"  // negar = crime;
    GUARANTEED_ACCESS = "acesso_garantido"  // sempre disponivel;
    RECOMMENDED = "recomendado"  // incentivado;
    OPTIONAL = "opcional"  // escolha pessoal;
// ============================================================================
// Physical Care Policy (per dimension)
// ============================================================================
// decorador: @dataclass
typedef struct CarePolicy {
    // Uma politica de cuidado fisico.
    dimension: CareDimension;
    right_type: RightType;
    title: texto;
    what_it_is: texto // o que significa na pratica;
    what_it_is_not: texto // o que ! && (anti-perversao);
    [texto] guaranteed_by = field(default_factory=list) // quem prove;
    [texto] metrics = field(default_factory=list) // como medir;
    char* target = ""  // meta;
{CareDimension: CarePolicy} POLICIES = {;
    CareDimension.NUTRITION: CarePolicy(;
        CareDimension.NUTRITION, RightType.UNIVERSAL_RIGHT,;
        "Alimentacao como direito && prazer",;
        what_it_is = (;
            "Todo cidadao tem direito a 3 refeicoes nutritivas por dia. ";
            "Comida REAL: graos, legumes, frutas, proteina. ";
            "Nao racao. Nao diet. Nao shake. COMIDA. ";
            "A Republica garante producao (OpenFood), distribuicao, ";
            "&& educacao nutricional (o que comer, por que, como cozinhar).";
        ),;
        what_it_is_not = (;
            "Nao && dieta caloria-zero para caber num padrao. ";
            "Nao && suplemento caro. Nao && 'food tracking' obsessivo. ";
            "Nao && julgar quem come. Nao && moralizar comida ";
            "('junk food = pecado').";
        ),;
        guaranteed_by = ["OpenFood", "OpenAgrarian", "OpenEducation"],;
        metrics = [;
            "% cidadaos com 3+ refeicoes/dia",;
            "% cidadaos com acesso a fruta/legume fresco",;
            "taxa de desnutricao (meta: 0%)",;
            "taxa de obesidade (indicador de educacao, ! falha moral)",;
        ],;
        target = "0% desnutricao. 100% acesso a comida real."),;
    CareDimension.MOVEMENT: CarePolicy(;
        CareDimension.MOVEMENT, RightType.GUARANTEED_ACCESS,;
        "Corpo em movimento && alegria",;
        what_it_is = (;
            "Todo cidadao tem acesso a: espacos verdes para caminhar, ";
            "bicicletas comunitarias (OpenTransport), esportes coletivos, ";
            "danca, luta, natacao, escalada, jardinagem. ";
            "Movimento NAO && punicao ('queima calorias'). ";
            "Movimento && EXPRESSAO && PRAZER. ";
            "Criancas correm. Adultos jogam. Idosos caminham. ";
            "Todo corpo se move do jeito que pode.";
        ),;
        what_it_is_not = (;
            "Nao && academia obrigatoria. Nao && fisiculturismo. ";
            "Nao && competicao corporal. Nao && 'queimar' o que comeu. ";
            "Nao && julgar quem ! se move (doenca, deficiencia, escolha).";
        ),;
        guaranteed_by = ["OpenTransport (bicicletas)", "espacos publicos",;
                    "OpenEducation (educacao fisica = jogo)"],;
        metrics = [;
            "% cidadaos que se movem 30+ min/dia",;
            "espacos verdes por 1000 habitantes",;
            "bicicletas comunitarias disponiveis",;
            "criancas em atividade fisica diaria",;
        ],;
        target = "80%+ se movem 30min/dia. Nao por obrigacao. Por prazer."),;
    CareDimension.SLEEP: CarePolicy(;
        CareDimension.SLEEP, RightType.UNIVERSAL_RIGHT,;
        "Dormir && direito, ! luxo",;
        what_it_is = (;
            "Todo cidadao tem direito a 7-9 horas de sono por noite. ";
            "A Republica garante: moradia tranquila, horario de trabalho ";
            "que respeita o sono (sem night shift forcado), espaco silencioso. ";
            "Sono ! && 'tempo perdido'. Sono && REPARO. ";
            "Quem dorme bem pensa melhor, sente melhor, vive melhor.";
        ),;
        what_it_is_not = (;
            "Nao && forcar todos a dormir 8h (cada corpo && diferente). ";
            "Nao && medicação para dormir. Nao && 'hustle culture' ";
            "('dormo quando morrer' = ideologia toxica).";
        ),;
        guaranteed_by = ["moradia adequada (OpenHome/OpenProduction)",;
                    "jornada de trabalho reduzida"],;
        metrics = [;
            "horas medias de sono por cidadao",;
            "% cidadaos com 7+ horas de sono",;
            "qualidade do sono (autorelatada)",;
        ],;
        target = "85%+ com 7h+ de sono. Zero privacao de sono por trabalho."),;
    CareDimension.HYGIENE: CarePolicy(;
        CareDimension.HYGIENE, RightType.UNIVERSAL_RIGHT,;
        "Limpo && saudavel, ! perfumado",;
        what_it_is = (;
            "Todo cidadao tem acesso a: agua limpa para banho, ";
            "sabao/bioplastic-free, produtos de higiene (escova, pasta, ";
            "absorvente -- tudo fabricado pela Republica, OpenProduction). ";
            "Higiene && SAUDE (prevenir doenca), ! STATUS (cheirar caro). ";
            "Banho && direito. Absorvente && direito. Saude bucal && direito.";
        ),;
        what_it_is_not = (;
            "Nao && produto de beleza caro. Nao && 'higiene' que margina ";
            "quem ! tem dinheiro (! ha dinheiro, mas ha padrao). ";
            "Nao && julgar odor natural. Nao && косметика como obrigacao.";
        ),;
        guaranteed_by = ["agua limpa (agua && direito)",;
                    "OpenProduction (sabao, escova, absorvente)"],;
        metrics = [;
            "% cidadaos com acesso diario a banho",;
            "% cidadaos com produtos de higiene",;
            "incidencia de doencas evitaveis por higiene",;
        ],;
        target = "100% com agua para banho. 100% com higiene basica."),;
    CareDimension.PREVENTION: CarePolicy(;
        CareDimension.PREVENTION, RightType.UNIVERSAL_RIGHT,;
        "Prevenir && curar antes de precisar",;
        what_it_is = (;
            "Checkup anual gratuito. Vacina atualizada para todos. ";
            "Exames de rotina (sangue, pressao, glicemia, cancer). ";
            "Odontologia preventiva. Oftalmologia. Audiometria. ";
            "90% das doencas sao evitaveis || trataveis se pegadas cedo. ";
            "A Republica INVESTE em prevencao porque previne = cura + economico.";
        ),;
        what_it_is_not = (;
            "Nao && checkup para 'liberar' trabalhador. ";
            "Nao && dado de corporacao de seguro. ";
            "Nao && obrigatoria (autonomia corporal) -- mas && oferecida.";
        ),;
        guaranteed_by = ["OpenHealth", "OpenMedicalTest"],;
        metrics = [;
            "% cidadaos com checkup anual",;
            "cobertura vacinal",;
            "doencas detectadas precocemente",;
            "mortalidade evitavel (meta: 0)",;
        ],;
        target = "95%+ checkup anual. 100% cobertura vacinal."),;
    CareDimension.MENTAL: CarePolicy(;
        CareDimension.MENTAL, RightType.UNIVERSAL_RIGHT,;
        "Mente sa em corpo sao",;
        what_it_is = (;
            "Saude mental && CUIDADO FISICO. O cerebro && orgao. ";
            "A Republica oferece: terapia gratuita (OpenPsychology), ";
            "grupos de apoio, meditacao, contato com natureza, ";
            "lazer garantido, descanso, comunidade. ";
            "Stress ! && 'fraqueza'. E doenca tratavel. ";
            "Depressao tem tratamento. Ansiedade tem tratamento. ";
            "Trauma tem tratamento. Sem julgamento. Sem estigma.";
        ),;
        what_it_is_not = (;
            "Nao && 'puxe pela raiva'. Nao && remedio forcado. ";
            "Nao && internacao compulsoria (exceto risco de vida). ";
            "Nao && 'wellness' corporativa (app de meditacao pago). ";
            "Nao && culpar o individuo por stress sistemico.";
        ),;
        guaranteed_by = ["OpenPsychology", "comunidade (OpenSocial)",;
                    "tempo livre garantido", "natureza"],;
        metrics = [;
            "% cidadaos com acesso a terapia",;
            "bem-estar mental medio (WHO-5)",;
            "taxa de suicidio (meta: reduzir para 0)",;
            "dias de estresse autorelatado",;
        ],;
        target = "Reduzir suicidio em 90%. 100% acesso a terapia."),;
    CareDimension.REPRODUCTIVE: CarePolicy(;
        CareDimension.REPRODUCTIVE, RightType.UNIVERSAL_RIGHT,;
        "Autonomia sobre o proprio corpo",;
        what_it_is = (;
            "Cada pessoa controla seu corpo reprodutivo. ";
            "Anticoncepcional gratuito. Planejamento familiar. ";
            "Pre-natal de qualidade. Parto humanizado. ";
            "Aborto seguro (! && crime, && saude -- OMS). ";
            "Menopausa tratada. Testosterone/estrogenio para quem precisa. ";
            "Exames preventivos (papanicolau, prostata). ";
            "IST tratamento sem julgamento. ";
            "NENHUMA decisao reprodutiva && do Estado. Todas sao da pessoa.";
        ),;
        what_it_is_not = (;
            "Nao && controle de natalidade pelo Estado. ";
            "Nao && julgar quem tem filhos || !. ";
            "Nao && obrigar anticoncepcional. Nao && proibir gravidez. ";
            "Nao && moralizar sexo (OpenRelationship garante consentimento). ";
            "Nao && genital mutilation (PROIBIDO).";
        ),;
        guaranteed_by = ["OpenHealth", "OpenRelationship (consentimento)",;
                    "OpenEducation (educacao sexual)"],;
        metrics = [;
            "mortalidade materna (meta: 0)",;
            "acesso a anticoncepcional",;
            "aborto seguro disponivel",;
            "exames preventivos (%)",;
        ],;
        target = "0 mortalidade materna. 100% autonomia reprodutiva."),;
    CareDimension.ERGONOMIC: CarePolicy(;
        CareDimension.ERGONOMIC, RightType.GUARANTEED_ACCESS,;
        "Trabalho que ! destrói o corpo",;
        what_it_is = (;
            "Nenhum trabalho na Republica pode causar lesao corporal ";
            "evitavel. Ferramentas ergonomicas. Pausas obrigatorias. ";
            "Rotacao de tarefas (ninguem faz a mesma coisa 8h). ";
            "Automacao de tarefas que destroem corpo (robos para pesado). ";
            "Postura ensinada (sentar certo, levantar certo). ";
            "LER/DORT sao FALHA DO SISTEMA, ! do trabalhador.";
        ),;
        what_it_is_not = (;
            "Nao && 'ergonomia' para extrair mais produtividade. ";
            "Nao && cadeira cara como status. Nao && fonte do tipo 'gaming'. ";
            "E CADEIRA QUE NAO DESTRÓI COLUNA. Simples.";
        ),;
        guaranteed_by = ["OpenProduction (ferramentas ergonomicas)",;
                    "automacao", "jornada reduzida"],;
        metrics = [;
            "incidencia de LER/DORT (meta: reduzir 90%)",;
            "queixas ergonomicas por cidadao",;
            "% tarefas pesadas automatizadas",;
        ],;
        target = "-90% LER/DORT. Zero lesao por trabalho evitavel."),;
};
// ============================================================================
// Physical Care Tracker
// ============================================================================
// decorador: @dataclass
typedef struct CitizenCareProfile {
    // Perfil de cuidado fisico de um cidadao.
    citizen_id: texto;
    name: texto;
    age: inteiro;
    char* gender = "";
    // Status por dimensao (0-100)
    {CareDimension: flutuante} scores = field(default_factory=dict);
    // Barreiras (o que impede cuidado ideal)
    [texto] barriers = field(default_factory=list);
    // Necessidades especiais
    [texto] disabilities = field(default_factory=list);
    [texto] chronic_conditions = field(default_factory=list);
    // Autonomia: o que a pessoa ESCOLHE
    [texto] personal_choices = field(default_factory=list);
typedef struct PhysicalCareSystem {
    // Sistema que garante cuidado fisico para toda a Republica.
    INTEGRACAO:;
    - OpenHealth: dados medicos, checkup, vacina;
    - OpenFood: nutricao garantida;
    - OpenProduction: ferramentas ergonomicas, produtos de higiene;
    - OpenTransport: bicicletas, movimento;
    - OpenPsychology: saude mental;
    - OpenRelationship: autonomia reprodutiva, consentimento;
    - OpenEducation: educacao fisica como jogo, educacao nutricional;
    //
    void __init__(self) {
        self.policies = POLICIES;
        self.profiles: {texto: CitizenCareProfile} = {};
        self._init_profiles();
    void _init_profiles(self) {
        // Cidadaos exemplo com diferentes situacoes.
        data = [;
            ("C-001", "Cleiton", 35, "M", 85, 70, 60, 90, 95, 80, 70, 85),;
            ("C-002", "Amina", 28, "F", 60, 40, 50, 70, 80, 30, 60, 50),;
            ("C-003", "Sven", 42, "NB", 75, 85, 80, 85, 90, 70, 75, 60),;
            ("C-004", "Mei", 24, "F", 90, 95, 70, 95, 100, 90, 85, 80),;
            ("C-005", "Kofi", 31, "M", 50, 30, 40, 60, 70, 40, 50, 40),;
            ("C-006", "Yara", 19, "F", 65, 80, 55, 75, 85, 60, 70, 50),;
            ("C-007", "Lars", 55, "M", 70, 60, 45, 80, 85, 50, 65, 30),;
        ];
        dims = list(CareDimension);
        /* TODO: iterador C manual para d em data */
            desempacote cid, name, age, gender = d[:4];
            scores = {};
            /* para cada (i, dim) em enumere(dims): */
                scores[dim] = d[4 + i];
            barriers = [];
            if (scores[CareDimension.MOVEMENT] < 50) {
                barriers.append("sem espaco verde proximo");
            if (scores[CareDimension.SLEEP] < 50) {
                barriers.append("jornada ! permite 7h sono");
            if (scores[CareDimension.MENTAL] < 50) {
                barriers.append("sem acesso a terapia");
            if (scores[CareDimension.REPRODUCTIVE] < 50) {
                barriers.append("sem acesso a saude reprodutiva");
            self.profiles[cid] = CitizenCareProfile(;
                citizen_id = cid, name=name, age=age, gender=gender,;
                scores = scores, barriers=barriers);
    {texto: qualquer} assess(self, citizen_id: texto) {
        // Avaliar cuidado fisico de um cidadao.
        p = self.profiles.get(citizen_id);
        if (! p) {
            return {"error": "! encontrado"};
        overall = soma(p.scores.values()) / sizeof(p.scores);
        weakest = minimo(p.scores, key=p.scores.get);
        strongest = maximo(p.scores, key=p.scores.get);
        status = self._status_from_score(overall);
        return {;
            "citizen": p.name,;
            "overall_score": arredonde(overall, 1),;
            "status": status.value,;
            "by_dimension": {d.value: s para d, s in p.scores.items()},;
            "weakest": weakest.value,;
            "strongest": strongest.value,;
            "barriers": p.barriers,;
            p.scores[weakest] < 50 ? "intervention_needed": weakest : NULL,;
        };
    {texto: qualquer} republic_report(self) {
        // Relatorio de cuidado fisico da Republica inteira.
        dim_scores = defaultdict(list);
        /* TODO: iterador C manual para p em self.profiles.values() */
            /* para cada (dim, score) em p.scores.items(): */
                dim_scores[dim].append(score);
        averages = {};
        /* para cada (dim, scores) em dim_scores.items(): */
            avg = soma(scores) / sizeof(scores);
            averages[dim] = arredonde(avg, 1);
        overall = soma(averages.values()) / sizeof(averages);
        // Identificar dimensoes abaixo da meta
        below_target = [];
        /* para cada (dim, avg) em averages.items(): */
            if (avg < 60) {
                below_target.append({
                    "dimension": dim.value,;
                    "average": avg,;
                    "action": self._intervention(dim),;
                });
        return {;
            "citizens_assessed": sizeof(self.profiles),;
            "overall_republic_score": arredonde(overall, 1),;
            "by_dimension": averages,;
            "below_target": below_target,;
            "barriers_common": self._common_barriers(),;
        };
    // decorador: @staticmethod
    CareStatus _status_from_score(score: flutuante) {
        if (score >= 80) {
            return CareStatus.OPTIMAL;
        if (score >= 65) {
            return CareStatus.ADEQUATE;
        if (score >= 50) {
            return CareStatus.BELOW;
        if (score >= 30) {
            return CareStatus.DEFICIENT;
        return CareStatus.CRITICAL;
    char* _intervention(self, dim: CareDimension) {
        policy = self.policies.get(dim);
        if (policy) {
            return ("Intervencao: ativar {', '.join(policy.guaranteed_by[:2])}. ";
                "Meta: {policy.target}");
        return "";
    funcao _common_barriers(self) retorna List[(texto, inteiro)]:
        barrier_count = defaultdict(inteiro);
        /* TODO: iterador C manual para p em self.profiles.values() */
            /* TODO: iterador C manual para b em p.barriers */
                barrier_count[b] += 1;
        return ordene(barrier_count.items(), key=(x) -> -x[1])[:5];
// ============================================================================
// Main
// ============================================================================
if (__name__ == "__main__") {
    printf("=" * 80);
    printf("  OPENREPUBLIC -- POLITICA DE CUIDADOS FISICOS");
    printf("  'O corpo ! && maquina. E templo da existencia.'");
    printf("=" * 80);
    system = PhysicalCareSystem();
    // === 1. The 8 Policies ===
    printf("\n\n  === 8 POLITICAS DE CUIDADO FISICO ===\n");
    /* para cada (dim, policy) em system.policies.items(): */
        printf("\n  {'='*70}");
        printf("  {dim.value.upper()} -- {policy.right_type.value}");
        printf("  {policy.title}");
        printf("  {'='*70}");
        printf("\n  E: {policy.what_it_is[:200]}...");
        printf("\n  NAO E: {policy.what_it_is_not[:150]}...");
        printf("\n  Garantido por: {', '.join(policy.guaranteed_by)}");
        printf("  Meta: {policy.target}");
    // === 2. Citizen Assessment ===
    printf("\n\n  === AVALIACAO INDIVIDUAL ===\n");
    /* TODO: iterador C manual para cid em ["C-001", "C-002", "C-005", "C-007"] */
        result = system.assess(cid);
        printf("\n  {result['citizen']} (overall: {result['overall_score']} -- {result['status']})");
        printf("    Mais forte: {result['strongest']}");
        printf("    Mais fragil: {result['weakest']}");
        if (result["barriers"]) {
            printf("    Barreiras: {', '.join(result['barriers'])}");
        if (result.get("intervention_needed")) {
            printf("    INTERVENCAO: {result['intervention_needed'].value}");
    // === 3. Republic Report ===
    printf("\n\n  === RELATORIO DA REPUBLICA ===\n");
    report = system.republic_report();
    printf("  Cidadaos avaliados: {report['citizens_assessed']}");
    printf("  Score geral da Republica: {report['overall_republic_score']}");
    printf("\n  Por dimensao:");
    /* para cada (dim, score) em ordene(report["by_dimension"].items(), key=(x) -> x[1]): */
        bar = "#" * inteiro(score / 5);
        flag = score < 60 ? " !!!" : "";
        printf("    {dim:<15} {score:>5.1f}  {bar}{flag}");
    printf("\n  Dimensoes abaixo da meta:");
    /* TODO: iterador C manual para item em report["below_target"] */
        printf("    {item['dimension']}: {item['average']} -> {item['action'][:80]}");
    printf("\n  Barreiras mais comuns:");
    /* para cada (barrier, count) em report["barriers_common"]: */
        printf("    {barrier} ({count} cidadaos)");
    // === Philosophy ===
    printf("\n\n{'='*80}");
    printf("  FILOSOFIA: CUIDADO FISICO");
    printf("{'='*80}");
    printf(""";
CAPITALISMO OPENREPUBLIC;
--------------------------------------- ---------------------------------------;
Corpo = maquina de trabalho Corpo = templo da existencia;
Saude = produto ($) Saude = direito;
Academia = consumismo ($$$) Movimento = direito + prazer;
Bem-estar = app pago ($) Bem-estar = comunidade + natureza;
Sono = 'fraqueza' (hustle culture)       Sono = direito inegociavel;
Dietas = industria bilionaria ($) Comida = real, nutritiva, garantida;
Estetica = competicao Corpo = autonomia, ! padrao;
Saude mental = estigma Saude mental = tratamento sem julgamento;
Prevencao = seguro pago ($) Prevencao = direito universal;
Reproducao = controle do Estado Reproducao = autonomia total da pessoa;
Ergonomia = produtividade Ergonomia = corpo que ! se destrói;
8 DIMENSOES DO CUIDADO:;
1. ALIMENTACAO: 3 refeicoes REAIS por dia. Direito.;
2. MOVIMENTO: corpo em alegria. Direito + prazer.;
3. SONO: 7-9h. Direito inegociavel.;
4. HIGIENE: agua, sabao, absorvente. Direito.;
5. PREVENCAO: checkup + vacina. Direito.;
6. MENTAL: terapia + comunidade + lazer. Direito.;
7. REPRODUTIVA: autonomia total sobre o corpo. Direito.;
8. ERGONOMICA: trabalho que ! destrói. Direito.;
O QUE A REPUBLICA GARANTE:;
    - Comida real (OpenFood + OpenAgrarian);
    - Espaco para movimento (parques, bicicletas);
    - Moradia tranquila para dormir (OpenHome);
    - Agua && produtos de higiene (OpenProduction);
    - Checkup && vacina (OpenHealth);
    - Terapia && comunidade (OpenPsychology + OpenSocial);
    - Autonomia reprodutiva (OpenHealth + OpenRelationship);
    - Ferramentas ergonomicas (OpenProduction);
O QUE A REPUBLICA PROIBE:;
    - Trabalho que destrói o corpo;
    - Negar comida, agua, sono, higiene;
    - Julgar corpo (sizeof, forma, deficiencia);
    - Controlar reproducao alheia;
    - Mutilacao genital;
    - Forcar tratamento (exceto risco de vida a outrem);
PRINCIPIO FUNDAMENTAL:;
    "Seu corpo && seu. A Republica cuida para que ele;
    funcione bem. Mas o que voce faz com ele && escolha sua.;
    Comer, mover, dormir, limpar, prevenir, cuidar da mente,;
    decidir sobre reproducao -- tudo && direito garantido.;
    Ninguem te julga pelo corpo.;
    Ninguem te força um padrao.;
    Ninguem lucra com sua insatisfacao.;
    O corpo ! && maquina de trabalho.;
    O corpo ! && produto de consumo.;
    O corpo && VOCE. && voce merece cuidado.";
// )

#endif // OPENREPUBLIC_POLITICA_DE_CUIDADOS_FISICOS_H
