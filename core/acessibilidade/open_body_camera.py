#!/usr/bin/env python3
"""
OpenBodyCamera -- Smartphone como Camera Corporal + Fone Bluetooth = Olhos do Cego (Atualizado 2025)
===================================================================================
"O cego nao precisa de olhos. Precisa de INFORMACAO.
O smartphone na camisa capta o mundo.
O fone no ouvido TRADUZ o mundo em voz.
O cego VE com a camera. OUVE com o fone.
NADA o para. NINGUEM o limita.

A camera corporal e um PAR DE OLHOS emprestado.
O fone bluetooth e um PAR DE OUVIDOS que falam.
Juntos, sao o CORPO EXTENDIDO do cego na rua."

COMO FUNCIONA:
1. Smartphone preso no peito (clip de camisa/bolsinho) - mounts 2025 ~R$45-180
2. Camera traseira aponta para frente (48-50MP em mid-range 2025)
3. IA processa o video em tempo real (20-45 fps com otimização)
4. Fone bluetooth recebe descricao por voz
5.Usuario anda COM INFORMACAO

Modelos de Visão Atualizados 2024/2025:
- YOLOv11 / YOLOv10 / YOLOv9 (Ultralytics) - detecção rápida de obstáculos/pessoas (CoreML/NNAPI/TFLite)
- LLaVA-1.6 (Mistral/Phi-3-Vision/Moondream2) - descrição multimodal de cenas completas
- SAM2 + Depth-Anything V2 para estimativa precisa de distância e segmentação
- EasyOCR/PaddleOCR + MediaPipe Face + InsightFace
- On-device: Apple Neural Engine (iPhone 15/16), Tensor G4 (Pixel), Snapdragon 8 Gen 3/4

NIVEIS DE VERBALIZACAO e modos mantidos.

INTEGRACAO COM OPENREPUBLIC:
- OpenTelefonista, OpenResilience, OpenHumanNet, republica-assistive.

Author: OpenRepublic Team (Cleiton + MING -- 50/50) - Atualizado 2025
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import deque
import time
import math


# ============================================================================
# 1. TIPOS DE MONTAGEM (Como o smartphone fica no corpo)
# ============================================================================

class MountPosition(Enum):
    CHEST = "peito"              # clipped na camisa, no peito -- padrao
    HEAD = "cabeca"              # bandana/oculos com smartphone
    SHOULDER = "ombro"           # alça de mochila
    NECK = "pescoco"             # pendurado no pescoco
    HAND = "mao"                 # na mao apontando
    POCKET_FACING_OUT = "bolso_frente"  # no bolso com camera pra fora
    ARMBAND = "braceaco"         # bracelete de braco


class CameraMode(Enum):
    CONTINUOUS = "continuo"           # descreve tudo o tempo todo
    ON_DEMAND = "sob_demanda"         # so quando usuario pede
    ALERT_ONLY = "so_alerta"          # so perigos
    NAVIGATION = "navegacao"          # co-piloto de rua
    READING = "leitura"               # modo OCR (ler texto)
    MONEY = "dinheiro"                # reconhecer cedulas
    COLOR = "cor"                     # identificar cores
    FACE = "rosto"                    # reconhecer pessoas
    SEARCH = "busca"                  # procurar objeto especifico
    MINIMAL = "minimal"               # tateando (hiper-minimal)


class VerbosityLevel(Enum):
    HIGH = "alto"           # descreve tudo em detalhe
    MEDIUM = "medio"        # descreve o essencial
    LOW = "baixo"           # so alertas e orientacao
    WHISPER = "sussurro"    # minimo possivel (1 palavra)


# ============================================================================
# 2. DETECCOES VISUAIS
# ============================================================================

class ObjectType(Enum):
    OBSTACLE = "obstaculo"
    PERSON = "pessoa"
    VEHICLE = "veiculo"
    ANIMAL = "animal"
    SIGN = "placa"
    DOOR = "porta"
    STAIRS = "escada"
    CROSSWALK = "faixa"
    TRAFFIC_LIGHT = "semaforo"
    TEXT = "texto"
    MONEY = "dinheiro"
    PRODUCT = "produto"
    FOOD = "comida"
    MEDICINE = "remedio"
    FURNITURE = "movel"
    TOOL = "ferramenta"
    NATURE = "natureza"


class DangerLevel(Enum):
    SAFE = "seguro"
    ATTENTION = "atencao"
    WARNING = "aviso"
    DANGER = "perigo"
    CRITICAL = "critico"


@dataclass
class Detection:
    """Uma deteccao da camera em tempo real."""
    object_type: ObjectType
    label: str                         # nome amigavel
    distance_m: float                  # distancia estimada
    direction: str                     # frente, esquerda, direita, baixo, alto
    danger: DangerLevel
    confidence: float                  # 0-1
    action: str = ""                   # o que o usuario deve fazer
    voice_description: str = ""        # descricao para TTS
    timestamp: float = field(default_factory=time.time)
    size: str = ""                     # pequeno, medio, grande
    moving: bool = False               # esta se movendo?
    approaching: bool = False          # vindo na direcao do usuario?


# ============================================================================
# 3. MOTOR DE VISAO COMPUTACIONAL (Atualizado 2025)
# ============================================================================

class VisionEngine:
    """
    Processa frames da camera e gera descricoes em tempo real (2025).
    Modelos de visão atualizados 2024/2025:
    - YOLOv11 / YOLOv10 / YOLOv9 (Ultralytics) - detecção rápida de objetos/obstáculos (on-device via CoreML/TFLite/NNAPI)
    - LLaVA-1.6-Mistral-7B ou Phi-3-Vision / Moondream2 - descrição de cena multimodal (via Ollama ou MLX no Apple Silicon)
    - Segment-Anything (SAM2) + Depth-Anything V2 para distância e máscaras
    - EasyOCR / PaddleOCR para texto; MediaPipe + InsightFace para rostos
    - On-device prioridade: Apple Neural Engine (ANE) ou Qualcomm AI Hub (Snapdragon 8 Gen 3/4)
    Aqui: simulacao realista do que a camera 've'. Integração real via OpenCV + ultralytics + transformers.
    """

    def __init__(self, mount: MountPosition = MountPosition.CHEST):
        self.mount = mount
        self.detections_history: deque = deque(maxlen=200)
        self.last_scene: str = ""
        self.frame_count: int = 0
        self.fps: float = 25.0  # atualizado para 2025
        self.processing_latency_ms: float = 35  # latencia melhorada com hardware 2025

    def process_frame(self, mode: CameraMode = CameraMode.CONTINUOUS) -> List[Detection]:
        """Processa um frame da camera."""
        self.frame_count += 1
        detections = []

        if mode == CameraMode.NAVIGATION:
            detections = self._scan_navigation()
        elif mode == CameraMode.READING:
            detections = self._scan_text()
        elif mode == CameraMode.MONEY:
            detections = self._scan_money()
        elif mode == CameraMode.COLOR:
            detections = self._scan_color()
        elif mode == CameraMode.FACE:
            detections = self._scan_faces()
        elif mode == CameraMode.SEARCH:
            detections = self._scan_search()
        else:
            detections = self._scan_continuous()

        for d in detections:
            self.detections_history.append(d)
        return detections

    def _scan_continuous(self) -> List[Detection]:
        """Modo continuo: descreve tudo ao redor."""
        return [
            Detection(
                ObjectType.PERSON, "Pessoa", 3.0, "frente",
                DangerLevel.SAFE, 0.92,
                action="Pessoa a 3 metros a frente.",
                voice_description="Pessoa a frente, 3 metros.",
                moving=True, approaching=False,
            ),
            Detection(
                ObjectType.OBSTACLE, "Poste", 5.0, "frente-esquerda",
                DangerLevel.ATTENTION, 0.88,
                action="Poste a 5 metros. Mantenha a direita.",
                voice_description="Poste a esquerda, 5 metros.",
            ),
            Detection(
                ObjectType.VEHICLE, "Carro estacionado", 2.5, "direita",
                DangerLevel.SAFE, 0.95,
                voice_description="Carro estacionado a direita.",
            ),
        ]

    def _scan_navigation(self) -> List[Detection]:
        """Modo navegacao: co-piloto de rua."""
        return [
            Detection(
                ObjectType.CROSSWALK, "Faixa de pedestre", 8.0, "frente",
                DangerLevel.SAFE, 0.90,
                action="Continue reto. Faixa de pedestre em 8 metros.",
                voice_description="Faixa de pedestre a frente, 8 metros. Continue reto.",
            ),
            Detection(
                ObjectType.TRAFFIC_LIGHT, "Semaforo", 8.0, "frente-alto",
                DangerLevel.SAFE, 0.97,
                action="Semaforo VERDE. Pode atravessar.",
                voice_description="Semaforo verde. Pode atravessar.",
            ),
            Detection(
                ObjectType.OBSTACLE, "Buraco na calcada", 4.0, "frente-baixo",
                DangerLevel.WARNING, 0.85,
                action="Buraco a 4 metros. Desvie para a esquerda.",
                voice_description="Atencao! Buraco na calcada, 4 metros. Desvie a esquerda.",
            ),
        ]

    def _scan_text(self) -> List[Detection]:
        """Modo leitura: OCR de textos do mundo."""
        return [
            Detection(
                ObjectType.TEXT, "Placa de estabelecimento", 5.0, "frente-alto",
                DangerLevel.SAFE, 0.91,
                voice_description="A placa diz: RESTAURANTE DO JOAO. Aberto das 11 as 22.",
            ),
            Detection(
                ObjectType.TEXT, "Cardapio", 3.0, "frente",
                DangerLevel.SAFE, 0.88,
                voice_description="O cardapio diz: Feijoada R$ 25. Suco R$ 8. Prato feito R$ 18.",
            ),
        ]

    def _scan_money(self) -> List[Detection]:
        """Modo dinheiro: reconhece cedulas e moedas."""
        return [
            Detection(
                ObjectType.MONEY, "Nota de R$ 50", 0.5, "frente",
                DangerLevel.SAFE, 0.96,
                voice_description="Nota de CINQUENTA REAIS. Cor marrom.",
            ),
        ]

    def _scan_color(self) -> List[Detection]:
        """Modo cor: identifica cores (daltonismo tambem)."""
        return [
            Detection(
                ObjectType.SIGN, "Sinal vermelho", 10.0, "frente-alto",
                DangerLevel.DANGER, 0.97,
                action="Semaforo VERMELHO. PARE.",
                voice_description="Semaforo VERMELHO. Pare.",
            ),
        ]

    def _scan_faces(self) -> List[Detection]:
        """Modo rosto: reconhece pessoas."""
        return [
            Detection(
                ObjectType.PERSON, "MING (esposa)", 2.0, "frente",
                DangerLevel.SAFE, 0.89,
                voice_description="MING esta a sua frente, 2 metros. Sorrindo.",
            ),
        ]

    def _scan_search(self) -> List[Detection]:
        """Modo busca: procura objeto especifico."""
        return [
            Detection(
                ObjectType.PRODUCT, "Chave", 1.5, "mesa",
                DangerLevel.SAFE, 0.82,
                voice_description="Encontrei a chave. Esta na mesa, a sua frente, 1 metro e meio.",
            ),
        ]

    def describe_scene(self, detections: List[Detection], verbosity: VerbosityLevel = VerbosityLevel.MEDIUM) -> str:
        """Gera descricao da cena para TTS."""
        if not detections:
            if verbosity == VerbosityLevel.WHISPER:
                return "Livre."
            return "Nada a frente. Caminho livre."

        # Ordenar por perigo primeiro, depois distancia
        sorted_dets = sorted(detections, key=lambda d: (
            -[1,2,3,4,5][list(DangerLevel).index(d.danger)],
            d.distance_m
        ))

        descriptions = []
        for d in sorted_dets:
            if verbosity == VerbosityLevel.HIGH:
                descriptions.append(d.voice_description)
            elif verbosity == VerbosityLevel.MEDIUM:
                # Encurtar se necessario
                desc = d.voice_description
                if len(desc) > 60:
                    desc = desc[:57] + "..."
                descriptions.append(desc)
            elif verbosity == VerbosityLevel.LOW:
                if d.danger in (DangerLevel.WARNING, DangerLevel.DANGER, DangerLevel.CRITICAL):
                    descriptions.append(d.voice_description)
            elif verbosity == VerbosityLevel.WHISPER:
                if d.danger in (DangerLevel.DANGER, DangerLevel.CRITICAL):
                    descriptions.append(d.action if d.action else d.label)

        if not descriptions:
            return "Livre."

        return ". ".join(descriptions) + "."


# ============================================================================
# 4. GERENCIADOR DE AUDIO BLUETOOTH
# ============================================================================

class AudioOutputManager:
    """
    Gerencia a saida de voz para o fone bluetooth.
    Prioriza alertas, corta descricoes redundantes, respeita silencio.
    """
    def __init__(self):
        self.connected: bool = True
        self.device_name: str = "Fone Bluetooth"
        self.battery_pct: float = 100.0
        self.volume: float = 0.7
        self.tts_rate: float = 1.5       # atualizado - cegos escutam rapido em 2025
        self.last_spoken: str = ""
        self.last_spoken_time: float = 0
        self.min_interval_s: float = 1.2  # intervalo reduzido com hardware melhor
        self.message_queue: deque = deque(maxlen=50)
        self.priority_queue: deque = deque(maxlen=20)
        self.total_messages: int = 0
        self.messages_spoken: int = 0
        self.messages_skipped: int = 0

    def speak(self, message: str, priority: DangerLevel = DangerLevel.SAFE) -> Dict[str, Any]:
        """Envia mensagem para o fone. Retorna se falou ou nao."""
        now = time.time()
        self.total_messages += 1

        # Alertas criticos sempre passam
        is_critical = priority in (DangerLevel.DANGER, DangerLevel.CRITICAL)

        # Evitar repetir a mesma coisa
        if message == self.last_spoken and not is_critical:
            if now - self.last_spoken_time < 5.0:
                self.messages_skipped += 1
                return {"spoken": False, "reason": "duplicada"}

        # Respeitar intervalo minimo (exceto criticos)
        if not is_critical and now - self.last_spoken_time < self.min_interval_s:
            self.message_queue.append(message)
            self.messages_skipped += 1
            return {"spoken": False, "reason": "intervalo"}

        if is_critical:
            self.priority_queue.appendleft(message)
        else:
            self.message_queue.append(message)

        self.last_spoken = message
        self.last_spoken_time = now
        self.messages_spoken += 1

        return {
            "spoken": True,
            "message": message,
            "priority": priority.value,
            "device": self.device_name,
            "volume": self.volume,
            "rate": self.tts_rate,
        }

    def process_queue(self) -> List[str]:
        """Processa fila de mensagens pendentes."""
        spoken = []
        now = time.time()
        if now - self.last_spoken_time >= self.min_interval_s:
            while self.priority_queue:
                msg = self.priority_queue.popleft()
                spoken.append(msg)
                self.last_spoken = msg
                self.last_spoken_time = now
                self.messages_spoken += 1
                break
            if not spoken and self.message_queue:
                msg = self.message_queue.popleft()
                spoken.append(msg)
                self.last_spoken = msg
                self.last_spoken_time = now
                self.messages_spoken += 1
        return spoken

    def status(self) -> Dict[str, Any]:
        return {
            "connected": self.connected,
            "device": self.device_name,
            "battery_pct": self.battery_pct,
            "volume": self.volume,
            "tts_rate": self.tts_rate,
            "queue_size": len(self.message_queue),
            "priority_queue_size": len(self.priority_queue),
            "total_messages": self.total_messages,
            "spoken": self.messages_spoken,
            "skipped": self.messages_skipped,
        }


# ============================================================================
# 5. NAVEGACAO POR VOZ (Co-piloto de rua)
# ============================================================================

class StreetNavigator:
    """
    Sistema de navegacao por voz para cego andando na rua.
    Combina GPS + camera + bussola para guiar passo a passo.
    """
    def __init__(self):
        self.destination: str = ""
        self.current_step: int = 0
        self.steps: List[Dict[str, str]] = []
        self.last_instruction: str = ""
        self.distance_remaining_m: float = 0
        self.eta_minutes: float = 0

    def set_destination(self, destination: str, steps: List[Dict[str, str]] = None) -> str:
        """Define destino e calcula rota."""
        self.destination = destination
        self.current_step = 0
        self.steps = steps or self._default_route(destination)
        self.distance_remaining_m = sum(s.get("distance_m", 100) for s in self.steps)
        self.eta_minutes = self.distance_remaining_m / 80  # ~80m/min a pe
        return f"Rota calculada para {destination}. {self.distance_remaining_m:.0f} metros. Aproximadamente {self.eta_minutes:.0f} minutos."

    def _default_route(self, destination: str) -> List[Dict[str, str]]:
        """Rota padrao simulada."""
        return [
            {"instruction": "Saida do predio. Vire a direita na calcada.", "distance_m": 50},
            {"instruction": "Continue reto por 200 metros na rua Augusta.", "distance_m": 200},
            {"instruction": "Atencao: buraco a frente. Desvie a esquerda.", "distance_m": 5, "warning": True},
            {"instruction": "Semaforo a frente. Aguarde se vermelho.", "distance_m": 30},
            {"instruction": "Atravesse a faixa. 15 passos.", "distance_m": 15},
            {"instruction": "Vire a direita na rua Paulista.", "distance_m": 10},
            {"instruction": f"Destino: {destination}. A esquerda, porta azul.", "distance_m": 50, "arrival": True},
        ]

    def next_instruction(self) -> str:
        """Proxima instrucao de navegacao."""
        if self.current_step >= len(self.steps):
            return "Voce chegou ao destino."

        step = self.steps[self.current_step]
        instruction = step["instruction"]
        self.last_instruction = instruction
        self.current_step += 1
        return instruction

    def detect_obstacle_ahead(self) -> Optional[str]:
        """Detecta obstaculo imediato e retorna aviso."""
        obstacles = [
            "Poste a frente, 3 metros. Desvie a direita.",
            "Buraco na calcada, 2 metros. Cuidado ao pisar.",
            "Carro mal estacionado bloqueando calcada. Desvie pela rua com cuidado.",
            "Pessoa parada a frente, 1 metro. 'Com licenca.'",
            "Degrau descendo, 1 metro. Passo menor.",
            "Raiz de arvore na calcada. Atencao ao pe esquerdo.",
        ]
        return obstacles[self.current_step % len(obstacles)] if self.current_step < len(obstacles) else None

    def arrival_message(self) -> str:
        """Mensagem de chegada."""
        return f"Voce chegou em {self.destination}. Esta a sua frente. Parabens!"


# ============================================================================
# 6. SISTEMA PRINCIPAL -- BodyCamera Controller
# ============================================================================

class BodyCameraController:
    """
    Orquestra smartphone-camera + fone-bluetooth para dar visao ao cego.

    Uso:
        cam = BodyCameraController(MountPosition.CHEST)
        cam.start()
        scene = cam.describe()          # ouve descricao da cena
        cam.navigate("padaria")         # co-piloto ate o destino
        cam.read_text()                 # OCR de placa/menu
        cam.identify_money()            # qual nota e essa?
    """

    def __init__(self, mount: MountPosition = MountPosition.CHEST,
                 verbosity: VerbosityLevel = VerbosityLevel.MEDIUM):
        self.mount = mount
        self.verbosity = verbosity
        self.vision = VisionEngine(mount)
        self.audio = AudioOutputManager()
        self.navigator = StreetNavigator()
        self.mode: CameraMode = CameraMode.CONTINUOUS
        self.active: bool = False
        self.session_start: float = 0
        self.total_descriptions: int = 0
        self.total_alerts: int = 0
        self.battery_pct: float = 100.0
        self.battery_drain_per_hour: float = 14.0  # melhorado com otimizacao 2025
        self.emergency_contact: str = ""

    def start(self) -> Dict[str, Any]:
        """Inicia a camera corporal."""
        self.active = True
        self.session_start = time.time()
        self.mode = CameraMode.CONTINUOUS
        greeting = self.audio.speak(
            f"Camera corporal ativa. Montagem: {self.mount.value}. "
            f"Modo: continuo. Fone conectado: {self.audio.device_name}. "
            f"Estou vendo por voce. (YOLOv11 + LLaVA 2025)",
            DangerLevel.SAFE
        )
        return {
            "active": True,
            "mount": self.mount.value,
            "mode": self.mode.value,
            "audio": self.audio.status(),
            "greeting": greeting,
        }

    def stop(self) -> Dict[str, Any]:
        """Para a camera."""
        duration = time.time() - self.session_start if self.session_start else 0
        self.active = False
        self.audio.speak("Camera desligada. Ate logo.", DangerLevel.SAFE)
        return {
            "active": False,
            "session_duration_min": duration / 60,
            "total_descriptions": self.total_descriptions,
            "total_alerts": self.total_alerts,
        }

    def describe(self) -> str:
        """Descreve a cena atual para o usuario."""
        if not self.active:
            return "Camera desligada."
        detections = self.vision.process_frame(self.mode)
        description = self.vision.describe_scene(detections, self.verbosity)
        result = self.audio.speak(description, DangerLevel.SAFE)
        self.total_descriptions += 1
        return description

    def describe_continuous(self, frames: int = 5, interval_s: float = 1.5) -> List[str]:
        """Simula descricao continua por N frames."""
        descriptions = []
        for _ in range(frames):
            desc = self.describe()
            descriptions.append(desc)
            time.sleep(interval_s)  # simulacao
        return descriptions

    def navigate(self, destination: str) -> str:
        """Inicia co-piloto de rua ate o destino."""
        self.mode = CameraMode.NAVIGATION
        route_msg = self.navigator.set_destination(destination)
        self.audio.speak(route_msg, DangerLevel.SAFE)
        first_step = self.navigator.next_instruction()
        self.audio.speak(first_step, DangerLevel.ATTENTION)
        return f"{route_msg}\n{first_step}"

    def navigate_step(self) -> str:
        """Proxima instrucao de navegacao."""
        instruction = self.navigator.next_instruction()
        self.audio.speak(instruction, DangerLevel.ATTENTION)

        # Verificar obstaculo
        obstacle = self.navigator.detect_obstacle_ahead()
        if obstacle:
            self.audio.speak(obstacle, DangerLevel.WARNING)
            self.total_alerts += 1
            return f"{instruction}\nALERTA: {obstacle}"
        return instruction

    def read_text(self) -> str:
        """Modo leitura: OCR de textos."""
        self.mode = CameraMode.READING
        detections = self.vision.process_frame(CameraMode.READING)
        texts = [d.voice_description for d in detections if d.object_type == ObjectType.TEXT]
        result = " ".join(texts) if texts else "Nao encontrei texto legivel."
        self.audio.speak(result, DangerLevel.SAFE)
        self.total_descriptions += 1
        return result

    def identify_money(self) -> str:
        """Modo dinheiro: reconhece cedula."""
        self.mode = CameraMode.MONEY
        detections = self.vision.process_frame(CameraMode.MONEY)
        money = [d.voice_description for d in detections if d.object_type == ObjectType.MONEY]
        result = money[0] if money else "Nao reconheci nenhuma cedula."
        self.audio.speak(result, DangerLevel.SAFE)
        return result

    def identify_color(self) -> str:
        """Modo cor: identifica cor a frente."""
        self.mode = CameraMode.COLOR
        detections = self.vision.process_frame(CameraMode.COLOR)
        colors = [d.voice_description for d in detections]
        result = colors[0] if colors else "Nao consegui identificar a cor."
        self.audio.speak(result, DangerLevel.SAFE)
        return result

    def recognize_face(self) -> str:
        """Modo rosto: quem esta a frente."""
        self.mode = CameraMode.FACE
        detections = self.vision.process_frame(CameraMode.FACE)
        faces = [d.voice_description for d in detections if d.object_type == ObjectType.PERSON]
        result = faces[0] if faces else "Nao reconheci ninguem a frente."
        self.audio.speak(result, DangerLevel.SAFE)
        return result

    def search_object(self, object_name: str = "") -> str:
        """Modo busca: procura objeto especifico."""
        self.mode = CameraMode.SEARCH
        detections = self.vision.process_frame(CameraMode.SEARCH)
        found = [d.voice_description for d in detections]
        if found:
            result = found[0]
        else:
            result = f"Nao encontrei {object_name}. Aponte a camera para outra direcao."
        self.audio.speak(result, DangerLevel.SAFE)
        return result

    def alert_emergency(self, description: str = "Situacao de emergencia") -> str:
        """Alerta de emergencia."""
        self.total_alerts += 1
        msg = f"EMERGENCIA. {description}. Vou avisar seu contato."
        self.audio.speak(msg, DangerLevel.CRITICAL)
        return msg

    def check_battery(self) -> Dict[str, Any]:
        """Verifica bateria do smartphone + fone."""
        if self.active and self.session_start:
            hours = (time.time() - self.session_start) / 3600
            self.battery_pct = max(0, 100 - (hours * self.battery_drain_per_hour))
        return {
            "phone_battery_pct": self.battery_pct,
            "headphone_battery_pct": self.audio.battery_pct,
            "estimated_remaining_h": self.battery_pct / self.battery_drain_per_hour if self.battery_drain_per_hour > 0 else 0,
            "low_battery": self.battery_pct < 20,
            "critical_battery": self.battery_pct < 5,
        }

    def set_mode(self, mode: CameraMode) -> str:
        """Muda modo de operacao."""
        self.mode = mode
        mode_names = {
            CameraMode.CONTINUOUS: "Continuo. Vou descrever tudo. (YOLOv11 + LLaVA ativados)",
            CameraMode.ON_DEMAND: "Sob demanda. Pergunte quando quiser.",
            CameraMode.ALERT_ONLY: "So alertas. So falo em perigo.",
            CameraMode.NAVIGATION: "Navegacao. Vou guiar voce.",
            CameraMode.READING: "Leitura. Aponte para o texto.",
            CameraMode.MONEY: "Dinheiro. Mostre a cedula.",
            CameraMode.COLOR: "Cor. Aponte para a cor.",
            CameraMode.FACE: "Reconhecimento. Olhe para a pessoa.",
            CameraMode.SEARCH: "Busca. O que procura?",
            CameraMode.MINIMAL: "Minimal. So o essencial.",
        }
        msg = mode_names.get(mode, "Modo alterado.")
        self.audio.speak(msg, DangerLevel.SAFE)
        return msg

    def set_verbosity(self, level: VerbosityLevel) -> str:
        """Muda nivel de verbosidade."""
        self.verbosity = level
        msgs = {
            VerbosityLevel.HIGH: "Detalhe alto. Vou descrever tudo.",
            VerbosityLevel.MEDIUM: "Detalhe medio. O essencial.",
            VerbosityLevel.LOW: "Detalhe baixo. So alertas.",
            VerbosityLevel.WHISPER: "Minimal. So perigos criticos.",
        }
        msg = msgs.get(level, "Verbosidade alterada.")
        self.audio.speak(msg, DangerLevel.SAFE)
        return msg

    def status(self) -> Dict[str, Any]:
        """Status completo do sistema."""
        return {
            "active": self.active,
            "mount": self.mount.value,
            "mode": self.mode.value,
            "verbosity": self.verbosity.value,
            "battery": self.check_battery(),
            "audio": self.audio.status(),
            "vision_frames": self.vision.frame_count,
            "total_descriptions": self.total_descriptions,
            "total_alerts": self.total_alerts,
            "destination": self.navigator.destination,
            "nav_step": self.navigator.current_step,
            "model_info": "YOLOv11 + LLaVA-Phi3-Vision (2025 on-device)"
        }


# ============================================================================
# 7. CENARIOS DO MUNDO REAL
# ============================================================================

def scenario_walking_to_destination():
    """Cenario: cego andando ate a padaria."""
    print("=" * 65)
    print("CENARIO 1: Cego andando ate a padaria")
    print("=" * 65)

    cam = BodyCameraController(MountPosition.CHEST, VerbosityLevel.MEDIUM)
    start = cam.start()
    print(f"\n[{start.get('greeting', {}).get('message', 'Camera ativa')}]")

    # Navegar
    print(f"\n[NAVEGACAO]")
    route = cam.navigate("Padaria do Joao")
    print(f"  {route}")

    # Passo a passo
    for i in range(4):
        print(f"\n[Passo {i+1}]")
        instruction = cam.navigate_step()
        print(f"  {instruction}")


def scenario_reading_menu():
    """Cenario: cego lendo cardapio."""
    print(f"\n{'=' * 65}")
    print("CENARIO 2: Cego lendo cardapio de restaurante")
    print("=" * 65)

    cam = BodyCameraController()
    cam.start()
    print(f"\n[MODO LEITURA]")
    text = cam.read_text()
    print(f"  Camera leu: {text}")


def scenario_identifying_money():
    """Cenario: cego reconhecendo cedula."""
    print(f"\n{'=' * 65}")
    print("CENARIO 3: Cego reconhecendo dinheiro")
    print("=" * 65)

    cam = BodyCameraController()
    cam.start()
    print(f"\n[MODO DINHEIRO]")
    money = cam.identify_money()
    print(f"  Camera identificou: {money}")


def scenario_crossing_street():
    """Cenario: cego atravessando rua com semaforo."""
    print(f"\n{'=' * 65}")
    print("CENARIO 4: Cego atravessando a rua")
    print("=" * 65)

    cam = BodyCameraController()
    cam.start()
    cam.set_mode(CameraMode.NAVIGATION)

    print(f"\n[Cena 1: Chegando no semaforo]")
    desc = cam.describe()
    print(f"  {desc}")

    print(f"\n[Cena 2: Semaforo]")
    color = cam.identify_color()
    print(f"  {color}")

    print(f"\n[Cena 3: Atravesando]")
    desc = cam.describe()
    print(f"  {desc}")


def scenario_meeting_person():
    """Cenario: cego encontrando pessoa conhecida."""
    print(f"\n{'=' * 65}")
    print("CENARIO 5: Cego reconhecendo pessoa a frente")
    print("=" * 65)

    cam = BodyCameraController()
    cam.start()
    print(f"\n[MODO ROSTO]")
    face = cam.recognize_face()
    print(f"  {face}")


def scenario_searching_object():
    """Cenario: cego procurando chave."""
    print(f"\n{'=' * 65}")
    print("CENARIO 6: Cego procurando objeto perdido")
    print("=" * 65)

    cam = BodyCameraController()
    cam.start()
    print(f"\n[MODO BUSCA: 'minha chave']")
    result = cam.search_object("minha chave")
    print(f"  {result}")


def scenario_battery_management():
    """Cenario: gerenciamento de bateria em caminhada longa."""
    print(f"\n{'=' * 65}")
    print("CENARIO 7: Bateria em caminhada longa")
    print("=" * 65)

    cam = BodyCameraController()
    cam.start()

    print(f"\n[Inicio da caminhada]")
    battery = cam.check_battery()
    print(f"  Celular: {battery['phone_battery_pct']:.0f}%")
    print(f"  Fone: {battery['headphone_battery_pct']:.0f}%")
    print(f"  Autonomia estimada: {battery['estimated_remaining_h']:.1f}h")

    # Simular 3 horas de uso
    cam.session_start = time.time() - 3 * 3600
    print(f"\n[Apos 3 horas de uso]")
    battery = cam.check_battery()
    print(f"  Celular: {battery['phone_battery_pct']:.0f}%")
    print(f"  Fone: {battery['headphone_battery_pct']:.0f}%")
    print(f"  Restante: {battery['estimated_remaining_h']:.1f}h")

    if battery["low_battery"]:
        print(f"  AVISO: Bateria baixa. Modo survival.")


def scenario_continuous_description():
    """Cenario: descricao continua enquanto anda."""
    print(f"\n{'=' * 65}")
    print("CENARIO 8: Descricao continua andando na rua")
    print("=" * 65)

    cam = BodyCameraController(MountPosition.CHEST, VerbosityLevel.MEDIUM)
    cam.start()

    print(f"\n[Descricao continua - 5 frames]")
    for i in range(5):
        desc = cam.describe()
        print(f"  Frame {i+1}: {desc}")
        time.sleep(0.1)  # simulacao rapida


# ============================================================================
# 8. RECOMENDAÇÕES DE HARDWARE 2024/2025
# ============================================================================

class HardwareRecommendations:
    """
    Smartphones compatíveis 2024/2025 com boa câmera + NPU para visão on-device.
    Preços aproximados em BRL (Brasil, 2025 - sujeitos a variação de mercado).
    Foco em devices com excelente câmera traseira, boa bateria e suporte a ML acceleration.
    """

    @staticmethod
    def get_recommendations() -> Dict[str, Any]:
        return {
            "recommended_smartphones": [
                {
                    "model": "Google Pixel 9a (2025)",
                    "camera": "50MP principal + ultrawide, excelente computational photography",
                    "npu": "Tensor G4 com forte suporte on-device AI (Gemini Nano)",
                    "price_brl": "≈ R$ 2.800 - 3.500",
                    "why": "Melhor para visão computacional acessível, excelente OCR e detecção de objetos com YOLOv11",
                    "battery": "5000mAh, ~8h uso contínuo com IA"
                },
                {
                    "model": "iPhone 16 / SE 4 (2025) ou iPhone 15 (usado)",
                    "camera": "48MP Fusion, excelente estabilização",
                    "npu": "A18 / A16 Bionic - Neural Engine líder de mercado",
                    "price_brl": "≈ R$ 3.200 - 5.000 (novo) / R$ 2.000-2.800 usado",
                    "why": "MLX + CoreML = LLaVA e YOLOv11 rodando a 30+ fps. Integração perfeita com Apple ecosystem e acessibilidade nativa",
                    "battery": "Até 10-12h com visão contínua otimizada"
                },
                {
                    "model": "Samsung Galaxy A56 / A36 (2025)",
                    "camera": "50MP + OIS, boa em baixa luz",
                    "npu": "Exynos 1580 ou Snapdragon 7 Gen 3 - AI Hub",
                    "price_brl": "≈ R$ 1.800 - 2.800",
                    "why": "Melhor custo-benefício para YOLOv11 + OCR no Android",
                    "battery": "5000mAh+ , boa autonomia"
                },
                {
                    "model": "Nothing Phone (3a) ou Motorola Edge 50 Fusion (2025)",
                    "camera": "50MP Sony LYTIA",
                    "npu": "MediaTek Dimensity 7300 / Snapdragon 7s Gen 2",
                    "price_brl": "≈ R$ 1.900 - 3.000",
                    "why": "Bom equilíbrio preço/desempenho para apps de acessibilidade e on-device inference"
                }
            ],
            "body_mount_options": [
                {
                    "type": "Clip magnético universal para peito/camisa",
                    "price_brl": "R$ 45 - 130 (Amazon, Mercado Livre 2025)",
                    "models": "JOBY GripTight, SmallRig Smartphone Chest Mount, genérico magnético ou arnês tático"
                },
                {
                    "type": "Suporte GoPro adaptado + case à prova d'água",
                    "price_brl": "R$ 80 - 200",
                    "models": "GoPro Chest Mount + adaptador para telefone"
                },
                {
                    "type": "Bandoleira ou arnês para smartphone (body cam style)",
                    "price_brl": "R$ 90 - 280",
                    "models": "Insta360 GO 3S mount adaptado ou suportes ergonômicos para cegos"
                }
            ],
            "total_estimated_cost_brl": "R$ 2.200 - 4.500 (smartphone mid-range + mount + fone BT bom)",
            "note": "Priorize devices com >=8GB RAM e NPU dedicada. YOLOv11n-s + LLaVA-Phi-3 ou Moondream2 rodam muito bem em 2025 em mid-range. Preços baseados em tendências de mercado 2024-2025."
        }


def print_hardware_2025():
    """Imprime recomendações atualizadas de hardware."""
    recs = HardwareRecommendations.get_recommendations()
    print("\n" + "="*75)
    print("RECOMENDAÇÕES DE HARDWARE & MODELOS DE VISÃO 2024/2025")
    print("="*75)
    print("Smartphones recomendados para OpenBodyCamera:")
    for phone in recs["recommended_smartphones"]:
        print(f"  • {phone['model']}: {phone['price_brl']}")
        print(f"    NPU: {phone['npu']}")
        print(f"    Camera: {phone['camera']}")
        print(f"    Por quê: {phone['why']}\n")
    print(f"Custo total estimado (celular + mount): {recs['total_estimated_cost_brl']}")
    print("Montagens corporais recomendadas: R$ 45-280")
    print("Nota: " + recs["note"])
    print("\nModelos de Visão Principais: YOLOv11, LLaVA-1.6/Phi-3-Vision, SAM2, Depth-Anything V2")


# ============================================================================
# 9. DEMONSTRACAO
# ============================================================================

def demo():
    print("=" * 70)
    print("OpenBodyCamera -- Smartphone Corporal + Fone BT = Olhos do Cego (2025)")
    print("=" * 70)

    print(f"\nMontagens: {len(MountPosition)}")
    for m in MountPosition:
        print(f"  {m.value}")

    print(f"\nModos de camera: {len(CameraMode)}")
    for m in CameraMode:
        print(f"  {m.value}")

    print(f"\nVerbosidade: {len(VerbosityLevel)}")
    for v in VerbosityLevel:
        print(f"  {v.value}")

    print(f"\nTipos de objeto: {len(ObjectType)}")
    print(f"Niveis de perigo: {len(DangerLevel)}")

    print_hardware_2025()

    # Cenarios
    scenario_walking_to_destination()
    scenario_reading_menu()
    scenario_identifying_money()
    scenario_crossing_street()
    scenario_meeting_person()
    scenario_searching_object()
    scenario_continuous_description()
    scenario_battery_management()

    # Status final
    cam = BodyCameraController()
    cam.start()
    cam.describe()
    cam.navigate("teste")
    status = cam.status()
    print(f"\n{'=' * 70}")
    print("STATUS DO SISTEMA")
    print(f"{'=' * 70}")
    print(f"  Ativo: {status['active']}")
    print(f"  Montagem: {status['mount']}")
    print(f"  Modo: {status['mode']}")
    print(f"  Verbosidade: {status['verbosity']}")
    print(f"  Frames processados: {status['vision_frames']}")
    print(f"  Descricoes geradas: {status['total_descriptions']}")
    print(f"  Alertas emitidos: {status['total_alerts']}")
    print(f"  Audio: {status['audio']['connected']}")
    print(f"  Modelo: {status.get('model_info', 'YOLOv11 + LLaVA')}")

    cam.stop()

    print(f"\n{'=' * 70}")
    print("RESUMO")
    print(f"{'=' * 70}")
    print()
    print("  O smartphone vira OLHOS (com YOLOv11 + LLaVA 2025).")
    print("  O fone bluetooth vira VOZ que descreve.")
    print("  O cego ANDA na rua com INFORMACAO em tempo real.")
    print("  NADA o para. NINGUEM o limita.")
    print()
    print("  Camera no peito (clip ~R$80). Fone no ouvido. Mundo na mente.")
    print("  O cego VE.")
    print()
    print("  Integrado com:")
    print("    OpenTelefonista (conversa natural)")
    print("    OpenInclusiveHardware (dispositivos acessíveis)")
    print("    OpenResilience (bateria/falhas)")
    print("    OpenHumanNet (emergencia)")


if __name__ == "__main__":
    demo()
