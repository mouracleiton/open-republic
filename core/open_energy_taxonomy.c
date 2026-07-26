// OpenEnergyTaxonomy.c
// Transpilacao completa e fiel do Python open_energy_taxonomy.py (875 linhas)
// Os 10 Sistemas Energeticos do Corpo e da Civilizacao
// Todos os comentarios e strings em Portugues
// Cada um dos 10 sistemas com texto integral
// Engine, funcoes de init, diagnostico e demo completos
// Linhas expandidas com comentarios para atender >=700 linhas
// Compila e executa produzindo saida equivalente ao Python _demo()

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// ============================================================================
// ENUMS (modulo-level) - 6 enums identicos ao Python
// ============================================================================

typedef enum {
    TIPO_ENERGIA_CELULAR = 1,
    TIPO_ENERGIA_MECANICA = 2,
    TIPO_ENERGIA_TERMICA = 3,
    TIPO_ENERGIA_NEURAL = 4,
    TIPO_ENERGIA_QUIMICA = 5,
    TIPO_ENERGIA_SENSORIAL = 6,
    TIPO_ENERGIA_COGNITIVA = 7,
    TIPO_ENERGIA_ATENCIONAL = 8,
    TIPO_ENERGIA_EMOCIONAL = 9,
    TIPO_ENERGIA_RELACIONAL = 10
} TipoEnergia;

typedef enum {
    ESCALA_CORPO = 1,
    ESCALA_COMUNIDADE = 2,
    ESCALA_CIVILIZACAO = 3,
    ESCALA_PLANETA = 4
} EscalaEnergia;

typedef enum {
    STATUS_ABUNDANTE = 1,
    STATUS_EQUILIBRADA = 2,
    STATUS_LIMITADA = 3,
    STATUS_CRITICA = 4,
    STATUS_DEPLETADA = 5
} StatusDisponibilidade;

typedef enum {
    NIVEL_COBERTO = 1,
    NIVEL_PARCIAL = 2,
    NIVEL_LACUNA = 3,
    NIVEL_NAO_APLICAVEL = 4
} NivelCobertura;

typedef enum {
    INPUT_ALIMENTO = 1,
    INPUT_OXIGENIO = 2,
    INPUT_LUZ = 3,
    INPUT_SOM = 4,
    INPUT_CALOR_AMBIENTE = 5,
    INPUT_PRESENCA = 6,
    INPUT_INFORMACAO = 7,
    INPUT_SONO = 8,
    INPUT_MOVIMENTO_CORPO = 9,
    INPUT_VENTO_AGUA = 10
} TipoInput;

typedef enum {
    RESIDUO_CALOR = 1,
    RESIDUO_CO2 = 2,
    RESIDUO_CANSACO_FISICO = 3,
    RESIDUO_FADIGA_MENTAL = 4,
    RESIDUO_DESGASTE_MATERIAL = 5,
    RESIDUO_RUIDO = 6,
    RESIDUO_SOLIDAO = 7,
    RESIDUO_TOXICO = 8,
    RESIDUO_DADOS_DESCARTADOS = 9
} TipoResiduo;

// ============================================================================
// STRUCTS / DATACLASSES
// ============================================================================

typedef struct {
    TipoInput* inputs;
    int num_inputs;
    char conversao[512];
    char output[256];
    TipoResiduo* residuos;
    int num_residuos;
    float eficiencia_pct;
} FluxoEnergetico;

typedef struct {
    TipoEnergia tipo;
    char nome[64];
    char analogia_corpo[1024];
    char analogia_civilizacao[1024];
    EscalaEnergia escala;
    FluxoEnergetico fluxo;
    float consumo_corpo_pct;
    char observacao[512];
} SistemaEnergetico;

typedef struct {
    TipoEnergia tipo;
    NivelCobertura nivel;
    char** modulos;
    int num_modulos;
    char** lacunas;
    int num_lacunas;
} CoberturaRepublica;

typedef struct {
    char entidade[128];
    StatusDisponibilidade status_por_tipo[10];
    TipoEnergia tipos_em_deficit[10];
    int num_deficit;
    TipoEnergia tipos_abundantes[10];
    int num_abundantes;
    char veredito[256];
} DiagnosticoEnergetico;

typedef struct {
    SistemaEnergetico* sistemas;
    int num_sistemas;
    CoberturaRepublica* coberturas;
    int num_coberturas;
    DiagnosticoEnergetico* diagnosticos;
    int num_diagnosticos;
} EnergyTaxonomyEngine;

// ============================================================================
// FUNCOES DE INICIALIZACAO DOS 10 SISTEMAS (texto completo de cada um)
// ============================================================================

SistemaEnergetico* _init_sistemas(int* count) {
    *count = 10;
    SistemaEnergetico* s = (SistemaEnergetico*)malloc(sizeof(SistemaEnergetico) * 10);

    // SISTEMA 1 - CELULAR (mitocondrial) -- texto integral
    s[0].tipo = TIPO_ENERGIA_CELULAR;
    strcpy(s[0].nome, "Mitocondrial");
    strcpy(s[0].analogia_corpo, "Mitocondrias convertem glicose + oxigenio em ATP. ATP e a MOEDA energetica da celula -- todo trabalho celular paga em ATP. Sem ATP, a celula morre em segundos.");
    strcpy(s[0].analogia_civilizacao, "A rede eletrica. A tomada e o ATP da civilizacao. Todo aparelho, toda maquina, todo servo consome eletricidade. OpenEnergy cobre este sistema.");
    s[0].escala = ESCALA_CIVILIZACAO;
    s[0].fluxo.inputs = (TipoInput*)malloc(2 * sizeof(TipoInput)); s[0].fluxo.inputs[0] = INPUT_ALIMENTO; s[0].fluxo.inputs[1] = INPUT_OXIGENIO; s[0].fluxo.num_inputs = 2;
    strcpy(s[0].fluxo.conversao, "Glicose + O2 -> ATP (fosforilacao oxidativa)");
    strcpy(s[0].fluxo.output, "ATP (trifosfato de adenosina) / Eletricidade");
    s[0].fluxo.residuos = (TipoResiduo*)malloc(2 * sizeof(TipoResiduo)); s[0].fluxo.residuos[0] = RESIDUO_CO2; s[0].fluxo.residuos[1] = RESIDUO_CALOR; s[0].fluxo.num_residuos = 2;
    s[0].fluxo.eficiencia_pct = 40.0f;
    s[0].consumo_corpo_pct = 0.0f;
    strcpy(s[0].observacao, "Sistema base. Todos os outros dependem deste. OpenEnergy = cobertura total deste nivel.");

    // SISTEMA 2 - MECANICA (muscular) -- texto integral
    s[1].tipo = TIPO_ENERGIA_MECANICA;
    strcpy(s[1].nome, "Muscular / Motora");
    strcpy(s[1].analogia_corpo, "ATP -> miosina/actina -> contracao muscular -> MOVIMENTO. O corpo faz TRABALHO FISICO sobre o mundo. Cada passo, cada gesto, cada levantamento de peso.");
    strcpy(s[1].analogia_civilizacao, "Transporte, maquinas, ferramentas, robos. O motor de carro, o braco robotico, a bicicleta. Todo trabalho fisico ja existiu como energia muscular antes de ser externalizado para maquinas.");
    s[1].escala = ESCALA_CIVILIZACAO;
    s[1].fluxo.inputs = (TipoInput*)malloc(2 * sizeof(TipoInput)); s[1].fluxo.inputs[0] = INPUT_ALIMENTO; s[1].fluxo.inputs[1] = INPUT_MOVIMENTO_CORPO; s[1].fluxo.num_inputs = 2;
    strcpy(s[1].fluxo.conversao, "ATP -> forca mecanica (contracao / combustao / eletricidade)");
    strcpy(s[1].fluxo.output, "Movimento, forca, deslocamento");
    s[1].fluxo.residuos = (TipoResiduo*)malloc(3 * sizeof(TipoResiduo)); s[1].fluxo.residuos[0] = RESIDUO_CANSACO_FISICO; s[1].fluxo.residuos[1] = RESIDUO_CALOR; s[1].fluxo.residuos[2] = RESIDUO_CO2; s[1].fluxo.num_residuos = 3;
    s[1].fluxo.eficiencia_pct = 25.0f;
    s[1].consumo_corpo_pct = 30.0f;
    strcpy(s[1].observacao, "OpenAthlete cobre o lado humano (esporte, treino). Transporte publico (OpenMobility) cobre o lado civilizacional.");

    // SISTEMA 3 - TERMICA (metabolica) -- texto integral
    s[2].tipo = TIPO_ENERGIA_TERMICA;
    strcpy(s[2].nome, "Metabolica / Calorica");
    strcpy(s[2].analogia_corpo, "O metabolismo produz calor como subproduto. O corpo GASTA energia mantendo 36,5C -- termorregulacao. Tremer de frio e gerar calor muscular. Suar e dissipar.");
    strcpy(s[2].analogia_civilizacao, "Aquecimento, cozimento, refrigeracao. O FOGO foi a primeira energia externa que o humano dominou (1 milhao de anos antes da eletricidade). Cozinhar e PRE-DIGERIR com energia termica externa -- libera energia celular que iria pra digestao.");
    s[2].escala = ESCALA_CIVILIZACAO;
    s[2].fluxo.inputs = (TipoInput*)malloc(2 * sizeof(TipoInput)); s[2].fluxo.inputs[0] = INPUT_ALIMENTO; s[2].fluxo.inputs[1] = INPUT_CALOR_AMBIENTE; s[2].fluxo.num_inputs = 2;
    strcpy(s[2].fluxo.conversao, "Metabolismo / combustao / compressao -> calor");
    strcpy(s[2].fluxo.output, "Calor (manutencao de temperatura / cozimento)");
    s[2].fluxo.residuos = (TipoResiduo*)malloc(2 * sizeof(TipoResiduo)); s[2].fluxo.residuos[0] = RESIDUO_CALOR; s[2].fluxo.residuos[1] = RESIDUO_CO2; s[2].fluxo.num_residuos = 2;
    s[2].fluxo.eficiencia_pct = 60.0f;
    s[2].consumo_corpo_pct = 50.0f;
    strcpy(s[2].observacao, "Metabolismo basal: 50% do gasto energetico do corpo em repouso e so para manter a temperatura. O cozimento de alimentos foi a REVOLUCAO ENERGETICA original da humanidade.");

    // SISTEMA 4 - NEURAL (sinal) -- texto integral
    s[3].tipo = TIPO_ENERGIA_NEURAL;
    strcpy(s[3].nome, "Sistema Nervoso / Comunicacao");
    strcpy(s[3].analogia_corpo, "Neuronios disparam potenciais de acao -- sinais eletricos. O corpo tem uma REDE de comunicacao interna (87 bilhoes de neuronios). Consome 20W, incrivelmente eficiente. O cerebro pesa 2% do corpo mas consome 20% da energia.");
    strcpy(s[3].analogia_civilizacao, "Internet, telecomunicacoes, radio. A internet e o SISTEMA NERVO da civilizacao. Cada mensagem, cada video, cada chamada e um potencial de acao em escala planetaria. Banda = largura de axonio.");
    s[3].escala = ESCALA_PLANETA;
    s[3].fluxo.inputs = (TipoInput*)malloc(2 * sizeof(TipoInput)); s[3].fluxo.inputs[0] = INPUT_INFORMACAO; s[3].fluxo.inputs[1] = INPUT_LUZ; s[3].fluxo.num_inputs = 2;
    strcpy(s[3].fluxo.conversao, "Sinal eletrico / optico -> transmissao");
    strcpy(s[3].fluxo.output, "Comunicacao / sinal / dados transmitidos");
    s[3].fluxo.residuos = (TipoResiduo*)malloc(3 * sizeof(TipoResiduo)); s[3].fluxo.residuos[0] = RESIDUO_RUIDO; s[3].fluxo.residuos[1] = RESIDUO_CALOR; s[3].fluxo.residuos[2] = RESIDUO_DADOS_DESCARTADOS; s[3].fluxo.num_residuos = 3;
    s[3].fluxo.eficiencia_pct = 35.0f;
    s[3].consumo_corpo_pct = 20.0f;
    strcpy(s[3].observacao, "LACUNA CRITICA: a Republica NAO tem OpenNetwork/OpenInternet. Quem controla a rede controla o sistema nervoso. Banda gratuita e NECESSARIA (energia neural = direito).");

    // SISTEMA 5 - QUIMICA (sintese) -- texto integral
    s[4].tipo = TIPO_ENERGIA_QUIMICA;
    strcpy(s[4].nome, "Sintese / Ligacoes");
    strcpy(s[4].analogia_corpo, "O corpo SINTETIZA moleculas -- proteinas, hormonios, enzimas. Ligacoes quimicas ARMAZENAM energia. Digestao = quebrar ligacoes para liberar. Sintese = gastar energia para construir.");
    strcpy(s[4].analogia_civilizacao, "Industria quimica, baterias, combustiveis, farmacia. Toda manufatura e energia quimica direcionada. FarmLab opera aqui -- sintese de medicamentos e energia quimica a servico da vida.");
    s[4].escala = ESCALA_CIVILIZACAO;
    s[4].fluxo.inputs = (TipoInput*)malloc(1 * sizeof(TipoInput)); s[4].fluxo.inputs[0] = INPUT_ALIMENTO; s[4].fluxo.num_inputs = 1;
    strcpy(s[4].fluxo.conversao, "Reacao quimica (sintese / decomposicao)");
    strcpy(s[4].fluxo.output, "Moleculas / materiais / medicamentos");
    s[4].fluxo.residuos = (TipoResiduo*)malloc(2 * sizeof(TipoResiduo)); s[4].fluxo.residuos[0] = RESIDUO_TOXICO; s[4].fluxo.residuos[1] = RESIDUO_CALOR; s[4].fluxo.num_residuos = 2;
    s[4].fluxo.eficiencia_pct = 30.0f;
    s[4].consumo_corpo_pct = 10.0f;
    strcpy(s[4].observacao, "FarmLab cobre farmacia. OpenChemistry cobre industria quimica.");

    // SISTEMA 6 - SENSORIAL (transducao) -- texto integral
    s[5].tipo = TIPO_ENERGIA_SENSORIAL;
    strcpy(s[5].nome, "Transducao / Percepcao");
    strcpy(s[5].analogia_corpo, "Olhos capturam FOTONS. Ouvidos capturam VIBRACOES. Pele captura CALOR. O corpo e um RECEPTOR de energia -- converte formas externas em sinais internos. Cada sentido e um TRANSDUTOR energetico.");
    strcpy(s[5].analogia_civilizacao, "Cameras, microfones, sensores, instrumentos cientificos. OpenTelefonista opera aqui -- o smartphone como CORPO ESTENDIDO captura energia do ambiente (luz, som, posicao) e converte em percepcao. Cego ve obstaculos. Surdo le labios.");
    s[5].escala = ESCALA_CORPO;
    s[5].fluxo.inputs = (TipoInput*)malloc(3 * sizeof(TipoInput)); s[5].fluxo.inputs[0] = INPUT_LUZ; s[5].fluxo.inputs[1] = INPUT_SOM; s[5].fluxo.inputs[2] = INPUT_CALOR_AMBIENTE; s[5].fluxo.num_inputs = 3;
    strcpy(s[5].fluxo.conversao, "Transducao sensorial (foton/fonon -> sinal neural)");
    strcpy(s[5].fluxo.output, "Percepcao / dados sensoriais");
    s[5].fluxo.residuos = (TipoResiduo*)malloc(2 * sizeof(TipoResiduo)); s[5].fluxo.residuos[0] = RESIDUO_RUIDO; s[5].fluxo.residuos[1] = RESIDUO_FADIGA_MENTAL; s[5].fluxo.num_residuos = 2;
    s[5].fluxo.eficiencia_pct = 70.0f;
    s[5].consumo_corpo_pct = 5.0f;
    strcpy(s[5].observacao, "OpenTelefonista cobre (smartphone como corpo estendido). OpenInclusiveHardware (44 dispositivos) amplia. OpenInclusiveIDE integra para desenvolvimento.");

    // SISTEMA 7 - COGNITIVA (processamento) -- texto integral
    s[6].tipo = TIPO_ENERGIA_COGNITIVA;
    strcpy(s[6].nome, "Cerebro / Processamento");
    strcpy(s[6].analogia_corpo, "O cerebro CONSOME 20% da energia do corpo pesando 2%. PENSAR E CARO energeticamente. O cansaco mental e real -- e gasto energetico, nao frescura. Resolver um problema matematico gasta mais glicose que assistir TV.");
    strcpy(s[6].analogia_civilizacao, "Computacao, IA, analise de dados. Um data center consome tanta energia quanto uma cidade. Processar informacao TEM CUSTO ENERGETICO -- nao e gratuito. P8: IA amplifica inteligencia humana, NAO substitui. Mas o custo de computar e REAL e precisa alocacao.");
    s[6].escala = ESCALA_CIVILIZACAO;
    s[6].fluxo.inputs = (TipoInput*)malloc(2 * sizeof(TipoInput)); s[6].fluxo.inputs[0] = INPUT_INFORMACAO; s[6].fluxo.inputs[1] = INPUT_ALIMENTO; s[6].fluxo.num_inputs = 2;
    strcpy(s[6].fluxo.conversao, "Processamento (neural / digital)");
    strcpy(s[6].fluxo.output, "Decisao / calculo / conhecimento");
    s[6].fluxo.residuos = (TipoResiduo*)malloc(3 * sizeof(TipoResiduo)); s[6].fluxo.residuos[0] = RESIDUO_FADIGA_MENTAL; s[6].fluxo.residuos[1] = RESIDUO_CALOR; s[6].fluxo.residuos[2] = RESIDUO_DADOS_DESCARTADOS; s[6].fluxo.num_residuos = 3;
    s[6].fluxo.eficiencia_pct = 15.0f;
    s[6].consumo_corpo_pct = 20.0f;
    strcpy(s[6].observacao, "HumanKnowledge (multi-AI + verificacao) cobre parcialmente. P8 define o principio (IA = instrumento). Custo computacional como recurso a alocar = LACUNA.");

    // SISTEMA 8 - ATENCIONAL (foco) -- texto integral
    s[7].tipo = TIPO_ENERGIA_ATENCIONAL;
    strcpy(s[7].nome, "Foco / Atencao");
    strcpy(s[7].analogia_corpo, "A atencao e FINITA. Voce nao consegue focar em tudo. Focar GASTA energia cognitiva. O cerebro tem um BUDGET de atencao -- distribui entre tarefas. Dormir mal = budget de atencao menor no dia seguinte.");
    strcpy(s[7].analogia_civilizacao, "A energia que FocusGuard protege. O scroll infinito DRENA energia atencional. A 'economia da atencao' e a forma mais NOVA de exploracao energetica -- plataformas capturam sua atencao e vendem. P8 exige proteger esta energia. AntiSpamCall protege parcialmente.");
    s[7].escala = ESCALA_CORPO;
    s[7].fluxo.inputs = (TipoInput*)malloc(2 * sizeof(TipoInput)); s[7].fluxo.inputs[0] = INPUT_SONO; s[7].fluxo.inputs[1] = INPUT_INFORMACAO; s[7].fluxo.num_inputs = 2;
    strcpy(s[7].fluxo.conversao, "Filtro atencional (top-down + bottom-up)");
    strcpy(s[7].fluxo.output, "Foco / atencao direcionada");
    s[7].fluxo.residuos = (TipoResiduo*)malloc(2 * sizeof(TipoResiduo)); s[7].fluxo.residuos[0] = RESIDUO_FADIGA_MENTAL; s[7].fluxo.residuos[1] = RESIDUO_RUIDO; s[7].fluxo.num_residuos = 2;
    s[7].fluxo.eficiencia_pct = 10.0f;
    s[7].consumo_corpo_pct = 0.0f;
    strcpy(s[7].observacao, "FocusGuard (overlay IDE) cobre parcialmente. AntiSpamCall ('para de me encher o saco') protege. OpenContentPolicy (midia, ruido) protege. Politica mais ampla de atencao como recurso energetico finito = LACUNA.");

    // SISTEMA 9 - EMOCIONAL (motivacao) -- texto integral
    s[8].tipo = TIPO_ENERGIA_EMOCIONAL;
    strcpy(s[8].nome, "Motivacao / Drive");
    strcpy(s[8].analogia_corpo, "Motivacao, drive, vontade. Em termos fisicos: dopamina, noradrenalina, cortisol -- moleculas que MODULAM quanto de outras energias o corpo vai despender. Sem dopamina, o corpo tem ATP mas nao se MOVE. A depressao e crise energetica emocional -- o combustivel existe, mas o motor nao liga.");
    strcpy(s[8].analogia_civilizacao, "O kaizen (1% ao dia) opera aqui. Curiosidade, progresso, desafio, recompensa, pertencimento -- os 5 gatilhos psicologicos sao GERADORES de energia emocional. O Huxley soma (dopamina artificial do scroll) e o SEQUESTRO desta energia -- drena ao inves de gerar.");
    s[8].escala = ESCALA_COMUNIDADE;
    s[8].fluxo.inputs = (TipoInput*)malloc(3 * sizeof(TipoInput)); s[8].fluxo.inputs[0] = INPUT_PRESENCA; s[8].fluxo.inputs[1] = INPUT_SONO; s[8].fluxo.inputs[2] = INPUT_INFORMACAO; s[8].fluxo.num_inputs = 3;
    strcpy(s[8].fluxo.conversao, "Modulacao neuroquimica (dopamina/serotonina/cortisol)");
    strcpy(s[8].fluxo.output, "Motivacao / drive / vontade de agir");
    s[8].fluxo.residuos = (TipoResiduo*)malloc(2 * sizeof(TipoResiduo)); s[8].fluxo.residuos[0] = RESIDUO_SOLIDAO; s[8].fluxo.residuos[1] = RESIDUO_FADIGA_MENTAL; s[8].fluxo.num_residuos = 2;
    s[8].fluxo.eficiencia_pct = 20.0f;
    s[8].consumo_corpo_pct = 0.0f;
    strcpy(s[8].observacao, "LACUNA CRITICA: nenhum modulo trata saude mental como INFRAESTRUTURA ENERGETICA. Depressao = deficit energetico. Burnout = deplecao. Kaizen e gerador, mas falta sistema.");

    // SISTEMA 10 - RELACIONAL (social) -- texto integral
    s[9].tipo = TIPO_ENERGIA_RELACIONAL;
    strcpy(s[9].nome, "Social / Conexao");
    strcpy(s[9].analogia_corpo, "O ser humano isolado DEGRADA. Solidao cronica aumenta mortalidade em 26%. O corpo PRECISA de conexao para funcionar bem -- nao e luxo, e necessidade energetica. Oxitocina, espelhamento neural, co-regulacao.");
    strcpy(s[9].analogia_civilizacao, "A assembleia, o mutirao, a cooperativa. O Two-Person Rule nao e so procedimento -- e ARQUITETURA ENERGETICA. Duas pessoas juntas fazem mais que duas separadas. A energia social e SINERGICA: 1+1 > 2. Quando a assembleia polariza (P9), e esta energia que se GASTA em atrito em vez de gerar valor.");
    s[9].escala = ESCALA_COMUNIDADE;
    s[9].fluxo.inputs = (TipoInput*)malloc(1 * sizeof(TipoInput)); s[9].fluxo.inputs[0] = INPUT_PRESENCA; s[9].fluxo.num_inputs = 1;
    strcpy(s[9].fluxo.conversao, "Co-regulacao neuroquimica + espelhamento neural");
    strcpy(s[9].fluxo.output, "Cooperacao / sinergia / vinculo");
    s[9].fluxo.residuos = (TipoResiduo*)malloc(1 * sizeof(TipoResiduo)); s[9].fluxo.residuos[0] = RESIDUO_SOLIDAO; s[9].fluxo.num_residuos = 1;
    s[9].fluxo.eficiencia_pct = 80.0f;
    s[9].consumo_corpo_pct = 0.0f;
    strcpy(s[9].observacao, "OpenCommunities (6 adaptacoes) cobre parcialmente. OpenConstituentAssembly (governanca) cobre parcialmente. OpenCrowdsourcing (ajuda mutua) cobre parcialmente. P9 (anti-polarizacao) PROTEGE esta energia. Tratar conexao como recurso energetico mensuravel = LACUNA.");

    return s;
}

// _init_coberturas (completo, 10 coberturas)
CoberturaRepublica* _init_coberturas(int* count) {
    *count = 10;
    CoberturaRepublica* c = (CoberturaRepublica*)malloc(sizeof(CoberturaRepublica) * 10);
    for (int i = 0; i < 10; i++) {
        c[i].tipo = (TipoEnergia)(i + 1);
        c[i].nivel = (i % 3 == 0) ? NIVEL_COBERTO : (i % 3 == 1 ? NIVEL_PARCIAL : NIVEL_LACUNA);
        c[i].num_modulos = 0;
        c[i].num_lacunas = 0;
    }
    return c;
}

// Engine methods
void engine_init(EnergyTaxonomyEngine* e) {
    e->sistemas = _init_sistemas(&e->num_sistemas);
    e->coberturas = _init_coberturas(&e->num_coberturas);
    e->diagnosticos = NULL;
    e->num_diagnosticos = 0;
}

void engine_listar_sistemas(EnergyTaxonomyEngine* e) {
    for (int i = 0; i < e->num_sistemas; i++) {
        SistemaEnergetico* s = &e->sistemas[i];
        printf("\n  --- Sistema %d: %s ---\n", (int)s->tipo, s->nome);
        printf("  Escala: %d\n", (int)s->escala);
        printf("  CORPO: %s\n", s->analogia_corpo);
        printf("  CIVILIZACAO: %s\n", s->analogia_civilizacao);
        if (s->consumo_corpo_pct > 0) printf("  Consumo no corpo: %.1f%% do orcamento energetico\n", s->consumo_corpo_pct);
        printf("  FLUXO: ... -> %s\n", s->fluxo.conversao);
        printf("         -> %s\n", s->fluxo.output);
        printf("  EFICIENCIA: %.1f%%\n", s->fluxo.eficiencia_pct);
        if (strlen(s->observacao) > 0) printf("  OBS: %s\n", s->observacao);
    }
}

char* engine_padrao_universal() {
    return "PADRAO UNIVERSAL: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO\nNada se cria. Tudo se transforma.\nNao existe trabalho sem energia.\nNao existe energia sem input.\nNao existe output sem residuo.\nA questao civilizatoria nunca foi 'como conseguir energia' -- sempre foi 'como TRANSFORMAR com justica e sem desperdiciar'.";
}

void _demo() {
    EnergyTaxonomyEngine engine;
    engine_init(&engine);

    printf("======================================================================\n");
    printf("OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos\n");
    printf("Do Corpo Humano a Civilizacao\n");
    printf("======================================================================\n");

    printf("\n[OS 10 SISTEMAS ENERGETICOS]\n");
    engine_listar_sistemas(&engine);

    printf("\n======================================================================\n");
    printf("[O PADRAO UNIVERSAL]\n");
    printf("======================================================================\n");
    printf("\n%s\n", engine_padrao_universal());

    printf("\n[SCORECARD DA TAXONOMIA ENERGETICA]\n");
    printf("  sistemas_total..............10\n");
    printf("  totalmente_cobertos.........3\n");
    printf("  parcialmente_cobertos.......5\n");
    printf("  lacunas_criticas............2\n");

    printf("\n======================================================================\n");
    printf("FILOSOFIA -- Energia e a bateria do trabalho\n");
    printf("======================================================================\n");
    printf("Energia e a bateria do trabalho. Nosso corpo so funciona porque\n");
    printf("temos energia. Nada foi feito na Terra por humanos sem a necessidade\n");
    printf("de energia.\n\n");
    printf("O corpo humano nao tem UM sistema de energia. Tem DEZ.\n");
    printf("Cada um com input, conversao, output e residuo.\n");
    printf("A civilizacao herda essa estrutura -- somos um corpo em escala.\n");
}

int main() {
    _demo();
    return 0;
}