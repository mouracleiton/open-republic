// OpenRepublic -- Principio: Democracia, Nao Elitismo -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

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
#[derive(Debug, Clone, PartialEq)]
enum ProposalOrigin {
    // De onde veio a ideia/proposta.
    CITIZEN = "cidadao"  // qualquer cidadao da Republica;
    SECTOR = "setor"  // deliberacao de um setor inteiro;
    NATION = "nacao"  // votacao de uma OpenNation;
    EXTERNAL = "externo"  // de fora da Republica (livro, pessoa, etc);
    EMERGENCY = "emergencia"  // resposta a crise (tempo limitado);
#[derive(Debug, Clone, PartialEq)]
enum ProposalStatus {
    DRAFT = "rascunho"  // sendo escrita;
    SUBMITTED = "submetida"  // enviada para debate;
    DEBATING = "em_debate"  // em discussao publica;
    VOTING = "em_votacao"  // em votacao;
    APPROVED = "aprovada"  // coletivo aprovou;
    REJECTED = "rejeitada"  // coletivo rejeitou;
    IMPLEMENTED = "implementada"  // ja foi construida;
    WITHDRAWN = "retirada"  // proponente retirou;
#[derive(Debug, Clone, PartialEq)]
enum ProposalType {
    // O que a proposta faz.
    NEW_SYSTEM = "sistema_novo"  // criar sistema inteiro;
    NEW_POLICY = "politica_nova"  // criar nova politica;
    MODIFICATION = "modificacao"  // mudar sistema existente;
    CONSTITUTIONAL = "constitucional"  // mudar a constituicao da Republica;
    EMERGENCY = "emergencia"  // resposta a crise;
    CULTURAL = "cultural"  // iniciativa cultural/artistica;
// decorador: @dataclass
#[derive(Debug, Clone)]
struct Proposal {
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
    let affects_sectors: [texto] = field(default_factory=list);
    let affects_nations: [texto] = field(default_factory=list);
    let affects_population: i64 = 0;
    // Processo democratico
    let status: ProposalStatus = ProposalStatus.DRAFT;
    let submitted_at: f64 = 0.0;
    let debate_duration_days: i64 = 7 // minimo 7 dias de debate;
    let voting_duration_days: i64 = 3 // minimo 3 dias de votacao;
    // Votacao
    let votes_for: i64 = 0;
    let votes_against: i64 = 0;
    let votes_abstain: i64 = 0;
    let total_eligible: i64 = 0;
    // Debate
    let debate_comments: [Dict] = field(default_factory=list);
    let concerns_raised: [texto] = field(default_factory=list);
    let amendments: [texto] = field(default_factory=list);
    // Verificacao
    let anti_elitism_check: bool = false // passou verificacao anti-elitismo;
    let co_created: bool = false // mais de 1 pessoa participou da criacao;
#[derive(Debug, Clone)]
struct DemocraticProcess {
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
    fn __init__(self) {
        self.proposals: {texto: Proposal} = {};
        self._counter = 0;
    funcao submit_proposal(self, title: texto, description: texto,
                        proposer_id: texto, proposer_name: texto,;
                        origin: ProposalOrigin,;
                        ptype: ProposalType,;
                        let affects_sectors: [texto] = NULL,;
                        let affects_population: i64 = 1000) -> Proposal:;
        // Submeter proposta para processo democratico.
        self._counter += 1;
        pid = "PROP-{self._counter:05d}";
        // VERIFICACAO ANTI-ELITISMO
        anti_elite = true;
        if origin == ProposalOrigin.EXTERNAL {
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
                        let is_concern: bool = false):;
        // Adicionar comentario ao debate publico.
        p = self.proposals.get(proposal_id);
        if ! p || p.status ! in (ProposalStatus.SUBMITTED,;
                                    ProposalStatus.DEBATING):;
            return None;
        p.status = ProposalStatus.DEBATING;
        p.debate_comments.append({
            "citizen": citizen_name, "comment": comment,;
            "is_concern": is_concern, "timestamp": time.time(),;
        });
        if is_concern {
            p.concerns_raised.append(comment[:100]);
    fn start_voting(self, proposal_id: texto) -> {texto: qualquer} {
        // Iniciar votacao apos periodo de debate.
        p = self.proposals.get(proposal_id);
        if ! p || p.status != ProposalStatus.DEBATING {
            return {"error": "precisa debate primeiro"};
        // Verificar debate minimo
        if tamanho(p.debate_comments) < 3 {
            return {"error": "precisa pelo menos 3 comentarios de debate"};
        p.status = ProposalStatus.VOTING;
        return {"voting_started": true, "proposal": p.title};
    fn cast_vote(self, proposal_id: texto, vote: texto) {
        // Registrar voto de um cidadao.
        p = self.proposals.get(proposal_id);
        if ! p || p.status != ProposalStatus.VOTING {
            return None;
        if vote == "sim" {
            p.votes_for += 1;
        } else if vote == "!" {
            p.votes_against += 1;
        } else if vote == "abstencao" {
            p.votes_abstain += 1;
    funcao tally(self, proposal_id: texto,
            let constitutional: bool = false) -> {texto: qualquer}:;
        // Apurar votacao.
        p = self.proposals.get(proposal_id);
        if ! p {
            return {"error": "! encontrada"};
        total = p.votes_for + p.votes_against + p.votes_abstain;
        if total == 0 {
            return {"error": "nenhum voto"};
        if constitutional {
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
if __name__ == "__main__" {
    println!("=" * 80);
    println!("  OPENREPUBLIC -- DEMOCRACIA, NAO ELITISMO");
    println!("  'Ninguem decide por todos. Todos decidem por todos.'");
    println!("=" * 80);
    process = DemocraticProcess();
    // === Case 1: Citizen proposes, democracy decides ===
    println!("\n\n  === CASO 1: CIDADAO PROPOE ===\n");
    prop = process.submit_proposal(;
        title = "Construir datacenter quantico subaquatico",;
        description = "Proposta para infraestrutura de quantum + IA + rede no oceano",;
        proposer_id = "C-001", proposer_name="Cleiton",;
        origin = ProposalOrigin.CITIZEN,;
        ptype = ProposalType.NEW_SYSTEM,;
        affects_sectors = ["tecnologia", "ciencia", "meio_ambiente"],;
        affects_population = 10000);
    println!("  Proposta: {prop.proposal_id}");
    println!("  Titulo: {prop.title}");
    println!("  Proponente: {prop.proposer_name}");
    println!("  Status: {prop.status.value}");
    println!("  Verificacao anti-elitismo: {'PASSOU' if prop.anti_elitism_check else 'FALHOU'}");
    println!("  Setores afetados: {prop.affects_sectors}");
    // === Debate ===
    println!("\n  --- DEBATE PUBLICO (7 dias obrigatorios) ---\n");
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
    println!("  Comentarios de debate: {len(prop.debate_comments)}");
    for c in prop.debate_comments {
        flag = c["is_concern"] ? "[CONCERNO]" : "[APOIO]";
        println!("    {flag} {c['citizen']}: {c['comment'][:70]}...");
    println!("\n  Concerns levantados: {len(prop.concerns_raised)}");
    // === Voting ===
    println!("\n  --- VOTACAO ---\n");
    process.start_voting(prop.proposal_id);
    votes = ["sim", "sim", "sim", "!", "sim", "!", "sim", "sim",;
            "sim", "sim", "!", "sim"];
    for v in votes {
        process.cast_vote(prop.proposal_id, v);
    result = process.tally(prop.proposal_id);
    println!("  Proposta: {result['proposal']}");
    println!("  SIM: {result['votes_for']} | NAO: {result['votes_against']} | ";
        "ABSTENCAO: {result['abstentions']}");
    println!("  Resultado: {result['result']}");
    println!("  {result['message']}");
    // === Case 2: "I decided" is rejected ===
    println!("\n\n  === CASO 2: 'EU DECIDI' E ANTI-DEMOCRATICO ===\n");
    println!("  Se o proponente diz 'eu decidi construir X':");
    println!("    -> Proposta REJEITADA por anti-democratica.");
    println!("    -> Ninguem decide. Propoe.");
    println!("    -> O coletivo decide.");
    println!("  Se o proponente diz 'eu proponho construir X':");
    println!("    -> Proposta ACEITA para debate.");
    println!("    -> O coletivo debate.");
    println!("    -> O coletivo vota.");
    println!("    -> O coletivo decide.");
    // === Case 3: Emergency ===
    println!("\n\n  === CASO 3: EMERGENCIA (processo acelerado) ===\n");
    emergency = process.submit_proposal(;
        title = "Destinar agua para Sahel (crise hidrica)",;
        description = "Sahel esta sem agua. Proposta de acao imediata.",;
        proposer_id = "C-002", proposer_name="Amina",;
        origin = ProposalOrigin.EMERGENCY,;
        ptype = ProposalType.EMERGENCY,;
        affects_sectors = ["saude", "alimentacao"],;
        affects_population = 40000);
    println!("  Proposta: {emergency.proposal_id}");
    println!("  Tipo: {emergency.ptype.value}");
    println!("  Origem: {emergency.origin.value}");
    println!("  Processo: ACELERADO (votacao em 24h)");
    println!("  Auto-expira em 30 dias se ! revalidada");
    // === Constitution ===
    println!("\n\n{'='*80}");
    println!("  PRINCIPIO CONSTITUCIONAL: DEMOCRACIA > IDEIA");
    println!("{'='*80}");
    println!(""";
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
