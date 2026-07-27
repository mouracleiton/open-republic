# Treinamento Iniciante 02 -- Condicionais para Classificacao de Dados

**Nivel:** Iniciante
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 30 min

**Objetivo:** Usar se/senao para classificar dados em categorias.

---

```portugol++

// TREINAMENTO INICIANTE -- Licao 02: Condicionais
// ============================================================
// Condicionais sao usadas para CLASSIFICAR dados.
// Ex: cliente VIP? produto em falta? aluno aprovado?

// 1. SE / SENAO BASICO
// ------------------------------------------------------------
seja nota: flutuante = 7.5

se nota >= 7 entao:
    imprima("Aprovado")
senao se nota >= 5 entao:
    imprima("Recuperacao")
senao:
    imprima("Reprovado")

// 2. CLASSIFICACAO DE CLIENTES POR GASTO
// ------------------------------------------------------------
seja gasto_mensal: flutuante = 3500.0

se gasto_mensal >= 5000 entao:
    imprima("Cliente VIP -- oferece gerente dedicado")
senao se gasto_mensal >= 1000 entao:
    imprima("Cliente Premium -- oferece cashback")
senao se gasto_mensal >= 500 entao:
    imprima("Cliente Regular -- oferece desconto")
senao:
    imprima("Cliente Novo -- oferece primeira compra")

// 3. COMBINANDO CONDICOES (E / OU / NAO)
// ------------------------------------------------------------
seja tem_estoque: logico = verdadeiro
seja tem_desconto: logico = verdadeiro
seja preco_alto: logico = falso

se tem_estoque e tem_desconto entao:
    imprima("Produto promocional -- destacar na vitrine!")

se nao tem_estoque entao:
    imprima("Produto esgotado -- notificar quando chegar")

if tem_estoque e nao preco_alto entao:
    imprima("Oportunidade de compra")

// 4. APLICACAO: SISTEMA DE SCORING DE CREDITO
// ------------------------------------------------------------
seja renda: flutuante = 4000.0
seja dividas: flutuante = 1000.0
seja historico_limpo: logico = verdadeiro

seja limite_aprovado: flutuante = 0.0

se renda >= 5000 e historico_limpo entao:
    limite_aprovado = renda * 3.0
    imprima("Credito aprovado -- limite: R$ " + texto(limite_aprovado))
senao se renda >= 2000 e dividas < renda entao:
    limite_aprovado = renda * 1.5
    imprima("Credito moderado -- limite: R$ " + texto(limite_aprovado))
senao:
    imprima("Credito negado -- consultar analise manual")

// EXERCICIO: crie um classificador de produtos que recebe
// o preco e diz se e: "Barato" (<50), "Acessivel" (50-200),
// "Premium" (200-1000) ou "Luxo" (>1000)
```
