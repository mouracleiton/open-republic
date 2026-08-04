#!/usr/bin/env python3
"""
OpenPropostaValidacao -- Propostas de Pre-Candidatos vs Gate WO + Epistemologico
=================================================================================
"Cada proposta passa por 7 criterios. Nao passou = W.O."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


class StatusGate(Enum):
    APROVADO = "APROVADO"       # passou nos 7 criterios
    JEQUERI = "JEQUERI"         # passou nos 5 criticos, falhou nos 2 jequeri
    WO = "W.O."                 # nao passou nos criticos


class ClassificacaoEpistemica(Enum):
    FATO = "FATO"               # 7/7 criterios cientificos
    DADO = "DADO"               # tem dados mas nao triangulado
    OPINIAO = "OPINIAO"         # so discurso, sem dado verificavel


@dataclass
class Proposta:
    """Uma proposta de um pre-candidato."""
    candidato: str
    partido: str
    area: str                   # qual dominio do Raio X
    titulo: str

    # 5 criterios CRITICOS (Gate WO)
    tem_como: bool              # diz COMO vai fazer?
    tem_quem: bool              # diz QUEM vai executar?
    tem_custo: bool             # diz QUANTO CUSTA?
    tem_prazo: bool             # diz QUANDO entrega?
    tem_metrica: bool           # diz COMO VAI MEDIR resultado?

    # 2 criterios JEQUERI
    tem_fonte_dados: bool       # de onde tirou os dados que fundamentam?
    tem_diagnostico: bool       # baseado em que diagnostico?

    # Classificacao epistemica
    classificacao: ClassificacaoEpistemica

    # Texto real da proposta (resumo)
    texto_resumido: str = ""

    @property
    def n_criticos(self) -> int:
        return sum([self.tem_como, self.tem_quem, self.tem_custo,
                    self.tem_prazo, self.tem_metrica])

    @property
    def n_total(self) -> int:
        return sum([self.tem_como, self.tem_quem, self.tem_custo,
                    self.tem_prazo, self.tem_metrica,
                    self.tem_fonte_dados, self.tem_diagnostico])

    @property
    def status_gate(self) -> StatusGate:
        if self.n_criticos == 5 and self.n_total == 7:
            return StatusGate.APROVADO
        elif self.n_criticos == 5:
            return StatusGate.JEQUERI
        else:
            return StatusGate.WO

    @property
    def veredito_texto(self) -> str:
        s = self.status_gate
        if s == StatusGate.APROVADO:
            return f"APROVADO ({self.n_total}/7)"
        elif s == StatusGate.JEQUERI:
            return f"JEQUERI ({self.n_total}/7, criticos ok)"
        else:
            return f"W.O. ({self.n_criticos}/5 criticos)"


def _init_propostas() -> List[Proposta]:
    return [

        # ================================================================
        # LULA (PT)
        # ================================================================
        Proposta("Lula", "PT", "alimentacao", "Fome Zero + Bolsa Familia",
            tem_como=True, tem_quem=True, tem_custo=True, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.FATO,
            texto_resumido="Ampliar BF para R$700+, criar Brasil Sem Fome, guarnicoes. Custo R$170bi/ano."),

        Proposta("Lula", "PT", "saude", "Mais SUS + Mais Medicamentos",
            tem_como=True, tem_quem=True, tem_custo=False, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.DADO,
            texto_resumido="Ampliar SUS, farmacia popular. Sem custo detalhado."),

        Proposta("Lula", "PT", "educacao", "Mais Educacao + ProUni+",
            tem_como=True, tem_quem=True, tem_custo=False, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.DADO,
            texto_resumido="Ampliar universidades, PROUNI. Sem custo detalhado."),

        Proposta("Lula", "PT", "inflacao", "Reforma Tributaria",
            tem_como=True, tem_quem=True, tem_custo=True, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.FATO,
            texto_resumido="IVA dual, CBS+IBS. Aprovado em 2023."),

        Proposta("Lula", "PT", "violencia", "Mais Seguranca Publica",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=False,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Discurso generico sobre seguranca. Sem COMO, SEM QUEM, SEM CUSTO."),

        # ================================================================
        # MARINA SILVA (REDE)
        # ================================================================
        Proposta("Marina Silva", "REDE", "ambiente", "Desmatamento Zero",
            tem_como=True, tem_quem=True, tem_custo=True, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.FATO,
            texto_resumido="PPCDAm, comando unificado, fiscalizacao por satelite. Fez antes: -80%."),

        Proposta("Marina Silva", "REDE", "agua", "Cisternas para 1M familias",
            tem_como=True, tem_quem=True, tem_custo=True, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.FATO,
            texto_resumido="Programa ja existe. Cisterna R$3k cada. Meta 1M familias. R$3bi."),

        Proposta("Marina Silva", "REDE", "alimentacao", "PAA + CONSEA + VIGISAN",
            tem_como=True, tem_quem=True, tem_custo=True, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.FATO,
            texto_resumido="Compra da agricultura familiar. CONSEA reativado. VIGISAN."),

        Proposta("Marina Silva", "REDE", "violencia", "Seguranca com inteligencia",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=False,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Discurso sobre reducao de violencia. Sem detalhamento."),

        Proposta("Marina Silva", "REDE", "drogas", "Guerra as Drogas Falhou",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Diagnostico correto mas sem proposta executavel."),

        # ================================================================
        # JONES MANOEL (PCB)
        # ================================================================
        Proposta("Jones Manoel", "PCB", "inflacao", "Nacionalizar bancos e empresas estrategicas",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Nacionalizar Itaun, Bradesco, Vale. Sem COMO, sem QUANTO, sem PRAZO."),

        Proposta("Jones Manoel", "PCB", "emprego", "Emprego para todos via Estado",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Estado garante emprego. Sem mecanismo, sem custo, sem prazo."),

        Proposta("Jones Manoel", "PCB", "habitacao", "Moradia como direito",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Expropriar imoveis ociosos. Sem mecanismo legal, sem custo."),

        Proposta("Jones Manoel", "PCB", "violencia", "Policia para o povo",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Extincao das policias militares. Sem plano de transicao."),

        Proposta("Jones Manoel", "PCB", "saude", "SUS universal e gratuito",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="SUS ampliado. Sem financiamento, sem mecanismo."),

        # ================================================================
        # CIRO GOMES (PDT)
        # ================================================================
        Proposta("Ciro Gomes", "PDT", "inflacao", "Reordenar arcabouco fiscal",
            tem_como=True, tem_quem=True, tem_custo=True, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.DADO,
            texto_resumido="Simplificar tributos, reduzir juros. Tem plano mas dados sao parciais."),

        Proposta("Ciro Gomes", "PDT", "energia", "Transposicao Sao Francisco",
            tem_como=True, tem_quem=True, tem_custo=True, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.FATO,
            texto_resumido="Ja executou como ministro. 600km de canais."),

        Proposta("Ciro Gomes", "PDT", "violencia", "Seguranca com inteligencia",
            tem_como=True, tem_quem=True, tem_custo=False, tem_prazo=True, tem_metrica=True,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.DADO,
            texto_resumido="Pacto federativo, inteligencia. Sem custo detalhado."),

        # ================================================================
        # EDMILSON COSTA (PCB)
        # ================================================================
        Proposta("Edmilson Costa", "PCB", "inflacao", "Socializar meios de producao",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Controle operario dos meios de producao. Sem mecanismo executavel."),

        Proposta("Edmilson Costa", "PCB", "emprego", "Plano economico centralizado",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Plano quinquenal estilo sovietico. Sem dados brasileiros."),

        # ================================================================
        # SAMARA MARTINS (UP)
        # ================================================================
        Proposta("Samara Martins", "UP", "habitacao", "Moradia popular urgente",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Ocupar imoveis ociosos. Sem mecanismo legal, sem custo."),

        Proposta("Samara Martins", "UP", "saude", "SUS para o povo",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=True, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="SUS ampliado. Sem detalhamento."),

        # ================================================================
        # HERTZ DIAS (PSTU)
        # ================================================================
        Proposta("Hertz Dias", "PSTU", "emprego", "Greve geral revolucionaria",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Revolucao socialista. Sem proposta de governo executavel."),

        # ================================================================
        # RUI COSTA PIMENTA (PCO)
        # ================================================================
        Proposta("Rui Costa Pimenta", "PCO", "inflacao", "Abolir capitalismo",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao=ClassificacaoEpistemica.OPINIAO,
            texto_resumido="Fim do capitalismo. Sem mecanismo, sem transicao, sem custo."),
    ]


class PropostaValidacao:
    """
    Valida propostas pelo Gate WO e Epistemologico.
    """

    def __init__(self):
        self.propostas = _init_propostas()

    def por_candidato(self) -> Dict[str, List[Proposta]]:
        resultado = defaultdict(list)
        for p in self.propostas:
            resultado[p.candidato].append(p)
        return dict(resultado)

    def scorecard_candidato(self, nome: str) -> Dict[str, Any]:
        props = [p for p in self.propostas if p.candidato == nome]
        if not props:
            return {"candidato": nome, "n_propostas": 0, "veredito": "SEM PROPOSTAS"}

        aprovadas = sum(1 for p in props if p.status_gate == StatusGate.APROVADO)
        jequeri = sum(1 for p in props if p.status_gate == StatusGate.JEQUERI)
        wo = sum(1 for p in props if p.status_gate == StatusGate.WO)
        fato = sum(1 for p in props if p.classificacao == ClassificacaoEpistemica.FATO)
        dado = sum(1 for p in props if p.classificacao == ClassificacaoEpistemica.DADO)
        opiniao = sum(1 for p in props if p.classificacao == ClassificacaoEpistemica.OPINIAO)

        pct_aprovado = aprovadas / len(props) * 100 if props else 0

        return {
            "candidato": nome,
            "partido": props[0].partido,
            "n_propostas": len(props),
            "aprovadas": aprovadas,
            "jequeri": jequeri,
            "wo": wo,
            "fato": fato,
            "dado": dado,
            "opiniao": opiniao,
            "pct_aprovado": round(pct_aprovado, 1),
            "score_propostas": round(pct_aprovado / 20, 2),  # 0-5
            "veredito": "APROVADO" if pct_aprovado >= 80 else ("JEQUERI" if pct_aprovado >= 40 else "W.O."),
        }

    def ranking_candidatos(self) -> List[Dict[str, Any]]:
        nomes = sorted(set(p.candidato for p in self.propostas))
        scores = [self.scorecard_candidato(n) for n in nomes]
        return sorted(scores, key=lambda x: x["score_propostas"], reverse=True)

    def areas_sem_proposta_aprovada(self) -> List[str]:
        """Dominios do Raio X sem nenhuma proposta APROVADA."""
        todas_areas = {
            "violencia", "saude", "alimentacao", "agua", "saneamento",
            "educacao", "emprego", "inflacao", "agropecuaria", "energia",
            "transporte", "habitacao", "comunicacao", "ambiente",
            "indigena", "drogas", "cultura", "seguranca_alimentar",
        }
        areas_aprovadas = {p.area for p in self.propostas if p.status_gate == StatusGate.APROVADO}
        return sorted(todas_areas - areas_aprovadas)

    def scorecard(self) -> Dict[str, Any]:
        nomes = sorted(set(p.candidato for p in self.propostas))
        return {
            "modulo": "open_proposta_validacao",
            "versao": "0.1.0-spec",
            "candidatos": len(nomes),
            "propostas_total": len(self.propostas),
            "criterios_gate": 7,
            "corte_gate": "5 criticos = APROVADO. <5 = W.O.",
        }


def _demo():
    pv = PropostaValidacao()
    sc = pv.scorecard()
    ranking = pv.ranking_candidatos()
    por_cand = pv.por_candidato()
    lacunas = pv.areas_sem_proposta_aprovada()

    print("=" * 85)
    print("PROPOSTAS DOS PRE-CANDIDATOS vs GATE WO + EPISTEMOLOGICO")
    print("=" * 85)

    print(f"\n{sc['candidatos']} candidatos | {sc['propostas_total']} propostas | {sc['criterios_gate']} criterios")

    for cand_data in ranking:
        nome = cand_data["candidato"]
        print(f"\n{'='*85}")
        print(f"CANDIDATO: {nome} ({cand_data['partido']})")
        print(f"{'='*85}")
        print(f"  Propostas: {cand_data['n_propostas']}")
        print(f"  APROVADAS: {cand_data['aprovadas']} | JEQUERI: {cand_data['jequeri']} | W.O.: {cand_data['wo']}")
        print(f"  FATO: {cand_data['fato']} | DADO: {cand_data['dado']} | OPINIAO: {cand_data['opiniao']}")
        print(f"  Score propostas: {cand_data['score_propostas']}/5.0")
        print(f"  VEREDITO: {cand_data['veredito']}")

        props = por_cand.get(nome, [])
        for p in props:
            flag = ""
            if p.status_gate == StatusGate.APROVADO:
                flag = " *** APROVADO"
            elif p.status_gate == StatusGate.WO:
                flag = " *** W.O."
            print(f"\n  [{p.area.upper()}] {p.titulo}")
            print(f"    Gate: {p.veredito_texto}{flag}")
            print(f"    Epistemologia: {p.classificacao.value}")
            print(f"    Como={p.tem_como} Quem={p.tem_quem} Custo={p.tem_custo} Prazo={p.tem_prazo} Metrica={p.tem_metrica}")
            print(f"    Texto: {p.texto_resumido[:70]}")

    print(f"\n{'='*85}")
    print(f"DOMINIOS DO RAIO X SEM PROPOSTA APROVADA: {len(lacunas)}")
    print(f"{'='*85}")
    for a in lacunas:
        print(f"  *** {a.upper()}")

    print(f"\n{'='*85}")
    print("VEREDITO GERAL")
    print(f"{'='*85}")
    for c in ranking:
        print(f"  {c['candidato']:<25} {c['partido']:<6} propostas={c['n_propostas']} aprovadas={c['aprovadas']} score={c['score_propostas']}/5.0 [{c['veredito']}]")


if __name__ == "__main__":
    _demo()
