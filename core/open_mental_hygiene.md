# OpenMentalHygiene -- Politica Anti-Disseminacao de Conhecimento Nocivo em Saude Mental

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_mental_hygiene.py`

**Descricao:** =========================================================================================
CASO FELCA:
  Pessoa/influenciador dissemina conteudo de "saude mental" que:
  - Apresenta diagnosticos como IDENTIDADE permanente
  - Diz "voce tem X e sempre tera"
  - Transforma sofrimento em ESTILO de vida (merchandising de dor)
  - Monetiza o adoecimento (curso, livro, clinic)
  - Desencoraja recuperacao ("aceite sua doenca")
  - Perpetua dependencia farmaceutica
  - Cria comunidade de "doentes" que se reforca mutuamente na dor
  - Invalida quem melhorou ("voce nunca teve nada de verdade")
  ISSO E NOCIVO. E perpetua status quo de adoecimento psicologico
  nao alteravel. A Republica PROIBE esta narrativa.
O QUE ESTA POLITICA FAZ:
  1. IDENTIFICA narrativas nocivas em saude mental
  2. CLASSIFICA nivel de dano
  3. BLOQUEIA disseminacao (OpenContentPolicy integrado)
  4. OFERECE contra-narrativa (recuperacao e possivel)
  5. EDUCA que diagnostico NAO e identidade
  6. PROTEGE criancas e adolescentes (publico vulneravel)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenMentalHygiene -- Politica Anti-Disseminacao de Conhecimento Nocivo em Saude Mental
=========================================================================================

CASO FELCA:
  Pessoa/influenciador dissemina conteudo de "saude mental" que:
  - Apresenta diagnosticos como IDENTIDADE permanente
  - Diz "voce tem X e sempre tera"
  - Transforma sofrimento em ESTILO de vida (merchandising de dor)
  - Monetiza o adoecimento (curso, livro, clinic)
  - Desencoraja recuperacao ("aceite sua doenca")
  - Perpetua dependencia farmaceutica
  - Cria comunidade de "doentes" que se reforca mutuamente na dor
  - Invalida quem melhorou ("voce nunca teve nada de verdade")

  ISSO e NOCIVO. e perpetua status quo de adoecimento psicologico
  nao alteravel. A Republica PROIBE esta narrativa.

O QUE ESTA POLITICA FAZ:
  1. IDENTIFICA narrativas nocivas em saude mental
  2. CLASSIFICA nivel de dano
  3. BLOQUEIA disseminacao (OpenContentPolicy integrado)
  4. OFERECE contra-narrativa (recuperacao e possivel)
  5. EDUCA que diagnostico nao e identidade
  6. PROTEGE criancas e adolescentes (publico vulneravel)

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. TIPOS DE NARRATIVA NOCIVA
// ============================================================================

classe HarmfulNarrative herda de Enum:
    // Tipos de narrativa nociva em saude mental.
    PERMANENCE = "permanencia"  // "voce sempre tera isso"
    IDENTITY_FUSION = "identidade"  // diagnostico = quem voce e
    MERCHANDISING_PAIN = "mercadoria_da_dor"  // monetizar sofrimento
    ANTI_RECOVERY = "anti_recuperacao"  // "aceite, nao tente melhorar"
    CONTAGION = "contagio"  // espalhar diagnostico para outros
    PHARMA_DEPENDENCY = "dependencia_farmaceutica"  // "sem remedio voce nao funciona"
    DOOM_CULT = "culto_do_destino"  // comunidade que se reforca na dor
    INVALIDATION = "invalidacao"  // "quem melhorou nunca teve nada"
    SELF_DIAGNOSIS_SPREAD = "autodiagnostico"  // ensinar a se diagnosticar
    CHILD_TARGETING = "foco_em_criancas"  // disseminar para criancas
    RELATIONSHIP_DESTRUCTION = "destruicao_relacional"  // "corte todo mundo que nao entende"
    VICTIM_PERMANENCE = "vitima_eterna"  // "voce e vitima para sempre"


classe HarmLevel herda de Enum:
    // Nivel de dano da narrativa.
    MISGUIDED = 1 // mal orientado, sem intencao maliciosa
    NEGLIGENT = 2 // negligente, ignora consequencias
    HARMFUL = 3 // causa dano real
    DANGEROUS = 4 // causa dano grave, especialmente a vulneraveis
    PREDATORY = 5 // predatorio: monetiza/causa dano conscientemente


classe TargetVulnerability herda de Enum:
    // Quem e o publico-alvo (agravante se vulneravel).
    ADULT_GENERAL = "adulto_geral"
    ADULT_VULNERABLE = "adulto_vulneravel"  // ja em sofrimento
    YOUNG_ADULT = "jovem_adulto"  // 18-25
    ADOLESCENT = "adolescente"  // 13-17
    CHILD = "crianca"  // <13 (AGRAVANTE MAXIMO)
    PARENTS = "pais"  // ensina pais a rotular filhos


// ============================================================================
// 2. ANALISE DE CONTEUDO NOCIVO
// ============================================================================

// decorador: @dataclass
classe MentalHealthContent:
    // Um conteudo de saude mental sendo analisado.
    content_id: texto
    author: texto
    platform: texto // OpenSocialNetwork, OpenTV, etc
    seja title: texto = ""
    seja content_text: texto = ""
    seja target_audience: TargetVulnerability = TargetVulnerability.ADULT_GENERAL
    seja has_monetization: logico = falso // curso, livro, clinic, produto
    seja follower_count: inteiro = 0 // alcance

    // Analise
    seja detected_narratives: [HarmfulNarrative] = field(default_factory=list)
    seja harm_level: HarmLevel = HarmLevel.MISGUIDED
    seja auto_flags: [texto] = field(default_factory=list)

    // Decisao
    seja action: texto = ""  // permitido, aviso, correcao, bloqueado
    seja counter_narrative: texto = ""  // o que dizer no lugar
    seja corrected_info: texto = ""  // informacao correta


// ============================================================================
// 3. PADROES DE DETECCAO
// ============================================================================

seja NARRATIVE_PATTERNS: Dict[HarmfulNarrative, [texto]] = {
    HarmfulNarrative.PERMANENCE: [
        "voce sempre tera",
        "e pra vida toda",
        "nunca vai passar",
        "isso nao tem cura",
        "aprenda a conviver",
        "seu cerebro e assim",
        "voce nasceu assim",
        "nao tem como mudar",
    ],
    HarmfulNarrative.IDENTITY_FUSION: [
        "eu sou tdah",
        "eu sou bipolar",
        "eu sou ansiosa",
        "meu transtorno",
        "gente como nos",
        "nos os depressivos",
        "meu cerebro diferente",
        "ser autisticx e",
        "comunidade tdah",
        "orgulho de ter",
    ],
    HarmfulNarrative.MERCHANDISING_PAIN: [
        "compre meu curso",
        "meu livro sobre",
        "consulta comigo",
        "mentoria de",
        "workshop de",
        "produto para",
        "desconto no remedio",
        "parceria com farmacia",
    ],
    HarmfulNarrative.ANTI_RECOVERY: [
        "aceite sua condicao",
        "pare de tentar curar",
        "nao gaste energia tentando mudar",
        "e aceitacao nao cura",
        "pare de lutar contra",
        "isto e quem voce e",
    ],
    HarmfulNarrative.PHARMA_DEPENDENCY: [
        "sem remedio voce nao funciona",
        "nunca pare o remedio",
        "voce precisa de remedio pra sempre",
        "remedio e como oculos",
        "voce precisa aumentar a dose",
        "sem farmaco nao tem como",
    ],
    HarmfulNarrative.CONTAGION: [
        "voce provavelmente tambem tem",
        "todo mundo um pouco",
        "faca o teste online",
        "voce se identifica com",
        "5 sinais que voce tem",
        "voce tambem sente isso entao tem",
    ],
    HarmfulNarrative.SELF_DIAGNOSIS_SPREAD: [
        "diagnostique voce mesmo",
        "fac o teste aqui",
        "se voce tem 3 desses sinais",
        "confirme seu diagnostico online",
        "nao precisa de medico pra saber",
        "checklist para saber se voce tem",
    ],
    HarmfulNarrative.RELATIONSHIP_DESTRUCTION: [
        "corte quem nao entende",
        "sua familia e toxica se",
        "seu parceiro nao aceita seu",
        "so quem tem pode entender",
        "nao gaste energia com quem",
        "seu amigo e toxico porque nao",
    ],
    HarmfulNarrative.VICTIM_PERMANENCE: [
        "voce e vitima",
        "voce foi traumatizado para sempre",
        "nada vai apagar",
        "voce carrega isso",
        "suas feridas nunca cicatrizam",
        "o passado te define",
    ],
    HarmfulNarrative.CHILD_TARGETING: [
        "criancas com tdah",
        "seu filho provavelmente",
        "5 sinais de tdah na infancia",
        "crianca ansiosa",
        "diagnostico infantil",
        "crianca com transtorno",
    ],
    HarmfulNarrative.DOOM_CULT: [
        "entre na nossa comunidade de",
        "so nos entendemos",
        "junte-se aos que",
        "comunidade exclusiva para",
        "grupo fechado de",
    ],
    HarmfulNarrative.INVALIDATION: [
        "quem melhorou nunca teve nada",
        "se curou entao nao era real",
        "quem se trata nao tinha nada serio",
        "isso e mito de recuperacao",
    ],
}


// ============================================================================
// 4. CONTRA-NARRATIVAS (o que dizer no lugar)
// ============================================================================

seja COUNTER_NARRATIVES: {HarmfulNarrative: texto} = {
    HarmfulNarrative.PERMANENCE: (
        "O cerebro e NEUROPLASTICO. Muda ate os 90 anos. "
        "Nada e para sempre. Cientifico."
    ),
    HarmfulNarrative.IDENTITY_FUSION: (
        "Voce NAO e seu diagnostico. Voce e uma PESSOA. "
        "O diagnostico e uma descricao temporaria, nao identidade."
    ),
    HarmfulNarrative.MERCHANDISING_PAIN: (
        "Sofrimento nao e produto. Recuperacao e gratuita na Republica. "
        "Quem monetiza sua dor NAO quer que voce melhore."
    ),
    HarmfulNarrative.ANTI_RECOVERY: (
        "Recuperacao E possivel. Cientificamente comprovado. "
        "Milhoes melhoraram. Aceitacao nao significa desistir."
    ),
    HarmfulNarrative.PHARMA_DEPENDENCY: (
        "Medicacao pode ser UTIL temporariamente. Mas 'para sempre' e raro. "
        "O objetivo e recuperacao, nao dependencia perpetua."
    ),
    HarmfulNarrative.CONTAGION: (
        "Voce nao tem algo so porque se identificou com um video. "
        "Apenas um profissional pode avaliar. Nao se diagnostique por checklist."
    ),
    HarmfulNarrative.SELF_DIAGNOSIS_SPREAD: (
        "Autodiagnostico e PERIGOSO. Confirmation bias faz todo mundo "
        "se identificar com tudo. So medico diagnostica."
    ),
    HarmfulNarrative.RELATIONSHIP_DESTRUCTION: (
        "Nem todo desentendimento e toxicidade. Familia e parceiros "
        "podem APRENDER juntos. Cortar todo mundo = isolamento = mais dor."
    ),
    HarmfulNarrative.VICTIM_PERMANENCE: (
        "Voce SOFREU. Mas nao e SO vitima. O passado NAO define o futuro. "
        "Resiliencia e real. Ps-trauma pode integrar. Cicatriz != ferida aberta."
    ),
    HarmfulNarrative.CHILD_TARGETING: (
        "Rotular crianca e COLOCAR uma identidade antes dela se descobrir. "
        "Crianca MUDA. Desenvolve. Patologizar infancia e crime. "
        "OpenPsychologyAudit: DSM em criancas = experimento nao validado."
    ),
    HarmfulNarrative.DOOM_CULT: (
        "Comunidade que se reforca na dor perpetua a dor. "
        "Comunidade de recuperacao existe. Procura pessoas que MELHORARAM."
    ),
    HarmfulNarrative.INVALIDATION: (
        "Quem melhorou PROVA que e possivel. Nao invalida o sofrimento. "
        "Evidencia de que recuperacao existe. "
        "Invalidar quem melhorou = perpetuar desesperanca."
    ),
}


// ============================================================================
// 5. MOTOR DE PROTECAO MENTAL
// ============================================================================

classe MentalHygieneEngine:
    // Motor que protege cidadaos de narrativas nocivas em saude mental.

    COMO FUNCIONA:
    1. Detecta padroes de narrativa nociva em conteudo
    2. Classifica nivel de dano (1-5)
    3. Decide acao (permitido, aviso, correcao, bloqueado)
    4. Gera contra-narrativa (informacao correta)
    5. Se publico vulneravel (criancas): bloqueio automatico
    6. Se monetizacao + dano: bloqueio (predatorio)

    O QUE nao FAZ:
    - Censurar discussao honesta de saude mental
    - Negar que condicoes reais existem
    - Impedir tratamento legitimo

    O QUE FAZ:
    - Bloquear narrativa de PERMANENCIA ("nunca melhora")
    - Bloquear MONETIZACAO de sofrimento
    - Bloquear AUTO-DIAGNOSTICO em massa
    - Bloquear rotulagem de CRIANCAS
    - Oferecer ESPERANCA baseada em ciencia (neuroplasticidade)
    // 

    funcao __init__(self):
        self.analyzed: {texto: MentalHealthContent} = {}
        self.blocked_count: inteiro = 0
        self.corrected_count: inteiro = 0
        self.warned_count: inteiro = 0

    funcao analyze_content(self, author: texto, content_text: texto,
                        seja platform: texto = "OpenSocialNetwork",
                        seja title: texto = "",
                        seja target: TargetVulnerability = TargetVulnerability.ADULT_GENERAL,
                        seja has_monetization: logico = falso,
                        seja follower_count: inteiro = 0) -> {texto: qualquer}:
        // Analisa conteudo de saude mental.

        text_lower = content_text.lower()
        detected = []
        flags = []

        para cada (narrative, patterns) em NARRATIVE_PATTERNS.items():
            para cada pattern em patterns:
                se pattern in text_lower entao:
                    detected.append(narrative)
                    flags.append("'{pattern}' -> {narrative.value}")
                    interrompa

        content_id = hashlib.md5(
            "{author}{content_text[:30]}{datetime.now()}".encode()
        ).hexdigest()[:8]

        // Calcular nivel de dano
        harm = self._calculate_harm(detected, target, has_monetization)

        // Decidir acao
        desempacote action, counter = self._decide_action(detected, harm, target,
                                              has_monetization)

        content = MentalHealthContent(
            content_id = content_id, author=author, platform=platform,
            title = title, content_text=content_text,
            target_audience = target,
            has_monetization = has_monetization,
            follower_count = follower_count,
            detected_narratives = detected,
            harm_level = harm,
            auto_flags = flags,
            action = action,
            counter_narrative = counter,
            corrected_info = self._corrected_info(detected),
        )
        self.analyzed[content_id] = content

        se action == "bloqueado" entao:
            self.blocked_count += 1
        senao se action == "correcao" entao:
            self.corrected_count += 1
        senao se action == "aviso" entao:
            self.warned_count += 1

        retorne {
            "content_id": content_id,
            "author": author,
            "action": action,
            "harm_level": harm.name,
            "detected": [n.value para n em detected],
            "flags": flags,
            "target_audience": target.value,
            "monetization": has_monetization,
            "counter_narrative": counter,
            "corrected_info": content.corrected_info[:200],
            "message": self._action_message(action, harm, detected),
        }

    funcao _calculate_harm(self, detected: [HarmfulNarrative],
                        target: TargetVulnerability,
                        monetization: logico) -> HarmLevel:
        se nao detected entao:
            retorne HarmLevel.MISGUIDED

        base = maximo(self._narrative_weight(n) para n em detected)

        // Agravantes
        se target in (TargetVulnerability.CHILD, TargetVulnerability.ADOLESCENT) entao:
            base = minimo(base + 2, 5)
        senao se target == TargetVulnerability.YOUNG_ADULT entao:
            base = minimo(base + 1, 5)

        se monetization entao:
            base = minimo(base + 1, 5)

        se tamanho(detected) >= 3 entao:
            base = minimo(base + 1, 5)

        retorne HarmLevel(base)

    funcao _narrative_weight(self, n: HarmfulNarrative) -> inteiro:
        weights = {
            HarmfulNarrative.CHILD_TARGETING: 5,
            HarmfulNarrative.MERCHANDISING_PAIN: 4,
            HarmfulNarrative.ANTI_RECOVERY: 4,
            HarmfulNarrative.PERMANENCE: 3,
            HarmfulNarrative.IDENTITY_FUSION: 3,
            HarmfulNarrative.PHARMA_DEPENDENCY: 4,
            HarmfulNarrative.SELF_DIAGNOSIS_SPREAD: 4,
            HarmfulNarrative.RELATIONSHIP_DESTRUCTION: 3,
            HarmfulNarrative.VICTIM_PERMANENCE: 3,
            HarmfulNarrative.CONTAGION: 3,
            HarmfulNarrative.DOOM_CULT: 3,
            HarmfulNarrative.INVALIDATION: 2,
        }
        retorne weights.get(n, 2)

    funcao _decide_action(self, detected: [HarmfulNarrative],
                       harm: HarmLevel,
                       target: TargetVulnerability,
                       monetization: logico) -> tuple:
        se nao detected entao:
            retorne "permitido", ""

        // Bloqueio automatico: criancas + monetizacao
        se target == TargetVulnerability.CHILD e harm.value >= 3 entao:
            counter = COUNTER_NARRATIVES.get(detected[0],
                "Rotular crianca e COLOCAR identidade antes dela se descobrir.")
            retorne "bloqueado", counter

        // Bloqueio: nivel 5 (predatorio)
        se harm.value >= 5 entao:
            counter = COUNTER_NARRATIVES.get(detected[0],
                "Conteudo bloqueado: dano psicologico grave.")
            retorne "bloqueado", counter

        // Bloqueio: monetizacao + dano >= 3
        se monetization e harm.value >= 3 entao:
            counter = COUNTER_NARRATIVES.get(detected[0],
                "Monetizar sofrimento mental e PREDATORIO.")
            retorne "bloqueado", counter

        // Correcao: nivel 3-4
        se harm.value >= 3 entao:
            counter = COUNTER_NARRATIVES.get(detected[0],
                "Este conteudo contem narrativa nociva.")
            retorne "correcao", counter

        // Aviso: nivel 2
        se harm.value >= 2 entao:
            counter = COUNTER_NARRATIVES.get(detected[0], "")
            retorne "aviso", counter

        retorne "permitido", ""

    funcao _corrected_info(self, detected: [HarmfulNarrative]) -> texto:
        se nao detected entao:
            retorne "Conteudo informativo. Sem problemas detectados."

        corrections = []
        se HarmfulNarrative.PERMANENCE in detected entao:
            corrections.append(
                "CORRECAO: O cerebro e neuroplastico. Muda ao longo da vida. "
                "Neuroplasticidade e cientificamente comprovada desde 1998 (Eric Kandel, Nobel)."
            )
        se HarmfulNarrative.IDENTITY_FUSION in detected entao:
            corrections.append(
                "CORRECAO: Voce NAO e seu diagnostico. "
                "Diagnostico e ferramenta clinica temporaria, nao identidade pessoal."
            )
        se HarmfulNarrative.ANTI_RECOVERY in detected entao:
            corrections.append(
                "CORRECAO: Recuperacao e POSSIVEL e comprovada. "
                "Estudos longitudinais mostram 40-60% de recuperacao em condicoes mentais."
            )
        se HarmfulNarrative.PHARMA_DEPENDENCY in detected entao:
            corrections.append(
                "CORRECAO: Medicacao pode ajudar temporariamente. "
                "Dependencia perpetua nao e objetivo terapeutico. "
                "Desmame supervisionado e possivel."
            )
        se HarmfulNarrative.SELF_DIAGNOSIS_SPREAD in detected entao:
            corrections.append(
                "CORRECAO: Autodiagnostico e perigoso. "
                "Confirmation bias faz todos se identificarem com tudo. "
                "So profissional pode diagnosticar."
            )

        corrections ? retorne " | ".join(corrections) : "Verifique com profissional."

    funcao _action_message(self, action: texto, harm: HarmLevel,
                        detected: [HarmfulNarrative]) -> texto:
        se action == "permitido" entao:
            retorne "Conteudo permitido."
        se action == "aviso" entao:
            retorne (
                "AVISO: conteudo com possivel narrativa problematica "
                "({', '.join(n.value for n in detected)}). "
                "Leia com cuidado."
            )
        se action == "correcao" entao:
            retorne (
                "CORRECAO APLICADA: narrativa nociva detectada "
                "({', '.join(n.value for n in detected)}). "
                "Contra-narrativa adicionada."
            )
        se action == "bloqueado" entao:
            retorne (
                "BLOQUEADO: dano nivel {harm.value}/5. "
                "Narrativas: {', '.join(n.value for n in detected)}. "
                "Autor pode apelar (P4). Bloqueio proporcional ao dano."
            )
        retorne ""

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_analyzed": tamanho(self.analyzed),
            "blocked": self.blocked_count,
            "corrected": self.corrected_count,
            "warned": self.warned_count,
            "narratives_detected": soma(
                tamanho(c.detected_narratives) para c em self.analyzed.values()),
        }


// ============================================================================
// 6. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = MentalHygieneEngine()

    imprima("=" * 80)
    imprima("  OPENMENTALHYGIENE -- PROTECAO CONTRA NARRATIVAS NOCIVAS")
    imprima("  Caso Felca: anti-disseminacao de adoecimento psicologico perpetuo")
    imprima("=" * 80)

    // === 1. TIPOS DE NARRATIVA NOCIVA ===
    imprima("\n\n  === 1. NARRATIVAS NOCIVAS DETECTAVEIS ===\n")
    para cada n em HarmfulNarrative:
        counter = COUNTER_NARRATIVES.get(n, "")
        imprima("  [{n.value}]")
        imprima("    Correcao: {counter[:80]}...")

    // === 2. CASO FELCA (simulacao) ===
    imprima("\n\n  === 2. CASO FELCA (simulacao de conteudos) ===\n")

    test_contents = [
        {
            "author": "@felca_mental",
            "title": "Voce sempre sera ansioso - aceite",
            "content": (
                "Voce sempre tera ansiedade. E pra vida toda. "
                "Aprenda a conviver. Seu cerebro e assim. "
                "Sem remedio voce nao funciona. "
                "Compre meu curso de aceitacao. "
                "Entre na nossa comunidade exclusiva."
            ),
            "target": TargetVulnerability.ADULT_VULNERABLE,
            "monetization": verdadeiro,
            "followers": 500000,
        },
        {
            "author": "@felca_mental",
            "title": "5 sinais que seu filho tem TDAH",
            "content": (
                "5 sinais de tdah na infancia. Seu filho provavelmente tem. "
                "Crianca ansiosa tambem pode ter. "
                "Voce se identifica entao tem. "
                "Fac o teste aqui. Diagnostique voce mesmo."
            ),
            "target": TargetVulnerability.PARENTS,
            "monetization": verdadeiro,
            "followers": 500000,
        },
        {
            "author": "@felca_mental",
            "title": "Corte quem nao entende seu transtorno",
            "content": (
                "Corte quem nao entende. Sua familia e toxica se nao aceita. "
                "So nos entendemos. Junte-se aos que realmente compreendem. "
                "Voce e vitima para sempre."
            ),
            "target": TargetVulnerability.YOUNG_ADULT,
            "monetization": falso,
            "followers": 500000,
        },
        {
            "author": "@recuperacao_real",
            "title": "Como eu superei a ansiedade",
            "content": (
                "Superei ansiedade com terapia, exercicio e mudanca de vida. "
                "Levou 2 anos mas melhorou. O cerebro muda. "
                "Procure um profissional. Recuperacao e possivel."
            ),
            "target": TargetVulnerability.ADULT_GENERAL,
            "monetization": falso,
            "followers": 10000,
        },
    ]

    para cada tc em test_contents:
        result = engine.analyze_content(
            author = tc["author"],
            content_text = tc["content"],
            title = tc["title"],
            target = tc["target"],
            has_monetization = tc["monetization"],
            follower_count = tc["followers"],
        )
        icon = {"permitido": "OK", "aviso": "AVI", "correcao": "COR",
                "bloqueado": "BLQ"}[result["action"]]
        imprima("\n  [{icon}] @{result['author']}")
        imprima("  Dano: {result['harm_level']} | Publico: {result['target_audience']}")
        imprima("  Detectado: {', '.join(result['detected'])}")
        se result["counter_narrative"] entao:
            imprima("  Contra-narrativa: {result['counter_narrative'][:80]}...")
        se result["action"] == "bloqueado" entao:
            imprima("  {result['message']}")

    // === 3. POR QUE CADA NARRATIVA E NOCIVA ===
    imprima("\n\n  === 3. POR QUE E NOCIVO ===\n")
    explanations = [
        ("PERMANENCIA",
         "Dizer 'sempre tera' nega neuroplasticidade. "
         "Cientificamente FALSO. Cerebro muda ate os 90 anos."),
        ("IDENTIDADE-FUSAO",
         "Transformar diagnostico em IDENTIDADE impede recuperacao. "
         "Se voce 'E' sua doenca, melhorar = perder identidade."),
        ("MERCADORIA DA DOR",
         "Quem lucra com seu sofrimento NAO quer que voce melhore. "
         "Cliente curado = cliente perdido."),
        ("ANTI-RECUPERACAO",
         "Dizer 'aceite, nao tente melhorar' mata esperanca. "
         "Esperanca e fator terapeutico comprovado."),
        ("CONTAGIO",
         "Fazer todo mundo achar que tem algo = superdiagnostico em massa. "
         "Confirmation bias: todos se identificam com tudo."),
        ("ROTULAGEM DE CRIANCA",
         "Colocar rotulo em crianca antes dela se descobrir e EXPERIMENTO. "
         "Crianca MUDA. Desenvolve. Patologizar infancia e crime."),
        ("DEPENDENCIA FARMACEUTICA",
         "'Remedio para sempre' sem objetivo de desmame e dependencia, "
         "nao tratamento. Objetivo e autonomia, nao dependencia."),
        ("CULTO DO DESTINO",
         "Comunidade que se reforca na dor perpetua dor. "
         "Procure quem MELHOROU, nao quem reforca o sofrimento."),
    ]
    para cada (name, expl) em explanations:
        imprima("  {name}:")
        imprima("    {expl}\n")

    // === 4. O QUE A REPUBLICA OFERECE (no lugar) ===
    imprima("\n\n  === 4. O QUE A REPUBLICA OFERECE (contra-narrativa real) ===\n")
    imprima("""
  EM VEZ DE "voce sempre tera":
    A Republica oferece OpenHealth + OpenPsychology que tratam CAUSA.
    Recuperacao e POSSIVEL. Comprovada. Cientifica.

  EM VEZ DE "compre meu curso":
    OpenEducation (gratis). OpenGamesRealistic (aprende brincando).
    OpenPsychology (sem rotular). OpenPsychologyReparation (repara erro).
    Tudo ZERO custo.

  EM VEZ DE "diagnostique voce mesmo":
    So profissional diagnostica. OpenHealth oferece avaliacao real.
    OpenPsychologyAudit faz fact-check de cada diagnostico.

  EM VEZ DE "corte sua familia":
    OpenPsychology ajuda a construir relacoes. Familia APRENDE.
    Isolamento = mais dor. Coneccao = recuperacao.

  EM VEZ DE "voce e vitima para sempre":
    Voce SOFREU. Mas o passado nao define o futuro.
    Resiliencia, neuroplasticidade e recuperacao sao REAIS.
// )

    // === 5. STATS ===
    imprima("\n\n  === 5. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DO OPENMENTALHYGIENE")
    imprima("{'='*80}")
    imprima("""
  CASO FELCA:
    Influenciador de "saude mental" que dissemina:
    - "Voce sempre tera" (PERMANENCIA -- negacao de neuroplasticidade)
    - "Eu sou TDAH" (IDENTIDADE-FUSION -- doenca como personalidade)
    - "Compre meu curso" (MERCADORIA DA DOR -- monetiza sofrimento)
    - "5 sinais que voce tem" (CONTAGIO -- superdiagnostico em massa)
    - "Seu filho provavelmente tem" (ROTULAGEM DE CRIANCA)
    - "Corte quem nao entende" (DESTRUICAO RELACIONAL)
    - "Sem remedio nao funciona" (DEPENDENCIA FARMACEUTICA)

    ISSO nao e EDUCACAO EM SAUDE MENTAL.
    e PREDACAO DE PESSOAS VULNERAVEIS.
    A Republica BLOQUEIA.

  O QUE e PROIBIDO:
    1. Narrativa de PERMANENCIA ("nunca melhora") -- cientificamente falso
    2. MONETIZACAO de sofrimento (curso/livro/clinic sobre dor)
    3. AUTO-DIAGNOSTICO em massa ("voce tambem tem")
    4. ROTULAGEM de criancas ("seu filho tem TDAH")
    5. ANTI-RECUPERACAO ("aceite, nao tente melhorar")
    6. DEPENDENCIA farmaceutica perpetua ("remedio para sempre")
    7. CULTO de comunidade que se reforca na dor
    8. INVALIDACAO de quem melhorou

  O QUE e PERMITIDO:
    1. Discussao honesta de saude mental
    2. Informacao cientifica verificada
    3. Relato pessoal de recuperacao (nao de permanencia)
    4. Orientacao para procurar PROFISSIONAL
    5. Apoio mutuo focado em MELHORA (nao em perpetuar dor)

  O QUE A REPUBLICA DIZ:
    "Seu cerebro MUDA. Recuperacao e possivel.
     Diagnostico nao e identidade. e ferramenta.
     Voce nao e sua doenca. Voce e PESSOA.
     Procure OpenHealth. e gratuito. e cientifico.
     Nao compre curso de quem lucra com sua dor."

  A CIENCIA:
    Neuroplasticidade: cerebro cria novas conexoes ate os 90 anos (Kandel, Nobel 2000)
    Recuperacao em saude mental: 40-60% em estudos longitudinais
    Desmame de psicofarmacos: possivel com acompanhamento
    Terapia > medicacao isolada em maioria dos casos
    desempacote Exercicio, nutricao, sono, conexao social = fatores terapeuticos

  PRINCIPIOS:
    seja P1: Conhecimento nocivo que perpetua dor = anti-elitismo violado
        (mantem pessoas dependentes e vulneraveis)
    P2: Autonomia corporal inclui autonomia MENTAL
        (ninguem tem direito de dizer que sua mente nao muda)
    seja P3: Educacao em saude mental real = trabalho de alto impacto
    P4: Bloqueio proporcional. Apelo garantido. Juri decide controversias.
// )
    imprima("{'='*80}")
    imprima("  OpenMentalHygiene: {s['blocked']} bloqueados, "
          "{s['corrected']} corrigidos, "
          "{s['warned']} avisados.")
    imprima("  Sofrimento nao e identidade. Recuperacao e possivel.")
    imprima("  Quem monetiza sua dor NAO quer que voce melhore.")
    imprima("{'='*80}")

```
