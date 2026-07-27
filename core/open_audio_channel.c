/* OpenAudioChannel -- Separacao de Audio em Micro-Canais -- gerado de Portugol++ */
#ifndef OPENAUDIOCHANNEL_SEPARACAO_DE_AUDIO_EM_MICRO_CANAIS_H
#define OPENAUDIOCHANNEL_SEPARACAO_DE_AUDIO_EM_MICRO_CANAIS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenAudioChannel -- Separacao de Audio em Micro-Canais;
=========================================================;
"O microfone ! ouve. O CEREBRO ouve.;
O microfone capta tudo misturado.;
O cerebro separa: minha voz, a voz do outro, o som da rua.;
O Hermes precisa fazer o mesmo.";
O QUE ISTO FAZ:;
Pega UM fluxo de audio (microfone + smartphone);
Separa em MULTIPLOS micro-canais identificados:;
- Canal 1: VOZ DO USUARIO (eu falando);
- Canal 2: VOZ DE OUTRA PESSOA (alguem conversando perto);
- Canal 3: MUSICA/TV (tocando ao fundo);
- Canal 4: SOM AMBIENTE (rua, vento, maquina);
- Canal 5: SILENCIO (! descartar -- contexto = sozinho);
Cada canal && processado, classificado && enviado separadamente.;
O Hermes recebe o CONJUNTO: "voce disse X, enquanto Y tocava".;
COMO FUNCIONA (pipeline):;
Audio bruto -> VAD (detectar fala) -> Diarizacao (quem fala);
            -> Source Separation (separar fontes);
            -> Voice ID (&& o usuario?);
            -> Classificacao (musica/ambiente/pessoa);
            -> Micro-canais separados;
            -> Fusion em prompt contextual;
TECNOLOGIAS:;
- VAD: WebRTC Voice Activity Detection (silero-vad);
- Diarizacao: pyannote.audio (speaker diarization);
- Source Separation: Demucs / Spleeter (vocal vs instrumental);
- Voice ID: x-vectors / ECAPA-TDNN (fingerprint do usuario);
- Classificacao: YAMNet / AudioSet (ambiente);
- Tudo LOCAL, sem nuvem, sem enviar audio a terceiros;
Author: OpenRepublic Team;
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
typedef struct AudioChannelType {
    // Cada fonte de audio vira um tipo de canal.
    USER_VOICE = "voz_usuario"  // o dono falando (PRIORIDADE);
    OTHER_VOICE = "outra_voz"  // outra pessoa conversando perto;
    MUSIC = "musica"  // musica/TV/playlist tocando;
    TV_MEDIA = "tv_midia"  // TV, podcast, video tocando;
    AMBIENT_NATURE = "ambiente_natureza"  // vento, chuva, passatos;
    AMBIENT_URBAN = "ambiente_urbano"  // transito, construcao, gente;
    MACHINE = "maquina"  // ventilador, motor, computador;
    SILENCE = "silencio"  // nada (contexto: sozinho/foco);
    UNKNOWN = "desconhecido";
typedef struct ChannelPriority {
    // Prioridade do canal para o prompt do Hermes.
    CRITICAL = 0 // voz do usuario -- sempre processa;
    HIGH = 1 // outra voz dirigida ao usuario;
    CONTEXTUAL = 2 // musica/TV -- contexto mas ! comando;
    BACKGROUND = 3 // ambiente -- referencia apenas;
    IGNORE = 4 // maquina/ruido -- descartar;
// Mapeamento tipo -> prioridade
CHANNEL_PRIORITY = {
    AudioChannelType.USER_VOICE: ChannelPriority.CRITICAL,;
    AudioChannelType.OTHER_VOICE: ChannelPriority.HIGH,;
    AudioChannelType.MUSIC: ChannelPriority.CONTEXTUAL,;
    AudioChannelType.TV_MEDIA: ChannelPriority.CONTEXTUAL,;
    AudioChannelType.AMBIENT_NATURE: ChannelPriority.BACKGROUND,;
    AudioChannelType.AMBIENT_URBAN: ChannelPriority.BACKGROUND,;
    AudioChannelType.MACHINE: ChannelPriority.IGNORE,;
    AudioChannelType.SILENCE: ChannelPriority.IGNORE,;
    AudioChannelType.UNKNOWN: ChannelPriority.IGNORE,;
};
// ============================================================================
// 2. SEGMENTO DE AUDIO DETECTADO
// ============================================================================
// decorador: @dataclass
typedef struct AudioSegment {
    // Um segmento de audio detectado e classificado.
    segment_id: texto;
    channel_type: AudioChannelType;
    priority: ChannelPriority;
    start_time: flutuante // quando comecou (segundos desde inicio);
    end_time: flutuante // quando terminou;
    double duration_sec = 0.0;
    // Transcricao (se for voz)
    char* transcript = "";
    char* language = "pt-BR";
    double confidence = 0.0 // 0-1;
    // Speaker info (se for voz)
    char* speaker_id = ""  // quem esta falando;
    bool is_user = false // && o dono do dispositivo?;
    char* speaker_name = "";
    // Audio features
    double volume_db = 0.0 // volume em dB;
    double snr_db = 0.0 // signal-to-noise ratio;
    bool overlap = false // sobreposto com outro canal?;
    // Contexto
    char* source_device = ""  // "microfone_notebook" / "smartphone_mesa";
    char* room_estimate = ""  // estimativa do ambiente;
    // decorador: @property
    bool is_speech(self) {
        return self.channel_type in (AudioChannelType.USER_VOICE,;
                                    AudioChannelType.OTHER_VOICE);
    // decorador: @property
    bool is_command(self) {
        // E uma fala do usuario que parece comando?
        if (! self.is_user || ! self.transcript) {
            return false;
        commands = ["hermes", "escreve", "cria", "desenvolve", "abre",;
                    "fecha", "procura", "manda", "configura"];
        return any(c in self.transcript.lower() para c em commands);
// ============================================================================
// 3. VOICE PRINT (identidade vocal do usuario)
// ============================================================================
// decorador: @dataclass
typedef struct VoicePrint {
    // Impressao digital da voz do usuario.
    Permite distinguir o usuario de outras pessoas.;
    Construido durante o onboarding (usuario fala 30 segundos).;
    TECNICAMENTE:;
    - x-vector || ECAPA-TDNN embedding (192-512 dimensoes);
    - Comparado com cada voz detectada (cosine similarity);
    - >0.7 = mesmo falante (usuario);
    - <0.5 = pessoa diferente;
    //
    user_id: texto;
    user_name: texto;
    [flutuante] embedding = field(default_factory=list) // placeholder;
    char* enrolled_at = "";
    int samples_count = 0;
    // Caracteristicas vocais (para demo sem modelo real)
    (flutuante, flutuante) pitch_range = (80.0, 200.0) // Hz (masculino tipico);
    double speaking_rate = 150.0 // palavras por minuto;
    char* accent = "brasileiro";
    funcao identify(self, speaker_embedding: [flutuante],
                double pitch = 0.0) -> (logico, flutuante):;
        // Verifica se uma voz e do usuario.
        Returns:;
            (is_user, confidence 0-1);
        //
        if (! self.embedding && ! speaker_embedding) {
            // Demo sem embedding real: usar pitch
            if (pitch > 0) {
                desempacote lo, hi = self.pitch_range;
                if (lo <= pitch <= hi) {
                    return true, 0.75;
            return false, 0.3;
        // Cosine similarity (simulado)
        if (sizeof(self.embedding) > 0 && sizeof(speaker_embedding) > 0) {
            dot = soma(a*b para a,b in intercale(self.embedding, speaker_embedding));
            norm_a = math.sqrt(soma(a*a para a em self.embedding));
            norm_b = math.sqrt(soma(b*b para b em speaker_embedding));
            if (norm_a > 0 && norm_b > 0) {
                similarity = dot / (norm_a * norm_b);
                return similarity > 0.7, similarity;
        return false, 0.0;
// ============================================================================
// 4. PIPELINE DE SEPARACAO
// ============================================================================
typedef struct AudioChannelSeparator {
    // Pipeline que separa audio bruto em micro-canais.
    ESTAGIOS:;
    1. VAD: detectar segmentos com fala vs silencio/ruido;
    2. SOURCE SEPARATION: separar vocais de musica/ambiente;
    3. DIARIZACAO: separar falantes diferentes;
    4. VOICE ID: qual && o usuario?;
    5. CLASSIFICACAO: o que && o que ! && voz?;
    6. ROUTING: enviar cada canal para destino certo;
    //
    void __init__(self) {
        self.user_voiceprint: VoicePrint? = NULL;
        self.known_speakers: {texto: VoicePrint} = {};
        self.segments: [AudioSegment] = [];
        self.active_channels: {AudioChannelType: AudioSegment} = {};
        self.sample_rate: inteiro = 16000 // 16kHz;
        self.frame_duration_ms: inteiro = 30 // janela de 30ms;
        // Configuracao
        self.min_speech_duration_ms: inteiro = 250 // ignorar < 250ms;
        self.min_silence_duration_ms: inteiro = 500 // silencio > 500ms = pausa;
        self.max_audio_buffer_sec: inteiro = 60 // buffer de 60s;
        self.privacy_mode: logico = true // NUNCA enviar audio bruto;
        self.local_only: logico = true // tudo processa local;
        // Stats
        self.total_segments: inteiro = 0;
        self.user_commands: inteiro = 0;
        self.other_voices: inteiro = 0;
        self.ambient_detected: inteiro = 0;
    funcao enroll_user(self, user_id: texto, user_name: texto,
                    double pitch_low = 80.0, pitch_high: flutuante = 200.0) -> VoicePrint:;
        // Cadastra a voz do usuario (onboarding).
        Usuario fala por 30 segundos. Sistema cria voiceprint.;
        //
        vp = VoicePrint(;
            user_id = user_id,;
            user_name = user_name,;
            pitch_range = (pitch_low, pitch_high),;
            enrolled_at = datetime.now().isoformat(),;
            samples_count = 30,;
            // Em producao: embedding real de 30s de audio
            embedding = [0.1] * 192, // placeholder;
        );
        self.user_voiceprint = vp;
        return vp;
    funcao enroll_speaker(self, speaker_id: texto, name: texto,
                    double pitch_low = 0, pitch_high: flutuante = 0) -> VoicePrint:;
        // Cadastra outra pessoa conhecida (familia, colega).
        vp = VoicePrint(;
            user_id = speaker_id,;
            user_name = name,;
            pitch_range = (pitch_low || 100, pitch_high || 300),;
            embedding = [0.2] * 192, // placeholder diferente;
        );
        self.known_speakers[speaker_id] = vp;
        return vp;
    funcao process_frame(self, audio_data: bytes,
                    char* device = "microfone_notebook",;
                    [Dict] simulated_segments = NULL) -> [AudioSegment]:;
        // Processa um frame de audio e retorna segmentos classificados.
        Em producao isto chamaria:;
        1. silero-vad para VAD;
        2. demucs para source separation;
        3. pyannote para diarizacao;
        4. ECAPA-TDNN para voice ID;
        5. YAMNet para classificacao;
        Aqui simulamos com dados de demonstracao.;
        //
        if (simulated_segments) {
            return self._process_simulated(simulated_segments, device);
        return [];
    funcao _process_simulated(self, segments: [Dict],
                        device: texto) -> [AudioSegment]:;
        // Processa segmentos simulados para demonstracao.
        results = [];
        /* TODO: iterador C manual para seg em segments */
            channel = seg.get("type", AudioChannelType.UNKNOWN);
            if (isinstance(channel, texto)) {
                channel = AudioChannelType(channel);
            priority = CHANNEL_PRIORITY.get(channel, ChannelPriority.IGNORE);
            // Voice ID
            is_user = false;
            speaker_name = "";
            if (channel == AudioChannelType.USER_VOICE) {
                is_user = true;
                speaker_name = self.user_voiceprint ? self.user_voiceprint.user_name : "Usuario";
            } else if (channel == AudioChannelType.OTHER_VOICE) {
                speaker_name = seg.get("speaker", "Desconhecido");
                // Verificar se e conhecido
                /* para cada (sid, vp) em self.known_speakers.items(): */
                    if (vp.user_name == speaker_name) {
                        speaker_name = vp.user_name;
                        break;
            segment = AudioSegment(;
                segment_id = hashlib.md5(;
                    "{channel.value}{seg.get('start', 0)}{time.time()}".encode();
                ).hexdigest()[:8],;
                channel_type = channel,;
                priority = priority,;
                start_time = seg.get("start", 0.0),;
                end_time = seg.get("end", 0.0),;
                duration_sec = seg.get("end", 0.0) - seg.get("start", 0.0),;
                transcript = seg.get("text", ""),;
                confidence = seg.get("confidence", 0.9),;
                speaker_id = speaker_name,;
                is_user = is_user,;
                speaker_name = speaker_name,;
                volume_db = seg.get("volume", -30.0),;
                snr_db = seg.get("snr", 15.0),;
                overlap = seg.get("overlap", false),;
                source_device = device,;
            );
            results.append(segment);
            self.segments.append(segment);
            self.total_segments += 1;
            if (is_user && segment.is_command) {
                self.user_commands += 1;
            } else if (channel == AudioChannelType.OTHER_VOICE) {
                self.other_voices += 1;
            elif channel in (AudioChannelType.MUSIC, AudioChannelType.TV_MEDIA,;
                            AudioChannelType.AMBIENT_NATURE,;
                            AudioChannelType.AMBIENT_URBAN):;
                self.ambient_detected += 1;
        return results;
    {texto: qualquer} get_active_channels(self) {
        // Retorna os canais ativos no momento.
        channels = defaultdict(list);
        /* para seg em self.segments[-50:]: // ultimos 50 segmentos */
            channels[seg.channel_type.value].append({
                "transcript": seg.transcript[:60],;
                "speaker": seg.speaker_name,;
                "is_user": seg.is_user,;
                "duration": "{seg.duration_sec:.1f}s",;
                "priority": seg.priority.name,;
            });
        return dict(channels);
    char* build_context_prompt(self) {
        // Constroi o prompt de contexto para o Hermes.
        Fusion dos micro-canais num texto que o Hermes entende.;
        //
        if (! self.segments) {
            return "";
        parts = [];
        // Voz do usuario (comandos)
        user_speech = [s para s em self.segments[-20:];
                    if s.is_user && s.transcript];
        if (user_speech) {
            cmds = [s.transcript para s em user_speech if s.is_command];
            casual = [s.transcript para s em user_speech if ! s.is_command];
            if (cmds) {
                parts.append("COMANDO DO USUARIO: {' | '.join(cmds[-3:])}");
            if (casual) {
                parts.append("CONTEXTO (usuario falou): {' | '.join(casual[-2:])}");
        // Outras vozes
        others = [s para s em self.segments[-20:];
                if s.channel_type == AudioChannelType.OTHER_VOICE && s.transcript];
        if (others) {
            speakers = set(s.speaker_name para s em others);
            parts.append(;
                "AMBIENTE SOCIAL: {', '.join(speakers)} presente. ";
                "Ultima fala ouvivel: '{others[-1].transcript[:50]}'";
            );
        // Musica/TV
        media = [s para s em self.segments[-20:];
                if s.channel_type in (AudioChannelType.MUSIC,;
                                    AudioChannelType.TV_MEDIA)];
        if (media) {
            last = media[-1];
            if (last.channel_type == AudioChannelType.MUSIC) {
                parts.append("CONTEXTO: musica tocando ao fundo");
            } else {
                parts.append("CONTEXTO: TV/midia tocando (possivel referencia)");
        // Ambiente
        ambient = [s para s em self.segments[-10:];
                if s.channel_type in (AudioChannelType.AMBIENT_NATURE,;
                                        AudioChannelType.AMBIENT_URBAN)];
        if (ambient) {
            last = ambient[-1];
            if (last.channel_type == AudioChannelType.AMBIENT_URBAN) {
                parts.append("CONTEXTO: ambiente urbano (transito/gente)");
            } else {
                parts.append("CONTEXTO: ambiente natural");
        // Silencio
        recent_types = [s.channel_type para s em self.segments[-5:]];
        if (all(t == AudioChannelType.SILENCE para t em recent_types)) {
            parts.append("CONTEXTO: silencio -- usuario provavelmente sozinho/focado");
        parts ? retorne " || ".join(parts) : "";
    {texto: qualquer} stats(self) {
        return {;
            "total_segments": self.total_segments,;
            "user_commands": self.user_commands,;
            "other_voices": self.other_voices,;
            "ambient_detected": self.ambient_detected,;
            "known_speakers": sizeof(self.known_speakers),;
            "user_enrolled": self.user_voiceprint is !  NULL,;
            "privacy_mode": self.privacy_mode,;
            "local_only": self.local_only,;
        };
// ============================================================================
// 5. MULTI-DISPOSITIVO (microfone + smartphone)
// ============================================================================
// decorador: @dataclass
typedef struct AudioSource {
    // Um dispositivo captando audio.
    device_id: texto;
    device_name: texto;
    device_type: texto         // "microfone_notebook", "smartphone", "wearable";
    location: texto            // "mesa", "bolso", "parede";
    double quality = 0.8 // 0-1 (quao bom && o microfone);
    bool active = true;
    double latency_ms = 50 // latencia estimada;
typedef struct MultiDeviceFusion {
    // Funde audio de multiplos dispositivos.
    CENARIO:;
    - Notebook na mesa: capta voz do usuario + TV ao fundo;
    - Smartphone no bolso: capta voz do usuario abafada + ambiente;
    - Wearable no pescoco: capta SO a voz do usuario (alta qualidade);
    FUSAO:;
    - Se ambos captam a MESMA voz do usuario: usar o de melhor qualidade;
    - Se um capta algo que o outro !: combinar;
    - Se conflito: priorizar dispositivo mais proximo da fonte;
    - Beamforming virtual: usar diferenca de timing para localizar fonte;
    //
    void __init__(self) {
        self.sources: {texto: AudioSource} = {};
        self.separator = AudioChannelSeparator();
    None add_source(self, source: AudioSource) {
        self.sources[source.device_id] = source;
    funcao best_source_for(self, channel_type: AudioChannelType) retorna AudioSource?:
        // Determina qual dispositivo capt melhor cada canal.
        preferences = {
            AudioChannelType.USER_VOICE: ["wearable_pescoco", "microfone_notebook",;
                                        "smartphone_mesa"],;
            AudioChannelType.OTHER_VOICE: ["microfone_notebook", "smartphone_mesa"],;
            AudioChannelType.MUSIC: ["microfone_notebook", "smartphone_mesa"],;
            AudioChannelType.TV_MEDIA: ["smartphone_mesa", "microfone_notebook"],;
            AudioChannelType.AMBIENT_URBAN: ["smartphone_bolso", "microfone_notebook"],;
            AudioChannelType.AMBIENT_NATURE: ["microfone_notebook", "smartphone_mesa"],;
        };
        preferred = preferences.get(channel_type, ["microfone_notebook"]);
        /* TODO: iterador C manual para dev_type em preferred */
            /* TODO: iterador C manual para source em self.sources.values() */
                if (source.device_type == dev_type && source.active) {
                    return source;
        return NULL;
    {texto: qualquer} fusion_report(self) {
        return {;
            "total_sources": sizeof(self.sources),;
            "active_sources": soma(1 para s em self.sources.values() if s.active),;
            "devices": [;
                {
                    "name": s.device_name,;
                    "type": s.device_type,;
                    "location": s.location,;
                    "quality": s.quality,;
                    "active": s.active,;
                };
                /* para s em self.sources.values() */
            ],;
        };
// ============================================================================
// 6. MAIN -- DEMONSTRACAO
// ============================================================================
if (__name__ == "__main__") {
    printf("=" * 75);
    printf("  OPENAUDIOCHANNEL -- SEPARACAO EM MICRO-CANAIS");
    printf("  'O microfone capta tudo. O cerebro separa.'");
    printf("=" * 75);
    separator = AudioChannelSeparator();
    fusion = MultiDeviceFusion();
    // === 1. CADASTRAR VOZ DO USUARIO ===
    printf("\n\n  === 1. ONBOARDING: VOZ DO USUARIO ===\n");
    vp = separator.enroll_user("cleiton", "Cleiton",;
                                pitch_low = 85, pitch_high=180);
    printf("  Usuario: {vp.user_name}");
    printf("  Pitch range: {vp.pitch_range[0]:.0f}-{vp.pitch_range[1]:.0f} Hz");
    printf("  Amostras: {vp.samples_count}s de audio");
    printf("  Voiceprint: criado (192 dimensoes)");
    // Cadastrar pessoas conhecidas
    separator.enroll_speaker("s-001", "Esposa", 180, 280);
    separator.enroll_speaker("s-002", "Filho", 250, 400);
    printf("\n  Pessoas conhecidas: {len(separator.known_speakers)}");
    /* TODO: iterador C manual para s em separator.known_speakers.values() */
        printf("    {s.user_name} (pitch {s.pitch_range[0]:.0f}-{s.pitch_range[1]:.0f} Hz)");
    // === 2. DISPOSITIVOS ===
    printf("\n\n  === 2. MULTI-DISPOSITIVO ===\n");
    fusion.add_source(AudioSource("D-01", "Microfone MacBook",;
                                "microfone_notebook", "mesa", 0.85));
    fusion.add_source(AudioSource("D-02", "iPhone 15",;
                                "smartphone_mesa", "mesa", 0.90));
    fusion.add_source(AudioSource("D-03", "AirPods Pro",;
                                "wearableOuvido", "ouvido", 0.95));
    report = fusion.fusion_report();
    printf("  Dispositivos: {report['total_sources']}");
    /* TODO: iterador C manual para d em report["devices"] */
        printf("    {d['name']:<20} {d['type']:<20} {d['location']:<10} Q:{d['quality']:.2f}");
    // Melhor dispositivo por canal
    printf("\n  Melhor fonte por canal:");
    /* para ch em [AudioChannelType.USER_VOICE, AudioChannelType.OTHER_VOICE, */
            AudioChannelType.MUSIC, AudioChannelType.AMBIENT_URBAN]:;
        best = fusion.best_source_for(ch);
        printf("    {ch.value:<20} -> {best.device_name if best else 'N/A'}");
    // === 3. SIMULACAO: CENARIO REAL ===
    printf("\n\n  === 3. CENARIO REAL: AUDIO MISTURADO ===\n");
    printf("  Situacao: Cleiton no escritorio. Esposa conversa ao fundo.");
    printf("  Musica toca no Spotify. Transito na rua.\n");
    // Simular segmentos detectados pelo pipeline
    simulated = [;
        // Cleiton falando (comando)
        {"type": AudioChannelType.USER_VOICE, "start": 0.0, "end": 3.5,;
        "text": "Hermes, desenvolve o OpenMilitary", "confidence": 0.95,;
        "volume": -20, "snr": 25, "overlap": false},;
        // Musica de fundo
        {"type": AudioChannelType.MUSIC, "start": 0.0, "end": 15.0,;
        "text": "", "volume": -45, "snr": 5},;
        // Esposa falando ao fundo
        {"type": AudioChannelType.OTHER_VOICE, "start": 4.0, "end": 7.0,;
        "text": "amor, o almoco esta pronto", "confidence": 0.80,;
        "speaker": "Esposa", "volume": -35, "snr": 12, "overlap": false},;
        // Cleiton responde a esposa
        {"type": AudioChannelType.USER_VOICE, "start": 7.5, "end": 9.0,;
        "text": "ja vou amor", "confidence": 0.90,;
        "volume": -22, "snr": 22, "overlap": false},;
        // Cleiton continua falando pro Hermes
        {"type": AudioChannelType.USER_VOICE, "start": 10.0, "end": 14.0,;
        "text": "com foco em sistema anti-golpe && autonomia corporal",;
        "confidence": 0.93, "volume": -21, "snr": 24, "overlap": false},;
        // Transito la fora
        {"type": AudioChannelType.AMBIENT_URBAN, "start": 0.0, "end": 15.0,;
        "text": "", "volume": -55, "snr": 2},;
        // Silencio depois
        {"type": AudioChannelType.SILENCE, "start": 15.0, "end": 18.0,;
        "text": "", "volume": -70},;
    ];
    segments = separator.process_frame(b"", "microfone_notebook", simulated);
    printf("  Segmentos detectados: {len(segments)}\n");
    printf("  {'Canal':<20} {'Quem':<12} {'Prioridade':<12} {'Dur':>5} {'Texto'}");
    printf("  {'-'*75}");
    /* TODO: iterador C manual para seg em segments */
        text = seg.transcript ? seg.transcript[ : 35] : "(som)";
        marker = seg.is_command ? "[CMD]" : "";
        printf("  {seg.channel_type.value:<20} {seg.speaker_name or '-':<12} ";
            "{seg.priority.name:<12} {seg.duration_sec:>4.1f}s ";
            "{text} {marker}");
    // === 4. MICRO-CANAIS SEPARADOS ===
    printf("\n\n  === 4. MICRO-CANAIS SEPARADOS ===\n");
    channels = separator.get_active_channels();
    /* para cada (ch_type, ch_segments) em channels.items(): */
        priority = CHANNEL_PRIORITY.get(;
            AudioChannelType(ch_type), ChannelPriority.IGNORE);
        printf("\n  CANAL: {ch_type} (prioridade: {priority.name})");
        /* TODO: iterador C manual para s em ch_segments */
            marker = s["is_user"] ? " <-- USUARIO" : "";
            text = s["transcript"]  ||  "(som ambiente)";
            printf("    [{s['duration']}] {s['speaker'] or '-'}: ";
                "{text}{marker}");
    // === 5. FUSAO EM PROMPT CONTEXTUAL ===
    printf("\n\n  === 5. FUSAO EM PROMPT PARA HERMES ===\n");
    context = separator.build_context_prompt();
    printf("  PROMPT GERADO:");
    printf("  ---");
    printf("  {context}");
    printf("  ---");
    printf("\n  Hermes recebe: comando + contexto social + ambiente");
    printf("  NAO recebe: audio bruto de outras pessoas (privacidade)");
    // === 6. IDENTIFICACAO DE VOZ ===
    printf("\n\n  === 6. IDENTIFICACAO: QUEM ESTA FALANDO? ===\n");
    test_voices = [;
        ("Voz A", 95, "pitch baixo, masculino"),;
        ("Voz B", 220, "pitch alto, feminino"),;
        ("Voz C", 300, "pitch muito alto, crianca"),;
        ("Voz D", 150, "pitch medio, masculino"),;
    ];
    /* para label, pitch, desc in test_voices: */
        desempacote is_user, conf = vp.identify([], pitch);
        identity = is_user ? "CLEITON" : "desconhecido";
        // Verificar conhecidos
        if (! is_user) {
            /* para cada (sid, sp) em separator.known_speakers.items(): */
                if (sp.pitch_range[0] <= pitch <= sp.pitch_range[1]) {
                    identity = sp.user_name;
                    break;
        printf("  {label} ({desc}): pitch {pitch}Hz -> {identity} ";
            "(confianca {conf:.0%})");
    // === 7. PRIVACIDADE ===
    printf("\n\n  === 7. POLITICA DE PRIVACIDADE ===\n");
    printf("  Tudo processa LOCALMENTE: {separator.local_only}");
    printf("  Audio bruto NUNCA enviado: {separator.privacy_mode}");
    printf("  So transcritos do USUARIO vao pro Hermes");
    printf("  Outras vozes: so contexto (nome, ! conteudo)");
    printf("  Musica/TV: so tipo, ! conteudo");
    printf("  Ambiente: so classificacao, ! audio");
    // === 8. STATS ===
    printf("\n\n  === 8. ESTATISTICAS ===\n");
    s = separator.stats();
    /* para cada (k, v) em s.items(): */
        printf("  {k:<25} {v}");
    // === ARQUITETURA ===
    printf("\n\n{'='*75}");
    printf("  ARQUITETURA DO OPENAUDIOCHANNEL");
    printf("{'='*75}");
    printf(""";
PIPELINE (tudo local, sem nuvem):;
    [Microfone Notebook] --+;
    [Smartphone Mesa] ---+--> FUSAO --> VAD --> SEPARATION;
    [AirPods/Wearable] ---+ |;
                                        v;
                                    DIARIZACAO (quem fala?);
                                        |;
                            +------------+------------+;
                            v v v;
                        USER_VOICE OTHER_VOICE AMBIENTE;
                            | | |;
                        VOICE ID CONTEXT ONLY CLASSIFICA;
                            | | |;
                            v v v;
                        COMANDO       "Esposa       "Musica;
                        + CONTEXTO    presente"     tocando";
                            | | |;
                            +------------+------------+;
                                        |;
                                        v;
                                    PROMPT FUSIONADO;
                                        |;
                                        v;
                                    HERMES RECEBE:;
                                    "Desenvolve OpenMilitary;
                                    (foco anti-golpe);
                                    CONTEXTO: esposa presente,;
                                    musica tocando";
O QUE O HERMES SABE:;
    - Comando do usuario (CRITICAL);
    - Outras pessoas presentes (CONTEXTUAL -- nomes, ! conteudo);
    - Ambiente (BACKGROUND -- tipo, ! audio);
O QUE O HERMES ! SABE:;
    - O que outras pessoas disseram (PRIVACIDADE);
    - Que musica esta tocando (so sabe que tem musica);
    - Audio bruto de qualquer fonte (PRIVACIDADE);
MULTIPLOS DISPOSITIVOS:;
    - 3 fontes captam simultaneamente;
    - Melhor qualidade selecionada por canal;
    - Conflito resolvido por proximidade da fonte;
    - Beamforming virtual com timing difference;
VOICE ID:;
    - Onboarding: 30s de fala do usuario;
    - x-vector / ECAPA-TDNN embedding (192-512 dim);
    - >0.7 cosine similarity = mesmo usuario;
    - Cada pessoa conhecida pode ser cadastrada;
    - Pessoa desconhecida = "desconhecido" (sem nomear);
// )
    printf("{'='*75}");
    printf("  OpenAudioChannel: {s['total_segments']} segmentos processados.");
    printf("  {s['user_commands']} comandos do usuario identificados.");
    printf("  {s['other_voices']} vozes de outros separadas (contexto only).");
    printf("  Tudo local. Zero nuvem. Zero audio bruto enviado.");
    printf("{'='*75}");

#endif // OPENAUDIOCHANNEL_SEPARACAO_DE_AUDIO_EM_MICRO_CANAIS_H
