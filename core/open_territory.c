/* OpenTerritory -- Redistribuicao Populacional e Novas Metropoles -- gerado de Portugol++ */
#ifndef OPENTERRITORY_REDISTRIBUICAO_POPULACIONAL_E_NOVAS_METROPOLES_H
#define OPENTERRITORY_REDISTRIBUICAO_POPULACIONAL_E_NOVAS_METROPOLES_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenTerritory -- Redistribuicao Populacional && Novas Metropoles;
=================================================================;
"Sao Paulo ! cabe mais gente. O interior ! tem gente alguma.;
A distribuicao esta ERRADA. A Republica CORRIGE.;
Esvaziar SP para obras. Construir infraestrutura em todo territorio.;
Novas metropoles onde hoje && 'interior'. Interior ! existe mais --;
so existe territorio nacional democraticamente ocupado.";
O QUE ISTO FAZ:;
1. MAPEIA densidade populacional atual (desigual);
2. DEFINE metas de redistribuicao;
3. CRIA novas metropoles em regioes estrategicas;
4. PLANEJA infraestrutura completa (saude, educacao, transporte, energia);
5. GERE o esvaziamento ordenado de SP/Rio (sem caos);
6. GARANTE que migrar && OPCIONAL mas incentivado;
O PROBLEMA:;
Sao Paulo: 12.3 milhoes em 1.521 km2 = 8.087 hab/km2;
Amazonas: 4.2 milhoes em 1.559.000 km2 = 2.7 hab/km2;
Desequilibrio: 3.000x entre extremos;
Metropoles saturadas: SP, Rio, BH, Brasilia, Fortaleza, Salvador;
Vazios demograficos: Centro-Oeste, Norte, sertao nordestino, sul profundo;
A SOLUCAO:;
50+ novas metropoles espalhadas pelo territorio;
Cada nova metropolis: 500k-2M habitantes;
Infraestrutura nivel Sirio-Libanes (OpenHealthcareAccess);
Tudo conectado (OpenNetwork, OpenMobility, OpenProtocol);
ZERAR o conceito de "interior" -- todo ponto && centro;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime
// ============================================================================
// 1. DENSIDADE POPULACIONAL ATUAL (o problema)
// ============================================================================
typedef struct DensityClass {
    // Classificacao de densidade populacional.
    HYPER = "hiper_saturada"  // >5.000 hab/km2 (SP, Rio);
    SATURATED = "saturada"  // 1.000-5.000;
    ADEQUATE = "adequada"  // 100-1.000;
    LOW = "baixa"  // 10-100;
    EMPTY = "vazio"  // <10 hab/km2;
// decorador: @dataclass
typedef struct PopulationCenter {
    // Um centro populacional atual.
    name: texto;
    state: texto;
    region: texto;
    population: inteiro;
    area_km2: flutuante;
    double current_density = 0.0;
    double target_density = 0.0 // meta da Republica;
    char* status = "desconhecido"  // esvaziar, manter, crescer, criar;
    // decorador: @property
    DensityClass density_class(self) {
        d = self.current_density;
        if (d > 5000) {
            return DensityClass.HYPER;
        if (d > 1000) {
            return DensityClass.SATURATED;
        if (d > 100) {
            return DensityClass.ADEQUATE;
        if (d > 10) {
            return DensityClass.LOW;
        return DensityClass.EMPTY;
    // decorador: @property
    bool overpopulated(self) {
        return self.current_density > 2000;
    // decorador: @property
    bool underpopulated(self) {
        return self.current_density < 50;
    // decorador: @property
    int surplus_population(self) {
        // Quantas pessoas PRECISAM sair (se hiper).
        if (! self.overpopulated) {
            return 0;
        target = 2000 * self.area_km2 // meta: 2.000 hab/km2;
        return maximo(0, self.population - inteiro(target));
    // decorador: @property
    int capacity_to_grow(self) {
        // Quantas pessoas PODEM ir (se vazio).
        if (self.overpopulated) {
            return 0;
        target = 1000 * self.area_km2;
        return maximo(0, inteiro(target) - self.population);
// ============================================================================
// 2. NOVAS METROPOLES (a solucao)
// ============================================================================
typedef struct MetropolisTier {
    ALPHA = "alfa"  // 1M-2M habitantes (capital regional);
    BETA = "beta"  // 500k-1M (centro estadual);
    GAMMA = "gamma"  // 200k-500k (centro microrregional);
// decorador: @dataclass
typedef struct NewMetropolis {
    // Uma nova metropolis planejada.
    metro_id: texto;
    name: texto // nome novo (! existe ainda);
    state: texto;
    region: texto;
    coordinates: texto // aprox;
    tier: MetropolisTier;
    target_population: inteiro;
    int current_population = 0 // geralmente <50k (interior);
    double area_km2 = 500.0;
    // Infraestrutura planejada
    bool has_healthcare = false // nivel Sirio-Libanes;
    bool has_education = false // universidade + escolas;
    bool has_transport = false // OpenMobility (metro, VLT, aeroporto);
    bool has_energy = false // OpenEnergy (solar/eolica);
    bool has_network = false // OpenNetwork/OpenProtocol;
    bool has_fablab = false // FabLab industrial;
    bool has_terminal = false // OpenTerminal em todo estabelecimento;
    bool has_housing = false // OpenCivilConstruction;
    bool has_food_production = false // agricultura urbana periurbana;
    bool has_water = false // saneamento + reservatorio;
    // Status de construcao
    char* construction_phase = "planejamento"  // planejamento, obras, habitavel, ativa;
    double construction_progress = 0.0 // 0-1;
    int est_completion_months = 36;
    // Atrativos (por que morar aqui?)
    [texto] incentives = field(default_factory=list);
    // decorador: @property
    bool infrastructure_ready(self) {
        return all([self.has_healthcare, self.has_education,;
                    self.has_transport, self.has_energy,;
                    self.has_network, self.has_fablab,;
                    self.has_terminal, self.has_housing,;
                    self.has_food_production, self.has_water]);
    // decorador: @property
    bool ready_for_habitation(self) {
        return self.infrastructure_ready && self.construction_progress >= 0.8;
// ============================================================================
// 3. DEFINIR NOVAS METROPOLES POR REGIAO
// ============================================================================
[NewMetropolis] _build_new_metroplan(void) {
    // Plano de 50+ novas metropoles pelo Brasil.
    metros = [];
    // === NORTE (desbloquear Amazonia com sustentabilidade) ===
    metros.append(NewMetropolis("NM-01", "Nova Manaus", "AM", "Norte",;
        "-3.1, -60.0", MetropolisTier.BETA, 800000, area_km2=800));
    metros.append(NewMetropolis("NM-02", "Porto Sustentavel", "PA", "Norte",;
        "-1.4, -48.4", MetropolisTier.ALPHA, 1200000, area_km2=1000));
    metros.append(NewMetropolis("NM-03", "Centro Rondonia", "RO", "Norte",;
        "-10.8, -63.3", MetropolisTier.GAMMA, 300000, area_km2=500));
    metros.append(NewMetropolis("NM-04", "Acre Tecnopolo", "AC", "Norte",;
        "-9.9, -67.8", MetropolisTier.GAMMA, 250000, area_km2=400));
    // === NORDESTE (desconcentrar do litoral para o sertao) ===
    metros.append(NewMetropolis("NM-05", "Sertao Central", "CE", "Nordeste",;
        "-5.0, -40.0", MetropolisTier.BETA, 600000, area_km2=600));
    metros.append(NewMetropolis("NM-06", "Trans-Sao Francisco", "BA", "Nordeste",;
        "-12.0, -41.0", MetropolisTier.BETA, 700000, area_km2=700));
    metros.append(NewMetropolis("NM-07", "Picos Sertao", "PI", "Nordeste",;
        "-7.0, -41.4", MetropolisTier.GAMMA, 250000, area_km2=400));
    metros.append(NewMetropolis("NM-08", "Serido Potiguar", "RN", "Nordeste",;
        "-6.5, -37.0", MetropolisTier.GAMMA, 200000, area_km2=300));
    metros.append(NewMetropolis("NM-09", "Sertao Pernambucano", "PE", "Nordeste",;
        "-8.6, -37.7", MetropolisTier.GAMMA, 300000, area_km2=400));
    metros.append(NewMetropolis("NM-10", "Centro Maranhense", "MA", "Nordeste",;
        "-5.0, -45.0", MetropolisTier.BETA, 500000, area_km2=500));
    metros.append(NewMetropolis("NM-11", "Alto Sertao Sergipano", "SE", "Nordeste",;
        "-10.3, -37.6", MetropolisTier.GAMMA, 150000, area_km2=250));
    metros.append(NewMetropolis("NM-12", "Sertao Paraibano", "PB", "Nordeste",;
        "-7.2, -37.5", MetropolisTier.GAMMA, 200000, area_km2=300));
    // === CENTRO-OESTE (povoar o centro do pais) ===
    metros.append(NewMetropolis("NM-13", "Centro-Matogrossense", "MT", "Centro-Oeste",;
        "-14.0, -55.0", MetropolisTier.ALPHA, 1000000, area_km2=900));
    metros.append(NewMetropolis("NM-14", "Norte Goiano", "GO", "Centro-Oeste",;
        "-13.0, -49.0", MetropolisTier.BETA, 600000, area_km2=600));
    metros.append(NewMetropolis("NM-15", "Sul Mato-Grossense", "MS", "Centro-Oeste",;
        "-21.0, -55.0", MetropolisTier.BETA, 500000, area_km2=500));
    metros.append(NewMetropolis("NM-16", "Tocantins Central", "TO", "Centro-Oeste",;
        "-10.0, -48.0", MetropolisTier.BETA, 400000, area_km2=500));
    // === SUDESTE (desconcentrar de SP/Rio) ===
    metros.append(NewMetropolis("NM-17", "Alta Mogiana", "SP", "Sudeste",;
        "-20.7, -47.0", MetropolisTier.BETA, 700000, area_km2=500));
    metros.append(NewMetropolis("NM-18", "Vale do Ribeira", "SP", "Sudeste",;
        "-24.5, -48.5", MetropolisTier.GAMMA, 300000, area_km2=400));
    metros.append(NewMetropolis("NM-19", "Norte Mineiro", "MG", "Sudeste",;
        "-16.0, -43.0", MetropolisTier.BETA, 500000, area_km2=600));
    metros.append(NewMetropolis("NM-20", "Triangulo Expandido", "MG", "Sudeste",;
        "-19.0, -48.0", MetropolisTier.BETA, 600000, area_km2=500));
    metros.append(NewMetropolis("NM-21", "Noroeste Fluminense", "RJ", "Sudeste",;
        "-21.8, -41.5", MetropolisTier.GAMMA, 250000, area_km2=350));
    metros.append(NewMetropolis("NM-22", "Norte Capixaba", "ES", "Sudeste",;
        "-19.0, -40.5", MetropolisTier.GAMMA, 300000, area_km2=350));
    // === SUL (povoar o interior profundo) ===
    metros.append(NewMetropolis("NM-23", "Centro Paranaense", "PR", "Sul",;
        "-24.5, -51.5", MetropolisTier.BETA, 600000, area_km2=550));
    metros.append(NewMetropolis("NM-24", "Oeste Catarinense", "SC", "Sul",;
        "-26.7, -52.0", MetropolisTier.BETA, 500000, area_km2=450));
    metros.append(NewMetropolis("NM-25", "Norte Gaucho", "RS", "Sul",;
        "-28.0, -52.5", MetropolisTier.BETA, 600000, area_km2=550));
    metros.append(NewMetropolis("NM-26", "Campanha Gaucha", "RS", "Sul",;
        "-31.0, -54.5", MetropolisTier.GAMMA, 250000, area_km2=400));
    metros.append(NewMetropolis("NM-27", "Sul Paranaense", "PR", "Sul",;
        "-26.0, -53.0", MetropolisTier.GAMMA, 300000, area_km2=350));
    return metros;
// ============================================================================
// 4. MOTOR DE REDISTRIBUICAO TERRITORIAL
// ============================================================================
typedef struct TerritoryEngine {
    // Motor que reorganiza a ocupacao do territorio nacional.
    PROCESSO:;
    1. DIAGNOSTICO: onde tem gente demais vs de menos;
    2. PLANO: onde criar novas metropoles;
    3. CONSTRUCAO: infraestrutura completa antes de migrar;
    4. MIGRACAO: voluntaria, incentivada, assistida;
    5. RECALIBRAGEM: monitora densidade, ajusta;
    PRINCIPIOS:;
    - Migrar && OPCIONAL (P2 autonomia). Ninguem && forcado.;
    - Mas && FORTEMENTE incentivado (credito, moradia, infraestrutura);
    - SP ! && abandonada -- && REFORMADA (obras enquanto esvazia);
    - Novas metropoles tem TUDO antes de receber gente;
    - "Interior" deixa de existir como conceito;
    //
    void __init__(self) {
        self.current_centers: {texto: PopulationCenter} = {};
        self.new_metropolises: {texto: NewMetropolis} = {
            m.metro_id: m para m em _build_new_metroplan();
        };
        self.migrations: [Dict] = [];
        self._init_current_population();
    void _init_current_population(self) {
        // Dados populacionais atuais (desequilibrio).
        centers = [;
            ("Sao Paulo", "SP", "Sudeste", 12325000, 1521),;
            ("Rio de Janeiro", "RJ", "Sudeste", 6747815, 1182),;
            ("Brasilia", "DF", "Centro-Oeste", 3055149, 5760),;
            ("Salvador", "BA", "Nordeste", 2886698, 693),;
            ("Fortaleza", "CE", "Nordeste", 2686612, 314),;
            ("Belo Horizonte", "MG", "Sudeste", 2521564, 331),;
            ("Manaus", "AM", "Norte", 2219580, 11401),;
            ("Curitiba", "PR", "Sul", 1963726, 435),;
            ("Recife", "PE", "Nordeste", 1661017, 218),;
            ("Porto Alegre", "RS", "Sul", 1488252, 496),;
            ("Belem", "PA", "Norte", 1499641, 1059),;
            ("Goiania", "GO", "Centro-Oeste", 1549750, 739),;
            // Vazios
            ("Amazonas Interior", "AM", "Norte", 2000000, 1547000),;
            ("Sertao Nordestino", "Multi", "Nordeste", 5000000, 800000),;
            ("Centro-Oeste Rural", "Multi", "Centro-Oeste", 1500000, 500000),;
            ("Pampa Gaucho", "RS", "Sul", 300000, 100000),;
        ];
        /* para name, state, region, pop, area in centers: */
            c = PopulationCenter(name, state, region, pop, area,;
                                current_density = pop / area,;
                                target_density = 1500);
            c.status = ("esvaziar" if c.overpopulated else;
                        c.underpopulated ? "crescer" : "manter");
            self.current_centers[name] = c;
    {texto: qualquer} diagnosis(self) {
        // Diagnostico do desequilibrio territorial.
        hyper = [c para c em self.current_centers.values();
                if c.density_class == DensityClass.HYPER];
        saturated = [c para c em self.current_centers.values();
                    if c.density_class == DensityClass.SATURATED];
        empty = [c para c em self.current_centers.values();
                if c.density_class in (DensityClass.EMPTY, DensityClass.LOW)];
        total_surplus = soma(c.surplus_population para c em hyper);
        return {;
            "hiper_saturadas": sizeof(hyper),;
            "saturadas": sizeof(saturated),;
            "vazios_demograficos": sizeof(empty),;
            "populacao_excedente": total_surplus,;
            "pior_caso": {
                hyper ? "nome": hyper[0].name : "N/A",;
                hyper ? "densidade": "{hyper[0].current_density:.0f} hab/km2" : "N/A",;
                hyper ? "excedente": "{hyper[0].surplus_population:,}" : "0",;
            },;
            "desequilibrio": (;
                "{max(c.current_density for c in self.current_centers.values()):.0f} vs ";
                "{min(c.current_density for c in self.current_centers.values()):.1f} hab/km2";
            ),;
        };
    {texto: qualquer} new_metroplan_summary(self) {
        // Resumo do plano de novas metropoles.
        by_region = Counter(m.region para m em self.new_metropolises.values());
        by_tier = Counter(m.tier.value para m em self.new_metropolises.values());
        total_capacity = soma(m.target_population para m em self.new_metropolises.values());
        return {;
            "total_novas_metropoles": sizeof(self.new_metropolises),;
            "capacidade_total": total_capacity,;
            "por_regiao": dict(by_region),;
            "por_tier": dict(by_tier),;
            "alfa_1m_2m": soma(1 para m em self.new_metropolises.values();
                            if m.tier == MetropolisTier.ALPHA),;
            "beta_500k_1m": soma(1 para m em self.new_metropolises.values();
                                if m.tier == MetropolisTier.BETA),;
            "gamma_200k_500k": soma(1 para m em self.new_metropolises.values();
                                if m.tier == MetropolisTier.GAMMA),;
        };
    {texto: qualquer} build_infrastructure(self, metro_id: texto) {
        // Constroi TODA infraestrutura antes de receber populacao.
        metro = self.new_metropolises.get(metro_id);
        if (! metro) {
            return {"error": "Metropolis ! encontrada"};
        // Tudo construido em paralelo (OpenCivilConstruction + OpenLaborRelay)
        metro.has_healthcare = true // Hospital nivel Sirio-Libanes;
        metro.has_education = true // Universidade + escolas;
        metro.has_transport = true // Metro/VLT + OpenMobility;
        metro.has_energy = true // Solar + eolica (OpenEnergy);
        metro.has_network = true // OpenNetwork/OpenProtocol;
        metro.has_fablab = true // Distrito industrial;
        metro.has_terminal = true // OpenTerminal em todo lugar;
        metro.has_housing = true // OpenCivilConstruction;
        metro.has_food_production = true // Agricultura periurbana;
        metro.has_water = true // Saneamento + reservatorio;
        metro.construction_phase = "habitavel";
        metro.construction_progress = 1.0;
        metro.incentives = [;
            "Moradia ZERO custo (OpenKit + OpenCivilConstruction)",;
            "Saude nivel Sirio-Libanes",;
            "Universidade gratis (OpenEducation)",;
            "Transporte publico (OpenMobility)",;
            "FabLab para criar/trabalhar",;
            "OpenTerminal em todo estabelecimento",;
            "Credito inicial 15 (piso da assembleia)",;
            "Agricultura urbana (autossuficiencia alimentar)",;
            "100% energia renovavel",;
            "Internet livre (OpenNetwork)",;
        ];
        return {;
            "built": true,;
            "metro": metro.name,;
            "ready": metro.ready_for_habitation,;
            "infrastructure": "COMPLETA (10/10 servicos)",;
            "incentives": metro.incentives,;
            "message": (;
                "{metro.name} esta PRONTA. ";
                "Tem hospital, universidade, transporte, energia, ";
                "FabLab, terminal, moradia, comida, agua, rede. ";
                "Tudo nivel Republica. Pode receber {metro.target_population:,} pessoas.";
            ),;
        };
    funcao offer_migration(self, citizen_id: texto, citizen_name: texto,
                        from_city: texto, to_metro_id: texto) -> {texto: qualquer}:;
        // Oferece migracao voluntaria com incentivos.
        metro = self.new_metropolises.get(to_metro_id);
        if (! metro) {
            return {"error": "Destino ! encontrado"};
        city = self.current_centers.get(from_city);
        if (! city || ! city.overpopulated) {
            from_status = "! saturada (migracao permitida mas sem bonus)";
            bonus = 0;
        } else {
            from_status = "SATURADA ({city.current_density:.0f} hab/km2)";
            bonus = 20 // credito extra por sair de cidade saturada;
        self.migrations.append({
            "citizen": citizen_name,;
            "from": from_city,;
            "to": metro.name,;
            "date": datetime.now().isoformat(),;
            "bonus_credit": bonus,;
        });
        return {;
            "offered": true,;
            "citizen": citizen_name,;
            "from": from_city,;
            "from_status": from_status,;
            "to": metro.name,;
            "to_region": metro.region,;
            "incentives": metro.incentives[:6],;
            "bonus_credit": bonus,;
            "voluntary": true,;
            "forced": false,;
            "message": (;
                "{citizen_name}, a Republica oferece: sair de {from_city} ";
                "&& morar em {metro.name} ({metro.region}). ";
                "Moradia ZERO. Saude Sirio-Libanes. Universidade. ";
                "Transporte. FabLab. Credito +{bonus}. ";
                "OPCIONAL. Sua escolha (P2 autonomia).";
            ),;
        };
    {texto: qualquer} stats(self) {
        diag = self.diagnosis();
        plan = self.new_metroplan_summary();
        built = soma(1 para m em self.new_metropolises.values();
                    if m.construction_progress >= 1.0);
        return {;
            "diagnostico": diag,;
            "plano": plan,;
            "construidas": built,;
            "migracoes_oferecidas": sizeof(self.migrations),;
            "total_metropoles": sizeof(self.new_metropolises),;
        };
// ============================================================================
// 5. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = TerritoryEngine();
    printf("=" * 80);
    printf("  OPENTERRITORY -- REDISTRIBUICAO POPULACIONAL E NOVAS METROPOLES");
    printf("  'SP ta pequeno demais. O interior ! existe mais.'");
    printf("=" * 80);
    // === 1. DIAGNOSTICO ===
    printf("\n\n  === 1. DIAGNOSTICO: DESEQUILIBRIO TERRITORIAL ===\n");
    printf("  {'Cidade':<25} {'Regiao':<15} {'Populacao':>12} {'Densidade':>12} {'Status'}");
    printf("  {'-'*80}");
    /* para c em ordene(engine.current_centers.values(), */
                    key = (x) -> -x.current_density):;
        printf("  {c.name:<25} {c.region:<15} {c.population:>12,} ";
            "{c.current_density:>10.0f}/km2  {c.status.upper()}");
    // === 2. DESEQUILIBRIO ===
    printf("\n\n  === 2. O PROBLEMA ===\n");
    diag = engine.diagnosis();
    printf("  Hiper-saturadas: {diag['hiper_saturadas']}");
    printf("  Saturadas: {diag['saturadas']}");
    printf("  Vazios demograficos: {diag['vazios_demograficos']}");
    printf("  Populacao excedente (precisa sair): {diag['populacao_excedente']:,}");
    printf("  Pior caso: {diag['pior_caso']['nome']} ";
        "({diag['pior_caso']['densidade']}, ";
        "excedente: {diag['pior_caso']['excedente']})");
    printf("  Desequilibrio: {diag['desequilibrio']}");
    // === 3. PLANO DE NOVAS METROPOLES ===
    printf("\n\n  === 3. PLANO: {len(engine.new_metropolises)} NOVAS METROPOLES ===\n");
    plan = engine.new_metroplan_summary();
    printf("  Por regiao:");
    /* para cada (region, count) em ordene(plan["por_regiao"].items()): */
        printf("    {region:<15} {count} metropoles");
    printf("\n  Por sizeof:");
    printf("    ALPHA (1M-2M):    {plan['alfa_1m_2m']}");
    printf("    BETA (500k-1M):   {plan['beta_500k_1m']}");
    printf("    GAMMA (200k-500k):{plan['gamma_200k_500k']}");
    printf("\n  Capacidade total: {plan['capacidade_total']:,} habitantes");
    // === 4. TODAS AS NOVAS METROPOLES ===
    printf("\n\n  === 4. NOVAS METROPOLES POR REGIAO ===\n");
    by_region = defaultdict(list);
    /* TODO: iterador C manual para m em engine.new_metropolises.values() */
        by_region[m.region].append(m);
    /* TODO: iterador C manual para region em ordene(by_region.keys()) */
        printf("\n  {region.upper()}:");
        /* TODO: iterador C manual para m em by_region[region] */
            printf("    [{m.metro_id}] {m.name:<25} {m.state}  ";
                "meta: {m.target_population:,}  ({m.tier.value})");
    // === 5. CONSTRUIR INFRAESTRUTURA ===
    printf("\n\n  === 5. CONSTRUCAO DE INFRAESTRUTURA ===\n");
    // Construir todas
    /* TODO: iterador C manual para mid em list(engine.new_metropolises.keys()) */
        result = engine.build_infrastructure(mid);
    printf("  {len(engine.new_metropolises)} metropoles construidas.");
    printf("  Cada uma tem:");
    printf("    [OK] Hospital nivel Sirio-Libanes");
    printf("    [OK] Universidade + escolas");
    printf("    [OK] Metro/VLT + OpenMobility");
    printf("    [OK] Energia solar/eolica");
    printf("    [OK] OpenNetwork/OpenProtocol");
    printf("    [OK] FabLab industrial");
    printf("    [OK] OpenTerminal em todo lugar");
    printf("    [OK] Moradia (OpenCivilConstruction)");
    printf("    [OK] Agricultura periurbana");
    printf("    [OK] Saneamento + agua");
    // === 6. MIGRACAO VOLUNTARIA ===
    printf("\n\n  === 6. MIGRACAO VOLUNTARIA (com incentivos) ===\n");
    migrations = [;
        ("C-001", "Maria", "Sao Paulo", "NM-17"),;
        ("C-002", "Joao", "Sao Paulo", "NM-19"),;
        ("C-003", "Ana", "Rio de Janeiro", "NM-21"),;
        ("C-004", "Pedro", "Fortaleza", "NM-05"),;
        ("C-005", "Beatriz", "Salvador", "NM-06"),;
    ];
    /* para cid, name, from_city, to_metro in migrations: */
        result = engine.offer_migration(cid, name, from_city, to_metro);
        printf("\n  {result['citizen']} de {result['from']} -> {result['to']}");
        printf("    Status saida: {result['from_status']}");
        printf("    Bonus: +{result['bonus_credit']} credito");
        printf("    Voluntario: SIM (P2)");
    // === 7. SP SENDO ESVAZIADA PARA OBRAS ===
    printf("\n\n  === 7. SAO PAULO: ESVAZIAR PARA REFORMAR ===\n");
    sp = engine.current_centers.get("Sao Paulo");
    if (sp) {
        printf("  ANTES:");
        printf("    Populacao: {sp.population:,}");
        printf("    Densidade: {sp.current_density:.0f} hab/km2");
        printf("    Excedente: {sp.surplus_population:,} pessoas precisam sair");
        printf("\n  DEPOIS (meta):");
        printf("    Populacao meta: {int(2000 * sp.area_km2):,}");
        printf("    Densidade meta: 2.000 hab/km2 (ainda urbano, mas respiravel)");
        printf("    Reducao: {sp.surplus_population:,} pessoas ({sp.surplus_population/sp.population*100:.0f}%)");
        printf("\n  O QUE FAZER COM ESPACO LIBERADO:");
        printf("    - Reformar infraestrutura antiga");
        printf("    - Criar espacos verdes");
        printf("    - Reconstruir moradias dignas");
        printf("    - Reduzir transito");
        printf("    - Limpar rios (Tiete, Pinheiros)");
        printf("    - Descongestionar hospitais");
    // === 8. STATS ===
    printf("\n\n  === 8. ESTATISTICAS ===\n");
    s = engine.stats();
    printf("  Novas metropoles: {s['total_metropoles']}");
    printf("  Construidas: {s['construidas']}");
    printf("  Migracoes oferecidas: {s['migracoes_oferecidas']}");
    printf("  Capacidade total: {s['plano']['capacidade_total']:,}");
    printf("  Populacao excedente: {s['diagnostico']['populacao_excedente']:,}");
    // === FILOSOFIA ===
    printf("\n\n{'='*80}");
    printf("  FILOSOFIA DO OPENTERRITORY");
    printf("{'='*80}");
    printf(""";
O PROBLEMA:;
    Sao Paulo: 8.087 hab/km2 (! cabe mais NINGUEM);
    Sertao: 6 hab/km2 (vazio);
    Desequilibrio: 1.300x;
    Metropoles saturadas ! funcionam:;
    - Transito caotico;
    - Hospitais colapsados;
    - Moradia digna IMPOSSIVEL (R$ 3.000 aluguel);
    - Poluicao;
    - Violencia;
    - Fila para TUDO;
A SOLUCAO:;
    27 novas metropoles espalhadas pelo territorio.;
    Cada uma com:;
    - Hospital nivel Sirio-Libanes (antes so SP tinha);
    - Universidade (antes so capitais tinham);
    - Metro/VLT (antes so SP/Rio tinham);
    - FabLab (distrito industrial);
    - OpenTerminal em todo estabelecimento;
    - Moradia ZERO (OpenCivilConstruction);
    - Energia renovavel;
    - Agricultura periurbana;
    Capcidade total: {s['plano']['capacidade_total']:,} pessoas;
    Populacao excedente: {s['diagnostico']['populacao_excedente']:,};
"INTERIOR" DEIXA DE EXISTIR:;
    Nao ha mais "interior". Nao ha "capitais vs cidades pequenas".;
    TODO ponto do territorio && CENTRO.;
    Todo centro tem nivel Sirio-Libanes.;
    Todo centro tem universidade.;
    Todo centro tem OpenNetwork.;
    A diferenca entre "capital" && "interior" && ZERO.;
MIGRACAO && OPCIONAL (P2):;
    Ninguem && OBRIGADO a sair de SP.;
    MAS && fortemente INCENTIVADO:;
    - Moradia ZERO;
    - Credito +20 (bonus por sair de saturada);
    - Mesma qualidade de servicos (|| melhor);
    - Mais espaco, menos caos, mais natureza;
SP ! && ABANDONADA:;
    SP && REFORMADA enquanto esvazia.;
    Quem fica tem:;
    - Mais espaco (menos gente);
    - Melhor infraestrutura (obras com espaco liberado);
    - Mais verde;
    - Menos transito;
    - Rios limpos;
    - Hospitais descongestionados;
PRINCIPIOS:;
    P1: Todo territorio tem mesma qualidade. Sem "capitais privilegiadas".;
    P2: Migrar && OPCIONAL. Incentivado, nunca forcado.;
    Construir novas metropoles P3 = trabalho massivo (OpenLaborRelay).;
    P4: Plano votado pela assembleia. Regioes decidem suas prioridades.;
// )
    printf("{'='*80}");
    printf("  OpenTerritory: {s['total_metropoles']} novas metropoles, ";
        "{s['plano']['capacidade_total']:,} de capacidade.");
    printf("  'Interior' ! existe mais. Todo ponto && centro.");
    printf("{'='*80}");

#endif // OPENTERRITORY_REDISTRIBUICAO_POPULACIONAL_E_NOVAS_METROPOLES_H
