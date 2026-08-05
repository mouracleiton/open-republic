#!/usr/bin/env python3
"""
OpenEmendaCoPresidencia -- Emenda Constitucional: Co-Presidência
==================================================================
"Eduardo Suplicy [sic] sonhou. Nós codamos."

ARTIGO 1: O Presidente e o Vice-Presidente têm o MESMO PODER.
Nada é sancionado sem assinatura de AMBOS.
Nada é vetado sem recusa de AMBOS.
Um não decide sem o outro. Decisão é DUPLO COMANDO.

ARTIGO 2: O Vice-Presidente DEVE ser MULHER NEGRA.
Não é cota simbólica. É LEI.
O cargo existe para DESESTRUTURAR 524 anos de poder branco, masculino e patriarcal.

ARTIGO 3: O Sensor (OpenRepublic) ILUMINA. Não decide.
Decidir é CRIME de usurpação popular.

ARTIGO 4: O Conselho do Povo COBRA com dado na mão.
Protesto digital e físico. Sem dado, sem cobrança.

AVISO: TODOS os nomes sao MOCK (placeholder).
O sistema de medicao e REAL. As pessoas sao HIPOTETICAS.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class PoderDecisao(Enum):
    """Quem tem poder de quê."""
    CO_PRESIDENTE = "co_presidente"        # presidente: veto+sancão
    CO_VICE = "co_vice"                     # vice: veto+sancão (MESMO poder)
    SENSOR = "sensor"                        # ilumina, NÃO decide
    CONSELHO_POVO = "conselho_povo"         # cobra com dado
    NENHUM = "nenhum"                        # sem poder


class TipoPoder(Enum):
    SANCAO = "sancao"            # aprovar lei
    VETO = "veto"                # bloquear lei
    DECRETO = "decreto"          # medida provisória
    INDICACAO = "indicacao"      # nomear ministro
    ORCAMENTO = "orcamento"      # definir verba
    MEDICAO = "medicao"          # medir resultado
    COBRANCA = "cobranca"        # cobrar promessa


@dataclass
class RegraConstitucional:
    """Uma regra da emenda constitucional."""
    artigo: str
    titulo: str
    regra: str
    irrevogavel: bool          # cláusula pétrea (não pode ser mudada)


def _init_regras() -> List[RegraConstitucional]:
    return [
        RegraConstitucional("Art. 1", "MESMO PODER",
            "Presidente e Vice têm poder IDÊNTICO de sanção e veto. "
            "Nenhuma lei é sancionada sem assinatura de AMBOS. "
            "Nenhuma lei é vetada sem recusa de AMBOS. "
            "Um não governa sem o outro.",
            True),

        RegraConstitucional("Art. 2", "PRESIDENTE É MULHER NEGRA",
            "O cargo de Presidente é RESERVADO para mulher negra. "
            "Não é cota simbólica. É correção de 524 anos de poder "
            "branco, masculino e patriarcal. "
            "Chapa sem presidente mulher negra = W.O. (impedimento).",
            True),

        RegraConstitucional("Art. 2-A", "VICE É O ÚLTIMO PRESIDENTE",
            "O Vice-Presidente é o presidente recém-saído (último mandato). "
            "Cargo de transição: aporta experiência executiva. "
            "Mesmo poder de veto e sanção. "
            "Não é decoração: é garantia de continuidade + freio.",
            True),

        RegraConstitucional("Art. 3", "DUPLO COMANDO",
            "Toda nomeação de ministro requer assinatura de AMBOS. "
            "Todo decreto exige AMBOS. "
            "Toda medida provisória precisa de AMBOS. "
            "Não existe 'decisão unilateral'.",
            True),

        RegraConstitucional("Art. 4", "SENSOR INDEPENDENTE",
            "O Sensor (sistema de medição) é INDEPENDENTE. "
            "ILUMINA com dado. NÃO decide. "
            "Decidir é CRIME de usurpação popular. "
            "O Sensor mede: Raio X, Censo, Gate, Triagem.",
            True),

        RegraConstitucional("Art. 5", "CONSELHO DO POVO",
            "O Conselho do Povo COBRA com dado na mão. "
            "Protesto digital: dado publico + meta não cumprida. "
            "Protesto físico: presença + dado. "
            "Sem dado, sem cobrança. Sem cobrança, sem pressão.",
            True),

        RegraConstitucional("Art. 6", "TRANSPARÊNCIA RADICAL",
            "Toda decisão é pública em 24h. "
            "Tudo tem fonte, custo, prazo e métrica. "
            "Sem Gate WO (7/7), nada entra em pauta.",
            True),

        RegraConstitucional("Art. 7", "REVOGÁVEL",
            "Qualquer decisão pode ser revista se o dado mostrar que falhou. "
            "Não existe 'foi feito, agora fica'. "
            "Resultado > intenção. Dado > discurso.",
            False),

        RegraConstitucional("Art. 8", "EMENDA",
            "Esta emenda só pode ser revogada por 3/5 do Congresso "
            "EM DUAS SESSÕES + referendo popular. "
            "Cláusulas pétreas (Art. 1-5) NÃO podem ser revogadas.",
            True),
    ]


@dataclass
class CoPresidente:
    """Um dos dois co-presidentes. MOCK."""
    cargo: str                    # "Presidente" ou "Vice-Presidente"
    nome: str                     # MOCK (placeholder)
    obrigatoria_mulher_negra: bool
    poder: List[TipoPoder]
    restricoes: str


def _init_co_presidencia() -> List[CoPresidente]:
    return [
        CoPresidente(
            cargo="Presidente",
            nome="[MOCK - DEVE ser mulher negra]",
            obrigatoria_mulher_negra=True,
            poder=[TipoPoder.SANCAO, TipoPoder.VETO, TipoPoder.DECRETO,
                   TipoPoder.INDICACAO, TipoPoder.ORCAMENTO],
            restricoes="LEI: cargo reservado para mulher negra. "
                       "Chapa sem presidente mulher negra = impugnação (W.O.)."),

        CoPresidente(
            cargo="Vice-Presidente",
            nome="[MOCK - último presidente, cargo de transição]",
            obrigatoria_mulher_negra=False,
            poder=[TipoPoder.SANCAO, TipoPoder.VETO, TipoPoder.DECRETO,
                   TipoPoder.INDICACAO, TipoPoder.ORCAMENTO],
            restricoes="LEI: cargo ocupado pelo presidente recém-saído. "
                       "Aporta experiência. Mesmo poder. Não governa sozinho."),
    ]


def _demo():
    regras = _init_regras()
    co_pres = _init_co_presidencia()

    print("=" * 90)
    print("EMENDA CONSTITUCIONAL: CO-PRESIDÊNCIA COM MESMO PODER")
    print("=" * 90)

    print(f"""
  EDUARDO SUPPLICY SONHOU. NÓS CODAMOS.

  O Brasil teve 36 presidentes. TODOS homens. QUASE TODOS brancos.
  1 mulher (Dilma) -- deposta em golpe.
  0 negros na presidência em 524 anos.
  0 indígenas. 0 pobres.

  A emenda inverte: PRESIDENTE é mulher negra.
  O último presidente vira VICE com mesmo poder.
  Decisão é dupla. Continuidade + correção histórica.
""")

    print(f"{'='*90}")
    print("8 ARTIGOS DA EMENDA")
    print(f"{'='*90}")
    for r in regras:
        pétrea = " *** CLÁUSULA PÉTREA" if r.irrevogavel else ""
        print(f"""
  [{r.artigo}] {r.titulo}{pétrea}
    {r.regra}""")

    print(f"\n{'='*90}")
    print("CO-PRESIDÊNCIA: MESMO PODER")
    print(f"{'='*90}")

    for cp in co_pres:
        print(f"""
  [{cp.cargo.upper()}]
    NOME: {cp.nome}
    OBRIGATÓRIA MULHER NEGRA: {'SIM (LEI)' if cp.obrigatoria_mulher_negra else 'não'}
    PODER: {', '.join(p.value for p in cp.poder)}
    RESTRIÇÕES: {cp.restricoes}""")

    print(f"\n{'='*90}")
    print("COMPARAÇÃO: SISTEMA ATUAL vs CO-PRESIDÊNCIA")
    print(f"{'='*90}")
    print(f"""
  SISTEMA ATUAL (1988-2026):
    Presidente tem TODO o poder de veto e sanção.
    Vice é figura decorativa (espera o presidente morrer).
    36 presidentes. 1 mulher. 0 negros. 0 indígenas.
    Vice serve pra embelezar chapa.

  CO-PRESIDÊNCIA (emenda):
    PRESIDENTE é MULHER NEGRA por LEI.
    VICE é o último presidente (cargo de transição, mesmo poder).
    Nada passa sem AMBOS.
    Decisão é dupla. Ninguém governa sozinho.

  POR QUE PRESIDENTE MULHER NEGRA:
    - 56% da população brasileira é negra (IBGE 2022)
    - Mulher negra ganha R$ 1.500/mês (R$ 3.200 branco, R$ 2.500 negro, R$ 1.500 negra)
    - Feminicídio: 1.8/dia (80% vítimas negras)
    - 0 presidentas negras em 524 anos
    - Não é cota. É JUSTIÇA. É LEI.
    - Quem construiu este país (escravidão, trabalho, cultura) tem direito de governá-lo

  POR QUE O ÚLTIMO PRESIDENTE COMO VICE:
    - Aporta experiência executiva que a presidenta negra pode não ter
      (o sistema excluiu negros do poder por 524 anos)
    - Garante continuidade de governo (não reinventa a roda)
    - Mesmo poder = freio e equilíbrio
    - A presidenta governa com a experiência do vice, não contra
    - O vice não é decoração: é co-piloto com mesmo volante

  POR QUE MESMO PODER:
    - Dilma foi vice de Lula (2003-2010). Sem poder. Decorativa.
    - Quando assumiu (2011), não tinha experiência de duplo comando.
    - O sistema de "vice decorativo" gera figura sem treino.
    - Vice com poder REAL desde o dia 1 = governa junto, aprende junto,
      decide junto. Se o presidente cai, o vice já está no comando.
    - Michel Temer era vice decorativo. Virou presidente por golpe.
      Com co-presidência, golpe não funciona: o vice JÁ tem poder.
""")


if __name__ == "__main__":
    _demo()
