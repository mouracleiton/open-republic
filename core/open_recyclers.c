/* OpenRecyclers -- Dispositivos, Maquinas e Gratificacao para Catadores -- gerado de Portugol++ */
#ifndef OPENRECYCLERS_DISPOSITIVOS_MAQUINAS_E_GRATIFICACAO_PARA_CATADORES_H
#define OPENRECYCLERS_DISPOSITIVOS_MAQUINAS_E_GRATIFICACAO_PARA_CATADORES_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

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
typedef struct RecyclableType {
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
typedef struct DeviceType {
    CART = "carrinho_eletrico";
    EXOSKELETON = "exoesqueleto";
    SMART_CLAW = "garra_inteligente";
    PRESS = "prensa_portatil";
    SORTER = "triagem_automatica";
    WEIGHING = "balanca_inteligente";
    PROTECTION = "equipamento_protecao";
    SCANNER = "scanner_material";
// decorador: @dataclass
typedef struct ErgonomicDevice {
    device_id: texto;
    name: texto;
    device_type: DeviceType;
    char* description = "";
    double reduces_effort = 0.8;
    double increases_speed = 2.0;
    bool auto_credit = false;
    double fabrication_hours = 20.0;
    [texto] materials = field(default_factory=list);
[ErgonomicDevice] DEVICES = [;
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
typedef struct RecyclerProfile {
    citizen_id: texto;
    name: texto;
    age: inteiro;
    char* start_date = "";
    [texto] devices_assigned = field(default_factory=list);
    bool has_epi = false;
    bool has_cart = false;
    bool has_exo = false;
    double total_kg_collected = 0.0;
    double total_credit_earned = 0.0;
    {texto: flutuante} materials_collected = field(default_factory=dict);
    int days_active = 0;
    char* badge_level = "INICIANTE";
    int community_recognition = 0;
    char* health_check_date = "";
    int injuries_prevented = 0;
    double ergonomic_score = 0.0;
typedef struct RecyclerEngine {
    // Motor de gestao e gratificacao de catadores.
    void __init__(self) {
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
    {texto: qualquer} assign_devices(self, citizen_id: texto) {
        recycler = self.recyclers.get(citizen_id);
        if (! recycler) {
            return {"error": "Catador ! registrado"};
        assigned = [];
        /* TODO: iterador C manual para dev em self.devices.values() */
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
            "total_devices": sizeof(assigned),;
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
    {texto: qualquer} health_check(self, citizen_id: texto) {
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
    {texto: qualquer} stats(self) {
        return {;
            "total_recyclers": sizeof(self.recyclers),;
            "total_kg_collected": arredonde(self.stats_total_kg, 0),;
            "total_credit_distributed": arredonde(self.stats_total_credit, 0),;
            "avg_kg_per_recycler": arredonde(;
                self.stats_total_kg / maximo(sizeof(self.recyclers), 1), 0),;
            "devices_available": sizeof(self.devices),;
            "cost_to_citizens": "ZERO",;
        };
// ============================================================================
// 3. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = RecyclerEngine();
    printf("=" * 80);
    printf("  OPENRECYCLERS -- TRABALHADORES AMBIENTAIS DA REPUBLICA");
    printf("  Maquinas, ergonomia && reconhecimento para quem LIMPA o mundo");
    printf("=" * 80);
    // === 1. DISPOSITIVOS ===
    printf("\n\n  === 1. DISPOSITIVOS ERGONOMICOS ({len(engine.devices)}) ===\n");
    /* TODO: iterador C manual para d em engine.devices.values() */
        printf("  [{d.device_id}] {d.name}");
        printf("    {d.description[:70]}");
        printf("    Esforco -{d.reduces_effort*100:.0f}%  Velocidade {d.increases_speed:.1f}x  ";
            "FabLab: {d.fabrication_hours:.0f}h");
    // === 2. REGISTRAR CATADORES ===
    printf("\n\n  === 2. TRABALHADORES AMBIENTAIS ===\n");
    recyclers = [;
        ("R-001", "Seu Ze", 52),;
        ("R-002", "Dona Maria", 48),;
        ("R-003", "Carlos", 35),;
        ("R-004", "Ana (iniciante)", 22),;
    ];
    /* para cid, name, age in recyclers: */
        result = engine.register_recycler(cid, name, age);
        printf("  {result['citizen']:<20} -> {result['title']} ({result['badge']})");
    // === 3. EQUIPAMENTOS ===
    printf("\n\n  === 3. EQUIPAMENTO COMPLETO (ZERO custo) ===\n");
    /* para cid, name, age in recyclers: */
        result = engine.assign_devices(cid);
        if (result.get("assigned")) {
            printf("  {result['citizen']}: {result['total_devices']} dispositivos. ";
                "Protecao: {result['protection_level']}");
    // === 4. COLETAS COM CREDITO ===
    printf("\n\n  === 4. COLETAS + CREDITO DE IMPACTO ===\n");
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
    /* para cid, mat, kg in collections: */
        result = engine.record_collection(cid, mat, kg);
        printf("  {result['citizen']:<20} {result['material']:<15} ";
            "{result['weight']:>8} -> +{result['credit_earned']:.1f} ";
            "(badge: {result['badge']})");
    // === 5. SAUDE ===
    printf("\n\n  === 5. EXAME DE SAUDE REGULAR ===\n");
    /* para cid, name, age in recyclers: */
        result = engine.health_check(cid);
        printf("  {result.get('citizen', name):<20} -> {result.get('status', '?')}");
    // === 6. CREDITO POR MATERIAL ===
    printf("\n\n  === 6. TABELA DE CREDITO POR MATERIAL ===\n");
    /* para mat, credit in ordene(engine.credit_per_kg.items(), */
                            key = (x) -> -x[1]):;
        printf("  {mat.value:<20} {credit:.1f}/kg");
    // === 7. STATS ===
    printf("\n\n  === 7. ESTATISTICAS ===\n");
    s = engine.stats();
    /* para cada (k, v) em s.items(): */
        printf("  {k:<30} {v}");
    // === FILOSOFIA ===
    printf("\n\n{'='*80}");
    printf("  FILOSOFIA DO OPENRECYCLERS");
    printf("{'='*80}");
    printf(""";
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
    Catador P1 = trabalhador ambiental. Nao marginalizado.;
    Equipamento protege corpo. Exoesqueleto P2 = autonomia.;
    P3: Credito por impacto real (! migalhas).;
    P4: Reconhecimento publico. Orgulho, ! invisibilidade.;
// )
    printf("{'='*80}");
    printf("  OpenRecyclers: {s['total_recyclers']} trabalhadores, ";
        "{s['total_kg_collected']:,.0f}kg coletados, ";
        "{s['total_credit_distributed']:,.0f} credito distribuido.");
    printf("  Quem LIMPA o mundo NAO && invisivel.");
    printf("{'='*80}");

#endif // OPENRECYCLERS_DISPOSITIVOS_MAQUINAS_E_GRATIFICACAO_PARA_CATADORES_H
