# OpenAccessibilityShim -- Camada de Adaptacao para Software sem Acessibilidade

**Arquivo original:** `open-republic/core/open_accessibility_shim.py`

**Descricao:** =================================================================================
"O app nao tem acessibilidade? O sistema COLOCA."
80% do software do mundo NAO e acessivel. Nao tem AT-SPI. Nao tem leitor
de tela. Nao tem contraste. Nao tem fonte escalavel. Nao tem legenda.
A Republica NAO pode esperar que todo desenvolvedor adicione acessibilidade.
Precisa de uma camada que INJETA acessibilidade por cima de qualquer app.
O SHIM funciona como um ADAPTADOR (como um adaptador de tomada):
- App nao fala AT-SPI? Shim LE a tela (OCR) e expoe para o Orca.
- App nao tem contraste? Shim INVERTE cores em tempo real.
- App nao escala fonte? Shim faz ZOOM de regiao da tela.
- App nao tem legenda? Shim transcreve audio do app com Whisper.
- App nao aceita comando de voz? Shim INJETA xdotool por cima.
- App nao tem focus ring? Shim DESENHA um por cima.
6 ESTRATEGIAS DE ADAPTACAO:
1. SCREEN READER BRIDGE (Orca fallback):
   Para apps que nao expoe arvore de acessibilidade (AT-SPI).
   Shim captura a tela, roda OCR (Tesseract/PaddleOCR), e
   expoe o texto reconhecido como arvore AT-SPI sintetica.
   O Orca le como se o app fosse acessivel.
2. CONTRASTE FORCADO:
   Para apps sem dark mode ou com cores de baixo contraste.
   Shim intercepta a renderizacao (compositor Wayland/X11) e
   aplica filtro: inverte cores, aumenta contraste, ajusta gamma.
   O app nao sabe que foi modificado. O usuario VE melhor.
3. FONTE ESCALAVEL:
   Para apps com fonte minima fixa (muitos apps legados).
   Shim aplica zoom de regiao (magnifier) na area do texto.
   Ou: OCR -> detecta texto -> re-renderiza com fonte maior.
4. CAPTION INJECTION:
   Para players de video sem Closed Caption.
   Shim captura o audio do app, transcreve com Whisper,
   e exibe legenda flutuante por cima do video.
   O app nao sabe que tem legenda. O usuario VE.
5. INPUT INJECTION:
   Para apps que nao respondem a AT-SPI (apps Electron, Java, etc).
   Shim injeta xdotool/ydotool: clique, digite, role.
   O VoiceOSControl manda comando -> Shim injeta no app.
6. FOCUS RING FORCADO:
   Para apps sem indicador visual de foco.
   Shim detecta elemento focado (via OCR ou posicao do cursor)
   e desenha uma borda colorida por cima (overlay compositor).
A ARQUITETURA:
  App sem acessibilidade
    |
    v
  [Compositor Wayland/X11] -- intercepta renderizacao
    |
    v
  [OpenAccessibilityShim] -- camada de adaptacao
    |-- OCR Engine (Tesseract/PaddleOCR) -> texto para Orca
    |-- Contrast Filter (shader OpenGL) -> inverte/ajusta
    |-- Zoom Engine (magnifier) -> fonte maior
    |-- Whisper (audio do app) -> legenda
    |-- xdotool/ydotool -> input injection
    |-- Overlay (layer-shell) -> focus ring + visual cues
    |
    v
  [AT-SPI sintetica] -- expoe para Orca/leitor de tela
    |
    v
  Usuario (cegoouve via Orca, surdo ve via legenda, etc)
DETECCAO AUTOMATICA:
  O Shim MONITORA cada janela aberta. Para cada app, verifica:
  1. Tem arvore AT-SPI? Se SIM, nao precisa de shim (deixa o Orca ler).
  2. Se NAO tem AT-SPI, ativa OCR Bridge.
  3. Tem audio sem legenda? Ativa Caption Injection.
  4. Tem baixo contraste? Ativa Contrast Filter.
  O usuario nao configura nada. O Shim detecta e adapta.
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenAccessibilityShim -- Camada de Adaptacao para Software sem Acessibilidade
=================================================================================
"O app nao tem acessibilidade? O sistema COLOCA."

80% do software do mundo NAO e acessivel. Nao tem AT-SPI. Nao tem leitor
de tela. Nao tem contraste. Nao tem fonte escalavel. Nao tem legenda.

A Republica NAO pode esperar que todo desenvolvedor adicione acessibilidade.
Precisa de uma camada que INJETA acessibilidade por cima de qualquer app.

O SHIM funciona como um ADAPTADOR (como um adaptador de tomada):
- App nao fala AT-SPI? Shim LE a tela (OCR) e expoe para o Orca.
- App nao tem contraste? Shim INVERTE cores em tempo real.
- App nao escala fonte? Shim faz ZOOM de regiao da tela.
- App nao tem legenda? Shim transcreve audio do app com Whisper.
- App nao aceita comando de voz? Shim INJETA xdotool por cima.
- App nao tem focus ring? Shim DESENHA um por cima.

6 ESTRATEGIAS DE ADAPTACAO:

1. SCREEN READER BRIDGE (Orca fallback):
   Para apps que nao expoe arvore de acessibilidade (AT-SPI).
   Shim captura a tela, roda OCR (Tesseract/PaddleOCR), e
   expoe o texto reconhecido como arvore AT-SPI sintetica.
   O Orca le como se o app fosse acessivel.

2. CONTRASTE FORCADO:
   Para apps sem dark mode ou com cores de baixo contraste.
   Shim intercepta a renderizacao (compositor Wayland/X11) e
   aplica filtro: inverte cores, aumenta contraste, ajusta gamma.
   O app nao sabe que foi modificado. O usuario VE melhor.

3. FONTE ESCALAVEL:
   Para apps com fonte minima fixa (muitos apps legados).
   Shim aplica zoom de regiao (magnifier) na area do texto.
   Ou: OCR -> detecta texto -> re-renderiza com fonte maior.

4. CAPTION INJECTION:
   Para players de video sem Closed Caption.
   Shim captura o audio do app, transcreve com Whisper,
   e exibe legenda flutuante por cima do video.
   O app nao sabe que tem legenda. O usuario VE.

5. INPUT INJECTION:
   Para apps que nao respondem a AT-SPI (apps Electron, Java, etc).
   Shim injeta xdotool/ydotool: clique, digite, role.
   O VoiceOSControl manda comando -> Shim injeta no app.

6. FOCUS RING FORCADO:
   Para apps sem indicador visual de foco.
   Shim detecta elemento focado (via OCR ou posicao do cursor)
   e desenha uma borda colorida por cima (overlay compositor).

A ARQUITETURA:

  App sem acessibilidade
    |
    v
  [Compositor Wayland/X11] -- intercepta renderizacao
    |
    v
  [OpenAccessibilityShim] -- camada de adaptacao
    |-- OCR Engine (Tesseract/PaddleOCR) -> texto para Orca
    |-- Contrast Filter (shader OpenGL) -> inverte/ajusta
    |-- Zoom Engine (magnifier) -> fonte maior
    |-- Whisper (audio do app) -> legenda
    |-- xdotool/ydotool -> input injection
    |-- Overlay (layer-shell) -> focus ring + visual cues
    |
    v
  [AT-SPI sintetica] -- expoe para Orca/leitor de tela
    |
    v
  Usuario (cegoouve via Orca, surdo ve via legenda, etc)

DETECCAO AUTOMATICA:

  O Shim MONITORA cada janela aberta. Para cada app, verifica:
  1. Tem arvore AT-SPI? Se SIM, nao precisa de shim (deixa o Orca ler).
  2. Se NAO tem AT-SPI, ativa OCR Bridge.
  3. Tem audio sem legenda? Ativa Caption Injection.
  4. Tem baixo contraste? Ativa Contrast Filter.

  O usuario nao configura nada. O Shim detecta e adapta.

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa datetime de datetime
// importa re


// ============================================================================
// 1. ENUMS
// ============================================================================

classe EstrategiaAdaptacao herda de Enum:
    // As 6 estrategias de injecao de acessibilidade.
    OCR_BRIDGE <- ("ocr", "OCR Bridge: le tela e expoe para Orca (cego)")
    CONTRASTE <- ("contraste", "Contraste forçado: inverte/ajusta cores")
    FONTE_ZOOM <- ("fonte", "Fonte escalavel: zoom de regiao de texto")
    CAPTION_INJECTION <- ("caption", "Caption injection: legenda audio do app")
    INPUT_INJECTION <- ("input", "Input injection: xdotool/ydotool para apps nao-AT-SPI")
    FOCUS_RING <- ("focus", "Focus ring forcado: borda visual no elemento focado")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe NivelAcessibilidadeApp herda de Enum:
    // Quao acessivel o app e nativamente.
    NATIVO <- ("nativo", "Nativo: tem AT-SPI completo (GNOME, GTK, Qt)")
    PARCIAL <- ("parcial", "Parcial: tem algo mas nao tudo (Electron, alguns Java)")
    MINIMO <- ("minimo", "Minimo: quase nada (apps antigos, alguns jogos)")
    NENHUM <- ("nenhum", "Nenhum: zero acessibilidade (canvas, WebGL, terminal cru)")
    DESCONHECIDO <- ("desconhecido", "Desconhecido: shim analisa para descobrir")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe TipoApp herda de Enum:
    // Tipos de aplicativos e seu nivel tipico de acessibilidade.
    GTK <- ("gtk", "GTK (GNOME): nativamente acessivel")
    QT <- ("qt", "Qt (KDE): nativamente acessivel")
    ELECTRON <- ("electron", "Electron (VS Code, Slack, Discord): parcial")
    JAVA <- ("java", "Java Swing: parcial (precisa Java Access Bridge)")
    FLTK <- ("fltk", "FLTK/Tk: minimo")
    CANVAS_WEBGL <- ("canvas", "Canvas/WebGL (jogos, tools visuais): nenhum")
    TERMINAL_CRU <- ("terminal", "Terminal sem AT-SPI: nenhum")
    WINE <- ("wine", "Wine/Windows app: nenhum (sem MSAA no Linux)")
    PROPRIETARIO <- ("proprietario", "Proprietario fechado: desconhecido")
    ANDROID_APP <- ("android", "Android app (via anbox/waydroid): parcial")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe StatusAdaptacao herda de Enum:
    // Status da adaptacao de um app.
    ATIVO <- ("ativo", "Shim ativo: adaptando este app")
    PAUSADO <- ("pausado", "Pausado: app acessivel nativamente, shim nao needed")
    FALHOU <- ("falhou", "Falhou: OCR/adaptacao nao funcionou")
    ANALISANDO <- ("analisando", "Analisando: detectando nivel de acessibilidade")
    DESLIGADO <- ("desligado", "Desligado: usuario desativou shim para este app")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe DeficienciaAlvo herda de Enum:
    // Que deficiencia a estrategia de adaptacao atende.
    CEGUEIRA <- ("cego", "Cegueira: precisa de leitor de tela / OCR")
    BAIXA_VISAO <- ("baixa_visao", "Baixa visao: precisa de zoom / contraste")
    SURDEZ <- ("surdo", "Surdez: precisa de legenda")
    MOTORA <- ("motora", "Motora: precisa de input injection")
    DALTONISMO <- ("daltonismo", "Daltonismo: precisa de ajuste de cores")
    COGNITIVA <- ("cognitiva", "Cognitiva: precisa de simplificacao visual")

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
classe AppDetectado:
    // Um app detectado pelo shim.
    pid: int
    nome: str                 // "firefox", "code", "discord"
    declare titulo_janela: str  <- ""  // "OpenRepublic IDE - main.py"
    declare tipo: TipoApp  <- TipoApp.PROPRIETARIO
    declare nivel_nat: NivelAcessibilidadeApp  <- NivelAcessibilidadeApp.DESCONHECIDO
    declare tem_atspi: bool  <- FALSO
    declare tem_audio: bool  <- FALSO
    declare tem_video: bool  <- FALSO
    declare toolkit: str  <- ""  // "gtk3", "electron", "qt6"


// decorador: @dataclass
classe AdaptacaoAtiva:
    // Uma adaptacao ativa para um app.
    app_pid: int
    estrategia: EstrategiaAdaptacao
    declare status: StatusAdaptacao  <- StatusAdaptacao.ATIVO
    // performance
    declare cpu_pct: float  <- 0.0
    declare ram_mb: float  <- 0.0
    declare latencia_ms: float  <- 0.0
    // resultados
    declare texto_ocr_ultima_linha: str  <- ""
    declare legenda_ultima: str  <- ""
    // config
    declare intervalo_ms: int  <- 500  // quanto tempo entre ciclos de OCR


// decorador: @dataclass
classe PerfilAdaptacao:
    // Perfil do usuario define quais adaptacoes ativar.
    declare cego: bool  <- FALSO
    declare baixa_visao: bool  <- FALSO
    declare surdo: bool  <- FALSO
    declare motora: bool  <- FALSO
    declare daltonismo: str  <- ""  // "protanopia", "deuteranopia", "tritanopia"
    declare cognitiva: bool  <- FALSO
    // preferencias
    declare ocr_idioma: str  <- "por"  // Tesseract lang
    declare contraste_nivel: str  <- "alto"  // baixo, medio, alto, maximo
    declare zoom_nivel: float  <- 2.0
    declare legenda_posicao: str  <- "baixo"


// decorador: @dataclass
classe RegraAdaptacao:
    // Regra: se app e tipo X e usuario e Y, ativar estrategia Z.
    tipo_app: TipoApp
    deficiencia: DeficienciaAlvo
    estrategia: EstrategiaAdaptacao
    declare prioridade: int  <- 5  // 1 (alta) a 10 (baixa)
    declare condicao: str  <- ""  // "sempre", "se_sem_atspi", "se_tem_audio"


// ============================================================================
// 3. TABELA DE REGRAS DE ADAPTACAO
// ============================================================================

funcao _init_regras() retorna List[RegraAdaptacao]:
    // Define quando cada estrategia e ativada.
    retorne [
        // OCR Bridge: para apps sem AT-SPI + usuario cego
        RegraAdaptacao(TipoApp.CANVAS_WEBGL, DeficienciaAlvo.CEGUEIRA,
                       EstrategiaAdaptacao.OCR_BRIDGE, 1, "sempre"),
        RegraAdaptacao(TipoApp.TERMINAL_CRU, DeficienciaAlvo.CEGUEIRA,
                       EstrategiaAdaptacao.OCR_BRIDGE, 1, "sempre"),
        RegraAdaptacao(TipoApp.WINE, DeficienciaAlvo.CEGUEIRA,
                       EstrategiaAdaptacao.OCR_BRIDGE, 2, "sempre"),
        RegraAdaptacao(TipoApp.PROPRIETARIO, DeficienciaAlvo.CEGUEIRA,
                       EstrategiaAdaptacao.OCR_BRIDGE, 2, "se_sem_atspi"),
        RegraAdaptacao(TipoApp.ELECTRON, DeficienciaAlvo.CEGUEIRA,
                       EstrategiaAdaptacao.OCR_BRIDGE, 3, "se_sem_atspi"),
        RegraAdaptacao(TipoApp.JAVA, DeficienciaAlvo.CEGUEIRA,
                       EstrategiaAdaptacao.OCR_BRIDGE, 3, "se_sem_atspi"),

        // Contraste: para baixa visao + daltonismo
        RegraAdaptacao(TipoApp.CANVAS_WEBGL, DeficienciaAlvo.BAIXA_VISAO,
                       EstrategiaAdaptacao.CONTRASTE, 1, "sempre"),
        RegraAdaptacao(TipoApp.PROPRIETARIO, DeficienciaAlvo.BAIXA_VISAO,
                       EstrategiaAdaptacao.CONTRASTE, 2, "sempre"),
        RegraAdaptacao(TipoApp.ELECTRON, DeficienciaAlvo.BAIXA_VISAO,
                       EstrategiaAdaptacao.CONTRASTE, 3, "sempre"),
        RegraAdaptacao(TipoApp.GTK, DeficienciaAlvo.BAIXA_VISAO,
                       EstrategiaAdaptacao.CONTRASTE, 5, "se_baixo_contraste"),

        // Fonte/Zoom: para baixa visao
        RegraAdaptacao(TipoApp.FLTK, DeficienciaAlvo.BAIXA_VISAO,
                       EstrategiaAdaptacao.FONTE_ZOOM, 1, "sempre"),
        RegraAdaptacao(TipoApp.TERMINAL_CRU, DeficienciaAlvo.BAIXA_VISAO,
                       EstrategiaAdaptacao.FONTE_ZOOM, 2, "sempre"),
        RegraAdaptacao(TipoApp.PROPRIETARIO, DeficienciaAlvo.BAIXA_VISAO,
                       EstrategiaAdaptacao.FONTE_ZOOM, 3, "se_fonte_pequena"),

        // Caption Injection: para surdo + apps com audio/video
        RegraAdaptacao(TipoApp.ELECTRON, DeficienciaAlvo.SURDEZ,
                       EstrategiaAdaptacao.CAPTION_INJECTION, 1, "se_tem_audio"),
        RegraAdaptacao(TipoApp.PROPRIETARIO, DeficienciaAlvo.SURDEZ,
                       EstrategiaAdaptacao.CAPTION_INJECTION, 1, "se_tem_audio"),
        RegraAdaptacao(TipoApp.CANVAS_WEBGL, DeficienciaAlvo.SURDEZ,
                       EstrategiaAdaptacao.CAPTION_INJECTION, 1, "se_tem_audio"),

        // Input Injection: para motora + apps sem AT-SPI
        RegraAdaptacao(TipoApp.ELECTRON, DeficienciaAlvo.MOTORA,
                       EstrategiaAdaptacao.INPUT_INJECTION, 1, "se_sem_atspi"),
        RegraAdaptacao(TipoApp.JAVA, DeficienciaAlvo.MOTORA,
                       EstrategiaAdaptacao.INPUT_INJECTION, 2, "se_sem_atspi"),
        RegraAdaptacao(TipoApp.WINE, DeficienciaAlvo.MOTORA,
                       EstrategiaAdaptacao.INPUT_INJECTION, 2, "sempre"),
        RegraAdaptacao(TipoApp.CANVAS_WEBGL, DeficienciaAlvo.MOTORA,
                       EstrategiaAdaptacao.INPUT_INJECTION, 1, "sempre"),

        // Focus Ring: para baixa visao + cognitiva
        RegraAdaptacao(TipoApp.CANVAS_WEBGL, DeficienciaAlvo.BAIXA_VISAO,
                       EstrategiaAdaptacao.FOCUS_RING, 2, "sempre"),
        RegraAdaptacao(TipoApp.PROPRIETARIO, DeficienciaAlvo.COGNITIVA,
                       EstrategiaAdaptacao.FOCUS_RING, 3, "sempre"),
        RegraAdaptacao(TipoApp.FLTK, DeficienciaAlvo.BAIXA_VISAO,
                       EstrategiaAdaptacao.FOCUS_RING, 2, "sempre"),
    ]


// ============================================================================
// 4. MOTOR DE ADAPTACAO
// ============================================================================

classe AccessibilityShimEngine:
    // Motor da camada de adaptacao para apps sem acessibilidade.

    funcao __init__(self) retorna None:
        self.regras: List[RegraAdaptacao] = _init_regras()
        self.apps_monitorados: Dict[int, AppDetectado] = {}
        self.adaptacoes_ativas: Dict[int, List[AdaptacaoAtiva]] = defaultdict(list)
        self.perfil: PerfilAdaptacao = PerfilAdaptacao()

    // -- configurar perfil -------------------------------------------------

    def configurar_perfil(
        self,
        declare cego: bool  <- FALSO,
        declare baixa_visao: bool  <- FALSO,
        declare surdo: bool  <- FALSO,
        declare motora: bool  <- FALSO,
        declare daltonismo: str  <- "",
        declare cognitiva: bool  <- FALSO,
    ) -> PerfilAdaptacao:
        self.perfil = PerfilAdaptacao(
            cego <- cego, baixa_visao=baixa_visao, surdo=surdo,
            motora <- motora, daltonismo=daltonismo, cognitiva=cognitiva,
        )
        retorne self.perfil

    // -- registrar app detectado -------------------------------------------

    def registrar_app(
        self,
        pid: int,
        nome: str,
        declare tipo: TipoApp  <- TipoApp.PROPRIETARIO,
        declare titulo: str  <- "",
        declare tem_atspi: bool  <- FALSO,
        declare tem_audio: bool  <- FALSO,
        declare tem_video: bool  <- FALSO,
        declare toolkit: str  <- "",
    ) -> AppDetectado:
        // Registra um app detectado pelo monitor de janelas.
        // determinar nivel nativo
        niveis <- {
            TipoApp.GTK: NivelAcessibilidadeApp.NATIVO,
            TipoApp.QT: NivelAcessibilidadeApp.NATIVO,
            TipoApp.ELECTRON: NivelAcessibilidadeApp.PARCIAL,
            TipoApp.JAVA: NivelAcessibilidadeApp.PARCIAL,
            TipoApp.FLTK: NivelAcessibilidadeApp.MINIMO,
            TipoApp.CANVAS_WEBGL: NivelAcessibilidadeApp.NENHUM,
            TipoApp.TERMINAL_CRU: NivelAcessibilidadeApp.NENHUM,
            TipoApp.WINE: NivelAcessibilidadeApp.NENHUM,
            TipoApp.PROPRIETARIO: NivelAcessibilidadeApp.DESCONHECIDO,
            TipoApp.ANDROID_APP: NivelAcessibilidadeApp.PARCIAL,
        }
        app <- AppDetectado(
            pid <- pid, nome=nome, tipo=tipo, titulo_janela=titulo,
            tem_atspi <- tem_atspi, tem_audio=tem_audio, tem_video=tem_video,
            toolkit <- toolkit,
            nivel_nat <- niveis.get(tipo, NivelAcessibilidadeApp.DESCONHECIDO),
        )
        self.apps_monitorados[pid] = app
        retorne app

    // -- decidir adaptacoes ------------------------------------------------

    funcao decidir_adaptacoes(self, app: AppDetectado) retorna List[EstrategiaAdaptacao]:
        // 
        Decide quais estrategias de adaptacao ativar para o app.
        Baseado no tipo do app + perfil do usuario + regras.
        // 
        declare estrategias: List[EstrategiaAdaptacao]  <- []

        // mapear perfil para deficiencias ativas
        declare deficiencias_ativas: List[DeficienciaAlvo]  <- []
        se self.perfil.cego entao:
            deficiencias_ativas.append(DeficienciaAlvo.CEGUEIRA)
        se self.perfil.baixa_visao entao:
            deficiencias_ativas.append(DeficienciaAlvo.BAIXA_VISAO)
        se self.perfil.surdo entao:
            deficiencias_ativas.append(DeficienciaAlvo.SURDEZ)
        se self.perfil.motora entao:
            deficiencias_ativas.append(DeficienciaAlvo.MOTORA)
        se self.perfil.daltonismo entao:
            deficiencias_ativas.append(DeficienciaAlvo.DALTONISMO)
        se self.perfil.cognitiva entao:
            deficiencias_ativas.append(DeficienciaAlvo.COGNITIVA)

        // encontrar regras aplicaveis
        regras_match <- [
            r for r in self.regras
            if r.tipo_app == app.tipo  E  r.deficiencia in deficiencias_ativas
        ]

        // ordenar por prioridade
        regras_match.sort(key=funcao anonima(r): r.prioridade)

        para cada regra em regras_match:
            // verificar condicao
            se regra.condicao == "se_sem_atspi"  E  app.tem_atspi entao:
                continue   // app tem AT-SPI, nao precisa de shim
            se regra.condicao == "se_tem_audio"  E  NAO  app.tem_audio entao:
                continue   // app nao tem audio, nao precisa de legenda
            se regra.condicao == "se_baixo_contraste" entao:
                pass   // simplificado: sempre ativa se baixa visao
            se regra.condicao == "se_fonte_pequena" entao:
                pass   // simplificado

            se regra.estrategia NAO  in estrategias entao:
                estrategias.append(regra.estrategia)

        retorne estrategias

    // -- ativar adaptacao --------------------------------------------------

    funcao ativar_adaptacao(self, app: AppDetectado) retorna List[AdaptacaoAtiva]:
        // Ativa as adaptacoes decididas para o app.
        estrategias <- self.decidir_adaptacoes(app)
        declare adaptacoes: List[AdaptacaoAtiva]  <- []

        para cada est em estrategias:
            // simular custo de cada estrategia
            desempacote cpu, ram, lat <- self._estimar_custo(est)
            adapt <- AdaptacaoAtiva(
                app_pid <- app.pid,
                estrategia <- est,
                cpu_pct <- cpu,
                ram_mb <- ram,
                latencia_ms <- lat,
                intervalo_ms <- self._intervalo_recomendado(est),
            )
            adaptacoes.append(adapt)
            self.adaptacoes_ativas[app.pid].append(adapt)

        retorne adaptacoes

    funcao _estimar_custo(self, est: EstrategiaAdaptacao) retorna Tuple[float, float, float]:
        // Estima CPU%, RAM MB, latencia ms por estrategia.
        custos <- {
            EstrategiaAdaptacao.OCR_BRIDGE: (15.0, 200.0, 300.0),
            EstrategiaAdaptacao.CONTRASTE: (2.0, 20.0, 5.0),
            EstrategiaAdaptacao.FONTE_ZOOM: (5.0, 50.0, 20.0),
            EstrategiaAdaptacao.CAPTION_INJECTION: (20.0, 300.0, 500.0),
            EstrategiaAdaptacao.INPUT_INJECTION: (1.0, 10.0, 10.0),
            EstrategiaAdaptacao.FOCUS_RING: (3.0, 30.0, 15.0),
        }
        retorne custos.get(est, (5.0, 50.0, 50.0))

    funcao _intervalo_recomendado(self, est: EstrategiaAdaptacao) retorna int:
        // Intervalo entre ciclos (ms) por estrategia.
        intervalos <- {
            EstrategiaAdaptacao.OCR_BRIDGE: 500,        // 2x por segundo
            EstrategiaAdaptacao.CONTRASTE: 0,            // continuo (shader)
            EstrategiaAdaptacao.FONTE_ZOOM: 0,           // continuo (magnifier)
            EstrategiaAdaptacao.CAPTION_INJECTION: 500,  // 2x por segundo (Whisper)
            EstrategiaAdaptacao.INPUT_INJECTION: 0,      // on-demand
            EstrategiaAdaptacao.FOCUS_RING: 100,         // 10x por segundo
        }
        retorne intervalos.get(est, 500)

    // -- OCR Bridge (simulado) ---------------------------------------------

    funcao ocr_extrair_texto(self, app: AppDetectado) retorna List[str]:
        // 
        Simula extracao de texto da tela via OCR.
        No mundo real: Tesseract ou PaddleOCR no screenshot da janela.
        // 
        textos_simulados <- {
            "firefox": [
                "Barra de enderecos: republica.local",
                "Botao: Voltar | Botao: Avancar | Botao: Atualizar",
                "Link: Documentacao | Link: Forum | Link: Download",
                "Texto: Bem-vindo a Republica Aberta",
                "Campo de busca: Digite para pesquisar...",
            ],
            "discord": [
                "Canal: geral | Canal: desenvolvimento | Canal: acessibilidade",
                "Mensagem de Maria: Bom dia pessoal!",
                "Mensagem de Joao: Alguem pode ajudar com o i3?",
                "Campo de mensagem: Digite aqui...",
                "Botao: Enviar | Botao: Anexar | Botao: Emoji",
            ],
            "code": [
                "Aba: open_iara.py | Aba: terminal",
                "Linha 42: def _demo():",
                "Linha 43:     print('OpenIara')",
                "Painel: Explorador | Painel: Editor | Painel: Terminal",
                "Status: Python 3.11 | UTF-8 | Espacos: 4",
            ],
            "jogo": [
                "Menu: Novo Jogo | Continuar | Configuracoes | Sair",
                "Vida: 100% | Municao: 30 | Pontos: 1250",
                "Botao: Atacar | Botao: Defender | Botao: Item",
            ],
        }
        retorne textos_simulados.get(app.nome.lower(), [
            f"[OCR] Texto detectado na janela: {app.titulo_janela}",
            "[OCR] Interface grafica detectada",
            "[OCR] Botoes e campos identificados",
        ])

    // -- Caption Injection (simulado) --------------------------------------

    funcao caption_extrair_legenda(self, app: AppDetectado) retorna str:
        // 
        Simula legenda do audio do app via Whisper.
        No mundo real: captura audio do app (PulseAudio) -> Whisper.
        // 
        legendas <- {
            "firefox": "Pagina carregada. Conteudo sobre a Republica Aberta.",
            "discord": "Maria disse: bom dia pessoal.",
            "vlc": "E entao ele disse: a Republica e para todos.",
            "youtube": "Neste video, vamos aprender sobre acessibilidade.",
        }
        retorne legendas.get(app.nome.lower(), "[audio do app detectado, transcrevendo...]")

    // -- relatorio ----------------------------------------------------------

    funcao relatorio_adaptacoes(self) retorna Dict[str, Any]:
        // Gera relatorio de todas as adaptacoes ativas.
        total_cpu <- 0.0
        total_ram <- 0.0
        declare por_estategia: Dict[str, int]  <- defaultdict(int)

        para cada (pid, adaptacoes) em self.adaptacoes_ativas.items():
            para cada a em adaptacoes:
                total_cpu <- total_cpu + a.cpu_pct
                total_ram <- total_ram + a.ram_mb
                por_estategia[a.estrategia.id] += 1

        retorne {
            "apps_monitorados": len(self.apps_monitorados),
            "apps_com_adaptacao": len(self.adaptacoes_ativas),
            "adaptacoes_totais": sum(len(v) for v in self.adaptacoes_ativas.values()),
            "cpu_total_estimada": round(total_cpu, 1),
            "ram_total_estimada_mb": round(total_ram, 0),
            "por_estrategia": dict(por_estategia),
        }

    // -- scorecard ----------------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        retorne {
            "estrategias": len(list(EstrategiaAdaptacao)),
            "tipos_app": len(list(TipoApp)),
            "niveis_acessibilidade": len(list(NivelAcessibilidadeApp)),
            "deficiencias_alvo": len(list(DeficienciaAlvo)),
            "regras_cadastradas": len(self.regras),
            "apps_monitorados": len(self.apps_monitorados),
            "adaptacoes_ativas": sum(len(v) for v in self.adaptacoes_ativas.values()),
        }


// ============================================================================
// 5. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- AccessibilityShimEngine()

    print("=" * 70)
    print("OpenAccessibilityShim -- Adaptacao para Software sem Acessibilidade")
    print("=" * 70)

    // --- As 6 estrategias ---
    print(f"\n[AS 6 ESTRATEGIAS DE ADAPTACAO]")
    para cada est em EstrategiaAdaptacao:
        desempacote cpu, ram, lat <- e._estimar_custo(est)
        intervalo <- e._intervalo_recomendado(est)
        freq <- f"{1000/intervalo:.0f}x/seg" if intervalo > 0 else "continuo"
        print(f"\n  [{est.id}] {est.rotulo}")
        print(f"    Custo: {cpu:.0f}% CPU, {ram:.0f}MB RAM, {lat:.0f}ms latencia")
        print(f"    Frequencia: {freq}")

    // --- Tipos de app ---
    print(f"\n[TIPOS DE APP E SEU NIVEL NATIVO]")
    para cada tipo em TipoApp:
        niveis <- {
            TipoApp.GTK: "NATIVO", TipoApp.QT: "NATIVO",
            TipoApp.ELECTRON: "PARCIAL", TipoApp.JAVA: "PARCIAL",
            TipoApp.ANDROID_APP: "PARCIAL",
            TipoApp.FLTK: "MINIMO",
            TipoApp.CANVAS_WEBGL: "NENHUM", TipoApp.TERMINAL_CRU: "NENHUM",
            TipoApp.WINE: "NENHUM",
            TipoApp.PROPRIETARIO: "DESCONHECIDO",
        }
        nivel <- niveis.get(tipo, "?")
        print(f"  {tipo.id:<15} {nivel:<12} {tipo.rotulo}")

    // --- Configurar perfil ---
    print("\n[PERFIL: Usuario cego + baixa visao]")
    e.configurar_perfil(cego=VERDADEIRO, baixa_visao=VERDADEIRO)
    print(f"  Cego: {e.perfil.cego}")
    print(f"  Baixa visao: {e.perfil.baixa_visao}")
    print(f"  OCR idioma: {e.perfil.ocr_idioma}")
    print(f"  Contraste: {e.perfil.contraste_nivel}")

    // --- Cenario 1: Discord (Electron) ---
    print("\n" + "=" * 70)
    print("[CENARIO 1] Discord (Electron) -- parcialmente acessivel")
    print("=" * 70)
    discord <- e.registrar_app(
        pid <- 1234, nome="discord", tipo=TipoApp.ELECTRON,
        titulo <- "Discord - #geral", tem_atspi=FALSO, tem_audio=VERDADEIRO,
        toolkit <- "electron"
    )
    print(f"  App: {discord.nome} ({discord.tipo.id})")
    print(f"  Nivel nativo: {discord.nivel_nat.rotulo}")
    print(f"  Tem AT-SPI: {discord.tem_atspi}")
    print(f"  Tem audio: {discord.tem_audio}")

    adaptacoes <- e.ativar_adaptacao(discord)
    print(f"\n  ADAPTACOES ATIVADAS ({len(adaptacoes)}):")
    para cada a em adaptacoes:
        print(f"    [{a.estrategia.id}] {a.estrategia.rotulo}")
        print(f"      Custo: {a.cpu_pct:.0f}% CPU, {a.ram_mb:.0f}MB RAM")

    // OCR bridge resultado
    textos <- e.ocr_extrair_texto(discord)
    print(f"\n  OCR BRIDGE (texto extraido da tela):")
    para cada t em textos:
        print(f"    -> \"{t}\"")

    // Caption injection
    legenda <- e.caption_extrair_legenda(discord)
    print(f"\n  CAPTION INJECTION (legenda do audio):")
    print(f"    -> \"{legenda}\"")

    // --- Cenario 2: Jogo Canvas/WebGL ---
    print("\n" + "=" * 70)
    print("[CENARIO 2] Jogo Canvas/WebGL -- ZERO acessibilidade")
    print("=" * 70)
    jogo <- e.registrar_app(
        pid <- 5678, nome="jogo", tipo=TipoApp.CANVAS_WEBGL,
        titulo <- "Jogo Online", tem_atspi=FALSO, tem_audio=VERDADEIRO,
        toolkit <- "canvas"
    )
    print(f"  Nivel nativo: {jogo.nivel_nat.rotulo}")
    adaptacoes_jogo <- e.ativar_adaptacao(jogo)
    print(f"\n  ADAPTACOES ATIVADAS ({len(adaptacoes_jogo)}):")
    para cada a em adaptacoes_jogo:
        print(f"    [{a.estrategia.id}] {a.estrategia.rotulo}")

    textos_jogo <- e.ocr_extrair_texto(jogo)
    print(f"\n  OCR BRIDGE (lendo a interface do jogo):")
    para cada t em textos_jogo:
        print(f"    -> \"{t}\"")

    // --- Cenario 3: App Wine ---
    print("\n" + "=" * 70)
    print("[CENARIO 3] App Windows via Wine -- sem acessibilidade no Linux")
    print("=" * 70)
    wine_app <- e.registrar_app(
        pid <- 9012, nome="photoshop_wine", tipo=TipoApp.WINE,
        titulo <- "Photoshop CS6 (Wine)", tem_atspi=FALSO,
        toolkit <- "wine"
    )
    print(f"  Nivel nativo: {wine_app.nivel_nat.rotulo}")
    adaptacoes_wine <- e.ativar_adaptacao(wine_app)
    print(f"\n  ADAPTACOES ATIVADAS ({len(adaptacoes_wine)}):")
    para cada a em adaptacoes_wine:
        print(f"    [{a.estrategia.id}] {a.estrategia.rotulo}")

    // --- Cenario 4: GTK (nativo, sem shim) ---
    print("\n" + "=" * 70)
    print("[CENARIO 4] GNOME Calculator (GTK) -- NATIVAMENTE acessivel")
    print("=" * 70)
    gtk_app <- e.registrar_app(
        pid <- 3456, nome="gnome-calculator", tipo=TipoApp.GTK,
        titulo <- "Calculadora", tem_atspi=VERDADEIRO, toolkit="gtk3"
    )
    print(f"  Nivel nativo: {gtk_app.nivel_nat.rotulo}")
    print(f"  Tem AT-SPI: {gtk_app.tem_atspi}")
    adaptacoes_gtk <- e.ativar_adaptacao(gtk_app)
    print(f"\n  ADAPTACOES ATIVADAS: {len(adaptacoes_gtk)}")
    se len(adaptacoes_gtk) == 0 entao:
        print(f"    -> NENHUMA. App ja e acessivel nativamente. Shim desnecessario.")

    // --- Relatorio ---
    print(f"\n[RELATORIO DE ADAPTACOES]")
    rel <- e.relatorio_adaptacoes()
    para cada (k, v) em rel.items():
        se isinstance(v, dict) entao:
            print(f"  {k}:")
            para cada (dk, dv) em v.items():
                print(f"    {dk:<20} {dv}")
        senao:
            print(f"  {k:.<28} {v}")

    // --- Scorecard ---
    print(f"\n[SCORECARD]")
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<28} {v}")

    // --- Fluxo tecnico ---
    print(f"\n[FLUXO TECNICO -- Como o Shim funciona]")
    print("""
  1. MONITOR DE JANELAS (atk-bridge / xdg-desktop-portal):
     Detecta cada janela aberta. Identifica PID, toolkit, titulo.
     Para cada app: verifica se tem arvore AT-SPI.

  2. CLASSIFICADOR DE ACESSIBILIDADE:
     GTK/Qt -> NATIVO (nao precisa shim)
     Electron -> PARCIAL (verifica o que falta)
     Canvas/Wine/Terminal cru -> NENHUM (precisa shim completo)

  3. MOTOR DE REGRAS:
     Cruza tipo do app + perfil do usuario + regras cadastradas.
     "App Canvas + usuario cego -> ativar OCR Bridge"
     "App Electron + usuario surdo -> ativar Caption Injection"

  4. OCR BRIDGE (Tesseract/PaddleOCR):
     a) Screenshot da janela (grim/kdump no Wayland, xwd no X11)
     b) OCR no screenshot -> extrai texto
     c) Texto exposto como arvore AT-SPI SINTETICA
     d) Orca le como se o app fosse acessivel
     Intervalo: 500ms (2x por segundo)

  5. CONTRASTE FORCADO (shader compositor):
     a) Wayland: wlroots compositor aplica shader na saida
     b) X11: xrandr gamma ou compositor (Picom)
     c) Inverte cores (dark mode forçado)
     d) Aumenta contraste (gamma adjust)
     e) Filtra para daltonismo (simulacao de daltonismo -> ajuste)
     Custo: quase zero (GPU faz via shader)

  6. CAPTION INJECTION (Whisper):
     a) Captura audio do app (PulseAudio: pavucontrol ou module-loopback)
     b) Whisper transcreve em tempo real
     c) Legenda exibida como overlay (layer-shell) por cima do app
     d) App nao sabe que tem legenda
     Custo: 20% CPU + 300MB RAM (Whisper base)

  7. INPUT INJECTION (xdotool/ydotool):
     a) VoiceOSControl manda: "clicar em enviar"
     b) Shim nao tem AT-SPI para clicar no botao
     c) OCR encontra "Enviar" na tela (coordenada X,Y)
     d) ydotool click X,Y (Wayland) ou xdotool (X11)
     e) O botao e clicado. O app responde.

  8. FOCUS RING (overlay):
     a) Detecta elemento focado (cursor pos ou OCR)
     b) Desenha borda colorida por cima (layer-shell overlay)
     c) Usuario VE onde o foco esta (mesmo em apps sem focus ring)
// )

    // --- Filosofia ---
    print(f"{'='*70}")
    print(f"FILOSOFIA -- O sistema COLOCA acessibilidade")
    print(f"{'='*70}")
    print("""
O PROBLEMA REAL:

  80% do software do mundo NAO e acessivel.
  - Apps Electron (Discord, Slack, VS Code): parcial.
  - Apps Java (IntelliJ, Android Studio): parcial.
  - Jogos (Canvas/WebGL): nenhum.
  - Apps Windows via Wine: nenhum no Linux.
  - Apps antigos (FLTK, Tk): minimo.
  - Sites com Canvas (Figma, Canva): nenhum.

  A Republica NAO pode esperar que todo desenvolvedor adicione AT-SPI.
  Isso levaria DECADAS. O cidadao precisa de acessibilidade AGORA.

A SOLUCAO: SHIM (adaptador)

  Um adaptador de tomada nao espera que a tomada mude.
  Ele ADAPTA o que existe para o que voce precisa.

  O OpenAccessibilityShim nao espera que o Discord adicione OCR.
  Ele LE a tela do Discord com OCR e expoe para o Orca.
  O Discord nao sabe. O Orca nao sabe. O usuario LE.

  O Shim nao espera que o jogo tenha legenda.
  Ele CAPTURA o audio do jogo e transcreve com Whisper.
  O jogo nao sabe. O usuario VE a legenda.

A METAFORA DO INTERPRETE:

  Um interprete de Libras traduz entre mundos.
  O surdo fala Libras. O ouvinte fala portugues.
  O interprete faz a ponte.

  O Shim e o INTERPRETE TECNICO.
  O app fala "canvas" (pixels sem significado).
  O Orca fala "AT-SPI" (arvore de acessibilidade).
  O Shim faz a ponte: pixels -> OCR -> AT-SPI sintetica.

OCR BRIDGE E A ARMA MAIS PODEROSA:

  OCR le QUALQUER tela. Qualquer app. Qualquer interface.
  Nao importa se e GTK, Electron, Canvas, Wine, ou terminal.
  OCR le pixels e extrai TEXTO. O Orca le o texto.

  Custo: 15% CPU, 300ms de latencia.
  Nao e perfeito (nao le icones sem texto, nao le cores).
  Mas e INFINITAMENTE melhor que ZERO acessibilidade.

O PRINCIPIO:

  Acessibilidade nao e responsabilidade so do desenvolvedor.
  E responsabilidade do SISTEMA.
  Se o app nao e acessivel, o sistema FAZ ser acessivel.
  Shim. OCR. Caption. Contraste. Input injection. Focus ring.

  O usuario nao escolhe apps acessiveis.
  O sistema TORNA todos os apps acessiveis.
// )


se __name__ == "__main__" entao:
    _demo()

```
