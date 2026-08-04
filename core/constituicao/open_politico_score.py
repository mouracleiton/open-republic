#!/usr/bin/env python3
"""
OpenPoliticoScore -- 593 Politicos Federais Brasileiros Avaliados
===================================================================
81 senadores + 512 deputados = 593 politicos em exercicio.
Score de capacidade + alinhamento Raio X. Corte 4.0.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple
from collections import defaultdict

def score_total(c1: float, c2: float, c3: float) -> float:
    return (c1 * 3 + c2 * 2 + c3 * 1) / 6 * 5


# ============================================================
# SCORES DETALHADOS (politicos de alto perfil conhecidos)
# ============================================================

SCORES_DETALHADOS = {
    # Senadores (herdados do modulo anterior)
    "Camilo Santana": (0.89, 1.0, 1.0, "Governador CE 2x. IDEB subiu. Vacinacao 95%.", {"educacao": 0.9, "saude": 0.7, "violencia": 0.4}),
    "Sergio Moro": (0.63, 0.4, 0.6, "Lava Jato. Lei Anticrime. Prefeito Maringa.", {"violencia": 0.5, "drogas": 0.2}),
    "Marina Silva": (0.844, 0.80, 0.80, "Reduziu desmatamento 80%. Cisternas. PAA.", {"ambiente": 1.0, "agua": 0.9, "alimentacao": 0.9, "agropecuaria": 0.8, "seguranca_alimentar": 0.9}),
    "Rodrigo Pacheco": (0.58, 0.6, 0.6, "Presidente do Senado. Advogado.", {}),
    "Randolfe Rodrigues": (0.55, 0.4, 0.7, "Senador AP. Ambientalista.", {"ambiente": 0.6, "indigena": 0.5}),
    "Hamilton Mourão": (0.58, 0.6, 0.5, "General. Vice-presidente.", {"violencia": 0.2, "transporte": 0.2}),
    "Omar Aziz": (0.65, 0.8, 0.6, "Governador Amazonas 2x.", {"saude": 0.4, "ambiente": 0.3, "indigena": 0.3}),
    "Jader Barbalho": (0.70, 1.0, 0.5, "Governador PA. Presidente Camara. Senador 4x.", {"habitacao": 0.3, "saude": 0.2}),
    "Renan Calheiros": (0.68, 1.0, 0.4, "Presidente Senado 3x. Senador 6x.", {}),
    "Eduardo Braga": (0.62, 0.8, 0.6, "Governador Amazonas 2x. Ministro.", {"energia": 0.3, "saude": 0.2}),
    "Ciro Nogueira": (0.60, 0.8, 0.4, "Ministro Casa Civil. Senador.", {}),
    "Marcelo Castro": (0.58, 0.8, 0.5, "Ministro Saude. Senador.", {"saude": 0.5}),
    "Flávio Arns": (0.55, 0.6, 0.7, "Senador PR. Educador. Ex-prefeito Curitiba.", {"educacao": 0.6, "cultura": 0.4}),
    "Alessandro Vieira": (0.50, 0.4, 0.8, "Senador SE. Auditor TCU.", {"inflacao": 0.3}),
    "Cid Gomes": (0.62, 0.8, 0.4, "Governador CE. Prefeito Fortaleza.", {"educacao": 0.4, "saude": 0.3}),
    "Jaques Wagner": (0.68, 1.0, 0.6, "Governador BA. Ministro Casa Civil.", {"saude": 0.3, "educacao": 0.3}),
    "Humberto Costa": (0.62, 0.8, 0.6, "Ministro Saude. Prefeito Recife.", {"saude": 0.5}),
    "Paulo Paim": (0.60, 0.6, 0.8, "Senador RS 5x. Sindicalista.", {"emprego": 0.4, "violencia": 0.2}),
    "Otto Alencar": (0.65, 0.8, 0.6, "Senador BA. Medico.", {"saude": 0.6}),
    "Mara Gabrilli": (0.55, 0.6, 0.7, "Senadora SP. Psicologa.", {"saude": 0.4, "educacao": 0.3}),
    "Esperidião Amin": (0.62, 0.8, 0.6, "Governador SC 2x. Prefeito Floripa.", {"educacao": 0.4, "transporte": 0.3}),
    "Davi Alcolumbre": (0.58, 0.6, 0.5, "Presidente Senado (2019-2021).", {}),
    "Tereza Cristina": (0.62, 0.8, 0.6, "Ministra Agricultura.", {"agropecuaria": 0.6, "alimentacao": 0.3}),
    "Damares Alves": (0.44, 0.2, 0.4, "Ministra Mulheres/DH.", {"violencia": 0.1}),
    "Romário": (0.40, 0.2, 0.6, "Senador. Ex-jogador.", {"cultura": 0.2, "violencia": 0.1}),
    "Soraya Thronicke": (0.40, 0.2, 0.5, "Candidata presidente 2022.", {}),
    "Jorge Kajuru": (0.40, 0.2, 0.5, "Jornalista. Comunicador.", {"comunicacao": 0.3}),

    # Deputados de alto perfil
    "Arthur Lira": (0.62, 0.8, 0.5, "Presidente Camara. Deputado AL.", {}),
    "Gleisi Hoffmann": (0.58, 0.8, 0.7, "Presidente PT. Senadora. Deputada.", {"saude": 0.2, "emprego": 0.3}),
    "Aécio Neves": (0.62, 0.8, 0.4, "Governador MG. Presidente Camara. Senador.", {"saude": 0.3, "educacao": 0.3}),
    "Beto Richa": (0.60, 0.8, 0.4, "Governador PR 2x. Prefeito Curitiba.", {"transporte": 0.3, "habitacao": 0.2}),
    "Eunício Oliveira": (0.60, 0.8, 0.4, "Governador CE. Presidente Senado.", {}),
    "Celso Russomanno": (0.55, 0.6, 0.4, "Prefeito SP (licenca). Deputado.", {"habitacao": 0.4, "transporte": 0.3}),
    "Juscelino Filho": (0.55, 0.6, 0.4, "Ministro Comunicacoes. Deputado.", {"comunicacao": 0.3}),
    "Ricardo Barros": (0.58, 0.8, 0.4, "Ministro Saude (Bolsonaro). Deputado.", {"saude": 0.4}),
    "Mendonça Filho": (0.60, 0.8, 0.5, "Ministro Educacao. Deputado.", {"educacao": 0.5}),
    "Silvio Costa Filho": (0.55, 0.6, 0.4, "Ministro Portos/Aeroportos. Deputado.", {"transporte": 0.3}),
    "Marcelo Álvaro Antônio": (0.50, 0.6, 0.4, "Ministro Turismo. Deputado.", {}),
    "Osmar Terra": (0.58, 0.6, 0.5, "Ministro Desenvolvimento Social. Deputado.", {"alimentacao": 0.3, "saude": 0.2}),
    "Jandira Feghali": (0.55, 0.6, 0.7, "Deputada RJ. Medica. Coerencia.", {"saude": 0.5}),
    "Benedita da Silva": (0.55, 0.6, 0.8, "Governadora RJ. Ministra. Deputada.", {"habitacao": 0.3, "saude": 0.2}),
    "Orlando Silva": (0.50, 0.4, 0.7, "Ministro Esporte. Deputado.", {"cultura": 0.3, "educacao": 0.2}),
    "Patrus Ananias": (0.55, 0.8, 0.7, "Ministro Cidades. Deputado.", {"habitacao": 0.4, "saneamento": 0.3}),
    "Erika Hilton": (0.40, 0.0, 0.5, "Vereadora SP. Deputada.", {"violencia": 0.3}),
    "Sônia Guajajara": (0.50, 0.2, 0.7, "Ministra Povos Originarios.", {"indigena": 1.0, "ambiente": 0.8}),
    "Tabata Amaral": (0.45, 0.2, 0.6, "Deputada. Educacao. Cientista.", {"educacao": 0.5}),
    "Kim Kataguiri": (0.35, 0.0, 0.5, "Vereador SP. Deputado.", {}),
    "Nikolas Ferreira": (0.36, 0.0, 0.4, "Deputado. Advogado. Youtuber.", {}),
    "André Janones": (0.40, 0.0, 0.5, "Deputado. Engenheiro. Internet.", {}),
    "General Pazuello": (0.45, 0.6, 0.4, "General. Ministro Saude (Bolsonaro).", {"saude": 0.2}),
    "Ricardo Salles": (0.45, 0.6, 0.4, "Ministro Meio Ambiente (Bolsonaro).", {"ambiente": 0.3}),
    "Marcelo Crivella": (0.50, 0.6, 0.4, "Prefeito RJ. Bispo. Senador.", {"saude": 0.2, "cultura": 0.1}),
    "Baleia Rossi": (0.50, 0.4, 0.5, "Deputado. Lider MDB. Economista.", {"inflacao": 0.3}),
    "Carlos Zarattini": (0.50, 0.4, 0.6, "Deputado. Lider PT.", {"habitacao": 0.3}),
    "Luiza Erundina": (0.55, 0.6, 0.8, "Prefeita SP. Deputada. Coerencia.", {"educacao": 0.4, "saude": 0.3, "habitacao": 0.3}),
    "Chico Alencar": (0.45, 0.2, 0.8, "Deputado. Professor. Coerencia 30 anos.", {"educacao": 0.4}),
    "Fernando Coelho Filho": (0.55, 0.6, 0.4, "Ministro Minas/Energia. Deputado.", {"energia": 0.4}),
    "Roseana Sarney": (0.55, 0.8, 0.3, "Governadora MA 3x. Deputada.", {}),
    "Newton Cardoso Jr": (0.50, 0.6, 0.4, "Deputado. Medico.", {"saude": 0.3}),
    "Célia Xakriabá": (0.35, 0.0, 0.6, "Deputada. Indigena. Educadora.", {"indigena": 0.8, "educacao": 0.3, "ambiente": 0.5}),
}

# ============================================================
# HEURISTICA POR CARGO/PERFIL (para os demais)
# ============================================================

# Ex-governadores, ex-ministros, prefeitos de capitais
ALTO_PERFIL = {
    "Confúcio Moura", "Veneziano Vital do Rêgo", "Renan Filho", "Weverton",
    "Flávio Bolsonaro", "Zenaide Maia", "Nelsinho Trad", "Angelo Coronel",
    "Beto Faro", "Teresa Leitão", "Rogério Carvalho", "Fabiano Contarato",
    "Izalci Lucas", "Magno Malta", "Marcos Rogério", "Wellington Fagundes",
    "Rogerio Marinho", "Eduardo Gomes", "Elcione Barbalho", "Robinson Faria",
    "Marx Beltrão", "Luciano Bivar", "Antonio Brito", "Rodrigo Rollemberg",
    "Lídice da Mata", "Lindbergh Farias", "Rui Falcão", "Paulo Pimenta",
    "Rubens Otoni", "José Priante", "Eriberto Medeiros",
}

MEDIO_PERFIL = {
    "Marcos do Val", "Ivete da Silveira", "Leila Barros", "Carlos Portinho",
    "Efraim Filho", "Hermes Klann", "Jaime Bagattoli", "Marcio Bittar",
    "Giordano", "Styvenson Valentim", "Zequinha Marinho", "Daniella Ribeiro",
    "Dr. Hiran", "Laércio Oliveira", "Luis Carlos Heinze", "Ana Paula Lobato",
    "Chico Rodrigues", "Dra. Eudócia", "Oriovisto Guimarães", "Plínio Valério",
    "Carlos Viana", "Fernando Dueire", "Irajá", "Jussara Lima", "Lucas Barreto",
    "Sérgio Petecão", "Vanderlan Cardoso", "Alan Rick", "Cleitinho",
    "Roberta Acioly", "Jayme Campos", "Professora Dorinha Seabra",
    "Carlos Sampaio", "Carlos Jordy", "Bia Kicis", "Caroline de Toni",
    "Chris Tonietto", "Daniel Freitas", "Gustavo Gayer", "Junio Amaral",
    "Luiz Philippe de Orleans e Bragança", "Bibo Nunes", "Eros Biondini",
    "Filipe Barros", "General Girão", "Sargento Gonçalves", "Sargento Fahur",
    "Captain Augusto", "Capitão Alberto Neto", "Capitão Alden", "Coronel Assis",
    "Coronel Chrisóstomo", "Coronel Fernanda", "Coronel Meira", "Detinha",
    "Rosângela Reis", "Pastor Gil", "Pr. Marco Feliciano", "Mario Frias",
    "Jefferson Campos", "Vinicius Carvalho", "Vinicius Gurgel", "Zé Trovão",
    "Sóstenes Cavalcante", "Fred Costa", "Marreca Filho", "Tiririca",
    "Cabralzinho", "Bebeto", "Dani Cunha", "Mauricio do Vôlei", "Yury do Paredão",
    "Pastor Sargento Isidório", "Duda Salabert", "Erika Kokay", "Sâmia Bomfim",
    "Talíria Petrone", "Tarcísio Motta", "Fernanda Melchionna", "Glauber Braga",
    "Natália Bonavides", "Pastor Henrique Vieira", "Professora Luciene Cavalcante",
}


def score_politico(nome: str, partido: str, uf: str, cargo: str = "") -> Dict[str, Any]:
    if nome in SCORES_DETALHADOS:
        c1, c2, c3, feito, alinhamentos = SCORES_DETALHADOS[nome]
        s = score_total(c1, c2, c3)
        return {
            "nome": nome, "partido": partido, "uf": uf, "cargo": cargo,
            "score": round(s, 2), "c1": c1, "c2": c2, "c3": c3,
            "feito": feito, "alinhamentos": alinhamentos,
            "veredito": "APROVADO" if s >= 4.0 else "WO",
            "fonte": "detalhado",
        }

    if nome in ALTO_PERFIL:
        c1, c2, c3 = 0.50, 0.60, 0.50
    elif nome in MEDIO_PERFIL:
        c1, c2, c3 = 0.35, 0.20, 0.45
    else:
        c1, c2, c3 = 0.20, 0.10, 0.35

    s = score_total(c1, c2, c3)
    return {
        "nome": nome, "partido": partido, "uf": uf, "cargo": cargo,
        "score": round(s, 2), "c1": c1, "c2": c2, "c3": c3,
        "feito": "Sem obra publica majoritaria conhecida",
        "alinhamentos": {},
        "veredito": "APROVADO" if s >= 4.0 else "WO",
        "fonte": "heuristico",
    }


def _demo():
    with open("/tmp/todos_politicos.json") as f:
        todos = json.load(f)

    print("=" * 80)
    print("593 POLITICOS FEDERAIS EM EXERCICIO -- SCORE DE CAPACIDADE")
    print("81 senadores + 512 deputados")
    print("=" * 80)

    # Score todos
    resultados = []
    for i, p in enumerate(todos):
        cargo = "senador" if i < 81 else "deputado"
        r = score_politico(p["nome"], p["partido"], p["uf"], cargo)
        resultados.append(r)

    resultados.sort(key=lambda x: x["score"], reverse=True)

    aprovados = [r for r in resultados if r["veredito"] == "APROVADO"]
    wo = [r for r in resultados if r["veredito"] == "WO"]

    print(f"\nTotal: {len(resultados)} politicos")
    print(f"APROVADOS (>=4.0): {len(aprovados)}")
    print(f"WO (<4.0): {len(wo)}")
    print(f"Taxa de aprovacao: {len(aprovados)/len(resultados)*100:.1f}%")

    # Top 30
    print(f"\n{'='*80}")
    print("TOP 30 POLITICOS POR SCORE")
    print(f"{'='*80}")
    for i, r in enumerate(resultados[:30]):
        f = "[D]" if r["fonte"] == "detalhado" else "[H]"
        print(f"  {i+1:>3}. {r['score']:.2f} [{r['veredito']:<3}] {f} {r['nome']:<30} {r['partido']:<12} {r['uf']} ({r['cargo']})")
        if r["fonte"] == "detalhado" and r["feito"]:
            print(f"       FEZ: {r['feito'][:65]}")

    # Score por partido
    print(f"\n{'='*80}")
    print("SCORE MEDIO POR PARTIDO")
    print(f"{'='*80}")
    por_partido = defaultdict(list)
    for r in resultados:
        por_partido[r["partido"]].append(r["score"])

    for partido in sorted(por_partido.keys(), key=lambda p: sum(por_partido[p])/len(por_partido[p]), reverse=True):
        scores = por_partido[partido]
        media = sum(scores) / len(scores)
        maximo = max(scores)
        melhor_nome = next(r["nome"] for r in resultados if r["partido"] == partido and r["score"] == maximo)
        n_aprov = sum(1 for s in scores if s >= 4.0)
        print(f"  {partido:<15} media={media:.2f}  max={maximo:.2f} ({melhor_nome[:25]:<25})  aprov={n_aprov}/{len(scores)}")

    # Score por UF
    print(f"\n{'='*80}")
    print("SCORE MEDIO POR UF (top 15)")
    print(f"{'='*80}")
    por_uf = defaultdict(list)
    for r in resultados:
        por_uf[r["uf"]].append(r["score"])

    for uf in sorted(por_uf.keys(), key=lambda u: sum(por_uf[u])/len(por_uf[u]), reverse=True)[:15]:
        scores = por_uf[uf]
        media = sum(scores) / len(scores)
        print(f"  {uf:<5} media={media:.2f}  n={len(scores)}")

    print(f"\n{'='*80}")
    print("VEREDITO FINAL")
    print(f"{'='*80}")
    print(f"  {len(aprovados)} de {len(resultados)} politicos passam no corte >=4.0")
    print(f"  {len(wo)} de {len(resultados)} sao WO ({len(wo)/len(resultados)*100:.0f}%)")
    print(f"  Score medio nacional: {sum(r['score'] for r in resultados)/len(resultados):.2f}")
    if aprovados:
        print(f"\n  APROVADOS:")
        for r in aprovados:
            alinh_max = max(r["alinhamentos"].values()) if r["alinhamentos"] else 0
            dom = max(r["alinhamentos"], key=r["alinhamentos"].get) if r["alinhamentos"] else "sem"
            print(f"    {r['nome']} ({r['partido']}/{r['uf']}) score={r['score']:.2f} alinh:{dom}={alinh_max:.1f}")


if __name__ == "__main__":
    _demo()
