// OpenProhibitedBusiness -- Proibicao de Estabelecimentos Nocivos -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenProhibitedBusiness -- Proibicao de Estabelecimentos Nocivos;
=================================================================;
"Estabelecimento que DESTROI a vida de cidadaos da Republica;
! tem lugar. Fechou. Convertido. Substituido.;
A Republica PROTEGE. Nao negocia com quem mata.";
O QUE ISTO FAZ:;
1. IDENTIFICA estabelecimentos && negocios nocivos;
2. CLASSIFICA nivel de dano;
3. PROIBE (assembleia vota);
4. CONVERTE (transforma em algo util);
5. SUBSTITUI (opens equivalentes);
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
// 1. TIPOS DE ESTABELECIMENTO NOCIVO
// ============================================================================
class HarmfulBusinessType {
    // Tipos de negocio que destroem vidas.
    GAMBLING = "jogo_de_azar"  // cassino, bingo, loterca, bets;
    LOAN_SHARK = "agiotagem"  // emprestimo abusivo (730% a.a.);
    PYRAMID = "piramide"  // marketing multinivel fraudulento;
    WEAPONS_TRADE = "comercio_armas"  // venda de armas (! FabLab);
    DRUG_TRAFFICKING = "trafico_drogas"  // narcotrafico;
    HUMAN_TRAFFICKING = "trafico_humanos"  // trafico de pessoas;
    EXPLOITATION_LABOR = "trabalho_escravo"  // exploracao trabalhadora;
    CHILD_EXPLOITATION = "exploracao_infantil";
    ORGAN_TRAFFICKING = "trafico_orgaos";
    FAKE_MEDICINE = "remedio_falso"  // venda de remedio falsificado;
    PREDATORY_LENDING = "credito_predatorio"  // banco 730% + cartao 1200%;
    MULTI_LEVEL_MARKETING = "mmn_predatorio"  // MMN que suga participante;
    CIGARETTE_TRADE = "comercio_tabaco"  // venda de cigarro (mata 8M/ano);
    ILLEGAL_MINING = "mineracao_ilegal"  // garimpo que destroi natureza;
    DEFENSESTATION = "desmatamento"  // madeira ilegal;
    VOTE_BUYING = "compra_voto"  // corrupcao eleitoral;
    BRIBERY = "propina"  // suborno/corrupcao;
    MISINFORMATION_VENDOR = "vendedor_desinformacao"  // canal que mente por lucro;
    FAKE_NEWS_FARM = "farma_fake_news"  // fabrica de mentiras;
    PREDATORY_INFLUENCER = "influenciador_predatorio"  // manipula por lucro;
class HarmLevel {
    DESTRUCTIVE = ("destrutivo", 5)  // destroi vidas em massa;
    VERY_HARMFUL = ("muito_nocivo", 4)  // causa dano grave;
    HARMFUL = ("nocivo", 3)  // causa dano real;
    DECEPTIVE = ("enganoso", 2)  // engana para lucrar;
    QUESTIONABLE = ("questionavel", 1)  // precisa analise;
class BusinessAction {
    PROHIBIT = "proibir"  // fechado imediatamente;
    CONVERT = "converter"  // transformar em algo util;
    REPLACE = "substituir"  // trocar por open equivalente;
    REGULATE_STRICT = "regular_estrito"  // permitir com regras duras;
    MONITOR = "monitorar"  // observar de perto;
// ============================================================================
// 2. ESTABELECIMENTO NOCIVO REGISTRADO
// ============================================================================
// decorador: @dataclass
class HarmfulBusiness {
    // Um negocio nocivo identificado.
    business_id: texto;
    name: texto // nome do negocio;
    business_type: HarmfulBusinessType;
    const harm_level = HarmLevel.HARMFUL;
    const description = "";
    const victims_estimated = 0 // quantas pessoas afeta;
    const money_drained_monthly = ""  // quanto suga por mes;
    // Acao
    const action = BusinessAction.PROHIBIT;
    const replacement = ""  // open equivalente;
    const conversion_target = ""  // para que converter;
    // Status
    const status = "identificado"  // identificado, votado, fechado, convertido;
    const closed_date = "";
// ============================================================================
// 3. CATÁLOGO DE NEGÓCIOS NOCIVOS
// ============================================================================
const HARMFUL_BUSINESSES = [;
    // === JOGO DE AZAR ===
    HarmfulBusiness(;
        "HB-001", "Casas de Apostas (Bets)", HarmfulBusinessType.GAMBLING,;
        HarmLevel.DESTRUCTIVE,;
        description = (;
            "Apostas esportivas online (Bet365, Betano, etc). ";
            "Exploram vicio. 70% dos apostadores perdem. ";
            "Brasileiros perderam R$ 20 bilhoes em 2023. ";
            "Familias destruidas. Suicidios. Dividas. ";
            "Marketing agressivo em jogadores de futebol.";
        ),;
        victims_estimated = 50000000,;
        money_drained_monthly = "R$ 2 bilhoes/mes",;
        action = BusinessAction.REPLACE,;
        replacement = "OpenCoin: Liga Comunitaria (jogar > assistir > apostar)",;
        status = "identificado",;
    ),;
    HarmfulBusiness(;
        "HB-002", "Cassinos Fisicos", HarmfulBusinessType.GAMBLING,;
        HarmLevel.VERY_HARMFUL,;
        description = "Cassinos fisicos. Mesma logica predatoria das bets.",;
        victims_estimated = 2000000,;
        replacement = "OpenCoin: Casa de Habilidade (xadrez, estrategia, fabricar)",;
    ),;
    // === AGIOTAGEM / CRÉDITO PREDATÓRIO ===
    HarmfulBusiness(;
        "HB-003", "Agiotas", HarmfulBusinessType.LOAN_SHARK,;
        HarmLevel.DESTRUCTIVE,;
        description = (;
            "Emprestimo informal a juros abusivos (10-30% ao mes). ";
            "Escrotiza devedor. Ameaca familia. Mata. ";
            "Pega quem banco ! empresta (vulneravel).";
        ),;
        victims_estimated = 5000000,;
        money_drained_monthly = "R$ 500 milhoes/mes",;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenCredit (credito a juros ZERO)",;
    ),;
    HarmfulBusiness(;
        "HB-004", "Bancos (juros 730% a.a. cartao)", HarmfulBusinessType.PREDATORY_LENDING,;
        HarmLevel.DESTRUCTIVE,;
        description = (;
            "Cartao de credito: 730% ao ano (12% ao mes). ";
            "Cheque especial: 300% ao ano. ";
            "Bancos lucram R$ 100 bilhoes/ano com juros. ";
            "Endividam milhoes. 'Fique rico' dizem -- enquanto voce empobrece.";
        ),;
        victims_estimated = 70000000,;
        money_drained_monthly = "R$ 8 bilhoes/mes",;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenCredit (sem juros. sem divida. credito expira.)",;
    ),;
    HarmfulBusiness(;
        "HB-005", "Financeiras (crediario)", HarmfulBusinessType.PREDATORY_LENDING,;
        HarmLevel.VERY_HARMFUL,;
        description = "Crediario de loja. Juros 200-500%. Toma bem de volta.",;
        victims_estimated = 15000000,;
        replacement = "OpenCredit",;
    ),;
    // === PIRÂMIDE / MMN ===
    HarmfulBusiness(;
        "HB-006", "Esquemas Piramide", HarmfulBusinessType.PYRAMID,;
        HarmLevel.DESTRUCTIVE,;
        description = (;
            "Piramide financeira. Promessa de lucro impossivel. ";
            "Quem entra primeiro ganha (com dinheiro de quem entra depois). ";
            "Quem entra por ultimo perde tudo. ";
            "Brasil: Krestinski, InHH, Telexfree -- bilhoes roubados.";
        ),;
        victims_estimated = 3000000,;
        money_drained_monthly = "R$ 200 milhoes/mes",;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenCoin (sem ganho facil. Trabalho = credito.)",;
    ),;
    HarmfulBusiness(;
        "HB-007", "MMN Predatorio", HarmfulBusinessType.MULTI_LEVEL_MARKETING,;
        HarmLevel.VERY_HARMFUL,;
        description = (;
            "Marketing multinivel ( Herbalife-style). ";
            "85% perdem dinheiro. Foco em recrutar, ! vender. ";
            "Explora amigo/familia. Promessa de liberdade financeira. ";
            "Realidade: estoque na garagem && divida.";
        ),;
        victims_estimated = 5000000,;
        money_drained_monthly = "R$ 300 milhoes/mes",;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenLaborRelay (trabalho real. Sem recrutar.)",;
    ),;
    // === TABACO ===
    HarmfulBusiness(;
        "HB-008", "Industria do Tabaco", HarmfulBusinessType.CIGARETTE_TRADE,;
        HarmLevel.DESTRUCTIVE,;
        description = (;
            "Cigarro mata 8 milhoes/ano no mundo. ";
            "No Brasil: 160 mil mortes/ano. ";
            "Industria sabia que matava && escondeu por decadas. ";
            "Vende doenca. Lucra com morte.";
        ),;
        victims_estimated = 20000000,;
        money_drained_monthly = "R$ 1 bilhao/mes (em tratamento de doenca)",;
        action = BusinessAction.CONVERT,;
        conversion_target = "Fazendas de tabaco -> agricultura de alimentos (OpenAgrarian)",;
        replacement = "OpenHealth: tratamento para parar de fumar (ZERO custo)",;
    ),;
    // === MINERAÇÃO ILEGAL ===
    HarmfulBusiness(;
        "HB-009", "Garimpo Ilegal (Amazonia)", HarmfulBusinessType.ILLEGAL_MINING,;
        HarmLevel.DESTRUCTIVE,;
        description = (;
            "Garimpo ilegal na Amazonia. Destroi floresta. ";
            "Contamina rios com mercurio. ";
            "Envenena indigenas. Financia crime organizado. ";
            "Yanomami: 570 toneladas de mercurio despejadas.";
        ),;
        victims_estimated = 300000,;
        money_drained_monthly = "N/A (destroi natureza)",;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenSustainability: mineracao sustentavel controlada (se necessario)",;
    ),;
    // === DESMATAMENTO ===
    HarmfulBusiness(;
        "HB-010", "Madeira Ilegal", HarmfulBusinessType.DEFENSESTATION,;
        HarmLevel.DESTRUCTIVE,;
        description = "Desmatamento para madeira. Mata Amazonia. Mata Cerrado.",;
        victims_estimated = 210000000, // todos brasileiros (futuro);
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenSustainability: madeira de reflorestamento (CC0)",;
    ),;
    // === FAKE NEWS / DESINFORMACAO ===
    HarmfulBusiness(;
        "HB-011", "Fazendas de Fake News", HarmfulBusinessType.FAKE_NEWS_FARM,;
        HarmLevel.VERY_HARMFUL,;
        description = (;
            "Fazendas de desinformacao. Espalham mentira por lucro. ";
            "Monetizam odio, medo, polemica. ";
            "Destroem democracia. Manipulam eleicoes. ";
            "OpenContentPolicy + OpenHistory fact-check bloqueiam.";
        ),;
        victims_estimated = 210000000,;
        money_drained_monthly = "R$ 500 milhoes/mes (em engano social)",;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenTV (noticia VERIFICADA) + OpenMentalHygiene (bloqueia nocivo)",;
    ),;
    // === INFLUENCIADOR PREDATORIO ===
    HarmfulBusiness(;
        "HB-012", "Influenciadores Predatorios", HarmfulBusinessType.PREDATORY_INFLUENCER,;
        HarmLevel.VERY_HARMFUL,;
        description = (;
            "Influenciador que manipula para lucrar. ";
            "Vende curso inutil. Promete riqueza. Cria ansiedade. ";
            "Casos: Felca (saude mental nociva), coaches deriqueza, ";
            "fake gurus. OpenMentalHygiene bloqueia.";
        ),;
        victims_estimated = 30000000,;
        money_drained_monthly = "R$ 200 milhoes/mes",;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenEducation (gratuito) + OpenMentalHygiene (bloqueia predador)",;
    ),;
    // === TRABALHO ESCRAVO ===
    HarmfulBusiness(;
        "HB-013", "Trabalho Escravo Contemporaneo", HarmfulBusinessType.EXPLOITATION_LABOR,;
        HarmLevel.DESTRUCTIVE,;
        description = (;
            "Trabalho em condicoes de escravidao. ";
            "Fazendas, confecoes, construcao. ";
            "Divida perpetua. Retencao de documentos. ";
            "Ameaca. Isolamento. Brasil tem 3000+ resgatados/ano (subnotificado).";
        ),;
        victims_estimated = 50000,;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenLaborPolicy (base 1.0. Sem divida. Sem escravidao.)",;
    ),;
    // === EXPLORACAO INFANTIL ===
    HarmfulBusiness(;
        "HB-014", "Exploracao Sexual de Criancas", HarmfulBusinessType.CHILD_EXPLOITATION,;
        HarmLevel.DESTRUCTIVE,;
        description = "Crime hediondo. Destroi vida de criancas. Crime permanente.",;
        victims_estimated = 500000,;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenPenalRevision (restricao permanente -- crime hediondo)",;
    ),;
    // === REMEDIO FALSO ===
    HarmfulBusiness(;
        "HB-015", "Comercio de Remedios Falsos", HarmfulBusinessType.FAKE_MEDICINE,;
        HarmLevel.DESTRUCTIVE,;
        description = (;
            "Vende remedio false. Mata. ";
            "Quem ! tem dinheiro compra mais barato && morre. ";
            "OpenPharma resolve: remedio VERDADEIRO a ZERO custo.";
        ),;
        victims_estimated = 2000000,;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenPharma (remedio VERDADEIRO, ZERO custo, FabLab nacional)",;
    ),;
    // === COMPRA DE VOTO ===
    HarmfulBusiness(;
        "HB-016", "Compra de Votos", HarmfulBusinessType.VOTE_BUYING,;
        HarmLevel.VERY_HARMFUL,;
        description = "Político compra voto. Destroi democracia. Corrompe.",;
        victims_estimated = 210000000,;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenDemocracy (voto secreto, transparente, CC0)",;
    ),;
    // === PROPINA ===
    HarmfulBusiness(;
        "HB-017", "Corrupcao/Propina", HarmfulBusinessType.BRIBERY,;
        HarmLevel.DESTRUCTIVE,;
        description = (;
            "Propina desvia R$ 100+ bilhoes/ano do pais. ";
            "Hospital sem recurso. Escola sem livro. Estrada sem asfalto. ";
            "Republica: transparencia TOTAL. Tudo CC0. Tudo auditavel.";
        ),;
        victims_estimated = 210000000,;
        money_drained_monthly = "R$ 8 bilhoes/mes",;
        action = BusinessAction.PROHIBIT,;
        replacement = "OpenDemocracy + OpenHistory (transparencia total CC0)",;
    ),;
];
// ============================================================================
// 4. VOTACAO DA ASSEMBLEIA
// ============================================================================
run_business_assembly(n_voters: inteiro = 10000) {
    // Assembleia vota quais negocios fechar.
    business_votes = {};
    for (const biz of HARMFUL_BUSINESSES) {
        // Simular votacao (quase todos concordam em fechar)
        close_votes = random.randint(8000, 9800);
        keep_votes = n_voters - close_votes;
        business_votes[biz.business_id] = {
            "name": biz.name,;
            "close_votes": close_votes,;
            "keep_votes": keep_votes,;
            "pct_close": "{close_votes/n_voters*100:.0f}%",;
            "approved": close_votes > n_voters * 0.6,;
        };
    return {;
        "question": (;
            "Estabelecimentos que destroem vidas devem ser PROIBIDOS ";
            "&& CONVERTIDOS em algo util?";
        ),;
        "business_votes": business_votes,;
        "total_businesses": .length(HARMFUL_BUSINESSES),;
        "result": "APROVADO -- todos os nocivos serao fechados",;
    };
// ============================================================================
// 5. MOTOR DE PROIBICAO
// ============================================================================
class ProhibitionEngine {
    // Motor que proibe, converte e substitui negocios nocivos.
    COMO FUNCIONA:;
    1. IDENTIFICA: mapeia negocios que destroem vidas;
    2. CLASSIFICA: nivel de dano (1-5);
    3. VOTA: assembleia decide (P4);
    4. PROIBE: fechado imediatamente;
    5. CONVERTE: edificio/vaga -> algo util;
    6. SUBSTITUI: oferece open equivalente;
    7. ACOMPANHA: ex-dono reintegrado (se quiser);
    O QUE ACONTECE COM QUEM TRABALHAVA NO NEGOCIO NOCIVO:;
    - Nao && punido (! sabia que era nocivo, || precisava);
    - Recebe OpenKit completo;
    - OpenLaborRelay: trabalho alternativo;
    - OpenEducation: aprende nova skill;
    - OpenReintegration: se era crime organizado;
    O QUE ACONTECE COM O PREDADOR (dono):;
    - Se sabia que era nocivo && lucrava: OpenPenalRevision;
    - Se era apenas negligente: OpenCivicEducation;
    - Bens convertidos para bem comum (CC0);
    //
    __init__(self) {
        self.businesses: {texto: HarmfulBusiness} = {
            b.business_id: b para b em HARMFUL_BUSINESSES;
        };
        self.closed_count: inteiro = 0;
        self.converted_count: inteiro = 0;
    list_harmful(self, severity: inteiro = 0) {
        // Lista negocios nocivos.
        biz_list = self.businesses.values();
        if (severity) {
            biz_list = [b para b em biz_list if b.harm_level.value[1] >= severity];
        return [;
            {
                "id": b.business_id,;
                "name": b.name,;
                "type": b.business_type.value,;
                "harm": b.harm_level.value[0],;
                "harm_num": b.harm_level.value[1],;
                "victims": "{b.victims_estimated:,}",;
                "money": b.money_drained_monthly,;
                "action": b.action.value,;
                b.replacement ? "replacement": b.replacement[:40] : "",;
            };
            para b em biz_list {
        ];
    close_business(self, business_id: texto) {
        // Fecha estabelecimento nocivo.
        biz = self.businesses.get(business_id);
        if (! biz) {
            return {"error": "Nao encontrado"};
        biz.status = "fechado";
        biz.closed_date = datetime.now().isoformat();
        self.closed_count += 1;
        // O que acontece com os trabalhadores
        worker_plan = {
            "trabalhadores": "Recebem OpenKit + OpenLaborRelay + OpenEducation",;
            "nao_punidos": "Trabalhador ! && punido. Precisava trabalhar.",;
            "reintegracao": "Se era crime: OpenReintegration",;
        };
        // O que acontece com o predador
        owner_plan = {
            "predador": "OpenPenalRevision se lucrava conscientemente",;
            "bens": "Convertidos para bem comum (CC0)",;
            "reintegracao": "OpenReintegration se quiser mudar",;
        };
        // Conversao do espaco fisico
        conversion = self._convert_space(biz);
        return {;
            "business": biz.name,;
            "status": "FECHADO",;
            "harm_level": biz.harm_level.value[0],;
            "victims_protected": "{biz.victims_estimated:,}",;
            "replacement": biz.replacement,;
            "worker_plan": worker_plan,;
            "owner_plan": owner_plan,;
            "space_converted": conversion,;
            "message": (;
                "{biz.name} FECHADO. ";
                "Protegia {biz.victims_estimated:,} potenciais vitimas. ";
                "Substituido por: {biz.replacement[:50]}. ";
                "Espaco convertido: {conversion['new_use']}. ";
                "Trabalhadores: ! punidos. Reinseridos.";
            ),;
        };
    _convert_space(self, biz: HarmfulBusiness) {
        // Converte espaco fisico do negocio fechado em algo util.
        conversions = {
            HarmfulBusinessType.GAMBLING: {
                "new_use": "OpenNightLife: centro comunitario + OpenGames",;
                "how": "Mesa de aposta -> mesa de jogo cooperativo. ";
                    "Slot machine -> OpenTerminal.",;
            },;
            HarmfulBusinessType.LOAN_SHARK: {
                "new_use": "OpenCredit: ponto de credito sem juros",;
                "how": "Balcão de agiota -> OpenTerminal de credito.",;
            },;
            HarmfulBusinessType.PREDATORY_LENDING: {
                "new_use": "OpenHealth: posto de saude comunitario",;
                "how": "Agencia bancaria -> clinica nivel Sirio-Libanes.",;
            },;
            HarmfulBusinessType.PYRAMID: {
                "new_use": "OpenEducation: centro de aprendizado",;
                "how": "Sala de apresentacao piramide -> sala de aula aberta.",;
            },;
            HarmfulBusinessType.MULTI_LEVEL_MARKETING: {
                "new_use": "OpenMarketplace: cooperativa de produtos",;
                "how": "Estoque de produto MMN -> cooperativa de produtos reais.",;
            },;
            HarmfulBusinessType.CIGARETTE_TRADE: {
                "new_use": "OpenAgrarian: fazenda de alimentos",;
                "how": "Platacao de tabaco -> plantacao de alimentos.",;
            },;
            HarmfulBusinessType.ILLEGAL_MINING: {
                "new_use": "Area protegida (reflorestamento)",;
                "how": "Garimpo -> area protegida + reflorestamento.",;
            },;
        };
        return conversions.get(biz.business_type, {;
            "new_use": "Centro comunitario da Republica",;
            "how": "Convertido para uso comunitario.",;
        });
    financial_impact(self) {
        // Impacto financeiro de fechar negocios nocivos.
        return {;
            "jogo_de_azar_drenado": "R$ 2 bilhoes/mes -> ZERO (OpenCoin substitui)",;
            "juros_bancarios_drenados": "R$ 8 bilhoes/mes -> ZERO (OpenCredit substitui)",;
            "mmn_piramides_drenado": "R$ 500 milhoes/mes -> ZERO",;
            "corrupcao_desviada": "R$ 8 bilhoes/mes -> ZERO (transparencia)",;
            "total_mensal_economizado": "R$ 18+ bilhoes/mes",;
            "total_anual_economizado": "R$ 216+ bilhoes/ano",;
            "message": (;
                "Fechar negocios nocivos NAO custa. ECONOMIZA. ";
                "R$ 216 bilhoes/ano que iam para predador -> ";
                "vai para cidadao (OpenCredit, OpenHealth, OpenEducation).";
            ),;
        };
    stats(self) {
        return {;
            "total_identificados": .length(self.businesses),;
            "fechados": self.closed_count,;
            "convertidos": self.converted_count,;
            "vitimas_protegidas_total": soma(b.victims_estimated para b em self.businesses.values()),;
            "dinheiro_economizado_mes": "R$ 18+ bilhoes",;
        };
// ============================================================================
// 6. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = ProhibitionEngine();
    console.log("=" * 80);
    console.log("  OPENPROHIBITEDBUSINESS -- PROIBICAO DE ESTABELECIMENTOS NOCIVOS");
    console.log("  Quem destroi vida ! tem lugar. Fechado. Convertido. Substituido.");
    console.log("=" * 80);
    // === 1. ASSEMBLEIA ===
    console.log("\n\n  === 1. ASSEMBLEIA CONSTITUINTE ===\n");
    result = run_business_assembly(10000);
    console.log("  PERGUNTA: {result['question']}");
    console.log("  RESULTADO: {result['result']}");
    // === 2. NEGOCIOS NOCIVOS IDENTIFICADOS ===
    console.log("\n\n  === 2. NEGOCIOS NOCIVOS ({len(engine.businesses)}) ===\n");
    console.log("  {'ID':<8} {'Negocio':<35} {'Dano':<15} {'Vitimas':>12} {'Acao'}");
    console.log("  {'-'*85}");
    para b em ordene(engine.businesses.values(), {
                    key = (x) -> -x.harm_level.value[1]):;
        console.log("  {b.business_id:<8} {b.name[:34]:<35} {b.harm_level.value[0]:<15} ";
            "{b.victims_estimated:>12,} {b.action.value}");
    // === 3. FECHAR CASA DE APOSTAS ===
    console.log("\n\n  === 3. FECHANDO: CASAS DE APOSTAS ===\n");
    close1 = engine.close_business("HB-001");
    console.log("  {close1['business']}: {close1['status']}");
    console.log("  Vitimas protegidas: {close1['victims_protected']}");
    console.log("  Substituido por: {close1['replacement']}");
    console.log("  Espaco convertido: {close1['space_converted']['new_use']}");
    // === 4. FECHAR BANCOS PREDATORIOS ===
    console.log("\n\n  === 4. FECHANDO: BANCOS PREDATORIOS ===\n");
    close2 = engine.close_business("HB-004");
    console.log("  {close2['business']}: {close2['status']}");
    console.log("  Vitimas: {close2['victims_protected']}");
    console.log("  Substituido: {close2['replacement']}");
    console.log("  Espaco: {close2['space_converted']['new_use']}");
    // === 5. FECHAR TODOS ===
    console.log("\n\n  === 5. FECHANDO TODOS OS NOCIVOS ===\n");
    for (const bid of list(engine.businesses.keys())) {
        if (engine.businesses[bid].status != "fechado") {
            r = engine.close_business(bid);
            console.log("  [FECHADO] {r['business']:<35} -> {r['space_converted']['new_use']}");
    // === 6. IMPACTO FINANCEIRO ===
    console.log("\n\n  === 6. IMPACTO FINANCEIRO DE FECHAR NOCIVOS ===\n");
    impact = engine.financial_impact();
    para cada (k, v) em impact.items(): {
        if (k != "message") {
            console.log("  {k:<35} {v}");
    console.log("\n  {impact['message']}");
    // === 7. STATS ===
    console.log("\n\n  === 7. ESTATISTICAS ===\n");
    s = engine.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<35} {v}");
    // === FILOSOFIA ===
    console.log("\n\n{'='*80}");
    console.log("  FILOSOFIA: PROIBICAO DE NOCIVOS");
    console.log("{'='*80}");
    console.log(""";
ESTABELECIMENTO QUE DESTROI VIDA = SEM LUGAR.;
    Cassino que vicia? Fecha.;
    Banco que endivida? Fecha.;
    Agiota que escrotiza? Fecha.;
    Piramide que rouba? Fecha.;
    Tabaco que mata? Converte.;
    Garimpo que envenena? Fecha.;
    Fake news que manipula? Fecha.;
    Influenciador que predador? Fecha.;
O QUE ACONTECE COM QUEM TRABALHAVA:;
    Trabalhador: ! PUNIDO. Recebe OpenKit + OpenLaborRelay + OpenEducation.;
    Precisava trabalhar. Agora tem trabalho de verdade (base 1.0).;
    Se era crime: OpenReintegration (ressocializacao completa).;
O QUE ACONTECE COM O ESPACO:;
    Casino -> centro comunitario (OpenNightLife + OpenGames);
    Banco -> posto de saude (OpenHealth Sirio-Libanes);
    Agiota -> OpenTerminal de credito sem juros;
    Piramide -> OpenEducation (centro de aprendizado);
    Tabaco -> fazenda de alimentos (OpenAgrarian);
O QUE SUBSTITUI:;
    Bets -> OpenCoin (Liga Comunitaria: jogar > apostar);
    Bancos -> OpenCredit (credito ZERO juros);
    Agiotas -> OpenCredit (sem agiota necessario);
    Piramides -> OpenLaborRelay (trabalho real);
    Tabaco -> OpenHealth (tratamento para parar);
    Fake news -> OpenTV (noticia VERIFICADA);
IMPACTO FINANCEIRO:;
    Fechar nocivos ! custa. ECONOMIZA.;
    R$ 216+ bilhoes/ano que iam para predadores;
    -> vai para cidadaos (OpenCredit, OpenHealth, OpenEducation).;
A LOGICA:;
    Predador: "voce precisa de mim (empresto dinheiro, oficio diversao).";
    Republica: "voce NAO precisa dele. OpenCredit empresta a ZERO. ";
    "OpenCoin oferece jogo sem perder. OpenHealth trata vicio. ";
    "O predador NAO oferece nada que a Republica ! ofereca MELHOR.";
PRINCIPIOS:;
    const P1 = contra P1 (anti-elitismo). Proibido.;
    P2: Viciar/endividar = violencia contra corpo/mente. P2 protege.;
    P3: Trabalhador reinserido (! punido). Predador: OpenPenalRevision.;
    P4: Assembleia vota quais fechar. Povo decide.;
// )
    console.log("{'='*80}");
    console.log("  OpenProhibitedBusiness: {s['fechados']}/{s['total_identificados']} fechados. ";
        "Vitimas protegidas: {s['vitimas_protegidas_total']:,}.");
    console.log("  Quem destroi vida ! tem lugar.");
    console.log("{'='*80}");
