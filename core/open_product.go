// OpenProduct -- Produtos Otimizados para Meio Ambiente, Pessoas e Animais -- gerado de Portugol++
package openproduct_produtos_otimizados_para_meio_ambiente_pessoas_e_animais

import "fmt"

// !/usr/bin/env python3
//
OpenProduct -- Produtos Otimizados para Meio Ambiente, Pessoas && Animais
=========================================================================
"Todo produto da Republica && projetado para:
1. ! prejudicar PESSOAS (toxico, perigoso, explorador)
2. ! prejudicar ANIMAIS (teste, crueldade, extincao)
3. ! prejudicar MEIO AMBIENTE (poluicao, desperdicio, extracao)
4. SER REPARAVEL (OpenRepair, ! descartavel)
5. SER MODULAR (LEGO, troca peca, ! produto inteiro)
6. SER CC0 (bem comum, sem propriedade)
Produto que prejudica? REFORMULADO.
Produto que polui? REPROJETADO.
Produto que testa em animais? PROIBIDO.
Produto que && descartavel? SUBSTITUIDO."
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
// 1. CRITERIOS DE SUSTENTABILIDADE
// ============================================================================
type ImpactArea int
const (
    // Areas que um produto impacta.
    HUMAN_HEALTH = "saude_humana"
    ANIMAL_WELFARE = "bem_estar_animal"
    ENVIRONMENT = "meio_ambiente"
    SOCIAL = "social"
    CIRCULARITY = "circularidade"
    ENERGY = "energia"
type HarmLevel int
const (
    NONE = ("nenhum", 0)  // zero dano
    MINIMAL = ("minimo", 1)  // dano minimo aceitavel
    LOW = ("baixo", 2)  // dano baixo (mitigavel)
    MODERATE = ("moderado", 3)  // dano moderado (precisa melhorar)
    HIGH = ("alto", 4)  // dano alto (inaceitavel)
    CRITICAL = ("critico", 5)  // dano critico (PROIBIDO)
type ProductStatus int
const (
    APPROVED = "aprovado"  // passou em tudo
    NEEDS_IMPROVEMENT = "precisa_melhorar"
    REFORMULATING = "reformulando"  // sendo reprojetado
    PROHIBITED = "proibido"  // dano critico, banido
    REPLACED = "substituido"  // trocado por alternativa
type MaterialType int
const (
    RECYCLED = "reciclado"
    BIODEGRADABLE = "biodegradavel"
    RENEWABLE = "renovavel"
    MINERAL = "mineral"
    SYNTHETIC = "sintetico"
    TOXIC = "toxico"  // PROIBIDO
    ANIMAL_DERIVED = "animal"  // precisa verificacao etica
    FOREST = "floresta"  // precisa certificacao
// ============================================================================
// 2. PRODUTO
// ============================================================================
// decorador: @dataclass
type RepublicProduct struct {
    // Um produto projetado para nao prejudicar nada nem ninguem.
    product_id: texto
    name: texto
    category: texto // vestuario, eletronico, moveis, etc
    description := "" // string
    // Impactos (0 = nenhum dano, 5 = critico)
    human_health_harm := HarmLevel.NONE // HarmLevel
    animal_harm := HarmLevel.NONE // HarmLevel
    environment_harm := HarmLevel.NONE // HarmLevel
    social_harm := HarmLevel.NONE // HarmLevel
    // Materiais
    materials := field(default_factory=list) // [MaterialType]
    materials_detail := "" // string
    // Ciclo de vida
    biodegradable := false // bool
    recyclable := true // bool
    repairable := true // OpenRepair // bool
    modular := true // LEGO // bool
    lifespan_years := 10.0 // float64
    // Energia
    energy_efficient := true // bool
    energy_source := "solar/eolica" // string
    // Producao
    fablab_producible := true // FabLab fabrica? // bool
    tested_on_animals := false // PROIBIDO // bool
    fair_labor := true // trabalho base 1.0 // bool
    // Status
    status := ProductStatus.APPROVED // ProductStatus
    replacement_for := ""  // substitui qual produto nocivo? // string
    alternative_if_prohibited := "" // string
    // decorador: @property
    func overall_score(self) int64 {
        // Score 0-100 (100 = perfeito para tudo).
        harms = [self.human_health_harm, self.animal_harm,
                self.environment_harm, self.social_harm]
        penalty = soma(h.value[1] * 5 para h em harms)
        bonus = 0
        if self.biodegradable {
            bonus = bonus + 5
        if self.recyclable {
            bonus = bonus + 5
        if self.repairable {
            bonus = bonus + 10
        if self.modular {
            bonus = bonus + 10
        if self.energy_efficient {
            bonus = bonus + 5
        if ! self.tested_on_animals {
            bonus = bonus + 10
        if self.fablab_producible {
            bonus = bonus + 5
        return maximo(0, minimo(100, 100 - penalty + bonus))
// ============================================================================
// 3. CATÁLOGO DE PRODUTOS
// ============================================================================
PRODUCTS := [ // [RepublicProduct]
    // === VESTUARIO ===
    RepublicProduct(
        "PRD-SHIRT", "OpenShirt (camiseta)", "vestuario",
        "Camiseta de algodao organico nacional. Costurada por costureira (OpenProfessions).",
        materials = [MaterialType.RENEWABLE, MaterialType.BIODEGRADABLE],
        materials_detail = "Algodao organico nacional. Sem pesticida. Tinta natural.",
        biodegradable = true, recyclable=true, repairable=true,
        lifespan_years = 5.0,
        replacement_for = "Camiseta fast-fashion (Zara/H&M/Shein)",
    ),
    RepublicProduct(
        "PRD-SHOE", "OpenShoe (tenis)", "vestuario",
        "Tenis de materiais reciclados. Sol de borracha reciclada (OpenRecyclers).",
        materials = [MaterialType.RECYCLED, MaterialType.RENEWABLE],
        materials_detail = "Superior: garrafa PET reciclada. Sol: borracha reciclada. Palmilha: fibra de coco.",
        biodegradable = false, recyclable=true, repairable=true, modular=true,
        lifespan_years = 8.0,
        replacement_for = "Tenis Nike/Adidas (exploracao trabalhadora, residuo)",
    ),
    RepublicProduct(
        "PRD-JACKET", "OpenJacket (casaco)", "vestuario",
        "Casaco de lã de ovelha criada solta (NÃO tosquia violenta).",
        materials = [MaterialType.ANIMAL_DERIVED, MaterialType.RENEWABLE],
        materials_detail = "La de ovelha solta (sem crueldade). Forro: algodao organico.",
        animal_harm = HarmLevel.MINIMAL,
        biodegradable = true, repairable=true,
        lifespan_years = 15.0,
        replacement_for = "Casaco sintetico (petroquimico, microplastico)",
    ),
    // === ELETRONICOS ===
    RepublicProduct(
        "PRD-PHONE", "OpenPhone", "eletronico",
        "Smartphone RISC-V modular. Tudo trocavel. OpenRepair eterno.",
        materials = [MaterialType.MINERAL, MaterialType.RECYCLED],
        materials_detail = "Chip RISC-V nacional. Vidro reciclado. Bateria de litio reciclavel.",
        recyclable = true, repairable=true, modular=true,
        lifespan_years = 20.0,
        energy_efficient = true,
        replacement_for = "iPhone (obsoleto 2 anos, irreparavel, toxico)",
    ),
    RepublicProduct(
        "PRD-BATT", "OpenBattery (bateria)", "eletronico",
        "Bateria modular de ion-litio reciclavel. Celulas trocaveis.",
        materials = [MaterialType.MINERAL, MaterialType.RECYCLED],
        materials_detail = "Ion-litio reciclavel. Sem cobalto de mina escrava (RDC).",
        environment_harm = HarmLevel.LOW,
        recyclable = true, repairable=true, modular=true,
        lifespan_years = 15.0,
    ),
    // === MOVEIS ===
    RepublicProduct(
        "PRD-CHAIR", "OpenChair (cadeira)", "moveis",
        "Cadeira de madeira de reflorestamento. Selo de manejo florestal.",
        materials = [MaterialType.FOREST, MaterialType.RENEWABLE],
        materials_detail = "Madeira de eucalipto de reflorestamento (certificado). Sem madeira nativa.",
        biodegradable = true, recyclable=true, repairable=true, modular=true,
        lifespan_years = 30.0,
        replacement_for = "Cadeira plastica/MDF (descartavel, toxico)",
    ),
    RepublicProduct(
        "PRD-TABLE", "OpenTable (mesa)", "moveis",
        "Mesa de bambu (cresce 30x mais rapido que madeira).",
        materials = [MaterialType.RENEWABLE, MaterialType.BIODEGRADABLE],
        materials_detail = "Bambu cultivado (renovavel em 3 anos). Sem desmatamento.",
        biodegradable = true, repairable=true, modular=true,
        lifespan_years = 25.0,
    ),
    // === COZINHA ===
    RepublicProduct(
        "PRD-PAN", "OpenPan (panela)", "cozinha",
        "Panela de ferro fundido. Duravel. Sem teflon (toxico).",
        materials = [MaterialType.MINERAL],
        materials_detail = "Ferro fundido. Sem teflon (PFAS toxico). Antiaderente natural com tempero.",
        human_health_harm = HarmLevel.NONE,
        repairable = true,
        lifespan_years = 50.0,
        replacement_for = "Panela teflon (PFAS/PFOA -- cancerigeno)",
    ),
    RepublicProduct(
        "PRD-CUP", "OpenCup (caneca)", "cozinha",
        "Caneca de ceramica nacional. Reutilizavel. NAO descartavel.",
        materials = [MaterialType.MINERAL],
        materials_detail = "Ceramica de argila nacional. Esmalte sem chumbo.",
        biodegradable = false, recyclable=true,
        lifespan_years = 20.0,
        replacement_for = "Copos descartaveis (12 bilhoes/ano no Brasil)",
    ),
    // === LIMPEZA ===
    RepublicProduct(
        "PRD-SOAP", "OpenSoap (sabao)", "limpeza",
        "Sabao de oleos essenciais. Biodegradavel. Sem fosfato. Sem teste em animais.",
        materials = [MaterialType.BIODEGRADABLE, MaterialType.RENEWABLE],
        materials_detail = "Oleo de coco + oleos essenciais. Sem fosfato. Sem lauril. Biodegradavel.",
        biodegradable = true, tested_on_animals=false,
        lifespan_years = 1.0,
        replacement_for = "Sabao industrial (fosfato + teste em animais + rio poluido)",
    ),
    RepublicProduct(
        "PRD-CLEAN", "OpenClean (multi-uso)", "limpeza",
        "Limpa-tudo de acido citrico + vinagre. Zero toxico.",
        materials = [MaterialType.BIODEGRADABLE],
        materials_detail = "Acido citrico + vinagre + oleos essenciais. Biodegradavel.",
        biodegradable = true,
        replacement_for = "QBoa/Ajax (quimico toxico + teste em animais)",
    ),
    // === HIGIENE ===
    RepublicProduct(
        "PRD-BRUSH", "OpenBrush (escova dental)", "higiene",
        "Escova de bamboo + cerdas de nilon biodegradavel.",
        materials = [MaterialType.RENEWABLE, MaterialType.BIODEGRADABLE],
        materials_detail = "Cabo de bamboo (renovavel). Cerdas de nilon biodegradavel.",
        biodegradable = true,
        lifespan_years = 0.3,
        replacement_for = "Escova plastica (5 bilhoes/ano descartados)",
    ),
    RepublicProduct(
        "PRD-PAD", "OpenPad (absorvente)", "higiene",
        "Absorvente de algodao organico lavavel. Reutilizavel. ZERO lixo.",
        materials = [MaterialType.RENEWABLE, MaterialType.BIODEGRADABLE],
        materials_detail = "Algodao organico. Lavavel. 5 anos de uso. ZERO residuo mensal.",
        biodegradable = true,
        lifespan_years = 5.0,
        replacement_for = "Absorvente descartavel (200kg lixo/mulher/vida)",
    ),
    // === ENERGIA ===
    RepublicProduct(
        "PRD-SOLAR", "OpenSolarPanel", "energia",
        "Painel solar modular. Celulas trocaveis. OpenRepair.",
        materials = [MaterialType.MINERAL, MaterialType.RECYCLED],
        materials_detail = "Silicio nacional. Vidro reciclado. Celulas modulares (troca individual).",
        environment_harm = HarmLevel.MINIMAL,
        recyclable = true, repairable=true, modular=true,
        lifespan_years = 30.0,
        energy_efficient = true,
        replacement_for = "Energia termica (petroleo/carvao)",
    ),
    // === EMBALAGEM ===
    RepublicProduct(
        "PRD-BAG", "OpenBag (sacola)", "embalagem",
        "Sacola de pano reutilizavel. NAO descartavel.",
        materials = [MaterialType.RENEWABLE, MaterialType.BIODEGRADABLE],
        materials_detail = "Algodao organico. Reutilizavel por 10 anos.",
        biodegradable = true, recyclable=true,
        lifespan_years = 10.0,
        replacement_for = "Sacola plastica (1 TRILHAO/ano no planeta)",
    ),
    RepublicProduct(
        "PRD-BOTTLE", "OpenBottle (garrafa)", "embalagem",
        "Garrafa de aco inoxidavel || vidro. Reutilizavel eternamente.",
        materials = [MaterialType.MINERAL],
        materials_detail = "Aco inoxidavel reciclavel || vidro. Sem plastico.",
        recyclable = true, repairable=true,
        lifespan_years = 30.0,
        replacement_for = "Garrafa PET (500 bilhoes/ano planeta)",
    ),
    // === PRODUTOS NOCIVOS (PROIBIDOS) ===
    RepublicProduct(
        "PRD-TEFLON", "Panela Teflon", "cozinha",
        "PROIBIDA. Teflon = PFAS/PFOA. Cancerigeno. Contamina agua.",
        human_health_harm = HarmLevel.CRITICAL,
        environment_harm = HarmLevel.CRITICAL,
        materials = [MaterialType.TOXIC],
        status = ProductStatus.PROHIBITED,
        alternative_if_prohibited = "OpenPan (ferro fundido, sem toxico)",
        lifespan_years = 2.0,
        repairable = false,
    ),
    RepublicProduct(
        "PRD-PLASTIC-CUP", "Copo Plastico Descartavel", "embalagem",
        "PROIBIDO. 12 bilhoes/ano no Brasil. 400 anos para degradar.",
        environment_harm = HarmLevel.CRITICAL,
        materials = [MaterialType.SYNTHETIC],
        status = ProductStatus.PROHIBITED,
        alternative_if_prohibited = "OpenCup (ceramica reutilizavel)",
        lifespan_years = 0.01,
        repairable = false,
    ),
    RepublicProduct(
        "PRD-ANIMAL-TEST", "Produto Testado em Animais", "cosmetico",
        "PROIBIDO. Teste em animais && CRUELDADE desnecessaria.",
        animal_harm = HarmLevel.CRITICAL,
        social_harm = HarmLevel.MODERATE,
        status = ProductStatus.PROHIBITED,
        alternative_if_prohibited = "OpenSoap + OpenClean (sem teste em animais)",
    ),
]
// ============================================================================
// 4. MOTOR DE PRODUTOS
// ============================================================================
type ProductEngine struct {
    // Motor que aprova, reprova e reformula produtos.
    CRITERIOS DE APROVACAO (TODOS devem passar):
    1. ! prejudica saude humana (sem toxico, sem cancerigeno)
    2. ! testa em animais (PROIBIDO)
    3. ! prejudica meio ambiente (biodegradavel/reciclavel)
    4. REPARAVEL (OpenRepair, ! descartavel)
    5. MODULAR (LEGO, troca peca)
    6. FABLAB PRODUCIVEL (producao nacional)
    7. TRABALHO JUSTO (base 1.0, sem exploracao)
    SE FALHA EM UM CRITERIO: reformular || proibir.
    SE DANO CRITICO: PROIBIDO imediatamente.
    //
    func __init__(self) {
        self.products: {texto: RepublicProduct} = {
            p.product_id: p para p em PRODUCTS
        }
    func evaluate(self, product_id: texto) {texto: qualquer} {
        // Avalia produto contra todos os criterios.
        p = self.products.get(product_id)
        if ! p {
            return {"error": "Produto ! encontrado"}
        checks = {
            "saude_humana": p.human_health_harm.value[1] <= 1,
            "sem_teste_animal": !  p.tested_on_animals,
            "bem_estar_animal": p.animal_harm.value[1] <= 1,
            "meio_ambiente": p.environment_harm.value[1] <= 2,
            "reparavel": p.repairable,
            "modular": p.modular,
            "fablab": p.fablab_producible,
            "trabalho_justo": p.fair_labor,
            "sem_toxico": MaterialType.TOXIC !  in p.materials,
        }
        failed = [k para k, v in checks.items() if ! v]
        any_critical = any([
            p.human_health_harm == HarmLevel.CRITICAL,
            p.animal_harm == HarmLevel.CRITICAL,
            p.environment_harm == HarmLevel.CRITICAL,
        ])
        if any_critical {
            p.status = ProductStatus.PROHIBITED
        } else if failed {
            p.status = ProductStatus.NEEDS_IMPROVEMENT
        } else {
            p.status = ProductStatus.APPROVED
        return {
            "product": p.name,
            "score": p.overall_score,
            "checks": checks,
            "failed": failed,
            "critical": any_critical,
            "status": p.status.value,
            "message": (
                "{p.name}: Score {p.overall_score}/100. "
                "Status: {p.status.value}. "
                "{'PROIBIDO.' if any_critical else 'APROVADO.' if not failed else 'PRECISA MELHORAR.'}"
            ),
        }
    func list_approved(self) [Dict] {
        return [
            {"id": p.product_id, "name": p.name,
            "category": p.category,
            "score": p.overall_score,
            "lifespan": p.lifespan_years,
            "biodegradable": p.biodegradable,
            "recyclable": p.recyclable,
            "repairable": p.repairable,
            "modular": p.modular,
            "replaces": p.replacement_for[:30]}
            para p em self.products.values() {
            if p.status == ProductStatus.APPROVED
        ]
    func list_prohibited(self) [Dict] {
        return [
            {"id": p.product_id, "name": p.name,
            "why": "Saude:{p.human_health_harm.value[0]} "
                    "Animal:{p.animal_harm.value[0]} "
                    "Ambiente:{p.environment_harm.value[0]}",
            "alternative": p.alternative_if_prohibited}
            para p em self.products.values() {
            if p.status == ProductStatus.PROHIBITED
        ]
    func waste_report(self) {texto: qualquer} {
        // Relatorio de residuos evitados.
        return {
            "sacola_plastica": {
                "atual": "1 trilhao/ano (planeta)",
                "republica": "ZERO (OpenBag reutilizavel)",
                "economia_anual": "1 trilhao de sacolas",
            },
            "copo_descartavel": {
                "atual": "12 bilhoes/ano (Brasil)",
                "republica": "ZERO (OpenCup ceramica)",
                "economia_anual": "12 bilhoes de copos",
            },
            "garrafa_pet": {
                "atual": "500 bilhoes/ano (planeta)",
                "republica": "ZERO (OpenBottle inox)",
                "economia_anual": "500 bilhoes de garrafas",
            },
            "absorvente": {
                "atual": "200kg lixo/mulher/vida",
                "republica": "ZERO (OpenPad lavavel)",
                "economia_por_mulher": "200kg de lixo",
            },
            "escova_dental": {
                "atual": "5 bilhoes/ano (planeta)",
                "republica": "bamboo biodegradavel (OpenBrush)",
                "economia_anual": "5 bilhoes de plasticos",
            },
            "fast_fashion": {
                "atual": "92 milhoes toneladas/ano lixo (planeta)",
                "republica": "OpenShirt/OpenShoe duravel + reparavel",
                "economia_anual": "milhoes de toneladas",
            },
            "message": (
                "Produto Republicano = ZERO lixo. "
                "Tudo reutilizavel, reparavel, biodegradavel. "
                "Descartavel ! existe. Lixo ! existe."
            ),
        }
    func stats(self) {texto: qualquer} {
        approved = soma(1 para p em self.products.values()
                    if p.status == ProductStatus.APPROVED)
        prohibited = soma(1 para p em self.products.values()
                        if p.status == ProductStatus.PROHIBITED)
        avg_score = soma(p.overall_score para p em self.products.values()
                        if p.status == ProductStatus.APPROVED) / maximo(approved, 1)
        return {
            "total_produtos": len(self.products),
            "aprovados": approved,
            "proibidos": prohibited,
            "score_medio_aprovados": "{avg_score:.0f}/100",
            "criterios": 8,
            "custo": "ZERO",
        }
// ============================================================================
// 5. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = ProductEngine()
    fmt.Println("=" * 80)
    fmt.Println("  OPENPRODUCT -- PRODUTOS QUE NAO PREJUDICAM")
    fmt.Println("  Pessoas. Animais. Meio Ambiente. Tudo protegido.")
    fmt.Println("=" * 80)
    // === 1. AVALIAR TODOS OS PRODUTOS ===
    fmt.Println("\n\n  === 1. AVALIACAO DE PRODUTOS ===\n")
    for _, pid := range engine.products {
        r = engine.evaluate(pid)
    // === 2. PRODUTOS APROVADOS ===
    fmt.Println("\n\n  === 2. PRODUTOS APROVADOS ===\n")
    approved = engine.list_approved()
    fmt.Println("  {'Produto':<25} {'Score':>5} {'Vida':>5} {'Bio':>4} {'Rep':>4} {'Mod':>4} {'Substitui'}")
    fmt.Println("  {'-'*85}")
    for _, p := range approved {
        fmt.Println("  {p['name'][:24]:<25} {p['score']:>5} {p['lifespan']:>4.0f}a "
            "{'S' if p['biodegradable'] else 'N':>4} "
            "{'S' if p['repairable'] else 'N':>4} "
            "{'S' if p['modular'] else 'N':>4} "
            "{p['replaces']}")
    // === 3. PRODUTOS PROIBIDOS ===
    fmt.Println("\n\n  === 3. PRODUTOS PROIBIDOS ===\n")
    prohibited = engine.list_prohibited()
    for _, p := range prohibited {
        fmt.Println("  {p['name']:<30} DANO: {p['why']}")
        fmt.Println("    Alternativa: {p['alternative']}")
    // === 4. RELATORIO DE RESIDUOS ===
    fmt.Println("\n\n  === 4. RESIDUOS EVITADOS ===\n")
    waste = engine.waste_report()
    para cada (key, data) em waste.items(): {
        if key != "message"  &&  isinstance(data, dict) {
            fmt.Println("\n  {key.upper()}:")
            fmt.Println("    Atual: {data['atual']}")
            fmt.Println("    Republica: {data['republica']}")
    fmt.Println("\n  {waste['message']}")
    // === 5. STATS ===
    fmt.Println("\n\n  === 5. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items(): {
        fmt.Println("  {k:<30} {v}")
    fmt.Println("\n{'='*80}")
    fmt.Println("  OpenProduct: {s['aprovados']} aprovados, {s['proibidos']} proibidos. "
        "Score medio: {s['score_medio_aprovados']}.")
    fmt.Println("  Nao prejudica pessoas. Nao prejudica animais. Nao prejudica planeta.")
    fmt.Println("{'='*80}")
