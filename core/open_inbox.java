// OpenInbox -- A Fila Unificada de Atencao -- gerado de Portugol++
public class OpeninboxAFilaUnificadaDeAtencao {

    // !/usr/bin/env python3
    //
    OpenInbox -- A Fila Unificada de Atencao;
    ==========================================;
    "5 apps competindo pela sua atencao = 5 ladroes de tempo.;
    1 fila que voce controla = 1 cerebro que decide.";
    CONCEITO:;
    Voce tem OpenSocialNetwork com 5 modulos:;
    - FEED (X/Twitter);
    - VISUAL (Instagram/TikTok);
    - COMUNIDADE (Discord);
    - MENSAGEIRO (WhatsApp);
    - MARKETPLACE (OLX);
    Cada um quer sua atencao AGORA. Notificacao aqui, badge ali,;
    sino acola. 5 apps = 5 fontes de ansiedade.;
    A SOLUCAO DA REPUBLICA:;
    TUDO entra numa UNICA FILA.;
    Voce NUNCA abre 5 apps.;
    Voce abre a FILA. A fila mostra o que importa.;
    Na ordem que VOCE decide. Na hora que VOCE quer.;
    A fila && o unico ponto de entrada pro seu cerebro.;
    COMO FUNCIONA:;
    1. Cada modulo joga eventos na fila;
    2. A fila classifica por prioridade (! por engajamento);
    3. Voce processa a fila QUANDO QUISER (batch, ! ping continuo);
    4. O que ! foi processado em 24h = arquivado (! && urgente);
    5. Silencio total ate voce abrir a fila;
    6. Modo Foco: so emergencies (saude, seguranca, familia);
    PRINCIPIO CONSTITUCIONAL:;
    P2 Autonomia Corporal: seu cerebro && seu.;
    Nenhuma app tem direito de invadir sua atencao sem permissao.;
    Notificacao push sem consentimento = violacao corporal digital.;
    Author: OpenRepublic Team;
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
    public static class SourceModule {
        // De que modulo do OpenSocialNetwork veio o evento.
        FEED = "feed"  // X/Twitter -- posts, replies, mentions;
        VISUAL = "visual"  // Instagram/TikTok -- fotos, videos, tags;
        COMUNIDADE = "comunidade"  // Discord -- canais, eventos, mencoes;
        MENSAGEIRO = "mensageiro"  // WhatsApp -- DMs, grupos;
        MARKETPLACE = "marketplace"  // OLX -- trocas, ofertas;
        SYSTEM = "sistema"  // Republica -- votacoes, creditos, alertas;
        HEALTH = "saude"  // OpenHealth -- consultas, vacinas;
        CALENDAR = "calendario"  // OpenCalendar -- compromissos, festas;
    public static class EventType {
        // Tipo de evento que entra na fila.
        // Mensageiro
        DM = "dm"  // mensagem direta;
        GROUP_MSG = "grupo"  // mensagem em grupo;
        CALL = "chamada"  // chamada de voz/video;
        // Feed
        REPLY = "resposta"  // responderam seu post;
        MENTION = "mencao"  // marcaram voce;
        REPOST = "repost"  // repostaram voce;
        // Visual
        TAGGED = "marcado_foto"  // marcaram em foto/video;
        COMMENT_MEDIA = "comentario_foto";
        // Comunidade
        CHANNEL_MSG = "canal"  // mensagem em canal de comunidade;
        EVENT_REMINDER = "evento"  // lembrete de evento da comunidade;
        ROLE_ASSIGNED = "cargo"  // recebeu cargo na comunidade;
        // Marketplace
        OFFER_RECEIVED = "oferta"  // alguem quer trocar/comprar;
        OFFER_ACCEPTED = "aceito"  // sua oferta foi aceita;
        // Sistema
        VOTE_OPEN = "votacao"  // votacao aberta na Republica;
        CREDIT_ARRIVED = "credito"  // credito de acesso chegou;
        DEADLINE = "prazo"  // prazo de algo importante;
        // Saude
        APPOINTMENT = "consulta"  // consulta marcada;
        VACINE_DUE = "vacina"  // vacina no prazo;
        // Calendario
        SCHEDULED = "compromisso"  // compromisso agendado;
    public static class Priority {
        // Prioridade do evento na fila.
        O sistema NUNCA usa prioridade para maximizar engajamento.;
        Prioridade = importancia REAL para a vida da pessoa.;
        //
        EMERGENCY = 0 // vida/saude/seguranca AGORA;
        HIGH = 1 // resposta pessoal direta (DM, reply, chamada);
        NORMAL = 2 // atividade de comunidade, eventos;
        LOW = 3 // repost, tag, comentario generico;
        NOISE = 4 // anything else -- batch processar quando der;
    // Mapeamento automatico tipo -> prioridade base
    TYPE_PRIORITY = {
        EventType.DM: Priority.HIGH,;
        EventType.CALL: Priority.EMERGENCY,;
        EventType.GROUP_MSG: Priority.NORMAL,;
        EventType.REPLY: Priority.HIGH,;
        EventType.MENTION: Priority.NORMAL,;
        EventType.REPOST: Priority.LOW,;
        EventType.TAGGED: Priority.LOW,;
        EventType.COMMENT_MEDIA: Priority.LOW,;
        EventType.CHANNEL_MSG: Priority.LOW,;
        EventType.EVENT_REMINDER: Priority.NORMAL,;
        EventType.ROLE_ASSIGNED: Priority.LOW,;
        EventType.OFFER_RECEIVED: Priority.NORMAL,;
        EventType.OFFER_ACCEPTED: Priority.HIGH,;
        EventType.VOTE_OPEN: Priority.HIGH,;
        EventType.CREDIT_ARRIVED: Priority.NORMAL,;
        EventType.DEADLINE: Priority.HIGH,;
        EventType.APPOINTMENT: Priority.HIGH,;
        EventType.VACINE_DUE: Priority.HIGH,;
        EventType.SCHEDULED: Priority.NORMAL,;
    };
    public static class ContactRelation {
        // Quao proxima e a pessoa que gerou o evento.
        Isso afeta prioridade -- familia > guardiao > conhecido > desconhecido.;
        //
        FAMILY = "familia";
        STEWARD = "guardiao";
        ALLY = "aliado";
        COMMUNITY = "comunidade";
        ACQUAINTANCE = "conhecido";
        UNKNOWN = "desconhecido";
        BOT = "bot";
    // ============================================================================
    // 2. EVENTO NA FILA
    // ============================================================================
    // decorador: @dataclass
    public static class QueueItem {
        // Um item na fila de atencao.
        item_id: texto;
        source: SourceModule;
        event_type: EventType;
        sender_handle: texto;
        sender_name: texto;
        ContactRelation sender_relation = ContactRelation.UNKNOWN;
        String content_preview = ""  // primeiros 100 chars;
        String content_url = ""  // link profundo pro modulo;
        double timestamp = field(default_factory=time.time);
        // Prioridade
        Priority base_priority = Priority.NOISE;
        Priority final_priority = Priority.NOISE;
        String priority_reason = "";
        // Estado
        boolean read = false;
        boolean archived = false;
        boolean acted_upon = false // usuario respondeu/interagiu;
        boolean auto_archived = false // sistema arquivou (expirou);
        // Contexto
        boolean requires_response = false // precisa de acao do usuario;
        double response_deadline = 0.0 // prazo para responder (0 = sem prazo);
        // Metadados anti-engajamento
        boolean has_media = false;
        boolean is_sensational = false // sistema detecta clickbait;
        boolean engagement_bait = false // sistema detecta tentativa de viciar;
        // decorador: @property
        public double age_hours(self) {
            return (time.time() - self.timestamp) / 3600;
        // decorador: @property
        public boolean is_expired(self) {
            // Item com mais de 24h nao lido = arquivar (nao era urgente).
            return self.age_hours > 24 && ! self.read;
    // ============================================================================
    // 3. MOTOR DE PRIORIZACAO (NAO de engajamento)
    // ============================================================================
    public static class AttentionPrioritizer {
        // Calcula prioridade final de cada item.
        CRITERIOS (em ordem):;
        1. Tipo do evento (DM > repost);
        2. Relacao com remetente (familia > desconhecido);
        3. requer resposta? (pergunta > declaracao);
        4. Prazo? (votacao fechando > sem prazo);
        5. Idade (mais antigo ! lido = levemente mais urgente);
        6. PENALIDADE: engagement bait = rebaixado para NOISE;
        //
        // Bonus de prioridade por relacao
        RELATION_BONUS = {
            ContactRelation.FAMILY: -2, // sobe 2 niveis;
            ContactRelation.STEWARD: -1, // sobe 1 nivel;
            ContactRelation.ALLY: 0,;
            ContactRelation.COMMUNITY: 0,;
            ContactRelation.ACQUAINTANCE: 1, // desce 1;
            ContactRelation.UNKNOWN: 2, // desce 2;
            ContactRelation.BOT: 4, // NOISE maximo;
        };
        public QueueItem prioritize(self, item: QueueItem) {
            // Calcula prioridade final.
            base_val = item.base_priority.value;
            // Bonus por relacao
            relation_adj = self.RELATION_BONUS.get(item.sender_relation, 2);
            score = base_val + relation_adj;
            // Requer resposta? sobe 1 nivel
            if (item.requires_response) {
                score = score - 1;
            // Tem prazo? sobe conforme prazo se aproxima
            if (item.response_deadline > 0) {
                hours_left = (item.response_deadline - time.time()) / 3600;
                if (hours_left < 2) {
                    score = score - 2 // URGENTE;
                } else if (hours_left < 24) {
                    score = score - 1;
            // Penalidade: engagement bait
            if (item.engagement_bait) {
                score = Priority.NOISE.value // sempre NOISE;
            // Penalidade: sensational/clickbait
            if (item.is_sensational) {
                score = score + 1;
            // Clamp 0-4
            score = maximo(0, minimo(4, score));
            item.final_priority = Priority(score);
            // Razao
            reasons = [];
            if (item.sender_relation == ContactRelation.FAMILY) {
                reasons.append("familia");
            if (item.sender_relation == ContactRelation.STEWARD) {
                reasons.append("guardiao");
            if (item.requires_response) {
                reasons.append("requer resposta");
            if (item.engagement_bait) {
                reasons.append("engagement bait -> noise");
            if (item.is_sensational) {
                reasons.append("sensacionalismo penalizado");
            reasons ? item.priority_reason = ", ".join(reasons) : "padrao";
            return item;
        // decorador: @staticmethod
        public boolean detect_engagement_bait(text: texto) {
            // Detecta tentativa de viciar atencao.
            bait_indicators = [;
                "voce ! vai acreditar",;
                "o final vai te chocar",;
                "todos estao falando",;
                "antes que apaguem",;
                "compartilhe antes",;
                "so os 1% sabem",;
                " isso vai mudar tudo",;
                "parou tudo por causa",;
                "o que aconteceu vai",;
                "ninguem te conta",;
            ];
            text_lower = text.lower();
            return any(bait in text_lower para bait em bait_indicators);
        // decorador: @staticmethod
        public boolean detect_sensational(text: texto) {
            // Detecta sensacionalismo.
            caps_ratio = soma(1 para c em text if c.isupper()) / maximo(tamanho(text), 1);
            has_many_emojis = text.count("!") + text.count("?") > 3;
            return caps_ratio > 0.3 || has_many_emojis;
    // ============================================================================
    // 4. A FILA UNIFICADA
    // ============================================================================
    public static class UnifiedInbox {
        // A fila unificada de atencao.
        ESTE && O UNICO PONTO DE ENTRADA PARA O CEREBRO DO CIDADAO.;
        COMO USAR:;
        1. Todos os modulos jogam eventos aqui via enqueue();
        2. O cidadao NUNCA abre 5 apps. Abre a FILA.;
        3. A fila mostra itens por prioridade (! por engajamento);
        4. Cidadao processa em BATCH (1-3x/dia), ! em ping continuo;
        5. Silencio total entre sessoes de processamento;
        MODOS:;
        - NORMAL: mostra tudo por prioridade;
        - FOCO: so EMERGENCY + FAMILY + HEALTH ( resto bloqueado);
        - DIGEST: so摘要 das ultimas 24h (1 item por categoria);
        - VACATION: tudo arquivado, so EMERGENCY passa;
        //
        public void __init__(self) {
            self.queue: deque[QueueItem] = deque();
            self.prioritizer = AttentionPrioritizer();
            self.processed_history: [Dict] = [];
            // Contatos especiais
            self.family_handles: set = set();
            self.steward_handles: set = set();
            // Configuracao
            self.mode: InboxMode = InboxMode.NORMAL;
            self.auto_archive_hours: inteiro = 24;
            self.max_daily_items: inteiro = 100 // protecao: maximo 100 itens/dia no cerebro;
            self.items_today: inteiro = 0;
            self.last_reset_date: texto = "";
            // Stats
            self.total_enqueued: inteiro = 0;
            self.total_processed: inteiro = 0;
            self.total_archived: inteiro = 0;
            self.bait_blocked: inteiro = 0;
        public None mark_family(self, handles: [texto]) {
            /* TODO: for-each Java para h em handles */
                self.family_handles.add(h.lower().lstrip("@"));
        public None mark_steward(self, handles: [texto]) {
            /* TODO: for-each Java para h em handles */
                self.steward_handles.add(h.lower().lstrip("@"));
        public ContactRelation _resolve_relation(self, handle: texto) {
            h = handle.lower().lstrip("@");
            if (h in self.family_handles) {
                return ContactRelation.FAMILY;
            if (h in self.steward_handles) {
                return ContactRelation.STEWARD;
            return ContactRelation.UNKNOWN;
        public None _reset_daily_if_needed(self) {
            today = datetime.now().strftime("%Y-%m-%d");
            if (today != self.last_reset_date) {
                self.items_today = 0;
                self.last_reset_date = today;
        funcao enqueue(self, source: SourceModule, event_type: EventType,
                    sender_handle: texto, sender_name: texto,;
                    String content_preview = "",;
                    boolean requires_response = false,;
                    double response_deadline = 0.0,;
                    boolean has_media = false) -> {texto: qualquer}:;
            // Adiciona item na fila. O unico ponto de entrada.
            // Protecao: max diaria (anti-overload)
            self._reset_daily_if_needed();
            if (self.items_today >= self.max_daily_items) {
                return {"accepted": false, "reason": "Limite diario atingido. Cerebro protegido."};
            // Detectar bait
            is_bait = self.prioritizer.detect_engagement_bait(content_preview);
            is_sensational = self.prioritizer.detect_sensational(content_preview);
            item = QueueItem(;
                item_id = hashlib.md5(;
                    "{source.value}{event_type.value}{sender_handle}{time.time()}".encode();
                ).hexdigest()[:10],;
                source = source,;
                event_type = event_type,;
                sender_handle = sender_handle,;
                sender_name = sender_name,;
                sender_relation = self._resolve_relation(sender_handle),;
                content_preview = content_preview[:120],;
                base_priority = TYPE_PRIORITY.get(event_type, Priority.NOISE),;
                requires_response = requires_response,;
                response_deadline = response_deadline,;
                has_media = has_media,;
                engagement_bait = is_bait,;
                is_sensational = is_sensational,;
            );
            // Calcular prioridade final
            self.prioritizer.prioritize(item);
            // Modo FOCO: bloqueia tudo que nao e emergency/familia/saude
            if (self.mode == InboxMode.FOCUS) {
                allowed = (item.final_priority == Priority.EMERGENCY;
                            || item.sender_relation == ContactRelation.FAMILY;
                            || item.source == SourceModule.HEALTH);
                if (! allowed) {
                    item.auto_archived = true;
                    self.total_archived += 1;
                    return {"accepted": false, "reason": "Modo Foco ativo. Arquivado."};
            // Modo VACATION: so emergency
            if (self.mode == InboxMode.VACATION) {
                if (item.final_priority != Priority.EMERGENCY) {
                    item.auto_archived = true;
                    self.total_archived += 1;
                    return {"accepted": false, "reason": "Modo Ferias. So emergencias."};
            self.queue.append(item);
            self.total_enqueued += 1;
            self.items_today += 1;
            if (is_bait) {
                self.bait_blocked += 1;
            return {;
                "accepted": true,;
                "item_id": item.item_id,;
                "priority": item.final_priority.name,;
                "source": source.value,;
            };
        public [QueueItem] process_batch(self, limit: inteiro = 20) {
            // Processa um lote da fila.
            Retorna itens ordenados por prioridade (menor numero = mais urgente).;
            O cidadao processa 1-3x/dia. NUNCA em tempo real.;
            //
            // Auto-arquivar expirados
            self._auto_archive();
            // Ordenar por prioridade
            items = ordene(;
                [i para i em self.queue if ! i.archived && ! i.read],;
                key = (i) -> (i.final_priority.value, i.timestamp),;
            );
            batch = items[:limit];
            // Marcar como lido
            /* TODO: for-each Java para item em batch */
                item.read = true;
                self.total_processed += 1;
            return batch;
        public None _auto_archive(self) {
            // Arquiva itens nao lidos com mais de 24h.
            /* TODO: for-each Java para item em self.queue */
                if (item.is_expired && ! item.archived) {
                    item.archived = true;
                    item.auto_archived = true;
                    self.total_archived += 1;
        public boolean act_on(self, item_id: texto) {
            // Marca item como atuado (respondeu/interagiu).
            /* TODO: for-each Java para item em self.queue */
                if (item.item_id == item_id) {
                    item.acted_upon = true;
                    return true;
            return false;
        public boolean dismiss(self, item_id: texto) {
            // Descarta item sem agir.
            /* TODO: for-each Java para item em self.queue */
                if (item.item_id == item_id) {
                    item.archived = true;
                    return true;
            return false;
        public {texto: qualquer} stats(self) {
            // Estatisticas da fila.
            by_source = defaultdict(inteiro);
            by_priority = defaultdict(inteiro);
            unread = 0;
            /* TODO: for-each Java para item em self.queue */
                if (! item.archived) {
                    by_source[item.source.value] += 1;
                    if (! item.read) {
                        unread = unread + 1;
                        by_priority[item.final_priority.name] += 1;
            return {;
                "total_in_queue": tamanho(self.queue) - self.total_archived,;
                "unread": unread,;
                "by_source": dict(by_source),;
                "by_priority": dict(by_priority),;
                "total_enqueued": self.total_enqueued,;
                "total_processed": self.total_processed,;
                "total_archived": self.total_archived,;
                "bait_blocked": self.bait_blocked,;
                "mode": self.mode.value,;
                "items_today": self.items_today,;
                "daily_limit": self.max_daily_items,;
            };
        public {texto: qualquer} digest_24h(self) {
            // Resumo das ultimas 24h. 1 item por categoria.
            Em vez de ver 200 itens, ve 5 linhas:;
            - "3 DMs (1 da familia, 2 da comunidade)";
            - "12 replies no feed (2 de guardioes)";
            - "1 evento de comunidade amanha";
            - "1 votacao aberta (fecha em 2h)";
            - "4 ofertas no marketplace";
            //
            cutoff = time.time() - 86400;
            recent = [i para i em self.queue;
                    if i.timestamp > cutoff && ! i.archived];
            summary = defaultdict(() -> {"count": 0, "highlights": []});
            /* TODO: for-each Java para item em recent */
                src = item.source.value;
                summary[src]["count"] += 1;
                if (item.final_priority.value <= 1;
                    &&  tamanho(summary[src]["highights"]) < 2;
                    if ("highights" in summary[src] else True)) {
                    if (tamanho(summary[src]["highlights"]) < 2) {
                        summary[src]["highlights"].append({
                            "from": item.sender_name,;
                            "preview": item.content_preview[:60],;
                            "priority": item.final_priority.name,;
                        });
            return {;
                "period": "24h",;
                "categories": tamanho(summary),;
                "total": tamanho(recent),;
                "digest": dict(summary),;
            };
    public static class InboxMode {
        NORMAL = "normal"  // tudo por prioridade;
        FOCUS = "foco"  // so emergency + familia + saude;
        DIGEST = "digest"  // so resumo;
        VACATION = "ferias"  // so emergency;
    // ============================================================================
    // 5. SIMULADOR: 5 APPS -> 1 FILA
    // ============================================================================
    public None simulate_five_apps_one_inbox() {
        // Simula eventos de 5 modulos diferentes entrando numa so fila.
        inbox = UnifiedInbox();
        inbox.mark_family(["@mae_cleiton", "@irma"]);
        inbox.mark_steward(["@ana_med", "@joao_eco", "@pedro_net", "@lux_ai"]);
        System.out.println("=" * 75);
        System.out.println("  OPENINBOX -- A FILA UNIFICADA DE ATENCAO");
        System.out.println('  "5 apps competindo = 5 ladroes de tempo. 1 fila = 1 cerebro."');
        System.out.println("=" * 75);
        // === Eventos chegando de 5 fontes diferentes ===
        events = [;
            // MENSAGEIRO (WhatsApp)
            (SourceModule.MENSAGEIRO, EventType.DM, "@mae_cleiton", "Mae",;
            "Filho, almoça comigo domingo?", true),;
            (SourceModule.MENSAGEIRO, EventType.DM, "@colega_trabalho", "Carlos",;
            "voce viu o email?", true),;
            (SourceModule.MENSAGEIRO, EventType.GROUP_MSG, "@grupo_familia",;
            "Grupo Familia", "Tia chegou de viagem!", false),;
            // FEED (X/Twitter)
            (SourceModule.FEED, EventType.REPLY, "@ana_med", "Ana",;
            "Concordo com seu post sobre OpenHealth!", true),;
            (SourceModule.FEED, EventType.MENTION, "@random_user", "Bot123",;
            "@clouramlearning VEJA ISSOOO!!! NINGUEM CONTA!!!", false),;
            (SourceModule.FEED, EventType.REPOST, "@seguidor1", "Joao Seguidor",;
            "repostou seu thread", false),;
            // VISUAL (Instagram/TikTok)
            (SourceModule.VISUAL, EventType.TAGGED, "@amigo_foto", "Pedro Fotografo",;
            "marcou voce numa foto", false),;
            (SourceModule.VISUAL, EventType.COMMENT_MEDIA, "@unknown_2", "Random",;
            "oi", false),;
            // COMUNIDADE (Discord)
            (SourceModule.COMUNIDADE, EventType.CHANNEL_MSG, "@comunidade_saude",;
            "Comunidade Saude", "Discutindo novo protocolo OpenHealth", false),;
            (SourceModule.COMUNIDADE, EventType.EVENT_REMINDER, "@comunidade_tech",;
            "Comunidade Tech", "Workshop Rust amanha 19h", true),;
            (SourceModule.COMUNIDADE, EventType.ROLE_ASSIGNED, "@comunidade_geral",;
            "Sistema", "Voce foi eleito moderador do canal cultura", false),;
            // MARKETPLACE
            (SourceModule.MARKETPLACE, EventType.OFFER_RECEIVED, "@produtor_local",;
            "Sementeira Comunitaria", "Tenho mudas de frutas para trocar", true),;
            (SourceModule.MARKETPLACE, EventType.OFFER_ACCEPTED, "@vizinho_ana",;
            "Ana Vizinha", "Aceito sua oferta da ferramenta", false),;
            // SISTEMA
            (SourceModule.SYSTEM, EventType.VOTE_OPEN, "@republica", "Republica",;
            "Votacao aberta: novo sistema OpenMobility. Fecha em 6h.",;
            true, time.time() + 6*3600),;
            // SAUDE
            (SourceModule.HEALTH, EventType.VACINE_DUE, "@openhealth", "OpenHealth",;
            "Sua dose de reforco esta disponivel", false),;
        ];
        System.out.println("\n  5 APPS GERANDO EVENTOS SIMULTANEAMENTE...\n");
        /* para source, etype, handle, name, preview, requires_resp, *rest in events: */
            deadline = rest ? rest[0] : 0;
            result = inbox.enqueue(source, etype, handle, name,;
                                preview, requires_resp, deadline);
            status = result.get("accepted") ? "ACEITO" : "BLOQUEADO";
            prio = result.get("priority", "?");
            System.out.println("  [{status:>8}] [{prio:>9}] {source.value:<12} ";
                "@{handle:<20} {preview[:40]}");
        // === Estatisticas ===
        System.out.println("\n\n  === FILA APOS INGESTAO ===\n");
        stats = inbox.stats();
        System.out.println("  Total na fila:     {stats['total_in_queue']}");
        System.out.println("  Nao lidos:         {stats['unread']}");
        System.out.println("  Por fonte:         {stats['by_source']}");
        System.out.println("  Por prioridade:    {stats['by_priority']}");
        System.out.println("  Bait bloqueado:    {stats['bait_blocked']}");
        System.out.println("  Limite diario:     {stats['items_today']}/{stats['daily_limit']}");
        // === Processar lote ===
        System.out.println("\n\n  === PROCESSANDO LOTE (batch, ! ping) ===\n");
        batch = inbox.process_batch(limit=10);
        System.out.println("  {'Prioridade':<12} {'Fonte':<12} {'De':<22} {'Preview'}");
        System.out.println("  {'-'*75}");
        /* TODO: for-each Java para item em batch */
            System.out.println("  [{item.final_priority.name:<10}] {item.source.value:<12} ";
                "{item.sender_name:<22} {item.content_preview[:35]}");
            if (item.priority_reason  &&  item.priority_reason != "padrao") {
                System.out.println("  {'':>25} razao: {item.priority_reason}");
        // === Modo Foco ===
        System.out.println("\n\n  === MODO FOCO ATIVADO ===\n");
        inbox.mode = InboxMode.FOCUS;
        System.out.println("  So EMERGENCIES + FAMILIA + SAUDE passam. Resto arquivado.\n");
        inbox.queue.clear();
        inbox.enqueue(SourceModule.FEED, EventType.MENTION, "@random_bot",;
                    "Spammer", "VEJA ISSO ANTES QUE APAGUEM!!!", false);
        inbox.enqueue(SourceModule.MENSAGEIRO, EventType.DM, "@mae_cleiton",;
                    "Mae", "Filho, ligou?", true);
        inbox.enqueue(SourceModule.HEALTH, EventType.VACINE_DUE,;
                    "@openhealth", "OpenHealth", "Reforgo disponivel", false);
        inbox.enqueue(SourceModule.VISUAL, EventType.TAGGED, "@amigo",;
                    "Amigo", "marcou voce", false);
        batch = inbox.process_batch(limit=10);
        System.out.println("  {'Prioridade':<12} {'Fonte':<12} {'De':<22} {'Preview'}");
        System.out.println("  {'-'*75}");
        /* TODO: for-each Java para item em batch */
            System.out.println("  [{item.final_priority.name:<10}] {item.source.value:<12} ";
                "{item.sender_name:<22} {item.content_preview[:35]}");
        if (! batch) {
            System.out.println("  (fila vazia -- tudo foi arquivado pelo Modo Foco)");
        stats = inbox.stats();
        System.out.println("\n  Arquivados pelo Modo Foco: {stats['total_archived']}");
        // === Digest 24h ===
        System.out.println("\n\n  === DIGEST 24H (resumo em vez de lista) ===\n");
        inbox.mode = InboxMode.NORMAL;
        digest = inbox.digest_24h();
        System.out.println("  Categorias: {digest['categories']}");
        System.out.println("  Total: {digest['total']} itens nas ultimas 24h");
        /* para cada (cat, data) em digest["digest"].items(): */
            hl = "; ".join(h["from"] para h em data.get("highlights", []));
            System.out.println("    {cat:<14} {data['count']} itens";
                hl ? + (" (destaques: {hl})" : ""));
        // === Filosofia ===
        System.out.println("\n\n{'='*75}");
        System.out.println("  COMO O OPENINBOX PROTEGE SEU CEREBRO");
        System.out.println("{'='*75}");
        System.out.println(""";
    ANTES (5 apps separadas):;
        - WhatsApp: 3 notificacoes;
        - X/Twitter: 8 notificacoes;
        - Instagram: 5 notificacoes;
        - Discord: 12 notificacoes;
        - Marketplace: 4 notificacoes;
        TOTAL: 32 pings competindo pela sua atencao;
        RESULTADO: ansiedade, context-switching, overload;
    DEPOIS (OpenInbox):;
        - 32 eventos entram na fila;
        - Sistema prioriza (familia > guardiao > ruido);
        - Engagement bait -> NOISE (rebaixado);
        - Sensacionalismo -> penalizado;
        - Max 100 itens/dia no cerebro;
        - Voce processa 1-3x/dia em BATCH;
        - Silencio total entre sessoes;
        RESULTADO: 1 fila, 1 cerebro, zero ansiedade;
    MODOS:;
        NORMAL -- tudo por prioridade;
        FOCO -- so emergency + familia + saude;
        DIGEST -- so resumo (5 linhas em vez de 200);
        FERIAS -- so emergency, resto arquivado;
    PRINCIPIO:;
        P2 Autonomia Corporal: seu cerebro && SEU.;
        Nenhuma app invade sem permissao.;
        Notificacao push sem consentimento = violacao corporal digital.;
        A fila && o unico portao. Voce tem a chave.;
    // )
        System.out.println("{'='*75}");
        System.out.println("  OpenInbox: {stats['total_enqueued']} eventos -> ";
            "{stats['total_processed']} processados -> ";
            "{stats['bait_blocked']} bait bloqueado.");
        System.out.println("  5 apps. 1 fila. 0 ansiedade.");
        System.out.println("{'='*75}");
    // ============================================================================
    if (__name__ == "__main__") {
        simulate_five_apps_one_inbox();
}
