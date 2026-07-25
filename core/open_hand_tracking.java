// OpenHandTracking -- Interface de Games com Webcam + Hand Tracking -- gerado de Portugol++
public class OpenhandtrackingInterfaceDeGamesComWebcamHandTracking {

    // !/usr/bin/env python3
    //
    OpenHandTracking -- Interface de Games com Webcam + Hand Tracking;
    ===================================================================;
    "O controle do futuro ! tem botoes.;
    && a sua MAO.;
    A webcam le. A IA interpreta. O jogo responde.;
    Gestos = Acoes:;
    - Punho fechado = pegar/agarrar;
    - Mao aberta = soltar/relaxar;
    - Indicador aponta = mira/clicar;
    - Pinca = zoom/selecionar;
    - Dedo de fora = sim/confirmar;
    - Polegar para cima = like/OK;
    - Arrastar = mover objeto;
    - Rotacao de pulso = rotacionar;
    Funciona com QUALQUER webcam.;
    Nao precisa Kinect. Nao precisa Leap Motion.;
    So webcam + IA (MediaPipe Hands).;
    Author: OpenRepublic Team;
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
    public static class Gesture {
        // Gestos que a IA reconhece.
        OPEN_HAND = ("mao_aberta", "Mao aberta -- soltar, relaxar");
        FIST = ("punho_fechado", "Punho -- pegar, agarrar");
        POINT = ("apontar", "Indicador -- mira, clicar");
        PINCH = ("pinca", "Pinca -- zoom, selecionar");
        THUMBS_UP = ("joinha", "Polegar cima -- OK, confirmar");
        PEACE = ("paz", "Indicador + medio -- V de paz");
        GUN = ("arma", "Polegar + indicador -- arma de brinquedo");
        FLAT = ("plano", "Mao plana --(parar");
        SWIPE_LEFT = ("arrastar_esquerda", "Mover para esquerda");
        SWIPE_RIGHT = ("arrastar_direita", "Mover para direita");
    // ============================================================================
    // 2. DETECTOR DE MAOS
    // ============================================================================
    // decorador: @dataclass
    public static class HandState {
        // Estado atual da mao detectada.
        boolean detected = false;
        Gesture gesture = Gesture.OPEN_HAND;
        List[(inteiro, inteiro)] landmarks = field(default_factory=list);
        (inteiro, inteiro) center = (0, 0);
        double wrist_angle = 0.0;
        [logico] fingers_up = field(default_factory=() -> [false]*5);
        double pinch_distance = 0.0;
        (inteiro, inteiro) prev_center = (0, 0);
        (flutuante, flutuante) velocity = (0.0, 0.0);
    public static class HandTracker {
        // Detector de maos com MediaPipe.
        MediaPipe Hands:;
        - 21 landmarks por mao;
        - Até 2 maos simultaneas;
        - ~30 FPS em CPU;
        - Funciona com qualquer webcam;
        - Modelo ML otimizado (Google);
        Landmarks (21 pontos):;
            0: pulso (wrist);
            1-4: polegar (thumb);
            5-8: indicador (index);
            9-12: medio (middle);
            13-16: anelar (ring);
            17-20: minimo (pinky);
        //
        // Conexoes dos dedos para desenhar esqueleto
        HAND_CONNECTIONS = [;
            // Polegar
            (0,1), (1,2), (2,3), (3,4),;
            // Indicador
            (0,5), (5,6), (6,7), (7,8),;
            // Medio
            (5,9), (9,10), (10,11), (11,12),;
            // Anelar
            (9,13), (13,14), (14,15), (15,16),;
            // Minimo
            (13,17), (17,18), (18,19), (19,20),;
            // Palma
            (0,17),;
        ];
        funcao __init__(self, max_hands: inteiro = 2, min_detection_conf: flutuante = 0.7,
                    double min_tracking_conf = 0.5):;
            self.mp_hands = mp.solutions.hands;
            self.mp_draw = mp.solutions.drawing_utils;
            self.hands = self.mp_hands.Hands(;
                static_image_mode = false,;
                max_num_hands = max_hands,;
                min_detection_confidence = min_detection_conf,;
                min_tracking_confidence = min_tracking_conf,;
            );
            self.state = HandState();
            self.smoothing = 0.6 // suavizacao de movimento;
            self.gesture_buffer: [Gesture] = [];
            self.buffer_size = 5 // estabilidade do gesto;
        funcao process(self, frame: np.ndarray) retorna Tuple[np.ndarray, HandState]:
            // Processa frame da webcam e retorna frame + estado da mao.
            desempacote h, w = frame.shape[:2];
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
            rgb.flags.writeable = false;
            results = self.hands.process(rgb);
            rgb.flags.writeable = true;
            self.state.detected = false;
            if (results.multi_hand_landmarks) {
                /* TODO: for-each Java para hand_lms em results.multi_hand_landmarks */
                    self.state.detected = true;
                    // Converter landmarks para pixels
                    landmarks = [];
                    /* TODO: for-each Java para lm em hand_lms.landmark */
                        px = inteiro(lm.x * w);
                        py = inteiro(lm.y * h);
                        landmarks.append((px, py));
                    self.state.landmarks = landmarks;
                    // Centro da mao (landmark 0 = pulso)
                    if (landmarks) {
                        self.state.prev_center = self.state.center;
                        raw_center = landmarks[0];
                        // Suavizar movimento
                        sx = inteiro(self.smoothing * self.state.center[0] + (1-self.smoothing) * raw_center[0]);
                        sy = inteiro(self.smoothing * self.state.center[1] + (1-self.smoothing) * raw_center[1]);
                        self.state.center = (sx, sy);
                        // Velocidade (pixels por frame)
                        self.state.velocity = (;
                            self.state.center[0] - self.state.prev_center[0],;
                            self.state.center[1] - self.state.prev_center[1],;
                        );
                    // Detectar dedos esticados
                    self.state.fingers_up = self._detect_fingers(landmarks, w, h);
                    // Distancia pinca (polegar vs indicador)
                    if (tamanho(landmarks) >= 9) {
                        thumb_tip = landmarks[4];
                        index_tip = landmarks[8];
                        self.state.pinch_distance = math.hypot(;
                            thumb_tip[0] - index_tip[0],;
                            thumb_tip[1] - index_tip[1],;
                        );
                    // Angulo do pulso (rotacao)
                    if (tamanho(landmarks) >= 5) {
                        wrist = landmarks[0];
                        middle_mcp = landmarks[9];
                        self.state.wrist_angle = math.degrees(math.atan2(;
                            middle_mcp[1] - wrist[1],;
                            middle_mcp[0] - wrist[0],;
                        ));
                    // Classificar gesto
                    gesture = self._classify_gesture();
                    self._buffer_gesture(gesture);
                    self.state.gesture = self._stable_gesture();
                    // Desenhar esqueleto na tela
                    self.mp_draw.draw_landmarks(;
                        frame, hand_lms, self.mp_hands.HAND_CONNECTIONS,;
                    );
            return frame, self.state;
        funcao _detect_fingers(self, lms: List[(inteiro, inteiro)],
                            w: inteiro, h: inteiro) -> [logico]:;
            // Detecta quais dedos estao esticados (True = esticado).
            if (tamanho(lms) < 21) {
                return [false] * 5;
            fingers = [];
            // Polegar: compara x (horizontal) -- diferente dos outros
            // Mao direita: tip.x < ip.x -> esticado
            // Mao esquerda: tip.x > ip.x -> esticado
            thumb_tip = lms[4];
            thumb_ip = lms[3];
            thumb_mcp = lms[2];
            // Usar distancia relativa
            fingers.append(thumb_tip[0] < thumb_ip[0] if lms[0][0] < lms[5][0];
                        else thumb_tip[0] > thumb_ip[0]);
            // Outros 4 dedos: tip.y < pip.y (ponta acima da junta media) = esticado
            tip_pip = [(8,6), (12,10), (16,14), (20,18)];
            /* para cada (tip, pip) em tip_pip: */
                fingers.append(lms[tip][1] < lms[pip][1]);
            return fingers;
        public Gesture _classify_gesture(self) {
            // Classifica gesto baseado nos dedos esticados.
            f = self.state.fingers_up;
            count = soma(f);
            pinch = self.state.pinch_distance < 40 // pixels;
            if (pinch && f[1] && f[2]) {
                return Gesture.PINCH;
            if (count == 0) {
                return Gesture.FIST;
            if (count == 5) {
                return Gesture.OPEN_HAND;
            if (f[1] && ! f[2] && ! f[3] && ! f[4]) {
                return Gesture.POINT;
            if (f[0] && ! f[1] && ! f[2] && ! f[3] && ! f[4]) {
                return Gesture.THUMBS_UP;
            if (f[1] && f[2] && ! f[3] && ! f[4]) {
                return Gesture.PEACE;
            if (f[0] && f[1] && ! f[2] && ! f[3] && ! f[4]) {
                return Gesture.GUN;
            return Gesture.FLAT;
        public void _buffer_gesture(self, gesture: Gesture) {
            // Buffer para estabilizar gesto (evita oscilacao).
            self.gesture_buffer.append(gesture);
            if (tamanho(self.gesture_buffer) > self.buffer_size) {
                self.gesture_buffer.pop(0);
        public Gesture _stable_gesture(self) {
            // Retorna gesto mais comum no buffer (estabilidade).
            if (! self.gesture_buffer) {
                return Gesture.OPEN_HAND;
            {Gesture: inteiro} counts = {};
            /* TODO: for-each Java para g em self.gesture_buffer */
                counts[g] = counts.get(g, 0) + 1;
            return maximo(counts, key=counts.get);
    // ============================================================================
    // 3. UI VIRTUAL (cursor, botoes, objetos)
    // ============================================================================
    public static class VirtualUI {
        // Interface virtual controlada por gestos.
        Elementos:;
        - Cursor: segue a mao;
        - Botoes: clicar com pinca || punho fechado;
        - Slider: arrastar;
        - Objetos: pegar && mover;
        //
        // decorador: @dataclass
        public static class Button {
            x: inteiro; y: inteiro; w: inteiro; h: inteiro;
            label: texto;
            Tuple[inteiro, inteiro, inteiro] color = (100, 100, 100);
            Tuple[inteiro, inteiro, inteiro] hover_color = (0, 255, 0);
            boolean pressed = false;
            Object on_click = null;
        // decorador: @dataclass
        public static class GameObject {
            x: flutuante; y: flutuante; r: inteiro;
            color: Tuple[inteiro, inteiro, inteiro];
            boolean grabbed = false;
            double vx = 0.0;
            double vy = 0.0;
        public void __init__(self, width: inteiro = 640, height: inteiro = 480) {
            self.width = width;
            self.height = height;
            self.buttons: List[VirtualUI.Button] = [];
            self.objects: List[VirtualUI.GameObject] = [];
            self.cursor_pos = (width // 2, height // 2);
            self.cursor_size = 15;
            self.score = 0;
            self.game_mode = "menu"   // menu, catch, paint, free;
        public void setup_menu(self) {
            // Menu principal com botoes.
            self.buttons = [;
                self.Button(50, 100, 200, 60, "PEGAR FRUTAS",;
                            color = (50, 50, 200)),;
                self.Button(50, 200, 200, 60, "PINTAR",;
                            color = (200, 50, 50)),;
                self.Button(50, 300, 200, 60, "LIVRE (teste)",;
                            color = (50, 200, 50)),;
            ];
            self.objects = [];
            self.game_mode = "menu";
        public void setup_catch(self) {
            // Modo pegar frutas: objetos caem, pegar com mao.
            self.objects = [];
            self.score = 0;
            self.buttons = [];
            self.game_mode = "catch";
            // Gerar frutas
            /* TODO: for-each Java para _ em intervalo(5) */
                self._spawn_fruit();
        public void _spawn_fruit(self) {
            // importa random
            self.objects.append(self.GameObject(;
                x = random.uniform(50, self.width - 50),;
                y = random.uniform(-100, -20),;
                r = random.randint(20, 35),;
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),;
            ));
        public void setup_paint(self) {
            // Modo pintar: desenhar com o dedo.
            self.objects = [];
            self.buttons = [];
            self.game_mode = "paint";
            self.paint_points: List[Tuple[inteiro, inteiro, Tuple[inteiro,inteiro,inteiro]]] = [];
        public void setup_free(self) {
            // Modo livre: mover objetos.
            // importa random
            self.objects = [];
            self.buttons = [];
            self.score = 0;
            self.game_mode = "free";
            /* TODO: for-each Java para _ em intervalo(8) */
                self.objects.append(self.GameObject(;
                    x = random.uniform(100, self.width - 100),;
                    y = random.uniform(100, self.height - 100),;
                    r = 30,;
                    color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),;
                ));
        public void update(self, hand: HandState) {
            // Atualiza UI com base no estado da mao.
            if (hand.detected) {
                self.cursor_pos = hand.center;
                if (self.game_mode == "menu") {
                    self._update_menu(hand);
                } else if (self.game_mode == "catch") {
                    self._update_catch(hand);
                } else if (self.game_mode == "paint") {
                    self._update_paint(hand);
                } else if (self.game_mode == "free") {
                    self._update_free(hand);
            } else {
                // Sem mao detectada
                /* TODO: for-each Java para obj em self.objects */
                    obj.grabbed = false;
        public void _update_menu(self, hand: HandState) {
            // Menu: pinca ou punho para clicar.
            click = hand.gesture in (Gesture.PINCH, Gesture.FIST);
            /* TODO: for-each Java para btn em self.buttons */
                desempacote bx, by, bw, bh = btn.x, btn.y, btn.w, btn.h;
                hover = (bx <= self.cursor_pos[0] <= bx + bw &&;
                        by <= self.cursor_pos[1] <= by + bh);
                btn.pressed = hover && click;
                if (btn.pressed && btn.on_click && ! None) {
                    btn.on_click();
        public void _update_catch(self, hand: HandState) {
            // Pegar frutas: punho fecha para agarrar.
            grab = hand.gesture in (Gesture.FIST, Gesture.PINCH);
            /* TODO: for-each Java para obj em self.objects */
                // Fisica (gravidade)
                if (! obj.grabbed) {
                    obj.vy += 0.5 // gravidade;
                    obj.x += obj.vx;
                    obj.y += obj.vy;
                    // Bater no chao
                    if (obj.y + obj.r > self.height) {
                        obj.y = self.height - obj.r;
                        obj.vy *= -0.5 // quica;
                        obj.vx *= 0.9;
                // Colisao com mao
                dist = math.hypot(obj.x - hand.center[0], obj.y - hand.center[1]);
                if (dist < obj.r + 30) {
                    if (grab) {
                        obj.grabbed = true;
                        obj.x = hand.center[0];
                        obj.y = hand.center[1];
                    } else if (obj.grabbed && ! grab) {
                        obj.grabbed = false;
                        obj.vx = hand.velocity[0] * 0.5;
                        obj.vy = hand.velocity[1] * 0.5;
                        self.score += 1;
            // Manter supply de frutas
            while (tamanho(self.objects) < 5) {
                self._spawn_fruit();
        public void _update_paint(self, hand: HandState) {
            // Pintar: apontar para desenhar.
            if (!  hasattr(self, 'paint_points')) {
                self.paint_points = [];
            if (hand.gesture == Gesture.POINT) {
                cor = (;
                    inteiro(hand.center[0] / self.width * 255),;
                    inteiro(hand.center[1] / self.height * 255),;
                    128,;
                );
                self.paint_points.append((hand.center[0], hand.center[1], cor));
                if (tamanho(self.paint_points) > 1000) {
                    self.paint_points.pop(0);
        public void _update_free(self, hand: HandState) {
            // Modo livre: pegar e jogar objetos.
            grab = hand.gesture in (Gesture.FIST, Gesture.PINCH);
            /* TODO: for-each Java para obj em self.objects */
                if (obj.grabbed) {
                    if (! grab) {
                        obj.grabbed = false;
                        obj.vx = hand.velocity[0] * 0.5;
                        obj.vy = hand.velocity[1] * 0.5;
                    } else {
                        hasattr(obj, 'cursor_pos') ? obj.x = hand.cursor_pos[0] : hand.center[0];
                        obj.y = hand.center[1];
                    continue;
                obj.x += obj.vx;
                obj.y += obj.vy;
                obj.vx *= 0.98 // friccao;
                obj.vy *= 0.98;
                // Bordas
                if obj.x < obj.r: obj.x = obj.r; obj.vx *= -0.5;
                if obj.x > self.width - obj.r: obj.x = self.width - obj.r; obj.vx *= -0.5;
                if obj.y < obj.r: obj.y = obj.r; obj.vy *= -0.5;
        funcao render(self, frame: np.ndarray, hand: HandState) retorna np.ndarray:
            // Desenha UI no frame.
            // Cursor
            if (hand.detected) {
                color = self._gesture_color(hand.gesture);
                cv2.circle(frame, self.cursor_pos, self.cursor_size, color, -1);
                cv2.circle(frame, self.cursor_pos, self.cursor_size + 5, color, 1);
                // Label do gesto
                label = hand.gesture.value[0];
                cv2.putText(frame, label, (self.cursor_pos[0] + 20, self.cursor_pos[1]),;
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2);
            // Botoes
            /* TODO: for-each Java para btn em self.buttons */
                color = btn.hover_color if (;
                    btn.x <= self.cursor_pos[0] <= btn.x + btn.w &&;
                    btn.y <= self.cursor_pos[1] <= btn.y + btn.h && hand.detected;
                ) else btn.color;
                if (btn.pressed) {
                    color = (255, 255, 255);
                cv2.rectangle(frame, (btn.x, btn.y), (btn.x + btn.w, btn.y + btn.h), color, -1);
                cv2.putText(frame, btn.label, (btn.x + 10, btn.y + 40),;
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2);
            // Objetos
            /* TODO: for-each Java para obj em self.objects */
                cv2.circle(frame, (inteiro(obj.x), inteiro(obj.y)), obj.r, obj.color, -1);
                if (obj.grabbed) {
                    cv2.circle(frame, (inteiro(obj.x), inteiro(obj.y)), obj.r + 5, (0, 255, 0), 2);
            // Pintura
            if (self.game_mode == "paint"  &&  hasattr(self, 'paint_points')) {
                /* para i, (px, py, pcolor) in enumere(self.paint_points): */
                    cv2.circle(frame, (px, py), 5, pcolor, -1);
                    if (i > 0) {
                        cv2.line(frame, self.paint_points[i-1][:2], (px, py), pcolor, 3);
            // HUD
            hud_lines = [;
                "Modo: {self.game_mode}",;
                "Gesto: {hand.gesture.value[0] if hand.detected else '---'}",;
                "Score: {self.score}",;
                "Objetos: {len(self.objects)}",;
            ];
            /* para cada (i, line) em enumere(hud_lines): */
                cv2.putText(frame, line, (10, 25 * (i + 1)),;
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1);
            // Instrucoes
            instr = {
                "menu": "PINCA || PUNHO para clicar. ESC sai.",;
                "catch": "PUNHO FECHADO para agarrar frutas.",;
                "paint": "APONTAR para desenhar. PINCA para apagar.",;
                "free": "PUNHO para pegar. ARRASTAR para jogar.",;
            };
            cv2.putText(frame, instr.get(self.game_mode, ""),;
                        (10, self.height - 15),;
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1);
            return frame;
        funcao _gesture_color(self, gesture: Gesture) retorna Tuple[inteiro, inteiro, inteiro]:
            colors = {
                Gesture.FIST: (0, 0, 255), // vermelho;
                Gesture.OPEN_HAND: (0, 255, 0), // verde;
                Gesture.POINT: (255, 0, 0), // azul;
                Gesture.PINCH: (0, 255, 255), // amarelo;
                Gesture.THUMBS_UP: (0, 200, 0), // verde escuro;
                Gesture.PEACE: (200, 0, 200), // roxo;
                Gesture.FLAT: (100, 100, 100), // cinza;
            };
            return colors.get(gesture, (255, 255, 255));
    // ============================================================================
    // 4. APLICACAO PRINCIPAL
    // ============================================================================
    public static class HandTrackingApp {
        // Aplicacao de webcam + hand tracking para games.
        COMO RODAR:;
            python3 open_hand_tracking.py;
        COMO USAR:;
            1. Permita acesso a webcam;
            2. Mostre a mao para a camera;
            3. Faca gestos:;
            - PINCA || PUNHO = clicar;
            - APONTAR = desenhar (modo pintura);
            - PUNHO = agarrar (modo pegar/jogar);
            4. ESC para sair;
            5. 'M' para voltar ao menu;
            6. 'C' limpa tela (modo pintura);
        INTEGRACAO COM OPENREPUBLIC:;
        - OpenGames: minigames controlados por mao (P1: sem controle caro);
        - OpenMartialArts: treino de golpes com tracking;
        - OpenGamesRealistic: simulador medico por gesto;
        - OpenLegoStudio: programar apontando (sem teclado);
        - OpenHealth: reabilitacao motora em casa;
        - P1 anti-elitismo: QUALQUER webcam funciona. Sem Kinect. Sem Leap Motion.;
        //
        public void __init__(self, camera_index: inteiro = 0) {
            self.tracker = HandTracker(max_hands=2);
            self.ui = VirtualUI();
            self.camera_index = camera_index;
            self.running = false;
        public void run(self) {
            // Roda a aplicacao.
            cap = cv2.VideoCapture(self.camera_index);
            if (! cap.isOpened()) {
                System.out.println("ERRO: webcam ! disponivel");
                return null;
            // Configurar camera
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640);
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480);
            self.ui.setup_menu();
            self.running = true;
            System.out.println("=" * 50);
            System.out.println("  OpenHandTracking");
            System.out.println("  Mostre a mao para a camera.");
            System.out.println("  PINCA/PUNHO = clicar. ESC = sair. M = menu.");
            System.out.println("=" * 50);
            prev_time = time.time();
            while (self.running) {
                desempacote ret, frame = cap.read();
                if (! ret) {
                    break;
                // Espelhar horizontalmente (selfie)
                frame = cv2.flip(frame, 1);
                // Processar hand tracking
                desempacote frame, hand = self.tracker.process(frame);
                // Atualizar UI
                self.ui.update(hand);
                // Renderizar
                frame = self.ui.render(frame, hand);
                // FPS
                curr_time = time.time();
                fps = 1.0 / maximo(curr_time - prev_time, 0.001);
                prev_time = curr_time;
                cv2.putText(frame, "FPS: {fps:.0f}", (self.ui.width - 80, 25),;
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1);
                cv2.imshow("OpenHandTracking", frame);
                // Teclas
                key = cv2.waitKey(1) & 0xFF;
                if key = = 27: // ESC;
                    self.running = false;
                } else if (key == ord('m')  ||  key == ord('M')) {
                    self.ui.setup_menu();
                } else if (key == ord('c')  ||  key == ord('C')) {
                    if (hasattr(self.ui, 'paint_points')) {
                        self.ui.paint_points = [];
            cap.release();
            cv2.destroyAllWindows();
    // ============================================================================
    // 5. MENU CALLBACKS (ligar botoes a modos)
    // ============================================================================
    public void main() {
        app = HandTrackingApp();
        // Ligar botoes do menu aos modos
        app.ui.buttons[0].on_click = () -> app.ui.setup_catch();
        app.ui.buttons[1].on_click = () -> app.ui.setup_paint();
        app.ui.buttons[2].on_click = () -> app.inverse();
        tente:;
            app.run();
        capture KeyboardInterrupt:;
            // (sem operacao)
        finalmente:;
            cv2.destroyAllWindows();
    if (__name__ == "__main__") {
        main();
}
