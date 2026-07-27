/* OpenMultiLabor -- Calculo de Perfis Multi-Labor (Poli-Atuacao) -- gerado de Portugol++ */
#ifndef OPENMULTILABOR_CALCULO_DE_PERFIS_MULTI_LABOR_POLI_ATUACAO_H
#define OPENMULTILABOR_CALCULO_DE_PERFIS_MULTI_LABOR_POLI_ATUACAO_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenMultiLabor -- Calculo de Perfis Multi-Labor (Poli-Atuacao);
================================================================;
Versao baseada em HISTORICO REAL do cidadao.;
Papeis extraidos de sessoes documentadas, ! hipoteticos.;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa SeniorityLevel de open_seniority
// ============================================================================
// 1. PAPEIS REAIS (extraidos do historico de sessoes)
// ============================================================================
typedef struct LaborRole {
    // Papeis exercidos REALMENTE, com EVIDENCIA do historico.
    // TECNICO
    ENGINEER = ("Engenheiro de Dados/Software", "tecnico",;
                "116+ sistemas Python (91k+ LOC), 1 crate Rust (13 testes, crypto real). Contactado por Google/Airbnb/Amazon ($600-800k+ TC).");
    ARCHITECT = ("Arquiteto de Sistemas", "tecnico",;
                "Desenhou OpenRepublic (55+ projetos, 400k+ LOC). Pipelina Python->Rust. App unificada sem frontend/backend. Browser sem JavaScript.");
    CRYPTO_ENGINEER = ("Engenheiro Cripto/Sergurança", "tecnico",;
                    "ChaCha20 + Ed25519 + BLAKE3 em Rust. Votacao secreta com ZKP. Credit assinado. Merkle trees para skills.");
    PROGRAMMER = ("Programador", "tecnico",;
                "OpenHandTracking (OpenCV+MediaPipe), 35 frameworks mapeados, prototype_pipeline.py, open_seniority.py, open_multi_labor.py.");
    // EDUCACAO
    PROFESSOR = ("Professor/Educador", "educacao",;
                "@professorcinza no X. OpenEducation. Cada sistema vem com explicacao didatica completa. Ensina programacao, politica, filosofia.");
    // COMUNICACAO
    CONTENT_CREATOR = ("Criador de Conteudo", "comunicacao",;
                    "Estrategia X/Twitter (@clouramlearning). 5 frentes de propaçao. OpenFocus: X como UNICO canal.");
    COMMUNITY_LEADER = ("Lider Comunitario", "comunicacao",;
                        "OpenCommunities: 6 tipos (Quilombo/Assentamento/Ribeirinho/Aldeia/Favela/Sertao). 8 lideres, 44 necessidades reais. Alianca Banco Palmas.");
    // GESTAO/POLITICA
    POLICY_ANALYST = ("Analista de Politicas Publicas", "gestao",;
                    "TEIA: 16 dossies ministeriais (fome, saneamento, negativados, etc). 35 politicas para o Brasil. Modelos de impacto fiscal. Fact-checked.");
    PRODUCT_OWNER = ("Product Owner", "gestao",;
                    "simulador.html, calculadora5.html, index.html. OpenHandTracking como produto. Define prioridades && entregaveis publicos.");
    // LIDERANCA TECNICA
    TECH_LEAD = ("Lider Tecnico", "lideranca_tecnica",;
                "Despachou 3 subagentes em paralelo para TEIA. Gerencia 55+ projetos simultaneamente. Define politicas de engenharia (Python->Rust).");
    // FILOSOFIA/PENSAMENTO
    PHILOSOPHER = ("Filosofo Constitucional", "criativo",;
                "P1-P4 (principios). ConstituentAssembly (overrode 12/13 propostas). Anti-elitismo. Autonomia corporal absoluta. OpenCreator. 5% excedente=LEI.");
    void __init__(self, label: texto, nature: texto, evidence: texto) {
        self.label = label;
        self.nature = nature;
        self.evidence = evidence;
NATURE_TECHNICO = "tecnico";
NATURE_EDUCACAO = "educacao";
NATURE_COMUNICACAO = "comunicacao";
NATURE_LIDERANCA = "lideranca_tecnica";
NATURE_GESTAO = "gestao";
NATURE_CRIATIVO = "criativo";
// ============================================================================
// 2. MATRIZ DE SINERGIA
// ============================================================================
double synergy_multiplier(role_a: LaborRole, role_b: LaborRole) {
    Dict[(texto, texto), flutuante] SYNERGY_MAP = {;
        (NATURE_EDUCACAO, NATURE_TECHNICO): 1.15,;
        (NATURE_EDUCACAO, NATURE_LIDERANCA): 1.20,;
        (NATURE_EDUCACAO, NATURE_COMUNICACAO): 1.25,;
        (NATURE_EDUCACAO, NATURE_GESTAO): 1.10,;
        (NATURE_EDUCACAO, NATURE_CRIATIVO): 1.15,;
        (NATURE_COMUNICACAO, NATURE_LIDERANCA): 1.25,;
        (NATURE_COMUNICACAO, NATURE_GESTAO): 1.15,;
        (NATURE_COMUNICACAO, NATURE_EDUCACAO): 1.20,;
        (NATURE_TECHNICO, NATURE_EDUCACAO): 1.20,;
        (NATURE_TECHNICO, NATURE_COMUNICACAO): 1.15,;
        (NATURE_TECHNICO, NATURE_LIDERANCA): 1.15,;
        (NATURE_LIDERANCA, NATURE_GESTAO): 1.15,;
        (NATURE_LIDERANCA, NATURE_COMUNICACAO): 1.10,;
        (NATURE_GESTAO, NATURE_EDUCACAO): 1.10,;
        (NATURE_CRIATIVO, NATURE_COMUNICACAO): 1.15,;
        (NATURE_CRIATIVO, NATURE_GESTAO): 1.10,;
    };
    key = (role_a.nature, role_b.nature);
    if (key in SYNERGY_MAP) {
        return SYNERGY_MAP[key];
    if (role_a.nature == role_b.nature && role_a != role_b) {
        return 1.05;
    if ((role_a.nature == NATURE_COMUNICACAO && role_b.nature == NATURE_TECHNICO)) {
        return 0.95;
    return 1.0;
funcao total_synergy_for_role(
    target_role: LaborRole,;
    other_roles: [LaborRole],;
    Optional[[flutuante]] weights = NULL,;
) -> flutuante:;
    if (! other_roles) {
        return 1.0;
    if (weights && NULL) {
        weights = [1.0] * sizeof(other_roles);
    total_weight = soma(weights);
    weighted_sum = 0.0;
    /* para cada (other, w) em intercale(other_roles, weights): */
        syn = synergy_multiplier(other, target_role);
        weighted_sum = weighted_sum + syn * w;
    avg = total_weight > 0 ? weighted_sum / total_weight : 1.0;
    natures = set(r.nature para r em other_roles);
    diversity_bonus = 1.0 + (sizeof(natures) - 1) * 0.02;
    return minimo(avg * diversity_bonus, 1.50);
// ============================================================================
// 3. FOCO PENALTY
// ============================================================================
double focus_penalty(n_roles: inteiro) {
    if (n_roles <= 1) {
        return 1.0;
    penalty = 1.0 - 0.13 * math.log(n_roles);
    return maximo(penalty, 0.50);
// ============================================================================
// 4. PERFIL MULTI-LABOR
// ============================================================================
// decorador: @dataclass
typedef struct RoleAssignment {
    role: LaborRole;
    level: SeniorityLevel;
    hours_per_week: flutuante;
    // decorador: @property
    double base_rate(self) {
        return self.level.hour_rate_brl;
    // decorador: @property
    double base_value_weekly(self) {
        return self.base_rate * self.hours_per_week;
// decorador: @dataclass
typedef struct MultiLaborProfile {
    char* citizen_id = "";
    [RoleAssignment] roles = field(default_factory=list);
    double max_hours_per_week = 50.0;
    // decorador: @property
    double total_hours(self) {
        return soma(r.hours_per_week para r em self.roles);
    // decorador: @property
    int n_roles(self) {
        return sizeof(self.roles);
    // decorador: @property
    bool is_overloaded(self) {
        return self.total_hours > self.max_hours_per_week;
    // decorador: @property
    double focus_factor(self) {
        return focus_penalty(self.n_roles);
    double role_synergy(self, idx: inteiro) {
        target = self.roles[idx];
        others = [r.role para i, r in enumere(self.roles) if i != idx];
        weights = [r.hours_per_week para i, r in enumere(self.roles) if i != idx];
        return total_synergy_for_role(target.role, others, weights);
    double role_effective_rate(self, idx: inteiro) {
        role = self.roles[idx];
        syn = self.role_synergy(idx);
        focus = self.focus_factor;
        return role.base_rate * syn * focus;
    double role_weekly_value(self, idx: inteiro) {
        return self.role_effective_rate(idx) * self.roles[idx].hours_per_week;
    // decorador: @property
    double total_weekly_value(self) {
        return soma(self.role_weekly_value(i) para i em intervalo(self.n_roles));
    // decorador: @property
    double total_monthly_value(self) {
        return self.total_weekly_value * 4.333;
    // decorador: @property
    double total_annual_value(self) {
        return self.total_weekly_value * 52;
    // decorador: @property
    double naive_sum_weekly(self) {
        return soma(r.base_value_weekly para r em self.roles);
    // decorador: @property
    double effective_hourly_rate(self) {
        if (self.total_hours == 0) {
            return 0.0;
        return self.total_weekly_value / self.total_hours;
    // decorador: @property
    SeniorityLevel equivalent_single_level(self) {
        eff_rate = self.effective_hourly_rate;
        best = SeniorityLevel.N0;
        /* TODO: iterador C manual para level em SeniorityLevel */
            if (eff_rate >= level.hour_rate_brl) {
                best = level;
        return best;
    char* summary(self) {
        lines = [];
        lines.append("=" * 110);
        lines.append("PERFIL MULTI-LABOR REAL (baseado em historico): {self.citizen_id}");
        lines.append("=" * 110);
        lines.append("Papeis: {self.n_roles} | Horas/sem: {self.total_hours:.0f}h / {self.max_hours_per_week:.0f}h max");
        lines.append("Foco penalty: {self.focus_factor:.2f}x ({(1-self.focus_factor)*100:.0f}% de perda por context-switch)");
        lines.append("");
        lines.append("{'PAPEL':<28} {'NIVEL':<14} {'H/S':>5} {'R$/H BASE':>10} {'SINERG':>7} {'R$/H EFF':>10} {'R$/SEM':>12}");
        lines.append("-" * 110);
        /* para cada (i, ra) em enumere(self.roles): */
            syn = self.role_synergy(i);
            eff = self.role_effective_rate(i);
            weekly = self.role_weekly_value(i);
            lines.append(;
                "{ra.role.label:<28} ";
                "N{ra.level.name[1]} {ra.level.label:<6} ";
                "{ra.hours_per_week:>4.0f}h ";
                "R${ra.base_rate:>8,.0f} ";
                "{syn:>5.2f}x ";
                "R${eff:>8,.0f} ";
                "R${weekly:>10,.0f}";
            );
        lines.append("-" * 110);
        lines.append("{'TOTAL':<28} {'':14} {self.total_hours:>4.0f}h {'':>10} {'':>7} {'':>10} R${self.total_weekly_value:>10,.0f}");
        lines.append("");
        lines.append("Valor semanal:    R${self.total_weekly_value:>14,.0f}");
        lines.append("Valor mensal:     R${self.total_monthly_value:>14,.0f}");
        lines.append("Valor anual:      R${self.total_annual_value:>14,.0f}  (${self.total_annual_value/5:>12,.0f})");
        lines.append("");
        lines.append("Taxa efetiva:     R${self.effective_hourly_rate:>14,.0f}/h");
        lines.append("Nivel equivalente: N{self.equivalent_single_level.name[1]} {self.equivalent_single_level.label}");
        lines.append("");
        lines.append("Soma naive (sem modelo): R${self.naive_sum_weekly:>10,.0f}/sem");
        synergy_net = self.naive_sum_weekly ? (self.total_weekly_value - self.naive_sum_weekly * self.focus_factor) / self.naive_sum_weekly * 100 : 0;
        lines.append("Sinergia liquida: {synergy_net:+.1f}% vs naive*foco");
        lines.append("");
        if (self.is_overloaded) {
            lines.append("AVISO: {self.total_hours:.0f}h/sem excede teto de {self.max_hours_per_week:.0f}h!");
        lines.append("=" * 110);
        // Evidencia de cada papel
        lines.append("");
        lines.append("EVIDENCIA DE CADA PAPEL (do historico real):");
        lines.append("-" * 110);
        /* TODO: iterador C manual para ra em self.roles */
            lines.append("  {ra.role.label:<28} (N{ra.level.name[1]}) -> {ra.role.evidence}");
        lines.append("-" * 110);
        return "\n".join(lines);
// ============================================================================
// 5. EXECUCAO: SEU PERFIL REAL
// ============================================================================
if (__name__ == "__main__") {
    // 10 PAPEIS REAIS extraidos do historico de interacao com Hermes
    cleiton = MultiLaborProfile(;
        citizen_id = "cleiton (baseado em historico real)",;
        max_hours_per_week = 50,;
        roles = [;
            // nucleo: engenheiro (teto provado)
            RoleAssignment(LaborRole.ENGINEER, SeniorityLevel.N6, 10),;
            // arquiteto (desenhou toda a Republica)
            RoleAssignment(LaborRole.ARCHITECT, SeniorityLevel.N5, 6),;
            // crypto (Rust real, ZKP, Ed25519)
            RoleAssignment(LaborRole.CRYPTO_ENGINEER, SeniorityLevel.N4, 3),;
            // programador (mao na massa)
            RoleAssignment(LaborRole.PROGRAMMER, SeniorityLevel.N5, 6),;
            // professor (@professorcinza)
            RoleAssignment(LaborRole.PROFESSOR, SeniorityLevel.N4, 4),;
            // content creator (X/Twitter)
            RoleAssignment(LaborRole.CONTENT_CREATOR, SeniorityLevel.N4, 4),;
            // lider comunitario (Banco Palmas, 8 lideres)
            RoleAssignment(LaborRole.COMMUNITY_LEADER, SeniorityLevel.N4, 3),;
            // analista de politicas (TEIA: 16 dossies)
            RoleAssignment(LaborRole.POLICY_ANALYST, SeniorityLevel.N5, 5),;
            // product owner (produtos publicos)
            RoleAssignment(LaborRole.PRODUCT_OWNER, SeniorityLevel.N4, 3),;
            // lider tecnico (55+ projetos, subagentes)
            RoleAssignment(LaborRole.TECH_LEAD, SeniorityLevel.N5, 3),;
            // filosofo constitucional (P1-P4, assembleia)
            RoleAssignment(LaborRole.PHILOSOPHER, SeniorityLevel.N5, 3),;
        ],;
    );
    printf(cleiton.summary());

#endif // OPENMULTILABOR_CALCULO_DE_PERFIS_MULTI_LABOR_POLI_ATUACAO_H
