// OpenDataStructure -- Estrutura, Compactacao e Metadados de Pacotes -- gerado de Portugol++
package opendatastructure_estrutura_compactacao_e_metadados_de_pacotes

import "fmt"

// !/usr/bin/env python3
//
OpenDataStructure -- Estrutura, Compactacao && Metadados de Pacotes
====================================================================
"O Hermes precisa receber dados de 3 fontes:
1. Teclado (texto que o usuario digita)
2. Audio (voz do usuario + ambiente)
3. Webcam (rosto, gestos, tela)
Cada fonte gera DADOS BRUTOS diferentes.
Cada dado precisa ser ESTRUTURADO, COMPACTADO && ROTULADO.
O Hermes recebe UM pacote unificado. Nao tres baguncas.
Este sistema define o FORMATO do pacote."
FORMATO DO PACOTE (OpenDataPacket):
{
    "metadata": {
    "packet_id": "PKT-xxxx",
    "timestamp": "2026-07-24T12:00:00Z",
    "user_id": "cleiton",
    "session_id": "sess-xxxx",
    "sources": ["keyboard", "audio", "webcam"],
    "compression": "openpack_v1",
    "priority": "normal",
    "context": "trabalhando em OpenRepublic"
    },
    "keyboard": {
    "data": "<compressed_text>",
    "raw_length": 450,
    "compressed_length": 120,
    "language": "pt-BR",
    "input_type": "command",
    "modifiers": []
    },
    "audio": {
    "data": "<compressed_audio>",
    "channels": ["user_voice", "ambient"],
    "duration_sec": 3.5,
    "format": "opus_16khz",
    "vad": true,
    "diarization": {"user_voice": 0.92, "ambient": 0.31}
    },
    "webcam": {
    "data": "<compressed_frames>",
    "frames": 3,
    "resolution": "640x480",
    "fps_captured": 3,
    "face_detected": true,
    "gesture": "none",
    "screen_share": false
    },
    "fusion": {
    "mode": "combo_multimodal",
    "primary": "keyboard",
    "secondary": ["audio"],
    "context_combo": true
    }
}
Author: OpenRepublic Team
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
type DataSource int
const (
    KEYBOARD = "keyboard"
    AUDIO = "audio"
    WEBCAM = "webcam"
    SCREEN = "screen"
    SENSOR = "sensor"  // acelerometro, GPS, etc
type DataPriority int
const (
    CRITICAL = "critico"  // comando urgente
    NORMAL = "normal"  // entrada padrao
    BACKGROUND = "background"  // contexto (audio ambiente)
    IDLE = "ocio"  // sem interacao
type InputType int
const (
    // Tipo de entrada (para IA processar diferente).
    COMMAND = "comando"  // instrucao direta
    QUESTION = "pergunta"  // quer resposta
    CONTEXT = "contexto"  // informacao de fundo
    CORRECTION = "correcao"  // corrigindo algo
    EMOTION = "emocao"  // expressando sentimento
    IDLE = "ocio"  // sem input
// ============================================================================
// 2. METADADOS DO PACOTE
// ============================================================================
// decorador: @dataclass
type PacketMetadata struct {
    // Metadados do pacote (quem, quando, o que, prioridade).
    packet_id := "" // string
    timestamp := "" // string
    user_id := "" // string
    session_id := "" // string
    sources := field(default_factory=list) // [texto]
    compression := "openpack_v1" // string
    priority := DataPriority.NORMAL // DataPriority
    input_type := InputType.COMMAND // InputType
    context := ""  // o que o usuario esta fazendo // string
    location := ""  // onde (opcional) // string
    device := ""  // smartphone, notebook, terminal // string
    language := "pt-BR" // string
    // decorador: @classmethod
    funcao create(cls, user_id: texto, sources: [texto],
            priority := DataPriority.NORMAL, // DataPriority
            input_type := InputType.COMMAND, // InputType
            context := "", // string
            device := "notebook") -> "PacketMetadata": // string
        return cls(
            packet_id = hashlib.md5(
                "{user_id}{datetime.now()}".encode()).hexdigest()[:8],
            timestamp = datetime.now().isoformat(),
            user_id = user_id,
            session_id = hashlib.md5(user_id.encode()).hexdigest()[:8],
            sources = sources,
            priority = priority,
            input_type = input_type,
            context = context,
            device = device,
        )
// ============================================================================
// 3. DADOS DE CADA FONTE (estruturados)
// ============================================================================
// decorador: @dataclass
type KeyboardData struct {
    // Dados do teclado (texto que o usuario digita).
    raw_text := "" // string
    compressed_text := ""  // base64(zlib(text)) // string
    raw_length := 0 // int64
    compressed_length := 0 // int64
    compression_ratio := 0.0 // float64
    language := "pt-BR" // string
    input_type := "command"  // command, question, context // string
    modifiers := field(default_factory=list) // shift, ctrl, etc // [texto]
    typing_speed_wpm := 0.0 // palavras por minuto // float64
    autocorrect_used := false // bool
    emoji_detected := false // bool
    code_detected := false // se digitou codigo // bool
    url_detected := false // bool
    // decorador: @classmethod
    funcao from_input(cls, text: texto, language: texto = "pt-BR",
                input_type := "command", // string
                modifiers := nil) -> "KeyboardData": // [texto]
        // Cria dado de teclado a partir de texto bruto.
        raw_len = len(text.encode("utf-8"))
        compressed = zlib.compress(text.encode("utf-8"), level=9)
        compressed_b64 = base64.b64encode(compressed).decode("ascii")
        comp_len = len(compressed_b64)
        ratio = (1 - comp_len / maximo(raw_len, 1)) * 100
        return cls(
            raw_text = text,
            compressed_text = compressed_b64,
            raw_length = raw_len,
            compressed_length = comp_len,
            compression_ratio = arredonde(ratio, 1),
            language = language,
            input_type = input_type,
            modifiers = modifiers || [],
            code_detected = any(kw in text para kw em ["def ", "fn ", "import ", "{", "}"]),
            url_detected = "http" in text  ||  "www." in text,
            emoji_detected = any(ord(c) > 0x1F600 para c em text),
        )
    func decompress(self) string {
        // Descomprime o texto.
        compressed = base64.b64decode(self.compressed_text)
        return zlib.decompress(compressed).decode("utf-8")
// decorador: @dataclass
type AudioData struct {
    // Dados de audio (voz + ambiente).
    Dados ja processados pelo OpenAudioChannel:
    - VAD (detectou fala)
    - Diarization (quem falou)
    - Source separation (vozMovito vs ambiente)
    - Transcricao (texto da fala)
    //
    compressed_audio := ""  // base64(opus) // string
    channels := field(default_factory=() -> ["user_voice"]) // [texto]
    duration_sec := 0.0 // float64
    format := "opus_16khz" // string
    sample_rate := 16000 // int64
    bitrate_kbps := 24 // int64
    vad_detected := false // voice activity detection // bool
    diarization := field(default_factory=dict) // {texto: flutuante}
    transcription := ""  // texto transcrito (STT) // string
    transcription_confidence := 0.0 // float64
    ambient_type := ""  // rua, escritorio, silencio, musica // string
    noise_level_db := 0.0 // float64
    // decorador: @classmethod
    funcao from_capture(cls, duration: flutuante = 3.0,
                    transcription := "", // string
                    channels := nil, // [texto]
                    vad := true, // bool
                    ambient := "escritorio", // string
                    noise_db := 35.0) -> "AudioData": // float64
        // Cria dado de audio a partir de captura.
        // Simular compressao OPUS
        raw_size = inteiro(duration * 16000 * 2) // 16kHz, 16-bit
        compressed_size = inteiro(duration * 24000 // 8) // 24kbps
        compressed_b64 = base64.b64encode(
            "AUDIO_OPUS_{duration}s".encode()).decode("ascii")
        return cls(
            compressed_audio = compressed_b64,
            channels = channels  ||  ["user_voice"],
            duration_sec = duration,
            vad_detected = vad,
            diarization = vad ? {"user_voice" : 0.92, "ambient": 0.31} : {},
            transcription = transcription,
            transcription_confidence = transcription ? 0.95 : 0.0,
            ambient_type = ambient,
            noise_level_db = noise_db,
        )
// decorador: @dataclass
type WebcamData struct {
    // Dados de webcam (rosto, gestos, tela).
    FRAMES (! video continuo):
    - 1-3 frames por pacote (! 30fps)
    - Redundancia removida (so muda o que mudou)
    - Face detection + expressao
    - Gesto detection (mao, cabeca)
    - Screen share opcional
    //
    compressed_frames := "" // string
    frame_count := 0 // int64
    resolution := "640x480" // string
    fps_captured := 1 // 1-3 frames por pacote // int64
    face_detected := false // bool
    face_expression := ""  // neutro, feliz, focado, cansado // string
    gesture := "none"  // none, wave, point, thumbs_up // string
    gaze_direction := "screen"  // screen, away, phone // string
    posture := "upright"  // upright, leaning, standing // string
    screen_share := false // bool
    screen_content := ""  // texto detectado na tela (OCR) // string
    objects_detected := field(default_factory=list) // [texto]
    // decorador: @classmethod
    funcao from_capture(cls, face: logico = verdadeiro,
                    expression := "focado", // string
                    gesture := "none", // string
                    gaze := "screen", // string
                    posture := "upright", // string
                    screen_share := false, // bool
                    screen_text := "", // string
                    objects := nil) -> "WebcamData": // [texto]
        // Cria dado de webcam a partir de captura.
        compressed_b64 = base64.b64encode(
            "FRAMES_{3 if face else 0}".encode()).decode("ascii")
        return cls(
            compressed_frames = compressed_b64,
            frame_count = face ? 3 : 0,
            face_detected = face,
            face_expression = expression,
            gesture = gesture,
            gaze_direction = gaze,
            posture = posture,
            screen_share = screen_share,
            screen_content = screen_text,
            objects_detected = objects || [],
        )
// ============================================================================
// 4. PACOTE UNIFICADO (OpenDataPacket)
// ============================================================================
// decorador: @dataclass
type OpenDataPacket struct {
    // Pacote unificado enviado ao Hermes.
    Um pacote pode conter:
    - SO keyboard (texto)
    - SO audio (voz)
    - SO webcam (imagem)
    - COMBO (2+ fontes) -- combo multimodal
    O Hermes recebe UM pacote com metadados claros.
    Nao precisa adivinhar de onde veio.
    //
    metadata: PacketMetadata
    keyboard := nil // KeyboardData?
    audio := nil // AudioData?
    webcam := nil // WebcamData?
    // Fusao multimodal
    fusion_mode := "single"  // single, combo_multimodal // string
    primary_source := DataSource.KEYBOARD // DataSource
    secondary_sources := field(default_factory=list) // [DataSource]
    // decorador: @property
    func source_count(self) int64 {
        count = 0
        if self.keyboard: count += 1
        if self.audio: count += 1
        if self.webcam: count += 1
        return count
    // decorador: @property
    func is_multimodal(self) bool {
        return self.source_count >= 2
    // decorador: @property
    func total_compressed_size(self) int64 {
        size = 0
        if self.keyboard: size += self.keyboard.compressed_length
        if self.audio: size += len(self.audio.compressed_audio)
        if self.webcam: size += len(self.webcam.compressed_frames)
        return size
    // decorador: @property
    func total_raw_size(self) int64 {
        size = 0
        if self.keyboard: size += self.keyboard.raw_length
        if self.audio {
            size = size + inteiro(self.audio.duration_sec * 16000 * 2)
        if self.webcam {
            size = size + self.webcam.frame_count * 640 * 480 * 3 // RGB
        return size
    // decorador: @property
    func compression_ratio(self) float64 {
        raw = self.total_raw_size
        comp = self.total_compressed_size
        if raw == 0 {
            return 0.0
        return arredonde((1 - comp / raw) * 100, 1)
    func to_json(self) string {
        // Serializa pacote para JSON (para transmissao).
        return json.dumps({
            "metadata": {
                "packet_id": self.metadata.packet_id,
                "timestamp": self.metadata.timestamp,
                "user_id": self.metadata.user_id,
                "sources": self.metadata.sources,
                "priority": self.metadata.priority.value,
                "input_type": self.metadata.input_type.value,
                "context": self.metadata.context,
                "device": self.metadata.device,
                "language": self.metadata.language,
            },
            self.keyboard ? "keyboard": asdict(self.keyboard) : nil,
            self.audio ? "audio": asdict(self.audio) : nil,
            self.webcam ? "webcam": asdict(self.webcam) : nil,
            "fusion": {
                "mode": self.fusion_mode,
                "primary": self.primary_source.value,
                "secondary": [s.value para s em self.secondary_sources],
                "source_count": self.source_count,
                "multimodal": self.is_multimodal,
            },
            "stats": {
                "raw_size_bytes": self.total_raw_size,
                "compressed_size_bytes": self.total_compressed_size,
                "compression_ratio_pct": self.compression_ratio,
            },
        }, ensure_ascii=false, indent=2)
    func summary(self) {texto: qualquer} {
        // Resumo legivel do pacote.
        return {
            "packet_id": self.metadata.packet_id,
            "timestamp": self.metadata.timestamp[:19],
            "user": self.metadata.user_id,
            "sources": self.metadata.sources,
            "priority": self.metadata.priority.value,
            "input_type": self.metadata.input_type.value,
            "multimodal": self.is_multimodal,
            "fusion": self.fusion_mode,
            "primary": self.primary_source.value,
            "raw_size": "{self.total_raw_size:,} bytes",
            "compressed": "{self.total_compressed_size:,} bytes",
            "compression": "{self.compression_ratio:.1f}%",
            self.keyboard ? "keyboard_text": self.keyboard.decompress()[:50] : nil,
            self.audio ? "audio_transcription": self.audio.transcription[:50] : nil,
            self.webcam ? "webcam_expression": self.webcam.face_expression : nil,
        }
// ============================================================================
// 5. MOTOR DE PACOTES
// ============================================================================
type DataPacketEngine struct {
    // Motor que cria, compacta e envia pacotes ao Hermes.
    COMO FUNCIONA:
    1. Captura dados de 3 fontes (keyboard, audio, webcam)
    2. Cada fonte ESTRUTURA && COMPACTA seus dados
    3. Motor cria PACOTE UNIFICADO com metadados
    4. Pacote && enviado ao Hermes (JSON compactado)
    5. Hermes recebe, descompacta && processa
    COMBOS MULTIMODAIS:
    - keyboard + audio: texto + voz = combo referencial
    - keyboard + webcam: texto + expressao = contexto visual
    - audio + webcam: voz + rosto = comunicacao rica
    - keyboard + audio + webcam: combo completo
    PRIORIDADES:
    - CRITICAL: comando urgente ("Hermes, para!")
    - NORMAL: entrada padrao ("desenvolve OpenX")
    - BACKGROUND: contexto (audio ambiente, postura)
    - IDLE: sem input (mas webcam/audio monitorando)
    //
    func __init__(self) {
        self.packets_sent: inteiro = 0
        self.total_bytes_raw: inteiro = 0
        self.total_bytes_compressed: inteiro = 0
    funcao create_keyboard_packet(self, user_id: texto, text: texto,
                            context := "", // string
                            priority := DataPriority.NORMAL, // DataPriority
                            input_type := InputType.COMMAND, // InputType
                            device := "notebook" // string
                            ) -> OpenDataPacket:
        // Cria pacote so de teclado.
        meta = PacketMetadata.create(
            user_id, [DataSource.KEYBOARD.value],
            priority, input_type, context, device)
        kb = KeyboardData.from_input(text, input_type=input_type.value)
        packet = OpenDataPacket(
            metadata = meta, keyboard=kb,
            primary_source = DataSource.KEYBOARD)
        self._register(packet)
        return packet
    funcao create_audio_packet(self, user_id: texto,
                            transcription := "", // string
                            duration := 3.0, // float64
                            ambient := "escritorio", // string
                            context := "", // string
                            priority := DataPriority.NORMAL, // DataPriority
                            ) -> OpenDataPacket:
        // Cria pacote so de audio.
        meta = PacketMetadata.create(
            user_id, [DataSource.AUDIO.value],
            priority, InputType.COMMAND, context)
        audio = AudioData.from_capture(
            desempacote duration, transcription, ambient = ambient)
        packet = OpenDataPacket(
            metadata = meta, audio=audio,
            primary_source = DataSource.AUDIO)
        self._register(packet)
        return packet
    funcao create_webcam_packet(self, user_id: texto,
                            expression := "focado", // string
                            gesture := "none", // string
                            gaze := "screen", // string
                            screen_text := "", // string
                            context := "", // string
                            ) -> OpenDataPacket:
        // Cria pacote so de webcam.
        meta = PacketMetadata.create(
            user_id, [DataSource.WEBCAM.value],
            DataPriority.BACKGROUND, InputType.CONTEXT, context)
        cam = WebcamData.from_capture(
            expression = expression, gesture=gesture, gaze=gaze,
            screen_text = screen_text)
        packet = OpenDataPacket(
            metadata = meta, webcam=cam,
            primary_source = DataSource.WEBCAM)
        self._register(packet)
        return packet
    funcao create_combo_packet(self, user_id: texto,
                            text := "", // string
                            transcription := "", // string
                            expression := "focado", // string
                            gesture := "none", // string
                            gaze := "screen", // string
                            ambient := "escritorio", // string
                            context := "", // string
                            priority := DataPriority.NORMAL, // DataPriority
                            input_type := InputType.COMMAND, // InputType
                            ) -> OpenDataPacket:
        // Cria pacote COMBO multimodal (2+ fontes).
        Este && o COMBO REFERENCIAL que o usuario quer:
        escrita + voz + ambiente + expressao = contexto completo.
        //
        sources = []
        if text: sources.append(DataSource.KEYBOARD.value)
        if transcription: sources.append(DataSource.AUDIO.value)
        sources.append(DataSource.WEBCAM.value) // sempre
        meta = PacketMetadata.create(
            user_id, sources, priority, input_type, context)
        kb = text ? KeyboardData.from_input(text) : nil
        audio = AudioData.from_capture(
            transcription ? 3.0, transcription, ambient=ambient) : nil
        cam = WebcamData.from_capture(
            expression = expression, gesture=gesture, gaze=gaze)
        secondary = []
        if text: secondary.append(DataSource.KEYBOARD)
        if transcription: secondary.append(DataSource.AUDIO)
        packet = OpenDataPacket(
            metadata = meta, keyboard=kb, audio=audio, webcam=cam,
            fusion_mode = "combo_multimodal",
            primary_source = text ? DataSource.KEYBOARD : DataSource.AUDIO,
            secondary_sources = secondary,
        )
        self._register(packet)
        multimodal_sources = []
        if kb: multimodal_sources.append("keyboard")
        if audio: multimodal_sources.append("audio")
        if cam: multimodal_sources.append("webcam")
        meta.sources = multimodal_sources
        return packet
    func _register(self, packet: OpenDataPacket) None {
        self.packets_sent += 1
        self.total_bytes_raw += packet.total_raw_size
        self.total_bytes_compressed += packet.total_compressed_size
    func stats(self) {texto: qualquer} {
        ratio = 0.0
        if self.total_bytes_raw > 0 {
            ratio = (1 - self.total_bytes_compressed / self.total_bytes_raw) * 100
        return {
            "packets_sent": self.packets_sent,
            "total_raw_bytes": self.total_bytes_raw,
            "total_compressed_bytes": self.total_bytes_compressed,
            "avg_compression_ratio": "{ratio:.1f}%",
            "bandwidth_saved": "{self.total_bytes_raw - self.total_bytes_compressed:,} bytes",
        }
// ============================================================================
// 6. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = DataPacketEngine()
    fmt.Println("=" * 80)
    fmt.Println("  OPENDATASTRUCTURE -- PACOTE UNIFICADO DE DADOS")
    fmt.Println("  Keyboard + Audio + Webcam em UM pacote compactado")
    fmt.Println("=" * 80)
    // === 1. PACOTE SO DE TECLADO ===
    fmt.Println("\n\n  === 1. PACOTE: SO TECLADO ===\n")
    p1 = engine.create_keyboard_packet(
        "cleiton",
        "Desenvolva o OpenRepublic com 110+ sistemas modulares",
        context = "trabalhando em OpenRepublic",
        input_type = InputType.COMMAND,
    )
    s1 = p1.summary()
    fmt.Println("  Packet ID: {s1['packet_id']}")
    fmt.Println("  Fonte: {s1['sources']}")
    fmt.Println("  Texto: '{s1['keyboard_text']}'")
    fmt.Println("  Bruto: {s1['raw_size']}")
    fmt.Println("  Compactado: {s1['compressed']}")
    fmt.Println("  Compressao: {s1['compression']}")
    // === 2. PACOTE SO DE AUDIO ===
    fmt.Println("\n\n  === 2. PACOTE: SO AUDIO ===\n")
    p2 = engine.create_audio_packet(
        "cleiton",
        transcription = "Hermes, desenvolve o OpenMetaCognition",
        duration = 3.5,
        ambient = "escritorio_com_musica",
        context = "trabalhando",
    )
    s2 = p2.summary()
    fmt.Println("  Packet ID: {s2['packet_id']}")
    fmt.Println("  Fonte: {s2['sources']}")
    fmt.Println("  Transcricao: '{s2['audio_transcription']}'")
    fmt.Println("  Duracao: {p2.audio.duration_sec}s")
    fmt.Println("  VAD: {p2.audio.vad_detected}")
    fmt.Println("  Diarizacao: {p2.audio.diarization}")
    fmt.Println("  Ambiente: {p2.audio.ambient_type}")
    fmt.Println("  Bruto: {s2['raw_size']}")
    fmt.Println("  Compactado: {s2['compressed']}")
    fmt.Println("  Compressao: {s2['compression']}")
    // === 3. PACOTE SO DE WEBCAM ===
    fmt.Println("\n\n  === 3. PACOTE: SO WEBCAM ===\n")
    p3 = engine.create_webcam_packet(
        "cleiton",
        expression = "focado",
        gaze = "screen",
        screen_text = "open_republic core open_lego_code.py",
        context = "programando",
    )
    s3 = p3.summary()
    fmt.Println("  Packet ID: {s3['packet_id']}")
    fmt.Println("  Fonte: {s3['sources']}")
    fmt.Println("  Expressao: {s3['webcam_expression']}")
    fmt.Println("  Olhar: {p3.webcam.gaze_direction}")
    fmt.Println("  Postura: {p3.webcam.posture}")
    fmt.Println("  Tela (OCR): {p3.webcam.screen_content}")
    fmt.Println("  Bruto: {s3['raw_size']}")
    fmt.Println("  Compactado: {s3['compressed']}")
    fmt.Println("  Compressao: {s3['compression']}")
    // === 4. PACOTE COMBO MULTIMODAL (keyboard + audio + webcam) ===
    fmt.Println("\n\n  === 4. PACOTE COMBO MULTIMODAL ===\n")
    p4 = engine.create_combo_packet(
        "cleiton",
        text = "Desenvolva o OpenRepublic",
        transcription = "com foco em modularidade LEGO",
        expression = "focado",
        gesture = "none",
        gaze = "screen",
        ambient = "escritorio",
        context = "trabalhando em OpenRepublic",
    )
    s4 = p4.summary()
    fmt.Println("  Packet ID: {s4['packet_id']}")
    fmt.Println("  Fontes: {s4['sources']}")
    fmt.Println("  Multimodal: {s4['multimodal']}")
    fmt.Println("  Fusao: {s4['fusion']}")
    fmt.Println("  Primaria: {s4['primary']}")
    fmt.Println("  Texto: '{s4['keyboard_text']}'")
    fmt.Println("  Voz: '{s4['audio_transcription']}'")
    fmt.Println("  Expressao: {s4['webcam_expression']}")
    fmt.Println("  Ambiente: {p4.audio.ambient_type} ({p4.audio.noise_level_db}dB)")
    fmt.Println("  Bruto: {s4['raw_size']}")
    fmt.Println("  Compactado: {s4['compressed']}")
    fmt.Println("  Compressao: {s4['compression']}")
    // === 5. ESTRUTURA JSON DO PACOTE ===
    fmt.Println("\n\n  === 5. ESTRUTURA JSON DO PACOTE COMBO ===\n")
    json_str = p4.to_json()
    // Mostrar primeiras 60 linhas
    for _, line := range json_str.split("\n")[:60] {
        fmt.Println("  {line}")
    json_lines = json_str.split("\n")
    if len(json_lines) > 60 {
        fmt.Println("  ... ({len(json_lines) - 60} linhas omitidas)")
    // === 6. COMPRESSAO ===
    fmt.Println("\n\n  === 6. COMPACTACAO DE DADOS ===\n")
    fmt.Println("  {'Tipo':<25} {'Bruto':>15} {'Compactado':>15} {'Ratio'}")
    fmt.Println("  {'-'*65}")
    para label, p in [("So teclado", p1), ("So audio", p2), {
                    ("So webcam", p3), ("Combo (3 fontes)", p4)]:
        fmt.Println("  {label:<25} {p.total_raw_size:>14,}B {p.total_compressed_size:>14,}B "
            "{p.compression_ratio:>7.1f}%")
    // === 7. STATS ===
    fmt.Println("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items(): {
        fmt.Println("  {k:<30} {v}")
    // === FILOSOFIA ===
    fmt.Println("\n\n{'='*80}")
    fmt.Println("  FILOSOFIA DO OPENDATASTRUCTURE")
    fmt.Println("{'='*80}")
    fmt.Println("""
O PROBLEMA:
    Hermes recebe texto, audio && imagem de fontes separadas.
    Sem estrutura, vira BAGUNCA.
    Qual dado && prioridade? Qual && contexto? Qual && comando?
    Sem metadados, Hermes ADIVINHA.
A SOLUCAO:
    OpenDataPacket: UM pacote unificado com:
    - Metadados (quem, quando, prioridade, contexto)
    - Keyboard (texto compactado com zlib)
    - Audio (opus comprimido + transcricao + VAD + diarizacao)
    - Webcam (frames comprimidos + face + gesto + OCR)
    - Fusao (qual fonte && primaria, qual && secundaria)
COMPACTACAO (cada fonte comprime diferente):
    Keyboard: zlib level 9 (texto comprime muito bem)
    Audio: OPUS 24kbps (codec de voz otimizado)
    Webcam: JPEG/WebP para frames + delta (so muda o que mudou)
    Pacote final: JSON compactado
TIPOS DE PACOTE:
    1. SO TECLADO: texto digitado -> Hermes processa comando
    2. SO AUDIO: voz transcrita -> Hermes processa comando
    3. SO WEBCAM: expressao/gesto/tela -> Hermes tem CONTEXTO
    4. COMBO (2+ fontes): combo multimodal -> Hermes tem REFERENCIA
COMBO MULTIMODAL (o que o usuario quer):
    texto ("desenvolva OpenRepublic")
    + voz ("com foco em modularidade")
    + ambiente (musica tocando)
    + expressao (focado)
    + postura (ereto)
    = CONJUNTO REFERENCIAL COMPLETO
    Hermes sabe:
    - COMANDO: desenvolva OpenRepublic com foco em modularidade
    - CONTEXTO: usuario focado, escrevendo + falando
    - AMBIENTE: escritorio com musica
    - PRIORIDADE: normal (! urgente)
    - DISPOSITIVO: notebook
METADADOS (rotulagem):
    Cada pacote tem METADADOS claros:
    - packet_id: identificador unico
    - timestamp: quando foi criado
    - user_id: quem enviou
    - sources: quais fontes estao no pacote
    - priority: critico/normal/background/ocio
    - input_type: comando/pergunta/contexto/correcao/emocao
    - context: o que o usuario esta fazendo
    - device: notebook/smartphone/terminal/tv
PRIORIDADES:
    CRITICAL: "Hermes, PARA!" (interrompe tudo)
    NORMAL: "desenvolva OpenX" (entrada padrao)
    BACKGROUND: audio ambiente, postura (contexto)
    IDLE: sem input (mas monitorando)
O QUE HERMES FAZ COM O PACOTE:
    1. Descompacta cada fonte
    2. Le metadados (sabe prioridade && contexto)
    3. Fusao: combina fontes (texto + voz = comando completo)
    4. Processa: executa comando com CONTEXTO
    5. Responde: resposta tambem && estruturada
FLUXO COMPLETO:
    Usuario digita+fala+expressa
    -> OpenDataStructure cria pacote
    -> Compacta (zlib + opus + jpeg)
    -> Adiciona metadados
    -> Envia ao Hermes
    -> Hermes descompacta
    -> Le metadados
    -> Fusiona fontes
    -> Processa com contexto completo
    -> Responde
PRINCIPIOS:
    P1: Pacote estruturado. Sem bagunca. Todos podem ler.
    P2: Dados do corpo (webcam/audio) sao do usuario. Privacidade.
    P3 := eficiencia (menos banda, mais velocidade). // Compactar dados
    P4: Metadados transparentes. Usuario sabe o que envia.
// )
    fmt.Println("{'='*80}")
    fmt.Println("  OpenDataStructure: {s['packets_sent']} pacotes enviados. "
        "Compressao media: {s['avg_compression_ratio']}.")
    fmt.Println("  Banda economizada: {s['bandwidth_saved']}.")
    fmt.Println("  Keyboard + Audio + Webcam = 1 pacote unificado.")
    fmt.Println("{'='*80}")
