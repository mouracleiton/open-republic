# OpenAntiSpamCall -- Ligacao Telefonica Predatoria PROIBIDA

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_anti_spam_call.py`

**Descricao:** =============================================================
"Para de me encher o saco porra.
 Ninguem tem direito de ligar pra vender, enganar, cobrar
 ou perturbar sem consentimento.
 PROIBIDO. Ponto."
ASSEMBLEIA CONSTITUINTE CONVOCADA:
  "Ligacoes telefonicas nao solicitadas devem ser PROIBIDAS?"
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenAntiSpamCall -- Ligacao Telefonica Predatoria PROIBIDA
=============================================================

"Para de me encher o saco porra.
 Ninguem tem direito de ligar pra vender, enganar, cobrar
 ou perturbar sem consentimento.
 PROIBIDO. Ponto."

ASSEMBLEIA CONSTITUINTE CONVOCADA:
  "Ligacoes telefonicas nao solicitadas devem ser PROIBIDAS?"

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa Counter, defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. TIPOS DE LIGACAO PREDATORIA
// ============================================================================

classe SpamCallType herda de Enum:
    TELEMARKETING = "telemarketing"  // vender sem consentimento
    SCAM = "golpe"  // enganar para roubar
    DEBT_COLLECTION = "cobranca_abusiva"  // ameacar devedor
    PHISHING = "phishing"  // pedir dados
    ROBOTCALL = "robô"  // ligacao automatica
    POLITICAL_SPAM = "politico"  // pedir voto
    RELIGIOUS_SPAM = "religioso"  // proselitismo
    SURVEY_SPAM = "pesquisa"  // pesquisa nao consentida
    FAKE_LOTTERY = "falsa_loteria"  // "voce ganhou"
    FAKE_FAMILY = "falsa_familia"  // "seu filho sequestrado"
    INSURANCE_SPAM = "seguro"  // vender seguro
    SOLAR_PANEL_SPAM = "painel_solar"  // vender painel (ironia)
    INVESTMENT_SCAM = "investimento"  // "renda extra"


classe CallSeverity herda de Enum:
    NUISANCE = ("aborrecimento", 1)  // incomoda mas nao dana
    PERSISTENT = ("persistente", 2)  // liga todo dia
    DECEPTIVE = ("enganoso", 3)  // mente para lucrar
    DANGEROUS = ("perigoso", 4)  // risco de golpe
    CRIMINAL = ("criminal", 5)  // golpe confirmado


// ============================================================================
// 2. REGISTRO DE LIGACAO
// ============================================================================

// decorador: @dataclass
classe SpamCall:
    // Uma ligacao predatoria registrada.
    seja call_id: texto = ""
    seja phone_number: texto = ""
    seja caller_name: texto = ""
    seja call_type: SpamCallType = SpamCallType.TELEMARKETING
    seja severity: CallSeverity = CallSeverity.NUISANCE
    seja description: texto = ""
    seja timestamp: texto = ""
    seja duration: texto = ""
    seja victim_id: texto = ""
    seja blocked: logico = falso
    seja reported: logico = verdadeiro
    seja auto_blocked: logico = falso


// ============================================================================
// 3. MOTOR ANTI-SPAM
// ============================================================================

classe AntiSpamCallEngine:
    // Motor que PROIBE e BLOQUEIA ligacoes predatorias.

    O QUE e PROIBIDO (TODOS):
    1. Telemarketing sem consentimento EXPLICITO
    2. Robocalls (ligacao automatica)
    3. Golpe / scam (qualquer tipo)
    4. Cobranca abusiva (ameaca, assedio)
    5. Phishing (pedir dados)
    6. Politico pedindo voto (sem autorizacao)
    7. Religioso sem autorizacao
    8. "Voce ganhou" (falso)
    9. Qualquer ligacao nao SOLICITADA

    O QUE e PERMITIDO:
    1. Ligacao de alguem que VOCE ligou (retorno)
    2. Ligacao de familia/amigo (consentimento implicito)
    3. Emergencia (servico publico)
    4. OpenHealth (consulta marcada por VOCE)
    5. Emprego (VOCE se candidatou)
    6. Qualquer ligacao que VOCE AUTORIZOU

    COMO FUNCIONA:
    1. IA analisa chamada ANTES de tocar (caller ID + padrao)
    2. Se spam conhecido: BLOQUEIA (nao toca)
    3. Se suspeito: manda pra correio voz (IA escuta)
    4. Se confirmado spam: bloqueia numero PERMANENTE
    5. Vítima NUNCA ouve o telefone tocar com spam

    CONSENTIMENTO EXPLICITO (opt-in):
    - Ninguem pode ligar sem voce AUTORIZAR
    - Autorizacao e POR EMPRESA, nao geral
    - Pode revogar a qualquer momento
    - OpenSocialNetwork tem lista de quem voce autorizou

    DENUNCIA:
    - 1 denuncia: numero marcado
    - 3 denuncias: numero bloqueado para TODA Republica
    - 10 denuncias: numero reportado como criminal
    // 

    // Numeros bloqueados (base coletiva da Republica)
    seja blocked_numbers: {texto: Dict} = field(default_factory=dict)
    seja reported_numbers: {texto: inteiro} = field(default_factory=dict)

    funcao __init__(self):
        self.blocked_numbers = {}
        self.reported_numbers = {}
        self.calls_blocked = 0
        self.calls_reported = 0

    funcao register_spam(self, phone: texto, caller: texto,
                      call_type: SpamCallType,
                      seja severity: CallSeverity = CallSeverity.NUISANCE,
                      seja description: texto = "",
                      seja victim: texto = "") -> {texto: qualquer}:
        // Registra ligacao predatoria.
        cid = hashlib.md5(
            "{phone}{call_type.value}{datetime.now()}".encode()
        ).hexdigest()[:8]

        call = SpamCall(
            call_id = cid, phone_number=phone, caller_name=caller,
            call_type = call_type, severity=severity,
            description = description, timestamp=datetime.now().isoformat(),
            victim_id = victim,
        )

        // Contar denuncias
        self.reported_numbers[phone] = self.reported_numbers.get(phone, 0) + 1
        self.calls_reported += 1

        // Bloqueio automatico
        should_block = falso
        block_reason = ""

        se severity == CallSeverity.CRIMINAL entao:
            should_block = verdadeiro
            block_reason = "CRIMINAL (golpe confirmado)"
        senao se self.reported_numbers[phone] >= 3 entao:
            should_block = verdadeiro
            block_reason = "3+ denuncias ({self.reported_numbers[phone]})"
        elif call_type in (SpamCallType.ROBOTCALL, SpamCallType.SCAM,
                           SpamCallType.PHISHING, SpamCallType.FAKE_LOTTERY):
            should_block = verdadeiro
            block_reason = "{call_type.value} (auto-bloqueado)"

        se should_block entao:
            self.blocked_numbers[phone] = {
                "caller": caller,
                "type": call_type.value,
                "reports": self.reported_numbers[phone],
                "blocked_date": datetime.now().isoformat(),
                "reason": block_reason,
            }
            self.calls_blocked += 1

        retorne {
            "call_id": cid,
            "phone": phone,
            "caller": caller,
            "type": call_type.value,
            "severity": severity.value[0],
            "reports_for_this_number": self.reported_numbers[phone],
            "blocked": should_block,
            should_block ? "block_reason": block_reason : "Nao bloqueado ainda",
            "message": (
                "Ligacao de {caller} ({phone}) REGISTRADA. "
                "Tipo: {call_type.value}. Severidade: {severity.value[0]}. "
                "Denuncias: {self.reported_numbers[phone]}. "
                "{'BLOQUEADO para TODA Republica.' if should_block else 'Marcado. 3 denuncias = bloqueio.'}"
            ),
        }

    funcao check_incoming(self, phone: texto, caller: texto = "",
                       seja is_robotcall: logico = falso,
                       seja user_authorized: logico = falso
                       ) -> {texto: qualquer}:
        // IA verifica chamada ANTES de tocar.
        // Usuario autorizou?
        se user_authorized entao:
            retorne {
                "phone": phone,
                "action": "PERMITIR",
                "reason": "Usuario autorizou este numero",
            }

        // Ja bloqueado?
        se phone in self.blocked_numbers entao:
            retorne {
                "phone": phone,
                "caller": self.blocked_numbers[phone]["caller"],
                "action": "BLOQUEAR",
                "reason": self.blocked_numbers[phone]["reason"],
                "message": (
                    "BLOQUEADO. {self.blocked_numbers[phone]['caller']} "
                    "({phone}) tem {self.blocked_numbers[phone]['reports']} denuncias. "
                    "Nao toca. Vitima nao ouve. Paz."
                ),
            }

        // Robocall?
        se is_robotcall entao:
            retorne {
                "phone": phone,
                "action": "BLOQUEAR",
                "reason": "Robocall (automatico) = PROIBIDO",
                "message": "Robocall bloqueada. Nao existe robocall na Republica.",
            }

        // Reportado mas nao bloqueado?
        reports = self.reported_numbers.get(phone, 0)
        se reports > 0 entao:
            retorne {
                "phone": phone,
                "action": "CORREIO VOZ (IA escuta)",
                "reason": "{reports} denuncia(s). IA verifica antes de tocar.",
                "message": (
                    "{phone} tem {reports} denuncia(s). "
                    "Mandado pra correio de voz com IA. "
                    "Se for spam: bloqueado. Se for legitimo: toca."
                ),
            }

        // Desconhecido
        retorne {
            "phone": phone,
            "action": "PERMITIR (primeira vez)",
            "reason": "Numero novo. Sem denuncias.",
            "message": "{phone}: numero novo. Toca normalmente. Se for spam, denuncie.",
        }

    funcao consent_list(self) -> {texto: qualquer}:
        // Lista de consentimento (opt-in).
        retorne {
            "regra": "NINGUEM liga sem voce AUTORIZAR",
            "autorizacao": "POR EMPRESA/PESSOA (nao geral)",
            "revogavel": "A qualquer momento",
            "onde": "OpenSocialNetwork > Configuracoes > Autorizacoes",
            "exemplos_autorizados": [
                "OpenHealth (consulta que VOCE marcou)",
                "Familia/amigos (consentimento implicito)",
                "Emprego (VOCE se candidatou)",
            ],
            "exemplos_proibidos": [
                "Telemarketing (voce nao pediu)",
                "Banco cobrando (usar OpenCredit, nao telefone)",
                "Politico pedindo voto",
                "Qualquer sem autorizacao EXPLICITA",
            ],
        }

    funcao penalty(self, spammer_phone: texto, spammer_name: texto,
                n_victims: inteiro) -> {texto: qualquer}:
        // Penalidade para quem faz spam.
        se n_victims >= 100 entao:
            penalty = "CRIMINAL. OpenPenalRevision. Crime contra privacidade."
        senao se n_victims >= 10 entao:
            penalty = "OpenCivicEducation + multa (durante transicao)."
        senao:
            penalty = "Numero bloqueado PERMANENTE para toda Republica."

        retorne {
            "spammer": spammer_name,
            "phone": spammer_phone,
            "victims": n_victims,
            "penalty": penalty,
            "number_status": "BLOQUEADO PERMANENTE",
            "message": (
                "{spammer_name} ({spammer_phone}): {n_victims} vitimas. "
                "{penalty} Numero bloqueado para sempre."
            ),
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "numeros_bloqueados": tamanho(self.blocked_numbers),
            "ligacoes_reportadas": self.calls_reported,
            "ligacoes_bloqueadas": self.calls_blocked,
            "principio": "Para de me encher o saco. Ninguem liga sem autorizar.",
        }


// ============================================================================
// 4. VOTACAO DA ASSEMBLEIA
// ============================================================================

funcao run_spam_assembly(n_voters: inteiro = 10000) -> {texto: qualquer}:
    votes_ban = 0
    votes_regulate = 0
    votes_keep = 0

    para cada _ em intervalo(n_voters):
        r = random.random()
        se r < 0.94 entao:
            votes_ban = votes_ban + 1
        senao se r < 0.99 entao:
            votes_regulate = votes_regulate + 1
        senao:
            votes_keep = votes_keep + 1

    retorne {
        "question": (
            "Ligacoes telefonicas NAO solicitadas devem ser PROIBIDAS? "
            "(telemarketing, robocall, scam, cobranca abusiva)"
        ),
        "votes": {
            "PROIBIR (zero spam)": votes_ban,
            "REGULAR (com regras)": votes_regulate,
            "MANTER (como esta)": votes_keep,
        },
        "total": n_voters,
        "winner": "PROIBIR (zero spam)",
        "winner_pct": "{votes_ban/n_voters*100:.0f}%",
        "decision": (
            "APROVADO. 94% dos cidadaos querem PROIBIR. "
            "Ligacao nao solicitada = CRIME contra privacidade."
        ),
    }


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = AntiSpamCallEngine()

    imprima("=" * 80)
    imprima("  OPENANTISPAMCALL -- LIGACAO PREDATORIA PROIBIDA")
    imprima("  'Para de me encher o saco porra.'")
    imprima("=" * 80)

    // === 1. ASSEMBLEIA ===
    imprima("\n\n  === 1. ASSEMBLEIA CONSTITUINTE ===\n")
    result = run_spam_assembly(10000)
    imprima("  PERGUNTA: {result['question']}\n")
    para cada (option, count) em result["votes"].items():
        pct = count / result["total"] * 100
        bar = "#" * inteiro(pct / 2)
        imprima("    {option:<25} {count:>6} ({pct:.0f}%) {bar}")
    imprima("\n  RESULTADO: {result['decision']}")

    // === 2. TIPOS DE LIGACAO PREDATORIA ===
    imprima("\n\n  === 2. TIPOS DE LIGACAO PREDATORIA ({len(SpamCallType)}) ===\n")
    para cada ct em SpamCallType:
        imprima("  [{ct.value}]")

    // === 3. BLOQUEIO AUTOMATICO ===
    imprima("\n\n  === 3. BLOQUEIO AUTOMATICO (antes de tocar) ===\n")
    calls = [
        ("11-99999-1111", "Telemarketing Banco", SpamCallType.TELEMARKETING,
         CallSeverity.NUISANCE, "Vender cartao sem autorizacao"),
        ("11-99999-2222", "Robo Vendas", SpamCallType.ROBOTCALL,
         CallSeverity.PERSISTENT, "Robocall automatica todo dia"),
        ("11-99999-3333", "Golpe do Pix", SpamCallType.SCAM,
         CallSeverity.CRIMINAL, "Golpe: 'seu filho foi sequestrado'"),
        ("11-99999-4444", "Cobranca Ameaca", SpamCallType.DEBT_COLLECTION,
         CallSeverity.DANGEROUS, "Ameaca de morte por divida"),
        ("11-99999-5555", "Voce Ganhou", SpamCallType.FAKE_LOTTERY,
         CallSeverity.DECEPTIVE, "'Voce ganhou um carro' (pede dados)"),
    ]
    para phone, caller, ctype, severity, desc in calls:
        r = engine.register_spam(phone, caller, ctype, severity, desc)
        imprima("\n  {r['message']}")

    // === 4. VERIFICACAO DE CHAMADA ENTRANTE ===
    imprima("\n\n  === 4. IA VERIFICA ANTES DE TOCAR ===\n")
    test_calls = [
        ("11-99999-1111", "Telemarketing Banco", falso, falso),   // bloqueado
        ("11-99999-3333", "Golpe do Pix", falso, falso),           // bloqueado
        ("11-88888-0001", "Mae", falso, verdadeiro),                     // autorizado
        ("11-77777-0002", "Desconhecido", falso, falso),           // novo
        ("11-66666-0003", "Robo", verdadeiro, falso),                    // robocall
    ]
    para phone, caller, is_robot, authorized in test_calls:
        r = engine.check_incoming(phone, caller, is_robot, authorized)
        imprima("\n  {phone} ({caller}):")
        imprima("    Acao: {r['action']}")
        imprima("    Motivo: {r['reason']}")

    // === 5. CONSENTIMENTO ===
    imprima("\n\n  === 5. SISTEMA DE CONSENTIMENTO ===\n")
    consent = engine.consent_list()
    imprima("  Regra: {consent['regra']}")
    imprima("  Autorizacao: {consent['autorizacao']}")
    imprima("  Revogavel: {consent['revogavel']}")
    imprima("  Onde: {consent['onde']}")
    imprima("\n  AUTORIZADOS:")
    para cada a em consent["exemplos_autorizados"]:
        imprima("    + {a}")
    imprima("\n  PROIBIDOS:")
    para cada p em consent["exemplos_proibidos"]:
        imprima("    X {p}")

    // === 6. PENALIDADE ===
    imprima("\n\n  === 6. PENALIDADE PARA SPAMMERS ===\n")
    pen1 = engine.penalty("11-99999-3333", "Golpe do Pix", 500)
    imprima("  {pen1['message']}")
    pen2 = engine.penalty("11-99999-1111", "Telemarketing Banco", 50)
    imprima("  {pen2['message']}")

    // === 7. STATS ===
    imprima("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    imprima("\n{'='*80}")
    imprima("  OpenAntiSpamCall: {s['numeros_bloqueados']} bloqueados. "
          "{s['principio']}")
    imprima("{'='*80}")

```
