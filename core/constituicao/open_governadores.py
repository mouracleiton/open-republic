#!/usr/bin/env python3
"""
OpenGovernadores -- 27 Governadores da Frente Unificada
=========================================================
"Governador que não resolve o Raio X do seu estado = W.O."
Um por estado. Score >= 4.0 ou EM_ANALISE (cargo técnico).

AVISO: TODOS os nomes sao MOCK (placeholder).
Score = OPINIAO (0.5/7 no Gate Epistemológico).
Composição final só após triangulação de fontes.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List
from collections import defaultdict


class StatusGov(Enum):
    APROVADO = "APROVADO"        # score >= 4.0
    EM_ANALISE = "EM_ANALISE"   # score < 4.0, entra por habilidade regional
    VAZIO = "VAZIO"              # sem candidato


@dataclass
class Governador:
    """Um candidato a governador da frente unificada."""
    estado: str                  # sigla UF
    nome_estado: str             # nome completo
    nome: str                    # MOCK (placeholder)
    origem: str                  # de onde veio (histórico)
    habilidade: str              # o que sabe fazer
    score: float                 # 0-5.0
    status: StatusGov
    alinhamento_raiox: str       # qual eixo do Raio X mais urgente no estado
    evidencia: str               # o que FEZ
    problema_estado: str         # maior problema do estado


def _init_governadores() -> List[Governador]:
    return [
        # NORTE
        Governador("AC", "Acre", "[MOCK - a definir]",
            "seringal", "extrativismo, ambiente",
            0.0, StatusGov.VAZIO, "ambiente",
            "A definir.", "Desmatamento + narcotráfico."),

        Governador("AM", "Amazonas", "[MOCK - a definir]",
            "Amazônia", "floresta, povos originários",
            0.0, StatusGov.VAZIO, "ambiente",
            "A definir.", "Desmatamento recorde. Manaus pobreza."),

        Governador("AP", "Amapá", "[MOCK - a definir]",
            "norte", "mineração, floresta",
            0.0, StatusGov.VAZIO, "ambiente",
            "A definir.", "Ilhas sem luz. Pobreza extrema."),

        Governador("PA", "Pará", "[MOCK - a definir]",
            "Amazônia", "garimpo, floresta, violência",
            0.0, StatusGov.VAZIO, "violencia",
            "A definir.", "Garimpo ilegal. Violência rural. Marajó."),

        Governador("RO", "Rondônia", "[MOCK - a definir]",
            "norte", "desmatamento, pecuária",
            0.0, StatusGov.VAZIO, "ambiente",
            "A definir.", "Desmatamento. Pecuária ilegal."),

        Governador("RR", "Roraima", "[MOCK - a definir]",
            "norte", "Yanomami, fronteira",
            0.0, StatusGov.VAZIO, "indigena",
            "A definir.", "Crise Yanomami. Imigração Venezuela."),

        Governador("TO", "Tocantins", "[MOCK - a definir]",
            "norte", "agronegócio, cerrado",
            0.0, StatusGov.VAZIO, "agropecuaria",
            "A definir.", "Agronegócio predatório. Trabalho escravo."),

        # NORDESTE
        Governador("MA", "Maranhão", "[MOCK - a definir]",
            "nordeste", "segurança, pobreza",
            0.0, StatusGov.VAZIO, "violencia",
            "A definir.", "Pobreza extrema. Violência rural."),

        Governador("PI", "Piauí", "[MOCK - a definir]",
            "nordeste", "semi-árido, seca",
            0.0, StatusGov.VAZIO, "agua",
            "A definir.", "Seca. Migração. Pobreza."),

        Governador("CE", "Ceará", "Camilo Santana",
            "gestão pública", "educação, saúde, gestão",
            4.72, StatusGov.APROVADO, "educacao",
            "Governador 2x. IDEB subiu. Vacinação 95%.",
            "IDEB baixo. Violência em Fortaleza."),

        Governador("RN", "Rio Grande do Norte", "[MOCK - a definir]",
            "nordeste", "segurança, turismo",
            0.0, StatusGov.VAZIO, "violencia",
            "A definir.", "Natal: violência. Pobreza litoral."),

        Governador("PB", "Paraíba", "[MOCK - a definir]",
            "nordeste", "semi-árido, educação",
            0.0, StatusGov.VAZIO, "agua",
            "A definir.", "Seca. Campina Grande subemprego."),

        Governador("PE", "Pernambuco", "Humberto Costa",
            "gestão pública", "saúde, região metropolitana",
            3.40, StatusGov.EM_ANALISE, "saude",
            "Senador. Ex-ministro Saúde. Gestão NE.",
            "Recife: violência. Interior: seca."),

        Governador("AL", "Alagoas", "[MOCK - a definir]",
            "nordeste", "pobreza, educação",
            0.0, StatusGov.VAZIO, "educacao",
            "A definir.", "Pior IDH do Brasil. Analfabetismo."),

        Governador("SE", "Sergipe", "[MOCK - a definir]",
            "nordeste", "petróleo, pobreza",
            0.0, StatusGov.VAZIO, "saude",
            "A definir.", "Pobreza. Saneamento zero."),

        Governador("BA", "Bahia", "[MOCK - a definir]",
            "nordeste", "cultura, violência, racial",
            0.0, StatusGov.VAZIO, "violencia",
            "A definir.", "Salvador: violência. Negro 80%. Semi-árido."),

        # CENTRO-OESTE
        Governador("MT", "Mato Grosso", "[MOCK - a definir]",
            "centro-oeste", "agronegócio, floresta",
            0.0, StatusGov.VAZIO, "agropecuaria",
            "A definir.", "Desmatamento. Pecuária. Trabalho escravo."),

        Governador("MS", "Mato Grosso do Sul", "[MOCK - a definir]",
            "centro-oeste", "fronteira, pecuária",
            0.0, StatusGov.VAZIO, "violencia",
            "A definir.", "Violência fronteiriça. Indígena Guarani."),

        Governador("GO", "Goiás", "[MOCK - a definir]",
            "centro-oeste", "agronegócio, cerrado",
            0.0, StatusGov.VAZIO, "saude",
            "A definir.", "Goiânia crescimento desordenado."),

        Governador("DF", "Distrito Federal", "Aguinaldo Ribeiro",
            "gestão pública", "planejamento, administration pública",
            2.80, StatusGov.EM_ANALISE, "violencia",
            "Deputado. Gestão pública DF.",
            "Brasília: contraste riqueza/plano piloto vs periferia."),

        # SUDESTE
        Governador("SP", "São Paulo", "[MOCK - a definir]",
            "sudeste", "indústria, periferia, transporte",
            0.0, StatusGov.VAZIO, "violencia",
            "A definir.", "45M habitantes. Periferia: violência, drogas."),

        Governador("RJ", "Rio de Janeiro", "[MOCK - a definir]",
            "sudeste", "segurança, favelas, petróleo",
            0.0, StatusGov.VAZIO, "violencia",
            "A definir.", "Favelas: guerra. Polícia mata mais que EUA."),

        Governador("MG", "Minas Gerais", "Patrus Ananias",
            "gestão pública", "cidades, habitação",
            3.29, StatusGov.EM_ANALISE, "habitacao",
            "Ministro Cidades 2x. MCMV. Saneamento.",
            "Interior: pobreza. Brumadinho. Saneamento."),

        Governador("ES", "Espírito Santo", "[MOCK - a definir]",
            "sudeste", "petróleo, marém",
            0.0, StatusGov.VAZIO, "saude",
            "A definir.", "Petróleo vs pobreza. Marés."),

        # SUL
        Governador("PR", "Paraná", "[MOCK - a definir]",
            "sul", "agronegócio, indústria",
            0.0, StatusGov.VAZIO, "emprego",
            "A definir.", "Agronegócio. Curitiba desemprego."),

        Governador("SC", "Santa Catarina", "[MOCK - a definir]",
            "sul", "indústria, tecnologia",
            0.0, StatusGov.VAZIO, "saude",
            "A definir.", "Conservadorismo. Sul: desemprego."),

        Governador("RS", "Rio Grande do Sul", "Erika Hilton",
            "movimento popular", "direitos, periferia, reconstrução",
            1.67, StatusGov.EM_ANALISE, "habitacao",
            "Deputada. Vereadora. Reconstrução pós-enchente 2024.",
            "Enchente 2024: 500k desabrigados. Reconstrução."),
    ]


def scorecard() -> Dict[str, Any]:
    govs = _init_governadores()
    n_aprovados = sum(1 for g in govs if g.status == StatusGov.APROVADO)
    n_em_analise = sum(1 for g in govs if g.status == StatusGov.EM_ANALISE)
    n_vazios = sum(1 for g in govs if g.status == StatusGov.VAZIO)

    return {
        "modulo": "open_governadores",
        "versao": "0.1.0-spec",
        "total_estados": len(govs),
        "aprovados": n_aprovados,
        "em_analise": n_em_analise,
        "vazios": n_vazios,
        "cobertura": f"{n_aprovados + n_em_analise}/{len(govs)}",
        "criterio_corte": ">= 4.0",
    }


def _demo():
    govs = _init_governadores()
    sc = scorecard()

    print("=" * 90)
    print("FRENTE UNIFICADA — 27 GOVERNADORES")
    print("=" * 90)

    print(f"""
  27 estados (26 + DF)

  APROVADOS (>= 4.0):   {sc['aprovados']}
  EM ANÁLISE (< 4.0):   {sc['em_analise']}
  VAZIOS (sem nome):    {sc['vazios']}
  COBERTURA:            {sc['cobertura']}
""")

    # Por regiao
    regioes = {
        "NORTE": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
        "NORDESTE": ["MA", "PI", "CE", "RN", "PB", "PE", "AL", "SE", "BA"],
        "CENTRO-OESTE": ["MT", "MS", "GO", "DF"],
        "SUDESTE": ["SP", "RJ", "MG", "ES"],
        "SUL": ["PR", "SC", "RS"],
    }

    for regiao, ufs in regioes.items():
        print(f"\n{'='*90}")
        print(f"{regiao}")
        print(f"{'='*90}")
        for g in govs:
            if g.estado in ufs:
                if g.status == StatusGov.APROVADO:
                    flag = " *** APROVADO"
                    score_str = f"[{g.score:.2f}]"
                elif g.status == StatusGov.EM_ANALISE:
                    flag = " (em análise)"
                    score_str = f"[{g.score:.2f}]"
                else:
                    flag = " *** VAZIO"
                    score_str = "[----]"
                print(f"""
  {g.estado} ({g.nome_estado}){flag}
    NOME: {g.nome}
    SCORE: {score_str}
    PROBLEMA: {g.problema_estado}
    ALINHAMENTO: {g.alinhamento_raiox}
    EVIDÊNCIA: {g.evidencia}""")

    print(f"\n{'='*90}")
    print("VEREDITO")
    print(f"{'='*90}")
    print(f"""
  {sc['aprovados']} de 27 com nome e score >= 4.0.
  {sc['em_analise']} com nome mas score < 4.0 (entra por habilidade).
  {sc['vazios']} SEM NOME. Precisa de gente.

  Cada estado tem um problema diferente.
  O governador precisa alinhar com o Raio X do SEU estado.
  Camilo no CE resolveu educação. Marina na Amazônia resolveu desmatamento.
  Não existe governador genérico. Existe o que resolve o problema local.

  Para preencher os {sc['vazios']} vazios:
  Cada candidato passa pelo Gate WO.
  Score >= 4.0 + alinhamento estadual = APROVADO.
""")


if __name__ == "__main__":
    _demo()
