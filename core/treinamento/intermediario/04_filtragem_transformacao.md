# Treinamento Intermediario 04 -- Filtragem e Transformacao de Dados

**Nivel:** Intermediario
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 40 min

**Objetivo:** Filtrar, ordenar e transformar datasets como um analyst faria.

---

```portugol++

// TREINAMENTO INTERMEDIARIO -- Licao 04: Filtragem e Transformacao
// ============================================================
// O dia a dia do analista: pegar dados crus, filtrar, transformar,
// ordenar e preparar para relatorios.

// ============================================================
// DATASET DE EXEMPLO
// ============================================================

seja funcionarios = [
    {"nome": "Ana", "depto": "Engenharia", "salario": 8000.0, "anos": 5},
    {"nome": "Bruno", "depto": "Vendas", "salario": 3500.0, "anos": 2},
    {"nome": "Carla", "depto": "Engenharia", "salario": 9500.0, "anos": 7},
    {"nome": "Diego", "depto": "RH", "salario": 4200.0, "anos": 3},
    {"nome": "Elena", "depto": "Vendas", "salario": 5000.0, "anos": 4},
    {"nome": "Felipe", "depto": "Engenharia", "salario": 7000.0, "anos": 4},
    {"nome": "Gabi", "depto": "RH", "salario": 3800.0, "anos": 1},
    {"nome": "Hugo", "depto": "Vendas", "salario": 6200.0, "anos": 6},
]


// ============================================================
// 1. FILTRAR POR CONDICAO
// ============================================================

funcao filtrar_por_depto(dados: [Dict], depto: texto) -> [Dict]:
    seja resultado: [Dict] = []
    para cada f em dados:
        se f["depto"] == depto entao:
            resultado.adicione(f)
    retorne resultado


funcao filtrar_por_salario(dados: [Dict], minimo: flutuante) -> [Dict]:
    seja resultado: [Dict] = []
    para cada f em dados:
        se f["salario"] >= minimo entao:
            resultado.adicione(f)
    retorne resultado


// Aplicando filtros
seja engenharia = filtrar_por_depto(funcionarios, "Engenharia")
imprima("Engenharia: " + texto(tamanho(engenharia)) + " pessoas")

seja alta_renda = filtrar_por_salario(funcionarios, 6000.0)
imprima("Salario >= R$ 6000: " + texto(tamanho(alta_renda)) + " pessoas")


// ============================================================
// 2. AGRUPAR E CONTAR
// ============================================================

funcao contar_por_depto(dados: [Dict]) -> Dict:
    seja grupos = {}
    para cada f em dados:
        seja depto = f["depto"]
        se depto em grupos entao:
            grupos[depto] = grupos[depto] + 1
        senao:
            grupos[depto] = 1
    retorne grupos


seja distribuicao = contar_por_depto(funcionarios)
imprima("Distribuicao por departamento:")
para cada (depto, count) em distribuicao:
    imprima("  " + depto + ": " + texto(count))


// ============================================================
// 3. CALCULAR CAMPO DERIVADO (transformacao)
// ============================================================

// Adicionar campo "bonus" = 1 mes de salario por ano trabalhado
funcao calcular_bonuses(dados: [Dict]) -> [Dict]:
    seja resultado: [Dict] = []
    para cada f em dados:
        seja bonus = f["salario"] * f["anos"] * 0.1
        f["bonus"] = bonus
        resultado.adicione(f)
    retorne resultado


seja com_bonus = calcular_bonuses(funcionarios)
imprima("--- Bonus calculado ---")
para cada f em com_bonus:
    imprima("  " + f["nome"] + ": bonus R$ " + texto(f["bonus"]))


// ============================================================
// 4. ORDENAR POR CAMPO (selection sort)
// ============================================================

funcao ordenar_por_salario(dados: [Dict]) -> [Dict]:
    seja resultado = dados
    seja n = tamanho(resultado)
    para cada i em intervalo(n):
        seja min_idx = i
        para cada j em intervalo(i + 1, n):
            se resultado[j]["salario"] < resultado[min_idx]["salario"] entao:
                min_idx = j
        seja temp = resultado[i]
        resultado[i] = resultado[min_idx]
        resultado[min_idx] = temp
    retorne resultado


seja ordenados = ordenar_por_salario(funcionarios)
imprima("--- Ranking salarial (menor -> maior) ---")
para cada f em ordenados:
    imprima("  " + f["nome"] + " (" + f["depto"] + "): R$ " + texto(f["salario"]))

// EXERCICIO: crie uma funcao que calcula a folha salarial total
// por departamento e retorna um dicionario {depto: total}.
```
