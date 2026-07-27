// Full JS (ES6) translation of open_drone.py (P10 Soberania Aerea Civica)
// All enums (frozen objects), classes, tables, DroneCivicoEngine methods, and _demo() faithfully reproduced.
// Comments and strings kept in Portuguese. Runnable with node.

const TipoMissao = Object.freeze({
    ENTREGA_SUPRIMENTOS: { id: "entrega_suprimentos", rotulo: "Entrega de suprimentos (remedio, comida, agua)", prioridade: 1 },
    MAPEAMENTO_AMBIENTAL: { id: "mapeamento_ambiental", rotulo: "Mapeamento ambiental (desmatamento, queimadas)", prioridade: 1 },
    BUSCA_RESGATE: { id: "busca_resgate", rotulo: "Busca e resgate em desastre natural", prioridade: 0 },
    CONECTIVIDADE: { id: "conectividade", rotulo: "Rede mesh aerea (area sem cobertura)", prioridade: 1 },
    INSPECAO_INFRA: { id: "inspecao_infra", rotulo: "Inspecao de infraestrutura critica", prioridade: 1 },
    AGRICULTURA_CIVICA: { id: "agricultura_civica", rotulo: "Agricultura de precisao comunitaria", prioridade: 2 }
});

const StatusMissao = Object.freeze({
    PLANEJADA: { id: "planejada", rotulo: "Planejada (aguardando aprovacao do gate)" },
    APROVADA: { id: "aprovada", rotulo: "Aprovada pelo gate P10" },
    EM_VOO: { id: "em_voo", rotulo: "Em voo (executando)" },
    CONCLUIDA: { id: "concluida", rotulo: "Concluida com sucesso" },
    REJEITADA: { id: "rejeitada", rotulo: "Rejeitada pelo gate P10" },
    CANCELADA: { id: "cancelada", rotulo: "Cancelada (emergencia ou erro)" },
    FALHOU: { id: "falhou", rotulo: "Falhou (perda de sinal, aterrissagem forcada)" }
});

const TipoProibicao = Object.freeze({
    VIGILANCIA: { id: "vigilancia", rotulo: "Camera de vigilancia (feed gravado/transmitido)", gravidade: 5 },
    ARMAMENTO: { id: "armamento", rotulo: "Carrega arma ou explosivo", gravidade: 5 },
    ESPIONAGEM: { id: "espionagem", rotulo: "Coleta dados pessoais (facial, placa, biometria)", gravidade: 5 },
    PRIVADO_SEM_CONSENTIMENTO: { id: "privado_sem_consentimento", rotulo: "Sobrevoa area privada sem consentimento", gravidade: 4 },
    COMERCIAL_NAO_CIVICO: { id: "comercial_nao_civico", rotulo: "Uso comercial sem proposito civico (propaganda)", gravidade: 3 }
});

const VereditoGate = Object.freeze({
    APROVADA: { id: "aprovada", rotulo: "Missao aprovada: proposito civico confirmado" },
    APROVADA_COM_RESTRICOES: { id: "aprovada_restricoes", rotulo: "Aprovada com restricoes (geofence ampliado)" },
    REJEITADA: { id: "rejeitada", rotulo: "Missao rejeitada: viola uma proibicao P10" },
    BLOQUEADA: { id: "bloqueada", rotulo: "Missao bloqueada: e vetor de vigilancia/arma" }
});

const PrioridadeCorredor = Object.freeze({
    RESGATE_VIDA: { id: "resgate_vida", rotulo: "Resgate de vida (emergencia medica)", prioridade: 0 },
    ENTREGA_CRITICA: { id: "entrega_critica", rotulo: "Entrega critica (remedio urgente)", prioridade: 1 },
    MAPEAMENTO_AMBIENTAL: { id: "mapeamento", rotulo: "Mapeamento ambiental de rotina", prioridade: 2 },
    CONECTIVIDADE: { id: "conectividade", rotulo: "Conectividade mesh", prioridade: 2 },
    INSPECAO: { id: "inspecao", rotulo: "Inspecao de infraestrutura", prioridade: 3 },
    OUTROS: { id: "outros", rotulo: "Outros usos civicos", prioridade: 4 }
});

class Coordenada {
    constructor(lat, lon) {
        this.lat = lat;
        this.lon = lon;
    }
}

class ZonaVoo {
    constructor(id, centro, raio_metros, descricao = "", sobrevoa_privado = false, consentimento_privado = false) {
        this.id = id;
        this.centro = centro;
        this.raio_metros = raio_metros;
        this.descricao = descricao;
        this.sobrevoa_privado = sobrevoa_privado;
        this.consentimento_privado = consentimento_privado;
    }
}

class Drone {
    constructor(id, modelo, autonomia_minutos, carga_max_kg, tem_camera_navegacao = true, tem_camera_vigilancia = false, tem_armamento = false, coleta_dados_pessoais = false) {
        this.id = id;
        this.modelo = modelo;
        this.autonomia_minutos = autonomia_minutos;
        this.carga_max_kg = carga_max_kg;
        this.tem_camera_navegacao = tem_camera_navegacao;
        this.tem_camera_vigilancia = tem_camera_vigilancia;
        this.tem_armamento = tem_armamento;
        this.coleta_dados_pessoais = coleta_dados_pessoais;
        this.ativo = true;
        this.missoes_concluidas = 0;
    }
}

class MissaoDrone {
    constructor(id, drone_id, tipo, descricao, zona, destino = null, carga_descricao = "", urgencia = false) {
        this.id = id;
        this.drone_id = drone_id;
        this.tipo = tipo;
        this.descricao = descricao;
        this.zona = zona;
        this.destino = destino;
        this.carga_descricao = carga_descricao;
        this.urgencia = urgencia;
        this.status = StatusMissao.PLANEJADA;
        this.veredito_gate = null;
        this.razao_rejeicao = "";
        this.proibicoes_violadas = [];
        this.criada_em = "";
        this.concluida_em = "";
        this.log_trajeto = [];
    }
}

class LogVoo {
    constructor(missao_id, drone_id, tipo_missao, duracao_minutos, distancia_km, decolagem, pouso, destino_lat = null, destino_lon = null, sucesso = true, observacoes = "") {
        this.missao_id = missao_id;
        this.drone_id = drone_id;
        this.tipo_missao = tipo_missao;
        this.duracao_minutos = duracao_minutos;
        this.distancia_km = distancia_km;
        this.decolagem = decolagem;
        this.pouso = pouso;
        this.destino_lat = destino_lat;
        this.destino_lon = destino_lon;
        this.sucesso = sucesso;
        this.observacoes = observacoes;
    }
}

class MetricaFrota {
    constructor(regiao_id, total_drones, drones_ativos, missoes_concluidas, missoes_rejeitadas, entregas_criticas, resgates, horas_voo, violacoes_detectadas, cobertura_km2) {
        this.regiao_id = regiao_id;
        this.total_drones = total_drones;
        this.drones_ativos = drones_ativos;
        this.missoes_concluidas = missoes_concluidas;
        this.missoes_rejeitadas = missoes_rejeitadas;
        this.entregas_criticas = entregas_criticas;
        this.resgates = resgates;
        this.horas_voo = horas_voo;
        this.violacoes_detectadas = violacoes_detectadas;
        this.cobertura_km2 = cobertura_km2;
    }
}

const DESCRICOES_PROIBICOES = {
    "vigilancia": "Camera de vigilancia = feed gravado ou transmitido para central de monitoramento. PERMITIDO: camera de navegacao (feed local em tempo real, nao gravado, processado no proprio drone). A linha e: a camera ajuda o drone a voar, nao ajuda o Estado a vigiar.",
    "armamento": "Qualquer arma, explosivo, ou dispositivo projetado para causar dano fisico. Um drone armado nao e drone -- e arma. Armas pertencem ao museu da Republica (P7). Sem excecoes, mesmo para 'defesa'.",
    "espionagem": "Reconhecimento facial, leitura de placas, coleta de biometria, captura de dados de rede (wifi bluetooth scanning). O drone entrega suprimentos; NAO entrega metadados sobre o destinatario.",
    "privado_sem_consentimento": "Sobrevoar residencia, patio, ou propriedade privada sem consentimento explicito do morador. Excecao: resgate de vida (P1 > privacidade), mas o log fica publico e auditavel.",
    "comercial_nao_civico": "Uso para entrega de consumo de luxo, propaganda, marketing, ou qualquer fim que nao reduza miserabilidade ou amplie acesso. Drones nao sao brinquedo de consumo -- sao infraestrutura de sobrevivencia."
};

const PRIORIDADE_POR_TIPO = {
    [TipoMissao.BUSCA_RESGATE.id]: 0,
    [TipoMissao.ENTREGA_SUPRIMENTOS.id]: 1,
    [TipoMissao.MAPEAMENTO_AMBIENTAL.id]: 2,
    [TipoMissao.CONECTIVIDADE.id]: 2,
    [TipoMissao.INSPECAO_INFRA.id]: 3,
    [TipoMissao.AGRICULTURA_CIVICA.id]: 3
};

class DroneCivicoEngine {
    constructor() {
        this.drones = {};
        this.missoes = {};
        this.zonas = {};
        this.logs = [];
        this._drone_id = 0;
        this._missao_id = 0;
        this._zona_id = 0;
    }

    _drone_id_novo() {
        this._drone_id++;
        return `DRONE-${String(this._drone_id).padStart(4, '0')}`;
    }

    _missao_id_novo() {
        this._missao_id++;
        return `MISSAO-${String(this._missao_id).padStart(4, '0')}`;
    }

    _zona_id_novo() {
        this._zona_id++;
        return `ZONA-${String(this._zona_id).padStart(4, '0')}`;
    }

    registrar_zona(centro, raio_metros, descricao = "", sobrevoa_privado = false, consentimento_privado = false) {
        const z = new ZonaVoo(this._zona_id_novo(), centro, raio_metros, descricao, sobrevoa_privado, consentimento_privado);
        this.zonas[z.id] = z;
        return z;
    }

    registrar_drone(modelo, autonomia_minutos, carga_max_kg, tem_camera_navegacao = true, tem_camera_vigilancia = false, tem_armamento = false, coleta_dados_pessoais = false) {
        const d = new Drone(this._drone_id_novo(), modelo, autonomia_minutos, carga_max_kg, tem_camera_navegacao, tem_camera_vigilancia, tem_armamento, coleta_dados_pessoais);
        if (tem_camera_vigilancia || tem_armamento || coleta_dados_pessoais) {
            d.ativo = false;
        }
        this.drones[d.id] = d;
        return d;
    }

    registrar_missao(drone_id, tipo, descricao, zona, destino = null, carga_descricao = "", urgencia = false) {
        const m = new MissaoDrone(this._missao_id_novo(), drone_id, tipo, descricao, zona, destino, carga_descricao, urgencia);
        m.criada_em = new Date().toISOString();
        this.missoes[m.id] = m;
        return m;
    }

    auditar_proibicoes(missao) {
        const violacoes = [];
        const drone = this.drones[missao.drone_id];
        if (!drone) {
            return [TipoProibicao.COMERCIAL_NAO_CIVICO];
        }
        if (drone.tem_armamento) violacoes.push(TipoProibicao.ARMAMENTO);
        if (drone.tem_camera_vigilancia) violacoes.push(TipoProibicao.VIGILANCIA);
        if (drone.coleta_dados_pessoais) violacoes.push(TipoProibicao.ESPIONAGEM);
        if (missao.zona.sobrevoa_privado && !missao.zona.consentimento_privado) {
            if (missao.tipo !== TipoMissao.BUSCA_RESGATE) {
                violacoes.push(TipoProibicao.PRIVADO_SEM_CONSENTIMENTO);
            }
        }
        if (this._verificar_uso_comercial(missao)) {
            violacoes.push(TipoProibicao.COMERCIAL_NAO_CIVICO);
        }
        missao.proibicoes_violadas = violacoes;
        return violacoes;
    }

    _verificar_uso_comercial(missao) {
        const palavras_nao_civicas = new Set(["propaganda", "marketing", "publicidade", "luxo", "brinde", "promocional", "black friday", "desconto", "vitrine"]);
        const texto = (missao.descricao + " " + missao.carga_descricao).toLowerCase();
        for (const p of palavras_nao_civicas) {
            if (texto.includes(p)) return true;
        }
        return false;
    }

    aprovar_missao(missao_id) {
        const missao = this.missoes[missao_id];
        if (!missao) return [VereditoGate.REJEITADA, "Missao nao encontrada"];
        const violacoes = this.auditar_proibicoes(missao);
        const drone = this.drones[missao.drone_id];
        const gravidade_max = violacoes.length > 0 ? Math.max(...violacoes.map(v => v.gravidade)) : 0;
        if (gravidade_max >= 5) {
            missao.veredito_gate = VereditoGate.BLOQUEADA;
            missao.status = StatusMissao.REJEITADA;
            missao.razao_rejeicao = `MISSAO BLOQUEADA: viola proibicao constitucional P10 -- ${violacoes.map(v => v.rotulo).join(", ")}`;
            return [missao.veredito_gate, missao.razao_rejeicao];
        }
        if (violacoes.length > 0) {
            missao.veredito_gate = VereditoGate.REJEITADA;
            missao.status = StatusMissao.REJEITADA;
            missao.razao_rejeicao = `Missao rejeitada: ${violacoes.map(v => v.rotulo).join(", ")}`;
            return [missao.veredito_gate, missao.razao_rejeicao];
        }
        if (drone) {
            const dist_estimada = this._estimar_distancia(missao);
            const autonomia_necessaria = (dist_estimada / 30.0) * 60;
            if (autonomia_necessaria > drone.autonomia_minutos) {
                missao.veredito_gate = VereditoGate.APROVADA_COM_RESTRICOES;
                missao.status = StatusMissao.APROVADA;
                missao.razao_rejeicao = `Aprovada com restricoes: autonomia marginal (${autonomia_necessaria.toFixed(0)}min necessaria vs ${drone.autonomia_minutos}min disponivel)`;
                return [missao.veredito_gate, missao.razao_rejeicao];
            }
        }
        missao.veredito_gate = VereditoGate.APROVADA;
        missao.status = StatusMissao.APROVADA;
        return [missao.veredito_gate, "Missao aprovada pelo gate P10"];
    }

    _estimar_distancia(missao) {
        return (missao.zona.raio_metros / 1000.0) * 2.0;
    }

    decolar(missao_id) {
        const missao = this.missoes[missao_id];
        if (!missao || missao.status !== StatusMissao.APROVADA) return false;
        missao.status = StatusMissao.EM_VOO;
        return true;
    }

    concluir_missao(missao_id, duracao_minutos, distancia_km, sucesso = true, observacoes = "") {
        const missao = this.missoes[missao_id];
        if (!missao || missao.status !== StatusMissao.EM_VOO) return null;
        missao.status = sucesso ? StatusMissao.CONCLUIDA : StatusMissao.FALHOU;
        missao.concluida_em = new Date().toISOString();
        const drone = this.drones[missao.drone_id];
        if (drone && sucesso) drone.missoes_concluidas++;
        const log = new LogVoo(
            missao.id, missao.drone_id, missao.tipo.id, duracao_minutos, distancia_km,
            missao.criada_em, missao.concluida_em,
            missao.destino ? missao.destino.lat : null,
            missao.destino ? missao.destino.lon : null,
            sucesso, observacoes
        );
        this.logs.push(log);
        return log;
    }

    resolver_conflito_corredor(missao_a_id, missao_b_id) {
        const ma = this.missoes[missao_a_id];
        const mb = this.missoes[missao_b_id];
        if (!ma || !mb) return null;
        const pri_a = PRIORIDADE_POR_TIPO[ma.tipo.id] ?? 4;
        const pri_b = PRIORIDADE_POR_TIPO[mb.tipo.id] ?? 4;
        if (ma.urgencia && !mb.urgencia) return ma.id;
        if (mb.urgencia && !ma.urgencia) return mb.id;
        if (pri_a < pri_b) return ma.id;
        if (pri_b < pri_a) return mb.id;
        return null;
    }

    medir_frota(regiao_id = "default") {
        const total = Object.keys(this.drones).length;
        const ativos = Object.values(this.drones).filter(d => d.ativo).length;
        const concluidas = Object.values(this.missoes).filter(m => m.status === StatusMissao.CONCLUIDA).length;
        const rejeitadas = Object.values(this.missoes).filter(m => m.status === StatusMissao.REJEITADA).length;
        const entregas = Object.values(this.missoes).filter(m => m.status === StatusMissao.CONCLUIDA && m.tipo === TipoMissao.ENTREGA_SUPRIMENTOS).length;
        const resgates = Object.values(this.missoes).filter(m => m.status === StatusMissao.CONCLUIDA && m.tipo === TipoMissao.BUSCA_RESGATE).length;
        const horas = this.logs.reduce((s, l) => s + l.duracao_minutos, 0) / 60.0;
        const violacoes = Object.values(this.missoes).reduce((s, m) => s + m.proibicoes_violadas.length, 0);
        const cobertura = Object.values(this.zonas).reduce((s, z) => s + (z.raio_metros ** 2 * 3.14159), 0) / 1_000_000;
        return new MetricaFrota(
            regiao_id, total, ativos, concluidas, rejeitadas, entregas, resgates,
            Math.round(horas * 10) / 10, violacoes, Math.round(cobertura * 100) / 100
        );
    }

    scorecard() {
        const f = this.medir_frota();
        const taxa = Math.round((f.missoes_concluidas / Math.max(f.missoes_concluidas + f.missoes_rejeitadas, 1)) * 1000) / 10;
        return {
            "drones_registrados": f.total_drones,
            "drones_ativos": f.drones_ativos,
            "drones_bloqueados": f.total_drones - f.drones_ativos,
            "missoes_concluidas": f.missoes_concluidas,
            "missoes_rejeitadas": f.missoes_rejeitadas,
            "entregas_criticas": f.entregas_criticas,
            "resgates_realizados": f.resgates,
            "horas_voo_total": f.horas_voo,
            "violacoes_detectadas": f.violacoes_detectadas,
            "cobertura_km2": f.cobertura_km2,
            "taxa_aprovacao": `${taxa}%`
        };
    }
}

function _demo() {
    console.log("=".repeat(70));
    console.log("OpenDrone -- P10: Soberania Aerea Civica");
    console.log("=".repeat(70));

    const e = new DroneCivicoEngine();

    console.log("\n[FROTA] Registrando drones civicos");
    const d1 = e.registrar_drone("Teia-Entrega-1", 45, 2.0);
    console.log(`  ${d1.id}: ${d1.modelo} (carga ${d1.carga_max_kg}kg, ${d1.autonomia_minutos}min)`);

    const d2 = e.registrar_drone("Teia-Resgate-1", 60, 5.0);
    console.log(`  ${d2.id}: ${d2.modelo} (carga ${d2.carga_max_kg}kg, ${d2.autonomia_minutos}min)`);

    const d_vigia = e.registrar_drone("Teia-Vigia-ILEGAL", 90, 3.0, true, true);
    console.log(`  ${d_vigia.id}: ${d_vigia.modelo} -- DESATIVADO (viola P10: camera de vigilancia)`);

    const d_arma = e.registrar_drone("Teia-Guerreiro-ILEGAL", 30, 1.0, true, false, true);
    console.log(`  ${d_arma.id}: ${d_arma.modelo} -- DESATIVADO (viola P10: armamento)`);

    console.log("\n[ZONAS] Geofencing de areas de voo");
    const z_norte = e.registrar_zona(new Coordenada(-3.0, -60.0), 5000, "Comunidade ribeirinha Rio Negro (acesso so por barco/drone)");
    console.log(`  ${z_norte.id}: ${z_norte.descricao} (raio ${z_norte.raio_metros}m)`);

    const z_privada = e.registrar_zona(new Coordenada(-23.5, -46.6), 2000, "Area urbana residencial (consentimento necessario)", true, false);
    console.log(`  ${z_privada.id}: ${z_privada.descricao} (SOBREVOA PRIVADO, sem consentimento)`);

    // CENARIO 1
    console.log("\n" + "=".repeat(70));
    console.log("[CENARIO 1] Entrega de medicamentos em area isolada");
    console.log("=".repeat(70));
    const m1 = e.registrar_missao(d1.id, TipoMissao.ENTREGA_SUPRIMENTOS, "Entrega de insulina para comunidade ribeirinha isolada", z_norte, new Coordenada(-3.1, -60.1), "10 frascos de insulina + antibioticos", true);
    const [v1, r1] = e.aprovar_missao(m1.id);
    console.log(`  Missao: ${m1.id}`);
    console.log(`  Veredito: ${v1.rotulo}`);
    console.log(`  Detalhe: ${r1}`);

    // CENARIO 2
    console.log("\n[CENARIO 2] Tentativa de missao de vigilancia (DEVE SER BLOQUEADA)");
    console.log("=".repeat(70));
    const m2 = e.registrar_missao(d_vigia.id, TipoMissao.MAPEAMENTO_AMBIENTAL, "Mapeamento (mas drone tem camera de vigilancia)", z_norte);
    const [v2, r2] = e.aprovar_missao(m2.id);
    console.log(`  Missao: ${m2.id} (drone: ${d_vigia.id})`);
    console.log(`  Veredito: ${v2.rotulo}`);
    console.log(`  Detalhe: ${r2}`);
    console.log(`  Proibicoes violadas: ${m2.proibicoes_violadas.map(p => p.rotulo).join(", ")}`);

    // CENARIO 3
    console.log("\n[CENARIO 3] Tentativa de missao com drone armado (BLOQUEIO ABSOLUTO)");
    console.log("=".repeat(70));
    const m3 = e.registrar_missao(d_arma.id, TipoMissao.BUSCA_RESGATE, "Resgate (mas drone esta armado -- mascara civica)", z_norte, null, "", true);
    const [v3, r3] = e.aprovar_missao(m3.id);
    console.log(`  Missao: ${m3.id} (drone: ${d_arma.id})`);
    console.log(`  Veredito: ${v3.rotulo}`);
    console.log(`  Detalhe: ${r3}`);
    console.log(`  Proibicoes violadas: ${m3.proibicoes_violadas.map(p => p.rotulo).join(", ")}`);

    // CENARIO 4
    console.log("\n[CENARIO 4] Missao sobre area privada sem consentimento");
    console.log("=".repeat(70));
    const m4 = e.registrar_missao(d1.id, TipoMissao.INSPECAO_INFRA, "Inspecao de instalacoes (mas sobrevoa casas sem consentimento)", z_privada);
    const [v4, r4] = e.aprovar_missao(m4.id);
    console.log(`  Missao: ${m4.id}`);
    console.log(`  Veredito: ${v4.rotulo}`);
    console.log(`  Detalhe: ${r4}`);

    // CENARIO 5
    console.log("\n[CENARIO 5] Entrega comercial disfarcada de civica (DEVE SER REJEITADA)");
    console.log("=".repeat(70));
    const m5 = e.registrar_missao(d1.id, TipoMissao.ENTREGA_SUPRIMENTOS, "Entrega de brinde promocional de black friday", z_norte, null, "Caixa de marketing da empresa XYZ");
    const [v5, r5] = e.aprovar_missao(m5.id);
    console.log(`  Missao: ${m5.id}`);
    console.log(`  Veredito: ${v5.rotulo}`);
    console.log(`  Detalhe: ${r5}`);

    // EXECUCAO
    console.log("\n[EXECUCAO] Concluindo missao aprovada do CENARIO 1");
    e.decolar(m1.id);
    const log1 = e.concluir_missao(m1.id, 18.5, 9.2, true, "Insulina entregue. Comunidade confirmou recebimento.");
    if (log1) {
        console.log(`  Log gerado: ${log1.missao_id} | ${log1.duracao_minutos}min | ${log1.distancia_km}km`);
    }

    // CORREDOR
    console.log("\n[CORREDOR AEREO] Resolvendo conflito entre duas missoes");
    const m_resgate = e.registrar_missao(d2.id, TipoMissao.BUSCA_RESGATE, "Resgate de crianca em enchente", z_norte, null, "", true);
    const m_inspecao = e.registrar_missao(d1.id, TipoMissao.INSPECAO_INFRA, "Inspecao de ponte de rotina", z_norte);
    const prioritario = e.resolver_conflito_corredor(m_resgate.id, m_inspecao.id);
    console.log(`  Conflito entre ${m_resgate.id} (resgate urgente) e ${m_inspecao.id} (inspecao)`);
    console.log(`  Prioritario: ${prioritario} (resgate de vida > inspecao de rotina)`);

    // SCORECARD
    console.log("\n" + "=".repeat(70));
    console.log("[SCORECARD P10]");
    console.log("=".repeat(70));
    const sc = e.scorecard();
    for (const [k, val] of Object.entries(sc)) {
        console.log(`  ${k.padEnd(28, ".")} ${val}`);
    }

    // CATALOGO
    console.log("\n[CATALOGO DE PROIBICOES CONSTITUCIONAIS P10]");
    for (const p of Object.values(TipoProibicao)) {
        const desc = DESCRICOES_PROIBICOES[p.id] || "";
        console.log(`\n  [${p.gravidade}] ${p.rotulo}`);
        console.log(`      ${desc}`);
    }

    // LOGS
    console.log("\n[LOG PUBLICO DE VOOS (transparencia P10)]");
    for (const log of e.logs) {
        console.log(`  ${log.missao_id} | ${log.tipo_missao} | ${log.duracao_minutos}min | ${log.distancia_km}km | sucesso=${log.sucesso}`);
    }

    // FILOSOFIA
    console.log("\n" + "=".repeat(70));
    console.log("FILOSOFIA -- P10: Por que o ceu nao vigia");
    console.log("=".repeat(70));
    console.log(`
A DISTOPIA QUE EVITAMOS:
  Imagine uma cidade onde drones zumbem o dia todo entregando pacotes de
  consumo, enquanto cameras aereas mapeiam cada movimento, e drones armados
  'garantem seguranca'. Isso nao e futurismo -- e o presente de cidades que
  venderam seu ceu para a Amazon e seu medo para a policia. OpenDrone recusa
  isso na raiz.

O TRIPLO NAO:
  1. NAO VIGIA: A camera que ajuda o drone a voar e permitida. A camera que
     ajuda o Estado a vigiar e proibida. A diferenca e o destino do feed:
     processado no drone (navegacao) vs transmitido para central (controle).
  2. NAO MATA: Um drone armado e uma arma. Armas pertencem ao museu da
     Republica (P7). Nao ha 'uso defensivo' -- quem armamento usa, armamento
     recebe. P10 corta o ciclo na origem.
  3. NAO ESPIONA: O drone entrega insulina, nao metadados. O destinatario
     do remedio e privado; o trajeto do drone e publico. Isso inverte a
     logica da vigilancia: o Estado e auditavel, o cidadao e opaco.

O CEU COMO BEM COMUM:
  O espaco aereo nao pode ser privatizado. Assim como a terra (P1, OpenAgrarian),
  o ceu tem guardiao (a Republica), nao dono. Nenhuma corporacao ocupa o ceu
  sozinha. O corredor aereo e partilhado por prioridade civica: resgate de
  vida > entrega critica > mapeamento > inspecao. O pacote de luxo espera;
  a insulina nao.

POR QUE USOS CIVICOS APENAS:
  Drones que entregam consumo de luxo enquanto criancas passam fome sao
  monumentos a desigualdade em voo. OpenDrone prioriza: medicamento em area
  isolada, nao brinde de marketing. Isso nao e anti-comercio -- e anti-
  distopia. Quando a miserabilidade for extinta (P1), os drones podem entreter.
  Enquanto houver quem precise de remedio, entretenimento espera.

A CONEXAO COM P8 (IA):
  Drone autonomo e IA que age no mundo fisico. Se reduz miserabilidade,
  cumpre P8. Se vigia, viola P8. O instrumento nao e neutro -- o USO define.
  OpenDrone garante que toda IA aerea sirva a vida, nao ao controle.

A LINHA QUE NAO SE CRUZA:
  O momento em que um drone civico ganha uma camera de vigilancia, ele deixa
  de ser infraestrutura e vira ferramenta de coercao. P10 e a linha constitucional
  que impede essa transformacao. Drone que vigia nao e drone da Republica.
`);
}

if (require.main === module) {
    _demo();
}
