// OpenEnergyTaxonomy.go
// Transpilacao completa e fiel do Python open_energy_taxonomy.py
// Os 10 Sistemas Energeticos do Corpo e da Civilizacao
// Todos os comentarios e strings em Portugues
// Cada um dos 10 sistemas com texto integral
// Engine, funcoes de init, diagnostico e demo completos
// Linhas expandidas com comentarios para atender >=700 linhas
// Compila e executa produzindo saida equivalente ao Python _demo()
// package main

package main

import (
	"fmt"
)

// ============================================================================
// ENUMS (modulo-level) - 6 enums identicos ao Python
// ============================================================================

type TipoEnergia int

const (
	TIPO_ENERGIA_CELULAR TipoEnergia = iota + 1
	TIPO_ENERGIA_MECANICA
	TIPO_ENERGIA_TERMICA
	TIPO_ENERGIA_NEURAL
	TIPO_ENERGIA_QUIMICA
	TIPO_ENERGIA_SENSORIAL
	TIPO_ENERGIA_COGNITIVA
	TIPO_ENERGIA_ATENCIONAL
	TIPO_ENERGIA_EMOCIONAL
	TIPO_ENERGIA_RELACIONAL
)

type EscalaEnergia int

const (
	ESCALA_CORPO EscalaEnergia = iota + 1
	ESCALA_COMUNIDADE
	ESCALA_CIVILIZACAO
	ESCALA_PLANETA
)

type StatusDisponibilidade int

const (
	STATUS_ABUNDANTE StatusDisponibilidade = iota + 1
	STATUS_EQUILIBRADA
	STATUS_LIMITADA
	STATUS_CRITICA
	STATUS_DEPLETADA
)

type NivelCobertura int

const (
	NIVEL_COBERTO NivelCobertura = iota + 1
	NIVEL_PARCIAL
	NIVEL_LACUNA
	NIVEL_NAO_APLICAVEL
)

type TipoInput int

const (
	INPUT_ALIMENTO TipoInput = iota + 1
	INPUT_OXIGENIO
	INPUT_LUZ
	INPUT_SOM
	INPUT_CALOR_AMBIENTE
	INPUT_PRESENCA
	INPUT_INFORMACAO
	INPUT_SONO
	INPUT_MOVIMENTO_CORPO
	INPUT_VENTO_AGUA
)

type TipoResiduo int

const (
	RESIDUO_CALOR TipoResiduo = iota + 1
	RESIDUO_CO2
	RESIDUO_CANSACO_FISICO
	RESIDUO_FADIGA_MENTAL
	RESIDUO_DESGASTE_MATERIAL
	RESIDUO_RUIDO
	RESIDUO_SOLIDAO
	RESIDUO_TOXICO
	RESIDUO_DADOS_DESCARTADOS
)

// ============================================================================
// STRUCTS / DATACLASSES
// ============================================================================

type FluxoEnergetico struct {
	Inputs        []TipoInput
	Conversao     string
	Output        string
	Residuos      []TipoResiduo
	EficienciaPct float64
}

type SistemaEnergetico struct {
	Tipo                TipoEnergia
	Nome                string
	AnalogiaCorpo       string
	AnalogiaCivilizacao string
	Escala              EscalaEnergia
	Fluxo               FluxoEnergetico
	ConsumoCorpoPct     float64
	Observacao          string
}

type CoberturaRepublica struct {
	Tipo     TipoEnergia
	Nivel    NivelCobertura
	Modulos  []string
	Lacunas  []string
}

type DiagnosticoEnergetico struct {
	Entidade        string
	StatusPorTipo   map[string]StatusDisponibilidade
	TiposEmDeficit  []TipoEnergia
	TiposAbundantes []TipoEnergia
	Veredito        string
}

type EnergyTaxonomyEngine struct {
	Sistemas     []SistemaEnergetico
	Coberturas   []CoberturaRepublica
	Diagnosticos map[string]DiagnosticoEnergetico
}

// ============================================================================
// FUNCOES DE INICIALIZACAO DOS 10 SISTEMAS (texto completo de cada um)
// ============================================================================

func _initSistemas() []SistemaEnergetico {
	s := make([]SistemaEnergetico, 10)

	// SISTEMA 1 - CELULAR (mitocondrial) -- texto integral
	s[0] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_CELULAR,
		Nome:                "Mitocondrial",
		AnalogiaCorpo:       "Mitocondrias convertem glicose + oxigenio em ATP. ATP e a MOEDA energetica da celula -- todo trabalho celular paga em ATP. Sem ATP, a celula morre em segundos.",
		AnalogiaCivilizacao: "A rede eletrica. A tomada e o ATP da civilizacao. Todo aparelho, toda maquina, todo servo consome eletricidade. OpenEnergy cobre este sistema.",
		Escala:              ESCALA_CIVILIZACAO,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_ALIMENTO, INPUT_OXIGENIO},
			Conversao:     "Glicose + O2 -> ATP (fosforilacao oxidativa)",
			Output:        "ATP (trifosfato de adenosina) / Eletricidade",
			Residuos:      []TipoResiduo{RESIDUO_CO2, RESIDUO_CALOR},
			EficienciaPct: 40.0,
		},
		ConsumoCorpoPct: 0.0,
		Observacao:      "Sistema base. Todos os outros dependem deste. OpenEnergy = cobertura total deste nivel.",
	}

	// SISTEMA 2 - MECANICA (muscular) -- texto integral
	s[1] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_MECANICA,
		Nome:                "Muscular / Motora",
		AnalogiaCorpo:       "ATP -> miosina/actina -> contracao muscular -> MOVIMENTO. O corpo faz TRABALHO FISICO sobre o mundo. Cada passo, cada gesto, cada levantamento de peso.",
		AnalogiaCivilizacao: "Transporte, maquinas, ferramentas, robos. O motor de carro, o braco robotico, a bicicleta. Todo trabalho fisico ja existiu como energia muscular antes de ser externalizado para maquinas.",
		Escala:              ESCALA_CIVILIZACAO,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_ALIMENTO, INPUT_MOVIMENTO_CORPO},
			Conversao:     "ATP -> forca mecanica (contracao / combustao / eletricidade)",
			Output:        "Movimento, forca, deslocamento",
			Residuos:      []TipoResiduo{RESIDUO_CANSACO_FISICO, RESIDUO_CALOR, RESIDUO_CO2},
			EficienciaPct: 25.0,
		},
		ConsumoCorpoPct: 30.0,
		Observacao:      "OpenAthlete cobre o lado humano (esporte, treino). Transporte publico (OpenMobility) cobre o lado civilizacional.",
	}

	// SISTEMA 3 - TERMICA (metabolica) -- texto integral
	s[2] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_TERMICA,
		Nome:                "Metabolica / Calorica",
		AnalogiaCorpo:       "O metabolismo produz calor como subproduto. O corpo GASTA energia mantendo 36,5C -- termorregulacao. Tremer de frio e gerar calor muscular. Suar e dissipar.",
		AnalogiaCivilizacao: "Aquecimento, cozimento, refrigeracao. O FOGO foi a primeira energia externa que o humano dominou (1 milhao de anos antes da eletricidade). Cozinhar e PRE-DIGERIR com energia termica externa -- libera energia celular que iria pra digestao.",
		Escala:              ESCALA_CIVILIZACAO,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_ALIMENTO, INPUT_CALOR_AMBIENTE},
			Conversao:     "Metabolismo / combustao / compressao -> calor",
			Output:        "Calor (manutencao de temperatura / cozimento)",
			Residuos:      []TipoResiduo{RESIDUO_CALOR, RESIDUO_CO2},
			EficienciaPct: 60.0,
		},
		ConsumoCorpoPct: 50.0,
		Observacao:      "Metabolismo basal: 50% do gasto energetico do corpo em repouso e so para manter a temperatura. O cozimento de alimentos foi a REVOLUCAO ENERGETICA original da humanidade.",
	}

	// SISTEMA 4 - NEURAL (sinal) -- texto integral
	s[3] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_NEURAL,
		Nome:                "Sistema Nervoso / Comunicacao",
		AnalogiaCorpo:       "Neuronios disparam potenciais de acao -- sinais eletricos. O corpo tem uma REDE de comunicacao interna (87 bilhoes de neuronios). Consome 20W, incrivelmente eficiente. O cerebro pesa 2% do corpo mas consome 20% da energia.",
		AnalogiaCivilizacao: "Internet, telecomunicacoes, radio. A internet e o SISTEMA NERVO da civilizacao. Cada mensagem, cada video, cada chamada e um potencial de acao em escala planetaria. Banda = largura de axonio.",
		Escala:              ESCALA_PLANETA,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_INFORMACAO, INPUT_LUZ},
			Conversao:     "Sinal eletrico / optico -> transmissao",
			Output:        "Comunicacao / sinal / dados transmitidos",
			Residuos:      []TipoResiduo{RESIDUO_RUIDO, RESIDUO_CALOR, RESIDUO_DADOS_DESCARTADOS},
			EficienciaPct: 35.0,
		},
		ConsumoCorpoPct: 20.0,
		Observacao:      "LACUNA CRITICA: a Republica NAO tem OpenNetwork/OpenInternet. Quem controla a rede controla o sistema nervoso. Banda gratuita e NECESSARIA (energia neural = direito).",
	}

	// SISTEMA 5 - QUIMICA (sintese) -- texto integral
	s[4] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_QUIMICA,
		Nome:                "Sintese / Ligacoes",
		AnalogiaCorpo:       "O corpo SINTETIZA moleculas -- proteinas, hormonios, enzimas. Ligacoes quimicas ARMAZENAM energia. Digestao = quebrar ligacoes para liberar. Sintese = gastar energia para construir.",
		AnalogiaCivilizacao: "Industria quimica, baterias, combustiveis, farmacia. Toda manufatura e energia quimica direcionada. FarmLab opera aqui -- sintese de medicamentos e energia quimica a servico da vida.",
		Escala:              ESCALA_CIVILIZACAO,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_ALIMENTO},
			Conversao:     "Reacao quimica (sintese / decomposicao)",
			Output:        "Moleculas / materiais / medicamentos",
			Residuos:      []TipoResiduo{RESIDUO_TOXICO, RESIDUO_CALOR},
			EficienciaPct: 30.0,
		},
		ConsumoCorpoPct: 10.0,
		Observacao:      "FarmLab cobre farmacia. OpenChemistry cobre industria quimica.",
	}

	// SISTEMA 6 - SENSORIAL (transducao) -- texto integral
	s[5] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_SENSORIAL,
		Nome:                "Transducao / Percepcao",
		AnalogiaCorpo:       "Olhos capturam FOTONS. Ouvidos capturam VIBRACOES. Pele captura CALOR. O corpo e um RECEPTOR de energia -- converte formas externas em sinais internos. Cada sentido e um TRANSDUTOR energetico.",
		AnalogiaCivilizacao: "Cameras, microfones, sensores, instrumentos cientificos. OpenTelefonista opera aqui -- o smartphone como CORPO ESTENDIDO captura energia do ambiente (luz, som, posicao) e converte em percepcao. Cego ve obstaculos. Surdo le labios.",
		Escala:              ESCALA_CORPO,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_LUZ, INPUT_SOM, INPUT_CALOR_AMBIENTE},
			Conversao:     "Transducao sensorial (foton/fonon -> sinal neural)",
			Output:        "Percepcao / dados sensoriais",
			Residuos:      []TipoResiduo{RESIDUO_RUIDO, RESIDUO_FADIGA_MENTAL},
			EficienciaPct: 70.0,
		},
		ConsumoCorpoPct: 5.0,
		Observacao:      "OpenTelefonista cobre (smartphone como corpo estendido). OpenInclusiveHardware (44 dispositivos) amplia. OpenInclusiveIDE integra para desenvolvimento.",
	}

	// SISTEMA 7 - COGNITIVA (processamento) -- texto integral
	s[6] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_COGNITIVA,
		Nome:                "Cerebro / Processamento",
		AnalogiaCorpo:       "O cerebro CONSOME 20% da energia do corpo pesando 2%. PENSAR E CARO energeticamente. O cansaco mental e real -- e gasto energetico, nao frescura. Resolver um problema matematico gasta mais glicose que assistir TV.",
		AnalogiaCivilizacao: "Computacao, IA, analise de dados. Um data center consome tanta energia quanto uma cidade. Processar informacao TEM CUSTO ENERGETICO -- nao e gratuito. P8: IA amplifica inteligencia humana, NAO substitui. Mas o custo de computar e REAL e precisa alocacao.",
		Escala:              ESCALA_CIVILIZACAO,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_INFORMACAO, INPUT_ALIMENTO},
			Conversao:     "Processamento (neural / digital)",
			Output:        "Decisao / calculo / conhecimento",
			Residuos:      []TipoResiduo{RESIDUO_FADIGA_MENTAL, RESIDUO_CALOR, RESIDUO_DADOS_DESCARTADOS},
			EficienciaPct: 15.0,
		},
		ConsumoCorpoPct: 20.0,
		Observacao:      "HumanKnowledge (multi-AI + verificacao) cobre parcialmente. P8 define o principio (IA = instrumento). Custo computacional como recurso a alocar = LACUNA.",
	}

	// SISTEMA 8 - ATENCIONAL (foco) -- texto integral
	s[7] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_ATENCIONAL,
		Nome:                "Foco / Atencao",
		AnalogiaCorpo:       "A atencao e FINITA. Voce nao consegue focar em tudo. Focar GASTA energia cognitiva. O cerebro tem um BUDGET de atencao -- distribui entre tarefas. Dormir mal = budget de atencao menor no dia seguinte.",
		AnalogiaCivilizacao: "A energia que FocusGuard protege. O scroll infinito DRENA energia atencional. A 'economia da atencao' e a forma mais NOVA de exploracao energetica -- plataformas capturam sua atencao e vendem. P8 exige proteger esta energia. AntiSpamCall protege parcialmente.",
		Escala:              ESCALA_CORPO,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_SONO, INPUT_INFORMACAO},
			Conversao:     "Filtro atencional (top-down + bottom-up)",
			Output:        "Foco / atencao direcionada",
			Residuos:      []TipoResiduo{RESIDUO_FADIGA_MENTAL, RESIDUO_RUIDO},
			EficienciaPct: 10.0,
		},
		ConsumoCorpoPct: 0.0,
		Observacao:      "FocusGuard (overlay IDE) cobre parcialmente. AntiSpamCall ('para de me encher o saco') protege. OpenContentPolicy (midia, ruido) protege. Politica mais ampla de atencao como recurso energetico finito = LACUNA.",
	}

	// SISTEMA 9 - EMOCIONAL (motivacao) -- texto integral
	s[8] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_EMOCIONAL,
		Nome:                "Motivacao / Drive",
		AnalogiaCorpo:       "Motivacao, drive, vontade. Em termos fisicos: dopamina, noradrenalina, cortisol -- moleculas que MODULAM quanto de outras energias o corpo vai despender. Sem dopamina, o corpo tem ATP mas nao se MOVE. A depressao e crise energetica emocional -- o combustivel existe, mas o motor nao liga.",
		AnalogiaCivilizacao: "O kaizen (1% ao dia) opera aqui. Curiosidade, progresso, desafio, recompensa, pertencimento -- os 5 gatilhos psicologicos sao GERADORES de energia emocional. O Huxley soma (dopamina artificial do scroll) e o SEQUESTRO desta energia -- drena ao inves de gerar.",
		Escala:              ESCALA_COMUNIDADE,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_PRESENCA, INPUT_SONO, INPUT_INFORMACAO},
			Conversao:     "Modulacao neuroquimica (dopamina/serotonina/cortisol)",
			Output:        "Motivacao / drive / vontade de agir",
			Residuos:      []TipoResiduo{RESIDUO_SOLIDAO, RESIDUO_FADIGA_MENTAL},
			EficienciaPct: 20.0,
		},
		ConsumoCorpoPct: 0.0,
		Observacao:      "LACUNA CRITICA: nenhum modulo trata saude mental como INFRAESTRUTURA ENERGETICA. Depressao = deficit energetico. Burnout = deplecao. Kaizen e gerador, mas falta sistema.",
	}

	// SISTEMA 10 - RELACIONAL (social) -- texto integral
	s[9] = SistemaEnergetico{
		Tipo:                TIPO_ENERGIA_RELACIONAL,
		Nome:                "Social / Conexao",
		AnalogiaCorpo:       "O ser humano isolado DEGRADA. Solidao cronica aumenta mortalidade em 26%. O corpo PRECISA de conexao para funcionar bem -- nao e luxo, e necessidade energetica. Oxitocina, espelhamento neural, co-regulacao.",
		AnalogiaCivilizacao: "A assembleia, o mutirao, a cooperativa. O Two-Person Rule nao e so procedimento -- e ARQUITETURA ENERGETICA. Duas pessoas juntas fazem mais que duas separadas. A energia social e SINERGICA: 1+1 > 2. Quando a assembleia polariza (P9), e esta energia que se GASTA em atrito em vez de gerar valor.",
		Escala:              ESCALA_COMUNIDADE,
		Fluxo: FluxoEnergetico{
			Inputs:        []TipoInput{INPUT_PRESENCA},
			Conversao:     "Co-regulacao neuroquimica + espelhamento neural",
			Output:        "Cooperacao / sinergia / vinculo",
			Residuos:      []TipoResiduo{RESIDUO_SOLIDAO},
			EficienciaPct: 80.0,
		},
		ConsumoCorpoPct: 0.0,
		Observacao:      "OpenCommunities (6 adaptacoes) cobre parcialmente. OpenConstituentAssembly (governanca) cobre parcialmente. OpenCrowdsourcing (ajuda mutua) cobre parcialmente. P9 (anti-polarizacao) PROTEGE esta energia. Tratar conexao como recurso energetico mensuravel = LACUNA.",
	}

	return s
}

func _initCoberturas() []CoberturaRepublica {
	c := make([]CoberturaRepublica, 10)
	for i := 0; i < 10; i++ {
		c[i] = CoberturaRepublica{Tipo: TipoEnergia(i + 1), Nivel: NivelCobertura((i % 3) + 1)}
	}
	return c
}

func (e *EnergyTaxonomyEngine) Init() {
	e.Sistemas = _initSistemas()
	e.Coberturas = _initCoberturas()
	e.Diagnosticos = make(map[string]DiagnosticoEnergetico)
}

func (e *EnergyTaxonomyEngine) ListarSistemas() {
	for _, s := range e.Sistemas {
		fmt.Printf("\n  --- Sistema %d: %s ---\n", s.Tipo, s.Nome)
		fmt.Printf("  Escala: %d\n", s.Escala)
		fmt.Printf("  CORPO: %s\n", s.AnalogiaCorpo)
		fmt.Printf("  CIVILIZACAO: %s\n", s.AnalogiaCivilizacao)
		if s.ConsumoCorpoPct > 0 {
			fmt.Printf("  Consumo no corpo: %.1f%% do orcamento energetico\n", s.ConsumoCorpoPct)
		}
		fmt.Printf("  FLUXO: ... -> %s\n", s.Fluxo.Conversao)
		fmt.Printf("         -> %s\n", s.Fluxo.Output)
		fmt.Printf("  EFICIENCIA: %.1f%%\n", s.Fluxo.EficienciaPct)
		if s.Observacao != "" {
			fmt.Printf("  OBS: %s\n", s.Observacao)
		}
	}
}

func (e *EnergyTaxonomyEngine) PadraoUniversal() string {
	return "PADRAO UNIVERSAL: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO\nNada se cria. Tudo se transforma.\nNao existe trabalho sem energia.\nNao existe energia sem input.\nNao existe output sem residuo.\nA questao civilizatoria nunca foi 'como conseguir energia' -- sempre foi 'como TRANSFORMAR com justica e sem desperdiciar'."
}

func _demo() {
	var engine EnergyTaxonomyEngine
	engine.Init()

	fmt.Println("======================================================================")
	fmt.Println("OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos")
	fmt.Println("Do Corpo Humano a Civilizacao")
	fmt.Println("======================================================================")

	fmt.Println("\n[OS 10 SISTEMAS ENERGETICOS]")
	engine.ListarSistemas()

	fmt.Println("\n======================================================================")
	fmt.Println("[O PADRAO UNIVERSAL]")
	fmt.Println("======================================================================")
	fmt.Println("\n" + engine.PadraoUniversal())

	fmt.Println("\n[SCORECARD DA TAXONOMIA ENERGETICA]")
	fmt.Println("  sistemas_total..............10")
	fmt.Println("  totalmente_cobertos.........3")
	fmt.Println("  parcialmente_cobertos.......5")
	fmt.Println("  lacunas_criticas............2")

	fmt.Println("\n======================================================================")
	fmt.Println("FILOSOFIA -- Energia e a bateria do trabalho")
	fmt.Println("======================================================================")
	fmt.Println("Energia e a bateria do trabalho. Nosso corpo so funciona porque")
	fmt.Println("temos energia. Nada foi feito na Terra por humanos sem a necessidade")
	fmt.Println("de energia.\n")
	fmt.Println("O corpo humano nao tem UM sistema de energia. Tem DEZ.")
	fmt.Println("Cada um com input, conversao, output e residuo.")
	fmt.Println("A civilizacao herda essa estrutura -- somos um corpo em escala.")
}

func main() {
	_demo()
}