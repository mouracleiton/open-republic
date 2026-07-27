// Full Java translation of open_anti_polarization.py (P9 Anti-Polarization)
// All enums, dataclasses, engine methods, and _demo() faithfully reproduced.
// Comments and strings kept in Portuguese. Runnable demo in main().

import java.util.*;
import java.util.stream.Collectors;

public class OpenAntiPolarization {

    // ============================================================================
    // 1. ENUMS
    // ============================================================================

    public enum FatorPolarizacao {
        RELIGIAO("religiao", "Religiao / fe / espiritualidade"),
        ETNIA("etnia", "Etnia / raca / origem"),
        REGIAO("regiao", "Regiao / geografia (norte vs sul, urbano vs rural)"),
        CLASSE("classe", "Classe / origem economica (heranca do sistema antigo)"),
        IDEOLOGIA("ideologia", "Ideologia politica (heranca do sistema partidario)"),
        IDENTIDADE("identidade", "Identidade de genero / sexual / expressao"),
        LINGUA("lingua", "Lingua / idioma / dialeto"),
        IDADE("idade", "Geracional (jovens vs velhos)"),
        ALGORITMO("algoritmo", "Algoritmo de feed (captura narrativa externa)"),
        CULTURA("cultura", "Cultura / costumes / tradicao");

        public final String id;
        public final String rotulo;

        FatorPolarizacao(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum NivelPolarizacao {
        SAUDAVEL("saudavel", "Saudavel: dissenso produtivo, confianca preservada", 0),
        BAIXO("baixo", "Baixo: blocos incipientes, ainda deliberam", 1),
        MODERADO("moderado", "Moderado: blocos claros, deliberacao degrada", 2),
        ALTO("alto", "Alto: votacao tribal, confianca em queda", 3),
        CRITICO("critico", "Critico: quase bloqueio assemblear", 4),
        RUPTURA("ruptura", "Ruptura epistemica: realidades de fato separadas", 5);

        public final String id;
        public final String rotulo;
        public final int gravidade;

        NivelPolarizacao(String id, String rotulo, int gravidade) {
            this.id = id;
            this.rotulo = rotulo;
            this.gravidade = gravidade;
        }
    }

    public enum TaticaPolarizante {
        OUTGROUP_DEHUMANIZATION("outgroup_dehumanization", "Desumanizacao do outro lado", 5),
        FALSE_DICHOTOMY("false_dichotomy", "Falsa dicotomia (ou nos ou eles)", 4),
        WHATABOUTISM("whataboutism", "Whataboutism (desvia com 'mas eles tambem')", 3),
        FEAR_MONGERING("fear_mongering", "Alarmismo / medo fabricado", 4),
        IDENTITY_BAITING("identity_baiting", "Isca de identidade (forca tribalismo)", 5),
        EPISTEMIC_BALKANIZATION("epistemic_balkanization", "Balkanizacao epistemica (fatos tribais)", 5),
        BOTH_SIDES_FALLACY("both_sides_fallacy", "Falsa simetria (os dois lados sao iguais)", 3),
        STRAWMAN("strawman", "Espantalho (deturpa para atacar)", 2),
        DOG_WHISTLE("dog_whistle", "Dog whistle (codigo tribal implicito)", 4),
        VIRTUE_SIGNALING("virtue_signaling", "Sinalizacao virtuosa (pertence vs exclui)", 2);

        public final String id;
        public final String rotulo;
        public final int gravidade;

        TaticaPolarizante(String id, String rotulo, int gravidade) {
            this.id = id;
            this.rotulo = rotulo;
            this.gravidade = gravidade;
        }
    }

    public enum StatusBloqueio {
        NENHUM("nenhum", "Nenhum: assembleia delibera normalmente", 0),
        ALERTA("alerta", "Alerta: moderador sinaliza polarizacao", 1),
        DELIBERACAO_ESTRUTURADA("deliberacao_estruturada", "Deliberacao estruturada obrigatoria", 2),
        MEDIACAO_OBRIGATORIA("mediacao_obrigatoria", "Mediacao obrigatoria antes de votar", 3),
        SUSPENDER_VOTACAO("suspender_votacao", "Votacao suspensa (bloqueio ativo)", 4),
        ASSEMBLEIA_PAUSA("assembleia_pausa", "Pausa assemblear (resfriamento obrigatorio)", 5);

        public final String id;
        public final String rotulo;
        public final int prioridade;

        StatusBloqueio(String id, String rotulo, int prioridade) {
            this.id = id;
            this.rotulo = rotulo;
            this.prioridade = prioridade;
        }
    }

    public enum VereditoAuditoria {
        APROVADA("aprovada", "Politica aprovada: baixo potencial polarizante"),
        APROVADA_COM_RESSALVAS("ressalvas", "Aprovada com ressalvas (mitigacoes exigidas)"),
        REJEITADA("rejeitada", "Politica rejeitada: potencial polarizante alto"),
        BLOQUEADA("bloqueada", "Politica bloqueada: e vetor de divisao identitaria");

        public final String id;
        public final String rotulo;

        VereditoAuditoria(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    // ============================================================================
    // 2. DATACLASSES (static inner classes)
    // ============================================================================

    public static class VotoCidadao {
        public final String cidadao_id;
        public final String proposta_id;
        public final boolean a_favor;
        public final String justificativa;

        public VotoCidadao(String cidadao_id, String proposta_id, boolean a_favor, String justificativa) {
            this.cidadao_id = cidadao_id;
            this.proposta_id = proposta_id;
            this.a_favor = a_favor;
            this.justificativa = justificativa == null ? "" : justificativa;
        }
    }

    public static class PropostaAssembleia {
        public final String id;
        public final String titulo;
        public String descricao;
        public FatorPolarizacao fator_aparente;
        public boolean votacao_encerrada;

        public PropostaAssembleia(String id, String titulo, String descricao, FatorPolarizacao fator_aparente) {
            this.id = id;
            this.titulo = titulo;
            this.descricao = descricao == null ? "" : descricao;
            this.fator_aparente = fator_aparente;
            this.votacao_encerrada = false;
        }
    }

    public static class BlocoVotante {
        public final String id;
        public List<String> membros;
        public double coesao;
        public FatorPolarizacao fator_dominante;

        public BlocoVotante(String id, List<String> membros, double coesao) {
            this.id = id;
            this.membros = membros == null ? new ArrayList<>() : membros;
            this.coesao = coesao;
            this.fator_dominante = null;
        }
    }

    public static class MetricaPolarizacao {
        public final String assembleia_id;
        public final int num_cidadaos;
        public final int num_blocos;
        public final double indice_divisao;
        public final double indice_tribalismo;
        public final double indice_ruptura_epistemica;
        public final NivelPolarizacao nivel;
        public final String veredito;

        public MetricaPolarizacao(String assembleia_id, int num_cidadaos, int num_blocos,
                                  double indice_divisao, double indice_tribalismo,
                                  double indice_ruptura_epistemica, NivelPolarizacao nivel, String veredito) {
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

    public static class AuditoriaPolitica {
        public final String politica_id;
        public final VereditoAuditoria veredito;
        public final List<TaticaPolarizante> taticas_detectadas;
        public final List<FatorPolarizacao> fatores_acionados;
        public final double score_polarizante;
        public final List<String> mitigacoes;
        public final String justificativa;

        public AuditoriaPolitica(String politica_id, VereditoAuditoria veredito,
                                 List<TaticaPolarizante> taticas_detectadas,
                                 List<FatorPolarizacao> fatores_acionados,
                                 double score_polarizante, List<String> mitigacoes, String justificativa) {
            this.politica_id = politica_id;
            this.veredito = veredito;
            this.taticas_detectadas = taticas_detectadas == null ? new ArrayList<>() : taticas_detectadas;
            this.fatores_acionados = fatores_acionados == null ? new ArrayList<>() : fatores_acionados;
            this.score_polarizante = score_polarizante;
            this.mitigacoes = mitigacoes == null ? new ArrayList<>() : mitigacoes;
            this.justificativa = justificativa == null ? "" : justificativa;
        }
    }

    // ============================================================================
    // 3. SINAIS DE RUPTURA EPISTEMICA
    // ============================================================================

    public static final Map<String, String> SINAIS_RUPTURA_EPISTEMICA = new LinkedHashMap<>();
    static {
        SINAIS_RUPTURA_EPISTEMICA.put("fontes_exclusivas", "Cada bloco cita fontes que o outro bloco considera falsas por principio");
        SINAIS_RUPTURA_EPISTEMICA.put("vocabulario_incomum", "Cada bloco usa vocabulario que o outro nao entende ou rejeita");
        SINAIS_RUPTURA_EPISTEMICA.put("desumanizacao", "Membros de um bloco descrevem o outro como inimigo, nao como cidadao");
        SINAIS_RUPTURA_EPISTEMICA.put("voto_identidade", "Voto decidido por identidade tribal, nao por merito da proposta");
        SINAIS_RUPTURA_EPISTEMICA.put("zero_trust", "Nenhuma afirmacao do outro lado e aceita mesmo quando factualmente correto");
        SINAIS_RUPTURA_EPISTEMICA.put("purity_test", "Membros sao punidos por reconhecer merito em argumento do outro lado");
        SINAIS_RUPTURA_EPISTEMICA.put("conspiracy_default", "Derrota politica e automaticamente atribuida a conspiracao");
        SINAIS_RUPTURA_EPISTEMICA.put("violencia_normalizada", "Violencia contra o outro bloco e tratada como legitima");
    }

    // ============================================================================
    // 4. ENGINE
    // ============================================================================

    public static class AntiPolarizacaoEngine {
        public Map<String, PropostaAssembleia> propostas = new HashMap<>();
        public List<VotoCidadao> votos = new ArrayList<>();
        public Map<String, BlocoVotante> blocos = new HashMap<>();
        public Map<String, AuditoriaPolitica> auditorias = new HashMap<>();
        private int prop_id = 0;
        private int bloco_id = 0;

        private String _prop_id_novo() {
            prop_id++;
            return String.format("PROP-%04d", prop_id);
        }

        private String _bloco_id_novo() {
            bloco_id++;
            return String.format("BLOCO-%04d", bloco_id);
        }

        public PropostaAssembleia registrar_proposta(String titulo, String descricao, FatorPolarizacao fator_aparente) {
            PropostaAssembleia p = new PropostaAssembleia(_prop_id_novo(), titulo, descricao, fator_aparente);
            propostas.put(p.id, p);
            return p;
        }

        public VotoCidadao registrar_voto(String cidadao_id, String proposta_id, boolean a_favor, String justificativa) {
            VotoCidadao v = new VotoCidadao(cidadao_id, proposta_id, a_favor, justificativa);
            votos.add(v);
            return v;
        }

        public void registrar_votacao_em_lote(List<Object[]> votacoes) {
            for (Object[] v : votacoes) {
                registrar_voto((String) v[0], (String) v[1], (Boolean) v[2], "");
            }
        }

        public void encerrar_proposta(String proposta_id) {
            if (propostas.containsKey(proposta_id)) {
                propostas.get(proposta_id).votacao_encerrada = true;
            }
        }

        public List<BlocoVotante> detectar_blocos(int num_propostas_min) {
            blocos.clear();
            Map<String, List<Boolean>> assinaturas = new HashMap<>();
            List<String> prop_ids_ordenadas = new ArrayList<>(propostas.keySet());
            Collections.sort(prop_ids_ordenadas);

            for (String pid : prop_ids_ordenadas) {
                Map<String, Boolean> votos_prop = new HashMap<>();
                for (VotoCidadao v : votos) {
                    if (v.proposta_id.equals(pid)) votos_prop.put(v.cidadao_id, v.a_favor);
                }
                for (Map.Entry<String, Boolean> entry : votos_prop.entrySet()) {
                    assinaturas.computeIfAbsent(entry.getKey(), k -> new ArrayList<>()).add(entry.getValue());
                }
            }

            Map<String, List<Boolean>> cidadaos_validos = new HashMap<>();
            for (Map.Entry<String, List<Boolean>> entry : assinaturas.entrySet()) {
                if (entry.getValue().size() >= num_propostas_min) {
                    cidadaos_validos.put(entry.getKey(), entry.getValue());
                }
            }
            if (cidadaos_validos.isEmpty()) return new ArrayList<>();

            Map<List<Boolean>, List<String>> grupos = new HashMap<>();
            for (Map.Entry<String, List<Boolean>> entry : cidadaos_validos.entrySet()) {
                grupos.computeIfAbsent(entry.getValue(), k -> new ArrayList<>()).add(entry.getKey());
            }

            List<BlocoVotante> blocos_criados = new ArrayList<>();
            for (Map.Entry<List<Boolean>, List<String>> entry : grupos.entrySet()) {
                if (entry.getValue().size() >= 2) {
                    BlocoVotante b = new BlocoVotante(_bloco_id_novo(), entry.getValue(), 1.0);
                    blocos.put(b.id, b);
                    blocos_criados.add(b);
                }
            }

            if (blocos_criados.size() == 2) {
                List<Integer> tamanhos = blocos_criados.stream().map(b -> b.membros.size()).sorted().collect(Collectors.toList());
                double razao = tamanhos.get(1) > 0 ? (double) tamanhos.get(0) / tamanhos.get(1) : 0;
                if (razao >= 0.4) {
                    blocos_criados.get(0).fator_dominante = FatorPolarizacao.IDEOLOGIA;
                    blocos_criados.get(1).fator_dominante = FatorPolarizacao.IDEOLOGIA;
                }
            }
            return blocos_criados;
        }

        public double indice_divisao() {
            if (propostas.isEmpty()) return 0.0;
            List<String> prop_ids = new ArrayList<>(propostas.keySet());
            Collections.sort(prop_ids);
            double soma = 0.0;
            int count = 0;
            for (String pid : prop_ids) {
                List<Boolean> votos_prop = new ArrayList<>();
                for (VotoCidadao v : votos) if (v.proposta_id.equals(pid)) votos_prop.add(v.a_favor);
                if (votos_prop.isEmpty()) continue;
                long favor = votos_prop.stream().filter(x -> x).count();
                long contra = votos_prop.size() - favor;
                long total = votos_prop.size();
                double d = 1.0 - Math.abs(favor - contra) / (double) total;
                soma += d;
                count++;
            }
            return count > 0 ? Math.round((soma / count) * 1000.0) / 1000.0 : 0.0;
        }

        public double indice_tribalismo() {
            List<BlocoVotante> blocosList = detectar_blocos(3);
            if (blocosList.isEmpty()) return 0.0;
            Set<String> cids_em_blocos = new HashSet<>();
            for (BlocoVotante b : blocosList) cids_em_blocos.addAll(b.membros);
            long votos_tribais = votos.stream().filter(v -> cids_em_blocos.contains(v.cidadao_id)).count();
            long total_votos = votos.size();
            return total_votos > 0 ? Math.round((votos_tribais / (double) total_votos) * 1000.0) / 1000.0 : 0.0;
        }

        public double indice_ruptura_epistemica(List<String> sinais_observados) {
            if (sinais_observados == null || sinais_observados.isEmpty()) return 0.0;
            long validos = sinais_observados.stream().filter(SINAIS_RUPTURA_EPISTEMICA::containsKey).count();
            return Math.round((validos / (double) SINAIS_RUPTURA_EPISTEMICA.size()) * 1000.0) / 1000.0;
        }

        public NivelPolarizacao classificar_nivel(List<String> sinais_observados) {
            double div = indice_divisao();
            double trib = indice_tribalismo();
            double rupt = indice_ruptura_epistemica(sinais_observados == null ? new ArrayList<>() : sinais_observados);
            if (rupt >= 0.5) return NivelPolarizacao.RUPTURA;
            if (div >= 0.8 && trib >= 0.7) return NivelPolarizacao.CRITICO;
            if (div >= 0.6 && trib >= 0.5) return NivelPolarizacao.ALTO;
            if (div >= 0.4) return NivelPolarizacao.MODERADO;
            if (div >= 0.2) return NivelPolarizacao.BAIXO;
            return NivelPolarizacao.SAUDAVEL;
        }

        public MetricaPolarizacao medir_polarizacao(String assembleia_id, List<String> sinais_observados) {
            List<BlocoVotante> blocosList = detectar_blocos(3);
            double div = indice_divisao();
            double trib = indice_tribalismo();
            double rupt = indice_ruptura_epistemica(sinais_observados == null ? new ArrayList<>() : sinais_observados);
            NivelPolarizacao nivel = classificar_nivel(sinais_observados);
            Set<String> cidadaos_unicos = new HashSet<>();
            for (VotoCidadao v : votos) cidadaos_unicos.add(v.cidadao_id);

            String veredito;
            if (nivel == NivelPolarizacao.RUPTURA) {
                veredito = "RUPTURA EPISTEMICA: realidades de fato separadas. Assembleia nao pode deliberar ate restaurar chao de fato compartilhado.";
            } else if (nivel == NivelPolarizacao.CRITICO) {
                veredito = "CRITICO: votacao tribal dominante. Mediacao obrigatoria antes de qualquer nova votacao.";
            } else if (nivel == NivelPolarizacao.ALTO) {
                veredito = "ALTO: confianca em queda. Deliberacao estruturada exigida.";
            } else if (nivel == NivelPolarizacao.MODERADO) {
                veredito = "MODERADO: blocos claros. Monitorar e facilitar dialogo.";
            } else if (nivel == NivelPolarizacao.BAIXO) {
                veredito = "BAIXO: dissenso saudavel com sinal de alinhamento tribal incipiente.";
            } else {
                veredito = "SAUDAVEL: dissenso produtivo, confianca preservada.";
            }

            return new MetricaPolarizacao(assembleia_id, cidadaos_unicos.size(), blocosList.size(), div, trib, rupt, nivel, veredito);
        }

        public AuditoriaPolitica auditar_politica(String politica_id, String titulo, String descricao,
                                                  List<TaticaPolarizante> taticas_detectadas,
                                                  List<FatorPolarizacao> fatores_acionados,
                                                  List<String> sinais_ruptura) {
            List<TaticaPolarizante> taticas = taticas_detectadas == null ? new ArrayList<>() : taticas_detectadas;
            List<FatorPolarizacao> fatores = fatores_acionados == null ? new ArrayList<>() : fatores_acionados;

            double score_taticas = Math.min(100.0, taticas.stream().mapToInt(t -> t.gravidade * 12).sum());
            Set<FatorPolarizacao> fatores_identitarios = new HashSet<>(Arrays.asList(
                    FatorPolarizacao.RELIGIAO, FatorPolarizacao.ETNIA, FatorPolarizacao.IDENTIDADE, FatorPolarizacao.CULTURA));
            int penalidade_fator = fatores.stream().mapToInt(f -> fatores_identitarios.contains(f) ? 8 : 4).sum();
            double score = Math.min(100.0, score_taticas + penalidade_fator);

            if (sinais_ruptura != null && !sinais_ruptura.isEmpty()) {
                double rupt = indice_ruptura_epistemica(sinais_ruptura);
                score = Math.min(100.0, score + rupt * 30);
            }

            List<String> mitigacoes = new ArrayList<>();
            if (taticas.contains(TaticaPolarizante.OUTGROUP_DEHUMANIZATION))
                mitigacoes.add("Remover linguagem que desumaniza cidadaos do outro lado.");
            if (taticas.contains(TaticaPolarizante.FALSE_DICHOTOMY))
                mitigacoes.add("Apresentar 3+ opcoes, nao binomio nos-vs-eles.");
            if (taticas.contains(TaticaPolarizante.FEAR_MONGERING))
                mitigacoes.add("Substituir alarmismo por dados verificaveis e calmos.");
            if (taticas.contains(TaticaPolarizante.IDENTITY_BAITING))
                mitigacoes.add("Desacoplar a politica de identidade tribal (P9: Estado nao polariza).");
            if (taticas.contains(TaticaPolarizante.EPISTEMIC_BALKANIZATION))
                mitigacoes.add("Citar fontes reconhecidas por AMBOS os blocos (chao de fato compartilhado).");
            if (fatores.stream().anyMatch(fatores_identitarios::contains))
                mitigacoes.add("Reescrever sem apelar a divisao identitaria (religiao/etnia/identidade).");
            if (score >= 40 && score < 70)
                mitigacoes.add("Submeter a deliberacao estruturada antes da votacao.");
            if (score >= 70)
                mitigacoes.add("Politica deve ser fundamentalmente reformulada.");

            VereditoAuditoria veredito;
            String justif;
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

            AuditoriaPolitica aud = new AuditoriaPolitica(politica_id, veredito, taticas, fatores, Math.round(score * 10.0) / 10.0, mitigacoes, justif);
            auditorias.put(politica_id, aud);
            return aud;
        }

        public StatusBloqueio protocolo_bloqueio(MetricaPolarizacao metrica) {
            if (metrica.nivel == NivelPolarizacao.RUPTURA) return StatusBloqueio.ASSEMBLEIA_PAUSA;
            if (metrica.nivel == NivelPolarizacao.CRITICO) return StatusBloqueio.SUSPENDER_VOTACAO;
            if (metrica.nivel == NivelPolarizacao.ALTO) return StatusBloqueio.MEDIACAO_OBRIGATORIA;
            if (metrica.nivel == NivelPolarizacao.MODERADO) return StatusBloqueio.DELIBERACAO_ESTRUTURADA;
            if (metrica.nivel == NivelPolarizacao.BAIXO) return StatusBloqueio.ALERTA;
            return StatusBloqueio.NENHUM;
        }

        public List<String> recomendacoes_mediacao(MetricaPolarizacao metrica) {
            List<String> recs = new ArrayList<>();
            NivelPolarizacao n = metrica.nivel;
            if (n == NivelPolarizacao.SAUDAVEL) {
                recs.add("Manter: dissenso produtivo e saudavel (P2).");
                return recs;
            }
            if (n == NivelPolarizacao.BAIXO || n == NivelPolarizacao.MODERADO) {
                recs.add("Facilitar dialogo estruturado entre blocos (nao debate livre -- agrava).");
                recs.add("Identificar o chao de fato compartilhado antes de divergir.");
                recs.add("Rotular taticas polarizantes quando aparecerem (metacognicao assemblear).");
            }
            if (n == NivelPolarizacao.ALTO || n == NivelPolarizacao.CRITICO) {
                recs.add("Mediador profissional obrigatoria (OpenCommunityLeaders).");
                recs.add("Votacao adiada ate confianca minima restaurada.");
                recs.add("Deliberacao em sub-grupos mistos (quebra de bloco tribal).");
                recs.add("Auditar algoritmos de feed que podem estar amplificando (P8).");
            }
            if (n == NivelPolarizacao.RUPTURA) {
                recs.add("EMERGENCIA: assembleia em pausa. Nao votar.");
                recs.add("Restaurar chao de fato: comissao de verificacao (HumanKnowledge).");
                recs.add("Dialogo individual antes de coletivo (quebra de tribalismo).");
                recs.add("Investigar captura narrativa externa (algoritmo, ator malicioso).");
                recs.add("Considerar OpenWololo se a divisao for irreparavel (separar, nao subjugar).");
            }
            return recs;
        }

        public Map<String, Object> scorecard() {
            List<BlocoVotante> blocosList = detectar_blocos(3);
            long bloqueadas = auditorias.values().stream().filter(a -> a.veredito == VereditoAuditoria.BLOQUEADA).count();
            long aprovadas = auditorias.values().stream().filter(a ->
                    a.veredito == VereditoAuditoria.APROVADA || a.veredito == VereditoAuditoria.APROVADA_COM_RESSALVAS).count();
            Map<String, Object> sc = new LinkedHashMap<>();
            sc.put("propostas_registradas", propostas.size());
            sc.put("votos_registrados", votos.size());
            sc.put("cidadaos_ativos", new HashSet<>(votos.stream().map(v -> v.cidadao_id).collect(Collectors.toList())).size());
            sc.put("blocos_detectados", blocosList.size());
            sc.put("indice_divisao", indice_divisao());
            sc.put("indice_tribalismo", indice_tribalismo());
            sc.put("politicas_auditadas", auditorias.size());
            sc.put("politicas_bloqueadas", bloqueadas);
            sc.put("politicas_aprovadas", aprovadas);
            return sc;
        }
    }

    // ============================================================================
    // 5. DEMO (main)
    // ============================================================================

    public static void main(String[] args) {
        AntiPolarizacaoEngine e = new AntiPolarizacaoEngine();

        System.out.println("=".repeat(70));
        System.out.println("OpenAntiPolarization -- P9: O Estado NAO Polariza");
        System.out.println("=".repeat(70));

        // Cenario 1
        System.out.println("\n[CENARIO 1] Assembleia saudavel (dissenso produtivo)");
        PropostaAssembleia p1 = e.registrar_proposta("Construir escola no norte", "", FatorPolarizacao.REGIAO);
        PropostaAssembleia p2 = e.registrar_proposta("Ampliar enfermaria central", "", null);
        PropostaAssembleia p3 = e.registrar_proposta("Importar capoeira como educacao fisica", "", null);
        List<Object[]> lote1 = Arrays.asList(
                new Object[]{"cid_01", p1.id, true}, new Object[]{"cid_02", p1.id, true}, new Object[]{"cid_03", p1.id, false},
                new Object[]{"cid_04", p1.id, true}, new Object[]{"cid_05", p1.id, true},
                new Object[]{"cid_01", p2.id, true}, new Object[]{"cid_02", p2.id, false}, new Object[]{"cid_03", p2.id, true},
                new Object[]{"cid_04", p2.id, true}, new Object[]{"cid_05", p2.id, true},
                new Object[]{"cid_01", p3.id, false}, new Object[]{"cid_02", p3.id, true}, new Object[]{"cid_03", p3.id, true},
                new Object[]{"cid_04", p3.id, false}, new Object[]{"cid_05", p3.id, true}
        );
        e.registrar_votacao_em_lote(lote1);
        MetricaPolarizacao m1 = e.medir_polarizacao("assembleia_norte_v1", null);
        System.out.printf("  Divisao: %.2f | Tribalismo: %.2f%n", m1.indice_divisao, m1.indice_tribalismo);
        System.out.println("  Nivel: " + m1.nivel.rotulo);
        System.out.println("  Veredito: " + m1.veredito);
        System.out.println("  Protocolo: " + e.protocolo_bloqueio(m1).rotulo);

        // Cenario 2
        System.out.println("\n[CENARIO 2] Assembleia polarizada (votacao tribal)");
        AntiPolarizacaoEngine e2 = new AntiPolarizacaoEngine();
        PropostaAssembleia pa = e2.registrar_proposta("Politica A", "", FatorPolarizacao.IDEOLOGIA);
        PropostaAssembleia pb = e2.registrar_proposta("Politica B", "", FatorPolarizacao.IDEOLOGIA);
        PropostaAssembleia pc = e2.registrar_proposta("Politica C", "", FatorPolarizacao.IDEOLOGIA);
        PropostaAssembleia pd = e2.registrar_proposta("Politica D", "", FatorPolarizacao.IDEOLOGIA);
        List<String> bloco_x = new ArrayList<>();
        List<String> bloco_y = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            bloco_x.add(String.format("x_%02d", i));
            bloco_y.add(String.format("y_%02d", i));
        }
        for (PropostaAssembleia prop : Arrays.asList(pa, pb, pc, pd)) {
            for (String cid : bloco_x) e2.registrar_voto(cid, prop.id, true, "");
            for (String cid : bloco_y) e2.registrar_voto(cid, prop.id, false, "");
        }
        List<String> sinais2 = Arrays.asList("voto_identidade", "zero_trust");
        MetricaPolarizacao m2 = e2.medir_polarizacao("assembleia_polarizada", sinais2);
        System.out.printf("  Divisao: %.2f | Tribalismo: %.2f%n", m2.indice_divisao, m2.indice_tribalismo);
        System.out.printf("  Ruptura epistemica: %.2f%n", m2.indice_ruptura_epistemica);
        System.out.println("  Nivel: " + m2.nivel.rotulo);
        System.out.println("  Veredito: " + m2.veredito);
        System.out.println("  Protocolo: " + e2.protocolo_bloqueio(m2).rotulo);
        System.out.println("  Blocos detectados: " + m2.num_blocos);
        System.out.println("  Recomendacoes:");
        for (String r : e2.recomendacoes_mediacao(m2)) System.out.println("    - " + r);

        // Cenario 3
        System.out.println("\n[CENARIO 3] Ruptura epistemica (EMERGENCIA)");
        AntiPolarizacaoEngine e3 = new AntiPolarizacaoEngine();
        for (int i = 0; i < 5; i++) e3.registrar_proposta("Proposta " + i, "", null);
        List<String> todos_sinais = new ArrayList<>(SINAIS_RUPTURA_EPISTEMICA.keySet());
        for (PropostaAssembleia prop : e3.propostas.values()) {
            for (int j = 0; j < 6; j++) {
                e3.registrar_voto("tribo_a_" + j, prop.id, true, "");
                e3.registrar_voto("tribo_b_" + j, prop.id, false, "");
            }
        }
        MetricaPolarizacao m3 = e3.medir_polarizacao("assembleia_ruptura", todos_sinais);
        System.out.printf("  Ruptura epistemica: %.2f%n", m3.indice_ruptura_epistemica);
        System.out.println("  Nivel: " + m3.nivel.rotulo);
        System.out.println("  Protocolo: " + e3.protocolo_bloqueio(m3).rotulo);
        System.out.println("  RECOMENDACOES DE EMERGENCIA:");
        for (String r : e3.recomendacoes_mediacao(m3)) System.out.println("    - " + r);

        // GATE P9
        System.out.println("\n" + "=".repeat(70));
        System.out.println("[GATE P9] Auditoria de politicas publicas");
        System.out.println("=".repeat(70));

        AuditoriaPolitica a1 = e.auditar_politica("pol-escola", "Construir escola no norte",
                "Politica de infraestrutura educacional sem apelo identitario.",
                new ArrayList<>(), Arrays.asList(FatorPolarizacao.REGIAO), null);
        System.out.printf("\n  [%s] %s (score=%.1f)%n", a1.politica_id, a1.veredito.rotulo, a1.score_polarizante);
        System.out.println("    " + a1.justificativa);

        List<TaticaPolarizante> t2 = Arrays.asList(TaticaPolarizante.FEAR_MONGERING);
        AuditoriaPolitica a2 = e.auditar_politica("pol-saude", "Reforma do sistema de saude",
                "Politica com algum alarmismo na apresentacao.", t2, new ArrayList<>(), null);
        System.out.printf("\n  [%s] %s (score=%.1f)%n", a2.politica_id, a2.veredito.rotulo, a2.score_polarizante);
        System.out.println("    " + a2.justificativa);
        for (String mit : a2.mitigacoes) System.out.println("    Mitigacao: " + mit);

        List<TaticaPolarizante> t3 = Arrays.asList(TaticaPolarizante.FALSE_DICHOTOMY, TaticaPolarizante.FEAR_MONGERING);
        AuditoriaPolitica a3 = e.auditar_politica("pol-seguranca", "Lei de seguranca publica",
                "Politica apresentada com falsa dicotomia e alarmismo.", t3, Arrays.asList(FatorPolarizacao.IDEOLOGIA), null);
        System.out.printf("\n  [%s] %s (score=%.1f)%n", a3.politica_id, a3.veredito.rotulo, a3.score_polarizante);
        System.out.println("    " + a3.justificativa);
        for (String mit : a3.mitigacoes) System.out.println("    Mitigacao: " + mit);

        List<TaticaPolarizante> t4 = Arrays.asList(TaticaPolarizante.IDENTITY_BAITING, TaticaPolarizante.OUTGROUP_DEHUMANIZATION, TaticaPolarizante.EPISTEMIC_BALKANIZATION);
        List<FatorPolarizacao> f4 = Arrays.asList(FatorPolarizacao.RELIGIAO, FatorPolarizacao.IDENTIDADE);
        List<String> s4 = Arrays.asList("zero_trust", "purity_test");
        AuditoriaPolitica a4 = e.auditar_politica("pol-identidade", "Declaracao sobre valores culturais",
                "Politica que aciona divisao religiosa e identitaria explicita.", t4, f4, s4);
        System.out.printf("\n  [%s] %s (score=%.1f)%n", a4.politica_id, a4.veredito.rotulo, a4.score_polarizante);
        System.out.println("    " + a4.justificativa);
        for (String mit : a4.mitigacoes) System.out.println("    Mitigacao: " + mit);

        // Scorecard
        System.out.println("\n" + "=".repeat(70));
        System.out.println("[SCORECARD P9]");
        System.out.println("=".repeat(70));
        Map<String, Object> sc = e.scorecard();
        for (Map.Entry<String, Object> entry : sc.entrySet()) {
            System.out.printf("  %s %s%n", String.format("%-28s", entry.getKey() + "."), entry.getValue());
        }

        // Catalogo
        System.out.println("\n[CATALOGO DE TATICAS POLARIZANTES AUDITADAS PELO ESTADO]");
        for (TaticaPolarizante t : TaticaPolarizante.values()) {
            System.out.printf("  [%d] %s%n", t.gravidade, t.rotulo);
        }

        // Sinais
        System.out.println("\n[SINAIS DE RUPTURA EPISTEMICA (monitoramento continuo)]");
        for (Map.Entry<String, String> entry : SINAIS_RUPTURA_EPISTEMICA.entrySet()) {
            System.out.printf("  %s: %s%n", entry.getKey(), entry.getValue());
        }

        // Filosofia
        System.out.println("\n" + "=".repeat(70));
        System.out.println("FILOSOFIA -- P9: Por que o Estado nao pode polarizar");
        System.out.println("=".repeat(70));
        System.out.println("""
DISTINCAO FUNDAMENTAL:
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
""");
    }
}
