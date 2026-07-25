# OpenRecyclers -- Dispositivos, Maquinas e Gratificacao para Catadores

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_recyclers.py`

**Descricao:** =====================================================================
"Quem recolhe o que outros jogaram fora NAO e 'catador'.
 E TRABALHADOR AMBIENTAL. E quem LIMPA o mundo."
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRecyclers -- Dispositivos, Maquinas e Gratificacao para Catadores
=====================================================================

"Quem recolhe o que outros jogaram fora nao e 'catador'.
 e TRABALHADOR AMBIENTAL. e quem LIMPA o mundo."

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime


// ============================================================================
// 1. MATERIAIS RECICLAVEIS
// ============================================================================

classe RecyclableType herda de Enum:
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


classe DeviceType herda de Enum:
    CART = "carrinho_eletrico"
    EXOSKELETON = "exoesqueleto"
    SMART_CLAW = "garra_inteligente"
    PRESS = "prensa_portatil"
    SORTER = "triagem_automatica"
    WEIGHING = "balanca_inteligente"
    PROTECTION = "equipamento_protecao"
    SCANNER = "scanner_material"


// decorador: @dataclass
classe ErgonomicDevice:
    device_id: texto
    name: texto
    device_type: DeviceType
    seja description: texto = ""
    seja reduces_effort: flutuante = 0.8
    seja increases_speed: flutuante = 2.0
    seja auto_credit: logico = falso
    seja fabrication_hours: flutuante = 20.0
    seja materials: [texto] = field(default_factory=list)


seja DEVICES: [ErgonomicDevice] = [
    ErgonomicDevice(
        "DEV-01", "Carrinho Eletrico Cargueiro",
        DeviceType.CART,
        "Carrinho motorizado 500W. Carrega 200kg. Bateria solar. "
        "5 compartimentos por material. GPS. Autonomia 30km.",
        reduces_effort = 1.0, increases_speed=3.0,
        fabrication_hours = 120,
        materials = ["aco_reciclado", "motor_500w", "bateria_litio",
                   "painel_solar", "rodas", "eletronica"],
        auto_credit = verdadeiro,
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
        auto_credit = verdadeiro,
    ),
    ErgonomicDevice(
        "DEV-06", "Balanca Inteligente com Credito",
        DeviceType.WEIGHING,
        "Pesagem -> credito AUTOMATICO na rede. Sem intermediario. "
        "Registra material + peso + local + pessoa.",
        reduces_effort = 0.0, increases_speed=1.0,
        auto_credit = verdadeiro,
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
        auto_credit = verdadeiro,
    ),
]


// ============================================================================
// 2. TRABALHADOR AMBIENTAL
// ============================================================================

// decorador: @dataclass
classe RecyclerProfile:
    citizen_id: texto
    name: texto
    age: inteiro
    seja start_date: texto = ""
    seja devices_assigned: [texto] = field(default_factory=list)
    seja has_epi: logico = falso
    seja has_cart: logico = falso
    seja has_exo: logico = falso
    seja total_kg_collected: flutuante = 0.0
    seja total_credit_earned: flutuante = 0.0
    seja materials_collected: {texto: flutuante} = field(default_factory=dict)
    seja days_active: inteiro = 0
    seja badge_level: texto = "INICIANTE"
    seja community_recognition: inteiro = 0
    seja health_check_date: texto = ""
    seja injuries_prevented: inteiro = 0
    seja ergonomic_score: flutuante = 0.0


classe RecyclerEngine:
    // Motor de gestao e gratificacao de catadores.

    funcao __init__(self):
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
        retorne {
            "registered": verdadeiro,
            "citizen": name,
            "title": "TRABALHADOR AMBIENTAL DA REPUBLICA",
            "badge": "INICIANTE",
            "message": (
                "Bem-vindo, {name}. Voce e TRABALHADOR AMBIENTAL. "
                "Nao catador. Voce LIMPA o mundo."
            ),
        }

    funcao assign_devices(self, citizen_id: texto) -> {texto: qualquer}:
        recycler = self.recyclers.get(citizen_id)
        se nao recycler entao:
            retorne {"error": "Catador nao registrado"}

        assigned = []
        para cada dev em self.devices.values():
            recycler.devices_assigned.append(dev.device_id)
            assigned.append(dev.name)
            se dev.device_type == DeviceType.CART entao:
                recycler.has_cart = verdadeiro
            senao se dev.device_type == DeviceType.EXOSKELETON entao:
                recycler.has_exo = verdadeiro
            senao se dev.device_type == DeviceType.PROTECTION entao:
                recycler.has_epi = verdadeiro

        recycler.ergonomic_score = 1.0

        retorne {
            "assigned": verdadeiro,
            "citizen": recycler.name,
            "devices": assigned,
            "total_devices": tamanho(assigned),
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
        se nao recycler entao:
            retorne {"error": "nao registrado"}

        credit = kg * self.credit_per_kg.get(material, 1.0)
        recycler.total_kg_collected += kg
        recycler.total_credit_earned += credit
        recycler.materials_collected[material.value] = \
            recycler.materials_collected.get(material.value, 0) + kg
        recycler.days_active += 1
        self.stats_total_kg += kg
        self.stats_total_credit += credit

        se recycler.total_kg_collected >= 10000 entao:
            recycler.badge_level = "LENDARIO"
        senao se recycler.total_kg_collected >= 5000 entao:
            recycler.badge_level = "MESTRE"
        senao se recycler.total_kg_collected >= 1000 entao:
            recycler.badge_level = "EXPERIENTE"
        senao se recycler.total_kg_collected >= 100 entao:
            recycler.badge_level = "ATIVO"

        retorne {
            "citizen": recycler.name,
            "material": material.value,
            "weight": "{kg:.1f}kg",
            "credit_earned": arredonde(credit, 1),
            "total_credit": arredonde(recycler.total_credit_earned, 1),
            "badge": recycler.badge_level,
        }

    funcao health_check(self, citizen_id: texto) -> {texto: qualquer}:
        recycler = self.recyclers.get(citizen_id)
        se nao recycler entao:
            retorne {"error": "nao registrado"}

        recycler.health_check_date = datetime.now().isoformat()
        se recycler.has_epi e recycler.has_exo entao:
            recycler.injuries_prevented += 1
            retorne {
                "citizen": recycler.name,
                "status": "SAUDAVEL",
                "injuries_prevented": recycler.injuries_prevented,
                "level": "Sirio-Libanes (padrao unico)",
            }
        retorne {
            "citizen": recycler.name,
            "status": "NECESSITA EPI",
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_recyclers": tamanho(self.recyclers),
            "total_kg_collected": arredonde(self.stats_total_kg, 0),
            "total_credit_distributed": arredonde(self.stats_total_credit, 0),
            "avg_kg_per_recycler": arredonde(
                self.stats_total_kg / maximo(tamanho(self.recyclers), 1), 0),
            "devices_available": tamanho(self.devices),
            "cost_to_citizens": "ZERO",
        }


// ============================================================================
// 3. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = RecyclerEngine()

    imprima("=" * 80)
    imprima("  OPENRECYCLERS -- TRABALHADORES AMBIENTAIS DA REPUBLICA")
    imprima("  Maquinas, ergonomia e reconhecimento para quem LIMPA o mundo")
    imprima("=" * 80)

    // === 1. DISPOSITIVOS ===
    imprima("\n\n  === 1. DISPOSITIVOS ERGONOMICOS ({len(engine.devices)}) ===\n")
    para cada d em engine.devices.values():
        imprima("  [{d.device_id}] {d.name}")
        imprima("    {d.description[:70]}")
        imprima("    Esforco -{d.reduces_effort*100:.0f}%  Velocidade {d.increases_speed:.1f}x  "
              "FabLab: {d.fabrication_hours:.0f}h")

    // === 2. REGISTRAR CATADORES ===
    imprima("\n\n  === 2. TRABALHADORES AMBIENTAIS ===\n")
    recyclers = [
        ("R-001", "Seu Ze", 52),
        ("R-002", "Dona Maria", 48),
        ("R-003", "Carlos", 35),
        ("R-004", "Ana (iniciante)", 22),
    ]
    para cid, name, age in recyclers:
        result = engine.register_recycler(cid, name, age)
        imprima("  {result['citizen']:<20} -> {result['title']} ({result['badge']})")

    // === 3. EQUIPAMENTOS ===
    imprima("\n\n  === 3. EQUIPAMENTO COMPLETO (ZERO custo) ===\n")
    para cid, name, age in recyclers:
        result = engine.assign_devices(cid)
        se result.get("assigned") entao:
            imprima("  {result['citizen']}: {result['total_devices']} dispositivos. "
                  "Protecao: {result['protection_level']}")

    // === 4. COLETAS COM CREDITO ===
    imprima("\n\n  === 4. COLETAS + CREDITO DE IMPACTO ===\n")
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
        imprima("  {result['citizen']:<20} {result['material']:<15} "
              "{result['weight']:>8} -> +{result['credit_earned']:.1f} "
              "(badge: {result['badge']})")

    // === 5. SAUDE ===
    imprima("\n\n  === 5. EXAME DE SAUDE REGULAR ===\n")
    para cid, name, age in recyclers:
        result = engine.health_check(cid)
        imprima("  {result.get('citizen', name):<20} -> {result.get('status', '?')}")

    // === 6. CREDITO POR MATERIAL ===
    imprima("\n\n  === 6. TABELA DE CREDITO POR MATERIAL ===\n")
    para mat, credit in ordene(engine.credit_per_kg.items(),
                              key = (x) -> -x[1]):
        imprima("  {mat.value:<20} {credit:.1f}/kg")

    // === 7. STATS ===
    imprima("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DO OPENRECYCLERS")
    imprima("{'='*80}")
    imprima("""
  HOJE:
    Catador e invisivel. Curva coluna. Carrega 80kg.
    Frio. Chuva. Perigo. Migalhas. Vergonha.

  REPUBLICA:
    Catador e TRABALHADOR AMBIENTAL HEROICO.
    Tem EXOESQUELETO (nao curva coluna).
    Tem CARRINHO ELETRICO (nao carrega peso).
    Tem TRIAGEM IA (nao separa com a mao).
    Tem CREDITO DE IMPACTO (nao migalha).
    Tem IDENTIFICACAO VISIVEL (ORCULHO, nao vergonha).

  8 DISPOSITIVOS (todos OpenHardware, custo ZERO):
    1. Carrinho eletrico (200kg, 500W, solar)
    2. Exoesqueleto lombar (-80% carga)
    3. Garra inteligente (2m telescopica)
    4. Prensa portatil (comprime 10:1)
    5. Triagem IA (100 itens/minimo)
    6. Balanca inteligente (credito automatico)
    7. EPI completo + colete REFLETIVO
    8. Scanner de material (IA)

  IDENTIFICACAO VISIVEL:
    Colete diz: "TRABALHADOR AMBIENTAL DA REPUBLICA"
    Comunidade ve e sabe: esta pessoa LIMPA o mundo.

  GRATIFICACAO (credito por impacto):
    PET: 1.5/kg Aluminio: 2.0/kg Bateria: 5.0/kg (toxico!)
    e-lixo: 3.0/kg Papel: 0.8/kg Vidro: 0.5/kg
    Credito AUTOMATICO na balanca inteligente.
    Sem atravessador. Sem intermediario.

  BADGES DE RECONHECIMENTO:
    100kg -> ATIVO
    1.000kg -> EXPERIENTE
    5.000kg -> MESTRE
    10.000kg -> LENDARIO

  PRINCIPIOS:
    seja P1: Catador = trabalhador ambiental. Nao marginalizado.
    seja P2: Equipamento protege corpo. Exoesqueleto = autonomia.
    P3: Credito por impacto real (nao migalhas).
    P4: Reconhecimento publico. Orgulho, nao invisibilidade.
// )
    imprima("{'='*80}")
    imprima("  OpenRecyclers: {s['total_recyclers']} trabalhadores, "
          "{s['total_kg_collected']:,.0f}kg coletados, "
          "{s['total_credit_distributed']:,.0f} credito distribuido.")
    imprima("  Quem LIMPA o mundo NAO e invisivel.")
    imprima("{'='*80}")

```
