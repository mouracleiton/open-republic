/* OpenValueSimulation -- Simulacoes com Pessoas Reais (Nomes Obfuscados) -- gerado de Portugol++ */
#ifndef OPENVALUESIMULATION_SIMULACOES_COM_PESSOAS_REAIS_NOMES_OBFUSCADOS_H
#define OPENVALUESIMULATION_SIMULACOES_COM_PESSOAS_REAIS_NOMES_OBFUSCADOS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenValueSimulation -- Simulacoes com Pessoas Reais (Nomes Obfuscados);
========================================================================;
Simula o fluxo de valor com salarios REAIS do mercado brasileiro.;
Nomes obfuscados para proteger identidade.;
Pega dados reais: salario mediano, receita que gera, quanto banco suga.;
Mostra: CAPITALISMO vs REPUBLICA para cada pessoa.;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List de typing
// importa datetime de datetime
// ============================================================================
// 1. PESSOAS REAIS (nomes obfuscados)
// ============================================================================
// decorador: @dataclass
typedef struct RealWorker {
    // Um trabalhador real com salario real (nome obfuscado).
    worker_id: texto;
    alias: texto // nome obfuscado;
    real_profession: texto;
    company_type: texto;
    monthly_salary: flutuante // salario real (R$/mes);
    hours_per_month: flutuante;
    company_revenue_from_worker: flutuante // quanto a empresa fatura com ele;
    bank_costs_monthly: flutuante // quanto o banco suga (juros+taxa);
    intermediary_cut: flutuante // intermediario suga;
    // Contexto pessoal
    int family_size = 1;
    double rent = 0.0;
    char* location = "";
// Dados baseados em salarios reais do mercado brasileiro (2024-2026)
// Fontes: CAGED, Glassdoor, Catho, IBGE
[RealWorker] WORKERS = [;
    RealWorker(;
        "W-001", "Trab_A", "Programador Pleno", "Tech Corp",;
        monthly_salary = 8000, hours_per_month=176,;
        company_revenue_from_worker = 25000,;
        bank_costs_monthly = 850, // cartao+juros+taxas;
        intermediary_cut = 0,;
        family_size = 3, rent=1800, location="Sao Paulo",;
    ),;
    RealWorker(;
        "W-002", "Trab_B", "Pedreiro", "Construtora",;
        monthly_salary = 2800, hours_per_month=200,;
        company_revenue_from_worker = 18000,;
        bank_costs_monthly = 420, // cartao+cheque especial;
        intermediary_cut = 0,;
        family_size = 4, rent=900, location="Interior SP",;
    ),;
    RealWorker(;
        "W-003", "Trab_C", "Medica Clinica Geral", "Hospital",;
        monthly_salary = 18000, hours_per_month=160,;
        company_revenue_from_worker = 60000,;
        bank_costs_monthly = 1500,;
        intermediary_cut = 0,;
        family_size = 2, rent=3500, location="Rio de Janeiro",;
    ),;
    RealWorker(;
        "W-004", "Trab_D", "Cozinheira de Restaurante", "Restaurante",;
        monthly_salary = 1850, hours_per_month=220,;
        company_revenue_from_worker = 12000,;
        bank_costs_monthly = 380,;
        intermediary_cut = 0,;
        family_size = 3, rent=700, location="Salvador",;
    ),;
    RealWorker(;
        "W-005", "Trab_E", "Motorista de Aplicativo", "Uber/99",;
        monthly_salary = 3200, hours_per_month=240,;
        company_revenue_from_worker = 8000,;
        bank_costs_monthly = 250,;
        intermediary_cut = 2800, // 35% pro app;
        family_size = 2, rent=1100, location="Belo Horizonte",;
    ),;
    RealWorker(;
        "W-006", "Trab_F", "Professor Ensino Medio", "Escola Publica",;
        monthly_salary = 4200, hours_per_month=160,;
        company_revenue_from_worker = 12000,;
        bank_costs_monthly = 450,;
        intermediary_cut = 0,;
        family_size = 4, rent=1200, location="Fortaleza",;
    ),;
    RealWorker(;
        "W-007", "Trab_G", "Agricultor Assalariado", "Fazenda",;
        monthly_salary = 1518, hours_per_month=220, // salario minimo;
        company_revenue_from_worker = 15000,;
        bank_costs_monthly = 200,;
        intermediary_cut = 0,;
        family_size = 5, rent=0, location="Zona Rural GO",;
    ),;
    RealWorker(;
        "W-008", "Trab_H", "Enfermeira", "Hospital",;
        monthly_salary = 5500, hours_per_month=180,;
        company_revenue_from_worker = 20000,;
        bank_costs_monthly = 620,;
        intermediary_cut = 0,;
        family_size = 3, rent=1400, location="Curitiba",;
    ),;
    RealWorker(;
        "W-009", "Trab_I", "Costureira em Fabrica", "Confecao",;
        monthly_salary = 1600, hours_per_month=200,;
        company_revenue_from_worker = 9000,;
        bank_costs_monthly = 280,;
        intermediary_cut = 0,;
        family_size = 2, rent=600, location="Caruaru PE",;
    ),;
    RealWorker(;
        "W-010", "Trab_J", "Entregador de App", "iFood",;
        monthly_salary = 2400, hours_per_month=240,;
        company_revenue_from_worker = 7000,;
        bank_costs_monthly = 180,;
        intermediary_cut = 2100, // 30% pro app;
        family_size = 1, rent=800, location="Recife",;
    ),;
    RealWorker(;
        "W-011", "Trab_K", "Eletricista Autonomo", "Autonomo",;
        monthly_salary = 3800, hours_per_month=180,;
        company_revenue_from_worker = 6000,;
        bank_costs_monthly = 550, // maquininha + imposto cartao;
        intermediary_cut = 300, // maquininha;
        family_size = 3, rent=1000, location="Porto Alegre",;
    ),;
    RealWorker(;
        "W-012", "Trab_L", "Auxiliar de Limpeza", "Terceirizada",;
        monthly_salary = 1412, hours_per_month=200, // salario minimo;
        company_revenue_from_worker = 5000,;
        bank_costs_monthly = 150,;
        intermediary_cut = 0,;
        family_size = 4, rent=500, location="Manaus",;
    ),;
];
// ============================================================================
// 2. SIMULADOR
// ============================================================================
typedef struct ValueSimulator {
    // Simula fluxo de valor para pessoas reais.
    PARA CADA TRABALHADOR MOSTRA:;
    1. CAPITALISMO: quanto recebe hoje vs quanto produz;
    2. PARASITAS: empresa + banco + intermediario;
    3. REPUBLICA EXECUTAVEL: quanto receberia;
    4. GANHO: diferenca (R$ && multiplicador);
    5. IMPACTO NA VIDA: o que muda;
    //
    void __init__(self) {
        self.workers = {w.worker_id: w para w em WORKERS};
    {texto: qualquer} simulate_worker(self, worker_id: texto) {
        // Simula um trabalhador especifico.
        w = self.workers.get(worker_id);
        if (! w) {
            return {"error": "! encontrado"};
        // CAPITALISMO
        company_profit = w.company_revenue_from_worker - w.monthly_salary \;
                        - (w.company_revenue_from_worker * 0.30) // 30% op real;
        company_extracted = maximo(0, company_profit);
        bank_extracted = w.bank_costs_monthly;
        intermediary_extracted = w.intermediary_cut;
        total_extracted = company_extracted + bank_extracted + intermediary_extracted;
        worker_keeps_pct = w.monthly_salary / w.company_revenue_from_worker * 100;
        // REPUBLICA EXECUTAVEL
        operational_real = w.company_revenue_from_worker * 0.30;
        pool_5pct = w.company_revenue_from_worker * 0.05;
        // Sem dono. Sem banco. Sem intermediario.
        worker_receives_republic = w.company_revenue_from_worker - operational_real;
        // Pool volta para o trabalhador
        worker_total_republic = worker_receives_republic;
        // GANHO
        gain = worker_total_republic - w.monthly_salary;
        multiplier = worker_total_republic / maximo(w.monthly_salary, 1);
        // Impacto na vida
        sobra_capitalism = w.monthly_salary - w.rent - (w.family_size * 400);
        sobra_republic = worker_total_republic - w.rent - (w.family_size * 400);
        return {;
            "alias": w.alias,;
            "profissao": w.real_profession,;
            "empresa": w.company_type,;
            "local": w.location,;
            "familia": w.family_size,;
            "horas_mes": w.hours_per_month,;
            "CAPITALISMO": {
                "produz": "R$ {w.company_revenue_from_worker:,.0f}/mes",;
                "recebe": "R$ {w.monthly_salary:,.0f}/mes",;
                "fica_com": "{worker_keeps_pct:.0f}%",;
                "empresa_suga": "R$ {company_extracted:,.0f}/mes",;
                "banco_suga": "R$ {bank_extracted:,.0f}/mes",;
                "intermediario_suga": "R$ {intermediary_extracted:,.0f}/mes",;
                "total_extraido": "R$ {total_extracted:,.0f}/mes",;
                "sobra_apos_aluguel_comida": "R$ {sobra_capitalism:,.0f}/mes",;
                "hora_valor": "R$ {w.monthly_salary/w.hours_per_month:.2f}/h",;
                "razao_exploracao": "{w.company_revenue_from_worker/w.monthly_salary:.1f}x",;
            },;
            "REPUBLICA_EXECUTAVEL": {
                "produz": "R$ {w.company_revenue_from_worker:,.0f}/mes",;
                "recebe": "R$ {worker_total_republic:,.0f}/mes",;
                "fica_com": "{worker_total_republic/w.company_revenue_from_worker*100:.0f}%",;
                "empresa_suga": "R$ 0 (cooperativa, sem dono)",;
                "banco_suga": "R$ 0 (OpenCredit)",;
                "intermediario_suga": "R$ 0 (OpenMarketplace)",;
                "total_extraido": "R$ 0",;
                "pool_5pct": "R$ {pool_5pct:,.0f}/mes (volta)",;
                "operacional_real": "R$ {operational_real:,.0f}/mes",;
                "sobra_apos_aluguel_comida": "R$ {sobra_republic:,.0f}/mes",;
                "hora_valor": "R$ {worker_total_republic/w.hours_per_month:.2f}/h",;
            },;
            "GANHO": {
                "extra_por_mes": "R$ {gain:,.0f}",;
                "extra_por_ano": "R$ {gain*12:,.0f}",;
                "multiplicador": "{multiplier:.1f}x",;
                "sobra_capitalismo": "R$ {sobra_capitalism:,.0f}/mes",;
                "sobra_republica": "R$ {sobra_republic:,.0f}/mes",;
                "mudanca_vida": self._life_impact(sobra_capitalism, sobra_republic),;
            },;
            "message": (;
                "{w.alias} ({w.real_profession}): ";
                "HOJE recebe R$ {w.monthly_salary:,.0f} de R$ {w.company_revenue_from_worker:,.0f} que produz ";
                "({worker_keeps_pct:.0f}%). ";
                "REPUBLICA: R$ {worker_total_republic:,.0f} ({multiplier:.1f}x). ";
                "GANHO: R$ {gain:,.0f}/mes (R$ {gain*12:,.0f}/ano).";
            ),;
        };
    char* _life_impact(self, sobra_cap: flutuante, sobra_rep: flutuante) {
        // O que muda na vida da pessoa.
        if (sobra_cap < 0 && sobra_rep > 0) {
            return "SAI DA POBREZA. Hoje passa fome. Republica: sobra dinheiro.";
        if (sobra_cap < 500 && sobra_rep > 2000) {
            return "MUDANCA DRAMATICA. Hoje apertado. Republica: qualidade de vida.";
        if (sobra_cap < 2000 && sobra_rep > 5000) {
            return "QUALIDADE DE VIDA. Hoje sobrevive. Republica: prospera.";
        if (sobra_cap < 5000 && sobra_rep > 10000) {
            return "PROSPERIDADE. Hoje confortavel. Republica: investe.";
        if (sobra_rep > sobra_cap * 2) {
            return "DOBRAR PADRAO DE VIDA.";
        return "Ganho de R$ {sobra_rep - sobra_cap:,.0f}/mes de sobra.";
    {texto: qualquer} simulate_all(self) {
        // Simula todos os trabalhadores.
        results = [];
        total_gain_monthly = 0;
        total_extracted_monthly = 0;
        total_workers = sizeof(self.workers);
        /* TODO: iterador C manual para wid em self.workers */
            r = self.simulate_worker(wid);
            results.append(r);
            gain_str = r["GANHO"]["extra_por_mes"].replace("R$ ", "").replace(",", "").replace("/mes", "");
            total_gain_monthly = total_gain_monthly + flutuante(gain_str);
            ext_str = r["CAPITALISMO"]["total_extraido"].replace("R$ ", "").replace(",", "").replace("/mes", "");
            total_extracted_monthly = total_extracted_monthly + flutuante(ext_str);
        return {;
            "total_trabalhadores": total_workers,;
            "total_extraido_mensal": "R$ {total_extracted_monthly:,.0f}",;
            "total_extraido_anual": "R$ {total_extracted_monthly*12:,.0f}",;
            "total_ganho_republica_mensal": "R$ {total_gain_monthly:,.0f}",;
            "total_ganho_republica_anual": "R$ {total_gain_monthly*12:,.0f}",;
            "message": (;
                "{total_workers} trabalhadores simulados. ";
                "Capitalismo extrai R$ {total_extracted_monthly:,.0f}/mes ";
                "(R$ {total_extracted_monthly*12:,.0f}/ano). ";
                "Republica devolve R$ {total_gain_monthly:,.0f}/mes ";
                "(R$ {total_gain_monthly*12:,.0f}/ano). ";
                "POR ANO: R$ {total_gain_monthly*12:,.0f} voltam pra quem trabalha.";
            ),;
        };
    {texto: qualquer} aggregate_stats(self) {
        // Stats agregadas de todos os trabalhadores.
        salaries = [w.monthly_salary para w em self.workers.values()];
        revenues = [w.company_revenue_from_worker para w em self.workers.values()];
        bank_costs = [w.bank_costs_monthly para w em self.workers.values()];
        intermediary = [w.intermediary_cut para w em self.workers.values()];
        return {;
            "trabalhadores": sizeof(self.workers),;
            "salario_medio": "R$ {sum(salaries)/len(salaries):,.0f}",;
            "salario_minimo_simulado": "R$ {min(salaries):,.0f}",;
            "salario_maximo_simulado": "R$ {max(salaries):,.0f}",;
            "receita_media_gerada": "R$ {sum(revenues)/len(revenues):,.0f}",;
            "banco_suga_total_mes": "R$ {sum(bank_costs):,.0f}",;
            "intermediario_suga_total_mes": "R$ {sum(intermediary):,.0f}",;
            "empresa_suga_total_mes": "R$ {sum(r - s - r*0.30 for r, s in zip(revenues, salaries)):,.0f}",;
        };
// ============================================================================
// 3. MAIN
// ============================================================================
if (__name__ == "__main__") {
    sim = ValueSimulator();
    printf("=" * 80);
    printf("  OPENVALUESIMULATION -- PESSOAS REAIS, SALARIOS REAIS");
    printf("  Nomes obfuscados. Dados reais do mercado brasileiro.");
    printf("=" * 80);
    // === 1. CADA TRABALHADOR ===
    printf("\n\n  === SIMULACAO POR TRABALHADOR ===\n");
    /* TODO: iterador C manual para wid em ordene(sim.workers.keys()) */
        r = sim.simulate_worker(wid);
        w = sim.workers[wid];
        printf("\n  {'='*70}");
        printf("  {r['alias']} | {r['profissao']} | {r['empresa']} | {r['local']}");
        printf("  Familia: {r['familia']} | Horas/mes: {r['horas_mes']}");
        printf("  {'='*70}");
        printf("\n  CAPITALISMO (hoje):");
        printf("    Produz:           {r['CAPITALISMO']['produz']}");
        printf("    Recebe:           {r['CAPITALISMO']['recebe']} ({r['CAPITALISMO']['fica_com']})");
        printf("    Empresa suga:     {r['CAPITALISMO']['empresa_suga']}");
        printf("    Banco suga:       {r['CAPITALISMO']['banco_suga']}");
        printf("    Intermediario:    {r['CAPITALISMO']['intermediario_suga']}");
        printf("    TOTAL EXTRAIDO:   {r['CAPITALISMO']['total_extraido']}");
        printf("    Razao:            {r['CAPITALISMO']['razao_exploracao']}");
        printf("    Hora vale:        {r['CAPITALISMO']['hora_valor']}");
        printf("    Sobra (apos ali+comida): {r['CAPITALISMO']['sobra_apos_aluguel_comida']}");
        printf("\n  REPUBLICA EXECUTAVEL:");
        printf("    Produz:           {r['REPUBLICA_EXECUTAVEL']['produz']}");
        printf("    Recebe:           {r['REPUBLICA_EXECUTAVEL']['recebe']} ({r['REPUBLICA_EXECUTAVEL']['fica_com']})");
        printf("    Empresa suga:     {r['REPUBLICA_EXECUTAVEL']['empresa_suga']}");
        printf("    Banco suga:       {r['REPUBLICA_EXECUTAVEL']['banco_suga']}");
        printf("    Intermediario:    {r['REPUBLICA_EXECUTAVEL']['intermediario_suga']}");
        printf("    Pool 5%:          {r['REPUBLICA_EXECUTAVEL']['pool_5pct']}");
        printf("    Operacional real: {r['REPUBLICA_EXECUTAVEL']['operacional_real']}");
        printf("    Hora vale:        {r['REPUBLICA_EXECUTAVEL']['hora_valor']}");
        printf("    Sobra (apos ali+comida): {r['REPUBLICA_EXECUTAVEL']['sobra_apos_aluguel_comida']}");
        printf("\n  GANHO:");
        printf("    Extra/mes:  {r['GANHO']['extra_por_mes']}");
        printf("    Extra/ano:  {r['GANHO']['extra_por_ano']}");
        printf("    Multiplicador: {r['GANHO']['multiplicador']}");
        printf("    Impacto: {r['GANHO']['mudanca_vida']}");
    // === 2. AGREGADO ===
    printf("\n\n  {'='*70}");
    printf("  === AGREGADO: TODOS OS {len(sim.workers)} TRABALHADORES ===");
    printf("  {'='*70}\n");
    agg = sim.simulate_all();
    printf("  {agg['message']}");
    printf("\n  Extracao mensal total: {agg['total_extraido_mensal']}");
    printf("  Extracao anual total:  {agg['total_extraido_anual']}");
    printf("  Ganho mensal Republica: {agg['total_ganho_republica_mensal']}");
    printf("  Ganho anual Republica:  {agg['total_ganho_republica_anual']}");
    // === 3. STATS ===
    printf("\n\n  === ESTATISTICAS BASE ===\n");
    s = sim.aggregate_stats();
    /* para cada (k, v) em s.items(): */
        printf("  {k:<30} {v}");
    // === 4. RESUMO INDIVIDUAL (tabela) ===
    printf("\n\n  === RESUMO (todos) ===\n");
    printf("  {'Alias':<10} {'Profissao':<25} {'Hoje':>10} {'Republica':>10} {'Ganho':>10} {'X':>5} {'Impacto'}");
    printf("  {'-'*95}");
    /* TODO: iterador C manual para wid em ordene(sim.workers.keys()) */
        r = sim.simulate_worker(wid);
        hoje = r["CAPITALISMO"]["recebe"].replace("R$ ", "").replace(",", "").replace("/mes", "");
        rep = r["REPUBLICA_EXECUTAVEL"]["recebe"].replace("R$ ", "").replace(",", "").replace("/mes", "");
        gain = r["GANHO"]["extra_por_mes"].replace("R$ ", "").replace(",", "").replace("/mes", "");
        mult = r["GANHO"]["multiplicador"];
        impacto = r["GANHO"]["mudanca_vida"][:25];
        printf("  {r['alias']:<10} {r['profissao'][:24]:<25} ";
            "R${int(hoje):>8,} R${int(rep):>8,} R${int(gain):>8,} ";
            "{mult:>4} {impacto}");
    printf("\n{'='*80}");
    printf("  Simulacao: {len(sim.workers)} trabalhadores reais.");
    printf("  Extracao anual: {agg['total_extraido_anual']}.");
    printf("  Se virasse Republica: {agg['total_ganho_republica_anual']} voltam.");
    printf("  Para trabalhadores. Nao parasitas.");
    printf("{'='*80}");

#endif // OPENVALUESIMULATION_SIMULACOES_COM_PESSOAS_REAIS_NOMES_OBFUSCADOS_H
