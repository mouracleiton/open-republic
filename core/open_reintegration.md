# OpenReintegration -- Infraestrutura Completa para Ex-Penitenciarios

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_reintegration.py`

**Descricao:** =====================================================================
"Se a pessoa nao tem pra onde voltar, ela volta pro crime.
 Se a pessoa nao tem o que comer, ela rouba de novo.
 Se a pessoa nao tem oficio, ela nao tem opcao.
 A Republica FORNECE TUDO. Para que nao precise errar."
O QUE ISTO FAZ:
  1. INFRAESTRUTURA TOTAL: moradia, comida, trabalho, saude, ID
  2. REVISAO HISTORICA DA PENA: prontuario limpo, passado apagado
  3. SUPORTE CONTINUO: nao abandona apos a saida
  4. PREVENCAO DE REINCIDENCIA: causa raiz addressada
A MATEMATICA:
  Sistema atual: 70% reincidencia. Causa: abandono.
  Republica: <20% estimado. Causa: infraestrutura garantida.
  Custo de reincidencia: nova vitima + nova prisao + R$ 42k/ano
  Custo de reintegration: moradia + OpenKit + trabalho = ZERO (direito)
  PREVENIR e mais barato que punir. Sempre.
O QUE O EX-PENITENCIARIO RECEBE (DIA 1 APOS SAIDA):
  - Moradia garantida (nao rua, nao favela, nao criminogeno)
  - Comida garantida (direito fundamental)
  - OpenKit COMPLETO (Smartphone, ID, credito, ferramentas)
  - Trabalho garantido (OpenLaborRelay + skill aprendida na prisao)
  - Saude (fisica + mental + adicao se necessario)
  - Comunidade de apoio (NAO sozinho)
  - Prontuario LIMPO (passado nao acessivel)
  - Mentor (pessoa que acompanha primeiro ano)
  - Dinheiro: ZERO (economia da Republica, sem dinheiro)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenReintegration -- Infraestrutura Completa para Ex-Penitenciarios
=====================================================================

"Se a pessoa nao tem pra onde voltar, ela volta pro crime.
 Se a pessoa nao tem o que comer, ela rouba de novo.
 Se a pessoa nao tem oficio, ela nao tem opcao.
 A Republica FORNECE TUDO. Para que nao precise errar."

O QUE ISTO FAZ:
  1. INFRAESTRUTURA TOTAL: moradia, comida, trabalho, saude, ID
  2. REVISAO HISTORICA DA PENA: prontuario limpo, passado apagado
  3. SUPORTE CONTINUO: nao abandona apos a saida
  4. PREVENCAO DE REINCIDENCIA: causa raiz addressada

A MATEMATICA:
  Sistema atual: 70% reincidencia. Causa: abandono.
  Republica: <20% estimado. Causa: infraestrutura garantida.

  Custo de reincidencia: nova vitima + nova prisao + R$ 42k/ano
  Custo de reintegration: moradia + OpenKit + trabalho = ZERO (direito)

  PREVENIR e mais barato que punir. Sempre.

O QUE O EX-PENITENCIARIO RECEBE (DIA 1 APOS SAIDA):
  - Moradia garantida (nao rua, nao favela, nao criminogeno)
  - Comida garantida (direito fundamental)
  - OpenKit COMPLETO (Smartphone, ID, credito, ferramentas)
  - Trabalho garantido (OpenLaborRelay + skill aprendida na prisao)
  - Saude (fisica + mental + adicao se necessario)
  - Comunidade de apoio (nao sozinho)
  - Prontuario LIMPO (passado nao acessivel)
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

classe ReintegrationPhase herda de Enum:
    // Estagios da reintegration do ex-penitenciario.
    PRE_RELEASE = "pre_liberacao"  // ainda dentro, preparando saida
    DAY_0 = "dia_0"  // dia da saida
    FIRST_WEEK = "primeira_semana"  // adaptacao
    FIRST_MONTH = "primeiro_mes"  // estabilizando
    FIRST_QUARTER = "primeiro_trimestre"  // consolidando
    FIRST_YEAR = "primeiro_ano"  // autonomia
    INTEGRATED = "integrado"  // completamente reintegrado
    RECIDIVED = "reincidiu"  // voltou a cometer crime (FALHA do sistema)


classe SupportNeed herda de Enum:
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


classe SupportStatus herda de Enum:
    PENDING = "pendente"  // ainda nao providenciado
    PROVIDED = "fornecido"  // entregue/garantido
    ONGOING = "continuo"  // suporte que nao acaba (saude, mentoria)
    FAILED = "falhou"  // nao conseguiu fornecer (SISTEMA falhou)


// ============================================================================
// 2. PLANO DE REINTEGRACAO INDIVIDUAL
// ============================================================================

// decorador: @dataclass
classe ReintegrationPlan:
    // Plano individual para cada ex-penitenciario.

    PRINCIPIO FUNDAMENTAL:
    A Republica ASSUME que se a pessoa voltar ao crime,
    e porque a Republica FALHOU em prover. Nao a pessoa.

    Cada plano e PERSONALIZADO mas a BASE e igual para todos.
    // 
    plan_id: texto
    citizen_id: texto
    citizen_name: texto
    age: inteiro
    seja original_crime: texto = ""
    seja years_served: flutuante = 0.0
    seja skills_learned: [texto] = field(default_factory=list)
    seja treatment_needs: [texto] = field(default_factory=list)

    // Fase atual
    seja phase: ReintegrationPhase = ReintegrationPhase.PRE_RELEASE
    seja release_date: texto = ""
    seja days_since_release: inteiro = 0

    // Suporte
    seja needs: {SupportNeed: SupportStatus} = field(default_factory=dict)
    seja housing_location: texto = ""
    seja assigned_mentor: texto = ""
    seja assigned_mentor_id: texto = ""
    seja community_group: texto = ""
    seja work_assignment: texto = ""

    // Historico
    seja check_ins: [Dict] = field(default_factory=list)
    seja milestones_achieved: [texto] = field(default_factory=list)
    seja flags: [texto] = field(default_factory=list) // alertas (nao infracoes)

    // Reincidencia
    seja recidivated: logico = falso
    seja recidivism_reason: texto = ""  // se voltou, POR QUE? (culpa do sistema)

    funcao init_needs(self):
        // Inicializa todas as necessidades como pendentes.
        para cada need em SupportNeed:
            self.needs[need] = SupportStatus.PENDING

    // decorador: @property
    funcao all_needs_met(self) -> logico:
        retorne all(s in (SupportStatus.PROVIDED, SupportStatus.ONGOING)
                   para s em self.needs.values())

    // decorador: @property
    funcao readiness_score(self) -> flutuante:
        // Score 0-100 de prontidao para saida.
        provided = soma(1 para s em self.needs.values()
                       if s in (SupportStatus.PROVIDED, SupportStatus.ONGOING))
        total = tamanho(self.needs)
        total > 0 ? retorne arredonde(provided / total * 100, 0) : 0

    // decorador: @property
    funcao can_release(self) -> logico:
        // So libera se TUDO estiver providenciado.
        retorne self.readiness_score >= 100 e self.phase == ReintegrationPhase.PRE_RELEASE


// ============================================================================
// 3. INFRAESTRUTURA FORNECIDA PELA REPUBLICA
// ============================================================================

classe InfrastructureProvider:
    // Fornece TODA a infraestrutura que o ex-penitenciario precisa.

    NADA e opcional. TUDO e obrigatorio.
    Se um item nao pode ser fornecido, a liberacao e ADIADA.
    O sistema nao libera para a rua sem suporte.
    // 

    funcao __init__(self):
        self.housing_units: {texto: Dict} = {}
        self.mentors: {texto: Dict} = {}
        self.community_groups: [Dict] = []
        self.work_assignments: {texto: Dict} = {}

    funcao provide_housing(self, citizen_id: texto, location: texto = ""
                        ) -> {texto: qualquer}:
        // Moradia garantida.

        REGRAS:
        - nao e presidencia. nao e favela. nao e area criminogena.
        - e unidade habitacional da Republica (OpenCivilConstruction).
        - Proximo a trabalho e saude.
        - Se possivel, proximo a familia.
        // 
        unit_id = "HOUSE-{citizen_id[:6]}"
        assigned_location = location  ou  "Comunidade de Reintegracao Centro"
        self.housing_units[unit_id] = {
            "citizen_id": citizen_id,
            "location": assigned_location,
            "type": "unidade_individual",
            "furnished": verdadeiro,
            "rent": "ZERO (direito)",
        }
        retorne {
            "provided": verdadeiro,
            "unit_id": unit_id,
            "location": assigned_location,
            "type": "unidade individual mobiliada",
            "rent": "ZERO -- moradia e direito",
            "note": "Nao e rua. Nao e area criminogena. E civilidade.",
        }

    funcao provide_openkit(self, citizen_id: texto) -> {texto: qualquer}:
        // OpenKit completo (mesmo de todo cidadao + extras).
        retorne {
            "provided": verdadeiro,
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
        para cada skill em skills:
            se skill in skill_to_job entao:
                assigned_job = skill_to_job[skill]
                interrompa

        self.work_assignments[citizen_id] = {
            "job": assigned_job,
            "hours_per_week": 20,
            "credit_per_cycle": 15,
            "mentor_work": verdadeiro,
        }

        retorne {
            "provided": verdadeiro,
            "job": assigned_job,
            "hours": "20h/semana (base 1.0)",
            "credit": "15/ciclo (piso da assembleia)",
            "note": "Trabalho baseado em skills aprendidas: {', '.join(skills[:3])}",
        }

    funcao assign_mentor(self, citizen_id: texto, citizen_name: texto,
                      mentor_name: texto, mentor_id: texto) -> {texto: qualquer}:
        // Mentor acompanha primeiro ano.

        O mentor nao e guarda. nao e policial. nao e oficial.
        e um cidadao voluntario que JA passou por reintegration
        (ou alguem treinado em acolhimento).
        // 
        self.mentors[citizen_id] = {
            "mentor_name": mentor_name,
            "mentor_id": mentor_id,
            "role": "APOIO, nao vigilancia",
            "commitment": "1 ano minimo",
            "check_ins": "semanal no primeiro mes, mensal depois",
        }
        retorne {
            "assigned": verdadeiro,
            "mentor": mentor_name,
            "role": "Apoio, acolhimento, navegacao da Republica",
            "not": "NAO e policial. NAO e oficial. NAO e vigilancia.",
            "commitment": "1 ano minimo",
        }

    funcao assign_community(self, citizen_id: texto,
                         seja group_name: texto = "") -> {texto: qualquer}:
        // Comunidade de apoio -- grupo de ex-reintegrados + voluntarios.
        group = group_name  ou  "Comunidade de Apoio Mutuo"
        se nao  any(g["name"] == group para g em self.community_groups) entao:
            self.community_groups.append({
                "name": group,
                "members": [],
                "meetings": "semanal",
            })
        para cada g em self.community_groups:
            se g["name"] == group entao:
                g["members"].append(citizen_id)
        retorne {
            "assigned": verdadeiro,
            "group": group,
            "meetings": "semanal",
            "purpose": "apoio mutuo, NAO isolamento",
        }

    funcao provide_healthcare(self, citizen_id: texto,
                           seja needs_treatment: [texto] = nulo) -> {texto: qualquer}:
        // Saude fisica + mental + tratamento de adicao.
        services = {
            "fisica": "OpenHealth (nivel Sirio-Libanes para todos)",
            "mental": "OpenPsychology (sem patologizar, sem rotular)",
            "adicao": "Programa de recuperacao (se aplicavel)",
            "medicacao": "Desmame supervisionado se medicado na prisao",
        }
        se needs_treatment entao:
            se "tratamento_dependencia_quimica" in needs_treatment entao:
                services["adicao_program"] = "12 meses de tratamento intensivo"
            se "tratamento_saude_mental" in needs_treatment entao:
                services["mental_program"] = "Terapia semanal + grupo de apoio"

        retorne {
            "provided": verdadeiro,
            "services": services,
            "level": "Sirio-Libanes (padrao unico P1)",
            "note": "Saude e direito. Tratamento nao e punicao.",
        }


// ============================================================================
// 4. REVISAO HISTORICA DA PENA
// ============================================================================

classe RecordExpungement:
    // Revisao historica da pena -- prontuario limpo.

    PRINCIPIO:
    Quem cumpriu transformacao na Republica tem DIREITO ao esquecimento.
    O passado penal nao e acessivel. nao aparece em consulta.
    nao aparece em emprego. nao aparece em moradia.

    EXCECAO (so):
    - Crimes hediondos: restricao permanente (OpenPenalRevision)
    - Esses nao sao "ex-penitenciarios" -- sao "restritos permanentes"

    PARA OS DEMAIS:
    - Prontuario LIMPO
    - Antecedentes: ZERO
    - Histórico: "cidadao" (sem marcador)
    - OpenHistory: nao registra como "crime" -- registra como "transformacao"
    // 

    funcao __init__(self):
        self.expunged: {texto: Dict} = {}
        self.not_eligible: set = set() // hediondos

    funcao check_eligibility(self, citizen_id: texto,
                          seja was_hediondous: logico = falso) -> {texto: qualquer}:
        // Verifica se pode ter prontuario limpo.
        se was_hediondous entao:
            self.not_eligible.add(citizen_id)
            retorne {
                "citizen_id": citizen_id,
                "eligible": falso,
                "reason": "Crime hediondo -- restricao permanente (OpenPenalRevision)",
                "record": "PERMANENTE -- nao pode ser limpo",
            }

        retorne {
            "citizen_id": citizen_id,
            "eligible": verdadeiro,
            "reason": "Cumpriu transformacao. Prontuario limpo garantido.",
        }

    funcao expunge(self, citizen_id: texto, citizen_name: texto,
                original_crime: texto, years_served: flutuante,
                skills_learned: [texto]) -> {texto: qualquer}:
        // Limpa prontuario -- apaga passado penal.
        se citizen_id in self.not_eligible entao:
            retorne {"error": "NAO elegivel -- crime hediondo"}

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
            "historical_record": "OpenHistory registra como TRANSFORMACAO, nao crime",
        }

        self.expunged[citizen_id] = record

        retorne {
            "expunged": verdadeiro,
            "citizen": citizen_name,
            "before": "Antecedente: {original_crime}",
            "after": "Antecedente: NENHUM -- cidadao",
            "visible": "Prontuario LIMPO. Ninguem ve o passado.",
            "employment_check": "Resultado: SEM antecedentes",
            "housing_check": "Resultado: SEM antecedentes",
            "credit_check": "Resultado: SEM antecedentes",
            "history": "OpenHistory: 'TRANSFORMACAO COMPLETA' (nao 'crime')",
            "message": (
                "{citizen_name} agora e CIDADAO sem passado. "
                "Aprendeu {', '.join(skills_learned[:3])}. "
                "Cumpriu {years_served:.0f} anos de transformacao. "
                "O passado NAO define. O futuro SIM."
            ),
        }

    funcao verify_clean_record(self, citizen_id: texto) -> {texto: qualquer}:
        // Verifica prontuario (como empregador/moradia veria).
        se citizen_id in self.expunged entao:
            retorne {
                "citizen_id": citizen_id,
                "record": "LIMPO",
                "antecedents": "NENHUM",
                "status": "CIDADAO",
                "note": "Sem antecedentes. Pessoa comum da Republica.",
            }
        se citizen_id in self.not_eligible entao:
            retorne {
                "citizen_id": citizen_id,
                "record": "RESTRITO",
                "antecedents": "PERMANENTE",
                "status": "RESTRITO",
            }
        retorne {
            "citizen_id": citizen_id,
            "record": "SEM REGISTRO",
            "status": "CIDADAO",
        }


// ============================================================================
// 5. MOTOR DE REINTEGRACAO
// ============================================================================

classe ReintegrationEngine:
    // Motor completo de reintegration.

    FLUXO:
    1. PRE-RELEASE (30 dias antes): preparar tudo
    2. DAY 0: liberar SO se 100% pronto
    3. FIRST WEEK: check-in diario
    4. FIRST MONTH: check-in semanal
    5. FIRST YEAR: mentor mensal
    6. INTEGRATED: autonomia total, prontuario limpo

    SE REINCIDIR:
    - nao e culpa da pessoa. e FALHA do sistema.
    - Analisar: o que faltou?
    - Corrigir processo para proximo.
    // 

    funcao __init__(self):
        self.infra = InfrastructureProvider()
        self.expungement = RecordExpungement()
        self.plans: {texto: ReintegrationPlan} = {}
        self.stats_total_reintegrated: inteiro = 0
        self.stats_total_recidivism: inteiro = 0
        self.stats_avg_days_to_integrate: flutuante = 0.0

    funcao create_plan(self, citizen_id: texto, citizen_name: texto, age: inteiro,
                    original_crime: texto, years_served: flutuante,
                    skills_learned: [texto],
                    seja treatment_needs: [texto] = nulo) -> ReintegrationPlan:
        // Cria plano de reintegration.
        plan = ReintegrationPlan(
            plan_id = hashlib.md5(citizen_id.encode()).hexdigest()[:8],
            citizen_id = citizen_id,
            citizen_name = citizen_name,
            age = age,
            original_crime = original_crime,
            years_served = years_served,
            skills_learned = skills_learned,
            treatment_needs = treatment_needs ou [],
        )
        plan.init_needs()
        self.plans[plan.plan_id] = plan
        retorne plan

    funcao prepare_release(self, plan_id: texto,
                        seja mentor_name: texto = "Mentor Voluntario",
                        seja mentor_id: texto = "M-001") -> {texto: qualquer}:
        // Prepara TODA a infraestrutura antes da liberacao (30 dias).
        plan = self.plans.get(plan_id)
        se nao plan entao:
            retorne {"error": "Plano nao encontrado"}

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
        se plan.treatment_needs entao:
            se "tratamento_dependencia_quimica" in plan.treatment_needs entao:
                plan.needs[SupportNeed.ADDICTION_TREATMENT] = SupportStatus.ONGOING
            se "tratamento_saude_mental" in plan.treatment_needs entao:
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

        retorne {
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

    funcao release(self, plan_id: texto) -> {texto: qualquer}:
        // Libera ex-penitenciario COM infraestrutura total.
        plan = self.plans.get(plan_id)
        se nao plan entao:
            retorne {"error": "Plano nao encontrado"}
        se nao plan.can_release entao:
            retorne {
                "error": "NAO PODE LIBERAR",
                "readiness": "{plan.readiness_score:.0f}%",
                "reason": "Infraestrutura incompleta. Republica NAO libera sem suporte.",
            }

        plan.phase = ReintegrationPhase.DAY_0
        plan.release_date = datetime.now().isoformat()
        plan.days_since_release = 0

        // Expungement (prontuario limpo)
        was_hediondous = "homicidio" in plan.original_crime.lower()  ou  \
                         "abuso" in plan.original_crime.lower()
        eligibility = self.expungement.check_eligibility(
            plan.citizen_id, was_hediondous)
        se eligibility["eligible"] entao:
            expungement = self.expungement.expunge(
                plan.citizen_id, plan.citizen_name,
                plan.original_crime, plan.years_served,
                plan.skills_learned)
        senao:
            expungement = eligibility

        retorne {
            "released": verdadeiro,
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
                 seja notes: texto = "") -> {texto: qualquer}:
        // Check-in periodico do ex-penitenciario.
        plan = self.plans.get(plan_id)
        se nao plan entao:
            retorne {"error": "nao encontrado"}

        plan.days_since_release += 7 // simular passagem de tempo
        plan.check_ins.append({
            "date": datetime.now().isoformat(),
            "days_since_release": plan.days_since_release,
            "status": status,
            "notes": notes,
        })

        // Progressao de fase
        se plan.days_since_release <= 1 entao:
            plan.phase = ReintegrationPhase.DAY_0
        senao se plan.days_since_release <= 7 entao:
            plan.phase = ReintegrationPhase.FIRST_WEEK
        senao se plan.days_since_release <= 30 entao:
            plan.phase = ReintegrationPhase.FIRST_MONTH
        senao se plan.days_since_release <= 90 entao:
            plan.phase = ReintegrationPhase.FIRST_QUARTER
        senao se plan.days_since_release <= 365 entao:
            plan.phase = ReintegrationPhase.FIRST_YEAR
            plan.milestones_achieved.append("sobreviveu_primeiro_ano")
        senao:
            plan.phase = ReintegrationPhase.INTEGRATED
            self.stats_total_reintegrated += 1

        retorne {
            "citizen": plan.citizen_name,
            "days_since_release": plan.days_since_release,
            "phase": plan.phase.value,
            "status": status,
            "mentor": plan.assigned_mentor,
            "work": plan.work_assignment,
        }

    funcao report_recidivism(self, plan_id: texto, reason: texto) -> {texto: qualquer}:
        // Se voltou a cometer crime -- FALHA do sistema.
        plan = self.plans.get(plan_id)
        se nao plan entao:
            retorne {"error": "nao encontrado"}

        plan.recidivated = verdadeiro
        plan.recidivism_reason = reason
        plan.phase = ReintegrationPhase.RECIDIVED
        self.stats_total_recidivism += 1

        // Analisar onde o sistema falhou
        failed_needs = [need.value para need, status in plan.needs.items()
                        if status = = SupportStatus.FAILED]

        retorne {
            "citizen": plan.citizen_name,
            "recidivated": verdadeiro,
            "reason": reason,
            "system_failure": (
                "A Republica ASSUME a culpa. Algo faltou. "
                "Processo sera revisado. Nao e culpa da pessoa."
            ),
            "failed_supports": failed_needs  ou  ["analise_necessaria"],
            "action": (
                "Revisar processo de reintegration. "
                "Corrigir para o proximo. "
                "Reabrir plano de transformacao (OpenPenalRevision)."
            ),
        }

    funcao stats(self) -> {texto: qualquer}:
        reintegrated = soma(1 para p em self.plans.values()
                           if p.phase in (ReintegrationPhase.FIRST_YEAR,
                                           ReintegrationPhase.INTEGRATED)
                            e nao p.recidivated)
        recidivated = soma(1 para p em self.plans.values() if p.recidivated)
        in_progress = soma(1 para p em self.plans.values()
                          if p.phase nao in (ReintegrationPhase.INTEGRATED,
                                             ReintegrationPhase.RECIDIVED)
                           e nao p.recidivated)
        total_outcome = tamanho(self.plans)
        rate = total_outcome > 0 ? (recidivated / total_outcome * 100) : 0
        retorne {
            "total_plans": tamanho(self.plans),
            "in_progress": in_progress,
            "fully_reintegrated": reintegrated,
            "recidivated": recidivated,
            "recidivism_rate": "{rate:.0f}%",
            "comparison_current_system": "70% (Brasil atual)",
            "expunged_records": tamanho(self.expungement.expunged),
            "housing_provided": tamanho(self.infra.housing_units),
            "mentors_active": tamanho(self.infra.mentors),
            "community_groups": tamanho(self.infra.community_groups),
        }


// ============================================================================
// 6. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = ReintegrationEngine()

    imprima("=" * 80)
    imprima("  OPENREINTEGRATION")
    imprima("  Infraestrutura Completa para Ex-Penitenciarios")
    imprima("  'Para que nao precisem cometer erros.'")
    imprima("=" * 80)

    // === CASOS DE EX-PENITENCIARIOS ===
    cases = [
        ("P-005", "Pedro Costa", 25, "Furto R$ 500 em ferramentas",
         1.0, ["construcao_civil", "agricultura_urbana", "letramento_digital"]),
        ("P-009", "Marcos Vieira", 40, "Roubo a mao armada (simulacro)",
         2.0, ["marcenaria", "culinaria"], ["tratamento_dependencia_quimica"]),
        ("P-010", "Lucas Martins", 22, "Trafico (soldo, nao chefe)",
         3.0, ["cooperacao_comunitaria", "construcao_civil", "agricultura_urbana"],
         []),
        ("P-007", "Roberto Alves", 35, "Agressao fisica sem ferimentos graves",
         0.5, ["arte_terapia", "culinaria"], ["tratamento_saude_mental"]),
    ]

    // === 1. CRIAR PLANOS ===
    imprima("\n\n  === 1. PLANOS DE REINTEGRACAO ===\n")
    para cid, name, age, crime, served, skills, *treatments in cases:
        treatment = treatments ? treatments[0] : []
        plan = engine.create_plan(cid, name, age, crime, served, skills, treatment)
        imprima("  [{plan.plan_id}] {name} ({age} anos)")
        imprima("    Crime original: {crime}")
        imprima("    Tempo cumprido: {served:.1f} anos")
        imprima("    Skills: {', '.join(skills[:3])}")
        se treatment entao:
            imprima("    Tratamento: {', '.join(treatment)}")
        imprima("    Readiness inicial: {plan.readiness_score:.0f}%")

    // === 2. PREPARAR LIBERACAO (30 dias antes) ===
    imprima("\n\n  === 2. PREPARANDO INFRAESTRUTURA (30 dias antes) ===\n")
    para cid, name, *_ in cases:
        plans = [p para p em engine.plans.values() if p.citizen_id == cid]
        se plans entao:
            prep = engine.prepare_release(plans[0].plan_id)
            imprima("\n  [{prep['citizen']}] Readiness: {prep['readiness']}")
            imprima("    Moradia: {prep['details']['housing']['location']}")
            imprima("    Trabalho: {prep['details']['employment']['job']}")
            imprima("    Mentor: {prep['details']['mentor']['mentor']}")
            imprima("    Comunidade: {prep['details']['community']['group']}")
            imprima("    Saude: {prep['details']['health']['level']}")
            imprima("    OpenKit: {prep['details']['kit']['cost']}")
            imprima("    Pode liberar: {'SIM' if prep['can_release'] else 'NAO'}")

    // === 3. LIBERACAO ===
    imprima("\n\n  === 3. LIBERACAO COM INFRAESTRUTURA ===\n")
    para cid, name, *_ in cases:
        plans = [p para p em engine.plans.values() if p.citizen_id == cid]
        se plans entao:
            release = engine.release(plans[0].plan_id)
            imprima("\n  [{release.get('citizen', name)}]")
            se release.get("released") entao:
                imprima("    LIBERADO com infraestrutura completa")
                imprima("    Na rua: NAO -- {release['housing']}")
                imprima("    Abandonado: NAO -- mentor + comunidade")
                imprima("    Trabalho: {release['work']}")
                ex = release.get("prontuario", {})
                se ex.get("expunged") entao:
                    imprima("    Prontuario: {ex['after']}")
                    imprima("    Visivel a: {ex['visible']}")
            senao:
                imprima("    {release.get('error', 'ERRO')}")

    // === 4. CHECK-INS (simular passagem de tempo) ===
    imprima("\n\n  === 4. CHECK-INS PERIODICOS ===\n")
    para cid, name, *_ in cases:
        plans = [p para p em engine.plans.values() if p.citizen_id == cid]
        se plans entao:
            // Simular 4 check-ins (4 semanas)
            para cada _ em intervalo(4):
                ci = engine.check_in(plans[0].plan_id, "bom", "")
            imprima("  {name}: {ci['days_since_release']} dias -> {ci['phase']}")

    // === 5. VERIFICAR PRONTUARIO LIMPO ===
    imprima("\n\n  === 5. VERIFICACAO DE PRONTUARIO (como empregador veria) ===\n")
    para cid, name, *_ in cases:
        check = engine.expungement.verify_clean_record(cid)
        imprima("  {name:<20} -> {check['record']} ({check['status']})")

    // === 6. CASO DE REINCIDENCIA (FALHA DO SISTEMA) ===
    imprima("\n\n  === 6. REINCIDENCIA = FALHA DO SISTEMA ===\n")
    plans_list = list(engine.plans.values())
    se plans_list entao:
        rec = engine.report_recidivism(
            plans_list[1].plan_id, // Marcos
            "Recaiu em alcool + moradia distante do tratamento")
        imprima("  {rec['citizen']} reincidiu.")
        imprima("  Motivo: {rec['reason']}")
        imprima("  {rec['system_failure']}")
        imprima("  Suportes que falharam: {rec['failed_supports']}")
        imprima("  Acao: {rec['action']}")

    // === 7. COMPARACAO ===
    imprima("\n\n  === 7. COMPARACAO: SISTEMA ATUAL vs REPUBLICA ===\n")
    s = engine.stats()
    imprima("  {'Metrica':<30} {'Sistema Atual':>15} {'Republica':>15}")
    imprima("  {'-'*62}")
    imprima("  {'Reincidencia':<30} {'70%':>14} {s['recidivism_rate']:>14}")
    imprima("  {'Moradia ao sair':<30} {'Rua/favela':>15} {'Garantida':>15}")
    imprima("  {'Trabalho ao sair':<30} {'Nenhum':>15} {'Garantido':>15}")
    imprima("  {'Mentor':<30} {'Nenhum':>15} {'1 ano':>15}")
    imprima("  {'Saude':<30} {'SUS fila':>15} {'Sirio-Lib.':>15}")
    imprima("  {'Prontuario':<30} {'Marcado':>15} {'LIMPO':>15}")
    imprima("  {'Comunidade':<30} {'Isolado':>15} {'Apoio mutuo':>15}")
    imprima("  {'Custo':<30} {'R$ 42k/ano':>15} {'ZERO':>15}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DA REINTEGRACAO")
    imprima("{'='*80}")
    imprima("""
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
    - Moradia -> nao vai pra rua
    - Trabalho -> nao precisa roubar
    - Tratamento -> nao recai em drogas
    - Comunidade -> nao se isola
    - Prontuario LIMPO -> e cidadao igual aos outros

  O QUE FORNECE (DIA 1):
    1. MORADIA: unidade da Republica (nao rua, nao criminogeno)
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
    OpenHistory registra como "TRANSFORMACAO", nao "crime".
    Prontuario: LIMPO (ninguem ve o passado).
    Antecedentes: ZERO (resultado de consulta = cidadao).
    Excecao: crimes hediondos (restricao permanente).

  PREVENCAO > PUNICAO:
    Prevenir custa ZERO (direito, nao compra).
    Punir custa R$ 42k/ano + nova vitima + reincidencia.
    A Republica escolhe prevenir. Sempre.

  PRINCIPIOS:
    P1: Ex-penitenciario e cidadao igual. Sem marcador. Sem elitismo.
    P2: Seu corpo e vida sao soberanos. Apenas com suporte.
    P3: Trabalho garantido. Base 1.0 como todos.
    P4: Reincidencia e falha do SISTEMA, nao da pessoa.
// )
    imprima("{'='*80}")
    imprima("  OpenReintegration: {s['total_plans']} planos, "
          "{s['fully_reintegrated']} integrados, "
          "{s['expunged_records']} prontuarios limpos.")
    imprima("  Reincidencia: {s['recidivism_rate']} (vs 70% atual).")
    imprima("  Prevenir > Punir. Sempre.")
    imprima("{'='*80}")

```
