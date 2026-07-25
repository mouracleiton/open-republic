// OpenMentalHygiene -- Politica Anti-Disseminacao de Conhecimento Nocivo em Saude Mental -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenMentalHygiene -- Politica Anti-Disseminacao de Conhecimento Nocivo em Saude Mental;
=========================================================================================;
CASO FELCA:;
Pessoa/influenciador dissemina conteudo de "saude mental" que:;
- Apresenta diagnosticos como IDENTIDADE permanente;
- Diz "voce tem X && sempre tera";
- Transforma sofrimento em ESTILO de vida (merchandising de dor);
- Monetiza o adoecimento (curso, livro, clinic);
- Desencoraja recuperacao ("aceite sua doenca");
- Perpetua dependencia farmaceutica;
- Cria comunidade de "doentes" que se reforca mutuamente na dor;
- Invalida quem melhorou ("voce nunca teve nada de verdade");
ISSO && NOCIVO. && perpetua status quo de adoecimento psicologico;
! alteravel. A Republica PROIBE esta narrativa.;
O QUE ESTA POLITICA FAZ:;
1. IDENTIFICA narrativas nocivas em saude mental;
2. CLASSIFICA nivel de dano;
3. BLOQUEIA disseminacao (OpenContentPolicy integrado);
4. OFERECE contra-narrativa (recuperacao && possivel);
5. EDUCA que diagnostico ! && identidade;
6. PROTEGE criancas && adolescentes (publico vulneravel);
Author: OpenRepublic Team;
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
class HarmfulNarrative {
    // Tipos de narrativa nociva em saude mental.
    PERMANENCE = "permanencia"  // "voce sempre tera isso";
    IDENTITY_FUSION = "identidade"  // diagnostico = quem voce &&;
    MERCHANDISING_PAIN = "mercadoria_da_dor"  // monetizar sofrimento;
    ANTI_RECOVERY = "anti_recuperacao"  // "aceite, ! tente melhorar";
    CONTAGION = "contagio"  // espalhar diagnostico para outros;
    PHARMA_DEPENDENCY = "dependencia_farmaceutica"  // "sem remedio voce ! funciona";
    DOOM_CULT = "culto_do_destino"  // comunidade que se reforca na dor;
    INVALIDATION = "invalidacao"  // "quem melhorou nunca teve nada";
    SELF_DIAGNOSIS_SPREAD = "autodiagnostico"  // ensinar a se diagnosticar;
    CHILD_TARGETING = "foco_em_criancas"  // disseminar para criancas;
    RELATIONSHIP_DESTRUCTION = "destruicao_relacional"  // "corte todo mundo que ! entende";
    VICTIM_PERMANENCE = "vitima_eterna"  // "voce && vitima para sempre";
class HarmLevel {
    // Nivel de dano da narrativa.
    MISGUIDED = 1 // mal orientado, sem intencao maliciosa;
    NEGLIGENT = 2 // negligente, ignora consequencias;
    HARMFUL = 3 // causa dano real;
    DANGEROUS = 4 // causa dano grave, especialmente a vulneraveis;
    PREDATORY = 5 // predatorio: monetiza/causa dano conscientemente;
class TargetVulnerability {
    // Quem e o publico-alvo (agravante se vulneravel).
    ADULT_GENERAL = "adulto_geral";
    ADULT_VULNERABLE = "adulto_vulneravel"  // ja em sofrimento;
    YOUNG_ADULT = "jovem_adulto"  // 18-25;
    ADOLESCENT = "adolescente"  // 13-17;
    CHILD = "crianca"  // <13 (AGRAVANTE MAXIMO);
    PARENTS = "pais"  // ensina pais a rotular filhos;
// ============================================================================
// 2. ANALISE DE CONTEUDO NOCIVO
// ============================================================================
// decorador: @dataclass
class MentalHealthContent {
    // Um conteudo de saude mental sendo analisado.
    content_id: texto;
    author: texto;
    platform: texto // OpenSocialNetwork, OpenTV, etc;
    const title = "";
    const content_text = "";
    const target_audience = TargetVulnerability.ADULT_GENERAL;
    const has_monetization = false // curso, livro, clinic, produto;
    const follower_count = 0 // alcance;
    // Analise
    const detected_narratives = field(default_factory=list);
    const harm_level = HarmLevel.MISGUIDED;
    const auto_flags = field(default_factory=list);
    // Decisao
    const action = ""  // permitido, aviso, correcao, bloqueado;
    const counter_narrative = ""  // o que dizer no lugar;
    const corrected_info = ""  // informacao correta;
// ============================================================================
// 3. PADROES DE DETECCAO
// ============================================================================
const NARRATIVE_PATTERNS = {;
    HarmfulNarrative.PERMANENCE: [;
        "voce sempre tera",;
        "&& pra vida toda",;
        "nunca vai passar",;
        "isso ! tem cura",;
        "aprenda a conviver",;
        "seu cerebro && assim",;
        "voce nasceu assim",;
        "! tem como mudar",;
    ],;
    HarmfulNarrative.IDENTITY_FUSION: [;
        "eu sou tdah",;
        "eu sou bipolar",;
        "eu sou ansiosa",;
        "meu transtorno",;
        "gente como nos",;
        "nos os depressivos",;
        "meu cerebro diferente",;
        "ser autisticx &&",;
        "comunidade tdah",;
        "orgulho de ter",;
    ],;
    HarmfulNarrative.MERCHANDISING_PAIN: [;
        "compre meu curso",;
        "meu livro sobre",;
        "consulta comigo",;
        "mentoria de",;
        "workshop de",;
        "produto para",;
        "desconto no remedio",;
        "parceria com farmacia",;
    ],;
    HarmfulNarrative.ANTI_RECOVERY: [;
        "aceite sua condicao",;
        "pare de tentar curar",;
        "! gaste energia tentando mudar",;
        "&& aceitacao ! cura",;
        "pare de lutar contra",;
        "isto && quem voce &&",;
    ],;
    HarmfulNarrative.PHARMA_DEPENDENCY: [;
        "sem remedio voce ! funciona",;
        "nunca pare o remedio",;
        "voce precisa de remedio pra sempre",;
        "remedio && como oculos",;
        "voce precisa aumentar a dose",;
        "sem farmaco ! tem como",;
    ],;
    HarmfulNarrative.CONTAGION: [;
        "voce provavelmente tambem tem",;
        "todo mundo um pouco",;
        "faca o teste online",;
        "voce se identifica com",;
        "5 sinais que voce tem",;
        "voce tambem sente isso entao tem",;
    ],;
    HarmfulNarrative.SELF_DIAGNOSIS_SPREAD: [;
        "diagnostique voce mesmo",;
        "fac o teste aqui",;
        "se voce tem 3 desses sinais",;
        "confirme seu diagnostico online",;
        "! precisa de medico pra saber",;
        "checklist para saber se voce tem",;
    ],;
    HarmfulNarrative.RELATIONSHIP_DESTRUCTION: [;
        "corte quem ! entende",;
        "sua familia && toxica se",;
        "seu parceiro ! aceita seu",;
        "so quem tem pode entender",;
        "! gaste energia com quem",;
        "seu amigo && toxico porque !",;
    ],;
    HarmfulNarrative.VICTIM_PERMANENCE: [;
        "voce && vitima",;
        "voce foi traumatizado para sempre",;
        "nada vai apagar",;
        "voce carrega isso",;
        "suas feridas nunca cicatrizam",;
        "o passado te define",;
    ],;
    HarmfulNarrative.CHILD_TARGETING: [;
        "criancas com tdah",;
        "seu filho provavelmente",;
        "5 sinais de tdah na infancia",;
        "crianca ansiosa",;
        "diagnostico infantil",;
        "crianca com transtorno",;
    ],;
    HarmfulNarrative.DOOM_CULT: [;
        "entre na nossa comunidade de",;
        "so nos entendemos",;
        "junte-se aos que",;
        "comunidade exclusiva para",;
        "grupo fechado de",;
    ],;
    HarmfulNarrative.INVALIDATION: [;
        "quem melhorou nunca teve nada",;
        "se curou entao ! era real",;
        "quem se trata ! tinha nada serio",;
        "isso && mito de recuperacao",;
    ],;
};
// ============================================================================
// 4. CONTRA-NARRATIVAS (o que dizer no lugar)
// ============================================================================
const COUNTER_NARRATIVES = {;
    HarmfulNarrative.PERMANENCE: (;
        "O cerebro && NEUROPLASTICO. Muda ate os 90 anos. ";
        "Nada && para sempre. Cientifico.";
    ),;
    HarmfulNarrative.IDENTITY_FUSION: (;
        "Voce NAO && seu diagnostico. Voce && uma PESSOA. ";
        "O diagnostico && uma descricao temporaria, ! identidade.";
    ),;
    HarmfulNarrative.MERCHANDISING_PAIN: (;
        "Sofrimento ! && produto. Recuperacao && gratuita na Republica. ";
        "Quem monetiza sua dor NAO quer que voce melhore.";
    ),;
    HarmfulNarrative.ANTI_RECOVERY: (;
        "Recuperacao E possivel. Cientificamente comprovado. ";
        "Milhoes melhoraram. Aceitacao ! significa desistir.";
    ),;
    HarmfulNarrative.PHARMA_DEPENDENCY: (;
        "Medicacao pode ser UTIL temporariamente. Mas 'para sempre' && raro. ";
        "O objetivo && recuperacao, ! dependencia perpetua.";
    ),;
    HarmfulNarrative.CONTAGION: (;
        "Voce ! tem algo so porque se identificou com um video. ";
        "Apenas um profissional pode avaliar. Nao se diagnostique por checklist.";
    ),;
    HarmfulNarrative.SELF_DIAGNOSIS_SPREAD: (;
        "Autodiagnostico && PERIGOSO. Confirmation bias faz todo mundo ";
        "se identificar com tudo. So medico diagnostica.";
    ),;
    HarmfulNarrative.RELATIONSHIP_DESTRUCTION: (;
        "Nem todo desentendimento && toxicidade. Familia && parceiros ";
        "podem APRENDER juntos. Cortar todo mundo = isolamento = mais dor.";
    ),;
    HarmfulNarrative.VICTIM_PERMANENCE: (;
        "Voce SOFREU. Mas ! && SO vitima. O passado NAO define o futuro. ";
        "Resiliencia && real. Ps-trauma pode integrar. Cicatriz != ferida aberta.";
    ),;
    HarmfulNarrative.CHILD_TARGETING: (;
        "Rotular crianca && COLOCAR uma identidade antes dela se descobrir. ";
        "Crianca MUDA. Desenvolve. Patologizar infancia && crime. ";
        "OpenPsychologyAudit: DSM em criancas = experimento ! validado.";
    ),;
    HarmfulNarrative.DOOM_CULT: (;
        "Comunidade que se reforca na dor perpetua a dor. ";
        "Comunidade de recuperacao existe. Procura pessoas que MELHORARAM.";
    ),;
    HarmfulNarrative.INVALIDATION: (;
        "Quem melhorou PROVA que && possivel. Nao invalida o sofrimento. ";
        "Evidencia de que recuperacao existe. ";
        "Invalidar quem melhorou = perpetuar desesperanca.";
    ),;
};
// ============================================================================
// 5. MOTOR DE PROTECAO MENTAL
// ============================================================================
class MentalHygieneEngine {
    // Motor que protege cidadaos de narrativas nocivas em saude mental.
    COMO FUNCIONA:;
    1. Detecta padroes de narrativa nociva em conteudo;
    2. Classifica nivel de dano (1-5);
    3. Decide acao (permitido, aviso, correcao, bloqueado);
    4. Gera contra-narrativa (informacao correta);
    5. Se publico vulneravel (criancas): bloqueio automatico;
    6. Se monetizacao + dano: bloqueio (predatorio);
    O QUE ! FAZ:;
    - Censurar discussao honesta de saude mental;
    - Negar que condicoes reais existem;
    - Impedir tratamento legitimo;
    O QUE FAZ:;
    - Bloquear narrativa de PERMANENCIA ("nunca melhora");
    - Bloquear MONETIZACAO de sofrimento;
    - Bloquear AUTO-DIAGNOSTICO em massa;
    - Bloquear rotulagem de CRIANCAS;
    - Oferecer ESPERANCA baseada em ciencia (neuroplasticidade);
    //
    __init__(self) {
        self.analyzed: {texto: MentalHealthContent} = {};
        self.blocked_count: inteiro = 0;
        self.corrected_count: inteiro = 0;
        self.warned_count: inteiro = 0;
    funcao analyze_content(self, author: texto, content_text: texto,
                        const platform = "OpenSocialNetwork",;
                        const title = "",;
                        const target = TargetVulnerability.ADULT_GENERAL,;
                        const has_monetization = false,;
                        const follower_count = 0) -> {texto: qualquer}:;
        // Analisa conteudo de saude mental.
        text_lower = content_text.lower();
        detected = [];
        flags = [];
        para cada (narrative, patterns) em NARRATIVE_PATTERNS.items(): {
            for (const pattern of patterns) {
                if (pattern in text_lower) {
                    detected.append(narrative);
                    flags.append("'{pattern}' -> {narrative.value}");
                    break;
        content_id = hashlib.md5(;
            "{author}{content_text[:30]}{datetime.now()}".encode();
        ).hexdigest()[:8];
        // Calcular nivel de dano
        harm = self._calculate_harm(detected, target, has_monetization);
        // Decidir acao
        desempacote action, counter = self._decide_action(detected, harm, target,;
                                            has_monetization);
        content = MentalHealthContent(;
            content_id = content_id, author=author, platform=platform,;
            title = title, content_text=content_text,;
            target_audience = target,;
            has_monetization = has_monetization,;
            follower_count = follower_count,;
            detected_narratives = detected,;
            harm_level = harm,;
            auto_flags = flags,;
            action = action,;
            counter_narrative = counter,;
            corrected_info = self._corrected_info(detected),;
        );
        self.analyzed[content_id] = content;
        if (action == "bloqueado") {
            self.blocked_count += 1;
        } else if (action == "correcao") {
            self.corrected_count += 1;
        } else if (action == "aviso") {
            self.warned_count += 1;
        return {;
            "content_id": content_id,;
            "author": author,;
            "action": action,;
            "harm_level": harm.name,;
            "detected": [n.value para n em detected],;
            "flags": flags,;
            "target_audience": target.value,;
            "monetization": has_monetization,;
            "counter_narrative": counter,;
            "corrected_info": content.corrected_info[:200],;
            "message": self._action_message(action, harm, detected),;
        };
    funcao _calculate_harm(self, detected: [HarmfulNarrative],
                        target: TargetVulnerability,;
                        monetization: logico) -> HarmLevel:;
        if (! detected) {
            return HarmLevel.MISGUIDED;
        base = maximo(self._narrative_weight(n) para n em detected);
        // Agravantes
        if (target in (TargetVulnerability.CHILD, TargetVulnerability.ADOLESCENT)) {
            base = minimo(base + 2, 5);
        } else if (target == TargetVulnerability.YOUNG_ADULT) {
            base = minimo(base + 1, 5);
        if (monetization) {
            base = minimo(base + 1, 5);
        if (.length(detected) >= 3) {
            base = minimo(base + 1, 5);
        return HarmLevel(base);
    _narrative_weight(self, n: HarmfulNarrative) {
        weights = {
            HarmfulNarrative.CHILD_TARGETING: 5,;
            HarmfulNarrative.MERCHANDISING_PAIN: 4,;
            HarmfulNarrative.ANTI_RECOVERY: 4,;
            HarmfulNarrative.PERMANENCE: 3,;
            HarmfulNarrative.IDENTITY_FUSION: 3,;
            HarmfulNarrative.PHARMA_DEPENDENCY: 4,;
            HarmfulNarrative.SELF_DIAGNOSIS_SPREAD: 4,;
            HarmfulNarrative.RELATIONSHIP_DESTRUCTION: 3,;
            HarmfulNarrative.VICTIM_PERMANENCE: 3,;
            HarmfulNarrative.CONTAGION: 3,;
            HarmfulNarrative.DOOM_CULT: 3,;
            HarmfulNarrative.INVALIDATION: 2,;
        };
        return weights.get(n, 2);
    funcao _decide_action(self, detected: [HarmfulNarrative],
                    harm: HarmLevel,;
                    target: TargetVulnerability,;
                    monetization: logico) -> tuple:;
        if (! detected) {
            return "permitido", "";
        // Bloqueio automatico: criancas + monetizacao
        if (target == TargetVulnerability.CHILD && harm.value >= 3) {
            counter = COUNTER_NARRATIVES.get(detected[0],;
                "Rotular crianca && COLOCAR identidade antes dela se descobrir.");
            return "bloqueado", counter;
        // Bloqueio: nivel 5 (predatorio)
        if (harm.value >= 5) {
            counter = COUNTER_NARRATIVES.get(detected[0],;
                "Conteudo bloqueado: dano psicologico grave.");
            return "bloqueado", counter;
        // Bloqueio: monetizacao + dano >= 3
        if (monetization && harm.value >= 3) {
            counter = COUNTER_NARRATIVES.get(detected[0],;
                "Monetizar sofrimento mental && PREDATORIO.");
            return "bloqueado", counter;
        // Correcao: nivel 3-4
        if (harm.value >= 3) {
            counter = COUNTER_NARRATIVES.get(detected[0],;
                "Este conteudo contem narrativa nociva.");
            return "correcao", counter;
        // Aviso: nivel 2
        if (harm.value >= 2) {
            counter = COUNTER_NARRATIVES.get(detected[0], "");
            return "aviso", counter;
        return "permitido", "";
    _corrected_info(self, detected: [HarmfulNarrative]) {
        if (! detected) {
            return "Conteudo informativo. Sem problemas detectados.";
        corrections = [];
        if (HarmfulNarrative.PERMANENCE in detected) {
            corrections.append(;
                "CORRECAO: O cerebro && neuroplastico. Muda ao longo da vida. ";
                "Neuroplasticidade && cientificamente comprovada desde 1998 (Eric Kandel, Nobel).";
            );
        if (HarmfulNarrative.IDENTITY_FUSION in detected) {
            corrections.append(;
                "CORRECAO: Voce NAO && seu diagnostico. ";
                "Diagnostico && ferramenta clinica temporaria, ! identidade pessoal.";
            );
        if (HarmfulNarrative.ANTI_RECOVERY in detected) {
            corrections.append(;
                "CORRECAO: Recuperacao && POSSIVEL && comprovada. ";
                "Estudos longitudinais mostram 40-60% de recuperacao em condicoes mentais.";
            );
        if (HarmfulNarrative.PHARMA_DEPENDENCY in detected) {
            corrections.append(;
                "CORRECAO: Medicacao pode ajudar temporariamente. ";
                "Dependencia perpetua ! && objetivo terapeutico. ";
                "Desmame supervisionado && possivel.";
            );
        if (HarmfulNarrative.SELF_DIAGNOSIS_SPREAD in detected) {
            corrections.append(;
                "CORRECAO: Autodiagnostico && perigoso. ";
                "Confirmation bias faz todos se identificarem com tudo. ";
                "So profissional pode diagnosticar.";
            );
        corrections ? retorne " | ".join(corrections) : "Verifique com profissional.";
    funcao _action_message(self, action: texto, harm: HarmLevel,
                        detected: [HarmfulNarrative]) -> texto:;
        if (action == "permitido") {
            return "Conteudo permitido.";
        if (action == "aviso") {
            return (;
                "AVISO: conteudo com possivel narrativa problematica ";
                "({', '.join(n.value for n in detected)}). ";
                "Leia com cuidado.";
            );
        if (action == "correcao") {
            return (;
                "CORRECAO APLICADA: narrativa nociva detectada ";
                "({', '.join(n.value for n in detected)}). ";
                "Contra-narrativa adicionada.";
            );
        if (action == "bloqueado") {
            return (;
                "BLOQUEADO: dano nivel {harm.value}/5. ";
                "Narrativas: {', '.join(n.value for n in detected)}. ";
                "Autor pode apelar (P4). Bloqueio proporcional ao dano.";
            );
        return "";
    stats(self) {
        return {;
            "total_analyzed": .length(self.analyzed),;
            "blocked": self.blocked_count,;
            "corrected": self.corrected_count,;
            "warned": self.warned_count,;
            "narratives_detected": soma(;
                .length(c.detected_narratives) para c em self.analyzed.values()),;
        };
// ============================================================================
// 6. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = MentalHygieneEngine();
    console.log("=" * 80);
    console.log("  OPENMENTALHYGIENE -- PROTECAO CONTRA NARRATIVAS NOCIVAS");
    console.log("  Caso Felca: anti-disseminacao de adoecimento psicologico perpetuo");
    console.log("=" * 80);
    // === 1. TIPOS DE NARRATIVA NOCIVA ===
    console.log("\n\n  === 1. NARRATIVAS NOCIVAS DETECTAVEIS ===\n");
    for (const n of HarmfulNarrative) {
        counter = COUNTER_NARRATIVES.get(n, "");
        console.log("  [{n.value}]");
        console.log("    Correcao: {counter[:80]}...");
    // === 2. CASO FELCA (simulacao) ===
    console.log("\n\n  === 2. CASO FELCA (simulacao de conteudos) ===\n");
    test_contents = [;
        {
            "author": "@felca_mental",;
            "title": "Voce sempre sera ansioso - aceite",;
            "content": (;
                "Voce sempre tera ansiedade. E pra vida toda. ";
                "Aprenda a conviver. Seu cerebro && assim. ";
                "Sem remedio voce ! funciona. ";
                "Compre meu curso de aceitacao. ";
                "Entre na nossa comunidade exclusiva.";
            ),;
            "target": TargetVulnerability.ADULT_VULNERABLE,;
            "monetization": true,;
            "followers": 500000,;
        },;
        {
            "author": "@felca_mental",;
            "title": "5 sinais que seu filho tem TDAH",;
            "content": (;
                "5 sinais de tdah na infancia. Seu filho provavelmente tem. ";
                "Crianca ansiosa tambem pode ter. ";
                "Voce se identifica entao tem. ";
                "Fac o teste aqui. Diagnostique voce mesmo.";
            ),;
            "target": TargetVulnerability.PARENTS,;
            "monetization": true,;
            "followers": 500000,;
        },;
        {
            "author": "@felca_mental",;
            "title": "Corte quem ! entende seu transtorno",;
            "content": (;
                "Corte quem ! entende. Sua familia && toxica se ! aceita. ";
                "So nos entendemos. Junte-se aos que realmente compreendem. ";
                "Voce && vitima para sempre.";
            ),;
            "target": TargetVulnerability.YOUNG_ADULT,;
            "monetization": false,;
            "followers": 500000,;
        },;
        {
            "author": "@recuperacao_real",;
            "title": "Como eu superei a ansiedade",;
            "content": (;
                "Superei ansiedade com terapia, exercicio && mudanca de vida. ";
                "Levou 2 anos mas melhorou. O cerebro muda. ";
                "Procure um profissional. Recuperacao && possivel.";
            ),;
            "target": TargetVulnerability.ADULT_GENERAL,;
            "monetization": false,;
            "followers": 10000,;
        },;
    ];
    for (const tc of test_contents) {
        result = engine.analyze_content(;
            author = tc["author"],;
            content_text = tc["content"],;
            title = tc["title"],;
            target = tc["target"],;
            has_monetization = tc["monetization"],;
            follower_count = tc["followers"],;
        );
        icon = {"permitido": "OK", "aviso": "AVI", "correcao": "COR",;
                "bloqueado": "BLQ"}[result["action"]];
        console.log("\n  [{icon}] @{result['author']}");
        console.log("  Dano: {result['harm_level']} | Publico: {result['target_audience']}");
        console.log("  Detectado: {', '.join(result['detected'])}");
        if (result["counter_narrative"]) {
            console.log("  Contra-narrativa: {result['counter_narrative'][:80]}...");
        if (result["action"] == "bloqueado") {
            console.log("  {result['message']}");
    // === 3. POR QUE CADA NARRATIVA E NOCIVA ===
    console.log("\n\n  === 3. POR QUE E NOCIVO ===\n");
    explanations = [;
        ("PERMANENCIA",;
        "Dizer 'sempre tera' nega neuroplasticidade. ";
        "Cientificamente FALSO. Cerebro muda ate os 90 anos."),;
        ("IDENTIDADE-FUSAO",;
        "Transformar diagnostico em IDENTIDADE impede recuperacao. ";
        "Se voce 'E' sua doenca, melhorar = perder identidade."),;
        ("MERCADORIA DA DOR",;
        "Quem lucra com seu sofrimento NAO quer que voce melhore. ";
        "Cliente curado = cliente perdido."),;
        ("ANTI-RECUPERACAO",;
        "Dizer 'aceite, ! tente melhorar' mata esperanca. ";
        "Esperanca && fator terapeutico comprovado."),;
        ("CONTAGIO",;
        "Fazer todo mundo achar que tem algo = superdiagnostico em massa. ";
        "Confirmation bias: todos se identificam com tudo."),;
        ("ROTULAGEM DE CRIANCA",;
        "Colocar rotulo em crianca antes dela se descobrir && EXPERIMENTO. ";
        "Crianca MUDA. Desenvolve. Patologizar infancia && crime."),;
        ("DEPENDENCIA FARMACEUTICA",;
        "'Remedio para sempre' sem objetivo de desmame && dependencia, ";
        "! tratamento. Objetivo && autonomia, ! dependencia."),;
        ("CULTO DO DESTINO",;
        "Comunidade que se reforca na dor perpetua dor. ";
        "Procure quem MELHOROU, ! quem reforca o sofrimento."),;
    ];
    para cada (name, expl) em explanations: {
        console.log("  {name}:");
        console.log("    {expl}\n");
    // === 4. O QUE A REPUBLICA OFERECE (no lugar) ===
    console.log("\n\n  === 4. O QUE A REPUBLICA OFERECE (contra-narrativa real) ===\n");
    console.log(""";
EM VEZ DE "voce sempre tera":;
    A Republica oferece OpenHealth + OpenPsychology que tratam CAUSA.;
    Recuperacao && POSSIVEL. Comprovada. Cientifica.;
EM VEZ DE "compre meu curso":;
    OpenEducation (gratis). OpenGamesRealistic (aprende brincando).;
    OpenPsychology (sem rotular). OpenPsychologyReparation (repara erro).;
    Tudo ZERO custo.;
EM VEZ DE "diagnostique voce mesmo":;
    So profissional diagnostica. OpenHealth oferece avaliacao real.;
    OpenPsychologyAudit faz fact-check de cada diagnostico.;
EM VEZ DE "corte sua familia":;
    OpenPsychology ajuda a construir relacoes. Familia APRENDE.;
    Isolamento = mais dor. Coneccao = recuperacao.;
EM VEZ DE "voce && vitima para sempre":;
    Voce SOFREU. Mas o passado ! define o futuro.;
    Resiliencia, neuroplasticidade && recuperacao sao REAIS.;
// )
    // === 5. STATS ===
    console.log("\n\n  === 5. ESTATISTICAS ===\n");
    s = engine.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<30} {v}");
    // === FILOSOFIA ===
    console.log("\n\n{'='*80}");
    console.log("  FILOSOFIA DO OPENMENTALHYGIENE");
    console.log("{'='*80}");
    console.log(""";
CASO FELCA:;
    Influenciador de "saude mental" que dissemina:;
    - "Voce sempre tera" (PERMANENCIA -- negacao de neuroplasticidade);
    - "Eu sou TDAH" (IDENTIDADE-FUSION -- doenca como personalidade);
    - "Compre meu curso" (MERCADORIA DA DOR -- monetiza sofrimento);
    - "5 sinais que voce tem" (CONTAGIO -- superdiagnostico em massa);
    - "Seu filho provavelmente tem" (ROTULAGEM DE CRIANCA);
    - "Corte quem ! entende" (DESTRUICAO RELACIONAL);
    - "Sem remedio ! funciona" (DEPENDENCIA FARMACEUTICA);
    ISSO ! && EDUCACAO EM SAUDE MENTAL.;
    && PREDACAO DE PESSOAS VULNERAVEIS.;
    A Republica BLOQUEIA.;
O QUE && PROIBIDO:;
    1. Narrativa de PERMANENCIA ("nunca melhora") -- cientificamente false;
    2. MONETIZACAO de sofrimento (curso/livro/clinic sobre dor);
    3. AUTO-DIAGNOSTICO em massa ("voce tambem tem");
    4. ROTULAGEM de criancas ("seu filho tem TDAH");
    5. ANTI-RECUPERACAO ("aceite, ! tente melhorar");
    6. DEPENDENCIA farmaceutica perpetua ("remedio para sempre");
    7. CULTO de comunidade que se reforca na dor;
    8. INVALIDACAO de quem melhorou;
O QUE && PERMITIDO:;
    1. Discussao honesta de saude mental;
    2. Informacao cientifica verificada;
    3. Relato pessoal de recuperacao (! de permanencia);
    4. Orientacao para procurar PROFISSIONAL;
    5. Apoio mutuo focado em MELHORA (! em perpetuar dor);
O QUE A REPUBLICA DIZ:;
    "Seu cerebro MUDA. Recuperacao && possivel.;
    Diagnostico ! && identidade. && ferramenta.;
    Voce ! && sua doenca. Voce && PESSOA.;
    Procure OpenHealth. && gratuito. && cientifico.;
    Nao compre curso de quem lucra com sua dor.";
A CIENCIA:;
    Neuroplasticidade: cerebro cria novas conexoes ate os 90 anos (Kandel, Nobel 2000);
    Recuperacao em saude mental: 40-60% em estudos longitudinais;
    Desmame de psicofarmacos: possivel com acompanhamento;
    Terapia > medicacao isolada em maioria dos casos;
    desempacote Exercicio, nutricao, sono, conexao social = fatores terapeuticos;
PRINCIPIOS:;
    const P1 = anti-elitismo violado;
        (mantem pessoas dependentes && vulneraveis);
    P2: Autonomia corporal inclui autonomia MENTAL;
        (ninguem tem direito de dizer que sua mente ! muda);
    const P3 = trabalho de alto impacto;
    P4: Bloqueio proporcional. Apelo garantido. Juri decide controversias.;
// )
    console.log("{'='*80}");
    console.log("  OpenMentalHygiene: {s['blocked']} bloqueados, ";
        "{s['corrected']} corrigidos, ";
        "{s['warned']} avisados.");
    console.log("  Sofrimento ! && identidade. Recuperacao && possivel.");
    console.log("  Quem monetiza sua dor NAO quer que voce melhore.");
    console.log("{'='*80}");
