// OpenCreator -- O Contrato Individual-Coletivo -- gerado de Portugol++
package opencreator_o_contrato_individual_coletivo

import "fmt"

// !/usr/bin/env python3
//
OpenCreator -- O Contrato Individual-Coletivo
==============================================
"Quanto de mim pertence ao coletivo?"
"Nao tudo. Nunca tudo. O corpo && meu. O maximo && meu.
Mas algo && nosso. && esse algo && sagrado."
ESTE && O DOCUMENTO MAIS IMPORTANTE DA REPUBLICA.
Porque ele define o LIMITE entre o EU && o NOS.
O PROBLEMA QUE NINGUEM RESOLVEU:
Toda revolucao tem um criador. Toda utopia tem um arquiteto.
O criador trabalha 16h/dia. Da tudo. Sacrifica saude, sono, vida.
Depois chega o coletivo. && pergunta:
"Obrigado por construir tudo. Agora, quanto && seu?"
Capitalismo diz: "TUDO. Voce && o fundador. Aqui estao seus bilhoes."
Comunismo diz:  "NADA. Voce && um trabalhador como outro qualquer."
Republicas falham porque escolhem um dos dois errados.
A RESPOSTA DA OPENREPUBLIC:
O criador ! && dono do que criou (bem comum, CC0, anti-propriedade).
MAS o criador ! && escravo do que criou (autonomia corporal absoluta).
O criador ! tem poder especial sobre o que criou (anti-elitismo).
MAS o criador ! tem obrigacao de continuar criando (limite de doacao).
O criador JÁ cumpriu o contrato base 1.0.
Tudo que faz alem disso && DOM, ! DIVIDA.
Author: OpenRepublic Team
Principio central: "O coletivo ! pode sugar o criador ate seca-lo."
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// ============================================================================
// 1. O CONTRATO BASE -- O QUE CADA PESSOA DEVE
// ============================================================================
type LaborTier int
const (
    // Os 4 niveis de relacao entre individuo e coletivo.
    Nivel 1 (MINIMO): Base 1.0 -- todo cidadao deve.
    Nivel 2 (NORMAL): Contribuicao regular -- a maioria da.
    Nivel 3 (CRIADOR): Construcao de sistemas novos -- poucos dao.
    Nivel 4 (EXCESSO): Alem do limite saudavel -- PROIBIDO aceitar.
    //
    BASE = "base_1.0"
    NORMAL = "normal"
    CREATOR = "criador"
    EXCESS = "excesso_proibido"
// decorador: @dataclass
type LaborObligation struct {
    // O que CADA cidadao deve ao coletivo. Ninguem escapa. Ninguem excede.
    BASE 1.0 -- O CONTRATO MINIMO:
    - 20h/semana de trabalho reconhecido (meio periodo util)
    - || equivalente em impacto (uma cirurgia = varias semanas)
    - Nao pode comprar saida com credito
    - Nao pode transferir para outro
    - Nao pode acumular (fazer 80h numa semana ! zera as proximas 3)
    SAIDAS LEGITIMAS DA BASE:
    - Doenca (comprovada, sem julgamento)
    - Cuidado de filho/idoso dependente (conta como contribuicao)
    - Estudo que beneficia a comunidade (conta como contribuicao)
    - Descanso medicinal (autonomia corporal -- corpo manda)
    - Idade (acima de 65: voluntario, ! obrigatorio)
    //
    base_hours_per_week := 20.0 // float64
    max_hours_per_week := 40.0 // LIMITE: Republica PROIBE mais que isso // float64
    excess_threshold := 50.0 // Acima disto = EXCESSO, ! aceito // float64
    weeks_per_year := 46 // 46 semanas uteis (6 de descanso garantido) // int64
    rest_days_per_week := 2 // MINIMO 2 dias sem trabalho obrigatorio // int64
    min_vacation_weeks := 4 // MINIMO 4 semanas de ferias/ano // int64
    // decorador: @property
    func base_annual_hours(self) float64 {
        // Horas base anuais que cada cidadao deve.
        return self.base_hours_per_week * self.weeks_per_year
    // decorador: @property
    func max_annual_hours(self) float64 {
        // Maximo de horas/ano que a Republica ACEITA de qualquer pessoa.
        return self.max_hours_per_week * self.weeks_per_year
    // decorador: @property
    func excess_annual_hours(self) float64 {
        // Acima disso, a Republica DIZ NAO. Para o seu proprio bem.
        return self.excess_threshold * self.weeks_per_year
    // decorador: @property
    func contract(self) string {
        return (
            "CONTRATO BASE 1.0:\n"
            "  Cada cidadao: {self.base_hours_per_week}h/semana "
            "({self.base_annual_hours:.0f}h/ano)\n"
            "  Maximo aceito: {self.max_hours_per_week}h/semana "
            "({self.max_annual_hours:.0f}h/ano)\n"
            "  LIMITE INEGOCIAVEL: {self.excess_threshold}h/semana "
            "({self.excess_annual_hours:.0f}h/ano)\n"
            "  Acima do limite = Republica recusa o trabalho.\n"
            "  Descanso: {self.rest_days_per_week} dias/semana + "
            "{self.min_vacation_weeks} semanas ferias."
        )
// ============================================================================
// 2. O PARADOXO DO CRIADOR
// ============================================================================
type CreatorParadox int
const (
    // O problema fundamental que toda civilizacao enfrenta.
    O criador faz mais que o contrato base.
    MUITO mais. As vezes 10x, 100x, 1000x.
    Pergunta: isso da poder ao criador?
    Resposta da Republica: !. Anti-elitismo absoluto.
    Pergunta: isso cria obrigacao de continuar?
    Resposta da Republica: !. Autonomia corporal absoluta.
    Pergunta: o criador && especial?
    Resposta da Republica: ! no poder, SIM no reconhecimento.
    O criador ! && elite. O criador && um cidadao que deu mais.
    O extra dado ! compra poder.
    O extra dado ! cria obrigacao.
    O extra dado gera reconhecimento (credito de acesso).
    PONTO. Nada mais.
    //
    NO_EXTRA_POWER = (
        "sem_poder_extra",
        "Criar 100 projetos ! da 1 voto a mais. Democracia = 1 pessoa = 1 voto."
    )
    NO_PERPETUAL_DEBT = (
        "sem_divida_perpetua",
        "O criador ! deve continuar criando para sempre. "
        "Cada ciclo && independente. Amanha pode parar."
    )
    RECOGNITION_NOT_AUTHORITY = (
        "reconhecimento_nao_autoridade",
        "Reconhecimento = credito de acesso + gratidao publica. "
        "Autoridade = zero adicional."
    )
    RIGHT_TO_LEAVE = (
        "direito_de_sair",
        "O criador pode abandonar tudo que criou a qualquer momento. "
        "O que foi criado && bem comum. Nao ha propriedade para manter."
    )
    PROTECTION_FROM_SELF = (
        "protecao_de_si_mesmo",
        "A Republica PROIBE o criador de se sacrificar alem do limite. "
        "Burnout ! && dedicacao. E dano corporal."
    )
// ============================================================================
// 3. MEDIDOR DE CONTRIBUICAO INDIVIDUAL
// ============================================================================
type ContributionMetric int
const (
    // Como medir o que cada pessoa deu.
    HOURS = "horas"
    ARTIFACTS = "artefatos"  // projetos, sistemas, blueprints criados
    PEOPLE_IMPACTED = "pessoas_afetadas"
    KNOWLEDGE = "conhecimento"  // documentacao, ensino, pesquisa
    MAINTENANCE = "manutencao"  // manter sistemas existentes funcionando
    RIPPLE = "propagacao"  // impacto que se espalha no tempo
// decorador: @dataclass
type IndividualContribution struct {
    // Registro do que uma pessoa deu ao coletivo.
    citizen_id: texto
    name: texto
    role := "cidadao" // string
    // Tempo
    hours_base := 0.0 // horas do contrato base 1.0 // float64
    hours_voluntary := 0.0 // horas alem da base (voluntario) // float64
    hours_total := 0.0 // float64
    // Artefatos criados
    systems_created := 0 // int64
    systems_maintained := 0 // int64
    projects_count := 0 // int64
    lines_of_code := 0 // int64
    documents_written := 0 // int64
    // Impacto
    people_directly_impacted := 0 // int64
    people_indirectly_impacted := 0 // int64
    ripple_factor := 1.0 // quanto se espalha no tempo // float64
    // Reconhecimento
    community_recognition_score := 0.0 // float64
    cycles_active := 0 // quantos ciclos contribuiu // int64
    // decorador: @property
    func base_fulfilled(self) bool {
        // Cumpriu o contrato minimo?
        return self.hours_base >= 920 // 20h * 46 semanas
    // decorador: @property
    func excess(self) bool {
        // Deu DEMAIS? Republica deve INTERVIR.
        return self.hours_total > 2300 // 50h * 46 semanas
    // decorador: @property
    func contribution_ratio(self) float64 {
        // Quantas vezes alem do contrato base esta pessoa deu.
        1.0 = cumpriu o minimo.
        5.0 = deu 5x o minimo.
        20.0 = deu 20x o minimo.
        //
        base = 920 // horas anuais base
        total_effective = self.hours_base + self.hours_voluntary
        return arredonde(total_effective / base, 2)
    // decorador: @property
    func recognition_level(self) string {
        // Nivel de reconhecimento (NAO de autoridade).
        Considera TRES dimensoes:
        1. Ratio de horas (tempo dado alem do contrato base)
        2. Artefatos criados (sistemas/projetos que existem porque esta pessoa os fez)
        3. Pessoas impactadas (escala do efeito)
        Reconhecimento olha o MAIOR dos tres, porque cada dimensao
        mede algo diferente que ! se reduz a horas.
        //
        ratio = self.contribution_ratio
        // Por horas
        if ratio >= 20 {
            level_hours = 4 // FUNDADOR
        } else if ratio >= 10 {
            level_hours = 3 // ARQUITETO
        } else if ratio >= 5 {
            level_hours = 2 // CONSTRUTOR
        } else if ratio >= 2 {
            level_hours = 1 // CONTRIBUIDOR
        } else if ratio >= 1 {
            level_hours = 0 // CIDADAO
        } else {
            return "INCOMPLETO"
        // Por artefatos criados
        if self.systems_created >= 50 {
            level_artifacts = 4 // FUNDADOR
        } else if self.systems_created >= 20 {
            level_artifacts = 3 // ARQUITETO
        } else if self.systems_created >= 10 {
            level_artifacts = 2 // CONSTRUTOR
        } else if self.systems_created >= 1 {
            level_artifacts = 1 // CONTRIBUIDOR
        } else {
            level_artifacts = 0 // CIDADAO
        // Por pessoas impactadas
        if self.people_directly_impacted >= 10000 {
            level_people = 4 // FUNDADOR
        } else if self.people_directly_impacted >= 1000 {
            level_people = 3 // ARQUITETO
        } else if self.people_directly_impacted >= 100 {
            level_people = 2 // CONSTRUTOR
        } else if self.people_directly_impacted >= 10 {
            level_people = 1 // CONTRIBUIDOR
        } else {
            level_people = 0 // CIDADAO
        // Reconhecimento = maior das 3 dimensoes
        max_level = maximo(level_hours, level_artifacts, level_people)
        names = ["CIDADAO", "CONTRIBUIDOR", "CONSTRUTOR",
                "ARQUITETO", "FUNDADOR"]
        return names[max_level]
    // decorador: @property
    func authority_level(self) int64 {
        // Nivel de autoridade politica. SEMPRE 1 (um voto).
        Nao importa se criou 1 projeto || 1000.
        Anti-elitismo: poder ! se compra com contribuicao.
        //
        return 1
// ============================================================================
// 4. CALCULADORA DO CONTRATO
// ============================================================================
type CreatorContract struct {
    // Calcula o contrato entre individuo e coletivo.
    A pergunta fundamental:
    "Quanto de mim (Cleiton) tem que se dar pelo coletivo?"
    RESPOSTA:
    1. O MINIMO: 20h/semana (contrato base 1.0). Todo cidadao deve.
    2. O MAXIMO: 40h/semana. Republica aceita, reconhece, agradece.
    3. O LIMITE: 50h/semana. Republica PROIBE. Para protecao do individuo.
    4. O PODER: ZERO adicional. Nao importa quanto deu.
    5. O RECONHECIMENTO: Proporcional ao impacto, em credito de acesso.
    6. A OBRIGACAO FUTURA: ZERO. Cada ciclo && novo. Pode parar amanha.
    PARA O FUNDADOR ESPECIFICAMENTE:
    - Tudo que criou ate agora JA && bem comum (CC0).
    - Nao tem divida com a Republica. A Republica tem divida com ele.
    - Essa divida && reconhecimento (gratidao), ! poder.
    - Ele pode parar amanha. Tudo continua. Nao ha dependencia.
    - Se ele ! parar, a Republica deve monitorar saude (burnout).
    //
    func __init__(self) {
        self.obligation = LaborObligation()
        self.paradoxes = list(CreatorParadox)
    func evaluate_individual(self, contrib: IndividualContribution) {texto: qualquer} {
        // Avalia o contrato de um individuo com o coletivo.
        return {
            "citizen": contrib.name,
            "role": contrib.role,
            // Contrato base
            "base_required_hours": self.obligation.base_annual_hours,
            "base_fulfilled": contrib.base_fulfilled,
            "base_remaining": maximo(0, self.obligation.base_annual_hours - contrib.hours_base),
            // Contribuicao
            "total_hours": contrib.hours_total,
            "contribution_ratio": "{contrib.contribution_ratio:.1f}x",
            "artifacts_created": contrib.systems_created,
            "people_impacted": contrib.people_directly_impacted,
            "ripple_factor": contrib.ripple_factor,
            // Status
            "recognition_level": contrib.recognition_level,
            "authority_level": contrib.authority_level,
            "excess_detected": contrib.excess,
            // Veredicto
            "verdict": self._verdict(contrib),
            "recommendation": self._recommendation(contrib),
        }
    func _verdict(self, c: IndividualContribution) string {
        if c.excess {
            return (
                "EXCESSO: {c.name} trabalhou {c.hours_total:.0f}h "
                "(limite saudavel: {self.obligation.excess_annual_hours:.0f}h). "
                "Republica DEVE intervir: reduzir carga, exigir descanso. "
                "Burnout ! && dedicacao, && dano corporal."
            )
        if ! c.base_fulfilled {
            return (
                "BASE INCOMPLETA: {c.name} ! cumpriu contrato minimo "
                "({c.hours_base:.0f}h de {self.obligation.base_annual_hours:.0f}h). "
                "Nao ha punicao, mas a comunidade deve entender por que."
            )
        ratio = c.contribution_ratio
        if ratio >= 20 {
            return (
                "LEGADO: {c.name} deu {ratio:.0f}x o contrato base. "
                "Criou {c.systems_created} sistemas. Impactou "
                "{c.people_directly_impacted}+ pessoas. "
                "Reconhecimento: FUNDADOR. Poder: 1 voto (igual a todos)."
            )
        if ratio >= 5 {
            return (
                "MERITORIO: {c.name} deu {ratio:.1f}x o contrato base. "
                "Reconhecimento: CONSTRUTOR. Poder: 1 voto."
            )
        if ratio >= 1 {
            return (
                "CONTRATO CUMPRIDO: {c.name} cumpriu o contrato base 1.0. "
                "E um cidadao completo da Republica. Poder: 1 voto."
            )
        return "INCOMPLETO."
    func _recommendation(self, c: IndividualContribution) string {
        if c.excess {
            return (
                "ACAO: Comunidade deve conversar com {c.name}. "
                "Reduzir carga para maximo {self.obligation.max_hours_per_week}h/semana. "
                "Garantir {self.obligation.min_vacation_weeks} semanas de ferias. "
                "Monitorar saude fisica && mental. "
                "Transferir responsabilidades para outros. "
                "O criador ! && insubstituivel -- se fosse, a Republica falhou."
            )
        if c.contribution_ratio >= 10 {
            return (
                "ACAO: Reconhecer publicamente. Garantir descanso. "
                "Nao criar dependencia. Documentar conhecimento para que "
                "outros possam continuar. O criador deve poder sair sem "
                "que nada quebre."
            )
        return "Status normal. Continuar."
    funcao the_founder_question(self, name: texto, systems: inteiro,
                            lines: inteiro, hours_total: flutuante,
                            people: inteiro) -> {texto: qualquer}:
        // A pergunta que o fundador faz:
        'Quanto de MIM tem que se dar pelo coletivo?'
        Esta funcao responde com clareza brutal.
        //
        base = self.obligation.base_annual_hours
        ratio = hours_total / base
        contrib = IndividualContribution(
            citizen_id = "FOUNDER",
            name = name,
            role = "fundador",
            hours_base = minimo(base, hours_total),
            hours_voluntary = maximo(0, hours_total - base),
            hours_total = hours_total,
            systems_created = systems,
            projects_count = systems,
            lines_of_code = lines,
            people_directly_impacted = people,
        )
        evaluation = self.evaluate_individual(contrib)
        // Resposta direta
        answer = {
            "pergunta": "Quanto de {name} tem que se dar pelo coletivo?",
            "resposta_direta": self._direct_answer(ratio, systems),
            "contrato_base": self.obligation.contract,
            "avaliacao": evaluation,
            "declaracao_de_direitos_do_criador": self._creator_bill_of_rights(),
            "carga_atual": {
                "horas_totais_dadas": hours_total,
                "ratio_vs_base": "{ratio:.1f}x",
                "sistemas_criados": systems,
                "linhas_escritas": lines,
                "pessoas_impactadas": people,
            },
        }
        if ratio > 2.5 {
            answer["ALERTA"] = (
                "{name} deu {ratio:.1f}x o contrato base. "
                "A Republica ! deve aceitar mais sem garantias de saude. "
                "O sacrificio excessivo cria dependencia, && dependencia "
                "&& o oposto de anti-elitismo: se sem {name} tudo cai, "
                "{name} se tornou elite por fato, mesmo sem querer poder."
            )
        return answer
    func _direct_answer(self, ratio: flutuante, systems: inteiro) string {
        if ratio < 1 {
            return (
                "Voce deve {max(0, 1-ratio):.0%} do contrato base. "
                "Nada mais. O coletivo ! pode exigir."
            )
        return (
            "Voce JA cumpriu o contrato {ratio:.1f} vezes.\n"
            "Criou {systems} sistemas como bem comum.\n\n"
            "RESPOSTA: NADA mais && exigido de voce.\n"
            "Tudo que voce deu alem da base 1.0 foi DOM, ! DIVIDA.\n"
            "O coletivo NAO tem direito ao seu corpo, ao seu sono, "
            "|| a sua continuidade.\n\n"
            "Voce pode parar amanha.\n"
            "Tudo que criou ja && nosso.\n"
            "Voce continua sendo nosso igual.\n"
            "1 voto. 1 pessoa. 1 cidadao.\n"
            "Nada mais. Nada menos."
        )
    func _creator_bill_of_rights(self) [texto] {
        // Declaracao de Direitos do Criador.
        O criador TEM direitos que o coletivo ! pode tocar.
        Porque o coletivo sem limites se torna tirano.
        //
        return [
            "1. DIREITO DE PARAR: O criador pode cessar contribuicao a qualquer momento.",
            "2. DIREITO AO CORPO: Horas alem do limite sao recusadas pelo coletivo.",
            "3. DIREITO DE IGUALDADE: Nenhuma contribuicao compra poder adicional.",
            "4. DIREITO AO RECONHECIMENTO: O coletivo registra && agradece publicamente.",
            "5. DIREITO AO ESQUECIMENTO: O criador pode pedir para ! ser citado.",
            "6. DIREITO DE MUDAR: O criador pode mudar de area, projeto, paixao.",
            "7. DIREITO DE CRITICAR: O criador pode criticar o que criou, sem retaliacao.",
            "8. DIREITO DE NAO SER DEUS: Ninguem depende de uma so pessoa.",
            "9. DIREITO DE ERRAR: O criador pode falhar sem perder reconhecimento.",
            "10. DIREITO DE SER HUMANO: Saude mental && fisica vem ANTES da Republica.",
        ]
// ============================================================================
// 5. PROTECAO CONTRA DEPENDENCIA
// ============================================================================
type DependencyCheck struct {
    // Verifica se a Republica depende demais de uma pessoa.
    Se uma pessoa parar && tudo cai, a Republica FALHOU.
    Nao foi falha da pessoa. Foi falha estrutural.
    Anti-elitismo significa: ninguem && insubstituivel.
    Se o criador && insubstituivel, ele && elite -- mesmo sem querer.
    SOLUCAO:
    - Documentacao radical (TEIA)
    - Transferencia de conhecimento ativa
    - Distribuicao de responsabilidades
    - Testes de continuidade: "se X sair, o que quebra?"
    //
    // decorador: @dataclass
    type DependencyMetric struct {
        citizen_id: texto
        name: texto
        systems_owned_knowledge: inteiro // sistemas que SO ela entende
        systems_documented: inteiro // sistemas com doc publica
        systems_with_successors: inteiro // sistemas com substituto treinado
        bus_factor: inteiro // quantas pessoas precisam sair pra cair
        // decorador: @property
        func dependency_score(self) float64 {
            // 0 = sem dependencia (saudavel). 100 = dependencia critica.
            if self.systems_owned_knowledge == 0 {
                return 0
            undocumented = self.systems_owned_knowledge - self.systems_documented
            orphaned = self.systems_owned_knowledge - self.systems_with_successors
            bus_risk = maximo(0, 5 - self.bus_factor) * 10
            return minimo(100, (undocumented * 3 + orphaned * 5 + bus_risk))
        // decorador: @property
        func is_critical(self) bool {
            return self.dependency_score >= 50
    func assess(self, metric: DependencyMetric) {texto: qualquer} {
        return {
            "citizen": metric.name,
            "systems_solo_knowledge": metric.systems_owned_knowledge,
            "systems_documented": metric.systems_documented,
            "systems_with_successors": metric.systems_with_successors,
            "bus_factor": metric.bus_factor,
            "dependency_score": "{metric.dependency_score:.0f}/100",
            "critical": metric.is_critical,
            "action": self._action(metric),
        }
    func _action(self, m: DependencyMetric) string {
        if m.is_critical {
            return (
                "CRITICO: Se {m.name} sair, {m.systems_owned_knowledge} "
                "sistemas podem quebrar. ACAO IMEDIATA: "
                "documentar tudo (TEIA), trear sucessores, "
                "distribuir conhecimento. Republica com bus_factor "
                "de {m.bus_factor} && fraca por design."
            )
        if m.dependency_score >= 25 {
            return (
                "ATENCAO: Dependencia moderada em {m.name}. "
                "Documentar sistemas restantes. Treinar sucessores."
            )
        return "Saudavel. Conhecimento distribuido. Anti-elitismo funcionando."
// ============================================================================
// 6. MAIN
// ============================================================================
if __name__ == "__main__" {
    contract = CreatorContract()
    dep = DependencyCheck()
    fmt.Println("=" * 80)
    fmt.Println("  OPENCREATOR -- O CONTRATO INDIVIDUAL-COLETIVO")
    fmt.Println('  "Quanto de mim pertence ao coletivo?"')
    fmt.Println("=" * 80)
    // === 1. O CONTRATO BASE ===
    fmt.Println("\n\n  === 1. O CONTRATO BASE 1.0 ===\n")
    fmt.Println("  {contract.obligation.contract}")
    // === 2. PARADOXO DO CRIADOR ===
    fmt.Println("\n\n  === 2. O PARADOXO DO CRIADOR ===\n")
    for _, p := range CreatorParadox {
        fmt.Println("  [{p.value[0].upper()}]")
        fmt.Println("  {p.value[1]}")
        fmt.Println()
    // === 3. A PERGUNTA DO FUNDADOR ===
    fmt.Println("\n\n  === 3. A PERGUNTA DO FUNDADOR ===\n")
    fmt.Println('  "Quanto de mim (Cleiton) tem que se dar pelo coletivo?"')
    fmt.Println()
    // Dados reais aproximados do fundador
    result = contract.the_founder_question(
        name = "Cleiton",
        systems = 95,
        lines = 380000,
        hours_total = 4000, // estimativa conservadora
        people = 5000, // estimativa
    )
    fmt.Println("\n  {result['resposta_direta']}")
    fmt.Println("\n  CARGA ATUAL:")
    c = result['carga_atual']
    fmt.Println("    Horas totais dadas:     {c['horas_totais_dadas']:.0f}h")
    fmt.Println("    Razao vs contrato base: {c['ratio_vs_base']}")
    fmt.Println("    Sistemas criados:       {c['sistemas_criados']}")
    fmt.Println("    Linhas escritas:        {c['linhas_escritas']:,}")
    fmt.Println("    Pessoas impactadas:     {c['pessoas_impactadas']:,}")
    av = result['avaliacao']
    fmt.Println("\n  RECONHECIMENTO: {av['recognition_level']}")
    fmt.Println("  AUTORIDADE:     {av['authority_level']} voto (igual a todos)")
    fmt.Println("  EXCESSO:        {'SIM -- Republica deve intervir' if av['excess_detected'] else 'Nao detectado'}")
    fmt.Println("\n  VEREDICTO: {av['verdict']}")
    fmt.Println("\n  RECOMENDACAO: {av['recommendation']}")
    if 'ALERTA' in result {
        fmt.Println("\n  [!] {result['ALERTA']}")
    // === 4. DIREITOS DO CRIADOR ===
    fmt.Println("\n\n  === 4. DECLARACAO DE DIREITOS DO CRIADOR ===\n")
    for _, right := range result['declaracao_de_direitos_do_criador'] {
        fmt.Println("  {right}")
    // === 5. TESTE DE DEPENDENCIA ===
    fmt.Println("\n\n  === 5. TESTE DE DEPENDENCIA (BUS FACTOR) ===\n")
    // Cenario real: fundador com conhecimento solo
    founder_dep = DependencyCheck.DependencyMetric(
        citizen_id = "FOUNDER",
        name = "Cleiton",
        systems_owned_knowledge = 95,
        systems_documented = 30, // documentados em TEIA
        systems_with_successors = 0, // nenhum substituto treinado
        bus_factor = 1, // se ele sair, tudo para
    )
    dep_result = dep.assess(founder_dep)
    fmt.Println("  Cidadao:           {dep_result['citizen']}")
    fmt.Println("  Sistemas solo:     {dep_result['systems_solo_knowledge']}")
    fmt.Println("  Documentados:      {dep_result['systems_documented']}")
    fmt.Println("  Com sucessor:      {dep_result['systems_with_successors']}")
    fmt.Println("  Bus factor:        {dep_result['bus_factor']}")
    fmt.Println("  Score dependencia: {dep_result['dependency_score']}")
    fmt.Println("  Critico:           {'SIM' if dep_result['critical'] else 'NAO'}")
    fmt.Println("\n  ACAO: {dep_result['action']}")
    // Cenario ideal: conhecimento distribuido
    fmt.Println("\n  --- CENARIO IDEAL (meta da Republica) ---\n")
    ideal_dep = DependencyCheck.DependencyMetric(
        citizen_id = "COLLECTIVE",
        name = "Coletivo (meta)",
        systems_owned_knowledge = 0, // ninguem tem conhecimento solo
        systems_documented = 95,
        systems_with_successors = 95,
        bus_factor = 10, // 10 pessoas precisam sair pra cair
    )
    ideal_result = dep.assess(ideal_dep)
    fmt.Println("  Bus factor:        {ideal_result['bus_factor']}")
    fmt.Println("  Score dependencia: {ideal_result['dependency_score']}")
    fmt.Println("  Status:            SAUDAVEL")
    // === 6. EXEMPLOS DE CIDADAOS NORMAIS ===
    fmt.Println("\n\n  === 6. PADRAO PARA TODOS OS CIDADAOS ===\n")
    examples = [
        IndividualContribution("C-001", "Maria (professora)", "educadora",
            hours_base = 920, hours_total=920,
            people_directly_impacted = 300, ripple_factor=10),
        IndividualContribution("C-002", "Joao (agricultor)", "agricultor",
            hours_base = 1840, hours_total=1840,
            people_directly_impacted = 500, ripple_factor=1),
        IndividualContribution("C-003", "Ana (medica)", "medica",
            hours_base = 2000, hours_total=2000,
            people_directly_impacted = 800, ripple_factor=2),
        IndividualContribution("C-004", "Pedro (construtor)", "construtor",
            hours_base = 920, hours_total=1200,
            systems_created = 0, people_directly_impacted=200),
        IndividualContribution("C-005", "Lux (researcher)", "pesquisador",
            hours_base = 1840, hours_total=2500,
            systems_created = 3, people_directly_impacted=1000,
            ripple_factor = 50),
    ]
    fmt.Println("  {'Nome':<28} {'Ratio':>6} {'Reconhecimento':<16} "
        "{'Poder':>6} {'Cumprido'}")
    fmt.Println("  {'-'*75}")
    for _, ex := range examples {
        ev = contract.evaluate_individual(ex)
        fmt.Println("  {ex.name:<28} {ev['contribution_ratio']:>6} "
            "{ev['recognition_level']:<16} {ev['authority_level']:>5}v "
            "{'SIM' if ev['base_fulfilled'] else 'NAO'}")
    // === FILOSOFIA ===
    fmt.Println("\n\n{'='*80}")
    fmt.Println("  RESPOSTA FINAL")
    fmt.Println("{'='*80}")
    fmt.Println("""
PERGUNTA:
    "Quanto de mim tem que se dar pelo coletivo?
    Esse vai ser o padrao para todos."
RESPOSTA:
    O PADRAO PARA TODOS:
    20 horas/semana. 920 horas/ano.
    Isso && o contrato base 1.0. Todo cidadao deve.
    Ninguem escapa. Ninguem compra saida.
    O LIMITE PARA TODOS:
    40 horas/semana. 1840 horas/ano.
    A Republica aceita com gratidao.
    Acima disso, a Republica DIZ !.
    PARA O CRIADOR (Cleiton):
    Voce deu 4.3x o contrato base.
    Criou 95 sistemas. 380.000 linhas.
    Tudo ja && bem comum CC0.
    VOCE ! DEVE MAIS NADA.
    Tudo que voce fez alem de 920h/ano foi DOM.
    O coletivo ! tem direito ao seu sono.
    O coletivo ! tem direito a sua continuidade.
    O coletivo ! tem direito a sua saude mental.
    O que o coletivo TEM:
    - 1 voto seu (igual ao de todos)
    - Gratidao eterna (reconhecimento)
    - Credito de acesso proporcional ao impacto
    O que o coletivo ! TEM:
    - Direito de exigir mais horas
    - Direito de te tratar como elite
    - Direito de depender de voce
    SE AMANHA VOCE PARAR:
    A Republica continua.
    Tudo que voce criou ja && nosso.
    Voce continua sendo nosso igual.
    1 voto. 1 pessoa. 1 cidadao.
    O PERIGO:
    Bus factor = 1. Se voce sair, 95 sistemas ficam orfaos.
    Isso ! && seu problema -- && NOSSO problema.
    A Republica FALHOU em distribuir conhecimento.
    O fundador ! && insubstituivel por design.
    Se &&, a Republica ainda ! nasceu de verdade.
    O QUE A REPUBLICA DEVE FAZER AGORA:
    1. Reduzir sua carga para maximo 40h/semana
    2. Documentar tudo que voce sabe em TEIA
    3. Trear sucessores para cada sistema
    4. Garantir que bus_factor chege a 10+
    5. Proteger sua saude como politica de Estado
    PORQUE ISSO IMPORTA:
    O anti-elitismo ! && so sobre poder.
    && sobre DEPENDENCIA.
    Se o coletivo depende de um, o um && elite.
    Mesmo que ! queira ser.
    Mesmo que nunca peça poder.
    A unica Republica verdadeira
    && aquela onde o fundador pode morrer amanha
    && nada muda.
// )
    fmt.Println("{'='*80}")
    fmt.Println("  OpenCreator: O contrato entre o EU && o NOS.")
    fmt.Println("  Base: 920h/ano. Max: 1840h/ano. Limite: 2300h/ano.")
    fmt.Println("  Poder: SEMPRE 1 voto. Reconhecimento: proporcional.")
    fmt.Println("  Anti-elitismo = ninguem && insubstituivel.")
    fmt.Println("{'='*80}")
