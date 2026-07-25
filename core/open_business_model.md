# OpenBusinessModel -- Modelo de Negocio Hibirido da Transicao

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_business_model.py`

**Descricao:** ==============================================================
"DURANTE A TRANSICAO, dinheiro e credito coexistem.
 O OpenBusinessModel e o PONTE entre os dois mundos.
 Pessoas sao PREMIADAS por contribuir.
 Parte do premio vai para ONG que AJUDA pessoas reais.
 Modelo hibrido: dinheiro (antigo) + credito (Republica).
 DEPOIS DA TRANSICAO: dinheiro extinto. So credito.
 Mas DURANTE: os dois funcionam juntos."
CONCEITO (durante Fase 3-4 da OpenTransition):
  - Competicoes premiam contribuidores (jogos educativos, codigo, arte)
  - Premio e HIBRIDO: parte em credito (Republica) + parte em dinheiro (antigo)
  - Parte do dinheiro vai para ONG VERIFICADA que ajuda pessoas
  - Tudo rastreado. Tudo transparente. Tudo modular.
MODELO LEGO (encadeamento de pecas):
  Cada componente do business model e uma PECA.
  Pecas encaixam em CADEIA:
    [COMPETICAO] -> [PREMIACAO] -> [ONG_ALOCACAO] -> [IMPACTO] -> [CREDITO]
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenBusinessModel -- Modelo de Negocio Hibirido da Transicao
==============================================================

"DURANTE A TRANSICAO, dinheiro e credito coexistem.
 O OpenBusinessModel e o PONTE entre os dois mundos.

 Pessoas sao PREMIADAS por contribuir.
 Parte do premio vai para ONG que AJUDA pessoas reais.
 Modelo hibrido: dinheiro (antigo) + credito (Republica).

 DEPOIS DA TRANSICAO: dinheiro extinto. So credito.
 Mas DURANTE: os dois funcionam juntos."

CONCEITO (durante Fase 3-4 da OpenTransition):
  - Competicoes premiam contribuidores (jogos educativos, codigo, arte)
  - Premio e HIBRIDO: parte em credito (Republica) + parte em dinheiro (antigo)
  - Parte do dinheiro vai para ONG VERIFICADA que ajuda pessoas
  - Tudo rastreado. Tudo transparente. Tudo modular.

MODELO LEGO (encadeamento de pecas):
  Cada componente do business model e uma PECA.
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

classe LegoType herda de Enum:
    // Tipos de peca LEGO no encadeamento.
    COMPETITION = "competicao"
    REWARD = "premiacao"
    NGO_ALLOCATION = "ong_alocacao"
    IMPACT = "impacto"
    CREDIT = "credito"
    VERIFICATION = "verificacao"
    DISTRIBUTION = "distribuicao"
    FEEDBACK = "feedback"


classe LegoConnector herda de Enum:
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
classe LegoPiece:
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
    seja description: texto = ""

    // Encaixes
    seja input_connector: LegoConnector? = nulo
    seja output_connector: LegoConnector? = nulo

    // Configuracao
    seja config: {texto: qualquer} = field(default_factory=dict)

    // Estado
    seja executed: logico = falso
    seja result: {texto: qualquer} = field(default_factory=dict)

    funcao can_connect_to(self, other: "LegoPiece") -> logico:
        // Verifica se esta peca encaixa na proxima.
        se nao self.output_connector ou nao other.input_connector entao:
            retorne falso
        // Regras de encaixe
        compatible = {
            LegoConnector.OUT_WINNER: [LegoConnector.IN_PARTICIPANTS],
            LegoConnector.OUT_REWARD: [LegoConnector.IN_FUNDS, LegoConnector.IN_REWARD],
            LegoConnector.OUT_DONATION: [LegoConnector.IN_FUNDS],
            LegoConnector.OUT_IMPACT_REPORT: [LegoConnector.IN_IMPACT_DATA],
            LegoConnector.OUT_CREDIT: [LegoConnector.IN_FUNDS],
            LegoConnector.OUT_VERIFIED: [LegoConnector.IN_VERIFIED],
        }
        retorne other.input_connector in compatible.get(self.output_connector, [])


// decorador: @dataclass
classe LegoChain:
    // Cadeia de pecas LEGO encaixadas.

    Uma cadeia completa:
    [COMPETICAO] -> [PREMIACAO] -> [ONG] -> [IMPACTO] -> [CREDITO]

    Cada peca se conecta a proxima por encaixes compativeis.
    A cadeia so executa se TODOS os encaixes forem validos.
    // 
    chain_id: texto
    name: texto
    seja pieces: [LegoPiece] = field(default_factory=list)
    seja executed: logico = falso
    seja total_impact: {texto: qualquer} = field(default_factory=dict)

    // decorador: @property
    funcao is_valid(self) -> logico:
        // Verifica se todos os encaixes sao compativeis.
        para cada i em intervalo(tamanho(self.pieces) - 1):
            se nao self.pieces[i].can_connect_to(self.pieces[i + 1]) entao:
                retorne falso
        retorne verdadeiro

    // decorador: @property
    funcao piece_count(self) -> inteiro:
        retorne tamanho(self.pieces)


// ============================================================================
// 2. COMPONENTES DO BUSINESS MODEL
// ============================================================================

classe CompetitionType herda de Enum:
    GAMES_EDUCATIONAL = "jogos_educativos"
    CODE = "codigo"
    ART = "arte"
    MUSIC = "musica"
    HARDWARE = "hardware"
    SOLUTION = "solucao_problema"
    WRITING = "escrita"
    DESIGN = "design"


// decorador: @dataclass
classe Competition:
    // Competicao que premia contribuidores.
    comp_id: texto
    title: texto
    comp_type: CompetitionType
    seja description: texto = ""
    seja organizer: texto = ""
    seja participants: [texto] = field(default_factory=list)
    seja winners: [texto] = field(default_factory=list)
    seja prize_pool_money: flutuante = 0.0 // dinheiro (durante transicao)
    seja prize_pool_credit: flutuante = 0.0 // credito da Republica
    seja ngo_share_pct: flutuante = 0.3 // % que vai para ONG
    seja ngo_verified: texto = ""
    seja start_date: texto = ""
    seja end_date: texto = ""


// decorador: @dataclass
classe NGOAllocation:
    // Alocacao para ONG verificada.
    ngo_id: texto
    ngo_name: texto
    seja verified: logico = falso // OpenHistory fact-check
    seja verification_source: texto = ""
    seja causes: [texto] = field(default_factory=list)
    seja amount_received: flutuante = 0.0
    seja amount_used: flutuante = 0.0
    seja people_helped: inteiro = 0
    seja transparent: logico = verdadeiro // OpenSymbolRevision: ONG transparente


// ============================================================================
// 3. MOTOR DE BUSINESS MODEL
// ============================================================================

classe BusinessModelEngine:
    // Motor hibrido de negocio durante a transicao.

    COMO FUNCIONA (exemplo):
    1. Competicao de jogos educativos
    2. Vencedores recebem: 50% credito + 30% dinheiro + 20% ONG
    3. ONG verificada usa dinheiro para ajudar pessoas reais
    4. Impacto e medido e rastreado
    5. Credito cai na conta OpenCredit do vencedor
    6.chain LEGO completa: COMPETICAO -> PREMIACAO -> ONG -> IMPACTO -> CREDITO

    ALOCACAO PADRAO (definida por peca, votada pela assembleia):
    - 50% para vencedor (credito + dinheiro)
    - 30% para ONG verificada
    - 20% reinvestido na Republica (infraestrutura)
    // 

    funcao __init__(self):
        self.competitions: {texto: Competition} = {}
        self.ngos: {texto: NGOAllocation} = {}
        self.chains: {texto: LegoChain} = {}
        self._init_ngos()

    funcao _init_ngos(self):
        // ONGs verificadas (OpenHistory fact-check).
        ngos_data = [
            ("ONG-001", "Centro de Reintegracao Social", verdadeiro,
             "OpenHistory + OpenReintegration",
             ["moradores_de_rua", "ex_presidiarios", "adicao"]),
            ("ONG-002", "Saude Mental Real", verdadeiro,
             "OpenPsychologyAudit + OpenDignity",
             ["saude_mental", "anti_rotulagem"]),
            ("ONG-003", "Educacao para Todos", verdadeiro,
             "OpenEducation + OpenUniversity",
             ["educacao", "criancas", "alfabetizacao"]),
            ("ONG-004", "Horta Comunitaria Central", verdadeiro,
             "OpenAgrarian + OpenSustainability",
             ["comida", "agricultura", "fome_zero"]),
            ("ONG-005", "Mulheres em Situacao de Risco", verdadeiro,
             "OpenReintegration + OpenHealthcareAccess",
             ["mulheres", "violencia_domestica", "filhos"]),
            ("ONG-FAKE-01", "ONG Falsificada Ltda", falso,
             "OpenHistory: BLOQUEADA (fraude comprovada)",
             ["apropriacao_indébita"]),
        ]
        para nid, name, verified, source, causes in ngos_data:
            self.ngos[nid] = NGOAllocation(
                ngo_id = nid, ngo_name=name, verified=verified,
                verification_source = source, causes=causes,
            )

    funcao create_competition(self, title: texto, comp_type: CompetitionType,
                           seja prize_money: flutuante = 0.0,
                           seja prize_credit: flutuante = 0.0,
                           seja ngo_share: flutuante = 0.3,
                           seja ngo_id: texto = "",
                           seja organizer: texto = "",
                           seja description: texto = "") -> {texto: qualquer}:
        // Cria competicao com business model hibrido.
        // Verificar ONG
        ngo = self.ngos.get(ngo_id)
        se ngo_id e (nao ngo ou nao ngo.verified) entao:
            retorne {
                "error": "ONG nao verificada ou invalida",
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

        retorne {
            "created": verdadeiro,
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
                        ngo ? "verified": ngo.verified : falso,
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

        retorne LegoChain(chain_id=chain_id, name="Chain: {comp.title}",
                         pieces = pieces)

    funcao execute_chain(self, chain_id: texto,
                      seja winners: [texto] = nulo) -> {texto: qualquer}:
        // Executa cadeia LEGO completa.
        chain = self.chains.get(chain_id)
        se nao chain entao:
            retorne {"error": "Cadeia nao encontrada"}

        se nao chain.is_valid entao:
            retorne {"error": "Cadeia invalida -- encaixes incompativeis"}

        // Executar cada peca em sequencia
        results = []
        para cada piece em chain.pieces:
            piece.executed = verdadeiro
            se piece.piece_type == LegoType.COMPETITION entao:
                piece.result = {"winners": winners  ou  ["Vencedor Padrao"]}
            senao se piece.piece_type == LegoType.REWARD entao:
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
            senao se piece.piece_type == LegoType.NGO_ALLOCATION entao:
                ngo_id = piece.config.get("ngo_id", "")
                ngo = self.ngos.get(ngo_id)
                se ngo e ngo.verified entao:
                    amount = piece.config.get("amount", 0)
                    ngo.amount_received += amount
                    ngo.people_helped += inteiro(amount / 50) // estimativa
                    piece.result = {"donated": amount,
                                    "ngo": ngo.ngo_name,
                                    "people_helped": ngo.people_helped}
                senao:
                    piece.result = {"error": "ONG invalida"}
            senao se piece.piece_type == LegoType.IMPACT entao:
                piece.result = {"impact_measured": verdadeiro}
            senao se piece.piece_type == LegoType.CREDIT entao:
                piece.result = {"credit_distributed":
                                piece.config.get("credit_amount", 0)}

            results.append({
                "piece": piece.name,
                "type": piece.piece_type.value,
                "executed": piece.executed,
                "result": piece.result,
            })

        chain.executed = verdadeiro
        chain.total_impact = {
            "winners": winners  ou  [],
            "pieces_executed": tamanho(results),
        }

        retorne {
            "chain_id": chain_id,
            "name": chain.name,
            "pieces": chain.piece_count,
            "executed": verdadeiro,
            "results": results,
            "message": (
                "Cadeia '{chain.name}' executada. "
                "{chain.piece_count} pecas LEGO completas."
            ),
        }

    funcao verify_ngo(self, ngo_id: texto) -> {texto: qualquer}:
        // Verifica ONG (OpenHistory fact-check).
        ngo = self.ngos.get(ngo_id)
        se nao ngo entao:
            retorne {"error": "ONG nao encontrada"}
        retorne {
            "ngo": ngo.ngo_name,
            "verified": ngo.verified,
            "source": ngo.verification_source,
            "causes": ngo.causes,
            "transparent": ngo.transparent,
            "message": (
                "{'VERIFICADA -- pode receber doacoes' if ngo.verified else 'NAO VERIFICADA -- BLOQUEADA'}"
            ),
        }

    funcao list_ngos(self) -> [Dict]:
        retorne [
            {"id": n.ngo_id, "name": n.ngo_name, "verified": n.verified,
             "causes": n.causes, "received": n.amount_received,
             "helped": n.people_helped}
            para n em self.ngos.values()
        ]

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_competitions": tamanho(self.competitions),
            "total_chains": tamanho(self.chains),
            "total_ngos": tamanho(self.ngos),
            "verified_ngos": soma(1 para n em self.ngos.values() if n.verified),
            "total_donated": soma(n.amount_received para n em self.ngos.values()),
            "people_helped": soma(n.people_helped para n em self.ngos.values()),
            "model": "HIBRIDO (dinheiro + credito durante transicao)",
        }


// ============================================================================
// 4. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = BusinessModelEngine()

    imprima("=" * 80)
    imprima("  OPENBUSINESSMODEL -- MODELO HIBRIDO DA TRANSICAO")
    imprima("  Competicao -> Premiacao -> ONG -> Impacto -> Credito (LEGO chain)")
    imprima("=" * 80)

    // === 1. ONGs VERIFICADAS ===
    imprima("\n\n  === 1. ONGs VERIFICADAS ===\n")
    para cada ngo em engine.list_ngos():
        status = ngo["verified"] ? "OK" : "BLOQ"
        imprima("  [{status}] {ngo['name']:<35} causas: {', '.join(ngo['causes'][:2])}")

    // === 2. COMPETICOES COM BUSINESS MODEL ===
    imprima("\n\n  === 2. COMPETICOES (business model hibrido) ===\n")
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
    para title, ctype, money, credit, ngo_share, ngo_id in comps:
        r = engine.create_competition(title, ctype, money, credit,
                                       ngo_share, ngo_id)
        se r.get("created") entao:
            imprima("\n  {r['title']}")
            imprima("    Premio: {r['prize_money']} + {r['prize_credit']}")
            imprima("    ONG: {r['ngo']} ({r['ngo_share']})")
            imprima("    Chain LEGO: {r['chain_pieces']} pecas (valida: {r['chain_valid']})")
        senao:
            imprima("\n  {title}: {r.get('error', 'ERRO')}")
            imprima("    {r.get('message', '')}")

    // === 3. EXECUTAR CADEIA LEGO ===
    imprima("\n\n  === 3. EXECUTANDO CADEIA LEGO ===\n")
    para cada (chain_id, chain) em engine.chains.items():
        winners = ["Equipe Alpha", "Joao Solo"]
        result = engine.execute_chain(chain_id, winners)
        se result.get("executed") entao:
            imprima("\n  {result['name']}")
            imprima("  {result['message']}")
            para cada p em result["results"][:3]:
                imprima("    [{p['type']}] {p['piece']}")
                se p["result"] entao:
                    para cada (k, v) em list(p["result"].items())[:2]:
                        imprima("      {k}: {v}")

    // === 4. DISTRIBUICAO DO PREMIO ===
    imprima("\n\n  === 4. DISTRIBUICAO DO PREMIO (modelo hibrido) ===\n")
    imprima("  Para cada R$ 1.000 de premio:")
    imprima("    R$ 500 (50%) -> Vencedor (dinheiro durante transicao)")
    imprima("    R$ 300 (30%) -> ONG verificada (ajuda pessoas reais)")
    imprima("    R$ 200 (20%) -> Reinvestido na Republica (infraestrutura)")
    imprima("    + Credito da Republica para Vencedor")
    imprima("\n  DURANTE A TRANSICAO: dinheiro + credito coexistem")
    imprima("  DEPOIS DA TRANSICAO: so credito. Dinheiro extinto.")

    // === 5. ONG IMPACTO ===
    imprima("\n\n  === 5. IMPACTO DAS ONGs ===\n")
    para cada ngo em engine.list_ngos():
        se ngo["verified"]  e  ngo["received"] > 0 entao:
            imprima("  {ngo['name']:<35} recebeu R$ {ngo['received']:,.0f} "
                  "-> {ngo['helped']} pessoas ajudadas")

    // === 6. STATS ===
    imprima("\n\n  === 6. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<35} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DO OPENBUSINESSMODEL")
    imprima("{'='*80}")
    imprima("""
  DURANTE A TRANSICAO (OpenTransition Fase 3-4):
    Dinheiro e credito COEXISTEM.
    Competicoes premiam em HIBRIDO:
    - Parte em dinheiro (antigo) para vencedor
    - Parte em credito (Republica) para vencedor
    - Parte em dinheiro para ONG verificada
    - Parte reinvestida na Republica

  MODELO LEGO (encadeamento de pecas):
    Cada operacao e uma CADEIA de pecas encaixadas:

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
    ONGs continuam, mas financidas por credito, nao dinheiro.
    A cadeia LEGO continua a mesma. So a moeda muda.

  ARQUITETURA MODULAR LEGO:
    Tudo na Republica agora encaixa como LEGO.
    OpenBusinessModel encaixa em OpenTransition.
    OpenTransition encaixa em OpenModularArchitecture.
    OpenOperations encaixa em OpenBusinessModel.
    Cada peca tem entrada e saida. Tudo conecta.

  PRINCIPIOS:
    P1: Premio para todos. Sem elitismo na distribuicao.
    P2: ONG so se verificada. Protege pessoas de fraude.
    seja P3: Vencedor e ONG ganham. Trabalho = base 1.0.
    P4: Alocacao votada pela assembleia (50/30/20 ajustavel).
// )
    imprima("{'='*80}")
    imprima("  OpenBusinessModel: {s['total_competitions']} competicoes, "
          "{s['total_donated']:,.0f} doado, "
          "{s['people_helped']} pessoas ajudadas.")
    imprima("  Modelo LEGO: pecas encaixam em cadeia.")
    imprima("{'='*80}")

```
