// JS (ES6) translation of open_energy.py
// OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso
// Full faithful translation - all enums, classes, methods, demo

const FonteEnergia = {
    SOLAR: { id: "solar", rotulo: "Solar fotovoltaica", renovavel: true },
    EOLICA: { id: "eolica", rotulo: "Eolica (vento)", renovavel: true },
    HIDRO: { id: "hidro", rotulo: "Hidroeletrica", renovavel: true },
    GEOTERMICA: { id: "geotermica", rotulo: "Geotermica", renovavel: true },
    BIOMASSA: { id: "biomassa", rotulo: "Biomassa", renovavel: true },
    MARES: { id: "mares", rotulo: "Das mars e correntes", renovavel: true },
    NUCLEAR: { id: "nuclear", rotulo: "Nuclear (fissao)", renovavel: false },
    FUSAO: { id: "fusao", rotulo: "Fusao nuclear (futura)", renovavel: true }
};

const TipoConsumo = {
    ESSENCIAL_VIDA: { id: "essencial_vida", rotulo: "Essencial a vida (cozinhar, aquecer, iluminar, agua)", prioridade: 1 },
    SAUDE: { id: "saude", rotulo: "Saude (hospitais, clinicas, equipamentos medicos)", prioridade: 1 },
    COMUNICACAO: { id: "comunicacao", rotulo: "Comunicacao (internet, telefone, radio)", prioridade: 1 },
    EDUCACAO: { id: "educacao", rotulo: "Educacao (escolas, bibliotecas, laboratorios)", prioridade: 2 },
    MOBILIDADE: { id: "mobilidade", rotulo: "Mobilidade (transporte publico, veiculos)", prioridade: 2 },
    PRODUCAO_ALIMENTOS: { id: "producao_alimentos", rotulo: "Producao de alimentos (irrigacao, processamento)", prioridade: 2 },
    INFRAESTRUTURA_COMUM: { id: "infraestrutura", rotulo: "Infraestrutura comum (agua, esgoto, iluminacao publica)", prioridade: 2 },
    PRODUCAO_BENS: { id: "producao_bens", rotulo: "Producao de bens (fabril, artesanal)", prioridade: 3 },
    CULTURA_LAZER: { id: "cultura_lazer", rotulo: "Cultura e lazer (teatro, musica, esporte)", prioridade: 3 },
    PESQUISA_INOVACAO: { id: "pesquisa", rotulo: "Pesquisa e inovacao (laboratorios, computacao)", prioridade: 3 },
    RESIDENCIAL_EXCEDENTE: { id: "residencial_excedente", rotulo: "Residencial excedente (alem do essencial)", prioridade: 4 }
};

const TipoArmazenamento = {
    BATERIA_LITIO: { id: "bateria_litio", rotulo: "Bateria de litio-ion" },
    BATERIA_SODIO: { id: "bateria_sodio", rotulo: "Bateria de sodio (mais barato, menos denso)" },
    BATERIA_FLUXO: { id: "bateria_fluxo", rotulo: "Bateria de fluxo redox (escala grid)" },
    HIDRO_BOMBEADA: { id: "hidro_bombeada", rotulo: "Hidroeletrica reversivel (bombeada)" },
    GRAVIDADE: { id: "gravidade", rotulo: "Armazenamento por gravidade (pesos)" },
    HIDROGENIO: { id: "hidrogenio", rotulo: "Hidrogenio verde (eletrolise)" },
    AR_COMPRIMIDO: { id: "ar_comprimido", rotulo: "Ar comprimido (CAES)" },
    TERMICO: { id: "termico", rotulo: "Armazenamento termico (sal fundido, agua quente)" }
};

const StatusCenario = {
    ABUNDANCIA: { id: "abundancia", rotulo: "Abundancia: geracao supera demanda" },
    EQUILIBRIO: { id: "equilibrio", rotulo: "Equilibrio: geracao = demanda" },
    ATENCAO: { id: "atencao", rotulo: "Atencao: margem baixa (<10%)" },
    ESCASSEZ: { id: "escassez", rotulo: "Escassez: demanda supera geracao" },
    EMERGENCIA: { id: "emergencia", rotulo: "Emergencia: deficit critico, assembleia decide" }
};

const StatusInterconexao = {
    ILHADO: { id: "ilhado", rotulo: "Ilhado: microgrid autonomo (sem conexao externa)" },
    CONECTADO: { id: "conectado", rotulo: "Conectado a rede regional" },
    EXPORTANDO: { id: "exportando", rotulo: "Exportando excedente (doacao)" },
    IMPORTANDO: { id: "importando", rotulo: "Importando (recebendo doacao)" },
    MANUTENCAO: { id: "manutencao", rotulo: "Em manutencao" }
};

class UnidadeGeracao {
    constructor(id, fonte, capacidade_kw, producao_atual_kw = 0.0, comunidade_id = "", status = "operacional", sustentabilidade_pct = 100.0) {
        this.id = id;
        this.fonte = fonte;
        this.capacidade_kw = capacidade_kw;
        this.producao_atual_kw = producao_atual_kw;
        this.comunidade_id = comunidade_id;
        this.status = status;
        this.sustentabilidade_pct = sustentabilidade_pct;
    }
}

class UnidadeArmazenamento {
    constructor(id, tipo, capacidade_kwh, carga_atual_kwh = 0.0, comunidade_id = "", ciclos_vida = 10000) {
        this.id = id;
        this.tipo = tipo;
        this.capacidade_kwh = capacidade_kwh;
        this.carga_atual_kwh = carga_atual_kwh;
        this.comunidade_id = comunidade_id;
        this.ciclos_vida = ciclos_vida;
    }
}

class ConsumoRegistrado {
    constructor(id, comunidade_id, tipo, consumo_kw, timestamp = "", cidadao_ou_setor = "") {
        this.id = id;
        this.comunidade_id = comunidade_id;
        this.tipo = tipo;
        this.consumo_kw = consumo_kw;
        this.timestamp = timestamp;
        this.cidadao_ou_setor = cidadao_ou_setor;
    }
}

class Microgrid {
    constructor(id, nome, comunidade_id, unidades_geracao = [], unidades_armazenamento = [], interconexao = StatusInterconexao.ILHADO) {
        this.id = id;
        this.nome = nome;
        this.comunidade_id = comunidade_id;
        this.unidades_geracao = [...unidades_geracao];
        this.unidades_armazenamento = [...unidades_armazenamento];
        this.interconexao = interconexao;
        this.autonomia_horas = 0.0;
        this.geracao_total_kw = 0.0;
        this.demanda_total_kw = 0.0;
        this.cenario = StatusCenario.EQUILIBRIO;
    }
}

class AlocacaoEscassez {
    constructor(id, microgrid_id, deficit_kw, tipos_priorizados = [], tipos_rotacionados = [], tipos_suprimidos = [],
                duracao_estimada_h = 0.0, aprovado_em_assembleia = false, justificativa = "") {
        this.id = id;
        this.microgrid_id = microgrid_id;
        this.deficit_kw = deficit_kw;
        this.tipos_priorizados = [...tipos_priorizados];
        this.tipos_rotacionados = [...tipos_rotacionados];
        this.tipos_suprimidos = [...tipos_suprimidos];
        this.duracao_estimada_h = duracao_estimada_h;
        this.aprovado_em_assembleia = aprovado_em_assembleia;
        this.justificativa = justificativa;
    }
}

class EnergiaEngine {
    constructor() {
        this.geracao = {};
        this.armazenamento = {};
        this.consumos = [];
        this.microgrids = {};
        this.alocacoes = {};
        this._gen_id = 0;
        this._arm_id = 0;
        this._cons_id = 0;
        this._mg_id = 0;
        this._aloc_id = 0;
    }

    _gen_novo_id() { return `GEN-${String(++this._gen_id).padStart(4, '0')}`; }
    _arm_novo_id() { return `ARM-${String(++this._arm_id).padStart(4, '0')}`; }
    _cons_novo_id() { return `CON-${String(++this._cons_id).padStart(4, '0')}`; }
    _mg_novo_id() { return `GRID-${String(++this._mg_id).padStart(4, '0')}`; }
    _aloc_novo_id() { return `ALOC-${String(++this._aloc_id).padStart(4, '0')}`; }

    cadastrar_geracao(fonte, capacidade_kw, producao_atual_kw = 0.0, comunidade_id = "", sustentabilidade_pct = 100.0) {
        const u = new UnidadeGeracao(this._gen_novo_id(), fonte, capacidade_kw, producao_atual_kw, comunidade_id, "operacional", sustentabilidade_pct);
        this.geracao[u.id] = u;
        return u;
    }

    cadastrar_armazenamento(tipo, capacidade_kwh, carga_atual_kwh = 0.0, comunidade_id = "", ciclos_vida = 10000) {
        const a = new UnidadeArmazenamento(this._arm_novo_id(), tipo, capacidade_kwh, carga_atual_kwh, comunidade_id, ciclos_vida);
        this.armazenamento[a.id] = a;
        return a;
    }

    registrar_consumo(comunidade_id, tipo, consumo_kw, cidadao_ou_setor = "") {
        const c = new ConsumoRegistrado(this._cons_novo_id(), comunidade_id, tipo, consumo_kw, new Date().toISOString(), cidadao_ou_setor);
        this.consumos.push(c);
        return c;
    }

    criar_microgrid(nome, comunidade_id, unidades_geracao, unidades_armazenamento, interconexao = StatusInterconexao.ILHADO) {
        const mg = new Microgrid(this._mg_novo_id(), nome, comunidade_id, unidades_geracao, unidades_armazenamento, interconexao);
        this.microgrids[mg.id] = mg;
        this._atualizar_metricas_microgrid(mg.id);
        return mg;
    }

    _atualizar_metricas_microgrid(mg_id) {
        const mg = this.microgrids[mg_id];
        if (!mg) return;
        let geracao = 0;
        for (const gid of mg.unidades_geracao) if (this.geracao[gid]) geracao += this.geracao[gid].producao_atual_kw;
        let demanda = 0;
        for (const c of this.consumos) if (c.comunidade_id === mg.comunidade_id) demanda += c.consumo_kw;
        mg.geracao_total_kw = Math.round(geracao * 100) / 100;
        mg.demanda_total_kw = Math.round(demanda * 100) / 100;
        if (demanda === 0) { mg.cenario = StatusCenario.ABUNDANCIA; return; }
        const margem = (geracao - demanda) / demanda;
        if (margem >= 0.2) mg.cenario = StatusCenario.ABUNDANCIA;
        else if (margem >= 0) mg.cenario = StatusCenario.EQUILIBRIO;
        else if (margem >= -0.1) mg.cenario = StatusCenario.ATENCAO;
        else if (margem >= -0.3) mg.cenario = StatusCenario.ESCASSEZ;
        else mg.cenario = StatusCenario.EMERGENCIA;
        let armazenamento_total = 0;
        for (const aid of mg.unidades_armazenamento) if (this.armazenamento[aid]) armazenamento_total += this.armazenamento[aid].carga_atual_kwh;
        mg.autonomia_horas = demanda > 0 ? Math.round(armazenamento_total / demanda * 100) / 100 : 0;
    }

    diagnosticar_microgrid(mg_id) {
        this._atualizar_metricas_microgrid(mg_id);
        const mg = this.microgrids[mg_id];
        if (!mg) return [StatusCenario.EQUILIBRIO, { erro: "Microgrid nao encontrada" }];
        const deficit = Math.max(0, mg.demanda_total_kw - mg.geracao_total_kw);
        const excedente = Math.max(0, mg.geracao_total_kw - mg.demanda_total_kw);
        let renovavel = 0;
        for (const gid of mg.unidades_geracao) {
            const g = this.geracao[gid];
            if (g && g.fonte.renovavel) renovavel += g.producao_atual_kw;
        }
        const pct_renovavel = mg.geracao_total_kw ? Math.round(renovavel / mg.geracao_total_kw * 1000) / 10 : 0;
        const info = {
            geracao_kw: mg.geracao_total_kw,
            demanda_kw: mg.demanda_total_kw,
            deficit_kw: Math.round(deficit * 100) / 100,
            excedente_kw: Math.round(excedente * 100) / 100,
            autonomia_h: mg.autonomia_horas,
            pct_renovavel,
            interconexao: mg.interconexao.rotulo
        };
        return [mg.cenario, info];
    }

    propor_alocacao_escassez(mg_id, duracao_estimada_h = 24.0) {
        const mg = this.microgrids[mg_id];
        if (!mg) return null;
        this._atualizar_metricas_microgrid(mg_id);
        if (mg.cenario !== StatusCenario.ESCASSEZ && mg.cenario !== StatusCenario.EMERGENCIA) return null;
        const deficit = mg.demanda_total_kw - mg.geracao_total_kw;
        if (deficit <= 0) return null;
        const consumo_por_tipo = {};
        for (const c of this.consumos) {
            if (c.comunidade_id === mg.comunidade_id) {
                consumo_por_tipo[c.tipo] = (consumo_por_tipo[c.tipo] || 0) + c.consumo_kw;
            }
        }
        const tipos_ordenados = Object.keys(consumo_por_tipo).sort((a, b) => a.prioridade - b.prioridade);
        let geracao_disponivel = mg.geracao_total_kw;
        const priorizados = [], rotacionados = [], suprimidos = [];
        for (const tipo of tipos_ordenados) {
            const consumo_tipo = consumo_por_tipo[tipo];
            if (geracao_disponivel >= consumo_tipo) {
                priorizados.push(tipo);
                geracao_disponivel -= consumo_tipo;
            } else if (geracao_disponivel > 0) {
                rotacionados.push(tipo);
                geracao_disponivel = 0;
            } else {
                suprimidos.push(tipo);
            }
        }
        const aloc = new AlocacaoEscassez(this._aloc_novo_id(), mg_id, Math.round(deficit * 100) / 100,
            priorizados, rotacionados, suprimidos, duracao_estimada_h, false,
            `Deficit de ${deficit.toFixed(1)} kW. Geracao alocada por prioridade: essenciais garantidos, nao-essenciais em rodizio/corte. Ninguem fica sem energia essencial por dinheiro (P1).`);
        this.alocacoes[aloc.id] = aloc;
        return aloc;
    }

    aprovar_alocacao(aloc_id) {
        const a = this.alocacoes[aloc_id];
        if (!a) return false;
        a.aprovado_em_assembleia = true;
        return true;
    }

    doar_excedente(mg_origem_id, mg_destino_id) {
        this._atualizar_metricas_microgrid(mg_origem_id);
        this._atualizar_metricas_microgrid(mg_destino_id);
        const origem = this.microgrids[mg_origem_id];
        const destino = this.microgrids[mg_destino_id];
        if (!origem || !destino) return null;
        const excedente = origem.geracao_total_kw - origem.demanda_total_kw;
        const deficit = destino.demanda_total_kw - destino.geracao_total_kw;
        if (excedente <= 0 || deficit <= 0) return null;
        const doado = Math.min(excedente, deficit);
        origem.interconexao = StatusInterconexao.EXPORTANDO;
        destino.interconexao = StatusInterconexao.IMPORTANDO;
        origem.geracao_total_kw = Math.round((origem.geracao_total_kw - doado) * 100) / 100;
        destino.geracao_total_kw = Math.round((destino.geracao_total_kw + doado) * 100) / 100;
        this._atualizar_metricas_microgrid(mg_origem_id);
        this._atualizar_metricas_microgrid(mg_destino_id);
        return Math.round(doado * 100) / 100;
    }

    auditoria_eficiencia(comunidade_id) {
        const consumos_com = this.consumos.filter(c => c.comunidade_id === comunidade_id);
        if (!consumos_com.length) return { comunidade: comunidade_id, consumo_total_kw: 0, alertas_eficiencia: [] };
        const consumo_total = consumos_com.reduce((s, c) => s + c.consumo_kw, 0);
        const consumo_por_tipo = {};
        for (const c of consumos_com) consumo_por_tipo[c.tipo] = (consumo_por_tipo[c.tipo] || 0) + c.consumo_kw;
        const alertas = [];
        for (const [tipo, val] of Object.entries(consumo_por_tipo)) {
            if (tipo === TipoConsumo.RESIDENCIAL_EXCEDENTE && val > consumo_total * 0.3) {
                alertas.push(`Consumo residencial excedente alto (${val.toFixed(1)} kW, ${(val / consumo_total * 100).toFixed(0)}% do total). Lembrar: eficiencia liberta capacidade para a comunidade.`);
            }
            if (tipo === TipoConsumo.PRODUCAO_BENS && val > consumo_total * 0.4) {
                alertas.push(`Producao de bens consome ${val.toFixed(1)} kW. Otimizar processos = mais capacidade para saude e educacao.`);
            }
        }
        const porTipoRotulo = {};
        for (const [tipo, v] of Object.entries(consumo_por_tipo)) porTipoRotulo[tipo.rotulo] = Math.round(v * 10) / 10;
        return {
            comunidade: comunidade_id,
            consumo_total_kw: Math.round(consumo_total * 100) / 100,
            consumo_por_tipo: porTipoRotulo,
            alertas_eficiencia: alertas,
            mensagem: "Energia e gratuita. Eficiencia nao economiza dinheiro -- LIBERTA capacidade para quem precisa. E kaizen civico."
        };
    }

    scorecard() {
        const geracao_total = Object.values(this.geracao).reduce((s, g) => s + g.producao_atual_kw, 0);
        const renovavel = Object.values(this.geracao).filter(g => g.fonte.renovavel).reduce((s, g) => s + g.producao_atual_kw, 0);
        const demanda_total = this.consumos.reduce((s, c) => s + c.consumo_kw, 0);
        const armazenamento_total = Object.values(this.armazenamento).reduce((s, a) => s + a.carga_atual_kwh, 0);
        const doacoes_realizadas = Object.values(this.microgrids).filter(mg => mg.interconexao === StatusInterconexao.EXPORTANDO).length;
        return {
            unidades_geracao: Object.keys(this.geracao).length,
            unidades_armazenamento: Object.keys(this.armazenamento).length,
            microgrids: Object.keys(this.microgrids).length,
            geracao_total_kw: Math.round(geracao_total * 10) / 10,
            demanda_total_kw: Math.round(demanda_total * 10) / 10,
            excedente_kw: Math.round(Math.max(0, geracao_total - demanda_total) * 10) / 10,
            pct_renovavel: geracao_total ? Math.round(renovavel / geracao_total * 1000) / 10 : 0,
            armazenamento_kwh: Math.round(armazenamento_total * 10) / 10,
            alocacoes_escassez: Object.keys(this.alocacoes).length,
            doacoes_realizadas
        };
    }
}

function _demo() {
    const e = new EnergiaEngine();
    console.log("=".repeat(70));
    console.log("OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso");
    console.log("=".repeat(70));

    console.log("\n[CENARIO 1] Solar Village -- abundancia (geracao > demanda)");
    const g1 = e.cadastrar_geracao(FonteEnergia.SOLAR, 500.0, 480.0, "solar_village");
    const g2 = e.cadastrar_geracao(FonteEnergia.EOLICA, 300.0, 250.0, "solar_village");
    const a1 = e.cadastrar_armazenamento(TipoArmazenamento.BATERIA_LITIO, 2000.0, 1500.0, "solar_village");
    const a2 = e.cadastrar_armazenamento(TipoArmazenamento.BATERIA_FLUXO, 5000.0, 4000.0, "solar_village");
    e.registrar_consumo("solar_village", TipoConsumo.ESSENCIAL_VIDA, 120.0);
    e.registrar_consumo("solar_village", TipoConsumo.SAUDE, 40.0);
    e.registrar_consumo("solar_village", TipoConsumo.COMUNICACAO, 30.0);
    e.registrar_consumo("solar_village", TipoConsumo.EDUCACAO, 50.0);
    e.registrar_consumo("solar_village", TipoConsumo.CULTURA_LAZER, 80.0);
    e.registrar_consumo("solar_village", TipoConsumo.RESIDENCIAL_EXCEDENTE, 100.0);
    const mg1 = e.criar_microgrid("Solar Village Grid", "solar_village", [g1.id, g2.id], [a1.id, a2.id], StatusInterconexao.CONECTADO);
    const [cenario1, info1] = e.diagnosticar_microgrid(mg1.id);
    console.log(`  Geracao: ${info1.geracao_kw} kW | Demanda: ${info1.demanda_kw} kW`);
    console.log(`  Excedente: ${info1.excedente_kw} kW | Renovavel: ${info1.pct_renovavel}%`);
    console.log(`  Autonomia (ilhado): ${info1.autonomia_h}h`);
    console.log(`  Cenario: ${cenario1.rotulo}`);
    console.log("  Energia para QUALQUER uso: sim, sem conta, sem medidor de cobranca.");

    console.log("\n[CENARIO 2] Vale Seco -- escassez (seca reduziu hidro)");
    const g3 = e.cadastrar_geracao(FonteEnergia.HIDRO, 400.0, 150.0, "vale_seco");
    const g4 = e.cadastrar_geracao(FonteEnergia.SOLAR, 200.0, 180.0, "vale_seco");
    const a3 = e.cadastrar_armazenamento(TipoArmazenamento.HIDROGENIO, 3000.0, 800.0, "vale_seco");
    e.registrar_consumo("vale_seco", TipoConsumo.ESSENCIAL_VIDA, 100.0);
    e.registrar_consumo("vale_seco", TipoConsumo.SAUDE, 60.0);
    e.registrar_consumo("vale_seco", TipoConsumo.COMUNICACAO, 20.0);
    e.registrar_consumo("vale_seco", TipoConsumo.EDUCACAO, 40.0);
    e.registrar_consumo("vale_seco", TipoConsumo.PRODUCAO_BENS, 80.0);
    e.registrar_consumo("vale_seco", TipoConsumo.CULTURA_LAZER, 50.0);
    const mg2 = e.criar_microgrid("Vale Seco Grid", "vale_seco", [g3.id, g4.id], [a3.id], StatusInterconexao.CONECTADO);
    const [cenario2, info2] = e.diagnosticar_microgrid(mg2.id);
    console.log(`  Geracao: ${info2.geracao_kw} kW | Demanda: ${info2.demanda_kw} kW`);
    console.log(`  Deficit: ${info2.deficit_kw} kW | Cenario: ${cenario2.rotulo}`);
    console.log(`  Autonomia: ${info2.autonomia_h}h`);

    console.log("\n[ALOCACAO DEMOCRATICA EM ESCASSEZ]");
    const aloc = e.propor_alocacao_escassez(mg2.id, 48.0);
    if (aloc) {
        console.log(`  Proposta ${aloc.id} (assembleia precisa aprovar):`);
        console.log(`  Deficit: ${aloc.deficit_kw} kW | Duracao estimada: ${aloc.duracao_estimada_h}h`);
        console.log(`  GARANTIDOS (prioridade): ${aloc.tipos_priorizados.map(t => t.rotulo)}`);
        console.log(`  EM RODIZIO: ${aloc.tipos_rotacionados.map(t => t.rotulo)}`);
        console.log(`  SUPRIMIDOS: ${aloc.tipos_suprimidos.map(t => t.rotulo)}`);
        console.log(`  Justificativa: ${aloc.justificativa}`);
        e.aprovar_alocacao(aloc.id);
        console.log(`  Aprovado em assembleia: ${aloc.aprovado_em_assembleia}`);
    }

    console.log("\n[DOACAO P2P] Solar Village doe excedente para Vale Seco");
    const doado = e.doar_excedente(mg1.id, mg2.id);
    if (doado) {
        console.log(`  ${doado.toFixed(1)} kW doados (sem dinheiro, sem cobranca).`);
        const [, info2_pos] = e.diagnosticar_microgrid(mg2.id);
        console.log(`  Vale Seco pos-doacao: geracao=${info2_pos.geracao_kw} kW, deficit=${info2_pos.deficit_kw} kW, cenario=${info2_pos.interconexao}`);
    }

    console.log("\n[AUDITORIA DE EFICIENCIA -- dever civico, nao economia]");
    const aud = e.auditoria_eficiencia("solar_village");
    console.log(`  Comunidade: ${aud.comunidade}`);
    console.log(`  Consumo total: ${aud.consumo_total_kw} kW`);
    for (const [tipo, val] of Object.entries(aud.consumo_por_tipo)) console.log(`    ${tipo}: ${val} kW`);
    for (const alerta of aud.alertas_eficiencia) console.log(`  ALERTA: ${alerta}`);
    console.log(`  ${aud.mensagem}`);

    console.log("\n" + "=".repeat(70));
    console.log("[SCORECARD ENERGETICO DA REPUBLICA]");
    console.log("=".repeat(70));
    const sc = e.scorecard();
    for (const [k, v] of Object.entries(sc)) console.log(`  ${k.padEnd(28, ".")} ${v}`);

    console.log("\n[FONTES DE ENERGIA DA REPUBLICA]");
    for (const f of Object.values(FonteEnergia)) {
        const flag = f.renovavel ? "renovavel" : "NAO-renovavel";
        console.log(`  ${f.rotulo.padEnd(30, ".")} [${flag}]`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("FILOSOFIA -- Por que energia e gratuita para todo e qualquer uso");
    console.log("=".repeat(70));
    console.log(`ENERGIA NAO E MERCADORIA. E CONDICAO DE VIDA.
Cozinhar precisa de energia. Aquecer precisa de energia.
Curar precisa de energia. Comunicar precisa de energia.
Estudar precisa de energia. Criar precisa de energia.
Cobrar por energia e cobrar por EXISTIR.

O ARGUMENTO DA ESCASSEZ (e por que e falso):
O capitalismo diz: "se energia e gratis, todos desperdicam."
Falso. O capitalista desperdica porque o custo e EXTERNO ao lucro.
O cidadao da Republica SABE que a energia que desperdica falta para o vizinho.
Eficiencia nao economiza dinheiro -- LIBERTA capacidade para a comunidade.

A UNICA ESCASSEZ REAL (e como se resolve):
Quando a geracao nao cobre a demanda (seca, falha), a assembleia decide:
1. Essenciais (vida, saude, comunicacao) SEMPRE garantidos.
2. Nao-essenciais em rodizio democratico.
3. Ninguem fica sem energia por DINHEIRO. So por PRIORIDADE civica.
4. A solucao de longo prazo e GERAR MAIS, nao racionar.
O capitalismo raciona por preco (quem tem dinheiro usa, quem nao tem corta).
A Republica aloca por prioridade (todos tem o essencial, o resto e civico).

A REVOLUCAO ENERGETICA:
1. Cada comunidade gera a propria energia (geracao distribuida).
2. Excedente e DOADO, nao vendido (P2P, sem intermediario).
3. Armazenamento comunitario (baterias compartilhadas).
4. 100% renovavel (a Republica respeita o planeta que a sustenta).
5. Nucleo essencial garantido para TODOS, sem excecao, sem condicao.
6. "Para todo e qualquer uso" -- a Republica nao pergunta PARA QUE.
   Pergunta quanto voce PRECISA, e garante que tem.

A ENERGIA E O AR DA CIVILIZACAO.
Ninguem cobra pelo ar. Ninguem deve cobrar pela energia.
`);
}

if (require.main === module) {
    _demo();
}

module.exports = { EnergiaEngine, FonteEnergia, TipoConsumo, TipoArmazenamento, StatusCenario, StatusInterconexao };