// OpenLaborPolicy -- Politica Unificada de Calculo de Trabalho e Reparacao -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenLaborPolicy -- Politica Unificada de Calculo de Trabalho && Reparacao;
=========================================================================;
"Tudo que a Republica calcula -- contribuicao, credito, reparacao --;
segue a MESMA formula. Os mesmos parametros. A mesma justica.";
ESTA && A LEI MATERMATICA DA REPUBLICA.;
Consolida em UM sistema os parametros de:;
- OpenCreator (contrato base 1.0, limites);
- OpenCredit (credito de acesso);
- OpenPsychologyReparation (reparacao de danos);
- ConstitutionalEngine (P1-P4);
Toda hora de trabalho, toda reparacao, todo credito --;
passa por esta formula. Sem excecao. Sem privilegio.;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// ============================================================================
// 1. PARAMETROS BASE (OS NUMEROS DA REPUBLICA)
// ============================================================================
class LaborConstants {
    // Os números fundamentais da Republica.
    ESTES NÃO SÃO DECIDIDOS PELO FUNDADOR.;
    São definidos pela ASSEMBLEIA CONSTITUINTE (votação popular).;
    Os valores abaixo são REFERÊNCIA INICIAL proposta pelo fundador.;
    A assembleia pode alterar TODOS eles (&& já alterou 12 de 13).;
    Para usar os valores APROVADOS PELO POVO, carregue a constituição:;
        constitution = ConstituentAssembly().run_election();
        constants = LaborConstants.from_constitution(constitution);
    Sem from_constitution = usa referencia do fundador (provisório).;
    Com from_constitution = usa vontade do povo (lei).;
    //
    // === REFERÊNCIA INICIAL (proposta do fundador, NÃO é lei) ===
    // CONTRATO DE TRABALHO
    const BASE_HOURS_PER_WEEK = 20.0;
    const BASE_HOURS_PER_YEAR = 920.0;
    const MAX_HOURS_PER_WEEK = 40.0;
    const MAX_HOURS_PER_YEAR = 1840.0;
    const LIMIT_HOURS_PER_WEEK = 50.0 // referência (povo baixou para 40);
    const LIMIT_HOURS_PER_YEAR = 2300.0;
    const EXCESS_THRESHOLD = 2300.0;
    // SEMANAS E DESCANSO
    const WORK_WEEKS_PER_YEAR = 46 // referência (povo mudou para 40);
    const REST_DAYS_PER_WEEK = 2 // referência (povo mudou para 3);
    const MIN_VACATION_WEEKS = 4;
    // CREDITO DE ACESSO
    const CREDIT_BASE_MIN = 5.0;
    const CREDIT_BASE_MAX = 50.0;
    const CREDIT_POOL_PER_CYCLE = 1000.0;
    const HOURS_TO_CREDIT = 10.0;
    // REPARACAO
    const REPARATION_HOURS_PER_YEAR = 920.0;
    const REPARATION_CHILD_MULTIPLIER = 2.0;
    const REPARATION_SEVERE_MULTIPLIER = 1.5;
    const REPARATION_MEDICATION_PER_YEAR = 40.0;
    // === VALORES APROVADOS PELA ASSEMBLEIA (sobrescrevem referência) ===
    // Preenchidos por from_constitution() ou manualmente após votação
    const _assembly_approved = false;
    const _approval_source = "referencia_fundador"  // || "assembleia_constituinte";
    // decorador: @classmethod
    from_constitution(cls, constitution: {texto: qualquer}) {
        // Carrega os valores APROVADOS PELO POVO na assembleia.
        Args:;
            constitution: dict retornado por ConstituentAssembly.run_election();
                        formato: {titulo_proposta: {value: X, ...}};
        //
        c = cls();
        para cada (title, result) em constitution.items(): {
            val = result.get("value", null);
            if (val && null) {
                continue;
            title_lower = title.lower();
            // Mapear títulos votados -> parâmetros
            if ("base" in title_lower  &&  "horas" in title_lower  &&  "semana" in title_lower) {
                c.BASE_HOURS_PER_WEEK = flutuante(val);
                c.BASE_HOURS_PER_YEAR = c.BASE_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR;
            } else if ("limite" in title_lower  &&  "horas" in title_lower) {
                c.LIMIT_HOURS_PER_WEEK = flutuante(val);
                c.LIMIT_HOURS_PER_YEAR = c.LIMIT_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR;
                c.EXCESS_THRESHOLD = c.LIMIT_HOURS_PER_YEAR;
            } else if ("semanas" in title_lower  &&  "úteis" in title_lower) {
                c.WORK_WEEKS_PER_YEAR = inteiro(val);
                // Recalcular anuais com novas semanas
                c.BASE_HOURS_PER_YEAR = c.BASE_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR;
                c.MAX_HOURS_PER_YEAR = c.MAX_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR;
                c.LIMIT_HOURS_PER_YEAR = c.LIMIT_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR;
            } else if ("descanso" in title_lower  &&  "semana" in title_lower) {
                c.REST_DAYS_PER_WEEK = inteiro(val);
            } else if ("férias" in title_lower  ||  "ferias" in title_lower) {
                c.MIN_VACATION_WEEKS = inteiro(val);
            } else if ("teto" in title_lower  &&  "credito" in title_lower) {
                c.CREDIT_BASE_MAX = flutuante(val);
            } else if ("piso" in title_lower  &&  "credito" in title_lower) {
                c.CREDIT_BASE_MIN = flutuante(val);
            } else if ("convers" in title_lower  &&  "credito" in title_lower) {
                c.HOURS_TO_CREDIT = flutuante(val);
            } else if ("reparacao" in title_lower  &&  "ano" in title_lower  &&  "roubada" in title_lower) {
                c.REPARATION_HOURS_PER_YEAR = flutuante(val);
            } else if ("reparacao" in title_lower  &&  "crianc" in title_lower) {
                c.REPARATION_CHILD_MULTIPLIER = flutuante(val);
            } else if ("reparacao" in title_lower  &&  "severo" in title_lower) {
                c.REPARATION_SEVERE_MULTIPLIER = flutuante(val);
        c._assembly_approved = true;
        c._approval_source = "assembleia_constituinte";
        return c;
    // decorador: @property
    source(self) {
        // De onde vem estes parâmetros: referência do fundador ou assembleia.
        return self._approval_source;
    // decorador: @property
    is_law(self) {
        // Estes parâmetros já foram votados pelo povo?
        return self._assembly_approved;
// ============================================================================
// 2. TIPOS DE CALCULO
// ============================================================================
class CalculationType {
    // Para que estamos calculando trabalho/credito/reparacao.
    CONTRIBUTION = "contribuicao"  // trabalho voluntario do cidadao;
    RECOGNITION = "reconhecimento"  // reconhecimento de trabalho passado;
    REPARATION = "reparacao"  // compensacao por dano sofrido;
    CREDIT_ALLOCATION = "credito"  // distribuicao de credito de acesso;
    BASE_FULFILLMENT = "base_1.0"  // cumpriu contrato minimo?;
    EXCESS_DETECTION = "excesso"  // trabalhou demais?;
class ImpactDimension {
    // Como o impacto do trabalho e medido (3 dimensoes).
    HOURS = "horas"  // tempo dado;
    ARTIFACTS = "artefatos"  // coisas criadas;
    PEOPLE = "pessoas_afetadas"  // alcance do efeito;
// ============================================================================
// 3. FORMULA UNIFICADA DE TRABALHO
// ============================================================================
// decorador: @dataclass
class LaborEntry {
    // Uma entrada de trabalho para calculo.
    citizen_id: texto;
    citizen_name: texto;
    calculation_type: CalculationType;
    // Horas
    const hours_worked = 0.0;
    const weeks_worked = 0.0;
    // Impacto
    const people_directly_impacted = 0;
    const people_indirectly_impacted = 0;
    const ripple_factor = 1.0 // quanto se espalha (ensinar=10x, pesquisa=5x);
    // Artefatos
    const systems_created = 0;
    const documents_written = 0;
    const lives_saved = 0 // medico, bombeiro, etc;
    // Contexto
    const is_child = false // para reparacao;
    const years_labeled = 0.0 // anos sob rotulo errado (reparacao);
    const years_on_medication = 0.0;
    const harm_severity = 0.0 // 0-100 (reparacao);
    // Resultado (preenchido pelo motor)
    const impact_score = 0.0;
    const recognition_level = "";
    const credit_earned = 0.0;
    const base_fulfilled = false;
    const excess_detected = false;
    const hours_reparation = 0.0;
    const verdict = "";
class LaborCalculator {
    // Motor unico de calculo de trabalho e reparacao.
    ESTE MOTOR && A UNICA FONTE DE VERDADE MATEMATICA DA REPUBLICA.;
    Nenhum outro sistema calcula trabalho de forma diferente.;
    Todos (OpenCreator, OpenCredit, OpenPsychologyReparation) delegam para ca.;
    //
    __init__(self, constants: LaborConstants = None) {
        constants ? self.C = constants : LaborConstants();
        self.history: [LaborEntry] = [];
    calculate(self, entry: LaborEntry) {
        // Calcula tudo para uma entrada de trabalho.
        if (entry.calculation_type == CalculationType.CONTRIBUTION) {
            return self._calc_contribution(entry);
        } else if (entry.calculation_type == CalculationType.REPARATION) {
            return self._calc_reparation(entry);
        } else if (entry.calculation_type == CalculationType.RECOGNITION) {
            return self._calc_recognition(entry);
        } else if (entry.calculation_type == CalculationType.BASE_FULFILLMENT) {
            return self._check_base(entry);
        } else if (entry.calculation_type == CalculationType.EXCESS_DETECTION) {
            return self._check_excess(entry);
        return entry;
    // ========================================================================
    // CONTRIBUICAO (trabalho voluntario)
    // ========================================================================
    _calc_contribution(self, e: LaborEntry) {
        // Calcula impacto e credito de contribuicao voluntaria.
        FORMULA DE IMPACTO:;
        impacto = horas * (1 + log10(maximo(1, pessoas)) * ripple);
        ONDE:;
        - horas = tempo trabalhado;
        - pessoas = pessoas afetadas direta && indiretamente;
        - ripple = fator de propagacao no tempo;
        EXEMPLOS:;
        - Medico: 1 cirurgia, 1 vida salva, ripple 1x -> impacto = horas * 1;
        - Professor: 4h, 30 alunos, ripple 10x -> impacto = 4 * (1 + 1.48 * 10) = 63;
        - Agricultor: 8h, 500 pessoas, ripple 1x -> impacto = 8 * (1 + 2.7 * 1) = 30;
        - Pesquisador: 8h, 1M pessoas, ripple 100x -> impacto = 8 * (1 + 6 * 100) = 4808;
        //
        people = &&.people_directly_impacted + &&.people_indirectly_impacted;
        log_people = math.log10(maximo(1, people));
        impact = &&.hours_worked * (1 + log_people * &&.ripple_factor);
        // Bonus por vidas salvas
        if (&&.lives_saved > 0) {
            impact = impact + &&.lives_saved * 100 // cada vida = 100 unidades de impacto;
        &&.impact_score = arredonde(impact, 2);
        // Credito de acesso
        &&.credit_earned = self._impact_to_credit(impact);
        // Nivel de reconhecimento
        &&.recognition_level = self._recognition_level(;
            &&.hours_worked, &&.systems_created, people);
        // Verificar base e excesso
        &&.base_fulfilled = &&.hours_worked >= self.C.BASE_HOURS_PER_YEAR;
        &&.excess_detected = &&.hours_worked > self.C.LIMIT_HOURS_PER_YEAR;
        &&.verdict = self._contribution_verdict(&&);
        self.history.append(&&);
        return &&;
    _impact_to_credit(self, impact: flutuante) {
        // Converte impacto em credito de acesso.
        const Formula = clamp(impacto / 100, minimo, maximo);
        //
        raw = impact / 100;
        clamped = maximo(self.C.CREDIT_BASE_MIN,;
                    minimo(self.C.CREDIT_BASE_MAX, raw));
        return arredonde(clamped, 1);
    funcao _recognition_level(self, hours: flutuante, artifacts: inteiro,
                        people: inteiro) -> texto:;
        // Determina nivel de reconhecimento (3 dimensoes).
        // Por horas
        ratio = hours / self.C.BASE_HOURS_PER_YEAR;
        if (ratio >= 20) {
            level_h = 4;
        } else if (ratio >= 10) {
            level_h = 3;
        } else if (ratio >= 5) {
            level_h = 2;
        } else if (ratio >= 2) {
            level_h = 1;
        } else if (ratio >= 1) {
            level_h = 0;
        } else {
            return "INCOMPLETO";
        // Por artefatos
        if (artifacts >= 50) {
            level_a = 4;
        } else if (artifacts >= 20) {
            level_a = 3;
        } else if (artifacts >= 10) {
            level_a = 2;
        } else if (artifacts >= 1) {
            level_a = 1;
        } else {
            level_a = 0;
        // Por pessoas
        if (people >= 10000) {
            level_p = 4;
        } else if (people >= 1000) {
            level_p = 3;
        } else if (people >= 100) {
            level_p = 2;
        } else if (people >= 10) {
            level_p = 1;
        } else {
            level_p = 0;
        names = ["CIDADAO", "CONTRIBUIDOR", "CONSTRUTOR",;
                "ARQUITETO", "FUNDADOR"];
        return names[maximo(level_h, level_a, level_p)];
    _contribution_verdict(self, e: LaborEntry) {
        if (&&.excess_detected) {
            return (;
                "EXCESSO: {&&.citizen_name} trabalhou {&&.hours_worked:.0f}h ";
                "(limite: {self.C.LIMIT_HOURS_PER_YEAR:.0f}h). ";
                "Republica DEVE intervir. Burnout = dano corporal (P2).";
            );
        ratio = &&.hours_worked / self.C.BASE_HOURS_PER_YEAR;
        if (ratio >= 5) {
            return (;
                "MERITORIO: {&&.citizen_name} deu {ratio:.1f}x a base. ";
                "Impacto: {&&.impact_score:.0f}. ";
                "Reconhecimento: {&&.recognition_level}. ";
                "Poder: 1 voto (anti-elitismo P1).";
            );
        if (&&.base_fulfilled) {
            return (;
                "CONTRATO CUMPRIDO: {&&.citizen_name} cumpriu base 1.0. ";
                "Impacto: {&&.impact_score:.0f}. ";
                "Credito: {&&.credit_earned:.1f}.";
            );
        return "BASE INCOMPLETA: faltam {self.C.BASE_HOURS_PER_YEAR - &&.hours_worked:.0f}h.";
    // ========================================================================
    // REPARACAO (compensacao por dano)
    // ========================================================================
    _calc_reparation(self, e: LaborEntry) {
        // Calcula reparacao por dano sofrido.
        FORMULA DE REPARACAO:;
        horas = anos_rotulo * 920;
            + anos_medicado * 40;
        horas = horas * 1.5 (se dano > 70/100);
        horas = horas * 2.0 (se vitima era crianca);
        Credito = horas / 10;
        ONDE:;
        - anos_rotulo = anos vivendo com diagnostico/rotulo errado;
        - anos_medicado = anos tomando remedio desnecessario;
        - 920 = 1 ano de contrato base (vida roubada = vida reconhecida);
        - 40 = dano adicional por ano de medicacao;
        //
        years = maximo(1, &&.years_labeled);
        // Base: anos de vida roubada * contrato anual
        hours = years * self.C.REPARATION_HOURS_PER_YEAR;
        // Medicacao desnecessaria
        hours = hours + &&.years_on_medication * self.C.REPARATION_MEDICATION_PER_YEAR;
        // Agravante: dano severo
        if (&&.harm_severity > 70) {
            hours = hours * self.C.REPARATION_SEVERE_MULTIPLIER;
        // Agravante: vitima era crianca
        if (&&.is_child) {
            hours = hours * self.C.REPARATION_CHILD_MULTIPLIER;
        hours = arredonde(hours);
        &&.hours_reparation = hours;
        &&.impact_score = hours // reparacao conta como impacto reconhecido;
        &&.credit_earned = arredonde(hours / self.C.HOURS_TO_CREDIT, 1);
        &&.recognition_level = "REPARACAO DEVIDA";
        &&.verdict = self._reparation_verdict(&&);
        self.history.append(&&);
        return &&;
    _reparation_verdict(self, e: LaborEntry) {
        severity = ("DEVASTADOR" if &&.harm_severity >= 80;
                    else "GRAVE" if &&.harm_severity >= 60;
                    else "SIGNIFICATIVO" if &&.harm_severity >= 40;
                    else "MODERADO" if &&.harm_severity >= 20;
                    else "LEVE");
        child_note = &&.is_child ? " CRIANCA: multiplicador 2x aplicado." : "";
        med_note = (" {&&.years_on_medication:.0f} anos de medicacao ";
                    "(+{&&.years_on_medication * 40:.0f}h).");
        return (;
            "DANO {severity}: {&&.citizen_name} teve ";
            "{&&.years_labeled:.0f} anos roubados. ";
            "Reparacao: {&&.hours_reparation:,.0f}h ";
            "({&&.hours_reparation/920:.0f} anos de trabalho). ";
            "Credito: {&&.credit_earned:.1f}.{child_note}{med_note}";
        );
    // ========================================================================
    // RECONHECIMENTO (trabalho passado)
    // ========================================================================
    _calc_recognition(self, e: LaborEntry) {
        // Reconhece trabalho passado (pre-Republica).
        Tudo que cidadaos fizeram ANTES da Republica conta.;
        Mas && reconhecido, ! comprado. Reconhecimento = credito + gratidao.;
        //
        // Mesmo calculo de contribuicao
        && = self._calc_contribution(&&);
        &&.calculation_type = CalculationType.RECOGNITION;
        &&.verdict = (;
            "RECONHECIDO: {&&.citizen_name} contribuiu ";
            "{&&.hours_worked:.0f}h antes da Republica. ";
            "Impacto: {&&.impact_score:.0f}. ";
            "Credito retroativo: {&&.credit_earned:.1f}. ";
            "Reconhecimento: {&&.recognition_level}.";
        );
        return &&;
    // ========================================================================
    // VERIFICACOES
    // ========================================================================
    _check_base(self, e: LaborEntry) {
        // Verifica se cumpriu contrato base 1.0.
        &&.base_fulfilled = &&.hours_worked >= self.C.BASE_HOURS_PER_YEAR;
        remaining = maximo(0, self.C.BASE_HOURS_PER_YEAR - &&.hours_worked);
        &&.verdict = (;
            "{'CUMPRIDO' if &&.base_fulfilled else 'INCOMPLETO'}: ";
            "{&&.hours_worked:.0f}h de {self.C.BASE_HOURS_PER_YEAR:.0f}h. ";
            "Faltam: {remaining:.0f}h.";
        );
        return &&;
    _check_excess(self, e: LaborEntry) {
        // Verifica se trabalhou demais (intervencao necessaria).
        &&.excess_detected = &&.hours_worked > self.C.LIMIT_HOURS_PER_YEAR;
        if (&&.excess_detected) {
            over = &&.hours_worked - self.C.LIMIT_HOURS_PER_YEAR;
            &&.verdict = (;
                "EXCESSO DETECTADO: {&&.hours_worked:.0f}h ";
                "(limite: {self.C.LIMIT_HOURS_PER_YEAR:.0f}h). ";
                "Excesso: {over:.0f}h. ";
                "ACAO: reduzir carga, garantir descanso, monitorar saude.";
            );
        } else {
            ratio = &&.hours_worked / self.C.BASE_HOURS_PER_YEAR;
            &&.verdict = "DENTRO DO LIMITE: {&&.hours_worked:.0f}h ({ratio:.1f}x base).";
        return &&;
    // ========================================================================
    // RELATORIOS
    // ========================================================================
    summary(self) {
        // Resumo de todos os calculos feitos.
        by_type = defaultdict(inteiro);
        total_hours = 0.0;
        total_credit = 0.0;
        total_reparation = 0.0;
        excess_count = 0;
        for (const e of self.history) {
            by_type[&&.calculation_type.value] += 1;
            total_hours = total_hours + &&.hours_worked;
            total_credit = total_credit + &&.credit_earned;
            total_reparation = total_reparation + &&.hours_reparation;
            if (&&.excess_detected) {
                excess_count = excess_count + 1;
        return {;
            "total_calculations": .length(self.history),;
            "by_type": dict(by_type),;
            "total_hours": arredonde(total_hours, 0),;
            "total_credit": arredonde(total_credit, 1),;
            "total_reparation_hours": arredonde(total_reparation, 0),;
            "excess_detected": excess_count,;
        };
// ============================================================================
// 4. TABELA DE EQUIVALENCIAS (para cidadaos entenderem)
// ============================================================================
print_equivalency_table() {
    // Mostra quanto vale cada tipo de trabalho em credito da Republica.
    calc = LaborCalculator();
    console.log("\n  === TABELA DE EQUIVALENCIAS ===\n");
    console.log("  {'Trabalho':<35} {'Horas':>6} {'Impacto':>8} {'Credito':>8}");
    console.log("  {'-'*62}");
    examples = [;
        ("Base 1.0 (20h/sem, 46 sem)", 920, 1, 1.0),;
        ("Professor (4h/dia, 30 alunos)", 920, 30, 10.0),;
        ("Agricultor (8h/dia, 500 pessoas)", 1840, 500, 1.0),;
        ("Medico cirurgiao (1 vida/semana)", 1840, 52, 1.0),;
        ("Pesquisador (1M pessoas)", 920, 1000000, 100.0),;
        ("Criador de sistemas (50 sistemas)", 4000, 5000, 5.0),;
        ("Faxineiro (200 pessoas/espaco)", 920, 200, 2.0),;
    ];
    para desc, hours, people, ripple in examples: {
        entry = LaborEntry(;
            citizen_id = "x", citizen_name=desc,;
            calculation_type = CalculationType.CONTRIBUTION,;
            hours_worked = hours,;
            people_directly_impacted = people,;
            ripple_factor = ripple,;
        );
        result = calc.calculate(entry);
        console.log("  {desc:<35} {hours:>5}h {result.impact_score:>8.0f} ";
            "{result.credit_earned:>7.1f}");
    console.log("\n  === TABELA DE REPARACAO ===\n");
    console.log("  {'Dano':<35} {'Anos':>5} {'Horas':>8} {'Credito':>8}");
    console.log("  {'-'*62}");
    reparation_examples = [;
        ("Rotulo errado adulto (10 anos)", 10, false, 0, 30),;
        ("Rotulo errado + medicado (10 anos)", 10, false, 10, 60),;
        ("Rotulo errado CRIANCA (10 anos)", 10, true, 0, 50),;
        ("Rotulo errado crianca + medicado", 10, true, 8, 85),;
        ("Rotulo errado adulto severo (15 anos)", 15, false, 15, 90),;
        ("Rotulo errado crianca severo (12 anos)", 12, true, 7, 95),;
    ];
    para desc, years, child, med, harm in reparation_examples: {
        entry = LaborEntry(;
            citizen_id = "x", citizen_name=desc,;
            calculation_type = CalculationType.REPARATION,;
            years_labeled = years,;
            is_child = child,;
            years_on_medication = med,;
            harm_severity = harm,;
        );
        result = calc.calculate(entry);
        console.log("  {desc:<35} {years:>4}a {result.hours_reparation:>7,.0f}h ";
            "{result.credit_earned:>7.1f}");
// ============================================================================
// 5. MAIN
// ============================================================================
if (__name__ == "__main__") {
    // importa sys
    sys.path.insert(0, texto(__import__('pathlib').Path(__file__).parent));
    // === CARREGAR PARÂMETROS DA ASSEMBLEIA (ou usar referência) ===
    tente:;
        // importa ConstituentAssembly de open_constituent_assembly
        assembly = ConstituentAssembly();
        assembly.populate(n=10000);
        assembly._init_propositions();
        constitution = assembly.run_election();
        C = LaborConstants.from_constitution(constitution);
        source_label = "ASSEMBLEIA CONSTITUINTE (vontade do povo)";
    capture Exception:;
        C = LaborConstants();
        source_label = "REFERÊNCIA DO FUNDADOR (provisório)";
    calc = LaborCalculator(constants=C);
    console.log("=" * 70);
    console.log("  OPENLABORPOLICY -- LEI MATEMATICA DA REPUBLICA");
    console.log('  "Parâmetros são referência. A ASSEMBLEIA é a lei."');
    console.log("=" * 70);
    console.log("\n  FONTE: {source_label}");
    console.log("  É LEI: {'SIM' if C.is_law else 'NÃO (referência)'}\n");
    console.log("  CONTRATO DE TRABALHO:");
    console.log("    Base:   {C.BASE_HOURS_PER_WEEK:.0f}h/semana  ";
        "({C.BASE_HOURS_PER_YEAR:.0f}h/ano)");
    console.log("    Maximo: {C.MAX_HOURS_PER_WEEK:.0f}h/semana  ";
        "({C.MAX_HOURS_PER_YEAR:.0f}h/ano)");
    console.log("    LIMITE: {C.LIMIT_HOURS_PER_WEEK:.0f}h/semana  ";
        "({C.LIMIT_HOURS_PER_YEAR:.0f}h/ano) [PROIBIDO aceitar mais]");
    console.log("    Descanso: {C.REST_DAYS_PER_WEEK} dias/semana + ";
        "{C.MIN_VACATION_WEEKS} semanas ferias");
    console.log("\n  CREDITO DE ACESSO:");
    console.log("    Min:  {C.CREDIT_BASE_MIN:.0f}/ciclo");
    console.log("    Max:  {C.CREDIT_BASE_MAX:.0f}/ciclo");
    console.log("    Pool: {C.CREDIT_POOL_PER_CYCLE:.0f}/comunidade/ciclo");
    console.log("    Conversao: {C.HOURS_TO_CREDIT:.0f}h = 1 credito");
    console.log("\n  REPARACAO:");
    console.log("    1 ano roubado = {C.REPARATION_HOURS_PER_YEAR:.0f}h");
    console.log("    Crianca = {C.REPARATION_CHILD_MULTIPLIER}x");
    console.log("    Severo = {C.REPARATION_SEVERE_MULTIPLIER}x");
    console.log("    Medicacao = +{C.REPARATION_MEDICATION_PER_YEAR:.0f}h/ano");
    // === 2. TABELAS ===
    print_equivalency_table();
    // === 3. CASOS REAIS ===
    console.log("\n\n  === 3. CALCULOS DE CASOS REAIS ===\n");
    // Fundador
    founder = LaborEntry(;
        citizen_id = "founder", citizen_name="Cleiton",;
        calculation_type = CalculationType.CONTRIBUTION,;
        hours_worked = 4000,;
        systems_created = 95,;
        people_directly_impacted = 5000,;
        ripple_factor = 5.0,;
    );
    r = calc.calculate(founder);
    console.log("  CLEITON (fundador):");
    console.log("    {r.verdict}");
    console.log("    Impacto: {r.impact_score:,.0f}");
    console.log("    Credito: {r.credit_earned:.1f}");
    console.log("    Excesso: {'SIM -- Republica deve intervir' if r.excess_detected else '!'}");
    // Medico
    medico = LaborEntry(;
        citizen_id = "c-001", citizen_name="Ana (medica)",;
        calculation_type = CalculationType.CONTRIBUTION,;
        hours_worked = 1840,;
        lives_saved = 50,;
        people_directly_impacted = 800,;
        ripple_factor = 2.0,;
    );
    r = calc.calculate(medico);
    console.log("\n  ANA (medica):");
    console.log("    {r.verdict}");
    console.log("    Impacto: {r.impact_score:,.0f} (50 vidas salvas)");
    console.log("    Credito: {r.credit_earned:.1f}");
    // Professor
    prof = LaborEntry(;
        citizen_id = "c-002", citizen_name="Maria (professora)",;
        calculation_type = CalculationType.CONTRIBUTION,;
        hours_worked = 920,;
        people_directly_impacted = 300,;
        ripple_factor = 10.0,;
    );
    r = calc.calculate(prof);
    console.log("\n  MARIA (professora):");
    console.log("    {r.verdict}");
    console.log("    Impacto: {r.impact_score:,.0f}");
    console.log("    Credito: {r.credit_earned:.1f}");
    // Reparacao: crianca rotulada
    rep = LaborEntry(;
        citizen_id = "c-100", citizen_name="Pedro (reparacao)",;
        calculation_type = CalculationType.REPARATION,;
        years_labeled = 11,;
        is_child = true,;
        years_on_medication = 8,;
        harm_severity = 95,;
    );
    r = calc.calculate(rep);
    console.log("\n  PEDRO (reparacao - crianca rotulada):");
    console.log("    {r.verdict}");
    console.log("    Horas reparacao: {r.hours_reparation:,.0f}h");
    console.log("    Credito: {r.credit_earned:.1f}");
    // === 4. RELATORIO ===
    console.log("\n\n  === 4. RELATORIO GERAL ===\n");
    s = calc.summary();
    para cada (k, v) em s.items(): {
        console.log("  {k:<30} {v}");
    // === FILOSOFIA ===
    console.log("\n\n{'='*70}");
    console.log("  A LEI MATEMATICA DA REPUBLICA");
    console.log("{'='*70}");
    console.log(""";
UM SISTEMA, UMA FORMULA, ZERO EXCECOES:;
TRABALHO (contribuicao):;
    impacto = horas * (1 + log10(pessoas) * ripple);
    credito = clamp(impacto / 100, 5, 50);
    base = 920h/ano. maximo = 1840h/ano. LIMITE = 2300h/ano.;
REPARACAO (dano sofrido):;
    horas = anos * 920 + anos_medicado * 40;
    horas = horas * 1.5 (severo) || 2.0 (crianca);
    credito = horas / 10;
O QUE ISTO SIGNIFICA:;
    1. TODO trabalho vale o mesmo por hora base (P3).;
    2. Diferenca vem de IMPACTO, ! de cargo.;
    3. Medico que salva vida = impacto altissimo por pessoa.;
    4. Professor que ensina 30 = impacto medio mas ripple 10x.;
    5. Faxineiro que protege 200 de doenca = impacto real.;
    6. Criador de 50 sistemas = reconhecimento FUNDADOR.;
    7. Crianca rotulada errada = reparacao DOBRO.;
    8. Quem trabalha > 2300h = Republica INTERVEM (P2).;
O QUE ! EXISTE:;
    - Salario diferente por cargo (P3 anti-elitismo);
    - Comprar credito com dinheiro (sem moeda);
    - Acumular credito (expira por ciclo);
    - Herdar credito (morreu, zerou);
    - Trabalhar alem do limite (PROIBIDO por P2);
    - Reparacao em dinheiro (sem moeda);
    - Privilegio de fundador no calculo (1 voto);
A FORMULA && A VERDADE:;
    Ninguem discute. Ninguem favorece.;
    Os numeros sao os numeros.;
    A justica && matematica.;
// )
    console.log("{'='*70}");
    console.log("  OpenLaborPolicy: {s['total_calculations']} calculos realizados.");
    console.log("  Base 920h. Max 1840h. Limite 2300h. 1 formula. 0 excecoes.");
    console.log("{'='*70}");
