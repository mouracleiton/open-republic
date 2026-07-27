// OpenDebtImpact -- Todos os Impactos da Divida na Vida Humana
// ====================================================================
// "A divida nao so mata. Ela CASTRA.
// Castra a educacao. Castra a ciencia. Castra a moradia.
// Castra o futuro. Cada real pro agiota e um real roubado
// de cada area que faz a vida valer a pena."
//
// Este modulo simula o impacto da divida em TODAS as dimensoes
// da vida brasileira. Nao so mortes (OpenDebtMortality) -- mas
// tudo que a divida DESTRÓI silenciosamente:
//
// 1. EDUCACAO: escolas, professores, alfabetizacao
// 2. SAUDE MENTAL: depressao, ansiedade, suicidio
// 3. MORADIA: sem-teto, favelas, habitacao
// 4. SEGURANCA ALIMENTAR: fome, desnutricao
// 5. INFRAESTRUTURA: estradas, transporte, energia
// 6. SANEAMENTO: agua, esgoto, lixo
// 7. CIENCIA & TECNOLOGIA: pesquisa, inovacao, patentes
// 8. CULTURA & ARTE: museus, teatro, musica
// 9. DESIGUALDADE: renda, genero, raca
// 10. MEIO AMBIENTE: desmatamento, poluicao
// 11. SEGURANCA: policia, violencia
// 12. ESPORTE: educacao fisica, lazer
// 13. TRANSPORTES: metro, onibus, mobilidade
// 14. COMUNICACOES: internet, conectividade
// 15. INFANCIA: creches, primeira infancia
//
// Para cada area, calcula ano a ano:
// - Quanto foi ROUBADO pelo juros da divida
// - O que esse dinheiro teria construido
// - Quantas pessoas foram afetadas
// - O impacto cumulativo em 20 anos
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

package main

import (
	"fmt"
	"math"
)

// ============================================================================
// 1. AREAS DE IMPACTO
// ============================================================================

type ImpactArea int

const (
	IMPACT_EDUCATION ImpactArea = iota
	IMPACT_HEALTH_MENTAL
	IMPACT_HOUSING
	IMPACT_FOOD_SECURITY
	IMPACT_INFRASTRUCTURE
	IMPACT_SANITATION
	IMPACT_SCIENCE_TECH
	IMPACT_CULTURE_ARTS
	IMPACT_INEQUALITY
	IMPACT_ENVIRONMENT
	IMPACT_SECURITY
	IMPACT_SPORT
	IMPACT_TRANSPORT
	IMPACT_CONNECTIVITY
	IMPACT_CHILDHOOD
)

type SeverityLevel int

const (
	SEVERITY_CRITICAL SeverityLevel = iota
	SEVERITY_SEVERE
	SEVERITY_HIGH
	SEVERITY_MODERATE
	SEVERITY_LOW
)

type AreaImpact struct {
	area                        ImpactArea
	name                        string
	severity                    SeverityLevel
	annualBudgetNeededBrl       float64
	annualBudgetActualBrl       float64
	annualBudgetGapBrl          float64
	pctOfInterestThatShouldGo   float64
	peopleAffectedPerYear       int
	unitCostBrl                 float64
	unitName                    string
	unitsNotDeliveredPerYear    int
	description                 string
	humanCost                   string
}

type YearImpact struct {
	yearLabel               int
	interestPaidBrl         float64
	totalGapBrl             float64
	totalPeopleAffected     int
	cumulativeGapBrl        float64
	cumulativePeopleAffected int
}

type ImpactSimulator struct {
	startYear   int
	years       int
	initialDebt float64
	initialGdp  float64
	interestRate float64
	gdpGrowth   float64
	simulations []YearImpact
}

// ============================================================================
// 2. CATALOGO DE IMPACTOS (15 areas) - Portuguese comments
// ============================================================================

var AREA_IMPACTS = []AreaImpact{
	{IMPACT_EDUCATION, "Educacao Basica e Superior", SEVERITY_CRITICAL,
		600e9, 180e9, 420e9, 0.15, 50000000, 5e6, "escolas", 84000,
		"Educacao publica subfinanciada ha decadas.",
		"Criancas em escolas sem teto, sem merenda, sem professor. Universitarios sem bolsa. Analfabetismo funcional em 30% dos adultos."},
	{IMPACT_HEALTH_MENTAL, "Saude Mental", SEVERITY_SEVERE,
		80e9, 4e9, 76e9, 0.03, 20000000, 200000, "CAPS (centro de saude mental)", 380000,
		"Brasil tem 20 milhoes com transtorno mental. So 5% do orcamento necessario.",
		"Depressao nao tratada. Ansiedade cronica. Suicidios. Crack. Sem psicologo no SUS."},
	{IMPACT_HOUSING, "Moradia Digna", SEVERITY_CRITICAL,
		200e9, 15e9, 185e9, 0.10, 8000000, 80000, "casas populares", 2312500,
		"Deficit habitacional de 8 milhoes de familias.",
		"Familias em favelas, ruas, corticos. Criancas sem endereco fixo. Sem-teto morrendo de frio."},
	{IMPACT_FOOD_SECURITY, "Seguranca Alimentar (Fome)", SEVERITY_CRITICAL,
		120e9, 35e9, 85e9, 0.08, 33000000, 3, "refeicoes diarias", 28333333333,
		"33 milhoes de brasileiros passam fome. O pais da soja nao alimenta seu povo.",
		"Criancas desnutridas. Maes que pulam refeicoes. Idosos escolhendo entre comer e remedio."},
	{IMPACT_INFRASTRUCTURE, "Infraestrutura (Estradas, Energia)", SEVERITY_SEVERE,
		300e9, 60e9, 240e9, 0.12, 215000000, 20e6, "km de rodovia", 12000,
		"Estradas esburacadas. Pontes caindo. Sem investimento em energia.",
		"Acidentes fatais em estradas sem manutencao. Apagoes. Logistica cara = comida cara."},
	{IMPACT_SANITATION, "Saneamento Basico", SEVERITY_SEVERE,
		100e9, 12e9, 88e9, 0.05, 100000000, 12000, "ligacoes de agua/esgoto", 7333333,
		"Metade do Brasil nao tem esgoto tratado. Doencas por agua contaminada.",
		"Criancas com diarreia. Dengue. Leptospirose nas enchentes. Agua nao potavel."},
	{IMPACT_SCIENCE_TECH, "Ciencia e Tecnologia", SEVERITY_SEVERE,
		80e9, 8e9, 72e9, 0.04, 500000, 500000, "bolsas de pesquisa", 144000,
		"CNPq e Capes com orcamento destroicado. Cerebros fugindo do pais.",
		"Pesquisadores no radar de UBER. Doutores desempregados. Laboratorios fechados. Patentes perdidas."},
	{IMPACT_CULTURE_ARTS, "Cultura e Arte", SEVERITY_HIGH,
		30e9, 3e9, 27e9, 0.02, 10000000, 100000, "producoes culturais", 270000,
		"Cultura tratada como luxo. Artistas sem renda. Museus fechados.",
		"Teatros fechados. Cinema nacional morto. Musicos sem espaco. Identidade cultural apagada."},
	{IMPACT_INEQUALITY, "Desigualdade de Renda", SEVERITY_CRITICAL,
		500e9, 50e9, 450e9, 0.15, 150000000, 500, "transferencias de renda/mes", 900000000,
		"Brasil entre os 10 paises mais desiguais do mundo. Gini = 0.52.",
		"1% tem 50% da riqueza. Milhoes vivem com R$ 200/mes. Favelas ao lado de condominios."},
	{IMPACT_ENVIRONMENT, "Meio Ambiente", SEVERITY_SEVERE,
		50e9, 5e9, 45e9, 0.03, 215000000, 100000, "km2 protegidos/fiscalizados", 450000,
		"Desmatamento da Amazonia acelerando. IBAMA sem orcamento.",
		"Amazonia queimando. Agua acabando. Temperatura subindo. Futuro climatico destruido."},
	{IMPACT_SECURITY, "Seguranca Publica", SEVERITY_SEVERE,
		150e9, 70e9, 80e9, 0.05, 60000000, 2000000, "delegacias equipadas", 40000,
		"47 mil homicidios/ano. Mulheres mortas. LGBTQIA+ assassinados.",
		"Maes chorando filhos. Criancas sem pai. Medo de sair de casa. Violencia domestica."},
	{IMPACT_SPORT, "Esporte e Lazer", SEVERITY_MODERATE,
		20e9, 2e9, 18e9, 0.01, 40000000, 300000, "quadras esportivas", 60000,
		"Esporte como ferramenta de resgate social destruido.",
		"Criancas sem quadra. Jovens sem esporte = sem alternativa ao crime. Talentos perdidos."},
	{IMPACT_TRANSPORT, "Transporte Publico", SEVERITY_SEVERE,
		200e9, 30e9, 170e9, 0.08, 100000000, 100000000, "km de metro/onibus", 1700,
		"Metro sem expansao. Onibus lotados. Povo passa 3h/dia no transito.",
		"3 horas/dia no onibus lotado. Menos tempo com familia. Menos estudo. Mais estresse."},
	{IMPACT_CONNECTIVITY, "Internet e Conectividade", SEVERITY_HIGH,
		40e9, 5e9, 35e9, 0.02, 70000000, 5000, "conexoes de internet", 7000000,
		"70 milhoes sem internet de qualidade. Exclusao digital.",
		"Criancas estudando no celular 3G. Sem telemedicina. Sem servicos publicos digitais."},
	{IMPACT_CHILDHOOD, "Primeira Infancia (0-6 anos)", SEVERITY_CRITICAL,
		80e9, 8e9, 72e9, 0.04, 12000000, 1000000, "vagas em creches", 72000,
		"12 milhoes de criancas 0-6 sem creche. Desenvolvimento comprometido.",
		"Maes sem trabalhar porque nao tem creche. Criancas em casa sem estimulo. Futuro comprometido."},
}

// ============================================================================
// 3. SIMULACAO ANO A ANO (20 anos)
// ============================================================================

func (sim *ImpactSimulator) simulate() {
	debt := sim.initialDebt
	gdp := sim.initialGdp
	cumulativeGap := 0.0
	cumulativePeople := 0
	sim.simulations = make([]YearImpact, 0, sim.years+1)

	for i := 0; i <= sim.years; i++ {
		yearLabel := sim.startYear + i
		interest := debt * sim.interestRate
		totalGap := 0.0
		totalPeople := 0

		for j := range AREA_IMPACTS {
			ai := &AREA_IMPACTS[j]
			inflationFactor := math.Pow(1.05, float64(i))
			gap := ai.annualBudgetGapBrl * inflationFactor
			people := ai.peopleAffectedPerYear
			totalGap += gap
			totalPeople += people
		}

		cumulativeGap += totalGap
		cumulativePeople += totalPeople

		sim.simulations = append(sim.simulations, YearImpact{
			yearLabel:               yearLabel,
			interestPaidBrl:         interest,
			totalGapBrl:             totalGap,
			totalPeopleAffected:     totalPeople,
			cumulativeGapBrl:        cumulativeGap,
			cumulativePeopleAffected: cumulativePeople,
		})

		debt = debt + interest - (gdp * 0.18 * 0.3)
		gdp = gdp * (1 + sim.gdpGrowth)
	}
}

func (sim *ImpactSimulator) totalGapAllYears() float64 {
	return sim.simulations[len(sim.simulations)-1].cumulativeGapBrl
}

func (sim *ImpactSimulator) totalInterestAllYears() float64 {
	sum := 0.0
	for _, s := range sim.simulations {
		sum += s.interestPaidBrl
	}
	return sum
}

// ============================================================================
// 4. RENDERIZACOES VISUAIS - Portuguese comments
// ============================================================================

func renderAreaChart(sim *ImpactSimulator) {
	s := sim.simulations[0]
	fmt.Println("\n===========================================================================")
	fmt.Printf("  DEFICIT POR AREA -- %d (R$ bilhoes)\n", s.yearLabel)
	fmt.Println("===========================================================================\n")

	maxGap := 0.0
	for j := range AREA_IMPACTS {
		ai := &AREA_IMPACTS[j]
		inflationFactor := math.Pow(1.05, 0)
		gap := ai.annualBudgetGapBrl * inflationFactor
		if gap > maxGap {
			maxGap = gap
		}
	}

	for j := range AREA_IMPACTS {
		ai := &AREA_IMPACTS[j]
		inflationFactor := math.Pow(1.05, 0)
		gap := ai.annualBudgetGapBrl * inflationFactor
		gapBi := gap / 1e9
		barLen := int((gap / maxGap) * 40)
		if barLen < 1 {
			barLen = 1
		}
		bar := ""
		for k := 0; k < barLen; k++ {
			bar += "X"
		}
		sev := ""
		switch ai.severity {
		case SEVERITY_CRITICAL:
			sev = "CRIT"
		case SEVERITY_SEVERE:
			sev = "SEVE"
		case SEVERITY_HIGH:
			sev = "HIGH"
		case SEVERITY_MODERATE:
			sev = "MODE"
		default:
			sev = "LOW"
		}
		fmt.Printf("  %-35s R$%7.0fbi [%s] %s\n", ai.name, gapBi, bar, sev)
	}
	fmt.Println("\n  X = deficit orcamentario (dinheiro que FOI PRO JUROS)")
	fmt.Printf("  TOTAL DEFICIT/ANO: R$ %.0f bilhoes\n", s.totalGapBrl/1e9)
	fmt.Printf("  PESSOAS AFETADAS/ANO: %d\n\n", s.totalPeopleAffected)
}

func renderCumulativeChart(sim *ImpactSimulator) {
	fmt.Println("\n======================================================================")
	fmt.Println("  DEFICIT ACUMULADO POR ANO (R$ trilhoes)")
	fmt.Println("======================================================================\n")
	maxVal := sim.simulations[len(sim.simulations)-1].cumulativeGapBrl
	for _, s := range sim.simulations {
		valT := s.cumulativeGapBrl / 1e12
		barLen := int((s.cumulativeGapBrl / maxVal) * 50)
		if barLen < 1 {
			barLen = 1
		}
		bar := ""
		for k := 0; k < barLen; k++ {
			bar += "#"
		}
		fmt.Printf("  %d |%s| R$ %.1fT\n", s.yearLabel, bar, valT)
	}
	last := sim.simulations[len(sim.simulations)-1]
	fmt.Printf("\n  Em %d: R$ %.1f trilhoes ROUBADOS\n", last.yearLabel, last.cumulativeGapBrl/1e12)
	fmt.Println("  de educacao, saude, moradia, ciencia, cultura...\n")
}

func renderHumanCost() {
	fmt.Println("\n======================================================================")
	fmt.Println("  O CUSTO HUMANO -- O QUE A DIVIDA DESTRÓI")
	fmt.Println("======================================================================")
	for j := range AREA_IMPACTS {
		ai := &AREA_IMPACTS[j]
		sev := ""
		switch ai.severity {
		case SEVERITY_CRITICAL:
			sev = "CRITICO"
		case SEVERITY_SEVERE:
			sev = "SEVERO"
		case SEVERITY_HIGH:
			sev = "ALTO"
		case SEVERITY_MODERATE:
			sev = "MODERADO"
		default:
			sev = "BAIXO"
		}
		fmt.Printf("\n  %s [%s]\n", ai.name, sev)
		fmt.Printf("  Deficit: R$ %.0f bilhoes/ano\n", ai.annualBudgetGapBrl/1e9)
		fmt.Printf("  Pessoas afetadas: %d/ano\n", ai.peopleAffectedPerYear)
		fmt.Printf("  Nao entregue: %d %s/ano\n", ai.unitsNotDeliveredPerYear, ai.unitName)
		fmt.Printf("  CUSTO HUMANO: %s\n", ai.humanCost)
		fmt.Println("  ──────────────────────────────────────────────────────────────────")
	}
	fmt.Println()
}

func renderEquivalenceTable() {
	fmt.Println("\n======================================================================")
	fmt.Println("  O QUE R$ 100 BILHOES DE JUROS ROUBOU DO POVO")
	fmt.Println("  (equivalencia: se esse dinheiro ficasse no Brasil)")
	fmt.Println("======================================================================\n")
	fmt.Printf("  %-35s %15s\n", "RECURSO", "QTD")
	fmt.Println("  ----------------------------------------------------")

	labels := []string{
		"Escolas completas (R$ 5M)", "Hospitais (R$ 50M)", "Casas populares (R$ 80k)",
		"Creches (R$ 1M)", "CAPS saude mental (R$ 200k)", "Bolsas pesquisa (R$ 500k/ano)",
		"Quadras esportivas (R$ 300k)", "Delegacias equipadas (R$ 2M)", "km de rodovia (R$ 20M)",
		"km de metro/onibus (R$ 100M)", "Ligacoes de agua/esgoto (R$ 12k)", "Conexoes de internet (R$ 5k)",
		"Refeicoes (R$ 3)", "Producoes culturais (R$ 100k)", "Transferencias de renda/mes (R$ 500)",
		"Vagas em creches (R$ 1M)",
	}
	costs := []float64{5e6, 50e6, 8e4, 1e6, 2e5, 5e5, 3e5, 2e6, 2e7, 1e8, 12e3, 5e3, 3, 1e5, 500, 1e6}

	for i := range labels {
		qty := int64(100e9 / costs[i])
		var qtyStr string
		if qty >= 1000000000 {
			qtyStr = fmt.Sprintf("%.1f bilhoes", float64(qty)/1e9)
		} else if qty >= 1000000 {
			qtyStr = fmt.Sprintf("%.1f milhoes", float64(qty)/1e6)
		} else if qty >= 1000 {
			qtyStr = fmt.Sprintf("%d mil", qty/1000)
		} else {
			qtyStr = fmt.Sprintf("%d", qty)
		}
		fmt.Printf("  %-35s %15s\n", labels[i], qtyStr)
	}
	fmt.Println("\n  Cada R$ 100 bilhoes para o agiota e TUDO ISSO que nao existe.")
	fmt.Println("  O Brasil paga R$ 720 bilhoes/ano em juros.")
	fmt.Println("  Sao 7x essa tabela. TODO ANO.\n")
}

func renderComparisonOtherCountries() {
	fmt.Println("\n======================================================================")
	fmt.Println("  INVESTIMENTO PUBLICO POR HABITANTE/ANO")
	fmt.Println("  (Brasil vs paises que NAO tem divida extorsiva)")
	fmt.Println("======================================================================\n")
	fmt.Printf("  %-12s %15s  %30s\n", "PAIS", "R$/pessoa/ano", "BAR")
	fmt.Println("  ------------------------------------------------------------")

	countries := []string{"Noruega", "Dinamarca", "Suecia", "Alemanha", "Holanda", "Canada", "Brasil"}
	values := []int{25000, 22000, 20000, 18000, 17000, 16000, 3500}

	maxVal := 25000.0
	for i := range countries {
		barLen := int((float64(values[i]) / maxVal) * 30)
		if barLen < 1 {
			barLen = 1
		}
		bar := ""
		for k := 0; k < barLen; k++ {
			bar += "#"
		}
		marker := ""
		if countries[i] == "Brasil" {
			marker = " <<<"
		}
		fmt.Printf("  %-12s R$ %10d  [%s]%s\n", countries[i], values[i], bar, marker)
	}
	fmt.Println("\n  Brasil investe 7x MENOS por pessoa que paises ricos.")
	fmt.Println("  Nao e coincidencia. E a DIVIDA.")
	fmt.Println("  O dinheiro que iria pro povo vai pro AGIOTA.\n")
}

func renderNarrative(sim *ImpactSimulator) {
	s0 := sim.simulations[0]
	last := sim.simulations[len(sim.simulations)-1]
	fmt.Println("\n======================================================================")
	fmt.Println("NARRATIVA")
	fmt.Println("======================================================================")
	fmt.Print("Vou te mostrar o que a divida faz. Nao so matar. Mas DESTRUIR. ")
	fmt.Printf("Em %d, o Brasil pagou R$ %.0f bilhoes em juros. ", s0.yearLabel, s0.interestPaidBrl/1e9)
	fmt.Printf("Esse dinheiro deveria ter ido para %d areas da sua vida: ", len(AREA_IMPACTS))
	fmt.Print("Educacao: 50 milhoes de alunos em escolas destruidas. ")
	fmt.Print("Saude mental: 20 milhoes de brasileiros sem tratamento. ")
	fmt.Print("Moradia: 8 milhoes de familias sem casa digna. ")
	fmt.Print("Comida: 33 milhoes passando fome. ")
	fmt.Print("Saneamento: 100 milhoes sem esgoto. ")
	fmt.Print("Ciencia: pesquisadores no UBER. ")
	fmt.Print("Cultura: teatros fechados, artistas sem teto. ")
	fmt.Print("Esporte: criancas sem quadra. ")
	fmt.Print("Internet: 70 milhoes sem conexao. ")
	fmt.Print("Creches: 12 milhoes de criancas abandonadas. ")
	fmt.Printf("Em %d, o deficit acumulado sera de R$ %.0f trilhoes. ", last.yearLabel, last.cumulativeGapBrl/1e12)
	fmt.Print("Dinheiro que foi ROUBADO de cada area que faz a vida valer a pena. ")
	fmt.Print("A divida nao so mata. Ela CASTRA. Castra a educacao. Castra a ciencia. Castra a moradia. Castra o futuro. ")
	fmt.Print("Cada real pro agiota e um real roubado do seu filho. Da sua escola. Do seu hospital. Da sua casa. ")
	fmt.Print("Da sua cultura. Do seu esporte. Da sua internet. ")
	fmt.Println("A divida MATA. E o que ela nao mata, ela DESTRÓI.\n")
}

// ============================================================================
// 5. DEMONSTRACAO (main)
// ============================================================================

func main() {
	fmt.Println("======================================================================")
	fmt.Println("OpenDebtImpact -- Todos os Impactos da Divida")
	fmt.Println("======================================================================")

	sim := ImpactSimulator{
		startYear:   2024,
		years:       20,
		initialDebt: 6.0e12,
		initialGdp:  10.0e12,
		interestRate: 0.12,
		gdpGrowth:   0.025,
	}
	sim.simulate()

	crit, sev := 0, 0
	for j := range AREA_IMPACTS {
		if AREA_IMPACTS[j].severity == SEVERITY_CRITICAL {
			crit++
		}
		if AREA_IMPACTS[j].severity == SEVERITY_SEVERE {
			sev++
		}
	}
	fmt.Printf("\nAreas impactadas: %d\n", len(AREA_IMPACTS))
	fmt.Printf("Severidade critica: %d\n", crit)
	fmt.Printf("Severidade severa: %d\n", sev)

	renderAreaChart(&sim)
	renderHumanCost()
	renderEquivalenceTable()
	renderComparisonOtherCountries()
	renderCumulativeChart(&sim)
	renderNarrative(&sim)

	totalGapT := sim.totalGapAllYears() / 1e12
	totalIntT := sim.totalInterestAllYears() / 1e12
	fmt.Println("======================================================================")
	fmt.Println("RESUMO")
	fmt.Println("======================================================================")
	fmt.Printf("  Areas impactadas: %d\n", len(AREA_IMPACTS))
	fmt.Printf("  Pessoas afetadas/ano: %d\n", sim.simulations[0].totalPeopleAffected)
	fmt.Printf("  Deficit total em %d anos: R$ %.1f trilhoes\n", sim.years, totalGapT)
	fmt.Printf("  Juros pagos no periodo: R$ %.1f trilhoes\n", totalIntT)
	fmt.Printf("  Deficit medio/ano: R$ %.1f trilhoes\n", totalGapT/float64(sim.years))

	fmt.Println("\n======================================================================")
	fmt.Println("VEREDICTO")
	fmt.Println("======================================================================\n")
	fmt.Println("  A divida MATA (OpenDebtMortality).")
	fmt.Println("  E o que ela nao mata, ela DESTRÓI (este modulo).\n")
	fmt.Printf("  Em %d anos:\n", sim.years)
	fmt.Printf("  R$ %.0f trilhoes ROUBADOS\n", totalGapT)
	fmt.Println("  de educacao, saude, moradia, ciencia, cultura, esporte,")
	fmt.Println("  meio ambiente, seguranca, transporte, conectividade, infancia.\n")
	fmt.Printf("  %d areas destruidas.\n", len(AREA_IMPACTS))
	fmt.Printf("  %.0f milhoes de pessoas/ano afetadas.\n\n", float64(sim.simulations[0].totalPeopleAffected)/1e6)
	fmt.Println("  Cada parcela da divida e uma escola que nao existe.")
	fmt.Println("  Cada juros pago e uma creche que nao foi construida.")
	fmt.Println("  Cada bilhao pro agiota e mil futuros cancelados.\n")
	fmt.Println("  A divida MATA. E DESTRÓI. E CASTRA.")
	fmt.Println("  Nao renegociar. Nao alongar. EXTINGUIR.\n")
	fmt.Println("  'Nao existe pobreza, existe MISERIA.'")
	fmt.Println("  A divida e a maquina que PRODUZ a miseria.")
}
