// OpenDataStructure -- Estrutura, Compactacao e Metadados de Pacotes -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenDataStructure -- Estrutura, Compactacao && Metadados de Pacotes;
====================================================================;
"O Hermes precisa receber dados de 3 fontes:;
1. Teclado (texto que o usuario digita);
2. Audio (voz do usuario + ambiente);
3. Webcam (rosto, gestos, tela);
Cada fonte gera DADOS BRUTOS diferentes.;
Cada dado precisa ser ESTRUTURADO, COMPACTADO && ROTULADO.;
O Hermes recebe UM pacote unificado. Nao tres baguncas.;
Este sistema define o FORMATO do pacote.";
FORMATO DO PACOTE (OpenDataPacket):;
{
    "metadata": {
    "packet_id": "PKT-xxxx",;
    "timestamp": "2026-07-24T12:00:00Z",;
    "user_id": "cleiton",;
    "session_id": "sess-xxxx",;
    "sources": ["keyboard", "audio", "webcam"],;
    "compression": "openpack_v1",;
    "priority": "normal",;
    "context": "trabalhando em OpenRepublic";
    },;
    "keyboard": {
    "data": "<compressed_text>",;
    "raw_length": 450,;
    "compressed_length": 120,;
    "language": "pt-BR",;
    "input_type": "command",;
    "modifiers": [];
    },;
    "audio": {
    "data": "<compressed_audio>",;
    "channels": ["user_voice", "ambient"],;
    "duration_sec": 3.5,;
    "format": "opus_16khz",;
    "vad": true,;
    "diarization": {"user_voice": 0.92, "ambient": 0.31};
    },;
    "webcam": {
    "data": "<compressed_frames>",;
    "frames": 3,;
    "resolution": "640x480",;
    "fps_captured": 3,;
    "face_detected": true,;
    "gesture": "none",;
    "screen_share": false;
    },;
    "fusion": {
    "mode": "combo_multimodal",;
    "primary": "keyboard",;
    "secondary": ["audio"],;
    "context_combo": true;
    };
};
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa json
// importa zlib
// importa base64
// importa dataclass, field, asdict de dataclasses
// importa Any, Dict, List, Optional, Tuple, Union de typing
// importa Enum de enum
// importa datetime de datetime
// ============================================================================
// 1. FONTES DE DADOS
// ============================================================================
class DataSource {
    KEYBOARD = "keyboard";
    AUDIO = "audio";
    WEBCAM = "webcam";
    SCREEN = "screen";
    SENSOR = "sensor"  // acelerometro, GPS, etc;
class DataPriority {
    CRITICAL = "critico"  // comando urgente;
    NORMAL = "normal"  // entrada padrao;
    BACKGROUND = "background"  // contexto (audio ambiente);
    IDLE = "ocio"  // sem interacao;
class InputType {
    // Tipo de entrada (para IA processar diferente).
    COMMAND = "comando"  // instrucao direta;
    QUESTION = "pergunta"  // quer resposta;
    CONTEXT = "contexto"  // informacao de fundo;
    CORRECTION = "correcao"  // corrigindo algo;
    EMOTION = "emocao"  // expressando sentimento;
    IDLE = "ocio"  // sem input;
// ============================================================================
// 2. METADADOS DO PACOTE
// ============================================================================
// decorador: @dataclass
class PacketMetadata {
    // Metadados do pacote (quem, quando, o que, prioridade).
    const packet_id = "";
    const timestamp = "";
    const user_id = "";
    const session_id = "";
    const sources = field(default_factory=list);
    const compression = "openpack_v1";
    const priority = DataPriority.NORMAL;
    const input_type = InputType.COMMAND;
    const context = ""  // o que o usuario esta fazendo;
    const location = ""  // onde (opcional);
    const device = ""  // smartphone, notebook, terminal;
    const language = "pt-BR";
    // decorador: @classmethod
    funcao create(cls, user_id: texto, sources: [texto],
            const priority = DataPriority.NORMAL,;
            const input_type = InputType.COMMAND,;
            const context = "",;
            const device = "notebook") -> "PacketMetadata":;
        return cls(;
            packet_id = hashlib.md5(;
                "{user_id}{datetime.now()}".encode()).hexdigest()[:8],;
            timestamp = datetime.now().isoformat(),;
            user_id = user_id,;
            session_id = hashlib.md5(user_id.encode()).hexdigest()[:8],;
            sources = sources,;
            priority = priority,;
            input_type = input_type,;
            context = context,;
            device = device,;
        );
// ============================================================================
// 3. DADOS DE CADA FONTE (estruturados)
// ============================================================================
// decorador: @dataclass
class KeyboardData {
    // Dados do teclado (texto que o usuario digita).
    const raw_text = "";
    const compressed_text = ""  // base64(zlib(text));
    const raw_length = 0;
    const compressed_length = 0;
    const compression_ratio = 0.0;
    const language = "pt-BR";
    const input_type = "command"  // command, question, context;
    const modifiers = field(default_factory=list) // shift, ctrl, etc;
    const typing_speed_wpm = 0.0 // palavras por minuto;
    const autocorrect_used = false;
    const emoji_detected = false;
    const code_detected = false // se digitou codigo;
    const url_detected = false;
    // decorador: @classmethod
    funcao from_input(cls, text: texto, language: texto = "pt-BR",
                const input_type = "command",;
                const modifiers = null) -> "KeyboardData":;
        // Cria dado de teclado a partir de texto bruto.
        raw_len = .length(text.encode("utf-8"));
        compressed = zlib.compress(text.encode("utf-8"), level=9);
        compressed_b64 = base64.b64encode(compressed).decode("ascii");
        comp_len = .length(compressed_b64);
        ratio = (1 - comp_len / maximo(raw_len, 1)) * 100;
        return cls(;
            raw_text = text,;
            compressed_text = compressed_b64,;
            raw_length = raw_len,;
            compressed_length = comp_len,;
            compression_ratio = arredonde(ratio, 1),;
            language = language,;
            input_type = input_type,;
            modifiers = modifiers || [],;
            code_detected = any(kw in text para kw em ["def ", "fn ", "import ", "{", "}"]),;
            url_detected = "http" in text  ||  "www." in text,;
            emoji_detected = any(ord(c) > 0x1F600 para c em text),;
        );
    decompress(self) {
        // Descomprime o texto.
        compressed = base64.b64decode(self.compressed_text);
        return zlib.decompress(compressed).decode("utf-8");
// decorador: @dataclass
class AudioData {
    // Dados de audio (voz + ambiente).
    Dados ja processados pelo OpenAudioChannel:;
    - VAD (detectou fala);
    - Diarization (quem falou);
    - Source separation (vozMovito vs ambiente);
    - Transcricao (texto da fala);
    //
    const compressed_audio = ""  // base64(opus);
    const channels = field(default_factory=() -> ["user_voice"]);
    const duration_sec = 0.0;
    const format = "opus_16khz";
    const sample_rate = 16000;
    const bitrate_kbps = 24;
    const vad_detected = false // voice activity detection;
    const diarization = field(default_factory=dict);
    const transcription = ""  // texto transcrito (STT);
    const transcription_confidence = 0.0;
    const ambient_type = ""  // rua, escritorio, silencio, musica;
    const noise_level_db = 0.0;
    // decorador: @classmethod
    funcao from_capture(cls, duration: flutuante = 3.0,
                    const transcription = "",;
                    const channels = null,;
                    const vad = true,;
                    const ambient = "escritorio",;
                    const noise_db = 35.0) -> "AudioData":;
        // Cria dado de audio a partir de captura.
        // Simular compressao OPUS
        raw_size = inteiro(duration * 16000 * 2) // 16kHz, 16-bit;
        compressed_size = inteiro(duration * 24000 // 8) // 24kbps;
        compressed_b64 = base64.b64encode(;
            "AUDIO_OPUS_{duration}s".encode()).decode("ascii");
        return cls(;
            compressed_audio = compressed_b64,;
            channels = channels  ||  ["user_voice"],;
            duration_sec = duration,;
            vad_detected = vad,;
            diarization = vad ? {"user_voice" : 0.92, "ambient": 0.31} : {},;
            transcription = transcription,;
            transcription_confidence = transcription ? 0.95 : 0.0,;
            ambient_type = ambient,;
            noise_level_db = noise_db,;
        );
// decorador: @dataclass
class WebcamData {
    // Dados de webcam (rosto, gestos, tela).
    FRAMES (! video continuo):;
    - 1-3 frames por pacote (! 30fps);
    - Redundancia removida (so muda o que mudou);
    - Face detection + expressao;
    - Gesto detection (mao, cabeca);
    - Screen share opcional;
    //
    const compressed_frames = "";
    const frame_count = 0;
    const resolution = "640x480";
    const fps_captured = 1 // 1-3 frames por pacote;
    const face_detected = false;
    const face_expression = ""  // neutro, feliz, focado, cansado;
    const gesture = "none"  // none, wave, point, thumbs_up;
    const gaze_direction = "screen"  // screen, away, phone;
    const posture = "upright"  // upright, leaning, standing;
    const screen_share = false;
    const screen_content = ""  // texto detectado na tela (OCR);
    const objects_detected = field(default_factory=list);
    // decorador: @classmethod
    funcao from_capture(cls, face: logico = verdadeiro,
                    const expression = "focado",;
                    const gesture = "none",;
                    const gaze = "screen",;
                    const posture = "upright",;
                    const screen_share = false,;
                    const screen_text = "",;
                    const objects = null) -> "WebcamData":;
        // Cria dado de webcam a partir de captura.
        compressed_b64 = base64.b64encode(;
            "FRAMES_{3 if face else 0}".encode()).decode("ascii");
        return cls(;
            compressed_frames = compressed_b64,;
            frame_count = face ? 3 : 0,;
            face_detected = face,;
            face_expression = expression,;
            gesture = gesture,;
            gaze_direction = gaze,;
            posture = posture,;
            screen_share = screen_share,;
            screen_content = screen_text,;
            objects_detected = objects || [],;
        );
// ============================================================================
// 4. PACOTE UNIFICADO (OpenDataPacket)
// ============================================================================
// decorador: @dataclass
class OpenDataPacket {
    // Pacote unificado enviado ao Hermes.
    Um pacote pode conter:;
    - SO keyboard (texto);
    - SO audio (voz);
    - SO webcam (imagem);
    - COMBO (2+ fontes) -- combo multimodal;
    O Hermes recebe UM pacote com metadados claros.;
    Nao precisa adivinhar de onde veio.;
    //
    metadata: PacketMetadata;
    const keyboard = null;
    const audio = null;
    const webcam = null;
    // Fusao multimodal
    const fusion_mode = "single"  // single, combo_multimodal;
    const primary_source = DataSource.KEYBOARD;
    const secondary_sources = field(default_factory=list);
    // decorador: @property
    source_count(self) {
        count = 0;
        if self.keyboard: count += 1;
        if self.audio: count += 1;
        if self.webcam: count += 1;
        return count;
    // decorador: @property
    is_multimodal(self) {
        return self.source_count >= 2;
    // decorador: @property
    total_compressed_size(self) {
        size = 0;
        if self.keyboard: size += self.keyboard.compressed_length;
        if self.audio: size += .length(self.audio.compressed_audio);
        if self.webcam: size += .length(self.webcam.compressed_frames);
        return size;
    // decorador: @property
    total_raw_size(self) {
        size = 0;
        if self.keyboard: size += self.keyboard.raw_length;
        if (self.audio) {
            size = size + inteiro(self.audio.duration_sec * 16000 * 2);
        if (self.webcam) {
            size = size + self.webcam.frame_count * 640 * 480 * 3 // RGB;
        return size;
    // decorador: @property
    compression_ratio(self) {
        raw = self.total_raw_size;
        comp = self.total_compressed_size;
        if (raw == 0) {
            return 0.0;
        return arredonde((1 - comp / raw) * 100, 1);
    to_json(self) {
        // Serializa pacote para JSON (para transmissao).
        return json.dumps({;
            "metadata": {
                "packet_id": self.metadata.packet_id,;
                "timestamp": self.metadata.timestamp,;
                "user_id": self.metadata.user_id,;
                "sources": self.metadata.sources,;
                "priority": self.metadata.priority.value,;
                "input_type": self.metadata.input_type.value,;
                "context": self.metadata.context,;
                "device": self.metadata.device,;
                "language": self.metadata.language,;
            },;
            self.keyboard ? "keyboard": asdict(self.keyboard) : null,;
            self.audio ? "audio": asdict(self.audio) : null,;
            self.webcam ? "webcam": asdict(self.webcam) : null,;
            "fusion": {
                "mode": self.fusion_mode,;
                "primary": self.primary_source.value,;
                "secondary": [s.value para s em self.secondary_sources],;
                "source_count": self.source_count,;
                "multimodal": self.is_multimodal,;
            },;
            "stats": {
                "raw_size_bytes": self.total_raw_size,;
                "compressed_size_bytes": self.total_compressed_size,;
                "compression_ratio_pct": self.compression_ratio,;
            },;
        }, ensure_ascii=false, indent=2);
    summary(self) {
        // Resumo legivel do pacote.
        return {;
            "packet_id": self.metadata.packet_id,;
            "timestamp": self.metadata.timestamp[:19],;
            "user": self.metadata.user_id,;
            "sources": self.metadata.sources,;
            "priority": self.metadata.priority.value,;
            "input_type": self.metadata.input_type.value,;
            "multimodal": self.is_multimodal,;
            "fusion": self.fusion_mode,;
            "primary": self.primary_source.value,;
            "raw_size": "{self.total_raw_size:,} bytes",;
            "compressed": "{self.total_compressed_size:,} bytes",;
            "compression": "{self.compression_ratio:.1f}%",;
            self.keyboard ? "keyboard_text": self.keyboard.decompress()[:50] : null,;
            self.audio ? "audio_transcription": self.audio.transcription[:50] : null,;
            self.webcam ? "webcam_expression": self.webcam.face_expression : null,;
        };
// ============================================================================
// 5. MOTOR DE PACOTES
// ============================================================================
class DataPacketEngine {
    // Motor que cria, compacta e envia pacotes ao Hermes.
    COMO FUNCIONA:;
    1. Captura dados de 3 fontes (keyboard, audio, webcam);
    2. Cada fonte ESTRUTURA && COMPACTA seus dados;
    3. Motor cria PACOTE UNIFICADO com metadados;
    4. Pacote && enviado ao Hermes (JSON compactado);
    5. Hermes recebe, descompacta && processa;
    COMBOS MULTIMODAIS:;
    - keyboard + audio: texto + voz = combo referencial;
    - keyboard + webcam: texto + expressao = contexto visual;
    - audio + webcam: voz + rosto = comunicacao rica;
    - keyboard + audio + webcam: combo completo;
    PRIORIDADES:;
    - CRITICAL: comando urgente ("Hermes, para!");
    - NORMAL: entrada padrao ("desenvolve OpenX");
    - BACKGROUND: contexto (audio ambiente, postura);
    - IDLE: sem input (mas webcam/audio monitorando);
    //
    __init__(self) {
        self.packets_sent: inteiro = 0;
        self.total_bytes_raw: inteiro = 0;
        self.total_bytes_compressed: inteiro = 0;
    funcao create_keyboard_packet(self, user_id: texto, text: texto,
                            const context = "",;
                            const priority = DataPriority.NORMAL,;
                            const input_type = InputType.COMMAND,;
                            const device = "notebook";
                            ) -> OpenDataPacket:;
        // Cria pacote so de teclado.
        meta = PacketMetadata.create(;
            user_id, [DataSource.KEYBOARD.value],;
            priority, input_type, context, device);
        kb = KeyboardData.from_input(text, input_type=input_type.value);
        packet = OpenDataPacket(;
            metadata = meta, keyboard=kb,;
            primary_source = DataSource.KEYBOARD);
        self._register(packet);
        return packet;
    funcao create_audio_packet(self, user_id: texto,
                            const transcription = "",;
                            const duration = 3.0,;
                            const ambient = "escritorio",;
                            const context = "",;
                            const priority = DataPriority.NORMAL,;
                            ) -> OpenDataPacket:;
        // Cria pacote so de audio.
        meta = PacketMetadata.create(;
            user_id, [DataSource.AUDIO.value],;
            priority, InputType.COMMAND, context);
        audio = AudioData.from_capture(;
            desempacote duration, transcription, ambient = ambient);
        packet = OpenDataPacket(;
            metadata = meta, audio=audio,;
            primary_source = DataSource.AUDIO);
        self._register(packet);
        return packet;
    funcao create_webcam_packet(self, user_id: texto,
                            const expression = "focado",;
                            const gesture = "none",;
                            const gaze = "screen",;
                            const screen_text = "",;
                            const context = "",;
                            ) -> OpenDataPacket:;
        // Cria pacote so de webcam.
        meta = PacketMetadata.create(;
            user_id, [DataSource.WEBCAM.value],;
            DataPriority.BACKGROUND, InputType.CONTEXT, context);
        cam = WebcamData.from_capture(;
            expression = expression, gesture=gesture, gaze=gaze,;
            screen_text = screen_text);
        packet = OpenDataPacket(;
            metadata = meta, webcam=cam,;
            primary_source = DataSource.WEBCAM);
        self._register(packet);
        return packet;
    funcao create_combo_packet(self, user_id: texto,
                            const text = "",;
                            const transcription = "",;
                            const expression = "focado",;
                            const gesture = "none",;
                            const gaze = "screen",;
                            const ambient = "escritorio",;
                            const context = "",;
                            const priority = DataPriority.NORMAL,;
                            const input_type = InputType.COMMAND,;
                            ) -> OpenDataPacket:;
        // Cria pacote COMBO multimodal (2+ fontes).
        Este && o COMBO REFERENCIAL que o usuario quer:;
        escrita + voz + ambiente + expressao = contexto completo.;
        //
        sources = [];
        if text: sources.append(DataSource.KEYBOARD.value);
        if transcription: sources.append(DataSource.AUDIO.value);
        sources.append(DataSource.WEBCAM.value) // sempre;
        meta = PacketMetadata.create(;
            user_id, sources, priority, input_type, context);
        kb = text ? KeyboardData.from_input(text) : null;
        audio = AudioData.from_capture(;
            transcription ? 3.0, transcription, ambient=ambient) : null;
        cam = WebcamData.from_capture(;
            expression = expression, gesture=gesture, gaze=gaze);
        secondary = [];
        if text: secondary.append(DataSource.KEYBOARD);
        if transcription: secondary.append(DataSource.AUDIO);
        packet = OpenDataPacket(;
            metadata = meta, keyboard=kb, audio=audio, webcam=cam,;
            fusion_mode = "combo_multimodal",;
            primary_source = text ? DataSource.KEYBOARD : DataSource.AUDIO,;
            secondary_sources = secondary,;
        );
        self._register(packet);
        multimodal_sources = [];
        if kb: multimodal_sources.append("keyboard");
        if audio: multimodal_sources.append("audio");
        if cam: multimodal_sources.append("webcam");
        meta.sources = multimodal_sources;
        return packet;
    _register(self, packet: OpenDataPacket) {
        self.packets_sent += 1;
        self.total_bytes_raw += packet.total_raw_size;
        self.total_bytes_compressed += packet.total_compressed_size;
    stats(self) {
        ratio = 0.0;
        if (self.total_bytes_raw > 0) {
            ratio = (1 - self.total_bytes_compressed / self.total_bytes_raw) * 100;
        return {;
            "packets_sent": self.packets_sent,;
            "total_raw_bytes": self.total_bytes_raw,;
            "total_compressed_bytes": self.total_bytes_compressed,;
            "avg_compression_ratio": "{ratio:.1f}%",;
            "bandwidth_saved": "{self.total_bytes_raw - self.total_bytes_compressed:,} bytes",;
        };
// ============================================================================
// 6. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = DataPacketEngine();
    console.log("=" * 80);
    console.log("  OPENDATASTRUCTURE -- PACOTE UNIFICADO DE DADOS");
    console.log("  Keyboard + Audio + Webcam em UM pacote compactado");
    console.log("=" * 80);
    // === 1. PACOTE SO DE TECLADO ===
    console.log("\n\n  === 1. PACOTE: SO TECLADO ===\n");
    p1 = engine.create_keyboard_packet(;
        "cleiton",;
        "Desenvolva o OpenRepublic com 110+ sistemas modulares",;
        context = "trabalhando em OpenRepublic",;
        input_type = InputType.COMMAND,;
    );
    s1 = p1.summary();
    console.log("  Packet ID: {s1['packet_id']}");
    console.log("  Fonte: {s1['sources']}");
    console.log("  Texto: '{s1['keyboard_text']}'");
    console.log("  Bruto: {s1['raw_size']}");
    console.log("  Compactado: {s1['compressed']}");
    console.log("  Compressao: {s1['compression']}");
    // === 2. PACOTE SO DE AUDIO ===
    console.log("\n\n  === 2. PACOTE: SO AUDIO ===\n");
    p2 = engine.create_audio_packet(;
        "cleiton",;
        transcription = "Hermes, desenvolve o OpenMetaCognition",;
        duration = 3.5,;
        ambient = "escritorio_com_musica",;
        context = "trabalhando",;
    );
    s2 = p2.summary();
    console.log("  Packet ID: {s2['packet_id']}");
    console.log("  Fonte: {s2['sources']}");
    console.log("  Transcricao: '{s2['audio_transcription']}'");
    console.log("  Duracao: {p2.audio.duration_sec}s");
    console.log("  VAD: {p2.audio.vad_detected}");
    console.log("  Diarizacao: {p2.audio.diarization}");
    console.log("  Ambiente: {p2.audio.ambient_type}");
    console.log("  Bruto: {s2['raw_size']}");
    console.log("  Compactado: {s2['compressed']}");
    console.log("  Compressao: {s2['compression']}");
    // === 3. PACOTE SO DE WEBCAM ===
    console.log("\n\n  === 3. PACOTE: SO WEBCAM ===\n");
    p3 = engine.create_webcam_packet(;
        "cleiton",;
        expression = "focado",;
        gaze = "screen",;
        screen_text = "open_republic core open_lego_code.py",;
        context = "programando",;
    );
    s3 = p3.summary();
    console.log("  Packet ID: {s3['packet_id']}");
    console.log("  Fonte: {s3['sources']}");
    console.log("  Expressao: {s3['webcam_expression']}");
    console.log("  Olhar: {p3.webcam.gaze_direction}");
    console.log("  Postura: {p3.webcam.posture}");
    console.log("  Tela (OCR): {p3.webcam.screen_content}");
    console.log("  Bruto: {s3['raw_size']}");
    console.log("  Compactado: {s3['compressed']}");
    console.log("  Compressao: {s3['compression']}");
    // === 4. PACOTE COMBO MULTIMODAL (keyboard + audio + webcam) ===
    console.log("\n\n  === 4. PACOTE COMBO MULTIMODAL ===\n");
    p4 = engine.create_combo_packet(;
        "cleiton",;
        text = "Desenvolva o OpenRepublic",;
        transcription = "com foco em modularidade LEGO",;
        expression = "focado",;
        gesture = "none",;
        gaze = "screen",;
        ambient = "escritorio",;
        context = "trabalhando em OpenRepublic",;
    );
    s4 = p4.summary();
    console.log("  Packet ID: {s4['packet_id']}");
    console.log("  Fontes: {s4['sources']}");
    console.log("  Multimodal: {s4['multimodal']}");
    console.log("  Fusao: {s4['fusion']}");
    console.log("  Primaria: {s4['primary']}");
    console.log("  Texto: '{s4['keyboard_text']}'");
    console.log("  Voz: '{s4['audio_transcription']}'");
    console.log("  Expressao: {s4['webcam_expression']}");
    console.log("  Ambiente: {p4.audio.ambient_type} ({p4.audio.noise_level_db}dB)");
    console.log("  Bruto: {s4['raw_size']}");
    console.log("  Compactado: {s4['compressed']}");
    console.log("  Compressao: {s4['compression']}");
    // === 5. ESTRUTURA JSON DO PACOTE ===
    console.log("\n\n  === 5. ESTRUTURA JSON DO PACOTE COMBO ===\n");
    json_str = p4.to_json();
    // Mostrar primeiras 60 linhas
    for (const line of json_str.split("\n")[:60]) {
        console.log("  {line}");
    json_lines = json_str.split("\n");
    if (.length(json_lines) > 60) {
        console.log("  ... ({len(json_lines) - 60} linhas omitidas)");
    // === 6. COMPRESSAO ===
    console.log("\n\n  === 6. COMPACTACAO DE DADOS ===\n");
    console.log("  {'Tipo':<25} {'Bruto':>15} {'Compactado':>15} {'Ratio'}");
    console.log("  {'-'*65}");
    para label, p in [("So teclado", p1), ("So audio", p2), {
                    ("So webcam", p3), ("Combo (3 fontes)", p4)]:;
        console.log("  {label:<25} {p.total_raw_size:>14,}B {p.total_compressed_size:>14,}B ";
            "{p.compression_ratio:>7.1f}%");
    // === 7. STATS ===
    console.log("\n\n  === 7. ESTATISTICAS ===\n");
    s = engine.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<30} {v}");
    // === FILOSOFIA ===
    console.log("\n\n{'='*80}");
    console.log("  FILOSOFIA DO OPENDATASTRUCTURE");
    console.log("{'='*80}");
    console.log(""";
O PROBLEMA:;
    Hermes recebe texto, audio && imagem de fontes separadas.;
    Sem estrutura, vira BAGUNCA.;
    Qual dado && prioridade? Qual && contexto? Qual && comando?;
    Sem metadados, Hermes ADIVINHA.;
A SOLUCAO:;
    OpenDataPacket: UM pacote unificado com:;
    - Metadados (quem, quando, prioridade, contexto);
    - Keyboard (texto compactado com zlib);
    - Audio (opus comprimido + transcricao + VAD + diarizacao);
    - Webcam (frames comprimidos + face + gesto + OCR);
    - Fusao (qual fonte && primaria, qual && secundaria);
COMPACTACAO (cada fonte comprime diferente):;
    Keyboard: zlib level 9 (texto comprime muito bem);
    Audio: OPUS 24kbps (codec de voz otimizado);
    Webcam: JPEG/WebP para frames + delta (so muda o que mudou);
    Pacote final: JSON compactado;
TIPOS DE PACOTE:;
    1. SO TECLADO: texto digitado -> Hermes processa comando;
    2. SO AUDIO: voz transcrita -> Hermes processa comando;
    3. SO WEBCAM: expressao/gesto/tela -> Hermes tem CONTEXTO;
    4. COMBO (2+ fontes): combo multimodal -> Hermes tem REFERENCIA;
COMBO MULTIMODAL (o que o usuario quer):;
    texto ("desenvolva OpenRepublic");
    + voz ("com foco em modularidade");
    + ambiente (musica tocando);
    + expressao (focado);
    + postura (ereto);
    = CONJUNTO REFERENCIAL COMPLETO;
    Hermes sabe:;
    - COMANDO: desenvolva OpenRepublic com foco em modularidade;
    - CONTEXTO: usuario focado, escrevendo + falando;
    - AMBIENTE: escritorio com musica;
    - PRIORIDADE: normal (! urgente);
    - DISPOSITIVO: notebook;
METADADOS (rotulagem):;
    Cada pacote tem METADADOS claros:;
    - packet_id: identificador unico;
    - timestamp: quando foi criado;
    - user_id: quem enviou;
    - sources: quais fontes estao no pacote;
    - priority: critico/normal/background/ocio;
    - input_type: comando/pergunta/contexto/correcao/emocao;
    - context: o que o usuario esta fazendo;
    - device: notebook/smartphone/terminal/tv;
PRIORIDADES:;
    CRITICAL: "Hermes, PARA!" (interrompe tudo);
    NORMAL: "desenvolva OpenX" (entrada padrao);
    BACKGROUND: audio ambiente, postura (contexto);
    IDLE: sem input (mas monitorando);
O QUE HERMES FAZ COM O PACOTE:;
    1. Descompacta cada fonte;
    2. Le metadados (sabe prioridade && contexto);
    3. Fusao: combina fontes (texto + voz = comando completo);
    4. Processa: executa comando com CONTEXTO;
    5. Responde: resposta tambem && estruturada;
FLUXO COMPLETO:;
    Usuario digita+fala+expressa;
    -> OpenDataStructure cria pacote;
    -> Compacta (zlib + opus + jpeg);
    -> Adiciona metadados;
    -> Envia ao Hermes;
    -> Hermes descompacta;
    -> Le metadados;
    -> Fusiona fontes;
    -> Processa com contexto completo;
    -> Responde;
PRINCIPIOS:;
    P1: Pacote estruturado. Sem bagunca. Todos podem ler.;
    P2: Dados do corpo (webcam/audio) sao do usuario. Privacidade.;
    const P3 = eficiencia (menos banda, mais velocidade).;
    P4: Metadados transparentes. Usuario sabe o que envia.;
// )
    console.log("{'='*80}");
    console.log("  OpenDataStructure: {s['packets_sent']} pacotes enviados. ";
        "Compressao media: {s['avg_compression_ratio']}.");
    console.log("  Banda economizada: {s['bandwidth_saved']}.");
    console.log("  Keyboard + Audio + Webcam = 1 pacote unificado.");
    console.log("{'='*80}");
