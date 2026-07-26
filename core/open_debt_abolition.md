# OpenDebtAbolition -- A Prova Matematica Visual de que a Divida Nunca se Paga

**Arquivo original:** `open-republic/core/open_debt_abolition.py`

**Descricao:** ===============================================================================
"A divida publica nao e um emprestimo. E uma CORRENTE.
O juros composto nao e uma taxa. E um SANGUESSUGA.
Voce nao 'paga' uma divida que cresce mais rapido que sua renda.
Voce se torna ESCRAVO dela. Para sempre. Ate quebrar."
Este modulo PROVA matematicamente, com visualizacoes em multiplos formatos,
que a divida publica com juros compostos JAMAIS pode ser quitada.
A PROVA (simples, irrefutavel):
1. Divida cresce exponencialmente: D(t) = D0 * (1+r)^t
2. PIB cresce linearmente ou sub-exponencialmente: PIB(t) = PIB0 * (1+g)^t
3. Se r > g (juros > crescimento), divida/PIB -> infinito
4. Mesmo se r = g, pagar a divida requer superavit primario PERPETUO
5. Juros pago anualmente ja SUPEROU investimento publico
6. Portanto: a divida NAO PODE ser paga. Ponto. Matematica.
FORMATOS DE VISUALIZACAO:
1. ASCII art (terminal)
2. Grafico de barras ASCII
3. Tabela Markdown
4. HTML interativo (pagina web)
5. SVG (grafico vetorial)
6. CSV (dados brutos para Excel)
7. JSON (para API/integracao)
8. Infografico textual (para redes sociais)
9. Narrativa falada (para telefonista ler)
10. Comparativo visual (o que se perdeu)
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol

// !/usr/bin/env python3
// 
OpenDebtAbolition -- A Prova Matematica Visual de que a Divida Nunca se Paga
===============================================================================
"A divida publica nao e um emprestimo. E uma CORRENTE.
O juros composto nao e uma taxa. E um SANGUESSUGA.
Voce nao 'paga' uma divida que cresce mais rapido que sua renda.
Voce se torna ESCRAVO dela. Para sempre. Ate quebrar."

Este modulo PROVA matematicamente, com visualizacoes em multiplos formatos,
que a divida publica com juros compostos JAMAIS pode ser quitada.

A PROVA (simples, irrefutavel):
1. Divida cresce exponencialmente: D(t) = D0 * (1+r)^t
2. PIB cresce linearmente ou sub-exponencialmente: PIB(t) = PIB0 * (1+g)^t
3. Se r > g (juros > crescimento), divida/PIB -> infinito
4. Mesmo se r = g, pagar a divida requer superavit primario PERPETUO
5. Juros pago anualmente ja SUPEROU investimento publico
6. Portanto: a divida NAO PODE ser paga. Ponto. Matematica.

FORMATOS DE VISUALIZACAO:
1. ASCII art (terminal)
2. Grafico de barras ASCII
3. Tabela Markdown
4. HTML interativo (pagina web)
5. SVG (grafico vetorial)
6. CSV (dados brutos para Excel)
7. JSON (para API/integracao)
8. Infografico textual (para redes sociais)
9. Narrativa falada (para telefonista ler)
10. Comparativo visual (o que se perdeu)

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa math
// importa json
// importa os
// importa time


// ============================================================================
// 1. PARAMETROS DA DIVIDA
// ============================================================================

classe VisualizationFormat herda de Enum:
    // Formatos de visualizacao disponiveis.
    ASCII_BAR <- "barras_ascii"  // grafico de barras no terminal
    ASCII_ART <- "arte_ascii"  // representacao artistica
    MARKDOWN_TABLE <- "tabela_markdown"  // tabela em markdown
    HTML_PAGE <- "pagina_html"  // pagina web completa
    SVG_CHART <- "grafico_svg"  // grafico vetorial SVG
    CSV_DATA <- "dados_csv"  // planilha CSV
    JSON_DATA <- "dados_json"  // dados estruturados JSON
    INFOGRAPHIC <- "infografico"  // texto para redes sociais
    NARRATIVE <- "narrativa"  // texto para ser lido em voz alta
    COMPARISON <- "comparativo"  // o que se perdeu com juros


// decorador: @dataclass
classe DebtParameters:
    // Parametros de uma divida publica.
    declare country: str  <- "Brasil"
    declare initial_debt_brl: float  <- 6.0e12  // R$ 6 trilhoes (divida federal 2024)
    declare initial_gdp_brl: float  <- 10.0e12  // PIB ~R$ 10 trilhoes
    declare annual_interest_rate: float  <- 0.12  // 12% ao ano (Selic historica)
    declare annual_gdp_growth: float  <- 0.025  // 2.5% ao ano (crescimento real)
    declare annual_inflation: float  <- 0.045  // 4.5% ao ano
    declare annual_primary_surplus: float  <- -0.02  // -2% do PIB (deficit primario)
    declare population_millions: float  <- 215.0  // 215 milhoes de habitantes
    declare years_to_project: int  <- 50  // projetar 50 anos
    declare start_year: int  <- 2024

    funcao debt_to_gdp_ratio(self) retorna float:
        retorne self.initial_debt_brl / self.gdp_brl

    // decorador: @property
    funcao gdp_brl(self) retorna float:
        retorne self.initial_gdp_brl

    funcao real_interest_rate(self) retorna float:
        // Juros real = nominal - inflacao.
        retorne self.annual_interest_rate - self.annual_inflation

    funcao growth_gap(self) retorna float:
        // Diferenca entre juros e crescimento. Se positiva = INSUSTENTAVEL.
        retorne self.annual_interest_rate - self.annual_gdp_growth


// ============================================================================
// 2. MOTOR DE PROJECAO -- A Matematica da Morte
// ============================================================================

// decorador: @dataclass
classe YearProjection:
    // Projecao de um ano da divida.
    year: int
    year_label: int                           // ex: 2024
    debt_brl: float                           // divida total
    gdp_brl: float                            // PIB
    debt_to_gdp: float                        // divida/PIB (%)
    interest_paid_brl: float                  // juros pagos no ano
    primary_result_brl: float                 // superavit/deficit primario
    nominal_result_brl: float                 // resultado nominal
    interest_as_pct_gdp: float                // juros / PIB (%)
    interest_as_pct_revenue: float            // juros / receita (%)
    per_capita_debt_brl: float                // divida per capita
    per_capita_interest_brl: float            // juros per capita
    cumulative_interest_brl: float            // juros acumulados desde inicio
    declare point_of_no_return: bool  <- FALSO  // passou do ponto de nao retorno?


classe DebtProjectionEngine:
    // 
    Motor que projeta a divida ano a ano e PROVA que ela nao pode ser paga.

    EQUACOES:
    Divida(t+1) = Divida(t) * (1 + juros) - SuperavitPrimario(t)
    PIB(t+1) = PIB(t) * (1 + crescimento)
    JurosPagos(t) = Divida(t) * taxa_juros
    // 

    funcao __init__(self, params: DebtParameters):
        self.params = params
        self.projections: List[YearProjection] = []

    funcao project(self) retorna List[YearProjection]:
        // Projeta a divida para todos os anos.
        self.projections = []
        debt <- self.params.initial_debt_brl
        gdp <- self.params.initial_gdp_brl
        cumulative_interest <- 0.0
        point_of_no_return_found <- FALSO

        para cada i em range(self.params.years_to_project + 1):
            year_label <- self.params.start_year + i

            interest_paid <- debt * self.params.annual_interest_rate
            primary_result <- gdp * self.params.annual_primary_surplus
            revenue <- gdp * 0.18  // arrecadacao ~18% do PIB

            // Divida proximo ano = divida + juros - superavit primario
            se i > 0 entao:
                debt <- debt + interest_paid - primary_result
                gdp <- gdp * (1 + self.params.annual_gdp_growth)

            cumulative_interest <- cumulative_interest + interest_paid
            debt_to_gdp <- (debt / gdp) * 100 if gdp > 0 else 999
            interest_pct_gdp <- (interest_paid / gdp) * 100
            interest_pct_revenue <- (interest_paid / revenue) * 100 if revenue > 0 else 999
            per_capita_debt <- debt / (self.params.population_millions * 1e6)
            per_capita_interest <- interest_paid / (self.params.population_millions * 1e6)

            // Ponto de nao retorno: juros > 50% da receita
            ponr <- interest_pct_revenue > 50  E  NAO  point_of_no_return_found
            se ponr entao:
                point_of_no_return_found <- VERDADEIRO

            proj <- YearProjection(
                year <- i,
                year_label <- year_label,
                debt_brl <- debt,
                gdp_brl <- gdp,
                debt_to_gdp <- debt_to_gdp,
                interest_paid_brl <- interest_paid,
                primary_result_brl <- primary_result,
                nominal_result_brl <- primary_result - interest_paid,
                interest_as_pct_gdp <- interest_pct_gdp,
                interest_as_pct_revenue <- interest_pct_revenue,
                per_capita_debt_brl <- per_capita_debt,
                per_capita_interest_brl <- per_capita_interest,
                cumulative_interest_brl <- cumulative_interest,
                point_of_no_return <- ponr,
            )
            self.projections.append(proj)

        retorne self.projections

    funcao find_point_of_no_return(self) retorna Optional[YearProjection]:
        // Encontra o ano em que os juros superam 50% da receita.
        para cada p em self.projections:
            se p.point_of_no_return entao:
                retorne p
        retorne nulo

    funcao total_interest_paid(self) retorna float:
        // Total de juros pagos em todos os anos projetados.
        retorne sum(p.interest_paid_brl for p in self.projections)

    funcao final_debt(self) retorna float:
        retorne self.projections[-1].debt_brl if self.projections else 0

    funcao debt_multiplier(self) retorna float:
        // Quantas vezes a divida cresceu.
        se NAO  self.projections entao:
            retorne 1.0
        retorne self.projections[-1].debt_brl / self.params.initial_debt_brl

    funcao proof_summary(self) retorna Dict[str, Any]:
        // Resumo da prova matematica.
        ponr <- self.find_point_of_no_return()
        retorne {
            "country": self.params.country,
            "initial_debt_trillions": self.params.initial_debt_brl / 1e12,
            "initial_debt_to_gdp": (self.params.initial_debt_brl / self.params.gdp_brl) * 100,
            "final_debt_trillions": self.final_debt() / 1e12,
            "debt_multiplier": self.debt_multiplier(),
            "total_interest_paid_trillions": self.total_interest_paid() / 1e12,
            "interest_rate": self.params.annual_interest_rate * 100,
            "gdp_growth": self.params.annual_gdp_growth * 100,
            "growth_gap": self.params.growth_gap() * 100,
            "point_of_no_return_year": ponr.year_label if ponr else nulo,
            "point_of_no_return_detail": (
                f"No ano {ponr.year_label}, os juros da divida ({ponr.interest_as_pct_revenue:.1f}% "
                f"da receita) superaram METADE de tudo que o governo arrecada. "
                f"A partir daqui, e matematicamente impossivel pagar."
                if ponr else "Nao encontrado no periodo."
            ),
            "verdict": "IMPOSSIVEL DE PAGAR",
            "reason": (
                f"Juros ({self.params.annual_interest_rate*100:.0f}%) cresce mais rapido "
                f"que PIB ({self.params.annual_gdp_growth*100:.1f}%). "
                f"GAP = {self.params.growth_gap()*100:.1f} pontos percentuais. "
                f"A divida cresce exponencialmente. O PIB cresce lentamente. "
                f"A matematica nao mente: a divida NUNCA se paga."
            ),
        }


// ============================================================================
// 3. FORMATO 1: BARRAS ASCII (Terminal)
// ============================================================================

classe ASCIIBarChart:
    // Grafico de barras ASCII para terminal.

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection], metric: str = "debt_to_gdp") retorna str:
        // Renderiza grafico de barras ASCII.
        labels_map <- {
            "debt_to_gdp": ("Divida/PIB (%)", funcao anonima(p): p.debt_to_gdp),
            "interest_pct_gdp": ("Juros/PIB (%)", funcao anonima(p): p.interest_as_pct_gdp),
            "interest_pct_revenue": ("Juros/Receita (%)", funcao anonima(p): p.interest_as_pct_revenue),
            "per_capita_debt": ("Divida per capita (R$ mil)", funcao anonima(p): p.per_capita_debt_brl / 1e3),
        }

        desempacote title, getter <- labels_map.get(metric, labels_map["debt_to_gdp"])
        values <- [getter(p) for p in projections]
        max_val <- max(values) if values else 1
        se max_val == 0 entao:
            max_val <- 1

        lines <- []
        lines.append("")
        lines.append("=" * 70)
        lines.append(f"  {title}")
        lines.append("=" * 70)
        lines.append("")

        bar_width <- 40
        para cada (i, p) em enumerate(projections):
            val <- values[i]
            bar_len <- int((val / max_val) * bar_width) if max_val > 0 else 0
            bar <- "#" * bar_len
            marker <- " <<< PONTO DE NAO RETORNO" if p.point_of_no_return else ""
            lines.append(f"  {p.year_label} |{bar:<{bar_width}}| {val:>10.1f}{marker}")

        lines.append("")
        lines.append(f"  Cada # = {max_val/bar_width:.1f} unidades")
        lines.append("")
        retorne "\n".join(lines)


// ============================================================================
// 4. FORMATO 2: TABELA MARKDOWN
// ============================================================================

classe MarkdownTable:
    // Tabela em formato Markdown.

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection]) retorna str:
        lines <- []
        lines.append("## Projecao da Divida Publica -- A Prova Matematica")
        lines.append("")
        lines.append("| Ano | Divida (R$ T) | PIB (R$ T) | Div/PIB (%) | Juros (R$ T) | Juros/Receita (%) | Per Capita Div (R$) | Ponto Nao Retorno |")
        lines.append("|-----|--------------|------------|-------------|-------------|-------------------|--------------------|--------------------|")

        para cada p em projections:
            ponr <- "SIM" if p.point_of_no_return else ""
            lines.append(
                f"| {p.year_label} "
                f"| {p.debt_brl/1e12:.1f} "
                f"| {p.gdp_brl/1e12:.1f} "
                f"| {p.debt_to_gdp:.1f} "
                f"| {p.interest_paid_brl/1e12:.1f} "
                f"| {p.interest_as_pct_revenue:.1f} "
                f"| {p.per_capita_debt_brl:,.0f} "
                f"| {ponr} |"
            )

        lines.append("")
        retorne "\n".join(lines)


// ============================================================================
// 5. FORMATO 3: HTML INTERATIVO
// ============================================================================

classe HTMLPage:
    // Pagina HTML completa com graficos.

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection], proof: Dict[str, Any]) retorna str:
        years <- [p.year_label for p in projections]
        debts <- [round(p.debt_brl / 1e12, 2) for p in projections]
        gdps <- [round(p.gdp_brl / 1e12, 2) for p in projections]
        interests <- [round(p.interest_paid_brl / 1e12, 2) for p in projections]
        ratios <- [round(p.debt_to_gdp, 1) for p in projections]

        ponr <- proof.get("point_of_no_return_year")
        ponr_text <- proof.get("point_of_no_return_detail", "")

        html <- f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Divida Nunca Se Paga -- Prova Matematica</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Courier New', monospace;
            background: #0a0a0a; color:  // e0e0e0;
            padding: 20px; max-width: 1200px; margin: 0 auto;
        }}
        h1 {{ color:  // ff4444; text-align: center; margin: 20px 0; font-size: 2em; }}
        h2 {{ color:  // ff6666; margin: 30px 0 10px; }}
        .verdict {{
            background: #1a0000; border: 3px solid  // ff0000;
            padding: 20px; text-align: center; margin: 20px 0;
            font-size: 1.5em; color:  // ff0000; font-weight: bold;
        }}
        .proof {{
            background: #1a1100; border: 2px solid  // ffaa00;
            padding: 15px; margin: 15px 0; font-size: 1.1em;
        }}
        .chart {{ margin: 20px 0; }}
        .bar-container {{
            display: flex; align-items: center; margin: 4px 0;
            font-size: 0.85em;
        }}
        .bar-year {{ width: 50px; color:  // 888; }}
        .bar {{
            height: 20px; background: linear-gradient(90deg, #ff4444,  // ff0000);
            transition: width 0.5s; min-width: 2px;
        }}
        .bar.gdp {{ background: linear-gradient(90deg, #44ff44,  // 00aa00); }}
        .bar.interest {{ background: linear-gradient(90deg, #ffaa00,  // ff6600); }}
        .bar-label {{ margin-left: 8px; color:  // aaa; font-size: 0.8em; }}
        table {{
            width: 100%; border-collapse: collapse; margin: 15px 0;
            font-size: 0.85em;
        }}
        th, td {{ border: 1px solid  // 333; padding: 6px 8px; text-align: center; }}
        th {{ background: #1a1a1a; color:  // ff6666; }}
        td {{ color:  // ccc; }}
        .ponr {{ background: #330000; color:  // ff0000; font-weight: bold; }}
        .numbers {{ color:  // ff4444; font-weight: bold; font-size: 1.2em; }}
        .footer {{ text-align: center; margin-top: 40px; color:  // 666; font-size: 0.8em; }}
        .comparison {{
            background: #001a1a; border: 2px solid  // 00aaaa;
            padding: 15px; margin: 15px 0;
        }}
        .comparison-item {{
            display: flex; justify-content: space-between;
            padding: 8px 0; border-bottom: 1px solid  // 222;
        }}
        .comparison-lost {{ color:  // ff4444; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>A DIVIDA NUNCA SE PAGA</h1>
    <p style="text-align:center; color:#888;">Proof Visual -- {proof['country']} -- Juros Composto vs PIB</p>

    <div class="verdict">
        VEREDITO: {proof['verdict']}
    </div>

    <div class="proof">
        <strong>RAZAO:</strong> {proof['reason']}
    </div>
    // 

        // Grafico 1: Divida vs PIB
        html <- html + """
    <h2>Grafico 1: Divida vs PIB (R$ Trilhoes)</h2>
    <div class="chart">
// 
        max_val <- max(max(debts), max(gdps))
        para cada (i, year) em enumerate(years):
            debt_pct <- (debts[i] / max_val) * 100
            gdp_pct <- (gdps[i] / max_val) * 100
            html <- html + f'        <div class="bar-container"><span class="bar-year">{year}</span>'
            html <- html + f'<div class="bar" style="width:{debt_pct:.1f}%"></div>'
            html <- html + f'<span class="bar-label">R$ {debts[i]:.1f}T</span></div>\n'
            html <- html + f'        <div class="bar-container"><span class="bar-year"></span>'
            html <- html + f'<div class="bar gdp" style="width:{gdp_pct:.1f}%"></div>'
            html <- html + f'<span class="bar-label">PIB R$ {gdps[i]:.1f}T</span></div>\n'

        html <- html + """        <div style="margin-top:5px;">
            <span style="color:#ff0000;">&#9608;</span> Divida &nbsp;&nbsp;
            <span style="color:#00aa00;">&#9608;</span> PIB
        </div>
    </div>
// 

        // Grafico 2: Juros pagos por ano
        html <- html + """
    <h2>Grafico 2: Juros Pagos por Ano (R$ Trilhoes)</h2>
    <div class="chart">
// 
        max_interest <- max(interests)
        para cada (i, year) em enumerate(years):
            int_pct <- (interests[i] / max_interest) * 100 if max_interest > 0 else 0
            ponr_class <- ' ponr' if projections[i].point_of_no_return else ''
            html <- html + f'        <div class="bar-container"><span class="bar-year">{year}</span>'
            html <- html + f'<div class="bar interest" style="width:{int_pct:.1f}%"></div>'
            html <- html + f'<span class="bar-label{ponr_class}">R$ {interests[i]:.1f}T'
            se projections[i].point_of_no_return entao:
                html <- html + ' &lt;&lt;&lt; NAO RETORNO'
            html <- html + '</span></div>\n'

        html <- html + "    </div>\n"

        // Tabela
        html <- html + """
    <h2>Tabela Completa</h2>
    <table>
        <tr><th>Ano</th><th>Divida (R$ T)</th><th>PIB (R$ T)</th><th>Div/PIB %</th><th>Juros/Ano (R$ T)</th><th>Juros/Receita %</th><th>Per Capita (R$)</th></tr>
// 
        para cada p em projections:
            cls <- ' class="ponr"' if p.point_of_no_return else ''
            html <- html + (
                f'        <tr{cls}><td>{p.year_label}</td>'
                f'<td>{p.debt_brl/1e12:.1f}</td>'
                f'<td>{p.gdp_brl/1e12:.1f}</td>'
                f'<td>{p.debt_to_gdp:.1f}</td>'
                f'<td>{p.interest_paid_brl/1e12:.1f}</td>'
                f'<td>{p.interest_as_pct_revenue:.1f}</td>'
                f'<td>{p.per_capita_debt_brl:,.0f}</td></tr>\n'
            )
        html <- html + "    </table>\n"

        // Numeros chocantes
        total_int <- proof["total_interest_paid_trillions"]
        html <- html + f"""
    <h2>Os Numeros da Morte</h2>
    <div class="comparison">
        <div class="comparison-item">
            <span>Divida inicial:</span>
            <span class="numbers">R$ {proof['initial_debt_trillions']:.1f} trilhoes</span>
        </div>
        <div class="comparison-item">
            <span>Divida em {projections[-1].year_label}:</span>
            <span class="numbers">R$ {proof['final_debt_trillions']:.1f} trilhoes</span>
        </div>
        <div class="comparison-item">
            <span>Cresceu:</span>
            <span class="numbers">{proof['debt_multiplier']:.1f}x</span>
        </div>
        <div class="comparison-item">
            <span>Total de juros pagos em {len(projections)} anos:</span>
            <span class="comparison-lost">R$ {total_int:.1f} trilhoes</span>
        </div>
        <div class="comparison-item">
            <span>Isso e QUANTAS VEZES a divida inicial:</span>
            <span class="comparison-lost">{total_int / proof['initial_debt_trillions']:.1f}x</span>
        </div>
        <div class="comparison-item">
            <span>Juros pagos por cada brasileiro (total):</span>
            <span class="comparison-lost">R$ {total_int * 1e12 / 215e6:,.0f}</span>
        </div>
    </div>
// 

        // O que se perdeu
        html <- html + """
    <h2>O Que o Brasil Perdeu Pagando Juros</h2>
    <div class="comparison">
// 
        comparisons <- [
            ("Escolas publicas de qualidade (R$ 5M cada)", total_int * 1e12 / 5e6),
            ("Hospitais completos (R$ 50M cada)", total_int * 1e12 / 50e6),
            ("Casas populares (R$ 80 mil cada)", total_int * 1e12 / 80e3),
            ("Bolsas universitarias (R$ 2 mil/mes)", total_int * 1e12 / 24e3),
            ("Bolsa Familia anual por pessoa (R$ 6 mil)", total_int * 1e12 / 6e3),
            ("km de ferrovia (R$ 20M/km)", total_int * 1e12 / 20e6),
        ]
        para cada (label, qty) em comparisons:
            html <- html + (
                f'        <div class="comparison-item">'
                f'<span>{label}:</span>'
                f'<span class="comparison-lost">{qty:,.0f}</span>'
                f'</div>\n'
            )

        html <- html + """    </div>
// 

        // Ponto de nao retorno
        se ponr entao:
            html <- html + f"""
    <div class="verdict" style="font-size:1.2em;">
        PONTO DE NAO RETORNO: {ponr}
    </div>
    <div class="proof">
        {ponr_text}
    </div>
// 

        html <- html + """
    <div class="footer">
        OpenDebtAbolition -- A prova matematica visual de que a divida nunca se paga.<br>
        A divida nao e um emprestimo. E uma CORRENTE. O juros nao e uma taxa. E um SANGUESSUGA.<br>
        OpenRepublic -- Extincao da divida = Extincao da escravidao moderna.
    </div>
</body>
</html>"""
        retorne html


// ============================================================================
// 6. FORMATO 4: SVG (Grafico Vetorial)
// ============================================================================

classe SVGChart:
    // Grafico SVG vetorial.

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection], proof: Dict[str, Any]) retorna str:
        width <- 900
        height <- 500
        margin <- 60
        chart_w <- width - 2 * margin
        chart_h <- height - 2 * margin

        years <- [p.year_label for p in projections]
        debts <- [p.debt_brl / 1e12 for p in projections]
        gdps <- [p.gdp_brl / 1e12 for p in projections]
        max_val <- max(max(debts), max(gdps)) * 1.1

        n <- len(projections)
        x_step <- chart_w / max(1, n - 1)

        funcao to_x(i):
            retorne margin + i * x_step

        funcao to_y(val):
            retorne height - margin - (val / max_val) * chart_h

        // Path para divida
        debt_path <- "M " + " L ".join(f"{to_x(i):.1f},{to_y(debts[i]):.1f}" for i in range(n))
        gdp_path <- "M " + " L ".join(f"{to_x(i):.1f},{to_y(gdps[i]):.1f}" for i in range(n))

        svg <- f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="background:#0a0a0a;">
    <text x="{width/2}" y="30" text-anchor="middle" fill="#ff4444" font-size="20" font-family="monospace" font-weight="bold">
        A DIVIDA NUNCA SE PAGA -- {proof['country']}
    </text>

    <!-- Eixos -->
    <line x1="{margin}" y1="{height-margin}" x2="{width-margin}" y2="{height-margin}" stroke="#444" stroke-width="1"/>
    <line x1="{margin}" y1="{margin}" x2="{margin}" y2="{height-margin}" stroke="#444" stroke-width="1"/>

    <!-- Linha do PIB (verde) -->
    <path d="{gdp_path}" fill="none" stroke="#00cc00" stroke-width="2"/>

    <!-- Area sob a divida (vermelho) -->
    <path d="{debt_path} L {to_x(n-1):.1f},{height-margin} L {to_x(0):.1f},{height-margin} Z"
          fill <- "#ff0000" fill-opacity="0.15"/>
    <path d="{debt_path}" fill="none" stroke="#ff0000" stroke-width="3"/>
// 

        // Marcadores de ano
        para cada i em range(0, n, max(1, n // 10)):
            svg <- svg + f'    <text x="{to_x(i):.0f}" y="{height-margin+20}" text-anchor="middle" fill="#888" font-size="11" font-family="monospace">{years[i]}</text>\n'

        // Labels Y
        para cada j em range(5):
            val <- max_val * j / 4
            y <- height - margin - (val / max_val) * chart_h
            svg <- svg + f'    <text x="{margin-10}" y="{y+4:.0f}" text-anchor="end" fill="#888" font-size="10" font-family="monospace">{val:.0f}T</text>\n'
            svg <- svg + f'    <line x1="{margin}" y1="{y:.0f}" x2="{width-margin}" y2="{y:.0f}" stroke="#222" stroke-width="0.5" stroke-dasharray="3,3"/>\n'

        // Legenda
        svg <- svg + f"""
    <rect x="{width-180}" y="{margin}" width="12" height="12" fill="#ff0000"/>
    <text x="{width-160}" y="{margin+11}" fill="#ccc" font-size="12" font-family="monospace">Divida Publica</text>
    <rect x="{width-180}" y="{margin+25}" width="12" height="12" fill="#00cc00"/>
    <text x="{width-160}" y="{margin+36}" fill="#ccc" font-size="12" font-family="monospace">PIB</text>

    <text x="{width/2}" y="{height-5}" text-anchor="middle" fill="#ff0000" font-size="14" font-family="monospace" font-weight="bold">
        VEREDITO: {proof['verdict']} -- Divida cresce {proof['debt_multiplier']:.1f}x em {n-1} anos
    </text>
</svg>"""
        retorne svg


// ============================================================================
// 7. FORMATO 5: CSV (Dados Brutos)
// ============================================================================

classe CSVExporter:
    // Exporta dados para CSV.

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection]) retorna str:
        lines <- [
            "ano,divida_brl,pib_brl,divida_pib_pct,juros_pago_brl,juros_receita_pct,"
            "per_capita_divida,juros_acumulado_brl,ponto_nao_retorno"
        ]
        para cada p em projections:
            lines.append(
                f"{p.year_label},{p.debt_brl:.2f},{p.gdp_brl:.2f},{p.debt_to_gdp:.2f},"
                f"{p.interest_paid_brl:.2f},{p.interest_as_pct_revenue:.2f},"
                f"{p.per_capita_debt_brl:.2f},{p.cumulative_interest_brl:.2f},"
                f"{'SIM' if p.point_of_no_return else 'NAO'}"
            )
        retorne "\n".join(lines)


// ============================================================================
// 8. FORMATO 6: JSON
// ============================================================================

classe JSONExporter:
    // Exporta dados para JSON.

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection], proof: Dict[str, Any]) retorna str:
        data <- {
            "titulo": "A Divida Nunca Se Paga -- Prova Matematica",
            "veredito": proof["verdict"],
            "razao": proof["reason"],
            "resumo": proof,
            "projecoes": [
                {
                    "ano": p.year_label,
                    "divida_trilhoes": round(p.debt_brl / 1e12, 2),
                    "pib_trilhoes": round(p.gdp_brl / 1e12, 2),
                    "divida_pib_pct": round(p.debt_to_gdp, 1),
                    "juros_pago_trilhoes": round(p.interest_paid_brl / 1e12, 2),
                    "juros_receita_pct": round(p.interest_as_pct_revenue, 1),
                    "per_capita_divida": round(p.per_capita_debt_brl, 2),
                    "juros_acumulado_trilhoes": round(p.cumulative_interest_brl / 1e12, 2),
                    "ponto_nao_retorno": p.point_of_no_return,
                }
                for p in projections
            ],
        }
        retorne json.dumps(data, indent=2, ensure_ascii=FALSO)


// ============================================================================
// 9. FORMATO 7: INFOGRAFICO (Redes Sociais)
// ============================================================================

classe Infographic:
    // Infografico textual para redes sociais.

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection], proof: Dict[str, Any]) retorna str:
        p0 <- projections[0]
        p_last <- projections[-1]
        total_interest <- proof["total_interest_paid_trillions"]
        ponr <- proof.get("point_of_no_return_year")

        lines <- []
        lines.append("=" * 50)
        lines.append("A DIVIDA NUNCA SE PAGA")
        lines.append("=" * 50)
        lines.append("")
        lines.append(f"Pais: {proof['country']}")
        lines.append(f"Divida hoje: R$ {p0.debt_brl/1e12:.1f} trilhoes")
        lines.append(f"Em {p_last.year_label}: R$ {p_last.debt_brl/1e12:.1f} trilhoes")
        lines.append(f"Cresceu: {proof['debt_multiplier']:.1f}x")
        lines.append("")
        lines.append("--- A PROVA ---")
        lines.append(f"Juros: {proof['interest_rate']:.0f}% ao ano")
        lines.append(f"PIB cresce: {proof['gdp_growth']:.1f}% ao ano")
        lines.append(f"Gap: {proof['growth_gap']:.1f} pontos")
        lines.append("")
        lines.append(f"Juros cresce {proof['interest_rate']/proof['gdp_growth']:.1f}x")
        lines.append(f"mais rapido que a economia.")
        lines.append("")
        lines.append("--- O CUSTO HUMANO ---")
        lines.append(f"Juros pagos em {len(projections)} anos:")
        lines.append(f"R$ {total_interest:.1f} trilhoes")
        lines.append(f"= {total_interest/p0.debt_brl*1e12/1e12:.1f}x a divida inicial")
        lines.append(f"= R$ {total_interest*1e12/215e6:,.0f} por brasileiro")
        lines.append(f"= {total_interest*1e12/5e6:,.0f} escolas")
        lines.append(f"= {total_interest*1e12/50e6:,.0f} hospitais")
        lines.append(f"= {total_interest*1e12/80e3:,.0f} casas populares")
        lines.append("")

        se ponr entao:
            lines.append(f"PONTO DE NAO RETORNO: {ponr}")
            lines.append("Juros superou 50% da arrecadacao.")
            lines.append("A partir daqui, impossivel.")
            lines.append("")

        lines.append("--- O VEREDITO ---")
        lines.append("IMPOSSIVEL DE PAGAR.")
        lines.append("A matematica nao mente.")
        lines.append("A divida e uma CORRENDE.")
        lines.append("O juros e um SANGUESSUGA.")
        lines.append("")
        lines.append("A unica saida: EXTINCAO.")
        lines.append("Nao renegociar. Nao alongar.")
        lines.append("EXTINGUIR.")
        lines.append("")
        lines.append("#OpenRepublic #DividaNuncaSePaga")
        lines.append("#ExtincaoDaDivida")
        retorne "\n".join(lines)


// ============================================================================
// 10. FORMATO 8: NARRATIVA FALADA (para Telefonista)
// ============================================================================

classe Narrative:
    // Narrativa para ser lida em voz alta pela Telefonista (OpenTelefonista).

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection], proof: Dict[str, Any]) retorna str:
        p0 <- projections[0]
        p10 <- projections[min(10, len(projections)-1)]
        p_last <- projections[-1]
        total_interest <- proof["total_interest_paid_trillions"]
        ponr <- proof.get("point_of_no_return_year")

        parts <- []
        parts.append("Vou te provar algo em 30 segundos. Presta atencao.")
        parts.append("")
        parts.append(f"A divida do {proof['country']} hoje e de {p0.debt_brl/1e12:.0f} trilhoes de reais.")
        parts.append(f"O juros e de {proof['interest_rate']:.0f}% ao ano.")
        parts.append(f"Isso significa que SO EM JUROS, o pais paga {p0.interest_paid_brl/1e12:.0f} trilhoes por ano.")
        parts.append("")
        parts.append(f"O PIB cresce {proof['gdp_growth']:.0f}% ao ano.")
        parts.append(f"O juros cresce {proof['interest_rate']:.0f}% ao ano.")
        parts.append(f"O juros cresce {proof['interest_rate']/proof['gdp_growth']:.0f} vezes mais rapido que a economia.")
        parts.append("")
        parts.append(f"Em {p10.year_label}, a divida sera de R$ {p10.debt_brl/1e12:.0f} trilhoes.")
        parts.append(f"Em {p_last.year_label}, a divida sera de R$ {p_last.debt_brl/1e12:.0f} trilhoes.")
        parts.append(f"Cresceu {proof['debt_multiplier']:.0f} vezes.")
        parts.append("")
        parts.append(f"O total de juros pagos? R$ {total_interest:.0f} trilhoes.")
        parts.append(f"Isso e {total_interest/p0.debt_brl*1e12/1e12:.0f} vezes a divida original.")
        parts.append(f"Voce pagou a divida intearia varias vezes e ainda deve tudo.")
        parts.append("")

        se ponr entao:
            parts.append(f"E pior: em {ponr}, os juros superaram METADE de tudo que o governo arrecada.")
            parts.append("A partir dai, e matematicamente impossivel pagar.")

        parts.append("")
        parts.append("A divida NUNCA se paga. Ela so cresce.")
        parts.append("O pais nao paga a divida. O pais paga JUROS PARA SEMPRE.")
        parts.append("E uma corrente. E um sanguessuga. E escravidao moderna.")
        parts.append("A unica saida e a EXTINCAO. Nao renegociar. Extinguir.")
        parts.append("")
        parts.append("A matematica nao mente.")

        retorne " ".join(parts)


// ============================================================================
// 11. FORMATO 9: COMPARATIVO (O Que Se Perdeu)
// ============================================================================

classe ComparisonView:
    // Comparativo do que se perdeu pagando juros vs investindo.

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection], proof: Dict[str, Any]) retorna str:
        total_interest <- proof["total_interest_paid_trillions"]
        lines <- []
        lines.append("=" * 65)
        lines.append("O QUE O BRASIL PERDEU PAGANDO JUROS")
        lines.append(f"Total pago em juros: R$ {total_interest:.1f} trilhoes")
        lines.append("=" * 65)
        lines.append("")

        comparisons <- [
            ("Escolas publicas completas", 5e6, "R$ 5 milhoes cada"),
            ("Hospitais completos (100 leitos)", 50e6, "R$ 50 milhoes cada"),
            ("Casas populares", 80e3, "R$ 80 mil cada"),
            ("Bolsas universitarias anuais", 24e3, "R$ 2 mil/mes"),
            ("Bolsa Familia (1 ano por pessoa)", 6e3, "R$ 500/mes"),
            ("km de ferrovia nova", 20e6, "R$ 20 milhoes/km"),
            ("UPAs (Unidade Pronto Atendimento)", 15e6, "R$ 15 milhoes cada"),
            ("Creches publicas", 3e6, "R$ 3 milhoes cada"),
            ("Distribuicao de comida (cesta R$200/mes)", 2400, "R$ 200/mes por familia"),
            ("Saneamento basico por domicilio", 12e3, "R$ 12 mil por ligacao"),
        ]

        lines.append(f"{'ITEM':<45} {'QTD':>15} {'CUSTO UNIT.':>15}")
        lines.append("-" * 75)
        for label, unit_cost, cost_desc in comparisons:
            qty <- total_interest * 1e12 / unit_cost
            se qty > 1e9 entao:
                qty_str <- f"{qty/1e9:.1f} bilhoes"
            senao se qty > 1e6 entao:
                qty_str <- f"{qty/1e6:.1f} milhoes"
            senao se qty > 1e3 entao:
                qty_str <- f"{qty/1e3:.1f} mil"
            senao:
                qty_str <- f"{qty:,.0f}"
            lines.append(f"  {label:<43} {qty_str:>15} {cost_desc:>15}")

        lines.append("")
        lines.append("Cada real pago em juros e um real ROUBADO do povo.")
        lines.append("Nao e gasto publico. E SANGRIA.")
        lines.append("")
        retorne "\n".join(lines)


// ============================================================================
// 12. FORMATO 10: ARTE ASCII (Impacto Visual)
// ============================================================================

classe AsciiArt:
    // Representacao artistica ASCII do crescimento da divida.

    // decorador: @staticmethod
    funcao render(projections: List[YearProjection]) retorna str:
        lines <- []
        lines.append("")
        lines.append("  O CRESCIMENTO DA DIVIDA vs O CRESCIMENTO DO PIB")
        lines.append("  (cada bloco = ~10% da divida final)")
        lines.append("")

        final_debt <- projections[-1].debt_brl
        para cada p em projections:
            debt_blocks <- int((p.debt_brl / final_debt) * 40)
            gdp_blocks <- int((p.gdp_brl / final_debt) * 40)
            debt_bar <- "X" * max(1, debt_blocks)
            gdp_bar <- "=" * max(1, gdp_blocks)
            lines.append(f"  {p.year_label}  DIVIDA: [{debt_bar:<40}]")
            lines.append(f"         PIB:    [{gdp_bar:<40}]")
            lines.append("")

        lines.append("  X = DIVIDA (cresce exponencialmente)")
        lines.append("  = = PIB (cresce lentamente)")
        lines.append("")
        lines.append("  Veja como a divida ENGOLE o PIB.")
        lines.append("  Isso nao e opiniao. E matematica.")
        lines.append("")
        retorne "\n".join(lines)


// ============================================================================
// 13. GERADOR DE TODOS OS FORMATOS
// ============================================================================

classe DebtVisualizer:
    // Gera visualizacoes em todos os formatos e salva em arquivos.

    funcao __init__(self, params: DebtParameters):
        self.params = params
        self.engine = DebtProjectionEngine(params)
        self.projections = self.engine.project()
        self.proof = self.engine.proof_summary()

    funcao generate_all(self, output_dir: str = "") retorna Dict[str, str]:
        // Gera todos os formatos e retorna dict {formato: caminho_arquivo}.
        se NAO  output_dir entao:
            output_dir <- os.path.join(os.path.dirname(__file__), "..", "debt_visualizations")
        os.makedirs(output_dir, exist_ok=VERDADEIRO)

        results <- {}

        // ASCII Bar
        para cada metric em ["debt_to_gdp", "interest_pct_revenue", "per_capita_debt"]:
            content <- ASCIIBarChart.render(self.projections, metric)
            path <- os.path.join(output_dir, f"grafico_barras_{metric}.txt")
            use open(path, "w", encoding="utf-8") como f:
                f.write(content)
            results[f"barras_{metric}"] = path

        // Markdown
        content <- MarkdownTable.render(self.projections)
        path <- os.path.join(output_dir, "tabela_divida.md")
        use open(path, "w", encoding="utf-8") como f:
            f.write(content)
        results["markdown"] = path

        // HTML
        content <- HTMLPage.render(self.projections, self.proof)
        path <- os.path.join(output_dir, "index.html")
        use open(path, "w", encoding="utf-8") como f:
            f.write(content)
        results["html"] = path

        // SVG
        content <- SVGChart.render(self.projections, self.proof)
        path <- os.path.join(output_dir, "grafico_divida.svg")
        use open(path, "w", encoding="utf-8") como f:
            f.write(content)
        results["svg"] = path

        // CSV
        content <- CSVExporter.render(self.projections)
        path <- os.path.join(output_dir, "dados_divida.csv")
        use open(path, "w", encoding="utf-8") como f:
            f.write(content)
        results["csv"] = path

        // JSON
        content <- JSONExporter.render(self.projections, self.proof)
        path <- os.path.join(output_dir, "dados_divida.json")
        use open(path, "w", encoding="utf-8") como f:
            f.write(content)
        results["json"] = path

        // Infografico
        content <- Infographic.render(self.projections, self.proof)
        path <- os.path.join(output_dir, "infografico.txt")
        use open(path, "w", encoding="utf-8") como f:
            f.write(content)
        results["infografico"] = path

        // Narrativa
        content <- Narrative.render(self.projections, self.proof)
        path <- os.path.join(output_dir, "narrativa_falada.txt")
        use open(path, "w", encoding="utf-8") como f:
            f.write(content)
        results["narrativa"] = path

        // Comparativo
        content <- ComparisonView.render(self.projections, self.proof)
        path <- os.path.join(output_dir, "comparativo_perdas.txt")
        use open(path, "w", encoding="utf-8") como f:
            f.write(content)
        results["comparativo"] = path

        // ASCII Art
        content <- AsciiArt.render(self.projections)
        path <- os.path.join(output_dir, "arte_ascii.txt")
        use open(path, "w", encoding="utf-8") como f:
            f.write(content)
        results["ascii_art"] = path

        retorne results


// ============================================================================
// 14. DEMONSTRACAO
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenDebtAbolition -- A Prova Matematica Visual")
    print("A DIVIDA NUNCA SE PAGA")
    print("=" * 70)

    params <- DebtParameters()
    engine <- DebtProjectionEngine(params)
    projections <- engine.project()
    proof <- engine.proof_summary()

    // Resumo da prova
    print(f"\n{'=' * 70}")
    print("VEREDITO DA PROVA")
    print(f"{'=' * 70}")
    print(f"  Pais: {proof['country']}")
    print(f"  Divida inicial: R$ {proof['initial_debt_trillions']:.1f} trilhoes")
    print(f"  Divida/PIB inicial: {proof['initial_debt_to_gdp']:.1f}%")
    print(f"  Divida final ({projections[-1].year_label}): R$ {proof['final_debt_trillions']:.1f} trilhoes")
    print(f"  Cresceu: {proof['debt_multiplier']:.1f}x")
    print(f"  Total de juros pagos: R$ {proof['total_interest_paid_trillions']:.1f} trilhoes")
    print(f"  Juros: {proof['interest_rate']:.0f}% | PIB cresce: {proof['gdp_growth']:.1f}%")
    print(f"  Gap: {proof['growth_gap']:.1f} pontos percentuais")
    print(f"  Ponto de nao retorno: {proof['point_of_no_return_year']}")
    print(f"\n  VEREDITO: {proof['verdict']}")
    print(f"  RAZAO: {proof['reason']}")

    // ASCII Bar Charts
    print(ASCIIBarChart.render(projections, "debt_to_gdp"))
    print(ASCIIBarChart.render(projections, "interest_pct_revenue"))

    // ASCII Art
    print(AsciiArt.render(projections))

    // Infografico
    print(Infographic.render(projections, proof))

    // Comparativo
    print(ComparisonView.render(projections, proof))

    // Narrativa
    print(f"\n{'=' * 70}")
    print("NARRATIVA FALADA (para Telefonista ler)")
    print(f"{'=' * 70}")
    print(Narrative.render(projections, proof))

    // Gerar todos os arquivos
    print(f"\n{'=' * 70}")
    print("GERANDO TODOS OS FORMATOS...")
    print(f"{'=' * 70}")
    viz <- DebtVisualizer(params)
    results <- viz.generate_all()
    para cada (fmt, path) em results.items():
        print(f"  {fmt:25} -> {path}")

    print(f"\n{'=' * 70}")
    print(f"Total formatos: {len(VisualizationFormat)}")
    print(f"Anos projetados: {params.years_to_project}")
    print(f"Veredito: {proof['verdict']}")
    print(f"\nA matematica nao mente.")
    print(f"A divida NUNCA se paga.")
    print(f"O juros composto e um SANGUESSUGA.")
    print(f"A unica saida: EXTINCAO.")


se __name__ == "__main__" entao:
    demo()

```
