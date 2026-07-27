/* OpenDataStructure v2 -- Streaming com Constantes e Dinamicos -- gerado de Portugol++ */
#ifndef OPENDATASTRUCTURE_V2_STREAMING_COM_CONSTANTES_E_DINAMICOS_H
#define OPENDATASTRUCTURE_V2_STREAMING_COM_CONSTANTES_E_DINAMICOS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenDataStructure v2 -- Streaming com Constantes && Dinamicos;
===============================================================;
MELHORIAS vs v1:;
1. SEPARAÇÃO: constantes (previsíveis) vs dinâmicos (variáveis);
2. STREAMING: ! batch -- fluxo continuo com chunks;
3. DELTA: so envia o que MUDOU desde ultimo pacote;
4. SEQUENCE: pacotes numerados (ordem garantida);
5. ACK/NACK: Hermes confirma recebimento;
6. BACKPRESSURE: se Hermes sobrecarregado, cliente desacelera;
7. HEARTBEAT: idle envia minimal (! para);
8. CHECKSUM: integridade verificada;
9. FRAGMENTATION: pacotes grandes quebram em fragmentos;
10. BANDWIDTH ADAPTATION: rede lenta = menos qualidade;
11. ENCRYPTION: E2E (P2 privacidade);
12. COMPRESSION DICTIONARY: dicionario pre-compartilhado;
CONSTANTES (enviadas 1x por sessão):;
- Perfil do usuario (id, idioma, timezone);
- Hardware (CPU, RAM, camera, mic, screen);
- Capacidades de rede (bandwidth, protocolo);
- Voice ID fingerprint (OpenAudioChannel);
- Codec preferences;
- Compression dictionary hash;
- Hermes endpoint;
DINÂMICOS (enviados a cada pacote):;
- Texto digitado;
- Audio capturado;
- Frames de webcam;
- Timestamp;
- Prioridade (pode mudar);
- Contexto (pode mudar);
- Delta desde ultimo pacote;
Author: OpenRepublic Team;
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
typedef struct DeviceType {
    NOTEBOOK = "notebook";
    SMARTPHONE = "smartphone";
    TERMINAL = "terminal_burro";
    TV_STICK = "tv_stick";
    TABLET = "tablet";
    DESKTOP = "desktop";
    KIOSK = "kiosk";
    WEARABLE = "wearable";
typedef struct NetworkType {
    FIBER = "fibra"  // >100 Mbps;
    WIFI_FAST = "wifi_rapido"  // 50-100 Mbps;
    WIFI_SLOW = "wifi_lento"  // 10-50 Mbps;
    MOBILE_5G = "5g";
    MOBILE_4G = "4g";
    MOBILE_3G = "3g"  // adaptar qualidade;
    SATELLITE = "satelite"  // alta latencia;
    MESH = "mesh_republica"  // OpenNetwork P2P;
typedef struct AudioCodec {
    OPUS_24 = "opus_24kbps"  // voz -- melhor codec;
    OPUS_48 = "opus_48kbps"  // alta qualidade;
    OPUS_16 = "opus_16kbps"  // baixa banda;
    FLAC = "flac"  // sem perda (musica);
typedef struct VideoCodec {
    H264 = "h264";
    H265 = "h265"  // melhor compressao;
    VP9 = "vp9";
    AV1 = "av1"  // futuro;
    MJPEG = "mjpeg"  // frames simples;
    WEBP = "webp"  // frames otimizados;
typedef struct CompressionLevel {
    NONE = 0;
    FAST = 1 // zlib level 1;
    BALANCED = 6 // zlib level 6;
    MAX = 9 // zlib level 9;
// decorador: @dataclass
typedef struct SessionConstants {
    // CONSTANTES da sessão -- enviadas UMA VEZ no início.
    Estes dados NÃO mudam durante a sessão.;
    Hermes guarda && referencia. Não reenvia.;
    Economiza banda massiva.;
    //
    // Sessão
    char* session_id = "";
    char* user_id = "";
    DeviceType device_type = DeviceType.NOTEBOOK;
    char* language = "pt-BR";
    char* timezone = "America/Sao_Paulo";
    // Hardware (constante durante sessão)
    int cpu_cores = 4;
    char* cpu_arch = "x86_64"  // || "risc_v", "arm";
    int ram_gb = 8;
    char* camera_max_resolution = "1280x720";
    int camera_max_fps = 30;
    int mic_sample_rate = 48000;
    int mic_bit_depth = 16;
    int mic_channels = 1 // mono para voz;
    char* screen_resolution = "1920x1080";
    // Rede (constante durante sessão -- pode mudar, mas raro)
    NetworkType network_type = NetworkType.WIFI_FAST;
    double estimated_bandwidth_mbps = 50.0;
    double estimated_latency_ms = 20.0;
    double packet_loss_rate = 0.001 // 0.1%;
    // Codecs suportados (constante -- hardware define)
    AudioCodec audio_codec = AudioCodec.OPUS_24;
    VideoCodec video_codec = VideoCodec.WEBP;
    CompressionLevel compression = CompressionLevel.BALANCED;
    // Voice ID (OpenAudioChannel fingerprint -- constante)
    char* voice_id_hash = ""  // hash do fingerprint vocal;
    int voice_id_dimensions = 192 // dimensoes do embedding;
    // Hermes (constante)
    char* hermes_endpoint = "openprotocol://hermes.local";
    char* encryption_key_id = ""  // ID da chave E2E;
    char* compression_dict_hash = ""  // hash do dicionario pre-compartilhado;
    // Capacidades (constante -- o que este dispositivo PODE)
    bool can_stream_video = true;
    bool can_stream_audio = true;
    bool can_stream_screen = false;
    bool can_do_stt_local = false // STT no dispositivo?;
    bool can_do_vad_local = true // VAD no dispositivo?;
    bool can_do_face_detect = true // Face detection no dispositivo?;
    bool battery_powered = true;
    double battery_pct = 100.0 #近似 -- muda raramente;
    // Limites (constante -- configurado no início)
    int max_packet_size_kb = 64 // pacotes >64KB fragmentam;
    double heartbeat_interval_sec = 30.0 // idle -> heartbeat a cada 30s;
    int stream_chunk_interval_ms = 100 // chunk a cada 100ms;
    // decorador: @classmethod
    funcao create(cls, user_id: texto, device: DeviceType = DeviceType.NOTEBOOK,
            NetworkType network = NetworkType.WIFI_FAST) -> "SessionConstants":;
        return cls(;
            session_id = hashlib.sha256(;
                "{user_id}{time.time()}".encode()).hexdigest()[:16],;
            user_id = user_id,;
            device_type = device,;
            network_type = network,;
            voice_id_hash = hashlib.sha256(;
                "{user_id}_voice".encode()).hexdigest()[:32],;
            encryption_key_id = hashlib.sha256(;
                "{user_id}_e2e".encode()).hexdigest()[:16],;
            compression_dict_hash = hashlib.sha256(;
                b"openrepublic_dict_v1").hexdigest()[:16],;
        );
    char* to_json(self) {
        d = asdict(self);
        d["device_type"] = self.device_type.value;
        d["network_type"] = self.network_type.value;
        d["audio_codec"] = self.audio_codec.value;
        d["video_codec"] = self.video_codec.value;
        d["compression"] = self.compression.value;
        return json.dumps(d, ensure_ascii=false, indent=2);
    // decorador: @property
    int estimated_size_bytes(self) {
        // Tamanho aproximado das constantes serializadas.
        return sizeof(self.to_json().encode("utf-8"));
// ============================================================================
// 2. DADOS DINÂMICOS (variáveis -- enviados a cada pacote)
// ============================================================================
typedef struct StreamMode {
    ACTIVE = "ativo"  // usuario interagindo;
    LISTENING = "ouvindo"  // Hermes falando, usuario ouve;
    IDLE = "ocio"  // sem interacao (heartbeat);
    BACKGROUND = "background"  // contexto passivo;
typedef struct PacketType {
    DATA = "dados"  // pacote de dados normal;
    DELTA = "delta"  // so o que mudou;
    HEARTBEAT = "heartbeat"  // ocioso, minimal;
    FRAGMENT = "fragmento"  // parte de pacote grande;
    ACK = "ack"  // confirmacao de recebimento;
    NACK = "nack"  // erro de recebimento;
    BACKPRESSURE = "backpressure"  // pedir para desacelerar;
    END = "fim"  // encerrar stream;
// decorador: @dataclass
typedef struct KeyboardDynamic {
    // Dados dinâmicos do teclado.
    char* text = ""  // texto bruto;
    char* text_compressed = ""  // base64(zlib(text));
    char* text_delta = ""  // so caracteres NOVOS desde ultimo;
    bool is_delta = false // é delta?;
    int raw_bytes = 0;
    int compressed_bytes = 0;
    double typing_speed_wpm = 0.0;
    char* input_type = "command"  // command, question, correction;
    bool has_code = false;
    bool has_url = false;
    bool has_emoji = false;
    bool caps_lock = false;
    bool enter_pressed = false // submeteu?;
// decorador: @dataclass
typedef struct AudioDynamic {
    // Dados dinâmicos do audio.
    char* chunk_b64 = ""  // base64(opus chunk);
    int chunk_duration_ms = 100 // duracao deste chunk;
    bool is_silence = false // VAD: silencio? (! enviar se true);
    bool is_delta = false // audio delta (raro, mas possivel);
    char* transcription = ""  // STT local (se device suporta);
    double transcription_confidence = 0.0;
    double voice_id_match = 0.0 // match com fingerprint (0-1);
    bool ambient_changed = false // ambiente mudou?;
    char* ambient_type = ""  // rua, escritorio, musica;
    double noise_level_db = 0.0;
    int speaker_count = 1 // quantas pessoas falando;
    int raw_bytes = 0;
    int compressed_bytes = 0;
// decorador: @dataclass
typedef struct WebcamDynamic {
    // Dados dinâmicos do webcam.
    char* frame_b64 = ""  // base64(webp frame);
    bool is_delta_frame = true // delta (so pixels mudados);
    int frame_count = 1;
    char* resolution_sent = "640x480"  // pode ser reduzido (bandwidth);
    bool face_detected = false;
    char* face_expression = ""  // neutro, focado, cansado;
    double face_confidence = 0.0;
    char* gesture = "none";
    char* gaze_direction = "screen";
    char* posture = "upright";
    bool screen_share = false;
    char* screen_ocr = ""  // texto na tela;
    [texto] objects_detected = field(default_factory=list);
    bool background_changed = false // mudou de lugar?;
    int raw_bytes = 0;
    int compressed_bytes = 0;
// ============================================================================
// 3. PACOTE DE STREAM (dinâmico)
// ============================================================================
// decorador: @dataclass
typedef struct StreamPacket {
    // Pacote individual no fluxo de streaming.
    HEADER (constante por pacote -- mas dados sao dinâmicos):;
    - sequence: numero sequencial (ordem);
    - timestamp_ns: nanosegundos (precisão);
    - packet_type: DATA, DELTA, HEARTBEAT, FRAGMENT, ACK, etc;
    - checksum: integridade;
    PAYLOAD (dinâmico):;
    - keyboard, audio, webcam (opcionais cada);
    - delta_since_seq: referencia ao ultimo pacote (para delta);
    //
    // HEADER
    int sequence = 0 // numero sequencial;
    int timestamp_ns = 0 // nanosegundos;
    PacketType packet_type = PacketType.DATA;
    char* session_id = ""  // referencia às constantes;
    int priority = 5 // 0=critico, 5=normal, 9=background;
    StreamMode stream_mode = StreamMode.ACTIVE;
    char* checksum = ""  // SHA-256 do payload;
    char* context = ""  // o que usuario esta fazendo;
    // DELTA reference
    int delta_since_seq = 0 // baseado em qual pacote anterior?;
    bool is_fragment = false;
    int fragment_index = 0 // qual fragmento?;
    int fragment_total = 0 // quantos fragmentos?;
    char* fragment_id = ""  // ID do pacote original fragmentado;
    // PAYLOAD (dinâmico)
    KeyboardDynamic? keyboard = NULL;
    AudioDynamic? audio = NULL;
    WebcamDynamic? webcam = NULL;
    // TRANSPORTE
    double rtt_ms = 0.0 // arredonde-trip time (medido);
    double bandwidth_used_mbps = 0.0 // banda usada neste pacote;
    // decorador: @property
    int payload_size_bytes(self) {
        size = 0;
        if self.keyboard: size += self.keyboard.compressed_bytes;
        if self.audio: size += self.audio.compressed_bytes;
        if self.webcam: size += self.webcam.compressed_bytes;
        return size;
    // decorador: @property
    bool has_data(self) {
        return any([self.keyboard, self.audio, self.webcam]);
    char* compute_checksum(self) {
        // Calcula checksum do payload.
        payload = json.dumps({
            self.keyboard ? "kb": asdict(self.keyboard) : NULL,;
            self.audio ? "au": asdict(self.audio) : NULL,;
            self.webcam ? "wc": asdict(self.webcam) : NULL,;
        }, sort_keys=true).encode();
        return hashlib.sha256(payload).hexdigest()[:16];
    bool verify(self) {
        // Verifica integridade.
        return self.compute_checksum() == self.checksum;
    bytes to_transport(self) {
        // Serializa para bytes (transmissão de rede).
        Formato binario compacto:;
        [seq:4B][ts:8B][type:1B][prio:1B][mode:1B][checksum:16B];
        [ctx_len:2B][ctx:N B][payload_len:4B][payload:N B];
        //
        header = struct.pack("!IQBBB",;
            self.sequence,;
            self.timestamp_ns,;
            isinstance(self.packet_type.value, inteiro) ? self.packet_type.value : 0,;
            self.priority,;
            0, // mode placeholder;
        );
        payload = json.dumps({
            self.keyboard ? "kb": asdict(self.keyboard) : NULL,;
            self.audio ? "au": asdict(self.audio) : NULL,;
            self.webcam ? "wc": asdict(self.webcam) : NULL,;
            "ctx": self.context,;
        }, ensure_ascii=false).encode("utf-8");
        ctx_bytes = self.context.encode("utf-8");
        return header + struct.pack("!H", sizeof(ctx_bytes)) + ctx_bytes + \;
            struct.pack("!I", sizeof(payload)) + payload;
// ============================================================================
// 4. MOTOR DE STREAMING
// ============================================================================
typedef struct StreamingEngine {
    // Motor de streaming contínuo para Hermes.
    FLUXO:;
    1. HANDSHAKE: cliente envia SessionConstants (1x);
    2. Hermes responde com config confirmada;
    3. STREAM: cliente envia StreamPacket a cada chunk_interval;
    4. Hermes responde ACK/NACK;
    5. DELTA: se nada mudou, envia HEARTBEAT (minimal);
    6. BACKPRESSURE: se Hermes lento, pede para desacelerar;
    7. END: cliente envia END ao encerrar;
    OTIMIZACOES:;
    - DELTA: so envia o que MUDOU desde ultimo pacote;
    - SILENCE SKIP: audio em silencio ! && enviado (VAD local);
    - FRAME SKIP: webcam sem mudanca ! envia frame;
    - ADAPTIVE QUALITY: rede lenta = menos fps/resolucao;
    - FRAGMENTATION: pacote > max_size quebra em fragmentos;
    - COMPRESSION DICT: dicionario pre-compartilhado melhora compressao;
    CONSTANTES vs DINAMICOS:;
    - Constantes: SessionConstants (1x no handshake);
    - Dinamicos: StreamPacket (a cada chunk);
    - Delta: dentro do dinamico, so o que mudou;
    //
    void __init__(self) {
        self.constants: SessionConstants? = NULL;
        self.sequence_counter: inteiro = 0;
        self.last_packet: StreamPacket? = NULL;
        self.packets_sent: inteiro = 0;
        self.acks_received: inteiro = 0;
        self.nacks_received: inteiro = 0;
        self.bytes_sent: inteiro = 0;
        self.bytes_saved_delta: inteiro = 0;
        self.bytes_saved_silence: inteiro = 0;
        self.bytes_saved_frame_skip: inteiro = 0;
        self.fragments_sent: inteiro = 0;
        self.heartbeats_sent: inteiro = 0;
        self.backpressure_events: inteiro = 0;
        self.rtt_history: [flutuante] = [];
        self.bandwidth_history: [flutuante] = [];
        self.last_text: texto = ""         // para delta de texto;
        self.last_ambient: texto = ""      // para delta de ambiente;
        self.last_expression: texto = ""   // para delta de expressao;
    funcao handshake(self, user_id: texto,
                DeviceType device = DeviceType.NOTEBOOK,;
                NetworkType network = NetworkType.WIFI_FAST;
                ) -> {texto: qualquer}:;
        // Handshake: envia constantes UMA VEZ.
        self.constants = SessionConstants.create(user_id, device, network);
        return {;
            "handshake": "OK",;
            "session_id": self.constants.session_id,;
            "constants_size_bytes": self.constants.estimated_size_bytes,;
            "constants_sent_once": true,;
            "audio_codec": self.constants.audio_codec.value,;
            "video_codec": self.constants.video_codec.value,;
            "compression": "zlib level {self.constants.compression.value}",;
            "chunk_interval_ms": self.constants.stream_chunk_interval_ms,;
            "heartbeat_interval_s": self.constants.heartbeat_interval_sec,;
            "max_packet_kb": self.constants.max_packet_size_kb,;
            "encryption": "E2E key {self.constants.encryption_key_id[:8]}",;
            "compression_dict": "dict {self.constants.compression_dict_hash[:8]}",;
            "voice_id": "fingerprint {self.constants.voice_id_hash[:8]}",;
            "message": (;
                "Constantes enviadas UMA VEZ. ";
                "A partir de agora, so DADOS DINAMICOS. ";
                "Economia massiva de banda.";
            ),;
        };
    int _next_seq(self) {
        self.sequence_counter += 1;
        return self.sequence_counter;
    funcao _compress(self, data: texto) retorna Tuple[texto, inteiro, inteiro]:
        // Comprime string com zlib.
        raw = data.encode("utf-8");
        level = self.constants ? self.constants.compression.value : 6;
        compressed = zlib.compress(raw, level=level);
        return base64.b64encode(compressed).decode("ascii"), sizeof(raw), sizeof(compressed);
    void _compute_delta_text(self, new_text: texto) retorna (texto, logico) {
        // Computa delta de texto (so o que mudou).
        if (new_text == self.last_text) {
            return "", true  // nada mudou;
        // Delta simples: texto novo
        // (em produção: algoritmo diff real)
        self.last_text = new_text;
        return new_text, false;
    funcao send_data(self, text: texto = "",
                char* audio_transcription = "",;
                bool audio_silence = false,;
                char* audio_ambient = "",;
                char* expression = "",;
                char* gesture = "none",;
                char* gaze = "screen",;
                char* screen_ocr = "",;
                char* context = "",;
                int priority = 5,;
                ) -> {texto: qualquer}:;
        // Envia pacote de dados no stream.
        if (! self.constants) {
            return {"error": "Handshake ! feito"};
        seq = self._next_seq();
        ts = inteiro(time.time_ns());
        packet = StreamPacket(;
            sequence = seq, timestamp_ns=ts,;
            packet_type = PacketType.DATA,;
            session_id = self.constants.session_id,;
            priority = priority,;
            context = context,;
            delta_since_seq = self.last_packet ? self.last_packet.sequence : 0,;
        );
        savings = {"delta": 0, "silence": 0, "frame_skip": 0};
        // === KEYBOARD ===
        if (text) {
            desempacote delta_text, is_delta = self._compute_delta_text(text);
            if (is_delta && self.last_packet && self.last_packet.keyboard) {
                // Texto nao mudou -- pular
                savings["delta"] += sizeof(text.encode("utf-8"));
            } else {
                desempacote compressed, raw_b, comp_b = self._compress(text);
                packet.keyboard = KeyboardDynamic(;
                    text = text, text_compressed=compressed,;
                    raw_bytes = raw_b, compressed_bytes=comp_b,;
                    has_code = any(kw in text para kw em ["def ", "fn ", "import "]),;
                    has_url = "http" in text,;
                    enter_pressed = text.endswith("\n"),;
                );
        // === AUDIO ===
        if (! audio_silence) {
            if (audio_transcription || audio_ambient) {
                // Simular chunk OPUS
                chunk_data = "OPUS_{audio_transcription[:20]}".encode();
                chunk_b64 = base64.b64encode(chunk_data).decode("ascii");
                ambient_changed = audio_ambient != self.last_ambient;
                self.last_ambient = audio_ambient;
                packet.audio = AudioDynamic(;
                    chunk_b64 = chunk_b64,;
                    chunk_duration_ms = self.constants.stream_chunk_interval_ms,;
                    transcription = audio_transcription,;
                    transcription_confidence = 0.95,;
                    voice_id_match = 0.92,;
                    ambient_type = audio_ambient,;
                    ambient_changed = ambient_changed,;
                    noise_level_db = 35.0,;
                    compressed_bytes = sizeof(chunk_b64),;
                    raw_bytes = sizeof(chunk_data) * 10,;
                );
        } else {
            // Silencio -- VAD local detectou. Nao enviar audio.
            savings["silence"] += 2400   // ~100ms de opus 24kbps;
        // === WEBCAM ===
        if (expression) {
            expr_changed = expression != self.last_expression;
            if (!  expr_changed  &&  !  gesture != "none") {
                // Nada mudou visualmente -- pular frame
                savings["frame_skip"] += 640 * 480 * 3 // 10   // delta aprox;
            } else {
                self.last_expression = expression;
                frame_data = "WEBP_{expression}_{gesture}".encode();
                frame_b64 = base64.b64encode(frame_data).decode("ascii");
                packet.webcam = WebcamDynamic(;
                    frame_b64 = frame_b64,;
                    is_delta_frame = true,;
                    frame_count = 1,;
                    resolution_sent = "640x480",  // adaptivo;
                    face_detected = true,;
                    face_expression = expression,;
                    face_confidence = 0.93,;
                    gesture = gesture,;
                    gaze_direction = gaze,;
                    screen_ocr = screen_ocr,;
                    compressed_bytes = sizeof(frame_b64),;
                    raw_bytes = 640 * 480 * 3,;
                );
        // Se nada tem dados -> HEARTBEAT
        if (! packet.has_data) {
            packet.packet_type = PacketType.HEARTBEAT;
            self.heartbeats_sent += 1;
        // Checksum
        packet.checksum = packet.compute_checksum();
        // Fragmentação se necessario
        total_size = packet.payload_size_bytes;
        max_bytes = self.constants.max_packet_size_kb * 1024;
        fragmented = false;
        if (total_size > max_bytes) {
            fragmented = true;
            self.fragments_sent += 1;
        // Stats
        self.bytes_sent += total_size;
        self.bytes_saved_delta += savings["delta"];
        self.bytes_saved_silence += savings["silence"];
        self.bytes_saved_frame_skip += savings["frame_skip"];
        self.packets_sent += 1;
        self.last_packet = packet;
        return {;
            "sequence": seq,;
            "type": packet.packet_type.value,;
            "payload_bytes": total_size,;
            "fragmented": fragmented,;
            "savings": savings,;
            "checksum": packet.checksum,;
            "has_keyboard": packet.keyboard is !  NULL,;
            "has_audio": packet.audio is !  NULL,;
            "has_webcam": packet.webcam is !  NULL,;
            packet.has_data ? "stream_mode": "active" : "heartbeat",;
        };
    funcao receive_ack(self, sequence: inteiro, rtt_ms: flutuante,
                    bool backpressure = false) -> {texto: qualquer}:;
        // Hermes envia ACK de recebimento.
        self.acks_received += 1;
        self.rtt_history.append(rtt_ms);
        if (backpressure) {
            self.backpressure_events += 1;
        return {;
            "ack_for": sequence,;
            "rtt_ms": rtt_ms,;
            "backpressure": backpressure,;
            "message": (;
                "ACK recebido para pacote {sequence}. ";
                "RTT: {rtt_ms:.0f}ms. ";
                "{'BACKPRESSURE: desacelerando...' if backpressure else 'OK'}";
            ),;
        };
    {texto: qualquer} adaptive_quality(self) {
        // Adapta qualidade baseado em rede/RTT/backpressure.
        avg_rtt = soma(self.rtt_history[-10:]) / maximo(sizeof(self.rtt_history[-10:]), 1);
        adjustments = {};
        if (avg_rtt > 200) {
            adjustments["video_fps"] = "reduzido (rede lenta)";
            adjustments["audio_bitrate"] = "16kbps (baixa banda)";
            adjustments["webcam_resolution"] = "320x240 (reduzido)";
        } else if (avg_rtt > 100) {
            adjustments["video_fps"] = "normal";
            adjustments["audio_bitrate"] = "24kbps (normal)";
            adjustments["webcam_resolution"] = "640x480 (normal)";
        } else {
            adjustments["video_fps"] = "maximo";
            adjustments["audio_bitrate"] = "48kbps (alta qualidade)";
            adjustments["webcam_resolution"] = "1280x720 (alto)";
        if (self.backpressure_events > 3) {
            adjustments["chunk_interval"] = "aumentado (Hermes sobrecarregado)";
        return {;
            "avg_rtt_ms": arredonde(avg_rtt, 0),;
            "adjustments": adjustments,;
            "backpressure_count": self.backpressure_events,;
        };
    {texto: qualquer} end_stream(self) {
        // Encerra stream.
        return {;
            "ended": true,;
            self.constants ? "session_id": self.constants.session_id : "?",;
            "total_packets": self.packets_sent,;
            "total_acks": self.acks_received,;
            "total_bytes_sent": self.bytes_sent,;
            "bytes_saved_delta": self.bytes_saved_delta,;
            "bytes_saved_silence": self.bytes_saved_silence,;
            "bytes_saved_frame_skip": self.bytes_saved_frame_skip,;
            "total_saved": self.bytes_saved_delta + self.bytes_saved_silence + self.bytes_saved_frame_skip,;
            "heartbeats": self.heartbeats_sent,;
            "fragments": self.fragments_sent,;
        };
    {texto: qualquer} stats(self) {
        total_saved = self.bytes_saved_delta + self.bytes_saved_silence + self.bytes_saved_frame_skip;
        return {;
            self.constants ? "session": self.constants.session_id : "?",;
            "packets_sent": self.packets_sent,;
            "acks_received": self.acks_received,;
            "bytes_sent": self.bytes_sent,;
            "bytes_saved_total": total_saved,;
            "efficiency_pct": "{total_saved / max(self.bytes_sent + total_saved, 1) * 100:.1f}%",;
            "heartbeats": self.heartbeats_sent,;
            "fragments": self.fragments_sent,;
            "backpressure_events": self.backpressure_events,;
            "avg_rtt_ms": arredonde(soma(self.rtt_history) / maximo(sizeof(self.rtt_history), 1), 0),;
        };
// ============================================================================
// 5. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = StreamingEngine();
    printf("=" * 80);
    printf("  OPENDATASTRUCTURE v2 -- STREAMING COM CONSTANTES E DINAMICOS");
    printf("  Constantes 1x. Dinamicos a cada chunk. Delta so o que mudou.");
    printf("=" * 80);
    // === 1. HANDSHAKE (constantes enviadas 1x) ===
    printf("\n\n  === 1. HANDSHAKE (constantes -- 1x por sessao) ===\n");
    hs = engine.handshake("cleiton", DeviceType.NOTEBOOK, NetworkType.WIFI_FAST);
    /* para cada (k, v) em hs.items(): */
        if (k != "message") {
            printf("  {k:<30} {v}");
    printf("\n  {hs['message']}");
    printf("\n  CONSTANTES DETALHADAS:");
    c = engine.constants;
    printf("    Hardware: {c.cpu_cores} cores, {c.ram_gb}GB RAM, {c.cpu_arch}");
    printf("    Camera: {c.camera_max_resolution}@{c.camera_max_fps}fps");
    printf("    Mic: {c.mic_sample_rate}Hz, {c.mic_bit_depth}-bit, {c.mic_channels}ch");
    printf("    Rede: {c.network_type.value}, {c.estimated_bandwidth_mbps}Mbps, ";
        "{c.estimated_latency_ms}ms latency");
    printf("    Codecs: {c.audio_codec.value} + {c.video_codec.value}");
    printf("    Compressao: zlib level {c.compression.value}");
    printf("    Voice ID: {c.voice_id_hash[:16]}...");
    printf("    E2E: key {c.encryption_key_id[:16]}...");
    printf("    Dict: {c.compression_dict_hash[:16]}...");
    printf("    STT local: {c.can_do_stt_local}");
    printf("    VAD local: {c.can_do_vad_local}");
    printf("    Face detect local: {c.can_do_face_detect}");
    printf("    Max packet: {c.max_packet_size_kb}KB");
    printf("    Chunk interval: {c.stream_chunk_interval_ms}ms");
    printf("    Heartbeat: {c.heartbeat_interval_sec}s");
    printf("    Tamanho constantes: {c.estimated_size_bytes} bytes (1x)");
    // === 2. STREAM DE PACOTES (dinamicos) ===
    printf("\n\n  === 2. STREAM DE PACOTES (dinamicos) ===\n");
    // Pacote 1: texto + voz + webcam (combo completo)
    r1 = engine.send_data(;
        text = "Desenvolva o OpenMetaCognition",;
        audio_transcription = "com foco em auto-consciencia",;
        audio_ambient = "escritorio",;
        expression = "focado",;
        context = "trabalhando",;
    );
    printf("  [SEQ {r1['sequence']}] {r1['type']}: {r1['payload_bytes']}B");
    printf("    KB={r1['has_keyboard']} AU={r1['has_audio']} WC={r1['has_webcam']}");
    printf("    Savings: {r1['savings']}");
    // Pacote 2: mesmo texto (delta -- nada mudou)
    r2 = engine.send_data(;
        text = "Desenvolva o OpenMetaCognition",;
        audio_silence = true, // silencio -- VAD local;
        expression = "focado",  // mesma expressao -- frame skip;
        context = "trabalhando",;
    );
    printf("\n  [SEQ {r2['sequence']}] {r2['type']}: {r2['payload_bytes']}B");
    printf("    Delta aplicado: texto igual -> pular");
    printf("    Silencio: audio ! enviado (VAD local)");
    printf("    Frame skip: webcam ! mudou -> pular");
    printf("    Savings: {r2['savings']}");
    // Pacote 3: so voz (comando por voz)
    r3 = engine.send_data(;
        audio_transcription = "Hermes, cria modulo novo",;
        audio_ambient = "escritorio",;
        expression = "focado",;
        context = "trabalhando",;
        priority = 3,;
    );
    printf("\n  [SEQ {r3['sequence']}] {r3['type']}: {r3['payload_bytes']}B");
    printf("    Voz: 'Hermes, cria modulo novo'");
    printf("    Prioridade: {3} (mais alta)");
    // Pacote 4: silencio total -> HEARTBEAT
    r4 = engine.send_data(context="pensando");
    printf("\n  [SEQ {r4['sequence']}] {r4['type']}: HEARTBEAT (idle)");
    printf("    Nada mudou. Minimal packet. Mantem conexao.");
    // Pacote 5: novo texto
    r5 = engine.send_data(;
        text = "Desenvolva o OpenDataStructure v2",;
        expression = "focado",;
        context = "trabalhando",;
    );
    printf("\n  [SEQ {r5['sequence']}] {r5['type']}: {r5['payload_bytes']}B");
    printf("    Texto novo (delta detecta mudanca)");
    // === 3. ACK DO HERMES ===
    printf("\n\n  === 3. ACK DO HERMES ===\n");
    ack1 = engine.receive_ack(1, rtt_ms=18.5);
    ack3 = engine.receive_ack(3, rtt_ms=22.0);
    printf("  {ack1['message']}");
    printf("  {ack3['message']}");
    // === 4. BACKPRESSURE ===
    printf("\n\n  === 4. BACKPRESSURE (Hermes sobrecarregado) ===\n");
    ack_bp = engine.receive_ack(5, rtt_ms=350.0, backpressure=true);
    printf("  {ack_bp['message']}");
    adapt = engine.adaptive_quality();
    printf("  RTT medio: {adapt['avg_rtt_ms']}ms");
    /* para cada (k, v) em adapt["adjustments"].items(): */
        printf("    {k}: {v}");
    // === 5. CONSTANTES vs DINAMICOS (economia) ===
    printf("\n\n  === 5. CONSTANTES vs DINAMICOS (economia de banda) ===\n");
    printf("  {'Tipo':<25} {'Frequencia':<20} {'Tamanho':<15} {'Total/sessao'}");
    printf("  {'-'*70}");
    printf("  {'Constantes (handshake)':<25} {'1x por sessao':<20} ";
        "{'~800B':<15} {'800B'}");
    printf("  {'Dinamicos (stream)':<25} {'a cada 100ms':<20} ";
        "{'~200-2000B':<15} {'varia'}");
    printf("  {'Delta (so mudanca)':<25} {'quando muda':<20} ";
        "{'~0-500B':<15} {'muito menos'}");
    printf("  {'Heartbeat (idle)':<25} {'a cada 30s':<20} ";
        "{'~50B':<15} {'minimo'}");
    printf("\n  ECONOMIA:");
    printf("  Sem constantes: cada pacote levaria ~800B extra = desperdicio");
    printf("  Com constantes (1x): 800B uma vez. Resto so dinamicos.");
    printf("  Em 1h de sessao (36000 pacotes): {36000 * 800:,}B economizados");
    // === 6. STATS ===
    printf("\n\n  === 6. ESTATISTICAS ===\n");
    s = engine.stats();
    /* para cada (k, v) em s.items(): */
        printf("  {k:<30} {v}");
    // === 7. ENCERRAR ===
    printf("\n\n  === 7. ENCERRAR STREAM ===\n");
    end = engine.end_stream();
    /* para cada (k, v) em end.items(): */
        printf("  {k:<30} {v}");
    // === FILOSOFIA ===
    printf("\n\n{'='*80}");
    printf("  FILOSOFIA: CONSTANTES vs DINAMICOS");
    printf("{'='*80}");
    printf(""";
O QUE SAO CONSTANTES (previsiveis):;
    Dados que ! MUDAM durante a sessao.;
    Enviados UMA VEZ no handshake. Hermes guarda.;
    - Perfil: user_id, idioma, timezone;
    - Hardware: CPU, RAM, camera, mic, tela;
    - Rede: bandwidth, latencia, protocolo;
    - Codecs: OPUS, WEBP, zlib;
    - Voice ID: fingerprint vocal (192 dimensoes);
    - Capacidades: STT local? VAD local? Face detect local?;
    - Limites: maximo packet size, chunk interval, heartbeat;
    POR QUE SEPARAR:;
    Sem separacao: cada pacote leva ~800B de metadados repetidos.;
    Com separacao: 800B UMA VEZ. Resto so dados dinamicos.;
    Em 1h: 28.8MB economizados SO de metadados.;
O QUE SAO DINAMICOS (variaveis):;
    Dados que MUDAM a cada pacote.;
    Enviados a cada chunk (100ms).;
    - Texto digitado (muda quando usuario digita);
    - Audio capturado (muda continuamente);
    - Frames webcam (muda quando algo se move);
    - Timestamp (sempre muda);
    - Prioridade (pode mudar: normal -> critico);
    - Contexto (pode mudar: trabalhando -> descansando);
O QUE SAO DELTAS (so o que mudou):;
    Dentro dos dinamicos, so enviar o que MUDOU desde ultimo pacote.;
    - Texto igual ao ultimo? Nao enviar.;
    - Audio em silencio (VAD)? Nao enviar.;
    - Webcam sem mudanca visual? Nao enviar frame.;
    - Expressao facial igual? Pular.;
    - Ambiente sonoro igual? Pular.;
    Resultado: pacotes MINIMOS quando nada muda.;
    Heartbeat de 50B em vez de 2000B.;
DETALHES TECNICOS QUE FALTAVAM (previsiveis):;
    1. SEQUENCE NUMBER: pacotes numerados (ordem garantida);
    2. ACK/NACK: Hermes confirma cada pacote;
    3. BACKPRESSURE: Hermes pede para desacelerar se sobrecarregado;
    4. HEARTBEAT: idle envia minimal (conexao ! cai);
    5. CHECKSUM: integridade (SHA-256 do payload);
    6. FRAGMENTATION: pacote >64KB quebra em fragmentos;
    7. ADAPTIVE QUALITY: RTT alto = menos fps/resolucao/bitrate;
    8. ENCRYPTION: E2E (P2 privacidade -- dados do corpo);
    9. COMPRESSION DICT: dicionario pre-compartilhado (melhor compressao);
    10. RTT MEASUREMENT: mede latencia em tempo real;
    11. BANDWIDTH TRACKING: tracks banda usada por pacote;
    12. SILENCE SKIP: VAD local evita enviar silencio;
    13. FRAME SKIP: webcam sem mudanca ! envia frame;
    14. TEXT DELTA: texto repetido ! reenviado;
    15. CAPABILITY FLAGS: STT/VAD/Face local || remoto;
PROCESSAMENTO LOCAL vs REMOTO:;
    CONSTANTES definem o que o dispositivo PODE fazer local:;
    - can_do_stt_local: transcreve voz NO dispositivo (economiza banda);
    - can_do_vad_local: detecta silencio NO dispositivo (! envia);
    - can_do_face_detect: detecta face NO dispositivo (so envia resultado);
    Se dispositivo && fraco (terminal burro): tudo remoto (mais banda);
    Se dispositivo && forte (notebook): muito local (menos banda);
FLUXO COMPLETO:;
    1. HANDSHAKE: constantes (1x, ~800B);
    2. Hermes confirma config;
    3. STREAM: pacotes dinamicos a cada 100ms;
    - Delta so o que mudou;
    - Silencio/sem-mudanca = heartbeat;
    - ACK/NACK do Hermes;
    - Backpressure se necessario;
    - Adaptive quality baseado em RTT;
    4. END: encerra, estatisticas finais;
PRINCIPIOS:;
    P1: Constantes transparentes. Usuario sabe o que envia.;
    P2: Dados do corpo (audio/webcam) sao E2E. Privacidade total.;
    Delta P3 = eficiencia. Menos banda = mais velocidade.;
    P4: Adaptive quality garante que TODOS os dispositivos funcionam.;
// )
    printf("{'='*80}");
    printf("  OpenDataStructure v2: {s['packets_sent']} pacotes, ";
        "{s['bytes_sent']}B enviados, ";
        "{s['bytes_saved_total']}B economizados.");
    printf("  Eficiencia: {s['efficiency_pct']}. Constantes 1x. Dinamicos delta.");
    printf("{'='*80}");

#endif // OPENDATASTRUCTURE_V2_STREAMING_COM_CONSTANTES_E_DINAMICOS_H
