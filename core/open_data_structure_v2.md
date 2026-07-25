# OpenDataStructure v2 -- Streaming com Constantes e Dinamicos

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_data_structure_v2.py`

**Descricao:** ===============================================================
MELHORIAS vs v1:
  1. SEPARAÇÃO: constantes (previsíveis) vs dinâmicos (variáveis)
  2. STREAMING: nao batch -- fluxo continuo com chunks
  3. DELTA: so envia o que MUDOU desde ultimo pacote
  4. SEQUENCE: pacotes numerados (ordem garantida)
  5. ACK/NACK: Hermes confirma recebimento
  6. BACKPRESSURE: se Hermes sobrecarregado, cliente desacelera
  7. HEARTBEAT: idle envia minimal (nao para)
  8. CHECKSUM: integridade verificada
  9. FRAGMENTATION: pacotes grandes quebram em fragmentos
  10. BANDWIDTH ADAPTATION: rede lenta = menos qualidade
  11. ENCRYPTION: E2E (P2 privacidade)
  12. COMPRESSION DICTIONARY: dicionario pre-compartilhado
CONSTANTES (enviadas 1x por sessão):
  - Perfil do usuario (id, idioma, timezone)
  - Hardware (CPU, RAM, camera, mic, screen)
  - Capacidades de rede (bandwidth, protocolo)
  - Voice ID fingerprint (OpenAudioChannel)
  - Codec preferences
  - Compression dictionary hash
  - Hermes endpoint
DINÂMICOS (enviados a cada pacote):
  - Texto digitado
  - Audio capturado
  - Frames de webcam
  - Timestamp
  - Prioridade (pode mudar)
  - Contexto (pode mudar)
  - Delta desde ultimo pacote
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenDataStructure v2 -- Streaming com Constantes e Dinamicos
===============================================================

MELHORIAS vs v1:
  1. SEPARAÇÃO: constantes (previsíveis) vs dinâmicos (variáveis)
  2. STREAMING: nao batch -- fluxo continuo com chunks
  3. DELTA: so envia o que MUDOU desde ultimo pacote
  4. SEQUENCE: pacotes numerados (ordem garantida)
  5. ACK/NACK: Hermes confirma recebimento
  6. BACKPRESSURE: se Hermes sobrecarregado, cliente desacelera
  7. HEARTBEAT: idle envia minimal (nao para)
  8. CHECKSUM: integridade verificada
  9. FRAGMENTATION: pacotes grandes quebram em fragmentos
  10. BANDWIDTH ADAPTATION: rede lenta = menos qualidade
  11. ENCRYPTION: E2E (P2 privacidade)
  12. COMPRESSION DICTIONARY: dicionario pre-compartilhado

CONSTANTES (enviadas 1x por sessão):
  - Perfil do usuario (id, idioma, timezone)
  - Hardware (CPU, RAM, camera, mic, screen)
  - Capacidades de rede (bandwidth, protocolo)
  - Voice ID fingerprint (OpenAudioChannel)
  - Codec preferences
  - Compression dictionary hash
  - Hermes endpoint

DINÂMICOS (enviados a cada pacote):
  - Texto digitado
  - Audio capturado
  - Frames de webcam
  - Timestamp
  - Prioridade (pode mudar)
  - Contexto (pode mudar)
  - Delta desde ultimo pacote

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa json
// importa zlib
// importa base64
// importa struct
// importa time
// importa dataclass, field, asdict de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa datetime, timezone de datetime


// ============================================================================
// 1. CONSTANTES (previsíveis -- enviadas 1x por sessão)
// ============================================================================

classe DeviceType herda de Enum:
    NOTEBOOK = "notebook"
    SMARTPHONE = "smartphone"
    TERMINAL = "terminal_burro"
    TV_STICK = "tv_stick"
    TABLET = "tablet"
    DESKTOP = "desktop"
    KIOSK = "kiosk"
    WEARABLE = "wearable"


classe NetworkType herda de Enum:
    FIBER = "fibra"  // >100 Mbps
    WIFI_FAST = "wifi_rapido"  // 50-100 Mbps
    WIFI_SLOW = "wifi_lento"  // 10-50 Mbps
    MOBILE_5G = "5g"
    MOBILE_4G = "4g"
    MOBILE_3G = "3g"  // adaptar qualidade
    SATELLITE = "satelite"  // alta latencia
    MESH = "mesh_republica"  // OpenNetwork P2P


classe AudioCodec herda de Enum:
    OPUS_24 = "opus_24kbps"  // voz -- melhor codec
    OPUS_48 = "opus_48kbps"  // alta qualidade
    OPUS_16 = "opus_16kbps"  // baixa banda
    FLAC = "flac"  // sem perda (musica)


classe VideoCodec herda de Enum:
    H264 = "h264"
    H265 = "h265"  // melhor compressao
    VP9 = "vp9"
    AV1 = "av1"  // futuro
    MJPEG = "mjpeg"  // frames simples
    WEBP = "webp"  // frames otimizados


classe CompressionLevel herda de Enum:
    NONE = 0
    FAST = 1 // zlib level 1
    BALANCED = 6 // zlib level 6
    MAX = 9 // zlib level 9


// decorador: @dataclass
classe SessionConstants:
    // CONSTANTES da sessão -- enviadas UMA VEZ no início.

    Estes dados NÃO mudam durante a sessão.
    Hermes guarda e referencia. Não reenvia.
    Economiza banda massiva.
    // 
    // Sessão
    seja session_id: texto = ""
    seja user_id: texto = ""
    seja device_type: DeviceType = DeviceType.NOTEBOOK
    seja language: texto = "pt-BR"
    seja timezone: texto = "America/Sao_Paulo"

    // Hardware (constante durante sessão)
    seja cpu_cores: inteiro = 4
    seja cpu_arch: texto = "x86_64"  // ou "risc_v", "arm"
    seja ram_gb: inteiro = 8
    seja camera_max_resolution: texto = "1280x720"
    seja camera_max_fps: inteiro = 30
    seja mic_sample_rate: inteiro = 48000
    seja mic_bit_depth: inteiro = 16
    seja mic_channels: inteiro = 1 // mono para voz
    seja screen_resolution: texto = "1920x1080"

    // Rede (constante durante sessão -- pode mudar, mas raro)
    seja network_type: NetworkType = NetworkType.WIFI_FAST
    seja estimated_bandwidth_mbps: flutuante = 50.0
    seja estimated_latency_ms: flutuante = 20.0
    seja packet_loss_rate: flutuante = 0.001 // 0.1%

    // Codecs suportados (constante -- hardware define)
    seja audio_codec: AudioCodec = AudioCodec.OPUS_24
    seja video_codec: VideoCodec = VideoCodec.WEBP
    seja compression: CompressionLevel = CompressionLevel.BALANCED

    // Voice ID (OpenAudioChannel fingerprint -- constante)
    seja voice_id_hash: texto = ""  // hash do fingerprint vocal
    seja voice_id_dimensions: inteiro = 192 // dimensoes do embedding

    // Hermes (constante)
    seja hermes_endpoint: texto = "openprotocol://hermes.local"
    seja encryption_key_id: texto = ""  // ID da chave E2E
    seja compression_dict_hash: texto = ""  // hash do dicionario pre-compartilhado

    // Capacidades (constante -- o que este dispositivo PODE)
    seja can_stream_video: logico = verdadeiro
    seja can_stream_audio: logico = verdadeiro
    seja can_stream_screen: logico = falso
    seja can_do_stt_local: logico = falso // STT no dispositivo?
    seja can_do_vad_local: logico = verdadeiro // VAD no dispositivo?
    seja can_do_face_detect: logico = verdadeiro // Face detection no dispositivo?
    seja battery_powered: logico = verdadeiro
    seja battery_pct: flutuante = 100.0 #近似 -- muda raramente

    // Limites (constante -- configurado no início)
    seja max_packet_size_kb: inteiro = 64 // pacotes >64KB fragmentam
    seja heartbeat_interval_sec: flutuante = 30.0 // idle -> heartbeat a cada 30s
    seja stream_chunk_interval_ms: inteiro = 100 // chunk a cada 100ms

    // decorador: @classmethod
    funcao create(cls, user_id: texto, device: DeviceType = DeviceType.NOTEBOOK,
               seja network: NetworkType = NetworkType.WIFI_FAST) -> "SessionConstants":
        retorne cls(
            session_id = hashlib.sha256(
                "{user_id}{time.time()}".encode()).hexdigest()[:16],
            user_id = user_id,
            device_type = device,
            network_type = network,
            voice_id_hash = hashlib.sha256(
                "{user_id}_voice".encode()).hexdigest()[:32],
            encryption_key_id = hashlib.sha256(
                "{user_id}_e2e".encode()).hexdigest()[:16],
            compression_dict_hash = hashlib.sha256(
                b"openrepublic_dict_v1").hexdigest()[:16],
        )

    funcao to_json(self) -> texto:
        d = asdict(self)
        d["device_type"] = self.device_type.value
        d["network_type"] = self.network_type.value
        d["audio_codec"] = self.audio_codec.value
        d["video_codec"] = self.video_codec.value
        d["compression"] = self.compression.value
        retorne json.dumps(d, ensure_ascii=falso, indent=2)

    // decorador: @property
    funcao estimated_size_bytes(self) -> inteiro:
        // Tamanho aproximado das constantes serializadas.
        retorne tamanho(self.to_json().encode("utf-8"))


// ============================================================================
// 2. DADOS DINÂMICOS (variáveis -- enviados a cada pacote)
// ============================================================================

classe StreamMode herda de Enum:
    ACTIVE = "ativo"  // usuario interagindo
    LISTENING = "ouvindo"  // Hermes falando, usuario ouve
    IDLE = "ocio"  // sem interacao (heartbeat)
    BACKGROUND = "background"  // contexto passivo


classe PacketType herda de Enum:
    DATA = "dados"  // pacote de dados normal
    DELTA = "delta"  // so o que mudou
    HEARTBEAT = "heartbeat"  // ocioso, minimal
    FRAGMENT = "fragmento"  // parte de pacote grande
    ACK = "ack"  // confirmacao de recebimento
    NACK = "nack"  // erro de recebimento
    BACKPRESSURE = "backpressure"  // pedir para desacelerar
    END = "fim"  // encerrar stream


// decorador: @dataclass
classe KeyboardDynamic:
    // Dados dinâmicos do teclado.
    seja text: texto = ""  // texto bruto
    seja text_compressed: texto = ""  // base64(zlib(text))
    seja text_delta: texto = ""  // so caracteres NOVOS desde ultimo
    seja is_delta: logico = falso // é delta?
    seja raw_bytes: inteiro = 0
    seja compressed_bytes: inteiro = 0
    seja typing_speed_wpm: flutuante = 0.0
    seja input_type: texto = "command"  // command, question, correction
    seja has_code: logico = falso
    seja has_url: logico = falso
    seja has_emoji: logico = falso
    seja caps_lock: logico = falso
    seja enter_pressed: logico = falso // submeteu?


// decorador: @dataclass
classe AudioDynamic:
    // Dados dinâmicos do audio.
    seja chunk_b64: texto = ""  // base64(opus chunk)
    seja chunk_duration_ms: inteiro = 100 // duracao deste chunk
    seja is_silence: logico = falso // VAD: silencio? (nao enviar se verdadeiro)
    seja is_delta: logico = falso // audio delta (raro, mas possivel)
    seja transcription: texto = ""  // STT local (se device suporta)
    seja transcription_confidence: flutuante = 0.0
    seja voice_id_match: flutuante = 0.0 // match com fingerprint (0-1)
    seja ambient_changed: logico = falso // ambiente mudou?
    seja ambient_type: texto = ""  // rua, escritorio, musica
    seja noise_level_db: flutuante = 0.0
    seja speaker_count: inteiro = 1 // quantas pessoas falando
    seja raw_bytes: inteiro = 0
    seja compressed_bytes: inteiro = 0


// decorador: @dataclass
classe WebcamDynamic:
    // Dados dinâmicos do webcam.
    seja frame_b64: texto = ""  // base64(webp frame)
    seja is_delta_frame: logico = verdadeiro // delta (so pixels mudados)
    seja frame_count: inteiro = 1
    seja resolution_sent: texto = "640x480"  // pode ser reduzido (bandwidth)
    seja face_detected: logico = falso
    seja face_expression: texto = ""  // neutro, focado, cansado
    seja face_confidence: flutuante = 0.0
    seja gesture: texto = "none"
    seja gaze_direction: texto = "screen"
    seja posture: texto = "upright"
    seja screen_share: logico = falso
    seja screen_ocr: texto = ""  // texto na tela
    seja objects_detected: [texto] = field(default_factory=list)
    seja background_changed: logico = falso // mudou de lugar?
    seja raw_bytes: inteiro = 0
    seja compressed_bytes: inteiro = 0


// ============================================================================
// 3. PACOTE DE STREAM (dinâmico)
// ============================================================================

// decorador: @dataclass
classe StreamPacket:
    // Pacote individual no fluxo de streaming.

    HEADER (constante por pacote -- mas dados sao dinâmicos):
    - sequence: numero sequencial (ordem)
    - timestamp_ns: nanosegundos (precisão)
    - packet_type: DATA, DELTA, HEARTBEAT, FRAGMENT, ACK, etc
    - checksum: integridade

    PAYLOAD (dinâmico):
    - keyboard, audio, webcam (opcionais cada)
    - delta_since_seq: referencia ao ultimo pacote (para delta)
    // 
    // HEADER
    seja sequence: inteiro = 0 // numero sequencial
    seja timestamp_ns: inteiro = 0 // nanosegundos
    seja packet_type: PacketType = PacketType.DATA
    seja session_id: texto = ""  // referencia às constantes
    seja priority: inteiro = 5 // 0=critico, 5=normal, 9=background
    seja stream_mode: StreamMode = StreamMode.ACTIVE
    seja checksum: texto = ""  // SHA-256 do payload
    seja context: texto = ""  // o que usuario esta fazendo

    // DELTA reference
    seja delta_since_seq: inteiro = 0 // baseado em qual pacote anterior?
    seja is_fragment: logico = falso
    seja fragment_index: inteiro = 0 // qual fragmento?
    seja fragment_total: inteiro = 0 // quantos fragmentos?
    seja fragment_id: texto = ""  // ID do pacote original fragmentado

    // PAYLOAD (dinâmico)
    seja keyboard: KeyboardDynamic? = nulo
    seja audio: AudioDynamic? = nulo
    seja webcam: WebcamDynamic? = nulo

    // TRANSPORTE
    seja rtt_ms: flutuante = 0.0 // arredonde-trip time (medido)
    seja bandwidth_used_mbps: flutuante = 0.0 // banda usada neste pacote

    // decorador: @property
    funcao payload_size_bytes(self) -> inteiro:
        size = 0
        if self.keyboard: size += self.keyboard.compressed_bytes
        if self.audio: size += self.audio.compressed_bytes
        if self.webcam: size += self.webcam.compressed_bytes
        retorne size

    // decorador: @property
    funcao has_data(self) -> logico:
        retorne any([self.keyboard, self.audio, self.webcam])

    funcao compute_checksum(self) -> texto:
        // Calcula checksum do payload.
        payload = json.dumps({
            self.keyboard ? "kb": asdict(self.keyboard) : nulo,
            self.audio ? "au": asdict(self.audio) : nulo,
            self.webcam ? "wc": asdict(self.webcam) : nulo,
        }, sort_keys=verdadeiro).encode()
        retorne hashlib.sha256(payload).hexdigest()[:16]

    funcao verify(self) -> logico:
        // Verifica integridade.
        retorne self.compute_checksum() == self.checksum

    funcao to_transport(self) -> bytes:
        // Serializa para bytes (transmissão de rede).

        Formato binario compacto:
        [seq:4B][ts:8B][type:1B][prio:1B][mode:1B][checksum:16B]
        [ctx_len:2B][ctx:N B][payload_len:4B][payload:N B]
        // 
        header = struct.pack("!IQBBB",
            self.sequence,
            self.timestamp_ns,
            isinstance(self.packet_type.value, inteiro) ? self.packet_type.value : 0,
            self.priority,
            0, // mode placeholder
        )
        payload = json.dumps({
            self.keyboard ? "kb": asdict(self.keyboard) : nulo,
            self.audio ? "au": asdict(self.audio) : nulo,
            self.webcam ? "wc": asdict(self.webcam) : nulo,
            "ctx": self.context,
        }, ensure_ascii=falso).encode("utf-8")

        ctx_bytes = self.context.encode("utf-8")
        retorne header + struct.pack("!H", tamanho(ctx_bytes)) + ctx_bytes + \
               struct.pack("!I", tamanho(payload)) + payload


// ============================================================================
// 4. MOTOR DE STREAMING
// ============================================================================

classe StreamingEngine:
    // Motor de streaming contínuo para Hermes.

    FLUXO:
    1. HANDSHAKE: cliente envia SessionConstants (1x)
    2. Hermes responde com config confirmada
    3. STREAM: cliente envia StreamPacket a cada chunk_interval
    4. Hermes responde ACK/NACK
    5. DELTA: se nada mudou, envia HEARTBEAT (minimal)
    6. BACKPRESSURE: se Hermes lento, pede para desacelerar
    7. END: cliente envia END ao encerrar

    OTIMIZACOES:
    - DELTA: so envia o que MUDOU desde ultimo pacote
    - SILENCE SKIP: audio em silencio nao e enviado (VAD local)
    - FRAME SKIP: webcam sem mudanca nao envia frame
    - ADAPTIVE QUALITY: rede lenta = menos fps/resolucao
    - FRAGMENTATION: pacote > max_size quebra em fragmentos
    - COMPRESSION DICT: dicionario pre-compartilhado melhora compressao

    CONSTANTES vs DINAMICOS:
    - Constantes: SessionConstants (1x no handshake)
    - Dinamicos: StreamPacket (a cada chunk)
    - Delta: dentro do dinamico, so o que mudou
    // 

    funcao __init__(self):
        self.constants: SessionConstants? = nulo
        self.sequence_counter: inteiro = 0
        self.last_packet: StreamPacket? = nulo
        self.packets_sent: inteiro = 0
        self.acks_received: inteiro = 0
        self.nacks_received: inteiro = 0
        self.bytes_sent: inteiro = 0
        self.bytes_saved_delta: inteiro = 0
        self.bytes_saved_silence: inteiro = 0
        self.bytes_saved_frame_skip: inteiro = 0
        self.fragments_sent: inteiro = 0
        self.heartbeats_sent: inteiro = 0
        self.backpressure_events: inteiro = 0
        self.rtt_history: [flutuante] = []
        self.bandwidth_history: [flutuante] = []
        self.last_text: texto = ""         // para delta de texto
        self.last_ambient: texto = ""      // para delta de ambiente
        self.last_expression: texto = ""   // para delta de expressao

    funcao handshake(self, user_id: texto,
                  seja device: DeviceType = DeviceType.NOTEBOOK,
                  seja network: NetworkType = NetworkType.WIFI_FAST
                  ) -> {texto: qualquer}:
        // Handshake: envia constantes UMA VEZ.
        self.constants = SessionConstants.create(user_id, device, network)
        retorne {
            "handshake": "OK",
            "session_id": self.constants.session_id,
            "constants_size_bytes": self.constants.estimated_size_bytes,
            "constants_sent_once": verdadeiro,
            "audio_codec": self.constants.audio_codec.value,
            "video_codec": self.constants.video_codec.value,
            "compression": "zlib level {self.constants.compression.value}",
            "chunk_interval_ms": self.constants.stream_chunk_interval_ms,
            "heartbeat_interval_s": self.constants.heartbeat_interval_sec,
            "max_packet_kb": self.constants.max_packet_size_kb,
            "encryption": "E2E key {self.constants.encryption_key_id[:8]}",
            "compression_dict": "dict {self.constants.compression_dict_hash[:8]}",
            "voice_id": "fingerprint {self.constants.voice_id_hash[:8]}",
            "message": (
                "Constantes enviadas UMA VEZ. "
                "A partir de agora, so DADOS DINAMICOS. "
                "Economia massiva de banda."
            ),
        }

    funcao _next_seq(self) -> inteiro:
        self.sequence_counter += 1
        retorne self.sequence_counter

    funcao _compress(self, data: texto) retorna Tuple[texto, inteiro, inteiro]:
        // Comprime string com zlib.
        raw = data.encode("utf-8")
        level = self.constants ? self.constants.compression.value : 6
        compressed = zlib.compress(raw, level=level)
        retorne base64.b64encode(compressed).decode("ascii"), tamanho(raw), tamanho(compressed)

    funcao _compute_delta_text(self, new_text: texto) retorna (texto, logico):
        // Computa delta de texto (so o que mudou).
        se new_text == self.last_text entao:
            retorne "", verdadeiro  // nada mudou
        // Delta simples: texto novo
        // (em produção: algoritmo diff real)
        self.last_text = new_text
        retorne new_text, falso

    funcao send_data(self, text: texto = "",
                  seja audio_transcription: texto = "",
                  seja audio_silence: logico = falso,
                  seja audio_ambient: texto = "",
                  seja expression: texto = "",
                  seja gesture: texto = "none",
                  seja gaze: texto = "screen",
                  seja screen_ocr: texto = "",
                  seja context: texto = "",
                  seja priority: inteiro = 5,
                  ) -> {texto: qualquer}:
        // Envia pacote de dados no stream.

        se nao self.constants entao:
            retorne {"error": "Handshake nao feito"}

        seq = self._next_seq()
        ts = inteiro(time.time_ns())

        packet = StreamPacket(
            sequence = seq, timestamp_ns=ts,
            packet_type = PacketType.DATA,
            session_id = self.constants.session_id,
            priority = priority,
            context = context,
            delta_since_seq = self.last_packet ? self.last_packet.sequence : 0,
        )

        savings = {"delta": 0, "silence": 0, "frame_skip": 0}

        // === KEYBOARD ===
        se text entao:
            desempacote delta_text, is_delta = self._compute_delta_text(text)
            se is_delta e self.last_packet e self.last_packet.keyboard entao:
                // Texto nao mudou -- pular
                savings["delta"] += tamanho(text.encode("utf-8"))
            senao:
                desempacote compressed, raw_b, comp_b = self._compress(text)
                packet.keyboard = KeyboardDynamic(
                    text = text, text_compressed=compressed,
                    raw_bytes = raw_b, compressed_bytes=comp_b,
                    has_code = any(kw in text para kw em ["def ", "fn ", "import "]),
                    has_url = "http" in text,
                    enter_pressed = text.endswith("\n"),
                )

        // === AUDIO ===
        se nao audio_silence entao:
            se audio_transcription ou audio_ambient entao:
                // Simular chunk OPUS
                chunk_data = "OPUS_{audio_transcription[:20]}".encode()
                chunk_b64 = base64.b64encode(chunk_data).decode("ascii")
                ambient_changed = audio_ambient != self.last_ambient
                self.last_ambient = audio_ambient

                packet.audio = AudioDynamic(
                    chunk_b64 = chunk_b64,
                    chunk_duration_ms = self.constants.stream_chunk_interval_ms,
                    transcription = audio_transcription,
                    transcription_confidence = 0.95,
                    voice_id_match = 0.92,
                    ambient_type = audio_ambient,
                    ambient_changed = ambient_changed,
                    noise_level_db = 35.0,
                    compressed_bytes = tamanho(chunk_b64),
                    raw_bytes = tamanho(chunk_data) * 10,
                )
        senao:
            // Silencio -- VAD local detectou. Nao enviar audio.
            savings["silence"] += 2400   // ~100ms de opus 24kbps

        // === WEBCAM ===
        se expression entao:
            expr_changed = expression != self.last_expression
            se nao  expr_changed  e  nao  gesture != "none" entao:
                // Nada mudou visualmente -- pular frame
                savings["frame_skip"] += 640 * 480 * 3 // 10   // delta aprox
            senao:
                self.last_expression = expression
                frame_data = "WEBP_{expression}_{gesture}".encode()
                frame_b64 = base64.b64encode(frame_data).decode("ascii")
                packet.webcam = WebcamDynamic(
                    frame_b64 = frame_b64,
                    is_delta_frame = verdadeiro,
                    frame_count = 1,
                    resolution_sent = "640x480",  // adaptivo
                    face_detected = verdadeiro,
                    face_expression = expression,
                    face_confidence = 0.93,
                    gesture = gesture,
                    gaze_direction = gaze,
                    screen_ocr = screen_ocr,
                    compressed_bytes = tamanho(frame_b64),
                    raw_bytes = 640 * 480 * 3,
                )

        // Se nada tem dados -> HEARTBEAT
        se nao packet.has_data entao:
            packet.packet_type = PacketType.HEARTBEAT
            self.heartbeats_sent += 1

        // Checksum
        packet.checksum = packet.compute_checksum()

        // Fragmentação se necessario
        total_size = packet.payload_size_bytes
        max_bytes = self.constants.max_packet_size_kb * 1024
        fragmented = falso
        se total_size > max_bytes entao:
            fragmented = verdadeiro
            self.fragments_sent += 1

        // Stats
        self.bytes_sent += total_size
        self.bytes_saved_delta += savings["delta"]
        self.bytes_saved_silence += savings["silence"]
        self.bytes_saved_frame_skip += savings["frame_skip"]
        self.packets_sent += 1
        self.last_packet = packet

        retorne {
            "sequence": seq,
            "type": packet.packet_type.value,
            "payload_bytes": total_size,
            "fragmented": fragmented,
            "savings": savings,
            "checksum": packet.checksum,
            "has_keyboard": packet.keyboard is nao  nulo,
            "has_audio": packet.audio is nao  nulo,
            "has_webcam": packet.webcam is nao  nulo,
            packet.has_data ? "stream_mode": "active" : "heartbeat",
        }

    funcao receive_ack(self, sequence: inteiro, rtt_ms: flutuante,
                    seja backpressure: logico = falso) -> {texto: qualquer}:
        // Hermes envia ACK de recebimento.
        self.acks_received += 1
        self.rtt_history.append(rtt_ms)
        se backpressure entao:
            self.backpressure_events += 1

        retorne {
            "ack_for": sequence,
            "rtt_ms": rtt_ms,
            "backpressure": backpressure,
            "message": (
                "ACK recebido para pacote {sequence}. "
                "RTT: {rtt_ms:.0f}ms. "
                "{'BACKPRESSURE: desacelerando...' if backpressure else 'OK'}"
            ),
        }

    funcao adaptive_quality(self) -> {texto: qualquer}:
        // Adapta qualidade baseado em rede/RTT/backpressure.
        avg_rtt = soma(self.rtt_history[-10:]) / maximo(tamanho(self.rtt_history[-10:]), 1)

        adjustments = {}
        se avg_rtt > 200 entao:
            adjustments["video_fps"] = "reduzido (rede lenta)"
            adjustments["audio_bitrate"] = "16kbps (baixa banda)"
            adjustments["webcam_resolution"] = "320x240 (reduzido)"
        senao se avg_rtt > 100 entao:
            adjustments["video_fps"] = "normal"
            adjustments["audio_bitrate"] = "24kbps (normal)"
            adjustments["webcam_resolution"] = "640x480 (normal)"
        senao:
            adjustments["video_fps"] = "maximo"
            adjustments["audio_bitrate"] = "48kbps (alta qualidade)"
            adjustments["webcam_resolution"] = "1280x720 (alto)"

        se self.backpressure_events > 3 entao:
            adjustments["chunk_interval"] = "aumentado (Hermes sobrecarregado)"

        retorne {
            "avg_rtt_ms": arredonde(avg_rtt, 0),
            "adjustments": adjustments,
            "backpressure_count": self.backpressure_events,
        }

    funcao end_stream(self) -> {texto: qualquer}:
        // Encerra stream.
        retorne {
            "ended": verdadeiro,
            self.constants ? "session_id": self.constants.session_id : "?",
            "total_packets": self.packets_sent,
            "total_acks": self.acks_received,
            "total_bytes_sent": self.bytes_sent,
            "bytes_saved_delta": self.bytes_saved_delta,
            "bytes_saved_silence": self.bytes_saved_silence,
            "bytes_saved_frame_skip": self.bytes_saved_frame_skip,
            "total_saved": self.bytes_saved_delta + self.bytes_saved_silence + self.bytes_saved_frame_skip,
            "heartbeats": self.heartbeats_sent,
            "fragments": self.fragments_sent,
        }

    funcao stats(self) -> {texto: qualquer}:
        total_saved = self.bytes_saved_delta + self.bytes_saved_silence + self.bytes_saved_frame_skip
        retorne {
            self.constants ? "session": self.constants.session_id : "?",
            "packets_sent": self.packets_sent,
            "acks_received": self.acks_received,
            "bytes_sent": self.bytes_sent,
            "bytes_saved_total": total_saved,
            "efficiency_pct": "{total_saved / max(self.bytes_sent + total_saved, 1) * 100:.1f}%",
            "heartbeats": self.heartbeats_sent,
            "fragments": self.fragments_sent,
            "backpressure_events": self.backpressure_events,
            "avg_rtt_ms": arredonde(soma(self.rtt_history) / maximo(tamanho(self.rtt_history), 1), 0),
        }


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = StreamingEngine()

    imprima("=" * 80)
    imprima("  OPENDATASTRUCTURE v2 -- STREAMING COM CONSTANTES E DINAMICOS")
    imprima("  Constantes 1x. Dinamicos a cada chunk. Delta so o que mudou.")
    imprima("=" * 80)

    // === 1. HANDSHAKE (constantes enviadas 1x) ===
    imprima("\n\n  === 1. HANDSHAKE (constantes -- 1x por sessao) ===\n")
    hs = engine.handshake("cleiton", DeviceType.NOTEBOOK, NetworkType.WIFI_FAST)
    para cada (k, v) em hs.items():
        se k != "message" entao:
            imprima("  {k:<30} {v}")
    imprima("\n  {hs['message']}")
    imprima("\n  CONSTANTES DETALHADAS:")
    c = engine.constants
    imprima("    Hardware: {c.cpu_cores} cores, {c.ram_gb}GB RAM, {c.cpu_arch}")
    imprima("    Camera: {c.camera_max_resolution}@{c.camera_max_fps}fps")
    imprima("    Mic: {c.mic_sample_rate}Hz, {c.mic_bit_depth}-bit, {c.mic_channels}ch")
    imprima("    Rede: {c.network_type.value}, {c.estimated_bandwidth_mbps}Mbps, "
          "{c.estimated_latency_ms}ms latency")
    imprima("    Codecs: {c.audio_codec.value} + {c.video_codec.value}")
    imprima("    Compressao: zlib level {c.compression.value}")
    imprima("    Voice ID: {c.voice_id_hash[:16]}...")
    imprima("    E2E: key {c.encryption_key_id[:16]}...")
    imprima("    Dict: {c.compression_dict_hash[:16]}...")
    imprima("    STT local: {c.can_do_stt_local}")
    imprima("    VAD local: {c.can_do_vad_local}")
    imprima("    Face detect local: {c.can_do_face_detect}")
    imprima("    Max packet: {c.max_packet_size_kb}KB")
    imprima("    Chunk interval: {c.stream_chunk_interval_ms}ms")
    imprima("    Heartbeat: {c.heartbeat_interval_sec}s")
    imprima("    Tamanho constantes: {c.estimated_size_bytes} bytes (1x)")

    // === 2. STREAM DE PACOTES (dinamicos) ===
    imprima("\n\n  === 2. STREAM DE PACOTES (dinamicos) ===\n")

    // Pacote 1: texto + voz + webcam (combo completo)
    r1 = engine.send_data(
        text = "Desenvolva o OpenMetaCognition",
        audio_transcription = "com foco em auto-consciencia",
        audio_ambient = "escritorio",
        expression = "focado",
        context = "trabalhando",
    )
    imprima("  [SEQ {r1['sequence']}] {r1['type']}: {r1['payload_bytes']}B")
    imprima("    KB={r1['has_keyboard']} AU={r1['has_audio']} WC={r1['has_webcam']}")
    imprima("    Savings: {r1['savings']}")

    // Pacote 2: mesmo texto (delta -- nada mudou)
    r2 = engine.send_data(
        text = "Desenvolva o OpenMetaCognition",
        audio_silence = verdadeiro, // silencio -- VAD local
        expression = "focado",  // mesma expressao -- frame skip
        context = "trabalhando",
    )
    imprima("\n  [SEQ {r2['sequence']}] {r2['type']}: {r2['payload_bytes']}B")
    imprima("    Delta aplicado: texto igual -> pular")
    imprima("    Silencio: audio nao enviado (VAD local)")
    imprima("    Frame skip: webcam nao mudou -> pular")
    imprima("    Savings: {r2['savings']}")

    // Pacote 3: so voz (comando por voz)
    r3 = engine.send_data(
        audio_transcription = "Hermes, cria modulo novo",
        audio_ambient = "escritorio",
        expression = "focado",
        context = "trabalhando",
        priority = 3,
    )
    imprima("\n  [SEQ {r3['sequence']}] {r3['type']}: {r3['payload_bytes']}B")
    imprima("    Voz: 'Hermes, cria modulo novo'")
    imprima("    Prioridade: {3} (mais alta)")

    // Pacote 4: silencio total -> HEARTBEAT
    r4 = engine.send_data(context="pensando")
    imprima("\n  [SEQ {r4['sequence']}] {r4['type']}: HEARTBEAT (idle)")
    imprima("    Nada mudou. Minimal packet. Mantem conexao.")

    // Pacote 5: novo texto
    r5 = engine.send_data(
        text = "Desenvolva o OpenDataStructure v2",
        expression = "focado",
        context = "trabalhando",
    )
    imprima("\n  [SEQ {r5['sequence']}] {r5['type']}: {r5['payload_bytes']}B")
    imprima("    Texto novo (delta detecta mudanca)")

    // === 3. ACK DO HERMES ===
    imprima("\n\n  === 3. ACK DO HERMES ===\n")
    ack1 = engine.receive_ack(1, rtt_ms=18.5)
    ack3 = engine.receive_ack(3, rtt_ms=22.0)
    imprima("  {ack1['message']}")
    imprima("  {ack3['message']}")

    // === 4. BACKPRESSURE ===
    imprima("\n\n  === 4. BACKPRESSURE (Hermes sobrecarregado) ===\n")
    ack_bp = engine.receive_ack(5, rtt_ms=350.0, backpressure=verdadeiro)
    imprima("  {ack_bp['message']}")
    adapt = engine.adaptive_quality()
    imprima("  RTT medio: {adapt['avg_rtt_ms']}ms")
    para cada (k, v) em adapt["adjustments"].items():
        imprima("    {k}: {v}")

    // === 5. CONSTANTES vs DINAMICOS (economia) ===
    imprima("\n\n  === 5. CONSTANTES vs DINAMICOS (economia de banda) ===\n")
    imprima("  {'Tipo':<25} {'Frequencia':<20} {'Tamanho':<15} {'Total/sessao'}")
    imprima("  {'-'*70}")
    imprima("  {'Constantes (handshake)':<25} {'1x por sessao':<20} "
          "{'~800B':<15} {'800B'}")
    imprima("  {'Dinamicos (stream)':<25} {'a cada 100ms':<20} "
          "{'~200-2000B':<15} {'varia'}")
    imprima("  {'Delta (so mudanca)':<25} {'quando muda':<20} "
          "{'~0-500B':<15} {'muito menos'}")
    imprima("  {'Heartbeat (idle)':<25} {'a cada 30s':<20} "
          "{'~50B':<15} {'minimo'}")

    imprima("\n  ECONOMIA:")
    imprima("  Sem constantes: cada pacote levaria ~800B extra = desperdicio")
    imprima("  Com constantes (1x): 800B uma vez. Resto so dinamicos.")
    imprima("  Em 1h de sessao (36000 pacotes): {36000 * 800:,}B economizados")

    // === 6. STATS ===
    imprima("\n\n  === 6. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === 7. ENCERRAR ===
    imprima("\n\n  === 7. ENCERRAR STREAM ===\n")
    end = engine.end_stream()
    para cada (k, v) em end.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA: CONSTANTES vs DINAMICOS")
    imprima("{'='*80}")
    imprima("""
  O QUE SAO CONSTANTES (previsiveis):
    Dados que nao MUDAM durante a sessao.
    Enviados UMA VEZ no handshake. Hermes guarda.

    - Perfil: user_id, idioma, timezone
    - Hardware: CPU, RAM, camera, mic, tela
    - Rede: bandwidth, latencia, protocolo
    - Codecs: OPUS, WEBP, zlib
    - Voice ID: fingerprint vocal (192 dimensoes)
    - Capacidades: STT local? VAD local? Face detect local?
    - Limites: maximo packet size, chunk interval, heartbeat

    POR QUE SEPARAR:
    Sem separacao: cada pacote leva ~800B de metadados repetidos.
    Com separacao: 800B UMA VEZ. Resto so dados dinamicos.
    Em 1h: 28.8MB economizados SO de metadados.

  O QUE SAO DINAMICOS (variaveis):
    Dados que MUDAM a cada pacote.
    Enviados a cada chunk (100ms).

    - Texto digitado (muda quando usuario digita)
    - Audio capturado (muda continuamente)
    - Frames webcam (muda quando algo se move)
    - Timestamp (sempre muda)
    - Prioridade (pode mudar: normal -> critico)
    - Contexto (pode mudar: trabalhando -> descansando)

  O QUE SAO DELTAS (so o que mudou):
    Dentro dos dinamicos, so enviar o que MUDOU desde ultimo pacote.

    - Texto igual ao ultimo? Nao enviar.
    - Audio em silencio (VAD)? Nao enviar.
    - Webcam sem mudanca visual? Nao enviar frame.
    - Expressao facial igual? Pular.
    - Ambiente sonoro igual? Pular.

    Resultado: pacotes MINIMOS quando nada muda.
    Heartbeat de 50B em vez de 2000B.

  DETALHES TECNICOS QUE FALTAVAM (previsiveis):
    1. SEQUENCE NUMBER: pacotes numerados (ordem garantida)
    2. ACK/NACK: Hermes confirma cada pacote
    3. BACKPRESSURE: Hermes pede para desacelerar se sobrecarregado
    4. HEARTBEAT: idle envia minimal (conexao nao cai)
    5. CHECKSUM: integridade (SHA-256 do payload)
    6. FRAGMENTATION: pacote >64KB quebra em fragmentos
    7. ADAPTIVE QUALITY: RTT alto = menos fps/resolucao/bitrate
    8. ENCRYPTION: E2E (P2 privacidade -- dados do corpo)
    9. COMPRESSION DICT: dicionario pre-compartilhado (melhor compressao)
    10. RTT MEASUREMENT: mede latencia em tempo real
    11. BANDWIDTH TRACKING: tracks banda usada por pacote
    12. SILENCE SKIP: VAD local evita enviar silencio
    13. FRAME SKIP: webcam sem mudanca nao envia frame
    14. TEXT DELTA: texto repetido nao reenviado
    15. CAPABILITY FLAGS: STT/VAD/Face local ou remoto

  PROCESSAMENTO LOCAL vs REMOTO:
    CONSTANTES definem o que o dispositivo PODE fazer local:
    - can_do_stt_local: transcreve voz NO dispositivo (economiza banda)
    - can_do_vad_local: detecta silencio NO dispositivo (nao envia)
    - can_do_face_detect: detecta face NO dispositivo (so envia resultado)

    Se dispositivo e fraco (terminal burro): tudo remoto (mais banda)
    Se dispositivo e forte (notebook): muito local (menos banda)

  FLUXO COMPLETO:
    1. HANDSHAKE: constantes (1x, ~800B)
    2. Hermes confirma config
    3. STREAM: pacotes dinamicos a cada 100ms
       - Delta so o que mudou
       - Silencio/sem-mudanca = heartbeat
       - ACK/NACK do Hermes
       - Backpressure se necessario
       - Adaptive quality baseado em RTT
    4. END: encerra, estatisticas finais

  PRINCIPIOS:
    P1: Constantes transparentes. Usuario sabe o que envia.
    P2: Dados do corpo (audio/webcam) sao E2E. Privacidade total.
    seja P3: Delta = eficiencia. Menos banda = mais velocidade.
    P4: Adaptive quality garante que TODOS os dispositivos funcionam.
// )
    imprima("{'='*80}")
    imprima("  OpenDataStructure v2: {s['packets_sent']} pacotes, "
          "{s['bytes_sent']}B enviados, "
          "{s['bytes_saved_total']}B economizados.")
    imprima("  Eficiencia: {s['efficiency_pct']}. Constantes 1x. Dinamicos delta.")
    imprima("{'='*80}")

```
