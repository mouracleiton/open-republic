#!/usr/bin/env python3
"""
OpenSatisfacaoPopulacao -- A Única Métrica que Importa
=========================================================
"Partido é ferramenta. População é fim.
 Se a ferramenta não resolve, troca. Não celebra."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List
from collections import defaultdict


# ============================================================
# OS 18 PROBLEMAS (não eixos, não políticas -- PROBLEMAS)
# ============================================================

@dataclass
class Problema:
    """Um problema real que mata ou machuca brasileiros."""
    id: str
    nome: str
    descricao: str
    pessoas_afetadas_milhoes: float     # QUANTAS PESSOAS SOFREM
    indicador_atual: str                # o número de HOJE
    meta: str                           # o número que resolve
    fonte: str                          # de onde veio o número
    custo_resolver: str                 # QUANTO CUSTA
    prazo_resolver: str                 # QUANDO
    partido_executor: str               # QUEM faz (ferramenta)
    cobertura_esperada_pct: float       # % que a política cobre


def _init_problemas() -> List[Problema]:
    return [
        Problema("fome", "33 milhões passando fome",
            "Insegurança alimentar grave. Crianças com desnutrição.",
            33.0, "33 milhões", "0 (fome zero)", "VIGISAN 2022",
            "R$ 50 bi/ano", "2 anos", "REDE+PT", 85),

        Problema("agua", "35 milhões sem água potável",
            "Sede real. Nordeste em emergência. Mercúrio nos rios.",
            35.0, "35 milhões", "0 (água universal)", "SNIS 2024",
            "R$ 30 bi/ano", "4 anos", "REDE+PDT", 75),

        Problema("violencia", "47.500 homicídios/ano",
            "130 mortes por dia. Polícia mata 6.000/ano. 1.8 feminicídio/dia.",
            47.5, "47.500/ano", "<15.000/ano", "FBSP 2024",
            "R$ 20 bi/ano", "4 anos", "PSOL+PCdoB", 60),

        Problema("saude", "70% dependem de SUS subfinanciado",
            "Fila 6 meses. Dengue 6M. 4% PIB vs 8% OCDE.",
            142.0, "4% PIB", "8% PIB", "MS/CNJ 2024",
            "R$ 80 bi/ano", "4 anos", "PCdoB+PT", 70),

        Problema("educacao", "PISA 377, 7.2M analfabetos funcionais",
            "40% escolas rurais sem água. Professor 3 escolas. R$5.500/aluno.",
            50.0, "PISA 377", "PISA 450", "INEP/OCDE 2024",
            "R$ 150 bi/ano", "4 anos", "PCdoB+PT", 65),

        Problema("esgoto", "100 milhões sem coleta de esgoto",
            "Doença. Contaminação. Marco Legal promete 99% em 2033. Ritmo: 0.5%/ano.",
            100.0, "100 milhões", "0 (universal)", "SNIS 2024",
            "R$ 25 bi/ano", "4 anos", "PT+PDT", 70),

        Problema("moradia", "8 milhões sem moradia digna",
            "2 milhões de imóveis vazios em capitais. Déficit habitacional.",
            8.0, "8 milhões", "0 (déficit zero)", "IBGE 2024",
            "R$ 35 bi/ano", "4 anos", "UP+PT", 75),

        Problema("desemprego", "8.5 milhões desempregados",
            "Informalidade 39%. Renda média R$2.800. Jovem sem perspectiva.",
            8.5, "7.9% desemprego", "<4%", "IBGE/PNAD 2024",
            "R$ 120 bi/ano", "4 anos", "PCB+PT", 55),

        Problema("indigena", "251 terras sem demarcação",
            "305 etnias. Yanomami em crise. Mercúrio. Garimpo.",
            1.7, "251 pendentes", "0 (todas demarcadas)", "Funai 2024",
            "R$ 5 bi/ano", "2 anos", "PSOL", 80),

        Problema("desmatamento", "13.235 km²/ano desmatados",
            "Amazônia 30% degradada. 1.500 garimpos. Marina reduziu 80% antes.",
            25.0, "13.235 km²/ano", "<3.000 km²/ano", "PRODES/INPE 2024",
            "R$ 10 bi/ano", "4 anos", "REDE", 75),

        Problema("drogas", "17% dependentes sem tratamento",
            "Guerra às drogas falhou. Caps AD insuficiente. Tráfico armado.",
            10.0, "17% sem tratamento", "100% com tratamento", "SENAD 2024",
            "R$ 8 bi/ano", "4 anos", "PSOL+PCdoB", 60),

        Problema("trigo", "80% do trigo importado",
            "Dependência externa. Fertilizantes 80% importados. Soberania zero.",
            203.0, "80% importado", "50% nacional", "CONAB 2024",
            "R$ 20 bi/ano", "4 anos", "UP+PCB", 50),

        Problema("terra", "Gini de terra 0.85",
            "5% detêm 70%. 120M hectares improdutivos. 1.1M assentados em 30 anos.",
            15.0, "Gini 0.85", "Gini <0.6", "INCRA 2024",
            "R$ 15 bi/ano", "4 anos", "UP+PCB", 55),

        Problema("tarifa_transporte", "30 mortes/dia no trânsito",
            "Tarifa R$5,50. Frota velha. 60% privada.",
            50.0, "30/dia", "<10/dia", "ANTP 2024",
            "R$ 40 bi/ano", "4 anos", "PDT+UP", 65),

        Problema("energia_custo", "Tarifa de energia entre as mais caras do mundo",
            "Acesso 99% mas custo proíbe. Pré-sal privatizado.",
            100.0, "Tarifa altíssima", "Tarifa social", "ANEEL 2024",
            "R$ 60 bi/ano", "4 anos", "PDT+PCB", 60),

        Problema("corrupcao", "R$ 200 bi/ano em corrupção",
            "Recuperado: 2.5%. 80M processos. 5 anos por processo.",
            203.0, "R$ 200 bi/ano", "R$ 50 bi recuperado", "CGU 2024",
            "R$ 1 bi/ano", "Imediato", "UP+PCdoB", 40),

        Problema("cultura_dom", "80% conteúdo audiovisual estrangeiro",
            "Cultura = 1.6% PIB. Sem financiamento público direto.",
            30.0, "80% estrangeiro", "50% nacional", "IBGE 2022",
            "R$ 3 bi/ano", "2 anos", "PCB+PSOL", 55),

        Problema("midia", "6 grupos controlam 80% da mídia",
            "Concentração. 35% zona rural sem internet.",
            70.0, "6 grupos = 80%", "Herfindahl <0.3", "Anatel 2024",
            "R$ 5 bi/ano", "4 anos", "PCB+PSOL", 50),
    ]


# ============================================================
# SIMULAÇÃO: O QUE A COALIZÃO FAZ PELA POPULAÇÃO
# ============================================================

def simular() -> Dict[str, Any]:
    """
    A única métrica: quantas pessoas deixaram de sofrer?
    """
    problemas = _init_problemas()

    total_sofrendo = 0.0
    total_resolvido = 0.0
    total_restante = 0.0

    por_executor = defaultdict(lambda: {"resolvido": 0.0, "restante": 0.0})
    detalhes = []

    for p in problemas:
        resolvido = p.pessoas_afetadas_milhoes * (p.cobertura_esperada_pct / 100)
        restante = p.pessoas_afetadas_milhoes - resolvido

        total_sofrendo += p.pessoas_afetadas_milhoes
        total_resolvido += resolvido
        total_restante += restante

        for executor in p.partido_executor.split("+"):
            por_executor[executor]["resolvido"] += resolvido
            por_executor[executor]["restante"] += restante

        detalhes.append({
            "problema": p.nome,
            "pessoas": p.pessoas_afetadas_milhoes,
            "resolvido": round(resolvido, 1),
            "restante": round(restante, 1),
            "cobertura": p.cobertura_esperada_pct,
            "executor": p.partido_executor,
            "custo": p.custo_resolver,
            "prazo": p.prazo_resolver,
            "meta": p.meta,
            "indicador": p.indicador_atual,
            "fonte": p.fonte,
        })

    pct_resolvido = (total_resolvido / total_sofrendo * 100) if total_sofrendo > 0 else 0

    return {
        "total_sofrendo": round(total_sofrendo, 1),
        "total_resolvido": round(total_resolvido, 1),
        "total_restante": round(total_restante, 1),
        "pct_resolvido": round(pct_resolvido, 1),
        "por_executor": {k: {kk: round(vv, 1) for kk, vv in v.items()} for k, v in por_executor.items()},
        "detalhes": detalhes,
    }


def _demo():
    resultado = simular()

    print("=" * 90)
    print("A ÚNICA MÉTRICA QUE IMPORTA: A POPULAÇÃO COMEU?")
    print("=" * 90)

    print(f"""
  PARTIDO É FERRAMENTA. POPULAÇÃO É FIM.

  Sofrendo hoje:      {resultado['total_sofrendo']:.1f} milhões de pessoas
  Resolvido (coalizão): {resultado['total_resolvido']:.1f} milhões
  AINDA SOFRENDO:     {resultado['total_restante']:.1f} milhões

  COBERTURA: {resultado['pct_resolvido']:.1f}%
""")

    print(f"{'='*90}")
    print("PROBLEMA POR PROBLEMA: RESOLVEU OU NÃO?")
    print(f"{'='*90}")

    # Ordenar por restante (maior sofrimento restante primeiro)
    detalhes_ordenado = sorted(resultado["detalhes"], key=lambda x: x["restante"], reverse=True)

    for d in detalhes_ordenado:
        bar_res = "#" * int(d["cobertura"] / 5)
        bar_res = bar_res[:20]
        bar_rest = "-" * (20 - len(bar_res))
        print(f"""
  [{d['problema'].upper()}]
    PESSOAS:     {d['pessoas']:.1f}M sofrendo
    RESOLVIDO:  {d['resolvido']:.1f}M ({d['cobertura']}%)  [{bar_res}{bar_rest}]
    RESTANTE:   {d['restante']:.1f}M AINDA SOFRENDO
    EXECUTOR:   {d['executor']}
    META:       {d['indicador']} -> {d['meta']}
    CUSTO:      {d['custo']}
    PRAZO:      {d['prazo']}
    FONTE:      {d['fonte']}""")

    print(f"\n{'='*90}")
    print("QUEM RESOLVE MAIS SOFRIMENTO (ferramenta, não herói)")
    print(f"{'='*90}")
    print(f"\n{'EXECUTOR':<10} {'RESOLVEU':>10} {'RESTANTE':>10} {'COBERTURA':>10}")
    print("-" * 45)
    for executor, vals in sorted(resultado["por_executor"].items(), key=lambda x: x[1]["resolvido"], reverse=True):
        pct = vals["resolvido"] / (vals["resolvido"] + vals["restante"]) * 100 if (vals["resolvido"] + vals["restante"]) > 0 else 0
        print(f"  {executor:<8} {vals['resolvido']:>9.1f}M {vals['restante']:>9.1f}M {pct:>9.1f}%")

    print(f"\n{'='*90}")
    print("VEREDITO")
    print(f"{'='*90}")

    nao_resolvidos = [d for d in detalhes_ordenado if d["restante"] > 5]
    print(f"""
  A coalizão resolve {resultado['pct_resolvido']:.1f}% do sofrimento.
  {resultado['total_resolvido']:.1f} milhões param de sofrer.
  {resultado['total_restante']:.1f} milhões CONTINUAM sofrendo.

  MAIORES FALHAS (milhões ainda sofrendo):
""")
    for d in nao_resolvidos[:5]:
        print(f"    {d['problema']:<40} {d['restante']:.1f}M sofrendo")

    print(f"""
  O QUE ISSO SIGNIFICA:

  Não importa se 9 partidos estão felizes.
  Não importa se a coalizão sobrevive.
  Não importa quem ganhou a disputa interna.

  {resultado['total_restante']:.1f} milhões de pessoas AINDA SOFREM.

  Se você lidera uma nação, sua prioridade é ESTE número chegar a ZERO.
  Partido é ferramenta. Se a ferramenta não resolve, troca.
  Não celebra ferramenta que não aperta parafuso.

  "Se você está mais preocupado com disputa interna
   do que resolver 33 milhões em insegurança alimentar,
   pare neste exato momento e vá fazer outra coisa da sua vida."
""")


if __name__ == "__main__":
    _demo()
