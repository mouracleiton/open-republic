// OpenBusinessModel -- Modelo de Negocio Hibirido da Transicao -- gerado de Portugol++
package openbusinessmodel_modelo_de_negocio_hibirido_da_transicao

import "fmt"

// !/usr/bin/env python3
//
OpenBusinessModel -- Modelo de Negocio Hibirido da Transicao
==============================================================
"DURANTE A TRANSICAO, dinheiro && credito coexistem.
O OpenBusinessModel && o PONTE entre os dois mundos.
Pessoas sao PREMIADAS por contribuir.
Parte do premio vai para ONG que AJUDA pessoas reais.
Modelo hibrido: dinheiro (antigo) + credito (Republica).
DEPOIS DA TRANSICAO: dinheiro extinto. So credito.
Mas DURANTE: os dois funcionam juntos."
CONCEITO (durante Fase 3-4 da OpenTransition):
- Competicoes premiam contribuidores (jogos educativos, codigo, arte)
- Premio && HIBRIDO: parte em credito (Republica) + parte em dinheiro (antigo)
- Parte do dinheiro vai para ONG VERIFICADA que ajuda pessoas
- Tudo rastreado. Tudo transparente. Tudo modular.
MODELO LEGO (encadeamento de pecas):
Cada componente do business model && uma PECA.
Pecas encaixam em CADEIA:
    [COMPETICAO] -> [PREMIACAO] -> [ONG_ALOCACAO] -> [IMPACTO] -> [CREDITO]
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime
// ============================================================================
// 1. PECAS LEGO (modular chain)
// ============================================================================
type LegoType int
const (
    // Tipos de peca LEGO no encadeamento.
    COMPETITION = "competicao"
    REWARD = "premiacao"
    NGO_ALLOCATION = "ong_alocacao"
    IMPACT = "impacto"
    CREDIT = "credito"
    VERIFICATION = "verificacao"
    DISTRIBUTION = "distribuicao"
    FEEDBACK = "feedback"
type LegoConnector int
const (
    // Encaixes de cada peca LEGO (entrada e saida).
    // Entradas (o que a peca recebe)
    IN_PARTICIPANTS = "in_participantes"
    IN_FUNDS = "in_recursos"
    IN_REWARD = "in_premio"
    IN_IMPACT_DATA = "in_impacto"
    IN_VERIFIED = "in_verificado"
    // Saidas (o que a peca produz)
    OUT_WINNER = "out_vencedor"
    OUT_REWARD = "out_premio"
    OUT_DONATION = "out_doacao"
    OUT_IMPACT_REPORT = "out_relatorio_impacto"
    OUT_CREDIT = "out_credito"
    OUT_VERIFIED = "out_verificado"
// decorador: @dataclass
type LegoPiece struct {
    // Uma peca LEGO do encadeamento.
    Cada peca tem:
    - Tipo (o que faz)
    - Entrada (o que recebe da peca anterior)
    - Saida (o que passa para a proxima peca)
    - Configuracao (parametros especificos)
    //
    piece_id: texto
    piece_type: LegoType
    name: texto
    description := "" // string
    // Encaixes
    input_connector := nil // LegoConnector?
    output_connector := nil // LegoConnector?
    // Configuracao
    config := field(default_factory=dict) // {texto: qualquer}
    // Estado
    executed := false // bool
    result := field(default_factory=dict) // {texto: qualquer}
    func can_connect_to(self, other: "LegoPiece") bool {
        // Verifica se esta peca encaixa na proxima.
        if ! self.output_connector || ! other.input_connector {
            return false
        // Regras de encaixe
        compatible = {
            LegoConnector.OUT_WINNER: [LegoConnector.IN_PARTICIPANTS],
            LegoConnector.OUT_REWARD: [LegoConnector.IN_FUNDS, LegoConnector.IN_REWARD],
            LegoConnector.OUT_DONATION: [LegoConnector.IN_FUNDS],
            LegoConnector.OUT_IMPACT_REPORT: [LegoConnector.IN_IMPACT_DATA],
            LegoConnector.OUT_CREDIT: [LegoConnector.IN_FUNDS],
            LegoConnector.OUT_VERIFIED: [LegoConnector.IN_VERIFIED],
        }
        return other.input_connector in compatible.get(self.output_connector, [])
// decorador: @dataclass
type LegoChain struct {
    // Cadeia de pecas LEGO encaixadas.
    Uma cadeia completa:
    [COMPETICAO] -> [PREMIACAO] -> [ONG] -> [IMPACTO] -> [CREDITO]
    Cada peca se conecta a proxima por encaixes compativeis.
    A cadeia so executa se TODOS os encaixes forem validos.
    //
    chain_id: texto
    name: texto
    pieces := field(default_factory=list) // [LegoPiece]
    executed := false // bool
    total_impact := field(default_factory=dict) // {texto: qualquer}
    // decorador: @property
    func is_valid(self) bool {
        // Verifica se todos os encaixes sao compativeis.
        for _, i := range intervalo(len(self.pieces) - 1) {
            if ! self.pieces[i].can_connect_to(self.pieces[i + 1]) {
                return false
        return true
    // decorador: @property
    func piece_count(self) int64 {
        return len(self.pieces)
// ============================================================================
// 2. COMPONENTES DO BUSINESS MODEL
// ============================================================================
type CompetitionType int
const (
    GAMES_EDUCATIONAL = "jogos_educativos"
    CODE = "codigo"
    ART = "arte"
    MUSIC = "musica"
    HARDWARE = "hardware"
    SOLUTION = "solucao_problema"
    WRITING = "escrita"
    DESIGN = "design"
// decorador: @dataclass
type Competition struct {
    // Competicao que premia contribuidores.
    comp_id: texto
    title: texto
    comp_type: CompetitionType
    description := "" // string
    organizer := "" // string
    participants := field(default_factory=list) // [texto]
    winners := field(default_factory=list) // [texto]
    prize_pool_money := 0.0 // dinheiro (durante transicao) // float64
    prize_pool_credit := 0.0 // credito da Republica // float64
    ngo_share_pct := 0.3 // % que vai para ONG // float64
    ngo_verified := "" // string
    start_date := "" // string
    end_date := "" // string
// decorador: @dataclass
type NGOAllocation struct {
    // Alocacao para ONG verificada.
    ngo_id: texto
    ngo_name: texto
    verified := false // OpenHistory fact-check // bool
    verification_source := "" // string
    causes := field(default_factory=list) // [texto]
    amount_received := 0.0 // float64
    amount_used := 0.0 // float64
    people_helped := 0 // int64
    transparent := true // OpenSymbolRevision: ONG transparente // bool
// ============================================================================
// 3. MOTOR DE BUSINESS MODEL
// ============================================================================
type BusinessModelEngine struct {
    // Motor hibrido de negocio durante a transicao.
    COMO FUNCIONA (exemplo):
    1. Competicao de jogos educativos
    2. Vencedores recebem: 50% credito + 30% dinheiro + 20% ONG
    3. ONG verificada usa dinheiro para ajudar pessoas reais
    4. Impacto && medido && rastreado
    5. Credito cai na conta OpenCredit do vencedor
    6.chain LEGO completa: COMPETICAO -> PREMIACAO -> ONG -> IMPACTO -> CREDITO
    ALOCACAO PADRAO (definida por peca, votada pela assembleia):
    - 50% para vencedor (credito + dinheiro)
    - 30% para ONG verificada
    - 20% reinvestido na Republica (infraestrutura)
    //
    func __init__(self) {
        self.competitions: {texto: Competition} = {}
        self.ngos: {texto: NGOAllocation} = {}
        self.chains: {texto: LegoChain} = {}
        self._init_ngos()
    func _init_ngos(self) {
        // ONGs verificadas (OpenHistory fact-check).
        ngos_data = [
            ("ONG-001", "Centro de Reintegracao Social", true,
            "OpenHistory + OpenReintegration",
            ["moradores_de_rua", "ex_presidiarios", "adicao"]),
            ("ONG-002", "Saude Mental Real", true,
            "OpenPsychologyAudit + OpenDignity",
            ["saude_mental", "anti_rotulagem"]),
            ("ONG-003", "Educacao para Todos", true,
            "OpenEducation + OpenUniversity",
            ["educacao", "criancas", "alfabetizacao"]),
            ("ONG-004", "Horta Comunitaria Central", true,
            "OpenAgrarian + OpenSustainability",
            ["comida", "agricultura", "fome_zero"]),
            ("ONG-005", "Mulheres em Situacao de Risco", true,
            "OpenReintegration + OpenHealthcareAccess",
            ["mulheres", "violencia_domestica", "filhos"]),
            ("ONG-FAKE-01", "ONG Falsificada Ltda", false,
            "OpenHistory: BLOQUEADA (fraude comprovada)",
            ["apropriacao_indébita"]),
        ]
        para nid, name, verified, source, causes in ngos_data: {
            self.ngos[nid] = NGOAllocation(
                ngo_id = nid, ngo_name=name, verified=verified,
                verification_source = source, causes=causes,
            )
    funcao create_competition(self, title: texto, comp_type: CompetitionType,
                        prize_money := 0.0, // float64
                        prize_credit := 0.0, // float64
                        ngo_share := 0.3, // float64
                        ngo_id := "", // string
                        organizer := "", // string
                        description := "") -> {texto: qualquer}: // string
        // Cria competicao com business model hibrido.
        // Verificar ONG
        ngo = self.ngos.get(ngo_id)
        if ngo_id && (! ngo || ! ngo.verified) {
            return {
                "error": "ONG ! verificada || invalida",
                "ngo_id": ngo_id,
                "message": "A Republica so trabalha com ONG VERIFICADA.",
            }
        comp_id = hashlib.md5("{title}{datetime.now()}".encode()).hexdigest()[:8]
        comp = Competition(
            comp_id = comp_id, title=title, comp_type=comp_type,
            description = description, organizer=organizer,
            prize_pool_money = prize_money,
            prize_pool_credit = prize_credit,
            ngo_share_pct = ngo_share,
            ngo_verified = ngo_id,
        )
        self.competitions[comp_id] = comp
        // Criar cadeia LEGO
        chain = self._build_chain(comp, ngo)
        self.chains[chain.chain_id] = chain
        return {
            "created": true,
            "comp_id": comp_id,
            "title": title,
            "type": comp_type.value,
            "prize_money": "R$ {prize_money:,.0f}",
            "prize_credit": "{prize_credit:.0f} credito",
            "ngo_share": "{ngo_share*100:.0f}%",
            ngo ? "ngo": ngo.ngo_name : "N/A",
            "chain_id": chain.chain_id,
            "chain_valid": chain.is_valid,
            "chain_pieces": chain.piece_count,
            "message": (
                "Competicao '{title}' criada. "
                "Premio: R$ {prize_money:,.0f} + {prize_credit:.0f} credito. "
                "ONG: {ngo.ngo_name if ngo else 'N/A'} ({ngo_share*100:.0f}%). "
                "Cadeia LEGO: {chain.piece_count} pecas."
            ),
        }
    funcao _build_chain(self, comp: Competition,
                    ngo: NGOAllocation?) -> LegoChain:
        // Constroi cadeia LEGO para esta competicao.
        chain_id = hashlib.md5("chain{comp.comp_id}".encode()).hexdigest()[:8]
        pieces = [
            LegoPiece(
                piece_id = "{comp.comp_id}-P1",
                piece_type = LegoType.COMPETITION,
                name = "Competicao: {comp.title}",
                config = {"type": comp.comp_type.value,
                        "prize_money": comp.prize_pool_money,
                        "prize_credit": comp.prize_pool_credit},
                output_connector = LegoConnector.OUT_WINNER,
            ),
            LegoPiece(
                piece_id = "{comp.comp_id}-P2",
                piece_type = LegoType.REWARD,
                name = "Premiacao Hibrida",
                config = {"winner_share": 0.5, "ngo_share": comp.ngo_share_pct,
                        "reinvest": 0.2},
                input_connector = LegoConnector.IN_PARTICIPANTS,
                output_connector = LegoConnector.OUT_REWARD,
            ),
            LegoPiece(
                piece_id = "{comp.comp_id}-P3",
                piece_type = LegoType.NGO_ALLOCATION,
                name = "ONG: {ngo.ngo_name if ngo else 'N/A'}",
                config = ngo ? {"ngo_id" : ngo.ngo_id : "",
                        ngo ? "verified": ngo.verified : false,
                        "amount": comp.prize_pool_money * comp.ngo_share_pct},
                input_connector = LegoConnector.IN_FUNDS,
                output_connector = LegoConnector.OUT_DONATION,
            ),
            LegoPiece(
                piece_id = "{comp.comp_id}-P4",
                piece_type = LegoType.IMPACT,
                name = "Medicao de Impacto",
                config = {"track": ["people_helped", "credit_distributed",
                                "infrastructure_built"]},
                input_connector = LegoConnector.IN_IMPACT_DATA,
                output_connector = LegoConnector.OUT_IMPACT_REPORT,
            ),
            LegoPiece(
                piece_id = "{comp.comp_id}-P5",
                piece_type = LegoType.CREDIT,
                name = "Credito Distribuido",
                config = {"credit_amount": comp.prize_pool_credit * 0.5},
                input_connector = LegoConnector.IN_FUNDS,
                output_connector = LegoConnector.OUT_CREDIT,
            ),
        ]
        return LegoChain(chain_id=chain_id, name="Chain: {comp.title}",
                        pieces = pieces)
    funcao execute_chain(self, chain_id: texto,
                    winners := nil) -> {texto: qualquer}: // [texto]
        // Executa cadeia LEGO completa.
        chain = self.chains.get(chain_id)
        if ! chain {
            return {"error": "Cadeia ! encontrada"}
        if ! chain.is_valid {
            return {"error": "Cadeia invalida -- encaixes incompativeis"}
        // Executar cada peca em sequencia
        results = []
        for _, piece := range chain.pieces {
            piece.executed = true
            if piece.piece_type == LegoType.COMPETITION {
                piece.result = {"winners": winners  ||  ["Vencedor Padrao"]}
            } else if piece.piece_type == LegoType.REWARD {
                money = piece.config.get("prize_money", 0)
                credit = piece.config.get("prize_credit", 0)
                winner_share = piece.config.get("winner_share", 0.5)
                ngo_share = piece.config.get("ngo_share", 0.3)
                reinvest = piece.config.get("reinvest", 0.2)
                piece.result = {
                    "winner_money": money * winner_share,
                    "winner_credit": credit * winner_share,
                    "ngo_money": money * ngo_share,
                    "reinvest_money": money * reinvest,
                }
            } else if piece.piece_type == LegoType.NGO_ALLOCATION {
                ngo_id = piece.config.get("ngo_id", "")
                ngo = self.ngos.get(ngo_id)
                if ngo && ngo.verified {
                    amount = piece.config.get("amount", 0)
                    ngo.amount_received += amount
                    ngo.people_helped += inteiro(amount / 50) // estimativa
                    piece.result = {"donated": amount,
                                    "ngo": ngo.ngo_name,
                                    "people_helped": ngo.people_helped}
                } else {
                    piece.result = {"error": "ONG invalida"}
            } else if piece.piece_type == LegoType.IMPACT {
                piece.result = {"impact_measured": true}
            } else if piece.piece_type == LegoType.CREDIT {
                piece.result = {"credit_distributed":
                                piece.config.get("credit_amount", 0)}
            results.append({
                "piece": piece.name,
                "type": piece.piece_type.value,
                "executed": piece.executed,
                "result": piece.result,
            })
        chain.executed = true
        chain.total_impact = {
            "winners": winners  ||  [],
            "pieces_executed": len(results),
        }
        return {
            "chain_id": chain_id,
            "name": chain.name,
            "pieces": chain.piece_count,
            "executed": true,
            "results": results,
            "message": (
                "Cadeia '{chain.name}' executada. "
                "{chain.piece_count} pecas LEGO completas."
            ),
        }
    func verify_ngo(self, ngo_id: texto) {texto: qualquer} {
        // Verifica ONG (OpenHistory fact-check).
        ngo = self.ngos.get(ngo_id)
        if ! ngo {
            return {"error": "ONG ! encontrada"}
        return {
            "ngo": ngo.ngo_name,
            "verified": ngo.verified,
            "source": ngo.verification_source,
            "causes": ngo.causes,
            "transparent": ngo.transparent,
            "message": (
                "{'VERIFICADA -- pode receber doacoes' if ngo.verified else 'NAO VERIFICADA -- BLOQUEADA'}"
            ),
        }
    func list_ngos(self) [Dict] {
        return [
            {"id": n.ngo_id, "name": n.ngo_name, "verified": n.verified,
            "causes": n.causes, "received": n.amount_received,
            "helped": n.people_helped}
            para n em self.ngos.values() {
        ]
    func stats(self) {texto: qualquer} {
        return {
            "total_competitions": len(self.competitions),
            "total_chains": len(self.chains),
            "total_ngos": len(self.ngos),
            "verified_ngos": soma(1 para n em self.ngos.values() if n.verified),
            "total_donated": soma(n.amount_received para n em self.ngos.values()),
            "people_helped": soma(n.people_helped para n em self.ngos.values()),
            "model": "HIBRIDO (dinheiro + credito durante transicao)",
        }
// ============================================================================
// 4. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = BusinessModelEngine()
    fmt.Println("=" * 80)
    fmt.Println("  OPENBUSINESSMODEL -- MODELO HIBRIDO DA TRANSICAO")
    fmt.Println("  Competicao -> Premiacao -> ONG -> Impacto -> Credito (LEGO chain)")
    fmt.Println("=" * 80)
    // === 1. ONGs VERIFICADAS ===
    fmt.Println("\n\n  === 1. ONGs VERIFICADAS ===\n")
    for _, ngo := range engine.list_ngos() {
        status = ngo["verified"] ? "OK" : "BLOQ"
        fmt.Println("  [{status}] {ngo['name']:<35} causas: {', '.join(ngo['causes'][:2])}")
    // === 2. COMPETICOES COM BUSINESS MODEL ===
    fmt.Println("\n\n  === 2. COMPETICOES (business model hibrido) ===\n")
    comps = [
        ("Hackathon Jogos Educativos", CompetitionType.GAMES_EDUCATIONAL,
        50000, 500, 0.3, "ONG-001"),
        ("Desafio de Codigo Rust", CompetitionType.CODE,
        30000, 300, 0.25, "ONG-003"),
        ("Festival de Musica Republica", CompetitionType.MUSIC,
        20000, 200, 0.4, "ONG-004"),
        ("Torneio OpenMartialArts", CompetitionType.SOLUTION,
        10000, 150, 0.3, "ONG-005"),
        ("Competicao ONG Fake", CompetitionType.ART,
        5000, 50, 0.5, "ONG-FAKE-01"),   // Deve falhar
    ]
    para title, ctype, money, credit, ngo_share, ngo_id in comps: {
        r = engine.create_competition(title, ctype, money, credit,
                                    ngo_share, ngo_id)
        if r.get("created") {
            fmt.Println("\n  {r['title']}")
            fmt.Println("    Premio: {r['prize_money']} + {r['prize_credit']}")
            fmt.Println("    ONG: {r['ngo']} ({r['ngo_share']})")
            fmt.Println("    Chain LEGO: {r['chain_pieces']} pecas (valida: {r['chain_valid']})")
        } else {
            fmt.Println("\n  {title}: {r.get('error', 'ERRO')}")
            fmt.Println("    {r.get('message', '')}")
    // === 3. EXECUTAR CADEIA LEGO ===
    fmt.Println("\n\n  === 3. EXECUTANDO CADEIA LEGO ===\n")
    para cada (chain_id, chain) em engine.chains.items(): {
        winners = ["Equipe Alpha", "Joao Solo"]
        result = engine.execute_chain(chain_id, winners)
        if result.get("executed") {
            fmt.Println("\n  {result['name']}")
            fmt.Println("  {result['message']}")
            for _, p := range result["results"][:3] {
                fmt.Println("    [{p['type']}] {p['piece']}")
                if p["result"] {
                    para cada (k, v) em list(p["result"].items())[:2]: {
                        fmt.Println("      {k}: {v}")
    // === 4. DISTRIBUICAO DO PREMIO ===
    fmt.Println("\n\n  === 4. DISTRIBUICAO DO PREMIO (modelo hibrido) ===\n")
    fmt.Println("  Para cada R$ 1.000 de premio:")
    fmt.Println("    R$ 500 (50%) -> Vencedor (dinheiro durante transicao)")
    fmt.Println("    R$ 300 (30%) -> ONG verificada (ajuda pessoas reais)")
    fmt.Println("    R$ 200 (20%) -> Reinvestido na Republica (infraestrutura)")
    fmt.Println("    + Credito da Republica para Vencedor")
    fmt.Println("\n  DURANTE A TRANSICAO: dinheiro + credito coexistem")
    fmt.Println("  DEPOIS DA TRANSICAO: so credito. Dinheiro extinto.")
    // === 5. ONG IMPACTO ===
    fmt.Println("\n\n  === 5. IMPACTO DAS ONGs ===\n")
    for _, ngo := range engine.list_ngos() {
        if ngo["verified"]  &&  ngo["received"] > 0 {
            fmt.Println("  {ngo['name']:<35} recebeu R$ {ngo['received']:,.0f} "
                "-> {ngo['helped']} pessoas ajudadas")
    // === 6. STATS ===
    fmt.Println("\n\n  === 6. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items(): {
        fmt.Println("  {k:<35} {v}")
    // === FILOSOFIA ===
    fmt.Println("\n\n{'='*80}")
    fmt.Println("  FILOSOFIA DO OPENBUSINESSMODEL")
    fmt.Println("{'='*80}")
    fmt.Println("""
DURANTE A TRANSICAO (OpenTransition Fase 3-4):
    Dinheiro && credito COEXISTEM.
    Competicoes premiam em HIBRIDO:
    - Parte em dinheiro (antigo) para vencedor
    - Parte em credito (Republica) para vencedor
    - Parte em dinheiro para ONG verificada
    - Parte reinvestida na Republica
MODELO LEGO (encadeamento de pecas):
    Cada operacao && uma CADEIA de pecas encaixadas:
    [COMPETICAO] -> [PREMIACAO] -> [ONG] -> [IMPACTO] -> [CREDITO]
        | | | | |
        v v v v v
    participantes 50% vencedor 30% ONG mede ajuda credito cai
                    20% reinv. verificada rastreada na conta
    Pecas encaixam por CONECTORES compativeis.
    Cadeia so executa se TODOS os encaixes forem validos.
    Pecas podem ser TROCADAS (modular LEGO).
ONG VERIFICADA (OpenHistory fact-check):
    A Republica SO trabalha com ONG VERIFICADA.
    ONG fake -> BLOQUEADA (ex: "ONG Falsificada Ltda").
    ONG real -> verificada por OpenHistory + OpenReintegration.
    Transparencia total: quanto recebeu, quanto usou, quem ajudou.
EXEMPLO REAL:
    Hackathon de Jogos Educativos
    -> Premio: R$ 50.000 + 500 credito
    -> R$ 25.000 para vencedor (dinheiro)
    -> 250 credito para vencedor (Republica)
    -> R$ 15.000 para Centro de Reintegracao Social (ONG verificada)
    -> R$ 10.000 reinvestido em FabLab (infraestrutura)
    -> 300 pessoas ajudadas pela ONG
    -> Vencedor ganha credito + reconhecimento
DEPOIS DA TRANSICAO:
    Dinheiro EXTINTO. So credito.
    Competicoes dao CREDITO de impacto.
    ONGs continuam, mas financidas por credito, ! dinheiro.
    A cadeia LEGO continua a mesma. So a moeda muda.
ARQUITETURA MODULAR LEGO:
    Tudo na Republica agora encaixa como LEGO.
    OpenBusinessModel encaixa em OpenTransition.
    OpenTransition encaixa em OpenModularArchitecture.
    OpenOperations encaixa em OpenBusinessModel.
    Cada peca tem entrada && saida. Tudo conecta.
PRINCIPIOS:
    P1: Premio para todos. Sem elitismo na distribuicao.
    P2: ONG so se verificada. Protege pessoas de fraude.
    P3 := base 1.0. // Vencedor e ONG ganham. Trabalho
    P4: Alocacao votada pela assembleia (50/30/20 ajustavel).
// )
    fmt.Println("{'='*80}")
    fmt.Println("  OpenBusinessModel: {s['total_competitions']} competicoes, "
        "{s['total_donated']:,.0f} doado, "
        "{s['people_helped']} pessoas ajudadas.")
    fmt.Println("  Modelo LEGO: pecas encaixam em cadeia.")
    fmt.Println("{'='*80}")
