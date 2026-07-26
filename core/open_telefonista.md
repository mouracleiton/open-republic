# OpenTelefonista -- O Sistema Como Conversa Humana

**Arquivo original:** `open-republic/core/open_telefonista.py`

**Descricao:** ===================================================
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
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol

// !/usr/bin/env python3
// 
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

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set, Callable de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict, deque de collections
// importa hashlib
// importa time


// ============================================================================
// 1. PERSONALIDADE DA TELEFONISTA
// ============================================================================

classe TelefonistaPersonality herda de Enum:
    // Personalidades disponiveis da telefonista.
    GENTLE <- "gentil"  // calma, pausada, maternamente
    CHEERFUL <- "alegre"  // energica, motivadora
    SERIOUS <- "seria"  // direta, profissional
    FRIENDLY <- "amiga"  // casual, como uma amiga
    FORMAL <- "formal"  // educada, cerimoniosa
    PLAYFUL <- "brincalhona"  // humor, leveza
    PROTECTIVE <- "protetora"  // foca em seguranca
    MINIMAL <- "minimal"  // so o necessario, poucas palavras


classe EmotionalState herda de Enum:
    // Estado emocional detectado ou reportado pelo usuario.
    HAPPY <- "feliz"
    CALM <- "calmo"
    FOCUSED <- "focado"
    TIRED <- "cansado"
    STRESSED <- "estressado"
    ANXIOUS <- "ansioso"
    SAD <- "triste"
    ANGRY <- "irritado"
    OVERWHELMED <- "sobrecarregado"
    NEUTRAL <- "neutro"


classe ConversationMode herda de Enum:
    // Modo de conversa.
    DIALOGUE <- "dialogo"  // conversa bidirecional natural
    DICTATION <- "ditado"  // usuario dita, sistema executa
    NARRATION <- "narracao"  // sistema narrativa o que acontece
    EMERGENCY <- "emergencia"  // prioridade maxima, voz firme
    WHISPER <- "sussurro"  // resposta discreta (surdo = haptico)
    SILENT <- "silencioso"  // so visual/haptico, sem voz
    CO_DRIVER <- "copiloto"  // guia o usuario no mundo fisico
    TEACHER <- "professora"  // ensina enquanto faz


// decorador: @dataclass
classe TelefonistaConfig:
    // Configuracao da personalidade da telefonista.
    declare name: str  <- "Iara"  // nome da telefonista
    declare personality: TelefonistaPersonality  <- TelefonistaPersonality.GENTLE
    declare voice_id: str  <- "pt-BR-FemaleA"  // voz TTS
    declare speech_rate: float  <- 1.0  // velocidade da fala
    declare formality: float  <- 0.3  // 0=informal, 1=formal
    declare verbosity: float  <- 0.5  // 0=curto, 1=detalhado
    declare humor_enabled: bool  <- VERDADEIRO  // usa humor quando apropriado
    declare proactive: float  <- 0.3  // 0=so responde, 1=antecipa
    declare language: str  <- "pt-BR"
    declare respects_silence: bool  <- VERDADEIRO  // OpenSilencePolicy
    declare interruptible: bool  <- VERDADEIRO  // usuario pode interromper
    declare emotional_adaptation: bool  <- VERDADEIRO  // adapta ao humor do usuario

    funcao adapt_to_emotion(self, emotion: EmotionalState) retorna None:
        // Adapta comportamento ao estado emocional.
        se emotion in (EmotionalState.STRESSED, EmotionalState.ANXIOUS) entao:
            self.speech_rate = 0.85       // fala mais devagar
            self.verbosity = 0.3          // menos palavras
            self.humor_enabled = FALSO    // sem humor
            self.personality = TelefonistaPersonality.GENTLE
        senao se emotion == EmotionalState.TIRED entao:
            self.speech_rate = 0.9
            self.verbosity = 0.3
            self.proactive = 0.1          // nao antecipa
        senao se emotion == EmotionalState.HAPPY entao:
            self.humor_enabled = VERDADEIRO
            self.speech_rate = 1.1
        senao se emotion == EmotionalState.OVERWHELMED entao:
            self.verbosity = 0.1          // minimo de palavras
            self.speech_rate = 0.8
            self.proactive = 0.0
        senao se emotion == EmotionalState.FOCUSED entao:
            self.verbosity = 0.2          // direta, sem enrolacao
            self.humor_enabled = FALSO
            self.proactive = 0.1


// ============================================================================
// 2. CAPACIDADES DO SMARTPHONE COMO CORPO EXTENDIDO
// ============================================================================

classe SensorType herda de Enum:
    // Sensores do smartphone/hardware que captam o mundo.
    CAMERA_REAR <- "camera_traseira"  // camera principal
    CAMERA_FRONT <- "camera_frontal"  // camera selfie
    MICROPHONE <- "microfone"  // captura audio
    GPS <- "gps"  // localizacao
    ACCELEROMETER <- "acelerometro"  // movimento/queda
    GYROSCOPE <- "giroscopio"  // rotacao/orientacao
    COMPASS <- "bussola"  // direcao
    BAROMETER <- "barometro"  // altitude/pressao
    THERMOMETER <- "termometro"  // temperatura
    HUMIDITY <- "umidade"  // umidade do ar
    LIGHT <- "luminosidade"  // sensor de luz
    PROXIMITY <- "proximidade"  // distancia de objetos
    LIDAR <- "lidar"  // profundidade (iPhone Pro)
    TOF <- "tempo_de_voo"  // depth sensing
    HEART_RATE <- "frequencia_cardiaca"  // smartwatch
    SPO2 <- "oxigenio"  // smartwatch
    SKIN_TEMP <- "temperatura_pele"  // smartwatch
    NFC <- "nfc"  // proximidade de tags
    BLUETOOTH_BEACON <- "beacon_bluetooth"  // triangulacao indoor
    CELL_SIGNAL <- "sinal_celular"  // triangulacao GSM


classe WorldPerception herda de Enum:
    // O que o sistema percebe do mundo atraves dos sensores.
    // VISAO
    COLOR_DETECTION <- "deteccao_cor"  // daltonico ve a cor real
    TEXT_RECOGNITION <- "reconhecimento_texto"  // OCR -- le textos do mundo
    OBJECT_DETECTION <- "deteccao_objetos"  // identifica objetos
    FACE_RECOGNITION <- "reconhecimento_facial"  // reconhece pessoas
    OBSTACLE_DETECTION <- "deteccao_obstaculos"  // cego: obstaculo na frente
    CROSSWALK_DETECTION <- "deteccao_faixa"  // faixa de pedestre
    TRAFFIC_LIGHT <- "semaforo"  // cor do semaforo
    SIGN_RECOGNITION <- "reconhecimento_placas"  // placas de transito
    DOCUMENT_SCAN <- "escaneamento_documento"  // digitaliza papel
    MONEY_RECOGNITION <- "reconhecimento_cedula"  // cego: qual nota e?
    PRODUCT_LABEL <- "rotulo_produto"  // le rotulo no mercado
    // AUDICAO
    SOUND_CLASSIFICATION <- "classificacao_som"  // o que e esse som?
    SPEAKER_RECOGNITION <- "reconhecimento_voz"  // quem esta falando?
    MUSIC_RECOGNITION <- "reconhecimento_musica"  // que musica e?
    SPEECH_TO_TEXT <- "fala_para_texto"  // transcreve conversa
    AMBIENT_NOISE <- "ruido_ambiente"  // nivel de ruido
    DOORBELL <- "campainha"  // alguem na porta
    ALARM_SOUND <- "alarme"  // alarme de emergencia
    SIREN <- "sirene"  // policia/bombeiro/ambulancia
    BABY_CRYING <- "bebe_chorando"  // bebe chorando
    DOG_BARKING <- "cachorro_latindo"  // cao latindo
    // LOCALIZACAO
    GPS_LOCATION <- "localizacao_gps"  // onde estou
    INDOOR_LOCATION <- "localizacao_indoor"  // dentro de predio
    DIRECTION_FACING <- "direcao"  // para onde olho
    ALTITUDE <- "altitude"  // altura/aterrissagem
    SPEED <- "velocidade"  // andando/correndo/parado
    NEARBY_PLACES <- "lugares_proximos"  // hospitais, farmacias
    GEOCODING <- "geocoding"  // endereco <-> coordenada
    LOST_CHILD <- "crianca_perdida"  // geolocalizacao de criancas
    // BIOMETRIA
    FALL_DETECTION <- "deteccao_queda"  // caiu!
    HEART_ANOMALY <- "anomalia_cardiaca"  // coracao irregular
    STRESS_DETECTION <- "deteccao_stress"  // estressado pelo batimento
    SEIZURE_PREDICTION <- "previsao_crise"  // epilepsia
    TREMOR_DETECTION <- "deteccao_tremor"  // Parkinson
    POSTURE <- "postura"  // postura corporal
    // AMBIENTE
    TEMPERATURE <- "temperatura_ambiente"  // calor/frio
    AIR_QUALITY <- "qualidade_ar"  // poluicao
    UV_INDEX <- "indice_uv"  // sol forte
    WEATHER <- "clima"  // chuva, sol, vento


// decorador: @dataclass
classe SensorReading:
    // Uma leitura de sensor do mundo fisico.
    sensor: SensorType
    perception: WorldPerception
    value: Any                     // valor capturado
    declare confidence: float  <- 1.0  // 0-1
    declare timestamp: float  <- field(default_factory=time.time)
    declare description: str  <- ""  // descricao humanizada


// ============================================================================
// 3. VISAO COMPUTACIONAL -- Camera como Olhos
// ============================================================================

classe ComputerVisionEngine:
    // 
    Usa a camera do smartphone/oculos para traduzir o mundo visual
    para o usuario. Cada deficiencia tem uma traducao diferente.
    // 

    funcao __init__(self):
        self.active_perceptions: List[WorldPerception] = []
        self.last_readings: deque = deque(maxlen=100)

    funcao process_frame(self, sensor: SensorType, frame_data: Any = None) retorna List[SensorReading]:
        // Processa um frame da camera e gera leituras.
        readings <- []

        // DALTONICO: detecta e nomeia cores
        reading <- SensorReading(
            sensor <- sensor,
            perception <- WorldPerception.COLOR_DETECTION,
            value <- {"color_name": "vermelho", "hex": "#FF0000", "rgb": (255, 0, 0)},
            confidence <- 0.95,
            description <- "Aqui e VERMELHO. A luz do semaforo esta VERMELHA. Pare."
        )
        readings.append(reading)

        // CEGO: detecta obstaculos
        reading <- SensorReading(
            sensor <- sensor,
            perception <- WorldPerception.OBSTACLE_DETECTION,
            value <- {"obstacle": "poste", "distance_m": 2.5, "direction": "frente-esquerda"},
            confidence <- 0.88,
            description <- "Poste a 2.5 metros a frente e a esquerda. Desvie para a direita."
        )
        readings.append(reading)

        // OCR: le texto do mundo
        reading <- SensorReading(
            sensor <- sensor,
            perception <- WorldPerception.TEXT_RECOGNITION,
            value <- {"text": "RESTAURANTE JOAO", "location": "acima da porta"},
            confidence <- 0.92,
            description <- "Placa diz: RESTAURANTE JOAO. Fica acima da porta a frente."
        )
        readings.append(reading)

        // SEMAFORO
        reading <- SensorReading(
            sensor <- sensor,
            perception <- WorldPerception.TRAFFIC_LIGHT,
            value <- {"color": "verde", "action": "siga"},
            confidence <- 0.97,
            description <- "Semaforo VERDE. Pode atravessar."
        )
        readings.append(reading)

        // CEDULA -- cego reconhece dinheiro
        reading <- SensorReading(
            sensor <- sensor,
            perception <- WorldPerception.MONEY_RECOGNITION,
            value <- {"denomination": "R$ 50,00", "color_pattern": "marrom"},
            confidence <- 0.94,
            description <- "Isso e uma nota de CINQUENTA REAIS."
        )
        readings.append(reading)

        para cada r em readings:
            self.last_readings.append(r)
        retorne readings

    funcao narrate_scene(self, readings: List[SensorReading], user_disability: str = "") retorna str:
        // Transforma leituras visuais em narrativa falada.
        se NAO  readings entao:
            retorne "Nao consigo ver nada claramente agora."

        parts <- []
        para cada r em readings:
            se r.confidence > 0.7 entao:
                parts.append(r.description)

        se NAO  parts entao:
            retorne "Ambiente visual incerto. Vou continuar observando."

        retorne ". ".join(parts) + "."


// ============================================================================
// 4. AUDIO -- Microfone como Ouvidos
// ============================================================================

classe AudioPerceptionEngine:
    // 
    Usa o microfone do smartphone/smartwatch para traduzir o mundo sonoro.
    Integrado com OpenAudioChannel para separacao de fontes.
    // 

    funcao __init__(self):
        self.last_readings: deque = deque(maxlen=100)
        self.sound_buffer: deque = deque(maxlen=30)   // 30s de historico

    funcao process_audio(self) retorna List[SensorReading]:
        // Processa audio ambiente e gera leituras.
        readings <- []

        // SURDO: transcreve fala
        reading <- SensorReading(
            sensor <- SensorType.MICROPHONE,
            perception <- WorldPerception.SPEECH_TO_TEXT,
            value <- {"speaker": "homem", "text": "Bom dia, como vai?"},
            confidence <- 0.90,
            description <- "Um homem disse: Bom dia, como vai?"
        )
        readings.append(reading)

        // Classificacao de som ambiente
        reading <- SensorReading(
            sensor <- SensorType.MICROPHONE,
            perception <- WorldPerception.SOUND_CLASSIFICATION,
            value <- {"sound": "sirene", "direction": "direita", "approaching": VERDADEIRO},
            confidence <- 0.85,
            description <- "Sirene de ambulancia se aproximando pela direita."
        )
        readings.append(reading)

        // Campainha
        reading <- SensorReading(
            sensor <- SensorType.MICROPHONE,
            perception <- WorldPerception.DOORBELL,
            value <- {"detected": VERDADEIRO, "count": 2},
            confidence <- 0.95,
            description <- "Alguem tocou a campainha. Duas vezes."
        )
        readings.append(reading)

        // Bebe chorando
        reading <- SensorReading(
            sensor <- SensorType.MICROPHONE,
            perception <- WorldPerception.BABY_CRYING,
            value <- {"detected": VERDADEIRO, "intensity": "alta"},
            confidence <- 0.93,
            description <- "O bebe esta chorando. Intensidade alta."
        )
        readings.append(reading)

        para cada r em readings:
            self.last_readings.append(r)
        retorne readings

    funcao narrate_sounds(self, readings: List[SensorReading]) retorna str:
        // Transforma leituras de audio em narrativa para surdos.
        se NAO  readings entao:
            retorne "Silencio."
        parts <- [r.description for r in readings if r.confidence > 0.7]
        retorne ". ".join(parts) + "." if parts else "Nao identifico sons especificos."


// ============================================================================
// 5. GEOLOCALIZACAO -- GPS como Sentido de Direcao
// ============================================================================

classe GeoLocationEngine:
    // 
    Usa GPS + bussola + acelerometro para navegar e proteger.
    Inclui geolocalizacao de criancas e pessoas vulneraveis.
    // 

    funcao __init__(self):
        self.last_known_location: Tuple[float, float] = (-23.55, -46.63)   // Sao Paulo
        self.tracked_persons: Dict[str, Dict] = {}   // criancas, idosos, etc
        self.safe_zones: List[Dict] = []
        self.last_readings: deque = deque(maxlen=100)

    funcao update_location(self, lat: float, lon: float) retorna SensorReading:
        // Atualiza localizacao GPS.
        self.last_known_location = (lat, lon)
        reading <- SensorReading(
            sensor <- SensorType.GPS,
            perception <- WorldPerception.GPS_LOCATION,
            value <- {"lat": lat, "lon": lon},
            confidence <- 0.98,
            description <- f"Voce esta proximo a {lat:.4f}, {lon:.4f}."
        )
        self.last_readings.append(reading)
        retorne reading

    funcao navigate_for_blind(self, destination: str) retorna str:
        // Navegacao por voz para cego -- passo a passo.
        steps <- [
            "Voce esta na rua Augusta, numero 1000.",
            "Vire a direita. Ainda 200 metros.",
            "Cuidado, buraco a frente a 3 metros.",
            "Semaforo vermelho. Espere.",
            "Semaforo verde. Atravesse. Cinco passos.",
            "Chegou. O destino esta a sua frente.",
        ]
        // Em producao: OSRM + OpenStreetMap + obstructions
        retorne steps[0]

    def track_child(self, child_id: str, child_name: str,
                    child_phone: str, safe_zones: List[Dict] = nulo) -> Dict:
        // Registra uma crianca para rastreamento.
        self.tracked_persons[child_id] = {
            "name": child_name,
            "phone": child_phone,
            "last_location": nulo,
            "last_update": time.time(),
            "safe_zones": safe_zones  OU  [],
            "status": "safe",
            "battery": 100,
        }
        se safe_zones entao:
            self.safe_zones = safe_zones
        retorne self.tracked_persons[child_id]

    def check_child_location(self, child_id: str, lat: float, lon: float,
                              declare battery: int  <- 100) -> Dict:
        // Verifica se crianca esta em zona segura.
        se child_id NAO  in self.tracked_persons entao:
            retorne {"error": "crianca nao registrada"}

        child <- self.tracked_persons[child_id]
        child["last_location"] = (lat, lon)
        child["last_update"] = time.time()
        child["battery"] = battery

        // Verificar zonas seguras
        in_safe_zone <- FALSO
        para cada zone em child.get("safe_zones", []):
            dist <- self._haversine(lat, lon, zone["lat"], zone["lon"])
            se dist <= zone.get("radius_m", 200) entao:
                in_safe_zone <- VERDADEIRO
                interrompa

        se in_safe_zone entao:
            child["status"] = "safe"
            retorne {
                "child_id": child_id,
                "name": child["name"],
                "status": "safe",
                "location": (lat, lon),
                "zone": zone["name"] if zone else "zona segura",
                "battery": battery,
                "message": f"{child['name']} esta na zona segura: {zone.get('name', 'casa')}."
            }
        senao:
            child["status"] = "outside"
            // Verificar se mudou muito rapido (sequestro?)
            distance_from_safe <- 999
            nearest_zone_name <- ""
            para cada zone em child.get("safe_zones", []):
                dist <- self._haversine(lat, lon, zone["lat"], zone["lon"])
                se dist < distance_from_safe entao:
                    distance_from_safe <- dist
                    nearest_zone_name <- zone.get("name", "zona")

            retorne {
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

    funcao find_nearby_help(self, help_type: str = "hospital") retorna List[Dict]:
        // Encontra ajuda proxima (hospital, farmacia, delegacia).
        // Em producao: OpenStreetMap Overpass API
        retorne [
            {"name": "Hospital Sao Paulo", "distance_m": 800, "direction": "norte"},
            {"name": "UBS Vila Mariana", "distance_m": 1200, "direction": "leste"},
            {"name": "Farmacia 24h", "distance_m": 300, "direction": "oeste"},
        ]

    funcao _haversine(self, lat1: float, lon1: float, lat2: float, lon2: float) retorna float:
        // Distancia em metros entre dois pontos GPS.
        // importa radians, sin, cos, sqrt, atan2 de math
        R <- 6371000  // raio da terra em metros
        dlat <- radians(lat2 - lat1)
        dlon <- radians(lon2 - lon1)
        a <- sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        c <- 2 * atan2(sqrt(a), sqrt(1-a))
        retorne R * c


// ============================================================================
// 6. BIOMETRIA -- Smartwatch como Sensor Corporal
// ============================================================================

classe BiometricEngine:
    // 
    Usa smartwatch/monitor para detectar estados corporais.
    Previne crises, detecta quedas, monitora estresse.
    // 

    funcao __init__(self):
        self.last_readings: deque = deque(maxlen=1000)
        self.baseline_heart_rate: int = 75
        self.fall_detected: bool = FALSO

    def process_biometrics(self, heart_rate: int = 75, spo2: int = 98,
                           declare skin_temp: float  <- 36.5, movement: str = "normal") -> List[SensorReading]:
        // Processa dados biometricos.
        readings <- []

        // Deteccao de queda
        se movement == "fall" entao:
            self.fall_detected = VERDADEIRO
            reading <- SensorReading(
                sensor <- SensorType.ACCELEROMETER,
                perception <- WorldPerception.FALL_DETECTION,
                value <- {"detected": VERDADEIRO, "impact_g": 3.2},
                confidence <- 0.92,
                description <- "QUEDA DETECTADA. Voce esta bem? Responda em 30 segundos ou ligo para emergencia."
            )
            readings.append(reading)

        // Anomalia cardiaca
        se heart_rate > 120  OU  heart_rate < 50 entao:
            reading <- SensorReading(
                sensor <- SensorType.HEART_RATE,
                perception <- WorldPerception.HEART_ANOMALY,
                value <- {"heart_rate": heart_rate, "baseline": self.baseline_heart_rate},
                confidence <- 0.85,
                description <- f"Frequencia cardiaca {heart_rate} bpm. Isso esta fora do normal."
            )
            readings.append(reading)

        // Deteccao de estresse (variabilidade cardiaca reduzida)
        se heart_rate > 100  E  movement == "normal" entao:
            reading <- SensorReading(
                sensor <- SensorType.HEART_RATE,
                perception <- WorldPerception.STRESS_DETECTION,
                value <- {"heart_rate": heart_rate, "hrv_low": VERDADEIRO},
                confidence <- 0.70,
                description <- "Seu coracao esta acelerado e voce esta parado. Talvez estresse. Quer respirar comigo?"
            )
            readings.append(reading)

        // Previsao de crise epileptica (HRV + skin temp spike)
        se skin_temp > 37.0  E  heart_rate > 110 entao:
            reading <- SensorReading(
                sensor <- SensorType.SKIN_TEMP,
                perception <- WorldPerception.SEIZURE_PREDICTION,
                value <- {"skin_temp": skin_temp, "heart_rate": heart_rate, "risk": "moderate"},
                confidence <- 0.60,
                description <- "Sinais que podem preceder uma crise. Sente-se em local seguro."
            )
            readings.append(reading)

        // Tremor (Parkinson)
        se movement == "tremor" entao:
            reading <- SensorReading(
                sensor <- SensorType.ACCELEROMETER,
                perception <- WorldPerception.TREMOR_DETECTION,
                value <- {"frequency_hz": 5.0, "amplitude": "moderate"},
                confidence <- 0.80,
                description <- "Tremor detectado. Vou ajustar a sensibilidade dos botoes."
            )
            readings.append(reading)

        para cada r em readings:
            self.last_readings.append(r)
        retorne readings


// ============================================================================
// 7. TELEFONISTA -- A Voz que Conversa
// ============================================================================

classe Telefonista:
    // 
    A telefonista humana digital. Ela conversa com o usuario,
    capta o mundo pelos sensores, e responde como uma pessoa.

    DIFERENCA de um assistente de voz tradicional:
    - Alexa/Google: "Ok Google, qual a previsao do tempo"
    - Telefonista: "Cleiton, bom dia. Vi que esta nublado. Leva guarda-chuva.
                     Ah, e sua filha chegou na escola. Tudo certo."
    // 

    funcao __init__(self, config: TelefonistaConfig):
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
        self.children_tracked: Dict[str, str] = {}   // id -> name

        self._setup_sensors()

    funcao _setup_sensors(self) retorna None:
        // Configura sensores ativos baseado no hardware disponivel.
        // Smartphone tem sempre camera + mic + gps
        self.active_sensors.update([
            SensorType.CAMERA_REAR, SensorType.CAMERA_FRONT,
            SensorType.MICROPHONE, SensorType.GPS,
            SensorType.ACCELEROMETER, SensorType.GYROSCOPE,
            SensorType.COMPASS, SensorType.LIGHT,
            SensorType.PROXIMITY,
        ])

    funcao greet(self, user_name: str, time_of_day: str = "manha") retorna str:
        // Saudacao inicial personalizada.
        self.user_name = user_name
        greetings <- {
            "manha": "Bom dia",
            "tarde": "Boa tarde",
            "noite": "Boa noite",
        }
        g <- greetings.get(time_of_day, "Ola")

        se self.config.personality == TelefonistaPersonality.GENTLE entao:
            msg <- f"{g}, {user_name}. Aqui e a {self.config.name}. "
        senao se self.config.personality == TelefonistaPersonality.CHEERFUL entao:
            msg <- f"{g}, {user_name}! Que bom te ouvir! "
        senao se self.config.personality == TelefonistaPersonality.FORMAL entao:
            msg <- f"{g}. {self.config.name} a servico. "
        senao:
            msg <- f"{g}, {user_name}. "

        self._record(msg, "telefonista")
        retorne msg

    funcao listen_and_respond(self, user_input: str) retorna str:
        // Processa entrada do usuario e responde como conversa.
        self._record(user_input, "user")

        // Detectar emocao na fala
        emotion <- self._detect_emotion(user_input)
        se emotion != self.user_emotion entao:
            self.user_emotion = emotion
            se self.config.emotional_adaptation entao:
                self.config.adapt_to_emotion(emotion)

        // Detectar intencao
        intent <- self._detect_intent(user_input)
        response <- self._respond(intent, user_input)

        self._record(response, "telefonista")
        retorne response

    funcao see_world(self) retorna str:
        // Usa a camera para ver o mundo e narrar para o usuario.
        readings <- self.cv_engine.process_frame(SensorType.CAMERA_REAR)
        narration <- self.cv_engine.narrate_scene(readings, ", ".join(self.user_disabilities))
        self._record(narration, "telefonista")
        retorne narration

    funcao hear_world(self) retorna str:
        // Usa o microfone para ouvir o mundo e narrar para surdos.
        readings <- self.audio_engine.process_audio()
        narration <- self.audio_engine.narrate_sounds(readings)
        self._record(narration, "telefonista")
        retorne narration

    def sense_body(self, heart_rate: int = 75, movement: str = "normal",
                   declare spo2: int  <- 98, skin_temp: float = 36.5) -> str:
        // Usa biometria para checar o corpo do usuario.
        readings <- self.bio_engine.process_biometrics(
            heart_rate <- heart_rate, movement=movement, spo2=spo2, skin_temp=skin_temp
        )
        se NAO  readings entao:
            retorne "Tudo normal com seu corpo."
        messages <- [r.description for r in readings]
        msg <- " ".join(messages)
        self._record(msg, "telefonista")
        retorne msg

    funcao navigate(self, destination: str) retorna str:
        // Navegacao por voz (cego andando na rua).
        self.current_mode = ConversationMode.CO_DRIVER
        instruction <- self.geo_engine.navigate_for_blind(destination)
        self._record(instruction, "telefonista")
        retorne instruction

    def check_on_child(self, child_id: str, lat: float, lon: float,
                       declare battery: int  <- 100) -> str:
        // Verifica localizacao de crianca rastreada.
        result <- self.geo_engine.check_child_location(child_id, lat, lon, battery)
        msg <- result.get("message", "Sem informacoes.")
        self._record(msg, "telefonista")
        retorne msg

    def register_child(self, child_id: str, name: str, phone: str,
                       declare safe_zones: List[Dict]  <- nulo) -> str:
        // Registra crianca para rastreamento.
        self.geo_engine.track_child(child_id, name, phone, safe_zones)
        self.children_tracked[child_id] = name
        msg <- f"{name} registrada. Vou avisar se ela sair das zonas seguras."
        self._record(msg, "telefonista")
        retorne msg

    funcao find_help(self, help_type: str = "hospital") retorna str:
        // Encontra ajuda proxima.
        results <- self.geo_engine.find_nearby_help(help_type)
        se NAO  results entao:
            retorne "Nao encontrei nada proximo agora."
        parts <- []
        para cada r em results:
            parts.append(f"{r['name']} a {r['distance_m']} metros ao {r['direction']}")
        msg <- "Encontrei: " + ". ".join(parts) + "."
        self._record(msg, "telefonista")
        retorne msg

    funcao make_call(self, contact_name: str, reason: str = "") retorna str:
        // Faz uma ligacao telefonica real.
        reason_text <- f" Motivo: {reason}." if reason else ""
        msg <- f"Ligando para {contact_name}.{reason_text}"
        self._record(msg, "telefonista")
        // Em producao: intents Android/iOS para fazer ligacao
        retorne msg

    funcao emergency(self, service: str = "190") retorna str:
        // Aciona emergencia.
        self.current_mode = ConversationMode.EMERGENCY
        self.config.personality = TelefonistaPersonality.PROTECTIVE
        self.config.speech_rate = 0.9
        self.config.humor_enabled = FALSO
        self.config.verbosity = 0.2
        msg <- f"EMERGENCIA. Ligando para {service}. Fique calmo. Estou aqui."
        self._record(msg, "telefonista")
        retorne msg

    funcao dictate_code(self, code_input: str) retorna str:
        // Usuario dita codigo, telefonista escreve.
        self.current_mode = ConversationMode.DICTATION
        // Em producao: integracao com Talon/Cursorless para programacao por voz
        msg <- f"Anotado. Escrevi: {code_input}. Quer que eu execute?"
        self._record(msg, "telefonista")
        retorne msg

    funcao _detect_emotion(self, text: str) retorna EmotionalState:
        // Detecta emocao no texto (simplificado).
        text_lower <- text.lower()
        se any(w in text_lower for w in ["cansado", "exausto", "durmo"]) entao:
            retorne EmotionalState.TIRED
        se any(w in text_lower for w in ["estress", "put", "merda", "porra"]) entao:
            retorne EmotionalState.STRESSED
        se any(w in text_lower for w in ["ansios", "preocup", "medo"]) entao:
            retorne EmotionalState.ANXIOUS
        se any(w in text_lower for w in ["feliz", "otimo", "show", "massa"]) entao:
            retorne EmotionalState.HAPPY
        se any(w in text_lower for w in ["foco", "trabalh", "concentrad"]) entao:
            retorne EmotionalState.FOCUSED
        se any(w in text_lower for w in ["triste", "para", "desanim"]) entao:
            retorne EmotionalState.SAD
        se any(w in text_lower for w in ["irritad", "irritante", "raiva"]) entao:
            retorne EmotionalState.ANGRY
        se any(w in text_lower for w in ["muito", "sobrecarreg", "nao aguento"]) entao:
            retorne EmotionalState.OVERWHELMED
        retorne EmotionalState.NEUTRAL

    funcao _detect_intent(self, text: str) retorna str:
        // Detecta a intencao do usuario (simplificado).
        text_lower <- text.lower()
        se any(w in text_lower for w in ["codigo", "programar", "funcao", "variavel"]) entao:
            retorne "code"
        se any(w in text_lower for w in ["onde estou", "localizacao", "rua"]) entao:
            retorne "location"
        se any(w in text_lower for w in ["minha filha", "meu filho", "crianca"]) entao:
            retorne "child"
        se any(w in text_lower for w in ["cor", "cela", "vermelho", "verde", "azul"]) entao:
            retorne "color"
        se any(w in text_lower for w in ["socorro", "emergencia", "ajuda", "190", "192"]) entao:
            retorne "emergency"
        se any(w in text_lower for w in ["ligar", "telefone", "chamada"]) entao:
            retorne "call"
        se any(w in text_lower for w in ["ve", "olha", "camera", "enxergar"]) entao:
            retorne "see"
        se any(w in text_lower for w in ["ouvir", "som", "barulho"]) entao:
            retorne "hear"
        se any(w in text_lower for w in ["navegar", "ir para", "como chego"]) entao:
            retorne "navigate"
        retorne "chat"

    funcao _respond(self, intent: str, user_input: str) retorna str:
        // Gera resposta baseada na intencao e personalidade.
        name <- self.user_name  OU  "amigo"

        se intent == "code" entao:
            retorne self.dictate_code(user_input)
        se intent == "location" entao:
            retorne self.geo_engine.navigate_for_blind("")
        se intent == "child" entao:
            retorne "Quer que eu verifique onde ela esta?"
        se intent == "color" entao:
            readings <- self.cv_engine.process_frame(SensorType.CAMERA_REAR)
            color_reading <- [r for r in readings if r.perception == WorldPerception.COLOR_DETECTION]
            se color_reading entao:
                retorne color_reading[0].description
            retorne "Aponta a camera que eu vejo a cor."
        se intent == "emergency" entao:
            retorne self.emergency("192")
        se intent == "call" entao:
            retorne "Para quem voce quer ligar?"
        se intent == "see" entao:
            retorne self.see_world()
        se intent == "hear" entao:
            retorne self.hear_world()
        se intent == "navigate" entao:
            retorne "Para onde voce quer ir?"
        // Chat default
        se self.user_emotion == EmotionalState.TIRED entao:
            retorne f"{name}, voce parece cansado. Que tal uma pausa? Posso continuar depois."
        se self.user_emotion == EmotionalState.STRESSED entao:
            retorne f"Respira, {name}. Uma coisa de cada vez. No que eu posso ajudar agora?"
        se self.user_emotion == EmotionalState.HAPPY entao:
            retorne f"Que bom te ouvir feliz, {name}! No que posso ajudar?"
        retorne f"Entendi. Conte mais, {name}."

    funcao _record(self, text: str, speaker: str) retorna None:
        // Registra na historia da conversa.
        self.conversation_history.append({
            "speaker": speaker,
            "text": text,
            "timestamp": time.time(),
            "emotion": self.user_emotion.value if speaker == "user" else nulo,
        })

    funcao conversation_summary(self) retorna Dict[str, Any]:
        // Resumo da conversa.
        retorne {
            "telefonista_name": self.config.name,
            "user_name": self.user_name,
            "total_exchanges": len(self.conversation_history),
            "current_emotion": self.user_emotion.value,
            "current_mode": self.current_mode.value,
            "active_sensors": len(self.active_sensors),
            "children_tracked": len(self.children_tracked),
            "personality": self.config.personality.value,
        }


// ============================================================================
// 8. ADAPTACAO POR DEFICIENCIA
// ============================================================================

funcao create_telefonista_for_blind(user_name: str = "") retorna Telefonista:
    // Telefonista para cego: voz + camera + GPS + ligacao.
    config <- TelefonistaConfig(
        name <- "Iara",
        personality <- TelefonistaPersonality.GENTLE,
        speech_rate <- 1.3,  // cegos escutam rapido
        verbosity <- 0.7,
        proactive <- 0.6,
    )
    t <- Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = ["visual"]
    t.current_mode = ConversationMode.CO_DRIVER
    retorne t


funcao create_telefonista_for_deaf(user_name: str = "") retorna Telefonista:
    // Telefonista para surdo: visual + haptico + legenda.
    config <- TelefonistaConfig(
        name <- "Iara",
        personality <- TelefonistaPersonality.GENTLE,
        speech_rate <- 1.0,
        verbosity <- 0.5,
    )
    t <- Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = ["auditiva"]
    t.current_mode = ConversationMode.SILENT   // so visual/haptico
    retorne t


funcao create_telefonista_for_motor(user_name: str = "") retorna Telefonista:
    // Telefonista para tetraplegia: voz pura, sem botoes.
    config <- TelefonistaConfig(
        name <- "Iara",
        personality <- TelefonistaPersonality.CHEERFUL,
        speech_rate <- 1.0,
        verbosity <- 0.6,
        proactive <- 0.5,  // antecipa para reduzir necessidade de input
    )
    t <- Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = ["motora"]
    t.current_mode = ConversationMode.DIALOGUE
    retorne t


funcao create_telefonista_for_autism(user_name: str = "") retorna Telefonista:
    // Telefonista para autista: calma, previsivel, sem surpresas.
    config <- TelefonistaConfig(
        name <- "Iara",
        personality <- TelefonistaPersonality.GENTLE,
        speech_rate <- 0.9,
        verbosity <- 0.3,
        humor_enabled <- FALSO,
        proactive <- 0.2,
    )
    t <- Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = ["espectro_autista"]
    t.current_mode = ConversationMode.DIALOGUE
    retorne t


funcao create_telefonista_for_child(user_name: str = "") retorna Telefonista:
    // Telefonista para crianca: brincalhona, simples, protetora.
    config <- TelefonistaConfig(
        name <- "Tia Iara",
        personality <- TelefonistaPersonality.PLAYFUL,
        speech_rate <- 0.85,
        verbosity <- 0.3,
        proactive <- 0.4,
    )
    t <- Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = []
    t.current_mode = ConversationMode.DIALOGUE
    retorne t


funcao create_telefonista_for_elderly(user_name: str = "") retorna Telefonista:
    // Telefonista para idoso: devagar, formosa, protetora.
    config <- TelefonistaConfig(
        name <- "Iara",
        personality <- TelefonistaPersonality.PROTECTIVE,
        speech_rate <- 0.8,
        verbosity <- 0.6,
        humor_enabled <- VERDADEIRO,
        proactive <- 0.7,  // antecipa muito
        formality <- 0.6,
    )
    t <- Telefonista(config)
    t.user_name = user_name
    t.user_disabilities = []
    t.current_mode = ConversationMode.DIALOGUE
    retorne t


// ============================================================================
// 9. CENARIOS DO MUNDO REAL
// ============================================================================

funcao scenario_blind_walking():
    // Cenario: cego andando na rua.
    print("=" * 60)
    print("CENARIO: Cego andando na rua")
    print("=" * 60)

    t <- create_telefonista_for_blind("Cleiton")
    print(t.greet("Cleiton", "manha"))

    // Camera ve obstaculos + semaforo
    print(f"\n[Camera]")
    print(t.see_world())

    // GPS navega
    print(f"\n[GPS]")
    print(t.navigate("padaria"))

    // Reconhece dinheiro
    readings <- t.cv_engine.process_frame(SensorType.CAMERA_REAR)
    para cada r em readings:
        se r.perception == WorldPerception.MONEY_RECOGNITION entao:
            print(f"\n[Dinheiro]")
            print(r.description)

    // Microfone ouve sirene
    print(f"\n[Audio]")
    print(t.hear_world())


funcao scenario_deaf_conversation():
    // Cenario: surdo em conversa com legenda em tempo real.
    print("\n" + "=" * 60)
    print("CENARIO: Surdo em conversa")
    print("=" * 60)

    t <- create_telefonista_for_deaf("Maria")
    print(f"[Visual] {t.greet('Maria', 'tarde')}")

    // Microfone transcreve + classifica sons
    print(f"\n[Audio -> Visual]")
    print(f"[Visual] {t.hear_world()}")


funcao scenario_colorblind_shopping():
    // Cenario: daltonico comprando roupas.
    print("\n" + "=" * 60)
    print("CENARIO: Daltonico comprando roupas")
    print("=" * 60)

    t <- Telefonista(TelefonistaConfig(name="Iara"))
    t.user_name = "Joao"
    t.user_disabilities = ["visual"]

    print(t.greet("Joao", "tarde"))
    print("\n[Camera apontada para roupa]")
    readings <- t.cv_engine.process_frame(SensorType.CAMERA_REAR)
    para cada r em readings:
        se r.perception == WorldPerception.COLOR_DETECTION entao:
            print(f"  {r.description}")
    print("\n[Camera apontada para semaforo]")
    para cada r em readings:
        se r.perception == WorldPerception.TRAFFIC_LIGHT entao:
            print(f"  {r.description}")


funcao scenario_lost_child():
    // Cenario: crianca perdida rastreada por GPS.
    print("\n" + "=" * 60)
    print("CENARIO: Geolocalizacao de crianca")
    print("=" * 60)

    t <- Telefonista(TelefonistaConfig(name="Iara", personality=TelefonistaPersonality.PROTECTIVE))
    t.user_name = "Cleiton"

    // Registrar crianca
    safe_zones <- [
        {"name": "Casa", "lat": -23.55, "lon": -46.63, "radius_m": 200},
        {"name": "Escola", "lat": -23.56, "lon": -46.64, "radius_m": 200},
    ]
    print(t.register_child("child_01", "Sophia", "+5511999999999", safe_zones))

    // Crianca na escola (seguro)
    print(f"\n[Sophia na escola]")
    print(t.check_on_child("child_01", -23.56, -46.64, battery=85))

    // Crianca fora da zona segura
    print(f"\n[Sophia em local desconhecido]")
    result <- t.geo_engine.check_child_location("child_01", -23.60, -46.70, battery=45)
    print(f"  {result['message']}")
    print(f"  Nivel: {result.get('alert_level', 'info')}")

    // Bateria fraca
    print(f"\n[Sophia com bateria fraca]")
    result <- t.geo_engine.check_child_location("child_01", -23.58, -46.66, battery=12)
    print(f"  {result['message']}")


funcao scenario_fall_detection():
    // Cenario: idoso cai, sistema detecta e liga.
    print("\n" + "=" * 60)
    print("CENARIO: Deteccao de queda (idoso)")
    print("=" * 60)

    t <- create_telefonista_for_elderly("Dona Maria")
    print(t.greet("Dona Maria", "manha"))

    // Detecta queda
    print(f"\n[Queda detectada!]")
    print(t.sense_body(heart_rate=110, movement="fall"))

    // 30s sem resposta -> emergencia
    print(f"\n[Sem resposta em 30s]")
    print(t.emergency("192"))


funcao scenario_stress_detection():
    // Cenario: deteccao de estresse por smartwatch.
    print("\n" + "=" * 60)
    print("CENARIO: Deteccao de estresse")
    print("=" * 60)

    t <- Telefonista(TelefonistaConfig(name="Iara"))
    t.user_name = "Cleiton"

    print("Coracao acelerado, voce esta parado...")
    print(t.sense_body(heart_rate=115, movement="normal"))

    print("\nVoce diz: 'to estressado pra caralho'")
    print(t.listen_and_respond("to estressado pra caralho"))


funcao scenario_epilepsy_warning():
    // Cenario: previsao de crise epileptica.
    print("\n" + "=" * 60)
    print("CENARIO: Previsao de crise epileptica")
    print("=" * 60)

    t <- Telefonista(TelefonistaConfig(
        name <- "Iara", personality=TelefonistaPersonality.PROTECTIVE
    ))
    t.user_name = "Pedro"
    print(t.greet("Pedro", "tarde"))

    // Biometria detecta risco
    print(f"\n[Sinais pre-crise]")
    print(t.sense_body(heart_rate=115, skin_temp=37.5, movement="normal"))


// ============================================================================
// 10. DEMONSTRACAO COMPLETA
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenTelefonista -- O Sistema Como Conversa Humana")
    print("=" * 70)

    print(f"\nTelefonista: Iara")
    print(f"Personalidades: {len(TelefonistaPersonality)}")
    print(f"Estados emocionais: {len(EmotionalState)}")
    print(f"Modos de conversa: {len(ConversationMode)}")
    print(f"Tipos de sensor: {len(SensorType)}")
    print(f"Percepcoes do mundo: {len(WorldPerception)}")

    // Cenarios do mundo real
    scenario_blind_walking()
    scenario_deaf_conversation()
    scenario_colorblind_shopping()
    scenario_lost_child()
    scenario_fall_detection()
    scenario_stress_detection()
    scenario_epilepsy_warning()

    // Perfis
    print(f"\n{'=' * 70}")
    print("PERFIS DA TELEFONISTA")
    print(f"{'=' * 70}")

    profiles <- {
        "Cego": create_telefonista_for_blind("Cleiton"),
        "Surdo": create_telefonista_for_deaf("Maria"),
        "Tetraplegico": create_telefonista_for_motor("Joao"),
        "Autista": create_telefonista_for_autism("Pedro"),
        "Crianca": create_telefonista_for_child("Sophia"),
        "Idoso": create_telefonista_for_elderly("Dona Cecca"),
    }

    para cada (label, t) em profiles.items():
        print(f"\n  {label}:")
        print(f"    Nome: {t.config.name}")
        print(f"    Personalidade: {t.config.personality.value}")
        print(f"    Velocidade: {t.config.speech_rate}x")
        print(f"    Modo: {t.current_mode.value}")
        print(f"    Sensores ativos: {len(t.active_sensors)}")

    // Cobertura
    print(f"\n{'=' * 70}")
    print("COBERTURA DE PERCEPCAO DO MUNDO")
    print(f"{'=' * 70}")

    perception_categories <- {
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

    para cada (category, perceptions) em perception_categories.items():
        print(f"\n  {category}:")
        para cada p em perceptions:
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


se __name__ == "__main__" entao:
    demo()

```
