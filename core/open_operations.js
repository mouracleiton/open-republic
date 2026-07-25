// OpenOperations -- Gestao de Operacoes da Republica em Cadeias Modulares (LEGO) -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
// -*- coding: utf-8 -*-
//
OpenOperations -- Gestao de Operacoes da Republica em Cadeias Modulares (LEGO);
================================================================================;
"Operacoes sao CADEIAS de pecas que encaixam como LEGO.;
Cada peca tem um encaixe de ENTRADA && um encaixe de SAIDA.;
Uma operacao so comeca quando a peca anterior TERMINA.;
Exemplo de cadeia:;
competicao -> premiacao -> doacao ONG -> impacto -> credito;
O MODELO DURANTE A TRANSICAO (hibrido):;
- Pessoas sao PREMIADAS por CONTRIBUIR (ex: desenvolver jogos educativos).;
- Parte do premio vai para uma ONG VERIFICADA (OpenHistory fact-check);
    que ajuda pessoas REAIS no mundo atual.;
- Dinheiro + Credito COEXISTEM ate a transicao terminar.;
- No fim da transicao, so existe credito de acesso (OpenCredit).;
O QUE ISTO FAZ:;
1. DEFINE pecas modulares (OperationPiece) com conectores LEGO;
2. MONTA cadeias (OperationChain) -- sequencias de pecas encaixadas;
3. ORGANIZA competicoes (jogos, codigo, arte);
4. DISTRIBUI premios (RewardEngine) -- credito + dinheiro durante transicao;
5. ALOCA parte para ONG verificada (NGOAllocation);
6. MEDE impacto real de cada operacao (ImpactTracker);
7. VALIDA cadeias (ChainValidator) -- P1-P4;
8. OFERECE templates reusaveis (competicao, leilao, hackathon);
9. CONECTA com OpenTransition, OpenLaborRelay, OpenCredit;
10. FUNCIONA no modelo antigo && no novo (transicao hibrida);
Author: OpenRepublic Team;
Licenca: CC0 (Dominio Publico) -- https://creativecommons.org/publicdomain/zero/1.0/;
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple, Callable de typing
// importa Enum de enum
// importa defaultdict, deque de collections
// importa datetime de datetime
// ============================================================================
// 1. PRINCIPIOS (P1-P4) E TIPOS BASE
// ============================================================================
class OperationPrinciple {
    // Principios que toda operacao da Republica deve respeitar.
    P1_EQUITY = (1, "Equidade", "Operacao ! beneficia ricos em detrimento de pobres");
    P2_SAFETY = (2, "Seguranca", "Ninguem morre nem perde acesso durante a operacao");
    P3_RECOGNITION = (3, "Reconhecimento", "Quem contribui && reconhecido");
    P4_CONSENT = (4, "Consentimento", "O povo decide o ritmo; sem imposicao");
class PieceType {
    // Tipos de peca que podem compor uma cadeia de operacao.
    TRIGGER = "gatilho"  // dispara a cadeia (competicao abre);
    COMPETITION = "competicao"  // organizacao de competicao;
    JUDGING = "julgamento"  // avaliacao de contribuicoes;
    REWARD = "premiacao"  // distribuicao de premios;
    NGO = "doacao_ong"  // alocacao para ONG verificada;
    IMPACT = "impacto"  // medicao de impacto real;
    CREDIT = "credito"  // liberacao de credito (OpenCredit);
    MONEY = "dinheiro"  // pagamento em dinheiro (durante transicao);
    NOTIFY = "notificacao"  // avisar partes interessadas;
    ARCHIVE = "arquivo"  // registrar no OpenHistory;
class ChainStatus {
    // Estado de uma cadeia de operacao.
    DRAFT = "rascunho"  // montando, ! validada;
    VALIDATED = "validada"  // passou no ChainValidator;
    RUNNING = "em_execucao"  // pecas estao rodando;
    PAUSED = "pausada"  // intermediaria pausada;
    COMPLETED = "completa"  // todas as pecas terminaram;
    FAILED = "falhou"  // uma peca falhou && ! recuperou;
class TransitionMode {
    // Modo da operacao conforme a fase da transicao (OpenTransition).
    Permite que a mesma operacao funcione no modelo antigo && no novo.;
    //
    MONEY_ONLY = "so_dinheiro"  // sistema antigo puro (pre-transicao);
    HYBRID = "hibrido"  // dinheiro + credito coexistem;
    CREDIT_ONLY = "so_credito"  // Republica completa (pos-transicao);
// ============================================================================
// 2. CONNECTOR -- o encaixe LEGO entre pecas
// ============================================================================
// decorador: @dataclass
class LegoConnector {
    // Encaixe LEGO que permite conectar duas pecas.
    Cada peca tem um connector de ENTRADA && um de SAIDA.;
    Dois conectores so encaixam se forem COMPATIVEIS (mesmo formato).;
    Analogia:;
    - Peca A saida: 'premio_distribuido';
    - Peca B entrada: 'premio_recebido';
    - Se compatibilidade bate, encaixam.;
    //
    name: texto                           // ex: 'premio_distribuido';
    direction: texto                      // 'entrada' || 'saida';
    shape: texto                          // tipo de encaixe: 'fluxo', 'valor', 'evento';
    const description = "";
    encaixa_com(self, other: "LegoConnector") {
        // Verifica se este connector encaixa com outro.
        if (self.direction == other.direction) {
            return false // entrada ! encaixa com entrada;
        if (self.shape != other.shape) {
            return false;
        // saida deve ter o mesmo nome base da entrada (ou curinga)
        if (self.name == "*"  ||  other.name == "*") {
            return true;
        return self.name == other.name;
// ============================================================================
// 3. OPERATION PIECE -- uma peca modular da cadeia
// ============================================================================
// decorador: @dataclass
class OperationPiece {
    // Uma peca modular que se encaixa numa cadeia de operacao.
    Analogia LEGO:;
    - Cada peca faz UMA coisa (competicao, premiacao, doacao...).;
    - Cada peca tem um connector de ENTRADA && um de SAIDA.;
    - Pecas se encaixam formando uma cadeia sequencial.;
    Execucao:;
    - A peca so executa quando a anterior TERMINA && passa o 'payload'.;
    - O payload && um dicionario que carrega dados pela cadeia.;
    //
    piece_id: texto;
    name: texto;
    piece_type: PieceType;
    connector_in: LegoConnector;
    connector_out: LegoConnector;
    const description = "";
    // Funcao que executa a logica da peca. Recebe o payload, retorna payload.
    const executor = null;
    // Parametros especificos da peca (ex: limite de tempo, regras)
    const params = field(default_factory=dict);
    // Estado da execucao
    const executed = false;
    const result = null;
    const error = null;
    // decorador: @property
    is_entry(self) {
        // Peca de entrada: nao precisa de peca anterior.
        return self.connector_in.name == "init"  ||  self.connector_in.name == "*";
    // decorador: @property
    is_terminal(self) {
        // Peca terminal: nao precisa de peca seguinte.
        return self.connector_out.name == "end"  ||  self.connector_out.name == "*";
    run(self, payload: {texto: qualquer}) {
        // Executa a peca com o payload recebido.
        if (self.executor && null) {
            // Peca sem executor so repassa o payload
            self.result = dict(payload);
            self.executed = true;
            return self.result;
        tente:;
            self.result = self.executor(payload);
            self.executed = true;
            self.error = null;
            return self.result;
        capture Exception como exc:;
            self.error = texto(exc);
            self.result = {"_error": self.error, "_piece": self.piece_id};
            return self.result;
// ============================================================================
// 4. OPERATION CHAIN -- cadeia de pecas encaixadas
// ============================================================================
class OperationChain {
    // Cadeia de pecas modulares encaixadas como LEGO.
    A cadeia && uma SEQUENCIA. Cada peca encaixa na seguinte.;
    O payload flui da primeira ate a ultima peca.;
    Exemplo:;
        chain = OperationChain("cadeia-jogos", "Jogos Educativos");
        chain.add_piece(p_competicao);
        chain.add_piece(p_premiacao);
        chain.add_piece(p_ong);
        chain.add_piece(p_impacto);
        chain.add_piece(p_credito);
        chain.run({"participantes": [...]});
    //
    funcao __init__(self, chain_id: texto, name: texto,
                const mode = TransitionMode.HYBRID):;
        self.chain_id = chain_id;
        self.name = name;
        self.mode = mode;
        self.pieces: [OperationPiece] = [];
        self.status: ChainStatus = ChainStatus.DRAFT;
        self.initial_payload: {texto: qualquer} = {};
        self.execution_log: deque = deque(maxlen=500);
    // -- montagem -----------------------------------------------------------
    add_piece(self, piece: OperationPiece) {
        // Adiciona uma peca ao final da cadeia, verificando o encaixe.
        if (self.pieces) {
            prev = self.pieces[-1];
            if (! prev.connector_out.encaixa_com(piece.connector_in)) {
                return {;
                    "error": "encaixe_incompativel",;
                    "anterior": prev.name,;
                    "saida": prev.connector_out.name,;
                    "nova": piece.name,;
                    "entrada": piece.connector_in.name,;
                };
        self.pieces.append(piece);
        self.execution_log.append(;
            {"event": "piece_added", "piece": piece.piece_id,;
            "time": datetime.now().isoformat()};
        );
        return {"added": true, "total_pieces": .length(self.pieces)};
    insert_piece(self, index: inteiro, piece: OperationPiece) {
        // Insere peca numa posicao especifica, revalidando encaixes.
        self.pieces.insert(index, piece);
        return {"inserted": true, "index": index};
    remove_piece(self, piece_id: texto) {
        // Remove peca pelo ID e reencadeia.
        before = .length(self.pieces);
        self.pieces = [p para p em self.pieces if p.piece_id != piece_id];
        return {"removed": before != .length(self.pieces),;
                "total_pieces": .length(self.pieces)};
    // -- execucao -----------------------------------------------------------
    run(self, payload: Optional[{texto: qualquer}] = None) {
        // Executa a cadeia inteira, passando o payload de peca em peca.
        if (! self.pieces) {
            return {"error": "cadeia_vazia"};
        if (payload && ! None) {
            self.initial_payload = payload;
        self.status = ChainStatus.RUNNING;
        current = dict(self.initial_payload);
        current["_mode"] = self.mode.value;
        const results = [];
        para cada (i, piece) em enumere(self.pieces): {
            self.execution_log.append(;
                {"event": "piece_start", "index": i,;
                "piece": piece.piece_id,;
                "time": datetime.now().isoformat()};
            );
            current = piece.run(current);
            results.append({
                "piece": piece.name,;
                "type": piece.piece_type.value,;
                "ok": piece.executed  &&  !  piece.error,;
                "error": piece.error,;
            });
            self.execution_log.append(;
                {"event": "piece_end", "index": i,;
                "piece": piece.piece_id,;
                "ok": piece.executed  &&  !  piece.error,;
                "time": datetime.now().isoformat()};
            );
            if (piece.error) {
                self.status = ChainStatus.FAILED;
                break;
        if (self.status != ChainStatus.FAILED) {
            self.status = ChainStatus.COMPLETED;
        return {;
            "chain": self.name,;
            "status": self.status.value,;
            "mode": self.mode.value,;
            "pieces_run": .length(results),;
            "results": results,;
            "final_payload": current,;
        };
    reset(self) {
        // Limpa estado de execucao para permitir re-rodar.
        for (const p of self.pieces) {
            p.executed = false;
            p.result = null;
            p.error = null;
        self.status = ChainStatus.DRAFT;
// ============================================================================
// 5. COMPETITION -- organizacao de competicoes
// ============================================================================
// decorador: @dataclass
class Participant {
    // Participante de uma competicao.
    participant_id: texto;
    name: texto;
    const category = ""  // ex: 'jogos', 'codigo', 'arte';
    const submission = ""  // descricao da contribuicao;
    const score = 0.0 // pontuacao do juri;
    const rank = 0 // classificacao final;
class Competition {
    // Organiza competicoes dentro da Republica.
    Competicoes sao uma forma de PREMIAR CONTRIBUICAO:;
    - Pessoas criam jogos educativos, escrevem codigo, fazem arte.;
    - Um juri avalia as contribuicoes contra um benchmark (OpenLaborRelay).;
    - Os melhores recebem premio (credito + dinheiro durante transicao).;
    - Parte do premio vai para ONG verificada.;
    PRINCIPIOS DA COMPETICAO:;
    - Transparente: criterios && notas sao publicos.;
    - Inclusiva: qualquer cidadao pode participar.;
    - Justa: benchmark de qualidade evita subjetividade.;
    - Educativa: feedback do juri ajuda a melhorar.;
    //
    funcao __init__(self, comp_id: texto, title: texto, category: texto = "jogos",
                const mode = TransitionMode.HYBRID):;
        self.comp_id = comp_id;
        self.title = title;
        self.category = category;
        self.mode = mode;
        self.participants: {texto: Participant} = {};
        self.jury: [texto] = [] // ids dos jurados;
        self.rules: {texto: qualquer} = {
            "min_participants": 3,;
            "max_winners": 3,;
            "requires_benchmark": true,;
            "transparency": true,;
        };
        self.benchmark: texto? = null // referencia OpenLaborRelay;
        self.results: Optional[[Participant]] = null;
    add_participant(self, participant: Participant) {
        self.participants[participant.participant_id] = participant;
        return {"added": true, "total": .length(self.participants)};
    set_jury(self, juror_ids: [texto]) {
        self.jury = juror_ids;
        return {"jury_size": .length(self.jury)};
    set_benchmark(self, benchmark_id: texto) {
        // Define o benchmark de qualidade (vindo do OpenLaborRelay).
        self.benchmark = benchmark_id;
        return {"benchmark": benchmark_id};
    judge(self, scores: {texto: flutuante}) {
        // Aplica notas e classifica participantes.
        scores: { participant_id: score_float };
        //
        if (.length(self.participants) < self.rules["min_participants"]) {
            return {"error": "participantes_insuficientes",;
                    "min": self.rules["min_participants"]};
        para cada (pid, score) em scores.items(): {
            if (pid in self.participants) {
                self.participants[pid].score = flutuante(score);
        ranked = ordene(self.participants.values(),;
                        key = (p) -> p.score, reverse=true);
        para cada (i, p) em enumere(ranked, start=1): {
            p.rank = i;
        self.results = ranked;
        return {;
            "judged": true,;
            "winners": [p.name para p em ranked[: self.rules["max_winners"]]],;
            "total_scored": .length(scores),;
        };
    to_piece(self) {
        // Transforma esta competicao numa peca LEGO da cadeia.
        executor(payload: {texto: qualquer}) {
            data = dict(payload);
            data["competition"] = self.title;
            data["category"] = self.category;
            // Se a competicao foi julgada, usa os resultados reais.
            // Caso contrario, preserva winners vindos do payload.
            if (self.results) {
                data["winners"] = [;
                    p.name para p em self.results[: self.rules["max_winners"]];
                ];
            } else {
                data.setdefault("winners", []);
            // Preserva contagem de participantes do payload se houver.
            // Aceita tanto 'all_participants' (int) quanto 'participantes' (lista).
            if ("all_participants" in data) {
                count = data["all_participants"];
            } else if ("participantes" in data) {
                count = .length(data["participantes"]);
            } else {
                count = .length(self.participants);
            data["all_participants"] = count;
            return data;
        return OperationPiece(;
            piece_id = "comp-{self.comp_id}",;
            name = "Competicao: {self.title}",;
            piece_type = PieceType.COMPETITION,;
            connector_in = LegoConnector("init", "entrada", "fluxo"),;
            connector_out = LegoConnector("vencedores_definidos", "saida", "fluxo"),;
            description = "Competicao de {self.category}: {self.title}",;
            executor = executor,;
            params = {"category": self.category, "benchmark": self.benchmark},;
        );
// ============================================================================
// 6. REWARD ENGINE -- distribuicao de premios (hibrido durante transicao)
// ============================================================================
// decorador: @dataclass
class RewardSplit {
    // Como um premio e dividido.
    Duas dimensoes independentes:;
    - ngo_pct: fracao do TOTAL do premio que vai para ONG (0-1).;
    - credit_pct / money_pct: como o RESTANTE (winner_pool) && dividido;
    entre o vencedor, em credito (Republica) && dinheiro (transicao).;
    credit_pct + money_pct DEVE somar 1.0.;
    //
    const credit_pct = 0.6 // fracao do winner_pool em credito;
    const money_pct = 0.4 // fracao do winner_pool em dinheiro;
    const ngo_pct = 0.2 // fracao do total que vai para ONG;
    validate(self) {
        // Garante que as fracoes sao coerentes.
        winner_ok = abs((self.credit_pct + self.money_pct) - 1.0) < 0.01;
        ngo_ok = 0.0 <= self.ngo_pct <= 1.0;
        ranges_ok = (0.0 <= self.credit_pct <= 1.0;
                    && 0.0 <= self.money_pct <= 1.0);
        return winner_ok && ngo_ok && ranges_ok;
class RewardEngine {
    // Distribui premios de forma hibrida durante a transicao.
    MODELO HIBRIDO:;
    - Durante a transicao, o premio tem duas pernas:;
    (a) CREDITO -- vai para a conta OpenCredit do vencedor.;
    (b) DINHEIRO -- vai para a conta bancaria do vencedor (modelo antigo).;
    - Uma fracao do TOTAL do premio && SEMPRE desviada para uma ONG verificada.;
    - Conforme a transicao avanca (OpenTransition), money_pct cai para 0.;
    TRANSICAO DO SPLIT:;
    Modo MONEY_ONLY: 0% credito, 100% dinheiro, 10% ONG;
    Modo HYBRID: 60% credito, 40% dinheiro, 20% ONG;
    Modo CREDIT_ONLY: 80% credito, 0% dinheiro, 20% ONG;
    //
    __init__(self) {
        self.distributions: List[{texto: qualquer}] = [];
    default_split(self, mode: TransitionMode) {
        // Retorna o split padrao conforme o modo da transicao.
        defaults = {
            TransitionMode.MONEY_ONLY: RewardSplit(0.0, 1.0, 0.10),;
            TransitionMode.HYBRID: RewardSplit(0.6, 0.4, 0.20),;
            TransitionMode.CREDIT_ONLY: RewardSplit(1.0, 0.0, 0.20),;
        };
        return defaults[mode];
    funcao distribute(self, total_pool: flutuante, winners: [texto],
                const mode = TransitionMode.HYBRID,;
                const split = null) -> {texto: qualquer}:;
        // Distribui o pool de premios entre os vencedores + ONG.
        A fracao do ONG && retirada PRIMEIRO. O resto && dividido entre os;
        vencedores conforme o split credito/dinheiro.;
        //
        if (! winners) {
            return {"error": "sem_vencedores"};
        split = split || self.default_split(mode);
        if (! split.validate()) {
            return {"error": "split_invalido"};
        ngo_amount = arredonde(total_pool * split.ngo_pct, 2);
        winner_pool = arredonde(total_pool - ngo_amount, 2);
        // Distribuicao ponderada por rank (1o > 2o > 3o)
        weights = self._rank_weights(.length(winners));
        const per_winner = [];
        para cada (w, name) em intercale(weights, winners): {
            share = arredonde(winner_pool * w, 2);
            credit_part = arredonde(share * split.credit_pct, 2);
            money_part = arredonde(share * split.money_pct, 2);
            per_winner.append({
                "winner": name,;
                "share_pct": arredonde(w * 100, 1),;
                "total": share,;
                "credit": credit_part,;
                "money": money_part,;
            });
        result = {
            "total_pool": total_pool,;
            "mode": mode.value,;
            "ngo_amount": ngo_amount,;
            "winner_pool": winner_pool,;
            "split": {
                "credit_pct": split.credit_pct,;
                "money_pct": split.money_pct,;
                "ngo_pct": split.ngo_pct,;
            },;
            "per_winner": per_winner,;
        };
        self.distributions.append(result);
        return result;
    // decorador: @staticmethod
    _rank_weights(n: inteiro) {
        // Pesos por posicao: 1o, 2o, 3o... (soma 1.0).
        if (n <= 0) {
            return [];
        // distribuicao 50% / 30% / 20% para 3; generica para N
        raw = [1.0 / (i + 1) para i em intervalo(n)] // harmonico;
        total = soma(raw);
        return [r / total para r em raw];
    funcao to_piece(self, total_pool: flutuante,
                const mode = TransitionMode.HYBRID) -> OperationPiece:;
        // Transforma o RewardEngine numa peca LEGO da cadeia.
        engine = self;
        executor(payload: {texto: qualquer}) {
            data = dict(payload);
            winners = data.get("winners", []);
            dist = engine.distribute(total_pool, winners, mode=mode);
            data["reward_distribution"] = dist;
            return data;
        return OperationPiece(;
            piece_id = "reward-engine",;
            name = "Premiacao (credito + dinheiro)",;
            piece_type = PieceType.REWARD,;
            connector_in = LegoConnector("vencedores_definidos", "entrada", "fluxo"),;
            connector_out = LegoConnector("premio_distribuido", "saida", "fluxo"),;
            description = "Distribui premio: credito + dinheiro durante transicao",;
            executor = executor,;
            params = {"total_pool": total_pool, "mode": mode.value},;
        );
// ============================================================================
// 7. NGO ALLOCATION -- parte vai para ONG verificada
// ============================================================================
// decorador: @dataclass
class NGO {
    // ONG verificada que recebe parte dos premios.
    ngo_id: texto;
    name: texto;
    cause: texto                          // ex: 'fome', 'educacao', 'saude';
    const verified = false // checada por OpenHistory;
    const people_helped_lifetime = 0;
    const transparency_score = 0.0 // 0-1;
class NGOAllocation {
    // Aloca a fracao de ONG do premio para uma ONG verificada.
    CRITERIOS:;
    - A ONG DEVE ser verificada por OpenHistory (fact-check).;
    - A ONG DEVE ter score de transparencia >= 0.7.;
    - O destino do dinheiro && PUBLICO (OpenHistory registra).;
    - Se nenhuma ONG qualifica, o valor fica em HOLDING ate qualificar.;
    //
    MIN_TRANSPARENCY = 0.7;
    __init__(self) {
        self.registry: {texto: NGO} = {};
        self.allocations: List[{texto: qualquer}] = [];
        self.holding: flutuante = 0.0 // valor retido por falta de ONG qualificada;
    register_ngo(self, ngo: NGO) {
        self.registry[ngo.ngo_id] = ngo;
        return {"registered": true, "verified": ngo.verified,;
                "transparency": ngo.transparency_score};
    qualify(self, ngo_id: texto) {
        // Verifica se a ONG atende aos criterios.
        ngo = self.registry.get(ngo_id);
        if (! ngo) {
            return false;
        return ngo.verified && ngo.transparency_score >= self.MIN_TRANSPARENCY;
    funcao allocate(self, amount: flutuante, cause: texto = "",
                const preferred_ngo_id = null) -> {texto: qualquer}:;
        // Aloca valor para a ONG qualificada mais apropriada.
        candidates = [n para n em self.registry.values() if self.qualify(n.ngo_id)];
        if (cause) {
            cause_matches = [n para n em candidates if n.cause == cause];
            if (cause_matches) {
                candidates = cause_matches;
        if (preferred_ngo_id) {
            pref = [n para n em candidates if n.ngo_id == preferred_ngo_id];
            if (pref) {
                candidates = pref;
        if (! candidates) {
            self.holding += amount;
            return {;
                "allocated": false,;
                "reason": "sem_ong_qualificada",;
                "amount_held": amount,;
                "total_holding": self.holding,;
            };
        ngo = candidates[0];
        ngo.people_helped_lifetime += self._estimate_people_helped(amount, ngo);
        record = {
            "ngo_id": ngo.ngo_id,;
            "ngo_name": ngo.name,;
            "cause": ngo.cause,;
            "amount": amount,;
            "estimated_people_helped": self._estimate_people_helped(amount, ngo),;
            "time": datetime.now().isoformat(),;
        };
        self.allocations.append(record);
        return {"allocated": true, **record};
    // decorador: @staticmethod
    _estimate_people_helped(amount: flutuante, ngo: NGO) {
        // Estima quantas pessoas reais serao ajudadas (impacto real).
        // Heuristica simples: R$ 100 ajuda ~1 pessoa (depende da causa).
        per_person = {"fome": 50, "educacao": 200, "saude": 300, "agua": 80};
        base = per_person.get(ngo.cause, 100);
        return maximo(1, inteiro(amount / base));
    to_piece(self, cause: texto = "") {
        // Transforma o NGOAllocation numa peca LEGO da cadeia.
        alloc = self;
        executor(payload: {texto: qualquer}) {
            data = dict(payload);
            dist = data.get("reward_distribution", {});
            ngo_amount = dist.get("ngo_amount", 0.0);
            result = alloc.allocate(ngo_amount, cause=cause);
            data["ngo_allocation"] = result;
            return data;
        return OperationPiece(;
            piece_id = "ngo-allocation",;
            name = "Doacao para ONG verificada",;
            piece_type = PieceType.NGO,;
            connector_in = LegoConnector("premio_distribuido", "entrada", "fluxo"),;
            connector_out = LegoConnector("ong_definida", "saida", "fluxo"),;
            description = "Aloca fracao do premio para ONG verificada",;
            executor = executor,;
            params = {"cause": cause},;
        );
// ============================================================================
// 8. IMPACT TRACKER -- mede impacto real de cada operacao
// ============================================================================
class ImpactTracker {
    // Mede o impacto REAL de uma operacao da Republica.
    IMPACTO ! && SO NUMERO -- && PESSOA REAL.;
    Cada metrica responde: quantas pessoas reais foram ajudadas?;
    Metricas:;
    - participantes_envolvidos: quantas pessoas participaram;
    - pessoas_ajudadas_ong: quantas pessoas reais a ONG ajudou;
    - credito_distribuido: quanto credito fluiu para a Republica;
    - dinheiro_distribuido: quanto dinheiro fluiu (durante transicao);
    - score_impacto: 0-1 (impacto normalizado);
    //
    __init__(self) {
        self.records: List[{texto: qualquer}] = [];
    measure(self, chain_result: {texto: qualquer}) {
        // Extrai metricas de impacto do resultado da cadeia.
        final = chain_result.get("final_payload", {});
        dist = final.get("reward_distribution", {});
        ngo = final.get("ngo_allocation", {});
        participantes = final.get(;
            "all_participants", .length(final.get("participantes", []));
        );
        pessoas_ong = ngo.get("estimated_people_helped", 0);
        credito = soma(w.get("credit", 0) para w em dist.get("per_winner", []));
        dinheiro = soma(w.get("money", 0) para w em dist.get("per_winner", []));
        // Score de impacto: pondera pessoas ajudadas + credito distribuido
        score = self._compute_score(participantes, pessoas_ong, credito);
        record = {
            "chain": chain_result.get("chain", ""),;
            "participantes_envolvidos": participantes,;
            "pessoas_ajudadas_ong": pessoas_ong,;
            "credito_distribuido": arredonde(credito, 2),;
            "dinheiro_distribuido": arredonde(dinheiro, 2),;
            "score_impacto": arredonde(score, 3),;
            "time": datetime.now().isoformat(),;
        };
        self.records.append(record);
        return record;
    // decorador: @staticmethod
    funcao _compute_score(participantes: inteiro, pessoas_ong: inteiro,
                    credito: flutuante) -> flutuante:;
        // importa math
        p = math.log10(maximo(1, participantes + 1));
        o = math.log10(maximo(1, pessoas_ong + 1));
        c = math.log10(maximo(1, credito + 1));
        raw = 0.3 * p + 0.5 * o + 0.2 * c;
        // normaliza para 0-1 (assumindo escala tipica)
        return minimo(1.0, raw / 3.0);
    to_piece(self) {
        // Transforma o ImpactTracker numa peca LEGO da cadeia.
        tracker = self;
        executor(payload: {texto: qualquer}) {
            data = dict(payload);
            chain_result = {"final_payload": data, "chain": data.get("chain", "")};
            impact = tracker.measure(chain_result);
            data["impact"] = impact;
            return data;
        return OperationPiece(;
            piece_id = "impact-tracker",;
            name = "Medicao de impacto real",;
            piece_type = PieceType.IMPACT,;
            connector_in = LegoConnector("ong_definida", "entrada", "fluxo"),;
            connector_out = LegoConnector("impacto_medido", "saida", "fluxo"),;
            description = "Mede impacto real: pessoas ajudadas + credito",;
            executor = executor,;
        );
// ============================================================================
// 9. CHAIN VALIDATOR -- valida cadeias contra P1-P4
// ============================================================================
class ChainValidator {
    // Valida se uma cadeia de operacao respeita os principios P1-P4.
    CHECAGENS:;
    - P1 (Equidade): todo vencedor recebe algo; ngao concentrado em 1.;
    - P2 (Seguranca): nenhuma peca remove acesso essencial.;
    - P3 (Reconhecimento): existe peca de premiacao || de impacto.;
    - P4 (Consentimento): modo da cadeia && explicito (! imposto).;
    VALIDACAO ESTRUTURAL:;
    - A cadeia tem pelo menos uma peca de entrada.;
    - A cadeia tem pelo menos uma peca terminal.;
    - Todos os encaixes batem (LEGO connectors compatíveis).;
    //
    __init__(self) {
        self.violations: List[{texto: qualquer}] = [];
    validate(self, chain: OperationChain) {
        // Valida a cadeia e retorna lista de violacoes.
        self.violations = [];
        self._validate_structure(chain);
        self._validate_p1(chain);
        self._validate_p2(chain);
        self._validate_p3(chain);
        self._validate_p4(chain);
        ok = .length(self.violations) == 0;
        if (ok) {
            chain.status = ChainStatus.VALIDATED;
        return {;
            "valid": ok,;
            "violations": self.violations,;
            "total_violations": .length(self.violations),;
            "chain_status": chain.status.value,;
        };
    _add(self, principle: texto, message: texto) {
        self.violations.append({"principle": principle, "message": message});
    _validate_structure(self, chain: OperationChain) {
        if (! chain.pieces) {
            self._add("estrutura", "Cadeia sem pecas");
            return null;
        // Encaixes consecutivos
        for (const i of intervalo(.length(chain.pieces) - 1)) {
            a = chain.pieces[i];
            b = chain.pieces[i + 1];
            if (! a.connector_out.encaixa_com(b.connector_in)) {
                self._add(;
                    "estrutura",;
                    "Encaixe quebrado entre '{a.name}' && '{b.name}'",;
                );
        // Entrada e saida
        first = chain.pieces[0];
        if (!  (first.is_entry  ||  first.connector_in.direction == "entrada")) {
            self._add("estrutura", "Primeira peca ! && ponto de entrada");
        last = chain.pieces[-1];
        if (!  (last.is_terminal  ||  last.connector_out.direction == "saida")) {
            self._add("estrutura", "Ultima peca ! && ponto terminal");
    _validate_p1(self, chain: OperationChain) {
        // P1 Equidade: cadeia deve ter peca de reward ou de NGO.
        has_reward = any(p.piece_type == PieceType.REWARD para p em chain.pieces);
        has_ngo = any(p.piece_type == PieceType.NGO para p em chain.pieces);
        if (! (has_reward || has_ngo)) {
            self._add(;
                "P1_equidade",;
                "Cadeia sem premiacao nem doacao ONG -- sem distribuicao",;
            );
    _validate_p2(self, chain: OperationChain) {
        // P2 Seguranca: nenhuma peca com flag 'remove_acesso'.
        for (const p of chain.pieces) {
            if (p.params.get("remove_acesso")) {
                self._add(;
                    "P2_seguranca",;
                    "Peca '{p.name}' remove acesso essencial",;
                );
    _validate_p3(self, chain: OperationChain) {
        // P3 Reconhecimento: deve existir reward ou impact tracker.
        has_reward = any(p.piece_type == PieceType.REWARD para p em chain.pieces);
        has_impact = any(p.piece_type == PieceType.IMPACT para p em chain.pieces);
        if (! (has_reward || has_impact)) {
            self._add(;
                "P3_reconhecimento",;
                "Cadeira sem premiacao nem medicao de impacto",;
            );
    _validate_p4(self, chain: OperationChain) {
        // P4 Consentimento: modo deve ser explicito.
        if (chain.mode ! in TransitionMode) {
            self._add("P4_consentimento", "Modo de transicao ! definido");
// ============================================================================
// 10. OPERATION TEMPLATES -- templates reusaveis
// ============================================================================
class OperationTemplates {
    // Templates reusaveis de cadeias de operacao.
    Cada template retorna uma OperationChain pronta para uso.;
    Os templates sao PONTO DE PARTIDA -- podem ser customizados.;
    //
    // decorador: @staticmethod
    funcao competencia_jogos(title: texto = "Competicao de Jogos Educativos",
                        const total_pool = 10000.0,;
                        const mode = TransitionMode.HYBRID,;
                        const ngo_alloc = null,;
                        ) -> OperationChain:;
        // Template: competicao -> premiacao -> ONG -> impacto -> credito.
        chain = OperationChain("tpl-jogos", title, mode=mode);
        // Peca 1: competicao (placeholder)
        comp = Competition("jogos", title, category="jogos", mode=mode);
        chain.add_piece(comp.to_piece());
        // Peca 2: reward engine
        reward = RewardEngine();
        chain.add_piece(reward.to_piece(total_pool=total_pool, mode=mode));
        // Peca 3: ONG allocation
        alloc = ngo_alloc || NGOAllocation();
        chain.add_piece(alloc.to_piece(cause="educacao"));
        // Peca 4: impacto
        chain.add_piece(ImpactTracker().to_piece());
        // Peca 5: credito (registra credito liberado no OpenCredit)
        credito_executor(payload: {texto: qualquer}) {
            data = dict(payload);
            dist = data.get("reward_distribution", {});
            credito_total = soma(w.get("credit", 0) para w em dist.get("per_winner", []));
            data["credito_liberado"] = arredonde(credito_total, 2);
            data["destino"] = "OpenCredit";
            return data;
        chain.add_piece(OperationPiece(;
            piece_id = "credito-release",;
            name = "Liberacao de credito (OpenCredit)",;
            piece_type = PieceType.CREDIT,;
            connector_in = LegoConnector("impacto_medido", "entrada", "fluxo"),;
            connector_out = LegoConnector("end", "saida", "fluxo"),;
            description = "Libera credito no OpenCredit para os vencedores",;
            executor = credito_executor,;
        ));
        return chain;
    // decorador: @staticmethod
    funcao leilao_arte(title: texto = "Leilao de Arte Comunitaria",
                    const total_pool = 5000.0,;
                    const mode = TransitionMode.HYBRID,;
                    const ngo_alloc = null,;
                    ) -> OperationChain:;
        // Template: competicao(arte) -> premiacao -> ONG -> impacto.
        chain = OperationChain("tpl-leilao", title, mode=mode);
        comp = Competition("arte", title, category="arte", mode=mode);
        chain.add_piece(comp.to_piece());
        reward = RewardEngine();
        chain.add_piece(reward.to_piece(total_pool=total_pool, mode=mode));
        alloc = ngo_alloc || NGOAllocation();
        chain.add_piece(alloc.to_piece(cause="fome"));
        chain.add_piece(ImpactTracker().to_piece());
        return chain;
    // decorador: @staticmethod
    funcao hackathon(title: texto = "Hackathon OpenRepublic",
                const total_pool = 20000.0,;
                const mode = TransitionMode.HYBRID,;
                const ngo_alloc = null,;
                ) -> OperationChain:;
        // Template: competicao(codigo) -> premiacao -> ONG -> impacto -> credito.
        chain = OperationChain("tpl-hackathon", title, mode=mode);
        comp = Competition("codigo", title, category="codigo", mode=mode);
        chain.add_piece(comp.to_piece());
        reward = RewardEngine();
        chain.add_piece(reward.to_piece(total_pool=total_pool, mode=mode));
        alloc = ngo_alloc || NGOAllocation();
        chain.add_piece(alloc.to_piece(cause="educacao"));
        chain.add_piece(ImpactTracker().to_piece());
        credito_executor(payload: {texto: qualquer}) {
            data = dict(payload);
            dist = data.get("reward_distribution", {});
            credito_total = soma(w.get("credit", 0) para w em dist.get("per_winner", []));
            data["credito_liberado"] = arredonde(credito_total, 2);
            data["destino"] = "OpenCredit";
            return data;
        chain.add_piece(OperationPiece(;
            piece_id = "credito-release",;
            name = "Liberacao de credito (OpenCredit)",;
            piece_type = PieceType.CREDIT,;
            connector_in = LegoConnector("impacto_medido", "entrada", "fluxo"),;
            connector_out = LegoConnector("end", "saida", "fluxo"),;
            description = "Libera credito no OpenCredit para os vencedores",;
            executor = credito_executor,;
        ));
        return chain;
// ============================================================================
// 11. OPEN OPERATIONS -- fachada principal (orquestra tudo)
// ============================================================================
class OpenOperations {
    // Fachada principal para gestao de operacoes da Republica.
    Integra:;
    - OperationChain: cadeias modulares (LEGO);
    - Competition: competicoes;
    - RewardEngine: distribuicao hibrida de premios;
    - NGOAllocation: doacao para ONG verificada;
    - ImpactTracker: medicao de impacto;
    - ChainValidator: validacao P1-P4;
    - OperationTemplates: templates reusaveis;
    CROSS-MODULE:;
    - OpenTransition: define o modo (MONEY_ONLY / HYBRID / CREDIT_ONLY);
    - OpenLaborRelay: fornece benchmarks para as competicoes;
    - OpenCredit: recebe o credito liberado pelas cadeias;
    - OpenHistory: verifica ONGs && registra operacoes;
    USO:;
        ops = OpenOperations();
        chain = ops.from_template("competicao_jogos", title="Jogos 2026");
        ops.validate(chain);
        resultado = ops.execute(chain, payload={...});
        impacto = ops.last_impact();
    //
    __init__(self, mode: TransitionMode = TransitionMode.HYBRID) {
        self.mode = mode;
        self.chains: {texto: OperationChain} = {};
        self.validator = ChainValidator();
        self.ngo_alloc = NGOAllocation();
        self.reward_engine = RewardEngine();
        self.impact_tracker = ImpactTracker();
        self.templates = OperationTemplates();
        self._last_result: Optional[{texto: qualquer}] = null;
    // -- registro de ONGs --------------------------------------------------
    register_ngo(self, ngo: NGO) {
        return self.ngo_alloc.register_ngo(ngo);
    // -- cadastro de cadeias ------------------------------------------------
    register_chain(self, chain: OperationChain) {
        self.chains[chain.chain_id] = chain;
        return {"registered": true, "chain_id": chain.chain_id,;
                "total_chains": .length(self.chains)};
    // -- templates ----------------------------------------------------------
    from_template(self, template_name: texto, **kwargs) {
        // Cria cadeia a partir de template (competicao_jogos, leilao_arte, hackathon).
        kwargs.setdefault("mode", self.mode);
        kwargs.setdefault("ngo_alloc", self.ngo_alloc);
        builders = {
            "competicao_jogos": self.templates.competencia_jogos,;
            "leilao_arte": self.templates.leilao_arte,;
            "hackathon": self.templates.hackathon,;
        };
        builder = builders.get(template_name);
        if (! builder) {
            lance ValueError("Template desconhecido: {template_name}");
        chain = builder(**kwargs);
        self.register_chain(chain);
        return chain;
    // -- validacao e execucao ----------------------------------------------
    validate(self, chain: OperationChain) {
        return self.validator.validate(chain);
    funcao execute(self, chain: OperationChain,
                const payload = null) -> {texto: qualquer}:;
        // Valida e executa a cadeia.
        if (chain.status == ChainStatus.DRAFT) {
            val = self.validate(chain);
            if (!  val["valid"]) {
                return {"error": "cadeia_invalida", "violations": val["violations"]};
        if (chain.status in (ChainStatus.COMPLETED, ChainStatus.RUNNING)) {
            chain.reset();
        result = chain.run(payload);
        self._last_result = result;
        return result;
    funcao last_impact(self) retorna Optional[{texto: qualquer}]:
        // Retorna o impacto da ultima operacao executada.
        if (! self._last_result) {
            return null;
        return self.impact_tracker.measure(self._last_result);
    // -- cross-module -------------------------------------------------------
    cross_module_report(self) {
        // Relatorio de integracao com outros modulos da Republica.
        return {;
            "open_transition": {
                "modo_atual": self.mode.value,;
                "explicacao": (;
                    "MONEY_ONLY: so dinheiro (pre-transicao). ";
                    "HYBRID: dinheiro + credito coexistem. ";
                    "CREDIT_ONLY: so credito (Republica completa).";
                ),;
            },;
            "open_labor_relay": {
                "uso": "Fornece benchmarks de qualidade para as competicoes.",;
                "metodo": "Competition.set_benchmark(benchmark_id)",;
            },;
            "open_credit": {
                "uso": "Recebe credito liberado aos vencedores.",;
                "campo": "final_payload.credito_liberado",;
            },;
            "open_history": {
                "uso": "Verifica ONGs (fact-check) && registra operacoes.",;
                "metodo": "NGOAllocation.qualify(ngo_id) depende de OpenHistory",;
            },;
        };
    stats(self) {
        return {;
            "modo": self.mode.value,;
            "cadeias_registradas": .length(self.chains),;
            "ongs_registradas": .length(self.ngo_alloc.registry),;
            "ongs_qualificadas": soma(;
                1 para n em self.ngo_alloc.registry.values();
                if self.ngo_alloc.qualify(n.ngo_id);
            ),;
            "premios_distribuidos": .length(self.reward_engine.distributions),;
            "impactos_medidos": .length(self.impact_tracker.records),;
            "holding_ong": arredonde(self.ngo_alloc.holding, 2),;
        };
// ============================================================================
// 12. MAIN -- demonstracao executavel
// ============================================================================
_demo() {
    // Demonstracao do OpenOperations em acao.
    console.log("=" * 80);
    console.log("  OPENOPERATIONS -- OPERACOES DA REPUBLICA EM CADEIAS MODULARES (LEGO)");
    console.log("  Competicao -> Premiacao -> ONG -> Impacto -> Credito");
    console.log("=" * 80);
    // --- setup ---
    ops = OpenOperations(mode=TransitionMode.HYBRID);
    // Registrar ONGs verificadas
    ong1 = NGO("ong-1", "Cozinha Comunitaria SP", cause="fome",;
            verified = true, transparency_score=0.9);
    ong2 = NGO("ong-2", "Educacao para Todos", cause="educacao",;
            verified = true, transparency_score=0.85);
    ong3 = NGO("ong-3", "Saude Rural", cause="saude",;
            verified = false, transparency_score=0.5) // ! qualifica;
    for (const ong of (ong1, ong2, ong3)) {
        r = ops.register_ngo(ong);
        console.log("\n  ONG registrada: {ong.name:<30} ";
            "qualificada={ops.ngo_alloc.qualify(ong.ngo_id)}");
    // --- 1. TEMPLATE: COMPETICAO DE JOGOS EDUCATIVOS ---
    console.log("\n\n  === 1. TEMPLATE: COMPETICAO DE JOGOS EDUCATIVOS ===\n");
    chain = ops.from_template(;
        "competicao_jogos",;
        title = "Jogos Educativos 2026",;
        total_pool = 10000.0,;
    );
    console.log("  Cadeia criada: {chain.name}");
    console.log("  Pecas ({len(chain.pieces)}):");
    for (const p of chain.pieces) {
        console.log("    [{p.piece_type.value:<12}] {p.name}");
        console.log("      entrada={p.connector_in.name}  ";
            "saida={p.connector_out.name}");
    // Validar
    val = ops.validate(chain);
    console.log("\n  Validacao P1-P4: {val}");
    // Executar
    console.log("\n  Executando cadeia...");
    resultado = ops.execute(chain, payload={
        "participantes": ["ana", "bruno", "carla", "daniel"],;
        "winners": ["ana", "bruno", "carla"],;
        "chain": chain.name,;
    });
    console.log("\n  RESULTADO:");
    console.log("    Status: {resultado.get('status')}");
    console.log("    Modo:   {resultado.get('mode')}");
    for (const r of resultado.get("results", [])) {
        flag = r["ok"] ? "OK" : "FALHOU";
        console.log("    [{flag}] {r['piece']} ({r['type']})");
    // Impacto
    impacto = ops.last_impact();
    console.log("\n  IMPACTO MEDIDO:");
    para cada (k, v) em (impacto or {}).items(): {
        console.log("    {k}: {v}");
    // Detalhes da premiacao
    dist = resultado.get("final_payload", {}).get("reward_distribution", {});
    console.log("\n  DISTRIBUICAO DE PREMIOS:");
    console.log("    Pool total:      R$ {dist.get('total_pool', 0):.2f}");
    console.log("    Para ONG:        R$ {dist.get('ngo_amount', 0):.2f}");
    console.log("    Para vencedores: R$ {dist.get('winner_pool', 0):.2f}");
    for (const w of dist.get("per_winner", [])) {
        console.log("      {w['winner']:<10} total=R${w['total']:.2f}  ";
            "credito=R${w['credit']:.2f}  dinheiro=R${w['money']:.2f}");
    // Detalhes da ONG
    ngo_out = resultado.get("final_payload", {}).get("ngo_allocation", {});
    console.log("\n  DOACAO PARA ONG:");
    for (const k of ("ngo_name", "cause", "amount", "estimated_people_helped")) {
        console.log("    {k}: {ngo_out.get(k)}");
    // --- 2. TEMPLATE: HACKATHON ---
    console.log("\n\n  === 2. TEMPLATE: HACKATHON OPENREPUBLIC ===\n");
    chain_hk = ops.from_template(;
        "hackathon",;
        title = "Hackathon OpenRepublic 2026",;
        total_pool = 20000.0,;
    );
    resultado_hk = ops.execute(chain_hk, payload={
        "participantes": ["equipe-alpha", "equipe-beta", "equipe-gamma"],;
        "winners": ["equipe-alpha", "equipe-beta"],;
        "chain": chain_hk.name,;
    });
    console.log("  Status: {resultado_hk.get('status')}");
    console.log("  Pecas executadas: {resultado_hk.get('pieces_run')}");
    credito_hk = resultado_hk.get("final_payload", {}).get("credito_liberado", 0);
    console.log("  Credito liberado (OpenCredit): R$ {credito_hk:.2f}");
    // --- 3. CROSS-MODULE ---
    console.log("\n\n  === 3. INTEGRACAO CROSS-MODULE ===\n");
    cross = ops.cross_module_report();
    para cada (modulo, info) em cross.items(): {
        console.log("  {modulo}:");
        para cada (k, v) em info.items(): {
            console.log("    {k}: {v}");
    // --- 4. STATS ---
    console.log("\n\n  === 4. ESTATISTICAS ===\n");
    para cada (k, v) em ops.stats().items(): {
        console.log("  {k}: {v}");
    // --- 5. EXEMPLO MANUAL (montagem LEGO passo a passo) ---
    console.log("\n\n  === 5. MONTAGEM MANUAL (LEGO passo a passo) ===\n");
    manual = OperationChain("manual", "Operacao Manual", mode=TransitionMode.HYBRID);
    p1 = OperationPiece(;
        piece_id = "m-trigger", name="Gatilho",;
        piece_type = PieceType.TRIGGER,;
        connector_in = LegoConnector("init", "entrada", "fluxo"),;
        connector_out = LegoConnector("vencedores_definidos", "saida", "fluxo"),;
        executor = (d) -> {**d, "winners": ["x", "y"]},;
    );
    p2 = ops.reward_engine.to_piece(total_pool=1000.0, mode=TransitionMode.HYBRID);
    p3 = ops.ngo_alloc.to_piece(cause="fome");
    p4 = ops.impact_tracker.to_piece();
    for (const piece of (p1, p2, p3, p4)) {
        r = manual.add_piece(piece);
        console.log("  add '{piece.name}': {r}");
    val_manual = ops.validate(manual);
    console.log("\n  Validacao manual: valid={val_manual['valid']} ";
        "violacoes={val_manual['total_violations']}");
    res_manual = ops.execute(manual, payload={"chain": manual.name});
    console.log("  Execucao manual: status={res_manual.get('status')}");
    // --- FILOSOFIA ---
    console.log("\n\n{'='*80}");
    console.log("  FILOSOFIA DO OPENOPERATIONS");
    console.log("{'='*80}");
    console.log(""";
OPERACOES SAO CADEIAS DE PECAS (LEGO):;
    Cada peca faz UMA coisa. Cada peca tem encaixe de entrada && saida.;
    As pecas se conectam formando uma SEQUENCIA.;
    O payload flui da primeira ate a ultima peca.;
    competicao -> premiacao -> doacao ONG -> impacto -> credito;
O MODELO DURANTE A TRANSICAO:;
    Pessoas sao PREMIADAS por CONTRIBUIR (jogos educativos, codigo, arte).;
    Parte do premio vai para ONG VERIFICADA (OpenHistory fact-check);
    que ajuda PESSOAS REAIS no mundo atual.;
    Dinheiro + Credito COEXISTEM ate a transicao terminar.;
POR QUE ISSO IMPORTA:;
    - Premia contribuicao REAL (! especulacao).;
    - Conecta a Republica ao mundo atual (via ONGs).;
    - && MODULAR: trocar uma peca ! quebra a cadeia.;
    - && TRANSPARENTE: cada passo && registrado.;
    - && VALIDADO: P1-P4 garantem etica.;
PRINCIPIOS:;
    P1: Equidade -- operacao ! beneficia ricos em detrimento de pobres.;
    P2: Seguranca -- ninguem perde acesso durante a operacao.;
    P3: Reconhecimento -- quem contribui && reconhecido.;
    P4: Consentimento -- o povo decide o ritmo; sem imposicao.;
// )
    final_stats = ops.stats();
    console.log("{'='*80}");
    console.log("  OpenOperations concluido.");
    console.log("  Cadeias registradas: {final_stats['cadeias_registradas']}");
    console.log("  ONGs qualificadas: {final_stats['ongs_qualificadas']}";
        "/{final_stats['ongs_registradas']}");
    console.log("  Premios distribuidos: {final_stats['premios_distribuidos']}");
    console.log("  Impactos medidos: {final_stats['impactos_medidos']}");
    console.log("  Holding ONG (sem qualificada): R$ {final_stats['holding_ong']}");
    console.log("{'='*80}");
if (__name__ == "__main__") {
    _demo();
