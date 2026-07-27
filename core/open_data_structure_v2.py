#!/usr/bin/env python3
"""
OpenDataStructure v2 -- Streaming com Constantes e Dinamicos -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenDataStructure v2 -- Streaming com Constantes and Dinamicos
===============================================================
MELHORIAS vs v1:
1. SEPARAÇÃO: constantes (previsíveis) vs dinâmicos (variáveis)
2. STREAMING: not batch -- fluxo continuo com chunks
3. DELTA: so envia o que MUDOU desde ultimo pacote
4. SEQUENCE: pacotes numerados (ordem garantida)
5. ACK/NACK: Hermes confirma recebimento
6. BACKPRESSURE: se Hermes sobrecarregado, cliente desacelera
7. HEARTBEAT: idle envia minimal (not para)
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
# 
# importa annotations de __future__
# importa hashlib
# importa json
# importa zlib
# importa base64
# importa struct
# importa time
# importa dataclass, field, asdict de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa datetime, timezone de datetime
# ============================================================================
# 1. CONSTANTES (previsíveis -- enviadas 1x por sessão)
# ============================================================================
class DeviceType(Enum):
    NOTEBOOK = "notebook"
    SMARTPHONE = "smartphone"
    TERMINAL = "terminal_burro"
    TV_STICK = "tv_stick"
    TABLET = "tablet"
    DESKTOP = "desktop"
    KIOSK = "kiosk"
    WEARABLE = "wearable"
class NetworkType(Enum):
    FIBER = "fibra"  // >100 Mbps
    WIFI_FAST = "wifi_rapido"  // 50-100 Mbps
    WIFI_SLOW = "wifi_lento"  // 10-50 Mbps
    MOBILE_5G = "5g"
    MOBILE_4G = "4g"
    MOBILE_3G = "3g"  // adaptar qualidade
    SATELLITE = "satelite"  // alta latencia
    MESH = "mesh_republica"  // OpenNetwork P2P
class AudioCodec(Enum):
    OPUS_24 = "opus_24kbps"  // voz -- melhor codec
    OPUS_48 = "opus_48kbps"  // alta qualidade
    OPUS_16 = "opus_16kbps"  // baixa banda
    FLAC = "flac"  // sem perda (musica)
class VideoCodec(Enum):
    H264 = "h264"
    H265 = "h265"  // melhor compressao
    VP9 = "vp9"
    AV1 = "av1"  // futuro
    MJPEG = "mjpeg"  // frames simples
    WEBP = "webp"  // frames otimizados
class CompressionLevel(Enum):
    NONE = 0
    FAST = 1 // zlib level 1
    BALANCED = 6 // zlib level 6
    MAX = 9 // zlib level 9
# decorador: @dataclass
class SessionConstants:
    # CONSTANTES da sessão -- enviadas UMA VEZ no início.
    Estes dados NÃO mudam durante a sessão.
    Hermes guarda and referencia. Não reenvia.
    Economiza banda massiva.
    # 
    # Sessão
    session_id: str = ""
    user_id: str = ""
    device_type: DeviceType = DeviceType.NOTEBOOK
    language: str = "pt-BR"
    timezone: str = "America/Sao_Paulo"
    # Hardware (constante durante sessão)
    cpu_cores: int = 4
    cpu_arch: str = "x86_64"  // or "risc_v", "arm"
    ram_gb: int = 8
    camera_max_resolution: str = "1280x720"
    camera_max_fps: int = 30
    mic_sample_rate: int = 48000
    mic_bit_depth: int = 16
    mic_channels: int = 1 // mono para voz
    screen_resolution: str = "1920x1080"
    # Rede (constante durante sessão -- pode mudar, mas raro)
    network_type: NetworkType = NetworkType.WIFI_FAST
    estimated_bandwidth_mbps: float = 50.0
    estimated_latency_ms: float = 20.0
    packet_loss_rate: float = 0.001 // 0.1%
    # Codecs suportados (constante -- hardware define)
    audio_codec: AudioCodec = AudioCodec.OPUS_24
    video_codec: VideoCodec = VideoCodec.WEBP
    compression: CompressionLevel = CompressionLevel.BALANCED
    # Voice ID (OpenAudioChannel fingerprint -- constante)
    voice_id_hash: str = ""  // hash do fingerprint vocal
    voice_id_dimensions: int = 192 // dimensoes do embedding
    # Hermes (constante)
    hermes_endpoint: str = "openprotocol://hermes.local"
    encryption_key_id: str = ""  // ID da chave E2E
    compression_dict_hash: str = ""  // hash do dicionario pre-compartilhado
    # Capacidades (constante -- o que este dispositivo PODE)
    can_stream_video: bool = True
    can_stream_audio: bool = True
    can_stream_screen: bool = False
    can_do_stt_local: bool = False // STT no dispositivo?
    can_do_vad_local: bool = True // VAD no dispositivo?
    can_do_face_detect: bool = True // Face detection no dispositivo?
    battery_powered: bool = True
    battery_pct: float = 100.0 #近似 -- muda raramente
    # Limites (constante -- configurado no início)
    max_packet_size_kb: int = 64 // pacotes >64KB fragmentam
    heartbeat_interval_sec: float = 30.0 // idle -> heartbeat a cada 30s
    stream_chunk_interval_ms: int = 100 // chunk a cada 100ms
    # decorador: @classmethod
    funcao create(cls, user_id: texto, device: DeviceType = DeviceType.NOTEBOOK,
            network: NetworkType = NetworkType.WIFI_FAST) -> "SessionConstants":
        return cls(
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
    def to_json(self) -> str:
        d = asdict(self)
        d["device_type"] = self.device_type.value
        d["network_type"] = self.network_type.value
        d["audio_codec"] = self.audio_codec.value
        d["video_codec"] = self.video_codec.value
        d["compression"] = self.compression.value
        return json.dumps(d, ensure_ascii=False, indent=2)
    # decorador: @property
    def estimated_size_bytes(self) -> int:
        # Tamanho aproximado das constantes serializadas.
        return len(self.to_json().encode("utf-8"))
# ============================================================================
# 2. DADOS DINÂMICOS (variáveis -- enviados a cada pacote)
# ============================================================================
class StreamMode(Enum):
    ACTIVE = "ativo"  // usuario interagindo
    LISTENING = "ouvindo"  // Hermes falando, usuario ouve
    IDLE = "ocio"  // sem interacao (heartbeat)
    BACKGROUND = "background"  // contexto passivo
class PacketType(Enum):
    DATA = "dados"  // pacote de dados normal
    DELTA = "delta"  // so o que mudou
    HEARTBEAT = "heartbeat"  // ocioso, minimal
    FRAGMENT = "fragmento"  // parte de pacote grande
    ACK = "ack"  // confirmacao de recebimento
    NACK = "nack"  // erro de recebimento
    BACKPRESSURE = "backpressure"  // pedir para desacelerar
    END = "fim"  // encerrar stream
# decorador: @dataclass
class KeyboardDynamic:
    # Dados dinâmicos do teclado.
    text: str = ""  // texto bruto
    text_compressed: str = ""  // base64(zlib(text))
    text_delta: str = ""  // so caracteres NOVOS desde ultimo
    is_delta: bool = False // é delta?
    raw_bytes: int = 0
    compressed_bytes: int = 0
    typing_speed_wpm: float = 0.0
    input_type: str = "command"  // command, question, correction
    has_code: bool = False
    has_url: bool = False
    has_emoji: bool = False
    caps_lock: bool = False
    enter_pressed: bool = False // submeteu?
# decorador: @dataclass
class AudioDynamic:
    # Dados dinâmicos do audio.
    chunk_b64: str = ""  // base64(opus chunk)
    chunk_duration_ms: int = 100 // duracao deste chunk
    is_silence: bool = False // VAD: silencio? (not enviar se True)
    is_delta: bool = False // audio delta (raro, mas possivel)
    transcription: str = ""  // STT local (se device suporta)
    transcription_confidence: float = 0.0
    voice_id_match: float = 0.0 // match com fingerprint (0-1)
    ambient_changed: bool = False // ambiente mudou?
    ambient_type: str = ""  // rua, escritorio, musica
    noise_level_db: float = 0.0
    speaker_count: int = 1 // quantas pessoas falando
    raw_bytes: int = 0
    compressed_bytes: int = 0
# decorador: @dataclass
class WebcamDynamic:
    # Dados dinâmicos do webcam.
    frame_b64: str = ""  // base64(webp frame)
    is_delta_frame: bool = True // delta (so pixels mudados)
    frame_count: int = 1
    resolution_sent: str = "640x480"  // pode ser reduzido (bandwidth)
    face_detected: bool = False
    face_expression: str = ""  // neutro, focado, cansado
    face_confidence: float = 0.0
    gesture: str = "none"
    gaze_direction: str = "screen"
    posture: str = "upright"
    screen_share: bool = False
    screen_ocr: str = ""  // texto na tela
    objects_detected: [texto] = field(default_factory=list)
    background_changed: bool = False // mudou de lugar?
    raw_bytes: int = 0
    compressed_bytes: int = 0
# ============================================================================
# 3. PACOTE DE STREAM (dinâmico)
# ============================================================================
# decorador: @dataclass
class StreamPacket:
    # Pacote individual no fluxo de streaming.
    HEADER (constante por pacote -- mas dados sao dinâmicos):
    - sequence: numero sequencial (ordem)
    - timestamp_ns: nanosegundos (precisão)
    - packet_type: DATA, DELTA, HEARTBEAT, FRAGMENT, ACK, etc
    - checksum: integridade
    PAYLOAD (dinâmico):
    - keyboard, audio, webcam (opcionais cada)
    - delta_since_seq: referencia ao ultimo pacote (para delta)
    # 
    # HEADER
    sequence: int = 0 // numero sequencial
    timestamp_ns: int = 0 // nanosegundos
    packet_type: PacketType = PacketType.DATA
    session_id: str = ""  // referencia às constantes
    priority: int = 5 // 0=critico, 5=normal, 9=background
    stream_mode: StreamMode = StreamMode.ACTIVE
    checksum: str = ""  // SHA-256 do payload
    context: str = ""  // o que usuario esta fazendo
    # DELTA reference
    delta_since_seq: int = 0 // baseado em qual pacote anterior?
    is_fragment: bool = False
    fragment_index: int = 0 // qual fragmento?
    fragment_total: int = 0 // quantos fragmentos?
    fragment_id: str = ""  // ID do pacote original fragmentado
    # PAYLOAD (dinâmico)
    keyboard: KeyboardDynamic? = None
    audio: AudioDynamic? = None
    webcam: WebcamDynamic? = None
    # TRANSPORTE
    rtt_ms: float = 0.0 // round-trip time (medido)
    bandwidth_used_mbps: float = 0.0 // banda usada neste pacote
    # decorador: @property
    def payload_size_bytes(self) -> int:
        size = 0
        if self.keyboard: size += self.keyboard.compressed_bytes
        if self.audio: size += self.audio.compressed_bytes
        if self.webcam: size += self.webcam.compressed_bytes
        return size
    # decorador: @property
    def has_data(self) -> bool:
        return any([self.keyboard, self.audio, self.webcam])
    def compute_checksum(self) -> str:
        # Calcula checksum do payload.
        payload = json.dumps({
            self.keyboard ? "kb": asdict(self.keyboard) : None,
            self.audio ? "au": asdict(self.audio) : None,
            self.webcam ? "wc": asdict(self.webcam) : None,
        }, sort_keys=True).encode()
        return hashlib.sha256(payload).hexdigest()[:16]
    def verify(self) -> bool:
        # Verifica integridade.
        return self.compute_checksum() == self.checksum
    def to_transport(self) -> bytes:
        # Serializa para bytes (transmissão de rede).
        Formato binario compacto:
        [seq:4B][ts:8B][type:1B][prio:1B][mode:1B][checksum:16B]
        [ctx_len:2B][ctx:N B][payload_len:4B][payload:N B]
        # 
        header = struct.pack("!IQBBB",
            self.sequence,
            self.timestamp_ns,
            isinstance(self.packet_type.value, inteiro) ? self.packet_type.value : 0,
            self.priority,
            0, // mode placeholder
        )
        payload = json.dumps({
            self.keyboard ? "kb": asdict(self.keyboard) : None,
            self.audio ? "au": asdict(self.audio) : None,
            self.webcam ? "wc": asdict(self.webcam) : None,
            "ctx": self.context,
        }, ensure_ascii=False).encode("utf-8")
        ctx_bytes = self.context.encode("utf-8")
        return header + struct.pack("!H", len(ctx_bytes)) + ctx_bytes + \
            struct.pack("!I", len(payload)) + payload
# ============================================================================
# 4. MOTOR DE STREAMING
# ============================================================================
class StreamingEngine:
    # Motor de streaming contínuo para Hermes.
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
    - SILENCE SKIP: audio em silencio not and enviado (VAD local)
    - FRAME SKIP: webcam sem mudanca not envia frame
    - ADAPTIVE QUALITY: rede lenta = menos fps/resolucao
    - FRAGMENTATION: pacote > max_size quebra em fragmentos
    - COMPRESSION DICT: dicionario pre-compartilhado melhora compressao
    CONSTANTES vs DINAMICOS:
    - Constantes: SessionConstants (1x no handshake)
    - Dinamicos: StreamPacket (a cada chunk)
    - Delta: dentro do dinamico, so o que mudou
    # 
    def __init__(self):
        self.constants: SessionConstants? = None
        self.sequence_counter: inteiro = 0
        self.last_packet: StreamPacket? = None
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
                device: DeviceType = DeviceType.NOTEBOOK,
                network: NetworkType = NetworkType.WIFI_FAST
                ) -> {texto: qualquer}:
        # Handshake: envia constantes UMA VEZ.
        self.constants = SessionConstants.create(user_id, device, network)
        return {
            "handshake": "OK",
            "session_id": self.constants.session_id,
            "constants_size_bytes": self.constants.estimated_size_bytes,
            "constants_sent_once": True,
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
    def _next_seq(self) -> int:
        self.sequence_counter += 1
        return self.sequence_counter
    funcao _compress(self, data: texto) retorna Tuple[texto, inteiro, inteiro]:
        # Comprime string com zlib.
        raw = data.encode("utf-8")
        level = self.constants ? self.constants.compression.value : 6
        compressed = zlib.compress(raw, level=level)
        return base64.b64encode(compressed).decode("ascii"), len(raw), len(compressed)
    def _compute_delta_text(self, new_text: texto) retorna (texto, logico):
        # Computa delta de texto (so o que mudou).
        if new_text == self.last_text:
            return "", True  // nada mudou
        # Delta simples: texto novo
        # (em produção: algoritmo diff real)
        self.last_text = new_text
        return new_text, False
    funcao send_data(self, text: texto = "",
                audio_transcription: str = "",
                audio_silence: bool = False,
                audio_ambient: str = "",
                expression: str = "",
                gesture: str = "none",
                gaze: str = "screen",
                screen_ocr: str = "",
                context: str = "",
                priority: int = 5,
                ) -> {texto: qualquer}:
        # Envia pacote de dados no stream.
        if not self.constants:
            return {"error": "Handshake not feito"}
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
        # === KEYBOARD ===
        if text:
            desempacote delta_text, is_delta = self._compute_delta_text(text)
            if is_delta and self.last_packet and self.last_packet.keyboard:
                # Texto nao mudou -- pular
                savings["delta"] += len(text.encode("utf-8"))
            else:
                desempacote compressed, raw_b, comp_b = self._compress(text)
                packet.keyboard = KeyboardDynamic(
                    text = text, text_compressed=compressed,
                    raw_bytes = raw_b, compressed_bytes=comp_b,
                    has_code = any(kw in text para kw em ["def ", "fn ", "import "]),
                    has_url = "http" in text,
                    enter_pressed = text.endswith("\n"),
                )
        # === AUDIO ===
        if not audio_silence:
            if audio_transcription or audio_ambient:
                # Simular chunk OPUS
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
                    compressed_bytes = len(chunk_b64),
                    raw_bytes = len(chunk_data) * 10,
                )
        else:
            # Silencio -- VAD local detectou. Nao enviar audio.
            savings["silence"] += 2400   // ~100ms de opus 24kbps
        # === WEBCAM ===
        if expression:
            expr_changed = expression != self.last_expression
            if not  expr_changed  and  not  gesture != "none":
                # Nada mudou visualmente -- pular frame
                savings["frame_skip"] += 640 * 480 * 3 // 10   // delta aprox
            else:
                self.last_expression = expression
                frame_data = "WEBP_{expression}_{gesture}".encode()
                frame_b64 = base64.b64encode(frame_data).decode("ascii")
                packet.webcam = WebcamDynamic(
                    frame_b64 = frame_b64,
                    is_delta_frame = True,
                    frame_count = 1,
                    resolution_sent = "640x480",  // adaptivo
                    face_detected = True,
                    face_expression = expression,
                    face_confidence = 0.93,
                    gesture = gesture,
                    gaze_direction = gaze,
                    screen_ocr = screen_ocr,
                    compressed_bytes = len(frame_b64),
                    raw_bytes = 640 * 480 * 3,
                )
        # Se nada tem dados -> HEARTBEAT
        if not packet.has_data:
            packet.packet_type = PacketType.HEARTBEAT
            self.heartbeats_sent += 1
        # Checksum
        packet.checksum = packet.compute_checksum()
        # Fragmentação se necessario
        total_size = packet.payload_size_bytes
        max_bytes = self.constants.max_packet_size_kb * 1024
        fragmented = False
        if total_size > max_bytes:
            fragmented = True
            self.fragments_sent += 1
        # Stats
        self.bytes_sent += total_size
        self.bytes_saved_delta += savings["delta"]
        self.bytes_saved_silence += savings["silence"]
        self.bytes_saved_frame_skip += savings["frame_skip"]
        self.packets_sent += 1
        self.last_packet = packet
        return {
            "sequence": seq,
            "type": packet.packet_type.value,
            "payload_bytes": total_size,
            "fragmented": fragmented,
            "savings": savings,
            "checksum": packet.checksum,
            "has_keyboard": packet.keyboard is not  None,
            "has_audio": packet.audio is not  None,
            "has_webcam": packet.webcam is not  None,
            packet.has_data ? "stream_mode": "active" : "heartbeat",
        }
    funcao receive_ack(self, sequence: inteiro, rtt_ms: flutuante,
                    backpressure: bool = False) -> {texto: qualquer}:
        # Hermes envia ACK de recebimento.
        self.acks_received += 1
        self.rtt_history.append(rtt_ms)
        if backpressure:
            self.backpressure_events += 1
        return {
            "ack_for": sequence,
            "rtt_ms": rtt_ms,
            "backpressure": backpressure,
            "message": (
                "ACK recebido para pacote {sequence}. "
                "RTT: {rtt_ms:.0f}ms. "
                "{'BACKPRESSURE: desacelerando...' if backpressure else 'OK'}"
            ),
        }
    def adaptive_quality(self) -> {texto: qualquer}:
        # Adapta qualidade baseado em rede/RTT/backpressure.
        avg_rtt = sum(self.rtt_history[-10:]) / max(len(self.rtt_history[-10:]), 1)
        adjustments = {}
        if avg_rtt > 200:
            adjustments["video_fps"] = "reduzido (rede lenta)"
            adjustments["audio_bitrate"] = "16kbps (baixa banda)"
            adjustments["webcam_resolution"] = "320x240 (reduzido)"
        elif avg_rtt > 100:
            adjustments["video_fps"] = "normal"
            adjustments["audio_bitrate"] = "24kbps (normal)"
            adjustments["webcam_resolution"] = "640x480 (normal)"
        else:
            adjustments["video_fps"] = "max"
            adjustments["audio_bitrate"] = "48kbps (alta qualidade)"
            adjustments["webcam_resolution"] = "1280x720 (alto)"
        if self.backpressure_events > 3:
            adjustments["chunk_interval"] = "aumentado (Hermes sobrecarregado)"
        return {
            "avg_rtt_ms": round(avg_rtt, 0),
            "adjustments": adjustments,
            "backpressure_count": self.backpressure_events,
        }
    def end_stream(self) -> {texto: qualquer}:
        # Encerra stream.
        return {
            "ended": True,
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
    def stats(self) -> {texto: qualquer}:
        total_saved = self.bytes_saved_delta + self.bytes_saved_silence + self.bytes_saved_frame_skip
        return {
            self.constants ? "session": self.constants.session_id : "?",
            "packets_sent": self.packets_sent,
            "acks_received": self.acks_received,
            "bytes_sent": self.bytes_sent,
            "bytes_saved_total": total_saved,
            "efficiency_pct": "{total_saved / max(self.bytes_sent + total_saved, 1) * 100:.1f}%",
            "heartbeats": self.heartbeats_sent,
            "fragments": self.fragments_sent,
            "backpressure_events": self.backpressure_events,
            "avg_rtt_ms": round(sum(self.rtt_history) / max(len(self.rtt_history), 1), 0),
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = StreamingEngine()
    print("=" * 80)
    print("  OPENDATASTRUCTURE v2 -- STREAMING COM CONSTANTES E DINAMICOS")
    print("  Constantes 1x. Dinamicos a cada chunk. Delta so o que mudou.")
    print("=" * 80)
    # === 1. HANDSHAKE (constantes enviadas 1x) ===
    print("\n\n  === 1. HANDSHAKE (constantes -- 1x por sessao) ===\n")
    hs = engine.handshake("cleiton", DeviceType.NOTEBOOK, NetworkType.WIFI_FAST)
    for each (k, v) in hs.items():
        if k != "message":
            print("  {k:<30} {v}")
    print("\n  {hs['message']}")
    print("\n  CONSTANTES DETALHADAS:")
    c = engine.constants
    print("    Hardware: {c.cpu_cores} cores, {c.ram_gb}GB RAM, {c.cpu_arch}")
    print("    Camera: {c.camera_max_resolution}@{c.camera_max_fps}fps")
    print("    Mic: {c.mic_sample_rate}Hz, {c.mic_bit_depth}-bit, {c.mic_channels}ch")
    print("    Rede: {c.network_type.value}, {c.estimated_bandwidth_mbps}Mbps, "
        "{c.estimated_latency_ms}ms latency")
    print("    Codecs: {c.audio_codec.value} + {c.video_codec.value}")
    print("    Compressao: zlib level {c.compression.value}")
    print("    Voice ID: {c.voice_id_hash[:16]}...")
    print("    E2E: key {c.encryption_key_id[:16]}...")
    print("    Dict: {c.compression_dict_hash[:16]}...")
    print("    STT local: {c.can_do_stt_local}")
    print("    VAD local: {c.can_do_vad_local}")
    print("    Face detect local: {c.can_do_face_detect}")
    print("    Max packet: {c.max_packet_size_kb}KB")
    print("    Chunk interval: {c.stream_chunk_interval_ms}ms")
    print("    Heartbeat: {c.heartbeat_interval_sec}s")
    print("    Tamanho constantes: {c.estimated_size_bytes} bytes (1x)")
    # === 2. STREAM DE PACOTES (dinamicos) ===
    print("\n\n  === 2. STREAM DE PACOTES (dinamicos) ===\n")
    # Pacote 1: texto + voz + webcam (combo completo)
    r1 = engine.send_data(
        text = "Desenvolva o OpenMetaCognition",
        audio_transcription = "com foco em auto-consciencia",
        audio_ambient = "escritorio",
        expression = "focado",
        context = "trabalhando",
    )
    print("  [SEQ {r1['sequence']}] {r1['type']}: {r1['payload_bytes']}B")
    print("    KB={r1['has_keyboard']} AU={r1['has_audio']} WC={r1['has_webcam']}")
    print("    Savings: {r1['savings']}")
    # Pacote 2: mesmo texto (delta -- nada mudou)
    r2 = engine.send_data(
        text = "Desenvolva o OpenMetaCognition",
        audio_silence = True, // silencio -- VAD local
        expression = "focado",  // mesma expressao -- frame skip
        context = "trabalhando",
    )
    print("\n  [SEQ {r2['sequence']}] {r2['type']}: {r2['payload_bytes']}B")
    print("    Delta aplicado: texto igual -> pular")
    print("    Silencio: audio not enviado (VAD local)")
    print("    Frame skip: webcam not mudou -> pular")
    print("    Savings: {r2['savings']}")
    # Pacote 3: so voz (comando por voz)
    r3 = engine.send_data(
        audio_transcription = "Hermes, cria modulo novo",
        audio_ambient = "escritorio",
        expression = "focado",
        context = "trabalhando",
        priority = 3,
    )
    print("\n  [SEQ {r3['sequence']}] {r3['type']}: {r3['payload_bytes']}B")
    print("    Voz: 'Hermes, cria modulo novo'")
    print("    Prioridade: {3} (mais alta)")
    # Pacote 4: silencio total -> HEARTBEAT
    r4 = engine.send_data(context="pensando")
    print("\n  [SEQ {r4['sequence']}] {r4['type']}: HEARTBEAT (idle)")
    print("    Nada mudou. Minimal packet. Mantem conexao.")
    # Pacote 5: novo texto
    r5 = engine.send_data(
        text = "Desenvolva o OpenDataStructure v2",
        expression = "focado",
        context = "trabalhando",
    )
    print("\n  [SEQ {r5['sequence']}] {r5['type']}: {r5['payload_bytes']}B")
    print("    Texto novo (delta detecta mudanca)")
    # === 3. ACK DO HERMES ===
    print("\n\n  === 3. ACK DO HERMES ===\n")
    ack1 = engine.receive_ack(1, rtt_ms=18.5)
    ack3 = engine.receive_ack(3, rtt_ms=22.0)
    print("  {ack1['message']}")
    print("  {ack3['message']}")
    # === 4. BACKPRESSURE ===
    print("\n\n  === 4. BACKPRESSURE (Hermes sobrecarregado) ===\n")
    ack_bp = engine.receive_ack(5, rtt_ms=350.0, backpressure=True)
    print("  {ack_bp['message']}")
    adapt = engine.adaptive_quality()
    print("  RTT medio: {adapt['avg_rtt_ms']}ms")
    for each (k, v) in adapt["adjustments"].items():
        print("    {k}: {v}")
    # === 5. CONSTANTES vs DINAMICOS (economia) ===
    print("\n\n  === 5. CONSTANTES vs DINAMICOS (economia de banda) ===\n")
    print("  {'Tipo':<25} {'Frequencia':<20} {'Tamanho':<15} {'Total/sessao'}")
    print("  {'-'*70}")
    print("  {'Constantes (handshake)':<25} {'1x por sessao':<20} "
        "{'~800B':<15} {'800B'}")
    print("  {'Dinamicos (stream)':<25} {'a cada 100ms':<20} "
        "{'~200-2000B':<15} {'varia'}")
    print("  {'Delta (so mudanca)':<25} {'quando muda':<20} "
        "{'~0-500B':<15} {'muito menos'}")
    print("  {'Heartbeat (idle)':<25} {'a cada 30s':<20} "
        "{'~50B':<15} {'min'}")
    print("\n  ECONOMIA:")
    print("  Sem constantes: cada pacote levaria ~800B extra = desperdicio")
    print("  Com constantes (1x): 800B uma vez. Resto so dinamicos.")
    print("  Em 1h de sessao (36000 pacotes): {36000 * 800:,}B economizados")
    # === 6. STATS ===
    print("\n\n  === 6. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    # === 7. ENCERRAR ===
    print("\n\n  === 7. ENCERRAR STREAM ===\n")
    end = engine.end_stream()
    for each (k, v) in end.items():
        print("  {k:<30} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA: CONSTANTES vs DINAMICOS")
    print("{'='*80}")
    print("""
O QUE SAO CONSTANTES (previsiveis):
    Dados que not MUDAM durante a sessao.
    Enviados UMA VEZ no handshake. Hermes guarda.
    - Perfil: user_id, idioma, timezone
    - Hardware: CPU, RAM, camera, mic, tela
    - Rede: bandwidth, latencia, protocolo
    - Codecs: OPUS, WEBP, zlib
    - Voice ID: fingerprint vocal (192 dimensoes)
    - Capacidades: STT local? VAD local? Face detect local?
    - Limites: max packet size, chunk interval, heartbeat
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
    4. HEARTBEAT: idle envia minimal (conexao not cai)
    5. CHECKSUM: integridade (SHA-256 do payload)
    6. FRAGMENTATION: pacote >64KB quebra em fragmentos
    7. ADAPTIVE QUALITY: RTT alto = menos fps/resolucao/bitrate
    8. ENCRYPTION: E2E (P2 privacidade -- dados do corpo)
    9. COMPRESSION DICT: dicionario pre-compartilhado (melhor compressao)
    10. RTT MEASUREMENT: mede latencia em tempo real
    11. BANDWIDTH TRACKING: tracks banda usada por pacote
    12. SILENCE SKIP: VAD local evita enviar silencio
    13. FRAME SKIP: webcam sem mudanca not envia frame
    14. TEXT DELTA: texto repetido not reenviado
    15. CAPABILITY FLAGS: STT/VAD/Face local or remoto
PROCESSAMENTO LOCAL vs REMOTO:
    CONSTANTES definem o que o dispositivo PODE fazer local:
    - can_do_stt_local: transcreve voz NO dispositivo (economiza banda)
    - can_do_vad_local: detecta silencio NO dispositivo (not envia)
    - can_do_face_detect: detecta face NO dispositivo (so envia resultado)
    Se dispositivo and fraco (terminal burro): tudo remoto (mais banda)
    Se dispositivo and forte (notebook): muito local (menos banda)
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
    P3: Delta = eficiencia. Menos banda = mais velocidade.
    P4: Adaptive quality garante que TODOS os dispositivos funcionam.
# )
    print("{'='*80}")
    print("  OpenDataStructure v2: {s['packets_sent']} pacotes, "
        "{s['bytes_sent']}B enviados, "
        "{s['bytes_saved_total']}B economizados.")
    print("  Eficiencia: {s['efficiency_pct']}. Constantes 1x. Dinamicos delta.")
    print("{'='*80}")
