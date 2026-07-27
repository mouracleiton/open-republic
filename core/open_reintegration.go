// OpenReintegration -- Infraestrutura Completa para Ex-Penitenciarios -- gerado de Portugol++
package openreintegration_infraestrutura_completa_para_ex_penitenciarios

import "fmt"

// !/usr/bin/env python3
//
OpenReintegration -- Infraestrutura Completa para Ex-Penitenciarios
=====================================================================
"Se a pessoa ! tem pra onde voltar, ela volta pro crime.
Se a pessoa ! tem o que comer, ela rouba de novo.
Se a pessoa ! tem oficio, ela ! tem opcao.
A Republica FORNECE TUDO. Para que ! precise errar."
O QUE ISTO FAZ:
1. INFRAESTRUTURA TOTAL: moradia, comida, trabalho, saude, ID
2. REVISAO HISTORICA DA PENA: prontuario limpo, passado apagado
3. SUPORTE CONTINUO: ! abandona apos a saida
4. PREVENCAO DE REINCIDENCIA: causa raiz addressada
A MATEMATICA:
Sistema atual: 70% reincidencia. Causa: abandono.
Republica: <20% estimado. Causa: infraestrutura garantida.
Custo de reincidencia: nova vitima + nova prisao + R$ 42k/ano
Custo de reintegration: moradia + OpenKit + trabalho = ZERO (direito)
PREVENIR && mais barato que punir. Sempre.
O QUE O EX-PENITENCIARIO RECEBE (DIA 1 APOS SAIDA):
- Moradia garantida (! rua, ! favela, ! criminogeno)
- Comida garantida (direito fundamental)
- OpenKit COMPLETO (Smartphone, ID, credito, ferramentas)
- Trabalho garantido (OpenLaborRelay + skill aprendida na prisao)
- Saude (fisica + mental + adicao se necessario)
- Comunidade de apoio (! sozinho)
- Prontuario LIMPO (passado ! acessivel)
- Mentor (pessoa que acompanha primeiro ano)
- Dinheiro: ZERO (economia da Republica, sem dinheiro)
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime, timedelta de datetime
// ============================================================================
// 1. ESTAGIOS DA REINTEGRACAO
// ============================================================================
type ReintegrationPhase int
const (
    // Estagios da reintegration do ex-penitenciario.
    PRE_RELEASE = "pre_liberacao"  // ainda dentro, preparando saida
    DAY_0 = "dia_0"  // dia da saida
    FIRST_WEEK = "primeira_semana"  // adaptacao
    FIRST_MONTH = "primeiro_mes"  // estabilizando
    FIRST_QUARTER = "primeiro_trimestre"  // consolidando
    FIRST_YEAR = "primeiro_ano"  // autonomia
    INTEGRATED = "integrado"  // completamente reintegrado
    RECIDIVED = "reincidiu"  // voltou a cometer crime (FALHA do sistema)
type SupportNeed int
const (
    // Necessidades do ex-penitenciario.
    HOUSING = "moradia"
    FOOD = "comida"
    EMPLOYMENT = "trabalho"
    HEALTHCARE = "saude"
    MENTAL_HEALTH = "saude_mental"
    ADDICTION_TREATMENT = "tratamento_adicao"
    EDUCATION = "educacao"
    LEGAL_ID = "identidade"
    FAMILY_CONTACT = "familia"
    COMMUNITY = "comunidade"
    MENTORING = "mentoria"
    FINANCIAL = "credito"
    TRANSPORT = "transporte"
    CLOTHING = "roupas"
    COMMUNICATION = "comunicacao"
type SupportStatus int
const (
    PENDING = "pendente"  // ainda ! providenciado
    PROVIDED = "fornecido"  // entregue/garantido
    ONGOING = "continuo"  // suporte que ! acaba (saude, mentoria)
    FAILED = "falhou"  // ! conseguiu fornecer (SISTEMA falhou)
// ============================================================================
// 2. PLANO DE REINTEGRACAO INDIVIDUAL
// ============================================================================
// decorador: @dataclass
type ReintegrationPlan struct {
    // Plano individual para cada ex-penitenciario.
    PRINCIPIO FUNDAMENTAL:
    A Republica ASSUME que se a pessoa voltar ao crime,
    && porque a Republica FALHOU em prover. Nao a pessoa.
    Cada plano && PERSONALIZADO mas a BASE && igual para todos.
    //
    plan_id: texto
    citizen_id: texto
    citizen_name: texto
    age: inteiro
    original_crime := "" // string
    years_served := 0.0 // float64
    skills_learned := field(default_factory=list) // [texto]
    treatment_needs := field(default_factory=list) // [texto]
    // Fase atual
    phase := ReintegrationPhase.PRE_RELEASE // ReintegrationPhase
    release_date := "" // string
    days_since_release := 0 // int64
    // Suporte
    needs := field(default_factory=dict) // {SupportNeed: SupportStatus}
    housing_location := "" // string
    assigned_mentor := "" // string
    assigned_mentor_id := "" // string
    community_group := "" // string
    work_assignment := "" // string
    // Historico
    check_ins := field(default_factory=list) // [Dict]
    milestones_achieved := field(default_factory=list) // [texto]
    flags := field(default_factory=list) // alertas (! infracoes) // [texto]
    // Reincidencia
    recidivated := false // bool
    recidivism_reason := ""  // se voltou, POR QUE? (culpa do sistema) // string
    func init_needs(self) {
        // Inicializa todas as necessidades como pendentes.
        for _, need := range SupportNeed {
            self.needs[need] = SupportStatus.PENDING
    // decorador: @property
    func all_needs_met(self) bool {
        return all(s in (SupportStatus.PROVIDED, SupportStatus.ONGOING)
                para s em self.needs.values()) {
    // decorador: @property
    func readiness_score(self) float64 {
        // Score 0-100 de prontidao para saida.
        provided = soma(1 para s em self.needs.values()
                    if s in (SupportStatus.PROVIDED, SupportStatus.ONGOING))
        total = len(self.needs)
        total > 0 ? retorne arredonde(provided / total * 100, 0) : 0
    // decorador: @property
    func can_release(self) bool {
        // So libera se TUDO estiver providenciado.
        return self.readiness_score >= 100 && self.phase == ReintegrationPhase.PRE_RELEASE
// ============================================================================
// 3. INFRAESTRUTURA FORNECIDA PELA REPUBLICA
// ============================================================================
type InfrastructureProvider struct {
    // Fornece TODA a infraestrutura que o ex-penitenciario precisa.
    NADA && opcional. TUDO && obrigatorio.
    Se um item ! pode ser fornecido, a liberacao && ADIADA.
    O sistema ! libera para a rua sem suporte.
    //
    func __init__(self) {
        self.housing_units: {texto: Dict} = {}
        self.mentors: {texto: Dict} = {}
        self.community_groups: [Dict] = []
        self.work_assignments: {texto: Dict} = {}
    funcao provide_housing(self, citizen_id: texto, location: texto = ""
                        ) -> {texto: qualquer}:
        // Moradia garantida.
        REGRAS:
        - ! && presidencia. ! && favela. ! && area criminogena.
        - && unidade habitacional da Republica (OpenCivilConstruction).
        - Proximo a trabalho && saude.
        - Se possivel, proximo a familia.
        //
        unit_id = "HOUSE-{citizen_id[:6]}"
        assigned_location = location  ||  "Comunidade de Reintegracao Centro"
        self.housing_units[unit_id] = {
            "citizen_id": citizen_id,
            "location": assigned_location,
            "type": "unidade_individual",
            "furnished": true,
            "rent": "ZERO (direito)",
        }
        return {
            "provided": true,
            "unit_id": unit_id,
            "location": assigned_location,
            "type": "unidade individual mobiliada",
            "rent": "ZERO -- moradia && direito",
            "note": "Nao && rua. Nao && area criminogena. E civilidade.",
        }
    func provide_openkit(self, citizen_id: texto) {texto: qualquer} {
        // OpenKit completo (mesmo de todo cidadao + extras).
        return {
            "provided": true,
            "items": [
                "Smartphone (OpenSIMCARD com conectividade)",
                "ID Nacional (NOVO -- sem passado)",
                "Carteira de vacinacao (OpenVacine)",
                "Manual da Republica (constituicao + direitos)",
                "Credito inicial (15 -- piso da assembleia)",
                "Sementes agricolas (auto-suficiencia)",
                "Kit ferramentas (OpenProduct all-in-one)",
                "Painel solar portatil (energia)",
                "Filtro de agua",
                "Roupas basicas (4 pecas)",
            ],
            "cost": "ZERO -- kit de cidadania",
            "note": "Mesmo kit de todo cidadao. Sem marcacao de ex-presidiario.",
        }
    funcao provide_employment(self, citizen_id: texto,
                        skills: [texto]) -> {texto: qualquer}:
        // Trabalho garantido usando skills aprendidas na prisao.
        // Mapear skills para trabalhos
        skill_to_job = {
            "agricultura_urbana": "Horta Comunitaria Central",
            "construcao_civil": "OpenCivilConstruction (obra comunitaria)",
            "programacao_rust": "OpenSoftware (desenvolvimento)",
            "marcenaria": "FabLab Central (fabricacao)",
            "culinaria": "Restaurante Comunitario",
            "manutencao": "Manutencao de OpenTerminal (infraestrutura)",
            "programacao_basica": "OpenLaborRelay (micro-tarefas)",
            "design_fablab": "OpenProduct (design all-in-one)",
            "arte_terapia": "OpenTradition (preservacao cultural)",
            "letramento_digital": "OpenTerminal (suporte a cidadaos)",
            "cooperacao_comunitaria": "OpenDemocracy (mediador comunitario)",
        }
        assigned_job = "OpenLaborRelay (tarefas gerais)"
        for _, skill := range skills {
            if skill in skill_to_job {
                assigned_job = skill_to_job[skill]
                break
        self.work_assignments[citizen_id] = {
            "job": assigned_job,
            "hours_per_week": 20,
            "credit_per_cycle": 15,
            "mentor_work": true,
        }
        return {
            "provided": true,
            "job": assigned_job,
            "hours": "20h/semana (base 1.0)",
            "credit": "15/ciclo (piso da assembleia)",
            "note": "Trabalho baseado em skills aprendidas: {', '.join(skills[:3])}",
        }
    funcao assign_mentor(self, citizen_id: texto, citizen_name: texto,
                    mentor_name: texto, mentor_id: texto) -> {texto: qualquer}:
        // Mentor acompanha primeiro ano.
        O mentor ! && guarda. ! && policial. ! && oficial.
        && um cidadao voluntario que JA passou por reintegration
        (|| alguem treinado em acolhimento).
        //
        self.mentors[citizen_id] = {
            "mentor_name": mentor_name,
            "mentor_id": mentor_id,
            "role": "APOIO, ! vigilancia",
            "commitment": "1 ano minimo",
            "check_ins": "semanal no primeiro mes, mensal depois",
        }
        return {
            "assigned": true,
            "mentor": mentor_name,
            "role": "Apoio, acolhimento, navegacao da Republica",
            "not": "NAO && policial. NAO && oficial. NAO && vigilancia.",
            "commitment": "1 ano minimo",
        }
    funcao assign_community(self, citizen_id: texto,
                        group_name := "") -> {texto: qualquer}: // string
        // Comunidade de apoio -- grupo de ex-reintegrados + voluntarios.
        group = group_name  ||  "Comunidade de Apoio Mutuo"
        if !  any(g["name"] == group para g em self.community_groups) {
            self.community_groups.append({
                "name": group,
                "members": [],
                "meetings": "semanal",
            })
        for _, g := range self.community_groups {
            if g["name"] == group {
                g["members"].append(citizen_id)
        return {
            "assigned": true,
            "group": group,
            "meetings": "semanal",
            "purpose": "apoio mutuo, NAO isolamento",
        }
    funcao provide_healthcare(self, citizen_id: texto,
                        needs_treatment := nil) -> {texto: qualquer}: // [texto]
        // Saude fisica + mental + tratamento de adicao.
        services = {
            "fisica": "OpenHealth (nivel Sirio-Libanes para todos)",
            "mental": "OpenPsychology (sem patologizar, sem rotular)",
            "adicao": "Programa de recuperacao (se aplicavel)",
            "medicacao": "Desmame supervisionado se medicado na prisao",
        }
        if needs_treatment {
            if "tratamento_dependencia_quimica" in needs_treatment {
                services["adicao_program"] = "12 meses de tratamento intensivo"
            if "tratamento_saude_mental" in needs_treatment {
                services["mental_program"] = "Terapia semanal + grupo de apoio"
        return {
            "provided": true,
            "services": services,
            "level": "Sirio-Libanes (padrao unico P1)",
            "note": "Saude && direito. Tratamento ! && punicao.",
        }
// ============================================================================
// 4. REVISAO HISTORICA DA PENA
// ============================================================================
type RecordExpungement struct {
    // Revisao historica da pena -- prontuario limpo.
    PRINCIPIO:
    Quem cumpriu transformacao na Republica tem DIREITO ao esquecimento.
    O passado penal ! && acessivel. ! aparece em consulta.
    ! aparece em emprego. ! aparece em moradia.
    EXCECAO (so):
    - Crimes hediondos: restricao permanente (OpenPenalRevision)
    - Esses ! sao "ex-penitenciarios" -- sao "restritos permanentes"
    PARA OS DEMAIS:
    - Prontuario LIMPO
    - Antecedentes: ZERO
    - Histórico: "cidadao" (sem marcador)
    - OpenHistory: ! registra como "crime" -- registra como "transformacao"
    //
    func __init__(self) {
        self.expunged: {texto: Dict} = {}
        self.not_eligible: set = set() // hediondos
    funcao check_eligibility(self, citizen_id: texto,
                        was_hediondous := false) -> {texto: qualquer}: // bool
        // Verifica se pode ter prontuario limpo.
        if was_hediondous {
            self.not_eligible.add(citizen_id)
            return {
                "citizen_id": citizen_id,
                "eligible": false,
                "reason": "Crime hediondo -- restricao permanente (OpenPenalRevision)",
                "record": "PERMANENTE -- ! pode ser limpo",
            }
        return {
            "citizen_id": citizen_id,
            "eligible": true,
            "reason": "Cumpriu transformacao. Prontuario limpo garantido.",
        }
    funcao expunge(self, citizen_id: texto, citizen_name: texto,
                original_crime: texto, years_served: flutuante,
                skills_learned: [texto]) -> {texto: qualquer}:
        // Limpa prontuario -- apaga passado penal.
        if citizen_id in self.not_eligible {
            return {"error": "NAO elegivel -- crime hediondo"}
        record = {
            "citizen_id": citizen_id,
            "citizen_name": citizen_name,
            "expungement_date": datetime.now().isoformat(),
            "original_crime": original_crime,
            "years_served": years_served,
            "skills_learned": skills_learned,
            "new_record": "CIDADAO -- sem antecedentes",
            "visible_to": "NINGUEM (nem governo, nem empregador)",
            "accessible_by": "So com mandado democratico (P4)",
            "historical_record": "OpenHistory registra como TRANSFORMACAO, ! crime",
        }
        self.expunged[citizen_id] = record
        return {
            "expunged": true,
            "citizen": citizen_name,
            "before": "Antecedente: {original_crime}",
            "after": "Antecedente: NENHUM -- cidadao",
            "visible": "Prontuario LIMPO. Ninguem ve o passado.",
            "employment_check": "Resultado: SEM antecedentes",
            "housing_check": "Resultado: SEM antecedentes",
            "credit_check": "Resultado: SEM antecedentes",
            "history": "OpenHistory: 'TRANSFORMACAO COMPLETA' (! 'crime')",
            "message": (
                "{citizen_name} agora && CIDADAO sem passado. "
                "Aprendeu {', '.join(skills_learned[:3])}. "
                "Cumpriu {years_served:.0f} anos de transformacao. "
                "O passado NAO define. O futuro SIM."
            ),
        }
    func verify_clean_record(self, citizen_id: texto) {texto: qualquer} {
        // Verifica prontuario (como empregador/moradia veria).
        if citizen_id in self.expunged {
            return {
                "citizen_id": citizen_id,
                "record": "LIMPO",
                "antecedents": "NENHUM",
                "status": "CIDADAO",
                "note": "Sem antecedentes. Pessoa comum da Republica.",
            }
        if citizen_id in self.not_eligible {
            return {
                "citizen_id": citizen_id,
                "record": "RESTRITO",
                "antecedents": "PERMANENTE",
                "status": "RESTRITO",
            }
        return {
            "citizen_id": citizen_id,
            "record": "SEM REGISTRO",
            "status": "CIDADAO",
        }
// ============================================================================
// 5. MOTOR DE REINTEGRACAO
// ============================================================================
type ReintegrationEngine struct {
    // Motor completo de reintegration.
    FLUXO:
    1. PRE-RELEASE (30 dias antes): preparar tudo
    2. DAY 0: liberar SO se 100% pronto
    3. FIRST WEEK: check-in diario
    4. FIRST MONTH: check-in semanal
    5. FIRST YEAR: mentor mensal
    6. INTEGRATED: autonomia total, prontuario limpo
    SE REINCIDIR:
    - ! && culpa da pessoa. && FALHA do sistema.
    - Analisar: o que faltou?
    - Corrigir processo para proximo.
    //
    func __init__(self) {
        self.infra = InfrastructureProvider()
        self.expungement = RecordExpungement()
        self.plans: {texto: ReintegrationPlan} = {}
        self.stats_total_reintegrated: inteiro = 0
        self.stats_total_recidivism: inteiro = 0
        self.stats_avg_days_to_integrate: flutuante = 0.0
    funcao create_plan(self, citizen_id: texto, citizen_name: texto, age: inteiro,
                    original_crime: texto, years_served: flutuante,
                    skills_learned: [texto],
                    treatment_needs := nil) -> ReintegrationPlan: // [texto]
        // Cria plano de reintegration.
        plan = ReintegrationPlan(
            plan_id = hashlib.md5(citizen_id.encode()).hexdigest()[:8],
            citizen_id = citizen_id,
            citizen_name = citizen_name,
            age = age,
            original_crime = original_crime,
            years_served = years_served,
            skills_learned = skills_learned,
            treatment_needs = treatment_needs || [],
        )
        plan.init_needs()
        self.plans[plan.plan_id] = plan
        return plan
    funcao prepare_release(self, plan_id: texto,
                        mentor_name := "Mentor Voluntario", // string
                        mentor_id := "M-001") -> {texto: qualquer}: // string
        // Prepara TODA a infraestrutura antes da liberacao (30 dias).
        plan = self.plans.get(plan_id)
        if ! plan {
            return {"error": "Plano ! encontrado"}
        results = {}
        // 1. Moradia
        housing = self.infra.provide_housing(plan.citizen_id)
        plan.housing_location = housing["location"]
        plan.needs[SupportNeed.HOUSING] = SupportStatus.PROVIDED
        results["housing"] = housing
        // 2. OpenKit
        kit = self.infra.provide_openkit(plan.citizen_id)
        plan.needs[SupportNeed.CLOTHING] = SupportStatus.PROVIDED
        plan.needs[SupportNeed.COMMUNICATION] = SupportStatus.PROVIDED
        plan.needs[SupportNeed.TRANSPORT] = SupportStatus.PROVIDED
        results["kit"] = kit
        // 3. Trabalho
        job = self.infra.provide_employment(plan.citizen_id, plan.skills_learned)
        plan.work_assignment = job["job"]
        plan.needs[SupportNeed.EMPLOYMENT] = SupportStatus.PROVIDED
        results["employment"] = job
        // 4. Mentoria
        mentor = self.infra.assign_mentor(plan.citizen_id, plan.citizen_name,
                                        mentor_name, mentor_id)
        plan.assigned_mentor = mentor_name
        plan.needs[SupportNeed.MENTORING] = SupportStatus.ONGOING
        results["mentor"] = mentor
        // 5. Comunidade
        community = self.infra.assign_community(plan.citizen_id)
        plan.community_group = community["group"]
        plan.needs[SupportNeed.COMMUNITY] = SupportStatus.ONGOING
        results["community"] = community
        // 6. Saude
        health = self.infra.provide_healthcare(plan.citizen_id, plan.treatment_needs)
        plan.needs[SupportNeed.HEALTHCARE] = SupportStatus.ONGOING
        if plan.treatment_needs {
            if "tratamento_dependencia_quimica" in plan.treatment_needs {
                plan.needs[SupportNeed.ADDICTION_TREATMENT] = SupportStatus.ONGOING
            if "tratamento_saude_mental" in plan.treatment_needs {
                plan.needs[SupportNeed.MENTAL_HEALTH] = SupportStatus.ONGOING
        results["health"] = health
        // 7. Comida (direito garantido sempre)
        plan.needs[SupportNeed.FOOD] = SupportStatus.PROVIDED
        results["food"] = {"status": "garantido (direito fundamental)"}
        // 8. Educacao (continua aprendendo skills)
        plan.needs[SupportNeed.EDUCATION] = SupportStatus.ONGOING
        results["education"] = {"status": "continua (OpenEducation + OpenTerminal)"}
        // 9. ID nova (sem passado)
        plan.needs[SupportNeed.LEGAL_ID] = SupportStatus.PROVIDED
        results["id"] = {"status": "ID Nacional NOVA (sem marcador penal)"}
        // 10. Credito inicial
        plan.needs[SupportNeed.FINANCIAL] = SupportStatus.PROVIDED
        results["credit"] = {"amount": 15, "source": "piso da assembleia"}
        // 11. Familia (reconexao se possivel)
        plan.needs[SupportNeed.FAMILY_CONTACT] = SupportStatus.PROVIDED
        return {
            "plan_id": plan_id,
            "citizen": plan.citizen_name,
            "readiness": "{plan.readiness_score:.0f}%",
            "all_ready": plan.all_needs_met,
            "can_release": plan.can_release,
            "details": results,
            "message": (
                "{'PRONTO PARA LIBERACAO' if plan.can_release else 'AINDA PREPARANDO'}. "
                "Readiness: {plan.readiness_score:.0f}%. "
                "Tudo garantido: moradia, trabalho, saude, mentor, comunidade."
            ),
        }
    func release(self, plan_id: texto) {texto: qualquer} {
        // Libera ex-penitenciario COM infraestrutura total.
        plan = self.plans.get(plan_id)
        if ! plan {
            return {"error": "Plano ! encontrado"}
        if ! plan.can_release {
            return {
                "error": "NAO PODE LIBERAR",
                "readiness": "{plan.readiness_score:.0f}%",
                "reason": "Infraestrutura incompleta. Republica NAO libera sem suporte.",
            }
        plan.phase = ReintegrationPhase.DAY_0
        plan.release_date = datetime.now().isoformat()
        plan.days_since_release = 0
        // Expungement (prontuario limpo)
        was_hediondous = "homicidio" in plan.original_crime.lower()  ||  \
                        "abuso" in plan.original_crime.lower()
        eligibility = self.expungement.check_eligibility(
            plan.citizen_id, was_hediondous)
        if eligibility["eligible"] {
            expungement = self.expungement.expunge(
                plan.citizen_id, plan.citizen_name,
                plan.original_crime, plan.years_served,
                plan.skills_learned)
        } else {
            expungement = eligibility
        return {
            "released": true,
            "citizen": plan.citizen_name,
            "phase": plan.phase.value,
            "infrastructure": "COMPLETA (moradia + trabalho + saude + mentor + comunidade)",
            "prontuario": expungement,
            "mentor": plan.assigned_mentor,
            "community": plan.community_group,
            "work": plan.work_assignment,
            "housing": plan.housing_location,
            "on_street": "NAO -- moradia garantida",
            "abandoned": "NAO -- suporte continuo garantido",
            "message": (
                "{plan.citizen_name} sai COM infraestrutura. "
                "Nao vai pra rua. Nao fica sozinho. "
                "Tem trabalho. Tem mentor. Tem comunidade. "
                "Tem prontuario limpo. E cidadao."
            ),
        }
    funcao check_in(self, plan_id: texto, status: texto = "bom",
                notes := "") -> {texto: qualquer}: // string
        // Check-in periodico do ex-penitenciario.
        plan = self.plans.get(plan_id)
        if ! plan {
            return {"error": "! encontrado"}
        plan.days_since_release += 7 // simular passagem de tempo
        plan.check_ins.append({
            "date": datetime.now().isoformat(),
            "days_since_release": plan.days_since_release,
            "status": status,
            "notes": notes,
        })
        // Progressao de fase
        if plan.days_since_release <= 1 {
            plan.phase = ReintegrationPhase.DAY_0
        } else if plan.days_since_release <= 7 {
            plan.phase = ReintegrationPhase.FIRST_WEEK
        } else if plan.days_since_release <= 30 {
            plan.phase = ReintegrationPhase.FIRST_MONTH
        } else if plan.days_since_release <= 90 {
            plan.phase = ReintegrationPhase.FIRST_QUARTER
        } else if plan.days_since_release <= 365 {
            plan.phase = ReintegrationPhase.FIRST_YEAR
            plan.milestones_achieved.append("sobreviveu_primeiro_ano")
        } else {
            plan.phase = ReintegrationPhase.INTEGRATED
            self.stats_total_reintegrated += 1
        return {
            "citizen": plan.citizen_name,
            "days_since_release": plan.days_since_release,
            "phase": plan.phase.value,
            "status": status,
            "mentor": plan.assigned_mentor,
            "work": plan.work_assignment,
        }
    func report_recidivism(self, plan_id: texto, reason: texto) {texto: qualquer} {
        // Se voltou a cometer crime -- FALHA do sistema.
        plan = self.plans.get(plan_id)
        if ! plan {
            return {"error": "! encontrado"}
        plan.recidivated = true
        plan.recidivism_reason = reason
        plan.phase = ReintegrationPhase.RECIDIVED
        self.stats_total_recidivism += 1
        // Analisar onde o sistema falhou
        failed_needs = [need.value para need, status in plan.needs.items()
                        if status = = SupportStatus.FAILED]
        return {
            "citizen": plan.citizen_name,
            "recidivated": true,
            "reason": reason,
            "system_failure": (
                "A Republica ASSUME a culpa. Algo faltou. "
                "Processo sera revisado. Nao && culpa da pessoa."
            ),
            "failed_supports": failed_needs  ||  ["analise_necessaria"],
            "action": (
                "Revisar processo de reintegration. "
                "Corrigir para o proximo. "
                "Reabrir plano de transformacao (OpenPenalRevision)."
            ),
        }
    func stats(self) {texto: qualquer} {
        reintegrated = soma(1 para p em self.plans.values()
                        if p.phase in (ReintegrationPhase.FIRST_YEAR,
                                        ReintegrationPhase.INTEGRATED)
                            && ! p.recidivated)
        recidivated = soma(1 para p em self.plans.values() if p.recidivated)
        in_progress = soma(1 para p em self.plans.values()
                        if p.phase ! in (ReintegrationPhase.INTEGRATED,
                                            ReintegrationPhase.RECIDIVED)
                        && ! p.recidivated)
        total_outcome = len(self.plans)
        rate = total_outcome > 0 ? (recidivated / total_outcome * 100) : 0
        return {
            "total_plans": len(self.plans),
            "in_progress": in_progress,
            "fully_reintegrated": reintegrated,
            "recidivated": recidivated,
            "recidivism_rate": "{rate:.0f}%",
            "comparison_current_system": "70% (Brasil atual)",
            "expunged_records": len(self.expungement.expunged),
            "housing_provided": len(self.infra.housing_units),
            "mentors_active": len(self.infra.mentors),
            "community_groups": len(self.infra.community_groups),
        }
// ============================================================================
// 6. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = ReintegrationEngine()
    fmt.Println("=" * 80)
    fmt.Println("  OPENREINTEGRATION")
    fmt.Println("  Infraestrutura Completa para Ex-Penitenciarios")
    fmt.Println("  'Para que ! precisem cometer erros.'")
    fmt.Println("=" * 80)
    // === CASOS DE EX-PENITENCIARIOS ===
    cases = [
        ("P-005", "Pedro Costa", 25, "Furto R$ 500 em ferramentas",
        1.0, ["construcao_civil", "agricultura_urbana", "letramento_digital"]),
        ("P-009", "Marcos Vieira", 40, "Roubo a mao armada (simulacro)",
        2.0, ["marcenaria", "culinaria"], ["tratamento_dependencia_quimica"]),
        ("P-010", "Lucas Martins", 22, "Trafico (soldo, ! chefe)",
        3.0, ["cooperacao_comunitaria", "construcao_civil", "agricultura_urbana"],
        []),
        ("P-007", "Roberto Alves", 35, "Agressao fisica sem ferimentos graves",
        0.5, ["arte_terapia", "culinaria"], ["tratamento_saude_mental"]),
    ]
    // === 1. CRIAR PLANOS ===
    fmt.Println("\n\n  === 1. PLANOS DE REINTEGRACAO ===\n")
    para cid, name, age, crime, served, skills, *treatments in cases: {
        treatment = treatments ? treatments[0] : []
        plan = engine.create_plan(cid, name, age, crime, served, skills, treatment)
        fmt.Println("  [{plan.plan_id}] {name} ({age} anos)")
        fmt.Println("    Crime original: {crime}")
        fmt.Println("    Tempo cumprido: {served:.1f} anos")
        fmt.Println("    Skills: {', '.join(skills[:3])}")
        if treatment {
            fmt.Println("    Tratamento: {', '.join(treatment)}")
        fmt.Println("    Readiness inicial: {plan.readiness_score:.0f}%")
    // === 2. PREPARAR LIBERACAO (30 dias antes) ===
    fmt.Println("\n\n  === 2. PREPARANDO INFRAESTRUTURA (30 dias antes) ===\n")
    para cid, name, *_ in cases: {
        plans = [p para p em engine.plans.values() if p.citizen_id == cid]
        if plans {
            prep = engine.prepare_release(plans[0].plan_id)
            fmt.Println("\n  [{prep['citizen']}] Readiness: {prep['readiness']}")
            fmt.Println("    Moradia: {prep['details']['housing']['location']}")
            fmt.Println("    Trabalho: {prep['details']['employment']['job']}")
            fmt.Println("    Mentor: {prep['details']['mentor']['mentor']}")
            fmt.Println("    Comunidade: {prep['details']['community']['group']}")
            fmt.Println("    Saude: {prep['details']['health']['level']}")
            fmt.Println("    OpenKit: {prep['details']['kit']['cost']}")
            fmt.Println("    Pode liberar: {'SIM' if prep['can_release'] else 'NAO'}")
    // === 3. LIBERACAO ===
    fmt.Println("\n\n  === 3. LIBERACAO COM INFRAESTRUTURA ===\n")
    para cid, name, *_ in cases: {
        plans = [p para p em engine.plans.values() if p.citizen_id == cid]
        if plans {
            release = engine.release(plans[0].plan_id)
            fmt.Println("\n  [{release.get('citizen', name)}]")
            if release.get("released") {
                fmt.Println("    LIBERADO com infraestrutura completa")
                fmt.Println("    Na rua: NAO -- {release['housing']}")
                fmt.Println("    Abandonado: NAO -- mentor + comunidade")
                fmt.Println("    Trabalho: {release['work']}")
                ex = release.get("prontuario", {})
                if ex.get("expunged") {
                    fmt.Println("    Prontuario: {ex['after']}")
                    fmt.Println("    Visivel a: {ex['visible']}")
            } else {
                fmt.Println("    {release.get('error', 'ERRO')}")
    // === 4. CHECK-INS (simular passagem de tempo) ===
    fmt.Println("\n\n  === 4. CHECK-INS PERIODICOS ===\n")
    para cid, name, *_ in cases: {
        plans = [p para p em engine.plans.values() if p.citizen_id == cid]
        if plans {
            // Simular 4 check-ins (4 semanas)
            for _, _ := range intervalo(4) {
                ci = engine.check_in(plans[0].plan_id, "bom", "")
            fmt.Println("  {name}: {ci['days_since_release']} dias -> {ci['phase']}")
    // === 5. VERIFICAR PRONTUARIO LIMPO ===
    fmt.Println("\n\n  === 5. VERIFICACAO DE PRONTUARIO (como empregador veria) ===\n")
    para cid, name, *_ in cases: {
        check = engine.expungement.verify_clean_record(cid)
        fmt.Println("  {name:<20} -> {check['record']} ({check['status']})")
    // === 6. CASO DE REINCIDENCIA (FALHA DO SISTEMA) ===
    fmt.Println("\n\n  === 6. REINCIDENCIA = FALHA DO SISTEMA ===\n")
    plans_list = list(engine.plans.values())
    if plans_list {
        rec = engine.report_recidivism(
            plans_list[1].plan_id, // Marcos
            "Recaiu em alcool + moradia distante do tratamento")
        fmt.Println("  {rec['citizen']} reincidiu.")
        fmt.Println("  Motivo: {rec['reason']}")
        fmt.Println("  {rec['system_failure']}")
        fmt.Println("  Suportes que falharam: {rec['failed_supports']}")
        fmt.Println("  Acao: {rec['action']}")
    // === 7. COMPARACAO ===
    fmt.Println("\n\n  === 7. COMPARACAO: SISTEMA ATUAL vs REPUBLICA ===\n")
    s = engine.stats()
    fmt.Println("  {'Metrica':<30} {'Sistema Atual':>15} {'Republica':>15}")
    fmt.Println("  {'-'*62}")
    fmt.Println("  {'Reincidencia':<30} {'70%':>14} {s['recidivism_rate']:>14}")
    fmt.Println("  {'Moradia ao sair':<30} {'Rua/favela':>15} {'Garantida':>15}")
    fmt.Println("  {'Trabalho ao sair':<30} {'Nenhum':>15} {'Garantido':>15}")
    fmt.Println("  {'Mentor':<30} {'Nenhum':>15} {'1 ano':>15}")
    fmt.Println("  {'Saude':<30} {'SUS fila':>15} {'Sirio-Lib.':>15}")
    fmt.Println("  {'Prontuario':<30} {'Marcado':>15} {'LIMPO':>15}")
    fmt.Println("  {'Comunidade':<30} {'Isolado':>15} {'Apoio mutuo':>15}")
    fmt.Println("  {'Custo':<30} {'R$ 42k/ano':>15} {'ZERO':>15}")
    // === FILOSOFIA ===
    fmt.Println("\n\n{'='*80}")
    fmt.Println("  FILOSOFIA DA REINTEGRACAO")
    fmt.Println("{'='*80}")
    fmt.Println("""
A REPUBLICA ASSUME A CULPA:
    Se alguem volta a cometer crime apos reintegration,
    a Republica ASSUME que falhou. Nao a pessoa.
    O sistema atual libera para a RUA:
    - Sem moradia -> vai pra favela criminogena
    - Sem trabalho -> precisa roubar pra comer
    - Sem tratamento -> recai em drogas
    - Sem comunidade -> se isola -> volta pro crime
    - Com prontuario marcado -> ningem contrata -> sem opcao
    A Republica libera COM INFRAESTRUTURA:
    - Moradia -> ! vai pra rua
    - Trabalho -> ! precisa roubar
    - Tratamento -> ! recai em drogas
    - Comunidade -> ! se isola
    - Prontuario LIMPO -> && cidadao igual aos outros
O QUE FORNECE (DIA 1):
    1. MORADIA: unidade da Republica (! rua, ! criminogeno)
    2. COMIDA: direito garantido (OpenCredit)
    3. TRABALHO: baseado em skills aprendidas (OpenLaborRelay)
    4. SAUDE: nivel Sirio-Libanes (OpenHealthcareAccess)
    5. OpenKit COMPLETO: smartphone, ID, credito, ferramentas
    6. MENTOR: cidadao voluntario (1 ano)
    7. COMUNIDADE: grupo de apoio mutuo
    8. PRONTUARIO LIMPO: passado apagado
    9. EDUCACAO: continua (OpenTerminal + OpenEducation)
    10. CREDITO: piso da assembleia (15/ciclo)
REVISAO HISTORICA DA PENA:
    OpenHistory registra como "TRANSFORMACAO", ! "crime".
    Prontuario: LIMPO (ninguem ve o passado).
    Antecedentes: ZERO (resultado de consulta = cidadao).
    Excecao: crimes hediondos (restricao permanente).
PREVENCAO > PUNICAO:
    Prevenir custa ZERO (direito, ! compra).
    Punir custa R$ 42k/ano + nova vitima + reincidencia.
    A Republica escolhe prevenir. Sempre.
PRINCIPIOS:
    P1: Ex-penitenciario && cidadao igual. Sem marcador. Sem elitismo.
    P2: Seu corpo && vida sao soberanos. Apenas com suporte.
    P3: Trabalho garantido. Base 1.0 como todos.
    P4: Reincidencia && falha do SISTEMA, ! da pessoa.
// )
    fmt.Println("{'='*80}")
    fmt.Println("  OpenReintegration: {s['total_plans']} planos, "
        "{s['fully_reintegrated']} integrados, "
        "{s['expunged_records']} prontuarios limpos.")
    fmt.Println("  Reincidencia: {s['recidivism_rate']} (vs 70% atual).")
    fmt.Println("  Prevenir > Punir. Sempre.")
    fmt.Println("{'='*80}")
