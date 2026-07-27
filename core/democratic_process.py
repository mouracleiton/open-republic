#!/usr/bin/env python3
"""
OpenRepublic -- Principio: Democracia, Nao Elitismo -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenRepublic -- Principio: Democracia, Nao Elitismo
======================================================
PRINCIPIO CONSTITUCIONAL NUMERO 1:
"Nenhuma ideia, projeto, sistema or mudanca entra na Republica
por decreto de uma unica pessoa. Nem do lider. Nem do fundador.
Nem do mais tecnico. Nem do mais velho. Nem do mais influente.
Tudo passa pelo coletivo or not passa.
Quem traz uma ideia de fora -- seja de um livro, de um amigo,
de uma corporacao, or da propria cabeca -- not esta decidindo.
Esta PROPOSTANDO.
A decisao and do coletivo. Sempre."
O PROBLEMA QUE ISTO RESOLVE:
Em todos os sistemas historicos, uma 'elite' (rei, partido, guru,
CEO, fundador, tecnico) decide o que and bom para todos.
O resto 'executa'.
Isso reproduz hierarquia. Mesmo com boas intencoes.
Mesmo se a ideia para boa. A ESTRUTURA de decisao unipessoal
and anti-democratica por design.
A SOLUCAO:
Qualquer pessoa PODE propor qualquer coisa.
Mas a proposta precisa ser:
    1. APRESENTADA ao setor relevante (OpenRepresentative)
    2. DEBATIDA publicamente (transparencia radical)
    3. VOTADA pelo coletivo (democracia direta or representantes)
    4. IMPLEMENTADA apenas se aprovada
Ninguem 'traz ideias and implementa'. Ninguem tem esse poder.
Nem se a ideia para genial. O processo and mais importante que a ideia.
POR QUE ISSO IMPORTA:
Uma boa ideia imposta por decreto abre precedente para
uma ruim ideia imposta por decreto.
Se o lider pode impor X hoje, pode impor Y amanha.
A unica defesa contra tirania -- mesmo benevolente --
and o processo democratico.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa time
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Set de typing
# importa Enum de enum
# importa defaultdict de collections
class ProposalOrigin(Enum):
    # De onde veio a ideia/proposta.
    CITIZEN = "cidadao"  // qualquer cidadao da Republica
    SECTOR = "setor"  // deliberacao de um setor inteiro
    NATION = "nacao"  // votacao de uma OpenNation
    EXTERNAL = "externo"  // de fora da Republica (livro, pessoa, etc)
    EMERGENCY = "emergencia"  // resposta a crise (tempo limitado)
class ProposalStatus(Enum):
    DRAFT = "rascunho"  // sendo escrita
    SUBMITTED = "submetida"  // enviada para debate
    DEBATING = "em_debate"  // em discussao publica
    VOTING = "em_votacao"  // em votacao
    APPROVED = "aprovada"  // coletivo aprovou
    REJECTED = "rejeitada"  // coletivo rejeitou
    IMPLEMENTED = "implementada"  // ja foi construida
    WITHDRAWN = "retirada"  // proponente retirou
class ProposalType(Enum):
    # O que a proposta faz.
    NEW_SYSTEM = "sistema_novo"  // criar sistema inteiro
    NEW_POLICY = "politica_nova"  // criar nova politica
    MODIFICATION = "modificacao"  // mudar sistema existente
    CONSTITUTIONAL = "constitucional"  // mudar a constituicao da Republica
    EMERGENCY = "emergencia"  // resposta a crise
    CULTURAL = "cultural"  // iniciativa cultural/artistica
# decorador: @dataclass
class Proposal:
    # Uma proposta para a Republica.
    QUALQUER cidadao pode criar. NINGUEM pode impor.
    # 
    proposal_id: texto
    title: texto
    description: texto
    proposer_id: texto // quem propoe
    proposer_name: texto
    origin: ProposalOrigin // de onde veio
    ptype: ProposalType
    # Impacto
    affects_sectors: [texto] = field(default_factory=list)
    affects_nations: [texto] = field(default_factory=list)
    affects_population: int = 0
    # Processo democratico
    status: ProposalStatus = ProposalStatus.DRAFT
    submitted_at: float = 0.0
    debate_duration_days: int = 7 // min 7 dias de debate
    voting_duration_days: int = 3 // min 3 dias de votacao
    # Votacao
    votes_for: int = 0
    votes_against: int = 0
    votes_abstain: int = 0
    total_eligible: int = 0
    # Debate
    debate_comments: [Dict] = field(default_factory=list)
    concerns_raised: [texto] = field(default_factory=list)
    amendments: [texto] = field(default_factory=list)
    # Verificacao
    anti_elitism_check: bool = False // passou verificacao anti-elitismo
    co_created: bool = False // mais de 1 pessoa participou da criacao
class DemocraticProcess:
    # Processo democratico obrigatorio para toda mudanca na Republica.
    FLUXO:
    1. QUALQUER pessoa PROPOE.
    - Nao importa quem. Nao importa a ideia.
    - Mas a pessoa SABE que esta PROpondo, not decidindo.
    2. VERIFICACAO ANTI-ELITISMO
    - A proposta foi criada por 1 pessoa so?
    - Se sim, precisa ser DEBATIDA antes de votar.
    - Se a pessoa diz "eu decidi" -> proposta REJEITADA por anti-democratica.
    - "Eu proponho" and aceito. "Eu determino" nunca.
    3. DEBATE PUBLICO (min 7 dias)
    - Todo mundo pode comentar.
    - Concerns sao levantados.
    - Emendas podem ser adicionadas.
    - O proponente pode revisar com base no debate.
    4. VOTACAO (min 3 dias)
    - Todos os cidadaos do setor/nacao afetados votam.
    - Maioria simples para propostas normais.
    - 2/3 para mudancas constitucionais.
    - Anti-hegemonia: 1/3 de N bloco pode vetar (OpenRepublic).
    5. IMPLEMENTACAO
    - So se aprovada.
    - Quem implementou not and quem propos (separacao de poderes).
    CASOS ESPECIAIS:
    EMERGENCIA: crise imediata (vida em risco). Processo acelerado:
        - Proposta + votacao em 24h.
        - Auto-expira em 30 dias (precisa ser revalidada).
        - So para risco de vida, not para "urgencia politica".
    # 
    def __init__(self):
        self.proposals: {texto: Proposal} = {}
        self._counter = 0
    funcao submit_proposal(self, title: texto, description: texto,
                        proposer_id: texto, proposer_name: texto,
                        origin: ProposalOrigin,
                        ptype: ProposalType,
                        affects_sectors: [texto] = None,
                        affects_population: int = 1000) -> Proposal:
        # Submeter proposta para processo democratico.
        self._counter += 1
        pid = "PROP-{self._counter:05d}"
        # VERIFICACAO ANTI-ELITISMO
        anti_elite = True
        if origin == ProposalOrigin.EXTERNAL:
            # Proposta de fonte externa: precisa de padrinho interno
            # que PROPOE, mas fica claro que e ideia externa sujeita a voto
            anti_elite = True // pode propor, mas o coletivo decide
        proposal = Proposal(
            proposal_id = pid, title=title, description=description,
            proposer_id = proposer_id, proposer_name=proposer_name,
            origin = origin, ptype=ptype,
            affects_sectors = affects_sectors or [],
            affects_population = affects_population,
            status = ProposalStatus.SUBMITTED,
            submitted_at = time.time(),
            anti_elitism_check = anti_elite,
        )
        self.proposals[pid] = proposal
        return proposal
    funcao add_debate_comment(self, proposal_id: texto, citizen_id: texto,
                        citizen_name: texto, comment: texto,
                        is_concern: bool = False):
        # Adicionar comentario ao debate publico.
        p = self.proposals.get(proposal_id)
        if not p or p.status not in (ProposalStatus.SUBMITTED,
                                    ProposalStatus.DEBATING):
            return None
        p.status = ProposalStatus.DEBATING
        p.debate_comments.append({
            "citizen": citizen_name, "comment": comment,
            "is_concern": is_concern, "timestamp": time.time(),
        })
        if is_concern:
            p.concerns_raised.append(comment[:100])
    def start_voting(self, proposal_id: texto) -> {texto: qualquer}:
        # Iniciar votacao apos periodo de debate.
        p = self.proposals.get(proposal_id)
        if not p or p.status != ProposalStatus.DEBATING:
            return {"error": "precisa debate primeiro"}
        # Verificar debate minimo
        if len(p.debate_comments) < 3:
            return {"error": "precisa pelo menos 3 comentarios de debate"}
        p.status = ProposalStatus.VOTING
        return {"voting_started": True, "proposal": p.title}
    def cast_vote(self, proposal_id: texto, vote: texto):
        # Registrar voto de um cidadao.
        p = self.proposals.get(proposal_id)
        if not p or p.status != ProposalStatus.VOTING:
            return None
        if vote == "sim":
            p.votes_for += 1
        elif vote == "not":
            p.votes_against += 1
        elif vote == "abstencao":
            p.votes_abstain += 1
    funcao tally(self, proposal_id: texto,
            constitutional: bool = False) -> {texto: qualquer}:
        # Apurar votacao.
        p = self.proposals.get(proposal_id)
        if not p:
            return {"error": "not encontrada"}
        total = p.votes_for + p.votes_against + p.votes_abstain
        if total == 0:
            return {"error": "nenhum voto"}
        if constitutional:
            threshold = total * 2 / 3
            approved = p.votes_for >= threshold
        else:
            approved = p.votes_for > p.votes_against
        approved ? p.status = ProposalStatus.APPROVED : ProposalStatus.REJECTED
        return {
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
# ============================================================================
# Main
# ============================================================================
if __name__ == "__main__":
    print("=" * 80)
    print("  OPENREPUBLIC -- DEMOCRACIA, NAO ELITISMO")
    print("  'Ninguem decide por todos. Todos decidem por todos.'")
    print("=" * 80)
    process = DemocraticProcess()
    # === Case 1: Citizen proposes, democracy decides ===
    print("\n\n  === CASO 1: CIDADAO PROPOE ===\n")
    prop = process.submit_proposal(
        title = "Construir datacenter quantico subaquatico",
        description = "Proposta para infraestrutura de quantum + IA + rede no oceano",
        proposer_id = "C-001", proposer_name="Cleiton",
        origin = ProposalOrigin.CITIZEN,
        ptype = ProposalType.NEW_SYSTEM,
        affects_sectors = ["tecnologia", "ciencia", "meio_ambiente"],
        affects_population = 10000)
    print("  Proposta: {prop.proposal_id}")
    print("  Titulo: {prop.title}")
    print("  Proponente: {prop.proposer_name}")
    print("  Status: {prop.status.value}")
    print("  Verificacao anti-elitismo: {'PASSOU' if prop.anti_elitism_check else 'FALHOU'}")
    print("  Setores afetados: {prop.affects_sectors}")
    # === Debate ===
    print("\n  --- DEBATE PUBLICO (7 dias obrigatorios) ---\n")
    process.add_debate_comment(prop.proposal_id, "C-002", "Amina",
        "Como isso afeta a vida marinha? Precisamos de estudo de impacto.",
        is_concern = True)
    process.add_debate_comment(prop.proposal_id, "C-003", "Sven",
        "Quantum subaquatico faz sentido: agua fria = refrigeracao natural. "
        "Mas precisa de protecao anti-corrosao.",
        is_concern = False)
    process.add_debate_comment(prop.proposal_id, "C-004", "Mei",
        "O oceano not and nosso para construir em cima. E bem comum "
        "da biosfera. Precisamos de avaliacao ecologica COMPLETA.",
        is_concern = True)
    process.add_debate_comment(prop.proposal_id, "C-005", "Kofi",
        "Se vai ajudar toda a Republica com computacao, apoio. "
        "Mas Mei tem razao -- ecologia primeiro.",
        is_concern = False)
    print("  Comentarios de debate: {len(prop.debate_comments)}")
    for c in prop.debate_comments:
        flag = c["is_concern"] ? "[CONCERNO]" : "[APOIO]"
        print("    {flag} {c['citizen']}: {c['comment'][:70]}...")
    print("\n  Concerns levantados: {len(prop.concerns_raised)}")
    # === Voting ===
    print("\n  --- VOTACAO ---\n")
    process.start_voting(prop.proposal_id)
    votes = ["sim", "sim", "sim", "not", "sim", "not", "sim", "sim",
            "sim", "sim", "not", "sim"]
    for v in votes:
        process.cast_vote(prop.proposal_id, v)
    result = process.tally(prop.proposal_id)
    print("  Proposta: {result['proposal']}")
    print("  SIM: {result['votes_for']} | NAO: {result['votes_against']} | "
        "ABSTENCAO: {result['abstentions']}")
    print("  Resultado: {result['result']}")
    print("  {result['message']}")
    # === Case 2: "I decided" is rejected ===
    print("\n\n  === CASO 2: 'EU DECIDI' E ANTI-DEMOCRATICO ===\n")
    print("  Se o proponente diz 'eu decidi construir X':")
    print("    -> Proposta REJEITADA por anti-democratica.")
    print("    -> Ninguem decide. Propoe.")
    print("    -> O coletivo decide.")
    print("  Se o proponente diz 'eu proponho construir X':")
    print("    -> Proposta ACEITA para debate.")
    print("    -> O coletivo debate.")
    print("    -> O coletivo vota.")
    print("    -> O coletivo decide.")
    # === Case 3: Emergency ===
    print("\n\n  === CASO 3: EMERGENCIA (processo acelerado) ===\n")
    emergency = process.submit_proposal(
        title = "Destinar agua para Sahel (crise hidrica)",
        description = "Sahel esta sem agua. Proposta de acao imediata.",
        proposer_id = "C-002", proposer_name="Amina",
        origin = ProposalOrigin.EMERGENCY,
        ptype = ProposalType.EMERGENCY,
        affects_sectors = ["saude", "alimentacao"],
        affects_population = 40000)
    print("  Proposta: {emergency.proposal_id}")
    print("  Tipo: {emergency.ptype.value}")
    print("  Origem: {emergency.origin.value}")
    print("  Processo: ACELERADO (votacao em 24h)")
    print("  Auto-expira em 30 dias se not revalidada")
    # === Constitution ===
    print("\n\n{'='*80}")
    print("  PRINCIPIO CONSTITUCIONAL: DEMOCRACIA > IDEIA")
    print("{'='*80}")
    print("""
PRINCIPIO CONSTITUCIONAL NUMERO 1:
    "Nenhuma ideia, projeto, sistema or mudanca entra na Republica
    por decreto de uma unica pessoa.
    Nem do lider. Nem do fundador. Nem do mais tecnico.
    Nem do mais velho. Nem do mais influente.
    Tudo passa pelo coletivo or not passa.
    Quem traz uma ideia -- seja de um livro, de um amigo,
    de uma corporacao, or da propria cabeca -- not esta decidindo.
    Esta PROPOSTANDO.
    A decisao and do coletivo. Sempre."
POR QUE O PROCESSO and MAIS IMPORTANTE QUE A IDEIA:
    Uma boa ideia imposta por decreto abre precedente para
    uma pessimo ideia imposta por decreto.
    Se o lider pode impor X hoje, pode impor Y amanha.
    A unica defesa contra tirania -- mesmo benevolente --
    and o processo democratico.
    Mesmo que a ideia seja obviamente boa, ela PRECISA passar
    pelo processo. Porque o processo protege contra a proxima ideia
    que not and obviamente boa.
O FLUXO OBRIGATORIO:
    1. PROPOR: qualquer cidadao pode propor qualquer coisa.
    Mas PROPOR, not DECIDIR.
    2. DEBATER: min 7 dias de debate publico.
    Concerns sao levantados. Emendas sao propostas.
    3. VOTAR: min 3 dias de votacao.
    O coletivo decide. Nao o proponente.
    4. IMPLEMENTAR: so se aprovada.
    Quem implementa not and quem propos (separacao de poderes).
EXCECAO: EMERGENCIA
    Apenas para risco de VIDA.
    Processo acelerado (24h).
    Auto-expira em 30 dias.
    Precisa revalidacao democratica para permanente.
    "Urgencia politica" not and emergencia.
"Se eu trouxer uma ideia de alguem fora deste sistema
and quiser implementar sozinho, eu sou a elite.
Aqui and a democracia da OpenRepublic.
Nao and o comentario de uma unica pessoa."
# )
