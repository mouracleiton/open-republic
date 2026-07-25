# OpenFairSurplusAssembly -- Assembleia Vota: 5% e o Suficiente

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_fair_surplus_assembly.py`

**Descricao:** ================================================================
DESCOBERTA DO FUNDADOR:
  "5% de excedente. Voce recebe 5% de cada mercadoria.
   Incentiva ter MAIS gente trabalhando e se sustentando."
ASSEMBLEIA CONSTITUINTE CONVOCADA:
  "5% de excedente e o suficiente para sustentar a operacao
   sem explorar o trabalhador?"
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenFairSurplusAssembly -- Assembleia Vota: 5% e o Suficiente
================================================================

DESCOBERTA DO FUNDADOR:
  "5% de excedente. Voce recebe 5% de cada mercadoria.
   Incentiva ter MAIS gente trabalhando e se sustentando."

ASSEMBLEIA CONSTITUINTE CONVOCADA:
  "5% de excedente e o suficiente para sustentar a operacao
   sem explorar o trabalhador?"

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa random
// importa Any, Dict, List de typing
// importa Enum de enum
// importa Counter de collections


classe VoteOption herda de Enum:
    FIVE_PCT = ("5 por cento", 0.05)
    THREE_PCT = ("3 por cento", 0.03)
    SEVEN_PCT = ("7 por cento", 0.07)
    TEN_PCT = ("10 por cento", 0.10)
    ZERO = ("zero (sem excedente)", 0.00)


funcao run_assembly(n_voters: inteiro = 10000) -> {texto: qualquer}:
    votes = {opt: 0 para opt em VoteOption}

    para cada _ em intervalo(n_voters):
        r = random.random()
        se r < 0.62 entao:
            votes[VoteOption.FIVE_PCT] += 1
        senao se r < 0.78 entao:
            votes[VoteOption.THREE_PCT] += 1
        senao se r < 0.90 entao:
            votes[VoteOption.SEVEN_PCT] += 1
        senao se r < 0.96 entao:
            votes[VoteOption.TEN_PCT] += 1
        senao:
            votes[VoteOption.ZERO] += 1

    winner = maximo(votes, key=votes.get)
    runner_up = ordene(votes, key=votes.get, reverse=verdadeiro)[1]

    retorne {
        "question": (
            "5% de excedente sobre mercadoria e o suficiente para "
            "sustentar a operacao sem explorar o trabalhador?"
        ),
        "votes": {opt.value[0]: count para opt, count in votes.items()},
        "total": n_voters,
        "winner": winner.value[0],
        "winner_pct": winner.value[1],
        "winner_votes": votes[winner],
        "winner_percent": "{votes[winner]/n_voters*100:.0f}%",
        "runner_up": runner_up.value[0],
        "runner_up_votes": votes[runner_up],
        "decision": (
            "APROVADO. 5% e o excedente justo. "
            "Volta pra quem trabalha. Nao pra dono."
            if winner = = VoteOption.FIVE_PCT else
            "Decidido: {winner.value[0]}"
        ),
        "law": {
            "excedente_maximo": 0.05,
            "excedente_vai_para": "pool_coletivo_trabalhadores",
            "excedente_nao_vai_para": "dono (dono nao existe)",
            "acima_de_5pct": "PREDATORIO (OpenAntiPredatory bloqueia)",
            "incentivo": "mais trabalhadores = mais 5% circulando",
            "contrasta_com": "capitalismo 60-90% pro dono",
            "is_law": verdadeiro,
            "ratified_by": "Assembleia Constituinte",
            "ratified_date": "2026-07-24",
        },
    }


se __name__ == "__main__" entao:
    imprima("=" * 80)
    imprima("  ASSEMBLEIA CONSTITUINTE -- VOTACAO: EXCEDENTE DE 5%")
    imprima("=" * 80)

    result = run_assembly(10000)

    imprima("\n  PERGUNTA:\n    {result['question']}\n")
    imprima("  VOTACAO ({result['total']:,} cidadaos):\n")
    para option, count in ordene(result["votes"].items(),
                                key = (x) -> -x[1]):
        pct = count / result["total"] * 100
        bar = "#" * inteiro(pct / 2)
        winner_mark = option == result["winner"] ? " <--- VENCEDOR" : ""
        imprima("    {option:<25} {count:>6} ({pct:.0f}%) {bar}{winner_mark}")

    imprima("\n  RESULTADO: {result['decision']}")
    imprima("  Vencedor: {result['winner']} ({result['winner_percent']})")
    imprima("  Runner-up: {result['runner_up']} ({result['runner_up_votes']/result['total']*100:.0f}%)")

    imprima("\n  LEI RATIFICADA:")
    para cada (key, val) em result["law"].items():
        se isinstance(val, flutuante) entao:
            imprima("    {key:<30} {val:.0%}")
        senao:
            imprima("    {key:<30} {val}")

    imprima("\n{'='*80}")
    imprima("  ASSEMBLEIA DECIDIU: 5% de excedente. LEI.")
    imprima("  62% dos cidadaos concordaram.")
    imprima("  Acima de 5% = PREDATORIO = BLOQUEADO.")
    imprima("  O 5% volta pra quem trabalha. Sempre.")
    imprima("{'='*80}")

```
