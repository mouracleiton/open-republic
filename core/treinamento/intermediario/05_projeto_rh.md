# Treinamento Intermediario 05 -- Projeto: Dashboard de Recursos Humanos

**Nivel:** Intermediario
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 50 min

**Objetivo:** Construir um sistema de RH completo usando funcoes, classes e estatistica.

---

```portugol++

// TREINAMENTO INTERMEDIARIO -- Licao 05: Projeto Dashboard RH
// ============================================================
// Projeto final intermediario: sistema de analise de RH
// Combina: classes, funcoes, filtros, estatistica, transformacao

// ============================================================
// CLASSES DE DOMINIO
// ============================================================

classe Funcionario:
    nome: texto
    departamento: texto
    cargo: texto
    salario: flutuante
    anos_empresa: inteiro
    performance: flutuante  // 0.0 a 5.0

    funcao bonus_anual(self) -> flutuante:
        retorne self.salario * (self.anos_empresa * 0.05) + (self.salario * self.performance * 0.1)

    funcao nivel(self) -> texto:
        se self.anos_empresa >= 5 entao:
            retorne "Senior"
        senao se self.anos_empresa >= 2 entao:
            retorne "Pleno"
        senao:
            retorne "Junior"

    funcao resumo(self) -> texto:
        retorne self.nome + " | " + self.nivel() + " | " + self.departamento + " | R$ " + texto(self.salario) + " | Perf: " + texto(self.performance)


classe Departamento:
    nome: texto
    funcionarios: [Funcionario] = []

    funcao folha_total(self) -> flutuante:
        seja total: flutuante = 0.0
        para cada f em self.funcionarios:
            total = total + f.salario
        retorne total

    funcao salario_medio(self) -> flutuante:
        se tamanho(self.funcionarios) == 0 entao:
            retorne 0.0
        retorne self.folha_total() / tamanho(self.funcionarios)

    funcao performance_media(self) -> flutuante:
        se tamanho(self.funcionarios) == 0 entao:
            retorne 0.0
        seja soma: flutuante = 0.0
        para cada f em self.funcionarios:
            soma = soma + f.performance
        retorne soma / tamanho(self.funcionarios)

    funcao melhor_funcionario(self) -> Funcionario:
        seja melhor = self.funcionarios[0]
        para cada f em self.funcionarios:
            se f.performance > melhor.performance entao:
                melhor = f
        retorne melhor


// ============================================================
// DADOS DE EXEMPLO
// ============================================================

seja ana = Funcionario()
ana.nome = "Ana Souza"
ana.departamento = "Engenharia"
ana.cargo = "Tech Lead"
ana.salario = 12000.0
ana.anos_empresa = 6
ana.performance = 4.8

seja bruno = Funcionario()
bruno.nome = "Bruno Lima"
bruno.departamento = "Engenharia"
bruno.cargo = "Developer"
bruno.salario = 7000.0
bruno.anos_empresa = 3
bruno.performance = 4.2

seja carla = Funcionario()
carla.nome = "Carla Mendes"
carla.departamento = "Vendas"
carla.cargo = "Gerente"
carla.salario = 9000.0
carla.anos_empresa = 5
carla.performance = 4.5

seja diego = Funcionario()
diego.nome = "Diego Santos"
diego.departamento = "Vendas"
diego.cargo = "Vendedor"
diego.salario = 4000.0
diego.anos_empresa = 2
diego.performance = 3.8


// ============================================================
// DASHBOARD
// ============================================================

seja engenharia = Departamento()
engenharia.nome = "Engenharia"
engenharia.funcionarios = [ana, bruno]

seja vendas = Departamento()
vendas.nome = "Vendas"
vendas.funcionarios = [carla, diego]

imprima("============================================================")
imprima("           DASHBOARD DE RECURSOS HUMANOS")
imprima("============================================================")

imprima("\n--- POR DEPARTAMENTO ---")
imprima("Engenharia:")
imprima("  Pessoas: " + texto(tamanho(engenharia.funcionarios)))
imprima("  Folha: R$ " + texto(engenharia.folha_total()))
imprima("  Salario medio: R$ " + texto(engenharia.salario_medio()))
imprima("  Performance media: " + texto(engenharia.performance_media()))
imprima("  Destaque: " + engenharia.melhor_funcionario().nome)

imprima("\nVendas:")
imprima("  Pessoas: " + texto(tamanho(vendas.funcionarios)))
imprima("  Folha: R$ " + texto(vendas.folha_total()))
imprima("  Salario medio: R$ " + texto(vendas.salario_medio()))
imprima("  Performance media: " + texto(vendas.performance_media()))
imprima("  Destaque: " + vendas.melhor_funcionario().nome)

imprima("\n--- BONUS ANUAL PROJETADO ---")
seja todos = [ana, bruno, carla, diego]
para cada f em todos:
    imprima("  " + f.nome + ": R$ " + texto(f.bonus_anual()))

imprima("\n--- RESUMO INDIVIDUAL ---")
para cada f em todos:
    imprima("  " + f.resumo())

imprima("\n============================================================")
imprima("Analise concluida. Proximo nivel: AVANCADO.")
imprima("============================================================")
```
