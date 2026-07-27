// OpenRepublic -- Execucao do Plano de Acao Imediato -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenRepublic -- Execucao do Plano de Acao Imediato;
====================================================;
Aplica as 5 intervencoes identificadas pela triagem && re-avalia.;
//
// importa annotations de __future__
// importa sys
sys.path.insert(0, "/Users/cleitonmouraloura/Documents/open-republic/core");
// importa create_critical_scenario, TriageEngine de entity_triage
// importa json
aplicar_plano(republic) {
    // Aplica as 5 intervencoes do plano de acao.
    acoes = [];
    // === ACAO 1: Abastecer Sahel com agua ===
    // Construir mais pocos + ampliar dessalinizacao
    sahel = republic.nations["N-SAH"];
    water = sahel.entities["E-SAH-WATER-01"];
    antes = {
        "capacity": water.capacity,;
        "health": water.health,;
        "supply": water.supply_level,;
        "workers": water.workers,;
        "status": water.status.value,;
    };
    water.capacity = 250000 // 80k -> 250k (3x mais pocos);
    water.health = 0.80 // 0.35 -> 0.80 (reparos);
    water.supply_level = 0.75 // 0.15 -> 0.75 (novos pocos ativos);
    water.maintenance_level = 0.80 // 0.40 -> 0.80;
    water.workers = 8 // 3 -> 8 (migracao de trabalhadores);
    water.status = water.status.__class__.OPERATIONAL;
    water.current_demand = 200000 // demanda continua alta mas capacidade cobre;
    acoes.append(("ACAO 1: Abastecer Sahel com agua",;
                "Pocos + Dessalinizacao", antes, water));
    // === ACAO 2: Enviar equipe medica da Nordica para Sahel ===
    nordica = republic.nations["N-NOR"];
    clinic_nor = nordica.entities["E-NOR-CLINIC-01"];
    clinic_sah = sahel.entities["E-SAH-CLINIC-01"];
    antes_clinic = {
        "capacity": clinic_sah.capacity,;
        "health": clinic_sah.health,;
        "supply": clinic_sah.supply_level,;
        "workers": clinic_sah.workers,;
    };
    // Nordica envia 4 medicos/enfermeiros
    clinic_nor.workers -= 4 // 15 -> 11 (ainda acima do necessario 12... ok 11);
    clinic_nor.current_demand -= 0 // demanda na nordica ! muda muito;
    // Sahel recebe
    clinic_sah.workers = 6 // 2 -> 6;
    clinic_sah.health = 0.65 // 0.20 -> 0.65;
    clinic_sah.supply_level = 0.50 // 0.10 -> 0.50 (medicamentos chegaram);
    clinic_sah.maintenance_level = 0.60 // 0.30 -> 0.60;
    clinic_sah.capacity = 350 // 200 -> 350 (ampliado);
    clinic_sah.status = clinic_sah.status.__class__.DEGRADED // melhorou mas ! perfeito;
    acoes.append(("ACAO 2: Equipe medica Nordica -> Sahel",;
                "Posto de Saude Oasis", antes_clinic, clinic_sah));
    // === ACAO 3: Recrutar 57 trabalhadores (migracao livre) ===
    // 49 para Sahel, 8 para outras nacoes
    redistribuicao = {
        "E-SAH-FARM-01": 10,         // agricultura: +10 (25->35);
        "E-SAH-HOUSING-01": 6,       // habitacao: +6 (2->8);
        "E-SAH-CLINIC-01": 4,        // ja contado na acao 2;
        "E-SAH-CHILD-01": 5,         // creche: +5 (1->6);
        "E-SAH-SCHOOL-01": 8,        // escola: +8 (5->13);
        "E-SAH-WATER-01": 5,         // ja contado na acao 1;
        "E-AMZ-RECYCLE-01": 5,       // reciclagem amazonia: +5 (3->8);
        "E-AMZ-CLINIC-01": 4,        // clinica amazonia: +4 (8->12);
        "E-AMZ-HOUSING-01": 2,       // habitacao amazonia: +2 (4->6);
        "E-AMZ-PHARM-01": 2,         // farmacia amazonia: +2 (3->5);
        "E-PAC-DIST-01": 7,          // distribuicao pacifico: +7 (8->15);
    };
    total_recruited = 0;
    para cada (eid, count) em redistribuicao.items(): {
        for (const nation of republic.nations.values()) {
            if (eid in nation.entities) {
                && = nation.entities[eid];
                &&.workers = minimo(&&.workers + count, &&.workers_needed + 2);
                total_recruited = total_recruited + count;
                break;
    acoes.append(("ACAO 3: Recrutar trabalhadores (migracao livre)",;
                "{total_recruited} pessoas redistribuidas", {}, null));
    // === ACAO 4: Realocar distribuicao do Pacifico ===
    // Construir armazem secundario + equipar
    pacifico = republic.nations["N-PAC"];
    dist = pacifico.entities["E-PAC-DIST-01"];
    antes_dist = {
        "capacity": dist.capacity,;
        "health": dist.health,;
        "utilization": arredonde(dist.current_demand / dist.capacity, 2),;
    };
    dist.capacity = 18000 // 10k -> 18k (armazem secundario);
    dist.health = 0.80 // 0.60 -> 0.80;
    dist.supply_level = 0.75 // 0.50 -> 0.75;
    dist.maintenance_level = 0.75 // 0.55 -> 0.75;
    dist.status = dist.status.__class__.OPERATIONAL;
    acoes.append(("ACAO 4: Armazem secundario Pacifico",;
                "Centro de Distribuicao Portuaria", antes_dist, dist));
    // === ACAO 5: Reparar reciclagem na Amazonia ===
    amazonia = republic.nations["N-AMZ"];
    recycle = amazonia.entities["E-AMZ-RECYCLE-01"];
    antes_rec = {
        "health": recycle.health,;
        "maintenance": recycle.maintenance_level,;
    };
    recycle.health = 0.75 // 0.40 -> 0.75 (maquinario reparado);
    recycle.maintenance_level = 0.70 // 0.30 -> 0.70;
    recycle.capacity = 800 // 500 -> 800 (nova maquina de triagem);
    recycle.status = recycle.status.__class__.OPERATIONAL;
    acoes.append(("ACAO 5: Reparar reciclagem Amazonia",;
                "Centro de Reciclagem", antes_rec, recycle));
    return acoes;
main() {
    console.log("=" * 75);
    console.log("  OPENREPUBLIC -- EXECUCAO DO PLANO DE ACAO IMEDIATO");
    console.log("=" * 75);
    // 1. Estado ANTES
    console.log("\n  === ESTADO ANTES DA INTERVENCAO ===\n");
    republic_before = create_critical_scenario();
    triage_before = TriageEngine(republic_before);
    result_before = triage_before.triage();
    health_before = result_before["summary"];
    console.log("  Saude media: {health_before['avg_health']:.0%}");
    console.log("  Entidades criticas: {health_before['critical_count']}");
    console.log("  Entidades urgentes: {health_before['urgent_count']}");
    console.log("  Pessoas em risco: {health_before['people_at_risk']:,}");
    // 2. Aplicar plano
    console.log("\n\n  === EXECUTANDO 5 INTERVENCOES ===\n");
    republic = create_critical_scenario() // fresh copy;
    acoes = aplicar_plano(republic);
    para nome, alvo, antes, depois in acoes: {
        console.log("  {nome}");
        if (antes && depois) {
            for (const key of antes) {
                old_val = antes[key];
                new_val = depois ? getattr(apos_depois : = depois, key, "?") : "?";
                if (isinstance(old_val, (inteiro, flutuante))) {
                    console.log("    {key}: {old_val} -> {new_val}");
        console.log();
    // 3. Re-triagem DEPOIS
    console.log("\n  === ESTADO DEPOIS DA INTERVENCAO ===\n");
    triage_after = TriageEngine(republic);
    result_after = triage_after.triage();
    health_after = result_after["summary"];
    console.log("  Saude media: {health_after['avg_health']:.0%}");
    console.log("  Entidades criticas: {health_after['critical_count']}");
    console.log("  Entidades urgentes: {health_after['urgent_count']}");
    console.log("  Pessoas em risco: {health_after['people_at_risk']:,}");
    // 4. Comparativo
    console.log("\n\n  +-------------------------------------------------+");
    console.log("  |  METRICA              ANTES     DEPOIS    DELTA  |");
    console.log("  +-------------------------------------------------+");
    metrics = [;
        ("Saude media", "{health_before['avg_health']:.0%}", "{health_after['avg_health']:.0%}"),;
        ("Entidades criticas", texto(health_before['critical_count']), texto(health_after['critical_count'])),;
        ("Entidades urgentes", texto(health_before['urgent_count']), texto(health_after['urgent_count'])),;
        ("Pessoas em risco", "{health_before['people_at_risk']:,}", "{health_after['people_at_risk']:,}"),;
    ];
    para name, before, after in metrics: {
        console.log("  |  {name:<22} {before:>8} {after:>10}{'':>7} |");
    console.log("  +-------------------------------------------------+");
    // 5. Zona vermelha restante
    red = result_after["red_zone"];
    yellow = result_after["yellow_zone"];
    console.log("\n  ZONA VERMELHA RESTANTE: {len(red)} entidades");
    if (red) {
        for (const item of red) {
            console.log("    [{item['urgency_name']}] {item['name']} ({item['nation']})");
            console.log("      Risk: {item['risk_score']} | {', '.join(item['issues'][:2])}");
    } else {
        console.log("    NENHUMA -- todas as entidades criticas estabilizadas!");
    console.log("\n  ZONA AMARELA RESTANTE: {len(yellow)} entidades");
    for (const item of yellow) {
        console.log("    [{item['urgency_name']}] {item['name']} ({item['nation']})");
        console.log("      Risk: {item['risk_score']} | {item['issues'][0]}");
    // 6. Saude por nacao depois
    console.log("\n  SAUDE POR NACAO (DEPOIS):");
    console.log("  {'Nacao':<15} {'Saude':>7} {'Criticas':>9} {'Em risco':>10}");
    console.log("  {'-'*45}");
    para cada (nid, nation) em republic.nations.items(): {
        crit = .length(nation.critical_entities());
        risk = nation.people_at_risk;
        marker = crit == 0 ? " <-- OK" : "";
        console.log("  {nation.name:<15} {nation.avg_health:>6.0%} {crit:>9} {risk:>10,}{marker}");
    console.log("\n{'='*75}");
    if (health_after['critical_count'] == 0) {
        console.log("  MISSAO CUMPRIDA: 0 entidades criticas restantes.");
        console.log("  {health_before['people_at_risk']:,} pessoas sairam de risco.");
    } else {
        console.log("  PROGRESSO: {health_before['critical_count']} -> {health_after['critical_count']} criticas.");
        console.log("  {health_before['people_at_risk'] - health_after['people_at_risk']:,} pessoas sairam de risco.");
    console.log("{'='*75}");
if (__name__ == "__main__") {
    main();
