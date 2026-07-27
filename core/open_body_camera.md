# OpenBodyCamera -- Smartphone como Camera Corporal + Fone Bluetooth = Olhos do Cego

**Arquivo original:** `open-republic/core/open_body_camera.py`

**Descricao:** ===================================================================================
"O cego nao precisa de olhos. Precisa de INFORMACAO.
O smartphone na camisa capta o mundo.
O fone no ouvido TRADUZ o mundo em voz.
O cego VE com a camera. OUVE com o fone.
NADA o para. NINGUEM o limita.
A camera corporal e um PAR DE OLHOS emprestado.
O fone bluetooth e um PAR DE OUVIDOS que falam.
Juntos, sao o CORPO EXTENDIDO do cego na rua."
COMO FUNCIONA:
1. Smartphone preso no peito (clip de camisa/bolsinho)
2. Camera traseira aponta para frente
3. IA processa o video em tempo real (15-30 fps)
4. Fone bluetooth recebe descricao por voz
5.Usuario anda COM INFORMACAO
O QUE A CAMERA VE E DESCREVE:
- Obstaculos (poste, buraco, degrau, carro)
- Pessoas (quem e, quantas, proximidade)
- Textos (placas, menus, cartazes)
- Cores (semaforo, cedulas, roupas)
- Cena (restaurante, farmacia, rua, park)
- Perigos (moto approaching, objeto caindo)
- Orientacao (vire a direita, continue reto)
NIVEIS DE VERBALIZACAO:
- CONTINUO: descreve tudo o tempo todo (para iniciantes)
- POR DEMANDA: so descreve quando perguntado (para avancados)
- ALERTA: so fala em situacoes de perigo (para expertos)
- TATEANDO: descricao minima + sons direcionais (hiper-minimal)
MODO CO-PILOTO DE RUA:
A camera vira GPS visual. A voz no fone guia:
'Desca a calçada. Continue reto. Poste a esquerda em 3m.
Semaforo verde. Atravesse 15 passos. Farmacia a direita.
Seu destino e a porta azul, 10 metros.'
INTEGRACAO COM OPENHARDWARE:
- Smartphone: camera + processamento
- Fone bluetooth: saida de voz
- Smartwatch: vibracall para alertas criticos
- Bateria gerenciada por OpenResilience
- Emergency: OpenHumanNet se algo der errado
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol

// !/usr/bin/env python3
// 
OpenBodyCamera -- Smartphone como Camera Corporal + Fone Bluetooth = Olhos do Cego
===================================================================================
"O cego nao precisa de olhos. Precisa de INFORMACAO.
O smartphone na camisa capta o mundo.
O fone no ouvido TRADUZ o mundo em voz.
O cego VE com a camera. OUVE com o fone.
NADA o para. NINGUEM o limita.

A camera corporal e um PAR DE OLHOS emprestado.
O fone bluetooth e um PAR DE OUVIDOS que falam.
Juntos, sao o CORPO EXTENDIDO do cego na rua."

COMO FUNCIONA:
1. Smartphone preso no peito (clip de camisa/bolsinho)
2. Camera traseira aponta para frente
3. IA processa o video em tempo real (15-30 fps)
4. Fone bluetooth recebe descricao por voz
5.Usuario anda COM INFORMACAO

O QUE A CAMERA VE E DESCREVE:
- Obstaculos (poste, buraco, degrau, carro)
- Pessoas (quem e, quantas, proximidade)
- Textos (placas, menus, cartazes)
- Cores (semaforo, cedulas, roupas)
- Cena (restaurante, farmacia, rua, park)
- Perigos (moto approaching, objeto caindo)
- Orientacao (vire a direita, continue reto)

NIVEIS DE VERBALIZACAO:
- CONTINUO: descreve tudo o tempo todo (para iniciantes)
- POR DEMANDA: so descreve quando perguntado (para avancados)
- ALERTA: so fala em situacoes de perigo (para expertos)
- TATEANDO: descricao minima + sons direcionais (hiper-minimal)

MODO CO-PILOTO DE RUA:
A camera vira GPS visual. A voz no fone guia:
'Desca a calçada. Continue reto. Poste a esquerda em 3m.
Semaforo verde. Atravesse 15 passos. Farmacia a direita.
Seu destino e a porta azul, 10 metros.'

INTEGRACAO COM OPENHARDWARE:
- Smartphone: camera + processamento
- Fone bluetooth: saida de voz
- Smartwatch: vibracall para alertas criticos
- Bateria gerenciada por OpenResilience
- Emergency: OpenHumanNet se algo der errado

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
// 1. TIPOS DE MONTAGEM (Como o smartphone fica no corpo)
// ============================================================================

classe MountPosition herda de Enum:
    CHEST <- "peito"  // clipped na camisa, no peito -- padrao
    HEAD <- "cabeca"  // bandana/oculos com smartphone
    SHOULDER <- "ombro"  // alça de mochila
    NECK <- "pescoco"  // pendurado no pescoco
    HAND <- "mao"  // na mao apontando
    POCKET_FACING_OUT <- "bolso_frente"  // no bolso com camera pra fora
    ARMBAND <- "braceaco"  // bracelete de braco


classe CameraMode herda de Enum:
    CONTINUOUS <- "continuo"  // descreve tudo o tempo todo
    ON_DEMAND <- "sob_demanda"  // so quando usuario pede
    ALERT_ONLY <- "so_alerta"  // so perigos
    NAVIGATION <- "navegacao"  // co-piloto de rua
    READING <- "leitura"  // modo OCR (ler texto)
    MONEY <- "dinheiro"  // reconhecer cedulas
    COLOR <- "cor"  // identificar cores
    FACE <- "rosto"  // reconhecer pessoas
    SEARCH <- "busca"  // procurar objeto especifico
    MINIMAL <- "minimal"  // tateando (hiper-minimal)


classe VerbosityLevel herda de Enum:
    HIGH <- "alto"  // descreve tudo em detalhe
    MEDIUM <- "medio"  // descreve o essencial
    LOW <- "baixo"  // so alertas e orientacao
    WHISPER <- "sussurro"  // minimo possivel (1 palavra)


// ============================================================================
// 2. DETECCOES VISUAIS
// ============================================================================

classe ObjectType herda de Enum:
    OBSTACLE <- "obstaculo"
    PERSON <- "pessoa"
    VEHICLE <- "veiculo"
    ANIMAL <- "animal"
    SIGN <- "placa"
    DOOR <- "porta"
    STAIRS <- "escada"
    CROSSWALK <- "faixa"
    TRAFFIC_LIGHT <- "semaforo"
    TEXT <- "texto"
    MONEY <- "dinheiro"
    PRODUCT <- "produto"
    FOOD <- "comida"
    MEDICINE <- "remedio"
    FURNITURE <- "movel"
    TOOL <- "ferramenta"
    NATURE <- "natureza"


classe DangerLevel herda de Enum:
    SAFE <- "seguro"
    ATTENTION <- "atencao"
    WARNING <- "aviso"
    DANGER <- "perigo"
    CRITICAL <- "critico"


// decorador: @dataclass
classe Detection:
    // Uma deteccao da camera em tempo real.
    object_type: ObjectType
    label: str                          // nome amigavel
    distance_m: float                   // distancia estimada
    direction: str                      // frente, esquerda, direita, baixo, alto
    danger: DangerLevel
    confidence: float                   // 0-1
    declare action: str  <- ""  // o que o usuario deve fazer
    declare voice_description: str  <- ""  // descricao para TTS
    declare timestamp: float  <- field(default_factory=time.time)
    declare size: str  <- ""  // pequeno, medio, grande
    declare moving: bool  <- FALSO  // esta se movendo?
    declare approaching: bool  <- FALSO  // vindo na direcao do usuario?


// ============================================================================
// 3. MOTOR DE VISAO COMPUTACIONAL
// ============================================================================

classe VisionEngine:
    // 
    Processa frames da camera e gera descricoes em tempo real.
    Em producao: YOLO/MobileNet + MiDaS (depth) + OCR + face recognition.
    Aqui: simulacao realista do que a camera 've'.
    // 

    funcao __init__(self, mount: MountPosition = MountPosition.CHEST):
        self.mount = mount
        self.detections_history: deque = deque(maxlen=200)
        self.last_scene: str = ""
        self.frame_count: int = 0
        self.fps: float = 15.0
        self.processing_latency_ms: float = 80   // latencia processamento

    funcao process_frame(self, mode: CameraMode = CameraMode.CONTINUOUS) retorna List[Detection]:
        // Processa um frame da camera.
        self.frame_count += 1
        detections <- []

        se mode == CameraMode.NAVIGATION entao:
            detections <- self._scan_navigation()
        senao se mode == CameraMode.READING entao:
            detections <- self._scan_text()
        senao se mode == CameraMode.MONEY entao:
            detections <- self._scan_money()
        senao se mode == CameraMode.COLOR entao:
            detections <- self._scan_color()
        senao se mode == CameraMode.FACE entao:
            detections <- self._scan_faces()
        senao se mode == CameraMode.SEARCH entao:
            detections <- self._scan_search()
        senao:
            detections <- self._scan_continuous()

        para cada d em detections:
            self.detections_history.append(d)
        retorne detections

    funcao _scan_continuous(self) retorna List[Detection]:
        // Modo continuo: descreve tudo ao redor.
        retorne [
            Detection(
                ObjectType.PERSON, "Pessoa", 3.0, "frente",
                DangerLevel.SAFE, 0.92,
                action <- "Pessoa a 3 metros a frente.",
                voice_description <- "Pessoa a frente, 3 metros.",
                moving <- VERDADEIRO, approaching=FALSO,
            ),
            Detection(
                ObjectType.OBSTACLE, "Poste", 5.0, "frente-esquerda",
                DangerLevel.ATTENTION, 0.88,
                action <- "Poste a 5 metros. Mantenha a direita.",
                voice_description <- "Poste a esquerda, 5 metros.",
            ),
            Detection(
                ObjectType.VEHICLE, "Carro estacionado", 2.5, "direita",
                DangerLevel.SAFE, 0.95,
                voice_description <- "Carro estacionado a direita.",
            ),
        ]

    funcao _scan_navigation(self) retorna List[Detection]:
        // Modo navegacao: co-piloto de rua.
        retorne [
            Detection(
                ObjectType.CROSSWALK, "Faixa de pedestre", 8.0, "frente",
                DangerLevel.SAFE, 0.90,
                action <- "Continue reto. Faixa de pedestre em 8 metros.",
                voice_description <- "Faixa de pedestre a frente, 8 metros. Continue reto.",
            ),
            Detection(
                ObjectType.TRAFFIC_LIGHT, "Semaforo", 8.0, "frente-alto",
                DangerLevel.SAFE, 0.97,
                action <- "Semaforo VERDE. Pode atravessar.",
                voice_description <- "Semaforo verde. Pode atravessar.",
            ),
            Detection(
                ObjectType.OBSTACLE, "Buraco na calcada", 4.0, "frente-baixo",
                DangerLevel.WARNING, 0.85,
                action <- "Buraco a 4 metros. Desvie para a esquerda.",
                voice_description <- "Atencao! Buraco na calcada, 4 metros. Desvie a esquerda.",
            ),
        ]

    funcao _scan_text(self) retorna List[Detection]:
        // Modo leitura: OCR de textos do mundo.
        retorne [
            Detection(
                ObjectType.TEXT, "Placa de estabelecimento", 5.0, "frente-alto",
                DangerLevel.SAFE, 0.91,
                voice_description <- "A placa diz: RESTAURANTE DO JOAO. Aberto das 11 as 22.",
            ),
            Detection(
                ObjectType.TEXT, "Cardapio", 3.0, "frente",
                DangerLevel.SAFE, 0.88,
                voice_description <- "O cardapio diz: Feijoada R$ 25. Suco R$ 8. Prato feito R$ 18.",
            ),
        ]

    funcao _scan_money(self) retorna List[Detection]:
        // Modo dinheiro: reconhece cedulas e moedas.
        retorne [
            Detection(
                ObjectType.MONEY, "Nota de R$ 50", 0.5, "frente",
                DangerLevel.SAFE, 0.96,
                voice_description <- "Nota de CINQUENTA REAIS. Cor marrom.",
            ),
        ]

    funcao _scan_color(self) retorna List[Detection]:
        // Modo cor: identifica cores (daltonismo tambem).
        retorne [
            Detection(
                ObjectType.SIGN, "Sinal vermelho", 10.0, "frente-alto",
                DangerLevel.DANGER, 0.97,
                action <- "Semaforo VERMELHO. PARE.",
                voice_description <- "Semaforo VERMELHO. Pare.",
            ),
        ]

    funcao _scan_faces(self) retorna List[Detection]:
        // Modo rosto: reconhece pessoas.
        retorne [
            Detection(
                ObjectType.PERSON, "MING (esposa)", 2.0, "frente",
                DangerLevel.SAFE, 0.89,
                voice_description <- "MING esta a sua frente, 2 metros. Sorrindo.",
            ),
        ]

    funcao _scan_search(self) retorna List[Detection]:
        // Modo busca: procura objeto especifico.
        retorne [
            Detection(
                ObjectType.PRODUCT, "Chave", 1.5, "mesa",
                DangerLevel.SAFE, 0.82,
                voice_description <- "Encontrei a chave. Esta na mesa, a sua frente, 1 metro e meio.",
            ),
        ]

    funcao describe_scene(self, detections: List[Detection], verbosity: VerbosityLevel = VerbosityLevel.MEDIUM) retorna str:
        // Gera descricao da cena para TTS.
        se NAO  detections entao:
            se verbosity == VerbosityLevel.WHISPER entao:
                retorne "Livre."
            retorne "Nada a frente. Caminho livre."

        // Ordenar por perigo primeiro, depois distancia
        sorted_dets <- sorted(detections, key=funcao anonima(d): (
            -[1,2,3,4,5][list(DangerLevel).index(d.danger)],
            d.distance_m
        ))

        descriptions <- []
        para cada d em sorted_dets:
            se verbosity == VerbosityLevel.HIGH entao:
                descriptions.append(d.voice_description)
            senao se verbosity == VerbosityLevel.MEDIUM entao:
                // Encurtar se necessario
                desc <- d.voice_description
                se len(desc) > 60 entao:
                    desc <- desc[:57] + "..."
                descriptions.append(desc)
            senao se verbosity == VerbosityLevel.LOW entao:
                se d.danger in (DangerLevel.WARNING, DangerLevel.DANGER, DangerLevel.CRITICAL) entao:
                    descriptions.append(d.voice_description)
            senao se verbosity == VerbosityLevel.WHISPER entao:
                se d.danger in (DangerLevel.DANGER, DangerLevel.CRITICAL) entao:
                    descriptions.append(d.action if d.action else d.label)

        se NAO  descriptions entao:
            retorne "Livre."

        retorne ". ".join(descriptions) + "."


// ============================================================================
// 4. GERENCIADOR DE AUDIO BLUETOOTH
// ============================================================================

classe AudioOutputManager:
    // 
    Gerencia a saida de voz para o fone bluetooth.
    Prioriza alertas, corta descricoes redundantes, respeita silencio.
    // 

    funcao __init__(self):
        self.connected: bool = VERDADEIRO
        self.device_name: str = "Fone Bluetooth"
        self.battery_pct: float = 100.0
        self.volume: float = 0.7
        self.tts_rate: float = 1.4        // cegos escutam rapido
        self.last_spoken: str = ""
        self.last_spoken_time: float = 0
        self.min_interval_s: float = 1.5   // minimo entre falas (evita spam)
        self.message_queue: deque = deque(maxlen=50)
        self.priority_queue: deque = deque(maxlen=20)
        self.total_messages: int = 0
        self.messages_spoken: int = 0
        self.messages_skipped: int = 0

    funcao speak(self, message: str, priority: DangerLevel = DangerLevel.SAFE) retorna Dict[str, Any]:
        // Envia mensagem para o fone. Retorna se falou ou nao.
        now <- time.time()
        self.total_messages += 1

        // Alertas criticos sempre passam
        is_critical <- priority in (DangerLevel.DANGER, DangerLevel.CRITICAL)

        // Evitar repetir a mesma coisa
        se message == self.last_spoken  E  NAO  is_critical entao:
            se now - self.last_spoken_time < 5.0 entao:
                self.messages_skipped += 1
                retorne {"spoken": FALSO, "reason": "duplicada"}

        // Respeitar intervalo minimo (exceto criticos)
        se NAO  is_critical  E  now - self.last_spoken_time < self.min_interval_s entao:
            self.message_queue.append(message)
            self.messages_skipped += 1
            retorne {"spoken": FALSO, "reason": "intervalo"}

        se is_critical entao:
            self.priority_queue.appendleft(message)
        senao:
            self.message_queue.append(message)

        self.last_spoken = message
        self.last_spoken_time = now
        self.messages_spoken += 1

        retorne {
            "spoken": VERDADEIRO,
            "message": message,
            "priority": priority.value,
            "device": self.device_name,
            "volume": self.volume,
            "rate": self.tts_rate,
        }

    funcao process_queue(self) retorna List[str]:
        // Processa fila de mensagens pendentes.
        spoken <- []
        now <- time.time()
        se now - self.last_spoken_time >= self.min_interval_s entao:
            enquanto self.priority_queue faca:
                msg <- self.priority_queue.popleft()
                spoken.append(msg)
                self.last_spoken = msg
                self.last_spoken_time = now
                self.messages_spoken += 1
                interrompa
            se NAO  spoken  E  self.message_queue entao:
                msg <- self.message_queue.popleft()
                spoken.append(msg)
                self.last_spoken = msg
                self.last_spoken_time = now
                self.messages_spoken += 1
        retorne spoken

    funcao status(self) retorna Dict[str, Any]:
        retorne {
            "connected": self.connected,
            "device": self.device_name,
            "battery_pct": self.battery_pct,
            "volume": self.volume,
            "tts_rate": self.tts_rate,
            "queue_size": len(self.message_queue),
            "priority_queue_size": len(self.priority_queue),
            "total_messages": self.total_messages,
            "spoken": self.messages_spoken,
            "skipped": self.messages_skipped,
        }


// ============================================================================
// 5. NAVEGACAO POR VOZ (Co-piloto de rua)
// ============================================================================

classe StreetNavigator:
    // 
    Sistema de navegacao por voz para cego andando na rua.
    Combina GPS + camera + bussola para guiar passo a passo.
    // 

    funcao __init__(self):
        self.destination: str = ""
        self.current_step: int = 0
        self.steps: List[Dict[str, str]] = []
        self.last_instruction: str = ""
        self.distance_remaining_m: float = 0
        self.eta_minutes: float = 0

    funcao set_destination(self, destination: str, steps: List[Dict[str, str]] = None) retorna str:
        // Define destino e calcula rota.
        self.destination = destination
        self.current_step = 0
        self.steps = steps  OU  self._default_route(destination)
        self.distance_remaining_m = sum(s.get("distance_m", 100) for s in self.steps)
        self.eta_minutes = self.distance_remaining_m / 80   // ~80m/min a pe
        retorne f"Rota calculada para {destination}. {self.distance_remaining_m:.0f} metros. Aproximadamente {self.eta_minutes:.0f} minutos."

    funcao _default_route(self, destination: str) retorna List[Dict[str, str]]:
        // Rota padrao simulada.
        retorne [
            {"instruction": "Saida do predio. Vire a direita na calcada.", "distance_m": 50},
            {"instruction": "Continue reto por 200 metros na rua Augusta.", "distance_m": 200},
            {"instruction": "Atencao: buraco a frente. Desvie a esquerda.", "distance_m": 5, "warning": VERDADEIRO},
            {"instruction": "Semaforo a frente. Aguarde se vermelho.", "distance_m": 30},
            {"instruction": "Atravesse a faixa. 15 passos.", "distance_m": 15},
            {"instruction": "Vire a direita na rua Paulista.", "distance_m": 10},
            {"instruction": f"Destino: {destination}. A esquerda, porta azul.", "distance_m": 50, "arrival": VERDADEIRO},
        ]

    funcao next_instruction(self) retorna str:
        // Proxima instrucao de navegacao.
        se self.current_step >= len(self.steps) entao:
            retorne "Voce chegou ao destino."

        step <- self.steps[self.current_step]
        instruction <- step["instruction"]
        self.last_instruction = instruction
        self.current_step += 1
        retorne instruction

    funcao detect_obstacle_ahead(self) retorna Optional[str]:
        // Detecta obstaculo imediato e retorna aviso.
        obstacles <- [
            "Poste a frente, 3 metros. Desvie a direita.",
            "Buraco na calcada, 2 metros. Cuidado ao pisar.",
            "Carro mal estacionado bloqueando calcada. Desvie pela rua com cuidado.",
            "Pessoa parada a frente, 1 metro. 'Com licenca.'",
            "Degrau descendo, 1 metro. Passo menor.",
            "Raiz de arvore na calcada. Atencao ao pe esquerdo.",
        ]
        retorne obstacles[self.current_step % len(obstacles)] if self.current_step < len(obstacles) else nulo

    funcao arrival_message(self) retorna str:
        // Mensagem de chegada.
        retorne f"Voce chegou em {self.destination}. Esta a sua frente. Parabens!"


// ============================================================================
// 6. SISTEMA PRINCIPAL -- BodyCamera Controller
// ============================================================================

classe BodyCameraController:
    // 
    Orquestra smartphone-camera + fone-bluetooth para dar visao ao cego.

    Uso:
        cam <- BodyCameraController(MountPosition.CHEST)
        cam.start()
        scene <- cam.describe()  // ouve descricao da cena
        cam.navigate("padaria")          // co-piloto ate o destino
        cam.read_text()                  // OCR de placa/menu
        cam.identify_money()             // qual nota e essa?
    // 

    def __init__(self, mount: MountPosition = MountPosition.CHEST,
                 declare verbosity: VerbosityLevel  <- VerbosityLevel.MEDIUM):
        self.mount = mount
        self.verbosity = verbosity
        self.vision = VisionEngine(mount)
        self.audio = AudioOutputManager()
        self.navigator = StreetNavigator()
        self.mode: CameraMode = CameraMode.CONTINUOUS
        self.active: bool = FALSO
        self.session_start: float = 0
        self.total_descriptions: int = 0
        self.total_alerts: int = 0
        self.battery_pct: float = 100.0
        self.battery_drain_per_hour: float = 18.0   // camera+IA = 18%/h
        self.emergency_contact: str = ""

    funcao start(self) retorna Dict[str, Any]:
        // Inicia a camera corporal.
        self.active = VERDADEIRO
        self.session_start = time.time()
        self.mode = CameraMode.CONTINUOUS
        greeting <- self.audio.speak(
            f"Camera corporal ativa. Montagem: {self.mount.value}. "
            f"Modo: continuo. Fone conectado: {self.audio.device_name}. "
            f"Estou vendo por voce.",
            DangerLevel.SAFE
        )
        retorne {
            "active": VERDADEIRO,
            "mount": self.mount.value,
            "mode": self.mode.value,
            "audio": self.audio.status(),
            "greeting": greeting,
        }

    funcao stop(self) retorna Dict[str, Any]:
        // Para a camera.
        duration <- time.time() - self.session_start if self.session_start else 0
        self.active = FALSO
        self.audio.speak("Camera desligada. Ate logo.", DangerLevel.SAFE)
        retorne {
            "active": FALSO,
            "session_duration_min": duration / 60,
            "total_descriptions": self.total_descriptions,
            "total_alerts": self.total_alerts,
        }

    funcao describe(self) retorna str:
        // Descreve a cena atual para o usuario.
        se NAO  self.active entao:
            retorne "Camera desligada."
        detections <- self.vision.process_frame(self.mode)
        description <- self.vision.describe_scene(detections, self.verbosity)
        result <- self.audio.speak(description, DangerLevel.SAFE)
        self.total_descriptions += 1
        retorne description

    funcao describe_continuous(self, frames: int = 5, interval_s: float = 2.0) retorna List[str]:
        // Simula descricao continua por N frames.
        descriptions <- []
        para cada _ em range(frames):
            desc <- self.describe()
            descriptions.append(desc)
            time.sleep(interval_s)   // simulacao
        retorne descriptions

    funcao navigate(self, destination: str) retorna str:
        // Inicia co-piloto de rua ate o destino.
        self.mode = CameraMode.NAVIGATION
        route_msg <- self.navigator.set_destination(destination)
        self.audio.speak(route_msg, DangerLevel.SAFE)
        first_step <- self.navigator.next_instruction()
        self.audio.speak(first_step, DangerLevel.ATTENTION)
        retorne f"{route_msg}\n{first_step}"

    funcao navigate_step(self) retorna str:
        // Proxima instrucao de navegacao.
        instruction <- self.navigator.next_instruction()
        self.audio.speak(instruction, DangerLevel.ATTENTION)

        // Verificar obstaculo
        obstacle <- self.navigator.detect_obstacle_ahead()
        se obstacle entao:
            self.audio.speak(obstacle, DangerLevel.WARNING)
            self.total_alerts += 1
            retorne f"{instruction}\nALERTA: {obstacle}"
        retorne instruction

    funcao read_text(self) retorna str:
        // Modo leitura: OCR de textos.
        self.mode = CameraMode.READING
        detections <- self.vision.process_frame(CameraMode.READING)
        texts <- [d.voice_description for d in detections if d.object_type == ObjectType.TEXT]
        result <- " ".join(texts) if texts else "Nao encontrei texto legivel."
        self.audio.speak(result, DangerLevel.SAFE)
        self.total_descriptions += 1
        retorne result

    funcao identify_money(self) retorna str:
        // Modo dinheiro: reconhece cedula.
        self.mode = CameraMode.MONEY
        detections <- self.vision.process_frame(CameraMode.MONEY)
        money <- [d.voice_description for d in detections if d.object_type == ObjectType.MONEY]
        result <- money[0] if money else "Nao reconheci nenhuma cedula."
        self.audio.speak(result, DangerLevel.SAFE)
        retorne result

    funcao identify_color(self) retorna str:
        // Modo cor: identifica cor a frente.
        self.mode = CameraMode.COLOR
        detections <- self.vision.process_frame(CameraMode.COLOR)
        colors <- [d.voice_description for d in detections]
        result <- colors[0] if colors else "Nao consegui identificar a cor."
        self.audio.speak(result, DangerLevel.SAFE)
        retorne result

    funcao recognize_face(self) retorna str:
        // Modo rosto: quem esta a frente.
        self.mode = CameraMode.FACE
        detections <- self.vision.process_frame(CameraMode.FACE)
        faces <- [d.voice_description for d in detections if d.object_type == ObjectType.PERSON]
        result <- faces[0] if faces else "Nao reconheci ninguem a frente."
        self.audio.speak(result, DangerLevel.SAFE)
        retorne result

    funcao search_object(self, object_name: str = "") retorna str:
        // Modo busca: procura objeto especifico.
        self.mode = CameraMode.SEARCH
        detections <- self.vision.process_frame(CameraMode.SEARCH)
        found <- [d.voice_description for d in detections]
        se found entao:
            result <- found[0]
        senao:
            result <- f"Nao encontrei {object_name}. Aponte a camera para outra direcao."
        self.audio.speak(result, DangerLevel.SAFE)
        retorne result

    funcao alert_emergency(self, description: str = "Situacao de emergencia") retorna str:
        // Alerta de emergencia.
        self.total_alerts += 1
        msg <- f"EMERGENCIA. {description}. Vou avisar seu contato."
        self.audio.speak(msg, DangerLevel.CRITICAL)
        retorne msg

    funcao check_battery(self) retorna Dict[str, Any]:
        // Verifica bateria do smartphone + fone.
        se self.active  E  self.session_start entao:
            hours <- (time.time() - self.session_start) / 3600
            self.battery_pct = max(0, 100 - (hours * self.battery_drain_per_hour))
        retorne {
            "phone_battery_pct": self.battery_pct,
            "headphone_battery_pct": self.audio.battery_pct,
            "estimated_remaining_h": self.battery_pct / self.battery_drain_per_hour if self.battery_drain_per_hour > 0 else 0,
            "low_battery": self.battery_pct < 20,
            "critical_battery": self.battery_pct < 5,
        }

    funcao set_mode(self, mode: CameraMode) retorna str:
        // Muda modo de operacao.
        self.mode = mode
        mode_names <- {
            CameraMode.CONTINUOUS: "Continuo. Vou descrever tudo.",
            CameraMode.ON_DEMAND: "Sob demanda. Pergunte quando quiser.",
            CameraMode.ALERT_ONLY: "So alertas. So falo em perigo.",
            CameraMode.NAVIGATION: "Navegacao. Vou guiar voce.",
            CameraMode.READING: "Leitura. Aponte para o texto.",
            CameraMode.MONEY: "Dinheiro. Mostre a cedula.",
            CameraMode.COLOR: "Cor. Aponte para a cor.",
            CameraMode.FACE: "Reconhecimento. Olhe para a pessoa.",
            CameraMode.SEARCH: "Busca. O que procura?",
            CameraMode.MINIMAL: "Minimal. So o essencial.",
        }
        msg <- mode_names.get(mode, "Modo alterado.")
        self.audio.speak(msg, DangerLevel.SAFE)
        retorne msg

    funcao set_verbosity(self, level: VerbosityLevel) retorna str:
        // Muda nivel de verbosidade.
        self.verbosity = level
        msgs <- {
            VerbosityLevel.HIGH: "Detalhe alto. Vou descrever tudo.",
            VerbosityLevel.MEDIUM: "Detalhe medio. O essencial.",
            VerbosityLevel.LOW: "Detalhe baixo. So alertas.",
            VerbosityLevel.WHISPER: "Minimal. So perigos criticos.",
        }
        msg <- msgs.get(level, "Verbosidade alterada.")
        self.audio.speak(msg, DangerLevel.SAFE)
        retorne msg

    funcao status(self) retorna Dict[str, Any]:
        // Status completo do sistema.
        retorne {
            "active": self.active,
            "mount": self.mount.value,
            "mode": self.mode.value,
            "verbosity": self.verbosity.value,
            "battery": self.check_battery(),
            "audio": self.audio.status(),
            "vision_frames": self.vision.frame_count,
            "total_descriptions": self.total_descriptions,
            "total_alerts": self.total_alerts,
            "destination": self.navigator.destination,
            "nav_step": self.navigator.current_step,
        }


// ============================================================================
// 7. CENARIOS DO MUNDO REAL
// ============================================================================

funcao scenario_walking_to_destination():
    // Cenario: cego andando ate a padaria.
    print("=" * 65)
    print("CENARIO 1: Cego andando ate a padaria")
    print("=" * 65)

    cam <- BodyCameraController(MountPosition.CHEST, VerbosityLevel.MEDIUM)
    start <- cam.start()
    print(f"\n[{start['greeting']['message']}]")

    // Navegar
    print(f"\n[NAVEGACAO]")
    route <- cam.navigate("Padaria do Joao")
    print(f"  {route}")

    // Passo a passo
    para cada i em range(4):
        print(f"\n[Passo {i+1}]")
        instruction <- cam.navigate_step()
        print(f"  {instruction}")


funcao scenario_reading_menu():
    // Cenario: cego lendo cardapio.
    print(f"\n{'=' * 65}")
    print("CENARIO 2: Cego lendo cardapio de restaurante")
    print("=" * 65)

    cam <- BodyCameraController()
    cam.start()
    print(f"\n[MODO LEITURA]")
    text <- cam.read_text()
    print(f"  Camera leu: {text}")


funcao scenario_identifying_money():
    // Cenario: cego reconhecendo cedula.
    print(f"\n{'=' * 65}")
    print("CENARIO 3: Cego reconhecendo dinheiro")
    print("=" * 65)

    cam <- BodyCameraController()
    cam.start()
    print(f"\n[MODO DINHEIRO]")
    money <- cam.identify_money()
    print(f"  Camera identificou: {money}")


funcao scenario_crossing_street():
    // Cenario: cego atravessando rua com semaforo.
    print(f"\n{'=' * 65}")
    print("CENARIO 4: Cego atravessando a rua")
    print("=" * 65)

    cam <- BodyCameraController()
    cam.start()
    cam.set_mode(CameraMode.NAVIGATION)

    print(f"\n[Cena 1: Chegando no semaforo]")
    desc <- cam.describe()
    print(f"  {desc}")

    print(f"\n[Cena 2: Semaforo]")
    color <- cam.identify_color()
    print(f"  {color}")

    print(f"\n[Cena 3: Atravesando]")
    desc <- cam.describe()
    print(f"  {desc}")


funcao scenario_meeting_person():
    // Cenario: cego encontrando pessoa conhecida.
    print(f"\n{'=' * 65}")
    print("CENARIO 5: Cego reconhecendo pessoa a frente")
    print("=" * 65)

    cam <- BodyCameraController()
    cam.start()
    print(f"\n[MODO ROSTO]")
    face <- cam.recognize_face()
    print(f"  {face}")


funcao scenario_searching_object():
    // Cenario: cego procurando chave.
    print(f"\n{'=' * 65}")
    print("CENARIO 6: Cego procurando objeto perdido")
    print("=" * 65)

    cam <- BodyCameraController()
    cam.start()
    print(f"\n[MODO BUSCA: 'minha chave']")
    result <- cam.search_object("minha chave")
    print(f"  {result}")


funcao scenario_battery_management():
    // Cenario: gerenciamento de bateria em caminhada longa.
    print(f"\n{'=' * 65}")
    print("CENARIO 7: Bateria em caminhada longa")
    print("=" * 65)

    cam <- BodyCameraController()
    cam.start()

    print(f"\n[Inicio da caminhada]")
    battery <- cam.check_battery()
    print(f"  Celular: {battery['phone_battery_pct']:.0f}%")
    print(f"  Fone: {battery['headphone_battery_pct']:.0f}%")
    print(f"  Autonomia estimada: {battery['estimated_remaining_h']:.1f}h")

    // Simular 3 horas de uso
    cam.session_start = time.time() - 3 * 3600
    print(f"\n[Apos 3 horas de uso]")
    battery <- cam.check_battery()
    print(f"  Celular: {battery['phone_battery_pct']:.0f}%")
    print(f"  Fone: {battery['headphone_battery_pct']:.0f}%")
    print(f"  Restante: {battery['estimated_remaining_h']:.1f}h")

    se battery["low_battery"] entao:
        print(f"  AVISO: Bateria baixa. Modo survival.")


funcao scenario_continuous_description():
    // Cenario: descricao continua enquanto anda.
    print(f"\n{'=' * 65}")
    print("CENARIO 8: Descricao continua andando na rua")
    print("=" * 65)

    cam <- BodyCameraController(MountPosition.CHEST, VerbosityLevel.MEDIUM)
    cam.start()

    print(f"\n[Descricao continua - 5 frames]")
    para cada i em range(5):
        desc <- cam.describe()
        print(f"  Frame {i+1}: {desc}")
        time.sleep(0.1)   // simulacao rapida


// ============================================================================
// 8. DEMONSTRACAO
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenBodyCamera -- Smartphone Corporal + Fone BT = Olhos do Cego")
    print("=" * 70)

    print(f"\nMontagens: {len(MountPosition)}")
    para cada m em MountPosition:
        print(f"  {m.value}")

    print(f"\nModos de camera: {len(CameraMode)}")
    para cada m em CameraMode:
        print(f"  {m.value}")

    print(f"\nVerbosidade: {len(VerbosityLevel)}")
    para cada v em VerbosityLevel:
        print(f"  {v.value}")

    print(f"\nTipos de objeto: {len(ObjectType)}")
    print(f"Niveis de perigo: {len(DangerLevel)}")

    // Cenarios
    scenario_walking_to_destination()
    scenario_reading_menu()
    scenario_identifying_money()
    scenario_crossing_street()
    scenario_meeting_person()
    scenario_searching_object()
    scenario_continuous_description()
    scenario_battery_management()

    // Status final
    cam <- BodyCameraController()
    cam.start()
    cam.describe()
    cam.navigate("teste")
    status <- cam.status()
    print(f"\n{'=' * 70}")
    print("STATUS DO SISTEMA")
    print(f"{'=' * 70}")
    print(f"  Ativo: {status['active']}")
    print(f"  Montagem: {status['mount']}")
    print(f"  Modo: {status['mode']}")
    print(f"  Verbosidade: {status['verbosity']}")
    print(f"  Frames processados: {status['vision_frames']}")
    print(f"  Descricoes geradas: {status['total_descriptions']}")
    print(f"  Alertas emitidos: {status['total_alerts']}")
    print(f"  Audio: {status['audio']['connected']}")

    cam.stop()

    print(f"\n{'=' * 70}")
    print("RESUMO")
    print(f"{'=' * 70}")
    print()
    print("  O smartphone vira OLHOS.")
    print("  O fone bluetooth vira VOZ que descreve.")
    print("  O cego ANDA na rua com INFORMACAO.")
    print("  NADA o para. NINGUEM o limita.")
    print()
    print("  Camera no peito. Fone no ouvido. Mundo na mente.")
    print("  O cego VE.")
    print()
    print("  Integrado com:")
    print("    OpenTelefonista (conversa natural)")
    print("    OpenInclusiveHardware (44 dispositivos)")
    print("    OpenResilience (bateria/falhas)")
    print("    OpenHumanNet (emergencia)")


se __name__ == "__main__" entao:
    demo()

```
