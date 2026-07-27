// OpenAntiSpamCall -- Ligacao Telefonica Predatoria PROIBIDA -- gerado de Portugol++
package openantispamcall_ligacao_telefonica_predatoria_proibida

import "fmt"

// !/usr/bin/env python3
//
OpenAntiSpamCall -- Ligacao Telefonica Predatoria PROIBIDA
=============================================================
"Para de me encher o saco porra.
Ninguem tem direito de ligar pra vender, enganar, cobrar
|| perturbar sem consentimento.
PROIBIDO. Ponto."
ASSEMBLEIA CONSTITUINTE CONVOCADA:
"Ligacoes telefonicas ! solicitadas devem ser PROIBIDAS?"
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
type SpamCallType int
const (
    TELEMARKETING = "telemarketing"  // vender sem consentimento
    SCAM = "golpe"  // enganar para roubar
    DEBT_COLLECTION = "cobranca_abusiva"  // ameacar devedor
    PHISHING = "phishing"  // pedir dados
    ROBOTCALL = "robô"  // ligacao automatica
    POLITICAL_SPAM = "politico"  // pedir voto
    RELIGIOUS_SPAM = "religioso"  // proselitismo
    SURVEY_SPAM = "pesquisa"  // pesquisa ! consentida
    FAKE_LOTTERY = "falsa_loteria"  // "voce ganhou"
    FAKE_FAMILY = "falsa_familia"  // "seu filho sequestrado"
    INSURANCE_SPAM = "seguro"  // vender seguro
    SOLAR_PANEL_SPAM = "painel_solar"  // vender painel (ironia)
    INVESTMENT_SCAM = "investimento"  // "renda extra"
type CallSeverity int
const (
    NUISANCE = ("aborrecimento", 1)  // incomoda mas ! dana
    PERSISTENT = ("persistente", 2)  // liga todo dia
    DECEPTIVE = ("enganoso", 3)  // mente para lucrar
    DANGEROUS = ("perigoso", 4)  // risco de golpe
    CRIMINAL = ("criminal", 5)  // golpe confirmado
// ============================================================================
// 2. REGISTRO DE LIGACAO
// ============================================================================
// decorador: @dataclass
type SpamCall struct {
    // Uma ligacao predatoria registrada.
    call_id := "" // string
    phone_number := "" // string
    caller_name := "" // string
    call_type := SpamCallType.TELEMARKETING // SpamCallType
    severity := CallSeverity.NUISANCE // CallSeverity
    description := "" // string
    timestamp := "" // string
    duration := "" // string
    victim_id := "" // string
    blocked := false // bool
    reported := true // bool
    auto_blocked := false // bool
// ============================================================================
// 3. MOTOR ANTI-SPAM
// ============================================================================
type AntiSpamCallEngine struct {
    // Motor que PROIBE e BLOQUEIA ligacoes predatorias.
    O QUE && PROIBIDO (TODOS):
    1. Telemarketing sem consentimento EXPLICITO
    2. Robocalls (ligacao automatica)
    3. Golpe / scam (qualquer tipo)
    4. Cobranca abusiva (ameaca, assedio)
    5. Phishing (pedir dados)
    6. Politico pedindo voto (sem autorizacao)
    7. Religioso sem autorizacao
    8. "Voce ganhou" (false)
    9. Qualquer ligacao ! SOLICITADA
    O QUE && PERMITIDO:
    1. Ligacao de alguem que VOCE ligou (retorno)
    2. Ligacao de familia/amigo (consentimento implicito)
    3. Emergencia (servico publico)
    4. OpenHealth (consulta marcada por VOCE)
    5. Emprego (VOCE se candidatou)
    6. Qualquer ligacao que VOCE AUTORIZOU
    COMO FUNCIONA:
    1. IA analisa chamada ANTES de tocar (caller ID + padrao)
    2. Se spam conhecido: BLOQUEIA (! toca)
    3. Se suspeito: manda pra correio voz (IA escuta)
    4. Se confirmado spam: bloqueia numero PERMANENTE
    5. Vítima NUNCA ouve o telefone tocar com spam
    CONSENTIMENTO EXPLICITO (opt-in):
    - Ninguem pode ligar sem voce AUTORIZAR
    - Autorizacao && POR EMPRESA, ! geral
    - Pode revogar a qualquer momento
    - OpenSocialNetwork tem lista de quem voce autorizou
    DENUNCIA:
    - 1 denuncia: numero marcado
    - 3 denuncias: numero bloqueado para TODA Republica
    - 10 denuncias: numero reportado como criminal
    //
    // Numeros bloqueados (base coletiva da Republica)
    blocked_numbers := field(default_factory=dict) // {texto: Dict}
    reported_numbers := field(default_factory=dict) // {texto: inteiro}
    func __init__(self) {
        self.blocked_numbers = {}
        self.reported_numbers = {}
        self.calls_blocked = 0
        self.calls_reported = 0
    funcao register_spam(self, phone: texto, caller: texto,
                    call_type: SpamCallType,
                    severity := CallSeverity.NUISANCE, // CallSeverity
                    description := "", // string
                    victim := "") -> {texto: qualquer}: // string
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
        should_block = false
        block_reason = ""
        if severity == CallSeverity.CRIMINAL {
            should_block = true
            block_reason = "CRIMINAL (golpe confirmado)"
        } else if self.reported_numbers[phone] >= 3 {
            should_block = true
            block_reason = "3+ denuncias ({self.reported_numbers[phone]})"
        elif call_type in (SpamCallType.ROBOTCALL, SpamCallType.SCAM,
                        SpamCallType.PHISHING, SpamCallType.FAKE_LOTTERY):
            should_block = true
            block_reason = "{call_type.value} (auto-bloqueado)"
        if should_block {
            self.blocked_numbers[phone] = {
                "caller": caller,
                "type": call_type.value,
                "reports": self.reported_numbers[phone],
                "blocked_date": datetime.now().isoformat(),
                "reason": block_reason,
            }
            self.calls_blocked += 1
        return {
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
                    is_robotcall := false, // bool
                    user_authorized := false // bool
                    ) -> {texto: qualquer}:
        // IA verifica chamada ANTES de tocar.
        // Usuario autorizou?
        if user_authorized {
            return {
                "phone": phone,
                "action": "PERMITIR",
                "reason": "Usuario autorizou este numero",
            }
        // Ja bloqueado?
        if phone in self.blocked_numbers {
            return {
                "phone": phone,
                "caller": self.blocked_numbers[phone]["caller"],
                "action": "BLOQUEAR",
                "reason": self.blocked_numbers[phone]["reason"],
                "message": (
                    "BLOQUEADO. {self.blocked_numbers[phone]['caller']} "
                    "({phone}) tem {self.blocked_numbers[phone]['reports']} denuncias. "
                    "Nao toca. Vitima ! ouve. Paz."
                ),
            }
        // Robocall?
        if is_robotcall {
            return {
                "phone": phone,
                "action": "BLOQUEAR",
                "reason": "Robocall (automatico) = PROIBIDO",
                "message": "Robocall bloqueada. Nao existe robocall na Republica.",
            }
        // Reportado mas nao bloqueado?
        reports = self.reported_numbers.get(phone, 0)
        if reports > 0 {
            return {
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
        return {
            "phone": phone,
            "action": "PERMITIR (primeira vez)",
            "reason": "Numero novo. Sem denuncias.",
            "message": "{phone}: numero novo. Toca normalmente. Se for spam, denuncie.",
        }
    func consent_list(self) {texto: qualquer} {
        // Lista de consentimento (opt-in).
        return {
            "regra": "NINGUEM liga sem voce AUTORIZAR",
            "autorizacao": "POR EMPRESA/PESSOA (! geral)",
            "revogavel": "A qualquer momento",
            "onde": "OpenSocialNetwork > Configuracoes > Autorizacoes",
            "exemplos_autorizados": [
                "OpenHealth (consulta que VOCE marcou)",
                "Familia/amigos (consentimento implicito)",
                "Emprego (VOCE se candidatou)",
            ],
            "exemplos_proibidos": [
                "Telemarketing (voce ! pediu)",
                "Banco cobrando (usar OpenCredit, ! telefone)",
                "Politico pedindo voto",
                "Qualquer sem autorizacao EXPLICITA",
            ],
        }
    funcao penalty(self, spammer_phone: texto, spammer_name: texto,
                n_victims: inteiro) -> {texto: qualquer}:
        // Penalidade para quem faz spam.
        if n_victims >= 100 {
            penalty = "CRIMINAL. OpenPenalRevision. Crime contra privacidade."
        } else if n_victims >= 10 {
            penalty = "OpenCivicEducation + multa (durante transicao)."
        } else {
            penalty = "Numero bloqueado PERMANENTE para toda Republica."
        return {
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
    func stats(self) {texto: qualquer} {
        return {
            "numeros_bloqueados": len(self.blocked_numbers),
            "ligacoes_reportadas": self.calls_reported,
            "ligacoes_bloqueadas": self.calls_blocked,
            "principio": "Para de me encher o saco. Ninguem liga sem autorizar.",
        }
// ============================================================================
// 4. VOTACAO DA ASSEMBLEIA
// ============================================================================
func run_spam_assembly(n_voters: inteiro = 10000) {texto: qualquer} {
    votes_ban = 0
    votes_regulate = 0
    votes_keep = 0
    for _, _ := range intervalo(n_voters) {
        r = random.random()
        if r < 0.94 {
            votes_ban = votes_ban + 1
        } else if r < 0.99 {
            votes_regulate = votes_regulate + 1
        } else {
            votes_keep = votes_keep + 1
    return {
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
            "Ligacao ! solicitada = CRIME contra privacidade."
        ),
    }
// ============================================================================
// 5. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = AntiSpamCallEngine()
    fmt.Println("=" * 80)
    fmt.Println("  OPENANTISPAMCALL -- LIGACAO PREDATORIA PROIBIDA")
    fmt.Println("  'Para de me encher o saco porra.'")
    fmt.Println("=" * 80)
    // === 1. ASSEMBLEIA ===
    fmt.Println("\n\n  === 1. ASSEMBLEIA CONSTITUINTE ===\n")
    result = run_spam_assembly(10000)
    fmt.Println("  PERGUNTA: {result['question']}\n")
    para cada (option, count) em result["votes"].items(): {
        pct = count / result["total"] * 100
        bar = "#" * inteiro(pct / 2)
        fmt.Println("    {option:<25} {count:>6} ({pct:.0f}%) {bar}")
    fmt.Println("\n  RESULTADO: {result['decision']}")
    // === 2. TIPOS DE LIGACAO PREDATORIA ===
    fmt.Println("\n\n  === 2. TIPOS DE LIGACAO PREDATORIA ({len(SpamCallType)}) ===\n")
    for _, ct := range SpamCallType {
        fmt.Println("  [{ct.value}]")
    // === 3. BLOQUEIO AUTOMATICO ===
    fmt.Println("\n\n  === 3. BLOQUEIO AUTOMATICO (antes de tocar) ===\n")
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
    para phone, caller, ctype, severity, desc in calls: {
        r = engine.register_spam(phone, caller, ctype, severity, desc)
        fmt.Println("\n  {r['message']}")
    // === 4. VERIFICACAO DE CHAMADA ENTRANTE ===
    fmt.Println("\n\n  === 4. IA VERIFICA ANTES DE TOCAR ===\n")
    test_calls = [
        ("11-99999-1111", "Telemarketing Banco", false, false),   // bloqueado
        ("11-99999-3333", "Golpe do Pix", false, false),           // bloqueado
        ("11-88888-0001", "Mae", false, true),                     // autorizado
        ("11-77777-0002", "Desconhecido", false, false),           // novo
        ("11-66666-0003", "Robo", true, false),                    // robocall
    ]
    para phone, caller, is_robot, authorized in test_calls: {
        r = engine.check_incoming(phone, caller, is_robot, authorized)
        fmt.Println("\n  {phone} ({caller}):")
        fmt.Println("    Acao: {r['action']}")
        fmt.Println("    Motivo: {r['reason']}")
    // === 5. CONSENTIMENTO ===
    fmt.Println("\n\n  === 5. SISTEMA DE CONSENTIMENTO ===\n")
    consent = engine.consent_list()
    fmt.Println("  Regra: {consent['regra']}")
    fmt.Println("  Autorizacao: {consent['autorizacao']}")
    fmt.Println("  Revogavel: {consent['revogavel']}")
    fmt.Println("  Onde: {consent['onde']}")
    fmt.Println("\n  AUTORIZADOS:")
    for _, a := range consent["exemplos_autorizados"] {
        fmt.Println("    + {a}")
    fmt.Println("\n  PROIBIDOS:")
    for _, p := range consent["exemplos_proibidos"] {
        fmt.Println("    X {p}")
    // === 6. PENALIDADE ===
    fmt.Println("\n\n  === 6. PENALIDADE PARA SPAMMERS ===\n")
    pen1 = engine.penalty("11-99999-3333", "Golpe do Pix", 500)
    fmt.Println("  {pen1['message']}")
    pen2 = engine.penalty("11-99999-1111", "Telemarketing Banco", 50)
    fmt.Println("  {pen2['message']}")
    // === 7. STATS ===
    fmt.Println("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items(): {
        fmt.Println("  {k:<30} {v}")
    fmt.Println("\n{'='*80}")
    fmt.Println("  OpenAntiSpamCall: {s['numeros_bloqueados']} bloqueados. "
        "{s['principio']}")
    fmt.Println("{'='*80}")
