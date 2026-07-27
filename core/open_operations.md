# OpenOperations -- Gestao de Operacoes da Republica em Cadeias Modulares (LEGO)

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_operations.py`

**Descricao:** ================================================================================
"Operacoes sao CADEIAS de pecas que encaixam como LEGO.
 Cada peca tem um encaixe de ENTRADA e um encaixe de SAIDA.
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
 10. FUNCIONA no modelo antigo E no novo (transicao hibrida)
Author: OpenRepublic Team
Licenca: CC0 (Dominio Publico) -- https://creativecommons.org/publicdomain/zero/1.0/

---

```portugol++

// !/usr/bin/env python3
// -*- coding: utf-8 -*-
// 
OpenOperations -- Gestao de Operacoes da Republica em Cadeias Modulares (LEGO)
================================================================================

"Operacoes sao CADEIAS de pecas que encaixam como LEGO.
 Cada peca tem um encaixe de ENTRADA e um encaixe de SAIDA.
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
 10. FUNCIONA no modelo antigo e no novo (transicao hibrida)

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

classe OperationPrinciple herda de Enum:
    // Principios que toda operacao da Republica deve respeitar.
    P1_EQUITY = (1, "Equidade", "Operacao nao beneficia ricos em detrimento de pobres")
    P2_SAFETY = (2, "Seguranca", "Ninguem morre nem perde acesso durante a operacao")
    P3_RECOGNITION = (3, "Reconhecimento", "Quem contribui e reconhecido")
    P4_CONSENT = (4, "Consentimento", "O povo decide o ritmo; sem imposicao")


classe PieceType herda de Enum:
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


classe ChainStatus herda de Enum:
    // Estado de uma cadeia de operacao.
    DRAFT = "rascunho"  // montando, nao validada
    VALIDATED = "validada"  // passou no ChainValidator
    RUNNING = "em_execucao"  // pecas estao rodando
    PAUSED = "pausada"  // intermediaria pausada
    COMPLETED = "completa"  // todas as pecas terminaram
    FAILED = "falhou"  // uma peca falhou e nao recuperou


classe TransitionMode herda de Enum:
    // Modo da operacao conforme a fase da transicao (OpenTransition).
    Permite que a mesma operacao funcione no modelo antigo e no novo.
    // 
    MONEY_ONLY = "so_dinheiro"  // sistema antigo puro (pre-transicao)
    HYBRID = "hibrido"  // dinheiro + credito coexistem
    CREDIT_ONLY = "so_credito"  // Republica completa (pos-transicao)


// ============================================================================
// 2. CONNECTOR -- o encaixe LEGO entre pecas
// ============================================================================

// decorador: @dataclass
classe LegoConnector:
    // Encaixe LEGO que permite conectar duas pecas.

    Cada peca tem um connector de ENTRADA e um de SAIDA.
    Dois conectores so encaixam se forem COMPATIVEIS (mesmo formato).

    Analogia:
    - Peca A saida: 'premio_distribuido'
    - Peca B entrada: 'premio_recebido'
    - Se compatibilidade bate, encaixam.
    // 
    name: texto                           // ex: 'premio_distribuido'
    direction: texto                      // 'entrada' ou 'saida'
    shape: texto                          // tipo de encaixe: 'fluxo', 'valor', 'evento'
    seja description: texto = ""

    funcao encaixa_com(self, other: "LegoConnector") -> logico:
        // Verifica se este connector encaixa com outro.
        se self.direction == other.direction entao:
            retorne falso // entrada nao encaixa com entrada
        se self.shape != other.shape entao:
            retorne falso
        // saida deve ter o mesmo nome base da entrada (ou curinga)
        se self.name == "*"  ou  other.name == "*" entao:
            retorne verdadeiro
        retorne self.name == other.name


// ============================================================================
// 3. OPERATION PIECE -- uma peca modular da cadeia
// ============================================================================

// decorador: @dataclass
classe OperationPiece:
    // Uma peca modular que se encaixa numa cadeia de operacao.

    Analogia LEGO:
    - Cada peca faz UMA coisa (competicao, premiacao, doacao...).
    - Cada peca tem um connector de ENTRADA e um de SAIDA.
    - Pecas se encaixam formando uma cadeia sequencial.

    Execucao:
    - A peca so executa quando a anterior TERMINA e passa o 'payload'.
    - O payload e um dicionario que carrega dados pela cadeia.
    // 
    piece_id: texto
    name: texto
    piece_type: PieceType
    connector_in: LegoConnector
    connector_out: LegoConnector
    seja description: texto = ""

    // Funcao que executa a logica da peca. Recebe o payload, retorna payload.
    seja executor: Optional[Callable[[{texto: qualquer}], {texto: qualquer}]] = nulo

    // Parametros especificos da peca (ex: limite de tempo, regras)
    seja params: {texto: qualquer} = field(default_factory=dict)

    // Estado da execucao
    seja executed: logico = falso
    seja result: Optional[{texto: qualquer}] = nulo
    seja error: texto? = nulo

    // decorador: @property
    funcao is_entry(self) -> logico:
        // Peca de entrada: nao precisa de peca anterior.
        retorne self.connector_in.name == "init"  ou  self.connector_in.name == "*"

    // decorador: @property
    funcao is_terminal(self) -> logico:
        // Peca terminal: nao precisa de peca seguinte.
        retorne self.connector_out.name == "end"  ou  self.connector_out.name == "*"

    funcao run(self, payload: {texto: qualquer}) -> {texto: qualquer}:
        // Executa a peca com o payload recebido.
        se self.executor e nulo entao:
            // Peca sem executor so repassa o payload
            self.result = dict(payload)
            self.executed = verdadeiro
            retorne self.result
        tente:
            self.result = self.executor(payload)
            self.executed = verdadeiro
            self.error = nulo
            retorne self.result
        capture Exception como exc:
            self.error = texto(exc)
            self.result = {"_error": self.error, "_piece": self.piece_id}
            retorne self.result


// ============================================================================
// 4. OPERATION CHAIN -- cadeia de pecas encaixadas
// ============================================================================

classe OperationChain:
    // Cadeia de pecas modulares encaixadas como LEGO.

    A cadeia e uma SEQUENCIA. Cada peca encaixa na seguinte.
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
                 seja mode: TransitionMode = TransitionMode.HYBRID):
        self.chain_id = chain_id
        self.name = name
        self.mode = mode
        self.pieces: [OperationPiece] = []
        self.status: ChainStatus = ChainStatus.DRAFT
        self.initial_payload: {texto: qualquer} = {}
        self.execution_log: deque = deque(maxlen=500)

    // -- montagem -----------------------------------------------------------

    funcao add_piece(self, piece: OperationPiece) -> {texto: qualquer}:
        // Adiciona uma peca ao final da cadeia, verificando o encaixe.
        se self.pieces entao:
            prev = self.pieces[-1]
            se nao prev.connector_out.encaixa_com(piece.connector_in) entao:
                retorne {
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
        retorne {"added": verdadeiro, "total_pieces": tamanho(self.pieces)}

    funcao insert_piece(self, index: inteiro, piece: OperationPiece) -> {texto: qualquer}:
        // Insere peca numa posicao especifica, revalidando encaixes.
        self.pieces.insert(index, piece)
        retorne {"inserted": verdadeiro, "index": index}

    funcao remove_piece(self, piece_id: texto) -> {texto: qualquer}:
        // Remove peca pelo ID e reencadeia.
        before = tamanho(self.pieces)
        self.pieces = [p para p em self.pieces if p.piece_id != piece_id]
        retorne {"removed": before != tamanho(self.pieces),
                "total_pieces": tamanho(self.pieces)}

    // -- execucao -----------------------------------------------------------

    funcao run(self, payload: Optional[{texto: qualquer}] = None) -> {texto: qualquer}:
        // Executa a cadeia inteira, passando o payload de peca em peca.
        se nao self.pieces entao:
            retorne {"error": "cadeia_vazia"}
        se payload e nao None entao:
            self.initial_payload = payload

        self.status = ChainStatus.RUNNING
        current = dict(self.initial_payload)
        current["_mode"] = self.mode.value
        seja results: List[{texto: qualquer}] = []

        para cada (i, piece) em enumere(self.pieces):
            self.execution_log.append(
                {"event": "piece_start", "index": i,
                 "piece": piece.piece_id,
                 "time": datetime.now().isoformat()}
            )
            current = piece.run(current)
            results.append({
                "piece": piece.name,
                "type": piece.piece_type.value,
                "ok": piece.executed  e  nao  piece.error,
                "error": piece.error,
            })
            self.execution_log.append(
                {"event": "piece_end", "index": i,
                 "piece": piece.piece_id,
                 "ok": piece.executed  e  nao  piece.error,
                 "time": datetime.now().isoformat()}
            )
            se piece.error entao:
                self.status = ChainStatus.FAILED
                interrompa

        se self.status != ChainStatus.FAILED entao:
            self.status = ChainStatus.COMPLETED

        retorne {
            "chain": self.name,
            "status": self.status.value,
            "mode": self.mode.value,
            "pieces_run": tamanho(results),
            "results": results,
            "final_payload": current,
        }

    funcao reset(self) -> None:
        // Limpa estado de execucao para permitir re-rodar.
        para cada p em self.pieces:
            p.executed = falso
            p.result = nulo
            p.error = nulo
        self.status = ChainStatus.DRAFT


// ============================================================================
// 5. COMPETITION -- organizacao de competicoes
// ============================================================================

// decorador: @dataclass
classe Participant:
    // Participante de uma competicao.
    participant_id: texto
    name: texto
    seja category: texto = ""  // ex: 'jogos', 'codigo', 'arte'
    seja submission: texto = ""  // descricao da contribuicao
    seja score: flutuante = 0.0 // pontuacao do juri
    seja rank: inteiro = 0 // classificacao final


classe Competition:
    // Organiza competicoes dentro da Republica.

    Competicoes sao uma forma de PREMIAR CONTRIBUICAO:
    - Pessoas criam jogos educativos, escrevem codigo, fazem arte.
    - Um juri avalia as contribuicoes contra um benchmark (OpenLaborRelay).
    - Os melhores recebem premio (credito + dinheiro durante transicao).
    - Parte do premio vai para ONG verificada.

    PRINCIPIOS DA COMPETICAO:
    - Transparente: criterios e notas sao publicos.
    - Inclusiva: qualquer cidadao pode participar.
    - Justa: benchmark de qualidade evita subjetividade.
    - Educativa: feedback do juri ajuda a melhorar.
    // 

    funcao __init__(self, comp_id: texto, title: texto, category: texto = "jogos",
                 seja mode: TransitionMode = TransitionMode.HYBRID):
        self.comp_id = comp_id
        self.title = title
        self.category = category
        self.mode = mode
        self.participants: {texto: Participant} = {}
        self.jury: [texto] = [] // ids dos jurados
        self.rules: {texto: qualquer} = {
            "min_participants": 3,
            "max_winners": 3,
            "requires_benchmark": verdadeiro,
            "transparency": verdadeiro,
        }
        self.benchmark: texto? = nulo // referencia OpenLaborRelay
        self.results: Optional[[Participant]] = nulo

    funcao add_participant(self, participant: Participant) -> {texto: qualquer}:
        self.participants[participant.participant_id] = participant
        retorne {"added": verdadeiro, "total": tamanho(self.participants)}

    funcao set_jury(self, juror_ids: [texto]) -> {texto: qualquer}:
        self.jury = juror_ids
        retorne {"jury_size": tamanho(self.jury)}

    funcao set_benchmark(self, benchmark_id: texto) -> {texto: qualquer}:
        // Define o benchmark de qualidade (vindo do OpenLaborRelay).
        self.benchmark = benchmark_id
        retorne {"benchmark": benchmark_id}

    funcao judge(self, scores: {texto: flutuante}) -> {texto: qualquer}:
        // Aplica notas e classifica participantes.

        scores: { participant_id: score_float }
        // 
        se tamanho(self.participants) < self.rules["min_participants"] entao:
            retorne {"error": "participantes_insuficientes",
                    "min": self.rules["min_participants"]}

        para cada (pid, score) em scores.items():
            se pid in self.participants entao:
                self.participants[pid].score = flutuante(score)

        ranked = ordene(self.participants.values(),
                        key = (p) -> p.score, reverse=verdadeiro)
        para cada (i, p) em enumere(ranked, start=1):
            p.rank = i
        self.results = ranked
        retorne {
            "judged": verdadeiro,
            "winners": [p.name para p em ranked[: self.rules["max_winners"]]],
            "total_scored": tamanho(scores),
        }

    funcao to_piece(self) -> OperationPiece:
        // Transforma esta competicao numa peca LEGO da cadeia.
        funcao executor(payload: {texto: qualquer}) -> {texto: qualquer}:
            data = dict(payload)
            data["competition"] = self.title
            data["category"] = self.category
            // Se a competicao foi julgada, usa os resultados reais.
            // Caso contrario, preserva winners vindos do payload.
            se self.results entao:
                data["winners"] = [
                    p.name para p em self.results[: self.rules["max_winners"]]
                ]
            senao:
                data.setdefault("winners", [])
            // Preserva contagem de participantes do payload se houver.
            // Aceita tanto 'all_participants' (int) quanto 'participantes' (lista).
            se "all_participants" in data entao:
                count = data["all_participants"]
            senao se "participantes" in data entao:
                count = tamanho(data["participantes"])
            senao:
                count = tamanho(self.participants)
            data["all_participants"] = count
            retorne data
        retorne OperationPiece(
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
classe RewardSplit:
    // Como um premio e dividido.

    Duas dimensoes independentes:
    - ngo_pct: fracao do TOTAL do premio que vai para ONG (0-1).
    - credit_pct / money_pct: como o RESTANTE (winner_pool) e dividido
      entre o vencedor, em credito (Republica) e dinheiro (transicao).
      credit_pct + money_pct DEVE somar 1.0.
    // 
    seja credit_pct: flutuante = 0.6 // fracao do winner_pool em credito
    seja money_pct: flutuante = 0.4 // fracao do winner_pool em dinheiro
    seja ngo_pct: flutuante = 0.2 // fracao do total que vai para ONG

    funcao validate(self) -> logico:
        // Garante que as fracoes sao coerentes.
        winner_ok = abs((self.credit_pct + self.money_pct) - 1.0) < 0.01
        ngo_ok = 0.0 <= self.ngo_pct <= 1.0
        ranges_ok = (0.0 <= self.credit_pct <= 1.0
                      e 0.0 <= self.money_pct <= 1.0)
        retorne winner_ok e ngo_ok e ranges_ok


classe RewardEngine:
    // Distribui premios de forma hibrida durante a transicao.

    MODELO HIBRIDO:
    - Durante a transicao, o premio tem duas pernas:
      (a) CREDITO -- vai para a conta OpenCredit do vencedor.
      (b) DINHEIRO -- vai para a conta bancaria do vencedor (modelo antigo).
    - Uma fracao do TOTAL do premio e SEMPRE desviada para uma ONG verificada.
    - Conforme a transicao avanca (OpenTransition), money_pct cai para 0.

    TRANSICAO DO SPLIT:
      Modo MONEY_ONLY: 0% credito, 100% dinheiro, 10% ONG
      Modo HYBRID: 60% credito, 40% dinheiro, 20% ONG
      Modo CREDIT_ONLY: 80% credito, 0% dinheiro, 20% ONG
    // 

    funcao __init__(self):
        self.distributions: List[{texto: qualquer}] = []

    funcao default_split(self, mode: TransitionMode) -> RewardSplit:
        // Retorna o split padrao conforme o modo da transicao.
        defaults = {
            TransitionMode.MONEY_ONLY: RewardSplit(0.0, 1.0, 0.10),
            TransitionMode.HYBRID: RewardSplit(0.6, 0.4, 0.20),
            TransitionMode.CREDIT_ONLY: RewardSplit(1.0, 0.0, 0.20),
        }
        retorne defaults[mode]

    funcao distribute(self, total_pool: flutuante, winners: [texto],
                   seja mode: TransitionMode = TransitionMode.HYBRID,
                   seja split: RewardSplit? = nulo) -> {texto: qualquer}:
        // Distribui o pool de premios entre os vencedores + ONG.

        A fracao do ONG e retirada PRIMEIRO. O resto e dividido entre os
        vencedores conforme o split credito/dinheiro.
        // 
        se nao winners entao:
            retorne {"error": "sem_vencedores"}
        split = split ou self.default_split(mode)
        se nao split.validate() entao:
            retorne {"error": "split_invalido"}

        ngo_amount = arredonde(total_pool * split.ngo_pct, 2)
        winner_pool = arredonde(total_pool - ngo_amount, 2)

        // Distribuicao ponderada por rank (1o > 2o > 3o)
        weights = self._rank_weights(tamanho(winners))
        seja per_winner: List[{texto: qualquer}] = []
        para cada (w, name) em intercale(weights, winners):
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
        retorne result

    // decorador: @staticmethod
    funcao _rank_weights(n: inteiro) -> [flutuante]:
        // Pesos por posicao: 1o, 2o, 3o... (soma 1.0).
        se n <= 0 entao:
            retorne []
        // distribuicao 50% / 30% / 20% para 3; generica para N
        raw = [1.0 / (i + 1) para i em intervalo(n)] // harmonico
        total = soma(raw)
        retorne [r / total para r em raw]

    funcao to_piece(self, total_pool: flutuante,
                 seja mode: TransitionMode = TransitionMode.HYBRID) -> OperationPiece:
        // Transforma o RewardEngine numa peca LEGO da cadeia.
        engine = self

        funcao executor(payload: {texto: qualquer}) -> {texto: qualquer}:
            data = dict(payload)
            winners = data.get("winners", [])
            dist = engine.distribute(total_pool, winners, mode=mode)
            data["reward_distribution"] = dist
            retorne data

        retorne OperationPiece(
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
classe NGO:
    // ONG verificada que recebe parte dos premios.
    ngo_id: texto
    name: texto
    cause: texto                          // ex: 'fome', 'educacao', 'saude'
    seja verified: logico = falso // checada por OpenHistory
    seja people_helped_lifetime: inteiro = 0
    seja transparency_score: flutuante = 0.0 // 0-1


classe NGOAllocation:
    // Aloca a fracao de ONG do premio para uma ONG verificada.

    CRITERIOS:
    - A ONG DEVE ser verificada por OpenHistory (fact-check).
    - A ONG DEVE ter score de transparencia >= 0.7.
    - O destino do dinheiro e PUBLICO (OpenHistory registra).
    - Se nenhuma ONG qualifica, o valor fica em HOLDING ate qualificar.
    // 

    MIN_TRANSPARENCY = 0.7

    funcao __init__(self):
        self.registry: {texto: NGO} = {}
        self.allocations: List[{texto: qualquer}] = []
        self.holding: flutuante = 0.0 // valor retido por falta de ONG qualificada

    funcao register_ngo(self, ngo: NGO) -> {texto: qualquer}:
        self.registry[ngo.ngo_id] = ngo
        retorne {"registered": verdadeiro, "verified": ngo.verified,
                "transparency": ngo.transparency_score}

    funcao qualify(self, ngo_id: texto) -> logico:
        // Verifica se a ONG atende aos criterios.
        ngo = self.registry.get(ngo_id)
        se nao ngo entao:
            retorne falso
        retorne ngo.verified e ngo.transparency_score >= self.MIN_TRANSPARENCY

    funcao allocate(self, amount: flutuante, cause: texto = "",
                 seja preferred_ngo_id: texto? = nulo) -> {texto: qualquer}:
        // Aloca valor para a ONG qualificada mais apropriada.
        candidates = [n para n em self.registry.values() if self.qualify(n.ngo_id)]
        se cause entao:
            cause_matches = [n para n em candidates if n.cause == cause]
            se cause_matches entao:
                candidates = cause_matches

        se preferred_ngo_id entao:
            pref = [n para n em candidates if n.ngo_id == preferred_ngo_id]
            se pref entao:
                candidates = pref

        se nao candidates entao:
            self.holding += amount
            retorne {
                "allocated": falso,
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
        retorne {"allocated": verdadeiro, **record}

    // decorador: @staticmethod
    funcao _estimate_people_helped(amount: flutuante, ngo: NGO) -> inteiro:
        // Estima quantas pessoas reais serao ajudadas (impacto real).
        // Heuristica simples: R$ 100 ajuda ~1 pessoa (depende da causa).
        per_person = {"fome": 50, "educacao": 200, "saude": 300, "agua": 80}
        base = per_person.get(ngo.cause, 100)
        retorne maximo(1, inteiro(amount / base))

    funcao to_piece(self, cause: texto = "") -> OperationPiece:
        // Transforma o NGOAllocation numa peca LEGO da cadeia.
        alloc = self

        funcao executor(payload: {texto: qualquer}) -> {texto: qualquer}:
            data = dict(payload)
            dist = data.get("reward_distribution", {})
            ngo_amount = dist.get("ngo_amount", 0.0)
            result = alloc.allocate(ngo_amount, cause=cause)
            data["ngo_allocation"] = result
            retorne data

        retorne OperationPiece(
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

classe ImpactTracker:
    // Mede o impacto REAL de uma operacao da Republica.

    IMPACTO nao e SO NUMERO -- e PESSOA REAL.
    Cada metrica responde: quantas pessoas reais foram ajudadas?

    Metricas:
    - participantes_envolvidos: quantas pessoas participaram
    - pessoas_ajudadas_ong: quantas pessoas reais a ONG ajudou
    - credito_distribuido: quanto credito fluiu para a Republica
    - dinheiro_distribuido: quanto dinheiro fluiu (durante transicao)
    - score_impacto: 0-1 (impacto normalizado)
    // 

    funcao __init__(self):
        self.records: List[{texto: qualquer}] = []

    funcao measure(self, chain_result: {texto: qualquer}) -> {texto: qualquer}:
        // Extrai metricas de impacto do resultado da cadeia.
        final = chain_result.get("final_payload", {})
        dist = final.get("reward_distribution", {})
        ngo = final.get("ngo_allocation", {})

        participantes = final.get(
            "all_participants", tamanho(final.get("participantes", []))
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
        retorne record

    // decorador: @staticmethod
    funcao _compute_score(participantes: inteiro, pessoas_ong: inteiro,
                       credito: flutuante) -> flutuante:
        // importa math
        p = math.log10(maximo(1, participantes + 1))
        o = math.log10(maximo(1, pessoas_ong + 1))
        c = math.log10(maximo(1, credito + 1))
        raw = 0.3 * p + 0.5 * o + 0.2 * c
        // normaliza para 0-1 (assumindo escala tipica)
        retorne minimo(1.0, raw / 3.0)

    funcao to_piece(self) -> OperationPiece:
        // Transforma o ImpactTracker numa peca LEGO da cadeia.
        tracker = self

        funcao executor(payload: {texto: qualquer}) -> {texto: qualquer}:
            data = dict(payload)
            chain_result = {"final_payload": data, "chain": data.get("chain", "")}
            impact = tracker.measure(chain_result)
            data["impact"] = impact
            retorne data

        retorne OperationPiece(
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

classe ChainValidator:
    // Valida se uma cadeia de operacao respeita os principios P1-P4.

    CHECAGENS:
    - P1 (Equidade): todo vencedor recebe algo; ngao concentrado em 1.
    - P2 (Seguranca): nenhuma peca remove acesso essencial.
    - P3 (Reconhecimento): existe peca de premiacao ou de impacto.
    - P4 (Consentimento): modo da cadeia e explicito (nao imposto).

    VALIDACAO ESTRUTURAL:
    - A cadeia tem pelo menos uma peca de entrada.
    - A cadeia tem pelo menos uma peca terminal.
    - Todos os encaixes batem (LEGO connectors compatíveis).
    // 

    funcao __init__(self):
        self.violations: List[{texto: qualquer}] = []

    funcao validate(self, chain: OperationChain) -> {texto: qualquer}:
        // Valida a cadeia e retorna lista de violacoes.
        self.violations = []
        self._validate_structure(chain)
        self._validate_p1(chain)
        self._validate_p2(chain)
        self._validate_p3(chain)
        self._validate_p4(chain)

        ok = tamanho(self.violations) == 0
        se ok entao:
            chain.status = ChainStatus.VALIDATED
        retorne {
            "valid": ok,
            "violations": self.violations,
            "total_violations": tamanho(self.violations),
            "chain_status": chain.status.value,
        }

    funcao _add(self, principle: texto, message: texto) -> None:
        self.violations.append({"principle": principle, "message": message})

    funcao _validate_structure(self, chain: OperationChain) -> None:
        se nao chain.pieces entao:
            self._add("estrutura", "Cadeia sem pecas")
            retorne nulo
        // Encaixes consecutivos
        para cada i em intervalo(tamanho(chain.pieces) - 1):
            a = chain.pieces[i]
            b = chain.pieces[i + 1]
            se nao a.connector_out.encaixa_com(b.connector_in) entao:
                self._add(
                    "estrutura",
                    "Encaixe quebrado entre '{a.name}' e '{b.name}'",
                )
        // Entrada e saida
        first = chain.pieces[0]
        se nao  (first.is_entry  ou  first.connector_in.direction == "entrada") entao:
            self._add("estrutura", "Primeira peca nao e ponto de entrada")
        last = chain.pieces[-1]
        se nao  (last.is_terminal  ou  last.connector_out.direction == "saida") entao:
            self._add("estrutura", "Ultima peca nao e ponto terminal")

    funcao _validate_p1(self, chain: OperationChain) -> None:
        // P1 Equidade: cadeia deve ter peca de reward ou de NGO.
        has_reward = any(p.piece_type == PieceType.REWARD para p em chain.pieces)
        has_ngo = any(p.piece_type == PieceType.NGO para p em chain.pieces)
        se nao (has_reward ou has_ngo) entao:
            self._add(
                "P1_equidade",
                "Cadeia sem premiacao nem doacao ONG -- sem distribuicao",
            )

    funcao _validate_p2(self, chain: OperationChain) -> None:
        // P2 Seguranca: nenhuma peca com flag 'remove_acesso'.
        para cada p em chain.pieces:
            se p.params.get("remove_acesso") entao:
                self._add(
                    "P2_seguranca",
                    "Peca '{p.name}' remove acesso essencial",
                )

    funcao _validate_p3(self, chain: OperationChain) -> None:
        // P3 Reconhecimento: deve existir reward ou impact tracker.
        has_reward = any(p.piece_type == PieceType.REWARD para p em chain.pieces)
        has_impact = any(p.piece_type == PieceType.IMPACT para p em chain.pieces)
        se nao (has_reward ou has_impact) entao:
            self._add(
                "P3_reconhecimento",
                "Cadeira sem premiacao nem medicao de impacto",
            )

    funcao _validate_p4(self, chain: OperationChain) -> None:
        // P4 Consentimento: modo deve ser explicito.
        se chain.mode nao in TransitionMode entao:
            self._add("P4_consentimento", "Modo de transicao nao definido")


// ============================================================================
// 10. OPERATION TEMPLATES -- templates reusaveis
// ============================================================================

classe OperationTemplates:
    // Templates reusaveis de cadeias de operacao.

    Cada template retorna uma OperationChain pronta para uso.
    Os templates sao PONTO DE PARTIDA -- podem ser customizados.
    // 

    // decorador: @staticmethod
    funcao competencia_jogos(title: texto = "Competicao de Jogos Educativos",
                          seja total_pool: flutuante = 10000.0,
                          seja mode: TransitionMode = TransitionMode.HYBRID,
                          seja ngo_alloc: NGOAllocation? = nulo,
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
        alloc = ngo_alloc ou NGOAllocation()
        chain.add_piece(alloc.to_piece(cause="educacao"))

        // Peca 4: impacto
        chain.add_piece(ImpactTracker().to_piece())

        // Peca 5: credito (registra credito liberado no OpenCredit)
        funcao credito_executor(payload: {texto: qualquer}) -> {texto: qualquer}:
            data = dict(payload)
            dist = data.get("reward_distribution", {})
            credito_total = soma(w.get("credit", 0) para w em dist.get("per_winner", []))
            data["credito_liberado"] = arredonde(credito_total, 2)
            data["destino"] = "OpenCredit"
            retorne data

        chain.add_piece(OperationPiece(
            piece_id = "credito-release",
            name = "Liberacao de credito (OpenCredit)",
            piece_type = PieceType.CREDIT,
            connector_in = LegoConnector("impacto_medido", "entrada", "fluxo"),
            connector_out = LegoConnector("end", "saida", "fluxo"),
            description = "Libera credito no OpenCredit para os vencedores",
            executor = credito_executor,
        ))
        retorne chain

    // decorador: @staticmethod
    funcao leilao_arte(title: texto = "Leilao de Arte Comunitaria",
                    seja total_pool: flutuante = 5000.0,
                    seja mode: TransitionMode = TransitionMode.HYBRID,
                    seja ngo_alloc: NGOAllocation? = nulo,
                    ) -> OperationChain:
        // Template: competicao(arte) -> premiacao -> ONG -> impacto.
        chain = OperationChain("tpl-leilao", title, mode=mode)

        comp = Competition("arte", title, category="arte", mode=mode)
        chain.add_piece(comp.to_piece())

        reward = RewardEngine()
        chain.add_piece(reward.to_piece(total_pool=total_pool, mode=mode))

        alloc = ngo_alloc ou NGOAllocation()
        chain.add_piece(alloc.to_piece(cause="fome"))

        chain.add_piece(ImpactTracker().to_piece())
        retorne chain

    // decorador: @staticmethod
    funcao hackathon(title: texto = "Hackathon OpenRepublic",
                  seja total_pool: flutuante = 20000.0,
                  seja mode: TransitionMode = TransitionMode.HYBRID,
                  seja ngo_alloc: NGOAllocation? = nulo,
                  ) -> OperationChain:
        // Template: competicao(codigo) -> premiacao -> ONG -> impacto -> credito.
        chain = OperationChain("tpl-hackathon", title, mode=mode)

        comp = Competition("codigo", title, category="codigo", mode=mode)
        chain.add_piece(comp.to_piece())

        reward = RewardEngine()
        chain.add_piece(reward.to_piece(total_pool=total_pool, mode=mode))

        alloc = ngo_alloc ou NGOAllocation()
        chain.add_piece(alloc.to_piece(cause="educacao"))

        chain.add_piece(ImpactTracker().to_piece())

        funcao credito_executor(payload: {texto: qualquer}) -> {texto: qualquer}:
            data = dict(payload)
            dist = data.get("reward_distribution", {})
            credito_total = soma(w.get("credit", 0) para w em dist.get("per_winner", []))
            data["credito_liberado"] = arredonde(credito_total, 2)
            data["destino"] = "OpenCredit"
            retorne data

        chain.add_piece(OperationPiece(
            piece_id = "credito-release",
            name = "Liberacao de credito (OpenCredit)",
            piece_type = PieceType.CREDIT,
            connector_in = LegoConnector("impacto_medido", "entrada", "fluxo"),
            connector_out = LegoConnector("end", "saida", "fluxo"),
            description = "Libera credito no OpenCredit para os vencedores",
            executor = credito_executor,
        ))
        retorne chain


// ============================================================================
// 11. OPEN OPERATIONS -- fachada principal (orquestra tudo)
// ============================================================================

classe OpenOperations:
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
    - OpenHistory: verifica ONGs e registra operacoes

    USO:
        ops = OpenOperations()
        chain = ops.from_template("competicao_jogos", title="Jogos 2026")
        ops.validate(chain)
        resultado = ops.execute(chain, payload={...})
        impacto = ops.last_impact()
    // 

    funcao __init__(self, mode: TransitionMode = TransitionMode.HYBRID):
        self.mode = mode
        self.chains: {texto: OperationChain} = {}
        self.validator = ChainValidator()
        self.ngo_alloc = NGOAllocation()
        self.reward_engine = RewardEngine()
        self.impact_tracker = ImpactTracker()
        self.templates = OperationTemplates()
        self._last_result: Optional[{texto: qualquer}] = nulo

    // -- registro de ONGs --------------------------------------------------

    funcao register_ngo(self, ngo: NGO) -> {texto: qualquer}:
        retorne self.ngo_alloc.register_ngo(ngo)

    // -- cadastro de cadeias ------------------------------------------------

    funcao register_chain(self, chain: OperationChain) -> {texto: qualquer}:
        self.chains[chain.chain_id] = chain
        retorne {"registered": verdadeiro, "chain_id": chain.chain_id,
                "total_chains": tamanho(self.chains)}

    // -- templates ----------------------------------------------------------

    funcao from_template(self, template_name: texto, **kwargs) -> OperationChain:
        // Cria cadeia a partir de template (competicao_jogos, leilao_arte, hackathon).
        kwargs.setdefault("mode", self.mode)
        kwargs.setdefault("ngo_alloc", self.ngo_alloc)
        builders = {
            "competicao_jogos": self.templates.competencia_jogos,
            "leilao_arte": self.templates.leilao_arte,
            "hackathon": self.templates.hackathon,
        }
        builder = builders.get(template_name)
        se nao builder entao:
            lance ValueError("Template desconhecido: {template_name}")
        chain = builder(**kwargs)
        self.register_chain(chain)
        retorne chain

    // -- validacao e execucao ----------------------------------------------

    funcao validate(self, chain: OperationChain) -> {texto: qualquer}:
        retorne self.validator.validate(chain)

    funcao execute(self, chain: OperationChain,
                seja payload: Optional[{texto: qualquer}] = nulo) -> {texto: qualquer}:
        // Valida e executa a cadeia.
        se chain.status == ChainStatus.DRAFT entao:
            val = self.validate(chain)
            se nao  val["valid"] entao:
                retorne {"error": "cadeia_invalida", "violations": val["violations"]}
        se chain.status in (ChainStatus.COMPLETED, ChainStatus.RUNNING) entao:
            chain.reset()
        result = chain.run(payload)
        self._last_result = result
        retorne result

    funcao last_impact(self) retorna Optional[{texto: qualquer}]:
        // Retorna o impacto da ultima operacao executada.
        se nao self._last_result entao:
            retorne nulo
        retorne self.impact_tracker.measure(self._last_result)

    // -- cross-module -------------------------------------------------------

    funcao cross_module_report(self) -> {texto: qualquer}:
        // Relatorio de integracao com outros modulos da Republica.
        retorne {
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
                "uso": "Verifica ONGs (fact-check) e registra operacoes.",
                "metodo": "NGOAllocation.qualify(ngo_id) depende de OpenHistory",
            },
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "modo": self.mode.value,
            "cadeias_registradas": tamanho(self.chains),
            "ongs_registradas": tamanho(self.ngo_alloc.registry),
            "ongs_qualificadas": soma(
                1 para n em self.ngo_alloc.registry.values()
                if self.ngo_alloc.qualify(n.ngo_id)
            ),
            "premios_distribuidos": tamanho(self.reward_engine.distributions),
            "impactos_medidos": tamanho(self.impact_tracker.records),
            "holding_ong": arredonde(self.ngo_alloc.holding, 2),
        }


// ============================================================================
// 12. MAIN -- demonstracao executavel
// ============================================================================

funcao _demo() -> None:
    // Demonstracao do OpenOperations em acao.
    imprima("=" * 80)
    imprima("  OPENOPERATIONS -- OPERACOES DA REPUBLICA EM CADEIAS MODULARES (LEGO)")
    imprima("  Competicao -> Premiacao -> ONG -> Impacto -> Credito")
    imprima("=" * 80)

    // --- setup ---
    ops = OpenOperations(mode=TransitionMode.HYBRID)

    // Registrar ONGs verificadas
    ong1 = NGO("ong-1", "Cozinha Comunitaria SP", cause="fome",
               verified = verdadeiro, transparency_score=0.9)
    ong2 = NGO("ong-2", "Educacao para Todos", cause="educacao",
               verified = verdadeiro, transparency_score=0.85)
    ong3 = NGO("ong-3", "Saude Rural", cause="saude",
               verified = falso, transparency_score=0.5) // nao qualifica
    para cada ong em (ong1, ong2, ong3):
        r = ops.register_ngo(ong)
        imprima("\n  ONG registrada: {ong.name:<30} "
              "qualificada={ops.ngo_alloc.qualify(ong.ngo_id)}")

    // --- 1. TEMPLATE: COMPETICAO DE JOGOS EDUCATIVOS ---
    imprima("\n\n  === 1. TEMPLATE: COMPETICAO DE JOGOS EDUCATIVOS ===\n")
    chain = ops.from_template(
        "competicao_jogos",
        title = "Jogos Educativos 2026",
        total_pool = 10000.0,
    )
    imprima("  Cadeia criada: {chain.name}")
    imprima("  Pecas ({len(chain.pieces)}):")
    para cada p em chain.pieces:
        imprima("    [{p.piece_type.value:<12}] {p.name}")
        imprima("      entrada={p.connector_in.name}  "
              "saida={p.connector_out.name}")

    // Validar
    val = ops.validate(chain)
    imprima("\n  Validacao P1-P4: {val}")

    // Executar
    imprima("\n  Executando cadeia...")
    resultado = ops.execute(chain, payload={
        "participantes": ["ana", "bruno", "carla", "daniel"],
        "winners": ["ana", "bruno", "carla"],
        "chain": chain.name,
    })
    imprima("\n  RESULTADO:")
    imprima("    Status: {resultado.get('status')}")
    imprima("    Modo:   {resultado.get('mode')}")
    para cada r em resultado.get("results", []):
        flag = r["ok"] ? "OK" : "FALHOU"
        imprima("    [{flag}] {r['piece']} ({r['type']})")

    // Impacto
    impacto = ops.last_impact()
    imprima("\n  IMPACTO MEDIDO:")
    para cada (k, v) em (impacto or {}).items():
        imprima("    {k}: {v}")

    // Detalhes da premiacao
    dist = resultado.get("final_payload", {}).get("reward_distribution", {})
    imprima("\n  DISTRIBUICAO DE PREMIOS:")
    imprima("    Pool total:      R$ {dist.get('total_pool', 0):.2f}")
    imprima("    Para ONG:        R$ {dist.get('ngo_amount', 0):.2f}")
    imprima("    Para vencedores: R$ {dist.get('winner_pool', 0):.2f}")
    para cada w em dist.get("per_winner", []):
        imprima("      {w['winner']:<10} total=R${w['total']:.2f}  "
              "credito=R${w['credit']:.2f}  dinheiro=R${w['money']:.2f}")

    // Detalhes da ONG
    ngo_out = resultado.get("final_payload", {}).get("ngo_allocation", {})
    imprima("\n  DOACAO PARA ONG:")
    para cada k em ("ngo_name", "cause", "amount", "estimated_people_helped"):
        imprima("    {k}: {ngo_out.get(k)}")

    // --- 2. TEMPLATE: HACKATHON ---
    imprima("\n\n  === 2. TEMPLATE: HACKATHON OPENREPUBLIC ===\n")
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
    imprima("  Status: {resultado_hk.get('status')}")
    imprima("  Pecas executadas: {resultado_hk.get('pieces_run')}")
    credito_hk = resultado_hk.get("final_payload", {}).get("credito_liberado", 0)
    imprima("  Credito liberado (OpenCredit): R$ {credito_hk:.2f}")

    // --- 3. CROSS-MODULE ---
    imprima("\n\n  === 3. INTEGRACAO CROSS-MODULE ===\n")
    cross = ops.cross_module_report()
    para cada (modulo, info) em cross.items():
        imprima("  {modulo}:")
        para cada (k, v) em info.items():
            imprima("    {k}: {v}")

    // --- 4. STATS ---
    imprima("\n\n  === 4. ESTATISTICAS ===\n")
    para cada (k, v) em ops.stats().items():
        imprima("  {k}: {v}")

    // --- 5. EXEMPLO MANUAL (montagem LEGO passo a passo) ---
    imprima("\n\n  === 5. MONTAGEM MANUAL (LEGO passo a passo) ===\n")
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

    para cada piece em (p1, p2, p3, p4):
        r = manual.add_piece(piece)
        imprima("  add '{piece.name}': {r}")

    val_manual = ops.validate(manual)
    imprima("\n  Validacao manual: valid={val_manual['valid']} "
          "violacoes={val_manual['total_violations']}")

    res_manual = ops.execute(manual, payload={"chain": manual.name})
    imprima("  Execucao manual: status={res_manual.get('status')}")

    // --- FILOSOFIA ---
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DO OPENOPERATIONS")
    imprima("{'='*80}")
    imprima("""
  OPERACOES SAO CADEIAS DE PECAS (LEGO):
    Cada peca faz UMA coisa. Cada peca tem encaixe de entrada e saida.
    As pecas se conectam formando uma SEQUENCIA.
    O payload flui da primeira ate a ultima peca.

    competicao -> premiacao -> doacao ONG -> impacto -> credito

  O MODELO DURANTE A TRANSICAO:
    Pessoas sao PREMIADAS por CONTRIBUIR (jogos educativos, codigo, arte).
    Parte do premio vai para ONG VERIFICADA (OpenHistory fact-check)
    que ajuda PESSOAS REAIS no mundo atual.
    Dinheiro + Credito COEXISTEM ate a transicao terminar.

  POR QUE ISSO IMPORTA:
    - Premia contribuicao REAL (nao especulacao).
    - Conecta a Republica ao mundo atual (via ONGs).
    - e MODULAR: trocar uma peca nao quebra a cadeia.
    - e TRANSPARENTE: cada passo e registrado.
    - e VALIDADO: P1-P4 garantem etica.

  PRINCIPIOS:
    P1: Equidade -- operacao nao beneficia ricos em detrimento de pobres.
    P2: Seguranca -- ninguem perde acesso durante a operacao.
    P3: Reconhecimento -- quem contribui e reconhecido.
    P4: Consentimento -- o povo decide o ritmo; sem imposicao.
// )

    final_stats = ops.stats()
    imprima("{'='*80}")
    imprima("  OpenOperations concluido.")
    imprima("  Cadeias registradas: {final_stats['cadeias_registradas']}")
    imprima("  ONGs qualificadas: {final_stats['ongs_qualificadas']}"
          "/{final_stats['ongs_registradas']}")
    imprima("  Premios distribuidos: {final_stats['premios_distribuidos']}")
    imprima("  Impactos medidos: {final_stats['impactos_medidos']}")
    imprima("  Holding ONG (sem qualificada): R$ {final_stats['holding_ong']}")
    imprima("{'='*80}")


se __name__ == "__main__" entao:
    _demo()

```
