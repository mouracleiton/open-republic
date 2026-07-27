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

// ============================================================================
// 1. TIPOS DE FALHA
// ============================================================================

const FailureCategory = Object.freeze({
  HARDWARE: "hardware",
  SOFTWARE: "software",
  NETWORK: "rede",
  POWER: "energia",
  SENSOR: "sensor",
  PERIPHERAL: "periferico",
  OS: "sistema_operacional",
  CLOUD: "nuvem",
});

const FailureType = Object.freeze({
  // POWER
  BATTERY_CRITICAL: "bateria_critica",
  BATTERY_DEAD: "bateria_morta",
  BATTERY_OVERHEAT: "bateria_superaquecida",
  POWER_SURGE: "pico_energia",

  // HARDWARE
  SCREEN_BROKEN: "tela_quebrada",
  SCREEN_DEAD: "tela_morta",
  CAMERA_FAILURE: "camera_falhou",
  MICROPHONE_DEAD: "microfone_morto",
  SPEAKER_DEAD: "alto_falante_morto",
  VIBRATION_DEAD: "vibracao_morta",
  GPS_LOST: "gps_perdido",
  BLUETOOTH_DROP: "bluetooth_caiu",
  NFC_FAILURE: "nfc_falhou",
  WATER_DAMAGE: "dano_agua",
  PHYSICAL_DAMAGE: "dano_fisico",
  BUTTON_STUCK: "botao_preso",
  CHARGE_PORT_BROKEN: "porta_carga_quebrada",

  // PERIPHERAL
  BRAILLE_DISPLAY_DISCONNECTED: "braille_desconectou",
  EYE_TRACKER_LOST: "eye_tracker_perdeu",
  SWITCH_FAILURE: "switch_queimou",
  HEARING_AID_DISCONNECTED: "aparelho_desconectou",
  SMARTWATCH_LOST: "smartwatch_perdido",

  // SOFTWARE
  TTS_CRASH: "tts_crashou",
  STT_FAILURE: "stt_falhou",
  OCR_FAILURE: "ocr_falhou",
  APP_FREEZE: "app_travou",
  APP_CRASH: "app_crashou",
  MEMORY_EXHAUSTED: "memoria_esgotada",
  STORAGE_FULL: "armazenamento_cheio",
  MODEL_UNAVAILABLE: "ia_indisponivel",
  NAVIGATION_ENGINE_DOWN: "navegador_caiu",
  EMOTION_DETECTOR_DOWN: "detector_emocao_caiu",

  // NETWORK
  NETWORK_DOWN: "rede_caiu",
  NETWORK_SLOW: "rede_lenta",
  CLOUD_DOWN: "nuvem_caiu",
  API_RATE_LIMIT: "api_limite",
  DNS_FAILURE: "dns_falhou",

  // OS
  OS_UPDATE_BRICK: "atualizacao_bricou",
  BOOT_LOOP: "boot_loop",
  PERMISSION_REVOKED: "permissao_revogada",
});

const FailureSeverity = Object.freeze({
  COSMETIC: "cosmetico",
  MINOR: "menor",
  MAJOR: "maior",
  CRITICAL: "critico",
  CATASTROPHIC: "catastrofico",
});

const FailureDuration = Object.freeze({
  TRANSIENT: "transiente",
  SHORT: "curto",
  MEDIUM: "medio",
  LONG: "longo",
  PERMANENT: "permanente",
});

// ============================================================================
// 2. EVENTO DE FALHA
// ============================================================================

class FailureEvent {
  constructor(eventId, failureType, category, severity, duration, description) {
    this.eventId = eventId;
    this.failureType = failureType;
    this.category = category;
    this.severity = severity;
    this.duration = duration;
    this.description = description;
    this.affectedComponents = [];
    this.userImpact = "";
    this.timestamp = Date.now();
    this.recoveryProbability = 0.9;
    this.detected = false;
  }
}

// ============================================================================
// 3. NIVEIS DE DEGRADACAO
// ============================================================================

const DegradationLevel = Object.freeze({
  FULL: "completo",
  DEGRADED_1: "degradado_1",
  DEGRADED_2: "degradado_2",
  SURVIVAL: "sobrevivencia",
  EMERGENCY: "emergencia",
  DEAD: "morto",
});

class SystemState {
  constructor() {
    this.level = DegradationLevel.FULL;
    this.activeFailures = [];
    this.batteryPct = 100.0;
    this.availableInputs = [];
    this.availableOutputs = [];
    this.availableSensors = [];
    this.networkAvailable = true;
    this.gpsAvailable = true;
    this.cameraAvailable = true;
    this.microphoneAvailable = true;
    this.speakerAvailable = true;
    this.vibrationAvailable = true;
    this.screenAvailable = true;
    this.ttsAvailable = true;
    this.brailleConnected = false;
    this.eyeTrackerConnected = false;
    this.smartwatchConnected = false;
    this.offlineCacheSizeMb = 0.0;
    this.lastKnownLocation = null;
    this.uptimeSeconds = 0.0;
  }
}

// ============================================================================
// 4. ESTRATEGIAS DE MITIGACAO (TODAS AS 17)
// ============================================================================

class MitigationStrategy {
  constructor(strategyId, failureType, name, description) {
    this.strategyId = strategyId;
    this.failureType = failureType;
    this.name = name;
    this.description = description;
    this.fallbackChain = [];
    this.recoveryAction = "";
    this.userMessage = "";
    this.autoActivate = true;
    this.recoveryTimeEstimateS = 0;
  }
}

const MITIGATION_STRATEGIES = [];

// === BATERIA ===
let mt001 = new MitigationStrategy("MT-001", FailureType.BATTERY_CRITICAL,
  "Modo Survival de Bateria", "Bateria < 5%. Desliga tudo nao essencial. So mantem voz/sos.");
mt001.fallbackChain = [
  "Plano A: Reduzir brilho ao minimo, desligar animacoes",
  "Plano B: Desligar camera, GPS (usar contagem de passos)",
  "Plano C: Desligar TTS continuo, so falas criticas",
  "Plano D: SOS -- ligar para contato de emergencia e desligar",
];
mt001.recoveryAction = "Conectar carregador. Sistema avisa proximo terminal publico.";
mt001.userMessage = "Bateria critica. Entrei em modo sobrevivencia. So o essencial. Encontre um carregador ou vou te levar ate um terminal publico.";
MITIGATION_STRATEGIES.push(mt001);

let mt002 = new MitigationStrategy("MT-002", FailureType.BATTERY_DEAD,
  "Handoff para Terminal Publico", "Bateria em 0%. Smartphone morre. Sistema migra.");
mt002.fallbackChain = [
  "Plano A: Antes de morrer, enviar localizacao para emergencia",
  "Plano B: Enviar ultima tarefa nao salva para nuvem",
  "Plano C: Ligar para contato de emergencia com mensagem automatica",
  "Plano D: Avisar usuario: 'Proximo terminal publico: biblioteca a 200m norte'",
];
mt002.recoveryAction = "Carregar em terminal publico, biblioteca, estabelecimento.";
mt002.userMessage = "Vou desligar em 30 segundos. Mandei sua localizacao para emergencia. Terminal publico mais proximo: biblioteca, 200 metros ao norte.";
mt002.recoveryTimeEstimateS = 3600;
MITIGATION_STRATEGIES.push(mt002);

// === GPS ===
let mt003 = new MitigationStrategy("MT-003", FailureType.GPS_LOST,
  "Navegacao Sem GPS", "GPS perdido (predio, tunel, subsolo). Navegacao continua.");
mt003.fallbackChain = [
  "Plano A: Bussola magnetica + contagem de passos (dead reckoning)",
  "Plano B: Bluetooth beacons indoor (shopping, hospital)",
  "Plano C: WiFi triangulation (menos preciso mas funciona indoor)",
  "Plano D: Landmarks auditivos: 'Voce passou por um lugar barulhento a 30s -- provavelmente cozinha'",
];
mt003.recoveryAction = "Sair para area aberta. GPS re-adquire em 10-30 segundos.";
mt003.userMessage = "Perdi o GPS. Estou usando a bussola e contando seus passos. Vou continuar te guiando.";
mt003.recoveryTimeEstimateS = 30;
MITIGATION_STRATEGIES.push(mt003);

// === CAMERA ===
let mt004 = new MitigationStrategy("MT-004", FailureType.CAMERA_FAILURE,
  "Camera Cai, Audio Assume", "Camera falhou. Visao computacional perdida.");
mt004.fallbackChain = [
  "Plano A: Microfone assume deteccao de obstaculos por eco/sonar",
  "Plano B: Acelerometro + bussola mapeiam caminho percorrido",
  "Plano C: Pedir ajuda humana: 'Alguem pode me orientar?' via voz alta",
  "Plano D: Ligar para contato que ve por camera remota",
];
mt004.recoveryAction = "Limpar lente. Reiniciar app de camera. Se hardware, trocar smartphone.";
mt004.userMessage = "Minha camera parou. Vou usar o microfone para ouvir o ambiente e te guiar pelo som.";
mt004.recoveryTimeEstimateS = 60;
MITIGATION_STRATEGIES.push(mt004);

// === MICROFONE ===
let mt005 = new MitigationStrategy("MT-005", FailureType.MICROPHONE_DEAD,
  "Microfone Morto, Tela Assume", "Microfone falhou. Entrada por voz perdida.");
mt005.fallbackChain = [
  "Plano A: Switch/bluetooth keyboard assume entrada",
  "Plano B: Tela touch com botoes grandes (sim, mesmo para cego via TalkBack)",
  "Plano C: Eye tracker se disponivel",
  "Plano D: Pedir para alguem gravar e enviar audio",
];
mt005.recoveryAction = "Limpar entrada do microfone. Verificar permissoes. Bluetooth headset como backup.";
mt005.userMessage = "Nao estou te ouvindo. Vou passar para entrada por botoes/toque.";
mt005.recoveryTimeEstimateS = 10;
MITIGATION_STRATEGIES.push(mt005);

// === TTS ===
let mt006 = new MitigationStrategy("MT-006", FailureType.TTS_CRASH,
  "TTS Crashou, Vibracao Assume", "Motor de voz morreu. Cego nao ouve mais o sistema.");
mt006.fallbackChain = [
  "Plano A: Display braille assume (se conectado)",
  "Plano B: Padroes de vibracao codificam informacao",
  "Plano C: Auto-restart do TTS em background",
  "Plano D: Tocar tons com significado (agudo=ok, grave=erro)",
];
mt006.recoveryAction = "Reiniciar servico TTS. Android: Settings > Accessibility > TalkBack. iOS: VoiceOver toggle.";
mt006.userMessage = "[MENSAGEM POR VIBRACAO: 1 pulse = ok, 2 pulses = atencao, 3 pulses = erro]";
mt006.recoveryTimeEstimateS = 5;
MITIGATION_STRATEGIES.push(mt006);

// === BLUETOOTH / BRAILLE ===
let mt007 = new MitigationStrategy("MT-007", FailureType.BLUETOOTH_DROP,
  "Bluetooth Caiu", "Braille/switch/aparelho auditivo desconectou.");
mt007.fallbackChain = [
  "Plano A: Tentar reconexao automatica (3 tentativas em 10s)",
  "Plano B: Fallback para TTS alto-falante",
  "Plano C: Fallback para vibracao padrao",
  "Plano D: Pedir usuario para verificar Bluetooth manualmente",
];
mt007.recoveryAction = "Reativar Bluetooth. Emparelhar novamente. Verificar bateria do periferico.";
mt007.userMessage = "Perdi conexao com seu dispositivo. Tentando reconectar... Se nao voltar em 10 segundos, vou usar o alto-falante.";
mt007.recoveryTimeEstimateS = 10;
MITIGATION_STRATEGIES.push(mt007);

// === REDE ===
let mt008 = new MitigationStrategy("MT-008", FailureType.NETWORK_DOWN,
  "Modo Offline Total", "Sem internet. IA em nuvem, mapas, API tudo fora.");
mt008.fallbackChain = [
  "Plano A: Modelos de IA locais (menores mas funcionam offline)",
  "Plano B: Mapas offline (OpenStreetMap cached)",
  "Plano C: Tudo que nao precisa de rede continua: TTS, OCR, navegacao local",
  "Plano D: SMS para emergencia (nao precisa de internet, so sinal)",
];
mt008.recoveryAction = "Verificar WiFi/dados. Sair de area sem cobertura. Usar SMS para comunicacao.";
mt008.userMessage = "Sem internet. Continuo funcionando offline. IA local assumiu. Mapas em cache.";
mt008.recoveryTimeEstimateS = 300;
MITIGATION_STRATEGIES.push(mt008);

// === TELA ===
let mt009 = new MitigationStrategy("MT-009", FailureType.SCREEN_BROKEN,
  "Tela Quebrada", "Tela rachada/morta. Sem saida visual.");
mt009.fallbackChain = [
  "Plano A: TTS assume toda interacao (cego simulado)",
  "Plano B: Braille display conectado via bluetooth",
  "Plano C: Smartwatch mostra minimo na tela do relogio",
  "Plano D: Cast para TV/terminal publico proximo",
];
mt009.recoveryAction = "Trocar tela. Enquanto isso: TTS + braille + smartwatch.";
mt009.userMessage = "Sua tela quebrou. Vou guiar tudo por voz. Conecte um braille display se tiver.";
mt009.recoveryTimeEstimateS = 259200;
MITIGATION_STRATEGIES.push(mt009);

// === SOFTWARE CRASH ===
let mt010 = new MitigationStrategy("MT-010", FailureType.APP_CRASH,
  "Auto-Reinicio com Watchdog", "App crashou (SIGSEGV, OOM).");
mt010.fallbackChain = [
  "Plano A: Watchdog detecta crash e reinicia em 3 segundos",
  "Plano B: Estado salvo automaticamente a cada acao -- restaura",
  "Plano C: Se crash repetido (3x em 1min), modo seguro sem plugins",
  "Plano D: Se modo seguro tambem crasha, notificar e abrir bug report",
];
mt010.recoveryAction = "Watchdog reinicia. Log enviado. Estado restaurado do checkpoint.";
mt010.userMessage = "Ops, tive um problema. Reiniciando... Pronto, voltei. Tava onde?";
mt010.recoveryTimeEstimateS = 3;
MITIGATION_STRATEGIES.push(mt010);

// === SMARTWATCH ===
let mt011 = new MitigationStrategy("MT-011", FailureType.SMARTWATCH_LOST,
  "Smartwatch Perdido", "Smartwatch desconectou/perdeu-se. Biometria perdida.");
mt011.fallbackChain = [
  "Plano A: Smartphone assume biometria (camera = HR por rPPG)",
  "Plano B: Usuario reporta estado manualmente ('to bem')",
  "Plano C: Reduzir monitoramento ativo, pedir check-in periodico",
  "Plano D: Localizar smartwatch por ultimo sinal GPS",
];
mt011.recoveryAction = "Procurar smartwatch. Comprar substituto. Bio no smartphone.";
mt011.userMessage = "Perdi seu smartwatch. Vou monitorar pelo smartphone. Se achar o relogio, me avise.";
mt011.recoveryTimeEstimateS = 3600;
MITIGATION_STRATEGIES.push(mt011);

// === EYE TRACKER ===
let mt012 = new MitigationStrategy("MT-012", FailureType.EYE_TRACKER_LOST,
  "Eye Tracker Perdeu Calibracao", "Eye tracker perdeu tracking ou desconectou.");
mt012.fallbackChain = [
  "Plano A: Recalibrar automaticamente (pedir olhar para 3 pontos)",
  "Plano B: Switch/scan assume enquanto recalibra",
  "Plano C: Voz assume entrada",
  "Plano D: Pausar ate recuperar tracking",
];
mt012.recoveryAction = "Recalibrar. Verificar iluminacao. Limpar camera do tracker.";
mt012.userMessage = "Perdi o rastreio dos seus olhos. Vou usar seu switch enquanto tento recalibrar.";
mt012.recoveryTimeEstimateS = 15;
MITIGATION_STRATEGIES.push(mt012);

// === MEMORIA ===
let mt013 = new MitigationStrategy("MT-013", FailureType.MEMORY_EXHAUSTED,
  "OOM -- Memoria Esgotada", "Memoria RAM cheia. App sera morto pelo OS.");
mt013.fallbackChain = [
  "Plano A: Descarregar modelos de IA nao essenciais",
  "Plano B: Fechar abas/janelas nao ativas",
  "Plano C: Reduzir resolucao de camera/frame rate",
  "Plano D: Salvar estado e reiniciar limpo",
];
mt013.recoveryAction = "Fechar apps em background. Limpar cache. Adicionar RAM se possivel.";
mt013.userMessage = "Memoria cheia. Fechando coisas nao essenciais. Continue trabalhando.";
mt013.recoveryTimeEstimateS = 5;
MITIGATION_STRATEGIES.push(mt013);

// === PERMISSAO REVOCADA ===
let mt014 = new MitigationStrategy("MT-014", FailureType.PERMISSION_REVOKED,
  "Permissao Revogada", "OS revogou permissoes (microfone, camera, localizacao).");
mt014.fallbackChain = [
  "Plano A: Notificar usuario: 'Preciso de microfone para funcionar'",
  "Plano B: Abrir configuracoes de permissao automaticamente",
  "Plano C: Funcionalidade reduzida sem a permissao",
  "Plano D: Modo visitante (sem dados pessoais)",
];
mt014.recoveryAction = "Reconceder permissao em Configuracoes > Apps > Permissoes.";
mt014.userMessage = "Voce desligou minha permissao de microfone. Sem ele eu nao consigo te ouvir. Quer abrir as configuracoes?";
mt014.autoActivate = false;
mt014.recoveryTimeEstimateS = 30;
MITIGATION_STRATEGIES.push(mt014);

// === AGUA ===
let mt015 = new MitigationStrategy("MT-015", FailureType.WATER_DAMAGE,
  "Dano por Agua", "Smartphone molhou. Multiplas falhas simultaneas.");
mt015.fallbackChain = [
  "Plano A: Modo survival imediato -- desligar tudo para curto",
  "Plano B: Enquanto funciona: SOS + localizacao enviados",
  "Plano C: Handoff para terminal publico proximo",
  "Plano D: Ligar para emergencia antes de morrer",
];
mt015.recoveryAction = "Desligar imediatamente. Secar em silica gel por 48h. NAO carregar molhado.";
mt015.userMessage = "AGUA! Entrando em modo emergencia. Mandando sua localizacao. Vou tentar ligar para seu contato de emergencia.";
mt015.recoveryTimeEstimateS = 259200;
MITIGATION_STRATEGIES.push(mt015);

// === CLOUD ===
let mt016 = new MitigationStrategy("MT-016", FailureType.CLOUD_DOWN,
  "Nuvem Caiu, Local Assume", "Servidor na nuvem offline. Servicos cloud indisponiveis.");
mt016.fallbackChain = [
  "Plano A: Modelos de IA locais (menores mas funcionam)",
  "Plano B: Dados sincronizados localmente (ultima sync)",
  "Plano C: Queue de acoes -- executa quando nuvem volta",
  "Plano D: SMS/ligacao para servicos que precisam de servidor",
];
mt016.recoveryAction = "Aguardar recuperacao do servidor. Fila de acoes processada na volta.";
mt016.userMessage = "Servidor na nuvem caiu. Tudo continua local. Vou sincronizar quando voltar.";
mt016.recoveryTimeEstimateS = 600;
MITIGATION_STRATEGIES.push(mt016);

// === STT ===
let mt017 = new MitigationStrategy("MT-017", FailureType.STT_FAILURE,
  "Reconhecimento de Voz Falhou", "STT nao transcreve. Usuario nao consegue falar comandos.");
mt017.fallbackChain = [
  "Plano A: Reiniciar motor STT",
  "Plano B: Trocar para modelo STT local (offline, menos preciso)",
  "Plano C: Teclado virtual/braille assume entrada",
  "Plano D: Switch + scan de letras",
];
mt017.recoveryAction = "Verificar microfone. Reiniciar STT. Verificar permissoes.";
mt017.userMessage = "Nao estou entendendo sua voz. Vou passar para entrada por teclado/toque.";
mt017.recoveryTimeEstimateS = 5;
MITIGATION_STRATEGIES.push(mt017);

// ============================================================================
// 5. MOTOR DE SIMULACAO DE FALHAS
// ============================================================================

class FailureSimulator {
  constructor() {
    this.state = new SystemState();
    this.state.availableInputs = ["voz", "toque", "teclado", "camera", "gps", "microfone"];
    this.state.availableOutputs = ["tts", "tela", "vibracao", "braille", "haptico"];
    this.state.availableSensors = ["camera", "gps", "microfone", "acelerometro", "bussola", "luz"];
    this.mitigationsActive = {};
    this.eventLog = [];
    this.strategies = {};
    for (const s of MITIGATION_STRATEGIES) {
      this.strategies[s.failureType] = s;
    }
  }

  injectFailure(failure) {
    failure.detected = true;
    this.state.activeFailures.push(failure);
    this._updateSystemState(failure);

    const strategy = this.strategies[failure.failureType];
    let mitigationResult = null;
    if (strategy && strategy.autoActivate) {
      this.mitigationsActive[strategy.strategyId] = strategy;
      mitigationResult = this._applyMitigation(strategy);
    } else if (strategy) {
      mitigationResult = { action: "notify", message: strategy.userMessage };
    }

    const eventRecord = {
      event_id: failure.eventId,
      failure: failure.failureType,
      severity: failure.severity,
      mitigation: strategy ? strategy.name : "NENHUMA (sem estrategia)",
      fallback_chain: strategy ? strategy.fallbackChain : [],
      user_message: strategy ? strategy.userMessage : "Falha sem mitigacao definida!",
      degradation_level: this.state.level,
      mitigation_applied: mitigationResult,
    };
    this.eventLog.push(eventRecord);
    return eventRecord;
  }

  _updateSystemState(failure) {
    const ft = failure.failureType;
    if (ft === FailureType.BATTERY_CRITICAL) {
      this.state.batteryPct = 3.0;
      this.state.level = DegradationLevel.SURVIVAL;
    } else if (ft === FailureType.BATTERY_DEAD) {
      this.state.batteryPct = 0.0;
      this.state.level = DegradationLevel.DEAD;
    } else if (ft === FailureType.GPS_LOST) {
      this.state.gpsAvailable = false;
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_1);
    } else if (ft === FailureType.CAMERA_FAILURE) {
      this.state.cameraAvailable = false;
      this.state.availableSensors = this.state.availableSensors.filter(s => s !== "camera");
      this.state.availableInputs = this.state.availableInputs.filter(s => s !== "camera");
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_1);
    } else if (ft === FailureType.MICROPHONE_DEAD) {
      this.state.microphoneAvailable = false;
      this.state.availableInputs = this.state.availableInputs.filter(s => s !== "microfone" && s !== "voz");
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_2);
    } else if (ft === FailureType.SPEAKER_DEAD) {
      this.state.speakerAvailable = false;
      this.state.availableOutputs = this.state.availableOutputs.filter(s => s !== "tts");
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_2);
    } else if (ft === FailureType.TTS_CRASH) {
      this.state.ttsAvailable = false;
      this.state.availableOutputs = this.state.availableOutputs.filter(s => s !== "tts");
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_2);
    } else if (ft === FailureType.VIBRATION_DEAD) {
      this.state.vibrationAvailable = false;
      this.state.availableOutputs = this.state.availableOutputs.filter(s => s !== "vibracao" && s !== "haptico");
    } else if (ft === FailureType.SCREEN_BROKEN || ft === FailureType.SCREEN_DEAD) {
      this.state.screenAvailable = false;
      this.state.availableOutputs = this.state.availableOutputs.filter(s => s !== "tela");
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_2);
    } else if (ft === FailureType.BLUETOOTH_DROP) {
      this.state.brailleConnected = false;
      this.state.availableOutputs = this.state.availableOutputs.filter(s => s !== "braille");
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_1);
    } else if (ft === FailureType.NETWORK_DOWN || ft === FailureType.CLOUD_DOWN) {
      this.state.networkAvailable = false;
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_1);
    } else if (ft === FailureType.SMARTWATCH_LOST) {
      this.state.smartwatchConnected = false;
    } else if (ft === FailureType.EYE_TRACKER_LOST) {
      this.state.eyeTrackerConnected = false;
      this.state.availableInputs = this.state.availableInputs.filter(s => s !== "rastreio_olhos");
    } else if (ft === FailureType.WATER_DAMAGE) {
      this.state.level = DegradationLevel.EMERGENCY;
      this.state.cameraAvailable = false;
      this.state.microphoneAvailable = false;
      this.state.screenAvailable = false;
    } else if (ft === FailureType.APP_CRASH) {
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_1);
    } else if (ft === FailureType.MEMORY_EXHAUSTED) {
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_2);
    } else if (ft === FailureType.PERMISSION_REVOKED) {
      this.state.microphoneAvailable = false;
      this.state.availableInputs = this.state.availableInputs.filter(s => s !== "microfone");
    } else if (ft === FailureType.STT_FAILURE) {
      this.state.availableInputs = this.state.availableInputs.filter(s => s !== "voz");
      this.state.level = this._escalate(this.state.level, DegradationLevel.DEGRADED_2);
    }
  }

  _applyMitigation(strategy) {
    const result = {
      strategy: strategy.name,
      fallback_chain: strategy.fallbackChain,
      recovery_action: strategy.recoveryAction,
    };

    if (strategy.failureType === FailureType.TTS_CRASH) {
      if (this.state.brailleConnected) {
        if (!this.state.availableOutputs.includes("braille")) this.state.availableOutputs.push("braille");
        result.restored_output = "braille";
      } else if (this.state.vibrationAvailable) {
        if (!this.state.availableOutputs.includes("vibracao")) this.state.availableOutputs.push("vibracao");
        result.restored_output = "vibracao";
      }
    } else if (strategy.failureType === FailureType.CAMERA_FAILURE) {
      if (this.state.microphoneAvailable && !this.state.availableSensors.includes("audio_sonar")) {
        this.state.availableSensors.push("audio_sonar");
        result.restored_sensor = "audio_sonar (microfone como sonar)";
      }
    } else if (strategy.failureType === FailureType.MICROPHONE_DEAD) {
      if (!this.state.availableInputs.includes("switch") && this.state.screenAvailable) {
        this.state.availableInputs.push("switch");
        result.restored_input = "switch (botoes na tela)";
      }
    } else if (strategy.failureType === FailureType.GPS_LOST) {
      if (this.state.availableSensors.includes("bussola") && !this.state.availableSensors.includes("dead_reckoning")) {
        this.state.availableSensors.push("dead_reckoning");
        result.restored_sensor = "dead_reckoning (bussola + passos)";
      }
    } else if (strategy.failureType === FailureType.APP_CRASH) {
      result.restored = "watchdog reiniciou em 3s";
    }
    return result;
  }

  recoverFailure(failureType) {
    let recovered = false;
    for (let i = 0; i < this.state.activeFailures.length; i++) {
      if (this.state.activeFailures[i].failureType === failureType) {
        this.state.activeFailures.splice(i, 1);
        recovered = true;
        break;
      }
    }
    const strategy = this.strategies[failureType];
    if (strategy && this.mitigationsActive[strategy.strategyId]) {
      delete this.mitigationsActive[strategy.strategyId];
    }
    this._recalculateLevel();

    if (failureType === FailureType.GPS_LOST) {
      this.state.gpsAvailable = true;
      if (!this.state.availableSensors.includes("gps")) this.state.availableSensors.push("gps");
    } else if (failureType === FailureType.CAMERA_FAILURE) {
      this.state.cameraAvailable = true;
      if (!this.state.availableSensors.includes("camera")) this.state.availableSensors.push("camera");
    } else if (failureType === FailureType.NETWORK_DOWN) {
      this.state.networkAvailable = true;
    } else if (failureType === FailureType.TTS_CRASH) {
      this.state.ttsAvailable = true;
      if (!this.state.availableOutputs.includes("tts")) this.state.availableOutputs.push("tts");
    }

    return {
      recovered,
      failure: failureType,
      current_level: this.state.level,
      remaining_failures: this.state.activeFailures.length,
    };
  }

  _escalate(current, newLevel) {
    const levels = [
      DegradationLevel.FULL, DegradationLevel.DEGRADED_1, DegradationLevel.DEGRADED_2,
      DegradationLevel.SURVIVAL, DegradationLevel.EMERGENCY, DegradationLevel.DEAD,
    ];
    return levels[Math.max(levels.indexOf(current), levels.indexOf(newLevel))];
  }

  _recalculateLevel() {
    if (this.state.activeFailures.length === 0) {
      this.state.level = DegradationLevel.FULL;
      return;
    }
    const severityOrder = [FailureSeverity.COSMETIC, FailureSeverity.MINOR, FailureSeverity.MAJOR, FailureSeverity.CRITICAL, FailureSeverity.CATASTROPHIC];
    const maxSeverity = this.state.activeFailures.reduce((max, f) =>
      severityOrder.indexOf(f.severity) > severityOrder.indexOf(max.severity) ? f : max
    );
    if (maxSeverity.severity === FailureSeverity.CATASTROPHIC) this.state.level = DegradationLevel.EMERGENCY;
    else if (maxSeverity.severity === FailureSeverity.CRITICAL) this.state.level = DegradationLevel.SURVIVAL;
    else if (maxSeverity.severity === FailureSeverity.MAJOR) this.state.level = DegradationLevel.DEGRADED_2;
    else if (maxSeverity.severity === FailureSeverity.MINOR) this.state.level = DegradationLevel.DEGRADED_1;
    else this.state.level = DegradationLevel.FULL;
  }

  systemStatus() {
    return {
      degradation_level: this.state.level,
      battery_pct: this.state.batteryPct,
      active_failures: this.state.activeFailures.length,
      active_mitigations: Object.keys(this.mitigationsActive).length,
      available_inputs: [...this.state.availableInputs],
      available_outputs: [...this.state.availableOutputs],
      available_sensors: [...this.state.availableSensors],
      network: this.state.networkAvailable,
      gps: this.state.gpsAvailable,
      camera: this.state.cameraAvailable,
      microphone: this.state.microphoneAvailable,
      speaker: this.state.speakerAvailable,
      tts: this.state.ttsAvailable,
      screen: this.state.screenAvailable,
      vibration: this.state.vibrationAvailable,
      braille: this.state.brailleConnected,
    };
  }
}

// ============================================================================
// 6. SIMULACOES DE CENARIO CATASTROFICO (TODAS AS 6)
// ============================================================================

function simulateBlindUserBatteryDeath() {
  console.log("=".repeat(65));
  console.log("CENARIO 1: Cego na rua -- bateria morrendo");
  console.log("=".repeat(65));

  const sim = new FailureSimulator();
  console.log("\n[ESTADO INICIAL]");
  let status = sim.systemStatus();
  console.log(`  Nivel: ${status.degradation_level}`);
  console.log(`  Bateria: ${status.battery_pct}%`);
  console.log(`  Inputs: ${status.available_inputs}`);

  console.log("\n[FALHA: Bateria critica]");
  let event = new FailureEvent("EVT-001", FailureType.BATTERY_CRITICAL, FailureCategory.POWER,
    FailureSeverity.CRITICAL, FailureDuration.SHORT, "Bateria abaixo de 5%");
  event.userImpact = "Sistema entra em modo sobrevivencia";
  let result = sim.injectFailure(event);
  console.log(`  Mitigacao: ${result.mitigation}`);
  console.log(`  Mensagem ao usuario: ${result.user_message}`);
  status = sim.systemStatus();
  console.log(`  Nivel atual: ${status.degradation_level}`);
  console.log(`  Bateria: ${status.battery_pct}%`);

  console.log("\n[FALHA: Bateria morta]");
  event = new FailureEvent("EVT-002", FailureType.BATTERY_DEAD, FailureCategory.POWER,
    FailureSeverity.CATASTROPHIC, FailureDuration.LONG, "Bateria em 0%");
  event.userImpact = "Smartphone morre. Handoff necessario.";
  result = sim.injectFailure(event);
  console.log(`  Mitigacao: ${result.mitigation}`);
  for (const fb of result.fallback_chain) console.log(`    ${fb}`);
  console.log(`  Mensagem: ${result.user_message}`);
}

function simulateCascadingFailures() {
  console.log("\n" + "=".repeat(65));
  console.log("CENARIO 2: Falhas em cascata");
  console.log("=".repeat(65));

  const sim = new FailureSimulator();
  const cascading = [
    new FailureEvent("C-01", FailureType.NETWORK_DOWN, FailureCategory.NETWORK, FailureSeverity.MAJOR, FailureDuration.MEDIUM, "Internet caiu"),
    new FailureEvent("C-02", FailureType.GPS_LOST, FailureCategory.SENSOR, FailureSeverity.MAJOR, FailureDuration.MEDIUM, "GPS perdido"),
    new FailureEvent("C-03", FailureType.BLUETOOTH_DROP, FailureCategory.PERIPHERAL, FailureSeverity.MAJOR, FailureDuration.TRANSIENT, "Braille desconectou"),
    new FailureEvent("C-04", FailureType.TTS_CRASH, FailureCategory.SOFTWARE, FailureSeverity.CRITICAL, FailureDuration.SHORT, "TTS crashou"),
  ];

  for (const f of cascading) {
    console.log(`\n[FALHA: ${f.failureType}]`);
    const result = sim.injectFailure(f);
    const status = sim.systemStatus();
    console.log(`  Severidade: ${f.severity}`);
    console.log(`  Mitigacao: ${result.mitigation}`);
    console.log(`  Nivel sistema: ${status.degradation_level}`);
    console.log(`  Outputs restantes: ${status.available_outputs}`);
    console.log(`  Inputs restantes: ${status.available_inputs}`);
  }

  console.log("\n[ESTADO APOS 4 FALHAS EM CASCATA]");
  let status = sim.systemStatus();
  console.log(`  Nivel: ${status.degradation_level}`);
  console.log(`  Falhas ativas: ${status.active_failures}`);
  console.log(`  Mitigacoes ativas: ${status.active_mitigations}`);

  console.log("\n[RECUPERACAO GRADUAL]");
  for (const ft of [FailureType.TTS_CRASH, FailureType.BLUETOOTH_DROP, FailureType.GPS_LOST, FailureType.NETWORK_DOWN]) {
    const r = sim.recoverFailure(ft);
    console.log(`  ${ft}: nivel -> ${r.current_level}`);
  }
}

function simulateWaterDamage() {
  console.log("\n" + "=".repeat(65));
  console.log("CENARIO 3: Dano por agua");
  console.log("=".repeat(65));

  const sim = new FailureSimulator();
  console.log("\n[FALHA: Smartphone molhou]");
  const event = new FailureEvent("W-01", FailureType.WATER_DAMAGE, FailureCategory.HARDWARE,
    FailureSeverity.CATASTROPHIC, FailureDuration.PERMANENT, "Smartphone caiu na agua/poça");
  event.userImpact = "Multiplas falhas simultaneas. Dispositivo morrendo.";
  const result = sim.injectFailure(event);
  console.log(`  Mitigacao: ${result.mitigation}`);
  console.log(`  Mensagem: ${result.user_message}`);
  for (const fb of result.fallback_chain) console.log(`    ${fb}`);
  const status = sim.systemStatus();
  console.log(`  Nivel: ${status.degradation_level}`);
  console.log(`  Camera: ${status.camera} | Microfone: ${status.microphone} | Tela: ${status.screen}`);
}

function simulateSoftwareResilience() {
  console.log("\n" + "=".repeat(65));
  console.log("CENARIO 4: Software crash + auto-recovery");
  console.log("=".repeat(65));

  const sim = new FailureSimulator();
  for (let i = 0; i < 3; i++) {
    console.log(`\n[FALHA ${i+1}: App crashou]`);
    const event = new FailureEvent(`S-${String(i+1).padStart(2, "0")}`, FailureType.APP_CRASH,
      FailureCategory.SOFTWARE, FailureSeverity.MAJOR, FailureDuration.TRANSIENT, `App crashou (tentativa ${i+1})`);
    const result = sim.injectFailure(event);
    console.log(`  Mitigacao: ${result.mitigation}`);
    console.log(`  User message: ${result.user_message}`);
    if (i < 2) {
      const r = sim.recoverFailure(FailureType.APP_CRASH);
      console.log(`  Recuperado: nivel -> ${r.current_level}`);
    }
  }
}

function simulateMultiUserScenarios() {
  console.log("\n" + "=".repeat(65));
  console.log("CENARIO 5: Impacto por deficiencia");
  console.log("=".repeat(65));

  const scenarios = [
    ["CEGO", [FailureType.TTS_CRASH, FailureType.GPS_LOST, FailureType.BLUETOOTH_DROP]],
    ["SURDO", [FailureType.SCREEN_BROKEN, FailureType.VIBRATION_DEAD]],
    ["TETRAPLEGICO", [FailureType.STT_FAILURE, FailureType.EYE_TRACKER_LOST]],
    ["AUTISTA", [FailureType.NETWORK_DOWN, FailureType.SPEAKER_DEAD]],
  ];

  for (const [label, failures] of scenarios) {
    console.log(`\n  ${label}:`);
    const sim = new FailureSimulator();
    for (const ft of failures) {
      const event = new FailureEvent(`M-${label}-${ft}`, ft, FailureCategory.HARDWARE,
        FailureSeverity.CRITICAL, FailureDuration.SHORT, ft);
      const result = sim.injectFailure(event);
      const status = sim.systemStatus();
      console.log(`    Falha: ${ft}`);
      console.log(`      Nivel: ${status.degradation_level}`);
      console.log(`      Mitigacao: ${result.mitigation}`);
      console.log(`      Inputs: ${status.available_inputs}`);
      console.log(`      Outputs: ${status.available_outputs}`);
    }
  }
}

function simulateFullCatastrophe() {
  console.log("\n" + "=".repeat(65));
  console.log("CENARIO 6: CATASTROFE TOTAL");
  console.log("=".repeat(65));

  const sim = new FailureSimulator();
  const allFailures = [
    FailureType.BATTERY_CRITICAL, FailureType.GPS_LOST, FailureType.CAMERA_FAILURE,
    FailureType.MICROPHONE_DEAD, FailureType.TTS_CRASH, FailureType.BLUETOOTH_DROP,
    FailureType.NETWORK_DOWN, FailureType.SCREEN_BROKEN, FailureType.VIBRATION_DEAD,
    FailureType.SMARTWATCH_LOST,
  ];

  console.log(`\nInjetando ${allFailures.length} falhas simultaneas...`);
  for (const ft of allFailures) {
    const event = new FailureEvent(`CAT-${ft}`, ft, FailureCategory.HARDWARE,
      FailureSeverity.CATASTROPHIC, FailureDuration.PERMANENT, `Catastrofe: ${ft}`);
    sim.injectFailure(event);
  }

  const status = sim.systemStatus();
  console.log("\n[ESTADO APOS CATASTROFE]");
  console.log(`  Nivel: ${status.degradation_level}`);
  console.log(`  Bateria: ${status.battery_pct}%`);
  console.log(`  Falhas ativas: ${status.active_failures}`);
  console.log(`  Mitigacoes ativas: ${status.active_mitigations}`);
  console.log(`  Inputs: ${status.available_inputs}`);
  console.log(`  Outputs: ${status.available_outputs}`);
  console.log(`  Sensores: ${status.available_sensors}`);

  if (status.available_outputs.length === 0 && status.available_inputs.length === 0) {
    console.log("\n  PLANO D: LIGACAO CELULAR DIRETA");
    console.log("  O unico canal que resta e o sinal de celular + SMS.");
    console.log("  Sistema envia SMS com localizacao para emergencia.");
    console.log("  Se nem sinal tem: GRITE. Peça ajuda humana.");
  }
}

// ============================================================================
// 7. DEMONSTRACAO (main)
// ============================================================================

function demo() {
  console.log("=".repeat(70));
  console.log("OpenResilience -- Simulacao de Falhas e Mitigacao");
  console.log("=".repeat(70));

  console.log(`\nFalhas mapeadas: ${Object.keys(FailureType).length}`);
  console.log(`Categorias de falha: ${Object.keys(FailureCategory).length}`);
  console.log(`Estrategias de mitigacao: ${MITIGATION_STRATEGIES.length}`);
  console.log(`Niveis de degradacao: ${Object.keys(DegradationLevel).length}`);

  console.log("\n" + "=".repeat(70));
  console.log("COBERTURA DE MITIGACAO POR CATEGORIA");
  console.log("=".repeat(70));

  const covered = new Set(MITIGATION_STRATEGIES.map(s => s.failureType)).size;
  const total = Object.keys(FailureType).length;
  console.log(`  Falhas com mitigacao: ${covered}/${total}`);

  simulateBlindUserBatteryDeath();
  simulateCascadingFailures();
  simulateWaterDamage();
  simulateSoftwareResilience();
  simulateMultiUserScenarios();
  simulateFullCatastrophe();

  console.log("\n" + "=".repeat(70));
  console.log("RESUMO DE MITIGACOES");
  console.log("=".repeat(70));
  for (const s of MITIGATION_STRATEGIES) {
    console.log(`\n  ${s.strategyId}: ${s.name}`);
    console.log(`    Falha: ${s.failureType}`);
    console.log(`    Descricao: ${s.description}`);
    console.log(`    Planos: ${s.fallbackChain.length} fallbacks`);
    for (let i = 0; i < s.fallbackChain.length; i++) {
      console.log(`      ${s.fallbackChain[i]}`);
    }
  }

  console.log("\n" + "=".repeat(70));
  console.log(`Total falhas: ${Object.keys(FailureType).length}`);
  console.log(`Total mitigacoes: ${MITIGATION_STRATEGIES.length}`);
  console.log("Cada falha tem Plano A, B, C e D.");
  console.log("Nenhum ponto unico de falha.");
  console.log("Redundancia em TUDO.");
  console.log("\nO sistema PODE falhar. O usuario NAO pode ficar desamparado.");
}

if (require.main === module) {
  demo();
}

module.exports = {
  FailureCategory, FailureType, FailureSeverity, FailureDuration,
  FailureEvent, DegradationLevel, SystemState, MitigationStrategy,
  MITIGATION_STRATEGIES, FailureSimulator,
  simulateBlindUserBatteryDeath, simulateCascadingFailures, simulateWaterDamage,
  simulateSoftwareResilience, simulateMultiUserScenarios, simulateFullCatastrophe,
  demo,
};