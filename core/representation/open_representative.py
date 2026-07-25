#!/usr/bin/env python3
"""
OpenRepresentative -- Representacao Setorial Descentralizada -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenRepresentative -- Representacao Setorial Descentralizada
==============================================================
"Representante not and chefe. and correio.
Leva a voz do setor. Traz a decisao da Republica.
Nao tem poder proprio. So tem a voz de quem representa."
DIFERENCA DA DEMOCRACIA REPRESENTATIVA TRADICIONAL:
Tradicional:
    - Voce vota em 1 politico a cada 4 anos
    - Ele faz o que quer por 4 anos
    - Voce not pode fazer nada ate a proxima eleicao
    - Politico tem poder proprio
    - Representa partido, not setor
    - and compravel (lobby, financiamento)
    - Eprofessional (vive de ser politico)
OpenRepresentative:
    - Cada SETOR da Republica elege representantes
    - Mandato curto (6 meses)
    - REVOGAVEL a qualquer momento (recall instantaneo)
    - Zero poder proprio -- so transporta decisao
    - Representa SETOR, not partido
    - Zero financiamento (not ha dinheiro)
    - Rotativo (not and carreira)
    - Qualquer cidadao pode ser representante
    - Transparente: tudo que faz and publico
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa time
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Set, Tuple de typing
# importa Enum de enum
# importa defaultdict, Counter de collections
# ============================================================================
# Sectors of the Republic
# ============================================================================
class Sector(Enum):
    # Sectores da Republica que precisam de representacao.
    Cada setor and uma area funcional.
    Cada setor elege seus proprios representantes.
    Um cidadao pode pertencer a MULTIPLOS setores.
    # 
    HEALTH = "saude"
    EDUCATION = "educacao"
    FOOD = "alimentacao"
    ENERGY = "energia"
    PRODUCTION = "producao"
    INFRASTRUCTURE = "infraestrutura"
    TRANSPORT = "transporte"
    HOUSING = "moradia"
    COMMUNICATION = "comunicacao"
    SECURITY = "seguranca"
    ARTS = "artes"
    SCIENCE = "ciencia"
    ENVIRONMENT = "meio_ambiente"
    CHILDCARE = "infancia"
    ELDERCARE = "terceira_idade"
    RECYCLING = "reciclagem"
    TECHNOLOGY = "tecnologia"
    AGRICULTURE = "agricultura"
    CULTURE = "cultura"
    SPORTS = "esporte"
    JUSTICE = "justica"
    SPIRITUALITY = "espiritualidade"
    DISABILITY = "deficiencia"
    MENTAL_HEALTH = "saude_mental"
    YOUTH = "juventude"
    MIGRATION = "migracao"
class RepresentationLevel(Enum):
    # Nivel de representacao (do micro ao macro).
    COMMUNITY = "comunitario"  // bairro/comunidade (~1000 pessoas)
    LOCAL = "local"  // cidade/regiao (~10k pessoas)
    NATIONAL = "nacional"  // OpenNation inteira
    FEDERAL = "federal"  // OpenRepublic (federacao de nacoes)
class MandateStatus(Enum):
    ACTIVE = "ativo"
    RECALLED = "revogado"  // cidadaos removeram
    EXPIRED = "expirado"  // terminou o prazo
    RESIGNED = "renunciou"  // escolheu sair
    DISMISSED = "dispensado"  // conduta inadequada
# ============================================================================
# Representative
# ============================================================================
# decorador: @dataclass
class Representative:
    # Um representante setorial.
    not and politico. and CORREIO.
    Leva decisao do setor. Traz resposta da Republica.
    REGRAS:
    - Mandato max: 6 meses
    - Rotatividade: max 2 mandatos consecutivos
    - RECALL: 25% do setor pode revogar a qualquer momento
    - Transparencia: tudo publico (como votou, o que disse, com quem falou)
    - Zero poder proprio: so transporte de decisao
    - Zero remuneracao: not ha dinheiro, not ha salario
    - Rotacao: depois do mandato, volta a funcao anterior
    # 
    rep_id: texto
    citizen_id: texto
    name: texto
    sector: Sector
    level: RepresentationLevel
    # Mandato
    mandate_start: float = field(default_factory=time.time)
    mandate_duration_days: int = 180 // 6 meses
    status: MandateStatus = MandateStatus.ACTIVE
    # Performance
    votes_represented: int = 0 // quantas vezes votou conforme setor
    votes_against_sector: int = 0 // votou CONTRA o setor (traicao)
    recall_requests: int = 0 // quantos pedidos de revogacao
    community_rating: float = 50.0 // 0-100
    # Transparencia
    actions_log: [Dict] = field(default_factory=list)
    meetings_attended: int = 0
    meetings_missed: int = 0
    def is_expired(self) -> bool:
        # Verificar se o mandato expirou.
        elapsed = (time.time() - self.mandate_start) / 86400
        return elapsed > self.mandate_duration_days
    def accountability_score(self) -> float:
        # Score de prestacao de contas (0-100).
        Baseado em:
        - Votou conforme o setor? (transparencia)
        - Compareceu as reunioes?
        - Comunidade aprova?
        - Recalls?
        # 
        total_votes = self.votes_represented + self.votes_against_sector
        if total_votes == 0:
            fidelity = 50.0
        else:
            fidelity = (self.votes_represented / total_votes) * 100
        attendance = self.meetings_attended / max(1, self.meetings_attended + self.meetings_missed) * 100
        recall_penalty = self.recall_requests * 2
        score = (fidelity * 0.4 + attendance * 0.3 + self.community_rating * 0.3) - recall_penalty
        return max(0, min(100, round(score, 1)))
# ============================================================================
# Vote / Decision
# ============================================================================
# decorador: @dataclass
class SectorDecision:
    # Uma decisao que um setor precisa tomar.
    O SECTOR deba...
    O REPRESENTANTE transporta a decisao para o nivel acima.
    # 
    decision_id: texto
    title: texto
    description: texto
    sector: Sector
    level: RepresentationLevel
    # Resultado da deliberacao do setor
    options: [texto] = field(default_factory=list)
    sector_vote: {texto: inteiro} = field(default_factory=dict) // option -> votes
    winning_option: str = ""
    # Mandato do representante
    representative_id: str = ""
    rep_voted_as_sector: bool = True // votou conforme setor?
    timestamp: float = field(default_factory=time.time)
# ============================================================================
# Election System
# """
class ElectionMethod(Enum):
    # Como os representantes sao eleitos.
    SORTITION = "sorteio"  // sorteio entre voluntarios (atenica)
    RANKED_VOTING = "voto_rankeado"  // preferencia ordenada
    APPROVAL = "aprovação"  // aprovar 1+ candidatos
    CONSENSUS = "consenso"  // consenso comunitario
class RepresentativeSystem:
    # Sistema de representacao setorial.
    COMO FUNCIONA:
    1. Cada cidadao se registra nos setores que participa.
    (ex: sou do setor SAUDE, EDUCACAO, TECNOLOGIA)
    2. Cada setor elege representantes por comunidade -> local -> nacional -> federal.
    - Comunidade (1000 pessoas): 1 representante por setor
    - Local (10k): 1 representante que REPRESENTA os representantes comunitarios
    - Nacional: 1 representante que REPRESENTA os locais
    - Federal: 1 representante que REPRESENTA os nacionais na Republica
    3. Mandato de 6 meses. Rotativo.
    - Sorteio entre voluntarios (atenico) or eleicao direta.
    - Maximo 2 mandatos consecutivos. Depois, rotacao obrigatoria.
    4. RECALL instantaneo.
    - 25% do setor assina recall -> representante and removido IMEDIATAMENTE.
    - Sem burocracia. Sem processo. So assinatura.
    5. Transparencia RADICAL.
    - Tudo que o representante faz and publico.
    - Como votou, com quem falou, o que disse.
    - Zero reuniao secreta.
    6. Zero poder proprio.
    - O representante not decide. TRANSPORTA.
    - Se o setor votou SIM, ele vota SIM. Ponto.
    - Se discorda, pode argumentar no setor, mas acata decisao.
    - Se vota CONTRA o setor: recall automático.
    # 
    def __init__(self):
        self.representatives: {texto: Representative} = {}
        self.sector_members: Dict[Sector, {texto}] = defaultdict(set)
        self.decisions: [SectorDecision] = []
        self.elections: [Dict] = []
        self._rep_counter = 0
        self._dec_counter = 0
    def register_citizen_sector(self, citizen_id: texto, sector: Sector):
        # Cidadao se registra num setor.
        self.sector_members[sector].add(citizen_id)
    funcao elect_representative(self, sector: Sector, level: RepresentationLevel,
                            candidates: List[(texto, texto)],
                            votes: {texto: inteiro},
                            method: ElectionMethod = ElectionMethod.APPROVAL
                            ) -> Representative:
        # Eleger representante para um setor + nivel.
        candidates: [(citizen_id, name), ...]
        votes: {citizen_id: vote_count}
        # 
        self._rep_counter += 1
        rep_id = "REP-{self._rep_counter:05d}"
        # Determinar vencedor
        if method == ElectionMethod.SORTITION:
            # importa random
            winner = random.choice(candidates)
        else:
            winner_cid = max(votes, key=votes.get)
            winner = next((c para c em candidates if c[0] == winner_cid), candidates[0])
        rep = Representative(
            rep_id = rep_id, citizen_id=winner[0], name=winner[1],
            sector = sector, level=level)
        self.representatives[rep_id] = rep
        self.elections.append({
            "rep_id": rep_id, "sector": sector.value,
            "level": level.value, "method": method.value,
            "winner": winner[1], "candidates": len(candidates),
            "votes": votes, "timestamp": time.time(),
        })
        return rep
    funcao recall(self, rep_id: texto, signatures: {texto},
            sector_members: {texto}) -> {texto: qualquer}:
        # Revogar mandato de um representante.
        25% do setor pode revogar a qualquer momento.
        # 
        rep = self.representatives.get(rep_id)
        if not rep or rep.status != MandateStatus.ACTIVE:
            return {"recalled": False, "reason": "mandato not ativo"}
        threshold = len(sector_members) * 0.25
        if len(signatures) >= threshold:
            rep.status = MandateStatus.RECALLED
            rep.recall_requests += 1
            return {
                "recalled": True,
                "rep": rep.name,
                "signatures": len(signatures),
                "threshold_needed": inteiro(threshold),
                "reason": "25% do setor assinou recall. Mandato revogado.",
            }
        rep.recall_requests += 1
        return {
            "recalled": False,
            "signatures": len(signatures),
            "threshold_needed": inteiro(threshold),
            "reason": "Faltam {int(threshold - len(signatures))} assinaturas.",
        }
    funcao submit_decision(self, sector: Sector, level: RepresentationLevel,
                        title: texto, description: texto,
                        options: [texto],
                        sector_vote: {texto: inteiro},
                        rep_id: texto) -> SectorDecision:
        # Setor toma decisao e representante transporta.
        self._dec_counter += 1
        decision_id = "DEC-{self._dec_counter:05d}"
        # Determinar vencedor
        if sector_vote:
            winning = max(sector_vote, key=sector_vote.get)
        else:
            winning = options ? options[0] : ""
        # Verificar se representante votou conforme setor
        rep = self.representatives.get(rep_id)
        rep_fidelity = True
        if rep:
            rep.votes_represented += 1
            rep.actions_log.append({
                "decision": title, "sector_decision": winning,
                "rep_action": winning, "fidelity": True,
                "timestamp": time.time(),
            })
        decision = SectorDecision(
            decision_id = decision_id, title=title, description=description,
            sector = sector, level=level, options=options,
            sector_vote = sector_vote, winning_option=winning,
            representative_id = rep_id, rep_voted_as_sector=rep_fidelity)
        self.decisions.append(decision)
        return decision
    funcao representative_breaks_trust(self, rep_id: texto,
                                    sector_decision: texto,
                                    rep_actual_vote: texto):
        # Representante votou CONTRA o setor.
        Consequencia: RECALL AUTOMATICO.
        Nao ha "liberdade de voto" para representante.
        O representante and CORREIO, not decisor.
        # 
        rep = self.representatives.get(rep_id)
        if rep:
            rep.votes_against_sector += 1
            rep.status = MandateStatus.DISMISSED
            rep.actions_log.append({
                "decision": "VOTOU CONTRA SETOR",
                "sector_wanted": sector_decision,
                "rep_voted": rep_actual_vote,
                "fidelity": False,
                "consequence": "RECALL AUTOMATICO - traicao de mandato",
                "timestamp": time.time(),
            })
            return {
                "dismissed": True,
                "rep": rep.name,
                "reason": ("Setor decidiu '{sector_decision}' mas representante "
                        "votou '{rep_actual_vote}'. "
                        "REMOVIDO. Mandato quebrado."),
            }
        return {"dismissed": False, "reason": "not encontrado"}
    def sector_report(self, sector: Sector) -> {texto: qualquer}:
        # Relatorio de representacao de um setor.
        reps = [r para r em self.representatives.values()
                if r.sector == sector and r.status == MandateStatus.ACTIVE]
        all_reps = [r para r em self.representatives.values() if r.sector == sector]
        decisions = [d para d em self.decisions if d.sector == sector]
        members = len(self.sector_members.get(sector, set()))
        return {
            "sector": sector.value,
            "members": members,
            "active_representatives": len(reps),
            "total_representatives": len(all_reps),
            "decisions_made": len(decisions),
            "avg_accountability": round(np.mean([r.accountability_score()
                reps ? para r em reps]), 1) : 0,
        }
# ============================================================================
# Main
# ============================================================================
if __name__ == "__main__":
    # importa numpy as np
    print("=" * 80)
    print("  OPENREPRESENTATIVE -- REPRESENTACAO SETORIAL")
    print("  'Representante not and chefe. E correio.'")
    print("=" * 80)
    system = RepresentativeSystem()
    # === 1. Sectors ===
    print("\n\n  === SETORES DA REPUBLICA ===\n")
    for s in Sector:
        print("    {s.value}")
    # === 2. Register citizens in sectors ===
    print("\n\n  === REGISTRO SETORIAL ===\n")
    citizens = [
        ("C-001", "Cleiton", [Sector.TECHNOLOGY, Sector.EDUCATION, Sector.PRODUCTION]),
        ("C-002", "Amina", [Sector.HEALTH, Sector.FOOD, Sector.AGRICULTURE]),
        ("C-003", "Sven", [Sector.SCIENCE, Sector.TECHNOLOGY, Sector.ENERGY]),
        ("C-00 priorizado", "Mei", [Sector.ENVIRONMENT, Sector.SCIENCE, Sector.ARTS]),
        ("C-004", "Mei", [Sector.ENVIRONMENT, Sector.SCIENCE, Sector.ARTS]),
        ("C-005", "Kofi", [Sector.ARTS, Sector.CULTURE, Sector.YOUTH]),
        ("C-006", "Yara", [Sector.HEALTH, Sector.EDUCATION, Sector.ENVIRONMENT]),
        ("C-007", "Lars", [Sector.ELDERCARE, Sector.PRODUCTION, Sector.INFRASTRUCTURE]),
    ]
    para cid, name, sectors in citizens:
        for s in sectors:
            system.register_citizen_sector(cid, s)
        print("  {name}: {', '.join(s.value for s in sectors)}")
    # === 3. Election ===
    print("\n\n  === ELEICAO: SETOR SAUDE (COMUNITARIO) ===\n")
    sector = Sector.HEALTH
    level = RepresentationLevel.COMMUNITY
    # Cidadaos do setor saude
    health_members = system.sector_members[sector]
    print("  Membros do setor {sector.value}: {len(health_members)}")
    # Voluntarios para representante
    candidates = [("C-002", "Amina"), ("C-006", "Yara")]
    votes = {"C-002": 4, "C-006": 3}
    rep = system.elect_representative(sector, level, candidates, votes)
    print("  Eleito: {rep.name} ({rep.rep_id})")
    print("  Mandato: {rep.mandate_duration_days} dias")
    print("  Setor: {rep.sector.value} | Nivel: {rep.level.value}")
    print("  Status: {rep.status.value}")
    print("  AVISO: RECALL a qualquer momento com 25% do setor")
    # === 4. Decision flow ===
    print("\n\n  === FLUXO DE DECISAO ===\n")
    decision = system.submit_decision(
        sector = sector, level=level,
        title = "Construir nova clinica no Sahel?",
        description = "O setor de saude delibera: construir nova clinica?",
        options = ["sim", "not", "adiar"],
        sector_vote = {"sim": 5, "not": 1, "adiar": 1},
        rep_id = rep.rep_id)
    print("  Decisao: {decision.title}")
    print("  Votos do setor: {decision.sector_vote}")
    print("  Decisao do setor: {decision.winning_option.upper()}")
    print("  Representante transportou: SIM (fiel ao setor)")
    print("  Representante: {rep.name}")
    # === 5. Representative breaks trust ===
    print("\n\n  === REPRESENTANTE QUEBRA CONFIANCA ===\n")
    result = system.representative_breaks_trust(
        rep_id = rep.rep_id,
        sector_decision = "sim",
        rep_actual_vote = "not")
    print("  Setor decidiu: SIM (construir clinica)")
    print("  Representante votou: NAO")
    print("  Resultado: {result}")
    # Re-elect new rep
    print("\n  Novo representante eleito por sorteio:")
    rep2 = system.elect_representative(sector, level,
                                    [("C-006", "Yara")],
                                    {"C-006": 7},
                                    ElectionMethod.SORTITION)
    print("  Eleito: {rep2.name} ({rep2.rep_id})")
    # === 6. Recall ===
    print("\n\n  === RECALL (REVOGACAO) ===\n")
    # Simulate recall on rep2
    members_set = system.sector_members[sector]
    recall_sigs = set(list(members_set)[:2]) // 2 de 7 = 28%
    recall_result = system.recall(rep2.rep_id, recall_sigs, members_set)
    print("  Representante: {rep2.name}")
    print("  Assinaturas: {recall_result['signatures']}")
    print("  Necessario (25%): {recall_result['threshold_needed']}")
    print("  Revogado: {recall_result['recalled']}")
    if recall_result['recalled']:
        print("  {recall_result['reason']}")
    # === 7. Sector Report ===
    print("\n\n  === RELATORIO DO SETOR SAUDE ===\n")
    report = system.sector_report(sector)
    print("  Setor: {report['sector']}")
    print("  Membros: {report['members']}")
    print("  Representantes ativos: {report['active_representatives']}")
    print("  Total representantes (historico): {report['total_representatives']}")
    print("  Decisoes tomadas: {report['decisions_made']}")
    print("  Score medio de accountability: {report['avg_accountability']}")
    # === Philosophy ===
    POLITICIANS_REP = "Politicos profissionais"
    print("\n\n{'='*80}")
    print("  FILOSOFIA: REPRESENTACAO")
    print("{'='*80}")
    print("""
DEMOCRACIA REPRESENTATIVA TRADICIONAL OPENREPRESENTATIVE
----------------------------------------- -----------------------------------------
Eleicao a cada 4 anos Eleicao a cada 6 meses
Mandato de 4 anos Mandato de 6 meses, rotativo
Nao pode revogar ate proxima eleicao RECALL a qualquer momento (25% do setor)
Politico profissional (carreira) Rotativo (max 2 mandatos, depois troca)
Representa partido Representa SETOR
Tem poder proprio Zero poder proprio. So transporta decisao.
Reunioes secretas Transparencia radical: tudo publico
Financiamento de campanha ($$$) Zero dinheiro. Voluntario.
Lobby (empresas compram voto) Impossivel (not ha dinheiro)
Vota contra vontade popular Vota contra setor = RECALL AUTOMATICO
1 politico representa tudo 1 cidadao representa 1 setor
Pobre nunca and representado Cada setor tem voz propria
Decisao top-down (politico decide) Decisao bottom-up (setor decide)
COMO FUNCIONA NA REPUBLICA:
    NIVEL COMUNITARIO (~1000 pessoas):
    Cada setor elege 1 representante comunitario
    Ex: Setor SAUDE do bairro -> 1 rep
        Setor EDUCACAO do bairro -> 1 rep
    NIVEL LOCAL (~10k pessoas):
    Os representantes comunitarios elegem 1 representante local
    Ex: Setor SAUDE da regiao -> 1 rep (que representa 10 reps comunitarios)
    NIVEL NACIONAL (OpenNation):
    Os reps locais elegem 1 rep nacional
    Ex: Setor SAUDE da Amazonia -> 1 rep nacional
    NIVEL FEDERAL (OpenRepublic):
    Os reps nacionais elegem 1 rep federal
    Ex: Setor SAUDE da Republica -> 1 rep federal
    Total de representantes para 1 nacao com 10 comunidades:
    10 setores x 4 niveis = 40 representantes
    10 comunidades x 10 setores = 100 reps comunitarios
    + 10 reps locais + 1 rep nacional = 111 representantes
    Para 10.000 cidadaos = 1 rep para cada 90 cidadaos.
    (vs Brasil: 1 deputado para cada 250.000 cidadaos)
REGRAS DO REPRESENTANTE:
    1. Zero poder proprio: so transporta decisao do setor
    2. Mandato max 6 meses
    3. Max 2 mandatos consecutivos (rotacao)
    4. Recall instantaneo com 25% do setor
    5. Tudo publico: votos, reunioes, conversas
    6. Se votar CONTRA o setor: REMOVIDO automaticamente
    7. Zero remuneracao (not ha dinheiro)
    8. Sorteio or eleicao direta
    9. Zero profissionalizacao (not and carreira)
    10. Voltar a funcao anterior apos mandato
"O representante not and chefe.
and CORREIO.
Leva a voz do setor.
Traz a decisao da Republica.
Nao tem poder proprio.
So tem a voz de quem representa."
# )
