#!/usr/bin/env python3
"""
OpenSatisfacaoCruzada -- Partido x População: Quem Serve a Quem?
===============================================================
"Cada partido tem demandas. A população tem necessidades.
O cruzamento revela: a coalizão satisfaz a quem?"
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


# ============================================================
# NECESSIDADES DA POPULAÇÃO (por segmento)
# ============================================================

@dataclass
class SegmentoPopulacao:
    """Um segmento da população brasileira com necessidades especificas."""
    nome: str
    tamanho_milhoes: float           # quantos milhões de pessoas
    descricao: str

    # Necessidade por eixo (0-10: 0 = nao precisa, 10 = sobrevivencia)
    necessidades: Dict[str, int]

    # Fonte do dado de tamanho
    fonte_tamanho: str


def _init_segmentos() -> List[SegmentoPopulacao]:
    return [
        SegmentoPopulacao(
            "famintos", 33.0,
            "Pessoas em insegurança alimentar grave.",
            {"alimentacao": 10, "saude": 7, "agua": 6, "soberania_alimentar": 8},
            "VIGISAN 2022"),

        SegmentoPopulacao(
            "periferia", 60.0,
            "Moradores de periferia urbana. Jovens, negros, informalidade.",
            {"violencia": 10, "saude": 9, "emprego": 9, "educacao": 8,
             "habitacao": 8, "transporte": 7, "drogas": 6},
            "IBGE 2022 (estimativa)"),

        SegmentoPopulacao(
            "sem_agua", 35.0,
            "Sem água potável ou esgoto.",
            {"agua": 10, "saneamento": 10, "saude": 8},
            "SNIS 2024"),

        SegmentoPopulacao(
            "indigenas", 1.7,
            "Povos originários. 305 etnias, 274 línguas.",
            {"indigena": 10, "saude": 9, "ambiente": 8, "agua": 7, "alimentacao": 7},
            "IBGE 2022"),

        SegmentoPopulacao(
            "nordeste_rural", 18.0,
            "Nordeste rural. Seca, pobreza, êxodo.",
            {"agua": 10, "alimentacao": 9, "saude": 8, "educacao": 8,
             "emprego": 7, "energia": 6},
            "IBGE 2022"),

        SegmentoPopulacao(
            "trabalhador_formal", 25.0,
            "CLT, renda R$2-5k. Quer segurança e serviços públicos.",
            {"saude": 8, "educacao": 8, "emprego": 7, "transporte": 7,
             "habitacao": 6, "economia": 6},
            "IBGE/PNAD 2024"),

        SegmentoPopulacao(
            "idosos", 22.0,
            "60+ anos. Dependem do SUS e da previdência.",
            {"saude": 10, "economia": 7},
            "IBGE 2022"),

        SegmentoPopulacao(
            "mulheres_violencia", 15.0,
            "Mulheres vítimas de violência doméstica (53% das mulheres).",
            {"violencia": 10, "saude": 7, "habitacao": 6},
            "FBSP 2024"),

        SegmentoPopulacao(
            "ribeirinhos_quilombolas", 4.0,
            "Ribeirinhos, quilombolas, extrativistas. Invisíveis.",
            {"agua": 9, "saude": 9, "educacao": 8, "ambiente": 8,
             "alimentacao": 7, "indigena": 5},
            "IBGE/Censo 2022"),

        SegmentoPopulacao(
            "juventude", 35.0,
            "18-29 anos. Desempregados, cultura, frustração.",
            {"emprego": 9, "educacao": 8, "violencia": 7, "cultura": 7,
             "drogas": 6, "transporte": 5},
            "IBGE 2022"),
    ]


# ============================================================
# SATISFAÇÃO DOS PARTIDOS (importada da simulação)
# ============================================================

SATISFACAO_PARTIDOS = {
    "UP":    {"media": 9.2, "cede": 0},
    "PCB":   {"media": 8.8, "cede": 0},
    "PSOL":  {"media": 9.3, "cede": 0},
    "PCdoB": {"media": 8.4, "cede": 0},
    "REDE":  {"media": 8.0, "cede": 1},
    "PSTU":  {"media": 7.9, "cede": 0},
    "PT":    {"media": 6.2, "cede": 6},
    "PDT":   {"media": 5.2, "cede": 8},
    "PCO":   {"media": 7.2, "cede": 0},
}


# ============================================================
# POLÍTICAS APROVADAS POR EIXO (da simulação multipla)
# ============================================================

POLITICAS_APROVADAS_POR_EIXO = {
    "violencia": 5, "saude": 6, "alimentacao": 4, "agua": 3,
    "soberania_alimentar": 3, "educacao": 5, "emprego": 4,
    "economia": 6, "ambiente": 4, "indigena": 3, "agropecuaria": 3,
    "energia": 3, "transporte": 3, "habitacao": 3, "saneamento": 2,
    "drogas": 2, "cultura": 3, "comunicacao": 3,
}

GAP_POR_EIXO = {
    "violencia": 95, "saude": 80, "alimentacao": 70, "agua": 60,
    "soberania_alimentar": 65, "educacao": 75, "emprego": 65,
    "economia": 50, "ambiente": 45, "indigena": 80, "agropecuaria": 35,
    "energia": 40, "transporte": 55, "habitacao": 50, "saneamento": 65,
    "drogas": 70, "cultura": 60, "comunicacao": 55,
}


# ============================================================
# CRUZAMENTO
# ============================================================

@dataclass
class ResultadoCruzado:
    """Resultado do cruzamento partido x população."""
    segmento: str
    tamanho_milhoes: float
    eixo: str
    necessidade: int              # 0-10 (quanto precisa)
    gap_pct: float                # % da necessidade não coberta
    politicas_aprovadas: int      # quantas políticas para esse eixo
    cobertura_estimada: float     # % da necessidade que a coalizão cobre
    necessidades_atendidas: float # em milhões de pessoas
    necessidades_insatisfeitas: float  # em milhões
    veredito: str                 # RESOLVIDO / PARCIAL / FALHA


def calcular_cobertura(necessidade: int, gap_pct: float, politicas: int) -> Tuple[float, str]:
    """Estima quanto da necessidade a coalizão cobre."""
    # Base: gap% é o que falta. Cada política aprovada reduz o gap.
    # Máximo de cobertura = 90% (nunca 100% na vida real)
    reducao_gap = min(0.90, politicas * 0.15)  # 15% por política aprovada, max 90%
    cobertura = max(0, 100 - gap_pct + (gap_pct * reducao_gap))

    if cobertura >= 80:
        veredito = "RESOLVIDO"
    elif cobertura >= 50:
        veredito = "PARCIAL"
    else:
        veredito = "FALHA"

    return min(90, cobertura), veredito


def cruzar() -> List[ResultadoCruzado]:
    """Cruza necessidades da população com políticas aprovadas."""
    segmentos = _init_segmentos()
    resultados = []

    for seg in segmentos:
        for eixo, necessidade in seg.necessidades.items():
            if necessidade == 0:
                continue

            gap = GAP_POR_EIXO.get(eixo, 50)
            pols = POLITICAS_APROVADAS_POR_EIXO.get(eixo, 0)
            cobertura, veredito = calcular_cobertura(necessidade, gap, pols)

            atendidas = seg.tamanho_milhoes * (cobertura / 100)
            insatisfeitas = seg.tamanho_milhoes - atendidas

            resultados.append(ResultadoCruzado(
                segmento=seg.nome, tamanho_milhoes=seg.tamanho_milhoes,
                eixo=eixo, necessidade=necessidade, gap_pct=gap,
                politicas_aprovadas=pols, cobertura_estimada=round(cobertura, 1),
                necessidades_atendidas=round(atendidas, 1),
                necessidades_insatisfeitas=round(insatisfeitas, 1),
                veredito=veredito,
            ))

    return resultados


def satisfacao_populacao_por_partido(resultados: List[ResultadoCruzado]) -> Dict[str, Dict[str, Any]]:
    """
    Para cada partido, estima a satisfação da população QUE ELE REPRESENTA.
    Partido satisfeito + população atendida = sinergia.
    Partido satisfeito + população insatisfeita = descolamento.
    """
    partidos_e_base = {
        "UP": ("famintos", "periferia", "nordeste_rural"),
        "PCB": ("juventude", "periferia", "trabalhador_formal"),
        "PSOL": ("indigenas", "mulheres_violencia", "periferia"),
        "PCdoB": ("idosos", "trabalhador_formal", "periferia"),
        "REDE": ("nordeste_rural", "ribeirinhos_quilombolas", "indigenas"),
        "PSTU": ("trabalhador_formal", "juventude"),
        "PT": ("famintos", "idosos", "nordeste_rural", "trabalhador_formal"),
        "PDT": ("nordeste_rural", "trabalhador_formal"),
        "PCO": ("juventude", "trabalhador_formal"),
    }

    resultado = {}
    for partido, sat_info in SATISFACAO_PARTIDOS.items():
        base_segmentos = partidos_e_base.get(partido, ())
        base_total = 0
        base_atendida = 0
        base_insatisfeita = 0

        for seg_nome in base_segmentos:
            seg_resultados = [r for r in resultados if r.segmento == seg_nome]
            for r in seg_resultados:
                # Ponderar por necessidade (necessidade 10 = mais urgente)
                peso = r.necessidade / 10
                base_total += r.tamanho_milhoes * peso
                base_atendida += r.necessidades_atendidas * peso
                base_insatisfeita += r.necessidades_insatisfeitas * peso

        pct_atendida = (base_atendida / base_total * 100) if base_total > 0 else 0

        # Sinergia: partido satisfeito + população atendida = alto
        sinergia = (sat_info["media"] / 10) * (pct_atendida / 100) * 10
        # Descolamento: partido satisfeito + população insatisfeita
        descolamento = (sat_info["media"] / 10) * (1 - pct_atendida / 100) * 10

        resultado[partido] = {
            "sat_partido": sat_info["media"],
            "sat_populacao": round(pct_atendida, 1),
            "sinergia": round(sinergia, 1),
            "descolamento": round(descolamento, 1),
            "base_total_milhoes": round(base_total, 1),
            "base_atendida_milhoes": round(base_atendida, 1),
            "base_insatisfeita_milhoes": round(base_insatisfeita, 1),
            "cede": sat_info["cede"],
        }

    return dict(sorted(resultado.items(), key=lambda x: x[1]["sinergia"], reverse=True))


def _demo():
    resultados = cruzar()
    sat_cruzada = satisfacao_populacao_por_partido(resultados)

    print("=" * 95)
    print("CRUZAMENTO: SATISFAÇÃO DO PARTIDO x SATISFAÇÃO DA POPULAÇÃO")
    print("=" * 95)

    print(f"\n10 segmentos da população x 18 eixos do Raio X")

    print(f"\n{'='*95}")
    print("NECESSIDADES DA POPULAÇÃO: O QUE FALTA")
    print(f"{'='*95}")

    # Agrupar por segmento
    por_segmento = defaultdict(list)
    for r in resultados:
        por_segmento[r.segmento].append(r)

    for seg_nome, seg_rs in por_segmento.items():
        total_atendido = sum(r.necessidades_atendidas for r in seg_rs)
        total_insatisfeito = sum(r.necessidades_insatisfeitas for r in seg_rs)
        pct = total_atendido / (total_atendido + total_insatisfeito) * 100 if (total_atendido + total_insatisfeito) > 0 else 0
        print(f"\n  [{seg_nome.upper()}] ({seg_rs[0].tamanho_milhoes}M pessoas)")
        for r in seg_rs:
            flag = " *** RESOLVIDO" if r.veredito == "RESOLVIDO" else (" *** FALHA" if r.veredito == "FALHA" else "")
            print(f"    {r.eixo:<25} necessidade={r.necessidade} cobertura={r.cobertura_estimada}% [{r.veredito}]{flag}")
        print(f"    TOTAL: {total_atendido:.1f}M atendidos / {total_insatisfeito:.1f}M insatisfeitos ({pct:.0f}% cobertura)")

    print(f"\n{'='*95}")
    print("CRUZAMENTO: PARTIDO x POPULAÇÃO")
    print(f"{'='*95}")
    print(f"\n{'PARTIDO':<10} {'SAT_PART':>8} {'SAT_POP':>8} {'SINERGIA':>9} {'DESCOLADO':>10} {'CEDE':>5}")
    print("-" * 55)

    for partido, s in sat_cruzada.items():
        flag = ""
        if s["descolamento"] > 5:
            flag = " *** DESCOLADO"
        elif s["sinergia"] >= 6:
            flag = " *** SINERGIA"
        print(f"  {partido:<8} {s['sat_partido']:>7.1f} {s['sat_populacao']:>7.1f}% {s['sinergia']:>8.1f} {s['descolamento']:>9.1f} {s['cede']:>5}{flag}")

    print(f"\n{'='*95}")
    print("VEREDITO: QUEM SERVE AO POVO E QUEM SERVE A SI MESMO")
    print(f"{'='*95}")

    print(f"""
  SINERGIA = partido satisfeito + população atendida = serve ao povo
  DESCOLAMENTO = partido satisfeito + população insatisfeita = serve a si mesmo

  MAIOR SINERGIA (partido + povo alinhados):
""")
    for p, s in list(sat_cruzada.items())[:3]:
        print(f"    {p:<8} sinergia={s['sinergia']:.1f} | {s['base_atendida_milhoes']:.0f}M atendidos")

    print(f"""
  MAIOR DESCOLAMENTO (partido feliz, povo sofrendo):
""")
    for p, s in sorted(sat_cruzada.items(), key=lambda x: x[1]["descolamento"], reverse=True)[:3]:
        print(f"    {p:<8} descolamento={s['descolamento']:.1f} | {s['base_insatisfeita_milhoes']:.0f}M insatisfeitos")

    # Risco
    print(f"""
  RISCO POLÍTICO:
""")
    for p, s in sat_cruzada.items():
        if s["descolamento"] > s["sinergia"]:
            print(f"    *** {p}: descolamento ({s['descolamento']:.1f}) > sinergia ({s['sinergia']:.1f})")
            print(f"        Partido satisfeito mas população da sua base NÃO.")
            print(f"        {s['base_insatisfeita_milhoes']:.0f}M de pessoas insatisfeitas.")
    risco = [p for p, s in sat_cruzada.items() if s["descolamento"] > s["sinergia"]]
    if not risco:
        print(f"    Nenhum partido com descolamento > sinergia. População majoritariamente atendida.")

    # Total
    total_pop = sum(r.tamanho_milhoes for r in [s for s in _init_segmentos()])
    total_atendido = sum(s["base_atendida_milhoes"] for s in sat_cruzada.values())
    total_insatisfeito = sum(s["base_insatisfeita_milhoes"] for s in sat_cruzada.values())
    print(f"""
  TOTAL NACIONAL:
    {total_atendido:.0f}M necessidades atendidas pela coalizão
    {total_insatisfeito:.0f}M necessidades insatisfeitas
    {total_atendido/(total_atendido+total_insatisfeito)*100:.0f}% de cobertura populacional
""")


if __name__ == "__main__":
    _demo()
