// OpenCoin -- Sistema que Substitui Bets, Cassinos e Criptos -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

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
#[derive(Debug, Clone, PartialEq)]
enum ViceType {
    // Vicios que o OpenCoin substitui.
    SPORTS_BETTING = "aposta_esportiva"  // Bet365, Sportingbet;
    CASINO = "cassino"  // slots, roleta, blackjack;
    CRYPTO_TRADING = "cripto"  // Bitcoin, Ethereum speculation;
    LOTTERY = "loteria"  // Mega-Sena, PowerBall;
    POKER = "poker"  // poker online;
    GACHA_LOOTBOX = "lootbox"  // caixas de itens em jogos;
    DAY_TRADING = "day_trading"  // bolsa de valores;
#[derive(Debug, Clone, PartialEq)]
enum ViceHook {
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
#[derive(Debug, Clone)]
struct ViceReplacement {
    // Como o OpenCoin substitui um vicio.
    vice: ViceType;
    hooks: [ViceHook];
    replacement_activity: texto;
    replacement_description: texto;
    reward_type: texto // credito, reconhecimento, habilidade;
    adrenaline_source: texto // de onde vem a adrenalina saudavel;
let REPLACEMENTS: [ViceReplacement] = [;
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
#[derive(Debug, Clone, PartialEq)]
enum CoinTransactionType {
    CHALLENGE_REWARD = "desafio"  // ganhou desafio comunitario;
    SKILL_REWARD = "habilidade"  // ganhou jogo de habilidade;
    LEARNING_REWARD = "aprendizado"  // completou curso/licao;
    LOTTERY_WIN = "sorteio"  // ganhou sorteio democratico;
    TRANSFER_IN = "recebido"  // recebeu de outro;
    TRANSFER_OUT = "enviado"  // enviou para outro;
    EXPIRED = "expirado"  // ! usado no ciclo;
    CONVERTED_TO_CREDIT = "convertido"  // virou credito de acesso;
// decorador: @dataclass
#[derive(Debug, Clone)]
struct CoinTransaction {
    tx_id: texto;
    citizen: texto;
    type: CoinTransactionType;
    amount: flutuante;
    let description: String = "";
    let timestamp: f64 = field(default_factory=() -> datetime.now().timestamp());
#[derive(Debug, Clone)]
struct OpenCoin {
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
    fn __init__(self) {
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
    fn convert_to_credit(self, citizen: texto, amount: flutuante) -> {texto: qualquer} {
        // Converte OpenCoin em credito de acesso (1:1).
        if self.balances[citizen] < amount {
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
        replacement = next((r para r em REPLACEMENTS if r.vice == bet_type), NULL);
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
    fn expire_all(self) -> {texto: qualquer} {
        // Expira todos os saldos nao usados no ciclo.
        expired_total = 0;
        expired_citizens = 0;
        para cada (citizen, balance) em list(self.balances.items()): {
            if balance > 0 {
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
    fn balance(self, citizen: texto) -> {texto: qualquer} {
        return {;
            "citizen": citizen,;
            "balance": self.balances[citizen],;
            "expiry_days": self.expiry_cycles_days,;
            "mining": "IMPOSSIVEL",;
            "staking": "IMPOSSIVEL",;
            "betting": "IMPOSSIVEL",;
            "speculation": "IMPOSSIVEL",;
        };
    fn stats(self) -> {texto: qualquer} {
        return {;
            "total_citizens_with_coin": tamanho([b para b em self.balances.values() if b > 0]),;
            "total_coin_in_circulation": soma(self.balances.values()),;
            "total_transactions": tamanho(self.transactions),;
            "mining": self.mining_possible,;
            "staking": self.staking_possible,;
            "betting": self.betting_possible,;
            "speculation": self.speculation_possible,;
        };
// importa time
// ============================================================================
// 4. SORTEIO DEMOCRATICO (substitui loteria)
// ============================================================================
#[derive(Debug, Clone)]
struct DemocraticLottery {
    // Sorteio onde TODOS participam gratis. Sem bilhete. Sem custo.
    Substitui Mega-Sena, PowerBall, loteria em geral.;
    A chance && IGUAL para todos, ! proporcional a quanto voce compra.;
    //
    fn __init__(self) {
        self.participants: [texto] = [];
        self.winners: [Dict] = [];
        self.ticket_cost: flutuante = 0.0 // SEMPRE zero;
    fn register_all(self, citizens: [texto]) -> None {
        // Todos cidadaos sao automaticamente registrados.
        self.participants = list(citizens);
    fn draw(self, prize: texto, n_winners: inteiro = 1) -> {texto: qualquer} {
        // Realiza sorteio com chance igual para todos.
        winners = random.sample(self.participants, minimo(n_winners, tamanho(self.participants)));
        result = {
            "prize": prize,;
            "winners": winners,;
            "participants": tamanho(self.participants),;
            "ticket_cost": "ZERO",;
            "chance_per_person": "1 em {len(self.participants)}",;
            "note": "Chance IGUAL para todos. Sem bilhete. Sem custo.",;
        };
        for w in winners {
            self.winners.append({"winner": w, "prize": prize});
        return result;
// ============================================================================
// 5. MAIN
// ============================================================================
if __name__ == "__main__" {
    println!("=" * 75);
    println!("  OPENCOIN -- A MOEDA QUE NAO E MOEDA");
    println!("  Substitui bets, cassinos && criptos");
    println!("=" * 75);
    coin = OpenCoin();
    lottery = DemocraticLottery();
    // === 1. O QUE SUBSTITUI ===
    println!("\n\n  === 1. VICIOS SUBSTITUIDOS ===\n");
    println!("  {'Vicio':<25} {'Substituido por':<30} {'Recompensa'}");
    println!("  {'-'*75}");
    for rep in REPLACEMENTS {
        println!("  {rep.vice.value:<25} {rep.replacement_activity:<30} ";
            "{rep.reward_type}");
    // === 2. GANHAR OPENCOIN ===
    println!("\n\n  === 2. GANHANDO OPENCOIN POR ACAO REAL ===\n");
    r1 = coin.earn("Cleiton", 15, CoinTransactionType.CHALLENGE_REWARD,;
                "Construiu horta comunitaria em 6h");
    println!("  Cleiton: {r1['reason']} +{r1['amount']} (Construiu horta comunitaria)");
    r2 = coin.earn("Ana", 10, CoinTransactionType.SKILL_REWARD,;
                "Venceu torneio de xadrez da comunidade");
    println!("  Ana: {r2['reason']} +{r2['amount']} (Venceu torneio de xadrez)");
    r3 = coin.earn("Joao", 8, CoinTransactionType.LEARNING_REWARD,;
                "Completou curso de Rust basico");
    println!("  Joao: {r3['reason']} +{r3['amount']} (Completou curso de Rust)");
    r4 = coin.earn("Maria", 5, CoinTransactionType.CHALLENGE_REWARD,;
                "Organizou mutirao de limpeza do rio");
    println!("  Maria: {r4['reason']} +{r4['amount']} (Mutirao de limpeza do rio)");
    // === 3. TENTATIVA DE APOSTA (BLOQUEADA) ===
    println!("\n\n  === 3. TENTATIVA DE APOSTA -> REDIRECIONADA ===\n");
    bet = coin.attempt_bet("Pedro", 20, ViceType.SPORTS_BETING;
                        if false else ViceType.SPORTS_BETTING);
    println!("  Pedro tenta apostar no jogo:");
    println!("  Bloqueado: {bet['blocked']}");
    println!("  Redirecionado para: {bet['redirect']}");
    println!("  {bet['message']}");
    println!();
    bet2 = coin.attempt_bet("Carlos", 50, ViceType.CASINO);
    println!("  Carlos tenta entrar no cassino:");
    println!("  Redirecionado para: {bet2['redirect']}");
    println!("  {bet2['message']}");
    println!();
    bet3 = coin.attempt_bet("Lucas", 100, ViceType.CRYPTO_TRADING);
    println!("  Lucas tenta especular cripto:");
    println!("  Redirecionado para: {bet3['redirect']}");
    // === 4. CONVERTER EM CREDITO ===
    println!("\n\n  === 4. CONVERTENDO EM CREDITO DE ACESSO ===\n");
    conv = coin.convert_to_credit("Cleiton", 10);
    println!("  Cleiton converte 10 OpenCoin:");
    println!("  Taxa: {conv['rate']} | Credito recebido: {conv['credit_earned']}");
    println!("  Saldo restante: {coin.balances['Cleiton']}");
    // === 5. SORTEIO DEMOCRATICO ===
    println!("\n\n  === 5. SORTEIO DEMOCRATICO (sem bilhete) ===\n");
    lottery.register_all(["Cleiton", "Ana", "Joao", "Maria", "Pedro",;
                        "Carlos", "Lucas", "Beatriz", "Paulo", "Sofia"]);
    draw = lottery.draw("Bicicleta nova + 30 creditos", n_winners=1);
    println!("  Premio: {draw['prize']}");
    println!("  Ganhador: {draw['winners'][0]}");
    println!("  Participantes: {draw['participants']}");
    println!("  Custo do bilhete: {draw['ticket_cost']}");
    println!("  Chance: {draw['chance_per_person']}");
    // === 6. EXPIRACAO ===
    println!("\n\n  === 6. EXPIRACAO (! acumula) ===\n");
    exp = coin.expire_all();
    println!("  Total expirado: {exp['expired_total']}");
    println!("  Cidadaos afetados: {exp['expired_citizens']}");
    println!("  {exp['note']}");
    // === 7. STATS ===
    println!("\n\n  === 7. ESTATISTICAS ===\n");
    s = coin.stats();
    para cada (k, v) em s.items(): {
        println!("  {k:<35} {v}");
    // === FILOSOFIA ===
    println!("\n\n{'='*75}");
    println!("  FILOSOFIA DO OPENCOIN");
    println!("{'='*75}");
    println!(""";
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
    let P4: Sorteio democratico = chance igual para todos.;
// )
    println!("{'='*75}");
    println!("  OpenCoin: a moeda que ! && moeda.");
    println!("  Zero aposta. Zero cassino. Zero cripto. Zero exploracao.");
    println!("{'='*75}");
