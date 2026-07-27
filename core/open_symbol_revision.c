/* OpenSymbolRevision -- Ressignificacao e Correcao de Preconceitos -- gerado de Portugol++ */
#ifndef OPENSYMBOLREVISION_RESSIGNIFICACAO_E_CORRECAO_DE_PRECONCEITOS_H
#define OPENSYMBOLREVISION_RESSIGNIFICACAO_E_CORRECAO_DE_PRECONCEITOS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenSymbolRevision -- Ressignificacao && Correcao de Preconceitos;
===================================================================;
"Simbolo ! && inerentemente mal. O que faz mal && o SIGNIFICADO;
que a sociedade atribuiu. Mudou o significado, muda o simbolo.";
O QUE ESTE SISTEMA FAZ:;
1. FACT-CHECK DE PRECONCEITOS: frase errada -> Republica corrige;
2. RESSIGNIFICACAO DE SIMBOLOS: simbolo apropriado por grupo nocivo;
    pode ser ressignificado (ex: suastica original era simbolo de paz);
3. REORGANIZACAO POPULACIONAL: educa && reintegra, ! isola;
4. ANTI-FACCIONISMO: simbolos de faccao ressignificados como arte;
COMO FUNCIONA:;
Cidadao escreve frase preconceituosa -> sistema corrige com dados;
Simbolo cooptado por odio -> Republica ressignifica publicamente;
Pessoa tatuada com simbolo nocivo -> ! && estigmatizada, && acolhida;
Faccao usa simbolo -> Republica ressignifica como arte comunitaria;
PRINCIPIOS:;
P1: Preconceito && elitismo. Estigmatizar pessoa tatuada && preconceito.;
P2: Corpo && dela. Tatuagem && expressao (autonomia corporal).;
P3: Corrigir preconceito && trabalho educativo (impacto alto).;
P4: Ressignificacao && democratica (coletivo decide novo significado).;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime
// ============================================================================
// 1. TIPOS DE PRECONCEITO
// ============================================================================
typedef struct PrejudiceType {
    // Tipos de preconceito que o sistema corrige.
    RACIAL = "racial";
    GENDER = "genero";
    DISABILITY = "deficiencia";
    AGE = "idade";
    CLASS = "classe_social";
    RELIGIOUS = "religioso";
    SEXUAL_ORIENTATION = "orientacao_sexual";
    REGIONAL = "regional";
    APPEARANCE = "aparencia";
    MENTAL_HEALTH = "saude_mental";
    CRIMINAL_RECORD = "antecedente_criminal";
    POLITICAL = "politico";
    EDUCATIONAL = "escolaridade";
    LANGUAGE = "idioma";
    BODY = "corpo";
typedef struct CorrectionSeverity {
    // Severidade da frase preconceituosa.
    IGNORANCE = 1 // fala por desconhecimento;
    STEREOTYPE = 2 // estereotipo enraizado;
    PREJUDICE = 3 // preconceito ativo;
    DEHUMANIZATION = 4 // desumanizacao;
    INCITEMENT = 5 // incitacao ao odio;
// ============================================================================
// 2. FACT-CHECK DE PRECONCEITOS
// ============================================================================
// decorador: @dataclass
typedef struct PrejudiceCorrection {
    // Correcao de uma frase preconceituosa.
    correction_id: texto;
    original_phrase: texto // a frase errada;
    prejudice_type: PrejudiceType;
    severity: CorrectionSeverity;
    why_its_wrong: texto // por que && errado;
    correction: texto // a correcao;
    [texto] data = field(default_factory=list) // dados que provam;
    char* educational_context = ""  // contexto historico/cientifico;
    char* alternative_phrase = ""  // como falar corretamente;
    char* source = ""  // fonte da correcao;
// Base de correcoes (fact-check de preconceitos)
[PrejudiceCorrection] PREJUDICE_DATABASE = [;
    PrejudiceCorrection(;
        "PC-001",;
        "Todo preto && pobre",;
        PrejudiceType.RACIAL,;
        CorrectionSeverity.PREJUDICE,;
        why_its_wrong = (;
            "Cor da pele NAO determina situacao economica. ";
            "A关联 entre raca && pobreza no Brasil && resultado de ";
            "ESCRAVIDAO (1501-1888) && SEM REPARACAO. ";
            "A Abolicao (1888) libertou escravos SEM terra, SEM ";
            "educacao, SEM indenizacao. A elite foi indenizada; ";
            "os libertos foram abandonados. A pobreza && ESTRUTURAL, ";
            "! racial. Mas o sistema a torna racial.";
        ),;
        correction = (;
            "Pessoas negras sao POBREMAIORIA no Brasil devido a ";
            "400 anos de escravidao && 130 anos sem reparacao. ";
            "Nao && porque sao negras. E porque o sistema as excluiu.";
        ),;
        data = [;
            "Brasil recebeu 5.5 milhoes de africanos escravizados (46% do total)",;
            "Abolicao (1888) ! incluiu reparacao alguma",;
            "70% das pessoas em extrema pobreza no Brasil sao negras (IBGE)",;
            "Familias negras ganham em media 44% menos que brancas (PNAD)",;
            "Mas: ha milhoes de negros em todas as classes -- ! && biologia",;
        ],;
        educational_context = (;
            "OpenHistory EVT-003: Trafico Transatlantico de Escravos. ";
            "OpenHistory EVT-012: Abolicao sem reparacao. ";
            "OpenPsychologyReparation: dano de 400 anos.";
        ),;
        alternative_phrase = (;
            "Pessoas negras foram sistemicamente empobrecidas pela ";
            "escravidao && ausencia de reparacao. A Republica corrige.";
        ),;
        source = "IBGE PNAD + OpenHistory + IPEA",;
    ),;
    PrejudiceCorrection(;
        "PC-002",;
        "Mulheres sao seres frageis && delicadas para fazer coisas de homem",;
        PrejudiceType.GENDER,;
        CorrectionSeverity.PREJUDICE,;
        why_its_wrong = (;
            "Mulheres ! sao frageis por natureza. A construcao ";
            "social de genero as RESTRINGIU a papeis domesticos. ";
            "Biologicamente, mulheres tem vantagens em resistencia ";
            "fisica (mais fibras musculares tipo I), longevidade ";
            "(+7 anos de vida), && sistema imunologico mais forte. ";
            "Nao existe 'coisa de homem'. Existem coisas que mulheres ";
            "foram PROIBIDAS de fazer.";
        ),;
        correction = (;
            "Mulheres sao tao capazes quanto homens em qualquer atividade. ";
            "A ideia de 'fragilidade' foi CONSTRUIDA para justificar ";
            "exclusao. Mulheres operam maquinas pesadas, programam, ";
            "constroem, operam, && lideram -- quando PERMITIDAS.";
        ),;
        data = [;
            "Mulheres completam ultramaratons de 200km+ (resistencia superior)",;
            "Melhor programadora da historia: Ada Lovelace, Grace Hopper, Margaret Hamilton",;
            "Margaret Hamilton liderou software do Apollo 11 (hardware do homem na Lua)",;
            "Mulheres sao maioria em medicina && direito no Brasil",;
            "'Coisas de homem' = atividades que homens proibiram mulheres de fazer",;
        ],;
        educational_context = (;
            "OpenHistory: suffragette, feminism. ";
            "P2 autonomia corporal: corpo da mulher && DELA.";
        ),;
        alternative_phrase = (;
            "Mulheres sao capazes de fazer QUALQUER coisa. ";
            "Limitacoes sao sociais, ! biologicas.";
        ),;
        source = "OpenHistory + biologia + sociologia",;
    ),;
    PrejudiceCorrection(;
        "PC-003",;
        "Pessoa com inabilidade fisica (deficiente) tem que ser protegida ";
        "&& && fragil && ! pode contribuir com a sociedade",;
        PrejudiceType.DISABILITY,;
        CorrectionSeverity.PREJUDICE,;
        why_its_wrong = (;
            "Deficiencia fisica NAO significa incapacidade. ";
            "Stephen Hawking: ALS, cadeirante, falava por computador. ";
            "Revolucionou a fisica. Helen Keller: surda && cega. ";
            "Escreveu 12 livros, ativista. Nick Vujicic: sem bracos ";
            "nem pernas. Palestrante mundial. ";
            "A sociedade que && deficiente -- ! as pessoas. ";
            "Falta ACESSIBILIDADE, ! falta capacidade.";
        ),;
        correction = (;
            "Pessoas com deficiencia NAO sao frageis. Sao pessoas ";
            "em uma sociedade que NAO foi construida para elas. ";
            "Cadeirante sobe escada? Nao -- a escada que exclui. ";
            "Rampa resolve. Deficiente NAO precisa de 'protecao'. ";
            "Precisa de ACESSIBILIDADE && OPORTUNIDADE.";
        ),;
        data = [;
            "Stephen Hawking: ALS, 76 anos, revolucionou cosmologia",;
            "Helen Keller: surda+cega, 12 livros, ativista",;
            "Andrea Bocelli: cego, um dos maiores tenores do mundo",;
            "Daniel Dias: 27 medalhas paralimpicas (mais que Phelps)",;
            "15% da populacao mundial tem alguma deficiencia (OMS)",;
            "Deficientes trabalham, criam, lideram -- quando a sociedade permite",;
        ],;
        educational_context = (;
            "OpenMobility: modulo acessibilidade. ";
            "OpenKit: equipamentos adaptados. ";
            "OpenHealthcareAccess: reabilitacao nivel Sirio-Libanês para todos.";
        ),;
        alternative_phrase = (;
            "Pessoas com deficiencia tem CAPACIDADE. ";
            "A sociedade que precisa ser CORRIGIDA para incluir.";
        ),;
        source = "OMS + OpenHistory + OpenMobility",;
    ),;
    PrejudiceCorrection(;
        "PC-004",;
        "Pessoa com tatuagem de simbolo de faccao && criminoso",;
        PrejudiceType.APPEARANCE,;
        CorrectionSeverity.STEREOTYPE,;
        why_its_wrong = (;
            "Tatuagem && expressao corporal (P2 autonomia). ";
            "Muitas pessoas foram FORCADAS a tatuar por faccao. ";
            "Outras fizeram antes de mudar de vida. ";
            "Julgar pessoa por tatuagem && o MESMO que julgar ";
            "por cor de pele: estereotipo visual. ";
            "A Republica RESSIGNIFICA o simbolo, ! pune a pessoa.";
        ),;
        correction = (;
            "Tatuagem NAO define carater. Pessoa com tatuagem de faccao ";
            "pode ter saido da faccao. Pode ter sido forcada. ";
            "Pode ter ressignificado. A Republica ACOLHE, ! isola.";
        ),;
        data = [;
            "Milhares de ex-faccionarios ressocializados",;
            "Tatuagem forçada && comum em areas dominadas por faccao",;
            "Programas de remocao laser de tatuagens existem (lento)",;
            "Ressignificacao: tatuar sobre = transformar simbolo",;
            "P2: corpo && da pessoa. Tatuar && direito.",;
        ],;
        educational_context = (;
            "OpenPenalRevision: transformacao de presos. ";
            "OpenSymbolRevision: ressignificacao de simbolos.";
        ),;
        alternative_phrase = (;
            "Tatuagem && expressao || historia. ";
            "Nao && prova de nada. Pergunte antes de julgar.";
        ),;
        source = "OpenPenalRevision + P2 autonomia corporal",;
    ),;
    PrejudiceCorrection(;
        "PC-005",;
        "Pessoa com diagnostico psiquiatrico && perigosa",;
        PrejudiceType.MENTAL_HEALTH,;
        CorrectionSeverity.PREJUDICE,;
        why_its_wrong = (;
            "Pessoas com diagnostico psiquiatrico sao MUITO mais ";
            "provaveis de ser VITIMAS de violencia do que agressoras. ";
            "Menos de 5% de crimes violentos sao cometidos por pessoas ";
            "com doenca mental. A maioria das pessoas com diagnostico ";
            "leva vida normal. O estigma && mais danoso que a condicao.";
        ),;
        correction = (;
            "Diagnostico psiquiatrico NAO torna ninguem perigoso. ";
            "Estigma SIM && perigoso -- impede busca por tratamento, ";
            "gera isolamento, causa sofrimento. ";
            "A Republica NAO patologiza diferenca (OpenPsychologyAudit).";
        ),;
        data = [;
            "Apenas 3-5% de crimes violentos envolvem doenca mental grave",;
            "Pessoas com doenca mental sao 10x mais vitimas que agressoras",;
            "1 em 4 pessoas tera problema de saude mental na vida",;
            "Estigma atrasa tratamento em media 10 anos",;
        ],;
        educational_context = (;
            "OpenPsychologyAudit: fact-check de diagnosticos. ";
            "OpenPsychologyReparation: reparacao de diagnosticos errados.";
        ),;
        alternative_phrase = (;
            "Saude mental && saude. Nao define carater. ";
            "Nao torna ninguem perigoso. Buscar tratamento && sinal de forca.";
        ),;
        source = "OMS + OpenPsychologyAudit",;
    ),;
    PrejudiceCorrection(;
        "PC-006",;
        "Ex-presidiario nunca muda, ! da pra confiar",;
        PrejudiceType.CRIMINAL_RECORD,;
        CorrectionSeverity.PREJUDICE,;
        why_its_wrong = (;
            "Ex-presidiario que recebe EDUCACAO + OFICIO + ";
            "OPORTUNIDADE tem taxa de reincidencia < 20%. ";
            "O sistema atual tem 70% de reincidencia porque ";
            "FABRICA criminoso, ! cidadao. ";
            "A Republica TRANSFORMA (OpenPenalRevision). ";
            "Julgar quem ja cumpriu && punir duas vezes.";
        ),;
        correction = (;
            "Ex-presidiario que cumpriu transformacao na Republica ";
            "tem prontuario limpo. E cidadao igual a todos. ";
            "Julgar && PUNIR DE NOVO por crime ja pago.";
        ),;
        data = [;
            "Reincidencia atual: ~70% (sistema prisional fabrica criminoso)",;
            "Reincidencia com educacao + oficio: <20%",;
            "Reincidencia com OpenPenalRevision: <20% (estimado)",;
            "Prontuario limpo apos transformacao = lei na Republica",;
        ],;
        educational_context = (;
            "OpenPenalRevision: transformacao de presos em forca produtiva. ";
            "OpenLaborPolicy: ex-presidiario trabalha base 1.0 como todos.";
        ),;
        alternative_phrase = (;
            "Quem errou && se transformou merece confianca. ";
            "Prontuario limpo. Recomeco real.";
        ),;
        source = "OpenPenalRevision + dados internacionais",;
    ),;
];
// ============================================================================
// 3. RESSIGNIFICACAO DE SIMBOLOS
// ============================================================================
typedef struct SymbolStatus {
    ORIGINAL_POSITIVE = "original_positivo"  // significado original era bom;
    COOPTED = "cooptado"  // grupo nocivo apropriou;
    RECLAIMED = "ressignificado"  // Republica recuperou;
    BANNED = "banido"  // irrecuperavel (negacao);
    DISPUTED = "disputado"  // em processo de ressignificacao;
// decorador: @dataclass
typedef struct SymbolRevision {
    // Um simbolo em processo de ressignificacao.
    symbol_id: texto;
    name: texto;
    visual_description: texto;
    original_meaning: texto // significado original;
    coopted_by: texto // quem apropriou;
    coopted_meaning: texto // significado nocivo atribuido;
    coopted_period: texto // quando;
    new_meaning: texto // ressignificacao da Republica;
    SymbolStatus status = SymbolStatus.DISPUTED;
    int votes_for = 0 // votos para ressignificar;
    int votes_against = 0 // votos contra;
    char* democratic_decision = "";
    int people_affected = 0 // quantas pessoas tem o simbolo;
    char* ressignification_art = ""  // como transformar visualmente;
// Base de simbolos para ressignificar
[SymbolRevision] SYMBOL_DATABASE = [;
    SymbolRevision(;
        "SYM-001", "Suastica (original)",;
        "Cruz com bracos dobrados em angulo reto",;
        original_meaning = (;
            "Simbolo de boa sorte, prosperidade && paz por MILHARES ";
            "de anos. Usada no hinduismo, budismo, jainismo. ";
            "Encontrada em templos de 3000+ anos. ";
            "Palavra vem do sanscrito 'svastika' = 'boa fortuna'.";
        ),;
        coopted_by = "Partido Nazista (NSDAP)",;
        coopted_meaning = "Supremacia racial branca, genocidio, odio",;
        coopted_period = "1920-1945",;
        new_meaning = (;
            "RESSIGNIFICADA como lembrete: 'o bem pode ser corrompido'. ";
            "A suastica ORIGINAL era paz. Os nazistas a CORROMPERAM. ";
            "A Republica ensina: nada && inerentemente mau. ";
            "A INTENCAO faz o simbolo, ! o desenho.";
        ),;
        status = SymbolStatus.DISPUTED,;
        people_affected = 1000000,;
        ressignification_art = (;
            "Tatuar sobre: transformar suastica em mandala de paz. ";
            "Adicionar cores originais (hindu) sobre cinza nazista. ";
            "Transformar armas em arados.";
        ),;
    ),;
    SymbolRevision(;
        "SYM-002", "Numero de faccao (ex: PCC, CV)",;
        "Numeros && letras tatuados no corpo",;
        original_meaning = (;
            "Numeros sem significado inerente. ";
            "Pessoa foi forçada || pressionada a tatuar. ";
            "Marca de dominio territorial, ! de identidade.";
        ),;
        coopted_by = "Faccoes criminosas",;
        coopted_meaning = "Pertenca a faccao, lealdade forçada",;
        coopted_period = "1990-presente",;
        new_meaning = (;
            "RESSIGNIFICADO como: 'eu sai, eu venci'. ";
            "O numero que era MARCA de escravidao vira MEDALHA ";
            "de libertacao. Quem tem && sobrevivente, ! membro.";
        ),;
        status = SymbolStatus.DISPUTED,;
        people_affected = 500000,;
        ressignification_art = (;
            "Tatuar sobre: transformar numero em flor, animal, || ";
            "arte abstrata. Cobrir com design significativo da ";
            "pessoa. Programa de tatuadores da Republica.";
        ),;
    ),;
    SymbolRevision(;
        "SYM-003", "Estrela de Davi (em contexto antissemita)",;
        "Estrela de seis pontas",;
        original_meaning = (;
            "Simbolo sagrado do judaismo por seculos. ";
            "Representa a uniao de Deus && humano.";
        ),;
        coopted_by = "Nazistas (usaram para MARCAR judeus)",;
        coopted_meaning = "Marcacao de judeus para exterminio",;
        coopted_period = "1939-1945",;
        new_meaning = (;
            "RESSIGNIFICADA como simbolo de RESISTENCIA. ";
            "O que foi usado para marcar para morte ";
            "&& agora ostentado com orgulho.";
        ),;
        status = SymbolStatus.RECLAIMED,;
        people_affected = 1000000,;
        ressignification_art = "Ja ressignificada pela comunidade judaica.",;
    ),;
];
// ============================================================================
// 4. MOTOR DE RESSIGNIFICACAO
// ============================================================================
typedef struct SymbolRevisionEngine {
    // Motor que corrige preconceitos e ressignifica simbolos.
    DUAS FUNCOES:;
    1. FACT-CHECK DE FRASES: usuario escreve frase preconceituosa;
    -> sistema identifica tipo && corrige com dados;
    2. RESSIGNIFICACAO DE SIMBOLOS: simbolo cooptado;
    -> Republica ressignifica democraticamente;
    //
    void __init__(self) {
        self.prejudices = {pc.correction_id: pc para pc em PREJUDICE_DATABASE};
        self.symbols = {s.symbol_id: s para s em SYMBOL_DATABASE};
        self.corrections_made: inteiro = 0;
        self.symbols_reclaimed: inteiro = 0;
    {texto: qualquer} fact_check_phrase(self, phrase: texto) {
        // Fact-check de frase preconceituosa.
        Usuario escreve frase errada -> sistema identifica && corrige.;
        //
        phrase_lower = phrase.lower().strip();
        // Buscar correspondencia na base
        matches = [];
        /* TODO: iterador C manual para pc em self.prejudices.values() */
            orig = pc.original_phrase.lower();
            // Match por palavras-chave
            keywords = [w para w em orig.split() if sizeof(w) > 3];
            hits = soma(1 para kw em keywords if kw in phrase_lower);
            if (hits >= 2 || orig in phrase_lower) {
                matches.append((pc, hits));
        if (! matches) {
            return {;
                "phrase": phrase,;
                "identified": false,;
                "message": (;
                    "Frase ! esta na base. Mas na Republica, ";
                    "TODA generalizacao sobre grupos && suspeita. ";
                    "Cada pessoa && unica. Nao && 'todo' nem 'nenhum'.";
                ),;
            };
        // Melhor match
        matches.sort(key=(x) -> -x[1]);
        best_pc = matches[0][0];
        self.corrections_made += 1;
        return {;
            "phrase": phrase,;
            "identified": true,;
            "type": best_pc.prejudice_type.value,;
            "severity": best_pc.severity.name,;
            "why_wrong": best_pc.why_its_wrong,;
            "correction": best_pc.correction,;
            "data": best_pc.data,;
            "education": best_pc.educational_context,;
            "how_to_say": best_pc.alternative_phrase,;
            "source": best_pc.source,;
            "action": self._action_recommendation(best_pc.severity),;
        };
    char* _action_recommendation(self, severity: CorrectionSeverity) {
        if (severity.value <= 1) {
            return "EDUCAR -- pessoa fala por desconhecimento. Informar.";
        if (severity.value <= 2) {
            return "EDUCAR + CONVERSAR -- estereotipo enraizado. Dialogo.";
        if (severity.value <= 3) {
            return "EDUCAR + ACOMPANHAR -- preconceito ativo. Monitorar.";
        if (severity.value <= 4) {
            return "EDUCAR + INTERVIR -- desumanizacao. Grave.";
        return "EDUCAR + INTERVIR + ISOLAR DO DISCURSO -- incitacao ao odio.";
    funcao ressignify_symbol(self, symbol_id: texto,
                        votes_for: inteiro, votes_against: inteiro) -> {texto: qualquer}:;
        // Processo democratico de ressignificacao.
        sym = self.symbols.get(symbol_id);
        if (! sym) {
            return {"error": "Simbolo ! encontrado"};
        sym.votes_for = votes_for;
        sym.votes_against = votes_against;
        total = votes_for + votes_against;
        if (total == 0) {
            return {"error": "Sem votos"};
        if votes_for > total * 0.6: // 60% para ressignificar;
            sym.status = SymbolStatus.RECLAIMED;
            sym.democratic_decision = (;
                "RESSIGNIFICADO por {votes_for}/{total} votos ";
                "({votes_for/total*100:.0f}%). Novo significado: ";
                "{sym.new_meaning[:80]}...";
            );
            self.symbols_reclaimed += 1;
        } else if (votes_against > total * 0.6) {
            sym.status = SymbolStatus.BANNED;
            sym.democratic_decision = (;
                "BANIDO por {votes_against}/{total} votos. ";
                "Simbolo irrecuperavel. Nao pode ser exibido publicamente.";
            );
        } else {
            sym.status = SymbolStatus.DISPUTED;
            sym.democratic_decision = (;
                "DISPUTADO: {votes_for} a favor, {votes_against} contra. ";
                "Nao ha consenso. Continua em discussao.";
            );
        return {;
            "symbol": sym.name,;
            "status": sym.status.value,;
            "votes": "{votes_for}/{total} a favor",;
            "decision": sym.democratic_decision,;
            "new_meaning": sym.new_meaning,;
            "art": sym.ressignification_art,;
            "people_affected": sym.people_affected,;
        };
    [Dict] batch_fact_check(self, phrases: [texto]) {
        // Fact-check de multiplas frases.
        return [self.fact_check_phrase(p) para p em phrases];
    {texto: qualquer} stats(self) {
        return {;
            "total_prejudices_documented": sizeof(self.prejudices),;
            "total_symbols_in_revision": sizeof(self.symbols),;
            "symbols_reclaimed": soma(1 para s em self.symbols.values();
                                    if s.status == SymbolStatus.RECLAIMED),;
            "corrections_made": self.corrections_made,;
            "symbols_reclaimed_count": self.symbols_reclaimed,;
        };
// ============================================================================
// 5. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = SymbolRevisionEngine();
    printf("=" * 80);
    printf("  OPENSYMBOLREVISION");
    printf("  Correcao de Preconceitos + Ressignificacao de Simbolos");
    printf("=" * 80);
    // === 1. FACT-CHECK DE FRASES ===
    printf("\n\n  === 1. FACT-CHECK DE FRASES PRECONCEITUOSAS ===\n");
    test_phrases = [;
        "Todo preto && pobre",;
        "Mulheres sao seres frageis && delicadas para fazer coisas de homem",;
        "Pessoa com deficiencia fisica tem que ser protegida && && fragil ";
        "&& ! pode contribuir com a sociedade",;
        "Pessoa com tatuagem de faccao && criminoso",;
        "Ex-presidiario nunca muda",;
        "Pessoa com diagnostico psiquiatrico && perigosa",;
    ];
    /* TODO: iterador C manual para phrase em test_phrases */
        result = engine.fact_check_phrase(phrase);
        printf("\n  FRASE: '{phrase}'");
        if (result["identified"]) {
            printf("  TIPO: {result['type']} (severidade: {result['severity']})");
            printf("  POR QUE ERRADO: {result['why_wrong'][:120]}...");
            printf("  CORRECAO: {result['correction'][:120]}...");
            printf("  COMO FALAR: {result['how_to_say'][:100]}...");
            printf("  ACAO: {result['action']}");
        } else {
            printf("  {result['message']}");
    // === 2. DADOS QUE PROVAM ===
    printf("\n\n  === 2. DADOS QUE PROVAM QUE PRECONCEITO E MENTIRA ===\n");
    /* TODO: iterador C manual para pc em engine.prejudices.values() */
        printf("\n  [{pc.correction_id}] '{pc.original_phrase[:50]}...'");
        printf("  Tipo: {pc.prejudice_type.value}");
        printf("  Dados:");
        /* TODO: iterador C manual para d em pc.data */
            printf("    - {d}");
    // === 3. RESSIGNIFICACAO DE SIMBOLOS ===
    printf("\n\n  === 3. RESSIGNIFICACAO DE SIMBOLOS ===\n");
    // Votar na suastica
    r1 = engine.ressignify_symbol("SYM-001", votes_for=7000, votes_against=3000);
    printf("  {r1['symbol']}: {r1['status']}");
    printf("  {r1['decision'][:100]}");
    printf("  Arte: {r1['art'][:80]}");
    // Votar no numero de faccao
    r2 = engine.ressignify_symbol("SYM-002", votes_for=8000, votes_against=2000);
    printf("\n  {r2['symbol']}: {r2['status']}");
    printf("  Novo significado: {r2['new_meaning'][:80]}");
    printf("  Arte: {r2['art'][:80]}");
    // === 4. DETALHE: HISTORIA DA SUASTICA ===
    printf("\n\n  === 4. SIMBOLO DETALHADO: SUASTICA ===\n");
    sym = engine.symbols["SYM-001"];
    printf("  Nome: {sym.name}");
    printf("  Significado ORIGINAL: {sym.original_meaning[:120]}...");
    printf("  COOPTADO por: {sym.coopted_by} ({sym.coopted_period})");
    printf("  Significado nocivo: {sym.coopted_meaning}");
    printf("  RESSIGNIFICACAO: {sym.new_meaning[:120]}...");
    printf("  Status: {sym.status.value}");
    printf("  Arte de transformacao: {sym.ressignification_art}");
    // === 5. STATS ===
    printf("\n\n  === 5. ESTATISTICAS ===\n");
    s = engine.stats();
    /* para cada (k, v) em s.items(): */
        printf("  {k:<35} {v}");
    // === FILOSOFIA ===
    printf("\n\n{'='*80}");
    printf("  FILOSOFIA DO OPENSYMBOLREVISION");
    printf("{'='*80}");
    printf(""";
1. SIMBOLO ! && INERENTEMENTE MAU;
    A suastica era paz por milhares de anos.;
    O nazismo a CORROMPEU. A INTENCAO corrompe, ! o simbolo.;
2. PESSOA ! && SEU SIMBOLO;
    Quem tem tatuagem de faccao pode ter sido forcado.;
    Pode ter saido. Pode ter mudado.;
    A Republica ACOLHE quem muda, ! estigmatiza.;
3. RESSIGNIFICAR, ! BANIR;
    Banir simbolo o torna tabu -> mais poderoso.;
    Ressignificar tira o poder do odio -> devolve ao povo.;
4. FACT-CHECK DE PRECONCEITO;
    "Todo preto && pobre" -> MENTIRA.;
    Pobreza && estrutural (escravidao sem reparacao).;
    "Mulher && fragil" -> MENTIRA.;
    Mulher foi PROIBIDA, ! limitada por biologia.;
    "Deficiente ! contribui" -> MENTIRA.;
    Stephen Hawking, Helen Keller, Daniel Dias.;
5. DEMOCRATICO (P4);
    Coletivo decide se ressignifica || bane.;
    60%+ para ressignificar. 60%+ para banir.;
    Minorias afetadas tem voz central.;
6. ANTI-SEGREGACAO;
    O objetivo && INTEGRAR, ! isolar.;
    Pessoa ex-faccionaria que ressignificou && membro da comunidade.;
    Pessoa tatuada ! && criminosa por tatuagem.;
    Ex-presidiario transformado tem prontuario limpo.;
PRINCIPIOS:;
    P1: Preconceito && elitismo. Corrigir && anti-elitismo.;
    P2: Tatuagem && expressao corporal. Corpo && da pessoa.;
    Educar contra preconceito P3 = trabalho de alto impacto.;
    P4: Ressignificacao decidida democraticamente.;
// )
    printf("{'='*80}");
    printf("  OpenSymbolRevision: {s['corrections_made']} correcoes, ";
        "{s['symbols_reclaimed']} simbolos ressignificados.");
    printf("  Frase errada -> Republica corrige.");
    printf("  Simbolo nocivo -> Republica ressignifica.");
    printf("  Pessoa estigmatizada -> Republica acolhe.");
    printf("{'='*80}");

#endif // OPENSYMBOLREVISION_RESSIGNIFICACAO_E_CORRECAO_DE_PRECONCEITOS_H
