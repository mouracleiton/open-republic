# OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos do Corpo e da Civilizacao

**Arquivo original:** `open-republic/core/open_energy_taxonomy.py`

**Descricao:** ============================================================================
"Energia e a bateria do trabalho. Nada foi feito na Terra por humanos
sem a necessidade de energia."
O corpo humano nao tem UM sistema de energia. Tem DEZ.
Cada um com input, conversao, output e residuo.
A civilizacao herda essa estrutura.
OpenEnergy cobre o sistema 1 (eletrico = ATP).
Esta taxonomia revela os outros 9 -- e onde a Republica tem lacunas.
A LEI QUE PERMEIA TODOS OS 10:
  INPUT -> CONVERSAO -> OUTPUT -> RESIDUO
  Nada se cria. Tudo se transforma.
  Nao existe trabalho sem energia.
  Nao existe energia sem input.
  Nao existe output sem residuo.
OS 10 SISTEMAS:
  1. CELULAR (mitocondrial)  -- ATP, a moeda da celula
  2. MECANICA (muscular)     -- movimento, trabalho fisico
  3. TERMICA (metabolica)    -- calor, regulacao
  4. NEURAL (sinal)          -- sistema nervoso, comunicacao
  5. QUIMICA (sintese)       -- ligacoes, armazenamento molecular
  6. SENSORIAL (transducao)  -- receptores, captura ambiental
  7. COGNITIVA (processamento)-- cerebro, computacao
  8. ATENCIONAL (foco)       -- atencao finita, budget cognitivo
  9. EMOCIONAL (motivacao)   -- dopamina, drive, vontade
  10. RELACIONAL (social)    -- conexao, co-regulacao, sinergia
ALINHAMENTO CONSTITUCIONAL:
- P1: Cada tipo de energia e DIREITO. Nenhum e privilégio.
- P2: Autonomia corporal inclui autonomia ENERGETICA (todos os 10 tipos).
- P6: Acesso universal ao conhecimento = acesso a energia cognitiva/atencional.
- P8: IA amplifica energia cognitiva, NAO substitui. Protege atencao humana.
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos do Corpo e da Civilizacao
============================================================================
"Energia e a bateria do trabalho. Nada foi feito na Terra por humanos
sem a necessidade de energia."

O corpo humano nao tem UM sistema de energia. Tem DEZ.
Cada um com input, conversao, output e residuo.
A civilizacao herda essa estrutura.

OpenEnergy cobre o sistema 1 (eletrico = ATP).
Esta taxonomia revela os outros 9 -- e onde a Republica tem lacunas.

A LEI QUE PERMEIA TODOS OS 10:
  INPUT -> CONVERSAO -> OUTPUT -> RESIDUO
  Nada se cria. Tudo se transforma.
  Nao existe trabalho sem energia.
  Nao existe energia sem input.
  Nao existe output sem residuo.

OS 10 SISTEMAS:
  1. CELULAR (mitocondrial)  -- ATP, a moeda da celula
  2. MECANICA (muscular)     -- movimento, trabalho fisico
  3. TERMICA (metabolica)    -- calor, regulacao
  4. NEURAL (sinal)          -- sistema nervoso, comunicacao
  5. QUIMICA (sintese)       -- ligacoes, armazenamento molecular
  6. SENSORIAL (transducao)  -- receptores, captura ambiental
  7. COGNITIVA (processamento)-- cerebro, computacao
  8. ATENCIONAL (foco)       -- atencao finita, budget cognitivo
  9. EMOCIONAL (motivacao)   -- dopamina, drive, vontade
  10. RELACIONAL (social)    -- conexao, co-regulacao, sinergia

ALINHAMENTO CONSTITUCIONAL:
- P1: Cada tipo de energia e DIREITO. Nenhum e privilégio.
- P2: Autonomia corporal inclui autonomia ENERGETICA (todos os 10 tipos).
- P6: Acesso universal ao conhecimento = acesso a energia cognitiva/atencional.
- P8: IA amplifica energia cognitiva, NAO substitui. Protege atencao humana.

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. ENUMS (modulo-level)
// ============================================================================

classe TipoEnergia herda de Enum:
    // Os 10 sistemas energeticos do corpo e da civilizacao.
    CELULAR <- ("celular", "Energia Celular (mitocondrial)", 1)
    MECANICA <- ("mecanica", "Energia Mecanica (muscular)", 2)
    TERMICA <- ("termica", "Energia Termica (metabolica)", 3)
    NEURAL <- ("neural", "Energia Neural (sinal)", 4)
    QUIMICA <- ("quimica", "Energia Quimica (sintese)", 5)
    SENSORIAL <- ("sensorial", "Energia Sensorial (transducao)", 6)
    COGNITIVA <- ("cognitiva", "Energia Cognitiva (processamento)", 7)
    ATENCIONAL <- ("atencional", "Energia Atencional (foco)", 8)
    EMOCIONAL <- ("emocional", "Energia Emocional (motivacao)", 9)
    RELACIONAL <- ("relacional", "Energia Relacional (social)", 10)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao numero(self) retorna int:
        retorne self.value[2]


classe EscalaEnergia herda de Enum:
    // Em que nivel esta energia opera.
    CORPO <- ("corpo", "Nivel do corpo individual")
    COMUNIDADE <- ("comunidade", "Nivel da comunidade/local")
    CIVILIZACAO <- ("civilizacao", "Nivel da civilizacao/global")
    PLANETA <- ("planeta", "Nivel planetario/biosfera")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe StatusDisponibilidade herda de Enum:
    // Disponibilidade/estoque de um tipo de energia.
    ABUNDANTE <- ("abundante", "Abundante: excedente para doar")
    EQUILIBRADA <- ("equilibrada", "Equilibrada: cobre a demanda")
    LIMITADA <- ("limitada", "Limitada: alocacao necessaria")
    CRITICA <- ("critica", "Critica: deficit, intervene")
    DEPLETADA <- ("depletada", "Depletada: esgotada, recuperacao obrigatoria")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe NivelCobertura herda de Enum:
    // Quanto da Republica cobre este tipo de energia.
    COBERTO <- ("coberto", "Totalmente coberto por modulo(s) existente(s)")
    PARCIAL <- ("parcial", "Parcialmente coberto -- lacunas identificadas")
    LACUNA <- ("lacuna", "Lacuna: nenhum modulo cobre este tipo")
    NAO_APLICAVEL <- ("nao_aplicavel", "Nao aplicavel (conceitual)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe TipoInput herda de Enum:
    // Categorias de input energetico (o que alimenta cada sistema).
    ALIMENTO <- ("alimento", "Alimento/caloria (comida, combustivel)")
    OXIGENIO <- ("oxigenio", "Oxigenio/ar")
    LUZ <- ("luz", "Luz/fotons")
    SOM <- ("som", "Som/vibracao")
    CALOR_AMBIENTE <- ("calor", "Calor ambiental")
    PRESENCA <- ("presenca", "Presenca de outro ser humano")
    INFORMACAO <- ("informacao", "Informacao/dados")
    SONO <- ("sono", "Sono/descanso")
    MOVIMENTO_CORPO <- ("movimento", "Movimento do proprio corpo")
    VENTO_AGUA <- ("vento_agua", "Vento, agua, forcas naturais")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe TipoResiduo herda de Enum:
    // O que cada sistema energetico produz como residuo (2a lei).
    CALOR <- ("calor", "Calor dissipado")
    CO2 <- ("co2", "CO2 / gases de exaustao")
    CANSACO_FISICO <- ("cansaco_fisico", "Cansaco fisico / acido latico")
    FADIGA_MENTAL <- ("fadiga_mental", "Fadiga mental / saturacao")
    DESGASTE_MATERIAL <- ("desgaste", "Desgaste material (atriito, envelhecimento)")
    RUIDO <- ("ruido", "Ruido (sonoro, visual, informational)")
    SOLIDAO <- ("solidao", "Solidao (quando a conexao termina)")
    RESIDUO_TOXICO <- ("residuo_toxico", "Residuo toxico (quimico, radiativo)")
    DADOS_DESCARTADOS <- ("dados_descartados", "Dados descartados (log, cache)")

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
classe FluxoEnergetico:
    // Estrutura universal: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO.
    declare inputs: List[TipoInput]  <- field(default_factory=list)
    declare conversao: str  <- ""  // como se converte input em output
    declare output: str  <- ""  // o que o sistema PRODUZ
    declare residuos: List[TipoResiduo]  <- field(default_factory=list)
    declare eficiencia_pct: float  <- 100.0  // % do input que vira output util


// decorador: @dataclass
classe SistemaEnergetico:
    // Um dos 10 sistemas de energia, com mapeamento corpo <-> civilizacao.
    tipo: TipoEnergia
    nome: str
    analogia_corpo: str         // como funciona no corpo humano
    analogia_civilizacao: str   // como funciona na civilizacao
    escala: EscalaEnergia
    declare fluxo: FluxoEnergetico  <- field(default_factory=FluxoEnergetico)
    declare consumo_corpo_pct: float  <- 0.0  // % do orcamanto energetico do corpo (se aplicavel)
    declare observacao: str  <- ""


// decorador: @dataclass
classe CoberturaRepublica:
    // Quais modulos da Republica cobrem cada tipo de energia.
    tipo: TipoEnergia
    nivel: NivelCobertura
    declare modulos: List[str]  <- field(default_factory=list)  // modulos que cobrem
    declare lacunas: List[str]  <- field(default_factory=list)  // o que falta


// decorador: @dataclass
classe DiagnosticoEnergetico:
    // Snapshot da saude energetica de uma pessoa ou comunidade.
    entidade: str   // "pessoa:Maria" ou "comunidade:Solar Village"
    declare status_por_tipo: Dict[str, StatusDisponibilidade]  <- field(default_factory=dict)
    declare tipos_em_deficit: List[TipoEnergia]  <- field(default_factory=list)
    declare tipos_abundantes: List[TipoEnergia]  <- field(default_factory=list)
    declare veredito: str  <- ""


// ============================================================================
// 3. OS 10 SISTEMAS (dados canonicos)
// ============================================================================

funcao _init_sistemas() retorna List[SistemaEnergetico]:
    // Cria os 10 sistemas energeticos com dados completos.
    retorne [
        SistemaEnergetico(
            tipo <- TipoEnergia.CELULAR,
            nome <- "Mitocondrial",
            analogia_corpo <- (
                "Mitocondrias convertem glicose + oxigenio em ATP. "
                "ATP e a MOEDA energetica da celula -- todo trabalho "
                "celular paga em ATP. Sem ATP, a celula morre em segundos."
            ),
            analogia_civilizacao <- (
                "A rede eletrica. A tomada e o ATP da civilizacao. "
                "Todo aparelho, toda maquina, todo servo consome eletricidade. "
                "OpenEnergy cobre este sistema."
            ),
            escala <- EscalaEnergia.CIVILIZACAO,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.ALIMENTO, TipoInput.OXIGENIO],
                conversao <- "Glicose + O2 -> ATP (fosforilacao oxidativa)",
                output <- "ATP (trifosfato de adenosina) / Eletricidade",
                residuos <- [TipoResiduo.CO2, TipoResiduo.CALOR],
                eficiencia_pct <- 40.0,
            ),
            consumo_corpo_pct <- 0.0,
            observacao <- (
                "Sistema base. Todos os outros dependem deste. "
                "OpenEnergy = cobertura total deste nivel."
            ),
        ),
        SistemaEnergetico(
            tipo <- TipoEnergia.MECANICA,
            nome <- "Muscular / Motora",
            analogia_corpo <- (
                "ATP -> miosina/actina -> contracao muscular -> MOVIMENTO. "
                "O corpo faz TRABALHO FISICO sobre o mundo. "
                "Cada passo, cada gesto, cada levantamento de peso."
            ),
            analogia_civilizacao <- (
                "Transporte, maquinas, ferramentas, robos. "
                "O motor de carro, o braco robotico, a bicicleta. "
                "Todo trabalho fisico ja existiu como energia muscular "
                "antes de ser externalizado para maquinas."
            ),
            escala <- EscalaEnergia.CIVILIZACAO,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.ALIMENTO, TipoInput.MOVIMENTO_CORPO],
                conversao <- "ATP -> forca mecanica (contracao / combustao / eletricidade)",
                output <- "Movimento, forca, deslocamento",
                residuos <- [TipoResiduo.CANSACO_FISICO, TipoResiduo.CALOR, TipoResiduo.CO2],
                eficiencia_pct <- 25.0,
            ),
            consumo_corpo_pct <- 30.0,
            observacao <- (
                "OpenAthlete cobre o lado humano (esporte, treino). "
                "Transporte publico (OpenMobility) cobre o lado civilizacional."
            ),
        ),
        SistemaEnergetico(
            tipo <- TipoEnergia.TERMICA,
            nome <- "Metabolica / Calorica",
            analogia_corpo <- (
                "O metabolismo produz calor como subproduto. "
                "O corpo GASTA energia mantendo 36,5C -- termorregulacao. "
                "Tremer de frio e gerar calor muscular. Suar e dissipar."
            ),
            analogia_civilizacao <- (
                "Aquecimento, cozimento, refrigeracao. "
                "O FOGO foi a primeira energia externa que o humano dominou "
                "(1 milhao de anos antes da eletricidade). "
                "Cozinhar e PRE-DIGERIR com energia termica externa "
                "-- libera energia celular que iria pra digestao."
            ),
            escala <- EscalaEnergia.CIVILIZACAO,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.ALIMENTO, TipoInput.CALOR_AMBIENTE],
                conversao <- "Metabolismo / combustao / compressao -> calor",
                output <- "Calor (manutencao de temperatura / cozimento)",
                residuos <- [TipoResiduo.CALOR, TipoResiduo.CO2],
                eficiencia_pct <- 60.0,
            ),
            consumo_corpo_pct <- 50.0,
            observacao <- (
                "Metabolismo basal: 50% do gasto energetico do corpo em repouso "
                "e so para manter a temperatura. O cozimento de alimentos "
                "foi a REVOLUCAO ENERGETICA original da humanidade."
            ),
        ),
        SistemaEnergetico(
            tipo <- TipoEnergia.NEURAL,
            nome <- "Sistema Nervoso / Comunicacao",
            analogia_corpo <- (
                "Neuronios disparam potenciais de acao -- sinais eletricos. "
                "O corpo tem uma REDE de comunicacao interna (87 bilhoes de neuronios). "
                "Consome 20W, incrivelmente eficiente. "
                "O cerebro pesa 2% do corpo mas consome 20% da energia."
            ),
            analogia_civilizacao <- (
                "Internet, telecomunicacoes, radio. "
                "A internet e o SISTEMA NERVO da civilizacao. "
                "Cada mensagem, cada video, cada chamada e um potencial de acao "
                "em escala planetaria. Banda = largura de axonio."
            ),
            escala <- EscalaEnergia.PLANETA,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.INFORMACAO, TipoInput.LUZ],
                conversao <- "Sinal eletrico / optico -> transmissao",
                output <- "Comunicacao / sinal / dados transmitidos",
                residuos <- [TipoResiduo.RUIDO, TipoResiduo.CALOR, TipoResiduo.DADOS_DESCARTADOS],
                eficiencia_pct <- 35.0,
            ),
            consumo_corpo_pct <- 20.0,
            observacao <- (
                "LACUNA CRITICA: a Republica NAO tem OpenNetwork/OpenInternet. "
                "Quem controla a rede controla o sistema nervoso. "
                "Banda gratuita e NECESSARIA (energia neural = direito)."
            ),
        ),
        SistemaEnergetico(
            tipo <- TipoEnergia.QUIMICA,
            nome <- "Sintese / Ligacoes",
            analogia_corpo <- (
                "O corpo SINTETIZA moleculas -- proteinas, hormonios, enzimas. "
                "Ligacoes quimicas ARMAZENAM energia. "
                "Digestao = quebrar ligacoes para liberar. "
                "Sintese = gastar energia para construir."
            ),
            analogia_civilizacao <- (
                "Industria quimica, baterias, combustiveis, farmacia. "
                "Toda manufatura e energia quimica direcionada. "
                "FarmLab opera aqui -- sintese de medicamentos e energia "
                "quimica a servico da vida."
            ),
            escala <- EscalaEnergia.CIVILIZACAO,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.ALIMENTO],
                conversao <- "Reacao quimica (sintese / decomposicao)",
                output <- "Moleculas / materiais / medicamentos",
                residuos <- [TipoResiduo.RESIDUO_TOXICO, TipoResiduo.CALOR],
                eficiencia_pct <- 30.0,
            ),
            consumo_corpo_pct <- 10.0,
            observacao <- "FarmLab cobre farmacia. OpenChemistry cobre industria quimica.",
        ),
        SistemaEnergetico(
            tipo <- TipoEnergia.SENSORIAL,
            nome <- "Transducao / Percepcao",
            analogia_corpo <- (
                "Olhos capturam FOTONS. Ouvidos capturam VIBRACOES. "
                "Pele captura CALOR. O corpo e um RECEPTOR de energia -- "
                "converte formas externas em sinais internos. "
                "Cada sentido e um TRANSDUTOR energetico."
            ),
            analogia_civilizacao <- (
                "Cameras, microfones, sensores, instrumentos cientificos. "
                "OpenTelefonista opera aqui -- o smartphone como CORPO ESTENDIDO "
                "captura energia do ambiente (luz, som, posicao) e converte "
                "em percepcao. Cego ve obstaculos. Surdo le labios."
            ),
            escala <- EscalaEnergia.CORPO,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.LUZ, TipoInput.SOM, TipoInput.CALOR_AMBIENTE],
                conversao <- "Transducao sensorial (foton/fonon -> sinal neural)",
                output <- "Percepcao / dados sensoriais",
                residuos <- [TipoResiduo.RUIDO, TipoResiduo.FADIGA_MENTAL],
                eficiencia_pct <- 70.0,
            ),
            consumo_corpo_pct <- 5.0,
            observacao <- (
                "OpenTelefonista cobre (smartphone como corpo estendido). "
                "OpenInclusiveHardware (44 dispositivos) amplia. "
                "OpenInclusiveIDE integra para desenvolvimento."
            ),
        ),
        SistemaEnergetico(
            tipo <- TipoEnergia.COGNITIVA,
            nome <- "Cerebro / Processamento",
            analogia_corpo <- (
                "O cerebro CONSOME 20% da energia do corpo pesando 2%. "
                "PENSAR E CARO energeticamente. O cansaco mental e real -- "
                "e gasto energetico, nao frescura. "
                "Resolver um problema matematico gasta mais glicose "
                "que assistir TV."
            ),
            analogia_civilizacao <- (
                "Computacao, IA, analise de dados. "
                "Um data center consome tanta energia quanto uma cidade. "
                "Processar informacao TEM CUSTO ENERGETICO -- nao e gratuito. "
                "P8: IA amplifica inteligencia humana, NAO substitui. "
                "Mas o custo de computar e REAL e precisa alocacao."
            ),
            escala <- EscalaEnergia.CIVILIZACAO,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.INFORMACAO, TipoInput.ALIMENTO],
                conversao <- "Processamento (neural / digital)",
                output <- "Decisao / calculo / conhecimento",
                residuos <- [TipoResiduo.FADIGA_MENTAL, TipoResiduo.CALOR, TipoResiduo.DADOS_DESCARTADOS],
                eficiencia_pct <- 15.0,
            ),
            consumo_corpo_pct <- 20.0,
            observacao <- (
                "HumanKnowledge (multi-AI + verificacao) cobre parcialmente. "
                "P8 define o principio (IA = instrumento). "
                "Custo computacional como recurso a alocar = LACUNA."
            ),
        ),
        SistemaEnergetico(
            tipo <- TipoEnergia.ATENCIONAL,
            nome <- "Foco / Atencao",
            analogia_corpo <- (
                "A atencao e FINITA. Voce nao consegue focar em tudo. "
                "Focar GASTA energia cognitiva. "
                "O cerebro tem um BUDGET de atencao -- distribui entre tarefas. "
                "Dormir mal = budget de atencao menor no dia seguinte."
            ),
            analogia_civilizacao <- (
                "A energia que FocusGuard protege. "
                "O scroll infinito DRENA energia atencional. "
                "A 'economia da atencao' e a forma mais NOVA de exploracao "
                "energetica -- plataformas capturam sua atencao e vendem. "
                "P8 exige proteger esta energia. AntiSpamCall protege parcialmente."
            ),
            escala <- EscalaEnergia.CORPO,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.SONO, TipoInput.INFORMACAO],
                conversao <- "Filtro atencional (top-down + bottom-up)",
                output <- "Foco / atencao direcionada",
                residuos <- [TipoResiduo.FADIGA_MENTAL, TipoResiduo.RUIDO],
                eficiencia_pct <- 10.0,
            ),
            consumo_corpo_pct <- 0.0,
            observacao <- (
                "FocusGuard (overlay IDE) cobre parcialmente. "
                "AntiSpamCall ('para de me encher o saco') protege. "
                "OpenContentPolicy (midia, ruido) protege. "
                "Politica mais ampla de atencao como recurso = LACUNA."
            ),
        ),
        SistemaEnergetico(
            tipo <- TipoEnergia.EMOCIONAL,
            nome <- "Motivacao / Drive",
            analogia_corpo <- (
                "Motivacao, drive, vontade. Em termos fisicos: dopamina, "
                "noradrenalina, cortisol -- moleculas que MODULAM quanto "
                "de outras energias o corpo vai despender. "
                "Sem dopamina, o corpo tem ATP mas nao se MOVE. "
                "A depressao e crise energetica emocional -- o combustivel "
                "existe, mas o motor nao liga."
            ),
            analogia_civilizacao <- (
                "O kaizen (1% ao dia) opera aqui. "
                "Curiosidade, progresso, desafio, recompensa, pertencimento -- "
                "os 5 gatilhos psicologicos sao GERADORES de energia emocional. "
                "O Huxley soma (dopamina artificial do scroll) e o SEQUESTRO "
                "desta energia -- drena ao inves de gerar."
            ),
            escala <- EscalaEnergia.COMUNIDADE,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.PRESENCA, TipoInput.SONO, TipoInput.INFORMACAO],
                conversao <- "Modulacao neuroquimica (dopamina/serotonina/cortisol)",
                output <- "Motivacao / drive / vontade de agir",
                residuos <- [TipoResiduo.SOLIDAO, TipoResiduo.FADIGA_MENTAL],
                eficiencia_pct <- 20.0,
            ),
            consumo_corpo_pct <- 0.0,
            observacao <- (
                "LACUNA CRITICA: nenhum modulo trata saude mental como "
                "INFRAESTRUTURA ENERGETICA. Depressao = deficit energetico. "
                "Burnout = deplecao. Kaizen e gerador, mas falta sistema."
            ),
        ),
        SistemaEnergetico(
            tipo <- TipoEnergia.RELACIONAL,
            nome <- "Social / Conexao",
            analogia_corpo <- (
                "O ser humano isolado DEGRADA. Solidao cronica aumenta "
                "mortalidade em 26%. O corpo PRECISA de conexao para "
                "funcionar bem -- nao e luxo, e necessidade energetica. "
                "Oxitocina, espelhamento neural, co-regulacao."
            ),
            analogia_civilizacao <- (
                "A assembleia, o mutirao, a cooperativa. "
                "O Two-Person Rule nao e so procedimento -- e ARQUITETURA "
                "ENERGETICA. Duas pessoas juntas fazem mais que duas separadas. "
                "A energia social e SINERGICA: 1+1 > 2. "
                "Quando a assembleia polariza (P9), e esta energia que se "
                "GASTA em atrito em vez de gerar valor."
            ),
            escala <- EscalaEnergia.COMUNIDADE,
            fluxo <- FluxoEnergetico(
                inputs <- [TipoInput.PRESENCA],
                conversao <- "Co-regulacao neuroquimica + espelhamento neural",
                output <- "Cooperacao / sinergia / vinculo",
                residuos <- [TipoResiduo.SOLIDAO],
                eficiencia_pct <- 80.0,
            ),
            consumo_corpo_pct <- 0.0,
            observacao <- (
                "OpenCommunities (6 adaptacoes) cobre parcialmente. "
                "OpenConstituentAssembly (governanca) cobre parcialmente. "
                "OpenCrowdsourcing (ajuda mutua) cobre parcialmente. "
                "P9 (anti-polarizacao) PROTEGE esta energia. "
                "Tratar conexao como recurso energetico mensuravel = LACUNA."
            ),
        ),
    ]


funcao _init_coberturas() retorna List[CoberturaRepublica]:
    // Mapeia quais modulos cobrem cada tipo de energia.
    retorne [
        CoberturaRepublica(
            tipo <- TipoEnergia.CELULAR,
            nivel <- NivelCobertura.COBERTO,
            modulos <- ["open-energy", "open-agrarian-revolution", "open-credit"],
            lacunas <- [],
        ),
        CoberturaRepublica(
            tipo <- TipoEnergia.MECANICA,
            nivel <- NivelCobertura.PARCIAL,
            modulos <- ["open-athlete", "open-martial-arts"],
            lacunas <- ["sistema de transporte publico gratuito (OpenMobility)"],
        ),
        CoberturaRepublica(
            tipo <- TipoEnergia.TERMICA,
            nivel <- NivelCobertura.PARCIAL,
            modulos <- ["open-energy"],
            lacunas <- ["politica de cozimento comunitario", "aquecimento como direito"],
        ),
        CoberturaRepublica(
            tipo <- TipoEnergia.NEURAL,
            nivel <- NivelCobertura.LACUNA,
            modulos <- [],
            lacunas <- [
                "OpenNetwork/OpenInternet -- banda gratuita como direito",
                "sistema nervoso da civilizacao sem dono",
                "neutralidade de rede como P1 (anti-elitismo)",
            ],
        ),
        CoberturaRepublica(
            tipo <- TipoEnergia.QUIMICA,
            nivel <- NivelCobertura.PARCIAL,
            modulos <- ["open-chemistry", "open-physics"],
            lacunas <- ["FarmLab completo (sintese CC0 de medicamentos)"],
        ),
        CoberturaRepublica(
            tipo <- TipoEnergia.SENSORIAL,
            nivel <- NivelCobertura.COBERTO,
            modulos <- ["open-telefonista", "open-inclusive-hardware", "open-inclusive-ide"],
            lacunas <- [],
        ),
        CoberturaRepublica(
            tipo <- TipoEnergia.COGNITIVA,
            nivel <- NivelCobertura.PARCIAL,
            modulos <- ["open-human-knowledge", "open-human-amplification"],
            lacunas <- ["alocacao de custo computacional como recurso energetico"],
        ),
        CoberturaRepublica(
            tipo <- TipoEnergia.ATENCIONAL,
            nivel <- NivelCobertura.PARCIAL,
            modulos <- ["open-focus-guard", "open-anti-spam-call", "open-content-policy"],
            lacunas <- ["politica ampla de atencao como recurso energetico finito"],
        ),
        CoberturaRepublica(
            tipo <- TipoEnergia.EMOCIONAL,
            nivel <- NivelCobertura.LACUNA,
            modulos <- [],
            lacunas <- [
                "OpenMentalHealth -- saude mental como INFRAESTRUTURA ENERGETICA",
                "sistema de deteccao de deplecao emocional (burnout/depressao)",
                "geradores de energia emocional (kaizen, pertencimento, proposito)",
            ],
        ),
        CoberturaRepublica(
            tipo <- TipoEnergia.RELACIONAL,
            nivel <- NivelCobertura.PARCIAL,
            modulos <- ["open-communities", "open-constituent-assembly", "open-anti-polarization"],
            lacunas <- ["conexao como recurso energetico mensuravel e protegido"],
        ),
    ]


// ============================================================================
// 4. ENGINE
// ============================================================================

classe EnergyTaxonomyEngine:
    // Motor da Taxonomia Energetica: os 10 sistemas, coberturas, diagnosticos.

    funcao __init__(self) retorna None:
        self.sistemas: List[SistemaEnergetico] = _init_sistemas()
        self.coberturas: List[CoberturaRepublica] = _init_coberturas()
        self.diagnosticos: Dict[str, DiagnosticoEnergetico] = {}

    // -- consulta ----------------------------------------------------------

    funcao listar_sistemas(self) retorna List[SistemaEnergetico]:
        retorne sorted(self.sistemas, key=funcao anonima(s): s.tipo.numero)

    funcao sistema_por_tipo(self, tipo: TipoEnergia) retorna Optional[SistemaEnergetico]:
        para cada s em self.sistemas:
            se s.tipo == tipo entao:
                retorne s
        retorne nulo

    funcao coberturas_por_nivel(self, nivel: NivelCobertura) retorna List[CoberturaRepublica]:
        retorne [c for c in self.coberturas if c.nivel == nivel]

    funcao lacunas_identificadas(self) retorna List[Tuple[TipoEnergia, List[str]]]:
        // Retorna tipos com lacunas e o que falta.
        retorne [
            (c.tipo, c.lacunas)
            for c in self.coberturas
            if c.nivel in (NivelCobertura.LACUNA, NivelCobertura.PARCIAL)
        ]

    // -- diagnostico -------------------------------------------------------

    def diagnosticar(
        self,
        entidade: str,
        status: Dict[TipoEnergia, StatusDisponibilidade],
    ) -> DiagnosticoEnergetico:
        // Produz diagnostico energetico de uma pessoa ou comunidade.
        status_por_id <- {t.id: s for t, s in status.items()}
        em_deficit <- [t for t, s in status.items()
                      if s in (StatusDisponibilidade.LIMITADA,
                               StatusDisponibilidade.CRITICA,
                               StatusDisponibilidade.DEPLETADA)]
        abundantes <- [t for t, s in status.items()
                      if s <- = StatusDisponibilidade.ABUNDANTE]
        se len(em_deficit) >= 4 entao:
            veredito <- "CRITICO: multiplas deficiencias energeticas. Intervencao sistêmica."
        senao se len(em_deficit) >= 2 entao:
            veredito <- "ATENCAO: deficiencias energeticas em sistemas chave."
        senao se em_deficit entao:
            nomes <- ", ".join(t.rotulo.split("(")[0].strip() for t in em_deficit)
            veredito <- f"DEFICIT LOCAL: {nomes}. Tratar antes de propagar."
        senao:
            veredito <- "SAUDAVEL: todos os sistemas energeticos em equilibrio ou abundancia."
        diag <- DiagnosticoEnergetico(
            entidade <- entidade,
            status_por_tipo <- status_por_id,
            tipos_em_deficit <- em_deficit,
            tipos_abundantes <- abundantes,
            veredito <- veredito,
        )
        self.diagnosticos[entidade] = diag
        retorne diag

    // -- padrao universal --------------------------------------------------

    funcao padrao_universal(self) retorna str:
        // A lei que permeia todos os 10 sistemas.
        retorne (
            "PADRAO UNIVERSAL: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO\n"
            "Nada se cria. Tudo se transforma.\n"
            "Nao existe trabalho sem energia.\n"
            "Nao existe energia sem input.\n"
            "Nao existe output sem residuo.\n"
            "A questao civilizatoria nunca foi 'como conseguir energia' "
            "-- sempre foi 'como TRANSFORMAR com justica e sem desperdicar'."
        )

    // -- scorecard ---------------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        total <- len(self.sistemas)
        cobertos <- len(self.coberturas_por_nivel(NivelCobertura.COBERTO))
        parciais <- len(self.coberturas_por_nivel(NivelCobertura.PARCIAL))
        lacunas <- len(self.coberturas_por_nivel(NivelCobertura.LACUNA))
        total_lacunas_itens <- sum(len(c.lacunas) for c in self.coberturas)
        pct_coberto <- round(cobertos / total * 100, 1) if total else 0.0
        retorne {
            "sistemas_total": total,
            "totalmente_cobertos": cobertos,
            "parcialmente_cobertos": parciais,
            "lacunas_criticas": lacunas,
            "itens_faltantes": total_lacunas_itens,
            "pct_cobertura": pct_coberto,
            "diagnosticos_realizados": len(self.diagnosticos),
        }


// ============================================================================
// 5. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- EnergyTaxonomyEngine()

    print("=" * 70)
    print("OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos")
    print("Do Corpo Humano a Civilizacao")
    print("=" * 70)

    // --- Os 10 sistemas ---
    print("\n[OS 10 SISTEMAS ENERGETICOS]")
    para cada s em e.listar_sistemas():
        print(f"\n  --- Sistema {s.tipo.numero}: {s.tipo.rotulo} ---")
        print(f"  Escala: {s.escala.rotulo}")
        print(f"  CORPO: {s.analogia_corpo}")
        print(f"  CIVILIZACAO: {s.analogia_civilizacao}")
        se s.consumo_corpo_pct > 0 entao:
            print(f"  Consumo no corpo: {s.consumo_corpo_pct}% do orcamento energetico")
        f <- s.fluxo
        print(f"  FLUXO: {[i.rotulo for i in f.inputs]} -> {f.conversao}")
        print(f"         -> {f.output}")
        print(f"         -> RESIDUO: {[r.rotulo for r in f.residuos]}")
        print(f"  EFICIENCIA: {f.eficiencia_pct}%")
        se s.observacao entao:
            print(f"  OBS: {s.observacao}")

    // --- Padrao universal ---
    print("\n" + "=" * 70)
    print("[O PADRAO UNIVERSAL]")
    print("=" * 70)
    print(f"\n{e.padrao_universal()}")

    // --- Exemplo: cada sistema em uma linha ---
    print("\n[EXEMPLOS CORPO -> CIVILIZACAO]")
    para cada s em e.listar_sistemas():
        corpo_curto <- s.analogia_corpo.split(".")[0].strip()
        civ_curto <- s.analogia_civilizacao.split(".")[0].strip()
        print(f"  {s.tipo.numero:2d}. {s.tipo.rotulo}")
        print(f"      Corpo: {corpo_curto}")
        print(f"      Civil: {civ_curto}")

    // --- Cobertura da Republica ---
    print("\n" + "=" * 70)
    print("[COBERTURA DA REPUBLICA -- O QUE FALTA]")
    print("=" * 70)
    para cada c em e.coberturas:
        flag <- {"coberto": "OK", "parcial": "PARCIAL", "lacuna": "LACUNA",
                "nao_aplicavel": "N/A"}[c.nivel.id]
        print(f"\n  [{flag}] {c.tipo.rotulo}")
        se c.modulos entao:
            print(f"  Modulos: {', '.join(c.modulos)}")
        se c.lacunas entao:
            print(f"  LACUNAS:")
            para cada lac em c.lacunas:
                print(f"    - {lac}")

    // --- Lacunas criticas ---
    print("\n" + "=" * 70)
    print("[LACUNAS CRITICAS -- MODULOS QUE PRECISAM EXISTIR]")
    print("=" * 70)
    lacunas <- e.coberturas_por_nivel(NivelCobertura.LACUNA)
    para cada c em lacunas:
        print(f"\n  {c.tipo.rotulo}:")
        para cada lac em c.lacunas:
            print(f"    - {lac}")
    se NAO  lacunas entao:
        print("  (nenhuma lacuna critica)")

    // --- Diagnostico de exemplo ---
    print("\n" + "=" * 70)
    print("[DIAGNOSTICO ENERGETICO -- Pessoa: Maria]")
    print("=" * 70)
    diag_maria <- e.diagnosticar("pessoa:Maria", {
        TipoEnergia.CELULAR: StatusDisponibilidade.EQUILIBRADA,
        TipoEnergia.MECANICA: StatusDisponibilidade.EQUILIBRADA,
        TipoEnergia.TERMICA: StatusDisponibilidade.ABUNDANTE,
        TipoEnergia.NEURAL: StatusDisponibilidade.ABUNDANTE,
        TipoEnergia.QUIMICA: StatusDisponibilidade.EQUILIBRADA,
        TipoEnergia.SENSORIAL: StatusDisponibilidade.EQUILIBRADA,
        TipoEnergia.COGNITIVA: StatusDisponibilidade.LIMITADA,
        TipoEnergia.ATENCIONAL: StatusDisponibilidade.CRITICA,
        TipoEnergia.EMOCIONAL: StatusDisponibilidade.DEPLETADA,
        TipoEnergia.RELACIONAL: StatusDisponibilidade.EQUILIBRADA,
    })
    print(f"  Entidade: {diag_maria.entidade}")
    para cada (tid, st) em sorted(diag_maria.status_por_tipo.items()):
        print(f"    {tid:.<20} {st}")
    print(f"  Em deficit: {[t.rotulo.split('(')[0].strip() for t in diag_maria.tipos_em_deficit]}")
    print(f"  Abundantes: {[t.rotulo.split('(')[0].strip() for t in diag_maria.tipos_abundantes]}")
    print(f"  VEREDITO: {diag_maria.veredito}")

    // --- Diagnostico: comunidade ---
    print("\n[DIAGNOSTICO ENERGETICO -- Comunidade: Solar Village]")
    diag_sv <- e.diagnosticar("comunidade:solar_village", {
        TipoEnergia.CELULAR: StatusDisponibilidade.ABUNDANTE,
        TipoEnergia.MECANICA: StatusDisponibilidade.EQUILIBRADA,
        TipoEnergia.TERMICA: StatusDisponibilidade.ABUNDANTE,
        TipoEnergia.NEURAL: StatusDisponibilidade.LIMITADA,
        TipoEnergia.QUIMICA: StatusDisponibilidade.EQUILIBRADA,
        TipoEnergia.SENSORIAL: StatusDisponibilidade.EQUILIBRADA,
        TipoEnergia.COGNITIVA: StatusDisponibilidade.EQUILIBRADA,
        TipoEnergia.ATENCIONAL: StatusDisponibilidade.EQUILIBRADA,
        TipoEnergia.EMOCIONAL: StatusDisponibilidade.ABUNDANTE,
        TipoEnergia.RELACIONAL: StatusDisponibilidade.ABUNDANTE,
    })
    print(f"  Entidade: {diag_sv.entidade}")
    print(f"  Em deficit: {[t.rotulo.split('(')[0].strip() for t in diag_sv.tipos_em_deficit]}")
    print(f"  Abundantes: {[t.rotulo.split('(')[0].strip() for t in diag_sv.tipos_abundantes]}")
    print(f"  VEREDITO: {diag_sv.veredito}")

    // --- Scorecard ---
    print("\n" + "=" * 70)
    print("[SCORECARD DA TAXONOMIA ENERGETICA]")
    print("=" * 70)
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<28} {v}")

    // --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Energia e a bateria do trabalho")
    print("=" * 70)
    print("""
'Energia e a bateria do trabalho. Nosso corpo so funciona porque
temos energia. Nada foi feito na Terra por humanos sem a necessidade
de energia.'

O corpo humano nao tem UM sistema de energia. Tem DEZ.
Cada um com input, conversao, output e residuo.
A civilizacao herda essa estrutura -- somos um corpo em escala.

OpenEnergy cobre o sistema 1 (eletrico = ATP).
Mas existem outros 9 que a Republica precisa tratar:

NEURAL (sistema nervoso = internet):
  Quem controla a rede controla o sistema nervoso da civilizacao.
  Banda gratuita e NECESSARIA. A internet e o nervo. Sem nervo, paralisia.

COGNITIVA (cerebro = computacao):
  Processar informacao TEM CUSTO ENERGETICO. IA nao e gratuita.
  P8 exige que esse custo seja alocado democraticamente, nao por dinheiro.

ATENCIONAL (foco = atencao finita):
  A atencao e o recurso mais explorado do seculo XXI.
  Plataformas capturam sua atencao e vendem. Isso e EXTRATIVISMO ENERGETICO.
  FocusGuard e o comeco. Proteger atencao = proteger energia.

EMOCIONAL (motivacao = drive):
  Depressao e CRISE ENERGETICA. O combustivel existe (ATP), mas o motor
  nao liga (sem dopamina). Saude mental nao e luxo terapeutico --
  e INFRAESTRUTURA ENERGETICA. Sem motivacao, nenhuma outra energia se move.

RELACIONAL (social = conexao):
  O ser humano isolado DEGRADA. Conexao e necessidade energetica.
  A assembleia, o mutirao, a cooperativa sao GERADORES de energia relacional.
  P9 protege esta energia do atrito da polarizacao.

A LEI DE TODOS OS 10:
  INPUT -> CONVERSAO -> OUTPUT -> RESIDUO.
  Nada se cria, tudo se transforma.
  A Republica nao cria energia. TRANSFORMA.
  E transforma COM JUSTICA: sem desperdicio, sem exclusao, semElite.
// )


se __name__ == "__main__" entao:
    _demo()

```
