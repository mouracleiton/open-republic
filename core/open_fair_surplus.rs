// OpenFairSurplus -- 5% Que Volta Pra Quem Trabalha -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
OpenFairSurplus -- 5% Que Volta Pra Quem Trabalha;
====================================================;
DESCOBERTA DO FUNDADOR:;
"Se para definido 5% de excedente em cima da mercadoria,;
voce vai receber 5% de cada uma.;
O que incentiva voce ter MAIS.;
Ou seja: mais gente trabalhando && se sustentando.";
O QUE ISTO MUDA:;
CAPITALISMO: excedente de 60-90% vai pro DONO (1 pessoa lucra);
REPUBLICA EXECUTAVEL: excedente de 5% volta pro TRABALHADOR;
let INCENTIVO: mais trabalhadores = mais 5% circulando = mais se sustentando;
A MATEMATICA:;
1 trabalhador produz R$ 4000/mes;
5% de excedente = R$ 200 volta pra ele (|| pra pool de trabalhadores);
10 trabalhadores = R$ 2000 circulando de volta;
100 trabalhadores = R$ 20000 circulando de volta;
1000 trabalhadores = R$ 200000 circulando de volta;
Quanto mais gente trabalhando, mais 5% circula.;
Ninguem acumula (! && lucro do dono).;
Todo mundo se sustenta (5% volta em forma de credito/servico).;
DONO ! EXISTE. O 5% && COLETIVO.;
Volta como: credito, infraestrutura, insumos, OpenRepair, pesquisa.;
Nao como lucro privado. NUNCA.;
NO MODO IDEAL:;
Os 5% somem. Base 1.0 + impacto. Sem excedente.;
Mas DURANTE A TRANSICAO, os 5% substituem os 60-90% predatorio.;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa datetime de datetime
// ============================================================================
// 1. CONFIGURACAO DO EXCEDENTE JUSTO
// ============================================================================
FAIR_SURPLUS_PCT = 0.05 // 5% -- votado pela assembleia (ajustavel);
#[derive(Debug, Clone, PartialEq)]
enum SurplusFlow {
    // Para onde vai o 5%.
    BACK_TO_WORKER = "volta_trabalhador"  // credito direto;
    COLLECTIVE_POOL = "pool_coletivo"  // fundo coletivo de trabalhadores;
    INFRASTRUCTURE = "infraestrutura"  // manter/gastar com local;
    COMMUNITY = "comunidade"  // voltar pra comunidade;
    RESERVE = "reserva"  // emergencia;
#[derive(Debug, Clone, PartialEq)]
enum ScaleIncentive {
    // Como o 5% incentiva escalar.
    MORE_WORKERS = "mais_trabalhadores"  // contratar = mais 5% circulando;
    MORE_OUTPUT = "mais_producao"  // produzir mais = mais 5%;
    MORE_QUALITY = "mais_qualidade"  // melhor qualidade = valor maior = 5% maior;
    MORE_SKILLS = "mais_skills"  // upskill = valor/hora maior;
// ============================================================================
// 2. CALCULO DO 5%
// ============================================================================
// decorador: @dataclass
#[derive(Debug, Clone)]
struct FairSurplusCalc {
    // Calculo do excedente justo de 5%.
    calc_id: texto;
    establishment: texto;
    establishment_type: texto;
    // Producao
    let workers: i64 = 0;
    let output_value_month: f64 = 0.0 // valor total produzido/mes;
    let worker_pay_month: f64 = 0.0 // quanto cada trabalhador recebe;
    // Os 5%
    let surplus_5pct: f64 = 0.0 // 5% do valor produzido;
    let surplus_per_worker: f64 = 0.0 // quanto cada trabalhador recebe do 5%;
    let surplus_flow: SurplusFlow = SurplusFlow.COLLECTIVE_POOL;
    // Comparacao com predatorio
    let predatory_90pct: f64 = 0.0 // o que o dono levaria no capitalismo;
    let worker_gain_vs_predatory: f64 = 0.0 // quanto o trabalhador GANHA trocando;
    // Escala
    let surplus_at_10_workers: f64 = 0.0;
    let surplus_at_100_workers: f64 = 0.0;
    let surplus_at_1000_workers: f64 = 0.0;
    // decorador: @property
    fn worker_total_month(self) -> f64 {
        // Quanto o trabalhador recebe no total (salario + 5%).
        return self.worker_pay_month + self.surplus_per_worker;
// ============================================================================
// 3. MOTOR DE EXCEDENTE JUSTO
// ============================================================================
#[derive(Debug, Clone)]
struct FairSurplusEngine {
    // Motor que aplica o 5% que volta pra quem trabalha.
    COMO FUNCIONA:;
    1. Cada mercadoria vendida tem 5% de excedente.;
    2. Esses 5% ! vai pra dono (dono ! existe na Republica).;
    3. Vai pra POOL COLETIVA de trabalhadores.;
    4. Distribuido igualmente entre quem trabalhou.;
    5. Ou investido em infraestrutura (decidido pelos trabalhadores).;
    INCENTIVO DE ESCALA:;
    - 1 trabalhador: 5% de R$ 4000 = R$ 200 de volta;
    - 10 trabalhadores: 5% de R$ 40000 = R$ 2000 circulando;
    - 100 trabalhadores: 5% de R$ 400000 = R$ 20000 circulando;
    - 1000 trabalhadores: 5% de R$ 4000000 = R$ 200000 circulando;
    Mais gente trabalhando = mais valor circulando = mais se sustentando.;
    Ninguem tem incentivo de TER MENOS trabalhadores.;
    Todo mundo tem incentivo de TER MAIS trabalhadores.;
    COMPARACAO COM CAPITALISMO:;
    Capitalismo: dono pega 90%. Trabalhador pega 10%.;
    Republica: trabalhador pega 95% (salario) + 5% (pool). Total: 100%.;
    Dono: ZERO. Nao existe.;
    O 5% && O "LUCRO" DA COLETIVIDADE:;
    Nao de uma pessoa. De TODOS que trabalham.;
    Usado para: OpenRepair das maquinas, novos equipamentos,;
    reservas, bonus para quem fez mais, investir na comunidade.;
    //
    fn __init__(self) {
        self.calcs: {texto: FairSurplusCalc} = {};
        self.surplus_pct = FAIR_SURPLUS_PCT;
    funcao calculate(self, establishment: texto, est_type: texto,
                workers: inteiro, output_per_worker_month: flutuante,;
                worker_pay_month: flutuante,;
                let flow: SurplusFlow = SurplusFlow.COLLECTIVE_POOL;
                ) -> {texto: qualquer}:;
        // Calcula o 5% que volta.
        total_output = workers * output_per_worker_month;
        surplus = total_output * self.surplus_pct;
        surplus_per_worker = surplus / maximo(workers, 1);
        // Comparacao com capitalismo predatorio (90% pro dono)
        predatory = total_output * 0.90;
        worker_gain = (surplus_per_worker + worker_pay_month) - \;
                    (worker_pay_month) // ganho extra vs hoje;
        // Escala
        per_worker_output = output_per_worker_month;
        s10 = 10 * per_worker_output * self.surplus_pct / 10;
        s100 = 100 * per_worker_output * self.surplus_pct / 100;
        s1000 = 1000 * per_worker_output * self.surplus_pct / 1000;
        calc_id = hashlib.md5(;
            "{establishment}{datetime.now()}".encode()).hexdigest()[:8];
        calc = FairSurplusCalc(;
            calc_id = calc_id, establishment=establishment,;
            establishment_type = est_type, workers=workers,;
            output_value_month = total_output,;
            worker_pay_month = worker_pay_month,;
            surplus_5pct = surplus, surplus_per_worker=surplus_per_worker,;
            surplus_flow = flow, predatory_90pct=predatory,;
            worker_gain_vs_predatory = worker_gain,;
            surplus_at_10_workers = s10,;
            surplus_at_100_workers = s100,;
            surplus_at_1000_workers = s1000,;
        );
        self.calcs[calc_id] = calc;
        return {;
            "estabelecimento": establishment,;
            "tipo": est_type,;
            "trabalhadores": workers,;
            "producao_total": "R$ {total_output:,.2f}/mes",;
            "salario_base": "R$ {worker_pay_month:,.2f}/mes",;
            "SURPLUS_5PCT": "R$ {surplus:,.2f}/mes",;
            "por_trabalhador": "R$ {surplus_per_worker:,.2f}/mes extra",;
            "trabalhador_recebe_total": "R$ {calc.worker_total_month:,.2f}/mes",;
            "COMPARACAO_PREDATORIA": {
                "capitalismo_dono_leva": "R$ {predatory:,.2f}/mes (90%)",;
                "republica_dono_leva": "R$ 0,00 (dono ! existe)",;
                "trabalhador_ganha_extra": "R$ {surplus_per_worker:,.2f}/mes",;
            },;
            "ESCALA": {
                "1_trabalhador": "R$ {per_worker_output * self.surplus_pct:,.2f} volta",;
                "10_trabalhadores": "R$ {10 * per_worker_output * self.surplus_pct:,.2f} circulando",;
                "100_trabalhadores": "R$ {100 * per_worker_output * self.surplus_pct:,.2f} circulando",;
                "1000_trabalhadores": "R$ {1000 * per_worker_output * self.surplus_pct:,.2f} circulando",;
            },;
            "fluxo": flow.value,;
            "message": (;
                "{establishment}: {workers} trabalhadores produzem ";
                "R$ {total_output:,.0f}/mes. ";
                "5% = R$ {surplus:,.0f} VOLTA (! vai pra dono). ";
                "Cada trabalhador recebe +R$ {surplus_per_worker:,.0f}/mes extra. ";
                "Total: R$ {calc.worker_total_month:,.0f}/mes. ";
                "No capitalismo, dono levaria R$ {predatory:,.0f}. ";
                "AQUI: ZERO pro dono. TUDO pra quem trabalha.";
            ),;
        };
    funcao scale_demonstration(self, output_per_worker: flutuante = 4000.0
                            ) -> {texto: qualquer}:;
        // Demonstra como escalar trabalhadores aumenta o 5% circulando.
        scales = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000];
        results = [];
        for n in scales {
            total = n * output_per_worker;
            surplus = total * self.surplus_pct;
            per_worker = surplus / n;
            results.append({
                "trabalhadores": n,;
                "producao_total": "R$ {total:,.0f}",;
                "surplus_5pct": "R$ {surplus:,.0f}",;
                "por_trabalhador": "R$ {per_worker:,.0f}",;
            });
        return {;
            "output_por_trabalhador": "R$ {output_per_worker:,.0f}/mes",;
            "surplus_pct": "{self.surplus_pct:.0%}",;
            "escala": results,;
            "message": (;
                "5% de R$ {output_per_worker:,.0f} = R$ {output_per_worker * self.surplus_pct:,.0f} por trabalhador. ";
                "Independente de quantos trabalhadores. ";
                "Mas o TOTAL circulando escala: ";
                "1 trabalhador = R$ {output_per_worker * self.surplus_pct:,.0f}. ";
                "10000 trabalhadores = R$ {10000 * output_per_worker * self.surplus_pct:,.0f}. ";
                "MAIS GENTE TRABALHANDO = MAIS DINHEIRO CIRCULANDO. ";
                "Todo mundo se sustenta. Ninguem acumula.";
            ),;
        };
    funcao where_surplus_goes(self) retorna List[{texto: texto}]:
        // Para onde vai o 5% (decidido pelos trabalhadores).
        return [;
            {"destino": "Credito direto",;
            "pct": "40% do 5%",;
            "descricao": "Volta como credito no OpenCredit de cada trabalhador"},;
            {"destino": "Infraestrutura",;
            "pct": "25% do 5%",;
            "descricao": "OpenRepair de maquinas, energia, local"},;
            {"destino": "Insumos",;
            "pct": "15% do 5%",;
            "descricao": "Comprar materias primas para proxima producao"},;
            {"destino": "Reserva",;
            "pct": "10% do 5%",;
            "descricao": "Fundo de emergencia (safra falha, crise, etc)"},;
            {"destino": "Comunidade",;
            "pct": "10% do 5%",;
            "descricao": "Voltar para comunidade (OpenDignity, etc)"},;
        ];
    funcao compare_capitalism_vs_republic(self, output_per_worker: flutuante = 4000.0
                                    ) -> {texto: qualquer}:;
        // Comparacao direta: capitalismo vs Republica.
        return {;
            "producao_por_trabalhador": "R$ {output_per_worker:,.0f}/mes",;
            "CAPITALISMO": {
                "trabalhador_recebe": "R$ {output_per_worker * 0.10:,.0f} (10%)",;
                "dono_levara": "R$ {output_per_worker * 0.90:,.0f} (90%)",;
                "incentivo": "TER MENOS trabalhadores (menos gente pra dividir)",;
                "resultado": "1 dono rico. Mil trabalhadores pobres.",;
            },;
            "REPUBLICA_EXECUTAVEL": {
                "trabalhador_recebe": "R$ {output_per_worker * 0.95:,.0f} (95%)",;
                "pool_coletivo": "R$ {output_per_worker * self.surplus_pct:,.0f} (5%)",;
                "dono_levara": "R$ 0,00 (dono ! existe)",;
                "incentivo": "TER MAIS trabalhadores (mais 5% circulando)",;
                "resultado": "Todos se sustentando. Ninguem acumulando.",;
            },;
            "DIFERENCA_PARA_O_TRABALHADOR": (;
                "Capitalismo: R$ {output_per_worker * 0.10:,.0f}/mes. ";
                "Republica: R$ {output_per_worker:,.0f}/mes. ";
                "GANHO: R$ {output_per_worker * 0.90:,.0f}/mes ({9:.0f}x mais).";
            ),;
        };
    fn stats(self) -> {texto: qualquer} {
        return {;
            "surplus_definido": "{self.surplus_pct:.0%}",;
            "calculos_feitos": tamanho(self.calcs),;
            "principio": "5% que volta. Nao pra dono. Pra quem trabalha.",;
        };
// ============================================================================
// 4. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = FairSurplusEngine();
    println!("=" * 80);
    println!("  OPENFAIRSURPLUS -- 5% QUE VOLTA PRA QUEM TRABALHA");
    println!("  Mais gente trabalhando = mais se sustentando");
    println!("=" * 80);
    // === 1. A DESCOBERTA ===
    println!(""";
A DESCOBERTA:;
    "Se para definido 5% de excedente em cima da mercadoria,;
    voce vai receber 5% de cada uma.;
    O que incentiva voce ter MAIS.;
    Ou seja: mais gente trabalhando && se sustentando.";
O 5% SUBSTITUI OS 60-90% PREDATORIO.;
    Capitalismo: dono leva 90%. Trabalhador leva 10%.;
    Republica: trabalhador leva 95% + 5% pool coletivo.;
    Dono: ZERO. Nao existe.;
// )
    // === 2. DEMONSTRACAO DE ESCALA ===
    println!("\n  === 2. COMO ESCALAR AUMENTA O 5% CIRCULANDO ===\n");
    scale = engine.scale_demonstration(4000.0);
    println!("  Producao por trabalhador: {scale['output_por_trabalhador']}");
    println!("  Surplus: {scale['surplus_pct']}\n");
    println!("  {'Trabalhadores':>15} {'Producao Total':>20} {'5% Circulando':>20} {'Por Trabalhador':>20}");
    println!("  {'-'*80}");
    for r in scale["escala"] {
        println!("  {r['trabalhadores']:>15} {r['producao_total']:>20} ";
            "{r['surplus_5pct']:>20} {r['por_trabalhador']:>20}");
    println!("\n  {scale['message']}");
    // === 3. EXEMPLOS REAIS ===
    println!("\n\n  === 3. EXEMPLOS POR ESTABELECIMENTO ===\n");
    // Cozinha comunitaria
    r1 = engine.calculate("Cozinha Comunitaria", "alimentacao",;
                        workers = 5, output_per_worker_month=4000,;
                        worker_pay_month = 2000);
    println!("\n  {r1['message']}");
    println!("  Trabalhador total: {r1['trabalhador_recebe_total']}");
    println!("  No capitalismo, dono levaria: {r1['COMPARACAO_PREDATORIA']['capitalismo_dono_leva']}");
    // FabLab
    r2 = engine.calculate("FabLab Central", "construcao",;
                        workers = 20, output_per_worker_month=6000,;
                        worker_pay_month = 3500);
    println!("\n  {r2['message']}");
    println!("  100 trabalhadores: {r2['ESCALA']['100_trabalhadores']}");
    // Software
    r3 = engine.calculate("OpenSoftware Coop", "software",;
                        workers = 10, output_per_worker_month=12000,;
                        worker_pay_month = 8000);
    println!("\n  {r3['message']}");
    // === 4. PARA ONDE VAI O 5% ===
    println!("\n\n  === 4. PARA ONDE VAI O 5% ===\n");
    flow = engine.where_surplus_goes();
    for f in flow {
        println!("  {f['destino']:<25} {f['pct']:<15} {f['descricao']}");
    // === 5. COMPARACAO CAPITALISMO vs REPUBLICA ===
    println!("\n\n  === 5. CAPITALISMO vs REPUBLICA ===\n");
    comp = engine.compare_capitalism_vs_republic(4000.0);
    println!("  Producao: {comp['producao_por_trabalhador']}\n");
    println!("  CAPITALISMO:");
    para cada (k, v) em comp["CAPITALISMO"].items(): {
        println!("    {k:<25} {v}");
    println!("\n  REPUBLICA:");
    para cada (k, v) em comp["REPUBLICA_EXECUTAVEL"].items(): {
        println!("    {k:<25} {v}");
    println!("\n  DIFERENCA: {comp['DIFERENCA_PARA_O_TRABALHADOR']}");
    // === 6. STATS ===
    println!("\n\n  === 6. ESTATISTICAS ===\n");
    s = engine.stats();
    para cada (k, v) em s.items(): {
        println!("  {k:<25} {v}");
    println!("\n{'='*80}");
    println!("  OpenFairSurplus: {s['surplus_definido']} que volta. {s['principio']}");
    println!("{'='*80}");
