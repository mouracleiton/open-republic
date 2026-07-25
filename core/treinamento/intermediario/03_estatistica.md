# Treinamento Intermediario 03 -- Estatistica Descritiva em PP

**Nivel:** Intermediario
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 40 min

**Objetivo:** Implementar mediana, variancia, desvio padrao e percentis.

---

```portugol++

// TREINAMENTO INTERMEDIARIO -- Licao 03: Estatistica Descritiva
// ============================================================
// Estatistica descritiva resume um conjunto de dados em numeros.
// Media, mediana, variancia e desvio padrao sao fundamentais.

// ============================================================
// 1. MEDIA (ja vimos -- revisao rapida)
// ============================================================

funcao media(valores: [flutuante]) -> flutuante:
    seja s: flutuante = 0.0
    para cada v em valores:
        s = s + v
    retorne s / tamanho(valores)


// ============================================================
// 2. MEDIANA -- valor central dos dados ordenados
// ============================================================

funcao mediana(valores: [flutuante]) -> flutuante:
    // Ordenar (bubble sort simples)
    seja dados = valores
    seja n = tamanho(dados)
    para cada i em intervalo(n):
        para cada j em intervalo(n - 1):
            se dados[j] > dados[j + 1] entao:
                seja temp = dados[j]
                dados[j] = dados[j + 1]
                dados[j + 1] = temp

    se n % 2 == 0 entao:
        retorne (dados[n / 2 - 1] + dados[n / 2]) / 2.0
    senao:
        retorne dados[n / 2]


// ============================================================
// 3. VARIANCIA -- quao espalhados os dados estao da media
// ============================================================

funcao variancia(valores: [flutuante]) -> flutuante:
    seja m = media(valores)
    seja soma_quadrados: flutuante = 0.0
    para cada v em valores:
        seja diferenca = v - m
        soma_quadrados = soma_quadrados + (diferenca * diferenca)
    retorne soma_quadrados / tamanho(valores)


// ============================================================
// 4. DESVIO PADRAO -- raiz da variancia
// ============================================================

funcao desvio_padrao(valores: [flutuante]) -> flutuante:
    // Aproximacao da raiz quadrada pelo metodo de Newton
    seja v = variancia(valores)
    seja raiz: flutuante = v / 2.0
    para cada i em intervalo(20):
        raiz = (raiz + v / raiz) / 2.0
    retorne raiz


// ============================================================
// 5. APLICACAO: ANALISE COMPLETA DE UM DATASET
// ============================================================

seja salarios = [2500.0, 3200.0, 1800.0, 4500.0, 2900.0, 3700.0, 2200.0, 5500.0, 3100.0, 4000.0]

imprima("=== ANALISE SALARIAL ===")
imprima("N funcionarios: " + texto(tamanho(salarios)))
imprima("Media salarial: R$ " + texto(media(salarios)))
imprima("Mediana: R$ " + texto(mediana(salarios)))
imprima("Variancia: " + texto(variancia(salarios)))
imprima("Desvio padrao: R$ " + texto(desvio_padrao(salarios)))

// Interpretacao:
// Se media > mediana: outliers altos (poucos ganham muito)
// Se desvio padrao > 1000: grande desigualdade
se media(salarios) > mediana(salarios) entao:
    imprima("Distribuicao assimetrica -- poucos salarios altos puxam a media")

se desvio_padrao(salarios) > 1000 entao:
    imprima("ALERTA: Alta desigualdade salarial detectada")

// EXERCICIO: adicione funcoes para percentil(25) e percentil(75).
// Compare com a media para entender a distribuicao.
```
