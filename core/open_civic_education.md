# OpenCivicEducation -- Educacao Civica da Republica

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_civic_education.py`

**Descricao:** =====================================================
"Tratar o outro com dignidade nao e cortesia.
 E DEVER CIVILIZATORIO.
 A Republica nao pede respeito -- EXIGE.
 Quem nao consegue conviver, APRENDE.
 Quem se recusa a aprender, TEM ACOMPANHAMENTO."
O QUE ISTO FAZ:
  1. DEFINE 12 deveres civicos (obrigatorios, nao opcionais)
  2. CRIA curriculo civico para TODOS (crianca, adulto, imigrante)
  3. AVALIA convivencia (nao nota -- acompanhamento)
  4. INTERVEM quando alguem nao consegue conviver
  5. INTEGRA com OpenSymbolRevision, OpenRelationships, OpenMartialArts
PRINCIPIO:
  Direitos e DEVERES sao duas faces da mesma moeda.
  Voce TEM direito a moradia, saude, educacao, credito.
  Voce TEM dever de tratar o proximo com dignidade.
  Nao e opcional. Nao e "se voce quiser".
  E a BASE da civilizacao.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenCivicEducation -- Educacao Civica da Republica
=====================================================

"Tratar o outro com dignidade nao e cortesia.
 e DEVER CIVILIZATORIO.
 A Republica nao pede respeito -- EXIGE.
 Quem nao consegue conviver, APRENDE.
 Quem se recusa a aprender, TEM ACOMPANHAMENTO."

O QUE ISTO FAZ:
  1. DEFINE 12 deveres civicos (obrigatorios, nao opcionais)
  2. CRIA curriculo civico para TODOS (crianca, adulto, imigrante)
  3. AVALIA convivencia (nao nota -- acompanhamento)
  4. INTERVEM quando alguem nao consegue conviver
  5. INTEGRA com OpenSymbolRevision, OpenRelationships, OpenMartialArts

PRINCIPIO:
  Direitos e DEVERES sao duas faces da mesma moeda.
  Voce TEM direito a moradia, saude, educacao, credito.
  Voce TEM dever de tratar o proximo com dignidade.
  Nao e opcional. Nao e "se voce quiser".
  e a BASE da civilizacao.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime


// ============================================================================
// 1. OS 12 DEVERES CIVICOS
// ============================================================================

classe CivicDuty herda de Enum:
    // Os 12 deveres civicos NAO opcionais da Republica.

    Estes nao sao sugestoes. Sao CONDICOES de convivencia.
    Quem cumpre: cidadao pleno.
    Quem nao cumpre: acompanhamento civico.
    Quem se recusa: OpenPenalRevision (violação de convivencia).
    // 
    RESPECT_DIGNITY = ("respeitar_dignidade",
        "Tratar TODO ser humano com dignidade. Sem excecao. Sem condicao.")
    NO_DISCRIMINATION = ("nao_discriminar",
        "Nao discriminar por raca, genero, idade, deficiencia, origem, "
        "orientacao, aparencia, ou qualquer caracteristica.")
    NO_VIOLENCE = ("nao_violencia",
        "Nao iniciar violencia fisica ou verbal. Autodefesa e direito (P2). "
        "Agredir primeiro e VIOLACAO.")
    SOLIDARITY = ("solidariedade",
        "Ajudar quem precisa. Nao virar o rosto. Se alguem cai, estende a mao.")
    CONTRIBUTE = ("contribuir",
        "Trabalhar (base 1.0 minimo). A Republica nao sustenta ocioso "
        "que PODE e RECUSA contribuir.")
    RESPECT_AUTONOMY = ("respeitar_autonomia",
        "O corpo do outro e DELA. Ninguem decide pelo corpo de ninguem. "
        "P2 absoluta.")
    PROTECT_CHILDREN = ("proteger_criancas",
        "Toda crianca e responsabilidade de TODOS. "
        "Ver crianca em risco = INTERVIR. Sempre.")
    PROTECT_ENVIRONMENT = ("proteger_ambiente",
        "Nao destruir. Nao poluir. Nao desperdicar. "
        "O planeta e de quem ainda nao nasceu.")
    HONESTY = ("honestidade",
        "Nao mentir para prejudicar. Nao enganar para lucrar. "
        "Nao espalhar desinformacao (OpenContentPolicy).")
    PARTICIPATE = ("participar",
        "Votar. Propor. Debater. Democracia PRECISA de voce (P4). "
        "Quem nao participa, nao tem direito de reclamar.")
    EDUCATE_SELF = ("auto_educar",
        "Aprender continuamente. OpenTerminal + OpenEducation disponivel. "
        "Ignorancia voluntaria e irresponsabilidade.")
    RESPECT_SHARED = ("respeitar_bem_comum",
        "Tudo e bem comum (CC0). Nao depredar. Nao monopolizar. "
        "Nao apropriar. Compartilhar.")

    // decorador: @property
    funcao label(self) -> texto:
        retorne self.value[0]

    // decorador: @property
    funcao description(self) -> texto:
        retorne self.value[1]


// ============================================================================
// 2. CURRICULO CIVICO
// ============================================================================

classe CivicLevel herda de Enum:
    CHILD = "crianca"  // 6-11 anos
    TEEN = "adolescente"  // 12-17 anos
    ADULT = "adulto"  // 18+
    IMMIGRANT = "imigrante"  // chegou na Republica (qualquer idade)
    REFRESHER = "reciclagem"  // atualizacao periodica


// decorador: @dataclass
classe CivicLesson:
    // Uma licao de educacao civica.
    lesson_id: texto
    duty: CivicDuty
    level: CivicLevel
    title: texto
    seja description: texto = ""
    seja activity: texto = ""  // o que fazer para praticar
    seja open_system_link: texto = ""  // sistema da Republica conectado
    seja duration_min: inteiro = 30


// Base de licoes
funcao build_civic_curriculum() -> [CivicLesson]:
    retorne [
        // === CRIANCA (6-11) ===
        CivicLesson("CIV-C01", CivicDuty.RESPECT_DIGNITY, CivicLevel.CHILD,
            "Todo Mundo Merece Respeito",
            "Aprender que cada pessoa tem valor. Ninguem e 'menor'.",
            "Roda de conversa: cada um diz uma qualidade do colega.",
            "OpenSymbolRevision (versao infantil)", 20),
        CivicLesson("CIV-C02", CivicDuty.NO_DISCRIMINATION, CivicLevel.CHILD,
            "Diferentes, Mas Iguais",
            "Cores, tamanhos, habilidades diferentes. Todos iguais em valor.",
            "Brincar de 'troca de lugar': sentir o que e ser o outro.",
            "OpenSymbolRevision + OpenTradition", 25),
        CivicLesson("CIV-C03", CivicDuty.SOLIDARITY, CivicLevel.CHILD,
            "Estender a Mao",
            "Se alguem cai, voce ajuda. Se alguem chora, voce pergunta.",
            "Ajudar um colega em tarefa dificil.",
            "OpenDignity (versao infantil)", 20),
        CivicLesson("CIV-C04", CivicDuty.PROTECT_CHILDREN, CivicLevel.CHILD,
            "Cuidar dos Pequenos",
            "Crianca menor precisa de ajuda. Voce que e maior ajuda.",
            "Cada um adota um colega mais novo por 1 semana.",
            "OpenMartialArts (auto-protecao)", 20),

        // === ADOLESCENTE (12-17) ===
        CivicLesson("CIV-T01", CivicDuty.RESPECT_DIGNITY, CivicLevel.TEEN,
            "Respeito Nao E Opcional",
            "Tratar o outro bem nao e cortesia. E DEVER. "
            "Na Republica, respeito e LEI, nao favor.",
            "Role-play: resolver conflito sem desrespeito.",
            "OpenSymbolRevision + OpenRelationships", 40),
        CivicLesson("CIV-T02", CivicDuty.NO_VIOLENCE, CivicLevel.TEEN,
            "Violencia Nao Resolve -- DEFESA Sim",
            "Agredir primeiro e VIOLACAO. Defender-se e DIREITO (P2). "
            "OpenMartialArts: aprender a se defender SEM agredir.",
            "Treino OpenMartialArts: desescalada + defesa.",
            "OpenMartialArts", 60),
        CivicLesson("CIV-T03", CivicDuty.PARTICIPATE, CivicLevel.TEEN,
            "Sua Voz Importa",
            "Democracia PRECISA de voce. Votar. Propor. Debater. "
            "Quem cala, consente.",
            "Simular assembleia: propor e votar uma mudanca na escola.",
            "OpenConstituentAssembly + OpenDemocracy", 45),
        CivicLesson("CIV-T04", CivicDuty.CONTRIBUTE, CivicLevel.TEEN,
            "Todo Mundo Contribui",
            "A Republica nao sustenta ocioso que PODE e RECUSA. "
            "Trabalho e DEVER (base 1.0 minimo). Mas aprender tambem conta.",
            "Fazer 2h de trabalho comunitario (OpenLaborRelay).",
            "OpenLaborRelay + OpenLaborPolicy", 40),
        CivicLesson("CIV-T05", CivicDuty.RESPECT_AUTONOMY, CivicLevel.TEEN,
            "O Corpo e DELE",
            "Ninguem decide pelo corpo de ninguem. P2 absoluta. "
            "Consentimento. Autonomia. respeito aos limites.",
            "Workshop de consentimento e respeito corporal.",
            "OpenRelationships + OpenHealth", 45),

        // === ADULTO (18+) ===
        CivicLesson("CIV-A01", CivicDuty.RESPECT_DIGNITY, CivicLevel.ADULT,
            "Dever Civilizatorio",
            "Tratar o outro com dignidade nao e cortesia. "
            "E DEVER CIVILIZATORIO. A Republica exige.",
            "Avaliacao civica: como voce trata quem e diferente?",
            "OpenSymbolRevision + OpenMentalHygiene", 30),
        CivicLesson("CIV-A02", CivicDuty.PARTICIPATE, CivicLevel.ADULT,
            "Participar ou Calar",
            "Democracia precisa de voce. Votar nao e opcao -- e DEVER. "
            "Assembleia constituinte DECIDE os parametros.",
            "Participar de 1 assembleia por ciclo.",
            "OpenConstituentAssembly", 60),
        CivicLesson("CIV-A03", CivicDuty.CONTRIBUTE, CivicLevel.ADULT,
            "Contribuir e Dever",
            "Base 1.0 minimo (assembleia votou). "
            "Ocioso que PODE e RECUSA: acompanhamento civico.",
            "Registrar horas no OpenLaborRelay.",
            "OpenLaborPolicy + OpenLaborRelay", 20),
        CivicLesson("CIV-A04", CivicDuty.PROTECT_ENVIRONMENT, CivicLevel.ADULT,
            "Planeta nao e Seu",
            "O planeta e de quem ainda nao nasceu. "
            "Nao poluir. Nao desperdicar. Reciclar (OpenRecyclers).",
            "Fazer 1 coleta com catador (OpenRecyclers).",
            "OpenRecyclers + OpenSustainability", 40),
        CivicLesson("CIV-A05", CivicDuty.HONESTY, CivicLevel.ADULT,
            "Desinformacao e Crime Civico",
            "Espalhar mentira com dano real = VIOLACAO. "
            "OpenContentPolicy bloqueia. OpenHistory fact-check.",
            "Verificar 1 noticia antes de compartilhar.",
            "OpenContentPolicy + OpenHistory", 30),

        // === IMIGRANTE ===
        CivicLesson("CIV-I01", CivicDuty.RESPECT_DIGNITY, CivicLevel.IMMIGRANT,
            "Bem-vindo a Republica",
            "Voce e cidadao. Tem os mesmos direitos E DEVERES. "
            "Tratar todos com dignidade e regra AQUI tambem.",
            "Tour civico: conhecer sistemas da Republica.",
            "OpenKit + OpenTerminal", 60),
        CivicLesson("CIV-I02", CivicDuty.PARTICIPATE, CivicLevel.IMMIGRANT,
            "Sua Voz Conta Aqui",
            "Voce vota. Voce propoe. Voce e PARTE da Republica.",
            "Registrar-se no OpenDemocracy.",
            "OpenConstituentAssembly", 30),

        // === RECICLAGEM (todos, periodico) ===
        CivicLesson("CIV-R01", CivicDuty.RESPECT_DIGNITY, CivicLevel.REFRESHER,
            "Reciclagem: Continua Valendo",
            "Respeito nao expira. Dever nao tem ferias. "
            "Reciclar = lembrar por que convivemos.",
            "Auto-avaliacao civica no OpenTerminal.",
            "OpenTerminal + OpenProfessions", 20),
    ]


// ============================================================================
// 3. AVALIACAO DE CONVIVENCIA
// ============================================================================

classe ConductRating herda de Enum:
    EXCELLENT = ("excelente", 5, "Exemplo de convivencia")
    GOOD = ("bom", 4, "Cumpre deveres, ajuda outros")
    ADEQUATE = ("adequado", 3, "Cumpre o basico")
    NEEDS_WORK = ("precisa_melhorar", 2, "Falta em alguns deveres")
    INTERVENTION = ("intervencao", 1, "Nao consegue conviver -- acompanhamento")
    VIOLATION = ("violacao", 0, "Viola direitos de outros -- OpenPenalRevision")

    // decorador: @property
    funcao label(self) -> texto:
        retorne self.value[0]

    // decorador: @property
    funcao score(self) -> inteiro:
        retorne self.value[1]

    // decorador: @property
    funcao meaning(self) -> texto:
        retorne self.value[2]


// decorador: @dataclass
classe CivicAssessment:
    // Avaliacao de convivencia de um cidadao.

    nao e nota escolar. nao e ranking.
    e ACOMPANHAMENTO para garantir que TODOS convivem.
    // 
    citizen_id: texto
    citizen_name: texto
    seja assessment_date: texto = ""
    seja ratings: {texto: ConductRating} = field(default_factory=dict)
    seja overall: ConductRating = ConductRating.ADEQUATE
    seja needs_accompaniment: logico = falso
    seja notes: texto = ""


// ============================================================================
// 4. MOTOR DE EDUCACAO CIVICA
// ============================================================================

classe CivicEducationEngine:
    // Motor de educacao civica da Republica.

    O QUE FAZ:
    1. ENSINA os 12 deveres (curriculo por idade)
    2. AVALIA convivencia (acompanhamento, nao punicao)
    3. INTERVEM quando alguem nao consegue conviver
    4. REFORCA que tratar bem nao e OPCIONAL

    O QUE nao FAZ:
    - Punir quem 'tirou nota baixa' (nao e prova)
    - Criar ranking de 'melhor cidadao' (nao e competicao)
    - Forcar conformidade (P2 -- mas convivencia tem regras)

    O QUE FAZ:
    - EDUCAR continuamente (OpenSchool + OpenUniversity)
    - ACOMPANHAR quem tem dificuldade
    - INTERVIR quando ha risco a outros
    - REFORCAR que dever e DEVER (nao sugestao)
    // 

    funcao __init__(self):
        self.curriculum: [CivicLesson] = build_civic_curriculum()
        self.assessments: {texto: CivicAssessment} = {}

    funcao get_curriculum(self, level: CivicLevel) -> [Dict]:
        // Retorna curriculo civico para um nivel.
        lessons = [l para l em self.curriculum if l.level == level]
        retorne [
            {
                "lesson": l.title,
                "duty": l.duty.label,
                "description": l.description,
                "activity": l.activity,
                "system": l.open_system_link,
                "duration": "{l.duration_min} min",
            }
            para l em lessons
        ]

    funcao list_duties(self) -> [Dict]:
        // Lista os 12 deveres civicos.
        retorne [
            {"duty": d.label, "description": d.description}
            para d em CivicDuty
        ]

    funcao assess_citizen(self, citizen_id: texto, citizen_name: texto,
                       seja ratings: {texto: inteiro} = nulo) -> {texto: qualquer}:
        // Avalia convivencia (acompanhamento, nao nota).

        ratings: dicionario com dever -> score (0-5)
        // 
        se ratings e nulo entao:
            ratings = {d.label: 3 para d em CivicDuty} // default: adequado

        conduct_ratings = {}
        para cada (duty_label, score) em ratings.items():
            conduct_ratings[duty_label] = self._score_to_rating(score)

        avg_score = soma(r.score para r em conduct_ratings.values()) / maximo(tamanho(conduct_ratings), 1)

        se avg_score >= 4.5 entao:
            overall = ConductRating.EXCELLENT
        senao se avg_score >= 3.5 entao:
            overall = ConductRating.GOOD
        senao se avg_score >= 2.5 entao:
            overall = ConductRating.ADEQUATE
        senao se avg_score >= 1.5 entao:
            overall = ConductRating.NEEDS_WORK
        senao se avg_score >= 0.5 entao:
            overall = ConductRating.INTERVENTION
            needs_accomp = verdadeiro
        senao:
            overall = ConductRating.VIOLATION
            needs_accomp = verdadeiro

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

        se needs_accomp entao:
            result["action"] = self._intervention_plan(overall)
        senao:
            result["action"] = "Continuar. Voce cumpre seus deveres."

        retorne result

    funcao _score_to_rating(self, score: inteiro) -> ConductRating:
        se score >= 5 entao:
            retorne ConductRating.EXCELLENT
        se score >= 4 entao:
            retorne ConductRating.GOOD
        se score >= 3 entao:
            retorne ConductRating.ADEQUATE
        se score >= 2 entao:
            retorne ConductRating.NEEDS_WORK
        se score >= 1 entao:
            retorne ConductRating.INTERVENTION
        retorne ConductRating.VIOLATION

    funcao _intervention_plan(self, rating: ConductRating) -> texto:
        se rating == ConductRating.INTERVENTION entao:
            retorne (
                "ACOMPANHAMENTO CIVICO: mentor designado. "
                "Licoes civicas reforçadas. "
                "OpenPsychology (sem rotular) se necessario. "
                "Objetivo: APRENDER a conviver. Nao punir."
            )
        se rating == ConductRating.VIOLATION entao:
            retorne (
                "VIOLACAO DE CONVIVENCIA: OpenPenalRevision avalia. "
                "Se violou direitos de outros: transformacao (nao punicao). "
                "OpenReintegration: ressocializacao com infraestrutura."
            )
        retorne "Acompanhamento leve. Reforco civico."

    funcao intervention_report(self, citizen_id: texto,
                            issue: texto) -> {texto: qualquer}:
        // Reporta problema de convivencia e gera plano.
        assessment = self.assessments.get(citizen_id, CivicAssessment(
            citizen_id = citizen_id, citizen_name="Cidadao"))

        retorne {
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

    funcao stats(self) -> {texto: qualquer}:
        by_rating = Counter(a.overall.label para a em self.assessments.values())
        retorne {
            "total_deveres": tamanho(CivicDuty),
            "total_licoes": tamanho(self.curriculum),
            "total_avaliados": tamanho(self.assessments),
            "by_rating": dict(by_rating),
            "precisam_acompanhamento": soma(
                1 para a em self.assessments.values() if a.needs_accompaniment),
        }


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = CivicEducationEngine()

    imprima("=" * 80)
    imprima("  OPENCIVICEDUCATION -- EDUCACAO CIVICA DA REPUBLICA")
    imprima("  'Tratar o outro com dignidade nao e cortesia. E DEVER.'")
    imprima("=" * 80)

    // === 1. OS 12 DEVERES ===
    imprima("\n\n  === 1. OS 12 DEVERES CIVICOS (NAO opcionais) ===\n")
    para cada (i, duty) em enumere(CivicDuty, 1):
        imprima("  {i:>2}. [{duty.label}]")
        imprima("      {duty.description}")

    // === 2. CURRICULO POR IDADE ===
    imprima("\n\n  === 2. CURRICULO CIVICO POR IDADE ===\n")
    para cada level em CivicLevel:
        lessons = engine.get_curriculum(level)
        se lessons entao:
            imprima("\n  {level.value.upper()} ({len(lessons)} licoes):")
            para cada l em lessons[:3]:
                imprima("    [{l['duty']}] {l['lesson']}")
                imprima("      {l['description'][:60]}...")
                imprima("      Atividade: {l['activity'][:50]}...")

    // === 3. AVALIACAO DE CONVIVENCIA ===
    imprima("\n\n  === 3. AVALIACAO DE CONVIVENCIA (acompanhamento) ===\n")

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
        imprima("\n  {r['citizen']:<20} -> {r['overall'].upper()}")
        imprima("  {r['meaning']}")
        se r["needs_accompaniment"] entao:
            imprima("  [!] ACOMPANHAMENTO: {r['action'][:70]}...")
        senao:
            imprima("  {r['action']}")

    // === 4. INTERVENCAO ===
    imprima("\n\n  === 4. INTERVENCAO (nao punir -- ENSINAR) ===\n")
    intervention = engine.intervention_report(
        "C-003", "Discriminou colega por cor de pele + recusou trabalhar")
    imprima("  Cidadao: {intervention['citizen']}")
    imprima("  Problema: {intervention['issue']}")
    imprima("  Plano: {intervention['plan'][:80]}...")
    imprima("  Sistemas: {', '.join(intervention['systems'][:3])}")
    imprima("  {intervention['message'][:80]}...")

    // === 5. STATS ===
    imprima("\n\n  === 5. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DA EDUCACAO CIVICA")
    imprima("{'='*80}")
    imprima("""
  "TRATAR O OUTRO COM DIGNIDADE nao e CORTESIA.
   e DEVER CIVILIZATORIO."

  A frase melhorada:
    Nao: "tratar o outro bem nao e opcional"
    Sim: "Tratar o outro com dignidade e DEVER CIVILIZATORIO.
         Nao e cortesia. Nao e favor. Nao e 'se voce quiser'.
         e a BASE da Republica. Quem nao consegue, APRENDE.
         Quem se recusa, TEM ACOMPANHAMENTO."

  DIREITOS e DEVERES (duas faces):
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
    3. Nao iniciar violencia (defesa e direito, agressao e crime)
    4. Solidariedade (ajudar quem cai, nao virar rosto)
    5. Contribuir (trabalho base 1.0 -- nao sustenta ocioso que recusa)
    6. Respeitar autonomia (corpo do outro e DELA -- P2)
    7. Proteger criancas (responsabilidade de TODOS)
    8. Proteger ambiente (planeta e de quem nao nasceu)
    9. Honestidade (nao mentir, nao enganar, nao desinformar)
    10. Participar (votar, propor, debater -- P4)
    11. Auto-educar (ignorancia voluntaria e irresponsabilidade)
    12. Respeitar bem comum (tudo e CC0, nao apropriar)

  COMO A REPUBLICA LIDA COM QUEM nao CUMPRE:
    1. PRECISA_MELHORAR: reforgo civico (OpenTerminal)
    2. INTERVENCAO: mentor designado + OpenPsychology (sem rotular)
    3. VIOLACAO: OpenPenalRevision (transformacao, nao punicao)

    NUNCA: punir sem tentar ensinar.
    SEMPRE: educar primeiro. Intervir depois. Transformar por ultimo.

  EDUCACAO CONTINUA:
    Crianca (6-11): aprender respeito na pratica
    Adolescente (12-17): participacao + defesa + consentimento
    Adulto (18+): votar + contribuir + proteger
    Imigrante: bem-vindo, mesmos direitos e deveres
    Reciclagem: todo ciclo, auto-avaliacao civica

  PRINCIPIOS:
    P1: Todos tem os mesmos deveres. Sem excecao para rico/pobre/fundador.
    P2: Autonomia corporal protegida. Mas convivencia tem regras.
    P3: Contribuir e dever. Ocioso que recusa tem acompanhamento.
    P4: Participar e dever. Democracia precisa de TODO mundo.
// )
    imprima("{'='*80}")
    imprima("  OpenCivicEducation: {s['total_deveres']} deveres, "
          "{s['total_licoes']} licoes, "
          "{s['precisam_acompanhamento']} precisam de acompanhamento.")
    imprima("  Tratar o outro bem e DEVER. Nao cortesia.")
    imprima("{'='*80}")

```
