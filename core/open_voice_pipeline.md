# OpenVoicePipeline -- Arquitetura em Camadas para Processamento de Voz Near-Realtime

**Arquivo original:** `open-republic/core/open_voice_pipeline.py`

**Descricao:** ======================================================================================
"150 milissegundos. Do microfone a acao. E o alvo."
O PROBLEMA:
  Hoje o pipeline e SEQUENCIAL:
  Microfone -> Whisper (500ms) -> Parser (10ms) -> Executor (50ms) -> TTS (300ms)
  Total: ~860ms. O usuario PERCEBE a latencia. Parece lerdo.
A SOLUCAO:
  Pipeline em CAMADAS com processamento PARALELO e CASCATEADO.
  Cada camada tem um BUDGET de latencia. O total e < 150ms para
  deteccao de comando, < 500ms para inicio de fala (TTS).
AS 9 CAMADAS (com budget de latencia):
  Layer 0: AUDIO CAPTURE          |   5ms  | Ring buffer 2s, ALSA/PulseAudio
  Layer 1: VAD                    |  10ms  | Silero VAD: detecta fala vs silencio
  Layer 2: HOT WORD               |  20ms  | Snowboy/OpenWakeWord: "republica" -> acorda
  Layer 3: STT (Whisper cascaded) |  80ms  | tiny(39M) -> base(74M) se incerto
  Layer 4: NLU (intent parser)    |   5ms  | Regex + fuzzy match + cache
  Layer 5: ROUTER                 |   2ms  | Comando? Conversa? Legenda? Pentest?
  Layer 6: EXECUTOR               |  20ms  | Shell/system/AT-SPI (async)
  Layer 7: TTS                    | 100ms  | Kokoro/espeak/Chatterbox (streaming start)
  Layer 8: FEEDBACK               |   8ms  | Overlay + caption + haptic
  BUDGET TOTAL (Layer 0-6):  ~150ms  (comando detectado e executado)
  BUDGET TTS START (Layer 7): ~100ms (primeira silaba falada)
  TOTAL PERCEBIDO: ~250ms (imperceptivel para humano)
AS 7 OTIMIZACOES (que fazem 150ms ser possivel):
1. CASCATA DE MODELOS (model cascade):
   Whisper tiny (39M) transcreve primeiro. Se confianca > 0.85, USA.
   Se < 0.85, escala para base (74M). Se ainda incerto, small (244M).
   80% dos comandos sao claros -> tiny resolve em 20ms.
   So 20% precisa de base. Quase nenhum precisa de small.
2. VAD ANTES DE WHISPER (nao transcreve silencio):
   Silero VAD processa em 10ms. Se nao tem fala, Whisper NAO RODA.
   Economiza 80% do processamento (a maioria do tempo e silencio).
3. HOT WORD LEVE (nao usa Whisper para acordar):
   OpenWakeWord (1.8M params) detecta "republica" em 20ms.
   Whisper SO ACORDA depois da hot word. Economiza bateria + CPU.
4. RING BUFFER (audio do passado):
   Microfone grava continuamente num ring buffer de 2 segundos.
   Quando VAD detecta FIM de fala, transcreve os ULTIMOS 2 segundos.
   Nao precisa esperar o usuario terminar de falar para comecar.
5. CACHE DE TRANSCRICAO (comando repetido = zero latencia):
   "abrir firefox" ja foi transcrito antes. Cache hit -> 0ms.
   Comandos repetidos (bateria, horas, listar) sao cache hits.
   Hashtable: {texto_hash: (transcricao, timestamp)}. TTL 5 min.
6. EXECUCAO ESPECULATIVA (NLU antes de STT terminar):
   Whisper transcreve parcialmente: "abrir fire..."
   NLU ja casou "abrir" + prefix "fire" -> prepara firefox.
   Quando STT termina: "abrir firefox" -> ja esta pronto. EXECUTA.
7. TTS STREAMING (nao espera texto terminar):
   Kokoro/Chatterbox comeca a falar a PRIMEIRA FRASE antes do
   texto completo estar pronto. Primeira silaba em 100ms.
   O resto da resposta vem em streaming.
A ARQUITETURA EM CAMADAS:
  [Audio] -> L0 -> L1 -> L2 -> L3 -> L4 -> L5 -> L6 -> L7 -> L8
                                      |      |      |      |
                                      v      v      v      v
                                   Whisper  NLU   Shell   TTS
                                   (cascaded) (cache) (async) (stream)
  L0-L2: SEMPRE ATIVOS (baixo consumo, wake word)
  L3-L8: SO QUANDO ACORDADO (alto consumo, processamento real)
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenVoicePipeline -- Arquitetura em Camadas para Processamento de Voz Near-Realtime
======================================================================================
"150 milissegundos. Do microfone a acao. E o alvo."

O PROBLEMA:

  Hoje o pipeline e SEQUENCIAL:
  Microfone -> Whisper (500ms) -> Parser (10ms) -> Executor (50ms) -> TTS (300ms)
  Total: ~860ms. O usuario PERCEBE a latencia. Parece lerdo.

A SOLUCAO:

  Pipeline em CAMADAS com processamento PARALELO e CASCATEADO.
  Cada camada tem um BUDGET de latencia. O total e < 150ms para
  deteccao de comando, < 500ms para inicio de fala (TTS).

AS 9 CAMADAS (com budget de latencia):

  Layer 0: AUDIO CAPTURE          |   5ms  | Ring buffer 2s, ALSA/PulseAudio
  Layer 1: VAD                    |  10ms  | Silero VAD: detecta fala vs silencio
  Layer 2: HOT WORD               |  20ms  | Snowboy/OpenWakeWord: "republica" -> acorda
  Layer 3: STT (Whisper cascaded) |  80ms  | tiny(39M) -> base(74M) se incerto
  Layer 4: NLU (intent parser)    |   5ms  | Regex + fuzzy match + cache
  Layer 5: ROUTER                 |   2ms  | Comando? Conversa? Legenda? Pentest?
  Layer 6: EXECUTOR               |  20ms  | Shell/system/AT-SPI (async)
  Layer 7: TTS                    | 100ms  | Kokoro/espeak/Chatterbox (streaming start)
  Layer 8: FEEDBACK               |   8ms  | Overlay + caption + haptic

  BUDGET TOTAL (Layer 0-6):  ~150ms  (comando detectado e executado)
  BUDGET TTS START (Layer 7): ~100ms (primeira silaba falada)
  TOTAL PERCEBIDO: ~250ms (imperceptivel para humano)

AS 7 OTIMIZACOES (que fazem 150ms ser possivel):

1. CASCATA DE MODELOS (model cascade):
   Whisper tiny (39M) transcreve primeiro. Se confianca > 0.85, USA.
   Se < 0.85, escala para base (74M). Se ainda incerto, small (244M).
   80% dos comandos sao claros -> tiny resolve em 20ms.
   So 20% precisa de base. Quase nenhum precisa de small.

2. VAD ANTES DE WHISPER (nao transcreve silencio):
   Silero VAD processa em 10ms. Se nao tem fala, Whisper NAO RODA.
   Economiza 80% do processamento (a maioria do tempo e silencio).

3. HOT WORD LEVE (nao usa Whisper para acordar):
   OpenWakeWord (1.8M params) detecta "republica" em 20ms.
   Whisper SO ACORDA depois da hot word. Economiza bateria + CPU.

4. RING BUFFER (audio do passado):
   Microfone grava continuamente num ring buffer de 2 segundos.
   Quando VAD detecta FIM de fala, transcreve os ULTIMOS 2 segundos.
   Nao precisa esperar o usuario terminar de falar para comecar.

5. CACHE DE TRANSCRICAO (comando repetido = zero latencia):
   "abrir firefox" ja foi transcrito antes. Cache hit -> 0ms.
   Comandos repetidos (bateria, horas, listar) sao cache hits.
   Hashtable: {texto_hash: (transcricao, timestamp)}. TTL 5 min.

6. EXECUCAO ESPECULATIVA (NLU antes de STT terminar):
   Whisper transcreve parcialmente: "abrir fire..."
   NLU ja casou "abrir" + prefix "fire" -> prepara firefox.
   Quando STT termina: "abrir firefox" -> ja esta pronto. EXECUTA.

7. TTS STREAMING (nao espera texto terminar):
   Kokoro/Chatterbox comeca a falar a PRIMEIRA FRASE antes do
   texto completo estar pronto. Primeira silaba em 100ms.
   O resto da resposta vem em streaming.

A ARQUITETURA EM CAMADAS:

  [Audio] -> L0 -> L1 -> L2 -> L3 -> L4 -> L5 -> L6 -> L7 -> L8
                                      |      |      |      |
                                      v      v      v      v
                                   Whisper  NLU   Shell   TTS
                                   (cascaded) (cache) (async) (stream)

  L0-L2: SEMPRE ATIVOS (baixo consumo, wake word)
  L3-L8: SO QUANDO ACORDADO (alto consumo, processamento real)

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set, Callable de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa deque, OrderedDict de collections
// importa datetime, timedelta de datetime
// importa re
// importa time
// importa hashlib


// ============================================================================
// 1. ENUMS
// ============================================================================

classe CamadaPipeline herda de Enum:
    // As 9 camadas do pipeline de voz.
    AUDIO_CAPTURE <- ("l0_audio", "L0: Captura de Audio", 5)
    VAD <- ("l1_vad", "L1: Voice Activity Detection", 10)
    HOT_WORD <- ("l2_hotword", "L2: Hot Word Detection", 20)
    STT <- ("l3_stt", "L3: Speech-to-Text (Whisper cascaded)", 80)
    NLU <- ("l4_nlu", "L4: Natural Language Understanding", 5)
    ROUTER <- ("l5_router", "L5: Router (comando/conversa/legenda)", 2)
    EXECUTOR <- ("l6_executor", "L6: Executor (acao)", 20)
    TTS <- ("l7_tts", "L7: Text-to-Speech (streaming)", 100)
    FEEDBACK <- ("l8_feedback", "L8: Feedback (overlay/caption/haptic)", 8)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao budget_ms(self) retorna int:
        retorne self.value[2]


classe ModeloWhisper herda de Enum:
    // Modelos Whisper em cascata (do menor para o maior).
    TINY <- ("tiny", "Tiny: 39M params, int8, ~20ms/chunk", 39, 20, 0.70)
    BASE <- ("base", "Base: 74M params, int8, ~80ms/chunk", 74, 80, 0.85)
    SMALL <- ("small", "Small: 244M params, int8, ~200ms/chunk", 244, 200, 0.90)
    MEDIUM <- ("medium", "Medium: 769M params, ~500ms/chunk", 769, 500, 0.95)
    LARGE_TURBO <- ("large_v3_turbo", "Large-v3-Turbo: 809M, ~300ms GPU", 809, 300, 0.97)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao params_m(self) retorna int:
        retorne self.value[2]

    // decorador: @property
    funcao latencia_ms(self) retorna int:
        retorne self.value[3]

    // decorador: @property
    funcao limiar_confianca(self) retorna float:
        // Confianca minima para ACEITAR a transcricao deste modelo.
        retorne self.value[4]


classe TipoRoteamento herda de Enum:
    // Para onde o router envia o texto reconhecido.
    COMANDO_SO <- ("cmd_so", "Comando do SO (VoiceOSControl)")
    COMANDO_TERMINAL <- ("cmd_term", "Comando de terminal (Bridge)")
    COMANDO_PENTEST <- ("cmd_pentest", "Comando de pentest (VoicePentest)")
    CONVERSA_IARA <- ("conversa", "Conversa com Iara (Telefonista)")
    LEGENDA_CC <- ("legenda", "Legenda (UniversalCaption)")
    SOM_AMBIENTE <- ("ambiente", "Som ambiente (AmbientSound)")
    IGNORAR <- ("ignorar", "Ignorar (ruido/conversa irrelevante)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe EstrategiaOtimizacao herda de Enum:
    // As 7 estrategias de otimizacao do pipeline.
    CASCATA_MODELOS <- ("cascata", "Cascat de modelos: tiny -> base -> small")
    VAD_ANTES_STT <- ("vad", "VAD antes de Whisper (pula silencio)")
    HOT_WORD_LEVE <- ("hotword", "Hot word leve (OpenWakeWord 1.8M)")
    RING_BUFFER <- ("ring", "Ring buffer de audio (2s do passado)")
    CACHE_TRANSCRICAO <- ("cache", "Cache de transcricao (comando repetido)")
    EXECUCAO_ESPECULATIVA <- ("especulativa", "Execucao especulativa (NLU antes de STT terminar)")
    TTS_STREAMING <- ("streaming", "TTS streaming (primeira silaba em 100ms)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe EstadoPipeline herda de Enum:
    // Estado do pipeline em um momento.
    DORMINDO <- ("dormindo", "Dormindo: so L0-L2 ativos (wake word)")
    OUVINDO <- ("ouvindo", "Ouvindo: VAD detectou fala, Whisper rodando")
    PROCESSANDO <- ("processando", "Processando: NLU roteando")
    EXECUTANDO <- ("executando", "Executando: acao em andamento")
    FALANDO <- ("falando", "Falando: TTS em streaming")
    ERRO <- ("erro", "Erro: falha em alguma camada")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe HardwareTier herda de Enum:
    // Tiers de hardware que definem qual estrategia usar.
    MCU <- ("mcu", "MCU: RepublicaPort Essencial (RISC-V 32-bit, 4GB)")
    CPU_BASICO <- ("cpu_basico", "CPU Basico: RISC-V 64-bit, 8GB, sem GPU")
    CPU_PADRAO <- ("cpu_padrao", "CPU Padrao: RISC-V 64-bit, 16GB, sem GPU")
    GPU_NPU <- ("gpu_npu", "GPU/NPU: RepublicaPort Avancado, 32GB+ NPU")
    BROWSER <- ("browser", "Browser: WebGPU (Tablet/Smartphone)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


// ============================================================================
// 2. DATACLASSES
// ============================================================================

// decorador: @dataclass
classe ChunkAudio:
    // Um chunk de audio processado pelo pipeline.
    indice: int
    timestamp: str
    declare duracao_ms: int  <- 500
    declare tem_fala: bool  <- FALSO  // VAD detectou fala?
    declare volume_rms: float  <- 0.0
    declare tem_hot_word: bool  <- FALSO  // "republica" detectado?
    declare texto_parcial: str  <- ""  // transcricao parcial (streaming)
    declare texto_final: str  <- ""  // transcricao final
    declare confianca: float  <- 0.0
    declare modelo_usado: str  <- ""  // qual modelo Whisper resolveu
    declare latencia_total_ms: float  <- 0.0


// decorador: @dataclass
classe CacheEntry:
    // Entrada do cache de transcricao.
    texto: str
    timestamp: str
    declare hits: int  <- 0
    declare ttl_minutos: int  <- 5


// decorador: @dataclass
classe ConfigHardware:
    // Configuracao de hardware do dispositivo atual.
    declare tier: HardwareTier  <- HardwareTier.CPU_PADRAO
    declare ram_gb: int  <- 16
    declare tem_gpu: bool  <- FALSO
    declare tem_npu: bool  <- FALSO
    declare vram_gb: int  <- 0
    declare cpu_cores: int  <- 4
    declare cpu_freq_ghz: float  <- 2.0


// decorador: @dataclass
classe MetricaLatencia:
    // Medicao de latencia de uma camada.
    camada: CamadaPipeline
    declare latencia_real_ms: float  <- 0.0
    declare budget_ms: int  <- 0
    declare dentro_budget: bool  <- VERDADEIRO
    declare timestamp: str  <- ""

    // decorador: @property
    funcao overshot_ms(self) retorna float:
        retorne max(0, self.latencia_real_ms - self.budget_ms)


// decorador: @dataclass
classe ConfigPipeline:
    // Configuracao do pipeline para o hardware atual.
    declare hardware: ConfigHardware  <- field(default_factory=ConfigHardware)
    declare modelo_stt_inicial: ModeloWhisper  <- ModeloWhisper.TINY
    declare modelo_stt_maximo: ModeloWhisper  <- ModeloWhisper.BASE
    declare estrategia_cascata: bool  <- VERDADEIRO
    declare estrategia_vad: bool  <- VERDADEIRO
    declare estrategia_hot_word: bool  <- VERDADEIRO
    declare estrategia_ring_buffer: bool  <- VERDADEIRO
    declare estrategia_cache: bool  <- VERDADEIRO
    declare estrategia_especulativa: bool  <- VERDADEIRO
    declare estrategia_tts_streaming: bool  <- VERDADEIRO
    declare chunk_ms: int  <- 500
    declare ring_buffer_segundos: int  <- 2
    declare cache_ttl_minutos: int  <- 5
    declare confianca_minima: float  <- 0.65


// ============================================================================
// 3. SELETOR DE ESTRATEGIA POR HARDWARE
// ============================================================================

funcao selecionar_config_por_hardware(hw: ConfigHardware) retorna ConfigPipeline:
    // 
    Seleciona a configuracao otima de pipeline para o hardware.
    Hardware fraco <- modelos menores, mais otimizacoes.
    Hardware forte <- modelos maiores, menos otimizacao necessaria.
    // 
    config <- ConfigPipeline(hardware=hw)

    se hw.tier == HardwareTier.MCU entao:
        // MCU: SO cascata, VAD obrigatorio, tiny only, cache agressivo
        config.modelo_stt_inicial = ModeloWhisper.TINY
        config.modelo_stt_maximo = ModeloWhisper.TINY   // nao escala
        config.estrategia_cascata = FALSO   // so tiny
        config.chunk_ms = 1000   // chunk maior = menos processamento
        config.confianca_minima = 0.60   // aceita mais erro (compensa modelo fraco)

    senao se hw.tier == HardwareTier.CPU_BASICO entao:
        // CPU basico: cascata tiny->base, VAD, cache
        config.modelo_stt_inicial = ModeloWhisper.TINY
        config.modelo_stt_maximo = ModeloWhisper.BASE
        config.estrategia_cascata = VERDADEIRO
        config.chunk_ms = 500

    senao se hw.tier == HardwareTier.CPU_PADRAO entao:
        // CPU padrao: cascata tiny->base->small, todas otimizacoes
        config.modelo_stt_inicial = ModeloWhisper.TINY
        config.modelo_stt_maximo = ModeloWhisper.SMALL
        config.estrategia_cascata = VERDADEIRO
        config.chunk_ms = 500
        config.estrategia_especulativa = VERDADEIRO

    senao se hw.tier == HardwareTier.GPU_NPU entao:
        // GPU/NPU: large-v3-turbo direto, sem cascata (GPU e rapido)
        config.modelo_stt_inicial = ModeloWhisper.LARGE_TURBO
        config.modelo_stt_maximo = ModeloWhisper.LARGE_TURBO
        config.estrategia_cascata = FALSO   // GPU resolve direto no large
        config.chunk_ms = 300   // chunk menor = menos latencia (GPU aguenta)
        config.confianca_minima = 0.75

    senao se hw.tier == HardwareTier.BROWSER entao:
        // Browser: tiny ou base via WebGPU/WASM
        config.modelo_stt_inicial = ModeloWhisper.TINY
        config.modelo_stt_maximo = ModeloWhisper.BASE
        config.estrategia_cascata = VERDADEIRO
        config.chunk_ms = 500

    retorne config


// ============================================================================
// 4. SIMULADOR DE LATENCIA POR CAMADA
// ============================================================================

classe SimuladorLatencia:
    // 
    Simula a latencia de cada camada do pipeline.
    No mundo real: medir com time.perf_counter() em cada chamada.
    Aqui: simulacao baseada no hardware e estrategia.
    // 

    // decorador: @staticmethod
    def simular_camada(
        camada: CamadaPipeline,
        config: ConfigPipeline,
        declare tem_fala: bool  <- VERDADEIRO,
        declare cache_hit: bool  <- FALSO,
    ) -> float:
        // Simula a latencia de uma camada. Retorna ms.
        hw <- config.hardware

        se camada == CamadaPipeline.AUDIO_CAPTURE entao:
            retorne 3.0 + (1.0 if hw.cpu_cores >= 4 else 2.0)

        se camada == CamadaPipeline.VAD entao:
            se NAO  config.estrategia_vad entao:
                retorne 0.0  // VAD desligado
            retorne 8.0 if tem_fala else 5.0  // mais rapido se silencio

        se camada == CamadaPipeline.HOT_WORD entao:
            se NAO  config.estrategia_hot_word entao:
                retorne 0.0
            retorne 15.0  // OpenWakeWord ~15-20ms

        se camada == CamadaPipeline.STT entao:
            se cache_hit  E  config.estrategia_cache entao:
                retorne 0.5  // cache hit: quase zero
            se NAO  tem_fala entao:
                retorne 0.0  // VAD bloqueou, STT nao roda
            // cascata: tiny primeiro
            se config.estrategia_cascata entao:
                // 80% das vezes tiny resolve
                // importa random
                se random.random() < 0.80 entao:
                    retorne config.modelo_stt_inicial.latencia_ms * 0.8  // int8 otimizado
                senao:
                    // escala para base
                    retorne (config.modelo_stt_inicial.latencia_ms +
                            config.modelo_stt_maximo.latencia_ms) * 0.8
            senao:
                retorne config.modelo_stt_inicial.latencia_ms * 0.8

        se camada == CamadaPipeline.NLU entao:
            retorne 3.0 if config.estrategia_cache else 5.0

        se camada == CamadaPipeline.ROUTER entao:
            retorne 1.5

        se camada == CamadaPipeline.EXECUTOR entao:
            retorne 15.0  // shell async, nao bloqueia

        se camada == CamadaPipeline.TTS entao:
            se config.estrategia_tts_streaming entao:
                retorne 80.0  // primeira silaba em 80ms (streaming)
            senao:
                retorne 250.0  // sem streaming: espera gerar tudo

        se camada == CamadaPipeline.FEEDBACK entao:
            retorne 5.0

        retorne 0.0


// ============================================================================
// 5. CACHE DE TRANSCRICAO (LRU com TTL)
// ============================================================================

classe CacheTranscricao:
    // Cache LRU com TTL para transcries repetidas.

    funcao __init__(self, capacidade: int = 1000, ttl_minutos: int = 5) retorna None:
        self._cache: OrderedDict[str, CacheEntry] = OrderedDict()
        self.capacidade = capacidade
        self.ttl_minutos = ttl_minutos
        self.hits = 0
        self.misses = 0

    funcao _hash_audio(self, features: str) retorna str:
        // Hash das features do audio (nao o audio bruto).
        retorne hashlib.md5(features.encode()).hexdigest()[:16]

    funcao get(self, audio_features: str) retorna Optional[str]:
        // Busca no cache. Retorna texto ou None.
        chave <- self._hash_audio(audio_features)
        agora <- datetime.now()
        entry <- self._cache.get(chave)
        se entry e nulo entao:
            self.misses += 1
            retorne nulo
        // verificar TTL
        ts <- datetime.fromisoformat(entry.timestamp)
        se (agora - ts).total_seconds() > self.ttl_minutos * 60 entao:
            remova self._cache[chave]
            self.misses += 1
            retorne nulo
        entry.hits += 1
        self.hits += 1
        self._cache.move_to_end(chave)
        retorne entry.texto

    funcao put(self, audio_features: str, texto: str) retorna None:
        // Armazena no cache.
        chave <- self._hash_audio(audio_features)
        self._cache[chave] = CacheEntry(
            texto <- texto,
            timestamp <- datetime.now().isoformat(),
        )
        self._cache.move_to_end(chave)
        se len(self._cache) > self.capacidade entao:
            self._cache.popitem(last=FALSO)

    funcao taxa_hit(self) retorna float:
        total <- self.hits + self.misses
        retorne self.hits / total if total > 0 else 0.0

    funcao tamanho(self) retorna int:
        retorne len(self._cache)


// ============================================================================
// 6. EXECUCAO ESPECULATIVA (NLU parcial)
// ============================================================================

classe ExecutorEspeculativo:
    // 
    Execucao especulativa: NLU comeca a casar padroes
    ANTES de o STT terminar. Se o texto parcial ja casa
    um comando, prepara a execucao.
    // 

    // prefixos que indicam comando com alta certeza
    PREFIXOS_COMANDO <- {
        "abrir": "abrir_app",
        "fechar": "fechar_janela",
        "digit": "digitar_texto",
        "list": "listar",
        "aument": "volume_mais",
        "diminu": "volume_menos",
        "ler": "leitura",
        "escan": "pentest_scan",
        "audit": "pentest_audit",
        "ping": "rede_ping",
        "que hor": "falar_hora",
        "bater": "verificar_bateria",
    }

    // decorador: @classmethod
    funcao avaliar_parcial(cls, texto_parcial: str) retorna Optional[Tuple[str, float]]:
        // 
        Avalia texto parcial. Se ja casa um prefixo de comando,
        retorna (comando_preparado, confianca_especulativa).
        // 
        texto <- texto_parcial.strip().lower()
        se len(texto) < 3 entao:
            retorne nulo
        para cada (prefixo, comando) em cls.PREFIXOS_COMANDO.items():
            se texto.startswith(prefixo) entao:
                // confianca especulativa: mais letras = mais certo
                confianca <- min(0.95, 0.50 + len(prefixo) * 0.08)
                retorne (comando, confianca)
        retorne nulo

    // decorador: @classmethod
    funcao confirmar(cls, texto_final: str, comando_especulativo: str) retorna bool:
        // 
        Confirma se o texto final bate com a especulacao.
        desempacote Se sim, a execucao ja estava preparada <- ZERO latencia de NLU.
        // 
        aval <- cls.avaliar_parcial(texto_final)
        se aval  E  aval[0] == comando_especulativo entao:
            retorne VERDADEIRO
        retorne FALSO


// ============================================================================
// 7. ENGINE DO PIPELINE
// ============================================================================

classe VoicePipelineEngine:
    // Motor do pipeline de voz em camadas.

    funcao __init__(self, config: Optional[ConfigPipeline] = None) retorna None:
        self.config: ConfigPipeline = config  OU  selecionar_config_por_hardware(ConfigHardware())
        self.cache: CacheTranscricao = CacheTranscricao(
            ttl_minutos <- self.config.cache_ttl_minutos)
        self.especulador: ExecutorEspeculativo = ExecutorEspeculativo()
        self.simulador: SimuladorLatencia = SimuladorLatencia()
        self.metricas: List[MetricaLatencia] = []
        self.estado: EstadoPipeline = EstadoPipeline.DORMINDO
        self._chunk_counter = 0
        self._ring_buffer: deque = deque(maxlen=4)   // 4 chunks x 500ms = 2s

    // -- medir e simular pipeline completo --------------------------------

    def simular_pipeline_completo(
        self,
        declare tem_fala: bool  <- VERDADEIRO,
        declare cache_hit: bool  <- FALSO,
        declare hot_word_detectada: bool  <- VERDADEIRO,
    ) -> Dict[str, Any]:
        // 
        Simula o pipeline completo e retorna latencia por camada.
        // 
        declare latencias: Dict[str, float]  <- {}
        total_antes_tts <- 0.0
        declare metricas_ciclo: List[MetricaLatencia]  <- []

        para cada camada em CamadaPipeline:
            ms <- self.simulador.simular_camada(
                camada, self.config,
                tem_fala <- tem_fala,
                cache_hit <- cache_hit,
            )
            latencias[camada.id] = round(ms, 2)
            se camada != CamadaPipeline.TTS  E  camada != CamadaPipeline.FEEDBACK entao:
                total_antes_tts <- total_antes_tts + ms

            dentro <- ms <= camada.budget_ms
            metricas_ciclo.append(MetricaLatencia(
                camada <- camada,
                latencia_real_ms <- ms,
                budget_ms <- camada.budget_ms,
                dentro_budget <- dentro,
                timestamp <- datetime.now().isoformat(),
            ))

        total_com_tts <- total_antes_tts + latencias.get("l7_tts", 0)
        total_completo <- total_com_tts + latencias.get("l8_feedback", 0)

        retorne {
            "latencias_por_camada": latencias,
            "total_antes_tts_ms": round(total_antes_tts, 2),
            "total_com_tts_start_ms": round(total_com_tts, 2),
            "total_completo_ms": round(total_completo, 2),
            "dentro_budget_150ms": total_antes_tts <= 150,
            "tts_start_dentro_100ms": latencias.get("l7_tts", 999) <= 100,
            "metricas": metricas_ciclo,
        }

    // -- benchmark por hardware --------------------------------------------

    funcao benchmark_hardware(self) retorna Dict[str, Any]:
        // Roda benchmark do pipeline para o hardware atual.
        declare resultados: List[Dict[str, Any]]  <- []
        // importa random
        para cada _ em range(20):
            tem_fala <- random.random() > 0.3
            cache_hit <- random.random() < 0.25
            r <- self.simular_pipeline_completo(
                tem_fala <- tem_fala, cache_hit=cache_hit)
            resultados.append(r)

        medias <- {}
        para cada camada em CamadaPipeline:
            valores <- [r["latencias_por_camada"][camada.id] for r in resultados]
            medias[camada.id] = round(sum(valores) / len(valores), 2)

        total_medio <- sum(
            r["total_antes_tts_ms"] for r in resultados) / len(resultados)
        tts_medio <- sum(
            r["latencias_por_camada"].get("l7_tts", 0) for r in resultados) / len(resultados)
        cache_taxa <- self.cache.taxa_hit()

        retorne {
            "hardware": self.config.hardware.tier.rotulo,
            "modelo_inicial": self.config.modelo_stt_inicial.id,
            "modelo_maximo": self.config.modelo_stt_maximo.id,
            "cascata_ativa": self.config.estrategia_cascata,
            "vad_ativo": self.config.estrategia_vad,
            "hot_word_ativo": self.config.estrategia_hot_word,
            "cache_ativo": self.config.estrategia_cache,
            "especulativa_ativa": self.config.estrategia_especulativa,
            "tts_streaming_ativo": self.config.estrategia_tts_streaming,
            "latencia_media_por_camada": medias,
            "total_antes_tts_medio_ms": round(total_medio, 2),
            "tts_start_medio_ms": round(tts_medio, 2),
            "cache_hit_rate": round(cache_taxa, 2),
            "dentro_budget_150ms": total_medio <= 150,
        }

    // -- scorecard ---------------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        retorne {
            "camadas": len(list(CamadaPipeline)),
            "modelos_whisper": len(list(ModeloWhisper)),
            "estrategias_otimizacao": len(list(EstrategiaOtimizacao)),
            "tipos_roteamento": len(list(TipoRoteamento)),
            "hardware_tiers": len(list(HardwareTier)),
            "cache_tamanho": self.cache.tamanho(),
            "cache_hits": self.cache.hits,
            "cache_misses": self.cache.misses,
            "cache_hit_rate": round(self.cache.taxa_hit(), 2),
            "config_modelo_inicial": self.config.modelo_stt_inicial.id,
            "config_modelo_maximo": self.config.modelo_stt_maximo.id,
        }


// ============================================================================
// 8. DEMO
// ============================================================================

funcao _demo() retorna None:
    print("=" * 70)
    print("OpenVoicePipeline -- Arquitetura em Camadas Near-Realtime")
    print("=" * 70)

    // --- As 9 camadas ---
    print(f"\n[AS 9 CAMADAS DO PIPELINE]")
    print(f"  {'Camada':<12} {'Descricao':<45} {'Budget':>8}")
    print(f"  {'-'*68}")
    para cada c em CamadaPipeline:
        print(f"  {c.id:<12} {c.rotulo:<45} {c.budget_ms:>5}ms")

    total_budget <- sum(c.budget_ms for c in CamadaPipeline if c != CamadaPipeline.TTS)
    print(f"  {'':12} {'TOTAL (antes TTS)':<45} {total_budget:>5}ms")
    print(f"  {'':12} {'TTS start (primeira silaba)':<45} {'100':>5}ms")
    print(f"  {'':12} {'TOTAL PERCEBIDO PELO USUARIO':<45} {'~250':>5}ms")

    // --- As 7 otimizacoes ---
    print(f"\n[AS 7 OTIMIZACOES PARA NEAR-REALTIME]")
    para cada opt em EstrategiaOtimizacao:
        print(f"  [{opt.id}] {opt.rotulo}")

    // --- Cascata de modelos ---
    print(f"\n[CASCATA DE MODELOS WHISPER]")
    print(f"  {'Modelo':<18} {'Params':>8} {'Latencia':>10} {'Limiar':>8} {'Cenario':>30}")
    print(f"  {'-'*75}")
    para cada m em ModeloWhisper:
        cenario <- {
            ModeloWhisper.TINY: "80% dos comandos (rapido)",
            ModeloWhisper.BASE: "15% dos comandos (preciso)",
            ModeloWhisper.SMALL: "4% dos comandos (duvidoso)",
            ModeloWhisper.MEDIUM: "1% dos comandos (ruido forte)",
            ModeloWhisper.LARGE_TURBO: "GPU/NPU direto",
        }.get(m, "")
        print(f"  {m.id:<18} {m.params_m:>6}M {m.latencia_ms:>8}ms {m.limiar_confianca:>6.0%} {cenario:>30}")

    print(f"\n  COMO FUNCIONA A CASCATA:")
    print(f"    1. Tiny (39M) transcreve em ~20ms")
    print(f"    2. Confianca > 70%? -> ACEITA. (80% dos casos)")
    print(f"    3. Confianca < 70%? -> Base (74M) em ~80ms")
    print(f"    4. Confianca > 85%? -> ACEITA. (15% dos casos)")
    print(f"    5. Confianca < 85%? -> Small (244M) em ~200ms")
    print(f"    6. Quase sempre resolve no Tiny ou Base.")

    // --- Benchmark por hardware ---
    print(f"\n[BENCHMARK POR HARDWARE TIER]")
    print(f"  {'Hardware':<35} {'Modelo':<15} {'Pre-TTS':>10} {'TTS':>8} {'<150ms?':>8}")
    print(f"  {'-'*80}")

    para cada tier em HardwareTier:
        hw <- ConfigHardware(tier=tier)
        se tier == HardwareTier.MCU entao:
            hw.ram_gb = 4; hw.cpu_cores = 2; hw.cpu_freq_ghz = 1.0
        senao se tier == HardwareTier.CPU_BASICO entao:
            hw.ram_gb = 8; hw.cpu_cores = 4
        senao se tier == HardwareTier.CPU_PADRAO entao:
            hw.ram_gb = 16; hw.cpu_cores = 8
        senao se tier == HardwareTier.GPU_NPU entao:
            hw.ram_gb = 32; hw.tem_npu = VERDADEIRO; hw.cpu_cores = 16
        senao se tier == HardwareTier.BROWSER entao:
            hw.ram_gb = 8; hw.cpu_cores = 4

        config <- selecionar_config_por_hardware(hw)
        engine <- VoicePipelineEngine(config)
        bench <- engine.benchmark_hardware()
        pre_tts <- bench["total_antes_tts_medio_ms"]
        tts <- bench["tts_start_medio_ms"]
        dentro <- "SIM" if bench["dentro_budget_150ms"] else "NAO"
        modelo <- f"{config.modelo_stt_inicial.id}"
        se config.estrategia_cascata entao:
            modelo <- modelo + f"->{config.modelo_stt_maximo.id}"
        print(f"  {tier.rotulo:<35} {modelo:<15} {pre_tts:>8.0f}ms {tts:>6.0f}ms {dentro:>8}")

    // --- Detalhe: pipeline completo em acao ---
    print(f"\n[PIPELINE COMPLETO EM ACAO -- CPU Padrao]")
    print(f"  Simulando: usuario diz 'abrir firefox'")
    config <- selecionar_config_por_hardware(ConfigHardware(tier=HardwareTier.CPU_PADRAO))
    engine <- VoicePipelineEngine(config)

    // cenario 1: fala clara, sem cache
    print(f"\n  CENARIO 1: Fala clara, sem cache (primeira vez)")
    r <- engine.simular_pipeline_completo(tem_fala=VERDADEIRO, cache_hit=FALSO)
    print(f"    {'Camada':<12} {'Latencia':>10} {'Budget':>8} {'Status':>10}")
    print(f"    {'-'*42}")
    para cada m em r["metricas"]:
        status <- "OK" if m.dentro_budget else f"+{m.overshot_ms:.0f}ms OVER"
        print(f"    {m.camada.id:<12} {m.latencia_real_ms:>8.1f}ms {m.budget_ms:>6}ms {status:>10}")
    print(f"    {'TOTAL PRE-TTS':<12} {r['total_antes_tts_ms']:>8.1f}ms {'150':>6}ms {'OK' if r['dentro_budget_150ms'] else 'OVER':>10}")
    print(f"    {'TTS START':<12} {r['latencias_por_camada']['l7_tts']:>8.1f}ms {'100':>6}ms {'OK' if r['tts_start_dentro_100ms'] else 'OVER':>10}")

    // cenario 2: cache hit (comando repetido)
    print(f"\n  CENARIO 2: Cache HIT (comando repetido)")
    r2 <- engine.simular_pipeline_completo(tem_fala=VERDADEIRO, cache_hit=VERDADEIRO)
    print(f"    STT latencia: {r2['latencias_por_camada']['l3_stt']:.1f}ms (cache hit!)")
    print(f"    TOTAL PRE-TTS: {r2['total_antes_tts_ms']:.1f}ms")
    print(f"    Economia: {r['total_antes_tts_ms'] - r2['total_antes_tts_ms']:.1f}ms")

    // cenario 3: silencio (VAD bloqueia)
    print(f"\n  CENARIO 3: Silencio (VAD bloqueia STT)")
    r3 <- engine.simular_pipeline_completo(tem_fala=FALSO)
    print(f"    STT latencia: {r3['latencias_por_camada']['l3_stt']:.1f}ms (bloqueado)")
    print(f"    TOTAL: {r3['total_antes_tts_ms']:.1f}ms (quase zero)")

    // --- Execucao especulativa ---
    print(f"\n[EXECUCAO ESPECULATIVA]")
    print(f"  NLU comeca ANTES de STT terminar:")
    testes_parciais <- [
        ("ab", nulo),
        ("abr", ("abrir_app", 0.74)),
        ("abri", ("abrir_app", 0.82)),
        ("abrir", ("abrir_app", 0.90)),
        ("abrir fire", ("abrir_app", 0.95)),
        ("list", ("listar", 0.90)),
        ("escan", ("pentest_scan", 0.90)),
        ("que hor", ("falar_hora", 0.90)),
    ]
    para cada (parcial, esperado) em testes_parciais:
        result <- ExecutorEspeculativo.avaliar_parcial(parcial)
        se result entao:
            desempacote cmd, conf <- result
            print(f"    '{parcial}' -> {cmd} (confianca: {conf:.0%})")
        senao:
            print(f"    '{parcial}' -> (ainda nao reconhecido)")

    // --- O fluxo visual ---
    print(f"\n[FLUXO DO PIPELINE]")
    print("""
  ESTADO: DORMINDO (L0-L2 ativos, baixo consumo)
    L0: Audio -> ring buffer (2s)
    L1: VAD -> silencio? continua dormindo
    L2: Hot Word -> "republica"? -> ACORDA

  ESTADO: OUVINDO (L3 ativo)
    L1: VAD -> detectou fala!
    L3: STT -> Tiny transcreve em 20ms
    L4: NLU -> (especulativo: ja comecou no L3 parcial)
    Se confianca > 70% -> ACEITA
    Se nao -> Base transcreve em 80ms

  ESTADO: PROCESSANDO (L4-L5)
    L4: NLU -> "abrir firefox" -> cmd=abrir_app, param=firefox
    L5: Router -> COMANDO_SO (VoiceOSControl)
    (Se fosse "bom dia iara" -> CONVERSA_IARA)
    (Se fosse "escanear rede" -> COMANDO_PENTEST)

  ESTADO: EXECUTANDO (L6)
    L6: Executor -> xdotool/gdbus -> abre firefox
    (async: nao bloqueia o pipeline)

  ESTADO: FALANDO (L7-L8)
    L7: TTS -> Kokoro streaming -> "Abrindo Firefox."
    (primeira silaba em 80ms, resto em streaming)
    L8: Feedback -> overlay + caption + haptic

  VOLTA PARA: DORMINDO
    L0-L2 voltam a escutar (hot word)
    Pipeline pronto para proximo comando
// )

    // --- Comparacao: antes vs depois ---
    print(f"[COMPARACAO: SEQUENCIAL vs CAMADAS OTIMIZADAS]")
    print(f"  {'Cenario':<40} {'Sequencial':>12} {'Otimizado':>12} {'Economia':>10}")
    print(f"  {'-'*75}")
    print(f"  {'Fala clara (primeira vez)':<40} {'860ms':>12} {'~120ms':>12} {'740ms':>10}")
    print(f"  {'Comando repetido (cache hit)':<40} {'860ms':>12} {'~40ms':>12} {'820ms':>10}")
    print(f"  {'Silencio (VAD bloqueia)':<40} {'860ms':>12} {'~15ms':>12} {'845ms':>10}")
    print(f"  {'Musica/fundo (VAD+filtro)':<40} {'860ms':>12} {'~15ms':>12} {'845ms':>10}")
    print(f"  {'GPU/NPU (large direto)':<40} {'860ms':>12} {'~90ms':>12} {'770ms':>10}")

    // --- Scorecard ---
    print(f"\n[SCORECARD]")
    sc <- engine.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<30} {v}")

    // --- Filosofia ---
    print(f"\n{'='*70}")
    print(f"FILOSOFIA -- 150 milissegundos ou nada")
    print(f"{'='*70}")
    print("""
O NUMERO MAGICO:

  150ms. E o tempo que o cerebro humano leva para PERCEBER latencia.
  Abaixo de 150ms: parece INSTANTANEO.
  Acima de 150ms: parece LERDO.
  Acima de 500ms: parece QUEBRADO.
  Acima de 1s: o usuario DESISTE.

  Alexa tem ~500ms. Siri tem ~800ms. Google Assistant tem ~400ms.
  Todos acima de 150ms. Todos parecem lentos.

  A Republica alveja 150ms. E POSSIVEL com as 7 otimizacoes.

A CASCATA E O SEGREDO:

  80% dos comandos sao curtos e claros: "abrir firefox", "bateria".
  O modelo Tiny (39M) resolve em 20ms. 80% do tempo: 20ms de STT.

  So 20% dos comandos sao ambíguos ou longos.
  Ai escala para Base (74M) em 80ms. Ainda dentro do budget.

  A cascata nao e otimizacao. E ARQUITETURA.
  Usar large-v3-turbo para tudo e DESPERDICIO.
  Usar tiny para tudo e IMPRECISAO.
  Cascata <- o modelo certo para o comando certo.

VAD E A MELHOR OTIMIZACAO:

  80% do tempo, o microfone capta SILENCIO ou ruido de fundo.
  Sem VAD, Whisper roda em TODO chunk. 80% do processamento e perdido.
  Com VAD (Silero, 10ms), Whisper SO RODA quando tem fala.
  Economia de CPU: 80%. Economia de bateria: 80%.

  VAD nao e opcional. E OBRIGATORIO para near-realtime em CPU.

CACHE E ZERO LATENCIA:

  "bateria" dito 10 vezes por dia.
  Sem cache: 10x 80ms de Whisper = 800ms total.
  Com cache: 1x 80ms + 9x 0.5ms = 84.5ms total.
  Economia: 90%.

  O cache e a unica otimizacao que da latencia ZERO.
  E a mais importante para comandos repetitivos.

A INTEGRACAO COM TODO O STACK:

  Layer 5 (Router) decide para ONDE o texto vai:
  - "abrir firefox" -> VoiceOSControl -> executa
  - "sudo apt update" -> VoiceTerminalBridge -> shell
  - "escanear rede" -> VoicePentest -> nmap
  - "bom dia iara" -> Telefonista -> conversa
  - (audio do YouTube) -> UniversalCaption -> legenda
  - (campainha real) -> AmbientSoundAI -> alerta

  O pipeline e UM. O router direciona.
  O usuario nao sabe (nem precisa) qual modulo processa.
  Ele fala. O sistema responde. Em 150ms.

O PRINCIPIO FINAL:

  Latencia nao e feature. E ACESSIBILIDADE.
  Cego que espera 1s por resposta perde o RITMO de uso.
  Tetraplegico que espera 2s entre comando e acao perde a PACIENCIA.
  Idoso que espera 3s desiste e pede ajuda.

  Near-realtime nao e luxo de power user.
  E DIGNIDADE de quem DEPENDE da voz.
// )


se __name__ == "__main__" entao:
    _demo()

```
