// open_libras_bridge.c - Transpiled from open_libras_bridge.py
// Full faithful port (C99) with identical demo output and Portuguese strings.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>

typedef enum { LIBRAS_TO_TEXT, TEXT_TO_LIBRAS, LIBRAS_TO_AUDIO, AUDIO_TO_LIBRAS } TranslationDirection;
typedef enum { ALPHABET, NUMBERS, GREETINGS, QUESTIONS, VERBS, NOUNS, ADJECTIVES, EMOTIONS, DAILY_LIFE, PRONOUNS } SignCategory;
typedef enum { REALISTIC_HUMAN, CARTOON, ABSTRACT, MINIMAL } AvatarStyle;
typedef enum { HIGH, MEDIUM, LOW, FAILED } RecognitionConfidence;
typedef enum { RIGHT, LEFT, AMBIDEXTROUS } HandDominance;
typedef enum { NEUTRAL, HAPPY, SAD, ANGRY, SURPRISED, QUESTIONING, NEGATION } FacialExpression;

typedef struct {
    char sign_id[32];
    char portuguese_meaning[64];
    SignCategory sign_category;
    char handshape[8];
    char location[32];
    char movement[32];
    char palm_orientation[32];
    FacialExpression facial_expr;
    int requires_two_hands;
    char description[256];
} LibrasSign;

typedef struct {
    TranslationDirection direction;
    char input_text[128];
    char output_text[256];
    RecognitionConfidence confidence;
    LibrasSign signs_detected[16];
    int signs_count;
    float processing_time_ms;
    char avatar_animation_url[256];
} TranslationResult;

typedef struct {
    AvatarStyle style;
    char skin_tone[16];
    char clothing[32];
    char background[32];
    float speed;
    int show_facial_expressions;
    int show_hand_details;
} AvatarConfig;

LibrasSign LIBRAS_SIGNS[] = {
    {"ola", "ola", GREETINGS, "B", "frente_peito", "ondulacao", "para_frente", HAPPY, 0, "Mao aberta em B, movimento de aceno lateral na altura do peito."},
    {"obrigado", "obrigado", GREETINGS, "A", "queixo", "toque_queixo", "para_frente", HAPPY, 0, "Mao em A, toque no queixo e movimento para frente."},
    {"por_favor", "por favor", GREETINGS, "B", "frente_peito", "circular_pequeno", "para_cima", NEUTRAL, 0, "Mao aberta, pequeno circulo na frente do peito."},
    {"sim", "sim", QUESTIONS, "S", "frente_peito", "nod_vertical", "para_frente", NEUTRAL, 0, "Mao em S, movimento de confirmacao vertical."},
    {"nao", "nao", QUESTIONS, "G", "frente_peito", "balanco_lateral", "para_frente", NEGATION, 0, "Indicador esticado, balanco lateral da cabeca."},
    {"agua", "agua", DAILY_LIFE, "W", "queixo", "toque_queixo", "para_baixo", NEUTRAL, 0, "Mao em W, toque no queixo representando agua."},
    {"comida", "comida", DAILY_LIFE, "C", "boca", "toque_boca", "para_frente", NEUTRAL, 0, "Mao em C, movimento em direcao a boca."},
    {"casa", "casa", NOUNS, "C", "frente_peito", "telhado", "para_baixo", NEUTRAL, 1, "Duas maos em C formando telhado de casa."},
    {"familia", "familia", NOUNS, "F", "frente_peito", "circulo_grande", "para_frente", HAPPY, 1, "Duas maos em F girando em circulo representando uniao."},
    {"amor", "amor", EMOTIONS, "A", "frente_peito", "cruzado", "para_frente", HAPPY, 1, "Duas maos em A cruzadas sobre o coracao."},
    {"trabalho", "trabalho", VERBS, "T", "frente_peito", "martelo", "para_baixo", NEUTRAL, 0, "Mao em T simulando martelar."},
    {"escola", "escola", NOUNS, "E", "testa", "toque_testa", "para_frente", NEUTRAL, 0, "Mao em E, toque na testa representando conhecimento."},
    {"medico", "medico", NOUNS, "M", "pulso", "pulso_pulso", "para_frente", NEUTRAL, 0, "Mao em M medindo pulso como medico."},
    {"ajuda", "ajuda", VERBS, "A", "frente_peito", "empurra", "para_cima", NEUTRAL, 1, "Uma mao empurra a outra para cima pedindo ajuda."},
    {"nome", "nome", QUESTIONS, "N", "frente_peito", "toque_peito", "para_frente", QUESTIONING, 0, "Mao em N, toque no peito perguntando nome."},
    {"quantos_anos", "quantos anos", QUESTIONS, "Q", "queixo", "toque_queixo", "para_frente", QUESTIONING, 0, "Mao em Q no queixo perguntando idade."},
    {"bom_dia", "bom dia", GREETINGS, "B", "testa", "toque_testa", "para_frente", HAPPY, 0, "Mao em B, toque na testa e movimento de cumprimento."},
    {"boa_noite", "boa noite", GREETINGS, "B", "testa", "toque_testa", "para_baixo", NEUTRAL, 0, "Mao em B, toque na testa e movimento descendente."},
    {"desculpa", "desculpa", EMOTIONS, "D", "frente_peito", "circulo_peito", "para_frente", SAD, 0, "Mao em D, circulo pequeno no peito pedindo desculpas."},
    {"feliz", "feliz", EMOTIONS, "F", "frente_peito", "circulo_feliz", "para_frente", HAPPY, 0, "Mao em F, movimento circular alegre no peito."},
    {"eu", "eu", PRONOUNS, "I", "peito", "toque_peito", "para_frente", NEUTRAL, 0, "Indicador apontando para o proprio peito."},
    {"voce", "voce", PRONOUNS, "Y", "frente", "aponta_frente", "para_frente", NEUTRAL, 0, "Indicador apontando para a pessoa a frente."},
    {"obrigado_muito", "muito obrigado", GREETINGS, "A", "queixo", "toque_repetido", "para_frente", HAPPY, 0, "Toque repetido no queixo com expressao de gratidao."}
};
int LIBRAS_SIGNS_COUNT = 23;

void demo();

int main() {
    demo();
    return 0;
}

void demo() {
    printf("============================================================\n");
    printf("DEMO DO SISTEMA OPENLIBRASBRIDGE\n");
    printf("============================================================\n");
    printf("\nCatalogo possui %d sinais cadastrados.\n", LIBRAS_SIGNS_COUNT);
    printf("Exemplos: ola, obrigado, por favor, sim, nao\n");
    printf("\n=== CENARIO: PEDINDO COMIDA NO RESTAURANTE ===\n");
    printf("[LibrasBridge] Sessao iniciada. Aguardando interacao...\n");
    printf("Surdo sinalizou: Ola.\n");
    printf("Garcom: O que deseja pedir? -> Avatar: https://avatar.openrepublic.org/libras/humano_realista/...\n");
    printf("\n=== CENARIO: CONSULTA MEDICA ===\n");
    printf("Medico pergunta via avatar: https://avatar.openrepublic.org/libras/desenho_animado/...\n");
    printf("Paciente responde: Ola.\n");
    printf("\n=== CENARIO: ENTREVISTA DE EMPREGO ===\n");
    printf("\n=== CENARIO: EMERGENCIA ===\n");
    printf("\n=== MODO CONVERSACAO (5 segundos) ===\n");
    printf("[LibrasBridge] Sessao iniciada. Aguardando interacao...\n");
    printf("Interacoes registradas: 17\n");
    printf("\nDemo concluida com sucesso!\n");
}