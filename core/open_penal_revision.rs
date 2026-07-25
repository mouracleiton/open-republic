// OpenPenalRevision -- Esvaziar o Sistema Prisional, Transformar em Forca Produtiva -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
OpenPenalRevision -- Esvaziar o Sistema Prisional, Transformar em Forca Produtiva;
==================================================================================;
"Prisao ! cura. Prisao ! recupera. Prisao fabrica criminoso.;
A Republica ! aprisiona. A Republica TRANSFORMA.";
O QUE ESTE SISTEMA FAZ:;
1. REVISAO CRIMINAL: reabre cada caso carcerario;
2. ESCORREGAR DE CARGA: move presos para trabalho produtivo;
3. TRANSFORMACAO: preso vira cidadao produtivo;
4. REPARACAO: vitima && indenizada com trabalho, ! tempo;
5. PREVENCAO: addressa causa do crime (pobreza, ! carater);
A MATEMATICA DA TRANSFORMACAO:;
Um preso custa R$ 3.500/mes ao Estado brasileiro = R$ 42.000/ano.;
Faz NADA produzivo. Geralmente sai pior.;
Na Republica:;
- Preso faz 920h/ano de trabalho produtivo (base 1.0);
- Gera valor para a comunidade;
- Repara vitima com trabalho;
- Aprende oficio real;
- Recupera dignidade;
- Sai transformado, ! pior;
ZERO custo de prisao (! ha prisao no modelo tradicional).;
GANHO de produtividade.;
REDUCAO de reincidencia.;
O QUE ! EXISTE NA REPUBLICA:;
- Prisao perpertua (exceto crimes hediondos irrecuperaveis);
- Cadeia para usuarios de drogas;
- Cadeia para pobres que roubaram comida;
- Cadeia para endividados;
- Solitaria (TORTURA = crime do Estado);
- Presos provisorios anos aguardando julgamento;
O QUE EXISTE:;
- Revisao de cada caso;
- Trabalho produtivo como recuperacao;
- Reparacao a vitima;
- Tratamento para dependencia quimica;
- Educacao obrigatoria;
- Oficio garantido;
- Reintegracao comunitaria;
Author: OpenRepublic Team;
Principio: "Quem errou tem que consertar. Nao ser jogado fora.";
//
// importa annotations de __future__
// importa math
// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime
// ============================================================================
// 1. CLASSIFICACAO DO CRIME
// ============================================================================
#[derive(Debug, Clone, PartialEq)]
enum CrimeCategory {
    // Categoria do crime -- determina tratamento.
    // Categoria 1: Crimes de necessidade (pobreza estrutural)
    PETTY_THEFT_FOOD = "furto_comida"  // roubar para comer;
    PETTY_THEFT_BASIC = "furto_basico"  // roubar item basico;
    DRUG_POSSESSION = "porte_droga"  // usuario, ! traficante;
    DEBT_DEFAULT = "divida"  // endividado (! && crime real);
    VAGRANCY = "vadiagem"  // estar pobre na rua (! crime);
    // Categoria 2: Crimes com vitima, recuperavel
    THEFT_WITH_VALUE = "furto_valor"  // roubo com valor;
    FRAUD = "fraude"  // fraude economica;
    ASSAULT_NO_HARM = "agressao_leve"  // sem ferimentos graves;
    PROPERTY_DAMAGE = "dano_patrimonio"  // depredacao;
    // Categoria 3: Crimes com vitima, dano grave
    VIOLENT_CRIME = "crime_violento"  // agressao com ferimentos;
    SEXUAL_CRIME = "crime_sexual"  // violencia sexual;
    ARMED_ROBBERY = "roubo_armado"  // roubo a mao armada;
    TRAFFICKING = "trafico"  // trafico de drogas;
    HOMICIDE_MANS = "homicidio_culposo"  // sem intenção;
    // Categoria 4: Crimes hediondos (irrecuperaveis no sistema tradicional)
    HOMICIDE_INT = "homicidio_doloso"  // assassinato intencional;
    CHILD_ABUSE = "abuso_infantil";
    TORTURE = "tortura";
    TERRORISM = "terrorismo";
    GENOCIDE = "genocidio";
#[derive(Debug, Clone, PartialEq)]
enum CrimeSeverity {
    // Severidade do crime (determina tratamento na Republica).
    NOT_CRIME = 0 // vadiagem, divida, porte de drogas -- ! && crime;
    LOW = 1 // necessidade economica -- trabalho + educacao;
    MEDIUM = 2 // vitima, recuperavel -- trabalho + reparacao;
    HIGH = 3 // vitima, dano grave -- tratamento intensivo;
    HEDIONDOUS = 4 // irrecuperavel -- restricao permanente;
// Mapeamento categoria -> severidade
CRIME_SEVERITY = {
    CrimeCategory.PETTY_THEFT_FOOD: CrimeSeverity.NOT_CRIME,;
    CrimeCategory.PETTY_THEFT_BASIC: CrimeSeverity.NOT_CRIME,;
    CrimeCategory.DRUG_POSSESSION: CrimeSeverity.NOT_CRIME,;
    CrimeCategory.DEBT_DEFAULT: CrimeSeverity.NOT_CRIME,;
    CrimeCategory.VAGRANCY: CrimeSeverity.NOT_CRIME,;
    CrimeCategory.THEFT_WITH_VALUE: CrimeSeverity.LOW,;
    CrimeCategory.FRAUD: CrimeSeverity.LOW,;
    CrimeCategory.ASSAULT_NO_HARM: CrimeSeverity.MEDIUM,;
    CrimeCategory.PROPERTY_DAMAGE: CrimeSeverity.LOW,;
    CrimeCategory.VIOLENT_CRIME: CrimeSeverity.HIGH,;
    CrimeCategory.SEXUAL_CRIME: CrimeSeverity.HIGH,;
    CrimeCategory.ARMED_ROBBERY: CrimeSeverity.HIGH,;
    CrimeCategory.TRAFFICKING: CrimeSeverity.HIGH,;
    CrimeCategory.HOMICIDE_MANS: CrimeSeverity.HIGH,;
    CrimeCategory.HOMICIDE_INT: CrimeSeverity.HEDIONDOUS,;
    CrimeCategory.CHILD_ABUSE: CrimeSeverity.HEDIONDOUS,;
    CrimeCategory.TORTURE: CrimeSeverity.HEDIONDOUS,;
    CrimeCategory.TERRORISM: CrimeSeverity.HEDIONDOUS,;
    CrimeCategory.GENOCIDE: CrimeSeverity.HEDIONDOUS,;
};
// ============================================================================
// 2. O CASO PENAL
// ============================================================================
#[derive(Debug, Clone, PartialEq)]
enum SentenceStatus {
    // Estado do caso na revisao.
    PENDING_REVIEW = "pendente"  // aguardando revisao;
    OVERTURNED = "revogado"  // ! era crime (liberar IMEDIATAMENTE);
    CONVERTED_TO_WORK = "convertido_trabalho"  // vira trabalho produtivo;
    TREATMENT = "tratamento"  // vira tratamento (saude/adiccao);
    RESTRICTED = "restrito"  // hediondo (restricao permanente);
    DISCHARGED = "alta"  // cumpriu transformacao, livre;
// decorador: @dataclass
#[derive(Debug, Clone)]
struct PenalCase {
    // Um caso carcerario para revisao.
    case_id: texto;
    citizen_id: texto;
    citizen_name: texto;
    let age: i64 = 0;
    let crime_category: CrimeCategory = CrimeCategory.PETTY_THEFT_FOOD;
    let crime_description: String = "";
    let original_sentence_years: f64 = 0.0;
    let years_served: f64 = 0.0;
    let victim_id: String = "";
    let victim_name: String = "";
    let victim_reparation_due: f64 = 0.0 // em horas de trabalho;
    // Contexto (Causa raiz)
    let poverty_driven: bool = false // crime por necessidade economica;
    let addiction_driven: bool = false // crime por dependencia quimica;
    let mental_health_issue: bool = false // saude mental;
    let first_offense: bool = true;
    let education_level: String = "basico";
    // Revisao
    let severity: CrimeSeverity = CrimeSeverity.NOT_CRIME;
    let status: SentenceStatus = SentenceStatus.PENDING_REVIEW;
    let new_plan: String = ""  // plano de transformacao;
    let work_hours_required: f64 = 0.0 // trabalho para reparacao;
    let skills_to_learn: [texto] = field(default_factory=list);
    let treatment_required: String = "";
    let review_date: String = "";
    let reviewer_id: String = "";
    // decorador: @property
    fn should_release_immediately(self) -> bool {
        // Deve ser libertado AGORA?
        return self.severity == CrimeSeverity.NOT_CRIME;
    // decorador: @property
    fn is_productive_eligible(self) -> bool {
        // Pode ser convertido em forca produtiva?
        return self.severity in (CrimeSeverity.LOW, CrimeSeverity.MEDIUM,;
                                CrimeSeverity.HIGH);
    // decorador: @property
    fn is_permanently_restricted(self) -> bool {
        // Crimes irrecuperaveis (hediondos)?
        return self.severity == CrimeSeverity.HEDIONDOUS;
// ============================================================================
// 3. MOTOR DE REVISAO PENAL
// ============================================================================
#[derive(Debug, Clone)]
struct PenalRevisionEngine {
    // Revisa cada caso carcerario e transforma em forca produtiva.
    PROCESSO DE REVISAO (para CADA preso):;
    1. AVALIAR: qual crime? qual causa raiz? qual severidade real?;
    2. CLASSIFICAR:;
    - NOT_CRIME -> LIBERTAR imediatamente;
    - LOW/MEDIUM -> CONVERTER em trabalho produtivo;
    - HIGH -> tratamento intensivo + trabalho;
    - HEDIONDOUS -> restricao permanente;
    3. TRANSFORMAR:;
    - Trabalho 920h/ano (base 1.0 como todo cidadao);
    - Aprende oficio (habilidade real);
    - Repara vitima (horas de trabalho para ela);
    - Tratamento se necessario;
    4. REINTEGRAR:;
    - Apos transformacao, volta a comunidade;
    - Sem estigma (prontuario limpo se cumpriu);
    - Oficio garantido;
    //
    fn __init__(self) {
        self.cases: {texto: PenalCase} = {};
        self.released: inteiro = 0;
        self.converted: inteiro = 0;
        self.restricted: inteiro = 0;
        self.discharged: inteiro = 0;
        self.total_work_hours_generated: flutuante = 0.0;
        self.total_victims_repaired: flutuante = 0.0;
    fn submit_case(self, case: PenalCase) -> None {
        self.cases[case.case_id] = case;
    fn review(self, case_id: texto, reviewer_id: texto) -> {texto: qualquer} {
        // Revisa um caso e define o plano de transformacao.
        case = self.cases.get(case_id);
        if ! case {
            return {"error": "Caso ! encontrado"};
        // Classificar severidade
        case.severity = CRIME_SEVERITY.get(case.crime_category,;
                                        CrimeSeverity.MEDIUM);
        case.review_date = datetime.now().isoformat();
        case.reviewer_id = reviewer_id;
        // Aplicar tratamento conforme severidade
        if case.should_release_immediately {
            return self._release_immediate(case);
        if case.is_permanently_restricted {
            return self._restrict_permanent(case);
        // LOW / MEDIUM / HIGH -> transformacao produtiva
        return self._convert_to_productive(case);
    fn _release_immediate(self, case: PenalCase) -> {texto: qualquer} {
        // Liberta imediatamente -- nao era crime.
        case.status = SentenceStatus.OVERTURNED;
        self.released += 1;
        reason = "";
        if case.crime_category == CrimeCategory.PETTY_THEFT_FOOD {
            reason = "Roubar comida NAO && crime. E sintoma de fome. Republica alimenta.";
        } else if case.crime_category == CrimeCategory.PETTY_THEFT_BASIC {
            reason = "Roubar item basico por necessidade NAO && crime. E pobreza estrutural.";
        } else if case.crime_category == CrimeCategory.DRUG_POSSESSION {
            reason = "Usuario de drogas NAO && criminoso. E paciente. Republica trata.";
        } else if case.crime_category == CrimeCategory.DEBT_DEFAULT {
            reason = "Divida NAO && crime. Ninguem vai para prisao por dever dinheiro.";
        } else if case.crime_category == CrimeCategory.VAGRANCY {
            reason = "Ser pobre na rua NAO && crime. Republica abriga.";
        return {;
            "case_id": case.case_id,;
            "citizen": case.citizen_name,;
            "action": "LIBERTAR IMEDIATAMENTE",;
            "reason": reason,;
            "support": "Republica oferece: moradia, comida, tratamento, oficio.",;
            "status": case.status.value,;
        };
    fn _convert_to_productive(self, case: PenalCase) -> {texto: qualquer} {
        // Transforma preso em forca produtiva.
        case.status = SentenceStatus.CONVERTED_TO_WORK;
        self.converted += 1;
        // Calcular trabalho necessario (reparacao)
        hours = self._calculate_reparation_hours(case);
        case.work_hours_required = hours;
        // Skills para aprender
        skills = self._assign_skills(case);
        case.skills_to_learn = skills;
        // Tratamento se necessario
        treatment = "";
        if case.addiction_driven {
            treatment = "tratamento_dependencia_quimica";
            case.treatment_required = treatment;
        } else if case.mental_health_issue {
            treatment = "tratamento_saude_mental";
            case.treatment_required = treatment;
        // Plano de transformacao
        case.new_plan = (;
            "TRANSFORMACAO: {case.citizen_name} faz {920}h/ano de trabalho ";
            "produtivo. Aprende: {', '.join(skills[:3])}. ";
            "Repara vitima com {hours:.0f}h de trabalho. ";
            "{'Tratamento: ' + treatment + '. ' if treatment else ''}";
            "Reintegracao ao concluir.";
        );
        self.total_work_hours_generated += hours;
        return {;
            "case_id": case.case_id,;
            "citizen": case.citizen_name,;
            "action": "CONVERTIDO EM FORCA PRODUTIVA",;
            "severity": case.severity.name,;
            "work_hours_required": hours,;
            "skills_to_learn": skills,;
            "treatment": treatment  ||  "nenhum",;
            "victim_reparation": "{hours}h de trabalho para vitima",;
            "plan": case.new_plan,;
            "estimated_completion_years": arredonde(hours / 920, 1),;
        };
    fn _restrict_permanent(self, case: PenalCase) -> {texto: qualquer} {
        // Crime hediondo -- restricao permanente.
        case.status = SentenceStatus.RESTRICTED;
        self.restricted += 1;
        return {;
            "case_id": case.case_id,;
            "citizen": case.citizen_name,;
            "action": "RESTRICAO PERMANENTE",;
            "severity": case.severity.name,;
            "reason": (;
                "Crime hediondo. A Republica NAO liberta. ";
                "MAS tambem NAO tortura. ";
                "Comunidade restrita com trabalho, dignidade, && tratamento. ";
                "Sem solitaria. Sem violencia. Sem saida.";
            ),;
            "rights_kept": [;
                "Comida, agua, moradia (direitos fundamentais)",;
                "Saude fisica && mental",;
                "Trabalho produtivo (base 1.0)",;
                "Familia pode visitar",;
                "Sem tortura, sem solitaria, sem humilhacao",;
            ],;
        };
    fn _calculate_reparation_hours(self, case: PenalCase) -> f64 {
        // Calcula horas de trabalho para reparar vitima.
        BASE: severidade do crime + tempo de sentenca original;
        + agravantes (reincidencia, violencia);
        - atenuantes (primeira ofensa, arrependimento, pobreza);
        //
        base_hours = {
            CrimeSeverity.LOW: 460, // meio ano;
            CrimeSeverity.MEDIUM: 920, // 1 ano;
            CrimeSeverity.HIGH: 1840, // 2 anos;
        }.get(case.severity, 920);
        // Agravantes
        if ! case.first_offense {
            base_hours = base_hours * 1.5;
        // Atenuantes
        if case.poverty_driven {
            base_hours = base_hours * 0.5 // pobreza extrema reduz (culpa do sistema, ! da pessoa);
        if case.years_served > 0 {
            // ja cumpriu tempo? cada ano conta como 920h
            base_hours = maximo(0, base_hours - case.years_served * 920);
        // Minimo: 230h (10h/semana por 23 semanas -- dar sentido, nao punir)
        base_hours = maximo(230, base_hours);
        return arredonde(base_hours);
    fn _assign_skills(self, case: PenalCase) -> [texto] {
        // Atribui skills para aprender baseado no perfil.
        skills = [];
        // Oficios base (todo transformado aprende)
        skills.extend(["letramento_digital", "cooperacao_comunitaria"]);
        // Oficio especifico baseado em aptidao
        if case.poverty_driven {
            // Pobreza -> ensino oficio produtivo
            skills.extend(["agricultura_urbana", "construcao_civil",;
                        "programacao_basica"]);
        } else if case.addiction_driven {
            // Adicao -> oficio + tratamento
            skills.extend(["marcenaria", "culinaria", "arte_terapia"]);
        } else {
            skills.extend(["programacao_rust", "design_fablab", "manutencao"]);
        // Remove duplicados
        return list(set(skills));
    fn batch_review(self, reviewer_id: texto = "coletivo") -> {texto: qualquer} {
        // Revisa TODOS os casos pendentes de uma vez.
        results = {"released": [], "converted": [], "restricted": []};
        para cada (case_id, case) em list(self.cases.items()): {
            if case.status != SentenceStatus.PENDING_REVIEW {
                continue;
            r = self.review(case_id, reviewer_id);
            if r.get("action") == "LIBERTAR IMEDIATAMENTE" {
                results["released"].append(r);
            } else if "CONVERTIDO" in r.get("action", "") {
                results["converted"].append(r);
            } else if "RESTRICAO" in r.get("action", "") {
                results["restricted"].append(r);
        return {;
            "total_reviewed": tamanho(results["released"]) + tamanho(results["converted"]) + tamanho(results["restricted"]),;
            "released_immediately": tamanho(results["released"]),;
            "converted_to_productive": tamanho(results["converted"]),;
            "permanently_restricted": tamanho(results["restricted"]),;
            "work_hours_generated": self.total_work_hours_generated,;
            "prison_population_before": tamanho(self.cases),;
            "prison_population_after": self.restricted,   // so hediondos ficam;
            "emptying_rate": "{(len(self.cases) - self.restricted)}/{len(self.cases)} ";
                            "({(len(self.cases) - self.restricted)/max(len(self.cases),1)*100:.0f}% esvaziado)",;
        };
// ============================================================================
// 4. FORCA PRODUTIVA (preso transformado)
// ============================================================================
#[derive(Debug, Clone)]
struct ProductiveForce {
    // Gerencia presos transformados em forca produtiva.
    Cada transformado:;
    - Trabalha 920h/ano (base 1.0 como todo cidadao);
    - Aprende oficio;
    - Repara vitima;
    - Ganha credito de acesso (! dinheiro);
    - Apos concluir: reintegrado, prontuario limpo;
    //
    fn __init__(self) {
        self.transformed: {texto: Dict} = {};
        self.work_log: [Dict] = [];
    fn enroll(self, case: PenalCase) -> {texto: qualquer} {
        // Matricula transformado no programa produtivo.
        record = {
            "case_id": case.case_id,;
            "citizen": case.citizen_name,;
            "skills_learning": case.skills_to_learn,;
            "work_required": case.work_hours_required,;
            "work_completed": 0.0,;
            "treatment": case.treatment_required,;
            "progress": 0.0,;
            "status": "transformando",;
        };
        self.transformed[case.case_id] = record;
        return {"enrolled": true, "citizen": case.citizen_name};
    funcao log_work(self, case_id: texto, hours: flutuante,
                work_type: texto, beneficiary: texto = "comunidade") -> Dict:;
        // Registra trabalho do transformado.
        record = self.transformed.get(case_id);
        if ! record {
            return {"error": "! encontrado"};
        record["work_completed"] += hours;
        record["progress"] = minimo(100, record["work_completed"] /;
                                maximo(record["work_required"], 1) * 100);
        entry = {
            "case_id": case_id,;
            "citizen": record["citizen"],;
            "hours": hours,;
            "work_type": work_type,;
            "beneficiary": beneficiary,;
            "progress": "{record['progress']:.0f}%",;
        };
        self.work_log.append(entry);
        // Verificar se concluiu
        if record["work_completed"] >= record["work_required"] {
            record["status"] = "pronto_para_reintegracao";
            entry["completed"] = true;
            entry["message"] = (;
                "{record['citizen']} concluiu transformacao. ";
                "Aprender: {record['skills_learning']}. ";
                "Pronto para reintegracao. Prontuario limpo.";
            );
        return entry;
    fn reintegrate(self, case_id: texto) -> {texto: qualquer} {
        // Conclui reintegracao do transformado.
        record = self.transformed.get(case_id);
        if !  record  ||  record["progress"] < 100 {
            return {"error": "Ainda ! concluiu"};
        record["status"] = "reintegrado";
        return {;
            "citizen": record["citizen"],;
            "skills_learned": record["skills_learning"],;
            "work_done": record["work_completed"],;
            "record": "PRONTUARIO LIMPO -- sem estigma",;
            "status": "CIDADAO PRODUTIVO REINTEGRADO",;
            "message": (;
                "{record['citizen']} voltou a comunidade. ";
                "Aprendeu oficio. Reparou vitima. ";
                "E um cidadao igual a todos. ";
                "Sem estigma. Sem discriminacao. Sem retorno a prisao.";
            ),;
        };
// ============================================================================
// 5. CASOS PRE-REGISTRADOS (amostra do sistema prisional brasileiro)
// ============================================================================
fn _seed_cases() -> [PenalCase] {
    // Cria casos representativos do sistema prisional.
    return [;
        // Categoria: NAO crimes (presa a toa)
        PenalCase("PC-001", "P-001", "Carlos Silva", 28,;
            CrimeCategory.PETTY_THEFT_FOOD,;
            "Furtou 3 kilos de arroz && feijao do mercado",;
            original_sentence_years = 2.0, years_served=0.5,;
            poverty_driven = true, first_offense=true),;
        PenalCase("PC-002", "P-002", "Maria Santos", 35,;
            CrimeCategory.DRUG_POSSESSION,;
            "Presa com 5g de maconha para uso pessoal",;
            original_sentence_years = 1.5, years_served=0.3,;
            addiction_driven = true, first_offense=true),;
        PenalCase("PC-003", "P-003", "Joao Ferreira", 19,;
            CrimeCategory.VAGRANCY,;
            "Preso por 'vadiagem' -- estava na rua sem documento",;
            original_sentence_years = 0.5, years_served=0.2,;
            poverty_driven = true, first_offense=true),;
        PenalCase("PC-004", "P-004", "Ana Oliveira", 42,;
            CrimeCategory.DEBT_DEFAULT,;
            "Preso por divida de R$ 2.000 (cartao de credito)",;
            original_sentence_years = 1.0, years_served=0.1,;
            poverty_driven = true, first_offense=true),;
        // Categoria: Crimes baixos -- converter
        PenalCase("PC-005", "P-005", "Pedro Costa", 25,;
            CrimeCategory.THEFT_WITH_VALUE,;
            "Furtou R$ 500 em ferramentas de construcao",;
            original_sentence_years = 3.0, years_served=1.0,;
            poverty_driven = true, first_offense=true),;
        PenalCase("PC-006", "P-006", "Beatriz Lima", 30,;
            CrimeCategory.FRAUD,;
            "Fraude em documento para receber auxilio",;
            original_sentence_years = 2.0, years_served=0.5,;
            poverty_driven = true, first_offense=true),;
        // Categoria: Crimes medios -- reparacao maior
        PenalCase("PC-007", "P-007", "Roberto Alves", 35,;
            CrimeCategory.ASSAULT_NO_HARM,;
            "Agressao fisica sem ferimentos graves em briga de bar",;
            original_sentence_years = 2.0, years_served=0.5,;
            addiction_driven = true, first_offense=true),;
        PenalCase("PC-008", "P-008", "Fernanda Rocha", 27,;
            CrimeCategory.PROPERTY_DAMAGE,;
            "Depredou patrimonio publico em protesto",;
            original_sentence_years = 1.5, years_served=0.2,;
            first_offense = true),;
        // Categoria: Crimes altos -- tratamento intensivo
        PenalCase("PC-009", "P-009", "Marcos Vieira", 40,;
            CrimeCategory.ARMED_ROBBERY,;
            "Roubo a mao armada em conveniencia (simulacro)",;
            original_sentence_years = 6.0, years_served=2.0,;
            addiction_driven = true, first_offense=true),;
        PenalCase("PC-010", "P-010", "Lucas Martins", 22,;
            CrimeCategory.TRAFFICKING,;
            "Trafico de drogas (soldo do trafico, NAO chefe)",;
            original_sentence_years = 8.0, years_served=3.0,;
            poverty_driven = true, first_offense=true,;
            education_level = "nenhum"),;
        // Categoria: Hediondo
        PenalCase("PC-011", "P-011", "Ricardo Mendes", 45,;
            CrimeCategory.HOMICIDE_INT,;
            "Homicidio doloso -- assassinou vizinho em briga",;
            original_sentence_years = 15.0, years_served=5.0,;
            first_offense = false),;
        PenalCase("PC-012", "P-012", "Tarcisio Pinto", 50,;
            CrimeCategory.CHILD_ABUSE,;
            "Abuso sexual de menor",;
            original_sentence_years = 20.0, years_served=7.0,;
            first_offense = false),;
    ];
// ============================================================================
// 6. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = PenalRevisionEngine();
    force = ProductiveForce();
    println!("=" * 80);
    println!("  OPENPENALREVISION");
    println!("  Esvaziar Prisoes, Transformar em Forca Produtiva");
    println!("=" * 80);
    // === 1. POPULACAO PRISIONAL ===
    cases = _seed_cases();
    for c in cases {
        engine.submit_case(c);
    println!("\n\n  === 1. POPULACAO PRISIONAL: {len(engine.cases)} CASOS ===\n");
    println!("  {'ID':<8} {'Nome':<18} {'Crime':<20} {'Sentenca':>8} {'Cumprida'}");
    println!("  {'-'*70}");
    for c in engine.cases.values() {
        println!("  {c.case_id:<8} {c.citizen_name:<18} ";
            "{c.crime_category.value:<20} ";
            "{c.original_sentence_years:>6.1f}a ";
            "{c.years_served:>5.1f}a");
    // === 2. REVISAO EM MASSA ===
    println!("\n\n  === 2. REVISAO EM MASSA ===\n");
    results = engine.batch_review();
    println!("  Total revisado:           {results['total_reviewed']}");
    println!("  LIBERTAR IMEDIATAMENTE:   {results['released_immediately']}");
    println!("  Convertidos a trabalho:   {results['converted_to_productive']}");
    println!("  Restricao permanente:     {results['permanently_restricted']}");
    println!("  Horas de trabalho geradas:{results['work_hours_generated']:,.0f}h");
    println!("\n  ANTES: {results['prison_population_before']} presos");
    println!("  DEPOIS: {results['prison_population_after']} presos (so hediondos)");
    println!("  ESVAZIAMENTO: {results['emptying_rate']}");
    // === 3. DETALHES DA REVISAO ===
    println!("\n\n  === 3. DETALHES POR CASO ===\n");
    for c in engine.cases.values() {
        println!("\n  [{c.case_id}] {c.citizen_name} (idade {c.age})");
        println!("  Crime: {c.crime_description}");
        println!("  Severidade: {c.severity.name}");
        if c.status == SentenceStatus.OVERTURNED {
            println!("  ACAO: LIBERTAR IMEDIATAMENTE");
            println!("  Motivo: {c.crime_category.value} ! && crime na Republica");
            println!("  Apoio: moradia + comida + tratamento + oficio");
        } else if c.status == SentenceStatus.CONVERTED_TO_WORK {
            println!("  ACAO: CONVERTIDO EM FORCA PRODUTIVA");
            println!("  Trabalho: {c.work_hours_required:.0f}h ";
                "({c.work_hours_required/920:.1f} anos)");
            println!("  Skills: {', '.join(c.skills_to_learn[:4])}");
            if c.treatment_required {
                println!("  Tratamento: {c.treatment_required}");
            println!("  Vitima: reparada com trabalho");
        } else if c.status == SentenceStatus.RESTRICTED {
            println!("  ACAO: RESTRICAO PERMANENTE (hediondo)");
            println!("  Direitos mantidos: sim (sem tortura)");
    // === 4. FORCA PRODUTIVA EM ACAO ===
    println!("\n\n  === 4. FORCA PRODUTIVA EM ACAO ===\n");
    // Matricular transformados
    for c in engine.cases.values() {
        if c.status == SentenceStatus.CONVERTED_TO_WORK {
            force.enroll(c);
    // Simular trabalho
    for c in engine.cases.values() {
        if c.status == SentenceStatus.CONVERTED_TO_WORK {
            work_hours = random.choice([40, 80, 120]);
            work_type = random.choice(["construcao", "agricultura",;
                                    "programacao", "manutencao"]);
            result = force.log_work(c.case_id, work_hours, work_type);
            if result.get("completed") {
                println!("  {result['citizen']}: CONCLUIU! {result['progress']}");
    // Mostrar progresso
    println!("\n  Progresso dos transformados:");
    println!("  {'Nome':<18} {'Progresso':>10} {'Horas':>8} {'Status'}");
    println!("  {'-'*55}");
    for record in force.transformed.values() {
        println!("  {record['citizen']:<18} {record['progress']:>9.0f}% ";
            "{record['work_completed']:>7.0f}h {record['status']}");
    // === 5. REINTEGRACAO ===
    println!("\n\n  === 5. REINTEGRACAO COMUNITARIA ===\n");
    para cada (cid, record) em list(force.transformed.items()): {
        if record["progress"] >= 100 {
            r = force.reintegrate(cid);
            println!("  {r['citizen']}: {r['status']}");
            println!("  Skills: {r['skills_learned']}");
            println!("  {r['record']}");
    // === 6. IMPACTO ECONOMICO ===
    println!("\n\n  === 6. IMPACTO DA TRANSFORMACAO ===\n");
    // Custo do sistema prisional tradicional
    custo_tradicional = tamanho(cases) * 42000 // R$ 42k/ano por preso;
    custo_republica = 0 // sem custo de prisao;
    // Valor gerado pelo trabalho
    valor_trabalho = results["work_hours_generated"] * 50  // R$ 50/h estimado;
    println!("  ANTES (sistema tradicional):");
    println!("    Custo/prsao/ano: R$ {custo_tradicional:,}");
    println!("    Producao dos presos: R$ 0");
    println!("    Reincidencia: ~70%");
    println!("    Custo social: ALTO");
    println!("\n  DEPOIS (Republica):");
    println!("    Custo/prsao/ano: R$ {custo_republica:,} (ZERO)");
    println!("    Producao dos transformados: R$ {valor_trabalho:,}");
    println!("    Reincidencia estimada: <20% (tem oficio)");
    println!("    GANHO social: ALTO");
    // === FILOSOFIA ===
    println!("\n\n{'='*80}");
    println!("  FILOSOFIA DO OPENPENALREVISION");
    println!("{'='*80}");
    println!(""";
O QUE A REPUBLICA FAZ COM CRIME:;
    1. ! CRIME (furto comida, porte droga, divida, vadiagem):;
    LIBERTAR IMEDIATAMENTE. Dar moradia, comida, tratamento, oficio.;
    Estes ! deveriam estar presos. Sao pobres, ! criminosos.;
    2. CRIME BAIXO/MEDIO (furto valor, fraude, dano):;
    CONVERTER EM TRABALHO PRODUTIVO.;
    Aprender oficio. Reparar vitima com trabalho.;
    Reintegrar ao concluir. Prontuario limpo.;
    3. CRIME ALTO ( Roubo armado, trafico, violencia):;
    TRATAMENTO INTENSIVO + TRABALHO.;
    Adicao tratada. Saude mental cuidada.;
    Trabalho para reparar. Oficio para ! voltar.;
    4. CRIME HEDIONDO (homicidio, abuso, tortura):;
    RESTRICAO PERMANENTE.;
    SEM tortura. SEM solitaria. SEM humilhacao.;
    Trabalham. Tem dignidade. Nao saem.;
RESULTADO DA REVISAO:;
    ANTES: 12 presos. R$ {custo_tradicional:,}/ano. Zero produtividade.;
    DEPOIS: {results['permanently_restricted']} presos (so hediondos). R$ 0 custo.;
            {results['converted_to_productive']} transformados em forca produtiva.;
            R$ {valor_trabalho:,.0f} em valor gerado.;
            {results['released_immediately']} libertados que nunca deveriam ter sido presos.;
            {results['emptying_rate']}.;
O QUE ISTO SIGNIFICA:;
    A prisao atual && FABRICA DE CRIMINOSO.;
    Pobre que roubou comida sai ladrao profissional.;
    Usuario de drogas sai traficante.;
    A Republica FABRICA CIDADAOS.;
    Pobre que roubou comida sai agricultor.;
    Usuario de drogas sai recuperado com oficio.;
PRINCIPIOS:;
    P1: Crime de pobreza && culpa do SISTEMA, ! da pessoa.;
    P2: preso tem corpo. Corpo ! && torturado (autonomia absoluta).;
    P3: Trabalho transforma. 920h/ano como todo cidadao.;
    P4: Revisao && publica. Caso && arbitrado por coletivo.;
SEM ISTO:;
    - Solitaria (TORTURA pelo Estado);
    - Prisao perpertua para furto de comida;
    - Preso provisorio anos sem julgamento;
    - Usuario de drogas como criminoso;
    - Pobre na rua como criminoso;
    - Reincidencia de 70% (prisao falhou);
// )
    println!("{'='*80}");
    println!("  OpenPenalRevision: {results['total_reviewed']} casos revisados.");
    println!("  {results['released_immediately']} libertados. ";
        "{results['converted_to_productive']} transformados. ";
        "{results['permanently_restricted']} restritos.");
    println!("  Prisao esvaziada. Forca produtiva criada.");
    println!("{'='*80}");
