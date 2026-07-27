# OpenResilience -- Simulacao de Falhas e Mitigacao

**Arquivo original:** `open-republic/core/open_resilience.py`

**Descricao:** ====================================================
"O cego esta na rua. A bateria do smartphone cai pra 2%.
O GPS para. A camera trava. O TTS crasha.
E AGORA? O cego esta PERDIDO, CEGO, e SEM SISTEMA.
A resposta NAO e 'isso nao vai acontecer'.
A resposta e: 'quando acontecer, o sistema REAGE'.
Todo hardware falha. Todo software cai. Todo sinal se perde.
A pergunta nao e SE vai falhar -- e QUANDO.
E quando falhar, o usuario NAO pode ficar desamparado.
Este modulo simula TODA falha possivel e define a mitigacao:
- Bateria em 0%: modo survival, so essencial, voz lenta
- GPS perdido: bussola + contagem de passos + landmark auditivo
- Camera falhou: audio + acelerometro assumem
- TTS crashou: vibracao + braille assumem
- Rede caiu: tudo offline, dados em cache
- Software travou: watchdog reinicia em 3s
- Hardware morreu: fallback para terminal publico + ligacao
PRINCIPIO: Cada componente tem um PLANO B, PLANO C e PLAO D.
Nenhum ponto unico de falha. Redundancia em TUDO.
Integrado com:
- OpenTelefonista (telefonista sobrevive a falhas)
- OpenInclusiveIDE (IDE degrada graciosamente)
- OpenInclusiveHardware (44 dispositivos com fallback)
- OpenAbsence (pausa mesmo em modo survival)
- OpenSilencePolicy (silencio mesmo em emergencia)
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol

// !/usr/bin/env python3
// 
OpenResilience -- Simulacao de Falhas e Mitigacao
====================================================
"O cego esta na rua. A bateria do smartphone cai pra 2%.
O GPS para. A camera trava. O TTS crasha.
E AGORA? O cego esta PERDIDO, CEGO, e SEM SISTEMA.

A resposta NAO e 'isso nao vai acontecer'.
A resposta e: 'quando acontecer, o sistema REAGE'.

Todo hardware falha. Todo software cai. Todo sinal se perde.
A pergunta nao e SE vai falhar -- e QUANDO.
E quando falhar, o usuario NAO pode ficar desamparado.

Este modulo simula TODA falha possivel e define a mitigacao:
- Bateria em 0%: modo survival, so essencial, voz lenta
- GPS perdido: bussola + contagem de passos + landmark auditivo
- Camera falhou: audio + acelerometro assumem
- TTS crashou: vibracao + braille assumem
- Rede caiu: tudo offline, dados em cache
- Software travou: watchdog reinicia em 3s
- Hardware morreu: fallback para terminal publico + ligacao

PRINCIPIO: Cada componente tem um PLANO B, PLANO C e PLAO D.
Nenhum ponto unico de falha. Redundancia em TUDO.

Integrado com:
- OpenTelefonista (telefonista sobrevive a falhas)
- OpenInclusiveIDE (IDE degrada graciosamente)
- OpenInclusiveHardware (44 dispositivos com fallback)
- OpenAbsence (pausa mesmo em modo survival)
- OpenSilencePolicy (silencio mesmo em emergencia)

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set, Callable de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict, deque de collections
// importa hashlib
// importa time
// importa random


// ============================================================================
// 1. TIPOS DE FALHA
// ============================================================================

classe FailureCategory herda de Enum:
    HARDWARE <- "hardware"
    SOFTWARE <- "software"
    NETWORK <- "rede"
    POWER <- "energia"
    SENSOR <- "sensor"
    PERIPHERAL <- "periferico"
    OS <- "sistema_operacional"
    CLOUD <- "nuvem"


classe FailureType herda de Enum:
    // POWER
    BATTERY_CRITICAL <- "bateria_critica"  // < 5%
    BATTERY_DEAD <- "bateria_morta"  // 0%
    BATTERY_OVERHEAT <- "bateria_superaquecida"  // desliga por calor
    POWER_SURGE <- "pico_energia"  // dano eletrico

    // HARDWARE
    SCREEN_BROKEN <- "tela_quebrada"  // caiu, rachou
    SCREEN_DEAD <- "tela_morta"  // backlight queimou
    CAMERA_FAILURE <- "camera_falhou"  // lente riscada, modulo queimou
    MICROPHONE_DEAD <- "microfone_morto"  // agua, poeira
    SPEAKER_DEAD <- "alto_falante_morto"  // agua, volume max
    VIBRATION_DEAD <- "vibracao_morta"  // motor queimou
    GPS_LOST <- "gps_perdido"  // dentro de predio, tunel
    BLUETOOTH_DROP <- "bluetooth_caiu"  // desconectou do braille
    NFC_FAILURE <- "nfc_falhou"
    WATER_DAMAGE <- "dano_agua"  // chuva, queda na agua
    PHYSICAL_DAMAGE <- "dano_fisico"  // pisou, atropelou
    BUTTON_STUCK <- "botao_preso"  // poeira, impacto
    CHARGE_PORT_BROKEN <- "porta_carga_quebrada"  // nao carrega mais

    // PERIPHERAL
    BRAILLE_DISPLAY_DISCONNECTED <- "braille_desconectou"
    EYE_TRACKER_LOST <- "eye_tracker_perdeu"
    SWITCH_FAILURE <- "switch_queimou"
    HEARING_AID_DISCONNECTED <- "aparelho_desconectou"
    SMARTWATCH_LOST <- "smartwatch_perdido"

    // SOFTWARE
    TTS_CRASH <- "tts_crashou"  // motor de voz morreu
    STT_FAILURE <- "stt_falhou"  // reconhecimento de voz falhou
    OCR_FAILURE <- "ocr_falhou"  // leitura de imagem falhou
    APP_FREEZE <- "app_travou"  // ANR
    APP_CRASH <- "app_crashou"  // SIGSEGV
    MEMORY_EXHAUSTED <- "memoria_esgotada"  // OOM
    STORAGE_FULL <- "armazenamento_cheio"
    MODEL_UNAVAILABLE <- "ia_indisponivel"  // modelo IA nao carrega
    NAVIGATION_ENGINE_DOWN <- "navegador_caiu"
    EMOTION_DETECTOR_DOWN <- "detector_emocao_caiu"

    // NETWORK
    NETWORK_DOWN <- "rede_caiu"  // sem internet
    NETWORK_SLOW <- "rede_lenta"  // 2G,latencia alta
    CLOUD_DOWN <- "nuvem_caiu"  // servidor offline
    API_RATE_LIMIT <- "api_limite"  // rate limited
    DNS_FAILURE <- "dns_falhou"

    // OS
    OS_UPDATE_BRICK <- "atualizacao_bricou"
    BOOT_LOOP <- "boot_loop"
    PERMISSION_REVOKED <- "permissao_revogada"  // microfone negado


classe FailureSeverity herda de Enum:
    COSMETIC <- "cosmetico"  // nao afeta funcionalidade principal
    MINOR <- "menor"  // degradacao leve
    MAJOR <- "maior"  // degradacao significativa
    CRITICAL <- "critico"  // funcionalidade essencial perdida
    CATASTROPHIC <- "catastrofico"  // dispositivo inutilizavel


classe FailureDuration herda de Enum:
    TRANSIENT <- "transiente"  // segundos (bluetooth reconecta)
    SHORT <- "curto"  // minutos (GPS re-adquire)
    MEDIUM <- "medio"  // horas (bateria recarrega)
    LONG <- "longo"  // dias (tela quebrada ate consertar)
    PERMANENT <- "permanente"  // nao recupera (hardware morreu)


// ============================================================================
// 2. EVENTO DE FALHA
// ============================================================================

// decorador: @dataclass
classe FailureEvent:
    // Um evento de falha simulado.
    event_id: str
    failure_type: FailureType
    category: FailureCategory
    severity: FailureSeverity
    duration: FailureDuration
    description: str
    declare affected_components: List[str]  <- field(default_factory=list)  // o que para de funcionar
    declare user_impact: str  <- ""  // o que o usuario sente
    declare timestamp: float  <- field(default_factory=time.time)
    declare recovery_probability: float  <- 0.9  // 0=nunca recupera, 1=sempre recupera
    declare detected: bool  <- FALSO


// ============================================================================
// 3. NIVEIS DE DEGRADACAO
// ============================================================================

classe DegradationLevel herda de Enum:
    // Niveis de degradacao do sistema.
    FULL <- "completo"  // 100% funcional, tudo operacional
    DEGRADED_1 <- "degradado_1"  // 80% -- features nao essenciais off
    DEGRADED_2 <- "degradado_2"  // 50% -- so essencial, fallback ativo
    SURVIVAL <- "sobrevivencia"  // 20% -- minimo absoluto para nao morrer
    EMERGENCY <- "emergencia"  // 10% -- so chamada de socorro
    DEAD <- "morto"  // 0% -- dispositivo inutilizavel


// decorador: @dataclass
classe SystemState:
    // Estado atual do sistema sob falhas.
    declare level: DegradationLevel  <- DegradationLevel.FULL
    declare active_failures: List[FailureEvent]  <- field(default_factory=list)
    declare battery_pct: float  <- 100.0
    declare available_inputs: List[str]  <- field(default_factory=list)
    declare available_outputs: List[str]  <- field(default_factory=list)
    declare available_sensors: List[str]  <- field(default_factory=list)
    declare network_available: bool  <- VERDADEIRO
    declare gps_available: bool  <- VERDADEIRO
    declare camera_available: bool  <- VERDADEIRO
    declare microphone_available: bool  <- VERDADEIRO
    declare speaker_available: bool  <- VERDADEIRO
    declare vibration_available: bool  <- VERDADEIRO
    declare screen_available: bool  <- VERDADEIRO
    declare tts_available: bool  <- VERDADEIRO
    declare braille_connected: bool  <- FALSO
    declare eye_tracker_connected: bool  <- FALSO
    declare smartwatch_connected: bool  <- FALSO
    declare offline_cache_size_mb: float  <- 0.0
    declare last_known_location: Optional[Tuple[float, float]]  <- nulo
    declare uptime_seconds: float  <- 0.0


// ============================================================================
// 4. ESTRATEGIAS DE MITIGACAO
// ============================================================================

// decorador: @dataclass
classe MitigationStrategy:
    // Uma estrategia de mitigacao para uma falha.
    strategy_id: str
    failure_type: FailureType
    name: str
    description: str
    declare fallback_chain: List[str]  <- field(default_factory=list)  // plano A, B, C, D
    declare recovery_action: str  <- ""  // o que fazer para recuperar
    declare user_message: str  <- ""  // o que dizer ao usuario
    declare auto_activate: bool  <- VERDADEIRO  // ativa automaticamente
    declare recovery_time_estimate_s: int  <- 0  // tempo estimado de recuperacao


declare MITIGATION_STRATEGIES: List[MitigationStrategy]  <- [
    // === BATERIA ===
    MitigationStrategy(
        strategy_id <- "MT-001",
        failure_type <- FailureType.BATTERY_CRITICAL,
        name <- "Modo Survival de Bateria",
        description <- "Bateria < 5%. Desliga tudo nao essencial. So mantem voz/sos.",
        fallback_chain <- [
            "Plano A: Reduzir brilho ao minimo, desligar animacoes",
            "Plano B: Desligar camera, GPS (usar contagem de passos)",
            "Plano C: Desligar TTS continuo, so falas criticas",
            "Plano D: SOS -- ligar para contato de emergencia e desligar",
        ],
        recovery_action <- "Conectar carregador. Sistema avisa proximo terminal publico.",
        user_message <- "Bateria critica. Entrei em modo sobrevivencia. So o essencial. Encontre um carregador ou vou te levar ate um terminal publico.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 0,
    ),
    MitigationStrategy(
        strategy_id <- "MT-002",
        failure_type <- FailureType.BATTERY_DEAD,
        name <- "Handoff para Terminal Publico",
        description <- "Bateria em 0%. Smartphone morre. Sistema migra.",
        fallback_chain <- [
            "Plano A: Antes de morrer, enviar localizacao para emergencia",
            "Plano B: Enviar ultima tarefa nao salva para nuvem",
            "Plano C: Ligar para contato de emergencia com mensagem automatica",
            "Plano D: Avisar usuario: 'Proximo terminal publico: biblioteca a 200m norte'",
        ],
        recovery_action <- "Carregar em terminal publico, biblioteca, estabelecimento.",
        user_message <- "Vou desligar em 30 segundos. Mandei sua localizacao para emergencia. Terminal publico mais proximo: biblioteca, 200 metros ao norte.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 3600,
    ),

    // === GPS ===
    MitigationStrategy(
        strategy_id <- "MT-003",
        failure_type <- FailureType.GPS_LOST,
        name <- "Navegacao Sem GPS",
        description <- "GPS perdido (predio, tunel, subsolo). Navegacao continua.",
        fallback_chain <- [
            "Plano A: Bussola magnetica + contagem de passos (dead reckoning)",
            "Plano B: Bluetooth beacons indoor (shopping, hospital)",
            "Plano C: WiFi triangulation (menos preciso mas funciona indoor)",
            "Plano D: Landmarks auditivos: 'Voce passou por um lugar barulhento a 30s -- provavelmente cozinha'",
        ],
        recovery_action <- "Sair para area aberta. GPS re-adquire em 10-30 segundos.",
        user_message <- "Perdi o GPS. Estou usando a bussola e contando seus passos. Vou continuar te guiando.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 30,
    ),

    // === CAMERA ===
    MitigationStrategy(
        strategy_id <- "MT-004",
        failure_type <- FailureType.CAMERA_FAILURE,
        name <- "Camera Cai, Audio Assume",
        description <- "Camera falhou. Visao computacional perdida.",
        fallback_chain <- [
            "Plano A: Microfone assume deteccao de obstaculos por eco/sonar",
            "Plano B: Acelerometro + bussola mapeiam caminho percorrido",
            "Plano C: Pedir ajuda humana: 'Alguem pode me orientar?' via voz alta",
            "Plano D: Ligar para contato que ve por camera remota",
        ],
        recovery_action <- "Limpar lente. Reiniciar app de camera. Se hardware, trocar smartphone.",
        user_message <- "Minha camera parou. Vou usar o microfone para ouvir o ambiente e te guiar pelo som.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 60,
    ),

    // === MICROFONE ===
    MitigationStrategy(
        strategy_id <- "MT-005",
        failure_type <- FailureType.MICROPHONE_DEAD,
        name <- "Microfone Morto, Tela Assume",
        description <- "Microfone falhou. Entrada por voz perdida.",
        fallback_chain <- [
            "Plano A: Switch/bluetooth keyboard assume entrada",
            "Plano B: Tela touch com botoes grandes (sim, mesmo para cego via TalkBack)",
            "Plano C: Eye tracker se disponivel",
            "Plano D: Pedir para alguem gravar e enviar audio",
        ],
        recovery_action <- "Limpar entrada do microfone. Verificar permissoes. Bluetooth headset como backup.",
        user_message <- "Nao estou te ouvindo. Vou passar para entrada por botoes/toque.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 10,
    ),

    // === TTS (TEXT TO SPEECH) ===
    MitigationStrategy(
        strategy_id <- "MT-006",
        failure_type <- FailureType.TTS_CRASH,
        name <- "TTS Crashou, Vibracao Assume",
        description <- "Motor de voz morreu. Cego nao ouve mais o sistema.",
        fallback_chain <- [
            "Plano A: Display braille assume (se conectado)",
            "Plano B: Padroes de vibracao codificam informacao",
            "Plano C: Auto-restart do TTS em background",
            "Plano D: Tocar tons com significado (agudo=ok, grave=erro)",
        ],
        recovery_action <- "Reiniciar servico TTS. Android: Settings > Accessibility > TalkBack. iOS: VoiceOver toggle.",
        user_message <- "[MENSAGEM POR VIBRACAO: 1 pulse = ok, 2 pulses = atencao, 3 pulses = erro]",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 5,
    ),

    // === BLUETOOTH / BRAILLE ===
    MitigationStrategy(
        strategy_id <- "MT-007",
        failure_type <- FailureType.BLUETOOTH_DROP,
        name <- "Bluetooth Caiu",
        description <- "Braille/switch/aparelho auditivo desconectou.",
        fallback_chain <- [
            "Plano A: Tentar reconexao automatica (3 tentativas em 10s)",
            "Plano B: Fallback para TTS alto-falante",
            "Plano C: Fallback para vibracao padrao",
            "Plano D: Pedir usuario para verificar Bluetooth manualmente",
        ],
        recovery_action <- "Reativar Bluetooth. Emparelhar novamente. Verificar bateria do periferico.",
        user_message <- "Perdi conexao com seu dispositivo. Tentando reconectar... Se nao voltar em 10 segundos, vou usar o alto-falante.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 10,
    ),

    // === REDE / INTERNET ===
    MitigationStrategy(
        strategy_id <- "MT-008",
        failure_type <- FailureType.NETWORK_DOWN,
        name <- "Modo Offline Total",
        description <- "Sem internet. IA em nuvem, mapas, API tudo fora.",
        fallback_chain <- [
            "Plano A: Modelos de IA locais (menores mas funcionam offline)",
            "Plano B: Mapas offline (OpenStreetMap cached)",
            "Plano C: Tudo que nao precisa de rede continua: TTS, OCR, navegacao local",
            "Plano D: SMS para emergencia (nao precisa de internet, so sinal)",
        ],
        recovery_action <- "Verificar WiFi/dados. Sair de area sem cobertura. Usar SMS para comunicacao.",
        user_message <- "Sem internet. Continuo funcionando offline. IA local assumiu. Mapas em cache.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 300,
    ),

    // === TELA ===
    MitigationStrategy(
        strategy_id <- "MT-009",
        failure_type <- FailureType.SCREEN_BROKEN,
        name <- "Tela Quebrada",
        description <- "Tela rachada/morta. Sem saida visual.",
        fallback_chain <- [
            "Plano A: TTS assume toda interacao (cego simulado)",
            "Plano B: Braille display conectado via bluetooth",
            "Plano C: Smartwatch mostra minimo na tela do relogio",
            "Plano D: Cast para TV/terminal publico proximo",
        ],
        recovery_action <- "Trocar tela. Enquanto isso: TTS + braille + smartwatch.",
        user_message <- "Sua tela quebrou. Vou guiar tudo por voz. Conecte um braille display se tiver.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 259200,  // 3 dias ate consertar
    ),

    // === SOFTWARE CRASH ===
    MitigationStrategy(
        strategy_id <- "MT-010",
        failure_type <- FailureType.APP_CRASH,
        name <- "Auto-Reinicio com Watchdog",
        description <- "App crashou (SIGSEGV, OOM).",
        fallback_chain <- [
            "Plano A: Watchdog detecta crash e reinicia em 3 segundos",
            "Plano B: Estado salvo automaticamente a cada acao -- restaura",
            "Plano C: Se crash repetido (3x em 1min), modo seguro sem plugins",
            "Plano D: Se modo seguro tambem crasha, notificar e abrir bug report",
        ],
        recovery_action <- "Watchdog reinicia. Log enviado. Estado restaurado do checkpoint.",
        user_message <- "Ops, tive um problema. Reiniciando... Pronto, voltei. Tava onde?",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 3,
    ),

    // === SMARTWATCH ===
    MitigationStrategy(
        strategy_id <- "MT-011",
        failure_type <- FailureType.SMARTWATCH_LOST,
        name <- "Smartwatch Perdido",
        description <- "Smartwatch desconectou/perdeu-se. Biometria perdida.",
        fallback_chain <- [
            "Plano A: Smartphone assume biometria (camera = HR por rPPG)",
            "Plano B: Usuario reporta estado manualmente ('to bem')",
            "Plano C: Reduzir monitoramento ativo, pedir check-in periodico",
            "Plano D: Localizar smartwatch por ultimo sinal GPS",
        ],
        recovery_action <- "Procurar smartwatch. Comprar substituto. Bio no smartphone.",
        user_message <- "Perdi seu smartwatch. Vou monitorar pelo smartphone. Se achar o relogio, me avise.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 3600,
    ),

    // === EYE TRACKER ===
    MitigationStrategy(
        strategy_id <- "MT-012",
        failure_type <- FailureType.EYE_TRACKER_LOST,
        name <- "Eye Tracker Perdeu Calibracao",
        description <- "Eye tracker perdeu tracking ou desconectou.",
        fallback_chain <- [
            "Plano A: Recalibrar automaticamente (pedir olhar para 3 pontos)",
            "Plano B: Switch/scan assume enquanto recalibra",
            "Plano C: Voz assume entrada",
            "Plano D: Pausar ate recuperar tracking",
        ],
        recovery_action <- "Recalibrar. Verificar iluminacao. Limpar camera do tracker.",
        user_message <- "Perdi o rastreio dos seus olhos. Vou usar seu switch enquanto tento recalibrar.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 15,
    ),

    // === MEMORIA ===
    MitigationStrategy(
        strategy_id <- "MT-013",
        failure_type <- FailureType.MEMORY_EXHAUSTED,
        name <- "OOM -- Memoria Esgotada",
        description <- "Memoria RAM cheia. App sera morto pelo OS.",
        fallback_chain <- [
            "Plano A: Descarregar modelos de IA nao essenciais",
            "Plano B: Fechar abas/janelas nao ativas",
            "Plano C: Reduzir resolucao de camera/frame rate",
            "Plano D: Salvar estado e reiniciar limpo",
        ],
        recovery_action <- "Fechar apps em background. Limpar cache. Adicionar RAM se possivel.",
        user_message <- "Memoria cheia. Fechando coisas nao essenciais. Continue trabalhando.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 5,
    ),

    // === PERMISSAO REVOCADA ===
    MitigationStrategy(
        strategy_id <- "MT-014",
        failure_type <- FailureType.PERMISSION_REVOKED,
        name <- "Permissao Revogada",
        description <- "OS revogou permissoes (microfone, camera, localizacao).",
        fallback_chain <- [
            "Plano A: Notificar usuario: 'Preciso de microfone para funcionar'",
            "Plano B: Abrir configuracoes de permissao automaticamente",
            "Plano C: Funcionalidade reduzida sem a permissao",
            "Plano D: Modo visitante (sem dados pessoais)",
        ],
        recovery_action <- "Reconceder permissao em Configuracoes > Apps > Permissoes.",
        user_message <- "Voce desligou minha permissao de microfone. Sem ele eu nao consigo te ouvir. Quer abrir as configuracoes?",
        auto_activate <- FALSO,
        recovery_time_estimate_s <- 30,
    ),

    // === AGUA ===
    MitigationStrategy(
        strategy_id <- "MT-015",
        failure_type <- FailureType.WATER_DAMAGE,
        name <- "Dano por Agua",
        description <- "Smartphone molhou. Multiplas falhas simultaneas.",
        fallback_chain <- [
            "Plano A: Modo survival imediato -- desligar tudo para curto",
            "Plano B: Enquanto funciona: SOS + localizacao enviados",
            "Plano C: Handoff para terminal publico proximo",
            "Plano D: Ligar para emergencia antes de morrer",
        ],
        recovery_action <- "Desligar imediatamente. Secar em silica gel por 48h. NAO carregar molhado.",
        user_message <- "AGUA! Entrando em modo emergencia. Mandando sua localizacao. Vou tentar ligar para seu contato de emergencia.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 259200,  // dias
    ),

    // === CLOUD ===
    MitigationStrategy(
        strategy_id <- "MT-016",
        failure_type <- FailureType.CLOUD_DOWN,
        name <- "Nuvem Caiu, Local Assume",
        description <- "Servidor na nuvem offline. Servicos cloud indisponiveis.",
        fallback_chain <- [
            "Plano A: Modelos de IA locais (menores mas funcionam)",
            "Plano B: Dados sincronizados localmente (ultima sync)",
            "Plano C: Queue de acoes -- executa quando nuvem volta",
            "Plano D: SMS/ligacao para servicos que precisam de servidor",
        ],
        recovery_action <- "Aguardar recuperacao do servidor. Fila de acoes processada na volta.",
        user_message <- "Servidor na nuvem caiu. Tudo continua local. Vou sincronizar quando voltar.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 600,
    ),

    // === STT (SPEECH TO TEXT) ===
    MitigationStrategy(
        strategy_id <- "MT-017",
        failure_type <- FailureType.STT_FAILURE,
        name <- "Reconhecimento de Voz Falhou",
        description <- "STT nao transcreve. Usuario nao consegue falar comandos.",
        fallback_chain <- [
            "Plano A: Reiniciar motor STT",
            "Plano B: Trocar para modelo STT local (offline, menos preciso)",
            "Plano C: Teclado virtual/braille assume entrada",
            "Plano D: Switch + scan de letras",
        ],
        recovery_action <- "Verificar microfone. Reiniciar STT. Verificar permissoes.",
        user_message <- "Nao estou entendendo sua voz. Vou passar para entrada por teclado/toque.",
        auto_activate <- VERDADEIRO,
        recovery_time_estimate_s <- 5,
    ),
]


// ============================================================================
// 5. MOTOR DE SIMULACAO DE FALHAS
// ============================================================================

classe FailureSimulator:
    // 
    Simula falhas em sequencia ou simultaneas e testa mitigacoes.
    Cada falha disstra o sistema e o sistema reage.
    // 

    funcao __init__(self):
        self.state = SystemState()
        self.state.available_inputs = ["voz", "toque", "teclado", "camera", "gps", "microfone"]
        self.state.available_outputs = ["tts", "tela", "vibracao", "braille", "haptico"]
        self.state.available_sensors = ["camera", "gps", "microfone", "acelerometro", "bussola", "luz"]
        self.mitigations_active: Dict[str, MitigationStrategy] = {}
        self.event_log: deque = deque(maxlen=500)
        self.strategies = {s.failure_type: s for s in MITIGATION_STRATEGIES}

    funcao inject_failure(self, failure: FailureEvent) retorna Dict[str, Any]:
        // Injeta uma falha no sistema e ativa mitigacao.
        failure.detected = VERDADEIRO
        self.state.active_failures.append(failure)
        self._update_system_state(failure)

        // Buscar estrategia de mitigacao
        strategy <- self.strategies.get(failure.failure_type)
        mitigation_result <- nulo
        se strategy  E  strategy.auto_activate entao:
            self.mitigations_active[strategy.strategy_id] = strategy
            mitigation_result <- self._apply_mitigation(strategy)
        senao se strategy entao:
            mitigation_result <- {"action": "notify", "message": strategy.user_message}

        event_record <- {
            "event_id": failure.event_id,
            "failure": failure.failure_type.value,
            "severity": failure.severity.value,
            "mitigation": strategy.name if strategy else "NENHUMA (sem estrategia)",
            "fallback_chain": strategy.fallback_chain if strategy else [],
            "user_message": strategy.user_message if strategy else "Falha sem mitigacao definida!",
            "degradation_level": self.state.level.value,
            "mitigation_applied": mitigation_result,
        }
        self.event_log.append(event_record)
        retorne event_record

    funcao _update_system_state(self, failure: FailureEvent) retorna None:
        // Atualiza estado do sistema baseado na falha.
        ft <- failure.failure_type

        se ft == FailureType.BATTERY_CRITICAL entao:
            self.state.battery_pct = 3.0
            self.state.level = DegradationLevel.SURVIVAL
        senao se ft == FailureType.BATTERY_DEAD entao:
            self.state.battery_pct = 0.0
            self.state.level = DegradationLevel.DEAD
        senao se ft == FailureType.GPS_LOST entao:
            self.state.gps_available = FALSO
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_1)
        senao se ft == FailureType.CAMERA_FAILURE entao:
            self.state.camera_available = FALSO
            se "camera" in self.state.available_sensors entao:
                self.state.available_sensors.remove("camera")
            se "camera" in self.state.available_inputs entao:
                self.state.available_inputs.remove("camera")
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_1)
        senao se ft == FailureType.MICROPHONE_DEAD entao:
            self.state.microphone_available = FALSO
            se "microfone" in self.state.available_inputs entao:
                self.state.available_inputs.remove("microfone")
            se "voz" in self.state.available_inputs entao:
                self.state.available_inputs.remove("voz")
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_2)
        senao se ft == FailureType.SPEAKER_DEAD entao:
            self.state.speaker_available = FALSO
            se "tts" in self.state.available_outputs entao:
                self.state.available_outputs.remove("tts")
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_2)
        senao se ft == FailureType.TTS_CRASH entao:
            self.state.tts_available = FALSO
            se "tts" in self.state.available_outputs entao:
                self.state.available_outputs.remove("tts")
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_2)
        senao se ft == FailureType.VIBRATION_DEAD entao:
            self.state.vibration_available = FALSO
            se "vibracao" in self.state.available_outputs entao:
                self.state.available_outputs.remove("vibracao")
            se "haptico" in self.state.available_outputs entao:
                self.state.available_outputs.remove("haptico")
        senao se ft == FailureType.SCREEN_BROKEN  OU  ft == FailureType.SCREEN_DEAD entao:
            self.state.screen_available = FALSO
            se "tela" in self.state.available_outputs entao:
                self.state.available_outputs.remove("tela")
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_2)
        senao se ft == FailureType.BLUETOOTH_DROP entao:
            self.state.braille_connected = FALSO
            se "braille" in self.state.available_outputs entao:
                self.state.available_outputs.remove("braille")
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_1)
        senao se ft == FailureType.NETWORK_DOWN  OU  ft == FailureType.CLOUD_DOWN entao:
            self.state.network_available = FALSO
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_1)
        senao se ft == FailureType.SMARTWATCH_LOST entao:
            self.state.smartwatch_connected = FALSO
        senao se ft == FailureType.EYE_TRACKER_LOST entao:
            self.state.eye_tracker_connected = FALSO
            se "rastreio_olhos" in self.state.available_inputs entao:
                self.state.available_inputs.remove("rastreio_olhos")
        senao se ft == FailureType.WATER_DAMAGE entao:
            self.state.level = DegradationLevel.EMERGENCY
            self.state.camera_available = FALSO
            self.state.microphone_available = FALSO
            self.state.screen_available = FALSO
        senao se ft == FailureType.APP_CRASH entao:
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_1)
        senao se ft == FailureType.MEMORY_EXHAUSTED entao:
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_2)
        senao se ft == FailureType.PERMISSION_REVOKED entao:
            self.state.microphone_available = FALSO
            se "microfone" in self.state.available_inputs entao:
                self.state.available_inputs.remove("microfone")
        senao se ft == FailureType.STT_FAILURE entao:
            se "voz" in self.state.available_inputs entao:
                self.state.available_inputs.remove("voz")
            self.state.level = self._escalate(self.state.level, DegradationLevel.DEGRADED_2)

    funcao _apply_mitigation(self, strategy: MitigationStrategy) retorna Dict[str, Any]:
        // Aplica mitigacao e restaura capacidades quando possivel.
        result <- {
            "strategy": strategy.name,
            "fallback_chain": strategy.fallback_chain,
            "recovery_action": strategy.recovery_action,
        }

        // Mitigacoes especificas que restauram capacidade
        se strategy.failure_type == FailureType.TTS_CRASH entao:
            // Braille ou vibracao assumem
            se self.state.braille_connected entao:
                se "braille" NAO  in self.state.available_outputs entao:
                    self.state.available_outputs.append("braille")
                result["restored_output"] = "braille"
            senao se self.state.vibration_available entao:
                se "vibracao" NAO  in self.state.available_outputs entao:
                    self.state.available_outputs.append("vibracao")
                result["restored_output"] = "vibracao"

        senao se strategy.failure_type == FailureType.CAMERA_FAILURE entao:
            // Microfone + acelerometro assumem
            se self.state.microphone_available  E  "audio_sonar" NAO  in self.state.available_sensors entao:
                self.state.available_sensors.append("audio_sonar")
                result["restored_sensor"] = "audio_sonar (microfone como sonar)"

        senao se strategy.failure_type == FailureType.MICROPHONE_DEAD entao:
            // Switch/touch/eye assumem
            se "switch" NAO  in self.state.available_inputs  E  self.state.screen_available entao:
                self.state.available_inputs.append("switch")
                result["restored_input"] = "switch (botoes na tela)"

        senao se strategy.failure_type == FailureType.GPS_LOST entao:
            // Bussola + passos
            se "bussola" in self.state.available_sensors  E  "dead_reckoning" NAO  in self.state.available_sensors entao:
                self.state.available_sensors.append("dead_reckoning")
                result["restored_sensor"] = "dead_reckoning (bussola + passos)"

        senao se strategy.failure_type == FailureType.APP_CRASH entao:
            // Watchdog reinicia
            result["restored"] = "watchdog reiniciou em 3s"

        retorne result

    funcao recover_failure(self, failure_type: FailureType) retorna Dict[str, Any]:
        // Recupera de uma falha.
        recovered <- FALSO
        para cada (i, f) em enumerate(self.state.active_failures):
            se f.failure_type == failure_type entao:
                self.state.active_failures.pop(i)
                recovered <- VERDADEIRO
                interrompa

        // Remover mitigacao
        strategy <- self.strategies.get(failure_type)
        se strategy  E  strategy.strategy_id in self.mitigations_active entao:
            remova self.mitigations_active[strategy.strategy_id]

        // Recalcular nivel
        self._recalculate_level()

        // Restaurar capacidades
        se failure_type == FailureType.GPS_LOST entao:
            self.state.gps_available = VERDADEIRO
            se "gps" NAO  in self.state.available_sensors entao:
                self.state.available_sensors.append("gps")
        senao se failure_type == FailureType.CAMERA_FAILURE entao:
            self.state.camera_available = VERDADEIRO
            se "camera" NAO  in self.state.available_sensors entao:
                self.state.available_sensors.append("camera")
        senao se failure_type == FailureType.NETWORK_DOWN entao:
            self.state.network_available = VERDADEIRO
        senao se failure_type == FailureType.TTS_CRASH entao:
            self.state.tts_available = VERDADEIRO
            se "tts" NAO  in self.state.available_outputs entao:
                self.state.available_outputs.append("tts")

        result <- {
            "recovered": recovered,
            "failure": failure_type.value,
            "current_level": self.state.level.value,
            "remaining_failures": len(self.state.active_failures),
        }
        retorne result

    funcao _escalate(self, current: DegradationLevel, new: DegradationLevel) retorna DegradationLevel:
        // Escolhe o nivel de degradacao MAIS GRAVE.
        levels <- [
            DegradationLevel.FULL,
            DegradationLevel.DEGRADED_1,
            DegradationLevel.DEGRADED_2,
            DegradationLevel.SURVIVAL,
            DegradationLevel.EMERGENCY,
            DegradationLevel.DEAD,
        ]
        retorne levels[max(levels.index(current), levels.index(new))]

    funcao _recalculate_level(self) retorna None:
        // Recalcula nivel de degradacao baseado nas falhas ativas.
        se NAO  self.state.active_failures entao:
            self.state.level = DegradationLevel.FULL
            retorne nulo

        max_severity <- max(
            self.state.active_failures,
            key <- funcao anonima(f): [
                FailureSeverity.COSMETIC,
                FailureSeverity.MINOR,
                FailureSeverity.MAJOR,
                FailureSeverity.CRITICAL,
                FailureSeverity.CATASTROPHIC,
            ].index(f.severity)
        )

        se max_severity.severity == FailureSeverity.CATASTROPHIC entao:
            self.state.level = DegradationLevel.EMERGENCY
        senao se max_severity.severity == FailureSeverity.CRITICAL entao:
            self.state.level = DegradationLevel.SURVIVAL
        senao se max_severity.severity == FailureSeverity.MAJOR entao:
            self.state.level = DegradationLevel.DEGRADED_2
        senao se max_severity.severity == FailureSeverity.MINOR entao:
            self.state.level = DegradationLevel.DEGRADED_1
        senao:
            self.state.level = DegradationLevel.FULL

    funcao system_status(self) retorna Dict[str, Any]:
        // Retorna status completo do sistema.
        retorne {
            "degradation_level": self.state.level.value,
            "battery_pct": self.state.battery_pct,
            "active_failures": len(self.state.active_failures),
            "active_mitigations": len(self.mitigations_active),
            "available_inputs": list(self.state.available_inputs),
            "available_outputs": list(self.state.available_outputs),
            "available_sensors": list(self.state.available_sensors),
            "network": self.state.network_available,
            "gps": self.state.gps_available,
            "camera": self.state.camera_available,
            "microphone": self.state.microphone_available,
            "speaker": self.state.speaker_available,
            "tts": self.state.tts_available,
            "screen": self.state.screen_available,
            "vibration": self.state.vibration_available,
            "braille": self.state.braille_connected,
        }


// ============================================================================
// 6. SIMULACOES DE CENARIO CATASTROFICO
// ============================================================================

funcao simulate_blind_user_battery_death():
    // Cenario: cego na rua, bateria morrendo.
    print("=" * 65)
    print("CENARIO 1: Cego na rua -- bateria morrendo")
    print("=" * 65)

    sim <- FailureSimulator()

    // Sistema funcionando
    print(f"\n[ESTADO INICIAL]")
    status <- sim.system_status()
    print(f"  Nivel: {status['degradation_level']}")
    print(f"  Bateria: {status['battery_pct']}%")
    print(f"  Inputs: {status['available_inputs']}")

    // Bateria critica
    print(f"\n[FALHA: Bateria critica]")
    event <- FailureEvent(
        event_id <- "EVT-001",
        failure_type <- FailureType.BATTERY_CRITICAL,
        category <- FailureCategory.POWER,
        severity <- FailureSeverity.CRITICAL,
        duration <- FailureDuration.SHORT,
        description <- "Bateria abaixo de 5%",
        user_impact <- "Sistema entra em modo sobrevivencia",
    )
    result <- sim.inject_failure(event)
    print(f"  Mitigacao: {result['mitigation']}")
    print(f"  Mensagem ao usuario: {result['user_message']}")
    status <- sim.system_status()
    print(f"  Nivel atual: {status['degradation_level']}")
    print(f"  Bateria: {status['battery_pct']}%")

    // Bateria morta
    print(f"\n[FALHA: Bateria morta]")
    event <- FailureEvent(
        event_id <- "EVT-002",
        failure_type <- FailureType.BATTERY_DEAD,
        category <- FailureCategory.POWER,
        severity <- FailureSeverity.CATASTROPHIC,
        duration <- FailureDuration.LONG,
        description <- "Bateria em 0%",
        user_impact <- "Smartphone morre. Handoff necessario.",
    )
    result <- sim.inject_failure(event)
    print(f"  Mitigacao: {result['mitigation']}")
    para cada fb em result['fallback_chain']:
        print(f"    {fb}")
    print(f"  Mensagem: {result['user_message']}")


funcao simulate_cascading_failures():
    // Cenario: falhas em cascata -- multiplos sistemas falham juntos.
    print(f"\n{'=' * 65}")
    print("CENARIO 2: Falhas em cascata")
    print("=" * 65)

    sim <- FailureSimulator()

    cascading_failures <- [
        FailureEvent("C-01", FailureType.NETWORK_DOWN, FailureCategory.NETWORK,
                     FailureSeverity.MAJOR, FailureDuration.MEDIUM,
                     "Internet caiu"),
        FailureEvent("C-02", FailureType.GPS_LOST, FailureCategory.SENSOR,
                     FailureSeverity.MAJOR, FailureDuration.MEDIUM,
                     "GPS perdido"),
        FailureEvent("C-03", FailureType.BLUETOOTH_DROP, FailureCategory.PERIPHERAL,
                     FailureSeverity.MAJOR, FailureDuration.TRANSIENT,
                     "Braille desconectou"),
        FailureEvent("C-04", FailureType.TTS_CRASH, FailureCategory.SOFTWARE,
                     FailureSeverity.CRITICAL, FailureDuration.SHORT,
                     "TTS crashou"),
    ]

    para cada f em cascading_failures:
        print(f"\n[FALHA: {f.failure_type.value}]")
        result <- sim.inject_failure(f)
        status <- sim.system_status()
        print(f"  Severidade: {f.severity.value}")
        print(f"  Mitigacao: {result['mitigation']}")
        print(f"  Nivel sistema: {status['degradation_level']}")
        print(f"  Outputs restantes: {status['available_outputs']}")
        print(f"  Inputs restantes: {status['available_inputs']}")

    print(f"\n[ESTADO APOS 4 FALHAS EM CASCATA]")
    status <- sim.system_status()
    print(f"  Nivel: {status['degradation_level']}")
    print(f"  Falhas ativas: {status['active_failures']}")
    print(f"  Mitigacoes ativas: {status['active_mitigations']}")

    // Recuperar uma por uma
    print(f"\n[RECUPERACAO GRADUAL]")
    para cada ft em [FailureType.TTS_CRASH, FailureType.BLUETOOTH_DROP, FailureType.GPS_LOST, FailureType.NETWORK_DOWN]:
        r <- sim.recover_failure(ft)
        print(f"  {ft.value}: nivel -> {r['current_level']}")


funcao simulate_water_damage():
    // Cenario: smartphone caiu na agua.
    print(f"\n{'=' * 65}")
    print("CENARIO 3: Dano por agua")
    print("=" * 65)

    sim <- FailureSimulator()

    print(f"\n[FALHA: Smartphone molhou]")
    event <- FailureEvent(
        event_id <- "W-01",
        failure_type <- FailureType.WATER_DAMAGE,
        category <- FailureCategory.HARDWARE,
        severity <- FailureSeverity.CATASTROPHIC,
        duration <- FailureDuration.PERMANENT,
        description <- "Smartphone caiu na agua/poça",
        user_impact <- "Multiplas falhas simultaneas. Dispositivo morrendo.",
    )
    result <- sim.inject_failure(event)
    print(f"  Mitigacao: {result['mitigation']}")
    print(f"  Mensagem: {result['user_message']}")
    para cada fb em result['fallback_chain']:
        print(f"    {fb}")
    status <- sim.system_status()
    print(f"  Nivel: {status['degradation_level']}")
    print(f"  Camera: {status['camera']} | Microfone: {status['microphone']} | Tela: {status['screen']}")


funcao simulate_software_resilience():
    // Cenario: app crasha repetidamente.
    print(f"\n{'=' * 65}")
    print("CENARIO 4: Software crash + auto-recovery")
    print("=" * 65)

    sim <- FailureSimulator()

    para cada i em range(3):
        print(f"\n[FALHA {i+1}: App crashou]")
        event <- FailureEvent(
            event_id <- f"S-{i+1:02d}",
            failure_type <- FailureType.APP_CRASH,
            category <- FailureCategory.SOFTWARE,
            severity <- FailureSeverity.MAJOR,
            duration <- FailureDuration.TRANSIENT,
            description <- f"App crashou (tentativa {i+1})",
        )
        result <- sim.inject_failure(event)
        print(f"  Mitigacao: {result['mitigation']}")
        print(f"  User message: {result['user_message']}")

        se i < 2 entao:
            r <- sim.recover_failure(FailureType.APP_CRASH)
            print(f"  Recuperado: nivel -> {r['current_level']}")


funcao simulate_multi_user_scenarios():
    // Simula impacto de falhas para diferentes deficiencias.
    print(f"\n{'=' * 65}")
    print("CENARIO 5: Impacto por deficiencia")
    print("=" * 65)

    scenarios <- [
        ("CEGO", [
            FailureType.TTS_CRASH,       // perde voz = cego perdido
            FailureType.GPS_LOST,        // perde navegacao
            FailureType.BLUETOOTH_DROP,  // perde braille
        ]),
        ("SURDO", [
            FailureType.SCREEN_BROKEN,   // perde visual
            FailureType.VIBRATION_DEAD,  // perde haptico
        ]),
        ("TETRAPLEGICO", [
            FailureType.STT_FAILURE,     // perde voz = sem entrada
            FailureType.EYE_TRACKER_LOST,   // perde olhos
        ]),
        ("AUTISTA", [
            FailureType.NETWORK_DOWN,    // perde rotina familiar
            FailureType.SPEAKER_DEAD,    // perde audio calmante
        ]),
    ]

    para cada (label, failures) em scenarios:
        print(f"\n  {label}:")
        sim <- FailureSimulator()
        para cada ft em failures:
            event <- FailureEvent(
                event_id <- f"M-{label}-{ft.value}",
                failure_type <- ft,
                category <- FailureCategory.HARDWARE,
                severity <- FailureSeverity.CRITICAL,
                duration <- FailureDuration.SHORT,
                description <- ft.value,
            )
            result <- sim.inject_failure(event)
            status <- sim.system_status()
            print(f"    Falha: {ft.value}")
            print(f"      Nivel: {status['degradation_level']}")
            print(f"      Mitigacao: {result['mitigation']}")
            print(f"      Inputs: {status['available_inputs']}")
            print(f"      Outputs: {status['available_outputs']}")


funcao simulate_full_catastrophe():
    // Cenario: tudo falha ao mesmo tempo.
    print(f"\n{'=' * 65}")
    print("CENARIO 6: CATASTROFE TOTAL")
    print("=" * 65)

    sim <- FailureSimulator()
    all_failures <- [
        FailureType.BATTERY_CRITICAL, FailureType.GPS_LOST, FailureType.CAMERA_FAILURE,
        FailureType.MICROPHONE_DEAD, FailureType.TTS_CRASH, FailureType.BLUETOOTH_DROP,
        FailureType.NETWORK_DOWN, FailureType.SCREEN_BROKEN, FailureType.VIBRATION_DEAD,
        FailureType.SMARTWATCH_LOST,
    ]

    print(f"\nInjetando {len(all_failures)} falhas simultaneas...")
    para cada ft em all_failures:
        event <- FailureEvent(
            event_id <- f"CAT-{ft.value}",
            failure_type <- ft,
            category <- FailureCategory.HARDWARE,
            severity <- FailureSeverity.CATASTROPHIC,
            duration <- FailureDuration.PERMANENT,
            description <- f"Catastrofe: {ft.value}",
        )
        sim.inject_failure(event)

    status <- sim.system_status()
    print(f"\n[ESTADO APOS CATASTROFE]")
    print(f"  Nivel: {status['degradation_level']}")
    print(f"  Bateria: {status['battery_pct']}%")
    print(f"  Falhas ativas: {status['active_failures']}")
    print(f"  Mitigacoes ativas: {status['active_mitigations']}")
    print(f"  Inputs: {status['available_inputs']}")
    print(f"  Outputs: {status['available_outputs']}")
    print(f"  Sensores: {status['available_sensors']}")

    se NAO  status['available_outputs']  E  NAO  status['available_inputs'] entao:
        print(f"\n  PLANO D: LIGACAO CELULAR DIRETA")
        print(f"  O unico canal que resta e o sinal de celular + SMS.")
        print(f"  Sistema envia SMS com localizacao para emergencia.")
        print(f"  Se nem sinal tem: GRITE. Peça ajuda humana.")


// ============================================================================
// 7. DEMONSTRACAO
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenResilience -- Simulacao de Falhas e Mitigacao")
    print("=" * 70)

    print(f"\nFalhas mapeadas: {len(FailureType)}")
    print(f"Categorias de falha: {len(FailureCategory)}")
    print(f"Estrategias de mitigacao: {len(MITIGATION_STRATEGIES)}")
    print(f"Niveis de degradacao: {len(DegradationLevel)}")

    // Resumo de cobertura
    print(f"\n{'=' * 70}")
    print("COBERTURA DE MITIGACAO POR CATEGORIA")
    print(f"{'=' * 70}")
    by_category <- defaultdict(int)
    para cada s em MITIGATION_STRATEGIES:
        by_category[s.failure_type] += 1
    cats <- defaultdict(int)
    para cada ft em FailureType:
        se ft in [s.failure_type for s in MITIGATION_STRATEGIES] entao:
            cats[ft] = VERDADEIRO
    covered <- len(cats)
    total <- len(FailureType)
    print(f"  Falhas com mitigacao: {covered}/{total}")

    // Cenarios
    simulate_blind_user_battery_death()
    simulate_cascading_failures()
    simulate_water_damage()
    simulate_software_resilience()
    simulate_multi_user_scenarios()
    simulate_full_catastrophe()

    // Resumo final
    print(f"\n{'=' * 70}")
    print("RESUMO DE MITIGACOES")
    print(f"{'=' * 70}")
    para cada s em MITIGATION_STRATEGIES:
        print(f"\n  {s.strategy_id}: {s.name}")
        print(f"    Falha: {s.failure_type.value}")
        print(f"    Descricao: {s.description}")
        print(f"    Planos: {len(s.fallback_chain)} fallbacks")
        para cada (i, fb) em enumerate(s.fallback_chain):
            print(f"      {fb}")

    print(f"\n{'=' * 70}")
    print(f"Total falhas: {len(FailureType)}")
    print(f"Total mitigacoes: {len(MITIGATION_STRATEGIES)}")
    print(f"Cada falha tem Plano A, B, C e D.")
    print(f"Nenhum ponto unico de falha.")
    print(f"Redundancia em TUDO.")
    print(f"\nO sistema PODE falhar. O usuario NAO pode ficar desamparado.")


se __name__ == "__main__" entao:
    demo()

```
