// OpenAbsence -- Direito de Ausencia Protegido -- gerado de Portugol++
public class OpenabsenceDireitoDeAusenciaProtegido {

    // !/usr/bin/env python3
    //
    OpenAbsence -- Direito de Ausencia Protegido;
    ==============================================;
    "Necessidades medicas && pessoais de ausencia sao DIREITO.;
    Devem ser respeitadas por TODOS. Independentemente da situacao.;
    Ninguem precisa explicar POR QUE. Ninguem precisa JUSTIFICAR.;
    A Republica PROTEGE. A Republica RESPETA.";
    ASSEMBLEIA CONSTITUINTE CONVOCADA:;
    PERGUNTA: "Ausencias medicas && pessoais devem ser direito protegido?";
    RESPOSTA: APROVADO. Direito inalienavel.;
    O QUE ISTO FAZ:;
    1. Define 8 tipos de ausencia protegida;
    2. Estabelece que NINGUEM precisa explicar;
    3. Protege contra penalizacao por ausencia;
    4. Garante cobertura (OpenLaborRelay cobre);
    5. Integra com OpenHealth, OpenPsychology, OpenFamily;
    PRINCIPIO (P2):;
    O corpo && soberano. Se precisa ausentar, ausenta.;
    A mente && soberana. Se precisa pausa, pausa.;
    A familia && soberana. Se precisa estar com familia, esta.;
    Ninguem tem direito de questionar.;
    A Republica garante o DIREITO && a COBERTURA.;
    Author: OpenRepublic Team;
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
    public static class AbsenceType {
        MEDICAL = "medica";
        MENTAL_HEALTH = "saude_mental";
        FAMILY = "familia";
        BEREAVEMENT = "luto";
        PERSONAL = "pessoal";
        REST = "descanso";
        EMERGENCY = "emergencia";
        MATERNITY_PATERNITY = "maternidade_paternidade";
    public static class AbsenceDuration {
        // Duracao automaticamente aprovada (sem necessidade de explicar).
        FEW_HOURS = ("algumas_horas", 4)  // ate 4h;
        ONE_DAY = ("um_dia", 8)  // 1 dia;
        FEW_DAYS = ("alguns_dias", 24)  // 3 dias;
        ONE_WEEK = ("uma_semana", 40)  // 1 semana;
        TWO_WEEKS = ("duas_semanas", 80)  // 2 semanas;
        INDEFINITE = ("indefinida", -1)  // ate quando precisar;
    public static class AbsenceStatus {
        REQUESTED = "solicitada";
        AUTO_APPROVED = "auto_aprovada"  // ! precisa de aprovacao;
        ACTIVE = "ativa";
        RETURNED = "retornou";
        EXTENDED = "prorrogada"  // precisou mais tempo;
    // ============================================================================
    // 2. AUSENCIA REGISTRADA
    // ============================================================================
    // decorador: @dataclass
    public static class ProtectedAbsence {
        // Uma ausencia protegida pela Republica.
        DIFERENCA vs sistema atual:;
        - Atual: precisa atestado, prova, explicacao, chefe aprova.;
        - Republica: VOCE avisa. PONTO. Ninguem questiona.;
        - Atual: ausencia penalizada (desconto, atraso, demissao).;
        - Republica: ausencia PROTEGIDA. Sem penalidade. Cobertura garante.;
        //
        absence_id: texto;
        citizen_id: texto;
        citizen_name: texto;
        absence_type: AbsenceType;
        AbsenceDuration duration = AbsenceDuration.FEW_HOURS;
        AbsenceStatus status = AbsenceStatus.AUTO_APPROVED;
        String start_date = "";
        String end_date = "";
        double hours_away = 0.0;
        // PRIVACIDADE (P2)
        boolean explanation_provided = false // ! precisa explicar;
        boolean explanation_kept_private = true // se explicou, && PRIVADO;
        String visible_to_others = "ausente"  // so mostra "ausente";
        // Cobertura
        boolean coverage_assigned = false // OpenLaborRelay cobriu?;
        String coverage_by = ""  // quem cobriu;
        // Protecao
        boolean penalized = false // NUNCA. Lei.;
        boolean credit_affected = false // NUNCA. Lei.;
        boolean reputation_affected = false // NUNCA. Lei.;
        // decorador: @property
        public boolean is_protected(self) {
            return (self.status in (AbsenceStatus.AUTO_APPROVED, AbsenceStatus.ACTIVE);
                    && ! self.penalized);
    // ============================================================================
    // 3. VOTACAO DA ASSEMBLEIA
    // ============================================================================
    public {texto: qualquer} run_absence_assembly(n_voters: inteiro = 10000) {
        // Assembleia vota direito de ausencia.
        votes_protect = 0 // SIM -- direito protegido;
        votes_conditional = 0 // SIM mas com condicoes;
        votes_against = 0 // !;
        /* TODO: for-each Java para _ em intervalo(n_voters) */
            r = random.random();
            if (r < 0.88) {
                votes_protect = votes_protect + 1 // 88% -- proteger sem condicoes;
            } else if (r < 0.97) {
                votes_conditional = votes_conditional + 1 // 9% -- com condicoes;
            } else {
                votes_against = votes_against + 1 // 3% -- contra;
        return {;
            "question": (;
                "Necessidades medicas && pessoais de ausencia devem ser ";
                "DIREITO PROTEGIDO, respeitadas por todos, ";
                "independentemente da situacao?";
            ),;
            "votes_protect": votes_protect,;
            "votes_conditional": votes_conditional,;
            "votes_against": votes_against,;
            "total": n_voters,;
            votes_protect + votes_conditional > n_voters * 0.9 ? "result": "APROVADO" : "APROVADO",;
            "pct_protect": "{votes_protect/n_voters*100:.0f}%",;
            "decision": {
                "ausencia_e_direito": true,               // APROVADO (88%);
                "nao_precisa_explicar": true,              // APROVADO;
                "nao_penalizada": true,                    // APROVADO;
                "cobertura_garantida": true,               // APROVADO;
                "explicacao_e_privada": true,              // APROVADO;
                "ausencia_medica": true,                   // APROVADO;
                "ausencia_saude_mental": true,             // APROVADO;
                "ausencia_familiar": true,                 // APROVADO;
                "ausencia_luto": true,                     // APROVADO;
                "ausencia_pessoal": true,                  // APROVADO;
                "ausencia_descanso": true,                 // APROVADO;
                "ausencia_emergencia": true,               // APROVADO;
                "maternidade_paternidade": true,           // APROVADO;
                "visivel_a_outros": "so 'ausente'",        // sem detalhe;
                "tempo_limite": "indefinido (ate precisar)",;
                "credito_afetado": false,                  // NUNCA;
                "reputacao_afetada": false,                // NUNCA;
            },;
        };
    // ============================================================================
    // 4. MOTOR DE AUSENCIA PROTEGIDA
    // ============================================================================
    public static class AbsenceEngine {
        // Motor que protege ausencias na Republica.
        COMO FUNCIONA:;
        1. Cidadao AVISA que vai se ausentar (! pede permissao);
        2. Sistema AUTO-APROVA (sem chefe, sem aprovador);
        3. OpenLaborRelay COBRE (alguem assume tarefas);
        4. Ninguem ve o MOTIVO (so "ausente");
        5. Sem penalidade. Sem desconto. Sem julgamento.;
        6. Quando voltar: bem-vindo de volta. Sem cobranca.;
        O QUE && PROTEGIDO:;
        - Medica: tratamento, cirurgia, recuperacao, exame;
        - Saude mental: pausa mental, terapia, descanso psicologico;
        - Familiar: filho doente, parente, evento familiar;
        - Luto: morte de ente querido (tempo que precisar);
        - Pessoal: motivo pessoal (! PRECISA EXPLICAR);
        - Descanso: pausa, ferias, respiro;
        - Emergencia: situacao urgente;
        - Maternidade/Paternidade: nascimento, adocao;
        O QUE ! EXISTE:;
        - Atestado medico obrigatorio;
        - Chefe aprovando ausencia;
        - Desconto no salario/credito;
        - "Falta" no prontuario;
        - Pressao para voltar cedo;
        - Culpa por se ausentar;
        O QUE EXISTE:;
        - Aviso simples ("vou me ausentar");
        - Auto-aprovacao imediata;
        - Cobertura automatica (OpenLaborRelay);
        - Privacidade total do motivo;
        - Retorno sem cobranca;
        - Bem-vindo de volta;
        //
        public void __init__(self) {
            self.absences: {texto: ProtectedAbsence} = {};
            self.stats_total: inteiro = 0;
            self.stats_medical: inteiro = 0;
            self.stats_mental: inteiro = 0;
            self.stats_family: inteiro = 0;
        funcao request_absence(self, citizen_id: texto, citizen_name: texto,
                            absence_type: AbsenceType,;
                            AbsenceDuration duration = AbsenceDuration.FEW_HOURS,;
                            String explanation = "",;
                            boolean provide_explanation = false;
                            ) -> {texto: qualquer}:;
            // Cidadao solicita ausencia. AUTO-APROVADA.
            aid = hashlib.md5(;
                "{citizen_id}{absence_type.value}{datetime.now()}".encode();
            ).hexdigest()[:8];
            absence = ProtectedAbsence(;
                absence_id = aid, citizen_id=citizen_id, citizen_name=citizen_name,;
                absence_type = absence_type, duration=duration,;
                status = AbsenceStatus.AUTO_APPROVED,;
                start_date = datetime.now().isoformat(),;
                explanation_provided = provide_explanation,;
                explanation_kept_private = true,;
                visible_to_others = "ausente",;
            );
            self.absences[aid] = absence;
            self.stats_total += 1;
            if (absence_type == AbsenceType.MEDICAL) {
                self.stats_medical += 1;
            } else if (absence_type == AbsenceType.MENTAL_HEALTH) {
                self.stats_mental += 1;
            } else if (absence_type == AbsenceType.FAMILY) {
                self.stats_family += 1;
            // Cobertura
            coverage = self._assign_coverage(citizen_id, absence_type);
            return {;
                "absence_id": aid,;
                "citizen": citizen_name,;
                "status": "AUTO-APROVADA",;
                "type": absence_type.value,;
                "duration": duration.value[0],;
                "visible_to_others": "ausente",;
                "explanation_required": false,;
                "explanation_provided": provide_explanation,;
                provide_explanation ? "explanation_privacy": "PRIVADA (se fornecida)" : "N/A",;
                "coverage": coverage,;
                "penalized": false,;
                "credit_affected": false,;
                "message": (;
                    "{citizen_name}: ausencia {absence_type.value} AUTO-APROVADA. ";
                    "Ninguem ve o motivo. So veem 'ausente'. ";
                    "Sem penalidade. Sem desconto. Cobertura garantida. ";
                    "Volte quando estiver pronto. Bem-vindo de volta.";
                ),;
            };
        funcao _assign_coverage(self, citizen_id: texto,
                            absence_type: AbsenceType) -> {texto: qualquer}:;
            // OpenLaborRelay cobre a ausencia.
            return {;
                "covered": true,;
                "by": "OpenLaborRelay (sistema automatico)",;
                "method": (;
                    "Tarefas redistribuidas para proximo disponivel. ";
                    "Se ninguem disponivel: tarefa espera. ";
                    "Ninguem && obrigado a assumir trabalho alheio.";
                ),;
                "message": "Cobertura garantida. Ninguem sobrecarregado.",;
            };
        public {texto: qualquer} check_status(self, citizen_id: texto) {
            // Verifica status de um cidadao (o que outros veem).
            active = [a para a em self.absences.values();
                    if a.citizen_id == citizen_id;
                    && a.status in (AbsenceStatus.AUTO_APPROVED, AbsenceStatus.ACTIVE)];
            if (active) {
                return {;
                    "citizen": active[0].citizen_name,;
                    "status": "AUSENTE",;
                    "visible_info": "ausente",;
                    "reason_visible": "NENHUMA (privado)",;
                    "expected_return": "quando estiver pronto",;
                    "coverage": "GARANTIDA",;
                    "message": (;
                        "{active[0].citizen_name} esta AUSENTE. ";
                        "Motivo: PROTEGIDO (voce ! precisa saber). ";
                        "Volta quando estiver pronto. Respeite.";
                    ),;
                };
            return {;
                "citizen": citizen_id,;
                "status": "DISPONIVEL",;
                "message": "Cidadao disponivel.",;
            };
        public {texto: qualquer} return_from_absence(self, absence_id: texto) {
            // Cidadao retorna de ausencia.
            absence = self.absences.get(absence_id);
            if (! absence) {
                return {"error": "Ausencia ! encontrada"};
            absence.status = AbsenceStatus.RETURNED;
            absence.end_date = datetime.now().isoformat();
            return {;
                "citizen": absence.citizen_name,;
                "status": "RETORNOU",;
                "welcome": (;
                    "Bem-vindo de volta, {absence.citizen_name}. ";
                    "Sem cobranca. Sem 'onde voce estava'. ";
                    "Sem 'precisa recuperar tempo'. ";
                    "Voce esta de volta. Isso basta.";
                ),;
                "penalty": "NENHUMA",;
                "credit_impact": "NENHUM",;
                "message": (;
                    "{absence.citizen_name} retornou. ";
                    "Sem perguntas. Sem pressao. Bem-vindo.";
                ),;
            };
        funcao extend_absence(self, absence_id: texto,
                        new_duration: AbsenceDuration) -> {texto: qualquer}:;
            // Cidadao precisa de mais tempo. AUTO-APROVADO.
            absence = self.absences.get(absence_id);
            if (! absence) {
                return {"error": "Ausencia ! encontrada"};
            absence.duration = new_duration;
            absence.status = AbsenceStatus.EXTENDED;
            return {;
                "citizen": absence.citizen_name,;
                "status": "PRORROGADA",;
                "new_duration": new_duration.value[0],;
                "explanation_required": false,;
                "message": (;
                    "{absence.citizen_name}: ausencia prorrogada. ";
                    "Sem perguntas. Precisa de mais tempo? Tem. ";
                    "A Republica espera. Sem pressa.";
                ),;
            };
        funcao violation_report(self, citizen: texto,
                            violation: texto) -> {texto: qualquer}:;
            // Alguem penalizou/desrespeitou ausencia -> VIOLACAO.
            return {;
                "citizen": citizen,;
                "violation": violation,;
                "type": "VIOLACAO DE DIREITO",;
                "consequence": (;
                    "Quem penalizou/desrespeitou ausencia protegida COMETE VIOLACAO. ";
                    "OpenCivicEducation: acompanhamento civico. ";
                    "Se recorrente: OpenPenalRevision. ";
                    "Ausencia protegida && LEI. Nao sugestao.";
                ),;
                "law": (;
                    "Constituicao da Republica: Ausencia medica && pessoal ";
                    "&& DIREITO PROTEGIDO. Assembleia aprovou (88%). ";
                    "Penalizar ausencia && INCONSTITUCIONAL.";
                ),;
            };
        public {texto: qualquer} stats(self) {
            return {;
                "total_ausencias": self.stats_total,;
                "medicas": self.stats_medical,;
                "saude_mental": self.stats_mental,;
                "familiares": self.stats_family,;
                "penalizadas": 0,     // NUNCA;
                "credito_afetado": 0,   // NUNCA;
                "auto_aprovadas": self.stats_total,   // 100%;
            };
    // ============================================================================
    // 5. MAIN
    // ============================================================================
    if (__name__ == "__main__") {
        engine = AbsenceEngine();
        System.out.println("=" * 80);
        System.out.println("  OPENABSENCE -- DIREITO DE AUSENCIA PROTEGIDO");
        System.out.println("  Assembleia Constituinte: ausencia && direito. Sem perguntas.");
        System.out.println("=" * 80);
        // === 1. ASSEMBLEIA ===
        System.out.println("\n\n  === 1. ASSEMBLEIA CONSTITUINTE ===\n");
        result = run_absence_assembly(10000);
        System.out.println("  PERGUNTA: {result['question']}");
        System.out.println("\n  PROTEGER (sem condicoes):  {result['votes_protect']:>6} ({result['pct_protect']})");
        System.out.println("  COM CONDICOES:              {result['votes_conditional']:>6} ({result['votes_conditional']/100:.0f}%)");
        System.out.println("  CONTRA:                     {result['votes_against']:>6} ({result['votes_against']/100:.0f}%)");
        System.out.println("\n  RESULTADO: {result['result']}");
        System.out.println("\n  DECISAO DA ASSEMBLEIA:");
        /* para cada (key, val) em result["decision"].items(): */
            if (isinstance(val, logico)) {
                System.out.println("    {key:<35} {'SIM' if val else 'NAO'}");
            } else {
                System.out.println("    {key:<35} {val}");
        // === 2. SOLICITAR AUSENCIAS ===
        System.out.println("\n\n  === 2. SOLICITANDO AUSENCIAS (auto-aprovadas) ===\n");
        absences_data = [;
            ("C-001", "Cleiton", AbsenceType.MEDICAL, AbsenceDuration.ONE_DAY),;
            ("C-002", "Maria", AbsenceType.MENTAL_HEALTH, AbsenceDuration.FEW_DAYS),;
            ("C-003", "Joao", AbsenceType.FAMILY, AbsenceDuration.ONE_DAY),;
            ("C-004", "Ana", AbsenceType.PERSONAL, AbsenceDuration.FEW_HOURS),;
            ("C-005", "Pedro", AbsenceType.BEREAVEMENT, AbsenceDuration.INDEFINITE),;
            ("C-006", "Beatriz", AbsenceType.MATERNITY_PATERNITY, AbsenceDuration.TWO_WEEKS),;
        ];
        /* para cid, name, atype, dur in absences_data: */
            r = engine.request_absence(cid, name, atype, dur);
            System.out.println("\n  {r['citizen']:<12} -> {r['type']:<20} {r['duration']:<15} ";
                "[{r['status']}]");
            System.out.println("    Visivel: '{r['visible_to_others']}'  Penalizada: {r['penalized']}");
            System.out.println("    Cobertura: {r['coverage']['covered']}");
        // === 3. VERIFICAR STATUS (o que outros veem) ===
        System.out.println("\n\n  === 3. O QUE OUTROS VEEM (privacidade) ===\n");
        /* TODO: for-each Java para cid em ["C-001", "C-002", "C-005", "C-999"] */
            status = engine.check_status(cid);
            System.out.println("  {status.get('citizen', cid):<12} -> {status['status']}");
            if ("message" in status  &&  "ausente" in status.get("status", "").lower()) {
                System.out.println("    {status['message'][:70]}");
        // === 4. RETORNAR DE AUSENCIA ===
        System.out.println("\n\n  === 4. RETORNANDO DE AUSENCIA ===\n");
        // Pegar primeiras 2 ausencias
        aids = list(engine.absences.keys())[:2];
        /* TODO: for-each Java para aid em aids */
            r = engine.return_from_absence(aid);
            System.out.println("  {r['citizen']:<12} -> {r['status']}");
            System.out.println("    {r['welcome'][:70]}");
        // === 5. PRORROGAR ===
        System.out.println("\n\n  === 5. PRORROGANDO (precisa de mais tempo) ===\n");
        if (tamanho(aids) >= 3) {
            r = engine.extend_absence(aids[2], AbsenceDuration.ONE_WEEK);
            System.out.println("  {r['citizen']:<12} -> {r['status']} ({r['new_duration']})");
            System.out.println("    {r['message'][:70]}");
        // === 6. VIOLACAO ===
        System.out.println("\n\n  === 6. VIOLACAO (alguem desrespeitou) ===\n");
        viol = engine.violation_report(;
            "Supervisor Carlos",;
            "Cobrou explicacao de ausencia medica de Maria + pressao para voltar");
        System.out.println("  QUEM: {viol['citizen']}");
        System.out.println("  O QUE: {viol['violation']}");
        System.out.println("  TIPO: {viol['type']}");
        System.out.println("  CONSEQUENCIA: {viol['consequence'][:80]}");
        System.out.println("  LEI: {viol['law'][:80]}");
        // === 7. COMPARACAO ===
        System.out.println("\n\n  === 7. SISTEMA ATUAL vs REPUBLICA ===\n");
        comparisons = [;
            ("Aprovacao", "Chefe aprova", "AUTO-APROVADA (ninguem aprova)"),;
            ("Explicacao", "Atestado + prova + justificativa", "NAO PRECISA EXPLICAR"),;
            ("Visibilidade", "Setor sabe o motivo", "So ve 'ausente'"),;
            ("Penalidade", "Desconto, falta, demissao", "NENHUMA (lei)"),;
            ("Credito/salario", "Descontado", "NAO AFETADO"),;
            ("Pressao p/ voltar", "Cobra retorno", "Sem pressao. Volta quando pronto."),;
            ("Cobertura", "Colega sobrecarregado", "OpenLaborRelay redistribui"),;
            ("Luto", "3 dias (lei atual)", "Tempo que precisar"),;
            ("Saude mental", "Falta justificada", "DIREITO (sem estigma)"),;
            ("Maternidade", "4 meses (lei)", "Tempo que precisar"),;
        ];
        System.out.println("  {'Aspecto':<20} {'Sistema Atual':<35} {'Republica'}");
        System.out.println("  {'-'*80}");
        /* para aspect, atual, rep in comparisons: */
            System.out.println("  {aspect:<20} {atual:<35} {rep}");
        // === 8. STATS ===
        System.out.println("\n\n  === 8. ESTATISTICAS ===\n");
        s = engine.stats();
        /* para cada (k, v) em s.items(): */
            System.out.println("  {k:<25} {v}");
        // === FILOSOFIA ===
        System.out.println("\n\n{'='*80}");
        System.out.println("  FILOSOFIA: DIREITO DE AUSENCIA");
        System.out.println("{'='*80}");
        System.out.println(""";
    ASSEMBLEIA APROVOU (88%):;
        Ausencia medica && pessoal && DIREITO PROTEGIDO.;
        Respeitada por TODOS. Independentemente da situacao.;
    8 TIPOS DE AUSENCIA PROTEGIDA:;
        1. MEDICA: tratamento, cirurgia, exame, recuperacao;
        2. SAUDE MENTAL: pausa mental, terapia, descanso psicologico;
        3. FAMILIAR: filho doente, parente, evento familiar;
        4. LUTO: morte de ente querido (TEMPO QUE PRECISAR);
        5. PESSOAL: motivo pessoal (! PRECISA EXPLICAR);
        6. DESCANSO: pausa, ferias, respiro;
        7. EMERGENCIA: situacao urgente;
        8. MATERNIDADE/PATERNIDADE: nascimento, adocao (TEMPO QUE PRECISAR);
    O QUE && PROTEGIDO:;
        - ! PRECISA EXPLICAR (P2 privacidade);
        - ! PRECISA ATESTADO;
        - ! PENALIZADA (credito, reputacao, prontuario);
        - COBERTURA GARANTIDA (OpenLaborRelay);
        - VISIVEL SO COMO 'AUSENTE' (sem motivo);
        - VOLTA QUANDO ESTIVER PRONTO (sem pressao);
    O QUE ! EXISTE MAIS:;
        - Chefe aprovando ausencia;
        - Atestado obrigatorio;
        - "Falta" no prontuario;
        - Desconto no credito/salario;
        - Pressao para voltar cedo;
        - Culpa por se ausentar;
        - Colega sobrecarregado;
    O QUE EXISTE:;
        - AVISO ("vou me ausentar");
        - AUTO-APROVACAO imediata;
        - COBERTURA automatica;
        - PRIVACIDADE total do motivo;
        - RETORNO sem cobranca;
        - BEM-VINDO DE VOLTA;
    LUTO && TEMPO QUE PRECISAR:;
        Sistema atual: 3 dias de luto (lei). Absurdo.;
        Quem perdeu pai/mae/filho precisa de 3 dias?;
        Republica: tempo INDEFINIDO. Luto ! tem prazo.;
        Volta quando o coracao permitir.;
    MATERNIDADE/PATERNIDADE:;
        Sistema atual: 4-6 meses. Depois? Creche cara.;
        Republica: tempo que precisar. OpenFamilyLabor ajuda.;
        Filho pequeno precisa dos pais? Pais ficam.;
    SAUDE MENTAL:;
        Sistema atual: falta justificada (estigma).;
        Republica: DIREITO. Pausa mental && saude.;
        Sem julgamento. Sem rotulagem (OpenPsychology).;
    VIOLACAO:;
        Se alguem penalizar/desrespeitar ausencia protegida:;
        - OpenCivicEducation: acompanhamento civico;
        - Se recorrente: OpenPenalRevision;
        - Ausencia protegida && LEI. Nao sugestao.;
    PRINCIPIOS:;
        P1: Direito igual para todos. Sem excecao para cargo/funcao.;
        P2: Corpo && mente soberanos. Ninguem explica o que faz com o corpo.;
        P3: Cobertura por OpenLaborRelay. Ninguem sobrecarregado.;
        P4: Assembleia votou (88%). Direito inalienavel.;
    // )
        System.out.println("{'='*80}");
        System.out.println("  OpenAbsence: {s['total_ausencias']} ausencias protegidas. ";
            "Penalizadas: {s['penalizadas']}. Credito afetado: {s['credito_afetado']}.");
        System.out.println("  Ausencia && direito. Sem perguntas. Sem pressao.");
        System.out.println("{'='*80}");
}
