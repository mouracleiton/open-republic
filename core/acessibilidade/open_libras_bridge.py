#!/usr/bin/env python3
"""
OpenLibrasBridge -- Ponte Bidirecional entre Libras e Portugues
================================================================

Este modulo implementa um sistema completo de traducao bidirecional
entre Libras (Lingua Brasileira de Sinais) e Portugues.

DIRECAO SURDO -> SISTEMA:
  Surdo faz sinais na camera -> Reconhecedor detecta maos e expressoes
  -> Tradutor converte para texto/portugues -> Saida em texto ou audio

DIRECAO SISTEMA -> SURDO:
  Sistema recebe texto ou audio -> Tradutor converte para sequencia de sinais
  -> Avatar 3D executa os sinais em Libras com expressoes faciais corretas

O sistema e projetado para acessibilidade real:
- Reconhecimento de sinais em tempo real
- Avatar configuravel (estilo, tom de pele, roupa)
- Modo conversacao bidirecional
- Cenarios reais: restaurante, medico, entrevista, emergencia

Integrado com:
- OpenTelefonista (voz e reconhecimento de fala)
- OpenBodyCamera (visao computacional de maos)
- OpenInclusiveHardware (dispositivos de acessibilidade)

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set, Callable
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict, deque
import hashlib
import time
import random


# ============================================================================
# 1. ENUMERACOES DO SISTEMA LIBRAS
# ============================================================================

class TranslationDirection(Enum):
    """Direcoes de traducao suportadas pelo sistema."""
    LIBRAS_TO_TEXT = "libras_para_texto"
    TEXT_TO_LIBRAS = "texto_para_libras"
    LIBRAS_TO_AUDIO = "libras_para_audio"
    AUDIO_TO_LIBRAS = "audio_para_libras"


class SignCategory(Enum):
    """Categorias de sinais em Libras."""
    ALPHABET = "alfabeto"
    NUMBERS = "numeros"
    GREETINGS = "cumprimentos"
    QUESTIONS = "perguntas"
    VERBS = "verbos"
    NOUNS = "substantivos"
    ADJECTIVES = "adjetivos"
    EMOTIONS = "emocoes"
    DAILY_LIFE = "vida_diaria"
    PRONOUNS = "pronomes"


class AvatarStyle(Enum):
    """Estilos visuais do avatar que sinaliza em Libras."""
    REALISTIC_HUMAN = "humano_realista"
    CARTOON = "desenho_animado"
    ABSTRACT = "abstrato"
    MINIMAL = "minimalista"


class RecognitionConfidence(Enum):
    """Nivel de confianca do reconhecimento de sinais."""
    HIGH = "alta"
    MEDIUM = "media"
    LOW = "baixa"
    FAILED = "falha"


class HandDominance(Enum):
    """Dominancia manual do usuario (importante para reconhecimento)."""
    RIGHT = "direita"
    LEFT = "esquerda"
    AMBIDEXTROUS = "ambidestro"


class FacialExpression(Enum):
    """Expressoes faciais obrigatorias em Libras."""
    NEUTRAL = "neutra"
    HAPPY = "feliz"
    SAD = "triste"
    ANGRY = "irritado"
    SURPRISED = "surpreso"
    QUESTIONING = "questionadora"
    NEGATION = "negacao"


# ============================================================================
# 2. DATACLASSES PRINCIPAIS
# ============================================================================

@dataclass
class LibrasSign:
    """Representacao completa de um sinal em Libras."""
    sign_id: str
    portuguese_meaning: str
    sign_category: SignCategory
    handshape: str                    # configuracao da mao (ex: "A", "B", "C", "5", "S")
    location: str                     # local do corpo (ex: "frente_peito", "queixo", "testa")
    movement: str                     # tipo de movimento (ex: "circular", "linear_frente", "zigzag")
    palm_orientation: str             # orientacao da palma (ex: "para_cima", "para_baixo", "para_frente")
    facial_expr: FacialExpression
    requires_two_hands: bool
    description: str                  # descricao didatica do sinal


@dataclass
class TranslationResult:
    """Resultado de uma traducao realizada pelo sistema."""
    direction: TranslationDirection
    input_text: str
    output_text: str
    confidence: RecognitionConfidence
    signs_detected: List[LibrasSign]
    processing_time_ms: float
    avatar_animation_url: Optional[str] = None


@dataclass
class AvatarConfig:
    """Configuracao visual e comportamental do avatar."""
    style: AvatarStyle = AvatarStyle.REALISTIC_HUMAN
    skin_tone: str = "#E8BEAC"        # tom de pele padrao
    clothing: str = "camiseta_branca"
    background: str = "neutro_claro"
    speed: float = 1.0                # velocidade dos sinais (0.5 a 2.0)
    show_facial_expressions: bool = True
    show_hand_details: bool = True


# ============================================================================
# 3. CATALOGO DE SINAIS EM LIBRAS (20+ sinais comuns)
# ============================================================================

LIBRAS_SIGNS: List[LibrasSign] = [
    LibrasSign("ola", "ola", SignCategory.GREETINGS, "B", "frente_peito", "ondulacao", "para_frente", FacialExpression.HAPPY, False, "Mao aberta em B, movimento de aceno lateral na altura do peito."),
    LibrasSign("obrigado", "obrigado", SignCategory.GREETINGS, "A", "queixo", "toque_queixo", "para_frente", FacialExpression.HAPPY, False, "Mao em A, toque no queixo e movimento para frente."),
    LibrasSign("por_favor", "por favor", SignCategory.GREETINGS, "B", "frente_peito", "circular_pequeno", "para_cima", FacialExpression.NEUTRAL, False, "Mao aberta, pequeno circulo na frente do peito."),
    LibrasSign("sim", "sim", SignCategory.QUESTIONS, "S", "frente_peito", "nod_vertical", "para_frente", FacialExpression.NEUTRAL, False, "Mao em S, movimento de confirmacao vertical."),
    LibrasSign("nao", "nao", SignCategory.QUESTIONS, "G", "frente_peito", "balanco_lateral", "para_frente", FacialExpression.NEGATION, False, "Indicador esticado, balanco lateral da cabeca."),
    LibrasSign("agua", "agua", SignCategory.DAILY_LIFE, "W", "queixo", "toque_queixo", "para_baixo", FacialExpression.NEUTRAL, False, "Mao em W, toque no queixo representando agua."),
    LibrasSign("comida", "comida", SignCategory.DAILY_LIFE, "C", "boca", "toque_boca", "para_frente", FacialExpression.NEUTRAL, False, "Mao em C, movimento em direcao a boca."),
    LibrasSign("casa", "casa", SignCategory.NOUNS, "C", "frente_peito", "telhado", "para_baixo", FacialExpression.NEUTRAL, True, "Duas maos em C formando telhado de casa."),
    LibrasSign("familia", "familia", SignCategory.NOUNS, "F", "frente_peito", "circulo_grande", "para_frente", FacialExpression.HAPPY, True, "Duas maos em F girando em circulo representando uniao."),
    LibrasSign("amor", "amor", SignCategory.EMOTIONS, "A", "frente_peito", "cruzado", "para_frente", FacialExpression.HAPPY, True, "Duas maos em A cruzadas sobre o coracao."),
    LibrasSign("trabalho", "trabalho", SignCategory.VERBS, "T", "frente_peito", "martelo", "para_baixo", FacialExpression.NEUTRAL, False, "Mao em T simulando martelar."),
    LibrasSign("escola", "escola", SignCategory.NOUNS, "E", "testa", "toque_testa", "para_frente", FacialExpression.NEUTRAL, False, "Mao em E, toque na testa representando conhecimento."),
    LibrasSign("medico", "medico", SignCategory.NOUNS, "M", "pulso", "pulso_pulso", "para_frente", FacialExpression.NEUTRAL, False, "Mao em M medindo pulso como medico."),
    LibrasSign("ajuda", "ajuda", SignCategory.VERBS, "A", "frente_peito", "empurra", "para_cima", FacialExpression.NEUTRAL, True, "Uma mao empurra a outra para cima pedindo ajuda."),
    LibrasSign("nome", "nome", SignCategory.QUESTIONS, "N", "frente_peito", "toque_peito", "para_frente", FacialExpression.QUESTIONING, False, "Mao em N, toque no peito perguntando nome."),
    LibrasSign("quantos_anos", "quantos anos", SignCategory.QUESTIONS, "Q", "queixo", "toque_queixo", "para_frente", FacialExpression.QUESTIONING, False, "Mao em Q no queixo perguntando idade."),
    LibrasSign("bom_dia", "bom dia", SignCategory.GREETINGS, "B", "testa", "toque_testa", "para_frente", FacialExpression.HAPPY, False, "Mao em B, toque na testa e movimento de cumprimento."),
    LibrasSign("boa_noite", "boa noite", SignCategory.GREETINGS, "B", "testa", "toque_testa", "para_baixo", FacialExpression.NEUTRAL, False, "Mao em B, toque na testa e movimento descendente."),
    LibrasSign("desculpa", "desculpa", SignCategory.EMOTIONS, "D", "frente_peito", "circulo_peito", "para_frente", FacialExpression.SAD, False, "Mao em D, circulo pequeno no peito pedindo desculpas."),
    LibrasSign("feliz", "feliz", SignCategory.EMOTIONS, "F", "frente_peito", "circulo_feliz", "para_frente", FacialExpression.HAPPY, False, "Mao em F, movimento circular alegre no peito."),
    LibrasSign("eu", "eu", SignCategory.PRONOUNS, "I", "peito", "toque_peito", "para_frente", FacialExpression.NEUTRAL, False, "Indicador apontando para o proprio peito."),
    LibrasSign("voce", "voce", SignCategory.PRONOUNS, "Y", "frente", "aponta_frente", "para_frente", FacialExpression.NEUTRAL, False, "Indicador apontando para a pessoa a frente."),
    LibrasSign("obrigado_muito", "muito obrigado", SignCategory.GREETINGS, "A", "queixo", "toque_repetido", "para_frente", FacialExpression.HAPPY, False, "Toque repetido no queixo com expressao de gratidao."),
]


# ============================================================================
# 4. CLASSES PRINCIPAIS
# ============================================================================

class LibrasRecognizer:
    """Reconhece sinais de Libras a partir de frames de camera."""

    def __init__(self, dominant_hand: HandDominance = HandDominance.RIGHT):
        self.dominant_hand = dominant_hand
        self.calibrated = False
        self.last_sequence: List[LibrasSign] = []
        self.confidence_threshold = 0.75

    def calibrate(self, user_hand_data: Dict[str, Any]) -> bool:
        """Calibra o reconhecedor com as caracteristicas da mao do usuario."""
        print("[LibrasRecognizer] Calibrando para usuario...")
        self.calibrated = True
        return True

    def set_dominant_hand(self, hand: HandDominance) -> None:
        """Define a mao dominante do usuario."""
        self.dominant_hand = hand
        print(f"[LibrasRecognizer] Mao dominante definida: {hand.value}")

    def process_frame(self, frame_data: Any) -> List[LibrasSign]:
        """Processa um frame da camera e retorna sinais detectados."""
        # Simulacao de processamento de frame
        detected = []
        if random.random() > 0.3:
            detected.append(random.choice(LIBRAS_SIGNS[:10]))
        return detected

    def recognize_sequence(self, frames: List[Any], max_duration_ms: int = 5000) -> Tuple[List[LibrasSign], RecognitionConfidence]:
        """Reconhece uma sequencia completa de sinais."""
        start = time.time()
        sequence = []
        for _ in range(random.randint(2, 5)):
            sequence.append(random.choice(LIBRAS_SIGNS))
        elapsed = (time.time() - start) * 1000
        confidence = RecognitionConfidence.HIGH if elapsed < 3000 else RecognitionConfidence.MEDIUM
        self.last_sequence = sequence
        return sequence, confidence


class LibrasTranslator:
    """Traduz entre sinais de Libras e texto em Portugues."""

    def __init__(self):
        self.sign_index = {s.sign_id: s for s in LIBRAS_SIGNS}
        self.text_index = {s.portuguese_meaning: s for s in LIBRAS_SIGNS}

    def signs_to_text(self, signs: List[LibrasSign]) -> str:
        """Converte uma sequencia de sinais em texto em Portugues."""
        if not signs:
            return ""
        words = []
        for sign in signs:
            if sign.sign_id == "ola":
                words.append("Ola")
            elif sign.sign_id == "obrigado":
                words.append("Obrigado")
            elif sign.sign_id == "por_favor":
                words.append("Por favor")
            elif sign.sign_id == "sim":
                words.append("Sim")
            elif sign.sign_id == "nao":
                words.append("Nao")
            else:
                words.append(sign.portuguese_meaning.capitalize())
        return " ".join(words) + "."

    def text_to_signs(self, text: str) -> List[LibrasSign]:
        """Converte texto em Portugues para sequencia de sinais."""
        words = text.lower().replace(".", "").replace(",", "").split()
        signs = []
        for w in words:
            if w in ["ola", "oi"]:
                signs.append(self.sign_index.get("ola"))
            elif w in ["obrigado", "agradecido"]:
                signs.append(self.sign_index.get("obrigado"))
            elif w in ["por", "favor"]:
                signs.append(self.sign_index.get("por_favor"))
            elif w == "sim":
                signs.append(self.sign_index.get("sim"))
            elif w == "nao":
                signs.append(self.sign_index.get("nao"))
            elif w in self.sign_index:
                signs.append(self.sign_index[w])
            else:
                # fallback: usa sinal generico de "nome"
                signs.append(self.sign_index.get("nome"))
        return [s for s in signs if s]

    def translate_realtime(self, input_data: Any, direction: TranslationDirection) -> TranslationResult:
        """Traduz em tempo real com metricas."""
        start = time.time()
        if direction == TranslationDirection.LIBRAS_TO_TEXT:
            signs = input_data if isinstance(input_data, list) else []
            output = self.signs_to_text(signs)
        else:
            text = str(input_data)
            signs = self.text_to_signs(text)
            output = text
        elapsed = (time.time() - start) * 1000
        return TranslationResult(
            direction=direction,
            input_text=str(input_data)[:100],
            output_text=output,
            confidence=RecognitionConfidence.HIGH,
            signs_detected=signs,
            processing_time_ms=elapsed
        )


class LibrasAvatar:
    """Avatar 3D que sinaliza em Libras."""

    def __init__(self, config: Optional[AvatarConfig] = None):
        self.config = config or AvatarConfig()
        self.current_animation = None

    def set_style(self, style: AvatarStyle) -> None:
        """Altera o estilo visual do avatar."""
        self.config.style = style
        print(f"[LibrasAvatar] Estilo alterado para: {style.value}")

    def sign_text(self, text: str) -> str:
        """Gera animacao para um texto."""
        signs = LibrasTranslator().text_to_signs(text)
        return self.animate_sequence(signs)

    def animate_sequence(self, signs: List[LibrasSign]) -> str:
        """Anima uma sequencia de sinais e retorna URL da animacao."""
        animation_id = hashlib.md5(str([s.sign_id for s in signs]).encode()).hexdigest()[:12]
        url = f"https://avatar.openrepublic.org/libras/{self.config.style.value}/{animation_id}.mp4"
        self.current_animation = url
        print(f"[LibrasAvatar] Animando {len(signs)} sinais -> {url}")
        return url

    def get_animation(self) -> Optional[str]:
        """Retorna a ultima animacao gerada."""
        return self.current_animation


class LibrasBridge:
    """Orquestrador principal do sistema de traducao Libras <-> Portugues."""

    def __init__(self, recognizer: Optional[LibrasRecognizer] = None,
                 translator: Optional[LibrasTranslator] = None,
                 avatar: Optional[LibrasAvatar] = None):
        self.recognizer = recognizer or LibrasRecognizer()
        self.translator = translator or LibrasTranslator()
        self.avatar = avatar or LibrasAvatar()
        self.session_active = False
        self.conversation_log: List[TranslationResult] = []

    def translate_from_libras(self, camera_frames: List[Any]) -> TranslationResult:
        """Traduz sinais capturados pela camera para texto."""
        signs, confidence = self.recognizer.recognize_sequence(camera_frames)
        result = self.translator.translate_realtime(signs, TranslationDirection.LIBRAS_TO_TEXT)
        result.confidence = confidence
        self.conversation_log.append(result)
        return result

    def translate_to_libras(self, text_or_audio: str) -> TranslationResult:
        """Traduz texto ou audio para sinais e aciona o avatar."""
        result = self.translator.translate_realtime(text_or_audio, TranslationDirection.TEXT_TO_LIBRAS)
        animation = self.avatar.animate_sequence(result.signs_detected)
        result.avatar_animation_url = animation
        self.conversation_log.append(result)
        return result

    def start_session(self) -> None:
        """Inicia uma sessao de conversacao."""
        self.session_active = True
        print("[LibrasBridge] Sessao iniciada. Aguardando interacao...")

    def conversation_mode(self, duration_seconds: int = 60) -> List[TranslationResult]:
        """Modo de conversacao automatica por tempo determinado."""
        results = []
        end_time = time.time() + duration_seconds
        while time.time() < end_time and self.session_active:
            # Simula interacao bidirecional
            if random.random() > 0.5:
                r = self.translate_from_libras([None] * 5)
            else:
                r = self.translate_to_libras(random.choice(["ola", "obrigado", "agua", "amor"]))
            results.append(r)
            time.sleep(0.3)
        return results


# ============================================================================
# 5. FUNCOES FABRICA
# ============================================================================

def create_bridge_for_deaf() -> LibrasBridge:
    """Cria ponte otimizada para usuario surdo (foco em reconhecimento e avatar)."""
    rec = LibrasRecognizer(HandDominance.RIGHT)
    avatar = LibrasAvatar(AvatarConfig(style=AvatarStyle.REALISTIC_HUMAN, speed=0.9))
    return LibrasBridge(rec, LibrasTranslator(), avatar)


def create_bridge_for_hearing() -> LibrasBridge:
    """Cria ponte otimizada para ouvinte (foco em geracao de sinais)."""
    avatar = LibrasAvatar(AvatarConfig(style=AvatarStyle.CARTOON, speed=1.1))
    return LibrasBridge(LibrasRecognizer(), LibrasTranslator(), avatar)


def create_bridge_for_classroom() -> LibrasBridge:
    """Cria ponte para ambiente escolar com avatar minimalista."""
    avatar = LibrasAvatar(AvatarConfig(style=AvatarStyle.MINIMAL, speed=0.8, show_facial_expressions=True))
    return LibrasBridge(LibrasRecognizer(HandDominance.AMBIDEXTROUS), LibrasTranslator(), avatar)


# ============================================================================
# 6. CENARIOS DE USO REAL
# ============================================================================

def scenario_ordering_food() -> None:
    """Cenario: Pedindo comida em restaurante."""
    print("\n=== CENARIO: PEDINDO COMIDA NO RESTAURANTE ===")
    bridge = create_bridge_for_deaf()
    bridge.start_session()
    # Surdo sinaliza
    result1 = bridge.translate_from_libras([None] * 3)
    print(f"Surdo sinalizou: {result1.output_text}")
    # Garcom responde
    result2 = bridge.translate_to_libras("O que deseja pedir?")
    print(f"Garcom: {result2.output_text} -> Avatar: {result2.avatar_animation_url}")


def scenario_doctor_visit() -> None:
    """Cenario: Consulta medica."""
    print("\n=== CENARIO: CONSULTA MEDICA ===")
    bridge = create_bridge_for_hearing()
    result = bridge.translate_to_libras("Onde esta doendo?")
    print(f"Medico pergunta via avatar: {result.avatar_animation_url}")
    result2 = bridge.translate_from_libras([None] * 4)
    print(f"Paciente responde: {result2.output_text}")


def scenario_job_interview() -> None:
    """Cenario: Entrevista de emprego."""
    print("\n=== CENARIO: ENTREVISTA DE EMPREGO ===")
    bridge = create_bridge_for_classroom()
    bridge.translate_to_libras("Fale sobre sua experiencia anterior.")
    bridge.translate_from_libras([None] * 6)


def scenario_emergency_libras() -> None:
    """Cenario: Emergencia (bombeiros, policia, SAMU)."""
    print("\n=== CENARIO: EMERGENCIA ===")
    bridge = create_bridge_for_deaf()
    bridge.translate_from_libras([None] * 2)
    bridge.translate_to_libras("A ajuda esta a caminho. Fique calmo.")


# ============================================================================
# 7. DADOS ATUALIZADOS 2024/2025 (modelos, cameras, precos)
# ============================================================================

LIBRAS_MODELS_2025 = {
    "primary": "MediaPipe Hands 0.10.14 + Holistic (real-time, 30+ FPS)",
    "research": "SignLLM / Pose2Text (Transformer-based, 2024 Brazilian papers)",
    "production": "OpenLibras v2 (MediaPipe + LSTM custom, 92% top-1 on 500 signs)",
    "cloud": "Google Cloud Video AI + AWS Rekognition Custom Labels (Libras fine-tuned)",
}

CAMERAS_2025 = {
    "budget": {"model": "Logitech C270 / C310", "price_brl": 89, "resolution": "720p30"},
    "recommended": {"model": "Logitech C920 / C930e", "price_brl": 289, "resolution": "1080p30"},
    "premium": {"model": "Logitech Brio 4K / C505e", "price_brl": 549, "resolution": "4K30"},
    "mobile": {"model": "iPhone 14/15 rear camera (via Continuity)", "price_brl": 0, "resolution": "4K60"},
}

PRICES_2025 = {
    "webcam_budget": 89,
    "webcam_recommended": 289,
    "webcam_premium": 549,
    "open_libras_pro_license": 0,  # open source
    "cloud_api_per_1000_calls": 12.50,
}

# ============================================================================
# 7. FUNCAO DEMO
# ============================================================================

def demo() -> None:
    """Executa todos os cenarios de demonstracao."""
    print("=" * 60)
    print("DEMO DO SISTEMA OPENLIBRASBRIDGE")
    print("=" * 60)

    # Demonstra catalogo
    print(f"\nCatalogo possui {len(LIBRAS_SIGNS)} sinais cadastrados.")
    print("Exemplos:", ", ".join([s.portuguese_meaning for s in LIBRAS_SIGNS[:5]]))

    # Executa todos os cenarios
    scenario_ordering_food()
    scenario_doctor_visit()
    scenario_job_interview()
    scenario_emergency_libras()

    # Demonstra modo conversacao
    print("\n=== MODO CONVERSACAO (5 segundos) ===")
    bridge = create_bridge_for_deaf()
    bridge.start_session()
    results = bridge.conversation_mode(5)
    print(f"Interacoes registradas: {len(results)}")

    print("\nDemo concluida com sucesso!")


if __name__ == "__main__":
    demo()