# OpenInbox -- A Fila Unificada de Atencao

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_inbox.py`

**Descricao:** ==========================================
"5 apps competindo pela sua atencao = 5 ladroes de tempo.
 1 fila que voce controla = 1 cerebro que decide."
CONCEITO:
  Voce tem OpenSocialNetwork com 5 modulos:
  - FEED (X/Twitter)
  - VISUAL (Instagram/TikTok)
  - COMUNIDADE (Discord)
  - MENSAGEIRO (WhatsApp)
  - MARKETPLACE (OLX)
  Cada um quer sua atencao AGORA. Notificacao aqui, badge ali,
  sino acola. 5 apps = 5 fontes de ansiedade.
  A SOLUCAO DA REPUBLICA:
  TUDO entra numa UNICA FILA.
  Voce NUNCA abre 5 apps.
  Voce abre a FILA. A fila mostra o que importa.
  Na ordem que VOCE decide. Na hora que VOCE quer.
  A fila e o unico ponto de entrada pro seu cerebro.
COMO FUNCIONA:
  1. Cada modulo joga eventos na fila
  2. A fila classifica por prioridade (NAO por engajamento)
  3. Voce processa a fila QUANDO QUISER (batch, nao ping continuo)
  4. O que nao foi processado em 24h = arquivado (nao e urgente)
  5. Silencio total ate voce abrir a fila
  6. Modo Foco: so emergencies (saude, seguranca, familia)
PRINCIPIO CONSTITUCIONAL:
  P2 Autonomia Corporal: seu cerebro e seu.
  Nenhuma app tem direito de invadir sua atencao sem permissao.
  Notificacao push sem consentimento = violacao corporal digital.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenInbox -- A Fila Unificada de Atencao
==========================================

"5 apps competindo pela sua atencao = 5 ladroes de tempo.
 1 fila que voce controla = 1 cerebro que decide."

CONCEITO:
  Voce tem OpenSocialNetwork com 5 modulos:
  - FEED (X/Twitter)
  - VISUAL (Instagram/TikTok)
  - COMUNIDADE (Discord)
  - MENSAGEIRO (WhatsApp)
  - MARKETPLACE (OLX)

  Cada um quer sua atencao AGORA. Notificacao aqui, badge ali,
  sino acola. 5 apps = 5 fontes de ansiedade.

  A SOLUCAO DA REPUBLICA:
  TUDO entra numa UNICA FILA.
  Voce NUNCA abre 5 apps.
  Voce abre a FILA. A fila mostra o que importa.
  Na ordem que VOCE decide. Na hora que VOCE quer.

  A fila e o unico ponto de entrada pro seu cerebro.

COMO FUNCIONA:
  1. Cada modulo joga eventos na fila
  2. A fila classifica por prioridade (nao por engajamento)
  3. Voce processa a fila QUANDO QUISER (batch, nao ping continuo)
  4. O que nao foi processado em 24h = arquivado (nao e urgente)
  5. Silencio total ate voce abrir a fila
  6. Modo Foco: so emergencies (saude, seguranca, familia)

PRINCIPIO CONSTITUCIONAL:
  P2 Autonomia Corporal: seu cerebro e seu.
  Nenhuma app tem direito de invadir sua atencao sem permissao.
  Notificacao push sem consentimento = violacao corporal digital.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa time
// importa hashlib
// importa json
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, deque de collections
// importa datetime, timedelta de datetime


// ============================================================================
// 1. ORIGEM DOS EVENTOS (que modulo gerou)
// ============================================================================

classe SourceModule herda de Enum:
    // De que modulo do OpenSocialNetwork veio o evento.
    FEED = "feed"  // X/Twitter -- posts, replies, mentions
    VISUAL = "visual"  // Instagram/TikTok -- fotos, videos, tags
    COMUNIDADE = "comunidade"  // Discord -- canais, eventos, mencoes
    MENSAGEIRO = "mensageiro"  // WhatsApp -- DMs, grupos
    MARKETPLACE = "marketplace"  // OLX -- trocas, ofertas
    SYSTEM = "sistema"  // Republica -- votacoes, creditos, alertas
    HEALTH = "saude"  // OpenHealth -- consultas, vacinas
    CALENDAR = "calendario"  // OpenCalendar -- compromissos, festas


classe EventType herda de Enum:
    // Tipo de evento que entra na fila.
    // Mensageiro
    DM = "dm"  // mensagem direta
    GROUP_MSG = "grupo"  // mensagem em grupo
    CALL = "chamada"  // chamada de voz/video
    // Feed
    REPLY = "resposta"  // responderam seu post
    MENTION = "mencao"  // marcaram voce
    REPOST = "repost"  // repostaram voce
    // Visual
    TAGGED = "marcado_foto"  // marcaram em foto/video
    COMMENT_MEDIA = "comentario_foto"
    // Comunidade
    CHANNEL_MSG = "canal"  // mensagem em canal de comunidade
    EVENT_REMINDER = "evento"  // lembrete de evento da comunidade
    ROLE_ASSIGNED = "cargo"  // recebeu cargo na comunidade
    // Marketplace
    OFFER_RECEIVED = "oferta"  // alguem quer trocar/comprar
    OFFER_ACCEPTED = "aceito"  // sua oferta foi aceita
    // Sistema
    VOTE_OPEN = "votacao"  // votacao aberta na Republica
    CREDIT_ARRIVED = "credito"  // credito de acesso chegou
    DEADLINE = "prazo"  // prazo de algo importante
    // Saude
    APPOINTMENT = "consulta"  // consulta marcada
    VACINE_DUE = "vacina"  // vacina no prazo
    // Calendario
    SCHEDULED = "compromisso"  // compromisso agendado


classe Priority herda de Enum:
    // Prioridade do evento na fila.

    O sistema NUNCA usa prioridade para maximizar engajamento.
    Prioridade = importancia REAL para a vida da pessoa.
    // 
    EMERGENCY = 0 // vida/saude/seguranca AGORA
    HIGH = 1 // resposta pessoal direta (DM, reply, chamada)
    NORMAL = 2 // atividade de comunidade, eventos
    LOW = 3 // repost, tag, comentario generico
    NOISE = 4 // anything else -- batch processar quando der


// Mapeamento automatico tipo -> prioridade base
TYPE_PRIORITY = {
    EventType.DM: Priority.HIGH,
    EventType.CALL: Priority.EMERGENCY,
    EventType.GROUP_MSG: Priority.NORMAL,
    EventType.REPLY: Priority.HIGH,
    EventType.MENTION: Priority.NORMAL,
    EventType.REPOST: Priority.LOW,
    EventType.TAGGED: Priority.LOW,
    EventType.COMMENT_MEDIA: Priority.LOW,
    EventType.CHANNEL_MSG: Priority.LOW,
    EventType.EVENT_REMINDER: Priority.NORMAL,
    EventType.ROLE_ASSIGNED: Priority.LOW,
    EventType.OFFER_RECEIVED: Priority.NORMAL,
    EventType.OFFER_ACCEPTED: Priority.HIGH,
    EventType.VOTE_OPEN: Priority.HIGH,
    EventType.CREDIT_ARRIVED: Priority.NORMAL,
    EventType.DEADLINE: Priority.HIGH,
    EventType.APPOINTMENT: Priority.HIGH,
    EventType.VACINE_DUE: Priority.HIGH,
    EventType.SCHEDULED: Priority.NORMAL,
}


classe ContactRelation herda de Enum:
    // Quao proxima e a pessoa que gerou o evento.
    Isso afeta prioridade -- familia > guardiao > conhecido > desconhecido.
    // 
    FAMILY = "familia"
    STEWARD = "guardiao"
    ALLY = "aliado"
    COMMUNITY = "comunidade"
    ACQUAINTANCE = "conhecido"
    UNKNOWN = "desconhecido"
    BOT = "bot"


// ============================================================================
// 2. EVENTO NA FILA
// ============================================================================

// decorador: @dataclass
classe QueueItem:
    // Um item na fila de atencao.
    item_id: texto
    source: SourceModule
    event_type: EventType
    sender_handle: texto
    sender_name: texto
    seja sender_relation: ContactRelation = ContactRelation.UNKNOWN
    seja content_preview: texto = ""  // primeiros 100 chars
    seja content_url: texto = ""  // link profundo pro modulo
    seja timestamp: flutuante = field(default_factory=time.time)

    // Prioridade
    seja base_priority: Priority = Priority.NOISE
    seja final_priority: Priority = Priority.NOISE
    seja priority_reason: texto = ""

    // Estado
    seja read: logico = falso
    seja archived: logico = falso
    seja acted_upon: logico = falso // usuario respondeu/interagiu
    seja auto_archived: logico = falso // sistema arquivou (expirou)

    // Contexto
    seja requires_response: logico = falso // precisa de acao do usuario
    seja response_deadline: flutuante = 0.0 // prazo para responder (0 = sem prazo)

    // Metadados anti-engajamento
    seja has_media: logico = falso
    seja is_sensational: logico = falso // sistema detecta clickbait
    seja engagement_bait: logico = falso // sistema detecta tentativa de viciar

    // decorador: @property
    funcao age_hours(self) -> flutuante:
        retorne (time.time() - self.timestamp) / 3600

    // decorador: @property
    funcao is_expired(self) -> logico:
        // Item com mais de 24h nao lido = arquivar (nao era urgente).
        retorne self.age_hours > 24 e nao self.read


// ============================================================================
// 3. MOTOR DE PRIORIZACAO (NAO de engajamento)
// ============================================================================

classe AttentionPrioritizer:
    // Calcula prioridade final de cada item.

    CRITERIOS (em ordem):
    1. Tipo do evento (DM > repost)
    2. Relacao com remetente (familia > desconhecido)
    3. requer resposta? (pergunta > declaracao)
    4. Prazo? (votacao fechando > sem prazo)
    5. Idade (mais antigo nao lido = levemente mais urgente)
    6. PENALIDADE: engagement bait = rebaixado para NOISE
    // 

    // Bonus de prioridade por relacao
    RELATION_BONUS = {
        ContactRelation.FAMILY: -2, // sobe 2 niveis
        ContactRelation.STEWARD: -1, // sobe 1 nivel
        ContactRelation.ALLY: 0,
        ContactRelation.COMMUNITY: 0,
        ContactRelation.ACQUAINTANCE: 1, // desce 1
        ContactRelation.UNKNOWN: 2, // desce 2
        ContactRelation.BOT: 4, // NOISE maximo
    }

    funcao prioritize(self, item: QueueItem) -> QueueItem:
        // Calcula prioridade final.
        base_val = item.base_priority.value

        // Bonus por relacao
        relation_adj = self.RELATION_BONUS.get(item.sender_relation, 2)
        score = base_val + relation_adj

        // Requer resposta? sobe 1 nivel
        se item.requires_response entao:
            score = score - 1

        // Tem prazo? sobe conforme prazo se aproxima
        se item.response_deadline > 0 entao:
            hours_left = (item.response_deadline - time.time()) / 3600
            se hours_left < 2 entao:
                score = score - 2 // URGENTE
            senao se hours_left < 24 entao:
                score = score - 1

        // Penalidade: engagement bait
        se item.engagement_bait entao:
            score = Priority.NOISE.value // sempre NOISE

        // Penalidade: sensational/clickbait
        se item.is_sensational entao:
            score = score + 1

        // Clamp 0-4
        score = maximo(0, minimo(4, score))

        item.final_priority = Priority(score)

        // Razao
        reasons = []
        se item.sender_relation == ContactRelation.FAMILY entao:
            reasons.append("familia")
        se item.sender_relation == ContactRelation.STEWARD entao:
            reasons.append("guardiao")
        se item.requires_response entao:
            reasons.append("requer resposta")
        se item.engagement_bait entao:
            reasons.append("engagement bait -> noise")
        se item.is_sensational entao:
            reasons.append("sensacionalismo penalizado")
        reasons ? item.priority_reason = ", ".join(reasons) : "padrao"

        retorne item

    // decorador: @staticmethod
    funcao detect_engagement_bait(text: texto) -> logico:
        // Detecta tentativa de viciar atencao.
        bait_indicators = [
            "voce nao vai acreditar",
            "o final vai te chocar",
            "todos estao falando",
            "antes que apaguem",
            "compartilhe antes",
            "so os 1% sabem",
            " isso vai mudar tudo",
            "parou tudo por causa",
            "o que aconteceu vai",
            "ninguem te conta",
        ]
        text_lower = text.lower()
        retorne any(bait in text_lower para bait em bait_indicators)

    // decorador: @staticmethod
    funcao detect_sensational(text: texto) -> logico:
        // Detecta sensacionalismo.
        caps_ratio = soma(1 para c em text if c.isupper()) / maximo(tamanho(text), 1)
        has_many_emojis = text.count("!") + text.count("?") > 3
        retorne caps_ratio > 0.3 ou has_many_emojis


// ============================================================================
// 4. A FILA UNIFICADA
// ============================================================================

classe UnifiedInbox:
    // A fila unificada de atencao.

    ESTE e O UNICO PONTO DE ENTRADA PARA O CEREBRO DO CIDADAO.

    COMO USAR:
    1. Todos os modulos jogam eventos aqui via enqueue()
    2. O cidadao NUNCA abre 5 apps. Abre a FILA.
    3. A fila mostra itens por prioridade (nao por engajamento)
    4. Cidadao processa em BATCH (1-3x/dia), nao em ping continuo
    5. Silencio total entre sessoes de processamento

    MODOS:
    - NORMAL: mostra tudo por prioridade
    - FOCO: so EMERGENCY + FAMILY + HEALTH ( resto bloqueado)
    - DIGEST: so摘要 das ultimas 24h (1 item por categoria)
    - VACATION: tudo arquivado, so EMERGENCY passa
    // 

    funcao __init__(self):
        self.queue: deque[QueueItem] = deque()
        self.prioritizer = AttentionPrioritizer()
        self.processed_history: [Dict] = []

        // Contatos especiais
        self.family_handles: set = set()
        self.steward_handles: set = set()

        // Configuracao
        self.mode: InboxMode = InboxMode.NORMAL
        self.auto_archive_hours: inteiro = 24
        self.max_daily_items: inteiro = 100 // protecao: maximo 100 itens/dia no cerebro
        self.items_today: inteiro = 0
        self.last_reset_date: texto = ""

        // Stats
        self.total_enqueued: inteiro = 0
        self.total_processed: inteiro = 0
        self.total_archived: inteiro = 0
        self.bait_blocked: inteiro = 0

    funcao mark_family(self, handles: [texto]) -> None:
        para cada h em handles:
            self.family_handles.add(h.lower().lstrip("@"))

    funcao mark_steward(self, handles: [texto]) -> None:
        para cada h em handles:
            self.steward_handles.add(h.lower().lstrip("@"))

    funcao _resolve_relation(self, handle: texto) -> ContactRelation:
        h = handle.lower().lstrip("@")
        se h in self.family_handles entao:
            retorne ContactRelation.FAMILY
        se h in self.steward_handles entao:
            retorne ContactRelation.STEWARD
        retorne ContactRelation.UNKNOWN

    funcao _reset_daily_if_needed(self) -> None:
        today = datetime.now().strftime("%Y-%m-%d")
        se today != self.last_reset_date entao:
            self.items_today = 0
            self.last_reset_date = today

    funcao enqueue(self, source: SourceModule, event_type: EventType,
                sender_handle: texto, sender_name: texto,
                seja content_preview: texto = "",
                seja requires_response: logico = falso,
                seja response_deadline: flutuante = 0.0,
                seja has_media: logico = falso) -> {texto: qualquer}:
        // Adiciona item na fila. O unico ponto de entrada.

        // Protecao: max diaria (anti-overload)
        self._reset_daily_if_needed()
        se self.items_today >= self.max_daily_items entao:
            retorne {"accepted": falso, "reason": "Limite diario atingido. Cerebro protegido."}

        // Detectar bait
        is_bait = self.prioritizer.detect_engagement_bait(content_preview)
        is_sensational = self.prioritizer.detect_sensational(content_preview)

        item = QueueItem(
            item_id = hashlib.md5(
                "{source.value}{event_type.value}{sender_handle}{time.time()}".encode()
            ).hexdigest()[:10],
            source = source,
            event_type = event_type,
            sender_handle = sender_handle,
            sender_name = sender_name,
            sender_relation = self._resolve_relation(sender_handle),
            content_preview = content_preview[:120],
            base_priority = TYPE_PRIORITY.get(event_type, Priority.NOISE),
            requires_response = requires_response,
            response_deadline = response_deadline,
            has_media = has_media,
            engagement_bait = is_bait,
            is_sensational = is_sensational,
        )

        // Calcular prioridade final
        self.prioritizer.prioritize(item)

        // Modo FOCO: bloqueia tudo que nao e emergency/familia/saude
        se self.mode == InboxMode.FOCUS entao:
            allowed = (item.final_priority == Priority.EMERGENCY
                        ou item.sender_relation == ContactRelation.FAMILY
                        ou item.source == SourceModule.HEALTH)
            se nao allowed entao:
                item.auto_archived = verdadeiro
                self.total_archived += 1
                retorne {"accepted": falso, "reason": "Modo Foco ativo. Arquivado."}

        // Modo VACATION: so emergency
        se self.mode == InboxMode.VACATION entao:
            se item.final_priority != Priority.EMERGENCY entao:
                item.auto_archived = verdadeiro
                self.total_archived += 1
                retorne {"accepted": falso, "reason": "Modo Ferias. So emergencias."}

        self.queue.append(item)
        self.total_enqueued += 1
        self.items_today += 1

        se is_bait entao:
            self.bait_blocked += 1

        retorne {
            "accepted": verdadeiro,
            "item_id": item.item_id,
            "priority": item.final_priority.name,
            "source": source.value,
        }

    funcao process_batch(self, limit: inteiro = 20) -> [QueueItem]:
        // Processa um lote da fila.

        Retorna itens ordenados por prioridade (menor numero = mais urgente).
        O cidadao processa 1-3x/dia. NUNCA em tempo real.
        // 
        // Auto-arquivar expirados
        self._auto_archive()

        // Ordenar por prioridade
        items = ordene(
            [i para i em self.queue if nao i.archived e nao i.read],
            key = (i) -> (i.final_priority.value, i.timestamp),
        )

        batch = items[:limit]

        // Marcar como lido
        para cada item em batch:
            item.read = verdadeiro
            self.total_processed += 1

        retorne batch

    funcao _auto_archive(self) -> None:
        // Arquiva itens nao lidos com mais de 24h.
        para cada item em self.queue:
            se item.is_expired e nao item.archived entao:
                item.archived = verdadeiro
                item.auto_archived = verdadeiro
                self.total_archived += 1

    funcao act_on(self, item_id: texto) -> logico:
        // Marca item como atuado (respondeu/interagiu).
        para cada item em self.queue:
            se item.item_id == item_id entao:
                item.acted_upon = verdadeiro
                retorne verdadeiro
        retorne falso

    funcao dismiss(self, item_id: texto) -> logico:
        // Descarta item sem agir.
        para cada item em self.queue:
            se item.item_id == item_id entao:
                item.archived = verdadeiro
                retorne verdadeiro
        retorne falso

    funcao stats(self) -> {texto: qualquer}:
        // Estatisticas da fila.
        by_source = defaultdict(inteiro)
        by_priority = defaultdict(inteiro)
        unread = 0
        para cada item em self.queue:
            se nao item.archived entao:
                by_source[item.source.value] += 1
                se nao item.read entao:
                    unread = unread + 1
                    by_priority[item.final_priority.name] += 1

        retorne {
            "total_in_queue": tamanho(self.queue) - self.total_archived,
            "unread": unread,
            "by_source": dict(by_source),
            "by_priority": dict(by_priority),
            "total_enqueued": self.total_enqueued,
            "total_processed": self.total_processed,
            "total_archived": self.total_archived,
            "bait_blocked": self.bait_blocked,
            "mode": self.mode.value,
            "items_today": self.items_today,
            "daily_limit": self.max_daily_items,
        }

    funcao digest_24h(self) -> {texto: qualquer}:
        // Resumo das ultimas 24h. 1 item por categoria.

        Em vez de ver 200 itens, ve 5 linhas:
        - "3 DMs (1 da familia, 2 da comunidade)"
        - "12 replies no feed (2 de guardioes)"
        - "1 evento de comunidade amanha"
        - "1 votacao aberta (fecha em 2h)"
        - "4 ofertas no marketplace"
        // 
        cutoff = time.time() - 86400
        recent = [i para i em self.queue
                  if i.timestamp > cutoff e nao i.archived]

        summary = defaultdict(() -> {"count": 0, "highlights": []})
        para cada item em recent:
            src = item.source.value
            summary[src]["count"] += 1
            if (item.final_priority.value <= 1
                 e  tamanho(summary[src]["highights"]) < 2
                se "highights" in summary[src] else True) entao:
                se tamanho(summary[src]["highlights"]) < 2 entao:
                    summary[src]["highlights"].append({
                        "from": item.sender_name,
                        "preview": item.content_preview[:60],
                        "priority": item.final_priority.name,
                    })

        retorne {
            "period": "24h",
            "categories": tamanho(summary),
            "total": tamanho(recent),
            "digest": dict(summary),
        }


classe InboxMode herda de Enum:
    NORMAL = "normal"  // tudo por prioridade
    FOCUS = "foco"  // so emergency + familia + saude
    DIGEST = "digest"  // so resumo
    VACATION = "ferias"  // so emergency


// ============================================================================
// 5. SIMULADOR: 5 APPS -> 1 FILA
// ============================================================================

funcao simulate_five_apps_one_inbox() -> None:
    // Simula eventos de 5 modulos diferentes entrando numa so fila.

    inbox = UnifiedInbox()
    inbox.mark_family(["@mae_cleiton", "@irma"])
    inbox.mark_steward(["@ana_med", "@joao_eco", "@pedro_net", "@lux_ai"])

    imprima("=" * 75)
    imprima("  OPENINBOX -- A FILA UNIFICADA DE ATENCAO")
    imprima('  "5 apps competindo = 5 ladroes de tempo. 1 fila = 1 cerebro."')
    imprima("=" * 75)

    // === Eventos chegando de 5 fontes diferentes ===
    events = [
        // MENSAGEIRO (WhatsApp)
        (SourceModule.MENSAGEIRO, EventType.DM, "@mae_cleiton", "Mae",
         "Filho, almoça comigo domingo?", verdadeiro),
        (SourceModule.MENSAGEIRO, EventType.DM, "@colega_trabalho", "Carlos",
         "voce viu o email?", verdadeiro),
        (SourceModule.MENSAGEIRO, EventType.GROUP_MSG, "@grupo_familia",
         "Grupo Familia", "Tia chegou de viagem!", falso),

        // FEED (X/Twitter)
        (SourceModule.FEED, EventType.REPLY, "@ana_med", "Ana",
         "Concordo com seu post sobre OpenHealth!", verdadeiro),
        (SourceModule.FEED, EventType.MENTION, "@random_user", "Bot123",
         "@clouramlearning VEJA ISSOOO!!! NINGUEM CONTA!!!", falso),
        (SourceModule.FEED, EventType.REPOST, "@seguidor1", "Joao Seguidor",
         "repostou seu thread", falso),

        // VISUAL (Instagram/TikTok)
        (SourceModule.VISUAL, EventType.TAGGED, "@amigo_foto", "Pedro Fotografo",
         "marcou voce numa foto", falso),
        (SourceModule.VISUAL, EventType.COMMENT_MEDIA, "@unknown_2", "Random",
         "oi", falso),

        // COMUNIDADE (Discord)
        (SourceModule.COMUNIDADE, EventType.CHANNEL_MSG, "@comunidade_saude",
         "Comunidade Saude", "Discutindo novo protocolo OpenHealth", falso),
        (SourceModule.COMUNIDADE, EventType.EVENT_REMINDER, "@comunidade_tech",
         "Comunidade Tech", "Workshop Rust amanha 19h", verdadeiro),
        (SourceModule.COMUNIDADE, EventType.ROLE_ASSIGNED, "@comunidade_geral",
         "Sistema", "Voce foi eleito moderador do canal cultura", falso),

        // MARKETPLACE
        (SourceModule.MARKETPLACE, EventType.OFFER_RECEIVED, "@produtor_local",
         "Sementeira Comunitaria", "Tenho mudas de frutas para trocar", verdadeiro),
        (SourceModule.MARKETPLACE, EventType.OFFER_ACCEPTED, "@vizinho_ana",
         "Ana Vizinha", "Aceito sua oferta da ferramenta", falso),

        // SISTEMA
        (SourceModule.SYSTEM, EventType.VOTE_OPEN, "@republica", "Republica",
         "Votacao aberta: novo sistema OpenMobility. Fecha em 6h.",
         verdadeiro, time.time() + 6*3600),

        // SAUDE
        (SourceModule.HEALTH, EventType.VACINE_DUE, "@openhealth", "OpenHealth",
         "Sua dose de reforco esta disponivel", falso),
    ]

    imprima("\n  5 APPS GERANDO EVENTOS SIMULTANEAMENTE...\n")
    para source, etype, handle, name, preview, requires_resp, *rest in events:
        deadline = rest ? rest[0] : 0
        result = inbox.enqueue(source, etype, handle, name,
                               preview, requires_resp, deadline)
        status = result.get("accepted") ? "ACEITO" : "BLOQUEADO"
        prio = result.get("priority", "?")
        imprima("  [{status:>8}] [{prio:>9}] {source.value:<12} "
              "@{handle:<20} {preview[:40]}")

    // === Estatisticas ===
    imprima("\n\n  === FILA APOS INGESTAO ===\n")
    stats = inbox.stats()
    imprima("  Total na fila:     {stats['total_in_queue']}")
    imprima("  Nao lidos:         {stats['unread']}")
    imprima("  Por fonte:         {stats['by_source']}")
    imprima("  Por prioridade:    {stats['by_priority']}")
    imprima("  Bait bloqueado:    {stats['bait_blocked']}")
    imprima("  Limite diario:     {stats['items_today']}/{stats['daily_limit']}")

    // === Processar lote ===
    imprima("\n\n  === PROCESSANDO LOTE (batch, nao ping) ===\n")
    batch = inbox.process_batch(limit=10)
    imprima("  {'Prioridade':<12} {'Fonte':<12} {'De':<22} {'Preview'}")
    imprima("  {'-'*75}")
    para cada item em batch:
        imprima("  [{item.final_priority.name:<10}] {item.source.value:<12} "
              "{item.sender_name:<22} {item.content_preview[:35]}")
        se item.priority_reason  e  item.priority_reason != "padrao" entao:
            imprima("  {'':>25} razao: {item.priority_reason}")

    // === Modo Foco ===
    imprima("\n\n  === MODO FOCO ATIVADO ===\n")
    inbox.mode = InboxMode.FOCUS
    imprima("  So EMERGENCIES + FAMILIA + SAUDE passam. Resto arquivado.\n")

    inbox.queue.clear()
    inbox.enqueue(SourceModule.FEED, EventType.MENTION, "@random_bot",
                  "Spammer", "VEJA ISSO ANTES QUE APAGUEM!!!", falso)
    inbox.enqueue(SourceModule.MENSAGEIRO, EventType.DM, "@mae_cleiton",
                  "Mae", "Filho, ligou?", verdadeiro)
    inbox.enqueue(SourceModule.HEALTH, EventType.VACINE_DUE,
                  "@openhealth", "OpenHealth", "Reforgo disponivel", falso)
    inbox.enqueue(SourceModule.VISUAL, EventType.TAGGED, "@amigo",
                  "Amigo", "marcou voce", falso)

    batch = inbox.process_batch(limit=10)
    imprima("  {'Prioridade':<12} {'Fonte':<12} {'De':<22} {'Preview'}")
    imprima("  {'-'*75}")
    para cada item em batch:
        imprima("  [{item.final_priority.name:<10}] {item.source.value:<12} "
              "{item.sender_name:<22} {item.content_preview[:35]}")
    se nao batch entao:
        imprima("  (fila vazia -- tudo foi arquivado pelo Modo Foco)")

    stats = inbox.stats()
    imprima("\n  Arquivados pelo Modo Foco: {stats['total_archived']}")

    // === Digest 24h ===
    imprima("\n\n  === DIGEST 24H (resumo em vez de lista) ===\n")
    inbox.mode = InboxMode.NORMAL
    digest = inbox.digest_24h()
    imprima("  Categorias: {digest['categories']}")
    imprima("  Total: {digest['total']} itens nas ultimas 24h")
    para cada (cat, data) em digest["digest"].items():
        hl = "; ".join(h["from"] para h em data.get("highlights", []))
        imprima("    {cat:<14} {data['count']} itens"
              hl ? + (" (destaques: {hl})" : ""))

    // === Filosofia ===
    imprima("\n\n{'='*75}")
    imprima("  COMO O OPENINBOX PROTEGE SEU CEREBRO")
    imprima("{'='*75}")
    imprima("""
  ANTES (5 apps separadas):
    - WhatsApp: 3 notificacoes
    - X/Twitter: 8 notificacoes
    - Instagram: 5 notificacoes
    - Discord: 12 notificacoes
    - Marketplace: 4 notificacoes
    TOTAL: 32 pings competindo pela sua atencao
    RESULTADO: ansiedade, context-switching, overload

  DEPOIS (OpenInbox):
    - 32 eventos entram na fila
    - Sistema prioriza (familia > guardiao > ruido)
    - Engagement bait -> NOISE (rebaixado)
    - Sensacionalismo -> penalizado
    - Max 100 itens/dia no cerebro
    - Voce processa 1-3x/dia em BATCH
    - Silencio total entre sessoes
    RESULTADO: 1 fila, 1 cerebro, zero ansiedade

  MODOS:
    NORMAL -- tudo por prioridade
    FOCO -- so emergency + familia + saude
    DIGEST -- so resumo (5 linhas em vez de 200)
    FERIAS -- so emergency, resto arquivado

  PRINCIPIO:
    P2 Autonomia Corporal: seu cerebro e SEU.
    Nenhuma app invade sem permissao.
    Notificacao push sem consentimento = violacao corporal digital.
    A fila e o unico portao. Voce tem a chave.
// )
    imprima("{'='*75}")
    imprima("  OpenInbox: {stats['total_enqueued']} eventos -> "
          "{stats['total_processed']} processados -> "
          "{stats['bait_blocked']} bait bloqueado.")
    imprima("  5 apps. 1 fila. 0 ansiedade.")
    imprima("{'='*75}")


// ============================================================================

se __name__ == "__main__" entao:
    simulate_five_apps_one_inbox()

```
