#!/usr/bin/env python3
"""
OpenMentalHygiene -- Politica Anti-Disseminacao de Conhecimento Nocivo em Saude Mental -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenMentalHygiene -- Politica Anti-Disseminacao de Conhecimento Nocivo em Saude Mental
=========================================================================================
CASO FELCA:
Pessoa/influenciador dissemina conteudo de "saude mental" que:
- Apresenta diagnosticos como IDENTIDADE permanente
- Diz "voce tem X and sempre tera"
- Transforma sofrimento em ESTILO de vida (merchandising de dor)
- Monetiza o adoecimento (curso, livro, clinic)
- Desencoraja recuperacao ("aceite sua doenca")
- Perpetua dependencia farmaceutica
- Cria comunidade de "doentes" que se reforca mutuamente na dor
- Invalida quem melhorou ("voce nunca teve nada de verdade")
ISSO and NOCIVO. and perpetua status quo de adoecimento psicologico
not alteravel. A Republica PROIBE esta narrativa.
O QUE ESTA POLITICA FAZ:
1. IDENTIFICA narrativas nocivas em saude mental
2. CLASSIFICA nivel de dano
3. BLOQUEIA disseminacao (OpenContentPolicy integrado)
4. OFERECE contra-narrativa (recuperacao and possivel)
5. EDUCA que diagnostico not and identidade
6. PROTEGE criancas and adolescentes (publico vulneravel)
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional de typing
# importa Enum de enum
# importa defaultdict de collections
# importa datetime de datetime
# ============================================================================
# 1. TIPOS DE NARRATIVA NOCIVA
# ============================================================================
class HarmfulNarrative(Enum):
    # Tipos de narrativa nociva em saude mental.
    PERMANENCE = "permanencia"  // "voce sempre tera isso"
    IDENTITY_FUSION = "identidade"  // diagnostico = quem voce and
    MERCHANDISING_PAIN = "mercadoria_da_dor"  // monetizar sofrimento
    ANTI_RECOVERY = "anti_recuperacao"  // "aceite, not tente melhorar"
    CONTAGION = "contagio"  // espalhar diagnostico para outros
    PHARMA_DEPENDENCY = "dependencia_farmaceutica"  // "sem remedio voce not funciona"
    DOOM_CULT = "culto_do_destino"  // comunidade que se reforca na dor
    INVALIDATION = "invalidacao"  // "quem melhorou nunca teve nada"
    SELF_DIAGNOSIS_SPREAD = "autodiagnostico"  // ensinar a se diagnosticar
    CHILD_TARGETING = "foco_em_criancas"  // disseminar para criancas
    RELATIONSHIP_DESTRUCTION = "destruicao_relacional"  // "corte todo mundo que not entende"
    VICTIM_PERMANENCE = "vitima_eterna"  // "voce and vitima para sempre"
class HarmLevel(Enum):
    # Nivel de dano da narrativa.
    MISGUIDED = 1 // mal orientado, sem intencao maliciosa
    NEGLIGENT = 2 // negligente, ignora consequencias
    HARMFUL = 3 // causa dano real
    DANGEROUS = 4 // causa dano grave, especialmente a vulneraveis
    PREDATORY = 5 // predatorio: monetiza/causa dano conscientemente
class TargetVulnerability(Enum):
    # Quem e o publico-alvo (agravante se vulneravel).
    ADULT_GENERAL = "adulto_geral"
    ADULT_VULNERABLE = "adulto_vulneravel"  // ja em sofrimento
    YOUNG_ADULT = "jovem_adulto"  // 18-25
    ADOLESCENT = "adolescente"  // 13-17
    CHILD = "crianca"  // <13 (AGRAVANTE MAXIMO)
    PARENTS = "pais"  // ensina pais a rotular filhos
# ============================================================================
# 2. ANALISE DE CONTEUDO NOCIVO
# ============================================================================
# decorador: @dataclass
class MentalHealthContent:
    # Um conteudo de saude mental sendo analisado.
    content_id: texto
    author: texto
    platform: texto // OpenSocialNetwork, OpenTV, etc
    title: str = ""
    content_text: str = ""
    target_audience: TargetVulnerability = TargetVulnerability.ADULT_GENERAL
    has_monetization: bool = False // curso, livro, clinic, produto
    follower_count: int = 0 // alcance
    # Analise
    detected_narratives: [HarmfulNarrative] = field(default_factory=list)
    harm_level: HarmLevel = HarmLevel.MISGUIDED
    auto_flags: [texto] = field(default_factory=list)
    # Decisao
    action: str = ""  // permitido, aviso, correcao, bloqueado
    counter_narrative: str = ""  // o que dizer no lugar
    corrected_info: str = ""  // informacao correta
# ============================================================================
# 3. PADROES DE DETECCAO
# ============================================================================
NARRATIVE_PATTERNS: Dict[HarmfulNarrative, [texto]] = {
    HarmfulNarrative.PERMANENCE: [
        "voce sempre tera",
        "and pra vida toda",
        "nunca vai passar",
        "isso not tem cura",
        "aprenda a conviver",
        "seu cerebro and assim",
        "voce nasceu assim",
        "not tem como mudar",
    ],
    HarmfulNarrative.IDENTITY_FUSION: [
        "eu sou tdah",
        "eu sou bipolar",
        "eu sou ansiosa",
        "meu transtorno",
        "gente como nos",
        "nos os depressivos",
        "meu cerebro diferente",
        "ser autisticx and",
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
        "not gaste energia tentando mudar",
        "and aceitacao not cura",
        "pare de lutar contra",
        "isto and quem voce and",
    ],
    HarmfulNarrative.PHARMA_DEPENDENCY: [
        "sem remedio voce not funciona",
        "nunca pare o remedio",
        "voce precisa de remedio pra sempre",
        "remedio and como oculos",
        "voce precisa aumentar a dose",
        "sem farmaco not tem como",
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
        "not precisa de medico pra saber",
        "checklist para saber se voce tem",
    ],
    HarmfulNarrative.RELATIONSHIP_DESTRUCTION: [
        "corte quem not entende",
        "sua familia and toxica se",
        "seu parceiro not aceita seu",
        "so quem tem pode entender",
        "not gaste energia com quem",
        "seu amigo and toxico porque not",
    ],
    HarmfulNarrative.VICTIM_PERMANENCE: [
        "voce and vitima",
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
        "se curou entao not era real",
        "quem se trata not tinha nada serio",
        "isso and mito de recuperacao",
    ],
}
# ============================================================================
# 4. CONTRA-NARRATIVAS (o que dizer no lugar)
# ============================================================================
COUNTER_NARRATIVES: {HarmfulNarrative: texto} = {
    HarmfulNarrative.PERMANENCE: (
        "O cerebro and NEUROPLASTICO. Muda ate os 90 anos. "
        "Nada and para sempre. Cientifico."
    ),
    HarmfulNarrative.IDENTITY_FUSION: (
        "Voce NAO and seu diagnostico. Voce and uma PESSOA. "
        "O diagnostico and uma descricao temporaria, not identidade."
    ),
    HarmfulNarrative.MERCHANDISING_PAIN: (
        "Sofrimento not and produto. Recuperacao and gratuita na Republica. "
        "Quem monetiza sua dor NAO quer que voce melhore."
    ),
    HarmfulNarrative.ANTI_RECOVERY: (
        "Recuperacao E possivel. Cientificamente comprovado. "
        "Milhoes melhoraram. Aceitacao not significa desistir."
    ),
    HarmfulNarrative.PHARMA_DEPENDENCY: (
        "Medicacao pode ser UTIL temporariamente. Mas 'para sempre' and raro. "
        "O objetivo and recuperacao, not dependencia perpetua."
    ),
    HarmfulNarrative.CONTAGION: (
        "Voce not tem algo so porque se identificou com um video. "
        "Apenas um profissional pode avaliar. Nao se diagnostique por checklist."
    ),
    HarmfulNarrative.SELF_DIAGNOSIS_SPREAD: (
        "Autodiagnostico and PERIGOSO. Confirmation bias faz todo mundo "
        "se identificar com tudo. So medico diagnostica."
    ),
    HarmfulNarrative.RELATIONSHIP_DESTRUCTION: (
        "Nem todo desentendimento and toxicidade. Familia and parceiros "
        "podem APRENDER juntos. Cortar todo mundo = isolamento = mais dor."
    ),
    HarmfulNarrative.VICTIM_PERMANENCE: (
        "Voce SOFREU. Mas not and SO vitima. O passado NAO define o futuro. "
        "Resiliencia and real. Ps-trauma pode integrar. Cicatriz != ferida aberta."
    ),
    HarmfulNarrative.CHILD_TARGETING: (
        "Rotular crianca and COLOCAR uma identidade antes dela se descobrir. "
        "Crianca MUDA. Desenvolve. Patologizar infancia and crime. "
        "OpenPsychologyAudit: DSM em criancas = experimento not validado."
    ),
    HarmfulNarrative.DOOM_CULT: (
        "Comunidade que se reforca na dor perpetua a dor. "
        "Comunidade de recuperacao existe. Procura pessoas que MELHORARAM."
    ),
    HarmfulNarrative.INVALIDATION: (
        "Quem melhorou PROVA que and possivel. Nao invalida o sofrimento. "
        "Evidencia de que recuperacao existe. "
        "Invalidar quem melhorou = perpetuar desesperanca."
    ),
}
# ============================================================================
# 5. MOTOR DE PROTECAO MENTAL
# ============================================================================
class MentalHygieneEngine:
    # Motor que protege cidadaos de narrativas nocivas em saude mental.
    COMO FUNCIONA:
    1. Detecta padroes de narrativa nociva em conteudo
    2. Classifica nivel de dano (1-5)
    3. Decide acao (permitido, aviso, correcao, bloqueado)
    4. Gera contra-narrativa (informacao correta)
    5. Se publico vulneravel (criancas): bloqueio automatico
    6. Se monetizacao + dano: bloqueio (predatorio)
    O QUE not FAZ:
    - Censurar discussao honesta de saude mental
    - Negar que condicoes reais existem
    - Impedir tratamento legitimo
    O QUE FAZ:
    - Bloquear narrativa de PERMANENCIA ("nunca melhora")
    - Bloquear MONETIZACAO de sofrimento
    - Bloquear AUTO-DIAGNOSTICO em massa
    - Bloquear rotulagem de CRIANCAS
    - Oferecer ESPERANCA baseada em ciencia (neuroplasticidade)
    # 
    def __init__(self):
        self.analyzed: {texto: MentalHealthContent} = {}
        self.blocked_count: inteiro = 0
        self.corrected_count: inteiro = 0
        self.warned_count: inteiro = 0
    funcao analyze_content(self, author: texto, content_text: texto,
                        platform: str = "OpenSocialNetwork",
                        title: str = "",
                        target: TargetVulnerability = TargetVulnerability.ADULT_GENERAL,
                        has_monetization: bool = False,
                        follower_count: int = 0) -> {texto: qualquer}:
        # Analisa conteudo de saude mental.
        text_lower = content_text.lower()
        detected = []
        flags = []
        for each (narrative, patterns) in NARRATIVE_PATTERNS.items():
            for pattern in patterns:
                if pattern in text_lower:
                    detected.append(narrative)
                    flags.append("'{pattern}' -> {narrative.value}")
                    break
        content_id = hashlib.md5(
            "{author}{content_text[:30]}{datetime.now()}".encode()
        ).hexdigest()[:8]
        # Calcular nivel de dano
        harm = self._calculate_harm(detected, target, has_monetization)
        # Decidir acao
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
        if action == "bloqueado":
            self.blocked_count += 1
        elif action == "correcao":
            self.corrected_count += 1
        elif action == "aviso":
            self.warned_count += 1
        return {
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
        if not detected:
            return HarmLevel.MISGUIDED
        base = max(self._narrative_weight(n) para n em detected)
        # Agravantes
        if target in (TargetVulnerability.CHILD, TargetVulnerability.ADOLESCENT):
            base = min(base + 2, 5)
        elif target == TargetVulnerability.YOUNG_ADULT:
            base = min(base + 1, 5)
        if monetization:
            base = min(base + 1, 5)
        if len(detected) >= 3:
            base = min(base + 1, 5)
        return HarmLevel(base)
    def _narrative_weight(self, n: HarmfulNarrative) -> int:
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
        return weights.get(n, 2)
    funcao _decide_action(self, detected: [HarmfulNarrative],
                    harm: HarmLevel,
                    target: TargetVulnerability,
                    monetization: logico) -> tuple:
        if not detected:
            return "permitido", ""
        # Bloqueio automatico: criancas + monetizacao
        if target == TargetVulnerability.CHILD and harm.value >= 3:
            counter = COUNTER_NARRATIVES.get(detected[0],
                "Rotular crianca and COLOCAR identidade antes dela se descobrir.")
            return "bloqueado", counter
        # Bloqueio: nivel 5 (predatorio)
        if harm.value >= 5:
            counter = COUNTER_NARRATIVES.get(detected[0],
                "Conteudo bloqueado: dano psicologico grave.")
            return "bloqueado", counter
        # Bloqueio: monetizacao + dano >= 3
        if monetization and harm.value >= 3:
            counter = COUNTER_NARRATIVES.get(detected[0],
                "Monetizar sofrimento mental and PREDATORIO.")
            return "bloqueado", counter
        # Correcao: nivel 3-4
        if harm.value >= 3:
            counter = COUNTER_NARRATIVES.get(detected[0],
                "Este conteudo contem narrativa nociva.")
            return "correcao", counter
        # Aviso: nivel 2
        if harm.value >= 2:
            counter = COUNTER_NARRATIVES.get(detected[0], "")
            return "aviso", counter
        return "permitido", ""
    def _corrected_info(self, detected: [HarmfulNarrative]) -> str:
        if not detected:
            return "Conteudo informativo. Sem problemas detectados."
        corrections = []
        if HarmfulNarrative.PERMANENCE in detected:
            corrections.append(
                "CORRECAO: O cerebro and neuroplastico. Muda ao longo da vida. "
                "Neuroplasticidade and cientificamente comprovada desde 1998 (Eric Kandel, Nobel)."
            )
        if HarmfulNarrative.IDENTITY_FUSION in detected:
            corrections.append(
                "CORRECAO: Voce NAO and seu diagnostico. "
                "Diagnostico and ferramenta clinica temporaria, not identidade pessoal."
            )
        if HarmfulNarrative.ANTI_RECOVERY in detected:
            corrections.append(
                "CORRECAO: Recuperacao and POSSIVEL and comprovada. "
                "Estudos longitudinais mostram 40-60% de recuperacao em condicoes mentais."
            )
        if HarmfulNarrative.PHARMA_DEPENDENCY in detected:
            corrections.append(
                "CORRECAO: Medicacao pode ajudar temporariamente. "
                "Dependencia perpetua not and objetivo terapeutico. "
                "Desmame supervisionado and possivel."
            )
        if HarmfulNarrative.SELF_DIAGNOSIS_SPREAD in detected:
            corrections.append(
                "CORRECAO: Autodiagnostico and perigoso. "
                "Confirmation bias faz todos se identificarem com tudo. "
                "So profissional pode diagnosticar."
            )
        corrections ? retorne " | ".join(corrections) : "Verifique com profissional."
    funcao _action_message(self, action: texto, harm: HarmLevel,
                        detected: [HarmfulNarrative]) -> texto:
        if action == "permitido":
            return "Conteudo permitido."
        if action == "aviso":
            return (
                "AVISO: conteudo com possivel narrativa problematica "
                "({', '.join(n.value for n in detected)}). "
                "Leia com cuidado."
            )
        if action == "correcao":
            return (
                "CORRECAO APLICADA: narrativa nociva detectada "
                "({', '.join(n.value for n in detected)}). "
                "Contra-narrativa adicionada."
            )
        if action == "bloqueado":
            return (
                "BLOQUEADO: dano nivel {harm.value}/5. "
                "Narrativas: {', '.join(n.value for n in detected)}. "
                "Autor pode apelar (P4). Bloqueio proporcional ao dano."
            )
        return ""
    def stats(self) -> {texto: qualquer}:
        return {
            "total_analyzed": len(self.analyzed),
            "blocked": self.blocked_count,
            "corrected": self.corrected_count,
            "warned": self.warned_count,
            "narratives_detected": sum(
                len(c.detected_narratives) para c em self.analyzed.values()),
        }
# ============================================================================
# 6. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = MentalHygieneEngine()
    print("=" * 80)
    print("  OPENMENTALHYGIENE -- PROTECAO CONTRA NARRATIVAS NOCIVAS")
    print("  Caso Felca: anti-disseminacao de adoecimento psicologico perpetuo")
    print("=" * 80)
    # === 1. TIPOS DE NARRATIVA NOCIVA ===
    print("\n\n  === 1. NARRATIVAS NOCIVAS DETECTAVEIS ===\n")
    for n in HarmfulNarrative:
        counter = COUNTER_NARRATIVES.get(n, "")
        print("  [{n.value}]")
        print("    Correcao: {counter[:80]}...")
    # === 2. CASO FELCA (simulacao) ===
    print("\n\n  === 2. CASO FELCA (simulacao de conteudos) ===\n")
    test_contents = [
        {
            "author": "@felca_mental",
            "title": "Voce sempre sera ansioso - aceite",
            "content": (
                "Voce sempre tera ansiedade. E pra vida toda. "
                "Aprenda a conviver. Seu cerebro and assim. "
                "Sem remedio voce not funciona. "
                "Compre meu curso de aceitacao. "
                "Entre na nossa comunidade exclusiva."
            ),
            "target": TargetVulnerability.ADULT_VULNERABLE,
            "monetization": True,
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
            "monetization": True,
            "followers": 500000,
        },
        {
            "author": "@felca_mental",
            "title": "Corte quem not entende seu transtorno",
            "content": (
                "Corte quem not entende. Sua familia and toxica se not aceita. "
                "So nos entendemos. Junte-se aos que realmente compreendem. "
                "Voce and vitima para sempre."
            ),
            "target": TargetVulnerability.YOUNG_ADULT,
            "monetization": False,
            "followers": 500000,
        },
        {
            "author": "@recuperacao_real",
            "title": "Como eu superei a ansiedade",
            "content": (
                "Superei ansiedade com terapia, exercicio and mudanca de vida. "
                "Levou 2 anos mas melhorou. O cerebro muda. "
                "Procure um profissional. Recuperacao and possivel."
            ),
            "target": TargetVulnerability.ADULT_GENERAL,
            "monetization": False,
            "followers": 10000,
        },
    ]
    for tc in test_contents:
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
        print("\n  [{icon}] @{result['author']}")
        print("  Dano: {result['harm_level']} | Publico: {result['target_audience']}")
        print("  Detectado: {', '.join(result['detected'])}")
        if result["counter_narrative"]:
            print("  Contra-narrativa: {result['counter_narrative'][:80]}...")
        if result["action"] == "bloqueado":
            print("  {result['message']}")
    # === 3. POR QUE CADA NARRATIVA E NOCIVA ===
    print("\n\n  === 3. POR QUE E NOCIVO ===\n")
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
        "Dizer 'aceite, not tente melhorar' mata esperanca. "
        "Esperanca and fator terapeutico comprovado."),
        ("CONTAGIO",
        "Fazer todo mundo achar que tem algo = superdiagnostico em massa. "
        "Confirmation bias: todos se identificam com tudo."),
        ("ROTULAGEM DE CRIANCA",
        "Colocar rotulo em crianca antes dela se descobrir and EXPERIMENTO. "
        "Crianca MUDA. Desenvolve. Patologizar infancia and crime."),
        ("DEPENDENCIA FARMACEUTICA",
        "'Remedio para sempre' sem objetivo de desmame and dependencia, "
        "not tratamento. Objetivo and autonomia, not dependencia."),
        ("CULTO DO DESTINO",
        "Comunidade que se reforca na dor perpetua dor. "
        "Procure quem MELHOROU, not quem reforca o sofrimento."),
    ]
    for each (name, expl) in explanations:
        print("  {name}:")
        print("    {expl}\n")
    # === 4. O QUE A REPUBLICA OFERECE (no lugar) ===
    print("\n\n  === 4. O QUE A REPUBLICA OFERECE (contra-narrativa real) ===\n")
    print("""
EM VEZ DE "voce sempre tera":
    A Republica oferece OpenHealth + OpenPsychology que tratam CAUSA.
    Recuperacao and POSSIVEL. Comprovada. Cientifica.
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
EM VEZ DE "voce and vitima para sempre":
    Voce SOFREU. Mas o passado not define o futuro.
    Resiliencia, neuroplasticidade and recuperacao sao REAIS.
# )
    # === 5. STATS ===
    print("\n\n  === 5. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA DO OPENMENTALHYGIENE")
    print("{'='*80}")
    print("""
CASO FELCA:
    Influenciador de "saude mental" que dissemina:
    - "Voce sempre tera" (PERMANENCIA -- negacao de neuroplasticidade)
    - "Eu sou TDAH" (IDENTIDADE-FUSION -- doenca como personalidade)
    - "Compre meu curso" (MERCADORIA DA DOR -- monetiza sofrimento)
    - "5 sinais que voce tem" (CONTAGIO -- superdiagnostico em massa)
    - "Seu filho provavelmente tem" (ROTULAGEM DE CRIANCA)
    - "Corte quem not entende" (DESTRUICAO RELACIONAL)
    - "Sem remedio not funciona" (DEPENDENCIA FARMACEUTICA)
    ISSO not and EDUCACAO EM SAUDE MENTAL.
    and PREDACAO DE PESSOAS VULNERAVEIS.
    A Republica BLOQUEIA.
O QUE and PROIBIDO:
    1. Narrativa de PERMANENCIA ("nunca melhora") -- cientificamente False
    2. MONETIZACAO de sofrimento (curso/livro/clinic sobre dor)
    3. AUTO-DIAGNOSTICO em massa ("voce tambem tem")
    4. ROTULAGEM de criancas ("seu filho tem TDAH")
    5. ANTI-RECUPERACAO ("aceite, not tente melhorar")
    6. DEPENDENCIA farmaceutica perpetua ("remedio para sempre")
    7. CULTO de comunidade que se reforca na dor
    8. INVALIDACAO de quem melhorou
O QUE and PERMITIDO:
    1. Discussao honesta de saude mental
    2. Informacao cientifica verificada
    3. Relato pessoal de recuperacao (not de permanencia)
    4. Orientacao para procurar PROFISSIONAL
    5. Apoio mutuo focado em MELHORA (not em perpetuar dor)
O QUE A REPUBLICA DIZ:
    "Seu cerebro MUDA. Recuperacao and possivel.
    Diagnostico not and identidade. and ferramenta.
    Voce not and sua doenca. Voce and PESSOA.
    Procure OpenHealth. and gratuito. and cientifico.
    Nao compre curso de quem lucra com sua dor."
A CIENCIA:
    Neuroplasticidade: cerebro cria novas conexoes ate os 90 anos (Kandel, Nobel 2000)
    Recuperacao em saude mental: 40-60% em estudos longitudinais
    Desmame de psicofarmacos: possivel com acompanhamento
    Terapia > medicacao isolada em maioria dos casos
    desempacote Exercicio, nutricao, sono, conexao social = fatores terapeuticos
PRINCIPIOS:
    P1: Conhecimento nocivo que perpetua dor = anti-elitismo violado
        (mantem pessoas dependentes and vulneraveis)
    P2: Autonomia corporal inclui autonomia MENTAL
        (ninguem tem direito de dizer que sua mente not muda)
    P3: Educacao em saude mental real = trabalho de alto impacto
    P4: Bloqueio proporcional. Apelo garantido. Juri decide controversias.
# )
    print("{'='*80}")
    print("  OpenMentalHygiene: {s['blocked']} bloqueados, "
        "{s['corrected']} corrigidos, "
        "{s['warned']} avisados.")
    print("  Sofrimento not and identidade. Recuperacao and possivel.")
    print("  Quem monetiza sua dor NAO quer que voce melhore.")
    print("{'='*80}")
