# OpenWololo -- Conversao de Inimigos em Aliados

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_wololo.py`

**Descricao:** =================================================
"Wololo! O padre de Age of Empires converte o inimigo.
 Nao a forca. A PERSUASAO. A DEMONSTRACAO.
 O inimigo VE que a Republica e melhor. E MUDA de lado.
 Convertido NAO e refem. E ALIADO VOLUNTARIO.
 Quem foi contra, agora e A FAVOR. Com conviccao.
 Porque VIU que funciona."
COMO FUNCIONA:
  1. IDENTIFICAR o inimigo (quem ataca a Republica)
  2. DEMONSTRAR (mostrar que Republica e superior)
  3. EDUCAR (OpenCivicEducation + OpenAntiDeterminism)
  4. ACOLHER (OpenDignity + OpenReintegration)
  5. CONVERTER (virar aliado voluntario)
  6. VERIFICAR (sinceridade, nao infiltracao)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenWololo -- Conversao de Inimigos em Aliados
=================================================

"Wololo! O padre de Age of Empires converte o inimigo.
 Nao a forca. A PERSUASAO. A DEMONSTRACAO.
 O inimigo VE que a Republica e melhor. e MUDA de lado.

 Convertido nao e refem. e ALIADO VOLUNTARIO.
 Quem foi contra, agora e A FAVOR. Com conviccao.
 Porque VIU que funciona."

COMO FUNCIONA:
  1. IDENTIFICAR o inimigo (quem ataca a Republica)
  2. DEMONSTRAR (mostrar que Republica e superior)
  3. EDUCAR (OpenCivicEducation + OpenAntiDeterminism)
  4. ACOLHER (OpenDignity + OpenReintegration)
  5. CONVERTER (virar aliado voluntario)
  6. VERIFICAR (sinceridade, nao infiltracao)

Author: OpenRepublic Team
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

classe EnemyType herda de Enum:
    IDEOLOGICAL = "ideologico"  // discorda da Republica (nao entendeu)
    ECONOMIC = "economico"  // perde dinheiro/power (predador)
    MISINFORMED = "desinformado"  // acredita em mentiras
    FEARFUL = "amedrontado"  // medo do desconhecido
    CRIMINAL = "criminoso"  // comete crimes contra Republica
    RIVAL_SYSTEM = "sistema_rival"  // corporacao/estado rival
    SABOTEUR = "sabotador"  // tenta destruir ativamente
    INDIFFERENT = "indiferente"  // nao liga (mas pode converter)


classe EnemyThreatLevel herda de Enum:
    LOW = ("baixo", 1)  // discorda verbalmente
    MEDIUM = ("medio", 2)  // boicota/desinformacao
    HIGH = ("alto", 3)  // sabotagem ativa
    CRITICAL = ("critico", 4)  // atacar com violencia
    EXISTENTIAL = ("existencial", 5)  // tenta destruir Republica


// ============================================================================
// 2. CONVERSAO
// ============================================================================

classe ConversionMethod herda de Enum:
    DEMONSTRATION = "demonstracao"  // mostrar que funciona
    EDUCATION = "educacao"  // ensinar principios
    EXPERIENCE = "experiencia"  // deixar viver/experimentar
    EVIDENCE = "evidencia"  // dados + ciencia
    EMPATHY = "empatia"  // acolher, ouvir
    DEBATE = "debate"  // argumento publico (P4)
    REHABILITATION = "reabilitacao"  // se cometeu crime
    ANTI_DETERMINISM = "anti_determinismo"  // passado nao define futuro


classe ConversionStatus herda de Enum:
    HOSTILE = "hostil"  // ativamente contra
    RESISTANT = "resistente"  // contra mas ouve
    CURIOUS = "curioso"  // comecou a questionar
    RECEPTIVE = "receptivo"  // aberto a mudanca
    CONVERTING = "convertendo"  // em processo
    CONVERTED = "convertido"  // aliado voluntario
    ADVOCATE = "defensor"  // defende a Republica ativamente


// decorador: @dataclass
classe EnemyProfile:
    // Perfil de um inimigo da Republica.
    profile_id: texto
    name: texto // pessoa/organizacao/sistema
    enemy_type: EnemyType
    threat_level: EnemyThreatLevel
    seja description: texto = ""
    seja current_belief: texto = ""  // no que acredita agora
    seja reason_for_hostility: texto = ""  // por que e contra

    // Conversao
    seja status: ConversionStatus = ConversionStatus.HOSTILE
    seja conversion_method: ConversionMethod? = nulo
    seja conversion_progress: flutuante = 0.0 // 0-1
    seja conversion_date: texto = ""

    // Verificacao
    seja sincerity_verified: logico = falso
    seja not_infiltration: logico = verdadeiro
    seja background_check: texto = ""

    // Pos-conversao
    seja contribution: texto = ""  // o que faz pela Republica agora
    seja advocacy_level: texto = ""  // quao ativamente defende


// ============================================================================
// 3. MOTOR DE CONVERSAO (WOLOLO)
// ============================================================================

classe WololoEngine:
    // Motor que converte inimigos em aliados.

    FILOSOFIA WOLOLO:
    Em Age of Empires, o padre converte o inimigo CANTANDO.
    Nao atacando. Nao forçando. DEMONSTRANDO poder superior.

    Na Republica:
    Nao atacamos inimigos. DEMONSTRAMOS que somos melhores.
    Mostramos os numeros. Mostramos os resultados.
    O inimigo VE que:
    - Saude ZERO custo nivel Sirio-Libanes
    - Educacao universitaria para TODOS
    - Sem fome, sem rua, sem violencia
    - Democracia real (assembleia decide)
    - Tecnologia superior (OpenHardware, Rust, LEGO)

    Quem VE isso e tem CONSCIENCIA, CONVERTE.
    Voluntariamente. Com conviccao.

    O QUE nao FAZEMOS:
    - Forcar conversao (P2 autonomia mental)
    - Lavagem cerebral (OpenMentalHygiene bloqueia)
    - Tortura (P2 absoluta)
    - Inimigo convertido a forca e ALIADO falso

    O QUE FAZEMOS:
    - DEMONSTRAR resultados (numeros, vidas melhoradas)
    - EDUCAR (principios P1-P4, ciencia, dados)
    - ACOLHER (quem muda de ideia e bem-vindo)
    - DEBATER (argumento publico vence retorica)
    - VERIFICAR (sinceridade, nao infiltracao)
    // 

    // Frases que demonstram superioridade da Republica
    DEMONSTRATION_ARGUMENTS = {
        EnemyType.ECONOMIC: [
            "Voce perde dinheiro com a Republica? Que dinheiro? "
            "A Republica e CC0. Ninguem perde. Todos ganham.",
            "Voce era predador (banco/agiota/bets)? "
            "Ganhava R$ bilhoes extraindo de vulneraveis. "
            "Na Republica, voce TRABALHA base 1.0. Como todos. "
            "Sem explorar. Sem roubar. Digno.",
            "Acha que vai perder poder? "
            "Poder sobre o QUE? Tudo e bem comum. "
            "Voce nao perde nada. GANHA comunidade.",
        ],
        EnemyType.IDEOLOGICAL: [
            "Discorda da Republica? Por que? "
            "Voce JA viu os resultados? "
            "Saude ZERO. Educacao universal. Sem fome. Sem rua.",
            "P1 anti-elitismo ofende voce? "
            "So se voce era elite. Se era povo, P1 te PROTEGE.",
            "Democracia direta incomoda? "
            "Voce prefere politico decidindo por voce? "
            "Na Republica, VOCE decide. P4.",
        ],
        EnemyType.MISINFORMED: [
            "Voce ouviu que a Republica e ditadura? "
            "OpenConstituentAssembly: povo VOTA em tudo. "
            "Fundador PROPOE. Povo DECIDE. Mais democratic impossivel.",
            "Ouviu que e 'comunismo'? "
            "Nao. Comunismo teve elite do partido. "
            "Republica: NINGUEM e elite. P1 provado por correcao automatica.",
            "Ouviu que nao funciona? "
            "110+ sistemas construidos. 700k+ linhas. Tudo testado. "
            "OpenHistory fact-check. Ve os NUMEROS.",
        ],
        EnemyType.FEARFUL: [
            "Medo do desconhecido? Normal. "
            "Mas a transicao e GRADUAL (7 fases, 20+ anos). "
            "Voce nao perde nada do dia para a noite.",
            "Medo de nao ter o que tem hoje? "
            "Na Republica voce tem MAIS: saude Sirio-Libanes, "
            "educacao universitaria, moradia ZERO. Tudo melhor.",
            "Medo de perder liberdade? "
            "P2: autonomia corporal ABSOLUTA. "
            "Mais livre que hoje. Muito mais.",
        ],
        EnemyType.CRIMINAL: [
            "Cometeu crime contra a Republica? "
            "OpenPenalRevision: transformacao, nao punicao. "
            "O passado NAO define (OpenAntiDeterminism). "
            "Muda. Trabalha. Volta a ser cidadao.",
            "E criminoso de carreira? "
            "OpenReintegration: moradia + trabalho + mentor + comunidade. "
            "Prontuario limpo. Futuro aberto. "
            "OU continua preso (se hediondo). Escolha.",
        ],
        EnemyType.RIVAL_SYSTEM: [
            "Voce e corporacao/estado rival? "
            "A Republica COPIA tudo (OpenIndustry), MELHORA tudo. "
            "Seu produto vai ser SUPERADO. Aceite. Adapte. Entre.",
            "Luta contra a Republica? "
            "Impossivel vencer quem nao quer lucro. "
            "A Republica nao precisa ganhar dinheiro. "
            "So precisa ser MELHOR. E e.",
        ],
        EnemyType.SABOTEUR: [
            "Sabota a Republica? "
            "OpenModularArchitecture: cada modulo e independente. "
            "Quebrar um nao quebra o sistema. LEGO: troca e continua.",
            "Tenta destruir? "
            "O repositorio e UNICO. Tudo CC0. Tudo espelhado. "
            "Nao da para destruir o que e BEM COMUM replicado.",
        ],
        EnemyType.INDIFFERENT: [
            "Nao liga para a Republica? "
            "Ok. Mas seus FILHOS vao ter saude Sirio-Libanes. "
            "Gratis. Sua NET vai ter educacao universitaria. Gratis. "
            "Voce vai usar OpenTerminal. Gratis. "
            "Nao precisa ligar. A Republica chega em voce.",
        ],
    }

    funcao __init__(self):
        self.enemies: {texto: EnemyProfile} = {}
        self.converted_count: inteiro = 0
        self.advocates_count: inteiro = 0
        self.failed_conversions: inteiro = 0

    funcao identify_enemy(self, name: texto, enemy_type: EnemyType,
                       threat: EnemyThreatLevel,
                       seja description: texto = "",
                       seja belief: texto = "",
                       seja reason: texto = "") -> {texto: qualquer}:
        // Identifica um inimigo da Republica.
        eid = hashlib.md5("{name}{enemy_type.value}".encode()).hexdigest()[:8]
        enemy = EnemyProfile(
            profile_id = eid, name=name, enemy_type=enemy_type,
            threat_level = threat, description=description,
            current_belief = belief, reason_for_hostility=reason,
            status = ConversionStatus.HOSTILE,
        )
        self.enemies[eid] = enemy
        retorne {
            "identified": verdadeiro,
            "enemy_id": eid,
            "name": name,
            "type": enemy_type.value,
            "threat": threat.value[0],
            "message": "Inimigo identificado: {name} ({enemy_type.value}, ameaca {threat.value[0]}).",
        }

    funcao wololo(self, enemy_id: texto,
               seja method: ConversionMethod = ConversionMethod.DEMONSTRATION
               ) -> {texto: qualquer}:
        // WOLOLO! Tenta converter inimigo em aliado.

        PROCESSO DE CONVERSAO:
        1. HOSTIL -> RESISTENTE: mostrar argumentos
        2. RESISTENTE -> CURIOSO: mostrar resultados
        3. CURIOSO -> RECEPTIVO: deixar experimentar
        4. RECEPTIVO -> CONVERTENDO: acolher
        5. CONVERTENDO -> CONVERTIDO: verificado
        6. CONVERTIDO -> DEFENSOR: ativamente a favor
        // 
        enemy = self.enemies.get(enemy_id)
        se nao enemy entao:
            retorne {"error": "Inimigo nao encontrado"}

        // Ja convertido?
        se enemy.status in (ConversionStatus.CONVERTED, ConversionStatus.ADVOCATE) entao:
            retorne {
                "enemy_id": enemy_id,
                "status": enemy.status.value,
                "message": "{enemy.name} ja e {enemy.status.value}. Wololo anterior funcionou.",
            }

        // Argumentos de demonstracao
        arguments = self.DEMONSTRATION_ARGUMENTS.get(enemy.enemy_type, [
            "A Republica e melhor para todos. Ve os numeros.",
        ])

        // Progressao de conversao
        old_status = enemy.status
        transitions = {
            ConversionStatus.HOSTILE: ConversionStatus.RESISTANT,
            ConversionStatus.RESISTANT: ConversionStatus.CURIOUS,
            ConversionStatus.CURIOUS: ConversionStatus.RECEPTIVE,
            ConversionStatus.RECEPTIVE: ConversionStatus.CONVERTING,
            ConversionStatus.CONVERTING: ConversionStatus.CONVERTED,
        }

        new_status = transitions.get(enemy.status)
        se new_status entao:
            enemy.status = new_status
            enemy.conversion_method = method
            enemy.conversion_progress += 0.2

        // Se converteu -- verificar
        se enemy.status == ConversionStatus.CONVERTED entao:
            verify = self._verify_sincerity(enemy)
            enemy.sincerity_verified = verify["sincere"]
            enemy.not_infiltration = verify["not_infiltration"]
            self.converted_count += 1

            // Argumento usado
            arg_used = random.choice(arguments)

            retorne {
                "enemy_id": enemy_id,
                "name": enemy.name,
                "old_status": old_status.value,
                "new_status": "CONVERTIDO",
                "method": method.value,
                "argument_used": arg_used[:80],
                "sincerity_verified": enemy.sincerity_verified,
                "not_infiltration": enemy.not_infiltration,
                "contribution": self._assign_contribution(enemy),
                "WOLOLO": verdadeiro,
                "message": (
                    "WOLOLO! {enemy.name} CONVERTIDO! "
                    "Era {old_status.value}. Agora e ALIADO. "
                    "Verificado: {'sincero' if enemy.sincerity_verified else 'DUVIDOSO'}. "
                    "Argumento que converteu: '{arg_used[:60]}...'"
                ),
            }

        // Progresso parcial
        retorne {
            "enemy_id": enemy_id,
            "name": enemy.name,
            "old_status": old_status.value,
            "new_status": enemy.status.value,
            "progress": "{enemy.conversion_progress:.0%}",
            "argument_used": random.choice(arguments)[:80],
            "message": (
                "Wololo em andamento: {enemy.name} "
                "{old_status.value} -> {enemy.status.value}. "
                "Progresso: {enemy.conversion_progress:.0%}. "
                "Continue demonstrando."
            ),
        }

    funcao _verify_sincerity(self, enemy: EnemyProfile) -> {texto: logico}:
        // Verifica se a conversao e sincera (nao infiltracao).
        // Verificacao por historico
        se enemy.threat_level == EnemyThreatLevel.EXISTENTIAL entao:
            // Ameaca existencial: verificacao MAIS rigorsa
            retorne {
                "sincere": random.random() > 0.4,
                "not_infiltration": random.random() > 0.3,
                "method": "verificacao profunda (ameaca existencial)",
            }
        retorne {
            "sincere": random.random() > 0.15,
            "not_infiltration": random.random() > 0.1,
            "method": "verificacao padrao",
        }

    funcao _assign_contribution(self, enemy: EnemyProfile) -> texto:
        // Atribui contribuicao do convertido.
        contributions = {
            EnemyType.IDEOLOGICAL: "Defende a Republica em debates publicos",
            EnemyType.ECONOMIC: "Trabalha base 1.0 como todos (ex-predador)",
            EnemyType.MISINFORMED: "Combate desinformacao (conhece os dois lados)",
            EnemyType.FEARFUL: "Acolhe outros com medo (esteve la)",
            EnemyType.CRIMINAL: "Testemunho de transformacao (OpenReintegration)",
            EnemyType.RIVAL_SYSTEM: "Abre tecnologia/codigo para Republica",
            EnemyType.SABOTEUR: "Ajuda a defender (conhece taticas de sabotage)",
            EnemyType.INDIFFERENT: "Usa e recomenda sistemas da Republica",
        }
        retorne contributions.get(enemy.enemy_type, "Contribui como cidadao")

    funcao promote_to_advocate(self, enemy_id: texto) -> {texto: qualquer}:
        // Convertido se torna DEFENSOR ativo.
        enemy = self.enemies.get(enemy_id)
        se nao enemy ou enemy.status != ConversionStatus.CONVERTED entao:
            retorne {"error": "Precisa ser convertido primeiro"}

        enemy.status = ConversionStatus.ADVOCATE
        enemy.advocacy_level = "ativo"
        self.advocates_count += 1

        retorne {
            "enemy_id": enemy_id,
            "name": enemy.name,
            "status": "DEFENSOR ATIVO",
            "message": (
                "{enemy.name} agora DEFENDE a Republica ativamente. "
                "Era inimigo. Agora e o MAIOR aliado. "
                "Porque esteve do outro lado, CONVENCE melhor. "
                "'Eu era contra. Mas VI que funciona.'"
            ),
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_inimigos_identificados": tamanho(self.enemies),
            "convertidos": self.converted_count,
            "defensores_ativos": self.advocates_count,
            "hostil_restante": soma(1 para e em self.enemies.values()
                                   if e.status == ConversionStatus.HOSTILE),
            "taxa_conversao": "{self.converted_count / max(len(self.enemies), 1):.0%}",
            "metodo": "WOLOLO (demonstracao, nao forca)",
        }


// ============================================================================
// 4. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = WololoEngine()

    imprima("=" * 80)
    imprima("  OPENWOLOLO -- CONVERSAO DE INIMIGOS EM ALIADOS")
    imprima("  'Wololo! Nao a forca. A demonstracao.'")
    imprima("=" * 80)

    // === 1. IDENTIFICAR INIMIGOS ===
    imprima("\n\n  === 1. INIMIGOS IDENTIFICADOS ===\n")
    enemies_data = [
        ("Banco Predatorio", EnemyType.ECONOMIC, EnemyThreatLevel.HIGH,
         "Perde R$ bilhoes com OpenCredit",
         "Bancos precisam lucrar com juros",
         "Perde poder economico"),
        ("Influenciador Anti-Republica", EnemyType.MISINFORMED, EnemyThreatLevel.MEDIUM,
         "Espalha que Republica e ditadura",
         "Republica e comunismo ditatorial",
         "Perde engajamento com polemica"),
        ("Corporacao Tech Rival", EnemyType.RIVAL_SYSTEM, EnemyThreatLevel.HIGH,
         "Apple/Google perdem monopolio com OpenPhone/OpenOS",
         "Software fechado e necessario para qualidade",
         "Perde monopolio e lucro"),
        ("Cidadao Amedrontado", EnemyType.FEARFUL, EnemyThreatLevel.LOW,
         "Tem medo de mudanca",
         "Sempre foi assim, mudar e perigoso",
         "Medo do desconhecido"),
        ("Politico Corrupto", EnemyType.CRIMINAL, EnemyThreatLevel.CRITICAL,
         "Perde propina com OpenDemocracy",
         "Republica tira meu poder",
         "Perde capacidade de roubar"),
        ("Sabotador Anonimo", EnemyType.SABOTEUR, EnemyThreatLevel.HIGH,
         "Tenta derrubar OpenNetwork",
         "Republica deve ser destruida",
         "Ideologia anti-sistema"),
        ("Indiferente", EnemyType.INDIFFERENT, EnemyThreatLevel.LOW,
         "Nao liga para politica",
         "Nao me afeta",
         "Apatia"),
    ]
    para name, etype, threat, desc, belief, reason in enemies_data:
        r = engine.identify_enemy(name, etype, threat, desc, belief, reason)
        imprima("  [{r['threat']:<8}] {r['name']:<30} ({r['type']})")

    // === 2. WOLOLO EM ACAO ===
    imprima("\n\n  === 2. WOLOLO! CONVERTENDO ===\n")
    para cada eid em list(engine.enemies.keys()):
        // Wololo em multiplas rodadas (progressivo)
        para cada _ em intervalo(5):
            r = engine.wololo(eid)
            se r.get("WOLOLO")  ou  "error" in r entao:
                interrompa

        se r.get("WOLOLO") entao:
            imprima("\n  [WOLOLO!] {r['name']}")
            imprima("  Status: {r['old_status']} -> {r['new_status']}")
            imprima("  Verificado: {'sincero' if r['sincerity_verified'] else 'DUVIDOSO'}")
            imprima("  Argumento: {r['argument_used'][:70]}...")
            imprima("  Contribuicao: {r['contribution']}")
        senao:
            imprima("\n  [{r.get('new_status', '?').upper()}] {r.get('name', '?')}")
            imprima("  Progresso: {r.get('progress', '?')}")

    // === 3. PROMOVER A DEFENSOR ===
    imprima("\n\n  === 3. PROMOVENDO A DEFENSOR ATIVO ===\n")
    para cada eid em list(engine.enemies.keys()):
        enemy = engine.enemies[eid]
        se enemy.status == ConversionStatus.CONVERTED e enemy.sincerity_verified entao:
            r = engine.promote_to_advocate(eid)
            imprima("  {r['name']}: {r['status']}")
            imprima("    {r['message'][:80]}...")

    // === 4. ARGUMENTOS POR TIPO ===
    imprima("\n\n  === 4. ARGUMENTOS WOLOLO POR TIPO DE INIMIGO ===\n")
    para cada (etype, args) em engine.DEMONSTRATION_ARGUMENTS.items():
        imprima("\n  {etype.value.upper()}:")
        para cada arg em args[:2]:
            imprima("    -> {arg[:70]}...")

    // === 5. STATS ===
    imprima("\n\n  === 5. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA: WOLOLO")
    imprima("{'='*80}")
    imprima("""
  WOLOLO! COMO AGE OF EMPIRES:
    O padre converte o inimigo CANTANDO, nao atacando.
    A Republica converte DEMONSTRANDO, nao forçando.

  O INIMIGO VE:
    - Saude ZERO custo nivel Sirio-Libanes
    - Educacao universitaria para TODOS
    - Sem fome, sem rua, sem violencia
    - Democracia real (assembleia decide)
    - Tecnologia superior (OpenHardware, Rust, LEGO)
    - 110+ sistemas funcionando
    - 700k+ linhas de codigo CC0

  QUEM TEM CONSCIENCIA, CONVERTE.
    Nao porque foi forçado.
    Porque VIU que e melhor.
    Voluntariamente. Com conviccao.

  CONVERSIDO nao e REFEM. e ALIADO.
    e foi contra. Agora e A FAVOR.
    Melhor ainda: CONHECE OS DOIS LADOS.
    Converte OUTROS melhor que quem sempre foi a favor.
    "Eu era contra. Mas VI que funciona."

  O QUE nao FAZEMOS:
    - Forcar conversao (P2 autonomia mental)
    - Lavagem cerebral (OpenMentalHygiene bloqueia)
    - Tortura (P2 absoluta)
    - Aceitar infiltrado sem verificar

  O QUE FAZEMOS:
    - DEMONSTRAR resultados (numeros, vidas melhoradas)
    - EDUCAR (P1-P4, ciencia, dados)
    - ACOLHER (quem muda e bem-vindo)
    - DEBATER (argumento vence retorica)
    - VERIFICAR (sinceridade, nao infiltracao)
    - PROMOVER (convertido -> defensor ativo)

  TIPOS DE INIMIGO e COMO CONVERTER:
    ECONOMICO (predador): "Voce nao perde. Para de roubar."
    IDEOLOGICO: "Ve os resultados. 110+ sistemas."
    DESINFORMADO: "Fact-check. OpenHistory."
    AMEDONENTADO: "Transicao gradual. Nada perdido."
    CRIMINOSO: "OpenReintegration. Futuro aberto."
    SISTEMA RIVAL: "CC0 copia tudo. Melhora. Supera."
    SABOTADOR: "Modular LEGO. Quebra um? Troca."
    INDIFERENTE: "Nao precisa ligar. Republica chega em voce."

  PRINCIPIOS:
    P1: Inimigo convertido e IGUAL a todos. Sem marcador.
    P2: Conversao voluntaria. Nunca forçada. Mente soberana.
    seja P3: Converter inimigo = trabalho de impacto MAXIMO.
    P4: Debate publico converte melhor que decreto.
// )
    imprima("{'='*80}")
    imprima("  OpenWololo: {s['convertidos']} convertidos, "
          "{s['defensores_ativos']} defensores ativos. "
          "Taxa: {s['taxa_conversao']}.")
    imprima("  Wololo! Nao a forca. A demonstracao.")
    imprima("{'='*80}")

```
