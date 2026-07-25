# Treinamento Avancado 02 -- Agrupamento e Agregacao (GROUP BY)

**Nivel:** Avancado
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 50 min

**Objetivo:** Implementar GROUP BY + agregacoes (SUM, COUNT, AVG, MIN, MAX) em PP.

---

```portugol++

// TREINAMENTO AVANCADO -- Licao 02: Agrupamento e Agregacao
// ============================================================
// Agrupar dados por categoria e calcular metricas e o coracao
// de SQL (GROUP BY) e Pandas (groupby).

// ============================================================
// 1. FUNCAO GROUP BY GENERICA
// ============================================================

funcao agrupar_por(dados: [Dict], chave: texto) -> Dict:
    // Agrupa registros pelo valor de uma chave
    // Retorna {valor_chave: [registros]}
    seja grupos = {}
    para cada r em dados:
        seja valor = r[chave]
        se valor em grupos entao:
            grupos[valor].adicione(r)
        senao:
            grupos[valor] = [r]
    retorne grupos


// ============================================================
// 2. FUNCOES DE AGREGACAO
// ============================================================

funcao agg_soma(grupo: [Dict], campo: texto) -> flutuante:
    seja total: flutuante = 0.0
    para cada r em grupo:
        total = total + r[campo]
    retorne total


funcao agg_media(grupo: [Dict], campo: texto) -> flutuante:
    se tamanho(grupo) == 0 entao:
        retorne 0.0
    retorne agg_soma(grupo, campo) / tamanho(grupo)


funcao agg_max(grupo: [Dict], campo: texto) -> flutuante:
    seja maximo: flutuante = grupo[0][campo]
    para cada r em grupo:
        se r[campo] > maximo entao:
            maximo = r[campo]
    retorne maximo


funcao agg_min(grupo: [Dict], campo: texto) -> flutuante:
    seja minimo: flutuante = grupo[0][campo]
    para cada r em grupo:
        se r[campo] < minimo entao:
            minimo = r[campo]
    retorne minimo


// ============================================================
// 3. PIVOT TABLE: agrupar + multiplas agregacoes
// ============================================================

funcao pivot_table(dados: [Dict], chave_grupo: texto, campo_valor: texto) -> [Dict]:
    // Equivalente a: dados.groupby(chave)[campo].agg(['count','sum','mean','min','max'])
    seja grupos = agrupar_por(dados, chave_grupo)
    seja resultado: [Dict] = []

    para cada (grupo, registros) em grupos:
        seja linha = {
            "grupo": grupo,
            "count": tamanho(registros),
            "sum": agg_soma(registros, campo_valor),
            "mean": agg_media(registros, campo_valor),
            "min": agg_min(registros, campo_valor),
            "max": agg_max(registros, campo_valor),
        }
        resultado.adicione(linha)

    retorne resultado


// ============================================================
// 4. APLICACAO: ANALISE DE VENDAS POR REGIAO
// ============================================================

seja vendas = [
    {"vendedor": "Ana",   "regiao": "Norte", "valor": 5000.0},
    {"vendedor": "Bruno", "regiao": "Norte", "valor": 3000.0},
    {"vendedor": "Carla", "regiao": "Sul",   "valor": 7000.0},
    {"vendedor": "Diego", "regiao": "Sul",   "valor": 2000.0},
    {"vendedor": "Elena", "regiao": "Leste", "valor": 4500.0},
    {"vendedor": "Felipe","regiao": "Norte", "valor": 6000.0},
    {"vendedor": "Gabi",  "regiao": "Sul",   "valor": 8000.0},
    {"vendedor": "Hugo",  "regiao": "Leste", "valor": 1500.0},
]

seja relatorio = pivot_table(vendas, "regiao", "valor")

imprima("=== PIVOT TABLE: VENDAS POR REGIAO ===")
imprima("Regiao  | Count | Sum        | Mean      | Min      | Max")
imprima("--------|-------|------------|-----------|----------|----------")
para cada r em relatorio:
    imprima("  " + r["grupo"] + "  | " +
            texto(r["count"]) + "     | R$ " +
            texto(r["sum"]) + "  | R$ " +
            texto(r["mean"]) + "  | R$ " +
            texto(r["min"]) + "  | R$ " +
            texto(r["max"]))

// ============================================================
// 5. RANKING DENTRO DE GRUPOS
// ============================================================

imprima("\n--- TOP VENDEDOR POR REGIAO ---")
seja grupos_regiao = agrupar_por(vendas, "regiao")
para cada (regiao, regs) em grupos_regiao:
    seja maior: flutuante = 0.0
    seja top_vendedor: texto = ""
    para cada r em regs:
        se r["valor"] > maior entao:
            maior = r["valor"]
            top_vendedor = r["vendedor"]
    imprima("  " + regiao + ": " + top_vendedor + " (R$ " + texto(maior) + ")")

// EXERCICIO: crie um pivot com DUAS dimensoes (regiao + produto)
// usando uma chave composta "regiao|produto".
```
