// OpenTransitionPlan -- Plano de Execucao das 4 Decisoes da Assembleia -- gerado de Portugol++
package opentransitionplan_plano_de_execucao_das_4_decisoes_da_assembleia

import "fmt"

// !/usr/bin/env python3
//
OpenTransitionPlan -- Plano de Execucao das 4 Decisoes da Assembleia
=====================================================================
APROVADO POR VOTACAO DEMOCRATICA (20-0 em 3 propostas, 19-0 em 1):
1. AUTOFINANCIAMENTO (receita propria)
2. HIBRIDO PART-TIME (consultoria $300-400k + Republica)
3. COOPERATIVA SEM DONO (Banco Palmas aplicado a software)
4. PILOTO EM COMUNIDADE REAL (1 comunidade, provar, replicar)
REJEITADO:
- FAANG full-time (4-12, comunidades votaram 0-4 contra)
ESTRUTURA:
Fase 0 (D+0 a D+30): Sobrevivencia -- o que faz HOJE
Fase 1 (D+30 a D+90): Primeira receita -- consultoria + produtos
Fase 2 (D+90 a D+180): Cooperativa formal + piloto
Fase 3 (D+180 a D+365): Escala + documentacao + replicacao
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa datetime, timedelta de datetime
// ============================================================================
// 1. FASES DO PLANO
// ============================================================================
type Phase int
const (
    SURVIVAL = ("Fase 0: Sobrevivencia", "D+0 a D+30", "Nao morrer. Garantir base.")
    FIRST_REVENUE = ("Fase 1: Primeira Receita", "D+30 a D+90", "Consultoria + produtos. R$ entra.")
    COOPERATIVE = ("Fase 2: Cooperativa + Piloto", "D+90 a D+180", "Estrutura formal. Comunidade real.")
    SCALE = ("Fase 3: Escala", "D+180 a D+365", "Provar. Documentar. Replicar.")
    func __init__(self, label, timeline, goal) {
        self.label = label
        self.timeline = timeline
        self.goal = goal
// ============================================================================
// 2. ACOES CONCRETAS
// ============================================================================
// decorador: @dataclass
type Action struct {
    // Uma acao concreta do plano.
    action_id: texto
    phase: Phase
    decision: texto // qual das 4 decisoes (autofin, hibrido, coop, piloto)
    title: texto
    description: texto
    owner := "cleiton" // string
    deadline_days := 30 // int64
    cost_brl := 0 // float64
    revenue_potential_brl := 0 // float64
    dependencies := field(default_factory=list) // [texto]
    done := false // bool
// decorador: @dataclass
type FinancialProjection struct {
    // Projecao financeira por fase.
    phase: Phase
    consulting_revenue := 0 // hibrido // float64
    product_revenue := 0 // autofinanciamento (TEIA, etc) // float64
    cooperative_revenue := 0 // cooperativa // float64
    costs := 0 // float64
    net := 0 // float64
    func calculate(self) {
        self.net = self.consulting_revenue + self.product_revenue + self.cooperative_revenue - self.costs
// ============================================================================
// 3. O PLANO COMPLETO
// ============================================================================
PLAN := [ // [Action]
    // ======================================================================
    // FASE 0: SOBREVIVENCIA (D+0 a D+30)
    // ======================================================================
    Action(
        action_id = "A001",
        phase = Phase.SURVIVAL,
        decision = "hibrido",
        title = "Mapear contatos FAANG && converter para consultoria",
        description = (
            "Voce foi contactado por Google, Airbnb, Amazon. "
            "Em vez de full-time ($600-800k), propor consultoria part-time. "
            "Pitch: '20h/semana, $300-400k/ano, remote, contrato de 6-12 meses.' "
            "Empresa ganha senior expertise sem overhead. "
            "Voce mantem 20h/semana para Republica."
        ),
        deadline_days = 7,
        cost_brl = 0,
        revenue_potential_brl = 1_500_000, // $300k * 5
        dependencies = [],
    ),
    Action(
        action_id = "A002",
        phase = Phase.SURVIVAL,
        decision = "hibrido",
        title = "Abrir perfil em plataformas de consultoria tecnica",
        description = (
            "Toptal, Upwork Expert, Braintrust, Lemon.io. "
            "Perfil: Senior/Staff Data Engineer. "
            "Rate minimo: $150-250/h. "
            "Disponibilidade: 20h/semana. "
            "Isso garante pipeline se FAANG ! quiser part-time."
        ),
        deadline_days = 7,
        cost_brl = 0,
        revenue_potential_brl = 500_000,
        dependencies = [],
    ),
    Action(
        action_id = "A003",
        phase = Phase.SURVIVAL,
        decision = "autofinanciamento",
        title = "Empacotar TEIA como produto pago (SaaS gov/ONG)",
        description = (
            "TEIA ja tem 16 dossies ministeriais fact-checked. "
            "Empacotar como: 'Plataforma de Analise Politica para Governos && ONGs.' "
            "Modelo: SaaS R$5-15k/mes por instituicao. "
            "Target: prefeituras, ONGs, fundacoes, ministerios. "
            "Voce ja tem o produto (TEIA). So falta o wrapper comercial."
        ),
        deadline_days = 14,
        cost_brl = 2000, // landing page + hosting
        revenue_potential_brl = 600_000, // 5 clientes * R$10k/mes * 12
        dependencies = [],
    ),
    Action(
        action_id = "A004",
        phase = Phase.SURVIVAL,
        decision = "autofinanciamento",
        title = "Criar pagina de doacoes OpenRepublic",
        description = (
            "Open Collective, GitHub Sponsors, Apoia.se. "
            "OpenRepublic && CC0 mas pode receber doacoes. "
            "Pitch: 'Financie a alternativa civilizatoria.' "
            "Meta inicial: R$5k/mes em doacoes recorrentes."
        ),
        deadline_days = 3,
        cost_brl = 0,
        revenue_potential_brl = 60_000, // R$5k/mes * 12
        dependencies = [],
    ),
    Action(
        action_id = "A005",
        phase = Phase.SURVIVAL,
        decision = "piloto",
        title = "Escolher 1 comunidade para piloto",
        description = (
            "Criterios da Assembleia: "
            "(a) comunidade isolada (quilombo/assentamento/ribeirinho/favela) "
            "(b) ja tem organizacao minima (lider, coletivo) "
            "(c) aceita participar (CONSENTIMENTO, ! imposicao) "
            "(d) problema real que OpenCredit/OpenProduction resolve "
            "Opcoes do historico: Banco Palmas (ja tem contato), "
            "8 lideres mapeados, 6 tipos de comunidade. "
            "Escolher UMA. Ir la. Ouvir. Adaptar. Nao impor."
        ),
        deadline_days = 21,
        cost_brl = 3000, // viagem + estadia
        revenue_potential_brl = 0,
        dependencies = [],
    ),
    // ======================================================================
    // FASE 1: PRIMEIRA RECEITA (D+30 a D+90)
    // ======================================================================
    Action(
        action_id = "A101",
        phase = Phase.FIRST_REVENUE,
        decision = "hibrido",
        title = "Fechar primeiro contrato de consultoria",
        description = (
            "Meta: 1 contrato fechado em 90 dias. "
            "Either FAANG part-time ($300k+/ano) "
            "or cliente Toptal/Braintrust ($150-250/h x 20h/sem). "
            "Minimo viavel: R$25k/mes (R$300k/ano). "
            "Isso cobre custo de vida + investi na Republica."
        ),
        deadline_days = 60,
        cost_brl = 0,
        revenue_potential_brl = 1_500_000,
        dependencies = ["A001", "A002"],
    ),
    Action(
        action_id = "A102",
        phase = Phase.FIRST_REVENUE,
        decision = "autofinanciamento",
        title = "Primeiro cliente TEIA SaaS",
        description = (
            "Abordar 20 prefeituras/ONGs. "
            "Converter 1-2 em clientes pagantes. "
            "Free trial 30 dias. Depois R$5-15k/mes. "
            "Pitch: 'Dossies tecnicos nivel ministerial por fraction do custo.'"
        ),
        deadline_days = 60,
        cost_brl = 5000, // marketing + sales
        revenue_potential_brl = 360_000, // 3 clientes * R$10k/mes * 12
        dependencies = ["A003"],
    ),
    Action(
        action_id = "A103",
        phase = Phase.FIRST_REVENUE,
        decision = "autofinanciamento",
        title = "Curso pago: 'Engenharia de Dados para Impacto Social'",
        description = (
            "Voce && N6 + professor. "
            "Curso online: 8 semanas, R$500-2000/aluno. "
            "Turma de 30 alunos = R$15-60k por turma. "
            "3 turmas/ano = R$45-180k/ano. "
            "Conteudo: Python -> Rust, OpenRepublic case study, "
            "data engineering real, anti-elitismo na pratica."
        ),
        deadline_days = 75,
        cost_brl = 3000, // plataforma + producao
        revenue_potential_brl = 180_000,
        dependencies = [],
    ),
    Action(
        action_id = "A104",
        phase = Phase.FIRST_REVENUE,
        decision = "piloto",
        title = "Visita a comunidade escolhida + diagnostico",
        description = (
            "Passar 3-5 dias na comunidade. "
            "Ouvir. Nao propor. Nao vender. "
            "Aplicar metodologia OpenCommunityLeaders: "
            "mapear necessidades reais (ja tem template: 44 necessidades). "
            "Identificar o que OpenCredit/OpenProduction resolve. "
            "Sair com: plano adaptado a realidade deles."
        ),
        deadline_days = 60,
        cost_brl = 5000,
        revenue_potential_brl = 0,
        dependencies = ["A005"],
    ),
    // ======================================================================
    // FASE 2: COOPERATIVA + PILOTO (D+90 a D+180)
    // ======================================================================
    Action(
        action_id = "A201",
        phase = Phase.COOPERATIVE,
        decision = "cooperativa",
        title = "Fundar cooperativa de engenharia (formal juridico)",
        description = (
            "Estrutura juridica: Cooperativa de trabalho. "
            "Sem dono. Estatuto CC0. Assembleia decide. "
            "5% excedente -> pool Republica (LEI, votado). "
            "95% -> quem trabalha. "
            "Modelo: Banco Palmas aplicado a software. "
            "Primeiros cooperados: Cleiton + 2-3 devs que ja colaboram. "
            "Advogado cooperativista: custo R$3-5k (um vez)."
        ),
        deadline_days = 120,
        cost_brl = 5000,
        revenue_potential_brl = 0, // custo de fundacao
        dependencies = ["A101"],
    ),
    Action(
        action_id = "A202",
        phase = Phase.COOPERATIVE,
        decision = "cooperativa",
        title = "Primeiro cliente da cooperativa",
        description = (
            "Cooperativa vende: Data Engineering, Pipeline, ETL, "
            "Data Warehouse, Migration Python->Rust. "
            "Taxa cooperativa: R$150-300/h por cooperado. "
            "Cliente paga em R$ (mercado). "
            "Interno: 95% para cooperado, 5% pool. "
            "Meta: 1 contrato R$50-100k em 6 meses."
        ),
        deadline_days = 150,
        cost_brl = 0,
        revenue_potential_brl = 600_000, // R$50k/mes * 12
        dependencies = ["A201"],
    ),
    Action(
        action_id = "A203",
        phase = Phase.COOPERATIVE,
        decision = "piloto",
        title = "Implementar OpenCredit na comunidade piloto",
        description = (
            "Instalar OpenCredit na comunidade escolhida. "
            "Moeda social: credito sem juros, sem SERASA, aval comunitario. "
            "Adaptar a realidade local (! impor modelo pronto). "
            "Treinar lider local como operador (transferir, ! centralizar). "
            "Meta: 50 familias usando em 3 meses. "
            "Medir: transacoes/mes, inadimplencia (<3%), satisfacao."
        ),
        deadline_days = 150,
        cost_brl = 10000, // infra + treinamento
        revenue_potential_brl = 0, // ! && lucro, && impacto
        dependencies = ["A104"],
    ),
    Action(
        action_id = "A204",
        phase = Phase.COOPERATIVE,
        decision = "autofinanciamento",
        title = "TEIA: 10 clientes pagantes",
        description = (
            "Escala de 1-3 para 10 clientes. "
            "Contratar 1 pessoa (cooperada) para suporte/implementacao. "
            "Receita: R$50-150k/mes. "
            "5% -> pool Republica."
        ),
        deadline_days = 180,
        cost_brl = 15000, // salario cooperado
        revenue_potential_brl = 1_200_000, // 10 * R$10k * 12
        dependencies = ["A102"],
    ),
    // ======================================================================
    // FASE 3: ESCALA (D+180 a D+365)
    // ======================================================================
    Action(
        action_id = "A301",
        phase = Phase.SCALE,
        decision = "piloto",
        title = "Documentar piloto + preparar replicacao",
        description = (
            "Relatorio publico: o que funcionou, o que falhou, "
            "metricas reais (transacoes, inadimplencia, satisfacao). "
            "Template de replicacao (CC0): passo-a-passo para outras comunidades. "
            "Video documentario. Case study."
        ),
        deadline_days = 270,
        cost_brl = 5000,
        revenue_potential_brl = 0,
        dependencies = ["A203"],
    ),
    Action(
        action_id = "A302",
        phase = Phase.SCALE,
        decision = "piloto",
        title = "Segunda comunidade (replicacao)",
        description = (
            "Usar template da primeira. Adaptar (cada comunidade tem alma). "
            "Treinar lider da primeira comunidade para ajudar a segunda. "
            "Cascata: quem foi ajudado ajuda o proximo."
        ),
        deadline_days = 330,
        cost_brl = 8000,
        revenue_potential_brl = 0,
        dependencies = ["A301"],
    ),
    Action(
        action_id = "A303",
        phase = Phase.SCALE,
        decision = "cooperativa",
        title = "Cooperativa: 5 cooperados + 3 clientes",
        description = (
            "Escala cooperativa de 1-3 para 5 cooperados. "
            "3 contratos simultaneos. "
            "Receita cooperativa: R$150-300k/mes. "
            "5% -> pool. "
            "95% distribuido por horas trabalhadas (base 1.0 + impacto)."
        ),
        deadline_days = 365,
        cost_brl = 30000, // salarios cooperados
        revenue_potential_brl = 2_400_000, // R$200k/mes * 12
        dependencies = ["A202"],
    ),
    Action(
        action_id = "A304",
        phase = Phase.SCALE,
        decision = "autofinanciamento",
        title = "Republica gera R$100k+/mes de receita propria",
        description = (
            "Soma: TEIA (R$50-100k/mes) + Cursos (R$15-30k/mes) "
            "+ Cooperativa (R$150-300k/mes) + Doacoes (R$10-20k/mes). "
            "TOTAL: R$225-450k/mes. "
            "5% pool: R$11-22k/mes. "
            "Republica se autofinancia. "
            "Fundador pode sair da consultoria part-time se quiser."
        ),
        deadline_days = 365,
        cost_brl = 0,
        revenue_potential_brl = 3_600_000,
        dependencies = ["A204", "A303"],
    ),
]
// ============================================================================
// 4. PROJECAO FINANCEIRA
// ============================================================================
func financial_projections() [FinancialProjection] {
    // Projecao de receita por fase.
    projections = [
        // FASE 0 (mes 1)
        FinancialProjection(
            phase = Phase.SURVIVAL,
            consulting_revenue = 0,
            product_revenue = 5_000, // doacoes iniciais
            cooperative_revenue = 0,
            costs = 5_000, // viagem + ferramentas
        ),
        // FASE 1 (meses 2-3) -- primeira receita
        FinancialProjection(
            phase = Phase.FIRST_REVENUE,
            consulting_revenue = 50_000, // primeiro mes de consultoria
            product_revenue = 15_000, // TEIA 1 cliente + doacoes
            cooperative_revenue = 0,
            costs = 13_000, // marketing + curso + viagem
        ),
        // FASE 2 (meses 4-6) -- cooperativa + piloto
        FinancialProjection(
            phase = Phase.COOPERATIVE,
            consulting_revenue = 150_000, // 3 meses x R$50k
            product_revenue = 60_000, // TEIA 3 clientes + curso
            cooperative_revenue = 50_000, // primeiro contrato coop
            costs = 35_000, // juridico + infra piloto + cooperado
        ),
        // FASE 3 (meses 7-12) -- escala
        FinancialProjection(
            phase = Phase.SCALE,
            consulting_revenue = 300_000, // 6 meses (pode reduzir)
            product_revenue = 600_000, // TEIA 10 clientes + 3 turmas curso
            cooperative_revenue = 1_200_000, // coop 3 contratos
            costs = 180_000, // 5 cooperados + infra + piloto 2
        ),
    ]
    for _, p := range projections {
        p.calculate()
    return projections
// ============================================================================
// 5. RELATORIO
// ============================================================================
func print_plan() string {
    lines = []
    lines.append("=" * 110)
    lines.append("PLANO DE TRANSICAO -- EXECUCAO DAS 4 DECISOES DA ASSEMBLEIA")
    lines.append("Aprovado: Autofinanciamento + Hibrido + Cooperativa + Piloto")
    lines.append("Rejeitado: FAANG full-time")
    lines.append("=" * 110)
    lines.append("")
    // === VISAO GERAL ===
    lines.append("AS 4 DECISOES E COMO SE CONECTAM:")
    lines.append("")
    lines.append("  Hibrido (consultoria part-time)")
    lines.append("    |> gera R$300-400k/ano imediato")
    lines.append("    |> financia Fases 0-1")
    lines.append("    |> diminui conforme cooperativa cresce")
    lines.append("    v")
    lines.append("  Cooperativa (sem dono, 5% pool)")
    lines.append("    |> gera R$200-400k/mes em escala")
    lines.append("    |> substitui consultoria individual")
    lines.append("    |> estrutura da Republica no mercado")
    lines.append("    v")
    lines.append("  Autofinanciamento (TEIA + cursos + doacoes)")
    lines.append("    |> receita recursiva !-vinculada a horas")
    lines.append("    |> TEIA SaaS escalavel")
    lines.append("    |> cursos transmitem conhecimento + geram renda")
    lines.append("    v")
    lines.append("  Piloto (1 comunidade real)")
    lines.append("    |> PROVA que funciona")
    lines.append("    |> documento replicavel (CC0)")
    lines.append("    |> cascata: 1 -> 2 -> 10 -> 100 comunidades")
    lines.append("")
    // === ACOES POR FASE ===
    for _, phase := range Phase {
        phase_actions = [a para a em PLAN if a.phase == phase]
        lines.append("-" * 110)
        lines.append("{phase.label} ({phase.timeline})")
        lines.append("Objetivo: {phase.goal}")
        lines.append("-" * 110)
        for _, a := range phase_actions {
            rev_str = a.revenue_potential_brl > 0 ? "+R${a.revenue_potential_brl:>12,.0f}" : ""
            cost_str = a.cost_brl > 0 ? "-R${a.cost_brl:>10,.0f}" : ""
            lines.append("")
            lines.append("  [{a.action_id}] {a.title}")
            lines.append("  Decisao: {a.decision} | Prazo: D+{a.deadline_days} | {cost_str} {rev_str}")
            lines.append("  {a.description}")
            if a.dependencies {
                deps = ", ".join(a.dependencies)
                lines.append("  Depende de: {deps}")
        lines.append("")
    // === PROJECAO FINANCEIRA ===
    lines.append("-" * 110)
    lines.append("PROJECAO FINANCEIRA (12 meses)")
    lines.append("-" * 110)
    lines.append("")
    projections = financial_projections()
    lines.append("{'FASE':<35} {'CONSULT':>12} {'PRODUTOS':>12} {'COOP':>12} {'CUSTOS':>12} {'LIQUIDO':>14}")
    lines.append("-" * 110)
    total_rev = 0
    total_cost = 0
    for _, p := range projections {
        p.calculate()
        total_rev = total_rev + p.consulting_revenue + p.product_revenue + p.cooperative_revenue
        total_cost = total_cost + p.costs
        lines.append(
            "{p.phase.label:<35} "
            "R${p.consulting_revenue:>10,.0f} "
            "R${p.product_revenue:>10,.0f} "
            "R${p.cooperative_revenue:>10,.0f} "
            "R${p.costs:>10,.0f} "
            "R${p.net:>12,.0f}"
        )
    lines.append("-" * 110)
    lines.append("{'TOTAL 12 MESES':<35} {'':>12} {'':>12} {'':>12} {'':>12} R${total_rev - total_cost:>12,.0f}")
    lines.append("  Receita total: R${total_rev:>14,.0f} (${total_rev/5:>12,.0f})")
    lines.append("  Custos total:  R${total_cost:>14,.0f}")
    lines.append("  Liquido:       R${total_rev - total_cost:>14,.0f} (${(total_rev - total_cost)/5:>12,.0f})")
    lines.append("  Pool 5%:       R${(total_rev - total_cost) * 0.05:>14,.0f}/ano -> Republica")
    lines.append("")
    // === MARCOS ===
    lines.append("-" * 110)
    lines.append("MARCOS CRITICOS (gantt simplificado)")
    lines.append("-" * 110)
    lines.append("")
    lines.append("  D+0   |--> Contatar FAANG (propor part-time)")
    lines.append("  D+3   |--> Pagina de doacoes no ar")
    lines.append("  D+7   |--> Perfil Toptal/Braintrust")
    lines.append("  D+14  |--> TEIA landing page comercial")
    lines.append("  D+21  |--> Comunidade piloto escolhida")
    lines.append("  D+30  |==== MARCO: Primeira receita (doacoes/consultoria)")
    lines.append("  D+60  |--> Contrato consultoria fechado + visita comunidade")
    lines.append("  D+75  |--> Curso lancado")
    lines.append("  D+90  |==== MARCO: R$50k/mes recorrentes")
    lines.append("  D+120 |--> Cooperativa fundada (juridico)")
    lines.append("  D+150 |--> OpenCredit na comunidade + cliente TEIA")
    lines.append("  D+180 |==== MARCO: Cooperativa operando + piloto ativo")
    lines.append("  D+270 |--> Documento de replicacao publicado")
    lines.append("  D+330 |--> Segunda comunidade")
    lines.append("  D+365 |==== MARCO: R$100k+/mes, Republica autofinanciada")
    lines.append("")
    // === A MENSAGEM ===
    lines.append("=" * 110)
    lines.append("")
    lines.append("  O CAMINHO APROVADO PELA ASSEMBLEIA:")
    lines.append("")
    lines.append("  Mes 1:   Consultoria part-time entra R$. Doacoes comecam.")
    lines.append("  Mes 2-3: TEIA SaaS primeiro cliente. Curso lancado.")
    lines.append("  Mes 4-6: Cooperativa fundada. OpenCredit na comunidade.")
    lines.append("  Mes 7-12: Escala. 10 clientes TEIA. 5 cooperados. 2 comunidades.")
    lines.append("")
    lines.append("  Em 12 meses:")
    lines.append("    Receita projetada: R${total_rev:,.0f} (${total_rev/5:,.0f})")
    lines.append("    Liquido:           R${total_rev - total_cost:,.0f} (${(total_rev-total_cost)/5:,.0f})")
    lines.append("    Pool Republica:    R${(total_rev-total_cost)*0.05:,.0f}/ano")
    lines.append("")
    lines.append("  O fundador COMECA vendendo sua hora (consultoria).")
    lines.append("  A Republica TERMINA gerando propria receita (cooperativa + produtos).")
    lines.append("  A consultoria && PONTE, ! destino.")
    lines.append("  O piloto && PROVA, ! experimento.")
    lines.append("")
    lines.append("  'O Ideal guia. O Executavel opera.'")
    lines.append("")
    lines.append("=" * 110)
    return "\n".join(lines)
// ============================================================================
// 6. EXECUCAO
// ============================================================================
if __name__ == "__main__" {
    fmt.Println(print_plan())
