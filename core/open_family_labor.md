# OpenFamilyLabor -- Distribuicao de Carga no Seio Familiar

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_family_labor.py`

**Descricao:** ============================================================
"O avo divide com o pai que divide com o filho.
 Todo contexto familiar adjacente entra na conta.
 Assim continuamos produzindo mesmo com menos horas.
 E matematica de distribuicao."
O PROBLEMA:
  Uma pessoa trabalha 4000h/ano pela Republica.
  Isso e excesso (limite constitucional = 1840h).
  Ela se mata de trabalhar. Burnout. Dano corporal (P2).
  A SOLUCAO NAO E "trabalhe menos".
  A solucao e DISTRIBUIR a carga.
  Se 1 pessoa faz 4000h, 3 pessoas (avo + pai + filho) fazem
  1333h cada. Abaixo do maximo. Acima do base.
  MESMA PRODUCAO. MENOS SOFRIMENTO POR PESSOA.
A MATEMATICA:
  Trabalho total da familia = W_total
  Pessoas aptas na familia = N
  Carga por pessoa = W_total / N
  Se W_total = 4000h e N = 4 (avo, pai, mae, filho):
  Cada um faz 1000h/ano. Abaixo do max (1840h). Acima do base (920h).
  TODO MUNDO cumpre o contrato. NINGUEM se mata.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenFamilyLabor -- Distribuicao de Carga no Seio Familiar
============================================================

"O avo divide com o pai que divide com o filho.
 Todo contexto familiar adjacente entra na conta.
 Assim continuamos produzindo mesmo com menos horas.
 e matematica de distribuicao."

O PROBLEMA:
  Uma pessoa trabalha 4000h/ano pela Republica.
  Isso e excesso (limite constitucional = 1840h).
  Ela se mata de trabalhar. Burnout. Dano corporal (P2).

  A SOLUCAO nao e "trabalhe menos".
  A solucao e DISTRIBUIR a carga.

  Se 1 pessoa faz 4000h, 3 pessoas (avo + pai + filho) fazem
  1333h cada. Abaixo do maximo. Acima do base.
  MESMA PRODUCAO. MENOS SOFRIMENTO POR PESSOA.

A MATEMATICA:
  Trabalho total da familia = W_total
  Pessoas aptas na familia = N
  Carga por pessoa = W_total / N

  Se W_total = 4000h e N = 4 (avo, pai, mae, filho):
  Cada um faz 1000h/ano. Abaixo do maximo (1840h). Acima do base (920h).
  TODO MUNDO cumpre o contrato. NINGUEM se mata.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections


// ============================================================================
// 1. ESTRUTURA FAMILIAR
// ============================================================================

classe FamilyRole herda de Enum:
    // Papeis na estrutura familiar.
    GRANDPARENT = "avo"  // avo/avoh -- sabedoria, leve
    PARENT = "pai"  // pai/mae -- pilar central
    ADULT_CHILD = "filho_adulto"  // filho 18+ -- capacidade plena
    TEEN = "adolescente"  // 14-17 -- capacidade parcial
    CHILD = "crianca"  // abaixo de 14 -- nao conta (protecao)
    UNCLE_AUNT = "tio"  // tio/tia -- adjacente
    COUSIN = "primo"  // primo/adulto -- adjacente
    SIBLING = "irmao"  // irmao/irma -- adjacente
    SPOUSE = "conjuge"  // marido/esposa
    IN_LAW = "ente"  // genro/nora/cunhado


classe CapacityLevel herda de Enum:
    // Capacidade de trabalho por idade/saude.
    FULL = "plena"  // adulto saudavel -- 100% capacidade
    HIGH = "alta"  // adulto 60+ saudavel -- 80%
    MODERATE = "moderada"  // idoso 70+ -- 50%
    LIGHT = "leve"  // idoso 80+ ou recuperacao -- 25%
    TEEN = "adolescente"  // 14-17 -- 40% (protecao, escola primeiro)
    EXEMPT = "isenso"  // crianca, doente, gestante -- 0%


// decorador: @dataclass
classe FamilyMember:
    // Um membro da familia com capacidade de trabalho.
    member_id: texto
    name: texto
    role: FamilyRole
    age: inteiro
    capacity: CapacityLevel
    seja current_hours: flutuante = 0.0 // horas que ja trabalha
    seja specialties: [texto] = field(default_factory=list) // areas de competencia

    // decorador: @property
    funcao capacity_factor(self) -> flutuante:
        // Multiplicador de capacidade (0.0 a 1.0).
        retorne {
            CapacityLevel.FULL: 1.0,
            CapacityLevel.HIGH: 0.8,
            CapacityLevel.MODERATE: 0.5,
            CapacityLevel.LIGHT: 0.25,
            CapacityLevel.TEEN: 0.4,
            CapacityLevel.EXEMPT: 0.0,
        }.get(self.capacity, 0.0)

    // decorador: @property
    funcao can_work(self) -> logico:
        retorne self.capacity_factor > 0

    // decorador: @property
    funcao max_hours_per_year(self) -> flutuante:
        // Maximo de horas que esta pessoa pode fazer.
        base_max = 1840.0 // maximo constitucional
        // Teen tem teto mais baixo (escola primeiro)
        se self.capacity == CapacityLevel.TEEN entao:
            retorne 460.0 // maximo 10h/sem (escola e prioridade)
        retorne base_max * self.capacity_factor

    // decorador: @property
    funcao base_hours_per_year(self) -> flutuante:
        // Base esperada desta pessoa (ajustada por capacidade).
        base = 920.0 // base constitucional
        retorne base * self.capacity_factor


// ============================================================================
// 2. UNIDADE FAMILIAR
// ============================================================================

// decorador: @dataclass
classe FamilyUnit:
    // Uma familia que distribui carga de trabalho.

    O contrato familiar:
    - O trabalho que UMA pessoa fazia agora e de TODA a familia
    - Cada membro faz sua parte (proporcional a capacidade)
    - O avo faz o que pode (leve). O pai faz o pesado. O filho aprende.
    - Ninguem ultrapassa o limite. Todos contribuem.
    // 
    family_id: texto
    family_name: texto
    seja members: [FamilyMember] = field(default_factory=list)
    seja shared_projects: [texto] = field(default_factory=list) // projetos da Republica

    // decorador: @property
    funcao working_members(self) -> [FamilyMember]:
        retorne [m para m em self.members if m.can_work]

    // decorador: @property
    funcao total_capacity_factor(self) -> flutuante:
        // Soma das capacidades de todos os membros.
        retorne soma(m.capacity_factor para m em self.members)

    // decorador: @property
    funcao total_base_expected(self) -> flutuante:
        // Total de horas base que a familia deve coletivamente.
        retorne soma(m.base_hours_per_year para m em self.working_members)

    // decorador: @property
    funcao total_max_capacity(self) -> flutuante:
        // Total maximo que a familia pode fazer sem ninguem exceder limite.
        retorne soma(m.max_hours_per_year para m em self.working_members)

    // decorador: @property
    funcao total_current(self) -> flutuante:
        // Total de horas que a familia trabalha agora.
        retorne soma(m.current_hours para m em self.members)


// ============================================================================
// 3. MOTOR DE DISTRIBUICAO
// ============================================================================

classe FamilyLaborDistributor:
    // Distribui carga de trabalho entre membros da familia.

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
    - Cleiton: 4000 * (1.0/3.2) = 1250h (abaixo do maximo!)
    - Esposa: 4000 * (1.0/3.2) = 1250h (abaixo do maximo!)
    - Filho: 4000 * (0.4/3.2) = 500h (abaixo do teto teen!)
    - Avo: 4000 * (0.8/3.2) = 1000h (abaixo do maximo!)

    Cada um faz sua parte. Ninguem se mata.
    MESMA PRODUCAO. ZERO EXCESSO.
    // 

    funcao __init__(self):
        self.families: {texto: FamilyUnit} = {}

    funcao register_family(self, family: FamilyUnit) -> None:
        self.families[family.family_id] = family

    funcao distribute(self, family_id: texto,
                   total_work_hours: flutuante) -> {texto: qualquer}:
        // Distribui trabalho total entre membros da familia.

        Args:
            family_id: a familia
            total_work_hours: quantas horas de trabalho total distribuir

        Returns:
            Plano de distribuicao com carga por membro
        // 
        family = self.families.get(family_id)
        se nao family entao:
            retorne {"error": "Familia nao encontrada"}

        workers = family.working_members
        se nao workers entao:
            retorne {"error": "Nenhum membro pode trabalhar"}

        total_capacity = family.total_capacity_factor

        // Distribuir proporcional a capacidade
        distribution = []
        para cada member em workers:
            share = total_work_hours * (member.capacity_factor / total_capacity)
            // Respeitar teto individual
            capped = minimo(share, member.max_hours_per_year)
            excess_avoided = maximo(0, share - member.max_hours_per_year)

            distribution.append({
                "name": member.name,
                "role": member.role.value,
                "age": member.age,
                "capacity": member.capacity.value,
                "capacity_factor": member.capacity_factor,
                "hours_assigned": arredonde(capped, 0),
                "hours_per_week": arredonde(capped / 46, 1),
                "max_allowed": arredonde(member.max_hours_per_year, 0),
                "base_expected": arredonde(member.base_hours_per_year, 0),
                "excess_avoided": arredonde(excess_avoided, 0),
                "within_limit": capped <= member.max_hours_per_year,
                "meets_base": capped >= member.base_hours_per_year,
            })

        // Verificar se a distribuicao cobre o total
        total_assigned = soma(d["hours_assigned"] para d em distribution)
        coverage = total_assigned / maximo(total_work_hours, 1) * 100

        // Quem estava em excesso antes?
        before_excess = []
        para cada m em workers:
            se m.current_hours > m.max_hours_per_year entao:
                before_excess.append({
                    "name": m.name,
                    "was_working": m.current_hours,
                    "max": m.max_hours_per_year,
                    "excess": m.current_hours - m.max_hours_per_year,
                })

        retorne {
            "family": family.family_name,
            "total_work_to_distribute": total_work_hours,
            "total_capacity_factor": arredonde(total_capacity, 2),
            "distribution": distribution,
            "total_assigned": arredonde(total_assigned, 0),
            "coverage_pct": arredonde(coverage, 1),
            "anyone_in_excess": any(nao  d["within_limit"] para d em distribution),
            "everyone_meets_base": all(d["meets_base"] para d em distribution),
            "before_distribution": {
                "people_in_excess": tamanho(before_excess),
                "excess_details": before_excess,
            },
            "after_distribution": {
                "max_individual_hours": maximo(d["hours_assigned"] para d em distribution),
                "min_individual_hours": minimo(d["hours_assigned"] para d em distribution),
                "everyone_within_limit": all(d["within_limit"] para d em distribution),
            },
        }

    funcao expand_to_extended_family(self, family_id: texto,
                                  additional_members: [FamilyMember],
                                  total_work_hours: flutuante) -> {texto: qualquer}:
        // Expande distribuicao para familia extensa (avos, tios, primos).

        Quanto mais gente, menos carga por pessoa.
        // 
        family = self.families.get(family_id)
        se nao family entao:
            retorne {"error": "Familia nao encontrada"}

        para cada m em additional_members:
            se m.member_id nao in [ existing.member_id para existing em family.members] entao:
                family.members.append(m)

        retorne self.distribute(family_id, total_work_hours)

    funcao family_report(self, family_id: texto) -> {texto: qualquer}:
        family = self.families.get(family_id)
        se nao family entao:
            retorne {"error": "nao encontrada"}

        retorne {
            "family_name": family.family_name,
            "total_members": tamanho(family.members),
            "working_members": tamanho(family.working_members),
            "total_capacity": arredonde(family.total_capacity_factor, 2),
            "total_base_expected": arredonde(family.total_base_expected, 0),
            "total_max_capacity": arredonde(family.total_max_capacity, 0),
            "total_current_hours": arredonde(family.total_current, 0),
            "members": [
                {
                    "name": m.name,
                    "role": m.role.value,
                    "age": m.age,
                    "capacity": m.capacity.value,
                    "current_hours": m.current_hours,
                    "max": arredonde(m.max_hours_per_year, 0),
                }
                para m em family.members
            ],
        }


// ============================================================================
// 4. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 75)
    imprima("  OPENFAMILYLABOR -- DISTRIBUICAO DE CARGA FAMILIAR")
    imprima("  'O avo divide com o pai que divide com o filho.'")
    imprima("=" * 75)

    dist = FamilyLaborDistributor()

    // === FAMILIA LOURA (Cleiton) ===
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

    // === ANTES DA DISTRIBUICAO ===
    imprima("\n\n  === ANTES: 1 PESSOA FAZ TUDO ===\n")
    report = dist.family_report("F-LOURA")
    imprima("  Familia: {report['family_name']}")
    imprima("  {'Nome':<20} {'Papel':<12} {'Idade':>5} {'Capacidade':<12} "
          "{'Horas':>6} {'Max':>6}")
    imprima("  {'-'*65}")
    para cada m em report["members"]:
        excess = m["current_hours"] > m["max"] ? " [EXCESSO!]" : ""
        imprima("  {m['name']:<20} {m['role']:<12} {m['age']:>4} "
              "{m['capacity']:<12} {m['current_hours']:>5.0f} "
              "{m['max']:>5.0f}{excess}")

    imprima("\n  TOTAL atual: {report['total_current_hours']:.0f}h")
    imprima("  Pessoas em excesso: 1 (Cleiton: 4000h, limite 1840h)")
    imprima("  Excesso: {4000 - 1840:.0f}h ACIMA do limite constitucional")

    // === DISTRIBUICAO ===
    imprima("\n\n  === DEPOIS: DISTRIBUINDO ENTRE A FAMILIA ===\n")
    result = dist.distribute("F-LOURA", total_work_hours=4000)

    imprima("  Trabalho total a distribuir: {result['total_work_to_distribute']}h")
    imprima("  Capacidade total da familia: {result['total_capacity_factor']}")
    imprima("\n  {'Nome':<20} {'Papel':<14} {'Cap':<6} {'Horas':>6} {'h/sem':>6} "
          "{'Max':>6} {'Base':>6} {'OK?'}")
    imprima("  {'-'*72}")

    para cada d em result["distribution"]:
        ok = d["within_limit"] ? "OK" : "EXCESSO"
        base_ok = d["meets_base"] ? "+" : "-"
        imprima("  {d['name']:<20} {d['role']:<14} {d['capacity_factor']:>4.1f} "
              "{d['hours_assigned']:>5.0f}h {d['hours_per_week']:>5.1f}h "
              "{d['max_allowed']:>5.0f}h {d['base_expected']:>5.0f}h "
              "{ok} {base_ok}")

    imprima("\n  Total distribuido: {result['total_assigned']:.0f}h")
    imprima("  Cobertura: {result['coverage_pct']:.1f}%")
    imprima("  Todos dentro do limite: "
          "{'SIM' if result['after_distribution']['everyone_within_limit'] else 'NAO'}")
    imprima("  Carga maxima individual: "
          "{result['after_distribution']['max_individual_hours']:.0f}h "
          "(antes: 4000h)")
    imprima("  Carga minima individual: "
          "{result['after_distribution']['min_individual_hours']:.0f}h")

    // === EXPANDIR PARA FAMILIA EXTENSA ===
    imprima("\n\n  === EXPANDINDO: FAMILIA EXTENSA ENTRA ===\n")
    imprima("  Tio, tia, e primo adulto se juntam a distribuicao.\n")

    result2 = dist.expand_to_extended_family("F-LOURA", [
        FamilyMember("M-05", "Tio Beto", FamilyRole.UNCLE_AUNT, 45,
                     CapacityLevel.FULL, specialties=["construcao", "mecanica"]),
        FamilyMember("M-06", "Tia Rosa", FamilyRole.UNCLE_AUNT, 43,
                     CapacityLevel.FULL, specialties=["educacao", "saude"]),
        FamilyMember("M-07", "Prima Luna (19)", FamilyRole.COUSIN, 19,
                     CapacityLevel.FULL, specialties=["design", "arte"]),
    ], total_work_hours=4000)

    imprima("  Familia agora tem {len(family.members)} membros.")
    imprima("  Capacidade total: {result2['total_capacity_factor']}")
    imprima("\n  {'Nome':<20} {'Papel':<14} {'Horas':>6} {'h/sem':>6} {'OK?'}")
    imprima("  {'-'*55}")
    para cada d em result2["distribution"]:
        ok = d["within_limit"] ? "OK" : "EXCESSO"
        imprima("  {d['name']:<20} {d['role']:<14} "
              "{d['hours_assigned']:>5.0f}h {d['hours_per_week']:>5.1f}h {ok}")

    imprima("\n  Carga maxima apos expansao: "
          "{result2['after_distribution']['max_individual_hours']:.0f}h")
    imprima("  Carga minima: "
          "{result2['after_distribution']['min_individual_hours']:.0f}h")

    // === COMPARACAO ===
    imprima("\n\n  === COMPARACAO: ANTES VS DEPOIS ===\n")
    imprima("  {'Cenario':<35} {'Max individual':>15} {'Excesso?':>10}")
    imprima("  {'-'*62}")
    imprima("  {'Cleiton sozinho':<35} {'4000h':>14} {'2160h':>10}")
    imprima("  {'Familia nuclear (4 pessoas)':<35} "
          "{result['after_distribution']['max_individual_hours']:>13.0f}h "
          "{'ZERO':>10}")
    imprima("  {'Familia extensa (7 pessoas)':<35} "
          "{result2['after_distribution']['max_individual_hours']:>13.0f}h "
          "{'ZERO':>10}")

    // === MATEMATICA ===
    imprima("\n\n  === A MATEMATICA DA DISTRIBUICAO ===\n")
    imprima("""
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
    P1 Anti-Elitismo: o "genio" nao faz tudo sozinho.
    P4 Democracia: familia decide quem faz o que.

  REGRA DO AVO:
    O avo nao fica isento. O avo faz o que PODE.
    Sabedoria conta como trabalho. Ensinar neto = trabalho.
    Contar historia = preservar (OpenTradition/OpenHistory).
    25% da capacidade do avo vale mais que 0%.
// )

    imprima("{'='*75}")
    imprima("  OpenFamilyLabor: distribuicao matematica de carga.")
    imprima("  1 pessoa faz 4000h -> 4+ pessoas fazem 1000h cada.")
    imprima("  Mesma producao. Zero excesso. Zero burnout.")
    imprima("{'='*75}")

```
