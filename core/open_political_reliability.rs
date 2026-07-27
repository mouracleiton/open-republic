// OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito Politico
// =============================================================================
// "O poder nao se mede pela quantidade de votos, mas pela qualidade do processo."

// A Republica NAO confia em sujeitos politicos. Confia em PROCESSOS.
// Mas para AUDITAR processos, precisa avaliar a CONFIABILIDADE dos sujeitos
// que operam dentro deles.

// Este modulo e um SIMULADOR de confiabilidade politica. NAO e tribunal.
// NAO condena. AVALIA com base em indicadores verificaveis e produz um
// SCORE de confiabilidade que a assembleia pode usar para decidir se um
// sujeito pode operar dentro das instituicoes da Republica.

// PRINCIPIO (P4): A transparencia e radical. Se um sujeito opera no poder,
// todo seu historico e auditavel. Nao existe "privacidade politica" para
// quem exerce poder publico -- poder publico e PUBLICO.

// O QUE O SIMULADOR MEDE:
// 1. USO DE APARELHO PUBLICO para beneficio eleitoral
// 2. COMPRA DE VOTO (clientelismo, bolsa, promessa)
// 3. CONTINUIDADE NO PODER (quantos mandatos, indicio de perpetuacao)
// 4. DESMANCHE DE ALTERNATIVAS (impede novas candidaturas no proprio campo)
// 5. CORRUPCAO SISTEMICA (e caso isolado ou padrao?)
// 6. MANIPULACAO DE INFORMACAO (bots, redes, narrativa fabricada)
// 7. TRANSPARENCIA (abre dados ou esconde?)
// 8. RENOVACAO DE ELITES (treina sucessores ou se torna insubstituivel?)

// ALINHAMENTO CONSTITUCIONAL:
// - P1: Confianca politica nao heranca. Cada mandato auditado.
// - P4: Democracia radical exige sujeitos confiaveis. Processo corrompido = vitro eleitoral.
// - P9: Sujeito que polariza para perpetuar VIOLA o P9 (Estado nao polariza).

// Author: OpenRepublic Team (transpilado para Rust)

use std::collections::{HashMap, HashSet};
use std::fmt;

// ============================================================================
// 1. ENUMS (modulo-level)
// ============================================================================

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoIndicador {
    USO_APARELHO_PUBLICO,
    COMPRA_VOTO,
    CONTINUIDADE_PODER,
    DESMANCHE_ALTERNATIVAS,
    CORRUPCAO_SISTEMICA,
    MANIPULACAO_INFORMACAO,
    OPACIDADE,
    PERSONALISMO,
    VIOLACAO_PRINCIPIOS,
    MILITANCIA_FINANCEIRA,
}

impl TipoIndicador {
    pub fn id(&self) -> &'static str {
        match self {
            TipoIndicador::USO_APARELHO_PUBLICO => "uso_aparelho",
            TipoIndicador::COMPRA_VOTO => "compra_voto",
            TipoIndicador::CONTINUIDADE_PODER => "continuidade",
            TipoIndicador::DESMANCHE_ALTERNATIVAS => "desmanche",
            TipoIndicador::CORRUPCAO_SISTEMICA => "corrupcao",
            TipoIndicador::MANIPULACAO_INFORMACAO => "manipulacao_info",
            TipoIndicador::OPACIDADE => "opacidade",
            TipoIndicador::PERSONALISMO => "personalismo",
            TipoIndicador::VIOLACAO_PRINCIPIOS => "violacao_principios",
            TipoIndicador::MILITANCIA_FINANCEIRA => "militancia_fin",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoIndicador::USO_APARELHO_PUBLICO => "Uso de aparelho de Estado para fim eleitoral",
            TipoIndicador::COMPRA_VOTO => "Compra de voto / clientelismo / bolsa-eleicao",
            TipoIndicador::CONTINUIDADE_PODER => "Perpetuacao no poder (mandatos sucessivos)",
            TipoIndicador::DESMANCHE_ALTERNATIVAS => {
                "Desmanche de novas candidaturas no proprio campo"
            }
            TipoIndicador::CORRUPCAO_SISTEMICA => "Corrupcao sistemica (padrao, nao caso isolado)",
            TipoIndicador::MANIPULACAO_INFORMACAO => {
                "Manipulacao de informacao (bots, narrativa fabricada)"
            }
            TipoIndicador::OPACIDADE => "Falta de transparencia / esconda dados publicos",
            TipoIndicador::PERSONALISMO => "Personalismo (se torna insubstituivel, sem sucessor)",
            TipoIndicador::VIOLACAO_PRINCIPIOS => "Violacao de principios constitucionais",
            TipoIndicador::MILITANCIA_FINANCEIRA => "Militancia comprada (cargo em troca de apoio)",
        }
    }

    pub fn peso(&self) -> i32 {
        match self {
            TipoIndicador::USO_APARELHO_PUBLICO => 10,
            TipoIndicador::COMPRA_VOTO => 10,
            TipoIndicador::CONTINUIDADE_PODER => 8,
            TipoIndicador::DESMANCHE_ALTERNATIVAS => 7,
            TipoIndicador::CORRUPCAO_SISTEMICA => 10,
            TipoIndicador::MANIPULACAO_INFORMACAO => 8,
            TipoIndicador::OPACIDADE => 6,
            TipoIndicador::PERSONALISMO => 7,
            TipoIndicador::VIOLACAO_PRINCIPIOS => 9,
            TipoIndicador::MILITANCIA_FINANCEIRA => 7,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum NivelConfiabilidade {
    CONFIGAVEL,
    ACEITAVEL,
    PREOCUPANTE,
    ALTO_RISCO,
    INACEITAVEL,
}

impl NivelConfiabilidade {
    pub fn id(&self) -> &'static str {
        match self {
            NivelConfiabilidade::CONFIGAVEL => "confiavel",
            NivelConfiabilidade::ACEITAVEL => "aceitavel",
            NivelConfiabilidade::PREOCUPANTE => "preocupante",
            NivelConfiabilidade::ALTO_RISCO => "alto_risco",
            NivelConfiabilidade::INACEITAVEL => "inaceitavel",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            NivelConfiabilidade::CONFIGAVEL => {
                "Confiavel: sem indicadores graves, processo transparente"
            }
            NivelConfiabilidade::ACEITAVEL => "Aceitavel: indicadores leves, monitorar",
            NivelConfiabilidade::PREOCUPANTE => {
                "Preocupante: multiplos indicadores, assembleia avalia"
            }
            NivelConfiabilidade::ALTO_RISCO => "Alto risco: padrao de manipulacao sistemica",
            NivelConfiabilidade::INACEITAVEL => {
                "Inaceitavel: processo corrompido, nao opera na Republica"
            }
        }
    }

    pub fn score_max(&self) -> i32 {
        match self {
            NivelConfiabilidade::CONFIGAVEL => 100,
            NivelConfiabilidade::ACEITAVEL => 79,
            NivelConfiabilidade::PREOCUPANTE => 59,
            NivelConfiabilidade::ALTO_RISCO => 39,
            NivelConfiabilidade::INACEITAVEL => 19,
        }
    }

    pub fn score_min(&self) -> i32 {
        match self {
            NivelConfiabilidade::CONFIGAVEL => 80,
            NivelConfiabilidade::ACEITAVEL => 60,
            NivelConfiabilidade::PREOCUPANTE => 40,
            NivelConfiabilidade::ALTO_RISCO => 20,
            NivelConfiabilidade::INACEITAVEL => 0,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum MetodoManipulacao {
    BOTS_REDES,
    APARELHO_ELEITORAL,
    CLIENTELISMO,
    CARGOS_TROCA,
    NARRATIVA_FABRICADA,
    IMPEDIR_CANDIDATURA,
    JUDICIALIZACAO_ARMA,
    MIDIA_COMPRADA,
    FINANCIAMENTO_OCULTO,
    MEDO_E_AMEACA,
}

impl MetodoManipulacao {
    pub fn id(&self) -> &'static str {
        match self {
            MetodoManipulacao::BOTS_REDES => "bots_redes",
            MetodoManipulacao::APARELHO_ELEITORAL => "aparelho_eleitoral",
            MetodoManipulacao::CLIENTELISMO => "clientelismo",
            MetodoManipulacao::CARGOS_TROCA => "cargos_troca",
            MetodoManipulacao::NARRATIVA_FABRICADA => "narrativa_fabricada",
            MetodoManipulacao::IMPEDIR_CANDIDATURA => "impedir_candidatura",
            MetodoManipulacao::JUDICIALIZACAO_ARMA => "judicializacao_arma",
            MetodoManipulacao::MIDIA_COMPRADA => "midia_comprada",
            MetodoManipulacao::FINANCIAMENTO_OCULTO => "financiamento_oculto",
            MetodoManipulacao::MEDO_E_AMEACA => "medo_ameaca",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            MetodoManipulacao::BOTS_REDES => "Bots e operacao de redes sociais",
            MetodoManipulacao::APARELHO_ELEITORAL => "Maquina publica a servico de candidatura",
            MetodoManipulacao::CLIENTELISMO => "Troca de beneficio por voto",
            MetodoManipulacao::CARGOS_TROCA => "Distribuicao de cargos em troca de apoio",
            MetodoManipulacao::NARRATIVA_FABRICADA => "Construcao de narrativa falsa",
            MetodoManipulacao::IMPEDIR_CANDIDATURA => "Impedir surgimento de novas candidaturas",
            MetodoManipulacao::JUDICIALIZACAO_ARMA => "Usar sistema judicial contra oponentes",
            MetodoManipulacao::MIDIA_COMPRADA => "Comprar cobertura midiatica",
            MetodoManipulacao::FINANCIAMENTO_OCULTO => "Caixa 2 / financiamento nao declarado",
            MetodoManipulacao::MEDO_E_AMEACA => "Gerar medo na populacao para colher votos",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum GraveEvidencia {
    COMPROVADO_JUDICIAL,
    INVESTIGACAO_OFICIAL,
    EVIDENCIA_JORNALISTICA,
    INDICIO_FORTE,
    DENUNCIA,
    SUSPEITA,
}

impl GraveEvidencia {
    pub fn id(&self) -> &'static str {
        match self {
            GraveEvidencia::COMPROVADO_JUDICIAL => "comprovado_judicial",
            GraveEvidencia::INVESTIGACAO_OFICIAL => "investigacao_oficial",
            GraveEvidencia::EVIDENCIA_JORNALISTICA => "evidencia_jornalistica",
            GraveEvidencia::INDICIO_FORTE => "indicio_forte",
            GraveEvidencia::DENUNCIA => "denuncia",
            GraveEvidencia::SUSPEITA => "suspeita",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            GraveEvidencia::COMPROVADO_JUDICIAL => "Comprovado judicialmente (sentenca transitada)",
            GraveEvidencia::INVESTIGACAO_OFICIAL => "Investigacao oficial em curso",
            GraveEvidencia::EVIDENCIA_JORNALISTICA => "Evidencia jornalistica consistente",
            GraveEvidencia::INDICIO_FORTE => "Indicio forte (multiplos sinais convergentes)",
            GraveEvidencia::DENUNCIA => "Denuncia formal sem comprovacao",
            GraveEvidencia::SUSPEITA => "Suspeita / opiniao publica sem comprovacao",
        }
    }

    pub fn fator_confianca(&self) -> f64 {
        match self {
            GraveEvidencia::COMPROVADO_JUDICIAL => 1.0,
            GraveEvidencia::INVESTIGACAO_OFICIAL => 0.7,
            GraveEvidencia::EVIDENCIA_JORNALISTICA => 0.6,
            GraveEvidencia::INDICIO_FORTE => 0.5,
            GraveEvidencia::DENUNCIA => 0.3,
            GraveEvidencia::SUSPEITA => 0.1,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum StatusVeredito {
    APROVADO,
    MONITORAR,
    RESTRITO,
    SUSPEITO,
    VETADO,
}

impl StatusVeredito {
    pub fn id(&self) -> &'static str {
        match self {
            StatusVeredito::APROVADO => "aprovado",
            StatusVeredito::MONITORAR => "monitorar",
            StatusVeredito::RESTRITO => "restrito",
            StatusVeredito::SUSPEITO => "suspeito",
            StatusVeredito::VETADO => "vetado",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            StatusVeredito::APROVADO => "Sujeito pode operar na Republica",
            StatusVeredito::MONITORAR => "Pode operar com monitoramento continuo",
            StatusVeredito::RESTRITO => "Operacao restrita (sem cargo de poder decisiorio)",
            StatusVeredito::SUSPEITO => "Suspeito: assembleia decide caso a caso",
            StatusVeredito::VETADO => "Vetado: processo corrompido, nao exerce poder na Republica",
        }
    }
}

// ============================================================================
// 2. STRUCTS (dataclasses)
// ============================================================================

#[derive(Debug, Clone)]
pub struct IndicadorPolitico {
    pub tipo: TipoIndicador,
    pub descricao: String,
    pub grau_evidencia: GraveEvidencia,
    pub ocorrencias: i32,
    pub periodo: String,
    pub metodos: Vec<MetodoManipulacao>,
    pub detalhe: String,
}

#[derive(Debug, Clone)]
pub struct EventoPolitico {
    pub id: String,
    pub ano: String,
    pub descricao: String,
    pub tipo: String,
    pub impacto_confiabilidade: i32,
    pub evidencia: GraveEvidencia,
}

#[derive(Debug, Clone)]
pub struct AvaliacaoConfiabilidade {
    pub sujeito: String,
    pub cargo: String,
    pub mandatos: i32,
    pub score: i32,
    pub nivel: NivelConfiabilidade,
    pub veredito: StatusVeredito,
    pub indicadores: Vec<IndicadorPolitico>,
    pub pontos_forte: Vec<String>,
    pub pontos_fraco: Vec<String>,
    pub recomendacoes: Vec<String>,
    pub justificativa: String,
}

#[derive(Debug, Clone)]
pub struct SimulacaoCenario {
    pub cenario: String,
    pub probabilidade_pct: f64,
    pub impacto_democracia: String,
    pub impacto_republica: String,
    pub acao_recomendada: String,
}

// ============================================================================
// 3. ENGINE
// ============================================================================

pub struct ConfiabilidadeEngine {
    eventos: Vec<EventoPolitico>,
    ev_id: i32,
}

impl ConfiabilidadeEngine {
    pub fn new() -> Self {
        ConfiabilidadeEngine {
            eventos: Vec::new(),
            ev_id: 0,
        }
    }

    fn ev_novo_id(&mut self) -> String {
        self.ev_id += 1;
        format!("EV-{:04}", self.ev_id)
    }

    pub fn registrar_evento(
        &mut self,
        ano: &str,
        descricao: &str,
        tipo: &str,
        impacto: i32,
        evidencia: GraveEvidencia,
    ) -> EventoPolitico {
        let ev = EventoPolitico {
            id: self.ev_novo_id(),
            ano: ano.to_string(),
            descricao: descricao.to_string(),
            tipo: tipo.to_string(),
            impacto_confiabilidade: impacto,
            evidencia,
        };
        self.eventos.push(ev.clone());
        ev
    }

    pub fn avaliar(
        &mut self,
        sujeito: &str,
        cargo: &str,
        mandatos: i32,
        indicadores: Vec<IndicadorPolitico>,
        eventos: Option<Vec<EventoPolitico>>,
    ) -> AvaliacaoConfiabilidade {
        let mut score: f64 = 100.0;
        let mut pontos_fraco: Vec<String> = Vec::new();
        let mut pontos_forte: Vec<String> = Vec::new();

        for ind in &indicadores {
            let penalidade = (ind.tipo.peso() as f64)
                * ind.grau_evidencia.fator_confianca()
                * (ind.ocorrencias as f64).sqrt();
            let penalidade = penalidade.min(25.0);
            score -= penalidade;
            pontos_fraco.push(format!(
                "[{}] {} (evidencia: {}, ocorrencias: {})",
                ind.tipo.rotulo(),
                ind.descricao,
                ind.grau_evidencia.rotulo(),
                ind.ocorrencias
            ));
        }

        if mandatos >= 4 {
            score -= 10.0;
            pontos_fraco.push(format!(
                "Perpetuacao: {} mandatos (risco de insubstituibilidade).",
                mandatos
            ));
        } else if mandatos >= 3 {
            score -= 5.0;
            pontos_fraco.push(format!(
                "Continuidade: {} mandatos (monitorar renovacao).",
                mandatos
            ));
        }

        if let Some(evts) = &eventos {
            for ev in evts {
                if ev.impacto_confiabilidade < 0 {
                    score += ev.impacto_confiabilidade as f64;
                    pontos_fraco.push(format!(
                        "{}: {} ({})",
                        ev.ano,
                        ev.descricao,
                        ev.evidencia.rotulo()
                    ));
                } else if ev.impacto_confiabilidade > 0 {
                    score = score.min(100.0) + ev.impacto_confiabilidade as f64;
                    pontos_forte.push(format!("{}: {}", ev.ano, ev.descricao));
                }
            }
        }

        let score = (score.max(0.0).min(100.0)).round() as i32;

        let nivel = self.classificar_nivel(score);
        let veredito = self.veredito_por_nivel(&nivel, mandatos);
        let recomendacoes = self.gerar_recomendacoes(&indicadores, &nivel, mandatos);
        let justificativa =
            self.gerar_justificativa(sujeito, score, &nivel, &indicadores, mandatos);

        AvaliacaoConfiabilidade {
            sujeito: sujeito.to_string(),
            cargo: cargo.to_string(),
            mandatos,
            score,
            nivel,
            veredito,
            indicadores,
            pontos_forte,
            pontos_fraco,
            recomendacoes,
            justificativa,
        }
    }

    fn classificar_nivel(&self, score: i32) -> NivelConfiabilidade {
        for n in [
            NivelConfiabilidade::CONFIGAVEL,
            NivelConfiabilidade::ACEITAVEL,
            NivelConfiabilidade::PREOCUPANTE,
            NivelConfiabilidade::ALTO_RISCO,
            NivelConfiabilidade::INACEITAVEL,
        ] {
            if score >= n.score_min() && score <= n.score_max() {
                return n;
            }
        }
        NivelConfiabilidade::INACEITAVEL
    }

    fn veredito_por_nivel(&self, nivel: &NivelConfiabilidade, _mandatos: i32) -> StatusVeredito {
        match nivel {
            NivelConfiabilidade::CONFIGAVEL => StatusVeredito::APROVADO,
            NivelConfiabilidade::ACEITAVEL => StatusVeredito::MONITORAR,
            NivelConfiabilidade::PREOCUPANTE => StatusVeredito::RESTRITO,
            NivelConfiabilidade::ALTO_RISCO => StatusVeredito::SUSPEITO,
            NivelConfiabilidade::INACEITAVEL => StatusVeredito::VETADO,
        }
    }

    fn gerar_recomendacoes(
        &self,
        indicadores: &[IndicadorPolitico],
        nivel: &NivelConfiabilidade,
        mandatos: i32,
    ) -> Vec<String> {
        let mut recs: Vec<String> = Vec::new();
        let tipos_ativos: HashSet<_> = indicadores.iter().map(|i| &i.tipo).collect();

        if tipos_ativos.contains(&TipoIndicador::USO_APARELHO_PUBLICO) {
            recs.push(
                "Auditar uso de recursos publicos em periodo eleitoral (OpenPublicAudit)."
                    .to_string(),
            );
        }
        if tipos_ativos.contains(&TipoIndicador::COMPRA_VOTO) {
            recs.push(
                "Implementar OpenVoteIntegrity: rastrear fluxo de beneficios antes de eleicao."
                    .to_string(),
            );
        }
        if tipos_ativos.contains(&TipoIndicador::MANIPULACAO_INFORMACAO) {
            recs.push(
                "Auditar bots e operacao de redes (P9: Estado nao polariza via algoritmo)."
                    .to_string(),
            );
        }
        if tipos_ativos.contains(&TipoIndicador::DESMANCHE_ALTERNATIVAS) {
            recs.push(
                "Proteger pluralismo interno: assembleia garante direito a candidatura alternativa."
                    .to_string(),
            );
        }
        if tipos_ativos.contains(&TipoIndicador::PERSONALISMO) || mandatos >= 3 {
            recs.push(
                "Exigir plano de successao: sujeito treina substituto ou nao exerce novo mandato."
                    .to_string(),
            );
        }
        if tipos_ativos.contains(&TipoIndicador::CORRUPCAO_SISTEMICA) {
            recs.push(
                "Investigacao independente (OpenJudicialAudit) antes de qualquer integracao."
                    .to_string(),
            );
        }
        if *nivel == NivelConfiabilidade::ALTO_RISCO || *nivel == NivelConfiabilidade::INACEITAVEL {
            recs.push(
                "VETAR exercicio de cargo com poder decisiorio ate restaurar processo.".to_string(),
            );
            recs.push(
                "Assembleia avalia se o SUJEITO ou o SISTEMA esta corrompido (P4).".to_string(),
            );
        }
        recs
    }

    fn gerar_justificativa(
        &self,
        sujeito: &str,
        score: i32,
        nivel: &NivelConfiabilidade,
        indicadores: &[IndicadorPolitico],
        mandatos: i32,
    ) -> String {
        let count = indicadores.len();
        let graves = indicadores
            .iter()
            .filter(|i| i.grau_evidencia.fator_confianca() >= 0.5)
            .count();
        format!(
            "Sujeito '{}' avaliado com score {}/100 ({}). {} indicadores detectados, {} com evidencia forte ou superior. {} mandatos. Veredito baseado em indicadores verificaveis, nao em opiniao. A assembleia tem autoridade final (P4).",
            sujeito, score, nivel.rotulo(), count, graves, mandatos
        )
    }

    pub fn simular_cenarios(&self, avaliacao: &AvaliacaoConfiabilidade) -> Vec<SimulacaoCenario> {
        let mut cenarios: Vec<SimulacaoCenario> = Vec::new();
        let score = avaliacao.score;

        // Cenario 1
        let (prob, impacto_dem, impacto_rep, acao) = if score < 40 {
            (
                85.0,
                "Processo democratico degenerado: voto e transacao, nao deliberacao.",
                "Se integrar a Republica, corrompe o processo. Assembleia capturada.",
                if score < 60 {
                    "Votar limitacao de mandatos + auditoria continua."
                } else {
                    "Monitorar."
                },
            )
        } else if score < 60 {
            (
                60.0,
                "Erosao da confianca institucional. Alternativas sufocadas.",
                "Integracao arriscada. Monitoramento continuo necessario.",
                if score < 60 {
                    "Votar limitacao de mandatos + auditoria continua."
                } else {
                    "Monitorar."
                },
            )
        } else {
            (
                25.0,
                "Risco baixo de degeneracao. Renovacao possivel.",
                "Integracao com salvaguardas.",
                if score < 60 {
                    "Votar limitacao de mandatos + auditoria continua."
                } else {
                    "Monitorar."
                },
            )
        };

        cenarios.push(SimulacaoCenario {
            cenario: "Sujeito continua exercendo poder (status quo)".to_string(),
            probabilidade_pct: prob,
            impacto_democracia: impacto_dem.to_string(),
            impacto_republica: impacto_rep.to_string(),
            acao_recomendada: acao.to_string(),
        });

        // Cenario 2
        cenarios.push(SimulacaoCenario {
            cenario: "Sujeito e substituido por sucessor da mesma equipe".to_string(),
            probabilidade_pct: if avaliacao.mandatos >= 3 { 70.0 } else { 40.0 },
            impacto_democracia: "Equipe perpetua sem a 'cara'. Pode ser pior (menos escrutinio) ou melhor (renovacao).".to_string(),
            impacto_republica: "Avaliar a EQUIPE, nao so o sujeito. Se a equipe corrompeu o processo, trocar a cara nao resolve.".to_string(),
            acao_recomendada: "Auditar a EQUIPE (OpenTeamAudit), nao so o sujeito.".to_string(),
        });

        // Cenario 3
        cenarios.push(SimulacaoCenario {
            cenario: "Nova candidatura emerge fora da maquina".to_string(),
            probabilidade_pct: if score < 40 { 30.0 } else { 50.0 },
            impacto_democracia:
                "Renovacao democratica real. Risco de ser destruida pela maquina instalada."
                    .to_string(),
            impacto_republica:
                "Oportunidade de integrar sujeito sem divida com aparelho corrompido.".to_string(),
            acao_recomendada:
                "PROTEGER a nova candidatura (P4: democracia radical exige pluralismo real)."
                    .to_string(),
        });

        // Cenario 4
        cenarios.push(SimulacaoCenario {
            cenario: "Processo politico reestruturado (Nova Republica)".to_string(),
            probabilidade_pct: 100.0,
            impacto_democracia: "Fim do ciclo de manipulacao. Voto = deliberacao, nao transacao.".to_string(),
            impacto_republica: "O sujeito e avaliado em processo NOVO. Divida com o sistema antigo documentada, nao ignorada.".to_string(),
            acao_recomendada: "Assembleia constituinte decide: reintegrar com restricoes ou comecar do zero.".to_string(),
        });

        cenarios
    }

    pub fn comparar_sujeitos(
        &self,
        a: &AvaliacaoConfiabilidade,
        b: &AvaliacaoConfiabilidade,
    ) -> String {
        let diff = a.score - b.score;
        let relacao = if (diff).abs() < 5 {
            "equivalentes em confiabilidade".to_string()
        } else if diff > 0 {
            format!("'{}' mais confiavel por {} pontos", a.sujeito, diff)
        } else {
            format!("'{}' mais confiavel por {} pontos", b.sujeito, diff.abs())
        };

        format!(
            "COMPARACAO:\n  {}: score {} ({})\n  {}: score {} ({})\n  Resultado: {}.\n  AVISO: comparar scores NAO significa que um e 'melhor'. Significa que um tem MENOS indicadores de processo corrompido. A Republica nao escolhe o 'menos pior'. Escolhe o processo LIMPO.",
            a.sujeito, a.score, a.nivel.rotulo(),
            b.sujeito, b.score, b.nivel.rotulo(),
            relacao
        )
    }
}

// ============================================================================
// 4. DEMO (fn main)
// ============================================================================

fn main() {
    let mut e = ConfiabilidadeEngine::new();

    println!("{}", "=".repeat(70));
    println!("OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito");
    println!("{}", "=".repeat(70));

    // --- Sujeito A: "O Operador" ---
    println!("\n[AVALIACAO] Sujeito: 'O Operador' (perfil: lider historico de esquerda)");

    let indicadores_a: Vec<IndicadorPolitico> = vec![
        IndicadorPolitico {
            tipo: TipoIndicador::USO_APARELHO_PUBLICO,
            descricao: "Maquina publica (cargos, beneficios, programas sociais) usada como aparelho eleitoral em 3 ciclos eleitorais.".to_string(),
            grau_evidencia: GraveEvidencia::EVIDENCIA_JORNALISTICA,
            ocorrencias: 3,
            periodo: "3 eleicoes sucessivas".to_string(),
            metodos: vec![MetodoManipulacao::APARELHO_ELEITORAL],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::COMPRA_VOTO,
            descricao: "Programas sociais temporalmente ampliados antes de eleicoes; promessa de manutencao condicional ao voto.".to_string(),
            grau_evidencia: GraveEvidencia::INDICIO_FORTE,
            ocorrencias: 3,
            periodo: "3 ciclos eleitorais".to_string(),
            metodos: vec![MetodoManipulacao::CLIENTELISMO],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::CONTINUIDADE_PODER,
            descricao: "Busca pelo 4o mandato. Equipe articula continuidade com a mesma figura como 'cara' do projeto.".to_string(),
            grau_evidencia: GraveEvidencia::EVIDENCIA_JORNALISTICA,
            ocorrencias: 1,
            periodo: "pre-2026".to_string(),
            metodos: vec![],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::DESMANCHE_ALTERNATIVAS,
            descricao: "Novas candidaturas de esquerda desarticuladas pela maquina. Dissidentes marginalizados ou cooptados.".to_string(),
            grau_evidencia: GraveEvidencia::INDICIO_FORTE,
            ocorrencias: 4,
            periodo: "".to_string(),
            metodos: vec![MetodoManipulacao::IMPEDIR_CANDIDATURA, MetodoManipulacao::CARGOS_TROCA],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::CORRUPCAO_SISTEMICA,
            descricao: "Multiplos esquemas de corrupcao vinculados a figuras do nucleo de poder (mensalao, petrolao, etc.). Padrao, nao caso isolado.".to_string(),
            grau_evidencia: GraveEvidencia::COMPROVADO_JUDICIAL,
            ocorrencias: 5,
            periodo: "2005-presente".to_string(),
            metodos: vec![],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::MANIPULACAO_INFORMACAO,
            descricao: "Operacao de bots e redes sociais com intensidade equivalente a da direita. Narrativa fabricada em escala.".to_string(),
            grau_evidencia: GraveEvidencia::INVESTIGACAO_OFICIAL,
            ocorrencias: 2,
            periodo: "2022-2026".to_string(),
            metodos: vec![MetodoManipulacao::BOTS_REDES, MetodoManipulacao::NARRATIVA_FABRICADA],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::PERSONALISMO,
            descricao: "Lider apresentado como insubstituivel. Nao ha plano de successao real -- a figura e o projeto.".to_string(),
            grau_evidencia: GraveEvidencia::EVIDENCIA_JORNALISTICA,
            ocorrencias: 1,
            periodo: "".to_string(),
            metodos: vec![],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::MILITANCIA_FINANCEIRA,
            descricao: "Distribuicao de cargos e verbas em troca de apoio politico da base. Lealdade comprada, nao convencida.".to_string(),
            grau_evidencia: GraveEvidencia::COMPROVADO_JUDICIAL,
            ocorrencias: 3,
            periodo: "".to_string(),
            metodos: vec![MetodoManipulacao::CARGOS_TROCA],
            detalhe: "".to_string(),
        },
    ];

    let eventos_a = vec![
        e.registrar_evento(
            "2003-2010",
            "Dois mandatos presidenciais",
            "eleicao",
            0,
            GraveEvidencia::SUSPEITA,
        ),
        e.registrar_evento(
            "2005",
            "Mensalao: compra sistemica de votos no Congresso",
            "investigacao",
            -8,
            GraveEvidencia::COMPROVADO_JUDICIAL,
        ),
        e.registrar_evento(
            "2014",
            "Operacao Lava Jato: esquema PETROBRAS",
            "investigacao",
            -8,
            GraveEvidencia::COMPROVADO_JUDICIAL,
        ),
        e.registrar_evento(
            "2018-2021",
            "Prisao e condenacao (depois anuladas)",
            "judicial",
            -3,
            GraveEvidencia::INVESTIGACAO_OFICIAL,
        ),
        e.registrar_evento(
            "2023-2026",
            "Terceiro mandato: uso de aparelho em ritmo eleitoral",
            "politica_publica",
            -5,
            GraveEvidencia::INDICIO_FORTE,
        ),
    ];

    let aval_a = e.avaliar(
        "O Operador",
        "Presidente (historico)",
        4,
        indicadores_a.clone(),
        Some(eventos_a),
    );

    println!("\n  Score: {}/100", aval_a.score);
    println!("  Nivel: {}", aval_a.nivel.rotulo());
    println!("  Veredito: {}", aval_a.veredito.rotulo());
    println!("\n  INDICADORES DETECTADOS ({}):", aval_a.indicadores.len());
    for ind in &aval_a.indicadores {
        println!("    [{}]", ind.tipo.rotulo());
        println!("      {}", ind.descricao);
        println!(
            "      Evidencia: {} | Ocorrencias: {}",
            ind.grau_evidencia.rotulo(),
            ind.ocorrencias
        );
    }
    println!("\n  PONTOS FRACOS:");
    for pf in &aval_a.pontos_fraco {
        println!("    - {}", pf);
    }
    println!("\n  RECOMENDACOES:");
    for rec in &aval_a.recomendacoes {
        println!("    -> {}", rec);
    }
    println!("\n  JUSTIFICATIVA: {}", aval_a.justificativa);

    // --- Simulacao de cenarios ---
    println!("\n{}", "=".repeat(70));
    println!("[SIMULACAO DE CENARIOS]");
    println!("{}", "=".repeat(70));
    let cenarios = e.simular_cenarios(&aval_a);
    for (i, c) in cenarios.iter().enumerate() {
        println!("\n  Cenario {}: {}", i + 1, c.cenario);
        println!("  Probabilidade: {}%", c.probabilidade_pct);
        println!("  Impacto na democracia: {}", c.impacto_democracia);
        println!("  Impacto na Republica: {}", c.impacto_republica);
        println!("  Acao: {}", c.acao_recomendada);
    }

    // --- Comparacao com "O Polarizador" ---
    println!("\n{}", "=".repeat(70));
    println!("[COMPARACAO] O Operador vs O Polarizador (extrema-direita)");
    println!("{}", "=".repeat(70));

    let indicadores_b: Vec<IndicadorPolitico> = vec![
        IndicadorPolitico {
            tipo: TipoIndicador::MANIPULACAO_INFORMACAO,
            descricao: "Operacao massiva de bots e fake news. Gabinete do odio institucionalizado.".to_string(),
            grau_evidencia: GraveEvidencia::INVESTIGACAO_OFICIAL,
            ocorrencias: 3,
            periodo: "".to_string(),
            metodos: vec![MetodoManipulacao::BOTS_REDES, MetodoManipulacao::NARRATIVA_FABRICADA, MetodoManipulacao::MEDO_E_AMEACA],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::VIOLACAO_PRINCIPIOS,
            descricao: "Ataques sistemicos a instituicoes democraticas. Discurso de ruptura constitucional.".to_string(),
            grau_evidencia: GraveEvidencia::COMPROVADO_JUDICIAL,
            ocorrencias: 5,
            periodo: "".to_string(),
            metodos: vec![],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::CORRUPCAO_SISTEMICA,
            descricao: "Esquema de rachadinha no nucleo familiar e militar. Cargo publico como negocio.".to_string(),
            grau_evidencia: GraveEvidencia::COMPROVADO_JUDICIAL,
            ocorrencias: 3,
            periodo: "".to_string(),
            metodos: vec![],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::USO_APARELHO_PUBLICO,
            descricao: "Uso de atos oficiais, decretos e cargo para beneficios eleitorais e ataque a opositores.".to_string(),
            grau_evidencia: GraveEvidencia::EVIDENCIA_JORNALISTICA,
            ocorrencias: 2,
            periodo: "".to_string(),
            metodos: vec![MetodoManipulacao::APARELHO_ELEITORAL, MetodoManipulacao::JUDICIALIZACAO_ARMA],
            detalhe: "".to_string(),
        },
        IndicadorPolitico {
            tipo: TipoIndicador::PERSONALISMO,
            descricao: "Lider como messias. Movimento como seita. Nao ha sucesso institucional planejado.".to_string(),
            grau_evidencia: GraveEvidencia::EVIDENCIA_JORNALISTICA,
            ocorrencias: 1,
            periodo: "".to_string(),
            metodos: vec![],
            detalhe: "".to_string(),
        },
    ];

    let aval_b = e.avaliar(
        "O Polarizador",
        "Presidente (extrema-direita)",
        1,
        indicadores_b.clone(),
        None,
    );

    println!(
        "\n  O Polarizador: score {}/100 ({})",
        aval_b.score,
        aval_b.nivel.rotulo()
    );
    println!("  Veredito: {}", aval_b.veredito.rotulo());
    println!("\n{}", e.comparar_sujeitos(&aval_a, &aval_b));

    // --- Scorecard comparativo ---
    println!("\n{}", "=".repeat(70));
    println!("[SCORECARD COMPARATIVO]");
    println!("{}", "=".repeat(70));
    println!(
        "  {:.<40} {:>10} {:>12}",
        "Indicador", "Operador", "Polarizador"
    );
    println!("  {}", "-".repeat(62));
    for t in [
        TipoIndicador::USO_APARELHO_PUBLICO,
        TipoIndicador::COMPRA_VOTO,
        TipoIndicador::CONTINUIDADE_PODER,
        TipoIndicador::DESMANCHE_ALTERNATIVAS,
        TipoIndicador::CORRUPCAO_SISTEMICA,
        TipoIndicador::MANIPULACAO_INFORMACAO,
        TipoIndicador::OPACIDADE,
        TipoIndicador::PERSONALISMO,
        TipoIndicador::VIOLACAO_PRINCIPIOS,
        TipoIndicador::MILITANCIA_FINANCEIRA,
    ] {
        let a_tem = if indicadores_a.iter().any(|i| i.tipo == t) {
            "SIM"
        } else {
            "nao"
        };
        let b_tem = if indicadores_b.iter().any(|i| i.tipo == t) {
            "SIM"
        } else {
            "nao"
        };
        println!("  {:.<40} {:>10} {:>12}", t.rotulo(), a_tem, b_tem);
    }
    println!(
        "\n  {:.<40} {:>10} {:>12}",
        "Score final", aval_a.score, aval_b.score
    );
    println!(
        "  {:.<40} {:>10} {:>12}",
        "Nivel",
        aval_a.nivel.id(),
        aval_b.nivel.id()
    );
    println!(
        "  {:.<40} {:>10} {:>12}",
        "Veredito",
        aval_a.veredito.id(),
        aval_b.veredito.id()
    );

    // --- FILOSOFIA ---
    println!("\n{}", "=".repeat(70));
    println!("FILOSOFIA -- A Republica nao escolhe o 'menos pior'");
    println!("{}", "=".repeat(70));
    println!(
        r#"
A TENSAO FUNDAMENTAL:
  O sistema eleitoral atual obriga a escolher entre 'menos pior'.
  Esquerda que compra voto com bolsa vs Direita que compra voto com medo.
  Ambos manipulam. Ambos corrompem o processo. Ambos usam bots.
  A diferenca nao e de PRINCIPIO -- e de METODO.

O QUE A REPUBLICA FAZ DIFERENTE:
  A Republica NAO escolhe entre dois processos corrompidos.
  Ela CRIA um terceiro: processo limpo, voto = deliberacao, sem aparelho.

O DIAGNOSTICO:
  O Operador: usa o APARELHO DE ESTADO para perpetuar.
    - 3 eleicoes com maquina publica.
    - Equipe quer a 4a porque a figura e a 'cara' da transacao.
    - Desmancha alternativas DA PROPRIA ESQUERDA.
    - Corrupcao COMPROVADA judicialmente (mensalao, petrolao).
    - Bots em escala equivalente a extrema-direita.

  O Polarizador: usa o MEDO e a RUPTURA para perpetuar.
    - Ataca instituicoes.
    - Bots e gabinete do odio.
    - Corrupcao familiar/militar.
    - Risco de ruptura democratica.

  AMBOS tem score ALTO RISCO ou INACEITAVEL.
  A Republica NAO integra nenhum dos dois sem auditoria radical.

A SOLUCAO NAO E ESCOLHER LADOS:
  A solucao e RECONSTRUIR O PROCESSO.
  - Voto sem aparelho (OpenVoteIntegrity).
  - Bots detectados e neutralizados (P9 + OpenAntiPolarization).
  - Mandatos limitados (renovacao obrigatoria).
  - Novas candidaturas PROTEGIDAS (pluralismo real).
  - Equipe auditada, nao so o sujeito (OpenTeamAudit).

A PERGUNTA CERTA NAO E 'em quem confiar?'.
  E 'que PROCESSO merece confianca?'.
  O sujeito e temporario. O processo e permanente.
  Processo corrompido corrompe qualquer sujeito.
  Processo limpo protege qualquer sujeito -- inclusive de si mesmo.
"#
    );
}
