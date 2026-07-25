# Treinamento Avancado 03 -- Regressao Linear do Zero

**Nivel:** Avancado
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 50 min

**Objetivo:** Implementar regressao linear (minimos quadrados) para previsao.

---

```portugol++

// TREINAMENTO AVANCADO -- Licao 03: Regressao Linear
// ============================================================
// Regressao linear encontra a melhor reta que se ajusta aos dados.
// Formula: y = a*x + b, onde a = inclinacao, b = intercepto.
// Metodo: minimos quadrados (ordinary least squares).

// ============================================================
// 1. CLASSE MODELO DE REGRESSAO
// ============================================================

classe RegressaoLinear:
    coeficiente_a: flutuante = 0.0  // inclinacao
    coeficiente_b: flutuante = 0.0  // intercepto
    r_quadrado: flutuante = 0.0     // qualidade do ajuste

    funcao treinar(self, x: [flutuante], y: [flutuante]) -> vazio:
        // Calcula os coeficientes pelo metodo dos minimos quadrados
        seja n = tamanho(x)
        seja soma_x: flutuante = 0.0
        seja soma_y: flutuante = 0.0
        seja soma_xy: flutuante = 0.0
        seja soma_x2: flutuante = 0.0

        para cada i em intervalo(n):
            soma_x = soma_x + x[i]
            soma_y = soma_y + y[i]
            soma_xy = soma_xy + (x[i] * y[i])
            soma_x2 = soma_x2 + (x[i] * x[i])

        // a = (n*sum(xy) - sum(x)*sum(y)) / (n*sum(x^2) - sum(x)^2)
        self.coeficiente_a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x * soma_x)

        // b = (sum(y) - a*sum(x)) / n
        self.coeficiente_b = (soma_y - self.coeficiente_a * soma_x) / n

        // Calcular R^2
        self._calcular_r2(x, y)

    funcao _calcular_r2(self, x: [flutuante], y: [flutuante]) -> vazio:
        seja media_y: flutuante = 0.0
        para cada v em y:
            media_y = media_y + v
        media_y = media_y / tamanho(y)

        seja sq_total: flutuante = 0.0
        seja sq_residuo: flutuante = 0.0

        para cada i em intervalo(tamanho(x)):
            seja y_previsto = self.prever(x[i])
            sq_total = sq_total + ((y[i] - media_y) * (y[i] - media_y))
            sq_residuo = sq_residuo + ((y[i] - y_previsto) * (y[i] - y_previsto))

        se sq_total > 0 entao:
            self.r_quadrado = 1.0 - (sq_residuo / sq_total)

    funcao prever(self, x: flutuante) -> flutuante:
        retorne self.coeficiente_a * x + self.coeficiente_b

    funcao resumo(self) -> texto:
        retorne "y = " + texto(self.coeficiente_a) + "x + " + texto(self.coeficiente_b) + " | R^2 = " + texto(self.r_quadrado)


// ============================================================
// 2. APLICACAO: PREVER VENDAS COM BASE EM GASTO COM MARKETING
// ============================================================

// Dados historicos: gasto_marketing (x) vs vendas (y)
seja gastos_marketing = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0, 8000.0]
seja vendas = [15000.0, 22000.0, 28000.0, 38000.0, 42000.0, 52000.0, 58000.0, 68000.0]

seja modelo = RegressaoLinear()
modelo.treinar(gastos_marketing, vendas)

imprima("=== MODELO DE REGRESSAO LINEAR ===")
imprima("Equacao: " + modelo.resumo())
imprima("")

se modelo.r_quadrado > 0.9 entao:
    imprima("Qualidade do modelo: EXCELENTE (R^2 > 0.9)")
senao se modelo.r_quadrado > 0.7 entao:
    imprima("Qualidade do modelo: BOM (0.7 < R^2 < 0.9)")
senao:
    imprima("Qualidade do modelo: BAIXA -- relacao fraca entre variaveis")

// ============================================================
// 3. PREVISOES
// ============================================================

imprima("\n--- PREVISOES ---")
seja cenarios = [5000.0, 10000.0, 15000.0, 20000.0]
para cada gasto em cenarios:
    seja venda_prevista = modelo.prever(gasto)
    imprima("  Investindo R$ " + texto(gasto) + " -> Venda prevista: R$ " + texto(venda_prevista))

// ============================================================
// 4. ANALISE DE MARGEM
// ============================================================

imprima("\n--- ANALISE DE RETORNO ---")
para cada gasto em cenarios:
    seja receita = modelo.prever(gasto)
    seja lucro = receita - gasto
    seja roi = (lucro / gasto) * 100.0
    imprima("  R$ " + texto(gasto) + " investido -> ROI: " + texto(roi) + "%")

// EXERCICIO: adicione validacao cruzada: divida os dados em treino/teste
// e calcule o erro medio absoluto (MAE) no conjunto de teste.
```
