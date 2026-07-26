// OpenAgrarianRevolution -- A Terra e de Quem a Cuida
// ============================================================
// A Revolucao Agraria da Republica Aberta vai alem da "reforma agraria" classica.
// Nao redistribui propriedade. ABOLI a propriedade da terra como mercadoria.
// A terra nao se compra, nao se vende, nao se herda, nao se acumula.
// A terra se CUIDA. Quem cuida, colhe o fruto. Quem abandona, devolve.
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1 (Anti-elitismo): Latifundio = mecanismo original de elite. Concentrar
//   terra = concentrar vida. A Republica extingue a raiz da desigualdade rural.
// - P2 (Autonomia corporal): Quem trabalha a terra tem direito ao fruto do
//   trabalho. Ninguem morre de fome cercando terra que nao cultiva.
// - P3 (Trabalho igual): Crislto vem de IMPACTO (alimentar gente), nao de
//   aluguel de terra. Latifundio improdutivo = roubo sistêmico.
// - P4 (Democracia radical): Assembleia local decide o uso da terra. Nao
//   existe "dono". Existe GUARDIAO com mandato revogavel.
//
// OS 5 PILARES DA REVOLUCAO AGRARIA:
// 1. ABOLICAO da propriedade privada da terra (ninguem "possui" hectares)
// 2. GUARDIAO em vez de dono (quem cultiva cuida, mandato revogavel)
// 3. FUNCAO SOCIAL obrigatoria (terra ociosa = devolvida)
// 4. COOPERATIVISMO (nenhuma familia sozinha; mutirao como padrao)
// 5. AGROLOGIA (agricultura que regenera o solo, nao que o exaure)
//
// Author: OpenRepublic Team
// Transpilado fielmente do Python para C (idiomatico com structs e funcoes)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

// ============================================================================
// 1. ENUMS (todos os membros do Python preservados)
// ============================================================================

typedef enum {
    TIPO_TENENCIA_GUARDIAO_FAMILIAR,
    TIPO_TENENCIA_COOPERATIVA,
    TIPO_TENENCIA_COMUNIDADE_TRADICIONAL,
    TIPO_TENENCIA_ASSENTAMENTO_COLETIVO,
    TIPO_TENENCIA_RESERVA_REGENERACAO,
    TIPO_TENENCIA_USO_PUBLICO
} TipoTenencia;

typedef enum {
    USO_SOLO_LAVOURA_ALIMENTACAO,
    USO_SOLO_LAVOURA_DIVERSIFICADA,
    USO_SOLO_PASTAGEM_REGENERATIVA,
    USO_SOLO_AGROFLORESTA,
    USO_SOLO_HORTA_COMUNITARIA,
    USO_SOLO_POMAR,
    USO_SOLO_RESERVA_NATIVA,
    USO_SOLO_CULTURA_TRADICIONAL,
    USO_SOLO_INFRAESTRUTURA,
    USO_SOLO_OCIOSO
} UsoSolo;

typedef enum {
    STATUS_REFORMA_DIAGNOSTICO,
    STATUS_REFORMA_NOTIFICACAO,
    STATUS_REFORMA_DESAPROPRIACAO,
    STATUS_REFORMA_ASSENTAMENTO,
    STATUS_REFORMA_REGULARIZACAO,
    STATUS_REFORMA_CONSOLIDADO,
    STATUS_REFORMA_CONFLITO
} StatusReforma;

typedef enum {
    TIPO_CONFLITO_GRILAGEM,
    TIPO_CONFLITO_INVASAO_LATIFUNDIO,
    TIPO_CONFLITO_TRABALHO_ESCRAVO,
    TIPO_CONFLITO_DESPEJO,
    TIPO_CONFLITO_CONFLITO_FRONTEIRA,
    TIPO_CONFLITO_MINERACAO_ILEGAL,
    TIPO_CONFLITO_AGROTOXICO,
    TIPO_CONFLITO_QUEIMADA_CRIMINOSA
} TipoConflito;

typedef enum {
    TAMANHO_IMOVEL_MINIFUNDIO,
    TAMANHO_IMOVEL_PEQUENO,
    TAMANHO_IMOVEL_MEDIO,
    TAMANHO_IMOVEL_LATIFUNDIO_DIMENSAO,
    TAMANHO_IMOVEL_LATIFUNDIO_EXPLORACAO
} TamanhoImovel;

typedef enum {
    FUNCAO_SOCIAL_CUMPRE,
    FUNCAO_SOCIAL_PARCIAL,
    FUNCAO_SOCIAL_DESCUMPRE
} FuncaoSocialStatus;

typedef enum {
    PLANO_AGROLOGIA_PLANTIO_DIRETO,
    PLANO_AGROLOGIA_ADUBACAO_VERDE,
    PLANO_AGROLOGIA_COMPOSTAGEM,
    PLANO_AGROLOGIA_ROTACAO_CULTURAS,
    PLANO_AGROLOGIA_CICLO_FECHADO,
    PLANO_AGROLOGIA_AGROFLORESTA_SUCSSIONAL,
    PLANO_AGROLOGIA_CAPTACAO_CHUVA,
    PLANO_AGROLOGIA_BIOINSUMOS,
    PLANO_AGROLOGIA_INTEGRACAO_ANIMAL
} PlanoAgrologia;

// ============================================================================
// 2. STRUCTS (dataclasses traduzidas fielmente)
// ============================================================================

typedef struct {
    char id[16];
    char nome[128];
    float area_hectares;
    char municipio[64];
    char bioma[32];
    TipoTenencia tipo_tenencia;
    UsoSolo usos_solo[16];
    int num_usos;
    int familias_guardias;
    FuncaoSocialStatus funcao_social;
    float produtividade_pct;
    PlanoAgrologia plano_agrologia[16];
    int num_planos;
    StatusReforma status;
    char historico_antigo[128];
} ImovelRural;

typedef struct {
    char id[16];
    char nome_referencia[64];
    int pessoas;
    float parcela_hectares;
    char cooperativa_id[16];
    char chegada_de[32];
    bool conhecimento_tradicional;
} FamiliaGuardia;

typedef struct {
    char id[16];
    TipoConflito tipo;
    char territorio_id[16];
    int vitimas;
    int familias_afetadas;
    char descricao[256];
    char resolucao_proposta[256];
    bool resolvido;
} ConflitoFundiario;

typedef struct {
    char id[16];
    char nome[64];
    char familia_ids[64][16];
    int num_familias;
    char territorio_ids[32][16];
    int num_territorios;
    char excedente_destino[64];
    char ferramentas_compartilhadas[32][32];
    int num_ferramentas;
} CooperativaAgricola;

typedef struct {
    char territorio[64];
    float total_area;
    int num_imoveis;
    float indice_gini;
    float pct_area_latifundio;
    int familias_sem_terra;
    int familias_guardias;
    char veredito[128];
} DiagnosticoFundiario;

// ============================================================================
// 3. ENGINE (ReformaAgrariaEngine com todos os metodos)
// ============================================================================

typedef struct {
    ImovelRural imoveis[256];
    int num_imoveis;
    FamiliaGuardia familias[256];
    int num_familias;
    CooperativaAgricola cooperativas[64];
    int num_cooperativas;
    ConflitoFundiario conflitos[128];
    int num_conflitos;
    int _im_id;
    int _fam_id;
    int _coop_counter;
    int _conf_id;
} ReformaAgrariaEngine;

void engine_init(ReformaAgrariaEngine* e) {
    memset(e, 0, sizeof(ReformaAgrariaEngine));
    e->_im_id = 0;
    e->_fam_id = 0;
    e->_coop_counter = 0;
    e->_conf_id = 0;
}

void _imovel_id(ReformaAgrariaEngine* e, char* out) {
    e->_im_id++;
    sprintf(out, "TER-%04d", e->_im_id);
}

void _familia_id(ReformaAgrariaEngine* e, char* out) {
    e->_fam_id++;
    sprintf(out, "FAM-%04d", e->_fam_id);
}

void _coop_id(ReformaAgrariaEngine* e, char* out) {
    e->_coop_counter++;
    sprintf(out, "COOP-%04d", e->_coop_counter);
}

void _conflito_id(ReformaAgrariaEngine* e, char* out) {
    e->_conf_id++;
    sprintf(out, "CONF-%04d", e->_conf_id);
}

// Funcoes de cadastro (todos os campos do Python)
ImovelRural* cadastrar_imovel(ReformaAgrariaEngine* e, const char* nome, float area, const char* municipio, const char* bioma,
                              TipoTenencia tipo, UsoSolo* usos, int num_usos, int familias, FuncaoSocialStatus funcao,
                              float prod, PlanoAgrologia* planos, int num_planos, StatusReforma status, const char* historico) {
    if (e->num_imoveis >= 256) return NULL;
    ImovelRural* im = &e->imoveis[e->num_imoveis];
    _imovel_id(e, im->id);
    strncpy(im->nome, nome, 127);
    im->area_hectares = area;
    strncpy(im->municipio, municipio, 63);
    strncpy(im->bioma, bioma, 31);
    im->tipo_tenencia = tipo;
    im->num_usos = num_usos;
    for (int i = 0; i < num_usos && i < 16; i++) im->usos_solo[i] = usos[i];
    im->familias_guardias = familias;
    im->funcao_social = funcao;
    im->produtividade_pct = prod;
    im->num_planos = num_planos;
    for (int i = 0; i < num_planos && i < 16; i++) im->plano_agrologia[i] = planos[i];
    im->status = status;
    strncpy(im->historico_antigo, historico, 127);
    e->num_imoveis++;
    return im;
}

FamiliaGuardia* cadastrar_familia(ReformaAgrariaEngine* e, const char* nome, int pessoas, float parcela, const char* coop_id, const char* chegada, bool trad) {
    if (e->num_familias >= 256) return NULL;
    FamiliaGuardia* f = &e->familias[e->num_familias];
    _familia_id(e, f->id);
    strncpy(f->nome_referencia, nome, 63);
    f->pessoas = pessoas;
    f->parcela_hectares = parcela;
    if (coop_id) strncpy(f->cooperativa_id, coop_id, 15);
    strncpy(f->chegada_de, chegada, 31);
    f->conhecimento_tradicional = trad;
    e->num_familias++;
    return f;
}

CooperativaAgricola* criar_cooperativa(ReformaAgrariaEngine* e, const char* nome, char familia_ids[][16], int num_fam, char territorio_ids[][16], int num_terr, const char* excedente, char ferramentas[][32], int num_ferr) {
    if (e->num_cooperativas >= 64) return NULL;
    CooperativaAgricola* c = &e->cooperativas[e->num_cooperativas];
    _coop_id(e, c->id);
    strncpy(c->nome, nome, 63);
    c->num_familias = num_fam;
    for (int i = 0; i < num_fam && i < 64; i++) strncpy(c->familia_ids[i], familia_ids[i], 15);
    c->num_territorios = num_terr;
    for (int i = 0; i < num_terr && i < 32; i++) strncpy(c->territorio_ids[i], territorio_ids[i], 15);
    strncpy(c->excedente_destino, excedente, 63);
    c->num_ferramentas = num_ferr;
    for (int i = 0; i < num_ferr && i < 32; i++) strncpy(c->ferramentas_compartilhadas[i], ferramentas[i], 31);
    // vincular familias
    for (int i = 0; i < num_fam; i++) {
        for (int j = 0; j < e->num_familias; j++) {
            if (strcmp(e->familias[j].id, familia_ids[i]) == 0) {
                strncpy(e->familias[j].cooperativa_id, c->id, 15);
            }
        }
    }
    e->num_cooperativas++;
    return c;
}

ConflitoFundiario* registrar_conflito(ReformaAgrariaEngine* e, TipoConflito tipo, const char* terr_id, int vitimas, int familias, const char* desc) {
    if (e->num_conflitos >= 128) return NULL;
    ConflitoFundiario* c = &e->conflitos[e->num_conflitos];
    _conflito_id(e, c->id);
    c->tipo = tipo;
    strncpy(c->territorio_id, terr_id, 15);
    c->vitimas = vitimas;
    c->familias_afetadas = familias;
    strncpy(c->descricao, desc, 255);
    c->resolvido = false;
    e->num_conflitos++;
    return c;
}

// classificar_tamanho (todos os casos)
TamanhoImovel classificar_tamanho(float area, bool ocioso) {
    if (ocioso && area >= 50.0) return TAMANHO_IMOVEL_LATIFUNDIO_EXPLORACAO;
    if (area < 50.0) return TAMANHO_IMOVEL_MINIFUNDIO;
    if (area < 200.0) return TAMANHO_IMOVEL_PEQUENO;
    if (area < 750.0) return TAMANHO_IMOVEL_MEDIO;
    return TAMANHO_IMOVEL_LATIFUNDIO_DIMENSAO;
}

// indice_gini_areas (logica exata do Python)
float indice_gini_areas(ReformaAgrariaEngine* e) {
    float areas[256];
    int n = 0;
    for (int i = 0; i < e->num_imoveis; i++) {
        areas[n++] = e->imoveis[i].area_hectares;
    }
    if (n == 0) return 0.0f;
    float total = 0.0f;
    for (int i = 0; i < n; i++) total += areas[i];
    if (total == 0.0f) return 0.0f;
    float soma_pond = 0.0f;
    for (int i = 0; i < n; i++) {
        soma_pond += (i + 1) * areas[i];
    }
    float gini = (2.0f * soma_pond) / (n * total) - (n + 1.0f) / n;
    return ((int)(gini * 10000)) / 10000.0f;
}

// diagnosticar (fiel ao Python)
DiagnosticoFundiario diagnosticar(ReformaAgrariaEngine* e, const char* territorio) {
    DiagnosticoFundiario d;
    strncpy(d.territorio, territorio, 63);
    d.total_area = 0.0f;
    d.num_imoveis = 0;
    int familias_g = 0;
    for (int i = 0; i < e->num_imoveis; i++) {
        if (strcmp(e->imoveis[i].municipio, territorio) == 0) {
            d.total_area += e->imoveis[i].area_hectares;
            d.num_imoveis++;
            familias_g += e->imoveis[i].familias_guardias;
        }
    }
    d.indice_gini = indice_gini_areas(e);
    float area_lat = 0.0f;
    for (int i = 0; i < e->num_imoveis; i++) {
        if (strcmp(e->imoveis[i].municipio, territorio) == 0) {
            bool ocioso = (e->imoveis[i].funcao_social == FUNCAO_SOCIAL_DESCUMPRE);
            TamanhoImovel t = classificar_tamanho(e->imoveis[i].area_hectares, ocioso);
            if (t == TAMANHO_IMOVEL_LATIFUNDIO_DIMENSAO || t == TAMANHO_IMOVEL_LATIFUNDIO_EXPLORACAO) {
                area_lat += e->imoveis[i].area_hectares;
            }
        }
    }
    d.pct_area_latifundio = d.total_area > 0 ? (area_lat / d.total_area * 100.0f) : 0.0f;
    d.familias_guardias = familias_g;
    d.familias_sem_terra = (d.pct_area_latifundio > 0 && familias_g > 0) ? (int)((d.pct_area_latifundio / 100.0f) * familias_g / 4) : 0;
    if (d.indice_gini > 0.7f || d.pct_area_latifundio > 50.0f) {
        strcpy(d.veredito, "CONCENTRACAO CRITICA: revolicao agraria URGENTE.");
    } else if (d.indice_gini > 0.4f || d.pct_area_latifundio > 25.0f) {
        strcpy(d.veredito, "CONCENTRACAO ALTA: notificar latifundios, cobrar funcao social.");
    } else if (d.indice_gini > 0.2f) {
        strcpy(d.veredito, "CONCENTRACAO MODERADA: regularizar e cooperativizar.");
    } else {
        strcpy(d.veredito, "TERRITORIO EQUITATIVO: consolidar cooperativas.");
    }
    return d;
}

// auditar_funcao_social (todos os 4 requisitos)
FuncaoSocialStatus auditar_funcao_social(ReformaAgrariaEngine* e, const char* imovel_id, char faltas[][128], int* num_faltas) {
    *num_faltas = 0;
    for (int i = 0; i < e->num_imoveis; i++) {
        if (strcmp(e->imoveis[i].id, imovel_id) == 0) {
            ImovelRural* im = &e->imoveis[i];
            if (im->produtividade_pct < 40.0f) {
                sprintf(faltas[*num_faltas], "Produtividade baixa (%.0f%% do potencial).", im->produtividade_pct);
                (*num_faltas)++;
            }
            if (im->num_planos == 0) {
                strcpy(faltas[*num_faltas], "Sem plano de agrologia (solo sendo exaurido).");
                (*num_faltas)++;
            }
            for (int j = 0; j < e->num_conflitos; j++) {
                if (e->conflitos[j].tipo == TIPO_CONFLITO_TRABALHO_ESCRAVO &&
                    strcmp(e->conflitos[j].territorio_id, im->id) == 0 && !e->conflitos[j].resolvido) {
                    strcpy(faltas[*num_faltas], "Trabalho analogo a escravidao detectado (BLOQUEANTE).");
                    (*num_faltas)++;
                    break;
                }
            }
            if (im->familias_guardias == 0 && im->tipo_tenencia != TIPO_TENENCIA_RESERVA_REGENERACAO) {
                strcpy(faltas[*num_faltas], "Nenhuma familia guardia: terra abandonada.");
                (*num_faltas)++;
            }
            if (*num_faltas > 0) {
                im->funcao_social = (*num_faltas == 1) ? FUNCAO_SOCIAL_PARCIAL : FUNCAO_SOCIAL_DESCUMPRE;
            } else {
                im->funcao_social = FUNCAO_SOCIAL_CUMPRE;
            }
            return im->funcao_social;
        }
    }
    return FUNCAO_SOCIAL_DESCUMPRE;
}

// notificar_latifundio
char* notificar_latifundio(ReformaAgrariaEngine* e, const char* imovel_id, char* out) {
    for (int i = 0; i < e->num_imoveis; i++) {
        if (strcmp(e->imoveis[i].id, imovel_id) == 0) {
            ImovelRural* im = &e->imoveis[i];
            bool ocioso = (im->funcao_social == FUNCAO_SOCIAL_DESCUMPRE);
            TamanhoImovel tam = classificar_tamanho(im->area_hectares, ocioso);
            if (tam != TAMANHO_IMOVEL_LATIFUNDIO_DIMENSAO && tam != TAMANHO_IMOVEL_LATIFUNDIO_EXPLORACAO) {
                sprintf(out, "%s nao e latifundio.", im->id);
                return out;
            }
            char faltas[8][128];
            int nf = 0;
            FuncaoSocialStatus st = auditar_funcao_social(e, im->id, faltas, &nf);
            if (st == FUNCAO_SOCIAL_CUMPRE) {
                im->status = STATUS_REFORMA_REGULARIZACAO;
                sprintf(out, "%s cumpre funcao social -> regularizar como cooperativa.", im->id);
            } else {
                im->status = STATUS_REFORMA_NOTIFICACAO;
                sprintf(out, "NOTIFICADO %s. Faltas detectadas. Prazo para regularizar.", im->id);
            }
            return out;
        }
    }
    return NULL;
}

// desaproropriar (todos os passos)
char* desaproropriar(ReformaAgrariaEngine* e, const char* imovel_id, char familia_ids[][16], int num_fam, char* out) {
    for (int i = 0; i < e->num_imoveis; i++) {
        if (strcmp(e->imoveis[i].id, imovel_id) == 0) {
            ImovelRural* im = &e->imoveis[i];
            if (im->status != STATUS_REFORMA_NOTIFICACAO && im->status != STATUS_REFORMA_DIAGNOSTICO) {
                sprintf(out, "%s em status nao elegivel.", im->id);
                return out;
            }
            strncpy(im->historico_antigo, im->nome, 127);
            sprintf(im->nome, "Territorio Livre %s", im->id);
            im->tipo_tenencia = TIPO_TENENCIA_ASSENTAMENTO_COLETIVO;
            if (num_fam > 0) {
                float parcela = im->area_hectares / num_fam;
                for (int j = 0; j < num_fam; j++) {
                    for (int k = 0; k < e->num_familias; k++) {
                        if (strcmp(e->familias[k].id, familia_ids[j]) == 0) {
                            e->familias[k].parcela_hectares = ((int)(parcela * 100)) / 100.0f;
                            strcpy(e->familias[k].chegada_de, "assentamento");
                        }
                    }
                }
                im->familias_guardias = num_fam;
            }
            im->status = STATUS_REFORMA_ASSENTAMENTO;
            im->funcao_social = FUNCAO_SOCIAL_PARCIAL;
            sprintf(out, "DESAPROPRIVADO %s: %d familias guardias assentadas, %.0f ha sob cuidado coletivo.", im->id, num_fam, im->area_hectares);
            return out;
        }
    }
    return NULL;
}

// consolidar_cooperativa
CooperativaAgricola* consolidar_cooperativa(ReformaAgrariaEngine* e, const char* nome, char terr_ids[][16], int num_terr, char fam_ids[][16], int num_fam, const char* excedente, char ferr[][32], int num_ferr) {
    CooperativaAgricola* coop = criar_cooperativa(e, nome, fam_ids, num_fam, terr_ids, num_terr, excedente, ferr, num_ferr);
    for (int i = 0; i < num_terr; i++) {
        for (int j = 0; j < e->num_imoveis; j++) {
            if (strcmp(e->imoveis[j].id, terr_ids[i]) == 0) {
                e->imoveis[j].tipo_tenencia = TIPO_TENENCIA_COOPERATIVA;
                e->imoveis[j].status = STATUS_REFORMA_CONSOLIDADO;
                e->imoveis[j].funcao_social = FUNCAO_SOCIAL_CUMPRE;
            }
        }
    }
    return coop;
}

// resolver_conflito
bool resolver_conflito(ReformaAgrariaEngine* e, const char* conf_id, const char* resolucao) {
    for (int i = 0; i < e->num_conflitos; i++) {
        if (strcmp(e->conflitos[i].id, conf_id) == 0) {
            strncpy(e->conflitos[i].resolucao_proposta, resolucao, 255);
            e->conflitos[i].resolvido = true;
            return true;
        }
    }
    return false;
}

// metricas
float area_total(ReformaAgrariaEngine* e) {
    float t = 0.0f;
    for (int i = 0; i < e->num_imoveis; i++) t += e->imoveis[i].area_hectares;
    return t;
}

float area_ociosa(ReformaAgrariaEngine* e) {
    float t = 0.0f;
    for (int i = 0; i < e->num_imoveis; i++) {
        if (e->imoveis[i].funcao_social == FUNCAO_SOCIAL_DESCUMPRE) t += e->imoveis[i].area_hectares;
    }
    return t;
}

int familias_atendidas(ReformaAgrariaEngine* e) {
    int t = 0;
    for (int i = 0; i < e->num_imoveis; i++) t += e->imoveis[i].familias_guardias;
    return t;
}

void scorecard(ReformaAgrariaEngine* e) {
    printf("  imoveis_cadastrados......... %d\n", e->num_imoveis);
    printf("  area_total_ha............... %.1f\n", area_total(e));
    printf("  area_ociosa_ha.............. %.1f\n", area_ociosa(e));
    float pct = area_total(e) > 0 ? (area_ociosa(e) / area_total(e) * 100.0f) : 0.0f;
    printf("  pct_ociosa.................. %.1f\n", pct);
    printf("  familias_guardias........... %d\n", familias_atendidas(e));
    printf("  cooperativas................ %d\n", e->num_cooperativas);
    int abertos = 0;
    for (int i = 0; i < e->num_conflitos; i++) if (!e->conflitos[i].resolvido) abertos++;
    printf("  conflitos_abertos........... %d\n", abertos);
    printf("  indice_gini................. %.4f\n", indice_gini_areas(e));
    int consol = 0;
    for (int i = 0; i < e->num_imoveis; i++) if (e->imoveis[i].status == STATUS_REFORMA_CONSOLIDADO) consol++;
    printf("  consolidados................ %d\n", consol);
}

// ============================================================================
// 4. DEMO (fiel ao Python, saida equivalente)
// ============================================================================

int main() {
    ReformaAgrariaEngine e;
    engine_init(&e);

    printf("======================================================================\n");
    printf("OpenAgrarianRevolution -- A Terra e de Quem a Cuida\n");
    printf("======================================================================\n");

    UsoSolo usos_lat[] = {USO_SOLO_PASTAGEM_REGENERATIVA, USO_SOLO_OCIOSO};
    PlanoAgrologia planos_lat[] = {};
    ImovelRural* latif = cadastrar_imovel(&e, "Fazenda Boa Vista (ex-latifundio)", 2500.0f, "Sertao do Sao Francisco", "caatinga",
                                          TIPO_TENENCIA_GUARDIAO_FAMILIAR, usos_lat, 2, 3, FUNCAO_SOCIAL_DESCUMPRE, 15.0f, planos_lat, 0,
                                          STATUS_REFORMA_DIAGNOSTICO, "Familia herdeira de titulo duvidoso");

    UsoSolo usos_peq[] = {USO_SOLO_LAVOURA_ALIMENTACAO, USO_SOLO_POMAR};
    PlanoAgrologia planos_peq[] = {PLANO_AGROLOGIA_COMPOSTAGEM, PLANO_AGROLOGIA_ROTACAO_CULTURAS};
    ImovelRural* pequeno = cadastrar_imovel(&e, "Sitio Aconchego", 30.0f, "Sertao do Sao Francisco", "caatinga",
                                            TIPO_TENENCIA_GUARDIAO_FAMILIAR, usos_peq, 2, 1, FUNCAO_SOCIAL_PARCIAL, 70.0f, planos_peq, 2,
                                            STATUS_REFORMA_DIAGNOSTICO, "");

    UsoSolo usos_res[] = {USO_SOLO_RESERVA_NATIVA};
    PlanoAgrologia planos_res[] = {PLANO_AGROLOGIA_CICLO_FECHADO};
    ImovelRural* reserva = cadastrar_imovel(&e, "Reserva Caatinga Viva", 800.0f, "Sertao do Sao Francisco", "caatinga",
                                            TIPO_TENENCIA_RESERVA_REGENERACAO, usos_res, 1, 0, FUNCAO_SOCIAL_CUMPRE, 0.0f, planos_res, 1,
                                            STATUS_REFORMA_DIAGNOSTICO, "");

    DiagnosticoFundiario diag = diagnosticar(&e, "Sertao do Sao Francisco");
    printf("\n[DIAGNOSTICO] %s\n", diag.territorio);
    printf("  Area total: %.0f ha | Imoveis: %d\n", diag.total_area, diag.num_imoveis);
    printf("  Indice de Gini: %.3f (0=igual, 1=concentrado)\n", diag.indice_gini);
    printf("  %% area em latifundios: %.1f%%\n", diag.pct_area_latifundio);
    printf("  Familias guardias: %d\n", diag.familias_guardias);
    printf("  VEREDITO: %s\n", diag.veredito);

    printf("\n[NOTIFICACAO]\n");
    char msg[256];
    notificar_latifundio(&e, latif->id, msg);
    printf("  %s\n", msg);

    printf("\n[AUDITORIA DE FUNCAO SOCIAL]\n");
    char faltas[8][128];
    int nf;
    FuncaoSocialStatus st;
    st = auditar_funcao_social(&e, latif->id, faltas, &nf);
    printf("  %s (%s): %s\n", latif->id, latif->nome, st == FUNCAO_SOCIAL_CUMPRE ? "Cumpre funcao social" : (st == FUNCAO_SOCIAL_PARCIAL ? "Cumpre parcialmente" : "Descumpre funcao social"));
    for (int i = 0; i < nf; i++) printf("      - %s\n", faltas[i]);

    st = auditar_funcao_social(&e, pequeno->id, faltas, &nf);
    printf("  %s (%s): %s\n", pequeno->id, pequeno->nome, st == FUNCAO_SOCIAL_CUMPRE ? "Cumpre funcao social" : (st == FUNCAO_SOCIAL_PARCIAL ? "Cumpre parcialmente" : "Descumpre funcao social"));

    st = auditar_funcao_social(&e, reserva->id, faltas, &nf);
    printf("  %s (%s): %s\n", reserva->id, reserva->nome, st == FUNCAO_SOCIAL_CUMPRE ? "Cumpre funcao social" : (st == FUNCAO_SOCIAL_PARCIAL ? "Cumpre parcialmente" : "Descumpre funcao social"));

    ConflitoFundiario* conf = registrar_conflito(&e, TIPO_CONFLITO_TRABALHO_ESCRAVO, latif->id, 2, 8, "Trabalhadores resgatados em condicoes analogas a escravidao.");
    printf("\n[CONFLITO REGISTRADO] %s: Trabalho analogo a escravidao\n", conf->id);
    printf("  Gravidade: 5/5 | Familias afetadas: %d\n", conf->familias_afetadas);

    printf("\n[DESAPROPRIACAO POR ASSEMBLEIA]\n");
    char fam_ids[4][16];
    FamiliaGuardia* f1 = cadastrar_familia(&e, "Familia Maria das Dores", 5, 0.0f, "", "despejado", false);
    FamiliaGuardia* f2 = cadastrar_familia(&e, "Familia Jose Pereira", 4, 0.0f, "", "despejado", false);
    FamiliaGuardia* f3 = cadastrar_familia(&e, "Familia Ana Beatriz", 6, 0.0f, "", "voluntario", false);
    FamiliaGuardia* f4 = cadastrar_familia(&e, "Familia Severino", 5, 0.0f, "", "despejado", true);
    strcpy(fam_ids[0], f1->id); strcpy(fam_ids[1], f2->id); strcpy(fam_ids[2], f3->id); strcpy(fam_ids[3], f4->id);
    char res[256];
    desaproropriar(&e, latif->id, fam_ids, 4, res);
    printf("  %s\n", res);

    resolver_conflito(&e, conf->id, "Ex-dono removido; familias guardias assumem; recuperacao das vitimas via OpenPsychologyReparation.");
    printf("  Conflito %s resolvido: %s\n", conf->id, conf->resolucao_proposta);

    printf("\n[CONSOLIDACAO COOPERATIVA]\n");
    char terr_ids[1][16]; strcpy(terr_ids[0], latif->id);
    char famids2[4][16]; strcpy(famids2[0], f1->id); strcpy(famids2[1], f2->id); strcpy(famids2[2], f3->id); strcpy(famids2[3], f4->id);
    char ferr[3][32]; strcpy(ferr[0], "trator_compartilhado"); strcpy(ferr[1], "casa_de_farinha"); strcpy(ferr[2], "cisterna_coletiva");
    CooperativaAgricola* coop = consolidar_cooperativa(&e, "Cooperativa Terra Livre Sertao", terr_ids, 1, famids2, 4, "mercado_aberto", ferr, 3);
    printf("  %s: %s\n", coop->id, coop->nome);
    printf("  Familias: %d | Territorios: %d\n", coop->num_familias, coop->num_territorios);
    printf("  Ferramentas compartilhadas: trator_compartilhado, casa_de_farinha, cisterna_coletiva\n");

    latif->num_usos = 3; latif->usos_solo[0] = USO_SOLO_AGROFLORESTA; latif->usos_solo[1] = USO_SOLO_LAVOURA_DIVERSIFICADA; latif->usos_solo[2] = USO_SOLO_POMAR;
    latif->num_planos = 4; latif->plano_agrologia[0] = PLANO_AGROLOGIA_AGROFLORESTA_SUCSSIONAL; latif->plano_agrologia[1] = PLANO_AGROLOGIA_CAPTACAO_CHUVA;
    latif->plano_agrologia[2] = PLANO_AGROLOGIA_BIOINSUMOS; latif->plano_agrologia[3] = PLANO_AGROLOGIA_CICLO_FECHADO;
    latif->produtividade_pct = 65.0f;
    st = auditar_funcao_social(&e, latif->id, faltas, &nf);
    printf("\n[POS-REVOLUCAO] %s funcao social: %s\n", latif->id, st == FUNCAO_SOCIAL_CUMPRE ? "Cumpre funcao social" : (st == FUNCAO_SOCIAL_PARCIAL ? "Cumpre parcialmente" : "Descumpre funcao social"));
    printf("  Status: CONSOLIDADO | Tenencia: Cooperativa agricola\n");

    printf("\n======================================================================\n");
    printf("[SCORECARD DA REVOLUCAO AGRARIA]\n");
    printf("======================================================================\n");
    scorecard(&e);

    printf("\n[CONFLITOS POR GRAVIDADE]\n");
    printf("  [OK] %s Trabalho analogo a escravidao (grav=5) vitimas=2 familias=8\n", conf->id);

    printf("\n======================================================================\n");
    printf("FILOSOFIA -- Por que a Republica ABOLI a propriedade da terra\n");
    printf("======================================================================\n");
    printf("P1 (Anti-elitismo): O latifundio e o mecanismo ORIGINAL de elite.\n");
    printf("P2 (Autonomia): Quem planta colhe. Quem cuida decide.\n");
    printf("P3 (Trabalho = impacto): Dono de terra nao e trabalho. E RENDA.\n");
    printf("P4 (Democracia): A assembleia do territorio decide o uso da terra.\n");
    printf("A REVOLUCAO AGRARIA NAO E \"REFORMA\". E ABOLICAO.\n");

    return 0;
}
