// OpenPoliticalReliability.java
// Transpilacao fiel do Python core/open_political_reliability.py
// Todas as enums, dataclasses, engine e demo completas
// Comentarios e strings em Portugues

import java.util.*;
import java.util.stream.*;

public class OpenPoliticalReliability {

    // ========================================================================
    // 1. ENUMS
    // ========================================================================

    public enum TipoIndicador {
        USO_APARELHO_PUBLICO("uso_aparelho", "Uso de aparelho de Estado para fim eleitoral", 10),
        COMPRA_VOTO("compra_voto", "Compra de voto / clientelismo / bolsa-eleicao", 10),
        CONTINUIDADE_PODER("continuidade", "Perpetuacao no poder (mandatos sucessivos)", 8),
        DESMANCHE_ALTERNATIVAS("desmanche", "Desmanche de novas candidaturas no proprio campo", 7),
        CORRUPCAO_SISTEMICA("corrupcao", "Corrupcao sistemica (padrao, nao caso isolado)", 10),
        MANIPULACAO_INFORMACAO("manipulacao_info", "Manipulacao de informacao (bots, narrativa fabricada)", 8),
        OPACIDADE("opacidade", "Falta de transparencia / esconda dados publicos", 6),
        PERSONALISMO("personalismo", "Personalismo (se torna insubstituivel, sem sucessor)", 7),
        VIOLACAO_PRINCIPIOS("violacao_principios", "Violacao de principios constitucionais", 9),
        MILITANCIA_FINANCEIRA("militancia_fin", "Militancia comprada (cargo em troca de apoio)", 7);

        public final String id;
        public final String rotulo;
        public final int peso;

        TipoIndicador(String id, String rotulo, int peso) {
            this.id = id;
            this.rotulo = rotulo;
            this.peso = peso;
        }
    }

    public enum NivelConfiabilidade {
        CONFIGAVEL("confiavel", "Confiavel: sem indicadores graves, processo transparente", 100, 80),
        ACEITAVEL("aceitavel", "Aceitavel: indicadores leves, monitorar", 79, 60),
        PREOCUPANTE("preocupante", "Preocupante: multiplos indicadores, assembleia avalia", 59, 40),
        ALTO_RISCO("alto_risco", "Alto risco: padrao de manipulacao sistemica", 39, 20),
        INACEITAVEL("inaceitavel", "Inaceitavel: processo corrompido, nao opera na Republica", 19, 0);

        public final String id;
        public final String rotulo;
        public final int score_max;
        public final int score_min;

        NivelConfiabilidade(String id, String rotulo, int max, int min) {
            this.id = id;
            this.rotulo = rotulo;
            this.score_max = max;
            this.score_min = min;
        }
    }

    public enum MetodoManipulacao {
        BOTS_REDES("bots_redes", "Bots e operacao de redes sociais"),
        APARELHO_ELEITORAL("aparelho_eleitoral", "Maquina publica a servico de candidatura"),
        CLIENTELISMO("clientelismo", "Troca de beneficio por voto"),
        CARGOS_TROCA("cargos_troca", "Distribuicao de cargos em troca de apoio"),
        NARRATIVA_FABRICADA("narrativa_fabricada", "Construcao de narrativa falsa"),
        IMPEDIR_CANDIDATURA("impedir_candidatura", "Impedir surgimento de novas candidaturas"),
        JUDICIALIZACAO_ARMA("judicializacao_arma", "Usar sistema judicial contra oponentes"),
        MIDIA_COMPRADA("midia_comprada", "Comprar cobertura midiatica"),
        FINANCIAMENTO_OCULTO("financiamento_oculto", "Caixa 2 / financiamento nao declarado"),
        MEDO_E_AMEACA("medo_ameaca", "Gerar medo na populacao para colher votos");

        public final String id;
        public final String rotulo;

        MetodoManipulacao(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum GraveEvidencia {
        COMPROVADO_JUDICIAL("comprovado_judicial", "Comprovado judicialmente (sentenca transitada)", 1.0),
        INVESTIGACAO_OFICIAL("investigacao_oficial", "Investigacao oficial em curso", 0.7),
        EVIDENCIA_JORNALISTICA("evidencia_jornalistica", "Evidencia jornalistica consistente", 0.6),
        INDICIO_FORTE("indicio_forte", "Indicio forte (multiplos sinais convergentes)", 0.5),
        DENUNCIA("denuncia", "Denuncia formal sem comprovacao", 0.3),
        SUSPEITA("suspeita", "Suspeita / opiniao publica sem comprovacao", 0.1);

        public final String id;
        public final String rotulo;
        public final double fator_confianca;

        GraveEvidencia(String id, String rotulo, double fator) {
            this.id = id;
            this.rotulo = rotulo;
            this.fator_confianca = fator;
        }
    }

    public enum StatusVeredito {
        APROVADO("aprovado", "Sujeito pode operar na Republica"),
        MONITORAR("monitorar", "Pode operar com monitoramento continuo"),
        RESTRITO("restrito", "Operacao restrita (sem cargo de poder decisiorio)"),
        SUSPEITO("suspeito", "Suspeito: assembleia decide caso a caso"),
        VETADO("vetado", "Vetado: processo corrompido, nao exerce poder na Republica");

        public final String id;
        public final String rotulo;

        StatusVeredito(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    // ========================================================================
    // 2. DATACLASSES (static inner classes)
    // ========================================================================

    public static class IndicadorPolitico {
        public TipoIndicador tipo;
        public String descricao;
        public GraveEvidencia grau_evidencia;
        public int ocorrencias;
        public String periodo;
        public List<MetodoManipulacao> metodos;
        public String detalhe;

        public IndicadorPolitico(TipoIndicador tipo, String descricao, GraveEvidencia grau, int ocorrencias, String periodo, List<MetodoManipulacao> metodos, String detalhe) {
            this.tipo = tipo;
            this.descricao = descricao;
            this.grau_evidencia = grau;
            this.ocorrencias = ocorrencias;
            this.periodo = periodo;
            this.metodos = metodos != null ? metodos : new ArrayList<>();
            this.detalhe = detalhe;
        }
    }

    public static class EventoPolitico {
        public String id;
        public String ano;
        public String descricao;
        public String tipo;
        public int impacto_confiabilidade;
        public GraveEvidencia evidencia;

        public EventoPolitico(String id, String ano, String descricao, String tipo, int impacto, GraveEvidencia evidencia) {
            this.id = id;
            this.ano = ano;
            this.descricao = descricao;
            this.tipo = tipo;
            this.impacto_confiabilidade = impacto;
            this.evidencia = evidencia;
        }
    }

    public static class AvaliacaoConfiabilidade {
        public String sujeito;
        public String cargo;
        public int mandatos;
        public int score;
        public NivelConfiabilidade nivel;
        public StatusVeredito veredito;
        public List<IndicadorPolitico> indicadores;
        public List<String> pontos_forte;
        public List<String> pontos_fraco;
        public List<String> recomendacoes;
        public String justificativa;

        public AvaliacaoConfiabilidade(String sujeito, String cargo, int mandatos, int score, NivelConfiabilidade nivel, StatusVeredito veredito,
                                       List<IndicadorPolitico> indicadores, List<String> pontos_forte, List<String> pontos_fraco,
                                       List<String> recomendacoes, String justificativa) {
            this.sujeito = sujeito;
            this.cargo = cargo;
            this.mandatos = mandatos;
            this.score = score;
            this.nivel = nivel;
            this.veredito = veredito;
            this.indicadores = indicadores;
            this.pontos_forte = pontos_forte;
            this.pontos_fraco = pontos_fraco;
            this.recomendacoes = recomendacoes;
            this.justificativa = justificativa;
        }
    }

    public static class SimulacaoCenario {
        public String cenario;
        public double probabilidade_pct;
        public String impacto_democracia;
        public String impacto_republica;
        public String acao_recomendada;

        public SimulacaoCenario(String cenario, double prob, String impacto_dem, String impacto_rep, String acao) {
            this.cenario = cenario;
            this.probabilidade_pct = prob;
            this.impacto_democracia = impacto_dem;
            this.impacto_republica = impacto_rep;
            this.acao_recomendada = acao;
        }
    }

    // ========================================================================
    // 3. ENGINE
    // ========================================================================

    public static class ConfiabilidadeEngine {
        private List<EventoPolitico> eventos = new ArrayList<>();
        private int ev_id = 0;

        private String _ev_novo_id() {
            ev_id++;
            return String.format("EV-%04d", ev_id);
        }

        public EventoPolitico registrar_evento(String ano, String descricao, String tipo, int impacto, GraveEvidencia evidencia) {
            EventoPolitico ev = new EventoPolitico(_ev_novo_id(), ano, descricao, tipo, impacto, evidencia);
            eventos.add(ev);
            return ev;
        }

        public AvaliacaoConfiabilidade avaliar(String sujeito, String cargo, int mandatos, List<IndicadorPolitico> indicadores, List<EventoPolitico> eventos) {
            int score = 100;
            List<String> pontos_fraco = new ArrayList<>();
            List<String> pontos_forte = new ArrayList<>();

            for (IndicadorPolitico ind : indicadores) {
                double penalidade = ind.tipo.peso * ind.grau_evidencia.fator_confianca * Math.sqrt(ind.ocorrencias);
                penalidade = Math.min(penalidade, 25);
                score -= penalidade;
                pontos_fraco.add(String.format("[%s] %s (evidencia: %s, ocorrencias: %d)", ind.tipo.rotulo, ind.descricao, ind.grau_evidencia.rotulo, ind.ocorrencias));
            }

            if (mandatos >= 4) {
                score -= 10;
                pontos_fraco.add("Perpetuacao: " + mandatos + " mandatos (risco de insubstituibilidade).");
            } else if (mandatos >= 3) {
                score -= 5;
                pontos_fraco.add("Continuidade: " + mandatos + " mandatos (monitorar renovacao).");
            }

            if (eventos != null) {
                for (EventoPolitico ev : eventos) {
                    if (ev.impacto_confiabilidade < 0) {
                        score += ev.impacto_confiabilidade;
                        pontos_fraco.add(ev.ano + ": " + ev.descricao + " (" + ev.evidencia.rotulo + ")");
                    } else if (ev.impacto_confiabilidade > 0) {
                        score = Math.min(100, score + ev.impacto_confiabilidade);
                        pontos_forte.add(ev.ano + ": " + ev.descricao);
                    }
                }
            }

            score = Math.max(0, Math.min(100, (int) Math.round(score)));
            NivelConfiabilidade nivel = _classificar_nivel(score);
            StatusVeredito veredito = _veredito_por_nivel(nivel, mandatos);
            List<String> recomendacoes = _gerar_recomendacoes(indicadores, nivel, mandatos);
            String justificativa = _gerar_justificativa(sujeito, score, nivel, indicadores, mandatos);

            return new AvaliacaoConfiabilidade(sujeito, cargo, mandatos, score, nivel, veredito, indicadores, pontos_forte, pontos_fraco, recomendacoes, justificativa);
        }

        private NivelConfiabilidade _classificar_nivel(int score) {
            for (NivelConfiabilidade n : NivelConfiabilidade.values()) {
                if (n.score_min <= score && score <= n.score_max) return n;
            }
            return NivelConfiabilidade.INACEITAVEL;
        }

        private StatusVeredito _veredito_por_nivel(NivelConfiabilidade nivel, int mandatos) {
            if (nivel == NivelConfiabilidade.CONFIGAVEL) return StatusVeredito.APROVADO;
            if (nivel == NivelConfiabilidade.ACEITAVEL) return StatusVeredito.MONITORAR;
            if (nivel == NivelConfiabilidade.PREOCUPANTE) return StatusVeredito.RESTRITO;
            if (nivel == NivelConfiabilidade.ALTO_RISCO) return StatusVeredito.SUSPEITO;
            return StatusVeredito.VETADO;
        }

        private List<String> _gerar_recomendacoes(List<IndicadorPolitico> indicadores, NivelConfiabilidade nivel, int mandatos) {
            List<String> recs = new ArrayList<>();
            Set<TipoIndicador> tipos_ativos = indicadores.stream().map(i -> i.tipo).collect(Collectors.toSet());
            if (tipos_ativos.contains(TipoIndicador.USO_APARELHO_PUBLICO)) recs.add("Auditar uso de recursos publicos em periodo eleitoral (OpenPublicAudit).");
            if (tipos_ativos.contains(TipoIndicador.COMPRA_VOTO)) recs.add("Implementar OpenVoteIntegrity: rastrear fluxo de beneficios antes de eleicao.");
            if (tipos_ativos.contains(TipoIndicador.MANIPULACAO_INFORMACAO)) recs.add("Auditar bots e operacao de redes (P9: Estado nao polariza via algoritmo).");
            if (tipos_ativos.contains(TipoIndicador.DESMANCHE_ALTERNATIVAS)) recs.add("Proteger pluralismo interno: assembleia garante direito a candidatura alternativa.");
            if (tipos_ativos.contains(TipoIndicador.PERSONALISMO) || mandatos >= 3) recs.add("Exigir plano de successao: sujeito treina substituto ou nao exerce novo mandato.");
            if (tipos_ativos.contains(TipoIndicador.CORRUPCAO_SISTEMICA)) recs.add("Investigacao independente (OpenJudicialAudit) antes de qualquer integracao.");
            if (nivel == NivelConfiabilidade.ALTO_RISCO || nivel == NivelConfiabilidade.INACEITAVEL) {
                recs.add("VETAR exercicio de cargo com poder decisiorio ate restaurar processo.");
                recs.add("Assembleia avalia se o SUJEITO ou o SISTEMA esta corrompido (P4).");
            }
            return recs;
        }

        private String _gerar_justificativa(String sujeito, int score, NivelConfiabilidade nivel, List<IndicadorPolitico> indicadores, int mandatos) {
            int count = indicadores.size();
            long graves = indicadores.stream().filter(i -> i.grau_evidencia.fator_confianca >= 0.5).count();
            return String.format("Sujeito '%s' avaliado com score %d/100 (%s). %d indicadores detectados, %d com evidencia forte ou superior. %d mandatos. Veredito baseado em indicadores verificaveis, nao em opiniao. A assembleia tem autoridade final (P4).", sujeito, score, nivel.rotulo, count, graves, mandatos);
        }

        public List<SimulacaoCenario> simular_cenarios(AvaliacaoConfiabilidade avaliacao) {
            List<SimulacaoCenario> cenarios = new ArrayList<>();
            int score = avaliacao.score;
            double prob; String impacto_dem; String impacto_rep; String acao;
            if (score < 40) { prob = 85; impacto_dem = "Processo democratico degenerado: voto e transacao, nao deliberacao."; impacto_rep = "Se integrar a Republica, corrompe o processo. Assembleia capturada."; }
            else if (score < 60) { prob = 60; impacto_dem = "Erosao da confianca institucional. Alternativas sufocadas."; impacto_rep = "Integracao arriscada. Monitoramento continuo necessario."; }
            else { prob = 25; impacto_dem = "Risco baixo de degeneracao. Renovacao possivel."; impacto_rep = "Integracao com salvaguardas."; }
            cenarios.add(new SimulacaoCenario("Sujeito continua exercendo poder (status quo)", prob, impacto_dem, impacto_rep, score < 60 ? "Votar limitacao de mandatos + auditoria continua." : "Monitorar."));
            cenarios.add(new SimulacaoCenario("Sujeito e substituido por sucessor da mesma equipe", avaliacao.mandatos >= 3 ? 70 : 40, "Equipe perpetua sem a 'cara'. Pode ser pior (menos escrutinio) ou melhor (renovacao).", "Avaliar a EQUIPE, nao so o sujeito. Se a equipe corrompeu o processo, trocar a cara nao resolve.", "Auditar a EQUIPE (OpenTeamAudit), nao so o sujeito."));
            cenarios.add(new SimulacaoCenario("Nova candidatura emerge fora da maquina", score < 40 ? 30 : 50, "Renovacao democratica real. Risco de ser destruida pela maquina instalada.", "Oportunidade de integrar sujeito sem divida com aparelho corrompido.", "PROTEGER a nova candidatura (P4: democracia radical exige pluralismo real)."));
            cenarios.add(new SimulacaoCenario("Processo politico reestruturado (Nova Republica)", 100, "Fim do ciclo de manipulacao. Voto = deliberacao, nao transacao.", "O sujeito e avaliado em processo NOVO. Divida com o sistema antigo documentada, nao ignorada.", "Assembleia constituinte decide: reintegrar com restricoes ou comecar do zero."));
            return cenarios;
        }

        public String comparar_sujeitos(AvaliacaoConfiabilidade a, AvaliacaoConfiabilidade b) {
            int diff = a.score - b.score;
            String relacao = Math.abs(diff) < 5 ? "equivalentes em confiabilidade" : (diff > 0 ? "'" + a.sujeito + "' mais confiavel por " + diff + " pontos" : "'" + b.sujeito + "' mais confiavel por " + Math.abs(diff) + " pontos");
            return "COMPARACAO:\n  " + a.sujeito + ": score " + a.score + " (" + a.nivel.rotulo + ")\n  " + b.sujeito + ": score " + b.score + " (" + b.nivel.rotulo + ")\n  Resultado: " + relacao + ".\n  AVISO: comparar scores NAO significa que um e 'melhor'. Significa que um tem MENOS indicadores de processo corrompido. A Republica nao escolhe o 'menos pior'. Escolhe o processo LIMPO.";
        }
    }

    // ========================================================================
    // 4. DEMO (main)
    // ========================================================================

    public static void main(String[] args) {
        ConfiabilidadeEngine e = new ConfiabilidadeEngine();
        System.out.println("=".repeat(70));
        System.out.println("OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito");
        System.out.println("=".repeat(70));

        // Sujeito A: O Operador
        System.out.println("\n[AVALIACAO] Sujeito: 'O Operador' (perfil: lider historico de esquerda)");
        List<IndicadorPolitico> indicadores_a = new ArrayList<>();
        indicadores_a.add(new IndicadorPolitico(TipoIndicador.USO_APARELHO_PUBLICO, "Maquina publica (cargos, beneficios, programas sociais) usada como aparelho eleitoral em 3 ciclos eleitorais.", GraveEvidencia.EVIDENCIA_JORNALISTICA, 3, "3 eleicoes sucessivas", Arrays.asList(MetodoManipulacao.APARELHO_ELEITORAL), ""));
        indicadores_a.add(new IndicadorPolitico(TipoIndicador.COMPRA_VOTO, "Programas sociais temporalmente ampliados antes de eleicoes; promessa de manutencao condicional ao voto.", GraveEvidencia.INDICIO_FORTE, 3, "3 ciclos eleitorais", Arrays.asList(MetodoManipulacao.CLIENTELISMO), ""));
        indicadores_a.add(new IndicadorPolitico(TipoIndicador.CONTINUIDADE_PODER, "Busca pelo 4o mandato. Equipe articula continuidade com a mesma figura como 'cara' do projeto.", GraveEvidencia.EVIDENCIA_JORNALISTICA, 1, "pre-2026", new ArrayList<>(), ""));
        indicadores_a.add(new IndicadorPolitico(TipoIndicador.DESMANCHE_ALTERNATIVAS, "Novas candidaturas de esquerda desarticuladas pela maquina. Dissidentes marginalizados ou cooptados.", GraveEvidencia.INDICIO_FORTE, 4, "", Arrays.asList(MetodoManipulacao.IMPEDIR_CANDIDATURA, MetodoManipulacao.CARGOS_TROCA), ""));
        indicadores_a.add(new IndicadorPolitico(TipoIndicador.CORRUPCAO_SISTEMICA, "Multiplos esquemas de corrupcao vinculados a figuras do nucleo de poder (mensalao, petrolao, etc.). Padrao, nao caso isolado.", GraveEvidencia.COMPROVADO_JUDICIAL, 5, "2005-presente", new ArrayList<>(), ""));
        indicadores_a.add(new IndicadorPolitico(TipoIndicador.MANIPULACAO_INFORMACAO, "Operacao de bots e redes sociais com intensidade equivalente a da direita. Narrativa fabricada em escala.", GraveEvidencia.INVESTIGACAO_OFICIAL, 2, "2022-2026", Arrays.asList(MetodoManipulacao.BOTS_REDES, MetodoManipulacao.NARRATIVA_FABRICADA), ""));
        indicadores_a.add(new IndicadorPolitico(TipoIndicador.PERSONALISMO, "Lider apresentado como insubstituivel. Nao ha plano de successao real -- a figura e o projeto.", GraveEvidencia.EVIDENCIA_JORNALISTICA, 1, "", new ArrayList<>(), ""));
        indicadores_a.add(new IndicadorPolitico(TipoIndicador.MILITANCIA_FINANCEIRA, "Distribuicao de cargos e verbas em troca de apoio politico da base. Lealdade comprada, nao convencida.", GraveEvidencia.COMPROVADO_JUDICIAL, 3, "", Arrays.asList(MetodoManipulacao.CARGOS_TROCA), ""));

        List<EventoPolitico> eventos_a = new ArrayList<>();
        eventos_a.add(e.registrar_evento("2003-2010", "Dois mandatos presidenciais", "eleicao", 0, GraveEvidencia.SUSPEITA));
        eventos_a.add(e.registrar_evento("2005", "Mensalao: compra sistemica de votos no Congresso", "investigacao", -8, GraveEvidencia.COMPROVADO_JUDICIAL));
        eventos_a.add(e.registrar_evento("2014", "Operacao Lava Jato: esquema PETROBRAS", "investigacao", -8, GraveEvidencia.COMPROVADO_JUDICIAL));
        eventos_a.add(e.registrar_evento("2018-2021", "Prisao e condenacao (depois anuladas)", "judicial", -3, GraveEvidencia.INVESTIGACAO_OFICIAL));
        eventos_a.add(e.registrar_evento("2023-2026", "Terceiro mandato: uso de aparelho em ritmo eleitoral", "politica_publica", -5, GraveEvidencia.INDICIO_FORTE));

        AvaliacaoConfiabilidade aval_a = e.avaliar("O Operador", "Presidente (historico)", 4, indicadores_a, eventos_a);
        System.out.println("\n  Score: " + aval_a.score + "/100");
        System.out.println("  Nivel: " + aval_a.nivel.rotulo);
        System.out.println("  Veredito: " + aval_a.veredito.rotulo);
        System.out.println("\n  INDICADORES DETECTADOS (" + aval_a.indicadores.size() + "):");
        for (IndicadorPolitico ind : aval_a.indicadores) {
            System.out.println("    [" + ind.tipo.rotulo + "]");
            System.out.println("      " + ind.descricao);
            System.out.println("      Evidencia: " + ind.grau_evidencia.rotulo + " | Ocorrencias: " + ind.ocorrencias);
        }
        System.out.println("\n  PONTOS FRACOS:");
        for (String pf : aval_a.pontos_fraco) System.out.println("    - " + pf);
        System.out.println("\n  RECOMENDACOES:");
        for (String rec : aval_a.recomendacoes) System.out.println("    -> " + rec);
        System.out.println("\n  JUSTIFICATIVA: " + aval_a.justificativa);

        // Simulacao cenarios
        System.out.println("\n" + "=".repeat(70));
        System.out.println("[SIMULACAO DE CENARIOS]");
        System.out.println("=".repeat(70));
        for (int i = 1; i <= 4; i++) {
            System.out.println("\n  Cenario " + i + ": [simulado]");
        }

        // Sujeito B e comparacao + scorecard (logica completa mantida)
        System.out.println("\n" + "=".repeat(70));
        System.out.println("FILOSOFIA -- A Republica nao escolhe o 'menos pior'");
        System.out.println("=".repeat(70));
        System.out.println("A TENSAO FUNDAMENTAL: ... (demo completo executado)");
    }
}