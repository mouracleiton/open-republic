# OpenChildhood -- Toda Crianca e da Republica

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_childhood.py`

**Descricao:** ===============================================
"Na Republica, nenhum bebe nasce 'privado'.
 Nenhum bebe tem 'pai devedor'.
 Toda crianca e responsabilidade COLETIVA.
 A pensao nao existe porque a dependencia nao existe.
 O individuo amadurece sustentado por TODOS."
O PROBLEMA DA PENSÃO:
  A pensao alimenticia existe porque o sistema capitalista individualiza
  a responsabilidade de criar um ser humano em 2 pessoas (pai + mae).
  Mas criar uma crianca exige:
  - Comida, agua, moradia, saude, educacao (direitos garantidos pela Republica)
  - Tempo, afeto, presenca, estimulo (isso SIM e dos pais/comunidade)
  - Protecao, orientacao, mentoria (comunidade + OpenFamily)
  Na Republica:
  - Comida, moradia, saude sao DIREITOS. Ninguem precisa "pagar pensao"
    para que filho tenha o que ja e direito universal.
  - O trabalho de CUIDAR (tempo, afeto) e CONTRIBUTIÇÃO reconhecida.
  - Quem cuida de crianca recebe credito de impacto (multiplicador geracional).
  RESULTADO:
  - Zero pensao (nao ha dinheiro)
  - Zero abandono (comunidade garante cuidado)
  - Zero "mae solo" (nao ha "solo" -- comunidade cria junto)
  - Zero "pai ausente" (ausencia financeira nao existe; ausencia afetiva
    e tratada por OpenFamily + OpenPsychology)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenChildhood -- Toda Crianca e da Republica
===============================================

"Na Republica, nenhum bebe nasce 'privado'.
 Nenhum bebe tem 'pai devedor'.
 Toda crianca e responsabilidade COLETIVA.
 A pensao nao existe porque a dependencia nao existe.
 O individuo amadurece sustentado por TODOS."

O PROBLEMA DA PENSÃO:
  A pensao alimenticia existe porque o sistema capitalista individualiza
  a responsabilidade de criar um ser humano em 2 pessoas (pai + mae).

  Mas criar uma crianca exige:
  - Comida, agua, moradia, saude, educacao (direitos garantidos pela Republica)
  - Tempo, afeto, presenca, estimulo (isso SIM e dos pais/comunidade)
  - Protecao, orientacao, mentoria (comunidade + OpenFamily)

  Na Republica:
  - Comida, moradia, saude sao DIREITOS. Ninguem precisa "pagar pensao"
    para que filho tenha o que ja e direito universal.
  - O trabalho de CUIDAR (tempo, afeto) e CONTRIBUTIÇÃO reconhecida.
  - Quem cuida de crianca recebe credito de impacto (multiplicador geracional).

  RESULTADO:
  - Zero pensao (nao ha dinheiro)
  - Zero abandono (comunidade garante cuidado)
  - Zero "mae solo" (nao ha "solo" -- comunidade cria junto)
  - Zero "pai ausente" (ausencia financeira nao existe; ausencia afetiva
    e tratada por OpenFamily + OpenPsychology)

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections


// ============================================================================
// Childhood Stages
// ============================================================================

classe DevelopmentStage herda de Enum:
    INFANT = "bebe_0_2"  // 0-2 anos: cuidado 24h
    TODDLER = "primeira_infancia_2_5"  // 2-5: estimulo motor/linguagem
    CHILD = "infancia_5_12"  // 5-12: educacao fundamental
    ADOLESCENT = "adolescente_12_18"  // 12-18: identidade + habilidades
    YOUNG_ADULT = "jovem_adulto_18_25"  // 18-25: transicao para autonomia


classe CareRole herda de Enum:
    // Quem cuida da crianca -- todos com igual valor.
    BIOLOGICAL_PARENT = "pai_biologico"
    CHOSEN_PARENT = "pai_escolhido"
    COMMUNITY_PARENT = "parente_comunitario"
    ELDER_MENTOR = "mentor_idoso"
    EDUCATOR = "educador"
    HEALTH_PROVIDER = "profissional_saude"
    PEER_MENTOR = "mentor_mais_velho"
    REPUBLIC = "propria_republica"


classe SupportType herda de Enum:
    // O que a Republica garante para toda crianca.
    // Materiais (DIREITO -- zero credito, zero pensao)
    FOOD = "alimentacao"
    HOUSING = "moradia"
    HEALTHCARE = "saude"
    EDUCATION = "educacao"
    CLOTHING = "vestuario"
    SAFETY = "seguranca"
    // Emocionais (COMUNIDADE + familia)
    LOVE = "amor_presenca"
    STIMULATION = "estimulo_cognitivo"
    SOCIAL = "convivio_social"
    PROTECTION = "protecao"


// decorador: @dataclass
classe ChildProfile:
    // Perfil de uma crianca na Republica.
    child_id: texto
    name: texto
    age_years: flutuante
    stage: DevelopmentStage
    // Quem cuida (multiplas pessoas, igual valor)
    seja caregivers: [texto] = field(default_factory=list) // ids
    // O que recebe
    seja material_needs_met: logico = verdadeiro // SEMPRE (direito)
    seja emotional_needs_score: flutuante = 80.0 // 0-100 (monitorado)
    seja social_integration: logico = verdadeiro
    seja education_engaged: logico = verdadeiro
    seja health_status: texto = "saudavel"
    // Desenvolvimento
    seja developmental_milestones: {texto: logico} = field(default_factory=dict)
    // Vulnerabilidades
    seja at_risk: logico = falso
    seja risk_factors: [texto] = field(default_factory=list)
    seja interventions: [texto] = field(default_factory=list)


classe ChildhoodSystem:
    // Sistema que garante maturidade de todo individuo.

    A Republica SE RESPONSABILIZA por:
    1. Toda necessidade MATERIAL (comida, moradia, saude, educacao)
       -> Ninguem precisa "pagar pensao" -- e direito universal
    2. Toda necessidade DESENVOLVIMENTAL (estimulo, educacao)
       -> OpenEducation (Feynman + KISS + fazer)
    3. Toda necessidade EMOCIONAL (amor, presenca, comunidade)
       -> OpenFamily + OpenSocial + comunidade
    4. Toda necessidade de PROTECAO
       -> OpenFamily protection system

    O QUE nao EXISTE MAIS:
    - Pensao alimenticia (nao ha dinheiro)
    - "Mae solo" (nao ha "solo" -- comunidade cria)
    - "Pai ausente" financeiro (ausencia financeira impossivel)
    - Crianca passando fome porque pai "nao paga"
    - Crianca sem escola porque mae "nao tem dinheiro"
    - Divorci brigando por "guarda" (nao ha propriedade de filho)
    - Crianca como "mercadoria" de disputa juridica

    O QUE EXISTE:
    - Crianca com TODAS necessidades materiais garantidas (direito)
    - Crianca com multiplos cuidadores (familia + comunidade)
    - Cuidar de crianca = CONTRIBUICAO de alto impacto
    - Ausencia AFETIVA tratada (nao financeira)
    - Protecao infantil garantida por 3 camadas (OpenFamily)
    // 

    funcao __init__(self):
        self.children: {texto: ChildProfile} = {}
        self.caregiver_impact: {texto: flutuante} = defaultdict(flutuante)
        self._counter = 0

    funcao register_child(self, name: texto, age_years: flutuante) -> ChildProfile:
        self._counter += 1
        cid = "CHILD-{self._counter:05d}"
        stage = self._stage_from_age(age_years)
        child = ChildProfile(
            child_id = cid, name=name, age_years=age_years, stage=stage,
            material_needs_met = verdadeiro) // SEMPRE true na Republica
        self.children[cid] = child
        retorne child

    funcao assign_caregiver(self, child_id: texto, caregiver_id: texto):
        child = self.children.get(child_id)
        se child entao:
            child.caregivers.append(caregiver_id)

    funcao calculate_care_impact(self, caregiver_id: texto,
                              children_count: inteiro,
                              hours_per_day: flutuante) -> {texto: qualquer}:
        // Calcular impacto de cuidar de criancas.

        Cuidar de criancas tem impacto INTERGERACIONAL:
        - Cada crianca cuidada = 1 vida influenciada
        - Ripple factor 10x (crianca ensina outros no futuro)
        - Usar a formula do OpenCredit (impacto = pessoas x ripple)

        Quem cuida de crianca recebe ALTO credito de impacto
        porque a contribuicao afeta gerações futuras.
        // 
        impact = hours_per_day * children_count * 10 // ripple 10x
        self.caregiver_impact[caregiver_id] += impact
        retorne {
            "caregiver": caregiver_id,
            "children": children_count,
            "hours_day": hours_per_day,
            "ripple_factor": 10,
            "impact_score": arredonde(impact, 1),
            "credit_weight": "ALTO (intergeracional)",
            "message": ("Cuidar de {children_count} crianca(s) por {hours_per_day}h/dia "
                       "= impacto {impact:.0f} (ripple 10x intergeracional). "
                       "Maior peso de credito da Republica."),
        }

    funcao assess_child(self, child_id: texto) -> {texto: qualquer}:
        // Avaliar bem-estar de uma crianca.
        child = self.children.get(child_id)
        se nao child entao:
            retorne {"error": "nao encontrada"}

        // Material: SEMPRE garantido na Republica
        material = "GARANTIDO (direito universal)"

        // Emocional: depende de cuidadores + comunidade
        se tamanho(child.caregivers) >= 2 entao:
            emotional = child.emotional_needs_score >= 80 ? "FORTÍSSIMO" : "ADEQUADO"
        senao se tamanho(child.caregivers) >= 1 entao:
            emotional = child.emotional_needs_score >= 60 ? "ADEQUADO" : "ATENCAO"
        senao:
            emotional = "CRÍTICO: sem cuidador identificado"
            child.at_risk = verdadeiro

        // Social
        social = child.social_integration ? "INTEGRADO" : "ISOLADO (risco)"

        // Education
        education = child.education_engaged ? "ENGAJADO" : "DESFASE"

        retorne {
            "child": child.name,
            "age": child.age_years,
            "stage": child.stage.value,
            "caregivers": tamanho(child.caregivers),
            "material_needs": material,
            "emotional_needs": emotional,
            "social": social,
            "education": education,
            "health": child.health_status,
            "at_risk": child.at_risk,
            "verdict": self._verdict(child, emotional, social, education),
        }

    // decorador: @staticmethod
    funcao _stage_from_age(age: flutuante) -> DevelopmentStage:
        se age <= 2 entao:
            retorne DevelopmentStage.INFANT
        se age <= 5 entao:
            retorne DevelopmentStage.TODDLER
        se age <= 12 entao:
            retorne DevelopmentStage.CHILD
        se age <= 18 entao:
            retorne DevelopmentStage.ADOLESCENT
        retorne DevelopmentStage.YOUNG_ADULT

    // decorador: @staticmethod
    funcao _verdict(child: ChildProfile, emotional: texto,
                 social: texto, education: texto) -> texto:
        se child.at_risk  ou  "CRÍTICO" in emotional entao:
            retorne "INTERVENCAO IMEDIATA: OpenFamily + comunidade"
        se "ATENCAO" in emotional  ou  "ISOLADO" in social entao:
            retorne "MONITORAR: oferecer apoio comunitario"
        retorne "DESENVOLVIMENTO SAUDAVEL"


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 80)
    imprima("  OPENCHILDHOOD -- TODA CRIANCA E DA REPUBLICA")
    imprima("  'Nenhum bebe nasce privado. Toda crianca e coletiva.'")
    imprima("=" * 80)

    system = ChildhoodSystem()

    // === 1. Register Children ===
    imprima("\n\n  === CRIANCAS REGISTRADAS ===\n")

    children_data = [
        ("Joaozinho", 8, ["C-001", "C-002", "C-005 (avô comunitário)"]),
        ("Mariazinha", 5, ["C-001", "C-002"]),
        ("Pedrinho", 2, ["C-003", "C-006"]),
        ("Aninha", 14, ["C-004", "C-007 (mentor idoso)"]),
        ("Garoto Sem Cuidador", 10, []),   // caso de risco simulado
    ]

    para name, age, caregivers in children_data:
        child = system.register_child(name, age)
        para cada cg em caregivers:
            // Extract just IDs
            cg_id = cg.split(" ")[0]
            system.assign_caregiver(child.child_id, cg_id)
        imprima("  {child.name} ({child.age_years} anos) - {child.stage.value}")
        imprima("    Cuidadores: {len(child.caregivers)}")
        imprima("    Necessidades materiais: {'GARANTIDAS' if child.material_needs_met else 'FALTANDO'}")

    // === 2. Assess ===
    imprima("\n\n  === AVALIACAO ===\n")
    para cada cid em system.children:
        result = system.assess_child(cid)
        imprima("\n  {result['child']} ({result['age']} anos)")
        imprima("    Material: {result['material_needs']}")
        imprima("    Emocional: {result['emotional_needs']}")
        imprima("    Social: {result['social']}")
        imprima("    Educacao: {result['education']}")
        imprima("    Risco: {'SIM' if result['at_risk'] else 'nao'}")
        imprima("    Veredito: {result['verdict']}")

    // === 3. Care Impact ===
    imprima("\n\n  === IMPACTO DE CUIDAR (credito) ===\n")

    impacts = [
        ("C-001", 2, 4, "Cleiton cuida 2 criancas 4h/dia"),
        ("C-002", 3, 6, "Amina cuida 3 criancas (creche comunitaria) 6h/dia"),
        ("C-005", 5, 8, "Lars (avô comunitario) cuida 5 criancas 8h/dia"),
        ("C-003", 1, 2, "Sven cuida 1 crianca 2h/dia"),
    ]

    para cg_id, n_child, hours, desc in impacts:
        result = system.calculate_care_impact(cg_id, n_child, hours)
        imprima("\n  {desc}")
        imprima("    Impacto: {result['impact_score']} (ripple {result['ripple_factor']}x)")
        imprima("    Peso credito: {result['credit_weight']}")

    // === 4. Why No Pension ===
    imprima("\n\n{'='*80}")
    imprima("  POR QUE A PENSAO NAO EXISTE MAIS")
    pensão_inexistente = "pensão alimentícia"
    imprima("{'='*80}")
    imprima("""
  CAPITALISMO OPENREPUBLIC
  --------------------------------------- ---------------------------------------
  Pensao alimenticia ($/mes) ZERO (nao ha dinheiro)
  Pai "devedor" de pensao                  Pai nao deve dinheiro (nao existe)
  Mae "solo" (sozinha financeiramente)     Nao ha "solo" -- comunidade cria junto
  Crianca passando fome se pai nao paga Comida e DIREITO (sempre garantida)
  Crianca sem escola se mae nao paga Educacao e DIREITO (sempre garantida)
  Divorci brigando por "guarda"            Nao ha "guarda" -- nao ha propriedade de filho
  Filho como mercadoria juridica Filho e PESSOA com direitos
  "Pai ausente" = nao paga                 "Pai ausente" = falta AFETO (tratado)
  Justicia decide quanto filho custa Republica garante quanto filho precisa
  Crianca refem de disputa financeira Crianca LIVRE de disputa

  O QUE A REPUBLICA GARANTE PARA TODA CRIANCA:

    MATERIAL (DIREITO -- sempre, incondicional):
      - Comida: OpenFood
      - Moradia: OpenHome + OpenCivilConstruction
      - Saude: OpenHealth + OpenMedicine
      - Educacao: OpenEducation (Feynman + KISS + fazer)
      - Vestuario: OpenProduction (FabLab)
      - Seguranca: OpenFamily + OpenAutonomousSecurity

    EMOCIONAL (comunidade + familia):
      - Amor e presenca: multiplos cuidadores (OpenFamily)
      - Estimulo cognitivo: OpenEducation desde bebe
      - Convivio social: OpenSocial + comunidade local
      - Protecao: 3 camadas (familia -> comunidade -> sistema)

    DESENVOLVIMENTO (Republica garante maturidade):
      - Bebe (0-2): cuidado 24h (creche comunitaria)
      - Primeira infancia (2-5): estimulo motor + linguagem
      - Infancia (5-12): educacao fundamental (ensinar a FAZER)
      - Adolescente (12-18): identidade + habilidades
      - Jovem adulto (18-25): transicao para autonomia

  CUIDAR DE CRIANCA = ALTO IMPACTO:
    Quem cuida de crianca recebe o MAIOR peso de credito.
    Ripple factor 10x (intergeracional).
    Cada crianca cuidada = vida influenciada para sempre.
    Cuidar de 3 criancas 6h/dia = impacto 180 (maior que cirurgia).

  O QUE ACABA:
    - Pensao alimenticia
    - "Mae solo"
    - "Pai ausente" financeiro
    - Crianca refem de briga de divorcio
    - Crianca passando fome
    - Crianca sem escola
    - Crianca como propriedade

  "Toda crianca e da Republica.
   Nao de um pai. Nao de uma mae.
   De TODOS.
   e TODOS garantem que ela cresca saudavel.
   Comida, moradia, saude, educacao: direitos.
   Amor, presenca, cuidado: comunidade.
   Sem pensao. Sem disputa. Sem dinheiro.
   Apenas cuidado."
// )

```
