# Treinamento Iniciante 03 -- Loops para Processar Listas de Dados

**Nivel:** Iniciante
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 30 min

**Objetivo:** Usar loops para processar colecoes de dados repetidamente.

---

```portugol++

// TREINAMENTO INICIANTE -- Licao 03: Loops
// ============================================================
// Loops sao o motor da analise de dados.
// Para cada linha de uma tabela, para cada item de uma lista,
// voce processa, transforma e acumula resultados.

// 1. PARA CADA -- iterar sobre uma lista
// ------------------------------------------------------------
seja vendas = [100, 250, 80, 300, 150, 200, 90]

para cada valor em vendas:
    imprima("Venda: R$ " + texto(valor))

// 2. ACUMULADOR -- somar todos os valores
// ------------------------------------------------------------
seja total: flutuante = 0.0

para cada valor em vendas:
    total = total + valor

imprima("Total de vendas: R$ " + texto(total))
imprima("Media: R$ " + texto(total / tamanho(vendas)))

// 3. CONTADOR -- contar elementos que satisfazem condicao
// ------------------------------------------------------------
seja vendas_altas: inteiro = 0

para cada valor em vendas:
    se valor > 150 entao:
        vendas_altas = vendas_altas + 1

imprima("Vendas acima de R$ 150: " + texto(vendas_altas))

// 4. INTERVALO -- processar uma sequencia numerica
// ------------------------------------------------------------
seja meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

para cada mes em meses:
    imprima("Processando mes: " + mes)

// 5. MAXIMO E MINIMO -- encontrar extremos
// ------------------------------------------------------------
seja maior: flutuante = vendas[0]
seja menor: flutuante = vendas[0]

para cada valor em vendas:
    se valor > maior entao:
        maior = valor
    se valor < menor entao:
        menor = valor

imprima("Maior venda: R$ " + texto(maior))
imprima("Menor venda: R$ " + texto(menor))

// 6. ENQUANTO -- loop com condicao de parada
// ------------------------------------------------------------
seja indice: inteiro = 0
seja soma_parcial: flutuante = 0.0

enquanto soma_parcial < 500:
    soma_parcial = soma_parcial + vendas[indice]
    imprima("Indice " + texto(indice) + " -- acumulado: R$ " + texto(soma_parcial))
    indice = indice + 1

imprima("Atingiu R$ 500 apos " + texto(indice) + " vendas")

// EXERCICIO: dada a lista de temperaturas [22.5, 25.0, 28.3, 30.1, 27.8, 24.0]
// calcule: media, maxima, minima, e quantos dias acima de 26 graus
```
