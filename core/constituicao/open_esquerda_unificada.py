#!/usr/bin/env python3
"""
OpenEsquerdaUnificada -- Frente de Esquerda por Ministerio
=============================================================
"Unir a esquerda. Colocar cada um onde rende."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


class PartidoEsquerda(Enum):
    PT = "PT"
    PSOL = "PSOL"
    PSB = "PSB"
    PCdoB = "PCdoB"
    PSTU = "PSTU"
    PCB = "PCB"
    PCO = "PCO"
    UP = "UP"
    REDE = "REDE"
    PDT = "PDT"
    PV = "PV"
    SOLIDARIEDADE = "SOLIDARIEDADE"


class FitMinisterio(Enum):
    PERFEITO = 5      # ja fez exatamente isso
    FORTE = 4         # fez algo muito proximo
    BOM = 3           # tem correlacao
    FRACO = 2         # contato com a area
    NENHUM = 1        # sem fit nenhum


@dataclass
class CandidatoEsquerda:
    """Candidato de esquerda avaliado por ministerio."""
    nome: str
    partido: str
    cargo: str                # "presidente", "senador", "deputado", "tecnico"
    uf: str
    score_capacidade: float   # 0-5 (mesma formula 3 camadas)

    # Fit por area ministerial (FitMinisterio 1-5)
    fits: Dict[str, FitMinisterio] = field(default_factory=dict)

    feito_real: str = ""
    origem: str = ""          # "movimento", "sindical", "tecnico", "politico"


def _init_candidatos() -> List[CandidatoEsquerda]:
    return [

        # ================================================================
        # CANDIDATOS PRESIDENCIAIS DA ESQUERDA
        # ================================================================

        CandidatoEsquerda(
            nome="Lula da Silva", partido="PT", cargo="presidente", uf="SP",
            score_capacidade=4.50,
            origem="movimento/sindical",
            feito_real="Presidente 3 mandatos. Fome Zero, Bolsa Familia, PAC, Minha Casa. PIB cresceu, 30M sairam da pobreza.",
            fits={
                "Casa_Civil": FitMinisterio.PERFEITO,
                "Desenvolvimento_Social": FitMinisterio.PERFEITO,
                "Fazenda": FitMinisterio.BOM,
                "Relacoes_Exteriores": FitMinisterio.FORTE,
                "Cultura": FitMinisterio.FORTE,
            }),

        CandidatoEsquerda(
            nome="Samara Martins", partido="UP", cargo="presidente", uf="SP",
            score_capacidade=1.50,
            origem="movimento social",
            feito_real="Dentista. Militante do MTST. Sem cargo eletivo. Sem gestao publica.",
            fits={
                "Saude": FitMinisterio.FRACO,
                "Desenvolvimento_Social": FitMinisterio.FRACO,
            }),

        CandidatoEsquerda(
            nome="Edmilson Costa", partido="PCB", cargo="presidente", uf="SP",
            score_capacidade=2.00,
            origem="tecnico/academico",
            feito_real="Economista. Professor USP. Sem cargo eletivo executivo.",
            fits={
                "Fazenda": FitMinisterio.BOM,
                "Planejamento": FitMinisterio.BOM,
                "Educacao": FitMinisterio.FRACO,
            }),

        CandidatoEsquerda(
            nome="Hertz Dias", partido="PSTU", cargo="presidente", uf="SP",
            score_capacidade=1.30,
            origem="academico",
            feito_real="Professor universitario. Sem cargo executivo. Sem gestao publica.",
            fits={
                "Educacao": FitMinisterio.FRACO,
            }),

        CandidatoEsquerda(
            nome="Rui Costa Pimenta", partido="PCO", cargo="presidente", uf="SP",
            score_capacidade=1.20,
            origem="politico",
            feito_real="Dirigente PCO. Sem cargo executivo. Sem gestao publica.",
            fits={
                "Desenvolvimento_Social": FitMinisterio.NENHUM,
            }),

        # ================================================================
        # PT -- DEPUTADOS E SENADORES COM SCORE >= 3.0
        # ================================================================

        CandidatoEsquerda(
            nome="Camilo Santana", partido="PT", cargo="senador", uf="CE",
            score_capacidade=4.72,
            origem="politico/tecnico",
            feito_real="Governador CE 2x. IDEB subiu. Vacinacao 95%. Min Educacao.",
            fits={
                "Educacao": FitMinisterio.PERFEITO,
                "Saude": FitMinisterio.FORTE,
                "Casa_Civil": FitMinisterio.BOM,
                "Planejamento": FitMinisterio.BOM,
                "Cidades": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Jaques Wagner", partido="PT", cargo="senador", uf="BA",
            score_capacidade=3.87,
            origem="movimento/sindical",
            feito_real="Governador BA. Ministro Casa Civil. Lideranca industrial (Ford).",
            fits={
                "Casa_Civil": FitMinisterio.PERFEITO,
                "Desenvolvimento_Industrial": FitMinisterio.FORTE,
                "Trabalho": FitMinisterio.FORTE,
                "Transportes": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Humberto Costa", partido="PT", cargo="senador", uf="PE",
            score_capacidade=3.38,
            origem="politico",
            feito_real="Ministro Saude (2x). Prefeito Recife. Medico.",
            fits={
                "Saude": FitMinisterio.PERFEITO,
                "Previdencia": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Gleisi Hoffmann", partido="PT", cargo="deputada", uf="PR",
            score_capacidade=3.37,
            origem="politico/tecnico",
            feito_real="Presidente PT. Senadora. Chefe Casa Civil. Advogada.",
            fits={
                "Casa_Civil": FitMinisterio.PERFEITO,
                "Relacoes_Exteriores": FitMinisterio.BOM,
                "Justica_Seguranca": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Patrus Ananias", partido="PT", cargo="deputado", uf="MG",
            score_capacidade=3.29,
            origem="politico",
            feito_real="Ministro Cidades (2x). Minha Casa Minha Vida. Saneamento.",
            fits={
                "Cidades": FitMinisterio.PERFEITO,
                "Habitacao": FitMinisterio.PERFEITO,
                "Saneamento": FitMinisterio.FORTE,
            }),

        CandidatoEsquerda(
            nome="Arthur Lira", partido="PP", cargo="deputado", uf="AL",
            score_capacidade=3.30,
            origem="politico",
            feito_real="Presidente Camara. Articulador. Nao e esquerda pura mas opera com PT.",
            fits={
                "Casa_Civil": FitMinisterio.BOM,
                "Planejamento": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Benedita da Silva", partido="PT", cargo="deputada", uf="RJ",
            score_capacidade=3.04,
            origem="movimento",
            feito_real="Governadora RJ. Ministra. Favela, mulher, negra.",
            fits={
                "Mulheres": FitMinisterio.PERFEITO,
                "Igualdade_Racial": FitMinisterio.PERFEITO,
                "Direitos_Humanos": FitMinisterio.FORTE,
                "Cidades": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Paulo Paim", partido="PT", cargo="senador", uf="RS",
            score_capacidade=3.17,
            origem="sindical",
            feito_real="Senador RS 5x. Sindicalista. Coerencia 30 anos.",
            fits={
                "Trabalho": FitMinisterio.PERFEITO,
                "Previdencia": FitMinisterio.FORTE,
            }),

        CandidatoEsquerda(
            nome="Afonso Florence", partido="PT", cargo="deputado", uf="BA",
            score_capacidade=2.58,
            origem="movimento",
            feito_real="Deputado. Lideranca agraria. MST.",
            fits={
                "Agraria_Familiar": FitMinisterio.FORTE,
                "Agricultura": FitMinisterio.BOM,
            }),

        # ================================================================
        # PSOL
        # ================================================================

        CandidatoEsquerda(
            nome="Sonia Guajajara", partido="PSOL", cargo="deputada", uf="SP",
            score_capacidade=2.92,
            origem="movimento/indigena",
            feito_real="Ministra Povos Originarios. Lider APIB. Nobel alternativo.",
            fits={
                "Indigenas": FitMinisterio.PERFEITO,
                "Meio_Ambiente": FitMinisterio.FORTE,
                "Igualdade_Racial": FitMinisterio.BOM,
                "Cultura": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Erika Hilton", partido="PSOL", cargo="deputada", uf="SP",
            score_capacidade=2.67,
            origem="movimento",
            feito_real="Deputada. Vereadora SP. Primeira transexual eleita.",
            fits={
                "Direitos_Humanos": FitMinisterio.PERFEITO,
                "Mulheres": FitMinisterio.FORTE,
                "Igualdade_Racial": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Luiza Erundina", partido="PSOL", cargo="deputada", uf="SP",
            score_capacidade=3.13,
            origem="movimento/sindical",
            feito_real="Prefeita SP. 30 anos coerencia. Educacao, saude publica.",
            fits={
                "Cultura": FitMinisterio.FORTE,
                "Educacao": FitMinisterio.FORTE,
                "Saude": FitMinisterio.BOM,
                "Cidades": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Marcelo Freixo", partido="PSOL", cargo="tecnico", uf="RJ",
            score_capacidade=3.00,
            origem="movimento",
            feito_real="Deputado. Candiato governador RJ. Comissao de Direitos Humanos.",
            fits={
                "Justica_Seguranca": FitMinisterio.FORTE,
                "Direitos_Humanos": FitMinisterio.PERFEITO,
                "Cultura": FitMinisterio.BOM,
            }),

        # ================================================================
        # PSB
        # ================================================================

        CandidatoEsquerda(
            nome="Flavio Dino", partido="PSB", cargo="senador", uf="MA",
            score_capacidade=4.14,
            origem="politico/judicial",
            feito_real="Governador MA 2x. Reduziu homicidios. Ministro Justica. STF.",
            fits={
                "Justica_Seguranca": FitMinisterio.PERFEITO,
                "CGU": FitMinisterio.FORTE,
                "Casa_Civil": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Cid Gomes", partido="PSB", cargo="senador", uf="CE",
            score_capacidade=3.22,
            origem="politico/tecnico",
            feito_real="Governador CE. Prefeito Fortaleza. Educacao e infraestrutura.",
            fits={
                "Educacao": FitMinisterio.FORTE,
                "Cidades": FitMinisterio.FORTE,
                "Transportes": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Jonas Donizette", partido="PSB", cargo="deputado", uf="SP",
            score_capacidade=2.58,
            origem="politico",
            feito_real="Prefeito Campinas. Deputado. Gestao municipal.",
            fits={
                "Cidades": FitMinisterio.FORTE,
                "Ciencia_Tecnologia": FitMinisterio.BOM,
            }),

        # ================================================================
        # PCdoB
        # ================================================================

        CandidatoEsquerda(
            nome="Jandira Feghali", partido="PCdoB", cargo="deputada", uf="RJ",
            score_capacidade=3.00,
            origem="tecnico/profissional",
            feito_real="Deputada. Medica. Coerencia. Saude publica.",
            fits={
                "Saude": FitMinisterio.PERFEITO,
                "Ciencia_Tecnologia": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Orlando Silva", partido="PCdoB", cargo="deputado", uf="SP",
            score_capacidade=2.83,
            origem="movimento",
            feito_real="Ministro Esporte. Deputado. Professor educacao fisica.",
            fits={
                "Esporte": FitMinisterio.PERFEITO,
                "Educacao": FitMinisterio.FORTE,
                "Cultura": FitMinisterio.BOM,
            }),

        CandidatoEsquerda(
            nome="Manuela Davila", partido="PCdoB", cargo="tecnico", uf="RS",
            score_capacidade=2.50,
            origem="politico",
            feito_real="Deputada. Vice-governadora RS. Jovem lideranca.",
            fits={
                "Educacao": FitMinisterio.BOM,
                "Mulheres": FitMinisterio.BOM,
            }),

        # ================================================================
        # REDE
        # ================================================================

        CandidatoEsquerda(
            nome="Marina Silva", partido="REDE", cargo="senadora", uf="AC",
            score_capacidade=4.11,
            origem="movimento/seringueira",
            feito_real="Reduziu desmatamento 80%. Cisternas. PAA. CONSEA. Ministra MMA.",
            fits={
                "Meio_Ambiente": FitMinisterio.PERFEITO,
                "Agraria_Familiar": FitMinisterio.PERFEITO,
                "Desenvolvimento_Social": FitMinisterio.FORTE,
                "Agricultura": FitMinisterio.BOM,
            }),

        # ================================================================
        # PDT
        # ================================================================

        CandidatoEsquerda(
            nome="Ciro Gomes", partido="PDT", cargo="deputado", uf="CE",
            score_capacidade=3.81,
            origem="politico/tecnico",
            feito_real="Governador CE. Ministro Integracao. Prefeito Fortaleza. 3x candidato presidente.",
            fits={
                "Integracao_Regional": FitMinisterio.PERFEITO,
                "Fazenda": FitMinisterio.FORTE,
                "Cidades": FitMinisterio.FORTE,
                "Planejamento": FitMinisterio.FORTE,
            }),

        # ================================================================
        # PV
        # ================================================================

        CandidatoEsquerda(
            nome="Fabio Macedo", partido="PV", cargo="deputado", uf="MA",
            score_capacidade=2.25,
            origem="politico",
            feito_real="Deputado. Ambientalista.",
            fits={
                "Meio_Ambiente": FitMinisterio.BOM,
            }),
    ]


class EsquerdaUnificada:
    """
    Frente de esquerda unificada. Cada candidato no melhor ministerio.
    """

    MINISTERIOS = [
        # Estado maior
        "Casa_Civil", "Vice_Presidencia",
        # Economia
        "Fazenda", "Planejamento", "Desenvolvimento_Industrial",
        # Social
        "Saude", "Educacao", "Desenvolvimento_Social", "Trabalho",
        "Previdencia", "Cultura", "Esporte", "Cidades",
        # Direitos
        "Mulheres", "Igualdade_Racial", "Direitos_Humanos", "Indigenas",
        # Justica
        "Justica_Seguranca", "CGU",
        # Ambiente e Ciencia
        "Meio_Ambiente", "Ciencia_Tecnologia",
        # Infra
        "Transportes", "Minas_Energia", "Comunicacoes",
        # Outros
        "Agricultura", "Agraria_Familiar", "Integracao_Regional",
        "Relacoes_Exteriores", "Habitacao", "Saneamento",
    ]

    def __init__(self):
        self.candidatos = _init_candidatos()

    def melhor_candidato_por_ministerio(self) -> Dict[str, Dict[str, Any]]:
        """Para cada ministerio, o melhor candidato de esquerda."""
        resultado = {}
        for minist in self.MINISTERIOS:
            # Filtra candidatos com fit nesse ministerio
            candidatos_fit = []
            for c in self.candidatos:
                if minist in c.fits:
                    score_final = c.score_capacidade * (c.fits[minist].value / 5.0)
                    candidatos_fit.append({
                        "nome": c.nome, "partido": c.partido, "uf": c.uf,
                        "cargo": c.cargo, "score_base": c.score_capacidade,
                        "fit": c.fits[minist].value, "fit_nome": c.fits[minist].name,
                        "score_final": round(score_final, 2),
                        "feito": c.feito_real, "origem": c.origem,
                    })
            # Ordena por score_final
            candidatos_fit.sort(key=lambda x: x["score_final"], reverse=True)
            if candidatos_fit:
                resultado[minist] = {
                    "melhor": candidatos_fit[0],
                    "alternativas": candidatos_fit[1:3],
                    "total_candidatos": len(candidatos_fit),
                }
            else:
                resultado[minist] = {"melhor": None, "alternativas": [], "total_candidatos": 0}
        return resultado

    def ranking_candidatos(self) -> List[Dict[str, Any]]:
        """Ranking geral por score de capacidade."""
        return sorted([{
            "nome": c.nome, "partido": c.partido, "uf": c.uf,
            "cargo": c.cargo, "score": c.score_capacidade,
            "feito": c.feito_real[:60], "origem": c.origem,
            "n_ministerios": len(c.fits),
        } for c in self.candidatos], key=lambda x: x["score"], reverse=True)

    def scorecard(self) -> Dict[str, Any]:
        return {
            "modulo": "open_esquerda_unificada",
            "versao": "0.1.0-spec",
            "candidatos": len(self.candidatos),
            "partidos": len(set(c.partido for c in self.candidatos)),
            "ministerios": len(self.MINISTERIOS),
            "candidatos_presidenciais": sum(1 for c in self.candidatos if c.cargo == "presidente"),
            "principio": "Unir a esquerda. Cada um no melhor ministerio.",
        }

    def governista_ou_independente(self) -> Dict[str, List[str]]:
        """Separa quem esta na base governista de quem e independente."""
        governista = ["PT", "PSB", "PCdoB", "PV", "PDT", "REDE", "SOLIDARIEDADE"]
        independente = ["PSOL", "PSTU", "PCB", "PCO", "UP"]
        resultado = {"governista": [], "independente": []}
        for c in self.candidatos:
            if c.partido in governista:
                resultado["governista"].append(f"{c.nome} ({c.partido})")
            elif c.partido in independente:
                resultado["independente"].append(f"{c.nome} ({c.partido})")
        return resultado


def _demo():
    eu = EsquerdaUnificada()
    sc = eu.scorecard()
    melhores = eu.melhor_candidato_por_ministerio()
    ranking = eu.ranking_candidatos()
    separacao = eu.governista_ou_independente()

    print("=" * 85)
    print("FRENTE DE ESQUERDA UNIFICADA -- Cada um no melhor ministerio")
    print("=" * 85)

    print(f"\n{sc['candidatos']} candidatos | {sc['partidos']} partidos | {sc['ministerios']} ministerios")
    print(f"Candidatos presidenciais: {sc['candidatos_presidenciais']}")

    print(f"\n{'='*85}")
    print("SEPARACAO: GOVERNISTA x INDEPENDENTE")
    print(f"{'='*85}")
    print(f"\n  GOVERNISTA (base aliada):")
    for nome in separacao["governista"]:
        print(f"    + {nome}")
    print(f"\n  INDEPENDENTE (fora da base):")
    for nome in separacao["independente"]:
        print(f"    - {nome}")

    print(f"\n{'='*85}")
    print("MINISTERIO -> MELHOR CANDIDATO DE ESQUERDA")
    print(f"{'='*85}")
    for minist in eu.MINISTERIOS:
        info = melhores.get(minist, {})
        melhor = info.get("melhor")
        if melhor:
            alts = info.get("alternativas", [])
            score = melhor["score_final"]
            fit = melhor["fit_nome"]
            flag = " *** APROVADO" if score >= 4.0 else ""
            print(f"\n  {minist.replace('_', ' '):<30}")
            print(f"    -> {melhor['nome']:<25} {melhor['partido']:<6} score={score:.2f} fit={fit}{flag}")
            print(f"       FEZ: {melhor['feito'][:65]}")
            if alts:
                for a in alts:
                    print(f"    ALT: {a['nome']:<25} {a['partido']:<6} score={a['score_final']:.2f}")
        else:
            print(f"\n  {minist.replace('_', ' '):<30}")
            print(f"    -> SEM CANDIDATO DE ESQUERDA")

    print(f"\n{'='*85}")
    print("VEREDITO")
    print(f"{'='*85}")
    aprovados = [m for m in melhores.values() if m.get("melhor") and m["melhor"]["score_final"] >= 4.0]
    sem_candidato = [m for m in melhores.values() if not m.get("melhor")]
    print(f"  Ministerios com candidato APROVADO (>=4.0): {len(aprovados)}")
    print(f"  Ministerios SEM candidato de esquerda: {len(sem_candidato)}")
    print(f"\n  MINISTERIOS SEM ESQUERDA:")
    for minist in eu.MINISTERIOS:
        info = melhores.get(minist, {})
        if not info.get("melhor"):
            print(f"    *** {minist.replace('_', ' ')}")


if __name__ == "__main__":
    _demo()
