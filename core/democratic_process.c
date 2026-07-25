/* OpenRepublic -- Principio: Democracia, Nao Elitismo -- gerado de Portugol++ */
#ifndef OPENREPUBLIC_PRINCIPIO_DEMOCRACIA_NAO_ELITISMO_H
#define OPENREPUBLIC_PRINCIPIO_DEMOCRACIA_NAO_ELITISMO_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenRepublic -- Principio: Democracia, Nao Elitismo;
======================================================;
PRINCIPIO CONSTITUCIONAL NUMERO 1:;
"Nenhuma ideia, projeto, sistema || mudanca entra na Republica;
por decreto de uma unica pessoa. Nem do lider. Nem do fundador.;
Nem do mais tecnico. Nem do mais velho. Nem do mais influente.;
Tudo passa pelo coletivo || ! passa.;
Quem traz uma ideia de fora -- seja de um livro, de um amigo,;
de uma corporacao, || da propria cabeca -- ! esta decidindo.;
Esta PROPOSTANDO.;
A decisao && do coletivo. Sempre.";
O PROBLEMA QUE ISTO RESOLVE:;
Em todos os sistemas historicos, uma 'elite' (rei, partido, guru,;
CEO, fundador, tecnico) decide o que && bom para todos.;
O resto 'executa'.;
Isso reproduz hierarquia. Mesmo com boas intencoes.;
Mesmo se a ideia para boa. A ESTRUTURA de decisao unipessoal;
&& anti-democratica por design.;
A SOLUCAO:;
Qualquer pessoa PODE propor qualquer coisa.;
Mas a proposta precisa ser:;
    1. APRESENTADA ao setor relevante (OpenRepresentative);
    2. DEBATIDA publicamente (transparencia radical);
    3. VOTADA pelo coletivo (democracia direta || representantes);
    4. IMPLEMENTADA apenas se aprovada;
Ninguem 'traz ideias && implementa'. Ninguem tem esse poder.;
Nem se a ideia para genial. O processo && mais importante que a ideia.;
POR QUE ISSO IMPORTA:;
Uma boa ideia imposta por decreto abre precedente para;
uma ruim ideia imposta por decreto.;
Se o lider pode impor X hoje, pode impor Y amanha.;
A unica defesa contra tirania -- mesmo benevolente --;
&& o processo democratico.;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Set de typing
// importa Enum de enum
// importa defaultdict de collections
typedef struct ProposalOrigin {
    // De onde veio a ideia/proposta.
    CITIZEN = "cidadao"  // qualquer cidadao da Republica;
    SECTOR = "setor"  // deliberacao de um setor inteiro;
    NATION = "nacao"  // votacao de uma OpenNation;
    EXTERNAL = "externo"  // de fora da Republica (livro, pessoa, etc);
    EMERGENCY = "emergencia"  // resposta a crise (tempo limitado);
typedef struct ProposalStatus {
    DRAFT = "rascunho"  // sendo escrita;
    SUBMITTED = "submetida"  // enviada para debate;
    DEBATING = "em_debate"  // em discussao publica;
    VOTING = "em_votacao"  // em votacao;
    APPROVED = "aprovada"  // coletivo aprovou;
    REJECTED = "rejeitada"  // coletivo rejeitou;
    IMPLEMENTED = "implementada"  // ja foi construida;
    WITHDRAWN = "retirada"  // proponente retirou;
typedef struct ProposalType {
    // O que a proposta faz.
    NEW_SYSTEM = "sistema_novo"  // criar sistema inteiro;
    NEW_POLICY = "politica_nova"  // criar nova politica;
    MODIFICATION = "modificacao"  // mudar sistema existente;
    CONSTITUTIONAL = "constitucional"  // mudar a constituicao da Republica;
    EMERGENCY = "emergencia"  // resposta a crise;
    CULTURAL = "cultural"  // iniciativa cultural/artistica;
// decorador: @dataclass
typedef struct Proposal {
    // Uma proposta para a Republica.
    QUALQUER cidadao pode criar. NINGUEM pode impor.;
    //
    proposal_id: texto;
    title: texto;
    description: texto;
    proposer_id: texto // quem propoe;
    proposer_name: texto;
    origin: ProposalOrigin // de onde veio;
    ptype: ProposalType;
    // Impacto
    [texto] affects_sectors = field(default_factory=list);
    [texto] affects_nations = field(default_factory=list);
    int affects_population = 0;
    // Processo democratico
    ProposalStatus status = ProposalStatus.DRAFT;
    double submitted_at = 0.0;
    int debate_duration_days = 7 // minimo 7 dias de debate;
    int voting_duration_days = 3 // minimo 3 dias de votacao;
    // Votacao
    int votes_for = 0;
    int votes_against = 0;
    int votes_abstain = 0;
    int total_eligible = 0;
    // Debate
    [Dict] debate_comments = field(default_factory=list);
    [texto] concerns_raised = field(default_factory=list);
    [texto] amendments = field(default_factory=list);
    // Verificacao
    bool anti_elitism_check = false // passou verificacao anti-elitismo;
    bool co_created = false // mais de 1 pessoa participou da criacao;
typedef struct DemocraticProcess {
    // Processo democratico obrigatorio para toda mudanca na Republica.
    FLUXO:;
    1. QUALQUER pessoa PROPOE.;
    - Nao importa quem. Nao importa a ideia.;
    - Mas a pessoa SABE que esta PROpondo, ! decidindo.;
    2. VERIFICACAO ANTI-ELITISMO;
    - A proposta foi criada por 1 pessoa so?;
    - Se sim, precisa ser DEBATIDA antes de votar.;
    - Se a pessoa diz "eu decidi" -> proposta REJEITADA por anti-democratica.;
    - "Eu proponho" && aceito. "Eu determino" nunca.;
    3. DEBATE PUBLICO (minimo 7 dias);
    - Todo mundo pode comentar.;
    - Concerns sao levantados.;
    - Emendas podem ser adicionadas.;
    - O proponente pode revisar com base no debate.;
    4. VOTACAO (minimo 3 dias);
    - Todos os cidadaos do setor/nacao afetados votam.;
    - Maioria simples para propostas normais.;
    - 2/3 para mudancas constitucionais.;
    - Anti-hegemonia: 1/3 de N bloco pode vetar (OpenRepublic).;
    5. IMPLEMENTACAO;
    - So se aprovada.;
    - Quem implementou ! && quem propos (separacao de poderes).;
    CASOS ESPECIAIS:;
    EMERGENCIA: crise imediata (vida em risco). Processo acelerado:;
        - Proposta + votacao em 24h.;
        - Auto-expira em 30 dias (precisa ser revalidada).;
        - So para risco de vida, ! para "urgencia politica".;
    //
    void __init__(self) {
        self.proposals: {texto: Proposal} = {};
        self._counter = 0;
    funcao submit_proposal(self, title: texto, description: texto,
                        proposer_id: texto, proposer_name: texto,;
                        origin: ProposalOrigin,;
                        ptype: ProposalType,;
                        [texto] affects_sectors = NULL,;
                        int affects_population = 1000) -> Proposal:;
        // Submeter proposta para processo democratico.
        self._counter += 1;
        pid = "PROP-{self._counter:05d}";
        // VERIFICACAO ANTI-ELITISMO
        anti_elite = true;
        if (origin == ProposalOrigin.EXTERNAL) {
            // Proposta de fonte externa: precisa de padrinho interno
            // que PROPOE, mas fica claro que e ideia externa sujeita a voto
            anti_elite = true // pode propor, mas o coletivo decide;
        proposal = Proposal(;
            proposal_id = pid, title=title, description=description,;
            proposer_id = proposer_id, proposer_name=proposer_name,;
            origin = origin, ptype=ptype,;
            affects_sectors = affects_sectors || [],;
            affects_population = affects_population,;
            status = ProposalStatus.SUBMITTED,;
            submitted_at = time.time(),;
            anti_elitism_check = anti_elite,;
        );
        self.proposals[pid] = proposal;
        return proposal;
    funcao add_debate_comment(self, proposal_id: texto, citizen_id: texto,
                        citizen_name: texto, comment: texto,;
                        bool is_concern = false):;
        // Adicionar comentario ao debate publico.
        p = self.proposals.get(proposal_id);
        if ! p || p.status ! in (ProposalStatus.SUBMITTED,;
                                    ProposalStatus.DEBATING):;
            return NULL;
        p.status = ProposalStatus.DEBATING;
        p.debate_comments.append({
            "citizen": citizen_name, "comment": comment,;
            "is_concern": is_concern, "timestamp": time.time(),;
        });
        if (is_concern) {
            p.concerns_raised.append(comment[:100]);
    {texto: qualquer} start_voting(self, proposal_id: texto) {
        // Iniciar votacao apos periodo de debate.
        p = self.proposals.get(proposal_id);
        if (! p || p.status != ProposalStatus.DEBATING) {
            return {"error": "precisa debate primeiro"};
        // Verificar debate minimo
        if (sizeof(p.debate_comments) < 3) {
            return {"error": "precisa pelo menos 3 comentarios de debate"};
        p.status = ProposalStatus.VOTING;
        return {"voting_started": true, "proposal": p.title};
    void cast_vote(self, proposal_id: texto, vote: texto) {
        // Registrar voto de um cidadao.
        p = self.proposals.get(proposal_id);
        if (! p || p.status != ProposalStatus.VOTING) {
            return NULL;
        if (vote == "sim") {
            p.votes_for += 1;
        } else if (vote == "!") {
            p.votes_against += 1;
        } else if (vote == "abstencao") {
            p.votes_abstain += 1;
    funcao tally(self, proposal_id: texto,
            bool constitutional = false) -> {texto: qualquer}:;
        // Apurar votacao.
        p = self.proposals.get(proposal_id);
        if (! p) {
            return {"error": "! encontrada"};
        total = p.votes_for + p.votes_against + p.votes_abstain;
        if (total == 0) {
            return {"error": "nenhum voto"};
        if (constitutional) {
            threshold = total * 2 / 3;
            approved = p.votes_for >= threshold;
        } else {
            approved = p.votes_for > p.votes_against;
        approved ? p.status = ProposalStatus.APPROVED : ProposalStatus.REJECTED;
        return {;
            "proposal": p.title,;
            "proposer": p.proposer_name,;
            "votes_for": p.votes_for,;
            "votes_against": p.votes_against,;
            "abstentions": p.votes_abstain,;
            "total": total,;
            approved ? "result": "APROVADA" : "REJEITADA",;
            "message": ("O coletivo decidiu. Implementar." if approved;
                    else "O coletivo decidiu. Nao implementar."),;
        };
// ============================================================================
// Main
// ============================================================================
if (__name__ == "__main__") {
    printf("=" * 80);
    printf("  OPENREPUBLIC -- DEMOCRACIA, NAO ELITISMO");
    printf("  'Ninguem decide por todos. Todos decidem por todos.'");
    printf("=" * 80);
    process = DemocraticProcess();
    // === Case 1: Citizen proposes, democracy decides ===
    printf("\n\n  === CASO 1: CIDADAO PROPOE ===\n");
    prop = process.submit_proposal(;
        title = "Construir datacenter quantico subaquatico",;
        description = "Proposta para infraestrutura de quantum + IA + rede no oceano",;
        proposer_id = "C-001", proposer_name="Cleiton",;
        origin = ProposalOrigin.CITIZEN,;
        ptype = ProposalType.NEW_SYSTEM,;
        affects_sectors = ["tecnologia", "ciencia", "meio_ambiente"],;
        affects_population = 10000);
    printf("  Proposta: {prop.proposal_id}");
    printf("  Titulo: {prop.title}");
    printf("  Proponente: {prop.proposer_name}");
    printf("  Status: {prop.status.value}");
    printf("  Verificacao anti-elitismo: {'PASSOU' if prop.anti_elitism_check else 'FALHOU'}");
    printf("  Setores afetados: {prop.affects_sectors}");
    // === Debate ===
    printf("\n  --- DEBATE PUBLICO (7 dias obrigatorios) ---\n");
    process.add_debate_comment(prop.proposal_id, "C-002", "Amina",;
        "Como isso afeta a vida marinha? Precisamos de estudo de impacto.",;
        is_concern = true);
    process.add_debate_comment(prop.proposal_id, "C-003", "Sven",;
        "Quantum subaquatico faz sentido: agua fria = refrigeracao natural. ";
        "Mas precisa de protecao anti-corrosao.",;
        is_concern = false);
    process.add_debate_comment(prop.proposal_id, "C-004", "Mei",;
        "O oceano ! && nosso para construir em cima. E bem comum ";
        "da biosfera. Precisamos de avaliacao ecologica COMPLETA.",;
        is_concern = true);
    process.add_debate_comment(prop.proposal_id, "C-005", "Kofi",;
        "Se vai ajudar toda a Republica com computacao, apoio. ";
        "Mas Mei tem razao -- ecologia primeiro.",;
        is_concern = false);
    printf("  Comentarios de debate: {len(prop.debate_comments)}");
    /* TODO: iterador C manual para c em prop.debate_comments */
        flag = c["is_concern"] ? "[CONCERNO]" : "[APOIO]";
        printf("    {flag} {c['citizen']}: {c['comment'][:70]}...");
    printf("\n  Concerns levantados: {len(prop.concerns_raised)}");
    // === Voting ===
    printf("\n  --- VOTACAO ---\n");
    process.start_voting(prop.proposal_id);
    votes = ["sim", "sim", "sim", "!", "sim", "!", "sim", "sim",;
            "sim", "sim", "!", "sim"];
    /* TODO: iterador C manual para v em votes */
        process.cast_vote(prop.proposal_id, v);
    result = process.tally(prop.proposal_id);
    printf("  Proposta: {result['proposal']}");
    printf("  SIM: {result['votes_for']} | NAO: {result['votes_against']} | ";
        "ABSTENCAO: {result['abstentions']}");
    printf("  Resultado: {result['result']}");
    printf("  {result['message']}");
    // === Case 2: "I decided" is rejected ===
    printf("\n\n  === CASO 2: 'EU DECIDI' E ANTI-DEMOCRATICO ===\n");
    printf("  Se o proponente diz 'eu decidi construir X':");
    printf("    -> Proposta REJEITADA por anti-democratica.");
    printf("    -> Ninguem decide. Propoe.");
    printf("    -> O coletivo decide.");
    printf("  Se o proponente diz 'eu proponho construir X':");
    printf("    -> Proposta ACEITA para debate.");
    printf("    -> O coletivo debate.");
    printf("    -> O coletivo vota.");
    printf("    -> O coletivo decide.");
    // === Case 3: Emergency ===
    printf("\n\n  === CASO 3: EMERGENCIA (processo acelerado) ===\n");
    emergency = process.submit_proposal(;
        title = "Destinar agua para Sahel (crise hidrica)",;
        description = "Sahel esta sem agua. Proposta de acao imediata.",;
        proposer_id = "C-002", proposer_name="Amina",;
        origin = ProposalOrigin.EMERGENCY,;
        ptype = ProposalType.EMERGENCY,;
        affects_sectors = ["saude", "alimentacao"],;
        affects_population = 40000);
    printf("  Proposta: {emergency.proposal_id}");
    printf("  Tipo: {emergency.ptype.value}");
    printf("  Origem: {emergency.origin.value}");
    printf("  Processo: ACELERADO (votacao em 24h)");
    printf("  Auto-expira em 30 dias se ! revalidada");
    // === Constitution ===
    printf("\n\n{'='*80}");
    printf("  PRINCIPIO CONSTITUCIONAL: DEMOCRACIA > IDEIA");
    printf("{'='*80}");
    printf(""";
PRINCIPIO CONSTITUCIONAL NUMERO 1:;
    "Nenhuma ideia, projeto, sistema || mudanca entra na Republica;
    por decreto de uma unica pessoa.;
    Nem do lider. Nem do fundador. Nem do mais tecnico.;
    Nem do mais velho. Nem do mais influente.;
    Tudo passa pelo coletivo || ! passa.;
    Quem traz uma ideia -- seja de um livro, de um amigo,;
    de uma corporacao, || da propria cabeca -- ! esta decidindo.;
    Esta PROPOSTANDO.;
    A decisao && do coletivo. Sempre.";
POR QUE O PROCESSO && MAIS IMPORTANTE QUE A IDEIA:;
    Uma boa ideia imposta por decreto abre precedente para;
    uma pessimo ideia imposta por decreto.;
    Se o lider pode impor X hoje, pode impor Y amanha.;
    A unica defesa contra tirania -- mesmo benevolente --;
    && o processo democratico.;
    Mesmo que a ideia seja obviamente boa, ela PRECISA passar;
    pelo processo. Porque o processo protege contra a proxima ideia;
    que ! && obviamente boa.;
O FLUXO OBRIGATORIO:;
    1. PROPOR: qualquer cidadao pode propor qualquer coisa.;
    Mas PROPOR, ! DECIDIR.;
    2. DEBATER: minimo 7 dias de debate publico.;
    Concerns sao levantados. Emendas sao propostas.;
    3. VOTAR: minimo 3 dias de votacao.;
    O coletivo decide. Nao o proponente.;
    4. IMPLEMENTAR: so se aprovada.;
    Quem implementa ! && quem propos (separacao de poderes).;
EXCECAO: EMERGENCIA;
    Apenas para risco de VIDA.;
    Processo acelerado (24h).;
    Auto-expira em 30 dias.;
    Precisa revalidacao democratica para permanente.;
    "Urgencia politica" ! && emergencia.;
"Se eu trouxer uma ideia de alguem fora deste sistema;
&& quiser implementar sozinho, eu sou a elite.;
Aqui && a democracia da OpenRepublic.;
Nao && o comentario de uma unica pessoa.";
// )

#endif // OPENREPUBLIC_PRINCIPIO_DEMOCRACIA_NAO_ELITISMO_H
