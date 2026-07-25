// TEIA DataValuation -- Nem Todo Dado Vale o Mesmo -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
TEIA DataValuation -- Nem Todo Dado Vale o Mesmo;
==================================================;
Sim. Tem dado que vale MUITO mais que outros.;
7 DIMENSOES DE VALOR DE DADO:;
1. ESCASSEZ -- quao dificil de obter? (IBGE publico = baixo, dado exclusivo = alto);
2. DEMANDA -- quantas pessoas precisam? (fome = todo mundo, nicho = poucos);
3. FRESCURA -- quanto tempo vale? (CAGED mensal = fresco, censo 2017 = velho);
4. EXCLUSIVIDADE -- so TEIA tem? (modelo de impacto fiscal = exclusivo, IBGE = publico);
5. IMPACTO -- que decisao esse dado habilita? (R$ bi = alto, curiosidade = baixo);
6. CONEXAO -- conecta outros datasets? (CADunico cruza com tudo = alto);
7. RISCO -- decisao errada sem ele custa quanto? (saneamento = vidas, lazer = pouco);
Cada dimensao: 0 a 10.;
Score final = media ponderada.;
Token cost = dinamico, baseado no score.;
Author: TEIA / OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa Dict, List, Tuple de typing
// importa Enum de enum
// ============================================================================
// 1. DIMENSOES DE VALOR
// ============================================================================
// decorador: @dataclass
#[derive(Debug, Clone)]
struct DataValueScore {
    // Score de valor de um dataset em 7 dimensoes (0-10 cada).
    scarcity: flutuante // quao dificil de obter;
    demand: flutuante // quantas pessoas precisam;
    freshness: flutuante // quanto tempo vale;
    exclusivity: flutuante // so TEIA tem?;
    decision_impact: flutuante // que decisao habilita;
    connection: flutuante // conecta outros datasets?;
    risk_prevention: flutuante // decisao errada sem ele custa quanto?;
    // Pesos (soma 1.0) -- nem todas dimensoes pesam igual
    WEIGHTS = {
        "scarcity": 0.10,;
        "demand": 0.15,;
        "freshness": 0.10,;
        "exclusivity": 0.20,;
        "decision_impact": 0.20,;
        "connection": 0.10,;
        "risk_prevention": 0.15,;
    };
    // decorador: @property
    fn score(self) -> f64 {
        // Score ponderado 0-10.
        values = {
            "scarcity": self.scarcity,;
            "demand": self.demand,;
            "freshness": self.freshness,;
            "exclusivity": self.exclusivity,;
            "decision_impact": self.decision_impact,;
            "connection": self.connection,;
            "risk_prevention": self.risk_prevention,;
        };
        return soma(values[k] * self.WEIGHTS[k] para k em self.WEIGHTS);
    // decorador: @property
    fn tier(self) -> String {
        // Classificacao de valor.
        s = self.score;
        if s >= 8.0 {
            return "DIAMANTE";
        } else if s >= 6.5 {
            return "OURO";
        } else if s >= 5.0 {
            return "PRATA";
        } else if s >= 3.5 {
            return "BRONZE";
        } else {
            return "COMMODITY";
    // decorador: @property
    fn suggested_token_cost(self) -> f64 {
        // Custo em tokens baseado no score.
        Base: 0.5 tokens (score 0);
        Topo: 10.0 tokens (score 10);
        Curva: exponencial (diamante custa MUITO mais que commodity);
        //
        // Exponencial: dados de alto valor custam proporcionalmente MAIS
        return 0.5 * (2 ** (self.score / 2.5));
    // decorador: @property
    fn suggested_price_brl(self) -> f64 {
        return self.suggested_token_cost * 0.10;
// ============================================================================
// 2. CATALOGO DE DADOS AVALIADOS
// ============================================================================
// decorador: @dataclass
#[derive(Debug, Clone)]
struct ValuatedDataset {
    endpoint: texto;
    description: texto;
    source: texto;
    score: DataValueScore;
    current_token_cost: flutuante;
    why_valuable: texto;
    let why_not_more: String = "";
let DATASETS: [ValuatedDataset] = [;
    // ======================================================================
    // DIAMANTE (score 8+)
    // ======================================================================
    ValuatedDataset(;
        endpoint = "/api/v1/politica/impacto-fiscal",;
        description = "Impacto fiscal de 35 politicas publicas",;
        source = "Modelo TEIA proprietario",;
        score = DataValueScore(;
            scarcity = 9, // so TEIA cruza 35 politicas com modelos;
            demand = 8, // todo governo/ONG precisa;
            freshness = 7, // modelos sao semi-permanentes mas dados atualizam;
            exclusivity = 10, // NINGUEM tem isso pronto no Brasil;
            decision_impact = 10, // habilita decisao de R$ bilhoes;
            connection = 9, // conecta com TODOS os outros datasets;
            risk_prevention = 9, // decisao errada = R$ bi desperdicado;
        ),;
        current_token_cost = 2.5,;
        why_valuable = (;
            "Exclusivo. TEIA && a UNICA fonte no Brasil com 35 politicas ";
            "modeladas com impacto fiscal projetado. Nenhuma consultoria ";
            "tem isso pronto. FGV/Tendencias cobram R$200k+ por UM estudo ";
            "desse. TEIA tem 35.";
        ),;
        why_not_more = "Modelo precisa atualizacao anual quando novos dados saem.",;
    ),;
    ValuatedDataset(;
        endpoint = "/api/v1/simular/paa",;
        description = "Simular impacto de aumentar PAA em R$ X",;
        source = "Modelo TEIA (MDIC/IEPS multiplicador)",;
        score = DataValueScore(;
            scarcity = 8,;
            demand = 7,;
            freshness = 6,;
            exclusivity = 10, // so TEIA modela multiplicador PAA;
            decision_impact = 9, // habilita alocar R$ bi em seguridad alimentar;
            connection = 8,;
            risk_prevention = 8, // errar = 33M na fome;
        ),;
        current_token_cost = 2.0,;
        why_valuable = (;
            "Exclusivo. Modelo proprietario TEIA que cruza PAA x SUS x economia local. ";
            "Mostra que cada R$1 no PAA gera R$4 em economia de saude. ";
            "Nenhum governo tem essa calculadora. So TEIA.";
        ),;
    ),;
    // ======================================================================
    // OURO (score 6.5-8)
    // ======================================================================
    ValuatedDataset(;
        endpoint = "/api/v1/fome/por-municipio",;
        description = "Inseguranca alimentar por municipio (5570 cidades)",;
        source = "VIGISAN/IBGE 2022 + cruzamento CADunico",;
        score = DataValueScore(;
            scarcity = 6, // VIGISAN && publico, mas cruzamento !;
            demand = 10, // TODO MUNDO precisa saber fome;
            freshness = 5, // censo de 2022, atualiza em 5 anos;
            exclusivity = 7, // dado bruto publico, cruzamento && exclusivo;
            decision_impact = 8, // habilita alocar recurso contra fome;
            connection = 9, // cruza com saneamento, educacao, emprego;
            risk_prevention = 9, // errar = pessoas morrem;
        ),;
        current_token_cost = 1.0,;
        why_valuable = (;
            "Alto impacto + alta demanda. Dado bruto (VIGISAN) && publico, ";
            "mas o CRUZAMENTO por municipio com CADunico, saneamento && ";
            "educacao so TEIA fez. Jornalista/prefeito ! consegue sozinho.";
        ),;
        why_not_more = "Dado bruto && publico. Qualquer um pode baixar VIGISAN.",;
    ),;
    ValuatedDataset(;
        endpoint = "/api/v1/juros/impacto-orcamento",;
        description = "Impacto de cada ponto da Selic no orcamento publico",;
        source = "Bacen/STN + modelo TEIA",;
        score = DataValueScore(;
            scarcity = 5, // Bacen && publico;
            demand = 9, // jornalista, deputado, economista;
            freshness = 9, // atualiza todo mes (Selic);
            exclusivity = 7, // modelo de impacto && de TEIA;
            decision_impact = 9, // 1 p.p. Selic = R$31,4 bi;
            connection = 7, // conecta com orcamento, PAA, Bolsa Familia;
            risk_prevention = 8, // ! entender = votar cego;
        ),;
        current_token_cost = 1.5,;
        why_valuable = (;
            "Alta frescura + alto impacto. Todo mes a Selic muda. ";
            "TEIA converte '1 ponto Selic' em 'R$31,4 bi menos para PAA'. ";
            "Ninguem mais faz essa traducao para o publico.";
        ),;
    ),;
    ValuatedDataset(;
        endpoint = "/api/v1/simular/selic",;
        description = "Simular liberacao orcamentaria ao reduzir Selic",;
        source = "Modelo TEIA (Bacen)",;
        score = DataValueScore(;
            scarcity = 7,;
            demand = 8,;
            freshness = 9,;
            exclusivity = 9,;
            decision_impact = 10,;
            connection = 7,;
            risk_prevention = 8,;
        ),;
        current_token_cost = 2.0,;
        why_valuable = (;
            "Simulador que mostra: 'reduzir Selic 3p.p. = R$94bi/ano liberados'. ";
            "Exclusivo TEIA. Parlamentar entende o que significa votar a favor ";
            "de juros altos. Nenhuma outra fonte faz isso em 1 clique.";
        ),;
    ),;
    // ======================================================================
    // PRATA (score 5-6.5)
    // ======================================================================
    ValuatedDataset(;
        endpoint = "/api/v1/negativados/perfil",;
        description = "Perfil de negativados por regiao && renda",;
        source = "SPC/Boa Vista/Peic 2024",;
        score = DataValueScore(;
            scarcity = 7, // SPC ! && gratis, precisa pagar;
            demand = 8, // 63M de negativados = muita gente interessada;
            freshness = 8, // atualiza mensal;
            exclusivity = 5, // SPC vende para varios;
            decision_impact = 7, // habilita politica de renegociacao;
            connection = 6, // cruza com renda;
            risk_prevention = 6,;
        ),;
        current_token_cost = 0.8,;
        why_valuable = (;
            "63M de brasileiros negativados. Dado com demanda altissima. ";
            "Mas SPC ja vende para varios. TEIA adiciona cruzamento por renda.";
        ),;
        why_not_more = "Dado base ja && comercializado por SPC/Serasa.",;
    ),;
    ValuatedDataset(;
        endpoint = "/api/v1/saneamento/cobertura",;
        description = "Cobertura de agua && esgoto por municipio",;
        source = "SNIS/ANA 2024",;
        score = DataValueScore(;
            scarcity = 5, // SNIS && publico;
            demand = 8,;
            freshness = 6, // anual;
            exclusivity = 5,;
            decision_impact = 8, // habilita R$700bi de investimento;
            connection = 7,;
            risk_prevention = 9, // errar = doencas, mortes;
        ),;
        current_token_cost = 0.8,;
        why_valuable = (;
            "Alto impacto em saude publica. Cada R$1 saneamento = R$4 em saude. ";
            "Mas SNIS && publico. Valor do TEIA: cruza com impacto sanitario.";
        ),;
        why_not_more = "SNIS && publico. So o cruzamento && exclusivo.",;
    ),;
    // ======================================================================
    // BRONZE (score 3.5-5)
    // ======================================================================
    ValuatedDataset(;
        endpoint = "/api/v1/emprego/caged",;
        description = "Emprego formal por municipio/setor",;
        source = "CAGED/Min. Trabalho",;
        score = DataValueScore(;
            scarcity = 3, // CAGED && totalmente publico && facil;
            demand = 7, // jornalistas && economistas;
            freshness = 8, // mensal;
            exclusivity = 2, // todo mundo tem CAGED;
            decision_impact = 5, // informativo mas ! habilita decisao direta;
            connection = 6,;
            risk_prevention = 3,;
        ),;
        current_token_cost = 0.5,;
        why_valuable = (;
            "Demanda alta mas zero exclusividade. CAGED && publico, facil de baixar. ";
            "TEIA so adiciona conveniencia (! precisa baixar/limpar).";
        ),;
        why_not_more = "Todo mundo tem. Zero exclusividade. Commodity.",;
    ),;
    ValuatedDataset(;
        endpoint = "/api/v1/educacao/inep",;
        description = "Indicadores educacionais por escola/municipio",;
        source = "INEP",;
        score = DataValueScore(;
            scarcity = 3,;
            demand = 6,;
            freshness = 5, // anual;
            exclusivity = 2,;
            decision_impact = 5,;
            connection = 5,;
            risk_prevention = 4,;
        ),;
        current_token_cost = 0.5,;
        why_valuable = "INEP && publico && facil. Valor do TEIA && so conveniencia.",;
        why_not_more = "Commodity. INEP, QEdu, Todos Pela Educacao ja tem.",;
    ),;
    // ======================================================================
    // COMMODITY (score <3.5)
    // ======================================================================
    ValuatedDataset(;
        endpoint = "/api/v1/saude/datasus",;
        description = "Indicadores de saude por municipio",;
        source = "DATASUS",;
        score = DataValueScore(;
            scarcity = 2, // DATASUS && publico;
            demand = 5,;
            freshness = 4, // lag grande;
            exclusivity = 1, // todo mundo tem;
            decision_impact = 4,;
            connection = 4,;
            risk_prevention = 3,;
        ),;
        current_token_cost = 0.8,;
        why_valuable = "Conveniencia. Dado bruto && publico && facil.",;
        why_not_more = "Commodity pura. DATASUS, DataSUS TabNet, todo portal de transp tem.",;
    ),;
];
// ============================================================================
// 3. RELATORIO
// ============================================================================
fn print_valuation() -> String {
    lines = [];
    lines.append("=" * 115);
    lines.append("TEIA -- VALORACAO DE DADOS: Nem Todo Dado Vale o Mesmo");
    lines.append("=" * 115);
    lines.append("");
    // === AS 7 DIMENSOES ===
    lines.append("AS 7 DIMENSOES DE VALOR DE DADO:");
    lines.append("-" * 115);
    para cada (name, weight) em DataValueScore.WEIGHTS.items(): {
        desc = {
            "scarcity": "Quao dificil de obter. IBGE publico = baixo. Dado exclusivo = alto.",;
            "demand": "Quantas pessoas precisam. Fome = todo mundo. Nicho = poucos.",;
            "freshness": "Quanto tempo vale. CAGED mensal = fresco. Censo 2017 = velho.",;
            "exclusivity": "So TEIA tem? Modelo de impacto = sim. IBGE = !.",;
            "decision_impact": "Que decisao esse dado habilita? R$ bi = alto. Curiosidade = baixo.",;
            "connection": "Conecta outros datasets? CADunico = alto. Isolado = baixo.",;
            "risk_prevention": "Decisao errada sem ele custa quanto? Vidas = alto. Lazer = baixo.",;
        };
        lines.append("  {name:<22} (peso {weight:.0%})  {desc[name]}");
    lines.append("");
    // === RANKING ===
    lines.append("-" * 115);
    lines.append("RANKING DE DADOS POR VALOR");
    lines.append("-" * 115);
    lines.append("");
    // Ordena por score
    ranked = ordene(DATASETS, key=(d) -> d.score.score, reverse=true);
    lines.append("{'TIER':<10} {'SCORE':>6} {'ENDPOINT':<38} {'TOKENS ATUAL':>13} {'TOKENS SUGERIDO':>16} {'R$ SUGERIDO':>12}");
    lines.append("-" * 115);
    for d in ranked {
        s = d.score;
        suggested = s.suggested_token_cost;
        suggested_brl = s.suggested_price_brl;
        lines.append(;
            "{s.tier:<10} ";
            "{s.score:>5.1f}  ";
            "{d.endpoint:<38} ";
            "{d.current_token_cost:>10.1f} T  ";
            "{suggested:>14.1f} T  ";
            "R${suggested_brl:>9.2f}";
        );
    lines.append("");
    // === DETALHE POR TIER ===
    tiers = ["DIAMANTE", "OURO", "PRATA", "BRONZE", "COMMODITY"];
    tier_colors = {
        "DIAMANTE": "MAIS VALIOSO",;
        "OURO": "ALTO VALOR",;
        "PRATA": "VALOR MEDIO",;
        "BRONZE": "BAIXO VALOR",;
        "COMMODITY": "MENOS VALIOSO",;
    };
    for tier in tiers {
        tier_data = [d para d em ranked if d.score.tier == tier];
        if ! tier_data {
            continue;
        lines.append("-" * 115);
        lines.append("  TIER {tier} -- {tier_colors[tier]}");
        lines.append("-" * 115);
        for d in tier_data {
            s = d.score;
            lines.append("");
            lines.append("  {d.endpoint}");
            lines.append("  Score: {s.score:.1f}/10 | Custo atual: {d.current_token_cost}T | Sugerido: {s.suggested_token_cost:.1f}T (R${s.suggested_price_brl:.2f})");
            lines.append("  Fonte: {d.source}");
            lines.append("");
            // Radar de dimensoes
            dims = [;
                ("Escassez", s.scarcity),;
                ("Demanda", s.demand),;
                ("Frescura", s.freshness),;
                ("Exclusiv.", s.exclusivity),;
                ("Impacto", s.decision_impact),;
                ("Conexao", s.connection),;
                ("Risco", s.risk_prevention),;
            ];
            para cada (dim_name, val) em dims: {
                bar = "#" * inteiro(val);
                spaces = "." * (10 - inteiro(val));
                lines.append("    {dim_name:<10} [{bar}{spaces}] {val:.0f}/10");
            lines.append("");
            lines.append("    POR QUE VALE:  {d.why_valuable}");
            if d.why_not_more {
                lines.append("    POR QUE NAO MAIS: {d.why_not_more}");
            lines.append("");
    // === INSIGHT ===
    lines.append("-" * 115);
    lines.append("INSIGHT: A REGRA DE VALOR DE DADOS");
    lines.append("-" * 115);
    lines.append("");
    lines.append("  DADO PUBLICO E FACIL = COMMODITY (baixo valor)");
    lines.append("    CAGED, INEP, DATASUS -> todo mundo tem -> cobre conveniencia");
    lines.append("");
    lines.append("  DADO PUBLICO CRUZADO = PRATA");
    lines.append("    Fome x Saneamento x Renda -> so TEIA cruzou -> valor medio");
    lines.append("");
    lines.append("  DADO EXCLUSIVO + MODELO = DIAMANTE");
    lines.append("    Impacto fiscal de 35 politicas -> so TEIA tem -> valor maximo");
    lines.append("");
    lines.append("  A FORMULA:");
    lines.append("    valor = exclusividade x impacto_da_decisao");
    lines.append("");
    lines.append("    IBGE puro (todo mundo tem, ! habilita decisao) = R$0,05");
    lines.append("    IBGE cruzado (so TEIA, habilita alocar recurso)  = R$0,10");
    lines.append("    Modelo TEIA (exclusivo, habilita R$ bi)           = R$0,25");
    lines.append("    Simulador   (exclusivo, interactive, decisao)      = R$0,20");
    lines.append("    Dossie      (exclusivo, completo, ministerial)     = R$5,00");
    lines.append("");
    // === PRECIFICACAO DINAMICA ===
    lines.append("-" * 115);
    lines.append("PRECIFICACAO DINAMICA: token cost deve se ajustar ao VALOR");
    lines.append("-" * 115);
    lines.append("");
    lines.append("{'ENDPOINT':<38} {'ATUAL':>8} {'SUGERIDO':>10} {'DELTA':>10} {'ACAO'}");
    lines.append("-" * 115);
    for d in ranked {
        s = d.score;
        current = d.current_token_cost;
        suggested = s.suggested_token_cost;
        delta = suggested - current;
        if delta > current * 0.5 {
            action = "SUBIR PRECO (subvalorizado)";
        } else if delta < -current * 0.3 {
            action = "BAIXAR PRECO (sobvalorizado)";
        } else {
            action = "mantem";
        lines.append(;
            "{d.endpoint:<38} ";
            "{current:>6.1f} T  ";
            "{suggested:>8.1f} T  ";
            "{delta:>+8.1f} T  ";
            "{action}";
        );
    lines.append("");
    lines.append("=" * 115);
    return "\n".join(lines);
// ============================================================================
// 4. EXECUCAO
// ============================================================================
if __name__ == "__main__" {
    println!(print_valuation());
