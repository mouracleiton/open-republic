// OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?
// ==========================================================
// "Cada R$ 1 bilhao pago em juros e:
// - 2 hospitais que nao foram construidos
// - 50 mil casas populares que nao foram entregues
// - 200 mil cestas de comida que nao foram distribuidas
// - 10 mil bolsas universitarias que nao foram concedidas
//
// E esses hospitais, casas, comidas e bolsas que NAO EXISTEM
// porque o dinheiro foi pro agiota -- essas sao as PESSOAS que morrem.
//
// O juros da divida MATA. MATA de forma invisivel.
// Nao e uma bala. E a AUSENCIA de um medico.
// Nao e uma faca. E a AUSENCIA de comida na mesa.
// Nao e um tiro. E a AUSENCIA de saneamento basico.
//
// Este modulo calcula, ano a ano, quantas pessoas MORREM
// no Brasil porque o dinheiro que deveria salvar suas vidas
// foi enviado para o agiota international como 'juros da divida'.
//
// METODOLOGIA:
// - Calcular juros pagos por ano (R$ bilhoes)
// - Calcular quanto disso deveria ir para saude, comida, saneamento
// - Calcular mortes evitaveis por falta de cada recurso
// - Comparar: se nao pagasse a divida, quantas vidas seriam salvas?
//
// AS MORTES NAO SAO ABSTRATAS. SAO NOMES. SAO CRIANCAS.
// Sao os 124 mil brasileiros que morrem por ano por causas evitaveis
// no SUS subfinanciado. Sao as criancas desnutridas no Nordeste.
// Sao os idosos sem atendimento na fila do SUS.
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// ============================================================================

package main

import (
	"fmt"
	"math"
)

// ============================================================================
// 1. CAUSAS DE MORTE EVITAVEIS (vinculadas a subfinanciamento)
// ============================================================================

type PreventableDeathCategory int

const (
	HEALTHCARE_SHORTAGE PreventableDeathCategory = iota // morreu na fila do SUS
	CHILD_MORTALITY                                     // bebe nao sobreviveu
	MATERNAL_DEATH                                      // mae morreu no parto
	MALNUTRITION                                        // morreu de fome
	PREVENTABLE_DISEASE                                 // vacina/exame nao chegou
	VIOLENCE                                            // sem programa social
	SUICIDE                                             // sem saude mental
	SANITATION                                          // agua contaminada
	ROAD_DEATH                                          // estrada sem manutencao
	HEAT_COLD                                           // sem teto/climatizacao
	DRUG_OVERDOSE                                       // sem tratamento
	CANCER_UNTREATED                                    // fila de quimio
	HEART_UNTREATED                                     // sem UTI
	NEONATAL                                            // sem UTI neonatal
)

var PreventableDeathCategoryNames = []string{
	"falta_sus",
	"mortalidade_infantil",
	"morte_materna",
	"desnutricao",
	"doenca_evitavel",
	"violencia",
	"suicidio",
	"saneamento",
	"transito",
	"calor_frio",
	"overdose",
	"cancer_sem_tratamento",
	"coracao_sem_atendimento",
	"neonatal",
}

type DeathCost struct {
	Category                  PreventableDeathCategory
	Name                      string
	CostToSaveOneLifeBRL      float64
	DeathsPerYearBrazil       int
	PctLinkedToUnderfunding   float64
	Description               string
}

func (dc DeathCost) DeathsPreventable() int {
	return int(float64(dc.DeathsPerYearBrazil) * dc.PctLinkedToUnderfunding)
}

func (dc DeathCost) LivesSavedPerBillion() float64 {
	if dc.CostToSaveOneLifeBRL <= 0 {
		return 0
	}
	return 1e9 / dc.CostToSaveOneLifeBRL
}

// ============================================================================
// 2. TABELA DE MORTALIDADE (Dados baseados em OMS/IBGE/Datasus)
// ============================================================================

var DEATH_COSTS = []DeathCost{
	{HEALTHCARE_SHORTAGE, "Morte na fila do SUS", 500000, 124000, 0.60, "Pessoas que morrem esperando cirurgia, exame, consulta, UTI."},
	{CHILD_MORTALITY, "Mortalidade infantil (0-5 anos)", 80000, 40000, 0.70, "Criancas que morrem antes dos 5 anos por falta de atendimento."},
	{MATERNAL_DEATH, "Morte materna (no parto)", 50000, 1800, 0.80, "Maes que morrem no parto por falta de estrutura hospitalar."},
	{MALNUTRITION, "Desnutricao", 15000, 5000, 0.90, "Pessoas que morrem de fome ou desnutricao grave no Brasil."},
	{PREVENTABLE_DISEASE, "Doencas evitaveis (vacina/exame)", 20000, 50000, 0.65, "Mortes por doencas que vacina ou exame precoce previniria."},
	{VIOLENCE, "Violencia / Homicidio", 300000, 47000, 0.40, "Jovens mortos por violencia. Programa social reduz 40%."},
	{SUICIDE, "Suicidio (sem saude mental)", 100000, 14000, 0.55, "Pessoas que se matam por falta de atendimento psicologico."},
	{SANITATION, "Doenças por falta de saneamento", 40000, 8000, 0.85, "Mortes por diarreia, leptospirose, hepatite por agua suja."},
	{ROAD_DEATH, "Morte no transito", 2000000, 30000, 0.35, "Acidentes em estradas sem manutencao ou sinalizacao."},
	{CANCER_UNTREATED, "Cancer sem tratamento a tempo", 800000, 35000, 0.50, "Pessoas que morrem esperando tratamento de cancer no SUS."},
	{HEART_UNTREATED, "Infarto sem atendimento", 600000, 100000, 0.30, "Infartos que UTI/SAMU salvaria se chegasse a tempo."},
	{NEONATAL, "Morte neonatal", 120000, 19000, 0.65, "Bebe que morre nos primeiros 28 dias por falta de UTI neonatal."},
}

const DEATH_COSTS_COUNT = 12

// ============================================================================
// 3. SIMULACAO ANO A ANO
// ============================================================================

type YearMortality struct {
	YearLabel                int
	InterestPaidBRL          float64
	GDPBRL                   float64
	TotalPreventableDeaths   int
	DeathsLinkedToDebt       int
	PotentialLivesSaved      int
	HospitalsNotBuilt        int
	PeopleWithoutDoctor      int
	ChildrenNotVaccinated    int
	HousesNotBuilt           int
	MealsNotServed           int
	CumulativeDeathsByDebt   int
}

type DebtMortalitySimulator struct {
	StartYear             int
	Years                 int
	InitialDebt           float64
	InitialGDP            float64
	InterestRate          float64
	GDPGrowth             float64
	Population            float64
	FractionToHealth      float64
	FractionToFood        float64
	FractionToHousing     float64
	FractionToEducation   float64
	FractionToInfra       float64
	Simulations           []YearMortality
}

func NewDebtMortalitySimulator(startYear, years int) *DebtMortalitySimulator {
	return &DebtMortalitySimulator{
		StartYear:           startYear,
		Years:               years,
		InitialDebt:         6.0e12,
		InitialGDP:          10.0e12,
		InterestRate:        0.12,
		GDPGrowth:           0.025,
		Population:          215e6,
		FractionToHealth:    0.40,
		FractionToFood:      0.15,
		FractionToHousing:   0.15,
		FractionToEducation: 0.15,
		FractionToInfra:     0.15,
		Simulations:         nil,
	}
}

func (sim *DebtMortalitySimulator) Simulate() []YearMortality {
	sim.Simulations = make([]YearMortality, sim.Years+1)
	debt := sim.InitialDebt
	gdp := sim.InitialGDP
	cumulativeDeaths := 0

	for i := 0; i <= sim.Years; i++ {
		yearLabel := sim.StartYear + i
		interest := debt * sim.InterestRate
		moneyForHealth := interest * sim.FractionToHealth
		moneyForFood := interest * sim.FractionToFood

		potentialSaved := 0
		for j := 0; j < DEATH_COSTS_COUNT; j++ {
			livesSaved := moneyForHealth * 0.3 / DEATH_COSTS[j].CostToSaveOneLifeBRL
			potentialSaved += int(livesSaved)
		}

		totalPreventable := 0
		for j := 0; j < DEATH_COSTS_COUNT; j++ {
			totalPreventable += DEATH_COSTS[j].DeathsPreventable()
		}

		deathsByDebt := int(math.Min(float64(potentialSaved), float64(totalPreventable)))

		hospitalsNotBuilt := int(moneyForHealth / 50e6)
		peopleWithoutDoctor := int(moneyForHealth / 3000)
		childrenNotVaccinated := int(moneyForHealth / 50)
		housesNotBuilt := int((interest * sim.FractionToHousing) / 80000)
		mealsNotServed := int(moneyForFood / 3)

		cumulativeDeaths += deathsByDebt

		sim.Simulations[i] = YearMortality{
			YearLabel:              yearLabel,
			InterestPaidBRL:        interest,
			GDPBRL:                 gdp,
			TotalPreventableDeaths: totalPreventable,
			DeathsLinkedToDebt:     deathsByDebt,
			PotentialLivesSaved:    potentialSaved,
			HospitalsNotBuilt:      hospitalsNotBuilt,
			PeopleWithoutDoctor:    peopleWithoutDoctor,
			ChildrenNotVaccinated:  childrenNotVaccinated,
			HousesNotBuilt:         housesNotBuilt,
			MealsNotServed:         mealsNotServed,
			CumulativeDeathsByDebt: cumulativeDeaths,
		}

		debt = debt + interest - (gdp * 0.18 * 0.3)
		gdp = gdp * (1 + sim.GDPGrowth)
	}
	return sim.Simulations
}

func (sim *DebtMortalitySimulator) TotalDeathsByDebt() int {
	if len(sim.Simulations) == 0 {
		return 0
	}
	return sim.Simulations[len(sim.Simulations)-1].CumulativeDeathsByDebt
}

func (sim *DebtMortalitySimulator) TotalInterestPaid() float64 {
	total := 0.0
	for _, s := range sim.Simulations {
		total += s.InterestPaidBRL
	}
	return total
}

func (sim *DebtMortalitySimulator) DeathPerTrillionInterest() float64 {
	totalInt := sim.TotalInterestPaid()
	if totalInt == 0 {
		return 0
	}
	return float64(sim.TotalDeathsByDebt()) / (totalInt / 1e12)
}

func (sim *DebtMortalitySimulator) Summary() map[string]interface{} {
	last := YearMortality{}
	if len(sim.Simulations) > 0 {
		last = sim.Simulations[len(sim.Simulations)-1]
	}
	return map[string]interface{}{
		"years_simulated":                   sim.Years,
		"total_deaths_by_debt":              sim.TotalDeathsByDebt(),
		"total_interest_paid_trillions":     sim.TotalInterestPaid() / 1e12,
		"deaths_per_trillion_interest":      sim.DeathPerTrillionInterest(),
		"avg_deaths_per_year":               float64(sim.TotalDeathsByDebt()) / float64(sim.Years),
		"final_year_hospitals_not_built":    last.HospitalsNotBuilt,
		"final_year_meals_not_served":       last.MealsNotServed,
		"final_year_children_not_vaccinated": last.ChildrenNotVaccinated,
	}
}

// ============================================================================
// 4. QUEM O BRASIL PAGA (paises credores)
// ============================================================================

type CountryCreditor struct {
	Country            string
	AmountReceivedBRL  float64
	Flag               string
	Description        string
}

var COUNTRY_CREDITORS = []CountryCreditor{
	{"Estados Unidos", 180e9, "EUA", "Fundos de investimento e bancos americanos recebem bilhoes em juros."},
	{"Reino Unido", 80e9, "UK", "Londres e centro de vulture funds que lucram com divida alheia."},
	{"Alemanha", 50e9, "DE", "Bancos alemaes detem titulos brasileiros."},
	{"Japao", 40e9, "JP", "Fundos japoneses investem em divida soberana."},
	{"Franca", 35e9, "FR", "Bancos franceses (BNP, SocGen) detem titulos."},
	{"Suica", 30e9, "CH", "Centro de banca privada que lucra com juros."},
	{"China", 25e9, "CN", "Bancos chineses compraram titulos brasileiros."},
	{"Holanda", 20e9, "NL", "Centro financeiro (Amsterda) roteia investimentos."},
	{"Luxemburgo", 15e9, "LU", "Paraiso fiscal que abriga fundos especulativos."},
	{"Outros", 25e9, "??", "Outros paises e fundos internacionais."},
}

const COUNTRY_CREDITORS_COUNT = 10

// ============================================================================
// 5. RENDERIZACOES VISUAIS
// ============================================================================

func renderDeathChart(simulations []YearMortality) string {
	var lines []string
	lines = append(lines, "")
	lines = append(lines, "======================================================================")
	lines = append(lines, "  MORTES POR ANO CAUSADAS PELA DIVIDA")
	lines = append(lines, "  (pessoas que morreriam VIVAS se o juros fosse investido em saude)")
	lines = append(lines, "======================================================================")
	lines = append(lines, "")

	maxDeaths := 1
	for _, s := range simulations {
		if s.DeathsLinkedToDebt > maxDeaths {
			maxDeaths = s.DeathsLinkedToDebt
		}
	}
	if maxDeaths == 0 {
		maxDeaths = 1
	}

	for _, s := range simulations {
		barLen := int((float64(s.DeathsLinkedToDebt) / float64(maxDeaths)) * 50)
		if barLen < 1 {
			barLen = 1
		}
		bar := ""
		for i := 0; i < barLen; i++ {
			bar += "#"
		}
		for len(bar) < 50 {
			bar += " "
		}
		lines = append(lines, fmt.Sprintf("  %d |%s| %8d mortes", s.YearLabel, bar, s.DeathsLinkedToDebt))
	}

	lines = append(lines, "")
	lines = append(lines, fmt.Sprintf("  Cada # representa ~%d mortes", maxDeaths/50))
	lines = append(lines, fmt.Sprintf("  TOTAL ACUMULADO: %d mortes", simulations[len(simulations)-1].CumulativeDeathsByDebt))
	lines = append(lines, fmt.Sprintf("  em %d anos", len(simulations)-1))
	lines = append(lines, "")
	return joinLines(lines)
}

func renderCountryDeaths() string {
	var lines []string
	lines = append(lines, "")
	lines = append(lines, "======================================================================")
	lines = append(lines, "  PARA QUEM O BRASIL PAGA -- E QUANTOS MORREM POR ISSO")
	lines = append(lines, "======================================================================")
	lines = append(lines, "")

	totalReceived := 0.0
	for _, c := range COUNTRY_CREDITORS {
		totalReceived += c.AmountReceivedBRL
	}

	for _, c := range COUNTRY_CREDITORS {
		pct := (c.AmountReceivedBRL / totalReceived) * 100
		deathsCaused := int(c.AmountReceivedBRL / 500000)
		barLen := int(pct)
		bar := ""
		for i := 0; i < barLen && i < 20; i++ {
			bar += "$"
		}
		for len(bar) < 20 {
			bar += " "
		}
		lines = append(lines, fmt.Sprintf("  %-15s R$ %6.0f bi/ano [%s] %5.1f%%  ~%d mortes",
			c.Country, c.AmountReceivedBRL/1e9, bar, pct, deathsCaused))
	}

	lines = append(lines, "")
	lines = append(lines, fmt.Sprintf("  TOTAL ENVIADO AO EXTERIOR: R$ %.0f bilhoes/ano", totalReceived/1e9))
	lines = append(lines, fmt.Sprintf("  MORTES CAUSADAS: ~%d por ano", int(totalReceived/500000)))
	lines = append(lines, fmt.Sprintf("  Cada $ = R$ %.0f bilhoes que sai do Brasil", totalReceived/20/1e9))
	lines = append(lines, "")
	lines = append(lines, "  Cada real enviado ao agiota international e uma vida")
	lines = append(lines, "  que NAO foi salva no Brasil.")
	lines = append(lines, "")
	return joinLines(lines)
}

func renderCategoryBreakdown() string {
	var lines []string
	lines = append(lines, "")
	lines = append(lines, "======================================================================")
	lines = append(lines, "  MORTES EVITAVEIS NO BRASIL (por categoria, por ano)")
	lines = append(lines, "======================================================================")
	lines = append(lines, "")

	totalPreventable := 0
	for _, dc := range DEATH_COSTS {
		totalPreventable += dc.DeathsPreventable()
	}

	lines = append(lines, fmt.Sprintf("%-40s %12s %15s %12s", "CATEGORIA", "MORTES/ANO", "CUSTO/VIDA", "EVITAVEIS"))
	lines = append(lines, "--------------------------------------------------------------------------------")

	for _, dc := range DEATH_COSTS {
		lines = append(lines, fmt.Sprintf("  %-38s %10d R$ %12.0f %10d",
			dc.Name, dc.DeathsPerYearBrazil, dc.CostToSaveOneLifeBRL, dc.DeathsPreventable()))
	}

	lines = append(lines, "--------------------------------------------------------------------------------")
	totalDeaths := 0
	for _, dc := range DEATH_COSTS {
		totalDeaths += dc.DeathsPerYearBrazil
	}
	lines = append(lines, fmt.Sprintf("  %-38s %10d %15s %10d", "TOTAL", totalDeaths, "", totalPreventable))

	lines = append(lines, "")
	lines = append(lines, fmt.Sprintf("  Total de mortes evitaveis/ano: %d", totalPreventable))
	lines = append(lines, fmt.Sprintf("  Isso e %.0f mortes POR DIA.", totalPreventable/365.0))
	lines = append(lines, fmt.Sprintf("  %.0f mortes POR HORA.", totalPreventable/365.0/24))
	lines = append(lines, fmt.Sprintf("  %.1f mortes POR MINUTO.", totalPreventable/365.0/24/60))
	lines = append(lines, "")
	lines = append(lines, "  UMA PESSOA MORRE NO BRASIL A CADA MINUTO")
	lines = append(lines, "  POR ALGO QUE DINHEIRO RESOLVERIA.")
	lines = append(lines, "")
	lines = append(lines, "  E o dinheiro? FOI PRA O AGIOTA.")
	lines = append(lines, "")
	return joinLines(lines)
}

func renderLostInfrastructure(simulations []YearMortality) string {
	s := simulations[0]
	var lines []string
	lines = append(lines, "")
	lines = append(lines, "======================================================================")
	lines = append(lines, fmt.Sprintf("  O QUE O BRASIL NAO CONSTRUIU EM UM ANO"))
	lines = append(lines, fmt.Sprintf("  (%d -- R$ %.0f bi em juros)", s.YearLabel, s.InterestPaidBRL/1e9))
	lines = append(lines, "======================================================================")
	lines = append(lines, "")

	lines = append(lines, fmt.Sprintf("  Hospitais nao construidos:        %8d", s.HospitalsNotBuilt))
	lines = append(lines, fmt.Sprintf("  Casas populares nao entregues:    %8d", s.HousesNotBuilt))
	lines = append(lines, fmt.Sprintf("  Pessoas sem medico de familia:    %8d", s.PeopleWithoutDoctor))
	lines = append(lines, fmt.Sprintf("  Criancas nao vacinadas:            %8d", s.ChildrenNotVaccinated))
	lines = append(lines, fmt.Sprintf("  Refeicoes nao servidas:            %8d", s.MealsNotServed))
	lines = append(lines, "")

	lines = append(lines, "  Em UM ano, o juros da divida pagou:")
	lines = append(lines, fmt.Sprintf("  - %d hospitais QUE NAO EXISTEM", s.HospitalsNotBuilt))
	lines = append(lines, fmt.Sprintf("  - %d casas QUE NAO FORAM ENTREGUES", s.HousesNotBuilt))
	lines = append(lines, fmt.Sprintf("  - %d refeicoes QUE NAO FORAM SERVIDAS", s.MealsNotServed))
	lines = append(lines, "")

	lines = append(lines, "  Cada hospital que nao existe = pessoas que morrem na fila.")
	lines = append(lines, "  Cada casa que nao foi entregue = familias na rua.")
	lines = append(lines, "  Cada refeicao que nao foi servida = criancas desnutridas.")
	lines = append(lines, "")
	return joinLines(lines)
}

func renderTimelineHuman(simulations []YearMortality) string {
	var lines []string
	lines = append(lines, "")
	lines = append(lines, "======================================================================")
	lines = append(lines, "  LINHA DO TEMPO DA MORTE")
	lines = append(lines, "======================================================================")
	lines = append(lines, "")

	for _, s := range simulations {
		deathsPerDay := float64(s.DeathsLinkedToDebt) / 365.0
		lines = append(lines, fmt.Sprintf("  %d:", s.YearLabel))
		lines = append(lines, fmt.Sprintf("    Juros pago: R$ %.0f bilhoes", s.InterestPaidBRL/1e9))
		lines = append(lines, fmt.Sprintf("    Mortes causadas pela divida: %d", s.DeathsLinkedToDebt))
		lines = append(lines, fmt.Sprintf("    Isso sao %.0f mortes POR DIA", deathsPerDay))
		lines = append(lines, fmt.Sprintf("    Acumulado desde %d: %d", simulations[0].YearLabel, s.CumulativeDeathsByDebt))
		lines = append(lines, "")
	}

	lines = append(lines, fmt.Sprintf("  Em %d anos, a divida causou a morte de:", len(simulations)-1))
	lines = append(lines, fmt.Sprintf("  %d PESSOAS.", simulations[len(simulations)-1].CumulativeDeathsByDebt))
	lines = append(lines, "")
	lines = append(lines, "  Isso e mais que a populacao de muitas cidades brasileiras.")
	lines = append(lines, "  Mais que todas as guerras do Brasil juntas.")
	lines = append(lines, "  Mais que todas as epidemias da historia recente.")
	lines = append(lines, "")
	lines = append(lines, "  E nao foi uma bala. Foi um BOLETO.")
	lines = append(lines, "")
	return joinLines(lines)
}

func renderNarrative(simulations []YearMortality) string {
	s0 := simulations[0]
	last := simulations[len(simulations)-1]
	total := last.CumulativeDeathsByDebt

	parts := []string{
		"Vou te dizer algo que ninguem te conta.",
		fmt.Sprintf("No ano %d, o Brasil pagou R$ %.0f bilhoes apenas em JUROS da divida publica.", s0.YearLabel, s0.InterestPaidBRL/1e9),
		"Esse dinheiro foi para bancos, fundos, paises estrangeiros. Nao foi para o SUS. Nao foi para a escola. Nao foi para a comida.",
		fmt.Sprintf("No mesmo ano, %d brasileiros morreram por causas evitaveis. Filas do SUS. Desnutricao. Falta de medico.", s0.DeathsLinkedToDebt),
		fmt.Sprintf("Se o dinheiro dos juros tivesse ido para a saude, %d dessas pessoas poderiam estar VIVAS.", s0.PotentialLivesSaved),
		fmt.Sprintf("Em %d anos, se nada mudar, a divida tera causado a morte de %d pessoas.", len(simulations)-1, total),
		fmt.Sprintf("Sao %.0f mortes por dia. A cada minuto, alguem morre porque o dinheiro que salvaria sua vida foi para o agiota.", total/365.0),
		"A divida nao e um numero. E um CEMITERIO. Cada parcela paga e uma cova que nao foi aberta. Cada juros pago e uma vida que nao foi salva. A divida MATA.",
	}
	return joinParts(parts)
}

// ============================================================================
// 6. DEMONSTRACAO (main)
// ============================================================================

func main() {
	fmt.Println("======================================================================")
	fmt.Println("OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?")
	fmt.Println("======================================================================")

	sim := NewDebtMortalitySimulator(2024, 20)
	simulations := sim.Simulate()

	fmt.Print(renderCategoryBreakdown())
	fmt.Print(renderCountryDeaths())
	fmt.Print(renderLostInfrastructure(simulations))
	fmt.Print(renderDeathChart(simulations))
	fmt.Print(renderTimelineHuman(simulations))

	fmt.Println("\n======================================================================")
	fmt.Println("NARRATIVA (para Telefonista ler)")
	fmt.Println("======================================================================")
	fmt.Println(renderNarrative(simulations))

	summary := sim.Summary()
	fmt.Println("\n======================================================================")
	fmt.Println("RESUMO")
	fmt.Println("======================================================================")
	fmt.Printf("  Anos simulados: %v\n", summary["years_simulated"])
	fmt.Printf("  Total de mortes pela divida: %d\n", summary["total_deaths_by_debt"])
	fmt.Printf("  Total de juros pagos: R$ %.1f trilhoes\n", summary["total_interest_paid_trillions"])
	fmt.Printf("  Mortes por R$ 1 trilhao de juros: %.0f\n", summary["deaths_per_trillion_interest"])
	fmt.Printf("  Media de mortes/ano: %.0f\n", summary["avg_deaths_per_year"])

	fmt.Println("\n======================================================================")
	fmt.Println("VEREDICTO")
	fmt.Println("======================================================================")
	fmt.Println()
	fmt.Println("  A divida publica nao e apenas impossivel de pagar.")
	fmt.Println("  Ela e um ASSASSINO DE MASSA silencioso.")
	fmt.Println()
	fmt.Printf("  Em %v anos:\n", summary["years_simulated"])
	fmt.Printf("  %d brasileiros morreram\n", summary["total_deaths_by_debt"])
	fmt.Printf("  porque R$ %.1f trilhoes\n", summary["total_interest_paid_trillions"])
	fmt.Println("  foram enviados ao agiota em vez de ir para saude, comida, vida.")
	fmt.Println()
	fmt.Println("  A divida MATA.")
	fmt.Println("  Cada juros pago e uma vida nao salva.")
	fmt.Println("  Nao renegociar. Nao alongar.")
	fmt.Println("  EXTINGUIR.")
	fmt.Println("  Pelas vidas que ainda podem ser salvas.")
	fmt.Println()
	fmt.Println("  'Nao existe pobreza, existe MISERIA.'")
	fmt.Println("  A divida e a maquina que PRODUZ a miseria.")
}

func joinLines(lines []string) string {
	result := ""
	for i, line := range lines {
		if i > 0 {
			result += "\n"
		}
		result += line
	}
	return result
}

func joinParts(parts []string) string {
	result := ""
	for i, part := range parts {
		if i > 0 {
			result += " "
		}
		result += part
	}
	return result
}
