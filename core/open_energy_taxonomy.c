/********************************************************************************
 * OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos do Corpo e da Civilizacao
 * Energia e a bateria do trabalho. Nada foi feito na Terra por humanos
 * sem a necessidade de energia.
 *
 * O corpo humano nao tem UM sistema de energia. Tem DEZ.
 * Cada um com input, conversao, output e residuo.
 * A civilizacao herda essa estrutura.
 *
 * A LEI QUE PERMEIA TODOS OS 10:
 *   INPUT -> CONVERSAO -> OUTPUT -> RESIDUO
 *   Nada se cria. Tudo se transforma.
 * Author: OpenRepublic Team
 *******************************************************************************/
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

// ============================================================================
// 1. ENUMS
// ============================================================================

typedef enum {
    ENERGIA_CELULAR,  // Energia Celular (mitocondrial)
    ENERGIA_MECANICA,  // Energia Mecanica (muscular)
    ENERGIA_TERMICA,  // Energia Termica (metabolica)
    ENERGIA_NEURAL,  // Energia Neural (sinal)
    ENERGIA_QUIMICA,  // Energia Quimica (sintese)
    ENERGIA_SENSORIAL,  // Energia Sensorial (transducao)
    ENERGIA_COGNITIVA,  // Energia Cognitiva (processamento)
    ENERGIA_ATENCIONAL,  // Energia Atencional (foco)
    ENERGIA_EMOCIONAL,  // Energia Emocional (motivacao)
    ENERGIA_RELACIONAL  // Energia Relacional (social)
} TipoEnergia;

static const char* tipo_energia_id[] = {
    "celular",
    "mecanica",
    "termica",
    "neural",
    "quimica",
    "sensorial",
    "cognitiva",
    "atencional",
    "emocional",
    "relacional",
};

static const char* tipo_energia_rotulo[] = {
    "Energia Celular (mitocondrial)",
    "Energia Mecanica (muscular)",
    "Energia Termica (metabolica)",
    "Energia Neural (sinal)",
    "Energia Quimica (sintese)",
    "Energia Sensorial (transducao)",
    "Energia Cognitiva (processamento)",
    "Energia Atencional (foco)",
    "Energia Emocional (motivacao)",
    "Energia Relacional (social)",
};

typedef enum {
    ESCALA_CORPO,  // Nivel do corpo individual
    ESCALA_COMUNIDADE,  // Nivel da comunidade/local
    ESCALA_CIVILIZACAO,  // Nivel da civilizacao/global
    ESCALA_PLANETA  // Nivel planetario/biosfera
} EscalaEnergia;

static const char* escala_rotulo[] = {
    "Nivel do corpo individual",
    "Nivel da comunidade/local",
    "Nivel da civilizacao/global",
    "Nivel planetario/biosfera",
};

typedef enum {
    DISP_ABUNDANTE,  // Abundante: excedente para doar
    DISP_EQUILIBRADA,  // Equilibrada: cobre a demanda
    DISP_LIMITADA,  // Limitada: alocacao necessaria
    DISP_CRITICA,  // Critica: deficit, intervene
    DISP_DEPLETADA  // Depletada: esgotada, recuperacao obrigatoria
} StatusDisponibilidade;

typedef enum {
    COBERTURA_COBERTO,  // Totalmente coberto por modulo(s) existente(s)
    COBERTURA_PARCIAL,  // Parcialmente coberto -- lacunas identificadas
    COBERTURA_LACUNA,  // Lacuna: nenhum modulo cobre este tipo
    COBERTURA_NAO_APLICAVEL  // Nao aplicavel (conceitual)
} NivelCobertura;

typedef enum {
    INPUT_ALIMENTO,  // Alimento/caloria (comida, combustivel)
    INPUT_OXIGENIO,  // Oxigenio/ar
    INPUT_LUZ,  // Luz/fotons
    INPUT_SOM,  // Som/vibracao
    INPUT_CALOR,  // Calor ambiental
    INPUT_PRESENCA,  // Presenca de outro ser humano
    INPUT_INFORMACAO,  // Informacao/dados
    INPUT_SONO,  // Sono/descanso
    INPUT_MOVIMENTO,  // Movimento do proprio corpo
    INPUT_VENTO_AGUA  // Vento, agua, forcas naturais
} TipoInput;

static const char* input_rotulo[] = {
    "Alimento/caloria (comida, combustivel)",
    "Oxigenio/ar",
    "Luz/fotons",
    "Som/vibracao",
    "Calor ambiental",
    "Presenca de outro ser humano",
    "Informacao/dados",
    "Sono/descanso",
    "Movimento do proprio corpo",
    "Vento, agua, forcas naturais",
};

typedef enum {
    RESIDUO_CALOR,  // Calor dissipado
    RESIDUO_CO2,  // CO2 / gases de exaustao
    RESIDUO_CANSACO_FISICO,  // Cansaco fisico / acido latico
    RESIDUO_FADIGA_MENTAL,  // Fadiga mental / saturacao
    RESIDUO_DESGASTE,  // Desgaste material (atriito, envelhecimento)
    RESIDUO_RUIDO,  // Ruido (sonoro, visual, informational)
    RESIDUO_SOLIDAO,  // Solidao (quando a conexao termina)
    RESIDUO_RESIDUO_TOXICO,  // Residuo toxico (quimico, radiativo)
    RESIDUO_DADOS_DESCARTADOS  // Dados descartados (log, cache)
} TipoResiduo;

static const char* residuo_rotulo[] = {
    "Calor dissipado",
    "CO2 / gases de exaustao",
    "Cansaco fisico / acido latico",
    "Fadiga mental / saturacao",
    "Desgaste material (atriito, envelhecimento)",
    "Ruido (sonoro, visual, informational)",
    "Solidao (quando a conexao termina)",
    "Residuo toxico (quimico, radiativo)",
    "Dados descartados (log, cache)",
};

// ============================================================================
// 2. STRUCTS
// ============================================================================

typedef struct {
    TipoEnergia tipo;
    const char* nome;
    const char* analogia_corpo;
    const char* analogia_civilizacao;
    EscalaEnergia escala;
    const char* conversao;
    const char* output;
    float eficiencia_pct;
    float consumo_corpo_pct;
    const char* observacao;
} SistemaEnergetico;

typedef struct {
    TipoEnergia tipo;
    NivelCobertura nivel;
    const char* modulos;
    const char* lacunas;
} CoberturaRepublica;

// ============================================================================
// 3. DADOS: OS 10 SISTEMAS
// ============================================================================

static SistemaEnergetico sistemas[10] = {
    {
        .tipo = ENERGIA_CELULAR,
        .nome = "Mitocondrial",
        .analogia_corpo = "Mitocondrias convertem glicose + oxigenio em ATP. ATP e a MOEDA energetica da celula -- todo trabalho celular paga em ATP. Sem ATP, a celula morre em segundos.",
        .analogia_civilizacao = "A rede eletrica. A tomada e o ATP da civilizacao. Todo aparelho, toda maquina, todo servo consome eletricidade. OpenEnergy cobre este sistema.",
        .escala = ESCALA_CIVILIZACAO,
        .conversao = "Glicose + O2 -> ATP (fosforilacao oxidativa)",
        .output = "ATP (trifosfato de adenosina) / Eletricidade",
        .eficiencia_pct = 40.0f,
        .consumo_corpo_pct = 0.0f,
        .observacao = "Sistema base. Todos os outros dependem deste. OpenEnergy = cobertura total deste nivel.",
    },
    {
        .tipo = ENERGIA_MECANICA,
        .nome = "Muscular / Motora",
        .analogia_corpo = "ATP -> miosina/actina -> contracao muscular -> MOVIMENTO. O corpo faz TRABALHO FISICO sobre o mundo. Cada passo, cada gesto, cada levantamento de peso.",
        .analogia_civilizacao = "Transporte, maquinas, ferramentas, robos. O motor de carro, o braco robotico, a bicicleta. Todo trabalho fisico ja existiu como energia muscular antes de ser externalizado para maquinas.",
        .escala = ESCALA_CIVILIZACAO,
        .conversao = "ATP -> forca mecanica (contracao / combustao / eletricidade)",
        .output = "Movimento, forca, deslocamento",
        .eficiencia_pct = 25.0f,
        .consumo_corpo_pct = 30.0f,
        .observacao = "OpenAthlete cobre o lado humano (esporte, treino). Transporte publico (OpenMobility) cobre o lado civilizacional.",
    },
    {
        .tipo = ENERGIA_TERMICA,
        .nome = "Metabolica / Calorica",
        .analogia_corpo = "O metabolismo produz calor como subproduto. O corpo GASTA energia mantendo 36,5C -- termorregulacao. Tremer de frio e gerar calor muscular. Suar e dissipar.",
        .analogia_civilizacao = "Aquecimento, cozimento, refrigeracao. O FOGO foi a primeira energia externa que o humano dominou (1 milhao de anos antes da eletricidade). Cozinhar e PRE-DIGERIR com energia termica externa -- libera energia celular que iria pra digestao.",
        .escala = ESCALA_CIVILIZACAO,
        .conversao = "Metabolismo / combustao / compressao -> calor",
        .output = "Calor (manutencao de temperatura / cozimento)",
        .eficiencia_pct = 60.0f,
        .consumo_corpo_pct = 50.0f,
        .observacao = "Metabolismo basal: 50% do gasto energetico do corpo em repouso e so para manter a temperatura. O cozimento de alimentos foi a REVOLUCAO ENERGETICA original da humanidade.",
    },
    {
        .tipo = ENERGIA_NEURAL,
        .nome = "Sistema Nervoso / Comunicacao",
        .analogia_corpo = "Neuronios disparam potenciais de acao -- sinais eletricos. O corpo tem uma REDE de comunicacao interna (87 bilhoes de neuronios). Consome 20W, incrivelmente eficiente. O cerebro pesa 2% do corpo mas consome 20% da energia.",
        .analogia_civilizacao = "Internet, telecomunicacoes, radio. A internet e o SISTEMA NERVO da civilizacao. Cada mensagem, cada video, cada chamada e um potencial de acao em escala planetaria. Banda = largura de axonio.",
        .escala = ESCALA_PLANETA,
        .conversao = "Sinal eletrico / optico -> transmissao",
        .output = "Comunicacao / sinal / dados transmitidos",
        .eficiencia_pct = 35.0f,
        .consumo_corpo_pct = 20.0f,
        .observacao = "LACUNA CRITICA: a Republica NAO tem OpenNetwork/OpenInternet. Quem controla a rede controla o sistema nervoso. Banda gratuita e NECESSARIA (energia neural = direito).",
    },
    {
        .tipo = ENERGIA_QUIMICA,
        .nome = "Sintese / Ligacoes",
        .analogia_corpo = "O corpo SINTETIZA moleculas -- proteinas, hormonios, enzimas. Ligacoes quimicas ARMAZENAM energia. Digestao = quebrar ligacoes para liberar. Sintese = gastar energia para construir.",
        .analogia_civilizacao = "Industria quimica, baterias, combustiveis, farmacia. Toda manufatura e energia quimica direcionada. FarmLab opera aqui -- sintese de medicamentos e energia quimica a servico da vida.",
        .escala = ESCALA_CIVILIZACAO,
        .conversao = "Reacao quimica (sintese / decomposicao)",
        .output = "Moleculas / materiais / medicamentos",
        .eficiencia_pct = 30.0f,
        .consumo_corpo_pct = 10.0f,
        .observacao = "FarmLab cobre farmacia. OpenChemistry cobre industria quimica.",
    },
    {
        .tipo = ENERGIA_SENSORIAL,
        .nome = "Transducao / Percepcao",
        .analogia_corpo = "Olhos capturam FOTONS. Ouvidos capturam VIBRACOES. Pele captura CALOR. O corpo e um RECEPTOR de energia -- converte formas externas em sinais internos. Cada sentido e um TRANSDUTOR energetico.",
        .analogia_civilizacao = "Cameras, microfones, sensores, instrumentos cientificos. OpenTelefonista opera aqui -- o smartphone como CORPO ESTENDIDO captura energia do ambiente (luz, som, posicao) e converte em percepcao. Cego ve obstaculos. Surdo le labios.",
        .escala = ESCALA_CORPO,
        .conversao = "Transducao sensorial (foton/fonon -> sinal neural)",
        .output = "Percepcao / dados sensoriais",
        .eficiencia_pct = 70.0f,
        .consumo_corpo_pct = 5.0f,
        .observacao = "OpenTelefonista cobre (smartphone como corpo estendido). OpenInclusiveHardware (44 dispositivos) amplia. OpenInclusiveIDE integra para desenvolvimento.",
    },
    {
        .tipo = ENERGIA_COGNITIVA,
        .nome = "Cerebro / Processamento",
        .analogia_corpo = "O cerebro CONSOME 20% da energia do corpo pesando 2%. PENSAR E CARO energeticamente. O cansaco mental e real -- e gasto energetico, nao frescura. Resolver um problema matematico gasta mais glicose que assistir TV.",
        .analogia_civilizacao = "Computacao, IA, analise de dados. Um data center consome tanta energia quanto uma cidade. Processar informacao TEM CUSTO ENERGETICO -- nao e gratuito. P8: IA amplifica inteligencia humana, NAO substitui. Mas o custo de computar e REAL e precisa alocacao.",
        .escala = ESCALA_CIVILIZACAO,
        .conversao = "Processamento (neural / digital)",
        .output = "Decisao / calculo / conhecimento",
        .eficiencia_pct = 15.0f,
        .consumo_corpo_pct = 20.0f,
        .observacao = "HumanKnowledge (multi-AI + verificacao) cobre parcialmente. P8 define o principio (IA = instrumento). Custo computacional como recurso a alocar = LACUNA.",
    },
    {
        .tipo = ENERGIA_ATENCIONAL,
        .nome = "Foco / Atencao",
        .analogia_corpo = "A atencao e FINITA. Voce nao consegue focar em tudo. Focar GASTA energia cognitiva. O cerebro tem um BUDGET de atencao -- distribui entre tarefas. Dormir mal = budget de atencao menor no dia seguinte.",
        .analogia_civilizacao = "A energia que FocusGuard protege. O scroll infinito DRENA energia atencional. A 'economia da atencao' e a forma mais NOVA de exploracao energetica -- plataformas capturam sua atencao e vendem. P8 exige proteger esta energia. AntiSpamCall protege parcialmente.",
        .escala = ESCALA_CORPO,
        .conversao = "Filtro atencional (top-down + bottom-up)",
        .output = "Foco / atencao direcionada",
        .eficiencia_pct = 10.0f,
        .consumo_corpo_pct = 0.0f,
        .observacao = "FocusGuard (overlay IDE) cobre parcialmente. AntiSpamCall ('para de me encher o saco') protege. OpenContentPolicy (midia, ruido) protege. Politica mais ampla de atencao como recurso = LACUNA.",
    },
    {
        .tipo = ENERGIA_EMOCIONAL,
        .nome = "Motivacao / Drive",
        .analogia_corpo = "Motivacao, drive, vontade. Em termos fisicos: dopamina, noradrenalina, cortisol -- moleculas que MODULAM quanto de outras energias o corpo vai despender. Sem dopamina, o corpo tem ATP mas nao se MOVE. A depressao e crise energetica emocional -- o combustivel existe, mas o motor nao liga.",
        .analogia_civilizacao = "O kaizen (1% ao dia) opera aqui. Curiosidade, progresso, desafio, recompensa, pertencimento -- os 5 gatilhos psicologicos sao GERADORES de energia emocional. O Huxley soma (dopamina artificial do scroll) e o SEQUESTRO desta energia -- drena ao inves de gerar.",
        .escala = ESCALA_COMUNIDADE,
        .conversao = "Modulacao neuroquimica (dopamina/serotonina/cortisol)",
        .output = "Motivacao / drive / vontade de agir",
        .eficiencia_pct = 20.0f,
        .consumo_corpo_pct = 0.0f,
        .observacao = "LACUNA CRITICA: nenhum modulo trata saude mental como INFRAESTRUTURA ENERGETICA. Depressao = deficit energetico. Burnout = deplecao. Kaizen e gerador, mas falta sistema.",
    },
    {
        .tipo = ENERGIA_RELACIONAL,
        .nome = "Social / Conexao",
        .analogia_corpo = "O ser humano isolado DEGRADA. Solidao cronica aumenta mortalidade em 26%. O corpo PRECISA de conexao para funcionar bem -- nao e luxo, e necessidade energetica. Oxitocina, espelhamento neural, co-regulacao.",
        .analogia_civilizacao = "A assembleia, o mutirao, a cooperativa. O Two-Person Rule nao e so procedimento -- e ARQUITETURA ENERGETICA. Duas pessoas juntas fazem mais que duas separadas. A energia social e SINERGICA: 1+1 > 2. Quando a assembleia polariza (P9), e esta energia que se GASTA em atrito em vez de gerar valor.",
        .escala = ESCALA_COMUNIDADE,
        .conversao = "Co-regulacao neuroquimica + espelhamento neural",
        .output = "Cooperacao / sinergia / vinculo",
        .eficiencia_pct = 80.0f,
        .consumo_corpo_pct = 0.0f,
        .observacao = "OpenCommunities (6 adaptacoes) cobre parcialmente. OpenConstituentAssembly (governanca) cobre parcialmente. OpenCrowdsourcing (ajuda mutua) cobre parcialmente. P9 (anti-polarizacao) PROTEGE esta energia. Tratar conexao como recurso energetico mensuravel = LACUNA.",
    },
};

// ============================================================================
// 4. DADOS: COBERTURAS
// ============================================================================

static CoberturaRepublica coberturas_data[10] = {
    {
        .tipo = ENERGIA_CELULAR,
        .nivel = COBERTURA_COBERTO,
        .modulos = "open-energy; open-agrarian-revolution; open-credit",
        .lacunas = "",
    },
    {
        .tipo = ENERGIA_MECANICA,
        .nivel = COBERTURA_PARCIAL,
        .modulos = "open-athlete; open-martial-arts",
        .lacunas = "sistema de transporte publico gratuito (OpenMobility)",
    },
    {
        .tipo = ENERGIA_TERMICA,
        .nivel = COBERTURA_PARCIAL,
        .modulos = "open-energy",
        .lacunas = "politica de cozimento comunitario; aquecimento como direito",
    },
    {
        .tipo = ENERGIA_NEURAL,
        .nivel = COBERTURA_LACUNA,
        .modulos = "",
        .lacunas = "OpenNetwork/OpenInternet -- banda gratuita como direito; sistema nervoso da civilizacao sem dono; neutralidade de rede como P1 (anti-elitismo)",
    },
    {
        .tipo = ENERGIA_QUIMICA,
        .nivel = COBERTURA_PARCIAL,
        .modulos = "open-chemistry; open-physics",
        .lacunas = "FarmLab completo (sintese CC0 de medicamentos)",
    },
    {
        .tipo = ENERGIA_SENSORIAL,
        .nivel = COBERTURA_COBERTO,
        .modulos = "open-telefonista; open-inclusive-hardware; open-inclusive-ide",
        .lacunas = "",
    },
    {
        .tipo = ENERGIA_COGNITIVA,
        .nivel = COBERTURA_PARCIAL,
        .modulos = "open-human-knowledge; open-human-amplification",
        .lacunas = "alocacao de custo computacional como recurso energetico",
    },
    {
        .tipo = ENERGIA_ATENCIONAL,
        .nivel = COBERTURA_PARCIAL,
        .modulos = "open-focus-guard; open-anti-spam-call; open-content-policy",
        .lacunas = "politica ampla de atencao como recurso energetico finito",
    },
    {
        .tipo = ENERGIA_EMOCIONAL,
        .nivel = COBERTURA_LACUNA,
        .modulos = "",
        .lacunas = "OpenMentalHealth -- saude mental como INFRAESTRUTURA ENERGETICA; sistema de deteccao de deplecao emocional (burnout/depressao); geradores de energia emocional (kaizen, pertencimento, proposito)",
    },
    {
        .tipo = ENERGIA_RELACIONAL,
        .nivel = COBERTURA_PARCIAL,
        .modulos = "open-communities; open-constituent-assembly; open-anti-polarization",
        .lacunas = "conexao como recurso energetico mensuravel e protegido",
    },
};

// ============================================================================
// 5. FUNCOES AUXILIARES
// ============================================================================

static const char* nivel_cobertura_str(NivelCobertura n) {
    switch(n) {
        case COBERTURA_COBERTO: return "OK";
        case COBERTURA_PARCIAL: return "PARCIAL";
        case COBERTURA_LACUNA: return "LACUNA";
        case COBERTURA_NAO_APLICAVEL: return "N/A";
        default: return "?";
    }
}

static const char* disp_str(StatusDisponibilidade d) {
    switch(d) {
        case DISP_ABUNDANTE: return "abundante";
        case DISP_EQUILIBRADA: return "equilibrada";
        case DISP_LIMITADA: return "limitada";
        case DISP_CRITICA: return "critica";
        case DISP_DEPLETADA: return "depletada";
        default: return "?";
    }
}

// ============================================================================
// 6. DEMO
// ============================================================================

int main(void) {
    printf("======================================================================\n");
    printf("OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos\n");
    printf("Do Corpo Humano a Civilizacao\n");
    printf("======================================================================\n");

    // OS 10 SISTEMAS
    printf("\n[OS 10 SISTEMAS ENERGETICOS]\n");
    for (int i = 0; i < 10; i++) {
        SistemaEnergetico* s = &sistemas[i];
        printf("\n  --- Sistema %d: %s ---\n", i+1, tipo_energia_rotulo[i]);
        printf("  Escala: %s\n", escala_rotulo[s->escala]);
        printf("  CORPO: %s\n", s->analogia_corpo);
        printf("  CIVILIZACAO: %s\n", s->analogia_civilizacao);
        if (s->consumo_corpo_pct > 0)
            printf("  Consumo no corpo: %.0f%% do orcamento energetico\n", s->consumo_corpo_pct);
        printf("  CONVERSAO: %s\n", s->conversao);
        printf("  OUTPUT: %s\n", s->output);
        printf("  EFICIENCIA: %.0f%%\n", s->eficiencia_pct);
        if (strlen(s->observacao) > 0)
            printf("  OBS: %s\n", s->observacao);
    }

    // PADRAO UNIVERSAL
    printf("\n======================================================================\n");
    printf("[O PADRAO UNIVERSAL]\n");
    printf("======================================================================\n");
    printf("\nPADRAO UNIVERSAL: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO\n");
    printf("Nada se cria. Tudo se transforma.\n");
    printf("Nao existe trabalho sem energia.\n");
    printf("Nao existe energia sem input.\n");
    printf("Nao existe output sem residuo.\n");
    printf("A questao civilizatoria nunca foi 'como conseguir energia' ");
    printf("-- sempre foi 'como TRANSFORMAR com justica e sem desperdicar'.\n");

    // COBERTURA DA REPUBLICA
    printf("\n======================================================================\n");
    printf("[COBERTURA DA REPUBLICA -- O QUE FALTA]\n");
    printf("======================================================================\n");
    for (int i = 0; i < 10; i++) {
        CoberturaRepublica* c2 = &coberturas_data[i];
        printf("\n  [%s] %s\n", nivel_cobertura_str(c2->nivel), tipo_energia_rotulo[i]);
        if (strlen(c2->modulos) > 0)
            printf("  Modulos: %s\n", c2->modulos);
        if (strlen(c2->lacunas) > 0)
            printf("  LACUNAS: %s\n", c2->lacunas);
    }

    // SCORECARD
    int cobertos = 0, parciais = 0, lacunas = 0;
    for (int i = 0; i < 10; i++) {
        if (coberturas_data[i].nivel == COBERTURA_COBERTO) cobertos++;
        else if (coberturas_data[i].nivel == COBERTURA_PARCIAL) parciais++;
        else if (coberturas_data[i].nivel == COBERTURA_LACUNA) lacunas++;
    }
    printf("\n======================================================================\n");
    printf("[SCORECARD DA TAXONOMIA ENERGETICA]\n");
    printf("======================================================================\n");
    printf("  sistemas_total................ 10\n");
    printf("  totalmente_cobertos........... %d\n", cobertos);
    printf("  parcialmente_cobertos......... %d\n", parciais);
    printf("  lacunas_criticas.............. %d\n", lacunas);
    printf("  pct_cobertura................. %.1f%%\n", (float)cobertos / 10.0f * 100.0f);

    // FILOSOFIA
    printf("\n======================================================================\n");
    printf("FILOSOFIA -- Energia e a bateria do trabalho\n");
    printf("======================================================================\n");
    printf("\n");
    printf("\"Energia e a bateria do trabalho. Nosso corpo so funciona porque\n");
    printf("temos energia. Nada foi feito na Terra por humanos sem a necessidade\n");
    printf("de energia.\"\n");
    printf("\n");
    printf("O corpo humano nao tem UM sistema de energia. Tem DEZ.\n");
    printf("Cada um com input, conversao, output e residuo.\n");
    printf("A civilizacao herda essa estrutura -- somos um corpo em escala.\n");
    printf("\n");
    printf("NEURAL (sistema nervoso = internet):\n");
    printf("  Quem controla a rede controla o sistema nervoso da civilizacao.\n");
    printf("  Banda gratuita e NECESSARIA. A internet e o nervo. Sem nervo, paralisia.\n");
    printf("\n");
    printf("ATENCIONAL (foco = atencao finita):\n");
    printf("  A atencao e o recurso mais explorado do seculo XXI.\n");
    printf("  Plataformas capturam sua atencao e vendem. Isso e EXTRATIVISMO ENERGETICO.\n");
    printf("\n");
    printf("EMOCIONAL (motivacao = drive):\n");
    printf("  Depressao e CRISE ENERGETICA. O combustivel existe (ATP), mas o motor\n");
    printf("  nao liga (sem dopamina). Saude mental nao e luxo terapeutico --\n");
    printf("  e INFRAESTRUTURA ENERGETICA. Sem motivacao, nenhuma outra energia se move.\n");
    printf("\n");
    printf("A LEI DE TODOS OS 10:\n");
    printf("  INPUT -> CONVERSAO -> OUTPUT -> RESIDUO.\n");
    printf("  Nada se cria, tudo se transforma.\n");
    printf("  A Republica nao cria energia. TRANSFORMA.\n");
    printf("  E transforma COM JUSTICA: sem desperdicio, sem exclusao.\n");

    return 0;
}
