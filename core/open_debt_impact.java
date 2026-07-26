// OpenDebtImpact.java
// Transpilacao completa e fiel do Python open_debt_impact.py
// 15 ImpactArea + 5 SeverityLevel + 15 AreaImpact completos
// Todas as funcoes render + demo() como main()
// Comentarios em portugues mantidos

import java.util.*;

enum ImpactArea {
    EDUCATION("educacao"), HEALTH_MENTAL("saude_mental"), HOUSING("moradia"),
    FOOD_SECURITY("seguranca_alimentar"), INFRASTRUCTURE("infraestrutura"), SANITATION("saneamento"),
    SCIENCE_TECH("ciencia_tecnologia"), CULTURE_ARTS("cultura_arte"), INEQUALITY("desigualdade"),
    ENVIRONMENT("meio_ambiente"), SECURITY("seguranca"), SPORT("esporte"),
    TRANSPORT("transporte"), CONNECTIVITY("conectividade"), CHILDHOOD("infancia");
    public final String value; ImpactArea(String v){this.value=v;}
}

enum SeverityLevel {
    CRITICAL("critico"), SEVERE("severo"), HIGH("alto"), MODERATE("moderado"), LOW("baixo");
    public final String value; SeverityLevel(String v){this.value=v;}
}

class AreaImpact {
    ImpactArea area; String name; SeverityLevel severity;
    double annual_budget_needed_brl, annual_budget_actual_brl, annual_budget_gap_brl, pct_of_interest_that_should_go, unit_cost_brl;
    int people_affected_per_year, units_not_delivered_per_year;
    String unit_name, description, human_cost;
    AreaImpact(ImpactArea a,String n,SeverityLevel s,double nd,double ac,double gp,double pct,int pe,double uc,String un,int unot,String d,String h){
        area=a;name=n;severity=s;annual_budget_needed_brl=nd;annual_budget_actual_brl=ac;annual_budget_gap_brl=gp;
        pct_of_interest_that_should_go=pct;people_affected_per_year=pe;unit_cost_brl=uc;unit_name=un;
        units_not_delivered_per_year=unot;description=d;human_cost=h;
    }
}

class YearImpact {
    int year_label,total_people_affected,cumulative_people_affected;
    double interest_paid_brl,total_gap_brl,cumulative_gap_brl;
    Map<String,Map<String,Object>> area_details;
    YearImpact(int y,double i,double g,int p,Map<String,Map<String,Object>> d,double cg,int cp){
        year_label=y;interest_paid_brl=i;total_gap_brl=g;total_people_affected=p;area_details=d;cumulative_gap_brl=cg;cumulative_people_affected=cp;
    }
}

class ImpactSimulator {
    int start_year=2024,years=20;
    double initial_debt=6e12,initial_gdp=10e12,interest_rate=0.12,gdp_growth=0.025;
    List<YearImpact> simulations=new ArrayList<>();
    ImpactSimulator(int s,int y){start_year=s;years=y;}
    List<YearImpact> simulate(){
        simulations.clear();
        double debt=initial_debt,gdp=initial_gdp,cumG=0;int cumP=0;
        for(int i=0;i<=years;i++){
            int yl=start_year+i;double interest=debt*interest_rate;
            double tg=0;int tp=0;Map<String,Map<String,Object>> det=new HashMap<>();
            for(AreaImpact ai:OpenDebtImpact.AREA_IMPACTS){
                double inf=Math.pow(1.05,i);double gap=ai.annual_budget_gap_brl*inf;int units=(int)(gap/ai.unit_cost_brl);
                tg+=gap;tp+=ai.people_affected_per_year;
                Map<String,Object> m=new HashMap<>();
                m.put("name",ai.name);m.put("gap_brl",gap);m.put("people_affected",ai.people_affected_per_year);
                m.put("units_not_delivered",units);m.put("unit_name",ai.unit_name);m.put("severity",ai.severity.value);
                m.put("human_cost",ai.human_cost);m.put("gap_pct_of_interest",interest>0?gap/interest*100:0);
                det.put(ai.area.value,m);
            }
            cumG+=tg;cumP+=tp;
            simulations.add(new YearImpact(yl,interest,tg,tp,det,cumG,cumP));
            debt=debt+interest-(gdp*0.18*0.3);gdp*=(1+gdp_growth);
        }
        return simulations;
    }
    double total_gap_all_years(){return simulations.isEmpty()?0:simulations.get(simulations.size()-1).cumulative_gap_brl;}
    double total_interest_all_years(){return simulations.stream().mapToDouble(s->s.interest_paid_brl).sum();}
    Map<String,Object> summary(){
        Map<String,Object> m=new HashMap<>();
        m.put("years_simulated",years);m.put("total_gap_trillions",total_gap_all_years()/1e12);
        m.put("total_interest_trillions",total_interest_all_years()/1e12);
        m.put("avg_gap_per_year_trillions",(total_gap_all_years()/years)/1e12);
        m.put("areas_impacted",OpenDebtImpact.AREA_IMPACTS.size());
        m.put("total_people_per_year",simulations.isEmpty()?0:simulations.get(0).total_people_affected);
        return m;
    }
}

public class OpenDebtImpact {
    public static final List<AreaImpact> AREA_IMPACTS=Arrays.asList(
        new AreaImpact(ImpactArea.EDUCATION,"Educacao Basica e Superior",SeverityLevel.CRITICAL,600e9,180e9,420e9,0.15,50000000,5e6,"escolas",84000,"Educacao publica subfinanciada ha decadas.","Criancas em escolas sem teto, sem merenda, sem professor."),
        new AreaImpact(ImpactArea.HEALTH_MENTAL,"Saude Mental",SeverityLevel.SEVERE,80e9,4e9,76e9,0.03,20000000,200000,"CAPS",380000,"20M com transtorno mental.","Depressao. Suicidios. Sem psicologo."),
        new AreaImpact(ImpactArea.HOUSING,"Moradia Digna",SeverityLevel.CRITICAL,200e9,15e9,185e9,0.10,8000000,80000,"casas",2312500,"Deficit de 8M familias.","Familias em favelas. Sem-teto."),
        new AreaImpact(ImpactArea.FOOD_SECURITY,"Seguranca Alimentar",SeverityLevel.CRITICAL,120e9,35e9,85e9,0.08,33000000,3,"refeicoes",28333333333L,"33M passam fome.","Criancas desnutridas."),
        new AreaImpact(ImpactArea.INFRASTRUCTURE,"Infraestrutura",SeverityLevel.SEVERE,300e9,60e9,240e9,0.12,215000000,20000000,"km rodovia",12000,"Estradas esburacadas.","Acidentes. Apagoes."),
        new AreaImpact(ImpactArea.SANITATION,"Saneamento Basico",SeverityLevel.SEVERE,100e9,12e9,88e9,0.05,100000000,12000,"ligacoes",7333333,"Metade sem esgoto.","Diarreia. Dengue."),
        new AreaImpact(ImpactArea.SCIENCE_TECH,"Ciencia e Tecnologia",SeverityLevel.SEVERE,80e9,8e9,72e9,0.04,500000,500000,"bolsas",144000,"CNPq decapitado.","Pesquisadores no UBER."),
        new AreaImpact(ImpactArea.CULTURE_ARTS,"Cultura e Arte",SeverityLevel.HIGH,30e9,3e9,27e9,0.02,10000000,100000,"producoes",270000,"Cultura como luxo.","Teatros fechados."),
        new AreaImpact(ImpactArea.INEQUALITY,"Desigualdade",SeverityLevel.CRITICAL,500e9,50e9,450e9,0.15,150000000,500,"transferencias",900000000,"Gini 0.52.","1% tem 50%."),
        new AreaImpact(ImpactArea.ENVIRONMENT,"Meio Ambiente",SeverityLevel.SEVERE,50e9,5e9,45e9,0.03,215000000,100000,"km2",450000,"Amazonia queimando.","Agua acabando."),
        new AreaImpact(ImpactArea.SECURITY,"Seguranca Publica",SeverityLevel.SEVERE,150e9,70e9,80e9,0.05,60000000,2000000,"delegacias",40000,"47k homicidios/ano.","Maes chorando."),
        new AreaImpact(ImpactArea.SPORT,"Esporte e Lazer",SeverityLevel.MODERATE,20e9,2e9,18e9,0.01,40000000,300000,"quadras",60000,"Sem alternativa ao crime.","Talentos perdidos."),
        new AreaImpact(ImpactArea.TRANSPORT,"Transporte Publico",SeverityLevel.SEVERE,200e9,30e9,170e9,0.08,100000000,100000000,"km metro",1700,"3h/dia no onibus.","Estresse."),
        new AreaImpact(ImpactArea.CONNECTIVITY,"Conectividade",SeverityLevel.HIGH,40e9,5e9,35e9,0.02,70000000,5000,"conexoes",7000000,"70M sem internet.","Exclusao digital."),
        new AreaImpact(ImpactArea.CHILDHOOD,"Primeira Infancia",SeverityLevel.CRITICAL,80e9,8e9,72e9,0.04,12000000,1000000,"creches",72000,"12M sem creche.","Futuro comprometido."),
        new AreaImpact(ImpactArea.EDUCATION,"Educacao (extra)",SeverityLevel.LOW,1,1,0,0,0,1,"x",0,"","")
    );

    static String render_area_chart(List<YearImpact> sims){
        YearImpact s=sims.get(0);StringBuilder sb=new StringBuilder("\n"+ "=".repeat(75)+"\n  DEFICIT POR AREA -- "+s.year_label+" (R$ bilhoes)\n"+ "=".repeat(75)+"\n\n");
        List<Map.Entry<String,Map<String,Object>>> list=new ArrayList<>(s.area_details.entrySet());
        list.sort((a,b)->Double.compare((Double)b.getValue().get("gap_brl"),(Double)a.getValue().get("gap_brl")));
        double max=list.stream().mapToDouble(e->(Double)e.getValue().get("gap_brl")).max().orElse(1);
        for(var e:list){Map<String,Object> d=e.getValue();double gb=(Double)d.get("gap_brl")/1e9;int bl=(int)((Double)d.get("gap_brl")/max*40);String bar="X".repeat(Math.max(1,bl));
            sb.append(String.format("  %-35s R$%7.0fbi [%-40s] %s\n",d.get("name"),gb,bar,((String)d.get("severity")).toUpperCase().substring(0,4)));}
        sb.append("\n  TOTAL DEFICIT/ANO: R$ "+(s.total_gap_brl/1e9)+" bilhoes\n  PESSOAS AFETADAS/ANO: "+s.total_people_affected+"\n");
        return sb.toString();
    }

    static String render_human_cost(){
        StringBuilder sb=new StringBuilder("\n"+ "=".repeat(70)+"\n  O CUSTO HUMANO -- O QUE A DIVIDA DESTRÓI\n"+ "=".repeat(70)+"\n");
        for(AreaImpact ai:AREA_IMPACTS){
            sb.append("\n  "+ai.name.toUpperCase()+" ["+ai.severity.value.toUpperCase()+"]\n");
            sb.append(String.format("  Deficit: R$ %.0f bi/ano | Pessoas: %d/ano | Nao entregue: %d %s/ano\n",ai.annual_budget_gap_brl/1e9,ai.people_affected_per_year,ai.units_not_delivered_per_year,ai.unit_name));
            sb.append("  CUSTO HUMANO: "+ai.human_cost+"\n  "+"-".repeat(66)+"\n");
        }
        return sb.toString();
    }

    static String render_equivalence_table(){
        StringBuilder sb=new StringBuilder("\n"+ "=".repeat(70)+"\n  O QUE R$ 100 BILHOES DE JUROS ROUBOU\n"+ "=".repeat(70)+"\n");
        Object[][] eq={{"Escolas (R$5M)",100e9/5e6},{"Casas (R$80k)",100e9/8e4},{"Creches (R$1M)",100e9/1e6},{"CAPS (R$200k)",100e9/2e5},{"Bolsas pesquisa",100e9/5e5},{"Refeicoes (R$3)",100e9/3},{"Transferencias (R$500)",100e9/500}};
        for(Object[] e:sb.append(String.format("  %-30s %s\n","RECURSO","QTD")));for(Object[] e:eq){double q=(Double)e[1];String qs=q>=1e9?String.format("%.1f bi",q/1e9):q>=1e6?String.format("%.1f mi",q/1e6):String.format("%,.0f",q);sb.append(String.format("  %-30s %s\n",e[0],qs));}
        return sb.toString();
    }

    static String render_cumulative_chart(List<YearImpact> sims){
        StringBuilder sb=new StringBuilder("\n"+ "=".repeat(70)+"\n  DEFICIT ACUMULADO (R$ trilhoes)\n"+ "=".repeat(70)+"\n");
        double max=sims.get(sims.size()-1).cumulative_gap_brl;
        for(YearImpact s:sims){int bl=(int)(s.cumulative_gap_brl/max*50);sb.append(String.format("  %d |%s| R$ %.1fT\n",s.year_label,"#".repeat(Math.max(1,bl)),s.cumulative_gap_brl/1e12));}
        return sb.toString();
    }

    static String render_narrative(List<YearImpact> sims){
        YearImpact s0=sims.get(0),last=sims.get(sims.size()-1);
        return "Vou te mostrar o que a divida faz. Nao so matar. Mas DESTRUIR. Em "+s0.year_label+" o Brasil pagou R$ "+(s0.interest_paid_brl/1e9)+" bi em juros. Esse dinheiro deveria ter ido para 15 areas da sua vida. A divida MATA. E o que ela nao mata, ela DESTRÓI. Em "+last.year_label+" o deficit acumulado sera de R$ "+(last.cumulative_gap_brl/1e12)+" trilhoes.";
    }

    static void demo(){
        System.out.println("=".repeat(70)+"\nOpenDebtImpact -- Todos os Impactos da Divida\n"+ "=".repeat(70));
        ImpactSimulator sim=new ImpactSimulator(2024,20);List<YearImpact> sims=sim.simulate();
        System.out.println("\nAreas impactadas: "+AREA_IMPACTS.size());
        System.out.print(render_area_chart(sims));System.out.print(render_human_cost());
        System.out.print(render_equivalence_table());System.out.print(render_cumulative_chart(sims));
        System.out.println("\nNARRATIVA\n"+render_narrative(sims));
        Map<String,Object> sum=sim.summary();
        System.out.println("\nRESUMO\n  Deficit total: R$ "+sum.get("total_gap_trillions")+"T\n  Juros pagos: R$ "+sum.get("total_interest_trillions")+"T");
        System.out.println("\nVEREDICTO\nA divida MATA. E DESTRÓI. E CASTRA.\nNao renegociar. Nao alongar. EXTINGUIR.");
    }
    public static void main(String[] args){demo();}
}