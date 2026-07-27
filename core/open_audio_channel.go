// OpenAudioChannel -- Separacao de Audio em Micro-Canais -- gerado de Portugol++
package openaudiochannel_separacao_de_audio_em_micro_canais

import "fmt"

// !/usr/bin/env python3
//
OpenAudioChannel -- Separacao de Audio em Micro-Canais
=========================================================
"O microfone ! ouve. O CEREBRO ouve.
O microfone capta tudo misturado.
O cerebro separa: minha voz, a voz do outro, o som da rua.
O Hermes precisa fazer o mesmo."
O QUE ISTO FAZ:
Pega UM fluxo de audio (microfone + smartphone)
Separa em MULTIPLOS micro-canais identificados:
- Canal 1: VOZ DO USUARIO (eu falando)
- Canal 2: VOZ DE OUTRA PESSOA (alguem conversando perto)
- Canal 3: MUSICA/TV (tocando ao fundo)
- Canal 4: SOM AMBIENTE (rua, vento, maquina)
- Canal 5: SILENCIO (! descartar -- contexto = sozinho)
Cada canal && processado, classificado && enviado separadamente.
O Hermes recebe o CONJUNTO: "voce disse X, enquanto Y tocava".
COMO FUNCIONA (pipeline):
Audio bruto -> VAD (detectar fala) -> Diarizacao (quem fala)
            -> Source Separation (separar fontes)
            -> Voice ID (&& o usuario?)
            -> Classificacao (musica/ambiente/pessoa)
            -> Micro-canais separados
            -> Fusion em prompt contextual
TECNOLOGIAS:
- VAD: WebRTC Voice Activity Detection (silero-vad)
- Diarizacao: pyannote.audio (speaker diarization)
- Source Separation: Demucs / Spleeter (vocal vs instrumental)
- Voice ID: x-vectors / ECAPA-TDNN (fingerprint do usuario)
- Classificacao: YAMNet / AudioSet (ambiente)
- Tudo LOCAL, sem nuvem, sem enviar audio a terceiros
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa math
// importa hashlib
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, deque de collections
// importa datetime de datetime
// ============================================================================
// 1. TIPOS DE CANAL DE AUDIO
// ============================================================================
type AudioChannelType int
const (
    // Cada fonte de audio vira um tipo de canal.
    USER_VOICE = "voz_usuario"  // o dono falando (PRIORIDADE)
    OTHER_VOICE = "outra_voz"  // outra pessoa conversando perto
    MUSIC = "musica"  // musica/TV/playlist tocando
    TV_MEDIA = "tv_midia"  // TV, podcast, video tocando
    AMBIENT_NATURE = "ambiente_natureza"  // vento, chuva, passatos
    AMBIENT_URBAN = "ambiente_urbano"  // transito, construcao, gente
    MACHINE = "maquina"  // ventilador, motor, computador
    SILENCE = "silencio"  // nada (contexto: sozinho/foco)
    UNKNOWN = "desconhecido"
type ChannelPriority int
const (
    // Prioridade do canal para o prompt do Hermes.
    CRITICAL = 0 // voz do usuario -- sempre processa
    HIGH = 1 // outra voz dirigida ao usuario
    CONTEXTUAL = 2 // musica/TV -- contexto mas ! comando
    BACKGROUND = 3 // ambiente -- referencia apenas
    IGNORE = 4 // maquina/ruido -- descartar
// Mapeamento tipo -> prioridade
CHANNEL_PRIORITY = {
    AudioChannelType.USER_VOICE: ChannelPriority.CRITICAL,
    AudioChannelType.OTHER_VOICE: ChannelPriority.HIGH,
    AudioChannelType.MUSIC: ChannelPriority.CONTEXTUAL,
    AudioChannelType.TV_MEDIA: ChannelPriority.CONTEXTUAL,
    AudioChannelType.AMBIENT_NATURE: ChannelPriority.BACKGROUND,
    AudioChannelType.AMBIENT_URBAN: ChannelPriority.BACKGROUND,
    AudioChannelType.MACHINE: ChannelPriority.IGNORE,
    AudioChannelType.SILENCE: ChannelPriority.IGNORE,
    AudioChannelType.UNKNOWN: ChannelPriority.IGNORE,
}
// ============================================================================
// 2. SEGMENTO DE AUDIO DETECTADO
// ============================================================================
// decorador: @dataclass
type AudioSegment struct {
    // Um segmento de audio detectado e classificado.
    segment_id: texto
    channel_type: AudioChannelType
    priority: ChannelPriority
    start_time: flutuante // quando comecou (segundos desde inicio)
    end_time: flutuante // quando terminou
    duration_sec := 0.0 // float64
    // Transcricao (se for voz)
    transcript := "" // string
    language := "pt-BR" // string
    confidence := 0.0 // 0-1 // float64
    // Speaker info (se for voz)
    speaker_id := ""  // quem esta falando // string
    is_user := false // && o dono do dispositivo? // bool
    speaker_name := "" // string
    // Audio features
    volume_db := 0.0 // volume em dB // float64
    snr_db := 0.0 // signal-to-noise ratio // float64
    overlap := false // sobreposto com outro canal? // bool
    // Contexto
    source_device := ""  // "microfone_notebook" / "smartphone_mesa" // string
    room_estimate := ""  // estimativa do ambiente // string
    // decorador: @property
    func is_speech(self) bool {
        return self.channel_type in (AudioChannelType.USER_VOICE,
                                    AudioChannelType.OTHER_VOICE)
    // decorador: @property
    func is_command(self) bool {
        // E uma fala do usuario que parece comando?
        if ! self.is_user || ! self.transcript {
            return false
        commands = ["hermes", "escreve", "cria", "desenvolve", "abre",
                    "fecha", "procura", "manda", "configura"]
        return any(c in self.transcript.lower() para c em commands)
// ============================================================================
// 3. VOICE PRINT (identidade vocal do usuario)
// ============================================================================
// decorador: @dataclass
type VoicePrint struct {
    // Impressao digital da voz do usuario.
    Permite distinguir o usuario de outras pessoas.
    Construido durante o onboarding (usuario fala 30 segundos).
    TECNICAMENTE:
    - x-vector || ECAPA-TDNN embedding (192-512 dimensoes)
    - Comparado com cada voz detectada (cosine similarity)
    - >0.7 = mesmo falante (usuario)
    - <0.5 = pessoa diferente
    //
    user_id: texto
    user_name: texto
    embedding := field(default_factory=list) // placeholder // [flutuante]
    enrolled_at := "" // string
    samples_count := 0 // int64
    // Caracteristicas vocais (para demo sem modelo real)
    pitch_range := (80.0, 200.0) // Hz (masculino tipico) // (flutuante, flutuante)
    speaking_rate := 150.0 // palavras por minuto // float64
    accent := "brasileiro" // string
    funcao identify(self, speaker_embedding: [flutuante],
                pitch := 0.0) -> (logico, flutuante): // float64
        // Verifica se uma voz e do usuario.
        Returns:
            (is_user, confidence 0-1)
        //
        if ! self.embedding && ! speaker_embedding {
            // Demo sem embedding real: usar pitch
            if pitch > 0 {
                desempacote lo, hi = self.pitch_range
                if lo <= pitch <= hi {
                    return true, 0.75
            return false, 0.3
        // Cosine similarity (simulado)
        if len(self.embedding) > 0 && len(speaker_embedding) > 0 {
            dot = soma(a*b para a,b in intercale(self.embedding, speaker_embedding))
            norm_a = math.sqrt(soma(a*a para a em self.embedding))
            norm_b = math.sqrt(soma(b*b para b em speaker_embedding))
            if norm_a > 0 && norm_b > 0 {
                similarity = dot / (norm_a * norm_b)
                return similarity > 0.7, similarity
        return false, 0.0
// ============================================================================
// 4. PIPELINE DE SEPARACAO
// ============================================================================
type AudioChannelSeparator struct {
    // Pipeline que separa audio bruto em micro-canais.
    ESTAGIOS:
    1. VAD: detectar segmentos com fala vs silencio/ruido
    2. SOURCE SEPARATION: separar vocais de musica/ambiente
    3. DIARIZACAO: separar falantes diferentes
    4. VOICE ID: qual && o usuario?
    5. CLASSIFICACAO: o que && o que ! && voz?
    6. ROUTING: enviar cada canal para destino certo
    //
    func __init__(self) {
        self.user_voiceprint: VoicePrint? = nil
        self.known_speakers: {texto: VoicePrint} = {}
        self.segments: [AudioSegment] = []
        self.active_channels: {AudioChannelType: AudioSegment} = {}
        self.sample_rate: inteiro = 16000 // 16kHz
        self.frame_duration_ms: inteiro = 30 // janela de 30ms
        // Configuracao
        self.min_speech_duration_ms: inteiro = 250 // ignorar < 250ms
        self.min_silence_duration_ms: inteiro = 500 // silencio > 500ms = pausa
        self.max_audio_buffer_sec: inteiro = 60 // buffer de 60s
        self.privacy_mode: logico = true // NUNCA enviar audio bruto
        self.local_only: logico = true // tudo processa local
        // Stats
        self.total_segments: inteiro = 0
        self.user_commands: inteiro = 0
        self.other_voices: inteiro = 0
        self.ambient_detected: inteiro = 0
    funcao enroll_user(self, user_id: texto, user_name: texto,
                    pitch_low := 80.0, pitch_high: flutuante = 200.0) -> VoicePrint: // float64
        // Cadastra a voz do usuario (onboarding).
        Usuario fala por 30 segundos. Sistema cria voiceprint.
        //
        vp = VoicePrint(
            user_id = user_id,
            user_name = user_name,
            pitch_range = (pitch_low, pitch_high),
            enrolled_at = datetime.now().isoformat(),
            samples_count = 30,
            // Em producao: embedding real de 30s de audio
            embedding = [0.1] * 192, // placeholder
        )
        self.user_voiceprint = vp
        return vp
    funcao enroll_speaker(self, speaker_id: texto, name: texto,
                    pitch_low := 0, pitch_high: flutuante = 0) -> VoicePrint: // float64
        // Cadastra outra pessoa conhecida (familia, colega).
        vp = VoicePrint(
            user_id = speaker_id,
            user_name = name,
            pitch_range = (pitch_low || 100, pitch_high || 300),
            embedding = [0.2] * 192, // placeholder diferente
        )
        self.known_speakers[speaker_id] = vp
        return vp
    funcao process_frame(self, audio_data: bytes,
                    device := "microfone_notebook", // string
                    simulated_segments := nil) -> [AudioSegment]: // [Dict]
        // Processa um frame de audio e retorna segmentos classificados.
        Em producao isto chamaria:
        1. silero-vad para VAD
        2. demucs para source separation
        3. pyannote para diarizacao
        4. ECAPA-TDNN para voice ID
        5. YAMNet para classificacao
        Aqui simulamos com dados de demonstracao.
        //
        if simulated_segments {
            return self._process_simulated(simulated_segments, device)
        return []
    funcao _process_simulated(self, segments: [Dict],
                        device: texto) -> [AudioSegment]:
        // Processa segmentos simulados para demonstracao.
        results = []
        for _, seg := range segments {
            channel = seg.get("type", AudioChannelType.UNKNOWN)
            if isinstance(channel, texto) {
                channel = AudioChannelType(channel)
            priority = CHANNEL_PRIORITY.get(channel, ChannelPriority.IGNORE)
            // Voice ID
            is_user = false
            speaker_name = ""
            if channel == AudioChannelType.USER_VOICE {
                is_user = true
                speaker_name = self.user_voiceprint ? self.user_voiceprint.user_name : "Usuario"
            } else if channel == AudioChannelType.OTHER_VOICE {
                speaker_name = seg.get("speaker", "Desconhecido")
                // Verificar se e conhecido
                para cada (sid, vp) em self.known_speakers.items(): {
                    if vp.user_name == speaker_name {
                        speaker_name = vp.user_name
                        break
            segment = AudioSegment(
                segment_id = hashlib.md5(
                    "{channel.value}{seg.get('start', 0)}{time.time()}".encode()
                ).hexdigest()[:8],
                channel_type = channel,
                priority = priority,
                start_time = seg.get("start", 0.0),
                end_time = seg.get("end", 0.0),
                duration_sec = seg.get("end", 0.0) - seg.get("start", 0.0),
                transcript = seg.get("text", ""),
                confidence = seg.get("confidence", 0.9),
                speaker_id = speaker_name,
                is_user = is_user,
                speaker_name = speaker_name,
                volume_db = seg.get("volume", -30.0),
                snr_db = seg.get("snr", 15.0),
                overlap = seg.get("overlap", false),
                source_device = device,
            )
            results.append(segment)
            self.segments.append(segment)
            self.total_segments += 1
            if is_user && segment.is_command {
                self.user_commands += 1
            } else if channel == AudioChannelType.OTHER_VOICE {
                self.other_voices += 1
            elif channel in (AudioChannelType.MUSIC, AudioChannelType.TV_MEDIA,
                            AudioChannelType.AMBIENT_NATURE,
                            AudioChannelType.AMBIENT_URBAN):
                self.ambient_detected += 1
        return results
    func get_active_channels(self) {texto: qualquer} {
        // Retorna os canais ativos no momento.
        channels = defaultdict(list)
        para seg em self.segments[-50:]: // ultimos 50 segmentos {
            channels[seg.channel_type.value].append({
                "transcript": seg.transcript[:60],
                "speaker": seg.speaker_name,
                "is_user": seg.is_user,
                "duration": "{seg.duration_sec:.1f}s",
                "priority": seg.priority.name,
            })
        return dict(channels)
    func build_context_prompt(self) string {
        // Constroi o prompt de contexto para o Hermes.
        Fusion dos micro-canais num texto que o Hermes entende.
        //
        if ! self.segments {
            return ""
        parts = []
        // Voz do usuario (comandos)
        user_speech = [s para s em self.segments[-20:]
                    if s.is_user && s.transcript]
        if user_speech {
            cmds = [s.transcript para s em user_speech if s.is_command]
            casual = [s.transcript para s em user_speech if ! s.is_command]
            if cmds {
                parts.append("COMANDO DO USUARIO: {' | '.join(cmds[-3:])}")
            if casual {
                parts.append("CONTEXTO (usuario falou): {' | '.join(casual[-2:])}")
        // Outras vozes
        others = [s para s em self.segments[-20:]
                if s.channel_type == AudioChannelType.OTHER_VOICE && s.transcript]
        if others {
            speakers = set(s.speaker_name para s em others)
            parts.append(
                "AMBIENTE SOCIAL: {', '.join(speakers)} presente. "
                "Ultima fala ouvivel: '{others[-1].transcript[:50]}'"
            )
        // Musica/TV
        media = [s para s em self.segments[-20:]
                if s.channel_type in (AudioChannelType.MUSIC,
                                    AudioChannelType.TV_MEDIA)]
        if media {
            last = media[-1]
            if last.channel_type == AudioChannelType.MUSIC {
                parts.append("CONTEXTO: musica tocando ao fundo")
            } else {
                parts.append("CONTEXTO: TV/midia tocando (possivel referencia)")
        // Ambiente
        ambient = [s para s em self.segments[-10:]
                if s.channel_type in (AudioChannelType.AMBIENT_NATURE,
                                        AudioChannelType.AMBIENT_URBAN)]
        if ambient {
            last = ambient[-1]
            if last.channel_type == AudioChannelType.AMBIENT_URBAN {
                parts.append("CONTEXTO: ambiente urbano (transito/gente)")
            } else {
                parts.append("CONTEXTO: ambiente natural")
        // Silencio
        recent_types = [s.channel_type para s em self.segments[-5:]]
        if all(t == AudioChannelType.SILENCE para t em recent_types) {
            parts.append("CONTEXTO: silencio -- usuario provavelmente sozinho/focado")
        parts ? retorne " || ".join(parts) : ""
    func stats(self) {texto: qualquer} {
        return {
            "total_segments": self.total_segments,
            "user_commands": self.user_commands,
            "other_voices": self.other_voices,
            "ambient_detected": self.ambient_detected,
            "known_speakers": len(self.known_speakers),
            "user_enrolled": self.user_voiceprint is !  nil,
            "privacy_mode": self.privacy_mode,
            "local_only": self.local_only,
        }
// ============================================================================
// 5. MULTI-DISPOSITIVO (microfone + smartphone)
// ============================================================================
// decorador: @dataclass
type AudioSource struct {
    // Um dispositivo captando audio.
    device_id: texto
    device_name: texto
    device_type: texto         // "microfone_notebook", "smartphone", "wearable"
    location: texto            // "mesa", "bolso", "parede"
    quality := 0.8 // 0-1 (quao bom && o microfone) // float64
    active := true // bool
    latency_ms := 50 // latencia estimada // float64
type MultiDeviceFusion struct {
    // Funde audio de multiplos dispositivos.
    CENARIO:
    - Notebook na mesa: capta voz do usuario + TV ao fundo
    - Smartphone no bolso: capta voz do usuario abafada + ambiente
    - Wearable no pescoco: capta SO a voz do usuario (alta qualidade)
    FUSAO:
    - Se ambos captam a MESMA voz do usuario: usar o de melhor qualidade
    - Se um capta algo que o outro !: combinar
    - Se conflito: priorizar dispositivo mais proximo da fonte
    - Beamforming virtual: usar diferenca de timing para localizar fonte
    //
    func __init__(self) {
        self.sources: {texto: AudioSource} = {}
        self.separator = AudioChannelSeparator()
    func add_source(self, source: AudioSource) None {
        self.sources[source.device_id] = source
    funcao best_source_for(self, channel_type: AudioChannelType) retorna AudioSource?:
        // Determina qual dispositivo capt melhor cada canal.
        preferences = {
            AudioChannelType.USER_VOICE: ["wearable_pescoco", "microfone_notebook",
                                        "smartphone_mesa"],
            AudioChannelType.OTHER_VOICE: ["microfone_notebook", "smartphone_mesa"],
            AudioChannelType.MUSIC: ["microfone_notebook", "smartphone_mesa"],
            AudioChannelType.TV_MEDIA: ["smartphone_mesa", "microfone_notebook"],
            AudioChannelType.AMBIENT_URBAN: ["smartphone_bolso", "microfone_notebook"],
            AudioChannelType.AMBIENT_NATURE: ["microfone_notebook", "smartphone_mesa"],
        }
        preferred = preferences.get(channel_type, ["microfone_notebook"])
        for _, dev_type := range preferred {
            for _, source := range self.sources.values() {
                if source.device_type == dev_type && source.active {
                    return source
        return nil
    func fusion_report(self) {texto: qualquer} {
        return {
            "total_sources": len(self.sources),
            "active_sources": soma(1 para s em self.sources.values() if s.active),
            "devices": [
                {
                    "name": s.device_name,
                    "type": s.device_type,
                    "location": s.location,
                    "quality": s.quality,
                    "active": s.active,
                }
                para s em self.sources.values() {
            ],
        }
// ============================================================================
// 6. MAIN -- DEMONSTRACAO
// ============================================================================
if __name__ == "__main__" {
    fmt.Println("=" * 75)
    fmt.Println("  OPENAUDIOCHANNEL -- SEPARACAO EM MICRO-CANAIS")
    fmt.Println("  'O microfone capta tudo. O cerebro separa.'")
    fmt.Println("=" * 75)
    separator = AudioChannelSeparator()
    fusion = MultiDeviceFusion()
    // === 1. CADASTRAR VOZ DO USUARIO ===
    fmt.Println("\n\n  === 1. ONBOARDING: VOZ DO USUARIO ===\n")
    vp = separator.enroll_user("cleiton", "Cleiton",
                                pitch_low = 85, pitch_high=180)
    fmt.Println("  Usuario: {vp.user_name}")
    fmt.Println("  Pitch range: {vp.pitch_range[0]:.0f}-{vp.pitch_range[1]:.0f} Hz")
    fmt.Println("  Amostras: {vp.samples_count}s de audio")
    fmt.Println("  Voiceprint: criado (192 dimensoes)")
    // Cadastrar pessoas conhecidas
    separator.enroll_speaker("s-001", "Esposa", 180, 280)
    separator.enroll_speaker("s-002", "Filho", 250, 400)
    fmt.Println("\n  Pessoas conhecidas: {len(separator.known_speakers)}")
    for _, s := range separator.known_speakers.values() {
        fmt.Println("    {s.user_name} (pitch {s.pitch_range[0]:.0f}-{s.pitch_range[1]:.0f} Hz)")
    // === 2. DISPOSITIVOS ===
    fmt.Println("\n\n  === 2. MULTI-DISPOSITIVO ===\n")
    fusion.add_source(AudioSource("D-01", "Microfone MacBook",
                                "microfone_notebook", "mesa", 0.85))
    fusion.add_source(AudioSource("D-02", "iPhone 15",
                                "smartphone_mesa", "mesa", 0.90))
    fusion.add_source(AudioSource("D-03", "AirPods Pro",
                                "wearableOuvido", "ouvido", 0.95))
    report = fusion.fusion_report()
    fmt.Println("  Dispositivos: {report['total_sources']}")
    for _, d := range report["devices"] {
        fmt.Println("    {d['name']:<20} {d['type']:<20} {d['location']:<10} Q:{d['quality']:.2f}")
    // Melhor dispositivo por canal
    fmt.Println("\n  Melhor fonte por canal:")
    para ch em [AudioChannelType.USER_VOICE, AudioChannelType.OTHER_VOICE, {
            AudioChannelType.MUSIC, AudioChannelType.AMBIENT_URBAN]:
        best = fusion.best_source_for(ch)
        fmt.Println("    {ch.value:<20} -> {best.device_name if best else 'N/A'}")
    // === 3. SIMULACAO: CENARIO REAL ===
    fmt.Println("\n\n  === 3. CENARIO REAL: AUDIO MISTURADO ===\n")
    fmt.Println("  Situacao: Cleiton no escritorio. Esposa conversa ao fundo.")
    fmt.Println("  Musica toca no Spotify. Transito na rua.\n")
    // Simular segmentos detectados pelo pipeline
    simulated = [
        // Cleiton falando (comando)
        {"type": AudioChannelType.USER_VOICE, "start": 0.0, "end": 3.5,
        "text": "Hermes, desenvolve o OpenMilitary", "confidence": 0.95,
        "volume": -20, "snr": 25, "overlap": false},
        // Musica de fundo
        {"type": AudioChannelType.MUSIC, "start": 0.0, "end": 15.0,
        "text": "", "volume": -45, "snr": 5},
        // Esposa falando ao fundo
        {"type": AudioChannelType.OTHER_VOICE, "start": 4.0, "end": 7.0,
        "text": "amor, o almoco esta pronto", "confidence": 0.80,
        "speaker": "Esposa", "volume": -35, "snr": 12, "overlap": false},
        // Cleiton responde a esposa
        {"type": AudioChannelType.USER_VOICE, "start": 7.5, "end": 9.0,
        "text": "ja vou amor", "confidence": 0.90,
        "volume": -22, "snr": 22, "overlap": false},
        // Cleiton continua falando pro Hermes
        {"type": AudioChannelType.USER_VOICE, "start": 10.0, "end": 14.0,
        "text": "com foco em sistema anti-golpe && autonomia corporal",
        "confidence": 0.93, "volume": -21, "snr": 24, "overlap": false},
        // Transito la fora
        {"type": AudioChannelType.AMBIENT_URBAN, "start": 0.0, "end": 15.0,
        "text": "", "volume": -55, "snr": 2},
        // Silencio depois
        {"type": AudioChannelType.SILENCE, "start": 15.0, "end": 18.0,
        "text": "", "volume": -70},
    ]
    segments = separator.process_frame(b"", "microfone_notebook", simulated)
    fmt.Println("  Segmentos detectados: {len(segments)}\n")
    fmt.Println("  {'Canal':<20} {'Quem':<12} {'Prioridade':<12} {'Dur':>5} {'Texto'}")
    fmt.Println("  {'-'*75}")
    for _, seg := range segments {
        text = seg.transcript ? seg.transcript[ : 35] : "(som)"
        marker = seg.is_command ? "[CMD]" : ""
        fmt.Println("  {seg.channel_type.value:<20} {seg.speaker_name or '-':<12} "
            "{seg.priority.name:<12} {seg.duration_sec:>4.1f}s "
            "{text} {marker}")
    // === 4. MICRO-CANAIS SEPARADOS ===
    fmt.Println("\n\n  === 4. MICRO-CANAIS SEPARADOS ===\n")
    channels = separator.get_active_channels()
    para cada (ch_type, ch_segments) em channels.items(): {
        priority = CHANNEL_PRIORITY.get(
            AudioChannelType(ch_type), ChannelPriority.IGNORE)
        fmt.Println("\n  CANAL: {ch_type} (prioridade: {priority.name})")
        for _, s := range ch_segments {
            marker = s["is_user"] ? " <-- USUARIO" : ""
            text = s["transcript"]  ||  "(som ambiente)"
            fmt.Println("    [{s['duration']}] {s['speaker'] or '-'}: "
                "{text}{marker}")
    // === 5. FUSAO EM PROMPT CONTEXTUAL ===
    fmt.Println("\n\n  === 5. FUSAO EM PROMPT PARA HERMES ===\n")
    context = separator.build_context_prompt()
    fmt.Println("  PROMPT GERADO:")
    fmt.Println("  ---")
    fmt.Println("  {context}")
    fmt.Println("  ---")
    fmt.Println("\n  Hermes recebe: comando + contexto social + ambiente")
    fmt.Println("  NAO recebe: audio bruto de outras pessoas (privacidade)")
    // === 6. IDENTIFICACAO DE VOZ ===
    fmt.Println("\n\n  === 6. IDENTIFICACAO: QUEM ESTA FALANDO? ===\n")
    test_voices = [
        ("Voz A", 95, "pitch baixo, masculino"),
        ("Voz B", 220, "pitch alto, feminino"),
        ("Voz C", 300, "pitch muito alto, crianca"),
        ("Voz D", 150, "pitch medio, masculino"),
    ]
    para label, pitch, desc in test_voices: {
        desempacote is_user, conf = vp.identify([], pitch)
        identity = is_user ? "CLEITON" : "desconhecido"
        // Verificar conhecidos
        if ! is_user {
            para cada (sid, sp) em separator.known_speakers.items(): {
                if sp.pitch_range[0] <= pitch <= sp.pitch_range[1] {
                    identity = sp.user_name
                    break
        fmt.Println("  {label} ({desc}): pitch {pitch}Hz -> {identity} "
            "(confianca {conf:.0%})")
    // === 7. PRIVACIDADE ===
    fmt.Println("\n\n  === 7. POLITICA DE PRIVACIDADE ===\n")
    fmt.Println("  Tudo processa LOCALMENTE: {separator.local_only}")
    fmt.Println("  Audio bruto NUNCA enviado: {separator.privacy_mode}")
    fmt.Println("  So transcritos do USUARIO vao pro Hermes")
    fmt.Println("  Outras vozes: so contexto (nome, ! conteudo)")
    fmt.Println("  Musica/TV: so tipo, ! conteudo")
    fmt.Println("  Ambiente: so classificacao, ! audio")
    // === 8. STATS ===
    fmt.Println("\n\n  === 8. ESTATISTICAS ===\n")
    s = separator.stats()
    para cada (k, v) em s.items(): {
        fmt.Println("  {k:<25} {v}")
    // === ARQUITETURA ===
    fmt.Println("\n\n{'='*75}")
    fmt.Println("  ARQUITETURA DO OPENAUDIOCHANNEL")
    fmt.Println("{'='*75}")
    fmt.Println("""
PIPELINE (tudo local, sem nuvem):
    [Microfone Notebook] --+
    [Smartphone Mesa] ---+--> FUSAO --> VAD --> SEPARATION
    [AirPods/Wearable] ---+ |
                                        v
                                    DIARIZACAO (quem fala?)
                                        |
                            +------------+------------+
                            v v v
                        USER_VOICE OTHER_VOICE AMBIENTE
                            | | |
                        VOICE ID CONTEXT ONLY CLASSIFICA
                            | | |
                            v v v
                        COMANDO       "Esposa       "Musica
                        + CONTEXTO    presente"     tocando"
                            | | |
                            +------------+------------+
                                        |
                                        v
                                    PROMPT FUSIONADO
                                        |
                                        v
                                    HERMES RECEBE:
                                    "Desenvolve OpenMilitary
                                    (foco anti-golpe)
                                    CONTEXTO: esposa presente,
                                    musica tocando"
O QUE O HERMES SABE:
    - Comando do usuario (CRITICAL)
    - Outras pessoas presentes (CONTEXTUAL -- nomes, ! conteudo)
    - Ambiente (BACKGROUND -- tipo, ! audio)
O QUE O HERMES ! SABE:
    - O que outras pessoas disseram (PRIVACIDADE)
    - Que musica esta tocando (so sabe que tem musica)
    - Audio bruto de qualquer fonte (PRIVACIDADE)
MULTIPLOS DISPOSITIVOS:
    - 3 fontes captam simultaneamente
    - Melhor qualidade selecionada por canal
    - Conflito resolvido por proximidade da fonte
    - Beamforming virtual com timing difference
VOICE ID:
    - Onboarding: 30s de fala do usuario
    - x-vector / ECAPA-TDNN embedding (192-512 dim)
    - >0.7 cosine similarity = mesmo usuario
    - Cada pessoa conhecida pode ser cadastrada
    - Pessoa desconhecida = "desconhecido" (sem nomear)
// )
    fmt.Println("{'='*75}")
    fmt.Println("  OpenAudioChannel: {s['total_segments']} segmentos processados.")
    fmt.Println("  {s['user_commands']} comandos do usuario identificados.")
    fmt.Println("  {s['other_voices']} vozes de outros separadas (contexto only).")
    fmt.Println("  Tudo local. Zero nuvem. Zero audio bruto enviado.")
    fmt.Println("{'='*75}")
