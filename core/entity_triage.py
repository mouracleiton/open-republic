#!/usr/bin/env python3
"""
OpenRepublic -- Simulacao de Entidades Prioritarias -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenRepublic -- Simulacao de Entidades Prioritarias
=====================================================
Hierarquia:
OpenRepublic (federacao de nacoes)
    -> OpenNation (nacoes membros, cada uma sem propriedade privada)
    -> Entidade (subconjuntos funcionais dentro de cada nacao)
Uma OpenNation not and um bloco homogeneo. and composta por ENTIDADES:
- Cada entidade and um grupo/infraestrutura/instituicao que presta
    uma funcao essencial para a nacao.
- As entidades tem estados de saude, capacidade, and necessidade.
- A Republica precisa saber QUAIS entidades precisam de atencao
    AGORA para priorizar alocacao de trabalho and recursos.
Esta simulacao identifica and prioriza as entidades mais criticas.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa random
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple, Set de typing
# importa Enum de enum
# importa defaultdict, deque de collections
# importa numpy as np
# ============================================================================
# Entity Types (o que existe dentro de uma OpenNation)
# ============================================================================
class EntityType(Enum):
    # Producao
    FARM = "farm"  // producao de alimentos
    AQUAPONICS = "aquaponics"  // peixe + planta integrados
    FACTORY = "factory"  // manufatura (moveis, ferramentas, roupas)
    FABLAB = "fablab"  // fabricacao digital (3D print, CNC, laser)
    ENERGY_PLANT = "energy_plant"  // solar/eolica/hidro/fusao
    WATER_TREATMENT = "water_treatment"  // tratamento + distribuicao agua
    # Saude
    CLINIC = "clinic"  // atencao primaria
    HOSPITAL = "hospital"  // atencao especializada
    PHARMACY = "pharmacy"  // producao/distribuicao de remedios
    MENTAL_HEALTH = "mental_health"  // saude mental coletiva
    # Educacao
    SCHOOL = "school"  // educacao basica
    UNIVERSITY = "university"  // educacao superior + pesquisa
    LIBRARY = "library"  // conhecimento aberto
    # Habitacao
    HOUSING_BLOCK = "housing_block"  // conjunto habitacional comunitario
    # Logistica
    TRANSPORT_HUB = "transport_hub"  // centro de transporte compartilhado
    DISTRIBUTION = "distribution"  // armazen + distribuicao de bens
    # Social/Cultural
    COMMUNITY_CENTER = "community_center"  // espaco de convivencia
    KITCHEN = "community_kitchen"  // cozinha comunitaria
    CHILDCARE = "childcare"  // cuidado infantil
    ELDER_CARE = "elder_care"  // cuidado de idosos
    # Inovacao
    RESEARCH_LAB = "research_lab"  // laboratorio de pesquisa
    DATA_CENTER = "data_center"  // computacao/armazenamento
    QUANTUM_NODE = "quantum_node"  // no quantico da rede
    # Ecologia
    FORESTRY = "forestry"  // manejo florestal
    WASTE_RECYCLE = "waste_recycle"  // reciclagem + compostagem
    ECO_RESTORATION = "eco_restoration"  // restauracao de ecossistemas
class UrgencyLevel(Enum):
    CRITICAL = 5 // colapso iminente -- vidas em risco
    URGENT = 4 // funcionando precariamente, vai falhar em dias
    ELEVATED = 3 // precisa de atencao em semanas
    MODERATE = 2 // pode esperar, mas not esquecer
    STABLE = 1 // saudavel, continuar monitorando
    THRIVING = 0 // acima do esperado, pode ajudar outras
class EntityStatus(Enum):
    OPERATIONAL = "operational"
    DEGRADED = "degraded"  // funcionando abaixo do ideal
    CRITICAL = "critical"  // risco de colapso
    OFFLINE = "offline"  // parou de funcionar
    UNDER_CONSTRUCTION = "building"
    PLANNED = "planned"  // ainda not existe, precisa ser criada
# ============================================================================
# Entity Model
# ============================================================================
# decorador: @dataclass
class Entity:
    # Uma entidade dentro de uma OpenNation.
    Cada entidade and um componente funcional da nacao.
    Tem pessoas trabalhando, capacidade, estado de saude,
    and necessidades especificas.
    # 
    entity_id: texto
    name: texto
    etype: EntityType
    nation_id: texto
    # Capacidade
    capacity: float = 100.0 // unidades que pode produzir/atender por ciclo
    current_demand: float = 50.0 // demanda atual
    people_served: int = 0
    workers: int = 0
    workers_needed: int = 5
    # Estado
    status: EntityStatus = EntityStatus.OPERATIONAL
    health: float = 1.0 // 0=colapsou, 1=perfeito
    supply_level: float = 1.0 // 0=sem insumos, 1=abastecido
    maintenance_level: float = 1.0 // 0=precisa reparo urgente, 1=bem cuidado
    # Dependencias (outras entidades que esta precisa para funcionar)
    depends_on: {texto} = field(default_factory=set) // entity_ids
    # Necessidades atuais
    needs: [texto] = field(default_factory=list)
    # Historico
    last_issues: [texto] = field(default_factory=list)
    # decorador: @property
    def utilization(self) -> float:
        # Quao sobrecarregada esta (0=solta, 1=no limite, >1=estourou).
        return self.current_demand / max(self.capacity, 1)
    # decorador: @property
    def urgency(self) -> UrgencyLevel:
        # Nivel de urgencia calculado automaticamente.
        if self.status == EntityStatus.OFFLINE:
            return UrgencyLevel.CRITICAL
        if self.status == EntityStatus.CRITICAL:
            return UrgencyLevel.CRITICAL
        if self.health < 0.3 or self.supply_level < 0.2 or self.utilization > 1.5:
            return UrgencyLevel.CRITICAL
        if self.health < 0.5 or self.supply_level < 0.4 or self.utilization > 1.2:
            return UrgencyLevel.URGENT
        if self.health < 0.7 or self.supply_level < 0.6 or self.utilization > 1.0:
            return UrgencyLevel.ELEVATED
        if self.health < 0.85 or self.workers < self.workers_needed:
            return UrgencyLevel.MODERATE
        if self.utilization < 0.5:
            return UrgencyLevel.THRIVING
        return UrgencyLevel.STABLE
    # decorador: @property
    def risk_score(self) -> float:
        # Score de risco 0-100 (100=colapso iminente).
        health_risk = (1 - self.health) * 40
        supply_risk = (1 - self.supply_level) * 25
        overload_risk = min(50, max(0, (self.utilization - 0.8) * 50))
        staff_risk = max(0, (self.workers_needed - self.workers) / max(self.workers_needed, 1)) * 20
        maint_risk = (1 - self.maintenance_level) * 15
        return round(min(100, health_risk + supply_risk + overload_risk + staff_risk + maint_risk), 1)
    def assess(self) -> {texto: qualquer}:
        # Avaliacao completa da entidade.
        issues = []
        recommendations = []
        if self.status == EntityStatus.OFFLINE:
            issues.append("ENTIDADE PARADA")
            recommendations.append("Reativar imediatamente -- vidas afetadas")
        if self.health < 0.3:
            issues.append("Saude critica: {self.health:.0%}")
            recommendations.append("Manutencao de emergencia")
        if self.supply_level < 0.3:
            issues.append("Insumos criticos: {self.supply_level:.0%}")
            recommendations.append("Abastecer URGENTE")
        if self.utilization > 1.3:
            issues.append("Sobrecarga: {self.utilization:.0%} da capacidade")
            recommendations.append("Expandir capacidade or redistribuir demanda")
        if self.workers < self.workers_needed:
            deficit = self.workers_needed - self.workers
            issues.append("Falta de trabalhadores: {deficit} pessoas")
            recommendations.append("Recrutar {deficit} pessoas com habilidades relevantes")
        if self.maintenance_level < 0.5:
            issues.append("Manutencao atrasada: {self.maintenance_level:.0%}")
            recommendations.append("Agendar manutencao preventiva")
        if not issues:
            issues.append("Operacao normal")
            recommendations.append("Manter monitoramento")
        return {
            "entity_id": self.entity_id,
            "name": self.name,
            "type": self.etype.value,
            "nation": self.nation_id,
            "status": self.status.value,
            "urgency": self.urgency.value,
            "urgency_name": self.urgency.name,
            "risk_score": self.risk_score,
            "utilization": round(self.utilization * 100, 0),
            "health": round(self.health * 100, 0),
            "supply": round(self.supply_level * 100, 0),
            "workers": "{self.workers}/{self.workers_needed}",
            "issues": issues,
            "recommendations": recommendations,
            "depends_on": list(self.depends_on),
            "people_served": self.people_served,
        }
# ============================================================================
# Nation (container of entities)
# ============================================================================
# decorador: @dataclass
class NationState:
    # Estado de uma nacao dentro da Republica.
    nation_id: texto
    name: texto
    region: texto
    population: inteiro
    entities: {texto: Entity} = field(default_factory=dict)
    def add_entity(self, entity: Entity):
        entity.nation_id = self.nation_id
        self.entities[entity.entity_id] = entity
    def critical_entities(self) -> [Entity]:
        # Entidades em estado critico.
        return sorted(
            [and para and em self.entities.values() if and.urgency.value >= 4],
            key = (and) -> -and.risk_score
        )
    funcao all_by_urgency(self) retorna Dict[UrgencyLevel, [Entity]]:
        # Todas as entidades agrupadas por urgencia.
        groups = defaultdict(list)
        for e in self.entities.values():
            groups[and.urgency].append(and)
        for level in groups:
            groups[level].sort(key=(and) -> -and.risk_score)
        return dict(groups)
    # decorador: @property
    def avg_health(self) -> float:
        if not self.entities:
            return 0
        return round(flutuante(np.mean([and.health para and em self.entities.values()])), 2)
    # decorador: @property
    def total_capacity_utilization(self) -> float:
        if not self.entities:
            return 0
        return round(flutuante(np.mean([and.utilization para and em self.entities.values()])), 2)
    # decorador: @property
    def people_at_risk(self) -> int:
        # Pessoas afetadas por entidades em risco.
        return sum(and.people_served para and em self.entities.values() if and.urgency.value >= 4)
# ============================================================================
# Republic (container of nations)
# ============================================================================
# decorador: @dataclass
class RepublicState:
    # Estado da Republica completa.
    name: texto
    nations: {texto: NationState} = field(default_factory=dict)
    cycle: int = 0
    def add_nation(self, nation: NationState):
        self.nations[nation.nation_id] = nation
    def all_entities(self) -> [Entity]:
        entities = []
        for n in self.nations.values():
            entities.extend(n.entities.values())
        return entities
    funcao priority_queue(self) retorna List[{texto: qualquer}]:
        # Fila de prioridade: quais entidades tratar AGORA.
        Ordenada por:
        1. Urgencia (critico primeiro)
        2. Risk score (maior primeiro)
        3. Pessoas afetadas (mais pessoas primeiro)
        # 
        entities = self.all_entities()
        scored = []
        for e in entities:
            assessment = and.assess()
            # Composite priority score
            priority = (
                and.urgency.value * 1000 +
                and.risk_score * 10 +
                and.people_served * 0.01
            )
            scored.append((priority, assessment))
        scored.sort(key=(x) -> -x[0])
        return [s[1] para s em scored]
    def republic_health(self) -> {texto: qualquer}:
        # Saude geral da Republica.
        all_entities = self.all_entities()
        if not all_entities:
            return {}
        by_urgency = defaultdict(inteiro)
        for e in all_entities:
            by_urgency[and.urgency.name] += 1
        total_people_at_risk = sum(
            and.people_served para and em all_entities if and.urgency.value >= 4
        )
        total_people_served = sum(and.people_served para and em all_entities)
        return {
            "nations": len(self.nations),
            "total_entities": len(all_entities),
            "avg_health": round(flutuante(np.mean([and.health para and em all_entities])), 2),
            "critical_count": by_urgency.get("CRITICAL", 0),
            "urgent_count": by_urgency.get("URGENT", 0),
            "elevated_count": by_urgency.get("ELEVATED", 0),
            "stable_count": by_urgency.get("STABLE", 0) + by_urgency.get("THRIVING", 0),
            "people_at_risk": total_people_at_risk,
            "total_people_served": total_people_served,
            "risk_coverage_pct": round(
                total_people_at_risk / max(total_people_served, 1) * 100, 1
            ),
            "by_urgency": dict(by_urgency),
        }
# ============================================================================
# Simulation Setup: The Republic at a Critical Moment
# ============================================================================
def create_critical_scenario() -> RepublicState:
    # Cria um cenario onde varias entidades precisam atencao AGORA.
    Cenario: A Republica esta no ciclo 18. Algumas nacoes estao
    bem estabelecidas, outras sao recentes and tem gargalos.
    O objetivo and identificar o que tratar primeiro.
    # 
    republic = RepublicState(name="Republica dos Bens Comuns", cycle=18)
    # === NATION 1: Amazonia (estabelecida, alguns gargalos) ===
    amazonia = NationState("N-AMZ", "Amazonia", "America do Sul", 50000)
    amazonia.add_entity(Entity(
        "E-AMZ-CLINIC-01", "Clinica Central Manaus", EntityType.CLINIC, "N-AMZ",
        capacity = 500, current_demand=720, people_served=5000, workers=8, workers_needed=12,
        health = 0.45, supply_level=0.3, maintenance_level=0.6,
        status = EntityStatus.DEGRADED,
        depends_on = {"E-AMZ-PHARM-01"},
        needs = ["medicamentos", "mais medicos", "ampliar espaço"],
    ))
    amazonia.add_entity(Entity(
        "E-AMZ-FARM-01", "Cooperativa Agricola Rio Negro", EntityType.FARM, "N-AMZ",
        capacity = 10000, current_demand=8000, people_served=50000, workers=120, workers_needed=100,
        health = 0.92, supply_level=0.85, maintenance_level=0.88,
        status = EntityStatus.OPERATIONAL,
    ))
    amazonia.add_entity(Entity(
        "E-AMZ-PHARM-01", "Farmacia Comunitaria", EntityType.PHARMACY, "N-AMZ",
        capacity = 2000, current_demand=2400, people_served=15000, workers=3, workers_needed=5,
        health = 0.55, supply_level=0.25, maintenance_level=0.7,
        status = EntityStatus.DEGRADED,
        needs = ["reposicao de estoque"],
    ))
    amazonia.add_entity(Entity(
        "E-AMZ-ENERGY-01", "Microgrid Solar+Hidro", EntityType.ENERGY_PLANT, "N-AMZ",
        capacity = 5000, current_demand=4200, people_served=50000, workers=6, workers_needed=8,
        health = 0.88, supply_level=1.0, maintenance_level=0.82,
        status = EntityStatus.OPERATIONAL,
    ))
    amazonia.add_entity(Entity(
        "E-AMZ-HOUSING-01", "Habitacao Comunitaria Bloco A", EntityType.HOUSING_BLOCK, "N-AMZ",
        capacity = 5000, current_demand=6500, people_served=50000, workers=4, workers_needed=6,
        health = 0.65, supply_level=0.9, maintenance_level=0.5,
        status = EntityStatus.DEGRADED,
        needs = ["construir mais 500 unidades", "reparar encanamento"],
    ))
    amazonia.add_entity(Entity(
        "E-AMZ-SCHOOL-01", "Centro de Aprendizagem", EntityType.SCHOOL, "N-AMZ",
        capacity = 2000, current_demand=1800, people_served=8000, workers=40, workers_needed=35,
        health = 0.90, supply_level=0.95, maintenance_level=0.85,
        status = EntityStatus.OPERATIONAL,
    ))
    amazonia.add_entity(Entity(
        "E-AMZ-WATER-01", "Sistema de Agua + Tratamento", EntityType.WATER_TREATMENT, "N-AMZ",
        capacity = 500000, current_demand=480000, people_served=50000, workers=5, workers_needed=5,
        health = 0.75, supply_level=1.0, maintenance_level=0.60,
        status = EntityStatus.OPERATIONAL,
        needs = ["limpeza de filtros"],
    ))
    amazonia.add_entity(Entity(
        "E-AMZ-FORESTRY-01", "Manejo Florestal Sustentavel", EntityType.FORESTRY, "N-AMZ",
        capacity = 100, current_demand=40, people_served=50000, workers=30, workers_needed=25,
        health = 0.95, supply_level=1.0, maintenance_level=0.95,
        status = EntityStatus.OPERATIONAL,
    ))
    amazonia.add_entity(Entity(
        "E-AMZ-RECYCLE-01", "Centro de Reciclagem", EntityType.WASTE_RECYCLE, "N-AMZ",
        capacity = 500, current_demand=700, people_served=50000, workers=3, workers_needed=8,
        health = 0.40, supply_level=0.6, maintenance_level=0.3,
        status = EntityStatus.DEGRADED,
        needs = ["maquinario de triagem", "mais trabalhadores"],
    ))
    amazonia.add_entity(Entity(
        "E-AMZ-DATA-01", "Datacenter Comunitario", EntityType.DATA_CENTER, "N-AMZ",
        capacity = 100, current_demand=90, people_served=50000, workers=2, workers_needed=3,
        health = 0.85, supply_level=0.9, maintenance_level=0.80,
        status = EntityStatus.OPERATIONAL,
    ))
    republic.add_nation(amazonia)
    # === NATION 2: Sahel (nova, gargalos graves) ===
    sahel = NationState("N-SAH", "Sahel", "Africa", 40000)
    sahel.add_entity(Entity(
        "E-SAH-CLINIC-01", "Posto de Saude Oasis", EntityType.CLINIC, "N-SAH",
        capacity = 200, current_demand=450, people_served=12000, workers=2, workers_needed=8,
        health = 0.20, supply_level=0.10, maintenance_level=0.30,
        status = EntityStatus.CRITICAL,
        needs = ["medicamentos urgentes", "equipe medica", "agua potavel"],
        depends_on = {"E-SAH-WATER-01"},
    ))
    sahel.add_entity(Entity(
        "E-SAH-WATER-01", "Poços + Dessalinizacao Solar", EntityType.WATER_TREATMENT, "N-SAH",
        capacity = 80000, current_demand=200000, people_served=40000, workers=3, workers_needed=10,
        health = 0.35, supply_level=0.15, maintenance_level=0.40,
        status = EntityStatus.CRITICAL,
        needs = ["construir mais pocos", "painéis solares", "bombeamento"],
    ))
    sahel.add_entity(Entity(
        "E-SAH-ENERGY-01", "Fazenda Solar Continental", EntityType.ENERGY_PLANT, "N-SAH",
        capacity = 10000, current_demand=7500, people_served=40000, workers=15, workers_needed=20,
        health = 0.85, supply_level=1.0, maintenance_level=0.80,
        status = EntityStatus.OPERATIONAL,
    ))
    sahel.add_entity(Entity(
        "E-SAH-FARM-01", "Agricultura Seca + Hidroponia", EntityType.FARM, "N-SAH",
        capacity = 3000, current_demand=5000, people_served=40000, workers=25, workers_needed=40,
        health = 0.50, supply_level=0.30, maintenance_level=0.55,
        status = EntityStatus.DEGRADED,
        needs = ["sementes", "sistemas de irrigacao", "mais agricultores"],
        depends_on = {"E-SAH-WATER-01"},
    ))
    sahel.add_entity(Entity(
        "E-SAH-HOUSING-01", "Habitacao Desertica", EntityType.HOUSING_BLOCK, "N-SAH",
        capacity = 3000, current_demand=5000, people_served=40000, workers=2, workers_needed=8,
        health = 0.55, supply_level=0.7, maintenance_level=0.50,
        status = EntityStatus.DEGRADED,
        needs = ["construcao de novas unidades", "refrigeracao passiva"],
    ))
    sahel.add_entity(Entity(
        "E-SAH-SCHOOL-01", "Centro Educativo Nomade", EntityType.SCHOOL, "N-SAH",
        capacity = 800, current_demand=1200, people_served=5000, workers=5, workers_needed=15,
        health = 0.60, supply_level=0.50, maintenance_level=0.65,
        status = EntityStatus.DEGRADED,
        needs = ["professores", "material didatico"],
    ))
    sahel.add_entity(Entity(
        "E-SAH-CHILD-01", "Cuidado Infantil Comunitario", EntityType.CHILDCARE, "N-SAH",
        capacity = 100, current_demand=300, people_served=3000, workers=1, workers_needed=6,
        health = 0.30, supply_level=0.40, maintenance_level=0.35,
        status = EntityStatus.CRITICAL,
        needs = ["espaco fisico", "cuidadores", "material"],
    ))
    republic.add_nation(sahel)
    # === NATION 3: Nordica (estavel, pode ajudar) ===
    nordica = NationState("N-NOR", "Nordica", "Europa", 30000)
    nordica.add_entity(Entity(
        "E-NOR-CLINIC-01", "Clinica Universal", EntityType.CLINIC, "N-NOR",
        capacity = 600, current_demand=400, people_served=30000, workers=15, workers_needed=12,
        health = 0.95, supply_level=0.98, maintenance_level=0.95,
        status = EntityStatus.OPERATIONAL,
    ))
    nordica.add_entity(Entity(
        "E-NOR-ENERGY-01", "Parque Eolico + Fusion Node", EntityType.ENERGY_PLANT, "N-NOR",
        capacity = 20000, current_demand=12000, people_served=30000, workers=20, workers_needed=18,
        health = 0.98, supply_level=1.0, maintenance_level=0.97,
        status = EntityStatus.OPERATIONAL,
    ))
    nordica.add_entity(Entity(
        "E-NOR-LAB-01", "Laboratorio Quantico", EntityType.RESEARCH_LAB, "N-NOR",
        capacity = 50, current_demand=30, people_served=30000, workers=12, workers_needed=10,
        health = 0.97, supply_level=0.95, maintenance_level=0.96,
        status = EntityStatus.OPERATIONAL,
    ))
    nordica.add_entity(Entity(
        "E-NOR-DATA-01", "Datacenter Geotermico", EntityType.DATA_CENTER, "N-NOR",
        capacity = 500, current_demand=350, people_served=30000, workers=8, workers_needed=6,
        health = 0.96, supply_level=0.98, maintenance_level=0.94,
        status = EntityStatus.OPERATIONAL,
    ))
    nordica.add_entity(Entity(
        "E-NOR-QUANTUM-01", "No Quantico Republica", EntityType.QUANTUM_NODE, "N-NOR",
        capacity = 10, current_demand=8, people_served=200000, workers=4, workers_needed=5,
        health = 0.90, supply_level=0.92, maintenance_level=0.88,
        status = EntityStatus.OPERATIONAL,
        needs = ["1 especialista em QKD"],
    ))
    nordica.add_entity(Entity(
        "E-NOR-HOUSING-01", "Habitacao Modular Boreal", EntityType.HOUSING_BLOCK, "N-NOR",
        capacity = 12000, current_demand=10500, people_served=30000, workers=6, workers_needed=5,
        health = 0.93, supply_level=1.0, maintenance_level=0.90,
        status = EntityStatus.OPERATIONAL,
    ))
    republic.add_nation(nordica)
    # === NATION 4: Pacifico (estavel mas isolada) ===
    pacifico = NationState("N-PAC", "Pacifico", "Oceania", 20000)
    pacifico.add_entity(Entity(
        "E-PAC-ENERGY-01", "Geracao das Mars + Solar", EntityType.ENERGY_PLANT, "N-PAC",
        capacity = 3000, current_demand=2800, people_served=20000, workers=4, workers_needed=6,
        health = 0.80, supply_level=0.85, maintenance_level=0.72,
        status = EntityStatus.OPERATIONAL,
        needs = ["manutenção turbinas", "mais tecnicos"],
    ))
    pacifico.add_entity(Entity(
        "E-PAC-DIST-01", "Centro de Distribuicao Portuaria", EntityType.DISTRIBUTION, "N-PAC",
        capacity = 10000, current_demand=14000, people_served=200000, workers=8, workers_needed=15,
        health = 0.60, supply_level=0.50, maintenance_level=0.55,
        status = EntityStatus.DEGRADED,
        needs = ["ampliar armazen", "guindaste", "trabalhadores portuários"],
    ))
    pacifico.add_entity(Entity(
        "E-PAC-CLINIC-01", "Posto de Saude Insular", EntityType.CLINIC, "N-PAC",
        capacity = 150, current_demand=200, people_served=8000, workers=3, workers_needed=5,
        health = 0.70, supply_level=0.60, maintenance_level=0.75,
        status = EntityStatus.OPERATIONAL,
        needs = ["medico visitante", "telemedicina"],
    ))
    pacifico.add_entity(Entity(
        "E-PAC-SCHOOL-01", "Escola Comunitaria", EntityType.SCHOOL, "N-PAC",
        capacity = 500, current_demand=400, people_served=3000, workers=8, workers_needed=8,
        health = 0.85, supply_level=0.80, maintenance_level=0.82,
        status = EntityStatus.OPERATIONAL,
    ))
    republic.add_nation(pacifico)
    return republic
# ============================================================================
# Triage Engine: What to treat NOW
# ============================================================================
class TriageEngine:
    # Motor de triagem: o que tratar primeiro.
    Como numa sala de emergencia:
    - VERMELHO: tratar AGORA (vidas em risco)
    - AMARELO: tratar em horas/dias (vai piorar)
    - VERDE: pode esperar
    - AZUL: esta bem, pode ajudar
    A triagem considera:
    1. Quantas pessoas sao afetadas
    2. Se ha dependencia em cadeia (clinica depende de farmacia)
    3. Se a falha and de insumo, pessoal, or infraestrutura
    4. Se existe capacidade excedente em outra nacao para ajudar
    # 
    def __init__(self, republic: RepublicState):
        self.republic = republic
    def triage(self) -> {texto: qualquer}:
        # Realizar triagem completa da Republica.
        queue = self.republic.priority_queue()
        # Categorizar
        red = [] // CRITICAL -- AGORA
        yellow = [] // URGENT/ELEVATED -- em dias
        green = [] // MODERATE -- em semanas
        blue = [] // STABLE/THRIVING -- pode ajudar
        for item in queue:
            urgency = item["urgency"]
            if urgency >= 4:
                red.append(item)
            elif urgency >= 3:
                yellow.append(item)
            elif urgency >= 2:
                green.append(item)
            else:
                blue.append(item)
        # Analisar cadeias de dependencia
        chain_risks = self._dependency_chain_analysis()
        # Identificar capacidade excedente para realocar
        surplus = self._find_surplus_capacity()
        # Plano de acao
        action_plan = self._action_plan(red, yellow, surplus)
        return {
            "cycle": self.republic.cycle,
            "summary": self.republic.republic_health(),
            "red_zone": red,
            "yellow_zone": yellow,
            "green_zone": green,
            "blue_zone": blue,
            "dependency_chains_at_risk": chain_risks,
            "surplus_capacity_available": surplus,
            "action_plan": action_plan,
        }
    def _dependency_chain_analysis(self) -> [Dict]:
        # Se A depende de B, e B cai, A tambem cai.
        risks = []
        all_entities = {and.entity_id: and para and em self.republic.all_entities()}
        for entity in self.republic.all_entities():
            for dep_id in entity.depends_on:
                dep = all_entities.get(dep_id)
                if not dep:
                    risks.append({
                        "entity": entity.name,
                        "missing_dependency": dep_id,
                        "risk": "Dependency does not exist",
                    })
                elif dep.urgency.value >= 4:
                    risks.append({
                        "entity": entity.name,
                        "depends_on": dep.name,
                        "dependency_status": dep.status.value,
                        "risk": "{dep.name} is critical -- {entity.name} will cascade-fail",
                        "cascade_impact": entity.people_served,
                    })
        return risks
    def _find_surplus_capacity(self) -> [Dict]:
        # Encontrar entidades com capacidade excedente.
        surplus = []
        for e in self.republic.all_entities():
            if and.utilization < 0.7 and and.health > 0.85:
                surplus.append({
                    "entity": and.name,
                    "nation": and.nation_id,
                    "type": and.etype.value,
                    "capacity_used_pct": round(and.utilization * 100, 0),
                    "available_capacity_pct": round((1 - and.utilization) * 100, 0),
                    "health": round(and.health * 100, 0),
                    "can_help": True,
                })
        return sorted(surplus, key=(x) -> x["available_capacity_pct"], reverse=True)
    funcao _action_plan(self, red: List, yellow: List,
                    surplus: List) -> [Dict]:
        # Plano de acao: o que fazer, em que ordem.
        actions = []
        priority = 1
        for item in red:
            entity_type = item["type"]
            issues = item["issues"]
            recommendations = item["recommendations"]
            # Find surplus entities of same type that could help
            helpers = [s para s em surplus if s["type"] == entity_type]
            action = {
                "priority": priority,
                "action": "CRITICAL",
                "entity": item["name"],
                "nation": item["nation"],
                "issues": issues,
                "immediate_steps": recommendations,
                "people_affected": item["people_served"],
                "potential_helpers": [h["entity"] para h em helpers[:3]],
                "timeline": "IMEDIATO (hoje)",
            }
            actions.append(action)
            priority = priority + 1
        for item in yellow[:5]:
            actions.append({
                "priority": priority,
                "action": "URGENT",
                "entity": item["name"],
                "nation": item["nation"],
                "issues": item["issues"],
                "immediate_steps": item["recommendations"],
                "people_affected": item["people_served"],
                "timeline": "3-7 dias",
            })
            priority = priority + 1
        return actions
# ============================================================================
# Main
# ============================================================================
if __name__ == "__main__":
    print("=" * 75)
    print("  OPENREPUBLIC -- TRIAGEM DE ENTIDADES PRIORITARIAS")
    print("  'O que precisamos tratar AGORA'")
    print("=" * 75)
    republic = create_critical_scenario()
    triage = TriageEngine(republic)
    result = triage.triage()
    # Summary
    s = result["summary"]
    print("\n  REPUBLICA: {republic.name} | Ciclo {republic.cycle}")
    print("  Nacoes: {s['nations']} | Entidades: {s['total_entities']}")
    print("  Saude media: {s['avg_health']:.0%}")
    print("\n  {'Zona':<12} {'Quantidade':>10}")
    print("  {'-'*25}")
    print("  {'CRITICA':<12} {s['critical_count']:>10}  <-- TRATAR AGORA")
    print("  {'URGENTE':<12} {s['urgent_count']:>10}")
    print("  {'ELEVADA':<12} {s['elevated_count']:>10}")
    print("  {'ESTAVEL':<12} {s['stable_count']:>10}")
    print("\n  Pessoas em risco: {s['people_at_risk']:,} / {s['total_people_served']:,} ({s['risk_coverage_pct']}%)")
    # RED ZONE -- Critical entities
    print("\n\n{'='*75}")
    print("  ZONA VERMELHA -- TRATAR AGORA ({len(result['red_zone'])} entidades)")
    print("{'='*75}")
    for item in result["red_zone"]:
        print("\n  [{item['urgency_name']}] {item['name']}")
        print("    Nacao: {item['nation']} | Tipo: {item['type']}")
        print("    Risk score: {item['risk_score']}/100 | Utilizacao: {item['utilization']:.0f}%")
        print("    Saude: {item['health']:.0f}% | Insumos: {item['supply']:.0f}%")
        print("    Pessoas: {item['pessoas_servidas'] if 'pessoas_servidas' in item else item['people_served']:,}")
        print("    Trabalhadores: {item['workers']}")
        print("    Problemas:")
        for issue in item["issues"]:
            print("      ! {issue}")
        print("    Acao:")
        for rec in item["recommendations"]:
            print("      -> {rec}")
    # YELLOW ZONE
    if result["yellow_zone"]:
        print("\n\n{'='*75}")
        print("  ZONA AMARELA -- TRATAR EM DIAS ({len(result['yellow_zone'])} entidades)")
        print("{'='*75}")
        for item in result["yellow_zone"]:
            print("  [{item['urgency_name']}] {item['name']} ({item['nation']})")
            print("    Risk: {item['risk_score']} | Uso: {item['utilization']:.0f}% | "
                "Saude: {item['health']:.0f}%")
            print("    Issues: {', '.join(item['issues'][:2])}")
            print("    -> {item['recommendations'][0]}")
            print()
    # Dependency chains at risk
    print("\n{'='*75}")
    print("  CADEIAS DE DEPENDENCIA EM RISCO")
    print("{'='*75}")
    if result["dependency_chains_at_risk"]:
        for risk in result["dependency_chains_at_risk"]:
            print("\n  {risk.get('entity', '?')}")
            print("    {risk['risk']}")
            if "cascade_impact" in risk:
                print("    Impacto em cascata: {risk['cascade_impact']:,} pessoas")
    else:
        print("  Nenhuma cadeia de dependencia em risco.")
    # Surplus capacity
    print("\n{'='*75}")
    print("  CAPACIDADE EXCEDENTE DISPONIVEL PARA REALOCAR")
    print("{'='*75}")
    for s in result["surplus_capacity_available"][:8]:
        print("  {s['entity']:<35} {s['nation']}  "
            "livre: {s['available_capacity_pct']:.0f}%  saude: {s['health']:.0f}%")
    # Action plan
    print("\n{'='*75}")
    print("  PLANO DE ACAO PRIORITARIO")
    print("{'='*75}")
    for action in result["action_plan"]:
        print("\n  #{action['priority']} [{action['action']}] {action['entity']} ({action['nation']})")
        print("     Pessoas afetadas: {action['people_affected']:,}")
        print("     Prazo: {action['timeline']}")
        print("     Passos:")
        for step in action["immediate_steps"]:
            print("       -> {step}")
        if action.get("potential_helpers"):
            print("     Podem ajudar: {', '.join(action['potential_helpers'])}")
    # Per-nation breakdown
    print("\n{'='*75}")
    print("  SAUDE POR NACAO")
    print("{'='*75}")
    print("  {'Nacao':<15} {'Entidades':>10} {'Saude':>7} {'Criticas':>9} {'Em risco':>10}")
    print("  {'-'*55}")
    for each (nid, nation) in republic.nations.items():
        crit = len(nation.critical_entities())
        print("  {nation.name:<15} {len(nation.entities):>10} "
            "{nation.avg_health:>6.0%} {crit:>9} {nation.people_at_risk:>10,}")
    print("\n{'='*75}")
    print("  RESUMO: {len(result['red_zone'])} entidades precisam de acao IMEDIATA.")
    print("  {result['summary']['people_at_risk']:,} pessoas afetadas.")
    print("  {len(result['surplus_capacity_available'])} entidades tem capacidade")
    print("  para realocar and ajudar.")
    print("{'='*75}")
