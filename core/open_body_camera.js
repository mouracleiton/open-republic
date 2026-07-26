// open_body_camera.js
// Transpilado de Python para JavaScript - OpenRepublic Project
// Smartphone como Camera Corporal + Fone Bluetooth = Olhos do Cego
// Comentarios em Portugues mantidos exatamente como no original

// ============================================================================
// 1. TIPOS DE MONTAGEM (Como o smartphone fica no corpo)
// ============================================================================

const MountPosition = Object.freeze({
    CHEST: "peito",              // clipped na camisa, no peito -- padrao
    HEAD: "cabeca",              // bandana/oculos com smartphone
    SHOULDER: "ombro",           // alca de mochila
    NECK: "pescoco",             // pendurado no pescoco
    HAND: "mao",                 // na mao apontando
    POCKET_FACING_OUT: "bolso_frente",  // no bolso com camera pra fora
    ARMBAND: "braceaco",         // bracelete de braco
});

const CameraMode = Object.freeze({
    CONTINUOUS: "continuo",           // descreve tudo o tempo todo
    ON_DEMAND: "sob_demanda",         // so quando usuario pede
    ALERT_ONLY: "so_alerta",          // so perigos
    NAVIGATION: "navegacao",          // co-piloto de rua
    READING: "leitura",               // modo OCR (ler texto)
    MONEY: "dinheiro",                // reconhecer cedulas
    COLOR: "cor",                     // identificar cores
    FACE: "rosto",                    // reconhecer pessoas
    SEARCH: "busca",                  // procurar objeto especifico
    MINIMAL: "minimal",               // tateando (hiper-minimal)
});

const VerbosityLevel = Object.freeze({
    HIGH: "alto",           // descreve tudo em detalhe
    MEDIUM: "medio",        // descreve o essencial
    LOW: "baixo",           // so alertas e orientacao
    WHISPER: "sussurro",    // minimo possivel (1 palavra)
});

// ============================================================================
// 2. DETECCOES VISUAIS
// ============================================================================

const ObjectType = Object.freeze({
    OBSTACLE: "obstaculo",
    PERSON: "pessoa",
    VEHICLE: "veiculo",
    ANIMAL: "animal",
    SIGN: "placa",
    DOOR: "porta",
    STAIRS: "escada",
    CROSSWALK: "faixa",
    TRAFFIC_LIGHT: "semaforo",
    TEXT: "texto",
    MONEY: "dinheiro",
    PRODUCT: "produto",
    FOOD: "comida",
    MEDICINE: "remedio",
    FURNITURE: "movel",
    TOOL: "ferramenta",
    NATURE: "natureza",
});

const DangerLevel = Object.freeze({
    SAFE: "seguro",
    ATTENTION: "atencao",
    WARNING: "aviso",
    DANGER: "perigo",
    CRITICAL: "critico",
});

class Detection {
    constructor(objectType, label, distanceM, direction, danger, confidence,
                action = "", voiceDescription = "", size = "", moving = false, approaching = false) {
        this.objectType = objectType;
        this.label = label;
        this.distanceM = distanceM;
        this.direction = direction;
        this.danger = danger;
        this.confidence = confidence;
        this.action = action;
        this.voiceDescription = voiceDescription;
        this.timestamp = Date.now();
        this.size = size;
        this.moving = moving;
        this.approaching = approaching;
    }
}

// ============================================================================
// 3. MOTOR DE VISAO COMPUTACIONAL
// ============================================================================

class VisionEngine {
    constructor(mount = MountPosition.CHEST) {
        this.mount = mount;
        this.detectionsHistory = [];
        this.lastScene = "";
        this.frameCount = 0;
        this.fps = 15.0;
        this.processingLatencyMs = 80;
    }

    processFrame(mode = CameraMode.CONTINUOUS) {
        this.frameCount++;
        let detections = [];

        if (mode === CameraMode.NAVIGATION) detections = this._scanNavigation();
        else if (mode === CameraMode.READING) detections = this._scanText();
        else if (mode === CameraMode.MONEY) detections = this._scanMoney();
        else if (mode === CameraMode.COLOR) detections = this._scanColor();
        else if (mode === CameraMode.FACE) detections = this._scanFaces();
        else if (mode === CameraMode.SEARCH) detections = this._scanSearch();
        else detections = this._scanContinuous();

        for (const d of detections) {
            this.detectionsHistory.push(d);
            if (this.detectionsHistory.length > 200) this.detectionsHistory.shift();
        }
        return detections;
    }

    _scanContinuous() {
        return [
            new Detection(ObjectType.PERSON, "Pessoa", 3.0, "frente", DangerLevel.SAFE, 0.92,
                "Pessoa a 3 metros a frente.", "Pessoa a frente, 3 metros.", "", true, false),
            new Detection(ObjectType.OBSTACLE, "Poste", 5.0, "frente-esquerda", DangerLevel.ATTENTION, 0.88,
                "Poste a 5 metros. Mantenha a direita.", "Poste a esquerda, 5 metros."),
            new Detection(ObjectType.VEHICLE, "Carro estacionado", 2.5, "direita", DangerLevel.SAFE, 0.95,
                "", "Carro estacionado a direita."),
        ];
    }

    _scanNavigation() {
        return [
            new Detection(ObjectType.CROSSWALK, "Faixa de pedestre", 8.0, "frente", DangerLevel.SAFE, 0.90,
                "Continue reto. Faixa de pedestre em 8 metros.", "Faixa de pedestre a frente, 8 metros. Continue reto."),
            new Detection(ObjectType.TRAFFIC_LIGHT, "Semaforo", 8.0, "frente-alto", DangerLevel.SAFE, 0.97,
                "Semaforo VERDE. Pode atravessar.", "Semaforo verde. Pode atravessar."),
            new Detection(ObjectType.OBSTACLE, "Buraco na calcada", 4.0, "frente-baixo", DangerLevel.WARNING, 0.85,
                "Buraco a 4 metros. Desvie para a esquerda.", "Atencao! Buraco na calcada, 4 metros. Desvie a esquerda."),
        ];
    }

    _scanText() {
        return [
            new Detection(ObjectType.TEXT, "Placa de estabelecimento", 5.0, "frente-alto", DangerLevel.SAFE, 0.91,
                "", "A placa diz: RESTAURANTE DO JOAO. Aberto das 11 as 22."),
            new Detection(ObjectType.TEXT, "Cardapio", 3.0, "frente", DangerLevel.SAFE, 0.88,
                "", "O cardapio diz: Feijoada R$ 25. Suco R$ 8. Prato feito R$ 18."),
        ];
    }

    _scanMoney() {
        return [
            new Detection(ObjectType.MONEY, "Nota de R$ 50", 0.5, "frente", DangerLevel.SAFE, 0.96,
                "", "Nota de CINQUENTA REAIS. Cor marrom."),
        ];
    }

    _scanColor() {
        return [
            new Detection(ObjectType.SIGN, "Sinal vermelho", 10.0, "frente-alto", DangerLevel.DANGER, 0.97,
                "Semaforo VERMELHO. PARE.", "Semaforo VERMELHO. Pare."),
        ];
    }

    _scanFaces() {
        return [
            new Detection(ObjectType.PERSON, "MING (esposa)", 2.0, "frente", DangerLevel.SAFE, 0.89,
                "", "MING esta a sua frente, 2 metros. Sorrindo."),
        ];
    }

    _scanSearch() {
        return [
            new Detection(ObjectType.PRODUCT, "Chave", 1.5, "mesa", DangerLevel.SAFE, 0.82,
                "", "Encontrei a chave. Esta na mesa, a sua frente, 1 metro e meio."),
        ];
    }

    describeScene(detections, verbosity = VerbosityLevel.MEDIUM) {
        if (!detections || detections.length === 0) {
            return verbosity === VerbosityLevel.WHISPER ? "Livre." : "Nada a frente. Caminho livre.";
        }

        const sorted = [...detections].sort((a, b) => {
            const rankDiff = this._dangerRank(b.danger) - this._dangerRank(a.danger);
            return rankDiff !== 0 ? rankDiff : a.distanceM - b.distanceM;
        });

        const descriptions = [];
        for (const d of sorted) {
            if (verbosity === VerbosityLevel.HIGH) {
                descriptions.push(d.voiceDescription);
            } else if (verbosity === VerbosityLevel.MEDIUM) {
                let desc = d.voiceDescription;
                if (desc.length > 60) desc = desc.substring(0, 57) + "...";
                descriptions.push(desc);
            } else if (verbosity === VerbosityLevel.LOW) {
                if ([DangerLevel.WARNING, DangerLevel.DANGER, DangerLevel.CRITICAL].includes(d.danger)) {
                    descriptions.push(d.voiceDescription);
                }
            } else if (verbosity === VerbosityLevel.WHISPER) {
                if ([DangerLevel.DANGER, DangerLevel.CRITICAL].includes(d.danger)) {
                    descriptions.push(d.action || d.label);
                }
            }
        }
        return descriptions.length ? descriptions.join(". ") + "." : "Livre.";
    }

    _dangerRank(dl) {
        if (dl === DangerLevel.CRITICAL) return 5;
        if (dl === DangerLevel.DANGER) return 4;
        if (dl === DangerLevel.WARNING) return 3;
        if (dl === DangerLevel.ATTENTION) return 2;
        return 1;
    }
}

// ============================================================================
// 4. GERENCIADOR DE AUDIO BLUETOOTH
// ============================================================================

class AudioOutputManager {
    constructor() {
        this.connected = true;
        this.deviceName = "Fone Bluetooth";
        this.batteryPct = 100.0;
        this.volume = 0.7;
        this.ttsRate = 1.4;
        this.lastSpoken = "";
        this.lastSpokenTime = 0;
        this.minIntervalS = 1.5;
        this.messageQueue = [];
        this.priorityQueue = [];
        this.totalMessages = 0;
        this.messagesSpoken = 0;
        this.messagesSkipped = 0;
    }

    speak(message, priority = DangerLevel.SAFE) {
        const now = Date.now();
        this.totalMessages++;
        const isCritical = [DangerLevel.DANGER, DangerLevel.CRITICAL].includes(priority);

        if (message === this.lastSpoken && !isCritical) {
            if ((now - this.lastSpokenTime) / 1000 < 5.0) {
                this.messagesSkipped++;
                return { spoken: false, reason: "duplicada" };
            }
        }

        if (!isCritical && (now - this.lastSpokenTime) / 1000 < this.minIntervalS) {
            this.messageQueue.push(message);
            this.messagesSkipped++;
            return { spoken: false, reason: "intervalo" };
        }

        if (isCritical) this.priorityQueue.unshift(message);
        else this.messageQueue.push(message);

        this.lastSpoken = message;
        this.lastSpokenTime = now;
        this.messagesSpoken++;

        return {
            spoken: true, message, priority: priority,
            device: this.deviceName, volume: this.volume, rate: this.ttsRate
        };
    }

    processQueue() {
        const spoken = [];
        const now = Date.now();
        if ((now - this.lastSpokenTime) / 1000 >= this.minIntervalS) {
            if (this.priorityQueue.length) {
                const msg = this.priorityQueue.shift();
                spoken.push(msg);
                this.lastSpoken = msg;
                this.lastSpokenTime = now;
                this.messagesSpoken++;
            } else if (this.messageQueue.length) {
                const msg = this.messageQueue.shift();
                spoken.push(msg);
                this.lastSpoken = msg;
                this.lastSpokenTime = now;
                this.messagesSpoken++;
            }
        }
        return spoken;
    }

    status() {
        return {
            connected: this.connected, device: this.deviceName, battery_pct: this.batteryPct,
            volume: this.volume, tts_rate: this.ttsRate,
            queue_size: this.messageQueue.length, priority_queue_size: this.priorityQueue.length,
            total_messages: this.totalMessages, spoken: this.messagesSpoken, skipped: this.messagesSkipped
        };
    }
}

// ============================================================================
// 5. NAVEGACAO POR VOZ (Co-piloto de rua)
// ============================================================================

class StreetNavigator {
    constructor() {
        this.destination = "";
        this.currentStep = 0;
        this.steps = [];
        this.lastInstruction = "";
        this.distanceRemainingM = 0;
        this.etaMinutes = 0;
    }

    setDestination(destination, steps = null) {
        this.destination = destination;
        this.currentStep = 0;
        this.steps = steps && steps.length ? steps : this._defaultRoute(destination);
        this.distanceRemainingM = this.steps.reduce((sum, s) => sum + (s.distance_m || 100), 0);
        this.etaMinutes = this.distanceRemainingM / 80;
        return `Rota calculada para ${destination}. ${Math.round(this.distanceRemainingM)} metros. Aproximadamente ${Math.round(this.etaMinutes)} minutos.`;
    }

    _defaultRoute(destination) {
        return [
            { instruction: "Saida do predio. Vire a direita na calcada.", distance_m: 50 },
            { instruction: "Continue reto por 200 metros na rua Augusta.", distance_m: 200 },
            { instruction: "Atencao: buraco a frente. Desvie a esquerda.", distance_m: 5, warning: true },
            { instruction: "Semaforo a frente. Aguarde se vermelho.", distance_m: 30 },
            { instruction: "Atravesse a faixa. 15 passos.", distance_m: 15 },
            { instruction: "Vire a direita na rua Paulista.", distance_m: 10 },
            { instruction: `Destino: ${destination}. A esquerda, porta azul.`, distance_m: 50, arrival: true },
        ];
    }

    nextInstruction() {
        if (this.currentStep >= this.steps.length) return "Voce chegou ao destino.";
        const step = this.steps[this.currentStep];
        const instruction = step.instruction;
        this.lastInstruction = instruction;
        this.currentStep++;
        return instruction;
    }

    detectObstacleAhead() {
        const obstacles = [
            "Poste a frente, 3 metros. Desvie a direita.",
            "Buraco na calcada, 2 metros. Cuidado ao pisar.",
            "Carro mal estacionado bloqueando calcada. Desvie pela rua com cuidado.",
            "Pessoa parada a frente, 1 metro. 'Com licenca.'",
            "Degrau descendo, 1 metro. Passo menor.",
            "Raiz de arvore na calcada. Atencao ao pe esquerdo.",
        ];
        return this.currentStep < obstacles.length ? obstacles[this.currentStep % obstacles.length] : null;
    }

    arrivalMessage() {
        return `Voce chegou em ${this.destination}. Esta a sua frente. Parabens!`;
    }
}

// ============================================================================
// 6. SISTEMA PRINCIPAL -- BodyCamera Controller
// ============================================================================

class BodyCameraController {
    constructor(mount = MountPosition.CHEST, verbosity = VerbosityLevel.MEDIUM) {
        this.mount = mount;
        this.verbosity = verbosity;
        this.vision = new VisionEngine(this.mount);
        this.audio = new AudioOutputManager();
        this.navigator = new StreetNavigator();
        this.mode = CameraMode.CONTINUOUS;
        this.active = false;
        this.sessionStart = 0;
        this.totalDescriptions = 0;
        this.totalAlerts = 0;
        this.batteryPct = 100.0;
        this.batteryDrainPerHour = 18.0;
        this.emergencyContact = "";
    }

    start() {
        this.active = true;
        this.sessionStart = Date.now();
        this.mode = CameraMode.CONTINUOUS;
        const greeting = this.audio.speak(
            `Camera corporal ativa. Montagem: ${this.mount}. Modo: continuo. Fone conectado: ${this.audio.deviceName}. Estou vendo por voce.`,
            DangerLevel.SAFE
        );
        return { active: true, mount: this.mount, mode: this.mode, audio: this.audio.status(), greeting };
    }

    stop() {
        const duration = this.sessionStart ? (Date.now() - this.sessionStart) / 1000 / 60 : 0;
        this.active = false;
        this.audio.speak("Camera desligada. Ate logo.", DangerLevel.SAFE);
        return { active: false, session_duration_min: duration, total_descriptions: this.totalDescriptions, total_alerts: this.totalAlerts };
    }

    describe() {
        if (!this.active) return "Camera desligada.";
        const detections = this.vision.processFrame(this.mode);
        const description = this.vision.describeScene(detections, this.verbosity);
        this.audio.speak(description, DangerLevel.SAFE);
        this.totalDescriptions++;
        return description;
    }

    async describeContinuous(frames = 5, intervalS = 2.0) {
        const descriptions = [];
        for (let i = 0; i < frames; i++) {
            descriptions.push(this.describe());
            await new Promise(r => setTimeout(r, intervalS * 1000));
        }
        return descriptions;
    }

    navigate(destination) {
        this.mode = CameraMode.NAVIGATION;
        const routeMsg = this.navigator.setDestination(destination);
        this.audio.speak(routeMsg, DangerLevel.SAFE);
        const firstStep = this.navigator.nextInstruction();
        this.audio.speak(firstStep, DangerLevel.ATTENTION);
        return `${routeMsg}\n${firstStep}`;
    }

    navigateStep() {
        const instruction = this.navigator.nextInstruction();
        this.audio.speak(instruction, DangerLevel.ATTENTION);
        const obstacle = this.navigator.detectObstacleAhead();
        if (obstacle) {
            this.audio.speak(obstacle, DangerLevel.WARNING);
            this.totalAlerts++;
            return `${instruction}\nALERTA: ${obstacle}`;
        }
        return instruction;
    }

    readText() {
        this.mode = CameraMode.READING;
        const detections = this.vision.processFrame(CameraMode.READING);
        const texts = detections.filter(d => d.objectType === ObjectType.TEXT).map(d => d.voiceDescription);
        const result = texts.length ? texts.join(" ") : "Nao encontrei texto legivel.";
        this.audio.speak(result, DangerLevel.SAFE);
        this.totalDescriptions++;
        return result;
    }

    identifyMoney() {
        this.mode = CameraMode.MONEY;
        const detections = this.vision.processFrame(CameraMode.MONEY);
        const money = detections.filter(d => d.objectType === ObjectType.MONEY).map(d => d.voiceDescription);
        const result = money.length ? money[0] : "Nao reconheci nenhuma cedula.";
        this.audio.speak(result, DangerLevel.SAFE);
        return result;
    }

    identifyColor() {
        this.mode = CameraMode.COLOR;
        const detections = this.vision.processFrame(CameraMode.COLOR);
        const colors = detections.map(d => d.voiceDescription);
        const result = colors.length ? colors[0] : "Nao consegui identificar a cor.";
        this.audio.speak(result, DangerLevel.SAFE);
        return result;
    }

    recognizeFace() {
        this.mode = CameraMode.FACE;
        const detections = this.vision.processFrame(CameraMode.FACE);
        const faces = detections.filter(d => d.objectType === ObjectType.PERSON).map(d => d.voiceDescription);
        const result = faces.length ? faces[0] : "Nao reconheci ninguem a frente.";
        this.audio.speak(result, DangerLevel.SAFE);
        return result;
    }

    searchObject(objectName = "") {
        this.mode = CameraMode.SEARCH;
        const detections = this.vision.processFrame(CameraMode.SEARCH);
        const found = detections.map(d => d.voiceDescription);
        const result = found.length ? found[0] : `Nao encontrei ${objectName}. Aponte a camera para outra direcao.`;
        this.audio.speak(result, DangerLevel.SAFE);
        return result;
    }

    alertEmergency(description = "Situacao de emergencia") {
        this.totalAlerts++;
        const msg = `EMERGENCIA. ${description}. Vou avisar seu contato.`;
        this.audio.speak(msg, DangerLevel.CRITICAL);
        return msg;
    }

    checkBattery() {
        if (this.active && this.sessionStart) {
            const hours = (Date.now() - this.sessionStart) / 1000 / 3600;
            this.batteryPct = Math.max(0, 100 - hours * this.batteryDrainPerHour);
        }
        return {
            phone_battery_pct: this.batteryPct,
            headphone_battery_pct: this.audio.batteryPct,
            estimated_remaining_h: this.batteryDrainPerHour > 0 ? this.batteryPct / this.batteryDrainPerHour : 0,
            low_battery: this.batteryPct < 20,
            critical_battery: this.batteryPct < 5,
        };
    }

    setMode(mode) {
        this.mode = mode;
        const modeNames = {
            [CameraMode.CONTINUOUS]: "Continuo. Vou descrever tudo.",
            [CameraMode.ON_DEMAND]: "Sob demanda. Pergunte quando quiser.",
            [CameraMode.ALERT_ONLY]: "So alertas. So falo em perigo.",
            [CameraMode.NAVIGATION]: "Navegacao. Vou guiar voce.",
            [CameraMode.READING]: "Leitura. Aponte para o texto.",
            [CameraMode.MONEY]: "Dinheiro. Mostre a cedula.",
            [CameraMode.COLOR]: "Cor. Aponte para a cor.",
            [CameraMode.FACE]: "Reconhecimento. Olhe para a pessoa.",
            [CameraMode.SEARCH]: "Busca. O que procura?",
            [CameraMode.MINIMAL]: "Minimal. So o essencial.",
        };
        const msg = modeNames[mode] || "Modo alterado.";
        this.audio.speak(msg, DangerLevel.SAFE);
        return msg;
    }

    setVerbosity(level) {
        this.verbosity = level;
        const msgs = {
            [VerbosityLevel.HIGH]: "Detalhe alto. Vou descrever tudo.",
            [VerbosityLevel.MEDIUM]: "Detalhe medio. O essencial.",
            [VerbosityLevel.LOW]: "Detalhe baixo. So alertas.",
            [VerbosityLevel.WHISPER]: "Minimal. So perigos criticos.",
        };
        const msg = msgs[level] || "Verbosidade alterada.";
        this.audio.speak(msg, DangerLevel.SAFE);
        return msg;
    }

    status() {
        return {
            active: this.active, mount: this.mount, mode: this.mode, verbosity: this.verbosity,
            battery: this.checkBattery(), audio: this.audio.status(),
            vision_frames: this.vision.frameCount, total_descriptions: this.totalDescriptions,
            total_alerts: this.totalAlerts, destination: this.navigator.destination, nav_step: this.navigator.currentStep,
        };
    }
}

// ============================================================================
// 7. CENARIOS DO MUNDO REAL
// ============================================================================

async function scenarioWalkingToDestination() {
    console.log("=".repeat(65));
    console.log("CENARIO 1: Cego andando ate a padaria");
    console.log("=".repeat(65));
    const cam = new BodyCameraController(MountPosition.CHEST, VerbosityLevel.MEDIUM);
    const start = cam.start();
    console.log(`\n[${start.greeting.message}]`);
    console.log("\n[NAVEGACAO]");
    const route = cam.navigate("Padaria do Joao");
    console.log(`  ${route}`);
    for (let i = 0; i < 4; i++) {
        console.log(`\n[Passo ${i + 1}]`);
        const instruction = cam.navigateStep();
        console.log(`  ${instruction}`);
    }
}

async function scenarioReadingMenu() {
    console.log("\n" + "=".repeat(65));
    console.log("CENARIO 2: Cego lendo cardapio de restaurante");
    console.log("=".repeat(65));
    const cam = new BodyCameraController();
    cam.start();
    console.log("\n[MODO LEITURA]");
    const text = cam.readText();
    console.log(`  Camera leu: ${text}`);
}

async function scenarioIdentifyingMoney() {
    console.log("\n" + "=".repeat(65));
    console.log("CENARIO 3: Cego reconhecendo dinheiro");
    console.log("=".repeat(65));
    const cam = new BodyCameraController();
    cam.start();
    console.log("\n[MODO DINHEIRO]");
    const money = cam.identifyMoney();
    console.log(`  Camera identificou: ${money}`);
}

async function scenarioCrossingStreet() {
    console.log("\n" + "=".repeat(65));
    console.log("CENARIO 4: Cego atravessando a rua");
    console.log("=".repeat(65));
    const cam = new BodyCameraController();
    cam.start();
    cam.setMode(CameraMode.NAVIGATION);
    console.log("\n[Cena 1: Chegando no semaforo]");
    let desc = cam.describe();
    console.log(`  ${desc}`);
    console.log("\n[Cena 2: Semaforo]");
    const color = cam.identifyColor();
    console.log(`  ${color}`);
    console.log("\n[Cena 3: Atravesando]");
    desc = cam.describe();
    console.log(`  ${desc}`);
}

async function scenarioMeetingPerson() {
    console.log("\n" + "=".repeat(65));
    console.log("CENARIO 5: Cego reconhecendo pessoa a frente");
    console.log("=".repeat(65));
    const cam = new BodyCameraController();
    cam.start();
    console.log("\n[MODO ROSTO]");
    const face = cam.recognizeFace();
    console.log(`  ${face}`);
}

async function scenarioSearchingObject() {
    console.log("\n" + "=".repeat(65));
    console.log("CENARIO 6: Cego procurando objeto perdido");
    console.log("=".repeat(65));
    const cam = new BodyCameraController();
    cam.start();
    console.log("\n[MODO BUSCA: 'minha chave']");
    const result = cam.searchObject("minha chave");
    console.log(`  ${result}`);
}

async function scenarioBatteryManagement() {
    console.log("\n" + "=".repeat(65));
    console.log("CENARIO 7: Bateria em caminhada longa");
    console.log("=".repeat(65));
    const cam = new BodyCameraController();
    cam.start();
    console.log("\n[Inicio da caminhada]");
    let battery = cam.checkBattery();
    console.log(`  Celular: ${battery.phone_battery_pct.toFixed(0)}%`);
    console.log(`  Fone: ${battery.headphone_battery_pct.toFixed(0)}%`);
    console.log(`  Autonomia estimada: ${battery.estimated_remaining_h.toFixed(1)}h`);
    cam.sessionStart = Date.now() - 3 * 3600 * 1000;
    console.log("\n[Apos 3 horas de uso]");
    battery = cam.checkBattery();
    console.log(`  Celular: ${battery.phone_battery_pct.toFixed(0)}%`);
    console.log(`  Fone: ${battery.headphone_battery_pct.toFixed(0)}%`);
    console.log(`  Restante: ${battery.estimated_remaining_h.toFixed(1)}h`);
    if (battery.low_battery) console.log("  AVISO: Bateria baixa. Modo survival.");
}

async function scenarioContinuousDescription() {
    console.log("\n" + "=".repeat(65));
    console.log("CENARIO 8: Descricao continua andando na rua");
    console.log("=".repeat(65));
    const cam = new BodyCameraController(MountPosition.CHEST, VerbosityLevel.MEDIUM);
    cam.start();
    console.log("\n[Descricao continua - 5 frames]");
    for (let i = 0; i < 5; i++) {
        const desc = cam.describe();
        console.log(`  Frame ${i + 1}: ${desc}`);
        await new Promise(r => setTimeout(r, 100));
    }
}

// ============================================================================
// 8. DEMONSTRACAO (main)
// ============================================================================

async function demo() {
    console.log("=".repeat(70));
    console.log("OpenBodyCamera -- Smartphone Corporal + Fone BT = Olhos do Cego");
    console.log("=".repeat(70));

    console.log(`\nMontagens: ${Object.keys(MountPosition).length}`);
    for (const m of Object.values(MountPosition)) console.log(`  ${m}`);

    console.log(`\nModos de camera: ${Object.keys(CameraMode).length}`);
    for (const m of Object.values(CameraMode)) console.log(`  ${m}`);

    console.log(`\nVerbosidade: ${Object.keys(VerbosityLevel).length}`);
    for (const v of Object.values(VerbosityLevel)) console.log(`  ${v}`);

    console.log(`\nTipos de objeto: ${Object.keys(ObjectType).length}`);
    console.log(`Niveis de perigo: ${Object.keys(DangerLevel).length}`);

    await scenarioWalkingToDestination();
    await scenarioReadingMenu();
    await scenarioIdentifyingMoney();
    await scenarioCrossingStreet();
    await scenarioMeetingPerson();
    await scenarioSearchingObject();
    await scenarioContinuousDescription();
    await scenarioBatteryManagement();

    const cam = new BodyCameraController();
    cam.start();
    cam.describe();
    cam.navigate("teste");
    const status = cam.status();
    console.log("\n" + "=".repeat(70));
    console.log("STATUS DO SISTEMA");
    console.log("=".repeat(70));
    console.log(`  Ativo: ${status.active}`);
    console.log(`  Montagem: ${status.mount}`);
    console.log(`  Modo: ${status.mode}`);
    console.log(`  Verbosidade: ${status.verbosity}`);
    console.log(`  Frames processados: ${status.vision_frames}`);
    console.log(`  Descricoes geradas: ${status.total_descriptions}`);
    console.log(`  Alertas emitidos: ${status.total_alerts}`);
    console.log(`  Audio: ${status.audio.connected}`);

    cam.stop();

    console.log("\n" + "=".repeat(70));
    console.log("RESUMO");
    console.log("=".repeat(70));
    console.log();
    console.log("  O smartphone vira OLHOS.");
    console.log("  O fone bluetooth vira VOZ que descreve.");
    console.log("  O cego ANDA na rua com INFORMACAO.");
    console.log("  NADA o para. NINGUEM o limita.");
    console.log();
    console.log("  Camera no peito. Fone no ouvido. Mundo na mente.");
    console.log("  O cego VE.");
    console.log();
    console.log("  Integrado com:");
    console.log("    OpenTelefonista (conversa natural)");
    console.log("    OpenInclusiveHardware (44 dispositivos)");
    console.log("    OpenResilience (bateria/falhas)");
    console.log("    OpenHumanNet (emergencia)");
}

if (require.main === module) {
    demo().catch(console.error);
}

module.exports = {
    MountPosition, CameraMode, VerbosityLevel, ObjectType, DangerLevel,
    Detection, VisionEngine, AudioOutputManager, StreetNavigator, BodyCameraController,
    demo
};