# OpenLibrasBridge -- Ponte Bidirecional entre Libras e Portugues

**Arquivo original:** `open-republic/core/open_libras_bridge.py`

**Descricao:** ================================================================
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

---

```portugol

// !/usr/bin/env python3
// 
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
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set, Callable de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict, deque de collections
// importa hashlib
// importa time
// importa random


// ============================================================================
// 1. ENUMERACOES DO SISTEMA LIBRAS
// ============================================================================

classe TranslationDirection herda de Enum:
    // Direcoes de traducao suportadas pelo sistema.
    LIBRAS_TO_TEXT <- "libras_para_texto"
    TEXT_TO_LIBRAS <- "texto_para_libras"
    LIBRAS_TO_AUDIO <- "libras_para_audio"
    AUDIO_TO_LIBRAS <- "audio_para_libras"


classe SignCategory herda de Enum:
    // Categorias de sinais em Libras.
    ALPHABET <- "alfabeto"
    NUMBERS <- "numeros"
    GREETINGS <- "cumprimentos"
    QUESTIONS <- "perguntas"
    VERBS <- "verbos"
    NOUNS <- "substantivos"
    ADJECTIVES <- "adjetivos"
    EMOTIONS <- "emocoes"
    DAILY_LIFE <- "vida_diaria"
    PRONOUNS <- "pronomes"


classe AvatarStyle herda de Enum:
    // Estilos visuais do avatar que sinaliza em Libras.
    REALISTIC_HUMAN <- "humano_realista"
    CARTOON <- "desenho_animado"
    ABSTRACT <- "abstrato"
    MINIMAL <- "minimalista"


classe RecognitionConfidence herda de Enum:
    // Nivel de confianca do reconhecimento de sinais.
    HIGH <- "alta"
    MEDIUM <- "media"
    LOW <- "baixa"
    FAILED <- "falha"


classe HandDominance herda de Enum:
    // Dominancia manual do usuario (importante para reconhecimento).
    RIGHT <- "direita"
    LEFT <- "esquerda"
    AMBIDEXTROUS <- "ambidestro"


classe FacialExpression herda de Enum:
    // Expressoes faciais obrigatorias em Libras.
    NEUTRAL <- "neutra"
    HAPPY <- "feliz"
    SAD <- "triste"
    ANGRY <- "irritado"
    SURPRISED <- "surpreso"
    QUESTIONING <- "questionadora"
    NEGATION <- "negacao"


// ============================================================================
// 2. DATACLASSES PRINCIPAIS
// ============================================================================

// decorador: @dataclass
classe LibrasSign:
    // Representacao completa de um sinal em Libras.
    sign_id: str
    portuguese_meaning: str
    sign_category: SignCategory
    handshape: str                     // configuracao da mao (ex: "A", "B", "C", "5", "S")
    location: str                      // local do corpo (ex: "frente_peito", "queixo", "testa")
    movement: str                      // tipo de movimento (ex: "circular", "linear_frente", "zigzag")
    palm_orientation: str              // orientacao da palma (ex: "para_cima", "para_baixo", "para_frente")
    facial_expr: FacialExpression
    requires_two_hands: bool
    description: str                   // descricao didatica do sinal


// decorador: @dataclass
classe TranslationResult:
    // Resultado de uma traducao realizada pelo sistema.
    direction: TranslationDirection
    input_text: str
    output_text: str
    confidence: RecognitionConfidence
    signs_detected: List[LibrasSign]
    processing_time_ms: float
    declare avatar_animation_url: Optional[str]  <- nulo


// decorador: @dataclass
classe AvatarConfig:
    // Configuracao visual e comportamental do avatar.
    declare style: AvatarStyle  <- AvatarStyle.REALISTIC_HUMAN
    declare skin_tone: str  <- "#E8BEAC"  // tom de pele padrao
    declare clothing: str  <- "camiseta_branca"
    declare background: str  <- "neutro_claro"
    declare speed: float  <- 1.0  // velocidade dos sinais (0.5 a 2.0)
    declare show_facial_expressions: bool  <- VERDADEIRO
    declare show_hand_details: bool  <- VERDADEIRO


// ============================================================================
// 3. CATALOGO DE SINAIS EM LIBRAS (20+ sinais comuns)
// ============================================================================

declare LIBRAS_SIGNS: List[LibrasSign]  <- [
    LibrasSign("ola", "ola", SignCategory.GREETINGS, "B", "frente_peito", "ondulacao", "para_frente", FacialExpression.HAPPY, FALSO, "Mao aberta em B, movimento de aceno lateral na altura do peito."),
    LibrasSign("obrigado", "obrigado", SignCategory.GREETINGS, "A", "queixo", "toque_queixo", "para_frente", FacialExpression.HAPPY, FALSO, "Mao em A, toque no queixo e movimento para frente."),
    LibrasSign("por_favor", "por favor", SignCategory.GREETINGS, "B", "frente_peito", "circular_pequeno", "para_cima", FacialExpression.NEUTRAL, FALSO, "Mao aberta, pequeno circulo na frente do peito."),
    LibrasSign("sim", "sim", SignCategory.QUESTIONS, "S", "frente_peito", "nod_vertical", "para_frente", FacialExpression.NEUTRAL, FALSO, "Mao em S, movimento de confirmacao vertical."),
    LibrasSign("nao", "nao", SignCategory.QUESTIONS, "G", "frente_peito", "balanco_lateral", "para_frente", FacialExpression.NEGATION, FALSO, "Indicador esticado, balanco lateral da cabeca."),
    LibrasSign("agua", "agua", SignCategory.DAILY_LIFE, "W", "queixo", "toque_queixo", "para_baixo", FacialExpression.NEUTRAL, FALSO, "Mao em W, toque no queixo representando agua."),
    LibrasSign("comida", "comida", SignCategory.DAILY_LIFE, "C", "boca", "toque_boca", "para_frente", FacialExpression.NEUTRAL, FALSO, "Mao em C, movimento em direcao a boca."),
    LibrasSign("casa", "casa", SignCategory.NOUNS, "C", "frente_peito", "telhado", "para_baixo", FacialExpression.NEUTRAL, VERDADEIRO, "Duas maos em C formando telhado de casa."),
    LibrasSign("familia", "familia", SignCategory.NOUNS, "F", "frente_peito", "circulo_grande", "para_frente", FacialExpression.HAPPY, VERDADEIRO, "Duas maos em F girando em circulo representando uniao."),
    LibrasSign("amor", "amor", SignCategory.EMOTIONS, "A", "frente_peito", "cruzado", "para_frente", FacialExpression.HAPPY, VERDADEIRO, "Duas maos em A cruzadas sobre o coracao."),
    LibrasSign("trabalho", "trabalho", SignCategory.VERBS, "T", "frente_peito", "martelo", "para_baixo", FacialExpression.NEUTRAL, FALSO, "Mao em T simulando martelar."),
    LibrasSign("escola", "escola", SignCategory.NOUNS, "E", "testa", "toque_testa", "para_frente", FacialExpression.NEUTRAL, FALSO, "Mao em E, toque na testa representando conhecimento."),
    LibrasSign("medico", "medico", SignCategory.NOUNS, "M", "pulso", "pulso_pulso", "para_frente", FacialExpression.NEUTRAL, FALSO, "Mao em M medindo pulso como medico."),
    LibrasSign("ajuda", "ajuda", SignCategory.VERBS, "A", "frente_peito", "empurra", "para_cima", FacialExpression.NEUTRAL, VERDADEIRO, "Uma mao empurra a outra para cima pedindo ajuda."),
    LibrasSign("nome", "nome", SignCategory.QUESTIONS, "N", "frente_peito", "toque_peito", "para_frente", FacialExpression.QUESTIONING, FALSO, "Mao em N, toque no peito perguntando nome."),
    LibrasSign("quantos_anos", "quantos anos", SignCategory.QUESTIONS, "Q", "queixo", "toque_queixo", "para_frente", FacialExpression.QUESTIONING, FALSO, "Mao em Q no queixo perguntando idade."),
    LibrasSign("bom_dia", "bom dia", SignCategory.GREETINGS, "B", "testa", "toque_testa", "para_frente", FacialExpression.HAPPY, FALSO, "Mao em B, toque na testa e movimento de cumprimento."),
    LibrasSign("boa_noite", "boa noite", SignCategory.GREETINGS, "B", "testa", "toque_testa", "para_baixo", FacialExpression.NEUTRAL, FALSO, "Mao em B, toque na testa e movimento descendente."),
    LibrasSign("desculpa", "desculpa", SignCategory.EMOTIONS, "D", "frente_peito", "circulo_peito", "para_frente", FacialExpression.SAD, FALSO, "Mao em D, circulo pequeno no peito pedindo desculpas."),
    LibrasSign("feliz", "feliz", SignCategory.EMOTIONS, "F", "frente_peito", "circulo_feliz", "para_frente", FacialExpression.HAPPY, FALSO, "Mao em F, movimento circular alegre no peito."),
    LibrasSign("eu", "eu", SignCategory.PRONOUNS, "I", "peito", "toque_peito", "para_frente", FacialExpression.NEUTRAL, FALSO, "Indicador apontando para o proprio peito."),
    LibrasSign("voce", "voce", SignCategory.PRONOUNS, "Y", "frente", "aponta_frente", "para_frente", FacialExpression.NEUTRAL, FALSO, "Indicador apontando para a pessoa a frente."),
    LibrasSign("obrigado_muito", "muito obrigado", SignCategory.GREETINGS, "A", "queixo", "toque_repetido", "para_frente", FacialExpression.HAPPY, FALSO, "Toque repetido no queixo com expressao de gratidao."),
]


// ============================================================================
// 4. CLASSES PRINCIPAIS
// ============================================================================

classe LibrasRecognizer:
    // Reconhece sinais de Libras a partir de frames de camera.

    funcao __init__(self, dominant_hand: HandDominance = HandDominance.RIGHT):
        self.dominant_hand = dominant_hand
        self.calibrated = FALSO
        self.last_sequence: List[LibrasSign] = []
        self.confidence_threshold = 0.75

    funcao calibrate(self, user_hand_data: Dict[str, Any]) retorna bool:
        // Calibra o reconhecedor com as caracteristicas da mao do usuario.
        print("[LibrasRecognizer] Calibrando para usuario...")
        self.calibrated = VERDADEIRO
        retorne VERDADEIRO

    funcao set_dominant_hand(self, hand: HandDominance) retorna None:
        // Define a mao dominante do usuario.
        self.dominant_hand = hand
        print(f"[LibrasRecognizer] Mao dominante definida: {hand.value}")

    funcao process_frame(self, frame_data: Any) retorna List[LibrasSign]:
        // Processa um frame da camera e retorna sinais detectados.
        // Simulacao de processamento de frame
        detected <- []
        se random.random() > 0.3 entao:
            detected.append(random.choice(LIBRAS_SIGNS[:10]))
        retorne detected

    funcao recognize_sequence(self, frames: List[Any], max_duration_ms: int = 5000) retorna Tuple[List[LibrasSign], RecognitionConfidence]:
        // Reconhece uma sequencia completa de sinais.
        start <- time.time()
        sequence <- []
        para cada _ em range(random.randint(2, 5)):
            sequence.append(random.choice(LIBRAS_SIGNS))
        elapsed <- (time.time() - start) * 1000
        confidence <- RecognitionConfidence.HIGH if elapsed < 3000 else RecognitionConfidence.MEDIUM
        self.last_sequence = sequence
        retorne sequence, confidence


classe LibrasTranslator:
    // Traduz entre sinais de Libras e texto em Portugues.

    funcao __init__(self):
        self.sign_index = {s.sign_id: s for s in LIBRAS_SIGNS}
        self.text_index = {s.portuguese_meaning: s for s in LIBRAS_SIGNS}

    funcao signs_to_text(self, signs: List[LibrasSign]) retorna str:
        // Converte uma sequencia de sinais em texto em Portugues.
        se NAO  signs entao:
            retorne ""
        words <- []
        para cada sign em signs:
            se sign.sign_id == "ola" entao:
                words.append("Ola")
            senao se sign.sign_id == "obrigado" entao:
                words.append("Obrigado")
            senao se sign.sign_id == "por_favor" entao:
                words.append("Por favor")
            senao se sign.sign_id == "sim" entao:
                words.append("Sim")
            senao se sign.sign_id == "nao" entao:
                words.append("Nao")
            senao:
                words.append(sign.portuguese_meaning.capitalize())
        retorne " ".join(words) + "."

    funcao text_to_signs(self, text: str) retorna List[LibrasSign]:
        // Converte texto em Portugues para sequencia de sinais.
        words <- text.lower().replace(".", "").replace(",", "").split()
        signs <- []
        para cada w em words:
            se w in ["ola", "oi"] entao:
                signs.append(self.sign_index.get("ola"))
            senao se w in ["obrigado", "agradecido"] entao:
                signs.append(self.sign_index.get("obrigado"))
            senao se w in ["por", "favor"] entao:
                signs.append(self.sign_index.get("por_favor"))
            senao se w == "sim" entao:
                signs.append(self.sign_index.get("sim"))
            senao se w == "nao" entao:
                signs.append(self.sign_index.get("nao"))
            senao se w in self.sign_index entao:
                signs.append(self.sign_index[w])
            senao:
                // fallback: usa sinal generico de "nome"
                signs.append(self.sign_index.get("nome"))
        retorne [s for s in signs if s]

    funcao translate_realtime(self, input_data: Any, direction: TranslationDirection) retorna TranslationResult:
        // Traduz em tempo real com metricas.
        start <- time.time()
        se direction == TranslationDirection.LIBRAS_TO_TEXT entao:
            signs <- input_data if isinstance(input_data, list) else []
            output <- self.signs_to_text(signs)
        senao:
            text <- str(input_data)
            signs <- self.text_to_signs(text)
            output <- text
        elapsed <- (time.time() - start) * 1000
        retorne TranslationResult(
            direction <- direction,
            input_text <- str(input_data)[:100],
            output_text <- output,
            confidence <- RecognitionConfidence.HIGH,
            signs_detected <- signs,
            processing_time_ms <- elapsed
        )


classe LibrasAvatar:
    // Avatar 3D que sinaliza em Libras.

    funcao __init__(self, config: Optional[AvatarConfig] = None):
        self.config = config  OU  AvatarConfig()
        self.current_animation = nulo

    funcao set_style(self, style: AvatarStyle) retorna None:
        // Altera o estilo visual do avatar.
        self.config.style = style
        print(f"[LibrasAvatar] Estilo alterado para: {style.value}")

    funcao sign_text(self, text: str) retorna str:
        // Gera animacao para um texto.
        signs <- LibrasTranslator().text_to_signs(text)
        retorne self.animate_sequence(signs)

    funcao animate_sequence(self, signs: List[LibrasSign]) retorna str:
        // Anima uma sequencia de sinais e retorna URL da animacao.
        animation_id <- hashlib.md5(str([s.sign_id for s in signs]).encode()).hexdigest()[:12]
        url <- f"https://avatar.openrepublic.org/libras/{self.config.style.value}/{animation_id}.mp4"
        self.current_animation = url
        print(f"[LibrasAvatar] Animando {len(signs)} sinais -> {url}")
        retorne url

    funcao get_animation(self) retorna Optional[str]:
        // Retorna a ultima animacao gerada.
        retorne self.current_animation


classe LibrasBridge:
    // Orquestrador principal do sistema de traducao Libras <-> Portugues.

    def __init__(self, recognizer: Optional[LibrasRecognizer] = nulo,
                 declare translator: Optional[LibrasTranslator]  <- nulo,
                 declare avatar: Optional[LibrasAvatar]  <- nulo):
        self.recognizer = recognizer  OU  LibrasRecognizer()
        self.translator = translator  OU  LibrasTranslator()
        self.avatar = avatar  OU  LibrasAvatar()
        self.session_active = FALSO
        self.conversation_log: List[TranslationResult] = []

    funcao translate_from_libras(self, camera_frames: List[Any]) retorna TranslationResult:
        // Traduz sinais capturados pela camera para texto.
        desempacote signs, confidence <- self.recognizer.recognize_sequence(camera_frames)
        result <- self.translator.translate_realtime(signs, TranslationDirection.LIBRAS_TO_TEXT)
        result.confidence = confidence
        self.conversation_log.append(result)
        retorne result

    funcao translate_to_libras(self, text_or_audio: str) retorna TranslationResult:
        // Traduz texto ou audio para sinais e aciona o avatar.
        result <- self.translator.translate_realtime(text_or_audio, TranslationDirection.TEXT_TO_LIBRAS)
        animation <- self.avatar.animate_sequence(result.signs_detected)
        result.avatar_animation_url = animation
        self.conversation_log.append(result)
        retorne result

    funcao start_session(self) retorna None:
        // Inicia uma sessao de conversacao.
        self.session_active = VERDADEIRO
        print("[LibrasBridge] Sessao iniciada. Aguardando interacao...")

    funcao conversation_mode(self, duration_seconds: int = 60) retorna List[TranslationResult]:
        // Modo de conversacao automatica por tempo determinado.
        results <- []
        end_time <- time.time() + duration_seconds
        enquanto time.time() < end_time  E  self.session_active faca:
            // Simula interacao bidirecional
            se random.random() > 0.5 entao:
                r <- self.translate_from_libras([nulo] * 5)
            senao:
                r <- self.translate_to_libras(random.choice(["ola", "obrigado", "agua", "amor"]))
            results.append(r)
            time.sleep(0.3)
        retorne results


// ============================================================================
// 5. FUNCOES FABRICA
// ============================================================================

funcao create_bridge_for_deaf() retorna LibrasBridge:
    // Cria ponte otimizada para usuario surdo (foco em reconhecimento e avatar).
    rec <- LibrasRecognizer(HandDominance.RIGHT)
    avatar <- LibrasAvatar(AvatarConfig(style=AvatarStyle.REALISTIC_HUMAN, speed=0.9))
    retorne LibrasBridge(rec, LibrasTranslator(), avatar)


funcao create_bridge_for_hearing() retorna LibrasBridge:
    // Cria ponte otimizada para ouvinte (foco em geracao de sinais).
    avatar <- LibrasAvatar(AvatarConfig(style=AvatarStyle.CARTOON, speed=1.1))
    retorne LibrasBridge(LibrasRecognizer(), LibrasTranslator(), avatar)


funcao create_bridge_for_classroom() retorna LibrasBridge:
    // Cria ponte para ambiente escolar com avatar minimalista.
    avatar <- LibrasAvatar(AvatarConfig(style=AvatarStyle.MINIMAL, speed=0.8, show_facial_expressions=VERDADEIRO))
    retorne LibrasBridge(LibrasRecognizer(HandDominance.AMBIDEXTROUS), LibrasTranslator(), avatar)


// ============================================================================
// 6. CENARIOS DE USO REAL
// ============================================================================

funcao scenario_ordering_food() retorna None:
    // Cenario: Pedindo comida em restaurante.
    print("\n=== CENARIO: PEDINDO COMIDA NO RESTAURANTE ===")
    bridge <- create_bridge_for_deaf()
    bridge.start_session()
    // Surdo sinaliza
    result1 <- bridge.translate_from_libras([nulo] * 3)
    print(f"Surdo sinalizou: {result1.output_text}")
    // Garcom responde
    result2 <- bridge.translate_to_libras("O que deseja pedir?")
    print(f"Garcom: {result2.output_text} -> Avatar: {result2.avatar_animation_url}")


funcao scenario_doctor_visit() retorna None:
    // Cenario: Consulta medica.
    print("\n=== CENARIO: CONSULTA MEDICA ===")
    bridge <- create_bridge_for_hearing()
    result <- bridge.translate_to_libras("Onde esta doendo?")
    print(f"Medico pergunta via avatar: {result.avatar_animation_url}")
    result2 <- bridge.translate_from_libras([nulo] * 4)
    print(f"Paciente responde: {result2.output_text}")


funcao scenario_job_interview() retorna None:
    // Cenario: Entrevista de emprego.
    print("\n=== CENARIO: ENTREVISTA DE EMPREGO ===")
    bridge <- create_bridge_for_classroom()
    bridge.translate_to_libras("Fale sobre sua experiencia anterior.")
    bridge.translate_from_libras([nulo] * 6)


funcao scenario_emergency_libras() retorna None:
    // Cenario: Emergencia (bombeiros, policia, SAMU).
    print("\n=== CENARIO: EMERGENCIA ===")
    bridge <- create_bridge_for_deaf()
    bridge.translate_from_libras([nulo] * 2)
    bridge.translate_to_libras("A ajuda esta a caminho. Fique calmo.")


// ============================================================================
// 7. FUNCAO DEMO
// ============================================================================

funcao demo() retorna None:
    // Executa todos os cenarios de demonstracao.
    print("=" * 60)
    print("DEMO DO SISTEMA OPENLIBRASBRIDGE")
    print("=" * 60)

    // Demonstra catalogo
    print(f"\nCatalogo possui {len(LIBRAS_SIGNS)} sinais cadastrados.")
    print("Exemplos:", ", ".join([s.portuguese_meaning for s in LIBRAS_SIGNS[:5]]))

    // Executa todos os cenarios
    scenario_ordering_food()
    scenario_doctor_visit()
    scenario_job_interview()
    scenario_emergency_libras()

    // Demonstra modo conversacao
    print("\n=== MODO CONVERSACAO (5 segundos) ===")
    bridge <- create_bridge_for_deaf()
    bridge.start_session()
    results <- bridge.conversation_mode(5)
    print(f"Interacoes registradas: {len(results)}")

    print("\nDemo concluida com sucesso!")


se __name__ == "__main__" entao:
    demo()
```
