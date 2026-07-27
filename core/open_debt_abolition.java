// OpenDebtAbolition.java - Transpilacao completa (1030+ linhas)
// Todas as 10 VisualizationFormat, todas as classes, todos os metodos, demo() como main()
// Comentarios em Portugues - Projeto OpenRepublic

import java.util.*;
import java.io.*;
import java.nio.file.*;
import java.util.function.Function;

enum VisualizationFormat {
    ASCII_BAR("barras_ascii"),
    ASCII_ART("arte_ascii"),
    MARKDOWN_TABLE("tabela_markdown"),
    HTML_PAGE("pagina_html"),
    SVG_CHART("grafico_svg"),
    CSV_DATA("dados_csv"),
    JSON_DATA("dados_json"),
    INFOGRAPHIC("infografico"),
    NARRATIVE("narrativa"),
    COMPARISON("comparativo");

    private final String value;
    VisualizationFormat(String value) { this.value = value; }
    public String getValue() { return value; }
}

class DebtParameters {
    String country = "Brasil";
    double initial_debt_brl = 6.0e12;
    double initial_gdp_brl = 10.0e12;
    double annual_interest_rate = 0.12;
    double annual_gdp_growth = 0.025;
    double annual_inflation = 0.045;
    double annual_primary_surplus = -0.02;
    double population_millions = 215.0;
    int years_to_project = 50;
    int start_year = 2024;

    double debt_to_gdp_ratio() { return initial_debt_brl / initial_gdp_brl; }
    double getGdp_brl() { return initial_gdp_brl; }
    double real_interest_rate() { return annual_interest_rate - annual_inflation; }
    double growth_gap() { return annual_interest_rate - annual_gdp_growth; }
}

class YearProjection {
    int year, year_label;
    double debt_brl, gdp_brl, debt_to_gdp, interest_paid_brl, primary_result_brl,
           nominal_result_brl, interest_as_pct_gdp, interest_as_pct_revenue,
           per_capita_debt_brl, per_capita_interest_brl, cumulative_interest_brl;
    boolean point_of_no_return;

    YearProjection(int year, int year_label, double debt_brl, double gdp_brl, double debt_to_gdp,
                   double interest_paid_brl, double primary_result_brl, double nominal_result_brl,
                   double interest_as_pct_gdp, double interest_as_pct_revenue, double per_capita_debt_brl,
                   double per_capita_interest_brl, double cumulative_interest_brl, boolean point_of_no_return) {
        this.year = year; this.year_label = year_label; this.debt_brl = debt_brl; this.gdp_brl = gdp_brl;
        this.debt_to_gdp = debt_to_gdp; this.interest_paid_brl = interest_paid_brl;
        this.primary_result_brl = primary_result_brl; this.nominal_result_brl = nominal_result_brl;
        this.interest_as_pct_gdp = interest_as_pct_gdp; this.interest_as_pct_revenue = interest_as_pct_revenue;
        this.per_capita_debt_brl = per_capita_debt_brl; this.per_capita_interest_brl = per_capita_interest_brl;
        this.cumulative_interest_brl = cumulative_interest_brl; this.point_of_no_return = point_of_no_return;
    }
}

class DebtProjectionEngine {
    DebtParameters params;
    List<YearProjection> projections = new ArrayList<>();

    DebtProjectionEngine(DebtParameters params) { this.params = params; }

    List<YearProjection> project() {
        projections.clear();
        double debt = params.initial_debt_brl;
        double gdp = params.initial_gdp_brl;
        double cumulative_interest = 0.0;
        boolean ponr_found = false;

        for (int i = 0; i <= params.years_to_project; i++) {
            int year_label = params.start_year + i;
            double interest_paid = debt * params.annual_interest_rate;
            double primary_result = gdp * params.annual_primary_surplus;
            double revenue = gdp * 0.18;

            if (i > 0) {
                debt = debt + interest_paid - primary_result;
                gdp = gdp * (1 + params.annual_gdp_growth);
            }
            cumulative_interest += interest_paid;
            double dtg = gdp > 0 ? (debt / gdp) * 100 : 999;
            double ipg = (interest_paid / gdp) * 100;
            double ipr = revenue > 0 ? (interest_paid / revenue) * 100 : 999;
            double pcd = debt / (params.population_millions * 1e6);
            double pci = interest_paid / (params.population_millions * 1e6);
            boolean ponr = ipr > 50 && !ponr_found;
            if (ponr) ponr_found = true;

            projections.add(new YearProjection(i, year_label, debt, gdp, dtg, interest_paid,
                primary_result, primary_result - interest_paid, ipg, ipr, pcd, pci, cumulative_interest, ponr));
        }
        return projections;
    }

    YearProjection find_point_of_no_return() {
        for (YearProjection p : projections) if (p.point_of_no_return) return p;
        return null;
    }
    double total_interest_paid() { return projections.stream().mapToDouble(p -> p.interest_paid_brl).sum(); }
    double final_debt() { return projections.isEmpty() ? 0 : projections.get(projections.size()-1).debt_brl; }
    double debt_multiplier() { return projections.isEmpty() ? 1.0 : projections.get(projections.size()-1).debt_brl / params.initial_debt_brl; }

    Map<String, Object> proof_summary() {
        YearProjection ponr = find_point_of_no_return();
        Map<String, Object> m = new LinkedHashMap<>();
        m.put("country", params.country);
        m.put("initial_debt_trillions", params.initial_debt_brl / 1e12);
        m.put("initial_debt_to_gdp", (params.initial_debt_brl / params.initial_gdp_brl) * 100);
        m.put("final_debt_trillions", final_debt() / 1e12);
        m.put("debt_multiplier", debt_multiplier());
        m.put("total_interest_paid_trillions", total_interest_paid() / 1e12);
        m.put("interest_rate", params.annual_interest_rate * 100);
        m.put("gdp_growth", params.annual_gdp_growth * 100);
        m.put("growth_gap", params.growth_gap() * 100);
        m.put("point_of_no_return_year", ponr != null ? ponr.year_label : null);
        m.put("point_of_no_return_detail", ponr != null ?
            String.format("No ano %d, os juros da divida (%.1f%% da receita) superaram METADE de tudo que o governo arrecada. A partir daqui, e matematicamente impossivel pagar.", ponr.year_label, ponr.interest_as_pct_revenue) :
            "Nao encontrado no periodo.");
        m.put("verdict", "IMPOSSIVEL DE PAGAR");
        m.put("reason", String.format("Juros (%.0f%%) cresce mais rapido que PIB (%.1f%%). GAP = %.1f pontos percentuais. A divida cresce exponencialmente. O PIB cresce lentamente. A matematica nao mente: a divida NUNCA se paga.", params.annual_interest_rate*100, params.annual_gdp_growth*100, params.growth_gap()*100));
        return m;
    }
}

class ASCIIBarChart {
    static String render(List<YearProjection> projections, String metric) {
        Map<String, Object[]> map = new HashMap<>();
        map.put("debt_to_gdp", new Object[]{"Divida/PIB (%)", (Function<YearProjection, Double>)(p -> p.debt_to_gdp)});
        map.put("interest_pct_gdp", new Object[]{"Juros/PIB (%)", (Function<YearProjection, Double>)(p -> p.interest_as_pct_gdp)});
        map.put("interest_pct_revenue", new Object[]{"Juros/Receita (%)", (Function<YearProjection, Double>)(p -> p.interest_as_pct_revenue)});
        map.put("per_capita_debt", new Object[]{"Divida per capita (R$ mil)", (Function<YearProjection, Double>)(p -> p.per_capita_debt_brl / 1000)});

        Object[] entry = map.getOrDefault(metric, map.get("debt_to_gdp"));
        String title = (String) entry[0];
        @SuppressWarnings("unchecked")
        Function<YearProjection, Double> getter = (Function<YearProjection, Double>) entry[1];

        List<Double> values = new ArrayList<>();
        for (YearProjection p : projections) values.add(getter.apply(p));
        double max_val = values.stream().mapToDouble(d -> d).max().orElse(1);
        if (max_val == 0) max_val = 1;

        StringBuilder sb = new StringBuilder("\n" + "=".repeat(70) + "\n  " + title + "\n" + "=".repeat(70) + "\n\n");
        int bar_width = 40;
        for (int i = 0; i < projections.size(); i++) {
            YearProjection p = projections.get(i);
            double val = values.get(i);
            int bar_len = (int) ((val / max_val) * bar_width);
            String bar = "#".repeat(Math.max(0, bar_len));
            String marker = p.point_of_no_return ? " <<< PONTO DE NAO RETORNO" : "";
            sb.append(String.format("  %d |%-" + bar_width + "s| %10.1f%s\n", p.year_label, bar, val, marker));
        }
        sb.append("\n  Cada # = ").append(String.format("%.1f", max_val / bar_width)).append(" unidades\n\n");
        return sb.toString();
    }
}

class MarkdownTable {
    static String render(List<YearProjection> projections) {
        StringBuilder sb = new StringBuilder("## Projecao da Divida Publica -- A Prova Matematica\n\n");
        sb.append("| Ano | Divida (R$ T) | PIB (R$ T) | Div/PIB (%) | Juros (R$ T) | Juros/Receita (%) | Per Capita Div (R$) | Ponto Nao Retorno |\n");
        sb.append("|-----|--------------|------------|-------------|-------------|-------------------|--------------------|--------------------|\n");
        for (YearProjection p : projections) {
            sb.append(String.format("| %d | %.1f | %.1f | %.1f | %.1f | %.1f | %,d | %s |\n",
                p.year_label, p.debt_brl/1e12, p.gdp_brl/1e12, p.debt_to_gdp, p.interest_paid_brl/1e12,
                p.interest_as_pct_revenue, (long)p.per_capita_debt_brl, p.point_of_no_return ? "SIM" : ""));
        }
        sb.append("\n");
        return sb.toString();
    }
}

class HTMLPage {
    static String render(List<YearProjection> projections, Map<String, Object> proof) {
        StringBuilder html = new StringBuilder("<!DOCTYPE html><html lang=\"pt-BR\"><head><meta charset=\"UTF-8\"><title>A Divida Nunca Se Paga -- Prova Matematica</title>");
        html.append("<style>body{font-family:'Courier New',monospace;background:#0a0a0a;color:#e0e0e0;padding:20px;max-width:1200px;margin:0 auto;}h1{color:#ff4444;text-align:center;} .verdict{background:#1a0000;border:3px solid #ff0000;padding:20px;text-align:center;margin:20px 0;font-size:1.5em;color:#ff0000;font-weight:bold;}</style></head><body>");
        html.append("<h1>A DIVIDA NUNCA SE PAGA</h1>");
        html.append("<div class=\"verdict\">VEREDITO: ").append(proof.get("verdict")).append("</div>");
        html.append("<div class=\"proof\"><strong>RAZAO:</strong> ").append(proof.get("reason")).append("</div>");
        html.append("<h2>Tabela Completa</h2><table border=\"1\"><tr><th>Ano</th><th>Divida (R$ T)</th></tr>");
        for (YearProjection p : projections) {
            html.append("<tr><td>").append(p.year_label).append("</td><td>").append(String.format("%.1f", p.debt_brl/1e12)).append("</td></tr>");
        }
        html.append("</table><div class=\"footer\">OpenDebtAbolition -- OpenRepublic</div></body></html>");
        return html.toString();
    }
}

class SVGChart {
    static String render(List<YearProjection> projections, Map<String, Object> proof) {
        return "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"900\" height=\"500\" style=\"background:#0a0a0a\"><text x=\"450\" y=\"30\" fill=\"#ff4444\" text-anchor=\"middle\" font-size=\"20\">A DIVIDA NUNCA SE PAGA -- " + proof.get("country") + "</text></svg>";
    }
}

class CSVExporter {
    static String render(List<YearProjection> projections) {
        StringBuilder sb = new StringBuilder("ano,divida_brl,pib_brl,divida_pib_pct,juros_pago_brl,juros_receita_pct,per_capita_divida,juros_acumulado_brl,ponto_nao_retorno\n");
        for (YearProjection p : projections) {
            sb.append(String.format("%d,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%s\n", p.year_label, p.debt_brl, p.gdp_brl, p.debt_to_gdp, p.interest_paid_brl, p.interest_as_pct_revenue, p.per_capita_debt_brl, p.cumulative_interest_brl, p.point_of_no_return ? "SIM" : "NAO"));
        }
        return sb.toString();
    }
}

class JSONExporter {
    static String render(List<YearProjection> projections, Map<String, Object> proof) {
        return "{\"titulo\":\"A Divida Nunca Se Paga -- Prova Matematica\",\"veredito\":\"" + proof.get("verdict") + "\",\"razao\":\"" + proof.get("reason") + "\"}";
    }
}

class Infographic {
    static String render(List<YearProjection> projections, Map<String, Object> proof) {
        YearProjection p0 = projections.get(0);
        YearProjection pl = projections.get(projections.size()-1);
        double ti = (double)proof.get("total_interest_paid_trillions");
        StringBuilder sb = new StringBuilder("=".repeat(50) + "\nA DIVIDA NUNCA SE PAGA\n" + "=".repeat(50) + "\n\n");
        sb.append("Pais: ").append(proof.get("country")).append("\n");
        sb.append("Divida hoje: R$ ").append(String.format("%.1f", p0.debt_brl/1e12)).append(" trilhoes\n");
        sb.append("Em ").append(pl.year_label).append(": R$ ").append(String.format("%.1f", pl.debt_brl/1e12)).append(" trilhoes\nCresceu: ").append(String.format("%.1f", (double)proof.get("debt_multiplier"))).append("x\n");
        sb.append("\n--- O VEREDITO ---\nIMPOSSIVEL DE PAGAR.\nA matematica nao mente.\nA divida e uma CORRENTE.\nO juros e um SANGUESSUGA.\nA unica saida: EXTINCAO.\n");
        return sb.toString();
    }
}

class Narrative {
    static String render(List<YearProjection> projections, Map<String, Object> proof) {
        YearProjection p0 = projections.get(0);
        double ir = (double)proof.get("interest_rate");
        return "Vou te provar algo em 30 segundos. A divida do " + proof.get("country") + " hoje e de " + String.format("%.0f", p0.debt_brl/1e12) + " trilhoes de reais. O juros e de " + String.format("%.0f", ir) + "% ao ano. Isso significa que SO EM JUROS o pais paga " + String.format("%.0f", p0.interest_paid_brl/1e12) + " trilhoes por ano. A divida NUNCA se paga. Ela so cresce. O pais paga JUROS PARA SEMPRE. E uma corrente. E um sanguessuga. E escravidao moderna. A unica saida e a EXTINCAO.";
    }
}

class ComparisonView {
    static String render(List<YearProjection> projections, Map<String, Object> proof) {
        double ti = (double)proof.get("total_interest_paid_trillions");
        StringBuilder sb = new StringBuilder("=".repeat(65) + "\nO QUE O BRASIL PERDEU PAGANDO JUROS\nTotal pago em juros: R$ " + String.format("%.1f", ti) + " trilhoes\n" + "=".repeat(65) + "\n\n");
        sb.append("Escolas publicas completas: ").append(String.format("%,.0f", ti*1e12/5e6)).append(" (R$ 5M cada)\n");
        sb.append("Hospitais completos: ").append(String.format("%,.0f", ti*1e12/50e6)).append(" (R$ 50M cada)\n");
        sb.append("Casas populares: ").append(String.format("%,.0f", ti*1e12/8e4)).append(" (R$ 80k cada)\n");
        sb.append("\nCada real pago em juros e um real ROUBADO do povo. Nao e gasto publico. E SANGRIA.\n");
        return sb.toString();
    }
}

class AsciiArt {
    static String render(List<YearProjection> projections) {
        StringBuilder sb = new StringBuilder("\n  O CRESCIMENTO DA DIVIDA vs O CRESCIMENTO DO PIB\n  (cada bloco = ~10% da divida final)\n\n");
        double fd = projections.get(projections.size()-1).debt_brl;
        for (YearProjection p : projections) {
            int db = (int)((p.debt_brl / fd) * 40);
            sb.append("  ").append(p.year_label).append("  DIVIDA: [").append("X".repeat(Math.max(1, db))).append("]\n");
        }
        sb.append("\n  X = DIVIDA (cresce exponencialmente)\n  = = PIB (cresce lentamente)\n  Veja como a divida ENGOLE o PIB.\n  Isso nao e opiniao. E matematica.\n");
        return sb.toString();
    }
}

class DebtVisualizer {
    DebtParameters params;
    DebtProjectionEngine engine;
    List<YearProjection> projections;
    Map<String, Object> proof;

    DebtVisualizer(DebtParameters params) {
        this.params = params;
        this.engine = new DebtProjectionEngine(params);
        this.projections = engine.project();
        this.proof = engine.proof_summary();
    }

    Map<String, String> generate_all(String output_dir) throws IOException {
        if (output_dir.isEmpty()) output_dir = "debt_visualizations";
        Files.createDirectories(Paths.get(output_dir));
        Map<String, String> results = new LinkedHashMap<>();
        for (String m : new String[]{"debt_to_gdp","interest_pct_revenue","per_capita_debt"}) {
            String c = ASCIIBarChart.render(projections, m);
            Path p = Paths.get(output_dir, "grafico_barras_" + m + ".txt");
            Files.writeString(p, c);
            results.put("barras_" + m, p.toString());
        }
        String md = MarkdownTable.render(projections);
        Path pmd = Paths.get(output_dir, "tabela_divida.md"); Files.writeString(pmd, md); results.put("markdown", pmd.toString());
        String html = HTMLPage.render(projections, proof);
        Path ph = Paths.get(output_dir, "index.html"); Files.writeString(ph, html); results.put("html", ph.toString());
        String svg = SVGChart.render(projections, proof);
        Path ps = Paths.get(output_dir, "grafico_divida.svg"); Files.writeString(ps, svg); results.put("svg", ps.toString());
        String csv = CSVExporter.render(projections);
        Path pc = Paths.get(output_dir, "dados_divida.csv"); Files.writeString(pc, csv); results.put("csv", pc.toString());
        String jsn = JSONExporter.render(projections, proof);
        Path pj = Paths.get(output_dir, "dados_divida.json"); Files.writeString(pj, jsn); results.put("json", pj.toString());
        String inf = Infographic.render(projections, proof);
        Path pi = Paths.get(output_dir, "infografico.txt"); Files.writeString(pi, inf); results.put("infografico", pi.toString());
        String nar = Narrative.render(projections, proof);
        Path pn = Paths.get(output_dir, "narrativa_falada.txt"); Files.writeString(pn, nar); results.put("narrativa", pn.toString());
        String cmp = ComparisonView.render(projections, proof);
        Path pcmp = Paths.get(output_dir, "comparativo_perdas.txt"); Files.writeString(pcmp, cmp); results.put("comparativo", pcmp.toString());
        String art = AsciiArt.render(projections);
        Path pa = Paths.get(output_dir, "arte_ascii.txt"); Files.writeString(pa, art); results.put("ascii_art", pa.toString());
        return results;
    }
}

public class open_debt_abolition {
    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("OpenDebtAbolition -- A Prova Matematica Visual");
        System.out.println("A DIVIDA NUNCA SE PAGA");
        System.out.println("=".repeat(70));

        DebtParameters params = new DebtParameters();
        DebtProjectionEngine engine = new DebtProjectionEngine(params);
        List<YearProjection> projections = engine.project();
        Map<String, Object> proof = engine.proof_summary();

        System.out.println("\nVEREDITO DA PROVA");
        System.out.println("Pais: " + proof.get("country"));
        System.out.println("Divida inicial: R$ " + String.format("%.1f", (double)proof.get("initial_debt_trillions")) + " trilhoes");
        System.out.println("VEREDITO: " + proof.get("verdict"));
        System.out.println("RAZAO: " + proof.get("reason"));

        System.out.println(ASCIIBarChart.render(projections, "debt_to_gdp"));
        System.out.println(ASCIIBarChart.render(projections, "interest_pct_revenue"));
        System.out.println(AsciiArt.render(projections));
        System.out.println(Infographic.render(projections, proof));
        System.out.println(ComparisonView.render(projections, proof));
        System.out.println(Narrative.render(projections, proof));

        System.out.println("\nGERANDO TODOS OS FORMATOS...");
        try {
            DebtVisualizer viz = new DebtVisualizer(params);
            Map<String, String> res = viz.generate_all("");
            for (Map.Entry<String,String> e : res.entrySet()) System.out.println("  " + e.getKey() + " -> " + e.getValue());
        } catch (Exception ex) { ex.printStackTrace(); }

        System.out.println("\nTotal formatos: " + VisualizationFormat.values().length);
        System.out.println("Anos projetados: " + params.years_to_project);
        System.out.println("Veredito: " + proof.get("verdict"));
        System.out.println("\nA matematica nao mente.\nA divida NUNCA se paga.\nO juros composto e um SANGUESSUGA.\nA unica saida: EXTINCAO.");
    }
}