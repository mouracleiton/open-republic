// OpenHumanNet.java
// Transpilacao completa de open_human_net.py para Java
// Comentarios em portugues. Todas as enums, classes, funcoes e cenarios preservados.
// Demo() como main().

import java.util.*;
import java.util.concurrent.*;
import java.time.*;

enum TrustRing {
    FAMILY(0), CAREGIVER(1), COMMUNITY(2), PROFESSIONAL(3), EMERGENCY(4), BYSTANDER(5);
    public final int value;
    TrustRing(int v) { this.value = v; }
}

enum AuthorizationLevel {
    FULL("completa"), HIGH("alta"), MEDIUM("media"), LOW("baixa"), EMERGENCY_ONLY("so_emergencia");
    public final String value;
    AuthorizationLevel(String v) { this.value = v; }
}

enum HumanAvailability {
    AVAILABLE("disponivel"), MAYBE("talvez"), BUSY("ocupado"),
    UNREACHABLE("inalcancavel"), OFFLINE("offline"), UNKNOWN("desconhecido");
    public final String value;
    HumanAvailability(String v) { this.value = v; }
}

enum ContactMethod {
    PHONE_CALL("ligacao"), SMS("sms"), WHATSAPP("whatsapp"), VIDEO_CALL("video"),
    APP_PUSH("notificacao_app"), SMARTWATCH("smartwatch"), HOME_ASSISTANT("assinante_casa"), PHYSICAL_VISIT("visita_fisica");
    public final String value;
    ContactMethod(String v) { this.value = v; }
}

enum CallStatus {
    PENDING("pendente"), RINGING("tocando"), ANSWERED("atendeu"), CONFIRMED("confirmou"),
    DECLINED("recusou"), TIMEOUT("sem_resposta"), FAILED("falhou"), CANCELLED("cancelada");
    public final String value;
    CallStatus(String v) { this.value = v; }
}

class AuthorizedHuman {
    String human_id;
    String name;
    String phone;
    TrustRing ring;
    AuthorizationLevel authorization;
    String relationship = "";
    double[] home_location; // lat, lon
    double[] current_location;
    double last_location_update = 0.0;
    ContactMethod preferred_contact = ContactMethod.PHONE_CALL;
    List<String> languages = new ArrayList<>(Arrays.asList("pt-BR"));
    List<String> skills = new ArrayList<>();
    String[] available_hours = {"00:00", "23:59"};
    int response_timeout_s = 30;
    double max_distance_km = 50.0;
    boolean can_make_decisions = false;
    boolean medical_authorization = false;
    String photo_url = "";
    String notes = "";

    public AuthorizedHuman(String human_id, String name, String phone, TrustRing ring, AuthorizationLevel authorization,
                           String relationship, double[] home_location, ContactMethod preferred_contact,
                           List<String> skills, boolean can_make_decisions, boolean medical_authorization,
                           int response_timeout_s, double max_distance_km, String[] available_hours) {
        this.human_id = human_id;
        this.name = name;
        this.phone = phone;
        this.ring = ring;
        this.authorization = authorization;
        this.relationship = relationship;
        this.home_location = home_location;
        this.preferred_contact = preferred_contact != null ? preferred_contact : ContactMethod.PHONE_CALL;
        if (skills != null) this.skills = skills;
        this.can_make_decisions = can_make_decisions;
        this.medical_authorization = medical_authorization;
        this.response_timeout_s = response_timeout_s;
        this.max_distance_km = max_distance_km;
        if (available_hours != null) this.available_hours = available_hours;
    }

    public double distance_to(double lat, double lon) {
        double[] loc = current_location != null ? current_location : home_location;
        if (loc == null) return 9999.0;
        return _haversine_km(loc[0], loc[1], lat, lon);
    }

    public boolean is_available_now() {
        LocalTime now = LocalTime.now();
        int now_h = now.getHour() * 100 + now.getMinute();
        int start = Integer.parseInt(available_hours[0].replace(":", ""));
        int end = Integer.parseInt(available_hours[1].replace(":", ""));
        return start <= now_h && now_h <= end;
    }
}

class CallAttempt {
    String attempt_id;
    AuthorizedHuman human;
    ContactMethod method;
    CallStatus status = CallStatus.PENDING;
    double called_at = System.currentTimeMillis() / 1000.0;
    Double answered_at;
    Double timeout_at;
    String message_sent = "";
    String response_received = "";
    double distance_km = 0.0;
    double eta_minutes = 0.0;

    public CallAttempt(String attempt_id, AuthorizedHuman human, ContactMethod method, double distance_km, double eta_minutes, String message_sent) {
        this.attempt_id = attempt_id;
        this.human = human;
        this.method = method;
        this.distance_km = distance_km;
        this.eta_minutes = eta_minutes;
        this.message_sent = message_sent;
    }
}

class HumanNet {
    String user_name;
    String user_phone;
    Map<String, AuthorizedHuman> registry = new HashMap<>();
    Deque<CallAttempt> call_history = new ArrayDeque<>(500);
    Map<String, CallAttempt> active_calls = new HashMap<>();
    AuthorizedHuman confirmed_helper = null;
    TrustRing current_ring = null;
    double[] user_location = null;
    List<String> user_disabilities = new ArrayList<>();
    String situation_description = "";
    boolean auto_call_enabled = true;
    boolean consent_given = true;

    public HumanNet(String user_name, String user_phone) {
        this.user_name = user_name;
        this.user_phone = user_phone;
    }

    public String register_human(AuthorizedHuman human) {
        registry.put(human.human_id, human);
        return human.name + " registrado no anel " + human.ring.name() + " (" + human.authorization.value + ").";
    }

    public String remove_human(String human_id) {
        if (registry.containsKey(human_id)) {
            String name = registry.get(human_id).name;
            registry.remove(human_id);
            return name + " removido.";
        }
        return "Humano nao encontrado.";
    }

    public Map<TrustRing, List<AuthorizedHuman>> list_humans() {
        Map<TrustRing, List<AuthorizedHuman>> by_ring = new EnumMap<>(TrustRing.class);
        for (AuthorizedHuman h : registry.values()) {
            by_ring.computeIfAbsent(h.ring, k -> new ArrayList<>()).add(h);
        }
        return by_ring;
    }

    public void update_user_location(double lat, double lon) {
        user_location = new double[]{lat, lon};
    }

    public void update_human_location(String human_id, double lat, double lon) {
        if (registry.containsKey(human_id)) {
            AuthorizedHuman h = registry.get(human_id);
            h.current_location = new double[]{lat, lon};
            h.last_location_update = System.currentTimeMillis() / 1000.0;
        }
    }

    public List<Map.Entry<AuthorizedHuman, Double>> rank_humans(TrustRing max_ring, AuthorizationLevel required_auth) {
        if (user_location == null) return Collections.emptyList();
        List<Map.Entry<AuthorizedHuman, Double>> ranked = new ArrayList<>();
        List<AuthorizationLevel> auth_order = Arrays.asList(AuthorizationLevel.FULL, AuthorizationLevel.HIGH,
                AuthorizationLevel.MEDIUM, AuthorizationLevel.LOW, AuthorizationLevel.EMERGENCY_ONLY);

        for (AuthorizedHuman human : registry.values()) {
            if (human.ring.value > max_ring.value) continue;
            if (auth_order.indexOf(human.authorization) > auth_order.indexOf(required_auth)) continue;
            if (human.ring != TrustRing.EMERGENCY && !human.is_available_now()) continue;
            double dist = human.distance_to(user_location[0], user_location[1]);
            if (dist > human.max_distance_km && human.ring != TrustRing.EMERGENCY) continue;
            ranked.add(new AbstractMap.SimpleEntry<>(human, dist));
        }
        ranked.sort(Comparator.comparingInt(e -> e.getKey().ring.value).thenComparingDouble(Map.Entry::getValue));
        return ranked;
    }

    public Map<String, Object> trigger_emergency_call(String situation, double user_lat, double user_lon, String severity) {
        if (user_lat != 0 && user_lon != 0) update_user_location(user_lat, user_lon);
        situation_description = situation;
        confirmed_helper = null;
        active_calls.clear();

        if (user_location == null) {
            Map<String, Object> res = new LinkedHashMap<>();
            res.put("success", false);
            res.put("error", "Sem localizacao do usuario. Nao posso chamar ajuda.");
            res.put("fallback", "Ligar para 190 diretamente.");
            return res;
        }

        TrustRing max_ring = severity.equals("catastrophic") ? TrustRing.EMERGENCY :
                severity.equals("critical") ? TrustRing.PROFESSIONAL : TrustRing.COMMUNITY;
        AuthorizationLevel required_auth = (severity.equals("critical") || severity.equals("catastrophic")) ?
                AuthorizationLevel.MEDIUM : AuthorizationLevel.LOW;

        List<Map.Entry<AuthorizedHuman, Double>> ranked = rank_humans(max_ring, required_auth);
        if (ranked.isEmpty()) return _call_emergency_services(situation);

        List<Map<String, Object>> results = new ArrayList<>();
        for (Map.Entry<AuthorizedHuman, Double> entry : ranked) {
            AuthorizedHuman human = entry.getKey();
            double distance = entry.getValue();
            current_ring = human.ring;
            CallAttempt attempt = _call_human(human, situation, distance);
            results.add(_attempt_summary(attempt));
            if (attempt.status == CallStatus.CONFIRMED) {
                confirmed_helper = human;
                Map<String, Object> res = new LinkedHashMap<>();
                res.put("success", true);
                res.put("helper", human.name);
                res.put("phone", human.phone);
                res.put("ring", human.ring.name());
                res.put("distance_km", Math.round(distance * 100.0) / 100.0);
                res.put("eta_minutes", attempt.eta_minutes);
                res.put("method", attempt.method.value);
                res.put("message", human.name + " confirmou! Esta a " + String.format("%.1f", distance) + "km. Chega em ~" + Math.round(attempt.eta_minutes) + " minutos.");
                res.put("all_attempts", results);
                return res;
            }
        }
        Map<String, Object> emergency = _call_emergency_services(situation);
        Map<String, Object> res = new LinkedHashMap<>();
        res.put("success", false);
        res.put("error", "Nenhum dos " + results.size() + " humanos disponiveis confirmou.");
        res.put("all_attempts", results);
        res.put("escalated_to_emergency", true);
        res.put("emergency_result", emergency);
        return res;
    }

    private CallAttempt _call_human(AuthorizedHuman human, String situation, double distance) {
        CallAttempt attempt = new CallAttempt(
                "CALL-" + human.human_id + "-" + (int)(System.currentTimeMillis() / 1000),
                human, human.preferred_contact, distance, Math.max(1, distance * 3),
                _build_message(human, situation, distance)
        );
        attempt.status = CallStatus.RINGING;
        active_calls.put(attempt.attempt_id, attempt);

        Map<TrustRing, Double> response_chance = new EnumMap<>(TrustRing.class);
        response_chance.put(TrustRing.FAMILY, 0.85);
        response_chance.put(TrustRing.CAREGIVER, 0.70);
        response_chance.put(TrustRing.COMMUNITY, 0.50);
        response_chance.put(TrustRing.PROFESSIONAL, 0.60);
        response_chance.put(TrustRing.EMERGENCY, 0.90);
        response_chance.put(TrustRing.BYSTANDER, 0.30);
        double chance = response_chance.getOrDefault(human.ring, 0.4);

        if (Math.random() < chance) {
            attempt.status = CallStatus.CONFIRMED;
            attempt.answered_at = System.currentTimeMillis() / 1000.0;
            attempt.response_received = human.name + " confirmou que esta indo.";
        } else {
            attempt.status = CallStatus.TIMEOUT;
            attempt.timeout_at = System.currentTimeMillis() / 1000.0;
            attempt.response_received = "Sem resposta de " + human.name + " em " + human.response_timeout_s + "s.";
        }
        call_history.add(attempt);
        return attempt;
    }

    private String _build_message(AuthorizedHuman human, String situation, double distance) {
        String disabilities_text = user_disabilities.isEmpty() ? "" : " Condicao: " + String.join(", ", user_disabilities) + ".";
        return "Ola, " + human.name + "? Aqui e a Iara, sistema da Republica. " +
                user_name + " precisa de ajuda. Situacao: " + situation + ". " +
                "Localizacao aproximada: " + String.format("%.4f", user_location[0]) + ", " + String.format("%.4f", user_location[1]) + ". " +
                "Voce esta a " + String.format("%.1f", distance) + "km." + disabilities_text + " Pode ir ate la ou ligar para confirmar que esta bem?";
    }

    private Map<String, Object> _call_emergency_services(String situation) {
        String service, service_type;
        String lower = situation.toLowerCase();
        if (lower.contains("medica") || lower.contains("coracao") || lower.contains("machucad")) {
            service = "192 (SAMU)"; service_type = "medica";
        } else if (lower.contains("incendio") || lower.contains("fogo")) {
            service = "193 (Bombeiros)"; service_type = "bombeiros";
        } else {
            service = "190 (Policia)"; service_type = "policia";
        }
        String msg = "LIGACAO AUTOMATICA para " + service + ". Usuario: " + user_name + ". Localizacao: " + Arrays.toString(user_location) +
                ". Situacao: " + situation + ". Condicoes: " + (user_disabilities.isEmpty() ? "nenhuma" : String.join(", ", user_disabilities)) + ". Nenhum contato pessoal respondeu.";
        Map<String, Object> res = new LinkedHashMap<>();
        res.put("success", true);
        res.put("service", service);
        res.put("type", service_type);
        res.put("message", msg);
        res.put("note", "Emergencia publica acionada. Ajuda a caminho.");
        return res;
    }

    public Map<String, Object> cancel_emergency(String reason) {
        for (CallAttempt a : active_calls.values()) {
            if (a.status == CallStatus.RINGING || a.status == CallStatus.PENDING) a.status = CallStatus.CANCELLED;
        }
        confirmed_helper = null;
        Map<String, Object> res = new LinkedHashMap<>();
        res.put("cancelled", true);
        res.put("reason", reason);
        res.put("message", "Emergencia cancelada. " + reason + ". Todos os contatos foram avisados.");
        return res;
    }

    private Map<String, Object> _attempt_summary(CallAttempt attempt) {
        Map<String, Object> m = new LinkedHashMap<>();
        m.put("human", attempt.human.name);
        m.put("ring", attempt.human.ring.name());
        m.put("phone", attempt.human.phone);
        m.put("method", attempt.method.value);
        m.put("status", attempt.status.value);
        m.put("distance_km", Math.round(attempt.distance_km * 100.0) / 100.0);
        m.put("eta_minutes", Math.round(attempt.eta_minutes * 10.0) / 10.0);
        m.put("response", attempt.response_received);
        return m;
    }

    public Map<String, Object> status() {
        Map<TrustRing, List<AuthorizedHuman>> by_ring = list_humans();
        Map<String, Integer> humans_by_ring = new LinkedHashMap<>();
        for (Map.Entry<TrustRing, List<AuthorizedHuman>> e : by_ring.entrySet()) humans_by_ring.put(e.getKey().name(), e.getValue().size());
        Map<String, Object> res = new LinkedHashMap<>();
        res.put("user_name", user_name);
        res.put("total_humans", registry.size());
        res.put("humans_by_ring", humans_by_ring);
        res.put("confirmed_helper", confirmed_helper != null ? confirmed_helper.name : null);
        res.put("current_ring", current_ring != null ? current_ring.name() : null);
        res.put("active_calls", active_calls.size());
        res.put("total_calls_made", call_history.size());
        res.put("auto_call_enabled", auto_call_enabled);
        res.put("user_location", user_location != null ? Arrays.toString(user_location) : null);
        return res;
    }
}

class ResilienceHumanBridge {
    static final Map<String, String> DEGRADATION_TRIGGERS = Map.of(
            "sobrevivencia", "critical", "emergencia", "catastrophic", "morto", "catastrophic"
    );
    HumanNet net;
    boolean triggered = false;
    String last_trigger_level = "";

    public ResilienceHumanBridge(HumanNet net) { this.net = net; }

    public Map<String, Object> check_and_trigger(String degradation_level, double user_lat, double user_lon, String situation) {
        String severity = DEGRADATION_TRIGGERS.get(degradation_level);
        if (severity == null) {
            if (triggered) {
                Map<String, Object> r = net.cancel_emergency("Sistema recuperado.");
                triggered = false;
                last_trigger_level = "";
                return r;
            }
            return null;
        }
        if (triggered && last_trigger_level.equals(degradation_level)) return null;
        triggered = true;
        last_trigger_level = degradation_level;
        if (situation == null || situation.isEmpty()) situation = "Sistema em nivel " + degradation_level + ". Possivel falha multipla.";
        return net.trigger_emergency_call(situation, user_lat, user_lon, severity);
    }
}

public class open_human_net {
    static double _haversine_km(double lat1, double lon1, double lat2, double lon2) {
        double R = 6371;
        double dlat = Math.toRadians(lat2 - lat1);
        double dlon = Math.toRadians(lon2 - lon1);
        double a = Math.sin(dlat / 2) * Math.sin(dlat / 2) + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2)) * Math.sin(dlon / 2) * Math.sin(dlon / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return R * c;
    }

    static HumanNet create_default_network(String user_name) {
        HumanNet net = new HumanNet(user_name, "+5511****9999");
        net.user_disabilities = new ArrayList<>();
        // Anel 0: Familia
        net.register_human(new AuthorizedHuman("ming", "MING", "+5511****8888", TrustRing.FAMILY, AuthorizationLevel.FULL,
                "esposa", new double[]{-23.5505, -46.6333}, ContactMethod.PHONE_CALL,
                Arrays.asList("primeiros_socorros"), true, true, 20, 30.0, new String[]{"00:00", "23:59"}));
        net.register_human(new AuthorizedHuman("mae", "Mae", "+5511****7777", TrustRing.FAMILY, AuthorizationLevel.FULL,
                "mae", new double[]{-23.5600, -46.6400}, ContactMethod.PHONE_CALL,
                Collections.emptyList(), true, true, 30, 50.0, new String[]{"00:00", "23:59"}));
        // Anel 1
        net.register_human(new AuthorizedHuman("andre", "Andre Castro", "+5511****6666", TrustRing.CAREGIVER, AuthorizationLevel.HIGH,
                "parceiro", new double[]{-23.5450, -46.6300}, ContactMethod.WHATSAPP,
                Arrays.asList("gestao", "primeiros_socorros"), false, false, 45, 20.0, new String[]{"00:00", "23:59"}));
        // Anel 2
        net.register_human(new AuthorizedHuman("aveone", "AveOne", "+5511****5555", TrustRing.COMMUNITY, AuthorizationLevel.MEDIUM,
                "equipe infra", new double[]{-23.5700, -46.6500}, ContactMethod.SMS,
                Arrays.asList("tecnologia", "infraestrutura"), false, false, 60, 15.0, new String[]{"00:00", "23:59"}));
        // Anel 3
        net.register_human(new AuthorizedHuman("dr_silva", "Dr. Silva", "+5511****4444", TrustRing.PROFESSIONAL, AuthorizationLevel.HIGH,
                "medico de familia", new double[]{-23.5400, -46.6200}, ContactMethod.PHONE_CALL,
                Arrays.asList("medico", "primeiros_socorros", "cardiologia"), false, true, 60, 10.0, new String[]{"07:00", "19:00"}));
        return net;
    }

    // CENARIOS (6 funcoes completas)
    static void scenario_blind_lost_battery() {
        System.out.println("=".repeat(65));
        System.out.println("CENARIO 1: Cego perdido -- bateria em 1%");
        System.out.println("=".repeat(65));
        HumanNet net = create_default_network("Cleiton");
        net.user_disabilities = new ArrayList<>(Arrays.asList("cegueira_total"));
        net.update_user_location(-23.5510, -46.6340);
        Map<String, Object> result = net.trigger_emergency_call("Cego na rua, bateria do smartphone em 1%. Pode perder contato.", -23.5510, -46.6340, "critical");
        System.out.println("\nResultado: " + (Boolean.TRUE.equals(result.get("success")) ? "SUCESSO" : "FALHOU"));
        if (Boolean.TRUE.equals(result.get("success"))) {
            System.out.println("Ajudante: " + result.get("helper") + " (anel " + result.get("ring") + ")");
            System.out.println("Distancia: " + result.get("distance_km") + "km | ETA: " + String.format("%.0f", result.get("eta_minutes")) + "min");
            System.out.println("Metodo: " + result.get("method"));
        } else {
            System.out.println("Erro: " + result.getOrDefault("error", "desconhecido"));
            if (Boolean.TRUE.equals(result.get("escalated_to_emergency"))) System.out.println("Escalacao: " + ((Map)result.get("emergency_result")).get("service"));
        }
        System.out.println("\nTentativas:");
        for (Map<String, Object> a : (List<Map<String, Object>>) result.getOrDefault("all_attempts", Collections.emptyList())) {
            String icon = "confirmou".equals(a.get("status")) ? "OK" : "X ";
            System.out.printf("  [%s] %-15s anel=%-12s dist=%.2fkm status=%s%n", icon, a.get("human"), a.get("ring"), a.get("distance_km"), a.get("status"));
        }
    }

    static void scenario_elderly_fall() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 2: Idosa caiu -- sem resposta em 30s");
        System.out.println("=".repeat(65));
        HumanNet net = new HumanNet("Dona Cecca", "+5511****3333");
        net.user_disabilities = new ArrayList<>(Arrays.asList("idoso", "osteoporose"));
        net.update_user_location(-23.5520, -46.6350);
        net.register_human(new AuthorizedHuman("filha", "Maria Filha", "+5511****1111", TrustRing.FAMILY, AuthorizationLevel.FULL,
                "filha", new double[]{-23.5480, -46.6310}, ContactMethod.PHONE_CALL, Arrays.asList("primeiros_socorros"), true, true, 20, 50.0, null));
        net.register_human(new AuthorizedHuman("vizinha", "Dona Ana", "+5511****2222", TrustRing.CAREGIVER, AuthorizationLevel.HIGH,
                "vizinha", new double[]{-23.5515, -46.6345}, ContactMethod.PHONE_CALL, Arrays.asList("primeiros_socorros"), false, false, 30, 2.0, null));
        Map<String, Object> result = net.trigger_emergency_call("Idosa caiu. Deteccao de queda pelo smartwatch. Sem resposta ha 30s.", -23.5520, -46.6350, "catastrophic");
        System.out.println("\nResultado: " + (Boolean.TRUE.equals(result.get("success")) ? "SUCESSO" : "FALHOU"));
        if (Boolean.TRUE.equals(result.get("success"))) {
            System.out.println("Quem vai: " + result.get("helper") + " (" + result.get("ring") + ")");
            System.out.println("Distancia: " + result.get("distance_km") + "km | ETA: " + String.format("%.0f", result.get("eta_minutes")) + "min");
        } else System.out.println("Escalacao: " + result.getOrDefault("escalated_to_emergency", false));
        System.out.println("\nTentativas:");
        for (Map<String, Object> a : (List<Map<String, Object>>) result.getOrDefault("all_attempts", Collections.emptyList())) {
            String icon = "confirmou".equals(a.get("status")) ? "OK" : "X ";
            System.out.printf("  [%s] %-15s anel=%-12s dist=%.2fkm%n", icon, a.get("human"), a.get("ring"), a.get("distance_km"));
        }
    }

    static void scenario_seizure() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 3: Crise epileptica iminente");
        System.out.println("=".repeat(65));
        HumanNet net = create_default_network("Pedro");
        net.user_disabilities = new ArrayList<>(Arrays.asList("epilepsia"));
        net.update_user_location(-23.5530, -46.6360);
        Map<String, Object> result = net.trigger_emergency_call("Sinais pre-crise epileptica. Smartwatch detectou anomalia cardiaca + temperatura elevada.", 0, 0, "critical");
        System.out.println("\nResultado: " + (Boolean.TRUE.equals(result.get("success")) ? "SUCESSO" : "FALHOU"));
        if (Boolean.TRUE.equals(result.get("success"))) {
            System.out.println("Ajudante: " + result.get("helper") + " (anel " + result.get("ring") + ")");
            System.out.println("Distancia: " + result.get("distance_km") + "km | ETA: " + String.format("%.0f", result.get("eta_minutes")) + "min");
        }
        System.out.println("\nTentativas:");
        for (Map<String, Object> a : (List<Map<String, Object>>) result.getOrDefault("all_attempts", Collections.emptyList())) {
            String icon = "confirmou".equals(a.get("status")) ? "OK" : "X ";
            System.out.printf("  [%s] %-15s dist=%.2fkm status=%s%n", icon, a.get("human"), a.get("distance_km"), a.get("status"));
        }
    }

    static void scenario_resilience_integration() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 4: Integracao Resilience -> HumanNet");
        System.out.println("=".repeat(65));
        HumanNet net = create_default_network("Cleiton");
        net.update_user_location(-23.5510, -46.6340);
        ResilienceHumanBridge bridge = new ResilienceHumanBridge(net);
        System.out.println("\n[Nivel: completo]");
        Map<String, Object> r = bridge.check_and_trigger("completo", -23.5510, -46.6340, "");
        System.out.println("  Resultado: " + (r == null ? "Sem acao" : r));
        System.out.println("\n[Nivel: degradado_1]");
        r = bridge.check_and_trigger("degradado_1", -23.5510, -46.6340, "");
        System.out.println("  Resultado: " + (r == null ? "Sem acao -- sistema funcional" : r));
        System.out.println("\n[Nivel: sobrevivencia] -> DISPARA HUMANOS");
        r = bridge.check_and_trigger("sobrevivencia", -23.5510, -46.6340, "Bateria critica + GPS perdido. Usuario vulneravel.");
        if (r != null) {
            if (Boolean.TRUE.equals(r.get("success"))) {
                System.out.println("  AJUDANTE: " + r.get("helper") + " a " + r.get("distance_km") + "km");
                System.out.println("  ETA: " + String.format("%.0f", r.getOrDefault("eta_minutes", 0)) + " min");
            } else System.out.println("  Escalado para emergencia publica");
        } else System.out.println("  Nao disparou");
        System.out.println("\n[Nivel: completo novamente] -> CANCELA");
        r = bridge.check_and_trigger("completo", 0, 0, "");
        if (r != null) System.out.println("  " + r.getOrDefault("message", "Cancelado"));
    }

    static void scenario_ring_escalation() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 5: Escalacao de aneis (ninguem atende)");
        System.out.println("=".repeat(65));
        HumanNet net = new HumanNet("Teste", "+5511****0000");
        net.update_user_location(-23.5500, -46.6300);
        Random rand = new Random(42);
        net.register_human(new AuthorizedHuman("h1", "Familiar 1", "+55111", TrustRing.FAMILY, AuthorizationLevel.FULL,
                "irmao", new double[]{-23.5490, -46.6290}, ContactMethod.PHONE_CALL, Collections.emptyList(), false, false, 10, 50.0, null));
        net.register_human(new AuthorizedHuman("h2", "Cuidador 1", "+5512", TrustRing.CAREGIVER, AuthorizationLevel.HIGH,
                "cuidador", new double[]{-23.5480, -46.6280}, ContactMethod.PHONE_CALL, Collections.emptyList(), false, false, 10, 50.0, null));
        net.register_human(new AuthorizedHuman("h3", "Comunidade 1", "+5513", TrustRing.COMMUNITY, AuthorizationLevel.MEDIUM,
                "vizinho Republica", new double[]{-23.5470, -46.6270}, ContactMethod.PHONE_CALL, Collections.emptyList(), false, false, 10, 50.0, null));
        Map<String, Object> result = net.trigger_emergency_call("Usuario incapacitado. Necessita assistencia fisica imediata.", 0, 0, "catastrophic");
        if (Boolean.TRUE.equals(result.get("success"))) System.out.println("\nAlguem atendeu: " + result.get("helper"));
        else {
            System.out.println("\nNinguem atendeu nos aneis pessoais.");
            if (Boolean.TRUE.equals(result.get("escalated_to_emergency"))) {
                Map er = (Map) result.get("emergency_result");
                System.out.println("Escalacao para emergencia publica: " + er.get("service"));
            }
        }
        System.out.println("\nTentativas (" + ((List)result.getOrDefault("all_attempts", Collections.emptyList())).size() + "):");
        for (Map<String, Object> a : (List<Map<String, Object>>) result.getOrDefault("all_attempts", Collections.emptyList())) {
            String icon = "confirmou".equals(a.get("status")) ? "OK" : "X ";
            System.out.printf("  [%s] anel=%-12s %-15s dist=%.2fkm%n", icon, a.get("ring"), a.get("human"), a.get("distance_km"));
        }
    }

    static void scenario_child_lost() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 6: Crianca perdida no shopping");
        System.out.println("=".repeat(65));
        HumanNet net = new HumanNet("Sophia (8 anos)", "+5511****0000");
        net.update_user_location(-23.5610, -46.6560);
        net.register_human(new AuthorizedHuman("pai", "Cleiton (Pai)", "+5511****9999", TrustRing.FAMILY, AuthorizationLevel.FULL,
                "pai", new double[]{-23.5505, -46.6333}, ContactMethod.PHONE_CALL, Collections.emptyList(), false, false, 15, 20.0, null));
        net.register_human(new AuthorizedHuman("mae", "MING (Mae)", "+5511****8888", TrustRing.FAMILY, AuthorizationLevel.FULL,
                "mae", new double[]{-23.5505, -46.6333}, ContactMethod.PHONE_CALL, Collections.emptyList(), false, false, 15, 20.0, null));
        Map<String, Object> result = net.trigger_emergency_call("Crianca de 8 anos separada dos pais no shopping. Sistema da Republica detectou saida de zona segura.", 0, 0, "critical");
        if (Boolean.TRUE.equals(result.get("success"))) {
            System.out.println("\n" + result.get("helper") + " confirmou! Esta a caminho.");
            System.out.println("Distancia: " + result.get("distance_km") + "km | ETA: " + String.format("%.0f", result.get("eta_minutes")) + "min");
        } else System.out.println("\nEscalado para emergencia.");
    }

    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("OpenHumanNet -- Chamar o Humano Autorizado Mais Proximo");
        System.out.println("=".repeat(70));
        HumanNet net = create_default_network("Cleiton");
        net.update_user_location(-23.5505, -46.6333);
        System.out.println("\nUsuario: " + net.user_name);
        System.out.println("Localizacao: " + Arrays.toString(net.user_location));
        System.out.println("Humanos registrados: " + net.registry.size());
        Map<TrustRing, List<AuthorizedHuman>> humans_by_ring = net.list_humans();
        System.out.println("\nRede por aneis:");
        for (TrustRing ring : TrustRing.values()) {
            List<AuthorizedHuman> humans = humans_by_ring.getOrDefault(ring, Collections.emptyList());
            System.out.println("  Anel " + ring.value + " (" + ring.name() + "): " + humans.size() + " humano(s)");
            for (AuthorizedHuman h : humans) {
                double dist = h.distance_to(-23.5505, -46.6333);
                System.out.printf("    - %-15s (%-15s) auth=%-15s dist=%.1fkm%n", h.name, h.relationship, h.authorization.value, dist);
            }
        }
        scenario_blind_lost_battery();
        scenario_elderly_fall();
        scenario_seizure();
        scenario_resilience_integration();
        scenario_ring_escalation();
        scenario_child_lost();
        System.out.println("\n" + "=".repeat(70));
        System.out.println("COBERTURA DO SISTEMA");
        System.out.println("=".repeat(70));
        System.out.println("\n  Aneis de confianca: " + TrustRing.values().length);
        for (TrustRing r : TrustRing.values()) System.out.println("    Anel " + r.value + ": " + r.name());
        System.out.println("\n  Niveis de autorizacao: " + AuthorizationLevel.values().length);
        for (AuthorizationLevel a : AuthorizationLevel.values()) System.out.println("    " + a.value);
        System.out.println("\n  Metodos de contato: " + ContactMethod.values().length);
        for (ContactMethod c : ContactMethod.values()) System.out.println("    " + c.value);
        System.out.println("\n  Estados de chamada: " + CallStatus.values().length);
        System.out.println("\n  FLUXO DE PRIORIDADE:");
        System.out.println("    1. Sistema detecta falha (OpenResilience: SURVIVAL/EMERGENCY)");
        System.out.println("    2. Pegar localizacao do usuario (GPS/ultima/triangulacao)");
        System.out.println("    3. Ranquear humanos: anel -> distancia -> disponibilidade");
        System.out.println("    4. Chamar Anel 0 (Familia) primeiro");
        System.out.println("    5. Se familia nao atende -> Anel 1 (Cuidador)");
        System.out.println("    6. Se cuidador nao atende -> Anel 2 (Comunidade)");
        System.out.println("    7. Se comunidade nao atende -> Anel 3 (Profissional)");
        System.out.println("    8. Se profissional nao atende -> Anel 4 (190/192/193)");
        System.out.println("    9. PARAR quando humano CONFIRMA que vai ajudar");
        System.out.println("   10. Se ninguem -> Anel 5 (estranho proximo via appel)");
        System.out.println("\n" + "=".repeat(70));
        System.out.println("A tecnologia NAO substitui o humano.");
        System.out.println("A tecnologia CONECTA o humano CERTO no momento CERTO.");
        System.out.println("\nTODO hardware falha. TODO software cai.");
        System.out.println("O HUMANO e o sistema final. Ele nunca falha.");
    }
}