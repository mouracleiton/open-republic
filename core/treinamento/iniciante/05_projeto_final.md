# Treinamento Iniciante 05 -- Projeto Final: Mini Relatorio de Vendas

**Nivel:** Iniciante
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 45 min

**Objetivo:** Combinar variaveis, condicionais, loops e estruturas para gerar um relatorio completo.

---

```portugol++

// TREINAMENTO INICIANTE -- Licao 05: Projeto Final
// ============================================================
// Voce vai construir um SISTEMA COMPLETO de relatorio de vendas
// usando tudo que aprendeu nas 4 licoes anteriores.
// Este e o tipo de relatorio que analistas jr geram todo dia.

// ============================================================
// DADOS: base de vendas (tabela representada como lista de dicts)
// ============================================================

seja vendas = [
    {"produto": "Notebook", "categoria": "Eletronicos", "preco": 2500.0, "quantidade": 5},
    {"produto": "Mouse", "categoria": "Eletronicos", "preco": 50.0, "quantidade": 100},
    {"produto": "Caderno", "categoria": "Papelaria", "preco": 15.0, "quantidade": 200},
    {"produto": "Caneta", "categoria": "Papelaria", "preco": 2.50, "quantidade": 500},
    {"produto": "Mochila", "categoria": "Acessorios", "preco": 120.0, "quantidade": 30},
    {"produto": "Teclado", "categoria": "Eletronicos", "preco": 180.0, "quantidade": 40},
    {"produto": "Fone", "categoria": "Eletronicos", "preco": 250.0, "quantidade": 25},
]

// ============================================================
// 1. FATURAMENTO TOTAL
// ============================================================
seja faturamento_total: flutuante = 0.0

para cada venda em vendas:
    faturamento_total = faturamento_total + (venda["preco"] * venda["quantidade"])

imprima("Faturamento total: R$ " + texto(faturamento_total))

// ============================================================
// 2. FATURAMENTO POR CATEGORIA
// ============================================================
imprima("--- Faturamento por categoria ---")

para cada venda em vendas:
    seja fat = venda["preco"] * venda["quantidade"]
    imprima("  " + venda["categoria"] + " | " + venda["produto"] + ": R$ " + texto(fat))

// ============================================================
// 3. PRODUTO MAIS VENDIDO (por faturamento)
// ============================================================
seja maior_faturamento: flutuante = 0.0
seja produto_top: texto = ""

para cada venda em vendas:
    seja fat = venda["preco"] * venda["quantidade"]
    se fat > maior_faturamento entao:
        maior_faturamento = fat
        produto_top = venda["produto"]

imprima("Produto top: " + produto_top + " (R$ " + texto(maior_faturamento) + ")")

// ============================================================
// 4. TICKET MEDIO POR ITEM
// ============================================================
seja total_itens: inteiro = 0

para cada venda em vendas:
    total_itens = total_itens + venda["quantidade"]

seja ticket_medio = faturamento_total / total_itens
imprima("Ticket medio por item: R$ " + texto(ticket_medio))

// ============================================================
// 5. CLASSIFICACAO DE DESEMPENHO
// ============================================================
imprima("--- Classificacao de produtos ---")

para cada venda em vendas:
    seja fat = venda["preco"] * venda["quantidade"]
    seja classificacao: texto = ""

    se fat >= 5000 entao:
        classificacao = "ESTRELA"
    senao se fat >= 1000 entao:
        classificacao = "BOM"
    senao se fat >= 500 entao:
        classificacao = "REGULAR"
    senao:
        classificacao = "BAIXO"

    imprima("  " + venda["produto"] + " -> " + classificacao)

// ============================================================
// 6. RESUMO FINAL
// ============================================================
imprima("=== RESUMO DO RELATORIO ===")
imprima("Total de produtos: " + texto(tamanho(vendas)))
imprima("Faturamento total: R$ " + texto(faturamento_total))
imprima("Produto destaque: " + produto_top)
imprima("Itens vendidos: " + texto(total_itens))

// PARABENS! Voce construiu um relatorio de vendas completo!
// proximo nivel: INTERMEDIARIO -- funcoes, classes e datasets complexos.
```
