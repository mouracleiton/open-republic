#!/usr/bin/env python3
"""
OpenDebtImpact -- Todos os Impactos da Divida na Vida Humana
================================================================
"A divida nao so mata. Ela CASTRA.
Castr a educacao. Castra a ciencia. Castra a moradia.
Castr a o futuro. Cada real pro agiota e um real roubado
de cada area que faz a vida valer a pena."

Este modulo simula o impacto da divida em TODAS as dimensoes
da vida brasileira. Nao so mortes (OpenDebtMortality) -- mas
tudo que a divida DESTRÓI silenciosamente:

1. EDUCACAO: escolas, professores, alfabetizacao
2. SAUDE MENTAL: depressao, ansiedade, suicidio
3. MORADIA: sem-teto, favelas, habitacao
4. SEGURANCA ALIMENTAR: fome, desnutricao
5. INFRAESTRUTURA: estradas, transporte, energia
6. SANEAMENTO: agua, esgoto, lixo
7. CIENCIA & TECNOLOGIA: pesquisa, inovacao, patentes
8. CULTURA & ARTE: museus, teatro, musica
9. DESIGUALDADE: renda, genero, raca
10. MEIO AMBIENTE: desmatamento, poluicao
11. SEGURANCA: policia, violencia
12. ESPORTE: educacao fisica, lazer
13. TRANSPORTES: metro, onibus, mobilidade
14. COMUNICACOES: internet, conectividade
15. INFANCIA: creches, primeira infancia

Para cada area, calcula ano a ano:
- Quanto foi ROUBADO pelo juros da divida
- O que esse dinheiro teria construido
- Quantas pessoas foram afetadas
- O impacto cumulativo em 20 anos

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
import math


# ============================================================================
# 1. AREAS DE IMPACTO
# ============================================================================

class ImpactArea(Enum):
    EDUCATION = "educacao"
    HEALTH_MENTAL = "saude_mental"
    HOUSING = "moradia"
    FOOD_SECURITY = "seguranca_alimentar"
    INFRASTRUCTURE = "infraestrutura"
    SANITATION = "saneamento"
    SCIENCE_TECH = "ciencia_tecnologia"
    CULTURE_ARTS = "cultura_arte"
    INEQUALITY = "desigualdade"
    ENVIRONMENT = "meio_ambiente"
    SECURITY = "seguranca"
    SPORT = "esporte"
    TRANSPORT = "transporte"
    CONNECTIVITY = "conectividade"
    CHILDHOOD = "infancia"


class SeverityLevel(Enum):
    CRITICAL = "critico"       # destruicao total
    SEVERE = "severo"          # degradacao profunda
    HIGH = "alto"              # impacto significativo
    MODERATE = "moderado"      # degradacao visivel
    LOW = "baixo"             # impacto leve


@dataclass
class AreaImpact:
    """Impacto da divida em uma area especifica."""
    area: ImpactArea
    name: str
    severity: SeverityLevel

    # O que o juros ROUBOU desta area
    annual_budget_needed_brl: float    # quanto esta area precisa/ano
    annual_budget_actual_brl: float    # quanto recebe de verdade
    annual_budget_gap_brl: float       # deficit = roubo da divida
    pct_of_interest_that_should_go: float  # % do juros que deveria ir para ca

    # O que NAO foi feito (medidas de impacto humano)
    people_affected_per_year: int      # pessoas impactadas pela falta
    unit_cost_brl: float               # custo de 1 unidade (escola, casa, etc)
    unit_name: str = ""                # nome da unidade
    units_not_delivered_per_year: int = 0  # escolas/casas/km nao construidos

    # Descricao humanizada
    description: str = ""
    human_cost: str = ""               # o que significa na vida real

    def budget_gap_percentage(self) -> float:
        """Retorna o gap orcamentario como porcentagem."""
        if self.annual_budget_needed_brl <= 0:
            return 0
        return (self.annual_budget_gap_brl / self.annual_budget_needed_brl) * 100

    def units_lost_per_billion(self) -> float:
        """Quantas unidades se perdem por R$ 1 bilhao de juros."""
        if self.unit_cost_brl <= 0:
            return 0
        return 1e9 / self.unit_cost_brl


# ============================================================================
# 2. CATALOGO DE IMPACTOS (15 areas)
# ============================================================================

AREA_IMPACTS: List[AreaImpact] = [
    AreaImpact(
        ImpactArea.EDUCATION, "Educacao Basica e Superior",
        SeverityLevel.CRITICAL,
        annual_budget_needed_brl=600e9,
        annual_budget_actual_brl=180e9,
        annual_budget_gap_brl=420e9,
        pct_of_interest_that_should_go=0.15,
        people_affected_per_year=50_000_000,  # 50M alunos
        unit_cost_brl=5e6,                    # R$ 5M por escola
        unit_name="escolas",
        units_not_delivered_per_year=84_000,  # escolas faltando
        description="Educacao publica subfinanciada ha decadas.",
        human_cost="Criancas em escolas sem teto, sem merenda, sem professor. Universitarios sem bolsa. Analfabetismo funcional em 30% dos adultos.",
    ),
    AreaImpact(
        ImpactArea.HEALTH_MENTAL, "Saude Mental",
        SeverityLevel.SEVERE,
        annual_budget_needed_brl=80e9,
        annual_budget_actual_brl=4e9,         # 5% do necessario
        annual_budget_gap_brl=76e9,
        pct_of_interest_that_should_go=0.03,
        people_affected_per_year=20_000_000,  # 20M com transtorno mental
        unit_cost_brl=200_000,                # CAPS (Centro de Atencao Psicossocial)
        unit_name="CAPS (centro de saude mental)",
        units_not_delivered_per_year=380_000,
        description="Brasil tem 20 milhoes com transtorno mental. So 5% do orcamento necessario.",
        human_cost="Depressao nao tratada. Ansiedade cronica. Suicidios. Crack. Sem psicologo no SUS.",
    ),
    AreaImpact(
        ImpactArea.HOUSING, "Moradia Digna",
        SeverityLevel.CRITICAL,
        annual_budget_needed_brl=200e9,
        annual_budget_actual_brl=15e9,        # Minha Casa Minha Vida (reduzido)
        annual_budget_gap_brl=185e9,
        pct_of_interest_that_should_go=0.10,
        people_affected_per_year=8_000_000,   # 8M sem moradia adequada
        unit_cost_brl=80_000,                 # casa popular
        unit_name="casas populares",
        units_not_delivered_per_year=2_312_500,
        description="Deficit habitacional de 8 milhoes de familias.",
        human_cost="Familias em favelas, ruas, corticos. Criancas sem endereco fixo. Sem-teto morrendo de frio.",
    ),
    AreaImpact(
        ImpactArea.FOOD_SECURITY, "Seguranca Alimentar (Fome)",
        SeverityLevel.CRITICAL,
        annual_budget_needed_brl=120e9,
        annual_budget_actual_brl=35e9,        # Bolsa Familia + Programa de Aquisicao
        annual_budget_gap_brl=85e9,
        pct_of_interest_that_should_go=0.08,
        people_affected_per_year=33_000_000,  # 33M em inseguranca alimentar
        unit_cost_brl=3,                      # refeicao
        unit_name="refeicoes diarias",
        units_not_delivered_per_year=28_333_333_333,  # 28 bilhoes de refeicoes
        description="33 milhoes de brasileiros passam fome. O pais da soja nao alimenta seu povo.",
        human_cost="Criancas desnutridas. Maes que pulam refeicoes. Idosos escolhendo entre comer e remedio.",
    ),
    AreaImpact(
        ImpactArea.INFRASTRUCTURE, "Infraestrutura (Estradas, Energia)",
        SeverityLevel.SEVERE,
        annual_budget_needed_brl=300e9,
        annual_budget_actual_brl=60e9,
        annual_budget_gap_brl=240e9,
        pct_of_interest_that_should_go=0.12,
        people_affected_per_year=215_000_000,  # todo pais
        unit_cost_brl=20e6,                    # km de rodovia
        unit_name="km de rodovia",
        units_not_delivered_per_year=12_000,
        description="Estradas esburacadas. Pontes caindo. Sem investimento em energia.",
        human_cost="Acidentes fatais em estradas sem manutencao. Apagoes. Logistica cara = comida cara.",
    ),
    AreaImpact(
        ImpactArea.SANITATION, "Saneamento Basico",
        SeverityLevel.SEVERE,
        annual_budget_needed_brl=100e9,
        annual_budget_actual_brl=12e9,
        annual_budget_gap_brl=88e9,
        pct_of_interest_that_should_go=0.05,
        people_affected_per_year=100_000_000,  # 100M sem saneamento adequado
        unit_cost_brl=12_000,                  # ligacao domiciliar
        unit_name="ligacoes de agua/esgoto",
        units_not_delivered_per_year=7_333_333,
        description="Metade do Brasil nao tem esgoto tratado. Doencas por agua contaminada.",
        human_cost="Criancas com diarreia. Dengue. Leptospirose nas enchentes. Agua nao potavel.",
    ),
    AreaImpact(
        ImpactArea.SCIENCE_TECH, "Ciencia e Tecnologia",
        SeverityLevel.SEVERE,
        annual_budget_needed_brl=80e9,
        annual_budget_actual_brl=8e9,          # CNPq/Capes/LNCC decapitados
        annual_budget_gap_brl=72e9,
        pct_of_interest_that_should_go=0.04,
        people_affected_per_year=500_000,      # pesquisadores e estudantes
        unit_cost_brl=500_000,                 # bolsa de pesquisa anual
        unit_name="bolsas de pesquisa",
        units_not_delivered_per_year=144_000,
        description="CNPq e Capes com orcamento destroicado. Cerebros fugindo do pais.",
        human_cost="Pesquisadores no rdar de UBER. Doutores desempregados. Laboratorios fechados. Patentes perdidas.",
    ),
    AreaImpact(
        ImpactArea.CULTURE_ARTS, "Cultura e Arte",
        SeverityLevel.HIGH,
        annual_budget_needed_brl=30e9,
        annual_budget_actual_brl=3e9,          # Lei Rouanet destruida
        annual_budget_gap_brl=27e9,
        pct_of_interest_that_should_go=0.02,
        people_affected_per_year=10_000_000,   # artistas e publico
        unit_cost_brl=100_000,                 # producao cultural
        unit_name="producoes culturais",
        units_not_delivered_per_year=270_000,
        description="Cultura tratada como luxo. Artistas sem renda. Museus fechados.",
        human_cost="Teatros fechados. Cinema nacional morto. Musicos sem espaco. Identidade cultural apagada.",
    ),
    AreaImpact(
        ImpactArea.INEQUALITY, "Desigualdade de Renda",
        SeverityLevel.CRITICAL,
        annual_budget_needed_brl=500e9,        # reformas estruturais
        annual_budget_actual_brl=50e9,
        annual_budget_gap_brl=450e9,
        pct_of_interest_that_should_go=0.15,
        people_affected_per_year=150_000_000,  # 150M em vulnerabilidade
        unit_cost_brl=500,                     # transferencia mensal por pessoa
        unit_name="transferencias de renda/mes",
        units_not_delivered_per_year=900_000_000,  # 900M transferencias/mes nao feitas
        description="Brasil entre os 10 paises mais desiguais do mundo. Gini = 0.52.",
        human_cost="1% tem 50% da riqueza. Milhoes vivem com R$ 200/mes. Favelas ao lado de condominios.",
    ),
    AreaImpact(
        ImpactArea.ENVIRONMENT, "Meio Ambiente",
        SeverityLevel.SEVERE,
        annual_budget_needed_brl=50e9,
        annual_budget_actual_brl=5e9,
        annual_budget_gap_brl=45e9,
        pct_of_interest_that_should_go=0.03,
        people_affected_per_year=215_000_000,  # todo pais
        unit_cost_brl=100_000,                 # fiscalizacao/km2
        unit_name="km2 protegidos/fiscalizados",
        units_not_delivered_per_year=450_000,
        description="Desmatamento da Amazonia acelerando. IBAMA sem orcamento.",
        human_cost="Amazonia queimando. Agua acabando. Temperatura subindo. Futuro climatico destruido.",
    ),
    AreaImpact(
        ImpactArea.SECURITY, "Seguranca Publica",
        SeverityLevel.SEVERE,
        annual_budget_needed_brl=150e9,
        annual_budget_actual_brl=70e9,
        annual_budget_gap_brl=80e9,
        pct_of_interest_that_should_go=0.05,
        people_affected_per_year=60_000_000,   # 60M afetados por violencia
        unit_cost_brl=2e6,                     # delegacia equipada
        unit_name="delegacias equipadas",
        units_not_delivered_per_year=40_000,
        description="47 mil homicidios/ano. Mulheres mortas. LGBTQIA+ assassinados.",
        human_cost="Maes chorando filhos. Crianzas sem pai. Medo de sair de casa. Violencia doméstica.",
    ),
    AreaImpact(
        ImpactArea.SPORT, "Esporte e Lazer",
        SeverityLevel.MODERATE,
        annual_budget_needed_brl=20e9,
        annual_budget_actual_brl=2e9,
        annual_budget_gap_brl=18e9,
        pct_of_interest_that_should_go=0.01,
        people_affected_per_year=40_000_000,   # criancas e jovens
        unit_cost_brl=300_000,                 # quadra/centro esportivo
        unit_name="quadras esportivas",
        units_not_delivered_per_year=60_000,
        description="Esporte como herramienta de resgate social destruido.",
        human_cost="Criancas sem quadra. Jovens sem esporte = sem alternativa ao crime. Talentos perdidos.",
    ),
    AreaImpact(
        ImpactArea.TRANSPORT, "Transporte Publico",
        SeverityLevel.SEVERE,
        annual_budget_needed_brl=200e9,
        annual_budget_actual_brl=30e9,
        annual_budget_gap_brl=170e9,
        pct_of_interest_that_should_go=0.08,
        people_affected_per_year=100_000_000,  # usuarios de transporte publico
        unit_cost_brl=100e6,                   # km de metro
        unit_name="km de metro/onetbus",
        units_not_delivered_per_year=1_700,
        description="Metro sem expansao. Onibus lotados. Povo passa 3h/dia no transito.",
        human_cost="3 horas/dia no onibus lotado. Menos tempo com familia. Menos estudo. Mais estresse.",
    ),
    AreaImpact(
        ImpactArea.CONNECTIVITY, "Internet e Conectividade",
        SeverityLevel.HIGH,
        annual_budget_needed_brl=40e9,
        annual_budget_actual_brl=5e9,
        annual_budget_gap_brl=35e9,
        pct_of_interest_that_should_go=0.02,
        people_affected_per_year=70_000_000,   # 70M sem internet adequada
        unit_cost_brl=5_000,                   # conexao por domicilio
        unit_name="conexoes de internet",
        units_not_delivered_per_year=7_000_000,
        description="70 milhoes sem internet de qualidade. Exclusao digital.",
        human_cost="Criancas estudando no celular 3G. Sem telemedicina. Sem servicos publicos digitais.",
    ),
    AreaImpact(
        ImpactArea.CHILDHOOD, "Primeira Infancia (0-6 anos)",
        SeverityLevel.CRITICAL,
        annual_budget_needed_brl=80e9,
        annual_budget_actual_brl=8e9,          # creches subfinanciadas
        annual_budget_gap_brl=72e9,
        pct_of_interest_that_should_go=0.04,
        people_affected_per_year=12_000_000,   # criancas 0-6
        unit_cost_brl=1e6,                     # creche
        unit_name="vagas em creches",
        units_not_delivered_per_year=72_000,
        description="12 milhoes de criancas 0-6 sem creche. Desenvolvimento comprometido.",
        human_cost="Maes sem trabalhar porque nao tem creche. Criancas em casa sem estimulo. Futuro comprometido.",
    ),
]


# ============================================================================
# 3. SIMULACAO ANO A ANO (20 anos)
# ============================================================================

@dataclass
class YearImpact:
    """Impacto de um ano em todas as areas."""
    year_label: int
    interest_paid_brl: float
    total_gap_brl: float                     # deficit total
    total_people_affected: int               # pessoas impactadas no ano
    area_details: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    cumulative_gap_brl: float = 0.0
    cumulative_people_affected: int = 0


class ImpactSimulator:
    """
    Simula o impacto da divida em 15 areas da vida brasileira
    ao longo de 20 anos.
    """

    def __init__(self, start_year: int = 2024, years: int = 20):
        self.start_year = start_year
        self.years = years
        self.initial_debt = 6.0e12
        self.initial_gdp = 10.0e12
        self.interest_rate = 0.12
        self.gdp_growth = 0.025
        self.simulations: List[YearImpact] = []

    def simulate(self) -> List[YearImpact]:
        """Roda a simulacao ano a ano."""
        self.simulations = []
        debt = self.initial_debt
        gdp = self.initial_gdp
        cumulative_gap = 0.0
        cumulative_people = 0

        for i in range(self.years + 1):
            year_label = self.start_year + i
            interest = debt * self.interest_rate

            total_gap = 0
            total_people = 0
            area_details = {}

            for ai in AREA_IMPACTS:
                # Gap orcamentario cresce com inflacao/PIB
                inflation_factor = (1.05) ** i  # ~5% inflacao/ano
                gap = ai.annual_budget_gap_brl * inflation_factor
                people = ai.people_affected_per_year
                units = int(gap / ai.unit_cost_brl)

                total_gap += gap
                total_people += people

                area_details[ai.area.value] = {
                    "name": ai.name,
                    "gap_brl": gap,
                    "people_affected": people,
                    "units_not_delivered": units,
                    "unit_name": ai.unit_name,
                    "severity": ai.severity.value,
                    "human_cost": ai.human_cost,
                    "gap_pct_of_interest": (gap / interest * 100) if interest > 0 else 0,
                }

            cumulative_gap += total_gap
            cumulative_people += total_people

            sim = YearImpact(
                year_label=year_label,
                interest_paid_brl=interest,
                total_gap_brl=total_gap,
                total_people_affected=total_people,
                area_details=area_details,
                cumulative_gap_brl=cumulative_gap,
                cumulative_people_affected=cumulative_people,
            )
            self.simulations.append(sim)

            # Proximo ano
            debt = debt + interest - (gdp * 0.18 * 0.3)
            gdp = gdp * (1 + self.gdp_growth)

        return self.simulations

    def total_gap_all_years(self) -> float:
        return self.simulations[-1].cumulative_gap_brl if self.simulations else 0

    def total_interest_all_years(self) -> float:
        return sum(s.interest_paid_brl for s in self.simulations)

    def summary(self) -> Dict[str, Any]:
        return {
            "years_simulated": self.years,
            "total_gap_trillions": self.total_gap_all_years() / 1e12,
            "total_interest_trillions": self.total_interest_all_years() / 1e12,
            "avg_gap_per_year_trillions": (self.total_gap_all_years() / self.years) / 1e12,
            "areas_impacted": len(AREA_IMPACTS),
            "total_people_per_year": self.simulations[0].total_people_affected if self.simulations else 0,
        }


# ============================================================================
# 4. RENDERIZACOES VISUAIS
# ============================================================================

def render_area_chart(simulations: List[YearImpact]) -> str:
    """Grafico: deficit por area em um ano."""
    s = simulations[0]
    lines = []
    lines.append("")
    lines.append("=" * 75)
    lines.append(f"  DEFICIT POR AREA -- {s.year_label} (R$ bilhoes)")
    lines.append("=" * 75)
    lines.append("")

    areas_sorted = sorted(s.area_details.items(), key=lambda x: x[1]["gap_brl"], reverse=True)
    max_gap = max(v["gap_brl"] for _, v in areas_sorted) if areas_sorted else 1

    for area_key, details in areas_sorted:
        gap_bi = details["gap_brl"] / 1e9
        bar_len = int((details["gap_brl"] / max_gap) * 40)
        bar = "X" * max(1, bar_len)
        sev = details["severity"].upper()[:4]
        lines.append(f"  {details['name']:<35} R${gap_bi:>7.0f}bi [{bar:<40}] {sev}")

    lines.append("")
    lines.append(f"  X = deficit orcamentario (dinheiro que FOI PRO JUROS)")
    lines.append(f"  TOTAL DEFICIT/ANO: R$ {s.total_gap_brl/1e9:.0f} bilhoes")
    lines.append(f"  PESSOAS AFETADAS/ANO: {s.total_people_affected:,}")
    lines.append("")
    return "\n".join(lines)


def render_cumulative_chart(simulations: List[YearImpact]) -> str:
    """Grafico: deficit acumulado ao longo dos anos."""
    lines = []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  DEFICIT ACUMULADO POR ANO (R$ trilhoes)")
    lines.append("=" * 70)
    lines.append("")

    max_val = simulations[-1].cumulative_gap_brl if simulations else 1

    for s in simulations:
        val_t = s.cumulative_gap_brl / 1e12
        bar_len = int((s.cumulative_gap_brl / max_val) * 50)
        bar = "#" * max(1, bar_len)
        lines.append(f"  {s.year_label} |{bar:<50}| R$ {val_t:.1f}T")

    lines.append("")
    lines.append(f"  Em {simulations[-1].year_label}: R$ {simulations[-1].cumulative_gap_brl/1e12:.1f} trilhoes ROUBADOS")
    lines.append(f"  de educacao, saude, moradia, ciencia, cultura...")
    lines.append("")
    return "\n".join(lines)


def render_human_cost() -> str:
    """Detalha o custo humano por area."""
    lines = []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  O CUSTO HUMANO -- O QUE A DIVIDA DESTRÓI")
    lines.append("=" * 70)

    for ai in AREA_IMPACTS:
        lines.append("")
        lines.append(f"  {ai.name.upper()} [{ai.severity.value.upper()}]")
        lines.append(f"  Deficit: R$ {ai.annual_budget_gap_brl/1e9:.0f} bilhoes/ano")
        lines.append(f"  Pessoas afetadas: {ai.people_affected_per_year:,}/ano")
        lines.append(f"  Nao entregue: {ai.units_not_delivered_per_year:,} {ai.unit_name}/ano")
        lines.append(f"  CUSTO HUMANO: {ai.human_cost}")
        lines.append(f"  {'─' * 66}")

    lines.append("")
    return "\n".join(lines)


def render_equivalence_table() -> str:
    """Tabela: o que cada R$ 100 bilhoes de juros rouba."""
    lines = []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  O QUE R$ 100 BILHOES DE JUROS ROUBOU DO POVO")
    lines.append("  (equivalencia: se esse dinheiro ficasse no Brasil)")
    lines.append("=" * 70)
    lines.append("")
    lines.append(f"  {'RECURSO':<35} {'QTD':>15}")
    lines.append("  " + "-" * 52)

    equivalences = [
        ("Escolas completas (R$ 5M)", int(100e9 / 5e6)),
        ("Hospitais (R$ 50M)", int(100e9 / 50e6)),
        ("Casas populares (R$ 80k)", int(100e9 / 80e3)),
        ("Creches (R$ 1M)", int(100e9 / 1e6)),
        ("CAPS saude mental (R$ 200k)", int(100e9 / 2e5)),
        ("Bolsas pesquisa (R$ 500k/ano)", int(100e9 / 5e5)),
        ("Quadras esportivas (R$ 300k)", int(100e9 / 3e5)),
        ("Delegacias equipadas (R$ 2M)", int(100e9 / 2e6)),
        ("km de rodovia (R$ 20M)", int(100e9 / 20e6)),
        ("km de metro/onibus (R$ 100M)", int(100e9 / 1e8)),
        ("Ligacoes de agua/esgoto (R$ 12k)", int(100e9 / 12e3)),
        ("Conexoes de internet (R$ 5k)", int(100e9 / 5e3)),
        ("Reféicoes (R$ 3)", int(100e9 / 3)),
        ("Producoes culturais (R$ 100k)", int(100e9 / 1e5)),
        ("Transferencias de renda/mes (R$ 500)", int(100e9 / 500)),
        ("Vagas em creches (R$ 1M)", int(100e9 / 1e6)),
    ]

    for label, qty in equivalences:
        if qty >= 1e9:
            qty_str = f"{qty/1e9:.1f} bilhoes"
        elif qty >= 1e6:
            qty_str = f"{qty/1e6:.1f} milhoes"
        elif qty >= 1e3:
            qty_str = f"{qty/1e3:.0f} mil"
        else:
            qty_str = f"{qty:,}"
        lines.append(f"  {label:<35} {qty_str:>15}")

    lines.append("")
    lines.append("  Cada R$ 100 bilhoes para o agiota e TUDO ISSO que nao existe.")
    lines.append("  O Brasil paga R$ 720 bilhoes/ano em juros.")
    lines.append("  Sao 7x essa tabela. TODO ANO.")
    lines.append("")
    return "\n".join(lines)


def render_comparison_other_countries() -> str:
    """Compara investimento por habitante: Brasil vs paises ricos."""
    lines = []
    lines.append("")
    lines.append("=" * 70)
    lines.append("  INVESTIMENTO PUBLICO POR HABITANTE/ANO")
    lines.append("  (Brasil vs paises que NAO tem divida extorsiva)")
    lines.append("=" * 70)
    lines.append("")

    countries = [
        ("Noruega", 25_000, "Defaultou divida em 1905. Hoje e modelo."),
        ("Dinamarca", 22_000, "Estado de bem-estar. Sem divida extorsiva."),
        ("Suécia", 20_000, "Investimento publico massivo."),
        ("Alemanha", 18_000, "Divida controlada. Investe no povo."),
        ("Holanda", 17_000, "Infraestrutura de ponta."),
        ("Canadá", 16_000, "Saude e educacao gratuitas."),
        ("Brasil", 3_500, "Paga R$ 720 bi/ano em juros. Sobra R$ 3.500/pessoa."),
    ]

    lines.append(f"  {'PAIS':<12} {'R$/pessoa/ano':>15}  {'BAR':>30}")
    lines.append("  " + "-" * 60)
    max_val = 25_000

    for country, value, note in countries:
        bar_len = int((value / max_val) * 30)
        bar = "#" * max(1, bar_len)
        marker = " <<<" if country == "Brasil" else ""
        lines.append(f"  {country:<12} R$ {value:>10,}  [{bar:<30}]{marker}")

    lines.append("")
    lines.append(f"  Brasil investe 7x MENOS por pessoa que paises ricos.")
    lines.append(f"  Nao e coincidencia. E a DIVIDA.")
    lines.append(f"  O dinheiro que iria pro povo vai pro AGIOTA.")
    lines.append("")
    return "\n".join(lines)


def render_narrative(simulations: List[YearImpact]) -> str:
    """Narrativa para Telefonista ler."""
    s0 = simulations[0]
    last = simulations[-1]

    parts = []
    parts.append("Vou te mostrar o que a divida faz. Nao so matar. Mas DESTRUIR.")
    parts.append("")
    parts.append(f"Em {s0.year_label}, o Brasil pagou R$ {s0.interest_paid_brl/1e9:.0f} bilhoes em juros.")
    parts.append(f"Esse dinheiro deveria ter ido para {len(AREA_IMPACTS)} areas da sua vida:")
    parts.append("")
    parts.append("Educacao: 50 milhoes de alunos em escolas destruidas.")
    parts.append("Saude mental: 20 milhoes de brasileiros sem tratamento.")
    parts.append("Moradia: 8 milhoes de familias sem casa digna.")
    parts.append("Comida: 33 milhoes passando fome.")
    parts.append("Saneamento: 100 milhoes sem esgoto.")
    parts.append("Ciencia: pesquisadores no UBER.")
    parts.append("Cultura: teatros fechados, artistas sem teto.")
    parts.append("Esporte: criancas sem quadra.")
    parts.append("Internet: 70 milhoes sem conexao.")
    parts.append("Creches: 12 milhoes de criancas abandonadas.")
    parts.append("")
    parts.append(f"Em {last.year_label}, o deficit acumulado sera de")
    parts.append(f"R$ {last.cumulative_gap_brl/1e12:.0f} trilhoes.")
    parts.append(f"Dinheiro que foi ROUBADO de cada area que faz a vida valer a pena.")
    parts.append("")
    parts.append("A divida nao so mata. Ela CASTRA.")
    parts.append("Castr a educacao. Castra a ciencia. Castra a moradia.")
    parts.append("Castra o futuro.")
    parts.append("")
    parts.append("Cada real pro agiota e um real roubado do seu filho.")
    parts.append("Da sua escola. Do seu hospital. Da sua casa.")
    parts.append("Da sua cultura. Do seu esporte. Da sua internet.")
    parts.append("")
    parts.append("A divida MATA. E o que ela nao mata, ela DESTRÓI.")

    return " ".join(parts)


# ============================================================================
# 5. DEMONSTRACAO
# ============================================================================

def demo():
    print("=" * 70)
    print("OpenDebtImpact -- Todos os Impactos da Divida")
    print("=" * 70)

    sim = ImpactSimulator(2024, 20)
    simulations = sim.simulate()

    print(f"\nAreas impactadas: {len(AREA_IMPACTS)}")
    print(f"Severidade critica: {sum(1 for a in AREA_IMPACTS if a.severity == SeverityLevel.CRITICAL)}")
    print(f"Severidade severa: {sum(1 for a in AREA_IMPACTS if a.severity == SeverityLevel.SEVERE)}")

    # Grafico por area
    print(render_area_chart(simulations))

    # Custo humano detalhado
    print(render_human_cost())

    # Tabela de equivalencia
    print(render_equivalence_table())

    # Comparacao internacional
    print(render_comparison_other_countries())

    # Deficit acumulado
    print(render_cumulative_chart(simulations))

    # Narrativa
    print(f"\n{'=' * 70}")
    print("NARRATIVA")
    print(f"{'=' * 70}")
    print(render_narrative(simulations))

    # Resumo
    summary = sim.summary()
    print(f"\n{'=' * 70}")
    print("RESUMO")
    print(f"{'=' * 70}")
    print(f"  Areas impactadas: {summary['areas_impacted']}")
    print(f"  Pessoas afetadas/ano: {summary['total_people_per_year']:,}")
    print(f"  Deficit total em {summary['years_simulated']} anos: R$ {summary['total_gap_trillions']:.1f} trilhoes")
    print(f"  Juros pagos no periodo: R$ {summary['total_interest_trillions']:.1f} trilhoes")
    print(f"  Deficit medio/ano: R$ {summary['avg_gap_per_year_trillions']:.1f} trilhoes")

    print(f"\n{'=' * 70}")
    print("VEREDictO")
    print(f"{'=' * 70}")
    print()
    print("  A divida MATA (OpenDebtMortality).")
    print("  E o que ela nao mata, ela DESTRÓI (este modulo).")
    print()
    print(f"  Em {summary['years_simulated']} anos:")
    print(f"  R$ {summary['total_gap_trillions']:.0f} trilhoes ROUBADOS")
    print(f"  de educacao, saude, moradia, ciencia, cultura, esporte,")
    print(f"  meio ambiente, seguranca, transporte, conectividade, infancia.")
    print()
    print(f"  {len(AREA_IMPACTS)} areas destruidas.")
    print(f"  {summary['total_people_per_year']/1e6:.0f} milhoes de pessoas/ano afetadas.")
    print()
    print("  Cada parcela da divida e uma escola que nao existe.")
    print("  Cada juros pago e uma creche que nao foi construida.")
    print("  Cada bilhao pro agiota e mil futurós cancelados.")
    print()
    print("  A divida MATA. E DESTRÓI. E CASTRA.")
    print("  Nao renegociar. Nao alongar. EXTINGUIR.")
    print()
    print("  'Nao existe pobreza, existe MISERIA.'")
    print("  A divida e a maquina que PRODUZ a miseria.")


if __name__ == "__main__":
    demo()
