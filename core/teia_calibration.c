/* TEIA Parameter Calibration -- Como Estabelecer os Parametros Objetivamente -- gerado de Portugol++ */
#ifndef TEIA_PARAMETER_CALIBRATION_COMO_ESTABELECER_OS_PARAMETROS_OBJETIVAMENTE_H
#define TEIA_PARAMETER_CALIBRATION_COMO_ESTABELECER_OS_PARAMETROS_OBJETIVAMENTE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
TEIA Parameter Calibration -- Como Estabelecer os Parametros Objetivamente;
============================================================================;
O PROBLEMA:;
Os scores (escassez, demanda, etc) sao OPINIAO ate virarem METODO.;
Opiniao ! escala. Metodo escala.;
A SOLUCAO: 4 CAMADAS DE CALIBRACAO;
CAMADA 1: CUSTO DE REPLICACAO (piso objetivo);
    Quanto custaria para alguem refazer este dado do zero?;
    Se custa R$50k para replicar, ! faz sentido cobrar R$0,05.;
CAMADA 2: PRECO DE MERCADO COMPARAVEL (teto objetivo);
    Quanto FGV/Tendencias/McKinsey cobram pelo mesmo tipo de dado?;
    TEIA ! precisa ser mais barato que commodity nem mais caro que premium.;
CAMADA 3: FEEDBACK DE MERCADO (ajuste dinamico);
    Depois de 30 dias online, os DADOS REAIS falam:;
    - Endpoint com muitas chamadas = demanda alta -> pode subir;
    - Endpoint com zero chamadas = ninguem quer -> baixar || matar;
    - Elasticidade: subir 10% no preco cai quanto a demanda?;
CAMADA 4: GOVERNANCA DEMOCRATICA (override);
    A Assembleia pode ajustar qualquer parametro.;
    Nenhum preco && definitivo. Todos sao revistos.;
Author: TEIA / OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// ============================================================================
// 1. CUSTO DE REPLICACAO (piso objetivo)
// ============================================================================
// decorador: @dataclass
typedef struct ReplicationCost {
    // Quanto custaria para refazer este dado do zero.
    Este && o PISO. Ninguem paga mais que o custo de replicar.;
    Se TEIA cobra R$0,10/chamada mas replicar custa R$50k,;
    o cliente so paga R$0,10 se para mais barato que fazer sozinho.;
    //
    // Componentes de custo (em horas de trabalho senior)
    double data_collection_hours = 0 // baixar/coletar;
    double data_cleaning_hours = 0 // limpar/normalizar;
    double cross_referencing_hours = 0 // cruzar com outros;
    double model_building_hours = 0 // construir modelo;
    double documentation_hours = 0 // documentar;
    double fact_checking_hours = 0 // verificar;
    double engineering_hours = 0 // construir API/endpoint;
    // Custo/hora de um profissional senior no Brasil (R$)
    double senior_rate_brl = 200.0 // R$200/h (Data Engineer senior);
    // decorador: @property
    double total_hours(self) {
        return (self.data_collection_hours + self.data_cleaning_hours +;
                self.cross_referencing_hours + self.model_building_hours +;
                self.documentation_hours + self.fact_checking_hours +;
                self.engineering_hours);
    // decorador: @property
    double total_cost_brl(self) {
        return self.total_hours * self.senior_rate_brl;
    // decorador: @property
    double floor_price_per_call(self) {
        // Preco minimo por chamada para recuperar custo em N chamadas.
        Assumindo 10.000 chamadas no ciclo de vida do endpoint.;
        //
        expected_calls = 10_000;
        return self.total_cost_brl / expected_calls;
// Custos de replicacao estimados para cada dataset
{texto: ReplicationCost} REPLICATION_COSTS = {;
    "/api/v1/politica/impacto-fiscal": ReplicationCost(;
        data_collection_hours = 80, // coletar dados de 35 politicas;
        data_cleaning_hours = 40,;
        cross_referencing_hours = 60, // cruzar 35 politicas entre si;
        model_building_hours = 120, // construir 35 modelos de impacto fiscal;
        documentation_hours = 40,;
        fact_checking_hours = 60,;
        engineering_hours = 20,;
    ),;
    // Total: 420h x R$200 = R$84.000 para replicar
    "/api/v1/fome/por-municipio": ReplicationCost(;
        data_collection_hours = 20, // baixar VIGISAN;
        data_cleaning_hours = 30,;
        cross_referencing_hours = 40, // cruzar com CADunico;
        model_building_hours = 20,;
        documentation_hours = 10,;
        fact_checking_hours = 15,;
        engineering_hours = 10,;
    ),;
    // Total: 145h x R$200 = R$29.000
    "/api/v1/simular/paa": ReplicationCost(;
        data_collection_hours = 15,;
        data_cleaning_hours = 10,;
        cross_referencing_hours = 25,;
        model_building_hours = 50, // modelo multiplicador PAA && complexo;
        documentation_hours = 10,;
        fact_checking_hours = 20,;
        engineering_hours = 15,;
    ),;
    // Total: 145h x R$200 = R$29.000
    "/api/v1/simular/selic": ReplicationCost(;
        data_collection_hours = 10,;
        data_cleaning_hours = 5,;
        cross_referencing_hours = 10,;
        model_building_hours = 40,;
        documentation_hours = 8,;
        fact_checking_hours = 15,;
        engineering_hours = 15,;
    ),;
    // Total: 103h x R$200 = R$20.600
    "/api/v1/juros/impacto-orcamento": ReplicationCost(;
        data_collection_hours = 10,;
        data_cleaning_hours = 5,;
        cross_referencing_hours = 10,;
        model_building_hours = 30,;
        documentation_hours = 8,;
        fact_checking_hours = 10,;
        engineering_hours = 10,;
    ),;
    // Total: 83h x R$200 = R$16.600
    "/api/v1/negativados/perfil": ReplicationCost(;
        data_collection_hours = 15, // SPC ! && gratis;
        data_cleaning_hours = 20,;
        cross_referencing_hours = 15,;
        model_building_hours = 10,;
        documentation_hours = 5,;
        fact_checking_hours = 10,;
        engineering_hours = 8,;
    ),;
    // Total: 83h x R$200 = R$16.600
    "/api/v1/saneamento/cobertura": ReplicationCost(;
        data_collection_hours = 10,;
        data_cleaning_hours = 15,;
        cross_referencing_hours = 10,;
        model_building_hours = 10,;
        documentation_hours = 5,;
        fact_checking_hours = 8,;
        engineering_hours = 8,;
    ),;
    // Total: 66h x R$200 = R$13.200
    "/api/v1/emprego/caged": ReplicationCost(;
        data_collection_hours = 4, // CAGED && trivial de baixar;
        data_cleaning_hours = 8,;
        cross_referencing_hours = 2,;
        model_building_hours = 0,;
        documentation_hours = 3,;
        fact_checking_hours = 2,;
        engineering_hours = 5,;
    ),;
    // Total: 24h x R$200 = R$4.800
    "/api/v1/educacao/inep": ReplicationCost(;
        data_collection_hours = 4,;
        data_cleaning_hours = 6,;
        cross_referencing_hours = 2,;
        model_building_hours = 0,;
        documentation_hours = 3,;
        fact_checking_hours = 2,;
        engineering_hours = 5,;
    ),;
    // Total: 22h x R$200 = R$4.400
    "/api/v1/saude/datasus": ReplicationCost(;
        data_collection_hours = 3,;
        data_cleaning_hours = 5,;
        cross_referencing_hours = 2,;
        model_building_hours = 0,;
        documentation_hours = 2,;
        fact_checking_hours = 2,;
        engineering_hours = 5,;
    ),;
    // Total: 19h x R$200 = R$3.800
};
// ============================================================================
// 2. PRECO DE MERCADO COMPARAVEL (teto objetivo)
// ============================================================================
// decorador: @dataclass
typedef struct MarketComparable {
    // O que o mercado cobra por dados/inteligencia similar.
    Fontes reais:;
    - FGV: R$50-200k por estudo economico;
    - Tendencias Consultoria: R$80-300k por dossie setorial;
    - McKinsey: $200k-1M+ por strategy report;
    - TCU: gratuito mas so para auditores;
    - IPEA: gratuito mas tempo de espera = anos;
    - Serasa Experian: R$5-50k por relatorio setorial;
    - LCA Consultores: R$50-150k por parecer;
    - Sun-King Research: $50-200k por due diligence;
    //
    comparable_id: texto;
    provider: texto;
    product_type: texto;
    price_brl: flutuante;
    delivery_time_weeks: flutuante;
    quality: texto   // "premium", "alto", "medio", "basico";
    note: texto;
[MarketComparable] MARKET_COMPARABLES = [;
    // ESTUDOS DE IMPACTO FISCAL (comparavel ao DIAMANTE TEIA)
    MarketComparable(;
        "MC01", "FGV", "Estudo impacto fiscal", 150_000, 8, "premium",;
        "FGV cobra R$150k por estudo de impacto de UMA politica. TEIA tem 35.";
    ),;
    MarketComparable(;
        "MC02", "Tendencias Consultoria", "Dossie setorial", 200_000, 6, "premium",;
        "Tendencias cobra R$200k por dossie de UM setor. TEIA tem 16.";
    ),;
    MarketComparable(;
        "MC03", "LCA Consultores", "Parecer economico", 80_000, 4, "alto",;
        "LCA cobra R$80k por parecer sobre tributacao/financas.";
    ),;
    MarketComparable(;
        "MC04", "McKinsey & Company", "Strategy report", 500_000, 12, "premium",;
        "McKinsey: $100k+ (R$500k) por relatorio estrategico para governo/empresa.";
    ),;
    // DADOS SETORIAIS (comparavel ao OURO/PRATA TEIA)
    MarketComparable(;
        "MC05", "Serasa Experian", "Relatorio de credito setorial", 30_000, 2, "alto",;
        "Serasa vende relatorio de inadimplencia por R$30k.";
    ),;
    MarketComparable(;
        "MC06", "Datafolha", "Pesquisa de opiniao publica", 80_000, 2, "alto",;
        "Datafolha: R$80k por pesquisa nacional.";
    ),;
    MarketComparable(;
        "MC07", "Ibope/IPSOS", "Estudo de mercado", 50_000, 3, "alto",;
        "Ibope: R$50k por estudo setorial.";
    ),;
    // DADOS PUBLICOS COM VALOR AGREGADO
    MarketComparable(;
        "MC08", "TCU", "Auditoria tecnica", 0, 26, "premium",;
        "TCU faz gratuito mas so quando pede. Tempo = anos. So membros TCU.";
    ),;
    MarketComparable(;
        "MC09", "IPEA", "Estudo de politica publica", 0, 52, "alto",;
        "IPEA gratuito mas 1 ano de espera. TEIA entrega em dias.";
    ),;
    // DUE DILIGENCE
    MarketComparable(;
        "MC10", "Big4 (PwC/Deloitte/EY/KPMG)", "Due diligence", 200_000, 8, "premium",;
        "Big4 cobra R$200k+ por due diligence regulatoria.";
    ),;
];
// ============================================================================
// 3. FEEDBACK DE MERCADO (ajuste dinamico)
// ============================================================================
// decorador: @dataclass
typedef struct MarketFeedback {
    // Dados reais de uso apos lancamento da API.
    Depois de 30 dias online, estes numeros revelam a demanda REAL.;
    Antes disso, tudo && estimativa.;
    //
    endpoint: texto;
    int calls_last_30_days = 0;
    int unique_callers = 0;
    double revenue_30_days = 0.0;
    // Para calcular elasticidade (apos mudanca de preco)
    int calls_before_price_change = 0;
    int calls_after_price_change = 0;
    double price_change_pct = 0;
    // Conversao
    int free_tier_users = 0;
    double free_to_paid_conversion = 0 // %;
typedef struct DynamicPricer {
    // Ajusta precos baseado em dados REAIS de uso.
    REGRAS DE AJUSTE:;
    1. SE chamadas/dia > 100 && unique_callers > 10:;
    -> Demanda alta. Pode SUBIR 10%.;
    2. SE chamadas/dia < 5 && unique_callers < 3:;
    -> Demanda baixa. BAIXAR 20% || KILL.;
    3. SE free_tier_users > 50 mas free_to_paid < 2%:;
    -> Preco pago alto demais. BAIXAR 15%.;
    4. SE free_to_paid > 10%:;
    -> Preco bom. MANTER.;
    5. Elasticidade-preco:;
    SE subir 10% reduz demanda < 5% -> INELASTICO -> pode subir mais;
    SE subir 10% reduz demanda > 20% -> ELASTICO -> ! subir;
    //
    // decorador: @staticmethod
    funcao compute_adjustment(
        feedback: MarketFeedback,;
        current_token_cost: flutuante,;
        floor_price: flutuante,;
    ) -> (flutuante, texto):;
        // Retorna (novo_preco, razao).
        calls_per_day = feedback.calls_last_30_days / 30;
        // Caso 1: sem dados ainda
        if (feedback.calls_last_30_days == 0) {
            return current_token_cost, "SEM DADOS (manter ate ter 30 dias de trafego)";
        // Caso 2: demanda alta
        if (calls_per_day > 100 && feedback.unique_callers > 10) {
            new_price = current_token_cost * 1.10;
            return new_price, (;
                "DEMANDA ALTA ({calls_per_day:.0f}/dia, {feedback.unique_callers} clientes). ";
                "Subir 10%.";
            );
        // Caso 3: demanda baixa
        if (calls_per_day < 5 && feedback.unique_callers < 3) {
            new_price = current_token_cost * 0.80;
            if (new_price < floor_price * 2) {
                return current_token_cost * 0.5, (;
                    "DEMANDA MORTA ({calls_per_day:.0f}/dia). ";
                    "Baixar 50%. Considerar KILL.";
                );
            return new_price, (;
                "DEMANDA BAIXA ({calls_per_day:.0f}/dia). Baixar 20%.";
            );
        // Caso 4: elasticidade
        if (feedback.price_change_pct != 0 && feedback.calls_before_price_change > 0) {
            demand_change = (;
                (feedback.calls_after_price_change - feedback.calls_before_price_change);
                / feedback.calls_before_price_change * 100;
            );
            elasticity = abs(demand_change / feedback.price_change_pct);
            if (elasticity < 0.5) {
                return current_token_cost * 1.15, (;
                    "INELASTICO (elasticidade={elasticity:.2f}). ";
                    "Demanda pouco sensivel a preco. Subir 15%.";
                );
            } else if (elasticity > 2.0) {
                return current_token_cost * 0.90, (;
                    "MUITO ELASTICO (elasticidade={elasticity:.2f}). ";
                    "Demanda foge com preco alto. Baixar 10%.";
                );
        // Caso 5: conversao free -> paid
        if (feedback.free_tier_users > 20) {
            if (feedback.free_to_paid < 0.02) {
                return current_token_cost * 0.85, (;
                    "CONVERSAO BAIXA ({feedback.free_to_paid:.1%}). ";
                    "Preco pago alto demais. Baixar 15%.";
                );
            } else if (feedback.free_to_paid > 0.10) {
                return current_token_cost, (;
                    "CONVERSAO BOA ({feedback.free_to_paid:.1%}). Manter.";
                );
        return current_token_cost, "MANTER (dentro dos parametros)";
// ============================================================================
// 4. SISTEMA DE CALIBRACAO COMPLETO
// ============================================================================
// decorador: @dataclass
typedef struct CalibratedPrice {
    // Preco final calibrado pelas 4 camadas.
    endpoint: texto;
    current_token_cost: flutuante;
    // Camada 1: piso
    replication_cost_brl: flutuante;
    floor_token_cost: flutuante;
    // Camada 2: teto de mercado
    market_comparable_price: flutuante;
    ceiling_token_cost: flutuante;
    // Camada 3: feedback (preenchido apos 30 dias)
    flutuante? feedback_adjustment = NULL;
    char* feedback_reason = "SEM DADOS AINDA";
    // Camada 4: governance
    flutuante? assembly_override = NULL;
    char* assembly_reason = "";
    // decorador: @property
    double calibrated_token_cost(self) {
        // Preco final apos todas as camadas.
        if (self.assembly_override && ! None) {
            return self.assembly_override;
        if (self.feedback_adjustment && ! None) {
            return self.feedback_adjustment;
        // Default: ponto medio entre piso e teto
        return (self.floor_token_cost + self.ceiling_token_cost) / 2;
    // decorador: @property
    double calibrated_price_brl(self) {
        return self.calibrated_token_cost * 0.10;
[CalibratedPrice] calibrate_all(void) {
    // Calibra todos os endpoints.
    // Mapeamento: endpoint -> comparable
    comparable_map = {
        "/api/v1/politica/impacto-fiscal": ("MC01", 150_000),   // FGV;
        "/api/v1/simular/paa": ("MC01", 120_000),;
        "/api/v1/simular/selic": ("MC03", 80_000),    // LCA;
        "/api/v1/juros/impacto-orcamento": ("MC03", 80_000),;
        "/api/v1/fome/por-municipio": ("MC09", 0),     // IPEA gratuito mas 1 ano;
        "/api/v1/negativados/perfil": ("MC05", 30_000),   // Serasa;
        "/api/v1/saneamento/cobertura": ("MC09", 0),;
        "/api/v1/emprego/caged": (NULL, 0),;
        "/api/v1/educacao/inep": (NULL, 0),;
        "/api/v1/saude/datasus": (NULL, 0),;
    };
    current_costs = {
        "/api/v1/politica/impacto-fiscal": 2.5,;
        "/api/v1/simular/paa": 2.0,;
        "/api/v1/simular/selic": 2.0,;
        "/api/v1/juros/impacto-orcamento": 1.5,;
        "/api/v1/fome/por-municipio": 1.0,;
        "/api/v1/negativados/perfil": 0.8,;
        "/api/v1/saneamento/cobertura": 0.8,;
        "/api/v1/emprego/caged": 0.5,;
        "/api/v1/educacao/inep": 0.5,;
        "/api/v1/saude/datasus": 0.8,;
    };
    results = [];
    /* para cada (endpoint, rc) em REPLICATION_COSTS.items(): */
        current = current_costs.get(endpoint, 1.0);
        desempacote comp_id, comp_price = comparable_map.get(endpoint, (NULL, 0));
        // Piso: custo de replicacao / 10.000 chamadas esperadas
        floor_brl = rc.floor_price_per_call;
        floor_tokens = floor_brl / 0.10;
        // Teto: preco de mercado / chamadas equivalentes
        // Assumindo que 1 estudo de FGV = 500 chamadas API equivalentes
        if (comp_price > 0) {
            ceiling_brl = comp_price / 500;
            ceiling_tokens = ceiling_brl / 0.10;
        } else {
            // Sem comparable: teto = 5x piso
            ceiling_brl = floor_brl * 5;
            ceiling_tokens = floor_tokens * 5;
        results.append(CalibratedPrice(;
            endpoint = endpoint,;
            current_token_cost = current,;
            replication_cost_brl = rc.total_cost_brl,;
            floor_token_cost = floor_tokens,;
            market_comparable_price = comp_price,;
            ceiling_token_cost = ceiling_tokens,;
        ));
    return results;
// ============================================================================
// 5. RELATORIO
// ============================================================================
char* print_calibration(void) {
    lines = [];
    lines.append("=" * 120);
    lines.append("TEIA -- COMO ESTABELECER OS PARAMETROS DE PRECO");
    lines.append("4 Camadas de Calibracao: Nada && Opiniao. Tudo && Metodo.");
    lines.append("=" * 120);
    lines.append("");
    // === METODOLOGIA ===
    lines.append("AS 4 CAMADAS:");
    lines.append("-" * 120);
    lines.append("");
    lines.append("  CAMADA 1: CUSTO DE REPLICA o (piso)");
    lines.append("    'Quanto custaria para alguem refazer este dado do zero?'");
    lines.append("    Horas de trabalho senior x R$200/h = custo total");
    lines.append("    Custo / 10.000 chamadas = preco piso por chamada");
    lines.append("    NINGUEM paga mais que o custo de fazer sozinho.");
    lines.append("");
    lines.append("  CAMADA 2: PRECO DE MERCADO COMPARAVEL (teto)");
    lines.append("    'Quanto FGV/Tendencias/McKinsey cobram pelo mesmo?'");
    lines.append("    TEIA ! precisa ser mais barato que commodity.");
    lines.append("    TEIA ! deve ser mais caro que premium equivalente.");
    lines.append("");
    lines.append("  CAMADA 3: FEEDBACK DE MERCADO (ajuste dinamico)");
    lines.append("    'Depois de 30 dias, o que os DADOS REAIS dizem?'");
    lines.append("    - 100+ chamadas/dia = demanda alta -> subir 10%");
    lines.append("    - <5 chamadas/dia = ninguem quer -> baixar || matar");
    lines.append("    - Elasticidade: subir 10% cai quanto a demanda?");
    lines.append("    - Conversao: free -> paid = quantos %?");
    lines.append("");
    lines.append("  CAMADA 4: GOVERNANCA DEMOCRATICA (override)");
    lines.append("    'A Assembleia pode ajustar qualquer preco.'");
    lines.append("    Override democratico para casos especiais.");
    lines.append("    Exemplo: dado sobre fome pode ter preco subsidado por P1.");
    lines.append("");
    // === CAMADA 1: CUSTO DE REPLICA o ===
    lines.append("-" * 120);
    lines.append("CAMADA 1: CUSTO DE REPLICAO (piso por endpoint)");
    lines.append("-" * 120);
    lines.append("");
    lines.append("{'ENDPOINT':<38} {'HORAS':>7} {'CUSTO R$':>12} {'PISO/CALL':>10} {'PISO TOKENS':>12}");
    lines.append("-" * 120);
    /* para cada (endpoint, rc) em ordene(REPLICATION_COSTS.items(), key=(x) -> x[1].total_cost_brl, reverse=True): */
        lines.append(;
            "{endpoint:<38} ";
            "{rc.total_hours:>5.0f}h  ";
            "R${rc.total_cost_brl:>9,.0f}  ";
            "R${rc.floor_price_per_call:>7.4f}  ";
            "{rc.floor_price_per_call/0.10:>10.2f} T";
        );
    lines.append("");
    // === CAMADA 2: MERCADO COMPARAVEL ===
    lines.append("-" * 120);
    lines.append("CAMADA 2: PRECO DE MERCADO COMPARAVEL");
    lines.append("-" * 120);
    lines.append("");
    lines.append("{'PROVEDOR':<25} {'PRODUTO':<30} {'PRECO R$':>12} {'PRAZO':>8} {'QUALIDADE'}");
    lines.append("-" * 120);
    /* TODO: iterador C manual para mc em MARKET_COMPARABLES */
        lines.append(;
            "{mc.provider:<25} ";
            "{mc.product_type:<30} ";
            "R${mc.price_brl:>9,.0f}  ";
            "{mc.delivery_time_weeks:>5.0f}sem ";
            "{mc.quality}";
        );
    lines.append("");
    lines.append("  ANCHOR DE PRECO: TEIA entrega o que FGV cobra R$150k por R$0,25/chamada.");
    lines.append("  TEIA ! && mais barato. E OUTRO MODELO (API vs relatorio).");
    lines.append("");
    // === CALIBRACAO FINAL ===
    lines.append("-" * 120);
    lines.append("CALIBRACAO FINAL: PISO x TETO x FEEDBACK x GOVERNANCA");
    lines.append("-" * 120);
    lines.append("");
    calibrated = calibrate_all();
    lines.append("{'ENDPOINT':<38} {'ATUAL':>7} {'PISO':>7} {'TETO':>7} {'MEDIO':>7} {'RECOMENDADO':>12}");
    lines.append("-" * 120);
    /* TODO: iterador C manual para c em ordene(calibrated, key=(x) -> x.calibrated_token_cost, reverse=True) */
        recommended = c.calibrated_token_cost;
        lines.append(;
            "{c.endpoint:<38} ";
            "{c.current_token_cost:>5.1f}T  ";
            "{c.floor_token_cost:>5.1f}T  ";
            "{c.ceiling_token_cost:>5.1f}T  ";
            "{(c.floor_token_cost + c.ceiling_token_cost)/2:>5.1f}T  ";
            "{recommended:>10.1f}T (R${recommended*0.10:.2f})";
        );
    lines.append("");
    // === COMO CADA PARAMETRO E MEDIDO ===
    lines.append("-" * 120);
    lines.append("COMO MEDIR CADA UM DOS 7 PARAMETROS DE VALOR OBJETIVAMENTE");
    lines.append("-" * 120);
    lines.append("");
    params = [;
        ("ESCASSEZ", [;
            "Contar fontes alternativas: 0 = exclusivo (10), 5+ = commodity (1)",;
            "Custo financeiro de obter: gratis = baixo, R$50k+ = alto",;
            "Tempo para obter: 1 clique = baixo, 6 meses = alto",;
            "Metrica: (10 - min(fontes_alternativas, 10))",;
        ]),;
        ("DEMANDA", [;
            "Google Trends do tema (escala 0-100 -> dividir por 10)",;
            "Numero de stakeholders (ministerios, ONGs, jornais que cobrem)",;
            "Apos lancamento: chamadas/dia reais na API",;
            "Metrica: chamadas_dia / 10 (caps em 10)",;
        ]),;
        ("FRESCURA", [;
            "Frequencia de atualizacao da fonte: mensal=10, anual=5, quinquenal=2",;
            "Taxa de mudanca do fenomeno: Selic muda rapido, censo !",;
            "Metrica: frequencia_atualizacao (mensal=10, trimestral=8, anual=5, >2anos=2)",;
        ]),;
        ("EXCLUSIVIDADE", [;
            "TEIA criou o cruzamento/modelo? Sim=10, Nao=1",;
            "Quantos outros provedores oferecem o MESMO produto?",;
            "Existe barreira tecnica (modelos proprios)?",;
            "Metrica: 10 se so TEIA tem, -2 por cada concorrente direto",;
        ]),;
        ("IMPACTO_DE_DECISAO", [;
            "Que decisao o dado habilita? R$ bi = 10, R$ mi = 7, informativo = 3",;
            "Tamanho do orcamento afetado / R$ 10 bi",;
            "Metrica: log10(orcamento_afetado) caps em 10",;
        ]),;
        ("CONEXAO", [;
            "Quantos outros datasets este dado se conecta?",;
            "E no do grafo de dados (degree centrality)",;
            "Metrica: min(conexoes_possiveis, 10)",;
        ]),;
        ("PREVENCAO_DE_RISCO", [;
            "Custo de decisao ERRADA sem este dado",;
            "Vidas em risco = 10, R$ bi perdido = 8, R$ mi = 5, inconveniente = 2",;
            "Metrica: severidade_do_erro (vidas=10, financeiro=escala log)",;
        ]),;
    ];
    /* para cada (pname, methods) em params: */
        lines.append("  {pname}");
        /* TODO: iterador C manual para m em methods */
            lines.append("    -> {m}");
        lines.append("");
    // === REGRA DE OURO ===
    lines.append("-" * 120);
    lines.append("A REGRA DE OURO DA PRECIFICACAO TEIA");
    lines.append("-" * 120);
    lines.append("");
    lines.append("  1. COMECAR com custo de replicacao (piso objetivo)");
    lines.append("  2. LIMITAR por preco de mercado comparavel (teto)");
    lines.append("  3. AJUSTAR por demanda real apos 30 dias (feedback)");
    lines.append("  4. OVERRIDE democratico da Assembleia se necessario");
    lines.append("");
    lines.append("  NUNCA:");
    lines.append("    - Cobrar menos que o piso (desvaloriza trabalho)");
    lines.append("    - Cobrar mais que o teto (cliente replica sozinho)");
    lines.append("    - Manter preco fixo apos feedback (mercado muda)");
    lines.append("    - Decidir preco sozinho sem Assembleia (P1 anti-elitismo)");
    lines.append("");
    lines.append("  SEMPRE:");
    lines.append("    - Revisar trimestralmente");
    lines.append("    - Publicar metodologia (transparencia P4)");
    lines.append("    - Registrar quem contribuiu (royalty chain)");
    lines.append("    - 5% para o pool (LEI)");
    lines.append("");
    lines.append("=" * 120);
    return "\n".join(lines);
// ============================================================================
// 6. EXECUCAO
// ============================================================================
if (__name__ == "__main__") {
    printf(print_calibration());

#endif // TEIA_PARAMETER_CALIBRATION_COMO_ESTABELECER_OS_PARAMETROS_OBJETIVAMENTE_H
