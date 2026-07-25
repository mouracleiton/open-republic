# OpenTransition -- Transicao do Sistema Atual para a OpenRepublic

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_transition.py`

**Descricao:** ==================================================================
"A Republica nao nasce de um golpe. Nasce de uma TRANSICAO.
 Pessoas precisam tempo para mudar. Infraestrutura precisa ser construida.
 Dinheiro precisa perder sentido gradualmente. Propriedade precisa dissolver.
 Mas a direcao e CLARA: Republica completa."
O QUE ISTO FAZ:
  1. MAPEIA o estado atual (capitalismo, dinheiro, propriedade, desigualdade)
  2. DEFINE fases de transicao (gradual, nao abrupta)
  3. GERE migracao de cada sistema (saude, educacao, trabalho, etc)
  4. MEDe progresso (metricas de transicao)
  5. GERE resistencia (pessoas que nao querem mudar)
  6. GARANTE que ningém morre na transicao
AS 7 FASES DA TRANSICAO:
  FASE 0 -- CONSTRUCAO (ja acontecendo)
    Os 110+ sistemas da Republica sao construidos e testados.
    Codigo existe. Modelos existem. Ideia existe.
    ESTAMOS AQUI.
  FASE 1 -- ADOCAO VOLUNTARIA (pequenos grupos)
    Comunidades pequenas adotam sistemas da Republica.
    OpenTerminal instalado. OpenCredit testado. OpenHealth usado.
    Ninguem e obrigado. Grupos se formam organicamente.
  FASE 2 -- INFRAESTRUTURA PARALELA
    OpenNetwork construido. FabLabs abertos. OpenHealth em postos.
    OpenUniversity disponivel online. OpenMobility em testes.
    Sistema da Republica funciona PARALELAMENTE ao capitalismo.
  FASE 3 -- DUPLA CIRCULACAO
    Dinheiro e OpenCredit circulam juntos.
    Pessoas podem trabalhar no sistema antigo OU na Republica.
    Escolha gradual. Sem trauma.
  FASE 4 -- MIGRACAO EM MASSA
    Maioria da populacao usa sistemas da Republica.
    Dinheiro perde relevancia. Propriedade perde sentido.
    Escolas publicas viram OpenSchool. Hospitais viram OpenHealth.
  FASE 5 -- DESCOMISSIONAMENTO
    Sistema antigo e desligado gradualmente.
    Bancos fecham. Corporacoes dissolvem.
    Propriedade privada transferida para bem comum.
  FASE 6 -- REPUBLICA COMPLETA
    100% dos sistemas operacionais.
    Dinheiro: extinto. Propriedade: extinta.
    Trabalho: base 1.0. Saude: Sirio-Libanes para todos.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenTransition -- Transicao do Sistema Atual para a OpenRepublic
==================================================================

"A Republica nao nasce de um golpe. Nasce de uma TRANSICAO.
 Pessoas precisam tempo para mudar. Infraestrutura precisa ser construida.
 Dinheiro precisa perder sentido gradualmente. Propriedade precisa dissolver.
 Mas a direcao e CLARA: Republica completa."

O QUE ISTO FAZ:
  1. MAPEIA o estado atual (capitalismo, dinheiro, propriedade, desigualdade)
  2. DEFINE fases de transicao (gradual, nao abrupta)
  3. GERE migracao de cada sistema (saude, educacao, trabalho, etc)
  4. MEDe progresso (metricas de transicao)
  5. GERE resistencia (pessoas que nao querem mudar)
  6. GARANTE que ningém morre na transicao

AS 7 FASES DA TRANSICAO:

  FASE 0 -- CONSTRUCAO (ja acontecendo)
    Os 110+ sistemas da Republica sao construidos e testados.
    Codigo existe. Modelos existem. Ideia existe.
    ESTAMOS AQUI.

  FASE 1 -- ADOCAO VOLUNTARIA (pequenos grupos)
    Comunidades pequenas adotam sistemas da Republica.
    OpenTerminal instalado. OpenCredit testado. OpenHealth usado.
    Ninguem e obrigado. Grupos se formam organicamente.

  FASE 2 -- INFRAESTRUTURA PARALELA
    OpenNetwork construido. FabLabs abertos. OpenHealth em postos.
    OpenUniversity disponivel online. OpenMobility em testes.
    Sistema da Republica funciona PARALELAMENTE ao capitalismo.

  FASE 3 -- DUPLA CIRCULACAO
    Dinheiro e OpenCredit circulam juntos.
    Pessoas podem trabalhar no sistema antigo ou na Republica.
    Escolha gradual. Sem trauma.

  FASE 4 -- MIGRACAO EM MASSA
    Maioria da populacao usa sistemas da Republica.
    Dinheiro perde relevancia. Propriedade perde sentido.
    Escolas publicas viram OpenSchool. Hospitais viram OpenHealth.

  FASE 5 -- DESCOMISSIONAMENTO
    Sistema antigo e desligado gradualmente.
    Bancos fecham. Corporacoes dissolvem.
    Propriedade privada transferida para bem comum.

  FASE 6 -- REPUBLICA COMPLETA
    100% dos sistemas operacionais.
    Dinheiro: extinto. Propriedade: extinta.
    Trabalho: base 1.0. Saude: Sirio-Libanes para todos.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime


// ============================================================================
// 1. FASES DA TRANSICAO
// ============================================================================

classe TransitionPhase herda de Enum:
    CONSTRUCTION = (0, "Construcao", "Sistemas sendo construidos")
    VOLUNTARY = (1, "Adocao Voluntaria", "Pequenos grupos testam")
    PARALLEL = (2, "Infraestrutura Paralela", "Republica funciona ao lado do capitalismo")
    DUAL = (3, "Dupla Circulacao", "Dinheiro + Credito coexistem")
    MASS = (4, "Migracao em Massa", "Maioria usa sistema da Republica")
    DECOMMISION = (5, "Descomissionamento", "Sistema antigo desligado")
    COMPLETE = (6, "Republica Completa", "100% operacional")


classe SystemMigration herda de Enum:
    // Cada sistema do mundo atual que precisa migrar.
    MONEY = "dinheiro"  // R$/US$ -> OpenCredit
    BANKING = "bancos"  // bancos -> OpenCredit
    PROPERTY = "propriedade"  // titulo -> bem comum CC0
    HEALTH = "saude"  // planos/SUS -> OpenHealth
    EDUCATION = "educacao"  // escolas/faculdades -> OpenSchool/University
    LABOR = "trabalho"  // emprego/CLT -> OpenLaborRelay
    HOUSING = "moradia"  // aluguel/compra -> OpenCivilConstruction
    FOOD = "alimentacao"  // mercado/compra -> OpenAgrarian + OpenCredit
    TRANSPORT = "transporte"  // uber/onibus -> OpenMobility
    ENERGY = "energia"  // conta de luz -> OpenEnergy
    COMMUNICATION = "comunicacao"  // operadora -> OpenNetwork
    MEDIA = "midia"  // TV aberta -> OpenTV
    INTERNET = "internet"  // provedor -> OpenProtocol
    JUSTICE = "justica"  // tribunal -> OpenPenalRevision
    POLITICS = "politica"  // eleicoes -> OpenDemocracy
    CORPORATIONS = "corporacoes"  // empresas -> cooperativas/OpenLaborRelay
    INSURANCE = "seguros"  // seguro -> garantia da Republica
    TAXES = "impostos"  // imposto -> trabalho base 1.0
    RETAIL = "comercio"  // lojas -> OpenMarketplace + troca
    PRISONS = "prisoes"  // presidio -> OpenPenalRevision + OpenReintegration


classe MigrationStatus herda de Enum:
    NOT_STARTED = "nao_iniciado"
    PLANNING = "planejamento"
    PILOT = "piloto"  // teste em pequena escala
    EARLY = "inicio"  // comecando em larga escala
    ADVANCED = "avancado"  // maioria migrou
    NEAR_COMPLETE = "quase_completo"
    COMPLETE = "completo"


// ============================================================================
// 2. SISTEMA SENDO MIGRADO
// ============================================================================

// decorador: @dataclass
classe MigrationTrack:
    // Um sistema do mundo atual sendo migrado para a Republica.
    track_id: texto
    system: SystemMigration
    seja current_status: MigrationStatus = MigrationStatus.NOT_STARTED
    seja target_status: MigrationStatus = MigrationStatus.COMPLETE
    seja current_phase: inteiro = 0 // fase de transicao atual (0-6)

    // Populacao
    seja population_total: inteiro = 0 // populacao afetada
    seja population_migrated: inteiro = 0 // ja usando sistema da Republica
    seja population_resisting: inteiro = 0 // resiste a migracao

    // Infraestrutura
    seja infrastructure_built: flutuante = 0.0 // 0-1
    seja infrastructure_needed: flutuante = 1.0

    // Metricas
    seja old_system_cost: flutuante = 0.0 // custo do sistema antigo (R$/ano)
    seja new_system_cost: flutuante = 0.0 // custo da Republica (ZERO)
    seja people_benefited: inteiro = 0

    // Riscos
    seja risks: [texto] = field(default_factory=list)
    seja mitigation: [texto] = field(default_factory=list)

    // Dependencies
    seja depends_on: [texto] = field(default_factory=list)
    seja blocks: [texto] = field(default_factory=list) // outros sistemas que este bloqueia

    // decorador: @property
    funcao migration_pct(self) -> flutuante:
        se self.population_total == 0 entao:
            retorne 0.0
        retorne self.population_migrated / self.population_total

    // decorador: @property
    funcao readiness(self) -> flutuante:
        // Quao pronto este sistema esta para migrar.
        infra = self.infrastructure_built / maximo(self.infrastructure_needed, 0.01)
        pop = self.migration_pct
        retorne arredonde((infra + pop) / 2, 2)


// ============================================================================
// 3. GESTAO DE RESISTENCIA
// ============================================================================

classe ResistanceType herda de Enum:
    FINANCIAL = "financeira"  // perde dinheiro/power com mudanca
    IDEOLOGICAL = "ideologica"  // nao acredita na Republica
    FEAR = "medo"  // medo do desconhecido
    HABIT = "habito"  // sempre foi assim
    MISINFORMATION = "desinformacao"  // mentiras sobre a Republica
    LEGITIMATE = "legitima"  // preocupacao real e valida


// decorador: @dataclass
classe ResistanceCase:
    // Caso de resistencia a transicao.
    case_id: texto
    group: texto // quem resiste
    resistance_type: ResistanceType
    concern: texto // o que preocupam
    seja response: texto = ""  // como a Republica responde
    seja resolved: logico = falso


// ============================================================================
// 4. MOTOR DE TRANSICAO
// ============================================================================

classe TransitionEngine:
    // Motor que gerencia a transicao do capitalismo para a Republica.

    PRINCIPIOS DA TRANSICAO:
    1. GRADUAL: ninguem e jogado no desconhecido
    2. VOLUNTARIA: adocao por escolha, nao por forca
    3. SEGURA: ningém morre na transicao (P2)
    4. REVERSIVEL: se algo nao funciona, volta
    5. TRANSPARENTE: todos sabem onde estao na transicao
    6. MEDIVEL: metricas claras de progresso
    7. EQUITATIVA: ricos nao escapam; pobres nao prejudicados

    O QUE NUNCA ACONTECE:
    - Confisco violento de propriedade
    - Proibicao de dinheiro do dia para a noite
    - Fechamento de hospitais antes do OpenHealth funcionar
    - Fechamento de escolas antes do OpenSchool funcionar
    - Cortar empregos antes do OpenLaborRelay absorver

    O QUE SEMPRE ACONTECE:
    - Republica CONSTRUI antes de substituir
    - Sistema antigo so DESLIGA quando novo PROVA que funciona
    - Pessoas RECEBEM durante a transicao (ninguem perde acesso)
    - Metricas DECIDEM quando avancar (nao ideologia)
    // 

    funcao __init__(self):
        self.tracks: {texto: MigrationTrack} = {}
        self.resistance: {texto: ResistanceCase} = {}
        self.current_phase: inteiro = 0
        self._init_migration_tracks()

    funcao _init_migration_tracks(self):
        // Inicializa todas as trilhas de migracao.
        tracks_data = [
            ("TR-MONEY", SystemMigration.MONEY, 215000000,
             ["TR-BANKING"], ["TR-PROPERTY", "TR-LABOR", "TR-TAXES"]),
            ("TR-BANKING", SystemMigration.BANKING, 215000000,
             ["TR-MONEY"], []),
            ("TR-PROPERTY", SystemMigration.PROPERTY, 215000000,
             ["TR-MONEY"], ["TR-HOUSING"]),
            ("TR-HEALTH", SystemMigration.HEALTH, 215000000,
             [], []),
            ("TR-EDUCATION", SystemMigration.EDUCATION, 60000000,
             [], []),
            ("TR-LABOR", SystemMigration.LABOR, 110000000,
             ["TR-MONEY"], ["TR-CORPORATIONS", "TR-TAXES"]),
            ("TR-HOUSING", SystemMigration.HOUSING, 215000000,
             ["TR-PROPERTY"], ["TR-DIGNITY"]),
            ("TR-FOOD", SystemMigration.FOOD, 215000000,
             ["TR-MONEY"], []),
            ("TR-TRANSPORT", SystemMigration.TRANSPORT, 215000000,
             [], []),
            ("TR-ENERGY", SystemMigration.ENERGY, 215000000,
             [], []),
            ("TR-COMMUNICATION", SystemMigration.COMMUNICATION, 215000000,
             [], []),
            ("TR-MEDIA", SystemMigration.MEDIA, 215000000,
             ["TR-COMMUNICATION"], []),
            ("TR-INTERNET", SystemMigration.INTERNET, 215000000,
             [], []),
            ("TR-JUSTICE", SystemMigration.JUSTICE, 215000000,
             [], ["TR-PRISONS"]),
            ("TR-POLITICS", SystemMigration.POLITICS, 215000000,
             [], []),
            ("TR-CORPORATIONS", SystemMigration.CORPORATIONS, 50000000,
             ["TR-LABOR"], []),
            ("TR-INSURANCE", SystemMigration.INSURANCE, 215000000,
             ["TR-HEALTH"], []),
            ("TR-TAXES", SystemMigration.TAXES, 215000000,
             ["TR-MONEY", "TR-LABOR"], []),
            ("TR-RETAIL", SystemMigration.RETAIL, 215000000,
             ["TR-MONEY"], []),
            ("TR-PRISONS", SystemMigration.PRISONS, 800000,
             ["TR-JUSTICE"], []),
        ]

        para tid, system, pop, deps, blocks in tracks_data:
            track = MigrationTrack(
                track_id = tid, system=system,
                population_total = pop,
                depends_on = deps, blocks=blocks,
                old_system_cost = self._estimate_old_cost(system),
                new_system_cost = 0.0,
                risks = self._identify_risks(system),
                mitigation = self._plan_mitigation(system),
            )
            self.tracks[tid] = track

    funcao _estimate_old_cost(self, system: SystemMigration) -> flutuante:
        // Estima custo anual do sistema antigo (bilhoes R$).
        costs = {
            SystemMigration.HEALTH: 260.0, // R$ 260 bi/ano
            SystemMigration.EDUCATION: 180.0,
            SystemMigration.HOUSING: 400.0,
            SystemMigration.LABOR: 0, // custo do desemprego
            SystemMigration.JUSTICE: 80.0,
            SystemMigration.PRISONS: 42.0,
            SystemMigration.ENERGY: 150.0,
            SystemMigration.COMMUNICATION: 60.0,
            SystemMigration.BANKING: 200.0, // lucro bancario
            SystemMigration.INSURANCE: 100.0,
            SystemMigration.CORPORATIONS: 500.0, // lucro corporativo
        }
        retorne costs.get(system, 50.0)

    funcao _identify_risks(self, system: SystemMigration) -> [texto]:
        risks = {
            SystemMigration.MONEY: [
                "Pessoas com poupanca podem perder poder de compra",
                "Comercio pode resistir a aceitar credito",
                "Bancos podem sabotar transicao",
            ],
            SystemMigration.HEALTH: [
                "Medicos podem resistir a perder honorario",
                "Industria farmaceutica pode sabotar",
                "Transicao nao pode interromper tratamentos",
            ],
            SystemMigration.EDUCATION: [
                "Professores podem resistir a novo modelo",
                "Pais podem temer 'experimento' nos filhos",
                "Universidades privadas podem processar",
            ],
            SystemMigration.HOUSING: [
                "Proprietarios podem resistir a perder aluguel",
                "Construtoras podem sabotar OpenCivilConstruction",
                "Pessoas podem temer perder 'seu' imovel",
            ],
            SystemMigration.LABOR: [
                "Empresarios resistem a perder controle",
                "Trabalhadores podem temer instabilidade",
                "Sindicatos podem resistir a novo modelo",
            ],
            SystemMigration.CORPORATIONS: [
                "Empresas grandes resistem (perdem lucro)",
                "Acionistas processam",
                "Media corporativa faz campanha contra",
            ],
        }
        retorne risks.get(system, ["Resistencia geral a mudanca"])

    funcao _plan_mitigation(self, system: SystemMigration) -> [texto]:
        retorne [
            "Construir Republica ANTES de desligar sistema antigo",
            "Garantir que NINGUEM perde acesso durante transicao",
            "Educacao continua sobre beneficios da Republica",
            "Metricas claras: so avanca quando prova que funciona",
            "Pilotos em pequena escala antes de larga escala",
        ]

    funcao assess_phase(self) -> {texto: qualquer}:
        // Avalia em que fase da transicao estamos.
        phase_data = {
            0: {
                "name": "FASE 0: CONSTRUCAO",
                "description": "Sistemas sendo construidos. Codigo existe.",
                "criteria": "110+ sistemas construidos. Testados. Funcionando.",
                "status": "COMPLETO (110+ sistemas, 660k+ linhas)",
            },
            1: {
                "name": "FASE 1: ADOCAO VOLUNTARIA",
                "description": "Comunidades pequenas testam sistemas da Republica.",
                "criteria": "Pelo menos 1 comunidade usando OpenCredit + OpenHealth + OpenTerminal",
                "status": "NAO INICIADO",
            },
            2: {
                "name": "FASE 2: INFRAESTRUTURA PARALELA",
                "description": "Republica funciona ao lado do capitalismo.",
                "criteria": "OpenNetwork + FabLabs + OpenHealth em postos",
                "status": "NAO INICIADO",
            },
            3: {
                "name": "FASE 3: DUPLA CIRCULACAO",
                "description": "Dinheiro e Credito coexistem.",
                "criteria": "30%+ da populacao usando OpenCredit",
                "status": "NAO INICIADO",
            },
            4: {
                "name": "FASE 4: MIGRACAO EM MASSA",
                "description": "Maioria usa sistema da Republica.",
                "criteria": "60%+ migrou para cada sistema",
                "status": "NAO INICIADO",
            },
            5: {
                "name": "FASE 5: DESCOMISSIONAMENTO",
                "description": "Sistema antigo desligado gradualmente.",
                "criteria": "90%+ migrou. Sistema antigo e obsoleto.",
                "status": "NAO INICIADO",
            },
            6: {
                "name": "FASE 6: REPUBLICA COMPLETA",
                "description": "100% operacional. Dinheiro extinto.",
                "criteria": "100% migrou. Dinheiro: 0. Propriedade: 0.",
                "status": "NAO INICIADO",
            },
        }
        retorne phase_data

    funcao track_progress(self, track_id: texto,
                       seja migrated: inteiro = nulo,
                       seja infra_built: flutuante = nulo) -> {texto: qualquer}:
        // Atualiza progresso de uma trilha de migracao.
        track = self.tracks.get(track_id)
        se nao track entao:
            retorne {"error": "Trilha nao encontrada"}

        se migrated e nao None entao:
            track.population_migrated = migrated
        se infra_built e nao None entao:
            track.infrastructure_built = infra_built

        // Atualizar status baseado em progresso
        pct = track.migration_pct
        se pct >= 0.99 entao:
            track.current_status = MigrationStatus.COMPLETE
        senao se pct >= 0.90 entao:
            track.current_status = MigrationStatus.NEAR_COMPLETE
        senao se pct >= 0.60 entao:
            track.current_status = MigrationStatus.ADVANCED
        senao se pct >= 0.20 entao:
            track.current_status = MigrationStatus.EARLY
        senao se pct > 0 entao:
            track.current_status = MigrationStatus.PILOT
        senao se track.infrastructure_built > 0 entao:
            track.current_status = MigrationStatus.PLANNING

        retorne {
            "track": track.system.value,
            "status": track.current_status.value,
            "migrated": "{track.population_migrated:,}/{track.population_total:,}",
            "pct": "{pct:.1%}",
            "infrastructure": "{track.infrastructure_built:.0%}",
            "readiness": "{track.readiness:.0%}",
            "old_cost": "R$ {track.old_system_cost:.0f} bi/ano",
            "new_cost": "ZERO",
        }

    funcao register_resistance(self, group: texto,
                            rtype: ResistanceType,
                            concern: texto,
                            seja response: texto = "") -> {texto: qualquer}:
        // Registra caso de resistencia e planeja resposta.
        cid = hashlib.md5("{group}{concern}".encode()).hexdigest()[:8]

        responses = {
            ResistanceType.FINANCIAL: (
                "Republica garante: voce nao perde acesso a NADA. "
                "Pode ate ganhar. Sem aluguel. Sem conta de luz. "
                "Sem plano de saude. Tudo ZERO custo. "
                "O que voce perde e o EXCESSO, nao o necessario."
            ),
            ResistanceType.IDEOLOGICAL: (
                "Voce nao precisa acreditar. So precisa TESTAR. "
                "Use OpenTerminal por 1 dia. Veja se funciona. "
                "A Republica prova com resultados, nao com fe."
            ),
            ResistanceType.FEAR: (
                "Medo e legitimo. Por isso a transicao e GRADUAL. "
                "Voce nao perde nada do dia para a noite. "
                "Sistema antigo so desliga quando novo PROVA que funciona."
            ),
            ResistanceType.HABIT: (
                "Sempre foi assim NAO significa sempre tem que ser. "
                "Escravos 'sempre' foram escravos. Mudou. "
                "Mulheres 'sempre' ficaram em casa. Mudou. "
                "A Republica e a proxima mudanca."
            ),
            ResistanceType.MISINFORMATION: (
                "OpenHistory fact-check. OpenMentalHygiene analisa. "
                "A Republica nao esconde informacao. Transparencia total. "
                "Verifique. Questione. Decida com dados."
            ),
            ResistanceType.LEGITIMATE: (
                "Preocupacao legitima. A Republica ACOLHE. "
                "Assembleia pode ajustar. Parametros sao referencia. "
                "O povo decide. Se algo nao funciona, muda."
            ),
        }

        case = ResistanceCase(
            case_id = cid, group=group, resistance_type=rtype,
            concern = concern, response=response  ou  responses.get(rtype, ""),
        )
        self.resistance[cid] = case

        retorne {
            "case_id": cid,
            "group": group,
            "type": rtype.value,
            "concern": concern,
            "response": case.response,
        }

    funcao critical_path(self) -> [texto]:
        // Calcula caminho critico -- que sistemas DESTEM outros.
        blocking = [(tid, tamanho(t.blocks)) para tid, t in self.tracks.items()
                    if t.blocks]
        blocking.sort(key=(x) -> -x[1])
        retorne [tid para tid, _ in blocking]

    funcao overall_progress(self) -> {texto: qualquer}:
        total_pop = soma(t.population_total para t em self.tracks.values())
        migrated_pop = soma(t.population_migrated para t em self.tracks.values())
        total_old_cost = soma(t.old_system_cost para t em self.tracks.values())
        tracks_complete = soma(1 para t em self.tracks.values()
                              if t.current_status == MigrationStatus.COMPLETE)
        tracks_started = soma(1 para t em self.tracks.values()
                             if t.current_status != MigrationStatus.NOT_STARTED)

        retorne {
            "fase_atual": 0,   // Construcao
            "total_trilhas": tamanho(self.tracks),
            "trilhas_iniciadas": tracks_started,
            "trilhas_completas": tracks_complete,
            "populacao_total": total_pop,
            "populacao_migrada": migrated_pop,
            "migracao_global": "{migrated_pop/max(total_pop,1):.1%}",
            "custo_antigo_total": "R$ {total_old_cost:.0f} bi/ano",
            "custo_republica": "ZERO",
            "economia_anual": "R$ {total_old_cost:.0f} bi/ano",
        }


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = TransitionEngine()

    imprima("=" * 80)
    imprima("  OPENTRANSITION -- DO CAPITALISMO PARA A REPUBLICA")
    imprima("  Transicao gradual, voluntaria, segura e medivel.")
    imprima("=" * 80)

    // === 1. FASES DA TRANSICAO ===
    imprima("\n\n  === 1. AS 7 FASES DA TRANSICAO ===\n")
    phases = engine.assess_phase()
    para cada (phase_num, data) em phases.items():
        marker = phase_num == 0 ? "<<< VOCE ESTA AQUI" : ""
        imprima("\n  {data['name']} {marker}")
        imprima("  {data['description']}")
        imprima("  Criterio: {data['criteria']}")
        imprima("  Status: {data['status']}")

    // === 2. TRILHAS DE MIGRACAO ===
    imprima("\n\n  === 2. TRILHAS DE MIGRACAO ({len(engine.tracks)}) ===\n")
    imprima("  {'Trilha':<18} {'Status':<18} {'Populacao':>12} {'Custo antigo':>15} {'Riscos'}")
    imprima("  {'-'*85}")
    para cada t em engine.tracks.values():
        imprima("  {t.system.value:<18} {t.current_status.value:<18} "
              "{t.population_total:>12,} "
              "R$ {t.old_system_cost:>6.0f} bi  "
              "{len(t.risks)}")

    // === 3. SIMULAR PROGRESSO (FASE 1) ===
    imprima("\n\n  === 3. SIMULACAO: FASE 1 (piloto em 1 comunidade) ===\n")
    pilots = [
        ("TR-HEALTH", 1000, 0.3),
        ("TR-EDUCATION", 500, 0.2),
        ("TR-MONEY", 1000, 0.1),
        ("TR-TERMINAL", 1000, 0.5),
    ]
    // Track pode nao existir -- usar IDs que existem
    pilot_data = [
        ("TR-HEALTH", 1000, 0.3),
        ("TR-EDUCATION", 500, 0.2),
        ("TR-MONEY", 1000, 0.1),
        ("TR-COMMUNICATION", 1000, 0.4),
    ]
    para tid, pop, infra in pilot_data:
        r = engine.track_progress(tid, migrated=pop, infra_built=infra)
        imprima("  {r['track']:<18} {r['status']:<18} {r['pct']:<8} infra: {r['infrastructure']}")

    // === 4. GESTAO DE RESISTENCIA ===
    imprima("\n\n  === 4. GESTAO DE RESISTENCIA ===\n")
    resistance_cases = [
        ("Bancos", ResistanceType.FINANCIAL, "Perdemos lucro com extincao do dinheiro"),
        ("Donos de imoveis", ResistanceType.FINANCIAL, "Perdemos renda de aluguel"),
        ("Industria farmaceutica", ResistanceType.FINANCIAL, "Perdemos venda de remedio"),
        ("Pais preocupados", ResistanceType.FEAR, "Meu filho vai ser cobaia?"),
        ("Trabalhador CLT", ResistanceType.HABIT, "Sempre trabalhei com carteira assinada"),
        ("Cetico", ResistanceType.IDEOLOGICAL, "Isso nunca vai funcionar"),
        ("Preocupado real", ResistanceType.LEGITIMATE, "E se falhar no meio?"),
    ]
    para group, rtype, concern in resistance_cases:
        r = engine.register_resistance(group, rtype, concern)
        imprima("\n  {r['group']:<25} ({r['type']})")
        imprima("  Preocupacao: {r['concern'][:60]}")
        imprima("  Resposta: {r['response'][:80]}...")

    // === 5. CAMINHO CRITICO ===
    imprima("\n\n  === 5. CAMINHO CRITICO (sistemas que destem outros) ===\n")
    critical = engine.critical_path()
    para cada tid em critical[:8]:
        t = engine.tracks[tid]
        imprima("  {t.system.value:<18} bloqueia: {', '.join(t.blocks)}")

    // === 6. ECONOMIA DA TRANSICAO ===
    imprima("\n\n  === 6. ECONOMIA DA TRANSICAO ===\n")
    progress = engine.overall_progress()
    imprima("  Custo do sistema antigo: {progress['custo_antigo_total']}/ano")
    imprima("  Custo da Republica: {progress['custo_republica']}")
    imprima("  Economia anual: {progress['economia_anual']}")
    imprima("  Em 10 anos: R$ {float(progress['custo_antigo_total'].replace('R$ ', '').replace(' bi/ano', '')) * 10:.0f} bi")

    // === 7. RISCOS POR SISTEMA ===
    imprima("\n\n  === 7. RISCOS E MITIGACAO ===\n")
    para cada tid em ["TR-MONEY", "TR-HEALTH", "TR-HOUSING", "TR-CORPORATIONS"]:
        t = engine.tracks[tid]
        imprima("\n  {t.system.value.upper()}:")
        para cada risk em t.risks[:3]:
            imprima("    RISCO: {risk}")
        para cada mit em t.mitigation[:3]:
            imprima("    MITIGACAO: {mit}")

    // === 8. PROGRESSO GLOBAL ===
    imprima("\n\n  === 8. PROGRESSO GLOBAL ===\n")
    para cada (k, v) em progress.items():
        imprima("  {k:<25} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DO OPENTRANSITION")
    imprima("{'='*80}")
    imprima("""
  A REPUBLICA NASCE GRADUALMENTE:
    Nao e golpe. Nao e revolucao sangrenta. Nao e decreto.
    e CONSTRUCAO. Depois ADOCAO. Depois PARALELO.
    Depois DUPLA CIRCULACAO. Depois MASSA. Depois DESCOMISSIONAMENTO.
    Depois REPUBLICA COMPLETA.

    Cada fase so avanca quando a anterior PROVA que funciona.
    Ninguem e jogado no desconhecido.

  O QUE A REPUBLICA GARANTE DURANTE A TRANSICAO:
    1. NINGUEM MORRE: hospitais nao fecham ate OpenHealth funcionar
    2. NINGUEM PASSA FOME: comida continua ate OpenCredit assumir
    3. NINGUEM FICA SEM TETO: moradia continua ate OpenCivilConstruction
    4. NINGUEM PERDE ESCOLA: educacao continua ate OpenSchool assumir
    5. DINHEIRO CONTINUA: ate OpenCredit ser adotado pela maioria

  O QUE A REPUBLICA nao ACEITA:
    - Richos sabotando para manter privilegio
    - Corporacoes boicotando sistema novo
    - Media espalhando medo (OpenContentPolicy + OpenMentalHygiene)
    - Politicos bloqueando (OpenDemocracy substitui)
    - Banqueiros manipulando (dinheiro perde relevancia naturalmente)

  A MATEMATICA DA TRANSICAO:
    Sistema antigo: R$ {progress['custo_antigo_total']}/ano
    Republica: ZERO
    A cada ano que a Republica avanca: R$ bilhoes economizados
    A cada sistema que migra: milhoes beneficiados
    A metrica e SIMPLES: custo cai, qualidade sobe, pessoas felizes.

  CRONOGRAMA ESTIMADO:
    Fase 0 (Construcao): JA EM ANDAMENTO (110+ sistemas)
    Fase 1 (Adocao voluntaria): 1-3 anos
    Fase 2 (Infraestrutura): 3-5 anos
    Fase 3 (Dupla circulacao): 5-10 anos
    Fase 4 (Migracao em massa): 10-15 anos
    Fase 5 (Descomissionamento): 15-20 anos
    Fase 6 (Republica completa): 20-25 anos

    Pode ser mais rapido. Pode ser mais lento.
    A velocidade depende da adocao do povo. (P4)

  PRINCIPIOS:
    P1: Transicao equitativa. Richos nao escapam. Pobres nao prejudicados.
    P2: Ningém perde acesso a nada durante a transicao.
    seja P3: Quem migra primeiro = pioneiro (credito de impacto extra).
    P4: O povo decide o ritmo. Sem imposicao. Sem decreto.
// )
    imprima("{'='*80}")
    imprima("  OpenTransition: Fase {progress['fase_atual']} "
          "(Construcao completa: 110+ sistemas).")
    imprima("  {progress['total_trilhas']} trilhas de migracao mapeadas.")
    imprima("  Economia potencial: {progress['economia_anual']}.")
    imprima("  Gradual. Voluntaria. Segura. Medivel.")
    imprima("{'='*80}")

```
