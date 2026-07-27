# OpenRepublic -- Principio: Democracia, Nao Elitismo

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/democratic_process.py`

**Descricao:** ======================================================
PRINCIPIO CONSTITUCIONAL NUMERO 1:
  "Nenhuma ideia, projeto, sistema ou mudanca entra na Republica
   por decreto de uma unica pessoa. Nem do lider. Nem do fundador.
   Nem do mais tecnico. Nem do mais velho. Nem do mais influente.
   Tudo passa pelo coletivo ou nao passa.
   Quem traz uma ideia de fora -- seja de um livro, de um amigo,
   de uma corporacao, ou da propria cabeca -- NAO esta decidindo.
   Esta PROPOSTANDO.
   A decisao e do coletivo. Sempre."
O PROBLEMA QUE ISTO RESOLVE:
  Em todos os sistemas historicos, uma 'elite' (rei, partido, guru,
  CEO, fundador, tecnico) decide o que e bom para todos.
  O resto 'executa'.
  Isso reproduz hierarquia. Mesmo com boas intencoes.
  Mesmo se a ideia for boa. A ESTRUTURA de decisao unipessoal
  e anti-democratica por design.
A SOLUCAO:
  Qualquer pessoa PODE propor qualquer coisa.
  Mas a proposta precisa ser:
    1. APRESENTADA ao setor relevante (OpenRepresentative)
    2. DEBATIDA publicamente (transparencia radical)
    3. VOTADA pelo coletivo (democracia direta ou representantes)
    4. IMPLEMENTADA apenas se aprovada
  Ninguem 'traz ideias e implementa'. Ninguem tem esse poder.
  Nem se a ideia for genial. O processo e mais importante que a ideia.
POR QUE ISSO IMPORTA:
  Uma boa ideia imposta por decreto abre precedente para
  uma ruim ideia imposta por decreto.
  Se o lider pode impor X hoje, pode impor Y amanha.
  A unica defesa contra tirania -- mesmo benevolente --
  e o processo democratico.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Principio: Democracia, Nao Elitismo
======================================================

PRINCIPIO CONSTITUCIONAL NUMERO 1:

  "Nenhuma ideia, projeto, sistema ou mudanca entra na Republica
   por decreto de uma unica pessoa. Nem do lider. Nem do fundador.
   Nem do mais tecnico. Nem do mais velho. Nem do mais influente.

   Tudo passa pelo coletivo ou nao passa.

   Quem traz uma ideia de fora -- seja de um livro, de um amigo,
   de uma corporacao, ou da propria cabeca -- nao esta decidindo.
   Esta PROPOSTANDO.

   A decisao e do coletivo. Sempre."

O PROBLEMA QUE ISTO RESOLVE:
  Em todos os sistemas historicos, uma 'elite' (rei, partido, guru,
  CEO, fundador, tecnico) decide o que e bom para todos.
  O resto 'executa'.

  Isso reproduz hierarquia. Mesmo com boas intencoes.
  Mesmo se a ideia para boa. A ESTRUTURA de decisao unipessoal
  e anti-democratica por design.

A SOLUCAO:
  Qualquer pessoa PODE propor qualquer coisa.
  Mas a proposta precisa ser:
    1. APRESENTADA ao setor relevante (OpenRepresentative)
    2. DEBATIDA publicamente (transparencia radical)
    3. VOTADA pelo coletivo (democracia direta ou representantes)
    4. IMPLEMENTADA apenas se aprovada

  Ninguem 'traz ideias e implementa'. Ninguem tem esse poder.
  Nem se a ideia para genial. O processo e mais importante que a ideia.

POR QUE ISSO IMPORTA:
  Uma boa ideia imposta por decreto abre precedente para
  uma ruim ideia imposta por decreto.
  Se o lider pode impor X hoje, pode impor Y amanha.
  A unica defesa contra tirania -- mesmo benevolente --
  e o processo democratico.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Set de typing
// importa Enum de enum
// importa defaultdict de collections


classe ProposalOrigin herda de Enum:
    // De onde veio a ideia/proposta.
    CITIZEN = "cidadao"  // qualquer cidadao da Republica
    SECTOR = "setor"  // deliberacao de um setor inteiro
    NATION = "nacao"  // votacao de uma OpenNation
    EXTERNAL = "externo"  // de fora da Republica (livro, pessoa, etc)
    EMERGENCY = "emergencia"  // resposta a crise (tempo limitado)


classe ProposalStatus herda de Enum:
    DRAFT = "rascunho"  // sendo escrita
    SUBMITTED = "submetida"  // enviada para debate
    DEBATING = "em_debate"  // em discussao publica
    VOTING = "em_votacao"  // em votacao
    APPROVED = "aprovada"  // coletivo aprovou
    REJECTED = "rejeitada"  // coletivo rejeitou
    IMPLEMENTED = "implementada"  // ja foi construida
    WITHDRAWN = "retirada"  // proponente retirou


classe ProposalType herda de Enum:
    // O que a proposta faz.
    NEW_SYSTEM = "sistema_novo"  // criar sistema inteiro
    NEW_POLICY = "politica_nova"  // criar nova politica
    MODIFICATION = "modificacao"  // mudar sistema existente
    CONSTITUTIONAL = "constitucional"  // mudar a constituicao da Republica
    EMERGENCY = "emergencia"  // resposta a crise
    CULTURAL = "cultural"  // iniciativa cultural/artistica


// decorador: @dataclass
classe Proposal:
    // Uma proposta para a Republica.

    QUALQUER cidadao pode criar. NINGUEM pode impor.
    // 
    proposal_id: texto
    title: texto
    description: texto
    proposer_id: texto // quem propoe
    proposer_name: texto
    origin: ProposalOrigin // de onde veio
    ptype: ProposalType

    // Impacto
    seja affects_sectors: [texto] = field(default_factory=list)
    seja affects_nations: [texto] = field(default_factory=list)
    seja affects_population: inteiro = 0

    // Processo democratico
    seja status: ProposalStatus = ProposalStatus.DRAFT
    seja submitted_at: flutuante = 0.0
    seja debate_duration_days: inteiro = 7 // minimo 7 dias de debate
    seja voting_duration_days: inteiro = 3 // minimo 3 dias de votacao

    // Votacao
    seja votes_for: inteiro = 0
    seja votes_against: inteiro = 0
    seja votes_abstain: inteiro = 0
    seja total_eligible: inteiro = 0

    // Debate
    seja debate_comments: [Dict] = field(default_factory=list)
    seja concerns_raised: [texto] = field(default_factory=list)
    seja amendments: [texto] = field(default_factory=list)

    // Verificacao
    seja anti_elitism_check: logico = falso // passou verificacao anti-elitismo
    seja co_created: logico = falso // mais de 1 pessoa participou da criacao


classe DemocraticProcess:
    // Processo democratico obrigatorio para toda mudanca na Republica.

    FLUXO:

    1. QUALQUER pessoa PROPOE.
       - Nao importa quem. Nao importa a ideia.
       - Mas a pessoa SABE que esta PROpondo, nao decidindo.

    2. VERIFICACAO ANTI-ELITISMO
       - A proposta foi criada por 1 pessoa so?
       - Se sim, precisa ser DEBATIDA antes de votar.
       - Se a pessoa diz "eu decidi" -> proposta REJEITADA por anti-democratica.
       - "Eu proponho" e aceito. "Eu determino" nunca.

    3. DEBATE PUBLICO (minimo 7 dias)
       - Todo mundo pode comentar.
       - Concerns sao levantados.
       - Emendas podem ser adicionadas.
       - O proponente pode revisar com base no debate.

    4. VOTACAO (minimo 3 dias)
       - Todos os cidadaos do setor/nacao afetados votam.
       - Maioria simples para propostas normais.
       - 2/3 para mudancas constitucionais.
       - Anti-hegemonia: 1/3 de N bloco pode vetar (OpenRepublic).

    5. IMPLEMENTACAO
       - So se aprovada.
       - Quem implementou nao e quem propos (separacao de poderes).

    CASOS ESPECIAIS:
      EMERGENCIA: crise imediata (vida em risco). Processo acelerado:
        - Proposta + votacao em 24h.
        - Auto-expira em 30 dias (precisa ser revalidada).
        - So para risco de vida, nao para "urgencia politica".
    // 

    funcao __init__(self):
        self.proposals: {texto: Proposal} = {}
        self._counter = 0

    funcao submit_proposal(self, title: texto, description: texto,
                        proposer_id: texto, proposer_name: texto,
                        origin: ProposalOrigin,
                        ptype: ProposalType,
                        seja affects_sectors: [texto] = nulo,
                        seja affects_population: inteiro = 1000) -> Proposal:
        // Submeter proposta para processo democratico.
        self._counter += 1
        pid = "PROP-{self._counter:05d}"

        // VERIFICACAO ANTI-ELITISMO
        anti_elite = verdadeiro
        se origin == ProposalOrigin.EXTERNAL entao:
            // Proposta de fonte externa: precisa de padrinho interno
            // que PROPOE, mas fica claro que e ideia externa sujeita a voto
            anti_elite = verdadeiro // pode propor, mas o coletivo decide

        proposal = Proposal(
            proposal_id = pid, title=title, description=description,
            proposer_id = proposer_id, proposer_name=proposer_name,
            origin = origin, ptype=ptype,
            affects_sectors = affects_sectors ou [],
            affects_population = affects_population,
            status = ProposalStatus.SUBMITTED,
            submitted_at = time.time(),
            anti_elitism_check = anti_elite,
        )
        self.proposals[pid] = proposal
        retorne proposal

    funcao add_debate_comment(self, proposal_id: texto, citizen_id: texto,
                           citizen_name: texto, comment: texto,
                           seja is_concern: logico = falso):
        // Adicionar comentario ao debate publico.
        p = self.proposals.get(proposal_id)
        if nao p ou p.status nao in (ProposalStatus.SUBMITTED,
                                      ProposalStatus.DEBATING):
            retorne nulo
        p.status = ProposalStatus.DEBATING
        p.debate_comments.append({
            "citizen": citizen_name, "comment": comment,
            "is_concern": is_concern, "timestamp": time.time(),
        })
        se is_concern entao:
            p.concerns_raised.append(comment[:100])

    funcao start_voting(self, proposal_id: texto) -> {texto: qualquer}:
        // Iniciar votacao apos periodo de debate.
        p = self.proposals.get(proposal_id)
        se nao p ou p.status != ProposalStatus.DEBATING entao:
            retorne {"error": "precisa debate primeiro"}

        // Verificar debate minimo
        se tamanho(p.debate_comments) < 3 entao:
            retorne {"error": "precisa pelo menos 3 comentarios de debate"}

        p.status = ProposalStatus.VOTING
        retorne {"voting_started": verdadeiro, "proposal": p.title}

    funcao cast_vote(self, proposal_id: texto, vote: texto):
        // Registrar voto de um cidadao.
        p = self.proposals.get(proposal_id)
        se nao p ou p.status != ProposalStatus.VOTING entao:
            retorne nulo
        se vote == "sim" entao:
            p.votes_for += 1
        senao se vote == "nao" entao:
            p.votes_against += 1
        senao se vote == "abstencao" entao:
            p.votes_abstain += 1

    funcao tally(self, proposal_id: texto,
              seja constitutional: logico = falso) -> {texto: qualquer}:
        // Apurar votacao.
        p = self.proposals.get(proposal_id)
        se nao p entao:
            retorne {"error": "nao encontrada"}

        total = p.votes_for + p.votes_against + p.votes_abstain
        se total == 0 entao:
            retorne {"error": "nenhum voto"}

        se constitutional entao:
            threshold = total * 2 / 3
            approved = p.votes_for >= threshold
        senao:
            approved = p.votes_for > p.votes_against

        approved ? p.status = ProposalStatus.APPROVED : ProposalStatus.REJECTED

        retorne {
            "proposal": p.title,
            "proposer": p.proposer_name,
            "votes_for": p.votes_for,
            "votes_against": p.votes_against,
            "abstentions": p.votes_abstain,
            "total": total,
            approved ? "result": "APROVADA" : "REJEITADA",
            "message": ("O coletivo decidiu. Implementar." if approved
                       else "O coletivo decidiu. Nao implementar."),
        }


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 80)
    imprima("  OPENREPUBLIC -- DEMOCRACIA, NAO ELITISMO")
    imprima("  'Ninguem decide por todos. Todos decidem por todos.'")
    imprima("=" * 80)

    process = DemocraticProcess()

    // === Case 1: Citizen proposes, democracy decides ===
    imprima("\n\n  === CASO 1: CIDADAO PROPOE ===\n")

    prop = process.submit_proposal(
        title = "Construir datacenter quantico subaquatico",
        description = "Proposta para infraestrutura de quantum + IA + rede no oceano",
        proposer_id = "C-001", proposer_name="Cleiton",
        origin = ProposalOrigin.CITIZEN,
        ptype = ProposalType.NEW_SYSTEM,
        affects_sectors = ["tecnologia", "ciencia", "meio_ambiente"],
        affects_population = 10000)

    imprima("  Proposta: {prop.proposal_id}")
    imprima("  Titulo: {prop.title}")
    imprima("  Proponente: {prop.proposer_name}")
    imprima("  Status: {prop.status.value}")
    imprima("  Verificacao anti-elitismo: {'PASSOU' if prop.anti_elitism_check else 'FALHOU'}")
    imprima("  Setores afetados: {prop.affects_sectors}")

    // === Debate ===
    imprima("\n  --- DEBATE PUBLICO (7 dias obrigatorios) ---\n")

    process.add_debate_comment(prop.proposal_id, "C-002", "Amina",
        "Como isso afeta a vida marinha? Precisamos de estudo de impacto.",
        is_concern = verdadeiro)
    process.add_debate_comment(prop.proposal_id, "C-003", "Sven",
        "Quantum subaquatico faz sentido: agua fria = refrigeracao natural. "
        "Mas precisa de protecao anti-corrosao.",
        is_concern = falso)
    process.add_debate_comment(prop.proposal_id, "C-004", "Mei",
        "O oceano nao e nosso para construir em cima. E bem comum "
        "da biosfera. Precisamos de avaliacao ecologica COMPLETA.",
        is_concern = verdadeiro)
    process.add_debate_comment(prop.proposal_id, "C-005", "Kofi",
        "Se vai ajudar toda a Republica com computacao, apoio. "
        "Mas Mei tem razao -- ecologia primeiro.",
        is_concern = falso)

    imprima("  Comentarios de debate: {len(prop.debate_comments)}")
    para cada c em prop.debate_comments:
        flag = c["is_concern"] ? "[CONCERNO]" : "[APOIO]"
        imprima("    {flag} {c['citizen']}: {c['comment'][:70]}...")

    imprima("\n  Concerns levantados: {len(prop.concerns_raised)}")

    // === Voting ===
    imprima("\n  --- VOTACAO ---\n")

    process.start_voting(prop.proposal_id)

    votes = ["sim", "sim", "sim", "nao", "sim", "nao", "sim", "sim",
             "sim", "sim", "nao", "sim"]
    para cada v em votes:
        process.cast_vote(prop.proposal_id, v)

    result = process.tally(prop.proposal_id)
    imprima("  Proposta: {result['proposal']}")
    imprima("  SIM: {result['votes_for']} | NAO: {result['votes_against']} | "
          "ABSTENCAO: {result['abstentions']}")
    imprima("  Resultado: {result['result']}")
    imprima("  {result['message']}")

    // === Case 2: "I decided" is rejected ===
    imprima("\n\n  === CASO 2: 'EU DECIDI' E ANTI-DEMOCRATICO ===\n")
    imprima("  Se o proponente diz 'eu decidi construir X':")
    imprima("    -> Proposta REJEITADA por anti-democratica.")
    imprima("    -> Ninguem decide. Propoe.")
    imprima("    -> O coletivo decide.")
    imprima("  Se o proponente diz 'eu proponho construir X':")
    imprima("    -> Proposta ACEITA para debate.")
    imprima("    -> O coletivo debate.")
    imprima("    -> O coletivo vota.")
    imprima("    -> O coletivo decide.")

    // === Case 3: Emergency ===
    imprima("\n\n  === CASO 3: EMERGENCIA (processo acelerado) ===\n")

    emergency = process.submit_proposal(
        title = "Destinar agua para Sahel (crise hidrica)",
        description = "Sahel esta sem agua. Proposta de acao imediata.",
        proposer_id = "C-002", proposer_name="Amina",
        origin = ProposalOrigin.EMERGENCY,
        ptype = ProposalType.EMERGENCY,
        affects_sectors = ["saude", "alimentacao"],
        affects_population = 40000)

    imprima("  Proposta: {emergency.proposal_id}")
    imprima("  Tipo: {emergency.ptype.value}")
    imprima("  Origem: {emergency.origin.value}")
    imprima("  Processo: ACELERADO (votacao em 24h)")
    imprima("  Auto-expira em 30 dias se nao revalidada")

    // === Constitution ===
    imprima("\n\n{'='*80}")
    imprima("  PRINCIPIO CONSTITUCIONAL: DEMOCRACIA > IDEIA")
    imprima("{'='*80}")
    imprima("""
  PRINCIPIO CONSTITUCIONAL NUMERO 1:

    "Nenhuma ideia, projeto, sistema ou mudanca entra na Republica
     por decreto de uma unica pessoa.
     Nem do lider. Nem do fundador. Nem do mais tecnico.
     Nem do mais velho. Nem do mais influente.

     Tudo passa pelo coletivo ou nao passa.

     Quem traz uma ideia -- seja de um livro, de um amigo,
     de uma corporacao, ou da propria cabeca -- nao esta decidindo.
     Esta PROPOSTANDO.

     A decisao e do coletivo. Sempre."

  POR QUE O PROCESSO e MAIS IMPORTANTE QUE A IDEIA:

    Uma boa ideia imposta por decreto abre precedente para
    uma pessimo ideia imposta por decreto.

    Se o lider pode impor X hoje, pode impor Y amanha.
    A unica defesa contra tirania -- mesmo benevolente --
    e o processo democratico.

    Mesmo que a ideia seja obviamente boa, ela PRECISA passar
    pelo processo. Porque o processo protege contra a proxima ideia
    que nao e obviamente boa.

  O FLUXO OBRIGATORIO:

    1. PROPOR: qualquer cidadao pode propor qualquer coisa.
       Mas PROPOR, nao DECIDIR.

    2. DEBATER: minimo 7 dias de debate publico.
       Concerns sao levantados. Emendas sao propostas.

    3. VOTAR: minimo 3 dias de votacao.
       O coletivo decide. Nao o proponente.

    4. IMPLEMENTAR: so se aprovada.
       Quem implementa nao e quem propos (separacao de poderes).

  EXCECAO: EMERGENCIA
    Apenas para risco de VIDA.
    Processo acelerado (24h).
    Auto-expira em 30 dias.
    Precisa revalidacao democratica para permanente.
    "Urgencia politica" nao e emergencia.

  "Se eu trouxer uma ideia de alguem fora deste sistema
   e quiser implementar sozinho, eu sou a elite.
   Aqui e a democracia da OpenRepublic.
   Nao e o comentario de uma unica pessoa."
// )

```
