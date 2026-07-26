// OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos do Corpo e da Civilizacao
// Energia e a bateria do trabalho. Nada foi feito na Terra por humanos
// sem a necessidade de energia.
//
// O corpo humano nao tem UM sistema de energia. Tem DEZ.
// Cada um com input, conversao, output e residuo.
// A civilizacao herda essa estrutura.
// Author: OpenRepublic Team
package main

import (
    "fmt"
    "strings"
)

// ============================================================================
// 1. TIPOS
// ============================================================================

const (
    EnergiaCelular = "celular"  // Energia Celular (mitocondrial)
    EnergiaMecanica = "mecanica"  // Energia Mecanica (muscular)
    EnergiaTermica = "termica"  // Energia Termica (metabolica)
    EnergiaNeural = "neural"  // Energia Neural (sinal)
    EnergiaQuimica = "quimica"  // Energia Quimica (sintese)
    EnergiaSensorial = "sensorial"  // Energia Sensorial (transducao)
    EnergiaCognitiva = "cognitiva"  // Energia Cognitiva (processamento)
    EnergiaAtencional = "atencional"  // Energia Atencional (foco)
    EnergiaEmocional = "emocional"  // Energia Emocional (motivacao)
    EnergiaRelacional = "relacional"  // Energia Relacional (social)
)

var tipoEnergiaRotulo = map[string]string{
    "celular": "Energia Celular (mitocondrial)",
    "mecanica": "Energia Mecanica (muscular)",
    "termica": "Energia Termica (metabolica)",
    "neural": "Energia Neural (sinal)",
    "quimica": "Energia Quimica (sintese)",
    "sensorial": "Energia Sensorial (transducao)",
    "cognitiva": "Energia Cognitiva (processamento)",
    "atencional": "Energia Atencional (foco)",
    "emocional": "Energia Emocional (motivacao)",
    "relacional": "Energia Relacional (social)",
}

const (
    EscalaCorpo = "corpo"  // Nivel do corpo individual
    EscalaComunidade = "comunidade"  // Nivel da comunidade/local
    EscalaCivilizacao = "civilizacao"  // Nivel da civilizacao/global
    EscalaPlaneta = "planeta"  // Nivel planetario/biosfera
)

var escalaRotulo = map[string]string{
    "corpo": "Nivel do corpo individual",
    "comunidade": "Nivel da comunidade/local",
    "civilizacao": "Nivel da civilizacao/global",
    "planeta": "Nivel planetario/biosfera",
}

const (
    CoberturaCoberto = "coberto"
    CoberturaParcial = "parcial"
    CoberturaLacuna = "lacuna"
    CoberturaNao_aplicavel = "nao_aplicavel"
)

var nivelCoberturaFlag = map[string]string{
    "coberto": "OK",
    "parcial": "PARCIAL",
    "lacuna": "LACUNA",
    "nao_aplicavel": "N/A",
}

// ============================================================================
// 2. STRUCTS
// ============================================================================

type SistemaEnergetico struct {
    Tipo                string
    Nome                string
    AnalogiaCorpo       string
    AnalogiaCivilizacao string
    Escala              string
    Conversao           string
    Output              string
    EficienciaPct       float64
    ConsumoCorpoPct     float64
    Observacao          string
}

type CoberturaRepublica struct {
    Tipo    string
    Nivel   string
    Modulos []string
    Lacunas []string
}

// ============================================================================
// 3. DADOS: OS 10 SISTEMAS
// ============================================================================

var sistemas = []SistemaEnergetico{
    {
        Tipo: "celular",
        Nome: "Mitocondrial",
        AnalogiaCorpo: "Mitocondrias convertem glicose + oxigenio em ATP. ATP e a MOEDA energetica da celula -- todo trabalho celular paga em ATP. Sem ATP, a celula morre em segundos.",
        AnalogiaCivilizacao: "A rede eletrica. A tomada e o ATP da civilizacao. Todo aparelho, toda maquina, todo servo consome eletricidade. OpenEnergy cobre este sistema.",
        Escala: "civilizacao",
        Conversao: "Glicose + O2 -> ATP (fosforilacao oxidativa)",
        Output: "ATP (trifosfato de adenosina) / Eletricidade",
        EficienciaPct: 40.0,
        ConsumoCorpoPct: 0.0,
        Observacao: "Sistema base. Todos os outros dependem deste. OpenEnergy = cobertura total deste nivel.",
    },
    {
        Tipo: "mecanica",
        Nome: "Muscular / Motora",
        AnalogiaCorpo: "ATP -> miosina/actina -> contracao muscular -> MOVIMENTO. O corpo faz TRABALHO FISICO sobre o mundo. Cada passo, cada gesto, cada levantamento de peso.",
        AnalogiaCivilizacao: "Transporte, maquinas, ferramentas, robos. O motor de carro, o braco robotico, a bicicleta. Todo trabalho fisico ja existiu como energia muscular antes de ser externalizado para maquinas.",
        Escala: "civilizacao",
        Conversao: "ATP -> forca mecanica (contracao / combustao / eletricidade)",
        Output: "Movimento, forca, deslocamento",
        EficienciaPct: 25.0,
        ConsumoCorpoPct: 30.0,
        Observacao: "OpenAthlete cobre o lado humano (esporte, treino). Transporte publico (OpenMobility) cobre o lado civilizacional.",
    },
    {
        Tipo: "termica",
        Nome: "Metabolica / Calorica",
        AnalogiaCorpo: "O metabolismo produz calor como subproduto. O corpo GASTA energia mantendo 36,5C -- termorregulacao. Tremer de frio e gerar calor muscular. Suar e dissipar.",
        AnalogiaCivilizacao: "Aquecimento, cozimento, refrigeracao. O FOGO foi a primeira energia externa que o humano dominou (1 milhao de anos antes da eletricidade). Cozinhar e PRE-DIGERIR com energia termica externa -- libera energia celular que iria pra digestao.",
        Escala: "civilizacao",
        Conversao: "Metabolismo / combustao / compressao -> calor",
        Output: "Calor (manutencao de temperatura / cozimento)",
        EficienciaPct: 60.0,
        ConsumoCorpoPct: 50.0,
        Observacao: "Metabolismo basal: 50% do gasto energetico do corpo em repouso e so para manter a temperatura. O cozimento de alimentos foi a REVOLUCAO ENERGETICA original da humanidade.",
    },
    {
        Tipo: "neural",
        Nome: "Sistema Nervoso / Comunicacao",
        AnalogiaCorpo: "Neuronios disparam potenciais de acao -- sinais eletricos. O corpo tem uma REDE de comunicacao interna (87 bilhoes de neuronios). Consome 20W, incrivelmente eficiente. O cerebro pesa 2% do corpo mas consome 20% da energia.",
        AnalogiaCivilizacao: "Internet, telecomunicacoes, radio. A internet e o SISTEMA NERVO da civilizacao. Cada mensagem, cada video, cada chamada e um potencial de acao em escala planetaria. Banda = largura de axonio.",
        Escala: "planeta",
        Conversao: "Sinal eletrico / optico -> transmissao",
        Output: "Comunicacao / sinal / dados transmitidos",
        EficienciaPct: 35.0,
        ConsumoCorpoPct: 20.0,
        Observacao: "LACUNA CRITICA: a Republica NAO tem OpenNetwork/OpenInternet. Quem controla a rede controla o sistema nervoso. Banda gratuita e NECESSARIA (energia neural = direito).",
    },
    {
        Tipo: "quimica",
        Nome: "Sintese / Ligacoes",
        AnalogiaCorpo: "O corpo SINTETIZA moleculas -- proteinas, hormonios, enzimas. Ligacoes quimicas ARMAZENAM energia. Digestao = quebrar ligacoes para liberar. Sintese = gastar energia para construir.",
        AnalogiaCivilizacao: "Industria quimica, baterias, combustiveis, farmacia. Toda manufatura e energia quimica direcionada. FarmLab opera aqui -- sintese de medicamentos e energia quimica a servico da vida.",
        Escala: "civilizacao",
        Conversao: "Reacao quimica (sintese / decomposicao)",
        Output: "Moleculas / materiais / medicamentos",
        EficienciaPct: 30.0,
        ConsumoCorpoPct: 10.0,
        Observacao: "FarmLab cobre farmacia. OpenChemistry cobre industria quimica.",
    },
    {
        Tipo: "sensorial",
        Nome: "Transducao / Percepcao",
        AnalogiaCorpo: "Olhos capturam FOTONS. Ouvidos capturam VIBRACOES. Pele captura CALOR. O corpo e um RECEPTOR de energia -- converte formas externas em sinais internos. Cada sentido e um TRANSDUTOR energetico.",
        AnalogiaCivilizacao: "Cameras, microfones, sensores, instrumentos cientificos. OpenTelefonista opera aqui -- o smartphone como CORPO ESTENDIDO captura energia do ambiente (luz, som, posicao) e converte em percepcao. Cego ve obstaculos. Surdo le labios.",
        Escala: "corpo",
        Conversao: "Transducao sensorial (foton/fonon -> sinal neural)",
        Output: "Percepcao / dados sensoriais",
        EficienciaPct: 70.0,
        ConsumoCorpoPct: 5.0,
        Observacao: "OpenTelefonista cobre (smartphone como corpo estendido). OpenInclusiveHardware (44 dispositivos) amplia. OpenInclusiveIDE integra para desenvolvimento.",
    },
    {
        Tipo: "cognitiva",
        Nome: "Cerebro / Processamento",
        AnalogiaCorpo: "O cerebro CONSOME 20% da energia do corpo pesando 2%. PENSAR E CARO energeticamente. O cansaco mental e real -- e gasto energetico, nao frescura. Resolver um problema matematico gasta mais glicose que assistir TV.",
        AnalogiaCivilizacao: "Computacao, IA, analise de dados. Um data center consome tanta energia quanto uma cidade. Processar informacao TEM CUSTO ENERGETICO -- nao e gratuito. P8: IA amplifica inteligencia humana, NAO substitui. Mas o custo de computar e REAL e precisa alocacao.",
        Escala: "civilizacao",
        Conversao: "Processamento (neural / digital)",
        Output: "Decisao / calculo / conhecimento",
        EficienciaPct: 15.0,
        ConsumoCorpoPct: 20.0,
        Observacao: "HumanKnowledge (multi-AI + verificacao) cobre parcialmente. P8 define o principio (IA = instrumento). Custo computacional como recurso a alocar = LACUNA.",
    },
    {
        Tipo: "atencional",
        Nome: "Foco / Atencao",
        AnalogiaCorpo: "A atencao e FINITA. Voce nao consegue focar em tudo. Focar GASTA energia cognitiva. O cerebro tem um BUDGET de atencao -- distribui entre tarefas. Dormir mal = budget de atencao menor no dia seguinte.",
        AnalogiaCivilizacao: "A energia que FocusGuard protege. O scroll infinito DRENA energia atencional. A 'economia da atencao' e a forma mais NOVA de exploracao energetica -- plataformas capturam sua atencao e vendem. P8 exige proteger esta energia. AntiSpamCall protege parcialmente.",
        Escala: "corpo",
        Conversao: "Filtro atencional (top-down + bottom-up)",
        Output: "Foco / atencao direcionada",
        EficienciaPct: 10.0,
        ConsumoCorpoPct: 0.0,
        Observacao: "FocusGuard (overlay IDE) cobre parcialmente. AntiSpamCall ('para de me encher o saco') protege. OpenContentPolicy (midia, ruido) protege. Politica mais ampla de atencao como recurso = LACUNA.",
    },
    {
        Tipo: "emocional",
        Nome: "Motivacao / Drive",
        AnalogiaCorpo: "Motivacao, drive, vontade. Em termos fisicos: dopamina, noradrenalina, cortisol -- moleculas que MODULAM quanto de outras energias o corpo vai despender. Sem dopamina, o corpo tem ATP mas nao se MOVE. A depressao e crise energetica emocional -- o combustivel existe, mas o motor nao liga.",
        AnalogiaCivilizacao: "O kaizen (1% ao dia) opera aqui. Curiosidade, progresso, desafio, recompensa, pertencimento -- os 5 gatilhos psicologicos sao GERADORES de energia emocional. O Huxley soma (dopamina artificial do scroll) e o SEQUESTRO desta energia -- drena ao inves de gerar.",
        Escala: "comunidade",
        Conversao: "Modulacao neuroquimica (dopamina/serotonina/cortisol)",
        Output: "Motivacao / drive / vontade de agir",
        EficienciaPct: 20.0,
        ConsumoCorpoPct: 0.0,
        Observacao: "LACUNA CRITICA: nenhum modulo trata saude mental como INFRAESTRUTURA ENERGETICA. Depressao = deficit energetico. Burnout = deplecao. Kaizen e gerador, mas falta sistema.",
    },
    {
        Tipo: "relacional",
        Nome: "Social / Conexao",
        AnalogiaCorpo: "O ser humano isolado DEGRADA. Solidao cronica aumenta mortalidade em 26%. O corpo PRECISA de conexao para funcionar bem -- nao e luxo, e necessidade energetica. Oxitocina, espelhamento neural, co-regulacao.",
        AnalogiaCivilizacao: "A assembleia, o mutirao, a cooperativa. O Two-Person Rule nao e so procedimento -- e ARQUITETURA ENERGETICA. Duas pessoas juntas fazem mais que duas separadas. A energia social e SINERGICA: 1+1 > 2. Quando a assembleia polariza (P9), e esta energia que se GASTA em atrito em vez de gerar valor.",
        Escala: "comunidade",
        Conversao: "Co-regulacao neuroquimica + espelhamento neural",
        Output: "Cooperacao / sinergia / vinculo",
        EficienciaPct: 80.0,
        ConsumoCorpoPct: 0.0,
        Observacao: "OpenCommunities (6 adaptacoes) cobre parcialmente. OpenConstituentAssembly (governanca) cobre parcialmente. OpenCrowdsourcing (ajuda mutua) cobre parcialmente. P9 (anti-polarizacao) PROTEGE esta energia. Tratar conexao como recurso energetico mensuravel = LACUNA.",
    },
}

// ============================================================================
// 4. DADOS: COBERTURAS
// ============================================================================

var coberturas = []CoberturaRepublica{
    {
        Tipo: "celular",
        Nivel: "coberto",
        Modulos: []string{"open-energy", "open-agrarian-revolution", "open-credit"},
        Lacunas: []string{},
    },
    {
        Tipo: "mecanica",
        Nivel: "parcial",
        Modulos: []string{"open-athlete", "open-martial-arts"},
        Lacunas: []string{"sistema de transporte publico gratuito (OpenMobility)"},
    },
    {
        Tipo: "termica",
        Nivel: "parcial",
        Modulos: []string{"open-energy"},
        Lacunas: []string{"politica de cozimento comunitario", "aquecimento como direito"},
    },
    {
        Tipo: "neural",
        Nivel: "lacuna",
        Modulos: []string{},
        Lacunas: []string{"OpenNetwork/OpenInternet -- banda gratuita como direito", "sistema nervoso da civilizacao sem dono", "neutralidade de rede como P1 (anti-elitismo)"},
    },
    {
        Tipo: "quimica",
        Nivel: "parcial",
        Modulos: []string{"open-chemistry", "open-physics"},
        Lacunas: []string{"FarmLab completo (sintese CC0 de medicamentos)"},
    },
    {
        Tipo: "sensorial",
        Nivel: "coberto",
        Modulos: []string{"open-telefonista", "open-inclusive-hardware", "open-inclusive-ide"},
        Lacunas: []string{},
    },
    {
        Tipo: "cognitiva",
        Nivel: "parcial",
        Modulos: []string{"open-human-knowledge", "open-human-amplification"},
        Lacunas: []string{"alocacao de custo computacional como recurso energetico"},
    },
    {
        Tipo: "atencional",
        Nivel: "parcial",
        Modulos: []string{"open-focus-guard", "open-anti-spam-call", "open-content-policy"},
        Lacunas: []string{"politica ampla de atencao como recurso energetico finito"},
    },
    {
        Tipo: "emocional",
        Nivel: "lacuna",
        Modulos: []string{},
        Lacunas: []string{"OpenMentalHealth -- saude mental como INFRAESTRUTURA ENERGETICA", "sistema de deteccao de deplecao emocional (burnout/depressao)", "geradores de energia emocional (kaizen, pertencimento, proposito)"},
    },
    {
        Tipo: "relacional",
        Nivel: "parcial",
        Modulos: []string{"open-communities", "open-constituent-assembly", "open-anti-polarization"},
        Lacunas: []string{"conexao como recurso energetico mensuravel e protegido"},
    },
}

// ============================================================================
// 5. DEMO
// ============================================================================

func main() {
    fmt.Println(strings.Repeat("=", 70))
    fmt.Println("OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos")
    fmt.Println("Do Corpo Humano a Civilizacao")
    fmt.Println(strings.Repeat("=", 70))

    // OS 10 SISTEMAS
    fmt.Println("\n[OS 10 SISTEMAS ENERGETICOS]")
    for i, s := range sistemas {
        fmt.Printf("\n  --- Sistema %d: %s ---\n", i+1, tipoEnergiaRotulo[s.Tipo])
        fmt.Printf("  Escala: %s\n", escalaRotulo[s.Escala])
        fmt.Printf("  CORPO: %s\n", s.AnalogiaCorpo)
        fmt.Printf("  CIVILIZACAO: %s\n", s.AnalogiaCivilizacao)
        if s.ConsumoCorpoPct > 0 {
            fmt.Printf("  Consumo no corpo: %.0f%% do orcamento energetico\n", s.ConsumoCorpoPct)
        }
        fmt.Printf("  CONVERSAO: %s\n", s.Conversao)
        fmt.Printf("  OUTPUT: %s\n", s.Output)
        fmt.Printf("  EFICIENCIA: %.0f%%\n", s.EficienciaPct)
        if len(s.Observacao) > 0 {
            fmt.Printf("  OBS: %s\n", s.Observacao)
        }
    }

    // PADRAO UNIVERSAL
    fmt.Println("\n" + strings.Repeat("=", 70))
    fmt.Println("[O PADRAO UNIVERSAL]")
    fmt.Println(strings.Repeat("=", 70))
    fmt.Println("\nPADRAO UNIVERSAL: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO")
    fmt.Println("Nada se cria. Tudo se transforma.")
    fmt.Println("Nao existe trabalho sem energia.")
    fmt.Println("Nao existe energia sem input.")
    fmt.Println("Nao existe output sem residuo.")
    fmt.Println("A questao civilizatoria nunca foi 'como conseguir energia' ")
    fmt.Println("-- sempre foi 'como TRANSFORMAR com justica e sem desperdicar'.")

    // COBERTURA DA REPUBLICA
    fmt.Println("\n" + strings.Repeat("=", 70))
    fmt.Println("[COBERTURA DA REPUBLICA -- O QUE FALTA]")
    fmt.Println(strings.Repeat("=", 70))
    for _, c := range coberturas {
        flag := nivelCoberturaFlag[c.Nivel]
        fmt.Printf("\n  [%s] %s\n", flag, tipoEnergiaRotulo[c.Tipo])
        if len(c.Modulos) > 0 {
            fmt.Printf("  Modulos: %s\n", strings.Join(c.Modulos, ", "))
        }
        if len(c.Lacunas) > 0 {
            fmt.Println("  LACUNAS:")
            for _, l := range c.Lacunas {
                fmt.Printf("    - %s\n", l)
            }
        }
    }

    // SCORECARD
    cobertos, parciais, lacunas := 0, 0, 0
    for _, c := range coberturas {
        switch c.Nivel {
        case "coberto":
            cobertos++
        case "parcial":
            parciais++
        case "lacuna":
            lacunas++
        }
    }
    fmt.Println("\n" + strings.Repeat("=", 70))
    fmt.Println("[SCORECARD DA TAXONOMIA ENERGETICA]")
    fmt.Println(strings.Repeat("=", 70))
    fmt.Printf("  sistemas_total................ %d\n", 10)
    fmt.Printf("  totalmente_cobertos........... %d\n", cobertos)
    fmt.Printf("  parcialmente_cobertos......... %d\n", parciais)
    fmt.Printf("  lacunas_criticas.............. %d\n", lacunas)
    fmt.Printf("  pct_cobertura................. %.1f%%\n", float64(cobertos)/10.0*100.0)

    // FILOSOFIA
    fmt.Println("\n" + strings.Repeat("=", 70))
    fmt.Println("FILOSOFIA -- Energia e a bateria do trabalho")
    fmt.Println(strings.Repeat("=", 70))
    fmt.Println("\n\"Energia e a bateria do trabalho. Nosso corpo so funciona porque")
    fmt.Println("temos energia. Nada foi feito na Terra por humanos sem a necessidade")
    fmt.Println("de energia.\"")
    fmt.Println("\nO corpo humano nao tem UM sistema de energia. Tem DEZ.")
    fmt.Println("Cada um com input, conversao, output e residuo.")
    fmt.Println("A civilizacao herda essa estrutura -- somos um corpo em escala.")
    fmt.Println("\nNEURAL (sistema nervoso = internet):")
    fmt.Println("  Quem controla a rede controla o sistema nervoso da civilizacao.")
    fmt.Println("  Banda gratuita e NECESSARIA. A internet e o nervo. Sem nervo, paralisia.")
    fmt.Println("\nATENCIONAL (foco = atencao finita):")
    fmt.Println("  A atencao e o recurso mais explorado do seculo XXI.")
    fmt.Println("  Plataformas capturam sua atencao e vendem. Isso e EXTRATIVISMO ENERGETICO.")
    fmt.Println("\nEMOCIONAL (motivacao = drive):")
    fmt.Println("  Depressao e CRISE ENERGETICA. O combustivel existe (ATP), mas o motor")
    fmt.Println("  nao liga (sem dopamina). Saude mental nao e luxo terapeutico --")
    fmt.Println("  e INFRAESTRUTURA ENERGETICA. Sem motivacao, nenhuma outra energia se move.")
    fmt.Println("\nA LEI DE TODOS OS 10:")
    fmt.Println("  INPUT -> CONVERSAO -> OUTPUT -> RESIDUO.")
    fmt.Println("  Nada se cria, tudo se transforma.")
    fmt.Println("  A Republica nao cria energia. TRANSFORMA.")
    fmt.Println("  E transforma COM JUSTICA: sem desperdicio, sem exclusao.")
}
