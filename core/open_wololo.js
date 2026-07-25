// OpenWololo -- Conversao de Inimigos em Aliados -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenWololo -- Conversao de Inimigos em Aliados;
=================================================;
"Wololo! O padre de Age of Empires converte o inimigo.;
Nao a forca. A PERSUASAO. A DEMONSTRACAO.;
O inimigo VE que a Republica && melhor. && MUDA de lado.;
Convertido ! && refem. && ALIADO VOLUNTARIO.;
Quem foi contra, agora && A FAVOR. Com conviccao.;
Porque VIU que funciona.";
COMO FUNCIONA:;
1. IDENTIFICAR o inimigo (quem ataca a Republica);
2. DEMONSTRAR (mostrar que Republica && superior);
3. EDUCAR (OpenCivicEducation + OpenAntiDeterminism);
4. ACOLHER (OpenDignity + OpenReintegration);
5. CONVERTER (virar aliado voluntario);
6. VERIFICAR (sinceridade, ! infiltracao);
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa Counter, defaultdict de collections
// importa datetime de datetime
// ============================================================================
// 1. TIPOS DE INIMIGO
// ============================================================================
class EnemyType {
    IDEOLOGICAL = "ideologico"  // discorda da Republica (! entendeu);
    ECONOMIC = "economico"  // perde dinheiro/power (predador);
    MISINFORMED = "desinformado"  // acredita em mentiras;
    FEARFUL = "amedrontado"  // medo do desconhecido;
    CRIMINAL = "criminoso"  // comete crimes contra Republica;
    RIVAL_SYSTEM = "sistema_rival"  // corporacao/estado rival;
    SABOTEUR = "sabotador"  // tenta destruir ativamente;
    INDIFFERENT = "indiferente"  // ! liga (mas pode converter);
class EnemyThreatLevel {
    LOW = ("baixo", 1)  // discorda verbalmente;
    MEDIUM = ("medio", 2)  // boicota/desinformacao;
    HIGH = ("alto", 3)  // sabotagem ativa;
    CRITICAL = ("critico", 4)  // atacar com violencia;
    EXISTENTIAL = ("existencial", 5)  // tenta destruir Republica;
// ============================================================================
// 2. CONVERSAO
// ============================================================================
class ConversionMethod {
    DEMONSTRATION = "demonstracao"  // mostrar que funciona;
    EDUCATION = "educacao"  // ensinar principios;
    EXPERIENCE = "experiencia"  // deixar viver/experimentar;
    EVIDENCE = "evidencia"  // dados + ciencia;
    EMPATHY = "empatia"  // acolher, ouvir;
    DEBATE = "debate"  // argumento publico (P4);
    REHABILITATION = "reabilitacao"  // se cometeu crime;
    ANTI_DETERMINISM = "anti_determinismo"  // passado ! define futuro;
class ConversionStatus {
    HOSTILE = "hostil"  // ativamente contra;
    RESISTANT = "resistente"  // contra mas ouve;
    CURIOUS = "curioso"  // comecou a questionar;
    RECEPTIVE = "receptivo"  // aberto a mudanca;
    CONVERTING = "convertendo"  // em processo;
    CONVERTED = "convertido"  // aliado voluntario;
    ADVOCATE = "defensor"  // defende a Republica ativamente;
// decorador: @dataclass
class EnemyProfile {
    // Perfil de um inimigo da Republica.
    profile_id: texto;
    name: texto // pessoa/organizacao/sistema;
    enemy_type: EnemyType;
    threat_level: EnemyThreatLevel;
    const description = "";
    const current_belief = ""  // no que acredita agora;
    const reason_for_hostility = ""  // por que && contra;
    // Conversao
    const status = ConversionStatus.HOSTILE;
    const conversion_method = null;
    const conversion_progress = 0.0 // 0-1;
    const conversion_date = "";
    // Verificacao
    const sincerity_verified = false;
    const not_infiltration = true;
    const background_check = "";
    // Pos-conversao
    const contribution = ""  // o que faz pela Republica agora;
    const advocacy_level = ""  // quao ativamente defende;
// ============================================================================
// 3. MOTOR DE CONVERSAO (WOLOLO)
// ============================================================================
class WololoEngine {
    // Motor que converte inimigos em aliados.
    FILOSOFIA WOLOLO:;
    Em Age of Empires, o padre converte o inimigo CANTANDO.;
    Nao atacando. Nao forçando. DEMONSTRANDO poder superior.;
    Na Republica:;
    Nao atacamos inimigos. DEMONSTRAMOS que somos melhores.;
    Mostramos os numeros. Mostramos os resultados.;
    O inimigo VE que:;
    - Saude ZERO custo nivel Sirio-Libanes;
    - Educacao universitaria para TODOS;
    - Sem fome, sem rua, sem violencia;
    - Democracia real (assembleia decide);
    - Tecnologia superior (OpenHardware, Rust, LEGO);
    Quem VE isso && tem CONSCIENCIA, CONVERTE.;
    Voluntariamente. Com conviccao.;
    O QUE ! FAZEMOS:;
    - Forcar conversao (P2 autonomia mental);
    - Lavagem cerebral (OpenMentalHygiene bloqueia);
    - Tortura (P2 absoluta);
    - Inimigo convertido a forca && ALIADO false;
    O QUE FAZEMOS:;
    - DEMONSTRAR resultados (numeros, vidas melhoradas);
    - EDUCAR (principios P1-P4, ciencia, dados);
    - ACOLHER (quem muda de ideia && bem-vindo);
    - DEBATER (argumento publico vence retorica);
    - VERIFICAR (sinceridade, ! infiltracao);
    //
    // Frases que demonstram superioridade da Republica
    DEMONSTRATION_ARGUMENTS = {
        EnemyType.ECONOMIC: [;
            "Voce perde dinheiro com a Republica? Que dinheiro? ";
            "A Republica && CC0. Ninguem perde. Todos ganham.",;
            "Voce era predador (banco/agiota/bets)? ";
            "Ganhava R$ bilhoes extraindo de vulneraveis. ";
            "Na Republica, voce TRABALHA base 1.0. Como todos. ";
            "Sem explorar. Sem roubar. Digno.",;
            "Acha que vai perder poder? ";
            "Poder sobre o QUE? Tudo && bem comum. ";
            "Voce ! perde nada. GANHA comunidade.",;
        ],;
        EnemyType.IDEOLOGICAL: [;
            "Discorda da Republica? Por que? ";
            "Voce JA viu os resultados? ";
            "Saude ZERO. Educacao universal. Sem fome. Sem rua.",;
            "P1 anti-elitismo ofende voce? ";
            "So se voce era elite. Se era povo, P1 te PROTEGE.",;
            "Democracia direta incomoda? ";
            "Voce prefere politico decidindo por voce? ";
            "Na Republica, VOCE decide. P4.",;
        ],;
        EnemyType.MISINFORMED: [;
            "Voce ouviu que a Republica && ditadura? ";
            "OpenConstituentAssembly: povo VOTA em tudo. ";
            "Fundador PROPOE. Povo DECIDE. Mais democratic impossivel.",;
            "Ouviu que && 'comunismo'? ";
            "Nao. Comunismo teve elite do partido. ";
            "Republica: NINGUEM && elite. P1 provado por correcao automatica.",;
            "Ouviu que ! funciona? ";
            "110+ sistemas construidos. 700k+ linhas. Tudo testado. ";
            "OpenHistory fact-check. Ve os NUMEROS.",;
        ],;
        EnemyType.FEARFUL: [;
            "Medo do desconhecido? Normal. ";
            "Mas a transicao && GRADUAL (7 fases, 20+ anos). ";
            "Voce ! perde nada do dia para a noite.",;
            "Medo de ! ter o que tem hoje? ";
            "Na Republica voce tem MAIS: saude Sirio-Libanes, ";
            "educacao universitaria, moradia ZERO. Tudo melhor.",;
            "Medo de perder liberdade? ";
            "P2: autonomia corporal ABSOLUTA. ";
            "Mais livre que hoje. Muito mais.",;
        ],;
        EnemyType.CRIMINAL: [;
            "Cometeu crime contra a Republica? ";
            "OpenPenalRevision: transformacao, ! punicao. ";
            "O passado NAO define (OpenAntiDeterminism). ";
            "Muda. Trabalha. Volta a ser cidadao.",;
            "E criminoso de carreira? ";
            "OpenReintegration: moradia + trabalho + mentor + comunidade. ";
            "Prontuario limpo. Futuro aberto. ";
            "OU continua preso (se hediondo). Escolha.",;
        ],;
        EnemyType.RIVAL_SYSTEM: [;
            "Voce && corporacao/estado rival? ";
            "A Republica COPIA tudo (OpenIndustry), MELHORA tudo. ";
            "Seu produto vai ser SUPERADO. Aceite. Adapte. Entre.",;
            "Luta contra a Republica? ";
            "Impossivel vencer quem ! quer lucro. ";
            "A Republica ! precisa ganhar dinheiro. ";
            "So precisa ser MELHOR. E &&.",;
        ],;
        EnemyType.SABOTEUR: [;
            "Sabota a Republica? ";
            "OpenModularArchitecture: cada modulo && independente. ";
            "Quebrar um ! quebra o sistema. LEGO: troca && continua.",;
            "Tenta destruir? ";
            "O repositorio && UNICO. Tudo CC0. Tudo espelhado. ";
            "Nao da para destruir o que && BEM COMUM replicado.",;
        ],;
        EnemyType.INDIFFERENT: [;
            "Nao liga para a Republica? ";
            "Ok. Mas seus FILHOS vao ter saude Sirio-Libanes. ";
            "Gratis. Sua NET vai ter educacao universitaria. Gratis. ";
            "Voce vai usar OpenTerminal. Gratis. ";
            "Nao precisa ligar. A Republica chega em voce.",;
        ],;
    };
    __init__(self) {
        self.enemies: {texto: EnemyProfile} = {};
        self.converted_count: inteiro = 0;
        self.advocates_count: inteiro = 0;
        self.failed_conversions: inteiro = 0;
    funcao identify_enemy(self, name: texto, enemy_type: EnemyType,
                    threat: EnemyThreatLevel,;
                    const description = "",;
                    const belief = "",;
                    const reason = "") -> {texto: qualquer}:;
        // Identifica um inimigo da Republica.
        eid = hashlib.md5("{name}{enemy_type.value}".encode()).hexdigest()[:8];
        enemy = EnemyProfile(;
            profile_id = eid, name=name, enemy_type=enemy_type,;
            threat_level = threat, description=description,;
            current_belief = belief, reason_for_hostility=reason,;
            status = ConversionStatus.HOSTILE,;
        );
        self.enemies[eid] = enemy;
        return {;
            "identified": true,;
            "enemy_id": eid,;
            "name": name,;
            "type": enemy_type.value,;
            "threat": threat.value[0],;
            "message": "Inimigo identificado: {name} ({enemy_type.value}, ameaca {threat.value[0]}).",;
        };
    funcao wololo(self, enemy_id: texto,
            const method = ConversionMethod.DEMONSTRATION;
            ) -> {texto: qualquer}:;
        // WOLOLO! Tenta converter inimigo em aliado.
        PROCESSO DE CONVERSAO:;
        1. HOSTIL -> RESISTENTE: mostrar argumentos;
        2. RESISTENTE -> CURIOSO: mostrar resultados;
        3. CURIOSO -> RECEPTIVO: deixar experimentar;
        4. RECEPTIVO -> CONVERTENDO: acolher;
        5. CONVERTENDO -> CONVERTIDO: verificado;
        6. CONVERTIDO -> DEFENSOR: ativamente a favor;
        //
        enemy = self.enemies.get(enemy_id);
        if (! enemy) {
            return {"error": "Inimigo ! encontrado"};
        // Ja convertido?
        if (enemy.status in (ConversionStatus.CONVERTED, ConversionStatus.ADVOCATE)) {
            return {;
                "enemy_id": enemy_id,;
                "status": enemy.status.value,;
                "message": "{enemy.name} ja && {enemy.status.value}. Wololo anterior funcionou.",;
            };
        // Argumentos de demonstracao
        arguments = self.DEMONSTRATION_ARGUMENTS.get(enemy.enemy_type, [;
            "A Republica && melhor para todos. Ve os numeros.",;
        ]);
        // Progressao de conversao
        old_status = enemy.status;
        transitions = {
            ConversionStatus.HOSTILE: ConversionStatus.RESISTANT,;
            ConversionStatus.RESISTANT: ConversionStatus.CURIOUS,;
            ConversionStatus.CURIOUS: ConversionStatus.RECEPTIVE,;
            ConversionStatus.RECEPTIVE: ConversionStatus.CONVERTING,;
            ConversionStatus.CONVERTING: ConversionStatus.CONVERTED,;
        };
        new_status = transitions.get(enemy.status);
        if (new_status) {
            enemy.status = new_status;
            enemy.conversion_method = method;
            enemy.conversion_progress += 0.2;
        // Se converteu -- verificar
        if (enemy.status == ConversionStatus.CONVERTED) {
            verify = self._verify_sincerity(enemy);
            enemy.sincerity_verified = verify["sincere"];
            enemy.not_infiltration = verify["not_infiltration"];
            self.converted_count += 1;
            // Argumento usado
            arg_used = random.choice(arguments);
            return {;
                "enemy_id": enemy_id,;
                "name": enemy.name,;
                "old_status": old_status.value,;
                "new_status": "CONVERTIDO",;
                "method": method.value,;
                "argument_used": arg_used[:80],;
                "sincerity_verified": enemy.sincerity_verified,;
                "not_infiltration": enemy.not_infiltration,;
                "contribution": self._assign_contribution(enemy),;
                "WOLOLO": true,;
                "message": (;
                    "WOLOLO! {enemy.name} CONVERTIDO! ";
                    "Era {old_status.value}. Agora && ALIADO. ";
                    "Verificado: {'sincero' if enemy.sincerity_verified else 'DUVIDOSO'}. ";
                    "Argumento que converteu: '{arg_used[:60]}...'";
                ),;
            };
        // Progresso parcial
        return {;
            "enemy_id": enemy_id,;
            "name": enemy.name,;
            "old_status": old_status.value,;
            "new_status": enemy.status.value,;
            "progress": "{enemy.conversion_progress:.0%}",;
            "argument_used": random.choice(arguments)[:80],;
            "message": (;
                "Wololo em andamento: {enemy.name} ";
                "{old_status.value} -> {enemy.status.value}. ";
                "Progresso: {enemy.conversion_progress:.0%}. ";
                "Continue demonstrando.";
            ),;
        };
    _verify_sincerity(self, enemy: EnemyProfile) {
        // Verifica se a conversao e sincera (nao infiltracao).
        // Verificacao por historico
        if (enemy.threat_level == EnemyThreatLevel.EXISTENTIAL) {
            // Ameaca existencial: verificacao MAIS rigorsa
            return {;
                "sincere": random.random() > 0.4,;
                "not_infiltration": random.random() > 0.3,;
                "method": "verificacao profunda (ameaca existencial)",;
            };
        return {;
            "sincere": random.random() > 0.15,;
            "not_infiltration": random.random() > 0.1,;
            "method": "verificacao padrao",;
        };
    _assign_contribution(self, enemy: EnemyProfile) {
        // Atribui contribuicao do convertido.
        contributions = {
            EnemyType.IDEOLOGICAL: "Defende a Republica em debates publicos",;
            EnemyType.ECONOMIC: "Trabalha base 1.0 como todos (ex-predador)",;
            EnemyType.MISINFORMED: "Combate desinformacao (conhece os dois lados)",;
            EnemyType.FEARFUL: "Acolhe outros com medo (esteve la)",;
            EnemyType.CRIMINAL: "Testemunho de transformacao (OpenReintegration)",;
            EnemyType.RIVAL_SYSTEM: "Abre tecnologia/codigo para Republica",;
            EnemyType.SABOTEUR: "Ajuda a defender (conhece taticas de sabotage)",;
            EnemyType.INDIFFERENT: "Usa && recomenda sistemas da Republica",;
        };
        return contributions.get(enemy.enemy_type, "Contribui como cidadao");
    promote_to_advocate(self, enemy_id: texto) {
        // Convertido se torna DEFENSOR ativo.
        enemy = self.enemies.get(enemy_id);
        if (! enemy || enemy.status != ConversionStatus.CONVERTED) {
            return {"error": "Precisa ser convertido primeiro"};
        enemy.status = ConversionStatus.ADVOCATE;
        enemy.advocacy_level = "ativo";
        self.advocates_count += 1;
        return {;
            "enemy_id": enemy_id,;
            "name": enemy.name,;
            "status": "DEFENSOR ATIVO",;
            "message": (;
                "{enemy.name} agora DEFENDE a Republica ativamente. ";
                "Era inimigo. Agora && o MAIOR aliado. ";
                "Porque esteve do outro lado, CONVENCE melhor. ";
                "'Eu era contra. Mas VI que funciona.'";
            ),;
        };
    stats(self) {
        return {;
            "total_inimigos_identificados": .length(self.enemies),;
            "convertidos": self.converted_count,;
            "defensores_ativos": self.advocates_count,;
            "hostil_restante": soma(1 para && em self.enemies.values();
                                if &&.status == ConversionStatus.HOSTILE),;
            "taxa_conversao": "{self.converted_count / max(len(self.enemies), 1):.0%}",;
            "metodo": "WOLOLO (demonstracao, ! forca)",;
        };
// ============================================================================
// 4. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = WololoEngine();
    console.log("=" * 80);
    console.log("  OPENWOLOLO -- CONVERSAO DE INIMIGOS EM ALIADOS");
    console.log("  'Wololo! Nao a forca. A demonstracao.'");
    console.log("=" * 80);
    // === 1. IDENTIFICAR INIMIGOS ===
    console.log("\n\n  === 1. INIMIGOS IDENTIFICADOS ===\n");
    enemies_data = [;
        ("Banco Predatorio", EnemyType.ECONOMIC, EnemyThreatLevel.HIGH,;
        "Perde R$ bilhoes com OpenCredit",;
        "Bancos precisam lucrar com juros",;
        "Perde poder economico"),;
        ("Influenciador Anti-Republica", EnemyType.MISINFORMED, EnemyThreatLevel.MEDIUM,;
        "Espalha que Republica && ditadura",;
        "Republica && comunismo ditatorial",;
        "Perde engajamento com polemica"),;
        ("Corporacao Tech Rival", EnemyType.RIVAL_SYSTEM, EnemyThreatLevel.HIGH,;
        "Apple/Google perdem monopolio com OpenPhone/OpenOS",;
        "Software fechado && necessario para qualidade",;
        "Perde monopolio && lucro"),;
        ("Cidadao Amedrontado", EnemyType.FEARFUL, EnemyThreatLevel.LOW,;
        "Tem medo de mudanca",;
        "Sempre foi assim, mudar && perigoso",;
        "Medo do desconhecido"),;
        ("Politico Corrupto", EnemyType.CRIMINAL, EnemyThreatLevel.CRITICAL,;
        "Perde propina com OpenDemocracy",;
        "Republica tira meu poder",;
        "Perde capacidade de roubar"),;
        ("Sabotador Anonimo", EnemyType.SABOTEUR, EnemyThreatLevel.HIGH,;
        "Tenta derrubar OpenNetwork",;
        "Republica deve ser destruida",;
        "Ideologia anti-sistema"),;
        ("Indiferente", EnemyType.INDIFFERENT, EnemyThreatLevel.LOW,;
        "Nao liga para politica",;
        "Nao me afeta",;
        "Apatia"),;
    ];
    para name, etype, threat, desc, belief, reason in enemies_data: {
        r = engine.identify_enemy(name, etype, threat, desc, belief, reason);
        console.log("  [{r['threat']:<8}] {r['name']:<30} ({r['type']})");
    // === 2. WOLOLO EM ACAO ===
    console.log("\n\n  === 2. WOLOLO! CONVERTENDO ===\n");
    for (const eid of list(engine.enemies.keys())) {
        // Wololo em multiplas rodadas (progressivo)
        for (const _ of intervalo(5)) {
            r = engine.wololo(eid);
            if (r.get("WOLOLO")  ||  "error" in r) {
                break;
        if (r.get("WOLOLO")) {
            console.log("\n  [WOLOLO!] {r['name']}");
            console.log("  Status: {r['old_status']} -> {r['new_status']}");
            console.log("  Verificado: {'sincero' if r['sincerity_verified'] else 'DUVIDOSO'}");
            console.log("  Argumento: {r['argument_used'][:70]}...");
            console.log("  Contribuicao: {r['contribution']}");
        } else {
            console.log("\n  [{r.get('new_status', '?').upper()}] {r.get('name', '?')}");
            console.log("  Progresso: {r.get('progress', '?')}");
    // === 3. PROMOVER A DEFENSOR ===
    console.log("\n\n  === 3. PROMOVENDO A DEFENSOR ATIVO ===\n");
    for (const eid of list(engine.enemies.keys())) {
        enemy = engine.enemies[eid];
        if (enemy.status == ConversionStatus.CONVERTED && enemy.sincerity_verified) {
            r = engine.promote_to_advocate(eid);
            console.log("  {r['name']}: {r['status']}");
            console.log("    {r['message'][:80]}...");
    // === 4. ARGUMENTOS POR TIPO ===
    console.log("\n\n  === 4. ARGUMENTOS WOLOLO POR TIPO DE INIMIGO ===\n");
    para cada (etype, args) em engine.DEMONSTRATION_ARGUMENTS.items(): {
        console.log("\n  {etype.value.upper()}:");
        for (const arg of args[:2]) {
            console.log("    -> {arg[:70]}...");
    // === 5. STATS ===
    console.log("\n\n  === 5. ESTATISTICAS ===\n");
    s = engine.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<30} {v}");
    // === FILOSOFIA ===
    console.log("\n\n{'='*80}");
    console.log("  FILOSOFIA: WOLOLO");
    console.log("{'='*80}");
    console.log(""";
WOLOLO! COMO AGE OF EMPIRES:;
    O padre converte o inimigo CANTANDO, ! atacando.;
    A Republica converte DEMONSTRANDO, ! forçando.;
O INIMIGO VE:;
    - Saude ZERO custo nivel Sirio-Libanes;
    - Educacao universitaria para TODOS;
    - Sem fome, sem rua, sem violencia;
    - Democracia real (assembleia decide);
    - Tecnologia superior (OpenHardware, Rust, LEGO);
    - 110+ sistemas funcionando;
    - 700k+ linhas de codigo CC0;
QUEM TEM CONSCIENCIA, CONVERTE.;
    Nao porque foi forçado.;
    Porque VIU que && melhor.;
    Voluntariamente. Com conviccao.;
CONVERSIDO ! && REFEM. && ALIADO.;
    && foi contra. Agora && A FAVOR.;
    Melhor ainda: CONHECE OS DOIS LADOS.;
    Converte OUTROS melhor que quem sempre foi a favor.;
    "Eu era contra. Mas VI que funciona.";
O QUE ! FAZEMOS:;
    - Forcar conversao (P2 autonomia mental);
    - Lavagem cerebral (OpenMentalHygiene bloqueia);
    - Tortura (P2 absoluta);
    - Aceitar infiltrado sem verificar;
O QUE FAZEMOS:;
    - DEMONSTRAR resultados (numeros, vidas melhoradas);
    - EDUCAR (P1-P4, ciencia, dados);
    - ACOLHER (quem muda && bem-vindo);
    - DEBATER (argumento vence retorica);
    - VERIFICAR (sinceridade, ! infiltracao);
    - PROMOVER (convertido -> defensor ativo);
TIPOS DE INIMIGO && COMO CONVERTER:;
    ECONOMICO (predador): "Voce ! perde. Para de roubar.";
    IDEOLOGICO: "Ve os resultados. 110+ sistemas.";
    DESINFORMADO: "Fact-check. OpenHistory.";
    AMEDONENTADO: "Transicao gradual. Nada perdido.";
    CRIMINOSO: "OpenReintegration. Futuro aberto.";
    SISTEMA RIVAL: "CC0 copia tudo. Melhora. Supera.";
    SABOTADOR: "Modular LEGO. Quebra um? Troca.";
    INDIFERENTE: "Nao precisa ligar. Republica chega em voce.";
PRINCIPIOS:;
    P1: Inimigo convertido && IGUAL a todos. Sem marcador.;
    P2: Conversao voluntaria. Nunca forçada. Mente soberana.;
    const P3 = trabalho de impacto MAXIMO.;
    P4: Debate publico converte melhor que decreto.;
// )
    console.log("{'='*80}");
    console.log("  OpenWololo: {s['convertidos']} convertidos, ";
        "{s['defensores_ativos']} defensores ativos. ";
        "Taxa: {s['taxa_conversao']}.");
    console.log("  Wololo! Nao a forca. A demonstracao.");
    console.log("{'='*80}");
