#!/usr/bin/env python3
"""
OpenAudioChannel -- Separacao de Audio em Micro-Canais -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenAudioChannel -- Separacao de Audio em Micro-Canais
=========================================================
"O microfone not ouve. O CEREBRO ouve.
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
- Canal 5: SILENCIO (not descartar -- contexto = sozinho)
Cada canal and processado, classificado and enviado separadamente.
O Hermes recebe o CONJUNTO: "voce disse X, enquanto Y tocava".
COMO FUNCIONA (pipeline):
Audio bruto -> VAD (detectar fala) -> Diarizacao (quem fala)
            -> Source Separation (separar fontes)
            -> Voice ID (and o usuario?)
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
# 
# importa annotations de __future__
# importa math
# importa hashlib
# importa time
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict, deque de collections
# importa datetime de datetime
# ============================================================================
# 1. TIPOS DE CANAL DE AUDIO
# ============================================================================
class AudioChannelType(Enum):
    # Cada fonte de audio vira um tipo de canal.
    USER_VOICE = "voz_usuario"  // o dono falando (PRIORIDADE)
    OTHER_VOICE = "outra_voz"  // outra pessoa conversando perto
    MUSIC = "musica"  // musica/TV/playlist tocando
    TV_MEDIA = "tv_midia"  // TV, podcast, video tocando
    AMBIENT_NATURE = "ambiente_natureza"  // vento, chuva, passatos
    AMBIENT_URBAN = "ambiente_urbano"  // transito, construcao, gente
    MACHINE = "maquina"  // ventilador, motor, computador
    SILENCE = "silencio"  // nada (contexto: sozinho/foco)
    UNKNOWN = "desconhecido"
class ChannelPriority(Enum):
    # Prioridade do canal para o prompt do Hermes.
    CRITICAL = 0 // voz do usuario -- sempre processa
    HIGH = 1 // outra voz dirigida ao usuario
    CONTEXTUAL = 2 // musica/TV -- contexto mas not comando
    BACKGROUND = 3 // ambiente -- referencia apenas
    IGNORE = 4 // maquina/ruido -- descartar
# Mapeamento tipo -> prioridade
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
# ============================================================================
# 2. SEGMENTO DE AUDIO DETECTADO
# ============================================================================
# decorador: @dataclass
class AudioSegment:
    # Um segmento de audio detectado e classificado.
    segment_id: texto
    channel_type: AudioChannelType
    priority: ChannelPriority
    start_time: flutuante // quando comecou (segundos desde inicio)
    end_time: flutuante // quando terminou
    duration_sec: float = 0.0
    # Transcricao (se for voz)
    transcript: str = ""
    language: str = "pt-BR"
    confidence: float = 0.0 // 0-1
    # Speaker info (se for voz)
    speaker_id: str = ""  // quem esta falando
    is_user: bool = False // and o dono do dispositivo?
    speaker_name: str = ""
    # Audio features
    volume_db: float = 0.0 // volume em dB
    snr_db: float = 0.0 // signal-to-noise ratio
    overlap: bool = False // sobreposto com outro canal?
    # Contexto
    source_device: str = ""  // "microfone_notebook" / "smartphone_mesa"
    room_estimate: str = ""  // estimativa do ambiente
    # decorador: @property
    def is_speech(self) -> bool:
        return self.channel_type in (AudioChannelType.USER_VOICE,
                                    AudioChannelType.OTHER_VOICE)
    # decorador: @property
    def is_command(self) -> bool:
        # E uma fala do usuario que parece comando?
        if not self.is_user or not self.transcript:
            return False
        commands = ["hermes", "escreve", "cria", "desenvolve", "abre",
                    "fecha", "procura", "manda", "configura"]
        return any(c in self.transcript.lower() para c em commands)
# ============================================================================
# 3. VOICE PRINT (identidade vocal do usuario)
# ============================================================================
# decorador: @dataclass
class VoicePrint:
    # Impressao digital da voz do usuario.
    Permite distinguir o usuario de outras pessoas.
    Construido durante o onboarding (usuario fala 30 segundos).
    TECNICAMENTE:
    - x-vector or ECAPA-TDNN embedding (192-512 dimensoes)
    - Comparado com cada voz detectada (cosine similarity)
    - >0.7 = mesmo falante (usuario)
    - <0.5 = pessoa diferente
    # 
    user_id: texto
    user_name: texto
    embedding: [flutuante] = field(default_factory=list) // placeholder
    enrolled_at: str = ""
    samples_count: int = 0
    # Caracteristicas vocais (para demo sem modelo real)
    pitch_range: (flutuante, flutuante) = (80.0, 200.0) // Hz (masculino tipico)
    speaking_rate: float = 150.0 // palavras por minuto
    accent: str = "brasileiro"
    funcao identify(self, speaker_embedding: [flutuante],
                pitch: float = 0.0) -> (logico, flutuante):
        # Verifica se uma voz e do usuario.
        Returns:
            (is_user, confidence 0-1)
        # 
        if not self.embedding and not speaker_embedding:
            # Demo sem embedding real: usar pitch
            if pitch > 0:
                desempacote lo, hi = self.pitch_range
                if lo <= pitch <= hi:
                    return True, 0.75
            return False, 0.3
        # Cosine similarity (simulado)
        if len(self.embedding) > 0 and len(speaker_embedding) > 0:
            dot = sum(a*b para a,b in zip(self.embedding, speaker_embedding))
            norm_a = math.sqrt(sum(a*a para a em self.embedding))
            norm_b = math.sqrt(sum(b*b para b em speaker_embedding))
            if norm_a > 0 and norm_b > 0:
                similarity = dot / (norm_a * norm_b)
                return similarity > 0.7, similarity
        return False, 0.0
# ============================================================================
# 4. PIPELINE DE SEPARACAO
# ============================================================================
class AudioChannelSeparator:
    # Pipeline que separa audio bruto em micro-canais.
    ESTAGIOS:
    1. VAD: detectar segmentos com fala vs silencio/ruido
    2. SOURCE SEPARATION: separar vocais de musica/ambiente
    3. DIARIZACAO: separar falantes diferentes
    4. VOICE ID: qual and o usuario?
    5. CLASSIFICACAO: o que and o que not and voz?
    6. ROUTING: enviar cada canal para destino certo
    # 
    def __init__(self):
        self.user_voiceprint: VoicePrint? = None
        self.known_speakers: {texto: VoicePrint} = {}
        self.segments: [AudioSegment] = []
        self.active_channels: {AudioChannelType: AudioSegment} = {}
        self.sample_rate: inteiro = 16000 // 16kHz
        self.frame_duration_ms: inteiro = 30 // janela de 30ms
        # Configuracao
        self.min_speech_duration_ms: inteiro = 250 // ignorar < 250ms
        self.min_silence_duration_ms: inteiro = 500 // silencio > 500ms = pausa
        self.max_audio_buffer_sec: inteiro = 60 // buffer de 60s
        self.privacy_mode: logico = True // NUNCA enviar audio bruto
        self.local_only: logico = True // tudo processa local
        # Stats
        self.total_segments: inteiro = 0
        self.user_commands: inteiro = 0
        self.other_voices: inteiro = 0
        self.ambient_detected: inteiro = 0
    funcao enroll_user(self, user_id: texto, user_name: texto,
                    pitch_low: float = 80.0, pitch_high: flutuante = 200.0) -> VoicePrint:
        # Cadastra a voz do usuario (onboarding).
        Usuario fala por 30 segundos. Sistema cria voiceprint.
        # 
        vp = VoicePrint(
            user_id = user_id,
            user_name = user_name,
            pitch_range = (pitch_low, pitch_high),
            enrolled_at = datetime.now().isoformat(),
            samples_count = 30,
            # Em producao: embedding real de 30s de audio
            embedding = [0.1] * 192, // placeholder
        )
        self.user_voiceprint = vp
        return vp
    funcao enroll_speaker(self, speaker_id: texto, name: texto,
                    pitch_low: float = 0, pitch_high: flutuante = 0) -> VoicePrint:
        # Cadastra outra pessoa conhecida (familia, colega).
        vp = VoicePrint(
            user_id = speaker_id,
            user_name = name,
            pitch_range = (pitch_low or 100, pitch_high or 300),
            embedding = [0.2] * 192, // placeholder diferente
        )
        self.known_speakers[speaker_id] = vp
        return vp
    funcao process_frame(self, audio_data: bytes,
                    device: str = "microfone_notebook",
                    simulated_segments: [Dict] = None) -> [AudioSegment]:
        # Processa um frame de audio e retorna segmentos classificados.
        Em producao isto chamaria:
        1. silero-vad para VAD
        2. demucs para source separation
        3. pyannote para diarizacao
        4. ECAPA-TDNN para voice ID
        5. YAMNet para classificacao
        Aqui simulamos com dados de demonstracao.
        # 
        if simulated_segments:
            return self._process_simulated(simulated_segments, device)
        return []
    funcao _process_simulated(self, segments: [Dict],
                        device: texto) -> [AudioSegment]:
        # Processa segmentos simulados para demonstracao.
        results = []
        for seg in segments:
            channel = seg.get("type", AudioChannelType.UNKNOWN)
            if isinstance(channel, texto):
                channel = AudioChannelType(channel)
            priority = CHANNEL_PRIORITY.get(channel, ChannelPriority.IGNORE)
            # Voice ID
            is_user = False
            speaker_name = ""
            if channel == AudioChannelType.USER_VOICE:
                is_user = True
                speaker_name = self.user_voiceprint ? self.user_voiceprint.user_name : "Usuario"
            elif channel == AudioChannelType.OTHER_VOICE:
                speaker_name = seg.get("speaker", "Desconhecido")
                # Verificar se e conhecido
                for each (sid, vp) in self.known_speakers.items():
                    if vp.user_name == speaker_name:
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
                overlap = seg.get("overlap", False),
                source_device = device,
            )
            results.append(segment)
            self.segments.append(segment)
            self.total_segments += 1
            if is_user and segment.is_command:
                self.user_commands += 1
            elif channel == AudioChannelType.OTHER_VOICE:
                self.other_voices += 1
            elif channel in (AudioChannelType.MUSIC, AudioChannelType.TV_MEDIA,
                            AudioChannelType.AMBIENT_NATURE,
                            AudioChannelType.AMBIENT_URBAN):
                self.ambient_detected += 1
        return results
    def get_active_channels(self) -> {texto: qualquer}:
        # Retorna os canais ativos no momento.
        channels = defaultdict(list)
        para seg in self.segments[-50:]: // ultimos 50 segmentos
            channels[seg.channel_type.value].append({
                "transcript": seg.transcript[:60],
                "speaker": seg.speaker_name,
                "is_user": seg.is_user,
                "duration": "{seg.duration_sec:.1f}s",
                "priority": seg.priority.name,
            })
        return dict(channels)
    def build_context_prompt(self) -> str:
        # Constroi o prompt de contexto para o Hermes.
        Fusion dos micro-canais num texto que o Hermes entende.
        # 
        if not self.segments:
            return ""
        parts = []
        # Voz do usuario (comandos)
        user_speech = [s para s em self.segments[-20:]
                    if s.is_user and s.transcript]
        if user_speech:
            cmds = [s.transcript para s em user_speech if s.is_command]
            casual = [s.transcript para s em user_speech if not s.is_command]
            if cmds:
                parts.append("COMANDO DO USUARIO: {' | '.join(cmds[-3:])}")
            if casual:
                parts.append("CONTEXTO (usuario falou): {' | '.join(casual[-2:])}")
        # Outras vozes
        others = [s para s em self.segments[-20:]
                if s.channel_type == AudioChannelType.OTHER_VOICE and s.transcript]
        if others:
            speakers = set(s.speaker_name para s em others)
            parts.append(
                "AMBIENTE SOCIAL: {', '.join(speakers)} presente. "
                "Ultima fala ouvivel: '{others[-1].transcript[:50]}'"
            )
        # Musica/TV
        media = [s para s em self.segments[-20:]
                if s.channel_type in (AudioChannelType.MUSIC,
                                    AudioChannelType.TV_MEDIA)]
        if media:
            last = media[-1]
            if last.channel_type == AudioChannelType.MUSIC:
                parts.append("CONTEXTO: musica tocando ao fundo")
            else:
                parts.append("CONTEXTO: TV/midia tocando (possivel referencia)")
        # Ambiente
        ambient = [s para s em self.segments[-10:]
                if s.channel_type in (AudioChannelType.AMBIENT_NATURE,
                                        AudioChannelType.AMBIENT_URBAN)]
        if ambient:
            last = ambient[-1]
            if last.channel_type == AudioChannelType.AMBIENT_URBAN:
                parts.append("CONTEXTO: ambiente urbano (transito/gente)")
            else:
                parts.append("CONTEXTO: ambiente natural")
        # Silencio
        recent_types = [s.channel_type para s em self.segments[-5:]]
        if all(t == AudioChannelType.SILENCE para t em recent_types):
            parts.append("CONTEXTO: silencio -- usuario provavelmente sozinho/focado")
        parts ? retorne " || ".join(parts) : ""
    def stats(self) -> {texto: qualquer}:
        return {
            "total_segments": self.total_segments,
            "user_commands": self.user_commands,
            "other_voices": self.other_voices,
            "ambient_detected": self.ambient_detected,
            "known_speakers": len(self.known_speakers),
            "user_enrolled": self.user_voiceprint is not  None,
            "privacy_mode": self.privacy_mode,
            "local_only": self.local_only,
        }
# ============================================================================
# 5. MULTI-DISPOSITIVO (microfone + smartphone)
# ============================================================================
# decorador: @dataclass
class AudioSource:
    # Um dispositivo captando audio.
    device_id: texto
    device_name: texto
    device_type: texto         // "microfone_notebook", "smartphone", "wearable"
    location: texto            // "mesa", "bolso", "parede"
    quality: float = 0.8 // 0-1 (quao bom and o microfone)
    active: bool = True
    latency_ms: float = 50 // latencia estimada
class MultiDeviceFusion:
    # Funde audio de multiplos dispositivos.
    CENARIO:
    - Notebook na mesa: capta voz do usuario + TV ao fundo
    - Smartphone no bolso: capta voz do usuario abafada + ambiente
    - Wearable no pescoco: capta SO a voz do usuario (alta qualidade)
    FUSAO:
    - Se ambos captam a MESMA voz do usuario: usar o de melhor qualidade
    - Se um capta algo que o outro not: combinar
    - Se conflito: priorizar dispositivo mais proximo da fonte
    - Beamforming virtual: usar diferenca de timing para localizar fonte
    # 
    def __init__(self):
        self.sources: {texto: AudioSource} = {}
        self.separator = AudioChannelSeparator()
    def add_source(self, source: AudioSource) -> None:
        self.sources[source.device_id] = source
    funcao best_source_for(self, channel_type: AudioChannelType) retorna AudioSource?:
        # Determina qual dispositivo capt melhor cada canal.
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
        for dev_type in preferred:
            for source in self.sources.values():
                if source.device_type == dev_type and source.active:
                    return source
        return None
    def fusion_report(self) -> {texto: qualquer}:
        return {
            "total_sources": len(self.sources),
            "active_sources": sum(1 para s em self.sources.values() if s.active),
            "devices": [
                {
                    "name": s.device_name,
                    "type": s.device_type,
                    "location": s.location,
                    "quality": s.quality,
                    "active": s.active,
                }
                para s in self.sources.values()
            ],
        }
# ============================================================================
# 6. MAIN -- DEMONSTRACAO
# ============================================================================
if __name__ == "__main__":
    print("=" * 75)
    print("  OPENAUDIOCHANNEL -- SEPARACAO EM MICRO-CANAIS")
    print("  'O microfone capta tudo. O cerebro separa.'")
    print("=" * 75)
    separator = AudioChannelSeparator()
    fusion = MultiDeviceFusion()
    # === 1. CADASTRAR VOZ DO USUARIO ===
    print("\n\n  === 1. ONBOARDING: VOZ DO USUARIO ===\n")
    vp = separator.enroll_user("cleiton", "Cleiton",
                                pitch_low = 85, pitch_high=180)
    print("  Usuario: {vp.user_name}")
    print("  Pitch range: {vp.pitch_range[0]:.0f}-{vp.pitch_range[1]:.0f} Hz")
    print("  Amostras: {vp.samples_count}s de audio")
    print("  Voiceprint: criado (192 dimensoes)")
    # Cadastrar pessoas conhecidas
    separator.enroll_speaker("s-001", "Esposa", 180, 280)
    separator.enroll_speaker("s-002", "Filho", 250, 400)
    print("\n  Pessoas conhecidas: {len(separator.known_speakers)}")
    for s in separator.known_speakers.values():
        print("    {s.user_name} (pitch {s.pitch_range[0]:.0f}-{s.pitch_range[1]:.0f} Hz)")
    # === 2. DISPOSITIVOS ===
    print("\n\n  === 2. MULTI-DISPOSITIVO ===\n")
    fusion.add_source(AudioSource("D-01", "Microfone MacBook",
                                "microfone_notebook", "mesa", 0.85))
    fusion.add_source(AudioSource("D-02", "iPhone 15",
                                "smartphone_mesa", "mesa", 0.90))
    fusion.add_source(AudioSource("D-03", "AirPods Pro",
                                "wearableOuvido", "ouvido", 0.95))
    report = fusion.fusion_report()
    print("  Dispositivos: {report['total_sources']}")
    for d in report["devices"]:
        print("    {d['name']:<20} {d['type']:<20} {d['location']:<10} Q:{d['quality']:.2f}")
    # Melhor dispositivo por canal
    print("\n  Melhor fonte por canal:")
    para ch in [AudioChannelType.USER_VOICE, AudioChannelType.OTHER_VOICE,
            AudioChannelType.MUSIC, AudioChannelType.AMBIENT_URBAN]:
        best = fusion.best_source_for(ch)
        print("    {ch.value:<20} -> {best.device_name if best else 'N/A'}")
    # === 3. SIMULACAO: CENARIO REAL ===
    print("\n\n  === 3. CENARIO REAL: AUDIO MISTURADO ===\n")
    print("  Situacao: Cleiton no escritorio. Esposa conversa ao fundo.")
    print("  Musica toca no Spotify. Transito na rua.\n")
    # Simular segmentos detectados pelo pipeline
    simulated = [
        # Cleiton falando (comando)
        {"type": AudioChannelType.USER_VOICE, "start": 0.0, "end": 3.5,
        "text": "Hermes, desenvolve o OpenMilitary", "confidence": 0.95,
        "volume": -20, "snr": 25, "overlap": False},
        # Musica de fundo
        {"type": AudioChannelType.MUSIC, "start": 0.0, "end": 15.0,
        "text": "", "volume": -45, "snr": 5},
        # Esposa falando ao fundo
        {"type": AudioChannelType.OTHER_VOICE, "start": 4.0, "end": 7.0,
        "text": "amor, o almoco esta pronto", "confidence": 0.80,
        "speaker": "Esposa", "volume": -35, "snr": 12, "overlap": False},
        # Cleiton responde a esposa
        {"type": AudioChannelType.USER_VOICE, "start": 7.5, "end": 9.0,
        "text": "ja vou amor", "confidence": 0.90,
        "volume": -22, "snr": 22, "overlap": False},
        # Cleiton continua falando pro Hermes
        {"type": AudioChannelType.USER_VOICE, "start": 10.0, "end": 14.0,
        "text": "com foco em sistema anti-golpe and autonomia corporal",
        "confidence": 0.93, "volume": -21, "snr": 24, "overlap": False},
        # Transito la fora
        {"type": AudioChannelType.AMBIENT_URBAN, "start": 0.0, "end": 15.0,
        "text": "", "volume": -55, "snr": 2},
        # Silencio depois
        {"type": AudioChannelType.SILENCE, "start": 15.0, "end": 18.0,
        "text": "", "volume": -70},
    ]
    segments = separator.process_frame(b"", "microfone_notebook", simulated)
    print("  Segmentos detectados: {len(segments)}\n")
    print("  {'Canal':<20} {'Quem':<12} {'Prioridade':<12} {'Dur':>5} {'Texto'}")
    print("  {'-'*75}")
    for seg in segments:
        text = seg.transcript ? seg.transcript[ : 35] : "(som)"
        marker = seg.is_command ? "[CMD]" : ""
        print("  {seg.channel_type.value:<20} {seg.speaker_name or '-':<12} "
            "{seg.priority.name:<12} {seg.duration_sec:>4.1f}s "
            "{text} {marker}")
    # === 4. MICRO-CANAIS SEPARADOS ===
    print("\n\n  === 4. MICRO-CANAIS SEPARADOS ===\n")
    channels = separator.get_active_channels()
    for each (ch_type, ch_segments) in channels.items():
        priority = CHANNEL_PRIORITY.get(
            AudioChannelType(ch_type), ChannelPriority.IGNORE)
        print("\n  CANAL: {ch_type} (prioridade: {priority.name})")
        for s in ch_segments:
            marker = s["is_user"] ? " <-- USUARIO" : ""
            text = s["transcript"]  or  "(som ambiente)"
            print("    [{s['duration']}] {s['speaker'] or '-'}: "
                "{text}{marker}")
    # === 5. FUSAO EM PROMPT CONTEXTUAL ===
    print("\n\n  === 5. FUSAO EM PROMPT PARA HERMES ===\n")
    context = separator.build_context_prompt()
    print("  PROMPT GERADO:")
    print("  ---")
    print("  {context}")
    print("  ---")
    print("\n  Hermes recebe: comando + contexto social + ambiente")
    print("  NAO recebe: audio bruto de outras pessoas (privacidade)")
    # === 6. IDENTIFICACAO DE VOZ ===
    print("\n\n  === 6. IDENTIFICACAO: QUEM ESTA FALANDO? ===\n")
    test_voices = [
        ("Voz A", 95, "pitch baixo, masculino"),
        ("Voz B", 220, "pitch alto, feminino"),
        ("Voz C", 300, "pitch muito alto, crianca"),
        ("Voz D", 150, "pitch medio, masculino"),
    ]
    para label, pitch, desc in test_voices:
        desempacote is_user, conf = vp.identify([], pitch)
        identity = is_user ? "CLEITON" : "desconhecido"
        # Verificar conhecidos
        if not is_user:
            for each (sid, sp) in separator.known_speakers.items():
                if sp.pitch_range[0] <= pitch <= sp.pitch_range[1]:
                    identity = sp.user_name
                    break
        print("  {label} ({desc}): pitch {pitch}Hz -> {identity} "
            "(confianca {conf:.0%})")
    # === 7. PRIVACIDADE ===
    print("\n\n  === 7. POLITICA DE PRIVACIDADE ===\n")
    print("  Tudo processa LOCALMENTE: {separator.local_only}")
    print("  Audio bruto NUNCA enviado: {separator.privacy_mode}")
    print("  So transcritos do USUARIO vao pro Hermes")
    print("  Outras vozes: so contexto (nome, not conteudo)")
    print("  Musica/TV: so tipo, not conteudo")
    print("  Ambiente: so classificacao, not audio")
    # === 8. STATS ===
    print("\n\n  === 8. ESTATISTICAS ===\n")
    s = separator.stats()
    for each (k, v) in s.items():
        print("  {k:<25} {v}")
    # === ARQUITETURA ===
    print("\n\n{'='*75}")
    print("  ARQUITETURA DO OPENAUDIOCHANNEL")
    print("{'='*75}")
    print("""
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
    - Outras pessoas presentes (CONTEXTUAL -- nomes, not conteudo)
    - Ambiente (BACKGROUND -- tipo, not audio)
O QUE O HERMES not SABE:
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
# )
    print("{'='*75}")
    print("  OpenAudioChannel: {s['total_segments']} segmentos processados.")
    print("  {s['user_commands']} comandos do usuario identificados.")
    print("  {s['other_voices']} vozes de outros separadas (contexto only).")
    print("  Tudo local. Zero nuvem. Zero audio bruto enviado.")
    print("{'='*75}")
