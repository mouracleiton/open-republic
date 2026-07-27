# Treinamento Intermediario 02 -- Classes: Modelando Entidades de Dados

**Nivel:** Intermediario
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 40 min

**Objetivo:** Modelar entidades de dados (Produto, Cliente, Venda) como classes PP.

---

```portugol++

// TREINAMENTO INTERMEDIARIO -- Licao 02: Classes
// ============================================================
// Classes representam ENTIDADES do mundo real.
// Em vez de dicionarios soltos, modelamos com estrutura.

// ============================================================
// 1. CLASSE PRODUTO
// ============================================================

classe Produto:
    nome: texto
    categoria: texto
    preco: flutuante
    estoque: inteiro

    funcao faturamento_potencial(self) -> flutuante:
        retorne self.preco * self.estoque

    funcao classificar(self) -> texto:
        se self.faturamento_potencial() >= 10000 entao:
            retorne "ALTO IMPACTO"
        senao se self.faturamento_potencial() >= 1000 entao:
            retorne "IMPACTO MEDIO"
        senao:
            retorne "BAIXO IMPACTO"

    funcao resumo(self) -> texto:
        retorne self.nome + " [" + self.categoria + "] -- " + texto(self.preco) + " x " + texto(self.estoque) + " = " + texto(self.faturamento_potencial())


// ============================================================
// 2. CLASSE CLIENTE
// ============================================================

classe Cliente:
    nome: texto
    email: texto
    cidade: texto
    gasto_total: flutuante
    pedidos: inteiro

    funcao ticket_medio(self) -> flutuante:
        se self.pedidos > 0 entao:
            retorne self.gasto_total / self.pedidos
        retorne 0.0

    funcao segmento(self) -> texto:
        se self.gasto_total >= 5000 entao:
            retorne "VIP"
        senao se self.gasto_total >= 1000 entao:
            retorne "PREMIUM"
        senao:
            retorne "REGULAR"


// ============================================================
// 3. CLASSE VENDA
// ============================================================

classe Venda:
    produto: Produto
    cliente: Cliente
    quantidade: inteiro
    data: texto

    funcao valor_total(self) -> flutuante:
        retorne self.produto.preco * self.quantidade


// ============================================================
// 4. INSTANCIANDO E ANALISANDO
// ============================================================

seja notebook = Produto()
notebook.nome = "Notebook OpenRepublic"
notebook.categoria = "Eletronicos"
notebook.preco = 2500.0
notebook.estoque = 10

seja mouse = Produto()
mouse.nome = "Mouse Gamer"
mouse.categoria = "Eletronicos"
mouse.preco = 80.0
mouse.estoque = 50

seja ana = Cliente()
ana.nome = "Ana Beatriz"
ana.email = "ana@email.com"
ana.cidade = "Salvador"
ana.gasto_total = 5200.0
ana.pedidos = 12

imprima(notebook.resumo())
imprima("Classificacao: " + notebook.classificar())
imprima("Cliente: " + ana.nome + " -- Segmento: " + ana.segmento())
imprima("Ticket medio: R$ " + texto(ana.ticket_medio()))

// EXERCICIO: crie a classe Pedido com lista de produtos,
// metodo valor_total() e metodo adicionar_produto().
```
