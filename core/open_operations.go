// OpenOperations -- Gestao de Operacoes da Republica em Cadeias Modulares (LEGO) -- gerado de Portugol++
package openoperations_gestao_de_operacoes_da_republica_em_cadeias_modulares_lego

import "fmt"

// !/usr/bin/env python3
// -*- coding: utf-8 -*-
//
OpenOperations -- Gestao de Operacoes da Republica em Cadeias Modulares (LEGO)
================================================================================
"Operacoes sao CADEIAS de pecas que encaixam como LEGO.
Cada peca tem um encaixe de ENTRADA && um encaixe de SAIDA.
Uma operacao so comeca quando a peca anterior TERMINA.
Exemplo de cadeia:
competicao -> premiacao -> doacao ONG -> impacto -> credito
O MODELO DURANTE A TRANSICAO (hibrido):
- Pessoas sao PREMIADAS por CONTRIBUIR (ex: desenvolver jogos educativos).
- Parte do premio vai para uma ONG VERIFICADA (OpenHistory fact-check)
    que ajuda pessoas REAIS no mundo atual.
- Dinheiro + Credito COEXISTEM ate a transicao terminar.
- No fim da transicao, so existe credito de acesso (OpenCredit).
O QUE ISTO FAZ:
1. DEFINE pecas modulares (OperationPiece) com conectores LEGO
2. MONTA cadeias (OperationChain) -- sequencias de pecas encaixadas
3. ORGANIZA competicoes (jogos, codigo, arte)
4. DISTRIBUI premios (RewardEngine) -- credito + dinheiro durante transicao
5. ALOCA parte para ONG verificada (NGOAllocation)
6. MEDE impacto real de cada operacao (ImpactTracker)
7. VALIDA cadeias (ChainValidator) -- P1-P4
8. OFERECE templates reusaveis (competicao, leilao, hackathon)
9. CONECTA com OpenTransition, OpenLaborRelay, OpenCredit
10. FUNCIONA no modelo antigo && no novo (transicao hibrida)
Author: OpenRepublic Team
Licenca: CC0 (Dominio Publico) -- https://creativecommons.org/publicdomain/zero/1.0/
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
type OperationPrinciple int
const (
    // Principios que toda operacao da Republica deve respeitar.
    P1_EQUITY = (1, "Equidade", "Operacao ! beneficia ricos em detrimento de pobres")
    P2_SAFETY = (2, "Seguranca", "Ninguem morre nem perde acesso durante a operacao")
    P3_RECOGNITION = (3, "Reconhecimento", "Quem contribui && reconhecido")
    P4_CONSENT = (4, "Consentimento", "O povo decide o ritmo; sem imposicao")
type PieceType int
const (
    // Tipos de peca que podem compor uma cadeia de operacao.
    TRIGGER = "gatilho"  // dispara a cadeia (competicao abre)
    COMPETITION = "competicao"  // organizacao de competicao
    JUDGING = "julgamento"  // avaliacao de contribuicoes
    REWARD = "premiacao"  // distribuicao de premios
    NGO = "doacao_ong"  // alocacao para ONG verificada
    IMPACT = "impacto"  // medicao de impacto real
    CREDIT = "credito"  // liberacao de credito (OpenCredit)
    MONEY = "dinheiro"  // pagamento em dinheiro (durante transicao)
    NOTIFY = "notificacao"  // avisar partes interessadas
    ARCHIVE = "arquivo"  // registrar no OpenHistory
type ChainStatus int
const (
    // Estado de uma cadeia de operacao.
    DRAFT = "rascunho"  // montando, ! validada
    VALIDATED = "validada"  // passou no ChainValidator
    RUNNING = "em_execucao"  // pecas estao rodando
    PAUSED = "pausada"  // intermediaria pausada
    COMPLETED = "completa"  // todas as pecas terminaram
    FAILED = "falhou"  // uma peca falhou && ! recuperou
type TransitionMode int
const (
    // Modo da operacao conforme a fase da transicao (OpenTransition).
    Permite que a mesma operacao funcione no modelo antigo && no novo.
    //
    MONEY_ONLY = "so_dinheiro"  // sistema antigo puro (pre-transicao)
    HYBRID = "hibrido"  // dinheiro + credito coexistem
    CREDIT_ONLY = "so_credito"  // Republica completa (pos-transicao)
// ============================================================================
// 2. CONNECTOR -- o encaixe LEGO entre pecas
// ============================================================================
// decorador: @dataclass
type LegoConnector struct {
    // Encaixe LEGO que permite conectar duas pecas.
    Cada peca tem um connector de ENTRADA && um de SAIDA.
    Dois conectores so encaixam se forem COMPATIVEIS (mesmo formato).
    Analogia:
    - Peca A saida: 'premio_distribuido'
    - Peca B entrada: 'premio_recebido'
    - Se compatibilidade bate, encaixam.
    //
    name: texto                           // ex: 'premio_distribuido'
    direction: texto                      // 'entrada' || 'saida'
    shape: texto                          // tipo de encaixe: 'fluxo', 'valor', 'evento'
    description := "" // string
    func encaixa_com(self, other: "LegoConnector") bool {
        // Verifica se este connector encaixa com outro.
        if self.direction == other.direction {
            return false // entrada ! encaixa com entrada
        if self.shape != other.shape {
            return false
        // saida deve ter o mesmo nome base da entrada (ou curinga)
        if self.name == "*"  ||  other.name == "*" {
            return true
        return self.name == other.name
// ============================================================================
// 3. OPERATION PIECE -- uma peca modular da cadeia
// ============================================================================
// decorador: @dataclass
type OperationPiece struct {
    // Uma peca modular que se encaixa numa cadeia de operacao.
    Analogia LEGO:
    - Cada peca faz UMA coisa (competicao, premiacao, doacao...).
    - Cada peca tem um connector de ENTRADA && um de SAIDA.
    - Pecas se encaixam formando uma cadeia sequencial.
    Execucao:
    - A peca so executa quando a anterior TERMINA && passa o 'payload'.
    - O payload && um dicionario que carrega dados pela cadeia.
    //
    piece_id: texto
    name: texto
    piece_type: PieceType
    connector_in: LegoConnector
    connector_out: LegoConnector
    description := "" // string
    // Funcao que executa a logica da peca. Recebe o payload, retorna payload.
    executor := nil // Optional[Callable[[{texto: qualquer}], {texto: qualquer}]]
    // Parametros especificos da peca (ex: limite de tempo, regras)
    params := field(default_factory=dict) // {texto: qualquer}
    // Estado da execucao
    executed := false // bool
    result := nil // Optional[{texto: qualquer}]
    error := nil // texto?
    // decorador: @property
    func is_entry(self) bool {
        // Peca de entrada: nao precisa de peca anterior.
        return self.connector_in.name == "init"  ||  self.connector_in.name == "*"
    // decorador: @property
    func is_terminal(self) bool {
        // Peca terminal: nao precisa de peca seguinte.
        return self.connector_out.name == "end"  ||  self.connector_out.name == "*"
    func run(self, payload: {texto: qualquer}) {texto: qualquer} {
        // Executa a peca com o payload recebido.
        if self.executor && nil {
            // Peca sem executor so repassa o payload
            self.result = dict(payload)
            self.executed = true
            return self.result
        tente:
            self.result = self.executor(payload)
            self.executed = true
            self.error = nil
            return self.result
        capture Exception como exc:
            self.error = texto(exc)
            self.result = {"_error": self.error, "_piece": self.piece_id}
            return self.result
// ============================================================================
// 4. OPERATION CHAIN -- cadeia de pecas encaixadas
// ============================================================================
type OperationChain struct {
    // Cadeia de pecas modulares encaixadas como LEGO.
    A cadeia && uma SEQUENCIA. Cada peca encaixa na seguinte.
    O payload flui da primeira ate a ultima peca.
    Exemplo:
        chain = OperationChain("cadeia-jogos", "Jogos Educativos")
        chain.add_piece(p_competicao)
        chain.add_piece(p_premiacao)
        chain.add_piece(p_ong)
        chain.add_piece(p_impacto)
        chain.add_piece(p_credito)
        chain.run({"participantes": [...]})
    //
    funcao __init__(self, chain_id: texto, name: texto,
                mode := TransitionMode.HYBRID): // TransitionMode
        self.chain_id = chain_id
        self.name = name
        self.mode = mode
        self.pieces: [OperationPiece] = []
        self.status: ChainStatus = ChainStatus.DRAFT
        self.initial_payload: {texto: qualquer} = {}
        self.execution_log: deque = deque(maxlen=500)
    // -- montagem -----------------------------------------------------------
    func add_piece(self, piece: OperationPiece) {texto: qualquer} {
        // Adiciona uma peca ao final da cadeia, verificando o encaixe.
        if self.pieces {
            prev = self.pieces[-1]
            if ! prev.connector_out.encaixa_com(piece.connector_in) {
                return {
                    "error": "encaixe_incompativel",
                    "anterior": prev.name,
                    "saida": prev.connector_out.name,
                    "nova": piece.name,
                    "entrada": piece.connector_in.name,
                }
        self.pieces.append(piece)
        self.execution_log.append(
            {"event": "piece_added", "piece": piece.piece_id,
            "time": datetime.now().isoformat()}
        )
        return {"added": true, "total_pieces": len(self.pieces)}
    func insert_piece(self, index: inteiro, piece: OperationPiece) {texto: qualquer} {
        // Insere peca numa posicao especifica, revalidando encaixes.
        self.pieces.insert(index, piece)
        return {"inserted": true, "index": index}
    func remove_piece(self, piece_id: texto) {texto: qualquer} {
        // Remove peca pelo ID e reencadeia.
        before = len(self.pieces)
        self.pieces = [p para p em self.pieces if p.piece_id != piece_id]
        return {"removed": before != len(self.pieces),
                "total_pieces": len(self.pieces)}
    // -- execucao -----------------------------------------------------------
    func run(self, payload: Optional[{texto: qualquer}] = None) {texto: qualquer} {
        // Executa a cadeia inteira, passando o payload de peca em peca.
        if ! self.pieces {
            return {"error": "cadeia_vazia"}
        if payload && ! None {
            self.initial_payload = payload
        self.status = ChainStatus.RUNNING
        current = dict(self.initial_payload)
        current["_mode"] = self.mode.value
        results := [] // List[{texto: qualquer}]
        para cada (i, piece) em enumere(self.pieces): {
            self.execution_log.append(
                {"event": "piece_start", "index": i,
                "piece": piece.piece_id,
                "time": datetime.now().isoformat()}
            )
            current = piece.run(current)
            results.append({
                "piece": piece.name,
                "type": piece.piece_type.value,
                "ok": piece.executed  &&  !  piece.error,
                "error": piece.error,
            })
            self.execution_log.append(
                {"event": "piece_end", "index": i,
                "piece": piece.piece_id,
                "ok": piece.executed  &&  !  piece.error,
                "time": datetime.now().isoformat()}
            )
            if piece.error {
                self.status = ChainStatus.FAILED
                break
        if self.status != ChainStatus.FAILED {
            self.status = ChainStatus.COMPLETED
        return {
            "chain": self.name,
            "status": self.status.value,
            "mode": self.mode.value,
            "pieces_run": len(results),
            "results": results,
            "final_payload": current,
        }
    func reset(self) None {
        // Limpa estado de execucao para permitir re-rodar.
        for _, p := range self.pieces {
            p.executed = false
            p.result = nil
            p.error = nil
        self.status = ChainStatus.DRAFT
// ============================================================================
// 5. COMPETITION -- organizacao de competicoes
// ============================================================================
// decorador: @dataclass
type Participant struct {
    // Participante de uma competicao.
    participant_id: texto
    name: texto
    category := ""  // ex: 'jogos', 'codigo', 'arte' // string
    submission := ""  // descricao da contribuicao // string
    score := 0.0 // pontuacao do juri // float64
    rank := 0 // classificacao final // int64
type Competition struct {
    // Organiza competicoes dentro da Republica.
    Competicoes sao uma forma de PREMIAR CONTRIBUICAO:
    - Pessoas criam jogos educativos, escrevem codigo, fazem arte.
    - Um juri avalia as contribuicoes contra um benchmark (OpenLaborRelay).
    - Os melhores recebem premio (credito + dinheiro durante transicao).
    - Parte do premio vai para ONG verificada.
    PRINCIPIOS DA COMPETICAO:
    - Transparente: criterios && notas sao publicos.
    - Inclusiva: qualquer cidadao pode participar.
    - Justa: benchmark de qualidade evita subjetividade.
    - Educativa: feedback do juri ajuda a melhorar.
    //
    funcao __init__(self, comp_id: texto, title: texto, category: texto = "jogos",
                mode := TransitionMode.HYBRID): // TransitionMode
        self.comp_id = comp_id
        self.title = title
        self.category = category
        self.mode = mode
        self.participants: {texto: Participant} = {}
        self.jury: [texto] = [] // ids dos jurados
        self.rules: {texto: qualquer} = {
            "min_participants": 3,
            "max_winners": 3,
            "requires_benchmark": true,
            "transparency": true,
        }
        self.benchmark: texto? = nil // referencia OpenLaborRelay
        self.results: Optional[[Participant]] = nil
    func add_participant(self, participant: Participant) {texto: qualquer} {
        self.participants[participant.participant_id] = participant
        return {"added": true, "total": len(self.participants)}
    func set_jury(self, juror_ids: [texto]) {texto: qualquer} {
        self.jury = juror_ids
        return {"jury_size": len(self.jury)}
    func set_benchmark(self, benchmark_id: texto) {texto: qualquer} {
        // Define o benchmark de qualidade (vindo do OpenLaborRelay).
        self.benchmark = benchmark_id
        return {"benchmark": benchmark_id}
    func judge(self, scores: {texto: flutuante}) {texto: qualquer} {
        // Aplica notas e classifica participantes.
        scores: { participant_id: score_float }
        //
        if len(self.participants) < self.rules["min_participants"] {
            return {"error": "participantes_insuficientes",
                    "min": self.rules["min_participants"]}
        para cada (pid, score) em scores.items(): {
            if pid in self.participants {
                self.participants[pid].score = flutuante(score)
        ranked = ordene(self.participants.values(),
                        key = (p) -> p.score, reverse=true)
        para cada (i, p) em enumere(ranked, start=1): {
            p.rank = i
        self.results = ranked
        return {
            "judged": true,
            "winners": [p.name para p em ranked[: self.rules["max_winners"]]],
            "total_scored": len(scores),
        }
    func to_piece(self) OperationPiece {
        // Transforma esta competicao numa peca LEGO da cadeia.
        func executor(payload: {texto: qualquer}) {texto: qualquer} {
            data = dict(payload)
            data["competition"] = self.title
            data["category"] = self.category
            // Se a competicao foi julgada, usa os resultados reais.
            // Caso contrario, preserva winners vindos do payload.
            if self.results {
                data["winners"] = [
                    p.name para p em self.results[: self.rules["max_winners"]]
                ]
            } else {
                data.setdefault("winners", [])
            // Preserva contagem de participantes do payload se houver.
            // Aceita tanto 'all_participants' (int) quanto 'participantes' (lista).
            if "all_participants" in data {
                count = data["all_participants"]
            } else if "participantes" in data {
                count = len(data["participantes"])
            } else {
                count = len(self.participants)
            data["all_participants"] = count
            return data
        return OperationPiece(
            piece_id = "comp-{self.comp_id}",
            name = "Competicao: {self.title}",
            piece_type = PieceType.COMPETITION,
            connector_in = LegoConnector("init", "entrada", "fluxo"),
            connector_out = LegoConnector("vencedores_definidos", "saida", "fluxo"),
            description = "Competicao de {self.category}: {self.title}",
            executor = executor,
            params = {"category": self.category, "benchmark": self.benchmark},
        )
// ============================================================================
// 6. REWARD ENGINE -- distribuicao de premios (hibrido durante transicao)
// ============================================================================
// decorador: @dataclass
type RewardSplit struct {
    // Como um premio e dividido.
    Duas dimensoes independentes:
    - ngo_pct: fracao do TOTAL do premio que vai para ONG (0-1).
    - credit_pct / money_pct: como o RESTANTE (winner_pool) && dividido
    entre o vencedor, em credito (Republica) && dinheiro (transicao).
    credit_pct + money_pct DEVE somar 1.0.
    //
    credit_pct := 0.6 // fracao do winner_pool em credito // float64
    money_pct := 0.4 // fracao do winner_pool em dinheiro // float64
    ngo_pct := 0.2 // fracao do total que vai para ONG // float64
    func validate(self) bool {
        // Garante que as fracoes sao coerentes.
        winner_ok = abs((self.credit_pct + self.money_pct) - 1.0) < 0.01
        ngo_ok = 0.0 <= self.ngo_pct <= 1.0
        ranges_ok = (0.0 <= self.credit_pct <= 1.0
                    && 0.0 <= self.money_pct <= 1.0)
        return winner_ok && ngo_ok && ranges_ok
type RewardEngine struct {
    // Distribui premios de forma hibrida durante a transicao.
    MODELO HIBRIDO:
    - Durante a transicao, o premio tem duas pernas:
    (a) CREDITO -- vai para a conta OpenCredit do vencedor.
    (b) DINHEIRO -- vai para a conta bancaria do vencedor (modelo antigo).
    - Uma fracao do TOTAL do premio && SEMPRE desviada para uma ONG verificada.
    - Conforme a transicao avanca (OpenTransition), money_pct cai para 0.
    TRANSICAO DO SPLIT:
    Modo MONEY_ONLY: 0% credito, 100% dinheiro, 10% ONG
    Modo HYBRID: 60% credito, 40% dinheiro, 20% ONG
    Modo CREDIT_ONLY: 80% credito, 0% dinheiro, 20% ONG
    //
    func __init__(self) {
        self.distributions: List[{texto: qualquer}] = []
    func default_split(self, mode: TransitionMode) RewardSplit {
        // Retorna o split padrao conforme o modo da transicao.
        defaults = {
            TransitionMode.MONEY_ONLY: RewardSplit(0.0, 1.0, 0.10),
            TransitionMode.HYBRID: RewardSplit(0.6, 0.4, 0.20),
            TransitionMode.CREDIT_ONLY: RewardSplit(1.0, 0.0, 0.20),
        }
        return defaults[mode]
    funcao distribute(self, total_pool: flutuante, winners: [texto],
                mode := TransitionMode.HYBRID, // TransitionMode
                split := nil) -> {texto: qualquer}: // RewardSplit?
        // Distribui o pool de premios entre os vencedores + ONG.
        A fracao do ONG && retirada PRIMEIRO. O resto && dividido entre os
        vencedores conforme o split credito/dinheiro.
        //
        if ! winners {
            return {"error": "sem_vencedores"}
        split = split || self.default_split(mode)
        if ! split.validate() {
            return {"error": "split_invalido"}
        ngo_amount = arredonde(total_pool * split.ngo_pct, 2)
        winner_pool = arredonde(total_pool - ngo_amount, 2)
        // Distribuicao ponderada por rank (1o > 2o > 3o)
        weights = self._rank_weights(len(winners))
        per_winner := [] // List[{texto: qualquer}]
        para cada (w, name) em intercale(weights, winners): {
            share = arredonde(winner_pool * w, 2)
            credit_part = arredonde(share * split.credit_pct, 2)
            money_part = arredonde(share * split.money_pct, 2)
            per_winner.append({
                "winner": name,
                "share_pct": arredonde(w * 100, 1),
                "total": share,
                "credit": credit_part,
                "money": money_part,
            })
        result = {
            "total_pool": total_pool,
            "mode": mode.value,
            "ngo_amount": ngo_amount,
            "winner_pool": winner_pool,
            "split": {
                "credit_pct": split.credit_pct,
                "money_pct": split.money_pct,
                "ngo_pct": split.ngo_pct,
            },
            "per_winner": per_winner,
        }
        self.distributions.append(result)
        return result
    // decorador: @staticmethod
    func _rank_weights(n: inteiro) [flutuante] {
        // Pesos por posicao: 1o, 2o, 3o... (soma 1.0).
        if n <= 0 {
            return []
        // distribuicao 50% / 30% / 20% para 3; generica para N
        raw = [1.0 / (i + 1) para i em intervalo(n)] // harmonico
        total = soma(raw)
        return [r / total para r em raw]
    funcao to_piece(self, total_pool: flutuante,
                mode := TransitionMode.HYBRID) -> OperationPiece: // TransitionMode
        // Transforma o RewardEngine numa peca LEGO da cadeia.
        engine = self
        func executor(payload: {texto: qualquer}) {texto: qualquer} {
            data = dict(payload)
            winners = data.get("winners", [])
            dist = engine.distribute(total_pool, winners, mode=mode)
            data["reward_distribution"] = dist
            return data
        return OperationPiece(
            piece_id = "reward-engine",
            name = "Premiacao (credito + dinheiro)",
            piece_type = PieceType.REWARD,
            connector_in = LegoConnector("vencedores_definidos", "entrada", "fluxo"),
            connector_out = LegoConnector("premio_distribuido", "saida", "fluxo"),
            description = "Distribui premio: credito + dinheiro durante transicao",
            executor = executor,
            params = {"total_pool": total_pool, "mode": mode.value},
        )
// ============================================================================
// 7. NGO ALLOCATION -- parte vai para ONG verificada
// ============================================================================
// decorador: @dataclass
type NGO struct {
    // ONG verificada que recebe parte dos premios.
    ngo_id: texto
    name: texto
    cause: texto                          // ex: 'fome', 'educacao', 'saude'
    verified := false // checada por OpenHistory // bool
    people_helped_lifetime := 0 // int64
    transparency_score := 0.0 // 0-1 // float64
type NGOAllocation struct {
    // Aloca a fracao de ONG do premio para uma ONG verificada.
    CRITERIOS:
    - A ONG DEVE ser verificada por OpenHistory (fact-check).
    - A ONG DEVE ter score de transparencia >= 0.7.
    - O destino do dinheiro && PUBLICO (OpenHistory registra).
    - Se nenhuma ONG qualifica, o valor fica em HOLDING ate qualificar.
    //
    MIN_TRANSPARENCY = 0.7
    func __init__(self) {
        self.registry: {texto: NGO} = {}
        self.allocations: List[{texto: qualquer}] = []
        self.holding: flutuante = 0.0 // valor retido por falta de ONG qualificada
    func register_ngo(self, ngo: NGO) {texto: qualquer} {
        self.registry[ngo.ngo_id] = ngo
        return {"registered": true, "verified": ngo.verified,
                "transparency": ngo.transparency_score}
    func qualify(self, ngo_id: texto) bool {
        // Verifica se a ONG atende aos criterios.
        ngo = self.registry.get(ngo_id)
        if ! ngo {
            return false
        return ngo.verified && ngo.transparency_score >= self.MIN_TRANSPARENCY
    funcao allocate(self, amount: flutuante, cause: texto = "",
                preferred_ngo_id := nil) -> {texto: qualquer}: // texto?
        // Aloca valor para a ONG qualificada mais apropriada.
        candidates = [n para n em self.registry.values() if self.qualify(n.ngo_id)]
        if cause {
            cause_matches = [n para n em candidates if n.cause == cause]
            if cause_matches {
                candidates = cause_matches
        if preferred_ngo_id {
            pref = [n para n em candidates if n.ngo_id == preferred_ngo_id]
            if pref {
                candidates = pref
        if ! candidates {
            self.holding += amount
            return {
                "allocated": false,
                "reason": "sem_ong_qualificada",
                "amount_held": amount,
                "total_holding": self.holding,
            }
        ngo = candidates[0]
        ngo.people_helped_lifetime += self._estimate_people_helped(amount, ngo)
        record = {
            "ngo_id": ngo.ngo_id,
            "ngo_name": ngo.name,
            "cause": ngo.cause,
            "amount": amount,
            "estimated_people_helped": self._estimate_people_helped(amount, ngo),
            "time": datetime.now().isoformat(),
        }
        self.allocations.append(record)
        return {"allocated": true, **record}
    // decorador: @staticmethod
    func _estimate_people_helped(amount: flutuante, ngo: NGO) int64 {
        // Estima quantas pessoas reais serao ajudadas (impacto real).
        // Heuristica simples: R$ 100 ajuda ~1 pessoa (depende da causa).
        per_person = {"fome": 50, "educacao": 200, "saude": 300, "agua": 80}
        base = per_person.get(ngo.cause, 100)
        return maximo(1, inteiro(amount / base))
    func to_piece(self, cause: texto = "") OperationPiece {
        // Transforma o NGOAllocation numa peca LEGO da cadeia.
        alloc = self
        func executor(payload: {texto: qualquer}) {texto: qualquer} {
            data = dict(payload)
            dist = data.get("reward_distribution", {})
            ngo_amount = dist.get("ngo_amount", 0.0)
            result = alloc.allocate(ngo_amount, cause=cause)
            data["ngo_allocation"] = result
            return data
        return OperationPiece(
            piece_id = "ngo-allocation",
            name = "Doacao para ONG verificada",
            piece_type = PieceType.NGO,
            connector_in = LegoConnector("premio_distribuido", "entrada", "fluxo"),
            connector_out = LegoConnector("ong_definida", "saida", "fluxo"),
            description = "Aloca fracao do premio para ONG verificada",
            executor = executor,
            params = {"cause": cause},
        )
// ============================================================================
// 8. IMPACT TRACKER -- mede impacto real de cada operacao
// ============================================================================
type ImpactTracker struct {
    // Mede o impacto REAL de uma operacao da Republica.
    IMPACTO ! && SO NUMERO -- && PESSOA REAL.
    Cada metrica responde: quantas pessoas reais foram ajudadas?
    Metricas:
    - participantes_envolvidos: quantas pessoas participaram
    - pessoas_ajudadas_ong: quantas pessoas reais a ONG ajudou
    - credito_distribuido: quanto credito fluiu para a Republica
    - dinheiro_distribuido: quanto dinheiro fluiu (durante transicao)
    - score_impacto: 0-1 (impacto normalizado)
    //
    func __init__(self) {
        self.records: List[{texto: qualquer}] = []
    func measure(self, chain_result: {texto: qualquer}) {texto: qualquer} {
        // Extrai metricas de impacto do resultado da cadeia.
        final = chain_result.get("final_payload", {})
        dist = final.get("reward_distribution", {})
        ngo = final.get("ngo_allocation", {})
        participantes = final.get(
            "all_participants", len(final.get("participantes", []))
        )
        pessoas_ong = ngo.get("estimated_people_helped", 0)
        credito = soma(w.get("credit", 0) para w em dist.get("per_winner", []))
        dinheiro = soma(w.get("money", 0) para w em dist.get("per_winner", []))
        // Score de impacto: pondera pessoas ajudadas + credito distribuido
        score = self._compute_score(participantes, pessoas_ong, credito)
        record = {
            "chain": chain_result.get("chain", ""),
            "participantes_envolvidos": participantes,
            "pessoas_ajudadas_ong": pessoas_ong,
            "credito_distribuido": arredonde(credito, 2),
            "dinheiro_distribuido": arredonde(dinheiro, 2),
            "score_impacto": arredonde(score, 3),
            "time": datetime.now().isoformat(),
        }
        self.records.append(record)
        return record
    // decorador: @staticmethod
    funcao _compute_score(participantes: inteiro, pessoas_ong: inteiro,
                    credito: flutuante) -> flutuante:
        // importa math
        p = math.log10(maximo(1, participantes + 1))
        o = math.log10(maximo(1, pessoas_ong + 1))
        c = math.log10(maximo(1, credito + 1))
        raw = 0.3 * p + 0.5 * o + 0.2 * c
        // normaliza para 0-1 (assumindo escala tipica)
        return minimo(1.0, raw / 3.0)
    func to_piece(self) OperationPiece {
        // Transforma o ImpactTracker numa peca LEGO da cadeia.
        tracker = self
        func executor(payload: {texto: qualquer}) {texto: qualquer} {
            data = dict(payload)
            chain_result = {"final_payload": data, "chain": data.get("chain", "")}
            impact = tracker.measure(chain_result)
            data["impact"] = impact
            return data
        return OperationPiece(
            piece_id = "impact-tracker",
            name = "Medicao de impacto real",
            piece_type = PieceType.IMPACT,
            connector_in = LegoConnector("ong_definida", "entrada", "fluxo"),
            connector_out = LegoConnector("impacto_medido", "saida", "fluxo"),
            description = "Mede impacto real: pessoas ajudadas + credito",
            executor = executor,
        )
// ============================================================================
// 9. CHAIN VALIDATOR -- valida cadeias contra P1-P4
// ============================================================================
type ChainValidator struct {
    // Valida se uma cadeia de operacao respeita os principios P1-P4.
    CHECAGENS:
    - P1 (Equidade): todo vencedor recebe algo; ngao concentrado em 1.
    - P2 (Seguranca): nenhuma peca remove acesso essencial.
    - P3 (Reconhecimento): existe peca de premiacao || de impacto.
    - P4 (Consentimento): modo da cadeia && explicito (! imposto).
    VALIDACAO ESTRUTURAL:
    - A cadeia tem pelo menos uma peca de entrada.
    - A cadeia tem pelo menos uma peca terminal.
    - Todos os encaixes batem (LEGO connectors compatíveis).
    //
    func __init__(self) {
        self.violations: List[{texto: qualquer}] = []
    func validate(self, chain: OperationChain) {texto: qualquer} {
        // Valida a cadeia e retorna lista de violacoes.
        self.violations = []
        self._validate_structure(chain)
        self._validate_p1(chain)
        self._validate_p2(chain)
        self._validate_p3(chain)
        self._validate_p4(chain)
        ok = len(self.violations) == 0
        if ok {
            chain.status = ChainStatus.VALIDATED
        return {
            "valid": ok,
            "violations": self.violations,
            "total_violations": len(self.violations),
            "chain_status": chain.status.value,
        }
    func _add(self, principle: texto, message: texto) None {
        self.violations.append({"principle": principle, "message": message})
    func _validate_structure(self, chain: OperationChain) None {
        if ! chain.pieces {
            self._add("estrutura", "Cadeia sem pecas")
            return nil
        // Encaixes consecutivos
        for _, i := range intervalo(len(chain.pieces) - 1) {
            a = chain.pieces[i]
            b = chain.pieces[i + 1]
            if ! a.connector_out.encaixa_com(b.connector_in) {
                self._add(
                    "estrutura",
                    "Encaixe quebrado entre '{a.name}' && '{b.name}'",
                )
        // Entrada e saida
        first = chain.pieces[0]
        if !  (first.is_entry  ||  first.connector_in.direction == "entrada") {
            self._add("estrutura", "Primeira peca ! && ponto de entrada")
        last = chain.pieces[-1]
        if !  (last.is_terminal  ||  last.connector_out.direction == "saida") {
            self._add("estrutura", "Ultima peca ! && ponto terminal")
    func _validate_p1(self, chain: OperationChain) None {
        // P1 Equidade: cadeia deve ter peca de reward ou de NGO.
        has_reward = any(p.piece_type == PieceType.REWARD para p em chain.pieces)
        has_ngo = any(p.piece_type == PieceType.NGO para p em chain.pieces)
        if ! (has_reward || has_ngo) {
            self._add(
                "P1_equidade",
                "Cadeia sem premiacao nem doacao ONG -- sem distribuicao",
            )
    func _validate_p2(self, chain: OperationChain) None {
        // P2 Seguranca: nenhuma peca com flag 'remove_acesso'.
        for _, p := range chain.pieces {
            if p.params.get("remove_acesso") {
                self._add(
                    "P2_seguranca",
                    "Peca '{p.name}' remove acesso essencial",
                )
    func _validate_p3(self, chain: OperationChain) None {
        // P3 Reconhecimento: deve existir reward ou impact tracker.
        has_reward = any(p.piece_type == PieceType.REWARD para p em chain.pieces)
        has_impact = any(p.piece_type == PieceType.IMPACT para p em chain.pieces)
        if ! (has_reward || has_impact) {
            self._add(
                "P3_reconhecimento",
                "Cadeira sem premiacao nem medicao de impacto",
            )
    func _validate_p4(self, chain: OperationChain) None {
        // P4 Consentimento: modo deve ser explicito.
        if chain.mode ! in TransitionMode {
            self._add("P4_consentimento", "Modo de transicao ! definido")
// ============================================================================
// 10. OPERATION TEMPLATES -- templates reusaveis
// ============================================================================
type OperationTemplates struct {
    // Templates reusaveis de cadeias de operacao.
    Cada template retorna uma OperationChain pronta para uso.
    Os templates sao PONTO DE PARTIDA -- podem ser customizados.
    //
    // decorador: @staticmethod
    funcao competencia_jogos(title: texto = "Competicao de Jogos Educativos",
                        total_pool := 10000.0, // float64
                        mode := TransitionMode.HYBRID, // TransitionMode
                        ngo_alloc := nil, // NGOAllocation?
                        ) -> OperationChain:
        // Template: competicao -> premiacao -> ONG -> impacto -> credito.
        chain = OperationChain("tpl-jogos", title, mode=mode)
        // Peca 1: competicao (placeholder)
        comp = Competition("jogos", title, category="jogos", mode=mode)
        chain.add_piece(comp.to_piece())
        // Peca 2: reward engine
        reward = RewardEngine()
        chain.add_piece(reward.to_piece(total_pool=total_pool, mode=mode))
        // Peca 3: ONG allocation
        alloc = ngo_alloc || NGOAllocation()
        chain.add_piece(alloc.to_piece(cause="educacao"))
        // Peca 4: impacto
        chain.add_piece(ImpactTracker().to_piece())
        // Peca 5: credito (registra credito liberado no OpenCredit)
        func credito_executor(payload: {texto: qualquer}) {texto: qualquer} {
            data = dict(payload)
            dist = data.get("reward_distribution", {})
            credito_total = soma(w.get("credit", 0) para w em dist.get("per_winner", []))
            data["credito_liberado"] = arredonde(credito_total, 2)
            data["destino"] = "OpenCredit"
            return data
        chain.add_piece(OperationPiece(
            piece_id = "credito-release",
            name = "Liberacao de credito (OpenCredit)",
            piece_type = PieceType.CREDIT,
            connector_in = LegoConnector("impacto_medido", "entrada", "fluxo"),
            connector_out = LegoConnector("end", "saida", "fluxo"),
            description = "Libera credito no OpenCredit para os vencedores",
            executor = credito_executor,
        ))
        return chain
    // decorador: @staticmethod
    funcao leilao_arte(title: texto = "Leilao de Arte Comunitaria",
                    total_pool := 5000.0, // float64
                    mode := TransitionMode.HYBRID, // TransitionMode
                    ngo_alloc := nil, // NGOAllocation?
                    ) -> OperationChain:
        // Template: competicao(arte) -> premiacao -> ONG -> impacto.
        chain = OperationChain("tpl-leilao", title, mode=mode)
        comp = Competition("arte", title, category="arte", mode=mode)
        chain.add_piece(comp.to_piece())
        reward = RewardEngine()
        chain.add_piece(reward.to_piece(total_pool=total_pool, mode=mode))
        alloc = ngo_alloc || NGOAllocation()
        chain.add_piece(alloc.to_piece(cause="fome"))
        chain.add_piece(ImpactTracker().to_piece())
        return chain
    // decorador: @staticmethod
    funcao hackathon(title: texto = "Hackathon OpenRepublic",
                total_pool := 20000.0, // float64
                mode := TransitionMode.HYBRID, // TransitionMode
                ngo_alloc := nil, // NGOAllocation?
                ) -> OperationChain:
        // Template: competicao(codigo) -> premiacao -> ONG -> impacto -> credito.
        chain = OperationChain("tpl-hackathon", title, mode=mode)
        comp = Competition("codigo", title, category="codigo", mode=mode)
        chain.add_piece(comp.to_piece())
        reward = RewardEngine()
        chain.add_piece(reward.to_piece(total_pool=total_pool, mode=mode))
        alloc = ngo_alloc || NGOAllocation()
        chain.add_piece(alloc.to_piece(cause="educacao"))
        chain.add_piece(ImpactTracker().to_piece())
        func credito_executor(payload: {texto: qualquer}) {texto: qualquer} {
            data = dict(payload)
            dist = data.get("reward_distribution", {})
            credito_total = soma(w.get("credit", 0) para w em dist.get("per_winner", []))
            data["credito_liberado"] = arredonde(credito_total, 2)
            data["destino"] = "OpenCredit"
            return data
        chain.add_piece(OperationPiece(
            piece_id = "credito-release",
            name = "Liberacao de credito (OpenCredit)",
            piece_type = PieceType.CREDIT,
            connector_in = LegoConnector("impacto_medido", "entrada", "fluxo"),
            connector_out = LegoConnector("end", "saida", "fluxo"),
            description = "Libera credito no OpenCredit para os vencedores",
            executor = credito_executor,
        ))
        return chain
// ============================================================================
// 11. OPEN OPERATIONS -- fachada principal (orquestra tudo)
// ============================================================================
type OpenOperations struct {
    // Fachada principal para gestao de operacoes da Republica.
    Integra:
    - OperationChain: cadeias modulares (LEGO)
    - Competition: competicoes
    - RewardEngine: distribuicao hibrida de premios
    - NGOAllocation: doacao para ONG verificada
    - ImpactTracker: medicao de impacto
    - ChainValidator: validacao P1-P4
    - OperationTemplates: templates reusaveis
    CROSS-MODULE:
    - OpenTransition: define o modo (MONEY_ONLY / HYBRID / CREDIT_ONLY)
    - OpenLaborRelay: fornece benchmarks para as competicoes
    - OpenCredit: recebe o credito liberado pelas cadeias
    - OpenHistory: verifica ONGs && registra operacoes
    USO:
        ops = OpenOperations()
        chain = ops.from_template("competicao_jogos", title="Jogos 2026")
        ops.validate(chain)
        resultado = ops.execute(chain, payload={...})
        impacto = ops.last_impact()
    //
    func __init__(self, mode: TransitionMode = TransitionMode.HYBRID) {
        self.mode = mode
        self.chains: {texto: OperationChain} = {}
        self.validator = ChainValidator()
        self.ngo_alloc = NGOAllocation()
        self.reward_engine = RewardEngine()
        self.impact_tracker = ImpactTracker()
        self.templates = OperationTemplates()
        self._last_result: Optional[{texto: qualquer}] = nil
    // -- registro de ONGs --------------------------------------------------
    func register_ngo(self, ngo: NGO) {texto: qualquer} {
        return self.ngo_alloc.register_ngo(ngo)
    // -- cadastro de cadeias ------------------------------------------------
    func register_chain(self, chain: OperationChain) {texto: qualquer} {
        self.chains[chain.chain_id] = chain
        return {"registered": true, "chain_id": chain.chain_id,
                "total_chains": len(self.chains)}
    // -- templates ----------------------------------------------------------
    func from_template(self, template_name: texto, **kwargs) OperationChain {
        // Cria cadeia a partir de template (competicao_jogos, leilao_arte, hackathon).
        kwargs.setdefault("mode", self.mode)
        kwargs.setdefault("ngo_alloc", self.ngo_alloc)
        builders = {
            "competicao_jogos": self.templates.competencia_jogos,
            "leilao_arte": self.templates.leilao_arte,
            "hackathon": self.templates.hackathon,
        }
        builder = builders.get(template_name)
        if ! builder {
            lance ValueError("Template desconhecido: {template_name}")
        chain = builder(**kwargs)
        self.register_chain(chain)
        return chain
    // -- validacao e execucao ----------------------------------------------
    func validate(self, chain: OperationChain) {texto: qualquer} {
        return self.validator.validate(chain)
    funcao execute(self, chain: OperationChain,
                payload := nil) -> {texto: qualquer}: // Optional[{texto: qualquer}]
        // Valida e executa a cadeia.
        if chain.status == ChainStatus.DRAFT {
            val = self.validate(chain)
            if !  val["valid"] {
                return {"error": "cadeia_invalida", "violations": val["violations"]}
        if chain.status in (ChainStatus.COMPLETED, ChainStatus.RUNNING) {
            chain.reset()
        result = chain.run(payload)
        self._last_result = result
        return result
    funcao last_impact(self) retorna Optional[{texto: qualquer}]:
        // Retorna o impacto da ultima operacao executada.
        if ! self._last_result {
            return nil
        return self.impact_tracker.measure(self._last_result)
    // -- cross-module -------------------------------------------------------
    func cross_module_report(self) {texto: qualquer} {
        // Relatorio de integracao com outros modulos da Republica.
        return {
            "open_transition": {
                "modo_atual": self.mode.value,
                "explicacao": (
                    "MONEY_ONLY: so dinheiro (pre-transicao). "
                    "HYBRID: dinheiro + credito coexistem. "
                    "CREDIT_ONLY: so credito (Republica completa)."
                ),
            },
            "open_labor_relay": {
                "uso": "Fornece benchmarks de qualidade para as competicoes.",
                "metodo": "Competition.set_benchmark(benchmark_id)",
            },
            "open_credit": {
                "uso": "Recebe credito liberado aos vencedores.",
                "campo": "final_payload.credito_liberado",
            },
            "open_history": {
                "uso": "Verifica ONGs (fact-check) && registra operacoes.",
                "metodo": "NGOAllocation.qualify(ngo_id) depende de OpenHistory",
            },
        }
    func stats(self) {texto: qualquer} {
        return {
            "modo": self.mode.value,
            "cadeias_registradas": len(self.chains),
            "ongs_registradas": len(self.ngo_alloc.registry),
            "ongs_qualificadas": soma(
                1 para n em self.ngo_alloc.registry.values()
                if self.ngo_alloc.qualify(n.ngo_id)
            ),
            "premios_distribuidos": len(self.reward_engine.distributions),
            "impactos_medidos": len(self.impact_tracker.records),
            "holding_ong": arredonde(self.ngo_alloc.holding, 2),
        }
// ============================================================================
// 12. MAIN -- demonstracao executavel
// ============================================================================
func _demo() None {
    // Demonstracao do OpenOperations em acao.
    fmt.Println("=" * 80)
    fmt.Println("  OPENOPERATIONS -- OPERACOES DA REPUBLICA EM CADEIAS MODULARES (LEGO)")
    fmt.Println("  Competicao -> Premiacao -> ONG -> Impacto -> Credito")
    fmt.Println("=" * 80)
    // --- setup ---
    ops = OpenOperations(mode=TransitionMode.HYBRID)
    // Registrar ONGs verificadas
    ong1 = NGO("ong-1", "Cozinha Comunitaria SP", cause="fome",
            verified = true, transparency_score=0.9)
    ong2 = NGO("ong-2", "Educacao para Todos", cause="educacao",
            verified = true, transparency_score=0.85)
    ong3 = NGO("ong-3", "Saude Rural", cause="saude",
            verified = false, transparency_score=0.5) // ! qualifica
    for _, ong := range (ong1, ong2, ong3) {
        r = ops.register_ngo(ong)
        fmt.Println("\n  ONG registrada: {ong.name:<30} "
            "qualificada={ops.ngo_alloc.qualify(ong.ngo_id)}")
    // --- 1. TEMPLATE: COMPETICAO DE JOGOS EDUCATIVOS ---
    fmt.Println("\n\n  === 1. TEMPLATE: COMPETICAO DE JOGOS EDUCATIVOS ===\n")
    chain = ops.from_template(
        "competicao_jogos",
        title = "Jogos Educativos 2026",
        total_pool = 10000.0,
    )
    fmt.Println("  Cadeia criada: {chain.name}")
    fmt.Println("  Pecas ({len(chain.pieces)}):")
    for _, p := range chain.pieces {
        fmt.Println("    [{p.piece_type.value:<12}] {p.name}")
        fmt.Println("      entrada={p.connector_in.name}  "
            "saida={p.connector_out.name}")
    // Validar
    val = ops.validate(chain)
    fmt.Println("\n  Validacao P1-P4: {val}")
    // Executar
    fmt.Println("\n  Executando cadeia...")
    resultado = ops.execute(chain, payload={
        "participantes": ["ana", "bruno", "carla", "daniel"],
        "winners": ["ana", "bruno", "carla"],
        "chain": chain.name,
    })
    fmt.Println("\n  RESULTADO:")
    fmt.Println("    Status: {resultado.get('status')}")
    fmt.Println("    Modo:   {resultado.get('mode')}")
    for _, r := range resultado.get("results", []) {
        flag = r["ok"] ? "OK" : "FALHOU"
        fmt.Println("    [{flag}] {r['piece']} ({r['type']})")
    // Impacto
    impacto = ops.last_impact()
    fmt.Println("\n  IMPACTO MEDIDO:")
    para cada (k, v) em (impacto or {}).items(): {
        fmt.Println("    {k}: {v}")
    // Detalhes da premiacao
    dist = resultado.get("final_payload", {}).get("reward_distribution", {})
    fmt.Println("\n  DISTRIBUICAO DE PREMIOS:")
    fmt.Println("    Pool total:      R$ {dist.get('total_pool', 0):.2f}")
    fmt.Println("    Para ONG:        R$ {dist.get('ngo_amount', 0):.2f}")
    fmt.Println("    Para vencedores: R$ {dist.get('winner_pool', 0):.2f}")
    for _, w := range dist.get("per_winner", []) {
        fmt.Println("      {w['winner']:<10} total=R${w['total']:.2f}  "
            "credito=R${w['credit']:.2f}  dinheiro=R${w['money']:.2f}")
    // Detalhes da ONG
    ngo_out = resultado.get("final_payload", {}).get("ngo_allocation", {})
    fmt.Println("\n  DOACAO PARA ONG:")
    for _, k := range ("ngo_name", "cause", "amount", "estimated_people_helped") {
        fmt.Println("    {k}: {ngo_out.get(k)}")
    // --- 2. TEMPLATE: HACKATHON ---
    fmt.Println("\n\n  === 2. TEMPLATE: HACKATHON OPENREPUBLIC ===\n")
    chain_hk = ops.from_template(
        "hackathon",
        title = "Hackathon OpenRepublic 2026",
        total_pool = 20000.0,
    )
    resultado_hk = ops.execute(chain_hk, payload={
        "participantes": ["equipe-alpha", "equipe-beta", "equipe-gamma"],
        "winners": ["equipe-alpha", "equipe-beta"],
        "chain": chain_hk.name,
    })
    fmt.Println("  Status: {resultado_hk.get('status')}")
    fmt.Println("  Pecas executadas: {resultado_hk.get('pieces_run')}")
    credito_hk = resultado_hk.get("final_payload", {}).get("credito_liberado", 0)
    fmt.Println("  Credito liberado (OpenCredit): R$ {credito_hk:.2f}")
    // --- 3. CROSS-MODULE ---
    fmt.Println("\n\n  === 3. INTEGRACAO CROSS-MODULE ===\n")
    cross = ops.cross_module_report()
    para cada (modulo, info) em cross.items(): {
        fmt.Println("  {modulo}:")
        para cada (k, v) em info.items(): {
            fmt.Println("    {k}: {v}")
    // --- 4. STATS ---
    fmt.Println("\n\n  === 4. ESTATISTICAS ===\n")
    para cada (k, v) em ops.stats().items(): {
        fmt.Println("  {k}: {v}")
    // --- 5. EXEMPLO MANUAL (montagem LEGO passo a passo) ---
    fmt.Println("\n\n  === 5. MONTAGEM MANUAL (LEGO passo a passo) ===\n")
    manual = OperationChain("manual", "Operacao Manual", mode=TransitionMode.HYBRID)
    p1 = OperationPiece(
        piece_id = "m-trigger", name="Gatilho",
        piece_type = PieceType.TRIGGER,
        connector_in = LegoConnector("init", "entrada", "fluxo"),
        connector_out = LegoConnector("vencedores_definidos", "saida", "fluxo"),
        executor = (d) -> {**d, "winners": ["x", "y"]},
    )
    p2 = ops.reward_engine.to_piece(total_pool=1000.0, mode=TransitionMode.HYBRID)
    p3 = ops.ngo_alloc.to_piece(cause="fome")
    p4 = ops.impact_tracker.to_piece()
    for _, piece := range (p1, p2, p3, p4) {
        r = manual.add_piece(piece)
        fmt.Println("  add '{piece.name}': {r}")
    val_manual = ops.validate(manual)
    fmt.Println("\n  Validacao manual: valid={val_manual['valid']} "
        "violacoes={val_manual['total_violations']}")
    res_manual = ops.execute(manual, payload={"chain": manual.name})
    fmt.Println("  Execucao manual: status={res_manual.get('status')}")
    // --- FILOSOFIA ---
    fmt.Println("\n\n{'='*80}")
    fmt.Println("  FILOSOFIA DO OPENOPERATIONS")
    fmt.Println("{'='*80}")
    fmt.Println("""
OPERACOES SAO CADEIAS DE PECAS (LEGO):
    Cada peca faz UMA coisa. Cada peca tem encaixe de entrada && saida.
    As pecas se conectam formando uma SEQUENCIA.
    O payload flui da primeira ate a ultima peca.
    competicao -> premiacao -> doacao ONG -> impacto -> credito
O MODELO DURANTE A TRANSICAO:
    Pessoas sao PREMIADAS por CONTRIBUIR (jogos educativos, codigo, arte).
    Parte do premio vai para ONG VERIFICADA (OpenHistory fact-check)
    que ajuda PESSOAS REAIS no mundo atual.
    Dinheiro + Credito COEXISTEM ate a transicao terminar.
POR QUE ISSO IMPORTA:
    - Premia contribuicao REAL (! especulacao).
    - Conecta a Republica ao mundo atual (via ONGs).
    - && MODULAR: trocar uma peca ! quebra a cadeia.
    - && TRANSPARENTE: cada passo && registrado.
    - && VALIDADO: P1-P4 garantem etica.
PRINCIPIOS:
    P1: Equidade -- operacao ! beneficia ricos em detrimento de pobres.
    P2: Seguranca -- ninguem perde acesso durante a operacao.
    P3: Reconhecimento -- quem contribui && reconhecido.
    P4: Consentimento -- o povo decide o ritmo; sem imposicao.
// )
    final_stats = ops.stats()
    fmt.Println("{'='*80}")
    fmt.Println("  OpenOperations concluido.")
    fmt.Println("  Cadeias registradas: {final_stats['cadeias_registradas']}")
    fmt.Println("  ONGs qualificadas: {final_stats['ongs_qualificadas']}"
        "/{final_stats['ongs_registradas']}")
    fmt.Println("  Premios distribuidos: {final_stats['premios_distribuidos']}")
    fmt.Println("  Impactos medidos: {final_stats['impactos_medidos']}")
    fmt.Println("  Holding ONG (sem qualificada): R$ {final_stats['holding_ong']}")
    fmt.Println("{'='*80}")
if __name__ == "__main__" {
    _demo()
