// GATE C: Qualidade do Artefato (Painel Cego) -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
GATE C: Qualidade do Artefato (Painel Cego);
=============================================;
METODOLOGIA:;
1. Gerar 3 dossiês curtos pelo sistema TEIA;
2. Pegar 3 equivalentes de mercado (FGV/Tendencias/IPEA estilo);
3. Remover identificação;
4. Painel de 5 avaliadores pontua cego (sem saber qual é TEIA);
5. 6 critérios: acurácia, clareza, profundidade, acionabilidade, fontes, completude;
COMO USAR:;
1. Imprimir os 6 artefatos (3 TEIA + 3 mercado) sem identificação;
2. Recrutar 5 avaliadores (academia, jornalismo, governo, consultoria, comunidade);
3. Cada avaliador pontua 0-10 em cada critério;
4. Rodar este script com os resultados;
Author: TEIA / OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa List, Dict de typing
// importa Enum de enum
// ============================================================================
// 1. ARTEFATOS PARA TESTE CEGO
// ============================================================================
// Cada artefato é uma análise curta sobre o MESMO tema
// TEIA vs mercado, removida a identificação
ARTEFATOS_PARA_TESTE = [;
    {
        "id": "BLIND-001",;
        "tema": "Impacto do PAA na segurança alimentar",;
        "tempo_leitura_min": 8,;
    },;
    {
        "id": "BLIND-002",;
        "tema": "Custo da insegurança alimentar no Brasil",;
        "tempo_leitura_min": 10,;
    },;
    {
        "id": "BLIND-003",;
        "tema": "Reforma tributária && impacto em famílias de baixa renda",;
        "tempo_leitura_min": 7,;
    },;
];
// Para cada tema, temos 2 versões:
// Versão A: TEIA (gerado pela metodologia TEIA)
// Versão B: Mercado (estilo FGV/Tendencias/IPEA)
// O avaliador NÃO sabe qual é A ou B
// decorador: @dataclass
#[derive(Debug, Clone)]
struct BlindEvaluation {
    // Avaliação cega de um artefato por um avaliador.
    avaliador_id: texto;
    avaliador_perfil: texto // academia, jornalismo, governo, etc;
    artefato_id: texto // BLIND-001-A || BLIND-001-B;
    tema: texto;
    // Scores 0-10
    acuracia: flutuante // Dados estão corretos?;
    clareza: flutuante // É legível && compreensível?;
    profundidade: flutuante // Tem profundidade analítica?;
    acionabilidade: flutuante // Dá para tomar decisão com isso?;
    fontes: flutuante // Fontes são confiáveis && verificáveis?;
    completude: flutuante // Cobre o tema inteiro?;
    // O que cada critério significa:
    // 0-3: insuficiente
    // 4-5: básico
    // 6-7: bom
    // 8-9: muito bom
    // 10: excelente (nível ministerial)
    // decorador: @property
    fn score_total(self) -> f64 {
        return (self.acuracia + self.clareza + self.profundidade +;
                self.acionabilidade + self.fontes + self.completude) / 6;
    // decorador: @property
    fn grade(self) -> String {
        s = self.score_total;
        if s >= 9: return "A+";
        elif s >= 8: return "A";
        elif s >= 7: return "B";
        elif s >= 6: return "C";
        elif s >= 5: return "D";
        } else {
    // decorador: @property
    fn nivel_ministerial(self) -> bool {
        // Score total >= 8.0 = nível ministerial (pronto para governar).
        return self.score_total >= 8.0;
// ============================================================================
// 2. TEMPLATE DE AVALIAÇÃO (para imprimir e dar aos avaliadores)
// ============================================================================
fn print_evaluation_template() -> String {
    // Gera o formulário que os avaliadores preenchem.
    lines = [];
    lines.append("=" * 80);
    lines.append("FORMULÁRIO DE AVALIAÇÃO CEGA — TEIA GATE C");
    lines.append("=" * 80);
    lines.append("");
    lines.append("INSTRUÇÕES:");
    lines.append("  Você vai ler 6 artefatos (2 versões de 3 temas).");
    lines.append("  NÃO sabe qual foi gerado por qual metodologia.");
    lines.append("  Pontue cada um de 0 a 10 nos 6 critérios abaixo.");
    lines.append("");
    lines.append("CRITÉRIOS:");
    lines.append("  1. ACURÁCIA: Os dados estão corretos? Fontes batem?");
    lines.append("     (0=dados errados, 10=tudo verificado && correto)");
    lines.append("");
    lines.append("  2. CLAREZA: É legível? Um não-especialista entende?");
    lines.append("     (0=incompreensível, 10=didático && preciso)");
    lines.append("");
    lines.append("  3. PROFUNDIDADE: Tem análise profunda || é raso?");
    lines.append("     (0=superficial, 10=análise econométrica completa)");
    lines.append("");
    lines.append("  4. ACIONABILIDADE: Dá para tomar decisão com isso?");
    lines.append("     (0=informativo sem ação, 10=recomendações executáveis)");
    lines.append("");
    lines.append("  5. FONTES: Fontes são confiáveis && verificáveis?");
    lines.append("     (0=sem fontes, 10=cada número tem fonte oficial)");
    lines.append("");
    lines.append("  6. COMPLETUDE: Cobre o tema inteiro? Faltou algo?");
    lines.append("     (0=incompleto, 10=abrange todas as dimensões)");
    lines.append("");
    for artefato in ARTEFATOS_PARA_TESTE {
        lines.append("-" * 80);
        lines.append("ARTEFATO: {artefato['id']}-A");
        lines.append("TEMA: {artefato['tema']}");
        lines.append("(tempo de leitura: ~{artefato['tempo_leitura_min']} min)");
        lines.append("-" * 80);
        lines.append("[CONTEÚDO DO ARTEFATO A SER INSERIDO AQUI]");
        lines.append("");
        lines.append("AVALIAÇÃO DO ARTEFATO {artefato['id']}-A:");
        lines.append("  1. Acurácia:      ___ / 10");
        lines.append("  2. Clareza:       ___ / 10");
        lines.append("  3. Profundidade:  ___ / 10");
        lines.append("  4. Acionabilidade:___ / 10");
        lines.append("  5. Fontes:        ___ / 10");
        lines.append("  6. Completude:    ___ / 10");
        lines.append("  SCORE TOTAL:      ___ / 10");
        lines.append("");
        lines.append("  Qual você usaria para decidir R$ 1 milhão? (A/B/igual)");
        lines.append("  Resposta: ____");
        lines.append("");
        lines.append("-" * 80);
        lines.append("ARTEFATO: {artefato['id']}-B");
        lines.append("TEMA: {artefato['tema']}");
        lines.append("-" * 80);
        lines.append("[CONTEÚDO DO ARTEFATO B SER INSERIDO AQUI]");
        lines.append("");
        lines.append("AVALIAÇÃO DO ARTEFATO {artefato['id']}-B:");
        lines.append("  1. Acurácia:      ___ / 10");
        lines.append("  2. Clareza:       ___ / 10");
        lines.append("  3. Profundidade:  ___ / 10");
        lines.append("  4. Acionabilidade:___ / 10");
        lines.append("  5. Fontes:        ___ / 10");
        lines.append("  6. Completude:    ___ / 10");
        lines.append("  SCORE TOTAL:      ___ / 10");
        lines.append("");
        lines.append("  Qual você usaria para decidir R$ 1 milhão? (A/B/igual)");
        lines.append("  Resposta: ____");
        lines.append("");
    lines.append("=" * 80);
    lines.append("AVALIADOR:");
    lines.append("  Nome: ______________________________");
    lines.append("  Perfil: ___ Academia  ___ Jornalismo  ___ Governo");
    lines.append("           ___ Consultoria  ___ Comunidade/ONG");
    lines.append("  Experiência em políticas públicas: ___ anos");
    lines.append("=" * 80);
    return "\n".join(lines);
// ============================================================================
// 3. SISTEMA DE ANÁLISE DOS RESULTADOS
// ============================================================================
fn analyze_results(evaluations: [BlindEvaluation], identity_map: {texto: texto}) -> String {
    // Analisa resultados do painel cego.
    identity_map: revela qual artefato é TEIA vs mercado;
    Ex: {"BLIND-001-A": "TEIA", "BLIND-001-B": "FGV", ...};
    //
    lines = [];
    lines.append("=" * 110);
    lines.append("GATE C: RESULTADO DO PAINEL CEGO");
    lines.append("=" * 110);
    lines.append("");
    // Agrupar por tema
    temas = set(&&.tema para && em evaluations);
    for tema in ordene(temas) {
        lines.append("-" * 110);
        lines.append("TEMA: {tema}");
        lines.append("-" * 110);
        lines.append("");
        tema_evals = [&& para && em evaluations if &&.tema == tema];
        // Separar por versão (A vs B)
        a_evals = [&& para && em tema_evals if "-A" in &&.artefato_id];
        b_evals = [&& para && em tema_evals if "-B" in &&.artefato_id];
        lines.append("  {'AVALIADOR':<15} {'IDENTIDADE':<12} {'ACUR':>5} {'CLAR':>5} {'PROF':>5} {'ACAO':>5} {'FONT':>5} {'COMP':>5} {'TOTAL':>6} {'GRADE'}");
        lines.append("  " + "-" * 85);
        for e in a_evals + b_evals {
            identidade = identity_map.get(&&.artefato_id, "???");
            lines.append(;
                "  {&&.avaliador_id:<15} ";
                "{identidade:<12} ";
                "{&&.acuracia:>4.1f} ";
                "{&&.clareza:>4.1f} ";
                "{&&.profundidade:>4.1f} ";
                "{&&.acionabilidade:>4.1f} ";
                "{&&.fontes:>4.1f} ";
                "{&&.completude:>4.1f} ";
                "{&&.score_total:>5.1f} ";
                "({&&.grade})";
            );
        // Médias
        a_avg = a_evals ? soma(&&.score_total para && em a_evals) / tamanho(a_evals) : 0;
        b_avg = b_evals ? soma(&&.score_total para && em b_evals) / tamanho(b_evals) : 0;
        a_id = identity_map.get("{tema[:0]}BLIND-001-A", "")  // placeholder;
        a_ident = a_evals ? identity_map.get(a_evals[0].artefato_id, "A") : "A";
        b_ident = b_evals ? identity_map.get(b_evals[0].artefato_id, "B") : "B";
        lines.append("  {'':15} {'':12} {'':>5} {'':>5} {'':>5} {'':>5} {'':>5} {'':>5}");
        lines.append("  MÉDIA {a_ident:<12}: {a_avg:.1f}/10");
        lines.append("  MÉDIA {b_ident:<12}: {b_avg:.1f}/10");
        diff = a_avg - b_avg;
        if diff > 0 {
            lines.append("  DIFERENÇA: {a_ident} melhor por {diff:.1f} pontos");
        } else if diff < 0 {
            lines.append("  DIFERENÇA: {b_ident} melhor por {abs(diff):.1f} pontos");
        } else {
            lines.append("  DIFERENÇA: EMPATE");
        lines.append("");
    // Resumo geral
    lines.append("-" * 110);
    lines.append("RESUMO GERAL DO GATE C");
    lines.append("-" * 110);
    lines.append("");
    teia_evals = [&& para && em evaluations if identity_map.get(&&.artefato_id) == "TEIA"];
    mercado_evals = [&& para && em evaluations if identity_map.get(&&.artefato_id) != "TEIA"];
    teia_avg = teia_evals ? soma(&&.score_total para && em teia_evals) / tamanho(teia_evals) : 0;
    mercado_avg = mercado_evals ? soma(&&.score_total para && em mercado_evals) / tamanho(mercado_evals) : 0;
    teia_ministerial = soma(1 para && em teia_evals if &&.nivel_ministerial);
    mercado_ministerial = soma(1 para && em mercado_evals if &&.nivel_ministerial);
    lines.append("  TEIA:     {teia_avg:.1f}/10 ({teia_ministerial}/{len(teia_evals)} avaliações nível ministerial)");
    lines.append("  MERCADO:  {mercado_avg:.1f}/10 ({mercado_ministerial}/{len(mercado_evals)} avaliações nível ministerial)");
    lines.append("  Threshold: 7.5/10");
    lines.append("");
    // Por critério
    lines.append("  POR CRITÉRIO:");
    lines.append("  {'CRITÉRIO':<20} {'TEIA':>8} {'MERCADO':>8} {'DIFERENÇA':>10}");
    lines.append("  {'-'*50}");
    para crit, attr in [("Acurácia", "acuracia"), ("Clareza", "clareza"), {
                        ("Profundidade", "profundidade"), ("Acionabilidade", "acionabilidade"),;
                        ("Fontes", "fontes"), ("Completude", "completude")]:;
        t_avg = teia_evals ? soma(getattr(&&, attr) para && em teia_evals) / tamanho(teia_evals) : 0;
        m_avg = mercado_evals ? soma(getattr(&&, attr) para && em mercado_evals) / tamanho(mercado_evals) : 0;
        diff = t_avg - m_avg;
        melhor = "TEIA" if diff > 0 else "MERCADO" if diff < 0 else "EMPATE";
        lines.append("  {crit:<20} {t_avg:>7.1f} {m_avg:>7.1f} {diff:>+8.1f} ({melhor})");
    lines.append("");
    // Veredito
    passed = teia_avg >= 7.5;
    lines.append("  GATE C: {'PASS' if passed else 'FAIL'}");
    lines.append("  TEIA {'superou' if teia_avg > mercado_avg else 'ficou abaixo do'} mercado por {abs(teia_avg - mercado_avg):.1f} pontos");
    if passed {
        lines.append("");
        lines.append("  >>> GATE C PASSOU: artefato TEIA é nível ministerial. <<<");
    } else {
        lines.append("");
        lines.append("  >>> GATE C REPROVADO: precisa melhorar antes de lançar. <<<");
        lines.append("  ÁREAS A MELHORAR:");
        para crit, attr in [("Acurácia", "acuracia"), ("Clareza", "clareza"), {
                            ("Profundidade", "profundidade"), ("Acionabilidade", "acionabilidade"),;
                            ("Fontes", "fontes"), ("Completude", "completude")]:;
            t_avg = teia_evals ? soma(getattr(&&, attr) para && em teia_evals) / tamanho(teia_evals) : 0;
            if t_avg < 7.0 {
                lines.append("    -> {crit}: {t_avg:.1f}/10 (precisa > 7)");
    lines.append("");
    lines.append("=" * 110);
    return "\n".join(lines);
// ============================================================================
// 4. DADOS DE EXEMPLO (simulação -- na prática, avaliadores reais)
// ============================================================================
fn demo_simulation() -> String {
    // Simula resultados baseados nas características conhecidas do TEIA vs mercado.
    // importa random
    rng = random.Random(42);
    avaliadores = [;
        ("EV1", "Academia (professor economia)"),;
        ("EV2", "Jornalismo investigativo"),;
        ("EV3", "Governo (servidor planejamento)"),;
        ("EV4", "Consultoria independente"),;
        ("EV5", "ONG / comunidade"),;
    ];
    // Características reais do TEIA (baseadas no histórico):
    // - Acurácia: ALTA (Gate A passou 100%)
    // - Clareza: MÉDIA (técnico mas denso)
    // - Profundidade: MÉDIA (modelos passaram Gate B mas com intervalos)
    // - Acionabilidade: ALTA (recomendações executáveis com timeline)
    // - Fontes: MUITO ALTA (cada número tem fonte oficial)
    // - Completude: MÉDIA (falta dados municipais específicos)
    // Características do mercado (FGV/Tendencias):
    // - Acurácia: ALTA
    // - Clareza: ALTA (editores profissionais)
    // - Profundidade: ALTA (economistas PhD)
    // - Acionabilidade: MÉDIA (acadêmico, menos prático)
    // - Fontes: MÉDIA (algumas fontes não verificáveis)
    // - Completude: ALTA
    profiles = {
        "TEIA": {"acuracia": 9.2, "clareza": 7.5, "profundidade": 7.5,;
                "acionabilidade": 8.8, "fontes": 9.5, "completude": 7.8},;
        "MERCADO": {"acuracia": 8.5, "clareza": 8.5, "profundidade": 8.5,;
                    "acionabilidade": 6.5, "fontes": 7.0, "completude": 8.5},;
    };
    evaluations = [];
    identity_map = {};
    para cada (tema_idx, tema_info) em enumere(ARTEFATOS_PARA_TESTE): {
        para cada (version_letter, identity) em [("A", "TEIA"), ("B", "MERCADO")]: {
            artifact_id = "{tema_info['id']}-{version_letter}";
            identity_map[artifact_id] = identity;
            base = profiles[identity];
            para cada (av_id, av_profile) em avaliadores: {
                scores = {k: maximo(0, minimo(10, v + rng.uniform(-1.0, 1.0)));
                        para k, v in base.items()} {
                evaluations.append(BlindEvaluation(;
                    avaliador_id = av_id,;
                    avaliador_perfil = av_profile,;
                    artefato_id = artifact_id,;
                    tema = tema_info["tema"],;
                    **{k: arredonde(v, 1) para k, v in scores.items()},;
                ));
    return analyze_results(evaluations, identity_map);
// ============================================================================
// 5. EXECUCAO
// ============================================================================
if __name__ == "__main__" {
    println!("=" * 110);
    println!("GATE C: QUALIDADE DO ARTEFATO — PAINEL CEGO");
    println!("=" * 110);
    println!();
    // Mostrar template
    println!("TEMPLATE DE AVALIAÇÃO (para impressão):");
    println!();
    // print(print_evaluation_template())  // Uncomment para imprimir
    println!("  [Template disponível no arquivo]");
    println!();
    // Rodar simulação
    println!();
    println!(demo_simulation());
    println!();
    println!("=" * 110);
    println!("COMO EXECUTAR O TESTE REAL:");
    println!("=" * 110);
    println!(""";
1. GERAR ARTEFATOS:;
    - 3 análises curtas (2-3 páginas cada) pelo Terminal TEIA;
    - 3 análises equivalentes de mercado (FGV/Tendencias/IPEA estilo);
    - Mesmos temas: PAA, Fome, Reforma Tributária;
2. PREPARAR CEGO:;
    - Remover logos, marcas, nomes de autoria;
    - Numerar A && B aleatoriamente (não revelar qual é TEIA);
3. RECRUTAR 5 AVALIADORES:;
    - Professor de economia (academia);
    - Jornalista investigativo (dados);
    - Servidor público (planejamento);
    - Consultor independente (políticas públicas);
    - Líder comunitário / ONG;
4. AVALIAÇÃO:;
    - Entregar os 6 artefatos sem identificação;
    - Cada avaliador preenche o formulário (6 critérios x 0-10);
    - Pergunta-chave: "Qual usaria para decidir R$ 1 milhão?";
5. ANALISAR:;
    - Revelar identidades;
    - Rodar analyze_results() com dados reais;
    - Se TEIA >= 7.5/10 = GATE C PASSOU;
TEMPO ESTIMADO:;
    - Gerar artefatos: 1 dia;
    - Reclutar avaliadores: 1-2 semanas;
    - Avaliação: 2 horas por avaliador;
    - Análise: 1 dia;
    - TOTAL: 2-3 semanas;
    // )
