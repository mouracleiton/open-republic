#!/usr/bin/env python3
"""
OpenTelefonista -- O Sistema Como Conversa Humana
===================================================
"Voce nao abre um app. Voce nao clica um botao.
Voce FALA. E uma voz responde. Como telefonista humana.
'E a Republica.' 'Cleiton, voce tem 3 tarefas. Quer ouvir?'
'O codigo que voce ditou tem um erro na linha 5. Quer que eu corrija?'

A telefonista NAO e um chatbot. E uma PESSOA DIGITAL que:
1. CONVERSA naturalmente (nao comandos, dialogo)
2. CAPTA o mundo pelos sensores do smartphone/hardware
3. TRADUZ o mundo para o usuario (daltonico ve cor, cego ouve rua)
4. PROTEGE o usuario (geolocalizacao de criancas, deteccao de perigo)
5. AMPLIFICA o usuario (programa por voz, aprende por audio)
6. RESPEITA o silencio (OpenSilencePolicy -- so fala quando chamada)

O smartphone vira o CORPO EXTENDIDO do usuario:
- Camera = olhos (daltonico ve cores corretas, cego ve obstaculos)
- Microfone = ouvidos (surdo ve legendas, capta ambiente)
- GPS = sentido de direcao (cego navega, criancas localizadas)
- Acelerometro = equilibrio (detecta queda, tremor)
- Vibracall = tato (surdos sentem o mundo)
- Ligacao celular = telefone de verdade (telefonista LIGA para quem precisa)

DIFERENCA CRITICAL: A telefonista e HUMANIZADA, nao robotica.
Ela tem nome, personalidade, memoria, humor.
Ela PERGUNTA antes de agir. Ela ESPERA resposta.
Ela NUNCA interrompe (OpenSilencePolicy).
Ela se ADAPTA ao humor e energia do usuario.

Integrado com:
- OpenInclusiveIDE (programa por voz conversando)
- OpenInclusiveHardware (todos os 44 dispositivos)
- OpenAudioChannel (separa voz de ruido)
- OpenSilencePolicy (so fala quando chamada)
- OpenAbsence (respeita pausas)
- OpenBodilyAutonomy (usuario controla tudo)
- OpenFocus (nao distrai)

Modelos STT/TTS 2024/2025 (camada de voz atualizada):
- STT (Speech-to-Text): Whisper large-v3-turbo (OpenAI, Nov 2024),
  distil-large-v3, NVIDIA NeMo Canary-1B / Parakeet TDT 0.6b-v2
  (SOTA open-source ASR 2024), Moonshine (edge/mobile, 2024),
  WhisperX (diarizacao + VAD), faster-whisper (backend CTranslate2).
- TTS (Text-to-Speech): Kokoro-82M (Apache-2.0, leve, alta qualidade),
  F5-TTS (flow-matching, clonagem zero-shot), Coqui XTTS v2 (multilingue),
  Piper (edge/onnx), MeloTTS (MIT), StyleTTS 2, OpenVoice v2.
  Cloud de baixa latencia: OpenAI gpt-4o-mini-tts (2025),
  ElevenLabs Multilingual v2 / Turbo v2 / Flash v2.5,
  Google Gemini Live TTS (Gemini 2.0), PlayHT 3.0.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set, Callable
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict, deque
import hashlib
import time


# ============================================================================
# 1. PERSONALIDADE DA TELEFONISTA
# ============================================================================

# ============================================================================
# 1b. CAMADA DE VOZ -- Modelos STT/TTS 2024/2025
# ============================================================================

class STTModel(Enum):
    """Modelos de Speech-to-Text (STT / ASR) atualizados para 2024/2025.

    Curadoria SOTA open-source + edge + cloud (Nov 2024 / 2025).
    Selecao por latencia x acuracia x privacidade (on-device x cloud).
    """
    # --- OpenAI Whisper family (família 2024) ---
    WHISPER_LARGE_V3 = "whisper-large-v3"              # referencia, ~3GB
    WHISPER_LARGE_V3_TURBO = "whisper-large-v3-turbo"  # OpenAI Nov 2024, 8x mais rapido
    WHISPER_DISTIL_LARGE_V3 = "distil-large-v3"        # ~756MB, queda minima de acuracia
    FASTER_WHISPER_LARGE_V3 = "faster-whisper-large-v3"  # backend CTranslate2, 4x mais rapido
    WHISPERX = "whisperx"                               # + VAD + diarizacao (falantes)
    # --- NVIDIA NeMo (SOTA open-source ASR 2024) ---
    NEMO_CANARY_1B = "nvidia/canary-1b"                 # multilingue + traducao, 1B params
    NEMO_PARAKEET_TDT_06B_V2 = "nvidia/parakeet-tdt-0.6b-v2"  # SOTA EN, TDT decoder, 2024
    # --- Edge / mobile ---
    MOONSHINE_BASE = "moonshine-base"   # Useful Sensors, 27M, on-device 2024
    MOONSHINE_TINY = "moonshine-tiny"   # 27M menor latencia
    PIPER_STT = "piper-stt"             # ONNX, CPU raspi (placeholder STT)
    # --- Cloud de baixa latencia ---
    OPENAI_GPT4O_TRANSCRIBE = "gpt-4o-transcribe"       # OpenAI 2024/2025
    OPENAI_GPT4O_MINI_TRANSCRIBE = "gpt-4o-mini-transcribe"
    GOOGLE_GEMINI_LIVE_STT = "gemini-2.0-live-stt"      # streaming bidirecional
    ASSEMBLYAI_UNIVERSAL_2 = "assemblyai-universal-2"   # SOTA cloud 2024
    DEEPGRAM_NOVA_3 = "deepgram-nova-3"                 #低 latencia cloud


class TTSModel(Enum):
    """Modelos de Text-to-Speech (TTS) atualizados para 2024/2025.

    Prioridade em vozes naturais em PT-BR, latencia baixa e licencas
    permissivas (Apache/MIT) para soberania do usuario.
    """
    # --- Open-source / on-device ---
    KOKORO_82M = "kokoro-82m"          # Apache-2.0, 82M, alta qualidade 2024-2025
    F5_TTS = "f5-tts"                  # flow-matching, clonagem zero-shot
    XTTS_V2 = "xtts-v2"                # Coqui, multilingue (incl. PT-BR), clonagem
    PIPER = "piper"                    # ONNX, edge/CPU, vozes PT-BR comunitarias
    MELOTTS = "melotts"               # MIT, multilingue, CPU-friendly
    STYLE_TTS_2 = "styletts-2"         # alta expressividade
    OPENVOICE_V2 = "openvoice-v2"      # clonagem rapida multi-falante
    # --- Cloud de baixa latencia / comercial ---
    OPENAI_GPT4O_MINI_TTS = "gpt-4o-mini-tts"   # OpenAI 2025, 11 vozes
    ELEVENLABS_MULTILINGUAL_V2 = "eleven-multilingual-v2"
    ELEVENLABS_TURBO_V2 = "eleven-turbo-v2"
    ELEVENLABS_FLASH_V2_5 = "eleven-flash-v2-5"  # baixissima latencia 2024
    GOOGLE_GEMINI_LIVE_TTS = "gemini-2.0-live-tts"
    PLAYHT_3 = "playht-3"


@dataclass
class STTConfig:
    """Configuracao do motor STT (transcricao de voz -> texto)."""
    model: STTModel = STTModel.WHISPER_LARGE_V3_TURBO  # padrao 2024/2025
    language: str = "pt"                # codigo ISO 639-1
    enable_diarization: bool = True     # separar falantes (WhisperX/NeMo)
    enable_vad: bool = True             # Voice Activity Detection
    enable_punctuation: bool = True     # pontuacao automatica
    enable_casing: bool = True          # capitalizacao automatica
    beam_size: int = 5                  # equilibrio velocidade x acuracia
    sample_rate: int = 16000            # 16 kHz ( Whisper / NeMo )
    device: str = "auto"                # auto / cpu / cuda / metal
    compute_type: str = "int8"          # int8 (rapido) / float16 / float32
    cloud_api_key: Optional[str] = None  # só para modelos cloud
    streaming: bool = False             # transcricao em streaming


@dataclass
class TTSConfig:
    """Configuracao do motor TTS (texto -> voz)."""
    model: TTSModel = TTSModel.KOKORO_82M  # padrao 2024/2025 (Apache-2.0)
    voice_id: str = "pf_dora"             # voz Kokoro PT-BR "Dora" (2024)
    language: str = "pt-br"
    speed: float = 1.0                    # 0.5 (lento) ate 2.0 (rapido)
    sample_rate: int = 24000              # 24 kHz Kokoro / XTTS
    enable_cloning: bool = False          # clonar voz do usuario
    clone_reference_audio: Optional[str] = None  # path wav de referencia
    streaming: bool = True                # streaming de audio (baixa latencia)
    device: str = "auto"                  # auto / cpu / cuda / metal
    cloud_api_key: Optional[str] = None   # só para modelos cloud
    output_format: str = "wav"            # wav / mp3 / pcm_raw


class VoiceEngine:
    """
    Orquestra STT + TTS usando modelos SOTA 2024/2025.

    IMPORTANTE: a carga pesada (torch, faster-whisper, TTS) e feita LAZY,
    dentro dos metodos, para que este modulo continue importavel sem
    dependencias pesadas instaladas. Assim `python3 -m py_compile` e a
    importacao pura (sem deps) seguem funcionando.

    Cada backend tenta importar sua biblioteca; se ausente, cai para um
    mock que devolve/mostra o texto -- util para desenvolvimento e testes.
    """

    # Mapas modelo -> backend (para documentacao e fallback)
    WHISPER_BACKENDS = {
        STTModel.WHISPER_LARGE_V3, STTModel.WHISPER_LARGE_V3_TURBO,
        STTModel.WHISPER_DISTIL_LARGE_V3, STTModel.FASTER_WHISPER_LARGE_V3,
    }

    def __init__(self, stt_config: Optional[STTConfig] = None,
                 tts_config: Optional[TTSConfig] = None):
        self.stt_config = stt_config or STTConfig()
        self.tts_config = tts_config or TTSConfig()
        self._stt_backend: Optional[Any] = None
        self._tts_backend: Optional[Any] = None

    # ---------------------- STT ----------------------

    def transcribe(self, audio_path: str) -> Dict[str, Any]:
        """Transcreve um arquivo de audio para texto.

        Retorna dict com: text, language, segments (opcional), speakers.
        """
        try:
            if self.stt_config.model in self.WHISPER_BACKENDS:
                return self._transcribe_whisper(audio_path)
            if self.stt_config.model.value.startswith("nvidia/"):
                return self._transcribe_nemo(audio_path)
            if self.stt_config.model.value.startswith("moonshine"):
                return self._transcribe_moonshine(audio_path)
            if self.stt_config.model.value.startswith(("gpt-4o", "gemini",
                                                       "assemblyai", "deepgram")):
                return self._transcribe_cloud(audio_path)
        except ImportError:
            pass
        # Fallback mock (sem dependencias)
        return self._transcribe_mock(audio_path)

    def _transcribe_whisper(self, audio_path: str) -> Dict[str, Any]:
        # faster-whisper (CTranslate2) ou openai-whisper
        try:
            from faster_whisper import WhisperModel  # type: ignore
            backend = self._get_stt_backend_whisper()
            segments, info = backend.transcribe(
                audio_path,
                language=self.stt_config.language,
                beam_size=self.stt_config.beam_size,
                vad_filter=self.stt_config.enable_vad,
            )
            text = " ".join(s.text for s in segments)
            return {"text": text.strip(), "language": info.language,
                    "backend": "faster-whisper",
                    "model": self.stt_config.model.value}
        except ImportError:
            import whisper  # type: ignore
            backend = self._get_stt_backend_whisper(openai=True)
            result = backend.transcribe(
                audio_path,
                language=self.stt_config.language,
                beam_size=self.stt_config.beam_size,
            )
            return {"text": result["text"].strip(),
                    "language": result.get("language", self.stt_config.language),
                    "backend": "openai-whisper",
                    "model": self.stt_config.model.value}

    def _transcribe_nemo(self, audio_path: str) -> Dict[str, Any]:
        import nemo.collections.asr as nemo_asr  # type: ignore
        if self._stt_backend is None:
            self._stt_backend = nemo_asr.models.ASRModel.from_pretrained(
                self.stt_config.model.value
            )
        text = " ".join(self._stt_backend.transcribe([audio_path]))
        return {"text": text.strip(), "language": self.stt_config.language,
                "backend": "nemo", "model": self.stt_config.model.value}

    def _transcribe_moonshine(self, audio_path: str) -> Dict[str, Any]:
        from moonshine import Moonshine  # type: ignore
        if self._stt_backend is None:
            self._stt_backend = Moonshine.load_model(
                "tiny" if "tiny" in self.stt_config.model.value else "base"
            )
        text = self._stt_backend.transcribe(audio_path)
        return {"text": text.strip(), "language": "en",
                "backend": "moonshine",
                "model": self.stt_config.model.value}

    def _transcribe_cloud(self, audio_path: str) -> Dict[str, Any]:
        # Placeholder para APIs cloud (OpenAI / Gemini / Deepgram / AssemblyAI)
        # Em producao: HTTP multipart para o endpoint do provedor.
        return {"text": f"[cloud:{self.stt_config.model.value}] transcription placeholder",
                "language": self.stt_config.language,
                "backend": "cloud", "model": self.stt_config.model.value}

    def _transcribe_mock(self, audio_path: str) -> Dict[str, Any]:
        return {"text": f"[mock] audio em {audio_path} transcrito",
                "language": self.stt_config.language,
                "backend": "mock", "model": self.stt_config.model.value}

    def _get_stt_backend_whisper(self, openai: bool = False) -> Any:
        if self._stt_backend is None:
            if openai:
                import whisper  # type: ignore
                self._stt_backend = whisper.load_model(
                    self.stt_config.model.value.replace("faster-whisper-", "")
                )
            else:
                from faster_whisper import WhisperModel  # type: ignore
                self._stt_backend = WhisperModel(
                    self.stt_config.model.value.replace("faster-whisper-", ""),
                    device=self.stt_config.device,
                    compute_type=self.stt_config.compute_type,
                )
        return self._stt_backend

    # ---------------------- TTS ----------------------

    def synthesize(self, text: str, out_path: Optional[str] = None) -> str:
        """Sintetiza fala a partir de texto. Retorna caminho do arquivo wav."""
        if out_path is None:
            out_path = f"/tmp/open_telefonista_tts_{int(time.time()*1000)}.wav"
        try:
            m = self.tts_config.model
            if m == TTSModel.KOKORO_82M:
                return self._synthesize_kokoro(text, out_path)
            if m == TTSModel.PIPER:
                return self._synthesize_piper(text, out_path)
            if m == TTSModel.XTTS_V2:
                return self._synthesize_xtts(text, out_path)
            if m == TTSModel.MELOTTS:
                return self._synthesize_melotts(text, out_path)
            if m.value.startswith(("gpt-4o", "eleven", "gemini", "playht")):
                return self._synthesize_cloud(text, out_path)
            # F5-TTS, StyleTTS-2, OpenVoice-v2 -> backend generico Coqui/TTStqdm
            return self._synthesize_coqui_generic(text, out_path)
        except ImportError:
            return self._synthesize_mock(text, out_path)

    def _synthesize_kokoro(self, text: str, out_path: str) -> str:
        # Kokoro-82M: pipelinephonemizer -> KokoroGAN (Apache-2.0)
        from kokoro import KokoroTTS  # type: ignore
        if self._tts_backend is None:
            self._tts_backend = KokoroTTS(device=self.tts_config.device)
        self._tts_backend.synthesize(
            text, voice=self.tts_config.voice_id, out_path=out_path,
            speed=self.tts_config.speed,
        )
        return out_path

    def _synthesize_piper(self, text: str, out_path: str) -> str:
        import piper  # type: ignore
        if self._tts_backend is None:
            self._tts_backend = piper.PiperVoice.load(self.tts_config.voice_id)
        import wave
        with wave.open(out_path, "wb") as wav_file:
            self._tts_backend.synthesize(text, wav_file,
                                         length_scale=1.0 / self.tts_config.speed)
        return out_path

    def _synthesize_xtts(self, text: str, out_path: str) -> str:
        from TTS.api import TTS as CoquiTTS  # type: ignore
        if self._tts_backend is None:
            self._tts_backend = CoquiTTS("tts_models/multilingual/multi-dataset/xtts_v2")
        speaker = self.tts_config.clone_reference_audio or self.tts_config.voice_id
        self._tts_backend.tts_to_file(text=text, language=self.tts_config.language,
                                       speaker_wav=speaker, file_path=out_path)
        return out_path

    def _synthesize_melotts(self, text: str, out_path: str) -> str:
        from melotts import MeloTTS  # type: ignore
        if self._tts_backend is None:
            self._tts_backend = MeloTTS(language=self.tts_config.language)
        self._tts_backend.synthesize(text, out_path, speed=self.tts_config.speed)
        return out_path

    def _synthesize_coqui_generic(self, text: str, out_path: str) -> str:
        from TTS.api import TTS as CoquiTTS  # type: ignore
        if self._tts_backend is None:
            self._tts_backend = CoquiTTS(self.tts_config.model.value)
        self._tts_backend.tts_to_file(text=text, file_path=out_path)
        return out_path

    def _synthesize_cloud(self, text: str, out_path: str) -> str:
        # Placeholder: em producao chama OpenAI / ElevenLabs / Gemini / PlayHT.
        return self._synthesize_mock(text, out_path)

    def _synthesize_mock(self, text: str, out_path: str) -> str:
        # Fallback sem deps: grava um wav silencioso valido para o pipeline.
        import wave
        import struct
        sr = self.tts_config.sample_rate
        dur = max(0.5, len(text) * 0.07 / max(self.tts_config.speed, 0.1))
        with wave.open(out_path, "w") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(sr)
            w.writeframes(struct.pack("<" + "h" * int(sr * dur),
                                      *([0] * int(sr * dur))))
        return out_path

    # ---------------------- helpers ----------------------

    def describe(self) -> Dict[str, str]:
        return {
            "stt_model": self.stt_config.model.value,
            "stt_language": self.stt_config.language,
            "tts_model": self.tts_config.model.value,
            "tts_voice": self.tts_config.voice_id,
        }


# ============================================================================
# 2. PERSONALIDADE DA TELEFONISTA
# ============================================================================

class TelefonistaPersonality(Enum):
    """Personalidades disponiveis da telefonista."""
    GENTLE = "gentil"          # calma, pausada, maternamente
    CHEERFUL = "alegre"        # energica, motivadora
    SERIOUS = "seria"          # direta, profissional
    FRIENDLY = "amiga"         # casual, como uma amiga
    FORMAL = "formal"          # educada, cerimoniosa
    PLAYFUL = "brincalhona"    # humor, leveza
    PROTECTIVE = "protetora"  # foca em seguranca
    MINIMAL = "minimal"        # so o necessario, poucas palavras


class EmotionalState(Enum):
    """Estado emocional detectado ou reportado pelo usuario."""
    HAPPY = "feliz"
    CALM = "calmo"
    FOCUSED = "focado"
    TIRED = "cansado"
    STRESSED = "estressado"
    ANXIOUS = "ansioso"
    SAD = "triste"
    ANGRY = "irritado"
    OVERWHELMED = "sobrecarregado"
    NEUTRAL = "neutro"


class ConversationMode(Enum):
    """Modo de conversa."""
    DIALOGUE = "dialogo"           # conversa bidirecional natural
    DICTATION = "ditado"           # usuario dita, sistema executa
    NARRATION = "narracao"         # sistema narrativa o que acontece
    EMERGENCY = "emergencia"       # prioridade maxima, voz firme
    WHISPER = "sussurro"           # resposta discreta (surdo = haptico)
    SILENT = "silencioso"          # so visual/haptico, sem voz
    CO_DRIVER = "copiloto"         # guia o usuario no mundo fisico
    TEACHER = "professora"         # ensina enquanto faz


@dataclass
class TelefonistaConfig:
    """Configuracao da personalidade da telefonista."""
    name: str = "Iara"             # nome da telefonista
    personality: TelefonistaPersonality = TelefonistaPersonality.GENTLE
    voice_id: str = "pf_dora"  # voz TTS (Kokoro PT-BR "Dora", 2024-2025)
    stt_config: Optional[STTConfig] = None  # motor STT 2024/2025 (lazy)
    tts_config: Optional[TTSConfig] = None  # motor TTS 2024/2025 (lazy)
    speech_rate: float = 1.0       # velocidade da fala
    formality: float = 0.3         # 0=informal, 1=formal
    verbosity: float = 0.5         # 0=curto, 1=detalhado
    humor_enabled: bool = True     # usa humor quando apropriado
    proactive: float = 0.3         # 0=so responde, 1=antecipa
    language: str = "pt-BR"
    respects_silence: bool = True  # OpenSilencePolicy
    interruptible: bool = True     # usuario pode interromper
    emotional_adaptation: bool = True  # adapta ao humor do usuario

    def adapt_to_emotion(self, emotion: EmotionalState) -> None:
        """Adapta comportamento ao estado emocional."""
        if emotion in (EmotionalState.STRESSED, EmotionalState.ANXIOUS):
            self.speech_rate = 0.85      # fala mais devagar
            self.verbosity = 0.3         # menos palavras
            self.humor_enabled = False   # sem humor
            self.personality = TelefonistaPersonality.GENTLE
        elif emotion == EmotionalState.TIRED:
            self.speech_rate = 0.9
            self.verbosity = 0.3
            self.proactive = 0.1         # nao antecipa
        elif emotion == EmotionalState.HAPPY:
            self.humor_enabled = True
            self.speech_rate = 1.1
        elif emotion == EmotionalState.OVERWHELMED:
            self.verbosity = 0.1         # minimo de palavras
            self.speech_rate = 0.8
            self.proactive = 0.0
        elif emotion == EmotionalState.FOCUSED:
            self.verbosity = 0.2         # direta, sem enrolacao
            self.humor_enabled = False
            self.proactive = 0.1


# ============================================================================
# 2. CAPACIDADES DO SMARTPHONE COMO CORPO EXTENDIDO
# ============================================================================

class SensorType(Enum):
    """Sensores do smartphone/hardware que captam o mundo."""
    CAMERA_REAR = "camera_traseira"        # camera principal
    CAMERA_FRONT = "camera_frontal"        # camera selfie
    MICROPHONE = "microfone"               # captura audio
    GPS = "gps"                            # localizacao
    ACCELEROMETER = "acelerometro"         # movimento/queda
    GYROSCOPE = "giroscopio"              # rotacao/orientacao
    COMPASS = "bussola"                   # direcao
    BAROMETER = "barometro"               # altitude/pressao
    THERMOMETER = "termometro"            # temperatura
    HUMIDITY = "umidade"                  # umidade do ar
    LIGHT = "luminosidade"               # sensor de luz
    PROXIMITY = "proximidade"            # distancia de objetos
    LIDAR = "lidar"                       # profundidade (iPhone Pro)
    TOF = "tempo_de_voo"                  # depth sensing
    HEART_RATE = "frequencia_cardiaca"    # smartwatch
    SPO2 = "oxigenio"                     # smartwatch
    SKIN_TEMP = "temperatura_pele"        # smartwatch
    NFC = "nfc"                           # proximidade de tags
    BLUETOOTH_BEACON = "beacon_bluetooth" # triangulacao indoor
    CELL_SIGNAL = "sinal_celular"        # triangulacao GSM


class WorldPerception(Enum):
    """O que o sistema percebe do mundo atraves dos sensores."""
    # VISAO
    COLOR_DETECTION = "deteccao_cor"           # daltonico ve a cor real
    TEXT_RECOGNITION = "reconhecimento_texto"  # OCR -- le textos do mundo
    OBJECT_DETECTION = "deteccao_objetos"      # identifica objetos
    FACE_RECOGNITION = "reconhecimento_facial" # reconhece pessoas
    OBSTACLE_DETECTION = "deteccao_obstaculos"  # cego: obstaculo na frente
    CROSSWALK_DETECTION = "deteccao_faixa"     # faixa de pedestre
    TRAFFIC_LIGHT = "semaforo"                 # cor do semaforo
    SIGN_RECOGNITION = "reconhecimento_placas"  # placas de transito
    DOCUMENT_SCAN = "escaneamento_documento"    # digitaliza papel
    MONEY_RECOGNITION = "reconhecimento_cedula"  # cego: qual nota e?
    PRODUCT_LABEL = "rotulo_produto"            # le rotulo no mercado
    # AUDICAO
    SOUND_CLASSIFICATION = "classificacao_som"  # o que e esse som?
    SPEAKER_RECOGNITION = "reconhecimento_voz"  # quem esta falando?
    MUSIC_RECOGNITION = "reconhecimento_musica"  # que musica e?
    SPEECH_TO_TEXT = "fala_para_texto"          # transcreve conversa
    AMBIENT_NOISE = "ruido_ambiente"            # nivel de ruido
    DOORBELL = "campainha"                      # alguem na porta
    ALARM_SOUND = "alarme"                      # alarme de emergencia
    SIREN = "sirene"                            # policia/bombeiro/ambulancia
    BABY_CRYING = "bebe_chorando"               # bebe chorando
    DOG_BARKING = "cachorro_latindo"            # cao latindo
    # LOCALIZACAO
    GPS_LOCATION = "localizacao_gps"             # onde estou
    INDOOR_LOCATION = "localizacao_indoor"       # dentro de predio
    DIRECTION_FACING = "direcao"                 # para onde olho
    ALTITUDE = "altitude"                        # altura/aterrissagem
    SPEED = "velocidade"                         # andando/correndo/parado
    NEARBY_PLACES = "lugares_proximos"           # hospitais, farmacias
    GEOCODING = "geocoding"                      # endereco <-> coordenada
    LOST_CHILD = "crianca_perdida"               # geolocalizacao de criancas
    # BIOMETRIA
    FALL_DETECTION = "deteccao_queda"            # caiu!
    HEART_ANOMALY = "anomalia_cardiaca"          # coracao irregular
    STRESS_DETECTION = "deteccao_stress"         # estressado pelo batimento
    SEIZURE_PREDICTION = "previsao_crise"        # epilepsia
    TREMOR_DETECTION = "deteccao_tremor"         # Parkinson
    POSTURE = "postura"                          # postura corporal
    # AMBIENTE
    TEMPERATURE = "temperatura_ambiente"         # calor/frio
    AIR_QUALITY = "qualidade_ar"                 # poluicao
    UV_INDEX = "indice_uv"                       # sol forte
    WEATHER = "clima"                            # chuva, sol, vento


@dataclass
class SensorReading:
    """Uma leitura de sensor do mundo fisico."""
    sensor: SensorType
    perception: WorldPerception
    value: Any                    # valor capturado
    confidence: float = 1.0       # 0-1
    timestamp: float = field(default_factory=time.time)
    description: str = ""         # descricao humanizada


# ============================================================================
# 3. VISAO COMPUTACIONAL -- Camera como Olhos
# ============================================================================

class ComputerVisionEngine:
    """
    Usa a camera do smartphone/oculos para traduzir o mundo visual
    para o usuario. Cada deficiencia tem uma traducao diferente.
    """

    def __init__(self):
        self.active_perceptions: List[WorldPerception] = []
        self.last_readings: deque = deque(maxlen=100)

    def process_frame(self, sensor: SensorType, frame_data: Any = None) -> List[SensorReading]:
        """Processa um frame da camera e gera leituras."""
        readings = []

        # DALTONICO: detecta e nomeia cores
        reading = SensorReading(
            sensor=sensor,
            perception=WorldPerception.COLOR_DETECTION,
            value={"color_name": "vermelho", "hex": "#FF0000", "rgb": (255, 0, 0)},
            confidence=0.95,
            description="Aqui e VERMELHO. A luz do semaforo esta VERMELHA. Pare."
        )
        readings.append(reading)

        # CEGO: detecta obstaculos
        reading = SensorReading(
            sensor=sensor,
            perception=WorldPerception.OBSTACLE_DETECTION,
            value={"obstacle": "poste", "distance_m": 2.5, "direction": "frente-esquerda"},
            confidence=0.88,
            description="Poste a 2.5 metros a frente e a esquerda. Desvie para a direita."
        )
        readings.append(reading)

        # OCR: le texto do mundo
        reading = SensorReading(
            sensor=sensor,
            perception=WorldPerception.TEXT_RECOGNITION,
            value={"text": "RESTAURANTE JOAO", "location": "acima da porta"},
            confidence=0.92,
            description="Placa diz: RESTAURANTE JOAO. Fica acima da porta a frente."
        )
        readings.append(reading)

        # SEMAFORO
        reading = SensorReading(
            sensor=sensor,
            perception=WorldPerception.TRAFFIC_LIGHT,
            value={"color": "verde", "action": "siga"},
            confidence=0.97,
            description="Semaforo VERDE. Pode atravessar."
        )
        readings.append(reading)

        # CEDULA -- cego reconhece dinheiro
        reading = SensorReading(
            sensor=sensor,
            perception=WorldPerception.MONEY_RECOGNITION,
            value={"denomination": "R$ 50,00", "color_pattern": "marrom"},
            confidence=0.94,
            description="Isso e uma nota de CINQUENTA REAIS."
        )
        readings.append(reading)

        for r in readings:
            self.last_readings.append(r)
        return readings

    def narrate_scene(self, readings: List[SensorReading], user_disability: str = "") -> str:
        """Transforma leituras visuais em narrativa falada."""
        if not readings:
            return "Nao consigo ver nada claramente agora."

        parts = []
        for r in readings:
            if r.confidence > 0.7:
                parts.append(r.description)

        if not parts:
            return "Ambiente visual incerto. Vou continuar observando."

        return ". ".join(parts) + "."


# ============================================================================
# 4. AUDIO -- Microfone como Ouvidos
# ============================================================================

class AudioPerceptionEngine:
    """
    Usa o microfone do smartphone/smartwatch para traduzir o mundo sonoro.
    Integrado com OpenAudioChannel para separacao de fontes.
    """

    def __init__(self):
        self.last_readings: deque = deque(maxlen=100)
        self.sound_buffer: deque = deque(maxlen=30)  # 30s de historico

    def process_audio(self) -> List[SensorReading]:
        """Processa audio ambiente e gera leituras."""
        readings = []

        # SURDO: transcreve fala
        reading = SensorReading(
            sensor=SensorType.MICROPHONE,
            perception=WorldPerception.SPEECH_TO_TEXT,
            value={"speaker": "homem", "text": "Bom dia, como vai?"},
            confidence=0.90,
            description="Um homem disse: Bom dia, como vai?"
        )
        readings.append(reading)

        # Classificacao de som ambiente
        reading = SensorReading(
            sensor=SensorType.MICROPHONE,
            perception=WorldPerception.SOUND_CLASSIFICATION,
            value={"sound": "sirene", "direction": "direita", "approaching": True},
            confidence=0.85,
            description="Sirene de ambulancia se aproximando pela direita."
        )
        readings.append(reading)

        # Campainha
        reading = SensorReading(
            sensor=SensorType.MICROPHONE,
            perception=WorldPerception.DOORBELL,
            value={"detected": True, "count": 2},
            confidence=0.95,
            description="Alguem tocou a campainha. Duas vezes."
        )
        readings.append(reading)

        # Bebe chorando
        reading = SensorReading(
            sensor=SensorType.MICROPHONE,
            perception=WorldPerception.BABY_CRYING,
            value={"detected": True, "intensity": "alta"},
            confidence=0.93,
            description="O bebe esta chorando. Intensidade alta."
        )
        readings.append(reading)

        for r in readings:
            self.last_readings.append(r)
        return readings

    def narrate_sounds(self, readings: List[SensorReading]) -> str:
        """Transforma leituras de audio em narrativa para surdos."""
        if not readings:
            return "Silencio."
        parts = [r.description for r in readings if r.confidence > 0.7]
        return ". ".join(parts) + "." if parts else "Nao identifico sons especificos."


# ============================================================================
# 5. GEOLOCALIZACAO -- GPS como Sentido de Direcao
# ============================================================================

class GeoLocationEngine:
    """
    Usa GPS + bussola + acelerometro para navegar e proteger.
    Inclui geolocalizacao de criancas e pessoas vulneraveis.
    """

    def __init__(self):
        self.last_known_location: Tuple[float, float] = (-23.55, -46.63)  # Sao Paulo
        self.tracked_persons: Dict[str, Dict] = {}  # criancas, idosos, etc
        self.safe_zones: List[Dict] = []
        self.last_readings: deque = deque(maxlen=100)

    def update_location(self, lat: float, lon: float) -> SensorReading:
        """Atualiza localizacao GPS."""
        self.last_known_location = (lat, lon)
        reading = SensorReading(
            sensor=SensorType.GPS,
            perception=WorldPerception.GPS_LOCATION,
            value={"lat": lat, "lon": lon},
            confidence=0.98,
            description=f"Voce esta proximo a {lat:.4f}, {lon:.4f}."
        )
        self.last_readings.append(reading)
        return reading

    def navigate_for_blind(self, destination: str) -> str:
        """Navegacao por voz para cego -- passo a passo."""
        steps = [
            "Voce esta na rua Augusta, numero 1000.",
            "Vire a direita. Ainda 200 metros.",
            "Cuidado, buraco a frente a 3 metros.",
            "Semaforo vermelho. Espere.",
            "Semaforo verde. Atravesse. Cinco passos.",
            "Chegou. O destino esta a sua frente.",
        ]
        # Em producao: OSRM + OpenStreetMap + obstructions
        return steps[0]

    def track_child(self, child_id: str, child_name: str,
                    child_phone: str, safe_zones: List[Dict] = None) -> Dict:
        """Registra uma crianca para rastreamento."""
        self.tracked_persons[child_id] = {
            "name": child_name,
            "phone": child_phone,
            "last_location": None,
            "last_update": time.time(),
            "safe_zones": safe_zones or [],
            "status": "safe",
            "battery": 100,
        }
        if safe_zones:
            self.safe_zones = safe_zones
        return self.tracked_persons[child_id]

    def check_child_location(self, child_id: str, lat: float, lon: float,
                              battery: int = 100) -> Dict:
        """Verifica se crianca esta em zona segura."""
        if child_id not in self.tracked_persons:
            return {"error": "crianca nao registrada"}

        child = self.tracked_persons[child_id]
        child["last_location"] = (lat, lon)
        child["last_update"] = time.time()
        child["battery"] = battery

        # Verificar zonas seguras
        in_safe_zone = False
        for zone in child.get("safe_zones", []):
            dist = self._haversine(lat, lon, zone["lat"], zone["lon"])
            if dist <= zone.get("radius_m", 200):
                in_safe_zone = True
                break

        if in_safe_zone:
            child["status"] = "safe"
            return {
                "child_id": child_id,
                "name": child["name"],
                "status": "safe",
                "location": (lat, lon),
                "zone": zone["name"] if zone else "zona segura",
                "battery": battery,
                "message": f"{child['name']} esta na zona segura: {zone.get('name', 'casa')}."
            }
        else:
            child["status"] = "outside"
            # Verificar se mudou muito rapido (sequestro?)
            distance_from_safe = 999
            nearest_zone_name = ""
            for zone in child.get("safe_zones", []):
                dist = self._haversine(lat, lon, zone["lat"], zone["lon"])
                if dist < distance_from_safe:
                    distance_from_safe = dist
                    nearest_zone_name = zone.get("name", "zona")

            return {
                "child_id": child_id,
                "name": child["name"],
                "status": "outside_safe_zone",
                "location": (lat, lon),
                "distance_from_nearest_safe_m": round(distance_from_safe, 0),
                "nearest_zone": nearest_zone_name,
                "battery": battery,
                "message": (
                    f"ATENCAO: {child['name']} saiu da zona segura. "
                    f"Esta a {distance_from_safe:.0f} metros de {nearest_zone_name}. "
                    f"Bateria: {battery}%."
                ),
                "alert_level": "warning" if distance_from_safe < 1000 else "critical",
            }

    def find_nearby_help(self, help_type: str = "hospital") -> List[Dict]:
        """Encontra ajuda proxima (hospital, farmacia, delegacia)."""
        # Em producao: OpenStreetMap Overpass API
        return [
            {"name": "Hospital Sao Paulo", "distance_m": 800, "direction": "norte"},
            {"name": "UBS Vila Mariana", "distance_m": 1200, "direction": "leste"},
            {"name": "Farmacia 24h", "distance_m": 300, "direction": "oeste"},
        ]

    def _haversine(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Distancia em metros entre dois pontos GPS."""
        from math import radians, sin, cos, sqrt, atan2
        R = 6371000  # raio da terra em metros
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        return R * c


# ============================================================================
# 6. BIOMETRIA -- Smartwatch como Sensor Corporal
# ============================================================================

class BiometricEngine:
    """
    Usa smartwatch/monitor para detectar estados corporais.
    Previne crises, detecta quedas, monitora estresse.
    """

    def __init__(self):
        self.last_readings: deque = deque(maxlen=1000)
        self.baseline_heart_rate: int = 75
        self.fall_detected: bool = False

    def process_biometrics(self, heart_rate: int = 75, spo2: int = 98,
                           skin_temp: float = 36.5, movement: str = "normal") -> List[SensorReading]:
        """Processa dados biometricos."""
        readings = []

        # Deteccao de queda
        if movement == "fall":
            self.fall_detected = True
            reading = SensorReading(
                sensor=SensorType.ACCELEROMETER,
                perception=WorldPerception.FALL_DETECTION,
                value={"detected": True, "impact_g": 3.2},
                confidence=0.92,
                description="QUEDA DETECTADA. Voce esta bem? Responda em 30 segundos ou ligo para emergencia."
            )
            readings.append(reading)

        # Anomalia cardiaca
        if heart_rate > 120 or heart_rate < 50:
            reading = SensorReading(
                sensor=SensorType.HEART_RATE,
                perception=WorldPerception.HEART_ANOMALY,
                value={"heart_rate": heart_rate, "baseline": self.baseline_heart_rate},
                confidence=0.85,
                description=f"Frequencia cardiaca {heart_rate} bpm. Isso esta fora do normal."
            )
            readings.append(reading)

        # Deteccao de estresse (variabilidade cardiaca reduzida)
        if heart_rate > 100 and movement == "normal":
            reading = SensorReading(
                sensor=SensorType.HEART_RATE,
                perception=WorldPerception.STRESS_DETECTION,
                value={"heart_rate": heart_rate, "hrv_low": True},
                confidence=0.70,
                description="Seu coracao esta acelerado e voce esta parado. Talvez estresse. Quer respirar comigo?"
            )
            readings.append(reading)

        # Previsao de crise epileptica (HRV + skin temp spike)
        if skin_temp > 37.0 and heart_rate > 110:
            reading = SensorReading(
                sensor=SensorType.SKIN_TEMP,
                perception=WorldPerception.SEIZURE_PREDICTION,
                value={"skin_temp": skin_temp, "heart_rate": heart_rate, "risk": "moderate"},
                confidence=0.60,
                description="Sinais que podem preceder uma crise. Sente-se em local seguro."
            )
            readings.append(reading)

        # Tremor (Parkinson)
        if movement == "tremor":
            reading = SensorReading(
                sensor=SensorType.ACCELEROMETER,
                perception=WorldPerception.TREMOR_DETECTION,
                value={"frequency_hz": 5.0, "amplitude": "moderate"},
                confidence=0.80,
                description="Tremor detectado. Vou ajustar a sensibilidade dos botoes."
            )
            readings.append(reading)

        for r in readings:
            self.last_readings.append(r)
        return readings


# ============================================================================
# 7. TELEFONISTA -- A Voz que Conversa
# ============================================================================

class Telefonista:
    """
    A telefonista humana digital. Ela conversa com o usuario,
    capta o mundo pelos sensores, e responde como uma pessoa.

    DIFERENCA de um assistente de voz tradicional:
    - Alexa/Google: "Ok Google, qual a previsao do tempo"
    - Telefonista: "Cleiton, bom dia. Vi que esta nublado. Leva guarda-chuva.
                     Ah, e sua filha chegou na escola. Tudo certo."
    """

    def __init__(self, config: TelefonistaConfig):
        self.config = config
        self.cv_engine = ComputerVisionEngine()
        self.audio_engine = AudioPerceptionEngine()
        self.geo_engine = GeoLocationEngine()
        self.bio_engine = BiometricEngine()

        self.conversation_history: deque = deque(maxlen=500)
        self.user_emotion: EmotionalState = EmotionalState.NEUTRAL
        self.current_mode: ConversationMode = ConversationMode.DIALOGUE
        self.active_sensors: Set[SensorType] = set()
        self.user_name: str = ""
        self.user_disabilities: List[str] = []
        self.children_tracked: Dict[str, str] = {}  # id -> name

        self._setup_sensors()

    def _setup_sensors(self) -> None:
        """Configura sensores ativos baseado no hardware disponivel."""
        # Smartphone tem sempre camera + mic + gps
        self.active_sensors.update([
            SensorType.CAMERA_REAR, SensorType.CAMERA_FRONT,
            SensorType.MICROPHONE, SensorType.GPS,
            SensorType.ACCELEROMETER, SensorType.GYROSCOPE,
            SensorType.COMPASS, SensorType.LIGHT,
            SensorType.PROXIMITY,
        ])

    def greet(self, user_name: str, time_of_day: str = "manha") -> str:
        """Saudacao inicial personalizada."""
        self.user_name = user_name
        greetings = {
            "manha": "Bom dia",
            "tarde": "Boa tarde",
            "noite": "Boa noite",
        }
        g = greetings.get(time_of_day, "Ola")

        if self.config.personality == TelefonistaPersonality.GENTLE:
            msg = f"{g}, {user_name}. Aqui e a {self.config.name}. "
        elif self.config.personality == TelefonistaPersonality.CHEERFUL:
            msg = f"{g}, {user_name}! Que bom te ouvir! "
        elif self.config.personality == TelefonistaPersonality.FORMAL:
            msg = f"{g}. {self.config.name} a servico. "
        else:
            msg = f"{g}, {user_name}. "

        self._record(msg, "telefonista")
        return msg

    def listen_and_respond(self, user_input: str) -> str:
        """Processa entrada do usuario e responde como conversa."""
        self._record(user_input, "user")

        # Detectar emocao na fala
        emotion = self._detect_emotion(user_input)
        if emotion != self.user_emotion:
            self.user_emotion = emotion
            if self.config.emotional_adaptation:
                self.config.adapt_to_emotion(emotion)

        # Detectar intencao
        intent = self._detect_intent(user_input)
        response = self._respond(intent, user_input)

        self._record(response, "telefonista")
        return response

    def see_world(self) -> str:
        """Usa a camera para ver o mundo e narrar para o usuario."""
        readings = self.cv_engine.process_frame(SensorType.CAMERA_REAR)
        narration = self.cv_engine.narrate_scene(readings, ", ".join(self.user_disabilities))
        self._record(narration, "telefonista")
        return narration

    def hear_world(self) -> str:
        """Usa o microfone para ouvir o mundo e narrar para surdos."""
        readings = self.audio_engine.process_audio()
        narration = self.audio_engine.narrate_sounds(readings)
        self._record(narration, "telefonista")
        return narration

    def sense_body(self, heart_rate: int = 75, movement: str = "normal",
                   spo2: int = 98, skin_temp: float = 36.5) -> str:
        """Usa biometria para checar o corpo do usuario."""
        readings = self.bio_engine.process_biometrics(
            heart_rate=heart_rate, movement=movement, spo2=spo2, skin_temp=skin_temp
        )
        if not readings:
            return "Tudo normal com seu corpo."
        messages = [r.description for r in readings]
        msg = " ".join(messages)
        self._record(msg, "telefonista")
        return msg

    def navigate(self, destination: str) -> str:
        """Navegacao por voz (cego andando na rua)."""
        self.current_mode = ConversationMode.CO_DRIVER
        instruction = self.geo_engine.navigate_for_blind(destination)
        self._record(instruction, "telefonista")
        return instruction

    def check_on_child(self, child_id: str, lat: float, lon: float,
                       battery: int = 100) -> str:
        """Verifica localizacao de crianca rastreada."""
        result = self.geo_engine.check_child_location(child_id, lat, lon, battery)
        msg = result.get("message", "Sem informacoes.")
        self._record(msg, "telefonista")
        return msg

    def register_child(self, child_id: str, name: str, phone: str,
                       safe_zones: List[Dict] = None) -> str:
        """Registra crianca para rastreamento."""
        self.geo_engine.track_child(child_id, name, phone, safe_zones)
        self.children_tracked[child_id] = name
        msg = f"{name} registrada. Vou avisar se ela sair das zonas seguras."
        self._record(msg, "telefonista")
        return msg

    def find_help(self, help_type: str = "hospital") -> str:
        """Encontra ajuda proxima."""
        results = self.geo_engine.find_nearby_help(help_type)
        if not results:
            return "Nao encontrei nada proximo agora."
        parts = []
        for r in results:
            parts.append(f"{r['name']} a {r['distance_m']} metros ao {r['direction']}")
        msg = "Encontrei: " + ". ".join(parts) + "."
        self._record(msg, "telefonista")
        return msg

    def make_call(self, contact_name: str, reason: str = "") -> str:
        """Faz uma ligacao telefonica real."""
        reason_text = f" Motivo: {reason}." if reason else ""
        msg = f"Ligando para {contact_name}.{reason_text}"
        self._record(msg, "telefonista")
        # Em producao: intents Android/iOS para fazer ligacao
        return msg

    def emergency(self, service: str = "190") -> str:
        """Aciona emergencia."""
        self.current_mode = ConversationMode.EMERGENCY
        self.config.personality = TelefonistaPersonality.PROTECTIVE
        self.config.speech_rate = 0.9
        self.config.humor_enabled = False
        self.config.verbosity = 0.2
        msg = f"EMERGENCIA. Ligando para {service}. Fique calmo. Estou aqui."
        self._record(msg, "telefonista")
        return msg

    def dictate_code(self, code_input: str) -> str:
        """Usuario dita codigo, telefonista escreve."""
        self.current_mode = ConversationMode.DICTATION
        # Em producao: integracao com Talon/Cursorless para programacao por voz
        msg = f"Anotado. Escrevi: {code_input}. Quer que eu execute?"
        self._record(msg, "telefonista")
        return msg

    def _detect_emotion(self, text: str) -> EmotionalState:
        """Detecta emocao no texto (simplificado)."""
        text_lower = text.lower()
        if any(w in text_lower for w in ["cansado", "exausto", "durmo"]):
            return EmotionalState.TIRED
        if any(w in text_lower for w in ["estress", "put", "merda", "porra"]):
            return EmotionalState.STRESSED
        if any(w in text_lower for w in ["ansios", "preocup", "medo"]):
            return EmotionalState.ANXIOUS
        if any(w in text_lower for w in ["feliz", "otimo", "show", "massa"]):
            return EmotionalState.HAPPY
        if any(w in text_lower for w in ["foco", "trabalh", "concentrad"]):
            return EmotionalState.FOCUSED
        if any(w in text_lower for w in ["triste", "para", "desanim"]):
            return EmotionalState.SAD
        if any(w in text_lower for w in ["irritad", "irritante", "raiva"]):
            return EmotionalState.ANGRY
        if any(w in text_lower for w in ["muito", "sobrecarreg", "nao aguento"]):
            return EmotionalState.OVERWHELMED
        return EmotionalState.NEUTRAL

    def _detect_intent(self, text: str) -> str:
        """Detecta a intencao do usuario (simplificado)."""
        text_lower = text.lower()
        # Emergencia tem prioridade maxima
        if any(w in text_lower for w in ["socorro", "emergencia", "190", "192", "ajuda"]):
            return "emergency"
        if any(w in text_lower for w in ["codigo", "programar", "funcao", "variavel"]):
            return "code"
        if any(w in text_lower for w in ["onde estou", "localizacao", "rua"]):
            return "location"
        if any(w in text_lower for w in ["minha filha", "meu filho", "crianca"]):
            return "child"
        if any(w in text_lower for w in ["cor", "vermelho", "verde", "azul"]):
            return "color"
        if any(w in text_lower for w in ["ligar", "telefone", "chamada"]):
            return "call"
        if any(w in text_lower for w in ["ve", "olha", "camera", "enxergar"]):
            return "see"
        if any(w in text_lower for w in ["ouvir", "som", "barulho"]):
            return "hear"
        if any(w in text_lower for w in ["navegar", "ir para", "como chego"]):
            return "navigate"
        return "chat"

    def _respond(self, intent: str, user_input: str) -> str:
        """Gera resposta baseada na intencao e personalidade."""
        name = self.user_name or "amigo"

        if intent == "code":
            return self.dictate_code(user_input)
        if intent == "location":
            return self.geo_engine.navigate_for_blind("")
        if intent == "child":
            return "Quer que eu verifique onde ela esta?"
        if intent == "color":
            readings = self.cv_engine.process_frame(SensorType.CAMERA_REAR)
            color_reading = [r for r in readings if r.perception == WorldPerception.COLOR_DETECTION]
            if color_reading:
                return color_reading[0].description
            return "Aponta a camera que eu vejo a cor."
        if intent == "emergency":
            return self.emergency("192")
        if intent == "call":
            return "Para quem voce quer ligar?"
        if intent == "see":
            return self.see_world()
        if intent == "hear":
            return self.hear_world()
        if intent == "navigate":
            return "Para onde voce quer ir?"
        # Chat default
        if self.user_emotion == EmotionalState.TIRED:
            return f"{name}, voce parece cansado. Que tal uma pausa? Posso continuar depois."
        if self.user_emotion == EmotionalState.STRESSED:
            return f"Respira, {name}. Uma coisa de cada vez. No que eu posso ajudar agora?"
        if self.user_emotion == EmotionalState.HAPPY:
            return f"Que bom te ouvir feliz, {name}! No que posso ajudar?"
        return f"Entendi. Conte mais, {name}."

    def _record(self, text: str, speaker: str) -> None:
        """Registra na historia da conversa."""
        self.conversation_history.append({
            "speaker": speaker,
            "text": text,
            "timestamp": time.time(),
            "emotion": self.user_emotion.value if speaker == "user" else None,
        })

    def conversation_summary(self) -> Dict[str, Any]:
        """Resumo da conversa."""
        return {
            "telefonista_name": self.config.name,
            "user_name": self.user_name,
            "total_exchanges": len(self.conversation_history),
            "current_emotion": self.user_emotion.value,
            "current_mode": self.current_mode.value,
            "active_sensors": len(self.active_sensors),
            "children_tracked": len(self.children_tracked),
            "personality": self.config.personality.value,
        }


# ============================================================================
# 8. ADAPTACAO POR DEFICIENCIA
# ============================================================================

def create_telefonista_for_blind(user_name: str = "") -> Telefonista:
    """Telefonista para cego: voz + camera + GPS + ligacao."""
    config = TelefonistaConfig(
        name="Iara",
        personality=TelefonistaPersonality.GENTLE,
        speech_rate=1.3,  # cegos escutam rapido
        verbosity=0.7,
        proactive=0.6,
    )
    t = Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = ["visual"]
    t.current_mode = ConversationMode.CO_DRIVER
    return t


def create_telefonista_for_deaf(user_name: str = "") -> Telefonista:
    """Telefonista para surdo: visual + haptico + legenda."""
    config = TelefonistaConfig(
        name="Iara",
        personality=TelefonistaPersonality.GENTLE,
        speech_rate=1.0,
        verbosity=0.5,
    )
    t = Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = ["auditiva"]
    t.current_mode = ConversationMode.SILENT  # so visual/haptico
    return t


def create_telefonista_for_motor(user_name: str = "") -> Telefonista:
    """Telefonista para tetraplegia: voz pura, sem botoes."""
    config = TelefonistaConfig(
        name="Iara",
        personality=TelefonistaPersonality.CHEERFUL,
        speech_rate=1.0,
        verbosity=0.6,
        proactive=0.5,  # antecipa para reduzir necessidade de input
    )
    t = Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = ["motora"]
    t.current_mode = ConversationMode.DIALOGUE
    return t


def create_telefonista_for_autism(user_name: str = "") -> Telefonista:
    """Telefonista para autista: calma, previsivel, sem surpresas."""
    config = TelefonistaConfig(
        name="Iara",
        personality=TelefonistaPersonality.GENTLE,
        speech_rate=0.9,
        verbosity=0.3,
        humor_enabled=False,
        proactive=0.2,
    )
    t = Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = ["espectro_autista"]
    t.current_mode = ConversationMode.DIALOGUE
    return t


def create_telefonista_for_child(user_name: str = "") -> Telefonista:
    """Telefonista para crianca: brincalhona, simples, protetora."""
    config = TelefonistaConfig(
        name="Tia Iara",
        personality=TelefonistaPersonality.PLAYFUL,
        speech_rate=0.85,
        verbosity=0.3,
        proactive=0.4,
    )
    t = Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = []
    t.current_mode = ConversationMode.DIALOGUE
    return t


def create_telefonista_for_elderly(user_name: str = "") -> Telefonista:
    """Telefonista para idoso: devagar, formosa, protetora."""
    config = TelefonistaConfig(
        name="Iara",
        personality=TelefonistaPersonality.PROTECTIVE,
        speech_rate=0.8,
        verbosity=0.6,
        humor_enabled=True,
        proactive=0.7,  # antecipa muito
        formality=0.6,
    )
    t = Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = []
    t.current_mode = ConversationMode.DIALOGUE
    return t


# ============================================================================
# 9. CENARIOS DO MUNDO REAL
# ============================================================================

def scenario_blind_walking():
    """Cenario: cego andando na rua."""
    print("=" * 60)
    print("CENARIO: Cego andando na rua")
    print("=" * 60)

    t = create_telefonista_for_blind("Cleiton")
    print(t.greet("Cleiton", "manha"))

    # Camera ve obstaculos + semaforo
    print(f"\n[Camera]")
    print(t.see_world())

    # GPS navega
    print(f"\n[GPS]")
    print(t.navigate("padaria"))

    # Reconhece dinheiro
    readings = t.cv_engine.process_frame(SensorType.CAMERA_REAR)
    for r in readings:
        if r.perception == WorldPerception.MONEY_RECOGNITION:
            print(f"\n[Dinheiro]")
            print(r.description)

    # Microfone ouve sirene
    print(f"\n[Audio]")
    print(t.hear_world())


def scenario_deaf_conversation():
    """Cenario: surdo em conversa com legenda em tempo real."""
    print("\n" + "=" * 60)
    print("CENARIO: Surdo em conversa")
    print("=" * 60)

    t = create_telefonista_for_deaf("Maria")
    print(f"[Visual] {t.greet('Maria', 'tarde')}")

    # Microfone transcreve + classifica sons
    print(f"\n[Audio -> Visual]")
    print(f"[Visual] {t.hear_world()}")


def scenario_colorblind_shopping():
    """Cenario: daltonico comprando roupas."""
    print("\n" + "=" * 60)
    print("CENARIO: Daltonico comprando roupas")
    print("=" * 60)

    t = Telefonista(TelefonistaConfig(name="Iara"))
    t.user_name = "Joao"
    t.user_disabilities = ["visual"]

    print(t.greet("Joao", "tarde"))
    print("\n[Camera apontada para roupa]")
    readings = t.cv_engine.process_frame(SensorType.CAMERA_REAR)
    for r in readings:
        if r.perception == WorldPerception.COLOR_DETECTION:
            print(f"  {r.description}")
    print("\n[Camera apontada para semaforo]")
    for r in readings:
        if r.perception == WorldPerception.TRAFFIC_LIGHT:
            print(f"  {r.description}")


def scenario_lost_child():
    """Cenario: crianca perdida rastreada por GPS."""
    print("\n" + "=" * 60)
    print("CENARIO: Geolocalizacao de crianca")
    print("=" * 60)

    t = Telefonista(TelefonistaConfig(name="Iara", personality=TelefonistaPersonality.PROTECTIVE))
    t.user_name = "Cleiton"

    # Registrar crianca
    safe_zones = [
        {"name": "Casa", "lat": -23.55, "lon": -46.63, "radius_m": 200},
        {"name": "Escola", "lat": -23.56, "lon": -46.64, "radius_m": 200},
    ]
    print(t.register_child("child_01", "Sophia", "+5511999999999", safe_zones))

    # Crianca na escola (seguro)
    print(f"\n[Sophia na escola]")
    print(t.check_on_child("child_01", -23.56, -46.64, battery=85))

    # Crianca fora da zona segura
    print(f"\n[Sophia em local desconhecido]")
    result = t.geo_engine.check_child_location("child_01", -23.60, -46.70, battery=45)
    print(f"  {result['message']}")
    print(f"  Nivel: {result.get('alert_level', 'info')}")

    # Bateria fraca
    print(f"\n[Sophia com bateria fraca]")
    result = t.geo_engine.check_child_location("child_01", -23.58, -46.66, battery=12)
    print(f"  {result['message']}")


def scenario_fall_detection():
    """Cenario: idoso cai, sistema detecta e liga."""
    print("\n" + "=" * 60)
    print("CENARIO: Deteccao de queda (idoso)")
    print("=" * 60)

    t = create_telefonista_for_elderly("Dona Maria")
    print(t.greet("Dona Maria", "manha"))

    # Detecta queda
    print(f"\n[Queda detectada!]")
    print(t.sense_body(heart_rate=110, movement="fall"))

    # 30s sem resposta -> emergencia
    print(f"\n[Sem resposta em 30s]")
    print(t.emergency("192"))


def scenario_stress_detection():
    """Cenario: deteccao de estresse por smartwatch."""
    print("\n" + "=" * 60)
    print("CENARIO: Deteccao de estresse")
    print("=" * 60)

    t = Telefonista(TelefonistaConfig(name="Iara"))
    t.user_name = "Cleiton"

    print("Coracao acelerado, voce esta parado...")
    print(t.sense_body(heart_rate=115, movement="normal"))

    print("\nVoce diz: 'to estressado pra caralho'")
    print(t.listen_and_respond("to estressado pra caralho"))


def scenario_epilepsy_warning():
    """Cenario: previsao de crise epileptica."""
    print("\n" + "=" * 60)
    print("CENARIO: Previsao de crise epileptica")
    print("=" * 60)

    t = Telefonista(TelefonistaConfig(
        name="Iara", personality=TelefonistaPersonality.PROTECTIVE
    ))
    t.user_name = "Pedro"
    print(t.greet("Pedro", "tarde"))

    # Biometria detecta risco
    print(f"\n[Sinais pre-crise]")
    print(t.sense_body(heart_rate=115, skin_temp=37.5, movement="normal"))


# ============================================================================
# 10. DEMONSTRACAO COMPLETA
# ============================================================================

def demo():
    print("=" * 70)
    print("OpenTelefonista -- O Sistema Como Conversa Humana")
    print("=" * 70)

    print(f"\nTelefonista: Iara")
    print(f"Personalidades: {len(TelefonistaPersonality)}")
    print(f"Estados emocionais: {len(EmotionalState)}")
    print(f"Modos de conversa: {len(ConversationMode)}")
    print(f"Tipos de sensor: {len(SensorType)}")
    print(f"Percepcoes do mundo: {len(WorldPerception)}")

    # Cenarios do mundo real
    scenario_blind_walking()
    scenario_deaf_conversation()
    scenario_colorblind_shopping()
    scenario_lost_child()
    scenario_fall_detection()
    scenario_stress_detection()
    scenario_epilepsy_warning()

    # Perfis
    print(f"\n{'=' * 70}")
    print("PERFIS DA TELEFONISTA")
    print(f"{'=' * 70}")

    profiles = {
        "Cego": create_telefonista_for_blind("Cleiton"),
        "Surdo": create_telefonista_for_deaf("Maria"),
        "Tetraplegico": create_telefonista_for_motor("Joao"),
        "Autista": create_telefonista_for_autism("Pedro"),
        "Crianca": create_telefonista_for_child("Sophia"),
        "Idoso": create_telefonista_for_elderly("Dona Cecca"),
    }

    for label, t in profiles.items():
        print(f"\n  {label}:")
        print(f"    Nome: {t.config.name}")
        print(f"    Personalidade: {t.config.personality.value}")
        print(f"    Velocidade: {t.config.speech_rate}x")
        print(f"    Modo: {t.current_mode.value}")
        print(f"    Sensores ativos: {len(t.active_sensors)}")

    # Cobertura
    print(f"\n{'=' * 70}")
    print("COBERTURA DE PERCEPCAO DO MUNDO")
    print(f"{'=' * 70}")

    perception_categories = {
        "VISAO (camera como olhos)": [
            WorldPerception.COLOR_DETECTION,
            WorldPerception.TEXT_RECOGNITION,
            WorldPerception.OBSTACLE_DETECTION,
            WorldPerception.TRAFFIC_LIGHT,
            WorldPerception.MONEY_RECOGNITION,
            WorldPerception.FACE_RECOGNITION,
            WorldPerception.CROSSWALK_DETECTION,
        ],
        "AUDICAO (microfone como ouvidos)": [
            WorldPerception.SPEECH_TO_TEXT,
            WorldPerception.SOUND_CLASSIFICATION,
            WorldPerception.DOORBELL,
            WorldPerception.SIREN,
            WorldPerception.BABY_CRYING,
            WorldPerception.ALARM_SOUND,
        ],
        "LOCALIZACAO (GPS como direcao)": [
            WorldPerception.GPS_LOCATION,
            WorldPerception.INDOOR_LOCATION,
            WorldPerception.DIRECTION_FACING,
            WorldPerception.LOST_CHILD,
            WorldPerception.NEARBY_PLACES,
        ],
        "BIOMETRIA (smartwatch como corpo)": [
            WorldPerception.FALL_DETECTION,
            WorldPerception.HEART_ANOMALY,
            WorldPerception.STRESS_DETECTION,
            WorldPerception.SEIZURE_PREDICTION,
            WorldPerception.TREMOR_DETECTION,
        ],
    }

    for category, perceptions in perception_categories.items():
        print(f"\n  {category}:")
        for p in perceptions:
            print(f"    - {p.value}")

    print(f"\n{'=' * 70}")
    print(f"Total percepcoes: {len(WorldPerception)}")
    print(f"Total sensores: {len(SensorType)}")
    print(f"Total personalidades: {len(TelefonistaPersonality)}")
    print(f"\nO sistema NAO e um app. E uma CONVERSA.")
    print(f"A interface NAO e uma tela. E uma VOZ.")
    print(f"O smartphone NAO e um dispositivo. E o CORPO EXTENDIDO.")
    print(f"\nTODO hardware. TODA deficiencia. ZERO barreira.")
    print(f"UMA conversa.")


if __name__ == "__main__":
    demo()
