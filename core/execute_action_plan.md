# OpenRepublic -- Execucao do Plano de Acao Imediato

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/execute_action_plan.py`

**Descricao:** ====================================================
Aplica as 5 intervencoes identificadas pela triagem e re-avalia.

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Execucao do Plano de Acao Imediato
====================================================

Aplica as 5 intervencoes identificadas pela triagem e re-avalia.
// 

// importa annotations de __future__
// importa sys
sys.path.insert(0, "/Users/cleitonmouraloura/Documents/open-republic/core")

// importa create_critical_scenario, TriageEngine de entity_triage
// importa json


funcao aplicar_plano(republic):
    // Aplica as 5 intervencoes do plano de acao.
    acoes = []

    // === ACAO 1: Abastecer Sahel com agua ===
    // Construir mais pocos + ampliar dessalinizacao
    sahel = republic.nations["N-SAH"]
    water = sahel.entities["E-SAH-WATER-01"]
    antes = {
        "capacity": water.capacity,
        "health": water.health,
        "supply": water.supply_level,
        "workers": water.workers,
        "status": water.status.value,
    }
    water.capacity = 250000 // 80k -> 250k (3x mais pocos)
    water.health = 0.80 // 0.35 -> 0.80 (reparos)
    water.supply_level = 0.75 // 0.15 -> 0.75 (novos pocos ativos)
    water.maintenance_level = 0.80 // 0.40 -> 0.80
    water.workers = 8 // 3 -> 8 (migracao de trabalhadores)
    water.status = water.status.__class__.OPERATIONAL
    water.current_demand = 200000 // demanda continua alta mas capacidade cobre
    acoes.append(("ACAO 1: Abastecer Sahel com agua",
                  "Pocos + Dessalinizacao", antes, water))

    // === ACAO 2: Enviar equipe medica da Nordica para Sahel ===
    nordica = republic.nations["N-NOR"]
    clinic_nor = nordica.entities["E-NOR-CLINIC-01"]
    clinic_sah = sahel.entities["E-SAH-CLINIC-01"]

    antes_clinic = {
        "capacity": clinic_sah.capacity,
        "health": clinic_sah.health,
        "supply": clinic_sah.supply_level,
        "workers": clinic_sah.workers,
    }
    // Nordica envia 4 medicos/enfermeiros
    clinic_nor.workers -= 4 // 15 -> 11 (ainda acima do necessario 12... ok 11)
    clinic_nor.current_demand -= 0 // demanda na nordica nao muda muito
    // Sahel recebe
    clinic_sah.workers = 6 // 2 -> 6
    clinic_sah.health = 0.65 // 0.20 -> 0.65
    clinic_sah.supply_level = 0.50 // 0.10 -> 0.50 (medicamentos chegaram)
    clinic_sah.maintenance_level = 0.60 // 0.30 -> 0.60
    clinic_sah.capacity = 350 // 200 -> 350 (ampliado)
    clinic_sah.status = clinic_sah.status.__class__.DEGRADED // melhorou mas nao perfeito
    acoes.append(("ACAO 2: Equipe medica Nordica -> Sahel",
                  "Posto de Saude Oasis", antes_clinic, clinic_sah))

    // === ACAO 3: Recrutar 57 trabalhadores (migracao livre) ===
    // 49 para Sahel, 8 para outras nacoes
    redistribuicao = {
        "E-SAH-FARM-01": 10,         // agricultura: +10 (25->35)
        "E-SAH-HOUSING-01": 6,       // habitacao: +6 (2->8)
        "E-SAH-CLINIC-01": 4,        // ja contado na acao 2
        "E-SAH-CHILD-01": 5,         // creche: +5 (1->6)
        "E-SAH-SCHOOL-01": 8,        // escola: +8 (5->13)
        "E-SAH-WATER-01": 5,         // ja contado na acao 1
        "E-AMZ-RECYCLE-01": 5,       // reciclagem amazonia: +5 (3->8)
        "E-AMZ-CLINIC-01": 4,        // clinica amazonia: +4 (8->12)
        "E-AMZ-HOUSING-01": 2,       // habitacao amazonia: +2 (4->6)
        "E-AMZ-PHARM-01": 2,         // farmacia amazonia: +2 (3->5)
        "E-PAC-DIST-01": 7,          // distribuicao pacifico: +7 (8->15)
    }
    total_recruited = 0
    para cada (eid, count) em redistribuicao.items():
        para cada nation em republic.nations.values():
            se eid in nation.entities entao:
                e = nation.entities[eid]
                e.workers = minimo(e.workers + count, e.workers_needed + 2)
                total_recruited = total_recruited + count
                interrompa
    acoes.append(("ACAO 3: Recrutar trabalhadores (migracao livre)",
                  "{total_recruited} pessoas redistribuidas", {}, nulo))

    // === ACAO 4: Realocar distribuicao do Pacifico ===
    // Construir armazem secundario + equipar
    pacifico = republic.nations["N-PAC"]
    dist = pacifico.entities["E-PAC-DIST-01"]
    antes_dist = {
        "capacity": dist.capacity,
        "health": dist.health,
        "utilization": arredonde(dist.current_demand / dist.capacity, 2),
    }
    dist.capacity = 18000 // 10k -> 18k (armazem secundario)
    dist.health = 0.80 // 0.60 -> 0.80
    dist.supply_level = 0.75 // 0.50 -> 0.75
    dist.maintenance_level = 0.75 // 0.55 -> 0.75
    dist.status = dist.status.__class__.OPERATIONAL
    acoes.append(("ACAO 4: Armazem secundario Pacifico",
                  "Centro de Distribuicao Portuaria", antes_dist, dist))

    // === ACAO 5: Reparar reciclagem na Amazonia ===
    amazonia = republic.nations["N-AMZ"]
    recycle = amazonia.entities["E-AMZ-RECYCLE-01"]
    antes_rec = {
        "health": recycle.health,
        "maintenance": recycle.maintenance_level,
    }
    recycle.health = 0.75 // 0.40 -> 0.75 (maquinario reparado)
    recycle.maintenance_level = 0.70 // 0.30 -> 0.70
    recycle.capacity = 800 // 500 -> 800 (nova maquina de triagem)
    recycle.status = recycle.status.__class__.OPERATIONAL
    acoes.append(("ACAO 5: Reparar reciclagem Amazonia",
                  "Centro de Reciclagem", antes_rec, recycle))

    retorne acoes


funcao main():
    imprima("=" * 75)
    imprima("  OPENREPUBLIC -- EXECUCAO DO PLANO DE ACAO IMEDIATO")
    imprima("=" * 75)

    // 1. Estado ANTES
    imprima("\n  === ESTADO ANTES DA INTERVENCAO ===\n")
    republic_before = create_critical_scenario()
    triage_before = TriageEngine(republic_before)
    result_before = triage_before.triage()
    health_before = result_before["summary"]

    imprima("  Saude media: {health_before['avg_health']:.0%}")
    imprima("  Entidades criticas: {health_before['critical_count']}")
    imprima("  Entidades urgentes: {health_before['urgent_count']}")
    imprima("  Pessoas em risco: {health_before['people_at_risk']:,}")

    // 2. Aplicar plano
    imprima("\n\n  === EXECUTANDO 5 INTERVENCOES ===\n")
    republic = create_critical_scenario() // fresh copy
    acoes = aplicar_plano(republic)

    para nome, alvo, antes, depois in acoes:
        imprima("  {nome}")
        se antes e depois entao:
            para cada key em antes:
                old_val = antes[key]
                new_val = depois ? getattr(apos_depois : = depois, key, "?") : "?"
                se isinstance(old_val, (inteiro, flutuante)) entao:
                    imprima("    {key}: {old_val} -> {new_val}")
        imprima()

    // 3. Re-triagem DEPOIS
    imprima("\n  === ESTADO DEPOIS DA INTERVENCAO ===\n")
    triage_after = TriageEngine(republic)
    result_after = triage_after.triage()
    health_after = result_after["summary"]

    imprima("  Saude media: {health_after['avg_health']:.0%}")
    imprima("  Entidades criticas: {health_after['critical_count']}")
    imprima("  Entidades urgentes: {health_after['urgent_count']}")
    imprima("  Pessoas em risco: {health_after['people_at_risk']:,}")

    // 4. Comparativo
    imprima("\n\n  +-------------------------------------------------+")
    imprima("  |  METRICA              ANTES     DEPOIS    DELTA  |")
    imprima("  +-------------------------------------------------+")

    metrics = [
        ("Saude media", "{health_before['avg_health']:.0%}", "{health_after['avg_health']:.0%}"),
        ("Entidades criticas", texto(health_before['critical_count']), texto(health_after['critical_count'])),
        ("Entidades urgentes", texto(health_before['urgent_count']), texto(health_after['urgent_count'])),
        ("Pessoas em risco", "{health_before['people_at_risk']:,}", "{health_after['people_at_risk']:,}"),
    ]

    para name, before, after in metrics:
        imprima("  |  {name:<22} {before:>8} {after:>10}{'':>7} |")

    imprima("  +-------------------------------------------------+")

    // 5. Zona vermelha restante
    red = result_after["red_zone"]
    yellow = result_after["yellow_zone"]
    imprima("\n  ZONA VERMELHA RESTANTE: {len(red)} entidades")
    se red entao:
        para cada item em red:
            imprima("    [{item['urgency_name']}] {item['name']} ({item['nation']})")
            imprima("      Risk: {item['risk_score']} | {', '.join(item['issues'][:2])}")
    senao:
        imprima("    NENHUMA -- todas as entidades criticas estabilizadas!")

    imprima("\n  ZONA AMARELA RESTANTE: {len(yellow)} entidades")
    para cada item em yellow:
        imprima("    [{item['urgency_name']}] {item['name']} ({item['nation']})")
        imprima("      Risk: {item['risk_score']} | {item['issues'][0]}")

    // 6. Saude por nacao depois
    imprima("\n  SAUDE POR NACAO (DEPOIS):")
    imprima("  {'Nacao':<15} {'Saude':>7} {'Criticas':>9} {'Em risco':>10}")
    imprima("  {'-'*45}")
    para cada (nid, nation) em republic.nations.items():
        crit = tamanho(nation.critical_entities())
        risk = nation.people_at_risk
        marker = crit == 0 ? " <-- OK" : ""
        imprima("  {nation.name:<15} {nation.avg_health:>6.0%} {crit:>9} {risk:>10,}{marker}")

    imprima("\n{'='*75}")
    se health_after['critical_count'] == 0 entao:
        imprima("  MISSAO CUMPRIDA: 0 entidades criticas restantes.")
        imprima("  {health_before['people_at_risk']:,} pessoas sairam de risco.")
    senao:
        imprima("  PROGRESSO: {health_before['critical_count']} -> {health_after['critical_count']} criticas.")
        imprima("  {health_before['people_at_risk'] - health_after['people_at_risk']:,} pessoas sairam de risco.")
    imprima("{'='*75}")


se __name__ == "__main__" entao:
    main()

```
