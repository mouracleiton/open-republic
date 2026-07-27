// open_telefonista.js
// Transpilacao fiel de open_telefonista.py para JavaScript
// Todas as enums, classes, funcoes, cenarios e demo() preservados.
// Comentarios em portugues. Sem abreviacoes.

const TelefonistaPersonality = {
    GENTLE: "gentil", CHEERFUL: "alegre", SERIOUS: "seria",
    FRIENDLY: "amiga", FORMAL: "formal", PLAYFUL: "brincalhona",
    PROTECTIVE: "protetora", MINIMAL: "minimal"
};

const EmotionalState = {
    HAPPY: "feliz", CALM: "calmo", FOCUSED: "focado", TIRED: "cansado",
    STRESSED: "estressado", ANXIOUS: "ansioso", SAD: "triste",
    ANGRY: "irritado", OVERWHELMED: "sobrecarregado", NEUTRAL: "neutro"
};

const ConversationMode = {
    DIALOGUE: "dialogo", DICTATION: "ditado", NARRATION: "narracao",
    EMERGENCY: "emergencia", WHISPER: "sussurro", SILENT: "silencioso",
    CO_DRIVER: "copiloto", TEACHER: "professora"
};

class TelefonistaConfig {
    constructor() {
        this.name = "Iara";
        this.personality = TelefonistaPersonality.GENTLE;
        this.voice_id = "pt-BR-FemaleA";
        this.speech_rate = 1.0;
        this.formality = 0.3;
        this.verbosity = 0.5;
        this.humor_enabled = true;
        this.proactive = 0.3;
        this.language = "pt-BR";
        this.respects_silence = true;
        this.interruptible = true;
        this.emotional_adaptation = true;
    }
    adapt_to_emotion(emotion) {
        if (emotion === EmotionalState.STRESSED || emotion === EmotionalState.ANXIOUS) {
            this.speech_rate = 0.85; this.verbosity = 0.3; this.humor_enabled = false;
            this.personality = TelefonistaPersonality.GENTLE;
        } else if (emotion === EmotionalState.TIRED) {
            this.speech_rate = 0.9; this.verbosity = 0.3; this.proactive = 0.1;
        } else if (emotion === EmotionalState.HAPPY) {
            this.humor_enabled = true; this.speech_rate = 1.1;
        } else if (emotion === EmotionalState.OVERWHELMED) {
            this.verbosity = 0.1; this.speech_rate = 0.8; this.proactive = 0.0;
        } else if (emotion === EmotionalState.FOCUSED) {
            this.verbosity = 0.2; this.humor_enabled = false; this.proactive = 0.1;
        }
    }
}

const SensorType = {
    CAMERA_REAR: "camera_traseira", CAMERA_FRONT: "camera_frontal",
    MICROPHONE: "microfone", GPS: "gps", ACCELEROMETER: "acelerometro",
    GYROSCOPE: "giroscopio", COMPASS: "bussola", BAROMETER: "barometro",
    THERMOMETER: "termometro", HUMIDITY: "umidade", LIGHT: "luminosidade",
    PROXIMITY: "proximidade", LIDAR: "lidar", TOF: "tempo_de_voo",
    HEART_RATE: "frequencia_cardiaca", SPO2: "oxigenio",
    SKIN_TEMP: "temperatura_pele", NFC: "nfc",
    BLUETOOTH_BEACON: "beacon_bluetooth", CELL_SIGNAL: "sinal_celular"
};

const WorldPerception = {
    // VISAO
    COLOR_DETECTION: "deteccao_cor", TEXT_RECOGNITION: "reconhecimento_texto",
    OBJECT_DETECTION: "deteccao_objetos", FACE_RECOGNITION: "reconhecimento_facial",
    OBSTACLE_DETECTION: "deteccao_obstaculos", CROSSWALK_DETECTION: "deteccao_faixa",
    TRAFFIC_LIGHT: "semaforo", SIGN_RECOGNITION: "reconhecimento_placas",
    DOCUMENT_SCAN: "escaneamento_documento", MONEY_RECOGNITION: "reconhecimento_cedula",
    PRODUCT_LABEL: "rotulo_produto",
    // AUDICAO
    SOUND_CLASSIFICATION: "classificacao_som", SPEAKER_RECOGNITION: "reconhecimento_voz",
    MUSIC_RECOGNITION: "reconhecimento_musica", SPEECH_TO_TEXT: "fala_para_texto",
    AMBIENT_NOISE: "ruido_ambiente", DOORBELL: "campainha",
    ALARM_SOUND: "alarme", SIREN: "sirene", BABY_CRYING: "bebe_chorando",
    DOG_BARKING: "cachorro_latindo",
    // LOCALIZACAO
    GPS_LOCATION: "localizacao_gps", INDOOR_LOCATION: "localizacao_indoor",
    DIRECTION_FACING: "direcao", ALTITUDE: "altitude", SPEED: "velocidade",
    NEARBY_PLACES: "lugares_proximos", GEOCODING: "geocoding",
    LOST_CHILD: "crianca_perdida",
    // BIOMETRIA
    FALL_DETECTION: "deteccao_queda", HEART_ANOMALY: "anomalia_cardiaca",
    STRESS_DETECTION: "deteccao_stress", SEIZURE_PREDICTION: "previsao_crise",
    TREMOR_DETECTION: "deteccao_tremor", POSTURE: "postura",
    // AMBIENTE
    TEMPERATURE: "temperatura_ambiente", AIR_QUALITY: "qualidade_ar",
    UV_INDEX: "indice_uv", WEATHER: "clima"
};

class SensorReading {
    constructor(sensor, perception, value, confidence, description) {
        this.sensor = sensor; this.perception = perception; this.value = value;
        this.confidence = confidence; this.timestamp = Date.now() / 1000;
        this.description = description;
    }
}

class ComputerVisionEngine {
    constructor() {
        this.active_perceptions = [];
        this.last_readings = [];
    }
    process_frame(sensor, frame_data = null) {
        const readings = [];
        readings.push(new SensorReading(sensor, WorldPerception.COLOR_DETECTION,
            { color_name: "vermelho", hex: "#FF0000", rgb: [255,0,0] },
            0.95, "Aqui e VERMELHO. A luz do semaforo esta VERMELHA. Pare."));
        readings.push(new SensorReading(sensor, WorldPerception.OBSTACLE_DETECTION,
            { obstacle: "poste", distance_m: 2.5, direction: "frente-esquerda" },
            0.88, "Poste a 2.5 metros a frente e a esquerda. Desvie para a direita."));
        readings.push(new SensorReading(sensor, WorldPerception.TEXT_RECOGNITION,
            { text: "RESTAURANTE JOAO", location: "acima da porta" },
            0.92, "Placa diz: RESTAURANTE JOAO. Fica acima da porta a frente."));
        readings.push(new SensorReading(sensor, WorldPerception.TRAFFIC_LIGHT,
            { color: "verde", action: "siga" },
            0.97, "Semaforo VERDE. Pode atravessar."));
        readings.push(new SensorReading(sensor, WorldPerception.MONEY_RECOGNITION,
            { denomination: "R$ 50,00", color_pattern: "marrom" },
            0.94, "Isso e uma nota de CINQUENTA REAIS."));
        this.last_readings.push(...readings);
        if (this.last_readings.length > 100) this.last_readings = this.last_readings.slice(-100);
        return readings;
    }
    narrate_scene(readings, user_disability = "") {
        if (!readings.length) return "Nao consigo ver nada claramente agora.";
        const parts = readings.filter(r => r.confidence > 0.7).map(r => r.description);
        if (!parts.length) return "Ambiente visual incerto. Vou continuar observando.";
        return parts.join(". ") + ".";
    }
}

class AudioPerceptionEngine {
    constructor() {
        this.last_readings = [];
        this.sound_buffer = [];
    }
    process_audio() {
        const readings = [];
        readings.push(new SensorReading(SensorType.MICROPHONE, WorldPerception.SPEECH_TO_TEXT,
            { speaker: "homem", text: "Bom dia, como vai?" },
            0.90, "Um homem disse: Bom dia, como vai?"));
        readings.push(new SensorReading(SensorType.MICROPHONE, WorldPerception.SOUND_CLASSIFICATION,
            { sound: "sirene", direction: "direita", approaching: true },
            0.85, "Sirene de ambulancia se aproximando pela direita."));
        readings.push(new SensorReading(SensorType.MICROPHONE, WorldPerception.DOORBELL,
            { detected: true, count: 2 },
            0.95, "Alguem tocou a campainha. Duas vezes."));
        readings.push(new SensorReading(SensorType.MICROPHONE, WorldPerception.BABY_CRYING,
            { detected: true, intensity: "alta" },
            0.93, "O bebe esta chorando. Intensidade alta."));
        this.last_readings.push(...readings);
        if (this.last_readings.length > 100) this.last_readings = this.last_readings.slice(-100);
        return readings;
    }
    narrate_sounds(readings) {
        if (!readings.length) return "Silencio.";
        const parts = readings.filter(r => r.confidence > 0.7).map(r => r.description);
        return parts.length ? parts.join(". ") + "." : "Nao identifico sons especificos.";
    }
}

class GeoLocationEngine {
    constructor() {
        this.last_known_location = [-23.55, -46.63];
        this.tracked_persons = {};
        this.safe_zones = [];
        this.last_readings = [];
    }
    update_location(lat, lon) {
        this.last_known_location = [lat, lon];
        const r = new SensorReading(SensorType.GPS, WorldPerception.GPS_LOCATION,
            { lat, lon }, 0.98, `Voce esta proximo a ${lat.toFixed(4)}, ${lon.toFixed(4)}.`);
        this.last_readings.push(r);
        return r;
    }
    navigate_for_blind(destination) {
        return "Voce esta na rua Augusta, numero 1000.";
    }
    track_child(child_id, child_name, child_phone, safe_zones = null) {
        const child = {
            name: child_name, phone: child_phone, last_location: null,
            last_update: Date.now() / 1000,
            safe_zones: safe_zones || [], status: "safe", battery: 100
        };
        this.tracked_persons[child_id] = child;
        if (safe_zones) this.safe_zones = safe_zones;
        return child;
    }
    check_child_location(child_id, lat, lon, battery = 100) {
        if (!(child_id in this.tracked_persons)) return { error: "crianca nao registrada" };
        const child = this.tracked_persons[child_id];
        child.last_location = [lat, lon];
        child.last_update = Date.now() / 1000;
        child.battery = battery;
        let in_safe_zone = false, zoneHit = null;
        for (const zone of child.safe_zones || []) {
            const d = this._haversine(lat, lon, zone.lat, zone.lon);
            if (d <= (zone.radius_m || 200)) { in_safe_zone = true; zoneHit = zone; break; }
        }
        if (in_safe_zone) {
            child.status = "safe";
            return {
                child_id, name: child.name, status: "safe", location: [lat, lon],
                zone: zoneHit ? zoneHit.name : "zona segura", battery,
                message: `${child.name} esta na zona segura: ${zoneHit ? zoneHit.name : "casa"}.`
            };
        } else {
            child.status = "outside";
            let minDist = 999999, nearest = "";
            for (const zone of child.safe_zones || []) {
                const d = this._haversine(lat, lon, zone.lat, zone.lon);
                if (d < minDist) { minDist = d; nearest = zone.name || "zona"; }
            }
            return {
                child_id, name: child.name, status: "outside_safe_zone",
                location: [lat, lon], distance_from_nearest_safe_m: Math.round(minDist),
                nearest_zone: nearest, battery,
                message: `ATENCAO: ${child.name} saiu da zona segura. Esta a ${Math.round(minDist)} metros de ${nearest}. Bateria: ${battery}%.`,
                alert_level: minDist < 1000 ? "warning" : "critical"
            };
        }
    }
    find_nearby_help(help_type = "hospital") {
        return [
            { name: "Hospital Sao Paulo", distance_m: 800, direction: "norte" },
            { name: "UBS Vila Mariana", distance_m: 1200, direction: "leste" },
            { name: "Farmacia 24h", distance_m: 300, direction: "oeste" }
        ];
    }
    _haversine(lat1, lon1, lat2, lon2) {
        const R = 6371000;
        const dlat = (lat2 - lat1) * Math.PI / 180;
        const dlon = (lon2 - lon1) * Math.PI / 180;
        const a = Math.sin(dlat/2)**2 + Math.cos(lat1*Math.PI/180)*Math.cos(lat2*Math.PI/180)*Math.sin(dlon/2)**2;
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
        return R * c;
    }
}

class BiometricEngine {
    constructor() {
        this.last_readings = [];
        this.baseline_heart_rate = 75;
        this.fall_detected = false;
    }
    process_biometrics(heart_rate = 75, spo2 = 98, skin_temp = 36.5, movement = "normal") {
        const readings = [];
        if (movement === "fall") {
            this.fall_detected = true;
            readings.push(new SensorReading(SensorType.ACCELEROMETER, WorldPerception.FALL_DETECTION,
                { detected: true, impact_g: 3.2 }, 0.92,
                "QUEDA DETECTADA. Voce esta bem? Responda em 30 segundos ou ligo para emergencia."));
        }
        if (heart_rate > 120 || heart_rate < 50) {
            readings.push(new SensorReading(SensorType.HEART_RATE, WorldPerception.HEART_ANOMALY,
                { heart_rate, baseline: this.baseline_heart_rate }, 0.85,
                `Frequencia cardiaca ${heart_rate} bpm. Isso esta fora do normal.`));
        }
        if (heart_rate > 100 && movement === "normal") {
            readings.push(new SensorReading(SensorType.HEART_RATE, WorldPerception.STRESS_DETECTION,
                { heart_rate, hrv_low: true }, 0.70,
                "Seu coracao esta acelerado e voce esta parado. Talvez estresse. Quer respirar comigo?"));
        }
        if (skin_temp > 37.0 && heart_rate > 110) {
            readings.push(new SensorReading(SensorType.SKIN_TEMP, WorldPerception.SEIZURE_PREDICTION,
                { skin_temp, heart_rate, risk: "moderate" }, 0.60,
                "Sinais que podem preceder uma crise. Sente-se em local seguro."));
        }
        if (movement === "tremor") {
            readings.push(new SensorReading(SensorType.ACCELEROMETER, WorldPerception.TREMOR_DETECTION,
                { frequency_hz: 5.0, amplitude: "moderate" }, 0.80,
                "Tremor detectado. Vou ajustar a sensibilidade dos botoes."));
        }
        this.last_readings.push(...readings);
        return readings;
    }
}

class Telefonista {
    constructor(config) {
        this.config = config;
        this.cv_engine = new ComputerVisionEngine();
        this.audio_engine = new AudioPerceptionEngine();
        this.geo_engine = new GeoLocationEngine();
        this.bio_engine = new BiometricEngine();
        this.conversation_history = [];
        this.user_emotion = EmotionalState.NEUTRAL;
        this.current_mode = ConversationMode.DIALOGUE;
        this.active_sensors = new Set();
        this.user_name = "";
        this.user_disabilities = [];
        this.children_tracked = {};
        this._setup_sensors();
    }
    _setup_sensors() {
        [SensorType.CAMERA_REAR, SensorType.CAMERA_FRONT, SensorType.MICROPHONE,
         SensorType.GPS, SensorType.ACCELEROMETER, SensorType.GYROSCOPE,
         SensorType.COMPASS, SensorType.LIGHT, SensorType.PROXIMITY].forEach(s => this.active_sensors.add(s));
    }
    greet(user_name, time_of_day = "manha") {
        this.user_name = user_name;
        const greetings = { manha: "Bom dia", tarde: "Boa tarde", noite: "Boa noite" };
        const g = greetings[time_of_day] || "Ola";
        let msg;
        if (this.config.personality === TelefonistaPersonality.GENTLE)
            msg = `${g}, ${user_name}. Aqui e a ${this.config.name}. `;
        else if (this.config.personality === TelefonistaPersonality.CHEERFUL)
            msg = `${g}, ${user_name}! Que bom te ouvir! `;
        else if (this.config.personality === TelefonistaPersonality.FORMAL)
            msg = `${g}. ${this.config.name} a servico. `;
        else msg = `${g}, ${user_name}. `;
        this._record(msg, "telefonista");
        return msg;
    }
    listen_and_respond(user_input) {
        this._record(user_input, "user");
        const emotion = this._detect_emotion(user_input);
        if (emotion !== this.user_emotion) {
            this.user_emotion = emotion;
            if (this.config.emotional_adaptation) this.config.adapt_to_emotion(emotion);
        }
        const intent = this._detect_intent(user_input);
        const response = this._respond(intent, user_input);
        this._record(response, "telefonista");
        return response;
    }
    see_world() {
        const readings = this.cv_engine.process_frame(SensorType.CAMERA_REAR);
        const narration = this.cv_engine.narrate_scene(readings, this.user_disabilities.join(", "));
        this._record(narration, "telefonista");
        return narration;
    }
    hear_world() {
        const readings = this.audio_engine.process_audio();
        const narration = this.audio_engine.narrate_sounds(readings);
        this._record(narration, "telefonista");
        return narration;
    }
    sense_body(heart_rate = 75, movement = "normal", spo2 = 98, skin_temp = 36.5) {
        const readings = this.bio_engine.process_biometrics(heart_rate, spo2, skin_temp, movement);
        if (!readings.length) return "Tudo normal com seu corpo.";
        const msg = readings.map(r => r.description).join(" ");
        this._record(msg, "telefonista");
        return msg;
    }
    navigate(destination) {
        this.current_mode = ConversationMode.CO_DRIVER;
        const instruction = this.geo_engine.navigate_for_blind(destination);
        this._record(instruction, "telefonista");
        return instruction;
    }
    check_on_child(child_id, lat, lon, battery = 100) {
        const result = this.geo_engine.check_child_location(child_id, lat, lon, battery);
        const msg = result.message || "Sem informacoes.";
        this._record(msg, "telefonista");
        return msg;
    }
    register_child(child_id, name, phone, safe_zones = null) {
        this.geo_engine.track_child(child_id, name, phone, safe_zones);
        this.children_tracked[child_id] = name;
        const msg = `${name} registrada. Vou avisar se ela sair das zonas seguras.`;
        this._record(msg, "telefonista");
        return msg;
    }
    find_help(help_type = "hospital") {
        const results = this.geo_engine.find_nearby_help(help_type);
        if (!results.length) return "Nao encontrei nada proximo agora.";
        const parts = results.map(r => `${r.name} a ${r.distance_m} metros ao ${r.direction}`);
        const msg = "Encontrei: " + parts.join(". ") + ".";
        this._record(msg, "telefonista");
        return msg;
    }
    make_call(contact_name, reason = "") {
        const reason_text = reason ? ` Motivo: ${reason}.` : "";
        const msg = `Ligando para ${contact_name}.${reason_text}`;
        this._record(msg, "telefonista");
        return msg;
    }
    emergency(service = "190") {
        this.current_mode = ConversationMode.EMERGENCY;
        this.config.personality = TelefonistaPersonality.PROTECTIVE;
        this.config.speech_rate = 0.9; this.config.humor_enabled = false; this.config.verbosity = 0.2;
        const msg = `EMERGENCIA. Ligando para ${service}. Fique calmo. Estou aqui.`;
        this._record(msg, "telefonista");
        return msg;
    }
    dictate_code(code_input) {
        this.current_mode = ConversationMode.DICTATION;
        const msg = `Anotado. Escrevi: ${code_input}. Quer que eu execute?`;
        this._record(msg, "telefonista");
        return msg;
    }
    _detect_emotion(text) {
        const t = text.toLowerCase();
        if (t.includes("cansado") || t.includes("exausto") || t.includes("durmo")) return EmotionalState.TIRED;
        if (t.includes("estress") || t.includes("put") || t.includes("merda") || t.includes("porra")) return EmotionalState.STRESSED;
        if (t.includes("ansios") || t.includes("preocup") || t.includes("medo")) return EmotionalState.ANXIOUS;
        if (t.includes("feliz") || t.includes("otimo") || t.includes("show") || t.includes("massa")) return EmotionalState.HAPPY;
        if (t.includes("foco") || t.includes("trabalh") || t.includes("concentrad")) return EmotionalState.FOCUSED;
        if (t.includes("triste") || t.includes("para") || t.includes("desanim")) return EmotionalState.SAD;
        if (t.includes("irritad") || t.includes("irritante") || t.includes("raiva")) return EmotionalState.ANGRY;
        if (t.includes("muito") || t.includes("sobrecarreg") || t.includes("nao aguento")) return EmotionalState.OVERWHELMED;
        return EmotionalState.NEUTRAL;
    }
    _detect_intent(text) {
        const t = text.toLowerCase();
        if (t.includes("codigo") || t.includes("programar") || t.includes("funcao") || t.includes("variavel")) return "code";
        if (t.includes("onde estou") || t.includes("localizacao") || t.includes("rua")) return "location";
        if (t.includes("minha filha") || t.includes("meu filho") || t.includes("crianca")) return "child";
        if (t.includes("cor") || t.includes("cela") || t.includes("vermelho") || t.includes("verde") || t.includes("azul")) return "color";
        if (t.includes("socorro") || t.includes("emergencia") || t.includes("ajuda") || t.includes("190") || t.includes("192")) return "emergency";
        if (t.includes("ligar") || t.includes("telefone") || t.includes("chamada")) return "call";
        if (t.includes("ve") || t.includes("olha") || t.includes("camera") || t.includes("enxergar")) return "see";
        if (t.includes("ouvir") || t.includes("som") || t.includes("barulho")) return "hear";
        if (t.includes("navegar") || t.includes("ir para") || t.includes("como chego")) return "navigate";
        return "chat";
    }
    _respond(intent, user_input) {
        const name = this.user_name || "amigo";
        if (intent === "code") return this.dictate_code(user_input);
        if (intent === "location") return this.geo_engine.navigate_for_blind("");
        if (intent === "child") return "Quer que eu verifique onde ela esta?";
        if (intent === "color") {
            const readings = this.cv_engine.process_frame(SensorType.CAMERA_REAR);
            const color = readings.find(r => r.perception === WorldPerception.COLOR_DETECTION);
            return color ? color.description : "Aponta a camera que eu vejo a cor.";
        }
        if (intent === "emergency") return this.emergency("192");
        if (intent === "call") return "Para quem voce quer ligar?";
        if (intent === "see") return this.see_world();
        if (intent === "hear") return this.hear_world();
        if (intent === "navigate") return "Para onde voce quer ir?";
        if (this.user_emotion === EmotionalState.TIRED) return `${name}, voce parece cansado. Que tal uma pausa? Posso continuar depois.`;
        if (this.user_emotion === EmotionalState.STRESSED) return `Respira, ${name}. Uma coisa de cada vez. No que eu posso ajudar agora?`;
        if (this.user_emotion === EmotionalState.HAPPY) return `Que bom te ouvir feliz, ${name}! No que posso ajudar?`;
        return `Entendi. Conte mais, ${name}.`;
    }
    _record(text, speaker) {
        this.conversation_history.push({
            speaker, text, timestamp: Date.now() / 1000,
            emotion: speaker === "user" ? this.user_emotion : null
        });
        if (this.conversation_history.length > 500) this.conversation_history.shift();
    }
    conversation_summary() {
        return {
            telefonista_name: this.config.name, user_name: this.user_name,
            total_exchanges: this.conversation_history.length,
            current_emotion: this.user_emotion, current_mode: this.current_mode,
            active_sensors: this.active_sensors.size,
            children_tracked: Object.keys(this.children_tracked).length,
            personality: this.config.personality
        };
    }
}

// 6 factory functions
function create_telefonista_for_blind(user_name = "") {
    const cfg = new TelefonistaConfig();
    cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.GENTLE;
    cfg.speech_rate = 1.3; cfg.verbosity = 0.7; cfg.proactive = 0.6;
    const t = new Telefonista(cfg);
    t.user_name = user_name; t.user_disabilities = ["visual"];
    t.current_mode = ConversationMode.CO_DRIVER;
    return t;
}

function create_telefonista_for_deaf(user_name = "") {
    const cfg = new TelefonistaConfig();
    cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.GENTLE;
    cfg.speech_rate = 1.0; cfg.verbosity = 0.5;
    const t = new Telefonista(cfg);
    t.user_name = user_name; t.user_disabilities = ["auditiva"];
    t.current_mode = ConversationMode.SILENT;
    return t;
}

function create_telefonista_for_motor(user_name = "") {
    const cfg = new TelefonistaConfig();
    cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.CHEERFUL;
    cfg.speech_rate = 1.0; cfg.verbosity = 0.6; cfg.proactive = 0.5;
    const t = new Telefonista(cfg);
    t.user_name = user_name; t.user_disabilities = ["motora"];
    t.current_mode = ConversationMode.DIALOGUE;
    return t;
}

function create_telefonista_for_autism(user_name = "") {
    const cfg = new TelefonistaConfig();
    cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.GENTLE;
    cfg.speech_rate = 0.9; cfg.verbosity = 0.3; cfg.humor_enabled = false; cfg.proactive = 0.2;
    const t = new Telefonista(cfg);
    t.user_name = user_name; t.user_disabilities = ["espectro_autista"];
    t.current_mode = ConversationMode.DIALOGUE;
    return t;
}

function create_telefonista_for_child(user_name = "") {
    const cfg = new TelefonistaConfig();
    cfg.name = "Tia Iara"; cfg.personality = TelefonistaPersonality.PLAYFUL;
    cfg.speech_rate = 0.85; cfg.verbosity = 0.3; cfg.proactive = 0.4;
    const t = new Telefonista(cfg);
    t.user_name = user_name; t.user_disabilities = [];
    t.current_mode = ConversationMode.DIALOGUE;
    return t;
}

function create_telefonista_for_elderly(user_name = "") {
    const cfg = new TelefonistaConfig();
    cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.PROTECTIVE;
    cfg.speech_rate = 0.8; cfg.verbosity = 0.6; cfg.humor_enabled = true; cfg.proactive = 0.7; cfg.formality = 0.6;
    const t = new Telefonista(cfg);
    t.user_name = user_name; t.user_disabilities = [];
    t.current_mode = ConversationMode.DIALOGUE;
    return t;
}

// 7 scenario functions
function scenario_blind_walking() {
    console.log("=".repeat(60));
    console.log("CENARIO: Cego andando na rua");
    console.log("=".repeat(60));
    const t = create_telefonista_for_blind("Cleiton");
    console.log(t.greet("Cleiton", "manha"));
    console.log("\n[Camera]");
    console.log(t.see_world());
    console.log("\n[GPS]");
    console.log(t.navigate("padaria"));
    const readings = t.cv_engine.process_frame(SensorType.CAMERA_REAR);
    for (const r of readings) {
        if (r.perception === WorldPerception.MONEY_RECOGNITION) {
            console.log("\n[Dinheiro]"); console.log(r.description);
        }
    }
    console.log("\n[Audio]");
    console.log(t.hear_world());
}

function scenario_deaf_conversation() {
    console.log("\n" + "=".repeat(60));
    console.log("CENARIO: Surdo em conversa");
    console.log("=".repeat(60));
    const t = create_telefonista_for_deaf("Maria");
    console.log("[Visual] " + t.greet("Maria", "tarde"));
    console.log("\n[Audio -> Visual]");
    console.log("[Visual] " + t.hear_world());
}

function scenario_colorblind_shopping() {
    console.log("\n" + "=".repeat(60));
    console.log("CENARIO: Daltonico comprando roupas");
    console.log("=".repeat(60));
    const t = new Telefonista(new TelefonistaConfig());
    t.user_name = "Joao"; t.user_disabilities = ["visual"];
    console.log(t.greet("Joao", "tarde"));
    console.log("\n[Camera apontada para roupa]");
    const readings = t.cv_engine.process_frame(SensorType.CAMERA_REAR);
    for (const r of readings) if (r.perception === WorldPerception.COLOR_DETECTION) console.log("  " + r.description);
    console.log("\n[Camera apontada para semaforo]");
    for (const r of readings) if (r.perception === WorldPerception.TRAFFIC_LIGHT) console.log("  " + r.description);
}

function scenario_lost_child() {
    console.log("\n" + "=".repeat(60));
    console.log("CENARIO: Geolocalizacao de crianca");
    console.log("=".repeat(60));
    const t = new Telefonista(new TelefonistaConfig());
    t.config.personality = TelefonistaPersonality.PROTECTIVE;
    t.user_name = "Cleiton";
    const safe_zones = [
        { name: "Casa", lat: -23.55, lon: -46.63, radius_m: 200 },
        { name: "Escola", lat: -23.56, lon: -46.64, radius_m: 200 }
    ];
    console.log(t.register_child("child_01", "Sophia", "+551****9999", safe_zones));
    console.log("\n[Sophia na escola]");
    console.log(t.check_on_child("child_01", -23.56, -46.64, 85));
    console.log("\n[Sophia em local desconhecido]");
    let result = t.geo_engine.check_child_location("child_01", -23.60, -46.70, 45);
    console.log("  " + result.message);
    console.log("  Nivel: " + result.alert_level);
    console.log("\n[Sophia com bateria fraca]");
    result = t.geo_engine.check_child_location("child_01", -23.58, -46.66, 12);
    console.log("  " + result.message);
}

function scenario_fall_detection() {
    console.log("\n" + "=".repeat(60));
    console.log("CENARIO: Deteccao de queda (idoso)");
    console.log("=".repeat(60));
    const t = create_telefonista_for_elderly("Dona Maria");
    console.log(t.greet("Dona Maria", "manha"));
    console.log("\n[Queda detectada!]");
    console.log(t.sense_body(110, "fall", 98, 36.5));
    console.log("\n[Sem resposta em 30s]");
    console.log(t.emergency("192"));
}

function scenario_stress_detection() {
    console.log("\n" + "=".repeat(60));
    console.log("CENARIO: Deteccao de estresse");
    console.log("=".repeat(60));
    const t = new Telefonista(new TelefonistaConfig());
    t.user_name = "Cleiton";
    console.log("Coracao acelerado, voce esta parado...");
    console.log(t.sense_body(115, "normal", 98, 36.5));
    console.log("\nVoce diz: 'to estressado pra caralho'");
    console.log(t.listen_and_respond("to estressado pra caralho"));
}

function scenario_epilepsy_warning() {
    console.log("\n" + "=".repeat(60));
    console.log("CENARIO: Previsao de crise epileptica");
    console.log("=".repeat(60));
    const cfg = new TelefonistaConfig();
    cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.PROTECTIVE;
    const t = new Telefonista(cfg);
    t.user_name = "Pedro";
    console.log(t.greet("Pedro", "tarde"));
    console.log("\n[Sinais pre-crise]");
    console.log(t.sense_body(115, "normal", 98, 37.5));
}

// demo() como main()
function demo() {
    console.log("=".repeat(70));
    console.log("OpenTelefonista -- O Sistema Como Conversa Humana");
    console.log("=".repeat(70));
    console.log("\nTelefonista: Iara");
    console.log("Personalidades: " + Object.keys(TelefonistaPersonality).length);
    console.log("Estados emocionais: " + Object.keys(EmotionalState).length);
    console.log("Modos de conversa: " + Object.keys(ConversationMode).length);
    console.log("Tipos de sensor: " + Object.keys(SensorType).length);
    console.log("Percepcoes do mundo: " + Object.keys(WorldPerception).length);

    scenario_blind_walking();
    scenario_deaf_conversation();
    scenario_colorblind_shopping();
    scenario_lost_child();
    scenario_fall_detection();
    scenario_stress_detection();
    scenario_epilepsy_warning();

    console.log("\n" + "=".repeat(70));
    console.log("PERFIS DA TELEFONISTA");
    console.log("=".repeat(70));

    const profiles = {
        "Cego": create_telefonista_for_blind("Cleiton"),
        "Surdo": create_telefonista_for_deaf("Maria"),
        "Tetraplegico": create_telefonista_for_motor("Joao"),
        "Autista": create_telefonista_for_autism("Pedro"),
        "Crianca": create_telefonista_for_child("Sophia"),
        "Idoso": create_telefonista_for_elderly("Dona Cecca")
    };

    for (const [label, t] of Object.entries(profiles)) {
        console.log(`\n  ${label}:`);
        console.log(`    Nome: ${t.config.name}`);
        console.log(`    Personalidade: ${t.config.personality}`);
        console.log(`    Velocidade: ${t.config.speech_rate}x`);
        console.log(`    Modo: ${t.current_mode}`);
        console.log(`    Sensores ativos: ${t.active_sensors.size}`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("COBERTURA DE PERCEPCAO DO MUNDO");
    console.log("=".repeat(70));

    const perception_categories = {
        "VISAO (camera como olhos)": [
            WorldPerception.COLOR_DETECTION, WorldPerception.TEXT_RECOGNITION,
            WorldPerception.OBSTACLE_DETECTION, WorldPerception.TRAFFIC_LIGHT,
            WorldPerception.MONEY_RECOGNITION, WorldPerception.FACE_RECOGNITION,
            WorldPerception.CROSSWALK_DETECTION
        ],
        "AUDICAO (microfone como ouvidos)": [
            WorldPerception.SPEECH_TO_TEXT, WorldPerception.SOUND_CLASSIFICATION,
            WorldPerception.DOORBELL, WorldPerception.SIREN,
            WorldPerception.BABY_CRYING, WorldPerception.ALARM_SOUND
        ],
        "LOCALIZACAO (GPS como direcao)": [
            WorldPerception.GPS_LOCATION, WorldPerception.INDOOR_LOCATION,
            WorldPerception.DIRECTION_FACING, WorldPerception.LOST_CHILD,
            WorldPerception.NEARBY_PLACES
        ],
        "BIOMETRIA (smartwatch como corpo)": [
            WorldPerception.FALL_DETECTION, WorldPerception.HEART_ANOMALY,
            WorldPerception.STRESS_DETECTION, WorldPerception.SEIZURE_PREDICTION,
            WorldPerception.TREMOR_DETECTION
        ]
    };

    for (const [category, perceptions] of Object.entries(perception_categories)) {
        console.log(`\n  ${category}:`);
        for (const p of perceptions) console.log(`    - ${p}`);
    }

    console.log("\n" + "=".repeat(70));
    console.log(`Total percepcoes: ${Object.keys(WorldPerception).length}`);
    console.log(`Total sensores: ${Object.keys(SensorType).length}`);
    console.log(`Total personalidades: ${Object.keys(TelefonistaPersonality).length}`);
    console.log("\nO sistema NAO e um app. E uma CONVERSA.");
    console.log("A interface NAO e uma tela. E uma VOZ.");
    console.log("O smartphone NAO e um dispositivo. E o CORPO EXTENDIDO.");
    console.log("\nTODO hardware. TODA deficiencia. ZERO barreira.");
    console.log("UMA conversa.");
}

if (typeof require !== 'undefined' && require.main === module) {
    demo();
}

module.exports = {
    TelefonistaPersonality, EmotionalState, ConversationMode, TelefonistaConfig,
    SensorType, WorldPerception, SensorReading,
    ComputerVisionEngine, AudioPerceptionEngine, GeoLocationEngine, BiometricEngine, Telefonista,
    create_telefonista_for_blind, create_telefonista_for_deaf, create_telefonista_for_motor,
    create_telefonista_for_autism, create_telefonista_for_child, create_telefonista_for_elderly,
    scenario_blind_walking, scenario_deaf_conversation, scenario_colorblind_shopping,
    scenario_lost_child, scenario_fall_detection, scenario_stress_detection, scenario_epilepsy_warning,
    demo
};