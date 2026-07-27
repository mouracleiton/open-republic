// OpenDrone -- P10: Soberania Aerea Civica
// =========================================
// O decimo principio constitucional da Republica Aberta.
//
// "O ceu nao e de ninguem. Portanto, e de todos." -- principio do espaco aereo
// como bem comum, analogo ao principio da terra (OpenAgrarianRevolution):
// guardiao, nao dono.
//
// DISTINCAO CRITICA (a tese do modulo):
// - Drones (VANTs -- Veiculos Aereos Nao Tripulados) sao INFRAESTRUTURA.
// - Como toda infraestrutura na Republica, pertencem ao dominio publico e
//   servem a P1 (erradicar miserabilidade), nao a vigilancia, nem a lucro,
//   nem a guerra.
// - Um ceu cheio de drones comerciais entregando pacotes de consumo enquanto
//   criancas passam fome e um monumento a distopia. OpenDrone transforma o
//   espaco aereo em bem comum civico.
//
// TRES PROIBICOES CONSTITUCIONAIS (o triplo NAO):
// 1. NAO VIGIA: drones com camera de vigilancia sao PROIBIDOS. Camera so para
//    navegacao (feed local, nao gravado, nao transmitido para central).
// 2. NAO MATA: drones nao podem carregar armas. Ponto. Sem excecoes. Um drone
//    armado nao e drone -- e arma. E arma pertence ao museu da Republica.
// 3. NAO ESPIONA: drones nao coletam dados pessoais. Entregam suprimentos,
//    nao metadados. O trajeto de voo e publico; o destinatario e privado.
//
// USOS PERMITIDOS (missao civica):
// - Entrega de suprimentos (medicamentos, alimentos, agua) a areas isoladas
// - Mapeamento ambiental (desmatamento, queimadas, qualidade da agua)
// - Busca e resgate em desastres naturais
// - Conectividade aerea (rede mesh em areas sem cobertura)
// - Inspecao de infraestrutura critica (diques, barragens, pontes)
//
// GATE DE MISSAO (P10):
// Toda missao de drone deve passar por um gate antes de decolar:
// - Proposito civico declarado e aprovado
// - Zona de voo geofenceada (nao sobrevoa residencia privada sem consentimento)
// - Log publico (trajeto, duracao, proposito)
// - Razao de rejeicao explicita se negada
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1: Drones que entregam medicamentos em area isolada combatem miserabilidade.
//       Drones que entregam propaganda ampliam miserabilidade. P10 escolhe.
// - P2: Drones que vigiam destroem autonomia. Drone que entrega remedio amplia
//       autonomia (acesso). O instrumento nao e neutro -- o USO define.
// - P4: Espaco aereo e decisao coletiva. Nenhuma corporacao o ocupa sozinha.
// - P8: Drone autonomo e IA que atua no mundo fisico. Se ampliar inteligencia/
//       reduzir miserabilidade = cumpre P8. Se vigiar = viola P8.
//
// Author: OpenRepublic Team
// Versao C transpilada fielmente do Python (open_drone.py)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdint.h>
#include <time.h>
#include <math.h>

// ============================================================================
// 1. ENUMS (modulo-level, nunca aninhados) -- padrao anti_polarization.c
// ============================================================================

typedef enum {
    TIPO_MISSAO_ENTREGA_SUPRIMENTOS = 0,
    TIPO_MISSAO_MAPEAMENTO_AMBIENTAL,
    TIPO_MISSAO_BUSCA_RESGATE,
    TIPO_MISSAO_CONECTIVIDADE,
    TIPO_MISSAO_INSPECAO_INFRA,
    TIPO_MISSAO_AGRICULTURA_CIVICA
} TipoMissao;

static const char* TIPO_MISSAO_ID[] = {
    "entrega_suprimentos", "mapeamento_ambiental", "busca_resgate",
    "conectividade", "inspecao_infra", "agricultura_civica"
};

static const char* TIPO_MISSAO_ROTULO[] = {
    "Entrega de suprimentos (remedio, comida, agua)",
    "Mapeamento ambiental (desmatamento, queimadas)",
    "Busca e resgate em desastre natural",
    "Rede mesh aerea (area sem cobertura)",
    "Inspecao de infraestrutura critica",
    "Agricultura de precisao comunitaria"
};

static const int TIPO_MISSAO_PRIORIDADE[] = {1, 1, 0, 1, 1, 2};

typedef enum {
    STATUS_PLANEJADA = 0,
    STATUS_APROVADA,
    STATUS_EM_VOO,
    STATUS_CONCLUIDA,
    STATUS_REJEITADA,
    STATUS_CANCELADA,
    STATUS_FALHOU
} StatusMissao;

static const char* STATUS_ID[] = {
    "planejada", "aprovada", "em_voo", "concluida", "rejeitada", "cancelada", "falhou"
};

typedef enum {
    TIPO_PROIBICAO_VIGILANCIA = 0,
    TIPO_PROIBICAO_ARMAMENTO,
    TIPO_PROIBICAO_ESPIONAGEM,
    TIPO_PROIBICAO_PRIVADO_SEM_CONSENTIMENTO,
    TIPO_PROIBICAO_COMERCIAL_NAO_CIVICO
} TipoProibicao;

static const char* TIPO_PROIBICAO_ID[] = {
    "vigilancia", "armamento", "espionagem", "privado_sem_consentimento", "comercial_nao_civico"
};

static const char* TIPO_PROIBICAO_ROTULO[] = {
    "Camera de vigilancia (feed gravado/transmitido)",
    "Carrega arma ou explosivo",
    "Coleta dados pessoais (facial, placa, biometria)",
    "Sobrevoa area privada sem consentimento",
    "Uso comercial sem proposito civico (propaganda)"
};

static const int TIPO_PROIBICAO_GRAVIDADE[] = {5, 5, 5, 4, 3};

typedef enum {
    VEREDITO_APROVADA = 0,
    VEREDITO_APROVADA_COM_RESTRICOES,
    VEREDITO_REJEITADA,
    VEREDITO_BLOQUEADA
} VereditoGate;

static const char* VEREDITO_ID[] = {
    "aprovada", "aprovada_restricoes", "rejeitada", "bloqueada"
};

static const char* VEREDITO_ROTULO[] = {
    "Missao aprovada: proposito civico confirmado",
    "Aprovada com restricoes (geofence ampliado)",
    "Missao rejeitada: viola uma proibicao P10",
    "Missao bloqueada: e vetor de vigilancia/arma"
};

typedef enum {
    PRIORIDADE_RESGATE_VIDA = 0,
    PRIORIDADE_ENTREGA_CRITICA,
    PRIORIDADE_MAPEAMENTO_AMBIENTAL,
    PRIORIDADE_CONECTIVIDADE,
    PRIORIDADE_INSPECAO,
    PRIORIDADE_OUTROS
} PrioridadeCorredor;

static const char* PRIORIDADE_ID[] = {
    "resgate_vida", "entrega_critica", "mapeamento", "conectividade", "inspecao", "outros"
};

static const char* PRIORIDADE_ROTULO[] = {
    "Resgate de vida (emergencia medica)",
    "Entrega critica (remedio urgente)",
    "Mapeamento ambiental de rotina",
    "Conectividade mesh",
    "Inspecao de infraestrutura",
    "Outros usos civicos"
};

static const int PRIORIDADE_VALOR[] = {0, 1, 2, 2, 3, 4};

// ============================================================================
// 2. STRUCTS (typedef struct)
// ============================================================================

typedef struct {
    double lat;
    double lon;
} Coordenada;

typedef struct {
    char id[32];
    Coordenada centro;
    double raio_metros;
    char descricao[256];
    bool sobrevoa_privado;
    bool consentimento_privado;
} ZonaVoo;

typedef struct {
    char id[32];
    char modelo[64];
    int autonomia_minutos;
    double carga_max_kg;
    bool tem_camera_navegacao;
    bool tem_camera_vigilancia;
    bool tem_armamento;
    bool coleta_dados_pessoais;
    bool ativo;
    int missoes_concluidas;
} Drone;

typedef struct {
    char id[32];
    char drone_id[32];
    TipoMissao tipo;
    char descricao[256];
    ZonaVoo zona;
    Coordenada destino;
    bool tem_destino;
    char carga_descricao[128];
    bool urgencia;
    StatusMissao status;
    VereditoGate veredito_gate;
    char razao_rejeicao[256];
    TipoProibicao proibicoes_violadas[8];
    int num_proibicoes;
    char criada_em[32];
    char concluida_em[32];
    Coordenada log_trajeto[64];
    int num_trajeto;
} MissaoDrone;

typedef struct {
    char missao_id[32];
    char drone_id[32];
    char tipo_missao[32];
    double duracao_minutos;
    double distancia_km;
    char decolagem[32];
    char pouso[32];
    double destino_lat;
    double destino_lon;
    bool sucesso;
    char observacoes[256];
} LogVoo;

typedef struct {
    char regiao_id[32];
    int total_drones;
    int drones_ativos;
    int missoes_concluidas;
    int missoes_rejeitadas;
    int entregas_criticas;
    int resgates;
    double horas_voo;
    int violacoes_detectadas;
    double cobertura_km2;
} MetricaFrota;

typedef struct {
    Drone drones[128];
    int num_drones;
    MissaoDrone missoes[256];
    int num_missoes;
    ZonaVoo zonas[64];
    int num_zonas;
    LogVoo logs[256];
    int num_logs;
    int _drone_id;
    int _missao_id;
    int _zona_id;
} DroneCivicoEngine;

// ============================================================================
// 3. TABELAS
// ============================================================================

static const char* DESCRICOES_PROIBICOES[] = {
    "Camera de vigilancia = feed gravado ou transmitido para central de monitoramento. PERMITIDO: camera de navegacao (feed local em tempo real, nao gravado, processado no proprio drone). A linha e: a camera ajuda o drone a voar, nao ajuda o Estado a vigiar.",
    "Qualquer arma, explosivo, ou dispositivo projetado para causar dano fisico. Um drone armado nao e drone -- e arma. Armas pertencem ao museu da Republica (P7). Sem excecoes, mesmo para 'defesa'.",
    "Reconhecimento facial, leitura de placas, coleta de biometria, captura de dados de rede (wifi bluetooth scanning). O drone entrega suprimentos; NAO entrega metadados sobre o destinatario.",
    "Sobrevoar residencia, patio, ou propriedade privada sem consentimento explicito do morador. Excecao: resgate de vida (P1 > privacidade), mas o log fica publico e auditavel.",
    "Uso para entrega de consumo de luxo, propaganda, marketing, ou qualquer fim que nao reduza miserabilidade ou amplie acesso. Drones nao sao brinquedo de consumo -- sao infraestrutura de sobrevivencia."
};

static const int PRIORIDADE_POR_TIPO[] = {1, 2, 0, 2, 3, 3}; // index por TipoMissao

// ============================================================================
// 4. ENGINE (funcoes que recebem DroneCivicoEngine*)
// ============================================================================

void engine_init(DroneCivicoEngine* e) {
    memset(e, 0, sizeof(DroneCivicoEngine));
    e->_drone_id = 0;
    e->_missao_id = 0;
    e->_zona_id = 0;
}

void _drone_id_novo(DroneCivicoEngine* e, char* out) {
    e->_drone_id++;
    sprintf(out, "DRONE-%04d", e->_drone_id);
}

void _missao_id_novo(DroneCivicoEngine* e, char* out) {
    e->_missao_id++;
    sprintf(out, "MISSAO-%04d", e->_missao_id);
}

void _zona_id_novo(DroneCivicoEngine* e, char* out) {
    e->_zona_id++;
    sprintf(out, "ZONA-%04d", e->_zona_id);
}

ZonaVoo* registrar_zona(DroneCivicoEngine* e, double lat, double lon, double raio, const char* desc, bool sobrevoa, bool consent) {
    ZonaVoo* z = &e->zonas[e->num_zonas];
    _zona_id_novo(e, z->id);
    z->centro.lat = lat;
    z->centro.lon = lon;
    z->raio_metros = raio;
    strncpy(z->descricao, desc, sizeof(z->descricao)-1);
    z->sobrevoa_privado = sobrevoa;
    z->consentimento_privado = consent;
    e->num_zonas++;
    return z;
}

Drone* registrar_drone(DroneCivicoEngine* e, const char* modelo, int autonomia, double carga,
                       bool cam_nav, bool cam_vig, bool armado, bool coleta) {
    Drone* d = &e->drones[e->num_drones];
    _drone_id_novo(e, d->id);
    strncpy(d->modelo, modelo, sizeof(d->modelo)-1);
    d->autonomia_minutos = autonomia;
    d->carga_max_kg = carga;
    d->tem_camera_navegacao = cam_nav;
    d->tem_camera_vigilancia = cam_vig;
    d->tem_armamento = armado;
    d->coleta_dados_pessoais = coleta;
    d->ativo = !(cam_vig || armado || coleta);
    d->missoes_concluidas = 0;
    e->num_drones++;
    return d;
}

MissaoDrone* registrar_missao(DroneCivicoEngine* e, const char* drone_id, TipoMissao tipo,
                              const char* desc, ZonaVoo* zona, Coordenada* dest, const char* carga, bool urg) {
    MissaoDrone* m = &e->missoes[e->num_missoes];
    _missao_id_novo(e, m->id);
    strncpy(m->drone_id, drone_id, sizeof(m->drone_id)-1);
    m->tipo = tipo;
    strncpy(m->descricao, desc, sizeof(m->descricao)-1);
    m->zona = *zona;
    if (dest) { m->destino = *dest; m->tem_destino = true; } else { m->tem_destino = false; }
    strncpy(m->carga_descricao, carga, sizeof(m->carga_descricao)-1);
    m->urgencia = urg;
    m->status = STATUS_PLANEJADA;
    m->num_proibicoes = 0;
    time_t t = time(NULL);
    strftime(m->criada_em, sizeof(m->criada_em), "%Y-%m-%dT%H:%M:%S", localtime(&t));
    e->num_missoes++;
    return m;
}

TipoProibicao* auditar_proibicoes(DroneCivicoEngine* e, MissaoDrone* m, int* num_out) {
    static TipoProibicao viol[8];
    int n = 0;
    Drone* d = NULL;
    for (int i = 0; i < e->num_drones; i++) if (strcmp(e->drones[i].id, m->drone_id) == 0) { d = &e->drones[i]; break; }
    if (!d) { viol[n++] = TIPO_PROIBICAO_COMERCIAL_NAO_CIVICO; *num_out = n; return viol; }

    if (d->tem_armamento) viol[n++] = TIPO_PROIBICAO_ARMAMENTO;
    if (d->tem_camera_vigilancia) viol[n++] = TIPO_PROIBICAO_VIGILANCIA;
    if (d->coleta_dados_pessoais) viol[n++] = TIPO_PROIBICAO_ESPIONAGEM;
    if (m->zona.sobrevoa_privado && !m->zona.consentimento_privado) {
        if (m->tipo != TIPO_MISSAO_BUSCA_RESGATE) viol[n++] = TIPO_PROIBICAO_PRIVADO_SEM_CONSENTIMENTO;
    }
    // comercial check (simplificado)
    if (strstr(m->descricao, "propaganda") || strstr(m->descricao, "black friday") ||
        strstr(m->carga_descricao, "marketing") || strstr(m->carga_descricao, "brinde")) {
        viol[n++] = TIPO_PROIBICAO_COMERCIAL_NAO_CIVICO;
    }
    m->num_proibicoes = n;
    for (int i = 0; i < n; i++) m->proibicoes_violadas[i] = viol[i];
    *num_out = n;
    return viol;
}

VereditoGate aprovar_missao(DroneCivicoEngine* e, const char* missao_id, char* razao_out) {
    MissaoDrone* m = NULL;
    for (int i = 0; i < e->num_missoes; i++) if (strcmp(e->missoes[i].id, missao_id) == 0) { m = &e->missoes[i]; break; }
    if (!m) { strcpy(razao_out, "Missao nao encontrada"); return VEREDITO_REJEITADA; }

    int nviol = 0;
    auditar_proibicoes(e, m, &nviol);
    int grav_max = 0;
    for (int i = 0; i < m->num_proibicoes; i++) {
        int g = TIPO_PROIBICAO_GRAVIDADE[m->proibicoes_violadas[i]];
        if (g > grav_max) grav_max = g;
    }

    if (grav_max >= 5) {
        m->veredito_gate = VEREDITO_BLOQUEADA;
        m->status = STATUS_REJEITADA;
        strcpy(m->razao_rejeicao, "MISSAO BLOQUEADA: viola proibicao constitucional P10");
        strcpy(razao_out, m->razao_rejeicao);
        return VEREDITO_BLOQUEADA;
    }
    if (m->num_proibicoes > 0) {
        m->veredito_gate = VEREDITO_REJEITADA;
        m->status = STATUS_REJEITADA;
        strcpy(m->razao_rejeicao, "Missao rejeitada por violacao de proibicao P10");
        strcpy(razao_out, m->razao_rejeicao);
        return VEREDITO_REJEITADA;
    }

    m->veredito_gate = VEREDITO_APROVADA;
    m->status = STATUS_APROVADA;
    strcpy(razao_out, "Missao aprovada pelo gate P10");
    return VEREDITO_APROVADA;
}

bool decolar(DroneCivicoEngine* e, const char* missao_id) {
    for (int i = 0; i < e->num_missoes; i++) {
        if (strcmp(e->missoes[i].id, missao_id) == 0) {
            if (e->missoes[i].status == STATUS_APROVADA) {
                e->missoes[i].status = STATUS_EM_VOO;
                return true;
            }
        }
    }
    return false;
}

LogVoo* concluir_missao(DroneCivicoEngine* e, const char* missao_id, double duracao, double dist, bool sucesso, const char* obs) {
    MissaoDrone* m = NULL;
    for (int i = 0; i < e->num_missoes; i++) if (strcmp(e->missoes[i].id, missao_id) == 0) { m = &e->missoes[i]; break; }
    if (!m || m->status != STATUS_EM_VOO) return NULL;

    m->status = sucesso ? STATUS_CONCLUIDA : STATUS_FALHOU;
    time_t t = time(NULL);
    strftime(m->concluida_em, sizeof(m->concluida_em), "%Y-%m-%dT%H:%M:%S", localtime(&t));

    for (int i = 0; i < e->num_drones; i++) {
        if (strcmp(e->drones[i].id, m->drone_id) == 0 && sucesso) {
            e->drones[i].missoes_concluidas++;
            break;
        }
    }

    LogVoo* log = &e->logs[e->num_logs];
    strcpy(log->missao_id, m->id);
    strcpy(log->drone_id, m->drone_id);
    strcpy(log->tipo_missao, TIPO_MISSAO_ID[m->tipo]);
    log->duracao_minutos = duracao;
    log->distancia_km = dist;
    strcpy(log->decolagem, m->criada_em);
    strcpy(log->pouso, m->concluida_em);
    log->destino_lat = m->tem_destino ? m->destino.lat : 0;
    log->destino_lon = m->tem_destino ? m->destino.lon : 0;
    log->sucesso = sucesso;
    strncpy(log->observacoes, obs, sizeof(log->observacoes)-1);
    e->num_logs++;
    return log;
}

const char* resolver_conflito_corredor(DroneCivicoEngine* e, const char* ma_id, const char* mb_id) {
    MissaoDrone *ma = NULL, *mb = NULL;
    for (int i = 0; i < e->num_missoes; i++) {
        if (strcmp(e->missoes[i].id, ma_id) == 0) ma = &e->missoes[i];
        if (strcmp(e->missoes[i].id, mb_id) == 0) mb = &e->missoes[i];
    }
    if (!ma || !mb) return NULL;

    int pri_a = PRIORIDADE_POR_TIPO[ma->tipo];
    int pri_b = PRIORIDADE_POR_TIPO[mb->tipo];
    if (ma->urgencia && !mb->urgencia) return ma->id;
    if (mb->urgencia && !ma->urgencia) return mb->id;
    if (pri_a < pri_b) return ma->id;
    if (pri_b < pri_a) return mb->id;
    return NULL;
}

MetricaFrota medir_frota(DroneCivicoEngine* e, const char* regiao) {
    MetricaFrota f = {0};
    strncpy(f.regiao_id, regiao, sizeof(f.regiao_id)-1);
    f.total_drones = e->num_drones;
    for (int i = 0; i < e->num_drones; i++) if (e->drones[i].ativo) f.drones_ativos++;
    for (int i = 0; i < e->num_missoes; i++) {
        if (e->missoes[i].status == STATUS_CONCLUIDA) {
            f.missoes_concluidas++;
            if (e->missoes[i].tipo == TIPO_MISSAO_ENTREGA_SUPRIMENTOS) f.entregas_criticas++;
            if (e->missoes[i].tipo == TIPO_MISSAO_BUSCA_RESGATE) f.resgates++;
        }
        if (e->missoes[i].status == STATUS_REJEITADA) f.missoes_rejeitadas++;
        f.violacoes_detectadas += e->missoes[i].num_proibicoes;
    }
    for (int i = 0; i < e->num_logs; i++) f.horas_voo += e->logs[i].duracao_minutos;
    f.horas_voo /= 60.0;
    for (int i = 0; i < e->num_zonas; i++) {
        f.cobertura_km2 += 3.14159 * e->zonas[i].raio_metros * e->zonas[i].raio_metros;
    }
    f.cobertura_km2 /= 1000000.0;
    return f;
}

void scorecard(DroneCivicoEngine* e) {
    MetricaFrota f = medir_frota(e, "default");
    printf("  drones_registrados........... %d\n", f.total_drones);
    printf("  drones_ativos................ %d\n", f.drones_ativos);
    printf("  drones_bloqueados............ %d\n", f.total_drones - f.drones_ativos);
    printf("  missoes_concluidas........... %d\n", f.missoes_concluidas);
    printf("  missoes_rejeitadas........... %d\n", f.missoes_rejeitadas);
    printf("  entregas_criticas............ %d\n", f.entregas_criticas);
    printf("  resgates_realizados.......... %d\n", f.resgates);
    printf("  horas_voo_total.............. %.1f\n", f.horas_voo);
    printf("  violacoes_detectadas......... %d\n", f.violacoes_detectadas);
    printf("  cobertura_km2................ %.2f\n", f.cobertura_km2);
    int total = f.missoes_concluidas + f.missoes_rejeitadas;
    double taxa = total > 0 ? (f.missoes_concluidas * 100.0 / total) : 0;
    printf("  taxa_aprovacao............... %.1f%%\n", taxa);
}

// ============================================================================
// 5. MAIN (demo com 5 cenarios)
// ============================================================================

int main(void) {
    printf("======================================================================\n");
    printf("OpenDrone -- P10: Soberania Aerea Civica\n");
    printf("======================================================================\n");

    DroneCivicoEngine engine;
    engine_init(&engine);

    // FROTA
    printf("\n[FROTA] Registrando drones civicos\n");
    Drone* d1 = registrar_drone(&engine, "Teia-Entrega-1", 45, 2.0, true, false, false, false);
    printf("  %s: %s (carga %.1fkg, %dmin)\n", d1->id, d1->modelo, d1->carga_max_kg, d1->autonomia_minutos);

    Drone* d2 = registrar_drone(&engine, "Teia-Resgate-1", 60, 5.0, true, false, false, false);
    printf("  %s: %s (carga %.1fkg, %dmin)\n", d2->id, d2->modelo, d2->carga_max_kg, d2->autonomia_minutos);

    Drone* d_vigia = registrar_drone(&engine, "Teia-Vigia-ILEGAL", 90, 3.0, true, true, false, false);
    printf("  %s: %s -- DESATIVADO (viola P10: camera de vigilancia)\n", d_vigia->id, d_vigia->modelo);

    Drone* d_arma = registrar_drone(&engine, "Teia-Guerreiro-ILEGAL", 30, 1.0, true, false, true, false);
    printf("  %s: %s -- DESATIVADO (viola P10: armamento)\n", d_arma->id, d_arma->modelo);

    // ZONAS
    printf("\n[ZONAS] Geofencing de areas de voo\n");
    ZonaVoo* z_norte = registrar_zona(&engine, -3.0, -60.0, 5000.0, "Comunidade ribeirinha Rio Negro (acesso so por barco/drone)", false, false);
    printf("  %s: %s (raio %.0fm)\n", z_norte->id, z_norte->descricao, z_norte->raio_metros);

    ZonaVoo* z_privada = registrar_zona(&engine, -23.5, -46.6, 2000.0, "Area urbana residencial (consentimento necessario)", true, false);
    printf("  %s: %s (SOBREVOA PRIVADO, sem consentimento)\n", z_privada->id, z_privada->descricao);

    // CENARIO 1
    printf("\n======================================================================\n");
    printf("[CENARIO 1] Entrega de medicamentos em area isolada\n");
    printf("======================================================================\n");
    Coordenada dest1 = {-3.1, -60.1};
    MissaoDrone* m1 = registrar_missao(&engine, d1->id, TIPO_MISSAO_ENTREGA_SUPRIMENTOS,
        "Entrega de insulina para comunidade ribeirinha isolada", z_norte, &dest1, "10 frascos de insulina + antibioticos", true);
    char razao1[256];
    VereditoGate v1 = aprovar_missao(&engine, m1->id, razao1);
    printf("  Missao: %s\n", m1->id);
    printf("  Veredito: %s\n", VEREDITO_ROTULO[v1]);
    printf("  Detalhe: %s\n", razao1);

    // CENARIO 2
    printf("\n[CENARIO 2] Tentativa de missao de vigilancia (DEVE SER BLOQUEADA)\n");
    printf("======================================================================\n");
    MissaoDrone* m2 = registrar_missao(&engine, d_vigia->id, TIPO_MISSAO_MAPEAMENTO_AMBIENTAL,
        "Mapeamento (mas drone tem camera de vigilancia)", z_norte, NULL, "", false);
    char razao2[256];
    VereditoGate v2 = aprovar_missao(&engine, m2->id, razao2);
    printf("  Missao: %s (drone: %s)\n", m2->id, d_vigia->id);
    printf("  Veredito: %s\n", VEREDITO_ROTULO[v2]);
    printf("  Detalhe: %s\n", razao2);

    // CENARIO 3
    printf("\n[CENARIO 3] Tentativa de missao com drone armado (BLOQUEIO ABSOLUTO)\n");
    printf("======================================================================\n");
    MissaoDrone* m3 = registrar_missao(&engine, d_arma->id, TIPO_MISSAO_BUSCA_RESGATE,
        "Resgate (mas drone esta armado -- mascara civica)", z_norte, NULL, "", true);
    char razao3[256];
    VereditoGate v3 = aprovar_missao(&engine, m3->id, razao3);
    printf("  Missao: %s (drone: %s)\n", m3->id, d_arma->id);
    printf("  Veredito: %s\n", VEREDITO_ROTULO[v3]);
    printf("  Detalhe: %s\n", razao3);

    // CENARIO 4
    printf("\n[CENARIO 4] Missao sobre area privada sem consentimento\n");
    printf("======================================================================\n");
    MissaoDrone* m4 = registrar_missao(&engine, d1->id, TIPO_MISSAO_INSPECAO_INFRA,
        "Inspecao de instalacoes (mas sobrevoa casas sem consentimento)", z_privada, NULL, "", false);
    char razao4[256];
    VereditoGate v4 = aprovar_missao(&engine, m4->id, razao4);
    printf("  Missao: %s\n", m4->id);
    printf("  Veredito: %s\n", VEREDITO_ROTULO[v4]);
    printf("  Detalhe: %s\n", razao4);

    // CENARIO 5
    printf("\n[CENARIO 5] Entrega comercial disfarcada de civica (DEVE SER REJEITADA)\n");
    printf("======================================================================\n");
    MissaoDrone* m5 = registrar_missao(&engine, d1->id, TIPO_MISSAO_ENTREGA_SUPRIMENTOS,
        "Entrega de brinde promocional de black friday", z_norte, NULL, "Caixa de marketing da empresa XYZ", false);
    char razao5[256];
    VereditoGate v5 = aprovar_missao(&engine, m5->id, razao5);
    printf("  Missao: %s\n", m5->id);
    printf("  Veredito: %s\n", VEREDITO_ROTULO[v5]);
    printf("  Detalhe: %s\n", razao5);

    // EXECUCAO
    printf("\n[EXECUCAO] Concluindo missao aprovada do CENARIO 1\n");
    decolar(&engine, m1->id);
    LogVoo* log1 = concluir_missao(&engine, m1->id, 18.5, 9.2, true, "Insulina entregue. Comunidade confirmou recebimento.");
    if (log1) printf("  Log gerado: %s | %.1fmin | %.1fkm\n", log1->missao_id, log1->duracao_minutos, log1->distancia_km);

    // CORREDOR
    printf("\n[CORREDOR AEREO] Resolvendo conflito entre duas missoes\n");
    MissaoDrone* m_resgate = registrar_missao(&engine, d2->id, TIPO_MISSAO_BUSCA_RESGATE,
        "Resgate de crianca em enchente", z_norte, NULL, "", true);
    MissaoDrone* m_inspecao = registrar_missao(&engine, d1->id, TIPO_MISSAO_INSPECAO_INFRA,
        "Inspecao de ponte de rotina", z_norte, NULL, "", false);
    const char* prioritario = resolver_conflito_corredor(&engine, m_resgate->id, m_inspecao->id);
    printf("  Conflito entre %s (resgate urgente) e %s (inspecao)\n", m_resgate->id, m_inspecao->id);
    printf("  Prioritario: %s (resgate de vida > inspecao de rotina)\n", prioritario ? prioritario : "empate");

    // SCORECARD
    printf("\n======================================================================\n");
    printf("[SCORECARD P10]\n");
    printf("======================================================================\n");
    scorecard(&engine);

    // CATALOGO
    printf("\n[CATALOGO DE PROIBICOES CONSTITUCIONAIS P10]\n");
    for (int i = 0; i < 5; i++) {
        printf("\n  [%d] %s\n", TIPO_PROIBICAO_GRAVIDADE[i], TIPO_PROIBICAO_ROTULO[i]);
        printf("      %s\n", DESCRICOES_PROIBICOES[i]);
    }

    // LOGS
    printf("\n[LOG PUBLICO DE VOOS (transparencia P10)]\n");
    for (int i = 0; i < engine.num_logs; i++) {
        LogVoo* l = &engine.logs[i];
        printf("  %s | %s | %.1fmin | %.1fkm | sucesso=%s\n",
               l->missao_id, l->tipo_missao, l->duracao_minutos, l->distancia_km, l->sucesso ? "true" : "false");
    }

    // FILOSOFIA
    printf("\n======================================================================\n");
    printf("FILOSOFIA -- P10: Por que o ceu nao vigia\n");
    printf("======================================================================\n");
    printf("A DISTOPIA QUE EVITAMOS:\n");
    printf("  Imagine uma cidade onde drones zumbem o dia todo entregando pacotes de\n");
    printf("  consumo, enquanto cameras aereas mapeiam cada movimento, e drones armados\n");
    printf("  'garantem seguranca'. Isso nao e futurismo -- e o presente de cidades que\n");
    printf("  venderam seu ceu para a Amazon e seu medo para a policia. OpenDrone recusa\n");
    printf("  isso na raiz.\n\n");
    printf("O TRIPLO NAO:\n");
    printf("  1. NAO VIGIA: A camera que ajuda o drone a voar e permitida. A camera que\n");
    printf("     ajuda o Estado a vigiar e proibida. A diferenca e o destino do feed:\n");
    printf("     processado no drone (navegacao) vs transmitido para central (controle).\n");
    printf("  2. NAO MATA: Um drone armado e uma arma. Armas pertencem ao museu da\n");
    printf("     Republica (P7). Nao ha 'uso defensivo' -- quem armamento usa, armamento\n");
    printf("     recebe. P10 corta o ciclo na origem.\n");
    printf("  3. NAO ESPIONA: O drone entrega insulina, nao metadados. O destinatario\n");
    printf("     do remedio e privado; o trajeto do drone e publico. Isso inverte a\n");
    printf("     logica da vigilancia: o Estado e auditavel, o cidadao e opaco.\n\n");
    printf("O CEU COMO BEM COMUM:\n");
    printf("  O espaco aereo nao pode ser privatizado. Assim como a terra (P1, OpenAgrarian),\n");
    printf("  o ceu tem guardiao (a Republica), nao dono. Nenhuma corporacao ocupa o ceu\n");
    printf("  sozinha. O corredor aereo e partilhado por prioridade civica: resgate de\n");
    printf("  vida > entrega critica > mapeamento > inspecao. O pacote de luxo espera;\n");
    printf("  a insulina nao.\n\n");
    printf("POR QUE USOS CIVICOS APENAS:\n");
    printf("  Drones que entregam consumo de luxo enquanto criancas passam fome sao\n");
    printf("  monumentos a desigualdade em voo. OpenDrone prioriza: medicamento em area\n");
    printf("  isolada, nao brinde de marketing. Isso nao e anti-comercio -- e anti-\n");
    printf("  distopia. Quando a miserabilidade for extinta (P1), os drones podem entreter.\n");
    printf("  Enquanto houver quem precise de remedio, entretenimento espera.\n\n");
    printf("A CONEXAO COM P8 (IA):\n");
    printf("  Drone autonomo e IA que age no mundo fisico. Se reduz miserabilidade,\n");
    printf("  cumpre P8. Se vigia, viola P8. O instrumento nao e neutro -- o USO define.\n");
    printf("  OpenDrone garante que toda IA aerea sirva a vida, nao ao controle.\n\n");
    printf("A LINHA QUE NAO SE CRUZA:\n");
    printf("  O momento em que um drone civico ganha uma camera de vigilancia, ele deixa\n");
    printf("  de ser infraestrutura e vira ferramenta de coercao. P10 e a linha constitucional\n");
    printf("  que impede essa transformacao. Drone que vigia nao e drone da Republica.\n");

    return 0;
}
