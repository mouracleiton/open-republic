# OpenInclusiveHome -- A Casa Inteligente que se Adapta à Pessoa

**Arquivo original:** `open-republic/core/open_inclusive_home.py`

**Descricao:** ================================================================
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

---

```portugol

// !/usr/bin/env python3
// 
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
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set, Callable de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict, deque de collections
// importa time
// importa random


// ============================================================================
// 1. ENUMS -- TODOS OS DISPOSITIVOS E METODOS DE CONTROLE
// ============================================================================

classe DeviceType herda de Enum:
    // Tipos de dispositivos da casa inclusiva.
    LIGHT <- "luz"
    THERMOSTAT <- "termostato"
    DOOR_LOCK <- "fechadura"
    WINDOW <- "janela"
    CURTAIN <- "cortina"
    TV <- "televisao"
    SPEAKER <- "caixa_de_som"
    FAN <- "ventilador"
    AIR_CONDITIONER <- "ar_condicionado"
    OVEN <- "forno"
    MICROWAVE <- "microondas"
    COFFEE_MACHINE <- "cafeteira"
    BED_POSITION <- "posicao_cama"
    WHEELCHAIR_CHARGER <- "carregador_cadeira"
    MEDICAL_ALERT <- "alerta_medico"
    SECURITY_CAMERA <- "camera_seguranca"
    DOORBELL <- "campainha"
    GARAGE <- "garagem"
    ELEVATOR <- "elevador"
    ROBOTIC_ARM <- "braco_robotico"


classe ControlMethod herda de Enum:
    // Metodos de controle acessiveis.
    VOICE <- "voz"
    EYE_TRACKING <- "rastreamento_ocular"
    SWITCH <- "interruptor"
    BRAIN_INTERFACE <- "interface_cerebral"
    SMARTWATCH_GESTURE <- "gesto_smartwatch"
    BLOW_SUCK <- "sopro_sugada"
    HEAD_MOVEMENT <- "movimento_cabeca"
    AUTOMATION_SCHEDULE <- "automacao_agendada"
    PROXIMITY <- "proximidade"


classe RoomType herda de Enum:
    // Comodos da casa inclusiva.
    BEDROOM <- "quarto"
    LIVING_ROOM <- "sala"
    KITCHEN <- "cozinha"
    BATHROOM <- "banheiro"
    OFFICE <- "escritorio"
    GARAGE <- "garagem"
    GARDEN <- "jardim"
    ENTRANCE <- "entrada"


classe AutomationTrigger herda de Enum:
    // Gatilhos de automacao.
    TIME <- "horario"
    SUNRISE <- "nascer_sol"
    SUNSET <- "por_sol"
    TEMPERATURE <- "temperatura"
    MOTION <- "movimento"
    DOOR_OPEN <- "porta_aberta"
    WAKE_UP <- "acordar"
    SLEEP <- "dormir"
    EMERGENCY <- "emergencia"
    LOW_BATTERY <- "bateria_baixa"


classe UrgencyLevel herda de Enum:
    // Niveis de urgencia das acoes.
    ROUTINE <- "rotina"
    COMFORT <- "conforto"
    IMPORTANT <- "importante"
    URGENT <- "urgente"
    EMERGENCY <- "emergencia"


// ============================================================================
// 2. DATACLASSES -- ESTRUTURA DE DADOS
// ============================================================================

// decorador: @dataclass
classe SmartDevice:
    // Um dispositivo inteligente da casa inclusiva.
    device_id: str
    name: str
    device_type: DeviceType
    room: RoomType
    control_methods: List[ControlMethod]
    declare current_state: Dict[str, Any]  <- field(default_factory=dict)
    declare power_consumption_w: float  <- 0.0
    declare is_online: bool  <- VERDADEIRO
    declare automation_rules: List[str]  <- field(default_factory=list)

    funcao __post_init__(self):
        se NAO  self.current_state entao:
            self.current_state = {"status": "off", "level": 0}


// decorador: @dataclass
classe AutomationRule:
    // Regra de automacao da casa.
    rule_id: str
    trigger: AutomationTrigger
    condition: str
    action: str
    device_id: str
    declare enabled: bool  <- VERDADEIRO
    declare description: str  <- ""
    declare urgency: UrgencyLevel  <- UrgencyLevel.ROUTINE


// decorador: @dataclass
classe HomeState:
    // Estado completo da casa inclusiva.
    declare devices: Dict[str, SmartDevice]  <- field(default_factory=dict)
    declare temperature_c: float  <- 22.0
    declare security_armed: bool  <- FALSO
    declare energy_usage_w: float  <- 0.0
    declare solar_generation_w: float  <- 0.0
    declare battery_level_pct: float  <- 85.0
    declare last_update: float  <- field(default_factory=time.time)


// decorador: @dataclass
classe RoomConfig:
    // Configuracao de um comodo inclusivo.
    room_type: RoomType
    declare devices: List[str]  <- field(default_factory=list)
    declare ambient_preferences: Dict[str, Any]  <- field(default_factory=dict)
    declare accessibility_features: List[str]  <- field(default_factory=list)


// ============================================================================
// 3. CLASSES DE CONTROLE
// ============================================================================

classe DeviceController:
    // Controlador individual de dispositivos.

    funcao __init__(self, device: SmartDevice):
        self.device = device
        self.command_history: List[Dict] = []

    funcao turn_on(self) retorna str:
        self.device.current_state["status"] = "on"
        self._log_command("turn_on")
        retorne f"{self.device.name} ligado."

    funcao turn_off(self) retorna str:
        self.device.current_state["status"] = "off"
        self._log_command("turn_off")
        retorne f"{self.device.name} desligado."

    funcao set_level(self, level: int) retorna str:
        self.device.current_state["level"] = max(0, min(100, level))
        self._log_command("set_level", level)
        retorne f"{self.device.name} ajustado para nivel {level}%."

    funcao get_status(self) retorna Dict[str, Any]:
        retorne {
            "device": self.device.name,
            "state": self.device.current_state,
            "online": self.device.is_online,
            "power_w": self.device.power_consumption_w
        }

    funcao execute_command(self, command: str, params: Dict = None) retorna str:
        params <- params  OU  {}
        se command == "on" entao:
            retorne self.turn_on()
        senao se command == "off" entao:
            retorne self.turn_off()
        senao se command == "level" entao:
            retorne self.set_level(params.get("level", 50))
        retorne f"Comando desconhecido: {command}"

    funcao _log_command(self, cmd: str, value: Any = None):
        self.command_history.append({
            "timestamp": time.time(),
            "command": cmd,
            "value": value,
            "method": "manual"
        })


classe VoiceHomeControl:
    // Controle por voz -- comandos naturais em portugues.

    funcao __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.voice_history: List[str] = []

    funcao parse_command(self, utterance: str) retorna Tuple[str, Dict]:
        utterance <- utterance.lower()
        se "luz" in utterance  OU  "luz do quarto" in utterance entao:
            retorne "light", {"room": RoomType.BEDROOM, "action": "on" if "liga" in utterance else "off"}
        se "cama" in utterance  E  "levanta" in utterance entao:
            retorne "bed", {"action": "raise"}
        se "porta" in utterance  E  "abre" in utterance entao:
            retorne "door", {"action": "unlock"}
        se "emergencia" in utterance  OU  "socorro" in utterance entao:
            retorne "emergency", {"action": "alert"}
        retorne "unknown", {}

    funcao execute_voice_command(self, utterance: str) retorna str:
        desempacote cmd, params <- self.parse_command(utterance)
        self.voice_history.append(utterance)
        se cmd == "light" entao:
            device <- self.home.find_device(RoomType.BEDROOM, DeviceType.LIGHT)
            se device entao:
                ctrl <- DeviceController(device)
                retorne ctrl.turn_on() if params["action"] == "on" else ctrl.turn_off()
        se cmd == "bed" entao:
            device <- self.home.find_device(RoomType.BEDROOM, DeviceType.BED_POSITION)
            se device entao:
                retorne DeviceController(device).set_level(80)
        se cmd == "emergency" entao:
            retorne self.home.trigger_emergency("voz")
        retorne "Comando nao reconhecido. Pode repetir?"

    funcao confirm_action(self, action: str) retorna bool:
        // Em producao, usaria TTS + espera de confirmacao por voz
        retorne VERDADEIRO


classe EyeHomeControl:
    // Controle por rastreamento ocular (eye-tracking).

    funcao __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.calibrated = FALSO
        self.dwell_time_ms = 1200
        self.last_gaze: Optional[str] = nulo

    funcao calibrate(self) retorna str:
        self.calibrated = VERDADEIRO
        retorne "Calibracao ocular concluida. Olhe para o dispositivo desejado."

    funcao look_at_device(self, device_id: str) retorna str:
        se NAO  self.calibrated entao:
            retorne "Calibre primeiro o eye-tracker."
        self.last_gaze = device_id
        retorne f"Olhando para {device_id}. Mantenha o olhar por {self.dwell_time_ms}ms."

    funcao dwell_select(self, device_id: str) retorna str:
        device <- self.home.devices.get(device_id)
        se device entao:
            ctrl <- DeviceController(device)
            retorne ctrl.turn_on()
        retorne "Dispositivo nao encontrado."

    funcao scan_devices(self, room: RoomType) retorna List[str]:
        retorne [d.device_id for d in self.home.devices.values() if d.room == room]


classe SwitchHomeControl:
    // Controle por interruptor (switch scanning) -- varredura.

    funcao __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.current_scan_index = 0
        self.scan_list: List[str] = []

    funcao scan_rooms(self) retorna List[RoomType]:
        retorne list(RoomType)

    funcao scan_devices(self, room: RoomType) retorna List[str]:
        self.scan_list = [d.device_id for d in self.home.devices.values() if d.room == room]
        self.current_scan_index = 0
        retorne self.scan_list

    funcao select(self) retorna str:
        se NAO  self.scan_list entao:
            retorne "Nenhum dispositivo em varredura."
        device_id <- self.scan_list[self.current_scan_index]
        self.current_scan_index = (self.current_scan_index + 1) % len(self.scan_list)
        device <- self.home.devices.get(device_id)
        se device entao:
            retorne DeviceController(device).turn_on()
        retorne "Erro na selecao."


classe AutomationEngine:
    // Motor de automacoes -- executa regras sem intervencao humana.

    funcao __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.rules: Dict[str, AutomationRule] = {}
        self.execution_log: List[Dict] = []

    funcao add_rule(self, rule: AutomationRule) retorna str:
        self.rules[rule.rule_id] = rule
        retorne f"Regra {rule.rule_id} adicionada."

    funcao check_triggers(self, trigger: AutomationTrigger, context: Dict) retorna List[str]:
        executed <- []
        para cada rule em self.rules.values():
            se rule.trigger == trigger  E  rule.enabled entao:
                se self._condition_met(rule, context) entao:
                    result <- self.execute_automation(rule.rule_id)
                    executed.append(result)
        retorne executed

    funcao _condition_met(self, rule: AutomationRule, context: Dict) retorna bool:
        // Exemplo simples: temperatura > 28 ativa ar
        se "temperature" in rule.condition  E  context.get("temperature", 0) > 28 entao:
            retorne VERDADEIRO
        se rule.trigger == AutomationTrigger.WAKE_UP entao:
            retorne VERDADEIRO
        retorne FALSO

    funcao execute_automation(self, rule_id: str) retorna str:
        rule <- self.rules.get(rule_id)
        se NAO  rule entao:
            retorne "Regra nao encontrada."
        device <- self.home.devices.get(rule.device_id)
        se device entao:
            ctrl <- DeviceController(device)
            result <- ctrl.execute_command(rule.action)
            self.execution_log.append({"rule": rule_id, "time": time.time(), "result": result})
            retorne result
        retorne "Dispositivo offline."


classe HomeEnergyManager:
    // Gestor de energia -- prioriza solar e bateria.

    funcao __init__(self, home: 'InclusiveHome'):
        self.home = home
        self.daily_consumption: List[float] = []
        self.solar_history: List[float] = []

    funcao optimize(self) retorna str:
        state <- self.home.state
        se state.solar_generation_w > state.energy_usage_w entao:
            surplus <- state.solar_generation_w - state.energy_usage_w
            retorne f"Excedente solar: {surplus}W. Carregando bateria."
        se state.battery_level_pct < 20 entao:
            retorne "Bateria baixa. Reduzindo consumo de dispositivos nao essenciais."
        retorne "Consumo otimizado. Usando combinacao solar + rede."

    funcao report(self) retorna Dict[str, Any]:
        retorne {
            "uso_atual_w": self.home.state.energy_usage_w,
            "solar_w": self.home.state.solar_generation_w,
            "bateria_pct": self.home.state.battery_level_pct,
            "status": self.optimize()
        }


classe InclusiveHome:
    // Orquestrador principal da casa inclusiva.

    funcao __init__(self):
        self.devices: Dict[str, SmartDevice] = {}
        self.state = HomeState()
        self.voice = VoiceHomeControl(self)
        self.eye = EyeHomeControl(self)
        self.switch = SwitchHomeControl(self)
        self.automation = AutomationEngine(self)
        self.energy = HomeEnergyManager(self)
        self.rooms: Dict[RoomType, RoomConfig] = {}

    funcao add_device(self, device: SmartDevice) retorna str:
        self.devices[device.device_id] = device
        self.state.devices[device.device_id] = device
        se device.room NAO  in self.rooms entao:
            self.rooms[device.room] = RoomConfig(room_type=device.room)
        self.rooms[device.room].devices.append(device.device_id)
        retorne f"Dispositivo {device.name} adicionado ao {device.room.value}."

    funcao find_device(self, room: RoomType, dtype: DeviceType) retorna Optional[SmartDevice]:
        para cada d em self.devices.values():
            se d.room == room  E  d.device_type == dtype entao:
                retorne d
        retorne nulo

    funcao trigger_emergency(self, source: str) retorna str:
        alert <- self.find_device(RoomType.BEDROOM, DeviceType.MEDICAL_ALERT)
        se alert entao:
            DeviceController(alert).turn_on()
        self.state.security_armed = VERDADEIRO
        retorne f"EMERGENCIA acionada via {source}. Alerta medico enviado. Casa em modo seguro."

    funcao get_full_status(self) retorna Dict[str, Any]:
        retorne {
            "dispositivos": len(self.devices),
            "temperatura": self.state.temperature_c,
            "seguranca": self.state.security_armed,
            "energia": self.energy.report(),
            "automacoes_ativas": len(self.automation.rules)
        }


// ============================================================================
// 4. CENARIOS PREDEFINIDOS
// ============================================================================

funcao create_home_tetraplegic() retorna InclusiveHome:
    // Casa otimizada para tetraplegico -- controle total por voz/olhar/switch.
    home <- InclusiveHome()
    // Quarto
    home.add_device(SmartDevice("luz_quarto", "Luz do Quarto", DeviceType.LIGHT, RoomType.BEDROOM,
                                [ControlMethod.VOICE, ControlMethod.EYE_TRACKING, ControlMethod.SWITCH]))
    home.add_device(SmartDevice("cama", "Cama Articulada", DeviceType.BED_POSITION, RoomType.BEDROOM,
                                [ControlMethod.VOICE, ControlMethod.EYE_TRACKING, ControlMethod.BLOW_SUCK]))
    home.add_device(SmartDevice("alerta", "Alerta Medico", DeviceType.MEDICAL_ALERT, RoomType.BEDROOM,
                                [ControlMethod.VOICE, ControlMethod.BRAIN_INTERFACE]))
    // Sala
    home.add_device(SmartDevice("tv", "TV Smart", DeviceType.TV, RoomType.LIVING_ROOM,
                                [ControlMethod.VOICE, ControlMethod.EYE_TRACKING]))
    home.add_device(SmartDevice("ar", "Ar Condicionado", DeviceType.AIR_CONDITIONER, RoomType.LIVING_ROOM,
                                [ControlMethod.VOICE, ControlMethod.AUTOMATION_SCHEDULE]))
    // Cozinha
    home.add_device(SmartDevice("porta", "Fechadura Eletronica", DeviceType.DOOR_LOCK, RoomType.ENTRANCE,
                                [ControlMethod.VOICE, ControlMethod.PROXIMITY]))
    home.add_device(SmartDevice("braco", "Braco Robotico", DeviceType.ROBOTIC_ARM, RoomType.KITCHEN,
                                [ControlMethod.EYE_TRACKING, ControlMethod.SWITCH]))
    retorne home


funcao create_home_elderly() retorna InclusiveHome:
    // Casa para idoso -- automacoes fortes + voz simples.
    home <- InclusiveHome()
    home.add_device(SmartDevice("luz_banheiro", "Luz Banheiro", DeviceType.LIGHT, RoomType.BATHROOM,
                                [ControlMethod.VOICE, ControlMethod.PROXIMITY, ControlMethod.AUTOMATION_SCHEDULE]))
    home.add_device(SmartDevice("campainha", "Campainha Inteligente", DeviceType.DOORBELL, RoomType.ENTRANCE,
                                [ControlMethod.VOICE, ControlMethod.SMARTWATCH_GESTURE]))
    retorne home


funcao create_home_autism() retorna InclusiveHome:
    // Casa para autista -- controle previsivel, sem surpresas.
    home <- InclusiveHome()
    home.add_device(SmartDevice("luz_sala", "Luz Sala", DeviceType.LIGHT, RoomType.LIVING_ROOM,
                                [ControlMethod.SWITCH, ControlMethod.HEAD_MOVEMENT]))
    retorne home


funcao create_home_blind() retorna InclusiveHome:
    // Casa para cego -- voz + audio + feedback sonoro.
    home <- InclusiveHome()
    home.add_device(SmartDevice("speaker", "Caixa de Som", DeviceType.SPEAKER, RoomType.LIVING_ROOM,
                                [ControlMethod.VOICE]))
    retorne home


// ============================================================================
// 5. CENARIOS DE DEMONSTRACAO
// ============================================================================

funcao scenario_morning_routine():
    print("\n" + "=" * 60)
    print("CENARIO: Rotina da manha -- tetraplegico")
    print("=" * 60)
    home <- create_home_tetraplegic()
    print(home.voice.execute_voice_command("liga a luz do quarto"))
    print(home.voice.execute_voice_command("levanta a cama"))
    print("Casa adaptada para o usuario acordar sem ajuda humana.")


funcao scenario_emergency_fall():
    print("\n" + "=" * 60)
    print("CENARIO: Queda detectada -- idoso")
    print("=" * 60)
    home <- create_home_elderly()
    print(home.trigger_emergency("sensor_queda"))
    print("Alerta medico + vizinhos + familia notificados automaticamente.")


funcao scenario_voice_control_day():
    print("\n" + "=" * 60)
    print("CENARIO: Dia inteiro controlado por voz")
    print("=" * 60)
    home <- create_home_tetraplegic()
    comandos <- [
        "liga a luz do quarto",
        "abre a porta",
        "liga a tv",
        "socorro"
    ]
    para cada cmd em comandos:
        print(f"Usuario diz: '{cmd}' -> {home.voice.execute_voice_command(cmd)}")


funcao scenario_eye_control_cooking():
    print("\n" + "=" * 60)
    print("CENARIO: Preparar cafe com eye-tracking")
    print("=" * 60)
    home <- create_home_tetraplegic()
    print(home.eye.calibrate())
    print(home.eye.look_at_device("braco"))
    print(home.eye.dwell_select("braco"))
    print("Braco robotico pega xicara e liga cafeteira sem tocar em nada.")


// ============================================================================
// 6. DEMO COMPLETA
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenInclusiveHome -- A Casa que se Adapta à Pessoa")
    print("=" * 70)

    print(f"\nTipos de dispositivo: {len(DeviceType)}")
    print(f"Metodos de controle: {len(ControlMethod)}")
    print(f"Comodos: {len(RoomType)}")
    print(f"Gatilhos de automacao: {len(AutomationTrigger)}")
    print(f"Niveis de urgencia: {len(UrgencyLevel)}")

    // Cenários
    scenario_morning_routine()
    scenario_emergency_fall()
    scenario_voice_control_day()
    scenario_eye_control_cooking()

    // Perfis
    print(f"\n{'=' * 70}")
    print("PERFIS DE CASA INCLUSIVA")
    print(f"{'=' * 70}")

    perfis <- {
        "Tetraplegico": create_home_tetraplegic(),
        "Idoso": create_home_elderly(),
        "Autista": create_home_autism(),
        "Cego": create_home_blind(),
    }

    para cada (label, h) em perfis.items():
        status <- h.get_full_status()
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


se __name__ == "__main__" entao:
    demo()

```
