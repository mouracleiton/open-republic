# OpenLaborPolicy -- Politica Unificada de Calculo de Trabalho e Reparacao

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_labor_policy.py`

**Descricao:** =========================================================================
"Tudo que a Republica calcula -- contribuicao, credito, reparacao --
 segue a MESMA formula. Os mesmos parametros. A mesma justica."
ESTA E A LEI MATERMATICA DA REPUBLICA.
Consolida em UM sistema os parametros de:
- OpenCreator (contrato base 1.0, limites)
- OpenCredit (credito de acesso)
- OpenPsychologyReparation (reparacao de danos)
- ConstitutionalEngine (P1-P4)
Toda hora de trabalho, toda reparacao, todo credito --
passa por esta formula. Sem excecao. Sem privilegio.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenLaborPolicy -- Politica Unificada de Calculo de Trabalho e Reparacao
=========================================================================

"Tudo que a Republica calcula -- contribuicao, credito, reparacao --
 segue a MESMA formula. Os mesmos parametros. A mesma justica."

ESTA e A LEI MATERMATICA DA REPUBLICA.

Consolida em UM sistema os parametros de:
- OpenCreator (contrato base 1.0, limites)
- OpenCredit (credito de acesso)
- OpenPsychologyReparation (reparacao de danos)
- ConstitutionalEngine (P1-P4)

Toda hora de trabalho, toda reparacao, todo credito --
passa por esta formula. Sem excecao. Sem privilegio.

Author: OpenRepublic Team
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

classe LaborConstants:
    // Os números fundamentais da Republica.

    ESTES NÃO SÃO DECIDIDOS PELO FUNDADOR.
    São definidos pela ASSEMBLEIA CONSTITUINTE (votação popular).

    Os valores abaixo são REFERÊNCIA INICIAL proposta pelo fundador.
    A assembleia pode alterar TODOS eles (e já alterou 12 de 13).

    Para usar os valores APROVADOS PELO POVO, carregue a constituição:
        constitution = ConstituentAssembly().run_election()
        constants = LaborConstants.from_constitution(constitution)

    Sem from_constitution = usa referencia do fundador (provisório).
    Com from_constitution = usa vontade do povo (lei).
    // 

    // === REFERÊNCIA INICIAL (proposta do fundador, NÃO é lei) ===

    // CONTRATO DE TRABALHO
    seja BASE_HOURS_PER_WEEK: flutuante = 20.0
    seja BASE_HOURS_PER_YEAR: flutuante = 920.0

    seja MAX_HOURS_PER_WEEK: flutuante = 40.0
    seja MAX_HOURS_PER_YEAR: flutuante = 1840.0

    seja LIMIT_HOURS_PER_WEEK: flutuante = 50.0 // referência (povo baixou para 40)
    seja LIMIT_HOURS_PER_YEAR: flutuante = 2300.0

    seja EXCESS_THRESHOLD: flutuante = 2300.0

    // SEMANAS E DESCANSO
    seja WORK_WEEKS_PER_YEAR: inteiro = 46 // referência (povo mudou para 40)
    seja REST_DAYS_PER_WEEK: inteiro = 2 // referência (povo mudou para 3)
    seja MIN_VACATION_WEEKS: inteiro = 4

    // CREDITO DE ACESSO
    seja CREDIT_BASE_MIN: flutuante = 5.0
    seja CREDIT_BASE_MAX: flutuante = 50.0
    seja CREDIT_POOL_PER_CYCLE: flutuante = 1000.0
    seja HOURS_TO_CREDIT: flutuante = 10.0

    // REPARACAO
    seja REPARATION_HOURS_PER_YEAR: flutuante = 920.0
    seja REPARATION_CHILD_MULTIPLIER: flutuante = 2.0
    seja REPARATION_SEVERE_MULTIPLIER: flutuante = 1.5
    seja REPARATION_MEDICATION_PER_YEAR: flutuante = 40.0

    // === VALORES APROVADOS PELA ASSEMBLEIA (sobrescrevem referência) ===
    // Preenchidos por from_constitution() ou manualmente após votação

    seja _assembly_approved: logico = falso
    seja _approval_source: texto = "referencia_fundador"  // ou "assembleia_constituinte"

    // decorador: @classmethod
    funcao from_constitution(cls, constitution: {texto: qualquer}) -> 'LaborConstants':
        // Carrega os valores APROVADOS PELO POVO na assembleia.

        Args:
            constitution: dict retornado por ConstituentAssembly.run_election()
                          formato: {titulo_proposta: {value: X, ...}}
        // 
        c = cls()

        para cada (title, result) em constitution.items():
            val = result.get("value", nulo)
            se val e nulo entao:
                continue
            title_lower = title.lower()

            // Mapear títulos votados -> parâmetros
            se "base" in title_lower  e  "horas" in title_lower  e  "semana" in title_lower entao:
                c.BASE_HOURS_PER_WEEK = flutuante(val)
                c.BASE_HOURS_PER_YEAR = c.BASE_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR

            senao se "limite" in title_lower  e  "horas" in title_lower entao:
                c.LIMIT_HOURS_PER_WEEK = flutuante(val)
                c.LIMIT_HOURS_PER_YEAR = c.LIMIT_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR
                c.EXCESS_THRESHOLD = c.LIMIT_HOURS_PER_YEAR

            senao se "semanas" in title_lower  e  "úteis" in title_lower entao:
                c.WORK_WEEKS_PER_YEAR = inteiro(val)
                // Recalcular anuais com novas semanas
                c.BASE_HOURS_PER_YEAR = c.BASE_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR
                c.MAX_HOURS_PER_YEAR = c.MAX_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR
                c.LIMIT_HOURS_PER_YEAR = c.LIMIT_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR

            senao se "descanso" in title_lower  e  "semana" in title_lower entao:
                c.REST_DAYS_PER_WEEK = inteiro(val)

            senao se "férias" in title_lower  ou  "ferias" in title_lower entao:
                c.MIN_VACATION_WEEKS = inteiro(val)

            senao se "teto" in title_lower  e  "credito" in title_lower entao:
                c.CREDIT_BASE_MAX = flutuante(val)

            senao se "piso" in title_lower  e  "credito" in title_lower entao:
                c.CREDIT_BASE_MIN = flutuante(val)

            senao se "convers" in title_lower  e  "credito" in title_lower entao:
                c.HOURS_TO_CREDIT = flutuante(val)

            senao se "reparacao" in title_lower  e  "ano" in title_lower  e  "roubada" in title_lower entao:
                c.REPARATION_HOURS_PER_YEAR = flutuante(val)

            senao se "reparacao" in title_lower  e  "crianc" in title_lower entao:
                c.REPARATION_CHILD_MULTIPLIER = flutuante(val)

            senao se "reparacao" in title_lower  e  "severo" in title_lower entao:
                c.REPARATION_SEVERE_MULTIPLIER = flutuante(val)

        c._assembly_approved = verdadeiro
        c._approval_source = "assembleia_constituinte"
        retorne c

    // decorador: @property
    funcao source(self) -> texto:
        // De onde vem estes parâmetros: referência do fundador ou assembleia.
        retorne self._approval_source

    // decorador: @property
    funcao is_law(self) -> logico:
        // Estes parâmetros já foram votados pelo povo?
        retorne self._assembly_approved


// ============================================================================
// 2. TIPOS DE CALCULO
// ============================================================================

classe CalculationType herda de Enum:
    // Para que estamos calculando trabalho/credito/reparacao.
    CONTRIBUTION = "contribuicao"  // trabalho voluntario do cidadao
    RECOGNITION = "reconhecimento"  // reconhecimento de trabalho passado
    REPARATION = "reparacao"  // compensacao por dano sofrido
    CREDIT_ALLOCATION = "credito"  // distribuicao de credito de acesso
    BASE_FULFILLMENT = "base_1.0"  // cumpriu contrato minimo?
    EXCESS_DETECTION = "excesso"  // trabalhou demais?


classe ImpactDimension herda de Enum:
    // Como o impacto do trabalho e medido (3 dimensoes).
    HOURS = "horas"  // tempo dado
    ARTIFACTS = "artefatos"  // coisas criadas
    PEOPLE = "pessoas_afetadas"  // alcance do efeito


// ============================================================================
// 3. FORMULA UNIFICADA DE TRABALHO
// ============================================================================

// decorador: @dataclass
classe LaborEntry:
    // Uma entrada de trabalho para calculo.
    citizen_id: texto
    citizen_name: texto
    calculation_type: CalculationType

    // Horas
    seja hours_worked: flutuante = 0.0
    seja weeks_worked: flutuante = 0.0

    // Impacto
    seja people_directly_impacted: inteiro = 0
    seja people_indirectly_impacted: inteiro = 0
    seja ripple_factor: flutuante = 1.0 // quanto se espalha (ensinar=10x, pesquisa=5x)

    // Artefatos
    seja systems_created: inteiro = 0
    seja documents_written: inteiro = 0
    seja lives_saved: inteiro = 0 // medico, bombeiro, etc

    // Contexto
    seja is_child: logico = falso // para reparacao
    seja years_labeled: flutuante = 0.0 // anos sob rotulo errado (reparacao)
    seja years_on_medication: flutuante = 0.0
    seja harm_severity: flutuante = 0.0 // 0-100 (reparacao)

    // Resultado (preenchido pelo motor)
    seja impact_score: flutuante = 0.0
    seja recognition_level: texto = ""
    seja credit_earned: flutuante = 0.0
    seja base_fulfilled: logico = falso
    seja excess_detected: logico = falso
    seja hours_reparation: flutuante = 0.0
    seja verdict: texto = ""


classe LaborCalculator:
    // Motor unico de calculo de trabalho e reparacao.

    ESTE MOTOR e A UNICA FONTE DE VERDADE MATEMATICA DA REPUBLICA.
    Nenhum outro sistema calcula trabalho de forma diferente.
    Todos (OpenCreator, OpenCredit, OpenPsychologyReparation) delegam para ca.
    // 

    funcao __init__(self, constants: LaborConstants = None):
        constants ? self.C = constants : LaborConstants()
        self.history: [LaborEntry] = []

    funcao calculate(self, entry: LaborEntry) -> LaborEntry:
        // Calcula tudo para uma entrada de trabalho.
        se entry.calculation_type == CalculationType.CONTRIBUTION entao:
            retorne self._calc_contribution(entry)
        senao se entry.calculation_type == CalculationType.REPARATION entao:
            retorne self._calc_reparation(entry)
        senao se entry.calculation_type == CalculationType.RECOGNITION entao:
            retorne self._calc_recognition(entry)
        senao se entry.calculation_type == CalculationType.BASE_FULFILLMENT entao:
            retorne self._check_base(entry)
        senao se entry.calculation_type == CalculationType.EXCESS_DETECTION entao:
            retorne self._check_excess(entry)
        retorne entry

    // ========================================================================
    // CONTRIBUICAO (trabalho voluntario)
    // ========================================================================

    funcao _calc_contribution(self, e: LaborEntry) -> LaborEntry:
        // Calcula impacto e credito de contribuicao voluntaria.

        FORMULA DE IMPACTO:
        impacto = horas * (1 + log10(maximo(1, pessoas)) * ripple)

        ONDE:
        - horas = tempo trabalhado
        - pessoas = pessoas afetadas direta e indiretamente
        - ripple = fator de propagacao no tempo

        EXEMPLOS:
        - Medico: 1 cirurgia, 1 vida salva, ripple 1x -> impacto = horas * 1
        - Professor: 4h, 30 alunos, ripple 10x -> impacto = 4 * (1 + 1.48 * 10) = 63
        - Agricultor: 8h, 500 pessoas, ripple 1x -> impacto = 8 * (1 + 2.7 * 1) = 30
        - Pesquisador: 8h, 1M pessoas, ripple 100x -> impacto = 8 * (1 + 6 * 100) = 4808
        // 
        people = e.people_directly_impacted + e.people_indirectly_impacted
        log_people = math.log10(maximo(1, people))

        impact = e.hours_worked * (1 + log_people * e.ripple_factor)

        // Bonus por vidas salvas
        se e.lives_saved > 0 entao:
            impact = impact + e.lives_saved * 100 // cada vida = 100 unidades de impacto

        e.impact_score = arredonde(impact, 2)

        // Credito de acesso
        e.credit_earned = self._impact_to_credit(impact)

        // Nivel de reconhecimento
        e.recognition_level = self._recognition_level(
            e.hours_worked, e.systems_created, people)

        // Verificar base e excesso
        e.base_fulfilled = e.hours_worked >= self.C.BASE_HOURS_PER_YEAR
        e.excess_detected = e.hours_worked > self.C.LIMIT_HOURS_PER_YEAR

        e.verdict = self._contribution_verdict(e)
        self.history.append(e)
        retorne e

    funcao _impact_to_credit(self, impact: flutuante) -> flutuante:
        // Converte impacto em credito de acesso.

        seja Formula: credito = clamp(impacto / 100, minimo, maximo)
        // 
        raw = impact / 100
        clamped = maximo(self.C.CREDIT_BASE_MIN,
                      minimo(self.C.CREDIT_BASE_MAX, raw))
        retorne arredonde(clamped, 1)

    funcao _recognition_level(self, hours: flutuante, artifacts: inteiro,
                           people: inteiro) -> texto:
        // Determina nivel de reconhecimento (3 dimensoes).
        // Por horas
        ratio = hours / self.C.BASE_HOURS_PER_YEAR
        se ratio >= 20 entao:
            level_h = 4
        senao se ratio >= 10 entao:
            level_h = 3
        senao se ratio >= 5 entao:
            level_h = 2
        senao se ratio >= 2 entao:
            level_h = 1
        senao se ratio >= 1 entao:
            level_h = 0
        senao:
            retorne "INCOMPLETO"

        // Por artefatos
        se artifacts >= 50 entao:
            level_a = 4
        senao se artifacts >= 20 entao:
            level_a = 3
        senao se artifacts >= 10 entao:
            level_a = 2
        senao se artifacts >= 1 entao:
            level_a = 1
        senao:
            level_a = 0

        // Por pessoas
        se people >= 10000 entao:
            level_p = 4
        senao se people >= 1000 entao:
            level_p = 3
        senao se people >= 100 entao:
            level_p = 2
        senao se people >= 10 entao:
            level_p = 1
        senao:
            level_p = 0

        names = ["CIDADAO", "CONTRIBUIDOR", "CONSTRUTOR",
                 "ARQUITETO", "FUNDADOR"]
        retorne names[maximo(level_h, level_a, level_p)]

    funcao _contribution_verdict(self, e: LaborEntry) -> texto:
        se e.excess_detected entao:
            retorne (
                "EXCESSO: {e.citizen_name} trabalhou {e.hours_worked:.0f}h "
                "(limite: {self.C.LIMIT_HOURS_PER_YEAR:.0f}h). "
                "Republica DEVE intervir. Burnout = dano corporal (P2)."
            )
        ratio = e.hours_worked / self.C.BASE_HOURS_PER_YEAR
        se ratio >= 5 entao:
            retorne (
                "MERITORIO: {e.citizen_name} deu {ratio:.1f}x a base. "
                "Impacto: {e.impact_score:.0f}. "
                "Reconhecimento: {e.recognition_level}. "
                "Poder: 1 voto (anti-elitismo P1)."
            )
        se e.base_fulfilled entao:
            retorne (
                "CONTRATO CUMPRIDO: {e.citizen_name} cumpriu base 1.0. "
                "Impacto: {e.impact_score:.0f}. "
                "Credito: {e.credit_earned:.1f}."
            )
        retorne "BASE INCOMPLETA: faltam {self.C.BASE_HOURS_PER_YEAR - e.hours_worked:.0f}h."

    // ========================================================================
    // REPARACAO (compensacao por dano)
    // ========================================================================

    funcao _calc_reparation(self, e: LaborEntry) -> LaborEntry:
        // Calcula reparacao por dano sofrido.

        FORMULA DE REPARACAO:
        horas = anos_rotulo * 920
              + anos_medicado * 40
        horas = horas * 1.5 (se dano > 70/100)
        horas = horas * 2.0 (se vitima era crianca)

        Credito = horas / 10

        ONDE:
        - anos_rotulo = anos vivendo com diagnostico/rotulo errado
        - anos_medicado = anos tomando remedio desnecessario
        - 920 = 1 ano de contrato base (vida roubada = vida reconhecida)
        - 40 = dano adicional por ano de medicacao
        // 
        years = maximo(1, e.years_labeled)

        // Base: anos de vida roubada * contrato anual
        hours = years * self.C.REPARATION_HOURS_PER_YEAR

        // Medicacao desnecessaria
        hours = hours + e.years_on_medication * self.C.REPARATION_MEDICATION_PER_YEAR

        // Agravante: dano severo
        se e.harm_severity > 70 entao:
            hours = hours * self.C.REPARATION_SEVERE_MULTIPLIER

        // Agravante: vitima era crianca
        se e.is_child entao:
            hours = hours * self.C.REPARATION_CHILD_MULTIPLIER

        hours = arredonde(hours)
        e.hours_reparation = hours
        e.impact_score = hours // reparacao conta como impacto reconhecido
        e.credit_earned = arredonde(hours / self.C.HOURS_TO_CREDIT, 1)
        e.recognition_level = "REPARACAO DEVIDA"
        e.verdict = self._reparation_verdict(e)

        self.history.append(e)
        retorne e

    funcao _reparation_verdict(self, e: LaborEntry) -> texto:
        severity = ("DEVASTADOR" if e.harm_severity >= 80
                    else "GRAVE" if e.harm_severity >= 60
                    else "SIGNIFICATIVO" if e.harm_severity >= 40
                    else "MODERADO" if e.harm_severity >= 20
                    else "LEVE")

        child_note = e.is_child ? " CRIANCA: multiplicador 2x aplicado." : ""
        med_note = (" {e.years_on_medication:.0f} anos de medicacao "
                    "(+{e.years_on_medication * 40:.0f}h).")

        retorne (
            "DANO {severity}: {e.citizen_name} teve "
            "{e.years_labeled:.0f} anos roubados. "
            "Reparacao: {e.hours_reparation:,.0f}h "
            "({e.hours_reparation/920:.0f} anos de trabalho). "
            "Credito: {e.credit_earned:.1f}.{child_note}{med_note}"
        )

    // ========================================================================
    // RECONHECIMENTO (trabalho passado)
    // ========================================================================

    funcao _calc_recognition(self, e: LaborEntry) -> LaborEntry:
        // Reconhece trabalho passado (pre-Republica).

        Tudo que cidadaos fizeram ANTES da Republica conta.
        Mas e reconhecido, nao comprado. Reconhecimento = credito + gratidao.
        // 
        // Mesmo calculo de contribuicao
        e = self._calc_contribution(e)
        e.calculation_type = CalculationType.RECOGNITION
        e.verdict = (
            "RECONHECIDO: {e.citizen_name} contribuiu "
            "{e.hours_worked:.0f}h antes da Republica. "
            "Impacto: {e.impact_score:.0f}. "
            "Credito retroativo: {e.credit_earned:.1f}. "
            "Reconhecimento: {e.recognition_level}."
        )
        retorne e

    // ========================================================================
    // VERIFICACOES
    // ========================================================================

    funcao _check_base(self, e: LaborEntry) -> LaborEntry:
        // Verifica se cumpriu contrato base 1.0.
        e.base_fulfilled = e.hours_worked >= self.C.BASE_HOURS_PER_YEAR
        remaining = maximo(0, self.C.BASE_HOURS_PER_YEAR - e.hours_worked)
        e.verdict = (
            "{'CUMPRIDO' if e.base_fulfilled else 'INCOMPLETO'}: "
            "{e.hours_worked:.0f}h de {self.C.BASE_HOURS_PER_YEAR:.0f}h. "
            "Faltam: {remaining:.0f}h."
        )
        retorne e

    funcao _check_excess(self, e: LaborEntry) -> LaborEntry:
        // Verifica se trabalhou demais (intervencao necessaria).
        e.excess_detected = e.hours_worked > self.C.LIMIT_HOURS_PER_YEAR
        se e.excess_detected entao:
            over = e.hours_worked - self.C.LIMIT_HOURS_PER_YEAR
            e.verdict = (
                "EXCESSO DETECTADO: {e.hours_worked:.0f}h "
                "(limite: {self.C.LIMIT_HOURS_PER_YEAR:.0f}h). "
                "Excesso: {over:.0f}h. "
                "ACAO: reduzir carga, garantir descanso, monitorar saude."
            )
        senao:
            ratio = e.hours_worked / self.C.BASE_HOURS_PER_YEAR
            e.verdict = "DENTRO DO LIMITE: {e.hours_worked:.0f}h ({ratio:.1f}x base)."
        retorne e

    // ========================================================================
    // RELATORIOS
    // ========================================================================

    funcao summary(self) -> {texto: qualquer}:
        // Resumo de todos os calculos feitos.
        by_type = defaultdict(inteiro)
        total_hours = 0.0
        total_credit = 0.0
        total_reparation = 0.0
        excess_count = 0

        para cada e em self.history:
            by_type[e.calculation_type.value] += 1
            total_hours = total_hours + e.hours_worked
            total_credit = total_credit + e.credit_earned
            total_reparation = total_reparation + e.hours_reparation
            se e.excess_detected entao:
                excess_count = excess_count + 1

        retorne {
            "total_calculations": tamanho(self.history),
            "by_type": dict(by_type),
            "total_hours": arredonde(total_hours, 0),
            "total_credit": arredonde(total_credit, 1),
            "total_reparation_hours": arredonde(total_reparation, 0),
            "excess_detected": excess_count,
        }


// ============================================================================
// 4. TABELA DE EQUIVALENCIAS (para cidadaos entenderem)
// ============================================================================

funcao print_equivalency_table() -> None:
    // Mostra quanto vale cada tipo de trabalho em credito da Republica.

    calc = LaborCalculator()

    imprima("\n  === TABELA DE EQUIVALENCIAS ===\n")
    imprima("  {'Trabalho':<35} {'Horas':>6} {'Impacto':>8} {'Credito':>8}")
    imprima("  {'-'*62}")

    examples = [
        ("Base 1.0 (20h/sem, 46 sem)", 920, 1, 1.0),
        ("Professor (4h/dia, 30 alunos)", 920, 30, 10.0),
        ("Agricultor (8h/dia, 500 pessoas)", 1840, 500, 1.0),
        ("Medico cirurgiao (1 vida/semana)", 1840, 52, 1.0),
        ("Pesquisador (1M pessoas)", 920, 1000000, 100.0),
        ("Criador de sistemas (50 sistemas)", 4000, 5000, 5.0),
        ("Faxineiro (200 pessoas/espaco)", 920, 200, 2.0),
    ]

    para desc, hours, people, ripple in examples:
        entry = LaborEntry(
            citizen_id = "x", citizen_name=desc,
            calculation_type = CalculationType.CONTRIBUTION,
            hours_worked = hours,
            people_directly_impacted = people,
            ripple_factor = ripple,
        )
        result = calc.calculate(entry)
        imprima("  {desc:<35} {hours:>5}h {result.impact_score:>8.0f} "
              "{result.credit_earned:>7.1f}")

    imprima("\n  === TABELA DE REPARACAO ===\n")
    imprima("  {'Dano':<35} {'Anos':>5} {'Horas':>8} {'Credito':>8}")
    imprima("  {'-'*62}")

    reparation_examples = [
        ("Rotulo errado adulto (10 anos)", 10, falso, 0, 30),
        ("Rotulo errado + medicado (10 anos)", 10, falso, 10, 60),
        ("Rotulo errado CRIANCA (10 anos)", 10, verdadeiro, 0, 50),
        ("Rotulo errado crianca + medicado", 10, verdadeiro, 8, 85),
        ("Rotulo errado adulto severo (15 anos)", 15, falso, 15, 90),
        ("Rotulo errado crianca severo (12 anos)", 12, verdadeiro, 7, 95),
    ]

    para desc, years, child, med, harm in reparation_examples:
        entry = LaborEntry(
            citizen_id = "x", citizen_name=desc,
            calculation_type = CalculationType.REPARATION,
            years_labeled = years,
            is_child = child,
            years_on_medication = med,
            harm_severity = harm,
        )
        result = calc.calculate(entry)
        imprima("  {desc:<35} {years:>4}a {result.hours_reparation:>7,.0f}h "
              "{result.credit_earned:>7.1f}")


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    // importa sys
    sys.path.insert(0, texto(__import__('pathlib').Path(__file__).parent))

    // === CARREGAR PARÂMETROS DA ASSEMBLEIA (ou usar referência) ===
    tente:
        // importa ConstituentAssembly de open_constituent_assembly
        assembly = ConstituentAssembly()
        assembly.populate(n=10000)
        assembly._init_propositions()
        constitution = assembly.run_election()
        C = LaborConstants.from_constitution(constitution)
        source_label = "ASSEMBLEIA CONSTITUINTE (vontade do povo)"
    capture Exception:
        C = LaborConstants()
        source_label = "REFERÊNCIA DO FUNDADOR (provisório)"

    calc = LaborCalculator(constants=C)

    imprima("=" * 70)
    imprima("  OPENLABORPOLICY -- LEI MATEMATICA DA REPUBLICA")
    imprima('  "Parâmetros são referência. A ASSEMBLEIA é a lei."')
    imprima("=" * 70)
    imprima("\n  FONTE: {source_label}")
    imprima("  É LEI: {'SIM' if C.is_law else 'NÃO (referência)'}\n")
    imprima("  CONTRATO DE TRABALHO:")
    imprima("    Base:   {C.BASE_HOURS_PER_WEEK:.0f}h/semana  "
          "({C.BASE_HOURS_PER_YEAR:.0f}h/ano)")
    imprima("    Maximo: {C.MAX_HOURS_PER_WEEK:.0f}h/semana  "
          "({C.MAX_HOURS_PER_YEAR:.0f}h/ano)")
    imprima("    LIMITE: {C.LIMIT_HOURS_PER_WEEK:.0f}h/semana  "
          "({C.LIMIT_HOURS_PER_YEAR:.0f}h/ano) [PROIBIDO aceitar mais]")
    imprima("    Descanso: {C.REST_DAYS_PER_WEEK} dias/semana + "
          "{C.MIN_VACATION_WEEKS} semanas ferias")
    imprima("\n  CREDITO DE ACESSO:")
    imprima("    Min:  {C.CREDIT_BASE_MIN:.0f}/ciclo")
    imprima("    Max:  {C.CREDIT_BASE_MAX:.0f}/ciclo")
    imprima("    Pool: {C.CREDIT_POOL_PER_CYCLE:.0f}/comunidade/ciclo")
    imprima("    Conversao: {C.HOURS_TO_CREDIT:.0f}h = 1 credito")
    imprima("\n  REPARACAO:")
    imprima("    1 ano roubado = {C.REPARATION_HOURS_PER_YEAR:.0f}h")
    imprima("    Crianca = {C.REPARATION_CHILD_MULTIPLIER}x")
    imprima("    Severo = {C.REPARATION_SEVERE_MULTIPLIER}x")
    imprima("    Medicacao = +{C.REPARATION_MEDICATION_PER_YEAR:.0f}h/ano")

    // === 2. TABELAS ===
    print_equivalency_table()

    // === 3. CASOS REAIS ===
    imprima("\n\n  === 3. CALCULOS DE CASOS REAIS ===\n")

    // Fundador
    founder = LaborEntry(
        citizen_id = "founder", citizen_name="Cleiton",
        calculation_type = CalculationType.CONTRIBUTION,
        hours_worked = 4000,
        systems_created = 95,
        people_directly_impacted = 5000,
        ripple_factor = 5.0,
    )
    r = calc.calculate(founder)
    imprima("  CLEITON (fundador):")
    imprima("    {r.verdict}")
    imprima("    Impacto: {r.impact_score:,.0f}")
    imprima("    Credito: {r.credit_earned:.1f}")
    imprima("    Excesso: {'SIM -- Republica deve intervir' if r.excess_detected else 'nao'}")

    // Medico
    medico = LaborEntry(
        citizen_id = "c-001", citizen_name="Ana (medica)",
        calculation_type = CalculationType.CONTRIBUTION,
        hours_worked = 1840,
        lives_saved = 50,
        people_directly_impacted = 800,
        ripple_factor = 2.0,
    )
    r = calc.calculate(medico)
    imprima("\n  ANA (medica):")
    imprima("    {r.verdict}")
    imprima("    Impacto: {r.impact_score:,.0f} (50 vidas salvas)")
    imprima("    Credito: {r.credit_earned:.1f}")

    // Professor
    prof = LaborEntry(
        citizen_id = "c-002", citizen_name="Maria (professora)",
        calculation_type = CalculationType.CONTRIBUTION,
        hours_worked = 920,
        people_directly_impacted = 300,
        ripple_factor = 10.0,
    )
    r = calc.calculate(prof)
    imprima("\n  MARIA (professora):")
    imprima("    {r.verdict}")
    imprima("    Impacto: {r.impact_score:,.0f}")
    imprima("    Credito: {r.credit_earned:.1f}")

    // Reparacao: crianca rotulada
    rep = LaborEntry(
        citizen_id = "c-100", citizen_name="Pedro (reparacao)",
        calculation_type = CalculationType.REPARATION,
        years_labeled = 11,
        is_child = verdadeiro,
        years_on_medication = 8,
        harm_severity = 95,
    )
    r = calc.calculate(rep)
    imprima("\n  PEDRO (reparacao - crianca rotulada):")
    imprima("    {r.verdict}")
    imprima("    Horas reparacao: {r.hours_reparation:,.0f}h")
    imprima("    Credito: {r.credit_earned:.1f}")

    // === 4. RELATORIO ===
    imprima("\n\n  === 4. RELATORIO GERAL ===\n")
    s = calc.summary()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*70}")
    imprima("  A LEI MATEMATICA DA REPUBLICA")
    imprima("{'='*70}")
    imprima("""
  UM SISTEMA, UMA FORMULA, ZERO EXCECOES:

  TRABALHO (contribuicao):
    impacto = horas * (1 + log10(pessoas) * ripple)
    credito = clamp(impacto / 100, 5, 50)
    base = 920h/ano. maximo = 1840h/ano. LIMITE = 2300h/ano.

  REPARACAO (dano sofrido):
    horas = anos * 920 + anos_medicado * 40
    horas = horas * 1.5 (severo) ou 2.0 (crianca)
    credito = horas / 10

  O QUE ISTO SIGNIFICA:
    1. TODO trabalho vale o mesmo por hora base (P3).
    2. Diferenca vem de IMPACTO, nao de cargo.
    3. Medico que salva vida = impacto altissimo por pessoa.
    4. Professor que ensina 30 = impacto medio mas ripple 10x.
    5. Faxineiro que protege 200 de doenca = impacto real.
    6. Criador de 50 sistemas = reconhecimento FUNDADOR.
    7. Crianca rotulada errada = reparacao DOBRO.
    8. Quem trabalha > 2300h = Republica INTERVEM (P2).

  O QUE nao EXISTE:
    - Salario diferente por cargo (P3 anti-elitismo)
    - Comprar credito com dinheiro (sem moeda)
    - Acumular credito (expira por ciclo)
    - Herdar credito (morreu, zerou)
    - Trabalhar alem do limite (PROIBIDO por P2)
    - Reparacao em dinheiro (sem moeda)
    - Privilegio de fundador no calculo (1 voto)

  A FORMULA e A VERDADE:
    Ninguem discute. Ninguem favorece.
    Os numeros sao os numeros.
    A justica e matematica.
// )
    imprima("{'='*70}")
    imprima("  OpenLaborPolicy: {s['total_calculations']} calculos realizados.")
    imprima("  Base 920h. Max 1840h. Limite 2300h. 1 formula. 0 excecoes.")
    imprima("{'='*70}")

```
