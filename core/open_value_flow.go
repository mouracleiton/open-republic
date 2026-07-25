// OpenValueFlow -- Eliminar Empresa e Banco da Cadeia de Valor -- gerado de Portugol++
package openvalueflow_eliminar_empresa_e_banco_da_cadeia_de_valor

import "fmt"

// !/usr/bin/env python3
//
OpenValueFlow -- Eliminar Empresa && Banco da Cadeia de Valor
================================================================
O PROBLEMA:
Trabalhador produz R$ 100 de valor.
Empresa fica com R$ 60 (excedente predatorio).
Banco fica com R$ 20 (juros, taxas, spread).
Trabalhador recebe R$ 20 (20% do que produziu).
DOIS parasitas na cadeia: empresa && banco.
Resolver um sem o outro ! basta.
Tem que eliminar OS DOIS.
A SOLUCAO:
1. EMPRESA -> COOPERATIVA (sem dono, sem lucro)
    Os 5% ja resolvem (OpenFairSurplus). Nao ha dono.
    Mas a "empresa" ainda existe como entidade. Vira COLETIVO.
2. BANCO -> OPCREDIT (sem juros, sem taxa, sem spread)
    Banco cobra em 3 lugares:
    - Taxa de transacao (R$ 3,50 por PIX/cartao? "Gratis" mas embutido)
    - Juros (spread bancario: 730% a.a. cartao, 300% cheque especial)
    - Spread de cambio (compra/d vende, fica com diferenca)
    OpenCredit elimina OS TRES.
3. RESULTADO:
    Trabalhador produz R$ 100.
    Coletivo recebe R$ 100 (sem dono).
    5% volta pra pool (R$ 5).
    Transacao: ZERO taxa (OpenCredit, sem banco).
    Trabalhador recebe: R$ 95 + pool de R$ 5 = R$ 100.
    100% do valor fica com quem trabalha.
    ZERO para parasita. ZERO para banco. ZERO para dono.
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa datetime de datetime
// ============================================================================
// 1. CADEIA DE VALOR
// ============================================================================
type ValueSink int
const (
    // Onde o valor e EXTRAIDO do trabalhador.
    WORKER = ("trabalhador", "Quem produz o valor real")
    COMPANY_PROFIT = ("lucro_empresa", "Dono da empresa extrai")
    COMPANY_OPERATIONAL = ("operacional", "Custo real de operar")
    BANK_INTEREST = ("juros_banco", "Banco cobra juros sobre tudo")
    BANK_TRANSACTION = ("taxa_transacao", "Banco cobra por movimentar dinheiro")
    BANK_SPREAD = ("spread_bancario", "Banco cobra diferenca compra/venda")
    TAX = ("imposto", "Governo cobra imposto")
    INTERMEDIARY = ("intermediario", "Plataforma/atravessador cobra pedagio")
type FlowMode int
const (
    // Modo de fluxo de valor.
    CAPITALISM = "capitalismo_atual"  // empresa + banco + governo extrai
    REPUBLIC_EXECUTAVEL = "republica_executavel"  // 5% justo, sem banco
    REPUBLIC_IDEAL = "republica_ideal"  // base 1.0, sem dinheiro, sem extracao
// ============================================================================
// 2. ANALISE DA CADEIA
// ============================================================================
// decorador: @dataclass
type ValueChainAnalysis struct {
    // Analisa para onde vai cada R$ 1 produzido pelo trabalhador.
    analysis_id: texto
    scenario: texto
    mode: FlowMode
    // Valor produzido
    total_value := 100.0 // valor total produzido // float64
    // Para onde vai (em R$)
    worker_receives := 0.0 // float64
    company_profit := 0.0 // lucro do dono // float64
    company_operational := 0.0 // custo real de operar // float64
    bank_interest := 0.0 // juros // float64
    bank_transaction := 0.0 // taxas de transacao // float64
    bank_spread := 0.0 // spread cambial // float64
    tax := 0.0 // impostos // float64
    intermediary := 0.0 // intermediarios // float64
    // Pool coletivo (Republica)
    collective_pool := 0.0 // 5% que volta // float64
    // decorador: @property
    func worker_pct(self) float64 {
        return self.worker_receives / self.total_value * 100
    // decorador: @property
    func extracted_pct(self) float64 {
        // Quanto foi EXTRAIDO do trabalhador.
        return (self.company_profit + self.bank_interest
                + self.bank_transaction + self.bank_spread
                + self.intermediary) / self.total_value * 100
// ============================================================================
// 3. MOTOR DE FLUXO DE VALOR
// ============================================================================
type ValueFlowEngine struct {
    // Motor que rastreia e elimina TODA extracao de valor.
    O PROBLEMA EM 3 CAMADAS:
    CAMADA 1: EMPRESA (dono)
    Trabalhador produz R$ 100.
    Dono fica com R$ 60 (excedente).
    -> RESOLVIDO: OpenFairSurplus (5% pool, sem dono).
    CAMADA 2: BANCO (3 formas de sugar)
    a) Taxa de transacao: R$ 3,50 por cartao/PIX "gratis".
        Custa R$ 0,01 para processar. Cobra R$ 3,50.
        Em 100 transacoes/mes = R$ 350 extraido.
    b) Juros: spread bancario brasileiro = maior do mundo.
        Cartao: 730% a.a. Cheque especial: 300%.
        Empresa precisa capital de giro? Paga juros ao banco.
        Quem paga? O trabalhador (preco embutido).
    c) Spread de cambio: banco compra dolar a R$ 4, vende a R$ 5.
        Diferenca de R$ 1 vai pro banco. Zero servico.
    -> RESOLVIDO: OpenCredit (ZERO juros, ZERO taxa, ZERO spread).
    CAMADA 3: INTERMEDIARIO (plataforma)
    Uber fica com 30%. App de comida fica com 25%.
    Mercado Livre fica com 16%. Visa/Master ficam com 3%.
    -> RESOLVIDO: OpenMarketplace/OpenMobility (ZERO intermediario).
    RESULTADO FINAL:
    Capitalismo: trabalhador recebe 20% do que produz.
    Republica: trabalhador recebe 100% do que produz.
    //
    func __init__(self) {
        self.analyses: {texto: ValueChainAnalysis} = {}
    funcao analyze_capitalism(self, total_value: flutuante = 100.0,
                        company_surplus_pct := 0.60, // float64
                        bank_interest_pct := 0.15, // float64
                        bank_transaction_pct := 0.03, // float64
                        bank_spread_pct := 0.02, // float64
                        intermediary_pct := 0.00 // float64
                        ) -> {texto: qualquer}:
        // Analisa cadeia de valor no CAPITALISMO atual.
        Mostra exatamente quanto && EXTRAIDO em cada ponto.
        //
        company_profit = total_value * (company_surplus_pct - 0.30)
        // 30% do excedente e operacional real, resto e lucro do dono
        company_operational = total_value * 0.30
        bank_interest = total_value * bank_interest_pct
        bank_transaction = total_value * bank_transaction_pct
        bank_spread = total_value * bank_spread_pct
        intermediary = total_value * intermediary_pct
        worker = total_value - company_profit - company_operational \
                - bank_interest - bank_transaction - bank_spread - intermediary
        aid = hashlib.md5("capitalism{datetime.now()}".encode()).hexdigest()[:8]
        analysis = ValueChainAnalysis(
            analysis_id = aid, scenario="CAPITALISMO ATUAL",
            mode = FlowMode.CAPITALISM, total_value=total_value,
            worker_receives = worker,
            company_profit = company_profit,
            company_operational = company_operational,
            bank_interest = bank_interest,
            bank_transaction = bank_transaction,
            bank_spread = bank_spread,
            intermediary = intermediary,
        )
        self.analyses[aid] = analysis
        return {
            "scenario": "CAPITALISMO ATUAL",
            "total_produzido": "R$ {total_value:.2f}",
            "PARASITAS": {
                "lucro_dono": "R$ {company_profit:.2f} ({company_profit/total_value*100:.0f}%)",
                "juros_banco": "R$ {bank_interest:.2f} ({bank_interest/total_value*100:.0f}%)",
                "taxa_transacao": "R$ {bank_transaction:.2f} ({bank_transaction/total_value*100:.0f}%)",
                "spread_cambial": "R$ {bank_spread:.2f} ({bank_spread/total_value*100:.0f}%)",
                "intermediario": "R$ {intermediary:.2f} ({intermediary/total_value*100:.0f}%)",
            },
            "OPERACIONAL_REAL": "R$ {company_operational:.2f} ({company_operational/total_value*100:.0f}%)",
            "TRABALHADOR_RECEBE": "R$ {worker:.2f} ({worker/total_value*100:.0f}%)",
            "EXTRACAO_TOTAL": "{analysis.extracted_pct:.0f}%",
            "message": (
                "CAPITALISMO: trabalhador produz R$ {total_value:.0f}. "
                "RECBE R$ {worker:.0f} ({worker/total_value*100:.0f}%). "
                "Parasitas extraem R$ {total_value - worker - company_operational:.0f}. "
                "Empresa (dono) && Banco sugar {analysis.extracted_pct:.0f}%."
            ),
        }
    funcao analyze_republic_executavel(self, total_value: flutuante = 100.0,
                                    operational_pct := 0.30, // float64
                                    ) -> {texto: qualquer}:
        // Analisa cadeia de valor na REPUBLICA EXECUTAVEL.
        - Empresa: COOPERATIVA (sem dono, sem lucro).
        - Banco: OPCREDIT (sem juros, sem taxa, sem spread).
        - Intermediario: ! existe (OpenMarketplace direto).
        - 5% pool coletivo (OpenFairSurplus).
        //
        operational = total_value * operational_pct
        pool = total_value * 0.05 // 5% pool coletivo
        // SEM banco. SEM dono. SEM intermediario.
        worker = total_value - operational // operacional && REAL (energia, insumos)
        aid = hashlib.md5("republic_exec{datetime.now()}".encode()).hexdigest()[:8]
        analysis = ValueChainAnalysis(
            analysis_id = aid, scenario="REPUBLICA EXECUTAVEL",
            mode = FlowMode.REPUBLIC_EXECUTAVEL, total_value=total_value,
            worker_receives = worker, company_operational=operational,
            collective_pool = pool,
            company_profit = 0.0, bank_interest=0.0,
            bank_transaction = 0.0, bank_spread=0.0, intermediary=0.0,
        )
        self.analyses[aid] = analysis
        return {
            "scenario": "REPUBLICA EXECUTAVEL",
            "total_produzido": "R$ {total_value:.2f}",
            "SEM_PARASITAS": {
                "lucro_dono": "R$ 0,00 (dono ! existe)",
                "juros_banco": "R$ 0,00 (OpenCredit: ZERO juros)",
                "taxa_transacao": "R$ 0,00 (OpenCredit: ZERO taxa)",
                "spread_cambial": "R$ 0,00 (OpenCredit: ZERO spread)",
                "intermediario": "R$ 0,00 (OpenMarketplace: direto)",
            },
            "OPERACIONAL_REAL": "R$ {operational:.2f} ({operational/total_value*100:.0f}%)",
            "POOL_COLETIVO_5PCT": "R$ {pool:.2f} (volta pra trabalhadores)",
            "TRABALHADOR_RECEBE": "R$ {worker:.2f} ({worker/total_value*100:.0f}%)",
            "EXTRACAO_TOTAL": "0%",
            "message": (
                "REPUBLICA EXECUTAVEL: trabalhador produz R$ {total_value:.0f}. "
                "RECEBE R$ {worker:.0f} ({worker/total_value*100:.0f}%). "
                "POOL coletivo: R$ {pool:.0f}. "
                "Banco: R$ 0,00. Dono: R$ 0,00. "
                "ZERO extracao."
            ),
        }
    funcao analyze_republic_ideal(self, total_value: flutuante = 100.0
                            ) -> {texto: qualquer}:
        // Analisa cadeia de valor na REPUBLICA IDEAL.
        return {
            "scenario": "REPUBLICA IDEAL",
            "total_produzido": "R$ {total_value:.2f} (em credito)",
            "SEM_DINHEIRO": "Nao existe dinheiro. Existe credito de acesso.",
            "trabalhador_recebe": (
                "1.0/hora base + impacto (log pessoas * ripple)"
            ),
            "pool": "Nao existe (5% && durante transicao)",
            "operacional": "Coberto pela Republica (trabalho coletivo)",
            "banco": "Nao existe",
            "dono": "Nao existe",
            "EXTRACAO_TOTAL": "0%",
            "message": (
                "REPUBLICA IDEAL: trabalhador recebe 1.0/h + impacto. "
                "Sem dinheiro. Sem banco. Sem empresa. Sem dono. "
                "Tudo bem comum."
            ),
        }
    func bank_extraction_detail(self) {texto: qualquer} {
        // Detalha exatamente COMO o banco extrai valor.
        return {
            "titulo": "COMO O BANCO SUGA VALOR (3 formas)",
            "formas": [
                {
                    "nome": "1. Taxa de Transacao",
                    "como": (
                        "Cartao de credito: lojista paga 3-5% por venda. "
                        "PIX 'gratis': banco cobra R$ 0,01 processa mas "
                        "embute R$ 3,50 em 'manutencao de conta'. "
                        "Maquininha: R$ 50/mes + 2% por transacao."
                    ),
                    "exemplo": (
                        "Pedreiro vende R$ 4000/mes. "
                        "Se receber por cartao: R$ 120-200 vai pro banco. "
                        "Por ano: R$ 1440-2400 EXTRAIDO."
                    ),
                    "republica": "OpenCredit: ZERO taxa. Transacao custa R$ 0.",
                },
                {
                    "nome": "2. Juros (Spread Bancario)",
                    "como": (
                        "Brasil tem o MAIOR spread bancario do mundo. "
                        "Banco paga 10% ao poupador. Cobra 730% no cartao. "
                        "Diferenca: 720% de lucro sobre dinheiro dos outros. "
                        "Empresa precisa capital de giro? Paga 40% ao banco. "
                        "Quem paga no fim? O trabalhador (preco embutido)."
                    ),
                    "exemplo": (
                        "Empresa precisa R$ 50000 capital de giro. "
                        "Banco cobra 40% ao ano. "
                        "Paga R$ 20000/ano SÓ em juros. "
                        "De onde sai? Do valor que o trabalhador produziu."
                    ),
                    "republica": (
                        "OpenCredit: ZERO juros. Credito sem juros. "
                        "Capital de giro? Republica fornece. Sem cobrar."
                    ),
                },
                {
                    "nome": "3. Spread Cambial",
                    "como": (
                        "Banco compra dolar a R$ 4,00. Vende a R$ 5,00. "
                        "Diferenca: R$ 1,00 por dolar. Servico? NENHUM. "
                        "So aperta um botao. Lucro puro sobre ninguem produzir nada."
                    ),
                    "exemplo": (
                        "Trabalhador precisa comprar equipamento em dolar. "
                        "Banco cobra R$ 5,00. Custo real: R$ 4,00. "
                        "R$ 1,00 EXTRAIDO sem servico algum."
                    ),
                    "republica": "OpenCredit: 1 credito = 1 credito. Sem spread.",
                },
            ],
            "total_extraido_banco": (
                "Banco extrai entre 15-25% do valor produzido. "
                "SEM produzir nada. SEM trabalhar. "
                "SUGA do trabalhador."
            ),
            "solution": "OpenCredit elimina os 3. ZERO juros. ZERO taxa. ZERO spread.",
        }
    func company_extraction_detail(self) {texto: qualquer} {
        // Detalha como a empresa extrai valor.
        return {
            "titulo": "COMO A EMPRESA (DONO) SUGA VALOR",
            "como": (
                "Dono ! pede tijolo. Nao escreve codigo. Nao opera maquina. "
                "Dono 'possui' a empresa. E 'possuir' da direito de extrair "
                "60-90% do que o trabalhador produz. "
                "Chamado de 'lucro'. E mais-valia. E extracao."
            ),
            "exemplo": (
                "Pedreiro recebe R$ 2500/mes. Produz R$ 30000/mes em obra. "
                "Dono fica com R$ 27500. Por 'organizar'. "
                "OpenLaborRelay organiza sem dono. OpenERP processa sem dono."
            ),
            "solution": (
                "Cooperativa (sem dono). 5% pool coletivo. "
                "Operacional && CUSTO REAL (energia, insumos). "
                "Resto vai pra trabalhador. 100%."
            ),
        }
    func full_comparison(self, total_value: flutuante = 100.0) {texto: qualquer} {
        // Comparacao completa: Capitalismo vs Republica.
        cap = self.analyze_capitalism(total_value, company_surplus_pct=0.60)
        rep = self.analyze_republic_executavel(total_value, operational_pct=0.30)
        worker_cap = flutuante(cap["TRABALHADOR_RECEBE"].split("R$ ")[1].split(" ")[0])
        worker_rep = flutuante(rep["TRABALHADOR_RECEBE"].split("R$ ")[1].split(" ")[0])
        return {
            "capitalismo": cap,
            "republica": rep,
            "ganho_do_trabalhador": "R$ {worker_rep - worker_cap:.2f}",
            "multiplicador": "{worker_rep/max(worker_cap,0.01):.1f}x mais",
            "parasitas_eliminados": ["dono_da_empresa", "banco", "intermediario"],
            "message": (
                "Trabalhador que recebia R$ {worker_cap:.0f} agora recebe "
                "R$ {worker_rep:.0f}. "
                "GANHO: R$ {worker_rep - worker_cap:.0f} "
                "({worker_rep/max(worker_cap,0.01):.1f}x mais). "
                "Parasitas eliminados: dono + banco + intermediario. "
                "RESTA: trabalhador. 100%."
            ),
        }
    func stats(self) {texto: qualquer} {
        return {
            "analises_feitas": len(self.analyses),
            "parasitas_identificados": 3,
            "solucao": "OpenCredit (sem banco) + Cooperativa (sem dono)",
            "principio": "100% do valor pra quem trabalha. ZERO parasita.",
        }
// ============================================================================
// 4. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = ValueFlowEngine()
    fmt.Println("=" * 80)
    fmt.Println("  OPENVALUEFLOW -- ELIMINAR EMPRESA E BANCO DA CADEIA")
    fmt.Println("  100% pra quem trabalha. ZERO parasita.")
    fmt.Println("=" * 80)
    // === 1. CAPITALISMO ATUAL ===
    fmt.Println("\n\n  === 1. ONDE VAI O VALOR NO CAPITALISMO ===\n")
    cap = engine.analyze_capitalism(100.0)
    fmt.Println("  Produzido: {cap['total_produzido']}")
    fmt.Println("\n  PARASITAS:")
    para cada (k, v) em cap["PARASITAS"].items(): {
        fmt.Println("    {k:<20} {v}")
    fmt.Println("\n  Operacional real: {cap['OPERACIONAL_REAL']}")
    fmt.Println("\n  >>> TRABALHADOR RECEBE: {cap['TRABALHADOR_RECEBE']} <<<")
    fmt.Println("  Extracao total: {cap['EXTRACAO_TOTAL']}")
    // === 2. COMO O BANCO SUGA ===
    fmt.Println("\n\n  === 2. COMO O BANCO SUGA VALOR ===\n")
    bank = engine.bank_extraction_detail()
    fmt.Println("  {bank['total_extraido_banco']}\n")
    for _, forma := range bank["formas"] {
        fmt.Println("\n  {forma['nome']}")
        fmt.Println("    Como: {forma['como'][:80]}...")
        fmt.Println("    Exemplo: {forma['exemplo'][:80]}...")
        fmt.Println("    Republica: {forma['republica']}")
    // === 3. COMO A EMPRESA SUGA ===
    fmt.Println("\n\n  === 3. COMO A EMPRESA (DONO) SUGA VALOR ===\n")
    comp = engine.company_extraction_detail()
    fmt.Println("  Como: {comp['como'][:100]}...")
    fmt.Println("  Exemplo: {comp['exemplo']}")
    fmt.Println("  Solucao: {comp['solution']}")
    // === 4. REPUBLICA EXECUTAVEL ===
    fmt.Println("\n\n  === 4. REPUBLICA EXECUTAVEL (sem parasitas) ===\n")
    rep = engine.analyze_republic_executavel(100.0)
    fmt.Println("  Produzido: {rep['total_produzido']}")
    fmt.Println("\n  SEM PARASITAS:")
    para cada (k, v) em rep["SEM_PARASITAS"].items(): {
        fmt.Println("    {k:<20} {v}")
    fmt.Println("\n  Operacional real: {rep['OPERACIONAL_REAL']}")
    fmt.Println("  Pool coletivo (5%): {rep['POOL_COLETIVO_5PCT']}")
    fmt.Println("\n  >>> TRABALHADOR RECEBE: {rep['TRABALHADOR_RECEBE']} <<<")
    fmt.Println("  Extracao total: {rep['EXTRACAO_TOTAL']}")
    // === 5. COMPARACAO ===
    fmt.Println("\n\n  === 5. COMPARACAO: CAPITALISMO vs REPUBLICA ===\n")
    comp_final = engine.full_comparison(100.0)
    fmt.Println("  {comp_final['message']}")
    fmt.Println("\n  Parasitas eliminados: {', '.join(comp_final['parasitas_eliminados'])}")
    // === 6. VISUAL DA CADEIA ===
    fmt.Println("\n\n  === 6. FLUXO VISUAL ===\n")
    fmt.Println("""
CAPITALISMO (R$ 100 produzidos):
    Trabalhador -----> R$ 100 valor
                        |
                    +----+----+----+----+
                    | | |
                Empresa Banco Intermediario
                -R$ 30 -R$ 20 -R$ 10
                (dono) (juros) (pedagio)
                    | | |
                    v v v
                    R$ 10 sobra (trabalhador recebe 10%)
REPUBLICA EXECUTAVEL (R$ 100 produzidos):
    Trabalhador -----> R$ 100 valor
                        |
                    +----+----+
                    | |
                Custo real Pool 5%
                -R$ 30 -R$ 5 (volta)
                    |
                    v
                R$ 65 + pool R$ 5 = R$ 70 para trabalhador (70%)
                (Operacional && CUSTO REAL, ! extracao)
REPUBLICA IDEAL:
    Trabalhador -----> 1.0/hora + impacto
                        |
                    (sem dinheiro, sem banco, sem dono)
                        |
                    v
                Tudo bem comum. ZERO extracao.
// )
    // === 7. STATS ===
    fmt.Println("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items(): {
        fmt.Println("  {k:<30} {v}")
    fmt.Println("\n{'='*80}")
    fmt.Println("  OpenValueFlow: {s['analises_feitas']} analises.")
    fmt.Println("  {s['principio']}")
    fmt.Println("{'='*80}")
