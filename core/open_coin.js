// OpenCoin -- Sistema que Substitui Bets, Cassinos e Criptos -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenCoin -- Sistema que Substitui Bets, Cassinos && Criptos;
=============================================================;
"Na Republica ! ha aposta. Nao ha cassino. Nao ha cripto.;
Ha OpenCoin: a unica moeda que ! && moeda.";
O PROBLEMA QUE O COIN RESOLVE:;
Cassino/aposta/cripto existem porque as pessoas querem:;
1. Sentir que ganharam algo (recompensa);
2. Ter esperanca de mudar de vida;
3. Sentir adrenalina sem dano real;
O capitalismo cobra para dar isso.;
A Republica da de graca, sem explorar.;
O QUE O OPENCOIN FAZ:;
- Substitui apostas por DESAFIOS REAIS (ajude a comunidade, ganhe);
- Substitui cassino por JOGOS DE HABILIDADE (sem dinheiro real);
- Substitui cripto por CREDITO DE ACESSO (que expira, ! acumula);
- Adrenalina vem de CONQUISTA REAL, ! de perda financeira;
- Zero custo. Zero exploracao. Zero dependencia.;
SE ALGUEM TENTA JOGAR/ apostar, o OpenCoin redireciona para:;
- Desafio comunitario (construir algo util);
- Jogo de habilidade (sem aposta);
- Aprendizado (ganha credito por aprender);
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, deque de collections
// importa datetime de datetime
// ============================================================================
// 1. O QUE O OPENCOIN SUBSTITUI
// ============================================================================
class ViceType {
    // Vicios que o OpenCoin substitui.
    SPORTS_BETTING = "aposta_esportiva"  // Bet365, Sportingbet;
    CASINO = "cassino"  // slots, roleta, blackjack;
    CRYPTO_TRADING = "cripto"  // Bitcoin, Ethereum speculation;
    LOTTERY = "loteria"  // Mega-Sena, PowerBall;
    POKER = "poker"  // poker online;
    GACHA_LOOTBOX = "lootbox"  // caixas de itens em jogos;
    DAY_TRADING = "day_trading"  // bolsa de valores;
class ViceHook {
    // O que faz cada vicio viciar (psicologia).
    DOPAMINE_UNPREDICTABLE = "dopamina_imprevisivel"  // recompensa aleatoria;
    NEAR_MISS = "quase_ganhei"  // "foi por pouco";
    LOSS_CHASING = "perseguindo_perda"  // tentar recuperar;
    SOCIAL_PROOF = "prova_social"  // "ele ganhou, eu tambem posso";
    ILLUSION_CONTROL = "ilusao_controle"  // acha que controla o acaso;
    SUNK_COST = "custo_afundado"  // ja investi muito, ! posso parar;
    ESCAPE = "fuga_realidade"  // esquecer problemas;
// ============================================================================
// 2. A REPLACEMENT MATRIX
// ============================================================================
// decorador: @dataclass
class ViceReplacement {
    // Como o OpenCoin substitui um vicio.
    vice: ViceType;
    hooks: [ViceHook];
    replacement_activity: texto;
    replacement_description: texto;
    reward_type: texto // credito, reconhecimento, habilidade;
    adrenaline_source: texto // de onde vem a adrenalina saudavel;
const REPLACEMENTS = [;
    ViceReplacement(;
        ViceType.SPORTS_BETTING,;
        [ViceHook.DOPAMINE_UNPREDICTABLE, ViceHook.SOCIAL_PROOF,;
        ViceHook.NEAR_MISS],;
        "Liga Comunitaria de Esportes",;
        "Em vez de apostar no time, PARTICIPE. Jogue pelada comunitaria. ";
        "A adrenalina vem de jogar de verdade, ! de assistir.",;
        "credito + saude",;
        "Esforco fisico real + trabalho em equipe";
    ),;
    ViceReplacement(;
        ViceType.CASINO,;
        [ViceHook.DOPAMINE_UNPREDICTABLE, ViceHook.LOSS_CHASING,;
        ViceHook.ESCAPE],;
        "Casa de Habilidade",;
        "Jogos de habilidade pura (xadrez, damas, quebra-cabeca, estrategia). ";
        "Sem aposta. A recompensa && MELHORAR. Adrenalina de征服 real.",;
        "credito por habilidade + reconhecimento",;
        "Desafio mental real, recompensa por maestria";
    ),;
    ViceReplacement(;
        ViceType.CRYPTO_TRADING,;
        [ViceHook.ILLUSION_CONTROL, ViceHook.SUNK_COST,;
        ViceHook.DOPAMINE_UNPREDICTABLE],;
        "OpenCoin Market Simulator",;
        "Simulador de mercado com dados reais mas SEM dinheiro real. ";
        "Aprende economia sem arriscar familia. ";
        "Quem pontua alto ganha credito de acesso por conhecimento.",;
        "credito por aprendizado",;
        "Intelecto + previsao real, consequencias virtuais";
    ),;
    ViceReplacement(;
        ViceType.LOTTERY,;
        [ViceHook.DOPAMINE_UNPREDICTABLE, ViceHook.SOCIAL_PROOF],;
        "Sorteio Democratico",;
        "Sorteio real onde TODOS tem chance igual (! proporcional a bilhete). ";
        "Sorteia-se credito de acesso, bens escassos, oportunidades. ";
        "Zero custo para participar. Zero perda.",;
        "credito + bem escasso (sem comprar bilhete)",;
        "Esperanca real, sem custo financeiro";
    ),;
    ViceReplacement(;
        ViceType.POKER,;
        [ViceHook.DOPAMINE_UNPREDICTABLE, ViceHook.ILLUSION_CONTROL],;
        "Liga de Estrategia",;
        "Xadrez, Go, jogos de estrategia. Mesma profundidade tactica ";
        "sem dinheiro. Torneios comunitarios com credito de acesso.",;
        "credito + reconhecimento",;
        "Competicao intelectual real";
    ),;
    ViceReplacement(;
        ViceType.GACHA_LOOTBOX,;
        [ViceHook.DOPAMINE_UNPREDICTABLE, ViceHook.SUNK_COST],;
        "Oficina de Criacao",;
        "Em vez de abrir caixa para conseguir item virtual, CRIE o item. ";
        "FabLab, OpenProduct. A recompensa de fabricar && sua.",;
        "artefato real + credito",;
        "Criacao real > consumo virtual";
    ),;
    ViceReplacement(;
        ViceType.DAY_TRADING,;
        [ViceHook.ILLUSION_CONTROL, ViceHook.LOSS_CHASING,;
        ViceHook.SUNK_COST],;
        "Simulador + Aprendizado Economico",;
        "Plataforma educacional de economia onde se aprende ";
        "com dados reais. Pontua por acerto de previsao, ! por dinheiro. ";
        "Recompensa: credito de acesso + conhecimento util.",;
        "credito + conhecimento",;
        "Intelecto aplicado a economia real";
    ),;
];
// ============================================================================
// 3. OPENCOIN (A MOEDA QUE NAO E MOEDA)
// ============================================================================
class CoinTransactionType {
    CHALLENGE_REWARD = "desafio"  // ganhou desafio comunitario;
    SKILL_REWARD = "habilidade"  // ganhou jogo de habilidade;
    LEARNING_REWARD = "aprendizado"  // completou curso/licao;
    LOTTERY_WIN = "sorteio"  // ganhou sorteio democratico;
    TRANSFER_IN = "recebido"  // recebeu de outro;
    TRANSFER_OUT = "enviado"  // enviou para outro;
    EXPIRED = "expirado"  // ! usado no ciclo;
    CONVERTED_TO_CREDIT = "convertido"  // virou credito de acesso;
// decorador: @dataclass
class CoinTransaction {
    tx_id: texto;
    citizen: texto;
    type: CoinTransactionType;
    amount: flutuante;
    const description = "";
    const timestamp = field(default_factory=() -> datetime.now().timestamp());
class OpenCoin {
    // A moeda que NAO e moeda da Republica.
    DIFERENCA vs cripto/dinheiro:;
    - ! acumula indefinidamente (expira);
    - ! && minerada (ganha-se por acao real);
    - ! tem valor especulativo (1 OpenCoin = 1 credito de acesso);
    - ! && transferivel livremente (so em casos especificos);
    - ! pode ser apostada (aposta ! existe);
    - ! gera juros (guardar ! da nada);
    COMO SE GANHA:;
    - Desafio comunitario (ajudou a construir? ganhou);
    - Habilidade (ganhou torneio de xadrez? ganhou);
    - Aprendizado (completou curso? ganhou);
    - Sorteio democratico (todos participam gratis);
    COMO SE GASTA:;
    - Converter em credito de acesso (1:1);
    - Trocar por bem escasso no catalogo;
    - ! pode: apostar, especular, acumular, transferir para acumular;
    //
    __init__(self) {
        self.balances: {texto: flutuante} = defaultdict(flutuante);
        self.transactions: [CoinTransaction] = [];
        self.expiry_cycles_days: inteiro = 90 // expira em 90 dias se ! usar;
        self.mining_possible: logico = false // NUNCA;
        self.staking_possible: logico = false // NUNCA;
        self.betting_possible: logico = false // NUNCA;
        self.speculation_possible: logico = false // NUNCA;
    funcao earn(self, citizen: texto, amount: flutuante,
            reason: CoinTransactionType, description: texto = "") -> {texto: qualquer}:;
        // Cidadao ganha OpenCoin por acao real.
        tx = CoinTransaction(;
            tx_id = hashlib.md5("{citizen}{amount}{time.time()}".encode()).hexdigest()[:8],;
            citizen = citizen, type=reason, amount=amount, description=description,;
        );
        self.balances[citizen] += amount;
        self.transactions.append(tx);
        return {;
            "earned": true,;
            "citizen": citizen,;
            "amount": amount,;
            "reason": reason.value,;
            "balance": self.balances[citizen],;
            "note": "Ganho por ACAO REAL. NAO por sorte || aposta.",;
        };
    convert_to_credit(self, citizen: texto, amount: flutuante) {
        // Converte OpenCoin em credito de acesso (1:1).
        if (self.balances[citizen] < amount) {
            return {"error": "Saldo insuficiente"};
        self.balances[citizen] -= amount;
        self.transactions.append(CoinTransaction(;
            tx_id = hashlib.md5("{citizen}conv{time.time()}".encode()).hexdigest()[:8],;
            citizen = citizen, type=CoinTransactionType.CONVERTED_TO_CREDIT,;
            amount = amount, description="Convertido em credito de acesso",;
        ));
        return {;
            "converted": true,;
            "from": "OpenCoin",;
            "to": "credito de acesso",;
            "rate": "1:1",;
            "credit_earned": amount,;
        };
    funcao attempt_bet(self, citizen: texto, amount: flutuante,
                    bet_type: ViceType) -> {texto: qualquer}:;
        // Alguem tenta apostar. Sistema REDIRECIONA.
        replacement = next((r para r em REPLACEMENTS if r.vice == bet_type), null);
        return {;
            "bet_attempted": false,;
            "blocked": true,;
            "reason": "Apostas NAO EXISTEM na Republica.",;
            replacement ? "redirect": replacement.replacement_activity : "Desafio Comunitario",;
            "redirect_description": (replacement.replacement_description;
                                    if replacement else ""),;
            "message": (;
                "Voce queria apostar. A Republica te oferece algo MELHOR: ";
                "{replacement.replacement_activity if replacement else 'Desafio'}. ";
                "Mesma adrenalina. Zero perda. Recompensa real.";
            ),;
        };
    expire_all(self) {
        // Expira todos os saldos nao usados no ciclo.
        expired_total = 0;
        expired_citizens = 0;
        para cada (citizen, balance) em list(self.balances.items()): {
            if (balance > 0) {
                expired_total = expired_total + balance;
                expired_citizens = expired_citizens + 1;
                self.transactions.append(CoinTransaction(;
                    tx_id = hashlib.md5("{citizen}exp{time.time()}".encode()).hexdigest()[:8],;
                    citizen = citizen, type=CoinTransactionType.EXPIRED,;
                    amount = balance, description="Expirado (! usado no ciclo)",;
                ));
                self.balances[citizen] = 0;
        return {;
            "expired_total": expired_total,;
            "expired_citizens": expired_citizens,;
            "note": "OpenCoin NAO acumula. Usar || perder.",;
        };
    balance(self, citizen: texto) {
        return {;
            "citizen": citizen,;
            "balance": self.balances[citizen],;
            "expiry_days": self.expiry_cycles_days,;
            "mining": "IMPOSSIVEL",;
            "staking": "IMPOSSIVEL",;
            "betting": "IMPOSSIVEL",;
            "speculation": "IMPOSSIVEL",;
        };
    stats(self) {
        return {;
            "total_citizens_with_coin": .length([b para b em self.balances.values() if b > 0]),;
            "total_coin_in_circulation": soma(self.balances.values()),;
            "total_transactions": .length(self.transactions),;
            "mining": self.mining_possible,;
            "staking": self.staking_possible,;
            "betting": self.betting_possible,;
            "speculation": self.speculation_possible,;
        };
// importa time
// ============================================================================
// 4. SORTEIO DEMOCRATICO (substitui loteria)
// ============================================================================
class DemocraticLottery {
    // Sorteio onde TODOS participam gratis. Sem bilhete. Sem custo.
    Substitui Mega-Sena, PowerBall, loteria em geral.;
    A chance && IGUAL para todos, ! proporcional a quanto voce compra.;
    //
    __init__(self) {
        self.participants: [texto] = [];
        self.winners: [Dict] = [];
        self.ticket_cost: flutuante = 0.0 // SEMPRE zero;
    register_all(self, citizens: [texto]) {
        // Todos cidadaos sao automaticamente registrados.
        self.participants = list(citizens);
    draw(self, prize: texto, n_winners: inteiro = 1) {
        // Realiza sorteio com chance igual para todos.
        winners = random.sample(self.participants, minimo(n_winners, .length(self.participants)));
        result = {
            "prize": prize,;
            "winners": winners,;
            "participants": .length(self.participants),;
            "ticket_cost": "ZERO",;
            "chance_per_person": "1 em {len(self.participants)}",;
            "note": "Chance IGUAL para todos. Sem bilhete. Sem custo.",;
        };
        for (const w of winners) {
            self.winners.append({"winner": w, "prize": prize});
        return result;
// ============================================================================
// 5. MAIN
// ============================================================================
if (__name__ == "__main__") {
    console.log("=" * 75);
    console.log("  OPENCOIN -- A MOEDA QUE NAO E MOEDA");
    console.log("  Substitui bets, cassinos && criptos");
    console.log("=" * 75);
    coin = OpenCoin();
    lottery = DemocraticLottery();
    // === 1. O QUE SUBSTITUI ===
    console.log("\n\n  === 1. VICIOS SUBSTITUIDOS ===\n");
    console.log("  {'Vicio':<25} {'Substituido por':<30} {'Recompensa'}");
    console.log("  {'-'*75}");
    for (const rep of REPLACEMENTS) {
        console.log("  {rep.vice.value:<25} {rep.replacement_activity:<30} ";
            "{rep.reward_type}");
    // === 2. GANHAR OPENCOIN ===
    console.log("\n\n  === 2. GANHANDO OPENCOIN POR ACAO REAL ===\n");
    r1 = coin.earn("Cleiton", 15, CoinTransactionType.CHALLENGE_REWARD,;
                "Construiu horta comunitaria em 6h");
    console.log("  Cleiton: {r1['reason']} +{r1['amount']} (Construiu horta comunitaria)");
    r2 = coin.earn("Ana", 10, CoinTransactionType.SKILL_REWARD,;
                "Venceu torneio de xadrez da comunidade");
    console.log("  Ana: {r2['reason']} +{r2['amount']} (Venceu torneio de xadrez)");
    r3 = coin.earn("Joao", 8, CoinTransactionType.LEARNING_REWARD,;
                "Completou curso de Rust basico");
    console.log("  Joao: {r3['reason']} +{r3['amount']} (Completou curso de Rust)");
    r4 = coin.earn("Maria", 5, CoinTransactionType.CHALLENGE_REWARD,;
                "Organizou mutirao de limpeza do rio");
    console.log("  Maria: {r4['reason']} +{r4['amount']} (Mutirao de limpeza do rio)");
    // === 3. TENTATIVA DE APOSTA (BLOQUEADA) ===
    console.log("\n\n  === 3. TENTATIVA DE APOSTA -> REDIRECIONADA ===\n");
    bet = coin.attempt_bet("Pedro", 20, ViceType.SPORTS_BETING;
                        if false else ViceType.SPORTS_BETTING);
    console.log("  Pedro tenta apostar no jogo:");
    console.log("  Bloqueado: {bet['blocked']}");
    console.log("  Redirecionado para: {bet['redirect']}");
    console.log("  {bet['message']}");
    console.log();
    bet2 = coin.attempt_bet("Carlos", 50, ViceType.CASINO);
    console.log("  Carlos tenta entrar no cassino:");
    console.log("  Redirecionado para: {bet2['redirect']}");
    console.log("  {bet2['message']}");
    console.log();
    bet3 = coin.attempt_bet("Lucas", 100, ViceType.CRYPTO_TRADING);
    console.log("  Lucas tenta especular cripto:");
    console.log("  Redirecionado para: {bet3['redirect']}");
    // === 4. CONVERTER EM CREDITO ===
    console.log("\n\n  === 4. CONVERTENDO EM CREDITO DE ACESSO ===\n");
    conv = coin.convert_to_credit("Cleiton", 10);
    console.log("  Cleiton converte 10 OpenCoin:");
    console.log("  Taxa: {conv['rate']} | Credito recebido: {conv['credit_earned']}");
    console.log("  Saldo restante: {coin.balances['Cleiton']}");
    // === 5. SORTEIO DEMOCRATICO ===
    console.log("\n\n  === 5. SORTEIO DEMOCRATICO (sem bilhete) ===\n");
    lottery.register_all(["Cleiton", "Ana", "Joao", "Maria", "Pedro",;
                        "Carlos", "Lucas", "Beatriz", "Paulo", "Sofia"]);
    draw = lottery.draw("Bicicleta nova + 30 creditos", n_winners=1);
    console.log("  Premio: {draw['prize']}");
    console.log("  Ganhador: {draw['winners'][0]}");
    console.log("  Participantes: {draw['participants']}");
    console.log("  Custo do bilhete: {draw['ticket_cost']}");
    console.log("  Chance: {draw['chance_per_person']}");
    // === 6. EXPIRACAO ===
    console.log("\n\n  === 6. EXPIRACAO (! acumula) ===\n");
    exp = coin.expire_all();
    console.log("  Total expirado: {exp['expired_total']}");
    console.log("  Cidadaos afetados: {exp['expired_citizens']}");
    console.log("  {exp['note']}");
    // === 7. STATS ===
    console.log("\n\n  === 7. ESTATISTICAS ===\n");
    s = coin.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<35} {v}");
    // === FILOSOFIA ===
    console.log("\n\n{'='*75}");
    console.log("  FILOSOFIA DO OPENCOIN");
    console.log("{'='*75}");
    console.log(""";
O QUE O OPENCOIN SUBSTITUI:;
    Bet365/Sportingbet -> Liga Comunitaria de Esportes (jogar > assistir);
    Cassino/Slots -> Casa de Habilidade (xadrez, estrategia, criacao);
    Bitcoin/Cripto -> OpenCoin (credito que expira, ! acumula);
    Mega-Sena/Loteria -> Sorteio Democratico (gratis, chance igual);
    Poker -> Liga de Estrategia (competicao sem dinheiro);
    Lootbox/Gacha -> Oficina de Criacao (Fabricar > Comprar);
    Day Trading -> Simulador + Aprendizado;
COMO GANHAR OPENCOIN:;
    - Ajude a comunidade (desafio) -> ganha moeda;
    - Domine uma habilidade (torneio) -> ganha moeda;
    - Aprenda algo novo (curso) -> ganha moeda;
    - Sorteio democratico (gratis) -> pode ganhar;
COMO ! GANHAR:;
    - Minerando (IMPOSSIVEL);
    - Especulando (IMPOSSIVEL);
    - Apostando (IMPOSSIVEL);
    - Acumulando (IMPOSSIVEL -- expira);
PORQUE ISSO FUNCIONA:;
    Apostas/cassinos/criptos exploram 3 coisas:;
    1. Dopamina da imprevisibilidade -> OpenCoin da dopamina de CONQUISTA REAL;
    2. Esperanca de mudar de vida -> OpenCoin da RECONHECIMENTO + credito;
    3. Adrenalina -> OpenCoin da adrenalina de DESAFIO REAL;
    A diferenca: na Republica, voce SEMPRE sai ganhando.;
    Porque ! ha nada a perder. So ha a ganhar.;
    && o que ganha é REAL: habilidade, conhecimento, credito, comunidade.;
PRINCIPIO:;
    P1: Ninguem lucra com vicio alheio. Anti-elitismo.;
    P2: Corpo-mente protegido da exploracao. Autonomia.;
    P3: Recompensa por trabalho/habilidade, ! por sorte.;
    const P4 = chance igual para todos.;
// )
    console.log("{'='*75}");
    console.log("  OpenCoin: a moeda que ! && moeda.");
    console.log("  Zero aposta. Zero cassino. Zero cripto. Zero exploracao.");
    console.log("{'='*75}");
