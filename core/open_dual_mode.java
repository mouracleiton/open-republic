// OpenDualMode -- O Ideal Coletivo e o Executavel Agora -- gerado de Portugol++
public class OpendualmodeOIdealColetivoEOExecutavelAgora {

    // !/usr/bin/env python3
    //
    OpenDualMode -- O Ideal Coletivo && o Executavel Agora;
    ========================================================;
    DOIS MODOS DE OPERACAO:;
    MODO IDEAL (O DESTINO):;
        Republica completa. Sem dinheiro. Sem propriedade. CC0.;
        Trabalho = base 1.0 + impacto. Credito expira. Bem comum.;
        Tudo gratis. Tudo aberto. Tudo modular.;
    MODO EXECUTAVEL (O CAMINHO):;
        Mundo real. Agora. Com dinheiro. Com mercado.;
        TODA atividade humana && MERCADORIA.;
        TRABALHO && um tipo de mercadoria.;
        OpenERP processa. OpenBusinessModel distribui.;
        Transicao gradual (OpenTransition 7 fases).;
    A DIFERENCA:;
    No IDEAL, trabalho ! && mercadoria. && DEVER + IMPACTO.;
    No EXECUTAVEL, trabalho && mercadoria. Tem preco. && negociado.;
    O EXECUTAVEL trata o real. O IDEAL guia a direcao.;
    Nenhum sem o outro. Os dois coexistem durante a transicao.;
    POR QUE TRATAR TRABALHO COMO MERCADORIA NO EXECUTAVEL:;
    Porque no mundo REAL, agora, trabalho ja && mercadoria.;
    Ignorar isso && fingir que o mundo ! existe.;
    A Republica ! finge. ENCARA a realidade.;
    Trata trabalho como mercadoria AGORA.;
    Transiciona para DEVER + IMPACTO depois.;
    OpenTransition controla quando mudar.;
    Author: OpenRepublic Team;
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
    public static class OperatingMode {
        // Os dois modos da Republica.
        IDEAL = ("ideal_coletivo", "O destino: sem dinheiro, bem comum, CC0");
        EXECUTAVEL = ("executavel_agora", "O caminho: mercado real, mercadoria, dinheiro");
    public static class CommodityType {
        // Tipos de mercadoria no modo EXECUTAVEL.
        NO MODO EXECUTAVEL:;
        Toda atividade humana que gera valor && MERCADORIA.;
        Trabalho && um tipo. Mas ! o unico.;
        //
        LABOR = ("trabalho", "Trabalho humano (tempo + skill + esforco)");
        KNOWLEDGE = ("conhecimento", "Conhecimento/Skill (OpenSkills com valor)");
        PRODUCT = ("produto", "Produto fisico (OpenProduct/OpenIndustry)");
        SERVICE = ("servico", "Servico (saude, educacao, reparo)");
        CREATIVE = ("criativo", "Obra criativa (musica, arte, codigo)");
        DATA = ("dados", "Dados/Informacao (OpenDataStructure)");
        ATTENTION = ("atencao", "Atencao/Tempo (streaming, consumo)");
        SOCIAL = ("social", "Capital social (rede, confianca, reputacao)");
    public static class PricingModel {
        // Como precificar mercadoria no EXECUTAVEL.
        HOURLY = ("hora", "Por hora de trabalho");
        FIXED = ("fixo", "Preco fixo por entrega");
        VALUE_BASED = ("valor", "Baseado em valor entregue");
        IMPACT_BASED = ("impacto", "Baseado em impacto medido");
        MARKET = ("mercado", "Preco de mercado (durante transicao)");
        SLIDING = ("escala", "Escalsa social (paga conforme pode)");
        ZERO = ("zero", "Gratis (subsidio da Republica)");
        BARTER = ("troca", "Troca direta (sem dinheiro)");
    // ============================================================================
    // 2. MERCADORIA (commodity)
    // ============================================================================
    // decorador: @dataclass
    public static class Commodity {
        // Uma mercadoria no modo EXECUTAVEL.
        NO MODO IDEAL:;
        - Nao existe mercadoria. Existe CONTRIBUTUICAO.;
        - Trabalho = base 1.0 + impacto. Credito expira.;
        - Sem preco. Sem negociacao.;
        NO MODO EXECUTAVEL:;
        - Tudo que gera valor && mercadoria.;
        - Tem preco. && negociado. && transacionado.;
        - OpenERP registra. OpenBusinessModel distribui.;
        - Dinheiro existe (BRL/USD/etc). Credito coexiste.;
        //
        commodity_id: texto;
        name: texto;
        commodity_type: CommodityType;
        String description = "";
        // Preco no EXECUTAVEL
        PricingModel price_model = PricingModel.HOURLY;
        double price_brl = 0.0 // preco em dinheiro (transicao);
        double price_credit = 0.0 // equivalente em credito Republica;
        // No IDEAL
        String ideal_equivalent = ""  // como funciona sem dinheiro;
        double ideal_credit_per_hour = 1.0 // credito base no modo ideal;
        // Valor real
        double market_value = 0.0 // valor de mercado real;
        double production_cost = 0.0 // custo de producao;
        double fair_price = 0.0 // preco justo (sem exploracao);
        // Quem produz
        String skill_required = ""  // OpenSkills necessaria;
        double time_to_produce = 0.0 // horas para produzir;
    // ============================================================================
    // 3. CATÁLOGO DE MERCADORIAS
    // ============================================================================
    [Commodity] COMMODITIES = [;
        // === TRABALHO ===
        Commodity(;
            "CMD-L01", "Hora de Programacao Rust", CommodityType.LABOR,;
            "Desenvolvedor Rust desenvolve sistema.",;
            price_model = PricingModel.HOURLY, price_brl=80.0, price_credit=1.0,;
            ideal_equivalent = "Base 1.0/hora + impacto (log pessoas * ripple)",;
            market_value = 100.0, production_cost=0.0, fair_price=80.0,;
            skill_required = "programacao_rust", time_to_produce=1.0,;
        ),;
        Commodity(;
            "CMD-L02", "Consulta Medica", CommodityType.LABOR,;
            "Medico diagnostica && trata.",;
            price_model = PricingModel.FIXED, price_brl=200.0, price_credit=1.0,;
            ideal_equivalent = "Base 1.0/hora + impacto (vida salva peso maximo)",;
            market_value = 350.0, fair_price=200.0,;
            skill_required = "medicina_diagnostico", time_to_produce=0.5,;
        ),;
        Commodity(;
            "CMD-L03", "Aula Universitaria", CommodityType.LABOR,;
            "Professor ensina na OpenUniversity.",;
            price_model = PricingModel.HOURLY, price_brl=60.0, price_credit=1.0,;
            ideal_equivalent = "Base 1.0/hora + impacto (alunos * ripple)",;
            market_value = 100.0, fair_price=60.0,;
            skill_required = "doutorado", time_to_produce=1.0,;
        ),;
        Commodity(;
            "CMD-L04", "Hora de Construcao", CommodityType.LABOR,;
            "Pedreiro/eletricista/encanador trabalha.",;
            price_model = PricingModel.HOURLY, price_brl=40.0, price_credit=1.0,;
            ideal_equivalent = "Base 1.0/hora + impacto (obra * utilidade)",;
            market_value = 50.0, fair_price=40.0,;
            skill_required = "alvenaria", time_to_produce=1.0,;
        ),;
        Commodity(;
            "CMD-L05", "Hora de Cozinha", CommodityType.LABOR,;
            "Cozinheiro prepara alimentos.",;
            price_model = PricingModel.HOURLY, price_brl=30.0, price_credit=1.0,;
            ideal_equivalent = "Base 1.0/hora + impacto (pessoas alimentadas)",;
            market_value = 40.0, fair_price=30.0,;
            skill_required = "culinaria", time_to_produce=1.0,;
        ),;
        // === CONHECIMENTO ===
        Commodity(;
            "CMD-K01", "Curso OpenUniversity", CommodityType.KNOWLEDGE,;
            "Curso completo (ex: Medicina 6 anos).",;
            price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,;
            ideal_equivalent = "Gratis. Conhecimento && bem comum. CC0.",;
            market_value = 50000.0, fair_price=0.0,;
            skill_required = "doutorado", time_to_produce=2000.0,;
        ),;
        Commodity(;
            "CMD-K02", "Certificacao OpenSkills", CommodityType.KNOWLEDGE,;
            "Validacao de skill pelo sistema.",;
            price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,;
            ideal_equivalent = "Gratis. Sistema comprova. Sem papel.",;
            market_value = 500.0, fair_price=0.0,;
        ),;
        // === PRODUTO ===
        Commodity(;
            "CMD-P01", "OpenPhone", CommodityType.PRODUCT,;
            "Smartphone RISC-V modular.",;
            price_model = PricingModel.MARKET, price_brl=0.0, price_credit=0.0,;
            ideal_equivalent = "Gratis. FabLab fabrica. CC0.",;
            market_value = 2000.0, production_cost=300.0, fair_price=0.0,;
        ),;
        Commodity(;
            "CMD-P02", "OpenShirt", CommodityType.PRODUCT,;
            "Camiseta algodao organico.",;
            price_model = PricingModel.MARKET, price_brl=0.0, price_credit=0.0,;
            ideal_equivalent = "Gratis. Costureira base 1.0 + FabLab.",;
            market_value = 50.0, production_cost=15.0, fair_price=0.0,;
        ),;
        Commodity(;
            "CMD-P03", "Cesta de Alimentos", CommodityType.PRODUCT,;
            "Alimentos da horta comunitaria.",;
            price_model = PricingModel.MARKET, price_brl=0.0, price_credit=0.0,;
            ideal_equivalent = "Gratis. OpenAgrarian. CC0.",;
            market_value = 100.0, production_cost=20.0, fair_price=0.0,;
        ),;
        // === SERVICO ===
        Commodity(;
            "CMD-S01", "Tratamento OpenHealth", CommodityType.SERVICE,;
            "Consulta + exames + tratamento.",;
            price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,;
            ideal_equivalent = "Gratis. Saude && direito. Sirio-Libanes.",;
            market_value = 500.0, fair_price=0.0,;
        ),;
        Commodity(;
            "CMD-S02", "Reparo OpenRepair", CommodityType.SERVICE,;
            "Conserto de equipamento.",;
            price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,;
            ideal_equivalent = "Gratis. Tecnico base 1.0. Nada se joga fora.",;
            market_value = 80.0, fair_price=0.0,;
        ),;
        // === CRIATIVO ===
        Commodity(;
            "CMD-C01", "Musica (OpenMusic)", CommodityType.CREATIVE,;
            "Musico cria && distribui musica.",;
            price_model = PricingModel.ZERO, price_brl=0.0, price_credit=1.0,;
            ideal_equivalent = "Base 1.0/hora criar + impacto (ouvintes). CC0.",;
            market_value = 2000.0, fair_price=0.0,;
        ),;
        Commodity(;
            "CMD-C02", "Software (codigo)", CommodityType.CREATIVE,;
            "Programador cria sistema/modulo.",;
            price_model = PricingModel.ZERO, price_brl=0.0, price_credit=1.0,;
            ideal_equivalent = "Base 1.0/hora + impacto (usuarios * ripple). CC0.",;
            market_value = 50000.0, fair_price=0.0,;
        ),;
        // === ATENCAO ===
        Commodity(;
            "CMD-A01", "Stream OpenTV", CommodityType.ATTENTION,;
            "Cidadao assiste programacao.",;
            price_model = PricingModel.ZERO, price_brl=0.0, price_credit=0.0,;
            ideal_equivalent = "Gratis. Sem algoritmo de viciacao. Sem ads.",;
            market_value = 20.0, fair_price=0.0,;
        ),;
    ];
    // ============================================================================
    // 4. TRANSACAO
    // ============================================================================
    // decorador: @dataclass
    public static class Transaction {
        // Uma transacao no modo EXECUTAVEL ou IDEAL.
        transaction_id: texto;
        from_citizen: texto;
        to_citizen: texto;
        commodity: texto;
        mode: OperatingMode;
        // EXECUTAVEL
        double amount_brl = 0.0;
        double amount_credit = 0.0;
        // IDEAL
        double hours_worked = 0.0;
        double impact_score = 0.0;
        String date = "";
    // ============================================================================
    // 5. MOTOR DUAL
    // ============================================================================
    public static class DualModeEngine {
        // Motor que opera nos dois modos simultaneamente.
        COMO FUNCIONA:;
        MODO EXECUTAVEL (agora):;
        - Trabalho && MERCADORIA. Tem preco. BRL/USD.;
        - OpenERP registra transacoes.;
        - OpenBusinessModel distribui (competicao -> premio -> ONG).;
        - Mercadoria && negociada. Mercado existe.;
        - Dinheiro existe. Bancos existem (mas OpenCredit coexiste).;
        - TRABALHO = mercadoria com preco.;
        MODO IDEAL (destino):;
        - Trabalho ! && mercadoria. && DEVER + IMPACTO.;
        - Sem dinheiro. Sem mercado. Sem preco.;
        - Credito base 1.0 + impacto (log pessoas * ripple).;
        - Credito EXPIRA. Nao acumula.;
        - Tudo CC0. Tudo bem comum.;
        - TRABALHO = contribuicao, ! mercadoria.;
        TRANSICAO CONTROLADA POR OpenTransition:;
        - Fase 0-2: quase tudo EXECUTAVEL (mercado, dinheiro);
        - Fase 3-4: misto (dinheiro + credito coexistem);
        - Fase 5-6: quase tudo IDEAL (credito, bem comum);
        - Fase 7: Republica completa (ZERO dinheiro);
        O QUE O MODO EXECUTAVEL FAZ QUE O IDEAL !:;
        - Cobra dinheiro (BRL/USD/EUR);
        - Trata trabalho como mercadoria com preco;
        - Usa OpenERP para fiscal/contabil;
        - Paga impostos (durante transicao);
        - Negocia salario/valor;
        - Tem mercado (oferta/procura);
        O QUE O MODO IDEAL FAZ QUE O EXECUTAVEL !:;
        - Trabalho = base 1.0 (sem negociacao);
        - Sem dinheiro (credito expira);
        - Sem impostos (trabalho substitui);
        - Sem mercado (bem comum);
        - Sem salario (credito de acesso);
        - Impacto = log(pessoas) * ripple;
        COEXISTENCIA:;
        Durante a transicao, os dois modos operam AO MESMO TEMPO.;
        Uma consulta medica pode ser:;
        - EXECUTAVEL: R$ 200 (quem tem dinheiro paga);
        - IDEAL: credito base 1.0 (quem && da Republica usa credito);
        O SISTEMA ACEITA OS DOIS. Simultaneamente.;
        //
        public void __init__(self, current_phase: inteiro = 0) {
            self.commodities: {texto: Commodity} = {
                c.commodity_id: c para c em COMMODITIES;
            };
            self.transactions: [Transaction] = [];
            self.current_phase = current_phase // OpenTransition phase 0-6;
            self.mode_mix = self._calculate_mode_mix(current_phase);
        public {texto: flutuante} _calculate_mode_mix(self, phase: inteiro) {
            // Calcula mix de modos baseado na fase da transicao.
            // Fase 0-1: 90% executavel, 10% ideal
            // Fase 2-3: 60% executavel, 40% ideal
            // Fase 4-5: 30% executavel, 70% ideal
            // Fase 6+: 5% executavel, 95% ideal
            if (phase <= 1) {
                return {"executavel": 0.90, "ideal": 0.10};
            } else if (phase <= 3) {
                return {"executavel": 0.60, "ideal": 0.40};
            } else if (phase <= 5) {
                return {"executavel": 0.30, "ideal": 0.70};
            } else {
                return {"executavel": 0.05, "ideal": 0.95};
        public OperatingMode current_mode(self) {
            // Modo predominante atual.
            if (self.mode_mix["ideal"] > 0.5) {
                return OperatingMode.IDEAL;
            return OperatingMode.EXECUTAVEL;
        public {texto: qualquer} price_commodity(self, commodity_id: texto) {
            // Precifica mercadoria em ambos os modos.
            c = self.commodities.get(commodity_id);
            if (! c) {
                return {"error": "Mercadoria ! encontrada"};
            return {;
                "mercadoria": c.name,;
                "tipo": c.commodity_type.value[0],;
                "MODELO_EXECUTAVEL": {
                    c.price_brl > 0 ? "preco_brl": "R$ {c.price_brl:.2f}" : "ZERO",;
                    "modelo": c.price_model.value[0],;
                    "valor_mercado": "R$ {c.market_value:.2f}",;
                    "preco_justo": "R$ {c.fair_price:.2f}",;
                    "negociavel": true,;
                    "moeda": "BRL/USD/EUR (durante transicao)",;
                },;
                "MODELO_IDEAL": {
                    "preco": "ZERO (sem dinheiro)",;
                    "credito": "{c.ideal_credit_per_hour:.1f}/hora base",;
                    "equivalente": c.ideal_equivalent,;
                    "negociavel": false,;
                    "moeda": "OpenCredit (expira, ! acumula)",;
                },;
                "fase_atual": self.current_phase,;
                "modo_predominante": self.current_mode().value[0],;
                "message": (;
                    "{c.name}: EXECUTAVEL = ";
                    "{'R$ ' + str(c.price_brl) if c.price_brl > 0 else 'ZERO'}. ";
                    "IDEAL = credito base {c.ideal_credit_per_hour:.1f}/hora. ";
                    "Mix atual: {self.mode_mix['executavel']:.0%} executavel / ";
                    "{self.mode_mix['ideal']:.0%} ideal.";
                ),;
            };
        funcao transact(self, from_citizen: texto, to_citizen: texto,
                    commodity_id: texto, hours: flutuante = 1.0,;
                    OperatingMode mode = null,;
                    double amount_brl = null;
                    ) -> {texto: qualquer}:;
            // Registra transacao em qualquer modo.
            c = self.commodities.get(commodity_id);
            if (! c) {
                return {"error": "Mercadoria ! encontrada"};
            if (mode && null) {
                mode = self.current_mode();
            tid = hashlib.md5(;
                "{from_citizen}{to_citizen}{commodity_id}{datetime.now()}".encode();
            ).hexdigest()[:8];
            if (mode == OperatingMode.EXECUTAVEL) {
                brl = amount_brl is ! null ? amount_brl : c.price_brl * hours;
                credit = c.ideal_credit_per_hour * hours // credito tambem conta;
                txn = Transaction(;
                    transaction_id = tid, from_citizen=from_citizen,;
                    to_citizen = to_citizen, commodity=c.name,;
                    mode = mode, amount_brl=brl, amount_credit=credit,;
                    hours_worked = hours, date=datetime.now().isoformat(),;
                );
            } else {
                // IDEAL: sem dinheiro. So credito + impacto.
                impact = hours * (1 + tamanho(c.name) % 5) // simplificado;
                txn = Transaction(;
                    transaction_id = tid, from_citizen=from_citizen,;
                    to_citizen = to_citizen, commodity=c.name,;
                    mode = mode, amount_brl=0.0,;
                    amount_credit = c.ideal_credit_per_hour * hours,;
                    hours_worked = hours, impact_score=impact,;
                    date = datetime.now().isoformat(),;
                );
            self.transactions.append(txn);
            return {;
                "transaction_id": tid,;
                "mode": mode.value[0],;
                "from": from_citizen,;
                "to": to_citizen,;
                "mercadoria": c.name,;
                "horas": hours,;
                "executavel": "R$ {txn.amount_brl:.2f}",;
                "ideal": "{txn.amount_credit:.1f} credito + impacto {txn.impact_score:.1f}",;
                "message": (;
                    "Transacao {tid}: {from_citizen} -> {to_citizen}. ";
                    "{c.name}. {hours:.0f}h. ";
                    "{'PAGOU R$ ' + str(txn.amount_brl) if txn.amount_brl > 0 else 'ZERO dinheiro'}. ";
                    "Credito: {txn.amount_credit:.1f}.";
                ),;
            };
        public {texto: qualquer} labor_as_commodity_report(self) {
            // Relatorio: trabalho como mercadoria nos dois modos.
            return {;
                "modo_executavel": {
                    "trabalho_e": "MERCADORIA com preco",;
                    "precificacao": "Por hora / fixo / valor / mercado",;
                    "exemplos": {
                        "programador_rust": "R$ 80/h (mercado R$ 100/h)",;
                        "medico": "R$ 200/consulta (mercado R$ 350)",;
                        "pedreiro": "R$ 40/h (mercado R$ 50/h)",;
                        "cozinheiro": "R$ 30/h (mercado R$ 40/h)",;
                        "professor": "R$ 60/h (mercado R$ 100/h)",;
                    },;
                    "negociacao": "Preco justo (sem exploracao). Fair price.",;
                    "impostos": "OpenERP calcula (durante transicao)",;
                    "open_erp": "Processa folha, fiscal, contabil",;
                    "open_business_model": "Competicao -> premio -> ONG -> impacto",;
                },;
                "modo_ideal": {
                    "trabalho_e": "CONTRIBUICAO (base 1.0 + impacto)",;
                    "precificacao": "NENHUMA. Sem preco.",;
                    "credito": "1.0/hora base + log(pessoas) * ripple",;
                    "expira": "Credito NAO acumula. Expira.",;
                    "exemplos": {
                        "programador_rust": "1.0/h + impacto (modulos * usuarios)",;
                        "medico": "1.0/h + impacto (vidas * peso maximo)",;
                        "pedreiro": "1.0/h + impacto (obra * utilidade)",;
                        "cozinheiro": "1.0/h + impacto (pessoas alimentadas)",;
                        "professor": "1.0/h + impacto (alunos * ripple)",;
                    },;
                    "negociacao": "NENHUMA. Base 1.0 para todos.",;
                    "impostos": "ABOLIDOS. Trabalho substitui.",;
                },;
                "transicao": (;
                    "Fase atual: {self.current_phase}. ";
                    "Mix: {self.mode_mix['executavel']:.0%} executavel / ";
                    "{self.mode_mix['ideal']:.0%} ideal. ";
                    "Conforme avanca, executavel diminui && ideal aumenta.";
                ),;
            };
        public {texto: qualquer} advance_phase(self) {
            // Avanca uma fase na transicao.
            if (self.current_phase < 6) {
                self.current_phase += 1;
                self.mode_mix = self._calculate_mode_mix(self.current_phase);
            return {;
                "new_phase": self.current_phase,;
                "new_mix": self.mode_mix,;
                "mode": self.current_mode().value[0],;
                "message": (;
                    "Transicao avancou para fase {self.current_phase}. ";
                    "Mix: {self.mode_mix['executavel']:.0%} executavel / ";
                    "{self.mode_mix['ideal']:.0%} ideal. ";
                    "Modo predominante: {self.current_mode().value[0]}.";
                ),;
            };
        public {texto: qualquer} stats(self) {
            exec_txns = soma(1 para t em self.transactions;
                            if t.mode == OperatingMode.EXECUTAVEL);
            ideal_txns = soma(1 para t em self.transactions;
                            if t.mode == OperatingMode.IDEAL);
            return {;
                "fase_transicao": self.current_phase,;
                "modo_predominante": self.current_mode().value[0],;
                "mix_executavel": "{self.mode_mix['executavel']:.0%}",;
                "mix_ideal": "{self.mode_mix['ideal']:.0%}",;
                "mercadorias_catalogadas": tamanho(self.commodities),;
                "transacoes_executavel": exec_txns,;
                "transacoes_ideal": ideal_txns,;
                "principio": "O Ideal guia. O Executavel opera. Os dois coexistem.",;
            };
    // ============================================================================
    // 6. MAIN
    // ============================================================================
    if (__name__ == "__main__") {
        engine = DualModeEngine(current_phase=0);
        System.out.println("=" * 80);
        System.out.println("  OPENDUALMODE -- O IDEAL COLETIVO E O EXECUTAVEL AGORA");
        System.out.println("  Toda atividade humana = MERCADORIA. Trabalho = tipo de mercadoria.");
        System.out.println("=" * 80);
        // === 1. OS DOIS MODOS ===
        System.out.println("\n\n  === 1. OS DOIS MODOS ===\n");
        System.out.println("  MODO IDEAL (destino):");
        System.out.println("    Sem dinheiro. Sem propriedade. CC0.");
        System.out.println("    Trabalho = base 1.0 + impacto. Credito expira.");
        System.out.println("    Tudo gratis. Tudo bem comum.");
        System.out.println("");
        System.out.println("  MODO EXECUTAVEL (agora):");
        System.out.println("    Dinheiro existe. Mercado existe.");
        System.out.println("    Toda atividade = MERCADORIA. Trabalho = tipo de mercadoria.");
        System.out.println("    OpenERP processa. OpenBusinessModel distribui.");
        System.out.println("    Preco justo (sem exploracao). Fair price.");
        // === 2. TRABALHO COMO MERCADORIA ===
        System.out.println("\n\n  === 2. TRABALHO COMO MERCADORIA (EXECUTAVEL) ===\n");
        report = engine.labor_as_commodity_report();
        System.out.println("  EXECUTAVEL: {report['modo_executavel']['trabalho_e']}");
        /* para cada (job, price) em report["modo_executavel"]["exemplos"].items(): */
            System.out.println("    {job:<25} {price}");
        System.out.println("\n  IDEAL: {report['modo_ideal']['trabalho_e']}");
        /* para cada (job, price) em report["modo_ideal"]["exemplos"].items(): */
            System.out.println("    {job:<25} {price}");
        System.out.println("\n  {report['transicao']}");
        // === 3. PRECIFICACAO DUAL ===
        System.out.println("\n\n  === 3. PRECIFICACAO DUAL (mercadorias) ===\n");
        /* TODO: for-each Java para cid em ["CMD-L01", "CMD-L02", "CMD-L04", "CMD-C02"] */
            p = engine.price_commodity(cid);
            System.out.println("\n  {p['mercadoria']} ({p['tipo']}):");
            System.out.println("    EXECUTAVEL: {p['MODELO_EXECUTAVEL']['preco_brl']} ";
                "(mercado: {p['MODELO_EXECUTAVEL']['valor_mercado']})");
            System.out.println("    IDEAL: {p['MODELO_IDEAL']['credito']} ";
                "({p['MODELO_IDEAL']['equivalente'][:50]})");
        // === 4. TRANSACOES EM AMBOS OS MODOS ===
        System.out.println("\n\n  === 4. TRANSACOES (ambos modos) ===\n");
        // Executavel: Joao paga Maria R$ 200 por consulta
        t1 = engine.transact("Joao", "Dra Maria", "CMD-L02",;
                            hours = 0.5, mode=OperatingMode.EXECUTAVEL);
        System.out.println("  {t1['message']}");
        // Ideal: mesma consulta, sem dinheiro
        t2 = engine.transact("Joao", "Dra Maria", "CMD-L02",;
                            hours = 0.5, mode=OperatingMode.IDEAL);
        System.out.println("  {t2['message']}");
        // Programador
        t3 = engine.transact("Empresa X", "Dev Pedro", "CMD-L01",;
                            hours = 8, mode=OperatingMode.EXECUTAVEL);
        System.out.println("  {t3['message']}");
        // === 5. AVANCAR FASES ===
        System.out.println("\n\n  === 5. AVANCANDO TRANSICAO ===\n");
        /* TODO: for-each Java para _ em intervalo(4) */
            r = engine.advance_phase();
            System.out.println("  Fase {r['new_phase']}: {r['mode']} ";
                "(exec:{r['new_mix']['executavel']:.0%} / ";
                "ideal:{r['new_mix']['ideal']:.0%})");
        // === 6. STATS ===
        System.out.println("\n\n  === 6. ESTATISTICAS ===\n");
        s = engine.stats();
        /* para cada (k, v) em s.items(): */
            System.out.println("  {k:<30} {v}");
        System.out.println("\n{'='*80}");
        System.out.println("  OpenDualMode: fase {s['fase_transicao']}, ";
            "modo {s['modo_predominante']}.");
        System.out.println("  {s['principio']}");
        System.out.println("{'='*80}");
}
