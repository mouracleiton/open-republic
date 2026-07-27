# Treinamento Iniciante 01 -- Variaveis e Tipos de Dados

**Nivel:** Iniciante
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 30 min

**Objetivo:** Aprender a declarar variaveis e os tipos fundamentais para analise de dados.

---

```portugol++

// TREINAMENTO INICIANTE -- Licao 01: Variaveis e Tipos
// ============================================================
// Em analise de dados, tudo comeca com variaveis.
// Cada coluna de uma tabela e uma variavel.
// Cada medida e um numero. Cada categoria e um texto.

// 1. TIPOS PRIMITIVOS -- a base de tudo
// ------------------------------------------------------------
// INTEIRO: contagens (numero de vendas, pessoas, cliques)
seja vendas_janeiro: inteiro = 150
seja total_clientes: inteiro = 1200

// FLUTUANTE: medidas com casas decimais (preco, media, percentual)
seja preco_produto: flutuante = 29.90
seja taxa_conversao: flutuante = 0.035  // 3.5%
seja pi: flutuante = 3.14159

// TEXTO: categorias, nomes, rotulos
seja nome_produto: texto = "Notebook OpenRepublic"
seja categoria: texto = "Eletronicos"
seja status_pedido: texto = "Entregue"

// LOGICO: flags booleanas (ativo/inativo, aprovado/reprovado)
seja cliente_ativo: logico = verdadeiro
seja estoque_zerado: logico = falso

// 2. INFERENCIA DE TIPO -- Portugol++ descobre automaticamente
// ------------------------------------------------------------
seja x = 42           // inteiro (inferido)
seja nome = "Ana"     // texto (inferido)
seja ativo = falso    // logico (inferido)
seja altura = 1.75    // flutuante (inferido)

// 3. OPERACOES ARITMETICAS BASICAS
// ------------------------------------------------------------
seja a: inteiro = 10
seja b: inteiro = 3

seja soma = a + b           // 13
seja subtracao = a - b      // 7
seja multiplicacao = a * b  // 30
seja divisao = a / b        // 3.33... (flutuante)
seja resto = a % b          // 1 (modulo -- util para agrupar)

// 4. EXIBINDO DADOS
// ------------------------------------------------------------
imprima("=== Relatorio de Vendas ===")
imprima("Vendas de janeiro: " + texto(vendas_janeiro))
imprima("Preco do produto: R$ " + texto(preco_produto))
imprima("Cliente ativo: " + texto(cliente_ativo))

// EXERCICIO: declare variaveis para:
//   - sua idade (inteiro)
//   - seu nome (texto)
//   - seu peso (flutuante)
//   - se voce gosta de programar (logico)
// Depois imprima tudo com imprima()
```
