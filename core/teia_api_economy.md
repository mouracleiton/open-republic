# TEIA API Economy -- Micropagamentos por Chamada com Royalty Chain

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/teia_api_economy.py`

**Descricao:** ==================================================================
O MODELO:
  Instagram/TikTok pagam criadores por view.
  TEIA API paga CONTRIBUIDORES por chamada.
  Cada dado na API tem uma CADEIA DE PROVENIENCIA:
    - Quem coletou o dado bruto
    - Quem limpou
    - Quem cruzou com outro dataset
    - Quem construiu o modelo
    - Quem escreveu a documentacao
    - Quem fact-checkou
    - Quem construiu o endpoint
  Cada chamada API gera micro-receita.
  Essa receita ESCOA pela cadeia de proveniencia.
  Exemplo:
    Cliente chama /api/fome/por-municipio
    Custo: R$0,05 por chamada
    R$0,05 distribuido para 6 pessoas que contribuiram:
      - Quem coletou VIGISAN:    R$0,015 (30%)
      - Quem limpou dados:       R$0,010 (20%)
      - Quem cruzou com CADunico: R$0,008 (16%)
      - Quem construiu modelo:   R$0,007 (14%)
      - Quem documentou:         R$0,005 (10%)
      - Quem fact-checkou:       R$0,005 (10%)
    Pool Republica (5%):         R$0,0025
  1 chamada = R$0,05. 100.000 chamadas/dia = R$5.000/dia.
  Cada contribuidor recebe sua fração. Todo dia. Automaticamente.
Author: TEIA / OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
TEIA API Economy -- Micropagamentos por Chamada com Royalty Chain
==================================================================

O MODELO:
  Instagram/TikTok pagam criadores por view.
  TEIA API paga CONTRIBUIDORES por chamada.

  Cada dado na API tem uma CADEIA DE PROVENIENCIA:
    - Quem coletou o dado bruto
    - Quem limpou
    - Quem cruzou com outro dataset
    - Quem construiu o modelo
    - Quem escreveu a documentacao
    - Quem fact-checkou
    - Quem construiu o endpoint

  Cada chamada API gera micro-receita.
  Essa receita ESCOA pela cadeia de proveniencia.

  Exemplo:
    Cliente chama /api/fome/por-municipio
    Custo: R$0,05 por chamada
    R$0,05 distribuido para 6 pessoas que contribuiram:
      - Quem coletou VIGISAN: R$0,015 (30%)
      - Quem limpou dados: R$0,010 (20%)
      - Quem cruzou com CADunico: R$0,008 (16%)
      - Quem construiu modelo: R$0,007 (14%)
      - Quem documentou: R$0,005 (10%)
      - Quem fact-checkou: R$0,005 (10%)
    Pool Republica (5%): R$0,0025

  1 chamada = R$0,05. 100.000 chamadas/dia = R$5.000/dia.
  Cada contribuidor recebe sua fração. Todo dia. Automaticamente.

Author: TEIA / OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa datetime, timedelta de datetime
// importa defaultdict de collections


// ============================================================================
// 1. TIPOS DE CONTRIBUICAO (a cadeia de proveniencia)
// ============================================================================

classe ContributionType herda de Enum:
    // Cada forma de contribuir para um dado na API.

    DATA_COLLECTION = ("coleta", "Coletou dado bruto de fonte oficial", 0.25)
    DATA_CLEANING = ("limpeza", "Limpou, normalizou, deduplicou", 0.15)
    DATA_CROSS = ("cruzamento", "Cruzou com outro dataset", 0.15)
    MODEL_BUILDING = ("modelo", "Construiu modelo analitico", 0.15)
    DOCUMENTATION = ("documentacao", "Documentou metodo e fontes", 0.10)
    FACT_CHECK = ("fact_check", "Verificou acuracia", 0.10)
    ENGINEERING = ("engenharia", "Construiu endpoint/API", 0.05)
    MAINTENANCE = ("manutencao", "Atualiza dado periodicamente", 0.05)

    funcao __init__(self, key: texto, description: texto, default_weight: flutuante):
        self.key = key
        self.description = description
        self.default_weight = default_weight


// decorador: @dataclass
classe Contribution:
    // Uma contribuicao de uma pessoa para um endpoint/dado.

    contributor_id: texto
    contributor_name: texto
    contribution_type: ContributionType
    weight: flutuante // peso relativo (default = tipo.default_weight)
    seja timestamp: flutuante = 0
    seja description: texto = ""

    // decorador: @property
    funcao effective_weight(self) -> flutuante:
        // Pode ser ajustado pelo nivel de senioridade do contribuidor.
        retorne self.weight


// ============================================================================
// 2. ENDPOINT DA API (cada dado exposto)
// ============================================================================

// decorador: @dataclass
classe APIEndpoint:
    // Um endpoint da API TEIA.

    endpoint_id: texto           // ex: "/api/fome/por-municipio"
    path: texto                  // ex: "/api/v1/fome/por-municipio"
    description: texto
    data_source: texto           // ex: "VIGISAN/IBGE 2022"
    category: texto              // ex: "seguranca_alimentar"

    // Precificacao
    seja price_per_call: flutuante = 0.05 // R$ por chamada
    seja free_tier_daily: inteiro = 10 // chamadas gratis por dia

    // Contribuidores (CADEIA DE PROVENIENCIA)
    seja contributions: [Contribution] = field(default_factory=list)

    // Metricas
    seja calls_today: inteiro = 0
    seja calls_total: inteiro = 0
    seja revenue_total: flutuante = 0.0

    // decorador: @property
    funcao n_contributors(self) -> inteiro:
        retorne tamanho(set(c.contributor_id para c em self.contributions))

    // decorador: @property
    funcao total_weight(self) -> flutuante:
        retorne soma(c.effective_weight para c em self.contributions)

    funcao contributor_share(self, contributor_id: texto) -> flutuante:
        // Fracao da receita deste endpoint que vai para este contribuidor.
        contributor_weight = soma(
            c.effective_weight para c em self.contributions
            if c.contributor_id == contributor_id
        )
        se self.total_weight == 0 entao:
            retorne 0.0
        retorne contributor_weight / self.total_weight

    funcao revenue_split(self) retorna List[{texto: qualquer}]:
        // Como a receita de UMA chamada se divide.
        splits = []
        pool_pct = 0.05 // 5% para Republica (LEI)

        // Agrupa por contribuidor
        seja contributor_weights: {texto: flutuante} = defaultdict(flutuante)
        seja contributor_names: {texto: texto} = {}
        seja contributor_roles: Dict[texto, [texto]] = defaultdict(list)

        para cada c em self.contributions:
            contributor_weights[c.contributor_id] += c.effective_weight
            contributor_names[c.contributor_id] = c.contributor_name
            contributor_roles[c.contributor_id].append(c.contribution_type.key)

        total = soma(contributor_weights.values())
        se total == 0 entao:
            retorne []

        revenue_after_pool = self.price_per_call * (1 - pool_pct)

        para cada (cid, weight) em contributor_weights.items():
            share = weight / total
            amount = revenue_after_pool * share
            splits.append({
                "contributor_id": cid,
                "contributor_name": contributor_names[cid],
                "roles": contributor_roles[cid],
                "weight": weight,
                "share_pct": share * 100,
                "amount_per_call": amount,
            })

        // Pool da Republica
        splits.append({
            "contributor_id": "REPUBLIC_POOL",
            "contributor_name": "Pool da Republica (5% LEI)",
            "roles": ["pool"],
            "weight": 0,
            "share_pct": pool_pct * 100,
            "amount_per_call": self.price_per_call * pool_pct,
        })

        retorne splits


// ============================================================================
// 3. REGISTRO DE ENDPOINTS (a API completa)
// ============================================================================

classe TEIAAPI:
    // A API TEIA completa com sistema de micropagamentos.

    ESTRUTURA:
      /api/v1/fome/por-municipio
      /api/v1/fome/por-regiao
      /api/v1/saneamento/cobertura
      /api/v1/saneamento/impacto-saude
      /api/v1/negativados/por-regiao
      /api/v1/negativados/perfil
      /api/v1/emprego/caged
      /api/v1/educacao/inep
      /api/v1/saude/datasus
      /api/v1/juros/impacto-orcamento
      /api/v1/tributario/reforma-ec132
      /api/v1/politica/impacto-fiscal
      /api/v1/simular/paa
      /api/v1/simular/selic
      /api/v1/simular/creche
    // 

    funcao __init__(self):
        self.endpoints: {texto: APIEndpoint} = {}
        self._register_endpoints()

    funcao _register_endpoints(self):
        // Registra os endpoints baseados nos 16 dossies.

        // Helper para criar endpoint com contribuidores
        funcao make_endpoint(
            eid: texto, path: texto, desc: texto, source: texto, category: texto,
            price: flutuante,
            contributors: List[Tuple[texto, texto, ContributionType, flutuante]],
        ) -> APIEndpoint:

            ep = APIEndpoint(
                endpoint_id = eid,
                path = path,
                description = desc,
                data_source = source,
                category = category,
                price_per_call = price,
            )

            para cid, cname, ctype, weight in contributors:
                ep.contributions.append(Contribution(
                    contributor_id = cid,
                    contributor_name = cname,
                    contribution_type = ctype,
                    weight = weight,
                    description = ctype.description,
                ))

            retorne ep

        // === ENDPOINTS DOS 16 DOSSIES ===

        self.endpoints["fome_municipio"] = make_endpoint(
            "fome_municipio", "/api/v1/fome/por-municipio",
            "Inseguranca alimentar grave por municipio (5570 cidades)",
            "VIGISAN/IBGE 2022 + CADunico", "seguranca_alimentar",
            price = 0.10,
            contributors = [
                ("cleiton", "Cleiton", ContributionType.DATA_COLLECTION, 0.25),
                ("cleiton", "Cleiton", ContributionType.DATA_CLEANING, 0.15),
                ("cleiton", "Cleiton", ContributionType.MODEL_BUILDING, 0.15),
                ("cleiton", "Cleiton", ContributionType.DOCUMENTATION, 0.10),
                ("subagent_3", "Subagente TEIA-3", ContributionType.FACT_CHECK, 0.10),
                ("subagent_3", "Subagente TEIA-3", ContributionType.DATA_CROSS, 0.15),
                ("hermes", "Hermes AI", ContributionType.ENGINEERING, 0.05),
                ("cleiton", "Cleiton", ContributionType.MAINTENANCE, 0.05),
            ],
        )

        self.endpoints["saneamento_cobertura"] = make_endpoint(
            "saneamento_cobertura", "/api/v1/saneamento/cobertura",
            "Cobertura de agua e esgoto por municipio",
            "SNIS 2024 + ANA", "saneamento",
            price = 0.08,
            contributors = [
                ("cleiton", "Cleiton", ContributionType.DATA_COLLECTION, 0.25),
                ("subagent_3", "Subagente TEIA-3", ContributionType.DATA_CLEANING, 0.15),
                ("cleiton", "Cleiton", ContributionType.MODEL_BUILDING, 0.15),
                ("subagent_3", "Subagente TEIA-3", ContributionType.FACT_CHECK, 0.10),
                ("cleiton", "Cleiton", ContributionType.DOCUMENTATION, 0.10),
                ("cleiton", "Cleiton", ContributionType.DATA_CROSS, 0.15),
                ("hermes", "Hermes AI", ContributionType.ENGINEERING, 0.05),
                ("cleiton", "Cleiton", ContributionType.MAINTENANCE, 0.05),
            ],
        )

        self.endpoints["negativados_perfil"] = make_endpoint(
            "negativados_perfil", "/api/v1/negativados/perfil",
            "Perfil de negativados por regiao e faixa de renda",
            "SPC/Boa Vista/Peic 2024", "economia",
            price = 0.08,
            contributors = [
                ("cleiton", "Cleiton", ContributionType.DATA_COLLECTION, 0.25),
                ("cleiton", "Cleiton", ContributionType.DATA_CLEANING, 0.15),
                ("cleiton", "Cleiton", ContributionType.MODEL_BUILDING, 0.15),
                ("subagent_3", "Subagente TEIA-3", ContributionType.FACT_CHECK, 0.10),
                ("cleiton", "Cleiton", ContributionType.DOCUMENTATION, 0.10),
                ("cleiton", "Cleiton", ContributionType.DATA_CROSS, 0.15),
                ("hermes", "Hermes AI", ContributionType.ENGINEERING, 0.05),
            ],
        )

        self.endpoints["juros_impacto"] = make_endpoint(
            "juros_impacto", "/api/v1/juros/impacto-orcamento",
            "Impacto de cada ponto da Selic no orcamento publico",
            "Bacen/STN 2024", "economia",
            price = 0.15,
            contributors = [
                ("cleiton", "Cleiton", ContributionType.DATA_COLLECTION, 0.25),
                ("cleiton", "Cleiton", ContributionType.MODEL_BUILDING, 0.20),
                ("cleiton", "Cleiton", ContributionType.DOCUMENTATION, 0.10),
                ("hermes", "Hermes AI", ContributionType.ENGINEERING, 0.05),
                ("cleiton", "Cleiton", ContributionType.MAINTENANCE, 0.05),
            ],
        )

        self.endpoints["simular_paa"] = make_endpoint(
            "simular_paa", "/api/v1/simular/paa",
            "Simular impacto de aumentar PAA em R$ X",
            "Modelo TEIA (MDIC/IEPS multiplicador)", "simulacao",
            price = 0.20,
            contributors = [
                ("cleiton", "Cleiton", ContributionType.DATA_COLLECTION, 0.20),
                ("cleiton", "Cleiton", ContributionType.MODEL_BUILDING, 0.30),
                ("cleiton", "Cleiton", ContributionType.DOCUMENTATION, 0.10),
                ("subagent_3", "Subagente TEIA-3", ContributionType.FACT_CHECK, 0.10),
                ("cleiton", "Cleiton", ContributionType.DATA_CROSS, 0.15),
                ("hermes", "Hermes AI", ContributionType.ENGINEERING, 0.05),
                ("cleiton", "Cleiton", ContributionType.MAINTENANCE, 0.10),
            ],
        )

        self.endpoints["simular_selic"] = make_endpoint(
            "simular_selic", "/api/v1/simular/selic",
            "Simular liberacao orcamentaria ao reduzir Selic",
            "Modelo TEIA (Bacen)", "simulacao",
            price = 0.20,
            contributors = [
                ("cleiton", "Cleiton", ContributionType.DATA_COLLECTION, 0.20),
                ("cleiton", "Cleiton", ContributionType.MODEL_BUILDING, 0.30),
                ("cleiton", "Cleiton", ContributionType.DOCUMENTATION, 0.10),
                ("hermes", "Hermes AI", ContributionType.ENGINEERING, 0.05),
                ("cleiton", "Cleiton", ContributionType.MAINTENANCE, 0.10),
            ],
        )

        self.endpoints["emprego_caged"] = make_endpoint(
            "emprego_caged", "/api/v1/emprego/caged",
            "Emprego formal por municipio/setor (CAGED)",
            "CAGED/Min. Trabalho 2024", "emprego",
            price = 0.05,
            contributors = [
                ("cleiton", "Cleiton", ContributionType.DATA_COLLECTION, 0.25),
                ("cleiton", "Cleiton", ContributionType.DATA_CLEANING, 0.15),
                ("hermes", "Hermes AI", ContributionType.ENGINEERING, 0.05),
                ("cleiton", "Cleiton", ContributionType.MAINTENANCE, 0.05),
            ],
        )

        self.endpoints["politica_impacto"] = make_endpoint(
            "politica_impacto", "/api/v1/politica/impacto-fiscal",
            "Impacto fiscal de qualquer politica publica (35 mapeadas)",
            "Modelo TEIA (35 politicas)", "politica",
            price = 0.25,
            contributors = [
                ("cleiton", "Cleiton", ContributionType.DATA_COLLECTION, 0.20),
                ("cleiton", "Cleiton", ContributionType.MODEL_BUILDING, 0.25),
                ("subagent_3", "Subagente TEIA-3", ContributionType.DATA_CROSS, 0.15),
                ("cleiton", "Cleiton", ContributionType.DOCUMENTATION, 0.10),
                ("subagent_3", "Subagente TEIA-3", ContributionType.FACT_CHECK, 0.10),
                ("subagent_1", "Subagente TEIA-1", ContributionType.FACT_CHECK, 0.05),
                ("hermes", "Hermes AI", ContributionType.ENGINEERING, 0.05),
                ("cleiton", "Cleiton", ContributionType.MAINTENANCE, 0.10),
            ],
        )

    funcao call(self, endpoint_id: texto, n_calls: inteiro = 1) -> {texto: qualquer}:
        // Simula chamadas API e calcula distribuicao de receita.

        ep = self.endpoints.get(endpoint_id)
        se nao ep entao:
            retorne {"error": "Endpoint {endpoint_id} nao encontrado"}

        revenue = ep.price_per_call * n_calls
        ep.calls_total += n_calls
        ep.calls_today += n_calls
        ep.revenue_total += revenue

        splits = ep.revenue_split()

        // Multiplica pelo numero de chamadas
        para cada s em splits:
            s["amount_total"] = s["amount_per_call"] * n_calls

        retorne {
            "endpoint": ep.path,
            "calls": n_calls,
            "price_per_call": ep.price_per_call,
            "revenue_total": revenue,
            "splits": splits,
        }


// ============================================================================
// 4. SISTEMA DE ROYALTY (Creator Economy de Dados)
// ============================================================================

classe RoyaltyTracker:
    // Rastreia e distribui royalties para todos os contribuidores.

    MODELO INSTAGRAM/TIKTOK:
    - Plataforma rastreia views/clicks
    - Criador recebe fracao por view
    - Pagamento diario/semanal/mensal

    MODELO TEIA:
    - API rastreia chamadas por endpoint
    - Contribuidor recebe fracao por chamada
    - Cada dado tem CADEIA DE PROVENIENCIA
    - Pagamento automatico para carteira OpenCredit
    // 

    funcao __init__(self, api: TEiaAPI):
        self.api = api
        self.earnings: {texto: flutuante} = defaultdict(flutuante) // contributor_id -> R$
        self.pool_earnings: flutuante = 0.0
        self.call_log: [Dict] = []

    funcao register_calls(self, endpoint_id: texto, n_calls: inteiro):
        // Registra chamadas e distribui receita.
        result = self.api.call(endpoint_id, n_calls)

        se "error" in result entao:
            retorne result

        para cada split em result["splits"]:
            cid = split["contributor_id"]
            amount = split["amount_total"]

            se cid == "REPUBLIC_POOL" entao:
                self.pool_earnings += amount
            senao:
                self.earnings[cid] += amount

        self.call_log.append({
            "endpoint": endpoint_id,
            "calls": n_calls,
            "revenue": result["revenue_total"],
            "timestamp": tamanho(self.call_log),
        })

        retorne result

    funcao register_daily_traffic(self, calls_per_endpoint: {texto: inteiro}):
        // Simula um dia de trafego.
        para cada (eid, n) em calls_per_endpoint.items():
            self.register_calls(eid, n)

    funcao earnings_report(self) -> texto:
        // Relatorio de ganhos por contribuidor.
        lines = []

        total_revenue = soma(self.earnings.values()) + self.pool_earnings
        total_calls = soma(log["calls"] para log em self.call_log)

        lines.append("=" * 100)
        lines.append("TEIA API -- ROYALTY TRACKER (Creator Economy de Dados)")
        lines.append("=" * 100)
        lines.append("Chamadas totais: {total_calls:,}")
        lines.append("Receita total:   R${total_revenue:,.2f}")
        lines.append("Pool Republica:  R${self.pool_earnings:,.2f} (5%)")
        lines.append("")

        // Ranking de ganhos
        lines.append("-" * 100)
        lines.append("{'CONTRIBUIDOR':<25} {'GANHOS':>14} {'% DO TOTAL':>12}")
        lines.append("-" * 100)

        sorted_earnings = ordene(self.earnings.items(), key=(x) -> x[1], reverse=verdadeiro)
        para cada (cid, amount) em sorted_earnings:
            pct = total_revenue ? amount / total_revenue * 100 : 0
            lines.append("  {cid:<25} R${amount:>12,.2f} {pct:>10.1f}%")

        lines.append("  {'Pool Republica (5%)':<25} R${self.pool_earnings:>12,.2f}")
        lines.append("-" * 100)
        lines.append("  {'TOTAL':<25} R${total_revenue:>12,.2f}")

        retorne "\n".join(lines)

    funcao revenue_per_endpoint_detail(self) -> texto:
        // Detalha como cada endpoint divide a receita.
        lines = []

        lines.append("=" * 110)
        lines.append("CADEIA DE PROVENIENCIA POR ENDPOINT")
        lines.append("(Como cada chamada se divide entre contribuidores)")
        lines.append("=" * 110)

        para cada (eid, ep) em self.api.endpoints.items():
            lines.append("")
            lines.append("  {ep.path}")
            lines.append("  Preco: R${ep.price_per_call:.2f} por chamada | "
                         "Contribuidores: {ep.n_contributors} | "
                         "Fonte: {ep.data_source}")
            lines.append("  {'CONTRIBUIDOR':<25} {'PAPEIS':<40} {'PESO':>6} {'SHARE':>8} {'R$/CALL':>10}")
            lines.append("  {'-'*95}")

            splits = ep.revenue_split()
            para cada s em splits:
                roles_str = ", ".join(s["roles"])
                lines.append(
                    "  {s['contributor_name']:<25} "
                    "{roles_str:<40} "
                    "{s['weight']:>5.2f} "
                    "{s['share_pct']:>6.1f}% "
                    "R${s['amount_per_call']:>8.4f}"
                )

        retorne "\n".join(lines)


// ============================================================================
// 5. SIMULACAO DE TRAFEGO
// ============================================================================

funcao simulate_traffic() -> texto:
    // Simula cenarios de uso da API e projecao de receita.

    lines = []
    lines.append("=" * 100)
    lines.append("SIMULACAO DE TRAFEGO E RECEITA DA API TEIA")
    lines.append("=" * 100)

    api = TEIAAPI()
    tracker = RoyaltyTracker(api)

    // === CENARIO 1: Lançamento (mes 1-3) ===
    lines.append("")
    lines.append("CENARIO 1: LANCAMENTO (mes 1-3) -- poucos clientes")
    lines.append("-" * 100)

    traffic_m1 = {
        "fome_municipio": 500,        // 500 chamadas/dia
        "saneamento_cobertura": 300,
        "negativados_perfil": 200,
        "juros_impacto": 100,
        "simular_paa": 50,
        "simular_selic": 50,
        "emprego_caged": 800,
        "politica_impacto": 30,
    }

    daily_calls_1 = soma(traffic_m1.values())
    daily_revenue_1 = soma(
        api.endpoints[eid].price_per_call * n
        para eid, n in traffic_m1.items()
    )
    lines.append("  Chamadas/dia: {daily_calls_1:,}")
    lines.append("  Receita/dia:  R${daily_revenue_1:,.2f}")
    lines.append("  Receita/mes:  R${daily_revenue_1 * 30:,.2f}")

    tracker.register_daily_traffic(traffic_m1)
    // Simular 90 dias
    para cada _ em intervalo(89):
        tracker.register_daily_traffic(traffic_m1)

    lines.append("  Receita 90 dias: R${daily_revenue_1 * 90:,.2f}")
    lines.append("")

    // Reset para cenario 2
    api2 = TEIAAPI()
    tracker2 = RoyaltyTracker(api2)

    // === CENARIO 2: Crescimento (mes 4-6) ===
    lines.append("CENARIO 2: CRESCIMENTO (mes 4-6) -- 10 clientes ativos")
    lines.append("-" * 100)

    traffic_m4 = {k: v * 5 para k, v in traffic_m1.items()} // 5x trafego

    daily_calls_2 = soma(traffic_m4.values())
    daily_revenue_2 = soma(
        api2.endpoints[eid].price_per_call * n
        para eid, n in traffic_m4.items()
    )
    lines.append("  Chamadas/dia: {daily_calls_2:,}")
    lines.append("  Receita/dia:  R${daily_revenue_2:,.2f}")
    lines.append("  Receita/mes:  R${daily_revenue_2 * 30:,.2f}")

    para cada _ em intervalo(90):
        tracker2.register_daily_traffic(traffic_m4)

    lines.append("  Receita 90 dias: R${daily_revenue_2 * 90:,.2f}")
    lines.append("")

    // Reset para cenario 3
    api3 = TEIAAPI()
    tracker3 = RoyaltyTracker(api3)

    // === CENARIO 3: Escala (mes 7-12) ===
    lines.append("CENARIO 3: ESCALA (mes 7-12) -- 50 clientes + API publica")
    lines.append("-" * 100)

    traffic_m7 = {k: v * 20 para k, v in traffic_m1.items()} // 20x trafego

    daily_calls_3 = soma(traffic_m7.values())
    daily_revenue_3 = soma(
        api3.endpoints[eid].price_per_call * n
        para eid, n in traffic_m7.items()
    )
    lines.append("  Chamadas/dia: {daily_calls_3:,}")
    lines.append("  Receita/dia:  R${daily_revenue_3:,.2f}")
    lines.append("  Receita/mes:  R${daily_revenue_3 * 30:,.2f}")

    para cada _ em intervalo(180):
        tracker3.register_daily_traffic(traffic_m7)

    lines.append("  Receita 180 dias: R${daily_revenue_3 * 180:,.2f}")
    lines.append("")

    // === TABELA COMPARATIVA ===
    lines.append("-" * 100)
    lines.append("COMPARATIVO DE CENARIOS")
    lines.append("-" * 100)
    lines.append("{'CENARIO':<30} {'CALLS/DIA':>12} {'R$/DIA':>12} {'R$/MES':>14} {'R$/ANO':>16}")
    lines.append("-" * 100)
    lines.append("{'Lancamento (mes 1-3)':<30} {daily_calls_1:>12,} R${daily_revenue_1:>10,.2f} R${daily_revenue_1*30:>12,.0f} R${daily_revenue_1*365:>14,.0f}")
    lines.append("{'Crescimento (mes 4-6)':<30} {daily_calls_2:>12,} R${daily_revenue_2:>10,.2f} R${daily_revenue_2*30:>12,.0f} R${daily_revenue_2*365:>14,.0f}")
    lines.append("{'Escala (mes 7-12)':<30} {daily_calls_3:>12,} R${daily_revenue_3:>10,.2f} R${daily_revenue_3*30:>12,.0f} R${daily_revenue_3*365:>14,.0f}")
    lines.append("")

    // === DISTRIBUICAO NO CENARIO ESCALA ===
    lines.append("-" * 100)
    lines.append("DISTRIBUICAO DE ROYALTIES NO CENARIO ESCALA (90 dias)")
    lines.append("-" * 100)
    lines.append("")
    lines.append(tracker3.earnings_report())
    lines.append("")

    // === DETALHE DA CADEIA ===
    lines.append("-" * 100)
    lines.append("")
    lines.append(tracker3.revenue_per_endpoint_detail())

    lines.append("")
    lines.append("=" * 100)
    lines.append("O MODELO CREATOR Economy DE DADOS:")
    lines.append("")
    lines.append("  Instagram paga criadores por VIEW.")
    lines.append("  TEIA paga contribuidores por CHAMADA.")
    lines.append("")
    lines.append("  Cada dado tem proveniencia rastreada.")
    lines.append("  Cada chamada gera micro-pagamento.")
    lines.append("  95% vai para a cadeia de contribuidores.")
    lines.append("  5% vai para o pool da Republica (LEI).")
    lines.append("")
    lines.append("  Quem coleta ganha mais que quem documenta.")
    lines.append("  Quem modela ganha mais que quem limpa.")
    lines.append("  Quem fact-checkou ganha proporcional ao risco assumido.")
    lines.append("  Quem mantem atualizado ganha para sempre (residual).")
    lines.append("")
    lines.append("  O dado nao e de ninguem. A INTELIGENCIA de cada um.")
    lines.append("=" * 100)

    retorne "\n".join(lines)


// ============================================================================
// 6. EXECUCAO
// ============================================================================

se __name__ == "__main__" entao:
    imprima(simulate_traffic())

```
