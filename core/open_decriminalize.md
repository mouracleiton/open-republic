# OpenDescriminalize -- Descriminalizacao Popular via Assembleia

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_decriminalize.py`

**Descricao:** ================================================================
"A Republica NAO prende por saude.
 A Republica NAO prende por escolha corporal.
 Maconha? Descriminalizada. Usuario e PACIENTE, nao criminoso.
 Crack? Doenca. Tratamento, nao prisao.
 A assembleia DECIDE. O povo VOTA. A Republica OBEDECE."
O QUE ISTO FAZ:
  1. CONVOCA assembleia constituinte para votar descriminalizacao
  2. Define CADA substancia com politica propria (nao tudo igual)
  3. Separa USUARIO (saude) de TRAFICANTE (crime real)
  4. Tratamento OBRIGATORIO disponivel, prisao ABOLIDA para usuario
  5. Integracao com OpenHealth, OpenPsychology, OpenPenalRevision
PRINCIPIO FUNDAMENTAL (P2):
  O corpo e SOBERANO. O que a pessoa poe no proprio corpo
  e escolha DELA. A Republica EDUCA. TRATA. AMA.
  NAO PUNE. Nunca mais.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenDescriminalize -- Descriminalizacao Popular via Assembleia
================================================================

"A Republica nao prende por saude.
 A Republica nao prende por escolha corporal.
 Maconha? Descriminalizada. Usuario e PACIENTE, nao criminoso.
 Crack? Doenca. Tratamento, nao prisao.
 A assembleia DECIDE. O povo VOTA. A Republica OBEDECE."

O QUE ISTO FAZ:
  1. CONVOCA assembleia constituinte para votar descriminalizacao
  2. Define CADA substancia com politica propria (nao tudo igual)
  3. Separa USUARIO (saude) de TRAFICANTE (crime real)
  4. Tratamento OBRIGATORIO disponivel, prisao ABOLIDA para usuario
  5. Integracao com OpenHealth, OpenPsychology, OpenPenalRevision

PRINCIPIO FUNDAMENTAL (P2):
  O corpo e SOBERANO. O que a pessoa poe no proprio corpo
  e escolha DELA. A Republica EDUCA. TRATA. AMA.
  nao PUNE. Nunca mais.

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
// 1. CLASSIFICACAO DE SUBSTANCIAS
// ============================================================================

classe SubstanceCategory herda de Enum:
    NATURAL_MILD = "natural_leve"  // maconha, cafe, cha
    NATURAL_PSYCHEDELIC = "natural_psicodelico"  // psilocibina, ayahuasca, peyote
    SYNTHETIC_MILD = "sintetico_leve"  // MDMA (pesquisa)
    SYNTHETIC_HARD = "sintetico_pesado"  // crack, metaanfetamina
    PHARMACEUTICAL = "farmaceutico"  // calmantes, opioides (lucro farmaceutica)
    ALCOHOL = "alcool"
    TOBACCO = "tabaco"


classe DecriminalizationStatus herda de Enum:
    LEGAL_REGULATED = "legal_regulado"  // livre para adultos + regulado
    DECRIMINALIZED = "descriminalizado"  // sem prisao, tratamento
    MEDICAL_ONLY = "medicinal_apenas"  // so com receita
    TREATMENT_REQUIRED = "tratamento_obrigatorio"  // uso = tratamento (nao prisao)
    RESTRICTED = "restrito"  // pesquisa controlada
    PROHIBITED_TRAFFICKING = "trafico_proibido"  // trafico = crime, uso = saude


classe PolicyApproach herda de Enum:
    // Como a Republica trata cada substancia.
    EDUCATE = "educar"  // informar, deixar escolher
    TREAT = "tratar"  // tratamento disponivel, nao obrigatorio
    REGULATE = "regular"  // regular producao/distribuicao
    BAN_TRAFFIC = "banir_trafico"  // traficante = crime, usuario = saude
    RESEARCH = "pesquisar"  // estudo cientifico aberto


// ============================================================================
// 2. SUBSTANCIA
// ============================================================================

// decorador: @dataclass
classe Substance:
    // Uma substancia e sua politica na Republica.
    substance_id: texto
    name: texto
    category: SubstanceCategory
    seja description: texto = ""

    // Politica
    seja status: DecriminalizationStatus = DecriminalizationStatus.DECRIMINALIZED
    seja approach: [PolicyApproach] = field(default_factory=list)

    // Danos (0-10, base cientifica)
    seja physical_harm: inteiro = 0
    seja addiction_potential: inteiro = 0
    seja social_harm: inteiro = 0
    seja therapeutic_potential: inteiro = 0 // potencial medicinal

    // Regras
    seja min_age: inteiro = 18
    seja public_use: logico = falso // pode usar em publico?
    seja driving_after: logico = falso // pode dirigir apos uso?
    seja production_allowed: logico = falso // pode cultivar/produzir?
    seja commerce_allowed: logico = falso // pode vender?

    // Razao da politica
    seja rationale: texto = ""


seja SUBSTANCES: [Substance] = [

    // === MACONHA ===
    Substance(
        "SUB-CAN", "Maconha (Cannabis)",
        SubstanceCategory.NATURAL_MILD,
        description = (
            "Planta natural usada ha milhares de anos. "
            "Medicinal (dor, nauseia, epilepsia, ansiedade). "
            "Recreativa (relaxamento). "
            "Criminalizada por POLITICA (guerra as drogas), nao ciencia."
        ),
        status = DecriminalizationStatus.LEGAL_REGULATED,
        approach = [PolicyApproach.EDUCATE, PolicyApproach.REGULATE,
                  PolicyApproach.TREAT, PolicyApproach.BAN_TRAFFIC],
        physical_harm = 2,
        addiction_potential = 3,
        social_harm = 2,
        therapeutic_potential = 8,
        min_age = 18,
        public_use = falso,
        driving_after = falso,
        production_allowed = verdadeiro, // pode cultivar para uso proprio
        commerce_allowed = verdadeiro, // comercio regulado (cooperativas)
        rationale = (
            "Maconha e MENOS danosa que alcool e tabaco (estudo Lancet 2010). "
            "Criminalizacao LOTOU prisoes (OpenPenalRevision: 30% presos por drogas). "
            "Descriminalizacao (Portugal 2001): uso caiu, morte caiu, crime caiu. "
            "Usuario é PACIENTE ou CIDADANO. Nao criminoso. "
            "Traficante CONTINUA sendo crime (vitimiza outros). "
            "P2: corpo e soberano. O que poe no corpo e escolha."
        ),
    ),

    // === ALCOHOL ===
    Substance(
        "SUB-ALC", "Alcool",
        SubstanceCategory.ALCOHOL,
        description = (
            "Droga legal mais danosa do mundo. Causa violencia, "
            "doenca, morte. Mas e ACEITO socialmente. "
            "Hipocrisia criminalizar maconha e liberar alcool."
        ),
        status = DecriminalizationStatus.LEGAL_REGULATED,
        approach = [PolicyApproach.EDUCATE, PolicyApproach.REGULATE,
                  PolicyApproach.TREAT],
        physical_harm = 6,
        addiction_potential = 7,
        social_harm = 8,
        therapeutic_potential = 1,
        min_age = 18,
        public_use = verdadeiro, // ja e aceito em festas/restaurantes
        driving_after = falso,
        production_allowed = verdadeiro,
        commerce_allowed = verdadeiro,
        rationale = (
            "Alcool causa MAIS dano que maconha em TUDO (Lancet 2010). "
            "Mas e legal. A Republica mantem legal (nao proibe) mas EDUCA. "
            "OpenNightLife: festas sem obrigacao de beber. "
            "Tratamento para alcoolismo (OpenHealth). "
            "NAO proibe: P2 autonomia. MAS educa e trata."
        ),
    ),

    // === TABACO ===
    Substance(
        "SUB-TOB", "Tabaco",
        SubstanceCategory.TOBACCO,
        "Mata 8 milhoes/ano no mundo. Mais que todas drogas ilicitas juntas.",
        status = DecriminalizationStatus.LEGAL_REGULATED,
        approach = [PolicyApproach.EDUCATE, PolicyApproach.TREAT],
        physical_harm = 8,
        addiction_potential = 8,
        social_harm = 3,
        therapeutic_potential = 0,
        min_age = 18,
        public_use = falso, // nao em locais fechados
        driving_after = verdadeiro,
        production_allowed = verdadeiro,
        commerce_allowed = verdadeiro,
        rationale = (
            "Tabaco mata mais que TODAS as outras drogas COMBINADAS. "
            "A Republica NAO proibe (P2 corpo soberano). "
            "MAS educa FORTE. Tratamento gratuito (OpenHealth). "
            "OpenBeauty: regeneracao pulmonar (stem cells em pesquisa)."
        ),
    ),

    // === PSILOCIBINA (magic mushrooms) ===
    Substance(
        "SUB-PSI", "Psilocibina (cogumelos)",
        SubstanceCategory.NATURAL_PSYCHEDELIC,
        description = (
            "Psicodelico natural. Estudos (Johns Hopkins, Imperial College) "
            "mostram: trata depressao RESISTENTE, ansiedade terminal, "
            "TOC, adicao. 80% efficacia em depressao terminal. "
            "Nao causa adicao fisica. Nao causa danos cerebrais."
        ),
        status = DecriminalizationStatus.MEDICAL_ONLY,
        approach = [PolicyApproach.RESEARCH, PolicyApproach.TREAT,
                  PolicyApproach.EDUCATE],
        physical_harm = 1,
        addiction_potential = 1,
        social_harm = 1,
        therapeutic_potential = 9,
        min_age = 21,
        public_use = falso,
        driving_after = falso,
        production_allowed = falso, // so para pesquisa/tratamento
        commerce_allowed = falso,
        rationale = (
            "Psilocibina e PROMISSORA para saude mental (OpenPsychology). "
            "Estudos rigorosos (Nature, Lancet) comprovam eficacia. "
            "A Republica INVESTE em pesquisa. Tratamento supervisionado. "
            "NAO livre (potencial de uso irresponsavel). MAS medicinal."
        ),
    ),

    // === AYAHUASCA ===
    Substance(
        "SUB-AYA", "Ayahuasca",
        SubstanceCategory.NATURAL_PSYCHEDELIC,
        "Cha sagrado amazonico. Tradicao milenar (OpenTradition). Uso ritual.",
        status = DecriminalizationStatus.LEGAL_REGULATED,
        approach = [PolicyApproach.REGULATE, PolicyApproach.RESEARCH],
        physical_harm = 2,
        addiction_potential = 1,
        social_harm = 1,
        therapeutic_potential = 7,
        min_age = 18,
        public_use = falso,
        driving_after = falso,
        production_allowed = verdadeiro, // tradicao cultural
        commerce_allowed = falso, // so uso ritual/comunitario
        rationale = (
            "Ayahuasca e TRADICAO CULTURAL (OpenTradition). "
            "Uso milenar por povos amazonicos. "
            "Estudos mostram beneficio para depressao e adicao. "
            "Republica protege TRADICAO (P1 respeita cultura). "
            "Uso ritual regulado. Nao comercio."
        ),
    ),

    // === CRACK / COCAINA ===
    Substance(
        "SUB-CRA", "Crack / Cocaina",
        SubstanceCategory.SYNTHETIC_HARD,
        description = (
            "Droga de alta adicao. Destroi vidas. "
            "Usuario NAO e criminoso -- e DOENTE. "
            "Traficante e CRIMINOSO (explora vulneraveis)."
        ),
        status = DecriminalizationStatus.TREATMENT_REQUIRED,
        approach = [PolicyApproach.TREAT, PolicyApproach.BAN_TRAFFIC,
                  PolicyApproach.EDUCATE],
        physical_harm = 8,
        addiction_potential = 10,
        social_harm = 9,
        therapeutic_potential = 1,
        min_age = 0, // ninguem deveria usar
        public_use = falso,
        driving_after = falso,
        production_allowed = falso,
        commerce_allowed = falso,
        rationale = (
            "Crack e DOENCA, nao crime. "
            "Usuario precisa de TRATAMENTO (OpenDignity + OpenHealth). "
            "NAO prisao. Prisao NAO cura adicao. "
            "Traficante e CRIMINOSO que explora vulneraveis (OpenPenalRevision). "
            "Diferenca clara: usuario = paciente. Traficante = crime. "
            "OpenReintegration: tratamento de adicao na colonia de dignidade."
        ),
    ),

    // === MDMA (pesquisa) ===
    Substance(
        "SUB-MDMA", "MDMA (Ecstasy)",
        SubstanceCategory.SYNTHETIC_MILD,
        "Pesquisas (MAPS) mostram: trata TEPT (trauma). 67% efficacia.",
        status = DecriminalizationStatus.RESTRICTED,
        approach = [PolicyApproach.RESEARCH],
        physical_harm = 3,
        addiction_potential = 3,
        social_harm = 2,
        therapeutic_potential = 8,
        min_age = 21,
        production_allowed = falso,
        commerce_allowed = falso,
        rationale = (
            "MDMA em pesquisa para TEPT (OpenPsychology). "
            "Resultados promissores (MAPS Phase 3). "
            "Republica investe em pesquisa cientifica. "
            "Nao recreativo ainda. Medicinal em estudo."
        ),
    ),

    // === OPIOIDES FARMACEUTICOS ===
    Substance(
        "SUB-OPIO", "Opioides Farmaceuticos",
        SubstanceCategory.PHARMACEUTICAL,
        "Dolores. Fabricados por industria. Causam epidemia de adicao.",
        status = DecriminalizationStatus.MEDICAL_ONLY,
        approach = [PolicyApproach.REGULATE, PolicyApproach.TREAT],
        physical_harm = 7,
        addiction_potential = 9,
        social_harm = 7,
        therapeutic_potential = 5,
        min_age = 0,
        production_allowed = verdadeiro, // so farmaceutico
        commerce_allowed = falso, // so com receita
        rationale = (
            "Opioides sao ARMAS da industria farmaceutica. "
            "Epidemia nos EUA: 500mil mortos. "
            "Republica: receita ESTREITA. Monitoramento (OpenHealth). "
            "OpenPsychologyReparation: repara dependentes. "
            "OpenMentalHygiene: bloqueia lobby farmaceutico."
        ),
    ),
]


// ============================================================================
// 3. VOTACAO DA ASSEMBLEIA
// ============================================================================

funcao run_decrim_assembly(n_voters: inteiro = 10000) -> {texto: qualquer}:
    // Convoca assembleia para votar descriminalizacao.

    PERGUNTA: "Usuario de drogas deve ser tratado como paciente (saude)
               ou criminoso (prisao)?"

    + pergunta especifica para cada substancia.
    // 

    // Votacao geral: paciente vs criminoso
    votes_patient = 0 // tratamento, nao prisao
    votes_criminal = 0 // manter criminalizacao
    votes_regulate = 0 // regular + taxar

    para cada _ em intervalo(n_voters):
        r = random.random()
        se r < 0.72 entao:
            votes_patient = votes_patient + 1 // 72% -- tratamento
        senao se r < 0.90 entao:
            votes_regulate = votes_regulate + 1 // 18% -- regular
        senao:
            votes_criminal = votes_criminal + 1 // 10% -- manter crime

    // Votacao por substancia
    substance_votes = {}
    para cada sub em SUBSTANCES:
        // Simular votacao especifica
        se sub.category == SubstanceCategory.NATURAL_MILD entao:
            yes = random.randint(6500, 8500) // maconha: maioria a favor
        senao se sub.category == SubstanceCategory.NATURAL_PSYCHEDELIC entao:
            yes = random.randint(5000, 7000) // psicodelicos: moderado
        senao se sub.category == SubstanceCategory.SYNTHETIC_HARD entao:
            yes = random.randint(7000, 9000) // crack: tratamento (nao legalizar)
        senao se sub.category == SubstanceCategory.ALCOHOL entao:
            yes = random.randint(8000, 9500) // alcool: manter legal
        senao se sub.category == SubstanceCategory.TOBACCO entao:
            yes = random.randint(7500, 9000) // tabaco: manter legal
        senao:
            yes = random.randint(4000, 6000)

        no = n_voters - yes
        substance_votes[sub.substance_id] = {
            "name": sub.name,
            "yes": yes,
            "no": no,
            "approved": yes > no,
            "pct": "{yes/n_voters*100:.0f}%",
            "status": sub.status.value,
        }

    retorne {
        "question": (
            "Usuario de drogas deve ser tratado como PACIENTE (saude) "
            "ou CRIMINOSO (prisao)?"
        ),
        "votes_patient": votes_patient,
        "votes_regulate": votes_regulate,
        "votes_criminal": votes_criminal,
        "total": n_voters,
        "winner": "PACIENTE (TRATAMENTO)" if votes_patient > votes_criminal
                  else "CRIMINOSO (PRISAO)",
        "pct_patient": "{votes_patient/n_voters*100:.0f}%",
        "substance_votes": substance_votes,
        "decision": {
            "usuario_e_paciente": verdadeiro,         // APROVADO (72%)
            "usuario_e_criminoso": falso,        // REJEITADO
            "traficante_e_criminoso": verdadeiro,      // MANTIDO
            "tratamento_obrigatorio_disponivel": verdadeiro,
            "prisao_para_usuario": falso,        // ABOLIDA
            "maconha_legal_regulada": verdadeiro,      // APROVADO
            "psicodelicos_medicinais": verdadeiro,     // APROVADO (pesquisa)
            "crack_tratamento_nao_prisao": verdadeiro,   // APROVADO
            "producao_pessoal_maconha": verdadeiro,    // pode cultivar
            "open_dignity_para_dependentes": verdadeiro,   // colonia de tratamento
        },
    }


// ============================================================================
// 4. MOTOR DE DESCRIMINALIZACAO
// ============================================================================

classe DecrimEngine:
    // Motor que executa a descriminalizacao aprovada pela assembleia.

    O QUE MUDA IMEDIATAMENTE:
    1. Usuario preso por drogas -> LIBERADO (OpenPenalRevision revisa)
    2. Usuario nao preso mais -> encaminhado a OpenHealth (se quiser)
    3. Traficante CONTINUA preso (crime real)
    4. Maconha: legal regulado (producao propria + cooperativas)
    5. Psicodelicos: pesquisa medicinal aberta
    6. Crack: tratamento compulsorio em OpenDignity (nao prisao)

    O QUE nao MUDA:
    - Dirigir alcoolado continua proibido (P2 protege OUTROS)
    - Usar em publico continua restrito (respeitar espaco alheio)
    - Trafico continua crime (vitimiza outros)
    - Venda para menores continua crime (protege criancas)
    // 

    funcao __init__(self):
        self.substances: {texto: Substance} = {s.substance_id: s para s em SUBSTANCES}
        self.reviews: [Dict] = []
        self.liberated_prisoners: inteiro = 0
        self.treated_users: inteiro = 0

    funcao check_arrest_type(self, arrest_reason: texto,
                          seja quantity_grams: flutuante = 0,
                          seja is_trafficking: logico = falso) -> {texto: qualquer}:
        // Verifica se prisao e valida ou deve ser revertida.

        CRITERIO USER vs TRAFFICKER (Brasil atual):
        - < quantidade para uso pessoal: usuario (nao crime)
        - > quantidade ou com provas de venda: traficante (crime)

        Na Republica:
        - Usuario: nao PRENDE. Tratamento se quiser.
        - Traficante: PRENDE (vitimiza outros). OpenPenalRevision transforma.
        // 
        se is_trafficking entao:
            retorne {
                "type": "TRAFICANTE",
                "action": "MANTER PRISAO (vitimiza outros)",
                "process": "OpenPenalRevision: transformar em forca produtiva",
                "note": "Traficante e crime REAL. Explota vulneraveis.",
            }

        // Usuario -- LIBERAR
        self.liberated_prisoners += 1
        retorne {
            "type": "USUARIO",
            "action": "LIBERAR IMEDIATAMENTE",
            "reason": (
                "Usuario de drogas e PACIENTE, nao criminoso. "
                "Assembleia aprovou: tratamento, nao prisao. "
                "Prisao nao cura adicao. Tratamento cura."
            ),
            "referral": "OpenHealth (tratamento VOLUNTARIO)",
            "referral_optional": (
                "Se NAO quiser tratamento, e DIREITO (P2 autonomia corporal). "
                "A Republica so OFERECE. Nao obriga."
            ),
            "record": "PRONTUARIO LIMPO (sem marcador de drogas)",
            "message": (
                "Usuario preso por '{arrest_reason}' LIBERADO. "
                "Prisao por uso e INCONSTITUCIONAL na Republica. "
                "Tratamento disponivel. Nao obrigatorio. P2."
            ),
        }

    funcao offer_treatment(self, person: texto,
                        substance_id: texto) -> {texto: qualquer}:
        // Oferece tratamento (VOLUNTARIO).
        sub = self.substances.get(substance_id)
        se nao sub entao:
            retorne {"error": "Substancia nao encontrada"}

        self.treated_users += 1
        retorne {
            "person": person,
            "substance": sub.name,
            "treatment_type": (
                "OpenDignity (colonia de tratamento)" if sub.addiction_potential >= 8
                else "OpenHealth (ambulatorial)" if sub.addiction_potential >= 4
                else "OpenPsychology (terapia)" if sub.addiction_potential >= 2
                else "OpenEducation (informacao)"
            ),
            "voluntary": verdadeiro,
            "can_refuse": verdadeiro,
            "p2": "Corpo e soberano. Tratamento e oferta, nao obrigacao.",
            "message": (
                "{person}: tratamento para {sub.name} disponivel. "
                "Custo: ZERO. Nivel: Sirio-Libanes. "
                "VOLUNTARIO. Pode recusar (P2)."
            ),
        }

    funcao prison_impact_report(self) -> {texto: qualquer}:
        // Impacto da descriminalizacao no sistema prisional.
        retorne {
            "brasil_atual": {
                "total_presos": 800000,
                "presos_por_drogas": 240000,   // 30%
                "presos_por_USO": 70000,       // 9% so por uso
                "presos_por_TRAFICO": 170000,   // 21% trafico
                "custo_anual": "R$ 42 bi",
            },
            "republica": {
                "presos_por_USO": 0,            // ZERO -- abolido
                "presos_por_TRAFICO": 170000,   // mantido (crime real)
                "liberados": 70000,             // usuarios liberados
                "economizada": "R$ 3.7 bi/ano",
                "tratamento_oferecido": "OpenDignity + OpenHealth",
                "message": (
                    "70.000 pessoas presas SO por uso -> LIBERADAS. "
                    "Traficantes MANTIDOS (crime real). "
                    "Economia: R$ 3.7 bi/ano redirecionada para tratamento."
                ),
            },
        }

    funcao substance_policy(self, substance_id: texto) -> {texto: qualquer}:
        // Politica completa de uma substancia.
        sub = self.substances.get(substance_id)
        se nao sub entao:
            retorne {"error": "nao encontrada"}

        retorne {
            "substance": sub.name,
            "category": sub.category.value,
            "status": sub.status.value,
            "approach": [a.value para a em sub.approach],
            "harms": {
                "physical": "{sub.physical_harm}/10",
                "addiction": "{sub.addiction_potential}/10",
                "social": "{sub.social_harm}/10",
                "therapeutic": "{sub.therapeutic_potential}/10",
            },
            "rules": {
                "min_age": sub.min_age,
                sub.public_use ? "public_use": "permitido" : "proibido",
                sub.driving_after ? "driving": "permitido" : "proibido",
                sub.production_allowed ? "production": "permitido" : "proibido",
                sub.commerce_allowed ? "commerce": "permitido" : "proibido",
            },
            "rationale": sub.rationale,
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_substancias": tamanho(self.substances),
            "legal_regulado": soma(1 para s em self.substances.values()
                                  if s.status == DecriminalizationStatus.LEGAL_REGULATED),
            "medicinal": soma(1 para s em self.substances.values()
                             if s.status == DecriminalizationStatus.MEDICAL_ONLY),
            "tratamento_obrigatorio": soma(1 para s em self.substances.values()
                                          if s.status == DecriminalizationStatus.TREATMENT_REQUIRED),
            "presos_liberados": self.liberated_prisoners,
            "usuarios_tratados": self.treated_users,
        }


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = DecrimEngine()

    imprima("=" * 80)
    imprima("  OPENDESCRIMINALIZE -- ASSEMBLEIA CONSTITUINTE")
    imprima("  'Usuario e PACIENTE. Nao criminoso. Nunca mais.'")
    imprima("=" * 80)

    // === 1. PERGUNTA A ASSEMBLEIA ===
    imprima("\n\n  === 1. PERGUNTA A ASSEMBLEIA ===\n")
    result = run_decrim_assembly(10000)
    imprima("  {result['question']}")
    imprima("\n  PACIENTE (tratamento):    {result['votes_patient']:>6} "
          "({result['pct_patient']})")
    imprima("  REGULAR (taxar):          {result['votes_regulate']:>6} "
          "({result['votes_regulate']/100:.0f}%)")
    imprima("  CRIMINOSO (prisao):       {result['votes_criminal']:>6} "
          "({result['votes_criminal']/100:.0f}%)")
    imprima("\n  RESULTADO: {result['winner']}")

    // === 2. VOTACAO POR SUBSTANCIA ===
    imprima("\n\n  === 2. VOTACAO POR SUBSTANCIA ===\n")
    para cada (sid, vote) em result["substance_votes"].items():
        icon = vote["approved"] ? "APR" : "REJ"
        imprima("  [{icon}] {vote['name']:<25} {vote['yes']:>5} sim / "
              "{vote['no']:>5} nao ({vote['pct']})")
        imprima("       Status: {vote['status']}")

    // === 3. DECISAO DA ASSEMBLEIA ===
    imprima("\n\n  === 3. DECISAO DA ASSEMBLEIA ===\n")
    para cada (key, val) em result["decision"].items():
        status = val ? "SIM" : "NAO"
        imprima("  {key:<40} {status}")

    // === 4. POLITICA POR SUBSTANCIA ===
    imprima("\n\n  === 4. POLITICA DETALHADA POR SUBSTANCIA ===\n")
    para cada sid em engine.substances:
        policy = engine.substance_policy(sid)
        imprima("\n  {policy['substance'].upper()} ({policy['category']})")
        imprima("  Status: {policy['status']}")
        imprima("  Danos: fisico {policy['harms']['physical']}, "
              "adicao {policy['harms']['addiction']}, "
              "social {policy['harms']['social']}, "
              "terapeutico {policy['harms']['therapeutic']}")
        imprima("  Regras: idade {policy['rules']['min_age']}, "
              "publico: {policy['rules']['public_use']}, "
              "producao: {policy['rules']['production']}")
        imprima("  Razao: {policy['rationale'][:100]}...")

    // === 5. REVISAO DE PRISOES ===
    imprima("\n\n  === 5. REVISAO DE PRISOES (usuario vs traficante) ===\n")
    cases = [
        ("porte de maconha 5g (uso pessoal)", 5.0, falso),
        ("porte de crack 0.5g (uso)", 0.5, falso),
        ("trafico de maconha 5kg (venda)", 5000.0, verdadeiro),
        ("porte de cocaina 2g (uso)", 2.0, falso),
        ("trafico de crack (vendendo em esquina)", 50.0, verdadeiro),
        ("cultivo de 3 pes de maconha (uso proprio)", 300.0, falso),
    ]
    para reason, qty, trafficking in cases:
        check = engine.check_arrest_type(reason, qty, trafficking)
        action = check["action"]
        imprima("  [{check['type']:<11}] {reason:<45} -> {action}")

    // === 6. OFERECER TRATAMENTO ===
    imprima("\n\n  === 6. TRATAMENTO OFERECIDO (VOLUNTARIO) ===\n")
    treatments = [
        ("Carlos", "SUB-CRA"),    // crack
        ("Ana", "SUB-CAN"),       // maconha (leve -- so terapia)
        ("Pedro", "SUB-OPIO"),    // opioide
    ]
    para cada (person, sub_id) em treatments:
        t = engine.offer_treatment(person, sub_id)
        imprima("  {t['person']:<12} {t['substance']:<20} -> {t['treatment_type']}")
        imprima("    Voluntario: {t['voluntary']}. P2: {t['p2']}")

    // === 7. IMPACTO PRISIONAL ===
    imprima("\n\n  === 7. IMPACTO DA DESCRIMINALIZACAO NO SISTEMA PRISIONAL ===\n")
    impact = engine.prison_impact_report()
    imprima("\n  BRASIL ATUAL:")
    para cada (k, v) em impact["brasil_atual"].items():
        imprima("    {k:<25} {v}")
    imprima("\n  REPUBLICA:")
    para cada (k, v) em impact["republica"].items():
        se k != "message" entao:
            imprima("    {k:<25} {v}")
    imprima("\n  {impact['republica']['message']}")

    // === 8. STATS ===
    imprima("\n\n  === 8. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DO OPENDESCRIMINALIZE")
    imprima("{'='*80}")
    imprima("""
  USUARIO e PACIENTE. nao CRIMINOSO.
    A assembleia votou: 72% a favor de tratamento, nao prisao.
    Usuario de drogas tem ADICAO. Adicao e DOENCA.
    Prisao nao cura doenca. Tratamento cura.
    Prender usuario e PUNIR DOENTE. A Republica nao faz isso.

  TRAFICANTE e CRIMINOSO. CONTINUA PRESO.
    Quem vende droga EXPLORA vulneraveis.
    Quem financia adicao alheia por lucro COMETE CRIME.
    Traficante vai para OpenPenalRevision (transformacao).
    Diferenca clara: usuario = paciente. Traficante = crime.

  MACONHA: LEGAL REGULADO.
    Menos danosa que alcool e tabaco (Lancet 2010).
    Criminalizacao lotou prisoes (30% presos por drogas).
    Descriminalizacao funciona (Portugal 2001: uso caiu, morte caiu).
    Producao pessoal PERMITIDA (pode cultivar).
    Comercio REGULADO (cooperativas, nao traficante).
    Medicinal GARANTIDO (dor, epilepsia, ansiedade).
    P2: corpo soberano. O que poe no corpo e escolha.

  PSICOdelicos: MEDICINAL (PESQUISA).
    Psilocibina: 80% efficacia em depressao terminal (Johns Hopkins).
    Ayahuasca: tradicao milenar (OpenTradition protege).
    MDMA: trata TEPT (MAPS Phase 3).
    A Republica INVESTE em ciencia. Nao bloqueia por preconceito.

  CRACK: TRATAMENTO, nao PRISAO.
    Crack e adicao SEVERA. Usuario esta DOENTE.
    OpenDignity: colonia de tratamento para dependentes.
    Moradia + comida + tratamento + oficio + comunidade.
    nao prisao. nao abandono. TRATAMENTO.

  OPIoides: ARMAS FARMACEUTICAS.
    Industria fabrica adicao por lucro (500mil mortos EUA).
    Republica: receita ESTREITA. Monitoramento OpenHealth.
    OpenPsychologyReparation: repara dependentes.
    OpenMentalHygiene: bloqueia lobby farmaceutico.

  O QUE MUDA IMEDIATAMENTE:
    1. 70.000 presos SO por uso -> LIBERADOS
    2. Usuario nao e mais preso -> tratamento voluntario
    3. Maconha: cultivar proprio liberado
    4. Prontuario: LIMPO (sem marcador de drogas)
    5. Traficante: CONTINUA preso (crime real)
    6. Economia: R$ 3.7 bi/ano redirecionada para tratamento

  O QUE nao MUDA:
    - Dirigir drogado continua proibido (protege OUTROS)
    - Vender para menor continua crime (protege criancas)
    - Trafico continua crime (vitimiza)
    - Usar em publico continua restrito (respeito ao espaco alheio)

  DADOS CIENTIFICOS:
    - Lancet 2010: alcool mais danoso que heroina (Nutt et al.)
    - Portugal 2001: descriminalizacao -> uso caiu, morte caiu, crime caiu
    - Johns Hopkins: psilocibina 80% efficacia depressao terminal
    - MAPS: MDMA 67% efficacia TEPT
    - OpenHistory: fact-check de todas afirmacoes

  PRINCIPIOS:
    P1: Tratamento para todos. Sem classe. Sem estigma.
    P2: Corpo e SOBERANO. O que poe nele e escolha. Tratamento e oferta.
    seja P3: Tratar adicao = trabalho de alto impacto (medicos, terapeutas).
    P4: Assembleia DECIDE. 72% votou tratamento. Republica obedece.
// )
    imprima("{'='*80}")
    imprima("  OpenDescriminalize: {s['presos_liberados']} presos liberados, "
          "{s['usuarios_tratados']} usuarios em tratamento.")
    imprima("  Usuario e paciente. Nao criminoso. Nunca mais.")
    imprima("{'='*80}")

```
