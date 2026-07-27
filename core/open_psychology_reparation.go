// OpenPsychologyReparation -- Reavaliacao e Reparacao de Diagnosticos -- gerado de Portugol++
package openpsychologyreparation_reavaliacao_e_reparacao_de_diagnosticos

import "fmt"

// !/usr/bin/env python3
//
OpenPsychologyReparation -- Reavaliacao && Reparacao de Diagnosticos
=====================================================================
"Um diagnostico errado ! && um erro de papel. && um inferno humano.
Crianca rotulada de 'doente' cresce acreditando que && quebrada.
Adulto medicado por diagnosticoFabricado perde anos de vida.
A Republica ! aceita isso em silencio."
O QUE ISTO FAZ:
1. REAVALIACAO: reabre diagnosticos passados com criterios novos
2. REPARACAO: calcula dano && define compensacao
3. RESPONSABILIDADE: identifica quem errou (medico, sistema, industria)
4. PREVENCAO: impede novos diagnosticos errados
PRINCIPIOS:
P1: diagnostico errado && ELITISMO MEDICO -- medic se acha dono da verdade
P2: rotular corpo-mente alheio sem base = VIOLACAO DE AUTONOMIA CORPORAL
P3 := TRABALHO ROUBADO (anos de vida perdidos) // sofrimento por erro
P4: reavaliacao && DIREITO, ! favor
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// ============================================================================
// 1. CATEGORIAS DE ERRO DIAGNOSTICO
// ============================================================================
type ErrorType int
const (
    // Tipo de erro diagnostico.
    OVERDIAGNOSIS = "superdiagnostico"  // patologizou normalidade
    MISDIAGNOSIS = "diagnostico_errado"  // diagnostico A, era B
    FABRICATED = "fabricado"  // diagnostico sem base real
    PRESSURE = "pressao_farmaceutica"  // industria empurrou
    CHILD_LABEL = "rotulo_infantil"  // rotulou crianca sem necessidade
    CULTURAL_BLINDNESS = "cegueira_cultural"  // patologizou diferenca cultural
    GENDER_BIAS = "vies_genero"  // patologizou comportamento feminino
    PROFIT_DRIVEN = "lucro"  // diagnostico para vender remedio
type HarmCategory int
const (
    // Tipo de dano causado pelo erro.
    NONE = 0
    STIGMA = 1 // marcado socialmente
    SELF_IDENTITY = 2  // passou a se ver como "doente"
    MEDICATION_HARM = 3 // tomou remedio desnecessario com efeito colateral
    YEARS_LOST = 4  // anos de vida vividos como "defeituoso"
    FAMILY_DISRUPTION = 5 // familia reorganizou vida em torno do rotulo
    CAREER_BLOCKED = 6 // perdeu oportunidades por causa do rotulo
    INSTITUTIONALIZED = 7 // foi internado/tratado desnecessariamente
    CHILDHOOD_STOLEN = 8 // infancia roubada por rotulo infantil
type Liable int
const (
    // Quem e responsavel pelo erro.
    INDIVIDUAL_DOCTOR = "medico_individual"
    CLINIC_HOSPITAL = "clinica_hospital"
    PHARMA_COMPANY = "industria_farmaceutica"
    DIAGNOSTIC_MANUAL = "manual_dsm_cie"  // o proprio DSM/ICD falhou
    INSURANCE_SYSTEM = "seguro_saude"  // sistema empurrou diagnostico
    STATE = "estado"  // politica de saude publicou erro
    MULTIPLE = "multiplos"
// ============================================================================
// 2. CASO DE REAVALIACAO
// ============================================================================
// decorador: @dataclass
type DiagnosisCase struct {
    // Um caso de diagnostico a ser reavaliado.
    case_id: texto
    citizen_id: texto
    citizen_name: texto
    original_diagnosis: texto // diagnostico original
    diagnosing_doctor := "" // string
    diagnosing_institution := "" // string
    diagnosis_date := ""  // quando foi diagnosticado // string
    diagnosis_age := 0 // idade na epoca // int64
    current_age := 0 // int64
    medication_prescribed := "" // string
    years_on_medication := 0.0 // float64
    years_labeled := 0.0 // anos vivendo com o rotulo // float64
    // Reavaliacao
    error_type := nil // ErrorType?
    harm_categories := field(default_factory=list) // [HarmCategory]
    harm_severity_score := 0.0 // 0-100 // float64
    liable := Liable.INDIVIDUAL_DOCTOR // Liable
    // Reparacao
    reparation_work_hours := 0.0 // horas de trabalho reconhecidas como reparacao // float64
    reparation_credit := 0.0 // credito de acesso // float64
    apology_required := true // bool
    public_record_correction := true // apagar rotulo do prontuario // bool
    // Status
    status := "pendente"  // pendente, reavaliado, reparado // string
    reavaliated_by := field(default_factory=list) // [texto]
    notes := "" // string
    // decorador: @property
    func was_child(self) bool {
        return self.diagnosis_age > 0 && self.diagnosis_age < 18
    // decorador: @property
    func harm_description(self) string {
        descs = {
            HarmCategory.STIGMA: "Estigmatizacao social",
            HarmCategory.SELF_IDENTITY: "Identidade danificada (se viu como doente)",
            HarmCategory.MEDICATION_HARM: "Dano por medicacao desnecessaria",
            HarmCategory.YEARS_LOST: "Anos de vida vividos como defeituoso",
            HarmCategory.FAMILY_DISRUPTION: "Familia reorganizada em torno do rotulo",
            HarmCategory.CAREER_BLOCKED: "Oportunidades perdidas",
            HarmCategory.INSTITUTIONALIZED: "Internacao/tratamento desnecessario",
            HarmCategory.CHILDHOOD_STOLEN: "Infancia roubada pelo rotulo",
        }
        return "; ".join(descs[h] para h em self.harm_categories)
// ============================================================================
// 3. MOTOR DE REAVALIACAO
// ============================================================================
type DiagnosisReassessment struct {
    // Reavalia diagnosticos passados sob criterios novos da Republica.
    CRITERIOS DE REAVALIACAO:
    1. O diagnostico tem base neurologica COMPROVADA (imagem, genetica)?
    2. Ou && CONSTRUTO SOCIAL que mudou entre culturas/epocas?
    3. A pessoa foi medicada? Qual dano da medicacao?
    4. A pessoa era crianca? Rotulo infantil && mais grave.
    5. Quem lucrou com o diagnostico? (medico? farmaceutica? clinica?)
    6. A pessoa concordava com o diagnostico || foi imposto?
    7. O diagnostico impediu a pessoa de algo? (trabalho, estudo, vida)
    //
    func __init__(self) {
        self.cases: {texto: DiagnosisCase} = {}
        self.reassessed: inteiro = 0
        self.overturned: inteiro = 0
        self.reparations_total_hours: flutuante = 0.0
    func submit_case(self, case: DiagnosisCase) {texto: qualquer} {
        // Submete um caso para reavaliacao.
        self.cases[case.case_id] = case
        return {
            "submitted": true,
            "case_id": case.case_id,
            "citizen": case.citizen_name,
            "original_diagnosis": case.original_diagnosis,
            "status": "aguardando reavaliacao",
        }
    funcao reassess(self, case_id: texto, error_type: ErrorType,
                harms: [HarmCategory], liable: Liable,
                assessor_id: texto,
                notes := "") -> {texto: qualquer}: // string
        // Reavalia um caso -- determina se houve erro e qual dano.
        case = self.cases.get(case_id)
        if ! case {
            return {"error": "Caso ! encontrado"}
        case.error_type = error_type
        case.harm_categories = harms
        case.liable = liable
        case.notes = notes
        case.status = "reavaliado"
        case.reavaliated_by.append(assessor_id)
        self.reassessed += 1
        // Calcular dano
        case.harm_severity_score = self._calculate_harm(case)
        // Calcular reparacao
        case.reparation_work_hours, case.reparation_credit = \
            self._calculate_reparation(case)
        if error_type != ErrorType.MISDIAGNOSIS || harms {
            self.overturned += 1
        self.reparations_total_hours += case.reparation_work_hours
        return {
            "case_id": case_id,
            "citizen": case.citizen_name,
            "error_type": error_type.value,
            "harm_severity": "{case.harm_severity_score:.0f}/100",
            "liable": liable.value,
            "reparation_hours": case.reparation_work_hours,
            "reparation_credit": case.reparation_credit,
            "apology_required": case.apology_required,
            "record_correction": case.public_record_correction,
            "verdict": self._verdict(case),
        }
    func _calculate_harm(self, case: DiagnosisCase) float64 {
        // Calcula score de dano (0-100).
        score = 0
        // Tipo de erro
        error_weights = {
            ErrorType.OVERDIAGNOSIS: 20,
            ErrorType.MISDIAGNOSIS: 35,
            ErrorType.FABRICATED: 50,
            ErrorType.PRESSURE: 40,
            ErrorType.CHILD_LABEL: 45,
            ErrorType.CULTURAL_BLINDNESS: 25,
            ErrorType.GENDER_BIAS: 30,
            ErrorType.PROFIT_DRIVEN: 45,
        }
        score = score + error_weights.get(case.error_type, 15)
        // Categorias de dano
        harm_weights = {
            HarmCategory.STIGMA: 10,
            HarmCategory.SELF_IDENTITY: 20,
            HarmCategory.MEDICATION_HARM: 25,
            HarmCategory.YEARS_LOST: 15,
            HarmCategory.FAMILY_DISRUPTION: 10,
            HarmCategory.CAREER_BLOCKED: 15,
            HarmCategory.INSTITUTIONALIZED: 20,
            HarmCategory.CHILDHOOD_STOLEN: 30,
        }
        for _, h := range case.harm_categories {
            score = score + harm_weights.get(h, 5)
        // Agravantes
        if case.was_child {
            score = score + 15 // rotulo infantil && mais grave
        if case.years_on_medication > 5 {
            score = score + 10
        if case.years_labeled > 10 {
            score = score + 10
        return minimo(100, score)
    func _calculate_reparation(self, case: DiagnosisCase) retorna (flutuante, flutuante) {
        // Calcula reparacao em horas de trabalho reconhecido + credito.
        FORMULA:
        - Base: 920h (1 ano de contrato base 1.0) por ano rotulado
        - Dano severo: +50% se harm > 70
        - Crianca: +100% (infancia roubada vale mais)
        - Medicacao: +20h por ano medicado
        - Credito de acesso: horas / 10
        //
        years = maximo(1, case.years_labeled)
        // Anos de rotulo -> horas
        hours = years * 920 // 1 ano de vida base por ano roubado
        // Medicacao
        hours = hours + case.years_on_medication * 40
        // Agravante severidade
        if case.harm_severity_score > 70 {
            hours = hours * 1.5
        // Dobro para criancas
        if case.was_child {
            hours = hours * 2.0
        hours = arredonde(hours)
        credit = arredonde(hours / 10, 1)
        return hours, credit
    func _verdict(self, case: DiagnosisCase) string {
        // Veredicto textual.
        if case.harm_severity_score >= 80 {
            severity = "DEVASTADOR"
        } else if case.harm_severity_score >= 60 {
            severity = "GRAVE"
        } else if case.harm_severity_score >= 40 {
            severity = "SIGNIFICATIVO"
        } else if case.harm_severity_score >= 20 {
            severity = "MODERADO"
        } else {
            severity = "LEVE"
        target = {
            Liable.INDIVIDUAL_DOCTOR: "Dr(a). {case.diagnosing_doctor}",
            Liable.CLINIC_HOSPITAL: case.diagnosing_institution,
            Liable.PHARMA_COMPANY: "industria farmaceutica",
            Liable.DIAGNOSTIC_MANUAL: "manual diagnostico (DSM/ICD)",
            Liable.INSURANCE_SYSTEM: "sistema de seguro de saude",
            Liable.STATE: "Estado (politica de saude publica)",
            Liable.MULTIPLE: "multiplas partes",
        }.get(case.liable, "responsavel ! identificado")
        return (
            "DANO {severity}: {case.citizen_name} viveu {case.years_labeled:.0f} "
            "anos rotulado como '{case.original_diagnosis}'. "
            "Erro: {case.error_type.value}. "
            "Responsavel: {target}. "
            "Reparacao: {case.reparation_work_hours:.0f}h de trabalho reconhecido "
            "+ {case.reparation_credit:.1f} creditos de acesso. "
            "Prontuario: retificar. "
            "Pedir desculpas: {'SIM' if case.apology_required else '!'}."
        )
    funcao batch_reassess(self, diagnosis_name: texto,
                    error_type: ErrorType,
                    harms: [HarmCategory],
                    liable: Liable,
                    assessor_id: texto) -> [Dict]:
        // Reavalia TODOS os casos com o mesmo diagnostico de uma vez.
        Uso: quando se descobre que um diagnostico inteiro era invalido
        (ex: TDAH em criancas que eram apenas energetic as),
        reabre TODOS os casos relacionados.
        //
        results = []
        para cada (cid, case) em self.cases.items(): {
            if diagnosis_name.lower() in case.original_diagnosis.lower() {
                r = self.reassess(cid, error_type, harms, liable, assessor_id)
                results.append(r)
        return results
    func report(self) {texto: qualquer} {
        // Relatorio geral de reavaliacoes.
        by_error = defaultdict(inteiro)
        by_liable = defaultdict(inteiro)
        by_harm = defaultdict(inteiro)
        total_hours = 0
        for _, case := range self.cases.values() {
            if case.status in ("reavaliado", "reparado") {
                if case.error_type {
                    by_error[case.error_type.value] += 1
                by_liable[case.liable.value] += 1
                for _, h := range case.harm_categories {
                    by_harm[h.name] += 1
                total_hours = total_hours + case.reparation_work_hours
        return {
            "total_cases": len(self.cases),
            "reassessed": self.reassessed,
            "overturned": self.overturned,
            "by_error_type": dict(by_error),
            "by_liable": dict(by_liable),
            "by_harm": dict(by_harm),
            "total_reparation_hours": total_hours,
            "avg_harm_score": (
                soma(c.harm_severity_score para c em self.cases.values()
                    if c.status in ("reavaliado", "reparado")) / maximo(self.reassessed, 1)
            ),
        }
// ============================================================================
// 4. POLITICA DE PAGAMENTO POR SOFRIMENTO
// ============================================================================
type SufferingCompensation struct {
    // Politica de compensacao por sofrimento decorrente de diagnostico errado.
    NA REPUBLICA ! HA DINHEIRO. Mas ha:
    1. TRABALHO RECONHECIDO: anos perdidos contam como trabalho (P3)
    2. CREDITO DE ACESSO: proporcional ao dano
    3. RETIFICACAO PUBLICA: prontuario corrigido, nome limpo
    4. PEDIDO DE DESCULPAS: do responsavel (publico se institucional)
    5. APOIO CONTINUO: terapia, acompanhamento, comunidaded de suporte
    O QUE ! EXISTE:
    - Dinheiro/indenizacao monetaria (sem moeda)
    - Processo judicial adversarial (sem advogados, sem litigio)
    - Puniciao perpetua (responsavel repara && recupera)
    O QUE EXISTE:
    - Reconhecimento do dano (verdade, ! negacao)
    - Reparacao em trabalho + credito
    - Retificacao de registro
    - Apoio a recuperacao
    - Prevencao (! repetir)
    //
    func __init__(self) {
        self.reassessor = DiagnosisReassessment()
        self.compensations: [Dict] = []
    func process_compensation(self, case_id: texto) {texto: qualquer} {
        // Processa compensacao completa para um caso reavaliado.
        case = self.reassessor.cases.get(case_id)
        if !  case  ||  case.status != "reavaliado" {
            return {"error": "Caso ! encontrado || ! reavaliado"}
        compensation = {
            "case_id": case_id,
            "citizen": case.citizen_name,
            "diagnosis": case.original_diagnosis,
            "harm_severity": case.harm_severity_score,
            "components": {
                // 1. Trabalho reconhecido (anos perdidos contam como contrib)
                "trabalho_reconhecido_horas": case.reparation_work_hours,
                "trabalho_reconhecido_anos": arredonde(
                    case.reparation_work_hours / 920, 1),
                // 2. Credito de acesso
                "credito_acesso": case.reparation_credit,
                // 3. Retificacao
                "retificacao_prontuario": "Prontuario medico retificado. "
                                        "Rotulo removido. Historico corrigido.",
                // 4. Pedido de desculpas
                "pedido_desculpas": self._who_apologizes(case),
                // 5. Apoio continuo
                "apoio_continuo": self._support_plan(case),
            },
            "responsible": case.liable.value,
            "verdict": self.reassessor._verdict(case),
        }
        self.compensations.append(compensation)
        case.status = "reparado"
        return compensation
    func _who_apologizes(self, case: DiagnosisCase) string {
        // Define quem pede desculpas e como.
        if case.liable == Liable.INDIVIDUAL_DOCTOR {
            return (
                "Dr(a). {case.diagnosing_doctor} deve pedir desculpas "
                "pessoalmente a {case.citizen_name}. "
                "Reconhecimento do erro. Sem advogado. Humano a humano."
            )
        if case.liable == Liable.CLINIC_HOSPITAL {
            return (
                "{case.diagnosing_institution} deve emitir pedido de desculpas "
                "publico + retificacao no prontuario. "
                "Responsavel institucional (diretor) assina."
            )
        if case.liable == Liable.PHARMA_COMPANY {
            return (
                "Industria farmaceutica deve pedir desculpas PUBLICAS. "
                "Acknowledgment de que empurrou diagnostico para vender "
                "remedio. Cessar a pratica."
            )
        if case.liable == Liable.DIAGNOSTIC_MANUAL {
            return (
                "Manual diagnostico (DSM/ICD) deve ser revisado publicamente. "
                "Categoria invalidada. Comite da Republica emite nota."
            )
        if case.liable == Liable.STATE {
            return (
                "Estado deve pedir desculpas PUBLICAS. "
                "Politica de saude publicada que gerou o erro deve ser "
                "revogada. Vitimas identificadas && contatadas."
            )
        return "Responsavel deve pedir desculpas conforme avaliacao."
    func _support_plan(self, case: DiagnosisCase) {texto: texto} {
        // Plano de apoio continuo para recuperacao.
        plan = {
            "terapia": (
                "Acesso prioritario a psicologo da Republica (OpenPsychology). "
                "Minimo 12 sessoes. Sem rotular novamente."
            ),
            "comunidade": (
                "Conexao com comunidade de pessoas reavaliadas. "
                "Grupos de suporte mutuo. Sem hierarquia."
            ),
            "saude_fisica": (
                "Avaliacao de danos da medicacao desnecessaria. "
                "OpenHealth acompanha desmame de remedio se aplicavel."
            ),
            "identidade": (
                "Apoio para reconstruir identidade sem o rotulo. "
                "Anos de se ver como 'doente' deixam marca. "
                "Recuperar auto-imagem && trabalho."
            ),
        }
        if case.was_child {
            plan["familia"] = (
                "Familia tambem && vitima -- reorganizou vida em torno do "
                "rotulo. Terapia familiar. Desfazer mudancas desnecessarias."
            )
        if case.harm_severity_score >= 70 {
            plan["prioridade"] = (
                "DANO SEVERO: acompanhamento intensivo por 12 meses. "
                "Guardiao de saude designado. Checagem mensal."
            )
        return plan
// ============================================================================
// 5. CASOS PRE-REGISTRADOS (exemplos representativos)
// ============================================================================
func _seed_cases() DiagnosisReassessment {
    // Cria casos representativos de erros diagnosticos comuns.
    r = DiagnosisReassessment()
    cases = [
        DiagnosisCase(
            "CASE-001", "C-100", "Maria (35)", "TDAH",
            diagnosing_doctor = "Dr. Silva",
            diagnosing_institution = "Clinica A",
            diagnosis_date = "2005", diagnosis_age=14, current_age=35,
            medication_prescribed = "Ritalina 20mg",
            years_on_medication = 12,
            years_labeled = 21,
            notes = "Diagnostico aos 14 anos por ser 'agitada' na escola. "
                "Na verdade era adolescente com energia normal. "
                "Tomou ritalina por 12 anos. Perdeu adolescencia "
                "se sentindo defeituosa."
        ),
        DiagnosisCase(
            "CASE-002", "C-101", "Joao (28)", "TEA nivel 1 (Asperger)",
            diagnosing_doctor = "Dra. Costa",
            diagnosing_institution = "Hospital B",
            diagnosis_date = "2010", diagnosis_age=12, current_age=28,
            medication_prescribed = "Nenhuma",
            years_on_medication = 0,
            years_labeled = 18,
            notes = "Rotulado aos 12 por ser introvertido && gostar de "
                "computadores. Na verdade era crianca timida com "
                "interesse especifico. Rotulo travou socializacao."
        ),
        DiagnosisCase(
            "CASE-003", "C-102", "Ana (42)", "Bipolaridade",
            diagnosing_doctor = "Dr. Pires",
            diagnosing_institution = "Clinica C",
            diagnosis_date = "2012", diagnosis_age=28, current_age=42,
            medication_prescribed = "Litosina + antipsicotico",
            years_on_medication = 10,
            years_labeled = 14,
            notes = "Diagnosticada bipolar por ter fases de energia && "
                "tristeza -- normalidade humana. Medicada por 10 anos. "
                "Ganhou 30kg, perdeu libido, desenvolveu diabetes."
        ),
        DiagnosisCase(
            "CASE-004", "C-103", "Pedro (19)", "TDAH + Oposicionista",
            diagnosing_doctor = "Dra. Lima",
            diagnosing_institution = "Posto de Saude",
            diagnosis_date = "2015", diagnosis_age=8, current_age=19,
            medication_prescribed = "Concerta 36mg",
            years_on_medication = 8,
            years_labeled = 11,
            notes = "Crianca negra de periferia rotulada aos 8 anos. "
                "'Oposicionista' = questionava professora. "
                "Na verdade era inteligente && entediada. "
                "Medicada para ficar quieta. Cegueira cultural+racial."
        ),
        DiagnosisCase(
            "CASE-005", "C-104", "Beatriz (50)", "Depressao clinica",
            diagnosing_doctor = "Dr. Souza",
            diagnosing_institution = "Clinica D",
            diagnosis_date = "2008", diagnosis_age=32, current_age=50,
            medication_prescribed = "Antidepressivos variados",
            years_on_medication = 18,
            years_labeled = 18,
            notes = "Diagnosticada depressiva por estar triste apos "
                "divorcio. Luto normal patologizado. 18 anos de "
                "antidepressivo que nunca resolveu porque o problema "
                "! era quimico."
        ),
        DiagnosisCase(
            "CASE-006", "C-105", "Lucas (16)", "TEA nivel 2",
            diagnosing_doctor = "Equipe multidisciplinar",
            diagnosing_institution = "Hospital Infantil",
            diagnosis_date = "2016", diagnosis_age=6, current_age=16,
            medication_prescribed = "Risperidona",
            years_on_medication = 7,
            years_labeled = 10,
            notes = "Crianca autentica rotulada aos 6. Risperidona "
                "(antipsicotico) para 'comportamento'. Ganhou peso, "
                "ficou letargica. Infancia roubada."
        ),
    ]
    for _, case := range cases {
        r.submit_case(case)
    return r
// ============================================================================
// 6. MAIN
// ============================================================================
if __name__ == "__main__" {
    r = _seed_cases()
    comp = SufferingCompensation()
    comp.reassessor = r
    fmt.Println("=" * 80)
    fmt.Println("  OPENPSYCHOLOGYREPARATION")
    fmt.Println("  Reavaliacao de Diagnosticos + Pagamento por Sofrimento")
    fmt.Println("=" * 80)
    // === 1. CASOS SUBMETIDOS ===
    fmt.Println("\n\n  === 1. CASOS PARA REAVALIACAO: {len(r.cases)} ===\n")
    fmt.Println("  {'ID':<10} {'Cidadao':<14} {'Diagnostico':<20} "
        "{'Idade':>6} {'Anos rotulo':>11} {'Medicado'}")
    fmt.Println("  {'-'*80}")
    for _, c := range r.cases.values() {
        fmt.Println("  {c.case_id:<10} {c.citizen_name:<14} "
            "{c.original_diagnosis:<20} {c.diagnosis_age:>5}a "
            "{c.years_labeled:>9.0f}a "
            "{c.years_on_medication:.0f}a")
    // === 2. REAVALIACAO ===
    fmt.Println("\n\n  === 2. REAVALIACAO DE CADA CASO ===\n")
    r.reassess("CASE-001", ErrorType.OVERDIAGNOSIS,
            [HarmCategory.MEDICATION_HARM, HarmCategory.YEARS_LOST,
                HarmCategory.CHILDHOOD_STOLEN, HarmCategory.SELF_IDENTITY],
            Liable.PHARMA_COMPANY, "ASSESSOR-1",
            "TDAH superdiagnosticado em adolescente energetic a. "
            "Industria farmaceutica empurrou ritalina.")
    r.reassess("CASE-002", ErrorType.OVERDIAGNOSIS,
            [HarmCategory.STIGMA, HarmCategory.SELF_IDENTITY,
                HarmCategory.CHILDHOOD_STOLEN],
            Liable.DIAGNOSTIC_MANUAL, "ASSESSOR-1",
            "Introvertido com interesse especifico rotulado "
            "autista. Criterios DSM amplos demais.")
    r.reassess("CASE-003", ErrorType.MISDIAGNOSIS,
            [HarmCategory.MEDICATION_HARM, HarmCategory.YEARS_LOST],
            Liable.INDIVIDUAL_DOCTOR, "ASSESSOR-2",
            "Variacao emocional normal patologizada. "
            "Medicacao causou diabetes && obesidade.")
    r.reassess("CASE-004", ErrorType.CULTURAL_BLINDNESS,
            [HarmCategory.CHILDHOOD_STOLEN, HarmCategory.MEDICATION_HARM,
                HarmCategory.CAREER_BLOCKED],
            Liable.MULTIPLE, "ASSESSOR-1",
            "Crianca negra rotulada por comportamento que em "
            "crianca branca seria 'lideranca'. Racismo estrutural "
            "na psiquiatria.")
    r.reassess("CASE-005", ErrorType.OVERDIAGNOSIS,
            [HarmCategory.MEDICATION_HARM, HarmCategory.YEARS_LOST],
            Liable.INDIVIDUAL_DOCTOR, "ASSESSOR-2",
            "Luto normal patologizado. 18 anos de antidepressivo "
            "para tristeza que era humana, ! quimica.")
    r.reassess("CASE-006", ErrorType.CHILD_LABEL,
            [HarmCategory.CHILDHOOD_STOLEN, HarmCategory.MEDICATION_HARM,
                HarmCategory.INSTITUTIONALIZED],
            Liable.CLINIC_HOSPITAL, "ASSESSOR-1",
            "Crianca autentica rotulada && medicada com antipsicotico. "
            "Infancia roubada.")
    for _, cid := range r.cases {
        c = r.cases[cid]
        fmt.Println("\n  [{c.case_id}] {c.citizen_name}")
        fmt.Println("  Diagnostico original: {c.original_diagnosis}")
        fmt.Println("  Erro: {c.error_type.value}")
        fmt.Println("  Dano: {c.harm_severity_score:.0f}/100")
        fmt.Println("  Responsavel: {c.liable.value}")
        fmt.Println("  Danos: {c.harm_description}")
        fmt.Println("  VEREDICTO: {r._verdict(c)}")
    // === 3. COMPENSACAO ===
    fmt.Println("\n\n  === 3. COMPENSACAO POR SOFRIMENTO ===\n")
    for _, cid := range r.cases {
        result = comp.process_compensation(cid)
        if "error" in result {
            continue
        fmt.Println("\n  [{result['case_id']}] {result['citizen']}")
        fmt.Println("  Diagnostico: {result['diagnosis']}")
        comp_components = result["components"]
        fmt.Println("  Trabalho reconhecido: "
            "{comp_components['trabalho_reconhecido_horas']:.0f}h "
            "({comp_components['trabalho_reconhecido_anos']:.1f} anos)")
        fmt.Println("  Credito de acesso: {comp_components['credito_acesso']}")
        fmt.Println("  Retificacao: {comp_components['retificacao_prontuario'][:60]}")
        fmt.Println("  Desculpas: {comp_components['pedido_desculpas'][:80]}")
        plan = comp_components['apoio_continuo']
        fmt.Println("  Apoio: {', '.join(plan.keys())}")
    // === 4. RELATORIO GERAL ===
    fmt.Println("\n\n  === 4. RELATORIO GERAL ===\n")
    rep = r.report()
    fmt.Println("  Casos reavaliados:     {rep['reassessed']}")
    fmt.Println("  Diagnosticos revogados:{rep['overturned']}")
    fmt.Println("  Dano medio:            {rep['avg_harm_score']:.0f}/100")
    fmt.Println("  Reparacao total:       {rep['total_reparation_hours']:,.0f}h "
        "({rep['total_reparation_hours']/920:.0f} anos de trabalho)")
    fmt.Println("\n  Por tipo de erro:")
    para err, count in ordene(rep["by_error_type"].items(), {
                            key = (x) -> -x[1]):
        fmt.Println("    {err:<25} {count}")
    fmt.Println("\n  Por responsavel:")
    para liable, count in ordene(rep["by_liable"].items(), {
                                key = (x) -> -x[1]):
        fmt.Println("    {liable:<25} {count}")
    fmt.Println("\n  Por tipo de dano:")
    para harm, count in ordene(rep["by_harm"].items(), {
                            key = (x) -> -x[1]):
        fmt.Println("    {harm:<25} {count}")
    // === FILOSOFIA ===
    fmt.Println("\n\n{'='*80}")
    fmt.Println("  POLITICA DE REPARACAO PSICOLOGICA")
    fmt.Println("{'='*80}")
    fmt.Println("""
O QUE A REPUBLICA RECONHECE:
    Diagnosticos psiquiatricos errados causaram sofrimento real.
    Criancas rotuladas cresceram acreditando serem quebradas.
    Adultos medicados perderam anos de vida.
    Familias reorganizaram tudo em torno de rotulos falsos.
    Industria farmaceutica lucrou com sofrimento fabricado.
O QUE A REPUBLICA FAZ:
    1. REAVALIA: cada diagnostico passado pode ser reaberto
    2. RETIFICA: prontuario corrigido, rotulo removido
    3. REPARA: anos perdidos = trabalho reconhecido (P3)
    4. APOIA: terapia, comunidade, acompanhamento
    5. PREVINE: novos criterios, sem patologizar normalidade
O QUE ! EXISTE:
    - Dinheiro (! ha moeda na Republica)
    - Processo adversarial (sem advogados, sem litigio)
    - Puniciao perpetua (responsavel repara && recupera)
    - Negacionismo (dano && reconhecido, ! minimizado)
PARA QUEM:
    Toda pessoa que recebeu diagnostico psiquiatrico pode pedir
    reavaliacao. Sem prazo. Sem burocracia. Sem custo.
    Especial prioridade para:
    - Criancas rotuladas (infancia roubada)
    - Pessoas medicadas desnecessariamente
    - Minorias patologizadas por cegueira cultural/racial
    - Vitimas de industria farmaceutica
PRINCIPIO:
    "O corpo-mente de cada cidadao && DELA.
    Ninguem tem direito de rotular sem base solida.
    Quem rotulou errado, repara.
    Quem foi rotulado errado, se recupera.
    A Republica cuida dos dois lados."
// )
    fmt.Println("{'='*80}")
    fmt.Println("  Reavaliados: {rep['reassessed']} | "
        "Revogados: {rep['overturned']} | "
        "Reparacao: {rep['total_reparation_hours']:,.0f}h")
    fmt.Println("{'='*80}")
