#!/usr/bin/env python3
"""
OpenForgeOS -- L0: Servidor de Games Open Source
==================================================
Spec de sistema operacional para Mini PC servidor de jogos.

Hardware alvo:
  - Mini PC ARM (RK3588) ou x86 (N100)
  - 16-32GB RAM
  - 512GB-2TB NVMe
  - GPU opcional (eGPU USB4)

Software base:
  - NixOS (declarativo, reprodutivel)
  - Sunshine/Moonlight (game streaming)
  - Proton/Wine (compatibilidade Windows)
  - RetroArch (emulacao)
  - Steam Headless (biblioteca remota)

Camadas do sistema:
  L0  NixOS base (kernel, firmware, rede)
  L1  Sunshine (host de streaming, GPU virtual)
  L2  Moonlight (cliente, qualquer tela)
  L3  Proton/Wine (camada de compatibilidade)
  L4  RetroArch (8/16/32 bit, ate PS1/N64)
  L5  Steam Headless (biblioteca, downloads)
  L6  Controle remoto (Bluetooth, web pad)
  L7  Acessibilidade (narração de menu, mapeamento de botões)

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ENUMS
# ============================================================================

class ArquiteturaHardware(Enum):
    """Arquiteturas de hardware suportadas."""
    ARM_RK3588 = ("rk3588", "ARM a76x4 + a55x4, Mali-G610, NPU 6TOPS")
    X86_N100 = ("n100", "Intel N100, 4 cores, UHD Graphics")
    X86_RYZEN = ("ryzen", "AMD Ryzen 5600G/5700G, Radeon Vega")
    RISCV_JH7110 = ("jh7110", "RISC-V SiFive, StarFive VisionFive 2")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def desc(self) -> str:
        return self.value[1]


class CamadaForge(Enum):
    """As 8 camadas do ForgeOS."""
    KERNEL = (0, "kernel", "NixOS base: kernel, firmware, rede, SSH")
    HOST = (1, "host", "Sunshine: host de streaming, captura de GPU, encode H.264/H.265/AV1")
    CLIENTE = (2, "cliente", "Moonlight: cliente para qualquer tela (TV, celular, tablet)")
    COMPAT = (3, "compat", "Proton/Wine: camada de compatibilidade para jogos Windows")
    RETRO = (4, "retro", "RetroArch: emulacao 8/16/32-bit ate PS1/N64")
    BIBLIOTECA = (5, "biblioteca", "Steam Headless: biblioteca, downloads remotos")
    CONTROLE = (6, "controle", "Controle remoto: Bluetooth, web gamepad, gyro")
    ACESSIBILIDADE = (7, "a11y", "Acessibilidade: narracao de menu, remap de botoes, contraste")

    @property
    def numero(self) -> int:
        return self.value[0]

    @property
    def id(self) -> str:
        return self.value[1]

    @property
    def rotulo(self) -> str:
        return self.value[2]


class CodecVideo(Enum):
    """Codecs de video suportados para streaming."""
    H264 = ("h264", "H.264/AVC: compatibilidade maxima, todo dispositivo")
    H265 = ("h265", "H.265/HEVC: 50% menos banda, mesma qualidade")
    AV1 = ("av1", "AV1: codec aberto, melhor compressao, hardware recente")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class ResolucaoStream(Enum):
    """Resolucoes de streaming suportadas."""
    SD_720 = ("720p", "1280x720 @ 60fps", 10)      # Mbps min
    HD_1080 = ("1080p", "1920x1080 @ 60fps", 20)
    QHD_1440 = ("1440p", "2560x1440 @ 60fps", 35)
    UHD_4K = ("4k", "3840x2160 @ 60fps", 60)
    UHD_4K_120 = ("4k120", "3840x2160 @ 120fps", 80)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def mbps_min(self) -> int:
        return self.value[2]


class RetroCore(Enum):
    """Cores de emulacao do RetroArch (open-source)."""
    NES = ("nes", "Nintendo Entertainment System (1983)", "mesen")
    SNES = ("snes", "Super Nintendo (1990)", "bsnes_hd")
    GENESIS = ("genesis", "Sega Genesis/Mega Drive (1988)", "genesis_plus_gx")
    GAMEBOY = ("gb", "Game Boy / GBC / GBA (1989-2001)", "sameboy")
    PS1 = ("ps1", "PlayStation 1 (1994)", "swanstation")
    N64 = ("n64", "Nintendo 64 (1996)", "mupen64plus_next")
    ARCADE = ("arcade", "Arcade (FBNeo)", "fbneo")
    ATARI = ("atari", "Atari 2600 (1977)", "stella")
    MASTERSYS = ("ms", "Sega Master System (1985)", "genesis_plus_gx")
    PCE = ("pce", "PC Engine/TurboGrafx (1987)", "beetle_pce_fast")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def core(self) -> str:
        return self.value[2]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass(frozen=True)
class ConfigHardware:
    """Configuracao minima e recomendada de hardware."""
    arquitetura: ArquiteturaHardware
    ram_min_gb: int
    ram_rec_gb: int
    storage_min_gb: int
    storage_rec_gb: int
    gpu_necessaria: bool
    npu_opcional: bool
    usb4_thunderbolt: bool
    bluetooth: bool
    wifi6: bool
    ethernet_gbps: float
    preco_estimado_brl: Tuple[int, int]  # (min, max)


@dataclass(frozen=True)
class ConfigStream:
    """Configuracao de streaming."""
    codec: CodecVideo
    resolucao: ResolucaoStream
    bitrate_mbps: int
    latencia_alvo_ms: int
    packet_loss_tol: float  # %
    adaptive_bitrate: bool


@dataclass
class GameEntry:
    """Entrada de jogo na biblioteca."""
    id: str
    titulo: str
    plataforma: str           # "steam", "epic", "gog", "retro", "wine"
    caminho_exec: str         # path ou comando
    compatibilidade: str      # "nativo", "proton", "wine", "emulador"
    cover_art: str            # path ou URL
    acessivel: bool           # tem narracao/contraste/remap?
    rating_pegi: str          # idade


# ============================================================================
# 3. CATALOGO DE HARDWARE ALVO
# ============================================================================

def _init_hardware() -> List[ConfigHardware]:
    return [
        ConfigHardware(
            ArquiteturaHardware.ARM_RK3588,
            8, 16, 256, 1024,
            gpu_necessaria=False,  # Mali-G610 integrada
            npu_opcional=True,     # NPU 6TOPS para upscale
            usb4_thunderbolt=False,
            bluetooth=True,
            wifi6=True,
            ethernet_gbps=2.5,
            preco_estimado_brl=(350, 900),
        ),
        ConfigHardware(
            ArquiteturaHardware.X86_N100,
            8, 16, 256, 1024,
            gpu_necessaria=False,  # UHD Graphics integrada
            npu_opcional=False,
            usb4_thunderbolt=False,
            bluetooth=True,
            wifi6=True,
            ethernet_gbps=2.5,
            preco_estimado_brl=(600, 1200),
        ),
        ConfigHardware(
            ArquiteturaHardware.X86_RYZEN,
            16, 32, 512, 2048,
            gpu_necessaria=False,  # Vega integrada (5600G/5700G)
            npu_opcional=False,
            usb4_thunderbolt=True,  # eGPU possivel
            bluetooth=True,
            wifi6=True,
            ethernet_gbps=2.5,
            preco_estimado_brl=(1200, 2500),
        ),
        ConfigHardware(
            ArquiteturaHardware.RISCV_JH7110,
            8, 16, 128, 512,
            gpu_necessaria=False,  # Imagination BXE-2-32
            npu_opcional=False,
            usb4_thunderbolt=False,
            bluetooth=False,       # requer dongle
            wifi6=False,           # requer dongle
            ethernet_gbps=1.0,
            preco_estimado_brl=(500, 800),
        ),
    ]


# ============================================================================
# 4. SPEC DO FORGE OS
# ============================================================================

class ForgeOS:
    """
    Spec do sistema operacional ForgeOS.

    ForgeOS e NixOS configurado para ser servidor de jogos.
    Tudo e declarativo. Um arquivo .nix define o sistema inteiro.
    """

    NOME = "ForgeOS"
    VERSAO = "0.1.0-spec"
    BASE = "NixOS 24.05"
    LICENCA = "GPL-3.0 + MIT (componentes)"

    def __init__(self) -> None:
        self.hardware: List[ConfigHardware] = _init_hardware()
        self.camadas: List[CamadaForge] = list(CamadaForge)
        self.codecs: List[CodecVideo] = list(CodecVideo)
        self.resolucoes: List[ResolucaoStream] = list(ResolucaoStream)
        self.retro_cores: List[RetroCore] = list(RetroCore)

    # -- spec nix -----------------------------------------------------------

    def spec_nixos(self) -> str:
        """Gera o arquivo configuration.nix base do ForgeOS."""
        return f"""# {{ self.NOME }} v{{ self.VERSAO }}
# Spec gerada por open_forge_os.py
# NAO EDITAR MANUALMENTE -- regenere deste modulo.

{{ config, pkgs, ... }}:

{{
  # ============================================================
  # L0: KERNEL E BASE
  # ============================================================
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  networking.hostName = "forge";
  networking.networkmanager.enable = true;

  # SSH para administracao remota
  services.openssh.enable = true;
  services.openssh.settings.PasswordAuthentication = false;

  # Firewall: abrir portas de streaming
  networking.firewall.allowedTCPPorts = [ 47984 47989 47990 48010 ];
  networking.firewall.allowedUDPPorts = [ 47998 47999 48000 48002 48010 ];

  # ============================================================
  # L1: SUNSHINE (HOST DE STREAMING)
  # ============================================================
  services.sunshine = {{
    enable = true;
    openFirewall = true;
    settings = {{
      codec = "hevc";           # H.265 (codec.id)
      resolution = "1920x1080"; # ResolucaoStream
      fps = 60;
      bitrate = 20000;          # 20 Mbps
    }};
  }};

  # ============================================================
  # L3: PROTON/WINE (COMPATIBILIDADE)
  # ============================================================
  programs.steam.enable = true;
  programs.steam.remotePlay.openFirewall = true;
  programs.gamemode.enable = true;

  # Proton-GE (versao customizada com mais fixes)
  # Instalado via protonup-qt

  # ============================================================
  # L4: RETROARCH (EMULACAO)
  # ============================================================
  programs.retroarch.enable = true;
  # Cores: nes, snes, genesis, gb, ps1, n64, arcade, atari, ms, pce

  # ============================================================
  # L7: ACESSIBILIDADE
  # ============================================================
  services.orca.enable = true;           # Leitor de tela
  hardware.opentabletdriver.enable = true; # Mapeamento de controle

  # ============================================================
  # USUARIO
  # ============================================================
  users.users.forge = {{
    isNormalUser = true;
    extraGroups = [ "wheel" "video" "audio" "input" ];
    shell = pkgs.zsh;
  }};

  # ============================================================
  # PACOTES
  # ============================================================
  environment.systemPackages = with pkgs; [
    sunshine
    moonlight-qt
    steam
    steam-tui           # Steam no terminal
    protonup-qt         # Gerenciador de Proton-GE
    retroarch           # Emulacao
    gamemode             # Otimizacao de performance
    mangohud            # Overlay de FPS/temperatura
    gamescope           # Compositor para jogos
    orca                # Leitor de tela
    rustdesk            # Acesso remoto alternativo
  ];

  # GPU
  hardware.graphics.enable = true;
  hardware.graphics.enable32Bit = true;

  # Bluetooth (controle sem fio)
  hardware.bluetooth.enable = true;

  system.stateVersion = "24.05";
}}
"""

    # -- spec stream --------------------------------------------------------

    def spec_stream_padrao(self) -> ConfigStream:
        return ConfigStream(
            codec=CodecVideo.H265,
            resolucao=ResolucaoStream.HD_1080,
            bitrate_mbps=20,
            latencia_alvo_ms=16,
            packet_loss_tol=2.0,
            adaptive_bitrate=True,
        )

    def spec_stream_4k(self) -> ConfigStream:
        return ConfigStream(
            codec=CodecVideo.AV1,
            resolucao=ResolucaoStream.UHD_4K,
            bitrate_mbps=60,
            latencia_alvo_ms=20,
            packet_loss_tol=1.0,
            adaptive_bitrate=True,
        )

    def spec_stream_baixa_banda(self) -> ConfigStream:
        return ConfigStream(
            codec=CodecVideo.H264,
            resolucao=ResolucaoStream.SD_720,
            bitrate_mbps=8,
            latencia_alvo_ms=30,
            packet_loss_tol=5.0,
            adaptive_bitrate=True,
        )

    # -- catalogos ----------------------------------------------------------

    def hardware_suportado(self) -> List[Dict[str, Any]]:
        return [
            {
                "arquitetura": h.arquitetura.id,
                "desc": h.arquitetura.desc,
                "ram_min": f"{h.ram_min_gb}GB",
                "ram_rec": f"{h.ram_rec_gb}GB",
                "storage_min": f"{h.storage_min_gb}GB",
                "storage_rec": f"{h.storage_rec_gb}GB",
                "gpu": "integrada" if not h.gpu_necessaria else "necessaria",
                "npu": h.npu_opcional,
                "usb4": h.usb4_thunderbolt,
                "bt": h.bluetooth,
                "wifi6": h.wifi6,
                "ethernet": f"{h.ethernet_gbps}Gbps",
                "preco": f"R$ {h.preco_estimado_brl[0]}-{h.preco_estimado_brl[1]}",
            }
            for h in self.hardware
        ]

    def camadas_sistema(self) -> List[Dict[str, Any]]:
        return [
            {"L": c.numero, "id": c.id, "rotulo": c.rotulo}
            for c in self.camadas
        ]

    def cores_retro(self) -> List[Dict[str, str]]:
        return [
            {"id": r.id, "plataforma": r.rotulo, "core": r.core}
            for r in self.retro_cores
        ]

    # -- compatibilidade -----------------------------------------------------

    def compatibilidade_jogo(self, plataforma: str) -> str:
        """Retorna a camada de compatibilidade necessaria."""
        mapa = {
            "linux": "nativo",
            "steam_linux": "nativo (Steam Linux)",
            "steam_windows": "Proton/Proton-GE",
            "epic": "Heroic Games Launcher + Wine",
            "gog": "Heroic Games Launcher + Wine",
            "windows_exe": "Wine/Lutris",
            "nes": f"RetroArch core: {RetroCore.NES.core}",
            "snes": f"RetroArch core: {RetroCore.SNES.core}",
            "genesis": f"RetroArch core: {RetroCore.GENESIS.core}",
            "ps1": f"RetroArch core: {RetroCore.PS1.core}",
            "n64": f"RetroArch core: {RetroCore.N64.core}",
        }
        return mapa.get(plataforma.lower(), "desconhecido")

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "base": self.BASE,
            "licenca": self.LICENCA,
            "hardware_suportado": len(self.hardware),
            "camadas": len(self.camadas),
            "codecs": len(self.codecs),
            "resolucoes": len(self.resolucoes),
            "cores_retro": len(self.retro_cores),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    fos = ForgeOS()

    print("=" * 70)
    print(f"{fos.NOME} v{fos.VERSAO} -- Spec de Servidor de Games")
    print("=" * 70)

    # --- Hardware ---
    print(f"\n[HARDWARE SUPORTADO ({len(fos.hardware)} plataformas)]\n")
    print(f"  {'ARQ':<10} {'RAM':<10} {'STORAGE':<14} {'GPU':<12} {'PRECOS':<20}")
    print(f"  {'-'*70}")
    for h in fos.hardware_suportado():
        print(f"  {h['arquitetura']:<10} {h['ram_rec']:<10} {h['storage_rec']:<14} "
              f"{h['gpu']:<12} {h['preco']}")

    # --- Camadas ---
    print(f"\n\n[CAMADAS DO SISTEMA ({len(fos.camadas)})]\n")
    for c in fos.camadas_sistema():
        print(f"  L{c['L']} [{c['id']}] {c['rotulo']}")

    # --- Streaming ---
    print("\n\n[CONFIGURACOES DE STREAM]\n")
    for nome, cfg in [("Padrao (1080p)", fos.spec_stream_padrao()),
                      ("4K", fos.spec_stream_4k()),
                      ("Baixa Banda", fos.spec_stream_baixa_banda())]:
        print(f"  {nome}:")
        print(f"    Codec: {cfg.codec.rotulo}")
        print(f"    Resolucao: {cfg.resolucao.rotulo}")
        print(f"    Bitrate: {cfg.bitrate_mbps} Mbps")
        print(f"    Latencia alvo: {cfg.latencia_alvo_ms}ms")
        print()

    # --- Retro ---
    print(f"[CORES DE EMULACAO ({len(fos.retro_cores)})]\n")
    for r in fos.cores_retro():
        print(f"  {r['id']:<10} {r['plataforma']:<40} core: {r['core']}")

    # --- Compatibilidade ---
    print("\n\n[COMPATIBILIDADE DE PLATAFORMA]\n")
    for plat in ["linux", "steam_windows", "epic", "gog", "ps1", "n64"]:
        print(f"  {plat:<20} -> {fos.compatibilidade_jogo(plat)}")

    # --- NixOS ---
    print("\n\n[SPEC NIXOS (configuration.nix)]\n")
    nix = fos.spec_nixos()
    for linha in nix.split("\n")[:30]:
        print(f"  {linha}")
    print(f"  ... ({len(nix.split(chr(10)))} linhas total)")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = fos.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<24} {v}")


if __name__ == "__main__":
    _demo()
