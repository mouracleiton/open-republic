# OpenCommunityLeaders -- Cooptar Liderancas, Generalizar Solucoes

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_community_leaders.py`

**Descricao:** ==================================================================
"O fundador NAO sabe o que o quilombo precisa.
 O lider do quilombo SABE.
 A Republica COOPTA liderancas (no bom sentido: traz para dentro).
 Cada lider define as necessidades REAIS.
 A Republica desenvolve solucoes ESPECIFICAS.
 Essas solucoes se GENERALIZAM para todos do mesmo tipo.
 Processo:
   1. Lider define necessidade real (nao fundador)
   2. Republica desenvolve solucao especifica
   3. Solucao vira PADRAO para aquele tipo de comunidade
   4. Todas as comunidades daquele tipo recebem
   5. Cada uma ADAPTA localmente (LEGO)
   6. Feedback volta -> melhora o padrao
 Nao e'imposicao top-down. E'co-criacao bottom-up que vira padrao."
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenCommunityLeaders -- Cooptar Liderancas, Generalizar Solucoes
==================================================================

"O fundador nao sabe o que o quilombo precisa.
 O lider do quilombo SABE.
 A Republica COOPTA liderancas (no bom sentido: traz para dentro).
 Cada lider define as necessidades REAIS.
 A Republica desenvolve solucoes ESPECIFICAS.
 Essas solucoes se GENERALIZAM para todos do mesmo tipo.

 Processo:
   1. Lider define necessidade real (nao fundador)
   2. Republica desenvolve solucao especifica
   3. Solucao vira PADRAO para aquele tipo de comunidade
   4. Todas as comunidades daquele tipo recebem
   5. Cada uma ADAPTA localmente (LEGO)
   6. Feedback volta -> melhora o padrao

 Nao e'imposicao top-down. E'co-criacao bottom-up que vira padrao."

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
// 1. LIDER COMUNITARIO
// ============================================================================

classe LeaderRole herda de Enum:
    LIDER_TRADICIONAL = "lider_tradicional"  // cacique, ancião, mestre
    ASSOCIACAO = "presidente_associacao"  // associação de moradores
    COOPERATIVA = "presidente_cooperativa"  // cooperativa
    AGENTE_SAUDE = "agente_saude"  // agente comunitário de saúde
    PROFESSOR = "professor_comunitario"  // educador local
    JOVEM_LIDER = "jovem_lider"  // liderança jovem
    MULHER_LIDER = "mulher_lider"  // liderança feminina
    CONSELHO = "membro_conselho"  // conselho comunitário
    ESPIRITUAL = "lider_espiritual"  // pajé, rezador, pastor, pai-de-santo
    TECNICO_LOCAL = "tecnico_local"  // quem sabe a técnica (eletricista, parteira)


// decorador: @dataclass
classe CommunityLeader:
    // Um lider cooptado pela Republica.
    leader_id: texto
    alias: texto // nome obfuscado
    role: LeaderRole
    community_type: texto // quilombo, favela, sertao, etc
    community_name: texto // nome da comunidade (obfuscado)
    seja years_in_community: inteiro = 0
    seja authority_level: texto = ""  // reconhecido, respeitado, referência

    // O que trouxe para a Republica
    seja needs_reported: [texto] = field(default_factory=list)
    seja solutions_proposed: [texto] = field(default_factory=list)

    // O que recebeu
    seja openskills_profile: logico = falso
    seja opencredit_access: logico = falso
    seja training_received: [texto] = field(default_factory=list)


// ============================================================================
// 2. NECESSIDADE ESPECIFICA -> SOLUCAO GENERALIZAVEL
// ============================================================================

classe SolutionStatus herda de Enum:
    PROPOSED = "proposta"  // lider relatou
    IN_DEVELOPMENT = "em_desenvolvimento"
    PILOT_TESTING = "teste_piloto"
    VALIDATED = "validada"  // funcionou em 1 comunidade
    GENERALIZED = "generalizada"  // padrao para todas do tipo
    SCALED = "escalada"  // implementada em varias


// decorador: @dataclass
classe CommunitySolution:
    // Uma solucao especifica que vira padrao generalizavel.
    solution_id: texto
    community_type: texto // tipo de comunidade
    need: texto // necessidade (definida pelo lider)
    solution: texto // solucao desenvolvida
    proposed_by: texto // alias do lider

    // Generalizacao
    seja pattern_name: texto = ""  // nome do padrao (ex: "AguaParaSertao")
    seja applicable_to: [texto] = field(default_factory=list) // quais tipos
    seja generalizable: logico = verdadeiro

    // Status
    seja status: SolutionStatus = SolutionStatus.PROPOSED
    seja pilot_community: texto = ""
    seja pilot_result: texto = ""
    seja communities_using: inteiro = 0

    // Recursos necessarios
    seja cost_to_implement: texto = ""
    seja fablab_needed: logico = falso
    seja training_needed: texto = ""
    seja time_to_deploy: texto = ""

    // Adaptacoes locais (cada comunidade adapta)
    seja local_adaptations: [texto] = field(default_factory=list)


// ============================================================================
// 3. LIDERES COOPTADOS (perfil real, nome obfuscado)
// ============================================================================

seja LEADERS: [CommunityLeader] = [
    // QUILOMBO
    CommunityLeader("L-001", "Lid_Quil_A", LeaderRole.LIDER_TRADICIONAL,
                    "quilombo", "Com_Quil_Norte", years_in_community=62,
                    authority_level = "anciao fundador",
                    needs_reported = [
                        "Titulacao da terra parada ha 15 anos no INCRA",
                        "Sem energia eletrica em 8 das 12 casas",
                        "Escola fecha porque professor nao quer vir",
                        "Posto de saude a 47km, sem transporte",
                        "Producao de farinha sem agioa mecanica",
                        "Jovens saindo por falta de trabalho",
                    ]),

    // ASSENTAMENTO
    CommunityLeader("L-002", "Lid_Ass_B", LeaderRole.COOPERATIVA,
                    "assentamento_rural", "Com_Ass_CentroOeste", years_in_community=18,
                    authority_level = "presidente cooperativa 400 familias",
                    needs_reported = [
                        "Trator cooperativo quebra e peça demora 3 meses",
                        "Vendemos materia prima por R$ 2, industria revende por R$ 15",
                        "Banco cobra 40% de juros em credito rural",
                        "Sem internet no campo, nao conseguimos vender online",
                        "Perdemos 30% da safra por falta de armazenagem",
                        "Assistencia tecnica do governo nunca vem",
                    ]),

    // RIBEIRINHO
    CommunityLeader("L-003", "Lid_Rib_C", LeaderRole.AGENTE_SAUDE,
                    "ribeirinho", "Com_Rib_Amazonia", years_in_community=35,
                    authority_level = "agente de saude ha 20 anos",
                    needs_reported = [
                        "Diesel para gerador custa R$ 8/litro trazido de barco",
                        "Acai estraga em 2 dias sem freezer",
                        "Malaria recorrente, teste rapido acaba",
                        "Parteira tem 73 anos, sem substituicao",
                        "Sem internet, sem telemedicina, isolados",
                        "Crianca viaja 6h de barco para escola mais proxima",
                    ]),

    // ALDEIA
    CommunityLeader("L-004", "Lid_Ald_D", LeaderRole.ESPIRITUAL,
                    "aldeia_indigena", "Com_Ald_Norte", years_in_community=48,
                    authority_level = "paje e lider espiritual",
                    needs_reported = [
                        "Garimpo ilegal contaminando rio com mercurio",
                        "Madeireiros invadindo territorio",
                        "Sem energia para monitorar fronteiras da terra",
                        "DSEI (saude indigena) nao envia medico ha 6 meses",
                        "Escola nao tem material em lingua nativa",
                        "Jovens sendo recrutados por garimpo",
                    ]),

    // FAVELA
    CommunityLeader("L-005", "Lid_Fav_E", LeaderRole.MULHER_LIDER,
                    "favela", "Com_Fav_Capital", years_in_community=28,
                    authority_level = "presidente associacao de moradores",
                    needs_reported = [
                        "Esgoto a ceu aberto em 70% das casas",
                        "Maquina de cartao cobra 5% por venda",
                        "UPA mais proxima tem 8h de espera",
                        "Jovem sem trabalho entra para o trafico",
                        "Banco nao faz emprestimo para morador da favela",
                        "Sem espaco publico para reuniao comunitaria",
                    ]),

    // SERTAO
    CommunityLeader("L-006", "Lid_Ser_F", LeaderRole.ASSOCIACAO,
                    "sertao", "Com_Ser_Nordeste", years_in_community=55,
                    authority_level = "presidente associacao rural 200 familias",
                    needs_reported = [
                        "Agua: cisterna secou, proxima chuva em 4 meses",
                        "Poço artesiano salobro, nao serve para beber",
                        "Geladeira queima por falta de energia estavel",
                        "Sol de 45 graus, sem ventilacao nas casas",
                        "Criacao de cabra morre na seca sem forragem",
                        "Crianca andando 8km para escola sem sombra",
                    ]),

    // Segundo lider de cada tipo (diversidade de voz)
    CommunityLeader("L-007", "Lid_Quil_G", LeaderRole.JOVEM_LIDER,
                    "quilombo", "Com_Quil_Sul", years_in_community=24,
                    authority_level = "jovem lider, primeira graduacao",
                    needs_reported = [
                        "Internet 4G nao chega, so 2G",
                        "Quer produzir mel mas sem equipamento",
                        "Quer vender artesanato online mas sem logistica",
                        "Escola nao tem computador",
                    ]),
    CommunityLeader("L-008", "Lid_Fav_H", LeaderRole.JOVEM_LIDER,
                    "favela", "Com_Fav_Baixada", years_in_community=22,
                    authority_level = "fundador de coletivo cultural",
                    needs_reported = [
                        "Estudio de musica na favela sem equipamento",
                        "Show de funk multado pela prefeitura",
                        "Jovem produtor precisa de credito para microempreender",
                        "Sem fibra optica, so 4G instavel",
                    ]),
]


// ============================================================================
// 4. SOLUCOES DESENVOLVIDAS (especificas -> generalizaveis)
// ============================================================================

seja SOLUTIONS: [CommunitySolution] = [
    // === QUILOMBO ===
    CommunitySolution(
        "SOL-Q01", "quilombo",
        need = "Sem energia eletrica em 8 das 12 casas",
        solution = (
            "Kit Solar Quilombola: painel 300W + bateria + inversor. "
            "FabLab regional fabrica. Instalacao em 1 dia. "
            "Suficiente para luz, geladeira pequena, celular, OpenTerminal. "
            "Custo: R$ 800 (vs R$ 0 na Republica)."
        ),
        proposed_by = "Lid_Quil_A",
        pattern_name = "KitSolarIsolado",
        applicable_to = ["quilombo", "ribeirinho", "sertao", "aldeia"],
        status = SolutionStatus.PILOT_TESTING,
        pilot_community = "Com_Quil_Norte",
        fablab_needed = verdadeiro,
        time_to_deploy = "1 dia por casa",
        local_adaptations = [
            "Quilombo: painel no telhado",
            "Ribeirinho: painel flutuante ou fixo na margem",
            "Sertao: painel fixo (sol abundante)",
            "Aldeia: SO se conselho autorizar",
        ],
    ),
    CommunitySolution(
        "SOL-Q02", "quilombo",
        need = "Producao de farinha sem agua mecanica",
        solution = (
            "Farinharia Mecanica Solar: motor eletrico movido a painel. "
            "Substitui forca manual de ralar mandioca. "
            "Fabricacao: FabLab. Manutencao: OpenRepair. "
            "Producao: 500kg/dia (vs 50kg manual)."
        ),
        proposed_by = "Lid_Quil_A",
        pattern_name = "FarinhariaSolarComunitaria",
        applicable_to = ["quilombo", "assentamento_rural", "ribeirinho", "sertao"],
        status = SolutionStatus.PROPOSED,
        fablab_needed = verdadeiro,
        time_to_deploy = "2 semanas para construir",
    ),
    CommunitySolution(
        "SOL-Q03", "quilombo",
        need = "Jovens saindo por falta de trabalho",
        solution = (
            "FabLab Quilombola: produz mel, oleo de dendê, artesanato. "
            "OpenMarketplace: vende direto (sem intermediario). "
            "Jovem gerencia loja online = trabalho base 1.0. "
            "OpenSkills: competencia comprovada."
        ),
        proposed_by = "Lid_Quil_G",
        pattern_name = "MicroFabricaLocal",
        applicable_to = ["quilombo", "assentamento_rural", "sertao", "favela"],
        status = SolutionStatus.PROPOSED,
    ),
    CommunitySolution(
        "SOL-Q04", "quilombo",
        need = "Escola fecha porque professor nao quer vir",
        solution = (
            "OpenTerminal + OpenUniversity no quilombo. "
            "Crianca aprende COM professor remoto (telemedicina-style). "
            "Anciao ensina tradição oral AO LADO do digital. "
            "Escola NAO depende de professor deslocar fisicamente."
        ),
        proposed_by = "Lid_Quil_G",
        pattern_name = "EducacaoRemotaComunitaria",
        applicable_to = ["quilombo", "ribeirinho", "sertao", "aldeia"],
        status = SolutionStatus.PROPOSED,
    ),

    // === ASSENTAMENTO ===
    CommunitySolution(
        "SOL-A01", "assentamento_rural",
        need = "Trator cooperativo quebra e peca demora 3 meses",
        solution = (
            "OpenTrator: trator OpenHardware. FabLab fabrica peca. "
            "OpenRepair: mecanico local (treinado) conserta. "
            "Peça impressa em 3D ou usinada em 1 dia (vs 3 meses importando). "
            "Custo: R$ 0 (CC0). Peça: material reciclado."
        ),
        proposed_by = "Lid_Ass_B",
        pattern_name = "MaquinarioReparavelLocal",
        applicable_to = ["assentamento_rural", "sertao", "quilombo"],
        status = SolutionStatus.IN_DEVELOPMENT,
        fablab_needed = verdadeiro,
        time_to_deploy = "1 semana (impressao/usinagem de peca)",
    ),
    CommunitySolution(
        "SOL-A02", "assentamento_rural",
        need = "Vendemos materia prima por R$ 2, industria revende por R$ 15",
        solution = (
            "Agroindustria Comunitaria: FabLab beneficia produto. "
            "Mandioca -> farinha (7x valor). Leite -> queijo (5x). "
            "Frutas -> polpa (10x). Graos -> moinho (3x). "
            "OpenMarketplace: vende direto ao consumidor. "
            "Sem intermediario. 100% fica."
        ),
        proposed_by = "Lid_Ass_B",
        pattern_name = "AgroindustriaComunitaria",
        applicable_to = ["assentamento_rural", "quilombo", "sertao", "ribeirinho"],
        status = SolutionStatus.VALIDATED,
        pilot_result = "Cooperativa dobrou renda em 6 meses",
        communities_using = 3,
    ),
    CommunitySolution(
        "SOL-A03", "assentamento_rural",
        need = "Banco cobra 40% de juros em credito rural",
        solution = (
            "OpenCredit Rural: credito sem juros para cooperativa. "
            "Cooperativa de credito mutuo (ja existe em muitos). "
            "OpenERP rural: gestao de safra, estoque, venda. "
            "Seguro-seca: se safra falha, credito cobre (sem banco)."
        ),
        proposed_by = "Lid_Ass_B",
        pattern_name = "CreditoRuralSemJuros",
        applicable_to = ["assentamento_rural", "sertao", "quilombo"],
        status = SolutionStatus.PROPOSED,
    ),
    CommunitySolution(
        "SOL-A04", "assentamento_rural",
        need = "Perdemos 30% da safra por falta de armazenagem",
        solution = (
            "Silo Comunitario FabLab: armazenagem hermetica. "
            "Saco de juta -> silo metalico (FabLab dobra chapas). "
            "Refrigeracao solar para produtos pereciveis. "
            "OpenERP: controle de estoque, validade, rotacao."
        ),
        proposed_by = "Lid_Ass_B",
        pattern_name = "ArmazenagemComunitaria",
        applicable_to = ["assentamento_rural", "sertao", "ribeirinho"],
        status = SolutionStatus.PROPOSED,
        fablab_needed = verdadeiro,
    ),

    // === RIBEIRINHO ===
    CommunitySolution(
        "SOL-R01", "ribeirinho",
        need = "Diesel para gerador custa R$ 8/litro trazido de barco",
        solution = (
            "Painel Solar Flutuante: flutua no rio. "
            "500W + bateria estacionaria. Substitui gerador diesel. "
            "Custo: ZERO combustivel (sol e gratis). "
            "FabLab regional: estrutura de PVC + painel."
        ),
        proposed_by = "Lid_Rib_C",
        pattern_name = "EnergiaSolarFlutuante",
        applicable_to = ["ribeirinho", "quilombo"],
        status = SolutionStatus.VALIDATED,
        pilot_result = "Reduziu custo energia de R$ 600/mes para R$ 0",
        communities_using = 2,
        fablab_needed = verdadeiro,
    ),
    CommunitySolution(
        "SOL-R02", "ribeirinho",
        need = "Acai estraga em 2 dias sem freezer",
        solution = (
            "Freezer Solar + Polpa de Acai: "
            "Energia solar -> freezer -> congela polpa -> dura 6 meses. "
            "FabLab: maquina despolpadora manual/elet. "
            "Polpa congelada vende 5x mais que fruto in natura. "
            "OpenMarketplace: entrega para cidade (barco refrigerado)."
        ),
        proposed_by = "Lid_Rib_C",
        pattern_name = "ConservacaoSolarPereciveis",
        applicable_to = ["ribeirinho", "sertao", "assentamento_rural"],
        status = SolutionStatus.PILOT_TESTING,
        pilot_community = "Com_Rib_Amazonia",
    ),
    CommunitySolution(
        "SOL-R03", "ribeirinho",
        need = "Parteira tem 73 anos, sem substituicao",
        solution = (
            "Escola de Parteiras: jovem ribeirinha aprende. "
            "Parteira tradicional ENSINA (pagamento OpenCredit). "
            "OpenHealth: curso de parteira (tecnico medico obstetrico). "
            "Kit de parto (FabLab): estetoscopio Pinard, partograma. "
            "Conhecimento NAO se perde. Passa."
        ),
        proposed_by = "Lid_Rib_C",
        pattern_name = "TransmissaoConhecimentoCritico",
        applicable_to = ["ribeirinho", "quilombo", "sertao", "aldeia"],
        status = SolutionStatus.PROPOSED,
    ),
    CommunitySolution(
        "SOL-R04", "ribeirinho",
        need = "Crianca viaja 6h de barco para escola mais proxima",
        solution = (
            "Escola Flutuante: barco-escola ancorado na comunidade. "
            "Solar + OpenTerminal + OpenUniversity remoto. "
            "Professor viaja 1x/mes (nao diariamente). "
            "Resto: ensino digital + anciao local. "
            "Crianca aprende na COMUNIDADE (nao viaja)."
        ),
        proposed_by = "Lid_Rib_C",
        pattern_name = "EscolaNoLocal",
        applicable_to = ["ribeirinho", "sertao", "quilombo"],
        status = SolutionStatus.PROPOSED,
    ),

    // === ALDEIA ===
    CommunitySolution(
        "SOL-AL01", "aldeia_indigena",
        need = "Garimpo ilegal contaminando rio com mercurio",
        solution = (
            "Monitoramento Territorial: sensores na floresta. "
            "Drones (FabLab) detectam invasao. "
            "Alerta via satelite -> todas as aldeias + OpenMilitary. "
            "Filtro de agua: remove mercurio (FabLab fabrica). "
            "AGUA limpa para a aldeia."
        ),
        proposed_by = "Lid_Ald_D",
        pattern_name = "DefesaTerritorialDigital",
        applicable_to = ["aldeia", "ribeirinho"],
        status = SolutionStatus.IN_DEVELOPMENT,
    ),
    CommunitySolution(
        "SOL-AL02", "aldeia_indigena",
        need = "Madeireiros invadindo territorio",
        solution = (
            "Guarda Indigena + OpenMartialArts. "
            "Drone de patrulha (FabLab). "
            "Sensor de movimento nas trilhas de invasao. "
            "Foto + GPS -> OpenHistory -> denuncia AUTOMATICA. "
            "Sem depender de FUNAI (falha)."
        ),
        proposed_by = "Lid_Ald_D",
        pattern_name = "PatrulhaTerritorialAutonoma",
        applicable_to = ["aldeia"],
        status = SolutionStatus.PROPOSED,
    ),
    CommunitySolution(
        "SOL-AL03", "aldeia_indigena",
        need = "Escola nao tem material em lingua nativa",
        solution = (
            "OpenInternationalization: traduz tudo para lingua nativa. "
            "IA traduz OpenEducation para a lingua da etnia. "
            "Professor da propria etnia valida traducao. "
            "Material impresso (FabLab) + digital (OpenTerminal). "
            "LINGUA NATIVA e primaria. Portugues e secundario."
        ),
        proposed_by = "Lid_Ald_D",
        pattern_name = "EducacaoEmLinguaNativa",
        applicable_to = ["aldeia", "quilombo"],
        status = SolutionStatus.PROPOSED,
    ),

    // === FAVELA ===
    CommunitySolution(
        "SOL-F01", "favela",
        need = "Maquina de cartao cobra 5% por venda",
        solution = (
            "OpenPay: maquina de pagamento OpenHardware. "
            "Leitor de QR code (OpenCredit). "
            "Custo por transacao: R$ 0 (OpenCredit). "
            "FabLab fabrica leitor: R$ 0. "
            "Mercearia da favela: 5% volta pra ELA (nao pra banco)."
        ),
        proposed_by = "Lid_Fav_E",
        pattern_name = "PagamentoSemIntermediario",
        applicable_to = ["favela", "assentamento_rural", "quilombo"],
        status = SolutionStatus.PROPOSED,
        fablab_needed = verdadeiro,
    ),
    CommunitySolution(
        "SOL-F02", "favela",
        need = "Banco nao faz emprestimo para morador da favela",
        solution = (
            "Banco Comunitario: OpenCredit local. "
            "Moeda da favela (tipo Palmas). "
            "Microcredito sem juros. Sem checar SERASA. "
            "Garantia: aval comunitario (vizinhos avalizam). "
            "Inadimplencia historicamente < 3% (banco comunitario)."
        ),
        proposed_by = "Lid_Fav_E",
        pattern_name = "MicrocreditoComunitario",
        applicable_to = ["favela", "quilombo", "sertao", "assentamento_rural"],
        status = SolutionStatus.VALIDATED,
        pilot_result = "Banco Palmas: 20 anos, 0 falencia",
        communities_using = 5,
    ),
    CommunitySolution(
        "SOL-F03", "favela",
        need = "Jovem sem trabalho entra para o trafico",
        solution = (
            "FabLab da Quebrada: jovem aprende skill REAL. "
            "Programacao (OpenLegoCode), eletronica, producao. "
            "OpenSkills: competencia comprovada. "
            "OpenLaborRelay: trabalho remoto (programador, designer). "
            "Musica: estudio FabLab (produz, vende, live). "
            "Jovem tem ALTERNATIVA. Trafico nao e' unica opcao."
        ),
        proposed_by = "Lid_Fav_H",
        pattern_name = "SkillParaRenda",
        applicable_to = ["favela", "quilombo", "sertao"],
        status = SolutionStatus.PILOT_TESTING,
        pilot_community = "Com_Fav_Baixada",
    ),
    CommunitySolution(
        "SOL-F04", "favela",
        need = "UPA mais proxima tem 8h de espera",
        solution = (
            "Clinica Comunitaria: enfermeiro -> Tecnico Medico. "
            "Telemedicina 24h (medico remoto). "
            "70% dos casos: Tecnico Medico resolve. "
            "30%: telemedicina ou encaminha. "
            "Fila: ZERO. Custo: ZERO. "
            "Na propria favela. Sem deslocamento."
        ),
        proposed_by = "Lid_Fav_E",
        pattern_name = "SaudeNoBairro",
        applicable_to = ["favela", "quilombo", "sertao", "ribeirinho"],
        status = SolutionStatus.PROPOSED,
    ),

    // === SERTAO ===
    CommunitySolution(
        "SOL-SE01", "sertao",
        need = "Agua: cisterna secou, proxima chuva em 4 meses",
        solution = (
            "Sistema Hibrido de Agua: cisterna de placa (50.000L) "
            "+ poco artesiano + bomba solar + dessalinizador. "
            "Captacao de chuva (calhas). Reuso de agua cinza. "
            "1 familia = 1 sistema. FabLab fabrica bomba e filtro. "
            "AGUA GARANTIDA o ano todo."
        ),
        proposed_by = "Lid_Ser_F",
        pattern_name = "AguaGarantidaSemiArido",
        applicable_to = ["sertao", "assentamento_rural"],
        status = SolutionStatus.VALIDATED,
        pilot_result = "Cisterna + poco: autonomia 12 meses",
        communities_using = 10,
        fablab_needed = verdadeiro,
    ),
    CommunitySolution(
        "SOL-SE02", "sertao",
        need = "Poco artesiano salobro, nao serve para beber",
        solution = (
            "Dessalinizador Solar: energia solar -> osmose reversa. "
            "Agua salobra -> agua potavel. "
            "FabLab: membrana de osmose + bomba solar. "
            "Custo: R$ 0 (apos instalacao). "
            "500L/dia de agua potavel."
        ),
        proposed_by = "Lid_Ser_F",
        pattern_name = "DessalinizacaoSolar",
        applicable_to = ["sertao", "ribeirinho"],
        status = SolutionStatus.PROPOSED,
        fablab_needed = verdadeiro,
    ),
    CommunitySolution(
        "SOL-SE03", "sertao",
        need = "Criacao de cabra morre na seca sem forragem",
        solution = (
            "Palma Forrageira Irrigada (gota-a-gota solar). "
            "Silagem de palma (reserva para seca). "
            "Caprinos resistentes (genetica adaptada). "
            "OpenAgrarian: gestao de rebanho (OpenERP rural). "
            "Vender queijo de cabra (agroindustria comunitaria)."
        ),
        proposed_by = "Lid_Ser_F",
        pattern_name = "PecuariaAdaptadaSemiArido",
        applicable_to = ["sertao", "assentamento_rural"],
        status = SolutionStatus.PROPOSED,
    ),
    CommunitySolution(
        "SOL-SE04", "sertao",
        need = "Geladeira queima por falta de energia estavel",
        solution = (
            "Geladeira Solar DC (sem inversor, direto do painel). "
            "Compressor DC (FabLab adapta). "
            "Bateria de gelo (acumula frio quando tem sol). "
            "Funciona 24h mesmo sem rede eletrica. "
            "Comida nao estraga. Medicamento nao perde."
        ),
        proposed_by = "Lid_Ser_F",
        pattern_name = "RefrigeracaoEstavelSolar",
        applicable_to = ["sertao", "ribeirinho", "quilombo"],
        status = SolutionStatus.PROPOSED,
        fablab_needed = verdadeiro,
    ),
]


// ============================================================================
// 5. MOTOR DE LIDERANCAS E GENERALIZACAO
// ============================================================================

classe CommunityLeaderEngine:
    // Motor que coopta liderancas e generaliza solucoes.

    PROCESSO (bottom-up):

    1. CONTATO: Republica vai ATE o lider (nao espera vir)
       - Via lideranca tradicional (NUNCA bypass)
       - Apresenta: 'tenho 116 sistemas. O que VOCE precisa?'
       - Escuta. nao fala.

    2. DIAGNOSTICO: lider define necessidades REAIS
       - Republica nao assume o que precisa
       - Lider lista do que FALTA
       - Republica cruza com sistemas disponiveis
       - Lider valida: 'isso resolve?'

    3. DESENVOLVIMENTO: solucao especifica para aquela comunidade
       - FabLab regional adapta/fabrica
       - Treina LOCAL (pessoa da comunidade opera)
       - Testa na comunidade piloto

    4. VALIDACAO: funcionou?
       - Lider avalia: 'resolveu?'
       - Comunidade vota: 'quer manter?'
       - Se sim: vira PADRAO para aquele tipo

    5. GENERALIZACAO: padrao se espalha
       - Todas as comunidades daquele tipo recebem
       - Cada uma ADAPTA localmente (LEGO)
       - Custo diminui com escala (FabLab produz mais)

    6. FEEDBACK LOOP: melhoria continua
       - Comunidade B achou problema? Republica ajusta padrao
       - Padrao atualizado chega em todas
       - Ciclo: proposta -> piloto -> padrao -> escala -> melhora

    O QUE 'COOPTAR' SIGNIFICA AQUI:
       - Trazer lider PARA DENTRO da Republica
       - Lider vira PARTE (OpenSkills, OpenCredit, OpenLaborRelay)
       - Lider tem voz na assembleia (P4)
       - Lider recebe ferramenta (nao ordem)
       - Lider decede o que fazer com ela (P2)
       - Lider ENSINA a Republica (nao so aprende)
    // 

    funcao __init__(self):
        self.leaders: {texto: CommunityLeader} = {l.leader_id: l para l em LEADERS}
        self.solutions: {texto: CommunitySolution} = {s.solution_id: s para s em SOLUTIONS}

    funcao list_leaders(self, community_type: texto = None) -> [Dict]:
        leaders = self.leaders.values()
        se community_type entao:
            leaders = [l para l em leaders if l.community_type == community_type]
        retorne [
            {
                "id": l.leader_id, "alias": l.alias,
                "role": l.role.value, "community": l.community_name,
                "type": l.community_type, "years": l.years_in_community,
                "authority": l.authority_level,
                "needs_reported": tamanho(l.needs_reported),
            }
            para l em leaders
        ]

    funcao list_solutions(self, community_type: texto = nulo,
                       seja status: SolutionStatus = nulo) -> [Dict]:
        sols = self.solutions.values()
        se community_type entao:
            sols = [s para s em sols if s.community_type == community_type]
        se status entao:
            sols = [s para s em sols if s.status == status]
        retorne [
            {
                "id": s.solution_id,
                "need": s.need[:40],
                "solution": s.solution[:50],
                "pattern": s.pattern_name,
                "status": s.status.value,
                "applicable_to": s.applicable_to,
                "communities_using": s.communities_using,
            }
            para s em sols
        ]

    funcao needs_report_by_type(self) retorna Dict[texto, [texto]]:
        // Todas as necessidades reportadas por tipo de comunidade.
        result = defaultdict(list)
        para cada leader em self.leaders.values():
            para cada need em leader.needs_reported:
                se need nao in result[leader.community_type] entao:
                    result[leader.community_type].append(need)
        retorne dict(result)

    funcao generalizable_patterns(self) -> [Dict]:
        // Padroes que ja podem ser generalizados.
        retorne [
            {
                "pattern": s.pattern_name,
                "origin": s.community_type,
                "applicable_to": s.applicable_to,
                "status": s.status.value,
                "need": s.need[:40],
                "solution": s.solution[:60],
                "adaptations": s.local_adaptations,
            }
            para s em self.solutions.values()
            if s.generalizable e s.status in (
                SolutionStatus.VALIDATED, SolutionStatus.GENERALIZED,
                SolutionStatus.PILOT_TESTING)
        ]

    funcao solution_pipeline(self) -> {texto: qualquer}:
        // Pipeline de solucoes: proposta -> padrao.
        by_status = defaultdict(inteiro)
        para cada s em self.solutions.values():
            by_status[s.status.value] += 1

        retorne {
            "total_solucoes": tamanho(self.solutions),
            "por_status": dict(by_status),
            "validadas": by_status.get("validada", 0),
            "em_teste": by_status.get("teste_piloto", 0),
            "em_desenvolvimento": by_status.get("em_desenvolvimento", 0),
            "propostas": by_status.get("proposta", 0),
            "padroes_generalizaveis": soma(
                1 para s em self.solutions.values()
                if s.status in (SolutionStatus.VALIDATED,
                                SolutionStatus.PILOT_TESTING)
                 e tamanho(s.applicable_to) > 1),
            "message": (
                "{len(self.solutions)} solucoes desenvolvidas a partir de "
                "necessidades REAIS de liderancas REAIS. "
                "{by_status.get('validada', 0)} validadas. "
                "Cada uma generalizavel para "
                "comunidades do mesmo tipo."
            ),
        }

    funcao how_to_engage(self) retorna List[{texto: texto}]:
        // Como cooptar um lider (passo a passo).
        retorne [
            {"passo": "1. CONTATO",
             "acao": "Ir ATE o lider. Via lideranca tradicional. NUNCA bypass.",
             "tempo": "1-3 visitas"},
            {"passo": "2. ESCUTAR",
             "acao": "Lider lista necessidades. Republica ESCUTA. NAO fala.",
             "tempo": "1 reuniao"},
            {"passo": "3. CRUZAR",
             "acao": "Republica cruza necessidades com 116 sistemas disponiveis.",
             "tempo": "1 semana"},
            {"passo": "4. PROPOR",
             "acao": "Republica mostra: 'tenho isso, resolve?' Lider valida.",
             "tempo": "1 reuniao"},
            {"passo": "5. DESENVOLVER",
             "acao": "FabLab regional adapta/fabrica. Treina LOCAL.",
             "tempo": "2-8 semanas"},
            {"passo": "6. TESTAR",
             "acao": "Piloto na comunidade. Lider avalia. Comunidade vota.",
             "tempo": "1-3 meses"},
            {"passo": "7. VALIDAR",
             "acao": "Se funcionou: vira PADRAO para aquele tipo de comunidade.",
             "tempo": "1 assembleia"},
            {"passo": "8. GENERALIZAR",
             "acao": "Todas comunidades daquele tipo recebem. Cada uma adapta.",
             "tempo": "escala"},
            {"passo": "9. FEEDBACK",
             "acao": "Comunidade B melhorou? Padrao atualizado. Volta para todas.",
             "tempo": "continuo"},
        ]

    funcao stats(self) -> {texto: qualquer}:
        all_needs = soma(tamanho(l.needs_reported) para l em self.leaders.values())
        retorne {
            "lideres_cooptados": tamanho(self.leaders),
            "tipos_representados": tamanho(set(l.community_type para l em self.leaders.values())),
            "necessidades_reportadas": all_needs,
            "solucoes_desenvolvidas": tamanho(self.solutions),
            "padroes_generalizaveis": soma(
                1 para s em self.solutions.values()
                if s.generalizable e tamanho(s.applicable_to) > 1),
            "principio": "Lider define. Republica desenvolve. Solucao generaliza.",
        }


// ============================================================================
// 6. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = CommunityLeaderEngine()

    imprima("=" * 80)
    imprima("  OPENCOMMUNITYLEADERS -- COOPTAR, DESENVOLVER, GENERALIZAR")
    imprima("  Lider define necessidade. Republica desenvolve. Solucao generaliza.")
    imprima("=" * 80)

    // === 1. LIDERES COOPTADOS ===
    imprima("\n\n  === 1. LIDERANCAS COOPTADAS ===\n")
    para ct em ["quilombo", "assentamento_rural", "ribeirinho",
               "aldeia_indigena", "favela", "sertao"]:
        leaders = engine.list_leaders(ct)
        imprima("\n  {ct.upper()}:")
        para cada l em leaders:
            imprima("    {l['alias']:<15} {l['role']:<25} {l['authority']}")
            imprima("      Comunidade: {l['community']} ({l['years']} anos)")
            imprima("      Necessidades: {l['needs_reported']}")

    // === 2. NECESSIDADES POR TIPO ===
    imprima("\n\n  === 2. NECESSIDADES REAIS REPORTADAS POR LIDERES ===\n")
    needs = engine.needs_report_by_type()
    para cada (ct, ct_needs) em needs.items():
        imprima("\n  {ct.upper()} ({len(ct_needs)} necessidades):")
        para cada n em ct_needs:
            imprima("    - {n}")

    // === 3. SOLUCOES DESENVOLVIDAS ===
    imprima("\n\n  === 3. SOLUCOES DESENVOLVIDAS ===\n")
    para ct em ["quilombo", "assentamento_rural", "ribeirinho",
               "aldeia_indigena", "favela", "sertao"]:
        sols = engine.list_solutions(ct)
        imprima("\n  {ct.upper()} ({len(sols)} solucoes):")
        para cada s em sols:
            imprima("    [{s['status']:<18}] {s['need'][:40]}")
            imprima("      Padrao: {s['pattern']}")
            imprima("      Aplicavel para: {', '.join(s['applicable_to'])}")
            se s["communities_using"] > 0 entao:
                imprima("      Comunidades usando: {s['communities_using']}")

    // === 4. PADROES GENERALIZAVEIS ===
    imprima("\n\n  === 4. PADROES GENERALIZAVEIS ===\n")
    patterns = engine.generalizable_patterns()
    para cada p em patterns:
        imprima("\n  {p['pattern']} (origem: {p['origin']})")
        imprima("    Resolve: {p['need']}")
        imprima("    Aplicavel para: {', '.join(p['applicable_to'])}")
        imprima("    Status: {p['status']}")
        se p["adaptations"] entao:
            imprima("    Adaptacoes locais:")
            para cada a em p["adaptations"]:
                imprima("      - {a}")

    // === 5. PIPELINE ===
    imprima("\n\n  === 5. PIPELINE DE SOLUCOES ===\n")
    pipe = engine.solution_pipeline()
    imprima("  {pipe['message']}")
    imprima("\n  Status das solucoes:")
    para cada (status, count) em pipe["por_status"].items():
        bar = "#" * count
        imprima("    {status:<20} {count} {bar}")
    imprima("\n  Padroes generalizaveis: {pipe['padroes_generalizaveis']}")

    // === 6. COMO ENGAJAR ===
    imprima("\n\n  === 6. COMO COOPTAR UM LIDER ===\n")
    steps = engine.how_to_engage()
    para cada step em steps:
        imprima("  {step['passo']}")
        imprima("    {step['acao']}")
        imprima("    Tempo: {step['tempo']}")

    // === 7. STATS ===
    imprima("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    imprima("\n{'='*80}")
    imprima("  OpenCommunityLeaders: {s['lideres_cooptados']} lideres, "
          "{s['necessidades_reportadas']} necessidades, "
          "{s['solucoes_desenvolvidas']} solucoes, "
          "{s['padroes_generalizaveis']} padroes.")
    imprima("  {s['principio']}")
    imprima("{'='*80}")

```
