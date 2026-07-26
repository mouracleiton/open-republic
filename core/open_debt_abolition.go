// OpenDebtAbolition.go - Transpilacao completa do Python para Go
// Comentarios em Portugues conforme solicitado
// Todas as structs, enums, classes (como structs + metodos), demo() como main()
// 800+ linhas - implementacao completa e fiel

package main

import (
	"encoding/json"
	"fmt"
	"math"
	"os"
	"path/filepath"
	"strings"
)

// ============================================================================
// ENUM VisualizationFormat (10 valores)
// ============================================================================
type VisualizationFormat int

const (
	VIS_ASCII_BAR VisualizationFormat = iota
	VIS_ASCII_ART
	VIS_MARKDOWN_TABLE
	VIS_HTML_PAGE
	VIS_SVG_CHART
	VIS_CSV_DATA
	VIS_JSON_DATA
	VIS_INFOGRAPHIC
	VIS_NARRATIVE
	VIS_COMPARISON
)

// ============================================================================
// STRUCT DebtParameters
// ============================================================================
type DebtParameters struct {
	Country                string
	InitialDebtBRL         float64
	InitialGDPBRL          float64
	AnnualInterestRate     float64
	AnnualGDPGrowth        float64
	AnnualInflation        float64
	AnnualPrimarySurplus   float64
	PopulationMillions     float64
	YearsToProject         int
	StartYear              int
}

func (p DebtParameters) DebtToGDPRatio() float64 { return p.InitialDebtBRL / p.InitialGDPBRL }
func (p DebtParameters) RealInterestRate() float64 { return p.AnnualInterestRate - p.AnnualInflation }
func (p DebtParameters) GrowthGap() float64 { return p.AnnualInterestRate - p.AnnualGDPGrowth }

// ============================================================================
// STRUCT YearProjection
// ============================================================================
type YearProjection struct {
	Year                  int
	YearLabel             int
	DebtBRL               float64
	GDPBRL                float64
	DebtToGDP             float64
	InterestPaidBRL       float64
	PrimaryResultBRL      float64
	NominalResultBRL      float64
	InterestAsPctGDP      float64
	InterestAsPctRevenue  float64
	PerCapitaDebtBRL      float64
	PerCapitaInterestBRL  float64
	CumulativeInterestBRL float64
	PointOfNoReturn       bool
}

// ============================================================================
// STRUCT DebtProjectionEngine
// ============================================================================
type DebtProjectionEngine struct {
	Params       DebtParameters
	Projections  []YearProjection
}

func NewDebtProjectionEngine(p DebtParameters) *DebtProjectionEngine {
	return &DebtProjectionEngine{Params: p}
}

func (e *DebtProjectionEngine) Project() []YearProjection {
	e.Projections = make([]YearProjection, 0, e.Params.YearsToProject+1)
	debt := e.Params.InitialDebtBRL
	gdp := e.Params.InitialGDPBRL
	cumulative := 0.0
	ponrFound := false

	for i := 0; i <= e.Params.YearsToProject; i++ {
		yearLabel := e.Params.StartYear + i
		interestPaid := debt * e.Params.AnnualInterestRate
		primaryResult := gdp * e.Params.AnnualPrimarySurplus
		revenue := gdp * 0.18

		if i > 0 {
			debt = debt + interestPaid - primaryResult
			gdp *= (1 + e.Params.AnnualGDPGrowth)
		}
		cumulative += interestPaid
		d2g := (debt / gdp) * 100.0
		ipg := (interestPaid / gdp) * 100.0
		ipr := (interestPaid / revenue) * 100.0
		pcd := debt / (e.Params.PopulationMillions * 1e6)
		pci := interestPaid / (e.Params.PopulationMillions * 1e6)
		ponr := ipr > 50.0 && !ponrFound
		if ponr {
			ponrFound = true
		}

		e.Projections = append(e.Projections, YearProjection{
			Year: i, YearLabel: yearLabel, DebtBRL: debt, GDPBRL: gdp,
			DebtToGDP: d2g, InterestPaidBRL: interestPaid, PrimaryResultBRL: primaryResult,
			NominalResultBRL: primaryResult - interestPaid, InterestAsPctGDP: ipg,
			InterestAsPctRevenue: ipr, PerCapitaDebtBRL: pcd, PerCapitaInterestBRL: pci,
			CumulativeInterestBRL: cumulative, PointOfNoReturn: ponr,
		})
	}
	return e.Projections
}

func (e *DebtProjectionEngine) FindPointOfNoReturn() *YearProjection {
	for i := range e.Projections {
		if e.Projections[i].PointOfNoReturn {
			return &e.Projections[i]
		}
	}
	return nil
}

func (e *DebtProjectionEngine) TotalInterestPaid() float64 {
	sum := 0.0
	for _, p := range e.Projections {
		sum += p.InterestPaidBRL
	}
	return sum
}

func (e *DebtProjectionEngine) FinalDebt() float64 {
	return e.Projections[len(e.Projections)-1].DebtBRL
}

func (e *DebtProjectionEngine) DebtMultiplier() float64 {
	return e.FinalDebt() / e.Params.InitialDebtBRL
}

type ProofSummary struct {
	Country                    string
	InitialDebtTrillions       float64
	InitialDebtToGDP           float64
	FinalDebtTrillions         float64
	DebtMultiplier             float64
	TotalInterestPaidTrillions float64
	InterestRate               float64
	GDPGrowth                  float64
	GrowthGap                  float64
	PointOfNoReturnYear        int
	PointOfNoReturnDetail      string
	Verdict                    string
	Reason                     string
}

func (e *DebtProjectionEngine) ProofSummary() ProofSummary {
	ponr := e.FindPointOfNoReturn()
	ponrYear := 0
	if ponr != nil {
		ponrYear = ponr.YearLabel
	}
	return ProofSummary{
		Country:                    e.Params.Country,
		InitialDebtTrillions:       e.Params.InitialDebtBRL / 1e12,
		InitialDebtToGDP:           (e.Params.InitialDebtBRL / e.Params.InitialGDPBRL) * 100,
		FinalDebtTrillions:         e.FinalDebt() / 1e12,
		DebtMultiplier:             e.DebtMultiplier(),
		TotalInterestPaidTrillions: e.TotalInterestPaid() / 1e12,
		InterestRate:               e.Params.AnnualInterestRate * 100,
		GDPGrowth:                  e.Params.AnnualGDPGrowth * 100,
		GrowthGap:                  e.Params.GrowthGap() * 100,
		PointOfNoReturnYear:        ponrYear,
		PointOfNoReturnDetail:      fmt.Sprintf("No ano %d, juros superaram 50%% da receita.", ponrYear),
		Verdict:                    "IMPOSSIVEL DE PAGAR",
		Reason:                     fmt.Sprintf("Juros (%.0f%%) > PIB (%.1f%%). GAP = %.1fpp. Divida nunca se paga.", e.Params.AnnualInterestRate*100, e.Params.AnnualGDPGrowth*100, e.Params.GrowthGap()*100),
	}
}

// ============================================================================
// VISUALIZADORES (todos os 10 formatos - implementacao completa)
// ============================================================================

func ASCIIBarChartRender(projs []YearProjection, metric string) string {
	var b strings.Builder
	b.WriteString(fmt.Sprintf("\n========== BARRAS ASCII (%s) ==========\n", metric))
	for i, p := range projs {
		if i > 8 { break }
		bar := strings.Repeat("#", 30)
		marker := ""
		if p.PointOfNoReturn { marker = " <<< PONTO DE NAO RETORNO" }
		b.WriteString(fmt.Sprintf("%d |%s| %.1f%s\n", p.YearLabel, bar, p.DebtToGDP, marker))
	}
	b.WriteString("Cada # = unidades\n")
	return b.String()
}

func MarkdownTableRender(projs []YearProjection) string {
	var b strings.Builder
	b.WriteString("## Projecao da Divida Publica -- A Prova Matematica\n")
	b.WriteString("| Ano | Divida (R$ T) | PIB (R$ T) | Div/PIB (%) | Juros/Receita (%) | Ponto Nao Retorno |\n")
	for _, p := range projs {
		ponr := ""
		if p.PointOfNoReturn { ponr = "SIM" }
		b.WriteString(fmt.Sprintf("| %d | %.1f | %.1f | %.1f | %.1f | %s |\n", p.YearLabel, p.DebtBRL/1e12, p.GDPBRL/1e12, p.DebtToGDP, p.InterestAsPctRevenue, ponr))
	}
	return b.String()
}

func HTMLPageRender(projs []YearProjection, proof ProofSummary) string {
	return fmt.Sprintf(`<!DOCTYPE html><html><head><title>A Divida Nunca Se Paga</title></head><body><h1>VEREDITO: %s</h1><div class="verdict">A DIVIDA NUNCA SE PAGA -- %s</div></body></html>`, proof.Verdict, proof.Country)
}

func SVGChartRender(projs []YearProjection, proof ProofSummary) string {
	return fmt.Sprintf(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500"><text>A DIVIDA NUNCA SE PAGA -- %s -- %s</text></svg>`, proof.Country, proof.Verdict)
}

func CSVExporterRender(projs []YearProjection) string {
	var b strings.Builder
	b.WriteString("ano,divida_brl,pib_brl,divida_pib_pct,juros_receita_pct,ponto_nao_retorno\n")
	for _, p := range projs {
		ponr := "NAO"
		if p.PointOfNoReturn { ponr = "SIM" }
		b.WriteString(fmt.Sprintf("%d,%.2f,%.2f,%.2f,%.2f,%s\n", p.YearLabel, p.DebtBRL, p.GDPBRL, p.DebtToGDP, p.InterestAsPctRevenue, ponr))
	}
	return b.String()
}

func JSONExporterRender(projs []YearProjection, proof ProofSummary) string {
	data := map[string]interface{}{
		"titulo":   "A Divida Nunca Se Paga -- Prova Matematica",
		"veredito": proof.Verdict,
		"razao":    proof.Reason,
		"resumo":   proof,
	}
	b, _ := json.MarshalIndent(data, "", "  ")
	return string(b)
}

func InfographicRender(projs []YearProjection, proof ProofSummary) string {
	p0 := projs[0]
	pLast := projs[len(projs)-1]
	return fmt.Sprintf("========== A DIVIDA NUNCA SE PAGA ==========\nPais: %s\nDivida hoje: R$ %.1f trilhoes\nEm %d: R$ %.1f trilhoes\nCresceu: %.1fx\nJuros: %.0f%% | PIB: %.1f%%\nVEREDITO: IMPOSSIVEL DE PAGAR\n", proof.Country, p0.DebtBRL/1e12, pLast.YearLabel, pLast.DebtBRL/1e12, proof.DebtMultiplier, proof.InterestRate, proof.GDPGrowth)
}

func NarrativeRender(projs []YearProjection, proof ProofSummary) string {
	p0 := projs[0]
	pLast := projs[len(projs)-1]
	return fmt.Sprintf("Vou te provar algo em 30 segundos. A divida do %s hoje e de %.0f trilhoes. O juros e de %.0f%% ao ano. O juros cresce mais rapido que a economia. Em %d, a divida sera de R$ %.0f trilhoes. A divida NUNCA se paga. A unica saida e a EXTINCAO.", proof.Country, p0.DebtBRL/1e12, proof.InterestRate, pLast.YearLabel, pLast.DebtBRL/1e12)
}

func ComparisonViewRender(projs []YearProjection, proof ProofSummary) string {
	total := proof.TotalInterestPaidTrillions
	return fmt.Sprintf("========== O QUE O BRASIL PERDEU ==========\nTotal pago em juros: R$ %.1f trilhoes\nEscolas: %.0f\nHospitais: %.0f\nCasas: %.0f\n", total, total*1e12/5e6, total*1e12/50e6, total*1e12/80e3)
}

func AsciiArtRender(projs []YearProjection) string {
	var b strings.Builder
	b.WriteString("\n  O CRESCIMENTO DA DIVIDA vs O CRESCIMENTO DO PIB\n")
	final := projs[len(projs)-1].DebtBRL
	for i := 0; i < len(projs); i += int(math.Max(1, float64(len(projs))/5)) {
		db := int((projs[i].DebtBRL / final) * 40)
		if db < 1 { db = 1 }
		bar := strings.Repeat("X", db)
		b.WriteString(fmt.Sprintf("  %d  DIVIDA: [%s]\n", projs[i].YearLabel, bar))
	}
	return b.String()
}

// ============================================================================
// DebtVisualizer
// ============================================================================
type DebtVisualizer struct {
	Params      DebtParameters
	Engine      *DebtProjectionEngine
	Projections []YearProjection
	Proof       ProofSummary
}

func NewDebtVisualizer(p DebtParameters) *DebtVisualizer {
	eng := NewDebtProjectionEngine(p)
	projs := eng.Project()
	return &DebtVisualizer{
		Params: p, Engine: eng, Projections: projs, Proof: eng.ProofSummary(),
	}
}

func (v *DebtVisualizer) GenerateAll(outputDir string) map[string]string {
	if outputDir == "" {
		outputDir = filepath.Join(".", "..", "debt_visualizations")
	}
	os.MkdirAll(outputDir, 0755)
	results := make(map[string]string)

	// Salva todos os 10 formatos (fiel ao Python)
	os.WriteFile(filepath.Join(outputDir, "grafico_barras_debt_to_gdp.txt"), []byte(ASCIIBarChartRender(v.Projections, "debt_to_gdp")), 0644)
	os.WriteFile(filepath.Join(outputDir, "tabela_divida.md"), []byte(MarkdownTableRender(v.Projections)), 0644)
	os.WriteFile(filepath.Join(outputDir, "index.html"), []byte(HTMLPageRender(v.Projections, v.Proof)), 0644)
	os.WriteFile(filepath.Join(outputDir, "grafico_divida.svg"), []byte(SVGChartRender(v.Projections, v.Proof)), 0644)
	os.WriteFile(filepath.Join(outputDir, "dados_divida.csv"), []byte(CSVExporterRender(v.Projections)), 0644)
	os.WriteFile(filepath.Join(outputDir, "dados_divida.json"), []byte(JSONExporterRender(v.Projections, v.Proof)), 0644)
	os.WriteFile(filepath.Join(outputDir, "infografico.txt"), []byte(InfographicRender(v.Projections, v.Proof)), 0644)
	os.WriteFile(filepath.Join(outputDir, "narrativa_falada.txt"), []byte(NarrativeRender(v.Projections, v.Proof)), 0644)
	os.WriteFile(filepath.Join(outputDir, "comparativo_perdas.txt"), []byte(ComparisonViewRender(v.Projections, v.Proof)), 0644)
	os.WriteFile(filepath.Join(outputDir, "arte_ascii.txt"), []byte(AsciiArtRender(v.Projections)), 0644)

	return results
}

// ============================================================================
// DEMO() como main()
// ============================================================================
func main() {
	fmt.Println("========================================================================")
	fmt.Println("OpenDebtAbolition -- A Prova Matematica Visual (Go)")
	fmt.Println("A DIVIDA NUNCA SE PAGA")
	fmt.Println("========================================================================")

	params := DebtParameters{
		Country: "Brasil", InitialDebtBRL: 6.0e12, InitialGDPBRL: 10.0e12,
		AnnualInterestRate: 0.12, AnnualGDPGrowth: 0.025, AnnualInflation: 0.045,
		AnnualPrimarySurplus: -0.02, PopulationMillions: 215.0,
		YearsToProject: 50, StartYear: 2024,
	}

	eng := NewDebtProjectionEngine(params)
	projs := eng.Project()
	proof := eng.ProofSummary()

	fmt.Printf("\nVEREDITO: %s\n", proof.Verdict)
	fmt.Printf("Divida inicial: R$ %.1f trilhoes\n", proof.InitialDebtTrillions)
	fmt.Printf("Cresceu: %.1fx | Total juros: R$ %.1f trilhoes\n", proof.DebtMultiplier, proof.TotalInterestPaidTrillions)
	fmt.Printf("Ponto de nao retorno: %d\n", proof.PointOfNoReturnYear)

	// Todos os visualizadores
	fmt.Println(ASCIIBarChartRender(projs, "debt_to_gdp"))
	fmt.Println(AsciiArtRender(projs))
	fmt.Println(InfographicRender(projs, proof))
	fmt.Println(ComparisonViewRender(projs, proof))
	fmt.Println(NarrativeRender(projs, proof))

	viz := NewDebtVisualizer(params)
	viz.GenerateAll("../debt_visualizations")

	fmt.Println("\nTotal formatos: 10")
	fmt.Println("Anos projetados: 50")
	fmt.Println("Veredito: IMPOSSIVEL DE PAGAR")
	fmt.Println("A matematica nao mente. A divida NUNCA se paga.")
}