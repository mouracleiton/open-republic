# OpenRepublic -- Federacao de Nacoes OpenNation

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_republic.py`

**Descricao:** =================================================
Multiplas nacoes operando sob o principio de bens comuns (sem propriedade
privada), unidas numa federacao que coordena infraestrutura compartilhada,
migracao livre, resolucão de conflitos entre nacoes, e governanca federal
liquida.
"Varias OpenNations, uma OpenRepublic."
Cada nacao mantem autonomia cultural e decisoes locais.
A Republica coordena o que e transnacional:
  - Infraestrutura continental (energia, transporte, comunicacao)
  - Grandes projetos (fusao nuclear, espacial, erradicacao de doencas)
  - Migracao irrestrita entre nacoes (ninguem e ilegal)
  - Tratados entre nacoes (rios, florestas, oceanos compartilhados)
  - Defesa comum (defesa, nao ataque -- dissuasao pura)
  - Padroes e protocolos (OpenProtocol, OpenNetwork, etc.)
A Republica NAO tem poder de guerra, NAO cobra impostos (nao ha dinheiro),
NAO tem burocracia permanente. E uma rede de coordinacao, nao um Estado.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Federacao de Nacoes OpenNation
=================================================

Multiplas nacoes operando sob o principio de bens comuns (sem propriedade
privada), unidas numa federacao que coordena infraestrutura compartilhada,
migracao livre, resolucão de conflitos entre nacoes, e governanca federal
liquida.

"Varias OpenNations, uma OpenRepublic."

Cada nacao mantem autonomia cultural e decisoes locais.
A Republica coordena o que e transnacional:
  - Infraestrutura continental (energia, transporte, comunicacao)
  - Grandes projetos (fusao nuclear, espacial, erradicacao de doencas)
  - Migracao irrestrita entre nacoes (ninguem e ilegal)
  - Tratados entre nacoes (rios, florestas, oceanos compartilhados)
  - Defesa comum (defesa, nao ataque -- dissuasao pura)
  - Padroes e protocolos (OpenProtocol, OpenNetwork, etc.)

A Republica nao tem poder de guerra, nao cobra impostos (nao ha dinheiro),
nao tem burocracia permanente. e uma rede de coordinacao, nao um Estado.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa defaultdict de collections
// importa numpy as np


// ============================================================================
// Enums
// ============================================================================

classe InfrastructureType herda de Enum:
    // Infraestrutura federal compartilhada entre todas as nacoes.
    ENERGY_GRID = "energy_grid"  // rede eletrica continental
    TRANSPORT_NET = "transport_net"  // ferrovias, portos, aeroportos
    COMMUNICATION = "communication"  // OpenProtocol backbone, satellites
    WATER_SYS = "water_sys"  // aquedutos, bacias transfronteiricas
    FOOD_DIST = "food_dist"  // rede de distribuicao de alimentos
    HEALTH_NET = "health_net"  // hospitais de referencia, pesquisa
    SPACE_INFRA = "space_infra"  // satelites, estacoes espaciais
    DEFENSE = "defense"  // defesa dissuasoria compartilhada
    RESEARCH = "research"  // laboratorios nacionais, aceleradores


classe MigrationStatus herda de Enum:
    FREE = "free"  // migracao livre, sem fronteiras
    WELCOMING = "welcoming"  // nacao aceitando novos cidadaos
    BALANCED = "balanced"  // equilibrio populacional
    SATURATED = "saturated"  // temporariamente sem capacidade


classe TreatyType herda de Enum:
    RESOURCE = "resource"  // gestao de recurso compartilhado
    ECOLOGICAL = "ecological"  // preservacao ambiental
    SCIENTIFIC = "scientific"  // colaboracao cientifica
    CULTURAL = "cultural"  // intercambio cultural
    INFRASTRUCTURE = "infrastructure"  // construcao conjunta
    PEACE = "peace"  // pacto de nao-agressao


classe FederalProposalCategory herda de Enum:
    INFRASTRUCTURE = "infrastructure"
    TREATY = "treaty"
    STANDARD = "standard"  // definicao de padrao tecnico
    GRAND_PROJECT = "grand_project"
    PEACEKEEPING = "peacekeeping"
    RESOURCE_ALLOCATION = "resource_allocation"
    CONSTITUTIONAL = "constitutional"  // mudanca nos principios da Republica


// ============================================================================
// Nation (member of the Republic)
// ============================================================================

// decorador: @dataclass
classe NationMetrics:
    // Metricas de uma nacao membro.
    seja population: inteiro = 0
    seja housing_units: inteiro = 0
    seja food_kg_month: flutuante = 0.0
    seja energy_kwh_month: flutuante = 0.0
    seja water_liters_day: flutuante = 0.0
    seja healthcare_capacity: inteiro = 0
    seja education_centers: inteiro = 0
    seja innovation_count: inteiro = 0
    seja ecological_health: flutuante = 0.8
    seja commons_count: inteiro = 0
    seja conflicts_open: inteiro = 0

    // decorador: @property
    funcao qol_index(self) -> flutuante:
        // Indice de qualidade de vida da nacao (0-100).
        se self.population == 0 entao:
            retorne 0
        housing_ratio = minimo(1, self.housing_units / maximo(self.population / 3, 1))
        food_ratio = minimo(1, self.food_kg_month / maximo(self.population * 12, 1))
        energy_ratio = minimo(1, self.energy_kwh_month / maximo(self.population * 100, 1))
        health_ratio = minimo(1, self.healthcare_capacity / maximo(self.population / 500, 1))
        edu_ratio = minimo(1, self.education_centers / maximo(self.population / 5000, 1))
        overall = (housing_ratio * 0.20 + food_ratio * 0.20 +
                   energy_ratio * 0.15 + health_ratio * 0.15 +
                   edu_ratio * 0.15 + self.ecological_health * 0.15) * 100
        retorne arredonde(overall, 1)

    // decorador: @property
    funcao carrying_capacity(self) -> inteiro:
        // Populacao maxima sustentavel atual.
        cap_food = self.food_kg_month > 0 ? self.food_kg_month / 12 : 0
        cap_water = self.water_liters_day > 0 ? self.water_liters_day / 200 : 0
        cap_housing = self.housing_units * 3
        cap_energy = self.energy_kwh_month > 0 ? self.energy_kwh_month / 100 : 0
        retorne inteiro(minimo(cap_food, cap_water, cap_housing, cap_energy))


// decorador: @dataclass
classe Nation:
    // Uma nacao membro da Republica.

    Cada nacao opera sob os principios do OpenNation:
    sem propriedade privada, bens comuns, democracia liquida.
    A Republica adiciona coordenacao entre nacoes.
    // 
    nation_id: texto
    name: texto
    region: texto // continente/regiao
    culture: texto // descricao cultural
    languages: [texto]
    seja founded_cycle: inteiro = 0
    seja metrics: NationMetrics = field(default_factory=NationMetrics)
    seja migration_status: MigrationStatus = MigrationStatus.FREE
    seja specialties: [texto] = field(default_factory=list) // areas de excelencia
    seja citizens_ids: {texto} = field(default_factory=set)
    seja federal_proposals_voted: inteiro = 0
    seja federal_projects_contributed: inteiro = 0


// ============================================================================
// Shared Infrastructure (Federal)
// ============================================================================

// decorador: @dataclass
classe FederalInfrastructure:
    // Infraestrutura construida e mantida coletivamente por todas as nacoes.

    Nenhuma nacao possui estas infraestruturas. Sao bens comuns da Republica.
    Cada nacao contribui com trabalho e recursos para construcao/manutencao.
    // 
    infra_id: texto
    name: texto
    itype: InfrastructureType
    description: texto
    seja serving_nations: {texto} = field(default_factory=set) // nation_ids
    seja capacity: flutuante = 0.0
    seja unit: texto = ""
    seja condition: flutuante = 1.0
    seja build_cycles: inteiro = 0
    seja contributing_nations: {texto} = field(default_factory=set)
    seja labor_invested: flutuante = 0.0 // horas totais investidas


classe InfrastructureManager:
    // Gerencia infraestrutura federal compartilhada.

    Grandes projetos que uma nacao sozinha nao conseguiria:
    - Rede eletrica continental (fusion/solar/wind)
    - Sistema ferroviario de alta velocidade
    - Backbone de comunicacao (OpenProtocol satellites)
    - Aquedutos transcontinentais
    - Sistema de defesa dissuasoria compartilhada
    // 

    funcao __init__(self):
        self.projects: {texto: FederalInfrastructure} = {}
        self._counter = 0

    funcao propose(self, name: texto, itype: InfrastructureType,
                description: texto, capacity: flutuante, unit: texto,
                build_cycles: inteiro, proposing_nation: texto) -> texto:
        self._counter += 1
        iid = "INFRA-{self._counter:04d}"
        proj = FederalInfrastructure(
            infra_id = iid, name=name, itype=itype,
            description = description, capacity=capacity, unit=unit,
            build_cycles = build_cycles, contributing_nations={proposing_nation})
        self.projects[iid] = proj
        retorne iid

    funcao contribute(self, infra_id: texto, nation_id: texto, labor_hours: flutuante):
        proj = self.projects.get(infra_id)
        se proj entao:
            proj.contributing_nations.add(nation_id)
            proj.labor_invested += labor_hours

    funcao advance_build(self, infra_id: texto) -> {texto: qualquer}:
        // Avancar construcao por um ciclo.
        proj = self.projects.get(infra_id)
        se nao proj entao:
            retorne {"status": "not_found"}
        proj.build_cycles = maximo(0, proj.build_cycles - 1)
        se proj.build_cycles == 0 entao:
            retorne {"status": "completed", "infra_id": infra_id,
                    "name": proj.name, "capacity": proj.capacity}
        retorne {"status": "in_progress", "remaining_cycles": proj.build_cycles}

    funcao summary(self) -> {texto: qualquer}:
        by_type = defaultdict(() -> {"count": 0, "total_capacity": 0, "serving": 0})
        para cada proj em self.projects.values():
            by_type[proj.itype.value]["count"] += 1
            by_type[proj.itype.value]["total_capacity"] += proj.capacity
            by_type[proj.itype.value]["serving"] += tamanho(proj.serving_nations)

        completed = soma(1 para p em self.projects.values() if p.build_cycles == 0)
        in_progress = soma(1 para p em self.projects.values() if p.build_cycles > 0)

        retorne {
            "total_projects": tamanho(self.projects),
            "completed": completed,
            "in_progress": in_progress,
            "total_labor_invested": arredonde(soma(p.labor_invested para p em self.projects.values()), 0),
            "by_type": dict(by_type),
        }


// ============================================================================
// Inter-Nation Migration (free movement)
// ============================================================================

// decorador: @dataclass
classe MigrationEvent:
    // Movimento de um cidadao entre nacoes.
    citizen_id: texto
    from_nation: texto
    to_nation: texto
    reason: texto // opportunity, family, study, climate, curiosity
    seja cycle: inteiro = 0


classe MigrationSystem:
    // Migracao livre entre nacoes.

    Ninguem e ilegal. Nao ha fronteiras. Nao ha passaporte.
    Cada cidadao da Republica pode viver em qualquer nacao.

    O sistema balanceia automaticamente:
    - Se uma nacao esta saturada, novos chegados sao informados
      (mas nao proibidos -- a nacao precisa expandir capacidade)
    - Se uma nacao tem excesso de capacidade, incentiva chegada
    - O objetivo e que cada nacao atinja equilibrio populacional

    Motivacoes reais para migrar (sem dinheiro, sem propriedade):
    - Oportunidade de contribuir em area de especialidade
    - Clima e geografia preferidos
    - Proximidade de familia/comunidade
    - Aprendizado (estudar com mestres de outra nacao)
    - Curiosidade e aventura
    // 

    funcao __init__(self):
        self.events: [MigrationEvent] = []
        self.balance_bonus = 0.5 // incentivo para nacoes com capacidade

    funcao evaluate_migration(self, citizen_id: texto, from_nation: Nation,
                           to_nation: Nation, reason: texto = "opportunity") -> {texto: qualquer}:
        // Avaliar se migracao e benéfica.
        from_cap = from_nation.metrics.carrying_capacity
        to_cap = to_nation.metrics.carrying_capacity
        from_pop = from_nation.metrics.population
        to_pop = to_nation.metrics.population

        // Benefico se alivia pressao na origem e nao satura destino
        from_relief = from_pop > from_cap * 0.9 // origem esta sob pressao
        to_room = to_pop < to_cap * 0.85 // destino tem espaco

        beneficial = from_relief ou to_room

        status = MigrationStatus.FREE
        recommendation = "go"
        se to_nation.migration_status == MigrationStatus.SATURATED entao:
            recommendation = "wait"
            status = MigrationStatus.SATURATED
        senao se to_room e from_relief entao:
            recommendation = "strongly_recommended"
        senao se to_room entao:
            recommendation = "welcoming"
        senao se nao to_room entao:
            recommendation = "accepted_but_contribute_to_expansion"

        event = MigrationEvent(
            citizen_id = citizen_id, from_nation=from_nation.nation_id,
            to_nation = to_nation.nation_id, reason=reason)
        self.events.append(event)

        retorne {
            "citizen": citizen_id,
            "from": from_nation.name,
            "to": to_nation.name,
            "reason": reason,
            "beneficial": beneficial,
            "recommendation": recommendation,
            "to_nation_capacity_used": "{to_pop}/{to_cap}",
            "no_borders": verdadeiro,
            "no_passport_needed": verdadeiro,
        }

    funcao flow_stats(self) -> {texto: qualquer}:
        // Estatisticas de fluxo migratorio.
        by_reason = defaultdict(inteiro)
        para cada e em self.events:
            by_reason[e.reason] += 1

        nation_inflow = defaultdict(inteiro)
        nation_outflow = defaultdict(inteiro)
        para cada e em self.events:
            nation_inflow[e.to_nation] += 1
            nation_outflow[e.from_nation] += 1

        retorne {
            "total_migrations": tamanho(self.events),
            "by_reason": dict(by_reason),
            "top_destinations": dict(ordene(nation_inflow.items(),
                                            key = (x) -> -x[1])[:5]),
            "top_origins": dict(ordene(nation_outflow.items(),
                                       key = (x) -> -x[1])[:5]),
            "rejected_at_border": 0,   // sempre 0 -- sem fronteiras
        }


// ============================================================================
// Inter-Nation Treaties
// ============================================================================

// decorador: @dataclass
classe Treaty:
    // Tratado entre nacoes (ou multilateral).
    treaty_id: texto
    name: texto
    ttype: TreatyType
    description: texto
    seja signatories: {texto} = field(default_factory=set)
    seja terms: {texto: texto} = field(default_factory=dict)
    seja status: texto = "proposed"  // proposed, active, violated, dissolved
    seja created_cycle: inteiro = 0


classe TreatySystem:
    // Sistema de tratados entre nacoes.

    Tratados sao necessarios para:
    - Rios que cruzam fronteiras (bacias hidrograficas)
    - Florestas continentais (Amazonia, Congo, Boreal)
    - Oceanos compartilhados (pesca, mineracao, poluicao)
    - Grandes projetos de infraestrutura
    - Colaboracao cientifica
    - Intercambio cultural

    Tratados nao sao contratos comerciais (nao ha comercio).
    Sao acordos de STEWARDSHIP compartilhado de bens comuns.
    // 

    funcao __init__(self):
        self.treaties: {texto: Treaty} = {}
        self._counter = 0

    funcao propose(self, name: texto, ttype: TreatyType, description: texto,
                proposing_nation: texto, terms: {texto: texto} = nulo) -> texto:
        self._counter += 1
        tid = "TREATY-{self._counter:04d}"
        self.treaties[tid] = Treaty(
            treaty_id = tid, name=name, ttype=ttype, description=description,
            signatories = {proposing_nation}, terms=terms ou {})
        retorne tid

    funcao sign(self, treaty_id: texto, nation_id: texto):
        t = self.treaties.get(treaty_id)
        se t  e  t.status in ("proposed", "active") entao:
            t.signatories.add(nation_id)
            se tamanho(t.signatories) >= 2 entao:
                t.status = "active"

    funcao summary(self) -> {texto: qualquer}:
        active = [t para t em self.treaties.values() if t.status == "active"]
        retorne {
            "total_treaties": tamanho(self.treaties),
            "active": tamanho(active),
            "proposed": soma(1 para t em self.treaties.values() if t.status == "proposed"),
            active ? "avg_signatories": arredonde(np.mean([tamanho(t.signatories) para t em active]), 1) : 0,
            "by_type": dict(Counter(t.ttype.value para t em active)),
        }


// importa Counter de collections


// ============================================================================
// Federal Governance (Liquid Democracy across Nations)
// ============================================================================

// decorador: @dataclass
classe FederalProposal:
    // Proposta federal -- afeta todas as nacoes da Republica.
    proposal_id: texto
    title: texto
    description: texto
    category: FederalProposalCategory
    proposer_nation: texto
    seja votes_by_nation: Dict[texto, (flutuante, flutuante)] = field(default_factory=dict)
    // nation_id -> (votes_for, votes_against) weighted by population
    seja status: texto = "open"  // open, passed, rejected
    seja cycle_submitted: inteiro = 0
    seja affects_infra: texto = ""  // infra_id if applicable


classe FederalGovernance:
    // Governanca federal da Republica.

    Diferente da governanca nacional (1 cidadao = 1 voto),
    a federal pondera por populacao mas com teto anti-hegemonia.

    Principio anti-hegemonia: nenhuma nacao sozinha pode dominar.
    Veto coletivo: se 1/3 das nacoes votam contra, reprova mesmo
    com maioria populacional.

    Nao ha presidente. Nao ha congresso. Nao ha burocracia.
    Ha propostas, debates abertos, e votacao direta dos cidadaos
    de cada nacao -- com delegacao liquida transnacional.
    // 

    funcao __init__(self):
        self.proposals: {texto: FederalProposal} = {}
        self._counter = 0
        self.constitutional_principles = [
            "Nenhuma nacao possui outra nacao",
            "Todo cidadao e livre para migrar entre nacoes",
            "Todo conhecimento e bem comum (sem patentes)",
            "A natureza e responsabilidade de todas as nacoes",
            "Nenhuma nacao pode declarar guerra (apenas defesa)",
            "Infraestrutura federal e bem comum de todas as nacoes",
            "Decisoes federais requerem maioria + anti-hegemonia",
            "Qualquer nacao pode sair da Republica a qualquer momento",
        ]

    funcao submit(self, title: texto, description: texto, category: FederalProposalCategory,
               proposer: texto, cycle: inteiro = 0) -> texto:
        self._counter += 1
        pid = "FED-{self._counter:04d}"
        self.proposals[pid] = FederalProposal(
            proposal_id = pid, title=title, description=description,
            category = category, proposer_nation=proposer, cycle_submitted=cycle)
        retorne pid

    funcao vote_nation(self, proposal_id: texto, nation_id: texto,
                    pop_for: flutuante, pop_against: flutuante):
        // Registrar votacao de uma nacao (resultado do voto direto local).
        prop = self.proposals.get(proposal_id)
        se nao prop entao:
            retorne nulo
        prop.votes_by_nation[nation_id] = (pop_for, pop_against)

    funcao close(self, proposal_id: texto, total_nations: inteiro) -> {texto: qualquer}:
        // Fechar votacao com regra anti-hegemonia.
        prop = self.proposals.get(proposal_id)
        se nao prop entao:
            retorne {}

        total_for = soma(v[0] para v em prop.votes_by_nation.values())
        total_against = soma(v[1] para v em prop.votes_by_nation.values())
        total = total_for + total_against

        // Regra 1: maioria ponderada por populacao
        majority_passed = total > 0 ? total_for > total_against : falso

        // Regra 2: anti-hegemonia -- 1/3 das nacoes podem veto
        nations_voting = tamanho(prop.votes_by_nation)
        nations_against = soma(1 para v em prop.votes_by_nation.values()
                              if v[1] > v[0])
        veto_threshold = total_nations / 3
        anti_hegemony_veto = nations_against >= veto_threshold

        passed = majority_passed e nao anti_hegemony_veto
        passed ? prop.status = "passed" : "rejected"

        retorne {
            "proposal": prop.title,
            majority_passed ? "majority_vote": "pass" : "fail",
            "anti_hegemony_veto": anti_hegemony_veto,
            "nations_against": nations_against,
            "veto_threshold": arredonde(veto_threshold, 1),
            passed ? "result": "PASSED" : "REJECTED",
            "principle": "Majority + no 1/3 veto bloc",
        }

    funcao summary(self) -> {texto: qualquer}:
        retorne {
            "total_proposals": tamanho(self.proposals),
            "passed": soma(1 para p em self.proposals.values() if p.status == "passed"),
            "rejected": soma(1 para p em self.proposals.values() if p.status == "rejected"),
            "open": soma(1 para p em self.proposals.values() if p.status == "open"),
            "constitutional_principles": tamanho(self.constitutional_principles),
            "has_president": falso,
            "has_congress": falso,
            "has_bureaucracy": falso,
        }


// ============================================================================
// Grand Projects (Republic-scale endeavors)
// ============================================================================

// decorador: @dataclass
classe GrandProject:
    // Projeto grandioso que requer esforco de multiplas nacoes.
    project_id: texto
    name: texto
    description: texto
    required_nations: inteiro // minimo nacoes contribuindo
    required_labor_hours: flutuante // total de horas necessarias
    seja current_labor: flutuante = 0.0
    seja contributing_nations: {texto} = field(default_factory=set)
    seja status: texto = "recruiting"  // recruiting, active, completed
    seja benefit: texto = ""  // quem se beneficia


classe GrandProjectManager:
    // Gerencia projetos que uma nacao sozinha nao consegue.

    Exemplos historicos (se fossem feitos sem proprietarios):
    - Projeto Manhattan (sem armas -- so a fisica)
    - Programa Apollo
    - LHC (Large Hadron Collider)
    - ITER (fusao nuclear)
    - Telescopio James Webb
    - Sequenciamento do genoma humano
    - Erradicacao da polio

    Na OpenRepublic:
    - Fusao nuclear comercial (energia ilimitada para todas as nacoes)
    - Cidade orbital / colonia lunar
    - Rede global de computacao quantica (Open-Quantum)
    - Erradicacao de todas as doencas transmissiveis
    - Restauracao de ecossistemas continentais
    - Rede ferroviaria de alta velocidade global
    // 

    funcao __init__(self):
        self.projects: {texto: GrandProject} = {}
        self._counter = 0

    funcao propose(self, name: texto, description: texto, required_nations: inteiro,
                required_hours: flutuante, benefit: texto) -> texto:
        self._counter += 1
        pid = "GRAND-{self._counter:04d}"
        self.projects[pid] = GrandProject(
            project_id = pid, name=name, description=description,
            required_nations = required_nations, required_labor_hours=required_hours,
            benefit = benefit)
        retorne pid

    funcao contribute(self, project_id: texto, nation_id: texto, labor_hours: flutuante):
        proj = self.projects.get(project_id)
        se nao proj entao:
            retorne nulo
        proj.contributing_nations.add(nation_id)
        proj.current_labor += labor_hours

        se tamanho(proj.contributing_nations) >= proj.required_nations  e  proj.status == "recruiting" entao:
            proj.status = "active"

        se proj.current_labor >= proj.required_labor_hours  e  proj.status == "active" entao:
            proj.status = "completed"

    funcao progress(self, project_id: texto) -> {texto: qualquer}:
        proj = self.projects.get(project_id)
        se nao proj entao:
            retorne {}
        retorne {
            "name": proj.name,
            "status": proj.status,
            "labor_progress_pct": arredonde(proj.current_labor / maximo(proj.required_labor_hours, 1) * 100, 1),
            "nations_contributing": tamanho(proj.contributing_nations),
            "required_nations": proj.required_nations,
            "benefit": proj.benefit,
        }

    funcao summary(self) -> {texto: qualquer}:
        retorne {
            "total_projects": tamanho(self.projects),
            "completed": soma(1 para p em self.projects.values() if p.status == "completed"),
            "active": soma(1 para p em self.projects.values() if p.status == "active"),
            "recruiting": soma(1 para p em self.projects.values() if p.status == "recruiting"),
            "total_labor_invested": arredonde(soma(p.current_labor para p em self.projects.values()), 0),
        }


// ============================================================================
// Republic
// ============================================================================

classe OpenRepublic:
    // A Republica: federacao de nacoes OpenNation.

    Estrutura:
      Nacoes (autonomas culturalmente, bens comuns localmente)
        |
        v
      Republica (coordena o transnacional)
        - Infraestrutura compartilhada
        - Migracao livre
        - Tratados
        - Grandes projetos
        - Governanca federal liquida
    // 

    funcao __init__(self, name: texto = "OpenRepublic"):
        self.name = name
        self.nations: {texto: Nation} = {}
        self.infrastructure = InfrastructureManager()
        self.migration = MigrationSystem()
        self.treaties = TreatySystem()
        self.federal_gov = FederalGovernance()
        self.grand_projects = GrandProjectManager()
        self.current_cycle = 0
        self.history: [Dict] = []

    funcao admit_nation(self, nation: Nation):
        self.nations[nation.nation_id] = nation
        nation.founded_cycle = self.current_cycle

    funcao total_population(self) -> inteiro:
        retorne soma(n.metrics.population para n em self.nations.values())

    funcao run_cycle(self) -> {texto: qualquer}:
        // Avancar a Republica por um ciclo (mes).
        self.current_cycle += 1
        cycle_data = {"cycle": self.current_cycle}

        // 1. Migration flow
        migrations = 0
        nation_list = list(self.nations.values())
        se tamanho(nation_list) >= 2 entao:
            para cada _ em intervalo(random.randint(5, 20)):
                frm = random.choice(nation_list)
                to = random.choice([n para n em nation_list if n.nation_id != frm.nation_id])
                se frm.metrics.population > 0 entao:
                    citizen = "C-{random.randint(0, frm.metrics.population):04d}"
                    self.migration.evaluate_migration(citizen, frm, to,
                                                      random.choice(["opportunity", "study", "family", "curiosity"]))
                    migrations = migrations + 1

        // 2. Infrastructure advancement
        infra_completed = 0
        para cada iid em list(self.infrastructure.projects.keys()):
            // Random nations contribute labor
            para cada n em random.sample(nation_list, minimo(3, tamanho(nation_list))):
                self.infrastructure.contribute(iid, n.nation_id, random.uniform(50, 200))
            result = self.infrastructure.advance_build(iid)
            se result.get("status") == "completed" entao:
                infra_completed = infra_completed + 1

        // 3. Treaty signing
        se random.random() < 0.3 e tamanho(nation_list) >= 2 entao:
            types = [
                ("River Basin Sharing", TreatyType.RESOURCE, "Co-manage transboundary water"),
                ("Forest Protection Pact", TreatyType.ECOLOGICAL, "Preserve shared forest ecosystem"),
                ("Research Exchange", TreatyType.SCIENTIFIC, "Share research findings freely"),
                ("Rail Link Agreement", TreatyType.INFRASTRUCTURE, "Connect rail networks"),
            ]
            desempacote name, ttype, desc = random.choice(types)
            desempacote n1, n2 = random.sample(nation_list, 2)
            tid = self.treaties.propose(name, ttype, desc, n1.nation_id)
            self.treaties.sign(tid, n2.nation_id)
            se random.random() < 0.5 e tamanho(nation_list) > 2 entao:
                n3 = random.choice([n para n em nation_list if n.nation_id nao in (n1.nation_id, n2.nation_id)])
                self.treaties.sign(tid, n3.nation_id)

        // 4. Federal proposals
        proposals = random.choice([0, 1, 1, 2])
        para cada _ em intervalo(proposals):
            cats = [
                ("Padronizar protocolo de comunicacao", "Adotar OpenProtocol em todas as nacoes",
                 FederalProposalCategory.STANDARD),
                ("Construir usina de fusao compartilhada", "ITER coletivo para energia ilimitada",
                 FederalProposalCategory.GRAND_PROJECT),
                ("Expandir rede ferroviaria continental", "Conectar todas as nacoes por trem de alta velocidade",
                 FederalProposalCategory.INFRASTRUCTURE),
                ("Tratado do oceano aberto", "Oceanos sao bem comum, pesca sustentavel obrigatoria",
                 FederalProposalCategory.TREATY),
                ("Programa de erradicacao de malaria", "Esforco conjunto para eliminar malaria",
                 FederalProposalCategory.GRAND_PROJECT),
            ]
            desempacote title, desc, cat = random.choice(cats)
            proposer = random.choice(nation_list)
            pid = self.federal_gov.submit(title, desc, cat, proposer.nation_id, self.current_cycle)

            // Each nation votes (simulated direct democracy)
            para cada n em nation_list:
                pop = n.metrics.population
                turnout = random.uniform(0.3, 0.7)
                voting_pop = pop * turnout
                support = random.uniform(0.4, 0.85)
                pop_for = voting_pop * support
                pop_against = voting_pop * (1 - support)
                self.federal_gov.vote_nation(pid, n.nation_id, pop_for, pop_against)

            result = self.federal_gov.close(pid, tamanho(nation_list))
            cycle_data.setdefault("federal_results", []).append(result)

        // 5. Grand project contributions
        para cada pid em list(self.grand_projects.projects.keys()):
            para cada n em random.sample(nation_list, minimo(2, tamanho(nation_list))):
                self.grand_projects.contribute(pid, n.nation_id, random.uniform(100, 500))

        cycle_data.update({
            "migrations": migrations,
            "infra_completed": infra_completed,
        })
        self.history.append(cycle_data)
        retorne cycle_data

    funcao full_report(self) -> texto:
        total_pop = self.total_population()
        infra_s = self.infrastructure.summary()
        mig_s = self.migration.flow_stats()
        treaty_s = self.treaties.summary()
        fed_s = self.federal_gov.summary()
        grand_s = self.grand_projects.summary()

        // Nation rankings
        nations_sorted = ordene(self.nations.values(),
                                key = (n) -> n.metrics.qol_index, reverse=verdadeiro)

        lines = [
            "=" * 70,
            "  {self.name.upper()} -- FEDERACAO DE NACOES OPENNATION",
            "  'Varias nacoes sem propriedade. Uma Republica de bens comuns.'",
            "=" * 70,
            "\n  NACOES MEMBROS: {len(self.nations)}",
            "  POPULACAO TOTAL: {total_pop:,}",
            "  CICLO ATUAL: {self.current_cycle}",
            "\n  {'Nacao':<20} {'Regiao':<12} {'Pop':>6} {'QoL':>5} {'Capac.':>7} {'Espec.':>20}",
            "  {'-'*75}",
        ]

        para cada n em nations_sorted:
            specs = n.specialties ? ", ".join(n.specialties[ : 2]) : "-"
            lines.append("  {n.name:<20} {n.region:<12} {n.metrics.population:>6} "
                        "{n.metrics.qol_index:>4.0f} {n.metrics.carrying_capacity:>7} {specs:>20}")

        lines.append("\n  INFRAESTRUTURA FEDERAL COMPARTILHADA:")
        para cada (k, v) em infra_s.items():
            se k != "by_type" entao:
                lines.append("    {k:<25} {v}")
        para cada (itype, data) em infra_s.get("by_type", {}).items():
            lines.append("    {itype:<25} {data['count']} projetos, "
                        "capacidade {data['total_capacity']:.0f}")

        lines.append("\n  MIGRACAO LIVRE:")
        para cada (k, v) em mig_s.items():
            lines.append("    {k:<25} {v}")

        lines.append("\n  TRATADOS INTER-NACOES:")
        para cada (k, v) em treaty_s.items():
            lines.append("    {k:<25} {v}")

        lines.append("\n  GOVERNANCA FEDERAL:")
        para cada (k, v) em fed_s.items():
            lines.append("    {k:<25} {v}")

        lines.append("\n  GRANDES PROJETOS:")
        para cada (k, v) em grand_s.items():
            lines.append("    {k:<25} {v}")
        para cada (pid, proj) em self.grand_projects.projects.items():
            p = self.grand_projects.progress(pid)
            lines.append("    {proj.name[:30]:<30} {p['status']:>12} "
                        "{p['labor_progress_pct']:>5.1f}% ({len(proj.contributing_nations)} nacoes)")

        lines.append("\n  PRINCIPIOS CONSTITUCIONAIS:")
        para cada (i, principle) em enumere(self.federal_gov.constitutional_principles, 1):
            lines.append("    {i}. {principle}")

        avg_qol = np.mean([n.metrics.qol_index para n em self.nations.values()])
        lines.append("\n  QoL MEDIO DA REPUBLICA: {avg_qol:.1f}/100")
        lines.append("  Nacoes em equilibrio: "
                    "{sum(1 for n in self.nations.values() if n.metrics.population <= n.metrics.carrying_capacity)}/"
                    "{len(self.nations)}")
        lines.append("\n{'=' * 70}")
        retorne "\n".join(lines)


// ============================================================================
// Simulator: Create a Republic with multiple Nations
// ============================================================================

funcao create_sample_republic() -> OpenRepublic:
    // Cria uma Republica com nacoes baseadas em biomas/culturas reais.
    republic = OpenRepublic("Republica dos Bens Comuns")

    // Create diverse nations
    nations_data = [
        ("N-AMAZON", "Amazonia", "America do Sul", "Floresta tropical, biodiversidade",
         ["Portugues", "Tukano", "Yanomami"], 50000, 20000, 600000, 5000000, 200000, 100, 20,
         ["biodiversidade", "botanica medicinal", "permacultura"]),
        ("N-ANDES", "Andes", "America do Sul", "Montanha, astronomia ancestral",
         ["Quechua", "Aymara", "Espanhol"], 35000, 12000, 420000, 3000000, 150000, 70, 15,
         ["astronomia", "engenharia hidraulica", "texteis"]),
        ("N-SAHEL", "Sahel", "Africa", "Transicao deserto-savana, energia solar",
         ["Wolof", "Hausa", "Francoes"], 40000, 15000, 480000, 8000000, 300000, 80, 12,
         ["energia solar", "agricultura seca", "musica"]),
        ("N-NORDIC", "Nordica", "Europa", "Floresta boreal, tecnologia limpa",
         ["Sami", "Nordico", "Ingles"], 30000, 10000, 360000, 2500000, 200000, 60, 25,
         ["computacao quantica", "energia eolica", "design"]),
        ("N-PACIFIC", "Pacifico", "Oceania", "Ilhas, oceanografia",
         ["Maori", "Havaiano", "Ingles"], 20000, 8000, 240000, 1500000, 500000, 40, 10,
         ["oceanografia", "energia das mars", "navegacao"]),
        ("N-HIMALAYA", "Himalaia", "Asia", "Alta altitude, espiritualidade",
         ["Tibetano", "Nepali", "Hindi"], 25000, 9000, 300000, 2000000, 100000, 50, 8,
         ["meditacao", "medicina tibetana", "montanhismo"]),
    ]

    para (nid, name, region, culture, langs, pop, housing, food, water,
         energy, health, edu, specs) in nations_data:
        nation = Nation(
            nation_id = nid, name=name, region=region, culture=culture,
            languages = langs, specialties=specs,
            metrics = NationMetrics(
                population = pop, housing_units=housing, food_kg_month=food,
                water_liters_day = water, energy_kwh_month=energy,
                healthcare_capacity = health, education_centers=edu,
                ecological_health = random.uniform(0.7, 0.95),
                commons_count = random.randint(15, 30),
            ))
        republic.admit_nation(nation)

    // Federal infrastructure
    republic.infrastructure.propose("Rede Eletrica Continental", InfrastructureType.ENERGY_GRID,
        "Grid inteligente conectando todas as nacoes com energia renovavel",
        50000000, "kWh/dia", 3, "N-ANDES")
    republic.infrastructure.propose("Ferrovia de Alta Velocidade", InfrastructureType.TRANSPORT_NET,
        "Trens magneticos conectando todas as nacoes por terra",
        50000, "km", 5, "N-NORDIC")
    republic.infrastructure.propose("Satelite OpenProtocol", InfrastructureType.COMMUNICATION,
        "Constelacao de satelites para comunicacao em OpenProtocol",
        99, "satelites", 4, "N-PACIFIC")
    republic.infrastructure.propose("Aqueduto Transcontinental", InfrastructureType.WATER_SYS,
        "Sistema de aquedutos ligando regioes com excesso e escassez de agua",
        1000000, "litros/dia", 6, "N-SAHEL")

    // Grand projects
    republic.grand_projects.propose(
        "Reator de Fusao Compartilhado", "ITER coletivo: energia ilimitada para todas as nacoes",
        4, 5000000, "Energia ilimitada para todas as nacoes membros")
    republic.grand_projects.propose(
        "Colonia Lunar", "Primeira colonia permanente na Lua, bem comum da Humanidade",
        5, 8000000, "Base para expansao espacial, mineracao de Helio-3")
    republic.grand_projects.propose(
        "Erradicacao de Doencas Tropicais", "Vacinas para malaria, dengue, Chagas, leishmaniose",
        3, 2000000, "Salvacao de milhoes de vidas")
    republic.grand_projects.propose(
        "Rede Quantica Global", "Distribuicao de entrelacamento quantico entre nacoes (QKD)",
        4, 3000000, "Comunicacao absolutamente segura")

    retorne republic


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    random.seed(42)
    np.random.seed(42)

    imprima("Criando Republica dos Bens Comuns com 6 nacoes...\n")

    republic = create_sample_republic()

    imprima("Nacoes fundadoras: {len(republic.nations)}")
    para cada (nid, n) em republic.nations.items():
        imprima("  {n.name:<15} ({n.region:<15}) pop={n.metrics.population:>6}  "
              "QoL={n.metrics.qol_index:.0f}  cap={n.metrics.carrying_capacity:>6}  "
              "especialidades: {', '.join(n.specialties[:2])}")

    // Run 12 cycles
    imprima("\nSimulando 12 ciclos...\n")
    para cada c em intervalo(12):
        result = republic.run_cycle()
        se c < 3 ou c >= 9 entao:
            imprima("  Ciclo {result['cycle']:2d}: migracoes={result.get('migrations',0):2d}  "
                  "infra_completas={result.get('infra_completed',0)}  "
                  "federal={len(result.get('federal_results',[]))}")
            para cada fr em result.get("federal_results", []):
                imprima("    -> {fr['proposal'][:45]:<45} {fr['result']}")

    imprima("\n{republic.full_report()}")

    // Show grand project progress
    imprima("\n  --- PROGRESSO DOS GRANDES PROJETOS ---")
    para cada (pid, proj) em republic.grand_projects.projects.items():
        p = republic.grand_projects.progress(pid)
        bar_len = inteiro(p["labor_progress_pct"] / 5)
        bar = "#" * bar_len + "." * (20 - bar_len)
        imprima("  {proj.name[:30]:<30} [{bar}] {p['labor_progress_pct']:>5.1f}%  "
              "({len(proj.contributing_nations)}/{proj.required_nations} nacoes)  {p['status']}")

```
