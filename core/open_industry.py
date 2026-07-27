#!/usr/bin/env python3
"""
OpenIndustry -- Copiar, Melhorar e Criar Marcas Nacionais Superiores -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenIndustry -- Copiar, Melhorar and Criar Marcas Nacionais Superiores
=====================================================================
"O Brasil importa tudo. Produz pouco. Depende de fora.
A Republica COPIA tudo. MELHORA tudo. Cria marcas SUPERIORES.
Tudo nacional. Tudo melhor. Tudo CC0."
FILOSOFIA:
HOJE:
- iPhone: Apple (EUA) lucra. Brasil paga.
- Trator: John Deere (EUA). Brasil paga.
- Remédio: Big Pharma (EUA/Europa). Brasil paga.
- Software: Microsoft/Google (EUA). Brasil paga.
- Avião: Boeing (EUA). (Embora já tenhamos a Embraer!)
- Carro: montadoras estrangeiras. Brasil só monta.
REPÚBLICA:
- OpenPhone: smartphone RISC-V, OpenHardware, CC0. Melhor que iPhone.
- OpenTrator: trator OpenHardware. Melhor que John Deere.
- OpenPharma: remédios fabricados no FabLab. Melhor que Big Pharma.
- OpenOS: sistema operacional Rust. Melhor que Windows.
- OpenAero: avião OpenHardware. Melhor que Boeing.
- OpenCar: veículo elétrico aberto. Melhor que Tesla.
POLÍTICA DE CÓPIA and MELHORIA:
1. IDENTIFICAR o melhor produto estrangeiro
2. ENGENHARIA REVERSA (clean room, CC0)
3. MELHORAR: mais eficiente, mais barato, mais aberto
4. PRODUZIR nacionalmente (FabLab nacional)
5. MARCA PRÓPRIA com qualidade SUPERIOR
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
# 1. CATEGORIAS INDUSTRIAIS
# ============================================================================
class IndustryCategory(Enum):
    ELECTRONICS = "eletronicos"  // smartphone, laptop, TV
    AUTOMOTIVE = "automotivo"  // carro, moto, caminhão
    AEROSPACE = "aeroespacial"  // avião, drone, satélite
    MACHINERY = "maquinario"  // trator, retro, industrial
    PHARMACEUTICAL = "farmaceutico"  // remédios, vacinas
    SOFTWARE = "software"  // OS, apps, IA
    TEXTILE = "textil"  // roupas, tecidos
    FOOD = "alimentos"  // processados, bebidas
    CONSTRUCTION = "construcao"  // cimento, aço, vidro
    ENERGY = "energia"  // painel solar, turbina
    MEDICAL_EQUIP = "equip_medico"  // ressonância, laser, prótese
    CHEMICAL = "quimico"  // fertilizante, plástico
    METAL = "metalurgico"  // aço, alumínio, cobre
    AGRICULTURAL = "agricola"  // sementes, defensivos
    TELECOM = "telecom"  // antena, roteador, fibra
class CopyStatus(Enum):
    IDENTIFIED = "identificado"  // produto alvo identificado
    REVERSE_ENGINEERING = "eng_reversa"  // estudando como funciona
    PROTOTYPING = "prototipo"  // primeiro protótipo nacional
    IMPROVING = "melhorando"  // melhorando o original
    PRODUCTION = "producao"  // produzindo em escala
    SUPERIOR = "superior"  // qualidade SUPERIOR ao original
class AdvantageType(Enum):
    # Como a versão nacional é SUPERIOR.
    OPEN_SOURCE = "codigo_aberto"  // CC0 (vs fechado)
    CHEAPER = "mais_barato"  // ZERO (vs R$ caro)
    REPAIRABLE = "reparavel"  // OpenRepair (vs descartável)
    MODULAR = "modular_lego"  // peças trocáveis (vs monolítico)
    EFFICIENT = "mais_eficiente"  // menos energia/materia
    SUSTAINABLE = "sustentavel"  // reciclado, renovável
    ADAPTED = "adaptado"  // feito para o Brasil (vs genérico)
    SECURE = "seguro"  // Rust memory-safe (vs vulnerável)
    UPGRADEABLE = "atualizavel"  // peças melhoram (vs obsoleto)
# ============================================================================
# 2. PRODUTO INDUSTRIAL NACIONAL
# ============================================================================
# decorador: @dataclass
class NationalProduct:
    # Um produto nacional SUPERIOR ao estrangeiro.
    ESTRUTURA:
    - Produto estrangeiro (o que copiamos)
    - Produto nacional (o que criamos)
    - Vantagens (por que o nosso é melhor)
    - Status (até onde chegamos)
    # 
    product_id: texto
    national_brand: texto                   // marca nacional (ex: "OpenPhone")
    foreign_original: texto                 // marca estrangeira (ex: "iPhone")
    foreign_company: texto                  // empresa (ex: "Apple")
    foreign_country: texto                  // país (ex: "EUA")
    category: IndustryCategory
    # Comparação
    foreign_price: str = "R$ caro"  // preço estrangeiro
    national_price: str = "ZERO"  // preço na República
    foreign_quality: int = 8 // 1-10
    national_quality: int = 9 // 1-10
    # Vantagens
    advantages: [AdvantageType] = field(default_factory=list)
    why_better: str = ""
    # Produção
    status: CopyStatus = CopyStatus.IDENTIFIED
    fablab_capable: bool = True // FabLab nacional produz?
    materials_national: float = 0.8 // % de material nacional
    production_capacity: str = ""  // escala
    # Especificações
    specs: {texto: texto} = field(default_factory=dict)
# ============================================================================
# 3. CATÁLOGO DE PRODUTOS (15+ setores)
# ============================================================================
PRODUCTS: [NationalProduct] = [
    # === ELETRÔNICOS ===
    NationalProduct(
        "IND-PH", "OpenPhone", "iPhone", "Apple", "EUA",
        IndustryCategory.ELECTRONICS,
        foreign_price = "R$ 8.000-15.000",
        national_price = "ZERO",
        foreign_quality = 9, national_quality=10,
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.CHEAPER,
                    AdvantageType.REPAIRABLE, AdvantageType.MODULAR,
                    AdvantageType.UPGRADEABLE],
        why_better = (
            "iPhone é fechado. OpenPhone é CC0. "
            "iPhone obsoleto em 2 anos. OpenPhone atualizável (peças modulares). "
            "iPhone não repara. OpenPhone tem OpenRepair. "
            "iPhone Bateria presa. OpenPhone bateria troca. "
            "iPhone chip Apple. OpenPhone chip RISC-V nacional (OpenGPU)."
        ),
        status = CopyStatus.PROTOTYPING,
        specs = {
            "cpu": "RISC-V quad-core nacional (OpenCPU)",
            "gpu": "OpenGPU nacional",
            "ram": "8GB LPDDR5",
            "storage": "128GB (expansível)",
            "screen": "OLED 6.5\" (vidro nacional)",
            "battery": "5000mAh (trocável pelo usuário)",
            "camera": "48MP (sensor nacional)",
            "os": "OpenOS (Rust)",
            "modular": "SIM. Tudo trocável. LEGO.",
        },
    ),
    NationalProduct(
        "IND-LT", "OpenLaptop", "MacBook Pro", "Apple", "EUA",
        IndustryCategory.ELECTRONICS,
        foreign_price = "R$ 15.000-30.000",
        national_price = "ZERO",
        foreign_quality = 9, national_quality=10,
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE,
                    AdvantageType.MODULAR, AdvantageType.UPGRADEABLE],
        why_better = (
            "MacBook é fechado. OpenLaptop é CC0. "
            "MacBook RAM soldada. OpenLaptop RAM trocável. "
            "MacBook não repara. OpenLaptop tem OpenRepair. "
            "MacBook chip Apple. OpenLaptop RISC-V nacional."
        ),
        status = CopyStatus.PROTOTYPING,
        specs = {
            "cpu": "RISC-V 8-core nacional",
            "ram": "16-64GB (trocável)",
            "storage": "512GB-4TB (trocável)",
            "screen": "14\" IPS (vidro nacional)",
            "battery": "trocável pelo usuário",
            "os": "OpenOS (Rust)",
            "modular": "SIM. CPU, RAM, storage, bateria, tela -- tudo trocável.",
        },
    ),
    NationalProduct(
        "IND-TV", "OpenTV", "Samsung QLED", "Samsung", "Coreia",
        IndustryCategory.ELECTRONICS,
        foreign_price = "R$ 3.000-10.000",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.CHEAPER],
        why_better = (
            "Samsung espiando você. OpenTV é livre. "
            "Samsung te rastreia. OpenTV respeita. "
            "Samsung fecha em 5 anos. OpenTV: OpenRepair eterno."
        ),
        status = CopyStatus.REVERSE_ENGINEERING,
    ),
    # === AUTOMOTIVO ===
    NationalProduct(
        "IND-CAR", "OpenCar", "Tesla Model 3", "Tesla", "EUA",
        IndustryCategory.AUTOMOTIVE,
        foreign_price = "R$ 250.000+",
        national_price = "ZERO",
        foreign_quality = 9, national_quality=10,
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE,
                    AdvantageType.MODULAR, AdvantageType.SUSTAINABLE],
        why_better = (
            "Tesla é fechado. OpenCar é CC0. "
            "Tesla precisa concessionária. OpenCar: OpenRepair. "
            "Tesla bateria presa. OpenCar bateria modular (troca). "
            "Tesla software fechado. OpenCar: OpenOS automotivo. "
            "Tesla peças caras. OpenCar: FabLab fabrica."
        ),
        status = CopyStatus.IDENTIFIED,
        specs = {
            "type": "elétrico 100%",
            "battery": "modular (células trocáveis)",
            "motor": "OpenHardware elétrico",
            "range": "400km",
            "charging": "OpenEnergy (solar/eólica)",
            "software": "OpenOS Automotive (Rust)",
            "autonomous": "OpenDrive AI (pesquisa)",
            "modular": "SIM. Bateria, motor, painéis -- tudo trocável.",
        },
    ),
    NationalProduct(
        "IND-MOTO", "OpenMoto", "Honda CG", "Honda", "Japão",
        IndustryCategory.AUTOMOTIVE,
        foreign_price = "R$ 15.000-25.000",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.SUSTAINABLE,
                    AdvantageType.EFFICIENT],
        why_better = "Honda a combustão. OpenMoto elétrica. Silenciosa. Limpa.",
        status = CopyStatus.IDENTIFIED,
    ),
    # === AEROESPACIAL ===
    NationalProduct(
        "IND-AIR", "OpenAero", "Boeing 737", "Boeing", "EUA",
        IndustryCategory.AEROSPACE,
        foreign_price = "R$ 500 milhões",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE,
                    AdvantageType.EFFICIENT],
        why_better = (
            "Boeing fechado (MCAS matou). OpenAero: CC0, auditável. "
            "Boeing precisa peça importada. OpenAero: FabLab nacional. "
            "Boeing obsoleto. OpenAero: atualizável. "
            "Embraer já prova que o BRASIL faz avião. "
            "OpenAero leva Embraer ao próximo nível: aberto."
        ),
        status = CopyStatus.IDENTIFIED,
    ),
    # === MAQUINÁRIO AGRÍCOLA ===
    NationalProduct(
        "IND-TR", "OpenTrator", "John Deere", "John Deere", "EUA",
        IndustryCategory.MACHINERY,
        foreign_price = "R$ 300.000-800.000",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE,
                    AdvantageType.MODULAR, AdvantageType.ADAPTED],
        why_better = (
            "John Deere PROÍBE conserto (DRM). OpenTrator: OpenRepair. "
            "John Deere software fechado. OpenTrator: OpenOS Agricultural. "
            "John Deere peças caras importadas. OpenTrator: FabLab fabrica. "
            "John Deere feito para fazenda americana. OpenTrator: feito para Brasil. "
            "Adaptado: Cerrado, Amazônia, Pantanal, sertão."
        ),
        status = CopyStatus.REVERSE_ENGINEERING,
    ),
    # === FARMACÊUTICO ===
    NationalProduct(
        "IND-RX", "OpenPharma", "Big Pharma (várias)", "Pfizer/Novartis/etc", "EUA/Europa",
        IndustryCategory.PHARMACEUTICAL,
        foreign_price = "R$ 100-2.000/caixa",
        national_price = "ZERO",
        foreign_quality = 8, national_quality=9,
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.CHEAPER,
                    AdvantageType.ADAPTED],
        why_better = (
            "Big Pharma lucra com doença. OpenPharma cura. "
            "Big Pharma patente (monopólio). OpenPharma: CC0. "
            "Big Pharma remédio caro. OpenPharma: ZERO custo. "
            "Big Pharma esconde dados. OpenPharma: transparência total. "
            "Big Pharma lobby. OpenPharma: OpenMentalHygiene bloqueia. "
            "Síntese química aberta. FabLab farmacêutico nacional."
        ),
        status = CopyStatus.PRODUCTION,
        specs = {
            "sintese": "aberta (CC0). Sem patente.",
            "producao": "FabLab farmacêutico nacional",
            "qualidade": "Superior (padrão Sirio-Libanes)",
            "exemplos": "Insulina, antirretroviral, quimio, antibiótico",
            "custo": "ZERO (vs R$ 100-2.000)",
        },
    ),
    # === SOFTWARE ===
    NationalProduct(
        "IND-OS", "OpenOS", "Windows/macOS", "Microsoft/Apple", "EUA",
        IndustryCategory.SOFTWARE,
        foreign_price = "R$ 1.000-3.000 (licença)",
        national_price = "ZERO",
        foreign_quality = 7, national_quality=10,
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.CHEAPER,
                    AdvantageType.EFFICIENT, AdvantageType.SECURE],
        why_better = (
            "Windows rastreia (telemetria). OpenOS respeita. "
            "Windows vulnerável. OpenOS: Rust (memory-safe). "
            "Windows lento. OpenOS: leve (128MB RAM). "
            "Windows fecha em 5 anos. OpenOS: OpenRepair eterno. "
            "Windows monolítico. OpenOS: modular (OpenLegoCode). "
            "Windows precisa licença. OpenOS: CC0."
        ),
        status = CopyStatus.PROTOTYPING,
        specs = {
            "kernel": "Rust (memory-safe)",
            "modular": "OpenLegoCode (LEGO blocks)",
            "min_ram": "128MB (OpenLite)",
            "ui": "OpenLite (render adaptativo)",
            "apps": "OpenMarketplace",
            "security": "Rust + CC0 auditável",
        },
    ),
    # === ENERGIA ===
    NationalProduct(
        "IND-SOL", "OpenSolar", "Chinese panels", "Jinko/Trina", "China",
        IndustryCategory.ENERGY,
        foreign_price = "R$ 15.000-50.000 (instalação)",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE,
                    AdvantageType.SUSTAINABLE],
        why_better = (
            "Painel chines descendente (eficiência cai). "
            "OpenSolar: células nacionais + OpenRepair (troca célula). "
            "Painel preso. OpenSolar: modular (troca célula danificada)."
        ),
        status = CopyStatus.PROTOTYPING,
    ),
    NationalProduct(
        "IND-WND", "OpenTurbine", "Vestas/GE", "Vestas/GE", "Dinamarca/EUA",
        IndustryCategory.ENERGY,
        foreign_price = "R$ 5-20 milhões",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE],
        why_better = "Turbina nacional. FabLab fabrica peças. OpenRepair eterno.",
        status = CopyStatus.IDENTIFIED,
    ),
    # === EQUIPAMENTO MÉDICO ===
    NationalProduct(
        "IND-MR", "OpenMRI", "Siemens/GE", "Siemens/GE", "Alemanha/EUA",
        IndustryCategory.MEDICAL_EQUIP,
        foreign_price = "R$ 3-10 milhões",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE,
                    AdvantageType.CHEAPER],
        why_better = (
            "Ressonância Siemens: R$ 3 milhões + manutenção R$ 500k/ano. "
            "OpenMRI: FabLab fabrica. OpenRepair mantém. Custo ZERO. "
            "Todo hospital (mesmo remoto) tem ressonância."
        ),
        status = CopyStatus.IDENTIFIED,
    ),
    NationalProduct(
        "IND-LSR", "OpenLaser", "varios", "varios", "EUA/Europa",
        IndustryCategory.MEDICAL_EQUIP,
        foreign_price = "R$ 500.000-2.000.000",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE],
        why_better = "LASIK, cirurgia, dental. FabLab fabrica. OpenRepair mantém.",
        status = CopyStatus.REVERSE_ENGINEERING,
    ),
    # === TÊXTIL ===
    NationalProduct(
        "IND-TX", "OpenTextile", "Zara/H&M/Shein", "Zara/H&M", "Espanha/Suecia",
        IndustryCategory.TEXTILE,
        foreign_price = "R$ 50-500/peça",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.SUSTAINABLE,
                    AdvantageType.ADAPTED],
        why_better = (
            "Zara/H&M: fast fashion (descartável, explorador). "
            "OpenTextile: algodão nacional, costureira reconhecida (OpenProfessions). "
            "Peça sob medida. Durável. Reparável. CC0."
        ),
        status = CopyStatus.PRODUCTION,
    ),
    # === CONSTRUÇÃO ===
    NationalProduct(
        "IND-STL", "OpenSteel", "Vale/ArcelorMittal", "Vale/Arcelor", "Brasil/Multinacional",
        IndustryCategory.CONSTRUCTION,
        foreign_price = "R$ caro (mercado)",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.SUSTAINABLE],
        why_better = (
            "Aço reciclado (OpenRecyclers). FabLab siderúrgico. "
            "Qualidade controlada. Distribuição nacional."
        ),
        status = CopyStatus.IDENTIFIED,
    ),
    # === TELECOM ===
    NationalProduct(
        "IND-ANT", "OpenAntenna", "Ericsson/Huawei", "Ericsson/Huawei", "Suecia/China",
        IndustryCategory.TELECOM,
        foreign_price = "R$ 50.000-500.000/unid",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE],
        why_better = (
            "Antena 5G/6G nacional. OpenHardware. FabLab fabrica. "
            "OpenNetwork não depende de estrangeiro para telecom."
        ),
        status = CopyStatus.IDENTIFIED,
    ),
    NationalProduct(
        "IND-RTR", "OpenRouter", "Cisco/TP-Link", "Cisco/TP-Link", "EUA/China",
        IndustryCategory.TELECOM,
        foreign_price = "R$ 200-5.000",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.REPAIRABLE,
                    AdvantageType.SECURE],
        why_better = "Roteador nacional. OpenHardware. Sem backdoor. Rust firmware.",
        status = CopyStatus.PROTOTYPING,
    ),
    # === QUÍMICO ===
    NationalProduct(
        "IND-FRT", "OpenFertilizer", "Yara/Bunge", "Yara/Bunge", "Noruega/EUA",
        IndustryCategory.CHEMICAL,
        foreign_price = "R$ caro (sacas)",
        national_price = "ZERO",
        advantages = [AdvantageType.OPEN_SOURCE, AdvantageType.SUSTAINABLE,
                    AdvantageType.ADAPTED],
        why_better = (
            "Fertilizante químico importado (caro + dependência). "
            "OpenFertilizer: compostagem + biofertilizante nacional. "
            "Adaptado para solo brasileiro (Cerrado, Amazônia)."
        ),
        status = CopyStatus.PRODUCTION,
    ),
]
# ============================================================================
# 4. MOTOR INDUSTRIAL
# ============================================================================
class IndustryEngine:
    # Motor de industrialização nacional da República.
    POLÍTICA DE CÓPIA and MELHORIA:
    1. IDENTIFICAR: qual produto estrangeiro domina o mercado brasileiro?
    2. ENGENHARIA REVERSA: como funciona? (clean room, CC0)
    3. PROTOTIPAR: primeira versão nacional (FabLab)
    4. MELHORAR: onde o original falha? Corrigir.
    5. PRODUZIR: escala nacional (OpenLaborRelay)
    6. SUPERAR: qualidade SUPERIOR ao original
    O QUE TORNA O NACIONAL SUPERIOR:
    1. CC0 (aberto vs fechado)
    2. ZERO custo (vs caro)
    3. OpenRepair (vs descartável)
    4. Modular LEGO (vs monolítico)
    5. Sustentável (vs poluente)
    6. Adaptado ao Brasil (vs genérico)
    7. Atualizável (vs obsoleto)
    8. Memory-safe Rust (vs vulnerável)
    POR QUE COPIAR and MELHORAR NÃO É FALTA DE CRIATIVIDADE:
    - China copiou por 30 anos. Hoje lidera em muita coisa.
    - Japão copiou nos anos 50. Hoje supera em qualidade.
    - Coreia copiou nos anos 80. Hoje tem Samsung/LG.
    - Brasil SEMPRE podia ter feito. Não fez por dependência.
    - A República FAZ. Copia. Melhora. Supera.
    # 
    def __init__(self):
        self.products: {texto: NationalProduct} = {p.product_id: p para p em PRODUCTS}
    def list_by_category(self, category: IndustryCategory = None) -> [Dict]:
        prods = self.products.values()
        if category:
            prods = [p para p em prods if p.category == category]
        return [
            {
                "id": p.product_id,
                "nacional": p.national_brand,
                "estrangeiro": "{p.foreign_original} ({p.foreign_company})",
                "preco_ext": p.foreign_price,
                "preco_nac": p.national_price,
                "qualidade_ext": p.foreign_quality,
                "qualidade_nac": p.national_quality,
                "status": p.status.value,
                "vantagens": len(p.advantages),
            }
            para p in prods
        ]
    def compare(self, product_id: texto) -> {texto: qualquer}:
        # Comparação detalhada: nacional vs estrangeiro.
        p = self.products.get(product_id)
        if not p:
            return {"error": "Produto não encontrado"}
        return {
            "nacional": p.national_brand,
            "estrangeiro": p.foreign_original,
            "empresa_estrangeira": p.foreign_company,
            "pais": p.foreign_country,
            "preco_estrangeiro": p.foreign_price,
            "preco_nacional": p.national_price,
            "qualidade_estrangeiro": "{p.foreign_quality}/10",
            "qualidade_nacional": "{p.national_quality}/10",
            "vantagens_nacional": [a.value para a em p.advantages],
            "por_que_melhor": p.why_better,
            "status": p.status.value,
            p.specs ? "specs": p.specs : {},
        }
    def advance_status(self, product_id: texto) -> {texto: qualquer}:
        # Avança produto para próxima fase.
        p = self.products.get(product_id)
        if not p:
            return {"error": "não encontrado"}
        order = list(CopyStatus)
        idx = order.index(p.status)
        if idx + 1 < len(order):
            p.status = order[idx + 1]
        return {
            "product": p.national_brand,
            "new_status": p.status.value,
            "message": "{p.national_brand} avançou para: {p.status.value}.",
        }
    def dependency_report(self) -> {texto: qualquer}:
        # Relatório de dependência externa (o que ainda importamos).
        by_country = Counter()
        by_category = Counter()
        for p in self.products.values():
            by_country[p.foreign_country] += 1
            by_category[p.category.value] += 1
        total = len(self.products)
        superior = sum(1 para p em self.products.values()
                    if p.status == CopyStatus.SUPERIOR)
        in_production = sum(1 para p em self.products.values()
                            if p.status in (CopyStatus.PRODUCTION, CopyStatus.SUPERIOR))
        return {
            "total_produtos": total,
            "ja_superiores": superior,
            "em_producao": in_production,
            "dependencia_por_pais": dict(by_country.most_common()),
            "dependencia_por_setor": dict(by_category.most_common()),
            "message": (
                "Brasil importa de {len(by_country)} países em "
                "{len(by_category)} setores. "
                "A República já superou {superior} and produz {in_production}. "
                "Meta: SUPERAR TODOS."
            ),
        }
    def stats(self) -> {texto: qualquer}:
        return {
            "total_produtos": len(self.products),
            "categorias_cobertas": len(set(p.category para p em self.products.values())),
            "status_distribution": dict(
                Counter(p.status.value para p em self.products.values())),
            "marcas_nacionais_criadas": len(self.products),
            "custo_ao_cidadao": "ZERO (todos)",
            "politica": "COPIAR, MELHORAR, SUPERAR",
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = IndustryEngine()
    print("=" * 80)
    print("  OPENINDUSTRY -- COPIAR, MELHORAR, SUPERAR")
    print("  Brasil copia tudo. Cria marcas nacionais. Qualidade SUPERIOR.")
    print("=" * 80)
    # === 1. PRODUTOS NACIONAIS ===
    print("\n\n  === 1. PRODUTOS NACIONAIS ({len(engine.products)}) ===\n")
    print("  {'Nacional':<15} {'Estrangeiro':<25} {'Preço Ext':<18} {'Preço Nac':<10} {'Status'}")
    print("  {'-'*85}")
    for p in engine.list_by_category():
        print("  {p['nacional']:<15} {p['estrangeiro'][:24]:<25} "
            "{p['preco_ext'][:17]:<18} {p['preco_nac']:<10} {p['status']}")
    # === 2. COMPARAÇÃO DETALHADA: OpenPhone vs iPhone ===
    print("\n\n  === 2. COMPARAÇÃO: OpenPhone vs iPhone ===\n")
    comp = engine.compare("IND-PH")
    print("  NACIONAL: {comp['nacional']} (qualidade {comp['qualidade_nacional']})")
    print("  ESTRANGEIRO: {comp['estrangeiro']} ({comp['empresa_estrangeira']}, {comp['pais']})")
    print("  (qualidade {comp['qualidade_estrangeiro']})")
    print("\n  PREÇO:")
    print("    iPhone: {comp['preco_estrangeiro']}")
    print("    OpenPhone: {comp['preco_nacional']}")
    print("\n  POR QUE O NACIONAL É SUPERIOR:")
    print("    {comp['por_que_melhor']}")
    print("\n  VANTAGENS: {', '.join(comp['vantagens_nacional'])}")
    print("\n  ESPECIFICAÇÕES:")
    for each (k, v) in comp["specs"].items():
        print("    {k}: {v}")
    # === 3. COMPARAÇÃO: OpenPharma vs Big Pharma ===
    print("\n\n  === 3. COMPARAÇÃO: OpenPharma vs Big Pharma ===\n")
    comp2 = engine.compare("IND-RX")
    print("  NACIONAL: {comp2['nacional']}")
    print("  ESTRANGEIRO: {comp2['estrangeiro']} ({comp2['pais']})")
    print("  PREÇO: {comp2['preco_estrangeiro']} vs {comp2['preco_nacional']}")
    print("  POR QUE MELHOR: {comp2['por_que_melhor']}")
    # === 4. COMPARAÇÃO: OpenTrator vs John Deere ===
    print("\n\n  === 4. COMPARAÇÃO: OpenTrator vs John Deere ===\n")
    comp3 = engine.compare("IND-TR")
    print("  NACIONAL: {comp3['nacional']}")
    print("  ESTRANGEIRO: {comp3['estrangeiro']} ({comp3['pais']})")
    print("  POR QUE MELHOR: {comp3['por_que_melhor']}")
    # === 5. POR QUE COPIAR NÃO É FALTA DE CRIATIVIDADE ===
    print("\n\n  === 5. POR QUE COPIAR E MELHORAR É ESTRATÉGIA VENCEDORA ===\n")
    print("""
HISTÓRIA PROVA QUE COPIAR -> MELHORAR -> SUPERAR FUNCIONA:
CHINA (1990-2025):
    Copiou tudo por 30 anos. Hoje lidera em 5G, EV, solar, IA.
    Huawei superou Ericsson. BYD superou Tesla. DJI superou todos.
JAPÃO (1950-1980):
    Copiou produtos americanos. Hoje Toyota > GM. Sony > todas.
COREIA (1980-2020):
    Copiou eletrônicos. Hoje Samsung > em telas and chips.
BRASIL (SEMPRE PÔDE):
    Nunca fez por dependência econômica and política.
    A República FAZ. Copia. Melhora. Supera.
    Vantagem: não precisa lucrar (CC0). Só precisa ser MELHOR.
A DIFERENÇA DA REPÚBLICA:
    Outros países copiaram para LUCRAR.
    A República copia para LIBERTAR.
    Todo produto é CC0. Aberto. Reparável. Modular.
    Não há "marca premium" vs "marca genérica".
    Só existe o MELHOR produto, disponível para TODOS.
# )
    # === 6. RELATÓRIO DE DEPENDÊNCIA ===
    print("\n\n  === 6. RELATÓRIO DE DEPENDÊNCIA EXTERNA ===\n")
    dep = engine.dependency_report()
    print("  Total de produtos: {dep['total_produtos']}")
    print("  Já superiores: {dep['ja_superiores']}")
    print("  Em produção: {dep['em_producao']}")
    print("\n  Dependência por país:")
    for each (country, count) in dep["dependencia_por_pais"].items():
        print("    {country:<15} {count} produtos")
    print("\n  Dependência por setor:")
    for each (cat, count) in dep["dependencia_por_setor"].items():
        print("    {cat:<20} {count} produtos")
    # === 7. STATUS ===
    print("\n\n  === 7. DISTRIBUIÇÃO DE STATUS ===\n")
    s = engine.stats()
    for each (status, count) in s["status_distribution"].items():
        bar = "#" * count
        print("  {status:<25} {count:>2} {bar}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA DO OPENINDUSTRY")
    print("{'='*80}")
    print("""
POLÍTICA: COPIAR, MELHORAR, SUPERAR.
    O Brasil importa tudo. Produz pouco. Depende de fora.
    A República inverte: copia tudo, melhora tudo, supera tudo.
O QUE TORNA O NACIONAL SUPERIOR (sempre):
    1. CC0: código aberto (vs fechado/proprietário)
    2. ZERO: custo zero (vs R$ caro)
    3. OpenRepair: reparável eterno (vs descartável)
    4. Modular LEGO: peças trocáveis (vs monolítico)
    5. Sustentável: reciclado/renovável (vs poluente)
    6. Adaptado: feito para Brasil (vs genérico)
    7. Atualizável: melhora com tempo (vs obsoleto)
    8. Memory-safe Rust: seguro (vs vulnerável)
15 SETORES COBERTOS:
    Eletrônicos (OpenPhone, OpenLaptop, OpenTV)
    Automotivo (OpenCar elétrico, OpenMoto)
    Aeroespacial (OpenAero -- Embraer elevada)
    Maquinário (OpenTrator -- John Deere superada)
    Farmacêutico (OpenPharma -- Big Pharma superada)
    Software (OpenOS Rust -- Windows superado)
    Energia (OpenSolar, OpenTurbine)
    Médico (OpenMRI, OpenLaser)
    Têxtil (OpenTextile)
    Construção (OpenSteel)
    Telecom (OpenAntenna, OpenRouter)
    Químico (OpenFertilizer)
NÃO É FALTA DE CRIATIVIDADE:
    China copiou 30 anos. Hoje lidera.
    Japão copiou. Hoje supera.
    Coreia copiou. Hoje tem Samsung.
    Brasil sempre pôde. A República FAZ.
A DIFERENÇA:
    Outros países copiaram para LUCRAR.
    A República copia para LIBERTAR.
    Tudo CC0. Tudo aberto. Tudo para TODOS.
    Não há marca premium vs genérica.
    Só o MELHOR. Para TODOS.
PRINCÍPIOS:
    P1: Produtos para todos. Sem elite de marca. ZERO custo.
    P2: Produto é bem comum. Ninguém é dono da marca.
    P3: Fabricar nacional = trabalho de alto impacto.
    P4: Quais produtos priorizar? Assembleia vota.
# )
    print("{'='*80}")
    print("  OpenIndustry: {s['total_produtos']} produtos em {s['categorias_cobertas']} setores. "
        "Custo: {s['custo_ao_cidadao']}.")
    print("  Copiar. Melhorar. Superar. Tudo nacional. Tudo CC0.")
    print("{'='*80}")
