# OpenRepublic -- Politica: Fim das Baterias Descartaveis

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/battery_policy.py`

**Descricao:** =========================================================
"Pilha jogada no lixo e 100 anos de chumbo no solo.
 Bateria reparavel e 15 anos de uso.
 A Republica escolhe 15 anos."
PROIBIR:
  - Pilhas alcalinas descartaveis (AA, AAA, C, D, 9V)
  - Pilhas de botao descartaveis (relogio, chaveiro)
  - Baterias de litio seladas (nao abertas, nao reparaveis)
  - Baterias de chumbo-acido sem manutencao
  - Power banks selados (sem troca de celula)
  - Bateria embutida com cola (plano de obsolescencia)
OBRIGATORIO:
  - TUDO que usa energia usa celula 18650 ou 21700
  - TUDO tem compartimento aberto (sem cola, sem parafuso pentalobe)
  - TUDO permite troca de celula individual
  - Bateria de dispositivo = N celulas padrão, nao bateria unica selada
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Politica: Fim das Baterias Descartaveis
=========================================================

"Pilha jogada no lixo e 100 anos de chumbo no solo.
 Bateria reparavel e 15 anos de uso.
 A Republica escolhe 15 anos."

PROIBIR:
  - Pilhas alcalinas descartaveis (AA, AAA, C, D, 9V)
  - Pilhas de botao descartaveis (relogio, chaveiro)
  - Baterias de litio seladas (nao abertas, nao reparaveis)
  - Baterias de chumbo-acido sem manutencao
  - Power banks selados (sem troca de celula)
  - Bateria embutida com cola (plano de obsolescencia)

OBRIGATORIO:
  - TUDO que usa energia usa celula 18650 ou 21700
  - TUDO tem compartimento aberto (sem cola, sem parafuso pentalobe)
  - TUDO permite troca de celula individual
  - Bateria de dispositivo = N celulas padrão, nao bateria unica selada

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections


classe BatteryType herda de Enum:
    // Tipos de bateria/pilha.
    // PROIBIDOS
    ALKALINE_AA = "alcalina_aa"
    ALKALINE_AAA = "alcalina_aaa"
    ALKALINE_C = "alcalina_c"
    ALKALINE_D = "alcalina_d"
    ALKALINE_9V = "alcalina_9v"
    BUTTON_CELL = "botao_descartavel"
    SEALED_LIPO = "lipo_selada"  // colada, nao abre
    SEALED_LION = "lion_selada"  // selada, nao abre
    LEAD_ACID_SEALED = "chumbo_selada"
    // PERMITIDOS
    CELL_18650 = "celula_18650"  // padrao Republica
    CELL_21700 = "celula_21700"  // padrao Republica
    CELL_26650 = "celula_26650"  // alta capacidade
    LEAD_ACID_SERVICEABLE = "chubo_manutencao"
    LIFePO4 = "lifepo4_modular"  // ferro-fosfato (segura, longa vida)
    SUPERCAPACITOR = "supercapacitor"
    SAND_BATTERY = "areia"  // armazenamento termico
    GRAVITY = "gravidade"  // armazenamento mecanico


classe BatteryStatus herda de Enum:
    PROHIBITED = "proibida"
    PHASE_OUT = "descontinuar"
    PERMITTED = "permitida"
    PREFERRED = "preferida"
    MANDATORY = "obrigatoria"


// decorador: @dataclass
classe BatterySpec:
    // Especificacao de um tipo de bateria.
    btype: BatteryType
    status: BatteryStatus
    seja chemistry: texto = ""
    seja voltage_nominal: flutuante = 0
    seja capacity_mah: inteiro = 0
    seja cycles: inteiro = 0 // ciclos de carga ate 80% capacidade
    seja lifespan_years: flutuante = 0
    seja repairable: logico = falso // pode trocar celula individual?
    seja recyclable_pct: flutuante = 0 // % recuperavel
    seja toxic_materials: [texto] = field(default_factory=list)
    seja co2_manufacture_kg: flutuante = 0
    seja cost_recovery_credits: inteiro = 0 // creditos para recuperar na reciclagem
    seja notes: texto = ""


seja BATTERY_DATABASE: {BatteryType: BatterySpec} = {

    // === PROIBIDAS ===
    BatteryType.ALKALINE_AA: BatterySpec(
        BatteryType.ALKALINE_AA, BatteryStatus.PROHIBITED,
        "Zn/MnO2", 1.5, 2500, 0, 0, falso, 30,
        toxic_materials = ["zinco", "manganes", "potassio"],
        co2_manufacture_kg = 0.5, notes="Descartavel. 100 anos no solo. PROIBIDA."),

    BatteryType.ALKALINE_AAA: BatterySpec(
        BatteryType.ALKALINE_AAA, BatteryStatus.PROHIBITED,
        "Zn/MnO2", 1.5, 1000, 0, 0, falso, 30,
        toxic_materials = ["zinco", "manganes"],
        co2_manufacture_kg = 0.3, notes="Descartavel. PROIBIDA."),

    BatteryType.BUTTON_CELL: BatterySpec(
        BatteryType.BUTTON_CELL, BatteryStatus.PROHIBITED,
        "Zn-Ar/Li", 3.0, 200, 0, 0, falso, 20,
        toxic_materials = ["litio", "mercurio (algumas)"],
        co2_manufacture_kg = 0.2, notes="Criancas engolem. PROIBIDA."),

    BatteryType.SEALED_LIPO: BatterySpec(
        BatteryType.SEALED_LIPO, BatteryStatus.PROHIBITED,
        "Li-Po selada", 3.7, 3000, 500, 2, falso, 50,
        toxic_materials = ["litio", "cobalto", "eletrólito inflamavel"],
        co2_manufacture_kg = 5.0,
        notes = "Colada com adesivo. Plano de obsolescencia. PROIBIDA."),

    BatteryType.SEALED_LION: BatterySpec(
        BatteryType.SEALED_LION, BatteryStatus.PROHIBITED,
        "Li-ion selada", 3.7, 2500, 800, 3, falso, 60,
        toxic_materials = ["litio", "cobalto"],
        co2_manufacture_kg = 4.5,
        notes = "Bateria de smartphone colada. PROIBIDA na Republica."),

    BatteryType.LEAD_ACID_SEALED: BatterySpec(
        BatteryType.LEAD_ACID_SEALED, BatteryStatus.PROHIBITED,
        "Pb SLA", 12.0, 5000, 300, 3, falso, 95,
        toxic_materials = ["chumbo", "acido sulfurico"],
        co2_manufacture_kg = 8.0,
        notes = "Chumbo selado. Reciclavel mas toxico. Descontinuar."),

    // === PERMITIDAS / PREFERIDAS ===
    BatteryType.CELL_18650: BatterySpec(
        BatteryType.CELL_18650, BatteryStatus.MANDATORY,
        "Li-ion 18650", 3.7, 3500, 1000, 5, verdadeiro, 95,
        toxic_materials = ["litio (recuperavel)"],
        co2_manufacture_kg = 1.5, cost_recovery_credits=1,
        notes = "PADRAO DA REPUBLICA. Cilindro aberto. Troca individual."),

    BatteryType.CELL_21700: BatterySpec(
        BatteryType.CELL_21700, BatteryStatus.MANDATORY,
        "Li-ion 21700", 3.7, 5000, 1500, 8, verdadeiro, 95,
        toxic_materials = ["litio (recuperavel)"],
        co2_manufacture_kg = 2.0, cost_recovery_credits=1,
        notes = "PADRAO ALTA CAPACIDADE. Tesla usa estas. 8 anos."),

    BatteryType.CELL_26650: BatterySpec(
        BatteryType.CELL_26650, BatteryStatus.PREFERRED,
        "LiFePO4 26650", 3.2, 4000, 3000, 15, verdadeiro, 98,
        toxic_materials = [],
        co2_manufacture_kg = 2.5, cost_recovery_credits=2,
        notes = "LiFePO4: 3000 ciclos, 15 anos, NAO toxica."),

    BatteryType.LIFePO4: BatterySpec(
        BatteryType.LIFePO4, BatteryStatus.PREFERRED,
        "LiFePO4 modular", 3.2, 10000, 6000, 20, verdadeiro, 98,
        toxic_materials = [],
        co2_manufacture_kg = 3.0, cost_recovery_credits=3,
        notes = "Ferro-fosfato. Mais segura (nao pega fogo). 20 anos."),

    BatteryType.SUPERCAPACITOR: BatterySpec(
        BatteryType.SUPERCAPACITOR, BatteryStatus.PREFERRED,
        "EDLC", 2.7, 300, 100000, 30, verdadeiro, 100,
        toxic_materials = [],
        co2_manufacture_kg = 1.0,
        notes = "100.000 ciclos. 30 anos. Carbono puro. Zero toxico."),

    BatteryType.SAND_BATTERY: BatterySpec(
        BatteryType.SAND_BATTERY, BatteryStatus.PREFERRED,
        "Silica termica", 0, 0, 99999, 50, verdadeiro, 100,
        toxic_materials = [],
        co2_manufacture_kg = 0.5,
        notes = "Areia quente. 50 anos. Zero toxico. Armazenamento sazonal."),

    BatteryType.GRAVITY: BatterySpec(
        BatteryType.GRAVITY, BatteryStatus.PREFERRED,
        "Concreto + gravidade", 0, 0, 99999, 40, verdadeiro, 100,
        toxic_materials = [],
        co2_manufacture_kg = 2.0,
        notes = "Erguer peso. 40 anos. Sem quimica. Armazenamento comunitario."),
}


// ============================================================================
// Product Compliance Checker
// ============================================================================

// decorador: @dataclass
classe Product:
    // Um produto que usa bateria.
    name: texto
    battery_type: BatteryType
    seja battery_count: inteiro = 1
    seja battery_replaceable: logico = falso
    seja glued: logico = falso
    seja expected_life_years: flutuante = 0


classe BatteryPolicy:
    // Politica de bateria da Republica.

    REGRAS:
    1. PROIBIDAS: pilhas descartaveis, baterias coladas
    2. OBRIGATORIAS: 18650/21700 para dispositivos portateis
    3. PREFERIDAS: LiFePO4, supercapacitor, areia, gravidade
    4. TODO dispositivo tem compartimento ABERTO (sem cola)
    5. TODO dispositivo permite troca de celula INDIVIDUAL
    // 

    funcao __init__(self):
        self.db = BATTERY_DATABASE

    funcao check_product(self, product: Product) -> {texto: qualquer}:
        // Verificar se produto cumpre a politica.
        spec = self.db.get(product.battery_type)

        se nao spec entao:
            retorne {"verdict": "DESCONHECIDO", "allowed": falso,
                    "reason": "Tipo {product.battery_type.value} nao catalogado"}

        // Verificar se e proibida
        se spec.status == BatteryStatus.PROHIBITED entao:
            retorne {
                "product": product.name,
                "battery": product.battery_type.value,
                "verdict": "PROIBIDO",
                "allowed": falso,
                "reason": ("{product.battery_type.value} e PROIBIDA na Republica. "
                          "Substituir por celula 18650 ou 21700. "
                          "Razao: {spec.notes}"),
                "impact": ("CO2 de fabricacao: {spec.co2_manufacture_kg}kg/unidade. "
                          "Vida util: {spec.lifespan_years} anos (descartavel). "
                          "Toxicos: {', '.join(spec.toxic_materials) if spec.toxic_materials else 'nenhum'}"),
            }

        // Verificar se e colada
        se product.glued entao:
            retorne {
                "product": product.name,
                "verdict": "PROIBIDO",
                "allowed": falso,
                "reason": "Bateria colada = plano de obsolescencia. "
                         "PROIBIDO. Todo dispositivo tem compartimento ABERTO.",
            }

        // Verificar se e substituivel
        se nao product.battery_replaceable e spec.status != BatteryStatus.PROHIBITED entao:
            retorne {
                "product": product.name,
                "verdict": "NAO CONFORME",
                "allowed": falso,
                "reason": "Bateria nao substituivel. Deve permitir troca manual.",
            }

        // Conforme
        retorne {
            "product": product.name,
            "battery": product.battery_type.value,
            "verdict": "CONFORME",
            "allowed": verdadeiro,
            "status": spec.status.value,
            "lifespan_years": spec.lifespan_years,
            "cycles": spec.cycles,
            "recyclable_pct": spec.recyclable_pct,
            spec.toxic_materials ? "toxic": spec.toxic_materials : "nenhum",
            "recovery_credits": spec.cost_recovery_credits,
            "reason": "OK. {spec.notes}",
        }

    funcao recommend_replacement(self, prohibited_type: BatteryType) -> {texto: qualquer}:
        // Recomendar substituicao para bateria proibida.
        spec = self.db.get(prohibited_type)

        se nao spec ou spec.status != BatteryStatus.PROHIBITED entao:
            retorne {"error": "nao e proibida"}

        // Map de substituicao
        replacements = {
            BatteryType.ALKALINE_AA: ("CELL_18650", "1x 18650 + step-up substitui 2x AA"),
            BatteryType.ALKALINE_AAA: ("CELL_18650", "1x 18650 + step-down substitui 3x AAA"),
            BatteryType.BUTTON_CELL: ("SUPERCAPACITOR", "supercapacitor + solar recarrega"),
            BatteryType.SEALED_LIPO: ("CELL_18650", "1x 18650 substitui 1x LiPo selada"),
            BatteryType.SEALED_LION: ("CELL_18650", "2x 18650 substitui bateria smartphone"),
            BatteryType.LEAD_ACID_SEALED: ("LIfePO4", "banco LiFePO4 modular substitui chumbo"),
        }

        rec = replacements.get(prohibited_type, ("CELL_18650", "padrao universal"))
        retorne {
            "prohibited": prohibited_type.value,
            "replacement": rec[0],
            "how": rec[1],
            "lifespan_gain": "de {spec.lifespan_years} anos para 5-15 anos",
            "recycle_gain": "de {spec.recyclable_pct}% para 95-100%",
        }

    funcao impact_report(self, population: inteiro = 1_000_000) -> {texto: qualquer}:
        // Calcular impacto de eliminar pilhas descartaveis.
        // Brasileiro usa ~20 pilhas/ano
        pilhas_per_person_year = 20
        total_pilhas = population * pilhas_per_person_year

        // Dados por pilha alcalina
        co2_per_pilha = 0.4 // kg CO2 fabricacao + descarte
        toxic_per_pilha = 0.003 // kg de material toxico

        total_co2 = total_pilhas * co2_per_pilha
        total_toxic = total_pilhas * toxic_per_pilha

        // Com 18650: 1 celula substitui ~100 pilhas (5 anos x 20/ano)
        cells_needed = total_pilhas / 100
        co2_cells = cells_needed * 1.5 // kg CO2 por 18650

        co2_savings = total_co2 - co2_cells

        retorne {
            "population": population,
            "pilhas_descartadas_ano": total_pilhas,
            "co2_evitado_ton": arredonde(co2_savings / 1000),
            "material_toxico_evitado_ton": arredonde(total_toxic / 1000, 1),
            "celulas_18650_necessarias": inteiro(cells_needed),
            "comparacao": (
                "Em vez de {total_pilhas:,} pilhas descartaveis/ano "
                "({total_co2:,.0f} kg CO2), "
                "usar {int(cells_needed):,} celulas 18650 ({co2_cells:,.0f} kg CO2). "
                "Economia: {co2_savings/1000:,.0f} toneladas CO2/ano."
            ),
        }


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 75)
    imprima("  OPENREPUBLIC -- FIM DAS BATERIAS DESCARTAVEIS")
    imprima("  'Pilha no lixo = 100 anos de veneno.'")
    imprima("  'Bateria reparavel = 15 anos de uso.'")
    imprima("=" * 75)

    policy = BatteryPolicy()

    // === 1. Battery Database ===
    imprima("\n\n  === BANCO DE BATERIAS ===\n")
    imprima("  {'Tipo':<20} {'Status':<14} {'Vida':>5} {'Ciclos':>7} {'Recicl.':>8} {'Toxico'}")
    imprima("  {'-'*75}")
    para cada (bt, spec) em BATTERY_DATABASE.items():
        toxic = spec.toxic_materials ? "SIM" : "nao"
        imprima("  {bt.value:<20} {spec.status.value:<14} "
              "{spec.lifespan_years:>4.0f}a {spec.cycles:>7} "
              "{spec.recyclable_pct:>7}% {toxic:>6}")

    // === 2. Product Compliance ===
    imprima("\n\n  === VERIFICACAO DE PRODUTOS ===\n")

    products = [
        Product("Controle remoto", BatteryType.ALKALINE_AAA, 2, verdadeiro, falso),
        Product("Smartphone Republica", BatteryType.CELL_18650, 1, verdadeiro, falso),
        Product("iPhone (legado)", BatteryType.SEALED_LION, 1, falso, verdadeiro),
        Product("Lanterna FabLab", BatteryType.CELL_18650, 1, verdadeiro, falso),
        Product("Relogio pulso", BatteryType.BUTTON_CELL, 1, verdadeiro, falso),
        Product("Lanterna antiga", BatteryType.ALKALINE_AA, 4, verdadeiro, falso),
        Product("Power bank Republica", BatteryType.CELL_21700, 4, verdadeiro, falso),
        Product("Banco energia solar", BatteryType.LIFePO4, 8, verdadeiro, falso),
        Product("UPS comunitaria", BatteryType.LEAD_ACID_SEALED, 1, falso, falso),
    ]

    para cada p em products:
        result = policy.check_product(p)
        verdict = result["verdict"]
        ok = result["allowed"] ? "OK" : "BLOQUEADO"
        imprima("\n  {p.name}:")
        imprima("    Bateria: {p.battery_type.value} x{p.battery_count}")
        imprima("    Substituivel: {'sim' if p.battery_replaceable else 'NAO'} | "
              "Colada: {'sim' if p.glued else 'nao'}")
        imprima("    Veredito: {ok} ({verdict})")
        imprima("    Razao: {result['reason'][:80]}")

    // === 3. Replacement Recommendations ===
    imprima("\n\n  === SUBSTITUICOES RECOMENDADAS ===\n")

    prohibited_types = [BatteryType.ALKALINE_AA, BatteryType.ALKALINE_AAA,
                       BatteryType.BUTTON_CELL, BatteryType.SEALED_LION,
                       BatteryType.SEALED_LIPO, BatteryType.LEAD_ACID_SEALED]

    para cada pt em prohibited_types:
        rec = policy.recommend_replacement(pt)
        imprima("\n  {rec['prohibited']:<20} -> {rec['replacement']}")
        imprima("    Como: {rec['how']}")
        imprima("    Ganho: {rec['lifespan_gain']}")
        imprima("    Reciclavel: {rec['recycle_gain']}")

    // === 4. Impact Report ===
    imprima("\n\n  === IMPACTO AMBIENTAL ===\n")

    para cada pop em [10_000, 100_000, 1_000_000]:
        impact = policy.impact_report(pop)
        imprima("\n  Populacao: {pop:,}")
        imprima("    {impact['comparacao']}")
        imprima("    CO2 evitado: {impact['co2_evitado_ton']:,} toneladas/ano")
        imprima("    Material toxico evitado: {impact['material_toxico_evitado_ton']} ton/ano")

    // === Philosophy ===
    imprima("\n\n{'='*75}")
    imprima("  PRINCIPIOS")
    imprima("{'='*75}")
    imprima("""
  BATERIA TRADICIONAL BATERIA REPUBLICA
  --------------------------------------- ---------------------------------------
  Pilha descartavel (use e jogue) Celula 18650 (use e recarregue)
  Colada com adesivo (nao abre) Compartimento parafusado (abre)
  Bateria unica selada (obsoleta) N celulas individuais (troca uma)
  2-3 anos de vida 5-15 anos de vida
  50% reciclavel 95-100% reciclavel
  Plano de obsolescencia Plano de LONGEVIDADE
  Fabricante lucra com troca Republica nao lucra (sem dinheiro)
  Chumbo/cobalto/mercurio no solo Zero toxico (LiFePO4)
  Comprada ($) Recuperada de e-waste (OpenReverseLogistics)

  O QUE e PROIBIDO:
    - Pilhas alcalinas (AA, AAA, C, D, 9V)
    - Pilhas de botao descartaveis
    - Baterias coladas (smartphone, tablet, laptop)
    - Baterias seladas sem manutencao
    - Power banks sem troca de celula

  O QUE e OBRIGATORIO:
    - Celula 18650 ou 21700 para portateis
    - LiFePO4 para estacionario
    - Supercapacitor para alta potencia/curta duracao
    - Areia/gravidade para armazenamento comunitario

  O QUE e PREFERIDO:
    - LiFePO4 (ferro-fosfato): 6000 ciclos, 20 anos, nao pega fogo
    - Supercapacitor: 100.000 ciclos, 30 anos, carbono puro
    - Areia: 50 anos, zero toxico, armazenamento sazonal
    - Gravidade: 40 anos, sem quimica, armazenamento macro

  PARA TODA BATERIA:
    - Compartimento ABERTO (sem cola, sem pentalobe)
    - Troca de celula INDIVIDUAL (uma falha nao mata o banco)
    - Recuperacao de e-waste (OpenReverseLogistics)
    - Reciclagem ao fim da vida (95-100% recuperavel)

  "Pilha descartavel e veneno com prazo de validade.
   Bateria reparavel e responsabilidade com futuro.
   A Republica escolhe o futuro."
// )

```
