// Full JS (ES6) translation of open_anti_polarization.py (P9 Anti-Polarization)
// All enums, classes, engine methods, and _demo() faithfully reproduced.
// Comments and strings kept in Portuguese. Runnable with node.

const FatorPolarizacao = {
    RELIGIAO: { id: "religiao", rotulo: "Religiao / fe / espiritualidade" },
    ETNIA: { id: "etnia", rotulo: "Etnia / raca / origem" },
    REGIAO: { id: "regiao", rotulo: "Regiao / geografia (norte vs sul, urbano vs rural)" },
    CLASSE: { id: "classe", rotulo: "Classe / origem economica (heranca do sistema antigo)" },
    IDEOLOGIA: { id: "ideologia", rotulo: "Ideologia politica (heranca do sistema partidario)" },
    IDENTIDADE: { id: "identidade", rotulo: "Identidade de genero / sexual / expressao" },
    LINGUA: { id: "lingua", rotulo: "Lingua / idioma / dialeto" },
    IDADE: { id: "idade", rotulo: "Geracional (jovens vs velhos)" },
    ALGORITMO: { id: "algoritmo", rotulo: "Algoritmo de feed (captura narrativa externa)" },
    CULTURA: { id: "cultura", rotulo: "Cultura / costumes / tradicao" }
};

const NivelPolarizacao = {
    SAUDAVEL: { id: "saudavel", rotulo: "Saudavel: dissenso produtivo, confianca preservada", gravidade: 0 },
    BAIXO: { id: "baixo", rotulo: "Baixo: blocos incipientes, ainda deliberam", gravidade: 1 },
    MODERADO: { id: "moderado", rotulo: "Moderado: blocos claros, deliberacao degrada", gravidade: 2 },
    ALTO: { id: "alto", rotulo: "Alto: votacao tribal, confianca em queda", gravidade: 3 },
    CRITICO: { id: "critico", rotulo: "Critico: quase bloqueio assemblear", gravidade: 4 },
    RUPTURA: { id: "ruptura", rotulo: "Ruptura epistemica: realidades de fato separadas", gravidade: 5 }
};

const TaticaPolarizante = {
    OUTGROUP_DEHUMANIZATION: { id: "outgroup_dehumanization", rotulo: "Desumanizacao do outro lado", gravidade: 5 },
    FALSE_DICHOTOMY: { id: "false_dichotomy", rotulo: "Falsa dicotomia (ou nos ou eles)", gravidade: 4 },
    WHATABOUTISM: { id: "whataboutism", rotulo: "Whataboutism (desvia com 'mas eles tambem')", gravidade: 3 },
    FEAR_MONGERING: { id: "fear_mongering", rotulo: "Alarmismo / medo fabricado", gravidade: 4 },
    IDENTITY_BAITING: { id: "identity_baiting", rotulo: "Isca de identidade (forca tribalismo)", gravidade: 5 },
    EPISTEMIC_BALKANIZATION: { id: "epistemic_balkanization", rotulo: "Balkanizacao epistemica (fatos tribais)", gravidade: 5 },
    BOTH_SIDES_FALLACY: { id: "both_sides_fallacy", rotulo: "Falsa simetria (os dois lados sao iguais)", gravidade: 3 },
    STRAWMAN: { id: "strawman", rotulo: "Espantalho (deturpa para atacar)", gravidade: 2 },
    DOG_WHISTLE: { id: "dog_whistle", rotulo: "Dog whistle (codigo tribal implicito)", gravidade: 4 },
    VIRTUE_SIGNALING: { id: "virtue_signaling", rotulo: "Sinalizacao virtuosa (pertence vs exclui)", gravidade: 2 }
};

const StatusBloqueio = {
    NENHUM: { id: "nenhum", rotulo: "Nenhum: assembleia delibera normalmente", prioridade: 0 },
    ALERTA: { id: "alerta", rotulo: "Alerta: moderador sinaliza polarizacao", prioridade: 1 },
    DELIBERACAO_ESTRUTURADA: { id: "deliberacao_estruturada", rotulo: "Deliberacao estruturada obrigatoria", prioridade: 2 },
    MEDIACAO_OBRIGATORIA: { id: "mediacao_obrigatoria", rotulo: "Mediacao obrigatoria antes de votar", prioridade: 3 },
    SUSPENDER_VOTACAO: { id: "suspender_votacao", rotulo: "Votacao suspensa (bloqueio ativo)", prioridade: 4 },
    ASSEMBLEIA_PAUSA: { id: "assembleia_pausa", rotulo: "Pausa assemblear (resfriamento obrigatorio)", prioridade: 5 }
};

const VereditoAuditoria = {
    APROVADA: { id: "aprovada", rotulo: "Politica aprovada: baixo potencial polarizante" },
    APROVADA_COM_RESSALVAS: { id: "ressalvas", rotulo: "Aprovada com ressalvas (mitigacoes exigidas)" },
    REJEITADA: { id: "rejeitada", rotulo: "Politica rejeitada: potencial polarizante alto" },
    BLOQUEADA: { id: "bloqueada", rotulo: "Politica bloqueada: e vetor de divisao identitaria" }
};

class VotoCidadao {
    constructor(cidadao_id, proposta_id, a_favor, justificativa = "") {
        this.cidadao_id = cidadao_id;
        this.proposta_id = proposta_id;
        this.a_favor = a_favor;
        this.justificativa = justificativa;
    }
}

class PropostaAssembleia {
    constructor(id, titulo, descricao = "", fator_aparente = null) {
        this.id = id;
        this.titulo = titulo;
        this.descricao = descricao;
        this.fator_aparente = fator_aparente;
        this.votacao_encerrada = false;
    }
}

class BlocoVotante {
    constructor(id, membros = [], coesao = 0.0) {
        this.id = id;
        this.membros = membros;
        this.coesao = coesao;
        this.fator_dominante = null;
    }
}

class MetricaPolarizacao {
    constructor(assembleia_id, num_cidadaos, num_blocos, indice_divisao, indice_tribalismo,
                indice_ruptura_epistemica, nivel, veredito) {
        this.assembleia_id = assembleia_id;
        this.num_cidadaos = num_cidadaos;
        this.num_blocos = num_blocos;
        this.indice_divisao = indice_divisao;
        this.indice_tribalismo = indice_tribalismo;
        this.indice_ruptura_epistemica = indice_ruptura_epistemica;
        this.nivel = nivel;
        this.veredito = veredito;
    }
}

class AuditoriaPolitica {
    constructor(politica_id, veredito, taticas_detectadas = [], fatores_acionados = [],
                score_polarizante = 0.0, mitigacoes = [], justificativa = "") {
        this.politica_id = politica_id;
        this.veredito = veredito;
        this.taticas_detectadas = taticas_detectadas;
        this.fatores_acionados = fatores_acionados;
        this.score_polarizante = score_polarizante;
        this.mitigacoes = mitigacoes;
        this.justificativa = justificativa;
    }
}

const SINAIS_RUPTURA_EPISTEMICA = {
    "fontes_exclusivas": "Cada bloco cita fontes que o outro bloco considera falsas por principio",
    "vocabulario_incomum": "Cada bloco usa vocabulario que o outro nao entende ou rejeita",
    "desumanizacao": "Membros de um bloco descrevem o outro como inimigo, nao como cidadao",
    "voto_identidade": "Voto decidido por identidade tribal, nao por merito da proposta",
    "zero_trust": "Nenhuma afirmacao do outro lado e aceita mesmo quando factualmente correto",
    "purity_test": "Membros sao punidos por reconhecer merito em argumento do outro lado",
    "conspiracy_default": "Derrota politica e automaticamente atribuida a conspiracao",
    "violencia_normalizada": "Violencia contra o outro bloco e tratada como legitima"
};

class AntiPolarizacaoEngine {
    constructor() {
        this.propostas = {};
        this.votos = [];
        this.blocos = {};
        this.auditorias = {};
        this._prop_id = 0;
        this._bloco_id = 0;
    }

    _prop_id_novo() {
        this._prop_id++;
        return `PROP-${String(this._prop_id).padStart(4, '0')}`;
    }

    _bloco_id_novo() {
        this._bloco_id++;
        return `BLOCO-${String(this._bloco_id).padStart(4, '0')}`;
    }

    registrar_proposta(titulo, descricao = "", fator_aparente = null) {
        const p = new PropostaAssembleia(this._prop_id_novo(), titulo, descricao, fator_aparente);
        this.propostas[p.id] = p;
        return p;
    }

    registrar_voto(cidadao_id, proposta_id, a_favor, justificativa = "") {
        const v = new VotoCidadao(cidadao_id, proposta_id, a_favor, justificativa);
        this.votos.push(v);
        return v;
    }

    registrar_votacao_em_lote(votacoes) {
        for (const [cid, pid, fav] of votacoes) {
            this.registrar_voto(cid, pid, fav);
        }
    }

    encerrar_proposta(proposta_id) {
        if (this.propostas[proposta_id]) {
            this.propostas[proposta_id].votacao_encerrada = true;
        }
    }

    detectar_blocos(num_propostas_min = 3) {
        this.blocos = {};
        const assinaturas = {};
        const prop_ids_ordenadas = Object.keys(this.propostas).sort();

        for (const pid of prop_ids_ordenadas) {
            const votos_prop = {};
            for (const v of this.votos) {
                if (v.proposta_id === pid) votos_prop[v.cidadao_id] = v.a_favor;
            }
            for (const [cid, fav] of Object.entries(votos_prop)) {
                if (!assinaturas[cid]) assinaturas[cid] = [];
                assinaturas[cid].push(fav);
            }
        }

        const cidadaos_validos = {};
        for (const [c, s] of Object.entries(assinaturas)) {
            if (s.length >= num_propostas_min) cidadaos_validos[c] = s;
        }
        if (Object.keys(cidadaos_validos).length === 0) return [];

        const grupos = {};
        for (const [cid, sig] of Object.entries(cidadaos_validos)) {
            const key = JSON.stringify(sig);
            if (!grupos[key]) grupos[key] = [];
            grupos[key].push(cid);
        }

        const blocos_criados = [];
        for (const [key, membros] of Object.entries(grupos)) {
            if (membros.length >= 2) {
                const b = new BlocoVotante(this._bloco_id_novo(), membros, 1.0);
                this.blocos[b.id] = b;
                blocos_criados.push(b);
            }
        }

        if (blocos_criados.length === 2) {
            const tamanhos = blocos_criados.map(b => b.membros.length).sort((a, b) => a - b);
            const razao = tamanhos[1] ? tamanhos[0] / tamanhos[1] : 0;
            if (razao >= 0.4) {
                blocos_criados[0].fator_dominante = FatorPolarizacao.IDEOLOGIA;
                blocos_criados[1].fator_dominante = FatorPolarizacao.IDEOLOGIA;
            }
        }
        return blocos_criados;
    }

    indice_divisao() {
        if (Object.keys(this.propostas).length === 0) return 0.0;
        const prop_ids = Object.keys(this.propostas).sort();
        let soma = 0.0;
        let count = 0;
        for (const pid of prop_ids) {
            const votos_prop = this.votos.filter(v => v.proposta_id === pid).map(v => v.a_favor);
            if (votos_prop.length === 0) continue;
            const favor = votos_prop.filter(x => x).length;
            const contra = votos_prop.length - favor;
            const total = votos_prop.length;
            const d = 1.0 - Math.abs(favor - contra) / total;
            soma += d;
            count++;
        }
        return count ? Math.round((soma / count) * 1000) / 1000 : 0.0;
    }

    indice_tribalismo() {
        const blocos = this.detectar_blocos();
        if (blocos.length === 0) return 0.0;
        const cids_em_blocos = new Set();
        for (const b of blocos) b.membros.forEach(m => cids_em_blocos.add(m));
        const votos_tribais = this.votos.filter(v => cids_em_blocos.has(v.cidadao_id)).length;
        const total_votos = this.votos.length;
        return total_votos ? Math.round((votos_tribais / total_votos) * 1000) / 1000 : 0.0;
    }

    indice_ruptura_epistemica(sinais_observados = []) {
        if (!sinais_observados || sinais_observados.length === 0) return 0.0;
        const validos = sinais_observados.filter(s => s in SINAIS_RUPTURA_EPISTEMICA).length;
        return Math.round((validos / Object.keys(SINAIS_RUPTURA_EPISTEMICA).length) * 1000) / 1000;
    }

    classificar_nivel(sinais_observados = null) {
        const div = this.indice_divisao();
        const trib = this.indice_tribalismo();
        const rupt = this.indice_ruptura_epistemica(sinais_observados || []);
        if (rupt >= 0.5) return NivelPolarizacao.RUPTURA;
        if (div >= 0.8 && trib >= 0.7) return NivelPolarizacao.CRITICO;
        if (div >= 0.6 && trib >= 0.5) return NivelPolarizacao.ALTO;
        if (div >= 0.4) return NivelPolarizacao.MODERADO;
        if (div >= 0.2) return NivelPolarizacao.BAIXO;
        return NivelPolarizacao.SAUDAVEL;
    }

    medir_polarizacao(assembleia_id = "default", sinais_observados = null) {
        const blocos = this.detectar_blocos();
        const div = this.indice_divisao();
        const trib = this.indice_tribalismo();
        const rupt = this.indice_ruptura_epistemica(sinais_observados || []);
        const nivel = this.classificar_nivel(sinais_observados);
        const cidadaos_unicos = new Set(this.votos.map(v => v.cidadao_id));

        let veredito;
        if (nivel === NivelPolarizacao.RUPTURA) {
            veredito = "RUPTURA EPISTEMICA: realidades de fato separadas. Assembleia nao pode deliberar ate restaurar chao de fato compartilhado.";
        } else if (nivel === NivelPolarizacao.CRITICO) {
            veredito = "CRITICO: votacao tribal dominante. Mediacao obrigatoria antes de qualquer nova votacao.";
        } else if (nivel === NivelPolarizacao.ALTO) {
            veredito = "ALTO: confianca em queda. Deliberacao estruturada exigida.";
        } else if (nivel === NivelPolarizacao.MODERADO) {
            veredito = "MODERADO: blocos claros. Monitorar e facilitar dialogo.";
        } else if (nivel === NivelPolarizacao.BAIXO) {
            veredito = "BAIXO: dissenso saudavel com sinal de alinhamento tribal incipiente.";
        } else {
            veredito = "SAUDAVEL: dissenso produtivo, confianca preservada.";
        }

        return new MetricaPolarizacao(assembleia_id, cidadaos_unicos.size, blocos.length, div, trib, rupt, nivel, veredito);
    }

    auditar_politica(politica_id, titulo, descricao, taticas_detectadas = [], fatores_acionados = [], sinais_ruptura = null) {
        const taticas = taticas_detectadas || [];
        const fatores = fatores_acionados || [];

        let score_taticas = Math.min(100.0, taticas.reduce((sum, t) => sum + t.gravidade * 12, 0));
        const fatores_identitarios = new Set([FatorPolarizacao.RELIGIAO, FatorPolarizacao.ETNIA, FatorPolarizacao.IDENTIDADE, FatorPolarizacao.CULTURA]);
        const penalidade_fator = fatores.reduce((sum, f) => sum + (fatores_identitarios.has(f) ? 8 : 4), 0);
        let score = Math.min(100.0, score_taticas + penalidade_fator);

        if (sinais_ruptura && sinais_ruptura.length > 0) {
            const rupt = this.indice_ruptura_epistemica(sinais_ruptura);
            score = Math.min(100.0, score + rupt * 30);
        }

        const mitigacoes = [];
        if (taticas.includes(TaticaPolarizante.OUTGROUP_DEHUMANIZATION))
            mitigacoes.push("Remover linguagem que desumaniza cidadaos do outro lado.");
        if (taticas.includes(TaticaPolarizante.FALSE_DICHOTOMY))
            mitigacoes.push("Apresentar 3+ opcoes, nao binomio nos-vs-eles.");
        if (taticas.includes(TaticaPolarizante.FEAR_MONGERING))
            mitigacoes.push("Substituir alarmismo por dados verificaveis e calmos.");
        if (taticas.includes(TaticaPolarizante.IDENTITY_BAITING))
            mitigacoes.push("Desacoplar a politica de identidade tribal (P9: Estado nao polariza).");
        if (taticas.includes(TaticaPolarizante.EPISTEMIC_BALKANIZATION))
            mitigacoes.push("Citar fontes reconhecidas por AMBOS os blocos (chao de fato compartilhado).");
        if (fatores.some(f => fatores_identitarios.has(f)))
            mitigacoes.push("Reescrever sem apelar a divisao identitaria (religiao/etnia/identidade).");
        if (score >= 40 && score < 70)
            mitigacoes.push("Submeter a deliberacao estruturada antes da votacao.");
        if (score >= 70)
            mitigacoes.push("Politica deve ser fundamentalmente reformulada.");

        let veredito, justif;
        if (score >= 75) {
            veredito = VereditoAuditoria.BLOQUEADA;
            justif = "P9 VIOLADO: a politica e vetor de divisao identitaria. Reescrever do zero sem acionar tribo.";
        } else if (score >= 50) {
            veredito = VereditoAuditoria.REJEITADA;
            justif = "Potencial polarizante alto. Rejeitada ate mitigacoes aplicadas.";
        } else if (score >= 25) {
            veredito = VereditoAuditoria.APROVADA_COM_RESSALVAS;
            justif = "Aprovada condicionalmente. Mitigacoes exigidas antes da votacao.";
        } else {
            veredito = VereditoAuditoria.APROVADA;
            justif = "Baixo potencial polarizante. Livre para votacao.";
        }

        const aud = new AuditoriaPolitica(politica_id, veredito, taticas, fatores, Math.round(score * 10) / 10, mitigacoes, justif);
        this.auditorias[politica_id] = aud;
        return aud;
    }

    protocolo_bloqueio(metrica) {
        if (metrica.nivel === NivelPolarizacao.RUPTURA) return StatusBloqueio.ASSEMBLEIA_PAUSA;
        if (metrica.nivel === NivelPolarizacao.CRITICO) return StatusBloqueio.SUSPENDER_VOTACAO;
        if (metrica.nivel === NivelPolarizacao.ALTO) return StatusBloqueio.MEDIACAO_OBRIGATORIA;
        if (metrica.nivel === NivelPolarizacao.MODERADO) return StatusBloqueio.DELIBERACAO_ESTRUTURADA;
        if (metrica.nivel === NivelPolarizacao.BAIXO) return StatusBloqueio.ALERTA;
        return StatusBloqueio.NENHUM;
    }

    recomendacoes_mediacao(metrica) {
        const recs = [];
        const n = metrica.nivel;
        if (n === NivelPolarizacao.SAUDAVEL) {
            recs.push("Manter: dissenso produtivo e saudavel (P2).");
            return recs;
        }
        if (n === NivelPolarizacao.BAIXO || n === NivelPolarizacao.MODERADO) {
            recs.push("Facilitar dialogo estruturado entre blocos (nao debate livre -- agrava).");
            recs.push("Identificar o chao de fato compartilhado antes de divergir.");
            recs.push("Rotular taticas polarizantes quando aparecerem (metacognicao assemblear).");
        }
        if (n === NivelPolarizacao.ALTO || n === NivelPolarizacao.CRITICO) {
            recs.push("Mediador profissional obrigatoria (OpenCommunityLeaders).");
            recs.push("Votacao adiada ate confianca minima restaurada.");
            recs.push("Deliberacao em sub-grupos mistos (quebra de bloco tribal).");
            recs.push("Auditar algoritmos de feed que podem estar amplificando (P8).");
        }
        if (n === NivelPolarizacao.RUPTURA) {
            recs.push("EMERGENCIA: assembleia em pausa. Nao votar.");
            recs.push("Restaurar chao de fato: comissao de verificacao (HumanKnowledge).");
            recs.push("Dialogo individual antes de coletivo (quebra de tribalismo).");
            recs.push("Investigar captura narrativa externa (algoritmo, ator malicioso).");
            recs.push("Considerar OpenWololo se a divisao for irreparavel (separar, nao subjugar).");
        }
        return recs;
    }

    scorecard() {
        const blocos = this.detectar_blocos();
        const bloqueadas = Object.values(this.auditorias).filter(a => a.veredito === VereditoAuditoria.BLOQUEADA).length;
        const aprovadas = Object.values(this.auditorias).filter(a =>
            a.veredito === VereditoAuditoria.APROVADA || a.veredito === VereditoAuditoria.APROVADA_COM_RESSALVAS).length;
        return {
            "propostas_registradas": Object.keys(this.propostas).length,
            "votos_registrados": this.votos.length,
            "cidadaos_ativos": new Set(this.votos.map(v => v.cidadao_id)).size,
            "blocos_detectados": blocos.length,
            "indice_divisao": this.indice_divisao(),
            "indice_tribalismo": this.indice_tribalismo(),
            "politicas_auditadas": Object.keys(this.auditorias).length,
            "politicas_bloqueadas": bloqueadas,
            "politicas_aprovadas": aprovadas
        };
    }
}

function _demo() {
    const e = new AntiPolarizacaoEngine();

    console.log("=".repeat(70));
    console.log("OpenAntiPolarization -- P9: O Estado NAO Polariza");
    console.log("=".repeat(70));

    // Cenario 1
    console.log("\n[CENARIO 1] Assembleia saudavel (dissenso produtivo)");
    const p1 = e.registrar_proposta("Construir escola no norte", "", FatorPolarizacao.REGIAO);
    const p2 = e.registrar_proposta("Ampliar enfermaria central");
    const p3 = e.registrar_proposta("Importar capoeira como educacao fisica");
    e.registrar_votacao_em_lote([
        ["cid_01", p1.id, true], ["cid_02", p1.id, true], ["cid_03", p1.id, false],
        ["cid_04", p1.id, true], ["cid_05", p1.id, true],
        ["cid_01", p2.id, true], ["cid_02", p2.id, false], ["cid_03", p2.id, true],
        ["cid_04", p2.id, true], ["cid_05", p2.id, true],
        ["cid_01", p3.id, false], ["cid_02", p3.id, true], ["cid_03", p3.id, true],
        ["cid_04", p3.id, false], ["cid_05", p3.id, true]
    ]);
    const m1 = e.medir_polarizacao("assembleia_norte_v1");
    console.log(`  Divisao: ${m1.indice_divisao.toFixed(2)} | Tribalismo: ${m1.indice_tribalismo.toFixed(2)}`);
    console.log(`  Nivel: ${m1.nivel.rotulo}`);
    console.log(`  Veredito: ${m1.veredito}`);
    console.log(`  Protocolo: ${e.protocolo_bloqueio(m1).rotulo}`);

    // Cenario 2
    console.log("\n[CENARIO 2] Assembleia polarizada (votacao tribal)");
    const e2 = new AntiPolarizacaoEngine();
    const pa = e2.registrar_proposta("Politica A", "", FatorPolarizacao.IDEOLOGIA);
    const pb = e2.registrar_proposta("Politica B", "", FatorPolarizacao.IDEOLOGIA);
    const pc = e2.registrar_proposta("Politica C", "", FatorPolarizacao.IDEOLOGIA);
    const pd = e2.registrar_proposta("Politica D", "", FatorPolarizacao.IDEOLOGIA);
    const bloco_x = Array.from({ length: 5 }, (_, i) => `x_${String(i).padStart(2, '0')}`);
    const bloco_y = Array.from({ length: 5 }, (_, i) => `y_${String(i).padStart(2, '0')}`);
    for (const prop of [pa, pb, pc, pd]) {
        for (const cid of bloco_x) e2.registrar_voto(cid, prop.id, true);
        for (const cid of bloco_y) e2.registrar_voto(cid, prop.id, false);
    }
    const m2 = e2.medir_polarizacao("assembleia_polarizada", ["voto_identidade", "zero_trust"]);
    console.log(`  Divisao: ${m2.indice_divisao.toFixed(2)} | Tribalismo: ${m2.indice_tribalismo.toFixed(2)}`);
    console.log(`  Ruptura epistemica: ${m2.indice_ruptura_epistemica.toFixed(2)}`);
    console.log(`  Nivel: ${m2.nivel.rotulo}`);
    console.log(`  Veredito: ${m2.veredito}`);
    console.log(`  Protocolo: ${e2.protocolo_bloqueio(m2).rotulo}`);
    console.log(`  Blocos detectados: ${m2.num_blocos}`);
    console.log("  Recomendacoes:");
    for (const r of e2.recomendacoes_mediacao(m2)) console.log(`    - ${r}`);

    // Cenario 3
    console.log("\n[CENARIO 3] Ruptura epistemica (EMERGENCIA)");
    const e3 = new AntiPolarizacaoEngine();
    for (let i = 0; i < 5; i++) e3.registrar_proposta(`Proposta ${i}`);
    const todos_sinais = Object.keys(SINAIS_RUPTURA_EPISTEMICA);
    for (const prop of Object.values(e3.propostas)) {
        for (let j = 0; j < 6; j++) {
            e3.registrar_voto(`tribo_a_${j}`, prop.id, true);
            e3.registrar_voto(`tribo_b_${j}`, prop.id, false);
        }
    }
    const m3 = e3.medir_polarizacao("assembleia_ruptura", todos_sinais);
    console.log(`  Ruptura epistemica: ${m3.indice_ruptura_epistemica.toFixed(2)}`);
    console.log(`  Nivel: ${m3.nivel.rotulo}`);
    console.log(`  Protocolo: ${e3.protocolo_bloqueio(m3).rotulo}`);
    console.log("  RECOMENDACOES DE EMERGENCIA:");
    for (const r of e3.recomendacoes_mediacao(m3)) console.log(`    - ${r}`);

    // GATE P9
    console.log("\n" + "=".repeat(70));
    console.log("[GATE P9] Auditoria de politicas publicas");
    console.log("=".repeat(70));

    const a1 = e.auditar_politica("pol-escola", "Construir escola no norte",
        "Politica de infraestrutura educacional sem apelo identitario.",
        [], [FatorPolarizacao.REGIAO]);
    console.log(`\n  [${a1.politica_id}] ${a1.veredito.rotulo} (score=${a1.score_polarizante})`);
    console.log(`    ${a1.justificativa}`);

    const a2 = e.auditar_politica("pol-saude", "Reforma do sistema de saude",
        "Politica com algum alarmismo na apresentacao.",
        [TaticaPolarizante.FEAR_MONGERING], []);
    console.log(`\n  [${a2.politica_id}] ${a2.veredito.rotulo} (score=${a2.score_polarizante})`);
    console.log(`    ${a2.justificativa}`);
    for (const mit of a2.mitigacoes) console.log(`    Mitigacao: ${mit}`);

    const a3 = e.auditar_politica("pol-seguranca", "Lei de seguranca publica",
        "Politica apresentada com falsa dicotomia e alarmismo.",
        [TaticaPolarizante.FALSE_DICHOTOMY, TaticaPolarizante.FEAR_MONGERING], [FatorPolarizacao.IDEOLOGIA]);
    console.log(`\n  [${a3.politica_id}] ${a3.veredito.rotulo} (score=${a3.score_polarizante})`);
    console.log(`    ${a3.justificativa}`);
    for (const mit of a3.mitigacoes) console.log(`    Mitigacao: ${mit}`);

    const a4 = e.auditar_politica("pol-identidade", "Declaracao sobre valores culturais",
        "Politica que aciona divisao religiosa e identitaria explicita.",
        [TaticaPolarizante.IDENTITY_BAITING, TaticaPolarizante.OUTGROUP_DEHUMANIZATION, TaticaPolarizante.EPISTEMIC_BALKANIZATION],
        [FatorPolarizacao.RELIGIAO, FatorPolarizacao.IDENTIDADE],
        ["zero_trust", "purity_test"]);
    console.log(`\n  [${a4.politica_id}] ${a4.veredito.rotulo} (score=${a4.score_polarizante})`);
    console.log(`    ${a4.justificativa}`);
    for (const mit of a4.mitigacoes) console.log(`    Mitigacao: ${mit}`);

    // Scorecard
    console.log("\n" + "=".repeat(70));
    console.log("[SCORECARD P9]");
    console.log("=".repeat(70));
    const sc = e.scorecard();
    for (const [k, v] of Object.entries(sc)) {
        console.log(`  ${k.padEnd(28, ".")} ${v}`);
    }

    // Catalogo
    console.log("\n[CATALOGO DE TATICAS POLARIZANTES AUDITADAS PELO ESTADO]");
    for (const t of Object.values(TaticaPolarizante)) {
        console.log(`  [${t.gravidade}] ${t.rotulo}`);
    }

    // Sinais
    console.log("\n[SINAIS DE RUPTURA EPISTEMICA (monitoramento continuo)]");
    for (const [chave, desc] of Object.entries(SINAIS_RUPTURA_EPISTEMICA)) {
        console.log(`  ${chave}: ${desc}`);
    }

    // Filosofia
    console.log("\n" + "=".repeat(70));
    console.log("FILOSOFIA -- P9: Por que o Estado nao pode polarizar");
    console.log("=".repeat(70));
    console.log(`DISTINCAO FUNDAMENTAL:
  Diversidade de opiniao e DIREITO (P2). E saudavel. E combustivel da democracia.
  Polarizacao e DOENCA. Nao e "opiniao diferente". E realidade epistemica
  separada: duas tribos que nao so discordam, mas habitam mundos de fato
  diferentes, com zero confianca mutua e identidade fundida na tribo.

O ERRO LIBERAL:
  O liberalismo assume que "mais debate resolve polarizacao". Falso.
  Mais debate entre tribos epistemicamente separadas AMPLIFICA a polarizacao.
  O que resolve: (a) chao de fato compartilhado, (b) deliberacao estruturada,
  (c) Estado que se recusa a ser vetor de divisao identitaria.

POR QUE O ESTADO ESPECIFICAMENTE:
  O Estado tem monopolio da forca coercitiva. Se o Estado polariza, ele nao
  so reflete a divisao -- ele a INSTITUCIONALIZA. Politica publica que aciona
  tribo vira lei. Lei que aciona tribo perpertua a divisao por geracoes.
  P9 e a proibicao constitucional de o Estado ser vetor de divisao.

P9 NAO E CENSURA:
  P9 nao proibe discurso (isso violaria P2). P9 obriga o ESTADO a auditar
  suas proprias politicas quanto ao efeito polarizante. E um gate, como WCAG
  audita acessibilidade. Cidadao pode dizer o que quiser. O Estado nao pode
  GOVERNAR com divisao identitaria.

A CONEXAO COM P8 (IA):
  Algoritmos de feed que otimizam engajamento amplificam furia, nao verdade.
  Isso e a anti-tese do P8 (IA que amplia inteligencia humana). Engagement
  por furia e captura narrativa. P9 exige que o Estado audite algoritmos
  que afetam a assembleia -- nao para censurar, mas para nao ser capturado.

A UNICA SAIDA QUANDO A DIVISAO E IRREPARAVEL:
  Se duas comunidades habitam realidades epistemicas irrecuperavelmente
  separadas, a Republica nao as obriga a coexistir sob a mesma lei (isso
  recriaria coercicao). OpenWololo permite separar com dignidade -- duas
  assembleias, dois territorios, zero subordinacao. Melhor separar do que
  subjugar. Mas P9 trabalha para que isso seja ultimo recurso, nao rotina.
`);
}

if (require.main === module) {
    _demo();
}
