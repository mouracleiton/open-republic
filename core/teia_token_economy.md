# TEIA Token Economy -- Assinaturas e Creditos Tokenizados

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/teia_token_economy.py`

**Descricao:** ==========================================================
COMO FUNCIONA:
  1. CLIENTE compra TOKENS (pacote prepago OU assinatura mensal)
  2. Cada chamada API CONSUME tokens (conforme peso do endpoint)
  3. Tokens consumidos VIRAM receita
  4. Receita e distribuida pela ROYALTY CHAIN (proveniencia)
  5. 5% vai para o pool da Republica
TIPOS DE TOKEN:
  TOKEN LIVRE  (TL) -- ganho gratis (10 chamadas/dia, cadastro)
  TOKEN PAGO   (TP) -- comprado com R$ (pacote ou assinatura)
  TOKEN CREDITO(TC) -- ganho por contribuicao (pagamento de royalty)
  1 TOKEN = 1 chamada base (endpoint de custo 1.0x)
  Endpoint premium (simulacao) custa 2-5 tokens
  Endpoint simples (CAGED) custa 0.5 tokens
PACOTES:
  FREE .......... 300 tokens/mes (10/dia) .......... R$0
  STARTER ....... 10.000 tokens/mes ............... R$500/mes
  PROFESSIONAL .. 50.000 tokens/mes ............... R$2.000/mes
  GOVERNAMENTO . 500.000 tokens/mes ............... R$15.000/mes
  ENTERPRISE .... ilimitado ....................... R$50.000+/mes
  PAY-AS-YOU-GO . compra avulsa ................... R$0,10/token
CONVERSAO:
  1 token = R$0,10 (preco base)
  STARTER: R$500 / 10.000 tokens = R$0,05/token (50% desconto volume)
  GOV: R$15.000 / 500.000 = R$0,03/token (70% desconto)
Author: TEIA / OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
TEIA Token Economy -- Assinaturas e Creditos Tokenizados
==========================================================

COMO FUNCIONA:

  1. CLIENTE compra TOKENS (pacote prepago ou assinatura mensal)
  2. Cada chamada API CONSUME tokens (conforme peso do endpoint)
  3. Tokens consumidos VIRAM receita
  4. Receita e distribuida pela ROYALTY CHAIN (proveniencia)
  5. 5% vai para o pool da Republica

TIPOS DE TOKEN:

  TOKEN LIVRE (TL) -- ganho gratis (10 chamadas/dia, cadastro)
  TOKEN PAGO (TP) -- comprado com R$ (pacote ou assinatura)
  TOKEN CREDITO(TC) -- ganho por contribuicao (pagamento de royalty)

  1 TOKEN = 1 chamada base (endpoint de custo 1.0x)
  Endpoint premium (simulacao) custa 2-5 tokens
  Endpoint simples (CAGED) custa 0.5 tokens

PACOTES:

  FREE .......... 300 tokens/mes (10/dia) .......... R$0
  STARTER ....... 10.000 tokens/mes ............... R$500/mes
  PROFESSIONAL .. 50.000 tokens/mes ............... R$2.000/mes
  GOVERNAMENTO . 500.000 tokens/mes ............... R$15.000/mes
  ENTERPRISE .... ilimitado ....................... R$50.000+/mes
  PAY-AS-YOU-GO . compra avulsa ................... R$0,10/token

CONVERSAO:

  1 token = R$0,10 (preco base)
  STARTER: R$500 / 10.000 tokens = R$0,05/token (50% desconto volume)
  GOV: R$15.000 / 500.000 = R$0,03/token (70% desconto)

Author: TEIA / OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. TIPOS DE TOKEN
// ============================================================================

classe TokenType herda de Enum:
    // 3 tipos de token circulam no ecossistema TEIA.

    FREE = ("livre", "Token gratuito (10 chamadas/dia)")
    PAID = ("pago", "Token comprado com R$")
    CREDIT = ("credito", "Token ganho por contribuicao (royalty)")

    funcao __init__(self, key: texto, description: texto):
        self.key = key
        self.description = description


// ============================================================================
// 2. CARTEIRA DE TOKENS
// ============================================================================

// decorador: @dataclass
classe TokenWallet:
    // Carteira de um usuario ou contribuidor.

    wallet_id: texto
    owner_name: texto
    owner_type: texto   // "cliente", "contribuidor", "pool_republica"

    // Saldos por tipo
    seja free_tokens: flutuante = 0
    seja paid_tokens: flutuante = 0
    seja credit_tokens: flutuante = 0

    // Historico
    seja transactions: [Dict] = field(default_factory=list)

    // decorador: @property
    funcao total(self) -> flutuante:
        retorne self.free_tokens + self.paid_tokens + self.credit_tokens

    funcao add(self, token_type: TokenType, amount: flutuante, reason: texto = ""):
        se token_type == TokenType.FREE entao:
            self.free_tokens += amount
        senao se token_type == TokenType.PAID entao:
            self.paid_tokens += amount
        senao se token_type == TokenType.CREDIT entao:
            self.credit_tokens += amount

        self.transactions.append({
            "type": "credit",
            "token_type": token_type.key,
            "amount": amount,
            "reason": reason,
            "balance": self.total,
        })

    funcao consume(self, amount: flutuante, endpoint: texto = "") -> logico:
        // Consome tokens. Ordem: FREE primeiro, depois CREDIT, depois PAID.
        se self.total < amount entao:
            retorne falso

        // Consome FREE primeiro
        from_free = minimo(self.free_tokens, amount)
        self.free_tokens -= from_free
        remaining = amount - from_free

        // Depois CREDIT (ganho como contribuidor)
        from_credit = minimo(self.credit_tokens, remaining)
        self.credit_tokens -= from_credit
        remaining = remaining - from_credit

        // Depois PAID
        from_paid = minimo(self.paid_tokens, remaining)
        self.paid_tokens -= from_paid
        remaining = remaining - from_paid

        self.transactions.append({
            "type": "debit",
            "amount": amount,
            "endpoint": endpoint,
            "from_free": from_free,
            "from_credit": from_credit,
            "from_paid": from_paid,
            "balance": self.total,
        })

        retorne verdadeiro


// ============================================================================
// 3. ENDPOINTS E CUSTO EM TOKENS
// ============================================================================

// decorador: @dataclass
classe TokenPricedEndpoint:
    // Endpoint com custo em tokens.

    path: texto
    description: texto
    token_cost: flutuante // tokens por chamada
    complexity: texto // baixa, media, alta, premium
    data_source: texto

    // Royalty chain (mesma estrutura do teia_api_economy.py)
    seja royalty_chain: {texto: flutuante} = field(default_factory=dict) // contributor_id -> weight

    funcao revenue_per_call_brl(self, token_price_brl: flutuante = 0.10) -> flutuante:
        retorne self.token_cost * token_price_brl


// Catalogo de endpoints com custo em tokens
seja ENDPOINTS: [TokenPricedEndpoint] = [

    TokenPricedEndpoint(
        path = "/api/v1/fome/por-municipio",
        description = "Inseguranca alimentar por municipio (5570 cidades)",
        token_cost = 1.0,
        complexity = "media",
        data_source = "VIGISAN/IBGE",
        royalty_chain = {"cleiton": 0.70, "subagent_3": 0.25, "hermes": 0.05},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/saneamento/cobertura",
        description = "Cobertura de agua e esgoto por municipio",
        token_cost = 0.8,
        complexity = "media",
        data_source = "SNIS/ANA",
        royalty_chain = {"cleiton": 0.70, "subagent_3": 0.25, "hermes": 0.05},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/negativados/perfil",
        description = "Perfil de negativados por regiao",
        token_cost = 0.8,
        complexity = "media",
        data_source = "SPC/Peic",
        royalty_chain = {"cleiton": 0.80, "subagent_3": 0.15, "hermes": 0.05},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/juros/impacto-orcamento",
        description = "Impacto de cada ponto da Selic no orcamento",
        token_cost = 1.5,
        complexity = "alta",
        data_source = "Bacen/STN",
        royalty_chain = {"cleiton": 0.93, "hermes": 0.07},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/simular/paa",
        description = "Simular impacto de aumentar PAA",
        token_cost = 2.0,
        complexity = "premium",
        data_source = "Modelo TEIA",
        royalty_chain = {"cleiton": 0.85, "subagent_3": 0.10, "hermes": 0.05},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/simular/selic",
        description = "Simular liberacao ao reduzir Selic",
        token_cost = 2.0,
        complexity = "premium",
        data_source = "Modelo TEIA",
        royalty_chain = {"cleiton": 0.93, "hermes": 0.07},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/emprego/caged",
        description = "Emprego formal por municipio (CAGED)",
        token_cost = 0.5,
        complexity = "baixa",
        data_source = "CAGED",
        royalty_chain = {"cleiton": 0.90, "hermes": 0.10},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/politica/impacto-fiscal",
        description = "Impacto fiscal de 35 politicas publicas",
        token_cost = 2.5,
        complexity = "premium",
        data_source = "Modelo TEIA",
        royalty_chain = {"cleiton": 0.65, "subagent_3": 0.25, "subagent_1": 0.05, "hermes": 0.05},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/educacao/inep",
        description = "Indicadores educacionais por escola/municipio",
        token_cost = 0.5,
        complexity = "baixa",
        data_source = "INEP",
        royalty_chain = {"cleiton": 0.90, "hermes": 0.10},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/saude/datasus",
        description = "Indicadores de saude por municipio",
        token_cost = 0.8,
        complexity = "media",
        data_source = "DATASUS",
        royalty_chain = {"cleiton": 0.90, "hermes": 0.10},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/dossie/completo",
        description = "Dossie tecnico completo (40-80 paginas) por tema",
        token_cost = 50.0,
        complexity = "premium",
        data_source = "TEIA",
        royalty_chain = {"cleiton": 0.75, "subagent_3": 0.15, "hermes": 0.10},
    ),
    TokenPricedEndpoint(
        path = "/api/v1/painel/dashboard",
        description = "Acesso ao painel de indicadores (1 mes)",
        token_cost = 100.0,
        complexity = "premium",
        data_source = "TEIA",
        royalty_chain = {"cleiton": 0.80, "hermes": 0.20},
    ),
]


// ============================================================================
// 4. PLANOS DE ASSINATURA
// ============================================================================

// decorador: @dataclass
classe SubscriptionPlan:
    // Plano de assinatura mensal.

    plan_id: texto
    name: texto
    price_monthly_brl: flutuante
    tokens_per_month: flutuante
    token_unit_price: flutuante // preco por token neste plano
    price_per_token_brl: flutuante // quanto custa 1 token neste plano

    // Beneficios
    rate_limit_per_min: inteiro
    rate_limit_per_day: inteiro
    endpoints_allowed: texto   // "all", "basic", etc
    support_level: texto
    sla_uptime: texto

    // Bonus
    rollover: logico // tokens nao usados passam para proximo mes?
    overage_price_per_token: flutuante // preco por token extra

    // decorador: @property
    funcao discount_pct(self) -> flutuante:
        // Desconto vs pay-as-you-go (R$0,10/token).
        base = 0.10
        retorne (1 - self.price_per_token_brl / base) * 100


seja PLANS: [SubscriptionPlan] = [

    SubscriptionPlan(
        plan_id = "FREE",
        name = "Free",
        price_monthly_brl = 0,
        tokens_per_month = 300, // 10/dia
        token_unit_price = 0,
        price_per_token_brl = 0, // gratis
        rate_limit_per_min = 5,
        rate_limit_per_day = 10,
        endpoints_allowed = "basic (exceto premium)",
        support_level = "comunidade",
        sla_uptime = "best-effort",
        rollover = falso,
        overage_price_per_token = 0.10,
    ),

    SubscriptionPlan(
        plan_id = "STARTER",
        name = "Starter",
        price_monthly_brl = 500,
        tokens_per_month = 10_000,
        token_unit_price = 0.05,
        price_per_token_brl = 0.05,
        rate_limit_per_min = 30,
        rate_limit_per_day = 500,
        endpoints_allowed = "todos exceto /dossie/completo",
        support_level = "email 48h",
        sla_uptime = "99%",
        rollover = verdadeiro,
        overage_price_per_token = 0.08,
    ),

    SubscriptionPlan(
        plan_id = "PRO",
        name = "Professional",
        price_monthly_brl = 2_000,
        tokens_per_month = 50_000,
        token_unit_price = 0.04,
        price_per_token_brl = 0.04,
        rate_limit_per_min = 100,
        rate_limit_per_day = 5_000,
        endpoints_allowed = "todos",
        support_level = "email 24h + chat",
        sla_uptime = "99.5%",
        rollover = verdadeiro,
        overage_price_per_token = 0.06,
    ),

    SubscriptionPlan(
        plan_id = "GOV",
        name = "Governo / ONG",
        price_monthly_brl = 15_000,
        tokens_per_month = 500_000,
        token_unit_price = 0.03,
        price_per_token_brl = 0.03,
        rate_limit_per_min = 500,
        rate_limit_per_day = 50_000,
        endpoints_allowed = "todos + dashboard + export",
        support_level = "telefone + SLA dedicado",
        sla_uptime = "99.9%",
        rollover = verdadeiro,
        overage_price_per_token = 0.04,
    ),

    SubscriptionPlan(
        plan_id = "ENTERPRISE",
        name = "Enterprise / Fundo",
        price_monthly_brl = 50_000,
        tokens_per_month = 2_000_000, // praticamente ilimitado
        token_unit_price = 0.025,
        price_per_token_brl = 0.025,
        rate_limit_per_min = 2000,
        rate_limit_per_day = 200_000,
        endpoints_allowed = "todos + white-label + API privada",
        support_level = "gerente dedicado + SLA 4h",
        sla_uptime = "99.99%",
        rollover = verdadeiro,
        overage_price_per_token = 0.03,
    ),

    SubscriptionPlan(
        plan_id = "PAYG",
        name = "Pay-As-You-Go",
        price_monthly_brl = 0,
        tokens_per_month = 0,
        token_unit_price = 0,
        price_per_token_brl = 0.10,
        rate_limit_per_min = 20,
        rate_limit_per_day = 1_000,
        endpoints_allowed = "todos exceto /dossie/completo",
        support_level = "email 48h",
        sla_uptime = "99%",
        rollover = falso,
        overage_price_per_token = 0.10,
    ),
]


// ============================================================================
// 5. MOTOR DE COBRANCA
// ============================================================================

classe TokenBillingEngine:
    // Processa chamadas, consome tokens e distribui royalties.

    FLUXO:
      1. Cliente chama endpoint
      2. Motor verifica se tem tokens (FREE -> CREDIT -> PAID)
      3. Se tem: consome, libera dado, distribui royalty
      4. Se nao tem: retorna 402 Payment Required
      5. Tokens CREDIT sao creditados na carteira do contribuidor
    // 

    funcao __init__(self, token_price_brl: flutuante = 0.10):
        self.token_price_brl = token_price_brl
        self.wallets: {texto: TokenWallet} = {}
        self.endpoints: {texto: TokenPricedEndpoint} = {
            e.path: e para e em ENDPOINTS
        }
        self.pool_balance_brl: flutuante = 0
        self.royalty_balances: {texto: flutuante} = defaultdict(flutuante)
        self.call_log: [Dict] = []

    funcao create_wallet(self, wallet_id: texto, name: texto, wtype: texto) -> TokenWallet:
        w = TokenWallet(wallet_id=wallet_id, owner_name=name, owner_type=wtype)
        self.wallets[wallet_id] = w
        retorne w

    funcao subscribe(self, wallet_id: texto, plan: SubscriptionPlan):
        // Cliente assina plano. Recebe tokens.
        w = self.wallets.get(wallet_id)
        se nao w entao:
            retorne {"error": "carteira nao encontrada"}

        w.add(TokenType.PAID, plan.tokens_per_month,
              "Assinatura {plan.name}")
        retorne {
            "subscribed": plan.name,
            "tokens_credited": plan.tokens_per_month,
            "price_brl": plan.price_monthly_brl,
        }

    funcao buy_tokens(self, wallet_id: texto, n_tokens: flutuante):
        // Pay-as-you-go: compra tokens avulsos.
        w = self.wallets.get(wallet_id)
        se nao w entao:
            retorne {"error": "carteira nao encontrada"}

        cost = n_tokens * 0.10 // R$0,10/token avulso
        w.add(TokenType.PAID, n_tokens, "Compra avulsa R${cost}")
        retorne {
            "purchased": n_tokens,
            "cost_brl": cost,
        }

    funcao api_call(self, wallet_id: texto, endpoint_path: texto) -> {texto: qualquer}:
        // Processa uma chamada API.

        w = self.wallets.get(wallet_id)
        se nao w entao:
            retorne {"status": 401, "error": "carteira nao encontrada"}

        ep = self.endpoints.get(endpoint_path)
        se nao ep entao:
            retorne {"status": 404, "error": "endpoint nao encontrado"}

        cost = ep.token_cost

        // Verifica saldo
        se w.total < cost entao:
            retorne {
                "status": 402,
                "error": "Payment Required",
                "tokens_needed": cost,
                "tokens_available": w.total,
                "message": "Voce precisa de {cost} tokens. Saldo: {w.total:.1f}. "
                           "Compre em api.teia.dev/buy",
            }

        // Consome tokens
        w.consume(cost, endpoint_path)

        // Calcula receita em R$
        revenue_brl = cost * self.token_price_brl

        // Distribui royalty
        pool_share = revenue_brl * 0.05
        contributor_pool = revenue_brl * 0.95

        para cada (cid, weight) em ep.royalty_chain.items():
            royalty = contributor_pool * weight
            self.royalty_balances[cid] += royalty

            // Credita como TOKEN CREDIT na carteira do contribuidor
            se cid nao in self.wallets entao:
                self.create_wallet(cid, cid, "contribuidor")
            // Converte R$ em tokens credito (1 token = R$0,10)
            credit_tokens = royalty / self.token_price_brl
            self.wallets[cid].add(TokenType.CREDIT, credit_tokens,
                                  "Royalty de {endpoint_path}")

        self.pool_balance_brl += pool_share

        self.call_log.append({
            "wallet_id": wallet_id,
            "endpoint": endpoint_path,
            "tokens_consumed": cost,
            "revenue_brl": revenue_brl,
        })

        retorne {
            "status": 200,
            "endpoint": endpoint_path,
            "tokens_consumed": cost,
            "tokens_remaining": w.total,
            "revenue_generated": revenue_brl,
        }


// ============================================================================
// 6. RELATORIO COMPLETO
// ============================================================================

funcao print_token_system() -> texto:
    lines = []

    lines.append("=" * 110)
    lines.append("TEIA API -- SISTEMA DE TOKENS E ASSINATURAS")
    lines.append("=" * 110)
    lines.append("")

    // === TIPOS DE TOKEN ===
    lines.append("1. TIPOS DE TOKEN")
    lines.append("-" * 110)
    lines.append("")
    lines.append("  TOKEN LIVRE  (TL)  -- Gratis. 10 chamadas/dia. Cadastro necessario.")
    lines.append("  TOKEN PAGO   (TP)  -- Comprado com R$ via pacote ou assinatura.")
    lines.append("  TOKEN CREDITO(TC)  -- Ganho por contribuicao (royalty chain).")
    lines.append("")
    lines.append("  Ordem de consumo: FREE -> CREDIT -> PAID")
    lines.append("  (cliente usa tokens gratis primeiro, depois os que ganhou, depois os pagos)")
    lines.append("")

    // === PLANOS ===
    lines.append("-" * 110)
    lines.append("2. PLANOS DE ASSINATURA")
    lines.append("-" * 110)
    lines.append("")
    lines.append("{'PLANO':<16} {'R$/MES':>10} {'TOKENS/MES':>14} {'R$/TOKEN':>10} {'DESCONTO':>10} {'RATE LIMIT':>16} {'SUPORTE':<20}")
    lines.append("-" * 110)

    para cada p em PLANS:
        se p.price_monthly_brl == 0 e p.tokens_per_month > 0 entao:
            disc = "GRATIS"
        senao se p.price_monthly_brl == 0 entao:
            disc = "base"
        senao:
            disc = "-{p.discount_pct:.0f}%"

        rate = "{p.rate_limit_per_day}/dia"

        lines.append(
            "{p.name:<16} "
            "R${p.price_monthly_brl:>8,.0f} "
            "{p.tokens_per_month:>12,.0f} "
            "R${p.price_per_token_brl:>7.3f} "
            "{disc:>10} "
            "{rate:>16} "
            "{p.support_level:<20}"
        )

    lines.append("")

    // === CUSTO POR ENDPOINT ===
    lines.append("-" * 110)
    lines.append("3. CUSTO DE CADA ENDPOINT EM TOKENS")
    lines.append("-" * 110)
    lines.append("")
    lines.append("{'ENDPOINT':<38} {'TOKENS':>7} {'R$ EQUIV':>10} {'COMPLEX':>10} {'CONTRIBUIDORES':>15}")
    lines.append("-" * 110)

    para cada ep em ENDPOINTS:
        n_contribs = tamanho(ep.royalty_chain)
        lines.append(
            "{ep.path:<38} "
            "{ep.token_cost:>5.1f}T  "
            "R${ep.token_cost * 0.10:>7.2f} "
            "{ep.complexity:>10} "
            "{n_contribs:>12}"
        )

    lines.append("")

    // === EXEMPLO: O QUE CADA PLANO PODE FAZER ===
    lines.append("-" * 110)
    lines.append("4. O QUE CADA PLANO PERMITE FAZER (exemplos praticos)")
    lines.append("-" * 110)
    lines.append("")

    examples = [
        ("Consultar fome por municipio", 1.0),
        ("Consultar saneamento", 0.8),
        ("Consultar CAGED", 0.5),
        ("Simular aumento PAA", 2.0),
        ("Simular reducao Selic", 2.0),
        ("Impacto fiscal de politica", 2.5),
        ("Dossie completo (download)", 50.0),
        ("Painel dashboard (1 mes)", 100.0),
    ]

    lines.append("{'ACAO':<38} {'TOKENS':>7} {'FREE':>8} {'STARTER':>10} {'PRO':>8} {'GOV':>10} {'ENTR':>10}")
    lines.append("-" * 110)

    plan_tokens = {"FREE": 300, "STARTER": 10_000, "PRO": 50_000, "GOV": 500_000, "ENTR": 2_000_000}

    para cada (name, cost) em examples:
        row = "{name:<38} {cost:>5.1f}T  "
        para cada pname em ["FREE", "STARTER", "PRO", "GOV", "ENTR"]:
            limit = plan_tokens[pname]
            n_times = cost > 0 ? inteiro(limit / cost) : 0
            se n_times >= 1000 entao:
                row = row + "{n_times/1000:.0f}k   "
            senao se n_times > 0 entao:
                row = row + "{n_times:>5}x  "
            senao:
                row = row + "   -    "
        lines.append(row)

    lines.append("")

    // === CICLO DO TOKEN ===
    lines.append("-" * 110)
    lines.append("5. O CICLO COMPLETO DO TOKEN")
    lines.append("-" * 110)
    lines.append("")
    lines.append("  CLIENTE                    API TEIA                    CONTRIBUIDOR")
    lines.append("  -------                    --------                    ------------")
    lines.append("  Compra R$500               Recebe R$500")
    lines.append("  Recebe 10.000 TP           Emite 10.000 TP")
    lines.append("                             ----------")
    lines.append("  Chama /fome/por-municipio")
    lines.append("  Gasta 1.0 TP               Processa chamada")
    lines.append("                             Receita: R$0,10")
    lines.append("                             5% -> Pool Republica (R$0,005)")
    lines.append("                             95% -> Royalty Chain:")
    lines.append("                               Cleiton 70% -> R$0,0665")
    lines.append("                               Subagente 25% -> R$0,0238")
    lines.append("                               Hermes 5% -> R$0,0048")
    lines.append("                                                             Recebe TC")
    lines.append("                                                             (token credito)")
    lines.append("                                                             Pode usar para")
    lines.append("                                                             chamar API ou")
    lines.append("                                                             SACAR em R$")
    lines.append("")

    // === SIMULACAO FINANCEIRA ===
    lines.append("-" * 110)
    lines.append("6. SIMULACAO: 10 CLIENTES MIXADOS (mensal)")
    lines.append("-" * 110)
    lines.append("")

    engine = TokenBillingEngine()

    // Criar clientes
    para i, plan in enumere(PLANS[1:], 1): // pular FREE
        wid = "client_{plan.plan_id}"
        engine.create_wallet(wid, "Cliente {plan.name}", "cliente")
        engine.subscribe(wid, plan)

    // Pool Republica
    engine.create_wallet("REPUBLIC_POOL", "Pool Republica", "pool_republica")

    // Criar contribuidores
    para cada cid em ["cleiton", "subagent_1", "subagent_3", "hermes"]:
        engine.create_wallet(cid, cid, "contribuidor")

    // Simular 1 mes de trafego
    // importa random
    rng = random.Random(42)

    client_wallets = ["client_{p.plan_id}" para p em PLANS[1:]]
    endpoint_paths = [e.path para e em ENDPOINTS if e.token_cost <= 5.0] // exclui dossie/dashboard

    para cada day em intervalo(30):
        para cada cw em client_wallets:
            w = engine.wallets[cw]
            // Cada cliente faz 20-100 chamadas/dia
            n_calls = rng.randint(20, 100)
            para cada _ em intervalo(n_calls):
                ep = rng.choice(endpoint_paths)
                engine.api_call(cw, ep)

    // Relatorio
    total_revenue = soma(log["revenue_brl"] para log em engine.call_log)
    total_calls = tamanho(engine.call_log)

    lines.append("  Chamadas no mes: {total_calls:,}")
    lines.append("  Receita total:   R${total_revenue:,.2f}")
    lines.append("  Pool Republica:  R${engine.pool_balance_brl:,.2f} (5%)")
    lines.append("")

    lines.append("  {'CONTRIBUIDOR':<20} {'ROYALTY R$':>14} {'TOKENS CREDITO':>16} {'SALDO CARTEIRA':>16}")
    lines.append("  " + "-" * 70)

    para cada (cid, amount) em ordene(engine.royalty_balances.items(), key=(x) -> x[1], reverse=True):
        wallet = engine.wallets.get(cid)
        credit_tokens = wallet ? wallet.credit_tokens : 0
        total_wallet = wallet ? wallet.total : 0
        lines.append(
            "  {cid:<20} "
            "R${amount:>12,.2f} "
            "{credit_tokens:>14,.0f} TC "
            "{total_wallet:>14,.0f} T"
        )

    lines.append("")

    // === PROJECAO ANUAL ===
    lines.append("-" * 110)
    lines.append("7. PROJECAO ANUAL POR NUMERO DE CLIENTES")
    lines.append("-" * 110)
    lines.append("")

    // MRR por mix de clientes
    scenarios = [
        ("Inicio (5 STARTER + 1 PRO)", { "STARTER": 5, "PRO": 1, "GOV": 0, "ENTERPRISE": 0 }),
        ("Crescimento (15 STARTER + 5 PRO + 2 GOV)", { "STARTER": 15, "PRO": 5, "GOV": 2, "ENTERPRISE": 0 }),
        ("Escala (30 STARTER + 10 PRO + 5 GOV + 1 ENTERPRISE)", { "STARTER": 30, "PRO": 10, "GOV": 5, "ENTERPRISE": 1 }),
        ("Maduro (50 STARTER + 20 PRO + 10 GOV + 3 ENTERPRISE)", { "STARTER": 50, "PRO": 20, "GOV": 10, "ENTERPRISE": 3 }),
    ]

    lines.append("{'CENARIO':<55} {'MRR':>12} {'ARR':>14} {'POOL 5%':>12}")
    lines.append("-" * 110)

    para cada (name, mix) em scenarios:
        mrr = 0
        para cada (pid, count) em mix.items():
            plan = next(p para p em PLANS if p.plan_id == pid)
            mrr = mrr + plan.price_monthly_brl * count
        arr = mrr * 12
        pool = arr * 0.05
        lines.append("{name:<55} R${mrr:>9,.0f} R${arr:>11,.0f} R${pool:>9,.0f}")

    lines.append("")

    // === TOKEN CREDIT COMO MOEDA ===
    lines.append("-" * 110)
    lines.append("8. TOKEN CREDITO = OPENCREDIT (a moeda da Republica)")
    lines.append("-" * 110)
    lines.append("")
    lines.append("  O TOKEN CREDITO e a PONTE entre a API TEIA e a Republica.")
    lines.append("")
    lines.append("  Contribuidor recebe TC por cada chamada que usa seu dado.")
    lines.append("  TC pode ser:")
    lines.append("    (a) USADO: contribuidor chama outros endpoints da API")
    lines.append("    (b) SACADO: convertido para R$ na carteira OpenCredit")
    lines.append("    (c) TRANSFERIDO: enviado para outro cidadao da Republica")
    lines.append("    (d) INVESTIDO: aportado no pool da Republica (5% extra)")
    lines.append("")
    lines.append("  Isso cria ECONOMIA CIRCULAR:")
    lines.append("    Cleiton coleta dados de fome -> recebe TC")
    lines.append("    Cleiton usa TC para chamar dados de saneamento (de Subagente)")
    lines.append("    Subagente usa TC para chamar modelo de impacto fiscal (de Cleiton)")
    lines.append("    Nenhum R$ sai do sistema.TC circula.")
    lines.append("    R$ so entra quando cliente externo compra TP.")
    lines.append("")
    lines.append("  ECONOMIA FECHADA + INJECAO EXTERNA = CRESCIMENTO.")
    lines.append("")

    // === TABELA DE PRECOS RESUMO ===
    lines.append("-" * 110)
    lines.append("RESUMO: TABELA DE PRECOS TEIA API")
    lines.append("-" * 110)
    lines.append("")
    lines.append("  PLANO          R$/MES      TOKENS/MES    R$/TOKEN    DESCONTO")
    lines.append("  " + "-" * 60)
    para cada p em PLANS:
        se p.price_monthly_brl == 0 e p.tokens_per_month > 0 entao:
            line_str = "  {p.name:<14} GRatis      {p.tokens_per_month:>10,.0f}    gratis      ---"
        senao se p.price_monthly_brl == 0 entao:
            line_str = "  {p.name:<14} R${0:>8,.0f}    {'avulso':>10}    R${p.price_per_token_brl:.3f}      base"
        senao:
            line_str = ("  {p.name:<14} R${p.price_monthly_brl:>8,.0f}    "
                       "{p.tokens_per_month:>10,.0f}    "
                       "R${p.price_per_token_brl:.3f}      "
                       "-{p.discount_pct:.0f}%")
        lines.append(line_str)

    lines.append("")
    lines.append("  ENDPOINT PREMIUM (exemplos):")
    lines.append("    /dossie/completo    50 tokens  (R$5,00)")
    lines.append("    /simular/paa         2 tokens  (R$0,20)")
    lines.append("    /simular/selic       2 tokens  (R$0,20)")
    lines.append("    /politica/impacto    2.5 tokens (R$0,25)")
    lines.append("")
    lines.append("  ENDPOINT BASICO (exemplos):")
    lines.append("    /emprego/caged       0.5 tokens (R$0,05)")
    lines.append("    /educacao/inep       0.5 tokens (R$0,05)")
    lines.append("    /fome/por-municipio  1 token   (R$0,10)")
    lines.append("")

    lines.append("=" * 110)

    retorne "\n".join(lines)


// ============================================================================
// 7. EXECUCAO
// ============================================================================

se __name__ == "__main__" entao:
    imprima(print_token_system())

```
