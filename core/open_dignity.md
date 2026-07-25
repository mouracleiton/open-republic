# OpenDignity -- Erradicacao da Pobreza e Moradores de Rua

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_dignity.py`

**Descricao:** ===========================================================
"Ninguem dorme na rua. Ninguem passa fome. Ninguem fica so.
 A Republica NAO aceita que seres humanos vivam como descartaveis.
 Cada pessoa e RESGATADA. Acolhida. Tratada. Restaurada."
O QUE ISTO FAZ:
  1. IDENTIFICACAO: mapeia TODA pessoa em situacao de rua
  2. RESGATE: abordagem ativa (a Republica vai ate elas)
  3. COLONIAS DE DIGNIDADE: moradia + comunidade + tratamento
  4. RESTAURACAO COMPLETA: saude, mental, adicao, oficio, ID
  5. REINTEGRACAO: volta a sociedade com dignidade
  6. PREVENCAO: ningém mais cai na rua
NAO E CARIDADE. E JUSTICA.
  Morador de rua nao e 'problema'. E FALHA do sistema.
  A Republica ASSUME essa falha e CORRIGE.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenDignity -- Erradicacao da Pobreza e Moradores de Rua
===========================================================

"Ninguem dorme na rua. Ninguem passa fome. Ninguem fica so.
 A Republica nao aceita que seres humanos vivam como descartaveis.
 Cada pessoa e RESGATADA. Acolhida. Tratada. Restaurada."

O QUE ISTO FAZ:
  1. IDENTIFICACAO: mapeia TODA pessoa em situacao de rua
  2. RESGATE: abordagem ativa (a Republica vai ate elas)
  3. COLONIAS DE DIGNIDADE: moradia + comunidade + tratamento
  4. RESTAURACAO COMPLETA: saude, mental, adicao, oficio, ID
  5. REINTEGRACAO: volta a sociedade com dignidade
  6. PREVENCAO: ningém mais cai na rua

nao e CARIDADE. e JUSTICA.
  Morador de rua nao e 'problema'. e FALHA do sistema.
  A Republica ASSUME essa falha e CORRIGE.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime


// ============================================================================
// 1. SITUACAO DE VULNERABILIDADE
// ============================================================================

classe VulnerabilityType herda de Enum:
    STREET = "rua"  // morador de rua
    EXTREME_POVERTY = "pobreza_extrema"  // sem recursos basicos
    HOMELESS_FAMILY = "familia_sem_teto"  // familia inteira
    ORPHAN = "orfao"  // crianca sem familia
    ELDERLY_ABANDONED = "idoso_abandonado"  // idoso sozinho
    ADDICTION_HOMELESS = "dependente_rua"  // vicio + rua
    MENTAL_HEALTH_HOMELESS = "saude_mental_rua"
    REFUGEE = "refugiado"
    DOMESTIC_VIOLENCE = "violencia_domestica"
    RECENTLY_RELEASED = "recem_liberado"  // ex-penitenciario sem moradia
    DISASTER_VICTIM = "vitima_desastre"  // enchente, incêndio
    CHILD_AT_RISK = "crianca_risco"  // crianca em perigo


classe NeedLevel herda de Enum:
    CRITICAL = 5 // vida em risco AGORA (fome, frio, doença)
    URGENT = 4 // precisa de moradia hoje
    HIGH = 3 // precisa de suporte esta semana
    MODERATE = 2 // precisa de suporte este mês
    STABLE = 1 // já recebendo ajuda, estabilizando
    INTEGRATED = 0 // reintegrado com sucesso


// ============================================================================
// 2. PESSOA EM VULNERABILIDADE
// ============================================================================

// decorador: @dataclass
classe VulnerablePerson:
    // Uma pessoa em situacao de vulnerabilidade.
    person_id: texto
    name: texto // pode ser desconhecido inicialmente
    age: inteiro
    vulnerability: VulnerabilityType
    location: texto // onde foi encontrada
    seja found_date: texto = ""
    seja need_level: NeedLevel = NeedLevel.CRITICAL

    // Condicao
    seja has_shelter: logico = falso
    seja has_food: logico = falso
    seja has_id: logico = falso
    seja has_healthcare: logico = falso
    seja has_family_contact: logico = falso
    seja has_addiction: logico = falso
    seja has_mental_health: logico = falso
    seja has_employment: logico = falso
    seja days_on_street: inteiro = 0

    // Historia (respeito -- cada pessoa tem uma historia)
    seja backstory: texto = ""

    // Plano
    seja assigned_colony: texto = ""
    seja assigned_mentor: texto = ""
    seja treatment_plan: [texto] = field(default_factory=list)
    seja skills_to_learn: [texto] = field(default_factory=list)

    // Progresso
    seja status: texto = "identificado"  // identificado, resgatado, em_colonia, reintegrado
    seja check_ins: [Dict] = field(default_factory=list)


// ============================================================================
// 3. COLONIA DE DIGNIDADE
// ============================================================================

classe ColonyType herda de Enum:
    GENERAL = "geral"  // adultos sem necessidades especiais
    FAMILY = "familia"  // familias com criancas
    ELDERLY = "idosos"  // idosos
    RECOVERY = "recuperacao"  // tratamento de adicao
    MENTAL_HEALTH = "saude_mental"  // suporte de saude mental
    YOUTH = "jovens"  // adolescentes e jovens
    WOMEN_CHILDREN = "mulheres_criancas"  // vitimas de violencia


// decorador: @dataclass
classe DignityColony:
    // Uma Colonia de Dignidade da Republica.

    nao e abrigo. nao e albergue. nao e institution.
    e uma COMUNIDADE onde pessoas vulneraveis:
    - Tem MORADIA permanente (nao temporaria)
    - Tem COMUNIDADE (nao isolamento)
    - Tem TRATAMENTO (se necessario)
    - Tem OFICIO (aprendem e trabalham)
    - Tem DIGNIDADE (sao cidadaos, nao 'casos')

    ESTRUTURA:
    - Casas individuais ou compartilhadas (OpenCivilConstruction)
    - Cozinha comunitaria (OpenTradition culinaria)
    - Espaco de saude (OpenHealth)
    - Espaco de aprendizado (OpenEducation + OpenTerminal)
    - Area de trabalho (FabLab / horta / oficina)
    - Espaco de convivencia (OpenNightLife comunitario)
    // 
    colony_id: texto
    name: texto
    colony_type: ColonyType
    location: texto
    seja capacity: inteiro = 100
    seja current_residents: inteiro = 0

    // Infraestrutura
    seja has_housing: logico = verdadeiro
    seja has_kitchen: logico = verdadeiro
    seja has_clinic: logico = verdadeiro
    seja has_school: logico = verdadeiro
    seja has_fablab: logico = falso
    seja has_garden: logico = verdadeiro // horta comunitaria
    seja has_terminal: logico = verdadeiro // OpenTerminal

    // Servicos
    seja medical_staff: inteiro = 2
    seja social_workers: inteiro = 3
    seja mentors: inteiro = 5
    seja security: texto = "comunitaria"  // nao policial -- OpenMartialArts

    // Progresso
    seja residents_integrated: inteiro = 0 // quantos ja se reintegraram
    seja avg_stay_months: flutuante = 0.0


// ============================================================================
// 4. MOTOR DE ERRADICACAO DA POBREZA
// ============================================================================

classe DignityEngine:
    // Motor que erradica pobreza extrema e moradores de rua.

    PROCESSO DE 5 FASES:

    FASE 1: MAPEAMENTO (procura ativa)
    - Equipes SAEM as ruas (nao esperam vir ate elas)
    - Identificam cada pessoa
    - Avaliam necessidades
    - Registram no sistema

    FASE 2: RESGATE IMEDIATO
    - Alimentacao AGORA
    - Abrigo AGORA (se frio/chuva/perigo)
    - Saude AGORA (se ferido/doente)
    - Sem espera. Sem fila. Sem burocracia.

    FASE 3: COLONIA DE DIGNIDADE
    - Transferencia para colonia adequada
    - Moradia propria
    - Tratamento (adicao, saude mental, fisica)
    - Alimentacao
    - ID nacional (se nao tiver)
    - Roupas (OpenKit)

    FASE 4: RESTAURACAO
    - Tratamento completo (OpenHealth nivel Sirio-Libanes)
    - Aprendizado de oficio (OpenEducation + OpenGamesRealistic)
    - Reconexao familiar (se possivel/desejado)
    - Saude mental (OpenPsychology sem rotular)
    - Tratamento de adicao (se necessario)

    FASE 5: REINTEGRACAO
    - Moradia permanente na comunidade
    - Trabalho garantido (OpenLaborRelay)
    - Comunidade de apoio
    - Mentor por 1 ano
    - Prontuario limpo (sem marcador de 'sem teto')

    SE ALGUEM VOLTA PARA RUA:
    - A Republica ASSUME a falha
    - Analisa o que faltou
    - Corrige o processo
    - NUNCA desiste da pessoa
    // 

    funcao __init__(self):
        self.persons: {texto: VulnerablePerson} = {}
        self.colonies: {texto: DignityColony} = {}
        self.stats_rescued: inteiro = 0
        self.stats_integrated: inteiro = 0
        self.stats_relapsed: inteiro = 0

    funcao register_colony(self, colony: DignityColony) -> None:
        self.colonies[colony.colony_id] = colony

    funcao identify_person(self, name: texto, age: inteiro,
                        vulnerability: VulnerabilityType,
                        location: texto,
                        seja addiction: logico = falso,
                        seja mental_health: logico = falso,
                        seja days_on_street: inteiro = 0,
                        seja backstory: texto = "") -> {texto: qualquer}:
        // Fase 1: identificar pessoa em vulnerabilidade.
        pid = hashlib.md5("{name}{age}{location}{datetime.now()}".encode()).hexdigest()[:8]
        person = VulnerablePerson(
            person_id = pid, name=name  ou  "Desconhecido-{pid[:4]}",
            age = age, vulnerability=vulnerability, location=location,
            need_level = NeedLevel.CRITICAL,
            has_addiction = addiction, has_mental_health=mental_health,
            days_on_street = days_on_street, backstory=backstory,
            found_date = datetime.now().isoformat(),
        )
        self.persons[pid] = person
        retorne {
            "identified": verdadeiro,
            "person_id": pid,
            "name": person.name,
            "vulnerability": vulnerability.value,
            "need_level": person.need_level.name,
            "message": (
                "Pessoa identificada: {person.name}, {age} anos. "
                "Resgate IMEDIATO necessario."
            ),
        }

    funcao immediate_rescue(self, person_id: texto) -> {texto: qualquer}:
        // Fase 2: resgate imediato -- comer, abrigar, tratar AGORA.
        person = self.persons.get(person_id)
        se nao person entao:
            retorne {"error": "Pessoa nao encontrada"}

        person.has_food = verdadeiro
        person.has_shelter = verdadeiro // abrigo emergencial
        person.has_healthcare = verdadeiro
        person.status = "resgatado"
        person.need_level = NeedLevel.URGENT
        self.stats_rescued += 1

        retorne {
            "rescued": verdadeiro,
            "person": person.name,
            "provided_immediately": [
                "Alimentacao AGORA (OpenCredit + restaurante comunitario)",
                "Abrigo AGORA (protecao de frio/chuva/perigo)",
                "Saude AGORA (avaliacao medica imediata)",
                "Roupas AGORA (OpenKit basico)",
                "Higiene AGORA (banho, produtos)",
            ],
            "message": (
                "{person.name} foi resgatado. Comeu. Tomou banho. "
                "Foi examinado. Tem abrigo hoje. "
                "Nunca mais vai dormir com fome ou frio."
            ),
        }

    funcao assign_to_colony(self, person_id: texto) -> {texto: qualquer}:
        // Fase 3: transferir para Colonia de Dignidade.
        person = self.persons.get(person_id)
        se nao person entao:
            retorne {"error": "Pessoa nao encontrada"}

        // Determinar tipo de colonia
        se person.has_addiction entao:
            colony_type = ColonyType.RECOVERY
        senao se person.has_mental_health entao:
            colony_type = ColonyType.MENTAL_HEALTH
        senao se person.age >= 65 entao:
            colony_type = ColonyType.ELDERLY
        senao se person.age < 18 entao:
            colony_type = ColonyType.YOUTH
        senao se person.vulnerability == VulnerabilityType.DOMESTIC_VIOLENCE entao:
            colony_type = ColonyType.WOMEN_CHILDREN
        senao se person.vulnerability == VulnerabilityType.HOMELESS_FAMILY entao:
            colony_type = ColonyType.FAMILY
        senao:
            colony_type = ColonyType.GENERAL

        // Encontrar colonia disponivel
        suitable = [c para c em self.colonies.values()
                    if c.colony_type == colony_type
                     e c.current_residents < c.capacity]
        se nao suitable entao:
            // Qualquer colonia com espaco
            suitable = [c para c em self.colonies.values()
                        if c.current_residents < c.capacity]

        se nao suitable entao:
            retorne {"error": "Nenhuma colonia com vagas. EXPANDIR AGORA."}

        colony = suitable[0]
        colony.current_residents += 1
        person.assigned_colony = colony.name
        person.has_shelter = verdadeiro // moradia permanente agora
        person.status = "em_colonia"
        person.need_level = NeedLevel.HIGH

        // Plano de tratamento
        se person.has_addiction entao:
            person.treatment_plan.append("desintoxicacao_12_meses")
            person.treatment_plan.append("grupo_apoio_diario")
        se person.has_mental_health entao:
            person.treatment_plan.append("terapia_semanal")
            person.treatment_plan.append("medicacao_se_necessario")
        person.treatment_plan.append("avaliacao_saude_completa")

        // Skills
        person.skills_to_learn = ["letramento_digital",
                                  "cooperacao_comunitaria"]
        se colony.has_garden entao:
            person.skills_to_learn.append("agricultura_urbana")
        se colony.has_fablab entao:
            person.skills_to_learn.append("programacao_basica")

        retorne {
            "assigned": verdadeiro,
            "person": person.name,
            "colony": colony.name,
            "colony_type": colony.colony_type.value,
            "housing": "Moradia individual na colonia",
            "treatment": person.treatment_plan,
            "skills": person.skills_to_learn,
            "services": [
                "Moradia permanente",
                "Alimentacao 3x/dia",
                "Saude (nivel Sirio-Libanes)",
                "Tratamento de adicao (se necessario)",
                "Saude mental (OpenPsychology)",
                "OpenKit (roupas, ID, smartphone)",
                "OpenTerminal (acesso digital)",
                "Mentor (1 ano)",
            ],
            "message": (
                "{person.name} agora mora na {colony.name}. "
                "Tem casa. Tem comida. Tem tratamento. "
                "Tem comunidade. Tem dignidade."
            ),
        }

    funcao restore(self, person_id: texto) -> {texto: qualquer}:
        // Fase 4: restauracao completa.
        person = self.persons.get(person_id)
        se nao person entao:
            retorne {"error": "nao encontrada"}

        // Simular progresso
        person.has_id = verdadeiro
        person.has_family_contact = verdadeiro
        person.has_employment = falso // ainda nao
        person.need_level = NeedLevel.MODERATE
        person.status = "restaurando"

        retorne {
            "person": person.name,
            "progress": {
                "moradia": "GARANTIDA",
                "alimentacao": "GARANTIDA",
                "saude": "EM TRATAMENTO",
                "id": "FORNECIDA",
                "familia": "CONTATADA (se desejado)",
                "oficio": "EM APRENDIZADO",
                "tratamento": "EM ANDAMENTO",
            },
            "message": "{person.name} esta em restauracao. Leva tempo. Mas acontece.",
        }

    funcao reintegrate(self, person_id: texto) -> {texto: qualquer}:
        // Fase 5: reintegracao completa.
        person = self.persons.get(person_id)
        se nao person entao:
            retorne {"error": "nao encontrada"}

        person.has_employment = verdadeiro
        person.need_level = NeedLevel.INTEGRATED
        person.status = "reintegrado"
        self.stats_integrated += 1

        // Remover da colonia (moradia propria na comunidade)
        colony = next((c para c em self.colonies.values()
                       if c.name == person.assigned_colony), nulo)
        se colony entao:
            colony.current_residents = maximo(0, colony.current_residents - 1)
            colony.residents_integrated += 1

        retorne {
            "person": person.name,
            "status": "REINTEGRADO",
            "housing": "Moradia propria na comunidade",
            "employment": "Trabalho garantido (OpenLaborRelay)",
            "record": "PRONTUARIO LIMPO (sem marcador de sem-teto)",
            "mentor": "Acompanhamento de 1 ano",
            "message": (
                "{person.name} voltou a ser CIDADAO. "
                "Tem casa. Tem trabalho. Tem comunidade. "
                "Tem dignidade. Nunca mais na rua."
            ),
        }

    funcao report_relapse(self, person_id: texto, reason: texto) -> {texto: qualquer}:
        // Se voltou para rua -- FALHA DO SISTEMA.
        person = self.persons.get(person_id)
        se nao person entao:
            retorne {"error": "nao encontrada"}

        person.status = "recada"
        person.need_level = NeedLevel.URGENT
        self.stats_relapsed += 1

        retorne {
            "person": person.name,
            "relapsed": verdadeiro,
            "reason": reason,
            "system_failure": (
                "A Republica ASSUME a falha. Algo faltou. "
                "Nao e culpa da pessoa. Recomecar o processo. "
                "NUNCA desistir."
            ),
            "action": "Reabrir plano. Corrigir o que falhou. Recomecar.",
        }

    funcao stats(self) -> {texto: qualquer}:
        total = tamanho(self.persons)
        by_vuln = Counter(p.vulnerability.value para p em self.persons.values())
        by_status = Counter(p.status para p em self.persons.values())
        retorne {
            "total_identified": total,
            "total_rescued": self.stats_rescued,
            "total_integrated": self.stats_integrated,
            "total_relapsed": self.stats_relapsed,
            "success_rate": (
                "{self.stats_integrated}/{self.stats_rescued} "
                "({self.stats_integrated/max(self.stats_rescued,1)*100:.0f}%)"
            ),
            "by_vulnerability": dict(by_vuln),
            "by_status": dict(by_status),
            "colonies": tamanho(self.colonies),
            "colony_capacity": soma(c.capacity para c em self.colonies.values()),
            "colony_residents": soma(c.current_residents para c em self.colonies.values()),
        }


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = DignityEngine()

    imprima("=" * 80)
    imprima("  OPENDIGNITY -- ERRADICACAO DA POBREZA E MORADORES DE RUA")
    imprima("  Ninguem dorme na rua. Ninguem passa fome. Nunca mais.")
    imprima("=" * 80)

    // === 1. COLONIAS DE DIGNIDADE ===
    imprima("\n\n  === 1. COLONIAS DE DIGNIDADE ===\n")

    colonies_data = [
        DignityColony("COL-01", "Colonia Esperanca", ColonyType.GENERAL,
                      "Centro", capacity=100),
        DignityColony("COL-02", "Colonia Recuperacao", ColonyType.RECOVERY,
                      "Zona Rural", capacity=80, has_fablab=verdadeiro),
        DignityColony("COL-03", "Colonia FamiliA", ColonyType.FAMILY,
                      "Zona Sul", capacity=60),
        DignityColony("COL-04", "Colonia Idosos", ColonyType.ELDERLY,
                      "Centro", capacity=50),
        DignityColony("COL-05", "Colonia Mulheres", ColonyType.WOMEN_CHILDREN,
                      "Local seguro", capacity=40),
        DignityColony("COL-06", "Colonia Jovens", ColonyType.YOUTH,
                      "Centro", capacity=30, has_fablab=verdadeiro),
    ]

    para cada c em colonies_data:
        engine.register_colony(c)
        imprima("  [{c.colony_id}] {c.name:<30} {c.colony_type.value:<20} "
              "capacidade: {c.capacity}")

    // === 2. IDENTIFICAR PESSOAS EM SITUACAO DE RUA ===
    imprima("\n\n  === 2. MAPEAMENTO DE PESSOAS EM SITUACAO DE RUA ===\n")

    persons_data = [
        ("Jose", 55, VulnerabilityType.STREET, "Praca da Se", falso, verdadeiro,
         730, "Perdeu emprego, familia se desfez, alcool"),
        ("Maria (gravida)", 24, VulnerabilityType.HOMELESS_FAMILY,
         "Estacao rodoviaria", falso, falso, 60, "Fugiu de violencia domestica"),
        ("Joaozinho (8)", 8, VulnerabilityType.ORPHAN,
         "Semaforo", falso, falso, 365, "Orfão, mora na rua desde os 7"),
        ("Dona Rita", 72, VulnerabilityType.ELDERLY_ABANDONED,
         "Portao de hospital", falso, verdadeiro, 180, "Familia a abandonou"),
        ("Carlos", 40, VulnerabilityType.ADDICTION_HOMELESS,
         "Cracolandia", verdadeiro, verdadeiro, 1095, "Dependencia crack ha 5 anos"),
        ("Ana", 30, VulnerabilityType.MENTAL_HEALTH_HOMELESS,
         "Praca", falso, verdadeiro, 540, "Esquizofrenia nao tratada"),
        ("Familia Santos (4 pessoas)", 0, VulnerabilityType.HOMELESS_FAMILY,
         "Ocupacao", falso, falso, 90, "Despejo, perdeu casa"),
        ("Pedro", 19, VulnerabilityType.RECENTLY_RELEASED,
         "Portao da prisao", falso, falso, 1, "Saiu da prisao sem moradia"),
        ("Aisha", 28, VulnerabilityType.REFUGEE,
         "Centro de refugiados", falso, falso, 30, "Refugiada de guerra"),
        ("Beto", 45, VulnerabilityType.DISASTER_VICTIM,
         "Abrigo temporario", falso, falso, 7, "Perdeu tudo em enchente"),
    ]

    para name, age, vuln, loc, addic, mental, days, story in persons_data:
        result = engine.identify_person(name, age, vuln, loc, addic, mental,
                                        days, story)
        imprima("  [{result['person_id']}] {result['name']:<25} "
              "{vuln.value:<25} {loc}")

    // === 3. RESGATE IMEDIATO ===
    imprima("\n\n  === 3. RESGATE IMEDIATO (comer + abrigo + saude) ===\n")
    para cada pid em list(engine.persons.keys()):
        result = engine.immediate_rescue(pid)
        se result.get("rescued") entao:
            imprima("  {result['person']:<25} -> RESGATADO (comeu, abrigo, saude)")

    // === 4. TRANSFERENCIA PARA COLONIAS ===
    imprima("\n\n  === 4. COLONIA DE DIGNIDADE ===\n")
    para cada pid em list(engine.persons.keys()):
        result = engine.assign_to_colony(pid)
        se result.get("assigned") entao:
            imprima("\n  {result['person']:<25} -> {result['colony']}")
            imprima("    Moradia: {result['housing']}")
            se result['treatment'] entao:
                imprima("    Tratamento: {', '.join(result['treatment'][:3])}")
            imprima("    Skills: {', '.join(result['skills'][:3])}")

    // === 5. RESTAURACAO ===
    imprima("\n\n  === 5. RESTAURACAO (tempo, tratamento, oficio) ===\n")
    para cada pid em list(engine.persons.keys())[:5]:
        result = engine.restore(pid)
        se "person" in result entao:
            imprima("  {result['person']:<25} -> {result['message']}")

    // === 6. REINTEGRACAO ===
    imprima("\n\n  === 6. REINTEGRACAO (primeiros casos) ===\n")
    para cada pid em list(engine.persons.keys())[:3]:
        result = engine.reintegrate(pid)
        se result.get("status") == "REINTEGRADO" entao:
            imprima("\n  {result['person']:<25} -> {result['status']}")
            imprima("    {result['housing']}")
            imprima("    {result['employment']}")
            imprima("    {result['record']}")
            imprima("    {result['message']}")

    // === 7. CASO DE RECAIDA ===
    imprima("\n\n  === 7. RECAIDA = FALHA DO SISTEMA ===\n")
    se tamanho(engine.persons) > 5 entao:
        pids = list(engine.persons.keys())
        result = engine.report_relapse(pids[5], "Tratamento de adicao incompleto")
        imprima("  {result['person']} voltou para rua.")
        imprima("  Motivo: {result['reason']}")
        imprima("  {result['system_failure']}")

    // === 8. STATS ===
    imprima("\n\n  === 8. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DO OPENDIGNITY")
    imprima("{'='*80}")
    imprima("""
  A REPUBLICA nao ACEITA:
    - Ser humano dormindo na rua
    - Ser humano passando fome
    - Ser humano sem banho
    - Ser humano sem tratamento
    - Ser humano sem dignidade

  O PROCESSO (5 fases):
    1. MAPEAMENTO: Republica vai as ruas PROCURAR (nao espera vir)
    2. RESGATE: comer + abrigo + saude AGORA (sem fila)
    3. COLONIA: moradia + comunidade + tratamento
    4. RESTAURACAO: saude + oficio + familia (leva tempo)
    5. REINTEGRACAO: moradia propria + trabalho + mentor

  COLONIAS DE DIGNIDADE:
    nao sao abrigos. nao sao instituicoes.
    Sao COMUNIDADES onde pessoas se restauram.
    - Casa propria (OpenCivilConstruction)
    - Cozinha comunitaria
    - Clinica (OpenHealth Sirio-Libanes)
    - Escola (OpenEducation)
    - FabLab/Horta (trabalho + skills)
    - OpenTerminal (acesso digital)
    - Tratamento (adicao, mental, fisica)

  CADA PESSOA RECEBE:
    - Moradia PERMANENTE (nao temporaria)
    - Comida 3x/dia (direito)
    - Saude completa (Sirio-Libanes)
    - Tratamento de adicao (se necessario)
    - Saude mental (OpenPsychology sem rotular)
    - OpenKit completo (smartphone, ID, roupas)
    - Oficio (aprende, trabalha)
    - Mentor (1 ano)
    - Comunidade (nao sozinho)
    - ID nova (sem marcador)
    - Prontuario limpo (sem estigma)

  SE VOLTA PARA RUA:
    - FALHA DO SISTEMA (nao da pessoa)
    - Republica NUNCA desiste
    - Recomeca o processo
    - Corrige o que falhou

  PRINCIPIOS:
    P1: Pobreza nao e culpa. e falha do sistema. Republica corrige.
    P2: Corpo protegido. Moradia e direito. Fome e violencia.
    seja P3: Restauracao = trabalho de todos (medicos, mentores, construtores).
    P4: Colonias geridas democraticamente. Residentes participam.
// )
    imprima("{'='*80}")
    imprima("  OpenDignity: {s['total_identified']} pessoas mapeadas, "
          "{s['total_rescued']} resgatadas, "
          "{s['total_integrated']} reintegradas.")
    imprima("  Ninguem na rua. Nunca mais.")
    imprima("{'='*80}")

```
