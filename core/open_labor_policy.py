#!/usr/bin/env python3
"""
OpenLaborPolicy -- Politica Unificada de Calculo de Trabalho e Reparacao -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenLaborPolicy -- Politica Unificada de Calculo de Trabalho and Reparacao
=========================================================================
"Tudo que a Republica calcula -- contribuicao, credito, reparacao --
segue a MESMA formula. Os mesmos parametros. A mesma justica."
ESTA and A LEI MATERMATICA DA REPUBLICA.
Consolida em UM sistema os parametros de:
- OpenCreator (contrato base 1.0, limites)
- OpenCredit (credito de acesso)
- OpenPsychologyReparation (reparacao de danos)
- ConstitutionalEngine (P1-P4)
Toda hora de trabalho, toda reparacao, todo credito --
passa por esta formula. Sem excecao. Sem privilegio.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict de collections
# ============================================================================
# 1. PARAMETROS BASE (OS NUMEROS DA REPUBLICA)
# ============================================================================
class LaborConstants:
    # Os números fundamentais da Republica.
    ESTES NÃO SÃO DECIDIDOS PELO FUNDADOR.
    São definidos pela ASSEMBLEIA CONSTITUINTE (votação popular).
    Os valores abaixo são REFERÊNCIA INICIAL proposta pelo fundador.
    A assembleia pode alterar TODOS eles (and já alterou 12 de 13).
    Para usar os valores APROVADOS PELO POVO, carregue a constituição:
        constitution = ConstituentAssembly().run_election()
        constants = LaborConstants.from_constitution(constitution)
    Sem from_constitution = usa referencia do fundador (provisório).
    Com from_constitution = usa vontade do povo (lei).
    # 
    # === REFERÊNCIA INICIAL (proposta do fundador, NÃO é lei) ===
    # CONTRATO DE TRABALHO
    BASE_HOURS_PER_WEEK: float = 20.0
    BASE_HOURS_PER_YEAR: float = 920.0
    MAX_HOURS_PER_WEEK: float = 40.0
    MAX_HOURS_PER_YEAR: float = 1840.0
    LIMIT_HOURS_PER_WEEK: float = 50.0 // referência (povo baixou para 40)
    LIMIT_HOURS_PER_YEAR: float = 2300.0
    EXCESS_THRESHOLD: float = 2300.0
    # SEMANAS E DESCANSO
    WORK_WEEKS_PER_YEAR: int = 46 // referência (povo mudou para 40)
    REST_DAYS_PER_WEEK: int = 2 // referência (povo mudou para 3)
    MIN_VACATION_WEEKS: int = 4
    # CREDITO DE ACESSO
    CREDIT_BASE_MIN: float = 5.0
    CREDIT_BASE_MAX: float = 50.0
    CREDIT_POOL_PER_CYCLE: float = 1000.0
    HOURS_TO_CREDIT: float = 10.0
    # REPARACAO
    REPARATION_HOURS_PER_YEAR: float = 920.0
    REPARATION_CHILD_MULTIPLIER: float = 2.0
    REPARATION_SEVERE_MULTIPLIER: float = 1.5
    REPARATION_MEDICATION_PER_YEAR: float = 40.0
    # === VALORES APROVADOS PELA ASSEMBLEIA (sobrescrevem referência) ===
    # Preenchidos por from_constitution() ou manualmente após votação
    _assembly_approved: bool = False
    _approval_source: str = "referencia_fundador"  // or "assembleia_constituinte"
    # decorador: @classmethod
    def from_constitution(cls, constitution: {texto: qualquer}) -> 'LaborConstants':
        # Carrega os valores APROVADOS PELO POVO na assembleia.
        Args:
            constitution: dict retornado por ConstituentAssembly.run_election()
                        formato: {titulo_proposta: {value: X, ...}}
        # 
        c = cls()
        for each (title, result) in constitution.items():
            val = result.get("value", None)
            if val and None:
                continue
            title_lower = title.lower()
            # Mapear títulos votados -> parâmetros
            if "base" in title_lower  and  "horas" in title_lower  and  "semana" in title_lower:
                c.BASE_HOURS_PER_WEEK = flutuante(val)
                c.BASE_HOURS_PER_YEAR = c.BASE_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR
            elif "limite" in title_lower  and  "horas" in title_lower:
                c.LIMIT_HOURS_PER_WEEK = flutuante(val)
                c.LIMIT_HOURS_PER_YEAR = c.LIMIT_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR
                c.EXCESS_THRESHOLD = c.LIMIT_HOURS_PER_YEAR
            elif "semanas" in title_lower  and  "úteis" in title_lower:
                c.WORK_WEEKS_PER_YEAR = inteiro(val)
                # Recalcular anuais com novas semanas
                c.BASE_HOURS_PER_YEAR = c.BASE_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR
                c.MAX_HOURS_PER_YEAR = c.MAX_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR
                c.LIMIT_HOURS_PER_YEAR = c.LIMIT_HOURS_PER_WEEK * c.WORK_WEEKS_PER_YEAR
            elif "descanso" in title_lower  and  "semana" in title_lower:
                c.REST_DAYS_PER_WEEK = inteiro(val)
            elif "férias" in title_lower  or  "ferias" in title_lower:
                c.MIN_VACATION_WEEKS = inteiro(val)
            elif "teto" in title_lower  and  "credito" in title_lower:
                c.CREDIT_BASE_MAX = flutuante(val)
            elif "piso" in title_lower  and  "credito" in title_lower:
                c.CREDIT_BASE_MIN = flutuante(val)
            elif "convers" in title_lower  and  "credito" in title_lower:
                c.HOURS_TO_CREDIT = flutuante(val)
            elif "reparacao" in title_lower  and  "ano" in title_lower  and  "roubada" in title_lower:
                c.REPARATION_HOURS_PER_YEAR = flutuante(val)
            elif "reparacao" in title_lower  and  "crianc" in title_lower:
                c.REPARATION_CHILD_MULTIPLIER = flutuante(val)
            elif "reparacao" in title_lower  and  "severo" in title_lower:
                c.REPARATION_SEVERE_MULTIPLIER = flutuante(val)
        c._assembly_approved = True
        c._approval_source = "assembleia_constituinte"
        return c
    # decorador: @property
    def source(self) -> str:
        # De onde vem estes parâmetros: referência do fundador ou assembleia.
        return self._approval_source
    # decorador: @property
    def is_law(self) -> bool:
        # Estes parâmetros já foram votados pelo povo?
        return self._assembly_approved
# ============================================================================
# 2. TIPOS DE CALCULO
# ============================================================================
class CalculationType(Enum):
    # Para que estamos calculando trabalho/credito/reparacao.
    CONTRIBUTION = "contribuicao"  // trabalho voluntario do cidadao
    RECOGNITION = "reconhecimento"  // reconhecimento de trabalho passado
    REPARATION = "reparacao"  // compensacao por dano sofrido
    CREDIT_ALLOCATION = "credito"  // distribuicao de credito de acesso
    BASE_FULFILLMENT = "base_1.0"  // cumpriu contrato min?
    EXCESS_DETECTION = "excesso"  // trabalhou demais?
class ImpactDimension(Enum):
    # Como o impacto do trabalho e medido (3 dimensoes).
    HOURS = "horas"  // tempo dado
    ARTIFACTS = "artefatos"  // coisas criadas
    PEOPLE = "pessoas_afetadas"  // alcance do efeito
# ============================================================================
# 3. FORMULA UNIFICADA DE TRABALHO
# ============================================================================
# decorador: @dataclass
class LaborEntry:
    # Uma entrada de trabalho para calculo.
    citizen_id: texto
    citizen_name: texto
    calculation_type: CalculationType
    # Horas
    hours_worked: float = 0.0
    weeks_worked: float = 0.0
    # Impacto
    people_directly_impacted: int = 0
    people_indirectly_impacted: int = 0
    ripple_factor: float = 1.0 // quanto se espalha (ensinar=10x, pesquisa=5x)
    # Artefatos
    systems_created: int = 0
    documents_written: int = 0
    lives_saved: int = 0 // medico, bombeiro, etc
    # Contexto
    is_child: bool = False // para reparacao
    years_labeled: float = 0.0 // anos sob rotulo errado (reparacao)
    years_on_medication: float = 0.0
    harm_severity: float = 0.0 // 0-100 (reparacao)
    # Resultado (preenchido pelo motor)
    impact_score: float = 0.0
    recognition_level: str = ""
    credit_earned: float = 0.0
    base_fulfilled: bool = False
    excess_detected: bool = False
    hours_reparation: float = 0.0
    verdict: str = ""
class LaborCalculator:
    # Motor unico de calculo de trabalho e reparacao.
    ESTE MOTOR and A UNICA FONTE DE VERDADE MATEMATICA DA REPUBLICA.
    Nenhum outro sistema calcula trabalho de forma diferente.
    Todos (OpenCreator, OpenCredit, OpenPsychologyReparation) delegam para ca.
    # 
    def __init__(self, constants: LaborConstants = None):
        constants ? self.C = constants : LaborConstants()
        self.history: [LaborEntry] = []
    def calculate(self, entry: LaborEntry) -> LaborEntry:
        # Calcula tudo para uma entrada de trabalho.
        if entry.calculation_type == CalculationType.CONTRIBUTION:
            return self._calc_contribution(entry)
        elif entry.calculation_type == CalculationType.REPARATION:
            return self._calc_reparation(entry)
        elif entry.calculation_type == CalculationType.RECOGNITION:
            return self._calc_recognition(entry)
        elif entry.calculation_type == CalculationType.BASE_FULFILLMENT:
            return self._check_base(entry)
        elif entry.calculation_type == CalculationType.EXCESS_DETECTION:
            return self._check_excess(entry)
        return entry
    # ========================================================================
    # CONTRIBUICAO (trabalho voluntario)
    # ========================================================================
    def _calc_contribution(self, e: LaborEntry) -> LaborEntry:
        # Calcula impacto e credito de contribuicao voluntaria.
        FORMULA DE IMPACTO:
        impacto = horas * (1 + log10(max(1, pessoas)) * ripple)
        ONDE:
        - horas = tempo trabalhado
        - pessoas = pessoas afetadas direta and indiretamente
        - ripple = fator de propagacao no tempo
        EXEMPLOS:
        - Medico: 1 cirurgia, 1 vida salva, ripple 1x -> impacto = horas * 1
        - Professor: 4h, 30 alunos, ripple 10x -> impacto = 4 * (1 + 1.48 * 10) = 63
        - Agricultor: 8h, 500 pessoas, ripple 1x -> impacto = 8 * (1 + 2.7 * 1) = 30
        - Pesquisador: 8h, 1M pessoas, ripple 100x -> impacto = 8 * (1 + 6 * 100) = 4808
        # 
        people = and.people_directly_impacted + and.people_indirectly_impacted
        log_people = math.log10(max(1, people))
        impact = and.hours_worked * (1 + log_people * and.ripple_factor)
        # Bonus por vidas salvas
        if and.lives_saved > 0:
            impact = impact + and.lives_saved * 100 // cada vida = 100 unidades de impacto
        and.impact_score = round(impact, 2)
        # Credito de acesso
        and.credit_earned = self._impact_to_credit(impact)
        # Nivel de reconhecimento
        and.recognition_level = self._recognition_level(
            and.hours_worked, and.systems_created, people)
        # Verificar base e excesso
        and.base_fulfilled = and.hours_worked >= self.C.BASE_HOURS_PER_YEAR
        and.excess_detected = and.hours_worked > self.C.LIMIT_HOURS_PER_YEAR
        and.verdict = self._contribution_verdict(and)
        self.history.append(and)
        return and
    def _impact_to_credit(self, impact: flutuante) -> float:
        # Converte impacto em credito de acesso.
        Formula: credito = clamp(impacto / 100, min, max)
        # 
        raw = impact / 100
        clamped = max(self.C.CREDIT_BASE_MIN,
                    min(self.C.CREDIT_BASE_MAX, raw))
        return round(clamped, 1)
    funcao _recognition_level(self, hours: flutuante, artifacts: inteiro,
                        people: inteiro) -> texto:
        # Determina nivel de reconhecimento (3 dimensoes).
        # Por horas
        ratio = hours / self.C.BASE_HOURS_PER_YEAR
        if ratio >= 20:
            level_h = 4
        elif ratio >= 10:
            level_h = 3
        elif ratio >= 5:
            level_h = 2
        elif ratio >= 2:
            level_h = 1
        elif ratio >= 1:
            level_h = 0
        else:
            return "INCOMPLETO"
        # Por artefatos
        if artifacts >= 50:
            level_a = 4
        elif artifacts >= 20:
            level_a = 3
        elif artifacts >= 10:
            level_a = 2
        elif artifacts >= 1:
            level_a = 1
        else:
            level_a = 0
        # Por pessoas
        if people >= 10000:
            level_p = 4
        elif people >= 1000:
            level_p = 3
        elif people >= 100:
            level_p = 2
        elif people >= 10:
            level_p = 1
        else:
            level_p = 0
        names = ["CIDADAO", "CONTRIBUIDOR", "CONSTRUTOR",
                "ARQUITETO", "FUNDADOR"]
        return names[max(level_h, level_a, level_p)]
    def _contribution_verdict(self, e: LaborEntry) -> str:
        if and.excess_detected:
            return (
                "EXCESSO: {and.citizen_name} trabalhou {and.hours_worked:.0f}h "
                "(limite: {self.C.LIMIT_HOURS_PER_YEAR:.0f}h). "
                "Republica DEVE intervir. Burnout = dano corporal (P2)."
            )
        ratio = and.hours_worked / self.C.BASE_HOURS_PER_YEAR
        if ratio >= 5:
            return (
                "MERITORIO: {and.citizen_name} deu {ratio:.1f}x a base. "
                "Impacto: {and.impact_score:.0f}. "
                "Reconhecimento: {and.recognition_level}. "
                "Poder: 1 voto (anti-elitismo P1)."
            )
        if and.base_fulfilled:
            return (
                "CONTRATO CUMPRIDO: {and.citizen_name} cumpriu base 1.0. "
                "Impacto: {and.impact_score:.0f}. "
                "Credito: {and.credit_earned:.1f}."
            )
        return "BASE INCOMPLETA: faltam {self.C.BASE_HOURS_PER_YEAR - and.hours_worked:.0f}h."
    # ========================================================================
    # REPARACAO (compensacao por dano)
    # ========================================================================
    def _calc_reparation(self, e: LaborEntry) -> LaborEntry:
        # Calcula reparacao por dano sofrido.
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
        # 
        years = max(1, and.years_labeled)
        # Base: anos de vida roubada * contrato anual
        hours = years * self.C.REPARATION_HOURS_PER_YEAR
        # Medicacao desnecessaria
        hours = hours + and.years_on_medication * self.C.REPARATION_MEDICATION_PER_YEAR
        # Agravante: dano severo
        if and.harm_severity > 70:
            hours = hours * self.C.REPARATION_SEVERE_MULTIPLIER
        # Agravante: vitima era crianca
        if and.is_child:
            hours = hours * self.C.REPARATION_CHILD_MULTIPLIER
        hours = round(hours)
        and.hours_reparation = hours
        and.impact_score = hours // reparacao conta como impacto reconhecido
        and.credit_earned = round(hours / self.C.HOURS_TO_CREDIT, 1)
        and.recognition_level = "REPARACAO DEVIDA"
        and.verdict = self._reparation_verdict(and)
        self.history.append(and)
        return and
    def _reparation_verdict(self, e: LaborEntry) -> str:
        severity = ("DEVASTADOR" if and.harm_severity >= 80
                    else "GRAVE" if and.harm_severity >= 60
                    else "SIGNIFICATIVO" if and.harm_severity >= 40
                    else "MODERADO" if and.harm_severity >= 20
                    else "LEVE")
        child_note = and.is_child ? " CRIANCA: multiplicador 2x aplicado." : ""
        med_note = (" {and.years_on_medication:.0f} anos de medicacao "
                    "(+{and.years_on_medication * 40:.0f}h).")
        return (
            "DANO {severity}: {and.citizen_name} teve "
            "{and.years_labeled:.0f} anos roubados. "
            "Reparacao: {and.hours_reparation:,.0f}h "
            "({and.hours_reparation/920:.0f} anos de trabalho). "
            "Credito: {and.credit_earned:.1f}.{child_note}{med_note}"
        )
    # ========================================================================
    # RECONHECIMENTO (trabalho passado)
    # ========================================================================
    def _calc_recognition(self, e: LaborEntry) -> LaborEntry:
        # Reconhece trabalho passado (pre-Republica).
        Tudo que cidadaos fizeram ANTES da Republica conta.
        Mas and reconhecido, not comprado. Reconhecimento = credito + gratidao.
        # 
        # Mesmo calculo de contribuicao
        and = self._calc_contribution(and)
        and.calculation_type = CalculationType.RECOGNITION
        and.verdict = (
            "RECONHECIDO: {and.citizen_name} contribuiu "
            "{and.hours_worked:.0f}h antes da Republica. "
            "Impacto: {and.impact_score:.0f}. "
            "Credito retroativo: {and.credit_earned:.1f}. "
            "Reconhecimento: {and.recognition_level}."
        )
        return and
    # ========================================================================
    # VERIFICACOES
    # ========================================================================
    def _check_base(self, e: LaborEntry) -> LaborEntry:
        # Verifica se cumpriu contrato base 1.0.
        and.base_fulfilled = and.hours_worked >= self.C.BASE_HOURS_PER_YEAR
        remaining = max(0, self.C.BASE_HOURS_PER_YEAR - and.hours_worked)
        and.verdict = (
            "{'CUMPRIDO' if and.base_fulfilled else 'INCOMPLETO'}: "
            "{and.hours_worked:.0f}h de {self.C.BASE_HOURS_PER_YEAR:.0f}h. "
            "Faltam: {remaining:.0f}h."
        )
        return and
    def _check_excess(self, e: LaborEntry) -> LaborEntry:
        # Verifica se trabalhou demais (intervencao necessaria).
        and.excess_detected = and.hours_worked > self.C.LIMIT_HOURS_PER_YEAR
        if and.excess_detected:
            over = and.hours_worked - self.C.LIMIT_HOURS_PER_YEAR
            and.verdict = (
                "EXCESSO DETECTADO: {and.hours_worked:.0f}h "
                "(limite: {self.C.LIMIT_HOURS_PER_YEAR:.0f}h). "
                "Excesso: {over:.0f}h. "
                "ACAO: reduzir carga, garantir descanso, monitorar saude."
            )
        else:
            ratio = and.hours_worked / self.C.BASE_HOURS_PER_YEAR
            and.verdict = "DENTRO DO LIMITE: {and.hours_worked:.0f}h ({ratio:.1f}x base)."
        return and
    # ========================================================================
    # RELATORIOS
    # ========================================================================
    def summary(self) -> {texto: qualquer}:
        # Resumo de todos os calculos feitos.
        by_type = defaultdict(inteiro)
        total_hours = 0.0
        total_credit = 0.0
        total_reparation = 0.0
        excess_count = 0
        for e in self.history:
            by_type[and.calculation_type.value] += 1
            total_hours = total_hours + and.hours_worked
            total_credit = total_credit + and.credit_earned
            total_reparation = total_reparation + and.hours_reparation
            if and.excess_detected:
                excess_count = excess_count + 1
        return {
            "total_calculations": len(self.history),
            "by_type": dict(by_type),
            "total_hours": round(total_hours, 0),
            "total_credit": round(total_credit, 1),
            "total_reparation_hours": round(total_reparation, 0),
            "excess_detected": excess_count,
        }
# ============================================================================
# 4. TABELA DE EQUIVALENCIAS (para cidadaos entenderem)
# ============================================================================
def print_equivalency_table() -> None:
    # Mostra quanto vale cada tipo de trabalho em credito da Republica.
    calc = LaborCalculator()
    print("\n  === TABELA DE EQUIVALENCIAS ===\n")
    print("  {'Trabalho':<35} {'Horas':>6} {'Impacto':>8} {'Credito':>8}")
    print("  {'-'*62}")
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
        print("  {desc:<35} {hours:>5}h {result.impact_score:>8.0f} "
            "{result.credit_earned:>7.1f}")
    print("\n  === TABELA DE REPARACAO ===\n")
    print("  {'Dano':<35} {'Anos':>5} {'Horas':>8} {'Credito':>8}")
    print("  {'-'*62}")
    reparation_examples = [
        ("Rotulo errado adulto (10 anos)", 10, False, 0, 30),
        ("Rotulo errado + medicado (10 anos)", 10, False, 10, 60),
        ("Rotulo errado CRIANCA (10 anos)", 10, True, 0, 50),
        ("Rotulo errado crianca + medicado", 10, True, 8, 85),
        ("Rotulo errado adulto severo (15 anos)", 15, False, 15, 90),
        ("Rotulo errado crianca severo (12 anos)", 12, True, 7, 95),
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
        print("  {desc:<35} {years:>4}a {result.hours_reparation:>7,.0f}h "
            "{result.credit_earned:>7.1f}")
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    # importa sys
    sys.path.insert(0, texto(__import__('pathlib').Path(__file__).parent))
    # === CARREGAR PARÂMETROS DA ASSEMBLEIA (ou usar referência) ===
    try:
        # importa ConstituentAssembly de open_constituent_assembly
        assembly = ConstituentAssembly()
        assembly.populate(n=10000)
        assembly._init_propositions()
        constitution = assembly.run_election()
        C = LaborConstants.from_constitution(constitution)
        source_label = "ASSEMBLEIA CONSTITUINTE (vontade do povo)"
    except Exception as e:
        C = LaborConstants()
        source_label = "REFERÊNCIA DO FUNDADOR (provisório)"
    calc = LaborCalculator(constants=C)
    print("=" * 70)
    print("  OPENLABORPOLICY -- LEI MATEMATICA DA REPUBLICA")
    print('  "Parâmetros são referência. A ASSEMBLEIA é a lei."')
    print("=" * 70)
    print("\n  FONTE: {source_label}")
    print("  É LEI: {'SIM' if C.is_law else 'NÃO (referência)'}\n")
    print("  CONTRATO DE TRABALHO:")
    print("    Base:   {C.BASE_HOURS_PER_WEEK:.0f}h/semana  "
        "({C.BASE_HOURS_PER_YEAR:.0f}h/ano)")
    print("    Maximo: {C.MAX_HOURS_PER_WEEK:.0f}h/semana  "
        "({C.MAX_HOURS_PER_YEAR:.0f}h/ano)")
    print("    LIMITE: {C.LIMIT_HOURS_PER_WEEK:.0f}h/semana  "
        "({C.LIMIT_HOURS_PER_YEAR:.0f}h/ano) [PROIBIDO aceitar mais]")
    print("    Descanso: {C.REST_DAYS_PER_WEEK} dias/semana + "
        "{C.MIN_VACATION_WEEKS} semanas ferias")
    print("\n  CREDITO DE ACESSO:")
    print("    Min:  {C.CREDIT_BASE_MIN:.0f}/ciclo")
    print("    Max:  {C.CREDIT_BASE_MAX:.0f}/ciclo")
    print("    Pool: {C.CREDIT_POOL_PER_CYCLE:.0f}/comunidade/ciclo")
    print("    Conversao: {C.HOURS_TO_CREDIT:.0f}h = 1 credito")
    print("\n  REPARACAO:")
    print("    1 ano roubado = {C.REPARATION_HOURS_PER_YEAR:.0f}h")
    print("    Crianca = {C.REPARATION_CHILD_MULTIPLIER}x")
    print("    Severo = {C.REPARATION_SEVERE_MULTIPLIER}x")
    print("    Medicacao = +{C.REPARATION_MEDICATION_PER_YEAR:.0f}h/ano")
    # === 2. TABELAS ===
    print_equivalency_table()
    # === 3. CASOS REAIS ===
    print("\n\n  === 3. CALCULOS DE CASOS REAIS ===\n")
    # Fundador
    founder = LaborEntry(
        citizen_id = "founder", citizen_name="Cleiton",
        calculation_type = CalculationType.CONTRIBUTION,
        hours_worked = 4000,
        systems_created = 95,
        people_directly_impacted = 5000,
        ripple_factor = 5.0,
    )
    r = calc.calculate(founder)
    print("  CLEITON (fundador):")
    print("    {r.verdict}")
    print("    Impacto: {r.impact_score:,.0f}")
    print("    Credito: {r.credit_earned:.1f}")
    print("    Excesso: {'SIM -- Republica deve intervir' if r.excess_detected else 'not'}")
    # Medico
    medico = LaborEntry(
        citizen_id = "c-001", citizen_name="Ana (medica)",
        calculation_type = CalculationType.CONTRIBUTION,
        hours_worked = 1840,
        lives_saved = 50,
        people_directly_impacted = 800,
        ripple_factor = 2.0,
    )
    r = calc.calculate(medico)
    print("\n  ANA (medica):")
    print("    {r.verdict}")
    print("    Impacto: {r.impact_score:,.0f} (50 vidas salvas)")
    print("    Credito: {r.credit_earned:.1f}")
    # Professor
    prof = LaborEntry(
        citizen_id = "c-002", citizen_name="Maria (professora)",
        calculation_type = CalculationType.CONTRIBUTION,
        hours_worked = 920,
        people_directly_impacted = 300,
        ripple_factor = 10.0,
    )
    r = calc.calculate(prof)
    print("\n  MARIA (professora):")
    print("    {r.verdict}")
    print("    Impacto: {r.impact_score:,.0f}")
    print("    Credito: {r.credit_earned:.1f}")
    # Reparacao: crianca rotulada
    rep = LaborEntry(
        citizen_id = "c-100", citizen_name="Pedro (reparacao)",
        calculation_type = CalculationType.REPARATION,
        years_labeled = 11,
        is_child = True,
        years_on_medication = 8,
        harm_severity = 95,
    )
    r = calc.calculate(rep)
    print("\n  PEDRO (reparacao - crianca rotulada):")
    print("    {r.verdict}")
    print("    Horas reparacao: {r.hours_reparation:,.0f}h")
    print("    Credito: {r.credit_earned:.1f}")
    # === 4. RELATORIO ===
    print("\n\n  === 4. RELATORIO GERAL ===\n")
    s = calc.summary()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*70}")
    print("  A LEI MATEMATICA DA REPUBLICA")
    print("{'='*70}")
    print("""
UM SISTEMA, UMA FORMULA, ZERO EXCECOES:
TRABALHO (contribuicao):
    impacto = horas * (1 + log10(pessoas) * ripple)
    credito = clamp(impacto / 100, 5, 50)
    base = 920h/ano. max = 1840h/ano. LIMITE = 2300h/ano.
REPARACAO (dano sofrido):
    horas = anos * 920 + anos_medicado * 40
    horas = horas * 1.5 (severo) or 2.0 (crianca)
    credito = horas / 10
O QUE ISTO SIGNIFICA:
    1. TODO trabalho vale o mesmo por hora base (P3).
    2. Diferenca vem de IMPACTO, not de cargo.
    3. Medico que salva vida = impacto altissimo por pessoa.
    4. Professor que ensina 30 = impacto medio mas ripple 10x.
    5. Faxineiro que protege 200 de doenca = impacto real.
    6. Criador de 50 sistemas = reconhecimento FUNDADOR.
    7. Crianca rotulada errada = reparacao DOBRO.
    8. Quem trabalha > 2300h = Republica INTERVEM (P2).
O QUE not EXISTE:
    - Salario diferente por cargo (P3 anti-elitismo)
    - Comprar credito com dinheiro (sem moeda)
    - Acumular credito (expira por ciclo)
    - Herdar credito (morreu, zerou)
    - Trabalhar alem do limite (PROIBIDO por P2)
    - Reparacao em dinheiro (sem moeda)
    - Privilegio de fundador no calculo (1 voto)
A FORMULA and A VERDADE:
    Ninguem discute. Ninguem favorece.
    Os numeros sao os numeros.
    A justica and matematica.
# )
    print("{'='*70}")
    print("  OpenLaborPolicy: {s['total_calculations']} calculos realizados.")
    print("  Base 920h. Max 1840h. Limite 2300h. 1 formula. 0 excecoes.")
    print("{'='*70}")
