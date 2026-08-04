#!/usr/bin/env python3
"""
OpenHapticNavigation -- Navegacao por Vibracao para Cegos
==========================================================
"O cego nao precisa de voz o tempo todo.
As vezes o silencio e melhor. As vezes a vibracao fala.
Vire a esquerda = um toque no pulso esquerdo.
Obstaculo a frente = vibracao crescente na cintura.
Destino chegando = pulsacao ritmica no tornozelo.

A navegacao haptica e INSTINTIVA. Nao precisa traduzir.
O corpo ENTENDE. Como um sexto sentido que nasce da tecnologia.

DISPOSITIVOS HAPTICOS:
- Smartwatch (pulso esquerdo/direito)
- Bracelete haptico (bracos, pernas, cintura)
- Colete tatil (tronco -- direcional)
- Anel inteligente (dedo -- toque sutil)
- Tornozeleira vibratória (pes -- direcao)
- Cinto haptico (cintura -- 360 graus)

O sistema mapeia o ambiente (camera + GPS + lidar) e traduz
em PADROES DE VIBRACAO que o corpo entende sem precisar pensar.

SEM FONE. SEM VOZ. SEM CHAMAR ATENCAO.
Discreto. Silencioso. Instintivo.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import deque
import time
import math


# ============================================================================
# 1. DISPOSITIVOS HAPTICOS
# ============================================================================

class HapticDevice(Enum):
    SMARTWATCH_LEFT = "smartwatch_esquerdo"
    SMARTWATCH_RIGHT = "smartwatch_direito"
    BRACELET_LEFT_ARM = "braceaco_esquerdo"
    BRACELET_RIGHT_ARM = "braceaco_direito"
    ANKLE_LEFT = "tornozelo_esquerdo"
    ANKLE_RIGHT = "tornozelo_direito"
    WAIST_BAND = "cinto_cintura"
    CHEST_VEST = "colete_peito"
    RING_FINGER = "anel_dedo"
    NECKBAND = "colar_pescoco"
    INSOLE_LEFT = " palmilha_esquerda"
    INSOLE_RIGHT = "palmilha_direita"


class BodyPosition(Enum):
    """Onde no corpo o dispositivo fica."""
    LEFT_WRIST = "pulso_esquerdo"
    RIGHT_WRIST = "pulso_direito"
    LEFT_ARM = "braco_esquerdo"
    RIGHT_ARM = "braco_direito"
    LEFT_ANKLE = "tornozelo_esquerdo"
    RIGHT_ANKLE = "tornozelo_direito"
    WAIST = "cintura"
    CHEST = "peito"
    FINGER = "dedo"
    NECK = "pescoco"
    LEFT_FOOT = "pe_esquerdo"
    RIGHT_FOOT = "pe_direito"
    BACK = "costas"


class VibrationPattern(Enum):
    """Padroes de vibracao com significados."""
    NONE = "nenhuma"
    SINGLE_TAP = "toque_unica"          # 1 vibracao curta
    DOUBLE_TAP = "toque_duplo"          # 2 vibracoes curtas
    TRIPLE_TAP = "toque_triplo"         # 3 vibracoes curtas
    LONG_BUZZ = "zumbido_longo"         # 1 vibracao longa
    PULSE = "pulsacao"                  # pulsacao ritmica
    ESCALATING = "crescente"            # comeca fraco, aumenta
    DESCENDING = "decrescente"          # comeca forte, diminui
    WAVE = "onda"                       # onda de um lado pro outro
    HEARTBEAT = "batimento"             # batimento cardíaco
    ALARM = "alarme"                    # vibracao continua forte
    MORSE_LIKE = "morse"                # codificacao tipo morse


class Direction(Enum):
    """Direcoes para navegacao."""
    FORWARD = "frente"
    BACKWARD = "tras"
    LEFT = "esquerda"
    RIGHT = "direita"
    STOP = "pare"
    SLIGHT_LEFT = "levemente_esquerda"
    SLIGHT_RIGHT = "levemente_direita"
    TURN_AROUND = "meia_volta"
    UP = "subir"
    DOWN = "descer"


class HazardLevel(Enum):
    """Nivel de perigo detectado."""
    CLEAR = "livre"
    INFO = "informacao"
    CAUTION = "atencao"
    WARNING = "aviso"
    DANGER = "perigo"
    CRITICAL = "critico"


# ============================================================================
# 2. MAPA DE VIBRACOES (Linguagem Haptica)
# ============================================================================

@dataclass
class HapticSignal:
    """Um sinal haptico com significado."""
    signal_id: str
    device: HapticDevice
    body_position: BodyPosition
    pattern: VibrationPattern
    duration_ms: int                    # duracao em milissegundos
    intensity: float                    # 0.0 (fraquinho) a 1.0 (maximo)
    meaning: str = ""                   # o que significa
    direction: Optional[Direction] = None
    hazard: HazardLevel = HazardLevel.CLEAR


# ============================================================================
# 3. Dicionario Haptico (Cada situacao = 1 vibracao)
# ============================================================================

HAPTIC_DICTIONARY: List[HapticSignal] = [
    # === DIRECOES ===
    HapticSignal("H-001", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.SINGLE_TAP, 200, 0.5,
                 meaning="Vire a esquerda", direction=Direction.LEFT),
    HapticSignal("H-002", HapticDevice.SMARTWATCH_RIGHT, BodyPosition.RIGHT_WRIST,
                 VibrationPattern.SINGLE_TAP, 200, 0.5,
                 meaning="Vire a direita", direction=Direction.RIGHT),
    HapticSignal("H-003", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.DOUBLE_TAP, 300, 0.6,
                 meaning="Continue reto", direction=Direction.FORWARD),
    HapticSignal("H-004", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.LONG_BUZZ, 800, 0.8,
                 meaning="Pare", direction=Direction.STOP),
    HapticSignal("H-005", HapticDevice.WAIST_BAND, BodyPosition.WAIST,
                 VibrationPattern.WAVE, 600, 0.5,
                 meaning="Meia volta", direction=Direction.TURN_AROUND),

    # === OBSTACULOS ===
    HapticSignal("H-010", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.ESCALATING, 1000, 0.7,
                 meaning="Obstaculo a esquerda se aproximando", hazard=HazardLevel.WARNING),
    HapticSignal("H-011", HapticDevice.SMARTWATCH_RIGHT, BodyPosition.RIGHT_WRIST,
                 VibrationPattern.ESCALATING, 1000, 0.7,
                 meaning="Obstaculo a direita se aproximando", hazard=HazardLevel.WARNING),
    HapticSignal("H-012", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.ALARM, 1500, 1.0,
                 meaning="OBSTACULO DIRETO A FRENTE! PERIGO!", hazard=HazardLevel.CRITICAL),
    HapticSignal("H-013", HapticDevice.ANKLE_LEFT, BodyPosition.LEFT_ANKLE,
                 VibrationPattern.SINGLE_TAP, 150, 0.4,
                 meaning="Buraco/degrau a esquerda do pe", hazard=HazardLevel.CAUTION),
    HapticSignal("H-014", HapticDevice.ANKLE_RIGHT, BodyPosition.RIGHT_ANKLE,
                 VibrationPattern.SINGLE_TAP, 150, 0.4,
                 meaning="Buraco/degrau a direita do pe", hazard=HazardLevel.CAUTION),

    # === SEMAFORO ===
    HapticSignal("H-020", HapticDevice.SMARTWATCH_RIGHT, BodyPosition.RIGHT_WRIST,
                 VibrationPattern.PULSE, 2000, 0.4,
                 meaning="Semaforo verde -- pode atravessar", hazard=HazardLevel.CLEAR),
    HapticSignal("H-021", HapticDevice.SMARTWATCH_RIGHT, BodyPosition.RIGHT_WRIST,
                 VibrationPattern.LONG_BUZZ, 1500, 0.8,
                 meaning="Semaforo vermelho -- PARE", hazard=HazardLevel.DANGER),
    HapticSignal("H-022", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.DOUBLE_TAP, 400, 0.5,
                 meaning="Semaforo amarelo -- atencao", hazard=HazardLevel.CAUTION),

    # === NAVEGACAO GPS ===
    HapticSignal("H-030", HapticDevice.RING_FINGER, BodyPosition.FINGER,
                 VibrationPattern.SINGLE_TAP, 100, 0.3,
                 meaning="Destino se aproximando (100m)"),
    HapticSignal("H-031", HapticDevice.RING_FINGER, BodyPosition.FINGER,
                 VibrationPattern.DOUBLE_TAP, 200, 0.4,
                 meaning="Destino se aproximando (50m)"),
    HapticSignal("H-032", HapticDevice.RING_FINGER, BodyPosition.FINGER,
                 VibrationPattern.HEARTBEAT, 600, 0.6,
                 meaning="Voce CHEGOU no destino!"),
    HapticSignal("H-033", HapticDevice.ANKLE_LEFT, BodyPosition.LEFT_ANKLE,
                 VibrationPattern.PULSE, 500, 0.3,
                 meaning="Rota recalculada -- vire a esquerda logo"),
    HapticSignal("H-034", HapticDevice.ANKLE_RIGHT, BodyPosition.RIGHT_ANKLE,
                 VibrationPattern.PULSE, 500, 0.3,
                 meaning="Rota recalculada -- vire a direita logo"),

    # === DISTANCIA (feedback continuo) ===
    HapticSignal("H-040", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.NONE, 0, 0.0,
                 meaning="Caminho livre (>5m)"),
    HapticSignal("H-041", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.PULSE, 500, 0.2,
                 meaning="Objeto a 3-5 metros"),
    HapticSignal("H-042", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.PULSE, 300, 0.4,
                 meaning="Objeto a 1-3 metros"),
    HapticSignal("H-043", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.ESCALATING, 200, 0.7,
                 meaning="Objeto a <1 metro! Atencao!"),

    # === PESSOAS ===
    HapticSignal("H-050", HapticDevice.NECKBAND, BodyPosition.NECK,
                 VibrationPattern.SINGLE_TAP, 200, 0.3,
                 meaning="Pessoa se aproximando por tras"),
    HapticSignal("H-051", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.DOUBLE_TAP, 300, 0.4,
                 meaning="Pessoa a frente vindo na sua direcao"),
    HapticSignal("H-052", HapticDevice.WAIST_BAND, BodyPosition.WAIST,
                 VibrationPattern.TRIPLE_TAP, 400, 0.5,
                 meaning="Grupo de pessoas a frente"),

    # === AMBIENTE ===
    HapticSignal("H-060", HapticDevice.INSOLE_LEFT, BodyPosition.LEFT_FOOT,
                 VibrationPattern.SINGLE_TAP, 100, 0.3,
                 meaning="Superficie irregular sob pe esquerdo"),
    HapticSignal("H-061", HapticDevice.INSOLE_RIGHT, BodyPosition.RIGHT_FOOT,
                 VibrationPattern.SINGLE_TAP, 100, 0.3,
                 meaning="Superficie irregular sob pe direito"),
    HapticSignal("H-062", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.DESCENDING, 600, 0.4,
                 meaning="Descendo ladeira"),
    HapticSignal("H-063", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.ESCALATING, 600, 0.4,
                 meaning="Subindo ladeira"),

    # === EMERGENCIA ===
    HapticSignal("H-090", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.ALARM, 3000, 1.0,
                 meaning="EMERGENCIA -- perigo iminente", hazard=HazardLevel.CRITICAL),
    HapticSignal("H-091", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.TRIPLE_TAP, 500, 0.9,
                 meaning="ALERTA -- veiculo se aproximando rapido", hazard=HazardLevel.DANGER),
]


# ============================================================================
# 4. MOTOR DE MAPEAMENTO AMBIENTAL
# ============================================================================

@dataclass
class EnvironmentScan:
    """Leitura do ambiente ao redor do usuario."""
    timestamp: float = field(default_factory=time.time)
    obstacles: List[Dict[str, Any]] = field(default_factory=list)  # {direction, distance, type}
    nearest_obstacle_m: float = 100.0
    nearest_obstacle_direction: str = ""
    path_clear: bool = True
    people_nearby: int = 0
    vehicles_nearby: int = 0
    surface_quality: str = "smooth"
    slope: str = "flat"
    traffic_light: Optional[str] = None
    crosswalk: bool = False
    gps_accuracy: float = 5.0
    distance_to_destination_m: float = 0.0


class EnvironmentMapper:
    """
    Mapeia o ambiente (camera + GPS + lidar) e gera EnvironmentScan.
    Em producao: integra dados de OpenBodyCamera + GPS + sensores.
    """

    def __init__(self):
        self.scans_history: deque = deque(maxlen=200)
        self.last_scan: Optional[EnvironmentScan] = None

    def scan(self) -> EnvironmentScan:
        """Escaneia o ambiente (simulado)."""
        scan = EnvironmentScan(
            obstacles=[
                {"direction": "frente", "distance_m": 8.0, "type": "pessoa"},
                {"direction": "esquerda", "distance_m": 3.0, "type": "poste"},
                {"direction": "direita", "distance_m": 5.0, "type": "carro_estacionado"},
            ],
            nearest_obstacle_m=3.0,
            nearest_obstacle_direction="esquerda",
            path_clear=True,
            people_nearby=1,
            vehicles_nearby=1,
            surface_quality="smooth",
            slope="flat",
            traffic_light="verde",
            crosswalk=False,
            distance_to_destination_m=50.0,
        )
        self.last_scan = scan
        self.scans_history.append(scan)
        return scan

    def scan_with_obstacle(self, direction: str = "frente", distance: float = 1.5,
                           obstacle_type: str = "buraco") -> EnvironmentScan:
        """Simula cenario com obstaculo."""
        scan = EnvironmentScan(
            obstacles=[{"direction": direction, "distance_m": distance, "type": obstacle_type}],
            nearest_obstacle_m=distance,
            nearest_obstacle_direction=direction,
            path_clear=distance > 2.0,
        )
        self.last_scan = scan
        self.scans_history.append(scan)
        return scan

    def scan_traffic_light(self, color: str) -> EnvironmentScan:
        """Simula cenario de semaforo."""
        scan = EnvironmentScan(
            obstacles=[],
            nearest_obstacle_m=10.0,
            path_clear=color == "verde",
            traffic_light=color,
            crosswalk=True,
            distance_to_destination_m=30.0,
        )
        self.last_scan = scan
        self.scans_history.append(scan)
        return scan


# ============================================================================
# 5. TRADUTOR AMBIENTE -> VIBRACAO
# ============================================================================

class HapticTranslator:
    """
    Traduz EnvironmentScan em sinais hapticos.
    Decide QUAIS dispositivos vibrar, COMO e QUANDO.
    """

    def __init__(self, active_devices: List[HapticDevice] = None):
        self.active_devices = active_devices or [HapticDevice.SMARTWATCH_LEFT, HapticDevice.SMARTWATCH_RIGHT]
        self.dictionary = {s.signal_id: s for s in HAPTIC_DICTIONARY}
        self.last_signals: deque = deque(maxlen=50)
        self.min_interval_s: float = 0.8  # intervalo minimo entre sinais
        self.last_signal_time: float = 0

    def translate(self, scan: EnvironmentScan) -> List[HapticSignal]:
        """Traduz scan do ambiente em lista de sinais hapticos."""
        signals = []

        # 1. Obstaculos
        for obs in scan.obstacles:
            signal = self._obstacle_to_signal(obs)
            if signal:
                signals.append(signal)

        # 2. Semaforo
        if scan.traffic_light:
            signal = self._traffic_light_to_signal(scan.traffic_light)
            if signal:
                signals.append(signal)

        # 3. Destino se aproximando
        if scan.distance_to_destination_m > 0:
            signal = self._distance_to_signal(scan.distance_to_destination_m)
            if signal:
                signals.append(signal)

        # 4. Superficie
        if scan.surface_quality != "smooth":
            signal = self._surface_to_signal(scan.surface_quality)
            if signal:
                signals.append(signal)

        # 5. Inclinacao
        if scan.slope != "flat":
            signal = self._slope_to_signal(scan.slope)
            if signal:
                signals.append(signal)

        # Filtrar por dispositivos ativos
        signals = [s for s in signals if s.device in self.active_devices]

        # Dedup e rate limiting
        now = time.time()
        if now - self.last_signal_time < self.min_interval_s:
            # So passar criticos
            signals = [s for s in signals if s.hazard in (HazardLevel.DANGER, HazardLevel.CRITICAL)]

        if signals:
            self.last_signal_time = now
            for s in signals:
                self.last_signals.append(s)

        return signals

    def _obstacle_to_signal(self, obstacle: Dict[str, Any]) -> Optional[HapticSignal]:
        """Converte obstaculo em sinal haptico."""
        distance = obstacle.get("distance_m", 100)
        direction = obstacle.get("direction", "frente")

        if distance < 1.0:
            # CRITICO
            return self.dictionary.get("H-012")  # ALARM peito
        elif distance < 2.0:
            # Perigo
            if direction == "esquerda":
                return self.dictionary.get("H-010")
            elif direction == "direita":
                return self.dictionary.get("H-011")
            else:
                return self.dictionary.get("H-012")
        elif distance < 4.0:
            # Atencao
            if direction == "esquerda":
                return self.dictionary.get("H-010")
            elif direction == "direita":
                return self.dictionary.get("H-011")
        return None

    def _traffic_light_to_signal(self, color: str) -> Optional[HapticSignal]:
        if color == "verde":
            return self.dictionary.get("H-020")
        elif color == "vermelho":
            return self.dictionary.get("H-021")
        elif color == "amarelo":
            return self.dictionary.get("H-022")
        return None

    def _distance_to_signal(self, distance_m: float) -> Optional[HapticSignal]:
        if distance_m <= 5:
            return self.dictionary.get("H-032")  # CHEGOU
        elif distance_m <= 50:
            return self.dictionary.get("H-031")  # 50m
        elif distance_m <= 100:
            return self.dictionary.get("H-030")  # 100m
        return None

    def _surface_to_signal(self, quality: str) -> Optional[HapticSignal]:
        if quality == "irregular_left":
            return self.dictionary.get("H-060")
        elif quality == "irregular_right":
            return self.dictionary.get("H-061")
        return None

    def _slope_to_signal(self, slope: str) -> Optional[HapticSignal]:
        if slope == "downhill":
            return self.dictionary.get("H-062")
        elif slope == "uphill":
            return self.dictionary.get("H-063")
        return None

    def signal_to_direction(self, direction: Direction) -> Optional[HapticSignal]:
        """Converte direcao de navegacao em sinal haptico."""
        mapping = {
            Direction.LEFT: "H-001",
            Direction.RIGHT: "H-002",
            Direction.FORWARD: "H-003",
            Direction.STOP: "H-004",
            Direction.TURN_AROUND: "H-005",
        }
        sig_id = mapping.get(direction)
        return self.dictionary.get(sig_id) if sig_id else None


# ============================================================================
# 6. GERENCIADOR DE DISPOSITIVOS HAPTICOS
# ============================================================================

class HapticDeviceManager:
    """
    Gerencia dispositivos hapticos fisicos.
    Conecta, desconecta, envia vibracoes, monitora bateria.
    """

    def __init__(self):
        self.connected: Dict[HapticDevice, Dict] = {}
        self.signal_history: deque = deque(maxlen=500)

    def connect(self, device: HapticDevice, battery_pct: float = 100.0) -> str:
        """Conecta um dispositivo haptico."""
        self.connected[device] = {
            "battery_pct": battery_pct,
            "online": True,
            "signals_sent": 0,
            "last_active": time.time(),
        }
        return f"{device.value} conectado. Bateria: {battery_pct:.0f}%."

    def disconnect(self, device: HapticDevice) -> str:
        if device in self.connected:
            del self.connected[device]
            return f"{device.value} desconectado."
        return f"{device.value} nao estava conectado."

    def send_signal(self, signal: HapticSignal) -> Dict[str, Any]:
        """Envia um sinal haptico para o dispositivo."""
        if signal.device not in self.connected:
            return {"sent": False, "reason": "dispositivo nao conectado"}

        dev = self.connected[signal.device]
        if not dev["online"]:
            return {"sent": False, "reason": "dispositivo offline"}

        dev["signals_sent"] += 1
        dev["last_active"] = time.time()

        record = {
            "device": signal.device.value,
            "pattern": signal.pattern.value,
            "intensity": signal.intensity,
            "duration_ms": signal.duration_ms,
            "meaning": signal.meaning,
            "timestamp": time.time(),
            "sent": True,
        }
        self.signal_history.append(record)
        return record

    def send_signals(self, signals: List[HapticSignal]) -> List[Dict[str, Any]]:
        """Envia multiplos sinais."""
        return [self.send_signal(s) for s in signals]

    def status(self) -> Dict[str, Any]:
        return {
            "connected_devices": len(self.connected),
            "devices": {d.value: info for d, info in self.connected.items()},
            "total_signals_sent": sum(d["signals_sent"] for d in self.connected.values()),
        }


# ============================================================================
# 7. CONTROLADOR PRINCIPAL
# ============================================================================

class HapticNavigationController:
    """
    Orquestra mapeamento ambiental + traducao haptica + dispositivos.
    O usuario sente vibracoes e navega sem voz, sem fone, sem tela.

    Uso:
        nav = HapticNavigationController()
        nav.connect_device(HapticDevice.SMARTWATCH_LEFT)
        nav.connect_device(HapticDevice.SMARTWATCH_RIGHT)
        nav.start()
        # Sistema escaneia ambiente e vibra automaticamente
        nav.navigate_to("padaria")
    """

    def __init__(self, devices: List[HapticDevice] = None):
        self.mapper = EnvironmentMapper()
        self.translator = HapticTranslator(devices or [])
        self.device_manager = HapticDeviceManager()
        self.active: bool = False
        self.destination: str = ""
        self.scan_interval_s: float = 0.5  # escaneia a cada 500ms
        self.last_scan_time: float = 0
        self.total_scans: int = 0
        self.total_signals: int = 0
        self.session_start: float = 0

    def connect_device(self, device: HapticDevice, battery: float = 100) -> str:
        """Conecta dispositivo haptico."""
        return self.device_manager.connect(device, battery)

    def start(self) -> Dict[str, Any]:
        """Inicia navegacao haptica."""
        self.active = True
        self.session_start = time.time()
        return {
            "active": True,
            "devices": list(self.device_manager.connected.keys()),
            "device_count": len(self.device_manager.connected),
            "message": "Navegacao haptica ativa. Sinta as vibracoes.",
        }

    def stop(self) -> Dict[str, Any]:
        self.active = False
        duration = time.time() - self.session_start if self.session_start else 0
        return {
            "active": False,
            "duration_min": duration / 60,
            "total_scans": self.total_scans,
            "total_signals": self.total_signals,
        }

    def navigate_to(self, destination: str) -> str:
        self.destination = destination
        return f"Navegando para {destination}. Siga as vibracoes."

    def turn(self, direction: Direction) -> Dict[str, Any]:
        """Emite sinal de direcao."""
        signal = self.translator.signal_to_direction(direction)
        if signal and signal.device in self.device_manager.connected:
            result = self.device_manager.send_signal(signal)
            self.total_signals += 1
            return result
        return {"sent": False, "reason": "sem dispositivo para esta direcao"}

    def scan_and_vibrate(self) -> List[Dict[str, Any]]:
        """Escaneia ambiente e envia vibracoes automaticamente."""
        if not self.active:
            return []

        scan = self.mapper.scan()
        self.total_scans += 1

        signals = self.translator.translate(scan)
        results = self.device_manager.send_signals(signals)
        self.total_signals += len(signals)

        return results

    def alert_obstacle(self, direction: str = "frente", distance: float = 1.5,
                       obstacle_type: str = "buraco") -> Dict[str, Any]:
        """Alerta sobre obstaculo especifico."""
        scan = self.mapper.scan_with_obstacle(direction, distance, obstacle_type)
        signals = self.translator.translate(scan)
        if signals:
            result = self.device_manager.send_signal(signals[0])
            self.total_signals += 1
            return result
        return {"sent": False, "reason": "sem sinal para este obstaculo"}

    def alert_traffic_light(self, color: str) -> Dict[str, Any]:
        """Alerta sobre semaforo."""
        scan = self.mapper.scan_traffic_light(color)
        signals = self.translator.translate(scan)
        if signals:
            results = []
            for s in signals:
                if s.device in self.device_manager.connected:
                    r = self.device_manager.send_signal(s)
                    results.append(r)
                    self.total_signals += 1
            return {"signals": results, "color": color}
        return {"sent": False}

    def alert_arrival(self) -> Dict[str, Any]:
        """Emite sinal de chegada ao destino."""
        signal = self.translator.dictionary.get("H-032")
        if signal and signal.device in self.device_manager.connected:
            return self.device_manager.send_signal(signal)
        return {"sent": False}

    def alert_emergency(self) -> Dict[str, Any]:
        """Emite sinal de emergencia em todos os dispositivos."""
        signal = self.translator.dictionary.get("H-090")
        results = []
        for device in self.device_manager.connected:
            sig = HapticSignal(
                signal_id="EMERG",
                device=device,
                body_position=BodyPosition.CHEST,
                pattern=VibrationPattern.ALARM,
                duration_ms=3000,
                intensity=1.0,
                meaning="EMERGENCIA",
                hazard=HazardLevel.CRITICAL,
            )
            r = self.device_manager.send_signal(sig)
            results.append(r)
            self.total_signals += 1
        return {"emergency": True, "signals_sent": len(results)}

    def status(self) -> Dict[str, Any]:
        return {
            "active": self.active,
            "destination": self.destination,
            "devices": self.device_manager.status(),
            "total_scans": self.total_scans,
            "total_signals": self.total_signals,
            "dictionary_size": len(HAPTIC_DICTIONARY),
        }


# ============================================================================
# 8. CENARIOS DO MUNDO REAL
# ============================================================================

def scenario_walking_with_haptics():
    """Cenario: cego andando guiado por vibracoes."""
    print("=" * 65)
    print("CENARIO 1: Cego andando guiado por vibracoes")
    print("=" * 65)

    nav = HapticNavigationController()
    nav.connect_device(HapticDevice.SMARTWATCH_LEFT)
    nav.connect_device(HapticDevice.SMARTWATCH_RIGHT)
    nav.connect_device(HapticDevice.CHEST_VEST)

    start = nav.start()
    print(f"\n{start['message']}")
    print(f"Dispositivos: {start['device_count']}")

    # Escanear ambiente
    print(f"\n[Escaneando ambiente...]")
    results = nav.scan_and_vibrate()
    for r in results:
        if r.get("sent"):
            print(f"  -> {r['device']}: {r['pattern']} ({r['meaning']})")

    # Virar a esquerda
    print(f"\n[Instrucao: vire a esquerda]")
    result = nav.turn(Direction.LEFT)
    if result.get("sent"):
        print(f"  -> {result['device']}: {result['meaning']}")

    # Obstaaculo
    print(f"\n[Obstaculo detectado!]")
    result = nav.alert_obstacle("frente", 1.0, "poste")
    if result.get("sent"):
        print(f"  -> {result['device']}: {result['pattern']} | {result['meaning']}")


def scenario_crossing_with_haptics():
    """Cenario: atravessando rua com semaforo haptico."""
    print(f"\n{'=' * 65}")
    print("CENARIO 2: Atravessando rua -- semaforo por vibracao")
    print("=" * 65)

    nav = HapticNavigationController()
    nav.connect_device(HapticDevice.SMARTWATCH_RIGHT)
    nav.start()

    print(f"\n[Semaforo VERMELHO]")
    result = nav.alert_traffic_light("vermelho")
    for s in result.get("signals", []):
        if s.get("sent"):
            print(f"  -> {s['device']}: {s['pattern']} | {s['meaning']}")

    print(f"\n[Semaforo VERDE]")
    result = nav.alert_traffic_light("verde")
    for s in result.get("signals", []):
        if s.get("sent"):
            print(f"  -> {s['device']}: {s['pattern']} | {s['meaning']}")


def scenario_arriving_destination():
    """Cenario: chegando no destino."""
    print(f"\n{'=' * 65}")
    print("CENARIO 3: Chegando no destino")
    print("=" * 65)

    nav = HapticNavigationController()
    nav.connect_device(HapticDevice.RING_FINGER)
    nav.start()
    nav.navigate_to("casa")

    print(f"\n[100 metros do destino]")
    result = nav.alert_arrival()
    print(f"  -> {result.get('meaning', 'sem sinal')}")

    print(f"\n[Chegou!]")
    result = nav.alert_arrival()
    if result.get("sent"):
        print(f"  -> {result['device']}: {result['pattern']} | {result['meaning']}")


def scenario_emergency_haptic():
    """Cenario: emergencia -- todos os dispositivos vibram."""
    print(f"\n{'=' * 65}")
    print("CENARIO 4: Emergencia haptica")
    print("=" * 65)

    nav = HapticNavigationController()
    nav.connect_device(HapticDevice.SMARTWATCH_LEFT)
    nav.connect_device(HapticDevice.SMARTWATCH_RIGHT)
    nav.connect_device(HapticDevice.CHEST_VEST)
    nav.start()

    print(f"\n[EMERGENCIA!]")
    result = nav.alert_emergency()
    print(f"  Sinais enviados: {result.get('signals_sent', 0)}")
    print(f"  Todos os dispositivos vibrando em ALARME.")


def scenario_full_body_haptic():
    """Cenario: sistema completo body-haptic."""
    print(f"\n{'=' * 65}")
    print("CENARIO 5: Sistema completo (7 dispositivos)")
    print("=" * 65)

    nav = HapticNavigationController()
    # Conectar 7 dispositivos
    for dev in [HapticDevice.SMARTWATCH_LEFT, HapticDevice.SMARTWATCH_RIGHT,
                HapticDevice.CHEST_VEST, HapticDevice.ANKLE_LEFT,
                HapticDevice.ANKLE_RIGHT, HapticDevice.RING_FINGER,
                HapticDevice.WAIST_BAND]:
        nav.connect_device(dev)

    start = nav.start()
    print(f"\n{start['message']}")
    print(f"Dispositivos conectados: {start['device_count']}")

    # Escanear e vibrar
    print(f"\n[Escaneando e vibrando...]")
    results = nav.scan_and_vibrate()
    for r in results:
        if r.get("sent"):
            print(f"  -> {r['device']}: {r['pattern']} ({r['meaning']})")

    status = nav.status()
    print(f"\nTotal sinais enviados: {status['total_signals']}")


# ============================================================================
# 9. ANDROID HAPTICFEEDBACK V2 (2024/2025)
# ============================================================================

"""
Android HapticFeedbackConstants V2 (API 30+ Composition APIs)
-------------------------------------------------------------
- EFFECT_CLICK, EFFECT_HEAVY_CLICK, EFFECT_TICK, EFFECT_DOUBLE_CLICK
- Composition primitives: PRIMITIVE_CLICK, PRIMITIVE_TICK, PRIMITIVE_LOW_TICK,
  PRIMITIVE_SPIN, PRIMITIVE_THUD, PRIMITIVE_QUICK_FALL, PRIMITIVE_QUICK_RISE
- Requires: VibratorManager + VibrationEffect.createComposition()
- Supported on Pixel 7+, Galaxy S23+, OnePlus 11+ (2024-2025 flagships)
"""

ANDROID_HAPTIC_V2 = {
    "PRIMITIVE_CLICK": {"amplitude": 1.0, "duration_ms": 20, "intensity": 0.8},
    "PRIMITIVE_TICK": {"amplitude": 0.6, "duration_ms": 10, "intensity": 0.5},
    "PRIMITIVE_LOW_TICK": {"amplitude": 0.4, "duration_ms": 15, "intensity": 0.3},
    "PRIMITIVE_SPIN": {"amplitude": 0.9, "duration_ms": 40, "intensity": 0.7},
    "PRIMITIVE_THUD": {"amplitude": 1.0, "duration_ms": 60, "intensity": 1.0},
    "PRIMITIVE_QUICK_FALL": {"amplitude": 0.7, "duration_ms": 25, "intensity": 0.6},
    "PRIMITIVE_QUICK_RISE": {"amplitude": 0.8, "duration_ms": 30, "intensity": 0.65},
}

# ============================================================================
# 10. HARDWARE HAPTIC COSTS 2024/2025 (LRA actuators)
# ============================================================================

HAPTIC_HARDWARE_PRICES_USD_2025 = {
    "LRA_ERM_6mm": 0.85,      # generic coin LRA (smartwatch)
    "LRA_8mm_high_amp": 1.45, # high-amplitude for vest/ankle
    "LRA_10mm": 2.10,         # waist-band / chest vest
    "LRA_12mm": 3.25,         # professional-grade (colete)
    "DRV2605L_driver": 1.20,  # TI haptic driver IC
    "DRV2625_driver": 2.80,   # advanced closed-loop driver
}

# ============================================================================
# 11. DEMONSTRACAO
# ============================================================================

def demo():
    print("=" * 70)
    print("OpenHapticNavigation -- Navegacao por Vibracao para Cegos")
    print("=" * 70)

    print(f"\nDispositivos hapticos: {len(HapticDevice)}")
    print(f"Posicoes do corpo: {len(BodyPosition)}")
    print(f"Padroes de vibracao: {len(VibrationPattern)}")
    print(f"Direcoes: {len(Direction)}")
    print(f"Niveis de perigo: {len(HazardLevel)}")
    print(f"Sinais no dicionario: {len(HAPTIC_DICTIONARY)}")

    # Cenarios
    scenario_walking_with_haptics()
    scenario_crossing_with_haptics()
    scenario_arriving_destination()
    scenario_emergency_haptic()
    scenario_full_body_haptic()

    # Resumo do dicionario
    print(f"\n{'=' * 70}")
    print("DICIONARIO HAPTICO COMPLETO")
    print(f"{'=' * 70}")
    for s in HAPTIC_DICTIONARY:
        hazard_marker = ""
        if s.hazard == HazardLevel.CRITICAL:
            hazard_marker = " [CRITICO]"
        elif s.hazard == HazardLevel.DANGER:
            hazard_marker = " [PERIGO]"
        elif s.hazard == HazardLevel.WARNING:
            hazard_marker = " [ATENCAO]"
        print(f"  {s.signal_id}: {s.meaning}{hazard_marker}")
        print(f"    Dispositivo: {s.device.value} | Padrao: {s.pattern.value} "
              f"| Intensidade: {s.intensity:.1f} | Duracao: {s.duration_ms}ms")

    print(f"\n{'=' * 70}")
    print("RESUMO")
    print(f"{'=' * 70}")
    print()
    print("  SEM FONE. SEM VOZ. SEM CHAMAR ATENCAO.")
    print("  Discreto. Silencioso. Instintivo.")
    print()
    print("  O cego ANDA sentindo vibracoes.")
    print("  O corpo ENTENDE. Como um sexto sentido.")
    print()
    print("  Integrado com:")
    print("    OpenBodyCamera (mapeia ambiente)")
    print("    OpenTelefonista (fala so quando necessario)")
    print("    OpenResilience (bateria dos dispositivos)")
    print("    OpenHumanNet (emergencia)")


if __name__ == "__main__":
    demo()
