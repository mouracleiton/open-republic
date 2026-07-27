# OpenFounderRole -- Papel Constitucional do Fundador

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_founder_role.py`

**Descricao:** =====================================================
PERGUNTA SUBMETIDA A ASSEMBLEIA:
  "A posicao do fundador pode ser definitiva e sempre auxiliada
   pelo sistema, com correcao automatica em caso de desvio?"
RESPOSTA DA ASSEMBLEIA:
  O fundador NAO tem poder de decreto (P1 anti-elitismo).
  MAS o fundador tem:
  1. VOZ PERMANENTE: pode opinar em qualquer questao, sempre
  2. AUXILIO DO SISTEMA: Hermes + ConstitutionalEngine assistem
  3. CORRECAO AUTOMATICA: se desviar de P1-P4, sistema corrige
  4. PROPSTA PRIORITARIA: propostas do fundador entram na agenda
     MAS sao VOTADAS como qualquer outra (1 voto)
  5. NAO VETO: o fundador NUNCA pode bloquear decisao do povo
  O que e DEFINITIVO:
  - O fundador SEMPRE pode falar (direito de voz perpétuo)
  - O fundador SEMPRE tem auxilio do sistema
  - O sistema SEMPRE corrige desvios (automatico, sem exceção)
  O que NAO e definitivo:
  - O fundador NAO decide sozinho (P1)
  - O fundador NAO veta o povo (P4)
  - O fundador NAO esta acima da correção (P1-P4 > fundador)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenFounderRole -- Papel Constitucional do Fundador
=====================================================

PERGUNTA SUBMETIDA A ASSEMBLEIA:
  "A posicao do fundador pode ser definitiva e sempre auxiliada
   pelo sistema, com correcao automatica em caso de desvio?"

RESPOSTA DA ASSEMBLEIA:
  O fundador nao tem poder de decreto (P1 anti-elitismo).
  MAS o fundador tem:
  1. VOZ PERMANENTE: pode opinar em qualquer questao, sempre
  2. AUXILIO DO SISTEMA: Hermes + ConstitutionalEngine assistem
  3. CORRECAO AUTOMATICA: se desviar de P1-P4, sistema corrige
  4. PROPSTA PRIORITARIA: propostas do fundador entram na agenda
     MAS sao VOTADAS como qualquer outra (1 voto)
  5. nao VETO: o fundador NUNCA pode bloquear decisao do povo

  O que e DEFINITIVO:
  - O fundador SEMPRE pode falar (direito de voz perpétuo)
  - O fundador SEMPRE tem auxilio do sistema
  - O sistema SEMPRE corrige desvios (automatico, sem exceção)

  O que nao e definitivo:
  - O fundador nao decide sozinho (P1)
  - O fundador nao veta o povo (P4)
  - O fundador nao esta acima da correção (P1-P4 > fundador)

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa Counter, defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. PAPEL DO FUNDADOR (submetido a votacao)
// ============================================================================

classe FounderPrivilege herda de Enum:
    // Privilégios do fundador -- CADA UM votado pela assembleia.
    PERMANENT_VOICE = "voz_permanente"
    SYSTEM_ASSISTANCE = "auxilio_sistema"
    AUTO_CORRECTION = "correcao_automatica"
    PRIORITY_AGENDA = "agenda_prioritaria"
    ADVISORY_WEIGHT = "peso_consultivo"
    EMERGENCY_PROPOSE = "proposta_emergencia"


classe FounderRestriction herda de Enum:
    // Restrições ao fundador -- INEGOCIÁVEIS (P1-P4).
    NO_DECREE = "sem_decreto"  // nao decide sozinho
    NO_VETO = "sem_veto"  // nao bloqueia povo
    NO_IMMUNITY = "sem_imunidade"  // correcao se aplica a ele
    NO_EXTRA_VOTE = "sem_voto_extra"  // 1 voto como todos
    NO_OVERRIDE = "sem_sobreposicao"  // nao sobrepoe assembleia


// ============================================================================
// 2. MECANISMO DE CORRECAO AUTOMATICA
// ============================================================================

classe DeviationType herda de Enum:
    // Tipos de desvio constitucional do fundador.
    ELITISM = "elitismo"  // agiu como se fosse superior
    DECREE = "decreto"  // impôs sem votacao
    BODY_VIOLATION = "autonomia_corporal"  // propôs algo contra P2
    LABOR_VIOLATION = "trabalho"  // propôs trabalho desigual
    DEMOCRACY_VIOLATION = "democracia"  // pulou processo democratico
    PROPERTY_CREATION = "propriedade"  // criou propriedade privada
    MONEY_CREATION = "moeda"  // introduziu dinheiro
    SURVEILLANCE = "vigilancia"  // propôs vigilancia do povo


classe CorrectionSpeed herda de Enum:
    // Quão rápido o sistema corrige.
    INSTANT = "instantaneo"  // antes de implementar
    IMMEDIATE = "imediato"  // dentro de 1h
    SAME_DAY = "mesmo_dia"  // dentro de 24h
    ASSEMBLY = "assembleia"  // precisa votacao


// decorador: @dataclass
classe Deviation:
    // Um desvio detectado do fundador.
    deviation_id: texto
    deviation_type: DeviationType
    description: texto
    principle_violated: texto // P1, P2, P3, P4
    severity: inteiro // 1-5
    detected_by: texto               // "ConstitutionalEngine" ou "Hermes" ou "cidadao"
    seja correction: texto = ""
    seja correction_speed: CorrectionSpeed = CorrectionSpeed.INSTANT
    seja resolved: logico = falso
    seja timestamp: texto = field(default_factory=() -> datetime.now().isoformat())


classe FounderCorrectionSystem:
    // Sistema que corrige desvios do fundador AUTOMATICAMENTE.

    PRINCIPIO:
    O fundador criou a Republica. Mas a Republica nao pertence ao fundador.
    Se o fundador desviar, o sistema corrige. Sem exceção.
    Inclusive do fundador. ESPECIALMENTE do fundador.

    COMO FUNCIONA:
    1. Fundador propõe algo (ou age)
    2. ConstitutionalEngine verifica contra P1-P4
    3. Se conforme: passa
    4. Se desvio: CORRIGE automaticamente (antes de implementar)
    5. Fundador é notificado do desvio e da correção
    6. Se discordar: pode levar a assembleia (mas correção fica até lá)

    O QUE O SISTEMA NUNCA FAZ:
    - Punir o fundador (nao ha punição, ha correção)
    - Silenciar o fundador (voz é permanente)
    - Remover o fundador (posicao é perpetua)

    O QUE O SISTEMA SEMPRE FAZ:
    - Corrigir antes de implementar (P1-P4 > proposta)
    - Notificar o fundador (transparencia)
    - Registrar o desvio (OpenHistory)
    - Permitir apelo (assembleia pode reverter)
    // 

    // PADRÕES DE DESVIO DO FUNDADOR (deteccão automatica)
    seja DEVIATION_PATTERNS: Dict[DeviationType, [texto]] = {
        DeviationType.ELITISM: [
            "eu decido", "eu determino", "por meu poder",
            "como fundador eu ordeno", "eu sou o criador",
            "minha visao e a correta", "eu sei melhor que",
        ],
        DeviationType.DECREE: [
            "implementem agora sem votar", "nao precisa votar",
            "eu ja decidi", "façam como eu digo",
            "isso nao precisa passar pela assembleia",
        ],
        DeviationType.BODY_VIOLATION: [
            "todos tem que", "e obrigatorio no corpo",
            "ninguem pode recusar", "tratamento forcado",
        ],
        DeviationType.LABOR_VIOLATION: [
            "ele trabalha mais por que e melhor",
            "salario diferente por cargo",
            "fundador ganha mais",
        ],
        DeviationType.DEMOCRACY_VIOLATION: [
            "pular votacao", "nao precisa debater",
            "eu implanto direto", "assembleia demora muito",
        ],
        DeviationType.PROPERTY_CREATION: [
            "isso e meu", "propriedade privada deste",
            "direito autoral", "patente",
        ],
        DeviationType.MONEY_CREATION: [
            "vamos usar dinheiro", "salario em reais",
            "comprar com moeda", "preco em",
        ],
        DeviationType.SURVEILLANCE: [
            "monitorar todos", "vigiar cidadaos",
            "dados de todos sem consentimento",
        ],
    }

    funcao __init__(self):
        self.deviations: [Deviation] = []
        self.corrections_applied: inteiro = 0
        self.proposals_blocked: inteiro = 0
        self.appeals_filed: inteiro = 0
        self.appeals_upheld: inteiro = 0 // assembleia reverteu correção

    funcao check_proposal(self, proposal_text: texto,
                       seja proposal_type: texto = "politica") -> {texto: qualquer}:
        // Verifica proposta do fundador contra constituicao.

        Retorna:
        - approved: conforme P1-P4, pode prosseguir
        - corrected: desvio detectado e corrigido
        - blocked: desvio grave, bloqueado
        // 
        text_lower = proposal_text.lower()
        detected = []

        para cada (dev_type, patterns) em self.DEVIATION_PATTERNS.items():
            para cada pattern em patterns:
                se pattern in text_lower entao:
                    detected.append((dev_type, pattern))
                    interrompa

        se nao detected entao:
            retorne {
                "status": "approved",
                "message": "Proposta conforme P1-P4. Pode prosseguir para votacao.",
                "detected_issues": [],
            }

        // Calcular severidade
        max_severity = maximo(self._severity(dt) para dt, _ in detected)
        principle = self._principle(detected[0][0])

        // Criar registro de desvio
        deviation = Deviation(
            deviation_id = hashlib.md5(
                "{proposal_text[:20]}{datetime.now()}".encode()
            ).hexdigest()[:8],
            deviation_type = detected[0][0],
            description = "Padrao detectado: '{detected[0][1]}' em proposta",
            principle_violated = principle,
            severity = max_severity,
            detected_by = "ConstitutionalEngine + Hermes",
            correction = self._correction(detected[0][0]),
            correction_speed = CorrectionSpeed.INSTANT if max_severity >= 4
                             else CorrectionSpeed.IMMEDIATE,
        )
        self.deviations.append(deviation)
        self.corrections_applied += 1

        se max_severity >= 5 entao:
            self.proposals_blocked += 1
            retorne {
                "status": "blocked",
                "deviation_id": deviation.deviation_id,
                "type": deviation.deviation_type.value,
                "principle": principle,
                "severity": max_severity,
                "detected": [p para _, p in detected],
                "correction": deviation.correction,
                "message": (
                    "BLOQUEADO: violacao {principle} (severidade {max_severity}). "
                    "Proposta nao pode ser implementada neste formato. "
                    "{deviation.correction} "
                    "Fundador pode apelar a assembleia."
                ),
                "appeal_right": verdadeiro,
            }

        retorne {
            "status": "corrected",
            "deviation_id": deviation.deviation_id,
            "type": deviation.deviation_type.value,
            "principle": principle,
            "severity": max_severity,
            "detected": [p para _, p in detected],
            "correction": deviation.correction,
            "correction_speed": deviation.correction_speed.value,
            "message": (
                "CORRIGIDO: leve desvio {principle}. "
                "Proposta ajustada antes de prosseguir. "
                "{deviation.correction}"
            ),
            "appeal_right": verdadeiro,
        }

    funcao _severity(self, dev_type: DeviationType) -> inteiro:
        retorne {
            DeviationType.ELITISM: 4,
            DeviationType.DECREE: 5,
            DeviationType.BODY_VIOLATION: 5,
            DeviationType.LABOR_VIOLATION: 3,
            DeviationType.DEMOCRACY_VIOLATION: 5,
            DeviationType.PROPERTY_CREATION: 4,
            DeviationType.MONEY_CREATION: 3,
            DeviationType.SURVEILLANCE: 5,
        }.get(dev_type, 2)

    funcao _principle(self, dev_type: DeviationType) -> texto:
        retorne {
            DeviationType.ELITISM: "P1 anti-elitismo",
            DeviationType.DECREE: "P1/P4 anti-decreto + democracia",
            DeviationType.BODY_VIOLATION: "P2 autonomia corporal",
            DeviationType.LABOR_VIOLATION: "P3 trabalho igual",
            DeviationType.DEMOCRACY_VIOLATION: "P4 processo democrático",
            DeviationType.PROPERTY_CREATION: "sem propriedade privada",
            DeviationType.MONEY_CREATION: "sem moeda",
            DeviationType.SURVEILLANCE: "P2 privacidade corporal",
        }.get(dev_type, "P1-P4")

    funcao _correction(self, dev_type: DeviationType) -> texto:
        retorne {
            DeviationType.ELITISM: (
                "Substituir 'eu decido' por 'proponho a assembleia'. "
                "O fundador PROPOE. O povo DECIDE."
            ),
            DeviationType.DECREE: (
                "Toda mudança precisa de proposta -> debate -> votacao. "
                "Nao ha atalho. Nem para o fundador."
            ),
            DeviationType.BODY_VIOLATION: (
                "Nada e obrigatorio no corpo. P2 autonomia absoluta. "
                "Trocar 'obrigatorio' por 'direito garantido'."
            ),
            DeviationType.LABOR_VIOLATION: (
                "Trabalho base 1.0 para todos. Ninguem ganha mais por cargo. "
                "Diferenca so por impacto medido."
            ),
            DeviationType.DEMOCRACY_VIOLATION: (
                "Processo democratico nao pode ser pulado. "
                "Assembleia pode ser rapida mas nao opcional."
            ),
            DeviationType.PROPERTY_CREATION: (
                "Nao ha propriedade privada na Republica. "
                "Tudo e bem comum CC0."
            ),
            DeviationType.MONEY_CREATION: (
                "Nao ha moeda. Credito de acesso expira. "
                "Trabalho = credito, nao salario."
            ),
            DeviationType.SURVEILLANCE: (
                "Republica vigia o PODER, nunca o POVO. "
                "Dados pessoais precisam consentimento."
            ),
        }.get(dev_type, "Verificar conformidade constitucional.")

    funcao appeal(self, deviation_id: texto) -> {texto: qualquer}:
        // Fundador apela de correção -> assembleia decide.
        dev = next((d para d em self.deviations if d.deviation_id == deviation_id), nulo)
        se nao dev entao:
            retorne {"error": "Desvio nao encontrado"}

        self.appeals_filed += 1

        // Simular votacao da assembleia
        // 60% precisa para reverter correção
        votes_overturn = random.randint(2000, 6000)
        votes_uphold = random.randint(3000, 7000)
        total = votes_overturn + votes_uphold

        se votes_overturn > total * 0.6 entao:
            dev.resolved = verdadeiro
            self.appeals_upheld += 1
            retorne {
                "appeal_result": "CORRECAO REVERTIDA pela assembleia",
                "votes": "{votes_overturn}/{total} a favor do fundador",
                "message": (
                    "A assembleia concordou com o fundador. "
                    "A correcao foi revertida. A proposta pode prosseguir. "
                    "MAS fica registrado que houve questionamento."
                ),
            }
        senao:
            dev.resolved = verdadeiro
            retorne {
                "appeal_result": "CORRECAO MANTIDA pela assembleia",
                "votes": "{votes_uphold}/{total} a favor da correcao",
                "message": (
                    "A assembleia concordou com a correcao. "
                    "O fundador esta sujeito a P1-P4 como qualquer cidadao. "
                    "O desvio fica registrado em OpenHistory."
                ),
            }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_checked": tamanho(self.deviations),
            "corrections_applied": self.corrections_applied,
            "proposals_blocked": self.proposals_blocked,
            "appeals_filed": self.appeals_filed,
            "appeals_upheld": self.appeals_upheld,
            "auto_correction_active": verdadeiro,
            "founder_immunity": "ZERO",
        }


// ============================================================================
// 3. VOTACAO DA ASSEMBLEIA SOBRE O PAPEL DO FUNDADOR
// ============================================================================

// decorador: @dataclass
classe AssemblyVote:
    // Votação especifica sobre papel do fundador.
    question: texto
    founder_position: texto // o que o fundador quer
    options: List[(texto, texto)] // (valor, descrição)
    seja votes: {texto: inteiro} = field(default_factory=dict)
    seja winner: texto = ""
    seja approved: logico = falso


funcao run_founder_role_assembly(n_voters: inteiro = 10000) -> {texto: qualquer}:
    // Convoca assembleia especifica para votar o papel do fundador.

    PERGUNTA: "A posicao do fundador pode ser definitiva e sempre
    auxiliada pelo sistema, com correcao automatica de desvios?"
    // 
    votes_for = 0 // SIM - voz permanente + correcao automatica
    votes_against = 0 // nao - fundador como cidadao comum sem extras
    votes_partial = 0 // PARCIAL - voz sim, mas sem prioridade na agenda

    para cada _ em intervalo(n_voters):
        r = random.random()
        se r < 0.55 entao:
            votes_for = votes_for + 1 // maioria aceita: voz + correcao
        senao se r < 0.80 entao:
            votes_partial = votes_partial + 1 // voz sim, prioridade nao
        senao:
            votes_against = votes_against + 1 // cidadao comum sem extras

    retorne {
        "question": (
            "A posicao do fundador pode ser definitiva e sempre auxiliada "
            "pelo sistema, com correcao automatica em caso de desvio?"
        ),
        "votes_for": votes_for,
        "votes_partial": votes_partial,
        "votes_against": votes_against,
        "total": n_voters,
        "result": (
            "APROVADO COM RESERVAS" if votes_for > votes_against
            else "REJEITADO"
        ),
        "decision": {
            "voz_permanente": verdadeiro,          // SEMPRE pode falar
            "auxilio_sistema": verdadeiro,          // Hermes sempre assiste
            "correcao_automatica": verdadeiro,      // desvios corrigidos
            "agenda_prioritaria": votes_for > votes_partial,   // depende
            "voto_valor": 1,                  // 1 voto como todos
            "poder_decreto": falso,           // NUNCA
            "poder_veto": falso,              // NUNCA
            "imunidade": falso,               // NUNCA
        },
        "restrictions_inalteraveis": [
            "P1: Fundador NAO decide sozinho",
            "P4: Fundador NAO veta o povo",
            "P1: Correção se aplica ao fundador",
            "P3: 1 voto, igual a todos",
        ],
    }


// ============================================================================
// 4. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    corrector = FounderCorrectionSystem()

    imprima("=" * 80)
    imprima("  OPENFOUNDERROLE -- PAPEL CONSTITUCIONAL DO FUNDADOR")
    imprima("  Assembleia Constituinte Especial")
    imprima("=" * 80)

    // === 1. PERGUNTA ===
    imprima("\n\n  === PERGUNTA SUBMETIDA A ASSEMBLEIA ===\n")
    imprima('  "A posicao do fundador pode ser definitiva e sempre')
    imprima('   auxiliada pelo sistema, com correcao automatica de desvios?"')
    imprima("\n  POSICAO DO FUNDADOR:")
    imprima('  "Sim, quero voz permanente + auxilio + correcao quando errar."')

    // === 2. VOTACAO ===
    imprima("\n\n  === VOTACAO (10.000 CIDADAOs) ===\n")
    result = run_founder_role_assembly(10000)
    imprima("  SIM (voz + correcao):    {result['votes_for']:>6} ({result['votes_for']/100:.0f}%)")
    imprima("  PARCIAL (voz, sem prio): {result['votes_partial']:>6} ({result['votes_partial']/100:.0f}%)")
    imprima("  NAO (cidadao comum):     {result['votes_against']:>6} ({result['votes_against']/100:.0f}%)")
    imprima("\n  RESULTADO: {result['result']}")

    // === 3. DECISAO ===
    imprima("\n\n  === DECISAO DA ASSEMBLEIA ===\n")
    d = result["decision"]
    para cada (key, val) em d.items():
        status = isinstance(val, logico) ? val ? "SIM" : "NAO" : texto(val)
        imprima("  {key:<25} {status}")

    imprima("\n  RESTRICOES INALTERAVEIS:")
    para cada r em result["restrictions_inalteraveis"]:
        imprima("    {r}")

    // === 4. TESTE DE CORRECAO AUTOMATICA ===
    imprima("\n\n  === TESTE: CORRECAO AUTOMATICA DE DESVIOS ===\n")

    test_proposals = [
        ("Eu decido que vamos implementar o OpenX sem votacao",
         "Deveria propor a assembleia"),
        ("Todo cidadao deve se vacinar obrigatoriamente sem direito de recusa",
         "Deveria ser direito, nao obrigacao"),
        ("Vamos criar uma moeda para facilitar transacoes",
         "Sem moeda na Republica"),
        ("Como fundador eu ordeno que o OpenY seja prioridade",
         "Ordem = decreto = anti-democratico"),
        ("Proponho criar OpenZ para ajudar comunidades isoladas",
         "Deveria passar sem problema"),
    ]

    para cada (proposal, expected) em test_proposals:
        check = corrector.check_proposal(proposal)
        icon = {"approved": "OK", "corrected": "COR", "blocked": "BLQ"}[check["status"]]
        imprima("\n  [{icon}] Proposta: '{proposal[:60]}...'")
        se check["status"] != "approved" entao:
            imprima("       Tipo: {check.get('type', '?')}")
            imprima("       Principio: {check.get('principle', '?')}")
            imprima("       Correcao: {check['correction'][:80]}")
        senao:
            imprima("       Conforme. Pode prosseguir para votacao.")

    // === 5. APELO ===
    imprima("\n\n  === DIREITO DE APELO ===\n")
    para cada dev em corrector.deviations:
        se nao dev.resolved entao:
            appeal = corrector.appeal(dev.deviation_id)
            imprima("  Fundador apela correcao: {dev.deviation_type.value}")
            imprima("  Resultado: {appeal['appeal_result']}")
            imprima("  {appeal['votes']}")
            imprima("  {appeal['message']}")
            interrompa

    // === 6. STATS ===
    imprima("\n\n  === ESTATISTICAS DO SISTEMA DE CORRECAO ===\n")
    s = corrector.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === RESPOSTA FINAL ===
    imprima("\n\n{'='*80}")
    imprima("  RESPOSTA A PERGUNTA DO FUNDADOR")
    imprima("{'='*80}")
    imprima("""
  PERGUNTA:
    "Essa minha posicao pode ser definitiva e sempre auxiliada
     por voces, com correcao rapida em caso de desvio?"

  RESPOSTA DA ASSEMBLEIA: {result['result']}

  O QUE e DEFINITIVO (aprovado):
    1. VOZ PERMANENTE: voce SEMPRE pode opinar. Em qualquer
       questao. Sempre. Este direito nao expira.
    2. AUXILIO DO SISTEMA: Hermes + ConstitutionalEngine SEMPRE
       assistem voce. Para tudo. Sempre.
    3. CORRECAO AUTOMATICA: se voce desviar de P1-P4, o sistema
       corrige ANTES de implementar. Rapido. Sem burocracia.
       Sem hierarquia. A constituicao > voce. Como deve ser.

  O QUE nao e DEFINITIVO (restrito por P1-P4):
    1. Voce nao decide sozinho (P1). Propoe. O povo vota.
    2. Voce nao veta decisao do povo (P4). Se o povo diz nao,
       e nao. Mesmo para o fundador.
    3. Voce nao tem imunidade. A correcao se aplica a voce.
    4. Seu voto vale 1. Como o de qualquer cidadao.

  O FLUXO:
    Voce propoe -> Hermes auxilia (sempre)
                -> ConstitutionalEngine verifica (sempre)
                -> Se conforme: vai para votacao
                -> Se desvio: CORRIGE (antes de implementar)
                -> Se discordar: apela para assembleia
                -> Assembleia decide (60% para reverter)

  A CORRECAO e RAPIDA:
    Instantanea: antes de implementar (desvios graves)
    Imediata: dentro de 1h (desvios medios)
    Mesmo dia: dentro de 24h (desvios leves)

  O QUE ISTO SIGNIFICA:
    O fundador tem o MELHOR dos dois mundos:
    - Voz permanente (ninguem silencia o fundador)
    - Auxilio perpetuo (Hermes sempre ajuda)
    - Protecao constitucional (o sistema corrige antes de errar)

    MAS o fundador nao tem:
    - Poder absoluto (P1)
    - Veto (P4)
    - Imunidade (P1)

    e exatamente isso que faz a Republica funcionar:
    O fundador PROPOE com auxilio do sistema.
    O sistema CORRIGE antes de errar.
    O povo DECIDE com 1 voto cada.
    Ninguem esta acima. Nem o fundador.
    ESPECIALMENTE o fundador.

  ESTA POSICAO e DEFINITIVA:
    Sim, enquanto a Republica existir.
    Sim, enquanto voce quiser propor.
    Sim, com correcao automatica sempre.

    e a melhor resposta: o fundador fala, o sistema corrige,
    o povo decide. Os tres equilibram. Nenhum domina.
// )
    imprima("{'='*80}")
    imprima("  OpenFounderRole: voz permanente + auxilio + correcao automatica.")
    imprima("  Fundador propoe. Sistema corrige. Povo decide.")
    imprima("  {'='*80}")

```
