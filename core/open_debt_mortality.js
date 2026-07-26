// OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?
// ==========================================================
// "Cada R$ 1 bilhao pago em juros e:
// - 2 hospitais que nao foram construidos
// - 50 mil casas populares que nao foram entregues
// - 200 mil cestas de comida que nao foram distribuidas
// - 10 mil bolsas universitarias que nao foram concedidas
//
// E esses hospitais, casas, comidas e bolsas que NAO EXISTEM
// porque o dinheiro foi pro agiota -- essas sao as PESSOAS que morrem.
//
// O juros da divida MATA. MATA de forma invisivel.
// Nao e uma bala. E a AUSENCIA de um medico.
// Nao e uma faca. E a AUSENCIA de comida na mesa.
// Nao e um tiro. E a AUSENCIA de saneamento basico.
//
// Este modulo calcula, ano a ano, quantas pessoas MORREM
// no Brasil porque o dinheiro que deveria salvar suas vidas
// foi enviado para o agiota international como 'juros da divida'.
//
// METODOLOGIA:
// - Calcular juros pagos por ano (R$ bilhoes)
// - Calcular quanto disso deveria ir para saude, comida, saneamento
// - Calcular mortes evitaveis por falta de cada recurso
// - Comparar: se nao pagasse a divida, quantas vidas seriam salvas?
//
// AS MORTES NAO SAO ABSTRATAS. SAO NOMES. SAO CRIANCAS.
// Sao os 124 mil brasileiros que morrem por ano por causas evitaveis
// no SUS subfinanciado. Sao as criancas desnutridas no Nordeste.
// Sao os idosos sem atendimento na fila do SUS.
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

const PreventableDeathCategory = {
    HEALTHCARE_SHORTAGE: "falta_sus",
    CHILD_MORTALITY: "mortalidade_infantil",
    MATERNAL_DEATH: "morte_materna",
    MALNUTRITION: "desnutricao",
    PREVENTABLE_DISEASE: "doenca_evitavel",
    VIOLENCE: "violencia",
    SUICIDE: "suicidio",
    SANITATION: "saneamento",
    ROAD_DEATH: "transito",
    HEAT_COLD: "calor_frio",
    DRUG_OVERDOSE: "overdose",
    CANCER_UNTREATED: "cancer_sem_tratamento",
    HEART_UNTREATED: "coracao_sem_atendimento",
    NEONATAL: "neonatal"
};

class DeathCost {
    constructor(category, name, cost_to_save_one_life_brl, deaths_per_year_brazil, pct_linked_to_underfunding, description) {
        this.category = category;
        this.name = name;
        this.cost_to_save_one_life_brl = cost_to_save_one_life_brl;
        this.deaths_per_year_brazil = deaths_per_year_brazil;
        this.pct_linked_to_underfunding = pct_linked_to_underfunding;
        this.description = description;
    }
    deaths_preventable() {
        return Math.floor(this.deaths_per_year_brazil * this.pct_linked_to_underfunding);
    }
    lives_saved_per_billion() {
        if (this.cost_to_save_one_life_brl <= 0) return 0;
        return 1e9 / this.cost_to_save_one_life_brl;
    }
}

const DEATH_COSTS = [
    new DeathCost(PreventableDeathCategory.HEALTHCARE_SHORTAGE, "Morte na fila do SUS", 500000, 124000, 0.60, "Pessoas que morrem esperando cirurgia, exame, consulta, UTI."),
    new DeathCost(PreventableDeathCategory.CHILD_MORTALITY, "Mortalidade infantil (0-5 anos)", 80000, 40000, 0.70, "Criancas que morrem antes dos 5 anos por falta de atendimento."),
    new DeathCost(PreventableDeathCategory.MATERNAL_DEATH, "Morte materna (no parto)", 50000, 1800, 0.80, "Maes que morrem no parto por falta de estrutura hospitalar."),
    new DeathCost(PreventableDeathCategory.MALNUTRITION, "Desnutricao", 15000, 5000, 0.90, "Pessoas que morrem de fome ou desnutricao grave no Brasil."),
    new DeathCost(PreventableDeathCategory.PREVENTABLE_DISEASE, "Doencas evitaveis (vacina/exame)", 20000, 50000, 0.65, "Mortes por doencas que vacina ou exame precoce previniria."),
    new DeathCost(PreventableDeathCategory.VIOLENCE, "Violencia / Homicidio", 300000, 47000, 0.40, "Jovens mortos por violencia. Programa social reduz 40%."),
    new DeathCost(PreventableDeathCategory.SUICIDE, "Suicidio (sem saude mental)", 100000, 14000, 0.55, "Pessoas que se matam por falta de atendimento psicologico."),
    new DeathCost(PreventableDeathCategory.SANITATION, "Doenças por falta de saneamento", 40000, 8000, 0.85, "Mortes por diarreia, leptospirose, hepatite por agua suja."),
    new DeathCost(PreventableDeathCategory.ROAD_DEATH, "Morte no transito", 2000000, 30000, 0.35, "Acidentes em estradas sem manutencao ou sinalizacao."),
    new DeathCost(PreventableDeathCategory.CANCER_UNTREATED, "Cancer sem tratamento a tempo", 800000, 35000, 0.50, "Pessoas que morrem esperando tratamento de cancer no SUS."),
    new DeathCost(PreventableDeathCategory.HEART_UNTREATED, "Infarto sem atendimento", 600000, 100000, 0.30, "Infartos que UTI/SAMU salvaria se chegasse a tempo."),
    new DeathCost(PreventableDeathCategory.NEONATAL, "Morte neonatal", 120000, 19000, 0.65, "Bebe que morre nos primeiros 28 dias por falta de UTI neonatal.")
];

class CountryCreditor {
    constructor(country, amount_received_brl, flag, description) {
        this.country = country;
        this.amount_received_brl = amount_received_brl;
        this.flag = flag;
        this.description = description;
    }
}

const COUNTRY_CREDITORS = [
    new CountryCreditor("Estados Unidos", 180e9, "EUA", "Fundos de investimento e bancos americanos recebem bilhoes em juros."),
    new CountryCreditor("Reino Unido", 80e9, "UK", "Londres e centro de vulture funds que lucram com divida alheia."),
    new CountryCreditor("Alemanha", 50e9, "DE", "Bancos alemaes detem titulos brasileiros."),
    new CountryCreditor("Japao", 40e9, "JP", "Fundos japoneses investem em divida soberana."),
    new CountryCreditor("Franca", 35e9, "FR", "Bancos franceses (BNP, SocGen) detem titulos."),
    new CountryCreditor("Suica", 30e9, "CH", "Centro de banca privada que lucra com juros."),
    new CountryCreditor("China", 25e9, "CN", "Bancos chineses compraram titulos brasileiros."),
    new CountryCreditor("Holanda", 20e9, "NL", "Centro financeiro (Amsterda) roteia investimentos."),
    new CountryCreditor("Luxemburgo", 15e9, "LU", "Paraiso fiscal que abriga fundos especulativos."),
    new CountryCreditor("Outros", 25e9, "??", "Outros paises e fundos internacionais.")
];

class YearMortality {
    constructor(year_label, interest_paid_brl, gdp_brl, total_preventable_deaths, deaths_linked_to_debt,
                potential_lives_saved, hospitals_not_built, people_without_doctor,
                children_not_vaccinated, houses_not_built, meals_not_served, cumulative_deaths_by_debt) {
        this.year_label = year_label;
        this.interest_paid_brl = interest_paid_brl;
        this.gdp_brl = gdp_brl;
        this.total_preventable_deaths = total_preventable_deaths;
        this.deaths_linked_to_debt = deaths_linked_to_debt;
        this.potential_lives_saved = potential_lives_saved;
        this.hospitals_not_built = hospitals_not_built;
        this.people_without_doctor = people_without_doctor;
        this.children_not_vaccinated = children_not_vaccinated;
        this.houses_not_built = houses_not_built;
        this.meals_not_served = meals_not_served;
        this.cumulative_deaths_by_debt = cumulative_deaths_by_debt;
    }
}

class DebtMortalitySimulator {
    constructor(start_year = 2024, years = 20) {
        this.start_year = start_year;
        this.years = years;
        this.initial_debt = 6.0e12;
        this.initial_gdp = 10.0e12;
        this.interest_rate = 0.12;
        this.gdp_growth = 0.025;
        this.population = 215e6;
        this.fraction_to_health = 0.40;
        this.fraction_to_food = 0.15;
        this.fraction_to_housing = 0.15;
        this.fraction_to_education = 0.15;
        this.fraction_to_infra = 0.15;
        this.simulations = [];
    }

    simulate() {
        this.simulations = [];
        let debt = this.initial_debt;
        let gdp = this.initial_gdp;
        let cumulative_deaths = 0;

        for (let i = 0; i <= this.years; i++) {
            const year_label = this.start_year + i;
            const interest = debt * this.interest_rate;
            const money_for_health = interest * this.fraction_to_health;
            const money_for_food = interest * this.fraction_to_food;

            let potential_saved = 0;
            for (const dc of DEATH_COSTS) {
                const lives_saved = money_for_health * 0.3 / dc.cost_to_save_one_life_brl;
                potential_saved += Math.floor(lives_saved);
            }

            let total_preventable = 0;
            for (const dc of DEATH_COSTS) total_preventable += dc.deaths_preventable();

            const deaths_by_debt = Math.min(potential_saved, total_preventable);

            const hospitals_not_built = Math.floor(money_for_health / 50e6);
            const people_without_doctor = Math.floor(money_for_health / 3000);
            const children_not_vaccinated = Math.floor(money_for_health / 50);
            const houses_not_built = Math.floor(interest * this.fraction_to_housing / 80000);
            const meals_not_served = Math.floor(money_for_food / 3);

            cumulative_deaths += deaths_by_debt;

            const sim = new YearMortality(
                year_label, interest, gdp, total_preventable, deaths_by_debt,
                potential_saved, hospitals_not_built, people_without_doctor,
                children_not_vaccinated, houses_not_built, meals_not_served, cumulative_deaths
            );
            this.simulations.push(sim);

            debt = debt + interest - (gdp * 0.18 * 0.3);
            gdp = gdp * (1 + this.gdp_growth);
        }
        return this.simulations;
    }

    total_deaths_by_debt() {
        return this.simulations.length ? this.simulations[this.simulations.length-1].cumulative_deaths_by_debt : 0;
    }

    total_interest_paid() {
        return this.simulations.reduce((sum, s) => sum + s.interest_paid_brl, 0);
    }

    death_per_trillion_interest() {
        const total_int = this.total_interest_paid();
        if (total_int === 0) return 0;
        return this.total_deaths_by_debt() / (total_int / 1e12);
    }

    summary() {
        const last = this.simulations.length ? this.simulations[this.simulations.length-1] : null;
        return {
            years_simulated: this.years,
            total_deaths_by_debt: this.total_deaths_by_debt(),
            total_interest_paid_trillions: this.total_interest_paid() / 1e12,
            deaths_per_trillion_interest: this.death_per_trillion_interest(),
            avg_deaths_per_year: this.total_deaths_by_debt() / Math.max(1, this.years),
            final_year_hospitals_not_built: last ? last.hospitals_not_built : 0,
            final_year_meals_not_served: last ? last.meals_not_served : 0,
            final_year_children_not_vaccinated: last ? last.children_not_vaccinated : 0
        };
    }
}

function render_death_chart(simulations) {
    let lines = ["", "=".repeat(70), "  MORTES POR ANO CAUSADAS PELA DIVIDA",
        "  (pessoas que morreriam VIVAS se o juros fosse investido em saude)", "=".repeat(70), ""];
    let max_deaths = Math.max(...simulations.map(s => s.deaths_linked_to_debt)) || 1;
    for (const s of simulations) {
        const bar_len = Math.floor((s.deaths_linked_to_debt / max_deaths) * 50);
        const bar = "#".repeat(Math.max(1, bar_len));
        lines.push(`  ${s.year_label} |${bar.padEnd(50)}| ${s.deaths_linked_to_debt.toLocaleString().padStart(8)} mortes`);
    }
    lines.push("", `  Cada # representa ~${Math.floor(max_deaths/50).toLocaleString()} mortes`,
        `  TOTAL ACUMULADO: ${simulations[simulations.length-1].cumulative_deaths_by_debt.toLocaleString()} mortes`,
        `  em ${simulations.length-1} anos`, "");
    return lines.join("\n");
}

function render_country_deaths() {
    let lines = ["", "=".repeat(70), "  PARA QUEM O BRASIL PAGA -- E QUANTOS MORREM POR ISSO", "=".repeat(70), ""];
    const total_received = COUNTRY_CREDITORS.reduce((s, c) => s + c.amount_received_brl, 0);
    for (const c of COUNTRY_CREDITORS) {
        const pct = (c.amount_received_brl / total_received) * 100;
        const deaths_caused = Math.floor(c.amount_received_brl / 500000);
        const bar = "$".repeat(Math.floor(pct));
        lines.push(`  ${c.country.padEnd(15)} R$ ${(c.amount_received_brl/1e9).toFixed(0).padStart(6)} bi/ano [${bar.padEnd(20)}] ${pct.toFixed(1).padStart(5)}%  ~${deaths_caused.toLocaleString()} mortes`);
    }
    lines.push("", `  TOTAL ENVIADO AO EXTERIOR: R$ ${(total_received/1e9).toFixed(0)} bilhoes/ano`,
        `  MORTES CAUSADAS: ~${Math.floor(total_received/500000).toLocaleString()} por ano`,
        `  Cada $ = R$ ${(total_received/20/1e9).toFixed(0)} bilhoes que sai do Brasil`, "",
        "  Cada real enviado ao agiota international e uma vida",
        "  que NAO foi salva no Brasil.", "");
    return lines.join("\n");
}

function render_category_breakdown() {
    let lines = ["", "=".repeat(70), "  MORTES EVITAVEIS NO BRASIL (por categoria, por ano)", "=".repeat(70), ""];
    const total_preventable = DEATH_COSTS.reduce((s, dc) => s + dc.deaths_preventable(), 0);
    lines.push(`${"CATEGORIA".padEnd(40)} ${"MORTES/ANO".padStart(12)} ${"CUSTO/VIDA".padStart(15)} ${"EVITAVEIS".padStart(12)}`);
    lines.push("-".repeat(80));
    for (const dc of DEATH_COSTS) {
        lines.push(`  ${dc.name.padEnd(38)} ${dc.deaths_per_year_brazil.toLocaleString().padStart(10)} R$ ${dc.cost_to_save_one_life_brl.toLocaleString().padStart(12)} ${dc.deaths_preventable().toLocaleString().padStart(10)}`);
    }
    const sumDeaths = DEATH_COSTS.reduce((s, dc) => s + dc.deaths_per_year_brazil, 0);
    lines.push("-".repeat(80));
    lines.push(`  ${"TOTAL".padEnd(38)} ${sumDeaths.toLocaleString().padStart(10)} ${"".padStart(15)} ${total_preventable.toLocaleString().padStart(10)}`);
    lines.push("", `  Total de mortes evitaveis/ano: ${total_preventable.toLocaleString()}`,
        `  Isso e ${(total_preventable/365).toFixed(0)} mortes POR DIA.`,
        `  ${(total_preventable/365/24).toFixed(0)} mortes POR HORA.`,
        `  ${(total_preventable/365/24/60).toFixed(1)} mortes POR MINUTO.`, "",
        "  UMA PESSOA MORRE NO BRASIL A CADA MINUTO",
        "  POR ALGO QUE DINHEIRO RESOLVERIA.", "",
        "  E o dinheiro? FOI PRA O AGIOTA.", "");
    return lines.join("\n");
}

function render_lost_infrastructure(simulations) {
    const s = simulations[0];
    let lines = ["", "=".repeat(70), `  O QUE O BRASIL NAO CONSTRUIU EM UM ANO`, `  (${s.year_label} -- R$ ${(s.interest_paid_brl/1e9).toFixed(0)} bi em juros)`, "=".repeat(70), ""];
    lines.push(`  Hospitais nao construidos:        ${s.hospitals_not_built.toLocaleString().padStart(8)}`);
    lines.push(`  Casas populares nao entregues:    ${s.houses_not_built.toLocaleString().padStart(8)}`);
    lines.push(`  Pessoas sem medico de familia:    ${s.people_without_doctor.toLocaleString().padStart(8)}`);
    lines.push(`  Criancas nao vacinadas:            ${s.children_not_vaccinated.toLocaleString().padStart(8)}`);
    lines.push(`  Refeicoes nao servidas:            ${s.meals_not_served.toLocaleString().padStart(8)}`);
    lines.push("", "  Em UM ano, o juros da divida pagou:",
        `  - ${s.hospitals_not_built.toLocaleString()} hospitais QUE NAO EXISTEM`,
        `  - ${s.houses_not_built.toLocaleString()} casas QUE NAO FORAM ENTREGUES`,
        `  - ${s.meals_not_served.toLocaleString()} refeicoes QUE NAO FORAM SERVIDAS`, "",
        "  Cada hospital que nao existe = pessoas que morrem na fila.",
        "  Cada casa que nao foi entregue = familias na rua.",
        "  Cada refeicao que nao foi servida = criancas desnutridas.", "");
    return lines.join("\n");
}

function render_timeline_human(simulations) {
    let lines = ["", "=".repeat(70), "  LINHA DO TEMPO DA MORTE", "=".repeat(70), ""];
    for (const s of simulations) {
        const deaths_per_day = s.deaths_linked_to_debt / 365;
        lines.push(`  ${s.year_label}:`,
            `    Juros pago: R$ ${(s.interest_paid_brl/1e9).toFixed(0)} bilhoes`,
            `    Mortes causadas pela divida: ${s.deaths_linked_to_debt.toLocaleString()}`,
            `    Isso sao ${deaths_per_day.toFixed(0)} mortes POR DIA`,
            `    Acumulado desde ${simulations[0].year_label}: ${s.cumulative_deaths_by_debt.toLocaleString()}`, "");
    }
    const last = simulations[simulations.length-1];
    lines.push(`  Em ${simulations.length-1} anos, a divida causou a morte de:`,
        `  ${last.cumulative_deaths_by_debt.toLocaleString()} PESSOAS.`, "",
        "  Isso e mais que a populacao de muitas cidades brasileiras.",
        "  Mais que todas as guerras do Brasil juntas.",
        "  Mais que todas as epidemias da historia recente.", "",
        "  E nao foi uma bala. Foi um BOLETO.", "");
    return lines.join("\n");
}

function render_narrative(simulations) {
    const s0 = simulations[0];
    const last = simulations[simulations.length-1];
    const total = last.cumulative_deaths_by_debt;
    const parts = [
        "Vou te dizer algo que ninguem te conta.",
        "",
        `No ano ${s0.year_label}, o Brasil pagou R$ ${(s0.interest_paid_brl/1e9).toFixed(0)} bilhoes apenas em JUROS da divida publica.`,
        "Esse dinheiro foi para bancos, fundos, paises estrangeiros. Nao foi para o SUS. Nao foi para a escola. Nao foi para a comida.",
        "",
        `No mesmo ano, ${s0.deaths_linked_to_debt.toLocaleString()} brasileiros morreram por causas evitaveis. Filas do SUS. Desnutricao. Falta de medico.`,
        "",
        `Se o dinheiro dos juros tivesse ido para a saude,`,
        `${s0.potential_lives_saved.toLocaleString()} dessas pessoas poderiam estar VIVAS.`,
        "",
        `Em ${simulations.length-1} anos, se nada mudar,`,
        `a divida tera causado a morte de ${total.toLocaleString()} pessoas.`,
        "",
        `${(total/365).toFixed(0)} mortes por dia. A cada minuto, alguem morre porque o dinheiro que salvaria sua vida foi para o agiota.`,
        "",
        "A divida nao e um numero. E um CEMITERIO.",
        "Cada parcela paga e uma cova que nao foi aberta.",
        "Cada juros pago e uma vida que nao foi salva.",
        "",
        "A divida MATA."
    ];
    return parts.join(" ");
}

function demo() {
    console.log("=".repeat(70));
    console.log("OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?");
    console.log("=".repeat(70));

    const sim = new DebtMortalitySimulator(2024, 20);
    const simulations = sim.simulate();

    console.log(render_category_breakdown());
    console.log(render_country_deaths());
    console.log(render_lost_infrastructure(simulations));
    console.log(render_death_chart(simulations));
    console.log(render_timeline_human(simulations));

    console.log("\n" + "=".repeat(70));
    console.log("NARRATIVA (para Telefonista ler)");
    console.log("=".repeat(70));
    console.log(render_narrative(simulations));

    const summary = sim.summary();
    console.log("\n" + "=".repeat(70));
    console.log("RESUMO");
    console.log("=".repeat(70));
    console.log(`  Anos simulados: ${summary.years_simulated}`);
    console.log(`  Total de mortes pela divida: ${summary.total_deaths_by_debt.toLocaleString()}`);
    console.log(`  Total de juros pagos: R$ ${summary.total_interest_paid_trillions.toFixed(1)} trilhoes`);
    console.log(`  Mortes por R$ 1 trilhao de juros: ${summary.deaths_per_trillion_interest.toFixed(0)}`);
    console.log(`  Media de mortes/ano: ${summary.avg_deaths_per_year.toFixed(0)}`);

    console.log("\n" + "=".repeat(70));
    console.log("VEREDICTO");
    console.log("=".repeat(70));
    console.log();
    console.log("  A divida publica nao e apenas impossivel de pagar.");
    console.log("  Ela e um ASSASSINO DE MASSA silencioso.");
    console.log();
    console.log(`  Em ${summary.years_simulated} anos:`);
    console.log(`  ${summary.total_deaths_by_debt.toLocaleString()} brasileiros morreram`);
    console.log(`  porque R$ ${summary.total_interest_paid_trillions.toFixed(1)} trilhoes`);
    console.log("  foram enviados ao agiota em vez de ir para saude, comida, vida.");
    console.log();
    console.log("  A divida MATA.");
    console.log("  Cada juros pago e uma vida nao salva.");
    console.log("  Nao renegociar. Nao alongar.");
    console.log("  EXTINGUIR.");
    console.log("  Pelas vidas que ainda podem ser salvas.");
    console.log();
    console.log("  'Nao existe pobreza, existe MISERIA.'");
    console.log("  A divida e a maquina que PRODUZ a miseria.");
}

if (require.main === module) {
    demo();
}

module.exports = {
    PreventableDeathCategory, DeathCost, DEATH_COSTS, CountryCreditor, COUNTRY_CREDITORS,
    YearMortality, DebtMortalitySimulator, demo,
    render_death_chart, render_country_deaths, render_category_breakdown,
    render_lost_infrastructure, render_timeline_human, render_narrative
};