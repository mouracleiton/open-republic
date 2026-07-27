#!/usr/bin/env python3
"""
OpenInclusiveEducation -- Plataforma de Educacao Adaptativa para TODAS as Deficiencias
======================================================================================
"Cada cerebro aprende de forma diferente. A plataforma se adapta ao cerebro, nao o contrario.
Uma crianca autista aprende de forma distinta de uma crianca com Sindrome de Down ou TDAH.
Um cego usa audio e braille. Um surdo usa video legendado e visual. Um dislexico usa fontes especiais.
Um com discalculia usa blocos e manipulativos. Um com atraso cognitivo usa historias sociais e ritmo lento.

A plataforma nao foi feita para o aluno padrao -- porque aluno padrao nao existe.
Cada cerebro e diferente. Cada sensorio e diferente. Cada ritmo e diferente.
A EDUCACAO se ADAPTA ao aprendiz, nao o contrario.

ZERO barreira de entrada. MAXIMA inclusao. TODA deficiencia coberta.

Integrado com:
- OpenFocusGuard (protege contra sobrecarga sensorial)
- OpenSilencePolicy (silencio por padrao, som so quando solicitado)
- OpenAbsence (respeita pausas e regulacao emocional)
- OpenBodilyAutonomy (a crianca controla seu corpo/tempo)
- OpenHumanAmplification (IA como instrumento de apoio, nao substituto)

DEFICIENCIAS COBERTAS NA EDUCACAO:
1. VISUAL (cegueira, baixa visao)
2. AUDITIVA (surdez, baixa audicao)
3. AUTISMO (espectro, hipersensibilidade, rotina, sobrecarga)
4. SINDROME DE DOWN (aprendizado lento, memoria visual forte, repeticao)
5. TDAH (atencao curta, hiperatividade, necessidade de movimento)
6. DISLEXIA (leitura, processamento fonologico)
7. DISCALCULIA (numeros, quantidade, tempo)
8. ATRASO COGNITIVO (ritmo muito lento, conceitos basicos)
9. MULTIPLA (combinacoes)
10. NEUROTIPICO (controle para comparacao)

PRINCIPIO CHAVE: A deficiencia nao esta na crianca -- esta no AMBIENTE.
Se a plataforma nao serve para uma crianca, a plataforma que esta quebrada.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
import random
import time


# ============================================================================
# 1. PERFIS DE APRENDIZAGEM
# ============================================================================

class LearnerProfileType(Enum):
    """Tipos de perfil de aprendizagem adaptados a deficiencias."""
    BLIND = "cego"                      # cegueira total ou parcial
    DEAF = "surdo"                      # surdez total ou parcial
    AUTISM_SPECTRUM = "espectro_autista" # TEA, rotina, sensorial
    DOWN_SYNDROME = "sindrome_down"     # Down, repeticao, visual
    TDAH = "tdah"                       # atencao, movimento
    DYSLEXIA = "dislexia"               # leitura, fonologia
    DYSCALCULIA = "discalculia"         # numeros, quantidade
    COGNITIVE_DELAY = "atraso_cognitivo" # ritmo lento, conceitos basicos
    MULTIPLE = "multipla"               # combinacao
    NEUROTYPICAL = "neurotipico"        # controle


class ContentType(Enum):
    """Tipos de conteudo adaptados."""
    TEXT = "texto"
    AUDIO = "audio"
    VIDEO = "video"
    INTERACTIVE_GAME = "jogo_interativo"
    BLOCKS_VISUAL = "blocos_visuais"
    FLOWCHART = "fluxograma"
    HANDS_ON = "mao_na_massa"
    SOCIAL_STORY = "historia_social"
    MINDFULNESS = "mindfulness"
    QUIZ = "quiz"


class DifficultyAdaptation(Enum):
    """Adaptacao de dificuldade."""
    EASIER = "mais_facil"
    SAME = "mesmo"
    HARDER = "mais_dificil"
    CUSTOM = "personalizado"


class LearningPace(Enum):
    """Ritmo de aprendizagem."""
    VERY_SLOW = "muito_lento"
    SLOW = "lento"
    MEDIUM = "medio"
    FAST = "rapido"
    VERY_FAST = "muito_rapido"


class FeedbackStyle(Enum):
    """Estilo de feedback emocional."""
    GENTLE = "suave"
    ENCOURAGING = "encorajador"
    DIRECT = "direto"
    CELEBRATORY = "celebratorio"
    MINIMAL = "minimo"


class SensoryEnvironment(Enum):
    """Ambiente sensorial necessario."""
    CALM = "calmo"
    STIMULATING = "estimulante"
    MINIMAL = "minimo"
    STRUCTURED = "estruturado"
    FREE_EXPLORATION = "livre_exploracao"


class EmotionState(Enum):
    """Estados emocionais durante a aprendizagem."""
    ENGAGED = "engajado"
    FRUSTRATED = "frustrado"
    BORED = "entediado"
    ANXIOUS = "ansioso"
    CONFIDENT = "confiante"
    OVERWHELMED = "sobrecarregado"
    EXCITED = "excitado"


# ============================================================================
# 2. UNIDADES DE APRENDIZAGEM (CURRICULO)
# ============================================================================

@dataclass
class LearningUnit:
    """Unidade de aprendizagem com adaptacoes."""
    unit_id: str
    title: str
    subject: str  # "literacy", "numeracy", "social", "motor"
    content_types: List[ContentType]
    difficulty: int  # 1-10
    estimated_minutes: int
    prerequisites: List[str] = field(default_factory=list)
    accessibility_features: List[str] = field(default_factory=list)
    description: str = ""

    def supports_profile(self, profile_type: LearnerProfileType) -> bool:
        """Verifica se a unidade tem suporte para o perfil."""
        if profile_type == LearnerProfileType.BLIND:
            return ContentType.AUDIO in self.content_types or "audio" in self.accessibility_features
        if profile_type == LearnerProfileType.DEAF:
            return ContentType.VIDEO in self.content_types or "legendas" in self.accessibility_features
        if profile_type == LearnerProfileType.AUTISM_SPECTRUM:
            return ContentType.SOCIAL_STORY in self.content_types or ContentType.MINDFULNESS in self.content_types
        return True


# ============================================================================
# 3. PERFIL DO APRENDIZ
# ============================================================================

@dataclass
class LearnerProfile:
    """Perfil completo do aprendiz com adaptacoes."""
    learner_id: str
    name: str
    profile_type: LearnerProfileType
    pace: LearningPace
    preferred_content_types: List[ContentType]
    sensory_needs: SensoryEnvironment
    feedback_preference: FeedbackStyle
    strengths: List[str] = field(default_factory=list)
    challenges: List[str] = field(default_factory=list)
    current_level: int = 1
    motivation_triggers: List[str] = field(default_factory=list)
    sensory_triggers: List[str] = field(default_factory=list)

    def needs_calming(self) -> bool:
        return self.sensory_needs in (SensoryEnvironment.CALM, SensoryEnvironment.MINIMAL)

    def needs_structure(self) -> bool:
        return self.profile_type in (LearnerProfileType.AUTISM_SPECTRUM, LearnerProfileType.DOWN_SYNDROME)


# ============================================================================
# 4. CAMINHO ADAPTATIVO
# ============================================================================

@dataclass
class AdaptivePath:
    """Caminho de aprendizagem personalizado."""
    learner_id: str
    units_completed: List[str] = field(default_factory=list)
    current_unit: Optional[str] = None
    next_units: List[str] = field(default_factory=list)
    difficulty_trend: List[int] = field(default_factory=list)
    engagement_score: float = 0.8
    time_spent_min: int = 0


# ============================================================================
# 5. REGISTRO DE PROGRESSO
# ============================================================================

@dataclass
class ProgressRecord:
    """Registro de progresso em uma unidade."""
    unit_id: str
    score: float
    time_spent_min: int
    attempts: int
    hints_used: int
    emotion_during: EmotionState
    mastery_level: float  # 0.0 - 1.0


# ============================================================================
# 6. CURRICULO BASE (20+ UNIDADES)
# ============================================================================

CURRICULUM: List[LearningUnit] = [
    LearningUnit("lit_001", "Sons das Letras", "literacy", [ContentType.AUDIO, ContentType.INTERACTIVE_GAME], 1, 15, [], ["audio", "legendas"], "Identificar sons iniciais"),
    LearningUnit("lit_002", "Letras com Blocos", "literacy", [ContentType.BLOCKS_VISUAL, ContentType.HANDS_ON], 1, 20, ["lit_001"], ["tactil", "cores"], "Formar palavras simples"),
    LearningUnit("lit_003", "Leitura com Imagens", "literacy", [ContentType.VIDEO, ContentType.SOCIAL_STORY], 2, 18, ["lit_002"], ["legendas", "imagens"], "Leitura guiada por imagens"),
    LearningUnit("lit_004", "Historias Sociais", "literacy", [ContentType.SOCIAL_STORY, ContentType.AUDIO], 2, 12, ["lit_003"], ["rotina", "emocoes"], "Compreensao de historias"),
    LearningUnit("num_001", "Contar com Dedos", "numeracy", [ContentType.HANDS_ON, ContentType.BLOCKS_VISUAL], 1, 15, [], ["tactil"], "Contagem 1-5"),
    LearningUnit("num_002", "Numeros em Audio", "numeracy", [ContentType.AUDIO, ContentType.INTERACTIVE_GAME], 1, 12, ["num_001"], ["audio"], "Reconhecer numeros falados"),
    LearningUnit("num_003", "Quantidade Visual", "numeracy", [ContentType.BLOCKS_VISUAL, ContentType.FLOWCHART], 2, 18, ["num_002"], ["cores", "tamanho"], "Comparar quantidades"),
    LearningUnit("num_004", "Adicao com Blocos", "numeracy", [ContentType.HANDS_ON, ContentType.INTERACTIVE_GAME], 3, 20, ["num_003"], ["manipulativos"], "Adicao simples"),
    LearningUnit("soc_001", "Emocoes Basicas", "social", [ContentType.SOCIAL_STORY, ContentType.VIDEO], 1, 10, [], ["legendas", "imagens"], "Identificar alegria/tristeza"),
    LearningUnit("soc_002", "Turnos e Compartilhar", "social", [ContentType.INTERACTIVE_GAME, ContentType.SOCIAL_STORY], 2, 15, ["soc_001"], ["rotina"], "Aprender a esperar"),
    LearningUnit("mot_001", "Coordenacao Visual", "motor", [ContentType.HANDS_ON, ContentType.BLOCKS_VISUAL], 1, 12, [], ["tactil"], "Pegar e soltar"),
    LearningUnit("mot_002", "Movimento Ritmado", "motor", [ContentType.AUDIO, ContentType.MINDFULNESS], 1, 10, ["mot_001"], ["musica"], "Bater palmas no ritmo"),
    LearningUnit("reg_001", "Respiracao Calma", "regulation", [ContentType.MINDFULNESS, ContentType.AUDIO], 1, 8, [], ["calmo"], "Respirar para acalmar"),
    LearningUnit("reg_002", "Pausa Consciente", "regulation", [ContentType.MINDFULNESS, ContentType.SOCIAL_STORY], 2, 10, ["reg_001"], ["rotina"], "Pedir pausa quando sobrecarregado"),
    LearningUnit("lit_005", "Leitura com Fonte Especial", "literacy", [ContentType.TEXT, ContentType.AUDIO], 3, 15, ["lit_004"], ["fonte_dislexia"], "Leitura fluente"),
    LearningUnit("num_005", "Subtracao com Objetos", "numeracy", [ContentType.HANDS_ON, ContentType.BLOCKS_VISUAL], 3, 18, ["num_004"], ["manipulativos"], "Subtracao basica"),
    LearningUnit("soc_003", "Amizade e Empatia", "social", [ContentType.SOCIAL_STORY, ContentType.VIDEO], 3, 15, ["soc_002"], ["legendas"], "Entender sentimentos alheios"),
    LearningUnit("num_006", "Tempo e Relogio", "numeracy", [ContentType.FLOWCHART, ContentType.INTERACTIVE_GAME], 4, 20, ["num_005"], ["visual"], "Ler horas simples"),
    LearningUnit("lit_006", "Escrita com Voz", "literacy", [ContentType.AUDIO, ContentType.INTERACTIVE_GAME], 4, 15, ["lit_005"], ["voz"], "Escrever ditando"),
    LearningUnit("reg_003", "Rotina Visual", "regulation", [ContentType.FLOWCHART, ContentType.SOCIAL_STORY], 2, 12, ["reg_002"], ["visual"], "Seguir rotina diaria"),
]


# ============================================================================
# 7. MOTOR DE CURRICULO
# ============================================================================

class CurriculumEngine:
    """Gerencia o curriculo e unidades de aprendizagem."""

    def __init__(self):
        self.units = {u.unit_id: u for u in CURRICULUM}

    def get_next_unit(self, completed: List[str], profile: LearnerProfile) -> Optional[LearningUnit]:
        """Retorna proxima unidade adequada ao perfil."""
        for unit in CURRICULUM:
            if unit.unit_id not in completed and unit.supports_profile(profile.profile_type):
                if all(prereq in completed for prereq in unit.prerequisites):
                    return unit
        return None

    def get_prerequisites(self, unit_id: str) -> List[str]:
        unit = self.units.get(unit_id)
        return unit.prerequisites if unit else []

    def check_mastery(self, records: List[ProgressRecord], unit_id: str) -> bool:
        unit_records = [r for r in records if r.unit_id == unit_id]
        if not unit_records:
            return False
        avg_mastery = sum(r.mastery_level for r in unit_records) / len(unit_records)
        return avg_mastery >= 0.8


# ============================================================================
# 8. MOTOR DE ADAPTACAO
# ============================================================================

class AdaptationEngine:
    """Adapta conteudo ao perfil do aprendiz."""

    def adapt_content(self, unit: LearningUnit, profile: LearnerProfile) -> Dict[str, Any]:
        """Adapta uma unidade ao perfil."""
        content = {
            "unit": unit.title,
            "primary_type": profile.preferred_content_types[0].value if profile.preferred_content_types else "texto",
            "pace": profile.pace.value,
            "sensory": profile.sensory_needs.value,
            "feedback": profile.feedback_preference.value,
        }
        if profile.profile_type == LearnerProfileType.BLIND:
            content["primary_type"] = ContentType.AUDIO.value
            content["accessibility"] = ["audio", "braille"]
        elif profile.profile_type == LearnerProfileType.AUTISM_SPECTRUM:
            content["primary_type"] = ContentType.SOCIAL_STORY.value
            content["environment"] = "calmo"
        return content

    def adjust_difficulty(self, current: int, adaptation: DifficultyAdaptation) -> int:
        if adaptation == DifficultyAdaptation.EASIER:
            return max(1, current - 1)
        if adaptation == DifficultyAdaptation.HARDER:
            return min(10, current + 1)
        return current

    def select_content_type(self, profile: LearnerProfile) -> ContentType:
        return profile.preferred_content_types[0] if profile.preferred_content_types else ContentType.TEXT

    def modify_pace(self, profile: LearnerProfile, emotion: EmotionState) -> LearningPace:
        if emotion in (EmotionState.FRUSTRATED, EmotionState.OVERWHELMED):
            return LearningPace.VERY_SLOW
        if emotion == EmotionState.BORED:
            return LearningPace.FAST
        return profile.pace


# ============================================================================
# 9. DETECTOR DE EMOCOES
# ============================================================================

class EmotionDetector:
    """Detecta emocoes via padroes (camera, mouse, tempo)."""

    def detect_frustration(self, time_on_task: int, attempts: int, hints: int) -> bool:
        return attempts > 4 or (time_on_task > 25 and hints > 3)

    def detect_engagement(self, time_on_task: int, score: float) -> bool:
        return time_on_task > 8 and score > 0.6

    def recommend_break(self, emotion: EmotionState) -> bool:
        return emotion in (EmotionState.FRUSTRATED, EmotionState.OVERWHELMED, EmotionState.ANXIOUS)


# ============================================================================
# 10. RASTREADOR DE PROGRESSO
# ============================================================================

class ProgressTracker:
    """Registra e analisa progresso."""

    def __init__(self):
        self.records: List[ProgressRecord] = []

    def record_progress(self, record: ProgressRecord) -> None:
        self.records.append(record)

    def get_report(self, learner_id: str) -> Dict[str, Any]:
        if not self.records:
            return {"message": "Sem registros ainda"}
        avg_score = sum(r.score for r in self.records) / len(self.records)
        total_time = sum(r.time_spent_min for r in self.records)
        struggles = self.identify_struggles()
        return {
            "learner": learner_id,
            "media_score": round(avg_score, 2),
            "tempo_total_min": total_time,
            "unidades_tentadas": len(self.records),
            "dificuldades": struggles,
        }

    def identify_struggles(self) -> List[str]:
        struggles = []
        for r in self.records:
            if r.mastery_level < 0.6 and r.attempts > 3:
                struggles.append(r.unit_id)
        return struggles


# ============================================================================
# 11. PLATAFORMA PRINCIPAL
# ============================================================================

class InclusiveEducationPlatform:
    """Orquestrador principal da educacao inclusiva."""

    def __init__(self, profile: LearnerProfile):
        self.profile = profile
        self.curriculum = CurriculumEngine()
        self.adaptation = AdaptationEngine()
        self.emotion = EmotionDetector()
        self.tracker = ProgressTracker()
        self.path = AdaptivePath(learner_id=profile.learner_id)
        self.current_lesson: Optional[LearningUnit] = None

    def start_lesson(self) -> Dict[str, Any]:
        unit = self.curriculum.get_next_unit(self.path.units_completed, self.profile)
        if not unit:
            return {"status": "curriculo_completo"}
        self.current_lesson = unit
        self.path.current_unit = unit.unit_id
        adapted = self.adaptation.adapt_content(unit, self.profile)
        return {
            "lesson": unit.title,
            "adapted": adapted,
            "estimated_minutes": unit.estimated_minutes,
            "sensory_environment": self.profile.sensory_needs.value,
        }

    def next_activity(self) -> Optional[Dict[str, Any]]:
        if not self.current_lesson:
            return None
        content_type = self.adaptation.select_content_type(self.profile)
        return {
            "activity": content_type.value,
            "unit": self.current_lesson.title,
            "difficulty": self.current_lesson.difficulty,
        }

    def provide_feedback(self, emotion: EmotionState) -> str:
        if emotion == EmotionState.FRUSTRATED:
            return "Vamos respirar juntos. Voce esta indo bem. Quer tentar de outro jeito?"
        if emotion == EmotionState.CONFIDENT:
            return "Que otimo! Voce esta dominando isso!"
        return "Continue assim. Estou aqui com voce."

    def check_in(self, emotion: EmotionState) -> Dict[str, Any]:
        needs_break = self.emotion.recommend_break(emotion)
        new_pace = self.adaptation.modify_pace(self.profile, emotion)
        return {
            "emotion": emotion.value,
            "recommend_break": needs_break,
            "new_pace": new_pace.value,
            "message": self.provide_feedback(emotion),
        }

    def generate_report(self) -> Dict[str, Any]:
        return self.tracker.get_report(self.profile.learner_id)


# ============================================================================
# 12. FABRICAS DE PERFIS
# ============================================================================

def create_learner_autism(name: str = "Crianca Autista") -> LearnerProfile:
    return LearnerProfile(
        learner_id="autism_001",
        name=name,
        profile_type=LearnerProfileType.AUTISM_SPECTRUM,
        pace=LearningPace.SLOW,
        preferred_content_types=[ContentType.SOCIAL_STORY, ContentType.MINDFULNESS, ContentType.BLOCKS_VISUAL],
        sensory_needs=SensoryEnvironment.CALM,
        feedback_preference=FeedbackStyle.GENTLE,
        strengths=["memoria_visual", "rotina", "atencao_detalhes"],
        challenges=["mudanca", "sobrecarga_sensorial", "comunicacao_social"],
        motivation_triggers=["rotina", "elogio_suave", "previsibilidade"],
        sensory_triggers=["barulho_alto", "luzes_piscando", "toque_inesperado"],
    )


def create_learner_down(name: str = "Crianca Down") -> LearnerProfile:
    return LearnerProfile(
        learner_id="down_001",
        name=name,
        profile_type=LearnerProfileType.DOWN_SYNDROME,
        pace=LearningPace.VERY_SLOW,
        preferred_content_types=[ContentType.HANDS_ON, ContentType.BLOCKS_VISUAL, ContentType.SOCIAL_STORY],
        sensory_needs=SensoryEnvironment.STRUCTURED,
        feedback_preference=FeedbackStyle.CELEBRATORY,
        strengths=["afeto", "memoria_visual", "persistência"],
        challenges=["linguagem", "abstracao", "memoria_curta"],
        motivation_triggers=["musica", "danca", "carinho", "repeticao"],
        sensory_triggers=["pressa", "critica", "mudanca_rapida"],
    )


def create_learner_adhd(name: str = "Crianca TDAH") -> LearnerProfile:
    return LearnerProfile(
        learner_id="adhd_001",
        name=name,
        profile_type=LearnerProfileType.TDAH,
        pace=LearningPace.FAST,
        preferred_content_types=[ContentType.INTERACTIVE_GAME, ContentType.HANDS_ON, ContentType.VIDEO],
        sensory_needs=SensoryEnvironment.STIMULATING,
        feedback_preference=FeedbackStyle.ENERGIZING if hasattr(FeedbackStyle, 'ENERGIZING') else FeedbackStyle.ENCOURAGING,
        strengths=["energia", "criatividade", "hiperfoco_em_interesses"],
        challenges=["atencao_sustentada", "impulsividade", "esperar"],
        motivation_triggers=["jogo", "movimento", "competicao", "novidade"],
        sensory_triggers=["tarefa_repetitiva", "espera_longa", "silencio_absoluto"],
    )


def create_learner_dyslexia(name: str = "Crianca Dislexica") -> LearnerProfile:
    return LearnerProfile(
        learner_id="dyslexia_001",
        name=name,
        profile_type=LearnerProfileType.DYSLEXIA,
        pace=LearningPace.MEDIUM,
        preferred_content_types=[ContentType.AUDIO, ContentType.BLOCKS_VISUAL, ContentType.INTERACTIVE_GAME],
        sensory_needs=SensoryEnvironment.STRUCTURED,
        feedback_preference=FeedbackStyle.ENCOURAGING,
        strengths=["pensamento_espacial", "resolucao_problemas", "criatividade"],
        challenges=["leitura", "ortografia", "processamento_fonologico"],
        motivation_triggers=["jogo", "arte", "historia", "tecnologia"],
        sensory_triggers=["texto_puro", "tempo_limitado", "leitura_em_voz_alta"],
    )


def create_learner_blind(name: str = "Crianca Cega") -> LearnerProfile:
    return LearnerProfile(
        learner_id="blind_001",
        name=name,
        profile_type=LearnerProfileType.BLIND,
        pace=LearningPace.MEDIUM,
        preferred_content_types=[ContentType.AUDIO, ContentType.HANDS_ON, ContentType.INTERACTIVE_GAME],
        sensory_needs=SensoryEnvironment.STRUCTURED,
        feedback_preference=FeedbackStyle.DIRECT,
        strengths=["audição", "memoria", "tato"],
        challenges=["conceitos_visuais", "orientacao_espacial", "acesso_escrito"],
        motivation_triggers=["audio", "tato", "voz", "exploracao"],
        sensory_triggers=["silencio_total", "mudanca_ambiente"],
    )


def create_learner_deaf(name: str = "Crianca Surda") -> LearnerProfile:
    return LearnerProfile(
        learner_id="deaf_001",
        name=name,
        profile_type=LearnerProfileType.DEAF,
        pace=LearningPace.MEDIUM,
        preferred_content_types=[ContentType.VIDEO, ContentType.BLOCKS_VISUAL, ContentType.HANDS_ON],
        sensory_needs=SensoryEnvironment.STRUCTURED,
        feedback_preference=FeedbackStyle.DIRECT,
        strengths=["visao", "linguagem_sinais", "atencao_visual"],
        challenges=["linguagem_oral", "acesso_audio", "comunicacao_ouvintes"],
        motivation_triggers=["video", "sinais", "visual", "demonstracao"],
        sensory_triggers=["som_alto", "ambiente_ruidoso"],
    )


# ============================================================================
# 13. CENARIOS DE DEMONSTRACAO
# ============================================================================

def scenario_autism_learns_math():
    print("\n=== CENARIO: Crianca Autista Aprendendo Matematica ===")
    learner = create_learner_autism("Alex Autista")
    platform = InclusiveEducationPlatform(learner)
    lesson = platform.start_lesson()
    print(f"Licao inicial: {lesson['lesson']}")
    print(f"Adaptacao: {lesson['adapted']}")
    platform.check_in(EmotionState.OVERWHELMED)
    platform.tracker.record_progress(ProgressRecord("num_001", 0.75, 22, 3, 2, EmotionState.ENGAGED, 0.8))
    print(platform.generate_report())


def scenario_down_learns_reading():
    print("\n=== CENARIO: Crianca com Down Aprendendo Leitura ===")
    learner = create_learner_down("Bella Down")
    platform = InclusiveEducationPlatform(learner)
    lesson = platform.start_lesson()
    print(f"Licao inicial: {lesson['lesson']}")
    platform.check_in(EmotionState.CONFIDENT)
    platform.tracker.record_progress(ProgressRecord("lit_001", 0.9, 18, 2, 1, EmotionState.EXCITED, 0.85))
    print(platform.generate_report())


def scenario_adhd_learns_history():
    print("\n=== CENARIO: Crianca com TDAH Aprendendo Historia ===")
    learner = create_learner_adhd("Theo TDAH")
    platform = InclusiveEducationPlatform(learner)
    lesson = platform.start_lesson()
    print(f"Licao inicial: {lesson['lesson']}")
    platform.check_in(EmotionState.BORED)
    print("Adaptando ritmo para mais rapido e jogo interativo...")


def scenario_blind_learns_programming():
    print("\n=== CENARIO: Crianca Cega Aprendendo Programacao ===")
    learner = create_learner_blind("Luna Cega")
    platform = InclusiveEducationPlatform(learner)
    lesson = platform.start_lesson()
    print(f"Licao inicial: {lesson['lesson']}")
    print("Usando audio e blocos tacteis para introduzir logica...")


# ============================================================================
# 14. DEMONSTRACAO COMPLETA
# ============================================================================

def demo():
    print("=" * 70)
    print("OpenInclusiveEducation -- Educacao Adaptativa para TODAS as Deficiencias")
    print("=" * 70)

    learners = {
        "Autista": create_learner_autism(),
        "Sindrome de Down": create_learner_down(),
        "TDAH": create_learner_adhd(),
        "Dislexia": create_learner_dyslexia(),
        "Cego": create_learner_blind(),
        "Surdo": create_learner_deaf(),
    }

    for label, learner in learners.items():
        print(f"\n{'─' * 50}")
        print(f"PERFIL: {label} -- {learner.name}")
        print(f"{'─' * 50}")
        platform = InclusiveEducationPlatform(learner)
        lesson = platform.start_lesson()
        print(f"  Licao:      {lesson.get('lesson', 'N/A')}")
        print(f"  Ritmo:      {learner.pace.value}")
        print(f"  Sensorial:  {learner.sensory_needs.value}")
        print(f"  Feedback:   {learner.feedback_preference.value}")
        print(f"  Preferido:  {[c.value for c in learner.preferred_content_types][:2]}")

    print("\n" + "=" * 70)
    print("EXECUTANDO CENARIOS")
    print("=" * 70)
    scenario_autism_learns_math()
    scenario_down_learns_reading()
    scenario_adhd_learns_history()
    scenario_blind_learns_programming()

    print("\n" + "=" * 70)
    print("CURRICULO DISPONIVEL")
    print("=" * 70)
    for unit in CURRICULUM[:8]:
        print(f"  {unit.unit_id}: {unit.title} ({unit.subject}) -- {unit.difficulty}")

    print(f"\nTotal de unidades: {len(CURRICULUM)}")
    print(f"Total de perfis: {len(LearnerProfileType)}")
    print(f"Total de tipos de conteudo: {len(ContentType)}")
    print("\nEDUCACAO INCLUSIVA. ZERO BARREIRA. CADA CEREBRO IMPORTA.")


if __name__ == "__main__":
    demo()
