// OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota
// ===================================================================
// "O agiota diz: 'Se nao pagar, acabo com voce.'
// O pais ouve e paga. E paga. E paga. E nunca quita.
// Mas o que ACONTECE se parar de pagar? De verdade?
// O agiota grita. O mercado assusta. A midia apavora.
// E depois? O sol nasce. O pais existe. O povo continua.
// E o dinheiro que ia pro agiota vai pro povo."
//
// Este modulo simola ano a ano o que acontece quando um pais
// DECIDE PARAR DE PAGAR a divida. Mostra:
//
// 1. O ANO ZERO: o pais anuncia que nao vai pagar
// 2. O CHOQUE: panico, midia, agiotas gritando
// 3. A QUEDA: desvalorizacao, inflacao, recessao
// 4. A RECUPERACAO: sem juros, dinheiro sobra
// 5. A EXPLOSAO: investimento em povo, PIB dispara
// 6. O RESULTADO: pais rico vs pais escravo da divida
//
// O AGIOTA quem e:
// - Fundos de investimento (que compraram titulos por 30 centavos)
// - Bancos internacionais (que emprestaram criando dinheiro do nada)
// - FMI (que empresta para continuar pagando -- pau de se batr ate morrer)
// - Especuladores (que apostam NO nao-pagamento)
// - Bancada do capital financeiro (politicos a servico do agiota)
//
// O AGIOTA NAO E:
// - O povo brasileiro (que sofre pagando)
// - O trabalhador (que nao ve o dinheiro)
// - O idoso (cuidando das proprias contas)
// - A empresa produtiva (que paga imposto)
//
// CENARIO COMPARATIVO:
// - Caminho A: Continua pagando (OpenDebtAbolition prova que nunca acaba)
// - Caminho B: PARA de pagar (este modulo simula as consequencias)
//
// PRINCIPIO: O agiota so tem poder se voce tiver medo.
// O medo e a arma. A verdade e o antídoto.
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

package main

import (
	"fmt"
	"math"
)

// ============================================================================
// 1. OS AGIOTAS (Quem e o credor)
// ============================================================================

type CreditorType int

const (
	NATIONAL_BONDS CreditorType = iota
	FOREIGN_BANKS
	IMF
	FOREIGN_BONDS
	PENSION_FUNDS
	SOVEREIGN_FUNDS
	SPECULATORS
	LOCAL_BANKS
	SUPREME_COURT
)

func (ct CreditorType) String() string {
	switch ct {
	case NATIONAL_BONDS:
		return "titulos_publicos"
	case FOREIGN_BANKS:
		return "bancos_estrageiros"
	case IMF:
		return "fmi"
	case FOREIGN_BONDS:
		return "titulos_externos"
	case PENSION_FUNDS:
		return "fundos_pensao"
	case SOVEREIGN_FUNDS:
		return "fundos_soberanos"
	case SPECULATORS:
		return "especuladores"
	case LOCAL_BANKS:
		return "bancos_locais"
	case SUPREME_COURT:
		return "stf_judicial"
	default:
		return "unknown"
	}
}

type Creditor struct {
	creditor_id       string
	name              string
	creditor_type     CreditorType
	amount_owed_brl   float64
	owns_pct_of_total float64
	origin_country    string
	purchase_price_pct float64
	real_risk         string
	bluffs            []string
	real_consequence  string
	can_punish        bool
}

// ============================================================================
// 2. CATALOGO DE AGIOTAS (Quem sao, o que dizem, o que acontece)
// ============================================================================

var CREDITORS = []Creditor{
	{
		creditor_id: "CR-001", name: "Mercado de Titulos Internos (Tesouro Direto)",
		creditor_type: NATIONAL_BONDS, amount_owed_brl: 4.2e12, owns_pct_of_total: 70.0,
		purchase_price_pct: 0.95, origin_country: "Brasil",
		bluffs: []string{"Vai faltar dinheiro para tudo!", "O sistema financeiro vai colapsar!", "Ninguem vai mais emprestar pro Brasil!"},
		real_consequence: "Titulos sao renegociados. Investidores institucionais absorvem perda. O contribuinte brasileiro que injetou o dinheiro para pagar juros absurdos nao e responsavel por bancar especulador.",
		can_punish: false,
	},
	{
		creditor_id: "CR-002", name: "Fundos Especulativos (Vulture Funds)",
		creditor_type: SPECULATORS, amount_owed_brl: 300e9, owns_pct_of_total: 5.0,
		purchase_price_pct: 0.25, origin_country: "EUA/Reino Unido",
		bluffs: []string{"Vamos bloquear seus ativos no exterior!", "Vamos processar na justica internacional!", "Vamos confiscares as reservas!", "Nenhum pais vai negociar com voce!"},
		real_consequence: "Compraram a divida por 25 centavos de dolar. Querem 100 centavos. O Brasil pode pagar 25 centavos e fechar. Vulture funds sao parasitas. O mercado ja precifica default.",
		can_punish: false,
	},
	{
		creditor_id: "CR-003", name: "FMI (Fundo Monetario Internacional)",
		creditor_type: IMF, amount_owed_brl: 0, owns_pct_of_total: 0.0,
		purchase_price_pct: 1.0, origin_country: "Internacional",
		bluffs: []string{"Vamos impor austeridade!", "Vamos bloquear credito internacional!", "Vamos ditar sua politica economica!"},
		real_consequence: "FMI nao e deus. E um banco politico. Argentina deu calote em 2001 e 2014. Ainda existe. Grecia renegociou em 2012. Ainda existe. Islandia deu calote em 2008. Hoje e modelo.",
		can_punish: false,
	},
	{
		creditor_id: "CR-004", name: "Bancos Internacionais",
		creditor_type: FOREIGN_BANKS, amount_owed_brl: 500e9, owns_pct_of_total: 8.0,
		purchase_price_pct: 1.0, origin_country: "EUA/Europa",
		bluffs: []string{"Vamos cortar linhas de credito!", "Vai faltar dolar para importar!", "Empresas estrangeiras vao fugir!"},
		real_consequence: "Bancos internacionais perderam dinheiro com EUA em 2008. Perderam com Grecia, Argentina, Russia, Turquia. Sempre voltam a emprestar -- porque ganham com risco. Spreads cobrem risco de default.",
		can_punish: false,
	},
	{
		creditor_id: "CR-005", name: "Fundos de Pensao Brasileiros",
		creditor_type: PENSION_FUNDS, amount_owed_brl: 600e9, owns_pct_of_total: 10.0,
		purchase_price_pct: 1.0, origin_country: "Brasil",
		bluffs: []string{"Aposentados vao perder tudo!", "Os fundos vao quebrar!"},
		real_consequence: "Fundos de pensao tem diversificacao. Renegociacao preserva o valor principal. Risco de nao receber juros extorsivos e diferente de perder tudo. O brasileiro aposentado ja perde com a inflacao que a divida causa.",
		can_punish: false,
	},
	{
		creditor_id: "CR-006", name: "Fundos Soberanos (Paises)",
		creditor_type: SOVEREIGN_FUNDS, amount_owed_brl: 200e9, owns_pct_of_total: 3.0,
		purchase_price_pct: 1.0, origin_country: "China/Oriente Medio",
		bluffs: []string{"Vamos parar de investir no Brasil!", "Vamos cortar relacoes comerciais!"},
		real_consequence: "Paises investem por interesse, nao por amizade. Brasil tem commodities que o mundo precisa. China continua comprando soja independentemente de divida.",
		can_punish: false,
	},
}

// ============================================================================
// 3. FASES DO DEFAULT (O Que Acontece Ano a Ano)
// ============================================================================

type DefaultPhase int

const (
	PRE_DEFAULT DefaultPhase = iota
	ANNOUNCEMENT
	PANIC
	SHOCK
	ADJUSTMENT
	RECOVERY
	GROWTH
	PROSPERITY
)

func (dp DefaultPhase) String() string {
	switch dp {
	case PRE_DEFAULT:
		return "pre_calote"
	case ANNOUNCEMENT:
		return "anuncio"
	case PANIC:
		return "panico"
	case SHOCK:
		return "choque"
	case ADJUSTMENT:
		return "ajuste"
	case RECOVERY:
		return "recuperacao"
	case GROWTH:
		return "crescimento"
	case PROSPERITY:
		return "prosperidade"
	default:
		return "unknown"
	}
}

type YearSimulation struct {
	year                        int
	year_label                  int
	phase                       DefaultPhase
	pay_debt_brl                float64
	pay_interest_brl            float64
	pay_public_investment_brl   float64
	pay_gdp_brl                 float64
	pay_gdp_per_capita          float64
	pay_health_budget           float64
	pay_education_budget        float64
	pay_inflation               float64
	pay_unemployment            float64
	pay_poverty_pct             float64
	nopay_debt_brl              float64
	nopay_interest_brl          float64
	nopay_freed_money_brl       float64
	nopay_public_investment_brl float64
	nopay_gdp_brl               float64
	nopay_gdp_per_capita        float64
	nopay_health_budget         float64
	nopay_education_budget      float64
	nopay_inflation             float64
	nopay_unemployment          float64
	nopay_poverty_pct           float64
	gdp_gap                     float64
	cumulative_freed            float64
	winner                      string
}

// ============================================================================
// 4. MOTOR DE SIMULACAO DUAL
// ============================================================================

type DefaultSimulator struct {
	start_year             int
	years                  int
	initial_debt           float64
	initial_gdp            float64
	interest_rate          float64
	gdp_growth_normal      float64
	population             float64
	revenue_pct_gdp        float64
	health_pct_budget      float64
	education_pct_budget   float64
	investment_pct_gdp     float64
	default_currency_drop  float64
	default_inflation_spike float64
	default_recession      float64
	default_recovery_start int
	default_growth_boost   float64
	simulations            []YearSimulation
}

func NewDefaultSimulator(start_year int, years int) *DefaultSimulator {
	return &DefaultSimulator{
		start_year:              start_year,
		years:                   years,
		initial_debt:            6.0e12,
		initial_gdp:             10.0e12,
		interest_rate:           0.12,
		gdp_growth_normal:       0.025,
		population:              215e6,
		revenue_pct_gdp:         0.18,
		health_pct_budget:       0.04,
		education_pct_budget:    0.06,
		investment_pct_gdp:      0.02,
		default_currency_drop:   0.40,
		default_inflation_spike: 0.15,
		default_recession:       -0.04,
		default_recovery_start:  2,
		default_growth_boost:    0.05,
		simulations:             []YearSimulation{},
	}
}

func (ds *DefaultSimulator) simulate() []YearSimulation {
	ds.simulations = []YearSimulation{}
	pay_debt := ds.initial_debt
	pay_gdp := ds.initial_gdp
	nopay_debt := ds.initial_debt
	nopay_gdp := ds.initial_gdp
	cumulative_freed := 0.0

	for i := 0; i <= ds.years; i++ {
		year_label := ds.start_year + i

		var phase DefaultPhase
		if i == 0 {
			phase = ANNOUNCEMENT
		} else if i <= 1 {
			phase = PANIC
		} else if i <= 2 {
			phase = SHOCK
		} else if i <= 3 {
			phase = ADJUSTMENT
		} else if i <= 7 {
			phase = RECOVERY
		} else if i <= 15 {
			phase = GROWTH
		} else {
			phase = PROSPERITY
		}

		// CAMINHO A: CONTINUA PAGANDO
		pay_interest := pay_debt * ds.interest_rate
		pay_revenue := pay_gdp * ds.revenue_pct_gdp
		pay_primary := pay_revenue * 0.3
		pay_investment := pay_gdp * ds.investment_pct_gdp
		pay_health := pay_gdp * ds.health_pct_budget
		pay_education := pay_gdp * ds.education_pct_budget
		pay_inflation := 0.045 + (pay_debt/pay_gdp)*0.01
		pay_unemployment := 0.09 + (pay_debt/pay_gdp)*0.02
		pay_poverty := 0.25 + (pay_interest/pay_gdp)*0.1

		if i > 0 {
			pay_debt = pay_debt + pay_interest - pay_primary
			pay_gdp = pay_gdp * (1 + ds.gdp_growth_normal)
		}

		// CAMINHO B: PAROU DE PAGAR
		var nopay_interest, nopay_freed, nopay_inflation, nopay_unemployment, nopay_growth float64
		if i == 0 {
			nopay_interest = nopay_debt * ds.interest_rate
			nopay_freed = nopay_interest
			nopay_inflation = ds.default_inflation_spike * 0.3
			nopay_unemployment = 0.09
			nopay_growth = 0.0
			nopay_debt = nopay_debt
		} else if i == 1 {
			nopay_interest = 0
			nopay_freed = pay_interest
			nopay_inflation = ds.default_inflation_spike
			nopay_unemployment = 0.12
			nopay_growth = ds.default_recession
			nopay_debt = nopay_debt * 0.3
		} else if i == 2 {
			nopay_interest = 0
			nopay_freed = pay_interest * 1.2
			nopay_inflation = 0.08
			nopay_unemployment = 0.10
			nopay_growth = 0.01
		} else if i == 3 {
			nopay_interest = 0
			nopay_freed = pay_interest * 1.5
			nopay_inflation = 0.05
			nopay_unemployment = 0.08
			nopay_growth = ds.default_growth_boost * 0.6
		} else if i <= 7 {
			nopay_interest = 0
			nopay_freed = pay_interest * 2.0
			nopay_inflation = 0.04
			nopay_unemployment = 0.06
			nopay_growth = ds.default_growth_boost
		} else if i <= 15 {
			nopay_interest = 0
			nopay_freed = pay_interest * 2.5
			nopay_inflation = 0.035
			nopay_unemployment = 0.04
			nopay_growth = ds.default_growth_boost * 1.3
		} else {
			nopay_interest = 0
			nopay_freed = pay_interest * 3.0
			nopay_inflation = 0.03
			nopay_unemployment = 0.035
			nopay_growth = ds.default_growth_boost * 1.5
		}

		cumulative_freed += nopay_freed

		if i > 0 {
			nopay_gdp = nopay_gdp * (1 + nopay_growth)
		}

		nopay_revenue := nopay_gdp * ds.revenue_pct_gdp
		nopay_investment := nopay_gdp*ds.investment_pct_gdp + nopay_freed*0.6
		nopay_health := nopay_gdp*ds.health_pct_budget + nopay_freed*0.15
		nopay_education := nopay_gdp*ds.education_pct_budget + nopay_freed*0.15

		nopay_poverty := 0.25 - float64(i)*0.008
		if i <= 1 {
			nopay_poverty = 0.27
		}
		if nopay_poverty < 0.03 {
			nopay_poverty = 0.03
		}

		pay_per_capita := pay_gdp / ds.population
		nopay_per_capita := nopay_gdp / ds.population
		gdp_gap := nopay_gdp - pay_gdp

		winner := "nao_pagar"
		if nopay_gdp <= pay_gdp {
			winner = "pagar"
		}
		if i == 0 {
			winner = "igual"
		}

		sim := YearSimulation{
			year: i, year_label: year_label, phase: phase,
			pay_debt_brl: pay_debt, pay_interest_brl: pay_interest, pay_public_investment_brl: pay_investment,
			pay_gdp_brl: pay_gdp, pay_gdp_per_capita: pay_per_capita,
			pay_health_budget: pay_health, pay_education_budget: pay_education,
			pay_inflation: pay_inflation, pay_unemployment: pay_unemployment, pay_poverty_pct: pay_poverty,
			nopay_debt_brl: nopay_debt, nopay_interest_brl: nopay_interest, nopay_freed_money_brl: nopay_freed,
			nopay_public_investment_brl: nopay_investment, nopay_gdp_brl: nopay_gdp, nopay_gdp_per_capita: nopay_per_capita,
			nopay_health_budget: nopay_health, nopay_education_budget: nopay_education,
			nopay_inflation: nopay_inflation, nopay_unemployment: nopay_unemployment, nopay_poverty_pct: nopay_poverty,
			gdp_gap: gdp_gap, cumulative_freed: cumulative_freed, winner: winner,
		}
		ds.simulations = append(ds.simulations, sim)
	}
	return ds.simulations
}

func (ds *DefaultSimulator) crossover_year() int {
	for _, sim := range ds.simulations {
		if sim.year > 0 && sim.nopay_gdp_brl > sim.pay_gdp_brl {
			return sim.year_label
		}
	}
	return 0
}

func (ds *DefaultSimulator) final_comparison() map[string]interface{} {
	last := ds.simulations[len(ds.simulations)-1]
	return map[string]interface{}{
		"years_simulated":           ds.years,
		"crossover_year":            ds.crossover_year(),
		"pay_final_gdp_trillions":   last.pay_gdp_brl / 1e12,
		"nopay_final_gdp_trillions": last.nopay_gdp_brl / 1e12,
		"gdp_difference_trillions":  (last.nopay_gdp_brl - last.pay_gdp_brl) / 1e12,
		"gdp_advantage_pct":         ((last.nopay_gdp_brl/last.pay_gdp_brl)-1)*100,
		"pay_final_debt_trillions":  last.pay_debt_brl / 1e12,
		"nopay_final_debt_trillions": last.nopay_debt_brl / 1e12,
		"total_freed_trillions":     last.cumulative_freed / 1e12,
		"pay_poverty_final":         last.pay_poverty_pct * 100,
		"nopay_poverty_final":       last.nopay_poverty_pct * 100,
		"pay_unemployment_final":    last.pay_unemployment * 100,
		"nopay_unemployment_final":  last.nopay_unemployment * 100,
		"winner":                    func() string { if last.nopay_gdp_brl > last.pay_gdp_brl { return "NAO PAGAR" } else { return "PAGAR" } }(),
	}
}

// ============================================================================
// 5. O QUE O AGIOTA DIZ vs O QUE ACONTECE
// ============================================================================

var TRUTHS = []map[string]string{
	{"ameaca": "O sistema financeiro vai colapsar!", "realidade": "Bancos brasileiros sobreviveram a Hyperinflacao (80s), Plano Real (94), crise 2008. Sobrevivem a default.", "exemplos": "Argentina (2001, 2014), Islandia (2008), Grecia (2012), Russia (1998), Equador (2008). Todos existem."},
	{"ameaca": "Vai faltar comida!", "realidade": "Brasil e um dos maiores produtores de alimentos do mundo. Default nao queima plantacao.", "exemplos": "Argentina deu calote e continua exportando carne e soja."},
	{"ameaca": "O dolar vai disparar!", "realidade": "Dolar dispara por 6-12 meses. Depois estabiliza. Exportacoes ficam mais compencivel. Industria nacional renasce.", "exemplos": "Islandia: coroa islandesa caiu 50% em 2008. Recuperou e hoje tem menor desigualdade da Europa."},
	{"ameaca": "Inflacao vai explodir!", "realidade": "Inflacao sobe por 1-2 anos. Mas a divida extinta REMOVE pressao fiscal permanente. Sem juros extorsivos, inflacao estrutural CAI.", "exemplos": "Equador (Correa): defaultou, inflacao caiu, pobreza despencou."},
	{"ameaca": "Ninguem vai mais emprestar!", "realidade": "Mercados tem memoria curta. Argentina defaultou 9 vezes. Ainda emprestam. Risco paga prêmio.", "exemplos": "Russia foi banida em 2022. Sao titulos deram 15% ao ano. Gente comprou."},
	{"ameaca": "Vao confiscar reservas!", "realidade": "Reservas estao protegidas por imunidade soberana. Vulture funds litigam por decadas e recebem fracoes.", "exemplos": "Argentina vs Elliott Management: 15 anos de processo. Receve 75% a mais -- mas so depois de 15 anos."},
	{"ameaca": "A democracia vai cair!", "realidade": "Default nao derruba democracia. AUSTERIDADE para pagar divida derruba. Greca eisende com Nazis (Aurora Dourada) por austeridade do FMI.", "exemplos": "Islandia: defaultou, PRESIDIU banqueiros, democracia mais forte."},
	{"ameaca": "Os pobres vao sofrer!", "realidade": "Os pobres JA sofrem pagando R$ 500 bi/ano em juros. Default redireciona esse dinheiro para saude, educacao, moradia.", "exemplos": "Equador: pobreza caiu de 36% para 21% apos default de 2008."},
	{"ameaca": "As empresas vao falir!", "realidade": "Empresas EXPORTADORAS ganham com moeda desvalorizada. Empresas ligadas a divida perdem. Mas o pais se reequilibra.", "exemplos": "Argentina: Mal do default e curto prazo. Em 3-5 anos, exportacao dispara."},
	{"ameaca": "O Brasil vai virar Venezuela!", "realidade": "Venezuela quebrou por SANCOES, nao por default. Brasil tem reservas, producao, diversificacao. Analogia falsa.", "exemplos": "Equador, Islandia, Argentina -- nenhum virou Venezuela."},
}

// ============================================================================
// 6. SIMULACAO VISUAL
// ============================================================================

func render_comparison_chart(simulations []YearSimulation) string {
	lines := ""
	lines += "\n" + "======================================================================\n"
	lines += "  PIB: CONTINUA PAGANDO vs PARA DE PAGAR\n"
	lines += "======================================================================\n\n"

	max_gdp := 0.0
	for _, s := range simulations {
		if s.pay_gdp_brl > max_gdp { max_gdp = s.pay_gdp_brl }
		if s.nopay_gdp_brl > max_gdp { max_gdp = s.nopay_gdp_brl }
	}
	bar_width := 35

	for _, s := range simulations {
		pay_bar_len := int((s.pay_gdp_brl / max_gdp) * float64(bar_width))
		nopay_bar_len := int((s.nopay_gdp_brl / max_gdp) * float64(bar_width))
		if pay_bar_len < 1 { pay_bar_len = 1 }
		if nopay_bar_len < 1 { nopay_bar_len = 1 }

		pay_bar := ""
		for i := 0; i < pay_bar_len; i++ { pay_bar += "P" }
		nopay_bar := ""
		for i := 0; i < nopay_bar_len; i++ { nopay_bar += "L" }

		phase_marker := ""
		if s.phase == PANIC { phase_marker = " [PANICO]" }
		if s.phase == SHOCK { phase_marker = " [CHOQUE]" }
		if s.phase == RECOVERY { phase_marker = " [RECUPERANDO]" }
		if s.phase == GROWTH { phase_marker = " [DISPARANDO]" }
		if s.phase == PROSPERITY { phase_marker = " [PRÓSPERO]" }

		lines += fmt.Sprintf("  %d PAGAR: [%s] R$ %.1fT\n", s.year_label, pay_bar, s.pay_gdp_brl/1e12)
		lines += fmt.Sprintf("      LIVRE: [%s] R$ %.1fT%s\n\n", nopay_bar, s.nopay_gdp_brl/1e12, phase_marker)
	}
	lines += "  P = Continua pagando (escravo)\n"
	lines += "  L = Para de pagar (livre)\n\n"
	return lines
}

func render_poverty_chart(simulations []YearSimulation) string {
	lines := ""
	lines += "\n" + "======================================================================\n"
	lines += "  POBREZA (% DA POPULACAO): PAGAR vs NAO PAGAR\n"
	lines += "======================================================================\n\n"

	for _, s := range simulations {
		pay_bar_len := int(s.pay_poverty_pct * 50)
		nopay_bar_len := int(s.nopay_poverty_pct * 50)
		pay_bar := ""
		for i := 0; i < pay_bar_len; i++ { pay_bar += "X" }
		nopay_bar := ""
		for i := 0; i < nopay_bar_len; i++ { nopay_bar += "O" }

		lines += fmt.Sprintf("  %d PAGAR: [%s] %.1f%%\n", s.year_label, pay_bar, s.pay_poverty_pct*100)
		lines += fmt.Sprintf("      LIVRE: [%s] %.1f%%\n\n", nopay_bar, s.nopay_poverty_pct*100)
	}
	lines += "  X = Pobreza pagando divida (estagnada/alta)\n"
	lines += "  O = Pobreza sem pagar divida (desabando)\n\n"
	return lines
}

func render_truth_table() string {
	lines := ""
	lines += "\n" + "======================================================================\n"
	lines += "O AGIOTA DIZ vs O QUE REALMENTE ACONTECE\n"
	lines += "======================================================================\n"

	for i, truth := range TRUTHS {
		lines += fmt.Sprintf("\n  AMEACA %d: %s\n", i+1, truth["ameaca"])
		lines += fmt.Sprintf("  REALIDADE: %s\n", truth["realidade"])
		lines += fmt.Sprintf("  PROVA: %s\n", truth["exemplos"])
		lines += "  ------------------------------------------------------------------\n"
	}
	lines += "\n  O agiota so tem poder se voce tiver MEDO.\n"
	lines += "  O medo e a arma dele. A verdade e o antidoto.\n\n"
	return lines
}

func render_creditors() string {
	lines := ""
	lines += "\n" + "======================================================================\n"
	lines += "QUEM E O AGIOTA?\n"
	lines += "======================================================================\n"

	for _, c := range CREDITORS {
		lines += fmt.Sprintf("\n  %s\n", c.name)
		lines += fmt.Sprintf("  Tipo: %s\n", c.creditor_type.String())
		lines += fmt.Sprintf("  Valor: R$ %.0f bilhoes (%.0f%% da divida)\n", c.amount_owed_brl/1e9, c.owns_pct_of_total)
		lines += fmt.Sprintf("  Comprou por: %.0f centavos de cada real\n", c.purchase_price_pct*100)
		punish := "NAO"
		if c.can_punish { punish = "SIM" }
		lines += fmt.Sprintf("  Pode punir de verdade? %s\n", punish)
		lines += fmt.Sprintf("  O que diz: \"%s\"\n", c.bluffs[0])
		lines += fmt.Sprintf("  O que acontece: %s\n", c.real_consequence)
	}
	lines += "\n  O agiota comprou por 25 centavos. Quer 100.\n"
	lines += "  Paga 25. Fecha o livro. Fim do agiota.\n\n"
	return lines
}

func render_timeline(simulations []YearSimulation) string {
	lines := ""
	lines += "\n" + "======================================================================\n"
	lines += "LINHA DO TEMPO: O QUE ACONTECE APOS PARAR DE PAGAR\n"
	lines += "======================================================================\n"

	for idx, s := range simulations {
		lines += fmt.Sprintf("\n  ANO %d (%d) -- FASE: %s\n", s.year, s.year_label, s.phase.String())
		if s.phase == ANNOUNCEMENT {
			lines += "    O Brasil anuncia: NAO VAMOS PAGAR.\n"
			lines += "    Agiotas gritam. Midia apavora. Bolsa cai.\n"
			lines += "    Povo pergunta: 'E agora?'\n"
			lines += "    Resposta: 'O sol nasce amanha.'\n"
		} else if s.phase == PANIC {
			lines += fmt.Sprintf("    PANICO. Dolar sobe. Inflacao %.0f%%.\n", s.nopay_inflation*100)
			lines += fmt.Sprintf("    Desemprego sobe para %.0f%%.\n", s.nopay_unemployment*100)
			lines += "    Agiotas processam. Midia diz 'Eu avisei!'.\n"
			lines += fmt.Sprintf("    Mas: R$ %.0f bi ANTES iam pro agiota.\n", s.nopay_freed_money_brl/1e9)
			lines += "    Agora vai para: saude, educacao, infraestrutura.\n"
		} else if s.phase == SHOCK {
			lines += fmt.Sprintf("    AINDA DOLORIDO. Mas inflacao caindo: %.0f%%.\n", s.nopay_inflation*100)
			lines += "    PIB voltando a crescer.\n"
			lines += fmt.Sprintf("    Investimento publico: R$ %.0f bi\n", s.nopay_public_investment_brl/1e9)
			lines += fmt.Sprintf("    (vs R$ %.0f bi se pagasse)\n", s.pay_public_investment_brl/1e9)
		} else if s.phase == ADJUSTMENT {
			lines += "    NOVO EQUILIBRIO. Sem juros, dinheiro sobe.\n"
			lines += fmt.Sprintf("    Inflacao: %.0f%% (normalizando)\n", s.nopay_inflation*100)
			lines += fmt.Sprintf("    Desemprego: %.0f%% (caindo)\n", s.nopay_unemployment*100)
			if idx > 0 {
				growth := ((s.nopay_gdp_brl / simulations[idx-1].nopay_gdp_brl) - 1) * 100
				lines += fmt.Sprintf("    PIB crescendo %.1f%%\n", growth)
			}
		} else if s.phase == RECOVERY {
			lines += "    RECUPERANDO. PIB acelerando.\n"
			lines += fmt.Sprintf("    Pobreza: %.1f%% (vs %.1f%% pagando)\n", s.nopay_poverty_pct*100, s.pay_poverty_pct*100)
			lines += fmt.Sprintf("    Dinheiro liberado acumulado: R$ %.1f trilhoes\n", s.cumulative_freed/1e12)
			lines += fmt.Sprintf("    Saude: R$ %.0f bi vs R$ %.0f bi\n", s.nopay_health_budget/1e9, s.pay_health_budget/1e9)
		} else if s.phase == GROWTH {
			lines += "    DISPARANDO. Sem divida, sem juros.\n"
			lines += fmt.Sprintf("    PIB: R$ %.1fT vs R$ %.1fT (pagando)\n", s.nopay_gdp_brl/1e12, s.pay_gdp_brl/1e12)
			lines += fmt.Sprintf("    Desemprego: %.1f%% (vs %.1f%%)\n", s.nopay_unemployment*100, s.pay_unemployment*100)
			lines += fmt.Sprintf("    Diferenca acumulada: R$ %.1f trilhoes a favor\n", s.gdp_gap/1e12)
		} else if s.phase == PROSPERITY {
			lines += "    PROSPERO. Pais livre da divida.\n"
			lines += fmt.Sprintf("    PIB: R$ %.1fT vs R$ %.1fT\n", s.nopay_gdp_brl/1e12, s.pay_gdp_brl/1e12)
			lines += fmt.Sprintf("    Pobreza: %.1f%% vs %.1f%%\n", s.nopay_poverty_pct*100, s.pay_poverty_pct*100)
			lines += "    VEREDICTO: nao pagar VALEU A PENA.\n"
		}
	}
	lines += "\n"
	return lines
}

// ============================================================================
// 7. DEMONSTRACAO (main)
// ============================================================================

func main() {
	fmt.Println("======================================================================")
	fmt.Println("OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota")
	fmt.Println("======================================================================")

	sim := NewDefaultSimulator(2025, 20)
	simulations := sim.simulate()

	fmt.Print(render_creditors())
	fmt.Print(render_truth_table())
	fmt.Print(render_comparison_chart(simulations))
	fmt.Print(render_poverty_chart(simulations))
	fmt.Print(render_timeline(simulations))

	comparison := sim.final_comparison()
	crossover := sim.crossover_year()

	fmt.Println("======================================================================")
	fmt.Println("RESULTADO FINAL APOS 20 ANOS")
	fmt.Println("======================================================================")
	fmt.Printf("  CAMINHO A (continua pagando):\n")
	fmt.Printf("    PIB final: R$ %.1f trilhoes\n", comparison["pay_final_gdp_trillions"])
	fmt.Printf("    Divida final: R$ %.1f trilhoes\n", comparison["pay_final_debt_trillions"])
	fmt.Printf("    Pobreza: %.1f%%\n", comparison["pay_poverty_final"])
	fmt.Printf("    Desemprego: %.1f%%\n", comparison["pay_unemployment_final"])

	fmt.Printf("\n  CAMINHO B (parou de pagar):\n")
	fmt.Printf("    PIB final: R$ %.1f trilhoes\n", comparison["nopay_final_gdp_trillions"])
	fmt.Printf("    Divida final: R$ %.1f trilhoes\n", comparison["nopay_final_debt_trillions"])
	fmt.Printf("    Pobreza: %.1f%%\n", comparison["nopay_poverty_final"])
	fmt.Printf("    Desemprego: %.1f%%\n", comparison["nopay_unemployment_final"])
	fmt.Printf("    Dinheiro liberado (20 anos): R$ %.1f trilhoes\n", comparison["total_freed_trillions"])

	fmt.Printf("\n  VANTAGEM DE NAO PAGAR:\n")
	fmt.Printf("    PIB %.0f%% maior\n", comparison["gdp_advantage_pct"])
	fmt.Printf("    Diferenca: R$ %.1f trilhoes\n", comparison["gdp_difference_trillions"])
	fmt.Printf("    Crossover (ano em que ultrapassa): %d\n", crossover)
	fmt.Printf("\n  VENCEDOR: %s\n", comparison["winner"])

	fmt.Println("\n======================================================================")
	fmt.Println("CONCLUSAO")
	fmt.Println("======================================================================")
	fmt.Println()
	fmt.Println("  O agiota diz que e o fim do mundo se voce parar de pagar.")
	fmt.Println("  A simulacao mostra que em 3-5 anos o pais RECUPERA.")
	fmt.Println("  Em 10 anos, esta NA FRENTE.")
	fmt.Println("  Em 20 anos, e OUTRO PAIS.")
	fmt.Println()
	fmt.Println("  O curto prazo doi. O longo prazo liberta.")
	fmt.Println("  Continuar pagando doi PARA SEMPRE.")
	fmt.Println()
	fmt.Println("  O agiota so tem poder se voce tiver MEDO.")
	fmt.Println("  O medo e a arma. A verdade e o antidoto.")
	fmt.Println()
	fmt.Println("  'O Ideal guia. O Executavel opera.'")
}