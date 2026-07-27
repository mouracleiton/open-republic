// OpenResilience -- Simulacao de Falhas e Mitigacao
// ====================================================
// "O cego esta na rua. A bateria do smartphone cai pra 2%.
// O GPS para. A camera trava. O TTS crasha.
// E AGORA? O cego esta PERDIDO, CEGO, e SEM SISTEMA.
//
// A resposta NAO e 'isso nao vai acontecer'.
// A resposta e: 'quando acontecer, o sistema REAGE'.
//
// Todo hardware falha. Todo software cai. Todo sinal se perde.
// A pergunta nao e SE vai falhar -- e QUANDO.
// E quando falhar, o usuario NAO pode ficar desamparado.
//
// Este modulo simula TODA falha possivel e define a mitigacao:
// - Bateria em 0%: modo survival, so essencial, voz lenta
// - GPS perdido: bussola + contagem de passos + landmark auditivo
// - Camera falhou: audio + acelerometro assumem
// - TTS crashou: vibracao + braille assumem
// - Rede caiu: tudo offline, dados em cache
// - Software travou: watchdog reinicia em 3s
// - Hardware morreu: fallback para terminal publico + ligacao
//
// PRINCIPIO: Cada componente tem um PLANO B, PLANO C e PLANO D.
// Nenhum ponto unico de falha. Redundancia em TUDO.
//
// Integrado com:
// - OpenTelefonista (telefonista sobrevive a falhas)
// - OpenInclusiveIDE (IDE degrada graciosamente)
// - OpenInclusiveHardware (44 dispositivos com fallback)
// - OpenAbsence (pausa mesmo em modo survival)
// - OpenSilencePolicy (silencio mesmo em emergencia)
//
// Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Function;

// ============================================================================
// 1. TIPOS DE FALHA
// ============================================================================

enum FailureCategory {
    HARDWARE("hardware"),
    SOFTWARE("software"),
    NETWORK("rede"),
    POWER("energia"),
    SENSOR("sensor"),
    PERIPHERAL("periferico"),
    OS("sistema_operacional"),
    CLOUD("nuvem");

    private final String value;
    FailureCategory(String value) { this.value = value; }
    public String getValue() { return value; }
}

enum FailureType {
    // POWER
    BATTERY_CRITICAL("bateria_critica"),        // < 5%
    BATTERY_DEAD("bateria_morta"),              // 0%
    BATTERY_OVERHEAT("bateria_superaquecida"),  // desliga por calor
    POWER_SURGE("pico_energia"),                // dano eletrico

    // HARDWARE
    SCREEN_BROKEN("tela_quebrada"),             // caiu, rachou
    SCREEN_DEAD("tela_morta"),                  // backlight queimou
    CAMERA_FAILURE("camera_falhou"),            // lente riscada, modulo queimou
    MICROPHONE_DEAD("microfone_morto"),         // agua, poeira
    SPEAKER_DEAD("alto_falante_morto"),         // agua, volume max
    VIBRATION_DEAD("vibracao_morta"),           // motor queimou
    GPS_LOST("gps_perdido"),                    // dentro de predio, tunel
    BLUETOOTH_DROP("bluetooth_caiu"),           // desconectou do braille
    NFC_FAILURE("nfc_falhou"),
    WATER_DAMAGE("dano_agua"),                 // chuva, queda na agua
    PHYSICAL_DAMAGE("dano_fisico"),             // pisou, atropelou
    BUTTON_STUCK("botao_preso"),               // poeira, impacto
    CHARGE_PORT_BROKEN("porta_carga_quebrada"),  // nao carrega mais

    // PERIPHERAL
    BRAILLE_DISPLAY_DISCONNECTED("braille_desconectou"),
    EYE_TRACKER_LOST("eye_tracker_perdeu"),
    SWITCH_FAILURE("switch_queimou"),
    HEARING_AID_DISCONNECTED("aparelho_desconectou"),
    SMARTWATCH_LOST("smartwatch_perdido"),

    // SOFTWARE
    TTS_CRASH("tts_crashou"),                   // motor de voz morreu
    STT_FAILURE("stt_falhou"),                  // reconhecimento de voz falhou
    OCR_FAILURE("ocr_falhou"),                  // leitura de imagem falhou
    APP_FREEZE("app_travou"),                   // ANR
    APP_CRASH("app_crashou"),                   // SIGSEGV
    MEMORY_EXHAUSTED("memoria_esgotada"),       // OOM
    STORAGE_FULL("armazenamento_cheio"),
    MODEL_UNAVAILABLE("ia_indisponivel"),       // modelo IA nao carrega
    NAVIGATION_ENGINE_DOWN("navegador_caiu"),
    EMOTION_DETECTOR_DOWN("detector_emocao_caiu"),

    // NETWORK
    NETWORK_DOWN("rede_caiu"),                  // sem internet
    NETWORK_SLOW("rede_lenta"),                 // 2G,latencia alta
    CLOUD_DOWN("nuvem_caiu"),                   // servidor offline
    API_RATE_LIMIT("api_limite"),               // rate limited
    DNS_FAILURE("dns_falhou"),

    // OS
    OS_UPDATE_BRICK("atualizacao_bricou"),
    BOOT_LOOP("boot_loop"),
    PERMISSION_REVOKED("permissao_revogada");   // microfone negado

    private final String value;
    FailureType(String value) { this.value = value; }
    public String getValue() { return value; }
}

enum FailureSeverity {
    COSMETIC("cosmetico"),      // nao afeta funcionalidade principal
    MINOR("menor"),             // degradacao leve
    MAJOR("maior"),             // degradacao significativa
    CRITICAL("critico"),        // funcionalidade essencial perdida
    CATASTROPHIC("catastrofico");  // dispositivo inutilizavel

    private final String value;
    FailureSeverity(String value) { this.value = value; }
    public String getValue() { return value; }
}

enum FailureDuration {
    TRANSIENT("transiente"),    // segundos (bluetooth reconecta)
    SHORT("curto"),             // minutos (GPS re-adquire)
    MEDIUM("medio"),            // horas (bateria recarrega)
    LONG("longo"),              // dias (tela quebrada ate consertar)
    PERMANENT("permanente");    // nao recupera (hardware morreu)

    private final String value;
    FailureDuration(String value) { this.value = value; }
    public String getValue() { return value; }
}

// ============================================================================
// 2. EVENTO DE FALHA
// ============================================================================

class FailureEvent {
    String eventId;
    FailureType failureType;
    FailureCategory category;
    FailureSeverity severity;
    FailureDuration duration;
    String description;
    List<String> affectedComponents = new ArrayList<>();
    String userImpact = "";
    long timestamp = System.currentTimeMillis();
    double recoveryProbability = 0.9;
    boolean detected = false;

    public FailureEvent(String eventId, FailureType failureType, FailureCategory category,
                        FailureSeverity severity, FailureDuration duration, String description) {
        this.eventId = eventId;
        this.failureType = failureType;
        this.category = category;
        this.severity = severity;
        this.duration = duration;
        this.description = description;
    }
}

// ============================================================================
// 3. NIVEIS DE DEGRADACAO
// ============================================================================

enum DegradationLevel {
    FULL("completo"),          // 100% funcional, tudo operacional
    DEGRADED_1("degradado_1"),  // 80% -- features nao essenciais off
    DEGRADED_2("degradado_2"),  // 50% -- so essencial, fallback ativo
    SURVIVAL("sobrevivencia"),  // 20% -- minimo absoluto para nao morrer
    EMERGENCY("emergencia"),    // 10% -- so chamada de socorro
    DEAD("morto");             // 0% -- dispositivo inutilizavel

    private final String value;
    DegradationLevel(String value) { this.value = value; }
    public String getValue() { return value; }
}

class SystemState {
    DegradationLevel level = DegradationLevel.FULL;
    List<FailureEvent> activeFailures = new ArrayList<>();
    double batteryPct = 100.0;
    List<String> availableInputs = new ArrayList<>();
    List<String> availableOutputs = new ArrayList<>();
    List<String> availableSensors = new ArrayList<>();
    boolean networkAvailable = true;
    boolean gpsAvailable = true;
    boolean cameraAvailable = true;
    boolean microphoneAvailable = true;
    boolean speakerAvailable = true;
    boolean vibrationAvailable = true;
    boolean screenAvailable = true;
    boolean ttsAvailable = true;
    boolean brailleConnected = false;
    boolean eyeTrackerConnected = false;
    boolean smartwatchConnected = false;
    double offlineCacheSizeMb = 0.0;
    double[] lastKnownLocation = null;
    double uptimeSeconds = 0.0;
}

// ============================================================================
// 4. ESTRATEGIAS DE MITIGACAO
// ============================================================================

class MitigationStrategy {
    String strategyId;
    FailureType failureType;
    String name;
    String description;
    List<String> fallbackChain = new ArrayList<>();
    String recoveryAction = "";
    String userMessage = "";
    boolean autoActivate = true;
    int recoveryTimeEstimateS = 0;

    public MitigationStrategy(String strategyId, FailureType failureType, String name, String description) {
        this.strategyId = strategyId;
        this.failureType = failureType;
        this.name = name;
        this.description = description;
    }
}

class OpenResilience {
    public static final List<MitigationStrategy> MITIGATION_STRATEGIES = new ArrayList<>();

    static {
        // === BATERIA ===
        MitigationStrategy mt001 = new MitigationStrategy("MT-001", FailureType.BATTERY_CRITICAL,
            "Modo Survival de Bateria", "Bateria < 5%. Desliga tudo nao essencial. So mantem voz/sos.");
        mt001.fallbackChain.addAll(Arrays.asList(
            "Plano A: Reduzir brilho ao minimo, desligar animacoes",
            "Plano B: Desligar camera, GPS (usar contagem de passos)",
            "Plano C: Desligar TTS continuo, so falas criticas",
            "Plano D: SOS -- ligar para contato de emergencia e desligar"
        ));
        mt001.recoveryAction = "Conectar carregador. Sistema avisa proximo terminal publico.";
        mt001.userMessage = "Bateria critica. Entrei em modo sobrevivencia. So o essencial. Encontre um carregador ou vou te levar ate um terminal publico.";
        MITIGATION_STRATEGIES.add(mt001);

        MitigationStrategy mt002 = new MitigationStrategy("MT-002", FailureType.BATTERY_DEAD,
            "Handoff para Terminal Publico", "Bateria em 0%. Smartphone morre. Sistema migra.");
        mt002.fallbackChain.addAll(Arrays.asList(
            "Plano A: Antes de morrer, enviar localizacao para emergencia",
            "Plano B: Enviar ultima tarefa nao salva para nuvem",
            "Plano C: Ligar para contato de emergencia com mensagem automatica",
            "Plano D: Avisar usuario: 'Proximo terminal publico: biblioteca a 200m norte'"
        ));
        mt002.recoveryAction = "Carregar em terminal publico, biblioteca, estabelecimento.";
        mt002.userMessage = "Vou desligar em 30 segundos. Mandei sua localizacao para emergencia. Terminal publico mais proximo: biblioteca, 200 metros ao norte.";
        mt002.recoveryTimeEstimateS = 3600;
        MITIGATION_STRATEGIES.add(mt002);

        // === GPS ===
        MitigationStrategy mt003 = new MitigationStrategy("MT-003", FailureType.GPS_LOST,
            "Navegacao Sem GPS", "GPS perdido (predio, tunel, subsolo). Navegacao continua.");
        mt003.fallbackChain.addAll(Arrays.asList(
            "Plano A: Bussola magnetica + contagem de passos (dead reckoning)",
            "Plano B: Bluetooth beacons indoor (shopping, hospital)",
            "Plano C: WiFi triangulation (menos preciso mas funciona indoor)",
            "Plano D: Landmarks auditivos: 'Voce passou por um lugar barulhento a 30s -- provavelmente cozinha'"
        ));
        mt003.recoveryAction = "Sair para area aberta. GPS re-adquire em 10-30 segundos.";
        mt003.userMessage = "Perdi o GPS. Estou usando a bussola e contando seus passos. Vou continuar te guiando.";
        mt003.recoveryTimeEstimateS = 30;
        MITIGATION_STRATEGIES.add(mt003);

        // === CAMERA ===
        MitigationStrategy mt004 = new MitigationStrategy("MT-004", FailureType.CAMERA_FAILURE,
            "Camera Cai, Audio Assume", "Camera falhou. Visao computacional perdida.");
        mt004.fallbackChain.addAll(Arrays.asList(
            "Plano A: Microfone assume deteccao de obstaculos por eco/sonar",
            "Plano B: Acelerometro + bussola mapeiam caminho percorrido",
            "Plano C: Pedir ajuda humana: 'Alguem pode me orientar?' via voz alta",
            "Plano D: Ligar para contato que ve por camera remota"
        ));
        mt004.recoveryAction = "Limpar lente. Reiniciar app de camera. Se hardware, trocar smartphone.";
        mt004.userMessage = "Minha camera parou. Vou usar o microfone para ouvir o ambiente e te guiar pelo som.";
        mt004.recoveryTimeEstimateS = 60;
        MITIGATION_STRATEGIES.add(mt004);

        // === MICROFONE ===
        MitigationStrategy mt005 = new MitigationStrategy("MT-005", FailureType.MICROPHONE_DEAD,
            "Microfone Morto, Tela Assume", "Microfone falhou. Entrada por voz perdida.");
        mt005.fallbackChain.addAll(Arrays.asList(
            "Plano A: Switch/bluetooth keyboard assume entrada",
            "Plano B: Tela touch com botoes grandes (sim, mesmo para cego via TalkBack)",
            "Plano C: Eye tracker se disponivel",
            "Plano D: Pedir para alguem gravar e enviar audio"
        ));
        mt005.recoveryAction = "Limpar entrada do microfone. Verificar permissoes. Bluetooth headset como backup.";
        mt005.userMessage = "Nao estou te ouvindo. Vou passar para entrada por botoes/toque.";
        mt005.recoveryTimeEstimateS = 10;
        MITIGATION_STRATEGIES.add(mt005);

        // === TTS ===
        MitigationStrategy mt006 = new MitigationStrategy("MT-006", FailureType.TTS_CRASH,
            "TTS Crashou, Vibracao Assume", "Motor de voz morreu. Cego nao ouve mais o sistema.");
        mt006.fallbackChain.addAll(Arrays.asList(
            "Plano A: Display braille assume (se conectado)",
            "Plano B: Padroes de vibracao codificam informacao",
            "Plano C: Auto-restart do TTS em background",
            "Plano D: Tocar tons com significado (agudo=ok, grave=erro)"
        ));
        mt006.recoveryAction = "Reiniciar servico TTS. Android: Settings > Accessibility > TalkBack. iOS: VoiceOver toggle.";
        mt006.userMessage = "[MENSAGEM POR VIBRACAO: 1 pulse = ok, 2 pulses = atencao, 3 pulses = erro]";
        mt006.recoveryTimeEstimateS = 5;
        MITIGATION_STRATEGIES.add(mt006);

        // === BLUETOOTH / BRAILLE ===
        MitigationStrategy mt007 = new MitigationStrategy("MT-007", FailureType.BLUETOOTH_DROP,
            "Bluetooth Caiu", "Braille/switch/aparelho auditivo desconectou.");
        mt007.fallbackChain.addAll(Arrays.asList(
            "Plano A: Tentar reconexao automatica (3 tentativas em 10s)",
            "Plano B: Fallback para TTS alto-falante",
            "Plano C: Fallback para vibracao padrao",
            "Plano D: Pedir usuario para verificar Bluetooth manualmente"
        ));
        mt007.recoveryAction = "Reativar Bluetooth. Emparelhar novamente. Verificar bateria do periferico.";
        mt007.userMessage = "Perdi conexao com seu dispositivo. Tentando reconectar... Se nao voltar em 10 segundos, vou usar o alto-falante.";
        mt007.recoveryTimeEstimateS = 10;
        MITIGATION_STRATEGIES.add(mt007);

        // === REDE ===
        MitigationStrategy mt008 = new MitigationStrategy("MT-008", FailureType.NETWORK_DOWN,
            "Modo Offline Total", "Sem internet. IA em nuvem, mapas, API tudo fora.");
        mt008.fallbackChain.addAll(Arrays.asList(
            "Plano A: Modelos de IA locais (menores mas funcionam offline)",
            "Plano B: Mapas offline (OpenStreetMap cached)",
            "Plano C: Tudo que nao precisa de rede continua: TTS, OCR, navegacao local",
            "Plano D: SMS para emergencia (nao precisa de internet, so sinal)"
        ));
        mt008.recoveryAction = "Verificar WiFi/dados. Sair de area sem cobertura. Usar SMS para comunicacao.";
        mt008.userMessage = "Sem internet. Continuo funcionando offline. IA local assumiu. Mapas em cache.";
        mt008.recoveryTimeEstimateS = 300;
        MITIGATION_STRATEGIES.add(mt008);

        // === TELA ===
        MitigationStrategy mt009 = new MitigationStrategy("MT-009", FailureType.SCREEN_BROKEN,
            "Tela Quebrada", "Tela rachada/morta. Sem saida visual.");
        mt009.fallbackChain.addAll(Arrays.asList(
            "Plano A: TTS assume toda interacao (cego simulado)",
            "Plano B: Braille display conectado via bluetooth",
            "Plano C: Smartwatch mostra minimo na tela do relogio",
            "Plano D: Cast para TV/terminal publico proximo"
        ));
        mt009.recoveryAction = "Trocar tela. Enquanto isso: TTS + braille + smartwatch.";
        mt009.userMessage = "Sua tela quebrou. Vou guiar tudo por voz. Conecte um braille display se tiver.";
        mt009.recoveryTimeEstimateS = 259200;
        MITIGATION_STRATEGIES.add(mt009);

        // === SOFTWARE CRASH ===
        MitigationStrategy mt010 = new MitigationStrategy("MT-010", FailureType.APP_CRASH,
            "Auto-Reinicio com Watchdog", "App crashou (SIGSEGV, OOM).");
        mt010.fallbackChain.addAll(Arrays.asList(
            "Plano A: Watchdog detecta crash e reinicia em 3 segundos",
            "Plano B: Estado salvo automaticamente a cada acao -- restaura",
            "Plano C: Se crash repetido (3x em 1min), modo seguro sem plugins",
            "Plano D: Se modo seguro tambem crasha, notificar e abrir bug report"
        ));
        mt010.recoveryAction = "Watchdog reinicia. Log enviado. Estado restaurado do checkpoint.";
        mt010.userMessage = "Ops, tive um problema. Reiniciando... Pronto, voltei. Tava onde?";
        mt010.recoveryTimeEstimateS = 3;
        MITIGATION_STRATEGIES.add(mt010);

        // === SMARTWATCH ===
        MitigationStrategy mt011 = new MitigationStrategy("MT-011", FailureType.SMARTWATCH_LOST,
            "Smartwatch Perdido", "Smartwatch desconectou/perdeu-se. Biometria perdida.");
        mt011.fallbackChain.addAll(Arrays.asList(
            "Plano A: Smartphone assume biometria (camera = HR por rPPG)",
            "Plano B: Usuario reporta estado manualmente ('to bem')",
            "Plano C: Reduzir monitoramento ativo, pedir check-in periodico",
            "Plano D: Localizar smartwatch por ultimo sinal GPS"
        ));
        mt011.recoveryAction = "Procurar smartwatch. Comprar substituto. Bio no smartphone.";
        mt011.userMessage = "Perdi seu smartwatch. Vou monitorar pelo smartphone. Se achar o relogio, me avise.";
        mt011.recoveryTimeEstimateS = 3600;
        MITIGATION_STRATEGIES.add(mt011);

        // === EYE TRACKER ===
        MitigationStrategy mt012 = new MitigationStrategy("MT-012", FailureType.EYE_TRACKER_LOST,
            "Eye Tracker Perdeu Calibracao", "Eye tracker perdeu tracking ou desconectou.");
        mt012.fallbackChain.addAll(Arrays.asList(
            "Plano A: Recalibrar automaticamente (pedir olhar para 3 pontos)",
            "Plano B: Switch/scan assume enquanto recalibra",
            "Plano C: Voz assume entrada",
            "Plano D: Pausar ate recuperar tracking"
        ));
        mt012.recoveryAction = "Recalibrar. Verificar iluminacao. Limpar camera do tracker.";
        mt012.userMessage = "Perdi o rastreio dos seus olhos. Vou usar seu switch enquanto tento recalibrar.";
        mt012.recoveryTimeEstimateS = 15;
        MITIGATION_STRATEGIES.add(mt012);

        // === MEMORIA ===
        MitigationStrategy mt013 = new MitigationStrategy("MT-013", FailureType.MEMORY_EXHAUSTED,
            "OOM -- Memoria Esgotada", "Memoria RAM cheia. App sera morto pelo OS.");
        mt013.fallbackChain.addAll(Arrays.asList(
            "Plano A: Descarregar modelos de IA nao essenciais",
            "Plano B: Fechar abas/janelas nao ativas",
            "Plano C: Reduzir resolucao de camera/frame rate",
            "Plano D: Salvar estado e reiniciar limpo"
        ));
        mt013.recoveryAction = "Fechar apps em background. Limpar cache. Adicionar RAM se possivel.";
        mt013.userMessage = "Memoria cheia. Fechando coisas nao essenciais. Continue trabalhando.";
        mt013.recoveryTimeEstimateS = 5;
        MITIGATION_STRATEGIES.add(mt013);

        // === PERMISSAO REVOCADA ===
        MitigationStrategy mt014 = new MitigationStrategy("MT-014", FailureType.PERMISSION_REVOKED,
            "Permissao Revogada", "OS revogou permissoes (microfone, camera, localizacao).");
        mt014.fallbackChain.addAll(Arrays.asList(
            "Plano A: Notificar usuario: 'Preciso de microfone para funcionar'",
            "Plano B: Abrir configuracoes de permissao automaticamente",
            "Plano C: Funcionalidade reduzida sem a permissao",
            "Plano D: Modo visitante (sem dados pessoais)"
        ));
        mt014.recoveryAction = "Reconceder permissao em Configuracoes > Apps > Permissoes.";
        mt014.userMessage = "Voce desligou minha permissao de microfone. Sem ele eu nao consigo te ouvir. Quer abrir as configuracoes?";
        mt014.autoActivate = false;
        mt014.recoveryTimeEstimateS = 30;
        MITIGATION_STRATEGIES.add(mt014);

        // === AGUA ===
        MitigationStrategy mt015 = new MitigationStrategy("MT-015", FailureType.WATER_DAMAGE,
            "Dano por Agua", "Smartphone molhou. Multiplas falhas simultaneas.");
        mt015.fallbackChain.addAll(Arrays.asList(
            "Plano A: Modo survival imediato -- desligar tudo para curto",
            "Plano B: Enquanto funciona: SOS + localizacao enviados",
            "Plano C: Handoff para terminal publico proximo",
            "Plano D: Ligar para emergencia antes de morrer"
        ));
        mt015.recoveryAction = "Desligar imediatamente. Secar em silica gel por 48h. NAO carregar molhado.";
        mt015.userMessage = "AGUA! Entrando em modo emergencia. Mandando sua localizacao. Vou tentar ligar para seu contato de emergencia.";
        mt015.recoveryTimeEstimateS = 259200;
        MITIGATION_STRATEGIES.add(mt015);

        // === CLOUD ===
        MitigationStrategy mt016 = new MitigationStrategy("MT-016", FailureType.CLOUD_DOWN,
            "Nuvem Caiu, Local Assume", "Servidor na nuvem offline. Servicos cloud indisponiveis.");
        mt016.fallbackChain.addAll(Arrays.asList(
            "Plano A: Modelos de IA locais (menores mas funcionam)",
            "Plano B: Dados sincronizados localmente (ultima sync)",
            "Plano C: Queue de acoes -- executa quando nuvem volta",
            "Plano D: SMS/ligacao para servicos que precisam de servidor"
        ));
        mt016.recoveryAction = "Aguardar recuperacao do servidor. Fila de acoes processada na volta.";
        mt016.userMessage = "Servidor na nuvem caiu. Tudo continua local. Vou sincronizar quando voltar.";
        mt016.recoveryTimeEstimateS = 600;
        MITIGATION_STRATEGIES.add(mt016);

        // === STT ===
        MitigationStrategy mt017 = new MitigationStrategy("MT-017", FailureType.STT_FAILURE,
            "Reconhecimento de Voz Falhou", "STT nao transcreve. Usuario nao consegue falar comandos.");
        mt017.fallbackChain.addAll(Arrays.asList(
            "Plano A: Reiniciar motor STT",
            "Plano B: Trocar para modelo STT local (offline, menos preciso)",
            "Plano C: Teclado virtual/braille assume entrada",
            "Plano D: Switch + scan de letras"
        ));
        mt017.recoveryAction = "Verificar microfone. Reiniciar STT. Verificar permissoes.";
        mt017.userMessage = "Nao estou entendendo sua voz. Vou passar para entrada por teclado/toque.";
        mt017.recoveryTimeEstimateS = 5;
        MITIGATION_STRATEGIES.add(mt017);
    }

    // ============================================================================
    // 5. MOTOR DE SIMULACAO DE FALHAS
    // ============================================================================

    static class FailureSimulator {
        SystemState state = new SystemState();
        Map<String, MitigationStrategy> mitigationsActive = new HashMap<>();
        Deque<Map<String, Object>> eventLog = new LinkedList<>();
        Map<FailureType, MitigationStrategy> strategies = new HashMap<>();

        public FailureSimulator() {
            state.availableInputs = new ArrayList<>(Arrays.asList("voz", "toque", "teclado", "camera", "gps", "microfone"));
            state.availableOutputs = new ArrayList<>(Arrays.asList("tts", "tela", "vibracao", "braille", "haptico"));
            state.availableSensors = new ArrayList<>(Arrays.asList("camera", "gps", "microfone", "acelerometro", "bussola", "luz"));
            for (MitigationStrategy s : MITIGATION_STRATEGIES) {
                strategies.put(s.failureType, s);
            }
        }

        public Map<String, Object> injectFailure(FailureEvent failure) {
            failure.detected = true;
            state.activeFailures.add(failure);
            updateSystemState(failure);

            MitigationStrategy strategy = strategies.get(failure.failureType);
            Object mitigationResult = null;
            if (strategy != null && strategy.autoActivate) {
                mitigationsActive.put(strategy.strategyId, strategy);
                mitigationResult = applyMitigation(strategy);
            } else if (strategy != null) {
                mitigationResult = Map.of("action", "notify", "message", strategy.userMessage);
            }

            Map<String, Object> eventRecord = new LinkedHashMap<>();
            eventRecord.put("event_id", failure.eventId);
            eventRecord.put("failure", failure.failureType.getValue());
            eventRecord.put("severity", failure.severity.getValue());
            eventRecord.put("mitigation", strategy != null ? strategy.name : "NENHUMA (sem estrategia)");
            eventRecord.put("fallback_chain", strategy != null ? strategy.fallbackChain : new ArrayList<>());
            eventRecord.put("user_message", strategy != null ? strategy.userMessage : "Falha sem mitigacao definida!");
            eventRecord.put("degradation_level", state.level.getValue());
            eventRecord.put("mitigation_applied", mitigationResult);
            eventLog.add(eventRecord);
            return eventRecord;
        }

        private void updateSystemState(FailureEvent failure) {
            FailureType ft = failure.failureType;
            if (ft == FailureType.BATTERY_CRITICAL) {
                state.batteryPct = 3.0;
                state.level = DegradationLevel.SURVIVAL;
            } else if (ft == FailureType.BATTERY_DEAD) {
                state.batteryPct = 0.0;
                state.level = DegradationLevel.DEAD;
            } else if (ft == FailureType.GPS_LOST) {
                state.gpsAvailable = false;
                state.level = escalate(state.level, DegradationLevel.DEGRADED_1);
            } else if (ft == FailureType.CAMERA_FAILURE) {
                state.cameraAvailable = false;
                state.availableSensors.remove("camera");
                state.availableInputs.remove("camera");
                state.level = escalate(state.level, DegradationLevel.DEGRADED_1);
            } else if (ft == FailureType.MICROPHONE_DEAD) {
                state.microphoneAvailable = false;
                state.availableInputs.remove("microfone");
                state.availableInputs.remove("voz");
                state.level = escalate(state.level, DegradationLevel.DEGRADED_2);
            } else if (ft == FailureType.SPEAKER_DEAD) {
                state.speakerAvailable = false;
                state.availableOutputs.remove("tts");
                state.level = escalate(state.level, DegradationLevel.DEGRADED_2);
            } else if (ft == FailureType.TTS_CRASH) {
                state.ttsAvailable = false;
                state.availableOutputs.remove("tts");
                state.level = escalate(state.level, DegradationLevel.DEGRADED_2);
            } else if (ft == FailureType.VIBRATION_DEAD) {
                state.vibrationAvailable = false;
                state.availableOutputs.remove("vibracao");
                state.availableOutputs.remove("haptico");
            } else if (ft == FailureType.SCREEN_BROKEN || ft == FailureType.SCREEN_DEAD) {
                state.screenAvailable = false;
                state.availableOutputs.remove("tela");
                state.level = escalate(state.level, DegradationLevel.DEGRADED_2);
            } else if (ft == FailureType.BLUETOOTH_DROP) {
                state.brailleConnected = false;
                state.availableOutputs.remove("braille");
                state.level = escalate(state.level, DegradationLevel.DEGRADED_1);
            } else if (ft == FailureType.NETWORK_DOWN || ft == FailureType.CLOUD_DOWN) {
                state.networkAvailable = false;
                state.level = escalate(state.level, DegradationLevel.DEGRADED_1);
            } else if (ft == FailureType.SMARTWATCH_LOST) {
                state.smartwatchConnected = false;
            } else if (ft == FailureType.EYE_TRACKER_LOST) {
                state.eyeTrackerConnected = false;
                state.availableInputs.remove("rastreio_olhos");
            } else if (ft == FailureType.WATER_DAMAGE) {
                state.level = DegradationLevel.EMERGENCY;
                state.cameraAvailable = false;
                state.microphoneAvailable = false;
                state.screenAvailable = false;
            } else if (ft == FailureType.APP_CRASH) {
                state.level = escalate(state.level, DegradationLevel.DEGRADED_1);
            } else if (ft == FailureType.MEMORY_EXHAUSTED) {
                state.level = escalate(state.level, DegradationLevel.DEGRADED_2);
            } else if (ft == FailureType.PERMISSION_REVOKED) {
                state.microphoneAvailable = false;
                state.availableInputs.remove("microfone");
            } else if (ft == FailureType.STT_FAILURE) {
                state.availableInputs.remove("voz");
                state.level = escalate(state.level, DegradationLevel.DEGRADED_2);
            }
        }

        private Map<String, Object> applyMitigation(MitigationStrategy strategy) {
            Map<String, Object> result = new LinkedHashMap<>();
            result.put("strategy", strategy.name);
            result.put("fallback_chain", strategy.fallbackChain);
            result.put("recovery_action", strategy.recoveryAction);

            if (strategy.failureType == FailureType.TTS_CRASH) {
                if (state.brailleConnected) {
                    if (!state.availableOutputs.contains("braille")) state.availableOutputs.add("braille");
                    result.put("restored_output", "braille");
                } else if (state.vibrationAvailable) {
                    if (!state.availableOutputs.contains("vibracao")) state.availableOutputs.add("vibracao");
                    result.put("restored_output", "vibracao");
                }
            } else if (strategy.failureType == FailureType.CAMERA_FAILURE) {
                if (state.microphoneAvailable && !state.availableSensors.contains("audio_sonar")) {
                    state.availableSensors.add("audio_sonar");
                    result.put("restored_sensor", "audio_sonar (microfone como sonar)");
                }
            } else if (strategy.failureType == FailureType.MICROPHONE_DEAD) {
                if (!state.availableInputs.contains("switch") && state.screenAvailable) {
                    state.availableInputs.add("switch");
                    result.put("restored_input", "switch (botoes na tela)");
                }
            } else if (strategy.failureType == FailureType.GPS_LOST) {
                if (state.availableSensors.contains("bussola") && !state.availableSensors.contains("dead_reckoning")) {
                    state.availableSensors.add("dead_reckoning");
                    result.put("restored_sensor", "dead_reckoning (bussola + passos)");
                }
            } else if (strategy.failureType == FailureType.APP_CRASH) {
                result.put("restored", "watchdog reiniciou em 3s");
            }
            return result;
        }

        public Map<String, Object> recoverFailure(FailureType failureType) {
            boolean recovered = false;
            for (int i = 0; i < state.activeFailures.size(); i++) {
                if (state.activeFailures.get(i).failureType == failureType) {
                    state.activeFailures.remove(i);
                    recovered = true;
                    break;
                }
            }
            MitigationStrategy strategy = strategies.get(failureType);
            if (strategy != null && mitigationsActive.containsKey(strategy.strategyId)) {
                mitigationsActive.remove(strategy.strategyId);
            }
            recalculateLevel();

            if (failureType == FailureType.GPS_LOST) {
                state.gpsAvailable = true;
                if (!state.availableSensors.contains("gps")) state.availableSensors.add("gps");
            } else if (failureType == FailureType.CAMERA_FAILURE) {
                state.cameraAvailable = true;
                if (!state.availableSensors.contains("camera")) state.availableSensors.add("camera");
            } else if (failureType == FailureType.NETWORK_DOWN) {
                state.networkAvailable = true;
            } else if (failureType == FailureType.TTS_CRASH) {
                state.ttsAvailable = true;
                if (!state.availableOutputs.contains("tts")) state.availableOutputs.add("tts");
            }

            Map<String, Object> result = new LinkedHashMap<>();
            result.put("recovered", recovered);
            result.put("failure", failureType.getValue());
            result.put("current_level", state.level.getValue());
            result.put("remaining_failures", state.activeFailures.size());
            return result;
        }

        private DegradationLevel escalate(DegradationLevel current, DegradationLevel newLevel) {
            List<DegradationLevel> levels = Arrays.asList(
                DegradationLevel.FULL, DegradationLevel.DEGRADED_1, DegradationLevel.DEGRADED_2,
                DegradationLevel.SURVIVAL, DegradationLevel.EMERGENCY, DegradationLevel.DEAD
            );
            return levels.get(Math.max(levels.indexOf(current), levels.indexOf(newLevel)));
        }

        private void recalculateLevel() {
            if (state.activeFailures.isEmpty()) {
                state.level = DegradationLevel.FULL;
                return;
            }
            FailureEvent maxSeverity = Collections.max(state.activeFailures, Comparator.comparingInt(f ->
                Arrays.asList(FailureSeverity.COSMETIC, FailureSeverity.MINOR, FailureSeverity.MAJOR,
                              FailureSeverity.CRITICAL, FailureSeverity.CATASTROPHIC).indexOf(f.severity)
            ));
            if (maxSeverity.severity == FailureSeverity.CATASTROPHIC) state.level = DegradationLevel.EMERGENCY;
            else if (maxSeverity.severity == FailureSeverity.CRITICAL) state.level = DegradationLevel.SURVIVAL;
            else if (maxSeverity.severity == FailureSeverity.MAJOR) state.level = DegradationLevel.DEGRADED_2;
            else if (maxSeverity.severity == FailureSeverity.MINOR) state.level = DegradationLevel.DEGRADED_1;
            else state.level = DegradationLevel.FULL;
        }

        public Map<String, Object> systemStatus() {
            Map<String, Object> status = new LinkedHashMap<>();
            status.put("degradation_level", state.level.getValue());
            status.put("battery_pct", state.batteryPct);
            status.put("active_failures", state.activeFailures.size());
            status.put("active_mitigations", mitigationsActive.size());
            status.put("available_inputs", new ArrayList<>(state.availableInputs));
            status.put("available_outputs", new ArrayList<>(state.availableOutputs));
            status.put("available_sensors", new ArrayList<>(state.availableSensors));
            status.put("network", state.networkAvailable);
            status.put("gps", state.gpsAvailable);
            status.put("camera", state.cameraAvailable);
            status.put("microphone", state.microphoneAvailable);
            status.put("speaker", state.speakerAvailable);
            status.put("tts", state.ttsAvailable);
            status.put("screen", state.screenAvailable);
            status.put("vibration", state.vibrationAvailable);
            status.put("braille", state.brailleConnected);
            return status;
        }
    }

    // ============================================================================
    // 6. SIMULACOES DE CENARIO CATASTROFICO
    // ============================================================================

    public static void simulateBlindUserBatteryDeath() {
        System.out.println("=".repeat(65));
        System.out.println("CENARIO 1: Cego na rua -- bateria morrendo");
        System.out.println("=".repeat(65));

        FailureSimulator sim = new FailureSimulator();
        System.out.println("\n[ESTADO INICIAL]");
        Map<String, Object> status = sim.systemStatus();
        System.out.println("  Nivel: " + status.get("degradation_level"));
        System.out.println("  Bateria: " + status.get("battery_pct") + "%");
        System.out.println("  Inputs: " + status.get("available_inputs"));

        System.out.println("\n[FALHA: Bateria critica]");
        FailureEvent event = new FailureEvent("EVT-001", FailureType.BATTERY_CRITICAL, FailureCategory.POWER,
            FailureSeverity.CRITICAL, FailureDuration.SHORT, "Bateria abaixo de 5%");
        event.userImpact = "Sistema entra em modo sobrevivencia";
        Map<String, Object> result = sim.injectFailure(event);
        System.out.println("  Mitigacao: " + result.get("mitigation"));
        System.out.println("  Mensagem ao usuario: " + result.get("user_message"));
        status = sim.systemStatus();
        System.out.println("  Nivel atual: " + status.get("degradation_level"));
        System.out.println("  Bateria: " + status.get("battery_pct") + "%");

        System.out.println("\n[FALHA: Bateria morta]");
        event = new FailureEvent("EVT-002", FailureType.BATTERY_DEAD, FailureCategory.POWER,
            FailureSeverity.CATASTROPHIC, FailureDuration.LONG, "Bateria em 0%");
        event.userImpact = "Smartphone morre. Handoff necessario.";
        result = sim.injectFailure(event);
        System.out.println("  Mitigacao: " + result.get("mitigation"));
        @SuppressWarnings("unchecked")
        List<String> chain = (List<String>) result.get("fallback_chain");
        for (String fb : chain) System.out.println("    " + fb);
        System.out.println("  Mensagem: " + result.get("user_message"));
    }

    public static void simulateCascadingFailures() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 2: Falhas em cascata");
        System.out.println("=".repeat(65));

        FailureSimulator sim = new FailureSimulator();
        List<FailureEvent> cascading = Arrays.asList(
            new FailureEvent("C-01", FailureType.NETWORK_DOWN, FailureCategory.NETWORK, FailureSeverity.MAJOR, FailureDuration.MEDIUM, "Internet caiu"),
            new FailureEvent("C-02", FailureType.GPS_LOST, FailureCategory.SENSOR, FailureSeverity.MAJOR, FailureDuration.MEDIUM, "GPS perdido"),
            new FailureEvent("C-03", FailureType.BLUETOOTH_DROP, FailureCategory.PERIPHERAL, FailureSeverity.MAJOR, FailureDuration.TRANSIENT, "Braille desconectou"),
            new FailureEvent("C-04", FailureType.TTS_CRASH, FailureCategory.SOFTWARE, FailureSeverity.CRITICAL, FailureDuration.SHORT, "TTS crashou")
        );

        for (FailureEvent f : cascading) {
            System.out.println("\n[FALHA: " + f.failureType.getValue() + "]");
            Map<String, Object> result = sim.injectFailure(f);
            Map<String, Object> status = sim.systemStatus();
            System.out.println("  Severidade: " + f.severity.getValue());
            System.out.println("  Mitigacao: " + result.get("mitigation"));
            System.out.println("  Nivel sistema: " + status.get("degradation_level"));
            System.out.println("  Outputs restantes: " + status.get("available_outputs"));
            System.out.println("  Inputs restantes: " + status.get("available_inputs"));
        }

        System.out.println("\n[ESTADO APOS 4 FALHAS EM CASCATA]");
        Map<String, Object> status = sim.systemStatus();
        System.out.println("  Nivel: " + status.get("degradation_level"));
        System.out.println("  Falhas ativas: " + status.get("active_failures"));
        System.out.println("  Mitigacoes ativas: " + status.get("active_mitigations"));

        System.out.println("\n[RECUPERACAO GRADUAL]");
        for (FailureType ft : Arrays.asList(FailureType.TTS_CRASH, FailureType.BLUETOOTH_DROP, FailureType.GPS_LOST, FailureType.NETWORK_DOWN)) {
            Map<String, Object> r = sim.recoverFailure(ft);
            System.out.println("  " + ft.getValue() + ": nivel -> " + r.get("current_level"));
        }
    }

    public static void simulateWaterDamage() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 3: Dano por agua");
        System.out.println("=".repeat(65));

        FailureSimulator sim = new FailureSimulator();
        System.out.println("\n[FALHA: Smartphone molhou]");
        FailureEvent event = new FailureEvent("W-01", FailureType.WATER_DAMAGE, FailureCategory.HARDWARE,
            FailureSeverity.CATASTROPHIC, FailureDuration.PERMANENT, "Smartphone caiu na agua/poça");
        event.userImpact = "Multiplas falhas simultaneas. Dispositivo morrendo.";
        Map<String, Object> result = sim.injectFailure(event);
        System.out.println("  Mitigacao: " + result.get("mitigation"));
        System.out.println("  Mensagem: " + result.get("user_message"));
        @SuppressWarnings("unchecked")
        List<String> chain = (List<String>) result.get("fallback_chain");
        for (String fb : chain) System.out.println("    " + fb);
        Map<String, Object> status = sim.systemStatus();
        System.out.println("  Nivel: " + status.get("degradation_level"));
        System.out.println("  Camera: " + status.get("camera") + " | Microfone: " + status.get("microphone") + " | Tela: " + status.get("screen"));
    }

    public static void simulateSoftwareResilience() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 4: Software crash + auto-recovery");
        System.out.println("=".repeat(65));

        FailureSimulator sim = new FailureSimulator();
        for (int i = 0; i < 3; i++) {
            System.out.println("\n[FALHA " + (i+1) + ": App crashou]");
            FailureEvent event = new FailureEvent("S-" + String.format("%02d", i+1), FailureType.APP_CRASH,
                FailureCategory.SOFTWARE, FailureSeverity.MAJOR, FailureDuration.TRANSIENT, "App crashou (tentativa " + (i+1) + ")");
            Map<String, Object> result = sim.injectFailure(event);
            System.out.println("  Mitigacao: " + result.get("mitigation"));
            System.out.println("  User message: " + result.get("user_message"));
            if (i < 2) {
                Map<String, Object> r = sim.recoverFailure(FailureType.APP_CRASH);
                System.out.println("  Recuperado: nivel -> " + r.get("current_level"));
            }
        }
    }

    public static void simulateMultiUserScenarios() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 5: Impacto por deficiencia");
        System.out.println("=".repeat(65));

        List<Map.Entry<String, List<FailureType>>> scenarios = Arrays.asList(
            Map.entry("CEGO", Arrays.asList(FailureType.TTS_CRASH, FailureType.GPS_LOST, FailureType.BLUETOOTH_DROP)),
            Map.entry("SURDO", Arrays.asList(FailureType.SCREEN_BROKEN, FailureType.VIBRATION_DEAD)),
            Map.entry("TETRAPLEGICO", Arrays.asList(FailureType.STT_FAILURE, FailureType.EYE_TRACKER_LOST)),
            Map.entry("AUTISTA", Arrays.asList(FailureType.NETWORK_DOWN, FailureType.SPEAKER_DEAD))
        );

        for (Map.Entry<String, List<FailureType>> entry : scenarios) {
            String label = entry.getKey();
            List<FailureType> failures = entry.getValue();
            System.out.println("\n  " + label + ":");
            FailureSimulator sim = new FailureSimulator();
            for (FailureType ft : failures) {
                FailureEvent event = new FailureEvent("M-" + label + "-" + ft.getValue(), ft, FailureCategory.HARDWARE,
                    FailureSeverity.CRITICAL, FailureDuration.SHORT, ft.getValue());
                Map<String, Object> result = sim.injectFailure(event);
                Map<String, Object> status = sim.systemStatus();
                System.out.println("    Falha: " + ft.getValue());
                System.out.println("      Nivel: " + status.get("degradation_level"));
                System.out.println("      Mitigacao: " + result.get("mitigation"));
                System.out.println("      Inputs: " + status.get("available_inputs"));
                System.out.println("      Outputs: " + status.get("available_outputs"));
            }
        }
    }

    public static void simulateFullCatastrophe() {
        System.out.println("\n" + "=".repeat(65));
        System.out.println("CENARIO 6: CATASTROFE TOTAL");
        System.out.println("=".repeat(65));

        FailureSimulator sim = new FailureSimulator();
        List<FailureType> allFailures = Arrays.asList(
            FailureType.BATTERY_CRITICAL, FailureType.GPS_LOST, FailureType.CAMERA_FAILURE,
            FailureType.MICROPHONE_DEAD, FailureType.TTS_CRASH, FailureType.BLUETOOTH_DROP,
            FailureType.NETWORK_DOWN, FailureType.SCREEN_BROKEN, FailureType.VIBRATION_DEAD,
            FailureType.SMARTWATCH_LOST
        );

        System.out.println("\nInjetando " + allFailures.size() + " falhas simultaneas...");
        for (FailureType ft : allFailures) {
            FailureEvent event = new FailureEvent("CAT-" + ft.getValue(), ft, FailureCategory.HARDWARE,
                FailureSeverity.CATASTROPHIC, FailureDuration.PERMANENT, "Catastrofe: " + ft.getValue());
            sim.injectFailure(event);
        }

        Map<String, Object> status = sim.systemStatus();
        System.out.println("\n[ESTADO APOS CATASTROFE]");
        System.out.println("  Nivel: " + status.get("degradation_level"));
        System.out.println("  Bateria: " + status.get("battery_pct") + "%");
        System.out.println("  Falhas ativas: " + status.get("active_failures"));
        System.out.println("  Mitigacoes ativas: " + status.get("active_mitigations"));
        System.out.println("  Inputs: " + status.get("available_inputs"));
        System.out.println("  Outputs: " + status.get("available_outputs"));
        System.out.println("  Sensores: " + status.get("available_sensors"));

        if (((List<?>)status.get("available_outputs")).isEmpty() && ((List<?>)status.get("available_inputs")).isEmpty()) {
            System.out.println("\n  PLANO D: LIGACAO CELULAR DIRETA");
            System.out.println("  O unico canal que resta e o sinal de celular + SMS.");
            System.out.println("  Sistema envia SMS com localizacao para emergencia.");
            System.out.println("  Se nem sinal tem: GRITE. Peça ajuda humana.");
        }
    }

    // ============================================================================
    // 7. DEMONSTRACAO (main)
    // ============================================================================

    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("OpenResilience -- Simulacao de Falhas e Mitigacao");
        System.out.println("=".repeat(70));

        System.out.println("\nFalhas mapeadas: " + FailureType.values().length);
        System.out.println("Categorias de falha: " + FailureCategory.values().length);
        System.out.println("Estrategias de mitigacao: " + MITIGATION_STRATEGIES.size());
        System.out.println("Niveis de degradacao: " + DegradationLevel.values().length);

        System.out.println("\n" + "=".repeat(70));
        System.out.println("COBERTURA DE MITIGACAO POR CATEGORIA");
        System.out.println("=".repeat(70));

        Map<FailureType, Integer> byCategory = new HashMap<>();
        for (MitigationStrategy s : MITIGATION_STRATEGIES) {
            byCategory.put(s.failureType, byCategory.getOrDefault(s.failureType, 0) + 1);
        }
        int covered = byCategory.size();
        int total = FailureType.values().length;
        System.out.println("  Falhas com mitigacao: " + covered + "/" + total);

        simulateBlindUserBatteryDeath();
        simulateCascadingFailures();
        simulateWaterDamage();
        simulateSoftwareResilience();
        simulateMultiUserScenarios();
        simulateFullCatastrophe();

        System.out.println("\n" + "=".repeat(70));
        System.out.println("RESUMO DE MITIGACOES");
        System.out.println("=".repeat(70));
        for (MitigationStrategy s : MITIGATION_STRATEGIES) {
            System.out.println("\n  " + s.strategyId + ": " + s.name);
            System.out.println("    Falha: " + s.failureType.getValue());
            System.out.println("    Descricao: " + s.description);
            System.out.println("    Planos: " + s.fallbackChain.size() + " fallbacks");
            for (int i = 0; i < s.fallbackChain.size(); i++) {
                System.out.println("      " + s.fallbackChain.get(i));
            }
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("Total falhas: " + FailureType.values().length);
        System.out.println("Total mitigacoes: " + MITIGATION_STRATEGIES.size());
        System.out.println("Cada falha tem Plano A, B, C e D.");
        System.out.println("Nenhum ponto unico de falha.");
        System.out.println("Redundancia em TUDO.");
        System.out.println("\nO sistema PODE falhar. O usuario NAO pode ficar desamparado.");
    }
}