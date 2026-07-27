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

import java.util.*;

enum PreventableDeathCategory {
    HEALTHCARE_SHORTAGE("falta_sus"),           // morreu na fila do SUS
    CHILD_MORTALITY("mortalidade_infantil"),    // bebe nao sobreviveu
    MATERNAL_DEATH("morte_materna"),             // mae morreu no parto
    MALNUTRITION("desnutricao"),                 // morreu de fome
    PREVENTABLE_DISEASE("doenca_evitavel"),      // vacina/exame nao chegou
    VIOLENCE("violencia"),                       // sem programa social
    SUICIDE("suicidio"),                         // sem saude mental
    SANITATION("saneamento"),                    // agua contaminada
    ROAD_DEATH("transito"),                      // estrada sem manutencao
    HEAT_COLD("calor_frio"),                     // sem teto/climatizacao
    DRUG_OVERDOSE("overdose"),                   // sem tratamento
    CANCER_UNTREATED("cancer_sem_tratamento"),   // fila de quimio
    HEART_UNTREATED("coracao_sem_atendimento"),  // sem UTI
    NEONATAL("neonatal");                        // sem UTI neonatal

    public final String code;
    PreventableDeathCategory(String code) { this.code = code; }
}

class DeathCost {
    public final PreventableDeathCategory category;
    public final String name;
    public final double cost_to_save_one_life_brl;
    public final int deaths_per_year_brazil;
    public final double pct_linked_to_underfunding;
    public final String description;

    public DeathCost(PreventableDeathCategory category, String name,
                     double cost_to_save_one_life_brl, int deaths_per_year_brazil,
                     double pct_linked_to_underfunding, String description) {
        this.category = category;
        this.name = name;
        this.cost_to_save_one_life_brl = cost_to_save_one_life_brl;
        this.deaths_per_year_brazil = deaths_per_year_brazil;
        this.pct_linked_to_underfunding = pct_linked_to_underfunding;
        this.description = description;
    }

    public int deaths_preventable() {
        return (int)(this.deaths_per_year_brazil * this.pct_linked_to_underfunding);
    }

    public double lives_saved_per_billion() {
        if (this.cost_to_save_one_life_brl <= 0) return 0;
        return 1e9 / this.cost_to_save_one_life_brl;
    }
}

final class DebtMortalityData {
    public static final List<DeathCost> DEATH_COSTS = Arrays.asList(
        new DeathCost(PreventableDeathCategory.HEALTHCARE_SHORTAGE, "Morte na fila do SUS",
            500_000, 124_000, 0.60, "Pessoas que morrem esperando cirurgia, exame, consulta, UTI."),
        new DeathCost(PreventableDeathCategory.CHILD_MORTALITY, "Mortalidade infantil (0-5 anos)",
            80_000, 40_000, 0.70, "Criancas que morrem antes dos 5 anos por falta de atendimento."),
        new DeathCost(PreventableDeathCategory.MATERNAL_DEATH, "Morte materna (no parto)",
            50_000, 1_800, 0.80, "Maes que morrem no parto por falta de estrutura hospitalar."),
        new DeathCost(PreventableDeathCategory.MALNUTRITION, "Desnutricao",
            15_000, 5_000, 0.90, "Pessoas que morrem de fome ou desnutricao grave no Brasil."),
        new DeathCost(PreventableDeathCategory.PREVENTABLE_DISEASE, "Doencas evitaveis (vacina/exame)",
            20_000, 50_000, 0.65, "Mortes por doencas que vacina ou exame precoce previniria."),
        new DeathCost(PreventableDeathCategory.VIOLENCE, "Violencia / Homicidio",
            300_000, 47_000, 0.40, "Jovens mortos por violencia. Programa social reduz 40%."),
        new DeathCost(PreventableDeathCategory.SUICIDE, "Suicidio (sem saude mental)",
            100_000, 14_000, 0.55, "Pessoas que se matam por falta de atendimento psicologico."),
        new DeathCost(PreventableDeathCategory.SANITATION, "Doenças por falta de saneamento",
            40_000, 8_000, 0.85, "Mortes por diarreia, leptospirose, hepatite por agua suja."),
        new DeathCost(PreventableDeathCategory.ROAD_DEATH, "Morte no transito",
            2_000_000, 30_000, 0.35, "Acidentes em estradas sem manutencao ou sinalizacao."),
        new DeathCost(PreventableDeathCategory.CANCER_UNTREATED, "Cancer sem tratamento a tempo",
            800_000, 35_000, 0.50, "Pessoas que morrem esperando tratamento de cancer no SUS."),
        new DeathCost(PreventableDeathCategory.HEART_UNTREATED, "Infarto sem atendimento",
            600_000, 100_000, 0.30, "Infartos que UTI/SAMU salvaria se chegasse a tempo."),
        new DeathCost(PreventableDeathCategory.NEONATAL, "Morte neonatal",
            120_000, 19_000, 0.65, "Bebe que morre nos primeiros 28 dias por falta de UTI neonatal.")
    );

    public static final List<CountryCreditor> COUNTRY_CREDITORS = Arrays.asList(
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
    );
}

class YearMortality {
    public final int year_label;
    public final double interest_paid_brl;
    public final double gdp_brl;
    public final int total_preventable_deaths;
    public final int deaths_linked_to_debt;
    public final int potential_lives_saved;
    public final int hospitals_not_built;
    public final int people_without_doctor;
    public final int children_not_vaccinated;
    public final int houses_not_built;
    public final int meals_not_served;
    public final int cumulative_deaths_by_debt;

    public YearMortality(int year_label, double interest_paid_brl, double gdp_brl,
                         int total_preventable_deaths, int deaths_linked_to_debt,
                         int potential_lives_saved, int hospitals_not_built,
                         int people_without_doctor, int children_not_vaccinated,
                         int houses_not_built, int meals_not_served,
                         int cumulative_deaths_by_debt) {
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

class CountryCreditor {
    public final String country;
    public final double amount_received_brl;
    public final String flag;
    public final String description;

    public CountryCreditor(String country, double amount_received_brl, String flag, String description) {
        this.country = country;
        this.amount_received_brl = amount_received_brl;
        this.flag = flag;
        this.description = description;
    }
}

class DebtMortalitySimulator {
    public final int start_year;
    public final int years;
    public final double initial_debt = 6.0e12;
    public final double initial_gdp = 10.0e12;
    public final double interest_rate = 0.12;
    public final double gdp_growth = 0.025;
    public final double population = 215e6;
    public final double fraction_to_health = 0.40;
    public final double fraction_to_food = 0.15;
    public final double fraction_to_housing = 0.15;
    public final double fraction_to_education = 0.15;
    public final double fraction_to_infra = 0.15;

    public List<YearMortality> simulations = new ArrayList<>();

    public DebtMortalitySimulator(int start_year, int years) {
        this.start_year = start_year;
        this.years = years;
    }

    public List<YearMortality> simulate() {
        simulations.clear();
        double debt = initial_debt;
        double gdp = initial_gdp;
        int cumulative_deaths = 0;

        for (int i = 0; i <= years; i++) {
            int year_label = start_year + i;
            double interest = debt * interest_rate;
            double money_for_health = interest * fraction_to_health;
            double money_for_food = interest * fraction_to_food;

            int potential_saved = 0;
            for (DeathCost dc : DebtMortalityData.DEATH_COSTS) {
                double lives_saved = money_for_health * 0.3 / dc.cost_to_save_one_life_brl;
                potential_saved += (int)lives_saved;
            }

            int total_preventable = 0;
            for (DeathCost dc : DebtMortalityData.DEATH_COSTS) {
                total_preventable += dc.deaths_preventable();
            }

            int deaths_by_debt = Math.min(potential_saved, total_preventable);

            int hospitals_not_built = (int)(money_for_health / 50e6);
            int people_without_doctor = (int)(money_for_health / 3_000);
            int children_not_vaccinated = (int)(money_for_health / 50);
            int houses_not_built = (int)(interest * fraction_to_housing / 80_000);
            int meals_not_served = (int)(money_for_food / 3);

            cumulative_deaths += deaths_by_debt;

            YearMortality sim = new YearMortality(
                year_label, interest, gdp, total_preventable, deaths_by_debt,
                potential_saved, hospitals_not_built, people_without_doctor,
                children_not_vaccinated, houses_not_built, meals_not_served, cumulative_deaths
            );
            simulations.add(sim);

            debt = debt + interest - (gdp * 0.18 * 0.3);
            gdp = gdp * (1 + gdp_growth);
        }
        return simulations;
    }

    public int total_deaths_by_debt() {
        return simulations.isEmpty() ? 0 : simulations.get(simulations.size()-1).cumulative_deaths_by_debt;
    }

    public double total_interest_paid() {
        double sum = 0;
        for (YearMortality s : simulations) sum += s.interest_paid_brl;
        return sum;
    }

    public double death_per_trillion_interest() {
        double total_int = total_interest_paid();
        if (total_int == 0) return 0;
        return total_deaths_by_debt() / (total_int / 1e12);
    }

    public Map<String, Object> summary() {
        YearMortality last = simulations.isEmpty() ? null : simulations.get(simulations.size()-1);
        Map<String, Object> res = new LinkedHashMap<>();
        res.put("years_simulated", years);
        res.put("total_deaths_by_debt", total_deaths_by_debt());
        res.put("total_interest_paid_trillions", total_interest_paid() / 1e12);
        res.put("deaths_per_trillion_interest", death_per_trillion_interest());
        res.put("avg_deaths_per_year", total_deaths_by_debt() / Math.max(1, years));
        res.put("final_year_hospitals_not_built", last != null ? last.hospitals_not_built : 0);
        res.put("final_year_meals_not_served", last != null ? last.meals_not_served : 0);
        res.put("final_year_children_not_vaccinated", last != null ? last.children_not_vaccinated : 0);
        return res;
    }
}

class OpenDebtMortality {
    public static String render_death_chart(List<YearMortality> simulations) {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\n");
        sb.append("  MORTES POR ANO CAUSADAS PELA DIVIDA\n");
        sb.append("  (pessoas que morreriam VIVAS se o juros fosse investido em saude)\n");
        sb.append("=".repeat(70)).append("\n\n");

        int max_deaths = 1;
        for (YearMortality s : simulations) if (s.deaths_linked_to_debt > max_deaths) max_deaths = s.deaths_linked_to_debt;
        if (max_deaths == 0) max_deaths = 1;

        for (YearMortality s : simulations) {
            int bar_len = (int)((s.deaths_linked_to_debt / (double)max_deaths) * 50);
            String bar = "#".repeat(Math.max(1, bar_len));
            sb.append(String.format("  %d |%s| %8d mortes\n", s.year_label, String.format("%-50s", bar), s.deaths_linked_to_debt));
        }
        sb.append("\n  Cada # representa ~").append(max_deaths/50).append(" mortes\n");
        sb.append("  TOTAL ACUMULADO: ").append(simulations.get(simulations.size()-1).cumulative_deaths_by_debt).append(" mortes\n");
        sb.append("  em ").append(simulations.size()-1).append(" anos\n\n");
        return sb.toString();
    }

    public static String render_country_deaths() {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\n");
        sb.append("  PARA QUEM O BRASIL PAGA -- E QUANTOS MORREM POR ISSO\n");
        sb.append("=".repeat(70)).append("\n\n");

        double total = 0;
        for (CountryCreditor c : DebtMortalityData.COUNTRY_CREDITORS) total += c.amount_received_brl;

        for (CountryCreditor c : DebtMortalityData.COUNTRY_CREDITORS) {
            double pct = (c.amount_received_brl / total) * 100;
            int deaths_caused = (int)(c.amount_received_brl / 500_000);
            int bar_len = (int)pct;
            String bar = "$".repeat(bar_len);
            sb.append(String.format("  %-15s R$ %6.0f bi/ano [%s] %5.1f%%  ~%d mortes\n",
                c.country, c.amount_received_brl/1e9, String.format("%-20s", bar), pct, deaths_caused));
        }
        sb.append("\n  TOTAL ENVIADO AO EXTERIOR: R$ ").append((int)(total/1e9)).append(" bilhoes/ano\n");
        sb.append("  MORTES CAUSADAS: ~").append((int)(total/500_000)).append(" por ano\n");
        sb.append("  Cada $ = R$ ").append(String.format("%.0f", total/20/1e9)).append(" bilhoes que sai do Brasil\n\n");
        sb.append("  Cada real enviado ao agiota international e uma vida\n");
        sb.append("  que NAO foi salva no Brasil.\n\n");
        return sb.toString();
    }

    public static String render_category_breakdown() {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\n");
        sb.append("  MORTES EVITAVEIS NO BRASIL (por categoria, por ano)\n");
        sb.append("=".repeat(70)).append("\n\n");

        int total_preventable = 0;
        for (DeathCost dc : DebtMortalityData.DEATH_COSTS) total_preventable += dc.deaths_preventable();

        sb.append(String.format("%-40s %12s %15s %12s\n", "CATEGORIA", "MORTES/ANO", "CUSTO/VIDA", "EVITAVEIS"));
        sb.append("-".repeat(80)).append("\n");

        for (DeathCost dc : DebtMortalityData.DEATH_COSTS) {
            sb.append(String.format("  %-38s %10d R$ %12.0f %10d\n",
                dc.name, dc.deaths_per_year_brazil, dc.cost_to_save_one_life_brl, dc.deaths_preventable()));
        }
        sb.append("-".repeat(80)).append("\n");
        int sumDeaths = 0; for (DeathCost dc : DebtMortalityData.DEATH_COSTS) sumDeaths += dc.deaths_per_year_brazil;
        sb.append(String.format("  %-38s %10d %15s %10d\n", "TOTAL", sumDeaths, "", total_preventable));
        sb.append("\n  Total de mortes evitaveis/ano: ").append(total_preventable).append("\n");
        sb.append("  Isso e ").append(String.format("%.0f", total_preventable/365.0)).append(" mortes POR DIA.\n");
        sb.append("  ").append(String.format("%.0f", total_preventable/365.0/24)).append(" mortes POR HORA.\n");
        sb.append("  ").append(String.format("%.1f", total_preventable/365.0/24/60)).append(" mortes POR MINUTO.\n\n");
        sb.append("  UMA PESSOA MORRE NO BRASIL A CADA MINUTO\n");
        sb.append("  POR ALGO QUE DINHEIRO RESOLVERIA.\n\n");
        sb.append("  E o dinheiro? FOI PRA O AGIOTA.\n\n");
        return sb.toString();
    }

    public static String render_lost_infrastructure(List<YearMortality> simulations) {
        YearMortality s = simulations.get(0);
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\n");
        sb.append("  O QUE O BRASIL NAO CONSTRUIU EM UM ANO\n");
        sb.append("  (").append(s.year_label).append(" -- R$ ").append(String.format("%.0f", s.interest_paid_brl/1e9)).append(" bi em juros)\n");
        sb.append("=".repeat(70)).append("\n\n");
        sb.append(String.format("  Hospitais nao construidos:        %8d\n", s.hospitals_not_built));
        sb.append(String.format("  Casas populares nao entregues:    %8d\n", s.houses_not_built));
        sb.append(String.format("  Pessoas sem medico de familia:    %8d\n", s.people_without_doctor));
        sb.append(String.format("  Criancas nao vacinadas:            %8d\n", s.children_not_vaccinated));
        sb.append(String.format("  Refeicoes nao servidas:            %8d\n", s.meals_not_served));
        sb.append("\n  Em UM ano, o juros da divida pagou:\n");
        sb.append("  - ").append(s.hospitals_not_built).append(" hospitais QUE NAO EXISTEM\n");
        sb.append("  - ").append(s.houses_not_built).append(" casas QUE NAO FORAM ENTREGUES\n");
        sb.append("  - ").append(s.meals_not_served).append(" refeicoes QUE NAO FORAM SERVIDAS\n\n");
        sb.append("  Cada hospital que nao existe = pessoas que morrem na fila.\n");
        sb.append("  Cada casa que nao foi entregue = familias na rua.\n");
        sb.append("  Cada refeicao que nao foi servida = criancas desnutridas.\n\n");
        return sb.toString();
    }

    public static String render_timeline_human(List<YearMortality> simulations) {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(70)).append("\n");
        sb.append("  LINHA DO TEMPO DA MORTE\n");
        sb.append("=".repeat(70)).append("\n\n");

        for (YearMortality s : simulations) {
            double deaths_per_day = s.deaths_linked_to_debt / 365.0;
            sb.append("  ").append(s.year_label).append(":\n");
            sb.append("    Juros pago: R$ ").append(String.format("%.0f", s.interest_paid_brl/1e9)).append(" bilhoes\n");
            sb.append("    Mortes causadas pela divida: ").append(s.deaths_linked_to_debt).append("\n");
            sb.append("    Isso sao ").append(String.format("%.0f", deaths_per_day)).append(" mortes POR DIA\n");
            sb.append("    Acumulado desde ").append(simulations.get(0).year_label).append(": ").append(s.cumulative_deaths_by_debt).append("\n\n");
        }
        YearMortality last = simulations.get(simulations.size()-1);
        sb.append("  Em ").append(simulations.size()-1).append(" anos, a divida causou a morte de:\n");
        sb.append("  ").append(last.cumulative_deaths_by_debt).append(" PESSOAS.\n\n");
        sb.append("  Isso e mais que a populacao de muitas cidades brasileiras.\n");
        sb.append("  Mais que todas as guerras do Brasil juntas.\n");
        sb.append("  Mais que todas as epidemias da historia recente.\n\n");
        sb.append("  E nao foi uma bala. Foi um BOLETO.\n\n");
        return sb.toString();
    }

    public static String render_narrative(List<YearMortality> simulations) {
        YearMortality s0 = simulations.get(0);
        YearMortality last = simulations.get(simulations.size()-1);
        int total = last.cumulative_deaths_by_debt;

        StringBuilder sb = new StringBuilder();
        sb.append("Vou te dizer algo que ninguem te conta. ");
        sb.append("No ano ").append(s0.year_label).append(", o Brasil pagou R$ ").append(String.format("%.0f", s0.interest_paid_brl/1e9)).append(" bilhoes apenas em JUROS da divida publica. ");
        sb.append("Esse dinheiro foi para bancos, fundos, paises estrangeiros. Nao foi para o SUS. Nao foi para a escola. Nao foi para a comida. ");
        sb.append("No mesmo ano, ").append(s0.deaths_linked_to_debt).append(" brasileiros morreram por causas evitaveis. Filas do SUS. Desnutricao. Falta de medico. ");
        sb.append("Se o dinheiro dos juros tivesse ido para a saude, ").append(s0.potential_lives_saved).append(" dessas pessoas poderiam estar VIVAS. ");
        sb.append("Em ").append(simulations.size()-1).append(" anos, se nada mudar, a divida tera causado a morte de ").append(total).append(" pessoas. ");
        sb.append(String.format("%.0f", total/365.0)).append(" mortes por dia. A cada minuto, alguem morre porque o dinheiro que salvaria sua vida foi para o agiota. ");
        sb.append("A divida nao e um numero. E um CEMITERIO. Cada parcela paga e uma cova que nao foi aberta. Cada juros pago e uma vida que nao foi salva. ");
        sb.append("A divida MATA.");
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("OpenDebtMortality -- Quantos Morrem Para Pagar a Divida?");
        System.out.println("=".repeat(70));

        DebtMortalitySimulator sim = new DebtMortalitySimulator(2024, 20);
        List<YearMortality> simulations = sim.simulate();

        System.out.print(render_category_breakdown());
        System.out.print(render_country_deaths());
        System.out.print(render_lost_infrastructure(simulations));
        System.out.print(render_death_chart(simulations));
        System.out.print(render_timeline_human(simulations));

        System.out.println("\n" + "=".repeat(70));
        System.out.println("NARRATIVA (para Telefonista ler)");
        System.out.println("=".repeat(70));
        System.out.println(render_narrative(simulations));

        Map<String, Object> summary = sim.summary();
        System.out.println("\n" + "=".repeat(70));
        System.out.println("RESUMO");
        System.out.println("=".repeat(70));
        System.out.println("  Anos simulados: " + summary.get("years_simulated"));
        System.out.println("  Total de mortes pela divida: " + summary.get("total_deaths_by_debt"));
        System.out.println("  Total de juros pagos: R$ " + String.format("%.1f", (double)summary.get("total_interest_paid_trillions")) + " trilhoes");
        System.out.println("  Mortes por R$ 1 trilhao de juros: " + String.format("%.0f", (double)summary.get("deaths_per_trillion_interest")));
        System.out.println("  Media de mortes/ano: " + String.format("%,.0f", (double)summary.get("avg_deaths_per_year")));

        System.out.println("\n" + "=".repeat(70));
        System.out.println("VEREDICTO");
        System.out.println("=".repeat(70));
        System.out.println();
        System.out.println("  A divida publica nao e apenas impossivel de pagar.");
        System.out.println("  Ela e um ASSASSINO DE MASSA silencioso.");
        System.out.println();
        System.out.println("  Em " + summary.get("years_simulated") + " anos:");
        System.out.println("  " + summary.get("total_deaths_by_debt") + " brasileiros morreram");
        System.out.println("  porque R$ " + String.format("%.1f", (double)summary.get("total_interest_paid_trillions")) + " trilhoes");
        System.out.println("  foram enviados ao agiota em vez de ir para saude, comida, vida.");
        System.out.println();
        System.out.println("  A divida MATA.");
        System.out.println("  Cada juros pago e uma vida nao salva.");
        System.out.println("  Nao renegociar. Nao alongar.");
        System.out.println("  EXTINGUIR.");
        System.out.println("  Pelas vidas que ainda podem ser salvas.");
        System.out.println();
        System.out.println("  'Nao existe pobreza, existe MISERIA.'");
        System.out.println("  A divida e a maquina que PRODUZ a miseria.");
    }
}