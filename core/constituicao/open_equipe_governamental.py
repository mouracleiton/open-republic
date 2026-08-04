#!/usr/bin/env python3
"""
OpenEquipeGovernamental -- Alinhamento Capacidade x Necessidade
=================================================================
"Pega quem ja fez e coloca onde precisa ser feito."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


class NivelUrgencia(Enum):
    EMERGENCIA = "EMERGENCIA"       # vidas em risco AGORA
    ALTA = "ALTA"                   # afeta milhoes
    MEDIA = "MEDIA"                 # estrutural
    MONITORAR = "MONITORAR"         # nao critico agora


@dataclass
class DominioRaioX:
    """Um dos 18 dominios do Raio X do Brasil."""
    id: str
    nome: str
    urgencia: NivelUrgencia
    gap_pct: float                  # % da necessidade nao coberta
    indicador_chave: str            # ex: "33M passando fome"
    custo_anual: str                # ex: "R$ 12 bi/ano"


@dataclass
class MatchEquipe:
    """Um politico alinhado a um dominio."""
    nome: str
    partido: str
    uf: str
    cargo: str
    score_capacidade: float
    alinhamento: float              # 0-1: o que fez resolve esse problema?
    score_alinhado: float           # score_capacidade * alinhamento
    feito: str                      # o que JA FEZ
    papel_na_equipe: str            # lider, executor, fiscal, sensor
    veredito: str


DOMINIOS_RAIOX = [
    DominioRaioX("violencia", "Violencia e Seguranca Publica", NivelUrgencia.EMERGENCIA, 95, "47.5 mil homicidios/ano", "R$ 100 bi/ano"),
    DominioRaioX("saude", "Saude Publica", NivelUrgencia.EMERGENCIA, 80, "Fila SUS, Dengue 6M casos", "R$ 230 bi/ano"),
    DominioRaioX("alimentacao", "Seguranca Alimentar", NivelUrgencia.EMERGENCIA, 70, "33M passando fome", "R$ 50 bi/ano"),
    DominioRaioX("agua", "Agua e Sede", NivelUrgencia.EMERGENCIA, 60, "35M sem agua potavel", "R$ 30 bi/ano"),
    DominioRaioX("educacao", "Educacao", NivelUrgencia.ALTA, 75, "PISA 377, 7.2M analfabetos func.", "R$ 150 bi/ano"),
    DominioRaioX("emprego", "Emprego e Renda", NivelUrgencia.ALTA, 65, "Desemprego 7.9%, informalidade 40%", "R$ 80 bi/ano"),
    DominioRaioX("inflacao", "Inflacao e Economia", NivelUrgencia.ALTA, 50, "Juros 10.75%, divida R$ 8T", "R$ 800 bi/ano"),
    DominioRaioX("energia", "Energia", NivelUrgencia.MEDIA, 40, "Acesso 99% mas custo alto", "R$ 60 bi/ano"),
    DominioRaioX("transporte", "Transporte e Mobilidade", NivelUrgencia.MEDIA, 55, "Frota velha, transito mata 30/dia", "R$ 40 bi/ano"),
    DominioRaioX("habitacao", "Habitacao", NivelUrgencia.MEDIA, 50, "8M sem moradia digna", "R$ 35 bi/ano"),
    DominioRaioX("ambiente", "Meio Ambiente", NivelUrgencia.MEDIA, 45, "Desmatamento 13.235 km2/ano", "R$ 10 bi/ano"),
    DominioRaioX("saneamento", "Saneamento", NivelUrgencia.MEDIA, 65, "100M sem coleta esgoto", "R$ 25 bi/ano"),
    DominioRaioX("agropecuaria", "Agropecuaria", NivelUrgencia.MEDIA, 35, "Concentracao terra Gini 0.85", "R$ 15 bi/ano"),
    DominioRaioX("indigena", "Povos Originarios", NivelUrgencia.MEDIA, 80, "305 etnias, 274 mil Yanomami em crise", "R$ 5 bi/ano"),
    DominioRaioX("drogas", "Politica de Drogas", NivelUrgencia.MEDIA, 70, "17% dependentes sem tratamento", "R$ 8 bi/ano"),
    DominioRaioX("cultura", "Cultura", NivelUrgencia.MONITORAR, 60, "Sem Ministerio efetivo historico", "R$ 3 bi/ano"),
    DominioRaioX("comunicacao", "Comunicacao", NivelUrgencia.MONITORAR, 55, "Concentracao de midia", "R$ 2 bi/ano"),
    DominioRaioX("seguranca_alimentar", "Soberania Alimentar", NivelUrgencia.EMERGENCIA, 65, "Brasil importa 80% do trigo", "R$ 20 bi/ano"),
]


# ============================================================
# A EQUIPE (quem ja fez + quem precisa ser feito)
# ============================================================

def _init_matches() -> List[MatchEquipe]:
    return [

        # === EMERGENCIA: ALIMENTACAO ===
        MatchEquipe("Marina Silva", "REDE", "SP", "senadora", 4.11, 0.9, 3.70,
            "Criou PAA (Compra da Agricultura Familiar), CONSEA, VIGISAN. R$ 1bi+ para agricultura familiar.",
            "Lider seguranca alimentar", "APROVADO"),

        # === EMERGENCIA: AGUA ===
        MatchEquipe("Marina Silva", "REDE", "SP", "senadora", 4.11, 0.9, 3.70,
            "Criou Programa Cisternas: 1M+ familias no semi-arido.",
            "Lider agua e seca", "APROVADO"),

        # === MEDIA: AMBIENTE ===
        MatchEquipe("Marina Silva", "REDE", "SP", "senadora", 4.11, 1.0, 4.11,
            "Reduziu desmatamento 80% (2004-2012). PPCDAm.",
            "Lider meio ambiente", "APROVADO"),

        # === ALTA: EDUCACAO ===
        MatchEquipe("Camilo Santana", "PT", "CE", "senador", 4.72, 0.9, 4.25,
            "Governador CE: IDEB subiu, universidade estadual expandiu, vacinacao 95%.",
            "Lider educacao", "APROVADO"),

        # === MEDIA: INDIGENA ===
        MatchEquipe("Sonia Guajajara", "PSOL", "SP", "deputada", 2.92, 1.0, 2.92,
            "Criou Ministerio dos Povos Originarios. Lider APIB.",
            "Lider indigena", "WO (capacidade)"),

        # === EMERGENCIA: VIOLENCIA ===
        MatchEquipe("Flavio Dino", "PSB", "MA", "senador", 4.14, 0.8, 3.31,
            "Governador MA: reduziu homicidios. Ministro Justica.",
            "Executor violencia", "WO (alinhado)"),

        # === EMERGENCIA: SAUDE ===
        MatchEquipe("Camilo Santana", "PT", "CE", "senador", 4.72, 0.7, 3.30,
            "CE: vacinacao 95%. Expandiu cobertura basica.",
            "Executor saude", "WO (alinhado)"),

        MatchEquipe("Otto Alencar", "PSD", "BA", "senador", 3.46, 0.6, 2.08,
            "Medico. Prefeito Feira de Santana. Senador BA.",
            "Tecnico saude", "WO"),

        MatchEquipe("Humberto Costa", "PT", "PE", "senador", 3.38, 0.5, 1.69,
            "Ministro Saude (Lula). Prefeito Recife.",
            "Tecnico saude", "WO"),

        # === ALTA: INFLACAO/ECONOMIA ===
        # (Andre Lara Resende nao e politico em exercicio, mas e referencia)
        MatchEquipe("Jaques Wagner", "PT", "BA", "senador", 3.87, 0.3, 1.16,
            "Governador BA. Ministro Casa Civil. Gestao orçamentária.",
            "Gestao economica", "WO"),

        # === ALTA: EMPREGO ===
        MatchEquipe("Paulo Paim", "PT", "RS", "senador", 3.17, 0.4, 1.27,
            "Senador RS 5x. Sindicalista. Coerencia 30 anos direitos trabalhistas.",
            "Lider trabalhador", "WO"),

        # === MEDIA: HABITACAO ===
        MatchEquipe("Benedita da Silva", "PT", "RJ", "deputada", 3.04, 0.3, 0.91,
            "Governadora RJ. Ministra. Habitacao popular.",
            "Lider habitacao", "WO"),

        MatchEquipe("Patrus Ananias", "PT", "MG", "deputada", 3.29, 0.4, 1.32,
            "Ministro Cidades. Programa Minha Casa Minha Vida.",
            "Executor habitacao", "WO"),

        # === MEDIA: AMBIENTE (BACKUP) ===
        MatchEquipe("Randolfe Rodrigues", "PT", "AP", "senador", 2.62, 0.6, 1.57,
            "Senador AP. Ambientalista. Defesa Amazonia.",
            "Executor ambiente", "WO"),

        # === MEDIA: EDUCACAO (BACKUP) ===
        MatchEquipe("Flavio Arns", "PSB", "PR", "senador", 2.96, 0.6, 1.78,
            "Educador. Ex-prefeito Curitiba. Senador PR.",
            "Tecnico educacao", "WO"),

        MatchEquipe("Tabata Amaral", "PSB", "SP", "deputada", 2.67, 0.5, 1.34,
            "Deputada. Cientista. Protgonismo educacao.",
            "Voz educacao", "WO"),

        # === MEDIA: CULTURA ===
        MatchEquipe("Luiza Erundina", "PSOL", "SP", "deputada", 3.13, 0.3, 0.94,
            "Prefeita SP. Coerencia 30 anos.",
            "Lider cultura", "WO"),

        # === MEDIA: ENERGIA ===
        MatchEquipe("Fernando Coelho Filho", "UNIAO", "PE", "deputado", 2.83, 0.4, 1.13,
            "Ministro Minas/Energia.",
            "Tecnico energia", "WO"),

        # === MEDIA: TRANSPORTE ===
        MatchEquipe("Beto Richa", "PSDB", "PR", "deputado", 3.17, 0.3, 0.95,
            "Governador PR 2x. Concessoes rodovias.",
            "Executor transporte", "WO"),

        # === MEDIA: SANEAMENTO ===
        MatchEquipe("Patrus Ananias", "PT", "MG", "deputada", 3.29, 0.3, 0.99,
            "Ministro Cidades. Saneamento.",
            "Executor saneamento", "WO"),

        # === MEDIA: AGROPECUARIA ===
        MatchEquipe("Tereza Cristina", "PP", "MS", "senadora", 3.38, 0.6, 2.03,
            "Ministra Agricultura. Agro.",
            "Lider agropecuaria", "WO"),

        # === MONITORAR: COMUNICACAO ===
        MatchEquipe("Jandira Feghali", "PCdoB", "RJ", "deputada", 3.00, 0.3, 0.90,
            "Medica. Coerencia. Comunicação política.",
            "Voz comunicacao", "WO"),
    ]


class EquipeGovernamental:
    """
    Cruza quem ja fez com quem precisa ser feito.
    """

    def __init__(self):
        self.dominios = DOMINIOS_RAIOX
        self.matches = _init_matches()

    def equipe_por_dominio(self) -> Dict[str, List[MatchEquipe]]:
        """Para cada dominio, lista os politicos alinhados ordenados por score."""
        resultado = defaultdict(list)
        for m in self.matches:
            # Um match pode cobrir multiplos dominios
            for dom in self.dominios:
                if self._match_cobre_dominio(m, dom):
                    resultado[dom.id].append(m)

        # Ordenar por score_alinhado
        for dom_id in resultado:
            resultado[dom_id].sort(key=lambda m: m.score_alinhado, reverse=True)

        return resultado

    def _match_cobre_dominio(self, m: MatchEquipe, dom: DominioRaioX) -> bool:
        """Verifica se o papel do match cobre o dominio."""
        papel_lower = m.papel_na_equipe.lower()
        dom_id = dom.id.lower()
        dom_nome = dom.nome.lower()

        keywords = {
            "violencia": ["violencia", "seguranca"],
            "saude": ["saude"],
            "alimentacao": ["alimentar", "alimentacao"],
            "agua": ["agua", "seca"],
            "educacao": ["educacao"],
            "emprego": ["emprego", "trabalhador"],
            "inflacao": ["econom", "economia"],
            "energia": ["energia"],
            "transporte": ["transporte"],
            "habitacao": ["habitacao", "moradia"],
            "ambiente": ["ambiente"],
            "saneamento": ["saneamento"],
            "agropecuaria": ["agro", "agropecuaria"],
            "indigena": ["indigena"],
            "drogas": ["drogas"],
            "cultura": ["cultura"],
            "comunicacao": ["comunicacao"],
            "seguranca_alimentar": ["seguranca alimentar"],
        }

        for kw in keywords.get(dom_id, []):
            if kw in papel_lower:
                return True
        return False

    def scorecard(self) -> Dict[str, Any]:
        n_dominios = len(self.dominios)
        equipe_por_dom = self.equipe_por_dominio()
        n_cobertos = sum(1 for dom in self.dominios if equipe_por_dom.get(dom.id))
        n_emergencia = sum(1 for dom in self.dominios if dom.urgencia == NivelUrgencia.EMERGENCIA)
        emergencia_cobertos = sum(1 for dom in self.dominios
                                  if dom.urgencia == NivelUrgencia.EMERGENCIA
                                  and any(m.score_alinhado >= 3.0
                                          for m in equipe_por_dom.get(dom.id, [])))
        return {
            "modulo": "open_equipe_governamental",
            "versao": "0.1.0-spec",
            "dominios_raio_x": n_dominios,
            "dominios_com_equipe": n_cobertos,
            "dominios_sem_equipe": n_dominios - n_cobertos,
            "emergencias": n_emergencia,
            "emergencias_cobertas": emergencia_cobertos,
            "matches": len(self.matches),
            "principio": "Pega quem ja fez. Coloca onde precisa ser feito.",
        }

    def to_dict(self) -> List[Dict[str, Any]]:
        return [{
            "nome": m.nome, "partido": m.partido, "uf": m.uf, "cargo": m.cargo,
            "score": m.score_capacidade, "alinhamento": m.alinhamento,
            "score_alinhado": m.score_alinhado, "feito": m.feito,
            "papel": m.papel_na_equipe, "veredito": m.veredito,
        } for m in self.matches]


def _demo():
    eq = EquipeGovernamental()
    sc = eq.scorecard()
    equipe_dom = eq.equipe_por_dominio()

    print("=" * 80)
    print("EQUIPE GOVERNAMENTAL -- Quem ja fez x Quem precisa ser feito")
    print("=" * 80)

    print(f"\n{sc['dominios_raio_x']} dominios do Raio X")
    print(f"{sc['dominios_com_equipe']} com gente alinhada")
    print(f"{sc['dominios_sem_equipe']} SEM ninguem")
    print(f"{sc['emergencias']} emergencias, {sc['emergencias_cobertas']} cobertas")

    # EMERGENCIAS PRIMEIRO
    print(f"\n{'='*80}")
    print("EMERGENCIAS (vidas em risco AGORA)")
    print(f"{'='*80}")
    for dom in eq.dominios:
        if dom.urgencia == NivelUrgencia.EMERGENCIA:
            print(f"\n  *** {dom.nome.upper()} ***")
            print(f"      GAP: {dom.gap_pct}% | {dom.indicador_chave} | {dom.custo_anual}")
            matches = equipe_dom.get(dom.id, [])
            if matches:
                for m in matches[:3]:
                    flag = " <-- APROVADO" if m.score_alinhado >= 4.0 else ""
                    print(f"      -> {m.nome:<25} {m.partido:<8} score={m.score_capacidade:.2f} alinh={m.alinhamento:.1f} total={m.score_alinhado:.2f}{flag}")
                    print(f"         FEZ: {m.feito[:60]}")
            else:
                print(f"      -> SEM PESSOA ALINHADA. WO.")

    # ALTA
    print(f"\n{'='*80}")
    print("ALTA URGENCIA")
    print(f"{'='*80}")
    for dom in eq.dominios:
        if dom.urgencia == NivelUrgencia.ALTA:
            print(f"\n  {dom.nome}")
            print(f"      GAP: {dom.gap_pct}% | {dom.indicador_chave}")
            matches = equipe_dom.get(dom.id, [])
            if matches:
                for m in matches[:3]:
                    flag = " <-- APROVADO" if m.score_alinhado >= 4.0 else ""
                    print(f"      -> {m.nome:<25} {m.partido:<8} score={m.score_capacidade:.2f} alinh={m.alinhamento:.1f} total={m.score_alinhado:.2f}{flag}")
            else:
                print(f"      -> SEM PESSOA ALINHADA. WO.")

    # MEDIA + MONITORAR
    print(f"\n{'='*80}")
    print("MEDIA E MONITORAR")
    print(f"{'='*80}")
    for dom in eq.dominios:
        if dom.urgencia in (NivelUrgencia.MEDIA, NivelUrgencia.MONITORAR):
            print(f"\n  {dom.nome} [{dom.urgencia.value}]")
            print(f"      GAP: {dom.gap_pct}% | {dom.indicador_chave}")
            matches = equipe_dom.get(dom.id, [])
            if matches:
                for m in matches[:2]:
                    flag = " <-- APROVADO" if m.score_alinhado >= 4.0 else ""
                    print(f"      -> {m.nome:<25} score={m.score_capacidade:.2f} total={m.score_alinhado:.2f}{flag}")
            else:
                print(f"      -> SEM PESSOA. WO.")

    # VEREDITO
    print(f"\n{'='*80}")
    print("VEREDITO")
    print(f"{'='*80}")
    n_aprov = sum(1 for m in eq.matches if m.score_alinhado >= 4.0)
    n_wo = len(eq.matches) - n_aprov
    print(f"  {n_aprov} matches APROVADOS (>=4.0)")
    print(f"  {n_wo} matches WO (<4.0)")
    print(f"\n  EQUIPE MINIMA VIÁVEL:")
    for m in eq.matches:
        if m.score_alinhado >= 4.0:
            print(f"    {m.nome:<25} -> {m.papel_na_equipe} (score={m.score_alinhado:.2f})")
    print(f"\n  LACUNAS CRITICAS (emergencia sem ninguem >=4.0):")
    for dom in eq.dominios:
        if dom.urgencia == NivelUrgencia.EMERGENCIA:
            matches = equipe_dom.get(dom.id, [])
            if not any(m.score_alinhado >= 4.0 for m in matches):
                print(f"    *** {dom.nome.upper()} ***")


if __name__ == "__main__":
    _demo()
