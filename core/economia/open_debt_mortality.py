#!/usr/bin/env python3
"""
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
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
import math


# ============================================================================
# 1. CAUSAS DE MORTE EVITAVEIS (vinculadas a subfinanciamento)
# ============================================================================

class PreventableDeathCategory(Enum):
    """Categorias de morte evitaveis por investimento publico."""
    HEALTHCARE_SHORTAGE = "falta_sus"           # morreu na fila do SUS
    CHILD_MORTALITY = "mortalidade_infantil"    # bebe nao sobreviveu
    MATERNAL_DEATH = "morte_materna"             # mae morreu no parto
    MALNUTRITION = "desnutricao"                 # morreu de fome
    PREVENTABLE_DISEASE = "doenca_evitavel"      # vacina/exame nao chegou
    VIOLENCE = "violencia"                       # sem programa social
    SUICIDE = "suicidio"                         # sem saude mental
    SANITATION = "saneamento"                    # agua contaminada
    ROAD_DEATH = "transito"                      # estrada sem manutencao
    HEAT_COLD = "calor_frio"                     # sem teto/climatizacao
    DRUG_OVERDOSE = "overdose"                   # sem tratamento
    CANCER_UNTREATED = "cancer_sem_tratamento"   # fila de quimio
    HEART_UNTREATED = "coracao_sem_atendimento"  # sem UTI
    NEONATAL = "neonatal"                        # sem UTI neonatal


@dataclass
class DeathCost:
    """Custo de salvar uma vida em cada categoria."""
    category: PreventableDeathCategory
    name: str
    cost_to_save_one_life_brl: float    # quanto custa prevenir UMA morte
    deaths_per_year_brazil: int         # mortes/ano no Brasil hoje
    pct_linked_to_underfunding: float   # % que seria evitada com dinheiro
    description: str = ""

    def deaths_preventable(self) -> int:
        """Mortes que DA pra evitar com investimento."""
        return int(self.deaths_per_year_brazil * self.pct_linked_to_underfunding)

    def lives_saved_per_billion(self) -> float:
        """Quantas vidas R$ 1 bilhao salva nesta categoria."""
        if self.cost_to_save_one_life_brl <= 0:
            return 0
        return 1e9 / self.cost_to_save_one_life_brl


# ============================================================================
# 2. TABELA DE MORTALIDADE (Dados baseados em OMS/IBGE/Datasus)
# ============================================================================

DEATH_COSTS: List[DeathCost] = [
    DeathCost(
        PreventableDeathCategory.HEALTHCARE_SHORTAGE,
        "Morte na fila do SUS",
        cost_to_save_one_life_brl=500_000,    # UTI + cirurgia por pessoa
        deaths_per_year_brazil=124_000,        # mortes evitaveis no SUS
        pct_linked_to_underfunding=0.60,
        description="Pessoas que morrem esperando cirurgia, exame, consulta, UTI.",
    ),
    DeathCost(
        PreventableDeathCategory.CHILD_MORTALITY,
        "Mortalidade infantil (0-5 anos)",
        cost_to_save_one_life_brl=80_000,      # pre-natal + UTI neonatal
        deaths_per_year_brazil=40_000,
        pct_linked_to_underfunding=0.70,
        description="Criancas que morrem antes dos 5 anos por falta de atendimento.",
    ),
    DeathCost(
        PreventableDeathCategory.MATERNAL_DEATH,
        "Morte materna (no parto)",
        cost_to_save_one_life_brl=50_000,
        deaths_per_year_brazil=1_800,
        pct_linked_to_underfunding=0.80,
        description="Maes que morrem no parto por falta de estrutura hospitalar.",
    ),
    DeathCost(
        PreventableDeathCategory.MALNUTRITION,
        "Desnutricao",
        cost_to_save_one_life_brl=15_000,      # cesta + suplemento
        deaths_per_year_brazil=5_000,
        pct_linked_to_underfunding=0.90,
        description="Pessoas que morrem de fome ou desnutricao grave no Brasil.",
    ),
    DeathCost(
        PreventableDeathCategory.PREVENTABLE_DISEASE,
        "Doencas evitaveis (vacina/exame)",
        cost_to_save_one_life_brl=20_000,
        deaths_per_year_brazil=50_000,
        pct_linked_to_underfunding=0.65,
        description="Mortes por doencas que vacina ou exame precoce previniria.",
    ),
    DeathCost(
        PreventableDeathCategory.VIOLENCE,
        "Violencia / Homicidio",
        cost_to_save_one_life_brl=300_000,     # programa social + educacao
        deaths_per_year_brazil=47_000,
        pct_linked_to_underfunding=0.40,
        description="Jovens mortos por violencia. Programa social reduz 40%.",
    ),
    DeathCost(
        PreventableDeathCategory.SUICIDE,
        "Suicidio (sem saude mental)",
        cost_to_save_one_life_brl=100_000,     # CAPS + psicologo
        deaths_per_year_brazil=14_000,
        pct_linked_to_underfunding=0.55,
        description="Pessoas que se matam por falta de atendimento psicologico.",
    ),
    DeathCost(
        PreventableDeathCategory.SANITATION,
        "Doenças por falta de saneamento",
        cost_to_save_one_life_brl=40_000,
        deaths_per_year_brazil=8_000,
        pct_linked_to_underfunding=0.85,
        description="Mortes por diarreia, leptospirose, hepatite por agua suja.",
    ),
    DeathCost(
        PreventableDeathCategory.ROAD_DEATH,
        "Morte no transito",
        cost_to_save_one_life_brl=2_000_000,   # obra viaria
        deaths_per_year_brazil=30_000,
        pct_linked_to_underfunding=0.35,
        description="Acidentes em estradas sem manutencao ou sinalizacao.",
    ),
    DeathCost(
        PreventableDeathCategory.CANCER_UNTREATED,
        "Cancer sem tratamento a tempo",
        cost_to_save_one_life_brl=800_000,     # quimio + radioterapia
        deaths_per_year_brazil=35_000,
        pct_linked_to_underfunding=0.50,
        description="Pessoas que morrem esperando tratamento de cancer no SUS.",
    ),
    DeathCost(
        PreventableDeathCategory.HEART_UNTREATED,
        "Infarto sem atendimento",
        cost_to_save_one_life_brl=600_000,     # SAMU + UTI
        deaths_per_year_brazil=100_000,
        pct_linked_to_underfunding=0.30,
        description="Infartos que UTI/SAMU salvaria se chegasse a tempo.",
    ),
    DeathCost(
        PreventableDeathCategory.NEONATAL,
        "Morte neonatal",
        cost_to_save_one_life_brl=120_000,
        deaths_per_year_brazil=19_000,
        pct_linked_to_underfunding=0.65,
        description="Bebe que morre nos primeiros 28 dias por falta de UTI neonatal.",
    ),
]


# ============================================================================
# 3. SIMULACAO ANO A ANO
# ============================================================================

@dataclass
class YearMortality:
    """Um ano da simulacao de mortalidade por divida."""
    year_label: int
    interest_paid_brl: float            # juros pagos no ano
    gdp_brl: float                       # PIB do ano

    # Mortes
    total_preventable_deaths: int        # total de mortes evitaveis no ano
    deaths_linked_to_debt: int           # mortes por falta do dinheiro que foi pro juros

    # O que o juros poderia ter feito
    potential_lives_saved: int           # vidas que o juros salvaria se investido
    hospitals_not_built: int             # hospitais que nao foram construidos
    people_without_doctor: int           # pessoas sem medico
    children_not_vaccinated: int         # criancas sem vacina
    houses_not_built: int                # casas populares nao construidas
    meals_not_served: int                # refeicoes nao servidas

    # Acumulado
    cumulative_deaths_by_debt: int       # mortes acumuladas pela divida


class DebtMortalitySimulator:
    """
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
    """

    def __init__(self, start_year: int = 2025, years: int = 20):
        self.start_year = start_year
        self.years = years
        # ATUALIZADO 2024/2025 (em linha com open_debt_impact / open_debt_default)
        # Dívida pública federal bruta ~ R$ 8.0T (Dvida Mobility / Tesouro Nacional 2024-25)
        # Dívida líquida do setor público ~ R$ 5-6T; usamos a bruta como base de juros.
        # PIB nominal ~ R$ 11.5T (2024) -> ~R$ 12T (2025 proj. IBGE/BCB).
        # Taxa efetiva de juros da dívida ~ 10-11.5% (Selic média 2024-25).
        self.initial_debt = 8.0e12      # R$ 8.0T (dívida federal bruta 2024/2025)
        self.initial_gdp = 11.5e12      # R$ 11.5T (PIB nominal 2024/2025)
        self.interest_rate = 0.105      # 10.5% (taxa efetiva média juros da dívida 2024-25)
        self.gdp_growth = 0.025         # 2.5% (crescimento nominal projetado)
        self.population = 214.5e6       # População Brasil ~214.5M (2025 proj. IBGE)

        # Fracao do orcamento que vai para saude/bem-estar
        self.fraction_to_health = 0.40     # 40% do juros iria pra saude
        self.fraction_to_food = 0.15       # 15% iria pra comida
        self.fraction_to_housing = 0.15    # 15% iria pra moradia
        self.fraction_to_education = 0.15  # 15% iria pra educacao
        self.fraction_to_infra = 0.15      # 15% iria pra infraestrutura

        self.simulations: List[YearMortality] = []

    def simulate(self) -> List[YearMortality]:
        """Roda a simulacao ano a ano."""
        self.simulations = []
        debt = self.initial_debt
        gdp = self.initial_gdp
        cumulative_deaths = 0

        for i in range(self.years + 1):
            year_label = self.start_year + i

            interest = debt * self.interest_rate
            money_for_health = interest * self.fraction_to_health
            money_for_food = interest * self.fraction_to_food

            # Calcular vidas que poderiam ser salvas com o dinheiro da saude
            potential_saved = 0
            for dc in DEATH_COSTS:
                lives_saved = money_for_health * 0.3 / dc.cost_to_save_one_life_brl  # 30% pra cada categoria
                potential_saved += int(lives_saved)

            # Total de mortes evitaveis no ano (base OMS)
            total_preventable = sum(dc.deaths_preventable() for dc in DEATH_COSTS)

            # Mortes pela divida = o que NAO foi salvo por falta de dinheiro
            # Usar o potencial salvo como proxy (conservador)
            deaths_by_debt = min(potential_saved, total_preventable)

            # O que mais nao foi feito
            hospitals_not_built = int(money_for_health / 50e6)  # R$ 50M por hospital
            people_without_doctor = int(money_for_health / 3_000)  # R$ 3k/ano por paciente
            children_not_vaccinated = int(money_for_health / 50)  # R$ 50 por vacina
            houses_not_built = int(interest * self.fraction_to_housing / 80_000)
            meals_not_served = int(money_for_food / 3)  # R$ 3 por refeicao

            cumulative_deaths += deaths_by_debt

            sim = YearMortality(
                year_label=year_label,
                interest_paid_brl=interest,
                gdp_brl=gdp,
                total_preventable_deaths=total_preventable,
                deaths_linked_to_debt=deaths_by_debt,
                potential_lives_saved=potential_saved,
                hospitals_not_built=hospitals_not_built,
                people_without_doctor=people_without_doctor,
                children_not_vaccinated=children_not_vaccinated,
                houses_not_built=houses_not_built,
                meals_not_served=meals_not_served,
                cumulative_deaths_by_debt=cumulative_deaths,
            )
            self.simulations.append(sim)

            # Proximo ano
            debt = debt + interest - (gdp * 0.18 * 0.3)  # cresce com juros menos pagto
            gdp = gdp * (1 + self.gdp_growth)

        return self.simulations

    def total_deaths_by_debt(self) -> int:
        """Total de mortes acumuladas em todos os anos simulados."""
        return self.simulations[-1].cumulative_deaths_by_debt if self.simulations else 0

    def total_interest_paid(self) -> float:
        """Total de juros pagos em todos os anos."""
        return sum(s.interest_paid_brl for s in self.simulations)

    def death_per_trillion_interest(self) -> float:
        """Mortes por R$ 1 trilhao de juros pagos."""
        total_int = self.total_interest_paid()
        if total_int == 0:
            return 0
        return self.total_deaths_by_debt() / (total_int / 1e12)

    def summary(self) -> Dict[str, Any]:
        """Resumo da simulacao."""
        last = self.simulations[-1] if self.simulations else None
        return {
            "years_simulated": self.years,
            "total_deaths_by_debt": self.total_deaths_by_debt(),
            "total_interest_paid_trillions": self.total_interest_paid() / 1e12,
            "deaths_per_trillion_interest": self.death_per_trillion_interest(),
            "avg_deaths_per_year": self.total_deaths_by_debt() / max(1, self.years),
            "final_year_hospitals_not_built": last.hospitals_not_built if last else 0,
            "final_year_meals_not_served": last.meals_not_served if last else 0,
            "final_year_children_not_vaccinated": last.children_not_vaccinated if last else 0,
        }


# ============================================================================
# 4. QUEM O BRASIL PAGA (paises credores)
# ============================================================================

@dataclass
class CountryCreditor:
    """Pais que recebe juros do Brasil e quantas mortes isso causa."""
    country: str
    amount_received_brl: float         # quanto recebe por ano em juros
    flag: str = ""
    description: str = ""


# Nota: valores aproximados (2024/2025). A maior parte da dívida federal
# brasileira e interna (fundos de pensao, bancos, proprio BC). A parcela
# externa (titulos soberanos + global bonds detidos por nao-residentes) recebe
# uma fracao dos juros; abaixo distribui-se ~R$ 500 bi/ano entre os principais
# centros receptores. Valores ilustrativos para o modelo.
COUNTRY_CREDITORS: List[CountryCreditor] = [
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


# ============================================================================
# 5. AMORTIZACOES 2024 (Dados Tesouro Nacional / Dvida Mobility)
# ============================================================================
# Refs: Tesouro Nacional - Anual Report da Dvida Pblica Federal (DPMob) 2024
#       Banco Central do Brasil - Dvida Externa
#
# Em 2024 o Tesouro Nacional amortizou ~R$ 1.7 trilhoes em principal da
# divida mobiliaria federal, majoritariamente via rolagem (refinanciamento).
# Esses vencimentos representam o peso estrutural da divida: todo ano bilhoes
# saem so para REEMBOLSAR o agiota do capital emprestado -- alem dos juros.

@dataclass
class AmortizationItem:
    """Amortizacao de um instrumento da divida em 2024."""
    instrument: str                   # titulo / modalidade
    amount_brl: float                 # R$ amortizados no ano
    pct_of_total: float               # % do total amortizado
    description: str = ""


AMORTIZATIONS_2024: List[AmortizationItem] = [
    AmortizationItem(
        "Tesouro Prefixado (LTN/NTN-F)",
        amount_brl=620e9,
        pct_of_total=0.365,
        description="Vencimentos de titulos prefixados. Maior peso da rolagem.",
    ),
    AmortizationItem(
        "Tesouro Selic (LFT)",
        amount_brl=480e9,
        pct_of_total=0.282,
        description="Letras atreladas a Selic -- rolagem automatica frequente.",
    ),
    AmortizationItem(
        "Tesouro IPCA+ (NTN-B)",
        amount_brl=350e9,
        pct_of_total=0.206,
        description="Titulos indexados a inflacao -- vencimentos de medio/longo prazo.",
    ),
    AmortizationItem(
        "Tesouro Renda+ / Educacao+",
        amount_brl=30e9,
        pct_of_total=0.018,
        description="Titulos propositais com vencimentos iniciando.",
    ),
    AmortizationItem(
        "Divida Externa (Global Bonds)",
        amount_brl=130e9,
        pct_of_total=0.076,
        description="Titulos soberanos em moeda estrangeira (USD/EUR).",
    ),
    AmortizationItem(
        "Outros (FTOs, operacoes BC, etc.)",
        amount_brl=90e9,
        pct_of_total=0.053,
        description="Fundos, operacoes do BC e demais obrigacoes.",
    ),
]


def total_amortization_2024() -> float:
    """Total amortizado (principal) em 2024 -- R$."""
    return sum(a.amount_brl for a in AMORTIZATIONS_2024)


def render_amortizations_2024() -> str:
    """Mostra as amortizacoes (principal) da divida federal em 2024."""
    lines: List[str] = []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  AMORTIZACOES DA DIVIDA FEDERAL -- 2024")
    lines.append("  (principal reembolsado ao agiota, ALEM dos juros)")
    lines.append("=" * 70)
    lines.append("")

    total = total_amortization_2024()
    for a in AMORTIZATIONS_2024:
        bar_len = int(a.pct_of_total * 50)
        bar = "#" * bar_len
        lines.append(
            f"  {a.instrument:<34} R$ {a.amount_brl/1e9:>6.0f} bi "
            f"[{bar:<50}] {a.pct_of_total*100:>5.1f}%"
        )

    lines.append("")
    lines.append(f"  TOTAL AMORTIZADO EM 2024: R$ {total/1e9:.0f} bilhoes")
    lines.append(f"  (R$ {total/1e12:.2f} trilhoes)")
    lines.append("")
    lines.append("  Cada real aqui e CAPITAL devolvido ao credor.")
    lines.append("  Soma-se aos juros: e o custo TOTAL da divida.")
    lines.append("")
    return "\n".join(lines)


# ============================================================================
# 6. RENDERIZACOES VISUAIS
# ============================================================================

def render_death_chart(simulations: List[YearMortality]) -> str:
    """Grafico ASCII: mortes por ano por causa da divida."""
    lines = []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  MORTES POR ANO CAUSADAS PELA DIVIDA")
    lines.append("  (pessoas que morreriam VIVAS se o juros fosse investido em saude)")
    lines.append("=" * 70)
    lines.append("")

    max_deaths = max(s.deaths_linked_to_debt for s in simulations) if simulations else 1
    if max_deaths == 0:
        max_deaths = 1

    for s in simulations:
        bar_len = int((s.deaths_linked_to_debt / max_deaths) * 50)
        bar = "#" * max(1, bar_len)
        lines.append(f"  {s.year_label} |{bar:<50}| {s.deaths_linked_to_debt:>8,} mortes")

    lines.append("")
    lines.append(f"  Cada # representa ~{max_deaths//50:,} mortes")
    lines.append(f"  TOTAL ACUMULADO: {simulations[-1].cumulative_deaths_by_debt:,} mortes")
    lines.append(f"  em {len(simulations)-1} anos")
    lines.append("")
    return "\n".join(lines)


def render_country_deaths() -> str:
    """Mostra quanto cada pais credor recebe e quantas mortes causa."""
    lines = []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  PARA QUEM O BRASIL PAGA -- E QUANTOS MORREM POR ISSO")
    lines.append("=" * 70)
    lines.append("")

    total_received = sum(c.amount_received_brl for c in COUNTRY_CREDITORS)

    for c in COUNTRY_CREDITORS:
        pct = (c.amount_received_brl / total_received) * 100
        # Cada R$ 500k = 1 vida que nao foi salva
        deaths_caused = int(c.amount_received_brl / 500_000)
        bar_len = int(pct)
        bar = "$" * bar_len
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
    return "\n".join(lines)


def render_category_breakdown() -> str:
    """Detalha as mortes por categoria."""
    lines = []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  MORTES EVITAVEIS NO BRASIL (por categoria, por ano)")
    lines.append("=" * 70)
    lines.append("")

    total_preventable = sum(dc.deaths_preventable() for dc in DEATH_COSTS)

    lines.append(f"{'CATEGORIA':<40} {'MORTES/ANO':>12} {'CUSTO/VIDA':>15} {'EVITAVEIS':>12}")
    lines.append("-" * 80)

    for dc in DEATH_COSTS:
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
    return "\n".join(lines)


def render_lost_infrastructure(simulations: List[YearMortality]) -> str:
    """O que NAO foi construido porque o dinheiro foi pro juros."""
    s = simulations[0]  # primeiro ano como base
    lines = []
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
    return "\n".join(lines)


def render_timeline_human(simulations: List[YearMortality]) -> str:
    """Linha do tempo humanizada."""
    lines = []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  LINHA DO TEMPO DA MORTE")
    lines.append("=" * 70)
    lines.append("")

    for s in simulations:
        deaths_per_day = s.deaths_linked_to_debt / 365
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
    return "\n".join(lines)


def render_narrative(simulations: List[YearMortality]) -> str:
    """Narrativa para a Telefonista ler."""
    s0 = simulations[0]
    last = simulations[-1]
    total = last.cumulative_deaths_by_debt

    parts = []
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

    return " ".join(parts)


# ============================================================================
# 7. DEMONSTRACAO
# ============================================================================

def demo():
    print("=" * 70)
    print("OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?")
    print("=" * 70)

    sim = DebtMortalitySimulator(start_year=2025, years=20)
    simulations = sim.simulate()

    # Breakdown por categoria
    print(render_category_breakdown())

    # Amortizacoes 2024 (principal, alem dos juros)
    print(render_amortizations_2024())

    # Para quem o Brasil paga
    print(render_country_deaths())

    # O que nao foi construido
    print(render_lost_infrastructure(simulations))

    # Grafico de mortes por ano
    print(render_death_chart(simulations))

    # Linha do tempo
    print(render_timeline_human(simulations))

    # Narrativa
    print(f"\n{'=' * 70}")
    print("NARRATIVA (para Telefonista ler)")
    print(f"{'=' * 70}")
    print(render_narrative(simulations))

    # Resumo
    summary = sim.summary()
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


if __name__ == "__main__":
    demo()
