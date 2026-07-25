#!/usr/bin/env python3
"""
OpenDignity -- Erradicacao da Pobreza e Moradores de Rua -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenDignity -- Erradicacao da Pobreza and Moradores de Rua
===========================================================
"Ninguem dorme na rua. Ninguem passa fome. Ninguem fica so.
A Republica not aceita que seres humanos vivam como descartaveis.
Cada pessoa and RESGATADA. Acolhida. Tratada. Restaurada."
O QUE ISTO FAZ:
1. IDENTIFICACAO: mapeia TODA pessoa em situacao de rua
2. RESGATE: abordagem ativa (a Republica vai ate elas)
3. COLONIAS DE DIGNIDADE: moradia + comunidade + tratamento
4. RESTAURACAO COMPLETA: saude, mental, adicao, oficio, ID
5. REINTEGRACAO: volta a sociedade com dignidade
6. PREVENCAO: ningém mais cai na rua
not and CARIDADE. and JUSTICA.
Morador de rua not and 'problema'. and FALHA do sistema.
A Republica ASSUME essa falha and CORRIGE.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa random
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict, Counter de collections
# importa datetime de datetime
# ============================================================================
# 1. SITUACAO DE VULNERABILIDADE
# ============================================================================
class VulnerabilityType(Enum):
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
class NeedLevel(Enum):
    CRITICAL = 5 // vida em risco AGORA (fome, frio, doença)
    URGENT = 4 // precisa de moradia hoje
    HIGH = 3 // precisa de suporte esta semana
    MODERATE = 2 // precisa de suporte este mês
    STABLE = 1 // já recebendo ajuda, estabilizando
    INTEGRATED = 0 // reintegrado com sucesso
# ============================================================================
# 2. PESSOA EM VULNERABILIDADE
# ============================================================================
# decorador: @dataclass
class VulnerablePerson:
    # Uma pessoa em situacao de vulnerabilidade.
    person_id: texto
    name: texto // pode ser desconhecido inicialmente
    age: inteiro
    vulnerability: VulnerabilityType
    location: texto // onde foi encontrada
    found_date: str = ""
    need_level: NeedLevel = NeedLevel.CRITICAL
    # Condicao
    has_shelter: bool = False
    has_food: bool = False
    has_id: bool = False
    has_healthcare: bool = False
    has_family_contact: bool = False
    has_addiction: bool = False
    has_mental_health: bool = False
    has_employment: bool = False
    days_on_street: int = 0
    # Historia (respeito -- cada pessoa tem uma historia)
    backstory: str = ""
    # Plano
    assigned_colony: str = ""
    assigned_mentor: str = ""
    treatment_plan: [texto] = field(default_factory=list)
    skills_to_learn: [texto] = field(default_factory=list)
    # Progresso
    status: str = "identificado"  // identificado, resgatado, em_colonia, reintegrado
    check_ins: [Dict] = field(default_factory=list)
# ============================================================================
# 3. COLONIA DE DIGNIDADE
# ============================================================================
class ColonyType(Enum):
    GENERAL = "geral"  // adultos sem necessidades especiais
    FAMILY = "familia"  // familias com criancas
    ELDERLY = "idosos"  // idosos
    RECOVERY = "recuperacao"  // tratamento de adicao
    MENTAL_HEALTH = "saude_mental"  // suporte de saude mental
    YOUTH = "jovens"  // adolescentes and jovens
    WOMEN_CHILDREN = "mulheres_criancas"  // vitimas de violencia
# decorador: @dataclass
class DignityColony:
    # Uma Colonia de Dignidade da Republica.
    not and abrigo. not and albergue. not and institution.
    and uma COMUNIDADE onde pessoas vulneraveis:
    - Tem MORADIA permanente (not temporaria)
    - Tem COMUNIDADE (not isolamento)
    - Tem TRATAMENTO (se necessario)
    - Tem OFICIO (aprendem and trabalham)
    - Tem DIGNIDADE (sao cidadaos, not 'casos')
    ESTRUTURA:
    - Casas individuais or compartilhadas (OpenCivilConstruction)
    - Cozinha comunitaria (OpenTradition culinaria)
    - Espaco de saude (OpenHealth)
    - Espaco de aprendizado (OpenEducation + OpenTerminal)
    - Area de trabalho (FabLab / horta / oficina)
    - Espaco de convivencia (OpenNightLife comunitario)
    # 
    colony_id: texto
    name: texto
    colony_type: ColonyType
    location: texto
    capacity: int = 100
    current_residents: int = 0
    # Infraestrutura
    has_housing: bool = True
    has_kitchen: bool = True
    has_clinic: bool = True
    has_school: bool = True
    has_fablab: bool = False
    has_garden: bool = True // horta comunitaria
    has_terminal: bool = True // OpenTerminal
    # Servicos
    medical_staff: int = 2
    social_workers: int = 3
    mentors: int = 5
    security: str = "comunitaria"  // not policial -- OpenMartialArts
    # Progresso
    residents_integrated: int = 0 // quantos ja se reintegraram
    avg_stay_months: float = 0.0
# ============================================================================
# 4. MOTOR DE ERRADICACAO DA POBREZA
# ============================================================================
class DignityEngine:
    # Motor que erradica pobreza extrema e moradores de rua.
    PROCESSO DE 5 FASES:
    FASE 1: MAPEAMENTO (procura ativa)
    - Equipes SAEM as ruas (not esperam vir ate elas)
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
    - ID nacional (se not tiver)
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
    # 
    def __init__(self):
        self.persons: {texto: VulnerablePerson} = {}
        self.colonies: {texto: DignityColony} = {}
        self.stats_rescued: inteiro = 0
        self.stats_integrated: inteiro = 0
        self.stats_relapsed: inteiro = 0
    def register_colony(self, colony: DignityColony) -> None:
        self.colonies[colony.colony_id] = colony
    funcao identify_person(self, name: texto, age: inteiro,
                        vulnerability: VulnerabilityType,
                        location: texto,
                        addiction: bool = False,
                        mental_health: bool = False,
                        days_on_street: int = 0,
                        backstory: str = "") -> {texto: qualquer}:
        # Fase 1: identificar pessoa em vulnerabilidade.
        pid = hashlib.md5("{name}{age}{location}{datetime.now()}".encode()).hexdigest()[:8]
        person = VulnerablePerson(
            person_id = pid, name=name  or  "Desconhecido-{pid[:4]}",
            age = age, vulnerability=vulnerability, location=location,
            need_level = NeedLevel.CRITICAL,
            has_addiction = addiction, has_mental_health=mental_health,
            days_on_street = days_on_street, backstory=backstory,
            found_date = datetime.now().isoformat(),
        )
        self.persons[pid] = person
        return {
            "identified": True,
            "person_id": pid,
            "name": person.name,
            "vulnerability": vulnerability.value,
            "need_level": person.need_level.name,
            "message": (
                "Pessoa identificada: {person.name}, {age} anos. "
                "Resgate IMEDIATO necessario."
            ),
        }
    def immediate_rescue(self, person_id: texto) -> {texto: qualquer}:
        # Fase 2: resgate imediato -- comer, abrigar, tratar AGORA.
        person = self.persons.get(person_id)
        if not person:
            return {"error": "Pessoa not encontrada"}
        person.has_food = True
        person.has_shelter = True // abrigo emergencial
        person.has_healthcare = True
        person.status = "resgatado"
        person.need_level = NeedLevel.URGENT
        self.stats_rescued += 1
        return {
            "rescued": True,
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
                "Nunca mais vai dormir com fome or frio."
            ),
        }
    def assign_to_colony(self, person_id: texto) -> {texto: qualquer}:
        # Fase 3: transferir para Colonia de Dignidade.
        person = self.persons.get(person_id)
        if not person:
            return {"error": "Pessoa not encontrada"}
        # Determinar tipo de colonia
        if person.has_addiction:
            colony_type = ColonyType.RECOVERY
        elif person.has_mental_health:
            colony_type = ColonyType.MENTAL_HEALTH
        elif person.age >= 65:
            colony_type = ColonyType.ELDERLY
        elif person.age < 18:
            colony_type = ColonyType.YOUTH
        elif person.vulnerability == VulnerabilityType.DOMESTIC_VIOLENCE:
            colony_type = ColonyType.WOMEN_CHILDREN
        elif person.vulnerability == VulnerabilityType.HOMELESS_FAMILY:
            colony_type = ColonyType.FAMILY
        else:
            colony_type = ColonyType.GENERAL
        # Encontrar colonia disponivel
        suitable = [c para c em self.colonies.values()
                    if c.colony_type == colony_type
                    and c.current_residents < c.capacity]
        if not suitable:
            # Qualquer colonia com espaco
            suitable = [c para c em self.colonies.values()
                        if c.current_residents < c.capacity]
        if not suitable:
            return {"error": "Nenhuma colonia com vagas. EXPANDIR AGORA."}
        colony = suitable[0]
        colony.current_residents += 1
        person.assigned_colony = colony.name
        person.has_shelter = True // moradia permanente agora
        person.status = "em_colonia"
        person.need_level = NeedLevel.HIGH
        # Plano de tratamento
        if person.has_addiction:
            person.treatment_plan.append("desintoxicacao_12_meses")
            person.treatment_plan.append("grupo_apoio_diario")
        if person.has_mental_health:
            person.treatment_plan.append("terapia_semanal")
            person.treatment_plan.append("medicacao_se_necessario")
        person.treatment_plan.append("avaliacao_saude_completa")
        # Skills
        person.skills_to_learn = ["letramento_digital",
                                "cooperacao_comunitaria"]
        if colony.has_garden:
            person.skills_to_learn.append("agricultura_urbana")
        if colony.has_fablab:
            person.skills_to_learn.append("programacao_basica")
        return {
            "assigned": True,
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
    def restore(self, person_id: texto) -> {texto: qualquer}:
        # Fase 4: restauracao completa.
        person = self.persons.get(person_id)
        if not person:
            return {"error": "not encontrada"}
        # Simular progresso
        person.has_id = True
        person.has_family_contact = True
        person.has_employment = False // ainda not
        person.need_level = NeedLevel.MODERATE
        person.status = "restaurando"
        return {
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
    def reintegrate(self, person_id: texto) -> {texto: qualquer}:
        # Fase 5: reintegracao completa.
        person = self.persons.get(person_id)
        if not person:
            return {"error": "not encontrada"}
        person.has_employment = True
        person.need_level = NeedLevel.INTEGRATED
        person.status = "reintegrado"
        self.stats_integrated += 1
        # Remover da colonia (moradia propria na comunidade)
        colony = next((c para c em self.colonies.values()
                    if c.name == person.assigned_colony), None)
        if colony:
            colony.current_residents = max(0, colony.current_residents - 1)
            colony.residents_integrated += 1
        return {
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
    def report_relapse(self, person_id: texto, reason: texto) -> {texto: qualquer}:
        # Se voltou para rua -- FALHA DO SISTEMA.
        person = self.persons.get(person_id)
        if not person:
            return {"error": "not encontrada"}
        person.status = "recada"
        person.need_level = NeedLevel.URGENT
        self.stats_relapsed += 1
        return {
            "person": person.name,
            "relapsed": True,
            "reason": reason,
            "system_failure": (
                "A Republica ASSUME a falha. Algo faltou. "
                "Nao and culpa da pessoa. Recomecar o processo. "
                "NUNCA desistir."
            ),
            "action": "Reabrir plano. Corrigir o que falhou. Recomecar.",
        }
    def stats(self) -> {texto: qualquer}:
        total = len(self.persons)
        by_vuln = Counter(p.vulnerability.value para p em self.persons.values())
        by_status = Counter(p.status para p em self.persons.values())
        return {
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
            "colonies": len(self.colonies),
            "colony_capacity": sum(c.capacity para c em self.colonies.values()),
            "colony_residents": sum(c.current_residents para c em self.colonies.values()),
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = DignityEngine()
    print("=" * 80)
    print("  OPENDIGNITY -- ERRADICACAO DA POBREZA E MORADORES DE RUA")
    print("  Ninguem dorme na rua. Ninguem passa fome. Nunca mais.")
    print("=" * 80)
    # === 1. COLONIAS DE DIGNIDADE ===
    print("\n\n  === 1. COLONIAS DE DIGNIDADE ===\n")
    colonies_data = [
        DignityColony("COL-01", "Colonia Esperanca", ColonyType.GENERAL,
                    "Centro", capacity=100),
        DignityColony("COL-02", "Colonia Recuperacao", ColonyType.RECOVERY,
                    "Zona Rural", capacity=80, has_fablab=True),
        DignityColony("COL-03", "Colonia FamiliA", ColonyType.FAMILY,
                    "Zona Sul", capacity=60),
        DignityColony("COL-04", "Colonia Idosos", ColonyType.ELDERLY,
                    "Centro", capacity=50),
        DignityColony("COL-05", "Colonia Mulheres", ColonyType.WOMEN_CHILDREN,
                    "Local seguro", capacity=40),
        DignityColony("COL-06", "Colonia Jovens", ColonyType.YOUTH,
                    "Centro", capacity=30, has_fablab=True),
    ]
    for c in colonies_data:
        engine.register_colony(c)
        print("  [{c.colony_id}] {c.name:<30} {c.colony_type.value:<20} "
            "capacidade: {c.capacity}")
    # === 2. IDENTIFICAR PESSOAS EM SITUACAO DE RUA ===
    print("\n\n  === 2. MAPEAMENTO DE PESSOAS EM SITUACAO DE RUA ===\n")
    persons_data = [
        ("Jose", 55, VulnerabilityType.STREET, "Praca da Se", False, True,
        730, "Perdeu emprego, familia se desfez, alcool"),
        ("Maria (gravida)", 24, VulnerabilityType.HOMELESS_FAMILY,
        "Estacao rodoviaria", False, False, 60, "Fugiu de violencia domestica"),
        ("Joaozinho (8)", 8, VulnerabilityType.ORPHAN,
        "Semaforo", False, False, 365, "Orfão, mora na rua desde os 7"),
        ("Dona Rita", 72, VulnerabilityType.ELDERLY_ABANDONED,
        "Portao de hospital", False, True, 180, "Familia a abandonou"),
        ("Carlos", 40, VulnerabilityType.ADDICTION_HOMELESS,
        "Cracolandia", True, True, 1095, "Dependencia crack ha 5 anos"),
        ("Ana", 30, VulnerabilityType.MENTAL_HEALTH_HOMELESS,
        "Praca", False, True, 540, "Esquizofrenia not tratada"),
        ("Familia Santos (4 pessoas)", 0, VulnerabilityType.HOMELESS_FAMILY,
        "Ocupacao", False, False, 90, "Despejo, perdeu casa"),
        ("Pedro", 19, VulnerabilityType.RECENTLY_RELEASED,
        "Portao da prisao", False, False, 1, "Saiu da prisao sem moradia"),
        ("Aisha", 28, VulnerabilityType.REFUGEE,
        "Centro de refugiados", False, False, 30, "Refugiada de guerra"),
        ("Beto", 45, VulnerabilityType.DISASTER_VICTIM,
        "Abrigo temporario", False, False, 7, "Perdeu tudo em enchente"),
    ]
    para name, age, vuln, loc, addic, mental, days, story in persons_data:
        result = engine.identify_person(name, age, vuln, loc, addic, mental,
                                        days, story)
        print("  [{result['person_id']}] {result['name']:<25} "
            "{vuln.value:<25} {loc}")
    # === 3. RESGATE IMEDIATO ===
    print("\n\n  === 3. RESGATE IMEDIATO (comer + abrigo + saude) ===\n")
    for pid in list(engine.persons.keys()):
        result = engine.immediate_rescue(pid)
        if result.get("rescued"):
            print("  {result['person']:<25} -> RESGATADO (comeu, abrigo, saude)")
    # === 4. TRANSFERENCIA PARA COLONIAS ===
    print("\n\n  === 4. COLONIA DE DIGNIDADE ===\n")
    for pid in list(engine.persons.keys()):
        result = engine.assign_to_colony(pid)
        if result.get("assigned"):
            print("\n  {result['person']:<25} -> {result['colony']}")
            print("    Moradia: {result['housing']}")
            if result['treatment']:
                print("    Tratamento: {', '.join(result['treatment'][:3])}")
            print("    Skills: {', '.join(result['skills'][:3])}")
    # === 5. RESTAURACAO ===
    print("\n\n  === 5. RESTAURACAO (tempo, tratamento, oficio) ===\n")
    for pid in list(engine.persons.keys())[:5]:
        result = engine.restore(pid)
        if "person" in result:
            print("  {result['person']:<25} -> {result['message']}")
    # === 6. REINTEGRACAO ===
    print("\n\n  === 6. REINTEGRACAO (primeiros casos) ===\n")
    for pid in list(engine.persons.keys())[:3]:
        result = engine.reintegrate(pid)
        if result.get("status") == "REINTEGRADO":
            print("\n  {result['person']:<25} -> {result['status']}")
            print("    {result['housing']}")
            print("    {result['employment']}")
            print("    {result['record']}")
            print("    {result['message']}")
    # === 7. CASO DE RECAIDA ===
    print("\n\n  === 7. RECAIDA = FALHA DO SISTEMA ===\n")
    if len(engine.persons) > 5:
        pids = list(engine.persons.keys())
        result = engine.report_relapse(pids[5], "Tratamento de adicao incompleto")
        print("  {result['person']} voltou para rua.")
        print("  Motivo: {result['reason']}")
        print("  {result['system_failure']}")
    # === 8. STATS ===
    print("\n\n  === 8. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA DO OPENDIGNITY")
    print("{'='*80}")
    print("""
A REPUBLICA not ACEITA:
    - Ser humano dormindo na rua
    - Ser humano passando fome
    - Ser humano sem banho
    - Ser humano sem tratamento
    - Ser humano sem dignidade
O PROCESSO (5 fases):
    1. MAPEAMENTO: Republica vai as ruas PROCURAR (not espera vir)
    2. RESGATE: comer + abrigo + saude AGORA (sem fila)
    3. COLONIA: moradia + comunidade + tratamento
    4. RESTAURACAO: saude + oficio + familia (leva tempo)
    5. REINTEGRACAO: moradia propria + trabalho + mentor
COLONIAS DE DIGNIDADE:
    not sao abrigos. not sao instituicoes.
    Sao COMUNIDADES onde pessoas se restauram.
    - Casa propria (OpenCivilConstruction)
    - Cozinha comunitaria
    - Clinica (OpenHealth Sirio-Libanes)
    - Escola (OpenEducation)
    - FabLab/Horta (trabalho + skills)
    - OpenTerminal (acesso digital)
    - Tratamento (adicao, mental, fisica)
CADA PESSOA RECEBE:
    - Moradia PERMANENTE (not temporaria)
    - Comida 3x/dia (direito)
    - Saude completa (Sirio-Libanes)
    - Tratamento de adicao (se necessario)
    - Saude mental (OpenPsychology sem rotular)
    - OpenKit completo (smartphone, ID, roupas)
    - Oficio (aprende, trabalha)
    - Mentor (1 ano)
    - Comunidade (not sozinho)
    - ID nova (sem marcador)
    - Prontuario limpo (sem estigma)
SE VOLTA PARA RUA:
    - FALHA DO SISTEMA (not da pessoa)
    - Republica NUNCA desiste
    - Recomeca o processo
    - Corrige o que falhou
PRINCIPIOS:
    P1: Pobreza not and culpa. and falha do sistema. Republica corrige.
    P2: Corpo protegido. Moradia and direito. Fome and violencia.
    P3: Restauracao = trabalho de todos (medicos, mentores, construtores).
    P4: Colonias geridas democraticamente. Residentes participam.
# )
    print("{'='*80}")
    print("  OpenDignity: {s['total_identified']} pessoas mapeadas, "
        "{s['total_rescued']} resgatadas, "
        "{s['total_integrated']} reintegradas.")
    print("  Ninguem na rua. Nunca mais.")
    print("{'='*80}")
