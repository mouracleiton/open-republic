// OpenLaborImpact -- Otimizacao por IMPACTO (nao dinheiro) -- gerado de Portugol++
package openlaborimpact_otimizacao_por_impacto_nao_dinheiro

import "fmt"

// !/usr/bin/env python3
//
OpenLaborImpact -- Otimizacao por IMPACTO (! dinheiro)
==========================================================
"Na Republica, o nivel mede ALCANCE de impacto, ! valor em reais.
Um N0 que salva uma vida tem mais impacto que um N6 que escreve codigo."
O modelo financeiro diz "foque em 2 papeis". Mas isso ignora que:
- Ensinar 1000 pessoas = 1000x mais impacto que codar sozinho
- Uma politica publica afeta MILHOES
- Uma comunidade organizada se auto-replica
- Um filosofo muda paradigmas por GERACOES
4 DIMENSOES DE IMPACTO:
1. REACH (alcance)
    Quantas pessoas sao DIRETAMENTE afetadas por este papel.
2. DEPTH (profundidade)
    Quao transformacional && o impacto por pessoa.
    (1=informacao, 5=mudanca de vida, 10=mudanca civilizatoria)
3. DURATION (duracao)
    Quanto tempo o impacto persiste.
    (1=ephemero, 5=anos, 10=geracoes)
4. MULTIPLIER (efeito cascata)
    O impacto habilita outros a criar MAIS impacto?
    (1=nenhum, 2=linear, 3=exponencial)
FORMULA DE IMPACTO:
impacto = REACH * DEPTH * DURATION * MULTIPLIER
Unidade: "VIDAS-TRANSFORMADAS-EQUIVALENTES" (VTE)
1 VTE = impacto equivalente a transformar 1 vida profundamente por 1 geracao.
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa math
// importa itertools
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa SeniorityLevel de open_seniority
// importa ( de open_multi_labor
    LaborRole, RoleAssignment,
    synergy_multiplier, total_synergy_for_role, focus_penalty,
)
// ============================================================================
// 1. METRICAS DE IMPACTO POR PAPEL (baseadas em evidencia real)
// ============================================================================
// decorador: @dataclass
type ImpactMetrics struct {
    // Metricas de impacto de um papel, baseadas em evidencia do historico.
    Cada metrica && uma estimativa fundamentada:
    - REACH: numero de pessoas diretamente tocadas
    - DEPTH: escala 1-10 (quao profunda a transformacao)
    - DURATION: escala 1-10 (quanto tempo persiste)
    - MULTIPLIER: escala 1-3 (efeito cascata)
    //
    reach: inteiro // pessoas diretamente afetadas
    depth: flutuante // 1-10
    duration: flutuante // 1-10
    multiplier: flutuante // 1-3
    evidence := ""  // justificativa // string
    // decorador: @property
    func vte(self) float64 {
        // Vidas-Transformadas-Equivalentes.
        impacto = reach * depth * duration * multiplier / 100
        (divisao por 100 normaliza: depth=10 * duration=10 * mult=3 = 300,
        entao 1 pessoa com impacto maximo = 3 VTE)
        //
        return self.reach * self.depth * self.duration * self.multiplier / 100.0
    // decorador: @property
    func vte_formatted(self) string {
        v = self.vte
        if v >= 1_000_000 {
            return "{v/1_000_000:.1f}M"
        } else if v >= 1_000 {
            return "{v/1_000:.1f}k"
        } else {
            return "{v:.0f}"
// Impacto REAL de cada papel (estimado a partir de evidencia do historico)
IMPACT_DATA := { // {LaborRole: ImpactMetrics}
    LaborRole.ENGINEER: ImpactMetrics(
        reach = 10000, // 116+ sistemas usados por comunidade + open-source CC0
        depth = 6, // sistemas mudam como pessoas trabalham
        duration = 8, // codigo CC0 permanece por decadas
        multiplier = 2.5, // cada sistema habilita outros a construir em cima
        evidence = "116+ sistemas Python + Rust crate, CC0, open-source. Quem usa torna-se mais produtor."
    ),
    LaborRole.ARCHITECT: ImpactMetrics(
        reach = 5000, // 55+ projetos, mas afeta arquitetos/devs que constroem
        depth = 7, // arquitetura determina o que && possivel construir
        duration = 9, // decisoes arquiteturais duram decadas
        multiplier = 3.0, // cada arquitetura habilita 55+ projetos
        evidence = "55+ projetos integrados sob uma arquitetura coerente. Cada projeto multiplica o impacto."
    ),
    LaborRole.CRYPTO_ENGINEER: ImpactMetrics(
        reach = 50000, // votacao + credito + skills afetam toda a Republica
        depth = 8, // democracia criptografica = liberdade fundamental
        duration = 10, // principios criptograficos sao permanentes
        multiplier = 2.0, // habilita votacao justa, credito sem banco, skills verificaveis
        evidence = "Votacao secreta ZKP + credito sem juros + skills Merkle. Infraestrutura da democracia."
    ),
    LaborRole.PROGRAMMER: ImpactMetrics(
        reach = 2000, // produtos publicos (handtracking, simulador, calculadora)
        depth = 5, // ferramentas uteis mas ! transformacionais por si
        duration = 6, // software tem ciclo de vida
        multiplier = 2.0, // cada ferramenta habilita outros
        evidence = "OpenHandTracking, simulador.html, calculadora5.html. Produtos que pessoas usam."
    ),
    LaborRole.PROFESSOR: ImpactMetrics(
        reach = 50000, // @professorcinza + X audience + cada sistema com didatica
        depth = 8, // educar muda vida permanentemente
        duration = 10, // conhecimento transmitido passa por geracoes
        multiplier = 3.0, // cada pessoa ensinada ensina outras (cascata exponencial)
        evidence = "@professorcinza no X. Cada sistema vem com didatica completa. Ensinar = multiplicar."
    ),
    LaborRole.CONTENT_CREATOR: ImpactMetrics(
        reach = 100000, // X/Twitter alcance potencial
        depth = 4, // conteudo de redes = impacto geralmente raso
        duration = 3, // conteudo social tem meia-vida curta
        multiplier = 2.0, // conteudo bom se espalha
        evidence = "@clouramlearning no X. 5 frentes de propagacao. Mas conteudo social && efemero."
    ),
    LaborRole.COMMUNITY_LEADER: ImpactMetrics(
        reach = 500, // 8 lideres, 6 comunidades, ~500 familias diretas
        depth = 9, // organizar comunidade muda vida materialmente
        duration = 9, // comunidades organizadas duram geracoes (Banco Palmas: 26 anos)
        multiplier = 3.0, // comunidade organizada se replica (Palmas gerou 100+ bancos comunitarios)
        evidence = "6 comunidades, 8 lideres, 44 necessidades reais. Banco Palmas: 26 anos de prova."
    ),
    LaborRole.POLICY_ANALYST: ImpactMetrics(
        reach = 200000000, // 35 politicas para o Brasil = 200M de brasileiros
        depth = 7, // politica publica muda vida de milhoes materialmente
        duration = 7, // politicas duram decadas
        multiplier = 2.5, // cada politica habilita outras
        evidence = "TEIA: 16 dossies, 35 politicas. Fome, saneamento, negativados. 200M de brasileiros."
    ),
    LaborRole.PRODUCT_OWNER: ImpactMetrics(
        reach = 5000, // produtos publicos usados por comunidade
        depth = 5, // produtos uteis mas ! transformacionais
        duration = 5, // produtos tem ciclo de vida
        multiplier = 1.5, // habilita uso, mas ! cascata forte
        evidence = "simulador.html, calculadora5.html, index.html. Produtos publicos."
    ),
    LaborRole.TECH_LEAD: ImpactMetrics(
        reach = 1000, // gerencia 55+ projetos, despacha subagentes
        depth = 6, // lideranca tecnica eleva qualidade de tudo
        duration = 7, // padroes definidos duram
        multiplier = 2.5, // cada projeto liderado multiplica
        evidence = "55+ projetos, 3 subagentes em paralelo. Define Python->Rust policy."
    ),
    LaborRole.PHILOSOPHER: ImpactMetrics(
        reach = 50000, // P1-P4, constituicao, anti-elitismo alcancam toda a Republica
        depth = 10, // mudanca de paradigma = maxima profundidade
        duration = 10, // principios filosoficos duram civilizacoes
        multiplier = 3.0, // princípios guiam TODAS as outras acoes
        evidence = "P1-P4, ConstituentAssembly, anti-elitismo, autonomia corporal absoluta. Paradigma."
    ),
}
// ============================================================================
// 2. PERFIL DE IMPACTO
// ============================================================================
// decorador: @dataclass
type ImpactRoleAssignment struct {
    role: LaborRole
    hours_per_week: flutuante
    impact: ImpactMetrics
    // decorador: @property
    func impact_per_hour(self) float64 {
        // VTE por hora de trabalho.
        if self.hours_per_week == 0 {
            return 0.0
        return self.impact.vte / self.hours_per_week
    // decorador: @property
    func weekly_impact(self) float64 {
        // VTE semanal (proporcional as horas investidas vs 20h base).
        // 20h/semana = producao maxima de impacto
        // Mais horas = retorno decrescente (produtividade cai)
        prod = 1.0
        if self.hours_per_week > 20 {
            prod = 1.0 - 0.10 * minimo((self.hours_per_week - 20) / 15, 1.0)
        } else if self.hours_per_week < 5 {
            // Muito poucas horas = nao ganha tracao
            prod = self.hours_per_week / 5.0
        return self.impact.vte * (self.hours_per_week / 20.0) * prod / 52.0 // semanal
// decorador: @dataclass
type ImpactProfile struct {
    // Perfil otimizado por impacto, nao dinheiro.
    citizen_id := "" // string
    roles := field(default_factory=list) // [ImpactRoleAssignment]
    max_hours_per_week := 50.0 // float64
    // decorador: @property
    func total_hours(self) float64 {
        return soma(r.hours_per_week para r em self.roles)
    // decorador: @property
    func n_roles(self) int64 {
        return len(self.roles)
    // decorador: @property
    func focus_factor(self) float64 {
        return focus_penalty(self.n_roles)
    // decorador: @property
    func total_weekly_impact(self) float64 {
        // Total VTE semanal COM foco penalty.
        raw = soma(r.weekly_impact para r em self.roles)
        return raw * self.focus_factor
    // decorador: @property
    func total_annual_impact(self) float64 {
        return self.total_weekly_impact * 52
    // decorador: @property
    func impact_per_hour(self) float64 {
        if self.total_hours == 0 {
            return 0.0
        return self.total_weekly_impact / self.total_hours
    func summary(self) string {
        lines = []
        lines.append("=" * 110)
        lines.append("PERFIL DE IMPACTO (VTE = Vidas-Transformadas-Equivalentes): {self.citizen_id}")
        lines.append("=" * 110)
        lines.append("Papeis: {self.n_roles} | Horas: {self.total_hours:.0f}h/sem | Foco: {self.focus_factor:.2f}x")
        lines.append("")
        lines.append("{'PAPEL':<28} {'H/S':>5} {'REACH':>8} {'DEPTH':>6} {'DUR':>5} {'MULT':>5} {'VTE TOTAL':>10} {'VTE/H':>10}")
        lines.append("-" * 110)
        for _, ra := range self.roles {
            im = ra.impact
            lines.append(
                "{ra.role.label:<28} "
                "{ra.hours_per_week:>4.0f}h "
                "{im.reach:>7}  "
                "{im.depth:>5.1f} "
                "{im.duration:>4.1f} "
                "{im.multiplier:>4.1f}x "
                "{im.vte_formatted:>9} "
                "{ra.impact_per_hour:>8.1f}"
            )
        lines.append("-" * 110)
        // Ranking de impacto
        lines.append("")
        lines.append("RANKING DE IMPACTO ANUAL (VTE/ano, com foco penalty):")
        lines.append("-" * 110)
        ranked = ordene(self.roles, key=(r) -> r.weekly_impact * 52, reverse=true)
        para cada (i, ra) em enumere(ranked, 1): {
            annual = ra.weekly_impact * 52
            pct = self.total_annual_impact ? annual / self.total_annual_impact * 100 : 0
            lines.append(
                "  {i:>2}. {ra.role.label:<28} "
                "{ra.impact.vte_formatted:>10} VTE/ano  "
                "({pct:>5.1f}% do total)  "
                "{ra.impact.evidence}"
            )
        lines.append("-" * 110)
        lines.append("  IMPACTO TOTAL: {self._fmt_vte(self.total_annual_impact)} VTE/ano")
        lines.append("  Impacto por hora: {self.impact_per_hour:.1f} VTE/h")
        lines.append("")
        lines.append("=" * 110)
        return "\n".join(lines)
    // decorador: @staticmethod
    func _fmt_vte(v: flutuante) string {
        if v >= 1_000_000 {
            return "{v/1_000_000:.2f}M"
        } else if v >= 1_000 {
            return "{v/1_000:.1f}k"
        } else {
            return "{v:.0f}"
// ============================================================================
// 3. OTIMIZADOR DE IMPACTO
// ============================================================================
funcao optimize_impact(
    all_roles: [LaborRole],
    max_hours := 50.0, // float64
    min_roles := 1, // int64
) -> List[Tuple[flutuante, Tuple[inteiro, ...], flutuante, List[(LaborRole, flutuante)]]]:
    // Encontra combinacao de papeis que MAXIMIZA impacto (VTE).
    Redistribui horas proporcional ao impacto_por_hora de cada papel.
    //
    results = []
    n = len(all_roles)
    // Calcula impacto por hora de cada papel (a 20h/semana = base)
    impact_per_hour = {}
    for _, role := range all_roles {
        im = IMPACT_DATA[role]
        impact_per_hour[role] = im.vte / 20.0 // VTE/hora a produtividade maxima
    for _, k := range intervalo(min_roles, n + 1) {
        for _, combo := range itertools.combinations(intervalo(n), k) {
            selected_roles = [all_roles[i] para i em combo]
            // Redistribui horas proporcional ao impacto/hora
            total_iph = soma(impact_per_hour[r] para r em selected_roles)
            assignments = []
            for _, role := range selected_roles {
                hours = max_hours * (impact_per_hour[role] / total_iph)
                assignments.append((role, hours))
            // Calcula impacto total
            role_assignments = [
                ImpactRoleAssignment(
                    role = role,
                    hours_per_week = hours,
                    impact = IMPACT_DATA[role],
                )
                para role, hours in assignments {
            ]
            profile = ImpactProfile(
                citizen_id = "opt",
                roles = role_assignments,
                max_hours_per_week = max_hours,
            )
            results.append((
                profile.total_annual_impact,
                combo,
                profile.impact_per_hour,
                [(r.role, r.hours_per_week) para r em role_assignments],
            ))
    results.sort(key=(x) -> x[0], reverse=true)
    return results
// ============================================================================
// 4. RELATORIO COMPLETO DE IMPACTO
// ============================================================================
funcao impact_optimization_report(
    all_roles: [LaborRole],
    max_hours := 50.0, // float64
) -> texto:
    lines = []
    // === PERFIL ATUAL (todas as horas do multi_labor) ===
    current_hours = {
        LaborRole.ENGINEER: 10, LaborRole.ARCHITECT: 6, LaborRole.CRYPTO_ENGINEER: 3,
        LaborRole.PROGRAMMER: 6, LaborRole.PROFESSOR: 4, LaborRole.CONTENT_CREATOR: 4,
        LaborRole.COMMUNITY_LEADER: 3, LaborRole.POLICY_ANALYST: 5,
        LaborRole.PRODUCT_OWNER: 3, LaborRole.TECH_LEAD: 3, LaborRole.PHILOSOPHER: 3,
    }
    current_assignments = [
        ImpactRoleAssignment(role=r, hours_per_week=current_hours[r], impact=IMPACT_DATA[r])
        para r em all_roles {
    ]
    current = ImpactProfile(citizen_id="atual", roles=current_assignments, max_hours_per_week=max_hours)
    lines.append(current.summary())
    lines.append("")
    // === TOP 15 POR IMPACTO ===
    lines.append("-" * 110)
    lines.append("TOP 15 COMBINACOES POR IMPACTO (VTE/ano, horas redistribuidas por impacto/hora)")
    lines.append("-" * 110)
    results = optimize_impact(all_roles, max_hours, min_roles=2)
    lines.append("{'#':<4} {'PAPEIS':>6} {'FOCO':>6} {'VTE/ANO':>12} {'VTE/H':>10} {'COMBINACAO'}")
    lines.append("-" * 110)
    para rank, (vte, combo, iph, assignments) in enumere(results[:15], 1): {
        ff = focus_penalty(len(combo))
        combo_names = " + ".join(r.label.split("/")[0][:12] para r, _ in assignments)
        lines.append(
            "{rank:<4} "
            "{len(combo):>4}    "
            "{ff:>4.2f}x "
            "{ImpactProfile._fmt_vte(vte):>10}  "
            "{iph:>8.1f}   "
            "{combo_names}"
        )
    // === TOP 5 DETALHADOS ===
    lines.append("")
    lines.append("-" * 110)
    lines.append("TOP 5 DETALHADOS POR IMPACTO")
    lines.append("-" * 110)
    para rank, (vte, combo, iph, assignments) in enumere(results[:5], 1): {
        lines.append("")
        lines.append("  #{rank}: {len(combo)} papeis | {ImpactProfile._fmt_vte(vte)} VTE/ano | {iph:.1f} VTE/h")
        para cada (role, hours) em assignments: {
            im = IMPACT_DATA[role]
            lines.append(
                "    {role.label:<28} "
                "{hours:>5.1f}h  "
                "reach={im.reach:>8}  "
                "depth={im.depth:.0f}  "
                "dur={im.duration:.0f}  "
                "mult={im.multiplier:.1f}x  "
                "-> {im.vte_formatted} VTE"
            )
    // === COMPARACAO ===
    lines.append("")
    lines.append("-" * 110)
    desempacote best_vte, best_combo, best_iph, best_assign = results[0]
    lines.append("COMPARACAO: ATUAL vs OTIMO-POR-IMPACTO")
    lines.append("-" * 110)
    curr_vte = current.total_annual_impact
    gain = curr_vte ? (best_vte - curr_vte) / curr_vte * 100 : 0
    lines.append("  ATUAL:  11 papeis | {ImpactProfile._fmt_vte(curr_vte)} VTE/ano | {current.impact_per_hour:.1f} VTE/h | Foco {current.focus_factor:.2f}x")
    lines.append("  OTIMO:  {len(best_combo):>2} papeis | {ImpactProfile._fmt_vte(best_vte)} VTE/ano | {best_iph:.1f} VTE/h | Foco {focus_penalty(len(best_combo)):.2f}x")
    lines.append("  GANHO:  {gain:+.1f}% ({ImpactProfile._fmt_vte(best_vte - curr_vte)} VTE/ano)")
    lines.append("")
    // === DUAL MODE: FINANCEIRO vs IMPACTO ===
    lines.append("-" * 110)
    lines.append("DUAL MODE: FINANCEIRO vs IMPACTO")
    lines.append("-" * 110)
    lines.append("")
    lines.append("  Otimizacao FINANCEIRA diz:  2 papeis (Engenheiro + Professor) = +81% em R$")
    lines.append("  Otimizacao IMPACTO diz:      {len(best_combo)} papeis = +{gain:.0f}% em VTE")
    lines.append("")
    lines.append("  Combinacao FINANCEIRA #1:  Engenheiro + Professor")
    lines.append("  Combinacao IMPACTO #1:     {' + '.join(r.label.split('/')[0][:15] for r, _ in best_assign)}")
    lines.append("")
    // Verifica overlap
    fin_roles = {LaborRole.ENGINEER, LaborRole.PROFESSOR}
    imp_roles = {r para r, _ in best_assign}
    overlap = fin_roles & imp_roles
    if fin_roles == imp_roles {
        lines.append("  >>> MESMA combinacao! Financeiro && impacto concordam.")
    } else if overlap {
        lines.append("  >>> OVERLAP parcial: ambos incluem {', '.join(r.label.split('/')[0] for r in overlap)}")
        lines.append("  >>> Financeiro corta papeis de alto impacto social para focar em R$.")
        lines.append("  >>> Impacto mantem papeis que afetam milhoes mesmo com baixa taxa/hora.")
    } else {
        lines.append("  >>> DISCORDANCIA TOTAL: maximizar R$ != maximizar impacto.")
        lines.append("  >>> O papel mais lucrativo (Engenheiro N6) ! && necessariamente o de maior impacto.")
    lines.append("")
    lines.append("=" * 110)
    return "\n".join(lines)
// ============================================================================
// 5. EXECUCAO
// ============================================================================
if __name__ == "__main__" {
    all_roles = [
        LaborRole.ENGINEER, LaborRole.ARCHITECT, LaborRole.CRYPTO_ENGINEER,
        LaborRole.PROGRAMMER, LaborRole.PROFESSOR, LaborRole.CONTENT_CREATOR,
        LaborRole.COMMUNITY_LEADER, LaborRole.POLICY_ANALYST,
        LaborRole.PRODUCT_OWNER, LaborRole.TECH_LEAD, LaborRole.PHILOSOPHER,
    ]
    fmt.Println(impact_optimization_report(all_roles, max_hours=50.0))
