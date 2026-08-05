#!/usr/bin/env python3
"""
OpenDistribuicaoRenda -- A Média Mente. A Distribuição Mostra.
================================================================
"70% da população ganha abaixo da média. A média não é realidade.
 É uma mentira estatística que esconde desigualdade."

Este módulo substitui TODA referência a 'renda média' no sistema
por distribuição percentil (P10-P99). Mostra quem ganha o quê.

Fonte base: PNAD Contínua 2023 (IBGE), atualizado 2024.
ATENÇÃO: Dados MOCK até triangulação com IBGE direto.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


class FaixaRenda(Enum):
    """Faixas de renda que refletem a distribuição real, não a média."""
    INDIGENTE = "indigente"          # R$ 0 - 100 (extrema pobreza)
    MISERIA = "miseria"              # R$ 100 - 300
    POBREZA = "pobreza"              # R$ 300 - 600
    BAIXA = "baixa"                  # R$ 600 - 1.200
    MEDIANA_BAIXA = "mediana_baixa"  # R$ 1.200 - 2.000
    MEDIANA = "mediana"              # R$ 2.000 - 3.500
    ALTA = "alta"                    # R$ 3.500 - 8.000
    ALTA_MAIOR = "alta_maior"        # R$ 8.000 - 20.000
    RICA = "rica"                    # R$ 20.000 - 50.000
    ELITE = "elite"                  # R$ 50.000+ (1%)


@dataclass
class PercentilRenda:
    """Um percentil da distribuição de renda."""
    percentil: str                  # P10, P25, P50, P75, P90, P99
    renda_mensal: float             # R$/mês
    descricao: str                  # quem são essas pessoas


@dataclass
class DistribuicaoEstado:
    """Distribuição de renda de um estado (não média -- distribuição real)."""
    estado: str
    nome_estado: str
    populacao_milhoes: float

    # Percentis
    p10: float                      # 10% mais pobre
    p25: float
    p50: float                      # MEDIANA (50% ganha isto ou menos)
    p75: float
    p90: float
    p99: float                      # 1% mais rico

    # A média que MENTE
    media_mentirosa: float          # média aritmética (puxada pela elite)

    # Distribuição por faixa (% da população)
    faixas: Dict[str, float]        # faixa -> % da população

    # Racial
    renda_negro_p50: float          # mediana negro
    renda_branco_p50: float         # mediana branco
    racio_racial: float             # branco / negro

    # Gênero
    renda_mulher_p50: float
    renda_homem_p50: float
    racio_genero: float             # homem / mulher

    # Extremos
    topo_1pct_participacao: float   # % da renda total que o 1% leva
    base_50pct_participacao: float  # % da renda total que os 50% levam

    fonte: str

    @property
    def mediana(self) -> float:
        return self.p50

    @property
    def raca_gap(self) -> float:
        """Quanto o branco ganha a mais que o negro (múltiplo)."""
        return self.renda_branco_p50 / self.renda_negro_p50 if self.renda_negro_p50 > 0 else 0

    @property
    def genero_gap(self) -> float:
        return self.renda_homem_p50 / self.renda_mulher_p50 if self.renda_mulher_p50 > 0 else 0

    @property
    def desigualdade(self) -> float:
        """P99 / P10 = quanto o topo ganha vs a base."""
        return self.p99 / self.p10 if self.p10 > 0 else 0


def _init_estados() -> List[DistribuicaoEstado]:
    """
    Distribuição de renda por estado. MOCK baseado em PNAD 2023.

    A média mente em TODOS os estados. A mediana mostra a verdade.
    """
    return [
        # BRASIL (referência nacional)
        DistribuicaoEstado("BR", "Brasil", 203.1,
            p10=300, p25=700, p50=1600, p75=3200, p90=6500, p99=25000,
            media_mentirosa=2800,
            faixas={"indigente": 4, "miseria": 8, "pobreza": 12, "baixa": 20,
                    "mediana_baixa": 18, "mediana": 15, "alta": 12, "alta_maior": 7,
                    "rica": 3, "elite": 1},
            renda_negro_p50=1400, renda_branco_p50=2500, racio_racial=1.79,
            renda_mulher_p50=1500, renda_homem_p50=2000, racio_genero=1.33,
            topo_1pct_participacao=28.3, base_50pct_participacao=10.0,
            fonte="PNAD Contínua 2023 (IBGE) — MOCK"),

        # NORTE
        DistribuicaoEstado("AC", "Acre", 0.9,
            p10=100, p25=300, p50=900, p75=1800, p90=3500, p99=12000,
            media_mentirosa=1500,
            faixas={"indigente": 8, "miseria": 15, "pobreza": 20, "baixa": 22,
                    "mediana_baixa": 15, "mediana": 10, "alta": 6, "alta_maior": 3,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=700, renda_branco_p50=1200, racio_racial=1.71,
            renda_mulher_p50=800, renda_homem_p50=1100, racio_genero=1.38,
            topo_1pct_participacao=25.0, base_50pct_participacao=8.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("AM", "Amazonas", 4.3,
            p10=150, p25=400, p50=1100, p75=2200, p90=4500, p99=15000,
            media_mentirosa=1800,
            faixas={"indigente": 7, "miseria": 12, "pobreza": 18, "baixa": 22,
                    "mediana_baixa": 16, "mediana": 12, "alta": 8, "alta_maior": 4,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=900, renda_branco_p50=1600, racio_racial=1.78,
            renda_mulher_p50=1000, renda_homem_p50=1300, racio_genero=1.30,
            topo_1pct_participacao=26.0, base_50pct_participacao=9.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("PA", "Pará", 8.8,
            p10=100, p25=300, p50=850, p75=1700, p90=3500, p99=13000,
            media_mentirosa=1400,
            faixas={"indigente": 9, "miseria": 14, "pobreza": 20, "baixa": 22,
                    "mediana_baixa": 15, "mediana": 10, "alta": 6, "alta_maior": 3,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=650, renda_branco_p50=1300, racio_racial=2.00,
            renda_mulher_p50=750, renda_homem_p50=1000, racio_genero=1.33,
            topo_1pct_participacao=27.0, base_50pct_participacao=7.5,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("RO", "Rondônia", 1.8,
            p10=150, p25=400, p50=1000, p75=2000, p90=4000, p99=14000,
            media_mentirosa=1700,
            faixas={"indigente": 6, "miseria": 12, "pobreza": 18, "baixa": 22,
                    "mediana_baixa": 16, "mediana": 12, "alta": 8, "alta_maior": 4,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=800, renda_branco_p50=1300, racio_racial=1.63,
            renda_mulher_p50=900, renda_homem_p50=1200, racio_genero=1.33,
            topo_1pct_participacao=24.0, base_50pct_participacao=9.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("RR", "Roraima", 0.7,
            p10=150, p25=350, p50=950, p75=1900, p90=3800, p99=13000,
            media_mentirosa=1600,
            faixas={"indigente": 7, "miseria": 13, "pobreza": 19, "baixa": 21,
                    "mediana_baixa": 15, "mediana": 11, "alta": 7, "alta_maior": 4,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=750, renda_branco_p50=1300, racio_racial=1.73,
            renda_mulher_p50=850, renda_homem_p50=1150, racio_genero=1.35,
            topo_1pct_participacao=25.0, base_50pct_participacao=8.5,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("AP", "Amapá", 0.9,
            p10=120, p25=300, p50=850, p75=1700, p90=3400, p99=12000,
            media_mentirosa=1450,
            faixas={"indigente": 8, "miseria": 14, "pobreza": 20, "baixa": 22,
                    "mediana_baixa": 15, "mediana": 10, "alta": 6, "alta_maior": 3,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=650, renda_branco_p50=1200, racio_racial=1.85,
            renda_mulher_p50=750, renda_homem_p50=1000, racio_genero=1.33,
            topo_1pct_participacao=26.0, base_50pct_participacao=8.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("TO", "Tocantins", 1.6,
            p10=150, p25=350, p50=950, p75=1900, p90=3700, p99=13000,
            media_mentirosa=1550,
            faixas={"indigente": 7, "miseria": 13, "pobreza": 19, "baixa": 21,
                    "mediana_baixa": 16, "mediana": 11, "alta": 7, "alta_maior": 4,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=750, renda_branco_p50=1300, racio_racial=1.73,
            renda_mulher_p50=850, renda_homem_p50=1100, racio_genero=1.29,
            topo_1pct_participacao=25.0, base_50pct_participacao=8.5,
            fonte="PNAD 2023 — MOCK"),

        # NORDESTE
        DistribuicaoEstado("MA", "Maranhão", 7.2,
            p10=0, p25=150, p50=550, p75=1200, p90=2800, p99=10000,
            media_mentirosa=1000,
            faixas={"indigente": 12, "miseria": 18, "pobreza": 22, "baixa": 20,
                    "mediana_baixa": 12, "mediana": 8, "alta": 5, "alta_maior": 2,
                    "rica": 0.5, "elite": 0.3},
            renda_negro_p50=400, renda_branco_p50=900, racio_racial=2.25,
            renda_mulher_p50=450, renda_homem_p50=650, racio_genero=1.44,
            topo_1pct_participacao=30.0, base_50pct_participacao=6.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("PI", "Piauí", 3.3,
            p10=0, p25=200, p50=650, p75=1400, p90=3000, p99=10000,
            media_mentirosa=1100,
            faixas={"indigente": 10, "miseria": 16, "pobreza": 22, "baixa": 20,
                    "mediana_baixa": 14, "mediana": 9, "alta": 5, "alta_maior": 2,
                    "rica": 0.5, "elite": 0.3},
            renda_negro_p50=500, renda_branco_p50=1000, racio_racial=2.00,
            renda_mulher_p50=550, renda_homem_p50=750, racio_genero=1.36,
            topo_1pct_participacao=28.0, base_50pct_participacao=7.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("CE", "Ceará", 9.3,
            p10=100, p25=350, p50=850, p75=1700, p90=3500, p99=12000,
            media_mentirosa=1400,
            faixas={"indigente": 8, "miseria": 14, "pobreza": 20, "baixa": 21,
                    "mediana_baixa": 15, "mediana": 10, "alta": 7, "alta_maior": 3,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=650, renda_branco_p50=1300, racio_racial=2.00,
            renda_mulher_p50=750, renda_homem_p50=1000, racio_genero=1.33,
            topo_1pct_participacao=26.0, base_50pct_participacao=8.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("RN", "Rio Grande do Norte", 3.5,
            p10=100, p25=250, p50=750, p75=1500, p90=3000, p99=11000,
            media_mentirosa=1250,
            faixas={"indigente": 9, "miseria": 15, "pobreza": 21, "baixa": 20,
                    "mediana_baixa": 14, "mediana": 10, "alta": 6, "alta_maior": 3,
                    "rica": 0.5, "elite": 0.3},
            renda_negro_p50=550, renda_branco_p50=1100, racio_racial=2.00,
            renda_mulher_p50=650, renda_homem_p50=900, racio_genero=1.38,
            topo_1pct_participacao=27.0, base_50pct_participacao=7.5,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("PB", "Paraíba", 4.1,
            p10=100, p25=250, p50=700, p75=1400, p90=2900, p99=10500,
            media_mentirosa=1150,
            faixas={"indigente": 9, "miseria": 15, "pobreza": 21, "baixa": 20,
                    "mediana_baixa": 14, "mediana": 10, "alta": 6, "alta_maior": 3,
                    "rica": 0.5, "elite": 0.3},
            renda_negro_p50=500, renda_branco_p50=1050, racio_racial=2.10,
            renda_mulher_p50=600, renda_homem_p50=850, racio_genero=1.42,
            topo_1pct_participacao=28.0, base_50pct_participacao=7.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("PE", "Pernambuco", 9.7,
            p10=100, p25=300, p50=800, p75=1700, p90=3800, p99=14000,
            media_mentirosa=1400,
            faixas={"indigente": 8, "miseria": 14, "pobreza": 20, "baixa": 21,
                    "mediana_baixa": 15, "mediana": 10, "alta": 7, "alta_maior": 3,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=600, renda_branco_p50=1300, racio_racial=2.17,
            renda_mulher_p50=700, renda_homem_p50=950, racio_genero=1.36,
            topo_1pct_participacao=27.0, base_50pct_participacao=7.5,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("AL", "Alagoas", 3.4,
            p10=0, p25=150, p50=550, p75=1200, p90=2600, p99=9500,
            media_mentirosa=950,
            faixas={"indigente": 12, "miseria": 18, "pobreza": 22, "baixa": 18,
                    "mediana_baixa": 12, "mediana": 8, "alta": 5, "alta_maior": 2,
                    "rica": 0.5, "elite": 0.3},
            renda_negro_p50=400, renda_branco_p50=900, racio_racial=2.25,
            renda_mulher_p50=450, renda_homem_p50=650, racio_genero=1.44,
            topo_1pct_participacao=29.0, base_50pct_participacao=6.5,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("SE", "Sergipe", 2.3,
            p10=100, p25=250, p50=700, p75=1400, p90=2900, p99=10500,
            media_mentirosa=1150,
            faixas={"indigente": 9, "miseria": 15, "pobreza": 21, "baixa": 20,
                    "mediana_baixa": 14, "mediana": 10, "alta": 6, "alta_maior": 3,
                    "rica": 0.5, "elite": 0.3},
            renda_negro_p50=500, renda_branco_p50=1050, racio_racial=2.10,
            renda_mulher_p50=600, renda_homem_p50=850, racio_genero=1.42,
            topo_1pct_participacao=28.0, base_50pct_participacao=7.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("BA", "Bahia", 14.9,
            p10=100, p25=250, p50=700, p75=1500, p90=3200, p99=12000,
            media_mentirosa=1250,
            faixas={"indigente": 9, "miseria": 15, "pobreza": 21, "baixa": 20,
                    "mediana_baixa": 14, "mediana": 10, "alta": 6, "alta_maior": 3,
                    "rica": 1, "elite": 0.5},
            renda_negro_p50=550, renda_branco_p50=1200, racio_racial=2.18,
            renda_mulher_p50=600, renda_homem_p50=850, racio_genero=1.42,
            topo_1pct_participacao=28.0, base_50pct_participacao=7.0,
            fonte="PNAD 2023 — MOCK"),

        # CENTRO-OESTE
        DistribuicaoEstado("MT", "Mato Grosso", 3.7,
            p10=200, p25=500, p50=1300, p75=2800, p90=5500, p99=20000,
            media_mentirosa=2200,
            faixas={"indigente": 5, "miseria": 10, "pobreza": 16, "baixa": 20,
                    "mediana_baixa": 17, "mediana": 14, "alta": 10, "alta_maior": 5,
                    "rica": 2, "elite": 1},
            renda_negro_p50=1000, renda_branco_p50=1800, racio_racial=1.80,
            renda_mulher_p50=1100, renda_homem_p50=1500, racio_genero=1.36,
            topo_1pct_participacao=25.0, base_50pct_participacao=9.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("MS", "Mato Grosso do Sul", 2.8,
            p10=200, p25=500, p50=1300, p75=2700, p90=5200, p99=18000,
            media_mentirosa=2100,
            faixas={"indigente": 5, "miseria": 10, "pobreza": 16, "baixa": 20,
                    "mediana_baixa": 17, "mediana": 14, "alta": 10, "alta_maior": 5,
                    "rica": 2, "elite": 1},
            renda_negro_p50=1000, renda_branco_p50=1700, racio_racial=1.70,
            renda_mulher_p50=1100, renda_homem_p50=1400, racio_genero=1.27,
            topo_1pct_participacao=24.0, base_50pct_participacao=9.5,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("GO", "Goiás", 7.2,
            p10=150, p25=400, p50=1100, p75=2200, p90=4500, p99=16000,
            media_mentirosa=1800,
            faixas={"indigente": 6, "miseria": 11, "pobreza": 17, "baixa": 21,
                    "mediana_baixa": 16, "mediana": 13, "alta": 9, "alta_maior": 4,
                    "rica": 1.5, "elite": 0.5},
            renda_negro_p50=850, renda_branco_p50=1500, racio_racial=1.76,
            renda_mulher_p50=950, renda_homem_p50=1300, racio_genero=1.37,
            topo_1pct_participacao=25.0, base_50pct_participacao=8.5,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("DF", "Distrito Federal", 3.1,
            p10=300, p25=800, p50=2200, p75=5000, p90=12000, p99=40000,
            media_mentirosa=4500,
            faixas={"indigente": 3, "miseria": 6, "pobreza": 10, "baixa": 15,
                    "mediana_baixa": 15, "mediana": 17, "alta": 15, "alta_maior": 10,
                    "rica": 5, "elite": 2},
            renda_negro_p50=1600, renda_branco_p50=3500, racio_racial=2.19,
            renda_mulher_p50=1800, renda_homem_p50=2800, racio_genero=1.56,
            topo_1pct_participacao=30.0, base_50pct_participacao=12.0,
            fonte="PNAD 2023 — MOCK"),

        # SUDESTE
        DistribuicaoEstado("SP", "São Paulo", 45.9,
            p10=300, p25=800, p50=2000, p75=4500, p90=10000, p99=35000,
            media_mentirosa=3500,
            faixas={"indigente": 3, "miseria": 6, "pobreza": 10, "baixa": 15,
                    "mediana_baixa": 16, "mediana": 18, "alta": 16, "alta_maior": 10,
                    "rica": 4, "elite": 1.5},
            renda_negro_p50=1500, renda_branco_p50=3000, racio_racial=2.00,
            renda_mulher_p50=1700, renda_homem_p50=2500, racio_genero=1.47,
            topo_1pct_participacao=28.0, base_50pct_participacao=11.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("RJ", "Rio de Janeiro", 16.5,
            p10=200, p25=600, p50=1600, p75=3500, p90=8000, p99=30000,
            media_mentirosa=3000,
            faixas={"indigente": 4, "miseria": 8, "pobreza": 13, "baixa": 18,
                    "mediana_baixa": 16, "mediana": 15, "alta": 13, "alta_maior": 8,
                    "rica": 3, "elite": 1.2},
            renda_negro_p50=1200, renda_branco_p50=2500, racio_racial=2.08,
            renda_mulher_p50=1400, renda_homem_p50=2000, racio_genero=1.43,
            topo_1pct_participacao=29.0, base_50pct_participacao=10.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("MG", "Minas Gerais", 21.3,
            p10=150, p25=450, p50=1200, p75=2500, p90=5500, p99=18000,
            media_mentirosa=2000,
            faixas={"indigente": 5, "miseria": 10, "pobreza": 16, "baixa": 20,
                    "mediana_baixa": 17, "mediana": 14, "alta": 10, "alta_maior": 5,
                    "rica": 2, "elite": 0.7},
            renda_negro_p50=900, renda_branco_p50=1700, racio_racial=1.89,
            renda_mulher_p50=1000, renda_homem_p50=1400, racio_genero=1.40,
            topo_1pct_participacao=26.0, base_50pct_participacao=9.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("ES", "Espírito Santo", 4.1,
            p10=200, p25=500, p50=1300, p75=2700, p90=5200, p99=17000,
            media_mentirosa=2100,
            faixas={"indigente": 5, "miseria": 10, "pobreza": 16, "baixa": 20,
                    "mediana_baixa": 17, "mediana": 14, "alta": 10, "alta_maior": 5,
                    "rica": 2, "elite": 0.7},
            renda_negro_p50=1000, renda_branco_p50=1700, racio_racial=1.70,
            renda_mulher_p50=1100, renda_homem_p50=1400, racio_genero=1.27,
            topo_1pct_participacao=25.0, base_50pct_participacao=9.0,
            fonte="PNAD 2023 — MOCK"),

        # SUL
        DistribuicaoEstado("PR", "Paraná", 11.8,
            p10=200, p25=550, p50=1400, p75=2900, p90=6000, p99=20000,
            media_mentirosa=2300,
            faixas={"indigente": 4, "miseria": 8, "pobreza": 14, "baixa": 19,
                    "mediana_baixa": 17, "mediana": 15, "alta": 11, "alta_maior": 6,
                    "rica": 2.5, "elite": 0.8},
            renda_negro_p50=1000, renda_branco_p50=1700, racio_racial=1.70,
            renda_mulher_p50=1200, renda_homem_p50=1600, racio_genero=1.33,
            topo_1pct_participacao=25.0, base_50pct_participacao=10.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("SC", "Santa Catarina", 7.8,
            p10=300, p25=800, p50=1900, p75=3800, p90=7500, p99=25000,
            media_mentirosa=2900,
            faixas={"indigente": 3, "miseria": 6, "pobreza": 10, "baixa": 15,
                    "mediana_baixa": 16, "mediana": 18, "alta": 16, "alta_maior": 10,
                    "rica": 4, "elite": 1.5},
            renda_negro_p50=1400, renda_branco_p50=2200, racio_racial=1.57,
            renda_mulher_p50=1600, renda_homem_p50=2200, racio_genero=1.38,
            topo_1pct_participacao=24.0, base_50pct_participacao=11.0,
            fonte="PNAD 2023 — MOCK"),

        DistribuicaoEstado("RS", "Rio Grande do Sul", 10.9,
            p10=250, p25=650, p50=1600, p75=3300, p90=7000, p99=23000,
            media_mentirosa=2600,
            faixas={"indigente": 3, "miseria": 7, "pobreza": 11, "baixa": 16,
                    "mediana_baixa": 17, "mediana": 16, "alta": 14, "alta_maior": 9,
                    "rica": 3.5, "elite": 1.3},
            renda_negro_p50=1200, renda_branco_p50=2000, racio_racial=1.67,
            renda_mulher_p50=1400, renda_homem_p50=1900, racio_genero=1.36,
            topo_1pct_participacao=25.0, base_50pct_participacao=10.5,
            fonte="PNAD 2023 — MOCK"),
    ]


def _demo():
    estados = _init_estados()
    brasil = [e for e in estados if e.estado == "BR"][0]

    print("=" * 95)
    print("A MÉDIA MENTE. A DISTRIBUIÇÃO MOSTRA.")
    print("=" * 95)

    print(f"""
  RENDA MÉDIA BRASIL:   R$ {brasil.media_mentirosa:.0f}/mês
  RENDA MEDIANA BRASIL: R$ {brasil.mediana:.0f}/mês

  70% da população ganha ABAIXO da média.
  A média é puxada pelo 1% mais rico (R$ {brasil.p99:.0f}/mês).
  A mediana mostra a verdade: metade do Brasil vive com R$ {brasil.mediana:.0f} ou menos.

  O 1% MAIS RICO detém {brasil.topo_1pct_participacao:.1f}% de toda a renda.
  OS 50% MAIS POBRES detêm {brasil.base_50pct_participacao:.1f}% de toda a renda.
  Razão: {brasil.topo_1pct_participacao / brasil.base_50pct_participacao:.1f}x

  GAPS:
    Racial:  branco ganha {brasil.raca_gap:.2f}x o negro
    Gênero:  homem ganha {brasil.genero_gap:.2f}x a mulher
    Negro + mulher: R$ {brasil.renda_negro_p50 * 0.75:.0f}/mês (estimado)
""")

    print(f"{'='*95}")
    print("DISTRIBUIÇÃO NACIONAL (quem ganha o quê)")
    print(f"{'='*95}")
    print(f"\n{'PERCENTIL':<12} {'RENDA/MÊS':>12} {'QUEM SÃO':<50}")
    print("-" * 75)
    for p, r, desc in [
        ("P10", brasil.p10, "10% mais pobre. Fome. Sem teto."),
        ("P25", brasil.p25, "Trabalhador informal. Periferia."),
        ("P50", brasil.p50, "MEDIANA. Metade do Brasil vive com isto ou menos."),
        ("P75", brasil.p75, "CLT formal. Classe média baixa."),
        ("P90", brasil.p90, "Classe média. Diploma universitário."),
        ("P99", brasil.p99, "1% mais rico. Elite. Dono de empresa/herdeiro."),
    ]:
        print(f"  {p:<10} R$ {r:>8,.0f}    {desc}")

    print(f"\n{'='*95}")
    print("POR ESTADO: MÉDIA vs MEDIANA vs DESIGUALDADE")
    print(f"{'='*95}")
    print(f"\n{'UF':<4} {'ESTADO':<22} {'MÉDIA':>8} {'MEDIANA':>9} {'P10':>7} {'P99':>9} {'DESIG':>7} {'RACA':>6}")
    print("-" * 80)
    for e in sorted(estados, key=lambda x: x.desigualdade, reverse=True):
        if e.estado == "BR":
            continue
        print(f"  {e.estado:<3} {e.nome_estado:<21} R${e.media_mentirosa:>6,.0f}  R${e.mediana:>6,.0f}  R${e.p10:>5,.0f}  R${e.p99:>7,.0f}  {e.desigualdade:>6.1f}x  {e.raca_gap:.1f}x")

    print(f"\n{'='*95}")
    print("O QUE ISSO SIGNIFICA")
    print(f"{'='*95}")
    print(f"""
  ACRE (pior desigualdade):
    Mediana: R$ 900. P10: R$ 100. P99: R$ 12.000.
    Desigualdade: 120x (topo ganha 120x a base)
    8% em indigência (R$ 0-100/mês). 15% em miséria.

  MARANHÃO (pior mediana):
    Mediana: R$ 550. Metade do estado vive com isto ou menos.
    12% em indigência. Renda negro: R$ 400.
    O MA destrói a narrativa de "Brasil emergente".

  DF (maior mediana, maior gap racial):
    Mediana: R$ 2.200. Mas negro ganha R$ 1.600, branco R$ 3.500.
    Gap racial: 2.19x (pior do país).
    Brasília: contraste entre plano piloto (elite) e periferia (fome).

  SANTA CATARINA (melhor distribuição):
    Mediana: R$ 1.900. Gap racial menor: 1.57x.
    Mas ainda: 3% em indigência. Não é paraíso.

  NENHUM ESTADO É BOM. Todos têm pobres. Todos têm desigualdade.
  A média esconde. A distribuição revela.
""")


if __name__ == "__main__":
    _demo()
