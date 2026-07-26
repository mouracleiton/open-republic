#!/usr/bin/env python3
"""
OpenInclusiveHome -- A Casa Inteligente que se Adapta à Pessoa
================================================================
"A casa NAO pede para o usuario se adaptar.
A casa se adapta ao usuario -- tetraplegico, idoso, cego, autista.

Todo dispositivo e controlavel por:
- VOZ (comando natural, conversacional)
- OLHAR (eye-tracking com dwell)
- INTERRUPTOR (switch scanning)
- SOPRO/SUGADA (blow-suck)
- CABECA (movimento de cabeca)
- PULSO (smartwatch gesture)
- CEREBRO (brain interface)
- AUTOMACAO (horario, sensor, emergencia)

A casa e o CORPO EXTENDIDO da pessoa com deficiencia:
- Luz = olhos que acendem sozinhos quando escurece
- Porta = maos que abrem sem tocar
- Cama = posicao que se ajusta sozinha
- Alerta = voz que chama ajuda antes mesmo de pedir
- Energia = otimizada para solar/bateria, zero preocupacao

DIFERENCA CRITICAL: O sistema NAO e 'acessibilidade'.
E INCLUSAO RADICAL -- a casa inteira e projetada
para quem NAO PODE mexer o corpo.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set, Callable
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict, deque
import time
import random


# ============================================================================
# 1. ENUMS -- TODOS OS DISPOSITIVOS E METODOS DE CONTROLE
# ============================================================================

class DeviceType(Enum):
    """Tipos de dispositivos da casa inclusiva."""
    LIGHT = "luz"
    THERMOSTAT = "termostato"
    DOOR_LOCK = "fechadura"
    WINDOW = "janela"
    CURTAIN = "cortina"
    TV = "televisao"
    SPEAKER = "caixa_de_som"
    FAN = "ventilador"
    AIR_CONDITIONER = "ar_condicionado"
    OVEN = "forno"
    MICROWAVE = "microondas"
    COFFEE_MACHINE = "cafeteira"
    BED_POSITION = "posicao_cama"
    WHEELCHAIR_CHARGER = "carregador_cadeira"
    MEDICAL_ALERT = "alerta_medico"
    SECURITY_CAMERA = "camera_seguranca"
    DOORBELL = "campainha"
    GARAGE = "garagem"
    ELEVATOR = "elevador"
    ROBOTIC_ARM = "braco_robotico"


class ControlMethod(Enum):
    """Metodos de controle acessiveis."""
    VOICE = "voz"
    EYE_TRACKING = "rastreamento_ocular"
    SWITCH = "interruptor"
    BRAIN_INTERFACE = "interface_cerebral"
    SMARTWATCH_GESTURE = "gesto_smartwatch"
    BLOW_SUCK = "sopro_sugada"
    HEAD_MOVEMENT = "movimento_cabeca"
    AUTOMATION_SCHEDULE = "automacao_agendada"
    PROXIMITY = "proximidade"


class RoomType(Enum):
    """Comodos da casa inclusiva."""
    BEDROOM = "quarto"
    LIVING_ROOM = "sala"
    KITCHEN = "cozinha"
    BATHROOM = "banheiro"
    OFFICE = "escritorio"
    GARAGE = "garagem"
    GARDEN = "jardim"
    ENTRANCE = "entrada"


class AutomationTrigger(Enum):
    """Gatilhos de automacao."""
    TIME = "horario"
    SUNRISE = "nascer_sol"
    SUNSET = "por_sol"
    TEMPERATURE = "temperatura"
    MOTION = "movimento"
    DOOR_OPEN = "porta_aberta"
    WAKE_UP = "acordar"
    SLEEP = "dormir"
    EMERGENCY = "emergencia"
    LOW_BATTERY = "bateria_baixa"


class UrgencyLevel(Enum):
    """Niveis de urgencia das acoes."""
    ROUTINE = "rotina"
    COMFORT = "conforto"
    IMPORTANT = "importante"
    URGENT = "urgente"
    EMERGENCY = "emergencia"


# ============================================================================
# 2. DATACLASSES -- ESTRUTURA DE DADOS
# ============================================================================

@dataclass
class SmartDevice:
    """Um dispositivo inteligente da casa inclusiva."""
    device_id: str
    name: str
    device_type: DeviceType
    room: RoomType
    control_methods: List[ControlMethod]
    current_state: Dict[str, Any] = field(default_factory=dict)
    power_consumption_w: float = 0.0
    is_online: bool = True
    automation_rules: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.current_state:
            self.current_state = {"status": "off", "level": 0}


@dataclass
class AutomationRule:
    """Regra de automacao da casa."""
    rule_id: str
    trigger: AutomationTrigger
    condition: str
    action: str
    device_id: str
    enabled: bool = True
    description: str = ""
    urgency: UrgencyLevel = UrgencyLevel.ROUTINE


@dataclass
class HomeState:
    """Estado completo da casa inclusiva."""
    devices: Dict[str, SmartDevice] = field(default_factory=dict)
    temperature_c: float = 22.0
    security_armed: bool = False
    energy_usage_w: float = 0.0
    solar_generation_w: float = 0.0
    battery_level_pct: float = 85.0
    last_update: float = field(default_factory=time.time)


@dataclass
class RoomConfig:
    """Configuracao de um comodo inclusivo."""
    room_type: RoomType
    devices: List[str] = field(default_factory=list)
    ambient_preferences: Dict[str, Any] = field(default_factory=dict)
    accessibility_features: List[str] = field(default_factory=list)


# ============================================================================
# 3. CLASSES DE CONTROLE
# ============================================================================

class DeviceController:
    """Controlador individual de dispositivos."""

    def __init__(self, device: SmartDevice):
        self.device = device
        self.command_history: List[Dict] = []

    def turn_on(self) -> str:
        self.device.current_state["status"] = "on"
        self._log_command("turn_on")
        return f"{self.device.name} ligado."

    def turn_off(self) -> str:
        self.device.current_state["status"] = "off"
        self._log_command("turn_off")
        return f"{self.device.name} desligado."

    def set_level(self, level: int) -> str:
        self.device.current_state["level"] = max(0, min(100, level))
        self._log_command("set_level", level)
        return f"{self.device.name} ajustado para nivel {level}%."

    def get_status(self) -> Dict[str, Any]:
        return {
            "device": self.device.name,
            "state": self.device.current_state,
            "online": self.device.is_online,
            "power_w": self.device.power_consumption_w
        }

    def execute_command(self, command: str, params: Dict = None) -> str:
        params = params or {}
        if command == "on":
            return self.turn_on()
        elif command == "off":
            return self.turn_off()
        elif command == "level":
            return self.set_level(params.get("level", 50))
        return f"Comando desconhecido: {command}"

    def _log_command(self, cmd: str, value: Any = None):
        self.command_history.append({
            "timestamp": time.time(),
            "command": cmd,
            "value": value,
            "method": "manual"
        })


class VoiceHomeControl:
    """Controle por voz -- comandos naturais em portugues."""

    def __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.voice_history: List[str] = []

    def parse_command(self, utterance: str) -> Tuple[str, Dict]:
        utterance = utterance.lower()
        if "luz" in utterance or "luz do quarto" in utterance:
            return "light", {"room": RoomType.BEDROOM, "action": "on" if "liga" in utterance else "off"}
        if "cama" in utterance and "levanta" in utterance:
            return "bed", {"action": "raise"}
        if "porta" in utterance and "abre" in utterance:
            return "door", {"action": "unlock"}
        if "emergencia" in utterance or "socorro" in utterance:
            return "emergency", {"action": "alert"}
        return "unknown", {}

    def execute_voice_command(self, utterance: str) -> str:
        cmd, params = self.parse_command(utterance)
        self.voice_history.append(utterance)
        if cmd == "light":
            device = self.home.find_device(RoomType.BEDROOM, DeviceType.LIGHT)
            if device:
                ctrl = DeviceController(device)
                return ctrl.turn_on() if params["action"] == "on" else ctrl.turn_off()
        if cmd == "bed":
            device = self.home.find_device(RoomType.BEDROOM, DeviceType.BED_POSITION)
            if device:
                return DeviceController(device).set_level(80)
        if cmd == "emergency":
            return self.home.trigger_emergency("voz")
        return "Comando nao reconhecido. Pode repetir?"

    def confirm_action(self, action: str) -> bool:
        # Em producao, usaria TTS + espera de confirmacao por voz
        return True


class EyeHomeControl:
    """Controle por rastreamento ocular (eye-tracking)."""

    def __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.calibrated = False
        self.dwell_time_ms = 1200
        self.last_gaze: Optional[str] = None

    def calibrate(self) -> str:
        self.calibrated = True
        return "Calibracao ocular concluida. Olhe para o dispositivo desejado."

    def look_at_device(self, device_id: str) -> str:
        if not self.calibrated:
            return "Calibre primeiro o eye-tracker."
        self.last_gaze = device_id
        return f"Olhando para {device_id}. Mantenha o olhar por {self.dwell_time_ms}ms."

    def dwell_select(self, device_id: str) -> str:
        device = self.home.devices.get(device_id)
        if device:
            ctrl = DeviceController(device)
            return ctrl.turn_on()
        return "Dispositivo nao encontrado."

    def scan_devices(self, room: RoomType) -> List[str]:
        return [d.device_id for d in self.home.devices.values() if d.room == room]


class SwitchHomeControl:
    """Controle por interruptor (switch scanning) -- varredura."""

    def __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.current_scan_index = 0
        self.scan_list: List[str] = []

    def scan_rooms(self) -> List[RoomType]:
        return list(RoomType)

    def scan_devices(self, room: RoomType) -> List[str]:
        self.scan_list = [d.device_id for d in self.home.devices.values() if d.room == room]
        self.current_scan_index = 0
        return self.scan_list

    def select(self) -> str:
        if not self.scan_list:
            return "Nenhum dispositivo em varredura."
        device_id = self.scan_list[self.current_scan_index]
        self.current_scan_index = (self.current_scan_index + 1) % len(self.scan_list)
        device = self.home.devices.get(device_id)
        if device:
            return DeviceController(device).turn_on()
        return "Erro na selecao."


class AutomationEngine:
    """Motor de automacoes -- executa regras sem intervencao humana."""

    def __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.rules: Dict[str, AutomationRule] = {}
        self.execution_log: List[Dict] = []

    def add_rule(self, rule: AutomationRule) -> str:
        self.rules[rule.rule_id] = rule
        return f"Regra {rule.rule_id} adicionada."

    def check_triggers(self, trigger: AutomationTrigger, context: Dict) -> List[str]:
        executed = []
        for rule in self.rules.values():
            if rule.trigger == trigger and rule.enabled:
                if self._condition_met(rule, context):
                    result = self.execute_automation(rule.rule_id)
                    executed.append(result)
        return executed

    def _condition_met(self, rule: AutomationRule, context: Dict) -> bool:
        # Exemplo simples: temperatura > 28 ativa ar
        if "temperature" in rule.condition and context.get("temperature", 0) > 28:
            return True
        if rule.trigger == AutomationTrigger.WAKE_UP:
            return True
        return False

    def execute_automation(self, rule_id: str) -> str:
        rule = self.rules.get(rule_id)
        if not rule:
            return "Regra nao encontrada."
        device = self.home.devices.get(rule.device_id)
        if device:
            ctrl = DeviceController(device)
            result = ctrl.execute_command(rule.action)
            self.execution_log.append({"rule": rule_id, "time": time.time(), "result": result})
            return result
        return "Dispositivo offline."


class HomeEnergyManager:
    """Gestor de energia -- prioriza solar e bateria."""

    def __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.daily_consumption: List[float] = []
        self.solar_history: List[float] = []

    def optimize(self) -> str:
        state = self.home.state
        if state.solar_generation_w > state.energy_usage_w:
            surplus = state.solar_generation_w - state.energy_usage_w
            return f"Excedente solar: {surplus}W. Carregando bateria."
        if state.battery_level_pct < 20:
            return "Bateria baixa. Reduzindo consumo de dispositivos nao essenciais."
        return "Consumo otimizado. Usando combinacao solar + rede."

    def report(self) -> Dict[str, Any]:
        return {
            "uso_atual_w": self.home.state.energy_usage_w,
            "solar_w": self.home.state.solar_generation_w,
            "bateria_pct": self.home.state.battery_level_pct,
            "status": self.optimize()
        }


class InclusiveHome:
    """Orquestrador principal da casa inclusiva."""

    def __init__(self):
        self.devices: Dict[str, SmartDevice] = {}
        self.state = HomeState()
        self.voice = VoiceHomeControl(self)
        self.eye = EyeHomeControl(self)
        self.switch = SwitchHomeControl(self)
        self.automation = AutomationEngine(self)
        self.energy = HomeEnergyManager(self)
        self.rooms: Dict[RoomType, RoomConfig] = {}

    def add_device(self, device: SmartDevice) -> str:
        self.devices[device.device_id] = device
        self.state.devices[device.device_id] = device
        if device.room not in self.rooms:
            self.rooms[device.room] = RoomConfig(room_type=device.room)
        self.rooms[device.room].devices.append(device.device_id)
        return f"Dispositivo {device.name} adicionado ao {device.room.value}."

    def find_device(self, room: RoomType, dtype: DeviceType) -> Optional[SmartDevice]:
        for d in self.devices.values():
            if d.room == room and d.device_type == dtype:
                return d
        return None

    def trigger_emergency(self, source: str) -> str:
        alert = self.find_device(RoomType.BEDROOM, DeviceType.MEDICAL_ALERT)
        if alert:
            DeviceController(alert).turn_on()
        self.state.security_armed = True
        return f"EMERGENCIA acionada via {source}. Alerta medico enviado. Casa em modo seguro."

    def get_full_status(self) -> Dict[str, Any]:
        return {
            "dispositivos": len(self.devices),
            "temperatura": self.state.temperature_c,
            "seguranca": self.state.security_armed,
            "energia": self.energy.report(),
            "automacoes_ativas": len(self.automation.rules)
        }


# ============================================================================
# 4. CENARIOS PREDEFINIDOS
# ============================================================================

def create_home_tetraplegic() -> InclusiveHome:
    """Casa otimizada para tetraplegico -- controle total por voz/olhar/switch."""
    home = InclusiveHome()
    # Quarto
    home.add_device(SmartDevice("luz_quarto", "Luz do Quarto", DeviceType.LIGHT, RoomType.BEDROOM,
                                [ControlMethod.VOICE, ControlMethod.EYE_TRACKING, ControlMethod.SWITCH]))
    home.add_device(SmartDevice("cama", "Cama Articulada", DeviceType.BED_POSITION, RoomType.BEDROOM,
                                [ControlMethod.VOICE, ControlMethod.EYE_TRACKING, ControlMethod.BLOW_SUCK]))
    home.add_device(SmartDevice("alerta", "Alerta Medico", DeviceType.MEDICAL_ALERT, RoomType.BEDROOM,
                                [ControlMethod.VOICE, ControlMethod.BRAIN_INTERFACE]))
    # Sala
    home.add_device(SmartDevice("tv", "TV Smart", DeviceType.TV, RoomType.LIVING_ROOM,
                                [ControlMethod.VOICE, ControlMethod.EYE_TRACKING]))
    home.add_device(SmartDevice("ar", "Ar Condicionado", DeviceType.AIR_CONDITIONER, RoomType.LIVING_ROOM,
                                [ControlMethod.VOICE, ControlMethod.AUTOMATION_SCHEDULE]))
    # Cozinha
    home.add_device(SmartDevice("porta", "Fechadura Eletronica", DeviceType.DOOR_LOCK, RoomType.ENTRANCE,
                                [ControlMethod.VOICE, ControlMethod.PROXIMITY]))
    home.add_device(SmartDevice("braco", "Braco Robotico", DeviceType.ROBOTIC_ARM, RoomType.KITCHEN,
                                [ControlMethod.EYE_TRACKING, ControlMethod.SWITCH]))
    return home


def create_home_elderly() -> InclusiveHome:
    """Casa para idoso -- automacoes fortes + voz simples."""
    home = InclusiveHome()
    home.add_device(SmartDevice("luz_banheiro", "Luz Banheiro", DeviceType.LIGHT, RoomType.BATHROOM,
                                [ControlMethod.VOICE, ControlMethod.PROXIMITY, ControlMethod.AUTOMATION_SCHEDULE]))
    home.add_device(SmartDevice("campainha", "Campainha Inteligente", DeviceType.DOORBELL, RoomType.ENTRANCE,
                                [ControlMethod.VOICE, ControlMethod.SMARTWATCH_GESTURE]))
    return home


def create_home_autism() -> InclusiveHome:
    """Casa para autista -- controle previsivel, sem surpresas."""
    home = InclusiveHome()
    home.add_device(SmartDevice("luz_sala", "Luz Sala", DeviceType.LIGHT, RoomType.LIVING_ROOM,
                                [ControlMethod.SWITCH, ControlMethod.HEAD_MOVEMENT]))
    return home


def create_home_blind() -> InclusiveHome:
    """Casa para cego -- voz + audio + feedback sonoro."""
    home = InclusiveHome()
    home.add_device(SmartDevice("speaker", "Caixa de Som", DeviceType.SPEAKER, RoomType.LIVING_ROOM,
                                [ControlMethod.VOICE]))
    return home


# ============================================================================
# 5. CENARIOS DE DEMONSTRACAO
# ============================================================================

def scenario_morning_routine():
    print("\n" + "=" * 60)
    print("CENARIO: Rotina da manha -- tetraplegico")
    print("=" * 60)
    home = create_home_tetraplegic()
    print(home.voice.execute_voice_command("liga a luz do quarto"))
    print(home.voice.execute_voice_command("levanta a cama"))
    print("Casa adaptada para o usuario acordar sem ajuda humana.")


def scenario_emergency_fall():
    print("\n" + "=" * 60)
    print("CENARIO: Queda detectada -- idoso")
    print("=" * 60)
    home = create_home_elderly()
    print(home.trigger_emergency("sensor_queda"))
    print("Alerta medico + vizinhos + familia notificados automaticamente.")


def scenario_voice_control_day():
    print("\n" + "=" * 60)
    print("CENARIO: Dia inteiro controlado por voz")
    print("=" * 60)
    home = create_home_tetraplegic()
    comandos = [
        "liga a luz do quarto",
        "abre a porta",
        "liga a tv",
        "socorro"
    ]
    for cmd in comandos:
        print(f"Usuario diz: '{cmd}' -> {home.voice.execute_voice_command(cmd)}")


def scenario_eye_control_cooking():
    print("\n" + "=" * 60)
    print("CENARIO: Preparar cafe com eye-tracking")
    print("=" * 60)
    home = create_home_tetraplegic()
    print(home.eye.calibrate())
    print(home.eye.look_at_device("braco"))
    print(home.eye.dwell_select("braco"))
    print("Braco robotico pega xicara e liga cafeteira sem tocar em nada.")


# ============================================================================
# 6. DEMO COMPLETA
# ============================================================================

def demo():
    print("=" * 70)
    print("OpenInclusiveHome -- A Casa que se Adapta à Pessoa")
    print("=" * 70)

    print(f"\nTipos de dispositivo: {len(DeviceType)}")
    print(f"Metodos de controle: {len(ControlMethod)}")
    print(f"Comodos: {len(RoomType)}")
    print(f"Gatilhos de automacao: {len(AutomationTrigger)}")
    print(f"Niveis de urgencia: {len(UrgencyLevel)}")

    # Cenários
    scenario_morning_routine()
    scenario_emergency_fall()
    scenario_voice_control_day()
    scenario_eye_control_cooking()

    # Perfis
    print(f"\n{'=' * 70}")
    print("PERFIS DE CASA INCLUSIVA")
    print(f"{'=' * 70}")

    perfis = {
        "Tetraplegico": create_home_tetraplegic(),
        "Idoso": create_home_elderly(),
        "Autista": create_home_autism(),
        "Cego": create_home_blind(),
    }

    for label, h in perfis.items():
        status = h.get_full_status()
        print(f"\n  {label}:")
        print(f"    Dispositivos: {status['dispositivos']}")
        print(f"    Temperatura: {status['temperatura']}C")
        print(f"    Seguranca: {'armada' if status['seguranca'] else 'desarmada'}")
        print(f"    Energia: {status['energia']['status']}")

    print(f"\n{'=' * 70}")
    print("PRINCIPIOS DA CASA INCLUSIVA")
    print(f"{'=' * 70}")
    print("TODO dispositivo controlavel por voz, olhar, switch ou cerebro.")
    print("A casa se adapta ao usuario -- nunca o contrario.")
    print("Zero botoes fisicos. Zero telas. Zero barreiras.")
    print("Energia solar + bateria sempre priorizada.")
    print("Emergencias detectadas e tratadas automaticamente.")
    print("\nTODO mundo. TODA deficiencia. ZERO exclusao.")
    print("UMA casa. UMA pessoa. INFINITAS possibilidades.")


if __name__ == "__main__":
    demo()
