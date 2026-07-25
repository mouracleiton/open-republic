/* OpenRelationships -- Politica de Transparencia Relacional + Anti-Inveja -- gerado de Portugol++ */
#ifndef OPENRELATIONSHIPS_POLITICA_DE_TRANSPARENCIA_RELACIONAL_ANTI_INVEJA_H
#define OPENRELATIONSHIPS_POLITICA_DE_TRANSPARENCIA_RELACIONAL_ANTI_INVEJA_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenRelationships -- Politica de Transparencia Relacional + Anti-Inveja;
=========================================================================;
PERGUNTA SUBMETIDA A ASSEMBLEIA:;
"Todo relacionamento tem que ser publico? As pessoas precisam saber;
/* para nao cometer o problema de invasao de espaco. Nada de esconder." */
O QUE A ASSEMBLEIA DECIDIU:;
APROVADO COM NUANCES:;
1. RELACIONAMENTOS DECLARADOS (sim, publicos);
    - Todo relacionamento && registrado no OpenSocialNetwork;
    - Motivo: evitar invasao de espaco alheio;
    - Motivo: transparencia gera confianca;
    - Motivo: anti-inveja (saber que alguem esta com alguem elimina disputa);
2. MAS P2 AUTONOMIA (! obrigacao de detalhe);
    - VOCE declara que esta com quem (fato, ! detalhe);
    - Ninguem && obrigado a detalhar a RELACAO (intimidade);
    - "Estou com Maria" = sim. "O que faco com Maria" = !;
3. ANTI-INVEJA (politica complementar);
    - Inveja && reconhecida como doenca social;
    - Republica ! competi por pessoas;
    - Todo cidadao && suficiente (OpenCreator + OpenCredit);
    - Quem tem relacionamento ! && "melhor";
    - Quem ! tem ! && "pior";
4. O QUE ! EXISTE:;
    - Traicao (se tudo && publico, ! ha o que esconder);
    - Ciume possessivo (cada corpo && livre -- P2);
    - "Tomar" pessoa de outro (ninguem && dono de ninguem);
    - Relacionamento secreto (publico = regra);
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime
// ============================================================================
// 1. TIPOS DE RELACIONAMENTO
// ============================================================================
typedef struct RelationshipType {
    PARTNER = "namoro"  // namoro;
    MARRIAGE = "uniao"  // uniao estavel / casamento;
    DATING = "encontro"  // ficante / encontro casual;
    COMPANIONSHIP = "companhia"  // companhia (! sexual);
    CO_PARENTING = "coparentalidade"  // criar filhos juntos;
    POLY = "poliafectivo"  // relacionamento multilo;
    FRIENDSHIP_INTIMATE = "amizade_intima"  // melhor amigo(a);
    MENTORSHIP = "mentoria"  // mentor/aprendiz;
typedef struct RelationshipStatus {
    ACTIVE = "ativo";
    PAUSED = "pausado";
    ENDED = "encerrado";
    MUTUAL_AGREEMENT = "acordo_mutuo";
// decorador: @dataclass
typedef struct Relationship {
    // Um relacionamento declarado publicamente.
    rel_id: texto;
    person_a: texto;
    person_b: texto;
    rel_type: RelationshipType;
    RelationshipStatus status = RelationshipStatus.ACTIVE;
    char* declared_date = "";
    char* ended_date = "";
    bool public = true // TODOS sao publicos (regra);
    int children = 0;
    char* notes = ""  // optional (P2 -- sem detalhar intimidade);
    // Anti-inveja
    char* public_recognition = "relacao_normal"  // ! && "melhor" nem "pior";
// ============================================================================
// 2. ANTI-INVEJA
// ============================================================================
typedef struct EnvyType {
    RELATIONAL = "relacional"  // inveja de quem tem relacionamento;
    MATERIAL = "material"  // inveja de bens (! existe -- CC0);
    STATUS = "status"  // inveja de reconhecimento;
    PHYSICAL = "fisica"  // inveja de aparencia (anti--combate);
// decorador: @dataclass
typedef struct EnvyCase {
    // Caso de inveja identificado para tratamento.
    case_id: texto;
    person: texto;
    envy_type: EnvyType;
    target: texto // de quem tem inveja;
    char* description = "";
    char* treatment = "";
    bool resolved = false;
// ============================================================================
// 3. VOTACAO DA ASSEMBLEIA
// ============================================================================
{texto: qualquer} run_relationship_assembly(n_voters: inteiro = 10000) {
    // Assembleia constituinte sobre transparencia relacional.
    PERGUNTA:;
    "Todo relacionamento deve ser publico para evitar invasao de espaco?";
    OPCOES:;
    A) SIM -- todo relacionamento publico (declarar no OpenSocialNetwork);
    B) PARCIAL -- publico o fato, privado os detalhes;
    C) ! -- cada um decide o que revelar;
    //
    votes_a = 0 // publico total;
    votes_b = 0 // parcial (fato sim, detalhe !);
    votes_c = 0 // privado;
    /* TODO: iterador C manual para _ em intervalo(n_voters) */
        r = random.random();
        if (r < 0.45) {
            votes_a = votes_a + 1 // 45% -- publico;
        } else if (r < 0.85) {
            votes_b = votes_b + 1 // 40% -- parcial (P2 protege detalhe);
        } else {
            votes_c = votes_c + 1 // 15% -- privado;
    // Combinando A + B (ambos querem declaracao publica do FATO)
    want_public_fact = votes_a + votes_b;
    return {;
        "question": (;
            "Todo relacionamento deve ser publico para evitar ";
            "invasao de espaco && combater inveja?";
        ),;
        "votes_public_total": votes_a,;
        "votes_partial_p2": votes_b,;
        "votes_private": votes_c,;
        "total": n_voters,;
        "want_public_fact_pct": "{want_public_fact/n_voters*100:.0f}%",;
        want_public_fact > n_voters * 0.5 ? "result": "APROVADO" : "REJEITADO",;
        "decision": {
            "declarar_relacionamento": true,         // SIM (85%);
            "detalhar_intimidade": false,             // ! (P2 protege);
            "evitar_invasao": true,                   // SIM;
            "combater_inveja": true,                  // SIM;
            "poliafetivo_aceito": true,               // SIM (P2);
            "relacionamento_secreto": false,          // PROIBIDO;
            "tricao_conceito": false,                 // ! EXISTE (tudo publico);
            "ciume_possessivo": false,                // PROIBIDO (P2 corpo livre);
            "pessoa_e_possuida": false,               // NINGUEM && DONO (P2);
        },;
    };
// ============================================================================
// 4. MOTOR DE RELACIONAMENTOS
// ============================================================================
typedef struct RelationshipEngine {
    // Motor de relacionamentos transparentes da Republica.
    PRINCIPIOS:;
    1. PUBLICO: declarar relacionamento evita invasao de espaco;
    2. P2: detalhes da intimidade sao PRIVADOS (ninguem obrigado);
    3. ANTI-INVEJA: ter relacionamento ! && status. Nao ter ! && falha.;
    4. ANTI-POSSESSAO: ninguem && dono de ninguem. Corpo && livre (P2).;
    5. ANTI-TRAICAO: se tudo && publico, ! ha o que esconder;
    6. POLIAFETIVO: aceito (P2 autonomia corporal total);
    7. CO-PARENTALIDADE: criar filhos sem obrigacao romantica;
    //
    void __init__(self) {
        self.relationships: {texto: Relationship} = {};
        self.envy_cases: {texto: EnvyCase} = {};
        self.stats_declared: inteiro = 0;
        self.stats_ended: inteiro = 0;
        self.stats_envy_resolved: inteiro = 0;
    funcao declare_relationship(self, person_a: texto, person_b: texto,
                            rel_type: RelationshipType,;
                            char* notes = "") -> {texto: qualquer}:;
        // Declara relacionamento publicamente.
        rel_id = hashlib.md5(;
            "{person_a}{person_b}{datetime.now()}".encode();
        ).hexdigest()[:8];
        rel = Relationship(;
            rel_id = rel_id, person_a=person_a, person_b=person_b,;
            rel_type = rel_type,;
            declared_date <- datetime.now().isoformat(),;
            notes = notes,;
        );
        self.relationships[rel_id] = rel;
        self.stats_declared += 1;
        return {;
            "declared": true,;
            "rel_id": rel_id,;
            "relationship": "{person_a} + {person_b}",;
            "type": rel_type.value,;
            "status": "PUBLICO",;
            "intimacy_detail": "PRIVADO (P2 -- ! obrigado)",;
            "message": (;
                "Relacionamento declarado: {person_a} + {person_b} ({rel_type.value}). ";
                "PUBLICO no OpenSocialNetwork. ";
                "Comunidade sabe. Ninguem invade espaco. ";
                "Sem inveja -- && vida normal.";
            ),;
        };
    funcao end_relationship(self, rel_id: texto,
                        bool mutual = true) -> {texto: qualquer}:;
        // Encerra relacionamento publicamente.
        rel = self.relationships.get(rel_id);
        if (! rel) {
            return {"error": "Relacionamento ! encontrado"};
        rel.status = RelationshipStatus.ENDED;
        rel.ended_date = datetime.now().isoformat();
        self.stats_ended += 1;
        return {;
            "ended": true,;
            "relationship": "{rel.person_a} + {rel.person_b}",;
            "mutual": mutual,;
            "public_announcement": (;
                "Relacionamento encerrado: {rel.person_a} + {rel.person_b}. ";
                "Mutuo acordo. Ambos livres. ";
                "Comunidade sabe. Ninguem invade.";
            ),;
            "message": (;
                "Encerrado. Ambos voltam a estar disponiveis. ";
                "Sem drama. Sem ciume. Sem possessao. P2 corpo livre.";
            ),;
        };
    {texto: qualquer} check_status(self, person: texto) {
        // Verifica status relacional de uma pessoa (publico).
        active = [];
        ended = [];
        /* TODO: iterador C manual para rel em self.relationships.values() */
            if (person in (rel.person_a, rel.person_b)) {
                partner = person == rel.person_a ? rel.person_b : rel.person_a;
                if (rel.status == RelationshipStatus.ACTIVE) {
                    active.append({
                        "partner": partner,;
                        "type": rel.rel_type.value,;
                        "since": rel.declared_date[:10],;
                    });
                } else {
                    ended.append({"partner": partner});
        return {;
            "person": person,;
            "current_relationships": active,;
            "past_relationships": sizeof(ended),;
            "available": sizeof(active) == 0,;
            "message": (;
                "{person}: {len(active)} relacionamento(s) ativo(s). ";
                "{'DISPONIVEL' if not active else 'EM RELACIONAMENTO'}. ";
                "Antes de se aproximar: VERIFIQUE. Nao invada.";
            ),;
        };
    funcao report_envy(self, person: texto, target: texto,
                    EnvyType envy_type = EnvyType.RELATIONAL,;
                    char* description = "") -> {texto: qualquer}:;
        // Trata caso de inveja relacional/material.
        ANTI-INVEJA:;
        Na Republica, inveja && tratada como sinal de que a pessoa;
        precisa de RECONHECIMENTO (OpenCreator) || de AUTONOMIA (P2).;
        Ninguem inveja quem tem relacionamento se voce && SUFICIENTE.;
        A Republica garante que cada cidadao && suficiente.;
        //
        case_id = hashlib.md5(;
            "{person}{target}{datetime.now()}".encode();
        ).hexdigest()[:8];
        treatments = {
            EnvyType.RELATIONAL: (;
                "Tratamento: OpenPsychology (sem rotular). ";
                "Construcao de auto-estima. ";
                "Republica garante: relacionamento ! && status. ";
                "Voce && SUFICIENTE sozinho.";
            ),;
            EnvyType.MATERIAL: (;
                "Tratamento: Nao ha bens materiais para invejar (CC0). ";
                "Tudo && bem comum. Inveja material && ILOGICA na Republica.";
            ),;
            EnvyType.STATUS: (;
                "Tratamento: OpenCreator reconhecimento. ";
                "Todo mundo && reconhecido pelo impacto. ";
                "Voce tem impacto proprio. Compare consigo mesmo.";
            ),;
            EnvyType.PHYSICAL: (;
                "Tratamento: OpenBeauty disponivel para todos (ZERO custo). ";
                "Aparencia && ajustavel. Valor && interno.";
            ),;
        };
        case = EnvyCase(;
            case_id = case_id, person=person, target=target,;
            envy_type = envy_type, description=description,;
            treatment = treatments.get(envy_type, ""),;
        );
        self.envy_cases[case_id] = case;
        self.stats_envy_resolved += 1;
        return {;
            "case_id": case_id,;
            "person": person,;
            "target": target,;
            "envy_type": envy_type.value,;
            "treatment": case.treatment,;
            "message": (;
                "Inveja identificada: {person} -> {target}. ";
                "Nao && culpa. E sinal. {case.treatment}";
            ),;
        };
    {texto: qualquer} stats(self) {
        return {;
            "total_relationships": sizeof(self.relationships),;
            "active": soma(1 para r em self.relationships.values();
                        if r.status == RelationshipStatus.ACTIVE),;
            "ended": self.stats_ended,;
            "envy_cases_treated": self.stats_envy_resolved,;
            "secret_relationships": 0,   // ! EXISTEM;
            "tracoes_registered": 0,      // ! EXISTE (tudo publico);
        };
// ============================================================================
// 5. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = RelationshipEngine();
    printf("=" * 80);
    printf("  OPENRELATIONSHIPS -- TRANSPARENCIA RELACIONAL + ANTI-INVEJA");
    printf("  Assembleia Constituinte sobre relacionamentos publicos");
    printf("=" * 80);
    // === 1. PERGUNTA A ASSEMBLEIA ===
    printf("\n\n  === 1. PERGUNTA A ASSEMBLEIA ===\n");
    printf('  "Todo relacionamento deve ser publico para evitar');
    printf('   invasao de espaco && combater inveja?"');
    // === 2. VOTACAO ===
    printf("\n\n  === 2. VOTACAO (10.000 cidadaos) ===\n");
    result = run_relationship_assembly(10000);
    printf("  PUBLICO TOTAL (fato + detalhe): {result['votes_public_total']:>6} ";
        "({result['votes_public_total']/100:.0f}%)");
    printf("  PARCIAL (fato sim, detalhe !): {result['votes_partial_p2']:>6} ";
        "({result['votes_partial_p2']/100:.0f}%)");
    printf("  PRIVADO (cada um decide):       {result['votes_private']:>6} ";
        "({result['votes_private']/100:.0f}%)");
    printf("\n  Querem fato publico (A+B): {result['want_public_fact_pct']}");
    printf("  RESULTADO: {result['result']}");
    // === 3. DECISAO DA ASSEMBLEIA ===
    printf("\n\n  === 3. DECISAO DA ASSEMBLEIA ===\n");
    d = result["decision"];
    /* para cada (key, val) em d.items(): */
        status = val ? "SIM" : "NAO";
        printf("  {key:<30} {status}");
    // === 4. DECLARAR RELACIONAMENTOS ===
    printf("\n\n  === 4. RELACIONAMENTOS DECLARADOS ===\n");
    rels = [;
        ("Cleiton", "Maria", RelationshipType.PARTNER),;
        ("Joao", "Ana", RelationshipType.MARRIAGE),;
        ("Pedro", "Beatriz", RelationshipType.DATING),;
        ("Lucas", "Sofia", RelationshipType.POLY),;
        ("Tobias", "Dona Rita", RelationshipType.COMPANIONSHIP),;
    ];
    /* para a, b, rtype in rels: */
        result_decl = engine.declare_relationship(a, b, rtype);
        printf("  {a:<12} + {b:<12} -> {rtype.value:<15} ";
            "[{result_decl['status']}]");
    // === 5. VERIFICAR STATUS ===
    printf("\n\n  === 5. VERIFICACAO DE STATUS (anti-invasao) ===\n");
    /* TODO: iterador C manual para person em ["Cleiton", "Carlos", "Joao", "Ana"] */
        status = engine.check_status(person);
        avail = status["available"] ? "DISPONIVEL" : "EM RELACIONAMENTO";
        printf("  {person:<12} -> {avail}", end="");
        if (status["current_relationships"]) {
            /* TODO: iterador C manual para rel em status["current_relationships"] */
                printf(" ({rel['partner']}, {rel['type']})", end="");
        printf();
    // === 6. ENCERRAR RELACIONAMENTO ===
    printf("\n\n  === 6. ENCERRAMENTO PUBLICO ===\n");
    rels_list = list(engine.relationships.keys());
    if (rels_list) {
        end_result = engine.end_relationship(rels_list[2], mutual=true);
        printf("  {end_result['public_announcement']}");
        printf("  {end_result['message']}");
    // === 7. ANTI-INVEJA ===
    printf("\n\n  === 7. ANTI-INVEJA ===\n");
    envies = [;
        ("Carlos", "Cleiton", EnvyType.RELATIONAL,;
        "Carlos tem inveja de Cleiton ter relacionamento"),;
        ("Jose", "Pedro", EnvyType.STATUS,;
        "Jose acha que Pedro && mais reconhecido"),;
        ("Marcos", "Joao", EnvyType.PHYSICAL,;
        "Marcos acha Joao mais bonito"),;
    ];
    /* para person, target, etype, desc in envies: */
        result_envy = engine.report_envy(person, target, etype, desc);
        printf("\n  {result_envy['person']} -> {result_envy['target']} ";
            "({result_envy['envy_type']})");
        printf("  {result_envy['treatment'][:80]}");
    // === 8. STATS ===
    printf("\n\n  === 8. ESTATISTICAS ===\n");
    s = engine.stats();
    /* para cada (k, v) em s.items(): */
        printf("  {k:<30} {v}");
    // === FILOSOFIA ===
    printf("\n\n{'='*80}");
    printf("  FILOSOFIA DO OPENRELATIONSHIPS");
    printf("{'='*80}");
    printf(""";
ASSEMBLEIA DECIDIU (85% a favor do fato publico):;
1. RELACIONAMENTOS SAO PUBLICOS;
    Todo relacionamento && declarado no OpenSocialNetwork.;
    Motivo: evitar invasao de espaco alheio.;
    Se Maria sabe que Joao esta com Ana, Maria ! se aproxima.;
    Transparencia = respeito.;
2. MAS INTIMIDADE && PRIVADA (P2);
    "Estou com Maria" = PUBLICO (fato).;
    "O que faco com Maria" = PRIVADO (detalhe).;
    P2 autonomia corporal protege os DETALHES.;
    Ninguem && obrigado a detalhar a relacao.;
3. O QUE ISSO ELIMINA:;
    - TRAICAO: se tudo && publico, ! ha o que esconder.;
    "Traicao" deixa de existir como conceito.;
    - CIUME POSSESSIVO: ninguem && dono de ninguem (P2).;
    Se a pessoa escolhe outro, && DIREITO DELA.;
    - "TOMAR" PESSOA: ! se toma o que ! && possuido.;
    Pessoas ! sao objetos.;
    - INVASAO DE ESPACO: todo mundo sabe quem esta com quem.;
    Ninguem "mete o nariz" por engano.;
4. ANTI-INVEJA (politica complementar):;
    Inveja && SINAL de que a pessoa precisa:;
    - Auto-estima (OpenPsychology sem rotular);
    - Reconhecimento (OpenCreator -- todo mundo tem impacto);
    - Autonomia (P2 -- voce && suficiente);
    - Aparencia (OpenBeauty ZERO custo);
    Na Republica:;
    - Relacionamento ! && status (! && "melhor" ter);
    - Solteiro ! && falha (! && "pior" ! ter);
    - Bens materiais ! existem para invejar (CC0);
    - Status vem do IMPACTO (todo mundo tem);
5. POLIAFETIVO ACEITO (P2):;
    Relacionamento com mais de uma pessoa && ACEITO.;
    Desde que TODOS sabem && CONSENTEM.;
    Transparencia = ninguem && enganado.;
    P2: corpo de cada um. Escolha de cada um.;
6. O QUE ! EXISTE:;
    - Relacionamento secreto (PROIBIDO -- gera invasao);
    - Traicao (tudo publico, nada a esconder);
    - Ciume possessivo (P2 corpo livre);
    - Posse de pessoa (ninguem && dono);
    - Inveja de relacionamento (tratada);
    - Inveja material (ilologica -- CC0);
PRINCIPIOS:;
    P1: Relacionamento ! && status. Solteiro ! && inferior.;
    P2: Corpo && de cada um. Escolha && de cada um. Detalhe && privado.;
    P3: Relacionamento ! conta como trabalho (! && contribuicao).;
    P4: Assembleia votou. 85% a favor. Regra aplicada.;
// )
    printf("{'='*80}");
    printf("  OpenRelationships: {s['total_relationships']} declarados, ";
        "{s['active']} ativos, ";
        "{s['envy_cases_treated']} casos de inveja tratados.");
    printf("  Publico no fato. Privado na intimidade. Sem inveja.");
    printf("{'='*80}");

#endif // OPENRELATIONSHIPS_POLITICA_DE_TRANSPARENCIA_RELACIONAL_ANTI_INVEJA_H
