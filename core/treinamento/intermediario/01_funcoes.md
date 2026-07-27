# Treinamento Intermediario 01 -- Funcoes Reutilizaveis para Analise

**Nivel:** Intermediario
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 40 min

**Objetivo:** Encapsular logica de analise em funcoes reutilizaveis.

---

```portugol++

// TREINAMENTO INTERMEDIARIO -- Licao 01: Funcoes
// ============================================================
// Funcoes sao blocos reutilizaveis. Em analise de dados,
// voce escreve uma vez e usa em mil datasets diferentes.

// ============================================================
// 1. FUNCOES BASICAS DE ESTATISTICA
// ============================================================

funcao calcular_media(valores: [flutuante]) -> flutuante:
    seja total: flutuante = 0.0
    para cada v em valores:
        total = total + v
    retorne total / tamanho(valores)


funcao calcular_soma(valores: [flutuante]) -> flutuante:
    seja total: flutuante = 0.0
    para cada v em valores:
        total = total + v
    retorne total


funcao encontrar_maximo(valores: [flutuante]) -> flutuante:
    seja maximo: flutuante = valores[0]
    para cada v em valores:
        se v > maximo entao:
            maximo = v
    retorne maximo


funcao encontrar_minimo(valores: [flutuante]) -> flutuante:
    seja minimo: flutuante = valores[0]
    para cada v em valores:
        se v < minimo entao:
            minimo = v
    retorne minimo


// ============================================================
// 2. FUNCAO DE FORMATACAO MOEDARIA
// ============================================================

funcao formatar_moeda(valor: flutuante) -> texto:
    // Formata um numero como moeda brasileira
    seja valor_texto = texto(valor)
    retorne "R$ " + valor_texto


// ============================================================
// 3. FUNCAO DE CLASSIFICACAO
// ============================================================

funcao classificar_produto(faturamento: flutuante) -> texto:
    se faturamento >= 10000 entao:
        retorne "ESTRELA"
    senao se faturamento >= 5000 entao:
        retorne "ALTO"
    senao se faturamento >= 1000 entao:
        retorne "MEDIO"
    senao:
        retorne "BAIXO"


// ============================================================
// 4. FUNCAO DE FILTRO
// ============================================================

funcao filtrar_acima_de(valores: [flutuante], limite: flutuante) -> [flutuante]:
    // Retorna apenas valores maiores que o limite
    seja resultado: [flutuante] = []
    para cada v em valores:
        se v > limite entao:
            resultado.adicione(v)
    retorne resultado


// ============================================================
// 5. APLICACAO: ANALISE COMPLETA USANDO FUNCOES
// ============================================================

seja vendas_diarias = [1200.0, 800.0, 2500.0, 300.0, 1800.0, 950.0, 2100.0]

imprima("=== ANALISE DE VENDAS ===")
imprima("Total: " + formatar_moeda(calcular_soma(vendas_diarias)))
imprima("Media: " + formatar_moeda(calcular_media(vendas_diarias)))
imprima("Maximo: " + formatar_moeda(encontrar_maximo(vendas_diarias)))
imprima("Minimo: " + formatar_moeda(encontrar_minimo(vendas_diarias)))

seja vendas_altas = filtrar_acima_de(vendas_diarias, 1000.0)
imprima("Dias acima de R$ 1000: " + texto(tamanho(vendas_altas)))

para cada v em vendas_diarias:
    imprima("  " + formatar_moeda(v) + " -> " + classificar_produto(v))

// EXERCICIO: crie uma funcao calcular_mediana(valores) que ordena
// a lista e retorna o valor do meio.
```
