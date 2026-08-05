#!/usr/bin/env python3
"""
OpenCruzamento -- O Sistema Unificado de Avaliação
=====================================================
"Pegamos 3 sistemas. Juntamos num só. O político não tem mais onde se esconder."

CRUZA:
  1. Score base (C1×3 + C2×2 + C3×1) / 6 × 5
  2. 33 Etiquetas políticas (impacto -0.30 a +0.25 cada)
  3. Camada 0 (Omissão -0.50 / Comissão +0.30)
  4. 31 Tags de Representatividade (5 eixos)
  5. Regra de Reeleição por Mérito (AUTORIZADO/BLOQUEADO)

OUTPUT: Score final unificado + etiquetas + representatividade + bloqueio.

AVISO: Tudo aqui é SIMULAÇÃO. Os scores são OPINIAO ate triangulacao.
O sistema de medicao é REAL. Os dados atribuidos sao HIPOTETICOS.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# Importar todos os modulos
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import open_politico_score as ps
import open_etiquetas_politicas as et
import open_representatividade as rep
import open_sem_reeleicao as sr


# ============================================================================
# 1. DADOS DE AVALIACAO (etiquetas + representatividade + omissao por politico)
# ============================================================================

# Esta tabela cruza os 60 politicos com etiquetas, tags e merito.
# OPINIAO ate verificacao com fonte externa.

AVALIACAO_COMPLETA: Dict[str, Dict[str, Any]] = {
    # === APROVADOS ===
    "Camilo Santana": {
        "etiquetas": ["executor_eficiente", "meritocratico_tecnico", "baseado_em_evidencias", "visao_legado"],
        "tags_rep": ["pardo", "nordeste_litoral", "nova_classe_media", "desc_africana", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.GOVERNADOR, "2015-2022", True, "IDEB 4.2->5.8 (INEP)", "Educacao melhorou")],
    },
    "Marina Silva": {
        "etiquetas": ["baseado_em_evidencias", "visao_legado", "vidro_transparente", "protetor_vulneravel"],
        "tags_rep": ["pardo", "norte_amazonico", "base_vulneravel", "desc_indigena", "rural_subsistencia", "exclusao_digital"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.MINISTRO, "2003-2008", True, "Desmatamento 27792->12911 km2 (PRODES/INPE)", "Reduziu desmatamento")],
    },
    # === ALTO SCORE ===
    "Jaques Wagner": {
        "etiquetas": ["executor_eficiente", "conciliador_pragmatico"],
        "tags_rep": ["branco", "nordeste_litoral", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.GOVERNADOR, "2007-2015", False, "BA ainda pior IDH", "Desigualdade persistiu")],
    },
    "Jader Barbalha": {
        "etiquetas": ["apadrinhado_politico", "camaleao_oportunista"],
        "tags_rep": ["branco", "norte_amazonico", "elite_alta_renda", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.SENADOR, "multiplas", False, "PA continua com fome", "Omissao")],
    },
    "Renan Calheiros": {
        "etiquetas": ["caixa_preta", "apadrinhado_politico", "camaleao_oportunista"],
        "tags_rep": ["branco", "nordeste_litoral", "elite_alta_renda", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.SENADOR, "multiplas", False, "Operacao Lava Jato", "Corrupcao")],
    },
    "Fernando Haddad": {
        "etiquetas": ["planejador_estrategico", "baseado_em_evidencias", "meritocratico_tecnico"],
        "tags_rep": ["branco", "sudeste_metro", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.MINISTRO, "2005-2012", True, "IDEB subiu (INEP)", "Educacao melhorou"),
                    sr.CargoOcupado(sr.TipoCargo.PREFEITO, "2013-2016", None, "", "Sem dado conclusivo")],
    },
    "Flavio Dino": {
        "etiquetas": ["executor_eficiente", "protetor_vulneravel", "vidro_transparente"],
        "tags_rep": ["branco", "nordeste_litoral", "classe_media_tradicional", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.GOVERNADOR, "2015-2022", True, "MA melhorou IDH (IBGE)", "Pobreza reduziu")],
    },
    "Ciro Gomes": {
        "etiquetas": ["planejador_estrategico", "executor_eficiente", "conciliador_pragmatico"],
        "tags_rep": ["branco", "nordeste_litoral", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.GOVERNADOR, "2003-2006", True, "CE melhorou (IBGE)", "Gestao reconhecida")],
    },
    "Dilma Rousseff": {
        "etiquetas": ["baseado_em_evidencias", "planejador_estrategico", "vidro_transparente"],
        "tags_rep": ["branco", "sul_gaucho", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.PRESIDENTE, "2011-2016", False, "Fome voltou (VIGISAN)", "Deposta em golpe")],
    },
    "Rodrigo Pacheco": {
        "etiquetas": ["conciliador_pragmatico"],
        "tags_rep": ["branco", "sudeste_interior", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.SENADOR, "2019-2026", None, "", "Sem dado")],
    },
    "Randolfe Rodrigues": {
        "etiquetas": ["coerente_programatico", "protetor_vulneravel"],
        "tags_rep": ["pardo", "norte_amazonico", "nova_classe_media", "desc_indigena", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.SENADOR, "2011-2026", None, "", "Sem dado")],
    },
    "Humberto Costa": {
        "etiquetas": ["planejador_estrategico"],
        "tags_rep": ["branco", "nordeste_litoral", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.SENADOR, "2011-2026", None, "", "Sem dado")],
    },
    "Wellington Dias": {
        "etiquetas": ["protetor_vulneravel", "executor_eficiente"],
        "tags_rep": ["pardo", "nordeste_sertao", "base_vulneravel", "desc_africana", "urbano_periferia", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.GOVERNADOR, "2003-2010, 2015-2022", True, "PI melhorou (IBGE)", "Pobreza reduziu")],
    },
    "Simone Tebet": {
        "etiquetas": ["planejador_estrategico", "baseado_em_evidencias", "vidro_transparente"],
        "tags_rep": ["branco", "centro_oeste_agro, ", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.SENADOR, "2015-2026", None, "", "Sem dado")],
    },
    "Eduardo Leite": {
        "etiquetas": ["meritocratico_tecnico", "estado_digital"],
        "tags_rep": ["branco", "sul_gaucho, ", "elite_alta_renda", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.GOVERNADOR, "2019-2022", None, "", "Sem dado")],
    },
    "Rui Costa": {
        "etiquetas": ["executor_eficiente", "visao_legado"],
        "tags_rep": ["pardo", "nordeste_litoral", "classe_media_tradicional", "desc_africana", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.GOVERNADOR, "2015-2022", True, "BA melhorou (IBGE)", "Desigualdade reduziu")],
    },
    "Sonia Guajajara": {
        "etiquetas": ["protetor_vulneravel", "coerente_programatico", "vidro_transparente"],
        "tags_rep": ["indigena_cor", "norte_amazonico", "base_vulneravel", "desc_indigena", "rural_subsistencia", "exclusao_digital"],
        "cargos": [],
    },
    "Jandira Feghali": {
        "etiquetas": ["baseado_em_evidencias", "protetor_vulneravel"],
        "tags_rep": ["pardo", "sudeste_metro", "nova_classe_media", "desc_africana", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.DEPUTADO_FEDERAL, "2015-2026", None, "", "Sem dado")],
    },
    "Patrus Ananias": {
        "etiquetas": ["protetor_vulneravel", "visao_legado"],
        "tags_rep": ["branco", "sudeste_interior", "classe_media_tradicional", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.MINISTRO, "2003-2010", True, "Bolsa Familia (MDS)", "Fome Zero")],
    },
    "Paulo Paim": {
        "etiquetas": ["coerente_programatico", "protetor_vulneravel"],
        "tags_rep": ["preto", "sul_gaucho", "base_vulneravel", "desc_africana", "urbano_periferia", "exclusao_digital"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.SENADOR, "2003-2026", None, "", "Sem dado")],
    },
    "Erundina": {
        "etiquetas": ["coerente_programatico", "protetor_vulneravel"],
        "tags_rep": ["branco", "sudeste_metro", "classe_media_tradicional", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.PREFEITO, "1989-1992", True, "Habitacao popular SP", "Entregou")],
    },
    "Orlando Silva": {
        "etiquetas": ["coerente_programatico"],
        "tags_rep": ["preto", "sudeste_metro", "nova_classe_media", "desc_africana", "urbano_periferia", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.MINISTRO, "2011-2012", None, "", "Sem dado")],
    },
    "Jones Manoel": {
        "etiquetas": ["coerente_programatico", "baseado_em_evidencias"],
        "tags_rep": ["branco", "sudeste_metro", "nova_classe_media", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [],
    },
    "Samara Martins": {
        "etiquetas": ["coerente_programatico", "protetor_vulneravel"],
        "tags_rep": ["preto", "nordeste_litoral", "extrema_pobreza", "desc_africana", "urbano_periferia", "exclusao_digital"],
        "cargos": [],
    },
    "Celso Amorim": {
        "etiquetas": ["planejador_estrategico", "baseado_em_evidencias"],
        "tags_rep": ["branco", "sudeste_metro", "elite_alta_renda", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.MINISTRO, "2003-2010", True, "Sul-Sul diplomacia", "Itamaraty")],
    },
    "Ricardo Galvao": {
        "etiquetas": ["baseado_em_evidencias", "meritocratico_tecnico"],
        "tags_rep": ["branco", "sudeste_metro", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [],
    },
    "Silvio Almeida": {
        "etiquetas": ["baseado_em_evidencias", "protetor_vulneravel"],
        "tags_rep": ["preto", "sudeste_metro", "classe_media_alta", "desc_africana", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.MINISTRO, "2023-2026", None, "", "Sem dado")],
    },
    "Erika Hilton": {
        "etiquetas": ["coerente_programatico", "protetor_vulneravel"],
        "tags_rep": ["preto", "sudeste_metro", "base_vulneravel", "desc_africana", "urbano_periferia", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.DEPUTADO_FEDERAL, "2023-2026", None, "", "Primeiro mandato")],
    },
    # === BAIXO SCORE / WO ===
    "Sergio Moro": {
        "etiquetas": ["ideologico_rigido"],
        "tags_rep": ["branco", "sul_caicara", "classe_media_alta", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.MINISTRO, "2019-2020", False, "Politizacao Lava Jato", "Vazou conversas")],
    },
    "Tarcísio de Freitas": {
        "etiquetas": ["curto_prazista"],
        "tags_rep": ["branco", "sudeste_metro", "elite_alta_renda", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.GOVERNADOR, "2023-2026", None, "", "Primeiro mandato")],
    },
    "Romeiro Zema": {
        "etiquetas": ["predador_recursos", "elitista_excludente"],
        "tags_rep": ["branco", "sudeste_interior", "elite_alta_renda", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.GOVERNADOR, "2019-2026", None, "", "Sem dado")],
    },
    "Bolsonaro": {
        "etiquetas": ["negacionista_dados", "polarizador_toxico", "caixa_preta", "predador_recursos"],
        "tags_rep": ["branco", "sudeste_metro", "classe_media_tradicional", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.PRESIDENTE, "2019-2022", False, "Fome 10M->33M (VIGISAN)", "Pandemia negacionista")],
    },
    "Nikolas Ferreira": {
        "etiquetas": ["polarizador_toxico", "autor_lei_simbolica", "populista_numerico"],
        "tags_rep": ["branco", "sudeste_metro", "nova_classe_media", "desc_europeia", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.DEPUTADO_FEDERAL, "2023-2026", None, "", "Primeiro mandato")],
    },
    "Kim Kataguiri": {
        "etiquetas": ["autor_lei_simbolica", "populista_numerico"],
        "tags_rep": ["amarelo", "sudeste_metro", "classe_media_alta", "desc_asiatica", "urbano_centro", "digital_conectado"],
        "cargos": [sr.CargoOcupado(sr.TipoCargo.DEPUTADO_FEDERAL, "2019-2026", None, "", "Sem lei util")],
    },
}


# ============================================================================
# 2. CRUZAMENTO UNIFICADO
# ============================================================================

@dataclass
class AvaliacaoUnificada:
    """Resultado completo de um politico apos cruzar todos os sistemas."""
    nome: str
    score_base: float
    score_etiquetas: float
    score_camada0: float
    score_final: float
    status: str                    # APROVADO / WO / BLOQUEADO
    etiquetas: List[str]
    etiquetas_pos: List[str]
    etiquetas_neg: List[str]
    tags_rep: List[str]
    bloqueado_reeleicao: bool
    motivo_bloqueio: str
    explicacao_score: str
    cargos: List[Any]

    @property
    def endossado(self) -> bool:
        """OpenRepublic endossa este politico?"""
        return self.status == "APROVADO" and not self.bloqueado_reeleicao


def cruzar_politico(nome: str, cargo_desejado: Optional[sr.TipoCargo] = None) -> Optional[AvaliacaoUnificada]:
    """
    Cruza um politico em todos os sistemas.

    Returns None se o politico nao estiver no SCORES_DETALHADOS.
    """
    if nome not in ps.SCORES_DETALHADOS:
        return None

    c1, c2, c3, evidencia, alinhamento = ps.SCORES_DETALHADOS[nome]
    score_base = (c1 * 3 + c2 * 2 + c3 * 1) / 6 * 5

    av = AVALIACAO_COMPLETA.get(nome, {})
    etiqueta_ids = av.get("etiquetas", [])
    tags_rep = av.get("tags_rep", [])
    cargos = av.get("cargos", [])

    # 1. Etiquetas
    etiqueta_hashtags = [et._ETIQUETAS[e].hashtag for e in etiqueta_ids if e in et._ETIQUETAS]
    etiqueta_pos = [et._ETIQUETAS[e].hashtag for e in etiqueta_ids
                    if e in et._ETIQUETAS and et._ETIQUETAS[e].polaridade == et.Polaridade.POSITIVA]
    etiqueta_neg = [et._ETIQUETAS[e].hashtag for e in etiqueta_ids
                    if e in et._ETIQUETAS and et._ETIQUETAS[e].polaridade == et.Polaridade.NEGATIVA]

    # 2. Camada 0 + etiquetas
    omissao_obj = None
    if cargos:
        # Usar o primeiro cargo com resolveu=False ou o primeiro
        c_omissao = next((c for c in cargos if c.resolveu is False), cargos[0])
        omissao_obj = et.RegistroOmissao(
            nome, c_omissao.cargo.value, c_omissao.periodo,
            "problema", c_omissao.evidencia or "sem evidencia",
            c_omissao.evidencia or "sem evidencia",
            c_omissao.resolveu or False, "verificar"
        )

    perfil_et = et.classificar(nome, "", etiqueta_ids, omissao_obj)
    score_final, explicacao = et.aplicar_camada0(score_base, perfil_et)

    # Separar score de etiquetas vs camada0
    score_etiquetas = sum(et._ETIQUETAS[e].impacto_score for e in etiqueta_ids if e in et._ETIQUETAS)
    score_camada0 = score_final - score_base - score_etiquetas

    # 3. Reeleicao
    bloqueado = False
    motivo_bloqueio = ""
    if cargo_desejado and cargos:
        aval_reeleicao = sr.avaliar_candidatura(nome, cargo_desejado, cargos)
        bloqueado = not aval_reeleicao.endossado
        motivo_bloqueio = aval_reeleicao.motivo if bloqueado else ""

    # 4. Status final
    if bloqueado:
        status = "BLOQUEADO"
    elif score_final >= 4.0:
        status = "APROVADO"
    else:
        status = "WO"

    return AvaliacaoUnificada(
        nome=nome,
        score_base=round(score_base, 2),
        score_etiquetas=round(score_etiquetas, 2),
        score_camada0=round(score_camada0, 2),
        score_final=round(score_final, 2),
        status=status,
        etiquetas=etiqueta_hashtags,
        etiquetas_pos=etiqueta_pos,
        etiquetas_neg=etiqueta_neg,
        tags_rep=tags_rep,
        bloqueado_reeleicao=bloqueado,
        motivo_bloqueio=motivo_bloqueio,
        explicacao_score=explicacao,
        cargos=cargos,
    )


def cruzar_todos(cargo_desejado: Optional[sr.TipoCargo] = None) -> List[AvaliacaoUnificada]:
    """Cruza todos os 60 politicos."""
    resultados = []
    for nome in ps.SCORES_DETALHADOS:
        av = cruzar_politico(nome, cargo_desejado)
        if av:
            resultados.append(av)
    resultados.sort(key=lambda x: x.score_final, reverse=True)
    return resultados


# ============================================================================
# 3. DEMO
# ============================================================================

def _demo():
    print("=" * 75)
    print("OPEN CRUZAMENTO — SISTEMA UNIFICADO DE AVALIAÇÃO")
    print("=" * 75)
    print()
    print("CRUZA: Score base + 33 Etiquetas + Camada 0 + Representatividade + Reeleição")
    print()

    resultados = cruzar_todos()

    aprovados = [r for r in resultados if r.status == "APROVADO"]
    bloqueados = [r for r in resultados if r.status == "BLOQUEADO"]
    wo = [r for r in resultados if r.status == "WO"]

    print(f"RESULTADO: {len(resultados)} politicos")
    print(f"  APROVADOS: {len(aprovados)}")
    print(f"  BLOQUEADOS: {len(bloqueados)}")
    print(f"  WO: {len(wo)}")
    print()

    print("TOP 15:")
    print(f"  {'SCORE':>5} {'BASE':>5} {'ETIQ':>5} {'C0':>5} | {'NOME':30s} | {'STATUS':10s} | ETIQUETAS")
    print("  " + "-" * 100)
    for r in resultados[:15]:
        ets = ", ".join(r.etiquetas[:3]) if r.etiquetas else "—"
        print(f"  {r.score_final:5.2f} {r.score_base:5.2f} {r.score_etiquetas:+5.2f} {r.score_camada0:+5.2f} | "
              f"{r.nome:30s} | {r.status:10s} | {ets}")

    print()
    print("REPRESENTATIVIDADE (composição dos candidatos endossáveis):")
    # Score de representatividade
    endossaveis = [r for r in resultados if r.status != "BLOQUEADO"]
    perfis_rep = [rep.PerfilCandidato(r.nome, "", r.tags_rep) for r in endossaveis if r.tags_rep]
    if perfis_rep:
        score_rep, gaps = rep.score_representatividade(perfis_rep)
        print(f"  Score de representatividade: {score_rep:.1f}/100")
        sub = [g for g in gaps if g.status == "sub-representado"][:5]
        print(f"  Top 5 sub-representados:")
        for g in sub:
            print(f"    {g.resumo()}")

    print()
    print("BLOQUEADOS POR REELEIÇÃO/MÉRITO:")
    for r in bloqueados:
        print(f"  🚫 {r.nome}: {r.motivo_bloqueio[:70]}")

    print()
    print("=" * 75)
    print("AVISO: Scores são OPINIÃO até triangulação com fonte externa.")
    print("O sistema de medição é REAL. Os dados atribuídos são HIPOTÉTICOS.")
    print("=" * 75)


if __name__ == "__main__":
    _demo()
