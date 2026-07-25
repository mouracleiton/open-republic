// OpenRecyclers -- Dispositivos, Maquinas e Gratificacao para Catadores -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenRecyclers -- Dispositivos, Maquinas && Gratificacao para Catadores;
=====================================================================;
"Quem recolhe o que outros jogaram fora ! && 'catador'.;
&& TRABALHADOR AMBIENTAL. && quem LIMPA o mundo.";
Author: OpenRepublic Team;
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
class RecyclableType {
    PET = "pet";
    ALUMINIO = "aluminio";
    PAPEL = "papel";
    PLASTICO_DURO = "plastico_duro";
    VIDRO = "vidro";
    METAL = "metal";
    ELETRONICO = "eletronico";
    ORGANICO = "organico";
    BATERIA = "bateria";
    TEXTIL = "textil";
class DeviceType {
    CART = "carrinho_eletrico";
    EXOSKELETON = "exoesqueleto";
    SMART_CLAW = "garra_inteligente";
    PRESS = "prensa_portatil";
    SORTER = "triagem_automatica";
    WEIGHING = "balanca_inteligente";
    PROTECTION = "equipamento_protecao";
    SCANNER = "scanner_material";
// decorador: @dataclass
class ErgonomicDevice {
    device_id: texto;
    name: texto;
    device_type: DeviceType;
    const description = "";
    const reduces_effort = 0.8;
    const increases_speed = 2.0;
    const auto_credit = false;
    const fabrication_hours = 20.0;
    const materials = field(default_factory=list);
const DEVICES = [;
    ErgonomicDevice(;
        "DEV-01", "Carrinho Eletrico Cargueiro",;
        DeviceType.CART,;
        "Carrinho motorizado 500W. Carrega 200kg. Bateria solar. ";
        "5 compartimentos por material. GPS. Autonomia 30km.",;
        reduces_effort = 1.0, increases_speed=3.0,;
        fabrication_hours = 120,;
        materials = ["aco_reciclado", "motor_500w", "bateria_litio",;
                "painel_solar", "rodas", "eletronica"],;
        auto_credit = true,;
    ),;
    ErgonomicDevice(;
        "DEV-02", "Exoesqueleto Lombar",;
        DeviceType.EXOSKELETON,;
        "Reduz 80% da carga lombar ao levantar. 2kg. Bateria 8h. ";
        "Sensores de postura. OpenHardware 3D printed.",;
        reduces_effort = 0.8, increases_speed=1.5,;
        fabrication_hours = 80,;
        materials = ["filamento_reciclado", "servo", "bateria", "imu"],;
    ),;
    ErgonomicDevice(;
        "DEV-03", "Garra Inteligente Extensora",;
        DeviceType.SMART_CLAW,;
        "Garra telescopica 2m. Pega sem curvar. Imã para metal. LED.",;
        reduces_effort = 0.9, increases_speed=2.0,;
        fabrication_hours = 15,;
        materials = ["filamento", "mola", "ima", "led"],;
    ),;
    ErgonomicDevice(;
        "DEV-04", "Prensa Portatil Hidraulica",;
        DeviceType.PRESS,;
        "Comprime PET/aluminio 10:1. Reduz volume 90%. Manual.",;
        reduces_effort = 0.7, increases_speed=2.5,;
        fabrication_hours = 40,;
        materials = ["aco_reciclado", "pistao_hidraulico", "mola"],;
    ),;
    ErgonomicDevice(;
        "DEV-05", "Triagem Automatica por IA",;
        DeviceType.SORTER,;
        "Camera + IA identifica material. Braco robotico separa. ";
        "100 itens/min (vs 10 manual).",;
        reduces_effort = 0.5, increases_speed=10.0,;
        fabrication_hours = 160,;
        materials = ["raspberry_pi", "camera", "servo", "estrutura"],;
        auto_credit = true,;
    ),;
    ErgonomicDevice(;
        "DEV-06", "Balanca Inteligente com Credito",;
        DeviceType.WEIGHING,;
        "Pesagem -> credito AUTOMATICO na rede. Sem intermediario. ";
        "Registra material + peso + local + pessoa.",;
        reduces_effort = 0.0, increases_speed=1.0,;
        auto_credit = true,;
        fabrication_hours = 20,;
        materials = ["celula_carga", "raspberry_pi", "tela_touch"],;
    ),;
    ErgonomicDevice(;
        "DEV-07", "EPI Completo para Catador",;
        DeviceType.PROTECTION,;
        "Luvas, botas biqueira, mascara, oculos, capacete LED. ";
        "Colete REFLETIVO: 'TRABALHADOR AMBIENTAL DA REPUBLICA'.",;
        reduces_effort = 0.0, increases_speed=1.0,;
        fabrication_hours = 30,;
        materials = ["kevlar_reciclado", "borracha", "led", "tecido_refletivo"],;
    ),;
    ErgonomicDevice(;
        "DEV-08", "Scanner de Material",;
        DeviceType.SCANNER,;
        "Dispositivo de bolso. Aponta -> identifica material por IA.",;
        reduces_effort = 0.3, increases_speed=1.5,;
        fabrication_hours = 25,;
        materials = ["camera_mini", "raspberry_pi_zero", "bateria"],;
        auto_credit = true,;
    ),;
];
// ============================================================================
// 2. TRABALHADOR AMBIENTAL
// ============================================================================
// decorador: @dataclass
class RecyclerProfile {
    citizen_id: texto;
    name: texto;
    age: inteiro;
    const start_date = "";
    const devices_assigned = field(default_factory=list);
    const has_epi = false;
    const has_cart = false;
    const has_exo = false;
    const total_kg_collected = 0.0;
    const total_credit_earned = 0.0;
    const materials_collected = field(default_factory=dict);
    const days_active = 0;
    const badge_level = "INICIANTE";
    const community_recognition = 0;
    const health_check_date = "";
    const injuries_prevented = 0;
    const ergonomic_score = 0.0;
class RecyclerEngine {
    // Motor de gestao e gratificacao de catadores.
    __init__(self) {
        self.devices: {texto: ErgonomicDevice} = {d.device_id: d para d em DEVICES};
        self.recyclers: {texto: RecyclerProfile} = {};
        self.stats_total_kg: flutuante = 0.0;
        self.stats_total_credit: flutuante = 0.0;
        self.credit_per_kg: {RecyclableType: flutuante} = {
            RecyclableType.PET: 1.5,;
            RecyclableType.ALUMINIO: 2.0,;
            RecyclableType.PAPEL: 0.8,;
            RecyclableType.PLASTICO_DURO: 1.2,;
            RecyclableType.VIDRO: 0.5,;
            RecyclableType.METAL: 1.0,;
            RecyclableType.ELETRONICO: 3.0,;
            RecyclableType.ORGANICO: 0.3,;
            RecyclableType.BATERIA: 5.0,;
            RecyclableType.TEXTIL: 0.5,;
        };
    funcao register_recycler(self, citizen_id: texto, name: texto,
                        age: inteiro) -> {texto: qualquer}:;
        profile = RecyclerProfile(;
            citizen_id = citizen_id, name=name, age=age,;
            start_date = datetime.now().isoformat(),;
        );
        self.recyclers[citizen_id] = profile;
        return {;
            "registered": true,;
            "citizen": name,;
            "title": "TRABALHADOR AMBIENTAL DA REPUBLICA",;
            "badge": "INICIANTE",;
            "message": (;
                "Bem-vindo, {name}. Voce && TRABALHADOR AMBIENTAL. ";
                "Nao catador. Voce LIMPA o mundo.";
            ),;
        };
    assign_devices(self, citizen_id: texto) {
        recycler = self.recyclers.get(citizen_id);
        if (! recycler) {
            return {"error": "Catador ! registrado"};
        assigned = [];
        for (const dev of self.devices.values()) {
            recycler.devices_assigned.append(dev.device_id);
            assigned.append(dev.name);
            if (dev.device_type == DeviceType.CART) {
                recycler.has_cart = true;
            } else if (dev.device_type == DeviceType.EXOSKELETON) {
                recycler.has_exo = true;
            } else if (dev.device_type == DeviceType.PROTECTION) {
                recycler.has_epi = true;
        recycler.ergonomic_score = 1.0;
        return {;
            "assigned": true,;
            "citizen": recycler.name,;
            "devices": assigned,;
            "total_devices": .length(assigned),;
            "cost": "ZERO (OpenHardware / FabLab)",;
            "protection_level": "TOTAL",;
            "message": (;
                "{recycler.name} recebeu {len(assigned)} dispositivos. ";
                "Carrinho eletrico, exoesqueleto, EPI, prensa, scanner.";
            ),;
        };
    funcao record_collection(self, citizen_id: texto,
                        material: RecyclableType, kg: flutuante) -> {texto: qualquer}:;
        recycler = self.recyclers.get(citizen_id);
        if (! recycler) {
            return {"error": "! registrado"};
        credit = kg * self.credit_per_kg.get(material, 1.0);
        recycler.total_kg_collected += kg;
        recycler.total_credit_earned += credit;
        recycler.materials_collected[material.value] = \;
            recycler.materials_collected.get(material.value, 0) + kg;
        recycler.days_active += 1;
        self.stats_total_kg += kg;
        self.stats_total_credit += credit;
        if (recycler.total_kg_collected >= 10000) {
            recycler.badge_level = "LENDARIO";
        } else if (recycler.total_kg_collected >= 5000) {
            recycler.badge_level = "MESTRE";
        } else if (recycler.total_kg_collected >= 1000) {
            recycler.badge_level = "EXPERIENTE";
        } else if (recycler.total_kg_collected >= 100) {
            recycler.badge_level = "ATIVO";
        return {;
            "citizen": recycler.name,;
            "material": material.value,;
            "weight": "{kg:.1f}kg",;
            "credit_earned": arredonde(credit, 1),;
            "total_credit": arredonde(recycler.total_credit_earned, 1),;
            "badge": recycler.badge_level,;
        };
    health_check(self, citizen_id: texto) {
        recycler = self.recyclers.get(citizen_id);
        if (! recycler) {
            return {"error": "! registrado"};
        recycler.health_check_date = datetime.now().isoformat();
        if (recycler.has_epi && recycler.has_exo) {
            recycler.injuries_prevented += 1;
            return {;
                "citizen": recycler.name,;
                "status": "SAUDAVEL",;
                "injuries_prevented": recycler.injuries_prevented,;
                "level": "Sirio-Libanes (padrao unico)",;
            };
        return {;
            "citizen": recycler.name,;
            "status": "NECESSITA EPI",;
        };
    stats(self) {
        return {;
            "total_recyclers": .length(self.recyclers),;
            "total_kg_collected": arredonde(self.stats_total_kg, 0),;
            "total_credit_distributed": arredonde(self.stats_total_credit, 0),;
            "avg_kg_per_recycler": arredonde(;
                self.stats_total_kg / maximo(.length(self.recyclers), 1), 0),;
            "devices_available": .length(self.devices),;
            "cost_to_citizens": "ZERO",;
        };
// ============================================================================
// 3. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = RecyclerEngine();
    console.log("=" * 80);
    console.log("  OPENRECYCLERS -- TRABALHADORES AMBIENTAIS DA REPUBLICA");
    console.log("  Maquinas, ergonomia && reconhecimento para quem LIMPA o mundo");
    console.log("=" * 80);
    // === 1. DISPOSITIVOS ===
    console.log("\n\n  === 1. DISPOSITIVOS ERGONOMICOS ({len(engine.devices)}) ===\n");
    for (const d of engine.devices.values()) {
        console.log("  [{d.device_id}] {d.name}");
        console.log("    {d.description[:70]}");
        console.log("    Esforco -{d.reduces_effort*100:.0f}%  Velocidade {d.increases_speed:.1f}x  ";
            "FabLab: {d.fabrication_hours:.0f}h");
    // === 2. REGISTRAR CATADORES ===
    console.log("\n\n  === 2. TRABALHADORES AMBIENTAIS ===\n");
    recyclers = [;
        ("R-001", "Seu Ze", 52),;
        ("R-002", "Dona Maria", 48),;
        ("R-003", "Carlos", 35),;
        ("R-004", "Ana (iniciante)", 22),;
    ];
    para cid, name, age in recyclers: {
        result = engine.register_recycler(cid, name, age);
        console.log("  {result['citizen']:<20} -> {result['title']} ({result['badge']})");
    // === 3. EQUIPAMENTOS ===
    console.log("\n\n  === 3. EQUIPAMENTO COMPLETO (ZERO custo) ===\n");
    para cid, name, age in recyclers: {
        result = engine.assign_devices(cid);
        if (result.get("assigned")) {
            console.log("  {result['citizen']}: {result['total_devices']} dispositivos. ";
                "Protecao: {result['protection_level']}");
    // === 4. COLETAS COM CREDITO ===
    console.log("\n\n  === 4. COLETAS + CREDITO DE IMPACTO ===\n");
    collections = [;
        ("R-001", RecyclableType.PET, 25.0),;
        ("R-001", RecyclableType.ALUMINIO, 8.0),;
        ("R-001", RecyclableType.BATERIA, 2.0),;
        ("R-002", RecyclableType.PAPEL, 40.0),;
        ("R-002", RecyclableType.VIDRO, 15.0),;
        ("R-003", RecyclableType.ELETRONICO, 5.0),;
        ("R-003", RecyclableType.METAL, 30.0),;
        ("R-004", RecyclableType.PET, 10.0),;
    ];
    para cid, mat, kg in collections: {
        result = engine.record_collection(cid, mat, kg);
        console.log("  {result['citizen']:<20} {result['material']:<15} ";
            "{result['weight']:>8} -> +{result['credit_earned']:.1f} ";
            "(badge: {result['badge']})");
    // === 5. SAUDE ===
    console.log("\n\n  === 5. EXAME DE SAUDE REGULAR ===\n");
    para cid, name, age in recyclers: {
        result = engine.health_check(cid);
        console.log("  {result.get('citizen', name):<20} -> {result.get('status', '?')}");
    // === 6. CREDITO POR MATERIAL ===
    console.log("\n\n  === 6. TABELA DE CREDITO POR MATERIAL ===\n");
    para mat, credit in ordene(engine.credit_per_kg.items(), {
                            key = (x) -> -x[1]):;
        console.log("  {mat.value:<20} {credit:.1f}/kg");
    // === 7. STATS ===
    console.log("\n\n  === 7. ESTATISTICAS ===\n");
    s = engine.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<30} {v}");
    // === FILOSOFIA ===
    console.log("\n\n{'='*80}");
    console.log("  FILOSOFIA DO OPENRECYCLERS");
    console.log("{'='*80}");
    console.log(""";
HOJE:;
    Catador && invisivel. Curva coluna. Carrega 80kg.;
    Frio. Chuva. Perigo. Migalhas. Vergonha.;
REPUBLICA:;
    Catador && TRABALHADOR AMBIENTAL HEROICO.;
    Tem EXOESQUELETO (! curva coluna).;
    Tem CARRINHO ELETRICO (! carrega peso).;
    Tem TRIAGEM IA (! separa com a mao).;
    Tem CREDITO DE IMPACTO (! migalha).;
    Tem IDENTIFICACAO VISIVEL (ORCULHO, ! vergonha).;
8 DISPOSITIVOS (todos OpenHardware, custo ZERO):;
    1. Carrinho eletrico (200kg, 500W, solar);
    2. Exoesqueleto lombar (-80% carga);
    3. Garra inteligente (2m telescopica);
    4. Prensa portatil (comprime 10:1);
    5. Triagem IA (100 itens/minimo);
    6. Balanca inteligente (credito automatico);
    7. EPI completo + colete REFLETIVO;
    8. Scanner de material (IA);
IDENTIFICACAO VISIVEL:;
    Colete diz: "TRABALHADOR AMBIENTAL DA REPUBLICA";
    Comunidade ve && sabe: esta pessoa LIMPA o mundo.;
GRATIFICACAO (credito por impacto):;
    PET: 1.5/kg Aluminio: 2.0/kg Bateria: 5.0/kg (toxico!);
    &&-lixo: 3.0/kg Papel: 0.8/kg Vidro: 0.5/kg;
    Credito AUTOMATICO na balanca inteligente.;
    Sem atravessador. Sem intermediario.;
BADGES DE RECONHECIMENTO:;
    100kg -> ATIVO;
    1.000kg -> EXPERIENTE;
    5.000kg -> MESTRE;
    10.000kg -> LENDARIO;
PRINCIPIOS:;
    const P1 = trabalhador ambiental. Nao marginalizado.;
    const P2 = autonomia.;
    P3: Credito por impacto real (! migalhas).;
    P4: Reconhecimento publico. Orgulho, ! invisibilidade.;
// )
    console.log("{'='*80}");
    console.log("  OpenRecyclers: {s['total_recyclers']} trabalhadores, ";
        "{s['total_kg_collected']:,.0f}kg coletados, ";
        "{s['total_credit_distributed']:,.0f} credito distribuido.");
    console.log("  Quem LIMPA o mundo NAO && invisivel.");
    console.log("{'='*80}");
