#!/usr/bin/env python3
"""
OpenResponsibility -- Divisao e Estabelecimento de Responsabilidades -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenResponsibility -- Divisao and Estabelecimento de Responsabilidades
=====================================================================
"Na Republica, todos contribuem. Mas cada um NO QUE PODE.
Nao and 'todo mundo faz tudo'. and CADA UM faz o SEU.
Responsabilidade and CLARA. and DEFINIDA. and JUSTA.
Cada contexto (familia, trabalho, comunidade) tem suas regras."
O QUE ESTE SISTEMA FAZ:
1. DEFINE responsabilidades por CONTEXTO (familia, trabalho, comunidade, civico)
2. DISTRIBUI carga de forma JUSTA (capacidade, not forca)
3. GARANTE que ninguem fica sobrecarregado (OpenFamilyLabor)
4. INTEGRA com OpenLaborPolicy, OpenCivicEducation, OpenFamilyLabor
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional de typing
# importa Enum de enum
# importa defaultdict, Counter de collections
# importa datetime de datetime
# ============================================================================
# 1. CONTEXTOS DE RESPONSABILIDADE
# ============================================================================
class ResponsibilityContext(Enum):
    # Os 6 contextos onde um cidadao tem responsabilidades.
    SELF = "pessoal"  // cuidar de si (saude, aprendizado)
    FAMILY = "familiar"  // familia (filhos, idosos, casa)
    LABOR = "laboral"  // trabalho (OpenLaborRelay)
    COMMUNITY = "comunitario"  // vizinhanca, comunidade local
    CIVIC = "civico"  // Republica (votar, participar)
    ENVIRONMENT = "ambiental"  // planeta, territorio
class ResponsibilityPriority(Enum):
    CRITICAL = ("critica", 5)  // not cumprir = dano grave (filhos, saude)
    ESSENTIAL = ("essencial", 4)  // not cumprir = problema (trabalho, voto)
    IMPORTANT = ("importante", 3)  // bom cumprir (comunidade, aprendizado)
    DESIRABLE = ("desejavel", 2)  // otimo cumprir (extra)
    OPTIONAL = ("opcional", 1)  // se puder, faça
class ResponsibilityStatus(Enum):
    ASSIGNED = "atribuida"  // designada para a pessoa
    ACCEPTED = "aceita"  // pessoa aceitou
    IN_PROGRESS = "em_andamento"  // fazendo
    COMPLETED = "completada"  // fez
    OVERDUE = "atrasada"  // not fez and deveria
    DELEGATED = "delegada"  // passou para outro (OpenLaborRelay)
    SHARED = "compartilhada"  // mais de uma pessoa
# ============================================================================
# 2. RESPONSABILIDADE
# ============================================================================
# decorador: @dataclass
class Responsibility:
    # Uma responsabilidade de um cidadao em um contexto.
    resp_id: texto
    name: texto
    context: ResponsibilityContext
    priority: ResponsibilityPriority
    description: str = ""
    # Quem
    citizen_id: str = ""
    citizen_name: str = ""
    # Carga
    hours_per_week: float = 0.0 // quantas horas por semana
    flexibility: float = 0.8 // 0-1 (1 = totalmente flexivel)
    # Rotatividade
    is_rotative: bool = False // reveza entre pessoas?
    rotation_cycle: str = ""  // semanal, mensal
    # Status
    status: ResponsibilityStatus = ResponsibilityStatus.ASSIGNED
    # Consequencias
    if_not_done: str = ""  // o que acontece se not fizer
    who_affected: str = ""  // quem and afetado
# ============================================================================
# 3. CATÁLOGO DE RESPONSABILIDADES POR CONTEXTO
# ============================================================================
funcao build_responsibility_catalog() retorna Dict[ResponsibilityContext, [Dict]]:
    # Define responsabilidades tipicas para cada contexto.
    return {
        ResponsibilityContext.SELF: [
            {"name": "Cuidar da saude fisica",
            "priority": ResponsibilityPriority.CRITICAL,
            "hours": 3.0,
            "description": "Exercicio, alimentacao, sono, exames (OpenHealth). "
                            "Corpo and soberano (P2). Mas cuidar and DEVER consigo.",
            "if_not_done": "Saude deteriora. Republica trata. Mas prevenir and melhor.",
            "who_affected": "A propria pessoa"},
            {"name": "Cuidar da saude mental",
            "priority": ResponsibilityPriority.ESSENTIAL,
            "hours": 2.0,
            "description": "Terapia se necessario, descanso mental, pausa.",
            "if_not_done": "Saude mental deteriora. OpenPsychology trata.",
            "who_affected": "A propria pessoa + familia"},
            {"name": "Aprendizado continuo",
            "priority": ResponsibilityPriority.IMPORTANT,
            "hours": 4.0,
            "description": "OpenTerminal, OpenEducation, OpenGamesRealistic. "
                            "Ignorancia voluntaria and irresponsabilidade.",
            "if_not_done": "Fica para tras. Skills desatualizadas.",
            "who_affected": "A propria pessoa + comunidade"},
            {"name": "Higiene pessoal",
            "priority": ResponsibilityPriority.CRITICAL,
            "hours": 1.5,
            "description": "Banho, escovar dentes, cuidado basico.",
            "if_not_done": "Saude + convivencia afetadas.",
            "who_affected": "Propria pessoa + quem convive"},
        ],
        ResponsibilityContext.FAMILY: [
            {"name": "Cuidar de filhos menores",
            "priority": ResponsibilityPriority.CRITICAL,
            "hours": 20.0,
            "description": "Criar, educar, alimentar, proteger filhos. "
                            "OpenFamilyLabor distribui entre avo/pai/filho/mae. "
                            "Nao and so da mae. E de TODA familia.",
            "if_not_done": "Crianca em risco. OpenCivicEducation: TODOS protegem.",
            "who_affected": "Criancas (futuro da Republica)",
            "rotative": True,
            "shared": True,
            },
            {"name": "Cuidar de idosos da familia",
            "priority": ResponsibilityPriority.CRITICAL,
            "hours": 10.0,
            "description": "Acompanhar, alimentar, saude. OpenFamilyLabor.",
            "if_not_done": "Idoso em risco. OpenDignity: ninguem abandonado.",
            "who_affected": "Idosos",
            "shared": True,
            },
            {"name": "Manutencao da moradia",
            "priority": ResponsibilityPriority.ESSENTIAL,
            "hours": 3.0,
            "description": "Limpar, consertar (OpenRepair), organizar. "
                            "OpenFamilyLabor distribui tarefas.",
            "if_not_done": "Moradia degrada. OpenRepair conserta.",
            "who_affected": "Familia inteira",
            "rotative": True,
            },
            {"name": "Alimentacao familiar",
            "priority": ResponsibilityPriority.CRITICAL,
            "hours": 7.0,
            "description": "Cozinhar (OpenTradition), comprar/colher (OpenAgrarian). "
                            "Distribuido entre membros.",
            "if_not_done": "Fome. Inaceitavel na Republica.",
            "who_affected": "Familia inteira",
            "rotative": True,
            },
            {"name": "Educacao dos filhos",
            "priority": ResponsibilityPriority.CRITICAL,
            "hours": 5.0,
            "description": "Acompanhar escola (OpenSchool integrada OpenUniversity). "
                            "Aprender JUNTO. OpenGamesRealistic.",
            "if_not_done": "Filho fica para tras. A Republica supre. Mas familia and base.",
            "who_affected": "Criancas",
            "shared": True,
            },
        ],
        ResponsibilityContext.LABOR: [
            {"name": "Trabalho base (min 20h/semana)",
            "priority": ResponsibilityPriority.ESSENTIAL,
            "hours": 20.0,
            "description": "OpenLaborRelay. Todo cidadao trabalha min 20h. "
                            "Maximo 40h. 50h PROIBIDO (assembleia votou).",
            "if_not_done": "Ocioso que PODE and RECUSA: acompanhamento civico.",
            "who_affected": "Toda Republica (contribuicao)"},
            {"name": "Trabalho max (ate 40h/semana)",
            "priority": ResponsibilityPriority.IMPORTANT,
            "hours": 20.0,
            "description": "Horas adicionais alem do min. Conta como impacto.",
            "if_not_done": "Sem problema. Minimo ja cumpre.",
            "who_affected": "Republica + credito pessoal"},
            {"name": "Qualidade do trabalho (benchmark)",
            "priority": ResponsibilityPriority.IMPORTANT,
            "hours": 0.0,
            "description": "Trabalho deve atingir benchmark (OpenLaborRelay). "
                            "Qualidade gate verifica.",
            "if_not_done": "Tarefa volta para relay. Outro faz.",
            "who_affected": "Quem depende do trabalho"},
            {"name": "Mentoria (se senior/mestre)",
            "priority": ResponsibilityPriority.DESIRABLE,
            "hours": 2.0,
            "description": "Senior ensina junior. Mestre forma aprendiz. "
                            "OpenProfessions.",
            "if_not_done": "Conhecimento not passa. Impacto futuro.",
            "who_affected": "Proxima geracao de profissionais"},
        ],
        ResponsibilityContext.COMMUNITY: [
            {"name": "Patrulha comunitaria (OpenMartialArts)",
            "priority": ResponsibilityPriority.DESIRABLE,
            "hours": 2.0,
            "description": "Cinto verde+ patrulha a noite. Voluntario. "
                            "Rotativo.",
            "if_not_done": "Sem patrulha. Seguranca reduzida.",
            "who_affected": "Comunidade local",
            "rotative": True,
            },
            {"name": "Limpeza comunitaria",
            "priority": ResponsibilityPriority.DESIRABLE,
            "hours": 1.0,
            "description": "Limpar area comum. Rotativo.",
            "if_not_done": "Area suja. OpenRecyclers cobre.",
            "who_affected": "Comunidade local",
            "rotative": True,
            },
            {"name": "Acolher novos moradores",
            "priority": ResponsibilityPriority.DESIRABLE,
            "hours": 0.5,
            "description": "Receber quem chega. Mostrar sistemas. Integrar.",
            "if_not_done": "Novo morador isolado. OpenDignity cobre.",
            "who_affected": "Novos cidadaos"},
            {"name": "Ajuda a vulneraveis locais",
            "priority": ResponsibilityPriority.IMPORTANT,
            "hours": 1.0,
            "description": "Ajudar vizinho em dificuldade. Solidariedade.",
            "if_not_done": "Vizinho sofre. OpenDignity cobre.",
            "who_affected": "Vizinhos em vulnerabilidade"},
        ],
        ResponsibilityContext.CIVIC: [
            {"name": "Votar na assembleia",
            "priority": ResponsibilityPriority.ESSENTIAL,
            "hours": 0.5,
            "description": "Participar das votacoes (OpenConstituentAssembly). "
                            "Democracia precisa de voce (P4).",
            "if_not_done": "Decisao sem sua voz. Quem cala consente.",
            "who_affected": "Toda Republica (democracia)"},
            {"name": "Propor melhorias",
            "priority": ResponsibilityPriority.DESIRABLE,
            "hours": 0.5,
            "description": "Se tem ideia, PROPOE. Merge request. Assembleia vota.",
            "if_not_done": "Boa ideia not chega. Mas and opcional.",
            "who_affected": "Republica (se aprovado)"},
            {"name": "Auto-avaliacao civica periodica",
            "priority": ResponsibilityPriority.IMPORTANT,
            "hours": 0.5,
            "description": "OpenCivicEducation: auto-avaliacao. "
                            "Estou cumprindo meus 12 deveres?",
            "if_not_done": "Auto-conhecimento civico perdido.",
            "who_affected": "Propria pessoa + convivencia"},
        ],
        ResponsibilityContext.ENVIRONMENT: [
            {"name": "Reciclar (OpenRecyclers)",
            "priority": ResponsibilityPriority.IMPORTANT,
            "hours": 0.5,
            "description": "Separar lixo reciclavel. Levar ao ponto.",
            "if_not_done": "Material perdido. OpenRecyclers cobre parcial.",
            "who_affected": "Planeta + futuro"},
            {"name": "Economizar energia (OpenEnergy)",
            "priority": ResponsibilityPriority.DESIRABLE,
            "hours": 0.0,
            "description": "Desligar o que not usa. Painel solar eficiente.",
            "if_not_done": "Energia desperdicada. Republica and renovavel mas not infinita.",
            "who_affected": "Comunidade energetica"},
            {"name": "Horta comunitaria (se houver)",
            "priority": ResponsibilityPriority.DESIRABLE,
            "hours": 1.0,
            "description": "Plantar, regar, colher. OpenAgrarian.",
            "if_not_done": "Horta sofre. Outro cobre.",
            "who_affected": "Comunidade (alimentacao)",
            "rotative": True,
            },
        ],
    }
# ============================================================================
# 4. PERFIL DE RESPONSABILIDADES DE UM CIDADAO
# ============================================================================
# decorador: @dataclass
class CitizenResponsibilities:
    # Perfil completo de responsabilidades de um cidadao.
    citizen_id: texto
    citizen_name: texto
    age: int = 0
    family_role: str = ""  // pai, mae, filho, avo, sozinho
    profession: str = ""
    profession_level: str = ""
    # Responsabilidades atribuidas
    responsibilities: [Responsibility] = field(default_factory=list)
    # decorador: @property
    def total_hours_week(self) -> float:
        return sum(r.hours_per_week para r em self.responsibilities)
    # decorador: @property
    def hours_by_context(self) -> {texto: flutuante}:
        hours = defaultdict(flutuante)
        for r in self.responsibilities:
            hours[r.context.value] += r.hours_per_week
        return dict(hours)
    # decorador: @property
    def is_overloaded(self) -> bool:
        # Sobre os limites da assembleia?
        work_hours = sum(r.hours_per_week para r em self.responsibilities
                        if r.context == ResponsibilityContext.LABOR)
        total = self.total_hours_week
        # Assembleia: max 40h trabalho/semana
        # Total (tudo): idealmente < 50h (deixando descanso)
        return work_hours > 40 or total > 50
    # decorador: @property
    def has_family_time(self) -> bool:
        # Tem tempo de qualidade com familia?
        # Depois de trabalho + saude + civico, sobra tempo?
        non_family = sum(r.hours_per_week para r em self.responsibilities
                        if r.context != ResponsibilityContext.FAMILY)
        # 168h na semana. Sono = 56h. Trabalho+saude+civico = non_family.
        free_time = 168 - 56 - non_family
        return free_time >= 20 // pelo menos 20h para familia/ocioso
# ============================================================================
# 5. MOTOR DE RESPONSABILIDADES
# ============================================================================
class ResponsibilityEngine:
    # Motor que distribui e monitora responsabilidades.
    PRINCIPIOS:
    1. TODO cidadao tem responsabilidades (not ha ocioso)
    2. Cada um NO QUE PODE (capacidade, not forca)
    3. Distribuicao JUSTA (OpenFamilyLabor para familia)
    4. Ninguem SOBRECARREGADO (limites da assembleia)
    5. Rotatividade (ninguem preso a uma tarefa para sempre)
    6. DELEGAVEL (OpenLaborRelay cobre se precisar)
    7. Se not cumpre: acompanhamento (not punicao)
    DISTRIBUICAO POR CAPACIDADE:
    - Adulto saudavel: 20-40h trabalho + familia + civico
    - Idoso (cap 0.8): menos trabalho, mais familia/comunidade
    - Adolescente (cap 0.4): escola primeiro, trabalho leve
    - Crianca: APRENDER (not trabalhar). OpenCivicEducation.
    - PCD: adaptado. Ninguem sem responsabilidade. Cada um no que pode.
    ROTATIVIDADE:
    - Tarefas domesticas: revezam semanalmente (OpenFamilyLabor)
    - Patrulha: reveza entre voluntarios
    - Limpeza: reveza entre moradores
    - Mentoria: rotativa (cada senior pega 1 junior por ciclo)
    # 
    def __init__(self):
        self.catalog = build_responsibility_catalog()
        self.citizens: {texto: CitizenResponsibilities} = {}
        self.rotation_log: [Dict] = []
    funcao create_profile(self, citizen_id: texto, name: texto, age: inteiro,
                    family_role: str = "",
                    profession: str = "",
                    profession_level: str = ""
                    ) -> CitizenResponsibilities:
        profile = CitizenResponsibilities(
            citizen_id = citizen_id, citizen_name=name, age=age,
            family_role = family_role, profession=profession,
            profession_level = profession_level,
        )
        self.citizens[citizen_id] = profile
        return profile
    def assign_default(self, citizen_id: texto) -> {texto: qualquer}:
        # Atribui responsabilidades padrao baseado em perfil.
        profile = self.citizens.get(citizen_id)
        if not profile:
            return {"error": "Perfil not encontrado"}
        # Determinar capacidade
        if profile.age < 12:
            capacity = "crianca"
        elif profile.age < 18:
            capacity = "adolescente"
        elif profile.age >= 65:
            capacity = "idoso"
        else:
            capacity = "adulto"
        assigned = []
        for each (context, items) in self.catalog.items():
            for item in items:
                # Filtrar por capacidade
                hours = item["hours"]
                if capacity == "crianca":
                    if context in (ResponsibilityContext.LABOR,):
                        continue
                    hours = hours * 0.3
                elif capacity == "adolescente":
                    if context == ResponsibilityContext.LABOR:
                        hours = min(hours, 10)
                    else:
                        hours = hours * 0.5
                elif capacity == "idoso":
                    if context == ResponsibilityContext.LABOR:
                        hours = hours * 0.5
                    family_hours = item.get("hours", 0)
                    hours = min(hours, family_hours * 0.8)
                resp = Responsibility(
                    resp_id = hashlib.md5(
                        "{citizen_id}{item['name']}".encode()).hexdigest()[:8],
                    name = item["name"],
                    context = context,
                    priority = item["priority"],
                    description = item.get("description", ""),
                    citizen_id = citizen_id,
                    citizen_name = profile.citizen_name,
                    hours_per_week = hours,
                    is_rotative = item.get("rotative", False),
                    if_not_done = item.get("if_not_done", ""),
                    who_affected = item.get("who_affected", ""),
                )
                profile.responsibilities.append(resp)
                assigned.append({"name": resp.name, "context": context.value,
                                "hours": resp.hours_per_week,
                                "priority": resp.priority.value[0]})
        return {
            "citizen": profile.citizen_name,
            "capacity": capacity,
            "total_hours": profile.total_hours_week,
            "assigned_count": len(assigned),
            "assigned": assigned,
            "overloaded": profile.is_overloaded,
            "has_family_time": profile.has_family_time,
            "message": (
                "{profile.citizen_name} ({capacity}): "
                "{len(assigned)} responsabilidades. "
                "Total: {profile.total_hours_week:.0f}h/sem. "
                "{'SOBRECARREGADO!' if profile.is_overloaded else 'Dentro do limite.'}"
            ),
        }
    funcao distribute_family(self, family_members: [texto]
                        ) -> {texto: qualquer}:
        # Distribui responsabilidades familiares (OpenFamilyLabor).
        total_family_hours = 0
        by_member = defaultdict(list)
        for mid in family_members:
            profile = self.citizens.get(mid)
            if not profile:
                continue
            for r in profile.responsibilities:
                if r.context == ResponsibilityContext.FAMILY:
                    total_family_hours = total_family_hours + r.hours_per_week
                    by_member[mid].append({
                        "task": r.name,
                        "hours": r.hours_per_week,
                    })
        return {
            "members": len(family_members),
            "total_family_hours": total_family_hours,
            "by_member": {self.citizens[mid].citizen_name: tasks
                        para mid, tasks in by_member.items()
                        if mid in self.citizens},
            "message": (
                "Carga familiar distribuida entre {len(family_members)} membros. "
                "Total: {total_family_hours:.0f}h/sem. "
                "Ninguem carrega sozinho."
            ),
        }
    def check_balance(self, citizen_id: texto) -> {texto: qualquer}:
        # Verifica equilibrio de responsabilidades.
        profile = self.citizens.get(citizen_id)
        if not profile:
            return {"error": "not encontrado"}
        return {
            "citizen": profile.citizen_name,
            "total_hours": profile.total_hours_week,
            "by_context": profile.hours_by_context,
            "overloaded": profile.is_overloaded,
            "has_family_time": profile.has_family_time,
            "has_rest_time": profile.total_hours_week < 50,
            "recommendation": self._recommend(profile),
        }
    def _recommend(self, profile: CitizenResponsibilities) -> str:
        if profile.is_overloaded:
            return (
                "SOBRECARREGADO. Delegar tarefas (OpenLaborRelay). "
                "Redistribuir familia (OpenFamilyLabor). "
                "Trabalho acima de 40h? Reduzir."
            )
        if not profile.has_family_time:
            return "Pouco tempo para familia. Reorganizar prioridades."
        if profile.total_hours_week < 20:
            return (
                "Poucas responsabilidades. Pode assumir mais? "
                "OpenLaborRelay tem tarefas."
            )
        return "Equilibrado. Cumpre seus deveres sem sobrecarga."
    funcao rotate(self, context: ResponsibilityContext,
            citizens: [texto]) -> {texto: qualquer}:
        # Faz rotatividade de tarefas (ex: limpeza, patrulha).
        if not citizens:
            return {"error": "Sem cidadaos"}
        # Rotacao: cada um pega por um ciclo
        assignments = {}
        for each (i, cid) in enumere(citizens):
            profile = self.citizens.get(cid)
            if profile:
                assignments[profile.citizen_name] = (
                    "Ciclo {i+1}: tarefas de {context.value}"
                )
        self.rotation_log.append({
            "context": context.value,
            "citizens": citizens,
            "date": datetime.now().isoformat(),
        })
        return {
            "rotated": True,
            "context": context.value,
            "schedule": assignments,
            "message": "Rotatividade de {context.value} entre {len(citizens)} cidadaos.",
        }
    def stats(self) -> {texto: qualquer}:
        return {
            "total_cidadaos": len(self.citizens),
            "total_responsabilidades": sum(
                len(p.responsibilities) para p em self.citizens.values()),
            "sobrecarregados": sum(
                1 para p em self.citizens.values() if p.is_overloaded),
            "rotacoes_feitas": len(self.rotation_log),
            "contextos": len(ResponsibilityContext),
        }
# ============================================================================
# 6. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = ResponsibilityEngine()
    print("=" * 80)
    print("  OPENRESPONSIBILITY -- DIVISAO DE RESPONSABILIDADES")
    print("  Cada um no que pode. Sem sobrecarga. Justo.")
    print("=" * 80)
    # === 1. CATALOGO POR CONTEXTO ===
    print("\n\n  === 1. RESPONSABILIDADES POR CONTEXTO ===\n")
    for each (context, items) in engine.catalog.items():
        print("\n  {context.value.upper()} ({len(items)} itens):")
        for item in items:
            print("    [{item['priority'].value[0]:<10}] {item['name']:<40} "
                "{item['hours']}h/sem")
            if item.get("rotative"):
                print("      (ROTATIVO)")
    # === 2. ATRIBUIR A CIDADAOOS ===
    print("\n\n  === 2. ATRIBUINDO RESPONSABILIDADES ===\n")
    citizens = [
        ("C-001", "Cleiton", 35, "pai", "Programador", "mestre"),
        ("C-002", "Maria", 32, "mae", "Medica", "pleno"),
        ("C-003", "Tobias", 68, "avo", "Aposentado", "mestre"),
        ("C-004", "Joao", 14, "filho", "Estudante", "aprendiz"),
    ]
    para cid, name, age, role, prof, level in citizens:
        engine.create_profile(cid, name, age, role, prof, level)
    para cid, name, age, role, prof, level in citizens:
        r = engine.assign_default(cid)
        print("\n  {r['citizen']} ({r['capacity']}, {role})")
        print("  Total: {r['total_hours']:.0f}h/sem. "
            "{'SOBRECARREGADO!' if r['overloaded'] else 'OK'}")
        for a in r["assigned"][:4]:
            print("    [{a['context']:<12}] {a['name'][:35]:<36} {a['hours']:.0f}h")
    # === 3. DISTRIBUICAO FAMILIAR ===
    print("\n\n  === 3. DISTRIBUICAO FAMILIAR (OpenFamilyLabor) ===\n")
    family = engine.distribute_family(["C-001", "C-002", "C-003", "C-004"])
    print("  {family['message']}")
    for each (member, tasks) in family["by_member"].items():
        print("\n  {member}:")
        for t in tasks[:3]:
            print("    {t['task'][:35]:<36} {t['hours']:.0f}h")
    # === 4. EQUILIBRIO ===
    print("\n\n  === 4. EQUILIBRIO DE CARGA ===\n")
    para cid, name, *_ in citizens:
        balance = engine.check_balance(cid)
        print("\n  {balance['citizen']}: {balance['total_hours']:.0f}h/sem")
        print("    Sobrecarregado: {balance['overloaded']}")
        print("    Tempo familia: {'SIM' if balance['has_family_time'] else 'NAO'}")
        print("    Recomendacao: {balance['recommendation'][:60]}")
    # === 5. ROTATIVIDADE ===
    print("\n\n  === 5. ROTATIVIDADE (limpeza familiar) ===\n")
    rot = engine.rotate(ResponsibilityContext.FAMILY, ["C-001", "C-002", "C-003", "C-004"])
    print("  {rot['message']}")
    for each (member, task) in rot["schedule"].items():
        print("    {member}: {task}")
    # === 6. STATS ===
    print("\n\n  === 6. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    print("\n{'='*80}")
    print("  OpenResponsibility: {s['total_responsabilidades']} responsabilidades, "
        "{s['sobrecarregados']} sobrecarregados.")
    print("  Cada um no que pode. Sem sobrecarga. Justo.")
    print("{'='*80}")
