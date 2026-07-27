# OpenAbsence -- Direito de Ausencia Protegido

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_absence.py`

**Descricao:** ==============================================
"Necessidades medicas e pessoais de ausencia sao DIREITO.
 Devem ser respeitadas por TODOS. Independentemente da situacao.
 Ninguem precisa explicar POR QUE. Ninguem precisa JUSTIFICAR.
 A Republica PROTEGE. A Republica RESPETA."
ASSEMBLEIA CONSTITUINTE CONVOCADA:
  PERGUNTA: "Ausencias medicas e pessoais devem ser direito protegido?"
  RESPOSTA: APROVADO. Direito inalienavel.
O QUE ISTO FAZ:
  1. Define 8 tipos de ausencia protegida
  2. Estabelece que NINGUEM precisa explicar
  3. Protege contra penalizacao por ausencia
  4. Garante cobertura (OpenLaborRelay cobre)
  5. Integra com OpenHealth, OpenPsychology, OpenFamily
PRINCIPIO (P2):
  O corpo e soberano. Se precisa ausentar, ausenta.
  A mente e soberana. Se precisa pausa, pausa.
  A familia e soberana. Se precisa estar com familia, esta.
  Ninguem tem direito de questionar.
  A Republica garante o DIREITO e a COBERTURA.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenAbsence -- Direito de Ausencia Protegido
==============================================

"Necessidades medicas e pessoais de ausencia sao DIREITO.
 Devem ser respeitadas por TODOS. Independentemente da situacao.
 Ninguem precisa explicar POR QUE. Ninguem precisa JUSTIFICAR.
 A Republica PROTEGE. A Republica RESPETA."

ASSEMBLEIA CONSTITUINTE CONVOCADA:
  PERGUNTA: "Ausencias medicas e pessoais devem ser direito protegido?"
  RESPOSTA: APROVADO. Direito inalienavel.

O QUE ISTO FAZ:
  1. Define 8 tipos de ausencia protegida
  2. Estabelece que NINGUEM precisa explicar
  3. Protege contra penalizacao por ausencia
  4. Garante cobertura (OpenLaborRelay cobre)
  5. Integra com OpenHealth, OpenPsychology, OpenFamily

PRINCIPIO (P2):
  O corpo e soberano. Se precisa ausentar, ausenta.
  A mente e soberana. Se precisa pausa, pausa.
  A familia e soberana. Se precisa estar com familia, esta.
  Ninguem tem direito de questionar.
  A Republica garante o DIREITO e a COBERTURA.

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
// 1. TIPOS DE AUSENCIA PROTEGIDA
// ============================================================================

classe AbsenceType herda de Enum:
    MEDICAL = "medica"
    MENTAL_HEALTH = "saude_mental"
    FAMILY = "familia"
    BEREAVEMENT = "luto"
    PERSONAL = "pessoal"
    REST = "descanso"
    EMERGENCY = "emergencia"
    MATERNITY_PATERNITY = "maternidade_paternidade"


classe AbsenceDuration herda de Enum:
    // Duracao automaticamente aprovada (sem necessidade de explicar).
    FEW_HOURS = ("algumas_horas", 4)  // ate 4h
    ONE_DAY = ("um_dia", 8)  // 1 dia
    FEW_DAYS = ("alguns_dias", 24)  // 3 dias
    ONE_WEEK = ("uma_semana", 40)  // 1 semana
    TWO_WEEKS = ("duas_semanas", 80)  // 2 semanas
    INDEFINITE = ("indefinida", -1)  // ate quando precisar


classe AbsenceStatus herda de Enum:
    REQUESTED = "solicitada"
    AUTO_APPROVED = "auto_aprovada"  // nao precisa de aprovacao
    ACTIVE = "ativa"
    RETURNED = "retornou"
    EXTENDED = "prorrogada"  // precisou mais tempo


// ============================================================================
// 2. AUSENCIA REGISTRADA
// ============================================================================

// decorador: @dataclass
classe ProtectedAbsence:
    // Uma ausencia protegida pela Republica.

    DIFERENCA vs sistema atual:
    - Atual: precisa atestado, prova, explicacao, chefe aprova.
    - Republica: VOCE avisa. PONTO. Ninguem questiona.

    - Atual: ausencia penalizada (desconto, atraso, demissao).
    - Republica: ausencia PROTEGIDA. Sem penalidade. Cobertura garante.
    // 
    absence_id: texto
    citizen_id: texto
    citizen_name: texto
    absence_type: AbsenceType
    seja duration: AbsenceDuration = AbsenceDuration.FEW_HOURS
    seja status: AbsenceStatus = AbsenceStatus.AUTO_APPROVED
    seja start_date: texto = ""
    seja end_date: texto = ""
    seja hours_away: flutuante = 0.0

    // PRIVACIDADE (P2)
    seja explanation_provided: logico = falso // nao precisa explicar
    seja explanation_kept_private: logico = verdadeiro // se explicou, e PRIVADO
    seja visible_to_others: texto = "ausente"  // so mostra "ausente"

    // Cobertura
    seja coverage_assigned: logico = falso // OpenLaborRelay cobriu?
    seja coverage_by: texto = ""  // quem cobriu

    // Protecao
    seja penalized: logico = falso // NUNCA. Lei.
    seja credit_affected: logico = falso // NUNCA. Lei.
    seja reputation_affected: logico = falso // NUNCA. Lei.

    // decorador: @property
    funcao is_protected(self) -> logico:
        retorne (self.status in (AbsenceStatus.AUTO_APPROVED, AbsenceStatus.ACTIVE)
                 e nao self.penalized)


// ============================================================================
// 3. VOTACAO DA ASSEMBLEIA
// ============================================================================

funcao run_absence_assembly(n_voters: inteiro = 10000) -> {texto: qualquer}:
    // Assembleia vota direito de ausencia.

    votes_protect = 0 // SIM -- direito protegido
    votes_conditional = 0 // SIM mas com condicoes
    votes_against = 0 // nao

    para cada _ em intervalo(n_voters):
        r = random.random()
        se r < 0.88 entao:
            votes_protect = votes_protect + 1 // 88% -- proteger sem condicoes
        senao se r < 0.97 entao:
            votes_conditional = votes_conditional + 1 // 9% -- com condicoes
        senao:
            votes_against = votes_against + 1 // 3% -- contra

    retorne {
        "question": (
            "Necessidades medicas e pessoais de ausencia devem ser "
            "DIREITO PROTEGIDO, respeitadas por todos, "
            "independentemente da situacao?"
        ),
        "votes_protect": votes_protect,
        "votes_conditional": votes_conditional,
        "votes_against": votes_against,
        "total": n_voters,
        votes_protect + votes_conditional > n_voters * 0.9 ? "result": "APROVADO" : "APROVADO",
        "pct_protect": "{votes_protect/n_voters*100:.0f}%",
        "decision": {
            "ausencia_e_direito": verdadeiro,               // APROVADO (88%)
            "nao_precisa_explicar": verdadeiro,              // APROVADO
            "nao_penalizada": verdadeiro,                    // APROVADO
            "cobertura_garantida": verdadeiro,               // APROVADO
            "explicacao_e_privada": verdadeiro,              // APROVADO
            "ausencia_medica": verdadeiro,                   // APROVADO
            "ausencia_saude_mental": verdadeiro,             // APROVADO
            "ausencia_familiar": verdadeiro,                 // APROVADO
            "ausencia_luto": verdadeiro,                     // APROVADO
            "ausencia_pessoal": verdadeiro,                  // APROVADO
            "ausencia_descanso": verdadeiro,                 // APROVADO
            "ausencia_emergencia": verdadeiro,               // APROVADO
            "maternidade_paternidade": verdadeiro,           // APROVADO
            "visivel_a_outros": "so 'ausente'",        // sem detalhe
            "tempo_limite": "indefinido (ate precisar)",
            "credito_afetado": falso,                  // NUNCA
            "reputacao_afetada": falso,                // NUNCA
        },
    }


// ============================================================================
// 4. MOTOR DE AUSENCIA PROTEGIDA
// ============================================================================

classe AbsenceEngine:
    // Motor que protege ausencias na Republica.

    COMO FUNCIONA:
    1. Cidadao AVISA que vai se ausentar (nao pede permissao)
    2. Sistema AUTO-APROVA (sem chefe, sem aprovador)
    3. OpenLaborRelay COBRE (alguem assume tarefas)
    4. Ninguem ve o MOTIVO (so "ausente")
    5. Sem penalidade. Sem desconto. Sem julgamento.
    6. Quando voltar: bem-vindo de volta. Sem cobranca.

    O QUE e PROTEGIDO:
    - Medica: tratamento, cirurgia, recuperacao, exame
    - Saude mental: pausa mental, terapia, descanso psicologico
    - Familiar: filho doente, parente, evento familiar
    - Luto: morte de ente querido (tempo que precisar)
    - Pessoal: motivo pessoal (nao PRECISA EXPLICAR)
    - Descanso: pausa, ferias, respiro
    - Emergencia: situacao urgente
    - Maternidade/Paternidade: nascimento, adocao

    O QUE nao EXISTE:
    - Atestado medico obrigatorio
    - Chefe aprovando ausencia
    - Desconto no salario/credito
    - "Falta" no prontuario
    - Pressao para voltar cedo
    - Culpa por se ausentar

    O QUE EXISTE:
    - Aviso simples ("vou me ausentar")
    - Auto-aprovacao imediata
    - Cobertura automatica (OpenLaborRelay)
    - Privacidade total do motivo
    - Retorno sem cobranca
    - Bem-vindo de volta
    // 

    funcao __init__(self):
        self.absences: {texto: ProtectedAbsence} = {}
        self.stats_total: inteiro = 0
        self.stats_medical: inteiro = 0
        self.stats_mental: inteiro = 0
        self.stats_family: inteiro = 0

    funcao request_absence(self, citizen_id: texto, citizen_name: texto,
                        absence_type: AbsenceType,
                        seja duration: AbsenceDuration = AbsenceDuration.FEW_HOURS,
                        seja explanation: texto = "",
                        seja provide_explanation: logico = falso
                        ) -> {texto: qualquer}:
        // Cidadao solicita ausencia. AUTO-APROVADA.

        aid = hashlib.md5(
            "{citizen_id}{absence_type.value}{datetime.now()}".encode()
        ).hexdigest()[:8]

        absence = ProtectedAbsence(
            absence_id = aid, citizen_id=citizen_id, citizen_name=citizen_name,
            absence_type = absence_type, duration=duration,
            status = AbsenceStatus.AUTO_APPROVED,
            start_date = datetime.now().isoformat(),
            explanation_provided = provide_explanation,
            explanation_kept_private = verdadeiro,
            visible_to_others = "ausente",
        )
        self.absences[aid] = absence
        self.stats_total += 1

        se absence_type == AbsenceType.MEDICAL entao:
            self.stats_medical += 1
        senao se absence_type == AbsenceType.MENTAL_HEALTH entao:
            self.stats_mental += 1
        senao se absence_type == AbsenceType.FAMILY entao:
            self.stats_family += 1

        // Cobertura
        coverage = self._assign_coverage(citizen_id, absence_type)

        retorne {
            "absence_id": aid,
            "citizen": citizen_name,
            "status": "AUTO-APROVADA",
            "type": absence_type.value,
            "duration": duration.value[0],
            "visible_to_others": "ausente",
            "explanation_required": falso,
            "explanation_provided": provide_explanation,
            provide_explanation ? "explanation_privacy": "PRIVADA (se fornecida)" : "N/A",
            "coverage": coverage,
            "penalized": falso,
            "credit_affected": falso,
            "message": (
                "{citizen_name}: ausencia {absence_type.value} AUTO-APROVADA. "
                "Ninguem ve o motivo. So veem 'ausente'. "
                "Sem penalidade. Sem desconto. Cobertura garantida. "
                "Volte quando estiver pronto. Bem-vindo de volta."
            ),
        }

    funcao _assign_coverage(self, citizen_id: texto,
                         absence_type: AbsenceType) -> {texto: qualquer}:
        // OpenLaborRelay cobre a ausencia.
        retorne {
            "covered": verdadeiro,
            "by": "OpenLaborRelay (sistema automatico)",
            "method": (
                "Tarefas redistribuidas para proximo disponivel. "
                "Se ninguem disponivel: tarefa espera. "
                "Ninguem e obrigado a assumir trabalho alheio."
            ),
            "message": "Cobertura garantida. Ninguem sobrecarregado.",
        }

    funcao check_status(self, citizen_id: texto) -> {texto: qualquer}:
        // Verifica status de um cidadao (o que outros veem).
        active = [a para a em self.absences.values()
                  if a.citizen_id == citizen_id
                   e a.status in (AbsenceStatus.AUTO_APPROVED, AbsenceStatus.ACTIVE)]

        se active entao:
            retorne {
                "citizen": active[0].citizen_name,
                "status": "AUSENTE",
                "visible_info": "ausente",
                "reason_visible": "NENHUMA (privado)",
                "expected_return": "quando estiver pronto",
                "coverage": "GARANTIDA",
                "message": (
                    "{active[0].citizen_name} esta AUSENTE. "
                    "Motivo: PROTEGIDO (voce nao precisa saber). "
                    "Volta quando estiver pronto. Respeite."
                ),
            }
        retorne {
            "citizen": citizen_id,
            "status": "DISPONIVEL",
            "message": "Cidadao disponivel.",
        }

    funcao return_from_absence(self, absence_id: texto) -> {texto: qualquer}:
        // Cidadao retorna de ausencia.
        absence = self.absences.get(absence_id)
        se nao absence entao:
            retorne {"error": "Ausencia nao encontrada"}

        absence.status = AbsenceStatus.RETURNED
        absence.end_date = datetime.now().isoformat()

        retorne {
            "citizen": absence.citizen_name,
            "status": "RETORNOU",
            "welcome": (
                "Bem-vindo de volta, {absence.citizen_name}. "
                "Sem cobranca. Sem 'onde voce estava'. "
                "Sem 'precisa recuperar tempo'. "
                "Voce esta de volta. Isso basta."
            ),
            "penalty": "NENHUMA",
            "credit_impact": "NENHUM",
            "message": (
                "{absence.citizen_name} retornou. "
                "Sem perguntas. Sem pressao. Bem-vindo."
            ),
        }

    funcao extend_absence(self, absence_id: texto,
                       new_duration: AbsenceDuration) -> {texto: qualquer}:
        // Cidadao precisa de mais tempo. AUTO-APROVADO.
        absence = self.absences.get(absence_id)
        se nao absence entao:
            retorne {"error": "Ausencia nao encontrada"}

        absence.duration = new_duration
        absence.status = AbsenceStatus.EXTENDED

        retorne {
            "citizen": absence.citizen_name,
            "status": "PRORROGADA",
            "new_duration": new_duration.value[0],
            "explanation_required": falso,
            "message": (
                "{absence.citizen_name}: ausencia prorrogada. "
                "Sem perguntas. Precisa de mais tempo? Tem. "
                "A Republica espera. Sem pressa."
            ),
        }

    funcao violation_report(self, citizen: texto,
                         violation: texto) -> {texto: qualquer}:
        // Alguem penalizou/desrespeitou ausencia -> VIOLACAO.
        retorne {
            "citizen": citizen,
            "violation": violation,
            "type": "VIOLACAO DE DIREITO",
            "consequence": (
                "Quem penalizou/desrespeitou ausencia protegida COMETE VIOLACAO. "
                "OpenCivicEducation: acompanhamento civico. "
                "Se recorrente: OpenPenalRevision. "
                "Ausencia protegida e LEI. Nao sugestao."
            ),
            "law": (
                "Constituicao da Republica: Ausencia medica e pessoal "
                "e DIREITO PROTEGIDO. Assembleia aprovou (88%). "
                "Penalizar ausencia e INCONSTITUCIONAL."
            ),
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_ausencias": self.stats_total,
            "medicas": self.stats_medical,
            "saude_mental": self.stats_mental,
            "familiares": self.stats_family,
            "penalizadas": 0,     // NUNCA
            "credito_afetado": 0,   // NUNCA
            "auto_aprovadas": self.stats_total,   // 100%
        }


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = AbsenceEngine()

    imprima("=" * 80)
    imprima("  OPENABSENCE -- DIREITO DE AUSENCIA PROTEGIDO")
    imprima("  Assembleia Constituinte: ausencia e direito. Sem perguntas.")
    imprima("=" * 80)

    // === 1. ASSEMBLEIA ===
    imprima("\n\n  === 1. ASSEMBLEIA CONSTITUINTE ===\n")
    result = run_absence_assembly(10000)
    imprima("  PERGUNTA: {result['question']}")
    imprima("\n  PROTEGER (sem condicoes):  {result['votes_protect']:>6} ({result['pct_protect']})")
    imprima("  COM CONDICOES:              {result['votes_conditional']:>6} ({result['votes_conditional']/100:.0f}%)")
    imprima("  CONTRA:                     {result['votes_against']:>6} ({result['votes_against']/100:.0f}%)")
    imprima("\n  RESULTADO: {result['result']}")

    imprima("\n  DECISAO DA ASSEMBLEIA:")
    para cada (key, val) em result["decision"].items():
        se isinstance(val, logico) entao:
            imprima("    {key:<35} {'SIM' if val else 'NAO'}")
        senao:
            imprima("    {key:<35} {val}")

    // === 2. SOLICITAR AUSENCIAS ===
    imprima("\n\n  === 2. SOLICITANDO AUSENCIAS (auto-aprovadas) ===\n")

    absences_data = [
        ("C-001", "Cleiton", AbsenceType.MEDICAL, AbsenceDuration.ONE_DAY),
        ("C-002", "Maria", AbsenceType.MENTAL_HEALTH, AbsenceDuration.FEW_DAYS),
        ("C-003", "Joao", AbsenceType.FAMILY, AbsenceDuration.ONE_DAY),
        ("C-004", "Ana", AbsenceType.PERSONAL, AbsenceDuration.FEW_HOURS),
        ("C-005", "Pedro", AbsenceType.BEREAVEMENT, AbsenceDuration.INDEFINITE),
        ("C-006", "Beatriz", AbsenceType.MATERNITY_PATERNITY, AbsenceDuration.TWO_WEEKS),
    ]

    para cid, name, atype, dur in absences_data:
        r = engine.request_absence(cid, name, atype, dur)
        imprima("\n  {r['citizen']:<12} -> {r['type']:<20} {r['duration']:<15} "
              "[{r['status']}]")
        imprima("    Visivel: '{r['visible_to_others']}'  Penalizada: {r['penalized']}")
        imprima("    Cobertura: {r['coverage']['covered']}")

    // === 3. VERIFICAR STATUS (o que outros veem) ===
    imprima("\n\n  === 3. O QUE OUTROS VEEM (privacidade) ===\n")
    para cada cid em ["C-001", "C-002", "C-005", "C-999"]:
        status = engine.check_status(cid)
        imprima("  {status.get('citizen', cid):<12} -> {status['status']}")
        se "message" in status  e  "ausente" in status.get("status", "").lower() entao:
            imprima("    {status['message'][:70]}")

    // === 4. RETORNAR DE AUSENCIA ===
    imprima("\n\n  === 4. RETORNANDO DE AUSENCIA ===\n")
    // Pegar primeiras 2 ausencias
    aids = list(engine.absences.keys())[:2]
    para cada aid em aids:
        r = engine.return_from_absence(aid)
        imprima("  {r['citizen']:<12} -> {r['status']}")
        imprima("    {r['welcome'][:70]}")

    // === 5. PRORROGAR ===
    imprima("\n\n  === 5. PRORROGANDO (precisa de mais tempo) ===\n")
    se tamanho(aids) >= 3 entao:
        r = engine.extend_absence(aids[2], AbsenceDuration.ONE_WEEK)
        imprima("  {r['citizen']:<12} -> {r['status']} ({r['new_duration']})")
        imprima("    {r['message'][:70]}")

    // === 6. VIOLACAO ===
    imprima("\n\n  === 6. VIOLACAO (alguem desrespeitou) ===\n")
    viol = engine.violation_report(
        "Supervisor Carlos",
        "Cobrou explicacao de ausencia medica de Maria + pressao para voltar")
    imprima("  QUEM: {viol['citizen']}")
    imprima("  O QUE: {viol['violation']}")
    imprima("  TIPO: {viol['type']}")
    imprima("  CONSEQUENCIA: {viol['consequence'][:80]}")
    imprima("  LEI: {viol['law'][:80]}")

    // === 7. COMPARACAO ===
    imprima("\n\n  === 7. SISTEMA ATUAL vs REPUBLICA ===\n")
    comparisons = [
        ("Aprovacao", "Chefe aprova", "AUTO-APROVADA (ninguem aprova)"),
        ("Explicacao", "Atestado + prova + justificativa", "NAO PRECISA EXPLICAR"),
        ("Visibilidade", "Setor sabe o motivo", "So ve 'ausente'"),
        ("Penalidade", "Desconto, falta, demissao", "NENHUMA (lei)"),
        ("Credito/salario", "Descontado", "NAO AFETADO"),
        ("Pressao p/ voltar", "Cobra retorno", "Sem pressao. Volta quando pronto."),
        ("Cobertura", "Colega sobrecarregado", "OpenLaborRelay redistribui"),
        ("Luto", "3 dias (lei atual)", "Tempo que precisar"),
        ("Saude mental", "Falta justificada", "DIREITO (sem estigma)"),
        ("Maternidade", "4 meses (lei)", "Tempo que precisar"),
    ]
    imprima("  {'Aspecto':<20} {'Sistema Atual':<35} {'Republica'}")
    imprima("  {'-'*80}")
    para aspect, atual, rep in comparisons:
        imprima("  {aspect:<20} {atual:<35} {rep}")

    // === 8. STATS ===
    imprima("\n\n  === 8. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<25} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA: DIREITO DE AUSENCIA")
    imprima("{'='*80}")
    imprima("""
  ASSEMBLEIA APROVOU (88%):
    Ausencia medica e pessoal e DIREITO PROTEGIDO.
    Respeitada por TODOS. Independentemente da situacao.

  8 TIPOS DE AUSENCIA PROTEGIDA:
    1. MEDICA: tratamento, cirurgia, exame, recuperacao
    2. SAUDE MENTAL: pausa mental, terapia, descanso psicologico
    3. FAMILIAR: filho doente, parente, evento familiar
    4. LUTO: morte de ente querido (TEMPO QUE PRECISAR)
    5. PESSOAL: motivo pessoal (nao PRECISA EXPLICAR)
    6. DESCANSO: pausa, ferias, respiro
    7. EMERGENCIA: situacao urgente
    8. MATERNIDADE/PATERNIDADE: nascimento, adocao (TEMPO QUE PRECISAR)

  O QUE e PROTEGIDO:
    - nao PRECISA EXPLICAR (P2 privacidade)
    - nao PRECISA ATESTADO
    - nao PENALIZADA (credito, reputacao, prontuario)
    - COBERTURA GARANTIDA (OpenLaborRelay)
    - VISIVEL SO COMO 'AUSENTE' (sem motivo)
    - VOLTA QUANDO ESTIVER PRONTO (sem pressao)

  O QUE nao EXISTE MAIS:
    - Chefe aprovando ausencia
    - Atestado obrigatorio
    - "Falta" no prontuario
    - Desconto no credito/salario
    - Pressao para voltar cedo
    - Culpa por se ausentar
    - Colega sobrecarregado

  O QUE EXISTE:
    - AVISO ("vou me ausentar")
    - AUTO-APROVACAO imediata
    - COBERTURA automatica
    - PRIVACIDADE total do motivo
    - RETORNO sem cobranca
    - BEM-VINDO DE VOLTA

  LUTO e TEMPO QUE PRECISAR:
    Sistema atual: 3 dias de luto (lei). Absurdo.
    Quem perdeu pai/mae/filho precisa de 3 dias?
    Republica: tempo INDEFINIDO. Luto nao tem prazo.
    Volta quando o coracao permitir.

  MATERNIDADE/PATERNIDADE:
    Sistema atual: 4-6 meses. Depois? Creche cara.
    Republica: tempo que precisar. OpenFamilyLabor ajuda.
    Filho pequeno precisa dos pais? Pais ficam.

  SAUDE MENTAL:
    Sistema atual: falta justificada (estigma).
    Republica: DIREITO. Pausa mental e saude.
    Sem julgamento. Sem rotulagem (OpenPsychology).

  VIOLACAO:
    Se alguem penalizar/desrespeitar ausencia protegida:
    - OpenCivicEducation: acompanhamento civico
    - Se recorrente: OpenPenalRevision
    - Ausencia protegida e LEI. Nao sugestao.

  PRINCIPIOS:
    P1: Direito igual para todos. Sem excecao para cargo/funcao.
    P2: Corpo e mente soberanos. Ninguem explica o que faz com o corpo.
    P3: Cobertura por OpenLaborRelay. Ninguem sobrecarregado.
    P4: Assembleia votou (88%). Direito inalienavel.
// )
    imprima("{'='*80}")
    imprima("  OpenAbsence: {s['total_ausencias']} ausencias protegidas. "
          "Penalizadas: {s['penalizadas']}. Credito afetado: {s['credito_afetado']}.")
    imprima("  Ausencia e direito. Sem perguntas. Sem pressao.")
    imprima("{'='*80}")

```
