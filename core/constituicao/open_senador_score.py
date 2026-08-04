#!/usr/bin/env python3
"""
OpenSenadorScore -- 81 Senadores Avaliados pelo Sistema
=========================================================
Score de capacidade + alinhamento Raio X para cada senador em exercicio.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

# Scores conhecidos (da base anterior)
SCORES_CONHECIDOS = {
    "Camilo Santana": {"c1": 0.89, "c2": 1.0, "c3": 1.0, "feito": "Governador CE 2x. IDEB subiu. Vacinacao 95%. Min Educacao.", "alinhamentos": {"educacao": 0.9, "saude": 0.7, "violencia": 0.4, "agua": 0.3}},
    "Sergio Moro": {"c1": 0.63, "c2": 0.4, "c3": 0.6, "feito": "Lava Jato. Lei Anticrime. Prefeito Maringa.", "alinhamentos": {"violencia": 0.5, "drogas": 0.2}},
    "Damares Alves": {"c1": 0.44, "c2": 0.2, "c3": 0.4, "feito": "Ministra Mulheres/DH. Pastora.", "alinhamentos": {"violencia": 0.1}},
    "Tereza Cristina": {"c1": 0.62, "c2": 0.8, "c3": 0.6, "feito": "Ministra Agricultura. Deputada. Agro.", "alinhamentos": {"agropecuaria": 0.6, "alimentacao": 0.3}},
    "Rodrigo Pacheco": {"c1": 0.58, "c2": 0.6, "c3": 0.6, "feito": "Presidente do Senado. Advogado.", "alinhamentos": {}},
    "Randolfe Rodrigues": {"c1": 0.55, "c2": 0.4, "c3": 0.7, "feito": "Senador AP. Lider PT. Ambientalista.", "alinhamentos": {"ambiente": 0.6, "indigena": 0.5}},
    "Hamilton Mourão": {"c1": 0.58, "c2": 0.6, "c3": 0.5, "feito": "General. Vice-presidente (2019-2022).", "alinhamentos": {"violencia": 0.2, "transporte": 0.2}},
    "Omar Aziz": {"c1": 0.65, "c2": 0.8, "c3": 0.6, "feito": "Governador Amazonas 2x. Ex-prefeito Manaus.", "alinhamentos": {"saude": 0.4, "ambiente": 0.3, "indigena": 0.3}},
    "Jader Barbalho": {"c1": 0.70, "c2": 1.0, "c3": 0.5, "feito": "Governador PA. Presidente Camara. Senador 4x.", "alinhamentos": {"habitacao": 0.3, "saude": 0.2}},
    "Renan Calheiros": {"c1": 0.68, "c2": 1.0, "c3": 0.4, "feito": "Presidente Senado 3x. Senador AL 6x.", "alinhamentos": {}},
    "Eduardo Braga": {"c1": 0.62, "c2": 0.8, "c3": 0.6, "feito": "Governador Amazonas 2x. Ministro.", "alinhamentos": {"energia": 0.3, "saude": 0.2}},
    "Ciro Nogueira": {"c1": 0.60, "c2": 0.8, "c3": 0.4, "feito": "Ministro Casa Civil (Bolsonaro). Senador.", "alinhamentos": {}},
    "Marcelo Castro": {"c1": 0.58, "c2": 0.8, "c3": 0.5, "feito": "Ministro Saude. Deputado, Senador.", "alinhamentos": {"saude": 0.5}},
    "Flávio Arns": {"c1": 0.55, "c2": 0.6, "c3": 0.7, "feito": "Senador PR. Educador. Ex-prefeito Curitiba.", "alinhamentos": {"educacao": 0.6, "cultura": 0.4}},
    "Alessandro Vieira": {"c1": 0.50, "c2": 0.4, "c3": 0.8, "feito": "Senador SE. Tecnico. TCU auditor.", "alinhamentos": {"inflacao": 0.3}},
    "Cid Gomes": {"c1": 0.62, "c2": 0.8, "c3": 0.4, "feito": "Governador CE. Prefeito Fortaleza. Senador.", "alinhamentos": {"educacao": 0.4, "saude": 0.3}},
    "Jaques Wagner": {"c1": 0.68, "c2": 1.0, "c3": 0.6, "feito": "Governador BA. Ministro Casa Civil. Senador.", "alinhamentos": {"saude": 0.3, "educacao": 0.3}},
    "Humberto Costa": {"c1": 0.62, "c2": 0.8, "c3": 0.6, "feito": "Ministro Saude. Prefeito Recife. Senador.", "alinhamentos": {"saude": 0.5}},
    "Paulo Paim": {"c1": 0.60, "c2": 0.6, "c3": 0.8, "feito": "Senador RS 5x. Sindicalista. Coerencia 30 anos.", "alinhamentos": {"emprego": 0.4, "violencia": 0.2}},
    "Otto Alencar": {"c1": 0.65, "c2": 0.8, "c3": 0.6, "feito": "Senador BA. Medico. Prefeito Feira de Santana.", "alinhamentos": {"saude": 0.6}},
    "Mara Gabrilli": {"c1": 0.55, "c2": 0.6, "c3": 0.7, "feito": "Senadora SP. Deputada. Psicologa. Deficiencia.", "alinhamentos": {"saude": 0.4, "educacao": 0.3}},
    "Esperidião Amin": {"c1": 0.62, "c2": 0.8, "c3": 0.6, "feito": "Governador SC 2x. Prefeito Floripa. Senador 3x.", "alinhamentos": {"educacao": 0.4, "transporte": 0.3}},
    "Davi Alcolumbre": {"c1": 0.58, "c2": 0.6, "c3": 0.5, "feito": "Presidente Senado (2019-2021). Senador AP.", "alinhamentos": {}},
    "Carlos Fávaro": {"c1": 0.58, "c2": 0.6, "c3": 0.6, "feito": "Senador MT. Vice-governador MT. Produtor rural.", "alinhamentos": {"agropecuaria": 0.5, "energia": 0.3}},
    "Eliziane Gama": {"c1": 0.50, "c2": 0.4, "c3": 0.7, "feito": "Senadora MA. Deputada. Jornalista.", "alinhamentos": {"educacao": 0.3, "violencia": 0.2}},
    "Romário": {"c1": 0.40, "c2": 0.2, "c3": 0.6, "feito": "Senador RJ. Ex-jogador. Deputado. PCD.", "alinhamentos": {"cultura": 0.2, "violencia": 0.1}},
    "Astronauta Marcos Pontes": {"c1": 0.50, "c2": 0.4, "c3": 0.6, "feito": "Ministro Ciencia (Bolsonaro). Astronauta.", "alinhamentos": {"energia": 0.2, "educacao": 0.2}},
    "Soraya Thronicke": {"c1": 0.40, "c2": 0.2, "c3": 0.5, "feito": "Senadora MS. Candidata presidente 2022.", "alinhamentos": {}},
    "Jorge Kajuru": {"c1": 0.40, "c2": 0.2, "c3": 0.5, "feito": "Senador GO. Jornalista. Comunicador.", "alinhamentos": {"comunicacao": 0.3}},
    "Eduardo Girão": {"c1": 0.40, "c2": 0.2, "c3": 0.5, "feito": "Senador CE. Empresario. Comunicacao.", "alinhamentos": {"cultura": 0.2}},
}

def score_total(c1: float, c2: float, c3: float) -> float:
    return (c1 * 3 + c2 * 2 + c3 * 1) / 6 * 5

def score_senador(nome: str, partido: str, uf: str) -> Dict[str, Any]:
    # Score conhecido (detalhado)
    if nome in SCORES_CONHECIDOS:
        d = SCORES_CONHECIDOS[nome]
        s = score_total(d["c1"], d["c2"], d["c3"])
        return {
            "nome": nome, "partido": partido, "uf": uf,
            "score": round(s, 2),
            "c1": d["c1"], "c2": d["c2"], "c3": d["c3"],
            "feito": d["feito"],
            "alinhamentos": d["alinhamentos"],
            "veredito": "APROVADO" if s >= 4.0 else "WO",
            "fonte": "detalhado",
        }

    # Score heuristico para os demais
    # Base: sem obra publica conhecida = score baixo
    # Multiplos mandatos = liderou
    # Ex-governador/ministro = gestao+orcamento

    # Heuristica: nomes com alto perfil politico tendem a ter mais experiencia
    alto_perfil = ["Confúcio Moura", "Veneziano Vital do Rêgo", "Renan Filho",
                   "Weverton", "Flávio Bolsonaro", "Zenaide Maia",
                   "Nelsinho Trad", "Angelo Coronel", "Beto Faro",
                   "Teresa Leitão", "Rogério Carvalho", "Fabiano Contarato",
                   "Izalci Lucas", "Magno Malta", "Marcos Rogério",
                   "Wellington Fagundes", "Rogerio Marinho", "Eduardo Gomes"]

    medio_perfil = ["Marcos do Val", "Ivete da Silveira", "Leila Barros",
                    "Carlos Portinho", "Efraim Filho", "Hermes Klann",
                    "Jaime Bagattoli", "Marcio Bittar", "Giordano",
                    "Styvenson Valentim", "Zequinha Marinho", "Daniella Ribeiro",
                    "Dr. Hiran", "Laércio Oliveira", "Luis Carlos Heinze",
                    "Ana Paula Lobato", "Chico Rodrigues", "Dra. Eudócia",
                    "Oriovisto Guimarães", "Plínio Valério", "Carlos Viana",
                    "Fernando Dueire", "Irajá", "Jussara Lima", "Lucas Barreto",
                    "Sérgio Petecão", "Vanderlan Cardoso", "Alan Rick",
                    "Cleitinho", "Roberta Acioly", "Jayme Campos",
                    "Professora Dorinha Seabra"]

    if nome in alto_perfil:
        c1, c2, c3 = 0.50, 0.60, 0.50
    elif nome in medio_perfil:
        c1, c2, c3 = 0.35, 0.40, 0.45
    else:
        c1, c2, c3 = 0.25, 0.20, 0.40

    s = score_total(c1, c2, c3)
    return {
        "nome": nome, "partido": partido, "uf": uf,
        "score": round(s, 2),
        "c1": c1, "c2": c2, "c3": c3,
        "feito": "Sem obra publica majoritaria conhecida na base",
        "alinhamentos": {},
        "veredito": "APROVADO" if s >= 4.0 else "WO",
        "fonte": "heuristico",
    }


def _demo():
    with open("/tmp/senadores.json") as f:
        senadores = json.load(f)

    print("=" * 80)
    print("81 SENADORES EM EXERCICIO -- SCORE DE CAPACIDADE")
    print("=" * 80)

    resultados = []
    for s in senadores:
        r = score_senador(s["nome"], s["partido"], s["uf"])
        resultados.append(r)

    # Ordenar por score
    resultados.sort(key=lambda x: x["score"], reverse=True)

    aprovados = [r for r in resultados if r["veredito"] == "APROVADO"]
    wo = [r for r in resultados if r["veredito"] == "WO"]

    print(f"\nTotal: {len(resultados)} senadores")
    print(f"APROVADOS (>=4.0): {len(aprovados)}")
    print(f"WO (<4.0): {len(wo)}")

    print(f"\n{'='*80}")
    print("RANKING COMPLETO")
    print(f"{'='*80}")
    for i, r in enumerate(resultados):
        fonte = "[D]" if r["fonte"] == "detalhado" else "[H]"
        alinh_max = max(r["alinhamentos"].values()) if r["alinhamentos"] else 0
        dom_melhor = max(r["alinhamentos"], key=r["alinhamentos"].get) if r["alinhamentos"] else "sem alinhamento"
        print(f"  {i+1:>3}. {r['score']:.2f} [{r['veredito']:<3}] {fonte} {r['nome']:<30} {r['partido']:<12} {r['uf']}")
        if r["fonte"] == "detalhado":
            print(f"       FEZ: {r['feito'][:70]}")
            if r["alinhamentos"]:
                print(f"       ALINH: {dom_melhor}={alinh_max:.1f} -> score_alinhado={r['score']*alinh_max:.2f}")

    print(f"\n{'='*80}")
    print("SCORE MEDIO POR PARTIDO")
    print(f"{'='*80}")
    from collections import defaultdict
    por_partido = defaultdict(list)
    for r in resultados:
        por_partido[r["partido"]].append(r["score"])

    for partido in sorted(por_partido.keys(), key=lambda p: sum(por_partido[p])/len(por_partido[p]), reverse=True):
        scores = por_partido[partido]
        media = sum(scores) / len(scores)
        maximo = max(scores)
        melhor = next(r["nome"] for r in resultados if r["partido"] == partido and r["score"] == maximo)
        print(f"  {partido:<15} media={media:.2f}  max={maximo:.2f} ({melhor})  n={len(scores)}")


if __name__ == "__main__":
    _demo()
