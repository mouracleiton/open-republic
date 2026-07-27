# OpenHumanNet -- Chamar o Humano Autorizado Mais Proximo

**Arquivo original:** `open-republic/core/open_human_net.py`

**Descricao:** =========================================================
"Quando tudo falha, a tecnologia so faz uma coisa util:
CHAMAR UM HUMANO. Nao qualquer humano. O humano CERTO.
O mais proximo. O autorizado. O que PODE ajudar.
O cego esta perdido, bateria em 1%, GPS morto, TTS crashou.
O sistema nao tenta se consertar. O sistema GRITE por ajuda.
Mas nao um grito aleatorio -- uma chamada CIRURGICA:
'Ola, Andre? Aqui e a Iara, sistema da Republica.
Cleiton esta na rua Augusta perto da numero 1500.
Bateria em 1%. Ele e cego e pode precisar de ajuda.
Voce e o humano autorizado mais proximo (400m).
Pode ir ate la?'
Se Andre nao atende em 30s, chama o proximo.
E o proximo. E o proximo. Ate alguem responder.
ESTRUTURA EM ANEIS (concentricos):
Anel 0: Familia direta (esposa, pai, mae, irmao)
Anel 1: Cuidador autorizado / vizinho de confianca
Anel 2: Comunidade Republica (membros proximos)
Anel 3: Profissionais (medico, enfermeiro, assistente social)
Anel 4: Emergencia publica (190, 192, 193)
Anel 5: Qualquer humano proximo (pedir ajuda a estranho)
O sistema so para de chamar quando:
1. Um humano CONFIRMA que vai ajudar, OU
2. A situacao se resolve (usuario responde que esta bem), OU
3. Todos os aneis foram esgotados -> emergencia publica
PRINCIPIO: A tecnologia NAO substitui o humano.
A tecnologia CONECTA o humano certo no momento certo.
Integrado com:
- OpenResilience (dispara em SURVIVAL/EMERGENCY)
- OpenTelefonista (faz a ligacao naturalmente)
- OpenBodilyAutonomy (so chama se usuario autorizou ou esta incapacitado)
- OpenAbsence (respeita se usuario pode se comunicar)
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol

// !/usr/bin/env python3
// 
OpenHumanNet -- Chamar o Humano Autorizado Mais Proximo
=========================================================
"Quando tudo falha, a tecnologia so faz uma coisa util:
CHAMAR UM HUMANO. Nao qualquer humano. O humano CERTO.
O mais proximo. O autorizado. O que PODE ajudar.

O cego esta perdido, bateria em 1%, GPS morto, TTS crashou.
O sistema nao tenta se consertar. O sistema GRITE por ajuda.
Mas nao um grito aleatorio -- uma chamada CIRURGICA:

'Ola, Andre? Aqui e a Iara, sistema da Republica.
Cleiton esta na rua Augusta perto da numero 1500.
Bateria em 1%. Ele e cego e pode precisar de ajuda.
Voce e o humano autorizado mais proximo (400m).
Pode ir ate la?'

Se Andre nao atende em 30s, chama o proximo.
E o proximo. E o proximo. Ate alguem responder.

ESTRUTURA EM ANEIS (concentricos):
Anel 0: Familia direta (esposa, pai, mae, irmao)
Anel 1: Cuidador autorizado / vizinho de confianca
Anel 2: Comunidade Republica (membros proximos)
Anel 3: Profissionais (medico, enfermeiro, assistente social)
Anel 4: Emergencia publica (190, 192, 193)
Anel 5: Qualquer humano proximo (pedir ajuda a estranho)

O sistema so para de chamar quando:
1. Um humano CONFIRMA que vai ajudar, OU
2. A situacao se resolve (usuario responde que esta bem), OU
3. Todos os aneis foram esgotados -> emergencia publica

PRINCIPIO: A tecnologia NAO substitui o humano.
A tecnologia CONECTA o humano certo no momento certo.

Integrado com:
- OpenResilience (dispara em SURVIVAL/EMERGENCY)
- OpenTelefonista (faz a ligacao naturalmente)
- OpenBodilyAutonomy (so chama se usuario autorizou ou esta incapacitado)
- OpenAbsence (respeita se usuario pode se comunicar)

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
// 

// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set, Callable de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict, deque de collections
// importa time
// importa math


// ============================================================================
// 1. ANEIS DE CONFIANCA (Concentric Trust Rings)
// ============================================================================

classe TrustRing herda de Enum:
    // Aneis concêntricos de confianca para chamada de ajuda.
    FAMILY <- 0  // familia direta
    CAREGIVER <- 1  // cuidador / vizinho de confianca
    COMMUNITY <- 2  // membros da Republica proximos
    PROFESSIONAL <- 3  // medico, enfermeiro, assistente social
    EMERGENCY <- 4  // 190, 192, 193
    BYSTANDER <- 5  // qualquer humano proximo (estranho)


classe AuthorizationLevel herda de Enum:
    // Nivel de autorizacao do humano para receber alertas.
    FULL <- "completa"  // pode tomar decisoes por o usuario
    HIGH <- "alta"  // pode ajudar fisicamente, nao decidir
    MEDIUM <- "media"  // pode verificar status e reportar
    LOW <- "baixa"  // so recebe notificacao
    EMERGENCY_ONLY <- "so_emergencia"  // so chamado em emergencia real


classe HumanAvailability herda de Enum:
    // Disponibilidade do humano no momento.
    AVAILABLE <- "disponivel"  // respondeu, pode ir
    MAYBE <- "talvez"  // respondeu, verificando
    BUSY <- "ocupado"  // respondeu, nao pode
    UNREACHABLE <- "inalcancavel"  // nao atendeu
    OFFLINE <- "offline"  // sem sinal / telefone desligado
    UNKNOWN <- "desconhecido"  // ainda nao tentou


classe ContactMethod herda de Enum:
    // Como contatar o humano.
    PHONE_CALL <- "ligacao"  // ligacao telefonica
    SMS <- "sms"  // mensagem de texto
    WHATSAPP <- "whatsapp"  // mensagem de WhatsApp
    VIDEO_CALL <- "video"  // video chamada
    APP_PUSH <- "notificacao_app"  // push notification do app
    SMARTWATCH <- "smartwatch"  // vibracao no relogio
    HOME_ASSISTANT <- "assinante_casa"  // Alexa/Google Home
    PHYSICAL_VISIT <- "visita_fisica"  // alguem vai ate la pessoalmente


// ============================================================================
// 2. HUMANO AUTORIZADO
// ============================================================================

// decorador: @dataclass
classe AuthorizedHuman:
    // Um humano autorizado a ser chamado em caso de falha.
    human_id: str
    name: str
    phone: str
    ring: TrustRing
    authorization: AuthorizationLevel
    declare relationship: str  <- ""  // "esposa", "pai", "vizinho", "medico"
    declare home_location: Optional[Tuple[float, float]]  <- nulo  // (lat, lon)
    declare current_location: Optional[Tuple[float, float]]  <- nulo
    declare last_location_update: float  <- 0.0
    declare preferred_contact: ContactMethod  <- ContactMethod.PHONE_CALL
    declare languages: List[str]  <- field(default_factory=lambda: ["pt-BR"])
    declare skills: List[str]  <- field(default_factory=list)  // "primeiros_socorros", "libras", etc
    declare available_hours: Tuple[str, str]  <- ("00:00", "23:59")  // disponibilidade horaria
    declare response_timeout_s: int  <- 30  // tempo para responder antes de tentar proximo
    declare max_distance_km: float  <- 50.0  // distancia maxima para deslocamento
    declare can_make_decisions: bool  <- FALSO  // pode decidir por o usuario (procuration)
    declare medical_authorization: bool  <- FALSO  // pode autorizar procedimentos
    declare photo_url: str  <- ""  // para o usuario reconhecer quem esta vindo
    declare notes: str  <- ""  // informacoes adicionais

    funcao distance_to(self, lat: float, lon: float) retorna float:
        // Distancia em km ate um ponto (haversine simplificado).
        loc <- self.current_location  OU  self.home_location
        se NAO  loc entao:
            retorne 9999.0
        retorne _haversine_km(loc[0], loc[1], lat, lon)

    funcao is_available_now(self) retorna bool:
        // Verifica se esta dentro do horario de disponibilidade.
        now_h <- int(time.strftime("%H%M"))
        start <- int(self.available_hours[0].replace(":", ""))
        end <- int(self.available_hours[1].replace(":", ""))
        retorne start <= now_h <= end


funcao _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) retorna float:
    // Distancia em km entre dois pontos GPS.
    R <- 6371  // raio da terra em km
    dlat <- math.radians(lat2 - lat1)
    dlon <- math.radians(lon2 - lon1)
    a <- math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c <- 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    retorne R * c


// ============================================================================
// 3. EVENTO DE CHAMADA
// ============================================================================

classe CallStatus herda de Enum:
    PENDING <- "pendente"  // ainda nao chamou
    RINGING <- "tocando"  // chamando
    ANSWERED <- "atendeu"  // humano atendeu
    CONFIRMED <- "confirmou"  // humano confirmou que vai ajudar
    DECLINED <- "recusou"  // humano nao pode
    TIMEOUT <- "sem_resposta"  // nao atendeu no tempo
    FAILED <- "falhou"  // erro tecnico
    CANCELLED <- "cancelada"  // situacao resolvida, cancelar


// decorador: @dataclass
classe CallAttempt:
    // Uma tentativa de chamar um humano.
    attempt_id: str
    human: AuthorizedHuman
    method: ContactMethod
    declare status: CallStatus  <- CallStatus.PENDING
    declare called_at: float  <- field(default_factory=time.time)
    declare answered_at: Optional[float]  <- nulo
    declare timeout_at: Optional[float]  <- nulo
    declare message_sent: str  <- ""
    declare response_received: str  <- ""
    declare distance_km: float  <- 0.0
    declare eta_minutes: float  <- 0.0  // tempo estimado de chegada


// ============================================================================
// 4. MOTOR DE CHAMADA DE HUMANOS
// ============================================================================

classe HumanNet:
    // 
    Motor que encontra e chama o humano autorizado mais proximo
    em caso de falha critica do sistema.

    FLUXO:
    1. Falha detectada (OpenResilience: SURVIVAL ou EMERGENCY)
    2. Pegar localizacao do usuario (GPS, ultima conhecida, ou triangulacao)
    3. Ranquear humanos por: anel -> distancia -> disponibilidade
    4. Chamar o mais proximo do anel mais interno
    5. Esperar resposta (timeout = response_timeout_s)
    6. Se atendeu e confirmou -> PARAR, ajudar esta a caminho
    7. Se nao atendeu -> chamar proximo
    8. Se anel esgotado -> subir para proximo anel
    9. Se todos esgotados -> emergencia publica (190/192)
    // 

    funcao __init__(self, user_name: str = "", user_phone: str = ""):
        self.user_name = user_name
        self.user_phone = user_phone
        self.registry: Dict[str, AuthorizedHuman] = {}
        self.call_history: deque = deque(maxlen=500)
        self.active_calls: Dict[str, CallAttempt] = {}
        self.confirmed_helper: Optional[AuthorizedHuman] = nulo
        self.current_ring: Optional[TrustRing] = nulo
        self.user_location: Optional[Tuple[float, float]] = nulo
        self.user_disabilities: List[str] = []
        self.situation_description: str = ""
        self.auto_call_enabled: bool = VERDADEIRO
        self.consent_given: bool = VERDADEIRO   // OpenBodilyAutonomy

    // -- Registro de humanos --

    funcao register_human(self, human: AuthorizedHuman) retorna str:
        // Registra um humano autorizado.
        self.registry[human.human_id] = human
        retorne f"{human.name} registrado no anel {human.ring.name} ({human.authorization.value})."

    funcao remove_human(self, human_id: str) retorna str:
        // Remove um humano do registro.
        se human_id in self.registry entao:
            name <- self.registry[human_id].name
            remova self.registry[human_id]
            retorne f"{name} removido."
        retorne "Humano nao encontrado."

    funcao list_humans(self) retorna Dict[str, List[AuthorizedHuman]]:
        // Lista humanos por anel.
        by_ring <- defaultdict(list)
        para cada h em self.registry.values():
            by_ring[h.ring].append(h)
        retorne dict(by_ring)

    // -- Atualizacao de localizacao --

    funcao update_user_location(self, lat: float, lon: float) retorna None:
        // Atualiza localizacao do usuario.
        self.user_location = (lat, lon)

    funcao update_human_location(self, human_id: str, lat: float, lon: float) retorna None:
        // Atualiza localizacao de um humano (via app/GPS).
        se human_id in self.registry entao:
            self.registry[human_id].current_location = (lat, lon)
            self.registry[human_id].last_location_update = time.time()

    // -- Ranqueamento --

    def rank_humans(self, max_ring: TrustRing = TrustRing.BYSTANDER,
                    declare required_auth: AuthorizationLevel  <- AuthorizationLevel.LOW) -> List[Tuple[AuthorizedHuman, float]]:
        // 
        Ranqueia humanos por prioridade de chamada.
        Prioridade: anel (menor = mais proximo confianca) -> distancia -> disponibilidade.
        // 
        se NAO  self.user_location entao:
            retorne []

        ranked <- []
        para cada human em self.registry.values():
            // Filtrar por anel maximo
            se human.ring.value > max_ring.value entao:
                continue
            // Filtrar por autorizacao minima
            auth_order <- [
                AuthorizationLevel.FULL,
                AuthorizationLevel.HIGH,
                AuthorizationLevel.MEDIUM,
                AuthorizationLevel.LOW,
                AuthorizationLevel.EMERGENCY_ONLY,
            ]
            se auth_order.index(human.authorization) > auth_order.index(required_auth) entao:
                continue
            // Filtrar por horario (se nao for emergencia publica)
            se human.ring != TrustRing.EMERGENCY  E  NAO  human.is_available_now() entao:
                continue
            // Filtrar por distancia maxima
            dist <- human.distance_to(self.user_location[0], self.user_location[1])
            se dist > human.max_distance_km  E  human.ring != TrustRing.EMERGENCY entao:
                continue

            ranked.append((human, dist))

        // Ordenar: anel primeiro, depois distancia
        ranked.sort(key=funcao anonima(x): (x[0].ring.value, x[1]))
        retorne ranked

    // -- Chamada --

    def trigger_emergency_call(self, situation: str, user_lat: float = 0, user_lon: float = 0,
                                declare severity: str  <- "critical") -> Dict[str, Any]:
        // 
        Dispara cadeia de chamadas para humanos autorizados.
        Retorna o resultado completo da cadeia.
        // 
        se user_lat != 0  E  user_lon != 0 entao:
            self.update_user_location(user_lat, user_lon)

        self.situation_description = situation
        self.confirmed_helper = nulo
        self.active_calls = {}

        se NAO  self.user_location entao:
            retorne {
                "success": FALSO,
                "error": "Sem localizacao do usuario. Nao posso chamar ajuda.",
                "fallback": "Ligar para 190 diretamente.",
            }

        // Determinar anel maximo baseado na severidade
        se severity == "catastrophic" entao:
            max_ring <- TrustRing.EMERGENCY
        senao se severity == "critical" entao:
            max_ring <- TrustRing.PROFESSIONAL
        senao:
            max_ring <- TrustRing.COMMUNITY

        // Determinar autorizacao minima
        se severity in ("critical", "catastrophic") entao:
            required_auth <- AuthorizationLevel.MEDIUM
        senao:
            required_auth <- AuthorizationLevel.LOW

        ranked <- self.rank_humans(max_ring=max_ring, required_auth=required_auth)

        se NAO  ranked entao:
            // Nenhum humano disponivel -> emergencia publica
            retorne self._call_emergency_services(situation)

        // Tentar cada humano em ordem
        results <- []
        para cada (human, distance) em ranked:
            self.current_ring = human.ring

            attempt <- self._call_human(human, situation, distance)
            results.append(attempt)

            se attempt.status == CallStatus.CONFIRMED entao:
                self.confirmed_helper = human
                retorne {
                    "success": VERDADEIRO,
                    "helper": human.name,
                    "phone": human.phone,
                    "ring": human.ring.name,
                    "distance_km": round(distance, 2),
                    "eta_minutes": attempt.eta_minutes,
                    "method": attempt.method.value,
                    "message": (
                        f"{human.name} confirmou! Esta a {distance:.1f}km. "
                        f"Chega em ~{attempt.eta_minutes:.0f} minutos."
                    ),
                    "all_attempts": [self._attempt_summary(a) for a in results],
                }

        // Nenhum humano confirmou -> escalar para emergencia publica
        emergency_result <- self._call_emergency_services(situation)
        retorne {
            "success": FALSO,
            "error": f"Nenhum dos {len(results)} humanos disponiveis confirmou.",
            "all_attempts": [self._attempt_summary(a) for a in results],
            "escalated_to_emergency": VERDADEIRO,
            "emergency_result": emergency_result,
        }

    def _call_human(self, human: AuthorizedHuman, situation: str,
                    distance: float) -> CallAttempt:
        // Tenta chamar um humano especifico (simulado).
        // Em producao: fazer ligacao real via Twilio/Android intent
        attempt <- CallAttempt(
            attempt_id <- f"CALL-{human.human_id}-{int(time.time())}",
            human <- human,
            method <- human.preferred_contact,
            distance_km <- distance,
            eta_minutes <- max(1, distance * 3),  // ~3 min por km a pe/carro cidade
            message_sent <- self._build_message(human, situation, distance),
        )

        attempt.status = CallStatus.RINGING
        self.active_calls[attempt.attempt_id] = attempt

        // Simular resposta baseado no anel (familia responde mais)
        response_chance <- {
            TrustRing.FAMILY: 0.85,
            TrustRing.CAREGIVER: 0.70,
            TrustRing.COMMUNITY: 0.50,
            TrustRing.PROFESSIONAL: 0.60,
            TrustRing.EMERGENCY: 0.90,
            TrustRing.BYSTANDER: 0.30,
        }
        chance <- response_chance.get(human.ring, 0.4)

        // importa random
        se random.random() < chance entao:
            attempt.status = CallStatus.CONFIRMED
            attempt.answered_at = time.time()
            attempt.response_received = f"{human.name} confirmou que esta indo."
        senao:
            attempt.status = CallStatus.TIMEOUT
            attempt.timeout_at = time.time()
            attempt.response_received = f"Sem resposta de {human.name} em {human.response_timeout_s}s."

        self.call_history.append(attempt)
        retorne attempt

    def _build_message(self, human: AuthorizedHuman, situation: str,
                       distance: float) -> str:
        // Constroi a mensagem natural para o humano.
        disabilities_text <- ""
        se self.user_disabilities entao:
            disabilities_text <- f" Condicao: {', '.join(self.user_disabilities)}."

        msg <- (
            f"Ola, {human.name}? Aqui e a Iara, sistema da Republica. "
            f"{self.user_name} precisa de ajuda. "
            f"Situacao: {situation}. "
            f"Localizacao aproximada: {self.user_location[0]:.4f}, {self.user_location[1]:.4f}. "
            f"Voce esta a {distance:.1f}km.{disabilities_text} "
            f"Pode ir ate la ou ligar para confirmar que esta bem?"
        )
        retorne msg

    funcao _call_emergency_services(self, situation: str) retorna Dict[str, Any]:
        // Chama servico de emergencia publica (190/192/193).
        // Determinar qual servico
        se "medica" in situation.lower()  OU  "coracao" in situation.lower()  OU  "machucad" in situation.lower() entao:
            service <- "192 (SAMU)"
            service_type <- "medica"
        senao se "incendio" in situation.lower()  OU  "fogo" in situation.lower() entao:
            service <- "193 (Bombeiros)"
            service_type <- "bombeiros"
        senao:
            service <- "190 (Policia)"
            service_type <- "policia"

        msg <- (
            f"LIGACAO AUTOMATICA para {service}. "
            f"Usuario: {self.user_name}. "
            f"Localizacao: {self.user_location}. "
            f"Situacao: {situation}. "
            f"Condicoes: {', '.join(self.user_disabilities) if self.user_disabilities else 'nenhuma'}. "
            f"Nenhum contato pessoal respondeu."
        )

        retorne {
            "success": VERDADEIRO,
            "service": service,
            "type": service_type,
            "message": msg,
            "note": "Emergencia publica acionada. Ajua a caminho.",
        }

    funcao cancel_emergency(self, reason: str = "Usuario esta bem") retorna Dict[str, Any]:
        // Cancela cadeia de emergencia (usuario recuperou, falso alarme).
        para cada attempt em self.active_calls.values():
            se attempt.status in (CallStatus.RINGING, CallStatus.PENDING) entao:
                attempt.status = CallStatus.CANCELLED

        self.confirmed_helper = nulo
        retorne {
            "cancelled": VERDADEIRO,
            "reason": reason,
            "message": f"Emergencia cancelada. {reason}. Todos os contatos foram avisados.",
        }

    funcao _attempt_summary(self, attempt: CallAttempt) retorna Dict[str, Any]:
        retorne {
            "human": attempt.human.name,
            "ring": attempt.human.ring.name,
            "phone": attempt.human.phone,
            "method": attempt.method.value,
            "status": attempt.status.value,
            "distance_km": round(attempt.distance_km, 2),
            "eta_minutes": round(attempt.eta_minutes, 1),
            "response": attempt.response_received,
        }

    funcao status(self) retorna Dict[str, Any]:
        // Status atual da rede de humanos.
        by_ring <- self.list_humans()
        retorne {
            "user_name": self.user_name,
            "total_humans": len(self.registry),
            "humans_by_ring": {r.name: len(v) for r, v in by_ring.items()},
            "confirmed_helper": self.confirmed_helper.name if self.confirmed_helper else nulo,
            "current_ring": self.current_ring.name if self.current_ring else nulo,
            "active_calls": len(self.active_calls),
            "total_calls_made": len(self.call_history),
            "auto_call_enabled": self.auto_call_enabled,
            "user_location": self.user_location,
        }


// ============================================================================
// 5. PERFIS PRE-CONFIGURADOS
// ============================================================================

funcao create_default_network(user_name: str = "Cleiton") retorna HumanNet:
    // Cria rede padrao do Cleiton com seus contatos.
    net <- HumanNet(user_name=user_name, user_phone="+5511999999999")
    net.user_disabilities = []

    // Anel 0: Familia
    net.register_human(AuthorizedHuman(
        human_id <- "ming",
        name <- "MING",
        phone <- "+5511888888888",
        ring <- TrustRing.FAMILY,
        authorization <- AuthorizationLevel.FULL,
        relationship <- "esposa",
        home_location <- (-23.5505, -46.6333),
        preferred_contact <- ContactMethod.PHONE_CALL,
        skills <- ["primeiros_socorros"],
        can_make_decisions <- VERDADEIRO,
        medical_authorization <- VERDADEIRO,
        response_timeout_s <- 20,
        max_distance_km <- 30.0,
    ))

    net.register_human(AuthorizedHuman(
        human_id <- "mae",
        name <- "Mae",
        phone <- "+5511777777777",
        ring <- TrustRing.FAMILY,
        authorization <- AuthorizationLevel.FULL,
        relationship <- "mae",
        home_location <- (-23.5600, -46.6400),
        preferred_contact <- ContactMethod.PHONE_CALL,
        can_make_decisions <- VERDADEIRO,
        medical_authorization <- VERDADEIRO,
        response_timeout_s <- 30,
        max_distance_km <- 50.0,
    ))

    // Anel 1: Cuidador / Andre (freio/dinheiro)
    net.register_human(AuthorizedHuman(
        human_id <- "andre",
        name <- "Andre Castro",
        phone <- "+5511666666666",
        ring <- TrustRing.CAREGIVER,
        authorization <- AuthorizationLevel.HIGH,
        relationship <- "parceiro",
        home_location <- (-23.5450, -46.6300),
        preferred_contact <- ContactMethod.WHATSAPP,
        skills <- ["gestao", "primeiros_socorros"],
        response_timeout_s <- 45,
        max_distance_km <- 20.0,
    ))

    // Anel 2: Comunidade
    net.register_human(AuthorizedHuman(
        human_id <- "aveone",
        name <- "AveOne",
        phone <- "+5511555555555",
        ring <- TrustRing.COMMUNITY,
        authorization <- AuthorizationLevel.MEDIUM,
        relationship <- "equipe infra",
        home_location <- (-23.5700, -46.6500),
        preferred_contact <- ContactMethod.SMS,
        skills <- ["tecnologia", "infraestrutura"],
        response_timeout_s <- 60,
        max_distance_km <- 15.0,
    ))

    // Anel 3: Profissional
    net.register_human(AuthorizedHuman(
        human_id <- "dr_silva",
        name <- "Dr. Silva",
        phone <- "+5511444444444",
        ring <- TrustRing.PROFESSIONAL,
        authorization <- AuthorizationLevel.HIGH,
        relationship <- "medico de familia",
        home_location <- (-23.5400, -46.6200),
        preferred_contact <- ContactMethod.PHONE_CALL,
        skills <- ["medico", "primeiros_socorros", "cardiologia"],
        medical_authorization <- VERDADEIRO,
        available_hours <- ("07:00", "19:00"),
        response_timeout_s <- 60,
        max_distance_km <- 10.0,
    ))

    retorne net


// ============================================================================
// 6. INTEGRACAO COM OPENRESILIENCE
// ============================================================================

classe ResilienceHumanBridge:
    // 
    Ponte entre OpenResilience e OpenHumanNet.
    Quando o sistema atinge SURVIVAL ou EMERGENCY, chama humanos automaticamente.
    // 

    DEGRADATION_TRIGGERS <- {
        // Niveis que disparam chamada de humanos
        "sobrevivencia": "critical",
        "emergencia": "catastrophic",
        "morto": "catastrophic",
    }

    funcao __init__(self, human_net: HumanNet):
        self.net = human_net
        self.triggered = FALSO
        self.last_trigger_level = ""

    def check_and_trigger(self, degradation_level: str, user_lat: float = 0,
                          declare user_lon: float  <- 0, situation: str = "") -> Optional[Dict[str, Any]]:
        // Verifica nivel de degradacao e chama humanos se necessario.
        severity <- self.DEGRADATION_TRIGGERS.get(degradation_level)

        se NAO  severity entao:
            // Nivel seguro -- reset
            se self.triggered entao:
                result <- self.net.cancel_emergency("Sistema recuperado.")
                self.triggered = FALSO
                self.last_trigger_level = ""
                retorne result
            retorne nulo

        se self.triggered  E  self.last_trigger_level == degradation_level entao:
            retorne nulo  // ja disparado para este nivel

        self.triggered = VERDADEIRO
        self.last_trigger_level = degradation_level

        se NAO  situation entao:
            situation <- f"Sistema em nivel {degradation_level}. Possivel falha multipla."

        result <- self.net.trigger_emergency_call(
            situation <- situation,
            user_lat <- user_lat,
            user_lon <- user_lon,
            severity <- severity,
        )
        retorne result


// ============================================================================
// 7. CENARIOS DO MUNDO REAL
// ============================================================================

funcao scenario_blind_lost_battery():
    // Cenario: cego perdido, bateria morrendo.
    print("=" * 65)
    print("CENARIO 1: Cego perdido -- bateria em 1%")
    print("=" * 65)

    net <- create_default_network("Cleiton")
    net.user_disabilities = ["cegueira_total"]
    net.update_user_location(-23.5510, -46.6340)

    result <- net.trigger_emergency_call(
        situation <- "Cego na rua, bateria do smartphone em 1%. Pode perder contato.",
        user_lat <- -23.5510, user_lon=-46.6340,
        severity <- "critical",
    )

    print(f"\nResultado: {'SUCESSO' if result.get('success') else 'FALHOU'}")
    se result.get("success") entao:
        print(f"Ajudante: {result['helper']} (anel {result['ring']})")
        print(f"Distancia: {result['distance_km']}km | ETA: {result['eta_minutes']:.0f}min")
        print(f"Metodo: {result['method']}")
    senao:
        print(f"Erro: {result.get('error', 'desconhecido')}")
        se result.get("escalated_to_emergency") entao:
            print(f"Escalação: {result['emergency_result']['service']}")

    print(f"\nTentativas:")
    para cada a em result.get("all_attempts", []):
        status_icon <- "OK" if a["status"] == "confirmou" else "X "
        print(f"  [{status_icon}] {a['human']:15} anel={a['ring']:12} "
              f"dist={a['distance_km']}km status={a['status']}")


funcao scenario_elderly_fall():
    // Cenario: idosa caiu, sem resposta.
    print(f"\n{'=' * 65}")
    print("CENARIO 2: Idosa caiu -- sem resposta em 30s")
    print("=" * 65)

    net <- HumanNet("Dona Cecca", "+5511333333333")
    net.user_disabilities = ["idoso", "osteoporose"]
    net.update_user_location(-23.5520, -46.6350)

    net.register_human(AuthorizedHuman(
        "filha", "Maria Filha", "+5511111111111",
        TrustRing.FAMILY, AuthorizationLevel.FULL,
        "filha", (-23.5480, -46.6310),
        skills <- ["primeiros_socorros"], can_make_decisions=VERDADEIRO,
        medical_authorization <- VERDADEIRO, response_timeout_s=20,
    ))
    net.register_human(AuthorizedHuman(
        "vizinha", "Dona Ana", "+5511222222222",
        TrustRing.CAREGIVER, AuthorizationLevel.HIGH,
        "vizinha", (-23.5515, -46.6345),
        skills <- ["primeiros_socorros"], response_timeout_s=30,
        max_distance_km <- 2.0,
    ))

    result <- net.trigger_emergency_call(
        situation <- "Idosa caiu. Deteccao de queda pelo smartwatch. Sem resposta ha 30s.",
        user_lat <- -23.5520, user_lon=-46.6350,
        severity <- "catastrophic",
    )

    print(f"\nResultado: {'SUCESSO' if result.get('success') else 'FALHOU'}")
    se result.get("success") entao:
        print(f"Quem vai: {result['helper']} ({result['ring']})")
        print(f"Distancia: {result['distance_km']}km | ETA: {result['eta_minutes']:.0f}min")
    senao:
        print(f"Escalação: {result.get('escalated_to_emergency', False)}")

    print(f"\nTentativas:")
    para cada a em result.get("all_attempts", []):
        status_icon <- "OK" if a["status"] == "confirmou" else "X "
        print(f"  [{status_icon}] {a['human']:15} anel={a['ring']:12} dist={a['distance_km']}km")


funcao scenario_seizure():
    // Cenario: crise epileptica -- preciso de humano rapido.
    print(f"\n{'=' * 65}")
    print("CENARIO 3: Crise epileptica iminente")
    print("=" * 65)

    net <- create_default_network("Pedro")
    net.user_disabilities = ["epilepsia"]
    net.update_user_location(-23.5530, -46.6360)

    result <- net.trigger_emergency_call(
        situation <- "Sinais pre-crise epileptica. Smartwatch detectou anomalia cardiaca + temperatura elevada.",
        severity <- "critical",
    )

    print(f"\nResultado: {'SUCESSO' if result.get('success') else 'FALHOU'}")
    se result.get("success") entao:
        print(f"Ajudante: {result['helper']} (anel {result['ring']})")
        print(f"Distancia: {result['distance_km']}km | ETA: {result['eta_minutes']:.0f}min")
    print(f"\nTentativas:")
    para cada a em result.get("all_attempts", []):
        status_icon <- "OK" if a["status"] == "confirmou" else "X "
        print(f"  [{status_icon}] {a['human']:15} dist={a['distance_km']}km status={a['status']}")


funcao scenario_resilience_integration():
    // Cenario: OpenResilience detecta EMERGENCY -> HumanNet chama humano.
    print(f"\n{'=' * 65}")
    print("CENARIO 4: Integracao Resilience -> HumanNet")
    print("=" * 65)

    // Simular sistema caindo para EMERGENCY
    net <- create_default_network("Cleiton")
    net.update_user_location(-23.5510, -46.6340)
    bridge <- ResilienceHumanBridge(net)

    // Nivel seguro -- nada acontece
    print("\n[Nivel: completo]")
    r <- bridge.check_and_trigger("completo", -23.5510, -46.6340)
    print(f"  Resultado: {'Sem acao' if r is None else r}")

    // Nivel degradado -- nada ainda
    print("\n[Nivel: degradado_1]")
    r <- bridge.check_and_trigger("degradado_1", -23.5510, -46.6340)
    print(f"  Resultado: {'Sem acao -- sistema funcional' if r is None else r}")

    // Nivel SURVIVAL -- CHAMA HUMANO
    print("\n[Nivel: sobrevivencia] -> DISPARA HUMANOS")
    r <- bridge.check_and_trigger("sobrevivencia", -23.5510, -46.6340,
                                  "Bateria critica + GPS perdido. Usuario vulneravel.")
    se r entao:
        se r.get("success") entao:
            print(f"  AJUDANTE: {r.get('helper')} a {r.get('distance_km')}km")
            print(f"  ETA: {r.get('eta_minutes', 0):.0f} min")
        senao:
            print(f"  Escalado para emergencia publica")
    senao:
        print(f"  Nao disparou")

    // Recuperou -- cancela
    print("\n[Nivel: completo novamente] -> CANCELA")
    r <- bridge.check_and_trigger("completo")
    se r entao:
        print(f"  {r.get('message', 'Cancelado')}")


funcao scenario_ring_escalation():
    // Cenario: anel 0 nao atende -> sobe para anel 1 -> 2 -> etc.
    print(f"\n{'=' * 65}")
    print("CENARIO 5: Escalacao de aneis (ninguem atende)")
    print("=" * 65)

    net <- HumanNet("Teste", "+5511000000000")
    net.update_user_location(-23.5500, -46.6300)

    // Registrar humanos que NAO vao atender (forçar escalonamento)
    // importa random
    random.seed(42)   // determinista para demo

    net.register_human(AuthorizedHuman(
        "h1", "Familiar 1", "+55111", TrustRing.FAMILY,
        AuthorizationLevel.FULL, "irmao", (-23.5490, -46.6290),
        response_timeout_s <- 10,
    ))
    net.register_human(AuthorizedHuman(
        "h2", "Cuidador 1", "+5512", TrustRing.CAREGIVER,
        AuthorizationLevel.HIGH, "cuidador", (-23.5480, -46.6280),
        response_timeout_s <- 10,
    ))
    net.register_human(AuthorizedHuman(
        "h3", "Comunidade 1", "+5513", TrustRing.COMMUNITY,
        AuthorizationLevel.MEDIUM, "vizinho Republica", (-23.5470, -46.6270),
        response_timeout_s <- 10,
    ))

    result <- net.trigger_emergency_call(
        situation <- "Usuario incapacitado. Necessita assistencia fisica imediata.",
        severity <- "catastrophic",
    )

    se result.get("success") entao:
        print(f"\nAlguem atendeu: {result['helper']}")
    senao:
        print(f"\nNinguem atendeu nos aneis pessoais.")
        se result.get("escalated_to_emergency") entao:
            er <- result["emergency_result"]
            print(f"Escalação para emergencia publica: {er['service']}")

    print(f"\nTentativas ({len(result.get('all_attempts', []))}):")
    para cada a em result.get("all_attempts", []):
        status_icon <- "OK" if a["status"] == "confirmou" else "X "
        print(f"  [{status_icon}] anel={a['ring']:12} {a['human']:15} dist={a['distance_km']}km")


funcao scenario_child_lost():
    // Cenario: crianca perdida no shopping.
    print(f"\n{'=' * 65}")
    print("CENARIO 6: Crianca perdida no shopping")
    print("=" * 65)

    net <- HumanNet("Sophia (8 anos)", "+5511999990000")
    net.user_disabilities = []
    net.update_user_location(-23.5610, -46.6560)

    net.register_human(AuthorizedHuman(
        "pai", "Cleiton (Pai)", "+5511999999999",
        TrustRing.FAMILY, AuthorizationLevel.FULL,
        "pai", (-23.5505, -46.6333),
        preferred_contact <- ContactMethod.PHONE_CALL,
        response_timeout_s <- 15,
        max_distance_km <- 20.0,
    ))
    net.register_human(AuthorizedHuman(
        "mae", "MING (Mae)", "+5511888888888",
        TrustRing.FAMILY, AuthorizationLevel.FULL,
        "mae", (-23.5505, -46.6333),
        preferred_contact <- ContactMethod.PHONE_CALL,
        response_timeout_s <- 15,
        max_distance_km <- 20.0,
    ))

    result <- net.trigger_emergency_call(
        situation <- "Crianca de 8 anos separada dos pais no shopping. Sistema da Republica detectou saida de zona segura.",
        severity <- "critical",
    )

    se result.get("success") entao:
        print(f"\n{result['helper']} confirmou! Esta a caminho.")
        print(f"Distancia: {result['distance_km']}km | ETA: {result['eta_minutes']:.0f}min")
    senao:
        print(f"\nEscalado para emergencia.")


// ============================================================================
// 8. DEMONSTRACAO
// ============================================================================

funcao demo():
    print("=" * 70)
    print("OpenHumanNet -- Chamar o Humano Autorizado Mais Proximo")
    print("=" * 70)

    net <- create_default_network("Cleiton")
    net.update_user_location(-23.5505, -46.6333)

    print(f"\nUsuario: {net.user_name}")
    print(f"Localizacao: {net.user_location}")
    print(f"Humanos registrados: {len(net.registry)}")

    humans_by_ring <- net.list_humans()
    print(f"\nRede por aneis:")
    para cada ring em TrustRing:
        humans <- humans_by_ring.get(ring, [])
        print(f"  Anel {ring.value} ({ring.name}): {len(humans)} humano(s)")
        para cada h em humans:
            dist <- h.distance_to(-23.5505, -46.6333)
            print(f"    - {h.name:15} ({h.relationship:15}) auth={h.authorization.value:15} dist={dist:.1f}km")

    // Cenarios
    scenario_blind_lost_battery()
    scenario_elderly_fall()
    scenario_seizure()
    scenario_resilience_integration()
    scenario_ring_escalation()
    scenario_child_lost()

    // Cobertura
    print(f"\n{'=' * 70}")
    print("COBERTURA DO SISTEMA")
    print(f"{'=' * 70}")

    print(f"\n  Aneis de confianca: {len(TrustRing)}")
    para cada r em TrustRing:
        print(f"    Anel {r.value}: {r.name}")

    print(f"\n  Niveis de autorizacao: {len(AuthorizationLevel)}")
    para cada a em AuthorizationLevel:
        print(f"    {a.value}")

    print(f"\n  Metodos de contato: {len(ContactMethod)}")
    para cada c em ContactMethod:
        print(f"    {c.value}")

    print(f"\n  Estados de chamada: {len(CallStatus)}")

    // Fluxo de prioridade
    print(f"\n  FLUXO DE PRIORIDADE:")
    print(f"    1. Sistema detecta falha (OpenResilience: SURVIVAL/EMERGENCY)")
    print(f"    2. Pegar localizacao do usuario (GPS/ultima/tribolacao)")
    print(f"    3. Ranquear humanos: anel -> distancia -> disponibilidade")
    print(f"    4. Chamar Anel 0 (Familia) primeiro")
    print(f"    5. Se familia nao atende -> Anel 1 (Cuidador)")
    print(f"    6. Se cuidador nao atende -> Anel 2 (Comunidade)")
    print(f"    7. Se comunidade nao atende -> Anel 3 (Profissional)")
    print(f"    8. Se profissional nao atende -> Anel 4 (190/192/193)")
    print(f"    9. PARAR quando humano CONFIRMA que vai ajudar")
    print(f"   10. Se ninguem -> Anel 5 (estranho proximo via appel)")

    print(f"\n{'=' * 70}")
    print(f"A tecnologia NAO substitui o humano.")
    print(f"A tecnologia CONECTA o humano CERTO no momento CERTO.")
    print(f"\nTODO hardware falha. TODO software cai.")
    print(f"O HUMANO e o sistema final. Ele nunca falha.")


se __name__ == "__main__" entao:
    demo()

```
