// OpenBodyCamera.java
// Transpilado de Python para Java - OpenRepublic Project
// Smartphone como Camera Corporal + Fone Bluetooth = Olhos do Cego
// Comentarios em Portugues mantidos exatamente como no original

import java.util.*;
import java.util.concurrent.ConcurrentLinkedDeque;

// ============================================================================
// 1. TIPOS DE MONTAGEM (Como o smartphone fica no corpo)
// ============================================================================

enum MountPosition {
    CHEST("peito"),              // clipped na camisa, no peito -- padrao
    HEAD("cabeca"),              // bandana/oculos com smartphone
    SHOULDER("ombro"),           // alca de mochila
    NECK("pescoco"),             // pendurado no pescoco
    HAND("mao"),                 // na mao apontando
    POCKET_FACING_OUT("bolso_frente"),  // no bolso com camera pra fora
    ARMBAND("braceaco");         // bracelete de braco

    private final String value;
    MountPosition(String value) { this.value = value; }
    public String getValue() { return value; }
}

enum CameraMode {
    CONTINUOUS("continuo"),           // descreve tudo o tempo todo
    ON_DEMAND("sob_demanda"),         // so quando usuario pede
    ALERT_ONLY("so_alerta"),          // so perigos
    NAVIGATION("navegacao"),          // co-piloto de rua
    READING("leitura"),               // modo OCR (ler texto)
    MONEY("dinheiro"),                // reconhecer cedulas
    COLOR("cor"),                     // identificar cores
    FACE("rosto"),                    // reconhecer pessoas
    SEARCH("busca"),                  // procurar objeto especifico
    MINIMAL("minimal");               // tateando (hiper-minimal)

    private final String value;
    CameraMode(String value) { this.value = value; }
    public String getValue() { return value; }
}

enum VerbosityLevel {
    HIGH("alto"),           // descreve tudo em detalhe
    MEDIUM("medio"),        // descreve o essencial
    LOW("baixo"),           // so alertas e orientacao
    WHISPER("sussurro");    // minimo possivel (1 palavra)

    private final String value;
    VerbosityLevel(String value) { this.value = value; }
    public String getValue() { return value; }
}

// ============================================================================
// 2. DETECCOES VISUAIS
// ============================================================================

enum ObjectType {
    OBSTACLE("obstaculo"),
    PERSON("pessoa"),
    VEHICLE("veiculo"),
    ANIMAL("animal"),
    SIGN("placa"),
    DOOR("porta"),
    STAIRS("escada"),
    CROSSWALK("faixa"),
    TRAFFIC_LIGHT("semaforo"),
    TEXT("texto"),
    MONEY("dinheiro"),
    PRODUCT("produto"),
    FOOD("comida"),
    MEDICINE("remedio"),
    FURNITURE("movel"),
    TOOL("ferramenta"),
    NATURE("natureza");

    private final String value;
    ObjectType(String value) { this.value = value; }
    public String getValue() { return value; }
}

enum DangerLevel {
    SAFE("seguro"),
    ATTENTION("atencao"),
    WARNING("aviso"),
    DANGER("perigo"),
    CRITICAL("critico");

    private final String value;
    DangerLevel(String value) { this.value = value; }
    public String getValue() { return value; }
}

class Detection {
    public ObjectType objectType;
    public String label;
    public double distanceM;
    public String direction;
    public DangerLevel danger;
    public double confidence;
    public String action;
    public String voiceDescription;
    public long timestamp;
    public String size;
    public boolean moving;
    public boolean approaching;

    public Detection(ObjectType objectType, String label, double distanceM, String direction,
                     DangerLevel danger, double confidence, String action, String voiceDescription,
                     String size, boolean moving, boolean approaching) {
        this.objectType = objectType;
        this.label = label;
        this.distanceM = distanceM;
        this.direction = direction;
        this.danger = danger;
        this.confidence = confidence;
        this.action = action != null ? action : "";
        this.voiceDescription = voiceDescription != null ? voiceDescription : "";
        this.timestamp = System.currentTimeMillis();
        this.size = size != null ? size : "";
        this.moving = moving;
        this.approaching = approaching;
    }
}

// ============================================================================
// 3. MOTOR DE VISAO COMPUTACIONAL
// ============================================================================

class VisionEngine {
    public MountPosition mount;
    public Deque<Detection> detectionsHistory;
    public String lastScene;
    public int frameCount;
    public double fps;
    public double processingLatencyMs;

    public VisionEngine(MountPosition mount) {
        this.mount = mount != null ? mount : MountPosition.CHEST;
        this.detectionsHistory = new ConcurrentLinkedDeque<>();
        this.lastScene = "";
        this.frameCount = 0;
        this.fps = 15.0;
        this.processingLatencyMs = 80;
    }

    public List<Detection> processFrame(CameraMode mode) {
        this.frameCount++;
        List<Detection> detections;

        if (mode == CameraMode.NAVIGATION) {
            detections = _scanNavigation();
        } else if (mode == CameraMode.READING) {
            detections = _scanText();
        } else if (mode == CameraMode.MONEY) {
            detections = _scanMoney();
        } else if (mode == CameraMode.COLOR) {
            detections = _scanColor();
        } else if (mode == CameraMode.FACE) {
            detections = _scanFaces();
        } else if (mode == CameraMode.SEARCH) {
            detections = _scanSearch();
        } else {
            detections = _scanContinuous();
        }

        for (Detection d : detections) {
            this.detectionsHistory.addLast(d);
            if (this.detectionsHistory.size() > 200) this.detectionsHistory.pollFirst();
        }
        return detections;
    }

    private List<Detection> _scanContinuous() {
        List<Detection> list = new ArrayList<>();
        list.add(new Detection(ObjectType.PERSON, "Pessoa", 3.0, "frente",
                DangerLevel.SAFE, 0.92, "Pessoa a 3 metros a frente.",
                "Pessoa a frente, 3 metros.", "", true, false));
        list.add(new Detection(ObjectType.OBSTACLE, "Poste", 5.0, "frente-esquerda",
                DangerLevel.ATTENTION, 0.88, "Poste a 5 metros. Mantenha a direita.",
                "Poste a esquerda, 5 metros.", "", false, false));
        list.add(new Detection(ObjectType.VEHICLE, "Carro estacionado", 2.5, "direita",
                DangerLevel.SAFE, 0.95, "", "Carro estacionado a direita.", "", false, false));
        return list;
    }

    private List<Detection> _scanNavigation() {
        List<Detection> list = new ArrayList<>();
        list.add(new Detection(ObjectType.CROSSWALK, "Faixa de pedestre", 8.0, "frente",
                DangerLevel.SAFE, 0.90, "Continue reto. Faixa de pedestre em 8 metros.",
                "Faixa de pedestre a frente, 8 metros. Continue reto.", "", false, false));
        list.add(new Detection(ObjectType.TRAFFIC_LIGHT, "Semaforo", 8.0, "frente-alto",
                DangerLevel.SAFE, 0.97, "Semaforo VERDE. Pode atravessar.",
                "Semaforo verde. Pode atravessar.", "", false, false));
        list.add(new Detection(ObjectType.OBSTACLE, "Buraco na calcada", 4.0, "frente-baixo",
                DangerLevel.WARNING, 0.85, "Buraco a 4 metros. Desvie para a esquerda.",
                "Atencao! Buraco na calcada, 4 metros. Desvie a esquerda.", "", false, false));
        return list;
    }

    private List<Detection> _scanText() {
        List<Detection> list = new ArrayList<>();
        list.add(new Detection(ObjectType.TEXT, "Placa de estabelecimento", 5.0, "frente-alto",
                DangerLevel.SAFE, 0.91, "",
                "A placa diz: RESTAURANTE DO JOAO. Aberto das 11 as 22.", "", false, false));
        list.add(new Detection(ObjectType.TEXT, "Cardapio", 3.0, "frente",
                DangerLevel.SAFE, 0.88, "",
                "O cardapio diz: Feijoada R$ 25. Suco R$ 8. Prato feito R$ 18.", "", false, false));
        return list;
    }

    private List<Detection> _scanMoney() {
        List<Detection> list = new ArrayList<>();
        list.add(new Detection(ObjectType.MONEY, "Nota de R$ 50", 0.5, "frente",
                DangerLevel.SAFE, 0.96, "",
                "Nota de CINQUENTA REAIS. Cor marrom.", "", false, false));
        return list;
    }

    private List<Detection> _scanColor() {
        List<Detection> list = new ArrayList<>();
        list.add(new Detection(ObjectType.SIGN, "Sinal vermelho", 10.0, "frente-alto",
                DangerLevel.DANGER, 0.97, "Semaforo VERMELHO. PARE.",
                "Semaforo VERMELHO. Pare.", "", false, false));
        return list;
    }

    private List<Detection> _scanFaces() {
        List<Detection> list = new ArrayList<>();
        list.add(new Detection(ObjectType.PERSON, "MING (esposa)", 2.0, "frente",
                DangerLevel.SAFE, 0.89, "",
                "MING esta a sua frente, 2 metros. Sorrindo.", "", false, false));
        return list;
    }

    private List<Detection> _scanSearch() {
        List<Detection> list = new ArrayList<>();
        list.add(new Detection(ObjectType.PRODUCT, "Chave", 1.5, "mesa",
                DangerLevel.SAFE, 0.82, "",
                "Encontrei a chave. Esta na mesa, a sua frente, 1 metro e meio.", "", false, false));
        return list;
    }

    public String describeScene(List<Detection> detections, VerbosityLevel verbosity) {
        if (detections == null || detections.isEmpty()) {
            if (verbosity == VerbosityLevel.WHISPER) return "Livre.";
            return "Nada a frente. Caminho livre.";
        }

        List<Detection> sorted = new ArrayList<>(detections);
        sorted.sort(Comparator.comparingInt((Detection d) -> -dangerRank(d.danger))
                .thenComparingDouble(d -> d.distanceM));

        List<String> descriptions = new ArrayList<>();
        for (Detection d : sorted) {
            if (verbosity == VerbosityLevel.HIGH) {
                descriptions.add(d.voiceDescription);
            } else if (verbosity == VerbosityLevel.MEDIUM) {
                String desc = d.voiceDescription;
                if (desc.length() > 60) desc = desc.substring(0, 57) + "...";
                descriptions.add(desc);
            } else if (verbosity == VerbosityLevel.LOW) {
                if (d.danger == DangerLevel.WARNING || d.danger == DangerLevel.DANGER || d.danger == DangerLevel.CRITICAL) {
                    descriptions.add(d.voiceDescription);
                }
            } else if (verbosity == VerbosityLevel.WHISPER) {
                if (d.danger == DangerLevel.DANGER || d.danger == DangerLevel.CRITICAL) {
                    descriptions.add(!d.action.isEmpty() ? d.action : d.label);
                }
            }
        }
        if (descriptions.isEmpty()) return "Livre.";
        return String.join(". ", descriptions) + ".";
    }

    private int dangerRank(DangerLevel dl) {
        if (dl == DangerLevel.CRITICAL) return 5;
        if (dl == DangerLevel.DANGER) return 4;
        if (dl == DangerLevel.WARNING) return 3;
        if (dl == DangerLevel.ATTENTION) return 2;
        return 1;
    }
}

// ============================================================================
// 4. GERENCIADOR DE AUDIO BLUETOOTH
// ============================================================================

class AudioOutputManager {
    public boolean connected;
    public String deviceName;
    public double batteryPct;
    public double volume;
    public double ttsRate;
    public String lastSpoken;
    public long lastSpokenTime;
    public double minIntervalS;
    public Deque<String> messageQueue;
    public Deque<String> priorityQueue;
    public int totalMessages;
    public int messagesSpoken;
    public int messagesSkipped;

    public AudioOutputManager() {
        this.connected = true;
        this.deviceName = "Fone Bluetooth";
        this.batteryPct = 100.0;
        this.volume = 0.7;
        this.ttsRate = 1.4;
        this.lastSpoken = "";
        this.lastSpokenTime = 0;
        this.minIntervalS = 1.5;
        this.messageQueue = new ConcurrentLinkedDeque<>();
        this.priorityQueue = new ConcurrentLinkedDeque<>();
        this.totalMessages = 0;
        this.messagesSpoken = 0;
        this.messagesSkipped = 0;
    }

    public Map<String, Object> speak(String message, DangerLevel priority) {
        long now = System.currentTimeMillis();
        this.totalMessages++;
        boolean isCritical = priority == DangerLevel.DANGER || priority == DangerLevel.CRITICAL;

        if (message.equals(this.lastSpoken) && !isCritical) {
            if ((now - this.lastSpokenTime) / 1000.0 < 5.0) {
                this.messagesSkipped++;
                Map<String, Object> r = new HashMap<>();
                r.put("spoken", false);
                r.put("reason", "duplicada");
                return r;
            }
        }

        if (!isCritical && (now - this.lastSpokenTime) / 1000.0 < this.minIntervalS) {
            this.messageQueue.addLast(message);
            this.messagesSkipped++;
            Map<String, Object> r = new HashMap<>();
            r.put("spoken", false);
            r.put("reason", "intervalo");
            return r;
        }

        if (isCritical) {
            this.priorityQueue.addFirst(message);
        } else {
            this.messageQueue.addLast(message);
        }

        this.lastSpoken = message;
        this.lastSpokenTime = now;
        this.messagesSpoken++;

        Map<String, Object> result = new HashMap<>();
        result.put("spoken", true);
        result.put("message", message);
        result.put("priority", priority.getValue());
        result.put("device", this.deviceName);
        result.put("volume", this.volume);
        result.put("rate", this.ttsRate);
        return result;
    }

    public List<String> processQueue() {
        List<String> spoken = new ArrayList<>();
        long now = System.currentTimeMillis();
        if ((now - this.lastSpokenTime) / 1000.0 >= this.minIntervalS) {
            if (!this.priorityQueue.isEmpty()) {
                String msg = this.priorityQueue.pollFirst();
                spoken.add(msg);
                this.lastSpoken = msg;
                this.lastSpokenTime = now;
                this.messagesSpoken++;
            } else if (!this.messageQueue.isEmpty()) {
                String msg = this.messageQueue.pollFirst();
                spoken.add(msg);
                this.lastSpoken = msg;
                this.lastSpokenTime = now;
                this.messagesSpoken++;
            }
        }
        return spoken;
    }

    public Map<String, Object> status() {
        Map<String, Object> s = new HashMap<>();
        s.put("connected", this.connected);
        s.put("device", this.deviceName);
        s.put("battery_pct", this.batteryPct);
        s.put("volume", this.volume);
        s.put("tts_rate", this.ttsRate);
        s.put("queue_size", this.messageQueue.size());
        s.put("priority_queue_size", this.priorityQueue.size());
        s.put("total_messages", this.totalMessages);
        s.put("spoken", this.messagesSpoken);
        s.put("skipped", this.messagesSkipped);
        return s;
    }
}

// ============================================================================
// 5. NAVEGACAO POR VOZ (Co-piloto de rua)
// ============================================================================

class StreetNavigator {
    public String destination;
    public int currentStep;
    public List<Map<String, Object>> steps;
    public String lastInstruction;
    public double distanceRemainingM;
    public double etaMinutes;

    public StreetNavigator() {
        this.destination = "";
        this.currentStep = 0;
        this.steps = new ArrayList<>();
        this.lastInstruction = "";
        this.distanceRemainingM = 0;
        this.etaMinutes = 0;
    }

    public String setDestination(String destination, List<Map<String, Object>> steps) {
        this.destination = destination;
        this.currentStep = 0;
        this.steps = (steps != null && !steps.isEmpty()) ? steps : _defaultRoute(destination);
        double total = 0;
        for (Map<String, Object> s : this.steps) total += (Double) s.getOrDefault("distance_m", 100.0);
        this.distanceRemainingM = total;
        this.etaMinutes = this.distanceRemainingM / 80.0;
        return "Rota calculada para " + destination + ". " + (int) this.distanceRemainingM + " metros. Aproximadamente " + (int) this.etaMinutes + " minutos.";
    }

    private List<Map<String, Object>> _defaultRoute(String destination) {
        List<Map<String, Object>> route = new ArrayList<>();
        Map<String, Object> s1 = new HashMap<>(); s1.put("instruction", "Saida do predio. Vire a direita na calcada."); s1.put("distance_m", 50.0); route.add(s1);
        Map<String, Object> s2 = new HashMap<>(); s2.put("instruction", "Continue reto por 200 metros na rua Augusta."); s2.put("distance_m", 200.0); route.add(s2);
        Map<String, Object> s3 = new HashMap<>(); s3.put("instruction", "Atencao: buraco a frente. Desvie a esquerda."); s3.put("distance_m", 5.0); s3.put("warning", true); route.add(s3);
        Map<String, Object> s4 = new HashMap<>(); s4.put("instruction", "Semaforo a frente. Aguarde se vermelho."); s4.put("distance_m", 30.0); route.add(s4);
        Map<String, Object> s5 = new HashMap<>(); s5.put("instruction", "Atravesse a faixa. 15 passos."); s5.put("distance_m", 15.0); route.add(s5);
        Map<String, Object> s6 = new HashMap<>(); s6.put("instruction", "Vire a direita na rua Paulista."); s6.put("distance_m", 10.0); route.add(s6);
        Map<String, Object> s7 = new HashMap<>(); s7.put("instruction", "Destino: " + destination + ". A esquerda, porta azul."); s7.put("distance_m", 50.0); s7.put("arrival", true); route.add(s7);
        return route;
    }

    public String nextInstruction() {
        if (this.currentStep >= this.steps.size()) return "Voce chegou ao destino.";
        Map<String, Object> step = this.steps.get(this.currentStep);
        String instruction = (String) step.get("instruction");
        this.lastInstruction = instruction;
        this.currentStep++;
        return instruction;
    }

    public String detectObstacleAhead() {
        String[] obstacles = {
            "Poste a frente, 3 metros. Desvie a direita.",
            "Buraco na calcada, 2 metros. Cuidado ao pisar.",
            "Carro mal estacionado bloqueando calcada. Desvie pela rua com cuidado.",
            "Pessoa parada a frente, 1 metro. 'Com licenca.'",
            "Degrau descendo, 1 metro. Passo menor.",
            "Raiz de arvore na calcada. Atencao ao pe esquerdo."
        };
        return this.currentStep < obstacles.length ? obstacles[this.currentStep % obstacles.length] : null;
    }

    public String arrivalMessage() {
        return "Voce chegou em " + this.destination + ". Esta a sua frente. Parabens!";
    }
}

// ============================================================================
// 6. SISTEMA PRINCIPAL -- BodyCamera Controller
// ============================================================================

class BodyCameraController {
    public MountPosition mount;
    public VerbosityLevel verbosity;
    public VisionEngine vision;
    public AudioOutputManager audio;
    public StreetNavigator navigator;
    public CameraMode mode;
    public boolean active;
    public long sessionStart;
    public int totalDescriptions;
    public int totalAlerts;
    public double batteryPct;
    public double batteryDrainPerHour;
    public String emergencyContact;

    public BodyCameraController(MountPosition mount, VerbosityLevel verbosity) {
        this.mount = mount != null ? mount : MountPosition.CHEST;
        this.verbosity = verbosity != null ? verbosity : VerbosityLevel.MEDIUM;
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

    public Map<String, Object> start() {
        this.active = true;
        this.sessionStart = System.currentTimeMillis();
        this.mode = CameraMode.CONTINUOUS;
        Map<String, Object> greeting = this.audio.speak(
            "Camera corporal ativa. Montagem: " + this.mount.getValue() + ". " +
            "Modo: continuo. Fone conectado: " + this.audio.deviceName + ". " +
            "Estou vendo por voce.", DangerLevel.SAFE);
        Map<String, Object> result = new HashMap<>();
        result.put("active", true);
        result.put("mount", this.mount.getValue());
        result.put("mode", this.mode.getValue());
        result.put("audio", this.audio.status());
        result.put("greeting", greeting);
        return result;
    }

    public Map<String, Object> stop() {
        double duration = this.sessionStart > 0 ? (System.currentTimeMillis() - this.sessionStart) / 1000.0 / 60.0 : 0;
        this.active = false;
        this.audio.speak("Camera desligada. Ate logo.", DangerLevel.SAFE);
        Map<String, Object> result = new HashMap<>();
        result.put("active", false);
        result.put("session_duration_min", duration);
        result.put("total_descriptions", this.totalDescriptions);
        result.put("total_alerts", this.totalAlerts);
        return result;
    }

    public String describe() {
        if (!this.active) return "Camera desligada.";
        List<Detection> detections = this.vision.processFrame(this.mode);
        String description = this.vision.describeScene(detections, this.verbosity);
        this.audio.speak(description, DangerLevel.SAFE);
        this.totalDescriptions++;
        return description;
    }

    public List<String> describeContinuous(int frames, double intervalS) {
        List<String> descriptions = new ArrayList<>();
        for (int i = 0; i < frames; i++) {
            String desc = this.describe();
            descriptions.add(desc);
            try { Thread.sleep((long)(intervalS * 1000)); } catch (InterruptedException ignored) {}
        }
        return descriptions;
    }

    public String navigate(String destination) {
        this.mode = CameraMode.NAVIGATION;
        String routeMsg = this.navigator.setDestination(destination, null);
        this.audio.speak(routeMsg, DangerLevel.SAFE);
        String firstStep = this.navigator.nextInstruction();
        this.audio.speak(firstStep, DangerLevel.ATTENTION);
        return routeMsg + "\n" + firstStep;
    }

    public String navigateStep() {
        String instruction = this.navigator.nextInstruction();
        this.audio.speak(instruction, DangerLevel.ATTENTION);
        String obstacle = this.navigator.detectObstacleAhead();
        if (obstacle != null) {
            this.audio.speak(obstacle, DangerLevel.WARNING);
            this.totalAlerts++;
            return instruction + "\nALERTA: " + obstacle;
        }
        return instruction;
    }

    public String readText() {
        this.mode = CameraMode.READING;
        List<Detection> detections = this.vision.processFrame(CameraMode.READING);
        List<String> texts = new ArrayList<>();
        for (Detection d : detections) if (d.objectType == ObjectType.TEXT) texts.add(d.voiceDescription);
        String result = texts.isEmpty() ? "Nao encontrei texto legivel." : String.join(" ", texts);
        this.audio.speak(result, DangerLevel.SAFE);
        this.totalDescriptions++;
        return result;
    }

    public String identifyMoney() {
        this.mode = CameraMode.MONEY;
        List<Detection> detections = this.vision.processFrame(CameraMode.MONEY);
        List<String> money = new ArrayList<>();
        for (Detection d : detections) if (d.objectType == ObjectType.MONEY) money.add(d.voiceDescription);
        String result = money.isEmpty() ? "Nao reconheci nenhuma cedula." : money.get(0);
        this.audio.speak(result, DangerLevel.SAFE);
        return result;
    }

    public String identifyColor() {
        this.mode = CameraMode.COLOR;
        List<Detection> detections = this.vision.processFrame(CameraMode.COLOR);
        List<String> colors = new ArrayList<>();
        for (Detection d : detections) colors.add(d.voiceDescription);
        String result = colors.isEmpty() ? "Nao consegui identificar a cor." : colors.get(0);
        this.audio.speak(result, DangerLevel.SAFE);
        return result;
    }

    public String recognizeFace() {
        this.mode = CameraMode.FACE;
        List<Detection> detections = this.vision.processFrame(CameraMode.FACE);
        List<String> faces = new ArrayList<>();
        for (Detection d : detections) if (d.objectType == ObjectType.PERSON) faces.add(d.voiceDescription);
        String result = faces.isEmpty() ? "Nao reconheci ninguem a frente." : faces.get(0);
        this.audio.speak(result, DangerLevel.SAFE);
        return result;
    }

    public String searchObject(String objectName) {
        this.mode = CameraMode.SEARCH;
        List<Detection> detections = this.vision.processFrame(CameraMode.SEARCH);
        List<String> found = new ArrayList<>();
        for (Detection d : detections) found.add(d.voiceDescription);
        String result = found.isEmpty() ? "Nao encontrei " + objectName + ". Aponte a camera para outra direcao." : found.get(0);
        this.audio.speak(result, DangerLevel.SAFE);
        return result;
    }

    public String alertEmergency(String description) {
        this.totalAlerts++;
        String msg = "EMERGENCIA. " + description + ". Vou avisar seu contato.";
        this.audio.speak(msg, DangerLevel.CRITICAL);
        return msg;
    }

    public Map<String, Object> checkBattery() {
        if (this.active && this.sessionStart > 0) {
            double hours = (System.currentTimeMillis() - this.sessionStart) / 1000.0 / 3600.0;
            this.batteryPct = Math.max(0, 100 - (hours * this.batteryDrainPerHour));
        }
        Map<String, Object> b = new HashMap<>();
        b.put("phone_battery_pct", this.batteryPct);
        b.put("headphone_battery_pct", this.audio.batteryPct);
        b.put("estimated_remaining_h", this.batteryDrainPerHour > 0 ? this.batteryPct / this.batteryDrainPerHour : 0);
        b.put("low_battery", this.batteryPct < 20);
        b.put("critical_battery", this.batteryPct < 5);
        return b;
    }

    public String setMode(CameraMode mode) {
        this.mode = mode;
        Map<CameraMode, String> modeNames = new HashMap<>();
        modeNames.put(CameraMode.CONTINUOUS, "Continuo. Vou descrever tudo.");
        modeNames.put(CameraMode.ON_DEMAND, "Sob demanda. Pergunte quando quiser.");
        modeNames.put(CameraMode.ALERT_ONLY, "So alertas. So falo em perigo.");
        modeNames.put(CameraMode.NAVIGATION, "Navegacao. Vou guiar voce.");
        modeNames.put(CameraMode.READING, "Leitura. Aponte para o texto.");
        modeNames.put(CameraMode.MONEY, "Dinheiro. Mostre a cedula.");
        modeNames.put(CameraMode.COLOR, "Cor. Aponte para a cor.");
        modeNames.put(CameraMode.FACE, "Reconhecimento. Olhe para a pessoa.");
        modeNames.put(CameraMode.SEARCH, "Busca. O que procura?");
        modeNames.put(CameraMode.MINIMAL, "Minimal. So o essencial.");
        String msg = modeNames.getOrDefault(mode, "Modo alterado.");
        this.audio.speak(msg, DangerLevel.SAFE);
        return msg;
    }

    public String setVerbosity(VerbosityLevel level) {
        this.verbosity = level;
        Map<VerbosityLevel, String> msgs = new HashMap<>();
        msgs.put(VerbosityLevel.HIGH, "Detalhe alto. Vou descrever tudo.");
        msgs.put(VerbosityLevel.MEDIUM, "Detalhe medio. O essencial.");
        msgs.put(VerbosityLevel.LOW, "Detalhe baixo. So alertas.");
        msgs.put(VerbosityLevel.WHISPER, "Minimal. So perigos criticos.");
        String msg = msgs.getOrDefault(level, "Verbosidade alterada.");
        this.audio.speak(msg, DangerLevel.SAFE);
        return msg;
    }

    public Map<String, Object> status() {
        Map<String, Object> s = new HashMap<>();
        s.put("active", this.active);
        s.put("mount", this.mount.getValue());
        s.put("mode", this.mode.getValue());
        s.put("verbosity", this.verbosity.getValue());
        s.put("battery", this.checkBattery());
        s.put("audio", this.audio.status());
        s.put("vision_frames", this.vision.frameCount);
        s.put("total_descriptions", this.totalDescriptions);
        s.put("total_alerts", this.totalAlerts);
        s.put("destination", this.navigator.destination);
        s.put("nav_step", this.navigator.currentStep);
        return s;
    }
}

// ============================================================================
// 7. CENARIOS DO MUNDO REAL
// ============================================================================

class Scenarios {
    public static void scenarioWalkingToDestination() {
        System.out.println("=".repeat(65));
        System.out.println("CENARIO 1: Cego andando ate a padaria");
        System.out.println("=".repeat(65));
        BodyCameraController cam = new BodyCameraController(MountPosition.CHEST, VerbosityLevel.MEDIUM);
        Map<String, Object> start = cam.start();
        System.out.println("\n[" + ((Map)start.get("greeting")).get("message") + "]");
        System.out.println("\n[NAVEGACAO]");
        String route = cam.navigate("Padaria do Joao");
        System.out.println("  " + route);
        for (int i = 0; i < 4; i++) {
            System.out.println("\n[Passo " + (i+1) + "]");
            String instruction = cam.navigateStep();
            System.out.println("  " + instruction);
        }
    }

    public static void scenarioReadingMenu() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 2: Cego lendo cardapio de restaurante");
        System.out.println("=".repeat(65));
        BodyCameraController cam = new BodyCameraController(null, null);
        cam.start();
        System.out.println("\n[MODO LEITURA]");
        String text = cam.readText();
        System.out.println("  Camera leu: " + text);
    }

    public static void scenarioIdentifyingMoney() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 3: Cego reconhecendo dinheiro");
        System.out.println("=".repeat(65));
        BodyCameraController cam = new BodyCameraController(null, null);
        cam.start();
        System.out.println("\n[MODO DINHEIRO]");
        String money = cam.identifyMoney();
        System.out.println("  Camera identificou: " + money);
    }

    public static void scenarioCrossingStreet() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 4: Cego atravessando a rua");
        System.out.println("=".repeat(65));
        BodyCameraController cam = new BodyCameraController(null, null);
        cam.start();
        cam.setMode(CameraMode.NAVIGATION);
        System.out.println("\n[Cena 1: Chegando no semaforo]");
        String desc = cam.describe();
        System.out.println("  " + desc);
        System.out.println("\n[Cena 2: Semaforo]");
        String color = cam.identifyColor();
        System.out.println("  " + color);
        System.out.println("\n[Cena 3: Atravesando]");
        desc = cam.describe();
        System.out.println("  " + desc);
    }

    public static void scenarioMeetingPerson() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 5: Cego reconhecendo pessoa a frente");
        System.out.println("=".repeat(65));
        BodyCameraController cam = new BodyCameraController(null, null);
        cam.start();
        System.out.println("\n[MODO ROSTO]");
        String face = cam.recognizeFace();
        System.out.println("  " + face);
    }

    public static void scenarioSearchingObject() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 6: Cego procurando objeto perdido");
        System.out.println("=".repeat(65));
        BodyCameraController cam = new BodyCameraController(null, null);
        cam.start();
        System.out.println("\n[MODO BUSCA: 'minha chave']");
        String result = cam.searchObject("minha chave");
        System.out.println("  " + result);
    }

    public static void scenarioBatteryManagement() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 7: Bateria em caminhada longa");
        System.out.println("=".repeat(65));
        BodyCameraController cam = new BodyCameraController(null, null);
        cam.start();
        System.out.println("\n[Inicio da caminhada]");
        Map<String, Object> battery = cam.checkBattery();
        System.out.printf("  Celular: %.0f%%\n", (Double)battery.get("phone_battery_pct"));
        System.out.printf("  Fone: %.0f%%\n", (Double)battery.get("headphone_battery_pct"));
        System.out.printf("  Autonomia estimada: %.1fh\n", (Double)battery.get("estimated_remaining_h"));
        cam.sessionStart = System.currentTimeMillis() - 3L * 3600 * 1000;
        System.out.println("\n[Apos 3 horas de uso]");
        battery = cam.checkBattery();
        System.out.printf("  Celular: %.0f%%\n", (Double)battery.get("phone_battery_pct"));
        System.out.printf("  Fone: %.0f%%\n", (Double)battery.get("headphone_battery_pct"));
        System.out.printf("  Restante: %.1fh\n", (Double)battery.get("estimated_remaining_h"));
        if ((Boolean)battery.get("low_battery")) {
            System.out.println("  AVISO: Bateria baixa. Modo survival.");
        }
    }

    public static void scenarioContinuousDescription() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 8: Descricao continua andando na rua");
        System.out.println("=".repeat(65));
        BodyCameraController cam = new BodyCameraController(MountPosition.CHEST, VerbosityLevel.MEDIUM);
        cam.start();
        System.out.println("\n[Descricao continua - 5 frames]");
        for (int i = 0; i < 5; i++) {
            String desc = cam.describe();
            System.out.println("  Frame " + (i+1) + ": " + desc);
            try { Thread.sleep(100); } catch (InterruptedException ignored) {}
        }
    }
}

// ============================================================================
// 8. DEMONSTRACAO (main)
// ============================================================================

public class open_body_camera {
    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("OpenBodyCamera -- Smartphone Corporal + Fone BT = Olhos do Cego");
        System.out.println("=".repeat(70));

        System.out.println("\nMontagens: " + MountPosition.values().length);
        for (MountPosition m : MountPosition.values()) System.out.println("  " + m.getValue());

        System.out.println("\nModos de camera: " + CameraMode.values().length);
        for (CameraMode m : CameraMode.values()) System.out.println("  " + m.getValue());

        System.out.println("\nVerbosidade: " + VerbosityLevel.values().length);
        for (VerbosityLevel v : VerbosityLevel.values()) System.out.println("  " + v.getValue());

        System.out.println("\nTipos de objeto: " + ObjectType.values().length);
        System.out.println("Niveis de perigo: " + DangerLevel.values().length);

        Scenarios.scenarioWalkingToDestination();
        Scenarios.scenarioReadingMenu();
        Scenarios.scenarioIdentifyingMoney();
        Scenarios.scenarioCrossingStreet();
        Scenarios.scenarioMeetingPerson();
        Scenarios.scenarioSearchingObject();
        Scenarios.scenarioContinuousDescription();
        Scenarios.scenarioBatteryManagement();

        BodyCameraController cam = new BodyCameraController(null, null);
        cam.start();
        cam.describe();
        cam.navigate("teste");
        Map<String, Object> status = cam.status();
        System.out.println("\n" + "=".repeat(70));
        System.out.println("STATUS DO SISTEMA");
        System.out.println("=".repeat(70));
        System.out.println("  Ativo: " + status.get("active"));
        System.out.println("  Montagem: " + status.get("mount"));
        System.out.println("  Modo: " + status.get("mode"));
        System.out.println("  Verbosidade: " + status.get("verbosity"));
        System.out.println("  Frames processados: " + status.get("vision_frames"));
        System.out.println("  Descricoes geradas: " + status.get("total_descriptions"));
        System.out.println("  Alertas emitidos: " + status.get("total_alerts"));
        System.out.println("  Audio: " + ((Map)status.get("audio")).get("connected"));

        cam.stop();

        System.out.println("\n" + "=".repeat(70));
        System.out.println("RESUMO");
        System.out.println("=".repeat(70));
        System.out.println();
        System.out.println("  O smartphone vira OLHOS.");
        System.out.println("  O fone bluetooth vira VOZ que descreve.");
        System.out.println("  O cego ANDA na rua com INFORMACAO.");
        System.out.println("  NADA o para. NINGUEM o limita.");
        System.out.println();
        System.out.println("  Camera no peito. Fone no ouvido. Mundo na mente.");
        System.out.println("  O cego VE.");
        System.out.println();
        System.out.println("  Integrado com:");
        System.out.println("    OpenTelefonista (conversa natural)");
        System.out.println("    OpenInclusiveHardware (44 dispositivos)");
        System.out.println("    OpenResilience (bateria/falhas)");
        System.out.println("    OpenHumanNet (emergencia)");
    }
}