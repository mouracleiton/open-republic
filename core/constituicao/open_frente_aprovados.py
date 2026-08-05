#!/usr/bin/env python3
"""
OpenFrenteAprovados -- Lista de Aprovados pela Frente Unificada Comunista
============================================================================
"Frente não aprova por afinidade. Aprova por score >= 4.0.
 Passou no Gate, é da frente. Não passou, não é."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional
from collections import defaultdict


class Cargo(Enum):
    PRESIDENTE = "Presidente"
    VICE = "Vice-Presidente"
    SENADOR = "Senador"
    DEP_FEDERAL = "Deputado Federal"
    GOVERNADOR = "Governador"
    DEP_ESTADUAL = "Deputado Estadual"
    MINISTRO = "Ministro"
    SEM_CARGO = "Sem cargo (candidato)"


class StatusAprovacao(Enum):
    APROVADO = "APROVADO"          # score >= 4.0
    REJEITADO = "REJEITADO"        # score < 4.0
    EM_ANALISE = "EM_ANALISE"      # sem score, aguardando Gate


@dataclass
class PoliticoAprovado:
    """Um político avaliado pela frente unificada."""
    nome: str
    cargo: Cargo
    partido: str                    # sigla (histórico, não identidade)
    estado: str
    score: float                    # 0-5.0
    status: StatusAprovacao
    area_alinhamento: str           # qual eixo do Raio X
    evidencia: str                  # o que FEZ (não o que prometeu)
    fonte: str                      # de onde veio o score
    restricoes: str = ""            # limitações (se houver)


def _init_aprovados() -> List[PoliticoAprovado]:
    """
    Lista de políticos com score >= 4.0.
    PT foi reintegrado: score >= 4.0 e o único critério.

    AVISO: TODOS os scores sao OPINIAO (0.5/7 no Gate Epistemológico).
    A composicao final so e definida apos triangulacao de fontes.
    """
    return [
        # === PRESIDENCIA ===
        PoliticoAprovado("Dilma Rousseff", Cargo.PRESIDENTE, "PT", "BR",
            4.50, StatusAprovacao.APROVADO, "gestao_executiva",
            "Presidente 2011-2016. Minas/Energia, Casa Civil. PAC. Deposta em golpe sem crime.",
            "open_candidato_score.py (MOCK/OPINIAO)",
            "Voto de minerva. Duplo comando com vice."),

        PoliticoAprovado("Jones Manoel", Cargo.VICE, "PCB", "SP",
            2.50, StatusAprovacao.EM_ANALISE, "comunicacao",
            "Canal ~2M. 10 anos coerência. Comunicação política.",
            "open_candidato_score.py (MOCK/OPINIAO)",
            "Score < 4.0. VICE por habilidade de comunicação, não score."),

        # === SENADORES (score >= 4.0) ===
        PoliticoAprovado("Camilo Santana", Cargo.SENADOR, "PT", "CE",
            4.72, StatusAprovacao.APROVADO, "educacao",
            "Governador CE 2x. IDEB subiu. Vacinação 95%. Pós-graduação UP.",
            "open_senador_score.py (MOCK/OPINIAO)",
            "PT reintegrado. Score >= 4.0."),

        PoliticoAprovado("Flavio Dino", Cargo.SENADOR, "PSB", "MA",
            4.14, StatusAprovacao.APROVADO, "violencia",
            "Governador MA. Reduziu homicídios. Ministro Justiça. STF.",
            "open_senador_score.py (MOCK/OPINIAO)"),

        # === DEPUTADOS FEDERAIS (score >= 4.0) ===
        PoliticoAprovado("Marina Silva", Cargo.DEP_FEDERAL, "REDE", "SP",
            4.11, StatusAprovacao.APROVADO, "ambiente",
            "Ministra. -80% desmatamento (2004-2012). Cisternas 1M+. PAA R$1bi+.",
            "open_politico_score.py (MOCK/OPINIAO)"),

        # === MINISTROS/SECRETARIAS (MOCK, score baseado em habilidade) ===
        PoliticoAprovado("Samara Martins", Cargo.MINISTRO, "UP", "SP",
            1.50, StatusAprovacao.EM_ANALISE, "alimentacao",
            "Programa de 25 pontos. Diagnóstico 100%. Base MTST.",
            "open_candidato_score.py (MOCK/OPINIAO)",
            "Score < 4.0. Entra por programa + diagnóstico, não score."),

        PoliticoAprovado("Orlando Silva", Cargo.MINISTRO, "PCdoB", "SP",
            2.83, StatusAprovacao.EM_ANALISE, "educacao",
            "Ministro Esporte. Professor. Educação popular.",
            "open_candidato_score.py (MOCK/OPINIAO)"),

        PoliticoAprovado("Jandira Feghali", Cargo.MINISTRO, "PCdoB", "RJ",
            3.00, StatusAprovacao.EM_ANALISE, "saude",
            "Médica. Deputada. Saúde pública. Coerência.",
            "open_candidato_score.py (MOCK/OPINIAO)"),

        PoliticoAprovado("Sonia Guajajara", Cargo.MINISTRO, "PSOL", "SP",
            2.67, StatusAprovacao.EM_ANALISE, "indigena",
            "Liderança indígena. APIB. Ministério dos Povos Originários.",
            "open_candidato_score.py (MOCK/OPINIAO)"),

        PoliticoAprovado("Ciro Gomes", Cargo.MINISTRO, "PDT", "CE",
            3.81, StatusAprovacao.EM_ANALISE, "infraestrutura",
            "Governador. Ministro. Transposição. Ferrovias.",
            "open_candidato_score.py (MOCK/OPINIAO)"),

        PoliticoAprovado("Paulo Paim", Cargo.SENADOR, "PT", "RS",
            3.17, StatusAprovacao.EM_ANALISE, "emprego",
            "Senador 5x. Sindicalista. 30 anos direitos trabalhistas.",
            "open_senador_score.py (MOCK/OPINIAO)"),

        PoliticoAprovado("Patrus Ananias", Cargo.MINISTRO, "PT", "MG",
            3.29, StatusAprovacao.EM_ANALISE, "habitacao",
            "Ministro Cidades 2x. MCMV. Saneamento.",
            "open_candidato_score.py (MOCK/OPINIAO)"),

        PoliticoAprovado("Luiza Erundina", Cargo.MINISTRO, "PSB", "SP",
            3.13, StatusAprovacao.EM_ANALISE, "cultura",
            "Prefeita SP. 30 anos coerência. Cultura popular.",
            "open_candidato_score.py (MOCK/OPINIAO)"),

        PoliticoAprovado("Erika Hilton", Cargo.DEP_FEDERAL, "PSOL", "SP",
            1.67, StatusAprovacao.EM_ANALISE, "violencia",
            "Deputada. Vereadora. Primeira transexual eleita.",
            "open_politico_score.py (MOCK/OPINIAO)"),

        # === MINISTERIOS PREENCHIDOS (MOCK) ===
        PoliticoAprovado("Celso Amorim", Cargo.MINISTRO, "—", "DF",
            4.30, StatusAprovacao.APROVADO, "soberania_alimentar",
            "Diplomata. 2x ministro Itamaraty. Comércio Sul-Sul. Negociação Irã.",
            "heuristica (MOCK/OPINIAO)"),

        PoliticoAprovado("Aldo Rebelo", Cargo.MINISTRO, "—", "SP",
            3.50, StatusAprovacao.EM_ANALISE, "violencia",
            "Foi ministro Defesa. Nacionalista. Experiente.",
            "heuristica (MOCK/OPINIAO)"),

        PoliticoAprovado("Ricardo Galvão", Cargo.MINISTRO, "—", "SP",
            4.20, StatusAprovacao.APROVADO, "educacao",
            "Físico. Ex-INPE. Defendeu dados do desmatamento contra Bolsonaro.",
            "heuristica (MOCK/OPINIAO)"),

        PoliticoAprovado("Humberto Costa", Cargo.SENADOR, "PT", "PE",
            3.40, StatusAprovacao.EM_ANALISE, "agua",
            "Senador. Gestão NE. Ex-ministro Saúde.",
            "heuristica (MOCK/OPINIAO)"),

        PoliticoAprovado("Ana Moser", Cargo.MINISTRO, "—", "SP",
            2.50, StatusAprovacao.EM_ANALISE, "violencia",
            "Ex-vôlei. Educação popular pelo esporte.",
            "heuristica (MOCK/OPINIAO)"),

        PoliticoAprovado("Silvio Almeida", Cargo.MINISTRO, "—", "SP",
            4.00, StatusAprovacao.APROVADO, "violencia",
            "Filósofo. Autor 'Racismo Estrutural'. Ministro DH.",
            "heuristica (MOCK/OPINIAO)"),

        PoliticoAprovado("Eduardo Mancuso", Cargo.MINISTRO, "—", "RS",
            2.00, StatusAprovacao.EM_ANALISE, "emprego",
            "Economia solidária. Cooperativismo.",
            "heuristica (MOCK/OPINIAO)"),

        PoliticoAprovado("Bruno Dantas", Cargo.MINISTRO, "—", "DF",
            4.10, StatusAprovacao.APROVADO, "corrupcao",
            "TCU. Auditoria. Combate corrupção.",
            "heuristica (MOCK/OPINIAO)"),

        PoliticoAprovado("João Paulo Lopes", Cargo.MINISTRO, "—", "DF",
            3.50, StatusAprovacao.EM_ANALISE, "corrupcao",
            "Jurista. Direito constitucional popular.",
            "heuristica (MOCK/OPINIAO)"),

        PoliticoAprovado("Marina Silva", Cargo.MINISTRO, "REDE", "AC",
            4.11, StatusAprovacao.APROVADO, "ambiente",
            "Ministra. -80% desmatamento. Cisternas. PAA.",
            "open_politico_score.py (MOCK/OPINIAO)"),

        # === GOVERNADORES (PENDENTE -- preencher por estado) ===
        # 27 vagas. Aguardando analise.
    ]


def _init_criterios() -> List[str]:
    return [
        "1. Score >= 4.0 (Gate WO binário: APROVADO ou REJEITADO)",
        "2. Sem histórico de corrupção (CGU, TCU, MPF)",
        "3. Alinhamento com programa (18 eixos do Raio X)",
        "4. Aceita ser medido pelo Sensor (OpenRepublic)",
        "5. Respeita cotas do povo (genero 50%, raca 56%, classe 40%)",
        "6. Excecao: cargo tecnico pode ter score < 4.0 (EM_ANALISE)",
        "7. PT reintegrado: score >= 4.0 e o unico criterio",
    ]


def scorecard() -> Dict[str, Any]:
    aprovados = _init_aprovados()
    n_aprovados = sum(1 for p in aprovados if p.status == StatusAprovacao.APROVADO)
    n_em_analise = sum(1 for p in aprovados if p.status == StatusAprovacao.EM_ANALISE)
    n_rejeitados = sum(1 for p in aprovados if p.status == StatusAprovacao.REJEITADO)
    score_medio = sum(p.score for p in aprovados if p.status == StatusAprovacao.APROVADO) / n_aprovados if n_aprovados > 0 else 0

    return {
        "modulo": "open_frente_aprovados",
        "versao": "0.1.0-spec",
        "total_avaliados": len(aprovados),
        "aprovados": n_aprovados,
        "em_analise": n_em_analise,
        "rejeitados": n_rejeitados,
        "score_medio_aprovados": round(score_medio, 2),
        "criterio_corte": ">= 4.0",
    }


def _demo():
    aprovados = _init_aprovados()
    criterios = _init_criterios()
    sc = scorecard()

    print("=" * 90)
    print("FRENTE UNIFICADA COMUNISTA — LISTA DE APROVADOS")
    print("OpenRepublic · Sensor Independente")
    print("=" * 90)

    print(f"""
  CRITÉRIO ÚNICO: Score >= 4.0 (Gate WO binário)

  Total avaliados:  {sc['total_avaliados']}
  APROVADOS:        {sc['aprovados']}
  EM ANÁLISE:       {sc['em_analise']}
  REJEITADOS:       {sc['rejeitados']}
  Score médio (aprovados): {sc['score_medio_aprovados']}
""")

    print(f"{'='*90}")
    print("CRITÉRIOS DE APROVAÇÃO")
    print(f"{'='*90}")
    for c in criterios:
        print(f"  {c}")

    # Aprovados
    ap = [p for p in aprovados if p.status == StatusAprovacao.APROVADO]
    print(f"\n{'='*90}")
    print(f"APROVADOS (score >= 4.0): {len(ap)}")
    print(f"{'='*90}")
    for p in sorted(ap, key=lambda x: x.score, reverse=True):
        bar = "#" * int(p.score)
        print(f"""
  [{p.score:.2f}] [{bar}] {p.nome} ({p.cargo.value}, {p.estado})
    PARTIDO: {p.partido}
    ALINHAMENTO: {p.area_alinhamento}
    EVIDÊNCIA: {p.evidencia}
    FONTE: {p.fonte}""")

    # Em analise
    ea = [p for p in aprovados if p.status == StatusAprovacao.EM_ANALISE]
    print(f"\n{'='*90}")
    print(f"EM ANÁLISE (score < 4.0, cargo técnico): {len(ea)}")
    print(f"{'='*90}")
    for p in sorted(ea, key=lambda x: x.score, reverse=True):
        bar = "#" * int(p.score)
        print(f"""
  [{p.score:.2f}] [{bar}] {p.nome} ({p.cargo.value}, {p.estado})
    PARTIDO: {p.partido}
    ALINHAMENTO: {p.area_alinhamento}
    EVIDÊNCIA: {p.evidencia}
    RESTRIÇÃO: {p.restricoes or 'Nenhuma'}""")

    # Por estado
    print(f"\n{'='*90}")
    print("DISTRIBUIÇÃO POR ESTADO")
    print(f"{'='*90}")
    por_estado = defaultdict(int)
    for p in aprovados:
        por_estado[p.estado] += 1
    for estado, n in sorted(por_estado.items()):
        print(f"  {estado}: {n}")

    print(f"\n{'='*90}")
    print("GOVERNADORES: 27 VAGAS PENDENTES")
    print(f"{'='*90}")
    print("""
  0 de 27 governadores definidos.
  Aguardando análise estadual.

  DEPUTADOS ESTADUAIS: ~1.059 vagas
  Aguardando análise por assembleia.

  Para preencher: cada candidato passa pelo Gate WO.
  Score >= 4.0 = APROVADO. < 4.0 = REJEITADO.
""")

    print(f"{'='*90}")
    print("VEREDITO")
    print(f"{'='*90}")
    print(f"""
  {sc['aprovados']} APROVADOS com score >= 4.0.
  {sc['em_analise']} EM ANÁLISE (cargo técnico, score < 4.0).

  A frente não aprova por afinidade. Aprova por score.
  PT reintegrado: quem tem score >= 4.0, entra.
  Quem não tem, não entra -- não importa o partido.

  A lista cresce conforme novos candidatos passam pelo Gate.
  O Sensor mede. A frente aprova. O povo cobra.
""")


if __name__ == "__main__":
    _demo()
