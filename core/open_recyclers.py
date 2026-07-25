#!/usr/bin/env python3
"""
OpenRecyclers -- Dispositivos, Maquinas e Gratificacao para Catadores -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenRecyclers -- Dispositivos, Maquinas and Gratificacao para Catadores
=====================================================================
"Quem recolhe o que outros jogaram fora not and 'catador'.
and TRABALHADOR AMBIENTAL. and quem LIMPA o mundo."
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional de typing
# importa Enum de enum
# importa defaultdict, Counter de collections
# importa datetime de datetime
# ============================================================================
# 1. MATERIAIS RECICLAVEIS
# ============================================================================
class RecyclableType(Enum):
    PET = "pet"
    ALUMINIO = "aluminio"
    PAPEL = "papel"
    PLASTICO_DURO = "plastico_duro"
    VIDRO = "vidro"
    METAL = "metal"
    ELETRONICO = "eletronico"
    ORGANICO = "organico"
    BATERIA = "bateria"
    TEXTIL = "textil"
class DeviceType(Enum):
    CART = "carrinho_eletrico"
    EXOSKELETON = "exoesqueleto"
    SMART_CLAW = "garra_inteligente"
    PRESS = "prensa_portatil"
    SORTER = "triagem_automatica"
    WEIGHING = "balanca_inteligente"
    PROTECTION = "equipamento_protecao"
    SCANNER = "scanner_material"
# decorador: @dataclass
class ErgonomicDevice:
    device_id: texto
    name: texto
    device_type: DeviceType
    description: str = ""
    reduces_effort: float = 0.8
    increases_speed: float = 2.0
    auto_credit: bool = False
    fabrication_hours: float = 20.0
    materials: [texto] = field(default_factory=list)
DEVICES: [ErgonomicDevice] = [
    ErgonomicDevice(
        "DEV-01", "Carrinho Eletrico Cargueiro",
        DeviceType.CART,
        "Carrinho motorizado 500W. Carrega 200kg. Bateria solar. "
        "5 compartimentos por material. GPS. Autonomia 30km.",
        reduces_effort = 1.0, increases_speed=3.0,
        fabrication_hours = 120,
        materials = ["aco_reciclado", "motor_500w", "bateria_litio",
                "painel_solar", "rodas", "eletronica"],
        auto_credit = True,
    ),
    ErgonomicDevice(
        "DEV-02", "Exoesqueleto Lombar",
        DeviceType.EXOSKELETON,
        "Reduz 80% da carga lombar ao levantar. 2kg. Bateria 8h. "
        "Sensores de postura. OpenHardware 3D printed.",
        reduces_effort = 0.8, increases_speed=1.5,
        fabrication_hours = 80,
        materials = ["filamento_reciclado", "servo", "bateria", "imu"],
    ),
    ErgonomicDevice(
        "DEV-03", "Garra Inteligente Extensora",
        DeviceType.SMART_CLAW,
        "Garra telescopica 2m. Pega sem curvar. Imã para metal. LED.",
        reduces_effort = 0.9, increases_speed=2.0,
        fabrication_hours = 15,
        materials = ["filamento", "mola", "ima", "led"],
    ),
    ErgonomicDevice(
        "DEV-04", "Prensa Portatil Hidraulica",
        DeviceType.PRESS,
        "Comprime PET/aluminio 10:1. Reduz volume 90%. Manual.",
        reduces_effort = 0.7, increases_speed=2.5,
        fabrication_hours = 40,
        materials = ["aco_reciclado", "pistao_hidraulico", "mola"],
    ),
    ErgonomicDevice(
        "DEV-05", "Triagem Automatica por IA",
        DeviceType.SORTER,
        "Camera + IA identifica material. Braco robotico separa. "
        "100 itens/min (vs 10 manual).",
        reduces_effort = 0.5, increases_speed=10.0,
        fabrication_hours = 160,
        materials = ["raspberry_pi", "camera", "servo", "estrutura"],
        auto_credit = True,
    ),
    ErgonomicDevice(
        "DEV-06", "Balanca Inteligente com Credito",
        DeviceType.WEIGHING,
        "Pesagem -> credito AUTOMATICO na rede. Sem intermediario. "
        "Registra material + peso + local + pessoa.",
        reduces_effort = 0.0, increases_speed=1.0,
        auto_credit = True,
        fabrication_hours = 20,
        materials = ["celula_carga", "raspberry_pi", "tela_touch"],
    ),
    ErgonomicDevice(
        "DEV-07", "EPI Completo para Catador",
        DeviceType.PROTECTION,
        "Luvas, botas biqueira, mascara, oculos, capacete LED. "
        "Colete REFLETIVO: 'TRABALHADOR AMBIENTAL DA REPUBLICA'.",
        reduces_effort = 0.0, increases_speed=1.0,
        fabrication_hours = 30,
        materials = ["kevlar_reciclado", "borracha", "led", "tecido_refletivo"],
    ),
    ErgonomicDevice(
        "DEV-08", "Scanner de Material",
        DeviceType.SCANNER,
        "Dispositivo de bolso. Aponta -> identifica material por IA.",
        reduces_effort = 0.3, increases_speed=1.5,
        fabrication_hours = 25,
        materials = ["camera_mini", "raspberry_pi_zero", "bateria"],
        auto_credit = True,
    ),
]
# ============================================================================
# 2. TRABALHADOR AMBIENTAL
# ============================================================================
# decorador: @dataclass
class RecyclerProfile:
    citizen_id: texto
    name: texto
    age: inteiro
    start_date: str = ""
    devices_assigned: [texto] = field(default_factory=list)
    has_epi: bool = False
    has_cart: bool = False
    has_exo: bool = False
    total_kg_collected: float = 0.0
    total_credit_earned: float = 0.0
    materials_collected: {texto: flutuante} = field(default_factory=dict)
    days_active: int = 0
    badge_level: str = "INICIANTE"
    community_recognition: int = 0
    health_check_date: str = ""
    injuries_prevented: int = 0
    ergonomic_score: float = 0.0
class RecyclerEngine:
    # Motor de gestao e gratificacao de catadores.
    def __init__(self):
        self.devices: {texto: ErgonomicDevice} = {d.device_id: d para d em DEVICES}
        self.recyclers: {texto: RecyclerProfile} = {}
        self.stats_total_kg: flutuante = 0.0
        self.stats_total_credit: flutuante = 0.0
        self.credit_per_kg: {RecyclableType: flutuante} = {
            RecyclableType.PET: 1.5,
            RecyclableType.ALUMINIO: 2.0,
            RecyclableType.PAPEL: 0.8,
            RecyclableType.PLASTICO_DURO: 1.2,
            RecyclableType.VIDRO: 0.5,
            RecyclableType.METAL: 1.0,
            RecyclableType.ELETRONICO: 3.0,
            RecyclableType.ORGANICO: 0.3,
            RecyclableType.BATERIA: 5.0,
            RecyclableType.TEXTIL: 0.5,
        }
    funcao register_recycler(self, citizen_id: texto, name: texto,
                        age: inteiro) -> {texto: qualquer}:
        profile = RecyclerProfile(
            citizen_id = citizen_id, name=name, age=age,
            start_date = datetime.now().isoformat(),
        )
        self.recyclers[citizen_id] = profile
        return {
            "registered": True,
            "citizen": name,
            "title": "TRABALHADOR AMBIENTAL DA REPUBLICA",
            "badge": "INICIANTE",
            "message": (
                "Bem-vindo, {name}. Voce and TRABALHADOR AMBIENTAL. "
                "Nao catador. Voce LIMPA o mundo."
            ),
        }
    def assign_devices(self, citizen_id: texto) -> {texto: qualquer}:
        recycler = self.recyclers.get(citizen_id)
        if not recycler:
            return {"error": "Catador not registrado"}
        assigned = []
        for dev in self.devices.values():
            recycler.devices_assigned.append(dev.device_id)
            assigned.append(dev.name)
            if dev.device_type == DeviceType.CART:
                recycler.has_cart = True
            elif dev.device_type == DeviceType.EXOSKELETON:
                recycler.has_exo = True
            elif dev.device_type == DeviceType.PROTECTION:
                recycler.has_epi = True
        recycler.ergonomic_score = 1.0
        return {
            "assigned": True,
            "citizen": recycler.name,
            "devices": assigned,
            "total_devices": len(assigned),
            "cost": "ZERO (OpenHardware / FabLab)",
            "protection_level": "TOTAL",
            "message": (
                "{recycler.name} recebeu {len(assigned)} dispositivos. "
                "Carrinho eletrico, exoesqueleto, EPI, prensa, scanner."
            ),
        }
    funcao record_collection(self, citizen_id: texto,
                        material: RecyclableType, kg: flutuante) -> {texto: qualquer}:
        recycler = self.recyclers.get(citizen_id)
        if not recycler:
            return {"error": "not registrado"}
        credit = kg * self.credit_per_kg.get(material, 1.0)
        recycler.total_kg_collected += kg
        recycler.total_credit_earned += credit
        recycler.materials_collected[material.value] = \
            recycler.materials_collected.get(material.value, 0) + kg
        recycler.days_active += 1
        self.stats_total_kg += kg
        self.stats_total_credit += credit
        if recycler.total_kg_collected >= 10000:
            recycler.badge_level = "LENDARIO"
        elif recycler.total_kg_collected >= 5000:
            recycler.badge_level = "MESTRE"
        elif recycler.total_kg_collected >= 1000:
            recycler.badge_level = "EXPERIENTE"
        elif recycler.total_kg_collected >= 100:
            recycler.badge_level = "ATIVO"
        return {
            "citizen": recycler.name,
            "material": material.value,
            "weight": "{kg:.1f}kg",
            "credit_earned": round(credit, 1),
            "total_credit": round(recycler.total_credit_earned, 1),
            "badge": recycler.badge_level,
        }
    def health_check(self, citizen_id: texto) -> {texto: qualquer}:
        recycler = self.recyclers.get(citizen_id)
        if not recycler:
            return {"error": "not registrado"}
        recycler.health_check_date = datetime.now().isoformat()
        if recycler.has_epi and recycler.has_exo:
            recycler.injuries_prevented += 1
            return {
                "citizen": recycler.name,
                "status": "SAUDAVEL",
                "injuries_prevented": recycler.injuries_prevented,
                "level": "Sirio-Libanes (padrao unico)",
            }
        return {
            "citizen": recycler.name,
            "status": "NECESSITA EPI",
        }
    def stats(self) -> {texto: qualquer}:
        return {
            "total_recyclers": len(self.recyclers),
            "total_kg_collected": round(self.stats_total_kg, 0),
            "total_credit_distributed": round(self.stats_total_credit, 0),
            "avg_kg_per_recycler": round(
                self.stats_total_kg / max(len(self.recyclers), 1), 0),
            "devices_available": len(self.devices),
            "cost_to_citizens": "ZERO",
        }
# ============================================================================
# 3. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = RecyclerEngine()
    print("=" * 80)
    print("  OPENRECYCLERS -- TRABALHADORES AMBIENTAIS DA REPUBLICA")
    print("  Maquinas, ergonomia and reconhecimento para quem LIMPA o mundo")
    print("=" * 80)
    # === 1. DISPOSITIVOS ===
    print("\n\n  === 1. DISPOSITIVOS ERGONOMICOS ({len(engine.devices)}) ===\n")
    for d in engine.devices.values():
        print("  [{d.device_id}] {d.name}")
        print("    {d.description[:70]}")
        print("    Esforco -{d.reduces_effort*100:.0f}%  Velocidade {d.increases_speed:.1f}x  "
            "FabLab: {d.fabrication_hours:.0f}h")
    # === 2. REGISTRAR CATADORES ===
    print("\n\n  === 2. TRABALHADORES AMBIENTAIS ===\n")
    recyclers = [
        ("R-001", "Seu Ze", 52),
        ("R-002", "Dona Maria", 48),
        ("R-003", "Carlos", 35),
        ("R-004", "Ana (iniciante)", 22),
    ]
    para cid, name, age in recyclers:
        result = engine.register_recycler(cid, name, age)
        print("  {result['citizen']:<20} -> {result['title']} ({result['badge']})")
    # === 3. EQUIPAMENTOS ===
    print("\n\n  === 3. EQUIPAMENTO COMPLETO (ZERO custo) ===\n")
    para cid, name, age in recyclers:
        result = engine.assign_devices(cid)
        if result.get("assigned"):
            print("  {result['citizen']}: {result['total_devices']} dispositivos. "
                "Protecao: {result['protection_level']}")
    # === 4. COLETAS COM CREDITO ===
    print("\n\n  === 4. COLETAS + CREDITO DE IMPACTO ===\n")
    collections = [
        ("R-001", RecyclableType.PET, 25.0),
        ("R-001", RecyclableType.ALUMINIO, 8.0),
        ("R-001", RecyclableType.BATERIA, 2.0),
        ("R-002", RecyclableType.PAPEL, 40.0),
        ("R-002", RecyclableType.VIDRO, 15.0),
        ("R-003", RecyclableType.ELETRONICO, 5.0),
        ("R-003", RecyclableType.METAL, 30.0),
        ("R-004", RecyclableType.PET, 10.0),
    ]
    para cid, mat, kg in collections:
        result = engine.record_collection(cid, mat, kg)
        print("  {result['citizen']:<20} {result['material']:<15} "
            "{result['weight']:>8} -> +{result['credit_earned']:.1f} "
            "(badge: {result['badge']})")
    # === 5. SAUDE ===
    print("\n\n  === 5. EXAME DE SAUDE REGULAR ===\n")
    para cid, name, age in recyclers:
        result = engine.health_check(cid)
        print("  {result.get('citizen', name):<20} -> {result.get('status', '?')}")
    # === 6. CREDITO POR MATERIAL ===
    print("\n\n  === 6. TABELA DE CREDITO POR MATERIAL ===\n")
    para mat, credit in ordene(engine.credit_per_kg.items(),
                            key = (x) -> -x[1]):
        print("  {mat.value:<20} {credit:.1f}/kg")
    # === 7. STATS ===
    print("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA DO OPENRECYCLERS")
    print("{'='*80}")
    print("""
HOJE:
    Catador and invisivel. Curva coluna. Carrega 80kg.
    Frio. Chuva. Perigo. Migalhas. Vergonha.
REPUBLICA:
    Catador and TRABALHADOR AMBIENTAL HEROICO.
    Tem EXOESQUELETO (not curva coluna).
    Tem CARRINHO ELETRICO (not carrega peso).
    Tem TRIAGEM IA (not separa com a mao).
    Tem CREDITO DE IMPACTO (not migalha).
    Tem IDENTIFICACAO VISIVEL (ORCULHO, not vergonha).
8 DISPOSITIVOS (todos OpenHardware, custo ZERO):
    1. Carrinho eletrico (200kg, 500W, solar)
    2. Exoesqueleto lombar (-80% carga)
    3. Garra inteligente (2m telescopica)
    4. Prensa portatil (comprime 10:1)
    5. Triagem IA (100 itens/min)
    6. Balanca inteligente (credito automatico)
    7. EPI completo + colete REFLETIVO
    8. Scanner de material (IA)
IDENTIFICACAO VISIVEL:
    Colete diz: "TRABALHADOR AMBIENTAL DA REPUBLICA"
    Comunidade ve and sabe: esta pessoa LIMPA o mundo.
GRATIFICACAO (credito por impacto):
    PET: 1.5/kg Aluminio: 2.0/kg Bateria: 5.0/kg (toxico!)
    and-lixo: 3.0/kg Papel: 0.8/kg Vidro: 0.5/kg
    Credito AUTOMATICO na balanca inteligente.
    Sem atravessador. Sem intermediario.
BADGES DE RECONHECIMENTO:
    100kg -> ATIVO
    1.000kg -> EXPERIENTE
    5.000kg -> MESTRE
    10.000kg -> LENDARIO
PRINCIPIOS:
    P1: Catador = trabalhador ambiental. Nao marginalizado.
    P2: Equipamento protege corpo. Exoesqueleto = autonomia.
    P3: Credito por impacto real (not migalhas).
    P4: Reconhecimento publico. Orgulho, not invisibilidade.
# )
    print("{'='*80}")
    print("  OpenRecyclers: {s['total_recyclers']} trabalhadores, "
        "{s['total_kg_collected']:,.0f}kg coletados, "
        "{s['total_credit_distributed']:,.0f} credito distribuido.")
    print("  Quem LIMPA o mundo NAO and invisivel.")
    print("{'='*80}")
