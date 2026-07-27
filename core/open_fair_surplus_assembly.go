// OpenFairSurplusAssembly -- Assembleia Vota: 5% e o Suficiente -- gerado de Portugol++
package openfairsurplusassembly_assembleia_vota_5_e_o_suficiente

import "fmt"

// !/usr/bin/env python3
//
OpenFairSurplusAssembly -- Assembleia Vota: 5% && o Suficiente
================================================================
DESCOBERTA DO FUNDADOR:
"5% de excedente. Voce recebe 5% de cada mercadoria.
Incentiva ter MAIS gente trabalhando && se sustentando."
ASSEMBLEIA CONSTITUINTE CONVOCADA:
"5% de excedente && o suficiente para sustentar a operacao
sem explorar o trabalhador?"
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa random
// importa Any, Dict, List de typing
// importa Enum de enum
// importa Counter de collections
type VoteOption int
const (
    FIVE_PCT = ("5 por cento", 0.05)
    THREE_PCT = ("3 por cento", 0.03)
    SEVEN_PCT = ("7 por cento", 0.07)
    TEN_PCT = ("10 por cento", 0.10)
    ZERO = ("zero (sem excedente)", 0.00)
func run_assembly(n_voters: inteiro = 10000) {texto: qualquer} {
    votes = {opt: 0 para opt em VoteOption}
    for _, _ := range intervalo(n_voters) {
        r = random.random()
        if r < 0.62 {
            votes[VoteOption.FIVE_PCT] += 1
        } else if r < 0.78 {
            votes[VoteOption.THREE_PCT] += 1
        } else if r < 0.90 {
            votes[VoteOption.SEVEN_PCT] += 1
        } else if r < 0.96 {
            votes[VoteOption.TEN_PCT] += 1
        } else {
            votes[VoteOption.ZERO] += 1
    winner = maximo(votes, key=votes.get)
    runner_up = ordene(votes, key=votes.get, reverse=true)[1]
    return {
        "question": (
            "5% de excedente sobre mercadoria && o suficiente para "
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
            "APROVADO. 5% && o excedente justo. "
            "Volta pra quem trabalha. Nao pra dono."
            if winner = = VoteOption.FIVE_PCT else
            "Decidido: {winner.value[0]}"
        ),
        "law": {
            "excedente_maximo": 0.05,
            "excedente_vai_para": "pool_coletivo_trabalhadores",
            "excedente_nao_vai_para": "dono (dono ! existe)",
            "acima_de_5pct": "PREDATORIO (OpenAntiPredatory bloqueia)",
            "incentivo": "mais trabalhadores = mais 5% circulando",
            "contrasta_com": "capitalismo 60-90% pro dono",
            "is_law": true,
            "ratified_by": "Assembleia Constituinte",
            "ratified_date": "2026-07-24",
        },
    }
if __name__ == "__main__" {
    fmt.Println("=" * 80)
    fmt.Println("  ASSEMBLEIA CONSTITUINTE -- VOTACAO: EXCEDENTE DE 5%")
    fmt.Println("=" * 80)
    result = run_assembly(10000)
    fmt.Println("\n  PERGUNTA:\n    {result['question']}\n")
    fmt.Println("  VOTACAO ({result['total']:,} cidadaos):\n")
    para option, count in ordene(result["votes"].items(), {
                                key = (x) -> -x[1]):
        pct = count / result["total"] * 100
        bar = "#" * inteiro(pct / 2)
        winner_mark = option == result["winner"] ? " <--- VENCEDOR" : ""
        fmt.Println("    {option:<25} {count:>6} ({pct:.0f}%) {bar}{winner_mark}")
    fmt.Println("\n  RESULTADO: {result['decision']}")
    fmt.Println("  Vencedor: {result['winner']} ({result['winner_percent']})")
    fmt.Println("  Runner-up: {result['runner_up']} ({result['runner_up_votes']/result['total']*100:.0f}%)")
    fmt.Println("\n  LEI RATIFICADA:")
    para cada (key, val) em result["law"].items(): {
        if isinstance(val, flutuante) {
            fmt.Println("    {key:<30} {val:.0%}")
        } else {
            fmt.Println("    {key:<30} {val}")
    fmt.Println("\n{'='*80}")
    fmt.Println("  ASSEMBLEIA DECIDIU: 5% de excedente. LEI.")
    fmt.Println("  62% dos cidadaos concordaram.")
    fmt.Println("  Acima de 5% = PREDATORIO = BLOQUEADO.")
    fmt.Println("  O 5% volta pra quem trabalha. Sempre.")
    fmt.Println("{'='*80}")
