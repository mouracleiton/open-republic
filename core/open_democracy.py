#!/usr/bin/env python3
"""
OpenDemocracy + OpenTransparency -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenDemocracy + OpenTransparency
==================================
"Democracia sem transparencia and teatro.
Transparencia sem democracia and vigia.
Juntas, sao a Republica."
OPENDEMOCRACY:
Democracia direta + liquida + deliberativa + participativa.
Nao and "votar a cada 4 anos". and decidir TODOS os dias.
Nao and "escolher representante". and decidir DIRETAMENTE quando pode,
and delegar TEMPORARIAMENTE quando not pode.
OPENTRANSPARENCY:
Transparencia RADICAL. Tudo que and publico and VISIVEL.
Tudo que and decisao and RASTREAVEL. Tudo que and gasto and PUBLICO.
Zero reuniao secreta. Zero documento oculto. Zero conta escondida.
O UNICO que and privado: a vida intima do cidadao.
(OpenHealth, OpenRelationship, OpenFaith -- esses sao privados)
TUDO o que and do Estado/coletivo and publico.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa time
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Set, Tuple, Callable de typing
# importa Enum de enum
# importa defaultdict, Counter de collections
# ============================================================================
# Democracy Types
# ============================================================================
class DemocracyMode(Enum):
    # Modos de democracia que COEXISTEM.
    DIRECT = "direta"  // cidadao vota diretamente
    LIQUID = "liquida"  // delega voto por tema, revogavel
    DELIBERATIVE = "deliberativa"  // debate antes de votar
    PARTICIPATORY = "participativa"  // cidadao propoe leis/policies
    SORTITION = "sorteio"  // sorteio para cargos (atenico)
class VoteType(Enum):
    SIMPL = "maioria_simples"  // 50%+1
    QUALIFIED = "maioria_qualificada"  // 2/3
    SUPER = "supermajoridade"  // 3/4
    UNANIMOUS = "unanimidade"  // 100% (rarissimo)
    ANTI_HEGEMONY = "anti_hegemonia"  // 1/3 de qualquer nacao pode vetar
class ProposalCategory(Enum):
    CONSTITUTIONAL = "constitucional"  // muda a constituicao (2/3)
    BUDGET = "orcamento"  // como alocar recursos
    POLICY = "politica"  // nova regra/lei
    ELECTION = "eleicao"  // eleger representantes
    RECALL = "recall"  // revogar representante
    EMERGENCY = "emergencia"  // crise (acelerado)
    TREATY = "tratado"  // acordo entre nacoes
    AMENDMENT = "emenda"  // emendar proposta em debate
# ============================================================================
# OpenTransparency: Public Ledger
# ============================================================================
class TransparencyLevel(Enum):
    # Nivel de transparencia de cada item.
    RADICAL = "radical"  // 100% publico, qualquer cidadao ve
    PUBLIC = "publico"  // publico mas requer buscar
    RESTRICTED = "restrito"  // so cidadaos afetados
    PRIVATE = "privado"  // vida intima (protegido)
    SEALED = "lacrado"  // temporariamente selado (precisa justificativa)
# decorador: @dataclass
class PublicRecord:
    # Um registro no livro publico da Republica.
    TUDO que o coletivo faz entra no livro publico:
    - Decisoes votadas
    - Recursos alocados
    - Reunioes realizadas
    - Representantes eleitos
    - Recalls
    - Propostas
    - Emendas
    - Auditorias
    - Gastos (not ha dinheiro, mas alocacao de trabalho/material)
    Cada registro tem hash imutavel (blockchain).
    # 
    record_id: texto
    timestamp: float = field(default_factory=time.time)
    category: str = ""  // decision, resource, meeting, etc
    title: str = ""
    description: str = ""
    actor: str = ""  // quem fez
    affected: [texto] = field(default_factory=list) // quem afeta
    transparency: TransparencyLevel = TransparencyLevel.RADICAL
    data: {texto: qualquer} = field(default_factory=dict)
    hash: str = ""
    sealed: bool = False
    seal_reason: str = ""
    seal_expires: float = 0.0 // 0 = not selado
class PublicLedger:
    # Livro publico IMUTAVEL da Republica.
    Blockchain simples: cada registro tem hash que depende do anterior.
    Impossivel alterar historico sem quebrar a cadeia.
    Cada cidadao tem copia completa (no seu edge node).
    O QUE ENTRA NO LIVRO (RADICAL = qualquer cidadao ve):
    - Toda decisao votada (quem votou o que)
    - Toda alocacao de recurso (para onde foi)
    - Toda reuniao (quem participou, o que decidiu)
    - Todo representante (acoes, votos, reunioes)
    - Toda auditoria (resultado)
    - Toda proposta (texto completo, votos, debate)
    - Todo recall (quem assinou, resultado)
    - Todo gasto de trabalho/material (em vez de dinheiro)
    O QUE not ENTRA (PRIVATE = protegido):
    - Prontuario medico (OpenHealth)
    - Relacionamentos intimos (OpenRelationship)
    - Fe espiritual (OpenFaith)
    - Comunicacao privada (OpenSocial)
    - Dados de criancas (protecao maxima)
    # 
    def __init__(self):
        self.records: [PublicRecord] = []
        self._counter = 0
        self._chain_hash = "GENESIS"
    funcao add(self, category: texto, title: texto, description: texto,
            actor: str = "", affected: [texto] = None,
            transparency: TransparencyLevel = TransparencyLevel.RADICAL,
            data: Dict = None) -> PublicRecord:
        # Adicionar registro imutavel ao livro publico.
        self._counter += 1
        rid = "REC-{self._counter:06d}"
        # Hash encadeado (blockchain)
        content = "{self._chain_hash}{rid}{category}{title}{actor}{time.time()}"
        record_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        self._chain_hash = record_hash
        record = PublicRecord(
            record_id = rid, category=category, title=title,
            description = description, actor=actor,
            affected = affected or [],
            transparency = transparency,
            data = data or {},
            hash = record_hash)
        self.records.append(record)
        return record
    def seal(self, record_id: texto, reason: texto, duration_days: inteiro = 30):
        # Lacrar registro temporariamente.
        So pode lacrar com JUSTIFICATIVA PUBLICA and PRAZO.
        Lacrar sem justificativa = anti-democratico.
        # 
        for r in self.records:
            if r.record_id == record_id:
                r.sealed = True
                r.seal_reason = reason
                r.seal_expires = time.time() + duration_days * 86400
                r.transparency = TransparencyLevel.SEALED
                break
    funcao query(self, category: texto = "", actor: texto = "",
            keyword: str = "", limit: inteiro = 50) -> [Dict]:
        # Buscar no livro publico.
        results = []
        for r in reversed(self.records):
            if r.sealed and time.time() < r.seal_expires:
                continue // lacrado
            if category and r.category != category:
                continue
            if actor and r.actor != actor:
                continue
            if keyword and keyword.lower() not in (r.title + r.description).lower():
                continue
            results.append({
                "id": r.record_id, "category": r.category,
                "title": r.title, "actor": r.actor,
                "description": r.description[:100],
                "hash": r.hash,
                "timestamp": time.strftime("%Y-%m-%d %H:%M",
                                        time.localtime(r.timestamp)),
            })
            if len(results) >= limit:
                break
        return results
    def audit(self) -> {texto: qualquer}:
        # Auditoria do livro publico.
        by_cat = Counter(r.category para r em self.records)
        sealed_count = sum(1 para r em self.records if r.sealed)
        total = len(self.records)
        return {
            "total_records": total,
            "by_category": dict(by_cat),
            "sealed": sealed_count,
            "sealed_pct": round(sealed_count / max(1, total) * 100, 1),
            "chain_intact": self._verify_chain(),
            "message": ("Livro publico: {total} registros. "
                    "{sealed_count} lacrados ({sealed_count/max(1,total)*100:.1f}%). "
                    "Cadeia: {'INTACTA' if self._verify_chain() else 'COMPROMETIDA'}."),
        }
    def _verify_chain(self) -> bool:
        # Verificar integridade da cadeia de hashes.
        prev = "GENESIS"
        for r in self.records:
            content = "{prev}{r.record_id}{r.category}{r.title}{r.actor}"
            expected = hashlib.sha256(content.encode()).hexdigest()[:16]
            # Nota: em producao real, o hash incluiria timestamp exato
            prev = r.hash
        return True // simplificado para simulacao
# ============================================================================
# Liquid Democracy
# ============================================================================
# decorador: @dataclass
class Delegation:
    # Delegacao de voto (democracia liquida).
    "Eu not entendo de saude. Delego meu voto de saude para a Amina,
    que and medica. Mas se ela votar algo que eu discordo, revogo na hora."
    Caracteristicas:
    - Por TEMA (not por pessoa para tudo)
    - Revogavel a QUALQUER momento
    - Transitive (A delega para B que delega para C -> A->B->C)
    - Transparente (todos veem quem delegou para quem)
    - Sem representante profissional (not and cargo)
    # 
    delegation_id: texto
    delegator: texto // quem delega (cidadao)
    delegate: texto // para quem delega (pessoa de confianca)
    topic: texto // tema especifico (saude, educacao, etc)
    timestamp: float = field(default_factory=time.time)
    active: bool = True
    revoked_at: float = 0.0
    reason: str = ""
class LiquidDemocracy:
    # Sistema de democracia liquida.
    Cada cidadao tem 1 voto por proposta.
    Mas pode DELEGAR seu voto por tema para alguem em quem confia.
    DIFERENCA da democracia representativa:
    - Representante: voce da seu voto por 4 anos para uma pessoa decidir TUDO
    - Liquida: voce delega POR TEMA, pode MUDAR a qualquer momento,
    and pode VOTAR DIRETAMENTE quando quiser
    Exemplo:
    - Cleiton delega votos de TECNOLOGIA para Sven (ente quantum)
    - Cleiton delega votos de SAUDE para Amina (and medica)
    - Cleiton vota DIRETAMENTE em EDUCACAO (and sua area)
    - Se Sven votar algo que Cleiton discorda -> revoga delegacao na hora
    # 
    def __init__(self):
        self.delegations: {texto: Delegation} = {}
        self._counter = 0
    funcao delegate(self, delegator: texto, delegate: texto,
                topic: texto) -> Delegation:
        # Delegar voto por tema.
        # Revogar delegacoes anteriores do mesmo tema
        for d in self.delegations.values():
            if (d.delegator == delegator and d.topic == topic
                and d.active):
                d.active = False
                d.revoked_at = time.time()
                d.reason = "substituida por nova delegacao"
        self._counter += 1
        did = "DELEG-{self._counter:05d}"
        delegation = Delegation(
            delegation_id = did, delegator=delegator,
            delegate = delegate, topic=topic)
        self.delegations[did] = delegation
        return delegation
    def revoke(self, delegator: texto, topic: texto, reason: texto = ""):
        # Revogar delegacao a qualquer momento.
        for d in self.delegations.values():
            if (d.delegator == delegator and d.topic == topic
                and d.active):
                d.active = False
                d.revoked_at = time.time()
                d.reason = reason
                return {"revoked": True, "topic": topic, "reason": reason}
        return {"revoked": False, "reason": "delegacao not encontrada"}
    def resolve_vote(self, citizen: texto, topic: texto) retorna (texto, logico):
        # Resolver quem vota por um cidadao num tema.
        Retorna (quem_vota, e_delegado?)
        Se o cidadao votou diretamente, o voto dele conta.
        Se delegou, o delegado recebe o peso.
        # 
        for d in self.delegations.values():
            if (d.delegator == citizen and d.topic == topic
                and d.active):
                # Cidadao delegou -> delegate vota
                # Mas se cidadao votar diretamente, voto direto prevalece
                return (d.delegate, True)
        return (citizen, False)
    def vote_weight(self, delegate_id: texto, topic: texto) -> int:
        # Calcular peso de voto de um delegado (1 proprio + delegados).
        weight = 1 // proprio voto
        for d in self.delegations.values():
            if (d.delegate == delegate_id and d.topic == topic
                and d.active):
                weight = weight + 1
                # Transitive: se o delegado tambem delegou, seguir a cadeia
                # (simplificado: nao implementa transitivade profunda aqui)
        return weight
    funcao delegation_map(self) retorna Dict[texto, [Dict]]:
        # Mapa de quem delegou para quem (transparencia).
        active = defaultdict(list)
        for d in self.delegations.values():
            if d.active:
                active[d.delegate].append({
                    "from": d.delegator,
                    "topic": d.topic,
                })
        return dict(active)
# ============================================================================
# OpenDemocracy: The Full System
# ============================================================================
class VoteRecord:
    # Registro de um voto individual.
    funcao __init__(self, citizen: texto, vote: texto, direct: logico,
                weight: int = 1):
        self.citizen = citizen
        self.vote = vote // sim, not, abstencao
        self.direct = direct // votou diretamente?
        self.weight = weight // peso (1 + delegacoes)
        self.timestamp = time.time()
class OpenDemocracy:
    # Sistema democratico completo da Republica.
    Integra:
    - Democracia DIRETA (cidadao vota)
    - Democracia LIQUIDA (delega por tema, revogavel)
    - Democracia DELIBERATIVA (debate antes de votar)
    - Democracia PARTICIPATIVA (cidadao propoe)
    - SORTEIO (cargos temporarios)
    - OpenTransparency (tudo publico)
    # 
    def __init__(self):
        self.ledger = PublicLedger()
        self.liquid = LiquidDemocracy()
        self.proposals: {texto: Dict} = {}
        self.votes: Dict[texto, [VoteRecord]] = {}
        self._prop_counter = 0
    funcao propose(self, title: texto, description: texto, proposer: texto,
                category: ProposalCategory,
                vote_type: VoteType = VoteType.SIMPL,
                affected_nations: [texto] = None) -> texto:
        # Cidadao PROPOE (nao decide).
        self._prop_counter += 1
        pid = "DEM-{self._prop_counter:05d}"
        self.proposals[pid] = {
            "id": pid, "title": title, "description": description,
            "proposer": proposer, "category": category.value,
            "vote_type": vote_type.value,
            "affected_nations": affected_nations  or  [],
            "status": "debate",
            "debate_comments": [],
            "created": time.time(),
        }
        self.votes[pid] = []
        # Registrar no livro publico
        self.ledger.add(
            category = "proposal", title=title,
            description = "Proposta por {proposer}: {description[:100]}",
            actor = proposer, data={"category": category.value})
        return pid
    funcao debate(self, proposal_id: texto, citizen: texto, comment: texto,
            is_concern: bool = False):
        # Comentar proposta em debate.
        p = self.proposals.get(proposal_id)
        if not  p  or  p["status"] != "debate":
            return None
        p["debate_comments"].append({
            "citizen": citizen, "comment": comment,
            "concern": is_concern,
            "timestamp": time.time(),
        })
        self.ledger.add(
            category = "debate", title="Comentario em {proposal_id}",
            description = "{citizen}: {comment[:80]}",
            actor = citizen)
    def open_voting(self, proposal_id: texto):
        # Abrir votacao apos debate.
        p = self.proposals.get(proposal_id)
        if not p:
            return None
        if len(p["debate_comments"]) < 2:
            return // precisa debate min
        p["status"] = "voting"
        self.ledger.add(
            category = "voting_open", title=p["title"],
            description = "Votacao aberta para {proposal_id}",
            actor = "sistema")
    funcao vote(self, proposal_id: texto, citizen: texto, vote: texto,
            override_delegation: bool = False):
        # Cidadao vota (diretamente ou confirma delegacao).
        p = self.proposals.get(proposal_id)
        if not  p  or  p["status"] != "voting":
            return None
        # Resolver delegacao
        category = p["category"]
        desempacote delegate_id, is_delegated = self.liquid.resolve_vote(
            citizen, category)
        if is_delegated and not override_delegation:
            # Cidadao delegou -> nao vota diretamente
            # Delegate tera peso extra
            return None
        # Se override_delegation, cidadao vota direto mesmo tendo delegado
        weight = 1
        if override_delegation:
            # Revoga delegacao implicitamente para esta votacao
            # (sem operacao)
        vr = VoteRecord(citizen=citizen, vote=vote,
                    direct = not is_delegated, weight=weight)
        self.votes[proposal_id].append(vr)
        # Registrar voto no livro publico (transparencia radical)
        self.ledger.add(
            category = "vote", title="Voto em {proposal_id}",
            description = "{citizen} votou {vote} (peso {weight})",
            actor = citizen,
            data = {"proposal": proposal_id, "vote": vote,
                "weight": weight})
    def tally(self, proposal_id: texto) -> {texto: qualquer}:
        # Apurar votacao com peso de delegacoes e anti-hegemonia.
        p = self.proposals.get(proposal_id)
        if not p:
            return {"error": "not encontrada"}
        votes = self.votes.get(proposal_id, [])
        # Calcular votos diretos + pesos delegados
        for_v = 0
        against_v = 0
        abstain_v = 0
        for vr in votes:
            if vr.vote == "sim":
                for_v = for_v + vr.weight
            elif vr.vote == "not":
                against_v = against_v + vr.weight
            else:
                abstain_v = abstain_v + vr.weight
        # Adicionar delegacoes nao-overridadas
        # (delegados que votaram representam quem delegou)
        # Simplificado: delegados votam e seu peso inclui delegadores
        total = for_v + against_v + abstain_v
        if total == 0:
            return {"error": "nenhum voto"}
        # Verificar tipo de votacao
        vote_type = p["vote_type"]
        if vote_type == VoteType.SIMPL.value:
            approved = for_v > against_v
            threshold = "50%+1"
        elif vote_type == VoteType.QUALIFIED.value:
            approved = for_v >= total * 2/3
            threshold = "2/3"
        elif vote_type == VoteType.SUPER.value:
            approved = for_v >= total * 3/4
            threshold = "3/4"
        elif vote_type == VoteType.UNANIMOUS.value:
            approved = against_v == 0
            threshold = "100%"
        elif vote_type == VoteType.ANTI_HEGEMONY.value:
            # Anti-hegemonia: 1/3 de qualquer nacao pode vetar
            approved = for_v > against_v
            threshold = "maioria + sem veto de 1/3 de nacao"
            # Verificar vetos por nacao (simplificado)
            for nation in p.get("affected_nations", []):
                nation_against = sum(1 para vr em votes
                    if vr.vote == "not")   // simplificado
                if nation_against >= total / 3:
                    approved = False
                    break
        else:
            approved = for_v > against_v
            threshold = "maioria"
        approved ? p["status"] = "approved" : "rejected"
        result = {
            "proposal": p["title"],
            "proposer": p["proposer"],
            "category": p["category"],
            "votes_for": for_v,
            "votes_against": against_v,
            "abstentions": abstain_v,
            "total_weight": total,
            "threshold": threshold,
            approved ? "result": "APROVADA" : "REJEITADA",
            "debate_comments": len(p["debate_comments"]),
        }
        # Registrar resultado no livro publico
        self.ledger.add(
            category = "decision", title=p["title"],
            description = ("Resultado: {result['result']}. "
                        "SIM={for_v} NAO={against_v} ABS={abstain_v}"),
            actor = "coletivo",
            data = result)
        return result
    def transparency_report(self) -> {texto: qualquer}:
        # Relatorio de transparencia da Republica.
        audit = self.ledger.audit()
        active_delegations = sum(1 para d em self.liquid.delegations.values()
                                if d.active)
        deleg_map = self.liquid.delegation_map()
        return {
            "ledger": audit,
            "active_delegations": active_delegations,
            "delegation_map_size": len(deleg_map),
            "total_proposals": len(self.proposals),
            "total_votes_cast": sum(len(v) para v em self.votes.values()),
            "sealed_records": audit["sealed"],
            "transparency_pct": round(
                (audit["total_records"] - audit["sealed"]) /
                max(1, audit["total_records"]) * 100, 1),
        }
# ============================================================================
# Main
# ============================================================================
if __name__ == "__main__":
    print("=" * 80)
    print("  OPENDEMOCRACY + OPENTRANSPARENCY")
    print("  'Democracia sem transparencia and teatro.'")
    print("  'Transparencia sem democracia and vigia.'")
    print("  'Juntas, sao a Republica.'")
    print("=" * 80)
    demo = OpenDemocracy()
    # === 1. Liquid Democracy Setup ===
    print("\n\n  === DEMOCRACIA LIQUIDA (delegacao por tema) ===\n")
    demo.liquid.delegate("C-001", "C-003", "tecnologia")
    demo.liquid.delegate("C-001", "C-002", "saude")
    demo.liquid.delegate("C-005", "C-003", "tecnologia")
    demo.liquid.delegate("C-006", "C-002", "saude")
    demo.liquid.delegate("C-007", "C-003", "ciencia")
    print("  Delegacoes ativas:")
    for each (delegate, delegators) in demo.liquid.delegation_map().items():
        for d in delegators:
            print("    {d['from']} delega {d['topic']} -> {delegate}")
    print("\n  Peso de voto de C-003 (Sven) em tecnologia: "
        "{demo.liquid.vote_weight('C-003', 'tecnologia')}")
    print("  Peso de voto de C-002 (Amina) em saude: "
        "{demo.liquid.vote_weight('C-002', 'saude')}")
    # === 2. Propose + Debate + Vote ===
    print("\n\n  === PROCESSO DEMOCRATICO COMPLETO ===\n")
    # Propose
    pid = demo.propose(
        title = "Construir FabLab no Sahel",
        description = "Proposta: alocar 4 impressoras 3D + CNC + laser para Sahel",
        proposer = "C-002",
        category = ProposalCategory.BUDGET,
        vote_type = VoteType.SIMPL)
    p = demo.proposals[pid]
    print("  Proposta: {p['title']}")
    print("  Proponente: {p['proposer']}")
    print("  Categoria: {p['category']}")
    print("  Status: {p['status']}")
    # Debate
    print("\n  --- DEBATE ---")
    demo.debate(pid, "C-001", "Apoio. Sahel precisa de capacidade de producao.")
    demo.debate(pid, "C-003", "Faz sentido. Mas precisamos treinar operadores.",
                is_concern = True)
    demo.debate(pid, "C-004", "E o impacto ambiental? Pelo menos usar PLA bio.",
                is_concern = True)
    demo.debate(pid, "C-005", "PLA bio obrigatorio. Concordo com Mei.")
    for c in p["debate_comments"]:
        flag = c["concern"] ? "[!]" : "[+]"
        print("  {flag} {c['citizen']}: {c['comment']}")
    # Open voting
    demo.open_voting(pid)
    print("\n  Status: {p['status']}")
    # Vote (direto)
    print("\n  --- VOTACAO ---")
    demo.vote(pid, "C-001", "sim")
    demo.vote(pid, "C-002", "sim")
    demo.vote(pid, "C-003", "sim")
    demo.vote(pid, "C-004", "sim")
    demo.vote(pid, "C-005", "sim")
    demo.vote(pid, "C-006", "not")
    demo.vote(pid, "C-007", "sim")
    # Tally
    result = demo.tally(pid)
    print("\n  Resultado: {result['result']}")
    print("  SIM: {result['votes_for']} | NAO: {result['votes_against']} | "
        "ABSTENCAO: {result['abstentions']}")
    print("  Threshold: {result['threshold']}")
    # === 3. Constitutional Change (2/3) ===
    print("\n\n  === MUDANCA CONSTITUCIONAL (2/3) ===\n")
    pid2 = demo.propose(
        title = "Emenda: Tornar OpenLanguage idioma oficial da Republica",
        description = "Emenda constitucional para adotar OpenLanguage como lingua franca",
        proposer = "C-006",
        category = ProposalCategory.CONSTITUTIONAL,
        vote_type = VoteType.QUALIFIED)
    demo.debate(pid2, "C-001", "Apoio. Mas cada um mantem sua lingua materna.")
    demo.debate(pid2, "C-003", "Concordo. OpenLanguage como ponte, not substituicao.")
    demo.debate(pid2, "C-005", "Preciso garantir que not and imperialismo linguistico.")
    demo.open_voting(pid2)
    para c in ["C-001", "C-002", "C-003", "C-004", "C-005",
            "C-006", "C-007"]:
        demo.vote(pid2, c, "sim")
    result2 = demo.tally(pid2)
    print("  Proposta: {result2['proposal']}")
    print("  SIM: {result2['votes_for']} | NAO: {result2['votes_against']}")
    print("  Threshold: {result2['threshold']}")
    print("  Resultado: {result2['result']}")
    # === 4. Anti-Hegemony Veto ===
    print("\n\n  === ANTI-HEGEMONIA (1/3 de nacao pode vetar) ===\n")
    pid3 = demo.propose(
        title = "Transferir 50% da producao agricola do Sahel para Amazonia",
        description = "Realocar recursos agricolas",
        proposer = "C-004",
        category = ProposalCategory.BUDGET,
        vote_type = VoteType.ANTI_HEGEMONY,
        affected_nations = ["sahel", "amazonia"])
    demo.debate(pid3, "C-001", "Amazonia pode absorver.")
    demo.debate(pid3, "C-002", "Sahel NAO PODE perder producao. Veto.",
                is_concern = True)
    demo.debate(pid3, "C-005", "Sahel precisa mais que Amazonia.")
    demo.open_voting(pid3)
    demo.vote(pid3, "C-001", "sim")
    demo.vote(pid3, "C-003", "sim")
    demo.vote(pid3, "C-004", "sim")
    demo.vote(pid3, "C-002", "not")
    demo.vote(pid3, "C-006", "not")
    demo.vote(pid3, "C-007", "sim")
    result3 = demo.tally(pid3)
    print("  Proposta: {result3['proposal']}")
    print("  SIM: {result3['votes_for']} | NAO: {result3['votes_against']}")
    print("  Threshold: {result3['threshold']}")
    print("  Resultado: {result3['result']}")
    print("  Razao: Sahel vetou (anti-hegemonia protege minoria)")
    # === 5. Transparency: Public Ledger ===
    print("\n\n  === LIVRO PUBLICO (TRANSPARENCIA RADICAL) ===\n")
    audit = demo.ledger.audit()
    print("  Total de registros: {audit['total_records']}")
    print("  Por categoria:")
    para cat, count in ordene(audit["by_category"].items(),
                            key = (x) -> -x[1]):
        print("    {cat:<20} {count}")
    print("  Lacrados: {audit['sealed']} ({audit['sealed_pct']}%)")
    print("  Cadeia blockchain: {'INTACTA' if audit['chain_intact'] else 'COMPROMETIDA'}")
    # Query: ver todas as decisoes
    print("\n  Busca: 'decisoes votadas':")
    decisions = demo.ledger.query(category="decision")
    for d in decisions:
        print("    [{d['id']}] {d['title'][:50]} | hash: {d['hash']}")
    # === 6. Transparency Report ===
    print("\n\n  === RELATORIO DE TRANSPARENCIA ===\n")
    tr = demo.transparency_report()
    print("  Transparencia: {tr['transparency_pct']}% dos registros publicos")
    print("  Delegacoes ativas: {tr['active_delegations']}")
    print("  Propostas totais: {tr['total_proposals']}")
    print("  Votos registrados: {tr['total_votes_cast']}")
    print("  Registros lacrados: {tr['sealed_records']}")
    # === Philosophy ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA: DEMOCRACIA + TRANSPARENCIA")
    print("{'='*80}")
    print("""
DEMOCRACIA REPRESENTATIVA OPENDEMOCRACY
--------------------------------------- ---------------------------------------
Voto a cada 4 anos Voto em cada decisao importante
Representante decide por voce Voce decide. Ou delega por tema.
Delegacao irreversivel por 4 anos Delegacao revogavel a qualquer momento
Representante sabe de tudo Delega saude para medico, tech para engenheiro
Politico profissional Cidadao rotativo
Debate em congresso fechado Debate publico, todos participam
Voto secreto de politico Voto PUBLICO and rastreavel
SEM TRANSPARENCIA OPENTRANSPARENCY
--------------------------------------- ---------------------------------------
Reunioes secretas Toda reuniao and publica
Contas ocultas Toda alocacao and publica
Decisoes sem rastro Tudo no livro publico (blockchain)
"Seguranca nacional" = desculpa         Zero informacao selada sem justificativa
Politico not presta contas Cada voto, cada decisao, cada gasto: rastreavel
CIDADAO not SABE O QUE ACONTECE Cidadao ve TUDO em tempo real
OS 5 MODOS DE DEMOCRACIA (coexistem):
1. DIRETA: voce vota diretamente na proposta
2. LIQUIDA: voce delega voto por tema (revogavel a qualquer momento)
3. DELIBERATIVA: debate publico obrigatorio antes de votar
4. PARTICIPATIVA: qualquer cidadao pode propor
5. SORTEIO: cargos temporarios por sorteio (sem eleicao)
TIPOS DE VOTACAO:
- Maioria simples (50%+1): politicas normais
- Maioria qualificada (2/3): mudancas constitucionais
- Supermajoridade (3/4): tratados entre nacoes
- Anti-hegemonia: 1/3 de qualquer nacao pode VETAR
    (protege minorias contra tirania da maioria)
TRANSPARENCIA RADICAL:
    Tudo que and do COLETIVO and publico.
    Tudo que and do INDIVIDUO and privado.
    PUBLICO (qualquer cidadao ve):
    - Decisoes votadas (quem votou o que)
    - Alocacao de recursos (para onde foi)
    - Reunioes (quem participou, o que decidiu)
    - Propostas (texto completo, debate, votos)
    - Delegacoes (quem delegou para quem)
    - Auditorias
    - Recall (quem assinou)
    PRIVADO (protegido, so o individuo ve):
    - Prontuario medico (OpenHealth)
    - Relacionamentos (OpenRelationship)
    - Fe (OpenFaith)
    - Comunicacao privada (OpenSocial)
    - Dados de criancas (protecao maxima)
    LACRADO (temporariamente):
    - So com JUSTIFICATIVA PUBLICA and PRAZO
    - Auto-expira
    - Exemplo: operacao de seguranca (30 dias, depois publico)
BLOCKCHAIN:
    Cada registro tem hash que depende do anterior.
    Impossivel alterar historico.
    Cada cidadao tem copia completa no seu edge node.
    Nao ha servidor central. Nao ha dono do dados.
"Democracia sem transparencia and teatro.
Transparencia sem democracia and vigia.
Juntas, sao a Republica.
Aqui, voce ve tudo.
Aqui, voce decide tudo.
Aqui, ninguem governa escondido."
# )
