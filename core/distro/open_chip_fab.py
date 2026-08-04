#!/usr/bin/env python3
"""
OpenChipFab -- L0: Fab de Chip Nacional
==========================================
Spec de soberania de silicio para o Brasil.

O PROBLEMA:
  Brasil importa 100% dos chips que consome.
  Tudo que tem silicio vem de Taiwan (TSMC), China (SMIC), EUA (Intel).
  Se Taiwan cai, o Brasil para.

A REALIDADE:
  Brazil NAO vai fazer 3nm. Nao agora.
  Mas PODE fazer chips BASICOS: 180nm, 130nm, 65nm.
  Isso basta pra: microcontrolador, sensor, radio, IoT, cartao inteligente.

O PLANO:
  - Fase 1: 180nm (tecnologia de 1999, sem embargo)
  - Fase 2: 65nm (tecnologia de 2006, sem embargo)
  - Fase 3: RISC-V custom em processo nacional

ONDE:
  - Campinas/SP (CTI, CIATEC)
  - Porto Alegre/RS (Ceitec -- ja existe, 600nm)

CEITEC JA EXISTE:
  O Ceitec (Porto Alegre) ja fabrica chip 600nm desde 2008.
  Faz chip de Mifare (cartao busao), e-passport, RFID.
  E estatal. E capacidade REAL. So precisa de investimento.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ENUMS
# ============================================================================

class NodoProcesso(Enum):
    """Nodos de processo de fabricacao de chip."""
    N_600 = ("600nm", "600nm: poder de 1999. RFID, smart card, sensor simples")
    N_350 = ("350nm", "350nm: poder de 1995. Microcontrolador 8-bit, MCU IoT")
    N_180 = ("180nm", "180nm: poder de 1999. MCU 32-bit, radio, display driver")
    N_130 = ("130nm", "130nm: poder de 2001. MCU, SRAM, FPGA simples")
    N_65 = ("65nm", "65nm: poder de 2006. SoC basico, RISC-V dual-core")
    N_28 = ("28nm", "28nm: poder de 2010. SoC completo (RF, GPU basica)")
    N_14 = ("14nm", "14nm: poder de 2014. CPU competitiva (SOB EMBARGO)")
    N_3 = ("3nm", "3nm: poder de 2022. State-of-the-art (SOB EMBARGO)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def sob_embargo(self) -> bool:
        return self.value[0] in ("14nm", "3nm")


class TipoChip(Enum):
    """Tipos de chip fabricaveis."""
    RFID = ("rfid", "RFID/NFC: tag, cartao, passaporte")
    MCU_8BIT = ("mcu8", "Microcontrolador 8-bit (8051, AVR)")
    MCU_32BIT = ("mcu32", "Microcontrolador 32-bit (ARM Cortex-M, RISC-V)")
    SOC_BASICO = ("soc", "SoC basico (CPU+RAM+IO no mesmo die)")
    FPGA = ("fpga", "FPGA simples (reconfiguravel)")
    SENSOR = ("sensor", "Sensor integrado (temperatura, pressao, imagem)")
    RADIO = ("radio", "Radio integrado (LoRa, BLE, Zigbee)")
    DRIVER = ("driver", "Driver de display/touch/LED")
    MEMORIA = ("memoria", "Memoria (SRAM, Flash, EEPROM)")
    ENERGIA = ("energia", "PMIC (gestao de energia)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class EquipamentoFab(Enum):
    """Equipamentos necessarios para fabricacao de chip."""
    FORNO_OXIDACAO = ("forno", "Forno de oxidacao (SiO2)")
    PHOTOLITH = ("photolith", "Stepper/Scanner de fotolitografia")
    ETCH_DRY = ("etch", "Gravacao seca (plasma RIE)")
    ETCH_WET = ("etch_wet", "Gravacao umida (quimica)")
    CVD = ("cvd", "Deposicao quimica em fase vapor (CVD)")
    PVD = ("pvd", "Deposicao fisica em fase vapor (sputtering)")
    CMP = ("cmp", "Planarizacao quimico-mecanica")
    IMPLANT = ("implant", "Implantador de ions")
    INSPECAO = ("inspecao", "Sistema de inspecao optica")
    TESTER = ("tester", "Testador de wafer (probe card)")
    DICING = ("dicing", "Cortador de wafer (serra)")
    BONDING = ("bonding", "Wire bonding / flip chip")
    PACKAGING = ("packaging", "Encapsulamento (injeao plstica/cermica)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class FaseFab(Enum):
    """Fases do plano de soberania de silicio."""
    FASE_1_180NM = ("fase1", "Fase 1: 180nm nacional (sem embargo)")
    FASE_2_65NM = ("fase2", "Fase 2: 65nm nacional (sem embargo)")
    FASE_3_RISCV = ("fase3", "Fase 3: RISC-V custom em processo nacional")
    FASE_4_28NM = ("fase4", "Fase 4: 28nm (depende de parceria)")
    FASE_5_INOVACAO = ("fase5", "Fase 5: P&D em novos materiais (GaN, SiC)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass(frozen=True)
class ChipSpec:
    """Spec de um chip fabricavel nacionalmente."""
    id: str
    nome: str
    tipo: TipoChip
    nodo: NodoProcesso
    transistores: float      # milhoes
    area_mm2: float         # area do die
    clocks_mhz: int
    ram_kb: int
    flash_kb: int
    gpio: int
    interfaces: List[str]
    consumo_ma: float       # consumo em mA
    custo_estimado_brl: float  # custo por unidade
    aplicações: List[str]


@dataclass(frozen=True)
class FasePlano:
    """Uma fase do plano de soberania."""
    fase: FaseFab
    nodo: NodoProcesso
    prazo_anos: int
    investimento_brl_bi: float  # bilhoes
    equipamentos: List[str]
    chips_fabricaveis: List[str]
    dependencia_externa: str
    resultado: str


# ============================================================================
# 3. CATALOGO DE CHIPS NACIONAIS
# ============================================================================

def _init_chips() -> List[ChipSpec]:
    return [
        ChipSpec(
            "rchip_m8", "Republica M8 (RFID/NFC)",
            TipoChip.RFID, NodoProcesso.N_600,
            0.008, 1.5, 13, 0, 8, 0,
            [], 0.1,
            0.15,
            ["cartao busao", "passaporte", "identidade", "pagamento"],
        ),
        ChipSpec(
            "rchip_a8", "Republica A8 (MCU 8-bit)",
            TipoChip.MCU_8BIT, NodoProcesso.N_350,
            0.012, 4.0, 16, 1, 8, 12,
            ["I2C", "SPI", "UART"], 2.0,
            0.40,
            ["IoT simples", "eletrodomestico", "automacao", "educacao"],
        ),
        ChipSpec(
            "rchip_r32", "Republica R32 (RISC-V 32-bit)",
            TipoChip.MCU_32BIT, NodoProcesso.N_180,
            0.050, 8.0, 80, 32, 128, 40,
            ["I2C", "SPI", "UART", "CAN", "USB", "ADC", "PWM"], 15.0,
            1.20,
            ["automotivo", "industrial", "drones", "modular phone"],
        ),
        ChipSpec(
            "rchip_r64", "Republica R64 (RISC-V 64-bit dual-core)",
            TipoChip.SOC_BASICO, NodoProcesso.N_65,
            5.0, 25.0, 500, 256, 0, 64,
            ["I2C", "SPI", "UART", "USB3", "PCIe", "HDMI", "Gige"],
            200.0,
            8.50,
            ["mini PC", "telefone modular V2", "servidor edge"],
        ),
        ChipSpec(
            "rchip_lora", "Republica LoRa (radio integrado)",
            TipoChip.RADIO, NodoProcesso.N_180,
            0.020, 3.0, 32, 4, 32, 8,
            ["SPI", "LoRa SX1262", "BLE 5.0"], 5.0,
            0.80,
            ["mesh comunitario", "agricultura", "sensor remoto"],
        ),
        ChipSpec(
            "rchip_cam", "Republica Cam (sensor de imagem)",
            TipoChip.SENSOR, NodoProcesso.N_180,
            0.200, 16.0, 48, 0, 0, 0,
            ["MIPI CSI-2", "I2C"], 60.0,
            2.50,
            ["camera modular phone", "inspecao", "maquina de visao"],
        ),
        ChipSpec(
            "rchip_pmic", "Republica PMIC (gestao de energia)",
            TipoChip.ENERGIA, NodoProcesso.N_350,
            0.015, 5.0, 0, 0, 0, 0,
            ["I2C", "USB-C PD", "buck", "boost", "LDO"], 0.5,
            0.60,
            ["carregamento", "energia solar", "bateria", "modular phone"],
        ),
    ]


def _init_fases() -> List[FasePlano]:
    return [
        FasePlano(
            FaseFab.FASE_1_180NM, NodoProcesso.N_180,
            3, 2.5,
            ["forno", "photolith 180nm", "etch_dry", "cvd", "cmp",
             "implant", "tester", "dicing", "bonding", "packaging"],
            ["rchip_a8", "rchip_r32", "rchip_lora", "rchip_cam", "rchip_pmic"],
            "Stepper 180nm (ASML/Nikon, sem embargo). Materiais importados.",
            "Microcontrolador RISC-V nacional. IoT, automotivo, modular phone.",
        ),
        FasePlano(
            FaseFab.FASE_2_65NM, NodoProcesso.N_65,
            5, 5.0,
            ["photolith 65nm", "etch_dry avancado", "cvd avancado", "cmp avancado",
             "implant avancado", "inspecao avancada", "tester avancado"],
            ["rchip_r64"],
            "Stepper 65nm (disponivel, sem embargo). Silicio de alta pureza.",
            "SoC RISC-V nacional. Mini PC, telefone modular V2, servidor edge.",
        ),
        FasePlano(
            FaseFab.FASE_3_RISCV, NodoProcesso.N_65,
            7, 8.0,
            ["tudo da Fase 2 + EDA nacional", "IP cores proprios",
             "biblioteca de celulas propria"],
            ["rchip_r64 v2", "rchip_r128 (octa-core)", "NPU"],
            "Ferramenta EDA (Cadence/Synopsys). Alternativa open-source: OpenROAD.",
            "RISC-V 100% nacional. Design, mask, fab, test. Soberania real.",
        ),
        FasePlano(
            FaseFab.FASE_4_28NM, NodoProcesso.N_28,
            10, 15.0,
            ["photolith 28nm (ArF immersion)", "todas as outras"],
            ["rchip_r128", "rchip_gpu (GPU basica)", "rchip_npu"],
            "Stepper 28nm ArF immersion. Disponivel mas caro.",
            "SoC completo nacional. GPU basica, NPU para IA local.",
        ),
        FasePlano(
            FaseFab.FASE_5_INOVACAO, NodoProcesso.N_65,
            12, 20.0,
            ["MOCVD (GaN/SiC)", "forno de sinterizacao", "lab de novos materiais"],
            ["rchip_gan (radio potencia)", "rchip_sic (potencia)",
             "rchip_memristor"],
            "Pesquisa em materiais. Colaboracao universitaria.",
            "Chip de potencia GaN/SiC. Transformadores solidos. Display microLED.",
        ),
    ]


# ============================================================================
# 4. SPEC DA FAB NACIONAL
# ============================================================================

class ChipFab:
    """
    Spec de fabrica de chip nacional.

    Soberania de silicio. Sem embargo. Sem dependencia.
    """

    NOME = "OpenChipFab"
    VERSAO = "0.1.0-spec"

    def __init__(self) -> None:
        self.chips: List[ChipSpec] = _init_chips()
        self.fases: List[FasePlano] = _init_fases()

    # -- catalogo -----------------------------------------------------------

    def todos_chips(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": c.id,
                "nome": c.nome,
                "tipo": c.tipo.id,
                "nodo": c.nodo.id,
                "transistores_m": c.transistores,
                "area_mm2": c.area_mm2,
                "clock_mhz": c.clocks_mhz,
                "ram_kb": c.ram_kb,
                "flash_kb": c.flash_kb,
                "gpio": c.gpio,
                "interfaces": c.interfaces,
                "consumo_ma": c.consumo_ma,
                "custo_brl": f"R$ {c.custo_estimado_brl:.2f}",
                "aplicacoes": c.aplicações,
            }
            for c in self.chips
        ]

    def chip(self, chip_id: str) -> Optional[ChipSpec]:
        for c in self.chips:
            if c.id == chip_id:
                return c
        return None

    # -- plano de fases ----------------------------------------------------

    def plano_soberania(self) -> List[Dict[str, Any]]:
        return [
            {
                "fase": f.fase.id,
                "rotulo": f.fase.rotulo,
                "nodo": f.nodo.id,
                "prazo": f"{f.prazo_anos} anos",
                "investimento": f"R$ {f.investimento_brl_bi:.1f} bi",
                "chips": f.chips_fabricaveis,
                "dependencia": f.dependencia_externa,
                "resultado": f.resultado,
            }
            for f in self.fases
        ]

    # -- equipamentos -------------------------------------------------------

    def equipamentos_necessarios(self, fase_id: str) -> List[str]:
        for f in self.fases:
            if f.fase.id == fase_id:
                return f.equipamentos
        return []

    # -- dependencias -------------------------------------------------------

    def mapa_dependencias(self) -> Dict[str, Any]:
        """Mapeia dependencias externas e como quebra-las."""
        return {
            "stepper_fotolito": {
                "fornecedores": ["ASML (Holanda)", "Nikon (Japao)", "Canon (Japao)"],
                "embargo": "180nm-65nm: sem embargo. 28nm: comercial. 14nm: restrito. 3nm: bloqueado.",
                "quebra": "Stepper nacional e prjeto de 20 anos. Parceria com universidade.",
            },
            "silicio_wafer": {
                "fornecedores": ["Shin-Etsu (Japao)", "SUMCO (Japao)", "GlobalWafers (Taiwan)"],
                "embargo": "Nenhum. Commodity.",
                "quebra": "Brasil tem quartz de alta pureza em MG. Purificacao e problema.",
            },
            "eda_software": {
                "fornecedores": ["Cadence (EUA)", "Synopsys (EUA)", "Mentor/Siemens (EUA)"],
                "embargo": "Versoes antigas disponiveis. Novas restritas.",
                "quebra": "OpenROAD (open-source). Precisa de maturidade.",
            },
            "mask_making": {
                "fornecedores": ["Toppan (Japao)", "Photronics (EUA)", "DNP (Japao)"],
                "embargo": "Sem embargo para >= 65nm.",
                "quebra": "E-beam writer nacional. Investimento medio.",
            },
            "fotoresist": {
                "fornecedores": ["JSR (Japao)", "Tokyo Ohka (Japao)", "Shipley (EUA)"],
                "embargo": "Sem embargo para >= 65nm.",
                "quabra": "Quimica fina nacional. Braspol (SP) ja produz quimicos.",
            },
            "gases_especiais": {
                "fornecedores": ["Air Liquide (Franca)", "Linde (Alemanha)", "Praxair (EUA)"],
                "embargo": "Sem embargo.",
                "quebra": "White Martins (BR) ja purifica gases. Precisa de escala.",
            },
        }

    # -- custo total -------------------------------------------------------

    def custo_soberania_total(self) -> Dict[str, Any]:
        total = sum(f.investimento_brl_bi for f in self.fases)
        return {
            "total_bi": f"R$ {total:.1f} bilhoes",
            "comparativo_gripen": f"{total / 36:.1f}x o custo de 36 caças Gripen (R$ 36bi)",
            "comparativo_lava_jato": f"{total / 20:.1f}x o estimado da Lava Jato (R$ 20bi recuperados)",
            "comparativo_bolsa_familia_ano": f"{total / 35:.1f} anos de Bolsa Familia (R$ 35bi/ano)",
        }

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "chips_catalogados": len(self.chips),
            "fases_plano": len(self.fases),
            "nodos_processo": len(list(NodoProcesso)),
            "tipos_chip": len(list(TipoChip)),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    fab = ChipFab()

    print("=" * 70)
    print(f"{fab.NOME} v{fab.VERSAO} -- Soberania de Silicio Nacional")
    print("=" * 70)

    # --- Chips fabricaveis ---
    print(f"\n[CHIPS FABRICAVEIS NACIONALMENTE ({len(fab.chips)})]\n")
    print(f"  {'ID':<16} {'NOME':<35} {'NODO':<8} {'TRANS':>8} {'CUSTO':>8}")
    print(f"  {'-'*80}")
    for c in fab.todos_chips():
        print(f"  {c['id']:<16} {c['nome']:<35} {c['nodo']:<8} "
              f"{c['transistores_m']:>5.3f}M R$ {c['custo_brl']:>5}")

    # --- Plano de fases ---
    print(f"\n\n[PLANO DE SOBERANIA DE SILICIO ({len(fab.fases)} FASES)]\n")
    for p in fab.plano_soberania():
        print(f"\n  [{p['fase'].upper()}] {p['rotulo']}")
        print(f"  Nodo: {p['nodo']} | Prazo: {p['prazo']} | Investimento: {p['investimento']}")
        print(f"  Chips: {', '.join(p['chips'])}")
        print(f"  Dependencia: {p['dependencia']}")
        print(f"  Resultado: {p['resultat']}")

    # --- Mapa de dependencias ---
    print("\n\n[MAPA DE DEPENDENCIAS EXTERNAS]\n")
    for area, info in fab.mapa_dependencias().items():
        print(f"\n  [{area.upper()}]")
        print(f"  Fornecedores: {', '.join(info['fornecedores'])}")
        print(f"  Embargo: {info['embargo']}")
        quebra = info.get('quebra', info.get('quabra', 'N/A'))
        print(f"  Quebra: {quebra}")

    # --- Custo ---
    print("\n\n[CUSTO TOTAL DA SOBERANIA]\n")
    for k, v in fab.custo_soberania_total().items():
        print(f"  {k}: {v}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = fab.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
