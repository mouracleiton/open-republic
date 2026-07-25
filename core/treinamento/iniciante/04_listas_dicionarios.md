# Treinamento Iniciante 04 -- Listas e Dicionarios como Tabelas de Dados

**Nivel:** Iniciante
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 30 min

**Objetivo:** Modelar dados como listas (colunas) e dicionarios (registros).

---

```portugol++

// TREINAMENTO INICIANTE -- Licao 04: Estruturas de Dados
// ============================================================
// Em analise de dados, uma LISTA = uma coluna de tabela.
// Um DICIONARIO = uma linha (registro) com varias colunas.

// 1. LISTAS -- representando uma coluna de dados
// ------------------------------------------------------------
seja produtos = ["Arroz", "Feijao", "Acucar", "Cafe", "Leite"]
seja precos = [5.50, 8.20, 4.00, 15.90, 4.50]
seja quantidades = [100, 50, 80, 30, 200]

// Iterar com indice (enumere nos da a posicao + valor)
para cada (indice, produto) em enumere(produtos):
    imprima("Produto: " + produto)
    imprima("  Preco: R$ " + texto(precos[indice]))
    imprima("  Estoque: " + texto(quantidades[indice]) + " unidades")

// 2. CALCULAR FATURAMENTO POR PRODUTO
// ------------------------------------------------------------
seja faturamento_total: flutuante = 0.0

para cada (i, produto) em enumere(produtos):
    seja faturamento_item = precos[i] * quantidades[i]
    imprima(produto + ": R$ " + texto(faturamento_item))
    faturamento_total = faturamento_total + faturamento_item

imprima("Faturamento total: R$ " + texto(faturamento_total))

// 3. DICIONARIOS -- representando um registro (linha)
// ------------------------------------------------------------
seja cliente = {
    "nome": "Ana Beatriz",
    "idade": 28,
    "cidade": "Salvador",
    "email": "ana@email.com",
    "gasto_total": 2500.0,
}

imprima("Cliente: " + cliente["nome"])
imprima("Cidade: " + cliente["cidade"])
imprima("Gasto total: R$ " + texto(cliente["gasto_total"]))

// 4. LISTA DE DICIONARIOS -- representando uma tabela completa
// ------------------------------------------------------------
seja base_clientes = [
    {"nome": "Ana", "gasto": 2500.0, "ativo": verdadeiro},
    {"nome": "Bruno", "gasto": 300.0, "ativo": falso},
    {"nome": "Carla", "gasto": 5200.0, "ativo": verdadeiro},
    {"nome": "Diego", "gasto": 800.0, "ativo": verdadeiro},
]

// 5. FILTRAR E CALCULAR
// ------------------------------------------------------------
seja gasto_ativos: flutuante = 0.0
seja gasto_inativos: flutuante = 0.0

para cada cliente em base_clientes:
    se cliente["ativo"] == verdadeiro entao:
        gasto_ativos = gasto_ativos + cliente["gasto"]
    senao:
        gasto_inativos = gasto_inativos + cliente["gasto"]

imprima("Gasto de clientes ativos: R$ " + texto(gasto_ativos))
imprima("Gasto de clientes inativos: R$ " + texto(gasto_inativos))
imprima("Diferenca: R$ " + texto(gasto_ativos - gasto_inativos))

// EXERCICIO: crie uma lista de 5 funcionarios com salario.
// Calcule: folha total, media salarial, e quem ganha acima da media.
```
