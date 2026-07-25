# OpenDualMode -- O Ideal Coletivo e o Executavel Agora

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_dual_mode.py`

**Descricao:** ========================================================
DOIS MODOS DE OPERACAO:
  MODO IDEAL (O DESTINO):
    Republica completa. Sem dinheiro. Sem propriedade. CC0.
    Trabalho = base 1.0 + impacto. Credito expira. Bem comum.
    Tudo gratis. Tudo aberto. Tudo modular.
  MODO EXECUTAVEL (O CAMINHO):
    Mundo real. Agora. Com dinheiro. Com mercado.
    TODA atividade humana e MERCADORIA.
    TRABALHO e um tipo de mercadoria.
    OpenERP processa. OpenBusinessModel distribui.
    Transicao gradual (OpenTransition 7 fases).
A DIFERENCA:
  No IDEAL, trabalho nao e mercadoria. E DEVER + IMPACTO.
  No EXECUTAVEL, trabalho e mercadoria. Tem preco. E negociado.
  O EXECUTAVEL trata o real. O IDEAL guia a direcao.
  Nenhum sem o outro. Os dois coexistem durante a transicao.
POR QUE TRATAR TRABALHO COMO MERCADORIA NO EXECUTAVEL:
  Porque no mundo REAL, agora, trabalho ja e mercadoria.
  Ignorar isso e fingir que o mundo nao existe.
  A Republica NAO finge. ENCARA a realidade.
  Trata trabalho como mercadoria AGORA.
  Transiciona para DEVER + IMPACTO depois.
  OpenTransition controla quando mudar.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenDualMode -- O Ideal Coletivo e o Executavel Agora
========================================================

DOIS MODOS DE OPERACAO:

  MODO IDEAL (O DESTINO):
    Republica completa. Sem dinheiro. Sem propriedade. CC0.
    Trabalho = base 1.0 + impacto. Credito expira. Bem comum.
    Tudo gratis. Tudo aberto. Tudo modular.

  MODO EXECUTAVEL (O CAMINHO):
    Mundo real. Agora. Com dinheiro. Com mercado.
    TODA atividade humana e MERCADORIA.
    TRABALHO e um tipo de mercadoria.
    OpenERP processa. OpenBusinessModel distribui.
    Transicao gradual (OpenTransition 7 fases).

A DIFERENCA:
  No IDEAL, trabalho nao e mercadoria. e DEVER + IMPACTO.
  No EXECUTAVEL, trabalho e mercadoria. Tem preco. e negociado.
  O EXECUTAVEL trata o real. O IDEAL guia a direcao.
  Nenhum sem o outro. Os dois coexistem durante a transicao.

POR QUE TRATAR TRABALHO COMO MERCADORIA NO EXECUTAVEL:
  Porque no mundo REAL, agora, trabalho ja e mercadoria.
  Ignorar isso e fingir que o mundo nao existe.
  A Republica nao finge. ENCARA a realidade.
  Trata trabalho como mercadoria AGORA.
  Transiciona para DEVER + IMPACTO depois.
  OpenTransition controla quando mudar.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime


// ============================================================================
// 1. MODO DE OPERACAO
// ============================================================================

classe OperatingMode herda de Enum:
    // Os dois modos da Republica.
    IDEAL = ("ideal_coletivo", "O destino: sem dinheiro, bem comum, CC0")
    EXECUTAVEL = ("executavel_agora", "O caminho: mercado real, mercadoria, dinheiro")


classe CommodityType herda de Enum:
    // Tipos de mercadoria no modo EXECUTAVEL.

    NO MODO EXECUTAVEL:
    Toda atividade humana que gera valor e MERCADORIA.
    Trabalho e um tipo. Mas nao o unico.
    // 
    LABOR = ("trabalho", "Trabalho humano (tempo + skill + esforco)")
    KNOWLEDGE = ("conhecimento", "Conhecimento/Skill (OpenSkills com valor)")
    PRODUCT = ("produto", "Produto fisico (OpenProduct/OpenIndustry)")
    SERVICE = ("servico", "Servico (saude, educacao, reparo)")
    CREATIVE = ("criativo", "Obra criativa (musica, arte, codigo)")
    DATA = ("dados", "Dados/Informacao (OpenDataStructure)")
    ATTENTION = ("atencao", "Atencao/Tempo (streaming, consumo)")
    SOCIAL = ("social", "Capital social (rede, confianca, reputacao)")


classe PricingModel herda de Enum:
    // Como precificar mercadoria no EXECUTAVEL.
    HOURLY = ("hora", "Por hora de trabalho")
    FIXED = ("fixo", "Preco fixo por entrega")
    VALUE_BASED = ("valor", "Baseado em valor entregue")
    IMPACT_BASED = ("impacto", "Baseado em impacto medido")
    MARKET = ("mercado", "Preco de mercado (durante transicao)")
    SLIDING = ("escala", "Escalsa social (paga conforme pode)")
    ZERO = ("zero", "Gratis (subsidio da Republica)")
    BARTER = ("troca", "Troca direta (sem dinheiro)")


// ============================================================================
// 2. MERCADORIA (commodity)
// ============================================================================

// decorador: @dataclass
classe Commodity:
    // Uma mercadoria no modo EXECUTAVEL.

    NO MODO IDEAL:
    - Nao existe mercadoria. Existe CONTRIBUTUICAO.
    - Trabalho = base 1.0 + impacto. Credito expira.
    - Sem preco. Sem negociacao.

    NO MODO EXECUTAVEL:
    - Tudo que gera valor e mercadoria.
    - Tem preco. e negociado. e transacionado.
    - OpenERP registra. OpenBusinessModel distribui.
    - Dinheiro existe (BRL/USD/etc). Credito coexiste.
    // 
    commodity_id: texto
    name: texto
    commodity_type: CommodityType
    seja description: texto = ""

    // Preco no EXECUTAVEL
    seja price_model: PricingModel = PricingModel.HOURLY
    seja price_brl: flutuante = 0.0 // preco em dinheiro (transicao)
    seja price_credit: flutuante = 0.0 // equivalente em credito Republica

    // No IDEAL
    seja ideal_equivalent: texto = ""  // como funciona sem dinheiro
    seja ideal_credit_per_hour: flutuante = 1.0 // credito base no modo ideal

    // Valor real
    seja market_value: flutuante = 0.0 // valor de mercado real
    seja production_cost: flutuante = 0.0 // custo de producao
    seja fair_price: flutuante = 0.0 // preco justo (sem exploracao)

    // Quem produz
    seja skill_required: texto = ""  // OpenSkills necessaria
    seja time_to_produce: flutuante = 0.0 // horas para produzir


// ============================================================================
// 3. CATÁLOGO DE MERCADORIAS
// ============================================================================

seja COMMODITIES: [Commodity] = [

    // === TRABALHO ===
    Commodity(
        "CMD-L01", "Hora de Programacao Rust", CommodityType.LABOR,
        "Desenvolvedor Rust desenvolve sistema.",
        price_model = PricingModel.HOURLY, price_brl=80.0, price_credit=1.0,
        ideal_equivalent = "Base 1.0/hora + impacto (log pessoas * ripple)",
        market_value = 100.0, production_cost=0.0, fair_price=80.0,
        skill_required = "programacao_rust", time_to_produce=1.0,
    ),
    Commodity(
        "CMD-L02", "Consulta Medica", CommodityType.LABOR,
        "Medico diagnostica e trata.",
        price_model = PricingModel.FIXED, price_brl=200.0, price_credit=1.0,
        ideal_equivalent = "Base 1.0/hora + impacto (vida salva peso maximo)",
        market_value = 350.0, fair_price=200.0,
        skill_required = "medicina_diagnostico", time_to_produce=0.5,
    ),
    Commodity(
        "CMD-L03", "Aula Universitaria", CommodityType.LABOR,
        "Professor ensina na OpenUniversity.",
        price_model = PricingModel.HOURLY, price_brl=60.0, price_credit=1.0,
        ideal_equivalent = "Base 1.0/hora + impacto (alunos * ripple)",
        market_value = 100.0, fair_price=60.0,
        skill_required = "doutorado", time_to_produce=1.0,
    ),
    Commodity(
        "CMD-L04", "Hora de Construcao", CommodityType.LABOR,
        "Pedreiro/eletricista/encanador trabalha.",
        price_model = PricingModel.HOURLY, price_brl=40.0, price_credit=1.0,
        ideal_equivalent = "Base 1.0/hora + impacto (obra * utilidade)",
        market_value = 50.0, fair_price=40.0,
        skill_required = "alvenaria", time_to_produce=1.0,
    ),
    Commodity(
        "CMD-L05", "Hora de Cozinha", CommodityType.LABOR,
        "Cozinheiro prepara alimentos.",
        price_model = PricingModel.HOURLY, price_brl=30.0, price_credit=1.0,
        ideal_equivalent = "Base 1.0/hora + impacto (pessoas alimentadas)",
        market_value = 40.0, fair_price=30.0,
        skill_required = "culinaria", time_to_produce=1.0,
    ),

    // === CONHECIMENTO ===
    Commodity(
        "CMD-K01", "Curso OpenUniversity", CommodityType.KNOWLEDGE,
        "Curso completo (ex: Medicina 6 anos).",
        price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,
        ideal_equivalent = "Gratis. Conhecimento e bem comum. CC0.",
        market_value = 50000.0, fair_price=0.0,
        skill_required = "doutorado", time_to_produce=2000.0,
    ),
    Commodity(
        "CMD-K02", "Certificacao OpenSkills", CommodityType.KNOWLEDGE,
        "Validacao de skill pelo sistema.",
        price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,
        ideal_equivalent = "Gratis. Sistema comprova. Sem papel.",
        market_value = 500.0, fair_price=0.0,
    ),

    // === PRODUTO ===
    Commodity(
        "CMD-P01", "OpenPhone", CommodityType.PRODUCT,
        "Smartphone RISC-V modular.",
        price_model = PricingModel.MARKET, price_brl=0.0, price_credit=0.0,
        ideal_equivalent = "Gratis. FabLab fabrica. CC0.",
        market_value = 2000.0, production_cost=300.0, fair_price=0.0,
    ),
    Commodity(
        "CMD-P02", "OpenShirt", CommodityType.PRODUCT,
        "Camiseta algodao organico.",
        price_model = PricingModel.MARKET, price_brl=0.0, price_credit=0.0,
        ideal_equivalent = "Gratis. Costureira base 1.0 + FabLab.",
        market_value = 50.0, production_cost=15.0, fair_price=0.0,
    ),
    Commodity(
        "CMD-P03", "Cesta de Alimentos", CommodityType.PRODUCT,
        "Alimentos da horta comunitaria.",
        price_model = PricingModel.MARKET, price_brl=0.0, price_credit=0.0,
        ideal_equivalent = "Gratis. OpenAgrarian. CC0.",
        market_value = 100.0, production_cost=20.0, fair_price=0.0,
    ),

    // === SERVICO ===
    Commodity(
        "CMD-S01", "Tratamento OpenHealth", CommodityType.SERVICE,
        "Consulta + exames + tratamento.",
        price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,
        ideal_equivalent = "Gratis. Saude e direito. Sirio-Libanes.",
        market_value = 500.0, fair_price=0.0,
    ),
    Commodity(
        "CMD-S02", "Reparo OpenRepair", CommodityType.SERVICE,
        "Conserto de equipamento.",
        price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,
        ideal_equivalent = "Gratis. Tecnico base 1.0. Nada se joga fora.",
        market_value = 80.0, fair_price=0.0,
    ),

    // === CRIATIVO ===
    Commodity(
        "CMD-C01", "Musica (OpenMusic)", CommodityType.CREATIVE,
        "Musico cria e distribui musica.",
        price_model = PricingModel.ZERO, price_brl=0.0, price_credit=1.0,
        ideal_equivalent = "Base 1.0/hora criar + impacto (ouvintes). CC0.",
        market_value = 2000.0, fair_price=0.0,
    ),
    Commodity(
        "CMD-C02", "Software (codigo)", CommodityType.CREATIVE,
        "Programador cria sistema/modulo.",
        price_model = PricingModel.ZERO, price_brl=0.0, price_credit=1.0,
        ideal_equivalent = "Base 1.0/hora + impacto (usuarios * ripple). CC0.",
        market_value = 50000.0, fair_price=0.0,
    ),

    // === ATENCAO ===
    Commodity(
        "CMD-A01", "Stream OpenTV", CommodityType.ATTENTION,
        "Cidadao assiste programacao.",
        price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,
        ideal_equivalent = "Gratis. Sem algoritmo de viciacao. Sem ads.",
        market_value = 20.0, fair_price=0.0,
    ),
]


// ============================================================================
// 4. TRANSACAO
// ============================================================================

// decorador: @dataclass
classe Transaction:
    // Uma transacao no modo EXECUTAVEL ou IDEAL.
    transaction_id: texto
    from_citizen: texto
    to_citizen: texto
    commodity: texto
    mode: OperatingMode

    // EXECUTAVEL
    seja amount_brl: flutuante = 0.0
    seja amount_credit: flutuante = 0.0

    // IDEAL
    seja hours_worked: flutuante = 0.0
    seja impact_score: flutuante = 0.0

    seja date: texto = ""


// ============================================================================
// 5. MOTOR DUAL
// ============================================================================

classe DualModeEngine:
    // Motor que opera nos dois modos simultaneamente.

    COMO FUNCIONA:

    MODO EXECUTAVEL (agora):
    - Trabalho e MERCADORIA. Tem preco. BRL/USD.
    - OpenERP registra transacoes.
    - OpenBusinessModel distribui (competicao -> premio -> ONG).
    - Mercadoria e negociada. Mercado existe.
    - Dinheiro existe. Bancos existem (mas OpenCredit coexiste).
    - TRABALHO = mercadoria com preco.

    MODO IDEAL (destino):
    - Trabalho nao e mercadoria. e DEVER + IMPACTO.
    - Sem dinheiro. Sem mercado. Sem preco.
    - Credito base 1.0 + impacto (log pessoas * ripple).
    - Credito EXPIRA. Nao acumula.
    - Tudo CC0. Tudo bem comum.
    - TRABALHO = contribuicao, nao mercadoria.

    TRANSICAO CONTROLADA POR OpenTransition:
    - Fase 0-2: quase tudo EXECUTAVEL (mercado, dinheiro)
    - Fase 3-4: misto (dinheiro + credito coexistem)
    - Fase 5-6: quase tudo IDEAL (credito, bem comum)
    - Fase 7: Republica completa (ZERO dinheiro)

    O QUE O MODO EXECUTAVEL FAZ QUE O IDEAL nao:
    - Cobra dinheiro (BRL/USD/EUR)
    - Trata trabalho como mercadoria com preco
    - Usa OpenERP para fiscal/contabil
    - Paga impostos (durante transicao)
    - Negocia salario/valor
    - Tem mercado (oferta/procura)

    O QUE O MODO IDEAL FAZ QUE O EXECUTAVEL nao:
    - Trabalho = base 1.0 (sem negociacao)
    - Sem dinheiro (credito expira)
    - Sem impostos (trabalho substitui)
    - Sem mercado (bem comum)
    - Sem salario (credito de acesso)
    - Impacto = log(pessoas) * ripple

    COEXISTENCIA:
    Durante a transicao, os dois modos operam AO MESMO TEMPO.
    Uma consulta medica pode ser:
    - EXECUTAVEL: R$ 200 (quem tem dinheiro paga)
    - IDEAL: credito base 1.0 (quem e da Republica usa credito)
    O SISTEMA ACEITA OS DOIS. Simultaneamente.
    // 

    funcao __init__(self, current_phase: inteiro = 0):
        self.commodities: {texto: Commodity} = {
            c.commodity_id: c para c em COMMODITIES
        }
        self.transactions: [Transaction] = []
        self.current_phase = current_phase // OpenTransition phase 0-6
        self.mode_mix = self._calculate_mode_mix(current_phase)

    funcao _calculate_mode_mix(self, phase: inteiro) -> {texto: flutuante}:
        // Calcula mix de modos baseado na fase da transicao.
        // Fase 0-1: 90% executavel, 10% ideal
        // Fase 2-3: 60% executavel, 40% ideal
        // Fase 4-5: 30% executavel, 70% ideal
        // Fase 6+: 5% executavel, 95% ideal
        se phase <= 1 entao:
            retorne {"executavel": 0.90, "ideal": 0.10}
        senao se phase <= 3 entao:
            retorne {"executavel": 0.60, "ideal": 0.40}
        senao se phase <= 5 entao:
            retorne {"executavel": 0.30, "ideal": 0.70}
        senao:
            retorne {"executavel": 0.05, "ideal": 0.95}

    funcao current_mode(self) -> OperatingMode:
        // Modo predominante atual.
        se self.mode_mix["ideal"] > 0.5 entao:
            retorne OperatingMode.IDEAL
        retorne OperatingMode.EXECUTAVEL

    funcao price_commodity(self, commodity_id: texto) -> {texto: qualquer}:
        // Precifica mercadoria em ambos os modos.
        c = self.commodities.get(commodity_id)
        se nao c entao:
            retorne {"error": "Mercadoria nao encontrada"}

        retorne {
            "mercadoria": c.name,
            "tipo": c.commodity_type.value[0],
            "MODELO_EXECUTAVEL": {
                c.price_brl > 0 ? "preco_brl": "R$ {c.price_brl:.2f}" : "ZERO",
                "modelo": c.price_model.value[0],
                "valor_mercado": "R$ {c.market_value:.2f}",
                "preco_justo": "R$ {c.fair_price:.2f}",
                "negociavel": verdadeiro,
                "moeda": "BRL/USD/EUR (durante transicao)",
            },
            "MODELO_IDEAL": {
                "preco": "ZERO (sem dinheiro)",
                "credito": "{c.ideal_credit_per_hour:.1f}/hora base",
                "equivalente": c.ideal_equivalent,
                "negociavel": falso,
                "moeda": "OpenCredit (expira, nao acumula)",
            },
            "fase_atual": self.current_phase,
            "modo_predominante": self.current_mode().value[0],
            "message": (
                "{c.name}: EXECUTAVEL = "
                "{'R$ ' + str(c.price_brl) if c.price_brl > 0 else 'ZERO'}. "
                "IDEAL = credito base {c.ideal_credit_per_hour:.1f}/hora. "
                "Mix atual: {self.mode_mix['executavel']:.0%} executavel / "
                "{self.mode_mix['ideal']:.0%} ideal."
            ),
        }

    funcao transact(self, from_citizen: texto, to_citizen: texto,
                 commodity_id: texto, hours: flutuante = 1.0,
                 seja mode: OperatingMode = nulo,
                 seja amount_brl: flutuante = nulo
                 ) -> {texto: qualquer}:
        // Registra transacao em qualquer modo.
        c = self.commodities.get(commodity_id)
        se nao c entao:
            retorne {"error": "Mercadoria nao encontrada"}

        se mode e nulo entao:
            mode = self.current_mode()

        tid = hashlib.md5(
            "{from_citizen}{to_citizen}{commodity_id}{datetime.now()}".encode()
        ).hexdigest()[:8]

        se mode == OperatingMode.EXECUTAVEL entao:
            brl = amount_brl is nao nulo ? amount_brl : c.price_brl * hours
            credit = c.ideal_credit_per_hour * hours // credito tambem conta
            txn = Transaction(
                transaction_id = tid, from_citizen=from_citizen,
                to_citizen = to_citizen, commodity=c.name,
                mode = mode, amount_brl=brl, amount_credit=credit,
                hours_worked = hours, date=datetime.now().isoformat(),
            )
        senao:
            // IDEAL: sem dinheiro. So credito + impacto.
            impact = hours * (1 + tamanho(c.name) % 5) // simplificado
            txn = Transaction(
                transaction_id = tid, from_citizen=from_citizen,
                to_citizen = to_citizen, commodity=c.name,
                mode = mode, amount_brl=0.0,
                amount_credit = c.ideal_credit_per_hour * hours,
                hours_worked = hours, impact_score=impact,
                date = datetime.now().isoformat(),
            )

        self.transactions.append(txn)

        retorne {
            "transaction_id": tid,
            "mode": mode.value[0],
            "from": from_citizen,
            "to": to_citizen,
            "mercadoria": c.name,
            "horas": hours,
            "executavel": "R$ {txn.amount_brl:.2f}",
            "ideal": "{txn.amount_credit:.1f} credito + impacto {txn.impact_score:.1f}",
            "message": (
                "Transacao {tid}: {from_citizen} -> {to_citizen}. "
                "{c.name}. {hours:.0f}h. "
                "{'PAGOU R$ ' + str(txn.amount_brl) if txn.amount_brl > 0 else 'ZERO dinheiro'}. "
                "Credito: {txn.amount_credit:.1f}."
            ),
        }

    funcao labor_as_commodity_report(self) -> {texto: qualquer}:
        // Relatorio: trabalho como mercadoria nos dois modos.
        retorne {
            "modo_executavel": {
                "trabalho_e": "MERCADORIA com preco",
                "precificacao": "Por hora / fixo / valor / mercado",
                "exemplos": {
                    "programador_rust": "R$ 80/h (mercado R$ 100/h)",
                    "medico": "R$ 200/consulta (mercado R$ 350)",
                    "pedreiro": "R$ 40/h (mercado R$ 50/h)",
                    "cozinheiro": "R$ 30/h (mercado R$ 40/h)",
                    "professor": "R$ 60/h (mercado R$ 100/h)",
                },
                "negociacao": "Preco justo (sem exploracao). Fair price.",
                "impostos": "OpenERP calcula (durante transicao)",
                "open_erp": "Processa folha, fiscal, contabil",
                "open_business_model": "Competicao -> premio -> ONG -> impacto",
            },
            "modo_ideal": {
                "trabalho_e": "CONTRIBUICAO (base 1.0 + impacto)",
                "precificacao": "NENHUMA. Sem preco.",
                "credito": "1.0/hora base + log(pessoas) * ripple",
                "expira": "Credito NAO acumula. Expira.",
                "exemplos": {
                    "programador_rust": "1.0/h + impacto (modulos * usuarios)",
                    "medico": "1.0/h + impacto (vidas * peso maximo)",
                    "pedreiro": "1.0/h + impacto (obra * utilidade)",
                    "cozinheiro": "1.0/h + impacto (pessoas alimentadas)",
                    "professor": "1.0/h + impacto (alunos * ripple)",
                },
                "negociacao": "NENHUMA. Base 1.0 para todos.",
                "impostos": "ABOLIDOS. Trabalho substitui.",
            },
            "transicao": (
                "Fase atual: {self.current_phase}. "
                "Mix: {self.mode_mix['executavel']:.0%} executavel / "
                "{self.mode_mix['ideal']:.0%} ideal. "
                "Conforme avanca, executavel diminui e ideal aumenta."
            ),
        }

    funcao advance_phase(self) -> {texto: qualquer}:
        // Avanca uma fase na transicao.
        se self.current_phase < 6 entao:
            self.current_phase += 1
            self.mode_mix = self._calculate_mode_mix(self.current_phase)

        retorne {
            "new_phase": self.current_phase,
            "new_mix": self.mode_mix,
            "mode": self.current_mode().value[0],
            "message": (
                "Transicao avancou para fase {self.current_phase}. "
                "Mix: {self.mode_mix['executavel']:.0%} executavel / "
                "{self.mode_mix['ideal']:.0%} ideal. "
                "Modo predominante: {self.current_mode().value[0]}."
            ),
        }

    funcao stats(self) -> {texto: qualquer}:
        exec_txns = soma(1 para t em self.transactions
                        if t.mode == OperatingMode.EXECUTAVEL)
        ideal_txns = soma(1 para t em self.transactions
                         if t.mode == OperatingMode.IDEAL)
        retorne {
            "fase_transicao": self.current_phase,
            "modo_predominante": self.current_mode().value[0],
            "mix_executavel": "{self.mode_mix['executavel']:.0%}",
            "mix_ideal": "{self.mode_mix['ideal']:.0%}",
            "mercadorias_catalogadas": tamanho(self.commodities),
            "transacoes_executavel": exec_txns,
            "transacoes_ideal": ideal_txns,
            "principio": "O Ideal guia. O Executavel opera. Os dois coexistem.",
        }


// ============================================================================
// 6. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = DualModeEngine(current_phase=0)

    imprima("=" * 80)
    imprima("  OPENDUALMODE -- O IDEAL COLETIVO E O EXECUTAVEL AGORA")
    imprima("  Toda atividade humana = MERCADORIA. Trabalho = tipo de mercadoria.")
    imprima("=" * 80)

    // === 1. OS DOIS MODOS ===
    imprima("\n\n  === 1. OS DOIS MODOS ===\n")
    imprima("  MODO IDEAL (destino):")
    imprima("    Sem dinheiro. Sem propriedade. CC0.")
    imprima("    Trabalho = base 1.0 + impacto. Credito expira.")
    imprima("    Tudo gratis. Tudo bem comum.")
    imprima("")
    imprima("  MODO EXECUTAVEL (agora):")
    imprima("    Dinheiro existe. Mercado existe.")
    imprima("    Toda atividade = MERCADORIA. Trabalho = tipo de mercadoria.")
    imprima("    OpenERP processa. OpenBusinessModel distribui.")
    imprima("    Preco justo (sem exploracao). Fair price.")

    // === 2. TRABALHO COMO MERCADORIA ===
    imprima("\n\n  === 2. TRABALHO COMO MERCADORIA (EXECUTAVEL) ===\n")
    report = engine.labor_as_commodity_report()
    imprima("  EXECUTAVEL: {report['modo_executavel']['trabalho_e']}")
    para cada (job, price) em report["modo_executavel"]["exemplos"].items():
        imprima("    {job:<25} {price}")
    imprima("\n  IDEAL: {report['modo_ideal']['trabalho_e']}")
    para cada (job, price) em report["modo_ideal"]["exemplos"].items():
        imprima("    {job:<25} {price}")
    imprima("\n  {report['transicao']}")

    // === 3. PRECIFICACAO DUAL ===
    imprima("\n\n  === 3. PRECIFICACAO DUAL (mercadorias) ===\n")
    para cada cid em ["CMD-L01", "CMD-L02", "CMD-L04", "CMD-C02"]:
        p = engine.price_commodity(cid)
        imprima("\n  {p['mercadoria']} ({p['tipo']}):")
        imprima("    EXECUTAVEL: {p['MODELO_EXECUTAVEL']['preco_brl']} "
              "(mercado: {p['MODELO_EXECUTAVEL']['valor_mercado']})")
        imprima("    IDEAL: {p['MODELO_IDEAL']['credito']} "
              "({p['MODELO_IDEAL']['equivalente'][:50]})")

    // === 4. TRANSACOES EM AMBOS OS MODOS ===
    imprima("\n\n  === 4. TRANSACOES (ambos modos) ===\n")
    // Executavel: Joao paga Maria R$ 200 por consulta
    t1 = engine.transact("Joao", "Dra Maria", "CMD-L02",
                         hours = 0.5, mode=OperatingMode.EXECUTAVEL)
    imprima("  {t1['message']}")

    // Ideal: mesma consulta, sem dinheiro
    t2 = engine.transact("Joao", "Dra Maria", "CMD-L02",
                         hours = 0.5, mode=OperatingMode.IDEAL)
    imprima("  {t2['message']}")

    // Programador
    t3 = engine.transact("Empresa X", "Dev Pedro", "CMD-L01",
                         hours = 8, mode=OperatingMode.EXECUTAVEL)
    imprima("  {t3['message']}")

    // === 5. AVANCAR FASES ===
    imprima("\n\n  === 5. AVANCANDO TRANSICAO ===\n")
    para cada _ em intervalo(4):
        r = engine.advance_phase()
        imprima("  Fase {r['new_phase']}: {r['mode']} "
              "(exec:{r['new_mix']['executavel']:.0%} / "
              "ideal:{r['new_mix']['ideal']:.0%})")

    // === 6. STATS ===
    imprima("\n\n  === 6. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    imprima("\n{'='*80}")
    imprima("  OpenDualMode: fase {s['fase_transicao']}, "
          "modo {s['modo_predominante']}.")
    imprima("  {s['principio']}")
    imprima("{'='*80}")

```
