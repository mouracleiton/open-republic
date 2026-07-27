// OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito Politico
// Author: OpenRepublic Team

const TipoIndicador = {
    USO_APARELHO_PUBLICO: { id: "uso_aparelho", rotulo: "Uso de aparelho de Estado para fim eleitoral", peso: 10 },
    COMPRA_VOTO: { id: "compra_voto", rotulo: "Compra de voto / clientelismo / bolsa-eleicao", peso: 10 },
    CONTINUIDADE_PODER: { id: "continuidade", rotulo: "Perpetuacao no poder (mandatos sucessivos)", peso: 8 },
    DESMANCHE_ALTERNATIVAS: { id: "desmanche", rotulo: "Desmanche de novas candidaturas no proprio campo", peso: 7 },
    CORRUPCAO_SISTEMICA: { id: "corrupcao", rotulo: "Corrupcao sistemica (padrao, nao caso isolado)", peso: 10 },
    MANIPULACAO_INFORMACAO: { id: "manipulacao_info", rotulo: "Manipulacao de informacao (bots, narrativa fabricada)", peso: 8 },
    OPACIDADE: { id: "opacidade", rotulo: "Falta de transparencia / esconda dados publicos", peso: 6 },
    PERSONALISMO: { id: "personalismo", rotulo: "Personalismo (se torna insubstituivel, sem sucessor)", peso: 7 },
    VIOLACAO_PRINCIPIOS: { id: "violacao_principios", rotulo: "Violacao de principios constitucionais", peso: 9 },
    MILITANCIA_FINANCEIRA: { id: "militancia_fin", rotulo: "Militancia comprada (cargo em troca de apoio)", peso: 7 },
    MIGALHA_DIGITAL: { id: "migalha_digital", rotulo: "Exercito de migalhas: militancia online paga com esmola digital", peso: 9 },
    MISERIA_DEPENDENCIA: { id: "miseria_dep", rotulo: "Miseria como ferramenta: manter na miseria para manter dependente", peso: 10 },
    PERSECUICAO_JUDICIAL: { id: "persecucao_judicial", rotulo: "Perseguicao judicial ilicita / preso politico em quarentena", peso: 9 },
};

const NivelConfiabilidade = {
    CONFIGAVEL: { id: "confiavel", rotulo: "Confiavel: sem indicadores graves, processo transparente", score_max: 100, score_min: 80 },
    ACEITAVEL: { id: "aceitavel", rotulo: "Aceitavel: indicadores leves, monitorar", score_max: 79, score_min: 60 },
    PREOCUPANTE: { id: "preocupante", rotulo: "Preocupante: multiplos indicadores, assembleia avalia", score_max: 59, score_min: 40 },
    ALTO_RISCO: { id: "alto_risco", rotulo: "Alto risco: padrao de manipulacao sistêmica", score_max: 39, score_min: 20 },
    INACEITAVEL: { id: "inaceitavel", rotulo: "Inaceitavel: processo corrompido, nao opera na Republica", score_max: 19, score_min: 0 },
};

const MetodoManipulacao = {
    BOTS_REDES: { id: "bots_redes", rotulo: "Bots e operacao de redes sociais" },
    APARELHO_ELEITORAL: { id: "aparelho_eleitoral", rotulo: "Maquina publica a servico de candidatura" },
    CLIENTELISMO: { id: "clientelismo", rotulo: "Troca de beneficio por voto" },
    CARGOS_TROCA: { id: "cargos_troca", rotulo: "Distribuicao de cargos em troca de apoio" },
    NARRATIVA_FABRICADA: { id: "narrativa_fabricada", rotulo: "Construcao de narrativa falsa" },
    IMPEDIR_CANDIDATURA: { id: "impedir_candidatura", rotulo: "Impedir surgimento de novas candidaturas" },
    JUDICIALIZACAO_ARMA: { id: "judicializacao_arma", rotulo: "Usar sistema judicial contra oponentes" },
    MIDIA_COMPRADA: { id: "midia_comprada", rotulo: "Comprar cobertura midiatica" },
    FINANCIAMENTO_OCULTO: { id: "financiamento_oculto", rotulo: "Caixa 2 / financiamento nao declarado" },
    MEDO_E_AMEACA: { id: "medo_ameaca", rotulo: "Gerar medo na populacao para colher votos" },
    MIGALHA_SOCIAL: { id: "migalha_social", rotulo: "Esmola digital/migalha em troca de militancia online" },
    PRESO_QUARENTENA: { id: "preso_quarentena", rotulo: "Manter oponente preso em quarentena judicial sem sentenca" },
    ARMADILHA_JUDICIAL: { id: "armadilha_judicial", rotulo: "Construir caso judicial com meios ilicitos" },
};

const GraveEvidencia = {
    COMPROVADO_JUDICIAL: { id: "comprovado_judicial", rotulo: "Comprovado judicialmente (sentenca transitada)", fator_confianca: 1.0 },
    INVESTIGACAO_OFICIAL: { id: "investigacao_oficial", rotulo: "Investigacao oficial em curso", fator_confianca: 0.7 },
    EVIDENCIA_JORNALISTICA: { id: "evidencia_jornalistica", rotulo: "Evidencia jornalistica consistente", fator_confianca: 0.6 },
    INDICIO_FORTE: { id: "indicio_forte", rotulo: "Indicio forte (multiplos sinais convergentes)", fator_confianca: 0.5 },
    DENUNCIA: { id: "denuncia", rotulo: "Denuncia formal sem comprovacao", fator_confianca: 0.3 },
    SUSPEITA: { id: "suspeita", rotulo: "Suspeita / opiniao publica sem comprovacao", fator_confianca: 0.1 },
};

const StatusVeredito = {
    APROVADO: { id: "aprovado", rotulo: "Sujeito pode operar na Republica" },
    MONITORAR: { id: "monitorar", rotulo: "Pode operar com monitoramento continuo" },
    RESTRITO: { id: "restrito", rotulo: "Operacao restrita (sem cargo de poder decisiorio)" },
    SUSPEITO: { id: "suspeito", rotulo: "Suspeito: assembleia decide caso a caso" },
    VETADO: { id: "vetado", rotulo: "Vetado: processo corrompido, nao exerce poder na Republica" },
};

class IndicadorPolitico {
    constructor(tipo, descricao, grauEvidencia, ocorrencias = 1, periodo = "", metodos = []) {
        this.tipo = tipo; this.descricao = descricao; this.grauEvidencia = grauEvidencia;
        this.ocorrencias = ocorrencias; this.periodo = periodo; this.metodos = metodos;
    }
}

class EventoPolitico {
    constructor(ano, descricao, tipo, impacto = 0, evidencia = GraveEvidencia.SUSPEITA) {
        this.ano = ano; this.descricao = descricao; this.tipo = tipo;
        this.impactoConfiabilidade = impacto; this.evidencia = evidencia;
    }
}

class ConfiabilidadeEngine {
    constructor() { this.eventos = []; this._evId = 0; }
    registrarEvento(ano, descricao, tipo, impacto = 0, evidencia = GraveEvidencia.SUSPEITA) {
        this._evId++;
        const ev = new EventoPolitico(ano, descricao, tipo, impacto, evidencia);
        ev.id = `EV-${String(this._evId).padStart(4, "0")}`;
        this.eventos.push(ev); return ev;
    }
    avaliar(sujeito, cargo, mandatos, indicadores, eventos = null) {
        let score = 100;
        const pontosFraco = []; const pontosForte = [];
        for (const ind of indicadores) {
            const penalidade = Math.min(ind.tipo.peso * ind.grauEvidencia.fator_confianca * Math.sqrt(ind.ocorrencias), 25);
            score -= penalidade;
            pontosFraco.push(`[${ind.tipo.rotulo}] ${ind.descricao} (evidencia: ${ind.grauEvidencia.rotulo}, ocorrencias: ${ind.ocorrencias})`);
        }
        if (mandatos >= 4) { score -= 10; pontosFraco.push(`Perpetuacao: ${mandatos} mandatos.`); }
        else if (mandatos >= 3) { score -= 5; pontosFraco.push(`Continuidade: ${mandatos} mandatos.`); }
        if (eventos) { for (const ev of eventos) {
            if (ev.impactoConfiabilidade < 0) { score += ev.impactoConfiabilidade; pontosFraco.push(`${ev.ano}: ${ev.descricao}`); }
            else if (ev.impactoConfiabilidade > 0) { score = Math.min(100, score + ev.impactoConfiabilidade); pontosForte.push(`${ev.ano}: ${ev.descricao}`); }
        } }
        score = Math.max(0, Math.min(100, Math.round(score)));
        const nivel = this._classificarNivel(score);
        const veredito = this._vereditoPorNivel(nivel);
        const recomendacoes = this._gerarRecomendacoes(indicadores, nivel, mandatos);
        return { sujeito, cargo, mandatos, score, nivel, veredito, indicadores, pontosFraco, pontosForte, recomendacoes };
    }
    _classificarNivel(score) {
        for (const n of Object.values(NivelConfiabilidade)) { if (score >= n.score_min && score <= n.score_max) return n; }
        return NivelConfiabilidade.INACEITAVEL;
    }
    _vereditoPorNivel(nivel) {
        if (nivel === NivelConfiabilidade.CONFIGAVEL) return StatusVeredito.APROVADO;
        if (nivel === NivelConfiabilidade.ACEITAVEL) return StatusVeredito.MONITORAR;
        if (nivel === NivelConfiabilidade.PREOCUPANTE) return StatusVeredito.RESTRITO;
        if (nivel === NivelConfiabilidade.ALTO_RISCO) return StatusVeredito.SUSPEITO;
        return StatusVeredito.VETADO;
    }
    _gerarRecomendacoes(indicadores, nivel, mandatos) {
        const recs = []; const tipos = new Set(indicadores.map(i => i.tipo.id));
        if (tipos.has("uso_aparelho")) recs.push("Auditar uso de recursos publicos em periodo eleitoral.");
        if (tipos.has("compra_voto")) recs.push("Implementar OpenVoteIntegrity.");
        if (tipos.has("manipulacao_info")) recs.push("Auditar bots (P9).");
        if (tipos.has("desmanche")) recs.push("Proteger pluralismo interno.");
        if (tipos.has("personalismo") || mandatos >= 3) recs.push("Exigir plano de successao.");
        if (tipos.has("corrupcao")) recs.push("Investigacao independente.");
        if (tipos.has("migalha_digital")) recs.push("Rastrear fluxo de pagamentos a militancia online.");
        if (tipos.has("miseria_dep")) recs.push("AUDITAR politica social: beneficio liberta ou amarra?");
        if (tipos.has("persecucao_judicial")) recs.push("AUDITAR sistema judicial: preso em quarentena = sequestro processual.");
        if (nivel === NivelConfiabilidade.ALTO_RISCO || nivel === NivelConfiabilidade.INACEITAVEL) {
            recs.push("VETAR exercicio de cargo com poder decisiorio.");
            recs.push("Assembleia avalia se SUJEITO ou SISTEMA esta corrompido.");
        }
        return recs;
    }
    simularCenarios(avaliacao) {
        const cenarios = []; const s = avaliacao.score;
        cenarios.push({ cenario: "Sujeito continua no poder", probabilidade: s < 40 ? 85 : s < 60 ? 60 : 25, acao: s < 60 ? "Limitar mandatos." : "Monitorar." });
        cenarios.push({ cenario: "Substituido por sucessor", probabilidade: avaliacao.mandatos >= 3 ? 70 : 40, acao: "Auditar a EQUIPE." });
        cenarios.push({ cenario: "Nova candidatura emerge", probabilidade: s < 40 ? 30 : 50, acao: "PROTEGER nova candidatura." });
        cenarios.push({ cenario: "Processo reestruturado", probabilidade: 100, acao: "Assembleia constituinte." });
        return cenarios;
    }
}

const e = new ConfiabilidadeEngine();
console.log("=".repeat(70));
console.log("OpenPoliticalReliability -- Simulacao de Confiabilidade");
console.log("=".repeat(70));

const indicadoresA = [
    new IndicadorPolitico(TipoIndicador.USO_APARELHO_PUBLICO, "Uso de aparelho de Estado para fim eleitoral", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.COMPRA_VOTO, "Compra de voto / clientelismo / bolsa-eleicao", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.CONTINUIDADE_PODER, "Perpetuacao no poder (mandatos sucessivos)", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.DESMANCHE_ALTERNATIVAS, "Desmanche de novas candidaturas no proprio campo", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.CORRUPCAO_SISTEMICA, "Corrupcao sistemica (padrao, nao caso isolado)", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.MANIPULACAO_INFORMACAO, "Manipulacao de informacao (bots, narrativa fabricada)", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.OPACIDADE, "Falta de transparencia / esconda dados publicos", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.PERSONALISMO, "Personalismo (se torna insubstituivel, sem sucessor)", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.VIOLACAO_PRINCIPIOS, "Violacao de principios constitucionais", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.MILITANCIA_FINANCEIRA, "Militancia comprada (cargo em troca de apoio)", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.MIGALHA_DIGITAL, "Exercito de migalhas: militancia online paga com esmola digital", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.MISERIA_DEPENDENCIA, "Miseria como ferramenta: manter na miseria para manter dependente", GraveEvidencia.INDICIO_FORTE, 2),
    new IndicadorPolitico(TipoIndicador.PERSECUICAO_JUDICIAL, "Perseguicao judicial ilicita / preso politico em quarentena", GraveEvidencia.INDICIO_FORTE, 2),
];

const eventosA = [
    e.registrarEvento("2005", "Mensalao", "investigacao", -8, GraveEvidencia.COMPROVADO_JUDICIAL),
    e.registrarEvento("2014", "Lava Jato", "investigacao", -8, GraveEvidencia.COMPROVADO_JUDICIAL),
];

const avalA = e.avaliar("O Operador", "Presidente", 4, indicadoresA, eventosA);
console.log(`\n[AVALIACAO] ${avalA.sujeito}`);
console.log(`  Score: ${avalA.score}/100`);
console.log(`  Nivel: ${avalA.nivel.rotulo}`);
console.log(`  Veredito: ${avalA.veredito.rotulo}`);
console.log(`  Indicadores: ${avalA.indicadores.length}`);
console.log(`  Recomendacoes: ${avalA.recomendacoes.length}`);
for (const r of avalA.recomendacoes) console.log(`    -> ${r}`);

console.log("\n[SIMULACAO DE CENARIOS]");
const cenarios = e.simularCenarios(avalA);
cenarios.forEach((c, i) => console.log(`  ${i+1}. ${c.cenario} (${c.probabilidade}%) -> ${c.acao}`));

const indicadoresB = [
    new IndicadorPolitico(TipoIndicador.MANIPULACAO_INFORMACAO, "Bots e odio.", GraveEvidencia.INVESTIGACAO_OFICIAL, 3),
    new IndicadorPolitico(TipoIndicador.VIOLACAO_PRINCIPIOS, "Ataques a instituicoes.", GraveEvidencia.COMPROVADO_JUDICIAL, 5),
    new IndicadorPolitico(TipoIndicador.CORRUPCAO_SISTEMICA, "Rachadinha.", GraveEvidencia.COMPROVADO_JUDICIAL, 3),
];
const avalB = e.avaliar("O Polarizador", "Presidente (extrema-direita)", 1, indicadoresB);
console.log(`\n[COMPARACAO] Operador: ${avalA.score} | Polarizador: ${avalB.score}`);
console.log("  A Republica NAO escolhe o menos pior. Escolhe o processo LIMPO.");

console.log("\n[FILOSOFIA]");
console.log("O sistema atual obriga a escolher entre menos pior.");
console.log("Esquerda que compra com bolsa vs Direita que compra com medo.");
console.log("Ambos corrompem. Ambos manipulam. Diferenca e de METODO, nao PRINCIPIO.");
console.log("Exercito de migalhas, miseria como estrategia, persecucao judicial.");
console.log("A pergunta certa: que PROCESSO merece confianca?");
console.log("Sujeito e temporario. Processo e permanente.");
