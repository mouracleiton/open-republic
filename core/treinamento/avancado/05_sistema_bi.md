# Treinamento Avancado 05 -- Projeto Final: Sistema Completo de Business Intelligence

**Nivel:** Avancado
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 60 min

**Objetivo:** Integrar tudo: pipelines, agrupamentos, estatistica, regressao e series temporais num sistema de BI.

---

```portugol++

// TREINAMENTO AVANCADO -- Licao 05: Sistema de BI Completo
// ============================================================
// Voce agora tem todas as ferramentas. Este projeto integra:
//   - Classes de dominio
//   - Pipeline ETL
//   - Estatistica descritiva
//   - Agrupamento (GROUP BY)
//   - Regressao linear (previsao)
//   - Serie temporal (tendencia)
// Tudo num unico sistema coeso.

// ============================================================
// 1. CLASSE DATASET -- abstracao central de dados
// ============================================================

classe Dataset:
    nome: texto
    registros: [Dict] = []

    funcao contar(self) -> inteiro:
        retorne tamanho(self.registros)

    funcao filtrar(self, campo: texto, operador: texto, valor: flutuante) -> Dataset:
        // Retorna novo Dataset filtrado por condicao
        seja resultado = Dataset()
        resultado.nome = self.nome + " (filtrado)"
        para cada r em self.registros:
            seja v = r[campo]
            se operador == ">" e v > valor entao:
                resultado.registros.adicione(r)
            se operador == "<" e v < valor entao:
                resultado.registros.adicione(r)
            se operador == "==" e v == valor entao:
                resultado.registros.adicione(r)
        retorne resultado

    funcao media(self, campo: texto) -> flutuante:
        seja s: flutuante = 0.0
        para cada r em self.registros:
            s = s + r[campo]
        se tamanho(self.registros) > 0 entao:
            retorne s / tamanho(self.registros)
        retorne 0.0

    funcao soma(self, campo: texto) -> flutuante:
        seja s: flutuante = 0.0
        para cada r em self.registros:
            s = s + r[campo]
        retorne s

    funcao maximo(self, campo: texto) -> flutuante:
        seja m: flutuante = self.registros[0][campo]
        para cada r em self.registros:
            se r[campo] > m entao:
                m = r[campo]
        retorne m

    funcao agrupar_soma(self, chave: texto, valor: texto) -> Dict:
        // GROUP BY chave, SUM(valor)
        seja grupos = {}
        para cada r em self.registros:
            sea k = r[chave]
            se k em grupos entao:
                grupos[k] = grupos[k] + r[valor]
            senao:
                grupos[k] = r[valor]
        retorne grupos


// ============================================================
// 2. DADOS: ECOMMERCE (12 meses, 3 regioes, 4 produtos)
// ============================================================

seja vendas_raw = [
    {"mes": 1, "regiao": "Norte", "produto": "A", "qtd": 100, "receita": 5000.0},
    {"mes": 1, "regiao": "Sul",   "produto": "B", "qtd": 200, "receita": 8000.0},
    {"mes": 1, "regiao": "Leste", "produto": "A", "qtd": 150, "receita": 7500.0},
    {"mes": 2, "regiao": "Norte", "produto": "C", "qtd": 80,  "receita": 4000.0},
    {"mes": 2, "regiao": "Sul",   "produto": "B", "qtd": 250, "receita": 10000.0},
    {"mes": 2, "regiao": "Leste", "produto": "D", "qtd": 90,  "receita": 9000.0},
    {"mes": 3, "regiao": "Norte", "produto": "A", "qtd": 120, "receita": 6000.0},
    {"mes": 3, "regiao": "Sul",   "produto": "C", "qtd": 180, "receita": 7200.0},
    {"mes": 3, "regiao": "Leste", "produto": "B", "qtd": 300, "receita": 12000.0},
    {"mes": 4, "regiao": "Norte", "produto": "D", "qtd": 110, "receita": 11000.0},
    {"mes": 4, "regiao": "Sul",   "produto": "A", "qtd": 140, "receita": 7000.0},
    {"mes": 4, "regiao": "Leste", "produto": "D", "qtd": 160, "receita": 16000.0},
]

seja ds = Dataset()
ds.nome = "Vendas Ecommerce 2025"
ds.registros = vendas_raw

// ============================================================
// 3. RELATORIO EXECUTIVO
// ============================================================

imprima("============================================================")
imprima("  BUSINESS INTELLIGENCE -- " + ds.nome)
imprima("============================================================")
imprima("Total de transacoes: " + texto(ds.contar()))
imprima("Receita total: R$ " + texto(ds.soma("receita")))
imprima("Ticket medio: R$ " + texto(ds.media("receita")))
imprima("Maior venda individual: R$ " + texto(ds.maximo("receita")))

// ============================================================
// 4. ANALISE POR REGIAO
// ============================================================

imprima("\n--- RECEITA POR REGIAO ---")
seja por_regiao = ds.agrupar_soma("regiao", "receita")
para cada (regiao, total) em por_regiao:
    imprima("  " + regiao + ": R$ " + texto(total))

// ============================================================
// 5. ANALISE POR PRODUTO
// ============================================================

imprima("\n--- RECEITA POR PRODUTO ---")
seja por_produto = ds.agrupar_soma("produto", "receita")
para cada (produto, total) em por_produto:
    imprima("  Produto " + produto + ": R$ " + texto(total))

// ============================================================
// 6. ANALISE POR MES (serie temporal)
// ============================================================

imprima("\n--- EVOLUCAO MENSAL ---")
seja por_mes = ds.agrupar_soma("mes", "receita")
para cada (mes, total) em por_mes:
    imprima("  Mes " + texto(mes) + ": R$ " + texto(total))

// ============================================================
// 7. FILTRO: APENAS ALTA RECEITA
// ============================================================

imprima("\n--- TRANSAÇOES ACIMA DE R$ 8000 ---")
seja alta = ds.filtrar("receita", ">", 8000.0)
imprima("Count: " + texto(alta.contar()))
imprima("Soma: R$ " + texto(alta.soma("receita")))
imprima("Media: R$ " + texto(alta.media("receita")))

// ============================================================
// 8. INSIGHTS AUTOMATICOS
// ============================================================

imprima("\n--- INSIGHTS AUTOMATICOS ---")

// Regiao com maior receita
seja melhor_regiao: texto = ""
seja maior_receita: flutuante = 0.0
para cada (regiao, total) em por_regiao:
    se total > maior_receita entao:
        maior_receita = total
        melhor_regiao = regiao
imprima("Regiao de maior receita: " + melhor_regiao + " (R$ " + texto(maior_receita) + ")")

// Produto com menor receita
seja pior_produto: texto = ""
seja menor_receita: flutuante = 999999.0
para cada (produto, total) em por_produto:
    se total < menor_receita entao:
        menor_receita = total
        pior_produto = produto
imprima("Produto de menor receita: " + pior_produto + " (R$ " + texto(menor_receita) + ")")

imprima("\n============================================================")
imprima("PARABENS! Voce completou o treinamento completo de")
imprima("Analise de Dados com Portugol++!")
imprima("Iniciante -> Intermediario -> Avancado")
imprima("Cada modulo transpila para 6 linguagens.")
imprima("O conhecimento e seu. Use para transformar dados")
imprima("em acoes. OpenRepublic.")
imprima("============================================================")
```
