// OpenTelefonista.java
// Transpilacao fiel de open_telefonista.py para Java
// Todas as enums, classes, funcoes, cenarios e demo() preservados.
// Comentarios em portugues. Sem abreviacoes.

import java.util.*;
import java.util.function.*;

public class open_telefonista {

    // ============================================================================
    // 1. PERSONALIDADE DA TELEFONISTA
    // ============================================================================

    public enum TelefonistaPersonality {
        GENTLE("gentil"), CHEERFUL("alegre"), SERIOUS("seria"),
        FRIENDLY("amiga"), FORMAL("formal"), PLAYFUL("brincalhona"),
        PROTECTIVE("protetora"), MINIMAL("minimal");
        public final String value;
        TelefonistaPersonality(String v) { this.value = v; }
    }

    public enum EmotionalState {
        HAPPY("feliz"), CALM("calmo"), FOCUSED("focado"), TIRED("cansado"),
        STRESSED("estressado"), ANXIOUS("ansioso"), SAD("triste"),
        ANGRY("irritado"), OVERWHELMED("sobrecarregado"), NEUTRAL("neutro");
        public final String value;
        EmotionalState(String v) { this.value = v; }
    }

    public enum ConversationMode {
        DIALOGUE("dialogo"), DICTATION("ditado"), NARRATION("narracao"),
        EMERGENCY("emergencia"), WHISPER("sussurro"), SILENT("silencioso"),
        CO_DRIVER("copiloto"), TEACHER("professora");
        public final String value;
        ConversationMode(String v) { this.value = v; }
    }

    public static class TelefonistaConfig {
        public String name = "Iara";
        public TelefonistaPersonality personality = TelefonistaPersonality.GENTLE;
        public String voice_id = "pt-BR-FemaleA";
        public double speech_rate = 1.0;
        public double formality = 0.3;
        public double verbosity = 0.5;
        public boolean humor_enabled = true;
        public double proactive = 0.3;
        public String language = "pt-BR";
        public boolean respects_silence = true;
        public boolean interruptible = true;
        public boolean emotional_adaptation = true;

        public void adapt_to_emotion(EmotionalState emotion) {
            if (emotion == EmotionalState.STRESSED || emotion == EmotionalState.ANXIOUS) {
                this.speech_rate = 0.85; this.verbosity = 0.3; this.humor_enabled = false;
                this.personality = TelefonistaPersonality.GENTLE;
            } else if (emotion == EmotionalState.TIRED) {
                this.speech_rate = 0.9; this.verbosity = 0.3; this.proactive = 0.1;
            } else if (emotion == EmotionalState.HAPPY) {
                this.humor_enabled = true; this.speech_rate = 1.1;
            } else if (emotion == EmotionalState.OVERWHELMED) {
                this.verbosity = 0.1; this.speech_rate = 0.8; this.proactive = 0.0;
            } else if (emotion == EmotionalState.FOCUSED) {
                this.verbosity = 0.2; this.humor_enabled = false; this.proactive = 0.1;
            }
        }
    }

    // ============================================================================
    // 2. CAPACIDADES DO SMARTPHONE COMO CORPO EXTENDIDO
    // ============================================================================

    public enum SensorType {
        CAMERA_REAR("camera_traseira"), CAMERA_FRONT("camera_frontal"),
        MICROPHONE("microfone"), GPS("gps"), ACCELEROMETER("acelerometro"),
        GYROSCOPE("giroscopio"), COMPASS("bussola"), BAROMETER("barometro"),
        THERMOMETER("termometro"), HUMIDITY("umidade"), LIGHT("luminosidade"),
        PROXIMITY("proximidade"), LIDAR("lidar"), TOF("tempo_de_voo"),
        HEART_RATE("frequencia_cardiaca"), SPO2("oxigenio"),
        SKIN_TEMP("temperatura_pele"), NFC("nfc"),
        BLUETOOTH_BEACON("beacon_bluetooth"), CELL_SIGNAL("sinal_celular");
        public final String value; SensorType(String v){this.value=v;}
    }

    public enum WorldPerception {
        // VISAO
        COLOR_DETECTION("deteccao_cor"), TEXT_RECOGNITION("reconhecimento_texto"),
        OBJECT_DETECTION("deteccao_objetos"), FACE_RECOGNITION("reconhecimento_facial"),
        OBSTACLE_DETECTION("deteccao_obstaculos"), CROSSWALK_DETECTION("deteccao_faixa"),
        TRAFFIC_LIGHT("semaforo"), SIGN_RECOGNITION("reconhecimento_placas"),
        DOCUMENT_SCAN("escaneamento_documento"), MONEY_RECOGNITION("reconhecimento_cedula"),
        PRODUCT_LABEL("rotulo_produto"),
        // AUDICAO
        SOUND_CLASSIFICATION("classificacao_som"), SPEAKER_RECOGNITION("reconhecimento_voz"),
        MUSIC_RECOGNITION("reconhecimento_musica"), SPEECH_TO_TEXT("fala_para_texto"),
        AMBIENT_NOISE("ruido_ambiente"), DOORBELL("campainha"),
        ALARM_SOUND("alarme"), SIREN("sirene"), BABY_CRYING("bebe_chorando"),
        DOG_BARKING("cachorro_latindo"),
        // LOCALIZACAO
        GPS_LOCATION("localizacao_gps"), INDOOR_LOCATION("localizacao_indoor"),
        DIRECTION_FACING("direcao"), ALTITUDE("altitude"), SPEED("velocidade"),
        NEARBY_PLACES("lugares_proximos"), GEOCODING("geocoding"),
        LOST_CHILD("crianca_perdida"),
        // BIOMETRIA
        FALL_DETECTION("deteccao_queda"), HEART_ANOMALY("anomalia_cardiaca"),
        STRESS_DETECTION("deteccao_stress"), SEIZURE_PREDICTION("previsao_crise"),
        TREMOR_DETECTION("deteccao_tremor"), POSTURE("postura"),
        // AMBIENTE
        TEMPERATURE("temperatura_ambiente"), AIR_QUALITY("qualidade_ar"),
        UV_INDEX("indice_uv"), WEATHER("clima");
        public final String value; WorldPerception(String v){this.value=v;}
    }

    public static class SensorReading {
        public SensorType sensor;
        public WorldPerception perception;
        public Object value;
        public double confidence;
        public double timestamp;
        public String description;
        public SensorReading(SensorType s, WorldPerception p, Object v, double c, String d) {
            this.sensor = s; this.perception = p; this.value = v; this.confidence = c;
            this.timestamp = System.currentTimeMillis()/1000.0; this.description = d;
        }
    }

    // ============================================================================
    // 3. VISAO COMPUTACIONAL
    // ============================================================================

    public static class ComputerVisionEngine {
        public List<WorldPerception> active_perceptions = new ArrayList<>();
        public Deque<SensorReading> last_readings = new ArrayDeque<>(100);

        public List<SensorReading> process_frame(SensorType sensor, Object frame_data) {
            List<SensorReading> readings = new ArrayList<>();
            readings.add(new SensorReading(sensor, WorldPerception.COLOR_DETECTION,
                Map.of("color_name","vermelho","hex","#FF0000","rgb",Arrays.asList(255,0,0)),
                0.95, "Aqui e VERMELHO. A luz do semaforo esta VERMELHA. Pare."));
            readings.add(new SensorReading(sensor, WorldPerception.OBSTACLE_DETECTION,
                Map.of("obstacle","poste","distance_m",2.5,"direction","frente-esquerda"),
                0.88, "Poste a 2.5 metros a frente e a esquerda. Desvie para a direita."));
            readings.add(new SensorReading(sensor, WorldPerception.TEXT_RECOGNITION,
                Map.of("text","RESTAURANTE JOAO","location","acima da porta"),
                0.92, "Placa diz: RESTAURANTE JOAO. Fica acima da porta a frente."));
            readings.add(new SensorReading(sensor, WorldPerception.TRAFFIC_LIGHT,
                Map.of("color","verde","action","siga"),
                0.97, "Semaforo VERDE. Pode atravessar."));
            readings.add(new SensorReading(sensor, WorldPerception.MONEY_RECOGNITION,
                Map.of("denomination","R$ 50,00","color_pattern","marrom"),
                0.94, "Isso e uma nota de CINQUENTA REAIS."));
            for (SensorReading r : readings) last_readings.addLast(r);
            if (last_readings.size() > 100) last_readings.removeFirst();
            return readings;
        }

        public String narrate_scene(List<SensorReading> readings, String user_disability) {
            if (readings.isEmpty()) return "Nao consigo ver nada claramente agora.";
            List<String> parts = new ArrayList<>();
            for (SensorReading r : readings) if (r.confidence > 0.7) parts.add(r.description);
            if (parts.isEmpty()) return "Ambiente visual incerto. Vou continuar observando.";
            return String.join(". ", parts) + ".";
        }
    }

    // ============================================================================
    // 4. AUDIO
    // ============================================================================

    public static class AudioPerceptionEngine {
        public Deque<SensorReading> last_readings = new ArrayDeque<>(100);
        public Deque<SensorReading> sound_buffer = new ArrayDeque<>(30);

        public List<SensorReading> process_audio() {
            List<SensorReading> readings = new ArrayList<>();
            readings.add(new SensorReading(SensorType.MICROPHONE, WorldPerception.SPEECH_TO_TEXT,
                Map.of("speaker","homem","text","Bom dia, como vai?"),
                0.90, "Um homem disse: Bom dia, como vai?"));
            readings.add(new SensorReading(SensorType.MICROPHONE, WorldPerception.SOUND_CLASSIFICATION,
                Map.of("sound","sirene","direction","direita","approaching",true),
                0.85, "Sirene de ambulancia se aproximando pela direita."));
            readings.add(new SensorReading(SensorType.MICROPHONE, WorldPerception.DOORBELL,
                Map.of("detected",true,"count",2),
                0.95, "Alguem tocou a campainha. Duas vezes."));
            readings.add(new SensorReading(SensorType.MICROPHONE, WorldPerception.BABY_CRYING,
                Map.of("detected",true,"intensity","alta"),
                0.93, "O bebe esta chorando. Intensidade alta."));
            for (SensorReading r : readings) last_readings.addLast(r);
            if (last_readings.size() > 100) last_readings.removeFirst();
            return readings;
        }

        public String narrate_sounds(List<SensorReading> readings) {
            if (readings.isEmpty()) return "Silencio.";
            List<String> parts = new ArrayList<>();
            for (SensorReading r : readings) if (r.confidence > 0.7) parts.add(r.description);
            return parts.isEmpty() ? "Nao identifico sons especificos." : String.join(". ", parts) + ".";
        }
    }

    // ============================================================================
    // 5. GEOLOCALIZACAO
    // ============================================================================

    public static class GeoLocationEngine {
        public double[] last_known_location = {-23.55, -46.63};
        public Map<String, Map<String,Object>> tracked_persons = new HashMap<>();
        public List<Map<String,Object>> safe_zones = new ArrayList<>();
        public Deque<SensorReading> last_readings = new ArrayDeque<>(100);

        public SensorReading update_location(double lat, double lon) {
            last_known_location = new double[]{lat, lon};
            SensorReading r = new SensorReading(SensorType.GPS, WorldPerception.GPS_LOCATION,
                Map.of("lat",lat,"lon",lon), 0.98, String.format("Voce esta proximo a %.4f, %.4f.", lat, lon));
            last_readings.addLast(r);
            return r;
        }

        public String navigate_for_blind(String destination) {
            return "Voce esta na rua Augusta, numero 1000.";
        }

        public Map<String,Object> track_child(String child_id, String child_name, String child_phone, List<Map<String,Object>> safe_zones) {
            Map<String,Object> child = new HashMap<>();
            child.put("name", child_name); child.put("phone", child_phone);
            child.put("last_location", null); child.put("last_update", System.currentTimeMillis()/1000.0);
            child.put("safe_zones", safe_zones != null ? safe_zones : new ArrayList<>());
            child.put("status", "safe"); child.put("battery", 100);
            tracked_persons.put(child_id, child);
            if (safe_zones != null) this.safe_zones = safe_zones;
            return child;
        }

        public Map<String,Object> check_child_location(String child_id, double lat, double lon, int battery) {
            if (!tracked_persons.containsKey(child_id)) return Map.of("error","crianca nao registrada");
            Map<String,Object> child = tracked_persons.get(child_id);
            child.put("last_location", new double[]{lat,lon});
            child.put("last_update", System.currentTimeMillis()/1000.0);
            child.put("battery", battery);
            boolean in_safe = false;
            Map<String,Object> zoneHit = null;
            for (Map<String,Object> zone : (List<Map<String,Object>>)child.getOrDefault("safe_zones", List.of())) {
                double d = _haversine(lat, lon, (double)zone.get("lat"), (double)zone.get("lon"));
                if (d <= (double)zone.getOrDefault("radius_m", 200.0)) { in_safe = true; zoneHit = zone; break; }
            }
            if (in_safe) {
                child.put("status","safe");
                return Map.of("child_id",child_id,"name",child.get("name"),"status","safe",
                    "location",new double[]{lat,lon},"zone",zoneHit!=null?zoneHit.get("name"):"zona segura",
                    "battery",battery,"message",child.get("name")+" esta na zona segura.");
            } else {
                child.put("status","outside");
                double minDist = 999999;
                String nearest = "";
                for (Map<String,Object> zone : (List<Map<String,Object>>)child.getOrDefault("safe_zones", List.of())) {
                    double d = _haversine(lat, lon, (double)zone.get("lat"), (double)zone.get("lon"));
                    if (d < minDist) { minDist = d; nearest = (String)zone.getOrDefault("name","zona"); }
                }
                return Map.of("child_id",child_id,"name",child.get("name"),"status","outside_safe_zone",
                    "location",new double[]{lat,lon},"distance_from_nearest_safe_m",Math.round(minDist),
                    "nearest_zone",nearest,"battery",battery,
                    "message","ATENCAO: "+child.get("name")+" saiu da zona segura. Esta a "+Math.round(minDist)+" metros de "+nearest+". Bateria: "+battery+"%.",
                    "alert_level", minDist < 1000 ? "warning" : "critical");
            }
        }

        public List<Map<String,Object>> find_nearby_help(String help_type) {
            return List.of(
                Map.of("name","Hospital Sao Paulo","distance_m",800,"direction","norte"),
                Map.of("name","UBS Vila Mariana","distance_m",1200,"direction","leste"),
                Map.of("name","Farmacia 24h","distance_m",300,"direction","oeste")
            );
        }

        private double _haversine(double lat1, double lon1, double lat2, double lon2) {
            double R = 6371000;
            double dlat = Math.toRadians(lat2-lat1);
            double dlon = Math.toRadians(lon2-lon1);
            double a = Math.sin(dlat/2)*Math.sin(dlat/2) + Math.cos(Math.toRadians(lat1))*Math.cos(Math.toRadians(lat2))*Math.sin(dlon/2)*Math.sin(dlon/2);
            double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
            return R * c;
        }
    }

    // ============================================================================
    // 6. BIOMETRIA
    // ============================================================================

    public static class BiometricEngine {
        public Deque<SensorReading> last_readings = new ArrayDeque<>(1000);
        public int baseline_heart_rate = 75;
        public boolean fall_detected = false;

        public List<SensorReading> process_biometrics(int heart_rate, int spo2, double skin_temp, String movement) {
            List<SensorReading> readings = new ArrayList<>();
            if ("fall".equals(movement)) {
                fall_detected = true;
                readings.add(new SensorReading(SensorType.ACCELEROMETER, WorldPerception.FALL_DETECTION,
                    Map.of("detected",true,"impact_g",3.2), 0.92,
                    "QUEDA DETECTADA. Voce esta bem? Responda em 30 segundos ou ligo para emergencia."));
            }
            if (heart_rate > 120 || heart_rate < 50) {
                readings.add(new SensorReading(SensorType.HEART_RATE, WorldPerception.HEART_ANOMALY,
                    Map.of("heart_rate",heart_rate,"baseline",baseline_heart_rate), 0.85,
                    "Frequencia cardiaca "+heart_rate+" bpm. Isso esta fora do normal."));
            }
            if (heart_rate > 100 && "normal".equals(movement)) {
                readings.add(new SensorReading(SensorType.HEART_RATE, WorldPerception.STRESS_DETECTION,
                    Map.of("heart_rate",heart_rate,"hrv_low",true), 0.70,
                    "Seu coracao esta acelerado e voce esta parado. Talvez estresse. Quer respirar comigo?"));
            }
            if (skin_temp > 37.0 && heart_rate > 110) {
                readings.add(new SensorReading(SensorType.SKIN_TEMP, WorldPerception.SEIZURE_PREDICTION,
                    Map.of("skin_temp",skin_temp,"heart_rate",heart_rate,"risk","moderate"), 0.60,
                    "Sinais que podem preceder uma crise. Sente-se em local seguro."));
            }
            if ("tremor".equals(movement)) {
                readings.add(new SensorReading(SensorType.ACCELEROMETER, WorldPerception.TREMOR_DETECTION,
                    Map.of("frequency_hz",5.0,"amplitude","moderate"), 0.80,
                    "Tremor detectado. Vou ajustar a sensibilidade dos botoes."));
            }
            for (SensorReading r : readings) last_readings.addLast(r);
            return readings;
        }
    }

    // ============================================================================
    // 7. TELEFONISTA
    // ============================================================================

    public static class Telefonista {
        public TelefonistaConfig config;
        public ComputerVisionEngine cv_engine = new ComputerVisionEngine();
        public AudioPerceptionEngine audio_engine = new AudioPerceptionEngine();
        public GeoLocationEngine geo_engine = new GeoLocationEngine();
        public BiometricEngine bio_engine = new BiometricEngine();
        public Deque<Map<String,Object>> conversation_history = new ArrayDeque<>(500);
        public EmotionalState user_emotion = EmotionalState.NEUTRAL;
        public ConversationMode current_mode = ConversationMode.DIALOGUE;
        public Set<SensorType> active_sensors = new HashSet<>();
        public String user_name = "";
        public List<String> user_disabilities = new ArrayList<>();
        public Map<String,String> children_tracked = new HashMap<>();

        public Telefonista(TelefonistaConfig cfg) {
            this.config = cfg;
            _setup_sensors();
        }

        private void _setup_sensors() {
            active_sensors.addAll(Arrays.asList(
                SensorType.CAMERA_REAR, SensorType.CAMERA_FRONT, SensorType.MICROPHONE,
                SensorType.GPS, SensorType.ACCELEROMETER, SensorType.GYROSCOPE,
                SensorType.COMPASS, SensorType.LIGHT, SensorType.PROXIMITY
            ));
        }

        public String greet(String user_name, String time_of_day) {
            this.user_name = user_name;
            String g = switch(time_of_day) {
                case "manha" -> "Bom dia"; case "tarde" -> "Boa tarde"; case "noite" -> "Boa noite";
                default -> "Ola";
            };
            String msg;
            if (config.personality == TelefonistaPersonality.GENTLE)
                msg = g + ", " + user_name + ". Aqui e a " + config.name + ". ";
            else if (config.personality == TelefonistaPersonality.CHEERFUL)
                msg = g + ", " + user_name + "! Que bom te ouvir! ";
            else if (config.personality == TelefonistaPersonality.FORMAL)
                msg = g + ". " + config.name + " a servico. ";
            else msg = g + ", " + user_name + ". ";
            _record(msg, "telefonista");
            return msg;
        }

        public String listen_and_respond(String user_input) {
            _record(user_input, "user");
            EmotionalState emotion = _detect_emotion(user_input);
            if (emotion != user_emotion) {
                user_emotion = emotion;
                if (config.emotional_adaptation) config.adapt_to_emotion(emotion);
            }
            String intent = _detect_intent(user_input);
            String response = _respond(intent, user_input);
            _record(response, "telefonista");
            return response;
        }

        public String see_world() {
            List<SensorReading> readings = cv_engine.process_frame(SensorType.CAMERA_REAR, null);
            String narration = cv_engine.narrate_scene(readings, String.join(", ", user_disabilities));
            _record(narration, "telefonista");
            return narration;
        }

        public String hear_world() {
            List<SensorReading> readings = audio_engine.process_audio();
            String narration = audio_engine.narrate_sounds(readings);
            _record(narration, "telefonista");
            return narration;
        }

        public String sense_body(int heart_rate, String movement, int spo2, double skin_temp) {
            List<SensorReading> readings = bio_engine.process_biometrics(heart_rate, spo2, skin_temp, movement);
            if (readings.isEmpty()) return "Tudo normal com seu corpo.";
            List<String> messages = new ArrayList<>();
            for (SensorReading r : readings) messages.add(r.description);
            String msg = String.join(" ", messages);
            _record(msg, "telefonista");
            return msg;
        }

        public String navigate(String destination) {
            current_mode = ConversationMode.CO_DRIVER;
            String instruction = geo_engine.navigate_for_blind(destination);
            _record(instruction, "telefonista");
            return instruction;
        }

        public String check_on_child(String child_id, double lat, double lon, int battery) {
            Map<String,Object> result = geo_engine.check_child_location(child_id, lat, lon, battery);
            String msg = (String)result.getOrDefault("message", "Sem informacoes.");
            _record(msg, "telefonista");
            return msg;
        }

        public String register_child(String child_id, String name, String phone, List<Map<String,Object>> safe_zones) {
            geo_engine.track_child(child_id, name, phone, safe_zones);
            children_tracked.put(child_id, name);
            String msg = name + " registrada. Vou avisar se ela sair das zonas seguras.";
            _record(msg, "telefonista");
            return msg;
        }

        public String find_help(String help_type) {
            List<Map<String,Object>> results = geo_engine.find_nearby_help(help_type);
            if (results.isEmpty()) return "Nao encontrei nada proximo agora.";
            List<String> parts = new ArrayList<>();
            for (Map<String,Object> r : results)
                parts.add(r.get("name") + " a " + r.get("distance_m") + " metros ao " + r.get("direction"));
            String msg = "Encontrei: " + String.join(". ", parts) + ".";
            _record(msg, "telefonista");
            return msg;
        }

        public String make_call(String contact_name, String reason) {
            String reason_text = reason.isEmpty() ? "" : " Motivo: " + reason + ".";
            String msg = "Ligando para " + contact_name + "." + reason_text;
            _record(msg, "telefonista");
            return msg;
        }

        public String emergency(String service) {
            current_mode = ConversationMode.EMERGENCY;
            config.personality = TelefonistaPersonality.PROTECTIVE;
            config.speech_rate = 0.9; config.humor_enabled = false; config.verbosity = 0.2;
            String msg = "EMERGENCIA. Ligando para " + service + ". Fique calmo. Estou aqui.";
            _record(msg, "telefonista");
            return msg;
        }

        public String dictate_code(String code_input) {
            current_mode = ConversationMode.DICTATION;
            String msg = "Anotado. Escrevi: " + code_input + ". Quer que eu execute?";
            _record(msg, "telefonista");
            return msg;
        }

        private EmotionalState _detect_emotion(String text) {
            String t = text.toLowerCase();
            if (t.contains("cansado")||t.contains("exausto")||t.contains("durmo")) return EmotionalState.TIRED;
            if (t.contains("estress")||t.contains("put")||t.contains("merda")||t.contains("porra")) return EmotionalState.STRESSED;
            if (t.contains("ansios")||t.contains("preocup")||t.contains("medo")) return EmotionalState.ANXIOUS;
            if (t.contains("feliz")||t.contains("otimo")||t.contains("show")||t.contains("massa")) return EmotionalState.HAPPY;
            if (t.contains("foco")||t.contains("trabalh")||t.contains("concentrad")) return EmotionalState.FOCUSED;
            if (t.contains("triste")||t.contains("para")||t.contains("desanim")) return EmotionalState.SAD;
            if (t.contains("irritad")||t.contains("irritante")||t.contains("raiva")) return EmotionalState.ANGRY;
            if (t.contains("muito")||t.contains("sobrecarreg")||t.contains("nao aguento")) return EmotionalState.OVERWHELMED;
            return EmotionalState.NEUTRAL;
        }

        private String _detect_intent(String text) {
            String t = text.toLowerCase();
            if (t.contains("codigo")||t.contains("programar")||t.contains("funcao")||t.contains("variavel")) return "code";
            if (t.contains("onde estou")||t.contains("localizacao")||t.contains("rua")) return "location";
            if (t.contains("minha filha")||t.contains("meu filho")||t.contains("crianca")) return "child";
            if (t.contains("cor")||t.contains("cela")||t.contains("vermelho")||t.contains("verde")||t.contains("azul")) return "color";
            if (t.contains("socorro")||t.contains("emergencia")||t.contains("ajuda")||t.contains("190")||t.contains("192")) return "emergency";
            if (t.contains("ligar")||t.contains("telefone")||t.contains("chamada")) return "call";
            if (t.contains("ve")||t.contains("olha")||t.contains("camera")||t.contains("enxergar")) return "see";
            if (t.contains("ouvir")||t.contains("som")||t.contains("barulho")) return "hear";
            if (t.contains("navegar")||t.contains("ir para")||t.contains("como chego")) return "navigate";
            return "chat";
        }

        private String _respond(String intent, String user_input) {
            String name = user_name.isEmpty() ? "amigo" : user_name;
            if ("code".equals(intent)) return dictate_code(user_input);
            if ("location".equals(intent)) return geo_engine.navigate_for_blind("");
            if ("child".equals(intent)) return "Quer que eu verifique onde ela esta?";
            if ("color".equals(intent)) {
                List<SensorReading> readings = cv_engine.process_frame(SensorType.CAMERA_REAR, null);
                for (SensorReading r : readings)
                    if (r.perception == WorldPerception.COLOR_DETECTION) return r.description;
                return "Aponta a camera que eu vejo a cor.";
            }
            if ("emergency".equals(intent)) return emergency("192");
            if ("call".equals(intent)) return "Para quem voce quer ligar?";
            if ("see".equals(intent)) return see_world();
            if ("hear".equals(intent)) return hear_world();
            if ("navigate".equals(intent)) return "Para onde voce quer ir?";
            if (user_emotion == EmotionalState.TIRED) return name + ", voce parece cansado. Que tal uma pausa? Posso continuar depois.";
            if (user_emotion == EmotionalState.STRESSED) return "Respira, " + name + ". Uma coisa de cada vez. No que eu posso ajudar agora?";
            if (user_emotion == EmotionalState.HAPPY) return "Que bom te ouvir feliz, " + name + "! No que posso ajudar?";
            return "Entendi. Conte mais, " + name + ".";
        }

        private void _record(String text, String speaker) {
            Map<String,Object> entry = new HashMap<>();
            entry.put("speaker", speaker); entry.put("text", text);
            entry.put("timestamp", System.currentTimeMillis()/1000.0);
            entry.put("emotion", speaker.equals("user") ? user_emotion.value : null);
            conversation_history.addLast(entry);
            if (conversation_history.size() > 500) conversation_history.removeFirst();
        }

        public Map<String,Object> conversation_summary() {
            Map<String,Object> sum = new HashMap<>();
            sum.put("telefonista_name", config.name);
            sum.put("user_name", user_name);
            sum.put("total_exchanges", conversation_history.size());
            sum.put("current_emotion", user_emotion.value);
            sum.put("current_mode", current_mode.value);
            sum.put("active_sensors", active_sensors.size());
            sum.put("children_tracked", children_tracked.size());
            sum.put("personality", config.personality.value);
            return sum;
        }
    }

    // ============================================================================
    // 8. ADAPTACAO POR DEFICIENCIA (6 factories)
    // ============================================================================

    public static Telefonista create_telefonista_for_blind(String user_name) {
        TelefonistaConfig cfg = new TelefonistaConfig();
        cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.GENTLE;
        cfg.speech_rate = 1.3; cfg.verbosity = 0.7; cfg.proactive = 0.6;
        Telefonista t = new Telefonista(cfg);
        t.user_name = user_name; t.user_disabilities = List.of("visual");
        t.current_mode = ConversationMode.CO_DRIVER;
        return t;
    }

    public static Telefonista create_telefonista_for_deaf(String user_name) {
        TelefonistaConfig cfg = new TelefonistaConfig();
        cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.GENTLE;
        cfg.speech_rate = 1.0; cfg.verbosity = 0.5;
        Telefonista t = new Telefonista(cfg);
        t.user_name = user_name; t.user_disabilities = List.of("auditiva");
        t.current_mode = ConversationMode.SILENT;
        return t;
    }

    public static Telefonista create_telefonista_for_motor(String user_name) {
        TelefonistaConfig cfg = new TelefonistaConfig();
        cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.CHEERFUL;
        cfg.speech_rate = 1.0; cfg.verbosity = 0.6; cfg.proactive = 0.5;
        Telefonista t = new Telefonista(cfg);
        t.user_name = user_name; t.user_disabilities = List.of("motora");
        t.current_mode = ConversationMode.DIALOGUE;
        return t;
    }

    public static Telefonista create_telefonista_for_autism(String user_name) {
        TelefonistaConfig cfg = new TelefonistaConfig();
        cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.GENTLE;
        cfg.speech_rate = 0.9; cfg.verbosity = 0.3; cfg.humor_enabled = false; cfg.proactive = 0.2;
        Telefonista t = new Telefonista(cfg);
        t.user_name = user_name; t.user_disabilities = List.of("espectro_autista");
        t.current_mode = ConversationMode.DIALOGUE;
        return t;
    }

    public static Telefonista create_telefonista_for_child(String user_name) {
        TelefonistaConfig cfg = new TelefonistaConfig();
        cfg.name = "Tia Iara"; cfg.personality = TelefonistaPersonality.PLAYFUL;
        cfg.speech_rate = 0.85; cfg.verbosity = 0.3; cfg.proactive = 0.4;
        Telefonista t = new Telefonista(cfg);
        t.user_name = user_name; t.user_disabilities = List.of();
        t.current_mode = ConversationMode.DIALOGUE;
        return t;
    }

    public static Telefonista create_telefonista_for_elderly(String user_name) {
        TelefonistaConfig cfg = new TelefonistaConfig();
        cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.PROTECTIVE;
        cfg.speech_rate = 0.8; cfg.verbosity = 0.6; cfg.humor_enabled = true; cfg.proactive = 0.7; cfg.formality = 0.6;
        Telefonista t = new Telefonista(cfg);
        t.user_name = user_name; t.user_disabilities = List.of();
        t.current_mode = ConversationMode.DIALOGUE;
        return t;
    }

    // ============================================================================
    // 9. CENARIOS DO MUNDO REAL (7 cenarios)
    // ============================================================================

    public static void scenario_blind_walking() {
        System.out.println("=".repeat(60));
        System.out.println("CENARIO: Cego andando na rua");
        System.out.println("=".repeat(60));
        Telefonista t = create_telefonista_for_blind("Cleiton");
        System.out.println(t.greet("Cleiton", "manha"));
        System.out.println("\n[Camera]");
        System.out.println(t.see_world());
        System.out.println("\n[GPS]");
        System.out.println(t.navigate("padaria"));
        List<SensorReading> readings = t.cv_engine.process_frame(SensorType.CAMERA_REAR, null);
        for (SensorReading r : readings) {
            if (r.perception == WorldPerception.MONEY_RECOGNITION) {
                System.out.println("\n[Dinheiro]"); System.out.println(r.description);
            }
        }
        System.out.println("\n[Audio]");
        System.out.println(t.hear_world());
    }

    public static void scenario_deaf_conversation() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("CENARIO: Surdo em conversa");
        System.out.println("=".repeat(60));
        Telefonista t = create_telefonista_for_deaf("Maria");
        System.out.println("[Visual] " + t.greet("Maria", "tarde"));
        System.out.println("\n[Audio -> Visual]");
        System.out.println("[Visual] " + t.hear_world());
    }

    public static void scenario_colorblind_shopping() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("CENARIO: Daltonico comprando roupas");
        System.out.println("=".repeat(60));
        Telefonista t = new Telefonista(new TelefonistaConfig());
        t.user_name = "Joao"; t.user_disabilities = List.of("visual");
        System.out.println(t.greet("Joao", "tarde"));
        System.out.println("\n[Camera apontada para roupa]");
        List<SensorReading> readings = t.cv_engine.process_frame(SensorType.CAMERA_REAR, null);
        for (SensorReading r : readings) if (r.perception == WorldPerception.COLOR_DETECTION) System.out.println("  " + r.description);
        System.out.println("\n[Camera apontada para semaforo]");
        for (SensorReading r : readings) if (r.perception == WorldPerception.TRAFFIC_LIGHT) System.out.println("  " + r.description);
    }

    public static void scenario_lost_child() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("CENARIO: Geolocalizacao de crianca");
        System.out.println("=".repeat(60));
        Telefonista t = new Telefonista(new TelefonistaConfig());
        t.config.personality = TelefonistaPersonality.PROTECTIVE;
        t.user_name = "Cleiton";
        List<Map<String,Object>> safe_zones = List.of(
            Map.of("name","Casa","lat",-23.55,"lon",-46.63,"radius_m",200.0),
            Map.of("name","Escola","lat",-23.56,"lon",-46.64,"radius_m",200.0)
        );
        System.out.println(t.register_child("child_01", "Sophia", "+551****9999", safe_zones));
        System.out.println("\n[Sophia na escola]");
        System.out.println(t.check_on_child("child_01", -23.56, -46.64, 85));
        System.out.println("\n[Sophia em local desconhecido]");
        Map<String,Object> result = t.geo_engine.check_child_location("child_01", -23.60, -46.70, 45);
        System.out.println("  " + result.get("message"));
        System.out.println("  Nivel: " + result.getOrDefault("alert_level","info"));
        System.out.println("\n[Sophia com bateria fraca]");
        result = t.geo_engine.check_child_location("child_01", -23.58, -46.66, 12);
        System.out.println("  " + result.get("message"));
    }

    public static void scenario_fall_detection() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("CENARIO: Deteccao de queda (idoso)");
        System.out.println("=".repeat(60));
        Telefonista t = create_telefonista_for_elderly("Dona Maria");
        System.out.println(t.greet("Dona Maria", "manha"));
        System.out.println("\n[Queda detectada!]");
        System.out.println(t.sense_body(110, "fall", 98, 36.5));
        System.out.println("\n[Sem resposta em 30s]");
        System.out.println(t.emergency("192"));
    }

    public static void scenario_stress_detection() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("CENARIO: Deteccao de estresse");
        System.out.println("=".repeat(60));
        Telefonista t = new Telefonista(new TelefonistaConfig());
        t.user_name = "Cleiton";
        System.out.println("Coracao acelerado, voce esta parado...");
        System.out.println(t.sense_body(115, "normal", 98, 36.5));
        System.out.println("\nVoce diz: 'to estressado pra caralho'");
        System.out.println(t.listen_and_respond("to estressado pra caralho"));
    }

    public static void scenario_epilepsy_warning() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("CENARIO: Previsao de crise epileptica");
        System.out.println("=".repeat(60));
        TelefonistaConfig cfg = new TelefonistaConfig();
        cfg.name = "Iara"; cfg.personality = TelefonistaPersonality.PROTECTIVE;
        Telefonista t = new Telefonista(cfg);
        t.user_name = "Pedro";
        System.out.println(t.greet("Pedro", "tarde"));
        System.out.println("\n[Sinais pre-crise]");
        System.out.println(t.sense_body(115, "normal", 98, 37.5));
    }

    // ============================================================================
    // 10. DEMONSTRACAO COMPLETA (demo como main)
    // ============================================================================

    public static void demo() {
        System.out.println("=".repeat(70));
        System.out.println("OpenTelefonista -- O Sistema Como Conversa Humana");
        System.out.println("=".repeat(70));
        System.out.println("\nTelefonista: Iara");
        System.out.println("Personalidades: " + TelefonistaPersonality.values().length);
        System.out.println("Estados emocionais: " + EmotionalState.values().length);
        System.out.println("Modos de conversa: " + ConversationMode.values().length);
        System.out.println("Tipos de sensor: " + SensorType.values().length);
        System.out.println("Percepcoes do mundo: " + WorldPerception.values().length);

        scenario_blind_walking();
        scenario_deaf_conversation();
        scenario_colorblind_shopping();
        scenario_lost_child();
        scenario_fall_detection();
        scenario_stress_detection();
        scenario_epilepsy_warning();

        System.out.println("\n" + "=".repeat(70));
        System.out.println("PERFIS DA TELEFONISTA");
        System.out.println("=".repeat(70));

        Map<String, Telefonista> profiles = new LinkedHashMap<>();
        profiles.put("Cego", create_telefonista_for_blind("Cleiton"));
        profiles.put("Surdo", create_telefonista_for_deaf("Maria"));
        profiles.put("Tetraplegico", create_telefonista_for_motor("Joao"));
        profiles.put("Autista", create_telefonista_for_autism("Pedro"));
        profiles.put("Crianca", create_telefonista_for_child("Sophia"));
        profiles.put("Idoso", create_telefonista_for_elderly("Dona Cecca"));

        for (Map.Entry<String, Telefonista> e : profiles.entrySet()) {
            Telefonista t = e.getValue();
            System.out.println("\n  " + e.getKey() + ":");
            System.out.println("    Nome: " + t.config.name);
            System.out.println("    Personalidade: " + t.config.personality.value);
            System.out.println("    Velocidade: " + t.config.speech_rate + "x");
            System.out.println("    Modo: " + t.current_mode.value);
            System.out.println("    Sensores ativos: " + t.active_sensors.size());
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("COBERTURA DE PERCEPCAO DO MUNDO");
        System.out.println("=".repeat(70));

        Map<String, List<WorldPerception>> perception_categories = new LinkedHashMap<>();
        perception_categories.put("VISAO (camera como olhos)", List.of(
            WorldPerception.COLOR_DETECTION, WorldPerception.TEXT_RECOGNITION,
            WorldPerception.OBSTACLE_DETECTION, WorldPerception.TRAFFIC_LIGHT,
            WorldPerception.MONEY_RECOGNITION, WorldPerception.FACE_RECOGNITION,
            WorldPerception.CROSSWALK_DETECTION));
        perception_categories.put("AUDICAO (microfone como ouvidos)", List.of(
            WorldPerception.SPEECH_TO_TEXT, WorldPerception.SOUND_CLASSIFICATION,
            WorldPerception.DOORBELL, WorldPerception.SIREN,
            WorldPerception.BABY_CRYING, WorldPerception.ALARM_SOUND));
        perception_categories.put("LOCALIZACAO (GPS como direcao)", List.of(
            WorldPerception.GPS_LOCATION, WorldPerception.INDOOR_LOCATION,
            WorldPerception.DIRECTION_FACING, WorldPerception.LOST_CHILD,
            WorldPerception.NEARBY_PLACES));
        perception_categories.put("BIOMETRIA (smartwatch como corpo)", List.of(
            WorldPerception.FALL_DETECTION, WorldPerception.HEART_ANOMALY,
            WorldPerception.STRESS_DETECTION, WorldPerception.SEIZURE_PREDICTION,
            WorldPerception.TREMOR_DETECTION));

        for (Map.Entry<String, List<WorldPerception>> cat : perception_categories.entrySet()) {
            System.out.println("\n  " + cat.getKey() + ":");
            for (WorldPerception p : cat.getValue()) System.out.println("    - " + p.value);
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("Total percepcoes: " + WorldPerception.values().length);
        System.out.println("Total sensores: " + SensorType.values().length);
        System.out.println("Total personalidades: " + TelefonistaPersonality.values().length);
        System.out.println("\nO sistema NAO e um app. E uma CONVERSA.");
        System.out.println("A interface NAO e uma tela. E uma VOZ.");
        System.out.println("O smartphone NAO e um dispositivo. E o CORPO EXTENDIDO.");
        System.out.println("\nTODO hardware. TODA deficiencia. ZERO barreira.");
        System.out.println("UMA conversa.");
    }

    public static void main(String[] args) {
        demo();
    }
}