// OpenAgrarianRevolution.js
// Transpilacao fiel do Python para JavaScript (ES6)
// Comentarios e strings em Portugues (conforme fonte)

const TipoTenencia = {
    GUARDIAO_FAMILIAR: { id: "guardiao_familiar", rotulo: "Guardiao familiar", familias_max: 1 },
    COOPERATIVA: { id: "cooperativa", rotulo: "Cooperativa agricola", familias_max: 5 },
    COMUNIDADE_TRADICIONAL: { id: "comunidade_tradicional", rotulo: "Comunidade tradicional (quilombo/ribeirinho/aldeia)", familias_max: 10 },
    ASSENTAMENTO_COLETIVO: { id: "assentamento_coletivo", rotulo: "Assentamento coletivo da Republica", familias_max: 8 },
    RESERVA_REGENERACAO: { id: "reserva_regeneracao", rotulo: "Reserva de regeneracao do solo (repouso)", familias_max: 0 },
    USO_PUBLICO: { id: "uso_publico", rotulo: "Uso publico (escola, enfermaria, mercado)", familias_max: 0 }
};

const UsoSolo = {
    LAVOURA_ALIMENTACAO: { id: "lavoura_alimentacao", rotulo: "Lavoura de alimentos basicos" },
    LAVOURA_DIVERSIFICADA: { id: "lavoura_diversificada", rotulo: "Policultivo diversificado" },
    PASTAGEM_REGENERATIVA: { id: "pastagem_regenerativa", rotulo: "Pastagem rotativa regenerativa" },
    AGROFLORESTA: { id: "agrofloresta", rotulo: "Sistema agroflorestal (SAF)" },
    HORTA_COMUNITARIA: { id: "horta_comunitaria", rotulo: "Horta comunitaria de bairro" },
    POMAR: { id: "pomar", rotulo: "Pomar frutifero" },
    RESERVA_NATIVA: { id: "reserva_nativa", rotulo: "Reserva de vegetacao nativa" },
    CULTURA_TRADICIONAL: { id: "cultura_tradicional", rotulo: "Cultivo tradicional ancestral" },
    INFRAESTRUTURA: { id: "infraestrutura", rotulo: "Infraestrutura (casa, galpao, escola)" },
    OCIOSO: { id: "ocioso", rotulo: "Ocioso (sem funcao social)" }
};

const StatusReforma = {
    DIAGNOSTICO: { id: "diagnostico", rotulo: "Diagnostico fundiario em curso" },
    NOTIFICACAO: { id: "notificacao", rotulo: "Latifundio notificado (funcao social cobrada)" },
    DESAPROPRIACAO: { id: "desapropriacao", rotulo: "Desapropriacao decidida em assembleia" },
    ASSENTAMENTO: { id: "assentamento", rotulo: "Familias assentadas como guardias" },
    REGULARIZACAO: { id: "regularizacao", rotulo: "Regularizacao cooperativa ativa" },
    CONSOLIDADO: { id: "consolidado", rotulo: "Territorio consolidado (auto-gestionario)" },
    CONFLITO: { id: "conflito", rotulo: "Conflito fundiario ativo (grileiro/invasao)" }
};

const TipoConflito = {
    GRILAGEM: { id: "grilagem", rotulo: "Grilagem (falsificacao de titulo)", gravidade: 4 },
    INVASAO_LATIFUNDIO: { id: "invasao_latifundio", rotulo: "Trabalhador expulso por latifundio", gravidade: 5 },
    TRABALHO_ESCRAVO: { id: "trabalho_escravo", rotulo: "Trabalho analogo a escravidao", gravidade: 5 },
    DESPEJO: { id: "despejo", rotulo: "Despejo de familia guardi", gravidade: 4 },
    CONFLITO_FRONTEIRA: { id: "conflito_fronteira", rotulo: "Disputa de fronteira entre comunidades", gravidade: 2 },
    MINERACAO_ILEGAL: { id: "mineracao_ilegal", rotulo: "Mineracao/predacao ilegal em terra guardia", gravidade: 4 },
    AGROTOXICO: { id: "agrotoxico", rotulo: "Contaminacao por agrotoxico vizinho", gravidade: 3 },
    QUEIMADA_CRIMINOSA: { id: "queimada_criminosa", rotulo: "Queimada criminosa / desmatamento", gravidade: 4 }
};

const TamanhoImovel = {
    MINIFUNDIO: { id: "minifundio", rotulo: "Minifundio (insuficiente, < 1 modulo)", area_min: 0, area_max: 50 },
    PEQUENO: { id: "pequeno", rotulo: "Pequena area (1-4 modulos)", area_min: 50, area_max: 200 },
    MEDIO: { id: "medio", rotulo: "Media area (4-15 modulos)", area_min: 200, area_max: 750 },
    LATIFUNDIO_DIMENSAO: { id: "latifundio_dimensao", rotulo: "Latifundio por dimensao (>15 modulos)", area_min: 750, area_max: 99999 },
    LATIFUNDIO_EXPLORACAO: { id: "latifundio_exploracao", rotulo: "Latifundio por exploracao (ocioso/grilado)", area_min: 0, area_max: 99999 }
};

const FuncaoSocialStatus = {
    CUMPRE: { id: "cumpre", rotulo: "Cumpre funcao social" },
    PARCIAL: { id: "parcial", rotulo: "Cumpre parcialmente" },
    DESCUMPRE: { id: "descumpre", rotulo: "Descumpre funcao social" }
};

const PlanoAgrologia = {
    PLANTIO_DIRETO: { id: "plantio_direto", rotulo: "Plantio direto (nao revolver solo)" },
    ADUBACAO_VERDE: { id: "adubacao_verde", rotulo: "Adubacao verde (leguminosas)" },
    COMPOSTAGEM: { id: "compostagem", rotulo: "Compostagem comunitaria" },
    ROTACAO_CULTURAS: { id: "rotacao_culturas", rotulo: "Rotacao de culturas" },
    CICLO_FECHADO: { id: "ciclo_fechado", rotulo: "Ciclo fechado (zero insumo externo)" },
    AGROFLORESTA_SUCSSIONAL: { id: "agrofloresta_sucessional", rotulo: "Agrofloresta sucessional" },
    CAPTACAO_CHUVA: { id: "captacao_chuva", rotulo: "Captacao de agua de chuva" },
    BIOINSUMOS: { id: "bioinsumos", rotulo: "Bioinsumos (proibido agrotoxico sintetico)" },
    INTEGRACAO_ANIMAL: { id: "integracao_animal", rotulo: "Integracao lavoura-pecuaria-floresta" }
};

class ImovelRural {
    constructor(id, nome, area_hectares, municipio, bioma, tipo_tenencia, usos_solo = [], familias_guardias = 0,
                funcao_social = FuncaoSocialStatus.DESCUMPRE, produtividade_pct = 0.0, plano_agrologia = [],
                status = StatusReforma.DIAGNOSTICO, historico_antigo = "") {
        this.id = id;
        this.nome = nome;
        this.area_hectares = area_hectares;
        this.municipio = municipio;
        this.bioma = bioma;
        this.tipo_tenencia = tipo_tenencia;
        this.usos_solo = [...usos_solo];
        this.familias_guardias = familias_guardias;
        this.funcao_social = funcao_social;
        this.produtividade_pct = produtividade_pct;
        this.plano_agrologia = [...plano_agrologia];
        this.status = status;
        this.historico_antigo = historico_antigo;
    }
}

class FamiliaGuardia {
    constructor(id, nome_referencia, pessoas, parcela_hectares, cooperativa_id = null, chegada_de = "", conhecimento_tradicional = false) {
        this.id = id;
        this.nome_referencia = nome_referencia;
        this.pessoas = pessoas;
        this.parcela_hectares = parcela_hectares;
        this.cooperativa_id = cooperativa_id;
        this.chegada_de = chegada_de;
        this.conhecimento_tradicional = conhecimento_tradicional;
    }
}

class ConflitoFundiario {
    constructor(id, tipo, territorio_id, vitimas = 0, familias_afetadas = 0, descricao = "") {
        this.id = id;
        this.tipo = tipo;
        this.territorio_id = territorio_id;
        this.vitimas = vitimas;
        this.familias_afetadas = familias_afetadas;
        this.descricao = descricao;
        this.resolucao_proposta = "";
        this.resolvido = false;
    }
}

class CooperativaAgricola {
    constructor(id, nome, familia_ids = [], territorio_ids = [], excedente_destino = "", ferramentas_compartilhadas = []) {
        this.id = id;
        this.nome = nome;
        this.familia_ids = [...familia_ids];
        this.territorio_ids = [...territorio_ids];
        this.excedente_destino = excedente_destino;
        this.ferramentas_compartilhadas = [...ferramentas_compartilhadas];
    }
}

class DiagnosticoFundiario {
    constructor(territorio, total_area, num_imoveis, indice_gini, pct_area_latifundio, familias_sem_terra, familias_guardias, veredito = "") {
        this.territorio = territorio;
        this.total_area = total_area;
        this.num_imoveis = num_imoveis;
        this.indice_gini = indice_gini;
        this.pct_area_latifundio = pct_area_latifundio;
        this.familias_sem_terra = familias_sem_terra;
        this.familias_guardias = familias_guardias;
        this.veredito = veredito;
    }
}

class ReformaAgrariaEngine {
    constructor() {
        this.imoveis = {};
        this.familias = {};
        this.cooperativas = {};
        this.conflitos = {};
        this._im_id = 0;
        this._fam_id = 0;
        this._coop_counter = 0;
        this._conf_id = 0;
    }

    _imovel_id() {
        this._im_id++;
        return `TER-${String(this._im_id).padStart(4, '0')}`;
    }

    _familia_id() {
        this._fam_id++;
        return `FAM-${String(this._fam_id).padStart(4, '0')}`;
    }

    _coop_id() {
        this._coop_counter++;
        return `COOP-${String(this._coop_counter).padStart(4, '0')}`;
    }

    _conflito_id() {
        this._conf_id++;
        return `CONF-${String(this._conf_id).padStart(4, '0')}`;
    }

    cadastrar_imovel(nome, area_hectares, municipio, bioma, tipo_tenencia, usos_solo = null, familias_guardias = 0,
                     funcao_social = FuncaoSocialStatus.DESCUMPRE, produtividade_pct = 0.0, plano = null,
                     status = StatusReforma.DIAGNOSTICO, historico_antigo = "") {
        const im = new ImovelRural(this._imovel_id(), nome, area_hectares, municipio, bioma, tipo_tenencia,
            usos_solo || [], familias_guardias, funcao_social, produtividade_pct, plano || [], status, historico_antigo);
        this.imoveis[im.id] = im;
        return im;
    }

    cadastrar_familia(nome_referencia, pessoas, parcela_hectares, cooperativa_id = null, chegada_de = "voluntario", conhecimento_tradicional = false) {
        const f = new FamiliaGuardia(this._familia_id(), nome_referencia, pessoas, parcela_hectares, cooperativa_id, chegada_de, conhecimento_tradicional);
        this.familias[f.id] = f;
        return f;
    }

    criar_cooperativa(nome, familia_ids, territorio_ids, excedente_destino = "mercado_aberto", ferramentas = null) {
        const c = new CooperativaAgricola(this._coop_id(), nome, familia_ids, territorio_ids, excedente_destino, ferramentas || []);
        this.cooperativas[c.id] = c;
        for (const fid of familia_ids) {
            if (this.familias[fid]) this.familias[fid].cooperativa_id = c.id;
        }
        return c;
    }

    registrar_conflito(tipo, territorio_id, vitimas = 0, familias_afetadas = 0, descricao = "") {
        const c = new ConflitoFundiario(this._conflito_id(), tipo, territorio_id, vitimas, familias_afetadas, descricao);
        this.conflitos[c.id] = c;
        return c;
    }

    classificar_tamanho(area, ocioso = false) {
        if (ocioso && area >= TamanhoImovel.PEQUENO.area_min) return TamanhoImovel.LATIFUNDIO_EXPLORACAO;
        const tamanhos = [TamanhoImovel.MINIFUNDIO, TamanhoImovel.PEQUENO, TamanhoImovel.MEDIO, TamanhoImovel.LATIFUNDIO_DIMENSAO];
        for (const t of tamanhos) {
            if (t.area_min <= area && area < t.area_max) return t;
        }
        return TamanhoImovel.LATIFUNDIO_DIMENSAO;
    }

    indice_gini_areas() {
        const areas = Object.values(this.imoveis).map(im => im.area_hectares).sort((a, b) => a - b);
        const n = areas.length;
        if (n === 0) return 0.0;
        const total = areas.reduce((a, b) => a + b, 0);
        if (total === 0) return 0.0;
        let soma_pond = 0.0;
        for (let i = 0; i < n; i++) soma_pond += (i + 1) * areas[i];
        const gini = (2 * soma_pond) / (n * total) - (n + 1) / n;
        return Math.round(gini * 10000) / 10000;
    }

    diagnosticar(territorio) {
        const ims = Object.values(this.imoveis).filter(im => im.municipio === territorio);
        const total_area = ims.reduce((sum, im) => sum + im.area_hectares, 0);
        const num = ims.length;
        if (num === 0) {
            return new DiagnosticoFundiario(territorio, 0.0, 0, 0.0, 0.0, 0, 0, "Territorio vazio no cadastro.");
        }
        const gini = this.indice_gini_areas();
        let area_lat = 0.0;
        for (const im of ims) {
            const ocioso = im.funcao_social === FuncaoSocialStatus.DESCUMPRE;
            const tam = this.classificar_tamanho(im.area_hectares, ocioso);
            if (tam === TamanhoImovel.LATIFUNDIO_DIMENSAO || tam === TamanhoImovel.LATIFUNDIO_EXPLORACAO) {
                area_lat += im.area_hectares;
            }
        }
        const pct_lat = total_area > 0 ? (area_lat / total_area * 100.0) : 0.0;
        const familias_guardias = ims.reduce((sum, im) => sum + im.familias_guardias, 0);
        const familias_sem_terra = Math.max(0, Math.floor((pct_lat / 100.0) * familias_guardias / 4));
        let veredito;
        if (gini > 0.7 || pct_lat > 50) veredito = "CONCENTRACAO CRITICA: revolicao agraria URGENTE.";
        else if (gini > 0.4 || pct_lat > 25) veredito = "CONCENTRACAO ALTA: notificar latifundios, cobrar funcao social.";
        else if (gini > 0.2) veredito = "CONCENTRACAO MODERADA: regularizar e cooperativizar.";
        else veredito = "TERRITORIO EQUITATIVO: consolidar cooperativas.";
        return new DiagnosticoFundiario(territorio, total_area, num, gini, Math.round(pct_lat * 10) / 10,
            familias_sem_terra, familias_guardias, veredito);
    }

    auditar_funcao_social(imovel_id) {
        const im = this.imoveis[imovel_id];
        if (!im) return [FuncaoSocialStatus.DESCUMPRE, ["Imovel nao encontrado."]];
        const faltas = [];
        if (im.produtividade_pct < 40) faltas.push(`Produtividade baixa (${im.produtividade_pct.toFixed(0)}% do potencial).`);
        if (im.plano_agrologia.length === 0) faltas.push("Sem plano de agrologia (solo sendo exaurido).");
        for (const conf of Object.values(this.conflitos)) {
            if (conf.tipo === TipoConflito.TRABALHO_ESCRAVO && conf.territorio_id === im.id && !conf.resolvido) {
                faltas.push("Trabalho analogo a escravidao detectado (BLOQUEANTE).");
                break;
            }
        }
        if (im.familias_guardias === 0 && im.tipo_tenencia !== TipoTenencia.RESERVA_REGENERACAO) {
            faltas.push("Nenhuma familia guardia: terra abandonada.");
        }
        if (faltas.length > 0) {
            im.funcao_social = faltas.length === 1 ? FuncaoSocialStatus.PARCIAL : FuncaoSocialStatus.DESCUMPRE;
        } else {
            im.funcao_social = FuncaoSocialStatus.CUMPRE;
        }
        return [im.funcao_social, faltas];
    }

    notificar_latifundio(imovel_id) {
        const im = this.imoveis[imovel_id];
        if (!im) return null;
        const ocioso = im.funcao_social === FuncaoSocialStatus.DESCUMPRE;
        const tam = this.classificar_tamanho(im.area_hectares, ocioso);
        if (tam !== TamanhoImovel.LATIFUNDIO_DIMENSAO && tam !== TamanhoImovel.LATIFUNDIO_EXPLORACAO) {
            return `${im.id} nao e latifundio (${tam.rotulo}).`;
        }
        const [status, faltas] = this.auditar_funcao_social(im.id);
        if (status === FuncaoSocialStatus.CUMPRE) {
            im.status = StatusReforma.REGULARIZACAO;
            return `${im.id} cumpre funcao social -> regularizar como cooperativa.`;
        }
        im.status = StatusReforma.NOTIFICACAO;
        const faltasStr = faltas.length === 0 ? "none" : faltas.join("; ");
        return `NOTIFICADO ${im.id} (${tam.rotulo}, ${im.area_hectares.toFixed(0)} ha). Faltas: ${faltasStr}. Prazo para regularizar.`;
    }

    desaproropriar(imovel_id, familias_assentar) {
        const im = this.imoveis[imovel_id];
        if (!im) return null;
        if (im.status !== StatusReforma.NOTIFICACAO && im.status !== StatusReforma.DIAGNOSTICO) {
            return `${im.id} em status ${im.status.rotulo} -- nao elegivel para desapropriacao agora.`;
        }
        im.historico_antigo = im.historico_antigo || im.nome;
        im.nome = `Territorio Livre ${im.id}`;
        im.tipo_tenencia = TipoTenencia.ASSENTAMENTO_COLETIVO;
        if (familias_assentar.length > 0) {
            const parcela = im.area_hectares / familias_assentar.length;
            for (const fid of familias_assentar) {
                const fam = this.familias[fid];
                if (fam) {
                    fam.parcela_hectares = Math.round(parcela * 100) / 100;
                    fam.chegada_de = "assentamento";
                }
            }
            im.familias_guardias = familias_assentar.length;
        }
        im.status = StatusReforma.ASSENTAMENTO;
        im.funcao_social = FuncaoSocialStatus.PARCIAL;
        return `DESAPROPRIVADO ${im.id}: ${familias_assentar.length} familias guardias assentadas, ${im.area_hectares.toFixed(0)} ha sob cuidado coletivo.`;
    }

    consolidar_cooperativa(nome, territorio_ids, familias_ids, excedente = "mercado_aberto", ferramentas = null) {
        const coop = this.criar_cooperativa(nome, familias_ids, territorio_ids, excedente, ferramentas);
        for (const tid of territorio_ids) {
            const im = this.imoveis[tid];
            if (im) {
                im.tipo_tenencia = TipoTenencia.COOPERATIVA;
                im.status = StatusReforma.CONSOLIDADO;
                im.funcao_social = FuncaoSocialStatus.CUMPRE;
            }
        }
        return coop;
    }

    conflitos_por_gravidade() {
        return Object.values(this.conflitos).sort((c1, c2) => {
            const g = c2.tipo.gravidade - c1.tipo.gravidade;
            if (g !== 0) return g;
            return c2.familias_afetadas - c1.familias_afetadas;
        });
    }

    resolver_conflito(conflito_id, resolucao) {
        const c = this.conflitos[conflito_id];
        if (!c) return false;
        c.resolucao_proposta = resolucao;
        c.resolvido = true;
        return true;
    }

    area_total() {
        return Object.values(this.imoveis).reduce((sum, im) => sum + im.area_hectares, 0);
    }

    area_ociosa() {
        return Object.values(this.imoveis)
            .filter(im => im.funcao_social === FuncaoSocialStatus.DESCUMPRE)
            .reduce((sum, im) => sum + im.area_hectares, 0);
    }

    familias_atendidas() {
        return Object.values(this.imoveis).reduce((sum, im) => sum + im.familias_guardias, 0);
    }

    pessoas_atendidas() {
        return Object.values(this.imoveis).reduce((sum, im) => sum + im.familias_guardias * 4, 0);
    }

    scorecard() {
        const total = this.area_total();
        const ociosa = this.area_ociosa();
        const pct = total > 0 ? Math.round((ociosa / total * 100) * 10) / 10 : 0.0;
        const conflitos_abertos = Object.values(this.conflitos).filter(c => !c.resolvido).length;
        const consolidados = Object.values(this.imoveis).filter(im => im.status === StatusReforma.CONSOLIDADO).length;
        return {
            imoveis_cadastrados: Object.keys(this.imoveis).length,
            area_total_ha: Math.round(total * 10) / 10,
            area_ociosa_ha: Math.round(ociosa * 10) / 10,
            pct_ociosa: pct,
            familias_guardias: this.familias_atendidas(),
            cooperativas: Object.keys(this.cooperativas).length,
            conflitos_abertos: conflitos_abertos,
            indice_gini: this.indice_gini_areas(),
            consolidados: consolidados
        };
    }
}

function _demo() {
    const e = new ReformaAgrariaEngine();

    console.log("=".repeat(70));
    console.log("OpenAgrarianRevolution -- A Terra e de Quem a Cuida");
    console.log("=".repeat(70));

    const latif = e.cadastrar_imovel(
        "Fazenda Boa Vista (ex-latifundio)", 2500.0, "Sertao do Sao Francisco", "caatinga",
        TipoTenencia.GUARDIAO_FAMILIAR, [UsoSolo.PASTAGEM_REGENERATIVA, UsoSolo.OCIOSO], 3,
        FuncaoSocialStatus.DESCUMPRE, 15.0, [], StatusReforma.DIAGNOSTICO, "Familia herdeira de titulo duvidoso"
    );

    const pequeno_a = e.cadastrar_imovel(
        "Sitio Aconchego", 30.0, "Sertao do Sao Francisco", "caatinga",
        TipoTenencia.GUARDIAO_FAMILIAR, [UsoSolo.LAVOURA_ALIMENTACAO, UsoSolo.POMAR], 1,
        FuncaoSocialStatus.PARCIAL, 70.0, [PlanoAgrologia.COMPOSTAGEM, PlanoAgrologia.ROTACAO_CULTURAS]
    );

    const reserva = e.cadastrar_imovel(
        "Reserva Caatinga Viva", 800.0, "Sertao do Sao Francisco", "caatinga",
        TipoTenencia.RESERVA_REGENERACAO, [UsoSolo.RESERVA_NATIVA], 0,
        FuncaoSocialStatus.CUMPRE, 0.0, [PlanoAgrologia.CICLO_FECHADO]
    );

    const diag = e.diagnosticar("Sertao do Sao Francisco");
    console.log(`\n[DIAGNOSTICO] ${diag.territorio}`);
    console.log(`  Area total: ${diag.total_area.toFixed(0)} ha | Imoveis: ${diag.num_imoveis}`);
    console.log(`  Indice de Gini: ${diag.indice_gini.toFixed(3)} (0=igual, 1=concentrado)`);
    console.log(`  % area em latifundios: ${diag.pct_area_latifundio.toFixed(1)}%`);
    console.log(`  Familias guardias: ${diag.familias_guardias}`);
    console.log(`  VEREDITO: ${diag.veredito}`);

    console.log("\n[NOTIFICACAO]");
    const msg = e.notificar_latifundio(latif.id);
    console.log(`  ${msg}`);

    console.log("\n[AUDITORIA DE FUNCAO SOCIAL]");
    for (const iid of [latif.id, pequeno_a.id, reserva.id]) {
        const [status, faltas] = e.auditar_funcao_social(iid);
        const im = e.imoveis[iid];
        console.log(`  ${iid} (${im.nome.substring(0, 30)}): ${status.rotulo}`);
        for (const f of faltas) console.log(`      - ${f}`);
    }

    const conflito = e.registrar_conflito(
        TipoConflito.TRABALHO_ESCRAVO, latif.id, 2, 8,
        "Trabalhadores resgatados em condicoes analogas a escravidao."
    );
    console.log(`\n[CONFLITO REGISTRADO] ${conflito.id}: ${conflito.tipo.rotulo}`);
    console.log(`  Gravidade: ${conflito.tipo.gravidade}/5 | Familias afetadas: ${conflito.familias_afetadas}`);

    console.log("\n[DESAPROPRIACAO POR ASSEMBLEIA]");
    const fams = [
        e.cadastrar_familia("Familia Maria das Dores", 5, 0.0, null, "despejado", false),
        e.cadastrar_familia("Familia Jose Pereira", 4, 0.0, null, "despejado", false),
        e.cadastrar_familia("Familia Ana Beatriz", 6, 0.0, null, "voluntario", false),
        e.cadastrar_familia("Familia Severino", 5, 0.0, null, "despejado", true)
    ];
    const res = e.desaproropriar(latif.id, fams.map(f => f.id));
    console.log(`  ${res}`);

    e.resolver_conflito(conflito.id, "Ex-dono removido; familias guardias assumem; recuperacao das vitimas via OpenPsychologyReparation.");
    console.log(`  Conflito ${conflito.id} resolvido: ${conflito.resolucao_proposta}`);

    console.log("\n[CONSOLIDACAO COOPERATIVA]");
    const coop = e.consolidar_cooperativa(
        "Cooperativa Terra Livre Sertao", [latif.id], fams.map(f => f.id),
        "mercado_aberto", ["trator_compartilhado", "casa_de_farinha", "cisterna_coletiva"]
    );
    console.log(`  ${coop.id}: ${coop.nome}`);
    console.log(`  Familias: ${coop.familia_ids.length} | Territorios: ${coop.territorio_ids.length}`);
    console.log(`  Ferramentas compartilhadas: ${coop.ferramentas_compartilhadas.join(", ")}`);

    latif.usos_solo = [UsoSolo.AGROFLORESTA, UsoSolo.LAVOURA_DIVERSIFICADA, UsoSolo.POMAR];
    latif.plano_agrologia = [
        PlanoAgrologia.AGROFLORESTA_SUCSSIONAL, PlanoAgrologia.CAPTACAO_CHUVA,
        PlanoAgrologia.BIOINSUMOS, PlanoAgrologia.CICLO_FECHADO
    ];
    latif.produtividade_pct = 65.0;
    const [status_final] = e.auditar_funcao_social(latif.id);
    console.log(`\n[POS-REVOLUCAO] ${latif.id} funcao social: ${status_final.rotulo}`);
    console.log(`  Status: ${latif.status.rotulo} | Tenencia: ${latif.tipo_tenencia.rotulo}`);

    console.log("\n" + "=".repeat(70));
    console.log("[SCORECARD DA REVOLUCAO AGRARIA]");
    console.log("=".repeat(70));
    const sc = e.scorecard();
    for (const [k, v] of Object.entries(sc)) {
        console.log(`  ${k.padEnd(28, ".")} ${v}`);
    }

    console.log("\n[CONFLITOS POR GRAVIDADE]");
    for (const c of e.conflitos_por_gravidade()) {
        const flag = c.resolvido ? "OK" : "ABERTO";
        console.log(`  [${flag}] ${c.id} ${c.tipo.rotulo} (grav=${c.tipo.gravidade}) vitimas=${c.vitimas} familias=${c.familias_afetadas}`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("FILOSOFIA -- Por que a Republica ABOLI a propriedade da terra");
    console.log("=".repeat(70));
    console.log(`
P1 (Anti-elitismo): O latifundio e o mecanismo ORIGINAL de elite.
   Antes do banco, antes da empresa, antes da midia: a TERRA.
   Quem cerca a terra cerca a VIDA de quem precisa dela pra comer.
   Abolir a propriedade da terra = extirpar a raiz da desigualdade.

P2 (Autonomia): Quem planta colhe. Quem cuida decide.
   Ninguem morre de fome vigiando cerca de terra que nao cultiva.
   O corpo que sua na roca e dono do fruto -- nao de hectares.

P3 (Trabalho = impacto): "Dono de terra" nao e trabalho. E RENDA.
   Renda de propriedade e extrativismo puro: tirar sem botar.
   A Republica so reconhece credito por IMPACTO (alimentar gente).
   Latifundio improdutivo e roubo sistemico, nao "investimento".

P4 (Democracia): A assembleia do territorio decide o uso da terra.
   Nao ha "dono" para negociar as escuras com madeireira/mineradora.
   O guardiao tem MANDATO REVOGAVEL: abandona, devolve.
   Ninguem herda hectares. Herda-se o oficio, nao a propriedade.

A REVOLUCAO AGRARIA NAO E "REFORMA". E ABOLICAO.
Reforma distribui propriedade. Abolicao extingue a categoria.
A terra volta a ser o que sempre foi: CONDICAO DE VIDA,
nao ativo no balanco patrimonial de ninguem.
`);
}

if (require.main === module) {
    _demo();
}

module.exports = { ReformaAgrariaEngine, TipoTenencia, UsoSolo, StatusReforma, TipoConflito, TamanhoImovel, FuncaoSocialStatus, PlanoAgrologia };