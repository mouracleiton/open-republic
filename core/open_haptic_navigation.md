# OpenHapticNavigation -- Navegacao por Vibracao para Cegos

**Arquivo original:** `open-republic/core/open_haptic_navigation.py`

**Descricao:** ==========================================================
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

---

```portugol

// !/usr/bin/env python3
// 
OpenHapticNavigation -- Navegacao por Vibracao para Cegos
==========================================================
"O cego nao precisa de voz o tempo todo.
As vezes o silencio e melhor. As vezes a vibracao fala.
Vire a esquerda <- um toque no pulso esquerdo.
Obstaculo a frente <- vibracao crescente na cintura.
Destino chegando <- pulsacao ritmica no tornozelo.

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
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa deque de collections
// importa time
// importa math


// ============================================================================
// 1. DISPOSITIVOS HAPTICOS
// ============================================================================

classe HapticDevice herda de Enum:
    SMARTWATCH_LEFT <- "smartwatch_esquerdo"
    SMARTWATCH_RIGHT <- "smartwatch_direito"
    BRACELET_LEFT_ARM <- "braceaco_esquerdo"
    BRACELET_RIGHT_ARM <- "braceaco_direito"
    ANKLE_LEFT <- "tornozelo_esquerdo"
    ANKLE_RIGHT <- "tornozelo_direito"
    WAIST_BAND <- "cinto_cintura"
    CHEST_VEST <- "colete_peito"
    RING_FINGER <- "anel_dedo"
    NECKBAND <- "colar_pescoco"
    INSOLE_LEFT <- " palmilha_esquerda"
    INSOLE_RIGHT <- "palmilha_direita"


classe BodyPosition herda de Enum:
    // Onde no corpo o dispositivo fica.
    LEFT_WRIST <- "pulso_esquerdo"
    RIGHT_WRIST <- "pulso_direito"
    LEFT_ARM <- "braco_esquerdo"
    RIGHT_ARM <- "braco_direito"
    LEFT_ANKLE <- "tornozelo_esquerdo"
    RIGHT_ANKLE <- "tornozelo_direito"
    WAIST <- "cintura"
    CHEST <- "peito"
    FINGER <- "dedo"
    NECK <- "pescoco"
    LEFT_FOOT <- "pe_esquerdo"
    RIGHT_FOOT <- "pe_direito"
    BACK <- "costas"


classe VibrationPattern herda de Enum:
    // Padroes de vibracao com significados.
    NONE <- "nenhuma"
    SINGLE_TAP <- "toque_unica"  // 1 vibracao curta
    DOUBLE_TAP <- "toque_duplo"  // 2 vibracoes curtas
    TRIPLE_TAP <- "toque_triplo"  // 3 vibracoes curtas
    LONG_BUZZ <- "zumbido_longo"  // 1 vibracao longa
    PULSE <- "pulsacao"  // pulsacao ritmica
    ESCALATING <- "crescente"  // comeca fraco, aumenta
    DESCENDING <- "decrescente"  // comeca forte, diminui
    WAVE <- "onda"  // onda de um lado pro outro
    HEARTBEAT <- "batimento"  // batimento cardíaco
    ALARM <- "alarme"  // vibracao continua forte
    MORSE_LIKE <- "morse"  // codificacao tipo morse


classe Direction herda de Enum:
    // Direcoes para navegacao.
    FORWARD <- "frente"
    BACKWARD <- "tras"
    LEFT <- "esquerda"
    RIGHT <- "direita"
    STOP <- "pare"
    SLIGHT_LEFT <- "levemente_esquerda"
    SLIGHT_RIGHT <- "levemente_direita"
    TURN_AROUND <- "meia_volta"
    UP <- "subir"
    DOWN <- "descer"


classe HazardLevel herda de Enum:
    // Nivel de perigo detectado.
    CLEAR <- "livre"
    INFO <- "informacao"
    CAUTION <- "atencao"
    WARNING <- "aviso"
    DANGER <- "perigo"
    CRITICAL <- "critico"


// ============================================================================
// 2. MAPA DE VIBRACOES (Linguagem Haptica)
// ============================================================================

// decorador: @dataclass
classe HapticSignal:
    // Um sinal haptico com significado.
    signal_id: str
    device: HapticDevice
    body_position: BodyPosition
    pattern: VibrationPattern
    duration_ms: int                     // duracao em milissegundos
    intensity: float                     // 0.0 (fraquinho) a 1.0 (maximo)
    declare meaning: str  <- ""  // o que significa
    declare direction: Optional[Direction]  <- nulo
    declare hazard: HazardLevel  <- HazardLevel.CLEAR


// ============================================================================
// 3. Dicionario Haptico (Cada situacao = 1 vibracao)
// ============================================================================

declare HAPTIC_DICTIONARY: List[HapticSignal]  <- [
    // === DIRECOES ===
    HapticSignal("H-001", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.SINGLE_TAP, 200, 0.5,
                 meaning <- "Vire a esquerda", direction=Direction.LEFT),
    HapticSignal("H-002", HapticDevice.SMARTWATCH_RIGHT, BodyPosition.RIGHT_WRIST,
                 VibrationPattern.SINGLE_TAP, 200, 0.5,
                 meaning <- "Vire a direita", direction=Direction.RIGHT),
    HapticSignal("H-003", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.DOUBLE_TAP, 300, 0.6,
                 meaning <- "Continue reto", direction=Direction.FORWARD),
    HapticSignal("H-004", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.LONG_BUZZ, 800, 0.8,
                 meaning <- "Pare", direction=Direction.STOP),
    HapticSignal("H-005", HapticDevice.WAIST_BAND, BodyPosition.WAIST,
                 VibrationPattern.WAVE, 600, 0.5,
                 meaning <- "Meia volta", direction=Direction.TURN_AROUND),

    // === OBSTACULOS ===
    HapticSignal("H-010", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.ESCALATING, 1000, 0.7,
                 meaning <- "Obstaculo a esquerda se aproximando", hazard=HazardLevel.WARNING),
    HapticSignal("H-011", HapticDevice.SMARTWATCH_RIGHT, BodyPosition.RIGHT_WRIST,
                 VibrationPattern.ESCALATING, 1000, 0.7,
                 meaning <- "Obstaculo a direita se aproximando", hazard=HazardLevel.WARNING),
    HapticSignal("H-012", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.ALARM, 1500, 1.0,
                 meaning <- "OBSTACULO DIRETO A FRENTE! PERIGO!", hazard=HazardLevel.CRITICAL),
    HapticSignal("H-013", HapticDevice.ANKLE_LEFT, BodyPosition.LEFT_ANKLE,
                 VibrationPattern.SINGLE_TAP, 150, 0.4,
                 meaning <- "Buraco/degrau a esquerda do pe", hazard=HazardLevel.CAUTION),
    HapticSignal("H-014", HapticDevice.ANKLE_RIGHT, BodyPosition.RIGHT_ANKLE,
                 VibrationPattern.SINGLE_TAP, 150, 0.4,
                 meaning <- "Buraco/degrau a direita do pe", hazard=HazardLevel.CAUTION),

    // === SEMAFORO ===
    HapticSignal("H-020", HapticDevice.SMARTWATCH_RIGHT, BodyPosition.RIGHT_WRIST,
                 VibrationPattern.PULSE, 2000, 0.4,
                 meaning <- "Semaforo verde -- pode atravessar", hazard=HazardLevel.CLEAR),
    HapticSignal("H-021", HapticDevice.SMARTWATCH_RIGHT, BodyPosition.RIGHT_WRIST,
                 VibrationPattern.LONG_BUZZ, 1500, 0.8,
                 meaning <- "Semaforo vermelho -- PARE", hazard=HazardLevel.DANGER),
    HapticSignal("H-022", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.DOUBLE_TAP, 400, 0.5,
                 meaning <- "Semaforo amarelo -- atencao", hazard=HazardLevel.CAUTION),

    // === NAVEGACAO GPS ===
    HapticSignal("H-030", HapticDevice.RING_FINGER, BodyPosition.FINGER,
                 VibrationPattern.SINGLE_TAP, 100, 0.3,
                 meaning <- "Destino se aproximando (100m)"),
    HapticSignal("H-031", HapticDevice.RING_FINGER, BodyPosition.FINGER,
                 VibrationPattern.DOUBLE_TAP, 200, 0.4,
                 meaning <- "Destino se aproximando (50m)"),
    HapticSignal("H-032", HapticDevice.RING_FINGER, BodyPosition.FINGER,
                 VibrationPattern.HEARTBEAT, 600, 0.6,
                 meaning <- "Voce CHEGOU no destino!"),
    HapticSignal("H-033", HapticDevice.ANKLE_LEFT, BodyPosition.LEFT_ANKLE,
                 VibrationPattern.PULSE, 500, 0.3,
                 meaning <- "Rota recalculada -- vire a esquerda logo"),
    HapticSignal("H-034", HapticDevice.ANKLE_RIGHT, BodyPosition.RIGHT_ANKLE,
                 VibrationPattern.PULSE, 500, 0.3,
                 meaning <- "Rota recalculada -- vire a direita logo"),

    // === DISTANCIA (feedback continuo) ===
    HapticSignal("H-040", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.NONE, 0, 0.0,
                 meaning <- "Caminho livre (>5m)"),
    HapticSignal("H-041", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.PULSE, 500, 0.2,
                 meaning <- "Objeto a 3-5 metros"),
    HapticSignal("H-042", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.PULSE, 300, 0.4,
                 meaning <- "Objeto a 1-3 metros"),
    HapticSignal("H-043", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.ESCALATING, 200, 0.7,
                 meaning <- "Objeto a <1 metro! Atencao!"),

    // === PESSOAS ===
    HapticSignal("H-050", HapticDevice.NECKBAND, BodyPosition.NECK,
                 VibrationPattern.SINGLE_TAP, 200, 0.3,
                 meaning <- "Pessoa se aproximando por tras"),
    HapticSignal("H-051", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.DOUBLE_TAP, 300, 0.4,
                 meaning <- "Pessoa a frente vindo na sua direcao"),
    HapticSignal("H-052", HapticDevice.WAIST_BAND, BodyPosition.WAIST,
                 VibrationPattern.TRIPLE_TAP, 400, 0.5,
                 meaning <- "Grupo de pessoas a frente"),

    // === AMBIENTE ===
    HapticSignal("H-060", HapticDevice.INSOLE_LEFT, BodyPosition.LEFT_FOOT,
                 VibrationPattern.SINGLE_TAP, 100, 0.3,
                 meaning <- "Superficie irregular sob pe esquerdo"),
    HapticSignal("H-061", HapticDevice.INSOLE_RIGHT, BodyPosition.RIGHT_FOOT,
                 VibrationPattern.SINGLE_TAP, 100, 0.3,
                 meaning <- "Superficie irregular sob pe direito"),
    HapticSignal("H-062", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.DESCENDING, 600, 0.4,
                 meaning <- "Descendo ladeira"),
    HapticSignal("H-063", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.ESCALATING, 600, 0.4,
                 meaning <- "Subindo ladeira"),

    // === EMERGENCIA ===
    HapticSignal("H-090", HapticDevice.CHEST_VEST, BodyPosition.CHEST,
                 VibrationPattern.ALARM, 3000, 1.0,
                 meaning <- "EMERGENCIA -- perigo iminente", hazard=HazardLevel.CRITICAL),
    HapticSignal("H-091", HapticDevice.SMARTWATCH_LEFT, BodyPosition.LEFT_WRIST,
                 VibrationPattern.TRIPLE_TAP, 500, 0.9,
                 meaning <- "ALERTA -- veiculo se aproximando rapido", hazard=HazardLevel.DANGER),
]


// ============================================================================
// 4. MOTOR DE MAPEAMENTO AMBIENTAL
// ============================================================================

// decorador: @dataclass
classe EnvironmentScan:
    // Leitura do ambiente ao redor do usuario.
    declare timestamp: float  <- field(default_factory=time.time)
    declare obstacles: List[Dict[str, Any]]  <- field(default_factory=list)  // {direction, distance, type}
    declare nearest_obstacle_m: float  <- 100.0
    declare nearest_obstacle_direction: str  <- ""
    declare path_clear: bool  <- VERDADEIRO
    declare people_nearby: int  <- 0
    declare vehicles_nearby: int  <- 0
    declare surface_quality: str  <- "smooth"
    declare slope: str  <- "flat"
    declare traffic_light: Optional[str]  <- nulo
    declare crosswalk: bool  <- FALSO
    declare gps_accuracy: float  <- 5.0
    declare distance_to_destination_m: float  <- 0.0


classe EnvironmentMapper:
    // 
    Mapeia o ambiente (camera + GPS + lidar) e gera EnvironmentScan.
    Em producao: integra dados de OpenBodyCamera + GPS + sensores.
    // 

    funcao __init__(self):
        self.scans_history: deque = deque(maxlen=200)
        self.last_scan: Optional[EnvironmentScan] = nulo

    funcao scan(self) retorna EnvironmentScan:
        // Escaneia o ambiente (simulado).
        scan <- EnvironmentScan(
            obstacles <- [
                {"direction": "frente", "distance_m": 8.0, "type": "pessoa"},
                {"direction": "esquerda", "distance_m": 3.0, "type": "poste"},
                {"direction": "direita", "distance_m": 5.0, "type": "carro_estacionado"},
            ],
            nearest_obstacle_m <- 3.0,
            nearest_obstacle_direction <- "esquerda",
            path_clear <- VERDADEIRO,
            people_nearby <- 1,
            vehicles_nearby <- 1,
            surface_quality <- "smooth",
            slope <- "flat",
            traffic_light <- "verde",
            crosswalk <- FALSO,
            distance_to_destination_m <- 50.0,
        )
        self.last_scan = scan
        self.scans_history.append(scan)
        retorne scan

    def scan_with_obstacle(self, direction: str = "frente", distance: float = 1.5,
                           declare obstacle_type: str  <- "buraco") -> EnvironmentScan:
        // Simula cenario com obstaculo.
        scan <- EnvironmentScan(
            obstacles <- [{"direction": direction, "distance_m": distance, "type": obstacle_type}],
            nearest_obstacle_m <- distance,
            nearest_obstacle_direction <- direction,
            path_clear <- distance > 2.0,
        )
        self.last_scan = scan
        self.scans_history.append(scan)
        retorne scan

    funcao scan_traffic_light(self, color: str) retorna EnvironmentScan:
        // Simula cenario de semaforo.
        scan <- EnvironmentScan(
            obstacles <- [],
            nearest_obstacle_m <- 10.0,
            path_clear <- color == "verde",
            traffic_light <- color,
            crosswalk <- VERDADEIRO,
            distance_to_destination_m <- 30.0,
        )
        self.last_scan = scan
        self.scans_history.append(scan)
        retorne scan


// ============================================================================
// 5. TRADUTOR AMBIENTE -> VIBRACAO
// ============================================================================

classe HapticTranslator:
    // 
    Traduz EnvironmentScan em sinais hapticos.
    Decide QUAIS dispositivos vibrar, COMO e QUANDO.
    // 

    funcao __init__(self, active_devices: List[HapticDevice] = None):
        self.active_devices = active_devices  OU  [HapticDevice.SMARTWATCH_LEFT, HapticDevice.SMARTWATCH_RIGHT]
        self.dictionary = {s.signal_id: s for s in HAPTIC_DICTIONARY}
        self.last_signals: deque = deque(maxlen=50)
        self.min_interval_s: float = 0.8   // intervalo minimo entre sinais
        self.last_signal_time: float = 0

    funcao translate(self, scan: EnvironmentScan) retorna List[HapticSignal]:
        // Traduz scan do ambiente em lista de sinais hapticos.
        signals <- []

        // 1. Obstaculos
        para cada obs em scan.obstacles:
            signal <- self._obstacle_to_signal(obs)
            se signal entao:
                signals.append(signal)

        // 2. Semaforo
        se scan.traffic_light entao:
            signal <- self._traffic_light_to_signal(scan.traffic_light)
            se signal entao:
                signals.append(signal)

        // 3. Destino se aproximando
        se scan.distance_to_destination_m > 0 entao:
            signal <- self._distance_to_signal(scan.distance_to_destination_m)
            se signal entao:
                signals.append(signal)

        // 4. Superficie
        se scan.surface_quality != "smooth" entao:
            signal <- self._surface_to_signal(scan.surface_quality)
            se signal entao:
                signals.append(signal)

        // 5. Inclinacao
        se scan.slope != "flat" entao:
            signal <- self._slope_to_signal(scan.slope)
            se signal entao:
                signals.append(signal)

        // Filtrar por dispositivos ativos
        signals <- [s for s in signals if s.device in self.active_devices]

        // Dedup e rate limiting
        now <- time.time()
        se now - self.last_signal_time < self.min_interval_s entao:
            // So passar criticos
            signals <- [s for s in signals if s.hazard in (HazardLevel.DANGER, HazardLevel.CRITICAL)]

        se signals entao:
            self.last_signal_time = now
            para cada s em signals:
                self.last_signals.append(s)

        retorne signals

    funcao _obstacle_to_signal(self, obstacle: Dict[str, Any]) retorna Optional[HapticSignal]:
        // Converte obstaculo em sinal haptico.
        distance <- obstacle.get("distance_m", 100)
        direction <- obstacle.get("direction", "frente")

        se distance < 1.0 entao:
            // CRITICO
            retorne self.dictionary.get("H-012")  // ALARM peito
        senao se distance < 2.0 entao:
            // Perigo
            se direction == "esquerda" entao:
                retorne self.dictionary.get("H-010")
            senao se direction == "direita" entao:
                retorne self.dictionary.get("H-011")
            senao:
                retorne self.dictionary.get("H-012")
        senao se distance < 4.0 entao:
            // Atencao
            se direction == "esquerda" entao:
                retorne self.dictionary.get("H-010")
            senao se direction == "direita" entao:
                retorne self.dictionary.get("H-011")
        retorne nulo

    funcao _traffic_light_to_signal(self, color: str) retorna Optional[HapticSignal]:
        se color == "verde" entao:
            retorne self.dictionary.get("H-020")
        senao se color == "vermelho" entao:
            retorne self.dictionary.get("H-021")
        senao se color == "amarelo" entao:
            retorne self.dictionary.get("H-022")
        retorne nulo

    funcao _distance_to_signal(self, distance_m: float) retorna Optional[HapticSignal]:
        se distance_m <= 5 entao:
            retorne self.dictionary.get("H-032")  // CHEGOU
        senao se distance_m <= 50 entao:
            retorne self.dictionary.get("H-031")  // 50m
        senao se distance_m <= 100 entao:
            retorne self.dictionary.get("H-030")  // 100m
        retorne nulo

    funcao _surface_to_signal(self, quality: str) retorna Optional[HapticSignal]:
        se quality == "irregular_left" entao:
            retorne self.dictionary.get("H-060")
        senao se quality == "irregular_right" entao:
            retorne self.dictionary.get("H-061")
        retorne nulo

    funcao _slope_to_signal(self, slope: str) retorna Optional[HapticSignal]:
        se slope == "downhill" entao:
            retorne self.dictionary.get("H-062")
        senao se slope == "uphill" entao:
            retorne self.dictionary.get("H-063")
        retorne nulo

    funcao signal_to_direction(self, direction: Direction) retorna Optional[HapticSignal]:
        // Converte direcao de navegacao em sinal haptico.
        mapping <- {
            Direction.LEFT: "H-001",
            Direction.RIGHT: "H-002",
            Direction.FORWARD: "H-003",
            Direction.STOP: "H-004",
            Direction.TURN_AROUND: "H-005",
        }
        sig_id <- mapping.get(direction)
        retorne self.dictionary.get(sig_id) if sig_id else nulo


// ============================================================================
// 6. GERENCIADOR DE DISPOSITIVOS HAPTICOS
// ============================================================================

classe HapticDeviceManager:
    // 
    Gerencia dispositivos hapticos fisicos.
    Conecta, desconecta, envia vibracoes, monitora bateria.
    // 

    funcao __init__(self):
        self.connected: Dict[HapticDevice, Dict] = {}
        self.signal_history: deque = deque(maxlen=500)

    funcao connect(self, device: HapticDevice, battery_pct: float = 100.0) retorna str:
        // Conecta um dispositivo haptico.
        self.connected[device] = {
            "battery_pct": battery_pct,
            "online": VERDADEIRO,
            "signals_sent": 0,
            "last_active": time.time(),
        }
        retorne f"{device.value} conectado. Bateria: {battery_pct:.0f}%."

    funcao disconnect(self, device: HapticDevice) retorna str:
        se device in self.connected entao:
            remova self.connected[device]
            retorne f"{device.value} desconectado."
        retorne f"{device.value} nao estava conectado."

    funcao send_signal(self, signal: HapticSignal) retorna Dict[str, Any]:
        // Envia um sinal haptico para o dispositivo.
        se signal.device NAO  in self.connected entao:
            retorne {"sent": FALSO, "reason": "dispositivo nao conectado"}

        dev <- self.connected[signal.device]
        se NAO  dev["online"] entao:
            retorne {"sent": FALSO, "reason": "dispositivo offline"}

        dev["signals_sent"] += 1
        dev["last_active"] = time.time()

        record <- {
            "device": signal.device.value,
            "pattern": signal.pattern.value,
            "intensity": signal.intensity,
            "duration_ms": signal.duration_ms,
            "meaning": signal.meaning,
            "timestamp": time.time(),
            "sent": VERDADEIRO,
        }
        self.signal_history.append(record)
        retorne record

    funcao send_signals(self, signals: List[HapticSignal]) retorna List[Dict[str, Any]]:
        // Envia multiplos sinais.
        retorne [self.send_signal(s) for s in signals]

    funcao status(self) retorna Dict[str, Any]:
        retorne {
            "connected_devices": len(self.connected),
            "devices": {d.value: info for d, info in self.connected.items()},
            "total_signals_sent": sum(d["signals_sent"] for d in self.connected.values()),
        }


// ============================================================================
// 7. CONTROLADOR PRINCIPAL
// ============================================================================

classe HapticNavigationController:
    // 
    Orquestra mapeamento ambiental + traducao haptica + dispositivos.
    O usuario sente vibracoes e navega sem voz, sem fone, sem tela.

    Uso:
        nav <- HapticNavigationController()
        nav.connect_device(HapticDevice.SMARTWATCH_LEFT)
        nav.connect_device(HapticDevice.SMARTWATCH_RIGHT)
        nav.start()
        // Sistema escaneia ambiente e vibra automaticamente
        nav.navigate_to("padaria")
    // 

    funcao __init__(self, devices: List[HapticDevice] = None):
        self.mapper = EnvironmentMapper()
        self.translator = HapticTranslator(devices  OU  [])
        self.device_manager = HapticDeviceManager()
        self.active: bool = FALSO
        self.destination: str = ""
        self.scan_interval_s: float = 0.5   // escaneia a cada 500ms
        self.last_scan_time: float = 0
        self.total_scans: int = 0
        self.total_signals: int = 0
        self.session_start: float = 0

    funcao connect_device(self, device: HapticDevice, battery: float = 100) retorna str:
        // Conecta dispositivo haptico.
        retorne self.device_manager.connect(device, battery)

    funcao start(self) retorna Dict[str, Any]:
        // Inicia navegacao haptica.
        self.active = VERDADEIRO
        self.session_start = time.time()
        retorne {
            "active": VERDADEIRO,
            "devices": list(self.device_manager.connected.keys()),
            "device_count": len(self.device_manager.connected),
            "message": "Navegacao haptica ativa. Sinta as vibracoes.",
        }

    funcao stop(self) retorna Dict[str, Any]:
        self.active = FALSO
        duration <- time.time() - self.session_start if self.session_start else 0
        retorne {
            "active": FALSO,
            "duration_min": duration / 60,
            "total_scans": self.total_scans,
            "total_signals": self.total_signals,
        }

    funcao navigate_to(self, destination: str) retorna str:
        self.destination = destination
        retorne f"Navegando para {destination}. Siga as vibracoes."

    funcao turn(self, direction: Direction) retorna Dict[str, Any]:
        // Emite sinal de direcao.
        signal <- self.translator.signal_to_direction(direction)
        se signal  E  signal.device in self.device_manager.connected entao:
            result <- self.device_manager.send_signal(signal)
            self.total_signals += 1
            retorne result
        retorne {"sent": FALSO, "reason": "sem dispositivo para esta direcao"}

    funcao scan_and_vibrate(self) retorna List[Dict[str, Any]]:
        // Escaneia ambiente e envia vibracoes automaticamente.
        se NAO  self.active entao:
            retorne []

        scan <- self.mapper.scan()
        self.total_scans += 1

        signals <- self.translator.translate(scan)
        results <- self.device_manager.send_signals(signals)
        self.total_signals += len(signals)

        retorne results

    def alert_obstacle(self, direction: str = "frente", distance: float = 1.5,
                       declare obstacle_type: str  <- "buraco") -> Dict[str, Any]:
        // Alerta sobre obstaculo especifico.
        scan <- self.mapper.scan_with_obstacle(direction, distance, obstacle_type)
        signals <- self.translator.translate(scan)
        se signals entao:
            result <- self.device_manager.send_signal(signals[0])
            self.total_signals += 1
            retorne result
        retorne {"sent": FALSO, "reason": "sem sinal para este obstaculo"}

    funcao alert_traffic_light(self, color: str) retorna Dict[str, Any]:
        // Alerta sobre semaforo.
        scan <- self.mapper.scan_traffic_light(color)
        signals <- self.translator.translate(scan)
        se signals entao:
            results <- []
            para cada s em signals:
                se s.device in self.device_manager.connected entao:
                    r <- self.device_manager.send_signal(s)
                    results.append(r)
                    self.total_signals += 1
            retorne {"signals": results, "color": color}
        retorne {"sent": FALSO}

    funcao alert_arrival(self) retorna Dict[str, Any]:
        // Emite sinal de chegada ao destino.
        signal <- self.translator.dictionary.get("H-032")
        se signal  E  signal.device in self.device_manager.connected entao:
            retorne self.device_manager.send_signal(signal)
        retorne {"sent": FALSO}

    funcao alert_emergency(self) retorna Dict[str, Any]:
        // Emite sinal de emergencia em todos os dispositivos.
        signal <- self.translator.dictionary.get("H-090")
        results <- []
        para cada device em self.device_manager.connected:
            sig <- HapticSignal(
                signal_id <- "EMERG",
                device <- device,
                body_position <- BodyPosition.CHEST,
                pattern <- VibrationPattern.ALARM,
                duration_ms <- 3000,
                intensity <- 1.0,
                meaning <- "EMERGENCIA",
                hazard <- HazardLevel.CRITICAL,
            )
            r <- self.device_manager.send_signal(sig)
            results.append(r)
            self.total_signals += 1
        retorne {"emergency": VERDADEIRO, "signals_sent": len(results)}

    funcao status(self) retorna Dict[str, Any]:
        retorne {
            "active": self.active,
            "destination": self.destination,
            "devices": self.device_manager.status(),
            "total_scans": self.total_scans,
            "total_signals": self.total_signals,
            "dictionary_size": len(HAPTIC_DICTIONARY),
        }


// ============================================================================
// 8. CENARIOS DO MUNDO REAL
// ============================================================================

funcao scenario_walking_with_haptics():
    // Cenario: cego andando guiado por vibracoes.
    print("=" * 65)
    print("CENARIO 1: Cego andando guiado por vibracoes")
    print("=" * 65)

    nav <- HapticNavigationController()
    nav.connect_device(HapticDevice.SMARTWATCH_LEFT)
    nav.connect_device(HapticDevice.SMARTWATCH_RIGHT)
    nav.connect_device(HapticDevice.CHEST_VEST)

    start <- nav.start()
    print(f"\n{start['message']}")
    print(f"Dispositivos: {start['device_count']}")

    // Escanear ambiente
    print(f"\n[Escaneando ambiente...]")
    results <- nav.scan_and_vibrate()
    para cada r em results:
        se r.get("sent") entao:
            print(f"  -> {r['device']}: {r['pattern']} ({r['meaning']})")

    // Virar a esquerda
    print(f"\n[Instrucao: vire a esquerda]")
    result <- nav.turn(Direction.LEFT)
    se result.get("sent") entao:
        print(f"  -> {result['device']}: {result['meaning']}")

    // Obstaaculo
    print(f"\n[Obstaculo detectado!]")
    result <- nav.alert_obstacle("frente", 1.0, "poste")
    se result.get("sent") entao:
        print(f"  -> {result['device']}: {result['pattern']} | {result['meaning']}")


funcao scenario_crossing_with_haptics():
    // Cenario: atravessando rua com semaforo haptico.
    print(f"\n{'=' * 65}")
    print("CENARIO 2: Atravessando rua -- semaforo por vibracao")
    print("=" * 65)

    nav <- HapticNavigationController()
    nav.connect_device(HapticDevice.SMARTWATCH_RIGHT)
    nav.start()

    print(f"\n[Semaforo VERMELHO]")
    result <- nav.alert_traffic_light("vermelho")
    para cada s em result.get("signals", []):
        se s.get("sent") entao:
            print(f"  -> {s['device']}: {s['pattern']} | {s['meaning']}")

    print(f"\n[Semaforo VERDE]")
    result <- nav.alert_traffic_light("verde")
    para cada s em result.get("signals", []):
        se s.get("sent") entao:
            print(f"  -> {s['device']}: {s['pattern']} | {s['meaning']}")


funcao scenario_arriving_destination():
    // Cenario: chegando no destino.
    print(f"\n{'=' * 65}")
    print("CENARIO 3: Chegando no destino")
    print("=" * 65)

    nav <- HapticNavigationController()
    nav.connect_device(HapticDevice.RING_FINGER)
    nav.start()
    nav.navigate_to("casa")

    print(f"\n[100 metros do destino]")
    result <- nav.alert_arrival()
    print(f"  -> {result.get('meaning', 'sem sinal')}")

    print(f"\n[Chegou!]")
    result <- nav.alert_arrival()
    se result.get("sent") entao:
        print(f"  -> {result['device']}: {result['pattern']} | {result['meaning']}")


funcao scenario_emergency_haptic():
    // Cenario: emergencia -- todos os dispositivos vibram.
    print(f"\n{'=' * 65}")
    print("CENARIO 4: Emergencia haptica")
    print("=" * 65)

    nav <- HapticNavigationController()
    nav.connect_device(HapticDevice.SMARTWATCH_LEFT)
    nav.connect_device(HapticDevice.SMARTWATCH_RIGHT)
    nav.connect_device(HapticDevice.CHEST_VEST)
    nav.start()

    print(f"\n[EMERGENCIA!]")
    result <- nav.alert_emergency()
    print(f"  Sinais enviados: {result.get('signals_sent', 0)}")
    print(f"  Todos os dispositivos vibrando em ALARME.")


funcao scenario_full_body_haptic():
    // Cenario: sistema completo body-haptic.
    print(f"\n{'=' * 65}")
    print("CENARIO 5: Sistema completo (7 dispositivos)")
    print("=" * 65)

    nav <- HapticNavigationController()
    // Conectar 7 dispositivos
    for dev in [HapticDevice.SMARTWATCH_LEFT, HapticDevice.SMARTWATCH_RIGHT,
                HapticDevice.CHEST_VEST, HapticDevice.ANKLE_LEFT,
                HapticDevice.ANKLE_RIGHT, HapticDevice.RING_FINGER,
                HapticDevice.WAIST_BAND]:
        nav.connect_device(dev)

    start <- nav.start()
    print(f"\n{start['message']}")
    print(f"Dispositivos conectados: {start['device_count']}")

    // Escanear e vibrar
    print(f"\n[Escaneando e vibrando...]")
    results <- nav.scan_and_vibrate()
    para cada r em results:
        se r.get("sent") entao:
            print(f"  -> {r['device']}: {r['pattern']} ({r['meaning']})")

    status <- nav.status()
    print(f"\nTotal sinais enviados: {status['total_signals']}")


// ============================================================================
// 9. DEMONSTRACAO
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenHapticNavigation -- Navegacao por Vibracao para Cegos")
    print("=" * 70)

    print(f"\nDispositivos hapticos: {len(HapticDevice)}")
    print(f"Posicoes do corpo: {len(BodyPosition)}")
    print(f"Padroes de vibracao: {len(VibrationPattern)}")
    print(f"Direcoes: {len(Direction)}")
    print(f"Niveis de perigo: {len(HazardLevel)}")
    print(f"Sinais no dicionario: {len(HAPTIC_DICTIONARY)}")

    // Cenarios
    scenario_walking_with_haptics()
    scenario_crossing_with_haptics()
    scenario_arriving_destination()
    scenario_emergency_haptic()
    scenario_full_body_haptic()

    // Resumo do dicionario
    print(f"\n{'=' * 70}")
    print("DICIONARIO HAPTICO COMPLETO")
    print(f"{'=' * 70}")
    para cada s em HAPTIC_DICTIONARY:
        hazard_marker <- ""
        se s.hazard == HazardLevel.CRITICAL entao:
            hazard_marker <- " [CRITICO]"
        senao se s.hazard == HazardLevel.DANGER entao:
            hazard_marker <- " [PERIGO]"
        senao se s.hazard == HazardLevel.WARNING entao:
            hazard_marker <- " [ATENCAO]"
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


se __name__ == "__main__" entao:
    demo()

```
