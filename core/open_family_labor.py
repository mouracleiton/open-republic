#!/usr/bin/env python3
"""
OpenFamilyLabor -- Distribuicao de Carga no Seio Familiar -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenFamilyLabor -- Distribuicao de Carga no Seio Familiar
============================================================
"O avo divide com o pai que divide com o filho.
Todo contexto familiar adjacente entra na conta.
Assim continuamos produzindo mesmo com menos horas.
and matematica de distribuicao."
O PROBLEMA:
Uma pessoa trabalha 4000h/ano pela Republica.
Isso and excesso (limite constitucional = 1840h).
Ela se mata de trabalhar. Burnout. Dano corporal (P2).
A SOLUCAO not and "trabalhe menos".
A solucao and DISTRIBUIR a carga.
Se 1 pessoa faz 4000h, 3 pessoas (avo + pai + filho) fazem
1333h cada. Abaixo do max. Acima do base.
MESMA PRODUCAO. MENOS SOFRIMENTO POR PESSOA.
A MATEMATICA:
Trabalho total da familia = W_total
Pessoas aptas na familia = N
Carga por pessoa = W_total / N
Se W_total = 4000h and N = 4 (avo, pai, mae, filho):
Cada um faz 1000h/ano. Abaixo do max (1840h). Acima do base (920h).
TODO MUNDO cumpre o contrato. NINGUEM se mata.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict de collections
# ============================================================================
# 1. ESTRUTURA FAMILIAR
# ============================================================================
class FamilyRole(Enum):
    # Papeis na estrutura familiar.
    GRANDPARENT = "avo"  // avo/avoh -- sabedoria, leve
    PARENT = "pai"  // pai/mae -- pilar central
    ADULT_CHILD = "filho_adulto"  // filho 18+ -- capacidade plena
    TEEN = "adolescente"  // 14-17 -- capacidade parcial
    CHILD = "crianca"  // abaixo de 14 -- not conta (protecao)
    UNCLE_AUNT = "tio"  // tio/tia -- adjacente
    COUSIN = "primo"  // primo/adulto -- adjacente
    SIBLING = "irmao"  // irmao/irma -- adjacente
    SPOUSE = "conjuge"  // marido/esposa
    IN_LAW = "ente"  // genro/nora/cunhado
class CapacityLevel(Enum):
    # Capacidade de trabalho por idade/saude.
    FULL = "plena"  // adulto saudavel -- 100% capacidade
    HIGH = "alta"  // adulto 60+ saudavel -- 80%
    MODERATE = "moderada"  // idoso 70+ -- 50%
    LIGHT = "leve"  // idoso 80+ or recuperacao -- 25%
    TEEN = "adolescente"  // 14-17 -- 40% (protecao, escola primeiro)
    EXEMPT = "isenso"  // crianca, doente, gestante -- 0%
# decorador: @dataclass
class FamilyMember:
    # Um membro da familia com capacidade de trabalho.
    member_id: texto
    name: texto
    role: FamilyRole
    age: inteiro
    capacity: CapacityLevel
    current_hours: float = 0.0 // horas que ja trabalha
    specialties: [texto] = field(default_factory=list) // areas de competencia
    # decorador: @property
    def capacity_factor(self) -> float:
        # Multiplicador de capacidade (0.0 a 1.0).
        return {
            CapacityLevel.FULL: 1.0,
            CapacityLevel.HIGH: 0.8,
            CapacityLevel.MODERATE: 0.5,
            CapacityLevel.LIGHT: 0.25,
            CapacityLevel.TEEN: 0.4,
            CapacityLevel.EXEMPT: 0.0,
        }.get(self.capacity, 0.0)
    # decorador: @property
    def can_work(self) -> bool:
        return self.capacity_factor > 0
    # decorador: @property
    def max_hours_per_year(self) -> float:
        # Maximo de horas que esta pessoa pode fazer.
        base_max = 1840.0 // max constitucional
        # Teen tem teto mais baixo (escola primeiro)
        if self.capacity == CapacityLevel.TEEN:
            return 460.0 // max 10h/sem (escola and prioridade)
        return base_max * self.capacity_factor
    # decorador: @property
    def base_hours_per_year(self) -> float:
        # Base esperada desta pessoa (ajustada por capacidade).
        base = 920.0 // base constitucional
        return base * self.capacity_factor
# ============================================================================
# 2. UNIDADE FAMILIAR
# ============================================================================
# decorador: @dataclass
class FamilyUnit:
    # Uma familia que distribui carga de trabalho.
    O contrato familiar:
    - O trabalho que UMA pessoa fazia agora and de TODA a familia
    - Cada membro faz sua parte (proporcional a capacidade)
    - O avo faz o que pode (leve). O pai faz o pesado. O filho aprende.
    - Ninguem ultrapassa o limite. Todos contribuem.
    # 
    family_id: texto
    family_name: texto
    members: [FamilyMember] = field(default_factory=list)
    shared_projects: [texto] = field(default_factory=list) // projetos da Republica
    # decorador: @property
    def working_members(self) -> [FamilyMember]:
        return [m para m em self.members if m.can_work]
    # decorador: @property
    def total_capacity_factor(self) -> float:
        # Soma das capacidades de todos os membros.
        return sum(m.capacity_factor para m em self.members)
    # decorador: @property
    def total_base_expected(self) -> float:
        # Total de horas base que a familia deve coletivamente.
        return sum(m.base_hours_per_year para m em self.working_members)
    # decorador: @property
    def total_max_capacity(self) -> float:
        # Total maximo que a familia pode fazer sem ninguem exceder limite.
        return sum(m.max_hours_per_year para m em self.working_members)
    # decorador: @property
    def total_current(self) -> float:
        # Total de horas que a familia trabalha agora.
        return sum(m.current_hours para m em self.members)
# ============================================================================
# 3. MOTOR DE DISTRIBUICAO
# ============================================================================
class FamilyLaborDistributor:
    # Distribui carga de trabalho entre membros da familia.
    A MATEMATICA DA DISTRIBUICAO:
    Cenario: Cleiton (fundador) trabalha 4000h/ano.
    Limite constitucional = 1840h. Excesso = 2160h.
    Se a familia de Cleiton tem 4 pessoas aptas:
    - Cleiton (42, plena): capacidade 1.0
    - Esposa (40, plena): capacidade 1.0
    - Filho (16, adolescente): capacidade 0.4
    - Pai/Cleiton pai (68, alta): capacidade 0.8
    Total capacidade = 3.2
    Trabalho total = 4000h
    Distribuicao:
    - Cleiton: 4000 * (1.0/3.2) = 1250h (abaixo do max!)
    - Esposa: 4000 * (1.0/3.2) = 1250h (abaixo do max!)
    - Filho: 4000 * (0.4/3.2) = 500h (abaixo do teto teen!)
    - Avo: 4000 * (0.8/3.2) = 1000h (abaixo do max!)
    Cada um faz sua parte. Ninguem se mata.
    MESMA PRODUCAO. ZERO EXCESSO.
    # 
    def __init__(self):
        self.families: {texto: FamilyUnit} = {}
    def register_family(self, family: FamilyUnit) -> None:
        self.families[family.family_id] = family
    funcao distribute(self, family_id: texto,
                total_work_hours: flutuante) -> {texto: qualquer}:
        # Distribui trabalho total entre membros da familia.
        Args:
            family_id: a familia
            total_work_hours: quantas horas de trabalho total distribuir
        Returns:
            Plano de distribuicao com carga por membro
        # 
        family = self.families.get(family_id)
        if not family:
            return {"error": "Familia not encontrada"}
        workers = family.working_members
        if not workers:
            return {"error": "Nenhum membro pode trabalhar"}
        total_capacity = family.total_capacity_factor
        # Distribuir proporcional a capacidade
        distribution = []
        for member in workers:
            share = total_work_hours * (member.capacity_factor / total_capacity)
            # Respeitar teto individual
            capped = min(share, member.max_hours_per_year)
            excess_avoided = max(0, share - member.max_hours_per_year)
            distribution.append({
                "name": member.name,
                "role": member.role.value,
                "age": member.age,
                "capacity": member.capacity.value,
                "capacity_factor": member.capacity_factor,
                "hours_assigned": round(capped, 0),
                "hours_per_week": round(capped / 46, 1),
                "max_allowed": round(member.max_hours_per_year, 0),
                "base_expected": round(member.base_hours_per_year, 0),
                "excess_avoided": round(excess_avoided, 0),
                "within_limit": capped <= member.max_hours_per_year,
                "meets_base": capped >= member.base_hours_per_year,
            })
        # Verificar se a distribuicao cobre o total
        total_assigned = sum(d["hours_assigned"] para d em distribution)
        coverage = total_assigned / max(total_work_hours, 1) * 100
        # Quem estava em excesso antes?
        before_excess = []
        for m in workers:
            if m.current_hours > m.max_hours_per_year:
                before_excess.append({
                    "name": m.name,
                    "was_working": m.current_hours,
                    "max": m.max_hours_per_year,
                    "excess": m.current_hours - m.max_hours_per_year,
                })
        return {
            "family": family.family_name,
            "total_work_to_distribute": total_work_hours,
            "total_capacity_factor": round(total_capacity, 2),
            "distribution": distribution,
            "total_assigned": round(total_assigned, 0),
            "coverage_pct": round(coverage, 1),
            "anyone_in_excess": any(not  d["within_limit"] para d em distribution),
            "everyone_meets_base": all(d["meets_base"] para d em distribution),
            "before_distribution": {
                "people_in_excess": len(before_excess),
                "excess_details": before_excess,
            },
            "after_distribution": {
                "max_individual_hours": max(d["hours_assigned"] para d em distribution),
                "min_individual_hours": min(d["hours_assigned"] para d em distribution),
                "everyone_within_limit": all(d["within_limit"] para d em distribution),
            },
        }
    funcao expand_to_extended_family(self, family_id: texto,
                                additional_members: [FamilyMember],
                                total_work_hours: flutuante) -> {texto: qualquer}:
        # Expande distribuicao para familia extensa (avos, tios, primos).
        Quanto mais gente, menos carga por pessoa.
        # 
        family = self.families.get(family_id)
        if not family:
            return {"error": "Familia not encontrada"}
        for m in additional_members:
            if m.member_id not in [ existing.member_id para existing em family.members]:
                family.members.append(m)
        return self.distribute(family_id, total_work_hours)
    def family_report(self, family_id: texto) -> {texto: qualquer}:
        family = self.families.get(family_id)
        if not family:
            return {"error": "not encontrada"}
        return {
            "family_name": family.family_name,
            "total_members": len(family.members),
            "working_members": len(family.working_members),
            "total_capacity": round(family.total_capacity_factor, 2),
            "total_base_expected": round(family.total_base_expected, 0),
            "total_max_capacity": round(family.total_max_capacity, 0),
            "total_current_hours": round(family.total_current, 0),
            "members": [
                {
                    "name": m.name,
                    "role": m.role.value,
                    "age": m.age,
                    "capacity": m.capacity.value,
                    "current_hours": m.current_hours,
                    "max": round(m.max_hours_per_year, 0),
                }
                para m in family.members
            ],
        }
# ============================================================================
# 4. MAIN
# ============================================================================
if __name__ == "__main__":
    print("=" * 75)
    print("  OPENFAMILYLABOR -- DISTRIBUICAO DE CARGA FAMILIAR")
    print("  'O avo divide com o pai que divide com o filho.'")
    print("=" * 75)
    dist = FamilyLaborDistributor()
    # === FAMILIA LOURA (Cleiton) ===
    family = FamilyUnit(
        family_id = "F-LOURA",
        family_name = "Familia Loura",
        members = [
            FamilyMember("M-01", "Cleiton (pai)", FamilyRole.PARENT, 42,
                        CapacityLevel.FULL, current_hours=4000,
                        specialties = ["sistemas", "codigo", "arquitetura"]),
            FamilyMember("M-02", "Esposa", FamilyRole.SPOUSE, 40,
                        CapacityLevel.FULL, current_hours=920,
                        specialties = ["educacao", "saude"]),
            FamilyMember("M-03", "Filho (16)", FamilyRole.TEEN, 16,
                        CapacityLevel.TEEN, current_hours=0,
                        specialties = ["aprendizado"]),
            FamilyMember("M-04", "Avo (68)", FamilyRole.GRANDPARENT, 68,
                        CapacityLevel.HIGH, current_hours=0,
                        specialties = ["sabedoria", "tradição", "historia"]),
        ],
        shared_projects = ["OpenRepublic", "OpenEducation", "OpenHealth"],
    )
    dist.register_family(family)
    # === ANTES DA DISTRIBUICAO ===
    print("\n\n  === ANTES: 1 PESSOA FAZ TUDO ===\n")
    report = dist.family_report("F-LOURA")
    print("  Familia: {report['family_name']}")
    print("  {'Nome':<20} {'Papel':<12} {'Idade':>5} {'Capacidade':<12} "
        "{'Horas':>6} {'Max':>6}")
    print("  {'-'*65}")
    for m in report["members"]:
        excess = m["current_hours"] > m["max"] ? " [EXCESSO!]" : ""
        print("  {m['name']:<20} {m['role']:<12} {m['age']:>4} "
            "{m['capacity']:<12} {m['current_hours']:>5.0f} "
            "{m['max']:>5.0f}{excess}")
    print("\n  TOTAL atual: {report['total_current_hours']:.0f}h")
    print("  Pessoas em excesso: 1 (Cleiton: 4000h, limite 1840h)")
    print("  Excesso: {4000 - 1840:.0f}h ACIMA do limite constitucional")
    # === DISTRIBUICAO ===
    print("\n\n  === DEPOIS: DISTRIBUINDO ENTRE A FAMILIA ===\n")
    result = dist.distribute("F-LOURA", total_work_hours=4000)
    print("  Trabalho total a distribuir: {result['total_work_to_distribute']}h")
    print("  Capacidade total da familia: {result['total_capacity_factor']}")
    print("\n  {'Nome':<20} {'Papel':<14} {'Cap':<6} {'Horas':>6} {'h/sem':>6} "
        "{'Max':>6} {'Base':>6} {'OK?'}")
    print("  {'-'*72}")
    for d in result["distribution"]:
        ok = d["within_limit"] ? "OK" : "EXCESSO"
        base_ok = d["meets_base"] ? "+" : "-"
        print("  {d['name']:<20} {d['role']:<14} {d['capacity_factor']:>4.1f} "
            "{d['hours_assigned']:>5.0f}h {d['hours_per_week']:>5.1f}h "
            "{d['max_allowed']:>5.0f}h {d['base_expected']:>5.0f}h "
            "{ok} {base_ok}")
    print("\n  Total distribuido: {result['total_assigned']:.0f}h")
    print("  Cobertura: {result['coverage_pct']:.1f}%")
    print("  Todos dentro do limite: "
        "{'SIM' if result['after_distribution']['everyone_within_limit'] else 'NAO'}")
    print("  Carga maxima individual: "
        "{result['after_distribution']['max_individual_hours']:.0f}h "
        "(antes: 4000h)")
    print("  Carga minima individual: "
        "{result['after_distribution']['min_individual_hours']:.0f}h")
    # === EXPANDIR PARA FAMILIA EXTENSA ===
    print("\n\n  === EXPANDINDO: FAMILIA EXTENSA ENTRA ===\n")
    print("  Tio, tia, and primo adulto se juntam a distribuicao.\n")
    result2 = dist.expand_to_extended_family("F-LOURA", [
        FamilyMember("M-05", "Tio Beto", FamilyRole.UNCLE_AUNT, 45,
                    CapacityLevel.FULL, specialties=["construcao", "mecanica"]),
        FamilyMember("M-06", "Tia Rosa", FamilyRole.UNCLE_AUNT, 43,
                    CapacityLevel.FULL, specialties=["educacao", "saude"]),
        FamilyMember("M-07", "Prima Luna (19)", FamilyRole.COUSIN, 19,
                    CapacityLevel.FULL, specialties=["design", "arte"]),
    ], total_work_hours=4000)
    print("  Familia agora tem {len(family.members)} membros.")
    print("  Capacidade total: {result2['total_capacity_factor']}")
    print("\n  {'Nome':<20} {'Papel':<14} {'Horas':>6} {'h/sem':>6} {'OK?'}")
    print("  {'-'*55}")
    for d in result2["distribution"]:
        ok = d["within_limit"] ? "OK" : "EXCESSO"
        print("  {d['name']:<20} {d['role']:<14} "
            "{d['hours_assigned']:>5.0f}h {d['hours_per_week']:>5.1f}h {ok}")
    print("\n  Carga maxima apos expansao: "
        "{result2['after_distribution']['max_individual_hours']:.0f}h")
    print("  Carga minima: "
        "{result2['after_distribution']['min_individual_hours']:.0f}h")
    # === COMPARACAO ===
    print("\n\n  === COMPARACAO: ANTES VS DEPOIS ===\n")
    print("  {'Cenario':<35} {'Max individual':>15} {'Excesso?':>10}")
    print("  {'-'*62}")
    print("  {'Cleiton sozinho':<35} {'4000h':>14} {'2160h':>10}")
    print("  {'Familia nuclear (4 pessoas)':<35} "
        "{result['after_distribution']['max_individual_hours']:>13.0f}h "
        "{'ZERO':>10}")
    print("  {'Familia extensa (7 pessoas)':<35} "
        "{result2['after_distribution']['max_individual_hours']:>13.0f}h "
        "{'ZERO':>10}")
    # === MATEMATICA ===
    print("\n\n  === A MATEMATICA DA DISTRIBUICAO ===\n")
    print("""
FORMULA:
    carga_por_pessoa = trabalho_total * (capacidade_individual / capacidade_total)
EXEMPLO:
    Trabalho total: 4000h
    Familia nuclear: 4 pessoas (capacidade total: 3.2)
    Cleiton (cap 1.0): 4000 * (1.0/3.2) = 1250h
    Esposa (cap 1.0): 4000 * (1.0/3.2) = 1250h
    Filho (cap 0.4): 4000 * (0.4/3.2) = 500h
    Avo (cap 0.8): 4000 * (0.8/3.2) = 1000h
    TOTAL: 1250 + 1250 + 500 + 1000 = 4000h (mesma producao)
    MAX INDIVIDUAL: 1250h (antes era 4000h -- reducao de 69%)
    EXCESSO: ZERO (antes era 2160h)
PRINCIPIO:
    P2 Autonomia Corporal: burnout = dano. Distribuir previne.
    P3 Trabalho Igual: todos na familia contribuem (proporcional).
    P1 Anti-Elitismo: o "genio" not faz tudo sozinho.
    P4 Democracia: familia decide quem faz o que.
REGRA DO AVO:
    O avo not fica isento. O avo faz o que PODE.
    Sabedoria conta como trabalho. Ensinar neto = trabalho.
    Contar historia = preservar (OpenTradition/OpenHistory).
    25% da capacidade do avo vale mais que 0%.
# )
    print("{'='*75}")
    print("  OpenFamilyLabor: distribuicao matematica de carga.")
    print("  1 pessoa faz 4000h -> 4+ pessoas fazem 1000h cada.")
    print("  Mesma producao. Zero excesso. Zero burnout.")
    print("{'='*75}")
