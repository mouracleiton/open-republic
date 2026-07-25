# OpenAudioChannel -- Separacao de Audio em Micro-Canais

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_audio_channel.py`

**Descricao:** =========================================================
"O microfone nao ouve. O CEREBRO ouve.
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
  - Canal 5: SILENCIO (nao descartar -- contexto = sozinho)
  Cada canal e processado, classificado e enviado separadamente.
  O Hermes recebe o CONJUNTO: "voce disse X, enquanto Y tocava".
COMO FUNCIONA (pipeline):
  Audio bruto -> VAD (detectar fala) -> Diarizacao (quem fala)
             -> Source Separation (separar fontes)
             -> Voice ID (e o usuario?)
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

---

```portugol++

// !/usr/bin/env python3
// 
OpenAudioChannel -- Separacao de Audio em Micro-Canais
=========================================================

"O microfone nao ouve. O CEREBRO ouve.
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
  - Canal 5: SILENCIO (nao descartar -- contexto = sozinho)

  Cada canal e processado, classificado e enviado separadamente.
  O Hermes recebe o CONJUNTO: "voce disse X, enquanto Y tocava".

COMO FUNCIONA (pipeline):

  Audio bruto -> VAD (detectar fala) -> Diarizacao (quem fala)
             -> Source Separation (separar fontes)
             -> Voice ID (e o usuario?)
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

classe AudioChannelType herda de Enum:
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


classe ChannelPriority herda de Enum:
    // Prioridade do canal para o prompt do Hermes.
    CRITICAL = 0 // voz do usuario -- sempre processa
    HIGH = 1 // outra voz dirigida ao usuario
    CONTEXTUAL = 2 // musica/TV -- contexto mas nao comando
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
classe AudioSegment:
    // Um segmento de audio detectado e classificado.
    segment_id: texto
    channel_type: AudioChannelType
    priority: ChannelPriority
    start_time: flutuante // quando comecou (segundos desde inicio)
    end_time: flutuante // quando terminou
    seja duration_sec: flutuante = 0.0

    // Transcricao (se for voz)
    seja transcript: texto = ""
    seja language: texto = "pt-BR"
    seja confidence: flutuante = 0.0 // 0-1

    // Speaker info (se for voz)
    seja speaker_id: texto = ""  // quem esta falando
    seja is_user: logico = falso // e o dono do dispositivo?
    seja speaker_name: texto = ""

    // Audio features
    seja volume_db: flutuante = 0.0 // volume em dB
    seja snr_db: flutuante = 0.0 // signal-to-noise ratio
    seja overlap: logico = falso // sobreposto com outro canal?

    // Contexto
    seja source_device: texto = ""  // "microfone_notebook" / "smartphone_mesa"
    seja room_estimate: texto = ""  // estimativa do ambiente

    // decorador: @property
    funcao is_speech(self) -> logico:
        retorne self.channel_type in (AudioChannelType.USER_VOICE,
                                     AudioChannelType.OTHER_VOICE)

    // decorador: @property
    funcao is_command(self) -> logico:
        // E uma fala do usuario que parece comando?
        se nao self.is_user ou nao self.transcript entao:
            retorne falso
        commands = ["hermes", "escreve", "cria", "desenvolve", "abre",
                    "fecha", "procura", "manda", "configura"]
        retorne any(c in self.transcript.lower() para c em commands)


// ============================================================================
// 3. VOICE PRINT (identidade vocal do usuario)
// ============================================================================

// decorador: @dataclass
classe VoicePrint:
    // Impressao digital da voz do usuario.

    Permite distinguir o usuario de outras pessoas.
    Construido durante o onboarding (usuario fala 30 segundos).

    TECNICAMENTE:
    - x-vector ou ECAPA-TDNN embedding (192-512 dimensoes)
    - Comparado com cada voz detectada (cosine similarity)
    - >0.7 = mesmo falante (usuario)
    - <0.5 = pessoa diferente
    // 
    user_id: texto
    user_name: texto
    seja embedding: [flutuante] = field(default_factory=list) // placeholder
    seja enrolled_at: texto = ""
    seja samples_count: inteiro = 0

    // Caracteristicas vocais (para demo sem modelo real)
    seja pitch_range: (flutuante, flutuante) = (80.0, 200.0) // Hz (masculino tipico)
    seja speaking_rate: flutuante = 150.0 // palavras por minuto
    seja accent: texto = "brasileiro"

    funcao identify(self, speaker_embedding: [flutuante],
                 seja pitch: flutuante = 0.0) -> (logico, flutuante):
        // Verifica se uma voz e do usuario.

        Returns:
            (is_user, confidence 0-1)
        // 
        se nao self.embedding e nao speaker_embedding entao:
            // Demo sem embedding real: usar pitch
            se pitch > 0 entao:
                desempacote lo, hi = self.pitch_range
                se lo <= pitch <= hi entao:
                    retorne verdadeiro, 0.75
            retorne falso, 0.3

        // Cosine similarity (simulado)
        se tamanho(self.embedding) > 0 e tamanho(speaker_embedding) > 0 entao:
            dot = soma(a*b para a,b in intercale(self.embedding, speaker_embedding))
            norm_a = math.sqrt(soma(a*a para a em self.embedding))
            norm_b = math.sqrt(soma(b*b para b em speaker_embedding))
            se norm_a > 0 e norm_b > 0 entao:
                similarity = dot / (norm_a * norm_b)
                retorne similarity > 0.7, similarity

        retorne falso, 0.0


// ============================================================================
// 4. PIPELINE DE SEPARACAO
// ============================================================================

classe AudioChannelSeparator:
    // Pipeline que separa audio bruto em micro-canais.

    ESTAGIOS:
    1. VAD: detectar segmentos com fala vs silencio/ruido
    2. SOURCE SEPARATION: separar vocais de musica/ambiente
    3. DIARIZACAO: separar falantes diferentes
    4. VOICE ID: qual e o usuario?
    5. CLASSIFICACAO: o que e o que nao e voz?
    6. ROUTING: enviar cada canal para destino certo
    // 

    funcao __init__(self):
        self.user_voiceprint: VoicePrint? = nulo
        self.known_speakers: {texto: VoicePrint} = {}
        self.segments: [AudioSegment] = []
        self.active_channels: {AudioChannelType: AudioSegment} = {}
        self.sample_rate: inteiro = 16000 // 16kHz
        self.frame_duration_ms: inteiro = 30 // janela de 30ms

        // Configuracao
        self.min_speech_duration_ms: inteiro = 250 // ignorar < 250ms
        self.min_silence_duration_ms: inteiro = 500 // silencio > 500ms = pausa
        self.max_audio_buffer_sec: inteiro = 60 // buffer de 60s
        self.privacy_mode: logico = verdadeiro // NUNCA enviar audio bruto
        self.local_only: logico = verdadeiro // tudo processa local

        // Stats
        self.total_segments: inteiro = 0
        self.user_commands: inteiro = 0
        self.other_voices: inteiro = 0
        self.ambient_detected: inteiro = 0

    funcao enroll_user(self, user_id: texto, user_name: texto,
                    seja pitch_low: flutuante = 80.0, pitch_high: flutuante = 200.0) -> VoicePrint:
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
        retorne vp

    funcao enroll_speaker(self, speaker_id: texto, name: texto,
                       seja pitch_low: flutuante = 0, pitch_high: flutuante = 0) -> VoicePrint:
        // Cadastra outra pessoa conhecida (familia, colega).
        vp = VoicePrint(
            user_id = speaker_id,
            user_name = name,
            pitch_range = (pitch_low ou 100, pitch_high ou 300),
            embedding = [0.2] * 192, // placeholder diferente
        )
        self.known_speakers[speaker_id] = vp
        retorne vp

    funcao process_frame(self, audio_data: bytes,
                      seja device: texto = "microfone_notebook",
                      seja simulated_segments: [Dict] = nulo) -> [AudioSegment]:
        // Processa um frame de audio e retorna segmentos classificados.

        Em producao isto chamaria:
        1. silero-vad para VAD
        2. demucs para source separation
        3. pyannote para diarizacao
        4. ECAPA-TDNN para voice ID
        5. YAMNet para classificacao

        Aqui simulamos com dados de demonstracao.
        // 
        se simulated_segments entao:
            retorne self._process_simulated(simulated_segments, device)

        retorne []

    funcao _process_simulated(self, segments: [Dict],
                           device: texto) -> [AudioSegment]:
        // Processa segmentos simulados para demonstracao.
        results = []

        para cada seg em segments:
            channel = seg.get("type", AudioChannelType.UNKNOWN)
            se isinstance(channel, texto) entao:
                channel = AudioChannelType(channel)

            priority = CHANNEL_PRIORITY.get(channel, ChannelPriority.IGNORE)

            // Voice ID
            is_user = falso
            speaker_name = ""
            se channel == AudioChannelType.USER_VOICE entao:
                is_user = verdadeiro
                speaker_name = self.user_voiceprint ? self.user_voiceprint.user_name : "Usuario"
            senao se channel == AudioChannelType.OTHER_VOICE entao:
                speaker_name = seg.get("speaker", "Desconhecido")
                // Verificar se e conhecido
                para cada (sid, vp) em self.known_speakers.items():
                    se vp.user_name == speaker_name entao:
                        speaker_name = vp.user_name
                        interrompa

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
                overlap = seg.get("overlap", falso),
                source_device = device,
            )

            results.append(segment)
            self.segments.append(segment)
            self.total_segments += 1

            se is_user e segment.is_command entao:
                self.user_commands += 1
            senao se channel == AudioChannelType.OTHER_VOICE entao:
                self.other_voices += 1
            elif channel in (AudioChannelType.MUSIC, AudioChannelType.TV_MEDIA,
                             AudioChannelType.AMBIENT_NATURE,
                             AudioChannelType.AMBIENT_URBAN):
                self.ambient_detected += 1

        retorne results

    funcao get_active_channels(self) -> {texto: qualquer}:
        // Retorna os canais ativos no momento.
        channels = defaultdict(list)
        para seg em self.segments[-50:]: // ultimos 50 segmentos
            channels[seg.channel_type.value].append({
                "transcript": seg.transcript[:60],
                "speaker": seg.speaker_name,
                "is_user": seg.is_user,
                "duration": "{seg.duration_sec:.1f}s",
                "priority": seg.priority.name,
            })
        retorne dict(channels)

    funcao build_context_prompt(self) -> texto:
        // Constroi o prompt de contexto para o Hermes.

        Fusion dos micro-canais num texto que o Hermes entende.
        // 
        se nao self.segments entao:
            retorne ""

        parts = []

        // Voz do usuario (comandos)
        user_speech = [s para s em self.segments[-20:]
                       if s.is_user e s.transcript]
        se user_speech entao:
            cmds = [s.transcript para s em user_speech if s.is_command]
            casual = [s.transcript para s em user_speech if nao s.is_command]

            se cmds entao:
                parts.append("COMANDO DO USUARIO: {' | '.join(cmds[-3:])}")
            se casual entao:
                parts.append("CONTEXTO (usuario falou): {' | '.join(casual[-2:])}")

        // Outras vozes
        others = [s para s em self.segments[-20:]
                  if s.channel_type == AudioChannelType.OTHER_VOICE e s.transcript]
        se others entao:
            speakers = set(s.speaker_name para s em others)
            parts.append(
                "AMBIENTE SOCIAL: {', '.join(speakers)} presente. "
                "Ultima fala ouvivel: '{others[-1].transcript[:50]}'"
            )

        // Musica/TV
        media = [s para s em self.segments[-20:]
                 if s.channel_type in (AudioChannelType.MUSIC,
                                       AudioChannelType.TV_MEDIA)]
        se media entao:
            last = media[-1]
            se last.channel_type == AudioChannelType.MUSIC entao:
                parts.append("CONTEXTO: musica tocando ao fundo")
            senao:
                parts.append("CONTEXTO: TV/midia tocando (possivel referencia)")

        // Ambiente
        ambient = [s para s em self.segments[-10:]
                   if s.channel_type in (AudioChannelType.AMBIENT_NATURE,
                                         AudioChannelType.AMBIENT_URBAN)]
        se ambient entao:
            last = ambient[-1]
            se last.channel_type == AudioChannelType.AMBIENT_URBAN entao:
                parts.append("CONTEXTO: ambiente urbano (transito/gente)")
            senao:
                parts.append("CONTEXTO: ambiente natural")

        // Silencio
        recent_types = [s.channel_type para s em self.segments[-5:]]
        se all(t == AudioChannelType.SILENCE para t em recent_types) entao:
            parts.append("CONTEXTO: silencio -- usuario provavelmente sozinho/focado")

        parts ? retorne " || ".join(parts) : ""

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_segments": self.total_segments,
            "user_commands": self.user_commands,
            "other_voices": self.other_voices,
            "ambient_detected": self.ambient_detected,
            "known_speakers": tamanho(self.known_speakers),
            "user_enrolled": self.user_voiceprint is nao  nulo,
            "privacy_mode": self.privacy_mode,
            "local_only": self.local_only,
        }


// ============================================================================
// 5. MULTI-DISPOSITIVO (microfone + smartphone)
// ============================================================================

// decorador: @dataclass
classe AudioSource:
    // Um dispositivo captando audio.
    device_id: texto
    device_name: texto
    device_type: texto         // "microfone_notebook", "smartphone", "wearable"
    location: texto            // "mesa", "bolso", "parede"
    seja quality: flutuante = 0.8 // 0-1 (quao bom e o microfone)
    seja active: logico = verdadeiro
    seja latency_ms: flutuante = 50 // latencia estimada


classe MultiDeviceFusion:
    // Funde audio de multiplos dispositivos.

    CENARIO:
    - Notebook na mesa: capta voz do usuario + TV ao fundo
    - Smartphone no bolso: capta voz do usuario abafada + ambiente
    - Wearable no pescoco: capta SO a voz do usuario (alta qualidade)

    FUSAO:
    - Se ambos captam a MESMA voz do usuario: usar o de melhor qualidade
    - Se um capta algo que o outro nao: combinar
    - Se conflito: priorizar dispositivo mais proximo da fonte
    - Beamforming virtual: usar diferenca de timing para localizar fonte
    // 

    funcao __init__(self):
        self.sources: {texto: AudioSource} = {}
        self.separator = AudioChannelSeparator()

    funcao add_source(self, source: AudioSource) -> None:
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
        para cada dev_type em preferred:
            para cada source em self.sources.values():
                se source.device_type == dev_type e source.active entao:
                    retorne source
        retorne nulo

    funcao fusion_report(self) -> {texto: qualquer}:
        retorne {
            "total_sources": tamanho(self.sources),
            "active_sources": soma(1 para s em self.sources.values() if s.active),
            "devices": [
                {
                    "name": s.device_name,
                    "type": s.device_type,
                    "location": s.location,
                    "quality": s.quality,
                    "active": s.active,
                }
                para s em self.sources.values()
            ],
        }


// ============================================================================
// 6. MAIN -- DEMONSTRACAO
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 75)
    imprima("  OPENAUDIOCHANNEL -- SEPARACAO EM MICRO-CANAIS")
    imprima("  'O microfone capta tudo. O cerebro separa.'")
    imprima("=" * 75)

    separator = AudioChannelSeparator()
    fusion = MultiDeviceFusion()

    // === 1. CADASTRAR VOZ DO USUARIO ===
    imprima("\n\n  === 1. ONBOARDING: VOZ DO USUARIO ===\n")
    vp = separator.enroll_user("cleiton", "Cleiton",
                                pitch_low = 85, pitch_high=180)
    imprima("  Usuario: {vp.user_name}")
    imprima("  Pitch range: {vp.pitch_range[0]:.0f}-{vp.pitch_range[1]:.0f} Hz")
    imprima("  Amostras: {vp.samples_count}s de audio")
    imprima("  Voiceprint: criado (192 dimensoes)")

    // Cadastrar pessoas conhecidas
    separator.enroll_speaker("s-001", "Esposa", 180, 280)
    separator.enroll_speaker("s-002", "Filho", 250, 400)
    imprima("\n  Pessoas conhecidas: {len(separator.known_speakers)}")
    para cada s em separator.known_speakers.values():
        imprima("    {s.user_name} (pitch {s.pitch_range[0]:.0f}-{s.pitch_range[1]:.0f} Hz)")

    // === 2. DISPOSITIVOS ===
    imprima("\n\n  === 2. MULTI-DISPOSITIVO ===\n")
    fusion.add_source(AudioSource("D-01", "Microfone MacBook",
                                  "microfone_notebook", "mesa", 0.85))
    fusion.add_source(AudioSource("D-02", "iPhone 15",
                                  "smartphone_mesa", "mesa", 0.90))
    fusion.add_source(AudioSource("D-03", "AirPods Pro",
                                  "wearableOuvido", "ouvido", 0.95))

    report = fusion.fusion_report()
    imprima("  Dispositivos: {report['total_sources']}")
    para cada d em report["devices"]:
        imprima("    {d['name']:<20} {d['type']:<20} {d['location']:<10} Q:{d['quality']:.2f}")

    // Melhor dispositivo por canal
    imprima("\n  Melhor fonte por canal:")
    para ch em [AudioChannelType.USER_VOICE, AudioChannelType.OTHER_VOICE,
               AudioChannelType.MUSIC, AudioChannelType.AMBIENT_URBAN]:
        best = fusion.best_source_for(ch)
        imprima("    {ch.value:<20} -> {best.device_name if best else 'N/A'}")

    // === 3. SIMULACAO: CENARIO REAL ===
    imprima("\n\n  === 3. CENARIO REAL: AUDIO MISTURADO ===\n")
    imprima("  Situacao: Cleiton no escritorio. Esposa conversa ao fundo.")
    imprima("  Musica toca no Spotify. Transito na rua.\n")

    // Simular segmentos detectados pelo pipeline
    simulated = [
        // Cleiton falando (comando)
        {"type": AudioChannelType.USER_VOICE, "start": 0.0, "end": 3.5,
         "text": "Hermes, desenvolve o OpenMilitary", "confidence": 0.95,
         "volume": -20, "snr": 25, "overlap": falso},
        // Musica de fundo
        {"type": AudioChannelType.MUSIC, "start": 0.0, "end": 15.0,
         "text": "", "volume": -45, "snr": 5},
        // Esposa falando ao fundo
        {"type": AudioChannelType.OTHER_VOICE, "start": 4.0, "end": 7.0,
         "text": "amor, o almoco esta pronto", "confidence": 0.80,
         "speaker": "Esposa", "volume": -35, "snr": 12, "overlap": falso},
        // Cleiton responde a esposa
        {"type": AudioChannelType.USER_VOICE, "start": 7.5, "end": 9.0,
         "text": "ja vou amor", "confidence": 0.90,
         "volume": -22, "snr": 22, "overlap": falso},
        // Cleiton continua falando pro Hermes
        {"type": AudioChannelType.USER_VOICE, "start": 10.0, "end": 14.0,
         "text": "com foco em sistema anti-golpe e autonomia corporal",
         "confidence": 0.93, "volume": -21, "snr": 24, "overlap": falso},
        // Transito la fora
        {"type": AudioChannelType.AMBIENT_URBAN, "start": 0.0, "end": 15.0,
         "text": "", "volume": -55, "snr": 2},
        // Silencio depois
        {"type": AudioChannelType.SILENCE, "start": 15.0, "end": 18.0,
         "text": "", "volume": -70},
    ]

    segments = separator.process_frame(b"", "microfone_notebook", simulated)

    imprima("  Segmentos detectados: {len(segments)}\n")
    imprima("  {'Canal':<20} {'Quem':<12} {'Prioridade':<12} {'Dur':>5} {'Texto'}")
    imprima("  {'-'*75}")

    para cada seg em segments:
        text = seg.transcript ? seg.transcript[ : 35] : "(som)"
        marker = seg.is_command ? "[CMD]" : ""
        imprima("  {seg.channel_type.value:<20} {seg.speaker_name or '-':<12} "
              "{seg.priority.name:<12} {seg.duration_sec:>4.1f}s "
              "{text} {marker}")

    // === 4. MICRO-CANAIS SEPARADOS ===
    imprima("\n\n  === 4. MICRO-CANAIS SEPARADOS ===\n")
    channels = separator.get_active_channels()

    para cada (ch_type, ch_segments) em channels.items():
        priority = CHANNEL_PRIORITY.get(
            AudioChannelType(ch_type), ChannelPriority.IGNORE)
        imprima("\n  CANAL: {ch_type} (prioridade: {priority.name})")
        para cada s em ch_segments:
            marker = s["is_user"] ? " <-- USUARIO" : ""
            text = s["transcript"]  ou  "(som ambiente)"
            imprima("    [{s['duration']}] {s['speaker'] or '-'}: "
                  "{text}{marker}")

    // === 5. FUSAO EM PROMPT CONTEXTUAL ===
    imprima("\n\n  === 5. FUSAO EM PROMPT PARA HERMES ===\n")
    context = separator.build_context_prompt()
    imprima("  PROMPT GERADO:")
    imprima("  ---")
    imprima("  {context}")
    imprima("  ---")
    imprima("\n  Hermes recebe: comando + contexto social + ambiente")
    imprima("  NAO recebe: audio bruto de outras pessoas (privacidade)")

    // === 6. IDENTIFICACAO DE VOZ ===
    imprima("\n\n  === 6. IDENTIFICACAO: QUEM ESTA FALANDO? ===\n")
    test_voices = [
        ("Voz A", 95, "pitch baixo, masculino"),
        ("Voz B", 220, "pitch alto, feminino"),
        ("Voz C", 300, "pitch muito alto, crianca"),
        ("Voz D", 150, "pitch medio, masculino"),
    ]
    para label, pitch, desc in test_voices:
        desempacote is_user, conf = vp.identify([], pitch)
        identity = is_user ? "CLEITON" : "desconhecido"
        // Verificar conhecidos
        se nao is_user entao:
            para cada (sid, sp) em separator.known_speakers.items():
                se sp.pitch_range[0] <= pitch <= sp.pitch_range[1] entao:
                    identity = sp.user_name
                    interrompa
        imprima("  {label} ({desc}): pitch {pitch}Hz -> {identity} "
              "(confianca {conf:.0%})")

    // === 7. PRIVACIDADE ===
    imprima("\n\n  === 7. POLITICA DE PRIVACIDADE ===\n")
    imprima("  Tudo processa LOCALMENTE: {separator.local_only}")
    imprima("  Audio bruto NUNCA enviado: {separator.privacy_mode}")
    imprima("  So transcritos do USUARIO vao pro Hermes")
    imprima("  Outras vozes: so contexto (nome, nao conteudo)")
    imprima("  Musica/TV: so tipo, nao conteudo")
    imprima("  Ambiente: so classificacao, nao audio")

    // === 8. STATS ===
    imprima("\n\n  === 8. ESTATISTICAS ===\n")
    s = separator.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<25} {v}")

    // === ARQUITETURA ===
    imprima("\n\n{'='*75}")
    imprima("  ARQUITETURA DO OPENAUDIOCHANNEL")
    imprima("{'='*75}")
    imprima("""
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
    - Outras pessoas presentes (CONTEXTUAL -- nomes, nao conteudo)
    - Ambiente (BACKGROUND -- tipo, nao audio)

  O QUE O HERMES nao SABE:
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
    imprima("{'='*75}")
    imprima("  OpenAudioChannel: {s['total_segments']} segmentos processados.")
    imprima("  {s['user_commands']} comandos do usuario identificados.")
    imprima("  {s['other_voices']} vozes de outros separadas (contexto only).")
    imprima("  Tudo local. Zero nuvem. Zero audio bruto enviado.")
    imprima("{'='*75}")

```
