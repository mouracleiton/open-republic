// open_energy.c
// Transpilacao fiel de open_energy.py para C
// OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso
// Comentarios e strings em Portugues (conforme fonte)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>

#define MAX_ID 32
#define MAX_ROTULO 128
#define MAX_JUSTIFICATIVA 256
#define MAX_ITEMS 64
#define MAX_CONSUMOS 256
#define MAX_MICROGRIDS 32
#define MAX_ALOCACOES 32

// ============================================================================
// 1. ENUMS (modulo-level) - transpilacao fiel
// ============================================================================

typedef enum {
    FONTE_SOLAR,
    FONTE_EOLICA,
    FONTE_HIDRO,
    FONTE_GEOTERMICA,
    FONTE_BIOMASSA,
    FONTE_MARES,
    FONTE_NUCLEAR,
    FONTE_FUSAO
} FonteEnergia;

typedef struct {
    FonteEnergia id;
    const char* rotulo;
    bool renovavel;
} FonteInfo;

static FonteInfo fontes_info[] = {
    {FONTE_SOLAR, "Solar fotovoltaica", true},
    {FONTE_EOLICA, "Eolica (vento)", true},
    {FONTE_HIDRO, "Hidroeletrica", true},
    {FONTE_GEOTERMICA, "Geotermica", true},
    {FONTE_BIOMASSA, "Biomassa", true},
    {FONTE_MARES, "Das mars e correntes", true},
    {FONTE_NUCLEAR, "Nuclear (fissao)", false},
    {FONTE_FUSAO, "Fusao nuclear (futura)", true}
};

typedef enum {
    CONSUMO_ESSENCIAL_VIDA,
    CONSUMO_SAUDE,
    CONSUMO_COMUNICACAO,
    CONSUMO_EDUCACAO,
    CONSUMO_MOBILIDADE,
    CONSUMO_PRODUCAO_ALIMENTOS,
    CONSUMO_INFRAESTRUTURA_COMUM,
    CONSUMO_PRODUCAO_BENS,
    CONSUMO_CULTURA_LAZER,
    CONSUMO_PESQUISA_INOVACAO,
    CONSUMO_RESIDENCIAL_EXCEDENTE
} TipoConsumo;

typedef struct {
    TipoConsumo id;
    const char* rotulo;
    int prioridade;
} ConsumoInfo;

static ConsumoInfo consumos_info[] = {
    {CONSUMO_ESSENCIAL_VIDA, "Essencial a vida (cozinhar, aquecer, iluminar, agua)", 1},
    {CONSUMO_SAUDE, "Saude (hospitais, clinicas, equipamentos medicos)", 1},
    {CONSUMO_COMUNICACAO, "Comunicacao (internet, telefone, radio)", 1},
    {CONSUMO_EDUCACAO, "Educacao (escolas, bibliotecas, laboratorios)", 2},
    {CONSUMO_MOBILIDADE, "Mobilidade (transporte publico, veiculos)", 2},
    {CONSUMO_PRODUCAO_ALIMENTOS, "Producao de alimentos (irrigacao, processamento)", 2},
    {CONSUMO_INFRAESTRUTURA_COMUM, "Infraestrutura comum (agua, esgoto, iluminacao publica)", 2},
    {CONSUMO_PRODUCAO_BENS, "Producao de bens (fabril, artesanal)", 3},
    {CONSUMO_CULTURA_LAZER, "Cultura e lazer (teatro, musica, esporte)", 3},
    {CONSUMO_PESQUISA_INOVACAO, "Pesquisa e inovacao (laboratorios, computacao)", 3},
    {CONSUMO_RESIDENCIAL_EXCEDENTE, "Residencial excedente (alem do essencial)", 4}
};

typedef enum {
    ARMAZ_BATERIA_LITIO,
    ARMAZ_BATERIA_SODIO,
    ARMAZ_BATERIA_FLUXO,
    ARMAZ_HIDRO_BOMBEADA,
    ARMAZ_GRAVIDADE,
    ARMAZ_HIDROGENIO,
    ARMAZ_AR_COMPRIMIDO,
    ARMAZ_TERMICO
} TipoArmazenamento;

typedef struct {
    TipoArmazenamento id;
    const char* rotulo;
} ArmazenamentoInfo;

static ArmazenamentoInfo armazenamentos_info[] = {
    {ARMAZ_BATERIA_LITIO, "Bateria de litio-ion"},
    {ARMAZ_BATERIA_SODIO, "Bateria de sodio (mais barato, menos denso)"},
    {ARMAZ_BATERIA_FLUXO, "Bateria de fluxo redox (escala grid)"},
    {ARMAZ_HIDRO_BOMBEADA, "Hidroeletrica reversivel (bombeada)"},
    {ARMAZ_GRAVIDADE, "Armazenamento por gravidade (pesos)"},
    {ARMAZ_HIDROGENIO, "Hidrogenio verde (eletrolise)"},
    {ARMAZ_AR_COMPRIMIDO, "Ar comprimido (CAES)"},
    {ARMAZ_TERMICO, "Armazenamento termico (sal fundido, agua quente)"}
};

typedef enum {
    CENARIO_ABUNDANCIA,
    CENARIO_EQUILIBRIO,
    CENARIO_ATENCAO,
    CENARIO_ESCASSEZ,
    CENARIO_EMERGENCIA
} StatusCenario;

typedef struct {
    StatusCenario id;
    const char* rotulo;
} CenarioInfo;

static CenarioInfo cenarios_info[] = {
    {CENARIO_ABUNDANCIA, "Abundancia: geracao supera demanda"},
    {CENARIO_EQUILIBRIO, "Equilibrio: geracao = demanda"},
    {CENARIO_ATENCAO, "Atencao: margem baixa (<10%)"},
    {CENARIO_ESCASSEZ, "Escassez: demanda supera geracao"},
    {CENARIO_EMERGENCIA, "Emergencia: deficit critico, assembleia decide"}
};

typedef enum {
    INTER_ILHADO,
    INTER_CONECTADO,
    INTER_EXPORTANDO,
    INTER_IMPORTANDO,
    INTER_MANUTENCAO
} StatusInterconexao;

typedef struct {
    StatusInterconexao id;
    const char* rotulo;
} InterconexaoInfo;

static InterconexaoInfo interconexoes_info[] = {
    {INTER_ILHADO, "Ilhado: microgrid autonomo (sem conexao externa)"},
    {INTER_CONECTADO, "Conectado a rede regional"},
    {INTER_EXPORTANDO, "Exportando excedente (doacao)"},
    {INTER_IMPORTANDO, "Importando (recebendo doacao)"},
    {INTER_MANUTENCAO, "Em manutencao"}
};

// ============================================================================
// 2. DATACLASSES (structs)
// ============================================================================

typedef struct {
    char id[MAX_ID];
    FonteEnergia fonte;
    float capacidade_kw;
    float producao_atual_kw;
    char comunidade_id[MAX_ID];
    char status[32];
    float sustentabilidade_pct;
} UnidadeGeracao;

typedef struct {
    char id[MAX_ID];
    TipoArmazenamento tipo;
    float capacidade_kwh;
    float carga_atual_kwh;
    char comunidade_id[MAX_ID];
    int ciclos_vida;
} UnidadeArmazenamento;

typedef struct {
    char id[MAX_ID];
    char comunidade_id[MAX_ID];
    TipoConsumo tipo;
    float consumo_kw;
    char timestamp[32];
    char cidadao_ou_setor[64];
} ConsumoRegistrado;

typedef struct {
    char id[MAX_ID];
    char nome[64];
    char comunidade_id[MAX_ID];
    char unidades_geracao[MAX_ITEMS][MAX_ID];
    int num_geracao;
    char unidades_armazenamento[MAX_ITEMS][MAX_ID];
    int num_armazenamento;
    StatusInterconexao interconexao;
    float autonomia_horas;
    float geracao_total_kw;
    float demanda_total_kw;
    StatusCenario cenario;
} Microgrid;

typedef struct {
    char id[MAX_ID];
    char microgrid_id[MAX_ID];
    float deficit_kw;
    TipoConsumo tipos_priorizados[MAX_ITEMS];
    int num_priorizados;
    TipoConsumo tipos_rotacionados[MAX_ITEMS];
    int num_rotacionados;
    TipoConsumo tipos_suprimidos[MAX_ITEMS];
    int num_suprimidos;
    float duracao_estimada_h;
    bool aprovado_em_assembleia;
    char justificativa[MAX_JUSTIFICATIVA];
} AlocacaoEscassez;

// ============================================================================
// 3. ENGINE (structs + funcoes)
// ============================================================================

typedef struct {
    UnidadeGeracao geracao[MAX_ITEMS];
    int num_geracao;
    UnidadeArmazenamento armazenamento[MAX_ITEMS];
    int num_armazenamento;
    ConsumoRegistrado consumos[MAX_CONSUMOS];
    int num_consumos;
    Microgrid microgrids[MAX_MICROGRIDS];
    int num_microgrids;
    AlocacaoEscassez alocacoes[MAX_ALOCACOES];
    int num_alocacoes;
    int _gen_id;
    int _arm_id;
    int _cons_id;
    int _mg_id;
    int _aloc_id;
} EnergiaEngine;

// Funcoes de ID
void _gen_novo_id(EnergiaEngine* e, char* out) {
    e->_gen_id++;
    sprintf(out, "GEN-%04d", e->_gen_id);
}

void _arm_novo_id(EnergiaEngine* e, char* out) {
    e->_arm_id++;
    sprintf(out, "ARM-%04d", e->_arm_id);
}

void _cons_novo_id(EnergiaEngine* e, char* out) {
    e->_cons_id++;
    sprintf(out, "CON-%04d", e->_cons_id);
}

void _mg_novo_id(EnergiaEngine* e, char* out) {
    e->_mg_id++;
    sprintf(out, "GRID-%04d", e->_mg_id);
}

void _aloc_novo_id(EnergiaEngine* e, char* out) {
    e->_aloc_id++;
    sprintf(out, "ALOC-%04d", e->_aloc_id);
}

// Cadastros
UnidadeGeracao* cadastrar_geracao(EnergiaEngine* e, FonteEnergia fonte, float capacidade_kw, float producao_atual_kw, const char* comunidade_id, float sustentabilidade_pct) {
    if (e->num_geracao >= MAX_ITEMS) return NULL;
    UnidadeGeracao* u = &e->geracao[e->num_geracao];
    _gen_novo_id(e, u->id);
    u->fonte = fonte;
    u->capacidade_kw = capacidade_kw;
    u->producao_atual_kw = producao_atual_kw;
    strncpy(u->comunidade_id, comunidade_id, MAX_ID-1);
    strcpy(u->status, "operacional");
    u->sustentabilidade_pct = sustentabilidade_pct;
    e->num_geracao++;
    return u;
}

UnidadeArmazenamento* cadastrar_armazenamento(EnergiaEngine* e, TipoArmazenamento tipo, float capacidade_kwh, float carga_atual_kwh, const char* comunidade_id, int ciclos_vida) {
    if (e->num_armazenamento >= MAX_ITEMS) return NULL;
    UnidadeArmazenamento* a = &e->armazenamento[e->num_armazenamento];
    _arm_novo_id(e, a->id);
    a->tipo = tipo;
    a->capacidade_kwh = capacidade_kwh;
    a->carga_atual_kwh = carga_atual_kwh;
    strncpy(a->comunidade_id, comunidade_id, MAX_ID-1);
    a->ciclos_vida = ciclos_vida;
    e->num_armazenamento++;
    return a;
}

ConsumoRegistrado* registrar_consumo(EnergiaEngine* e, const char* comunidade_id, TipoConsumo tipo, float consumo_kw, const char* cidadao_ou_setor) {
    if (e->num_consumos >= MAX_CONSUMOS) return NULL;
    ConsumoRegistrado* c = &e->consumos[e->num_consumos];
    _cons_novo_id(e, c->id);
    strncpy(c->comunidade_id, comunidade_id, MAX_ID-1);
    c->tipo = tipo;
    c->consumo_kw = consumo_kw;
    time_t t = time(NULL);
    strftime(c->timestamp, 32, "%Y-%m-%dT%H:%M:%S", localtime(&t));
    strncpy(c->cidadao_ou_setor, cidadao_ou_setor, 63);
    e->num_consumos++;
    return c;
}

Microgrid* criar_microgrid(EnergiaEngine* e, const char* nome, const char* comunidade_id, char** unidades_geracao, int num_ger, char** unidades_armazenamento, int num_arm, StatusInterconexao interconexao) {
    if (e->num_microgrids >= MAX_MICROGRIDS) return NULL;
    Microgrid* mg = &e->microgrids[e->num_microgrids];
    _mg_novo_id(e, mg->id);
    strncpy(mg->nome, nome, 63);
    strncpy(mg->comunidade_id, comunidade_id, MAX_ID-1);
    mg->num_geracao = 0;
    for (int i = 0; i < num_ger && i < MAX_ITEMS; i++) {
        strncpy(mg->unidades_geracao[i], unidades_geracao[i], MAX_ID-1);
        mg->num_geracao++;
    }
    mg->num_armazenamento = 0;
    for (int i = 0; i < num_arm && i < MAX_ITEMS; i++) {
        strncpy(mg->unidades_armazenamento[i], unidades_armazenamento[i], MAX_ID-1);
        mg->num_armazenamento++;
    }
    mg->interconexao = interconexao;
    mg->autonomia_horas = 0.0f;
    mg->geracao_total_kw = 0.0f;
    mg->demanda_total_kw = 0.0f;
    mg->cenario = CENARIO_EQUILIBRIO;
    e->num_microgrids++;
    // _atualizar_metricas_microgrid sera chamada manualmente no demo
    return mg;
}

// Atualizacao de metricas (logica completa)
void _atualizar_metricas_microgrid(EnergiaEngine* e, const char* mg_id) {
    Microgrid* mg = NULL;
    for (int i = 0; i < e->num_microgrids; i++) {
        if (strcmp(e->microgrids[i].id, mg_id) == 0) {
            mg = &e->microgrids[i];
            break;
        }
    }
    if (!mg) return;
    float geracao = 0.0f;
    for (int i = 0; i < mg->num_geracao; i++) {
        for (int j = 0; j < e->num_geracao; j++) {
            if (strcmp(e->geracao[j].id, mg->unidades_geracao[i]) == 0) {
                geracao += e->geracao[j].producao_atual_kw;
                break;
            }
        }
    }
    float demanda = 0.0f;
    for (int i = 0; i < e->num_consumos; i++) {
        if (strcmp(e->consumos[i].comunidade_id, mg->comunidade_id) == 0) {
            demanda += e->consumos[i].consumo_kw;
        }
    }
    mg->geracao_total_kw = ((int)(geracao * 100)) / 100.0f;
    mg->demanda_total_kw = ((int)(demanda * 100)) / 100.0f;
    if (demanda == 0) {
        mg->cenario = CENARIO_ABUNDANCIA;
        return;
    }
    float margem = (geracao - demanda) / demanda;
    if (margem >= 0.2f) mg->cenario = CENARIO_ABUNDANCIA;
    else if (margem >= 0.0f) mg->cenario = CENARIO_EQUILIBRIO;
    else if (margem >= -0.1f) mg->cenario = CENARIO_ATENCAO;
    else if (margem >= -0.3f) mg->cenario = CENARIO_ESCASSEZ;
    else mg->cenario = CENARIO_EMERGENCIA;
    float armazenamento_total = 0.0f;
    for (int i = 0; i < mg->num_armazenamento; i++) {
        for (int j = 0; j < e->num_armazenamento; j++) {
            if (strcmp(e->armazenamento[j].id, mg->unidades_armazenamento[i]) == 0) {
                armazenamento_total += e->armazenamento[j].carga_atual_kwh;
                break;
            }
        }
    }
    mg->autonomia_horas = (demanda > 0) ? ((int)((armazenamento_total / demanda) * 100)) / 100.0f : 0.0f;
}

// Diagnostico completo
void diagnosticar_microgrid(EnergiaEngine* e, const char* mg_id, StatusCenario* out_cenario, float* geracao_kw, float* demanda_kw, float* deficit_kw, float* excedente_kw, float* autonomia_h, float* pct_renovavel, char* interconexao_rotulo) {
    _atualizar_metricas_microgrid(e, mg_id);
    Microgrid* mg = NULL;
    for (int i = 0; i < e->num_microgrids; i++) {
        if (strcmp(e->microgrids[i].id, mg_id) == 0) { mg = &e->microgrids[i]; break; }
    }
    if (!mg) {
        *out_cenario = CENARIO_EQUILIBRIO;
        strcpy(interconexao_rotulo, "Microgrid nao encontrada");
        return;
    }
    *geracao_kw = mg->geracao_total_kw;
    *demanda_kw = mg->demanda_total_kw;
    *deficit_kw = (mg->demanda_total_kw > mg->geracao_total_kw) ? mg->demanda_total_kw - mg->geracao_total_kw : 0.0f;
    *excedente_kw = (mg->geracao_total_kw > mg->demanda_total_kw) ? mg->geracao_total_kw - mg->demanda_total_kw : 0.0f;
    float renovavel = 0.0f;
    for (int i = 0; i < mg->num_geracao; i++) {
        for (int j = 0; j < e->num_geracao; j++) {
            if (strcmp(e->geracao[j].id, mg->unidades_geracao[i]) == 0 && fontes_info[e->geracao[j].fonte].renovavel) {
                renovavel += e->geracao[j].producao_atual_kw;
            }
        }
    }
    *pct_renovavel = (mg->geracao_total_kw > 0) ? ((int)((renovavel / mg->geracao_total_kw * 100) * 10)) / 10.0f : 0.0f;
    *autonomia_h = mg->autonomia_horas;
    *out_cenario = mg->cenario;
    strcpy(interconexao_rotulo, interconexoes_info[mg->interconexao].rotulo);
}

// Propor alocacao em escassez (logica completa)
bool propor_alocacao_escassez(EnergiaEngine* e, const char* mg_id, float duracao_estimada_h, AlocacaoEscassez* out_aloc) {
    Microgrid* mg = NULL;
    for (int i = 0; i < e->num_microgrids; i++) {
        if (strcmp(e->microgrids[i].id, mg_id) == 0) { mg = &e->microgrids[i]; break; }
    }
    if (!mg) return false;
    _atualizar_metricas_microgrid(e, mg_id);
    if (mg->cenario != CENARIO_ESCASSEZ && mg->cenario != CENARIO_EMERGENCIA) return false;
    float deficit = mg->demanda_total_kw - mg->geracao_total_kw;
    if (deficit <= 0) return false;
    // Agrupar consumo por tipo
    float consumo_por_tipo[11] = {0};
    for (int i = 0; i < e->num_consumos; i++) {
        if (strcmp(e->consumos[i].comunidade_id, mg->comunidade_id) == 0) {
            consumo_por_tipo[e->consumos[i].tipo] += e->consumos[i].consumo_kw;
        }
    }
    // Ordenar por prioridade (simplificado)
    int tipos_ordenados[11]; int num_tipos = 0;
    for (int p = 1; p <= 4; p++) {
        for (int t = 0; t < 11; t++) {
            if (consumos_info[t].prioridade == p && consumo_por_tipo[t] > 0) {
                tipos_ordenados[num_tipos++] = t;
            }
        }
    }
    float geracao_disponivel = mg->geracao_total_kw;
    out_aloc->num_priorizados = 0;
    out_aloc->num_rotacionados = 0;
    out_aloc->num_suprimidos = 0;
    for (int i = 0; i < num_tipos; i++) {
        int tipo = tipos_ordenados[i];
        float cons = consumo_por_tipo[tipo];
        if (geracao_disponivel >= cons) {
            out_aloc->tipos_priorizados[out_aloc->num_priorizados++] = tipo;
            geracao_disponivel -= cons;
        } else if (geracao_disponivel > 0) {
            out_aloc->tipos_rotacionados[out_aloc->num_rotacionados++] = tipo;
            geracao_disponivel = 0;
        } else {
            out_aloc->tipos_suprimidos[out_aloc->num_suprimidos++] = tipo;
        }
    }
    _aloc_novo_id(e, out_aloc->id);
    strncpy(out_aloc->microgrid_id, mg_id, MAX_ID-1);
    out_aloc->deficit_kw = ((int)(deficit * 100)) / 100.0f;
    out_aloc->duracao_estimada_h = duracao_estimada_h;
    out_aloc->aprovado_em_assembleia = false;
    snprintf(out_aloc->justificativa, MAX_JUSTIFICATIVA, "Deficit de %.1f kW. Geracao alocada por prioridade: essenciais garantidos, nao-essenciais em rodizio/corte. Ninguem fica sem energia essencial por dinheiro (P1).", deficit);
    if (e->num_alocacoes < MAX_ALOCACOES) {
        e->alocacoes[e->num_alocacoes] = *out_aloc;
        e->num_alocacoes++;
    }
    return true;
}

bool aprovar_alocacao(EnergiaEngine* e, const char* aloc_id) {
    for (int i = 0; i < e->num_alocacoes; i++) {
        if (strcmp(e->alocacoes[i].id, aloc_id) == 0) {
            e->alocacoes[i].aprovado_em_assembleia = true;
            return true;
        }
    }
    return false;
}

// Doacao P2P
float doar_excedente(EnergiaEngine* e, const char* mg_origem_id, const char* mg_destino_id) {
    _atualizar_metricas_microgrid(e, mg_origem_id);
    _atualizar_metricas_microgrid(e, mg_destino_id);
    Microgrid* origem = NULL; Microgrid* destino = NULL;
    for (int i = 0; i < e->num_microgrids; i++) {
        if (strcmp(e->microgrids[i].id, mg_origem_id) == 0) origem = &e->microgrids[i];
        if (strcmp(e->microgrids[i].id, mg_destino_id) == 0) destino = &e->microgrids[i];
    }
    if (!origem || !destino) return 0.0f;
    float excedente = origem->geracao_total_kw - origem->demanda_total_kw;
    float deficit = destino->demanda_total_kw - destino->geracao_total_kw;
    if (excedente <= 0 || deficit <= 0) return 0.0f;
    float doado = (excedente < deficit) ? excedente : deficit;
    origem->interconexao = INTER_EXPORTANDO;
    destino->interconexao = INTER_IMPORTANDO;
    origem->geracao_total_kw = ((int)((origem->geracao_total_kw - doado) * 100)) / 100.0f;
    destino->geracao_total_kw = ((int)((destino->geracao_total_kw + doado) * 100)) / 100.0f;
    _atualizar_metricas_microgrid(e, mg_origem_id);
    _atualizar_metricas_microgrid(e, mg_destino_id);
    return ((int)(doado * 10)) / 10.0f;
}

// Auditoria de eficiencia
void auditoria_eficiencia(EnergiaEngine* e, const char* comunidade_id, float* consumo_total, char alertas[][256], int* num_alertas, char consumo_por_tipo_str[512]) {
    float total = 0.0f;
    float por_tipo[11] = {0};
    for (int i = 0; i < e->num_consumos; i++) {
        if (strcmp(e->consumos[i].comunidade_id, comunidade_id) == 0) {
            total += e->consumos[i].consumo_kw;
            por_tipo[e->consumos[i].tipo] += e->consumos[i].consumo_kw;
        }
    }
    *consumo_total = ((int)(total * 100)) / 100.0f;
    *num_alertas = 0;
    strcpy(consumo_por_tipo_str, "");
    for (int t = 0; t < 11; t++) {
        if (por_tipo[t] > 0) {
            char buf[128];
            snprintf(buf, 128, "%s: %.1f kW; ", consumos_info[t].rotulo, por_tipo[t]);
            strcat(consumo_por_tipo_str, buf);
            if (t == CONSUMO_RESIDENCIAL_EXCEDENTE && por_tipo[t] > total * 0.3f) {
                snprintf(alertas[*num_alertas], 256, "Consumo residencial excedente alto (%.1f kW, %.0f%% do total). Lembrar: eficiencia liberta capacidade para a comunidade.", por_tipo[t], por_tipo[t]/total*100);
                (*num_alertas)++;
            }
            if (t == CONSUMO_PRODUCAO_BENS && por_tipo[t] > total * 0.4f) {
                snprintf(alertas[*num_alertas], 256, "Producao de bens consome %.1f kW. Otimizar processos = mais capacidade para saude e educacao.", por_tipo[t]);
                (*num_alertas)++;
            }
        }
    }
}

// Scorecard
void scorecard(EnergiaEngine* e, int* unidades_geracao, int* unidades_armazenamento, int* microgrids, float* geracao_total_kw, float* demanda_total_kw, float* excedente_kw, float* pct_renovavel, float* armazenamento_kwh, int* alocacoes_escassez, int* doacoes_realizadas) {
    *unidades_geracao = e->num_geracao;
    *unidades_armazenamento = e->num_armazenamento;
    *microgrids = e->num_microgrids;
    float gtotal = 0, renov = 0, dtotal = 0, atotal = 0;
    for (int i = 0; i < e->num_geracao; i++) {
        gtotal += e->geracao[i].producao_atual_kw;
        if (fontes_info[e->geracao[i].fonte].renovavel) renov += e->geracao[i].producao_atual_kw;
    }
    for (int i = 0; i < e->num_consumos; i++) dtotal += e->consumos[i].consumo_kw;
    for (int i = 0; i < e->num_armazenamento; i++) atotal += e->armazenamento[i].carga_atual_kwh;
    *geracao_total_kw = ((int)(gtotal * 10)) / 10.0f;
    *demanda_total_kw = ((int)(dtotal * 10)) / 10.0f;
    *excedente_kw = ((int)(fmaxf(0, gtotal - dtotal) * 10)) / 10.0f;
    *pct_renovavel = (gtotal > 0) ? ((int)((renov / gtotal * 100) * 10)) / 10.0f : 0.0f;
    *armazenamento_kwh = ((int)(atotal * 10)) / 10.0f;
    *alocacoes_escassez = e->num_alocacoes;
    *doacoes_realizadas = 0;
    for (int i = 0; i < e->num_microgrids; i++) {
        if (e->microgrids[i].interconexao == INTER_EXPORTANDO) (*doacoes_realizadas)++;
    }
}

// ============================================================================
// 4. DEMO (main completo)
// ============================================================================

int main() {
    EnergiaEngine e = {0};
    printf("======================================================================\n");
    printf("OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso\n");
    printf("======================================================================\n");

    // CENARIO 1 - Solar Village
    printf("\n[CENARIO 1] Solar Village -- abundancia (geracao > demanda)\n");
    UnidadeGeracao* g1 = cadastrar_geracao(&e, FONTE_SOLAR, 500.0f, 480.0f, "solar_village", 100.0f);
    UnidadeGeracao* g2 = cadastrar_geracao(&e, FONTE_EOLICA, 300.0f, 250.0f, "solar_village", 100.0f);
    UnidadeArmazenamento* a1 = cadastrar_armazenamento(&e, ARMAZ_BATERIA_LITIO, 2000.0f, 1500.0f, "solar_village", 10000);
    UnidadeArmazenamento* a2 = cadastrar_armazenamento(&e, ARMAZ_BATERIA_FLUXO, 5000.0f, 4000.0f, "solar_village", 10000);
    registrar_consumo(&e, "solar_village", CONSUMO_ESSENCIAL_VIDA, 120.0f, "");
    registrar_consumo(&e, "solar_village", CONSUMO_SAUDE, 40.0f, "");
    registrar_consumo(&e, "solar_village", CONSUMO_COMUNICACAO, 30.0f, "");
    registrar_consumo(&e, "solar_village", CONSUMO_EDUCACAO, 50.0f, "");
    registrar_consumo(&e, "solar_village", CONSUMO_CULTURA_LAZER, 80.0f, "");
    registrar_consumo(&e, "solar_village", CONSUMO_RESIDENCIAL_EXCEDENTE, 100.0f, "");
    char* ger1[2] = {g1->id, g2->id};
    char* arm1[2] = {a1->id, a2->id};
    Microgrid* mg1 = criar_microgrid(&e, "Solar Village Grid", "solar_village", ger1, 2, arm1, 2, INTER_CONECTADO);
    StatusCenario c1; float gkw1, dkw1, def1, exc1, aut1, pr1; char inter1[128];
    diagnosticar_microgrid(&e, mg1->id, &c1, &gkw1, &dkw1, &def1, &exc1, &aut1, &pr1, inter1);
    printf("  Geracao: %.2f kW | Demanda: %.2f kW\n", gkw1, dkw1);
    printf("  Excedente: %.2f kW | Renovavel: %.1f%%\n", exc1, pr1);
    printf("  Autonomia (ilhado): %.2fh\n", aut1);
    printf("  Cenario: %s\n", cenarios_info[c1].rotulo);
    printf("  Energia para QUALQUER uso: sim, sem conta, sem medidor de cobranca.\n");

    // CENARIO 2 - Vale Seco
    printf("\n[CENARIO 2] Vale Seco -- escassez (seca reduziu hidro)\n");
    UnidadeGeracao* g3 = cadastrar_geracao(&e, FONTE_HIDRO, 400.0f, 150.0f, "vale_seco", 100.0f);
    UnidadeGeracao* g4 = cadastrar_geracao(&e, FONTE_SOLAR, 200.0f, 180.0f, "vale_seco", 100.0f);
    UnidadeArmazenamento* a3 = cadastrar_armazenamento(&e, ARMAZ_HIDROGENIO, 3000.0f, 800.0f, "vale_seco", 10000);
    registrar_consumo(&e, "vale_seco", CONSUMO_ESSENCIAL_VIDA, 100.0f, "");
    registrar_consumo(&e, "vale_seco", CONSUMO_SAUDE, 60.0f, "");
    registrar_consumo(&e, "vale_seco", CONSUMO_COMUNICACAO, 20.0f, "");
    registrar_consumo(&e, "vale_seco", CONSUMO_EDUCACAO, 40.0f, "");
    registrar_consumo(&e, "vale_seco", CONSUMO_PRODUCAO_BENS, 80.0f, "");
    registrar_consumo(&e, "vale_seco", CONSUMO_CULTURA_LAZER, 50.0f, "");
    char* ger2[2] = {g3->id, g4->id};
    char* arm2[1] = {a3->id};
    Microgrid* mg2 = criar_microgrid(&e, "Vale Seco Grid", "vale_seco", ger2, 2, arm2, 1, INTER_CONECTADO);
    StatusCenario c2; float gkw2, dkw2, def2, exc2, aut2, pr2; char inter2[128];
    diagnosticar_microgrid(&e, mg2->id, &c2, &gkw2, &dkw2, &def2, &exc2, &aut2, &pr2, inter2);
    printf("  Geracao: %.2f kW | Demanda: %.2f kW\n", gkw2, dkw2);
    printf("  Deficit: %.2f kW | Cenario: %s\n", def2, cenarios_info[c2].rotulo);
    printf("  Autonomia: %.2fh\n", aut2);

    // ALOCACAO DEMOCRATICA
    printf("\n[ALOCACAO DEMOCRATICA EM ESCASSEZ]\n");
    AlocacaoEscassez aloc = {0};
    if (propor_alocacao_escassez(&e, mg2->id, 48.0f, &aloc)) {
        printf("  Proposta %s (assembleia precisa aprovar):\n", aloc.id);
        printf("  Deficit: %.2f kW | Duracao estimada: %.1fh\n", aloc.deficit_kw, aloc.duracao_estimada_h);
        printf("  GARANTIDOS (prioridade): ");
        for (int i = 0; i < aloc.num_priorizados; i++) printf("%s; ", consumos_info[aloc.tipos_priorizados[i]].rotulo);
        printf("\n  EM RODIZIO: ");
        for (int i = 0; i < aloc.num_rotacionados; i++) printf("%s; ", consumos_info[aloc.tipos_rotacionados[i]].rotulo);
        printf("\n  SUPRIMIDOS: ");
        for (int i = 0; i < aloc.num_suprimidos; i++) printf("%s; ", consumos_info[aloc.tipos_suprimidos[i]].rotulo);
        printf("\n  Justificativa: %s\n", aloc.justificativa);
        aprovar_alocacao(&e, aloc.id);
        printf("  Aprovado em assembleia: %s\n", aloc.aprovado_em_assembleia ? "true" : "false");
    }

    // DOACAO P2P
    printf("\n[DOACAO P2P] Solar Village doe excedente para Vale Seco\n");
    float doado = doar_excedente(&e, mg1->id, mg2->id);
    if (doado > 0) {
        printf("  %.1f kW doados (sem dinheiro, sem cobranca).\n", doado);
        StatusCenario cpos; float gpos, dpos, defpos, excpos, autpos, prpos; char interpos[128];
        diagnosticar_microgrid(&e, mg2->id, &cpos, &gpos, &dpos, &defpos, &excpos, &autpos, &prpos, interpos);
        printf("  Vale Seco pos-doacao: geracao=%.2f kW, deficit=%.2f kW, cenario=%s\n", gpos, defpos, interpos);
    }

    // AUDITORIA
    printf("\n[AUDITORIA DE EFICIENCIA -- dever civico, nao economia]\n");
    float cons_total; char alertas[8][256]; int nalertas; char por_tipo_str[512];
    auditoria_eficiencia(&e, "solar_village", &cons_total, alertas, &nalertas, por_tipo_str);
    printf("  Comunidade: solar_village\n");
    printf("  Consumo total: %.2f kW\n", cons_total);
    printf("  %s\n", por_tipo_str);
    for (int i = 0; i < nalertas; i++) printf("  ALERTA: %s\n", alertas[i]);
    printf("  Energia e gratuita. Eficiencia nao economiza dinheiro -- LIBERTA capacidade para quem precisa. E kaizen civico.\n");

    // SCORECARD
    printf("\n======================================================================\n");
    printf("[SCORECARD ENERGETICO DA REPUBLICA]\n");
    printf("======================================================================\n");
    int ug, ua, umg, nalocs, ndoacoes; float gt, dt, ex, pr, at;
    scorecard(&e, &ug, &ua, &umg, &gt, &dt, &ex, &pr, &at, &nalocs, &ndoacoes);
    printf("  unidades_geracao............. %d\n", ug);
    printf("  unidades_armazenamento....... %d\n", ua);
    printf("  microgrids................... %d\n", umg);
    printf("  geracao_total_kw............. %.1f\n", gt);
    printf("  demanda_total_kw............. %.1f\n", dt);
    printf("  excedente_kw................. %.1f\n", ex);
    printf("  pct_renovavel................ %.1f\n", pr);
    printf("  armazenamento_kwh............ %.1f\n", at);
    printf("  alocacoes_escassez........... %d\n", nalocs);
    printf("  doacoes_realizadas........... %d\n", ndoacoes);

    // FONTES
    printf("\n[FONTES DE ENERGIA DA REPUBLICA]\n");
    for (int f = 0; f < 8; f++) {
        printf("  %s [ %s ]\n", fontes_info[f].rotulo, fontes_info[f].renovavel ? "renovavel" : "NAO-renovavel");
    }

    // FILOSOFIA
    printf("\n======================================================================\n");
    printf("FILOSOFIA -- Por que energia e gratuita para todo e qualquer uso\n");
    printf("======================================================================\n");
    printf("ENERGIA NAO E MERCADORIA. E CONDICAO DE VIDA.\nCozinhar precisa de energia. Aquecer precisa de energia.\nCurar precisa de energia. Comunicar precisa de energia.\nEstudar precisa de energia. Criar precisa de energia.\nCobrar por energia e cobrar por EXISTIR.\n\nO ARGUMENTO DA ESCASSEZ (e por que e falso):\nO capitalismo diz: \"se energia e gratis, todos desperdicam.\"\nFalso. O capitalista desperdica porque o custo e EXTERNO ao lucro.\nO cidadao da Republica SABE que a energia que desperdica falta para o vizinho.\nEficiencia nao economiza dinheiro -- LIBERTA capacidade para a comunidade.\n\nA UNICA ESCASSEZ REAL (e como se resolve):\nQuando a geracao nao cobre a demanda (seca, falha), a assembleia decide:\n1. Essenciais (vida, saude, comunicacao) SEMPRE garantidos.\n2. Nao-essenciais em rodizio democratico.\n3. Ninguem fica sem energia por DINHEIRO. So por PRIORIDADE civica.\n4. A solucao de longo prazo e GERAR MAIS, nao racionar.\nO capitalismo raciona por preco (quem tem dinheiro usa, quem nao tem corta).\nA Republica aloca por prioridade (todos tem o essencial, o resto e civico).\n\nA REVOLUCAO ENERGETICA:\n1. Cada comunidade gera a propria energia (geracao distribuida).\n2. Excedente e DOADO, nao vendido (P2P, sem intermediario).\n3. Armazenamento comunitario (baterias compartilhadas).\n4. 100%% renovavel (a Republica respeita o planeta que a sustenta).\n5. Nucleo essencial garantido para TODOS, sem excecao, sem condicao.\n6. \"Para todo e qualquer uso\" -- a Republica nao pergunta PARA QUE.\n   Pergunta quanto voce PRECISA, e garante que tem.\n\nA ENERGIA E O AR DA CIVILIZACAO.\nNinguem cobra pelo ar. Ninguem deve cobrar pela energia.\n");

    return 0;
}
