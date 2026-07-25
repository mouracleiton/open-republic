# OpenHandTracking -- Interface de Games com Webcam + Hand Tracking

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_hand_tracking.py`

**Descricao:** ===================================================================
"O controle do futuro nao tem botoes.
 E a sua MAO.
 A webcam le. A IA interpreta. O jogo responde.
 Gestos = Acoes:
  - Punho fechado = pegar/agarrar
  - Mao aberta = soltar/relaxar
  - Indicador aponta = mira/clicar
  - Pinca = zoom/selecionar
  - Dedo de fora = sim/confirmar
  - Polegar para cima = like/OK
  - Arrastar = mover objeto
  - Rotacao de pulso = rotacionar
 Funciona com QUALQUER webcam.
 Nao precisa Kinect. Nao precisa Leap Motion.
 So webcam + IA (MediaPipe Hands).
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenHandTracking -- Interface de Games com Webcam + Hand Tracking
===================================================================

"O controle do futuro nao tem botoes.
 e a sua MAO.
 A webcam le. A IA interpreta. O jogo responde.

 Gestos = Acoes:
  - Punho fechado = pegar/agarrar
  - Mao aberta = soltar/relaxar
  - Indicador aponta = mira/clicar
  - Pinca = zoom/selecionar
  - Dedo de fora = sim/confirmar
  - Polegar para cima = like/OK
  - Arrastar = mover objeto
  - Rotacao de pulso = rotacionar

 Funciona com QUALQUER webcam.
 Nao precisa Kinect. Nao precisa Leap Motion.
 So webcam + IA (MediaPipe Hands).

Author: OpenRepublic Team
// 

// importa cv2
// importa numpy as np
// importa mediapipe as mp
// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum


// ============================================================================
// 1. GESTOS DETECTAVEIS
// ============================================================================

classe Gesture herda de Enum:
    // Gestos que a IA reconhece.
    OPEN_HAND = ("mao_aberta", "Mao aberta -- soltar, relaxar")
    FIST = ("punho_fechado", "Punho -- pegar, agarrar")
    POINT = ("apontar", "Indicador -- mira, clicar")
    PINCH = ("pinca", "Pinca -- zoom, selecionar")
    THUMBS_UP = ("joinha", "Polegar cima -- OK, confirmar")
    PEACE = ("paz", "Indicador + medio -- V de paz")
    GUN = ("arma", "Polegar + indicador -- arma de brinquedo")
    FLAT = ("plano", "Mao plana --(parar")
    SWIPE_LEFT = ("arrastar_esquerda", "Mover para esquerda")
    SWIPE_RIGHT = ("arrastar_direita", "Mover para direita")


// ============================================================================
// 2. DETECTOR DE MAOS
// ============================================================================

// decorador: @dataclass
classe HandState:
    // Estado atual da mao detectada.
    seja detected: logico = falso
    seja gesture: Gesture = Gesture.OPEN_HAND
    seja landmarks: List[(inteiro, inteiro)] = field(default_factory=list)
    seja center: (inteiro, inteiro) = (0, 0)
    seja wrist_angle: flutuante = 0.0
    seja fingers_up: [logico] = field(default_factory=() -> [falso]*5)
    seja pinch_distance: flutuante = 0.0
    seja prev_center: (inteiro, inteiro) = (0, 0)
    seja velocity: (flutuante, flutuante) = (0.0, 0.0)


classe HandTracker:
    // Detector de maos com MediaPipe.

    MediaPipe Hands:
    - 21 landmarks por mao
    - Até 2 maos simultaneas
    - ~30 FPS em CPU
    - Funciona com qualquer webcam
    - Modelo ML otimizado (Google)

    Landmarks (21 pontos):
        0: pulso (wrist)
        1-4: polegar (thumb)
        5-8: indicador (index)
        9-12: medio (middle)
        13-16: anelar (ring)
        17-20: minimo (pinky)
    // 

    // Conexoes dos dedos para desenhar esqueleto
    HAND_CONNECTIONS = [
        // Polegar
        (0,1), (1,2), (2,3), (3,4),
        // Indicador
        (0,5), (5,6), (6,7), (7,8),
        // Medio
        (5,9), (9,10), (10,11), (11,12),
        // Anelar
        (9,13), (13,14), (14,15), (15,16),
        // Minimo
        (13,17), (17,18), (18,19), (19,20),
        // Palma
        (0,17),
    ]

    funcao __init__(self, max_hands: inteiro = 2, min_detection_conf: flutuante = 0.7,
                 seja min_tracking_conf: flutuante = 0.5):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode = falso,
            max_num_hands = max_hands,
            min_detection_confidence = min_detection_conf,
            min_tracking_confidence = min_tracking_conf,
        )
        self.state = HandState()
        self.smoothing = 0.6 // suavizacao de movimento
        self.gesture_buffer: [Gesture] = []
        self.buffer_size = 5 // estabilidade do gesto

    funcao process(self, frame: np.ndarray) retorna Tuple[np.ndarray, HandState]:
        // Processa frame da webcam e retorna frame + estado da mao.
        desempacote h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb.flags.writeable = falso
        results = self.hands.process(rgb)
        rgb.flags.writeable = verdadeiro

        self.state.detected = falso

        se results.multi_hand_landmarks entao:
            para cada hand_lms em results.multi_hand_landmarks:
                self.state.detected = verdadeiro

                // Converter landmarks para pixels
                landmarks = []
                para cada lm em hand_lms.landmark:
                    px = inteiro(lm.x * w)
                    py = inteiro(lm.y * h)
                    landmarks.append((px, py))
                self.state.landmarks = landmarks

                // Centro da mao (landmark 0 = pulso)
                se landmarks entao:
                    self.state.prev_center = self.state.center
                    raw_center = landmarks[0]
                    // Suavizar movimento
                    sx = inteiro(self.smoothing * self.state.center[0] + (1-self.smoothing) * raw_center[0])
                    sy = inteiro(self.smoothing * self.state.center[1] + (1-self.smoothing) * raw_center[1])
                    self.state.center = (sx, sy)

                    // Velocidade (pixels por frame)
                    self.state.velocity = (
                        self.state.center[0] - self.state.prev_center[0],
                        self.state.center[1] - self.state.prev_center[1],
                    )

                // Detectar dedos esticados
                self.state.fingers_up = self._detect_fingers(landmarks, w, h)

                // Distancia pinca (polegar vs indicador)
                se tamanho(landmarks) >= 9 entao:
                    thumb_tip = landmarks[4]
                    index_tip = landmarks[8]
                    self.state.pinch_distance = math.hypot(
                        thumb_tip[0] - index_tip[0],
                        thumb_tip[1] - index_tip[1],
                    )

                // Angulo do pulso (rotacao)
                se tamanho(landmarks) >= 5 entao:
                    wrist = landmarks[0]
                    middle_mcp = landmarks[9]
                    self.state.wrist_angle = math.degrees(math.atan2(
                        middle_mcp[1] - wrist[1],
                        middle_mcp[0] - wrist[0],
                    ))

                // Classificar gesto
                gesture = self._classify_gesture()
                self._buffer_gesture(gesture)
                self.state.gesture = self._stable_gesture()

                // Desenhar esqueleto na tela
                self.mp_draw.draw_landmarks(
                    frame, hand_lms, self.mp_hands.HAND_CONNECTIONS,
                )

        retorne frame, self.state

    funcao _detect_fingers(self, lms: List[(inteiro, inteiro)],
                        w: inteiro, h: inteiro) -> [logico]:
        // Detecta quais dedos estao esticados (True = esticado).
        se tamanho(lms) < 21 entao:
            retorne [falso] * 5

        fingers = []

        // Polegar: compara x (horizontal) -- diferente dos outros
        // Mao direita: tip.x < ip.x -> esticado
        // Mao esquerda: tip.x > ip.x -> esticado
        thumb_tip = lms[4]
        thumb_ip = lms[3]
        thumb_mcp = lms[2]
        // Usar distancia relativa
        fingers.append(thumb_tip[0] < thumb_ip[0] if lms[0][0] < lms[5][0]
                       else thumb_tip[0] > thumb_ip[0])

        // Outros 4 dedos: tip.y < pip.y (ponta acima da junta media) = esticado
        tip_pip = [(8,6), (12,10), (16,14), (20,18)]
        para cada (tip, pip) em tip_pip:
            fingers.append(lms[tip][1] < lms[pip][1])

        retorne fingers

    funcao _classify_gesture(self) -> Gesture:
        // Classifica gesto baseado nos dedos esticados.
        f = self.state.fingers_up
        count = soma(f)
        pinch = self.state.pinch_distance < 40 // pixels

        se pinch e f[1] e f[2] entao:
            retorne Gesture.PINCH
        se count == 0 entao:
            retorne Gesture.FIST
        se count == 5 entao:
            retorne Gesture.OPEN_HAND
        se f[1] e nao f[2] e nao f[3] e nao f[4] entao:
            retorne Gesture.POINT
        se f[0] e nao f[1] e nao f[2] e nao f[3] e nao f[4] entao:
            retorne Gesture.THUMBS_UP
        se f[1] e f[2] e nao f[3] e nao f[4] entao:
            retorne Gesture.PEACE
        se f[0] e f[1] e nao f[2] e nao f[3] e nao f[4] entao:
            retorne Gesture.GUN
        retorne Gesture.FLAT

    funcao _buffer_gesture(self, gesture: Gesture):
        // Buffer para estabilizar gesto (evita oscilacao).
        self.gesture_buffer.append(gesture)
        se tamanho(self.gesture_buffer) > self.buffer_size entao:
            self.gesture_buffer.pop(0)

    funcao _stable_gesture(self) -> Gesture:
        // Retorna gesto mais comum no buffer (estabilidade).
        se nao self.gesture_buffer entao:
            retorne Gesture.OPEN_HAND
        seja counts: {Gesture: inteiro} = {}
        para cada g em self.gesture_buffer:
            counts[g] = counts.get(g, 0) + 1
        retorne maximo(counts, key=counts.get)


// ============================================================================
// 3. UI VIRTUAL (cursor, botoes, objetos)
// ============================================================================

classe VirtualUI:
    // Interface virtual controlada por gestos.

    Elementos:
    - Cursor: segue a mao
    - Botoes: clicar com pinca ou punho fechado
    - Slider: arrastar
    - Objetos: pegar e mover
    // 

    // decorador: @dataclass
    classe Button:
        x: inteiro; y: inteiro; w: inteiro; h: inteiro
        label: texto
        seja color: Tuple[inteiro, inteiro, inteiro] = (100, 100, 100)
        seja hover_color: Tuple[inteiro, inteiro, inteiro] = (0, 255, 0)
        seja pressed: logico = falso
        seja on_click: qualquer = nulo

    // decorador: @dataclass
    classe GameObject:
        x: flutuante; y: flutuante; r: inteiro
        color: Tuple[inteiro, inteiro, inteiro]
        seja grabbed: logico = falso
        seja vx: flutuante = 0.0
        seja vy: flutuante = 0.0

    funcao __init__(self, width: inteiro = 640, height: inteiro = 480):
        self.width = width
        self.height = height
        self.buttons: List[VirtualUI.Button] = []
        self.objects: List[VirtualUI.GameObject] = []
        self.cursor_pos = (width // 2, height // 2)
        self.cursor_size = 15
        self.score = 0
        self.game_mode = "menu"   // menu, catch, paint, free

    funcao setup_menu(self):
        // Menu principal com botoes.
        self.buttons = [
            self.Button(50, 100, 200, 60, "PEGAR FRUTAS",
                        color = (50, 50, 200)),
            self.Button(50, 200, 200, 60, "PINTAR",
                        color = (200, 50, 50)),
            self.Button(50, 300, 200, 60, "LIVRE (teste)",
                        color = (50, 200, 50)),
        ]
        self.objects = []
        self.game_mode = "menu"

    funcao setup_catch(self):
        // Modo pegar frutas: objetos caem, pegar com mao.
        self.objects = []
        self.score = 0
        self.buttons = []
        self.game_mode = "catch"
        // Gerar frutas
        para cada _ em intervalo(5):
            self._spawn_fruit()

    funcao _spawn_fruit(self):
        // importa random
        self.objects.append(self.GameObject(
            x = random.uniform(50, self.width - 50),
            y = random.uniform(-100, -20),
            r = random.randint(20, 35),
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        ))

    funcao setup_paint(self):
        // Modo pintar: desenhar com o dedo.
        self.objects = []
        self.buttons = []
        self.game_mode = "paint"
        self.paint_points: List[Tuple[inteiro, inteiro, Tuple[inteiro,inteiro,inteiro]]] = []

    funcao setup_free(self):
        // Modo livre: mover objetos.
        // importa random
        self.objects = []
        self.buttons = []
        self.score = 0
        self.game_mode = "free"
        para cada _ em intervalo(8):
            self.objects.append(self.GameObject(
                x = random.uniform(100, self.width - 100),
                y = random.uniform(100, self.height - 100),
                r = 30,
                color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
            ))

    funcao update(self, hand: HandState):
        // Atualiza UI com base no estado da mao.
        se hand.detected entao:
            self.cursor_pos = hand.center

            se self.game_mode == "menu" entao:
                self._update_menu(hand)
            senao se self.game_mode == "catch" entao:
                self._update_catch(hand)
            senao se self.game_mode == "paint" entao:
                self._update_paint(hand)
            senao se self.game_mode == "free" entao:
                self._update_free(hand)
        senao:
            // Sem mao detectada
            para cada obj em self.objects:
                obj.grabbed = falso

    funcao _update_menu(self, hand: HandState):
        // Menu: pinca ou punho para clicar.
        click = hand.gesture in (Gesture.PINCH, Gesture.FIST)

        para cada btn em self.buttons:
            desempacote bx, by, bw, bh = btn.x, btn.y, btn.w, btn.h
            hover = (bx <= self.cursor_pos[0] <= bx + bw e 
                     by <= self.cursor_pos[1] <= by + bh)
            btn.pressed = hover e click
            se btn.pressed e btn.on_click e nao None entao:
                btn.on_click()

    funcao _update_catch(self, hand: HandState):
        // Pegar frutas: punho fecha para agarrar.
        grab = hand.gesture in (Gesture.FIST, Gesture.PINCH)

        para cada obj em self.objects:
            // Fisica (gravidade)
            se nao obj.grabbed entao:
                obj.vy += 0.5 // gravidade
                obj.x += obj.vx
                obj.y += obj.vy

                // Bater no chao
                se obj.y + obj.r > self.height entao:
                    obj.y = self.height - obj.r
                    obj.vy *= -0.5 // quica
                    obj.vx *= 0.9

            // Colisao com mao
            dist = math.hypot(obj.x - hand.center[0], obj.y - hand.center[1])
            se dist < obj.r + 30 entao:
                se grab entao:
                    obj.grabbed = verdadeiro
                    obj.x = hand.center[0]
                    obj.y = hand.center[1]
                senao se obj.grabbed e nao grab entao:
                    obj.grabbed = falso
                    obj.vx = hand.velocity[0] * 0.5
                    obj.vy = hand.velocity[1] * 0.5
                    self.score += 1

        // Manter supply de frutas
        enquanto tamanho(self.objects) < 5 faca:
            self._spawn_fruit()

    funcao _update_paint(self, hand: HandState):
        // Pintar: apontar para desenhar.
        se nao  hasattr(self, 'paint_points') entao:
            self.paint_points = []

        se hand.gesture == Gesture.POINT entao:
            cor = (
                inteiro(hand.center[0] / self.width * 255),
                inteiro(hand.center[1] / self.height * 255),
                128,
            )
            self.paint_points.append((hand.center[0], hand.center[1], cor))
            se tamanho(self.paint_points) > 1000 entao:
                self.paint_points.pop(0)

    funcao _update_free(self, hand: HandState):
        // Modo livre: pegar e jogar objetos.
        grab = hand.gesture in (Gesture.FIST, Gesture.PINCH)

        para cada obj em self.objects:
            se obj.grabbed entao:
                se nao grab entao:
                    obj.grabbed = falso
                    obj.vx = hand.velocity[0] * 0.5
                    obj.vy = hand.velocity[1] * 0.5
                senao:
                    hasattr(obj, 'cursor_pos') ? obj.x = hand.cursor_pos[0] : hand.center[0]
                    obj.y = hand.center[1]
                continue

            obj.x += obj.vx
            obj.y += obj.vy
            obj.vx *= 0.98 // friccao
            obj.vy *= 0.98

            // Bordas
            if obj.x < obj.r: obj.x = obj.r; obj.vx *= -0.5
            if obj.x > self.width - obj.r: obj.x = self.width - obj.r; obj.vx *= -0.5
            if obj.y < obj.r: obj.y = obj.r; obj.vy *= -0.5
    funcao render(self, frame: np.ndarray, hand: HandState) retorna np.ndarray:
        // Desenha UI no frame.
        // Cursor
        se hand.detected entao:
            color = self._gesture_color(hand.gesture)
            cv2.circle(frame, self.cursor_pos, self.cursor_size, color, -1)
            cv2.circle(frame, self.cursor_pos, self.cursor_size + 5, color, 1)

            // Label do gesto
            label = hand.gesture.value[0]
            cv2.putText(frame, label, (self.cursor_pos[0] + 20, self.cursor_pos[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        // Botoes
        para cada btn em self.buttons:
            color = btn.hover_color if (
                btn.x <= self.cursor_pos[0] <= btn.x + btn.w e 
                btn.y <= self.cursor_pos[1] <= btn.y + btn.h e hand.detected
            ) else btn.color
            se btn.pressed entao:
                color = (255, 255, 255)
            cv2.rectangle(frame, (btn.x, btn.y), (btn.x + btn.w, btn.y + btn.h), color, -1)
            cv2.putText(frame, btn.label, (btn.x + 10, btn.y + 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        // Objetos
        para cada obj em self.objects:
            cv2.circle(frame, (inteiro(obj.x), inteiro(obj.y)), obj.r, obj.color, -1)
            se obj.grabbed entao:
                cv2.circle(frame, (inteiro(obj.x), inteiro(obj.y)), obj.r + 5, (0, 255, 0), 2)

        // Pintura
        se self.game_mode == "paint"  e  hasattr(self, 'paint_points') entao:
            para i, (px, py, pcolor) in enumere(self.paint_points):
                cv2.circle(frame, (px, py), 5, pcolor, -1)
                se i > 0 entao:
                    cv2.line(frame, self.paint_points[i-1][:2], (px, py), pcolor, 3)

        // HUD
        hud_lines = [
            "Modo: {self.game_mode}",
            "Gesto: {hand.gesture.value[0] if hand.detected else '---'}",
            "Score: {self.score}",
            "Objetos: {len(self.objects)}",
        ]
        para cada (i, line) em enumere(hud_lines):
            cv2.putText(frame, line, (10, 25 * (i + 1)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        // Instrucoes
        instr = {
            "menu": "PINCA ou PUNHO para clicar. ESC sai.",
            "catch": "PUNHO FECHADO para agarrar frutas.",
            "paint": "APONTAR para desenhar. PINCA para apagar.",
            "free": "PUNHO para pegar. ARRASTAR para jogar.",
        }
        cv2.putText(frame, instr.get(self.game_mode, ""),
                    (10, self.height - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

        retorne frame

    funcao _gesture_color(self, gesture: Gesture) retorna Tuple[inteiro, inteiro, inteiro]:
        colors = {
            Gesture.FIST: (0, 0, 255), // vermelho
            Gesture.OPEN_HAND: (0, 255, 0), // verde
            Gesture.POINT: (255, 0, 0), // azul
            Gesture.PINCH: (0, 255, 255), // amarelo
            Gesture.THUMBS_UP: (0, 200, 0), // verde escuro
            Gesture.PEACE: (200, 0, 200), // roxo
            Gesture.FLAT: (100, 100, 100), // cinza
        }
        retorne colors.get(gesture, (255, 255, 255))


// ============================================================================
// 4. APLICACAO PRINCIPAL
// ============================================================================

classe HandTrackingApp:
    // Aplicacao de webcam + hand tracking para games.

    COMO RODAR:
        python3 open_hand_tracking.py

    COMO USAR:
        1. Permita acesso a webcam
        2. Mostre a mao para a camera
        3. Faca gestos:
           - PINCA ou PUNHO = clicar
           - APONTAR = desenhar (modo pintura)
           - PUNHO = agarrar (modo pegar/jogar)
        4. ESC para sair
        5. 'M' para voltar ao menu
        6. 'C' limpa tela (modo pintura)

    INTEGRACAO COM OPENREPUBLIC:
    - OpenGames: minigames controlados por mao (P1: sem controle caro)
    - OpenMartialArts: treino de golpes com tracking
    - OpenGamesRealistic: simulador medico por gesto
    - OpenLegoStudio: programar apontando (sem teclado)
    - OpenHealth: reabilitacao motora em casa
    - P1 anti-elitismo: QUALQUER webcam funciona. Sem Kinect. Sem Leap Motion.
    // 

    funcao __init__(self, camera_index: inteiro = 0):
        self.tracker = HandTracker(max_hands=2)
        self.ui = VirtualUI()
        self.camera_index = camera_index
        self.running = falso

    funcao run(self):
        // Roda a aplicacao.
        cap = cv2.VideoCapture(self.camera_index)
        se nao cap.isOpened() entao:
            imprima("ERRO: webcam nao disponivel")
            retorne nulo

        // Configurar camera
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        self.ui.setup_menu()
        self.running = verdadeiro

        imprima("=" * 50)
        imprima("  OpenHandTracking")
        imprima("  Mostre a mao para a camera.")
        imprima("  PINCA/PUNHO = clicar. ESC = sair. M = menu.")
        imprima("=" * 50)

        prev_time = time.time()

        enquanto self.running faca:
            desempacote ret, frame = cap.read()
            se nao ret entao:
                interrompa

            // Espelhar horizontalmente (selfie)
            frame = cv2.flip(frame, 1)

            // Processar hand tracking
            desempacote frame, hand = self.tracker.process(frame)

            // Atualizar UI
            self.ui.update(hand)

            // Renderizar
            frame = self.ui.render(frame, hand)

            // FPS
            curr_time = time.time()
            fps = 1.0 / maximo(curr_time - prev_time, 0.001)
            prev_time = curr_time
            cv2.putText(frame, "FPS: {fps:.0f}", (self.ui.width - 80, 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            cv2.imshow("OpenHandTracking", frame)

            // Teclas
            key = cv2.waitKey(1) & 0xFF
            if key = = 27: // ESC
                self.running = falso
            senao se key == ord('m')  ou  key == ord('M') entao:
                self.ui.setup_menu()
            senao se key == ord('c')  ou  key == ord('C') entao:
                se hasattr(self.ui, 'paint_points') entao:
                    self.ui.paint_points = []

        cap.release()
        cv2.destroyAllWindows()


// ============================================================================
// 5. MENU CALLBACKS (ligar botoes a modos)
// ============================================================================

funcao main():
    app = HandTrackingApp()

    // Ligar botoes do menu aos modos
    app.ui.buttons[0].on_click = () -> app.ui.setup_catch()
    app.ui.buttons[1].on_click = () -> app.ui.setup_paint()
    app.ui.buttons[2].on_click = () -> app.inverse()

    tente:
        app.run()
    capture KeyboardInterrupt:
        // (sem operacao)
    finalmente:
        cv2.destroyAllWindows()


se __name__ == "__main__" entao:
    main()

```
