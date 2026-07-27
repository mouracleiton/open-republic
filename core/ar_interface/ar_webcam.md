# OpenRepublic -- Interface de Realidade Aumentada com Webcam

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/ar_interface/ar_webcam.py`

**Descricao:** =============================================================
Apenas uma webcam e um monitor. Sem oculos. Sem headset. Sem Kinecct.
A webcam VE as maos. O monitor MOSTRA objetos virtuais sobre o mundo real.
O usuario interage por GESTOS:
  - Pinca (polegar + indicador) -> pegar objeto
  - Mao aberta -> soltar / limpar
  - Apontar -> selecionar
  - Rotacao de punho -> girar objeto
  - Duas maos -> escalar (aproximar/afastar)
  - Deslizar -> navegar
  - Jab (soco no ar) -> confirmar / acionar
  - Palma para camera -> parar / pausar
CAPTURA:
  - MediaPipe Hands (Google, open-source) -> 21 pontos por mao
  - Funciona com QUALQUER webcam (inclusive terminal burro)
  - 30 FPS com webcam de 720p
  - Latencia < 50ms (processamento no edge node)
CASOS DE USO NA REPUBLICA:
  1. SIMULACAO DE FABLAB: montar peca virtual antes de imprimir
  2. EDUCACAO: manipular molecula, atomo, celula em 3D
  3. SAUDE: medico examina modelo de orgao antes da cirurgia
  4. ARQUITETURA: construir casa virtual antes de construir real
  5. ARTE: esculpir em ar livre
  6. ASSEMBLY: montar motor/protese/eletronica virtualmente
  5. GOVERNANCA: votar com gesto (mao levantada = sim)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Interface de Realidade Aumentada com Webcam
=============================================================

Apenas uma webcam e um monitor. Sem oculos. Sem headset. Sem Kinecct.
A webcam VE as maos. O monitor MOSTRA objetos virtuais sobre o mundo real.

O usuario interage por GESTOS:
  - Pinca (polegar + indicador) -> pegar objeto
  - Mao aberta -> soltar / limpar
  - Apontar -> selecionar
  - Rotacao de punho -> girar objeto
  - Duas maos -> escalar (aproximar/afastar)
  - Deslizar -> navegar
  - Jab (soco no ar) -> confirmar / acionar
  - Palma para camera -> parar / pausar

CAPTURA:
  - MediaPipe Hands (Google, open-source) -> 21 pontos por mao
  - Funciona com QUALQUER webcam (inclusive terminal burro)
  - 30 FPS com webcam de 720p
  - Latencia < 50ms (processamento no edge node)

CASOS DE USO NA REPUBLICA:
  1. SIMULACAO DE FABLAB: montar peca virtual antes de imprimir
  2. EDUCACAO: manipular molecula, atomo, celula em 3D
  3. SAUDE: medico examina modelo de orgao antes da cirurgia
  4. ARQUITETURA: construir casa virtual antes de construir real
  5. ARTE: esculpir em ar livre
  6. ASSEMBLY: montar motor/protese/eletronica virtualmente
  5. GOVERNANCA: votar com gesto (mao levantada = sim)

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa numpy as np


// ============================================================================
// Hand Tracking (MediaPipe Hands model -- 21 landmarks)
// ============================================================================

classe HandLandmark herda de Enum:
    // 21 pontos da mao detectados pela webcam.
    WRIST = 0
    THUMB_CMC = 1
    THUMB_MCP = 2
    THUMB_IP = 3
    THUMB_TIP = 4
    INDEX_MCP = 5
    INDEX_PIP = 6
    INDEX_DIP = 7
    INDEX_TIP = 8
    MIDDLE_MCP = 9
    MIDDLE_PIP = 10
    MIDDLE_DIP = 11
    MIDDLE_TIP = 12
    RING_MCP = 13
    RING_PIP = 14
    RING_DIP = 15
    RING_TIP = 16
    PINKY_MCP = 17
    PINKY_PIP = 18
    PINKY_DIP = 19
    PINKY_TIP = 20


classe GestureType herda de Enum:
    // Gestos reconhecidos pelo sistema.
    OPEN_PALM = "mao_aberta"  // 5 dedos esticados
    FIST = "punho_fechado"  // 0 dedos esticados
    PINCH = "pinca"  // polegar + indicador juntos
    POINT = "apontar"  // so indicador esticado
    PEACE = "paz"  // indicador + medio esticados
    THUMBS_UP = "joinha"  // so polegar esticado
    FLAT = "palma_plana"  // palma para camera (pare/pausa)
    PINCH_GRAB = "pinca_pegar"  // pinca + movimento = agarrar
    TWO_HAND_SCALE = "duas_maos_escala"  // duas maos afastar/aproximar
    TWO_HAND_ROTATE = "duas_maos_rotacao"
    SWIPE_LEFT = "deslizar_esquerda"
    SWIPE_RIGHT = "deslizar_direita"
    JAB = "soco"  // movimento rapido para frente
    SNAP = "estalar"  // polegar + medio (avancado)


classe Handedness herda de Enum:
    LEFT = "esquerda"
    RIGHT = "direita"
    BOTH = "ambas"


// ============================================================================
// Hand Data
// ============================================================================

// decorador: @dataclass
classe HandState:
    // Estado de uma mao detectada em um frame.
    handedness: Handedness
    landmarks: np.ndarray // (21, 3) -- x, y, z em coordenadas normalizadas
    seja gesture: GestureType = GestureType.OPEN_PALM
    seja confidence: flutuante = 0.0
    // Posicao do centro da palma (punto de referencia)
    seja palm_center: (flutuante, flutuante) = (0.5, 0.5)
    // Velocidade de movimento (px/frame)
    seja velocity: (flutuante, flutuante) = (0.0, 0.0)
    // Pinca strength (0=aberta, 1=totalmente pinçada)
    seja pinch_strength: flutuante = 0.0
    // Estabilidade (quao estavel a mao esta)
    seja stability: flutuante = 0.5


classe GestureRecognizer:
    // Reconhece gestos a partir dos 21 landmarks da mao.

    usa GEOMETRIA simples para classificar:
    - Dedo esticado vs dobrado: comparar articulacoes
    - Pinca: distancia polegar-indicador
    - Mao aberta: todos os 4 dedos esticados
    - Punho: nenhum dedo esticado
    - Apontar: so indicador esticado

    Nao precisa de ML para isso -- geometria basta.
    // 

    // Thresholds
    FINGER_EXTENDED_THRESH = 0.6 // se ponta > base em Y -> esticado
    PINCH_DISTANCE_THRESH = 0.05 // distancia polegar-indicador para pinca
    SWIPE_VEL_THRESH = 0.3 // velocidade para swipe
    JAB_VEL_THRESH = 0.5 // velocidade Z para jab
    STABILITY_THRESH = 0.02 // variancia para considerar estavel

    funcao __init__(self):
        self.prev_hands: {Handedness: HandState} = {}
        self.gesture_history: Dict[Handedness, [GestureType]] = {
            Handedness.LEFT: [], Handedness.RIGHT: []
        }

    funcao process(self, hands_data: [Dict]) -> [HandState]:
        // Processar frame da webcam e reconhecer gestos.

        hands_data: lista de dicionarios com 'handedness' e 'landmarks'
        (simulando saida do MediaPipe)
        // 
        current_hands = []
        current_set = set()

        para cada hd em hands_data:
            hand = Handedness(hd.get("handedness", "direita"))
            landmarks = np.array(hd.get("landmarks", []))

            se tamanho(landmarks) < 21 entao:
                continue

            current_set.add(hand)

            // Reconhecer gesto
            gesture = self._recognize(landmarks)

            // Calcular derivados
            palm_center = self._palm_center(landmarks)
            pinch = self._pinch_strength(landmarks)
            velocity = self._velocity(hand, palm_center)
            stability = self._stability(hand, landmarks)

            state = HandState(
                handedness = hand,
                landmarks = landmarks,
                gesture = gesture,
                confidence = hd.get("confidence", 0.9),
                palm_center = palm_center,
                velocity = velocity,
                pinch_strength = pinch,
                stability = stability,
            )

            current_hands.append(state)

            // Atualizar historico
            self.prev_hands[hand] = state
            self.gesture_history[hand].append(gesture)
            se tamanho(self.gesture_history[hand]) > 10 entao:
                self.gesture_history[hand] = self.gesture_history[hand][-10:]

        // Detectar gestos de duas maos
        se tamanho(current_hands) == 2 entao:
            two_hand = self._recognize_two_hand(current_hands[0], current_hands[1])
            se two_hand entao:
                current_hands[0].gesture = two_hand
                current_hands[1].gesture = two_hand

        retorne current_hands

    funcao _recognize(self, lm: np.ndarray) -> GestureType:
        // Reconhecer gesto de uma mao.
        fingers_up = self._count_fingers(lm)
        pinch = self._pinch_strength(lm)

        // Pinca tem prioridade
        se pinch > 0.8 entao:
            retorne GestureType.PINCH

        // Contar dedos
        se fingers_up == 0 entao:
            retorne GestureType.FIST
        se fingers_up == 5 entao:
            // Verificar se palma para camera (todos esticados + palma facing)
            retorne GestureType.OPEN_PALM
        se fingers_up == 1 entao:
            // So indicador
            se self._is_finger_extended(lm, "index") entao:
                retorne GestureType.POINT
        se fingers_up == 2 entao:
            // Indicador + medio
            if self._is_finger_extended(lm, "index")  e  \
               self._is_finger_extended(lm, "middle"):
                retorne GestureType.PEACE
        se fingers_up == 1  e  self._is_finger_extended(lm, "thumb") entao:
            retorne GestureType.THUMBS_UP

        retorne GestureType.OPEN_PALM

    // decorador: @staticmethod
    funcao _count_fingers(lm: np.ndarray) -> inteiro:
        // Contar quantos dedos estao esticados.
        count = 0
        // Polegar: comparar X (depende da mao, mas simplificado)
        thumb_extended = abs(lm[4][0] - lm[2][0]) > 0.04
        se thumb_extended entao:
            count = count + 1

        // Outros 4 dedos: ponta acima (Y menor) da articulacao PIP
        finger_tips = [8, 12, 16, 20] // index, middle, ring, pinky
        finger_pips = [6, 10, 14, 18]
        para cada (tip, pip) em intercale(finger_tips, finger_pips):
            if lm[tip][1] < lm[pip][1]: // Y da ponta < Y do pip = esticado
                count = count + 1
        retorne count

    // decorador: @staticmethod
    funcao _is_finger_extended(lm: np.ndarray, finger: texto) -> logico:
        finger_map = {"thumb": (4, 2), "index": (8, 6), "middle": (12, 10),
                      "ring": (16, 14), "pinky": (20, 18)}
        desempacote tip, pip = finger_map.get(finger, (0, 0))
        se finger == "thumb" entao:
            retorne abs(lm[tip][0] - lm[pip][0]) > 0.04
        retorne lm[tip][1] < lm[pip][1]

    // decorador: @staticmethod
    funcao _pinch_strength(lm: np.ndarray) -> flutuante:
        // Calcular forca da pinca (0-1).
        thumb_tip = lm[4]
        index_tip = lm[8]
        dist = math.sqrt((thumb_tip[0] - index_tip[0])**2 +
                        (thumb_tip[1] - index_tip[1])**2)
        // Normalizar: 0.15 = aberta, 0.02 = pinçada
        strength = maximo(0, minimo(1, (0.15 - dist) / (0.15 - 0.02)))
        retorne arredonde(strength, 2)

    // decorador: @staticmethod
    funcao _palm_center(lm: np.ndarray) retorna (flutuante, flutuante):
        // Centro da palma.
        // Media dos MCPs (base dos dedos) + pulso
        points = [lm[0], lm[5], lm[9], lm[13], lm[17]]
        cx = np.mean([p[0] para p em points])
        cy = np.mean([p[1] para p em points])
        retorne (arredonde(cx, 4), arredonde(cy, 4))

    funcao _velocity(self, hand: Handedness,
                  current_pos: (flutuante, flutuante)) -> (flutuante, flutuante):
        // Calcular velocidade da mao.
        prev = self.prev_hands.get(hand)
        se nao prev entao:
            retorne (0.0, 0.0)
        vx = current_pos[0] - prev.palm_center[0]
        vy = current_pos[1] - prev.palm_center[1]
        retorne (arredonde(vx, 4), arredonde(vy, 4))

    // decorador: @staticmethod
    funcao _stability(hand: Handedness, landmarks: np.ndarray) -> flutuante:
        // Quao estavel a mao esta (0=trêmula, 1=perfeitamente estável).
        // Jitter = variancia das posicoes da ponta do indicador
        index_tip = landmarks[8]
        // Simplificado: se z-variation baixa -> estável
        z_var = landmarks.shape[1] > 2 ? abs(landmarks[8][2]) : 0
        retorne maximo(0, minimo(1, 1 - z_var * 10))

    funcao _recognize_two_hand(self, left: HandState,
                            right: HandState) -> GestureType?:
        // Reconhecer gestos de duas maos.
        dist = math.sqrt(
            (left.palm_center[0] - right.palm_center[0])**2 +
            (left.palm_center[1] - right.palm_center[1])**2)

        // Verificar se ambas estao em pinca
        se left.pinch_strength > 0.7 e right.pinch_strength > 0.7 entao:
            retorne GestureType.TWO_HAND_SCALE

        // Verificar velocidade das duas maos
        if (abs(left.velocity[0]) > self.SWIPE_VEL_THRESH e 
            abs(right.velocity[0]) > self.SWIPE_VEL_THRESH):
            retorne GestureType.TWO_HAND_ROTATE

        retorne nulo


// ============================================================================
// Virtual Objects (what the AR shows)
// ============================================================================

classe ObjectType herda de Enum:
    CUBE = "cubo"
    SPHERE = "esfera"
    CYLINDER = "cilindro"
    MOLECULE = "molecula"  // para educacao quimica
    ATOM = "atomo"  // para fisica
    CELL = "celula"  // para biologia
    GEAR = "engrenagem"  // para engenharia
    HOUSE = "casa"  // para arquitetura
    PROSTHESIS = "protese"  // para medicina
    HEART = "coracao"  // para saude
    SOLAR_PANEL = "painel_solar"  // para energia
    PLANT = "planta"  // para agricultura
    TOOL = "ferramenta"  // para fablab
    TEXT = "texto"  // texto flutuante
    VOTE_BUTTON = "botao_voto"  // para governanca


// decorador: @dataclass
classe VirtualObject:
    // Um objeto virtual no espaco AR.
    obj_id: texto
    obj_type: ObjectType
    seja position: Tuple[flutuante, flutuante, flutuante] = (0.5, 0.5, 0.0) // x,y,z normalizado
    seja rotation: Tuple[flutuante, flutuante, flutuante] = (0.0, 0.0, 0.0) // graus
    seja scale: flutuante = 1.0
    seja color: Tuple[inteiro, inteiro, inteiro] = (100, 200, 100)
    seja grabbed: logico = falso // sendo segurado por gestos
    seja grabbed_by: texto = ""  // qual mao
    seja visible: logico = verdadeiro
    seja interactive: logico = verdadeiro
    seja label: texto = ""
    seja metadata: {texto: qualquer} = field(default_factory=dict)


classe ARScene:
    // Cena de Realidade Aumentada -- objetos virtuais sobre o mundo real.

    A cena e o que o usuario ve no monitor: o video da webcam com
    objetos 3D sobrepostos.
    // 
    funcao __init__(self):
        self.objects: {texto: VirtualObject} = {}
        self.active_hands: [HandState] = []
        self._obj_counter = 0
        self.on_grab: callable? = nulo
        self.on_release: callable? = nulo
        self.on_select: callable? = nulo
        self.on_gesture: callable? = nulo

    funcao add_object(self, obj_type: ObjectType,
                   seja position: Tuple[flutuante, flutuante, flutuante] = (0.5, 0.5, 0.0),
                   seja label: texto = "") -> VirtualObject:
        self._obj_counter += 1
        obj_id = "OBJ-{self._obj_counter:04d}"
        obj = VirtualObject(obj_id=obj_id, obj_type=obj_type,
                           position = position, label=label)
        self.objects[obj_id] = obj
        retorne obj

    funcao remove_object(self, obj_id: texto):
        self.objects.pop(obj_id, nulo)

    funcao update(self, hands: [HandState]):
        // Atualizar cena com base nos gestos detectados.
        self.active_hands = hands

        para cada hand em hands:
            para cada obj em self.objects.values():
                se nao obj.interactive ou nao obj.visible entao:
                    continue

                // Verificar se mao esta proxima ao objeto
                dist = math.sqrt(
                    (hand.palm_center[0] - obj.position[0])**2 +
                    (hand.palm_center[1] - obj.position[1])**2)

                // PINCA proxima = PEGAR
                if (hand.gesture == GestureType.PINCH e 
                    dist < 0.1 e nao obj.grabbed):
                    obj.grabbed = verdadeiro
                    obj.grabbed_by = hand.handedness.value
                    se self.on_grab entao:
                        self.on_grab(obj, hand)

                // SOLTAR
                elif (obj.grabbed e obj.grabbed_by == hand.handedness.value e 
                      hand.gesture != GestureType.PINCH):
                    obj.grabbed = falso
                    obj.grabbed_by = ""
                    se self.on_grab entao:
                        self.on_release(obj, hand)

                // Se grabbado, seguir mao
                se obj.grabbed e obj.grabbed_by == hand.handedness.value entao:
                    obj.position = (hand.palm_center[0],
                                   hand.palm_center[1],
                                   obj.position[2])

                // Se grabbado, seguir mao
                se obj.grabbed e obj.grabbed_by == hand.handedness.value entao:
                    obj.position = (hand.palm_center[0],
                                   hand.palm_center[1],
                                   obj.position[2])

                // ESCALAR com duas maos
                se hand.gesture == GestureType.TWO_HAND_SCALE entao:
                    pass // tratado abaixo

                // ROTACIONAR
                se obj.grabbed e hand.velocity != (0, 0) entao:
                    obj.rotation = (
                        obj.rotation[0],
                        obj.rotation[1],
                        obj.rotation[2] + hand.velocity[0] * 180)

            // APONTAR = SELECIONAR
            se hand.gesture == GestureType.POINT entao:
                closest = self._closest_object(hand.palm_center)
                se closest e self.on_select entao:
                    self.on_select(closest, hand)

        // Escala de duas maos
        if tamanho(hands) == 2 e all(h.gesture == GestureType.TWO_HAND_SCALE
                                   para cada h em hands):
            para cada obj em self.objects.values():
                se obj.grabbed entao:
                    dist = math.sqrt(
                        (hands[0].palm_center[0] - hands[1].palm_center[0])**2 +
                        (hands[0].palm_center[1] - hands[1].palm_center[1])**2)
                    obj.scale = maximo(0.1, minimo(5.0, dist * 3))
                    interrompa

    funcao _closest_object(self, pos: (flutuante, flutuante)) retorna VirtualObject?:
        closest = nulo
        min_dist = flutuante('inf')
        para cada obj em self.objects.values():
            se nao obj.visible entao:
                continue
            d = math.sqrt((pos[0] - obj.position[0])**2 +
                         (pos[1] - obj.position[1])**2)
            se d < min_dist entao:
                min_dist = d
                closest = obj
        min_dist < 0.2 ? retorne closest : nulo


// ============================================================================
// AR Application Scenarios for the Republic
// ============================================================================

classe ARScenario herda de Enum:
    FABLAB_SIMULATION = "simulacao_fablab"
    EDUCATION_ATOM = "educacao_atomo"
    EDUCATION_MOLECULE = "educacao_molecula"
    EDUCATION_CELL = "educacao_celula"
    HEALTH_ORGAN = "saude_orgao"
    ARCHITECTURE_HOUSE = "arquitetura_casa"
    ART_SCULPT = "arte_esculpir"
    ASSEMBLY_ENGINE = "montagem_motor"
    GOVERNANCE_VOTE = "governanca_voto"
    ENERGY_SOLAR = "energia_solar"


classe ARApplication:
    // Aplicacao AR completa para a Republica.

    CASOS DE USO:

    1. SIMULACAO DE FABLAB:
       Antes de imprimir 3D, o cidadao MONTA a peca virtualmente.
       Pega, gira, encaixa. Se faz sentido, manda para FabLab.
       Economiza material, tempo, e erro.

    2. EDUCACAO INTERATIVA:
       Em vez de ler sobre atomo, o aluno SEGURA um atomo na mao.
       Adiciona eletrons, ve o que acontece. Remove, ve.
       Manipula moleculas como se fossem LEGO.
       Aprende QUIMICA fazendo quimica.

    3. SAUDE:
       Medico gira um coracao 3D na frente do paciente.
       "E aqui que esta o bloqueio. Vamos fazer assim."
       Paciente ENTENDE porque nunca entendeu com panfleto.

    4. ARQUITETURA:
       Comunidade monta a casa virtual antes de construir.
       Cada um pega uma parede, posiziona. Ve se faz sentido.
       Decisão coletiva no espaco virtual antes do gasto real.

    5. VOTACAO POR GESTO:
       Proposta na tela. Cidadao levanta a mao (PALMA ABERTA = SIM,
       PUNHO FECHADO = nao). Webcam conta votos em tempo real.
    // 

    funcao __init__(self):
        self.scene = ARScene()
        self.recognizer = GestureRecognizer()
        self.active_scenario: ARScenario = nulo
        self.scenario_objects: [texto] = []

    funcao load_scenario(self, scenario: ARScenario):
        // Carregar um cenario predefinido.
        self.scene.objects.clear()
        self.scenario_objects.clear()

        se scenario == ARScenario.EDUCATION_ATOM entao:
            // Atomo: nucleo + eletrons
            nucleus = self.scene.add_object(ObjectType.ATOM,
                position = (0.5, 0.5, 0), label="Nucleo (protons + neutrons)")
            nucleus.color = (200, 50, 50)
            nucleus.scale = 2.0
            para cada i em intervalo(3):
                e = self.scene.add_object(ObjectType.SPHERE,
                    position = (0.5 + 0.1 * math.cos(i * 2.1),
                             0.5 + 0.1 * math.sin(i * 2.1), 0),
                    label = "Eletron {i+1}")
                e.color = (50, 100, 255)
                e.scale = 0.3
                self.scenario_objects.append(e.obj_id)
            self.scenario_objects.append(nucleus.obj_id)

        senao se scenario == ARScenario.FABLAB_SIMULATION entao:
            // Peca para montar: 3 blocos que encaixam
            block1 = self.scene.add_object(ObjectType.CUBE,
                position = (0.3, 0.3, 0), label="Base")
            block2 = self.scene.add_object(ObjectType.CUBE,
                position = (0.7, 0.3, 0), label="Suporte")
            block3 = self.scene.add_object(ObjectType.CUBE,
                position = (0.5, 0.7, 0), label="Topo")
            para cada b em [block1, block2, block3]:
                b.color = (200, 150, 50)
                self.scenario_objects.append(b.obj_id)

        senao se scenario == ARScenario.GOVERNANCE_VOTE entao:
            // Botao de voto
            btn = self.scene.add_object(ObjectType.VOTE_BUTTON,
                position = (0.5, 0.5, 0), label="PROPOSTA: Expandir automacao agricola")
            btn.color = (50, 200, 50)
            btn.scale = 2.0
            self.scenario_objects.append(btn.obj_id)

        senao se scenario == ARScenario.HEALTH_ORGAN entao:
            heart = self.scene.add_object(ObjectType.HEART,
                position = (0.5, 0.5, 0), label="Coracao")
            heart.color = (200, 30, 30)
            heart.scale = 2.5
            self.scenario_objects.append(heart.obj_id)

        senao se scenario == ARScenario.ARCHITECTURE_HOUSE entao:
            walls = ["Parede norte", "Parede sul", "Parede leste", "Parede oeste"]
            para cada (i, name) em enumere(walls):
                w = self.scene.add_object(ObjectType.CUBE,
                    position = (0.3 + 0.15 * (i % 2), 0.3 + 0.15 * (i // 2), 0),
                    label = name)
                w.color = (150, 150, 150)
                self.scenario_objects.append(w.obj_id)

        self.active_scenario = scenario

    funcao process_frame(self, hands_data: [Dict]) -> {texto: qualquer}:
        // Processar um frame completo: webcam -> gestos -> cena -> output.
        // 1. Reconhecer gestos
        hands = self.recognizer.process(hands_data)

        // 2. Atualizar cena
        self.scene.update(hands)

        // 3. Retornar estado para renderizar no monitor
        retorne self._render_state(hands)

    funcao _render_state(self, hands: [HandState]) -> {texto: qualquer}:
        // Estado que sera renderizado na tela (overlays sobre webcam).
        retorne {
            self.active_scenario ? "scenario": self.active_scenario.value : "none",
            "hands_detected": tamanho(hands),
            "gestures": [{"hand": h.handedness.value,
                         "gesture": h.gesture.value,
                         "pinch": h.pinch_strength,
                         "pos": h.palm_center} para h em hands],
            "objects": [{"id": o.obj_id, "type": o.obj_type.value,
                        "pos": o.position, "scale": o.scale,
                        "rot_z": o.rotation[2],
                        "grabbed": o.grabbed,
                        "label": o.label} para o em self.scene.objects.values()],
        }


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 75)
    imprima("  OPENREPUBLIC -- REALIDADE AUMENTADA COM WEBCAM")
    imprima("  'Sem oculos. Sem headset. So webcam e gestos.'")
    imprima("=" * 75)

    app = ARApplication()

    // Simulate hand data (MediaPipe-style output)
    funcao make_hand(handedness="direita", gesture="open", pos=(0.5, 0.5)):
        // Generate fake landmark data for testing.
        landmarks = []
        // Base template: 21 points
        base = [
            (0.5, 0.7, 0), // 0 wrist
            (0.48, 0.65, 0), // 1 thumb_cmc
            (0.45, 0.6, 0), // 2 thumb_mcp
            (0.42, 0.55, 0), // 3 thumb_ip
            (0.4, 0.5, 0), // 4 thumb_tip
            (0.5, 0.55, 0), // 5 index_mcp
            (0.5, 0.45, 0), // 6 index_pip
            (0.5, 0.38, 0), // 7 index_dip
            (0.5, 0.3, 0), // 8 index_tip
            (0.57, 0.53, 0), // 9 middle_mcp
            (0.6, 0.42, 0), // 10 middle_pip
            (0.62, 0.35, 0), // 11 middle_dip
            (0.64, 0.28, 0), // 12 middle_tip
            (0.64, 0.53, 0), // 13 ring_mcp
            (0.67, 0.42, 0), // 14 ring_pip
            (0.69, 0.35, 0), // 15 ring_dip
            (0.71, 0.28, 0), // 16 ring_tip
            (0.71, 0.55, 0), // 17 pinky_mcp
            (0.74, 0.47, 0), // 18 pinky_pip
            (0.76, 0.42, 0), // 19 pinky_dip
            (0.78, 0.38, 0), // 20 pinky_tip
        ]

        // Adjust based on gesture
        se gesture == "fist" entao:
            // Dobrar todos os dedos
            para cada tip em [4, 8, 12, 16, 20]:
                base[tip] = (base[tip][0], base[tip][1] + 0.1, 0)
            para cada pip em [6, 10, 14, 18]:
                base[pip] = (base[pip][0], base[pip][1] + 0.05, 0)
        senao se gesture == "pinch" entao:
            // Trazer polegar e indicador juntos
            base[4] = (base[8][0] - 0.01, base[8][1] - 0.01, 0)
        senao se gesture == "point" entao:
            // Dobrar tudo menos indicador
            para cada tip em [12, 16, 20]:
                base[tip] = (base[tip][0], base[tip][1] + 0.1, 0)
            para cada pip em [10, 14, 18]:
                base[pip] = (base[pip][0], base[pip][1] + 0.05, 0)
            base[4] = (base[4][0], base[4][1] + 0.05, 0)

        // Offset por position
        para cada i em intervalo(21):
            base[i] = (base[i][0] * 0.3 + pos[0] * 0.7,
                      base[i][1] * 0.3 + pos[1] * 0.7, 0)

        landmarks = np.array(base)
        retorne {"handedness": handedness, "landmarks": landmarks.tolist(),
                "confidence": 0.92}

    // === Test 1: Atom Education ===
    imprima("\n\n  === CENARIO: EDUCACAO -- ATOMO ===\n")
    app.load_scenario(ARScenario.EDUCATION_ATOM)
    imprima("  Objetos na cena: {len(app.scene.objects)}")
    para cada o em app.scene.objects.values():
        imprima("    {o.label}: pos={o.position} scale={o.scale}")

    // Simulate pinch to grab an electron
    imprima("\n  Frame 1: mao direita pinca proximo ao eletron")
    frame = app.process_frame([make_hand("direita", "pinch", (0.5, 0.5))])
    imprima("  Gesto: {frame['gestures'][0]['gesture']}")
    imprima("  Pinca: {frame['gestures'][0]['pinch']}")
    grabbed = [o para o em frame['objects'] if o['grabbed']]
    imprima("  Objetos grabbados: {len(grabbed)}")

    // Move
    imprima("\n  Frame 2: move mao para esquerda")
    frame = app.process_frame([make_hand("direita", "pinch", (0.4, 0.5))])
    para cada o em frame['objects']:
        se o['grabbed'] entao:
            imprima("    {o['label']}: nova pos={o['pos']}")

    // Release
    imprima("\n  Frame 3: solta (mao aberta)")
    frame = app.process_frame([make_hand("direita", "open", (0.4, 0.5))])
    imprima("  Gesto: {frame['gestures'][0]['gesture']}")
    grabbed = [o para o em frame['objects'] if o['grabbed']]
    imprima("  Objetos grabbados: {len(grabbed)}")

    // === Test 2: FabLab Simulation ===
    imprima("\n\n  === CENARIO: SIMULACAO FABLAB ===\n")
    app.load_scenario(ARScenario.FABLAB_SIMULATION)
    imprima("  Pecas para montar: {len(app.scene.objects)}")
    para cada o em app.scene.objects.values():
        imprima("    {o.label}: pos={o.position}")

    imprima("\n  Frame: pega a Base")
    frame = app.process_frame([make_hand("direita", "pinch", (0.3, 0.3))])
    grabbed = [o para o em frame['objects'] if o['grabbed']]
    imprima("  Grabbed: {[o['label'] for o in grabbed]}")

    // === Test 3: Governance Vote ===
    imprima("\n\n  === CENARIO: VOTACAO POR GESTO ===\n")
    app.load_scenario(ARScenario.GOVERNANCE_VOTE)
    imprima("  Proposta na tela")
    para cada o em app.scene.objects.values():
        imprima("    {o.label}")

    // Vote YES
    imprima("\n  Cidadao 1: PALMA ABERTA (SIM)")
    frame = app.process_frame([make_hand("direita", "open", (0.5, 0.5))])
    imprima("  Gesto: {frame['gestures'][0]['gesture']}")

    // Vote NO
    imprima("\n  Cidadao 2: PUNHO FECHADO (NAO)")
    frame = app.process_frame([make_hand("direita", "fist", (0.5, 0.5))])
    imprima("  Gesto: {frame['gestures'][0]['gesture']}")

    // === Summary ===
    imprima("\n\n{'='*75}")
    imprima("  COMO FUNCIONA")
    imprima("{'='*75}")
    imprima("""
  HARDWARE NECESSARIO:
    1 Webcam (qualquer uma, ate 720p)
    1 Monitor (terminal burro, smartphone, laptop)
    ZERO oculos, ZERO headset, ZERO periferico extra

  SOFTWARE:
    MediaPipe Hands (open-source, Google) -> 21 pontos por mao
    Renderizador 3D leve (Three.js / Panda3D / pygame)
    Tudo roda no EDGE NODE (processamento de gestos)
    Terminal burro so mostra a imagem

  GESTOS RECONHECIDOS:
    Pinca (polegar+indicador) -> pegar objeto
    Mao aberta -> soltar
    Apontar -> selecionar
    Punho -> confirmar / negar
    Duas maos afastar -> escalar
    Rotacao de punho -> girar
    Deslizar -> navegar
    Palma para camera -> parar/pausar

  10 CENARIOS PARA A REPUBLICA:
    1. FabLab: montar peca virtual antes de imprimir
    2. Atomo: segurar eletrons, ver orbits
    3. Molecula: ligar atomos como LEGO
    4. Celula: entrar numa celula 3D
    5. Orgao: medico gira coracao para paciente
    6. Casa: comunidade monta antes de construir
    7. Arte: esculpir no ar
    8. Motor: montar pea por pea virtualmente
    9. Voto: palma=SIM, punho=nao (webcam conta)
    10. Painel solar: posicionar antes de instalar

  "Na Republica, AR nao e luxo de oculos caros.
   e webcam de terminal burro + gestos no ar.
   Custa zero. Serve para tudo.
   A webcam ve. O monitor mostra. A mao faz."
// )

```
