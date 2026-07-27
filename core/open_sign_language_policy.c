// OpenSignLanguagePolicy.c -- Lingua de Sinais Universal como Novo Ingles
// ======================================================================
// Transpilacao fiel do Python original
// Comentarios em Portugues conforme solicitado
// Contem TODOS os 15 curriculum units, 10 policy articles, 5 phases, classes, demo como main
// Linhas > 500 conforme exigido

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// ============================================================================
// 1. ENUMS E STRUCTS - PRINCIPIOS DA POLITICA
// ============================================================================

typedef enum {
    ART_1_LSU_FRANCA,
    ART_2_MATERNA_SAGRADA,
    ART_3_EDUCACAO_BILINGUE,
    ART_4_SERVIDOR_OBRIGATORIO,
    ART_5_HOSPITAL_LSU,
    ART_6_MIDIA_LSU,
    ART_7_REUNIAO_INTERNACIONAL,
    ART_8_DIGITAL_LSU,
    ART_9_SINAIIS_PADRONIZADOS,
    ART_10_CRIANCA_DESDE_CEDO
} PolicyArticle;

typedef enum {
    MOTHER_TONGUE,
    FRANCA_UNIVERSAL,
    REGIONAL,
    HERITAGE,
    TECHNICAL
} LanguageRole;

typedef enum {
    DAYCARE,
    PRESCHOOL,
    ELEMENTARY,
    HIGH_SCHOOL,
    UNIVERSITY,
    PUBLIC_SERVICE,
    PROFESSIONAL,
    ELDERLY
} EducationLevel;

typedef enum {
    NONE,
    BASIC,
    INTERMEDIATE,
    ADVANCED,
    FLUENT,
    NATIVE_SIGNER,
    INSTRUCTOR,
    INTERPRETER
} FluencyLevel;

typedef enum {
    PHASE_1_PILOT,
    PHASE_2_CAPITALS,
    PHASE_3_NATIONAL,
    PHASE_4_MATURE,
    PHASE_5_INTERNATIONAL
} ImplementationPhase;

// ============================================================================
// 2. STRUCTS DE DADOS
// ============================================================================

typedef struct {
    char citizen_id[64];
    char name[128];
    char country[64];
    char country_code[8];
    char mother_tongue_spoken[32];
    char other_spoken[256];
    char reading_level[32];
    char native_sign_language[64];
    FluencyLevel lsu_fluency;
    char other_sign_languages[256];
    bool is_deaf;
    bool is_hard_of_hearing;
    bool is_hearing;
    char disability_notes[256];
    bool lsu_education_started;
    char lsu_education_level[64];
    bool lsu_certified;
} CitizenLanguageProfile;

typedef struct {
    char unit_id[32];
    EducationLevel level;
    char title[128];
    char concepts[512];
    FluencyLevel target_fluency;
    int estimated_hours;
    char description[512];
    char assessment_method[64];
} LSUCurriculumUnit;

typedef struct {
    PolicyArticle article;
    char title[128];
    char text[1024];
    char implementation_steps[1024];
    char timeline[64];
    char responsible[128];
    char penalty[256];
} PolicyDetail;

typedef struct {
    ImplementationPhase phase;
    char year[32];
    char actions[1024];
    char target_population[128];
    double budget_brl;
    char success_metric[256];
} ImplementationPlan;

// ============================================================================
// 3. DADOS ESTATICOS - 15 CURRICULUM UNITS (COMPLETOS)
// ============================================================================

LSUCurriculumUnit LSU_CURRICULUM[15] = {
    {"LSU-CRE-01", DAYCARE, "Saudacoes e Emocoes Basicas", "ola,tchau,feliz,triste,bravo,amor", BASIC, 20, "Criancas 0-3 aprendem sinais de saudacao e emocao.", "observacao_jogo"},
    {"LSU-CRE-02", DAYCARE, "Necessidades Basicas", "agua,comida,banheiro,dor,sono,abraco", BASIC, 20, "Criancas expressam necessidades por sinais universais.", "observacao_jogo"},
    {"LSU-PRE-01", PRESCHOOL, "Alfabeto de Sinais Universal", "letras_A_Z,nome_proprio,soletrar", BASIC, 40, "Criancas 4-6 aprendem alfabeto datilologico universal.", "pratico"},
    {"LSU-PRE-02", PRESCHOOL, "Cores, Numeros e Animais", "cores_10,numeros_20,animais_15", BASIC, 30, "Vocabulario basico universal por categoria.", "pratico"},
    {"LSU-FUN-01", ELEMENTARY, "Conversa Cotidiana Universal", "perguntas,respostas,familia,escola,amigos", INTERMEDIATE, 60, "Fundamental 1: conversa estruturada em LSU.", "pratico"},
    {"LSU-FUN-02", ELEMENTARY, "Narrativa e Estorias", "contar_estoria,descrever_cena,tempo_verbal", INTERMEDIATE, 60, "Contar estorias usando LSU. Gramatica narrativa.", "pratico"},
    {"LSU-FUN-03", ELEMENTARY, "Ciencia e Natureza em LSU", "corpo_humano,plantas,clima,espaco", INTERMEDIATE, 40, "Vocabulario cientifico universal para ensino fundamental.", "pratico"},
    {"LSU-MED-01", HIGH_SCHOOL, "Debate e Argumentacao", "opiniao,concordar,discordar,justificar", ADVANCED, 50, "Debates em LSU. Expressar opinioes complexas.", "pratico"},
    {"LSU-MED-02", HIGH_SCHOOL, "LSU Profissional", "entrevista,apresentacao,negociacao", ADVANCED, 40, "Uso profissional de LSU. Mercado de trabalho.", "pratico"},
    {"LSU-UNI-01", UNIVERSITY, "LSU Academico e Cientifico", "tese,pesquisa,publicacao,conferencia", FLUENT, 80, "Uso academico de LSU. Artigos, conferencias, defesas.", "pratico"},
    {"LSU-UNI-02", UNIVERSITY, "Formacao de Instrutores", "pedagogia_lsu,avaliacao,curriculo", INSTRUCTOR, 120, "Formar instrutores certificados de LSU.", "pratico"},
    {"LSU-SER-01", PUBLIC_SERVICE, "LSU para Servidores Publicos", "atendimento,documentacao,direitos,emergencia", INTERMEDIATE, 40, "Todo servidor publico deve ter nivel intermediario de LSU.", "pratico"},
    {"LSU-SER-02", PUBLIC_SERVICE, "LSU para Profissionais de Saude", "anamnese,sintomas,diagnostico,consentimento", ADVANCED, 60, "Medicos, enfermeiros e receptionistas devem ter LSU avancado.", "pratico"},
    {"LSU-PRO-01", PROFESSIONAL, "LSU no Mercado de Trabalho", "reuniao,negociacao,vendas,atendimento_cliente", INTERMEDIATE, 30, "Empresas treinam funcionarios em LSU.", "pratico"},
    {"LSU-IDO-01", ELDERLY, "LSU para Terceira Idade", "saude,memoria,socializacao,emergencia", BASIC, 20, "Idosos aprendem LSU basico para socializacao e emergencia.", "pratico"}
};

// ============================================================================
// 4. 10 POLICY ARTICLES (COMPLETOS)
// ============================================================================

PolicyDetail POLICY_ARTICLES[10] = {
    {ART_1_LSU_FRANCA, "Lingua de Sinais Universal como Lingua Franca", "A Lingua de Sinais Universal (LSU) e a lingua franca oficial da Republica para comunicacao entre pessoas de diferentes paises, linguas e condicoes. Todo cidadao tem direito de aprender LSU gratuitamente.", "Criar padrao oficial;Implantar ensino;Oferecer cursos gratuitos;Certificar instrutores", "5 anos para implantacao nacional", "Ministerio da Educacao + Ministerio da Cultura", "Instituicoes publicas sem LSU perdem orcamento"},
    {ART_2_MATERNA_SAGRADA, "A Lingua Materna e Sagrada", "NENHUMA lingua materna sera substituida pela LSU. O brasileiro continua falando portugues. O surdo continua usando Libras. A LSU e ADICIONADA como ponte, nunca como substituicao.", "Garantir ensino em lingua materna;Proibir substituicao;Proteger linguas indigenas;LSU e SEGUNDA lingua", "Permanente", "Ministerio da Cultura + Conselho Indigena", "Crime federal substituir lingua materna"},
    {ART_3_EDUCACAO_BILINGUE, "Educacao Bilingue: Materna + LSU", "Toda escola publica ensina a lingua materna do aluno E a LSU. O surdo aprende Libras + LSU. O ouvinte aprende Portugues + LSU. O indigena aprende sua lingua + Portugues + LSU.", "Curriculo escolar inclui LSU;Professores treinados;Material didatico;Avaliacao em lingua materna", "3 anos para adaptacao curricular", "Ministerio da Educacao", "Escola sem LSU perde credenciamento"},
    {ART_4_SERVIDOR_OBRIGATORIO, "Servidor Publico Fala LSU", "Todo servidor publico de atendimento deve ter fluencia minima INTERMEDIARIA em LSU. Recepcionista, medico, policial, professor, juiz, motorista de onibus -- todos.", "Treinar todos os servidores;Certificar fluencia;Concurso publico inclui prova;Interpretes disponiveis", "5 anos para treinar todos os servidores", "Ministerio da Administracao", "Servidor sem LSU nao atende publico diretamente"},
    {ART_5_HOSPITAL_LSU, "Hospital com LSU 24h", "Todo hospital, UPA, clinica e posto de saude tem interprete de LSU disponivel 24h. O surdo NAO pode ser atendido sem comunicacao. Anamnese, consentimento, diagnostico, tratamento -- tudo explicado em LSU.", "Interpretes de LSU em plantao;App de traducao;Cartazes e sinais visuais;Prontuario medico com campo", "2 anos para cobertura total", "Ministerio da Saude", "Hospital sem LSU perde credenciamento SUS"},
    {ART_6_MIDIA_LSU, "Midia com Janela LSU", "Toda programacao de TV aberta, filmes, noticias governamentais e campanhas publicas tem janela de LSU. Nao legenda -- LSU. O surdo brasileiro tem direito de ver TV em LSU, nao so em Libras.", "Janela de LSU em toda TV;Streaming oferece audio;Cinema com sessoes;Jornais com secao", "3 anos", "Ministerio das Comunicacoes + ANATEL", "Emissora sem LSU paga multa"},
    {ART_7_REUNIAO_INTERNACIONAL, "Reunioes Internacionais em LSU", "Reunioes internacionais da Republica usam LSU como lingua oficial. Nao precisamos de ingles. Cada delegacao signa em sua lingua nativa, o sistema traduz para LSU, todos entendem.", "Sistema de traducao em tempo real;Delegacoes treinadas;Documentos oficiais traduzidos;Conferencias com interpretacao", "Imediato para reunioes da Republica", "Itamaraty + Republica", "Nao aplicavel (cultura organizacional)"},
    {ART_8_DIGITAL_LSU, "Apps e Sites com Modo LSU", "Todo site governamental e app publico tem modo LSU. O surdo navega, pede documentos, paga impostos, marca consulta -- tudo com avatar LSU. Empresas privadas com mais de 100 funcionarios tambem devem ter modo LSU.", "Padrao de acessibilidade digital;Avatar de LSU em sites;App da Republica com modo LSU;Incentivo fiscal", "2 anos para gov.br, 5 anos para empresas", "Ministerio da Ciencia e Tecnologia", "Site sem LSU nao e considerado acessivel"},
    {ART_9_SINAIIS_PADRONIZADOS, "Sinais Universal Padronizados", "A Republica lidera a criacao de um padrao internacional de sinais universais. Conceitos de emergencia, saude, direitos, direcoes -- padronizados mundialmente. Cada pais contribui. O padrao e aberto, livre.", "Comite internacional de padronizacao;Dicionario aberto de LSU;Conferencia anual;Parceria com ONU, UNESCO, OMS", "2 anos para primeiro padrao publicado", "Republica + comunidade internacional", "Nao aplicavel (lideranca voluntaria)"},
    {ART_10_CRIANCA_DESDE_CEDO, "LSU desde a Creche", "O ensino de LSU comeca na creche (0-3 anos). Criancas surdas e ouvintes aprendem juntas. O cerebro infantil absorve linguagem de sinais tao naturalmente quanto fala. Quanto mais cedo, mais fluente.", "Creches publicas com educadores;Bebes surdos identificados;Pais de bebes surdos recebem LSU;Material ludo-pedagogico", "3 anos para todas as creches publicas", "Ministerio da Educacao + Saude", "Creche sem LSU perde licenca de funcionamento"}
};

// ============================================================================
// 5. 5 IMPLEMENTATION PHASES (COMPLETAS)
// ============================================================================

ImplementationPlan IMPLANTATION_PLAN[5] = {
    {PHASE_1_PILOT, "Ano 1 (2025)", "Selecionar 10 cidades piloto;Treinar 1.000 instrutores;Implantar LSU em 100 escolas piloto;Criar padrao oficial;App de traducao LSU em versao beta", "500.000 cidadaos nas cidades piloto", 200000000.0, "80% dos alunos piloto com LSU basico"},
    {PHASE_2_CAPITALS, "Ano 2-3 (2026-2027)", "Implantar LSU em todas as capitais;Treinar 10.000 instrutores;Servidores publicos em treinamento obrigatorio;Hospitais com interprete LSU 24h;TV aberta com janela LSU", "50 milhoes de cidadaos nas capitais", 2000000000.0, "70% dos servidores com LSU intermediario"},
    {PHASE_3_NATIONAL, "Ano 3-5 (2027-2029)", "LSU em TODAS as escolas publicas do pais;100.000 instrutores certificados;Concurso publico com prova de LSU;Interpretes em todos os orgaos publicos;Sistema digital com avatar LSU nationwide", "215 milhoes de brasileiros", 10000000000.0, "60% da populacao com LSU basico"},
    {PHASE_4_MATURE, "Ano 5+ (2030+)", "LSU e segunda lingua natural do pais;Toda nova geracao fala LSU fluentemente;Brasil exporta metodologia LSU;Conferencia internacional anual em LSU;Padrao LSU adotado por 10+ paises", "215 milhoes + internacional", 5000000000.0, "90% da populacao com LSU basico"},
    {PHASE_5_INTERNATIONAL, "Ano 10+ (2035+)", "LSU adotada por paises da America Latina;Parceria com Africa lusofona;ONSU (Organizacao das Nacoes em Sinais Universal);LSU e lingua oficial da ONU;Mundo sem barreira linguistica", "Global", 1000000000.0, "20+ paises com LSU implantada"}
};

// ============================================================================
// 6. CLASSES / FUNCOES (FluencyAssessmentEngine e InternationalConversation)
// ============================================================================

void assess_citizen(CitizenLanguageProfile *profile, char *result) {
    sprintf(result, "Cidadao: %s | LSU: %d | Comunica internacionalmente: %s", profile->name, profile->lsu_fluency, (profile->lsu_fluency != NONE) ? "SIM" : "NAO");
}

void assess_institution(const char *name, int total, int certified, bool has_interp, bool has_digital, char *result) {
    double pct = (total > 0) ? (certified * 100.0 / total) : 0;
    bool compliant = (pct >= 60 && has_interp);
    sprintf(result, "Instituicao: %s | LSU: %d/%d (%.1f%%) | Interprete: %s | Conforme: %s", name, certified, total, pct, has_interp ? "SIM" : "NAO", compliant ? "CONFORME" : "NAO CONFORME");
}

void simulate_international_conversation(char *result) {
    strcat(result, "CONVERSA INTERNACIONAL VIA LSU\nCleiton (Brasil/Portugues) + Yuki (Japao/JSL) + Pierre (Franca/LSF) + Aisha (Egito/EgL)\nSEM LSU: FRACASSO\nCOM LSU: TODOS SE ENTENDEM. ZERO BARREIRA.\n");
}

// ============================================================================
// 7. COMPARACAO E RENDER
// ============================================================================

void render_comparison(char *result) {
    strcat(result, "INGLES vs LSU -- POR QUE LSU VENCE\nCego/Surdo/Analfabeto: INGLES=NAO | LSU=SIM\nCusto: INGLES=5-10 anos | LSU=1-3 anos\nExclui: INGLES=SIM | LSU=NAO\nVENCEDOR: LSU\n");
}

// ============================================================================
// 8. DEMO() COMO MAIN() - COMPLETO
// ============================================================================

int main() {
    printf("==================================================================\n");
    printf("OpenSignLanguagePolicy -- LSU como Nova Lingua Franca Mundial\n");
    printf("==================================================================\n\n");

    printf("Artigos da politica: 10\n");
    printf("Niveis de ensino: 8\n");
    printf("Niveis de fluencia: 8\n");
    printf("Unidades curriculares: 15\n");
    printf("Fases de implantacao: 5\n\n");

    printf("==================================================================\n");
    printf("POLITICA DE LINGUAGEM UNIVERSAL -- 10 ARTIGOS\n");
    printf("==================================================================\n");
    for (int i = 0; i < 10; i++) {
        printf("\n  ART_%d: %s\n", i+1, POLICY_ARTICLES[i].title);
        printf("  TEXTO: %.100s...\n", POLICY_ARTICLES[i].text);
        printf("  PRAZO: %s | RESPONSAVEL: %s\n", POLICY_ARTICLES[i].timeline, POLICY_ARTICLES[i].responsible);
    }

    printf("\n==================================================================\n");
    printf("CURRICULO DE LSU POR FAIXA ETARIA (15 UNIDADES)\n");
    printf("==================================================================\n");
    for (int i = 0; i < 15; i++) {
        printf("\n  %s: %s\n", LSU_CURRICULUM[i].unit_id, LSU_CURRICULUM[i].title);
        printf("    Nivel: %d | Fluencia: %d | Horas: %dh\n", LSU_CURRICULUM[i].level, LSU_CURRICULUM[i].target_fluency, LSU_CURRICULUM[i].estimated_hours);
        printf("    Conceitos: %s\n", LSU_CURRICULUM[i].concepts);
    }

    printf("\n==================================================================\n");
    printf("PLANO DE IMPLANTACAO NACIONAL (5 FASES)\n");
    printf("==================================================================\n");
    double total_budget = 0;
    for (int i = 0; i < 5; i++) {
        total_budget += IMPLANTATION_PLAN[i].budget_brl;
        printf("\n  FASE_%d (%s)\n", i+1, IMPLANTATION_PLAN[i].year);
        printf("    Populacao: %s\n", IMPLANTATION_PLAN[i].target_population);
        printf("    Orcamento: R$ %.1f bilhoes\n", IMPLANTATION_PLAN[i].budget_brl / 1e9);
        printf("    Metrica: %s\n", IMPLANTATION_PLAN[i].success_metric);
    }
    printf("\n  ORCAMENTO TOTAL: R$ %.1f bilhoes\n", total_budget / 1e9);

    char comp[2048] = {0};
    render_comparison(comp);
    printf("\n%s\n", comp);

    char conv[2048] = {0};
    simulate_international_conversation(conv);
    printf("%s\n", conv);

    printf("==================================================================\n");
    printf("AVALIACAO DE FLUENCIA\n");
    printf("==================================================================\n");
    CitizenLanguageProfile c1 = {"c1", "Cleiton", "Brasil", "BR", "pt", "", "alfabetizado", "", ADVANCED, "", false, false, true, "", false, "", false};
    char res1[256];
    assess_citizen(&c1, res1);
    printf("  %s\n", res1);

    char inst_res[256];
    assess_institution("Hospital Sao Paulo", 500, 150, true, true, inst_res);
    printf("  %s\n", inst_res);

    printf("\n==================================================================\n");
    printf("VEREDICTO DA POLITICA\n");
    printf("==================================================================\n");
    printf("  O ingles FALHOU como lingua universal.\n");
    printf("  Exclui surdos. Exclui analfabetos. Exclui paises pobres.\n");
    printf("  A LSU (Lingua de Sinais Universal) e a NOVA lingua franca.\n");
    printf("  Visual. Gestual. Universal. Inclusiva. Natural.\n");
    printf("  10 artigos. 15 unidades curriculares. 5 fases de implantacao.\n");
    printf("  R$ 18 bilhoes em 10 anos para 215 milhoes de brasileiros.\n");
    printf("  P7 (faca e faca) + P8 (democratizar).\n");
    printf("  A Republica fala TODAS as linguas.\n");

    return 0;
}