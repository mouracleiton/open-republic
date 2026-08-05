#!/usr/bin/env python3
"""
OpenSimulacaoSatisfacao -- Simulacao de Satisfacao da Frente Comunista Unida
===============================================================================
"Toda coalizao tem tenso. A pergunta : quem fica feliz e quem engole sapo?"
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


class NivelSatisfacao(Enum):
    MUITO_SATISFEITO = "MUITO_SATISFEITO"    # ganhou o que queria
    SATISFEITO = "SATISFEITO"                 # maioria dos interesses atendida
    NEUTRO = "NEUTRO"                         # nem ganhou nem perdeu
    INSATISFEITO = "INSATISFEITO"             # abriu mo de algo importante
    MUITO_INSATISFEITO = "MUITO_INSATISFEITO" # traiu principio fundamental


@dataclass
class DemandasPartido:
    """O que cada partido quer da coalizao."""
    partido: str
    lider: str
    score_capacidade: float

    # Demandas (0-10 de importancia)
    demandas: Dict[str, int]  # area -> importancia

    # Nao negociavel (principio que nao cede)
    nao_negociavel: str

    # O que aporta
    aporta: List[str]


@dataclass
class ResultadoSatisfacao:
    """Resultado da simulacao para cada partido em cada eixo."""
    partido: str
    lider: str
    eixo: str
    demanda_importancia: int         # 0-10 (quanto queria)
    proposta_resultado: str          # o que a coalizao decidiu
    cedeu: bool                      # abriu mo?
    nivel: NivelSatisfacao
    pontos_ganhos: int               # 0-10 (quanto ganhou)
    delta: int                       # pontos_ganhos - importancia


def _init_demandas() -> List[DemandasPartido]:
    return [

        DemandasPartido(
            partido="UP", lider="Samara Martins", score_capacidade=1.50,
            demandas={
                "alimentacao": 10, "habitacao": 10, "saude": 9, "emprego": 9,
                "agropecuaria": 10, "violencia": 8, "economia": 10,
                "transporte": 8, "educacao": 9, "comunicacao": 9,
                "drogas": 7, "ambiente": 8, "indigena": 8,
            },
            nao_negociavel="Socialismo. Nacionalizao dos meios de produo. Sem retrocesso.",
            aporta=["Programa de 25 pontos", "Base MTST", "Autossustentao financeira"],
        ),

        DemandasPartido(
            partido="PCB", lider="Jones Manoel", score_capacidade=2.50,
            demandas={
                "comunicacao": 10, "economia": 10, "educacao": 8,
                "emprego": 9, "violencia": 8, "cultura": 9,
                "habitacao": 8, "drogas": 7,
            },
            nao_negociavel="Socialismo cientifico. Sem reformismo. Critica ao capitalismo.",
            aporta=["Comunicao (~2M)", "Anlise econmica", "10 anos de coerencia"],
        ),

        DemandasPartido(
            partido="PT", lider="Lula / Camilo / Haddad", score_capacidade=4.03,
            demandas={
                "saude": 9, "educacao": 10, "economia": 9, "habitacao": 9,
                "saneamento": 8, "alimentacao": 10, "emprego": 8,
            },
            nao_negociavel="Democracia representativa. Instituies. Sem ruptura constitucional.",
            aporta=["Mquina governista", "Ministrios", "Quadros tcnicos", "Experiencia executiva"],
        ),

        DemandasPartido(
            partido="PSOL", lider="Sonia Guajajara / Erika Hilton", score_capacidade=2.67,
            demandas={
                "indigena": 10, "ambiente": 10, "violencia": 9, "drogas": 9,
                "cultura": 9, "habitacao": 8, "saude": 7,
            },
            nao_negociavel="Autonomia. Direitos LGBTQIA+. Direitos indgenas. Aborto legal.",
            aporta=["Mobilizao de rua", "Pauta de direitos", "Visibilidade"],
        ),

        DemandasPartido(
            partido="PCdoB", lider="Jandira Feghali / Orlando Silva", score_capacidade=3.00,
            demandas={
                "saude": 10, "educacao": 9, "cultura": 7, "emprego": 7,
            },
            nao_negociavel="SUS universal. Sem privatizao da sade.",
            aporta=["Quadros tcnicos sade", "Experiencia ministerial"],
        ),

        DemandasPartido(
            partido="REDE", lider="Marina Silva", score_capacidade=4.11,
            demandas={
                "ambiente": 10, "agua": 10, "alimentacao": 9,
                "agropecuaria": 8, "indigena": 7,
            },
            nao_negociavel="Agenda ambiental. Sem retrocesso florestal.",
            aporta=["PPCDAm (-80% desmatamento)", "Cisternas", "PAA"],
        ),

        DemandasPartido(
            partido="PDT", lider="Ciro Gomes", score_capacidade=3.81,
            demandas={
                "economia": 9, "energia": 10, "transporte": 9,
                "habitacao": 7, "saneamento": 8,
            },
            nao_negociavel="Desenvolvimento nacional. Industrializao. Federalismo.",
            aporta=["Transposio So Francisco", "Experiencia infraestrutura"],
        ),

        DemandasPartido(
            partido="PSTU", lider="Hertz Dias", score_capacidade=1.30,
            demandas={
                "emprego": 10, "violencia": 8, "economia": 9,
            },
            nao_negociavel="Socialismo pela revoluo. Sem participao em governo burgus.",
            aporta=["Mobilizao sindical", "Critica anticapitalista"],
        ),

        DemandasPartido(
            partido="PCO", lider="Rui Costa Pimenta", score_capacidade=1.20,
            demandas={
                "economia": 10, "emprego": 9,
            },
            nao_negociavel="Fim do capitalismo. Sem acordo com a burguesia.",
            aporta=["Critica. Observador."],
        ),
    ]


# ============================================================
# SIMULACAO: o que a coalizao decide em cada eixo
# ============================================================

DECISOES_DA_COALIZAO = {
    "violencia": {
        "decisao": "Desmilitarizao da PM em 4 fases. Investimento em preveno > represso. Conselhos populares de segurana.",
        "lideranca": "Jones Manoel (PCB) coordena. PT executa transio.",
        "quem_ganhou": ["UP", "PSOL", "PCB", "PSTU"],
        "quem_cedeu": ["PT"],
        "motivo_cediu": "PT quer manter estrutura policial. Cede pela coalizo.",
    },
    "saude": {
        "decisao": "SUS universal. Fim dos planos privados. Mais Medicos expandido. 8% PIB em sade.",
        "lideranca": "PCdoB (Jandira Feghali). PT aporta Ministrio.",
        "quem_ganhou": ["UP", "PCdoB", "PT", "PSOL"],
        "quem_cedeu": [],
        "motivo_cediu": "Todos concordam. Sem tenso.",
    },
    "alimentacao": {
        "decisao": "PAA ampliado. CONSEA reativado. Rastreio individual. BF R$700. Cisternas.",
        "lideranca": "REDE (Marina). UP aporta reforma agrria.",
        "quem_ganhou": ["UP", "REDE", "PT"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso total. Fome une.",
    },
    "agua": {
        "decisao": "1M cisternas. Saneamento estatizado. Marco Legal revertido.",
        "lideranca": "REDE (Marina). PDT aporta infraestrutura.",
        "quem_ganhou": ["REDE", "UP", "PDT"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
    "soberania_alimentar": {
        "decisao": "Reforma agrria. Producao nacional de trigo. Fertilizantes nacionais.",
        "lideranca": "UP. PCB aporta planificao.",
        "quem_ganhou": ["UP", "PCB", "REDE"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
    "educacao": {
        "decisao": "Escola integral 7h-17h. Piso nacional professor R$8k. Fim do vestibular. Federalizao.",
        "lideranca": "PCdoB. PT aporta Camilo Santana.",
        "quem_ganhou": ["UP", "PCdoB", "PT", "PSOL"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
    "emprego": {
        "decisao": "Emprego garantido pelo Estado. Jornada 6h. Aumento real do salrio.",
        "lideranca": "PCB (Jones). PSTU aporta mobilizao.",
        "quem_ganhou": ["UP", "PCB", "PSTU", "PT"],
        "quem_cedeu": ["PDT"],
        "motivo_cediu": "PDT prefere modelo empresarial. Cede.",
    },
    "economia": {
        "decisao": "Nacionalizao bancria gradual. ISF. Auditoria da dvida. Planificao econmica.",
        "lideranca": "PCB (Jones). UP aporta programa.",
        "quem_ganhou": ["UP", "PCB", "PSTU", "PCO"],
        "quem_cedeu": ["PT", "PDT"],
        "motivo_cediu": "PT defende democracia representativa + mercado. Cede a maior parte mas exige transio gradual.",
    },
    "ambiente": {
        "decisao": "PPCDAm reativado. Desmatamento zero. Controle popular da Amaznia.",
        "lideranca": "REDE (Marina). PSOL aporta Sonia.",
        "quem_ganhou": ["REDE", "PSOL", "UP"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
    "indigena": {
        "decisao": "Demarcao imediata das 251 terras. Expulso de garimpos. Sade indgena DSEI.",
        "lideranca": "PSOL (Sonia Guajajara).",
        "quem_ganhou": ["PSOL", "REDE", "UP"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
    "agropecuaria": {
        "decisao": "Reforma agrria popular. Nacionalizao da terra. Fim do latifndio.",
        "lideranca": "UP. PCB aporta planificao.",
        "quem_ganhou": ["UP", "PCB", "PSOL", "REDE"],
        "quem_cedeu": ["PDT"],
        "motivo_cediu": "PDT tem base agrcola. Cede.",
    },
    "energia": {
        "decisao": "Reestatizao. Petrobras 100% estatal. Fim dos leiles. Tarifa social.",
        "lideranca": "PDT (Ciro). PCB aporta estatizao.",
        "quem_ganhou": ["PDT", "PCB", "UP"],
        "quem_cedeu": ["PT"],
        "motivo_cediu": "PT privatizou petrleo parcialmente. Cede pela coalizo.",
    },
    "transporte": {
        "decisao": "Estatizao do transporte coletivo. Tarifa zero. Frota eltrica.",
        "lideranca": "UP. PDT aporta expertise.",
        "quem_ganhou": ["UP", "PDT", "PSOL"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
    "habitacao": {
        "decisao": "Imveis vazios para o dficit. Reforma urbana. 4 milhes de moradias.",
        "lideranca": "UP. PT aporta MCMV.",
        "quem_ganhou": ["UP", "PT", "PSOL"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
    "saneamento": {
        "decisao": "Marco Legal revertido. Estatizao. 90% cobertura de esgoto em 4 anos.",
        "lideranca": "PT. PDT aporta infraestrutura.",
        "quem_ganhou": ["PT", "PDT", "UP"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
    "drogas": {
        "decisao": "Reduo de danos. Descriminalizao. Tratamento ampliado. Fim da guerra s drogas.",
        "lideranca": "PSOL. PCdoB aporta sade.",
        "quem_ganhou": ["PSOL", "PCdoB", "UP"],
        "quem_cedeu": ["REDE"],
        "motivo_cediu": "Marina  evanglica. Cede pela coalizo mas com reservas.",
    },
    "cultura": {
        "decisao": "Cotizao 40% nacional. Financiamento pblico direto. Cultura popular.",
        "lideranca": "PSOL. PCB aporta nacionalizao.",
        "quem_ganhou": ["PSOL", "PCB", "UP"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
    "comunicacao": {
        "decisao": "Democratizao da mdia. Fim do monoplio. Internet universal.",
        "lideranca": "PCB (Jones). PSOL apoia.",
        "quem_ganhou": ["PCB", "PSOL", "UP"],
        "quem_cedeu": [],
        "motivo_cediu": "Consenso.",
    },
}


def simular() -> List[ResultadoSatisfacao]:
    """Simula satisfacao de cada partido em cada eixo."""
    demandas = _init_demandas()
    resultados = []

    for partido in demandas:
        for eixo, decisao_info in DECISOES_DA_COALIZAO.items():
            importancia = partido.demandas.get(eixo, 0)

            if importancia == 0:
                continue  # partido nao tem demanda neste eixo

            ganhou = partido.partido in decisao_info["quem_ganhou"]
            cedeu = partido.partido in decisao_info["quem_cedeu"]

            if ganhou:
                pontos = importancia
                nivel = NivelSatisfacao.MUITO_SATISFEITO if importancia >= 8 else NivelSatisfacao.SATISFEITO
            elif cedeu:
                pontos = max(0, importancia - 5)
                nivel = NivelSatisfacao.INSATISFEITO if importancia >= 7 else NivelSatisfacao.NEUTRO
            else:
                pontos = max(0, importancia - 2)
                nivel = NivelSatisfacao.NEUTRO

            resultados.append(ResultadoSatisfacao(
                partido=partido.partido, lider=partido.lider, eixo=eixo,
                demanda_importancia=importancia,
                proposta_resultado=decisao_info["decisao"][:60],
                cedeu=cedeu, nivel=nivel,
                pontos_ganhos=pontos, delta=pontos - importancia,
            ))

    return resultados


def _demo():
    resultados = simular()

    print("=" * 90)
    print("SIMULAO DE SATISFAO — FRENTE COMUNISTA UNIDA")
    print("9 partidos x 18 eixos do Raio X")
    print("=" * 90)

    # Score por partido
    print(f"\n{'='*90}")
    print("SCORE DE SATISFAO POR PARTIDO")
    print(f"{'='*90}")

    por_partido = defaultdict(list)
    for r in resultados:
        por_partido[r.partido].append(r)

    scores_finais = []
    for partido, rs in sorted(por_partido.items(), key=lambda x: x[0]):
        total_demandas = sum(r.demanda_importancia for r in rs)
        total_ganhos = sum(r.pontos_ganhos for r in rs)
        n_ganhou = sum(1 for r in rs if not r.cedeu and r.delta == 0)
        n_cedeu = sum(1 for r in rs if r.cedeu)
        pct_satisfacao = (total_ganhos / total_demandas * 100) if total_demandas else 0
        lider = rs[0].lider

        scores_finais.append({
            "partido": partido, "lider": lider,
            "demandas": len(rs), "ganhou": n_ganhou, "cedeu": n_cedeu,
            "pct": round(pct_satisfacao, 1),
        })

        cedeu_eixos = [r.eixo for r in rs if r.cedeu]
        print(f"\n  [{partido}] {lider}")
        print(f"    Demandas: {len(rs)} | Ganhou: {n_ganhou} | Cedeu: {n_cedeu}")
        print(f"    SATISFAO: {pct_satisfacao:.1f}%")
        if cedeu_eixos:
            print(f"    Cedeu em: {', '.join(cedeu_eixos)}")

    # Ranking
    print(f"\n{'='*90}")
    print("RANKING DE SATISFAO")
    print(f"{'='*90}")
    scores_finais.sort(key=lambda x: x["pct"], reverse=True)
    for i, s in enumerate(scores_finais):
        bar = "#" * int(s["pct"] / 5)
        flag = " *** TENSO" if s["pct"] < 50 else ""
        print(f"  {i+1}. {s['partido']:<8} {s['pct']:>5.1f}%  {bar}{flag}")

    # Eixos com tenso
    print(f"\n{'='*90}")
    print("EIXOS COM TENSO (alguem cedeu)")
    print(f"{'='*90}")
    for eixo, info in DECISOES_DA_COALIZAO.items():
        if info["quem_cedeu"]:
            print(f"\n  [{eixo.upper()}]")
            print(f"    Deciso: {info['decisao'][:70]}")
            print(f"    Ganhou: {', '.join(info['quem_ganhou'])}")
            print(f"    CEDEU: {', '.join(info['quem_cedeu'])} -- {info['motivo_cediu']}")

    # Veredito
    print(f"\n{'='*90}")
    print("VEREDITO DA SIMULAO")
    print(f"{'='*90}")

    satisfacao_media = sum(s["pct"] for s in scores_finais) / len(scores_finais)
    n_tensoes = sum(1 for info in DECISOES_DA_COALIZAO.values() if info["quem_cedeu"])
    n_consenso = 18 - n_tensoes

    print(f"""
  18 eixos decididos pela coalizo.
  {n_consenso} por CONSENSO (ningum cedeu).
  {n_tensoes} com TENSO (algum abriu mo).

  SATISFAO MDIA DA COALIZO: {satisfacao_media:.1f}%

  QUEM FICA MAIS FELIZ:
""")

    for s in scores_finais[:3]:
        print(f"    {s['partido']:<8} ({s['lider'][:20]:<20}) {s['pct']:.1f}%")

    print(f"""
  QUEM ENGOLE SAPO:
""")
    for s in scores_finais[-3:]:
        print(f"    {s['partido']:<8} ({s['lider'][:20]:<20}) {s['pct']:.1f}%")

    # Risco de ruptura
    print(f"""
  RISCO DE RUPTURA:
""")
    for s in scores_finais:
        if s["pct"] < 50:
            print(f"    *** {s['partido']} ({s['pct']:.1f}%) -- ALTO RISCO")
        elif s["pct"] < 70:
            print(f"    {s['partido']} ({s['pct']:.1f}%) -- RISCO MODERADO")
    if not any(s["pct"] < 50 for s in scores_finais):
        print(f"    Nenhum partido abaixo de 50%. Coalizo estvel.")

    print(f"""
  FONTE DE TENSO PRINCIPAL: Economia.
  PCB/UP/PSTU/PCO querem nacionalizao. PT/PDT querem mercado regulado.
  PT cede (quer coalizo). PDT cede (quer infraestrutura).
  Mas PT  o nico partido com score >= 4.0 e mquina executiva.
  Sem PT, no h governo. Sem UP/PCB, no h diagnstico.

  O sensor (OpenRepublic) no decide quem cede.
  O sensor ILUMINA quem cede e por qu.
  O povo cobra se a deciso resolveu o Raio X.
""")


if __name__ == "__main__":
    _demo()
