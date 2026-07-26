# OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?

**Arquivo original:** `open-republic/core/open_debt_mortality.py`

**Descricao:** ==========================================================
"Cada R$ 1 bilhao pago em juros e:
- 2 hospitais que nao foram construidos
- 50 mil casas populares que nao foram entregues
- 200 mil cestas de comida que nao foram distribuidas
- 10 mil bolsas universitarias que nao foram concedidas
E esses hospitais, casas, comidas e bolsas que NAO EXISTEM
porque o dinheiro foi pro agiota -- essas sao as PESSOAS que morrem.
O juros da divida MATA. MATA de forma invisivel.
Nao e uma bala. E a AUSENCIA de um medico.
Nao e uma faca. E a AUSENCIA de comida na mesa.
Nao e um tiro. E a AUSENCIA de saneamento basico.
Este modulo calcula, ano a ano, quantas pessoas MORREM
no Brasil porque o dinheiro que deveria salvar suas vidas
foi enviado para o agiota international como 'juros da divida'.
METODOLOGIA:
- Calcular juros pagos por ano (R$ bilhoes)
- Calcular quanto disso deveria ir para saude, comida, saneamento
- Calcular mortes evitaveis por falta de cada recurso
- Comparar: se nao pagasse a divida, quantas vidas seriam salvas?
AS MORTES NAO SAO ABSTRATAS. SAO NOMES. SAO CRIANCAS.
Sao os 124 mil brasileiros que morrem por ano por causas evitaveis
no SUS subfinanciado. Sao as criancas desnutridas no Nordeste.
Sao os idosos sem atendimento na fila do SUS.
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol

// !/usr/bin/env python3
// 
OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?
==========================================================
"Cada R$ 1 bilhao pago em juros e:
- 2 hospitais que nao foram construidos
- 50 mil casas populares que nao foram entregues
- 200 mil cestas de comida que nao foram distribuidas
- 10 mil bolsas universitarias que nao foram concedidas

E esses hospitais, casas, comidas e bolsas que NAO EXISTEM
porque o dinheiro foi pro agiota -- essas sao as PESSOAS que morrem.

O juros da divida MATA. MATA de forma invisivel.
Nao e uma bala. E a AUSENCIA de um medico.
Nao e uma faca. E a AUSENCIA de comida na mesa.
Nao e um tiro. E a AUSENCIA de saneamento basico.

Este modulo calcula, ano a ano, quantas pessoas MORREM
no Brasil porque o dinheiro que deveria salvar suas vidas
foi enviado para o agiota international como 'juros da divida'.

METODOLOGIA:
- Calcular juros pagos por ano (R$ bilhoes)
- Calcular quanto disso deveria ir para saude, comida, saneamento
- Calcular mortes evitaveis por falta de cada recurso
- Comparar: se nao pagasse a divida, quantas vidas seriam salvas?

AS MORTES NAO SAO ABSTRATAS. SAO NOMES. SAO CRIANCAS.
Sao os 124 mil brasileiros que morrem por ano por causas evitaveis
no SUS subfinanciado. Sao as criancas desnutridas no Nordeste.
Sao os idosos sem atendimento na fila do SUS.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa math


// ============================================================================
// 1. CAUSAS DE MORTE EVITAVEIS (vinculadas a subfinanciamento)
// ============================================================================

classe PreventableDeathCategory herda de Enum:
    // Categorias de morte evitaveis por investimento publico.
    HEALTHCARE_SHORTAGE <- "falta_sus"  // morreu na fila do SUS
    CHILD_MORTALITY <- "mortalidade_infantil"  // bebe nao sobreviveu
    MATERNAL_DEATH <- "morte_materna"  // mae morreu no parto
    MALNUTRITION <- "desnutricao"  // morreu de fome
    PREVENTABLE_DISEASE <- "doenca_evitavel"  // vacina/exame nao chegou
    VIOLENCE <- "violencia"  // sem programa social
    SUICIDE <- "suicidio"  // sem saude mental
    SANITATION <- "saneamento"  // agua contaminada
    ROAD_DEATH <- "transito"  // estrada sem manutencao
    HEAT_COLD <- "calor_frio"  // sem teto/climatizacao
    DRUG_OVERDOSE <- "overdose"  // sem tratamento
    CANCER_UNTREATED <- "cancer_sem_tratamento"  // fila de quimio
    HEART_UNTREATED <- "coracao_sem_atendimento"  // sem UTI
    NEONATAL <- "neonatal"  // sem UTI neonatal


// decorador: @dataclass
classe DeathCost:
    // Custo de salvar uma vida em cada categoria.
    category: PreventableDeathCategory
    name: str
    cost_to_save_one_life_brl: float     // quanto custa prevenir UMA morte
    deaths_per_year_brazil: int          // mortes/ano no Brasil hoje
    pct_linked_to_underfunding: float    // % que seria evitada com dinheiro
    declare description: str  <- ""

    funcao deaths_preventable(self) retorna int:
        // Mortes que DA pra evitar com investimento.
        retorne int(self.deaths_per_year_brazil * self.pct_linked_to_underfunding)

    funcao lives_saved_per_billion(self) retorna float:
        // Quantas vidas R$ 1 bilhao salva nesta categoria.
        se self.cost_to_save_one_life_brl <= 0 entao:
            retorne 0
        retorne 1e9 / self.cost_to_save_one_life_brl


// ============================================================================
// 2. TABELA DE MORTALIDADE (Dados baseados em OMS/IBGE/Datasus)
// ============================================================================

declare DEATH_COSTS: List[DeathCost]  <- [
    DeathCost(
        PreventableDeathCategory.HEALTHCARE_SHORTAGE,
        "Morte na fila do SUS",
        cost_to_save_one_life_brl <- 500_000,  // UTI + cirurgia por pessoa
        deaths_per_year_brazil <- 124_000,  // mortes evitaveis no SUS
        pct_linked_to_underfunding <- 0.60,
        description <- "Pessoas que morrem esperando cirurgia, exame, consulta, UTI.",
    ),
    DeathCost(
        PreventableDeathCategory.CHILD_MORTALITY,
        "Mortalidade infantil (0-5 anos)",
        cost_to_save_one_life_brl <- 80_000,  // pre-natal + UTI neonatal
        deaths_per_year_brazil <- 40_000,
        pct_linked_to_underfunding <- 0.70,
        description <- "Criancas que morrem antes dos 5 anos por falta de atendimento.",
    ),
    DeathCost(
        PreventableDeathCategory.MATERNAL_DEATH,
        "Morte materna (no parto)",
        cost_to_save_one_life_brl <- 50_000,
        deaths_per_year_brazil <- 1_800,
        pct_linked_to_underfunding <- 0.80,
        description <- "Maes que morrem no parto por falta de estrutura hospitalar.",
    ),
    DeathCost(
        PreventableDeathCategory.MALNUTRITION,
        "Desnutricao",
        cost_to_save_one_life_brl <- 15_000,  // cesta + suplemento
        deaths_per_year_brazil <- 5_000,
        pct_linked_to_underfunding <- 0.90,
        description <- "Pessoas que morrem de fome ou desnutricao grave no Brasil.",
    ),
    DeathCost(
        PreventableDeathCategory.PREVENTABLE_DISEASE,
        "Doencas evitaveis (vacina/exame)",
        cost_to_save_one_life_brl <- 20_000,
        deaths_per_year_brazil <- 50_000,
        pct_linked_to_underfunding <- 0.65,
        description <- "Mortes por doencas que vacina ou exame precoce previniria.",
    ),
    DeathCost(
        PreventableDeathCategory.VIOLENCE,
        "Violencia / Homicidio",
        cost_to_save_one_life_brl <- 300_000,  // programa social + educacao
        deaths_per_year_brazil <- 47_000,
        pct_linked_to_underfunding <- 0.40,
        description <- "Jovens mortos por violencia. Programa social reduz 40%.",
    ),
    DeathCost(
        PreventableDeathCategory.SUICIDE,
        "Suicidio (sem saude mental)",
        cost_to_save_one_life_brl <- 100_000,  // CAPS + psicologo
        deaths_per_year_brazil <- 14_000,
        pct_linked_to_underfunding <- 0.55,
        description <- "Pessoas que se matam por falta de atendimento psicologico.",
    ),
    DeathCost(
        PreventableDeathCategory.SANITATION,
        "Doenças por falta de saneamento",
        cost_to_save_one_life_brl <- 40_000,
        deaths_per_year_brazil <- 8_000,
        pct_linked_to_underfunding <- 0.85,
        description <- "Mortes por diarreia, leptospirose, hepatite por agua suja.",
    ),
    DeathCost(
        PreventableDeathCategory.ROAD_DEATH,
        "Morte no transito",
        cost_to_save_one_life_brl <- 2_000_000,  // obra viaria
        deaths_per_year_brazil <- 30_000,
        pct_linked_to_underfunding <- 0.35,
        description <- "Acidentes em estradas sem manutencao ou sinalizacao.",
    ),
    DeathCost(
        PreventableDeathCategory.CANCER_UNTREATED,
        "Cancer sem tratamento a tempo",
        cost_to_save_one_life_brl <- 800_000,  // quimio + radioterapia
        deaths_per_year_brazil <- 35_000,
        pct_linked_to_underfunding <- 0.50,
        description <- "Pessoas que morrem esperando tratamento de cancer no SUS.",
    ),
    DeathCost(
        PreventableDeathCategory.HEART_UNTREATED,
        "Infarto sem atendimento",
        cost_to_save_one_life_brl <- 600_000,  // SAMU + UTI
        deaths_per_year_brazil <- 100_000,
        pct_linked_to_underfunding <- 0.30,
        description <- "Infartos que UTI/SAMU salvaria se chegasse a tempo.",
    ),
    DeathCost(
        PreventableDeathCategory.NEONATAL,
        "Morte neonatal",
        cost_to_save_one_life_brl <- 120_000,
        deaths_per_year_brazil <- 19_000,
        pct_linked_to_underfunding <- 0.65,
        description <- "Bebe que morre nos primeiros 28 dias por falta de UTI neonatal.",
    ),
]


// ============================================================================
// 3. SIMULACAO ANO A ANO
// ============================================================================

// decorador: @dataclass
classe YearMortality:
    // Um ano da simulacao de mortalidade por divida.
    year_label: int
    interest_paid_brl: float             // juros pagos no ano
    gdp_brl: float                        // PIB do ano

    // Mortes
    total_preventable_deaths: int         // total de mortes evitaveis no ano
    deaths_linked_to_debt: int            // mortes por falta do dinheiro que foi pro juros

    // O que o juros poderia ter feito
    potential_lives_saved: int            // vidas que o juros salvaria se investido
    hospitals_not_built: int              // hospitais que nao foram construidos
    people_without_doctor: int            // pessoas sem medico
    children_not_vaccinated: int          // criancas sem vacina
    houses_not_built: int                 // casas populares nao construidas
    meals_not_served: int                 // refeicoes nao servidas

    // Acumulado
    cumulative_deaths_by_debt: int        // mortes acumuladas pela divida


classe DebtMortalitySimulator:
    // 
    Simula quantas pessoas morrem porque o dinheiro foi para o agiota
    em vez de ir para saude, comida, educacao.

    METODOLOGIA:
    1. Calcular juros pago no ano (R$)
    2. Calcular o FRACAO que deveria ir para saude (40%)
    3. Dividir pelo custo de salvar uma vida em cada categoria
    4. Somar vidas que SERIAM salvas se o dinheiro ficasse
    5. Essas vidas nao salvas = MORTES PELA DIVIDA

    Este e um modelo conservador. Usa apenas 40% do juros como
    'dinheiro que deveria ir para saude'. O restante iria para
    educacao, infraestrutura, seguranca -- que tambm salva vidas.
    // 

    funcao __init__(self, start_year: int = 2024, years: int = 20):
        self.start_year = start_year
        self.years = years
        self.initial_debt = 6.0e12
        self.initial_gdp = 10.0e12
        self.interest_rate = 0.12
        self.gdp_growth = 0.025
        self.population = 215e6

        // Fracao do orcamento que vai para saude/bem-estar
        self.fraction_to_health = 0.40      // 40% do juros iria pra saude
        self.fraction_to_food = 0.15        // 15% iria pra comida
        self.fraction_to_housing = 0.15     // 15% iria pra moradia
        self.fraction_to_education = 0.15   // 15% iria pra educacao
        self.fraction_to_infra = 0.15       // 15% iria pra infraestrutura

        self.simulations: List[YearMortality] = []

    funcao simulate(self) retorna List[YearMortality]:
        // Roda a simulacao ano a ano.
        self.simulations = []
        debt <- self.initial_debt
        gdp <- self.initial_gdp
        cumulative_deaths <- 0

        para cada i em range(self.years + 1):
            year_label <- self.start_year + i

            interest <- debt * self.interest_rate
            money_for_health <- interest * self.fraction_to_health
            money_for_food <- interest * self.fraction_to_food

            // Calcular vidas que poderiam ser salvas com o dinheiro da saude
            potential_saved <- 0
            para cada dc em DEATH_COSTS:
                lives_saved <- money_for_health * 0.3 / dc.cost_to_save_one_life_brl  // 30% pra cada categoria
                potential_saved <- potential_saved + int(lives_saved)

            // Total de mortes evitaveis no ano (base OMS)
            total_preventable <- sum(dc.deaths_preventable() for dc in DEATH_COSTS)

            // Mortes pela divida = o que NAO foi salvo por falta de dinheiro
            // Usar o potencial salvo como proxy (conservador)
            deaths_by_debt <- min(potential_saved, total_preventable)

            // O que mais nao foi feito
            hospitals_not_built <- int(money_for_health / 50e6)  // R$ 50M por hospital
            people_without_doctor <- int(money_for_health / 3_000)  // R$ 3k/ano por paciente
            children_not_vaccinated <- int(money_for_health / 50)  // R$ 50 por vacina
            houses_not_built <- int(interest * self.fraction_to_housing / 80_000)
            meals_not_served <- int(money_for_food / 3)  // R$ 3 por refeicao

            cumulative_deaths <- cumulative_deaths + deaths_by_debt

            sim <- YearMortality(
                year_label <- year_label,
                interest_paid_brl <- interest,
                gdp_brl <- gdp,
                total_preventable_deaths <- total_preventable,
                deaths_linked_to_debt <- deaths_by_debt,
                potential_lives_saved <- potential_saved,
                hospitals_not_built <- hospitals_not_built,
                people_without_doctor <- people_without_doctor,
                children_not_vaccinated <- children_not_vaccinated,
                houses_not_built <- houses_not_built,
                meals_not_served <- meals_not_served,
                cumulative_deaths_by_debt <- cumulative_deaths,
            )
            self.simulations.append(sim)

            // Proximo ano
            debt <- debt + interest - (gdp * 0.18 * 0.3)  // cresce com juros menos pagto
            gdp <- gdp * (1 + self.gdp_growth)

        retorne self.simulations

    funcao total_deaths_by_debt(self) retorna int:
        // Total de mortes acumuladas em todos os anos simulados.
        retorne self.simulations[-1].cumulative_deaths_by_debt if self.simulations else 0

    funcao total_interest_paid(self) retorna float:
        // Total de juros pagos em todos os anos.
        retorne sum(s.interest_paid_brl for s in self.simulations)

    funcao death_per_trillion_interest(self) retorna float:
        // Mortes por R$ 1 trilhao de juros pagos.
        total_int <- self.total_interest_paid()
        se total_int == 0 entao:
            retorne 0
        retorne self.total_deaths_by_debt() / (total_int / 1e12)

    funcao summary(self) retorna Dict[str, Any]:
        // Resumo da simulacao.
        last <- self.simulations[-1] if self.simulations else nulo
        retorne {
            "years_simulated": self.years,
            "total_deaths_by_debt": self.total_deaths_by_debt(),
            "total_interest_paid_trillions": self.total_interest_paid() / 1e12,
            "deaths_per_trillion_interest": self.death_per_trillion_interest(),
            "avg_deaths_per_year": self.total_deaths_by_debt() / max(1, self.years),
            "final_year_hospitals_not_built": last.hospitals_not_built if last else 0,
            "final_year_meals_not_served": last.meals_not_served if last else 0,
            "final_year_children_not_vaccinated": last.children_not_vaccinated if last else 0,
        }


// ============================================================================
// 4. QUEM O BRASIL PAGA (paises credores)
// ============================================================================

// decorador: @dataclass
classe CountryCreditor:
    // Pais que recebe juros do Brasil e quantas mortes isso causa.
    country: str
    amount_received_brl: float          // quanto recebe por ano em juros
    declare flag: str  <- ""
    declare description: str  <- ""


declare COUNTRY_CREDITORS: List[CountryCreditor]  <- [
    CountryCreditor("Estados Unidos", 180e9, "EUA",
        "Fundos de investimento e bancos americanos recebem bilhoes em juros."),
    CountryCreditor("Reino Unido", 80e9, "UK",
        "Londres e centro de vulture funds que lucram com divida alheia."),
    CountryCreditor("Alemanha", 50e9, "DE",
        "Bancos alemaes detem titulos brasileiros."),
    CountryCreditor("Japao", 40e9, "JP",
        "Fundos japoneses investem em divida soberana."),
    CountryCreditor("Franca", 35e9, "FR",
        "Bancos franceses (BNP, SocGen) detem titulos."),
    CountryCreditor("Suica", 30e9, "CH",
        "Centro de banca privada que lucra com juros."),
    CountryCreditor("China", 25e9, "CN",
        "Bancos chineses compraram titulos brasileiros."),
    CountryCreditor("Holanda", 20e9, "NL",
        "Centro financeiro (Amsterda) roteia investimentos."),
    CountryCreditor("Luxemburgo", 15e9, "LU",
        "Paraiso fiscal que abriga fundos especulativos."),
    CountryCreditor("Outros", 25e9, "??",
        "Outros paises e fundos internacionais."),
]


// ============================================================================
// 5. RENDERIZACOES VISUAIS
// ============================================================================

funcao render_death_chart(simulations: List[YearMortality]) retorna str:
    // Grafico ASCII: mortes por ano por causa da divida.
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  MORTES POR ANO CAUSADAS PELA DIVIDA")
    lines.append("  (pessoas que morreriam VIVAS se o juros fosse investido em saude)")
    lines.append("=" * 70)
    lines.append("")

    max_deaths <- max(s.deaths_linked_to_debt for s in simulations) if simulations else 1
    se max_deaths == 0 entao:
        max_deaths <- 1

    para cada s em simulations:
        bar_len <- int((s.deaths_linked_to_debt / max_deaths) * 50)
        bar <- "#" * max(1, bar_len)
        lines.append(f"  {s.year_label} |{bar:<50}| {s.deaths_linked_to_debt:>8,} mortes")

    lines.append("")
    lines.append(f"  Cada # representa ~{max_deaths//50:,} mortes")
    lines.append(f"  TOTAL ACUMULADO: {simulations[-1].cumulative_deaths_by_debt:,} mortes")
    lines.append(f"  em {len(simulations)-1} anos")
    lines.append("")
    retorne "\n".join(lines)


funcao render_country_deaths() retorna str:
    // Mostra quanto cada pais credor recebe e quantas mortes causa.
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  PARA QUEM O BRASIL PAGA -- E QUANTOS MORREM POR ISSO")
    lines.append("=" * 70)
    lines.append("")

    total_received <- sum(c.amount_received_brl for c in COUNTRY_CREDITORS)

    para cada c em COUNTRY_CREDITORS:
        pct <- (c.amount_received_brl / total_received) * 100
        // Cada R$ 500k = 1 vida que nao foi salva
        deaths_caused <- int(c.amount_received_brl / 500_000)
        bar_len <- int(pct)
        bar <- "$" * bar_len
        lines.append(f"  {c.country:15} R$ {c.amount_received_brl/1e9:>6.0f} bi/ano "
                     f"[{bar:<20}] {pct:>5.1f}%  ~{deaths_caused:,} mortes")

    lines.append("")
    lines.append(f"  TOTAL ENVIADO AO EXTERIOR: R$ {total_received/1e9:.0f} bilhoes/ano")
    lines.append(f"  MORTES CAUSADAS: ~{int(total_received/500_000):,} por ano")
    lines.append(f"  Cada $ = R$ {total_received/20/1e9:.0f} bilhoes que sai do Brasil")
    lines.append("")
    lines.append("  Cada real enviado ao agiota international e uma vida")
    lines.append("  que NAO foi salva no Brasil.")
    lines.append("")
    retorne "\n".join(lines)


funcao render_category_breakdown() retorna str:
    // Detalha as mortes por categoria.
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  MORTES EVITAVEIS NO BRASIL (por categoria, por ano)")
    lines.append("=" * 70)
    lines.append("")

    total_preventable <- sum(dc.deaths_preventable() for dc in DEATH_COSTS)

    lines.append(f"{'CATEGORIA':<40} {'MORTES/ANO':>12} {'CUSTO/VIDA':>15} {'EVITAVEIS':>12}")
    lines.append("-" * 80)

    para cada dc em DEATH_COSTS:
        lines.append(
            f"  {dc.name:<38} {dc.deaths_per_year_brazil:>10,} "
            f"R$ {dc.cost_to_save_one_life_brl:>12,.0f} {dc.deaths_preventable():>10,}"
        )

    lines.append("-" * 80)
    lines.append(f"  {'TOTAL':<38} {sum(dc.deaths_per_year_brazil for dc in DEATH_COSTS):>10,}"
                 f" {'':>15} {total_preventable:>10,}")

    lines.append("")
    lines.append(f"  Total de mortes evitaveis/ano: {total_preventable:,}")
    lines.append(f"  Isso e {total_preventable/365:.0f} mortes POR DIA.")
    lines.append(f"  {total_preventable/365/24:.0f} mortes POR HORA.")
    lines.append(f"  {total_preventable/365/24/60:.1f} mortes POR MINUTO.")
    lines.append("")
    lines.append("  UMA PESSOA MORRE NO BRASIL A CADA MINUTO")
    lines.append("  POR ALGO QUE DINHEIRO RESOLVERIA.")
    lines.append("")
    lines.append(f"  E o dinheiro? FOI PRA O AGIOTA.")
    lines.append("")
    retorne "\n".join(lines)


funcao render_lost_infrastructure(simulations: List[YearMortality]) retorna str:
    // O que NAO foi construido porque o dinheiro foi pro juros.
    s <- simulations[0]  // primeiro ano como base
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  O QUE O BRASIL NAO CONSTRUIU EM UM ANO")
    lines.append(f"  ({s.year_label} -- R$ {s.interest_paid_brl/1e9:.0f} bi em juros)")
    lines.append("=" * 70)
    lines.append("")
    lines.append(f"  Hospitais nao construidos:        {s.hospitals_not_built:>8,}")
    lines.append(f"  Casas populares nao entregues:    {s.houses_not_built:>8,}")
    lines.append(f"  Pessoas sem medico de familia:    {s.people_without_doctor:>8,}")
    lines.append(f"  Criancas nao vacinadas:            {s.children_not_vaccinated:>8,}")
    lines.append(f"  Refeicoes nao servidas:            {s.meals_not_served:>8,}")
    lines.append("")
    lines.append("  Em UM ano, o juros da divida pagou:")
    lines.append(f"  - {s.hospitals_not_built:,} hospitais QUE NAO EXISTEM")
    lines.append(f"  - {s.houses_not_built:,} casas QUE NAO FORAM ENTREGUES")
    lines.append(f"  - {s.meals_not_served:,} refeicoes QUE NAO FORAM SERVIDAS")
    lines.append("")
    lines.append("  Cada hospital que nao existe = pessoas que morrem na fila.")
    lines.append("  Cada casa que nao foi entregue = familias na rua.")
    lines.append("  Cada refeicao que nao foi servida = criancas desnutridas.")
    lines.append("")
    retorne "\n".join(lines)


funcao render_timeline_human(simulations: List[YearMortality]) retorna str:
    // Linha do tempo humanizada.
    lines <- []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  LINHA DO TEMPO DA MORTE")
    lines.append("=" * 70)
    lines.append("")

    para cada s em simulations:
        deaths_per_day <- s.deaths_linked_to_debt / 365
        lines.append(f"  {s.year_label}:")
        lines.append(f"    Juros pago: R$ {s.interest_paid_brl/1e9:.0f} bilhoes")
        lines.append(f"    Mortes causadas pela divida: {s.deaths_linked_to_debt:,}")
        lines.append(f"    Isso sao {deaths_per_day:.0f} mortes POR DIA")
        lines.append(f"    Acumulado desde {simulations[0].year_label}: {s.cumulative_deaths_by_debt:,}")
        lines.append("")

    lines.append(f"  Em {len(simulations)-1} anos, a divida causou a morte de:")
    lines.append(f"  {simulations[-1].cumulative_deaths_by_debt:,} PESSOAS.")
    lines.append("")
    lines.append(f"  Isso e mais que a populacao de muitas cidades brasileiras.")
    lines.append(f"  Mais que todas as guerras do Brasil juntas.")
    lines.append(f"  Mais que todas as epidemias da historia recente.")
    lines.append("")
    lines.append(f"  E nao foi uma bala. Foi um BOLETO.")
    lines.append("")
    retorne "\n".join(lines)


funcao render_narrative(simulations: List[YearMortality]) retorna str:
    // Narrativa para a Telefonista ler.
    s0 <- simulations[0]
    last <- simulations[-1]
    total <- last.cumulative_deaths_by_debt

    parts <- []
    parts.append("Vou te dizer algo que ninguem te conta.")
    parts.append("")
    parts.append(f"No ano {s0.year_label}, o Brasil pagou R$ {s0.interest_paid_brl/1e9:.0f} bilhoes")
    parts.append("apenas em JUROS da divida publica.")
    parts.append("")
    parts.append("Esse dinheiro foi para bancos, fundos, paises estrangeiros.")
    parts.append("Nao foi para o SUS. Nao foi para a escola. Nao foi para a comida.")
    parts.append("")
    parts.append(f"No mesmo ano, {s0.deaths_linked_to_debt:,} brasileiros morreram")
    parts.append("por causas evitaveis. Filas do SUS. Desnutricao. Falta de medico.")
    parts.append("")
    parts.append(f"Se o dinheiro dos juros tivesse ido para a saude,")
    parts.append(f"{s0.potential_lives_saved:,} dessas pessoas poderiam estar VIVAS.")
    parts.append("")
    parts.append(f"Em {len(simulations)-1} anos, se nada mudar,")
    parts.append(f"a divida tera causado a morte de {total:,} pessoas.")
    parts.append("")
    parts.append(f"Sao {total/365:.0f} mortes por dia. A cada minuto, alguem morre")
    parts.append("porque o dinheiro que salvaria sua vida foi para o agiota.")
    parts.append("")
    parts.append("A divida nao e um numero. E um CEMITERIO.")
    parts.append("Cada parcela paga e uma cova que nao foi aberta.")
    parts.append("Cada juros pago e uma vida que nao foi salva.")
    parts.append("")
    parts.append("A divida MATA.")

    retorne " ".join(parts)


// ============================================================================
// 6. DEMONSTRACAO
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?")
    print("=" * 70)

    sim <- DebtMortalitySimulator(start_year=2024, years=20)
    simulations <- sim.simulate()

    // Breakdown por categoria
    print(render_category_breakdown())

    // Para quem o Brasil paga
    print(render_country_deaths())

    // O que nao foi construido
    print(render_lost_infrastructure(simulations))

    // Grafico de mortes por ano
    print(render_death_chart(simulations))

    // Linha do tempo
    print(render_timeline_human(simulations))

    // Narrativa
    print(f"\n{'=' * 70}")
    print("NARRATIVA (para Telefonista ler)")
    print(f"{'=' * 70}")
    print(render_narrative(simulations))

    // Resumo
    summary <- sim.summary()
    print(f"\n{'=' * 70}")
    print("RESUMO")
    print(f"{'=' * 70}")
    print(f"  Anos simulados: {summary['years_simulated']}")
    print(f"  Total de mortes pela divida: {summary['total_deaths_by_debt']:,}")
    print(f"  Total de juros pagos: R$ {summary['total_interest_paid_trillions']:.1f} trilhoes")
    print(f"  Mortes por R$ 1 trilhao de juros: {summary['deaths_per_trillion_interest']:.0f}")
    print(f"  Media de mortes/ano: {summary['avg_deaths_per_year']:,.0f}")

    print(f"\n{'=' * 70}")
    print("VEREDictO")
    print(f"{'=' * 70}")
    print()
    print("  A divida publica nao e apenas impossivel de pagar.")
    print("  Ela e um ASSASSINO DE MASSA silencioso.")
    print()
    print(f"  Em {summary['years_simulated']} anos:")
    print(f"  {summary['total_deaths_by_debt']:,} brasileiros morreram")
    print(f"  porque R$ {summary['total_interest_paid_trillions']:.1f} trilhoes")
    print(f"  foram enviados ao agiota em vez de ir para saude, comida, vida.")
    print()
    print(f"  A divida MATA.")
    print(f"  Cada juros pago e uma vida nao salva.")
    print(f"  Nao renegociar. Nao alongar.")
    print(f"  EXTINGUIR.")
    print(f"  Pelas vidas que ainda podem ser salvas.")
    print()
    print("  'Nao existe pobreza, existe MISERIA.'")
    print("  A divida e a maquina que PRODUZ a miseria.")


se __name__ == "__main__" entao:
    demo()

```
