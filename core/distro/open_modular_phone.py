#!/usr/bin/env python3
"""
OpenModularPhone -- L0: Smartphone Modular Brasileiro
=======================================================
Spec de smartphone modular aberto. Sucessor espiritual do N900.

Design:
  - Modulos removiveis (bateria, camera, sensor, radio)
  - CPU intercambiavel (ARM V1, RISC-V V2)
  - Tela reparavel (ilhoses, nao cola)
  - Bootloader desbloqueado
  - Linux nativo (Nao Android)
  - 3.5mm jack, microSD, USB-C

Filosofia:
  - O smartphone e do DONO, nao da fabricante
  - Reparo e DIREITO, nao servico premium
  - Modulo custa menos que aparelho novo
  - 7 anos de suporte minimo

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ENUMS
# ============================================================================

class SoCPhone(Enum):
    """SoCs suportados pelo phone modular."""
    RK3588S = ("rk3588s", "Rockchip RK3588S: 4xA76+4xA55, Mali-G610, NPU, 8nm")
    QCOM_7C_GEN2 = ("7c_gen2", "Qualcomm 7c Gen2: 8xCortex-A55, Adreno, 8nm")
    JH7110 = ("jh7110", "StarFive JH7110: RISC-V SiFive, 4xU74, BXE-2-32, 28nm")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def desc(self) -> str:
        return self.value[1]


class ModuloTipo(Enum):
    """Tipos de modulos removiveis."""
    BATERIA = ("bateria", "Bateria intercambiavel")
    CAMERA = ("camera", "Modulo de camera")
    SENSOR = ("sensor", "Sensor (temperatura, umidade, IR, UV, geiger)")
    RADIO = ("radio", "Radio (LoRa, NFC, FM, DTV)")
    AUDIO = ("audio", "Audio (DAC, amp, microfone direcional)")
    ARMAZENAMENTO = ("storage", "Armazenamento (NVMe, microSD)")
    BIOMETRIA = ("biometria", "Biometria (impressao, iris, veia)")
    SAUDE = ("saude", "Saude (oximetro, ECG, glicemia)")
    ENERGIA = ("energia", "Energia (solar, termoeletrica, cinetica)")
    EXPANSAO = ("expansao", "Expansao (GPIO, serial, JTAG, SDR)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class OSPhone(Enum):
    """Sistemas operacionais suportados (NENHUM e Android)."""
    POSTMARKETOS = ("pmos", "postmarketOS: Alpine Linux, mainline kernel")
    MOBIAN = ("mobian", "Mobian: Debian-based, Phosh shell")
    UBPORTS = ("ubports", "Ubuntu Touch: Ubuntu-based, confinement")
    PLASMA_MOBILE = ("plasma", "KDE Plasma Mobile: full desktop on phone")
    SXMO = ("sxmo", "sxmo: minimal, suckless, dwm on phone")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class ConectorModulo(Enum):
    """Padrao de conector para modulos."""
    POGO_MAGNETICO = ("pogo", "Pogo pin magnetico: 12 pinos,MagSafe-style")
    MIFI_MEZZANINE = ("mezzanine", "MIPI mezzanine: camera/display standard")
    USBC_ALT = ("usbc", "USB-C alternate mode + GPIO bridge")
    EDGE_CONNECTOR = ("edge", "Edge connector: tipo cartucho Game Boy")

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
class ConfigPhone:
    """Configuracao de hardware base do phone."""
    soc: SoCPhone
    ram_gb: int
    storage_gb: int
    tela_polegadas: float
    tela_resolucao: Tuple[int, int]
    refresh_rate: int
    bateria_mah: int
    peso_g: int
    dimensoes_mm: Tuple[float, float, float]  # L x A x P
    conector_principal: ConectorModulo
    slots_modulo: int
    jack_35mm: bool
    microsd: bool
    usbc: bool
    nfc: bool
    bluetooth: int  # versao (50 = 5.0, 52 = 5.2)
    wifi: str       # "6", "6E"
    gps: bool
    glonass: bool
    galileo: bool
    sbas: bool


@dataclass(frozen=True)
class Modulo:
    """Um modulo removivel."""
    id: str
    tipo: ModuloTipo
    nome: str
    preco_estimado_brl: int
    consumo_mw: float           # consumo em mW
    peso_g: int
    vida_util_anos: int
    descricao: str


# ============================================================================
# 3. CATALOGO DE MODULOS
# ============================================================================

def _init_modulos() -> List[Modulo]:
    return [
        Modulo("bat_5000", ModuloTipo.BATERIA, "Bateria 5000mAh",
               120, 0.0, 95, 3,
               "Bateria intercambiavel. 5000mAh. 2 slots. Carrega em 45min."),
        Modulo("bat_8000", ModuloTipo.BATERIA, "Bateria 8000mAh Extendida",
               180, 0.0, 140, 3,
               "Bateria extended. 8000mAh. Dobra a espessura. 3 dias de uso."),
        Modulo("cam_48mp", ModuloTipo.CAMERA, "Camera 48MP Sony IMX582",
               250, 450, 22, 5,
               "Camera principal 48MP, f/1.8, OIS. Postprocessing local com NPU."),
        Modulo("cam_ir", ModuloTipo.CAMERA, "Camera Infravermelho (FLIR Lepton)",
               450, 250, 15, 7,
               "Camera termica. Ve calor. Manutencao predial, inspecao eletrica, resgate."),
        Modulo("sensor_env", ModuloTipo.SENSOR, "Sensor Ambiental (BME680 + PMSA003)",
               80, 15, 8, 7,
               "Temperatura, umidade, pressao, VOC, particulas PM2.5. Qualidade do ar."),
        Modulo("sensor_geiger", ModuloTipo.SENSOR, "Contador Geiger",
               350, 50, 35, 10,
               "Radiacao ionizante. Cidadão sensor (P13). Mapeamento ambiental."),
        Modulo("radio_lora", ModuloTipo.RADIO, "LoRa SX1262 (868/915MHz)",
               90, 100, 12, 10,
               "LoRa de longo alcance. Mesh comunitario. Offline-first."),
        Modulo("radio_sdr", ModuloTipo.RADIO, "SDR RTL2832U (100kHz-1.7GHz)",
               200, 800, 25, 10,
               "Software Defined Radio. Scanner. Contravigilancia (P13)."),
        Modulo("radio_fm", ModuloTipo.RADIO, "FM/NOAA/Aviation",
               40, 60, 8, 15,
               "Radio FM + NOAA + banda aerea. Emergencia, escuta civil."),
        Modulo("audio_dac", ModuloTipo.AUDIO, "DAC ESS Sabre + Amp",
               200, 300, 18, 10,
               "DAC audiofilo. 32-bit/384kHz. AMP para headphone de alta impedancia."),
        Modulo("audio_mic", ModuloTipo.AUDIO, "Microfone Direcional (Shotgun)",
               150, 100, 20, 7,
               "Microfone direcional. Cego escuta ambiente. Jornalista grava."),
        Modulo("bio_fp", ModuloTipo.BIOMETRIA, "Leitor de Impressao Digital",
               60, 50, 5, 7,
               "Impressao digital capacitive. Dados locais, nunca cloud."),
        Modulo("bio_iris", ModuloTipo.BIOMETRIA, "Scanner de Iris",
               180, 400, 12, 7,
               "Iris recognition. Mais seguro que impressao. Dados locais."),
        Modulo("saude_oxi", ModuloTipo.SAUDE, "Oximetro + ECG",
               220, 100, 15, 5,
               "SpO2 + eletrocardiograma. Saude comunitaria. Dados locais."),
        Modulo("saude_glic", ModuloTipo.SAUDE, "Glicosimetro nao-invasivo",
               500, 200, 20, 5,
               "Glicemia sem furar dedo. Infravermelho. Pesquisa, nao medico."),
        Modulo("energia_solar", ModuloTipo.ENERGIA, "Painel Solar 2W",
               120, 0.0, 40, 10,
               "Recarga solar. 2W. Emergencia. Acampamento. Feld, praça, rua."),
        Modulo("energia_cinetica", ModuloTipo.ENERGIA, "Gerador Cinetico",
               200, 0.0, 60, 10,
               "Recarga por movimento. Shake-to-charge. Crank. Socorro."),
        Modulo("exp_gpio", ModuloTipo.EXPANSAO, "GPIO Breakout (40 pinos)",
               50, 0.0, 10, 15,
               "Raspberry-Pi compatible GPIO. Maker, IoT, prototipagem."),
        Modulo("exp_jtag", ModuloTipo.EXPANSAO, "JTAG + Serial Debug",
               40, 0.0, 8, 15,
               "Debug e flash. Reparo de hardware. Reversing."),
        Modulo("storage_nvme", ModuloTipo.ARMAZENAMENTO, "NVMe 1TB (M.2 2230)",
               400, 2000, 8, 7,
               "1TB NVMe em modulo. Mais rapido que microSD. Criptografia local."),
    ]


# ============================================================================
# 4. SPEC DO PHONE MODULAR
# ============================================================================

class ModularPhone:
    """
    Spec do smartphone modular da Republica.

    O phone e do dono. Reparo e direito. Modulo custa menos que aparelho.
    """

    NOME = "Republica Phone"
    VERSAO = "0.1.0-spec"
    FILISTROFIA = "O smartphone e do DONO, nao da fabricante"

    # Direitos do dono (P2 autonomia corporal aplicado a hardware)
    DIREITOS_DONO = [
        "Bootloader desbloqueado de fabrica",
        "Root sem void warranty",
        "Reparo sem autorizacao de fabricante",
        "Modulos de terceiros sem certificacao",
        "SoC intercambiavel (ARM hoje, RISC-V amanha)",
        "7 anos minimo de patches de seguranca",
        "Documentacao completa de hardware (schematics)",
        "NENHUM chip de gestao de direitos (DRM)",
    ]

    def __init__(self) -> None:
        self.modulos: List[Modulo] = _init_modulos()
        self.socs: List[SoCPhone] = list(SoCPhone)
        self.oses: List[OSPhone] = list(OSPhone)
        self.conectores: List[ConectorModulo] = list(ConectorModulo)

    # -- config V1 (ARM) ---------------------------------------------------

    def config_v1_arm(self) -> ConfigPhone:
        """Configuracao V1 com SoC ARM (disponivel hoje)."""
        return ConfigPhone(
            soc=SoCPhone.RK3588S,
            ram_gb=8,
            storage_gb=128,
            tela_polegadas=6.0,
            tela_resolucao=(2460, 1080),
            refresh_rate=90,
            bateria_mah=5000,
            peso_g=210,
            dimensoes_mm=(155.0, 75.0, 12.0),  # 12mm com modulo
            conector_principal=ConectorModulo.POGO_MAGNETICO,
            slots_modulo=2,
            jack_35mm=True,
            microsd=True,
            usbc=True,
            nfc=True,
            bluetooth=52,
            wifi="6",
            gps=True,
            glonass=True,
            galileo=True,
            sbas=True,
        )

    # -- config V2 (RISC-V) ------------------------------------------------

    def config_v2_riscv(self) -> ConfigPhone:
        """Configuracao V2 com SoC RISC-V (soberania de silicio)."""
        return ConfigPhone(
            soc=SoCPhone.JH7110,
            ram_gb=8,
            storage_gb=64,
            tela_polegadas=6.0,
            tela_resolucao=(2460, 1080),
            refresh_rate=60,
            bateria_mah=5000,
            peso_g=215,
            dimensoes_mm=(155.0, 75.0, 12.5),
            conector_principal=ConectorModulo.POGO_MAGNETICO,
            slots_modulo=2,
            jack_35mm=True,
            microsd=True,
            usbc=True,
            nfc=False,        # ainda nao suportado em RISC-V mainline
            bluetooth=50,
            wifi="5",         # wifi 5 em RISC-V por enquanto
            gps=True,
            glonass=False,    # driver pendente
            galileo=False,    # driver pendente
            sbas=False,
        )

    # -- catalogos ---------------------------------------------------------

    def todos_modulos(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": m.id,
                "tipo": m.tipo.id,
                "nome": m.nome,
                "preco": f"R$ {m.preco_estimado_brl}",
                "consumo_mw": m.consumo_mw,
                "peso_g": m.peso_g,
                "vida_util": f"{m.vida_util_anos} anos",
                "descricao": m.descricao,
            }
            for m in self.modulos
        ]

    def modulos_por_tipo(self, tipo: ModuloTipo) -> List[Modulo]:
        return [m for m in self.modulos if m.tipo == tipo]

    def modulos_para_cego(self) -> List[Modulo]:
        """Modulos especificamente uteis para cego (L5)."""
        uteis = {"audio_mic", "radio_sdr", "audio_dac", "radio_fm",
                 "sensor_env", "radio_lora", "exp_gpio"}
        return [m for m in self.modulos if m.id in uteis]

    def modulos_para_saude(self) -> List[Modulo]:
        return self.modulos_por_tipo(ModuloTipo.SAUDE)

    # -- custo total -------------------------------------------------------

    def custo_completo(self) -> Dict[str, Any]:
        """Custo estimado do phone base + todos modulos."""
        v1 = self.config_v1_arm()
        phone_base = 1500  # estimativa base sem modulo

        modulos_brasil = [
            "bat_5000", "cam_48mp", "sensor_env", "radio_lora",
            "audio_dac", "bio_fp", "storage_nvme",
        ]
        custo_modulos = sum(
            m.preco_estimado_brl for m in self.modulos if m.id in modulos_brasil
        )

        return {
            "phone_base": f"R$ {phone_base}",
            "modulos_brasil": f"R$ {custo_modulos}",
            "total_completo": f"R$ {phone_base + custo_modulos}",
            "iphone_15_pro_comparativo": "R$ 7.999",
            "razao": f"{(phone_base + custo_modulos) / 7999:.0%} do iPhone",
        }

    # -- comparativo -------------------------------------------------------

    def comparativo_fechado(self) -> List[Dict[str, str]]:
        return [
            {"recurso": "Bootloader", "republica": "Desbloqueado",
             "iphone": "Bloqueado", "android": "Bloqueado (maioria)"},
            {"recurso": "Reparo", "republica": "Modulo troca em casa",
             "iphone": "Autorizada +$$$", "android": "Autorizada ou descarte"},
            {"recurso": "Bateria", "republica": "Removivel, 2 slots",
             "iphone": "Colada, precisa aquecedor", "android": "Poucos tem removivel"},
            {"recurso": "Audio", "republica": "3.5mm + DAC modular",
             "iphone": "Sem jack, dongle", "android": "Poucos tem jack"},
            {"recurso": "OS", "republica": "Linux nativo (5 opcoes)",
             "iphone": "iOS (fechado)", "android": "Android (Google)"},
            {"recurso": "SoC", "republica": "Intercambiavel",
             "iphone": "Soldado", "android": "Soldado"},
            {"recurso": "Suporte", "republica": "7 anos minimo",
             "iphone": "5-6 anos", "android": "2-4 anos (maioria)"},
            {"recurso": "Schematics", "republica": "Aberto",
             "iphone": "Sigilo", "android": "Sigilo"},
            {"recurso": "DRM", "republica": "Nenhum",
             "iphone": "Multiple layers", "android": "Multiple layers"},
            {"recurso": "Dados biometricos", "republica": "Local, nunca cloud",
             "iphone": "Enclave (nao auditavel)", "android": "Google (nao auditavel)"},
        ]

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "nome": self.NOME,
            "versao": self.VERSAO,
            "modulos_catalogados": len(self.modulos),
            "tipos_modulo": len(list(ModuloTipo)),
            "socs_suportados": len(self.socs),
            "os_suportados": len(self.oses),
            "direitos_dono": len(self.DIREITOS_DONO),
            "suporte_minimo_anos": 7,
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    ph = ModularPhone()

    print("=" * 70)
    print(f"{ph.NOME} v{ph.VERSAO} -- Spec de Smartphone Modular")
    print("=" * 70)

    # --- Direitos do dono ---
    print(f"\n[DIREITOS DO DONO ({len(ph.DIREITOS_DONO)})]\n")
    for i, d in enumerate(ph.DIREITOS_DONO, 1):
        print(f"  {i}. {d}")

    # --- V1 ARM ---
    v1 = ph.config_v1_arm()
    print(f"\n\n[V1 ARM ({v1.soc.desc})]\n")
    print(f"  SoC: {v1.soc.id} -- {v1.soc.desc}")
    print(f"  RAM: {v1.ram_gb}GB | Storage: {v1.storage_gb}GB")
    print(f"  Tela: {v1.tela_polegadas}\" {v1.tela_resolucao[0]}x{v1.tela_resolucao[1]} @ {v1.refresh_rate}Hz")
    print(f"  Bateria: {v1.bateria_mah}mAh (intercambiavel)")
    print(f"  Peso: {v1.peso_g}g | Dim: {v1.dimensoes_mm[0]}x{v1.dimensoes_mm[1]}x{v1.dimensoes_mm[2]}mm")
    print(f"  Modulos: {v1.slots_modulo} slots ({v1.conector_principal.rotulo})")
    print(f"  Jack 3.5mm: {v1.jack_35mm} | microSD: {v1.microsd} | USB-C: {v1.usbc}")
    print(f"  NFC: {v1.nfc} | BT 5.{v1.bluetooth % 10} | WiFi {v1.wifi}")

    # --- V2 RISC-V ---
    v2 = ph.config_v2_riscv()
    print(f"\n\n[V2 RISC-V ({v2.soc.desc})]\n")
    print(f"  SoC: {v2.soc.id} -- {v2.soc.desc}")
    print(f"  RAM: {v2.ram_gb}GB | Storage: {v2.storage_gb}GB (microSD primario)")
    print(f"  Tela: {v2.tela_polegadas}\" {v2.tela_resolucao[0]}x{v2.tela_resolucao[1]} @ {v2.refresh_rate}Hz")
    print(f"  Bateria: {v2.bateria_mah}mAh")
    print(f"  Diferencas V1: NFC={v2.nfc} BT={v2.bluetooth} WiFi={v2.wifi}")
    print(f"  GNSS: GPS={v2.gps} GLONASS={v2.glonass} Galileo={v2.galileo}")

    # --- OS ---
    print(f"\n\n[SISTEMAS OPERACIONAIS ({len(ph.oses)} -- NENHUM e Android)]\n")
    for os_ in ph.oses:
        print(f"  {os_.id:<10} {os_.rotulo}")

    # --- Modulos ---
    print(f"\n\n[MODULOS ({len(ph.modulos)})]\n")
    print(f"  {'ID':<18} {'TIPO':<14} {'NOME':<35} {'PRECO':<8} {'CONSUMO':<8}")
    print(f"  {'-'*90}")
    for m in ph.modulos:
        print(f"  {m.id:<18} {m.tipo.id:<14} {m.nome:<35} R$ {m.preco_estimado_brl:<5} {m.consumo_mw:>5.0f}mW")

    # --- Modulos para cego ---
    print(f"\n\n[MODULOS PARA CEGO (L5)]\n")
    for m in ph.modulos_para_cego():
        print(f"  {m.id:<18} {m.nome}")

    # --- Custo ---
    print("\n\n[CUSTO ESTIMADO]\n")
    custo = ph.custo_completo()
    for k, v in custo.items():
        print(f"  {k}: {v}")

    # --- Comparativo ---
    print("\n\n[COMPARATIVO: REPUBLICA vs FECHADO]\n")
    print(f"  {'RECURSO':<22} {'REPUBLICA':<28} {'IPHONE':<22} {'ANDROID'}")
    print(f"  {'-'*95}")
    for c in ph.comparativo_fechado():
        print(f"  {c['recurso']:<22} {c['republica']:<28} {c['iphone']:<22} {c['android']}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = ph.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
