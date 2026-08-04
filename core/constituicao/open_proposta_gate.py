#!/usr/bin/env python3
"""
OpenPropostaGate -- Checklist WO para Propostas de Governo
=============================================================
"Toda proposta que nao responder 7 perguntas com clareza total
 leva WO. Walkover. Desclassificada. Nao passa."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class VereditoWO(Enum):
    APROVADO = "aprovado"        # passou nos 7 criterios
    WO = "wo"                     # walkover -- desclassificado
    EM_JEQUERI = "jequeri"        # quase, pode corrigir

    @property
    def rotulo(self) -> str:
        return {
            "aprovado": "APROVADO -- passou nos 7 criterios",
            "wo": "W.O. -- Walkover, desclassificada",
            "jequeri": "EM JEQUERI -- pode corrigir",
        }[self.value]


@dataclass
class CriterioWO:
    """Um dos 7 criterios que toda proposta deve responder."""
    id: int
    pergunta: str
    explicacao: str
    exemplo_falha: str
    peso: int = 1  # criterios criticos tem peso maior


@dataclass
class RespostaProposta:
    """Resposta de uma proposta a um criterio."""
    criterio_id: int
    respondido: bool
    resposta: str = ""
    problema: str = ""


@dataclass
class PropostaSubmetida:
    """Uma proposta de plano de governo submetida ao gate."""
    nome: str
    respostas: List[RespostaProposta] = field(default_factory=list)

    @property
    def veredito(self) -> VereditoWO:
        if not self.respostas:
            return VereditoWO.WO
        критicos_ok = all(
            r.respondido for r in self.respostas if r.criterio_id <= 5
        )
        todos_ok = all(r.respondido for r in self.respostas)
        if todos_ok:
            return VereditoWO.APROVADO
        if критicos_ok:
            return VereditoWO.EM_JEQUERI
        return VereditoWO.WO

    @property
    def score(self) -> int:
        if not self.respostas:
            return 0
        return sum(1 for r in self.respostas if r.respondido)


class PropostaGate:
    """
    Gate de propostas de governo. 7 criterios inegociaveis.

    REGRA: se faltar UM criterio critico (1-5), WO.
    Se faltar criterio nao-critico (6-7), EM JEQUERI (pode corrigir).
    """

    def __init__(self):
        self.criterios = self._init_criterios()

    def _init_criterios(self) -> List[CriterioWO]:
        return [
            CriterioWO(
                1,
                "COMO sera executado?",
                "A proposta descreve passo-a-passo o que sera feito. Nao 'vamos melhorar' -- sim 'construiremos X cisternas em Y municipios usando Z reais por unidade'.",
                "'Vamos combater a fome' -- COMO? Quantas cestas? Qual distribuicao? Qual logistica? Zero detalhe = WO.",
                peso=3,
            ),
            CriterioWO(
                2,
                "POR QUEM? (responsavel identificado)",
                "Existe um orgao, secretario ou equipe nominada como responsavel. Com nome, cargo e contato publico. Nao 'o governo fara' -- sim 'o Ministerio X, atraves da Secretaria Y, com coordenacao de Z'.",
                "'Seram criadas equipes' -- quais? Quantas pessoas? Quem responde se falhar? Sem dono = WO.",
                peso=3,
            ),
            CriterioWO(
                3,
                "QUANTO CUSTARA? (orcamento detalhado)",
                "Valor total em R$, com breakdown por item. Nao 'investiremos recursos' -- sim 'R$ 50 milhoes sendo R$ 30M em obras, R$ 15M em pessoal, R$ 5M em equipamentos'. Fonte do recurso identificada.",
                "'Vamos investir pesadamente' -- quanto? De onde vem? Imposto? Divida? Corta de onde? Sem numero = WO.",
                peso=3,
            ),
            CriterioWO(
                4,
            "COMO os dados foram manipulados? (transparencia metodologica)",
                "Toda estatistica citada tem fonte identificada, ano, metodologia de coleta e tratamento. Se diz '50% das criancas' -- de onde? Qual pesquisa? Qual amostra? Qual ano? Como foi coletado?",
                "'A maioria dos brasileiros quer...' -- qual pesquisa? Qual instituto? Qual amostra? Qual margem de erro? Dado sem fonte = WO.",
                peso=2,
            ),
            CriterioWO(
                5,
                "QUAL o prazo e marco verificavel?",
                "Data limite explicita com marco mensuravel. Nao 'ate o final do mandato' -- sim '30 mil cisternas instaladas ate dezembro de 2025, verificaveis por GPS e foto'.",
                "'Vamos zerar a fila ate 2026' -- qual fila? Quantas pessoas hoje? Quanto por mes? Sem marco = WO.",
                peso=2,
            ),
            CriterioWO(
                6,
                "QUEM sera afetado (e quem sera prejudicado)?",
                "Identifica beneficiarios E potenciais prejudicados. Toda politica cria vencedor e perdedor. Se nao admite o custo, e desonesta.",
                "'Vamos subsidiar X' -- quem paga o subsidio? Qual setor perde? Qual regiao sai prejudicada? Sem custo = JEQUERI.",
                peso=1,
            ),
            CriterioWO(
                7,
                "COMO sera medido o resultado?",
                "Define qual metrica sera usada para saber se funcionou. Nao 'avaliaremos periodicamente' -- sim 'taxa de mortalidade infantil medida mensalmente por DataSUS, meta: reduzir de X para Y'.",
                "'Vamos melhorar a educacao' -- medido por que? IDEB? PISA? ENEM? Nota de corte? Sem metrica = JEQUERI.",
                peso=1,
            ),
        ]

    def avaliar(self, proposta: PropostaSubmetida) -> Dict[str, Any]:
        veredito = proposta.veredito
        detalhes = []
        for c in self.criterios:
            r = next((r for r in proposta.respostas if r.criterio_id == c.id), None)
            respondido = r.respondido if r else False
            detalhes.append({
                "id": c.id,
                "pergunta": c.pergunta,
                "respondido": respondido,
                "critico": c.id <= 5,
                "peso": c.peso,
                "problema": r.problema if r else "Sem resposta",
                "explicacao": c.explicacao,
                "exemplo_falha": c.exemplo_falha,
            })

        criterios_ok = sum(1 for d in detalhes if d["respondido"])
        criterios_criticos_ok = sum(1 for d in detalhes if d["respondido"] and d["critico"])

        return {
            "proposta": proposta.nome,
            "veredito": veredito.value,
            "veredito_rotulo": veredito.rotulo,
            "score": f"{criterios_ok}/7 criterios",
            "criticos": f"{criterios_criticos_ok}/5 criticos",
            "detalhes": detalhes,
        }

    def scorecard(self) -> Dict[str, Any]:
        return {
            "modulo": "open_proposta_gate",
            "versao": "0.1.0-spec",
            "criterios": len(self.criterios),
            "criterios_criticos": sum(1 for c in self.criterios if c.id <= 5),
            "regra": "Falta 1 critico = WO. Falta nao-critico = JEQUERI.",
            "checklist": [c.pergunta for c in self.criterios],
        }


def _demo():
    gate = PropostaGate()
    sc = gate.scorecard()

    print("=" * 70)
    print("CHECKLIST W.O. -- Proposta de Governo")
    print("=" * 70)

    print(f"\n{sc['criterios']} criterios ({sc['criterios_criticos']} criticos)\n")
    print(f"REGRA: {sc['regra']}\n")

    for c in gate.criterios:
        flag = "[CRITICO]" if c.id <= 5 else "[JEQUERI]"
        print(f"\n{flag} {c.id}. {c.pergunta}")
        print(f"  {c.explicacao}")
        print(f"  FALHA TIPO: {c.exemplo_falha}")

    # --- CASO 1: Proposta vaga (WO) ---
    p1 = PropostaSubmetida(
        nome="\"Vamos transformar o Brasil\"",
        respostas=[
            RespostaProposta(1, False, "", "Nao diz COMO"),
            RespostaProposta(2, False, "", "Nao diz POR QUEM"),
            RespostaProposta(3, False, "", "Nao diz QUANTO"),
            RespostaProposta(4, False, "", "Nao cita fonte de dado"),
            RespostaProposta(5, False, "", "Nao tem prazo"),
            RespostaProposta(6, False, "", "Nao identifica afetados"),
            RespostaProposta(7, False, "", "Nao tem metrica"),
        ]
    )
    r1 = gate.avaliar(p1)
    print(f"\n{'='*70}")
    print(f"CASO 1: {p1.nome}")
    print(f"VEREDITO: {r1['veredito_rotulo']}")
    print(f"SCORE: {r1['score']} | CRITICOS: {r1['criticos']}")

    # --- CASO 2: Proposta detalhada (APROVADO) ---
    p2 = PropostaSubmetida(
        nome="\"30 mil cisternas no sertao ate 2025\"",
        respostas=[RespostaProposta(i, True) for i in range(1, 8)]
    )
    r2 = gate.avaliar(p2)
    print(f"\n{'='*70}")
    print(f"CASO 2: {p2.nome}")
    print(f"VEREDITO: {r2['veredito_rotulo']}")
    print(f"SCORE: {r2['score']} | CRITICOS: {r2['criticos']}")

    # --- CASO 3: Quase (JEQUERI) ---
    p3 = PropostaSubmetida(
        nome="\"Bolsa Familia ampliado\"",
        respostas=[
            RespostaProposta(i, True) for i in range(1, 6)
        ] + [
            RespostaProposta(6, False, "", "Nao identifica quem perde"),
            RespostaProposta(7, False, "", "Nao define metrica de resultado"),
        ]
    )
    r3 = gate.avaliar(p3)
    print(f"\n{'='*70}")
    print(f"CASO 3: {p3.nome}")
    print(f"VEREDITO: {r3['veredito_rotulo']}")
    print(f"SCORE: {r3['score']} | CRITICOS: {r3['criticos']}")


if __name__ == "__main__":
    _demo()
