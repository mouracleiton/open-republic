// OpenRepublic -- Simulacao de Entidades Prioritarias -- gerado de Portugol++
public class OpenrepublicSimulacaoDeEntidadesPrioritarias {

    // !/usr/bin/env python3
    //
    OpenRepublic -- Simulacao de Entidades Prioritarias;
    =====================================================;
    Hierarquia:;
    OpenRepublic (federacao de nacoes);
        -> OpenNation (nacoes membros, cada uma sem propriedade privada);
        -> Entidade (subconjuntos funcionais dentro de cada nacao);
    Uma OpenNation ! && um bloco homogeneo. && composta por ENTIDADES:;
    - Cada entidade && um grupo/infraestrutura/instituicao que presta;
        uma funcao essencial para a nacao.;
    - As entidades tem estados de saude, capacidade, && necessidade.;
    - A Republica precisa saber QUAIS entidades precisam de atencao;
        AGORA para priorizar alocacao de trabalho && recursos.;
    Esta simulacao identifica && prioriza as entidades mais criticas.;
    Author: OpenRepublic Team;
    //
    // importa annotations de __future__
    // importa math
    // importa random
    // importa dataclass, field de dataclasses
    // importa Any, Dict, List, Optional, Tuple, Set de typing
    // importa Enum de enum
    // importa defaultdict, deque de collections
    // importa numpy as np
    // ============================================================================
    // Entity Types (o que existe dentro de uma OpenNation)
    // ============================================================================
    public static class EntityType {
        // Producao
        FARM = "farm"  // producao de alimentos;
        AQUAPONICS = "aquaponics"  // peixe + planta integrados;
        FACTORY = "factory"  // manufatura (moveis, ferramentas, roupas);
        FABLAB = "fablab"  // fabricacao digital (3D System.out.println, CNC, laser);
        ENERGY_PLANT = "energy_plant"  // solar/eolica/hidro/fusao;
        WATER_TREATMENT = "water_treatment"  // tratamento + distribuicao agua;
        // Saude
        CLINIC = "clinic"  // atencao primaria;
        HOSPITAL = "hospital"  // atencao especializada;
        PHARMACY = "pharmacy"  // producao/distribuicao de remedios;
        MENTAL_HEALTH = "mental_health"  // saude mental coletiva;
        // Educacao
        SCHOOL = "school"  // educacao basica;
        UNIVERSITY = "university"  // educacao superior + pesquisa;
        LIBRARY = "library"  // conhecimento aberto;
        // Habitacao
        HOUSING_BLOCK = "housing_block"  // conjunto habitacional comunitario;
        // Logistica
        TRANSPORT_HUB = "transport_hub"  // centro de transporte compartilhado;
        DISTRIBUTION = "distribution"  // armazen + distribuicao de bens;
        // Social/Cultural
        COMMUNITY_CENTER = "community_center"  // espaco de convivencia;
        KITCHEN = "community_kitchen"  // cozinha comunitaria;
        CHILDCARE = "childcare"  // cuidado infantil;
        ELDER_CARE = "elder_care"  // cuidado de idosos;
        // Inovacao
        RESEARCH_LAB = "research_lab"  // laboratorio de pesquisa;
        DATA_CENTER = "data_center"  // computacao/armazenamento;
        QUANTUM_NODE = "quantum_node"  // no quantico da rede;
        // Ecologia
        FORESTRY = "forestry"  // manejo florestal;
        WASTE_RECYCLE = "waste_recycle"  // reciclagem + compostagem;
        ECO_RESTORATION = "eco_restoration"  // restauracao de ecossistemas;
    public static class UrgencyLevel {
        CRITICAL = 5 // colapso iminente -- vidas em risco;
        URGENT = 4 // funcionando precariamente, vai falhar em dias;
        ELEVATED = 3 // precisa de atencao em semanas;
        MODERATE = 2 // pode esperar, mas ! esquecer;
        STABLE = 1 // saudavel, continuar monitorando;
        THRIVING = 0 // acima do esperado, pode ajudar outras;
    public static class EntityStatus {
        OPERATIONAL = "operational";
        DEGRADED = "degraded"  // funcionando abaixo do ideal;
        CRITICAL = "critical"  // risco de colapso;
        OFFLINE = "offline"  // parou de funcionar;
        UNDER_CONSTRUCTION = "building";
        PLANNED = "planned"  // ainda ! existe, precisa ser criada;
    // ============================================================================
    // Entity Model
    // ============================================================================
    // decorador: @dataclass
    public static class Entity {
        // Uma entidade dentro de uma OpenNation.
        Cada entidade && um componente funcional da nacao.;
        Tem pessoas trabalhando, capacidade, estado de saude,;
        && necessidades especificas.;
        //
        entity_id: texto;
        name: texto;
        etype: EntityType;
        nation_id: texto;
        // Capacidade
        double capacity = 100.0 // unidades que pode produzir/atender por ciclo;
        double current_demand = 50.0 // demanda atual;
        int people_served = 0;
        int workers = 0;
        int workers_needed = 5;
        // Estado
        EntityStatus status = EntityStatus.OPERATIONAL;
        double health = 1.0 // 0=colapsou, 1=perfeito;
        double supply_level = 1.0 // 0=sem insumos, 1=abastecido;
        double maintenance_level = 1.0 // 0=precisa reparo urgente, 1=bem cuidado;
        // Dependencias (outras entidades que esta precisa para funcionar)
        {texto} depends_on = field(default_factory=set) // entity_ids;
        // Necessidades atuais
        [texto] needs = field(default_factory=list);
        // Historico
        [texto] last_issues = field(default_factory=list);
        // decorador: @property
        public double utilization(self) {
            // Quao sobrecarregada esta (0=solta, 1=no limite, >1=estourou).
            return self.current_demand / maximo(self.capacity, 1);
        // decorador: @property
        public UrgencyLevel urgency(self) {
            // Nivel de urgencia calculado automaticamente.
            if (self.status == EntityStatus.OFFLINE) {
                return UrgencyLevel.CRITICAL;
            if (self.status == EntityStatus.CRITICAL) {
                return UrgencyLevel.CRITICAL;
            if (self.health < 0.3 || self.supply_level < 0.2 || self.utilization > 1.5) {
                return UrgencyLevel.CRITICAL;
            if (self.health < 0.5 || self.supply_level < 0.4 || self.utilization > 1.2) {
                return UrgencyLevel.URGENT;
            if (self.health < 0.7 || self.supply_level < 0.6 || self.utilization > 1.0) {
                return UrgencyLevel.ELEVATED;
            if (self.health < 0.85 || self.workers < self.workers_needed) {
                return UrgencyLevel.MODERATE;
            if (self.utilization < 0.5) {
                return UrgencyLevel.THRIVING;
            return UrgencyLevel.STABLE;
        // decorador: @property
        public double risk_score(self) {
            // Score de risco 0-100 (100=colapso iminente).
            health_risk = (1 - self.health) * 40;
            supply_risk = (1 - self.supply_level) * 25;
            overload_risk = minimo(50, maximo(0, (self.utilization - 0.8) * 50));
            staff_risk = maximo(0, (self.workers_needed - self.workers) / maximo(self.workers_needed, 1)) * 20;
            maint_risk = (1 - self.maintenance_level) * 15;
            return arredonde(minimo(100, health_risk + supply_risk + overload_risk + staff_risk + maint_risk), 1);
        public {texto: qualquer} assess(self) {
            // Avaliacao completa da entidade.
            issues = [];
            recommendations = [];
            if (self.status == EntityStatus.OFFLINE) {
                issues.append("ENTIDADE PARADA");
                recommendations.append("Reativar imediatamente -- vidas afetadas");
            if (self.health < 0.3) {
                issues.append("Saude critica: {self.health:.0%}");
                recommendations.append("Manutencao de emergencia");
            if (self.supply_level < 0.3) {
                issues.append("Insumos criticos: {self.supply_level:.0%}");
                recommendations.append("Abastecer URGENTE");
            if (self.utilization > 1.3) {
                issues.append("Sobrecarga: {self.utilization:.0%} da capacidade");
                recommendations.append("Expandir capacidade || redistribuir demanda");
            if (self.workers < self.workers_needed) {
                deficit = self.workers_needed - self.workers;
                issues.append("Falta de trabalhadores: {deficit} pessoas");
                recommendations.append("Recrutar {deficit} pessoas com habilidades relevantes");
            if (self.maintenance_level < 0.5) {
                issues.append("Manutencao atrasada: {self.maintenance_level:.0%}");
                recommendations.append("Agendar manutencao preventiva");
            if (! issues) {
                issues.append("Operacao normal");
                recommendations.append("Manter monitoramento");
            return {;
                "entity_id": self.entity_id,;
                "name": self.name,;
                "type": self.etype.value,;
                "nation": self.nation_id,;
                "status": self.status.value,;
                "urgency": self.urgency.value,;
                "urgency_name": self.urgency.name,;
                "risk_score": self.risk_score,;
                "utilization": arredonde(self.utilization * 100, 0),;
                "health": arredonde(self.health * 100, 0),;
                "supply": arredonde(self.supply_level * 100, 0),;
                "workers": "{self.workers}/{self.workers_needed}",;
                "issues": issues,;
                "recommendations": recommendations,;
                "depends_on": list(self.depends_on),;
                "people_served": self.people_served,;
            };
    // ============================================================================
    // Nation (container of entities)
    // ============================================================================
    // decorador: @dataclass
    public static class NationState {
        // Estado de uma nacao dentro da Republica.
        nation_id: texto;
        name: texto;
        region: texto;
        population: inteiro;
        {texto: Entity} entities = field(default_factory=dict);
        public void add_entity(self, entity: Entity) {
            entity.nation_id = self.nation_id;
            self.entities[entity.entity_id] = entity;
        public [Entity] critical_entities(self) {
            // Entidades em estado critico.
            return ordene(;
                [&& para && em self.entities.values() if &&.urgency.value >= 4],;
                key = (&&) -> -&&.risk_score;
            );
        funcao all_by_urgency(self) retorna Dict[UrgencyLevel, [Entity]]:
            // Todas as entidades agrupadas por urgencia.
            groups = defaultdict(list);
            /* TODO: for-each Java para e em self.entities.values() */
                groups[&&.urgency].append(&&);
            /* TODO: for-each Java para level em groups */
                groups[level].sort(key=(&&) -> -&&.risk_score);
            return dict(groups);
        // decorador: @property
        public double avg_health(self) {
            if (! self.entities) {
                return 0;
            return arredonde(flutuante(np.mean([&&.health para && em self.entities.values()])), 2);
        // decorador: @property
        public double total_capacity_utilization(self) {
            if (! self.entities) {
                return 0;
            return arredonde(flutuante(np.mean([&&.utilization para && em self.entities.values()])), 2);
        // decorador: @property
        public int people_at_risk(self) {
            // Pessoas afetadas por entidades em risco.
            return soma(&&.people_served para && em self.entities.values() if &&.urgency.value >= 4);
    // ============================================================================
    // Republic (container of nations)
    // ============================================================================
    // decorador: @dataclass
    public static class RepublicState {
        // Estado da Republica completa.
        name: texto;
        {texto: NationState} nations = field(default_factory=dict);
        int cycle = 0;
        public void add_nation(self, nation: NationState) {
            self.nations[nation.nation_id] = nation;
        public [Entity] all_entities(self) {
            entities = [];
            /* TODO: for-each Java para n em self.nations.values() */
                entities.extend(n.entities.values());
            return entities;
        funcao priority_queue(self) retorna List[{texto: qualquer}]:
            // Fila de prioridade: quais entidades tratar AGORA.
            Ordenada por:;
            1. Urgencia (critico primeiro);
            2. Risk score (maior primeiro);
            3. Pessoas afetadas (mais pessoas primeiro);
            //
            entities = self.all_entities();
            scored = [];
            /* TODO: for-each Java para e em entities */
                assessment = &&.assess();
                // Composite priority score
                priority = (;
                    &&.urgency.value * 1000 +;
                    &&.risk_score * 10 +;
                    &&.people_served * 0.01;
                );
                scored.append((priority, assessment));
            scored.sort(key=(x) -> -x[0]);
            return [s[1] para s em scored];
        public {texto: qualquer} republic_health(self) {
            // Saude geral da Republica.
            all_entities = self.all_entities();
            if (! all_entities) {
                return {};
            by_urgency = defaultdict(inteiro);
            /* TODO: for-each Java para e em all_entities */
                by_urgency[&&.urgency.name] += 1;
            total_people_at_risk = soma(;
                &&.people_served para && em all_entities if &&.urgency.value >= 4;
            );
            total_people_served = soma(&&.people_served para && em all_entities);
            return {;
                "nations": tamanho(self.nations),;
                "total_entities": tamanho(all_entities),;
                "avg_health": arredonde(flutuante(np.mean([&&.health para && em all_entities])), 2),;
                "critical_count": by_urgency.get("CRITICAL", 0),;
                "urgent_count": by_urgency.get("URGENT", 0),;
                "elevated_count": by_urgency.get("ELEVATED", 0),;
                "stable_count": by_urgency.get("STABLE", 0) + by_urgency.get("THRIVING", 0),;
                "people_at_risk": total_people_at_risk,;
                "total_people_served": total_people_served,;
                "risk_coverage_pct": arredonde(;
                    total_people_at_risk / maximo(total_people_served, 1) * 100, 1;
                ),;
                "by_urgency": dict(by_urgency),;
            };
    // ============================================================================
    // Simulation Setup: The Republic at a Critical Moment
    // ============================================================================
    public RepublicState create_critical_scenario() {
        // Cria um cenario onde varias entidades precisam atencao AGORA.
        Cenario: A Republica esta no ciclo 18. Algumas nacoes estao;
        bem estabelecidas, outras sao recentes && tem gargalos.;
        O objetivo && identificar o que tratar primeiro.;
        //
        republic = RepublicState(name="Republica dos Bens Comuns", cycle=18);
        // === NATION 1: Amazonia (estabelecida, alguns gargalos) ===
        amazonia = NationState("N-AMZ", "Amazonia", "America do Sul", 50000);
        amazonia.add_entity(Entity(;
            "E-AMZ-CLINIC-01", "Clinica Central Manaus", EntityType.CLINIC, "N-AMZ",;
            capacity = 500, current_demand=720, people_served=5000, workers=8, workers_needed=12,;
            health = 0.45, supply_level=0.3, maintenance_level=0.6,;
            status = EntityStatus.DEGRADED,;
            depends_on = {"E-AMZ-PHARM-01"},;
            needs = ["medicamentos", "mais medicos", "ampliar espaço"],;
        ));
        amazonia.add_entity(Entity(;
            "E-AMZ-FARM-01", "Cooperativa Agricola Rio Negro", EntityType.FARM, "N-AMZ",;
            capacity = 10000, current_demand=8000, people_served=50000, workers=120, workers_needed=100,;
            health = 0.92, supply_level=0.85, maintenance_level=0.88,;
            status = EntityStatus.OPERATIONAL,;
        ));
        amazonia.add_entity(Entity(;
            "E-AMZ-PHARM-01", "Farmacia Comunitaria", EntityType.PHARMACY, "N-AMZ",;
            capacity = 2000, current_demand=2400, people_served=15000, workers=3, workers_needed=5,;
            health = 0.55, supply_level=0.25, maintenance_level=0.7,;
            status = EntityStatus.DEGRADED,;
            needs = ["reposicao de estoque"],;
        ));
        amazonia.add_entity(Entity(;
            "E-AMZ-ENERGY-01", "Microgrid Solar+Hidro", EntityType.ENERGY_PLANT, "N-AMZ",;
            capacity = 5000, current_demand=4200, people_served=50000, workers=6, workers_needed=8,;
            health = 0.88, supply_level=1.0, maintenance_level=0.82,;
            status = EntityStatus.OPERATIONAL,;
        ));
        amazonia.add_entity(Entity(;
            "E-AMZ-HOUSING-01", "Habitacao Comunitaria Bloco A", EntityType.HOUSING_BLOCK, "N-AMZ",;
            capacity = 5000, current_demand=6500, people_served=50000, workers=4, workers_needed=6,;
            health = 0.65, supply_level=0.9, maintenance_level=0.5,;
            status = EntityStatus.DEGRADED,;
            needs = ["construir mais 500 unidades", "reparar encanamento"],;
        ));
        amazonia.add_entity(Entity(;
            "E-AMZ-SCHOOL-01", "Centro de Aprendizagem", EntityType.SCHOOL, "N-AMZ",;
            capacity = 2000, current_demand=1800, people_served=8000, workers=40, workers_needed=35,;
            health = 0.90, supply_level=0.95, maintenance_level=0.85,;
            status = EntityStatus.OPERATIONAL,;
        ));
        amazonia.add_entity(Entity(;
            "E-AMZ-WATER-01", "Sistema de Agua + Tratamento", EntityType.WATER_TREATMENT, "N-AMZ",;
            capacity = 500000, current_demand=480000, people_served=50000, workers=5, workers_needed=5,;
            health = 0.75, supply_level=1.0, maintenance_level=0.60,;
            status = EntityStatus.OPERATIONAL,;
            needs = ["limpeza de filtros"],;
        ));
        amazonia.add_entity(Entity(;
            "E-AMZ-FORESTRY-01", "Manejo Florestal Sustentavel", EntityType.FORESTRY, "N-AMZ",;
            capacity = 100, current_demand=40, people_served=50000, workers=30, workers_needed=25,;
            health = 0.95, supply_level=1.0, maintenance_level=0.95,;
            status = EntityStatus.OPERATIONAL,;
        ));
        amazonia.add_entity(Entity(;
            "E-AMZ-RECYCLE-01", "Centro de Reciclagem", EntityType.WASTE_RECYCLE, "N-AMZ",;
            capacity = 500, current_demand=700, people_served=50000, workers=3, workers_needed=8,;
            health = 0.40, supply_level=0.6, maintenance_level=0.3,;
            status = EntityStatus.DEGRADED,;
            needs = ["maquinario de triagem", "mais trabalhadores"],;
        ));
        amazonia.add_entity(Entity(;
            "E-AMZ-DATA-01", "Datacenter Comunitario", EntityType.DATA_CENTER, "N-AMZ",;
            capacity = 100, current_demand=90, people_served=50000, workers=2, workers_needed=3,;
            health = 0.85, supply_level=0.9, maintenance_level=0.80,;
            status = EntityStatus.OPERATIONAL,;
        ));
        republic.add_nation(amazonia);
        // === NATION 2: Sahel (nova, gargalos graves) ===
        sahel = NationState("N-SAH", "Sahel", "Africa", 40000);
        sahel.add_entity(Entity(;
            "E-SAH-CLINIC-01", "Posto de Saude Oasis", EntityType.CLINIC, "N-SAH",;
            capacity = 200, current_demand=450, people_served=12000, workers=2, workers_needed=8,;
            health = 0.20, supply_level=0.10, maintenance_level=0.30,;
            status = EntityStatus.CRITICAL,;
            needs = ["medicamentos urgentes", "equipe medica", "agua potavel"],;
            depends_on = {"E-SAH-WATER-01"},;
        ));
        sahel.add_entity(Entity(;
            "E-SAH-WATER-01", "Poços + Dessalinizacao Solar", EntityType.WATER_TREATMENT, "N-SAH",;
            capacity = 80000, current_demand=200000, people_served=40000, workers=3, workers_needed=10,;
            health = 0.35, supply_level=0.15, maintenance_level=0.40,;
            status = EntityStatus.CRITICAL,;
            needs = ["construir mais pocos", "painéis solares", "bombeamento"],;
        ));
        sahel.add_entity(Entity(;
            "E-SAH-ENERGY-01", "Fazenda Solar Continental", EntityType.ENERGY_PLANT, "N-SAH",;
            capacity = 10000, current_demand=7500, people_served=40000, workers=15, workers_needed=20,;
            health = 0.85, supply_level=1.0, maintenance_level=0.80,;
            status = EntityStatus.OPERATIONAL,;
        ));
        sahel.add_entity(Entity(;
            "E-SAH-FARM-01", "Agricultura Seca + Hidroponia", EntityType.FARM, "N-SAH",;
            capacity = 3000, current_demand=5000, people_served=40000, workers=25, workers_needed=40,;
            health = 0.50, supply_level=0.30, maintenance_level=0.55,;
            status = EntityStatus.DEGRADED,;
            needs = ["sementes", "sistemas de irrigacao", "mais agricultores"],;
            depends_on = {"E-SAH-WATER-01"},;
        ));
        sahel.add_entity(Entity(;
            "E-SAH-HOUSING-01", "Habitacao Desertica", EntityType.HOUSING_BLOCK, "N-SAH",;
            capacity = 3000, current_demand=5000, people_served=40000, workers=2, workers_needed=8,;
            health = 0.55, supply_level=0.7, maintenance_level=0.50,;
            status = EntityStatus.DEGRADED,;
            needs = ["construcao de novas unidades", "refrigeracao passiva"],;
        ));
        sahel.add_entity(Entity(;
            "E-SAH-SCHOOL-01", "Centro Educativo Nomade", EntityType.SCHOOL, "N-SAH",;
            capacity = 800, current_demand=1200, people_served=5000, workers=5, workers_needed=15,;
            health = 0.60, supply_level=0.50, maintenance_level=0.65,;
            status = EntityStatus.DEGRADED,;
            needs = ["professores", "material didatico"],;
        ));
        sahel.add_entity(Entity(;
            "E-SAH-CHILD-01", "Cuidado Infantil Comunitario", EntityType.CHILDCARE, "N-SAH",;
            capacity = 100, current_demand=300, people_served=3000, workers=1, workers_needed=6,;
            health = 0.30, supply_level=0.40, maintenance_level=0.35,;
            status = EntityStatus.CRITICAL,;
            needs = ["espaco fisico", "cuidadores", "material"],;
        ));
        republic.add_nation(sahel);
        // === NATION 3: Nordica (estavel, pode ajudar) ===
        nordica = NationState("N-NOR", "Nordica", "Europa", 30000);
        nordica.add_entity(Entity(;
            "E-NOR-CLINIC-01", "Clinica Universal", EntityType.CLINIC, "N-NOR",;
            capacity = 600, current_demand=400, people_served=30000, workers=15, workers_needed=12,;
            health = 0.95, supply_level=0.98, maintenance_level=0.95,;
            status = EntityStatus.OPERATIONAL,;
        ));
        nordica.add_entity(Entity(;
            "E-NOR-ENERGY-01", "Parque Eolico + Fusion Node", EntityType.ENERGY_PLANT, "N-NOR",;
            capacity = 20000, current_demand=12000, people_served=30000, workers=20, workers_needed=18,;
            health = 0.98, supply_level=1.0, maintenance_level=0.97,;
            status = EntityStatus.OPERATIONAL,;
        ));
        nordica.add_entity(Entity(;
            "E-NOR-LAB-01", "Laboratorio Quantico", EntityType.RESEARCH_LAB, "N-NOR",;
            capacity = 50, current_demand=30, people_served=30000, workers=12, workers_needed=10,;
            health = 0.97, supply_level=0.95, maintenance_level=0.96,;
            status = EntityStatus.OPERATIONAL,;
        ));
        nordica.add_entity(Entity(;
            "E-NOR-DATA-01", "Datacenter Geotermico", EntityType.DATA_CENTER, "N-NOR",;
            capacity = 500, current_demand=350, people_served=30000, workers=8, workers_needed=6,;
            health = 0.96, supply_level=0.98, maintenance_level=0.94,;
            status = EntityStatus.OPERATIONAL,;
        ));
        nordica.add_entity(Entity(;
            "E-NOR-QUANTUM-01", "No Quantico Republica", EntityType.QUANTUM_NODE, "N-NOR",;
            capacity = 10, current_demand=8, people_served=200000, workers=4, workers_needed=5,;
            health = 0.90, supply_level=0.92, maintenance_level=0.88,;
            status = EntityStatus.OPERATIONAL,;
            needs = ["1 especialista em QKD"],;
        ));
        nordica.add_entity(Entity(;
            "E-NOR-HOUSING-01", "Habitacao Modular Boreal", EntityType.HOUSING_BLOCK, "N-NOR",;
            capacity = 12000, current_demand=10500, people_served=30000, workers=6, workers_needed=5,;
            health = 0.93, supply_level=1.0, maintenance_level=0.90,;
            status = EntityStatus.OPERATIONAL,;
        ));
        republic.add_nation(nordica);
        // === NATION 4: Pacifico (estavel mas isolada) ===
        pacifico = NationState("N-PAC", "Pacifico", "Oceania", 20000);
        pacifico.add_entity(Entity(;
            "E-PAC-ENERGY-01", "Geracao das Mars + Solar", EntityType.ENERGY_PLANT, "N-PAC",;
            capacity = 3000, current_demand=2800, people_served=20000, workers=4, workers_needed=6,;
            health = 0.80, supply_level=0.85, maintenance_level=0.72,;
            status = EntityStatus.OPERATIONAL,;
            needs = ["manutenção turbinas", "mais tecnicos"],;
        ));
        pacifico.add_entity(Entity(;
            "E-PAC-DIST-01", "Centro de Distribuicao Portuaria", EntityType.DISTRIBUTION, "N-PAC",;
            capacity = 10000, current_demand=14000, people_served=200000, workers=8, workers_needed=15,;
            health = 0.60, supply_level=0.50, maintenance_level=0.55,;
            status = EntityStatus.DEGRADED,;
            needs = ["ampliar armazen", "guindaste", "trabalhadores portuários"],;
        ));
        pacifico.add_entity(Entity(;
            "E-PAC-CLINIC-01", "Posto de Saude Insular", EntityType.CLINIC, "N-PAC",;
            capacity = 150, current_demand=200, people_served=8000, workers=3, workers_needed=5,;
            health = 0.70, supply_level=0.60, maintenance_level=0.75,;
            status = EntityStatus.OPERATIONAL,;
            needs = ["medico visitante", "telemedicina"],;
        ));
        pacifico.add_entity(Entity(;
            "E-PAC-SCHOOL-01", "Escola Comunitaria", EntityType.SCHOOL, "N-PAC",;
            capacity = 500, current_demand=400, people_served=3000, workers=8, workers_needed=8,;
            health = 0.85, supply_level=0.80, maintenance_level=0.82,;
            status = EntityStatus.OPERATIONAL,;
        ));
        republic.add_nation(pacifico);
        return republic;
    // ============================================================================
    // Triage Engine: What to treat NOW
    // ============================================================================
    public static class TriageEngine {
        // Motor de triagem: o que tratar primeiro.
        Como numa sala de emergencia:;
        - VERMELHO: tratar AGORA (vidas em risco);
        - AMARELO: tratar em horas/dias (vai piorar);
        - VERDE: pode esperar;
        - AZUL: esta bem, pode ajudar;
        A triagem considera:;
        1. Quantas pessoas sao afetadas;
        2. Se ha dependencia em cadeia (clinica depende de farmacia);
        3. Se a falha && de insumo, pessoal, || infraestrutura;
        4. Se existe capacidade excedente em outra nacao para ajudar;
        //
        public void __init__(self, republic: RepublicState) {
            self.republic = republic;
        public {texto: qualquer} triage(self) {
            // Realizar triagem completa da Republica.
            queue = self.republic.priority_queue();
            // Categorizar
            red = [] // CRITICAL -- AGORA;
            yellow = [] // URGENT/ELEVATED -- em dias;
            green = [] // MODERATE -- em semanas;
            blue = [] // STABLE/THRIVING -- pode ajudar;
            /* TODO: for-each Java para item em queue */
                urgency = item["urgency"];
                if (urgency >= 4) {
                    red.append(item);
                } else if (urgency >= 3) {
                    yellow.append(item);
                } else if (urgency >= 2) {
                    green.append(item);
                } else {
                    blue.append(item);
            // Analisar cadeias de dependencia
            chain_risks = self._dependency_chain_analysis();
            // Identificar capacidade excedente para realocar
            surplus = self._find_surplus_capacity();
            // Plano de acao
            action_plan = self._action_plan(red, yellow, surplus);
            return {;
                "cycle": self.republic.cycle,;
                "summary": self.republic.republic_health(),;
                "red_zone": red,;
                "yellow_zone": yellow,;
                "green_zone": green,;
                "blue_zone": blue,;
                "dependency_chains_at_risk": chain_risks,;
                "surplus_capacity_available": surplus,;
                "action_plan": action_plan,;
            };
        public [Dict] _dependency_chain_analysis(self) {
            // Se A depende de B, e B cai, A tambem cai.
            risks = [];
            all_entities = {&&.entity_id: && para && em self.republic.all_entities()};
            /* TODO: for-each Java para entity em self.republic.all_entities() */
                /* TODO: for-each Java para dep_id em entity.depends_on */
                    dep = all_entities.get(dep_id);
                    if (! dep) {
                        risks.append({
                            "entity": entity.name,;
                            "missing_dependency": dep_id,;
                            "risk": "Dependency does not exist",;
                        });
                    } else if (dep.urgency.value >= 4) {
                        risks.append({
                            "entity": entity.name,;
                            "depends_on": dep.name,;
                            "dependency_status": dep.status.value,;
                            "risk": "{dep.name} is critical -- {entity.name} will cascade-fail",;
                            "cascade_impact": entity.people_served,;
                        });
            return risks;
        public [Dict] _find_surplus_capacity(self) {
            // Encontrar entidades com capacidade excedente.
            surplus = [];
            /* TODO: for-each Java para e em self.republic.all_entities() */
                if (&&.utilization < 0.7 && &&.health > 0.85) {
                    surplus.append({
                        "entity": &&.name,;
                        "nation": &&.nation_id,;
                        "type": &&.etype.value,;
                        "capacity_used_pct": arredonde(&&.utilization * 100, 0),;
                        "available_capacity_pct": arredonde((1 - &&.utilization) * 100, 0),;
                        "health": arredonde(&&.health * 100, 0),;
                        "can_help": true,;
                    });
            return ordene(surplus, key=(x) -> x["available_capacity_pct"], reverse=true);
        funcao _action_plan(self, red: List, yellow: List,
                        surplus: List) -> [Dict]:;
            // Plano de acao: o que fazer, em que ordem.
            actions = [];
            priority = 1;
            /* TODO: for-each Java para item em red */
                entity_type = item["type"];
                issues = item["issues"];
                recommendations = item["recommendations"];
                // Find surplus entities of same type that could help
                helpers = [s para s em surplus if s["type"] == entity_type];
                action = {
                    "priority": priority,;
                    "action": "CRITICAL",;
                    "entity": item["name"],;
                    "nation": item["nation"],;
                    "issues": issues,;
                    "immediate_steps": recommendations,;
                    "people_affected": item["people_served"],;
                    "potential_helpers": [h["entity"] para h em helpers[:3]],;
                    "timeline": "IMEDIATO (hoje)",;
                };
                actions.append(action);
                priority = priority + 1;
            /* TODO: for-each Java para item em yellow[:5] */
                actions.append({
                    "priority": priority,;
                    "action": "URGENT",;
                    "entity": item["name"],;
                    "nation": item["nation"],;
                    "issues": item["issues"],;
                    "immediate_steps": item["recommendations"],;
                    "people_affected": item["people_served"],;
                    "timeline": "3-7 dias",;
                });
                priority = priority + 1;
            return actions;
    // ============================================================================
    // Main
    // ============================================================================
    if (__name__ == "__main__") {
        System.out.println("=" * 75);
        System.out.println("  OPENREPUBLIC -- TRIAGEM DE ENTIDADES PRIORITARIAS");
        System.out.println("  'O que precisamos tratar AGORA'");
        System.out.println("=" * 75);
        republic = create_critical_scenario();
        triage = TriageEngine(republic);
        result = triage.triage();
        // Summary
        s = result["summary"];
        System.out.println("\n  REPUBLICA: {republic.name} | Ciclo {republic.cycle}");
        System.out.println("  Nacoes: {s['nations']} | Entidades: {s['total_entities']}");
        System.out.println("  Saude media: {s['avg_health']:.0%}");
        System.out.println("\n  {'Zona':<12} {'Quantidade':>10}");
        System.out.println("  {'-'*25}");
        System.out.println("  {'CRITICA':<12} {s['critical_count']:>10}  <-- TRATAR AGORA");
        System.out.println("  {'URGENTE':<12} {s['urgent_count']:>10}");
        System.out.println("  {'ELEVADA':<12} {s['elevated_count']:>10}");
        System.out.println("  {'ESTAVEL':<12} {s['stable_count']:>10}");
        System.out.println("\n  Pessoas em risco: {s['people_at_risk']:,} / {s['total_people_served']:,} ({s['risk_coverage_pct']}%)");
        // RED ZONE -- Critical entities
        System.out.println("\n\n{'='*75}");
        System.out.println("  ZONA VERMELHA -- TRATAR AGORA ({len(result['red_zone'])} entidades)");
        System.out.println("{'='*75}");
        /* TODO: for-each Java para item em result["red_zone"] */
            System.out.println("\n  [{item['urgency_name']}] {item['name']}");
            System.out.println("    Nacao: {item['nation']} | Tipo: {item['type']}");
            System.out.println("    Risk score: {item['risk_score']}/100 | Utilizacao: {item['utilization']:.0f}%");
            System.out.println("    Saude: {item['health']:.0f}% | Insumos: {item['supply']:.0f}%");
            System.out.println("    Pessoas: {item['pessoas_servidas'] if 'pessoas_servidas' in item else item['people_served']:,}");
            System.out.println("    Trabalhadores: {item['workers']}");
            System.out.println("    Problemas:");
            /* TODO: for-each Java para issue em item["issues"] */
                System.out.println("      ! {issue}");
            System.out.println("    Acao:");
            /* TODO: for-each Java para rec em item["recommendations"] */
                System.out.println("      -> {rec}");
        // YELLOW ZONE
        if (result["yellow_zone"]) {
            System.out.println("\n\n{'='*75}");
            System.out.println("  ZONA AMARELA -- TRATAR EM DIAS ({len(result['yellow_zone'])} entidades)");
            System.out.println("{'='*75}");
            /* TODO: for-each Java para item em result["yellow_zone"] */
                System.out.println("  [{item['urgency_name']}] {item['name']} ({item['nation']})");
                System.out.println("    Risk: {item['risk_score']} | Uso: {item['utilization']:.0f}% | ";
                    "Saude: {item['health']:.0f}%");
                System.out.println("    Issues: {', '.join(item['issues'][:2])}");
                System.out.println("    -> {item['recommendations'][0]}");
                System.out.println();
        // Dependency chains at risk
        System.out.println("\n{'='*75}");
        System.out.println("  CADEIAS DE DEPENDENCIA EM RISCO");
        System.out.println("{'='*75}");
        if (result["dependency_chains_at_risk"]) {
            /* TODO: for-each Java para risk em result["dependency_chains_at_risk"] */
                System.out.println("\n  {risk.get('entity', '?')}");
                System.out.println("    {risk['risk']}");
                if ("cascade_impact" in risk) {
                    System.out.println("    Impacto em cascata: {risk['cascade_impact']:,} pessoas");
        } else {
            System.out.println("  Nenhuma cadeia de dependencia em risco.");
        // Surplus capacity
        System.out.println("\n{'='*75}");
        System.out.println("  CAPACIDADE EXCEDENTE DISPONIVEL PARA REALOCAR");
        System.out.println("{'='*75}");
        /* TODO: for-each Java para s em result["surplus_capacity_available"][:8] */
            System.out.println("  {s['entity']:<35} {s['nation']}  ";
                "livre: {s['available_capacity_pct']:.0f}%  saude: {s['health']:.0f}%");
        // Action plan
        System.out.println("\n{'='*75}");
        System.out.println("  PLANO DE ACAO PRIORITARIO");
        System.out.println("{'='*75}");
        /* TODO: for-each Java para action em result["action_plan"] */
            System.out.println("\n  #{action['priority']} [{action['action']}] {action['entity']} ({action['nation']})");
            System.out.println("     Pessoas afetadas: {action['people_affected']:,}");
            System.out.println("     Prazo: {action['timeline']}");
            System.out.println("     Passos:");
            /* TODO: for-each Java para step em action["immediate_steps"] */
                System.out.println("       -> {step}");
            if (action.get("potential_helpers")) {
                System.out.println("     Podem ajudar: {', '.join(action['potential_helpers'])}");
        // Per-nation breakdown
        System.out.println("\n{'='*75}");
        System.out.println("  SAUDE POR NACAO");
        System.out.println("{'='*75}");
        System.out.println("  {'Nacao':<15} {'Entidades':>10} {'Saude':>7} {'Criticas':>9} {'Em risco':>10}");
        System.out.println("  {'-'*55}");
        /* para cada (nid, nation) em republic.nations.items(): */
            crit = tamanho(nation.critical_entities());
            System.out.println("  {nation.name:<15} {len(nation.entities):>10} ";
                "{nation.avg_health:>6.0%} {crit:>9} {nation.people_at_risk:>10,}");
        System.out.println("\n{'='*75}");
        System.out.println("  RESUMO: {len(result['red_zone'])} entidades precisam de acao IMEDIATA.");
        System.out.println("  {result['summary']['people_at_risk']:,} pessoas afetadas.");
        System.out.println("  {len(result['surplus_capacity_available'])} entidades tem capacidade");
        System.out.println("  para realocar && ajudar.");
        System.out.println("{'='*75}");
}
