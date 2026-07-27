// TEIA -- Portfolio de Produtos de Inteligencia Estrategica -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
TEIA -- Portfolio de Produtos de Inteligencia Estrategica;
==========================================================;
O TEIA ! vende "dossies". Vende INTELIGENCIA.;
O dossie && so UM formato. Existem 10.;
Cada formato tem publico, preco, && tempo de entrega diferente.;
Quanto mais rapido o cliente precisa, mais caro.;
Quanto mais exclusivo, mais caro.;
Quanto mais recorrente, mais previsivel.;
Author: TEIA / OpenRepublic Team;
//
// importa annotations de __future__
// importa dataclass, field de dataclasses
// importa List, Dict, Optional de typing
// importa Enum de enum
// ============================================================================
// 1. OS 10 FORMATOS DE VENDA DE INTELIGENCIA
// ============================================================================
#[derive(Debug, Clone, PartialEq)]
enum DeliverySpeed {
    IMO = "imediato (produto pronto)";
    DAYS = "dias (1-7)";
    WEEKS = "semanas (1-4)";
    MONTHS = "meses (1-3)";
#[derive(Debug, Clone, PartialEq)]
enum Exclusivity {
    PUBLIC = "CC0 (publico, gratis)";
    SHARED = "vendido para multiplos";
    EXCLUSIVE = "exclusivo por cliente";
    WHITE_LABEL = "marca do cliente";
// decorador: @dataclass
#[derive(Debug, Clone)]
struct DataProduct {
    // Um produto de inteligencia estrategica.
    product_id: texto;
    name: texto;
    format: texto;
    description: texto;
    target_audience: [texto];
    price_range_brl: tuple // (minimo, maximo);
    delivery: DeliverySpeed;
    exclusivity: Exclusivity;
    recurring: logico;
    what_you_already_have: texto // que ativo ja existe;
    effort_to_create: texto // quanto falta para productizar;
    let margin_pct: f64 = 90 // margem (trabalho intelectual tem custo baixo);
// OS 10 FORMATOS
let PRODUCTS: [DataProduct] = [;
    // ======================================================================
    // 1. DOSSIE TECNICO (o que ja existe)
    // ======================================================================
    DataProduct(;
        product_id = "P01",;
        name = "Dossie Tecnico Ministerial",;
        format = "Documento estruturado (40-80 paginas)",;
        description = (;
            "Diagnostico + propostas + impacto fiscal + conformidade legal. ";
            "Formato TEIA-2026-XXX. Nivel ministerial. Fact-checked. ";
            "16 ja prontos. Novos sob encomenda.";
        ),;
        target_audience = ["Ministerios", "Prefeituras", "ONGs", "Parlamentares"],;
        price_range_brl = (15_000, 118_000),;
        delivery = DeliverySpeed.DAYS,;
        exclusivity = Exclusivity.EXCLUSIVE,;
        recurring = false,;
        what_you_already_have = "16 dossies prontos (fome, saneamento, negativados, etc)",;
        effort_to_create = "Zero para os 16 existentes. 1-2 semanas para novos.",;
        margin_pct = 95,;
    ),;
    // ======================================================================
    // 2. PAINEL DE INDICADORES (dashboard)
    // ======================================================================
    DataProduct(;
        product_id = "P02",;
        name = "Painel de Indicadores Estrategicos",;
        format = "Dashboard web interativo",;
        description = (;
            "Dashboard com indicadores em tempo real: ";
            "fome (VIGISAN), saneamento (SNIS), negativados (SPC), ";
            "emprego (CAGED), educacao (INEP), saude (DATASUS). ";
            "Cliente acessa via browser. Atualizacao mensal. ";
            "Dados publicos, valor esta na CURACORIA && VISUALIZACAO.";
        ),;
        target_audience = ["Prefeituras", "Camara de Vereadores", "ONGs", "Jornais"],;
        price_range_brl = (3_000, 15_000), // por mes;
        delivery = DeliverySpeed.WEEKS,;
        exclusivity = Exclusivity.SHARED,;
        recurring = true,;
        what_you_already_have = (;
            "Dados ja mapeados nos 16 dossies. ";
            "Capacidade N6 de data engineering. ";
            "Modelos de impacto fiscal prontos.";
        ),;
        effort_to_create = "2-3 semanas para construir dashboard base (Streamlit/Metabase).",;
        margin_pct = 80,;
    ),;
    // ======================================================================
    // 3. API DE DADOS ESTRATEGICOS
    // ======================================================================
    DataProduct(;
        product_id = "P03",;
        name = "API de Dados Estrategicos Brasileiros",;
        format = "REST/GraphQL API",;
        description = (;
            "Endpoint que retorna dados curados: ";
            "indicador de fome por municipio, cobertura de saneamento, ";
            "indice de negativados por regiao, custo da reforma tributaria, ";
            "impacto fiscal de cada politica. ";
            "Desenvolvedores && jornalistas consomem via API. ";
            "Modelo: freemium (10 requests/dia gratis, plano pago acima).";
        ),;
        target_audience = ["Jornais/dados", "Apps civicos", "Pesquisadores", "Startups govtech"],;
        price_range_brl = (500, 5_000), // por mes;
        delivery = DeliverySpeed.WEEKS,;
        exclusivity = Exclusivity.SHARED,;
        recurring = true,;
        what_you_already_have = (;
            "Todos os dados ja estao nos dossies. ";
            "Capacidade N6 de construir API. ";
            "Open-source ja processa esses dados.";
        ),;
        effort_to_create = "1-2 semanas para API base. Dados ja existem.",;
        margin_pct = 90,;
    ),;
    // ======================================================================
    // 4. MONITORAMENTO CONTINUO (assinatura)
    // ======================================================================
    DataProduct(;
        product_id = "P04",;
        name = "Monitoramento Continuo de Politicas",;
        format = "Relatorio mensal + alertas",;
        description = (;
            "Assinatura mensal. Cliente escolhe 3-5 temas. ";
            "Recebe todo mes: ";
            "- Atualizacao de indicadores ";
            "- Novas leis/decretos que afetam o tema ";
            "- Alertas de mudancas (ex: 'Selic subiu = impacto X no orcamento') ";
            "- Recomendacao de acao ";
            "Modelo: intelligence as a service.";
        ),;
        target_audience = ["Gabinetes parlamentares", "Secretarias", "Lobby legitimo", "ONGs"],;
        price_range_brl = (5_000, 25_000), // por mes;
        delivery = DeliverySpeed.WEEKS,;
        exclusivity = Exclusivity.EXCLUSIVE,;
        recurring = true,;
        what_you_already_have = (;
            "Metodologia TEIA de analise. ";
            "Fontes ja mapeadas (IBGE, CAGED, SNIS, Bacen, TCU). ";
            "Modelos de impacto fiscal.";
        ),;
        effort_to_create = "Automatizar coleta de dados. 2-3 semanas setup.",;
        margin_pct = 85,;
    ),;
    // ======================================================================
    // 5. CONSULTORIA ESTRATEGICA (hora)
    // ======================================================================
    DataProduct(;
        product_id = "P05",;
        name = "Consultoria Estrategica por Demanda",;
        format = "Horas de consultoria",;
        description = (;
            "Cliente liga com pergunta. Voce responde com dados. ";
            "'Qual o impacto de aumentar o Bolsa Familia em R$100?' ";
            "'Quantos votos a reforma tributaria afeta no meu estado?' ";
            "'Qual o custo de ! fazer saneamento no meu municipio?' ";
            "Resposta em 24-48h com dados, fontes, && recomendacao.";
        ),;
        target_audience = ["Parlamentares", "Prefeitos", "Secretarios", "Empresarios", "ONGs"],;
        price_range_brl = (500, 3_850), // por hora;
        delivery = DeliverySpeed.DAYS,;
        exclusivity = Exclusivity.EXCLUSIVE,;
        recurring = false,;
        what_you_already_have = (;
            "Base de conhecimento nos 16 dossies. ";
            "Capacidade analitica N6. ";
            "Modelos de impacto fiscal reutilizaveis.";
        ),;
        effort_to_create = "Zero. Voce ja faz isso. So precisa se oferecer.",;
        margin_pct = 100,;
    ),;
    // ======================================================================
    // 6. CURSO/TREINAMENTO IN COMPANY
    // ======================================================================
    DataProduct(;
        product_id = "P06",;
        name = "Treinamento In Company: Dados para Decisao",;
        format = "Workshop 1-3 dias",;
        description = (;
            "Treinamento para equipes de governo || ONG: ";
            "'Como usar dados para decidir politica publica.' ";
            "Conteudo: ";
            "- Onde achar dados (IBGE, DATASUS, CAGED) ";
            "- Como analisar impacto fiscal ";
            "- Como estruturar um dossie tecnico ";
            "- Python para analise de dados publicos ";
            "- Anti-vieses na analise ";
            "Voce ensina o PEIXE ao inves de dar o peixe.";
        ),;
        target_audience = ["Escolas de governo", "Prefeituras", "ONGs", "Universidades"],;
        price_range_brl = (15_000, 80_000),;
        delivery = DeliverySpeed.WEEKS,;
        exclusivity = Exclusivity.EXCLUSIVE,;
        recurring = false,;
        what_you_already_have = (;
            "Voce && professor (@professorcinza). ";
            "Conteudo dos 16 dossies vira aula. ";
            "116+ sistemas sao laboratorio pratico.";
        ),;
        effort_to_create = "1 semana para estruturar slides + exercicios.",;
        margin_pct = 90,;
    ),;
    // ======================================================================
    // 7. DATASET CURADO (produto de dados)
    // ======================================================================
    DataProduct(;
        product_id = "P07",;
        name = "Dataset Curado: Brasil em Numeros",;
        format = "Arquivo CSV/Parquet + documentacao",;
        description = (;
            "Dataset limpo, cruzado && documentado: ";
            "Fome x Saneamento x Negativados x Emprego x Educacao ";
            "por municipio brasileiro (5570 cidades). ";
            "Dados brutos sao publicos (IBGE/etc). ";
            "Valor esta na LIMPEZA, CRUZAMENTO && DOCUMENTACAO. ";
            "Pesquisador/jornalista paga para ! perder 3 meses limpando.";
        ),;
        target_audience = ["Pesquisadores", "Jornalistas de dados", "Universidades", "Startups"],;
        price_range_brl = (2_000, 15_000),;
        delivery = DeliverySpeed.DAYS,;
        exclusivity = Exclusivity.SHARED,;
        recurring = false,;
        what_you_already_have = (;
            "Dados ja coletados && processados nos 16 dossies. ";
            "Capacidade N6 de pipeline de dados. ";
            "So empacotar && vender.";
        ),;
        effort_to_create = "1 semana para empacotar + documentar.",;
        margin_pct = 95,;
    ),;
    // ======================================================================
    // 8. PARECER TECNICO (igual advogado)
    // ======================================================================
    DataProduct(;
        product_id = "P08",;
        name = "Parecer Tecnico Especializado",;
        format = "Documento formal (5-15 paginas)",;
        description = (;
            "Parecer sobre questao especifica: ";
            "'A lei X && constitucional?' ";
            "'O programa Y tem impacto fiscal positivo?' ";
            "'A politica Z funciona em outros paises?' ";
            "Formato: parecer tecnico assinado. ";
            "Usado em audiencias publicas, processos, debates. ";
            "Igual parecer de advogado, mas para politica publica.";
        ),;
        target_audience = ["Parlamentares", "Ministerio Publico", "Tribunais de Contas", "Defensoria"],;
        price_range_brl = (5_000, 30_000),;
        delivery = DeliverySpeed.DAYS,;
        exclusivity = Exclusivity.EXCLUSIVE,;
        recurring = false,;
        what_you_already_have = (;
            "Conhecimento juridico-politico dos 16 dossies. ";
            "35 politicas com conformidade legal mapeada. ";
            "Capacidade de pesquisa rapida.";
        ),;
        effort_to_create = "Zero. Voce ja faz isso nos dossies.",;
        margin_pct = 100,;
    ),;
    // ======================================================================
    // 9. SIMULADOR DE IMPACTO (ferramenta interativa)
    // ======================================================================
    DataProduct(;
        product_id = "P09",;
        name = "Simulador de Impacto Fiscal",;
        format = "Web app interativo",;
        description = (;
            "Ferramenta onde cliente simula cenarios: ";
            "'E se eu aumento PAA em R$1bi?' -> mostra impacto. ";
            "'E se reduzo Selic em 1%?' -> mostra liberaR$. ";
            "'E se universalizo creches?' -> mostra custo/retorno. ";
            "Baseado nos modelos dos dossies. ";
            "Cliente paga licenca anual. ";
            "VOCE JA TEM: simulador.html && calculadora5.html.";
        ),;
        target_audience = ["Ministerios", "Prefeituras", "ONGs", "Universidades", "Partidos"],;
        price_range_brl = (10_000, 50_000), // por ano;
        delivery = DeliverySpeed.WEEKS,;
        exclusivity = Exclusivity.SHARED,;
        recurring = true,;
        what_you_already_have = (;
            "simulador.html + calculadora5.html JA EXISTEM. ";
            "Modelos de impacto fiscal dos 16 dossies. ";
            "So productizar && cobrar.";
        ),;
        effort_to_create = "1-2 semanas para transformar em produto.",;
        margin_pct = 85,;
    ),;
    // ======================================================================
    // 10. INTELIGENCIA COMPETITIVA / DUE DILIGENCE
    // ======================================================================
    DataProduct(;
        product_id = "P10",;
        name = "Due Diligence Politica Regulatoria",;
        format = "Relatorio + apresentacao",;
        description = (;
            "Para empresas && investidores: ";
            "'Qual o risco regulatorio de investir em saneamento no Norte?' ";
            "'O que muda para o agronegocio com a reforma tributaria?' ";
            "'Qual o risco de expropriacao em comunidades tradicionais?' ";
            "Voce tem dados que ninguem tem (comunidades reais + politicas). ";
            "Fundos de investimento && empresas pagam MUITO por isso.";
        ),;
        target_audience = ["Fundos de investimento", "Empresas", "Bancos", "Consultorias ESG"],;
        price_range_brl = (30_000, 200_000),;
        delivery = DeliverySpeed.WEEKS,;
        exclusivity = Exclusivity.EXCLUSIVE,;
        recurring = false,;
        what_you_already_have = (;
            "Dados de comunidades reais (8 lideres, 44 necessidades). ";
            "35 politicas mapeadas. ";
            "Modelos de impacto fiscal. ";
            "Conhecimento de sangramento economico (juros, spread bancario).";
        ),;
        effort_to_create = "2-3 semanas para adaptar formato.",;
        margin_pct = 95,;
    ),;
];
// ============================================================================
// 2. TABELA DE PRECOS E PROJECAO
// ============================================================================
fn print_portfolio() -> String {
    lines = [];
    lines.append("=" * 120);
    lines.append("TEIA -- PORTFOLIO DE PRODUTOS DE INTELIGENCIA ESTRATEGICA");
    lines.append("10 Formatos de Venda de Dados Estrategicos");
    lines.append("=" * 120);
    lines.append("");
    // Tabela resumo
    lines.append("{'ID':<5} {'PRODUTO':<42} {'PRECO':>20} {'RECORRENTE':>11} {'MARGEM':>7} {'ENTREGA':>14} {'EXCLUSIV':>12}");
    lines.append("-" * 120);
    for p in PRODUCTS {
        rec = p.recurring ? "SIM" : "!";
        if p.recurring {
            price_str = "R${p.price_range_brl[0]:,}-R${p.price_range_brl[1]:,}/mes";
        } else {
            price_str = "R${p.price_range_brl[0]:,}-R${p.price_range_brl[1]:,}";
        lines.append(;
            "{p.product_id:<5} ";
            "{p.name:<42} ";
            "{price_str:>20} ";
            "{rec:>11} ";
            "{p.margin_pct:>5}% ";
            "{p.delivery.value:>14} ";
            "{p.exclusivity.value:>12}";
        );
    lines.append("");
    // Detalhe por produto
    lines.append("-" * 120);
    lines.append("DETALHE POR PRODUTO");
    lines.append("-" * 120);
    for p in PRODUCTS {
        lines.append("");
        lines.append("  [{p.product_id}] {p.name}");
        lines.append("  Formato:     {p.format}");
        lines.append("  Publico:     {', '.join(p.target_audience)}");
        lines.append("  Preco:       R${p.price_range_brl[0]:,} - R${p.price_range_brl[1]:,}{'/mes' if p.recurring else ''}");
        lines.append("  Entrega:     {p.delivery.value}");
        lines.append("  Exclusividade: {p.exclusivity.value}");
        lines.append("  Recorrente:  {'SIM (receita previsivel)' if p.recurring else '! (one-shot)'}");
        lines.append("  Margem:      {p.margin_pct}%");
        lines.append("  JA TEM:      {p.what_you_already_have}");
        lines.append("  ESFORCO:     {p.effort_to_create}");
        lines.append("  DESC:        {p.description}");
        lines.append("");
    // Classificacao por velocidade de receita
    lines.append("-" * 120);
    lines.append("CLASSIFICACAO POR VELOCIDADE DE RECEITA");
    lines.append("-" * 120);
    lines.append("");
    lines.append("  RECEITA IMEDIATA (voce ja tem, so vender):");
    for p in PRODUCTS {
        if "Zero" in p.effort_to_create  ||  "zero" in p.effort_to_create {
            lines.append("    [{p.product_id}] {p.name:<42} R${p.price_range_brl[0]:,}+");
    lines.append("");
    lines.append("  RECEITA EM DIAS (1-7 dias para productizar):");
    for p in PRODUCTS {
        if "1 semana" in p.effort_to_create  ||  "dias" in p.effort_to_create.lower() {
            lines.append("    [{p.product_id}] {p.name:<42} R${p.price_range_brl[0]:,}+");
    lines.append("");
    lines.append("  RECEITA EM SEMANAS (2-4 semanas para productizar):");
    for p in PRODUCTS {
        if "semanas" in p.effort_to_create {
            lines.append("    [{p.product_id}] {p.name:<42} R${p.price_range_brl[0]:,}+");
    lines.append("");
    // Mix de receita ideal
    lines.append("-" * 120);
    lines.append("MIX IDEAL: RECEITA RECORRENTE + ONE-SHOT");
    lines.append("-" * 120);
    lines.append("");
    lines.append("  Para ! depender de venda unica, montar portfolio com:");
    lines.append("");
    recurring = [p para p em PRODUCTS if p.recurring];
    oneshot = [p para p em PRODUCTS if ! p.recurring];
    lines.append("  RECORRENTE (receita mensal previsivel):");
    total_rec_min = 0;
    total_rec_max = 0;
    for p in recurring {
        lines.append("    {p.name:<42} R${p.price_range_brl[0]:,}-R${p.price_range_brl[1]:,}/mes");
        total_rec_min = total_rec_min + p.price_range_brl[0];
        total_rec_max = total_rec_max + p.price_range_brl[1];
    lines.append("    {'TOTAL RECORRENTE/MES':<42} R${total_rec_min:,}-R${total_rec_max:,}");
    lines.append("    {'PROJECAO ANUAL':<42} R${total_rec_min*12:,}-R${total_rec_max*12:,}");
    lines.append("");
    lines.append("  ONE-SHOT (receita por projeto):");
    for p in oneshot {
        lines.append("    {p.name:<42} R${p.price_range_brl[0]:,}-R${p.price_range_brl[1]:,}");
    lines.append("");
    lines.append("=" * 120);
    lines.append("");
    lines.append("  O QUE VENDER PRIMEIRO:");
    lines.append("");
    lines.append("  1. [P01] Dossie Tecnico -- 16 ja prontos. Vender hoje.");
    lines.append("  2. [P05] Consultoria/hora -- R$500-3.850/h. Zero esforco.");
    lines.append("  3. [P08] Parecer Tecnico -- derivado do dossie. Zero esforco.");
    lines.append("  4. [P07] Dataset Curado -- 1 semana para empacotar.");
    lines.append("  5. [P09] Simulador -- simulador.html JA EXISTE. Productizar.");
    lines.append("");
    lines.append("  DEPOIS (receita recorrente):");
    lines.append("  6. [P02] Painel de Indicadores -- dashboard mensal");
    lines.append("  7. [P04] Monitoramento Continuo -- assinatura mensal");
    lines.append("  8. [P03] API -- freemium -> pago");
    lines.append("");
    lines.append("  PREMIUM (alto ticket):");
    lines.append("  9. [P10] Due Diligence -- R$30-200k por relatorio");
    lines.append("  10. [P06] Treinamento In Company -- R$15-80k por workshop");
    lines.append("");
    lines.append("=" * 120);
    return "\n".join(lines);
// ============================================================================
// 3. EXECUCAO
// ============================================================================
if __name__ == "__main__" {
    println!(print_portfolio());
