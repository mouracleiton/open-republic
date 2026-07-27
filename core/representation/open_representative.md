# OpenRepresentative -- Representacao Setorial Descentralizada

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/representation/open_representative.py`

**Descricao:** ==============================================================
"Representante nao e chefe. E correio.
 Leva a voz do setor. Traz a decisao da Republica.
 Nao tem poder proprio. So tem a voz de quem representa."
DIFERENCA DA DEMOCRACIA REPRESENTATIVA TRADICIONAL:
  Tradicional:
    - Voce vota em 1 politico a cada 4 anos
    - Ele faz o que quer por 4 anos
    - Voce nao pode fazer nada ate a proxima eleicao
    - Politico tem poder proprio
    - Representa partido, nao setor
    - E compravel (lobby, financiamento)
    - Eprofessional (vive de ser politico)
  OpenRepresentative:
    - Cada SETOR da Republica elege representantes
    - Mandato curto (6 meses)
    - REVOGAVEL a qualquer momento (recall instantaneo)
    - Zero poder proprio -- so transporta decisao
    - Representa SETOR, nao partido
    - Zero financiamento (nao ha dinheiro)
    - Rotativo (nao e carreira)
    - Qualquer cidadao pode ser representante
    - Transparente: tudo que faz e publico
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepresentative -- Representacao Setorial Descentralizada
==============================================================

"Representante nao e chefe. e correio.
 Leva a voz do setor. Traz a decisao da Republica.
 Nao tem poder proprio. So tem a voz de quem representa."

DIFERENCA DA DEMOCRACIA REPRESENTATIVA TRADICIONAL:

  Tradicional:
    - Voce vota em 1 politico a cada 4 anos
    - Ele faz o que quer por 4 anos
    - Voce nao pode fazer nada ate a proxima eleicao
    - Politico tem poder proprio
    - Representa partido, nao setor
    - e compravel (lobby, financiamento)
    - Eprofessional (vive de ser politico)

  OpenRepresentative:
    - Cada SETOR da Republica elege representantes
    - Mandato curto (6 meses)
    - REVOGAVEL a qualquer momento (recall instantaneo)
    - Zero poder proprio -- so transporta decisao
    - Representa SETOR, nao partido
    - Zero financiamento (nao ha dinheiro)
    - Rotativo (nao e carreira)
    - Qualquer cidadao pode ser representante
    - Transparente: tudo que faz e publico

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Set, Tuple de typing
// importa Enum de enum
// importa defaultdict, Counter de collections


// ============================================================================
// Sectors of the Republic
// ============================================================================

classe Sector herda de Enum:
    // Sectores da Republica que precisam de representacao.

    Cada setor e uma area funcional.
    Cada setor elege seus proprios representantes.
    Um cidadao pode pertencer a MULTIPLOS setores.
    // 
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


classe RepresentationLevel herda de Enum:
    // Nivel de representacao (do micro ao macro).
    COMMUNITY = "comunitario"  // bairro/comunidade (~1000 pessoas)
    LOCAL = "local"  // cidade/regiao (~10k pessoas)
    NATIONAL = "nacional"  // OpenNation inteira
    FEDERAL = "federal"  // OpenRepublic (federacao de nacoes)


classe MandateStatus herda de Enum:
    ACTIVE = "ativo"
    RECALLED = "revogado"  // cidadaos removeram
    EXPIRED = "expirado"  // terminou o prazo
    RESIGNED = "renunciou"  // escolheu sair
    DISMISSED = "dispensado"  // conduta inadequada


// ============================================================================
// Representative
// ============================================================================

// decorador: @dataclass
classe Representative:
    // Um representante setorial.

    nao e politico. e CORREIO.
    Leva decisao do setor. Traz resposta da Republica.

    REGRAS:
    - Mandato maximo: 6 meses
    - Rotatividade: maximo 2 mandatos consecutivos
    - RECALL: 25% do setor pode revogar a qualquer momento
    - Transparencia: tudo publico (como votou, o que disse, com quem falou)
    - Zero poder proprio: so transporte de decisao
    - Zero remuneracao: nao ha dinheiro, nao ha salario
    - Rotacao: depois do mandato, volta a funcao anterior
    // 
    rep_id: texto
    citizen_id: texto
    name: texto
    sector: Sector
    level: RepresentationLevel
    // Mandato
    seja mandate_start: flutuante = field(default_factory=time.time)
    seja mandate_duration_days: inteiro = 180 // 6 meses
    seja status: MandateStatus = MandateStatus.ACTIVE
    // Performance
    seja votes_represented: inteiro = 0 // quantas vezes votou conforme setor
    seja votes_against_sector: inteiro = 0 // votou CONTRA o setor (traicao)
    seja recall_requests: inteiro = 0 // quantos pedidos de revogacao
    seja community_rating: flutuante = 50.0 // 0-100
    // Transparencia
    seja actions_log: [Dict] = field(default_factory=list)
    seja meetings_attended: inteiro = 0
    seja meetings_missed: inteiro = 0

    funcao is_expired(self) -> logico:
        // Verificar se o mandato expirou.
        elapsed = (time.time() - self.mandate_start) / 86400
        retorne elapsed > self.mandate_duration_days

    funcao accountability_score(self) -> flutuante:
        // Score de prestacao de contas (0-100).

        Baseado em:
        - Votou conforme o setor? (transparencia)
        - Compareceu as reunioes?
        - Comunidade aprova?
        - Recalls?
        // 
        total_votes = self.votes_represented + self.votes_against_sector
        se total_votes == 0 entao:
            fidelity = 50.0
        senao:
            fidelity = (self.votes_represented / total_votes) * 100

        attendance = self.meetings_attended / maximo(1, self.meetings_attended + self.meetings_missed) * 100
        recall_penalty = self.recall_requests * 2

        score = (fidelity * 0.4 + attendance * 0.3 + self.community_rating * 0.3) - recall_penalty
        retorne maximo(0, minimo(100, arredonde(score, 1)))


// ============================================================================
// Vote / Decision
// ============================================================================

// decorador: @dataclass
classe SectorDecision:
    // Uma decisao que um setor precisa tomar.

    O SECTOR deba...
    O REPRESENTANTE transporta a decisao para o nivel acima.
    // 
    decision_id: texto
    title: texto
    description: texto
    sector: Sector
    level: RepresentationLevel
    // Resultado da deliberacao do setor
    seja options: [texto] = field(default_factory=list)
    seja sector_vote: {texto: inteiro} = field(default_factory=dict) // option -> votes
    seja winning_option: texto = ""
    // Mandato do representante
    seja representative_id: texto = ""
    seja rep_voted_as_sector: logico = verdadeiro // votou conforme setor?
    seja timestamp: flutuante = field(default_factory=time.time)


// ============================================================================
// Election System
// """

classe ElectionMethod herda de Enum:
    // Como os representantes sao eleitos.
    SORTITION = "sorteio"  // sorteio entre voluntarios (atenica)
    RANKED_VOTING = "voto_rankeado"  // preferencia ordenada
    APPROVAL = "aprovação"  // aprovar 1+ candidatos
    CONSENSUS = "consenso"  // consenso comunitario


classe RepresentativeSystem:
    // Sistema de representacao setorial.

    COMO FUNCIONA:

    1. Cada cidadao se registra nos setores que participa.
       (ex: sou do setor SAUDE, EDUCACAO, TECNOLOGIA)

    2. Cada setor elege representantes por comunidade -> local -> nacional -> federal.
       - Comunidade (1000 pessoas): 1 representante por setor
       - Local (10k): 1 representante que REPRESENTA os representantes comunitarios
       - Nacional: 1 representante que REPRESENTA os locais
       - Federal: 1 representante que REPRESENTA os nacionais na Republica

    3. Mandato de 6 meses. Rotativo.
       - Sorteio entre voluntarios (atenico) ou eleicao direta.
       - Maximo 2 mandatos consecutivos. Depois, rotacao obrigatoria.

    4. RECALL instantaneo.
       - 25% do setor assina recall -> representante e removido IMEDIATAMENTE.
       - Sem burocracia. Sem processo. So assinatura.

    5. Transparencia RADICAL.
       - Tudo que o representante faz e publico.
       - Como votou, com quem falou, o que disse.
       - Zero reuniao secreta.

    6. Zero poder proprio.
       - O representante nao decide. TRANSPORTA.
       - Se o setor votou SIM, ele vota SIM. Ponto.
       - Se discorda, pode argumentar no setor, mas acata decisao.
       - Se vota CONTRA o setor: recall automático.
    // 

    funcao __init__(self):
        self.representatives: {texto: Representative} = {}
        self.sector_members: Dict[Sector, {texto}] = defaultdict(set)
        self.decisions: [SectorDecision] = []
        self.elections: [Dict] = []
        self._rep_counter = 0
        self._dec_counter = 0

    funcao register_citizen_sector(self, citizen_id: texto, sector: Sector):
        // Cidadao se registra num setor.
        self.sector_members[sector].add(citizen_id)

    funcao elect_representative(self, sector: Sector, level: RepresentationLevel,
                             candidates: List[(texto, texto)],
                             votes: {texto: inteiro},
                             seja method: ElectionMethod = ElectionMethod.APPROVAL
                             ) -> Representative:
        // Eleger representante para um setor + nivel.

        candidates: [(citizen_id, name), ...]
        votes: {citizen_id: vote_count}
        // 
        self._rep_counter += 1
        rep_id = "REP-{self._rep_counter:05d}"

        // Determinar vencedor
        se method == ElectionMethod.SORTITION entao:
            // importa random
            winner = random.choice(candidates)
        senao:
            winner_cid = maximo(votes, key=votes.get)
            winner = next((c para c em candidates if c[0] == winner_cid), candidates[0])

        rep = Representative(
            rep_id = rep_id, citizen_id=winner[0], name=winner[1],
            sector = sector, level=level)

        self.representatives[rep_id] = rep

        self.elections.append({
            "rep_id": rep_id, "sector": sector.value,
            "level": level.value, "method": method.value,
            "winner": winner[1], "candidates": tamanho(candidates),
            "votes": votes, "timestamp": time.time(),
        })

        retorne rep

    funcao recall(self, rep_id: texto, signatures: {texto},
               sector_members: {texto}) -> {texto: qualquer}:
        // Revogar mandato de um representante.

        25% do setor pode revogar a qualquer momento.
        // 
        rep = self.representatives.get(rep_id)
        se nao rep ou rep.status != MandateStatus.ACTIVE entao:
            retorne {"recalled": falso, "reason": "mandato nao ativo"}

        threshold = tamanho(sector_members) * 0.25
        se tamanho(signatures) >= threshold entao:
            rep.status = MandateStatus.RECALLED
            rep.recall_requests += 1
            retorne {
                "recalled": verdadeiro,
                "rep": rep.name,
                "signatures": tamanho(signatures),
                "threshold_needed": inteiro(threshold),
                "reason": "25% do setor assinou recall. Mandato revogado.",
            }

        rep.recall_requests += 1
        retorne {
            "recalled": falso,
            "signatures": tamanho(signatures),
            "threshold_needed": inteiro(threshold),
            "reason": "Faltam {int(threshold - len(signatures))} assinaturas.",
        }

    funcao submit_decision(self, sector: Sector, level: RepresentationLevel,
                        title: texto, description: texto,
                        options: [texto],
                        sector_vote: {texto: inteiro},
                        rep_id: texto) -> SectorDecision:
        // Setor toma decisao e representante transporta.
        self._dec_counter += 1
        decision_id = "DEC-{self._dec_counter:05d}"

        // Determinar vencedor
        se sector_vote entao:
            winning = maximo(sector_vote, key=sector_vote.get)
        senao:
            winning = options ? options[0] : ""

        // Verificar se representante votou conforme setor
        rep = self.representatives.get(rep_id)
        rep_fidelity = verdadeiro
        se rep entao:
            rep.votes_represented += 1
            rep.actions_log.append({
                "decision": title, "sector_decision": winning,
                "rep_action": winning, "fidelity": verdadeiro,
                "timestamp": time.time(),
            })

        decision = SectorDecision(
            decision_id = decision_id, title=title, description=description,
            sector = sector, level=level, options=options,
            sector_vote = sector_vote, winning_option=winning,
            representative_id = rep_id, rep_voted_as_sector=rep_fidelity)
        self.decisions.append(decision)
        retorne decision

    funcao representative_breaks_trust(self, rep_id: texto,
                                    sector_decision: texto,
                                    rep_actual_vote: texto):
        // Representante votou CONTRA o setor.

        Consequencia: RECALL AUTOMATICO.
        Nao ha "liberdade de voto" para representante.
        O representante e CORREIO, nao decisor.
        // 
        rep = self.representatives.get(rep_id)
        se rep entao:
            rep.votes_against_sector += 1
            rep.status = MandateStatus.DISMISSED
            rep.actions_log.append({
                "decision": "VOTOU CONTRA SETOR",
                "sector_wanted": sector_decision,
                "rep_voted": rep_actual_vote,
                "fidelity": falso,
                "consequence": "RECALL AUTOMATICO - traicao de mandato",
                "timestamp": time.time(),
            })
            retorne {
                "dismissed": verdadeiro,
                "rep": rep.name,
                "reason": ("Setor decidiu '{sector_decision}' mas representante "
                          "votou '{rep_actual_vote}'. "
                          "REMOVIDO. Mandato quebrado."),
            }
        retorne {"dismissed": falso, "reason": "nao encontrado"}

    funcao sector_report(self, sector: Sector) -> {texto: qualquer}:
        // Relatorio de representacao de um setor.
        reps = [r para r em self.representatives.values()
                if r.sector == sector e r.status == MandateStatus.ACTIVE]
        all_reps = [r para r em self.representatives.values() if r.sector == sector]
        decisions = [d para d em self.decisions if d.sector == sector]
        members = tamanho(self.sector_members.get(sector, set()))

        retorne {
            "sector": sector.value,
            "members": members,
            "active_representatives": tamanho(reps),
            "total_representatives": tamanho(all_reps),
            "decisions_made": tamanho(decisions),
            "avg_accountability": arredonde(np.mean([r.accountability_score()
                reps ? para r em reps]), 1) : 0,
        }


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    // importa numpy as np

    imprima("=" * 80)
    imprima("  OPENREPRESENTATIVE -- REPRESENTACAO SETORIAL")
    imprima("  'Representante nao e chefe. E correio.'")
    imprima("=" * 80)

    system = RepresentativeSystem()

    // === 1. Sectors ===
    imprima("\n\n  === SETORES DA REPUBLICA ===\n")
    para cada s em Sector:
        imprima("    {s.value}")

    // === 2. Register citizens in sectors ===
    imprima("\n\n  === REGISTRO SETORIAL ===\n")

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
        para cada s em sectors:
            system.register_citizen_sector(cid, s)
        imprima("  {name}: {', '.join(s.value for s in sectors)}")

    // === 3. Election ===
    imprima("\n\n  === ELEICAO: SETOR SAUDE (COMUNITARIO) ===\n")

    sector = Sector.HEALTH
    level = RepresentationLevel.COMMUNITY

    // Cidadaos do setor saude
    health_members = system.sector_members[sector]
    imprima("  Membros do setor {sector.value}: {len(health_members)}")

    // Voluntarios para representante
    candidates = [("C-002", "Amina"), ("C-006", "Yara")]
    votes = {"C-002": 4, "C-006": 3}

    rep = system.elect_representative(sector, level, candidates, votes)
    imprima("  Eleito: {rep.name} ({rep.rep_id})")
    imprima("  Mandato: {rep.mandate_duration_days} dias")
    imprima("  Setor: {rep.sector.value} | Nivel: {rep.level.value}")
    imprima("  Status: {rep.status.value}")
    imprima("  AVISO: RECALL a qualquer momento com 25% do setor")

    // === 4. Decision flow ===
    imprima("\n\n  === FLUXO DE DECISAO ===\n")

    decision = system.submit_decision(
        sector = sector, level=level,
        title = "Construir nova clinica no Sahel?",
        description = "O setor de saude delibera: construir nova clinica?",
        options = ["sim", "nao", "adiar"],
        sector_vote = {"sim": 5, "nao": 1, "adiar": 1},
        rep_id = rep.rep_id)

    imprima("  Decisao: {decision.title}")
    imprima("  Votos do setor: {decision.sector_vote}")
    imprima("  Decisao do setor: {decision.winning_option.upper()}")
    imprima("  Representante transportou: SIM (fiel ao setor)")
    imprima("  Representante: {rep.name}")

    // === 5. Representative breaks trust ===
    imprima("\n\n  === REPRESENTANTE QUEBRA CONFIANCA ===\n")

    result = system.representative_breaks_trust(
        rep_id = rep.rep_id,
        sector_decision = "sim",
        rep_actual_vote = "nao")

    imprima("  Setor decidiu: SIM (construir clinica)")
    imprima("  Representante votou: NAO")
    imprima("  Resultado: {result}")

    // Re-elect new rep
    imprima("\n  Novo representante eleito por sorteio:")
    rep2 = system.elect_representative(sector, level,
                                       [("C-006", "Yara")],
                                       {"C-006": 7},
                                       ElectionMethod.SORTITION)
    imprima("  Eleito: {rep2.name} ({rep2.rep_id})")

    // === 6. Recall ===
    imprima("\n\n  === RECALL (REVOGACAO) ===\n")

    // Simulate recall on rep2
    members_set = system.sector_members[sector]
    recall_sigs = set(list(members_set)[:2]) // 2 de 7 = 28%
    recall_result = system.recall(rep2.rep_id, recall_sigs, members_set)
    imprima("  Representante: {rep2.name}")
    imprima("  Assinaturas: {recall_result['signatures']}")
    imprima("  Necessario (25%): {recall_result['threshold_needed']}")
    imprima("  Revogado: {recall_result['recalled']}")
    se recall_result['recalled'] entao:
        imprima("  {recall_result['reason']}")

    // === 7. Sector Report ===
    imprima("\n\n  === RELATORIO DO SETOR SAUDE ===\n")

    report = system.sector_report(sector)
    imprima("  Setor: {report['sector']}")
    imprima("  Membros: {report['members']}")
    imprima("  Representantes ativos: {report['active_representatives']}")
    imprima("  Total representantes (historico): {report['total_representatives']}")
    imprima("  Decisoes tomadas: {report['decisions_made']}")
    imprima("  Score medio de accountability: {report['avg_accountability']}")

    // === Philosophy ===
    POLITICIANS_REP = "Politicos profissionais"
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA: REPRESENTACAO")
    imprima("{'='*80}")
    imprima("""
  DEMOCRACIA REPRESENTATIVA TRADICIONAL OPENREPRESENTATIVE
  ----------------------------------------- -----------------------------------------
  Eleicao a cada 4 anos Eleicao a cada 6 meses
  Mandato de 4 anos Mandato de 6 meses, rotativo
  Nao pode revogar ate proxima eleicao RECALL a qualquer momento (25% do setor)
  Politico profissional (carreira) Rotativo (maximo 2 mandatos, depois troca)
  Representa partido Representa SETOR
  Tem poder proprio Zero poder proprio. So transporta decisao.
  Reunioes secretas Transparencia radical: tudo publico
  Financiamento de campanha ($$$) Zero dinheiro. Voluntario.
  Lobby (empresas compram voto) Impossivel (nao ha dinheiro)
  Vota contra vontade popular Vota contra setor = RECALL AUTOMATICO
  1 politico representa tudo 1 cidadao representa 1 setor
  Pobre nunca e representado Cada setor tem voz propria
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
    2. Mandato maximo 6 meses
    3. Max 2 mandatos consecutivos (rotacao)
    4. Recall instantaneo com 25% do setor
    5. Tudo publico: votos, reunioes, conversas
    6. Se votar CONTRA o setor: REMOVIDO automaticamente
    7. Zero remuneracao (nao ha dinheiro)
    8. Sorteio ou eleicao direta
    9. Zero profissionalizacao (nao e carreira)
    10. Voltar a funcao anterior apos mandato

  "O representante nao e chefe.
   e CORREIO.
   Leva a voz do setor.
   Traz a decisao da Republica.
   Nao tem poder proprio.
   So tem a voz de quem representa."
// )

```
