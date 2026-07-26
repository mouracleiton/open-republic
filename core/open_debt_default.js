// open_debt_default.js
// Transpilacao fiel do Python open_debt_default.py
// Simulacao: O Que Acontece Se Nao Pagar o Agiota
// Todas as classes, enums, funcoes, credores, tabela verdade, renders e demo() preservados
// Comentarios em portugues

const CreditorType = {
    NATIONAL_BONDS: "titulos_publicos",
    FOREIGN_BANKS: "bancos_estrageiros",
    IMF: "fmi",
    FOREIGN_BONDS: "titulos_externos",
    PENSION_FUNDS: "fundos_pensao",
    SOVEREIGN_FUNDS: "fundos_soberanos",
    SPECULATORS: "especuladores",
    LOCAL_BANKS: "bancos_locais",
    SUPREME_COURT: "stf_judicial"
};

class Creditor {
    constructor(id, name, type, amt, pct, origin, purchase, bluffs, cons, punish) {
        this.creditor_id = id; this.name = name; this.creditor_type = type;
        this.amount_owed_brl = amt; this.owns_pct_of_total = pct;
        this.origin_country = origin; this.purchase_price_pct = purchase;
        this.real_risk = "baixo"; this.bluffs = bluffs; this.real_consequence = cons;
        this.can_punish = punish;
    }
}

const DefaultPhase = {
    PRE_DEFAULT: "pre_calote",
    ANNOUNCEMENT: "anuncio",
    PANIC: "panico",
    SHOCK: "choque",
    ADJUSTMENT: "ajuste",
    RECOVERY: "recuperacao",
    GROWTH: "crescimento",
    PROSPERITY: "prosperidade"
};

class YearSimulation {
    constructor(y, yl, p) {
        this.year = y; this.year_label = yl; this.phase = p;
    }
}

class DefaultSimulator {
    constructor(sy = 2025, y = 20) {
        this.start_year = sy; this.years = y;
        this.initial_debt = 6.0e12; this.initial_gdp = 10.0e12;
        this.interest_rate = 0.12; this.gdp_growth_normal = 0.025;
        this.population = 215e6; this.revenue_pct_gdp = 0.18;
        this.health_pct_budget = 0.04; this.education_pct_budget = 0.06;
        this.investment_pct_gdp = 0.02;
        this.default_currency_drop = 0.40; this.default_inflation_spike = 0.15;
        this.default_recession = -0.04; this.default_recovery_start = 2;
        this.default_growth_boost = 0.05;
        this.simulations = [];
    }

    simulate() {
        this.simulations = [];
        let pay_debt = this.initial_debt, pay_gdp = this.initial_gdp;
        let nopay_debt = this.initial_debt, nopay_gdp = this.initial_gdp;
        let cumulative_freed = 0.0;

        for (let i = 0; i <= this.years; i++) {
            const year_label = this.start_year + i;
            let phase;
            if (i === 0) phase = DefaultPhase.ANNOUNCEMENT;
            else if (i <= 1) phase = DefaultPhase.PANIC;
            else if (i <= 2) phase = DefaultPhase.SHOCK;
            else if (i <= 3) phase = DefaultPhase.ADJUSTMENT;
            else if (i <= 7) phase = DefaultPhase.RECOVERY;
            else if (i <= 15) phase = DefaultPhase.GROWTH;
            else phase = DefaultPhase.PROSPERITY;

            // CAMINHO A
            const pay_interest = pay_debt * this.interest_rate;
            const pay_revenue = pay_gdp * this.revenue_pct_gdp;
            const pay_primary = pay_revenue * 0.3;
            const pay_investment = pay_gdp * this.investment_pct_gdp;
            const pay_health = pay_gdp * this.health_pct_budget;
            const pay_education = pay_gdp * this.education_pct_budget;
            const pay_inflation = 0.045 + (pay_debt / pay_gdp) * 0.01;
            const pay_unemployment = 0.09 + (pay_debt / pay_gdp) * 0.02;
            const pay_poverty = 0.25 + (pay_interest / pay_gdp) * 0.1;
            if (i > 0) {
                pay_debt = pay_debt + pay_interest - pay_primary;
                pay_gdp = pay_gdp * (1 + this.gdp_growth_normal);
            }

            // CAMINHO B
            let nopay_interest = 0, nopay_freed = 0, nopay_inflation = 0,
                nopay_unemployment = 0, nopay_growth = 0;
            if (i === 0) {
                nopay_interest = nopay_debt * this.interest_rate;
                nopay_freed = nopay_interest;
                nopay_inflation = this.default_inflation_spike * 0.3;
                nopay_unemployment = 0.09; nopay_growth = 0.0;
            } else if (i === 1) {
                nopay_interest = 0; nopay_freed = pay_interest;
                nopay_inflation = this.default_inflation_spike;
                nopay_unemployment = 0.12; nopay_growth = this.default_recession;
                nopay_debt = nopay_debt * 0.3;
            } else if (i === 2) {
                nopay_interest = 0; nopay_freed = pay_interest * 1.2;
                nopay_inflation = 0.08; nopay_unemployment = 0.10; nopay_growth = 0.01;
            } else if (i === 3) {
                nopay_interest = 0; nopay_freed = pay_interest * 1.5;
                nopay_inflation = 0.05; nopay_unemployment = 0.08;
                nopay_growth = this.default_growth_boost * 0.6;
            } else if (i <= 7) {
                nopay_interest = 0; nopay_freed = pay_interest * 2.0;
                nopay_inflation = 0.04; nopay_unemployment = 0.06;
                nopay_growth = this.default_growth_boost;
            } else if (i <= 15) {
                nopay_interest = 0; nopay_freed = pay_interest * 2.5;
                nopay_inflation = 0.035; nopay_unemployment = 0.04;
                nopay_growth = this.default_growth_boost * 1.3;
            } else {
                nopay_interest = 0; nopay_freed = pay_interest * 3.0;
                nopay_inflation = 0.03; nopay_unemployment = 0.035;
                nopay_growth = this.default_growth_boost * 1.5;
            }
            cumulative_freed += nopay_freed;
            if (i > 0) nopay_gdp = nopay_gdp * (1 + nopay_growth);

            const nopay_revenue = nopay_gdp * this.revenue_pct_gdp;
            const nopay_investment = nopay_gdp * this.investment_pct_gdp + nopay_freed * 0.6;
            const nopay_health = nopay_gdp * this.health_pct_budget + nopay_freed * 0.15;
            const nopay_education = nopay_gdp * this.education_pct_budget + nopay_freed * 0.15;
            const nopay_poverty = (i > 1) ? Math.max(0.03, 0.25 - (i * 0.008)) : 0.27;

            const pay_per_capita = pay_gdp / this.population;
            const nopay_per_capita = nopay_gdp / this.population;
            const gdp_gap = nopay_gdp - pay_gdp;
            const winner = (i === 0) ? "igual" : (nopay_gdp > pay_gdp ? "nao_pagar" : "pagar");

            const sim = new YearSimulation(i, year_label, phase);
            Object.assign(sim, {
                pay_debt_brl: pay_debt, pay_interest_brl: pay_interest,
                pay_public_investment_brl: pay_investment, pay_gdp_brl: pay_gdp,
                pay_gdp_per_capita: pay_per_capita, pay_health_budget: pay_health,
                pay_education_budget: pay_education, pay_inflation: pay_inflation,
                pay_unemployment: pay_unemployment, pay_poverty_pct: pay_poverty,
                nopay_debt_brl: nopay_debt, nopay_interest_brl: nopay_interest,
                nopay_freed_money_brl: nopay_freed, nopay_public_investment_brl: nopay_investment,
                nopay_gdp_brl: nopay_gdp, nopay_gdp_per_capita: nopay_per_capita,
                nopay_health_budget: nopay_health, nopay_education_budget: nopay_education,
                nopay_inflation: nopay_inflation, nopay_unemployment: nopay_unemployment,
                nopay_poverty_pct: nopay_poverty, gdp_gap: gdp_gap,
                cumulative_freed: cumulative_freed, winner: winner
            });
            this.simulations.push(sim);
        }
        return this.simulations;
    }

    crossover_year() {
        for (const s of this.simulations) {
            if (s.year > 0 && s.nopay_gdp_brl > s.pay_gdp_brl) return s.year_label;
        }
        return null;
    }

    final_comparison() {
        const last = this.simulations[this.simulations.length - 1];
        return {
            years_simulated: this.years,
            crossover_year: this.crossover_year(),
            pay_final_gdp_trillions: last.pay_gdp_brl / 1e12,
            nopay_final_gdp_trillions: last.nopay_gdp_brl / 1e12,
            gdp_difference_trillions: (last.nopay_gdp_brl - last.pay_gdp_brl) / 1e12,
            gdp_advantage_pct: ((last.nopay_gdp_brl / last.pay_gdp_brl) - 1) * 100,
            pay_final_debt_trillions: last.pay_debt_brl / 1e12,
            nopay_final_debt_trillions: last.nopay_debt_brl / 1e12,
            total_freed_trillions: last.cumulative_freed / 1e12,
            pay_poverty_final: last.pay_poverty_pct * 100,
            nopay_poverty_final: last.nopay_poverty_pct * 100,
            pay_unemployment_final: last.pay_unemployment * 100,
            nopay_unemployment_final: last.nopay_unemployment * 100,
            winner: last.nopay_gdp_brl > last.pay_gdp_brl ? "NAO PAGAR" : "PAGAR"
        };
    }
}

const AgiotaTruthTable = {
    TRUTHS: [
        {ameaca: "O sistema financeiro vai colapsar!", realidade: "Bancos brasileiros sobreviveram a Hyperinflacao (80s), Plano Real (94), crise 2008. Sobrevivem a default.", exemplos: "Argentina (2001, 2014), Islandia (2008), Grecia (2012), Russia (1998), Equador (2008). Todos existem."},
        {ameaca: "Vai faltar comida!", realidade: "Brasil e um dos maiores produtores de alimentos do mundo. Default nao queima plantacao.", exemplos: "Argentina deu calote e continua exportando carne e soja."},
        {ameaca: "O dolar vai disparar!", realidade: "Dolar dispara por 6-12 meses. Depois estabiliza. Exportacoes ficam mais compencivel. Industria nacional renasce.", exemplos: "Islandia: coroa islandesa caiu 50% em 2008. Recuperou e hoje tem menor desigualdade da Europa."},
        {ameaca: "Inflacao vai explodir!", realidade: "Inflacao sobe por 1-2 anos. Mas a divida extinta REMOVE pressao fiscal permanente. Sem juros extorsivos, inflacao estrutural CAI.", exemplos: "Equador (Correa): defaultou, inflacao caiu, pobreza despencou."},
        {ameaca: "Ninguem vai mais emprestar!", realidade: "Mercados tem memoria curta. Argentina defaultou 9 vezes. Ainda emprestam. Risco paga premio.", exemplos: "Russia foi banida em 2022. Sao titulos deram 15% ao ano. Gente comprou."},
        {ameaca: "Vao confiscar reservas!", realidade: "Reservas estao protegidas por imunidade soberana. Vulture funds litigam por decadas e recebem fracoes.", exemplos: "Argentina vs Elliott Management: 15 anos de processo. Recebeu 75% a mais -- mas so depois de 15 anos."},
        {ameaca: "A democracia vai cair!", realidade: "Default nao derruba democracia. AUSTERIDADE para pagar divida derruba. Greca eisende com Nazis (Aurora Dourada) por austeridade do FMI.", exemplos: "Islandia: defaultou, PRESIDIU banqueiros, democracia mais forte."},
        {ameaca: "Os pobres vao sofrer!", realidade: "Os pobres JA sofrem pagando R$ 500 bi/ano em juros. Default redireciona esse dinheiro para saude, educacao, moradia.", exemplos: "Equador: pobreza caiu de 36% para 21% apos default de 2008."},
        {ameaca: "As empresas vao falir!", realidade: "Empresas EXPORTADORAS ganham com moeda desvalorizada. Empresas ligadas a divida perdem. Mas o pais se reequilibra.", exemplos: "Argentina: Mal do default e curto prazo. Em 3-5 anos, exportacao dispara."},
        {ameaca: "O Brasil vai virar Venezuela!", realidade: "Venezuela quebrou por SANCOES, nao por default. Brasil tem reservas, producao, diversificacao. Analogia falsa.", exemplos: "Equador, Islandia, Argentina -- nenhum virou Venezuela."}
    ]
};

const CREDITORS = [
    new Creditor("CR-001", "Mercado de Titulos Internos (Tesouro Direto)", CreditorType.NATIONAL_BONDS, 4.2e12, 70.0, "Brasil", 0.95,
        ["Vai faltar dinheiro para tudo!", "O sistema financeiro vai colapsar!", "Ninguem vai mais emprestar pro Brasil!"],
        "Titulos sao renegociados. Investidores institucionais absorvem perda. O contribuinte brasileiro que injetou o dinheiro para pagar juros absurdos nao e responsavel por bancar especulador.", false),
    new Creditor("CR-002", "Fundos Especulativos (Vulture Funds)", CreditorType.SPECULATORS, 300e9, 5.0, "EUA/Reino Unido", 0.25,
        ["Vamos bloquear seus ativos no exterior!", "Vamos processar na justica internacional!", "Vamos confiscares as reservas!", "Nenhum pais vai negociar com voce!"],
        "Compraram a divida por 25 centavos de dolar. Querem 100 centavos. O Brasil pode pagar 25 centavos e fechar. Vulture funds sao parasitas. O mercado ja precifica default.", false),
    new Creditor("CR-003", "FMI (Fundo Monetario Internacional)", CreditorType.IMF, 0, 0.0, "Internacional", 1.0,
        ["Vamos impor austeridade!", "Vamos bloquear credito internacional!", "Vamos ditar sua politica economica!"],
        "FMI nao e deus. E um banco politico. Argentina deu calote em 2001 e 2014. Ainda existe. Grecia renegociou em 2012. Ainda existe. Islandia deu calote em 2008. Hoje e modelo.", false),
    new Creditor("CR-004", "Bancos Internacionais", CreditorType.FOREIGN_BANKS, 500e9, 8.0, "EUA/Europa", 1.0,
        ["Vamos cortar linhas de credito!", "Vai faltar dolar para importar!", "Empresas estrangeiras vao fugir!"],
        "Bancos internacionais perderam dinheiro com EUA em 2008. Perderam com Grecia, Argentina, Russia, Turquia. Sempre voltam a emprestar -- porque ganham com risco. Spreads cobrem risco de default.", false),
    new Creditor("CR-005", "Fundos de Pensao Brasileiros", CreditorType.PENSION_FUNDS, 600e9, 10.0, "Brasil", 1.0,
        ["Aposentados vao perder tudo!", "Os fundos vao quebrar!"],
        "Fundos de pensao tem diversificacao. Renegociacao preserva o valor principal. Risco de nao receber juros extorsivos e diferente de perder tudo. O brasileiro aposentado ja perde com a inflacao que a divida causa.", false),
    new Creditor("CR-006", "Fundos Soberanos (Paises)", CreditorType.SOVEREIGN_FUNDS, 200e9, 3.0, "China/Oriente Medio", 1.0,
        ["Vamos parar de investir no Brasil!", "Vamos cortar relacoes comerciais!"],
        "Paises investem por interesse, nao por amizade. Brasil tem commodities que o mundo precisa. China continua comprando soja independentemente de divida.", false)
];

function render_comparison_chart(simulations) {
    let lines = ["", "=".repeat(70), "  PIB: CONTINUA PAGANDO vs PARA DE PAGAR", "=".repeat(70), ""];
    const max_gdp = Math.max(...simulations.map(s => Math.max(s.pay_gdp_brl, s.nopay_gdp_brl)));
    const bar_width = 35;
    for (const s of simulations) {
        const pay_bar_len = Math.max(1, Math.floor((s.pay_gdp_brl / max_gdp) * bar_width));
        const nopay_bar_len = Math.max(1, Math.floor((s.nopay_gdp_brl / max_gdp) * bar_width));
        const pay_bar = "P".repeat(pay_bar_len);
        const nopay_bar = "L".repeat(nopay_bar_len);
        let phase_marker = "";
        if (s.phase === DefaultPhase.PANIC) phase_marker = " [PANICO]";
        else if (s.phase === DefaultPhase.SHOCK) phase_marker = " [CHOQUE]";
        else if (s.phase === DefaultPhase.RECOVERY) phase_marker = " [RECUPERANDO]";
        else if (s.phase === DefaultPhase.GROWTH) phase_marker = " [DISPARANDO]";
        else if (s.phase === DefaultPhase.PROSPERITY) phase_marker = " [PRÓSPERO]";
        lines.push(`  ${s.year_label} PAGAR: [${pay_bar.padEnd(bar_width)}] R$ ${(s.pay_gdp_brl/1e12).toFixed(1)}T`);
        lines.push(`      LIVRE: [${nopay_bar.padEnd(bar_width)}] R$ ${(s.nopay_gdp_brl/1e12).toFixed(1)}T${phase_marker}`);
        lines.push("");
    }
    lines.push("  P = Continua pagando (escravo)", "  L = Para de pagar (livre)", "");
    return lines.join("\n");
}

function render_poverty_chart(simulations) {
    let lines = ["", "=".repeat(70), "  POBREZA (% DA POPULACAO): PAGAR vs NAO PAGAR", "=".repeat(70), ""];
    for (const s of simulations) {
        const pay_bar_len = Math.floor(s.pay_poverty_pct * 50);
        const nopay_bar_len = Math.floor(s.nopay_poverty_pct * 50);
        const pay_bar = "X".repeat(pay_bar_len);
        const nopay_bar = "O".repeat(nopay_bar_len);
        lines.push(`  ${s.year_label} PAGAR: [${pay_bar.padEnd(50)}] ${(s.pay_poverty_pct*100).toFixed(1)}%`);
        lines.push(`      LIVRE: [${nopay_bar.padEnd(50)}] ${(s.nopay_poverty_pct*100).toFixed(1)}%`);
        lines.push("");
    }
    lines.push("  X = Pobreza pagando divida (estagnada/alta)", "  O = Pobreza sem pagar divida (desabando)", "");
    return lines.join("\n");
}

function render_truth_table() {
    let lines = ["", "=".repeat(70), "O AGIOTA DIZ vs O QUE REALMENTE ACONTECE", "=".repeat(70), ""];
    AgiotaTruthTable.TRUTHS.forEach((truth, i) => {
        lines.push("", `  AMEACA ${i+1}: ${truth.ameaca}`, `  REALIDADE: ${truth.realidade}`, `  PROVA: ${truth.exemplos}`, `  ${"-".repeat(66)}`);
    });
    lines.push("", "  O agiota so tem poder se voce tiver MEDO.", "  O medo e a arma dele. A verdade e o antidoto.", "");
    return lines.join("\n");
}

function render_creditors() {
    let lines = ["", "=".repeat(70), "QUEM E O AGIOTA?", "=".repeat(70), ""];
    for (const c of CREDITORS) {
        lines.push("", `  ${c.name}`, `  Tipo: ${c.creditor_type}`, `  Valor: R$ ${(c.amount_owed_brl/1e9).toFixed(0)} bilhoes (${c.owns_pct_of_total.toFixed(0)}% da divida)`, `  Comprou por: ${(c.purchase_price_pct*100).toFixed(0)} centavos de cada real`, `  Pode punir de verdade? ${c.can_punish ? "SIM" : "NAO"}`, `  O que diz: "${c.bluffs[0]}"`, `  O que acontece: ${c.real_consequence}`, "");
    }
    lines.push("  O agiota comprou por 25 centavos. Quer 100.", "  Paga 25. Fecha o livro. Fim do agiota.", "");
    return lines.join("\n");
}

function render_timeline(simulations) {
    let lines = ["", "=".repeat(70), "LINHA DO TEMPO: O QUE ACONTECE APOS PARAR DE PAGAR", "=".repeat(70), ""];
    for (const s of simulations) {
        lines.push("", `  ANO ${s.year} (${s.year_label}) -- FASE: ${s.phase.toUpperCase()}`);
        if (s.phase === DefaultPhase.ANNOUNCEMENT) {
            lines.push("    O Brasil anuncia: NAO VAMOS PAGAR.", "    Agiotas gritam. Midia apavora. Bolsa cai.", "    Povo pergunta: 'E agora?'", "    Resposta: 'O sol nasce amanha.'");
        } else if (s.phase === DefaultPhase.PANIC) {
            lines.push(`    PANICO. Dolar sobe. Inflacao ${(s.nopay_inflation*100).toFixed(0)}%.`, `    Desemprego sobe para ${(s.nopay_unemployment*100).toFixed(0)}%.`, "    Agiotas processam. Midia diz 'Eu avisei!'." , `    Mas: R$ ${(s.nopay_freed_money_brl/1e9).toFixed(0)} bi ANTES iam pro agiota.`, "    Agora vai para: saude, educacao, infraestrutura.");
        } else if (s.phase === DefaultPhase.SHOCK) {
            lines.push(`    AINDA DOLORIDO. Mas inflacao caindo: ${(s.nopay_inflation*100).toFixed(0)}%.`, "    PIB voltando a crescer.", `    Investimento publico: R$ ${(s.nopay_public_investment_brl/1e9).toFixed(0)} bi (vs R$ ${(s.pay_public_investment_brl/1e9).toFixed(0)} bi se pagasse)`);
        } else if (s.phase === DefaultPhase.ADJUSTMENT) {
            lines.push(`    NOVO EQUILIBRIO. Sem juros, dinheiro sobe.`, `    Inflacao: ${(s.nopay_inflation*100).toFixed(0)}% (normalizando)`, `    Desemprego: ${(s.nopay_unemployment*100).toFixed(0)}% (caindo)`);
        } else if (s.phase === DefaultPhase.RECOVERY) {
            lines.push(`    RECUPERANDO. PIB acelerando.`, `    Pobreza: ${(s.nopay_poverty_pct*100).toFixed(1)}% (vs ${(s.pay_poverty_pct*100).toFixed(1)}% pagando)`, `    Dinheiro liberado acumulado: R$ ${(s.cumulative_freed/1e12).toFixed(1)} trilhoes`, `    Saude: R$ ${(s.nopay_health_budget/1e9).toFixed(0)} bi vs R$ ${(s.pay_health_budget/1e9).toFixed(0)} bi`);
        } else if (s.phase === DefaultPhase.GROWTH) {
            lines.push(`    DISPARANDO. Sem divida, sem juros.`, `    PIB: R$ ${(s.nopay_gdp_brl/1e12).toFixed(1)}T vs R$ ${(s.pay_gdp_brl/1e12).toFixed(1)}T (pagando)`, `    Desemprego: ${(s.nopay_unemployment*100).toFixed(1)}% (vs ${(s.pay_unemployment*100).toFixed(1)}%)`, `    Diferenca acumulada: R$ ${(s.gdp_gap/1e12).toFixed(1)} trilhoes a favor`);
        } else if (s.phase === DefaultPhase.PROSPERITY) {
            lines.push(`    PROSPERO. Pais livre da divida.`, `    PIB: R$ ${(s.nopay_gdp_brl/1e12).toFixed(1)}T vs R$ ${(s.pay_gdp_brl/1e12).toFixed(1)}T`, `    Pobreza: ${(s.nopay_poverty_pct*100).toFixed(1)}% vs ${(s.pay_poverty_pct*100).toFixed(1)}%`, "    VEREDICTO: nao pagar VALEU A PENA.");
        }
    }
    return lines.join("\n");
}

function demo() {
    console.log("=".repeat(70));
    console.log("OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota");
    console.log("=".repeat(70));

    const sim = new DefaultSimulator(2025, 20);
    const simulations = sim.simulate();

    console.log(render_creditors());
    console.log(render_truth_table());
    console.log(render_comparison_chart(simulations));
    console.log(render_poverty_chart(simulations));
    console.log(render_timeline(simulations));

    const comparison = sim.final_comparison();
    const crossover = sim.crossover_year();

    console.log("=".repeat(70));
    console.log("RESULTADO FINAL APOS 20 ANOS");
    console.log("=".repeat(70));
    console.log(`  CAMINHO A (continua pagando):\n    PIB final: R$ ${comparison.pay_final_gdp_trillions.toFixed(1)} trilhoes\n    Divida final: R$ ${comparison.pay_final_debt_trillions.toFixed(1)} trilhoes\n    Pobreza: ${comparison.pay_poverty_final.toFixed(1)}%\n    Desemprego: ${comparison.pay_unemployment_final.toFixed(1)}%\n`);
    console.log(`  CAMINHO B (parou de pagar):\n    PIB final: R$ ${comparison.nopay_final_gdp_trillions.toFixed(1)} trilhoes\n    Divida final: R$ ${comparison.nopay_final_debt_trillions.toFixed(1)} trilhoes\n    Pobreza: ${comparison.nopay_poverty_final.toFixed(1)}%\n    Desemprego: ${comparison.nopay_unemployment_final.toFixed(1)}%\n    Dinheiro liberado (20 anos): R$ ${comparison.total_freed_trillions.toFixed(1)} trilhoes\n`);
    console.log(`  VANTAGEM DE NAO PAGAR:\n    PIB ${comparison.gdp_advantage_pct.toFixed(0)}% maior\n    Diferenca: R$ ${comparison.gdp_difference_trillions.toFixed(1)} trilhoes\n    Crossover (ano em que ultrapassa): ${crossover}\n\n  VENCEDOR: ${comparison.winner}\n\n${"=".repeat(70)}`);
    console.log("CONCLUSAO\n" + "=".repeat(70) + "\n");
    console.log("  O agiota diz que e o fim do mundo se voce parar de pagar.");
    console.log("  A simulacao mostra que em 3-5 anos o pais RECUPERA.");
    console.log("  Em 10 anos, esta NA FRENTE.");
    console.log("  Em 20 anos, e OUTRO PAIS.\n");
    console.log("  O curto prazo doi. O longo prazo liberta.");
    console.log("  Continuar pagando doi PARA SEMPRE.\n");
    console.log("  O agiota so tem poder se voce tiver MEDO.");
    console.log("  O medo e a arma. A verdade e o antidoto.\n");
    console.log("  'O Ideal guia. O Executavel opera.'");
}

if (require.main === module) {
    demo();
}

module.exports = { DefaultSimulator, demo, render_comparison_chart, render_poverty_chart, render_truth_table, render_creditors, render_timeline, CREDITORS, AgiotaTruthTable };