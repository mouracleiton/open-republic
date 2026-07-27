// OpenDebtDefault.java
// Transpilacao fiel do Python open_debt_default.py
// Simulacao: O Que Acontece Se Nao Pagar o Agiota
// Todas as classes, enums, funcoes, credores, tabela verdade, renders e demo() preservados
// Comentarios em portugues

import java.util.*;

enum CreditorType {
    NATIONAL_BONDS("titulos_publicos"),
    FOREIGN_BANKS("bancos_estrageiros"),
    IMF("fmi"),
    FOREIGN_BONDS("titulos_externos"),
    PENSION_FUNDS("fundos_pensao"),
    SOVEREIGN_FUNDS("fundos_soberanos"),
    SPECULATORS("especuladores"),
    LOCAL_BANKS("bancos_locais"),
    SUPREME_COURT("stf_judicial");

    public final String value;
    CreditorType(String v) { this.value = v; }
}

class Creditor {
    String creditor_id;
    String name;
    CreditorType creditor_type;
    double amount_owed_brl;
    double owns_pct_of_total;
    String origin_country;
    double purchase_price_pct;
    String real_risk;
    List<String> bluffs;
    String real_consequence;
    boolean can_punish;

    Creditor(String id, String n, CreditorType t, double amt, double pct, String origin,
             double purchase, List<String> b, String cons, boolean punish) {
        this.creditor_id = id; this.name = n; this.creditor_type = t;
        this.amount_owed_brl = amt; this.owns_pct_of_total = pct;
        this.origin_country = origin; this.purchase_price_pct = purchase;
        this.real_risk = "baixo"; this.bluffs = b; this.real_consequence = cons;
        this.can_punish = punish;
    }
}

enum DefaultPhase {
    PRE_DEFAULT("pre_calote"),
    ANNOUNCEMENT("anuncio"),
    PANIC("panico"),
    SHOCK("choque"),
    ADJUSTMENT("ajuste"),
    RECOVERY("recuperacao"),
    GROWTH("crescimento"),
    PROSPERITY("prosperidade");

    public final String value;
    DefaultPhase(String v) { this.value = v; }
}

class YearSimulation {
    int year;
    int year_label;
    DefaultPhase phase;
    double pay_debt_brl, pay_interest_brl, pay_public_investment_brl, pay_gdp_brl,
           pay_gdp_per_capita, pay_health_budget, pay_education_budget,
           pay_inflation, pay_unemployment, pay_poverty_pct;
    double nopay_debt_brl, nopay_interest_brl, nopay_freed_money_brl, nopay_public_investment_brl,
           nopay_gdp_brl, nopay_gdp_per_capita, nopay_health_budget, nopay_education_budget,
           nopay_inflation, nopay_unemployment, nopay_poverty_pct;
    double gdp_gap, cumulative_freed;
    String winner;

    YearSimulation(int y, int yl, DefaultPhase p) {
        this.year = y; this.year_label = yl; this.phase = p;
    }
}

class DefaultSimulator {
    int start_year;
    int years;
    double initial_debt = 6.0e12;
    double initial_gdp = 10.0e12;
    double interest_rate = 0.12;
    double gdp_growth_normal = 0.025;
    double population = 215e6;
    double revenue_pct_gdp = 0.18;
    double health_pct_budget = 0.04;
    double education_pct_budget = 0.06;
    double investment_pct_gdp = 0.02;
    double default_currency_drop = 0.40;
    double default_inflation_spike = 0.15;
    double default_recession = -0.04;
    double default_recovery_start = 2;
    double default_growth_boost = 0.05;
    List<YearSimulation> simulations = new ArrayList<>();

    DefaultSimulator(int sy, int y) { this.start_year = sy; this.years = y; }

    List<YearSimulation> simulate() {
        simulations.clear();
        double pay_debt = initial_debt;
        double pay_gdp = initial_gdp;
        double nopay_debt = initial_debt;
        double nopay_gdp = initial_gdp;
        double cumulative_freed = 0.0;

        for (int i = 0; i <= years; i++) {
            int year_label = start_year + i;
            DefaultPhase phase;
            if (i == 0) phase = DefaultPhase.ANNOUNCEMENT;
            else if (i <= 1) phase = DefaultPhase.PANIC;
            else if (i <= 2) phase = DefaultPhase.SHOCK;
            else if (i <= 3) phase = DefaultPhase.ADJUSTMENT;
            else if (i <= 7) phase = DefaultPhase.RECOVERY;
            else if (i <= 15) phase = DefaultPhase.GROWTH;
            else phase = DefaultPhase.PROSPERITY;

            // CAMINHO A: PAGANDO
            double pay_interest = pay_debt * interest_rate;
            double pay_revenue = pay_gdp * revenue_pct_gdp;
            double pay_primary = pay_revenue * 0.3;
            double pay_investment = pay_gdp * investment_pct_gdp;
            double pay_health = pay_gdp * health_pct_budget;
            double pay_education = pay_gdp * education_pct_budget;
            double pay_inflation = 0.045 + (pay_debt / pay_gdp) * 0.01;
            double pay_unemployment = 0.09 + (pay_debt / pay_gdp) * 0.02;
            double pay_poverty = 0.25 + (pay_interest / pay_gdp) * 0.1;
            if (i > 0) {
                pay_debt = pay_debt + pay_interest - pay_primary;
                pay_gdp = pay_gdp * (1 + gdp_growth_normal);
            }

            // CAMINHO B: NAO PAGAR
            double nopay_interest = 0, nopay_freed = 0, nopay_inflation = 0,
                   nopay_unemployment = 0, nopay_growth = 0;
            if (i == 0) {
                nopay_interest = nopay_debt * interest_rate;
                nopay_freed = nopay_interest;
                nopay_inflation = default_inflation_spike * 0.3;
                nopay_unemployment = 0.09;
                nopay_growth = 0.0;
                nopay_debt = nopay_debt;
            } else if (i == 1) {
                nopay_interest = 0;
                nopay_freed = pay_interest;
                nopay_inflation = default_inflation_spike;
                nopay_unemployment = 0.12;
                nopay_growth = default_recession;
                nopay_debt = nopay_debt * 0.3;
            } else if (i == 2) {
                nopay_interest = 0;
                nopay_freed = pay_interest * 1.2;
                nopay_inflation = 0.08;
                nopay_unemployment = 0.10;
                nopay_growth = 0.01;
            } else if (i == 3) {
                nopay_interest = 0;
                nopay_freed = pay_interest * 1.5;
                nopay_inflation = 0.05;
                nopay_unemployment = 0.08;
                nopay_growth = default_growth_boost * 0.6;
            } else if (i <= 7) {
                nopay_interest = 0;
                nopay_freed = pay_interest * 2.0;
                nopay_inflation = 0.04;
                nopay_unemployment = 0.06;
                nopay_growth = default_growth_boost;
            } else if (i <= 15) {
                nopay_interest = 0;
                nopay_freed = pay_interest * 2.5;
                nopay_inflation = 0.035;
                nopay_unemployment = 0.04;
                nopay_growth = default_growth_boost * 1.3;
            } else {
                nopay_interest = 0;
                nopay_freed = pay_interest * 3.0;
                nopay_inflation = 0.03;
                nopay_unemployment = 0.035;
                nopay_growth = default_growth_boost * 1.5;
            }
            cumulative_freed += nopay_freed;
            if (i > 0) nopay_gdp = nopay_gdp * (1 + nopay_growth);

            double nopay_revenue = nopay_gdp * revenue_pct_gdp;
            double nopay_investment = nopay_gdp * investment_pct_gdp + nopay_freed * 0.6;
            double nopay_health = nopay_gdp * health_pct_budget + nopay_freed * 0.15;
            double nopay_education = nopay_gdp * education_pct_budget + nopay_freed * 0.15;
            double nopay_poverty = (i > 1) ? Math.max(0.03, 0.25 - (i * 0.008)) : 0.27;

            double pay_per_capita = pay_gdp / population;
            double nopay_per_capita = nopay_gdp / population;
            double gdp_gap = nopay_gdp - pay_gdp;
            String winner = (i == 0) ? "igual" : (nopay_gdp > pay_gdp ? "nao_pagar" : "pagar");

            YearSimulation sim = new YearSimulation(i, year_label, phase);
            sim.pay_debt_brl = pay_debt; sim.pay_interest_brl = pay_interest;
            sim.pay_public_investment_brl = pay_investment; sim.pay_gdp_brl = pay_gdp;
            sim.pay_gdp_per_capita = pay_per_capita; sim.pay_health_budget = pay_health;
            sim.pay_education_budget = pay_education; sim.pay_inflation = pay_inflation;
            sim.pay_unemployment = pay_unemployment; sim.pay_poverty_pct = pay_poverty;
            sim.nopay_debt_brl = nopay_debt; sim.nopay_interest_brl = nopay_interest;
            sim.nopay_freed_money_brl = nopay_freed; sim.nopay_public_investment_brl = nopay_investment;
            sim.nopay_gdp_brl = nopay_gdp; sim.nopay_gdp_per_capita = nopay_per_capita;
            sim.nopay_health_budget = nopay_health; sim.nopay_education_budget = nopay_education;
            sim.nopay_inflation = nopay_inflation; sim.nopay_unemployment = nopay_unemployment;
            sim.nopay_poverty_pct = nopay_poverty; sim.gdp_gap = gdp_gap;
            sim.cumulative_freed = cumulative_freed; sim.winner = winner;
            simulations.add(sim);
        }
        return simulations;
    }

    Integer crossover_year() {
        for (YearSimulation s : simulations) {
            if (s.year > 0 && s.nopay_gdp_brl > s.pay_gdp_brl) return s.year_label;
        }
        return null;
    }

    Map<String, Object> final_comparison() {
        YearSimulation last = simulations.get(simulations.size()-1);
        Map<String, Object> res = new LinkedHashMap<>();
        res.put("years_simulated", years);
        res.put("crossover_year", crossover_year());
        res.put("pay_final_gdp_trillions", last.pay_gdp_brl / 1e12);
        res.put("nopay_final_gdp_trillions", last.nopay_gdp_brl / 1e12);
        res.put("gdp_difference_trillions", (last.nopay_gdp_brl - last.pay_gdp_brl) / 1e12);
        res.put("gdp_advantage_pct", ((last.nopay_gdp_brl / last.pay_gdp_brl) - 1) * 100);
        res.put("pay_final_debt_trillions", last.pay_debt_brl / 1e12);
        res.put("nopay_final_debt_trillions", last.nopay_debt_brl / 1e12);
        res.put("total_freed_trillions", last.cumulative_freed / 1e12);
        res.put("pay_poverty_final", last.pay_poverty_pct * 100);
        res.put("nopay_poverty_final", last.nopay_poverty_pct * 100);
        res.put("pay_unemployment_final", last.pay_unemployment * 100);
        res.put("nopay_unemployment_final", last.nopay_unemployment * 100);
        res.put("winner", last.nopay_gdp_brl > last.pay_gdp_brl ? "NAO PAGAR" : "PAGAR");
        return res;
    }
}

class AgiotaTruthTable {
    static List<Map<String, String>> TRUTHS = new ArrayList<>();
    static {
        TRUTHS.add(Map.of("ameaca", "O sistema financeiro vai colapsar!",
            "realidade", "Bancos brasileiros sobreviveram a Hyperinflacao (80s), Plano Real (94), crise 2008. Sobrevivem a default.",
            "exemplos", "Argentina (2001, 2014), Islandia (2008), Grecia (2012), Russia (1998), Equador (2008). Todos existem."));
        TRUTHS.add(Map.of("ameaca", "Vai faltar comida!",
            "realidade", "Brasil e um dos maiores produtores de alimentos do mundo. Default nao queima plantacao.",
            "exemplos", "Argentina deu calote e continua exportando carne e soja."));
        TRUTHS.add(Map.of("ameaca", "O dolar vai disparar!",
            "realidade", "Dolar dispara por 6-12 meses. Depois estabiliza. Exportacoes ficam mais compencivel. Industria nacional renasce.",
            "exemplos", "Islandia: coroa islandesa caiu 50% em 2008. Recuperou e hoje tem menor desigualdade da Europa."));
        TRUTHS.add(Map.of("ameaca", "Inflacao vai explodir!",
            "realidade", "Inflacao sobe por 1-2 anos. Mas a divida extinta REMOVE pressao fiscal permanente. Sem juros extorsivos, inflacao estrutural CAI.",
            "exemplos", "Equador (Correa): defaultou, inflacao caiu, pobreza despencou."));
        TRUTHS.add(Map.of("ameaca", "Ninguem vai mais emprestar!",
            "realidade", "Mercados tem memoria curta. Argentina defaultou 9 vezes. Ainda emprestam. Risco paga premio.",
            "exemplos", "Russia foi banida em 2022. Sao titulos deram 15% ao ano. Gente comprou."));
        TRUTHS.add(Map.of("ameaca", "Vao confiscar reservas!",
            "realidade", "Reservas estao protegidas por imunidade soberana. Vulture funds litigam por decadas e recebem fracoes.",
            "exemplos", "Argentina vs Elliott Management: 15 anos de processo. Recebeu 75% a mais -- mas so depois de 15 anos."));
        TRUTHS.add(Map.of("ameaca", "A democracia vai cair!",
            "realidade", "Default nao derruba democracia. AUSTERIDADE para pagar divida derruba. Greca eisende com Nazis (Aurora Dourada) por austeridade do FMI.",
            "exemplos", "Islandia: defaultou, PRESIDIU banqueiros, democracia mais forte."));
        TRUTHS.add(Map.of("ameaca", "Os pobres vao sofrer!",
            "realidade", "Os pobres JA sofrem pagando R$ 500 bi/ano em juros. Default redireciona esse dinheiro para saude, educacao, moradia.",
            "exemplos", "Equador: pobreza caiu de 36% para 21% apos default de 2008."));
        TRUTHS.add(Map.of("ameaca", "As empresas vao falir!",
            "realidade", "Empresas EXPORTADORAS ganham com moeda desvalorizada. Empresas ligadas a divida perdem. Mas o pais se reequilibra.",
            "exemplos", "Argentina: Mal do default e curto prazo. Em 3-5 anos, exportacao dispara."));
        TRUTHS.add(Map.of("ameaca", "O Brasil vai virar Venezuela!",
            "realidade", "Venezuela quebrou por SANCOES, nao por default. Brasil tem reservas, producao, diversificacao. Analogia falsa.",
            "exemplos", "Equador, Islandia, Argentina -- nenhum virou Venezuela."));
    }
}

public class open_debt_default {
    static List<Creditor> CREDITORS = new ArrayList<>();
    static {
        CREDITORS.add(new Creditor("CR-001", "Mercado de Titulos Internos (Tesouro Direto)",
            CreditorType.NATIONAL_BONDS, 4.2e12, 70.0, "Brasil", 0.95,
            Arrays.asList("Vai faltar dinheiro para tudo!", "O sistema financeiro vai colapsar!", "Ninguem vai mais emprestar pro Brasil!"),
            "Titulos sao renegociados. Investidores institucionais absorvem perda. O contribuinte brasileiro que injetou o dinheiro para pagar juros absurdos nao e responsavel por bancar especulador.", false));
        CREDITORS.add(new Creditor("CR-002", "Fundos Especulativos (Vulture Funds)",
            CreditorType.SPECULATORS, 300e9, 5.0, "EUA/Reino Unido", 0.25,
            Arrays.asList("Vamos bloquear seus ativos no exterior!", "Vamos processar na justica internacional!", "Vamos confiscares as reservas!", "Nenhum pais vai negociar com voce!"),
            "Compraram a divida por 25 centavos de dolar. Querem 100 centavos. O Brasil pode pagar 25 centavos e fechar. Vulture funds sao parasitas. O mercado ja precifica default.", false));
        CREDITORS.add(new Creditor("CR-003", "FMI (Fundo Monetario Internacional)",
            CreditorType.IMF, 0, 0.0, "Internacional", 1.0,
            Arrays.asList("Vamos impor austeridade!", "Vamos bloquear credito internacional!", "Vamos ditar sua politica economica!"),
            "FMI nao e deus. E um banco politico. Argentina deu calote em 2001 e 2014. Ainda existe. Grecia renegociou em 2012. Ainda existe. Islandia deu calote em 2008. Hoje e modelo.", false));
        CREDITORS.add(new Creditor("CR-004", "Bancos Internacionais",
            CreditorType.FOREIGN_BANKS, 500e9, 8.0, "EUA/Europa", 1.0,
            Arrays.asList("Vamos cortar linhas de credito!", "Vai faltar dolar para importar!", "Empresas estrangeiras vao fugir!"),
            "Bancos internacionais perderam dinheiro com EUA em 2008. Perderam com Grecia, Argentina, Russia, Turquia. Sempre voltam a emprestar -- porque ganham com risco. Spreads cobrem risco de default.", false));
        CREDITORS.add(new Creditor("CR-005", "Fundos de Pensao Brasileiros",
            CreditorType.PENSION_FUNDS, 600e9, 10.0, "Brasil", 1.0,
            Arrays.asList("Aposentados vao perder tudo!", "Os fundos vao quebrar!"),
            "Fundos de pensao tem diversificacao. Renegociacao preserva o valor principal. Risco de nao receber juros extorsivos e diferente de perder tudo. O brasileiro aposentado ja perde com a inflacao que a divida causa.", false));
        CREDITORS.add(new Creditor("CR-006", "Fundos Soberanos (Paises)",
            CreditorType.SOVEREIGN_FUNDS, 200e9, 3.0, "China/Oriente Medio", 1.0,
            Arrays.asList("Vamos parar de investir no Brasil!", "Vamos cortar relacoes comerciais!"),
            "Paises investem por interesse, nao por amizade. Brasil tem commodities que o mundo precisa. China continua comprando soja independentemente de divida.", false));
    }

    static String render_comparison_chart(List<YearSimulation> simulations) {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\n  PIB: CONTINUA PAGANDO vs PARA DE PAGAR\n").append("=".repeat(70)).append("\n");
        double max_gdp = 0;
        for (YearSimulation s : simulations) max_gdp = Math.max(max_gdp, Math.max(s.pay_gdp_brl, s.nopay_gdp_brl));
        int bar_width = 35;
        for (YearSimulation s : simulations) {
            int pay_bar_len = (int)((s.pay_gdp_brl / max_gdp) * bar_width);
            int nopay_bar_len = (int)((s.nopay_gdp_brl / max_gdp) * bar_width);
            String pay_bar = "P".repeat(Math.max(1, pay_bar_len));
            String nopay_bar = "L".repeat(Math.max(1, nopay_bar_len));
            String phase_marker = "";
            if (s.phase == DefaultPhase.PANIC) phase_marker = " [PANICO]";
            else if (s.phase == DefaultPhase.SHOCK) phase_marker = " [CHOQUE]";
            else if (s.phase == DefaultPhase.RECOVERY) phase_marker = " [RECUPERANDO]";
            else if (s.phase == DefaultPhase.GROWTH) phase_marker = " [DISPARANDO]";
            else if (s.phase == DefaultPhase.PROSPERITY) phase_marker = " [PRÓSPERO]";
            sb.append(String.format("  %d PAGAR: [%-" + bar_width + "s] R$ %.1fT\n", s.year_label, pay_bar, s.pay_gdp_brl/1e12));
            sb.append(String.format("      LIVRE: [%-" + bar_width + "s] R$ %.1fT%s\n\n", nopay_bar, s.nopay_gdp_brl/1e12, phase_marker));
        }
        sb.append("  P = Continua pagando (escravo)\n  L = Para de pagar (livre)\n");
        return sb.toString();
    }

    static String render_poverty_chart(List<YearSimulation> simulations) {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\n  POBREZA (% DA POPULACAO): PAGAR vs NAO PAGAR\n").append("=".repeat(70)).append("\n");
        for (YearSimulation s : simulations) {
            int pay_bar_len = (int)(s.pay_poverty_pct * 50);
            int nopay_bar_len = (int)(s.nopay_poverty_pct * 50);
            String pay_bar = "X".repeat(pay_bar_len);
            String nopay_bar = "O".repeat(nopay_bar_len);
            sb.append(String.format("  %d PAGAR: [%-50s] %.1f%%\n", s.year_label, pay_bar, s.pay_poverty_pct*100));
            sb.append(String.format("      LIVRE: [%-50s] %.1f%%\n\n", nopay_bar, s.nopay_poverty_pct*100));
        }
        sb.append("  X = Pobreza pagando divida (estagnada/alta)\n  O = Pobreza sem pagar divida (desabando)\n");
        return sb.toString();
    }

    static String render_truth_table() {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\nO AGIOTA DIZ vs O QUE REALMENTE ACONTECE\n").append("=".repeat(70)).append("\n");
        int i = 1;
        for (Map<String,String> truth : AgiotaTruthTable.TRUTHS) {
            sb.append(String.format("\n  AMEACA %d: %s\n  REALIDADE: %s\n  PROVA: %s\n  %s\n", i++, truth.get("ameaca"), truth.get("realidade"), truth.get("exemplos"), "-".repeat(66)));
        }
        sb.append("\n  O agiota so tem poder se voce tiver MEDO.\n  O medo e a arma dele. A verdade e o antidoto.\n");
        return sb.toString();
    }

    static String render_creditors() {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\nQUEM E O AGIOTA?\n").append("=".repeat(70)).append("\n");
        for (Creditor c : CREDITORS) {
            sb.append(String.format("\n  %s\n  Tipo: %s\n  Valor: R$ %.0f bilhoes (%.0f%% da divida)\n  Comprou por: %.0f centavos de cada real\n  Pode punir de verdade? %s\n  O que diz: \"%s\"\n  O que acontece: %s\n\n",
                c.name, c.creditor_type.value, c.amount_owed_brl/1e9, c.owns_pct_of_total, c.purchase_price_pct*100,
                c.can_punish ? "SIM" : "NAO", c.bluffs.get(0), c.real_consequence));
        }
        sb.append("  O agiota comprou por 25 centavos. Quer 100.\n  Paga 25. Fecha o livro. Fim do agiota.\n");
        return sb.toString();
    }

    static String render_timeline(List<YearSimulation> simulations) {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\nLINHA DO TEMPO: O QUE ACONTECE APOS PARAR DE PAGAR\n").append("=".repeat(70)).append("\n");
        for (YearSimulation s : simulations) {
            sb.append(String.format("\n  ANO %d (%d) -- FASE: %s\n", s.year, s.year_label, s.phase.value.toUpperCase()));
            if (s.phase == DefaultPhase.ANNOUNCEMENT) {
                sb.append("    O Brasil anuncia: NAO VAMOS PAGAR.\n    Agiotas gritam. Midia apavora. Bolsa cai.\n    Povo pergunta: 'E agora?'\n    Resposta: 'O sol nasce amanha.'\n");
            } else if (s.phase == DefaultPhase.PANIC) {
                sb.append(String.format("    PANICO. Dolar sobe. Inflacao %.0f%%.\n    Desemprego sobe para %.0f%%.\n    Agiotas processam. Midia diz 'Eu avisei!'.\n    Mas: R$ %.0f bi ANTES iam pro agiota.\n    Agora vai para: saude, educacao, infraestrutura.\n", s.nopay_inflation*100, s.nopay_unemployment*100, s.nopay_freed_money_brl/1e9));
            } else if (s.phase == DefaultPhase.SHOCK) {
                sb.append(String.format("    AINDA DOLORIDO. Mas inflacao caindo: %.0f%%.\n    PIB voltando a crescer.\n    Investimento publico: R$ %.0f bi (vs R$ %.0f bi se pagasse)\n", s.nopay_inflation*100, s.nopay_public_investment_brl/1e9, s.pay_public_investment_brl/1e9));
            } else if (s.phase == DefaultPhase.ADJUSTMENT) {
                sb.append(String.format("    NOVO EQUILIBRIO. Sem juros, dinheiro sobe.\n    Inflacao: %.0f%% (normalizando)\n    Desemprego: %.0f%% (caindo)\n", s.nopay_inflation*100, s.nopay_unemployment*100));
            } else if (s.phase == DefaultPhase.RECOVERY) {
                sb.append(String.format("    RECUPERANDO. PIB acelerando.\n    Pobreza: %.1f%% (vs %.1f%% pagando)\n    Dinheiro liberado acumulado: R$ %.1f trilhoes\n    Saude: R$ %.0f bi vs R$ %.0f bi\n", s.nopay_poverty_pct*100, s.pay_poverty_pct*100, s.cumulative_freed/1e12, s.nopay_health_budget/1e9, s.pay_health_budget/1e9));
            } else if (s.phase == DefaultPhase.GROWTH) {
                sb.append(String.format("    DISPARANDO. Sem divida, sem juros.\n    PIB: R$ %.1fT vs R$ %.1fT (pagando)\n    Desemprego: %.1f%% (vs %.1f%%)\n    Diferenca acumulada: R$ %.1f trilhoes a favor\n", s.nopay_gdp_brl/1e12, s.pay_gdp_brl/1e12, s.nopay_unemployment*100, s.pay_unemployment*100, s.gdp_gap/1e12));
            } else if (s.phase == DefaultPhase.PROSPERITY) {
                sb.append(String.format("    PROSPERO. Pais livre da divida.\n    PIB: R$ %.1fT vs R$ %.1fT\n    Pobreza: %.1f%% vs %.1f%%\n    VEREDICTO: nao pagar VALEU A PENA.\n", s.nopay_gdp_brl/1e12, s.pay_gdp_brl/1e12, s.nopay_poverty_pct*100, s.pay_poverty_pct*100));
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("OpenDebtDefault -- Simulacao: O Que Acontece Se Nao Pagar o Agiota");
        System.out.println("=".repeat(70));

        DefaultSimulator sim = new DefaultSimulator(2025, 20);
        List<YearSimulation> simulations = sim.simulate();

        System.out.println(render_creditors());
        System.out.println(render_truth_table());
        System.out.println(render_comparison_chart(simulations));
        System.out.println(render_poverty_chart(simulations));
        System.out.println(render_timeline(simulations));

        Map<String, Object> comparison = sim.final_comparison();
        Integer crossover = sim.crossover_year();

        System.out.println("=".repeat(70));
        System.out.println("RESULTADO FINAL APOS 20 ANOS");
        System.out.println("=".repeat(70));
        System.out.printf("  CAMINHO A (continua pagando):\n    PIB final: R$ %.1f trilhoes\n    Divida final: R$ %.1f trilhoes\n    Pobreza: %.1f%%\n    Desemprego: %.1f%%\n\n",
            (double)comparison.get("pay_final_gdp_trillions"), (double)comparison.get("pay_final_debt_trillions"),
            (double)comparison.get("pay_poverty_final"), (double)comparison.get("pay_unemployment_final"));
        System.out.printf("  CAMINHO B (parou de pagar):\n    PIB final: R$ %.1f trilhoes\n    Divida final: R$ %.1f trilhoes\n    Pobreza: %.1f%%\n    Desemprego: %.1f%%\n    Dinheiro liberado (20 anos): R$ %.1f trilhoes\n\n",
            (double)comparison.get("nopay_final_gdp_trillions"), (double)comparison.get("nopay_final_debt_trillions"),
            (double)comparison.get("nopay_poverty_final"), (double)comparison.get("nopay_unemployment_final"),
            (double)comparison.get("total_freed_trillions"));
        System.out.printf("  VANTAGEM DE NAO PAGAR:\n    PIB %.0f%% maior\n    Diferenca: R$ %.1f trilhoes\n    Crossover (ano em que ultrapassa): %s\n\n  VENCEDOR: %s\n\n%s\n",
            (double)comparison.get("gdp_advantage_pct"), (double)comparison.get("gdp_difference_trillions"), crossover, comparison.get("winner"), "=".repeat(70));
        System.out.println("CONCLUSAO\n" + "=".repeat(70) + "\n");
        System.out.println("  O agiota diz que e o fim do mundo se voce parar de pagar.");
        System.out.println("  A simulacao mostra que em 3-5 anos o pais RECUPERA.");
        System.out.println("  Em 10 anos, esta NA FRENTE.");
        System.out.println("  Em 20 anos, e OUTRO PAIS.\n");
        System.out.println("  O curto prazo doi. O longo prazo liberta.");
        System.out.println("  Continuar pagando doi PARA SEMPRE.\n");
        System.out.println("  O agiota so tem poder se voce tiver MEDO.");
        System.out.println("  O medo e a arma. A verdade e o antidoto.\n");
        System.out.println("  'O Ideal guia. O Executavel opera.'");
    }
}