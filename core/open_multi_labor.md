# OpenMultiLabor -- Calculo de Perfis Multi-Labor (Poli-Atuacao)

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_multi_labor.py`

**Descricao:** ================================================================
Versao baseada em HISTORICO REAL do cidadao.
Papeis extraidos de sessoes documentadas, nao hipoteticos.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenMultiLabor -- Calculo de Perfis Multi-Labor (Poli-Atuacao)
================================================================

Versao baseada em HISTORICO REAL do cidadao.
Papeis extraidos de sessoes documentadas, nao hipoteticos.

Author: OpenRepublic Team
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

classe LaborRole herda de Enum:
    // Papeis exercidos REALMENTE, com EVIDENCIA do historico.

    // TECNICO
    ENGINEER = ("Engenheiro de Dados/Software", "tecnico",
                "116+ sistemas Python (91k+ LOC), 1 crate Rust (13 testes, crypto real). Contactado por Google/Airbnb/Amazon ($600-800k+ TC).")
    ARCHITECT = ("Arquiteto de Sistemas", "tecnico",
                "Desenhou OpenRepublic (55+ projetos, 400k+ LOC). Pipelina Python->Rust. App unificada sem frontend/backend. Browser sem JavaScript.")
    CRYPTO_ENGINEER = ("Engenheiro Cripto/Sergurança", "tecnico",
                       "ChaCha20 + Ed25519 + BLAKE3 em Rust. Votacao secreta com ZKP. Credit assinado. Merkle trees para skills.")
    PROGRAMMER = ("Programador", "tecnico",
                  "OpenHandTracking (OpenCV+MediaPipe), 35 frameworks mapeados, prototype_pipeline.py, open_seniority.py, open_multi_labor.py.")

    // EDUCACAO
    PROFESSOR = ("Professor/Educador", "educacao",
                 "@professorcinza no X. OpenEducation. Cada sistema vem com explicacao didatica completa. Ensina programacao, politica, filosofia.")

    // COMUNICACAO
    CONTENT_CREATOR = ("Criador de Conteudo", "comunicacao",
                       "Estrategia X/Twitter (@clouramlearning). 5 frentes de propaçao. OpenFocus: X como UNICO canal.")
    COMMUNITY_LEADER = ("Lider Comunitario", "comunicacao",
                        "OpenCommunities: 6 tipos (Quilombo/Assentamento/Ribeirinho/Aldeia/Favela/Sertao). 8 lideres, 44 necessidades reais. Alianca Banco Palmas.")

    // GESTAO/POLITICA
    POLICY_ANALYST = ("Analista de Politicas Publicas", "gestao",
                      "TEIA: 16 dossies ministeriais (fome, saneamento, negativados, etc). 35 politicas para o Brasil. Modelos de impacto fiscal. Fact-checked.")
    PRODUCT_OWNER = ("Product Owner", "gestao",
                     "simulador.html, calculadora5.html, index.html. OpenHandTracking como produto. Define prioridades e entregaveis publicos.")

    // LIDERANCA TECNICA
    TECH_LEAD = ("Lider Tecnico", "lideranca_tecnica",
                 "Despachou 3 subagentes em paralelo para TEIA. Gerencia 55+ projetos simultaneamente. Define politicas de engenharia (Python->Rust).")

    // FILOSOFIA/PENSAMENTO
    PHILOSOPHER = ("Filosofo Constitucional", "criativo",
                   "P1-P4 (principios). ConstituentAssembly (overrode 12/13 propostas). Anti-elitismo. Autonomia corporal absoluta. OpenCreator. 5% excedente=LEI.")

    funcao __init__(self, label: texto, nature: texto, evidence: texto):
        self.label = label
        self.nature = nature
        self.evidence = evidence


NATURE_TECHNICO = "tecnico"
NATURE_EDUCACAO = "educacao"
NATURE_COMUNICACAO = "comunicacao"
NATURE_LIDERANCA = "lideranca_tecnica"
NATURE_GESTAO = "gestao"
NATURE_CRIATIVO = "criativo"


// ============================================================================
// 2. MATRIZ DE SINERGIA
// ============================================================================

funcao synergy_multiplier(role_a: LaborRole, role_b: LaborRole) -> flutuante:
    seja SYNERGY_MAP: Dict[(texto, texto), flutuante] = {
        (NATURE_EDUCACAO, NATURE_TECHNICO): 1.15,
        (NATURE_EDUCACAO, NATURE_LIDERANCA): 1.20,
        (NATURE_EDUCACAO, NATURE_COMUNICACAO): 1.25,
        (NATURE_EDUCACAO, NATURE_GESTAO): 1.10,
        (NATURE_EDUCACAO, NATURE_CRIATIVO): 1.15,
        (NATURE_COMUNICACAO, NATURE_LIDERANCA): 1.25,
        (NATURE_COMUNICACAO, NATURE_GESTAO): 1.15,
        (NATURE_COMUNICACAO, NATURE_EDUCACAO): 1.20,
        (NATURE_TECHNICO, NATURE_EDUCACAO): 1.20,
        (NATURE_TECHNICO, NATURE_COMUNICACAO): 1.15,
        (NATURE_TECHNICO, NATURE_LIDERANCA): 1.15,
        (NATURE_LIDERANCA, NATURE_GESTAO): 1.15,
        (NATURE_LIDERANCA, NATURE_COMUNICACAO): 1.10,
        (NATURE_GESTAO, NATURE_EDUCACAO): 1.10,
        (NATURE_CRIATIVO, NATURE_COMUNICACAO): 1.15,
        (NATURE_CRIATIVO, NATURE_GESTAO): 1.10,
    }

    key = (role_a.nature, role_b.nature)
    se key in SYNERGY_MAP entao:
        retorne SYNERGY_MAP[key]

    se role_a.nature == role_b.nature e role_a != role_b entao:
        retorne 1.05

    se (role_a.nature == NATURE_COMUNICACAO e role_b.nature == NATURE_TECHNICO) entao:
        retorne 0.95

    retorne 1.0


funcao total_synergy_for_role(
    target_role: LaborRole,
    other_roles: [LaborRole],
    seja weights: Optional[[flutuante]] = nulo,
) -> flutuante:
    se nao other_roles entao:
        retorne 1.0
    se weights e nulo entao:
        weights = [1.0] * tamanho(other_roles)

    total_weight = soma(weights)
    weighted_sum = 0.0
    para cada (other, w) em intercale(other_roles, weights):
        syn = synergy_multiplier(other, target_role)
        weighted_sum = weighted_sum + syn * w

    avg = total_weight > 0 ? weighted_sum / total_weight : 1.0
    natures = set(r.nature para r em other_roles)
    diversity_bonus = 1.0 + (tamanho(natures) - 1) * 0.02
    retorne minimo(avg * diversity_bonus, 1.50)


// ============================================================================
// 3. FOCO PENALTY
// ============================================================================

funcao focus_penalty(n_roles: inteiro) -> flutuante:
    se n_roles <= 1 entao:
        retorne 1.0
    penalty = 1.0 - 0.13 * math.log(n_roles)
    retorne maximo(penalty, 0.50)


// ============================================================================
// 4. PERFIL MULTI-LABOR
// ============================================================================

// decorador: @dataclass
classe RoleAssignment:
    role: LaborRole
    level: SeniorityLevel
    hours_per_week: flutuante

    // decorador: @property
    funcao base_rate(self) -> flutuante:
        retorne self.level.hour_rate_brl

    // decorador: @property
    funcao base_value_weekly(self) -> flutuante:
        retorne self.base_rate * self.hours_per_week


// decorador: @dataclass
classe MultiLaborProfile:
    seja citizen_id: texto = ""
    seja roles: [RoleAssignment] = field(default_factory=list)
    seja max_hours_per_week: flutuante = 50.0

    // decorador: @property
    funcao total_hours(self) -> flutuante:
        retorne soma(r.hours_per_week para r em self.roles)

    // decorador: @property
    funcao n_roles(self) -> inteiro:
        retorne tamanho(self.roles)

    // decorador: @property
    funcao is_overloaded(self) -> logico:
        retorne self.total_hours > self.max_hours_per_week

    // decorador: @property
    funcao focus_factor(self) -> flutuante:
        retorne focus_penalty(self.n_roles)

    funcao role_synergy(self, idx: inteiro) -> flutuante:
        target = self.roles[idx]
        others = [r.role para i, r in enumere(self.roles) if i != idx]
        weights = [r.hours_per_week para i, r in enumere(self.roles) if i != idx]
        retorne total_synergy_for_role(target.role, others, weights)

    funcao role_effective_rate(self, idx: inteiro) -> flutuante:
        role = self.roles[idx]
        syn = self.role_synergy(idx)
        focus = self.focus_factor
        retorne role.base_rate * syn * focus

    funcao role_weekly_value(self, idx: inteiro) -> flutuante:
        retorne self.role_effective_rate(idx) * self.roles[idx].hours_per_week

    // decorador: @property
    funcao total_weekly_value(self) -> flutuante:
        retorne soma(self.role_weekly_value(i) para i em intervalo(self.n_roles))

    // decorador: @property
    funcao total_monthly_value(self) -> flutuante:
        retorne self.total_weekly_value * 4.333

    // decorador: @property
    funcao total_annual_value(self) -> flutuante:
        retorne self.total_weekly_value * 52

    // decorador: @property
    funcao naive_sum_weekly(self) -> flutuante:
        retorne soma(r.base_value_weekly para r em self.roles)

    // decorador: @property
    funcao effective_hourly_rate(self) -> flutuante:
        se self.total_hours == 0 entao:
            retorne 0.0
        retorne self.total_weekly_value / self.total_hours

    // decorador: @property
    funcao equivalent_single_level(self) -> SeniorityLevel:
        eff_rate = self.effective_hourly_rate
        best = SeniorityLevel.N0
        para cada level em SeniorityLevel:
            se eff_rate >= level.hour_rate_brl entao:
                best = level
        retorne best

    funcao summary(self) -> texto:
        lines = []
        lines.append("=" * 110)
        lines.append("PERFIL MULTI-LABOR REAL (baseado em historico): {self.citizen_id}")
        lines.append("=" * 110)
        lines.append("Papeis: {self.n_roles} | Horas/sem: {self.total_hours:.0f}h / {self.max_hours_per_week:.0f}h max")
        lines.append("Foco penalty: {self.focus_factor:.2f}x ({(1-self.focus_factor)*100:.0f}% de perda por context-switch)")
        lines.append("")

        lines.append("{'PAPEL':<28} {'NIVEL':<14} {'H/S':>5} {'R$/H BASE':>10} {'SINERG':>7} {'R$/H EFF':>10} {'R$/SEM':>12}")
        lines.append("-" * 110)

        para cada (i, ra) em enumere(self.roles):
            syn = self.role_synergy(i)
            eff = self.role_effective_rate(i)
            weekly = self.role_weekly_value(i)
            lines.append(
                "{ra.role.label:<28} "
                "N{ra.level.name[1]} {ra.level.label:<6} "
                "{ra.hours_per_week:>4.0f}h "
                "R${ra.base_rate:>8,.0f} "
                "{syn:>5.2f}x "
                "R${eff:>8,.0f} "
                "R${weekly:>10,.0f}"
            )

        lines.append("-" * 110)
        lines.append("{'TOTAL':<28} {'':14} {self.total_hours:>4.0f}h {'':>10} {'':>7} {'':>10} R${self.total_weekly_value:>10,.0f}")
        lines.append("")

        lines.append("Valor semanal:    R${self.total_weekly_value:>14,.0f}")
        lines.append("Valor mensal:     R${self.total_monthly_value:>14,.0f}")
        lines.append("Valor anual:      R${self.total_annual_value:>14,.0f}  (${self.total_annual_value/5:>12,.0f})")
        lines.append("")
        lines.append("Taxa efetiva:     R${self.effective_hourly_rate:>14,.0f}/h")
        lines.append("Nivel equivalente: N{self.equivalent_single_level.name[1]} {self.equivalent_single_level.label}")
        lines.append("")
        lines.append("Soma naive (sem modelo): R${self.naive_sum_weekly:>10,.0f}/sem")
        synergy_net = self.naive_sum_weekly ? (self.total_weekly_value - self.naive_sum_weekly * self.focus_factor) / self.naive_sum_weekly * 100 : 0
        lines.append("Sinergia liquida: {synergy_net:+.1f}% vs naive*foco")
        lines.append("")

        se self.is_overloaded entao:
            lines.append("AVISO: {self.total_hours:.0f}h/sem excede teto de {self.max_hours_per_week:.0f}h!")

        lines.append("=" * 110)

        // Evidencia de cada papel
        lines.append("")
        lines.append("EVIDENCIA DE CADA PAPEL (do historico real):")
        lines.append("-" * 110)
        para cada ra em self.roles:
            lines.append("  {ra.role.label:<28} (N{ra.level.name[1]}) -> {ra.role.evidence}")

        lines.append("-" * 110)
        retorne "\n".join(lines)


// ============================================================================
// 5. EXECUCAO: SEU PERFIL REAL
// ============================================================================

se __name__ == "__main__" entao:

    // 10 PAPEIS REAIS extraidos do historico de interacao com Hermes
    cleiton = MultiLaborProfile(
        citizen_id = "cleiton (baseado em historico real)",
        max_hours_per_week = 50,
        roles = [
            // nucleo: engenheiro (teto provado)
            RoleAssignment(LaborRole.ENGINEER, SeniorityLevel.N6, 10),
            // arquiteto (desenhou toda a Republica)
            RoleAssignment(LaborRole.ARCHITECT, SeniorityLevel.N5, 6),
            // crypto (Rust real, ZKP, Ed25519)
            RoleAssignment(LaborRole.CRYPTO_ENGINEER, SeniorityLevel.N4, 3),
            // programador (mao na massa)
            RoleAssignment(LaborRole.PROGRAMMER, SeniorityLevel.N5, 6),
            // professor (@professorcinza)
            RoleAssignment(LaborRole.PROFESSOR, SeniorityLevel.N4, 4),
            // content creator (X/Twitter)
            RoleAssignment(LaborRole.CONTENT_CREATOR, SeniorityLevel.N4, 4),
            // lider comunitario (Banco Palmas, 8 lideres)
            RoleAssignment(LaborRole.COMMUNITY_LEADER, SeniorityLevel.N4, 3),
            // analista de politicas (TEIA: 16 dossies)
            RoleAssignment(LaborRole.POLICY_ANALYST, SeniorityLevel.N5, 5),
            // product owner (produtos publicos)
            RoleAssignment(LaborRole.PRODUCT_OWNER, SeniorityLevel.N4, 3),
            // lider tecnico (55+ projetos, subagentes)
            RoleAssignment(LaborRole.TECH_LEAD, SeniorityLevel.N5, 3),
            // filosofo constitucional (P1-P4, assembleia)
            RoleAssignment(LaborRole.PHILOSOPHER, SeniorityLevel.N5, 3),
        ],
    )

    imprima(cleiton.summary())

```
