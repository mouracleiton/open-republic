# OpenContentPolicy + OpenTV -- TV Aberta e Streaming da Republica

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_content_policy.py`

**Descricao:** ==================================================================
"Toda comunicacao roda na OpenNetwork sobre o OpenProtocol.
 TV aberta NAO existe mais -- existe STREAMING comunitario.
 24h por dia, feito por rotatividade de pessoas."
O QUE ISTO FAZ:
  1. POLITICA ANTI-CONTEUDO NOCIVO: define o que NAO aceita
  2. MODERACAO DEMOCRATICA: juri sorteado, nao algoritmo
  3. OPENtv: streaming 24h sobre OpenNetwork/OpenProtocol
  4. PROGRAMACAO ROTATIVA: pessoas preenchem o tempo, NAO corporacao
  5. CANAIS TEMATICOS: educacao, saude, cultura, jogos, noticias (verificadas)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenContentPolicy + OpenTV -- TV Aberta e Streaming da Republica
==================================================================

"Toda comunicacao roda na OpenNetwork sobre o OpenProtocol.
 TV aberta nao existe mais -- existe STREAMING comunitario.
 24h por dia, feito por rotatividade de pessoas."

O QUE ISTO FAZ:
  1. POLITICA ANTI-CONTEUDO NOCIVO: define o que nao aceita
  2. MODERACAO DEMOCRATICA: juri sorteado, nao algoritmo
  3. OPENtv: streaming 24h sobre OpenNetwork/OpenProtocol
  4. PROGRAMACAO ROTATIVA: pessoas preenchem o tempo, nao corporacao
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

classe ContentCategory herda de Enum:
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


classe HarmfulType herda de Enum:
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


classe ModerationAction herda de Enum:
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
classe ContentAnalysis:
    // Analise de um conteudo postado.
    content_id: texto
    author: texto
    category: ContentCategory
    seja title: texto = ""
    seja description: texto = ""
    seja has_media: logico = falso
    seja media_type: texto = ""  // video, imagem, audio

    // Analise automatica
    seja detected_issues: [HarmfulType] = field(default_factory=list)
    seja auto_confidence: flutuante = 0.0 // 0-1 (confianca na deteccao)
    seja auto_flags: [texto] = field(default_factory=list)

    // Moderacao
    seja action: ModerationAction = ModerationAction.ALLOW
    seja jury_verdict: texto? = nulo
    seja jury_votes_for: inteiro = 0 // votos para remover
    seja jury_votes_against: inteiro = 0 // votos para manter
    seja moderated_by: texto = ""
    seja moderation_date: texto = ""

    // Apelo
    seja appealed: logico = falso
    seja appeal_result: texto = ""


classe ContentModerator:
    // Motor de moderacao de conteudo.

    FLUXO DE MODERACAO (3 camadas):

    CAMADA 1: AUTOMATICA (filtro rapido)
    - Detecta padrões de manipulacao, odio, dano
    - Se claro: bloqueia automaticamente
    - Se duvidoso: manda pra juri

    CAMADA 2: JURI DEMOCRATICO (9 cidadaos sorteados)
    - 9 pessoas aleatorias avaliam
    - Maioria 2/3 decide (6 de 9)
    - Nao e algoritmo. Sao pessoas.
    - Duracao maxima: 24h

    CAMADA 3: APELACAO
    - Autor pode apelar
    - Outro juri (diferente) revisa
    - Decisao final

    O QUE nao EXISTE:
    - Algoritmo opaco decidindo sozinho (P4)
    - Corporacao decidindo o que e "verdade"
    - Banimento sem processo
    - Shadow banning (banimento secreto)

    O QUE EXISTE:
    - Deteccao automatica TRANSPARENTE (mostra o que detectou)
    - Juri de cidadaos (sorteio democratico)
    - Apelo garantido
    - Tudo registrado e publico
    // 

    funcao __init__(self):
        self.analyses: {texto: ContentAnalysis} = {}
        self.jury_pool: [texto] = [] // cidadaos disponiveis para juri
        self.banned_authors: set = set()
        self.stats_auto_blocked: inteiro = 0
        self.stats_jury_reviewed: inteiro = 0
        self.stats_removed: inteiro = 0
        self.stats_allowed: inteiro = 0

    // PADROES DE DETECCAO AUTOMATICA
    seja HARMFUL_PATTERNS: Dict[HarmfulType, [texto]] = {
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
            "vacina mata mais que", "terra é plana e aqui está a prova",
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
            "investimento garantido 100%", "pix e ganhe o dobro",
            "dados do cartão para liberar", "você ganhou sorteio que não participou",
        ],
    }

    funcao analyze(self, author: texto, category: ContentCategory,
                title: texto, description: texto = "",
                seja has_media: logico = falso,
                seja media_type: texto = "") -> {texto: qualquer}:
        // Analisa conteudo automaticamente.
        full_text = (title + " " + description).lower()

        detected = []
        flags = []
        para cada (harm_type, patterns) em self.HARMFUL_PATTERNS.items():
            para cada pattern em patterns:
                se pattern in full_text entao:
                    detected.append(harm_type)
                    flags.append("Padrao detectado: '{pattern}' -> {harm_type.value}")
                    interrompa

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
        se tamanho(detected) >= 2 entao:
            analysis.action = ModerationAction.REMOVED
            analysis.auto_confidence = 0.9
            self.stats_auto_blocked += 1
        senao se tamanho(detected) == 1 entao:
            severity = self._severity(detected[0])
            se severity >= 4 entao:
                analysis.action = ModerationAction.REMOVED
                analysis.auto_confidence = 0.85
                self.stats_auto_blocked += 1
            senao:
                analysis.action = ModerationAction.FLAG_REVIEW
                analysis.auto_confidence = 0.6
        senao:
            analysis.action = ModerationAction.ALLOW
            analysis.auto_confidence = 0.95
            self.stats_allowed += 1

        self.analyses[content_id] = analysis

        retorne {
            "content_id": content_id,
            "author": author,
            "title": title[:50],
            "action": analysis.action.value,
            "detected": [d.value para d em detected],
            "flags": flags,
            "confidence": analysis.auto_confidence,
            "message": self._action_message(analysis),
        }

    funcao _severity(self, harm_type: HarmfulType) -> inteiro:
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
        retorne severity_map.get(harm_type, 2)

    funcao _action_message(self, a: ContentAnalysis) -> texto:
        se a.action == ModerationAction.ALLOW entao:
            retorne "Conteudo permitido."
        se a.action == ModerationAction.REMOVED entao:
            retorne (
                "CONTEUDO REMOVIDO. Detectado: "
                "{', '.join(d.value for d in a.detected_issues)}. "
                "Autor pode apelar. Juri revisara."
            )
        se a.action == ModerationAction.FLAG_REVIEW entao:
            retorne (
                "Conteudo marcado para revisao por juri. "
                "Suspeita: {', '.join(d.value for d in a.detected_issues)}."
            )
        retorne ""

    funcao jury_review(self, content_id: texto,
                    votes_for_removal: inteiro,
                    votes_against: inteiro) -> {texto: qualquer}:
        // Juri democratico decide.
        analysis = self.analyses.get(content_id)
        se nao analysis entao:
            retorne {"error": "Conteudo nao encontrado"}

        analysis.jury_votes_for = votes_for_removal
        analysis.jury_votes_against = votes_against
        total = votes_for_removal + votes_against

        se total == 0 entao:
            retorne {"error": "Sem votos"}

        // 2/3 para remover (6 de 9 tipicamente)
        se votes_for_removal >= total * 0.66 entao:
            analysis.action = ModerationAction.REMOVED
            analysis.jury_verdict = "REMOVIDO por juri"
            self.stats_removed += 1
            self.stats_jury_reviewed += 1

            // Se autor recidiva, banir
            author_strikes = soma(
                1 para a em self.analyses.values()
                if a.author == analysis.author
                 e a.action == ModerationAction.REMOVED
            )
            se author_strikes >= 3 entao:
                analysis.action = ModerationAction.BANNED_AUTHOR
                self.banned_authors.add(analysis.author)

        senao se votes_against >= total * 0.66 entao:
            analysis.action = ModerationAction.ALLOW
            analysis.jury_verdict = "PERMITIDO por juri"
            self.stats_allowed += 1
            self.stats_jury_reviewed += 1
        senao:
            analysis.action = ModerationAction.FLAG_REVIEW
            analysis.jury_verdict = "INCONCLUSIVO -- novo juri"

        retorne {
            "content_id": content_id,
            "verdict": analysis.jury_verdict,
            "action": analysis.action.value,
            "votes": "{votes_for_removal} remover / {votes_against} manter",
        }

    funcao appeal(self, content_id: texto) -> {texto: qualquer}:
        // Autor apela de remocao.
        analysis = self.analyses.get(content_id)
        se nao analysis entao:
            retorne {"error": "nao encontrado"}

        analysis.appealed = verdadeiro
        retorne {
            "content_id": content_id,
            "appeal_filed": verdadeiro,
            "message": (
                "Apelo registrado. Novo juri (diferente) revisara em 48h. "
                "Se revertido, conteudo volta. "
                "Republica garante direito de defesa (P4)."
            ),
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_analyzed": tamanho(self.analyses),
            "auto_blocked": self.stats_auto_blocked,
            "jury_reviewed": self.stats_jury_reviewed,
            "removed": self.stats_removed,
            "allowed": self.stats_allowed,
            "banned_authors": tamanho(self.banned_authors),
        }


// ============================================================================
// 3. OPENtv -- STREAMING COMUNITARIO 24h
// ============================================================================

classe ProgramType herda de Enum:
    LIVE = "ao_vivo"  // streaming ao vivo
    RECORDED = "gravado"  // pre-gravado
    AUTOMATED = "automatizado"  // gerado por IA/republica
    INTERACTIVE = "interativo"  // audiencia participa
    EDUCATIONAL_LOOP = "educativo_loop"  // modulo educativo em loop


classe TVChannel herda de Enum:
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
classe TVProgram:
    // Um programa da grade de TV da Republica.
    program_id: texto
    title: texto
    channel: TVChannel
    program_type: ProgramType
    duration_min: inteiro
    seja presenter: texto = ""  // quem apresenta (rotativo!)
    seja description: texto = ""
    seja interactive: logico = falso // audiencia participa?
    seja age_rating: texto = "Livre"
    seja educational_value: texto = ""

    // Rotatividade
    seja is_rotative: logico = verdadeiro // pessoas revezam na apresentacao
    seja presenters_history: [texto] = field(default_factory=list)


// decorador: @dataclass
classe TVScheduleSlot:
    // Um slot na grade de programacao 24h.
    start_hour: inteiro // 0-23
    start_minute: inteiro // 0 ou 30
    seja program: TVProgram? = nulo
    seja channel: TVChannel = TVChannel.REPUBLIC_MAIN


classe OpenTV:
    // TV Aberta da Republica -- 100% streaming sobre OpenNetwork.

    COMO FUNCIONA:
    1. nao existe TV aberta tradicional (antena/sinal analogico)
    2. TUDO e streaming via OpenNetwork sobre OpenProtocol
    3. Qualquer dispositivo (TV Stick, smartphone, PC, terminal) acessa
    4. Programacao 24h preenchida por ROTATIVIDADE de pessoas
    5. Tempo ocioso = programacao automatizada (modulos educativos, IA)

    ROTATIVIDADE DE PESSOAS:
    - Maria apresenta das 14h-16h (usa tempo de descanso)
    - Joao apresenta das 16h-18h (apos trabalho na horta)
    - Sistema de IA apresenta das 3h-6h (madrugada, ninguem quer)
    - Criancas apresentam programa infantil aos sabados

    nao e CORPORACAO:
    - Nao ha "apresentador fixo" ganhando milhoes
    - Nao ha "grade comercial" com anuncios
    - Nao ha "audiencia" no sentido capitalista (sem IBOPE)
    - e COMUNIDADE se comunicando com comunidade
    // 

    funcao __init__(self):
        self.programs: {texto: TVProgram} = {}
        self.schedule: Dict[inteiro, [TVScheduleSlot]] = defaultdict(list)
        self.active_streamers: {texto: texto} = {} // channel -> presenter atual
        self.total_viewers: inteiro = 0
        self.uptime_hours: flutuante = 0.0

        // Politica
        self.commercial_ads: logico = falso // NUNCA
        self.corporate_sponsorship: logico = falso // NUNCA
        self.algorithms_engagement: logico = falso // NUNCA
        self.hate_content: logico = falso // NUNCA
        self.protocol: texto = "OpenProtocol"
        self.network: texto = "OpenNetwork"

        self._init_default_schedule()

    funcao _init_default_schedule(self):
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

        para hour, minute, title, channel, ptype, duration in default_day:
            prog = TVProgram(
                program_id = hashlib.md5("{title}{hour}".encode()).hexdigest()[:8],
                title = title,
                channel = channel,
                program_type = ptype,
                duration_min = duration,
                is_rotative = verdadeiro,
                description = "Programa {title} -- apresentacao rotativa.",
            )
            self.programs[prog.program_id] = prog
            slot = TVScheduleSlot(hour, minute, prog, channel)
            self.schedule[hour].append(slot)

    funcao volunteer_to_present(self, citizen_id: texto, citizen_name: texto,
                             channel: TVChannel, time_slot: texto) -> {texto: qualquer}:
        // Cidadao se voluntaria para apresentar programa.

        Apresentar TV conta como TRABALHO (P3).
        e contribuicao real para a comunidade.
        // 
        retorne {
            "volunteered": verdadeiro,
            "citizen": citizen_name,
            "channel": channel.value,
            "slot": time_slot,
            "counts_as_work": verdadeiro,
            "work_hours": 2.0,   // tipico 2h de programa
            "credit": 4.0,
            "message": (
                "{citizen_name} vai apresentar no canal {channel.value} "
                "as {time_slot}. Comunidade agradece! "
                "Conta como trabalho (2h base 1.0)."
            ),
        }

    funcao now_playing(self, hour: inteiro = None, minute: inteiro = None) -> {texto: qualquer}:
        // O que esta passando agora em cada canal.
        now_h = hour is nao nulo ? hour : datetime.now().hour

        // Encontrar programa atual no canal principal
        main_slot = nulo
        para cada h em ordene(self.schedule.keys(), reverse=True):
            se h <= now_h entao:
                main_slot = self.schedule[h][0]
                interrompa

        se nao main_slot ou nao main_slot.program entao:
            retorne {"channel": "automatizado", "message": "Programacao automatizada"}

        retorne {
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
        para cada hour em ordene(self.schedule.keys()):
            para cada slot em self.schedule[hour]:
                se slot.program entao:
                    schedule.append({
                        "time": "{slot.start_hour:02d}:{slot.start_minute:02d}",
                        "channel": slot.channel.value,
                        "program": slot.program.title,
                        "type": slot.program.program_type.value,
                        "duration": "{slot.program.duration_min}min",
                        "rotative": slot.program.is_rotative,
                    })
        retorne schedule

    funcao channels_available(self) retorna List[{texto: texto}]:
        // Lista de canais disponiveis.
        retorne [
            {"channel": c.value, "description": self._channel_desc(c)}
            para c em TVChannel
        ]

    funcao _channel_desc(self, c: TVChannel) -> texto:
        descs = {
            TVChannel.REPUBLIC_MAIN: "Canal principal da Republica",
            TVChannel.EDUCATION: "Educacao 24h (OpenEducation + OpenBlackBoard)",
            TVChannel.HEALTH: "Saude + telemedicina (OpenHealth)",
            TVChannel.CULTURE: "Cultura e tradicoes (OpenTradition)",
            TVChannel.GAMES: "Torneios e gameplay (OpenGames)",
            TVChannel.SCIENCE: "Ciencia e tecnologia (OpenScience)",
            TVChannel.DEMOCRACY: "Votacoes e debates ao vivo (P4)",
            TVChannel.KIDS: "Infantil educativo (sem ads)",
            TVChannel.NEWS: "Noticias VERIFICADAS (OpenHistory fact-check)",
            TVChannel.COMMUNITY: "Canais locais comunitarios",
            TVChannel.MUSIC: "Musica aberta sem direitos autorais",
            TVChannel.LABOR: "Trabalho comunitario ao vivo (OpenLaborRelay)",
        }
        retorne descs.get(c, "")

    funcao report(self) -> {texto: qualquer}:
        retorne {
            "total_programs": tamanho(self.programs),
            "channels": tamanho(list(TVChannel)),
            "schedule_slots": soma(tamanho(slots) para slots em self.schedule.values()),
            "infrastructure": "{self.network} / {self.protocol}",
            "commercials": "PROIBIDO",
            "sponsorship": "PROIBIDO",
            "algorithms": "PROIBIDO",
            "uptime_24h": verdadeiro,
        }


// ============================================================================
// 4. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    moderator = ContentModerator()
    tv = OpenTV()

    imprima("=" * 80)
    imprima("  OPENCONTENTPOLICY + OPENTV")
    imprima("  Anti-Conteudo Nocivo + TV Streaming da Republica")
    imprima("=" * 80)

    // === 1. POLITICA ANTI-CONTEUDO NOCIVO ===
    imprima("\n\n  === 1. TIPOS DE CONTEUDO NOCIVO (PROIBIDOS) ===\n")
    para cada ht em HarmfulType:
        imprima("  [{ht.value}]")

    // === 2. TESTE DE MODERACAO ===
    imprima("\n\n  === 2. TESTE DE MODERACAO AUTOMATICA ===\n")

    test_contents = [
        ("canal_dark_666", ContentCategory.ENTERTAINMENT,
         "Como manipular pessoas e tecnicas de gaslighting tutorial",
         "Ensina manipulacao degenerativa para controlar pessoas"),
        ("user_normal", ContentCategory.EDUCATIONAL,
         "Aula de matematica basica: frações",
         "Como somar e subtrair frações passo a passo"),
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
         "Investimento garantido 100% pix e ganhe o dobro",
         "Oportunidade unica de ficar rico rapido"),
    ]

    para author, cat, title, desc in test_contents:
        result = moderator.analyze(author, cat, title, desc)
        action_icon = {"permitir": "OK", "removido": "BLOQ",
                       "marcar_revisao": "JURI"}[result["action"]]
        imprima("\n  [{action_icon}] @{result['author']:<20} {result['title']}")
        se result["detected"] entao:
            imprima("       Detectado: {', '.join(result['detected'])}")
        imprima("       Acao: {result['action']} (conf: {result['confidence']:.0%})")

    // === 3. JURI DEMOCRATICO ===
    imprima("\n\n  === 3. JURI DEMOCRATICO (9 SORTeados) ===\n")
    // Pegar o conteudo marcado para revisao
    para cada (cid, analysis) em moderator.analyses.items():
        se analysis.action == ModerationAction.FLAG_REVIEW entao:
            result = moderator.jury_review(cid, votes_for_removal=6, votes_against=3)
            imprima("  Conteudo: {analysis.title[:40]}")
            imprima("  {result['verdict']} ({result['votes']})")
            interrompa

    // === 4. APELO ===
    imprima("\n\n  === 4. DIREITO DE APELO ===\n")
    para cada (cid, analysis) em moderator.analyses.items():
        se analysis.action == ModerationAction.REMOVED entao:
            appeal = moderator.appeal(cid)
            imprima("  Autor @{analysis.author} apela de: '{analysis.title[:40]}'")
            imprima("  {appeal['message']}")
            interrompa

    // === 5. STATS DE MODERACAO ===
    imprima("\n\n  === 5. ESTATISTICAS DE MODERACAO ===\n")
    s = moderator.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<25} {v}")

    // === 6. OPENTV -- GRADE 24h ===
    imprima("\n\n  === 6. OPENTV -- STREAMING 24h ===\n")
    imprima("  Infraestrutura: {tv.network} / {tv.protocol}")
    imprima("  Canais: {len(list(TVChannel))}")
    imprima("  Comerciais: {'SIM' if tv.commercial_ads else 'PROIBIDO'}")
    imprima("  Patrocinio: {'SIM' if tv.corporate_sponsorship else 'PROIBIDO'}")
    imprima("  Algoritmos de engajamento: {'SIM' if tv.algorithms_engagement else 'PROIBIDO'}")

    imprima("\n  === GRADE DE PROGRAMACAO 24h ===\n")
    imprima("  {'Hora':<6} {'Canal':<20} {'Programa':<50} {'Tipo'}")
    imprima("  {'-'*90}")
    para cada slot em tv.full_schedule():
        imprima("  {slot['time']:<6} {slot['channel']:<20} "
              "{slot['program']:<50} {slot['type']}")

    // === 7. ROTATIVIDADE ===
    imprima("\n\n  === 7. ROTATIVIDADE DE PESSOAS ===\n")
    volunteers = [
        ("L-001", "Maria", TVChannel.EDUCATION, "08:00"),
        ("L-002", "Joao", TVChannel.HEALTH, "10:00"),
        ("L-003", "Ana (14 anos)", TVChannel.KIDS, "17:00 (sabado)"),
        ("L-004", "Pedro", TVChannel.GAMES, "21:00"),
        ("L-005", "Tobias (65)", TVChannel.CULTURE, "12:00"),
    ]
    para cid, name, ch, slot in volunteers:
        v = tv.volunteer_to_present(cid, name, ch, slot)
        imprima("  {v['citizen']:<16} -> {v['channel']:<20} as {v['slot']:<15} "
              "({v['work_hours']}h trabalho)")

    imprima("\n  Ninguem apresenta sozinho. Todos revezam.")
    imprima("  Madrugada: programacao automatizada por IA.")
    imprima("  Fim de semana: criancas e adolescentes no Kids.")

    // === 8. CANAIS ===
    imprima("\n\n  === 8. CANAIS DA OPENTV ===\n")
    para cada ch em tv.channels_available():
        imprima("  {ch['channel']:<20} {ch['description']}")

    // === 9. AGORA NA TV ===
    imprima("\n\n  === 9. PASSANDO AGORA ===\n")
    para cada h em [8, 12, 17, 21, 3]:
        playing = tv.now_playing(hour=h)
        imprima("  {h:02d}h -> {playing.get('channel', '?')}: "
              "{playing.get('program', '?')}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DO OPENCONTENT + OPENTV")
    imprima("{'='*80}")
    imprima("""
  ANTI-CONTEUDO NOCIVO:
    O que nao existe na Republica:
    - Canais dark de manipulacao degenerativa
    - Discurso de odio (racismo, machismo, LGBTfobia)
    - Desinformacao com dano real
    - Recrutamento extremista/faccao
    - Grooming de criancas
    - Anti-ciencia letal (anti-vacina que mata)
    - Golpes e fraudes
    - Exploracao de vulneraveis

    COMO MODERA (sem algoritmo opaco):
    1. Filtro automatico TRANSPARENTE (mostra o que detectou)
    2. Juri de 9 cidadaos sorteados (P4 democracia)
    3. Apelo garantido (novo juri revisa)
    4. 3 strikes = banimento do autor
    5. Tudo registrado e publico

  OPENTV -- STREAMING 24h SOBRE OPENNETWORK/OPENPROTOCOL:
    - nao existe TV aberta analógica
    - TUDO e streaming via OpenProtocol
    - 12 canais tematicos
    - Grade 24h preenchida por ROTATIVIDADE
    - Programas apresentados por VOLUNTARIOS (conta como trabalho)
    - Madrugada: IA automatizada (ninguem quer apresentar 3h)
    - ZERO comerciais. ZERO patrocinio. ZERO IBOPE.
    - Noticias: VERIFICADAS (OpenHistory fact-check)
    - Infantil: educativo puro (sem manipulacao)

  A NOVA TV nao e CORPORACAO:
    Nao ha Globo. Nao ha SBT. Nao ha Record.
    Nao ha apresentador fixo ganhando milhoes.
    Nao ha grade comercial com anuncios.
    Ha COMUNIDADE se comunicando com COMUNIDADE.
    Maria apresenta das 8h as 10h. Joao das 10h as 12h.
    e rotation de pessoas, nao monopolio de empresa.

  PRINCIPIOS:
    P1: Conteudo para todos, sem paywall, sem premium
    P2: Criancas protegidas de conteudo nocivo (autonomia corporal)
    seja P3: Apresentar TV = trabalho. Voluntario conta base 1.0.
    P4: Moderacao por juri democratico. Nao por algoritmo.
// )
    imprima("{'='*80}")
    mod_s = moderator.stats()
    tv_s = tv.report()
    imprima("  Moderacao: {mod_s['total_analyzed']} analisados, "
          "{mod_s['removed']} removidos, {mod_s['auto_blocked']} auto-bloq.")
    imprima("  OpenTV: {tv_s['channels']} canais, "
          "{tv_s['total_programs']} programas, "
          "24h sobre {tv_s['infrastructure']}.")
    imprima("{'='*80}")

```
