# OpenUniversalCaption -- Legendas em Tempo Real para TUDO

**Arquivo original:** `open-republic/core/open_universal_caption.py`

**Descricao:** ==========================================================
"Todo audio que sai do SO e legendado. Surdo nao perde nada."
O surdo nao ouve:
- Videochamada no Jitsi/Meet
- Video no YouTube
- Podcast no navegador
- Musica com letra
- Notificacao do sistema
- Alerta do sistema
- Voz da Iara
Este modulo captura TODO o audio que sai do SO (system audio)
e transcreve em tempo real com Whisper, exibindo legendas flutuantes.
NAO e legenda de um app so. E legenda do SISTEMA INTEIRO.
COMO FUNCIONA (pipeline):
  Audio do SO (PulseAudio/PipeWire/WASM loopback)
  -> Captura em chunks de 500ms
  -> Whisper (STT local) transcreve
  -> Filtro de ruido (musica != fala)
  -> Formatador de legenda (CC standard)
  -> Overlay flutuante na tela
3 MODOS DE LEGENDA:
1. MODO TOTAL: legendas tudo (videochamada + YouTube + podcast + sistema)
2. MODO COMUNICACAO: so transcreve fala humana (ignora musica/ruido)
3. MODO SISTEMA: so transcreve voz da Iara e notificacoes
FORMATO DA LEGENDA (CC standard):
  [14:32:05] Maria: "Bom dia, vamos comecar a reuniao."
  [14:32:12] Joao: "Pode deixar, ja estou com a apresentacao."
  [14:32:20] Maria: "Otimo. Primeiro item: orcamento."
CARACTERISTICAS:
- Posicao configuravel (baixo da tela, topo, overlay)
- Fonte configuravel (tamanho, cor, fundo)
- Cores por falante (se diarizacao disponivel)
- Timestamp em cada linha
- Buffer das ultimas 5 linhas (historico visivel)
- Maximo 2 linhas simultaneas (nao cobre tela inteira)
A ETICA DE LEGENDAR:
  O surdo tem DIREITO a saber o que esta sendo dito.
  Videochamada sem legenda e EXCLUSAO.
  Video institucional sem legenda e DESCASO.
  Podcast sem legenda e INACESSIBILIDADE.
  A Republica NAO pede legenda. A Republica LEGENDA.
  Automaticamente. Para tudo. Em tempo real. Local.
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenUniversalCaption -- Legendas em Tempo Real para TUDO
==========================================================
"Todo audio que sai do SO e legendado. Surdo nao perde nada."

O surdo nao ouve:
- Videochamada no Jitsi/Meet
- Video no YouTube
- Podcast no navegador
- Musica com letra
- Notificacao do sistema
- Alerta do sistema
- Voz da Iara

Este modulo captura TODO o audio que sai do SO (system audio)
e transcreve em tempo real com Whisper, exibindo legendas flutuantes.

NAO e legenda de um app so. E legenda do SISTEMA INTEIRO.

COMO FUNCIONA (pipeline):

  Audio do SO (PulseAudio/PipeWire/WASM loopback)
  -> Captura em chunks de 500ms
  -> Whisper (STT local) transcreve
  -> Filtro de ruido (musica != fala)
  -> Formatador de legenda (CC standard)
  -> Overlay flutuante na tela

3 MODOS DE LEGENDA:

1. MODO TOTAL: legendas tudo (videochamada + YouTube + podcast + sistema)
2. MODO COMUNICACAO: so transcreve fala humana (ignora musica/ruido)
3. MODO SISTEMA: so transcreve voz da Iara e notificacoes

FORMATO DA LEGENDA (CC standard):

  [14:32:05] Maria: "Bom dia, vamos comecar a reuniao."
  [14:32:12] Joao: "Pode deixar, ja estou com a apresentacao."
  [14:32:20] Maria: "Otimo. Primeiro item: orcamento."

CARACTERISTICAS:
- Posicao configuravel (baixo da tela, topo, overlay)
- Fonte configuravel (tamanho, cor, fundo)
- Cores por falante (se diarizacao disponivel)
- Timestamp em cada linha
- Buffer das ultimas 5 linhas (historico visivel)
- Maximo 2 linhas simultaneas (nao cobre tela inteira)

A ETICA DE LEGENDAR:

  O surdo tem DIREITO a saber o que esta sendo dito.
  Videochamada sem legenda e EXCLUSAO.
  Video institucional sem legenda e DESCASO.
  Podcast sem legenda e INACESSIBILIDADE.

  A Republica NAO pede legenda. A Republica LEGENDA.
  Automaticamente. Para tudo. Em tempo real. Local.

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa deque de collections
// importa datetime, timedelta de datetime
// importa re


// ============================================================================
// 1. ENUMS
// ============================================================================

classe FonteAudio herda de Enum:
    // Fontes de audio que o SO pode legendars.
    VIDEOCHAMADA <- ("videochamada", "Videochamada (Jitsi, Meet, Zoom)")
    NAVEGADOR <- ("navegador", "Navegador (YouTube, sites, podcasts)")
    MEDIA_PLAYER <- ("media", "Player de midia (VLC, mpv)")
    SISTEMA <- ("sistema", "Sistema (notificacoes, alertas)")
    IARA <- ("iara", "Iara (voz da Telefonista)")
    MICROFONE_LOCAL <- ("microfone", "Microfone local (pessoa falando ao lado)")
    DESCONHECIDA <- ("desconhecida", "Fonte desconhecida")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe ModoLegenda herda de Enum:
    // Modos de operacao da legenda universal.
    TOTAL <- ("total", "Total: legendas todo audio do SO")
    COMUNICACAO <- ("comunicacao", "Comunicacao: so fala humana (ignora musica)")
    SISTEMA <- ("sistema", "Sistema: so Iara + notificacoes")
    DESLIGADO <- ("desligado", "Desligado")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe PosicaoLegenda herda de Enum:
    // Onde a legenda aparece na tela.
    BAIXO_CENTRO <- ("baixo_centro", "Baixo centro (padrao TV/film)")
    BAIXO_ESQUERDA <- ("baixo_esq", "Baixo esquerda")
    TOPO_CENTRO <- ("topo_centro", "Topo centro")
    TOPO_DIREITA <- ("topo_dir", "Topo direita (overlay)")
    CENTRO <- ("centro", "Centro (para surdo-cego)")
    FLUTUANTE <- ("flutuante", "Flutuante ( segue o foco)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe EstiloLegenda herda de Enum:
    // Estilo visual da legenda.
    PADRAO <- ("padrao", "Padrao: fundo preto semi-transparente, texto branco")
    ALTO_CONTRASTE <- ("alto_contraste", "Alto contraste: fundo preto, texto amarelo")
    CAIXA <- ("caixa", "Caixa: fundo preto opaco, texto branco, borda")
    MINIMALISTA <- ("minimalista", "Minimalista: sem fundo, texto com sombra")
    GRANDE <- ("grande", "Grande: fonte 28pt para baixa visao surdo-cego")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe StatusTranscricao herda de Enum:
    // Status de uma transcricao em andamento.
    OUVINDO <- ("ouvindo", "Ouvindo: capturando audio")
    TRANSCRIVENDO <- ("transcrevendo", "Transcrevendo: Whisper processando")
    PRONTO <- ("pronto", "Pronto: texto transcrito")
    VAZIO <- ("vazio", "Vazio: silencio detectado")
    ERRO <- ("erro", "Erro: falha na transcricao")
    MUSICA <- ("musica", "Musica: audio nao-fala detectado (ignorar)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


// ============================================================================
// 2. DATACLASSES
// ============================================================================

// decorador: @dataclass
classe LinhaLegenda:
    // Uma linha de legenda exibida na tela.
    id: str
    texto: str
    timestamp: str           // "14:32:05"
    declare fonte: FonteAudio  <- FonteAudio.DESCONHECIDA
    declare falante: str  <- ""  // "Maria" (se diarizacao)
    declare confianca: float  <- 0.0  // confianca do Whisper
    declare duracao_ms: int  <- 4000  // quanto tempo fica na tela
    declare cor_falante: str  <- "#FFFFFF"  // cor por falante
    declare parcial: bool  <- FALSO  // transcrição parcial (ainda processando)


// decorador: @dataclass
classe SessaoLegenda:
    // Sessao ativa de legenda universal.
    id: str
    declare modo: ModoLegenda  <- ModoLegenda.COMUNICACAO
    declare posicao: PosicaoLegenda  <- PosicaoLegenda.BAIXO_CENTRO
    declare estilo: EstiloLegenda  <- EstiloLegenda.PADRAO
    declare fonte_tamanho: int  <- 20  // pt
    declare max_linhas_tela: int  <- 2  // max simultaneas
    declare buffer_historico: int  <- 50  // linhas guardadas
    declare transcricoes_totais: int  <- 0
    declare silencios_ignorados: int  <- 0
    declare musicas_ignoradas: int  <- 0
    declare inicio: str  <- ""
    declare ativa: bool  <- VERDADEIRO


// decorador: @dataclass
classe ConfigWhisper:
    // Configuracao do modelo Whisper para legenda.
    declare modelo: str  <- "base"  // tiny, base, small, medium, large-v3-turbo
    declare idioma: str  <- "pt"  // pt-BR
    declare chunk_ms: int  <- 500  // tamanho do chunk de audio
    declare beam_size: int  <- 1  // 1 = rapido (greedy), 5 = preciso
    declare vad_filter: bool  <- VERDADEIRO  // Voice Activity Detection
    declare filtrar_musica: bool  <- VERDADEIRO  // ignorar audio nao-fala


// decorador: @dataclass
classe PerfilUsuarioCC:
    // Perfil do usuario de legenda.
    declare usuario: str  <- "cidadao"
    declare surdo: bool  <- VERDADEIRO
    declare surdo_cego: bool  <- FALSO
    declare baixa_visao: bool  <- FALSO
    declare tdah: bool  <- FALSO
    declare ler_labios: bool  <- FALSO  // se le labios, ver o video e importante
    // preferencias
    declare velocidade_leitura: str  <- "normal"  // lento, normal, rapido
    declare mostrar_timestamp: bool  <- VERDADEIRO
    declare mostrar_falante: bool  <- VERDADEIRO
    declare max_caracteres_linha: int  <- 42  // CC standard


// ============================================================================
// 3. MOTOR DE TRANSCRICAO (simulado)
// ============================================================================

classe TranscritorWhisper:
    // 
    Simula a transcricao de audio pelo Whisper em tempo real.
    No mundo real: faster-whisper ou whisper.cpp capturando audio do sistema.
    Aqui: simulacao deterministica para o demo.
    // 

    // frases de exemplo para a simulacao
    FRASES_EXEMPLO <- [
        "Bom dia a todos, vamos comecar a reuniao.",
        "Primeiro item da pauta: orcamento do trimestre.",
        "Alguem tem alguma duvida sobre os numeros?",
        "Acho que precisamos rever os custos de energia.",
        "Concordo, vamos colocar isso como prioridade.",
        "Pode passar para o proximo slide, por favor.",
        "O prazo final e sexta-feira que vem.",
        "Vou enviar o relatorio por email hoje a tarde.",
        "Obrigado pela participacao de todos.",
        "Boa tarde, em que posso ajudar?",
        "Estou com dificuldade para ouvir, pode repetir?",
        "Vamos definir as responsabilidades de cada um.",
    ]

    FRASES_IARA <- [
        "Abrindo Firefox.",
        "Feito.",
        "Comando executado com sucesso.",
        "Nao reconheci o comando.",
        "Bateria em 45 por cento.",
        "Sao 14 horas e 32 minutos.",
    ]

    FRASES_SISTEMA <- [
        "Atualizacao disponivel.",
        "Bateria fraca. Conecte o carregador.",
        "Conexao WiFi restabelecida.",
        "Novo email recebido.",
    ]

    MUSICAS_EXEMPLO <- [
        "[musica instrumental]",
        "[trilha sonora]",
        "[efeito sonoro]",
        "[ruido de fundo]",
    ]

    funcao __init__(self) retorna None:
        self._counter = 0

    def transcrever_chunk(
        self, fonte: FonteAudio = FonteAudio.DESCONHECIDA
    ) -> Optional[Tuple[str, float, bool]]:
        // 
        Simula transcrever 1 chunk de audio.
        Retorna (texto, confianca, e_musica) ou nulo (silencio).
        // 
        self._counter += 1

        // 60% silencio
        se self._counter % 10 < 6 entao:
            retorne nulo

        // 10% musica/ruido (nao-fala)
        se self._counter % 10 == 6 entao:
            se fonte == FonteAudio.NAVEGADOR entao:
                // importa random
                retorne (random.choice(self.MUSICAS_EXEMPLO), 0.3, VERDADEIRO)
            retorne nulo

        // 30% fala
        // importa random
        se fonte == FonteAudio.IARA entao:
            texto <- random.choice(self.FRASES_IARA)
        senao se fonte == FonteAudio.SISTEMA entao:
            texto <- random.choice(self.FRASES_SISTEMA)
        senao se fonte == FonteAudio.VIDEOCHAMADA entao:
            texto <- random.choice(self.FRASES_EXEMPLO)
        senao se fonte == FonteAudio.NAVEGADOR entao:
            texto <- random.choice(self.FRASES_EXEMPLO)
        senao:
            texto <- random.choice(self.FRASES_EXEMPLO)

        confianca <- random.uniform(0.75, 0.98)
        retorne (texto, round(confianca, 3), FALSO)


// ============================================================================
// 4. ENGINE
// ============================================================================

classe UniversalCaptionEngine:
    // Motor de legenda universal para o SO.

    funcao __init__(self) retorna None:
        self.sessao: Optional[SessaoLegenda] = nulo
        self.transcritor = TranscritorWhisper()
        self.linhas: deque = deque(maxlen=50)   // historico
        self.tela_atual: List[LinhaLegenda] = []   // na tela agora
        self.perfil: PerfilUsuarioCC = PerfilUsuarioCC()
        self.config_whisper = ConfigWhisper()
        self._linha_id = 0
        self._falante_colors: Dict[str, str] = {}
        self._paleta = ["#FFFFFF", "#00FF00", "#00CCFF", "#FFAA00",
                        "#FF69B4", "#AA77FF"]

    // -- sessao ------------------------------------------------------------

    def iniciar(
        self,
        declare usuario: str  <- "cidadao",
        declare modo: ModoLegenda  <- ModoLegenda.COMUNICACAO,
        declare posicao: PosicaoLegenda  <- PosicaoLegenda.BAIXO_CENTRO,
        declare estilo: EstiloLegenda  <- EstiloLegenda.PADRAO,
        declare surdo: bool  <- VERDADEIRO,
        declare surdo_cego: bool  <- FALSO,
        declare baixa_visao: bool  <- FALSO,
    ) -> SessaoLegenda:
        // Inicia sessao de legenda universal.
        // adaptar para surdo-cego
        se surdo_cego entao:
            posicao <- PosicaoLegenda.CENTRO
            estilo <- EstiloLegenda.GRANDE
        senao se baixa_visao entao:
            estilo <- EstiloLegenda.GRANDE

        self.sessao = SessaoLegenda(
            id <- f"CC-{datetime.now().strftime('%H%M%S')}",
            modo <- modo, posicao=posicao, estilo=estilo,
            inicio <- datetime.now().isoformat(),
        )
        self.perfil = PerfilUsuarioCC(
            usuario <- usuario, surdo=surdo, surdo_cego=surdo_cego,
            baixa_visao <- baixa_visao,
        )
        retorne self.sessao

    // -- processar chunk ---------------------------------------------------

    def processar_chunk(
        self, fonte: FonteAudio = FonteAudio.DESCONHECIDA
    ) -> Optional[LinhaLegenda]:
        // 
        Processa 1 chunk de audio do SO.
        No mundo real: captura de PulseAudio/PipeWire monitor.
        Aqui: simulacao.
        // 
        se NAO  self.sessao  OU  NAO  self.sessao.ativa entao:
            retorne nulo

        // filtrar por modo
        se self.sessao.modo == ModoLegenda.SISTEMA entao:
            se fonte NAO  in (FonteAudio.IARA, FonteAudio.SISTEMA) entao:
                retorne nulo
        senao se self.sessao.modo == ModoLegenda.COMUNICACAO entao:
            se fonte == FonteAudio.SISTEMA  E  "notificacao" in fonte.id entao:
                pass   // nao ignora sistema, so filtra musica

        // transcrever
        resultado <- self.transcritor.transcrever_chunk(fonte)

        se resultado e nulo entao:
            self.sessao.silencios_ignorados += 1
            retorne nulo

        desempacote texto, confianca, e_musica <- resultado

        // filtrar musica se configurado
        se e_musica  E  self.config_whisper.filtrar_musica entao:
            self.sessao.musicas_ignoradas += 1
            retorne nulo

        // filtrar confianca baixa
        se confianca < 0.50 entao:
            retorne nulo

        // criar linha de legenda
        self._linha_id += 1
        agora <- datetime.now()
        timestamp <- agora.strftime("%H:%M:%S")
        falante <- self._detectar_falante(texto, fonte)

        linha <- LinhaLegenda(
            id <- f"CC-{self._linha_id:04d}",
            texto <- texto,
            timestamp <- timestamp,
            fonte <- fonte,
            falante <- falante,
            confianca <- confianca,
            duracao_ms <- self._calcular_duracao(texto),
            cor_falante <- self._cor_para_falante(falante),
        )

        self.linhas.append(linha)
        self.sessao.transcricoes_totais += 1
        retorne linha

    funcao _detectar_falante(self, texto: str, fonte: FonteAudio) retorna str:
        // Heuristica simples para identificar falante.
        se fonte == FonteAudio.IARA entao:
            retorne "Iara"
        se fonte == FonteAudio.SISTEMA entao:
            retorne "Sistema"
        // simulacao: alternar entre 2 falantes em videochamada
        se fonte == FonteAudio.VIDEOCHAMADA entao:
            // importa random
            retorne random.choice(["Maria", "Joao", "Pedro"])
        retorne ""

    funcao _calcular_duracao(self, texto: str) retorna int:
        // Calcula quanto tempo a legenda fica na tela (ms).
        // CC standard: ~15 caracteres por segundo de leitura
        chars <- len(texto)
        segs <- max(2, chars / 15)
        se self.perfil  E  self.perfil.velocidade_leitura == "lento" entao:
            segs <- segs * 1.5
        retorne int(segs * 1000)

    funcao _cor_para_falante(self, falante: str) retorna str:
        // Atribui cor consistente a cada falante.
        se NAO  falante entao:
            retorne "#FFFFFF"
        se falante NAO  in self._falante_colors entao:
            cor_idx <- len(self._falante_colors) % len(self._paleta)
            self._falante_colors[falante] = self._paleta[cor_idx]
        retorne self._falante_colors[falante]

    // -- renderizar legenda (ASCII) ----------------------------------------

    funcao renderizar_ascii(self) retorna str:
        // Renderiza a legenda atual como ASCII art (para terminal).
        se NAO  self.tela_atual entao:
            retorne ""
        linhas_render <- []
        para cada linha em self.tela_atual[-self.sessao.max_linhas_tela:]:
            ts <- linha.timestamp if self.perfil.mostrar_timestamp else ""
            falante <- f"{linha.falante}: " if linha.falante  E  self.perfil.mostrar_falante else ""
            prefix <- f"[{ts}] {falante}"
            texto <- linha.texto[:self.perfil.max_caracteres_linha]
            linhas_render.append(f"  {prefix}{texto}")
        retorne "\n".join(linhas_render)

    funcao renderizar_cc_box(self) retorna str:
        // Renderiza legenda em formato de caixa CC standard.
        se NAO  self.tela_atual entao:
            retorne ""
        largura <- self.perfil.max_caracteres_linha + 4
        borda <- "═" * largura
        linhas_render <- [f"  ╔{borda}╗"]
        para cada linha em self.tela_atual[-self.sessao.max_linhas_tela:]:
            ts <- linha.timestamp if self.perfil.mostrar_timestamp else ""
            falante <- f"{linha.falante}: " if linha.falante  E  self.perfil.mostrar_falante else ""
            texto <- linha.texto[:self.perfil.max_caracteres_linha]
            conteudo <- f"[{ts}] {falante}{texto}"
            conteudo <- conteudo[:self.perfil.max_caracteres_linha].ljust(self.perfil.max_caracteres_linha)
            linhas_render.append(f"  ║ {conteudo} ║")
        linhas_render.append(f"  ╚{borda}╝")
        retorne "\n".join(linhas_render)

    // -- exportar transcricao ----------------------------------------------

    funcao exportar_transcricao(self) retorna str:
        // Exporta a transcricao completa da sessao em texto.
        se NAO  self.linhas entao:
            retorne "(sem transcricao)"
        linhas_texto <- []
        para cada linha em self.linhas:
            falante <- f"{linha.falante}: " if linha.falante else ""
            linhas_texto.append(f"[{linha.timestamp}] {falante}{linha.texto}")
        retorne "\n".join(linhas_texto)

    // -- scorecard ---------------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        retorne {
            "modos": len(list(ModoLegenda)),
            "fontes_audio": len(list(FonteAudio)),
            "posicoes": len(list(PosicaoLegenda)),
            "estilos": len(list(EstiloLegenda)),
            "transcricoes_totais": self.sessao.transcricoes_totais if self.sessao else 0,
            "silencios_ignorados": self.sessao.silencios_ignorados if self.sessao else 0,
            "musicas_ignoradas": self.sessao.musicas_ignoradas if self.sessao else 0,
            "linhas_historico": len(self.linhas),
            "falantes_identificados": len(self._falante_colors),
            "config_whisper_modelo": self.config_whisper.modelo,
            "config_chunk_ms": self.config_whisper.chunk_ms,
        }


// ============================================================================
// 5. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- UniversalCaptionEngine()

    print("=" * 70)
    print("OpenUniversalCaption -- Legendas em Tempo Real para TUDO")
    print("=" * 70)

    // --- Visao geral ---
    print(f"""
ESTE MODULO DA LEGENDAS PARA TODO O AUDIO DO SO:

  Videochamada (Jitsi/Meet/Zoom)   -> legendado
  YouTube / video no navegador      -> legendado
  Podcast / radio streaming         -> legendado
  Notificacoes do sistema           -> legendado
  Voz da Iara                       -> legendado
  Pessoa falando ao lado            -> legendado

  Tudo em tempo real. Tudo local. Sem nuvem. Sem Google.
  Whisper roda no processador. Legendas aparecem na tela.
// )

    // --- Fontes de audio ---
    print(f"[FONTES DE AUDIO SUPORTADAS ({len(list(FonteAudio))})]")
    para cada f em FonteAudio:
        print(f"  {f.id:<15} {f.rotulo}")

    // --- Modos ---
    print(f"\n[MODOS DE LEGENDA ({len(list(ModoLegenda))})]")
    para cada m em ModoLegenda:
        print(f"  {m.id:<15} {m.rotulo}")

    // --- Posicoes ---
    print(f"\n[POSICOES ({len(list(PosicaoLegenda))})]")
    para cada p em PosicaoLegenda:
        print(f"  {p.id:<15} {p.rotulo}")

    // --- Estilos ---
    print(f"\n[ESTILOS ({len(list(EstiloLegenda))})]")
    para cada est em EstiloLegenda:
        print(f"  {est.id:<15} {est.rotulo}")

    // --- Simulacao: videochamada ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] Videochamada -- Maria e Joao em reuniao")
    print("=" * 70)
    e.iniciar("Maria", modo=ModoLegenda.COMUNICACAO, surdo=VERDADEIRO)
    print(f"  Sessao: {e.sessao.id}")
    print(f"  Modo: {e.sessao.modo.rotulo}")
    print(f"  Posicao: {e.sessao.posicao.rotulo}")
    print(f"  Estilo: {e.sessao.estilo.rotulo}")

    para cada i em range(40):
        fonte <- FonteAudio.VIDEOCHAMADA
        linha <- e.processar_chunk(fonte)
        se linha entao:
            e.tela_atual.append(linha)
            print(f"\n{e.renderizar_cc_box()}")

    // --- Simulacao: Iara ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] Iara executando comandos")
    print("=" * 70)
    e2 <- UniversalCaptionEngine()
    e2.iniciar("Joao", modo=ModoLegenda.SISTEMA, surdo=VERDADEIRO)
    para cada i em range(20):
        linha <- e2.processar_chunk(FonteAudio.IARA)
        se linha entao:
            e2.tela_atual.append(linha)
            print(f"\n{e2.renderizar_cc_box()}")

    // --- Simulacao: YouTube ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] YouTube -- video educativo")
    print("=" * 70)
    e3 <- UniversalCaptionEngine()
    e3.iniciar("Pedro", modo=ModoLegenda.COMUNICACAO, surdo=VERDADEIRO)
    print("  (musica de introducao deve ser IGNORADA)")
    para cada i em range(30):
        linha <- e3.processar_chunk(FonteAudio.NAVEGADOR)
        se linha entao:
            e3.tela_atual.append(linha)
            print(f"\n{e3.renderizar_cc_box()}")

    // --- Surdo-cego ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] Surdo-cego -- posicao CENTRO, fonte GRANDE")
    print("=" * 70)
    e4 <- UniversalCaptionEngine()
    e4.iniciar("Ana", surdo_cego=VERDADEIRO)
    print(f"  Posicao: {e4.sessao.posicao.rotulo}")
    print(f"  Estilo: {e4.sessao.estilo.rotulo}")
    para cada i em range(15):
        linha <- e4.processar_chunk(FonteAudio.VIDEOCHAMADA)
        se linha entao:
            e4.tela_atual.append(linha)
            print(f"\n{e4.renderizar_cc_box()}")

    // --- Exportar transcricao ---
    print("\n[EXPORTAR TRANSCRICAO COMPLETA]")
    print("-" * 50)
    transcricao <- e.exportar_transcricao()
    print(transcricao[:1000])
    se len(transcricao) > 1000 entao:
        print(f"\n  ... ({len(transcricao) - 1000} caracteres a mais)")

    // --- Pipeline tecnico ---
    print("\n[PIPELINE TECNICO]")
    print("""
  1. CAPTURA DE AUDIO DO SISTEMA:
     PulseAudio/PipeWire monitor source (loopback).
     Sem isso, nao tem audio para transcrever.
     - PulseAudio: module-loopback
     - PipeWire: pipewire-pulse
     - Wayland: xdg-desktop-portal (captura de tela + audio)
     - WASM (browser): Web Audio API

  2. CHUNKING:
     Audio dividido em chunks de 500ms.
     Buffer circular: sempre processa o ultimo segundo.
     Chunk menor <- menor latencia, mais ruido.
     Chunk maior <- mais preciso, mais latencia.

  3. WHISPER (STT local):
     faster-whisper ou whisper.cpp com modelo 'base' ou 'small'.
     - base: 74M params, ~1x realtime em CPU, bom para uso diario
     - small: 244M params, ~0.5x realtime em CPU, mais preciso
     VAD (Voice Activity Detection): pula silencio automaticamente.
     filtrar_musica <- VERDADEIRO: ignora audio nao-fala (economiza CPU).

  4. FORMATACAO CC:
     Texto formatado como Closed Caption standard:
     - Max 42 caracteres por linha
     - Max 2 linhas simultaneas
     - Timestamp [HH:MM:SS]
     - Falante: "Maria: ..."
     - Cor por falante (se diarizacao)

  5. OVERLAY NA TELA:
     - X11: overlay transparente via xrender
     - Wayland: layer-shell protocol (wlr-layer-shell)
     - GNOME: extension que desenha na tela
     - Browser: DIV flutuante (position: fixed)
     Posicao, tamanho e estilo configuraveis.

  6. HISTORICO E EXPORT:
     Ultimas 50 linhas guardadas no buffer.
     Transcricao completa exportavel em .txt ou .srt.
     Para relatorios de reuniao, atas, auditoria.
// )

    // --- Adaptacao por deficiencia ---
    print("[ADAPTACAO POR DEFICIENCIA]")
    print("""
  SURDO:
    Legenda principal. Fonte padrao (20pt).
    Posicao baixo centro (nao atrapalha video).
    Mostra falante e timestamp.

  SURDO-CEGO:
    Fonte GRANDE (28pt+). Posicao CENTRO.
    Alto contraste maximo (preto/amarelo).
    Integracao com display Braille (saida alternativa).
    Linha unica (nao 2 linhas -- confuso para baixa visao+tatil).

  BAIXA VISAO + SURDO (Helen Keller profile):
    Mesmo que surdo-cego. Fonte grande, contraste maximo.
    Reduz velocidade de leitura (legenda fica mais tempo).

  TDAH:
    Legenda minimalista (sem fundo, texto com sombra).
    Sem timestamp (pode distrair).
    Sem cores (apenas branco).
    Reduz sobrecarga visual.

  IDOSO:
    Fonte grande (24pt+).
    Velocidade de leitura LENTA (1.5x mais tempo na tela).
    Alto contraste.
    Falante sempre mostrado (ajuda a seguir conversa).
// )

    // --- Scorecard ---
    print("[SCORECARD]")
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        se isinstance(v, dict) entao:
            print(f"  {k}:")
            para cada (dk, dv) em v.items():
                print(f"    {dk:<25} {dv}")
        senao:
            print(f"  {k:.<28} {v}")

    // --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Legenda e direito, nao favor")
    print("=" * 70)
    print("""
O PROBLEMA:

  Videochamada sem legenda <- EXCLUSAO.
  O surdo nao participa da reuniao.
  Video institucional sem legenda <- DESCASO.
  O surdo nao consome o conteudo.
  Podcast sem legenda <- INACESSIBILIDADE.
  O surdo nao acessa a informacao.

  Hoje, legenda depende da boa vontade de cada plataforma:
  - Google Meet tem legenda automatica (mas so em chamada).
  - YouTube tem legenda automatica (mas nem sempre ligada).
  - Jitsi tem legenda (mas precisa ativar manualmente).
  - Zoom cobra extra por legenda.
  - Podcast: quase nenhum tem legenda.
  - Notificacao do sistema: nenhum tem legenda.

  A Republica NAO pede legenda. A Republica LEGENDA.
  Automaticamente. Para tudo. Em tempo real.

COMO FUNCIONA NA PRATICA:

  O surdo liga o RepublicaOS. Abre o YouTube.
  A legenda aparece automaticamente. Sem ativar nada.
  Abre o Jitsi. Legenda automatica.
  A Iara fala. Legenda automatica.
  Notificacao chega. Legenda automatica.

  O surdo NAO PRECISA PEDIR.
  O sistema JA SABE que o usuario e surdo (perfil).
  E legenda. Sempre. Tudo.

POR QUE LOCAL (Whisper):

  Google Meet usa servidores do Google para legenda.
  Isso significa: audio da sua reuniao vai para o Google.
  A Republica NAO ENVIA audio para ninguem.
  Whisper roda no processador. Audio fica no dispositivo.
  Legenda local <- privacidade local.

  Latencia: Whisper 'base' em CPU ~500ms-1s.
  Para conversa em tempo real, aceitavel.
  Para video, perfeito (legenda sincroniza com video).

A METAFORA DO INTÉRPRETE:

  Um interprete de Libras traduz em tempo real.
  Cada palavra falada vira sinal.
  O surdo acompanha pela Libras.

  O OpenUniversalCaption e o INTERPRETE DIGITAL.
  Cada palavra falada vira TEXTO na tela.
  O surdo acompanha pela leitura.

  Diferente do interprete humano:
  - Esta disponivel 24/7.
  - Nao se cansa.
  - Nao precisa ser agendado.
  - Custo zero (depois de instalado).
  - Transcreve QUALQUER audio, nao so conversa.

A INTEGRACAO COM A IARA:

  Quando a Iara fala ("Abrindo Firefox."),
  a legenda mostra "[14:32] Iara: Abrindo Firefox."
  O surdo VE o que a Iara disse.
  Quando o OpenAmbientSoundAI detecta "campainha",
  a legenda mostra "[14:33] Sistema: CAMPAINHA"
  O surdo-cego com display Braille LE pelo tatil.

  Tudo conectado. Tudo acessivel. Tudo local.
// )


se __name__ == "__main__" entao:
    _demo()

```
