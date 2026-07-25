// OpenCommunityLeaders -- Cooptar Liderancas, Generalizar Solucoes -- gerado de Portugol++
package opencommunityleaders_cooptar_liderancas_generalizar_solucoes

import "fmt"

// !/usr/bin/env python3
//
OpenCommunityLeaders -- Cooptar Liderancas, Generalizar Solucoes
==================================================================
"O fundador ! sabe o que o quilombo precisa.
O lider do quilombo SABE.
A Republica COOPTA liderancas (no bom sentido: traz para dentro).
Cada lider define as necessidades REAIS.
A Republica desenvolve solucoes ESPECIFICAS.
Essas solucoes se GENERALIZAM para todos do mesmo tipo.
Processo:
1. Lider define necessidade real (! fundador)
2. Republica desenvolve solucao especifica
3. Solucao vira PADRAO para aquele tipo de comunidade
4. Todas as comunidades daquele tipo recebem
5. Cada uma ADAPTA localmente (LEGO)
6. Feedback volta -> melhora o padrao
Nao &&'imposicao top-down. E'co-criacao bottom-up que vira padrao."
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
type LeaderRole int
const (
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
type CommunityLeader struct {
    // Um lider cooptado pela Republica.
    leader_id: texto
    alias: texto // nome obfuscado
    role: LeaderRole
    community_type: texto // quilombo, favela, sertao, etc
    community_name: texto // nome da comunidade (obfuscado)
    years_in_community := 0 // int64
    authority_level := ""  // reconhecido, respeitado, referência // string
    // O que trouxe para a Republica
    needs_reported := field(default_factory=list) // [texto]
    solutions_proposed := field(default_factory=list) // [texto]
    // O que recebeu
    openskills_profile := false // bool
    opencredit_access := false // bool
    training_received := field(default_factory=list) // [texto]
// ============================================================================
// 2. NECESSIDADE ESPECIFICA -> SOLUCAO GENERALIZAVEL
// ============================================================================
type SolutionStatus int
const (
    PROPOSED = "proposta"  // lider relatou
    IN_DEVELOPMENT = "em_desenvolvimento"
    PILOT_TESTING = "teste_piloto"
    VALIDATED = "validada"  // funcionou em 1 comunidade
    GENERALIZED = "generalizada"  // padrao para todas do tipo
    SCALED = "escalada"  // implementada em varias
// decorador: @dataclass
type CommunitySolution struct {
    // Uma solucao especifica que vira padrao generalizavel.
    solution_id: texto
    community_type: texto // tipo de comunidade
    need: texto // necessidade (definida pelo lider)
    solution: texto // solucao desenvolvida
    proposed_by: texto // alias do lider
    // Generalizacao
    pattern_name := ""  // nome do padrao (ex: "AguaParaSertao") // string
    applicable_to := field(default_factory=list) // quais tipos // [texto]
    generalizable := true // bool
    // Status
    status := SolutionStatus.PROPOSED // SolutionStatus
    pilot_community := "" // string
    pilot_result := "" // string
    communities_using := 0 // int64
    // Recursos necessarios
    cost_to_implement := "" // string
    fablab_needed := false // bool
    training_needed := "" // string
    time_to_deploy := "" // string
    // Adaptacoes locais (cada comunidade adapta)
    local_adaptations := field(default_factory=list) // [texto]
// ============================================================================
// 3. LIDERES COOPTADOS (perfil real, nome obfuscado)
// ============================================================================
LEADERS := [ // [CommunityLeader]
    // QUILOMBO
    CommunityLeader("L-001", "Lid_Quil_A", LeaderRole.LIDER_TRADICIONAL,
                    "quilombo", "Com_Quil_Norte", years_in_community=62,
                    authority_level = "anciao fundador",
                    needs_reported = [
                        "Titulacao da terra parada ha 15 anos no INCRA",
                        "Sem energia eletrica em 8 das 12 casas",
                        "Escola fecha porque professor ! quer vir",
                        "Posto de saude a 47km, sem transporte",
                        "Producao de farinha sem agioa mecanica",
                        "Jovens saindo por falta de trabalho",
                    ]),
    // ASSENTAMENTO
    CommunityLeader("L-002", "Lid_Ass_B", LeaderRole.COOPERATIVA,
                    "assentamento_rural", "Com_Ass_CentroOeste", years_in_community=18,
                    authority_level = "presidente cooperativa 400 familias",
                    needs_reported = [
                        "Trator cooperativo quebra && peça demora 3 meses",
                        "Vendemos materia prima por R$ 2, industria revende por R$ 15",
                        "Banco cobra 40% de juros em credito rural",
                        "Sem internet no campo, ! conseguimos vender online",
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
                    authority_level = "paje && lider espiritual",
                    needs_reported = [
                        "Garimpo ilegal contaminando rio com mercurio",
                        "Madeireiros invadindo territorio",
                        "Sem energia para monitorar fronteiras da terra",
                        "DSEI (saude indigena) ! envia medico ha 6 meses",
                        "Escola ! tem material em lingua nativa",
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
                        "Banco ! faz emprestimo para morador da favela",
                        "Sem espaco publico para reuniao comunitaria",
                    ]),
    // SERTAO
    CommunityLeader("L-006", "Lid_Ser_F", LeaderRole.ASSOCIACAO,
                    "sertao", "Com_Ser_Nordeste", years_in_community=55,
                    authority_level = "presidente associacao rural 200 familias",
                    needs_reported = [
                        "Agua: cisterna secou, proxima chuva em 4 meses",
                        "Poço artesiano salobro, ! serve para beber",
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
                        "Internet 4G ! chega, so 2G",
                        "Quer produzir mel mas sem equipamento",
                        "Quer vender artesanato online mas sem logistica",
                        "Escola ! tem computador",
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
SOLUTIONS := [ // [CommunitySolution]
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
        fablab_needed = true,
        time_to_deploy = "1 dia por casa",
        local_adaptations = [
            "Quilombo: painel no telhado",
            "Ribeirinho: painel flutuante || fixo na margem",
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
        fablab_needed = true,
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
        need = "Escola fecha porque professor ! quer vir",
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
        need = "Trator cooperativo quebra && peca demora 3 meses",
        solution = (
            "OpenTrator: trator OpenHardware. FabLab fabrica peca. "
            "OpenRepair: mecanico local (treinado) conserta. "
            "Peça impressa em 3D || usinada em 1 dia (vs 3 meses importando). "
            "Custo: R$ 0 (CC0). Peça: material reciclado."
        ),
        proposed_by = "Lid_Ass_B",
        pattern_name = "MaquinarioReparavelLocal",
        applicable_to = ["assentamento_rural", "sertao", "quilombo"],
        status = SolutionStatus.IN_DEVELOPMENT,
        fablab_needed = true,
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
        fablab_needed = true,
    ),
    // === RIBEIRINHO ===
    CommunitySolution(
        "SOL-R01", "ribeirinho",
        need = "Diesel para gerador custa R$ 8/litro trazido de barco",
        solution = (
            "Painel Solar Flutuante: flutua no rio. "
            "500W + bateria estacionaria. Substitui gerador diesel. "
            "Custo: ZERO combustivel (sol && gratis). "
            "FabLab regional: estrutura de PVC + painel."
        ),
        proposed_by = "Lid_Rib_C",
        pattern_name = "EnergiaSolarFlutuante",
        applicable_to = ["ribeirinho", "quilombo"],
        status = SolutionStatus.VALIDATED,
        pilot_result = "Reduziu custo energia de R$ 600/mes para R$ 0",
        communities_using = 2,
        fablab_needed = true,
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
            "Professor viaja 1x/mes (! diariamente). "
            "Resto: ensino digital + anciao local. "
            "Crianca aprende na COMUNIDADE (! viaja)."
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
        need = "Escola ! tem material em lingua nativa",
        solution = (
            "OpenInternationalization: traduz tudo para lingua nativa. "
            "IA traduz OpenEducation para a lingua da etnia. "
            "Professor da propria etnia valida traducao. "
            "Material impresso (FabLab) + digital (OpenTerminal). "
            "LINGUA NATIVA && primaria. Portugues && secundario."
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
            "Mercearia da favela: 5% volta pra ELA (! pra banco)."
        ),
        proposed_by = "Lid_Fav_E",
        pattern_name = "PagamentoSemIntermediario",
        applicable_to = ["favela", "assentamento_rural", "quilombo"],
        status = SolutionStatus.PROPOSED,
        fablab_needed = true,
    ),
    CommunitySolution(
        "SOL-F02", "favela",
        need = "Banco ! faz emprestimo para morador da favela",
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
            "Jovem tem ALTERNATIVA. Trafico ! &&' unica opcao."
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
            "30%: telemedicina || encaminha. "
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
            "1 familia = 1 sistema. FabLab fabrica bomba && filtro. "
            "AGUA GARANTIDA o ano todo."
        ),
        proposed_by = "Lid_Ser_F",
        pattern_name = "AguaGarantidaSemiArido",
        applicable_to = ["sertao", "assentamento_rural"],
        status = SolutionStatus.VALIDATED,
        pilot_result = "Cisterna + poco: autonomia 12 meses",
        communities_using = 10,
        fablab_needed = true,
    ),
    CommunitySolution(
        "SOL-SE02", "sertao",
        need = "Poco artesiano salobro, ! serve para beber",
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
        fablab_needed = true,
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
            "Comida ! estraga. Medicamento ! perde."
        ),
        proposed_by = "Lid_Ser_F",
        pattern_name = "RefrigeracaoEstavelSolar",
        applicable_to = ["sertao", "ribeirinho", "quilombo"],
        status = SolutionStatus.PROPOSED,
        fablab_needed = true,
    ),
]
// ============================================================================
// 5. MOTOR DE LIDERANCAS E GENERALIZACAO
// ============================================================================
type CommunityLeaderEngine struct {
    // Motor que coopta liderancas e generaliza solucoes.
    PROCESSO (bottom-up):
    1. CONTATO: Republica vai ATE o lider (! espera vir)
    - Via lideranca tradicional (NUNCA bypass)
    - Apresenta: 'tenho 116 sistemas. O que VOCE precisa?'
    - Escuta. ! fala.
    2. DIAGNOSTICO: lider define necessidades REAIS
    - Republica ! assume o que precisa
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
    - Lider recebe ferramenta (! ordem)
    - Lider decede o que fazer com ela (P2)
    - Lider ENSINA a Republica (! so aprende)
    //
    func __init__(self) {
        self.leaders: {texto: CommunityLeader} = {l.leader_id: l para l em LEADERS}
        self.solutions: {texto: CommunitySolution} = {s.solution_id: s para s em SOLUTIONS}
    func list_leaders(self, community_type: texto = None) [Dict] {
        leaders = self.leaders.values()
        if community_type {
            leaders = [l para l em leaders if l.community_type == community_type]
        return [
            {
                "id": l.leader_id, "alias": l.alias,
                "role": l.role.value, "community": l.community_name,
                "type": l.community_type, "years": l.years_in_community,
                "authority": l.authority_level,
                "needs_reported": len(l.needs_reported),
            }
            para l em leaders {
        ]
    funcao list_solutions(self, community_type: texto = nulo,
                    status := nil) -> [Dict]: // SolutionStatus
        sols = self.solutions.values()
        if community_type {
            sols = [s para s em sols if s.community_type == community_type]
        if status {
            sols = [s para s em sols if s.status == status]
        return [
            {
                "id": s.solution_id,
                "need": s.need[:40],
                "solution": s.solution[:50],
                "pattern": s.pattern_name,
                "status": s.status.value,
                "applicable_to": s.applicable_to,
                "communities_using": s.communities_using,
            }
            para s em sols {
        ]
    funcao needs_report_by_type(self) retorna Dict[texto, [texto]]:
        // Todas as necessidades reportadas por tipo de comunidade.
        result = defaultdict(list)
        for _, leader := range self.leaders.values() {
            for _, need := range leader.needs_reported {
                if need ! in result[leader.community_type] {
                    result[leader.community_type].append(need)
        return dict(result)
    func generalizable_patterns(self) [Dict] {
        // Padroes que ja podem ser generalizados.
        return [
            {
                "pattern": s.pattern_name,
                "origin": s.community_type,
                "applicable_to": s.applicable_to,
                "status": s.status.value,
                "need": s.need[:40],
                "solution": s.solution[:60],
                "adaptations": s.local_adaptations,
            }
            para s em self.solutions.values() {
            if s.generalizable && s.status in (
                SolutionStatus.VALIDATED, SolutionStatus.GENERALIZED,
                SolutionStatus.PILOT_TESTING)
        ]
    func solution_pipeline(self) {texto: qualquer} {
        // Pipeline de solucoes: proposta -> padrao.
        by_status = defaultdict(inteiro)
        for _, s := range self.solutions.values() {
            by_status[s.status.value] += 1
        return {
            "total_solucoes": len(self.solutions),
            "por_status": dict(by_status),
            "validadas": by_status.get("validada", 0),
            "em_teste": by_status.get("teste_piloto", 0),
            "em_desenvolvimento": by_status.get("em_desenvolvimento", 0),
            "propostas": by_status.get("proposta", 0),
            "padroes_generalizaveis": soma(
                1 para s em self.solutions.values()
                if s.status in (SolutionStatus.VALIDATED,
                                SolutionStatus.PILOT_TESTING)
                && len(s.applicable_to) > 1),
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
        return [
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
    func stats(self) {texto: qualquer} {
        all_needs = soma(len(l.needs_reported) para l em self.leaders.values())
        return {
            "lideres_cooptados": len(self.leaders),
            "tipos_representados": len(set(l.community_type para l em self.leaders.values())),
            "necessidades_reportadas": all_needs,
            "solucoes_desenvolvidas": len(self.solutions),
            "padroes_generalizaveis": soma(
                1 para s em self.solutions.values()
                if s.generalizable && len(s.applicable_to) > 1),
            "principio": "Lider define. Republica desenvolve. Solucao generaliza.",
        }
// ============================================================================
// 6. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = CommunityLeaderEngine()
    fmt.Println("=" * 80)
    fmt.Println("  OPENCOMMUNITYLEADERS -- COOPTAR, DESENVOLVER, GENERALIZAR")
    fmt.Println("  Lider define necessidade. Republica desenvolve. Solucao generaliza.")
    fmt.Println("=" * 80)
    // === 1. LIDERES COOPTADOS ===
    fmt.Println("\n\n  === 1. LIDERANCAS COOPTADAS ===\n")
    para ct em ["quilombo", "assentamento_rural", "ribeirinho", {
            "aldeia_indigena", "favela", "sertao"]:
        leaders = engine.list_leaders(ct)
        fmt.Println("\n  {ct.upper()}:")
        for _, l := range leaders {
            fmt.Println("    {l['alias']:<15} {l['role']:<25} {l['authority']}")
            fmt.Println("      Comunidade: {l['community']} ({l['years']} anos)")
            fmt.Println("      Necessidades: {l['needs_reported']}")
    // === 2. NECESSIDADES POR TIPO ===
    fmt.Println("\n\n  === 2. NECESSIDADES REAIS REPORTADAS POR LIDERES ===\n")
    needs = engine.needs_report_by_type()
    para cada (ct, ct_needs) em needs.items(): {
        fmt.Println("\n  {ct.upper()} ({len(ct_needs)} necessidades):")
        for _, n := range ct_needs {
            fmt.Println("    - {n}")
    // === 3. SOLUCOES DESENVOLVIDAS ===
    fmt.Println("\n\n  === 3. SOLUCOES DESENVOLVIDAS ===\n")
    para ct em ["quilombo", "assentamento_rural", "ribeirinho", {
            "aldeia_indigena", "favela", "sertao"]:
        sols = engine.list_solutions(ct)
        fmt.Println("\n  {ct.upper()} ({len(sols)} solucoes):")
        for _, s := range sols {
            fmt.Println("    [{s['status']:<18}] {s['need'][:40]}")
            fmt.Println("      Padrao: {s['pattern']}")
            fmt.Println("      Aplicavel para: {', '.join(s['applicable_to'])}")
            if s["communities_using"] > 0 {
                fmt.Println("      Comunidades usando: {s['communities_using']}")
    // === 4. PADROES GENERALIZAVEIS ===
    fmt.Println("\n\n  === 4. PADROES GENERALIZAVEIS ===\n")
    patterns = engine.generalizable_patterns()
    for _, p := range patterns {
        fmt.Println("\n  {p['pattern']} (origem: {p['origin']})")
        fmt.Println("    Resolve: {p['need']}")
        fmt.Println("    Aplicavel para: {', '.join(p['applicable_to'])}")
        fmt.Println("    Status: {p['status']}")
        if p["adaptations"] {
            fmt.Println("    Adaptacoes locais:")
            for _, a := range p["adaptations"] {
                fmt.Println("      - {a}")
    // === 5. PIPELINE ===
    fmt.Println("\n\n  === 5. PIPELINE DE SOLUCOES ===\n")
    pipe = engine.solution_pipeline()
    fmt.Println("  {pipe['message']}")
    fmt.Println("\n  Status das solucoes:")
    para cada (status, count) em pipe["por_status"].items(): {
        bar = "#" * count
        fmt.Println("    {status:<20} {count} {bar}")
    fmt.Println("\n  Padroes generalizaveis: {pipe['padroes_generalizaveis']}")
    // === 6. COMO ENGAJAR ===
    fmt.Println("\n\n  === 6. COMO COOPTAR UM LIDER ===\n")
    steps = engine.how_to_engage()
    for _, step := range steps {
        fmt.Println("  {step['passo']}")
        fmt.Println("    {step['acao']}")
        fmt.Println("    Tempo: {step['tempo']}")
    // === 7. STATS ===
    fmt.Println("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items(): {
        fmt.Println("  {k:<30} {v}")
    fmt.Println("\n{'='*80}")
    fmt.Println("  OpenCommunityLeaders: {s['lideres_cooptados']} lideres, "
        "{s['necessidades_reportadas']} necessidades, "
        "{s['solucoes_desenvolvidas']} solucoes, "
        "{s['padroes_generalizaveis']} padroes.")
    fmt.Println("  {s['principio']}")
    fmt.Println("{'='*80}")
