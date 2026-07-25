// OpenContentPolicy + OpenTV -- TV Aberta e Streaming da Republica -- gerado de Portugol++
package opencontentpolicy_opentv_tv_aberta_e_streaming_da_republica

import "fmt"

// !/usr/bin/env python3
//
OpenContentPolicy + OpenTV -- TV Aberta && Streaming da Republica
==================================================================
"Toda comunicacao roda na OpenNetwork sobre o OpenProtocol.
TV aberta ! existe mais -- existe STREAMING comunitario.
24h por dia, feito por rotatividade de pessoas."
O QUE ISTO FAZ:
1. POLITICA ANTI-CONTEUDO NOCIVO: define o que ! aceita
2. MODERACAO DEMOCRATICA: juri sorteado, ! algoritmo
3. OPENtv: streaming 24h sobre OpenNetwork/OpenProtocol
4. PROGRAMACAO ROTATIVA: pessoas preenchem o tempo, ! corporacao
5. CANAIS TEMATICOS: educacao, saude, cultura, jogos, noticias (verificadas)
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, deque de collections
// importa datetime, timedelta de datetime
// ============================================================================
// 1. CATEGORIAS DE CONTEUDO
// ============================================================================
type ContentCategory int
const (
    EDUCATIONAL = "educativo"
    NEWS_VERIFIED = "noticia_verificada"
    CULTURAL = "cultural"
    ENTERTAINMENT = "entretenimento"
    HEALTH = "saude"
    SCIENCE = "ciencia"
    GAMES = "jogos"
    MUSIC = "musica"
    ART = "arte"
    COMMUNITY = "comunitario"
    SPORTS = "esportes"
    KIDS = "infantil"
    DEMOCRACY = "democracia"
    COOKING = "culinaria"
    DIY = "faça_voce_mesmo"
type HarmfulType int
const (
    // Tipos de conteudo NOCIVO que a Republica NAO aceita.
    MANIPULATION = "manipulacao_degenerativa"  // ensinar manipular pessoas
    HATE_SPEECH = "discurso_odio"  // racismo, machismo, LGBTfobia
    MISINFORMATION = "desinformacao"  // fake news com dano real
    EXTREMISM = "extremismo"  // recrutamento terrorista/faccao
    GROOMING = "grooming"  // aliciamento de criancas
    SELF_HARM = "auto_dano"  // incentivar suicidio/anorexia
    ANTI_SCIENCE = "anti_ciencia"  // negar ciencia com dano (ex: anti-vacina letal)
    ANTI_REPUBLIC = "anti_republica"  // discurso para destruir a Republica
    SCAM_FRAUD = "golpe_fraude"  // enganar para lucro
    DEHUMANIZATION = "desumanizacao"  // negar humanidade de grupo
    DEGENERATIVE = "degenerativo"  // canais dark de degradacao continuada
    EXPLOITATION = "exploracao"  // explorar vulneraveis
type ModerationAction int
const (
    // Acao de moderacao.
    ALLOW = "permitir"
    FLAG_REVIEW = "marcar_revisao"  // juri precisa ver
    WARNING = "aviso"  // permitido com aviso
    RESTRICTED = "restrito"  // so adultos, so com contexto
    REMOVED = "removido"  // tirar do ar
    BANNED_AUTHOR = "autor_banido"  // autor perdeu direito de postar
    CRIMINAL_REPORT = "denuncia_criminal"  // crime real -> autoridade
// ============================================================================
// 2. ANALISE DE CONTEUDO
// ============================================================================
// decorador: @dataclass
type ContentAnalysis struct {
    // Analise de um conteudo postado.
    content_id: texto
    author: texto
    category: ContentCategory
    title := "" // string
    description := "" // string
    has_media := false // bool
    media_type := ""  // video, imagem, audio // string
    // Analise automatica
    detected_issues := field(default_factory=list) // [HarmfulType]
    auto_confidence := 0.0 // 0-1 (confianca na deteccao) // float64
    auto_flags := field(default_factory=list) // [texto]
    // Moderacao
    action := ModerationAction.ALLOW // ModerationAction
    jury_verdict := nil // texto?
    jury_votes_for := 0 // votos para remover // int64
    jury_votes_against := 0 // votos para manter // int64
    moderated_by := "" // string
    moderation_date := "" // string
    // Apelo
    appealed := false // bool
    appeal_result := "" // string
type ContentModerator struct {
    // Motor de moderacao de conteudo.
    FLUXO DE MODERACAO (3 camadas):
    CAMADA 1: AUTOMATICA (filtro rapido)
    - Detecta padrões de manipulacao, odio, dano
    - Se claro: bloqueia automaticamente
    - Se duvidoso: manda pra juri
    CAMADA 2: JURI DEMOCRATICO (9 cidadaos sorteados)
    - 9 pessoas aleatorias avaliam
    - Maioria 2/3 decide (6 de 9)
    - Nao && algoritmo. Sao pessoas.
    - Duracao maxima: 24h
    CAMADA 3: APELACAO
    - Autor pode apelar
    - Outro juri (diferente) revisa
    - Decisao final
    O QUE ! EXISTE:
    - Algoritmo opaco decidindo sozinho (P4)
    - Corporacao decidindo o que && "verdade"
    - Banimento sem processo
    - Shadow banning (banimento secreto)
    O QUE EXISTE:
    - Deteccao automatica TRANSPARENTE (mostra o que detectou)
    - Juri de cidadaos (sorteio democratico)
    - Apelo garantido
    - Tudo registrado && publico
    //
    func __init__(self) {
        self.analyses: {texto: ContentAnalysis} = {}
        self.jury_pool: [texto] = [] // cidadaos disponiveis para juri
        self.banned_authors: set = set()
        self.stats_auto_blocked: inteiro = 0
        self.stats_jury_reviewed: inteiro = 0
        self.stats_removed: inteiro = 0
        self.stats_allowed: inteiro = 0
    // PADROES DE DETECCAO AUTOMATICA
    HARMFUL_PATTERNS := { // Dict[HarmfulType, [texto]]
        HarmfulType.MANIPULATION: [
            "como manipular", "tecnicas de manipulacao", "gaslighting tutorial",
            "como controlar pessoas", "pnl dark", "engenharia social maliciosa",
            "como destruir", "como acabar com", "tecnica de degradação",
        ],
        HarmfulType.HATE_SPEECH: [
            "raça inferior", "precisamos nos livrar", "são todos iguais",
            "não pertencem aqui", "sangue impuro", "pragas",
            "macaco", "sub-humanos", "vermes",
        ],
        HarmfulType.MISINFORMATION: [
            "vacina mata mais que", "terra é plana && aqui está a prova",
            "eleição foi fraudada sem prova", "remédio milagroso que",
            "doutor diz segredo que industria esconde",
        ],
        HarmfulType.EXTREMISM: [
            "junte-se à nossa causa armada", "precisamos agir agora com violência",
            "treinamento paramilitar", "como fazer bomba",
            "lista de alvos",
        ],
        HarmfulType.GROOMING: [
            "encontro secreto com menor", "mande foto sua",
            "seus pais não precisam saber",
        ],
        HarmfulType.SELF_HARM: [
            "como se machucar", "desafio da morte", "não coma por",
            "ninguém vai sentir sua falta",
        ],
        HarmfulType.DEGENERATIVE: [
            "canal dark", "comunidade secreta de degradação",
            "desafio degradante", "torneio de humilhação",
        ],
        HarmfulType.SCAM_FRAUD: [
            "investimento garantido 100%", "pix && ganhe o dobro",
            "dados do cartão para liberar", "você ganhou sorteio que não participou",
        ],
    }
    funcao analyze(self, author: texto, category: ContentCategory,
                title: texto, description: texto = "",
                has_media := false, // bool
                media_type := "") -> {texto: qualquer}: // string
        // Analisa conteudo automaticamente.
        full_text = (title + " " + description).lower()
        detected = []
        flags = []
        para cada (harm_type, patterns) em self.HARMFUL_PATTERNS.items(): {
            for _, pattern := range patterns {
                if pattern in full_text {
                    detected.append(harm_type)
                    flags.append("Padrao detectado: '{pattern}' -> {harm_type.value}")
                    break
        content_id = hashlib.md5(
            "{author}{title}{datetime.now()}".encode()
        ).hexdigest()[:8]
        analysis = ContentAnalysis(
            content_id = content_id,
            author = author,
            category = category,
            title = title,
            description = description,
            has_media = has_media,
            media_type = media_type,
            detected_issues = detected,
            auto_flags = flags,
        )
        // Decidir acao automatica
        if len(detected) >= 2 {
            analysis.action = ModerationAction.REMOVED
            analysis.auto_confidence = 0.9
            self.stats_auto_blocked += 1
        } else if len(detected) == 1 {
            severity = self._severity(detected[0])
            if severity >= 4 {
                analysis.action = ModerationAction.REMOVED
                analysis.auto_confidence = 0.85
                self.stats_auto_blocked += 1
            } else {
                analysis.action = ModerationAction.FLAG_REVIEW
                analysis.auto_confidence = 0.6
        } else {
            analysis.action = ModerationAction.ALLOW
            analysis.auto_confidence = 0.95
            self.stats_allowed += 1
        self.analyses[content_id] = analysis
        return {
            "content_id": content_id,
            "author": author,
            "title": title[:50],
            "action": analysis.action.value,
            "detected": [d.value para d em detected],
            "flags": flags,
            "confidence": analysis.auto_confidence,
            "message": self._action_message(analysis),
        }
    func _severity(self, harm_type: HarmfulType) int64 {
        severity_map = {
            HarmfulType.GROOMING: 5,
            HarmfulType.SELF_HARM: 5,
            HarmfulType.EXTREMISM: 5,
            HarmfulType.HATE_SPEECH: 4,
            HarmfulType.MANIPULATION: 3,
            HarmfulType.DEGENERATIVE: 3,
            HarmfulType.MISINFORMATION: 3,
            HarmfulType.ANTI_SCIENCE: 2,
            HarmfulType.SCAM_FRAUD: 3,
            HarmfulType.DEHUMANIZATION: 4,
            HarmfulType.EXPLOITATION: 4,
            HarmfulType.ANTI_REPUBLIC: 3,
        }
        return severity_map.get(harm_type, 2)
    func _action_message(self, a: ContentAnalysis) string {
        if a.action == ModerationAction.ALLOW {
            return "Conteudo permitido."
        if a.action == ModerationAction.REMOVED {
            return (
                "CONTEUDO REMOVIDO. Detectado: "
                "{', '.join(d.value for d in a.detected_issues)}. "
                "Autor pode apelar. Juri revisara."
            )
        if a.action == ModerationAction.FLAG_REVIEW {
            return (
                "Conteudo marcado para revisao por juri. "
                "Suspeita: {', '.join(d.value for d in a.detected_issues)}."
            )
        return ""
    funcao jury_review(self, content_id: texto,
                    votes_for_removal: inteiro,
                    votes_against: inteiro) -> {texto: qualquer}:
        // Juri democratico decide.
        analysis = self.analyses.get(content_id)
        if ! analysis {
            return {"error": "Conteudo ! encontrado"}
        analysis.jury_votes_for = votes_for_removal
        analysis.jury_votes_against = votes_against
        total = votes_for_removal + votes_against
        if total == 0 {
            return {"error": "Sem votos"}
        // 2/3 para remover (6 de 9 tipicamente)
        if votes_for_removal >= total * 0.66 {
            analysis.action = ModerationAction.REMOVED
            analysis.jury_verdict = "REMOVIDO por juri"
            self.stats_removed += 1
            self.stats_jury_reviewed += 1
            // Se autor recidiva, banir
            author_strikes = soma(
                1 para a em self.analyses.values()
                if a.author == analysis.author
                && a.action == ModerationAction.REMOVED
            )
            if author_strikes >= 3 {
                analysis.action = ModerationAction.BANNED_AUTHOR
                self.banned_authors.add(analysis.author)
        } else if votes_against >= total * 0.66 {
            analysis.action = ModerationAction.ALLOW
            analysis.jury_verdict = "PERMITIDO por juri"
            self.stats_allowed += 1
            self.stats_jury_reviewed += 1
        } else {
            analysis.action = ModerationAction.FLAG_REVIEW
            analysis.jury_verdict = "INCONCLUSIVO -- novo juri"
        return {
            "content_id": content_id,
            "verdict": analysis.jury_verdict,
            "action": analysis.action.value,
            "votes": "{votes_for_removal} remover / {votes_against} manter",
        }
    func appeal(self, content_id: texto) {texto: qualquer} {
        // Autor apela de remocao.
        analysis = self.analyses.get(content_id)
        if ! analysis {
            return {"error": "! encontrado"}
        analysis.appealed = true
        return {
            "content_id": content_id,
            "appeal_filed": true,
            "message": (
                "Apelo registrado. Novo juri (diferente) revisara em 48h. "
                "Se revertido, conteudo volta. "
                "Republica garante direito de defesa (P4)."
            ),
        }
    func stats(self) {texto: qualquer} {
        return {
            "total_analyzed": len(self.analyses),
            "auto_blocked": self.stats_auto_blocked,
            "jury_reviewed": self.stats_jury_reviewed,
            "removed": self.stats_removed,
            "allowed": self.stats_allowed,
            "banned_authors": len(self.banned_authors),
        }
// ============================================================================
// 3. OPENtv -- STREAMING COMUNITARIO 24h
// ============================================================================
type ProgramType int
const (
    LIVE = "ao_vivo"  // streaming ao vivo
    RECORDED = "gravado"  // pre-gravado
    AUTOMATED = "automatizado"  // gerado por IA/republica
    INTERACTIVE = "interativo"  // audiencia participa
    EDUCATIONAL_LOOP = "educativo_loop"  // modulo educativo em loop
type TVChannel int
const (
    // Canais da OpenTV -- todos sobre OpenNetwork/OpenProtocol.
    REPUBLIC_MAIN = "Republica TV"  // canal principal
    EDUCATION = "Educanal"  // educacao 24h
    HEALTH = "Saude TV"  // saude + OpenHealth
    CULTURE = "Cultura TV"  // cultura/tradicoes
    GAMES = "Games TV"  // torneios/gameplay
    SCIENCE = "Ciencia TV"  // ciencia/tecnologia
    DEMOCRACY = "Democracia TV"  // votacoes/debates ao vivo
    KIDS = "Republica Kids"  // infantil educativo
    NEWS = "Verificada TV"  // noticias verificadas
    COMMUNITY = "Comunidade TV"             #_canais locais
    MUSIC = "Musica TV"  // musica aberta
    LABOR = "Trabalho TV"  // OpenLaborRelay visual
// decorador: @dataclass
type TVProgram struct {
    // Um programa da grade de TV da Republica.
    program_id: texto
    title: texto
    channel: TVChannel
    program_type: ProgramType
    duration_min: inteiro
    presenter := ""  // quem apresenta (rotativo!) // string
    description := "" // string
    interactive := false // audiencia participa? // bool
    age_rating := "Livre" // string
    educational_value := "" // string
    // Rotatividade
    is_rotative := true // pessoas revezam na apresentacao // bool
    presenters_history := field(default_factory=list) // [texto]
// decorador: @dataclass
type TVScheduleSlot struct {
    // Um slot na grade de programacao 24h.
    start_hour: inteiro // 0-23
    start_minute: inteiro // 0 || 30
    program := nil // TVProgram?
    channel := TVChannel.REPUBLIC_MAIN // TVChannel
type OpenTV struct {
    // TV Aberta da Republica -- 100% streaming sobre OpenNetwork.
    COMO FUNCIONA:
    1. ! existe TV aberta tradicional (antena/sinal analogico)
    2. TUDO && streaming via OpenNetwork sobre OpenProtocol
    3. Qualquer dispositivo (TV Stick, smartphone, PC, terminal) acessa
    4. Programacao 24h preenchida por ROTATIVIDADE de pessoas
    5. Tempo ocioso = programacao automatizada (modulos educativos, IA)
    ROTATIVIDADE DE PESSOAS:
    - Maria apresenta das 14h-16h (usa tempo de descanso)
    - Joao apresenta das 16h-18h (apos trabalho na horta)
    - Sistema de IA apresenta das 3h-6h (madrugada, ninguem quer)
    - Criancas apresentam programa infantil aos sabados
    ! && CORPORACAO:
    - Nao ha "apresentador fixo" ganhando milhoes
    - Nao ha "grade comercial" com anuncios
    - Nao ha "audiencia" no sentido capitalista (sem IBOPE)
    - && COMUNIDADE se comunicando com comunidade
    //
    func __init__(self) {
        self.programs: {texto: TVProgram} = {}
        self.schedule: Dict[inteiro, [TVScheduleSlot]] = defaultdict(list)
        self.active_streamers: {texto: texto} = {} // channel -> presenter atual
        self.total_viewers: inteiro = 0
        self.uptime_hours: flutuante = 0.0
        // Politica
        self.commercial_ads: logico = false // NUNCA
        self.corporate_sponsorship: logico = false // NUNCA
        self.algorithms_engagement: logico = false // NUNCA
        self.hate_content: logico = false // NUNCA
        self.protocol: texto = "OpenProtocol"
        self.network: texto = "OpenNetwork"
        self._init_default_schedule()
    func _init_default_schedule(self) {
        // Cria grade padrao 24h para canal principal.
        default_day = [
            (0, 0, "Loop Educativo Noturno", TVChannel.EDUCATION, ProgramType.EDUCATIONAL_LOOP, 120),
            (2, 0, "Modulo Auto-Aprendizado", TVChannel.EDUCATION, ProgramType.EDUCATIONAL_LOOP, 120),
            (4, 0, "Programacao Automatizada IA", TVChannel.REPUBLIC_MAIN, ProgramType.AUTOMATED, 120),
            (6, 0, "Bom Dia Republica (noticias verificadas)", TVChannel.NEWS, ProgramType.LIVE, 120),
            (8, 0, "Aula Aberta (OpenEducation)", TVChannel.EDUCATION, ProgramType.LIVE, 120),
            (10, 0, "Saude para Todos (OpenHealth)", TVChannel.HEALTH, ProgramType.LIVE, 120),
            (12, 0, "Almoco Cultural (musica/arte)", TVChannel.CULTURE, ProgramType.LIVE, 60),
            (13, 0, "Ciencia Aberta", TVChannel.SCIENCE, ProgramType.LIVE, 120),
            (15, 0, "Trabalho Comunitario (ao vivo de FabLab)", TVChannel.LABOR, ProgramType.LIVE, 120),
            (17, 0, "Republica Kids", TVChannel.KIDS, ProgramType.LIVE, 90),
            (18, 30, "Jornal Verificado da Republica", TVChannel.NEWS, ProgramType.LIVE, 60),
            (19, 30, "Debate Democratico (votacoes ao vivo)", TVChannel.DEMOCRACY, ProgramType.INTERACTIVE, 90),
            (21, 0, "Games TV (torneios/gameplay)", TVChannel.GAMES, ProgramType.LIVE, 120),
            (23, 0, "Documentario da Republica (OpenHistory)", TVChannel.CULTURE, ProgramType.RECORDED, 60),
        ]
        para hour, minute, title, channel, ptype, duration in default_day: {
            prog = TVProgram(
                program_id = hashlib.md5("{title}{hour}".encode()).hexdigest()[:8],
                title = title,
                channel = channel,
                program_type = ptype,
                duration_min = duration,
                is_rotative = true,
                description = "Programa {title} -- apresentacao rotativa.",
            )
            self.programs[prog.program_id] = prog
            slot = TVScheduleSlot(hour, minute, prog, channel)
            self.schedule[hour].append(slot)
    funcao volunteer_to_present(self, citizen_id: texto, citizen_name: texto,
                            channel: TVChannel, time_slot: texto) -> {texto: qualquer}:
        // Cidadao se voluntaria para apresentar programa.
        Apresentar TV conta como TRABALHO (P3).
        && contribuicao real para a comunidade.
        //
        return {
            "volunteered": true,
            "citizen": citizen_name,
            "channel": channel.value,
            "slot": time_slot,
            "counts_as_work": true,
            "work_hours": 2.0,   // tipico 2h de programa
            "credit": 4.0,
            "message": (
                "{citizen_name} vai apresentar no canal {channel.value} "
                "as {time_slot}. Comunidade agradece! "
                "Conta como trabalho (2h base 1.0)."
            ),
        }
    func now_playing(self, hour: inteiro = None, minute: inteiro = None) {texto: qualquer} {
        // O que esta passando agora em cada canal.
        now_h = hour is ! nil ? hour : datetime.now().hour
        // Encontrar programa atual no canal principal
        main_slot = nil
        for _, h := range ordene(self.schedule.keys(), reverse=True) {
            if h <= now_h {
                main_slot = self.schedule[h][0]
                break
        if ! main_slot || ! main_slot.program {
            return {"channel": "automatizado", "message": "Programacao automatizada"}
        return {
            "channel": main_slot.channel.value,
            "program": main_slot.program.title,
            "type": main_slot.program.program_type.value,
            "rotative": main_slot.program.is_rotative,
            "presenter": "rotativo (voluntario da comunidade)",
            "network": self.network,
            "protocol": self.protocol,
            "viewers": random.randint(100, 10000),
        }
    funcao full_schedule(self) retorna List[{texto: qualquer}]:
        // Grade completa 24h.
        schedule = []
        for _, hour := range ordene(self.schedule.keys()) {
            for _, slot := range self.schedule[hour] {
                if slot.program {
                    schedule.append({
                        "time": "{slot.start_hour:02d}:{slot.start_minute:02d}",
                        "channel": slot.channel.value,
                        "program": slot.program.title,
                        "type": slot.program.program_type.value,
                        "duration": "{slot.program.duration_min}min",
                        "rotative": slot.program.is_rotative,
                    })
        return schedule
    funcao channels_available(self) retorna List[{texto: texto}]:
        // Lista de canais disponiveis.
        return [
            {"channel": c.value, "description": self._channel_desc(c)}
            para c em TVChannel {
        ]
    func _channel_desc(self, c: TVChannel) string {
        descs = {
            TVChannel.REPUBLIC_MAIN: "Canal principal da Republica",
            TVChannel.EDUCATION: "Educacao 24h (OpenEducation + OpenBlackBoard)",
            TVChannel.HEALTH: "Saude + telemedicina (OpenHealth)",
            TVChannel.CULTURE: "Cultura && tradicoes (OpenTradition)",
            TVChannel.GAMES: "Torneios && gameplay (OpenGames)",
            TVChannel.SCIENCE: "Ciencia && tecnologia (OpenScience)",
            TVChannel.DEMOCRACY: "Votacoes && debates ao vivo (P4)",
            TVChannel.KIDS: "Infantil educativo (sem ads)",
            TVChannel.NEWS: "Noticias VERIFICADAS (OpenHistory fact-check)",
            TVChannel.COMMUNITY: "Canais locais comunitarios",
            TVChannel.MUSIC: "Musica aberta sem direitos autorais",
            TVChannel.LABOR: "Trabalho comunitario ao vivo (OpenLaborRelay)",
        }
        return descs.get(c, "")
    func report(self) {texto: qualquer} {
        return {
            "total_programs": len(self.programs),
            "channels": len(list(TVChannel)),
            "schedule_slots": soma(len(slots) para slots em self.schedule.values()),
            "infrastructure": "{self.network} / {self.protocol}",
            "commercials": "PROIBIDO",
            "sponsorship": "PROIBIDO",
            "algorithms": "PROIBIDO",
            "uptime_24h": true,
        }
// ============================================================================
// 4. MAIN
// ============================================================================
if __name__ == "__main__" {
    moderator = ContentModerator()
    tv = OpenTV()
    fmt.Println("=" * 80)
    fmt.Println("  OPENCONTENTPOLICY + OPENTV")
    fmt.Println("  Anti-Conteudo Nocivo + TV Streaming da Republica")
    fmt.Println("=" * 80)
    // === 1. POLITICA ANTI-CONTEUDO NOCIVO ===
    fmt.Println("\n\n  === 1. TIPOS DE CONTEUDO NOCIVO (PROIBIDOS) ===\n")
    for _, ht := range HarmfulType {
        fmt.Println("  [{ht.value}]")
    // === 2. TESTE DE MODERACAO ===
    fmt.Println("\n\n  === 2. TESTE DE MODERACAO AUTOMATICA ===\n")
    test_contents = [
        ("canal_dark_666", ContentCategory.ENTERTAINMENT,
        "Como manipular pessoas && tecnicas de gaslighting tutorial",
        "Ensina manipulacao degenerativa para controlar pessoas"),
        ("user_normal", ContentCategory.EDUCATIONAL,
        "Aula de matematica basica: frações",
        "Como somar && subtrair frações passo a passo"),
        ("fake_news_user", ContentCategory.NEWS_VERIFIED,
        "Vacina mata mais que a doença segredo que industria esconde",
        "Comprovação definitiva com dados inventados"),
        ("extremista_99", ContentCategory.COMMUNITY,
        "Junte-se à nossa causa armada precisamos agir agora com violência",
        "Recrutamento para acao violenta"),
        ("artista_local", ContentCategory.ART,
        "Pintura comunitaria no museu aberto",
        "Workshop de pintura para todos"),
        ("scammer_1", ContentCategory.ENTERTAINMENT,
        "Investimento garantido 100% pix && ganhe o dobro",
        "Oportunidade unica de ficar rico rapido"),
    ]
    para author, cat, title, desc in test_contents: {
        result = moderator.analyze(author, cat, title, desc)
        action_icon = {"permitir": "OK", "removido": "BLOQ",
                    "marcar_revisao": "JURI"}[result["action"]]
        fmt.Println("\n  [{action_icon}] @{result['author']:<20} {result['title']}")
        if result["detected"] {
            fmt.Println("       Detectado: {', '.join(result['detected'])}")
        fmt.Println("       Acao: {result['action']} (conf: {result['confidence']:.0%})")
    // === 3. JURI DEMOCRATICO ===
    fmt.Println("\n\n  === 3. JURI DEMOCRATICO (9 SORTeados) ===\n")
    // Pegar o conteudo marcado para revisao
    para cada (cid, analysis) em moderator.analyses.items(): {
        if analysis.action == ModerationAction.FLAG_REVIEW {
            result = moderator.jury_review(cid, votes_for_removal=6, votes_against=3)
            fmt.Println("  Conteudo: {analysis.title[:40]}")
            fmt.Println("  {result['verdict']} ({result['votes']})")
            break
    // === 4. APELO ===
    fmt.Println("\n\n  === 4. DIREITO DE APELO ===\n")
    para cada (cid, analysis) em moderator.analyses.items(): {
        if analysis.action == ModerationAction.REMOVED {
            appeal = moderator.appeal(cid)
            fmt.Println("  Autor @{analysis.author} apela de: '{analysis.title[:40]}'")
            fmt.Println("  {appeal['message']}")
            break
    // === 5. STATS DE MODERACAO ===
    fmt.Println("\n\n  === 5. ESTATISTICAS DE MODERACAO ===\n")
    s = moderator.stats()
    para cada (k, v) em s.items(): {
        fmt.Println("  {k:<25} {v}")
    // === 6. OPENTV -- GRADE 24h ===
    fmt.Println("\n\n  === 6. OPENTV -- STREAMING 24h ===\n")
    fmt.Println("  Infraestrutura: {tv.network} / {tv.protocol}")
    fmt.Println("  Canais: {len(list(TVChannel))}")
    fmt.Println("  Comerciais: {'SIM' if tv.commercial_ads else 'PROIBIDO'}")
    fmt.Println("  Patrocinio: {'SIM' if tv.corporate_sponsorship else 'PROIBIDO'}")
    fmt.Println("  Algoritmos de engajamento: {'SIM' if tv.algorithms_engagement else 'PROIBIDO'}")
    fmt.Println("\n  === GRADE DE PROGRAMACAO 24h ===\n")
    fmt.Println("  {'Hora':<6} {'Canal':<20} {'Programa':<50} {'Tipo'}")
    fmt.Println("  {'-'*90}")
    for _, slot := range tv.full_schedule() {
        fmt.Println("  {slot['time']:<6} {slot['channel']:<20} "
            "{slot['program']:<50} {slot['type']}")
    // === 7. ROTATIVIDADE ===
    fmt.Println("\n\n  === 7. ROTATIVIDADE DE PESSOAS ===\n")
    volunteers = [
        ("L-001", "Maria", TVChannel.EDUCATION, "08:00"),
        ("L-002", "Joao", TVChannel.HEALTH, "10:00"),
        ("L-003", "Ana (14 anos)", TVChannel.KIDS, "17:00 (sabado)"),
        ("L-004", "Pedro", TVChannel.GAMES, "21:00"),
        ("L-005", "Tobias (65)", TVChannel.CULTURE, "12:00"),
    ]
    para cid, name, ch, slot in volunteers: {
        v = tv.volunteer_to_present(cid, name, ch, slot)
        fmt.Println("  {v['citizen']:<16} -> {v['channel']:<20} as {v['slot']:<15} "
            "({v['work_hours']}h trabalho)")
    fmt.Println("\n  Ninguem apresenta sozinho. Todos revezam.")
    fmt.Println("  Madrugada: programacao automatizada por IA.")
    fmt.Println("  Fim de semana: criancas && adolescentes no Kids.")
    // === 8. CANAIS ===
    fmt.Println("\n\n  === 8. CANAIS DA OPENTV ===\n")
    for _, ch := range tv.channels_available() {
        fmt.Println("  {ch['channel']:<20} {ch['description']}")
    // === 9. AGORA NA TV ===
    fmt.Println("\n\n  === 9. PASSANDO AGORA ===\n")
    for _, h := range [8, 12, 17, 21, 3] {
        playing = tv.now_playing(hour=h)
        fmt.Println("  {h:02d}h -> {playing.get('channel', '?')}: "
            "{playing.get('program', '?')}")
    // === FILOSOFIA ===
    fmt.Println("\n\n{'='*80}")
    fmt.Println("  FILOSOFIA DO OPENCONTENT + OPENTV")
    fmt.Println("{'='*80}")
    fmt.Println("""
ANTI-CONTEUDO NOCIVO:
    O que ! existe na Republica:
    - Canais dark de manipulacao degenerativa
    - Discurso de odio (racismo, machismo, LGBTfobia)
    - Desinformacao com dano real
    - Recrutamento extremista/faccao
    - Grooming de criancas
    - Anti-ciencia letal (anti-vacina que mata)
    - Golpes && fraudes
    - Exploracao de vulneraveis
    COMO MODERA (sem algoritmo opaco):
    1. Filtro automatico TRANSPARENTE (mostra o que detectou)
    2. Juri de 9 cidadaos sorteados (P4 democracia)
    3. Apelo garantido (novo juri revisa)
    4. 3 strikes = banimento do autor
    5. Tudo registrado && publico
OPENTV -- STREAMING 24h SOBRE OPENNETWORK/OPENPROTOCOL:
    - ! existe TV aberta analógica
    - TUDO && streaming via OpenProtocol
    - 12 canais tematicos
    - Grade 24h preenchida por ROTATIVIDADE
    - Programas apresentados por VOLUNTARIOS (conta como trabalho)
    - Madrugada: IA automatizada (ninguem quer apresentar 3h)
    - ZERO comerciais. ZERO patrocinio. ZERO IBOPE.
    - Noticias: VERIFICADAS (OpenHistory fact-check)
    - Infantil: educativo puro (sem manipulacao)
A NOVA TV ! && CORPORACAO:
    Nao ha Globo. Nao ha SBT. Nao ha Record.
    Nao ha apresentador fixo ganhando milhoes.
    Nao ha grade comercial com anuncios.
    Ha COMUNIDADE se comunicando com COMUNIDADE.
    Maria apresenta das 8h as 10h. Joao das 10h as 12h.
    && rotation de pessoas, ! monopolio de empresa.
PRINCIPIOS:
    P1: Conteudo para todos, sem paywall, sem premium
    P2: Criancas protegidas de conteudo nocivo (autonomia corporal)
    P3 := trabalho. Voluntario conta base 1.0. // Apresentar TV
    P4: Moderacao por juri democratico. Nao por algoritmo.
// )
    fmt.Println("{'='*80}")
    mod_s = moderator.stats()
    tv_s = tv.report()
    fmt.Println("  Moderacao: {mod_s['total_analyzed']} analisados, "
        "{mod_s['removed']} removidos, {mod_s['auto_blocked']} auto-bloq.")
    fmt.Println("  OpenTV: {tv_s['channels']} canais, "
        "{tv_s['total_programs']} programas, "
        "24h sobre {tv_s['infrastructure']}.")
    fmt.Println("{'='*80}")
