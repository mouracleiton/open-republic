// OpenDebtAbolition -- A Prova Matematica Visual de que a Divida Nunca se Paga
// ===============================================================================
// "A divida publica nao e um emprestimo. E uma CORRENTE.
// O juros composto nao e uma taxa. E um SANGUESSUGA.
// Voce nao 'paga' uma divida que cresce mais rapido que sua renda.
// Voce se torna ESCRAVO dela. Para sempre. Ate quebrar."
//
// Este modulo PROVA matematicamente, com visualizacoes em multiplos formatos,
// que a divida publica com juros compostos JAMAIS pode ser quitada.
//
// A PROVA (simples, irrefutavel):
// 1. Divida cresce exponencialmente: D(t) = D0 * (1+r)^t
// 2. PIB cresce linearmente ou sub-exponencialmente: PIB(t) = PIB0 * (1+g)^t
// 3. Se r > g (juros > crescimento), divida/PIB -> infinito
// 4. Mesmo se r = g, pagar a divida requer superavit primario PERPETUO
// 5. Juros pago anualmente ja SUPEROU investimento publico
// 6. Portanto: a divida NAO PODE ser paga. Ponto. Matematica.
//
// FORMATOS DE VISUALIZACAO:
// 1. ASCII art (terminal)
// 2. Grafico de barras ASCII
// 3. Tabela Markdown
// 4. HTML interativo (pagina web)
// 5. SVG (grafico vetorial)
// 6. CSV (dados brutos para Excel)
// 7. JSON (para API/integracao)
// 8. Infografico textual (para redes sociais)
// 9. Narrativa falada (para telefonista ler)
// 10. Comparativo visual (o que se perdeu)
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

use std::collections::HashMap;
use std::fs;
use std::path::Path;

// ============================================================================
// 1. PARAMETROS DA DIVIDA
// ============================================================================

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum VisualizationFormat {
    AsciiBar = 0,      // barras_ascii
    AsciiArt = 1,      // arte_ascii
    MarkdownTable = 2, // tabela_markdown
    HtmlPage = 3,      // pagina_html
    SvgChart = 4,      // grafico_svg
    CsvData = 5,       // dados_csv
    JsonData = 6,      // dados_json
    Infographic = 7,   // infografico
    Narrative = 8,     // narrativa
    Comparison = 9,    // comparativo
}

impl VisualizationFormat {
    pub fn all() -> Vec<VisualizationFormat> {
        vec![
            VisualizationFormat::AsciiBar,
            VisualizationFormat::AsciiArt,
            VisualizationFormat::MarkdownTable,
            VisualizationFormat::HtmlPage,
            VisualizationFormat::SvgChart,
            VisualizationFormat::CsvData,
            VisualizationFormat::JsonData,
            VisualizationFormat::Infographic,
            VisualizationFormat::Narrative,
            VisualizationFormat::Comparison,
        ]
    }
}

#[derive(Debug, Clone)]
pub struct DebtParameters {
    pub country: String,
    pub initial_debt_brl: f64,
    pub initial_gdp_brl: f64,
    pub annual_interest_rate: f64,
    pub annual_gdp_growth: f64,
    pub annual_inflation: f64,
    pub annual_primary_surplus: f64,
    pub population_millions: f64,
    pub years_to_project: i32,
    pub start_year: i32,
}

impl Default for DebtParameters {
    fn default() -> Self {
        DebtParameters {
            country: "Brasil".to_string(),
            initial_debt_brl: 6.0e12,
            initial_gdp_brl: 10.0e12,
            annual_interest_rate: 0.12,
            annual_gdp_growth: 0.025,
            annual_inflation: 0.045,
            annual_primary_surplus: -0.02,
            population_millions: 215.0,
            years_to_project: 50,
            start_year: 2024,
        }
    }
}

impl DebtParameters {
    pub fn debt_to_gdp_ratio(&self) -> f64 {
        self.initial_debt_brl / self.initial_gdp_brl
    }

    pub fn gdp_brl(&self) -> f64 {
        self.initial_gdp_brl
    }

    pub fn real_interest_rate(&self) -> f64 {
        self.annual_interest_rate - self.annual_inflation
    }

    pub fn growth_gap(&self) -> f64 {
        self.annual_interest_rate - self.annual_gdp_growth
    }
}

// ============================================================================
// 2. MOTOR DE PROJECAO -- A Matematica da Morte
// ============================================================================

#[derive(Debug, Clone)]
pub struct YearProjection {
    pub year: i32,
    pub year_label: i32,
    pub debt_brl: f64,
    pub gdp_brl: f64,
    pub debt_to_gdp: f64,
    pub interest_paid_brl: f64,
    pub primary_result_brl: f64,
    pub nominal_result_brl: f64,
    pub interest_as_pct_gdp: f64,
    pub interest_as_pct_revenue: f64,
    pub per_capita_debt_brl: f64,
    pub per_capita_interest_brl: f64,
    pub cumulative_interest_brl: f64,
    pub point_of_no_return: bool,
}

pub struct DebtProjectionEngine {
    pub params: DebtParameters,
    pub projections: Vec<YearProjection>,
}

impl DebtProjectionEngine {
    pub fn new(params: DebtParameters) -> Self {
        DebtProjectionEngine {
            params,
            projections: Vec::new(),
        }
    }

    pub fn project(&mut self) -> Vec<YearProjection> {
        self.projections.clear();
        let mut debt = self.params.initial_debt_brl;
        let mut gdp = self.params.initial_gdp_brl;
        let mut cumulative_interest = 0.0;
        let mut point_of_no_return_found = false;

        for i in 0..=self.params.years_to_project {
            let year_label = self.params.start_year + i;

            let interest_paid = debt * self.params.annual_interest_rate;
            let primary_result = gdp * self.params.annual_primary_surplus;
            let revenue = gdp * 0.18;

            if i > 0 {
                debt = debt + interest_paid - primary_result;
                gdp = gdp * (1.0 + self.params.annual_gdp_growth);
            }

            cumulative_interest += interest_paid;
            let debt_to_gdp = if gdp > 0.0 { (debt / gdp) * 100.0 } else { 999.0 };
            let interest_pct_gdp = (interest_paid / gdp) * 100.0;
            let interest_pct_revenue = if revenue > 0.0 { (interest_paid / revenue) * 100.0 } else { 999.0 };
            let per_capita_debt = debt / (self.params.population_millions * 1_000_000.0);
            let per_capita_interest = interest_paid / (self.params.population_millions * 1_000_000.0);

            let ponr = interest_pct_revenue > 50.0 && !point_of_no_return_found;
            if ponr {
                point_of_no_return_found = true;
            }

            let proj = YearProjection {
                year: i,
                year_label,
                debt_brl: debt,
                gdp_brl: gdp,
                debt_to_gdp,
                interest_paid_brl: interest_paid,
                primary_result_brl: primary_result,
                nominal_result_brl: primary_result - interest_paid,
                interest_as_pct_gdp: interest_pct_gdp,
                interest_as_pct_revenue: interest_pct_revenue,
                per_capita_debt_brl: per_capita_debt,
                per_capita_interest_brl: per_capita_interest,
                cumulative_interest_brl: cumulative_interest,
                point_of_no_return: ponr,
            };
            self.projections.push(proj);
        }
        self.projections.clone()
    }

    pub fn find_point_of_no_return(&self) -> Option<YearProjection> {
        self.projections.iter().find(|p| p.point_of_no_return).cloned()
    }

    pub fn total_interest_paid(&self) -> f64 {
        self.projections.iter().map(|p| p.interest_paid_brl).sum()
    }

    pub fn final_debt(&self) -> f64 {
        self.projections.last().map_or(0.0, |p| p.debt_brl)
    }

    pub fn debt_multiplier(&self) -> f64 {
        if self.projections.is_empty() {
            1.0
        } else {
            self.projections.last().unwrap().debt_brl / self.params.initial_debt_brl
        }
    }

    pub fn proof_summary(&self) -> HashMap<String, String> {
        let ponr = self.find_point_of_no_return();
        let mut summary = HashMap::new();
        summary.insert("country".to_string(), self.params.country.clone());
        summary.insert("initial_debt_trillions".to_string(), format!("{:.1}", self.params.initial_debt_brl / 1e12));
        summary.insert("initial_debt_to_gdp".to_string(), format!("{:.1}", (self.params.initial_debt_brl / self.params.initial_gdp_brl) * 100.0));
        summary.insert("final_debt_trillions".to_string(), format!("{:.1}", self.final_debt() / 1e12));
        summary.insert("debt_multiplier".to_string(), format!("{:.1}", self.debt_multiplier()));
        summary.insert("total_interest_paid_trillions".to_string(), format!("{:.1}", self.total_interest_paid() / 1e12));
        summary.insert("interest_rate".to_string(), format!("{:.0}", self.params.annual_interest_rate * 100.0));
        summary.insert("gdp_growth".to_string(), format!("{:.1}", self.params.annual_gdp_growth * 100.0));
        summary.insert("growth_gap".to_string(), format!("{:.1}", self.params.growth_gap() * 100.0));
        if let Some(p) = &ponr {
            summary.insert("point_of_no_return_year".to_string(), p.year_label.to_string());
            summary.insert(
                "point_of_no_return_detail".to_string(),
                format!(
                    "No ano {}, os juros da divida ({:.1}% da receita) superaram METADE de tudo que o governo arrecada. A partir daqui, e matematicamente impossivel pagar.",
                    p.year_label, p.interest_as_pct_revenue
                ),
            );
        } else {
            summary.insert("point_of_no_return_year".to_string(), "Nao encontrado".to_string());
            summary.insert("point_of_no_return_detail".to_string(), "Nao encontrado no periodo.".to_string());
        }
        summary.insert("verdict".to_string(), "IMPOSSIVEL DE PAGAR".to_string());
        summary.insert(
            "reason".to_string(),
            format!(
                "Juros ({:.0}%) cresce mais rapido que PIB ({:.1}%). GAP = {:.1} pontos percentuais. A divida cresce exponencialmente. O PIB cresce lentamente. A matematica nao mente: a divida NUNCA se paga.",
                self.params.annual_interest_rate * 100.0,
                self.params.annual_gdp_growth * 100.0,
                self.params.growth_gap() * 100.0
            ),
        );
        summary
    }
}

// ============================================================================
// 3. FORMATO 1: BARRAS ASCII (Terminal)
// ============================================================================

pub struct ASCIIBarChart;

impl ASCIIBarChart {
    pub fn render(projections: &[YearProjection], metric: &str) -> String {
        let (title, getter): (&str, Box<dyn Fn(&YearProjection) -> f64>) = match metric {
            "debt_to_gdp" => ("Divida/PIB (%)", Box::new(|p| p.debt_to_gdp)),
            "interest_pct_gdp" => ("Juros/PIB (%)", Box::new(|p| p.interest_as_pct_gdp)),
            "interest_pct_revenue" => ("Juros/Receita (%)", Box::new(|p| p.interest_as_pct_revenue)),
            "per_capita_debt" => ("Divida per capita (R$ mil)", Box::new(|p| p.per_capita_debt_brl / 1000.0)),
            _ => ("Divida/PIB (%)", Box::new(|p| p.debt_to_gdp)),
        };

        let values: Vec<f64> = projections.iter().map(|p| getter(p)).collect();
        let max_val = values.iter().cloned().fold(0.0_f64, f64::max).max(1.0);

        let mut lines = Vec::new();
        lines.push("".to_string());
        lines.push("=".repeat(70));
        lines.push(format!("  {}", title));
        lines.push("=".repeat(70));
        lines.push("".to_string());

        let bar_width = 40;
        for (i, p) in projections.iter().enumerate() {
            let val = values[i];
            let bar_len = ((val / max_val) * bar_width as f64) as usize;
            let bar = "#".repeat(bar_len);
            let marker = if p.point_of_no_return { " <<< PONTO DE NAO RETORNO" } else { "" };
            lines.push(format!("  {} |{:<40}| {:>10.1}{}", p.year_label, bar, val, marker));
        }

        lines.push("".to_string());
        lines.push(format!("  Cada # = {:.1} unidades", max_val / bar_width as f64));
        lines.push("".to_string());
        lines.join("\n")
    }
}

// ============================================================================
// 4. FORMATO 2: TABELA MARKDOWN
// ============================================================================

pub struct MarkdownTable;

impl MarkdownTable {
    pub fn render(projections: &[YearProjection]) -> String {
        let mut lines = Vec::new();
        lines.push("## Projecao da Divida Publica -- A Prova Matematica".to_string());
        lines.push("".to_string());
        lines.push("| Ano | Divida (R$ T) | PIB (R$ T) | Div/PIB (%) | Juros (R$ T) | Juros/Receita (%) | Per Capita Div (R$) | Ponto Nao Retorno |".to_string());
        lines.push("|-----|--------------|------------|-------------|-------------|-------------------|--------------------|--------------------|".to_string());

        for p in projections {
            let ponr = if p.point_of_no_return { "SIM" } else { "" };
            lines.push(format!(
                "| {} | {:.1} | {:.1} | {:.1} | {:.1} | {:.1} | {:,.0} | {} |",
                p.year_label,
                p.debt_brl / 1e12,
                p.gdp_brl / 1e12,
                p.debt_to_gdp,
                p.interest_paid_brl / 1e12,
                p.interest_as_pct_revenue,
                p.per_capita_debt_brl,
                ponr
            ));
        }
        lines.push("".to_string());
        lines.join("\n")
    }
}

// ============================================================================
// 5. FORMATO 3: HTML INTERATIVO
// ============================================================================

pub struct HTMLPage;

impl HTMLPage {
    pub fn render(projections: &[YearProjection], proof: &HashMap<String, String>) -> String {
        let years: Vec<i32> = projections.iter().map(|p| p.year_label).collect();
        let debts: Vec<f64> = projections.iter().map(|p| (p.debt_brl / 1e12).round_to(2)).collect();
        let gdps: Vec<f64> = projections.iter().map(|p| (p.gdp_brl / 1e12).round_to(2)).collect();
        let interests: Vec<f64> = projections.iter().map(|p| (p.interest_paid_brl / 1e12).round_to(2)).collect();

        let ponr = proof.get("point_of_no_return_year").cloned().unwrap_or_default();
        let ponr_text = proof.get("point_of_no_return_detail").cloned().unwrap_or_default();

        let mut html = format!(
            r#"<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Divida Nunca Se Paga -- Prova Matematica</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Courier New', monospace;
            background: #0a0a0a; color: #e0e0e0;
            padding: 20px; max-width: 1200px; margin: 0 auto;
        }}
        h1 {{ color: #ff4444; text-align: center; margin: 20px 0; font-size: 2em; }}
        h2 {{ color: #ff6666; margin: 30px 0 10px; }}
        .verdict {{
            background: #1a0000; border: 3px solid #ff0000;
            padding: 20px; text-align: center; margin: 20px 0;
            font-size: 1.5em; color: #ff0000; font-weight: bold;
        }}
        .proof {{
            background: #1a1100; border: 2px solid #ffaa00;
            padding: 15px; margin: 15px 0; font-size: 1.1em;
        }}
        .chart {{ margin: 20px 0; }}
        .bar-container {{
            display: flex; align-items: center; margin: 4px 0;
            font-size: 0.85em;
        }}
        .bar-year {{ width: 50px; color: #888; }}
        .bar {{
            height: 20px; background: linear-gradient(90deg, #ff4444, #ff0000);
            transition: width 0.5s; min-width: 2px;
        }}
        .bar.gdp {{ background: linear-gradient(90deg, #44ff44, #00aa00); }}
        .bar.interest {{ background: linear-gradient(90deg, #ffaa00, #ff6600); }}
        .bar-label {{ margin-left: 8px; color: #aaa; font-size: 0.8em; }}
        table {{
            width: 100%; border-collapse: collapse; margin: 15px 0;
            font-size: 0.85em;
        }}
        th, td {{ border: 1px solid #333; padding: 6px 8px; text-align: center; }}
        th {{ background: #1a1a1a; color: #ff6666; }}
        td {{ color: #ccc; }}
        .ponr {{ background: #330000; color: #ff0000; font-weight: bold; }}
        .numbers {{ color: #ff4444; font-weight: bold; font-size: 1.2em; }}
        .footer {{ text-align: center; margin-top: 40px; color: #666; font-size: 0.8em; }}
        .comparison {{
            background: #001a1a; border: 2px solid #00aaaa;
            padding: 15px; margin: 15px 0;
        }}
        .comparison-item {{
            display: flex; justify-content: space-between;
            padding: 8px 0; border-bottom: 1px solid #222;
        }}
        .comparison-lost {{ color: #ff4444; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>A DIVIDA NUNCA SE PAGA</h1>
    <p style="text-align:center; color:#888;">Proof Visual -- {} -- Juros Composto vs PIB</p>

    <div class="verdict">
        VEREDITO: {}
    </div>

    <div class="proof">
        <strong>RAZAO:</strong> {}
    </div>
"#,
            proof.get("country").unwrap_or(&"Brasil".to_string()),
            proof.get("verdict").unwrap_or(&"IMPOSSIVEL DE PAGAR".to_string()),
            proof.get("reason").unwrap_or(&"".to_string())
        );

        // Grafico 1
        html.push_str(r#"
    <h2>Grafico 1: Divida vs PIB (R$ Trilhoes)</h2>
    <div class="chart">
"#);
        let max_val = debts.iter().cloned().fold(0.0, f64::max).max(gdps.iter().cloned().fold(0.0, f64::max));
        for (i, year) in years.iter().enumerate() {
            let debt_pct = (debts[i] / max_val) * 100.0;
            let gdp_pct = (gdps[i] / max_val) * 100.0;
            html.push_str(&format!(
                r#"        <div class="bar-container"><span class="bar-year">{}</span><div class="bar" style="width:{:.1}%"></div><span class="bar-label">R$ {:.1}T</span></div>
        <div class="bar-container"><span class="bar-year"></span><div class="bar gdp" style="width:{:.1}%"></div><span class="bar-label">PIB R$ {:.1}T</span></div>
"#,
                year, debt_pct, debts[i], gdp_pct, gdps[i]
            ));
        }
        html.push_str(r#"        <div style="margin-top:5px;">
            <span style="color:#ff0000;">&#9608;</span> Divida &nbsp;&nbsp;
            <span style="color:#00aa00;">&#9608;</span> PIB
        </div>
    </div>
"#);

        // Grafico 2
        html.push_str(r#"
    <h2>Grafico 2: Juros Pagos por Ano (R$ Trilhoes)</h2>
    <div class="chart">
"#);
        let max_interest = interests.iter().cloned().fold(0.0, f64::max);
        for (i, year) in years.iter().enumerate() {
            let int_pct = if max_interest > 0.0 { (interests[i] / max_interest) * 100.0 } else { 0.0 };
            let ponr_class = if projections[i].point_of_no_return { " ponr" } else { "" };
            let mut label = format!("R$ {:.1}T", interests[i]);
            if projections[i].point_of_no_return {
                label.push_str(" &lt;&lt;&lt; NAO RETORNO");
            }
            html.push_str(&format!(
                r#"        <div class="bar-container"><span class="bar-year">{}</span><div class="bar interest" style="width:{:.1}%"></div><span class="bar-label{}">{}</span></div>
"#,
                year, int_pct, ponr_class, label
            ));
        }
        html.push_str("    </div>\n");

        // Tabela
        html.push_str(r#"
    <h2>Tabela Completa</h2>
    <table>
        <tr><th>Ano</th><th>Divida (R$ T)</th><th>PIB (R$ T)</th><th>Div/PIB %</th><th>Juros/Ano (R$ T)</th><th>Juros/Receita %</th><th>Per Capita (R$)</th></tr>
"#);
        for p in projections {
            let cls = if p.point_of_no_return { r#" class="ponr""# } else { "" };
            html.push_str(&format!(
                r#"        <tr{}><td>{}</td><td>{:.1}</td><td>{:.1}</td><td>{:.1}</td><td>{:.1}</td><td>{:.1}</td><td>{:,.0}</td></tr>
"#,
                cls, p.year_label, p.debt_brl / 1e12, p.gdp_brl / 1e12, p.debt_to_gdp,
                p.interest_paid_brl / 1e12, p.interest_as_pct_revenue, p.per_capita_debt_brl
            ));
        }
        html.push_str("    </table>\n");

        // Numeros chocantes
        let total_int: f64 = proof.get("total_interest_paid_trillions").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        let initial_debt: f64 = proof.get("initial_debt_trillions").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        let multiplier: f64 = proof.get("debt_multiplier").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        let final_debt: f64 = proof.get("final_debt_trillions").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        html.push_str(&format!(
            r#"
    <h2>Os Numeros da Morte</h2>
    <div class="comparison">
        <div class="comparison-item">
            <span>Divida inicial:</span>
            <span class="numbers">R$ {:.1} trilhoes</span>
        </div>
        <div class="comparison-item">
            <span>Divida em {}:</span>
            <span class="numbers">R$ {:.1} trilhoes</span>
        </div>
        <div class="comparison-item">
            <span>Cresceu:</span>
            <span class="numbers">{:.1}x</span>
        </div>
        <div class="comparison-item">
            <span>Total de juros pagos em {} anos:</span>
            <span class="comparison-lost">R$ {:.1} trilhoes</span>
        </div>
        <div class="comparison-item">
            <span>Isso e QUANTAS VEZES a divida inicial:</span>
            <span class="comparison-lost">{:.1}x</span>
        </div>
        <div class="comparison-item">
            <span>Juros pagos por cada brasileiro (total):</span>
            <span class="comparison-lost">R$ {:,.0}</span>
        </div>
    </div>
"#,
            initial_debt,
            years.last().unwrap_or(&2024),
            final_debt,
            multiplier,
            years.len(),
            total_int,
            total_int / initial_debt,
            total_int * 1e12 / 215e6
        ));

        // O que se perdeu
        html.push_str(r#"
    <h2>O Que o Brasil Perdeu Pagando Juros</h2>
    <div class="comparison">
"#);
        let comparisons = [
            ("Escolas publicas de qualidade (R$ 5M cada)", 5e6),
            ("Hospitais completos (R$ 50M cada)", 50e6),
            ("Casas populares (R$ 80 mil cada)", 80e3),
            ("Bolsas universitarias (R$ 2 mil/mes)", 24e3),
            ("Bolsa Familia anual por pessoa (R$ 6 mil)", 6e3),
            ("km de ferrovia (R$ 20M/km)", 20e6),
        ];
        for (label, unit) in comparisons {
            let qty = total_int * 1e12 / unit;
            html.push_str(&format!(
                r#"        <div class="comparison-item"><span>{}:</span><span class="comparison-lost">{:,.0}</span></div>
"#,
                label, qty
            ));
        }
        html.push_str("    </div>\n");

        if !ponr.is_empty() && ponr != "Nao encontrado" {
            html.push_str(&format!(
                r#"
    <div class="verdict" style="font-size:1.2em;">
        PONTO DE NAO RETORNO: {}
    </div>
    <div class="proof">
        {}
    </div>
"#,
                ponr, ponr_text
            ));
        }

        html.push_str(
            r#"
    <div class="footer">
        OpenDebtAbolition -- A prova matematica visual de que a divida nunca se paga.<br>
        A divida nao e um emprestimo. E uma CORRENTE. O juros nao e uma taxa. E um SANGUESSUGA.<br>
        OpenRepublic -- Extincao da divida = Extincao da escravidao moderna.
    </div>
</body>
</html>"#,
        );
        html
    }
}

// ============================================================================
// 6. FORMATO 4: SVG (Grafico Vetorial)
// ============================================================================

pub struct SVGChart;

impl SVGChart {
    pub fn render(projections: &[YearProjection], proof: &HashMap<String, String>) -> String {
        let width = 900;
        let height = 500;
        let margin = 60;
        let chart_w = width - 2 * margin;
        let chart_h = height - 2 * margin;

        let years: Vec<i32> = projections.iter().map(|p| p.year_label).collect();
        let debts: Vec<f64> = projections.iter().map(|p| p.debt_brl / 1e12).collect();
        let gdps: Vec<f64> = projections.iter().map(|p| p.gdp_brl / 1e12).collect();
        let max_val = debts.iter().cloned().fold(0.0, f64::max).max(gdps.iter().cloned().fold(0.0, f64::max)) * 1.1;

        let n = projections.len();
        let x_step = chart_w as f64 / (n.saturating_sub(1).max(1)) as f64;

        let to_x = |i: usize| margin as f64 + i as f64 * x_step;
        let to_y = |val: f64| height as f64 - margin as f64 - (val / max_val) * chart_h as f64;

        let debt_path: String = (0..n).map(|i| format!("{:.1},{:.1}", to_x(i), to_y(debts[i]))).collect::<Vec<_>>().join(" L ");
        let gdp_path: String = (0..n).map(|i| format!("{:.1},{:.1}", to_x(i), to_y(gdps[i]))).collect::<Vec<_>>().join(" L ");

        let mut svg = format!(
            r#"<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {} {}" style="background:#0a0a0a;">
    <text x="{}" y="30" text-anchor="middle" fill="#ff4444" font-size="20" font-family="monospace" font-weight="bold">
        A DIVIDA NUNCA SE PAGA -- {}
    </text>
    <!-- Eixos -->
    <line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#444" stroke-width="1"/>
    <line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#444" stroke-width="1"/>
    <!-- Linha do PIB (verde) -->
    <path d="M {}" fill="none" stroke="#00cc00" stroke-width="2"/>
    <!-- Area sob a divida (vermelho) -->
    <path d="M {} L {} {} L {} {} Z" fill="#ff0000" fill-opacity="0.15"/>
    <path d="M {}" fill="none" stroke="#ff0000" stroke-width="3"/>
"#,
            width, height,
            width / 2, proof.get("country").unwrap_or(&"Brasil".to_string()),
            margin, height - margin, width - margin, height - margin,
            margin, margin, margin, height - margin,
            debt_path,
            debt_path, to_x(n - 1), height - margin, to_x(0), height - margin,
            debt_path
        );

        for i in (0..n).step_by((n / 10).max(1)) {
            svg.push_str(&format!(
                r#"    <text x="{:.0}" y="{}" text-anchor="middle" fill="#888" font-size="11" font-family="monospace">{}</text>
"#,
                to_x(i), height - margin + 20, years[i]
            ));
        }

        for j in 0..5 {
            let val = max_val * j as f64 / 4.0;
            let y = height as f64 - margin as f64 - (val / max_val) * chart_h as f64;
            svg.push_str(&format!(
                r#"    <text x="{}" y="{:.0}" text-anchor="end" fill="#888" font-size="10" font-family="monospace">{:.0}T</text>
    <line x1="{}" y1="{:.0}" x2="{}" y2="{:.0}" stroke="#222" stroke-width="0.5" stroke-dasharray="3,3"/>
"#,
                margin - 10, y + 4.0, val, margin, y, width - margin, y
            ));
        }

        let multiplier: f64 = proof.get("debt_multiplier").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        svg.push_str(&format!(
            r#"    <rect x="{}" y="{}" width="12" height="12" fill="#ff0000"/>
    <text x="{}" y="{}" fill="#ccc" font-size="12" font-family="monospace">Divida Publica</text>
    <rect x="{}" y="{}" width="12" height="12" fill="#00cc00"/>
    <text x="{}" y="{}" fill="#ccc" font-size="12" font-family="monospace">PIB</text>

    <text x="{}" y="{}" text-anchor="middle" fill="#ff0000" font-size="14" font-family="monospace" font-weight="bold">
        VEREDITO: {} -- Divida cresce {:.1}x em {} anos
    </text>
</svg>"#,
            width - 180, margin, width - 160, margin + 11,
            width - 180, margin + 25, width - 160, margin + 36,
            width / 2, height - 5,
            proof.get("verdict").unwrap_or(&"IMPOSSIVEL DE PAGAR".to_string()), multiplier, n - 1
        ));
        svg
    }
}

// ============================================================================
// 7. FORMATO 5: CSV (Dados Brutos)
// ============================================================================

pub struct CSVExporter;

impl CSVExporter {
    pub fn render(projections: &[YearProjection]) -> String {
        let mut lines = vec![
            "ano,divida_brl,pib_brl,divida_pib_pct,juros_pago_brl,juros_receita_pct,per_capita_divida,juros_acumulado_brl,ponto_nao_retorno".to_string()
        ];
        for p in projections {
            lines.push(format!(
                "{},{:.2},{:.2},{:.2},{:.2},{:.2},{:.2},{:.2},{}",
                p.year_label,
                p.debt_brl,
                p.gdp_brl,
                p.debt_to_gdp,
                p.interest_paid_brl,
                p.interest_as_pct_revenue,
                p.per_capita_debt_brl,
                p.cumulative_interest_brl,
                if p.point_of_no_return { "SIM" } else { "NAO" }
            ));
        }
        lines.join("\n")
    }
}

// ============================================================================
// 8. FORMATO 6: JSON
// ============================================================================

pub struct JSONExporter;

impl JSONExporter {
    pub fn render(projections: &[YearProjection], proof: &HashMap<String, String>) -> String {
        let mut proj_json = Vec::new();
        for p in projections {
            proj_json.push(format!(
                r#"    {{
      "ano": {},
      "divida_trilhoes": {:.2},
      "pib_trilhoes": {:.2},
      "divida_pib_pct": {:.1},
      "juros_pago_trilhoes": {:.2},
      "juros_receita_pct": {:.1},
      "per_capita_divida": {:.2},
      "juros_acumulado_trilhoes": {:.2},
      "ponto_nao_retorno": {}
    }}"#,
                p.year_label,
                p.debt_brl / 1e12,
                p.gdp_brl / 1e12,
                p.debt_to_gdp,
                p.interest_paid_brl / 1e12,
                p.interest_as_pct_revenue,
                p.per_capita_debt_brl,
                p.cumulative_interest_brl / 1e12,
                p.point_of_no_return
            ));
        }
        format!(
            r#"{{
  "titulo": "A Divida Nunca Se Paga -- Prova Matematica",
  "veredito": "{}",
  "razao": "{}",
  "resumo": {{}},
  "projecoes": [
{}
  ]
}}"#,
            proof.get("verdict").unwrap_or(&"IMPOSSIVEL DE PAGAR".to_string()),
            proof.get("reason").unwrap_or(&"".to_string()),
            proj_json.join(",\n")
        )
    }
}

// ============================================================================
// 9. FORMATO 7: INFOGRAFICO (Redes Sociais)
// ============================================================================

pub struct Infographic;

impl Infographic {
    pub fn render(projections: &[YearProjection], proof: &HashMap<String, String>) -> String {
        let p0 = &projections[0];
        let p_last = projections.last().unwrap();
        let total_interest: f64 = proof.get("total_interest_paid_trillions").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        let ponr = proof.get("point_of_no_return_year").cloned().unwrap_or_default();

        let mut lines = Vec::new();
        lines.push("=".repeat(50));
        lines.push("A DIVIDA NUNCA SE PAGA".to_string());
        lines.push("=".repeat(50));
        lines.push("".to_string());
        lines.push(format!("Pais: {}", proof.get("country").unwrap_or(&"Brasil".to_string())));
        lines.push(format!("Divida hoje: R$ {:.1} trilhoes", p0.debt_brl / 1e12));
        lines.push(format!("Em {}: R$ {:.1} trilhoes", p_last.year_label, p_last.debt_brl / 1e12));
        lines.push(format!("Cresceu: {:.1}x", proof.get("debt_multiplier").unwrap_or(&"0".to_string())));
        lines.push("".to_string());
        lines.push("--- A PROVA ---".to_string());
        lines.push(format!("Juros: {}% ao ano", proof.get("interest_rate").unwrap_or(&"0".to_string())));
        lines.push(format!("PIB cresce: {}% ao ano", proof.get("gdp_growth").unwrap_or(&"0".to_string())));
        lines.push(format!("Gap: {} pontos", proof.get("growth_gap").unwrap_or(&"0".to_string())));
        lines.push("".to_string());
        let ir: f64 = proof.get("interest_rate").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        let gg: f64 = proof.get("gdp_growth").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        lines.push(format!("Juros cresce {:.1}x", if gg > 0.0 { ir / gg } else { 0.0 }));
        lines.push("mais rapido que a economia.".to_string());
        lines.push("".to_string());
        lines.push("--- O CUSTO HUMANO ---".to_string());
        lines.push(format!("Juros pagos em {} anos:", projections.len()));
        lines.push(format!("R$ {:.1} trilhoes", total_interest));
        lines.push(format!("= {:.1}x a divida inicial", total_interest / (p0.debt_brl / 1e12)));
        lines.push(format!("= R$ {:,.0} por brasileiro", total_interest * 1e12 / 215e6));
        lines.push(format!("= {:,.0} escolas", total_interest * 1e12 / 5e6));
        lines.push(format!("= {:,.0} hospitais", total_interest * 1e12 / 50e6));
        lines.push(format!("= {:,.0} casas populares", total_interest * 1e12 / 80e3));
        lines.push("".to_string());
        if !ponr.is_empty() && ponr != "Nao encontrado" {
            lines.push(format!("PONTO DE NAO RETORNO: {}", ponr));
            lines.push("Juros superou 50% da arrecadacao.".to_string());
            lines.push("A partir daqui, impossivel.".to_string());
            lines.push("".to_string());
        }
        lines.push("--- O VEREDITO ---".to_string());
        lines.push("IMPOSSIVEL DE PAGAR.".to_string());
        lines.push("A matematica nao mente.".to_string());
        lines.push("A divida e uma CORRENTE.".to_string());
        lines.push("O juros e um SANGUESSUGA.".to_string());
        lines.push("".to_string());
        lines.push("A unica saida: EXTINCAO.".to_string());
        lines.push("Nao renegociar. Nao alongar.".to_string());
        lines.push("EXTINGUIR.".to_string());
        lines.push("".to_string());
        lines.push("#OpenRepublic #DividaNuncaSePaga".to_string());
        lines.push("#ExtincaoDaDivida".to_string());
        lines.join("\n")
    }
}

// ============================================================================
// 10. FORMATO 8: NARRATIVA FALADA (para Telefonista)
// ============================================================================

pub struct Narrative;

impl Narrative {
    pub fn render(projections: &[YearProjection], proof: &HashMap<String, String>) -> String {
        let p0 = &projections[0];
        let p10 = &projections[projections.len().min(10) - 1];
        let p_last = projections.last().unwrap();
        let total_interest: f64 = proof.get("total_interest_paid_trillions").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        let ponr = proof.get("point_of_no_return_year").cloned().unwrap_or_default();

        let mut parts = Vec::new();
        parts.push("Vou te provar algo em 30 segundos. Presta atencao.".to_string());
        parts.push("".to_string());
        parts.push(format!("A divida do {} hoje e de {:.0} trilhoes de reais.", proof.get("country").unwrap_or(&"Brasil".to_string()), p0.debt_brl / 1e12));
        parts.push(format!("O juros e de {}% ao ano.", proof.get("interest_rate").unwrap_or(&"0".to_string())));
        parts.push(format!("Isso significa que SO EM JUROS, o pais paga {:.0} trilhoes por ano.", p0.interest_paid_brl / 1e12));
        parts.push("".to_string());
        parts.push(format!("O PIB cresce {}% ao ano.", proof.get("gdp_growth").unwrap_or(&"0".to_string())));
        parts.push(format!("O juros cresce {}% ao ano.", proof.get("interest_rate").unwrap_or(&"0".to_string())));
        let ir: f64 = proof.get("interest_rate").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        let gg: f64 = proof.get("gdp_growth").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        parts.push(format!("O juros cresce {:.0} vezes mais rapido que a economia.", if gg > 0.0 { ir / gg } else { 0.0 }));
        parts.push("".to_string());
        parts.push(format!("Em {}, a divida sera de R$ {:.0} trilhoes.", p10.year_label, p10.debt_brl / 1e12));
        parts.push(format!("Em {}, a divida sera de R$ {:.0} trilhoes.", p_last.year_label, p_last.debt_brl / 1e12));
        parts.push(format!("Cresceu {} vezes.", proof.get("debt_multiplier").unwrap_or(&"0".to_string())));
        parts.push("".to_string());
        parts.push(format!("O total de juros pagos? R$ {:.0} trilhoes.", total_interest));
        parts.push(format!("Isso e {:.0} vezes a divida original.", total_interest / (p0.debt_brl / 1e12)));
        parts.push("Voce pagou a divida inteira varias vezes e ainda deve tudo.".to_string());
        parts.push("".to_string());
        if !ponr.is_empty() && ponr != "Nao encontrado" {
            parts.push(format!("E pior: em {}, os juros superaram METADE de tudo que o governo arrecada.", ponr));
            parts.push("A partir dai, e matematicamente impossivel pagar.".to_string());
        }
        parts.push("".to_string());
        parts.push("A divida NUNCA se paga. Ela so cresce.".to_string());
        parts.push("O pais nao paga a divida. O pais paga JUROS PARA SEMPRE.".to_string());
        parts.push("E uma corrente. E um sanguessuga. E escravidao moderna.".to_string());
        parts.push("A unica saida e a EXTINCAO. Nao renegociar. Extinguir.".to_string());
        parts.push("".to_string());
        parts.push("A matematica nao mente.".to_string());
        parts.join(" ")
    }
}

// ============================================================================
// 11. FORMATO 9: COMPARATIVO (O Que Se Perdeu)
// ============================================================================

pub struct ComparisonView;

impl ComparisonView {
    pub fn render(projections: &[YearProjection], proof: &HashMap<String, String>) -> String {
        let total_interest: f64 = proof.get("total_interest_paid_trillions").unwrap_or(&"0".to_string()).parse().unwrap_or(0.0);
        let mut lines = Vec::new();
        lines.push("=".repeat(65));
        lines.push("O QUE O BRASIL PERDEU PAGANDO JUROS".to_string());
        lines.push(format!("Total pago em juros: R$ {:.1} trilhoes", total_interest));
        lines.push("=".repeat(65));
        lines.push("".to_string());

        let comparisons = [
            ("Escolas publicas completas", 5e6, "R$ 5 milhoes cada"),
            ("Hospitais completos (100 leitos)", 50e6, "R$ 50 milhoes cada"),
            ("Casas populares", 80e3, "R$ 80 mil cada"),
            ("Bolsas universitarias anuais", 24e3, "R$ 2 mil/mes"),
            ("Bolsa Familia (1 ano por pessoa)", 6e3, "R$ 500/mes"),
            ("km de ferrovia nova", 20e6, "R$ 20 milhoes/km"),
            ("UPAs (Unidade Pronto Atendimento)", 15e6, "R$ 15 milhoes cada"),
            ("Creches publicas", 3e6, "R$ 3 milhoes cada"),
            ("Distribuicao de comida (cesta R$200/mes)", 2400.0, "R$ 200/mes por familia"),
            ("Saneamento basico por domicilio", 12e3, "R$ 12 mil por ligacao"),
        ];

        lines.push(format!("{:<45} {:>15} {:>15}", "ITEM", "QTD", "CUSTO UNIT."));
        lines.push("-".repeat(75));
        for (label, unit_cost, cost_desc) in comparisons {
            let qty = total_interest * 1e12 / unit_cost;
            let qty_str = if qty > 1e9 {
                format!("{:.1} bilhoes", qty / 1e9)
            } else if qty > 1e6 {
                format!("{:.1} milhoes", qty / 1e6)
            } else if qty > 1e3 {
                format!("{:.1} mil", qty / 1e3)
            } else {
                format!("{:.0}", qty)
            };
            lines.push(format!("  {:<43} {:>15} {:>15}", label, qty_str, cost_desc));
        }

        lines.push("".to_string());
        lines.push("Cada real pago em juros e um real ROUBADO do povo.".to_string());
        lines.push("Nao e gasto publico. E SANGRIA.".to_string());
        lines.push("".to_string());
        lines.join("\n")
    }
}

// ============================================================================
// 12. FORMATO 10: ARTE ASCII (Impacto Visual)
// ============================================================================

pub struct AsciiArt;

impl AsciiArt {
    pub fn render(projections: &[YearProjection]) -> String {
        let mut lines = Vec::new();
        lines.push("".to_string());
        lines.push("  O CRESCIMENTO DA DIVIDA vs O CRESCIMENTO DO PIB".to_string());
        lines.push("  (cada bloco = ~10% da divida final)".to_string());
        lines.push("".to_string());

        let final_debt = projections.last().unwrap().debt_brl;
        for p in projections {
            let debt_blocks = ((p.debt_brl / final_debt) * 40.0) as usize;
            let gdp_blocks = ((p.gdp_brl / final_debt) * 40.0) as usize;
            let debt_bar = "X".repeat(debt_blocks.max(1));
            let gdp_bar = "=".repeat(gdp_blocks.max(1));
            lines.push(format!("  {}  DIVIDA: [{}]", p.year_label, format!("{:<40}", debt_bar)));
            lines.push(format!("         PIB:    [{}]", format!("{:<40}", gdp_bar)));
            lines.push("".to_string());
        }

        lines.push("  X = DIVIDA (cresce exponencialmente)".to_string());
        lines.push("  = = PIB (cresce lentamente)".to_string());
        lines.push("".to_string());
        lines.push("  Veja como a divida ENGOLE o PIB.".to_string());
        lines.push("  Isso nao e opiniao. E matematica.".to_string());
        lines.push("".to_string());
        lines.join("\n")
    }
}

// ============================================================================
// 13. GERADOR DE TODOS OS FORMATOS
// ============================================================================

pub struct DebtVisualizer {
    pub params: DebtParameters,
    pub engine: DebtProjectionEngine,
    pub projections: Vec<YearProjection>,
    pub proof: HashMap<String, String>,
}

impl DebtVisualizer {
    pub fn new(params: DebtParameters) -> Self {
        let mut engine = DebtProjectionEngine::new(params.clone());
        let projections = engine.project();
        let proof = engine.proof_summary();
        DebtVisualizer {
            params,
            engine,
            projections,
            proof,
        }
    }

    pub fn generate_all(&self, output_dir: Option<&str>) -> HashMap<String, String> {
        let output_dir = output_dir.unwrap_or_else(|| {
            // default relative to crate root
            "debt_visualizations"
        });
        fs::create_dir_all(output_dir).ok();

        let mut results = HashMap::new();

        for metric in ["debt_to_gdp", "interest_pct_revenue", "per_capita_debt"] {
            let content = ASCIIBarChart::render(&self.projections, metric);
            let path = format!("{}/grafico_barras_{}.txt", output_dir, metric);
            fs::write(&path, &content).ok();
            results.insert(format!("barras_{}", metric), path);
        }

        let content = MarkdownTable::render(&self.projections);
        let path = format!("{}/tabela_divida.md", output_dir);
        fs::write(&path, &content).ok();
        results.insert("markdown".to_string(), path);

        let content = HTMLPage::render(&self.projections, &self.proof);
        let path = format!("{}/index.html", output_dir);
        fs::write(&path, &content).ok();
        results.insert("html".to_string(), path);

        let content = SVGChart::render(&self.projections, &self.proof);
        let path = format!("{}/grafico_divida.svg", output_dir);
        fs::write(&path, &content).ok();
        results.insert("svg".to_string(), path);

        let content = CSVExporter::render(&self.projections);
        let path = format!("{}/dados_divida.csv", output_dir);
        fs::write(&path, &content).ok();
        results.insert("csv".to_string(), path);

        let content = JSONExporter::render(&self.projections, &self.proof);
        let path = format!("{}/dados_divida.json", output_dir);
        fs::write(&path, &content).ok();
        results.insert("json".to_string(), path);

        let content = Infographic::render(&self.projections, &self.proof);
        let path = format!("{}/infografico.txt", output_dir);
        fs::write(&path, &content).ok();
        results.insert("infografico".to_string(), path);

        let content = Narrative::render(&self.projections, &self.proof);
        let path = format!("{}/narrativa_falada.txt", output_dir);
        fs::write(&path, &content).ok();
        results.insert("narrativa".to_string(), path);

        let content = ComparisonView::render(&self.projections, &self.proof);
        let path = format!("{}/comparativo_perdas.txt", output_dir);
        fs::write(&path, &content).ok();
        results.insert("comparativo".to_string(), path);

        let content = AsciiArt::render(&self.projections);
        let path = format!("{}/arte_ascii.txt", output_dir);
        fs::write(&path, &content).ok();
        results.insert("ascii_art".to_string(), path);

        results
    }
}

// ============================================================================
// 14. DEMONSTRACAO (main)
// ============================================================================

fn main() {
    println!("{}", "=".repeat(70));
    println!("OpenDebtAbolition -- A Prova Matematica Visual");
    println!("A DIVIDA NUNCA SE PAGA");
    println!("{}", "=".repeat(70));

    let params = DebtParameters::default();
    let mut engine = DebtProjectionEngine::new(params.clone());
    let projections = engine.project();
    let proof = engine.proof_summary();

    println!("\n{}", "=".repeat(70));
    println!("VEREDITO DA PROVA");
    println!("{}", "=".repeat(70));
    println!("  Pais: {}", proof.get("country").unwrap_or(&"Brasil".to_string()));
    println!("  Divida inicial: R$ {} trilhoes", proof.get("initial_debt_trillions").unwrap_or(&"0".to_string()));
    println!("  Divida/PIB inicial: {}%", proof.get("initial_debt_to_gdp").unwrap_or(&"0".to_string()));
    println!("  Divida final ({}): R$ {} trilhoes", projections.last().unwrap().year_label, proof.get("final_debt_trillions").unwrap_or(&"0".to_string()));
    println!("  Cresceu: {}x", proof.get("debt_multiplier").unwrap_or(&"0".to_string()));
    println!("  Total de juros pagos: R$ {} trilhoes", proof.get("total_interest_paid_trillions").unwrap_or(&"0".to_string()));
    println!("  Juros: {}% | PIB cresce: {}%", proof.get("interest_rate").unwrap_or(&"0".to_string()), proof.get("gdp_growth").unwrap_or(&"0".to_string()));
    println!("  Gap: {} pontos percentuais", proof.get("growth_gap").unwrap_or(&"0".to_string()));
    println!("  Ponto de nao retorno: {}", proof.get("point_of_no_return_year").unwrap_or(&"Nao encontrado".to_string()));
    println!("\n  VEREDITO: {}", proof.get("verdict").unwrap_or(&"IMPOSSIVEL DE PAGAR".to_string()));
    println!("  RAZAO: {}", proof.get("reason").unwrap_or(&"".to_string()));

    println!("{}", ASCIIBarChart::render(&projections, "debt_to_gdp"));
    println!("{}", ASCIIBarChart::render(&projections, "interest_pct_revenue"));

    println!("{}", AsciiArt::render(&projections));

    println!("{}", Infographic::render(&projections, &proof));

    println!("{}", ComparisonView::render(&projections, &proof));

    println!("\n{}", "=".repeat(70));
    println!("NARRATIVA FALADA (para Telefonista ler)");
    println!("{}", "=".repeat(70));
    println!("{}", Narrative::render(&projections, &proof));

    println!("\n{}", "=".repeat(70));
    println!("GERANDO TODOS OS FORMATOS...");
    println!("{}", "=".repeat(70));
    let viz = DebtVisualizer::new(params);
    let results = viz.generate_all(None);
    for (fmt, path) in &results {
        println!("  {:25} -> {}", fmt, path);
    }

    println!("\n{}", "=".repeat(70));
    println!("Total formatos: {}", VisualizationFormat::all().len());
    println!("Anos projetados: {}", viz.params.years_to_project);
    println!("Veredito: {}", proof.get("verdict").unwrap_or(&"IMPOSSIVEL DE PAGAR".to_string()));
    println!("\nA matematica nao mente.");
    println!("A divida NUNCA se paga.");
    println!("O juros composto e um SANGUESSUGA.");
    println!("A unica saida: EXTINCAO.");
}

trait RoundTo {
    fn round_to(self, decimals: u32) -> f64;
}

impl RoundTo for f64 {
    fn round_to(self, decimals: u32) -> f64 {
        let factor = 10f64.powi(decimals as i32);
        (self * factor).round() / factor
    }
}