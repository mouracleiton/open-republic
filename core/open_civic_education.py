#!/usr/bin/env python3
"""
OpenCivicEducation -- Educacao Civica da Republica -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenCivicEducation -- Educacao Civica da Republica
=====================================================
"Tratar o outro com dignidade not and cortesia.
and DEVER CIVILIZATORIO.
A Republica not pede respeito -- EXIGE.
Quem not consegue conviver, APRENDE.
Quem se recusa a aprender, TEM ACOMPANHAMENTO."
O QUE ISTO FAZ:
1. DEFINE 12 deveres civicos (obrigatorios, not opcionais)
2. CRIA curriculo civico para TODOS (crianca, adulto, imigrante)
3. AVALIA convivencia (not nota -- acompanhamento)
4. INTERVEM quando alguem not consegue conviver
5. INTEGRA com OpenSymbolRevision, OpenRelationships, OpenMartialArts
PRINCIPIO:
Direitos and DEVERES sao duas faces da mesma moeda.
Voce TEM direito a moradia, saude, educacao, credito.
Voce TEM dever de tratar o proximo com dignidade.
Nao and opcional. Nao and "se voce quiser".
and a BASE da civilizacao.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional de typing
# importa Enum de enum
# importa defaultdict, Counter de collections
# importa datetime de datetime
# ============================================================================
# 1. OS 12 DEVERES CIVICOS
# ============================================================================
class CivicDuty(Enum):
    # Os 12 deveres civicos NAO opcionais da Republica.
    Estes not sao sugestoes. Sao CONDICOES de convivencia.
    Quem cumpre: cidadao pleno.
    Quem not cumpre: acompanhamento civico.
    Quem se recusa: OpenPenalRevision (violação de convivencia).
    # 
    RESPECT_DIGNITY = ("respeitar_dignidade",
        "Tratar TODO ser humano com dignidade. Sem excecao. Sem condicao.")
    NO_DISCRIMINATION = ("nao_discriminar",
        "Nao discriminar por raca, genero, idade, deficiencia, origem, "
        "orientacao, aparencia, or qualquer caracteristica.")
    NO_VIOLENCE = ("nao_violencia",
        "Nao iniciar violencia fisica or verbal. Autodefesa and direito (P2). "
        "Agredir primeiro and VIOLACAO.")
    SOLIDARITY = ("solidariedade",
        "Ajudar quem precisa. Nao virar o rosto. Se alguem cai, estende a mao.")
    CONTRIBUTE = ("contribuir",
        "Trabalhar (base 1.0 min). A Republica not sustenta ocioso "
        "que PODE and RECUSA contribuir.")
    RESPECT_AUTONOMY = ("respeitar_autonomia",
        "O corpo do outro and DELA. Ninguem decide pelo corpo de ninguem. "
        "P2 absoluta.")
    PROTECT_CHILDREN = ("proteger_criancas",
        "Toda crianca and responsabilidade de TODOS. "
        "Ver crianca em risco = INTERVIR. Sempre.")
    PROTECT_ENVIRONMENT = ("proteger_ambiente",
        "Nao destruir. Nao poluir. Nao desperdicar. "
        "O planeta and de quem ainda not nasceu.")
    HONESTY = ("honestidade",
        "Nao mentir para prejudicar. Nao enganar para lucrar. "
        "Nao espalhar desinformacao (OpenContentPolicy).")
    PARTICIPATE = ("participar",
        "Votar. Propor. Debater. Democracia PRECISA de voce (P4). "
        "Quem not participa, not tem direito de reclamar.")
    EDUCATE_SELF = ("auto_educar",
        "Aprender continuamente. OpenTerminal + OpenEducation disponivel. "
        "Ignorancia voluntaria and irresponsabilidade.")
    RESPECT_SHARED = ("respeitar_bem_comum",
        "Tudo and bem comum (CC0). Nao depredar. Nao monopolizar. "
        "Nao apropriar. Compartilhar.")
    # decorador: @property
    def label(self) -> str:
        return self.value[0]
    # decorador: @property
    def description(self) -> str:
        return self.value[1]
# ============================================================================
# 2. CURRICULO CIVICO
# ============================================================================
class CivicLevel(Enum):
    CHILD = "crianca"  // 6-11 anos
    TEEN = "adolescente"  // 12-17 anos
    ADULT = "adulto"  // 18+
    IMMIGRANT = "imigrante"  // chegou na Republica (qualquer idade)
    REFRESHER = "reciclagem"  // atualizacao periodica
# decorador: @dataclass
class CivicLesson:
    # Uma licao de educacao civica.
    lesson_id: texto
    duty: CivicDuty
    level: CivicLevel
    title: texto
    description: str = ""
    activity: str = ""  // o que fazer para praticar
    open_system_link: str = ""  // sistema da Republica conectado
    duration_min: int = 30
# Base de licoes
def build_civic_curriculum() -> [CivicLesson]:
    return [
        # === CRIANCA (6-11) ===
        CivicLesson("CIV-C01", CivicDuty.RESPECT_DIGNITY, CivicLevel.CHILD,
            "Todo Mundo Merece Respeito",
            "Aprender que cada pessoa tem valor. Ninguem and 'menor'.",
            "Roda de conversa: cada um diz uma qualidade do colega.",
            "OpenSymbolRevision (versao infantil)", 20),
        CivicLesson("CIV-C02", CivicDuty.NO_DISCRIMINATION, CivicLevel.CHILD,
            "Diferentes, Mas Iguais",
            "Cores, tamanhos, habilidades diferentes. Todos iguais em valor.",
            "Brincar de 'troca de lugar': sentir o que and ser o outro.",
            "OpenSymbolRevision + OpenTradition", 25),
        CivicLesson("CIV-C03", CivicDuty.SOLIDARITY, CivicLevel.CHILD,
            "Estender a Mao",
            "Se alguem cai, voce ajuda. Se alguem chora, voce pergunta.",
            "Ajudar um colega em tarefa dificil.",
            "OpenDignity (versao infantil)", 20),
        CivicLesson("CIV-C04", CivicDuty.PROTECT_CHILDREN, CivicLevel.CHILD,
            "Cuidar dos Pequenos",
            "Crianca menor precisa de ajuda. Voce que and maior ajuda.",
            "Cada um adota um colega mais novo por 1 semana.",
            "OpenMartialArts (auto-protecao)", 20),
        # === ADOLESCENTE (12-17) ===
        CivicLesson("CIV-T01", CivicDuty.RESPECT_DIGNITY, CivicLevel.TEEN,
            "Respeito Nao E Opcional",
            "Tratar o outro bem not and cortesia. E DEVER. "
            "Na Republica, respeito and LEI, not favor.",
            "Role-play: resolver conflito sem desrespeito.",
            "OpenSymbolRevision + OpenRelationships", 40),
        CivicLesson("CIV-T02", CivicDuty.NO_VIOLENCE, CivicLevel.TEEN,
            "Violencia Nao Resolve -- DEFESA Sim",
            "Agredir primeiro and VIOLACAO. Defender-se and DIREITO (P2). "
            "OpenMartialArts: aprender a se defender SEM agredir.",
            "Treino OpenMartialArts: desescalada + defesa.",
            "OpenMartialArts", 60),
        CivicLesson("CIV-T03", CivicDuty.PARTICIPATE, CivicLevel.TEEN,
            "Sua Voz Importa",
            "Democracia PRECISA de voce. Votar. Propor. Debater. "
            "Quem cala, consente.",
            "Simular assembleia: propor and votar uma mudanca na escola.",
            "OpenConstituentAssembly + OpenDemocracy", 45),
        CivicLesson("CIV-T04", CivicDuty.CONTRIBUTE, CivicLevel.TEEN,
            "Todo Mundo Contribui",
            "A Republica not sustenta ocioso que PODE and RECUSA. "
            "Trabalho and DEVER (base 1.0 min). Mas aprender tambem conta.",
            "Fazer 2h de trabalho comunitario (OpenLaborRelay).",
            "OpenLaborRelay + OpenLaborPolicy", 40),
        CivicLesson("CIV-T05", CivicDuty.RESPECT_AUTONOMY, CivicLevel.TEEN,
            "O Corpo and DELE",
            "Ninguem decide pelo corpo de ninguem. P2 absoluta. "
            "Consentimento. Autonomia. respeito aos limites.",
            "Workshop de consentimento and respeito corporal.",
            "OpenRelationships + OpenHealth", 45),
        # === ADULTO (18+) ===
        CivicLesson("CIV-A01", CivicDuty.RESPECT_DIGNITY, CivicLevel.ADULT,
            "Dever Civilizatorio",
            "Tratar o outro com dignidade not and cortesia. "
            "E DEVER CIVILIZATORIO. A Republica exige.",
            "Avaliacao civica: como voce trata quem and diferente?",
            "OpenSymbolRevision + OpenMentalHygiene", 30),
        CivicLesson("CIV-A02", CivicDuty.PARTICIPATE, CivicLevel.ADULT,
            "Participar or Calar",
            "Democracia precisa de voce. Votar not and opcao -- and DEVER. "
            "Assembleia constituinte DECIDE os parametros.",
            "Participar de 1 assembleia por ciclo.",
            "OpenConstituentAssembly", 60),
        CivicLesson("CIV-A03", CivicDuty.CONTRIBUTE, CivicLevel.ADULT,
            "Contribuir and Dever",
            "Base 1.0 min (assembleia votou). "
            "Ocioso que PODE and RECUSA: acompanhamento civico.",
            "Registrar horas no OpenLaborRelay.",
            "OpenLaborPolicy + OpenLaborRelay", 20),
        CivicLesson("CIV-A04", CivicDuty.PROTECT_ENVIRONMENT, CivicLevel.ADULT,
            "Planeta not and Seu",
            "O planeta and de quem ainda not nasceu. "
            "Nao poluir. Nao desperdicar. Reciclar (OpenRecyclers).",
            "Fazer 1 coleta com catador (OpenRecyclers).",
            "OpenRecyclers + OpenSustainability", 40),
        CivicLesson("CIV-A05", CivicDuty.HONESTY, CivicLevel.ADULT,
            "Desinformacao and Crime Civico",
            "Espalhar mentira com dano real = VIOLACAO. "
            "OpenContentPolicy bloqueia. OpenHistory fact-check.",
            "Verificar 1 noticia antes de compartilhar.",
            "OpenContentPolicy + OpenHistory", 30),
        # === IMIGRANTE ===
        CivicLesson("CIV-I01", CivicDuty.RESPECT_DIGNITY, CivicLevel.IMMIGRANT,
            "Bem-vindo a Republica",
            "Voce and cidadao. Tem os mesmos direitos E DEVERES. "
            "Tratar todos com dignidade and regra AQUI tambem.",
            "Tour civico: conhecer sistemas da Republica.",
            "OpenKit + OpenTerminal", 60),
        CivicLesson("CIV-I02", CivicDuty.PARTICIPATE, CivicLevel.IMMIGRANT,
            "Sua Voz Conta Aqui",
            "Voce vota. Voce propoe. Voce and PARTE da Republica.",
            "Registrar-se no OpenDemocracy.",
            "OpenConstituentAssembly", 30),
        # === RECICLAGEM (todos, periodico) ===
        CivicLesson("CIV-R01", CivicDuty.RESPECT_DIGNITY, CivicLevel.REFRESHER,
            "Reciclagem: Continua Valendo",
            "Respeito not expira. Dever not tem ferias. "
            "Reciclar = lembrar por que convivemos.",
            "Auto-avaliacao civica no OpenTerminal.",
            "OpenTerminal + OpenProfessions", 20),
    ]
# ============================================================================
# 3. AVALIACAO DE CONVIVENCIA
# ============================================================================
class ConductRating(Enum):
    EXCELLENT = ("excelente", 5, "Exemplo de convivencia")
    GOOD = ("bom", 4, "Cumpre deveres, ajuda outros")
    ADEQUATE = ("adequado", 3, "Cumpre o basico")
    NEEDS_WORK = ("precisa_melhorar", 2, "Falta em alguns deveres")
    INTERVENTION = ("intervencao", 1, "Nao consegue conviver -- acompanhamento")
    VIOLATION = ("violacao", 0, "Viola direitos de outros -- OpenPenalRevision")
    # decorador: @property
    def label(self) -> str:
        return self.value[0]
    # decorador: @property
    def score(self) -> int:
        return self.value[1]
    # decorador: @property
    def meaning(self) -> str:
        return self.value[2]
# decorador: @dataclass
class CivicAssessment:
    # Avaliacao de convivencia de um cidadao.
    not and nota escolar. not and ranking.
    and ACOMPANHAMENTO para garantir que TODOS convivem.
    # 
    citizen_id: texto
    citizen_name: texto
    assessment_date: str = ""
    ratings: {texto: ConductRating} = field(default_factory=dict)
    overall: ConductRating = ConductRating.ADEQUATE
    needs_accompaniment: bool = False
    notes: str = ""
# ============================================================================
# 4. MOTOR DE EDUCACAO CIVICA
# ============================================================================
class CivicEducationEngine:
    # Motor de educacao civica da Republica.
    O QUE FAZ:
    1. ENSINA os 12 deveres (curriculo por idade)
    2. AVALIA convivencia (acompanhamento, not punicao)
    3. INTERVEM quando alguem not consegue conviver
    4. REFORCA que tratar bem not and OPCIONAL
    O QUE not FAZ:
    - Punir quem 'tirou nota baixa' (not and prova)
    - Criar ranking de 'melhor cidadao' (not and competicao)
    - Forcar conformidade (P2 -- mas convivencia tem regras)
    O QUE FAZ:
    - EDUCAR continuamente (OpenSchool + OpenUniversity)
    - ACOMPANHAR quem tem dificuldade
    - INTERVIR quando ha risco a outros
    - REFORCAR que dever and DEVER (not sugestao)
    # 
    def __init__(self):
        self.curriculum: [CivicLesson] = build_civic_curriculum()
        self.assessments: {texto: CivicAssessment} = {}
    def get_curriculum(self, level: CivicLevel) -> [Dict]:
        # Retorna curriculo civico para um nivel.
        lessons = [l para l em self.curriculum if l.level == level]
        return [
            {
                "lesson": l.title,
                "duty": l.duty.label,
                "description": l.description,
                "activity": l.activity,
                "system": l.open_system_link,
                "duration": "{l.duration_min} min",
            }
            para l in lessons
        ]
    def list_duties(self) -> [Dict]:
        # Lista os 12 deveres civicos.
        return [
            {"duty": d.label, "description": d.description}
            para d in CivicDuty
        ]
    funcao assess_citizen(self, citizen_id: texto, citizen_name: texto,
                    ratings: {texto: inteiro} = None) -> {texto: qualquer}:
        # Avalia convivencia (acompanhamento, nao nota).
        ratings: dicionario com dever -> score (0-5)
        # 
        if ratings and None:
            ratings = {d.label: 3 para d em CivicDuty} // default: adequado
        conduct_ratings = {}
        for each (duty_label, score) in ratings.items():
            conduct_ratings[duty_label] = self._score_to_rating(score)
        avg_score = sum(r.score para r em conduct_ratings.values()) / max(len(conduct_ratings), 1)
        if avg_score >= 4.5:
            overall = ConductRating.EXCELLENT
        elif avg_score >= 3.5:
            overall = ConductRating.GOOD
        elif avg_score >= 2.5:
            overall = ConductRating.ADEQUATE
        elif avg_score >= 1.5:
            overall = ConductRating.NEEDS_WORK
        elif avg_score >= 0.5:
            overall = ConductRating.INTERVENTION
            needs_accomp = True
        else:
            overall = ConductRating.VIOLATION
            needs_accomp = True
        needs_accomp = overall.score <= 1
        assessment = CivicAssessment(
            citizen_id = citizen_id, citizen_name=citizen_name,
            assessment_date = datetime.now().isoformat(),
            ratings = conduct_ratings,
            overall = overall,
            needs_accompaniment = needs_accomp,
        )
        self.assessments[citizen_id] = assessment
        result = {
            "citizen": citizen_name,
            "overall": overall.label,
            "meaning": overall.meaning,
            "needs_accompaniment": needs_accomp,
            "ratings": {k: v.label para k, v in conduct_ratings.items()},
        }
        if needs_accomp:
            result["action"] = self._intervention_plan(overall)
        else:
            result["action"] = "Continuar. Voce cumpre seus deveres."
        return result
    def _score_to_rating(self, score: inteiro) -> ConductRating:
        if score >= 5:
            return ConductRating.EXCELLENT
        if score >= 4:
            return ConductRating.GOOD
        if score >= 3:
            return ConductRating.ADEQUATE
        if score >= 2:
            return ConductRating.NEEDS_WORK
        if score >= 1:
            return ConductRating.INTERVENTION
        return ConductRating.VIOLATION
    def _intervention_plan(self, rating: ConductRating) -> str:
        if rating == ConductRating.INTERVENTION:
            return (
                "ACOMPANHAMENTO CIVICO: mentor designado. "
                "Licoes civicas reforçadas. "
                "OpenPsychology (sem rotular) se necessario. "
                "Objetivo: APRENDER a conviver. Nao punir."
            )
        if rating == ConductRating.VIOLATION:
            return (
                "VIOLACAO DE CONVIVENCIA: OpenPenalRevision avalia. "
                "Se violou direitos de outros: transformacao (not punicao). "
                "OpenReintegration: ressocializacao com infraestrutura."
            )
        return "Acompanhamento leve. Reforco civico."
    funcao intervention_report(self, citizen_id: texto,
                            issue: texto) -> {texto: qualquer}:
        # Reporta problema de convivencia e gera plano.
        assessment = self.assessments.get(citizen_id, CivicAssessment(
            citizen_id = citizen_id, citizen_name="Cidadao"))
        return {
            "citizen": assessment.citizen_name,
            "issue": issue,
            "plan": self._intervention_plan(assessment.overall),
            "systems": [
                "OpenSymbolRevision (corrigir preconceito)",
                "OpenPsychology (entender causa)",
                "OpenMartialArts (desescalar conflito)",
                "OpenRelationships (respeitar espaco)",
                "OpenTerminal (continuar aprendendo)",
            ],
            "message": (
                "Problema: {issue}. "
                "A Republica INTERVEM. Nao para punir. Para ENSINAR. "
                "Se aprender: cidadao pleno. "
                "Se recusar: acompanhamento intensifica."
            ),
        }
    def stats(self) -> {texto: qualquer}:
        by_rating = Counter(a.overall.label para a em self.assessments.values())
        return {
            "total_deveres": len(CivicDuty),
            "total_licoes": len(self.curriculum),
            "total_avaliados": len(self.assessments),
            "by_rating": dict(by_rating),
            "precisam_acompanhamento": sum(
                1 para a em self.assessments.values() if a.needs_accompaniment),
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = CivicEducationEngine()
    print("=" * 80)
    print("  OPENCIVICEDUCATION -- EDUCACAO CIVICA DA REPUBLICA")
    print("  'Tratar o outro com dignidade not and cortesia. E DEVER.'")
    print("=" * 80)
    # === 1. OS 12 DEVERES ===
    print("\n\n  === 1. OS 12 DEVERES CIVICOS (NAO opcionais) ===\n")
    for each (i, duty) in enumere(CivicDuty, 1):
        print("  {i:>2}. [{duty.label}]")
        print("      {duty.description}")
    # === 2. CURRICULO POR IDADE ===
    print("\n\n  === 2. CURRICULO CIVICO POR IDADE ===\n")
    for level in CivicLevel:
        lessons = engine.get_curriculum(level)
        if lessons:
            print("\n  {level.value.upper()} ({len(lessons)} licoes):")
            for l in lessons[:3]:
                print("    [{l['duty']}] {l['lesson']}")
                print("      {l['description'][:60]}...")
                print("      Atividade: {l['activity'][:50]}...")
    # === 3. AVALIACAO DE CONVIVENCIA ===
    print("\n\n  === 3. AVALIACAO DE CONVIVENCIA (acompanhamento) ===\n")
    assessments = [
        ("C-001", "Maria", {
            "respeitar_dignidade": 5, "nao_discriminar": 5,
            "nao_violencia": 5, "solidariedade": 5,
            "contribuir": 5, "respeitar_autonomia": 5,
            "proteger_criancas": 5, "proteger_ambiente": 4,
            "honestidade": 5, "participar": 4,
            "auto_educar": 4, "respeitar_bem_comum": 5,
        }),
        ("C-002", "Carlos", {
            "respeitar_dignidade": 3, "nao_discriminar": 2,
            "nao_violencia": 3, "solidariedade": 2,
            "contribuir": 3, "respeitar_autonomia": 4,
            "proteger_criancas": 3, "proteger_ambiente": 2,
            "honestidade": 3, "participar": 2,
            "auto_educar": 2, "respeitar_bem_comum": 3,
        }),
        ("C-003", "Pedro (problema)", {
            "respeitar_dignidade": 1, "nao_discriminar": 0,
            "nao_violencia": 1, "solidariedade": 1,
            "contribuir": 2, "respeitar_autonomia": 1,
            "proteger_criancas": 2, "proteger_ambiente": 1,
            "honestidade": 1, "participar": 1,
            "auto_educar": 1, "respeitar_bem_comum": 1,
        }),
    ]
    para cid, name, ratings in assessments:
        r = engine.assess_citizen(cid, name, ratings)
        print("\n  {r['citizen']:<20} -> {r['overall'].upper()}")
        print("  {r['meaning']}")
        if r["needs_accompaniment"]:
            print("  [!] ACOMPANHAMENTO: {r['action'][:70]}...")
        else:
            print("  {r['action']}")
    # === 4. INTERVENCAO ===
    print("\n\n  === 4. INTERVENCAO (not punir -- ENSINAR) ===\n")
    intervention = engine.intervention_report(
        "C-003", "Discriminou colega por cor de pele + recusou trabalhar")
    print("  Cidadao: {intervention['citizen']}")
    print("  Problema: {intervention['issue']}")
    print("  Plano: {intervention['plan'][:80]}...")
    print("  Sistemas: {', '.join(intervention['systems'][:3])}")
    print("  {intervention['message'][:80]}...")
    # === 5. STATS ===
    print("\n\n  === 5. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA DA EDUCACAO CIVICA")
    print("{'='*80}")
    print("""
"TRATAR O OUTRO COM DIGNIDADE not and CORTESIA.
and DEVER CIVILIZATORIO."
A frase melhorada:
    Nao: "tratar o outro bem not and opcional"
    Sim: "Tratar o outro com dignidade and DEVER CIVILIZATORIO.
        Nao and cortesia. Nao and favor. Nao and 'se voce quiser'.
        and a BASE da Republica. Quem not consegue, APRENDE.
        Quem se recusa, TEM ACOMPANHAMENTO."
DIREITOS and DEVERES (duas faces):
    Voce TEM direitos:
    - Moradia, saude, educacao, credito, trabalho, voz.
    - A Republica GARANTE. Custo ZERO.
    Voce TEM deveres:
    - Respeitar dignidade alheia.
    - Nao discriminar.
    - Nao agredir.
    - Contribuir (base 1.0).
    - Participar (votar, propor).
    - Proteger criancas.
    - Proteger ambiente.
    - Ser honesto.
    - Respeitar autonomia corporal.
    - Solidariedade.
    - Auto-educar.
    - Respeitar bem comum.
    DIREITO sem DEVER = exploracao.
    DEVER sem DIREITO = opressao.
    A Republica garante OS DOIS.
12 DEVERES (todos iguais em importancia -- P1):
    1. Respeitar dignidade (TODO ser humano, sem excecao)
    2. Nao discriminar (raca, genero, idade, deficiencia, nada)
    3. Nao iniciar violencia (defesa and direito, agressao and crime)
    4. Solidariedade (ajudar quem cai, not virar rosto)
    5. Contribuir (trabalho base 1.0 -- not sustenta ocioso que recusa)
    6. Respeitar autonomia (corpo do outro and DELA -- P2)
    7. Proteger criancas (responsabilidade de TODOS)
    8. Proteger ambiente (planeta and de quem not nasceu)
    9. Honestidade (not mentir, not enganar, not desinformar)
    10. Participar (votar, propor, debater -- P4)
    11. Auto-educar (ignorancia voluntaria and irresponsabilidade)
    12. Respeitar bem comum (tudo and CC0, not apropriar)
COMO A REPUBLICA LIDA COM QUEM not CUMPRE:
    1. PRECISA_MELHORAR: reforgo civico (OpenTerminal)
    2. INTERVENCAO: mentor designado + OpenPsychology (sem rotular)
    3. VIOLACAO: OpenPenalRevision (transformacao, not punicao)
    NUNCA: punir sem tentar ensinar.
    SEMPRE: educar primeiro. Intervir depois. Transformar por ultimo.
EDUCACAO CONTINUA:
    Crianca (6-11): aprender respeito na pratica
    Adolescente (12-17): participacao + defesa + consentimento
    Adulto (18+): votar + contribuir + proteger
    Imigrante: bem-vindo, mesmos direitos and deveres
    Reciclagem: todo ciclo, auto-avaliacao civica
PRINCIPIOS:
    P1: Todos tem os mesmos deveres. Sem excecao para rico/pobre/fundador.
    P2: Autonomia corporal protegida. Mas convivencia tem regras.
    P3: Contribuir and dever. Ocioso que recusa tem acompanhamento.
    P4: Participar and dever. Democracia precisa de TODO mundo.
# )
    print("{'='*80}")
    print("  OpenCivicEducation: {s['total_deveres']} deveres, "
        "{s['total_licoes']} licoes, "
        "{s['precisam_acompanhamento']} precisam de acompanhamento.")
    print("  Tratar o outro bem and DEVER. Nao cortesia.")
    print("{'='*80}")
