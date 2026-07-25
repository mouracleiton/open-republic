#!/usr/bin/env python3
"""
OpenMultiLaborOptimizer v2 -- Otimizacao com Retornos Decrescentes -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenMultiLaborOptimizer v2 -- Otimizacao com Retornos Decrescentes
====================================================================
v1 assumia valor linear (mais horas = mais valor proporcional).
REALIDADE: retornos decrescentes. 40h de engenharia not produzem 4x de 10h.
- Primeiras horas sao super-produtivas (foco profundo)
- Horas adicionais tem produtividade decrescente
- 20h/semana and o pico de produtividade por hora (base: Base 1.0)
Formula: valor_hora = taxa * sinergia * foco * CURVA(horas)
CURVA(horas) = 1.0 ate 20h, depois decai
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa itertools
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa SeniorityLevel de open_seniority
# importa ( de open_multi_labor
    LaborRole, RoleAssignment, MultiLaborProfile,
    synergy_multiplier, total_synergy_for_role, focus_penalty,
)
# ============================================================================
# 1. CURVA DE RETORNO DECRESCENTE
# ============================================================================
def productivity_curve(hours: flutuante) -> float:
    # Fator de produtividade por hora baseado nas horas alocadas.
    Base cientifica:
    - 0-20h/semana: produtividade maxima por hora (1.0x)
    (estudos mostram que 4-5h de deep work / dia and o teto humano)
    - 20-35h: produtividade cai ~10% (fadiga)
    - 35-50h: produtividade cai ~30% (burnout proximo)
    - >50h: produtividade cai ~50% (trabalhando, mas not produzindo)
    Referencia: "Deep Work" (Cal Newport), "Rest" (Alex Soojung-Kim Pang),
    estudo Microsoft (4h de trabalho profundo real por dia).
    # 
    if hours <= 20:
        return 1.0
    elif hours <= 35:
        # Decaimento suave: 20h=1.0, 35h=0.90
        return 1.0 - 0.10 * (hours - 20) / 15
    elif hours <= 50:
        # Decaimento acelerado: 35h=0.90, 50h=0.70
        return 0.90 - 0.20 * (hours - 35) / 15
    else:
        # Alem de 50h: burnout zone
        return max(0.50, 0.70 - 0.20 * (hours - 50) / 10)
def productivity_label(hours: flutuante) -> str:
    if hours <= 20:
        return "PEAK"
    elif hours <= 35:
        return "FADIGA"
    elif hours <= 50:
        return "ALTO-RISCO"
    else:
        return "BURNOUT"
# ============================================================================
# 2. PERFIL COM RETORNO DECRESCENTE
# ============================================================================
# decorador: @dataclass
class RoleAssignmentV2:
    role: LaborRole
    level: SeniorityLevel
    hours_per_week: flutuante
    # decorador: @property
    def base_rate(self) -> float:
        return self.level.hour_rate_brl
    # decorador: @property
    def productivity_factor(self) -> float:
        return productivity_curve(self.hours_per_week)
    # decorador: @property
    def effective_rate(self) -> float:
        # Taxa efetiva COM curva de produtividade (sem sinergia/foco).
        return self.base_rate * self.productivity_factor
    # decorador: @property
    def label_productivity(self) -> str:
        return productivity_label(self.hours_per_week)
# decorador: @dataclass
class MultiLaborProfileV2:
    citizen_id: str = ""
    roles: [RoleAssignmentV2] = field(default_factory=list)
    max_hours_per_week: float = 50.0
    # decorador: @property
    def total_hours(self) -> float:
        return sum(r.hours_per_week para r em self.roles)
    # decorador: @property
    def n_roles(self) -> int:
        return len(self.roles)
    # decorador: @property
    def focus_factor(self) -> float:
        return focus_penalty(self.n_roles)
    def role_synergy(self, idx: inteiro) -> float:
        target = self.roles[idx]
        others = [r.role para i, r in enumerate(self.roles) if i != idx]
        weights = [r.hours_per_week para i, r in enumerate(self.roles) if i != idx]
        return total_synergy_for_role(target.role, others, weights)
    def role_effective_rate(self, idx: inteiro) -> float:
        # Taxa com sinergia + foco + produtividade.
        role = self.roles[idx]
        syn = self.role_synergy(idx)
        return role.base_rate * syn * self.focus_factor * role.productivity_factor
    def role_weekly_value(self, idx: inteiro) -> float:
        return self.role_effective_rate(idx) * self.roles[idx].hours_per_week
    # decorador: @property
    def total_weekly_value(self) -> float:
        return sum(self.role_weekly_value(i) para i em range(self.n_roles))
    # decorador: @property
    def total_annual_value(self) -> float:
        return self.total_weekly_value * 52
    # decorador: @property
    def effective_hourly_rate(self) -> float:
        if self.total_hours == 0:
            return 0.0
        return self.total_weekly_value / self.total_hours
    # decorador: @property
    def equivalent_single_level(self) -> SeniorityLevel:
        eff_rate = self.effective_hourly_rate
        best = SeniorityLevel.N0
        for level in SeniorityLevel:
            if eff_rate >= level.hour_rate_brl:
                best = level
        return best
    def summary(self) -> str:
        lines = []
        lines.append("=" * 115)
        lines.append("PERFIL MULTI-LABOR v2 (com retornos decrescentes): {self.citizen_id}")
        lines.append("=" * 115)
        lines.append("Papeis: {self.n_roles} | Horas: {self.total_hours:.0f}h/sem | Foco: {self.focus_factor:.2f}x")
        lines.append("")
        lines.append("{'PAPEL':<28} {'NIV':>4} {'H/S':>5} {'PROD':>6} {'R$/H BASE':>10} {'SINERG':>7} {'R$/H EFF':>10} {'R$/SEM':>12}")
        lines.append("-" * 115)
        for each (i, ra) in enumere(self.roles):
            syn = self.role_synergy(i)
            eff = self.role_effective_rate(i)
            weekly = self.role_weekly_value(i)
            lines.append(
                "{ra.role.label:<28} "
                "N{ra.level.name[1]:>2} "
                "{ra.hours_per_week:>4.0f}h "
                "{ra.productivity_factor:>4.2f}x "
                "R${ra.base_rate:>8,.0f} "
                "{syn:>5.2f}x "
                "R${eff:>8,.0f} "
                "R${weekly:>10,.0f}"
            )
        lines.append("-" * 115)
        lines.append("  TOTAL: {self.total_hours:.0f}h | R${self.total_weekly_value:,.0f}/sem | R${self.total_annual_value:,.0f}/ano (${self.total_annual_value/5:,.0f})")
        lines.append("  Taxa efetiva: R${self.effective_hourly_rate:,.0f}/h | Nivel equiv: N{self.equivalent_single_level.name[1]}")
        lines.append("=" * 115)
        return "\n".join(lines)
# ============================================================================
# 3. OTIMIZADOR v2 (brute force com curva de produtividade)
# ============================================================================
funcao redistribute_hours_v2(
    roles: [RoleAssignmentV2],
    max_hours: flutuante,
) -> [RoleAssignmentV2]:
    # Redistribui horas considerando retornos decrescentes.
    Estrategia: cap cada papel em 20h (PEAK productivity),
    depois distribui o resto ponderado por nivel.
    # 
    # Cap em 20h cada um (PEAK zone)
    n = len(roles)
    if n == 0:
        return []
    # Primeiro: ate 20h para cada (se couber no orcamento)
    base_alloc = min(20.0, max_hours / n)
    # Se todos cabem em 20h dentro do orcamento
    if base_alloc * n >= max_hours:
        return [
            RoleAssignmentV2(role=r.role, level=r.level, hours_per_week=max_hours / n)
            para r in roles
        ]
    # Se ha horas sobrando: distribui ponderado por nivel
    total_weight = sum(r.level.multiplier para r em roles)
    return [
        RoleAssignmentV2(
            role = r.role,
            level = r.level,
            hours_per_week = max_hours * (r.level.multiplier / total_weight),
        )
        para r in roles
    ]
funcao evaluate_combo_v2(
    all_roles: [RoleAssignmentV2],
    indices: Tuple[inteiro, ...],
    max_hours: flutuante,
) -> Tuple[flutuante, flutuante, flutuante, [RoleAssignmentV2]]:
    # Avalia combinacao, retorna (valor_semanal, horas, taxa_efetiva, roles).
    selected = [all_roles[i] para i em indices]
    selected = redistribute_hours_v2(selected, max_hours)
    profile = MultiLaborProfileV2(citizen_id="opt", roles=selected, max_hours_per_week=max_hours)
    return (profile.total_weekly_value, profile.total_hours, profile.effective_hourly_rate, selected)
funcao optimize_v2(
    all_roles: [RoleAssignmentV2],
    max_hours: float = 50.0,
    min_roles: int = 2,
) -> List[Tuple[flutuante, Tuple[inteiro, ...], flutuante, flutuante, [RoleAssignmentV2]]]:
    # Brute force: testa todas combinacoes com curva de produtividade.
    results = []
    n = len(all_roles)
    for k in intervalo(min_roles, n + 1):
        for combo in itertools.combinations(intervalo(n), k):
            desempacote val, hrs, rate, selected = evaluate_combo_v2(all_roles, combo, max_hours)
            results.append((val, combo, hrs, rate, selected))
    results.sort(key=(x) -> x[0], reverse=True)
    return results
# ============================================================================
# 4. RELATORIO v2
# ============================================================================
funcao optimization_report_v2(
    all_roles: [RoleAssignmentV2],
    max_hours: float = 50.0,
) -> texto:
    lines = []
    # === PERFIL ATUAL ===
    current = MultiLaborProfileV2(citizen_id="atual", roles=list(all_roles), max_hours_per_week=max_hours)
    lines.append(current.summary())
    lines.append("")
    # === TOP 15 COMBINACOES ===
    lines.append("-" * 115)
    lines.append("TOP 15 COMBINACOES (com curva de produtividade + redistribuicao)")
    lines.append("-" * 115)
    results = optimize_v2(all_roles, max_hours, min_roles=2)
    lines.append("{'#':<4} {'PAPEIS':>6} {'FOCO':>6} {'R$/SEM':>12} {'R$/ANO':>14} {'$/ANO':>12} {'R$/H EFF':>10}")
    lines.append("-" * 115)
    para rank, (val, combo, hrs, rate, selected) in enumere(results[:15], 1):
        ff = focus_penalty(len(combo))
        lines.append(
            "{rank:<4} "
            "{len(combo):>4}    "
            "{ff:>4.2f}x "
            "R${val:>10,.0f} "
            "R${val*52:>12,.0f} "
            "${val*52/5:>10,.0f} "
            "R${rate:>8,.0f}"
        )
    lines.append("")
    # === TOP 5 DETALHADOS ===
    lines.append("-" * 115)
    lines.append("TOP 5 COMBINACOES DETALHADAS")
    lines.append("-" * 115)
    para rank, (val, combo, hrs, rate, selected) in enumere(results[:5], 1):
        lines.append("")
        lines.append("  #{rank}: {len(combo)} papeis | R${val:,.0f}/sem | R${val*52:,.0f}/ano (${val*52/5:,.0f}) | R${rate:,.0f}/h")
        profile = MultiLaborProfileV2(citizen_id="top{rank}", roles=selected, max_hours_per_week=max_hours)
        for each (i, ra) in enumere(selected):
            syn = profile.role_synergy(i)
            eff = profile.role_effective_rate(i)
            weekly = profile.role_weekly_value(i)
            prod = ra.productivity_factor
            lines.append(
                "    {ra.role.label:<28} N{ra.level.name[1]} "
                "{ra.hours_per_week:>5.1f}h "
                "prod={prod:.2f}x "
                "sin={syn:.2f}x "
                "R${eff:>7,.0f}/h "
                "R${weekly:>9,.0f}/sem"
            )
    # === COMPARACAO ATUAL vs #1 ===
    lines.append("")
    lines.append("-" * 115)
    desempacote best_val, best_combo, best_hrs, best_rate, best_roles = results[0]
    lines.append("COMPARACAO: ATUAL (11 papeis) vs OTIMO ({len(best_combo)} papeis)")
    lines.append("-" * 115)
    curr_val = current.total_weekly_value
    opt_val = best_val
    gain = (opt_val - curr_val) / curr_val * 100
    lines.append("  ATUAL:  11 papeis | R${curr_val:,.0f}/sem | R${curr_val*52:,.0f}/ano | Foco {current.focus_factor:.2f}x")
    lines.append("  OTIMO:  {len(best_combo):>2} papeis | R${opt_val:,.0f}/sem | R${opt_val*52:,.0f}/ano | Foco {focus_penalty(len(best_combo)):.2f}x")
    lines.append("  GANHO:  {gain:+.1f}% (+R${(opt_val-curr_val)*52:,.0f}/ano)")
    lines.append("")
    lines.append("=" * 115)
    return "\n".join(lines)
# ============================================================================
# 5. EXECUCAO
# ============================================================================
if __name__ == "__main__":
    all_roles = [
        RoleAssignmentV2(LaborRole.ENGINEER, SeniorityLevel.N6, 10),
        RoleAssignmentV2(LaborRole.ARCHITECT, SeniorityLevel.N5, 6),
        RoleAssignmentV2(LaborRole.CRYPTO_ENGINEER, SeniorityLevel.N4, 3),
        RoleAssignmentV2(LaborRole.PROGRAMMER, SeniorityLevel.N5, 6),
        RoleAssignmentV2(LaborRole.PROFESSOR, SeniorityLevel.N4, 4),
        RoleAssignmentV2(LaborRole.CONTENT_CREATOR, SeniorityLevel.N4, 4),
        RoleAssignmentV2(LaborRole.COMMUNITY_LEADER, SeniorityLevel.N4, 3),
        RoleAssignmentV2(LaborRole.POLICY_ANALYST, SeniorityLevel.N5, 5),
        RoleAssignmentV2(LaborRole.PRODUCT_OWNER, SeniorityLevel.N4, 3),
        RoleAssignmentV2(LaborRole.TECH_LEAD, SeniorityLevel.N5, 3),
        RoleAssignmentV2(LaborRole.PHILOSOPHER, SeniorityLevel.N5, 3),
    ]
    print(optimization_report_v2(all_roles, max_hours=50.0))
