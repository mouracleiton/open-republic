#!/usr/bin/env python3
"""
OpenRepresentatividade -- Brasil Real no Poder
================================================
"Se 56% é negro e 50% é mulher, o poder tem que parecer isso.
 Se não parece, não é representação. É apropriação."

5 EIXOS DE REPRESENTATIVIDADE para maximizar a correspondência
entre o poder político e a população brasileira real.

EIXOS:
  1. FENOTÍPICO (cor/raça)
  2. GEOGRÁFICO-CULTURAL (região e contexto)
  3. SOCIOECONÔMICO (classe e renda)
  4. ORIGEM E MOBILIDADE (raízes)
  5. COMPLEMENTAR (contexto de vida)

Cada candidato recebe tags. O sistema mede o GAP entre
a composição política e a população real.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from collections import Counter


# ============================================================================
# 1. EIXOS DE REPRESENTATIVIDADE
# ============================================================================

class EixoRep(Enum):
    FENOTIPICO = "fenotipico"
    GEOGRAFICO = "geografico"
    SOCIOECONOMICO = "socioeconomico"
    ORIGEM = "origem"
    COMPLEMENTAR = "complementar"


@dataclass(frozen=True)
class TagRepresentatividade:
    id: str
    nome: str
    eixo: EixoRep
    pct_populacao: float       # % real da população brasileira
    descricao: str


def _init_tags() -> Dict[str, TagRepresentatividade]:
    return {

        # ===== 1. FENOTÍPICO (IBGE 2022) =====
        "branco": TagRepresentatividade(
            "branco", "Branco", EixoRep.FENOTIPICO, 43.5,
            "Fenótipo europeu predominante."),
        "pardo": TagRepresentatividade(
            "pardo", "Pardo", EixoRep.FENOTIPICO, 45.3,
            "Mistura evidente (euro-afro-indígena). Maioria estatística."),
        "preto": TagRepresentatividade(
            "preto", "Preto", EixoRep.FENOTIPICO, 10.6,
            "Fenótipo africano predominante."),
        "amarelo": TagRepresentatividade(
            "amarelo", "Amarelo", EixoRep.FENOTIPICO, 0.4,
            "Ascendência leste-asiática."),
        "indigena_cor": TagRepresentatividade(
            "indigena_cor", "Indígena (cor)", EixoRep.FENOTIPICO, 0.2,
            "Povos originários (autodeclaração de cor)."),

        # ===== 2. GEOGRÁFICO-CULTURAL =====
        "norte_amazonico": TagRepresentatividade(
            "norte_amazonico", "Norte Amazônico", EixoRep.GEOGRAFICO, 8.5,
            "Região norte. Logística fluvial, cultura ribeirinha."),
        "nordeste_litoral": TagRepresentatividade(
            "nordeste_litoral", "Nordeste Litoral", EixoRep.GEOGRAFICO, 18.0,
            "Faixa costeira. Turismo, alta densidade."),
        "nordeste_sertao": TagRepresentatividade(
            "nordeste_sertao", "Nordeste Sertão", EixoRep.GEOGRAFICO, 10.0,
            "Semiárido. Desafios hídricos, cultura específica."),
        "centro_oeste_agro": TagRepresentatividade(
            "centro_oeste_agro", "Centro-Oeste Agro", EixoRep.GEOGRAFICO, 7.8,
            "MT, GO, MS. Agronegócio, alta renda em polos."),
        "sudeste_metro": TagRepresentatividade(
            "sudeste_metro", "Sudeste Metropolitano", EixoRep.GEOGRAFICO, 30.0,
            "SP/RJ. Centro financeiro, multicultural."),
        "sudeste_interior": TagRepresentatividade(
            "sudeste_interior", "Sudeste Interior", EixoRep.GEOGRAFICO, 13.0,
            "Vale do Paraíba, Campinas, Triângulo Mineiro. Industrializado."),
        "sul_gaucho": TagRepresentatividade(
            "sul_gaucho", "Sul Gaúcho/Platino", EixoRep.GEOGRAFICO, 6.8,
            "RS. Influência platina, clima temperado."),
        "sul_caicara": TagRepresentatividade(
            "sul_caicara", "Sul Caçara/Ítalo", EixoRep.GEOGRAFICO, 6.9,
            "PR e SC. Influência europeia recente, industrialização difusa."),

        # ===== 3. SOCIOECONÔMICO =====
        "elite_alta_renda": TagRepresentatividade(
            "elite_alta_renda", "Elite Alta Renda", EixoRep.SOCIOECONOMICO, 1.5,
            "Topo da pirâmide. Consumo global, ativos robustos."),
        "classe_media_alta": TagRepresentatividade(
            "classe_media_alta", "Classe Média Alta", EixoRep.SOCIOECONOMICO, 8.5,
            "Profissionais liberais, gestores. Saúde/educação privada."),
        "classe_media_tradicional": TagRepresentatividade(
            "classe_media_tradicional", "Classe Média Tradicional", EixoRep.SOCIOECONOMICO, 20.0,
            "Estabilidade, posse de imóveis, consumo consciente."),
        "nova_classe_media": TagRepresentatividade(
            "nova_classe_media", "Nova Classe Média", EixoRep.SOCIOECONOMICO, 30.0,
            "Ascensão recente, consumo aspiracional, vulnerável a crises."),
        "base_vulneravel": TagRepresentatividade(
            "base_vulneravel", "Base Vulnerável", EixoRep.SOCIOECONOMICO, 28.0,
            "Baixa renda, dependência de programas sociais, informalidade."),
        "extrema_pobreza": TagRepresentatividade(
            "extrema_pobreza", "Extrema Pobreza", EixoRep.SOCIOECONOMICO, 12.0,
            "Subsistência, exclusão de serviços básicos."),

        # ===== 4. ORIGEM E MOBILIDADE =====
        "desc_europeia": TagRepresentatividade(
            "desc_europeia", "Descendência Europeia Recente", EixoRep.ORIGEM, 10.0,
            "Italianos, portugueses, alemães, eslavos (Sul/SP)."),
        "desc_africana": TagRepresentatividade(
            "desc_africana", "Descendência Africana", EixoRep.ORIGEM, 56.0,
            "Raízes na diáspora. Bahia, RJ, MA, todo o Brasil."),
        "desc_indigena": TagRepresentatividade(
            "desc_indigena", "Descendência Indígena", EixoRep.ORIGEM, 8.0,
            "Presença forte no Norte/Nordeste/Centro-Oeste."),
        "desc_asiatica": TagRepresentatividade(
            "desc_asiatica", "Descendência Asiática", EixoRep.ORIGEM, 1.0,
            "Concentrada em SP e PR."),
        "migrante_interno": TagRepresentatividade(
            "migrante_interno", "Migrante Interno", EixoRep.ORIGEM, 15.0,
            "Nordestinos no Sudeste, sulistas no Centro-Oeste."),
        "imigrante_recente": TagRepresentatividade(
            "imigrante_recente", "Imigrante Recente", EixoRep.ORIGEM, 1.0,
            "Haitianos, venezuelanos, sírios, africanos subsaarianos."),

        # ===== 5. COMPLEMENTAR =====
        "urbano_periferia": TagRepresentatividade(
            "urbano_periferia", "Urbano Periferia", EixoRep.COMPLEMENTAR, 35.0,
            "Grandes aglomerados, transporte precário, economia informal."),
        "urbano_centro": TagRepresentatividade(
            "urbano_centro", "Urbano Centro", EixoRep.COMPLEMENTAR, 45.0,
            "Acesso facilitado a infraestrutura."),
        "rural_produtor": TagRepresentatividade(
            "rural_produtor", "Rural Produtor", EixoRep.COMPLEMENTAR, 8.0,
            "Pequeno/médio agricultor."),
        "rural_subsistencia": TagRepresentatividade(
            "rural_subsistencia", "Rural Subsistência", EixoRep.COMPLEMENTAR, 7.0,
            "Agricultura familiar de baixa tecnologia."),
        "digital_conectado": TagRepresentatividade(
            "digital_conectado", "Digitalmente Conectado", EixoRep.COMPLEMENTAR, 70.0,
            "Acesso pleno à internet e serviços digitais."),
        "exclusao_digital": TagRepresentatividade(
            "exclusao_digital", "Exclusão Digital", EixoRep.COMPLEMENTAR, 30.0,
            "Dependência de pontos públicos ou sem acesso."),
    }


# ============================================================================
# 2. PERFIL DE CANDIDATO
# ============================================================================

@dataclass
class PerfilCandidato:
    """Perfil representativo de um candidato."""
    nome: str
    cargo_desejado: str
    tags: List[str] = field(default_factory=list)

    def tags_por_eixo(self, eixo: EixoRep) -> List[str]:
        return [t for t in self.tags if _TAGS.get(t) and _TAGS[t].eixo == eixo]


# ============================================================================
# 3. MEDIDOR DE GAP REPRESENTATIVO
# ============================================================================

@dataclass
class GapRepresentatividade:
    """Diferença entre composição política e população real."""
    tag_id: str
    tag_nome: str
    eixo: EixoRep
    pct_populacao: float      # % na população real
    pct_composicao: float      # % na composição política atual
    gap: float                 # diferença (negativo = sub-representado)
    status: str                # "sub-representado", "proporcional", "super-representado"

    def resumo(self) -> str:
        icon = {"sub-representado": "❌", "proporcional": "✅", "super-representado": "⚠️"}.get(self.status, "?")
        return (
            f"{icon} {self.tag_nome}: pop={self.pct_populacao:.1f}% | "
            f"poder={self.pct_composicao:.1f}% | gap={self.gap:+.1f}%"
        )


def medir_gap(
    candidatos: List[PerfilCandidato],
) -> List[GapRepresentatividade]:
    """
    Mede o gap entre a composição política e a população real.

    Para cada tag, compara:
      - % da população real (IBGE)
      - % da composição política (candidatos com essa tag)

    Gap negativo = sub-representado (falta gente desse grupo)
    Gap positivo = super-representado (sobra gente desse grupo)
    """
    total_cand = len(candidatos)
    if total_cand == 0:
        return []

    # Contar tags por candidato
    tag_counts: Counter = Counter()
    for c in candidatos:
        for t in c.tags:
            if t in _TAGS:
                tag_counts[t] += 1

    gaps = []
    for tag_id, tag in _TAGS.items():
        pct_composicao = (tag_counts.get(tag_id, 0) / total_cand) * 100
        gap = pct_composicao - tag.pct_populacao

        if gap < -5.0:
            status = "sub-representado"
        elif gap > 5.0:
            status = "super-representado"
        else:
            status = "proporcional"

        gaps.append(GapRepresentatividade(
            tag_id, tag.nome, tag.eixo,
            tag.pct_populacao, pct_composicao, gap, status,
        ))

    return gaps


def score_representatividade(candidatos: List[PerfilCandidato]) -> Tuple[float, List[GapRepresentatividade]]:
    """
    Score de 0-100. 100 = composição perfeitamente proporcional.

    Retorna (score, lista_de_gaps).
    """
    gaps = medir_gap(candidatos)
    if not gaps:
        return 0.0, []

    # Penaliza gaps absolutos
    penalidade_total = sum(abs(g.gap) for g in gaps)
    # Penaliza mais sub-representação (falta gente) que super-representação
    penalidade_sub = sum(abs(g.gap) * 1.5 for g in gaps if g.status == "sub-representado")
    penalidade_total += penalidade_sub

    # Normalizar: 0 gaps = 100, mais gaps = menos
    score = max(0.0, 100.0 - (penalidade_total / len(gaps)))

    return score, gaps


# ============================================================================
# 4. SISTEMA
# ============================================================================

_TAGS: Dict[str, TagRepresentatividade] = {}


def _init():
    global _TAGS
    _TAGS = _init_tags()


_init()


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo():
    print("=" * 70)
    print("OPEN REPRESENTATIVIDADE — BRASIL REAL NO PODER")
    print("=" * 70)

    print(f"\n{_len_tags()} TAGS em 5 eixos:\n")
    for eixo in EixoRep:
        tags = [t for t in _TAGS.values() if t.eixo == eixo]
        print(f"  {eixo.value.upper()} ({len(tags)} tags):")
        for t in tags:
            print(f"    {t.nome:30s} {t.pct_populacao:5.1f}% da população")
        print()

    # Simular composição atual (MOCK)
    print("=" * 70)
    print("SIMULAÇÃO: COMPOSIÇÃO POLÍTICA MOCK (exemplo)\n")

    composicao_mock = [
        PerfilCandidato("[MOCK] Candidato 1", "Presidente", ["branco", "sudeste_metro", "elite_alta_renda", "desc_europeia", "urbano_centro", "digital_conectado"]),
        PerfilCandidato("[MOCK] Candidato 2", "Governador", ["branco", "sul_gaucho", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"]),
        PerfilCandidato("[MOCK] Candidato 3", "Senador", ["pardo", "nordeste_litoral", "classe_media_tradicional", "desc_africana", "urbano_centro", "digital_conectado"]),
        PerfilCandidato("[MOCK] Candidato 4", "Deputado", ["branco", "sudeste_interior", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"]),
        PerfilCandidato("[MOCK] Candidato 5", "Deputado", ["branco", "centro_oeste_agro", "classe_media_tradicional", "desc_europeia", "rural_produtor", "digital_conectado"]),
    ]

    score, gaps = score_representatividade(composicao_mock)
    print(f"  SCORE DE REPRESENTATIVIDADE: {score:.1f}/100\n")

    # Mostrar gaps críticos
    sub = [g for g in gaps if g.status == "sub-representado"]
    sub.sort(key=lambda g: g.gap)

    print(f"  SUB-REPRESENTADOS ({len(sub)} grupos com falta no poder):")
    for g in sub[:10]:
        print(f"    {g.resumo()}")

    print()
    sup = [g for g in gaps if g.status == "super-representado"]
    sup.sort(key=lambda g: -g.gap)
    print(f"  SUPER-REPRESENTADOS ({len(sup)} grupos com excesso no poder):")
    for g in sup[:10]:
        print(f"    {g.resumo()}")

    print()
    print("=" * 70)
    print("META: maximizar representatividade.")
    print("  Cada candidato adicionado deve cobrir um gap.")
    print("  Se falta preto no poder, o próximo indicado DEVE ser preto.")
    print("  Se falta periferia, o próximo DEVE vir da periferia.")


def _len_tags() -> int:
    return len(_TAGS)


if __name__ == "__main__":
    _demo()
