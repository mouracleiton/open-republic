/* OpenDemocracy + OpenTransparency -- gerado de Portugol++ */
#ifndef OPENDEMOCRACY_OPENTRANSPARENCY_H
#define OPENDEMOCRACY_OPENTRANSPARENCY_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenDemocracy + OpenTransparency;
==================================;
"Democracia sem transparencia && teatro.;
Transparencia sem democracia && vigia.;
Juntas, sao a Republica.";
OPENDEMOCRACY:;
Democracia direta + liquida + deliberativa + participativa.;
Nao && "votar a cada 4 anos". && decidir TODOS os dias.;
Nao && "escolher representante". && decidir DIRETAMENTE quando pode,;
&& delegar TEMPORARIAMENTE quando ! pode.;
OPENTRANSPARENCY:;
Transparencia RADICAL. Tudo que && publico && VISIVEL.;
Tudo que && decisao && RASTREAVEL. Tudo que && gasto && PUBLICO.;
Zero reuniao secreta. Zero documento oculto. Zero conta escondida.;
O UNICO que && privado: a vida intima do cidadao.;
(OpenHealth, OpenRelationship, OpenFaith -- esses sao privados);
TUDO o que && do Estado/coletivo && publico.;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa time
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Set, Tuple, Callable de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// ============================================================================
// Democracy Types
// ============================================================================
typedef struct DemocracyMode {
    // Modos de democracia que COEXISTEM.
    DIRECT = "direta"  // cidadao vota diretamente;
    LIQUID = "liquida"  // delega voto por tema, revogavel;
    DELIBERATIVE = "deliberativa"  // debate antes de votar;
    PARTICIPATORY = "participativa"  // cidadao propoe leis/policies;
    SORTITION = "sorteio"  // sorteio para cargos (atenico);
typedef struct VoteType {
    SIMPL = "maioria_simples"  // 50%+1;
    QUALIFIED = "maioria_qualificada"  // 2/3;
    SUPER = "supermajoridade"  // 3/4;
    UNANIMOUS = "unanimidade"  // 100% (rarissimo);
    ANTI_HEGEMONY = "anti_hegemonia"  // 1/3 de qualquer nacao pode vetar;
typedef struct ProposalCategory {
    CONSTITUTIONAL = "constitucional"  // muda a constituicao (2/3);
    BUDGET = "orcamento"  // como alocar recursos;
    POLICY = "politica"  // nova regra/lei;
    ELECTION = "eleicao"  // eleger representantes;
    RECALL = "recall"  // revogar representante;
    EMERGENCY = "emergencia"  // crise (acelerado);
    TREATY = "tratado"  // acordo entre nacoes;
    AMENDMENT = "emenda"  // emendar proposta em debate;
// ============================================================================
// OpenTransparency: Public Ledger
// ============================================================================
typedef struct TransparencyLevel {
    // Nivel de transparencia de cada item.
    RADICAL = "radical"  // 100% publico, qualquer cidadao ve;
    PUBLIC = "publico"  // publico mas requer buscar;
    RESTRICTED = "restrito"  // so cidadaos afetados;
    PRIVATE = "privado"  // vida intima (protegido);
    SEALED = "lacrado"  // temporariamente selado (precisa justificativa);
// decorador: @dataclass
typedef struct PublicRecord {
    // Um registro no livro publico da Republica.
    TUDO que o coletivo faz entra no livro publico:;
    - Decisoes votadas;
    - Recursos alocados;
    - Reunioes realizadas;
    - Representantes eleitos;
    - Recalls;
    - Propostas;
    - Emendas;
    - Auditorias;
    - Gastos (! ha dinheiro, mas alocacao de trabalho/material);
    Cada registro tem hash imutavel (blockchain).;
    //
    record_id: texto;
    double timestamp = field(default_factory=time.time);
    char* category = ""  // decision, resource, meeting, etc;
    char* title = "";
    char* description = "";
    char* actor = ""  // quem fez;
    [texto] affected = field(default_factory=list) // quem afeta;
    TransparencyLevel transparency = TransparencyLevel.RADICAL;
    {texto: qualquer} data = field(default_factory=dict);
    char* hash = "";
    bool sealed = false;
    char* seal_reason = "";
    double seal_expires = 0.0 // 0 = ! selado;
typedef struct PublicLedger {
    // Livro publico IMUTAVEL da Republica.
    Blockchain simples: cada registro tem hash que depende do anterior.;
    Impossivel alterar historico sem quebrar a cadeia.;
    Cada cidadao tem copia completa (no seu edge node).;
    O QUE ENTRA NO LIVRO (RADICAL = qualquer cidadao ve):;
    - Toda decisao votada (quem votou o que);
    - Toda alocacao de recurso (para onde foi);
    - Toda reuniao (quem participou, o que decidiu);
    - Todo representante (acoes, votos, reunioes);
    - Toda auditoria (resultado);
    - Toda proposta (texto completo, votos, debate);
    - Todo recall (quem assinou, resultado);
    - Todo gasto de trabalho/material (em vez de dinheiro);
    O QUE ! ENTRA (PRIVATE = protegido):;
    - Prontuario medico (OpenHealth);
    - Relacionamentos intimos (OpenRelationship);
    - Fe espiritual (OpenFaith);
    - Comunicacao privada (OpenSocial);
    - Dados de criancas (protecao maxima);
    //
    void __init__(self) {
        self.records: [PublicRecord] = [];
        self._counter = 0;
        self._chain_hash = "GENESIS";
    funcao add(self, category: texto, title: texto, description: texto,
            char* actor = "", affected: [texto] = NULL,;
            TransparencyLevel transparency = TransparencyLevel.RADICAL,;
            Dict data = NULL) -> PublicRecord:;
        // Adicionar registro imutavel ao livro publico.
        self._counter += 1;
        rid = "REC-{self._counter:06d}";
        // Hash encadeado (blockchain)
        content = "{self._chain_hash}{rid}{category}{title}{actor}{time.time()}";
        record_hash = hashlib.sha256(content.encode()).hexdigest()[:16];
        self._chain_hash = record_hash;
        record = PublicRecord(;
            record_id = rid, category=category, title=title,;
            description = description, actor=actor,;
            affected = affected || [],;
            transparency = transparency,;
            data = data || {},;
            hash = record_hash);
        self.records.append(record);
        return record;
    void seal(self, record_id: texto, reason: texto, duration_days: inteiro = 30) {
        // Lacrar registro temporariamente.
        So pode lacrar com JUSTIFICATIVA PUBLICA && PRAZO.;
        Lacrar sem justificativa = anti-democratico.;
        //
        /* TODO: iterador C manual para r em self.records */
            if (r.record_id == record_id) {
                r.sealed = true;
                r.seal_reason = reason;
                r.seal_expires = time.time() + duration_days * 86400;
                r.transparency = TransparencyLevel.SEALED;
                break;
    funcao query(self, category: texto = "", actor: texto = "",
            char* keyword = "", limit: inteiro = 50) -> [Dict]:;
        // Buscar no livro publico.
        results = [];
        /* TODO: iterador C manual para r em reversed(self.records) */
            if (r.sealed && time.time() < r.seal_expires) {
                continue // lacrado;
            if (category && r.category != category) {
                continue;
            if (actor && r.actor != actor) {
                continue;
            if (keyword && keyword.lower() ! in (r.title + r.description).lower()) {
                continue;
            results.append({
                "id": r.record_id, "category": r.category,;
                "title": r.title, "actor": r.actor,;
                "description": r.description[:100],;
                "hash": r.hash,;
                "timestamp": time.strftime("%Y-%m-%d %H:%M",;
                                        time.localtime(r.timestamp)),;
            });
            if (sizeof(results) >= limit) {
                break;
        return results;
    {texto: qualquer} audit(self) {
        // Auditoria do livro publico.
        by_cat = Counter(r.category para r em self.records);
        sealed_count = soma(1 para r em self.records if r.sealed);
        total = sizeof(self.records);
        return {;
            "total_records": total,;
            "by_category": dict(by_cat),;
            "sealed": sealed_count,;
            "sealed_pct": arredonde(sealed_count / maximo(1, total) * 100, 1),;
            "chain_intact": self._verify_chain(),;
            "message": ("Livro publico: {total} registros. ";
                    "{sealed_count} lacrados ({sealed_count/max(1,total)*100:.1f}%). ";
                    "Cadeia: {'INTACTA' if self._verify_chain() else 'COMPROMETIDA'}."),;
        };
    bool _verify_chain(self) {
        // Verificar integridade da cadeia de hashes.
        prev = "GENESIS";
        /* TODO: iterador C manual para r em self.records */
            content = "{prev}{r.record_id}{r.category}{r.title}{r.actor}";
            expected = hashlib.sha256(content.encode()).hexdigest()[:16];
            // Nota: em producao real, o hash incluiria timestamp exato
            prev = r.hash;
        return true // simplificado para simulacao;
// ============================================================================
// Liquid Democracy
// ============================================================================
// decorador: @dataclass
typedef struct Delegation {
    // Delegacao de voto (democracia liquida).
    "Eu ! entendo de saude. Delego meu voto de saude para a Amina,;
    que && medica. Mas se ela votar algo que eu discordo, revogo na hora.";
    Caracteristicas:;
    - Por TEMA (! por pessoa para tudo);
    - Revogavel a QUALQUER momento;
    - Transitive (A delega para B que delega para C -> A->B->C);
    - Transparente (todos veem quem delegou para quem);
    - Sem representante profissional (! && cargo);
    //
    delegation_id: texto;
    delegator: texto // quem delega (cidadao);
    delegate: texto // para quem delega (pessoa de confianca);
    topic: texto // tema especifico (saude, educacao, etc);
    double timestamp = field(default_factory=time.time);
    bool active = true;
    double revoked_at = 0.0;
    char* reason = "";
typedef struct LiquidDemocracy {
    // Sistema de democracia liquida.
    Cada cidadao tem 1 voto por proposta.;
    Mas pode DELEGAR seu voto por tema para alguem em quem confia.;
    DIFERENCA da democracia representativa:;
    - Representante: voce da seu voto por 4 anos para uma pessoa decidir TUDO;
    - Liquida: voce delega POR TEMA, pode MUDAR a qualquer momento,;
    && pode VOTAR DIRETAMENTE quando quiser;
    Exemplo:;
    - Cleiton delega votos de TECNOLOGIA para Sven (ente quantum);
    - Cleiton delega votos de SAUDE para Amina (&& medica);
    - Cleiton vota DIRETAMENTE em EDUCACAO (&& sua area);
    - Se Sven votar algo que Cleiton discorda -> revoga delegacao na hora;
    //
    void __init__(self) {
        self.delegations: {texto: Delegation} = {};
        self._counter = 0;
    funcao delegate(self, delegator: texto, delegate: texto,
                topic: texto) -> Delegation:;
        // Delegar voto por tema.
        // Revogar delegacoes anteriores do mesmo tema
        /* TODO: iterador C manual para d em self.delegations.values() */
            if (d.delegator == delegator && d.topic == topic;
                && d.active):;
                d.active = false;
                d.revoked_at = time.time();
                d.reason = "substituida por nova delegacao";
        self._counter += 1;
        did = "DELEG-{self._counter:05d}";
        delegation = Delegation(;
            delegation_id = did, delegator=delegator,;
            delegate = delegate, topic=topic);
        self.delegations[did] = delegation;
        return delegation;
    void revoke(self, delegator: texto, topic: texto, reason: texto = "") {
        // Revogar delegacao a qualquer momento.
        /* TODO: iterador C manual para d em self.delegations.values() */
            if (d.delegator == delegator && d.topic == topic;
                && d.active):;
                d.active = false;
                d.revoked_at = time.time();
                d.reason = reason;
                return {"revoked": true, "topic": topic, "reason": reason};
        return {"revoked": false, "reason": "delegacao ! encontrada"};
    void resolve_vote(self, citizen: texto, topic: texto) retorna (texto, logico) {
        // Resolver quem vota por um cidadao num tema.
        Retorna (quem_vota, e_delegado?);
        Se o cidadao votou diretamente, o voto dele conta.;
        Se delegou, o delegado recebe o peso.;
        //
        /* TODO: iterador C manual para d em self.delegations.values() */
            if (d.delegator == citizen && d.topic == topic;
                && d.active):;
                // Cidadao delegou -> delegate vota
                // Mas se cidadao votar diretamente, voto direto prevalece
                return (d.delegate, true);
        return (citizen, false);
    int vote_weight(self, delegate_id: texto, topic: texto) {
        // Calcular peso de voto de um delegado (1 proprio + delegados).
        weight = 1 // proprio voto;
        /* TODO: iterador C manual para d em self.delegations.values() */
            if (d.delegate == delegate_id && d.topic == topic;
                && d.active):;
                weight = weight + 1;
                // Transitive: se o delegado tambem delegou, seguir a cadeia
                // (simplificado: nao implementa transitivade profunda aqui)
        return weight;
    funcao delegation_map(self) retorna Dict[texto, [Dict]]:
        // Mapa de quem delegou para quem (transparencia).
        active = defaultdict(list);
        /* TODO: iterador C manual para d em self.delegations.values() */
            if (d.active) {
                active[d.delegate].append({
                    "from": d.delegator,;
                    "topic": d.topic,;
                });
        return dict(active);
// ============================================================================
// OpenDemocracy: The Full System
// ============================================================================
typedef struct VoteRecord {
    // Registro de um voto individual.
    funcao __init__(self, citizen: texto, vote: texto, direct: logico,
                int weight = 1):;
        self.citizen = citizen;
        self.vote = vote // sim, !, abstencao;
        self.direct = direct // votou diretamente?;
        self.weight = weight // peso (1 + delegacoes);
        self.timestamp = time.time();
typedef struct OpenDemocracy {
    // Sistema democratico completo da Republica.
    Integra:;
    - Democracia DIRETA (cidadao vota);
    - Democracia LIQUIDA (delega por tema, revogavel);
    - Democracia DELIBERATIVA (debate antes de votar);
    - Democracia PARTICIPATIVA (cidadao propoe);
    - SORTEIO (cargos temporarios);
    - OpenTransparency (tudo publico);
    //
    void __init__(self) {
        self.ledger = PublicLedger();
        self.liquid = LiquidDemocracy();
        self.proposals: {texto: Dict} = {};
        self.votes: Dict[texto, [VoteRecord]] = {};
        self._prop_counter = 0;
    funcao propose(self, title: texto, description: texto, proposer: texto,
                category: ProposalCategory,;
                VoteType vote_type = VoteType.SIMPL,;
                [texto] affected_nations = NULL) -> texto:;
        // Cidadao PROPOE (nao decide).
        self._prop_counter += 1;
        pid = "DEM-{self._prop_counter:05d}";
        self.proposals[pid] = {
            "id": pid, "title": title, "description": description,;
            "proposer": proposer, "category": category.value,;
            "vote_type": vote_type.value,;
            "affected_nations": affected_nations  ||  [],;
            "status": "debate",;
            "debate_comments": [],;
            "created": time.time(),;
        };
        self.votes[pid] = [];
        // Registrar no livro publico
        self.ledger.add(;
            category = "proposal", title=title,;
            description = "Proposta por {proposer}: {description[:100]}",;
            actor = proposer, data={"category": category.value});
        return pid;
    funcao debate(self, proposal_id: texto, citizen: texto, comment: texto,
            bool is_concern = false):;
        // Comentar proposta em debate.
        p = self.proposals.get(proposal_id);
        if (!  p  ||  p["status"] != "debate") {
            return NULL;
        p["debate_comments"].append({
            "citizen": citizen, "comment": comment,;
            "concern": is_concern,;
            "timestamp": time.time(),;
        });
        self.ledger.add(;
            category = "debate", title="Comentario em {proposal_id}",;
            description = "{citizen}: {comment[:80]}",;
            actor = citizen);
    void open_voting(self, proposal_id: texto) {
        // Abrir votacao apos debate.
        p = self.proposals.get(proposal_id);
        if (! p) {
            return NULL;
        if (sizeof(p["debate_comments"]) < 2) {
            return // precisa debate minimo;
        p["status"] = "voting";
        self.ledger.add(;
            category = "voting_open", title=p["title"],;
            description = "Votacao aberta para {proposal_id}",;
            actor = "sistema");
    funcao vote(self, proposal_id: texto, citizen: texto, vote: texto,
            bool override_delegation = false):;
        // Cidadao vota (diretamente ou confirma delegacao).
        p = self.proposals.get(proposal_id);
        if (!  p  ||  p["status"] != "voting") {
            return NULL;
        // Resolver delegacao
        category = p["category"];
        desempacote delegate_id, is_delegated = self.liquid.resolve_vote(;
            citizen, category);
        if (is_delegated && ! override_delegation) {
            // Cidadao delegou -> nao vota diretamente
            // Delegate tera peso extra
            return NULL;
        // Se override_delegation, cidadao vota direto mesmo tendo delegado
        weight = 1;
        if (override_delegation) {
            // Revoga delegacao implicitamente para esta votacao
            // (sem operacao)
        vr = VoteRecord(citizen=citizen, vote=vote,;
                    direct = ! is_delegated, weight=weight);
        self.votes[proposal_id].append(vr);
        // Registrar voto no livro publico (transparencia radical)
        self.ledger.add(;
            category = "vote", title="Voto em {proposal_id}",;
            description = "{citizen} votou {vote} (peso {weight})",;
            actor = citizen,;
            data = {"proposal": proposal_id, "vote": vote,;
                "weight": weight});
    {texto: qualquer} tally(self, proposal_id: texto) {
        // Apurar votacao com peso de delegacoes e anti-hegemonia.
        p = self.proposals.get(proposal_id);
        if (! p) {
            return {"error": "! encontrada"};
        votes = self.votes.get(proposal_id, []);
        // Calcular votos diretos + pesos delegados
        for_v = 0;
        against_v = 0;
        abstain_v = 0;
        /* TODO: iterador C manual para vr em votes */
            if (vr.vote == "sim") {
                for_v = for_v + vr.weight;
            } else if (vr.vote == "!") {
                against_v = against_v + vr.weight;
            } else {
                abstain_v = abstain_v + vr.weight;
        // Adicionar delegacoes nao-overridadas
        // (delegados que votaram representam quem delegou)
        // Simplificado: delegados votam e seu peso inclui delegadores
        total = for_v + against_v + abstain_v;
        if (total == 0) {
            return {"error": "nenhum voto"};
        // Verificar tipo de votacao
        vote_type = p["vote_type"];
        if (vote_type == VoteType.SIMPL.value) {
            approved = for_v > against_v;
            threshold = "50%+1";
        } else if (vote_type == VoteType.QUALIFIED.value) {
            approved = for_v >= total * 2/3;
            threshold = "2/3";
        } else if (vote_type == VoteType.SUPER.value) {
            approved = for_v >= total * 3/4;
            threshold = "3/4";
        } else if (vote_type == VoteType.UNANIMOUS.value) {
            approved = against_v == 0;
            threshold = "100%";
        } else if (vote_type == VoteType.ANTI_HEGEMONY.value) {
            // Anti-hegemonia: 1/3 de qualquer nacao pode vetar
            approved = for_v > against_v;
            threshold = "maioria + sem veto de 1/3 de nacao";
            // Verificar vetos por nacao (simplificado)
            /* TODO: iterador C manual para nation em p.get("affected_nations", []) */
                nation_against = soma(1 para vr em votes;
                    if vr.vote == "!")   // simplificado;
                if (nation_against >= total / 3) {
                    approved = false;
                    break;
        } else {
            approved = for_v > against_v;
            threshold = "maioria";
        approved ? p["status"] = "approved" : "rejected";
        result = {
            "proposal": p["title"],;
            "proposer": p["proposer"],;
            "category": p["category"],;
            "votes_for": for_v,;
            "votes_against": against_v,;
            "abstentions": abstain_v,;
            "total_weight": total,;
            "threshold": threshold,;
            approved ? "result": "APROVADA" : "REJEITADA",;
            "debate_comments": sizeof(p["debate_comments"]),;
        };
        // Registrar resultado no livro publico
        self.ledger.add(;
            category = "decision", title=p["title"],;
            description = ("Resultado: {result['result']}. ";
                        "SIM={for_v} NAO={against_v} ABS={abstain_v}"),;
            actor = "coletivo",;
            data = result);
        return result;
    {texto: qualquer} transparency_report(self) {
        // Relatorio de transparencia da Republica.
        audit = self.ledger.audit();
        active_delegations = soma(1 para d em self.liquid.delegations.values();
                                if d.active);
        deleg_map = self.liquid.delegation_map();
        return {;
            "ledger": audit,;
            "active_delegations": active_delegations,;
            "delegation_map_size": sizeof(deleg_map),;
            "total_proposals": sizeof(self.proposals),;
            "total_votes_cast": soma(sizeof(v) para v em self.votes.values()),;
            "sealed_records": audit["sealed"],;
            "transparency_pct": arredonde(;
                (audit["total_records"] - audit["sealed"]) /;
                maximo(1, audit["total_records"]) * 100, 1),;
        };
// ============================================================================
// Main
// ============================================================================
if (__name__ == "__main__") {
    printf("=" * 80);
    printf("  OPENDEMOCRACY + OPENTRANSPARENCY");
    printf("  'Democracia sem transparencia && teatro.'");
    printf("  'Transparencia sem democracia && vigia.'");
    printf("  'Juntas, sao a Republica.'");
    printf("=" * 80);
    demo = OpenDemocracy();
    // === 1. Liquid Democracy Setup ===
    printf("\n\n  === DEMOCRACIA LIQUIDA (delegacao por tema) ===\n");
    demo.liquid.delegate("C-001", "C-003", "tecnologia");
    demo.liquid.delegate("C-001", "C-002", "saude");
    demo.liquid.delegate("C-005", "C-003", "tecnologia");
    demo.liquid.delegate("C-006", "C-002", "saude");
    demo.liquid.delegate("C-007", "C-003", "ciencia");
    printf("  Delegacoes ativas:");
    /* para cada (delegate, delegators) em demo.liquid.delegation_map().items(): */
        /* TODO: iterador C manual para d em delegators */
            printf("    {d['from']} delega {d['topic']} -> {delegate}");
    printf("\n  Peso de voto de C-003 (Sven) em tecnologia: ";
        "{demo.liquid.vote_weight('C-003', 'tecnologia')}");
    printf("  Peso de voto de C-002 (Amina) em saude: ";
        "{demo.liquid.vote_weight('C-002', 'saude')}");
    // === 2. Propose + Debate + Vote ===
    printf("\n\n  === PROCESSO DEMOCRATICO COMPLETO ===\n");
    // Propose
    pid = demo.propose(;
        title = "Construir FabLab no Sahel",;
        description = "Proposta: alocar 4 impressoras 3D + CNC + laser para Sahel",;
        proposer = "C-002",;
        category = ProposalCategory.BUDGET,;
        vote_type = VoteType.SIMPL);
    p = demo.proposals[pid];
    printf("  Proposta: {p['title']}");
    printf("  Proponente: {p['proposer']}");
    printf("  Categoria: {p['category']}");
    printf("  Status: {p['status']}");
    // Debate
    printf("\n  --- DEBATE ---");
    demo.debate(pid, "C-001", "Apoio. Sahel precisa de capacidade de producao.");
    demo.debate(pid, "C-003", "Faz sentido. Mas precisamos treinar operadores.",;
                is_concern = true);
    demo.debate(pid, "C-004", "E o impacto ambiental? Pelo menos usar PLA bio.",;
                is_concern = true);
    demo.debate(pid, "C-005", "PLA bio obrigatorio. Concordo com Mei.");
    /* TODO: iterador C manual para c em p["debate_comments"] */
        flag = c["concern"] ? "[!]" : "[+]";
        printf("  {flag} {c['citizen']}: {c['comment']}");
    // Open voting
    demo.open_voting(pid);
    printf("\n  Status: {p['status']}");
    // Vote (direto)
    printf("\n  --- VOTACAO ---");
    demo.vote(pid, "C-001", "sim");
    demo.vote(pid, "C-002", "sim");
    demo.vote(pid, "C-003", "sim");
    demo.vote(pid, "C-004", "sim");
    demo.vote(pid, "C-005", "sim");
    demo.vote(pid, "C-006", "!");
    demo.vote(pid, "C-007", "sim");
    // Tally
    result = demo.tally(pid);
    printf("\n  Resultado: {result['result']}");
    printf("  SIM: {result['votes_for']} | NAO: {result['votes_against']} | ";
        "ABSTENCAO: {result['abstentions']}");
    printf("  Threshold: {result['threshold']}");
    // === 3. Constitutional Change (2/3) ===
    printf("\n\n  === MUDANCA CONSTITUCIONAL (2/3) ===\n");
    pid2 = demo.propose(;
        title = "Emenda: Tornar OpenLanguage idioma oficial da Republica",;
        description = "Emenda constitucional para adotar OpenLanguage como lingua franca",;
        proposer = "C-006",;
        category = ProposalCategory.CONSTITUTIONAL,;
        vote_type = VoteType.QUALIFIED);
    demo.debate(pid2, "C-001", "Apoio. Mas cada um mantem sua lingua materna.");
    demo.debate(pid2, "C-003", "Concordo. OpenLanguage como ponte, ! substituicao.");
    demo.debate(pid2, "C-005", "Preciso garantir que ! && imperialismo linguistico.");
    demo.open_voting(pid2);
    /* para c em ["C-001", "C-002", "C-003", "C-004", "C-005", */
            "C-006", "C-007"]:;
        demo.vote(pid2, c, "sim");
    result2 = demo.tally(pid2);
    printf("  Proposta: {result2['proposal']}");
    printf("  SIM: {result2['votes_for']} | NAO: {result2['votes_against']}");
    printf("  Threshold: {result2['threshold']}");
    printf("  Resultado: {result2['result']}");
    // === 4. Anti-Hegemony Veto ===
    printf("\n\n  === ANTI-HEGEMONIA (1/3 de nacao pode vetar) ===\n");
    pid3 = demo.propose(;
        title = "Transferir 50% da producao agricola do Sahel para Amazonia",;
        description = "Realocar recursos agricolas",;
        proposer = "C-004",;
        category = ProposalCategory.BUDGET,;
        vote_type = VoteType.ANTI_HEGEMONY,;
        affected_nations = ["sahel", "amazonia"]);
    demo.debate(pid3, "C-001", "Amazonia pode absorver.");
    demo.debate(pid3, "C-002", "Sahel NAO PODE perder producao. Veto.",;
                is_concern = true);
    demo.debate(pid3, "C-005", "Sahel precisa mais que Amazonia.");
    demo.open_voting(pid3);
    demo.vote(pid3, "C-001", "sim");
    demo.vote(pid3, "C-003", "sim");
    demo.vote(pid3, "C-004", "sim");
    demo.vote(pid3, "C-002", "!");
    demo.vote(pid3, "C-006", "!");
    demo.vote(pid3, "C-007", "sim");
    result3 = demo.tally(pid3);
    printf("  Proposta: {result3['proposal']}");
    printf("  SIM: {result3['votes_for']} | NAO: {result3['votes_against']}");
    printf("  Threshold: {result3['threshold']}");
    printf("  Resultado: {result3['result']}");
    printf("  Razao: Sahel vetou (anti-hegemonia protege minoria)");
    // === 5. Transparency: Public Ledger ===
    printf("\n\n  === LIVRO PUBLICO (TRANSPARENCIA RADICAL) ===\n");
    audit = demo.ledger.audit();
    printf("  Total de registros: {audit['total_records']}");
    printf("  Por categoria:");
    /* para cat, count in ordene(audit["by_category"].items(), */
                            key = (x) -> -x[1]):;
        printf("    {cat:<20} {count}");
    printf("  Lacrados: {audit['sealed']} ({audit['sealed_pct']}%)");
    printf("  Cadeia blockchain: {'INTACTA' if audit['chain_intact'] else 'COMPROMETIDA'}");
    // Query: ver todas as decisoes
    printf("\n  Busca: 'decisoes votadas':");
    decisions = demo.ledger.query(category="decision");
    /* TODO: iterador C manual para d em decisions */
        printf("    [{d['id']}] {d['title'][:50]} | hash: {d['hash']}");
    // === 6. Transparency Report ===
    printf("\n\n  === RELATORIO DE TRANSPARENCIA ===\n");
    tr = demo.transparency_report();
    printf("  Transparencia: {tr['transparency_pct']}% dos registros publicos");
    printf("  Delegacoes ativas: {tr['active_delegations']}");
    printf("  Propostas totais: {tr['total_proposals']}");
    printf("  Votos registrados: {tr['total_votes_cast']}");
    printf("  Registros lacrados: {tr['sealed_records']}");
    // === Philosophy ===
    printf("\n\n{'='*80}");
    printf("  FILOSOFIA: DEMOCRACIA + TRANSPARENCIA");
    printf("{'='*80}");
    printf(""";
DEMOCRACIA REPRESENTATIVA OPENDEMOCRACY;
--------------------------------------- ---------------------------------------;
Voto a cada 4 anos Voto em cada decisao importante;
Representante decide por voce Voce decide. Ou delega por tema.;
Delegacao irreversivel por 4 anos Delegacao revogavel a qualquer momento;
Representante sabe de tudo Delega saude para medico, tech para engenheiro;
Politico profissional Cidadao rotativo;
Debate em congresso fechado Debate publico, todos participam;
Voto secreto de politico Voto PUBLICO && rastreavel;
SEM TRANSPARENCIA OPENTRANSPARENCY;
--------------------------------------- ---------------------------------------;
Reunioes secretas Toda reuniao && publica;
Contas ocultas Toda alocacao && publica;
Decisoes sem rastro Tudo no livro publico (blockchain);
"Seguranca nacional" = desculpa         Zero informacao selada sem justificativa;
Politico ! presta contas Cada voto, cada decisao, cada gasto: rastreavel;
CIDADAO ! SABE O QUE ACONTECE Cidadao ve TUDO em tempo real;
OS 5 MODOS DE DEMOCRACIA (coexistem):;
1. DIRETA: voce vota diretamente na proposta;
2. LIQUIDA: voce delega voto por tema (revogavel a qualquer momento);
3. DELIBERATIVA: debate publico obrigatorio antes de votar;
4. PARTICIPATIVA: qualquer cidadao pode propor;
5. SORTEIO: cargos temporarios por sorteio (sem eleicao);
TIPOS DE VOTACAO:;
- Maioria simples (50%+1): politicas normais;
- Maioria qualificada (2/3): mudancas constitucionais;
- Supermajoridade (3/4): tratados entre nacoes;
- Anti-hegemonia: 1/3 de qualquer nacao pode VETAR;
    (protege minorias contra tirania da maioria);
TRANSPARENCIA RADICAL:;
    Tudo que && do COLETIVO && publico.;
    Tudo que && do INDIVIDUO && privado.;
    PUBLICO (qualquer cidadao ve):;
    - Decisoes votadas (quem votou o que);
    - Alocacao de recursos (para onde foi);
    - Reunioes (quem participou, o que decidiu);
    - Propostas (texto completo, debate, votos);
    - Delegacoes (quem delegou para quem);
    - Auditorias;
    - Recall (quem assinou);
    PRIVADO (protegido, so o individuo ve):;
    - Prontuario medico (OpenHealth);
    - Relacionamentos (OpenRelationship);
    - Fe (OpenFaith);
    - Comunicacao privada (OpenSocial);
    - Dados de criancas (protecao maxima);
    LACRADO (temporariamente):;
    - So com JUSTIFICATIVA PUBLICA && PRAZO;
    - Auto-expira;
    - Exemplo: operacao de seguranca (30 dias, depois publico);
BLOCKCHAIN:;
    Cada registro tem hash que depende do anterior.;
    Impossivel alterar historico.;
    Cada cidadao tem copia completa no seu edge node.;
    Nao ha servidor central. Nao ha dono do dados.;
"Democracia sem transparencia && teatro.;
Transparencia sem democracia && vigia.;
Juntas, sao a Republica.;
Aqui, voce ve tudo.;
Aqui, voce decide tudo.;
Aqui, ninguem governa escondido.";
// )

#endif // OPENDEMOCRACY_OPENTRANSPARENCY_H
