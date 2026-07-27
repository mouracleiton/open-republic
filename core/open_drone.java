// Full Java translation of open_drone.py (P10 Soberania Aerea Civica)
// All enums, dataclasses, tables, DroneCivicoEngine, and _demo() faithfully reproduced.
// Comments and strings kept in Portuguese. Runnable demo in main().

import java.time.Instant;
import java.util.*;
import java.util.stream.Collectors;

public class open_drone {

    // ============================================================================
    // 1. ENUMS
    // ============================================================================

    public enum TipoMissao {
        ENTREGA_SUPRIMENTOS("entrega_suprimentos", "Entrega de suprimentos (remedio, comida, agua)", 1),
        MAPEAMENTO_AMBIENTAL("mapeamento_ambiental", "Mapeamento ambiental (desmatamento, queimadas)", 1),
        BUSCA_RESGATE("busca_resgate", "Busca e resgate em desastre natural", 0),
        CONECTIVIDADE("conectividade", "Rede mesh aerea (area sem cobertura)", 1),
        INSPECAO_INFRA("inspecao_infra", "Inspecao de infraestrutura critica", 1),
        AGRICULTURA_CIVICA("agricultura_civica", "Agricultura de precisao comunitaria", 2);

        public final String id;
        public final String rotulo;
        public final int prioridade;

        TipoMissao(String id, String rotulo, int prioridade) {
            this.id = id;
            this.rotulo = rotulo;
            this.prioridade = prioridade;
        }
    }

    public enum StatusMissao {
        PLANEJADA("planejada", "Planejada (aguardando aprovacao do gate)"),
        APROVADA("aprovada", "Aprovada pelo gate P10"),
        EM_VOO("em_voo", "Em voo (executando)"),
        CONCLUIDA("concluida", "Concluida com sucesso"),
        REJEITADA("rejeitada", "Rejeitada pelo gate P10"),
        CANCELADA("cancelada", "Cancelada (emergencia ou erro)"),
        FALHOU("falhou", "Falhou (perda de sinal, aterrissagem forcada)");

        public final String id;
        public final String rotulo;

        StatusMissao(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum TipoProibicao {
        VIGILANCIA("vigilancia", "Camera de vigilancia (feed gravado/transmitido)", 5),
        ARMAMENTO("armamento", "Carrega arma ou explosivo", 5),
        ESPIONAGEM("espionagem", "Coleta dados pessoais (facial, placa, biometria)", 5),
        PRIVADO_SEM_CONSENTIMENTO("privado_sem_consentimento", "Sobrevoa area privada sem consentimento", 4),
        COMERCIAL_NAO_CIVICO("comercial_nao_civico", "Uso comercial sem proposito civico (propaganda)", 3);

        public final String id;
        public final String rotulo;
        public final int gravidade;

        TipoProibicao(String id, String rotulo, int gravidade) {
            this.id = id;
            this.rotulo = rotulo;
            this.gravidade = gravidade;
        }
    }

    public enum VereditoGate {
        APROVADA("aprovada", "Missao aprovada: proposito civico confirmado"),
        APROVADA_COM_RESTRICOES("aprovada_restricoes", "Aprovada com restricoes (geofence ampliado)"),
        REJEITADA("rejeitada", "Missao rejeitada: viola uma proibicao P10"),
        BLOQUEADA("bloqueada", "Missao bloqueada: e vetor de vigilancia/arma");

        public final String id;
        public final String rotulo;

        VereditoGate(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum PrioridadeCorredor {
        RESGATE_VIDA("resgate_vida", "Resgate de vida (emergencia medica)", 0),
        ENTREGA_CRITICA("entrega_critica", "Entrega critica (remedio urgente)", 1),
        MAPEAMENTO_AMBIENTAL("mapeamento", "Mapeamento ambiental de rotina", 2),
        CONECTIVIDADE("conectividade", "Conectividade mesh", 2),
        INSPECAO("inspecao", "Inspecao de infraestrutura", 3),
        OUTROS("outros", "Outros usos civicos", 4);

        public final String id;
        public final String rotulo;
        public final int prioridade;

        PrioridadeCorredor(String id, String rotulo, int prioridade) {
            this.id = id;
            this.rotulo = rotulo;
            this.prioridade = prioridade;
        }
    }

    // ============================================================================
    // 2. DATACLASSES (static inner classes)
    // ============================================================================

    public static class Coordenada {
        public final double lat;
        public final double lon;

        public Coordenada(double lat, double lon) {
            this.lat = lat;
            this.lon = lon;
        }
    }

    public static class ZonaVoo {
        public final String id;
        public final Coordenada centro;
        public final double raio_metros;
        public final String descricao;
        public final boolean sobrevoa_privado;
        public final boolean consentimento_privado;

        public ZonaVoo(String id, Coordenada centro, double raio_metros, String descricao,
                       boolean sobrevoa_privado, boolean consentimento_privado) {
            this.id = id;
            this.centro = centro;
            this.raio_metros = raio_metros;
            this.descricao = descricao == null ? "" : descricao;
            this.sobrevoa_privado = sobrevoa_privado;
            this.consentimento_privado = consentimento_privado;
        }
    }

    public static class Drone {
        public final String id;
        public final String modelo;
        public final int autonomia_minutos;
        public final double carga_max_kg;
        public final boolean tem_camera_navegacao;
        public boolean tem_camera_vigilancia;
        public boolean tem_armamento;
        public boolean coleta_dados_pessoais;
        public boolean ativo;
        public int missoes_concluidas;

        public Drone(String id, String modelo, int autonomia_minutos, double carga_max_kg,
                     boolean tem_camera_navegacao, boolean tem_camera_vigilancia,
                     boolean tem_armamento, boolean coleta_dados_pessoais) {
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

    public static class MissaoDrone {
        public final String id;
        public final String drone_id;
        public final TipoMissao tipo;
        public final String descricao;
        public final ZonaVoo zona;
        public final Coordenada destino;
        public final String carga_descricao;
        public final boolean urgencia;
        public StatusMissao status;
        public VereditoGate veredito_gate;
        public String razao_rejeicao;
        public List<TipoProibicao> proibicoes_violadas;
        public String criada_em;
        public String concluida_em;
        public List<Coordenada> log_trajeto;

        public MissaoDrone(String id, String drone_id, TipoMissao tipo, String descricao, ZonaVoo zona,
                           Coordenada destino, String carga_descricao, boolean urgencia, String criada_em) {
            this.id = id;
            this.drone_id = drone_id;
            this.tipo = tipo;
            this.descricao = descricao;
            this.zona = zona;
            this.destino = destino;
            this.carga_descricao = carga_descricao == null ? "" : carga_descricao;
            this.urgencia = urgencia;
            this.status = StatusMissao.PLANEJADA;
            this.veredito_gate = null;
            this.razao_rejeicao = "";
            this.proibicoes_violadas = new ArrayList<>();
            this.criada_em = criada_em;
            this.concluida_em = "";
            this.log_trajeto = new ArrayList<>();
        }
    }

    public static class LogVoo {
        public final String missao_id;
        public final String drone_id;
        public final String tipo_missao;
        public final double duracao_minutos;
        public final double distancia_km;
        public final String decolagem;
        public final String pouso;
        public final Double destino_lat;
        public final Double destino_lon;
        public final boolean sucesso;
        public final String observacoes;

        public LogVoo(String missao_id, String drone_id, String tipo_missao, double duracao_minutos,
                      double distancia_km, String decolagem, String pouso, Double destino_lat,
                      Double destino_lon, boolean sucesso, String observacoes) {
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
            this.observacoes = observacoes == null ? "" : observacoes;
        }
    }

    public static class MetricaFrota {
        public final String regiao_id;
        public final int total_drones;
        public final int drones_ativos;
        public final int missoes_concluidas;
        public final int missoes_rejeitadas;
        public final int entregas_criticas;
        public final int resgates;
        public final double horas_voo;
        public final int violacoes_detectadas;
        public final double cobertura_km2;

        public MetricaFrota(String regiao_id, int total_drones, int drones_ativos, int missoes_concluidas,
                            int missoes_rejeitadas, int entregas_criticas, int resgates, double horas_voo,
                            int violacoes_detectadas, double cobertura_km2) {
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

    // ============================================================================
    // 3. TABELAS DE PROIBICOES E SALVAGUARDAS
    // ============================================================================

    public static final Map<String, String> DESCRICOES_PROIBICOES = new LinkedHashMap<>();
    static {
        DESCRICOES_PROIBICOES.put("vigilancia",
            "Camera de vigilancia = feed gravado ou transmitido para central de " +
            "monitoramento. PERMITIDO: camera de navegacao (feed local em tempo real, " +
            "nao gravado, processado no proprio drone). A linha e: a camera ajuda o " +
            "drone a voar, nao ajuda o Estado a vigiar.");
        DESCRICOES_PROIBICOES.put("armamento",
            "Qualquer arma, explosivo, ou dispositivo projetado para causar dano " +
            "fisico. Um drone armado nao e drone -- e arma. Armas pertencem ao museu " +
            "da Republica (P7). Sem excecoes, mesmo para 'defesa'.");
        DESCRICOES_PROIBICOES.put("espionagem",
            "Reconhecimento facial, leitura de placas, coleta de biometria, captura " +
            "de dados de rede (wifi bluetooth scanning). O drone entrega suprimentos; " +
            "NAO entrega metadados sobre o destinatario.");
        DESCRICOES_PROIBICOES.put("privado_sem_consentimento",
            "Sobrevoar residencia, patio, ou propriedade privada sem consentimento " +
            "explicito do morador. Excecao: resgate de vida (P1 > privacidade), mas " +
            "o log fica publico e auditavel.");
        DESCRICOES_PROIBICOES.put("comercial_nao_civico",
            "Uso para entrega de consumo de luxo, propaganda, marketing, ou qualquer " +
            "fim que nao reduza miserabilidade ou amplie acesso. Drones nao sao " +
            "brinquedo de consumo -- sao infraestrutura de sobrevivencia.");
    }

    public static final Map<String, Integer> PRIORIDADE_POR_TIPO = new HashMap<>();
    static {
        PRIORIDADE_POR_TIPO.put(TipoMissao.BUSCA_RESGATE.id, 0);
        PRIORIDADE_POR_TIPO.put(TipoMissao.ENTREGA_SUPRIMENTOS.id, 1);
        PRIORIDADE_POR_TIPO.put(TipoMissao.MAPEAMENTO_AMBIENTAL.id, 2);
        PRIORIDADE_POR_TIPO.put(TipoMissao.CONECTIVIDADE.id, 2);
        PRIORIDADE_POR_TIPO.put(TipoMissao.INSPECAO_INFRA.id, 3);
        PRIORIDADE_POR_TIPO.put(TipoMissao.AGRICULTURA_CIVICA.id, 3);
    }

    // ============================================================================
    // 4. ENGINE
    // ============================================================================

    public static class DroneCivicoEngine {
        public Map<String, Drone> drones = new HashMap<>();
        public Map<String, MissaoDrone> missoes = new HashMap<>();
        public Map<String, ZonaVoo> zonas = new HashMap<>();
        public List<LogVoo> logs = new ArrayList<>();
        private int _drone_id = 0;
        private int _missao_id = 0;
        private int _zona_id = 0;

        private String _drone_id_novo() {
            _drone_id++;
            return String.format("DRONE-%04d", _drone_id);
        }

        private String _missao_id_novo() {
            _missao_id++;
            return String.format("MISSAO-%04d", _missao_id);
        }

        private String _zona_id_novo() {
            _zona_id++;
            return String.format("ZONA-%04d", _zona_id);
        }

        public ZonaVoo registrar_zona(Coordenada centro, double raio_metros, String descricao,
                                      boolean sobrevoa_privado, boolean consentimento_privado) {
            ZonaVoo z = new ZonaVoo(_zona_id_novo(), centro, raio_metros,
                    descricao == null ? "" : descricao, sobrevoa_privado, consentimento_privado);
            zonas.put(z.id, z);
            return z;
        }

        public Drone registrar_drone(String modelo, int autonomia_minutos, double carga_max_kg,
                                     boolean tem_camera_navegacao, boolean tem_camera_vigilancia,
                                     boolean tem_armamento, boolean coleta_dados_pessoais) {
            Drone d = new Drone(_drone_id_novo(), modelo, autonomia_minutos, carga_max_kg,
                    tem_camera_navegacao, tem_camera_vigilancia, tem_armamento, coleta_dados_pessoais);
            if (tem_camera_vigilancia || tem_armamento || coleta_dados_pessoais) {
                d.ativo = false;
            }
            drones.put(d.id, d);
            return d;
        }

        public MissaoDrone registrar_missao(String drone_id, TipoMissao tipo, String descricao,
                                            ZonaVoo zona, Coordenada destino, String carga_descricao, boolean urgencia) {
            String criada = Instant.now().toString();
            MissaoDrone m = new MissaoDrone(_missao_id_novo(), drone_id, tipo, descricao, zona,
                    destino, carga_descricao, urgencia, criada);
            missoes.put(m.id, m);
            return m;
        }

        public List<TipoProibicao> auditar_proibicoes(MissaoDrone missao) {
            List<TipoProibicao> violacoes = new ArrayList<>();
            Drone drone = drones.get(missao.drone_id);
            if (drone == null) {
                violacoes.add(TipoProibicao.COMERCIAL_NAO_CIVICO);
                missao.proibicoes_violadas = violacoes;
                return violacoes;
            }
            if (drone.tem_armamento) violacoes.add(TipoProibicao.ARMAMENTO);
            if (drone.tem_camera_vigilancia) violacoes.add(TipoProibicao.VIGILANCIA);
            if (drone.coleta_dados_pessoais) violacoes.add(TipoProibicao.ESPIONAGEM);
            if (missao.zona.sobrevoa_privado && !missao.zona.consentimento_privado) {
                if (missao.tipo != TipoMissao.BUSCA_RESGATE) {
                    violacoes.add(TipoProibicao.PRIVADO_SEM_CONSENTIMENTO);
                }
            }
            if (_verificar_uso_comercial(missao)) {
                violacoes.add(TipoProibicao.COMERCIAL_NAO_CIVICO);
            }
            missao.proibicoes_violadas = violacoes;
            return violacoes;
        }

        private boolean _verificar_uso_comercial(MissaoDrone missao) {
            Set<String> palavras = new HashSet<>(Arrays.asList(
                    "propaganda", "marketing", "publicidade", "luxo", "brinde",
                    "promocional", "black friday", "desconto", "vitrine"));
            String texto = (missao.descricao + " " + missao.carga_descricao).toLowerCase();
            for (String p : palavras) {
                if (texto.contains(p)) return true;
            }
            return false;
        }

        public AbstractMap.SimpleEntry<VereditoGate, String> aprovar_missao(String missao_id) {
            MissaoDrone missao = missoes.get(missao_id);
            if (missao == null) {
                return new AbstractMap.SimpleEntry<>(VereditoGate.REJEITADA, "Missao nao encontrada");
            }
            List<TipoProibicao> violacoes = auditar_proibicoes(missao);
            Drone drone = drones.get(missao.drone_id);

            int gravidade_max = violacoes.stream().mapToInt(v -> v.gravidade).max().orElse(0);
            if (gravidade_max >= 5) {
                missao.veredito_gate = VereditoGate.BLOQUEADA;
                missao.status = StatusMissao.REJEITADA;
                missao.razao_rejeicao = "MISSAO BLOQUEADA: viola proibicao constitucional P10 -- " +
                        violacoes.stream().map(v -> v.rotulo).collect(Collectors.joining(", "));
                return new AbstractMap.SimpleEntry<>(missao.veredito_gate, missao.razao_rejeicao);
            }
            if (!violacoes.isEmpty()) {
                missao.veredito_gate = VereditoGate.REJEITADA;
                missao.status = StatusMissao.REJEITADA;
                missao.razao_rejeicao = "Missao rejeitada: " +
                        violacoes.stream().map(v -> v.rotulo).collect(Collectors.joining(", "));
                return new AbstractMap.SimpleEntry<>(missao.veredito_gate, missao.razao_rejeicao);
            }
            if (drone != null) {
                double dist_estimada = _estimar_distancia(missao);
                double autonomia_necessaria = (dist_estimada / 30.0) * 60;
                if (autonomia_necessaria > drone.autonomia_minutos) {
                    missao.veredito_gate = VereditoGate.APROVADA_COM_RESTRICOES;
                    missao.status = StatusMissao.APROVADA;
                    missao.razao_rejeicao = String.format(
                            "Aprovada com restricoes: autonomia marginal (%.0fmin necessaria vs %dmin disponivel)",
                            autonomia_necessaria, drone.autonomia_minutos);
                    return new AbstractMap.SimpleEntry<>(missao.veredito_gate, missao.razao_rejeicao);
                }
            }
            missao.veredito_gate = VereditoGate.APROVADA;
            missao.status = StatusMissao.APROVADA;
            return new AbstractMap.SimpleEntry<>(missao.veredito_gate, "Missao aprovada pelo gate P10");
        }

        private double _estimar_distancia(MissaoDrone missao) {
            return (missao.zona.raio_metros / 1000.0) * 2.0;
        }

        public boolean decolar(String missao_id) {
            MissaoDrone missao = missoes.get(missao_id);
            if (missao == null || missao.status != StatusMissao.APROVADA) {
                return false;
            }
            missao.status = StatusMissao.EM_VOO;
            return true;
        }

        public LogVoo concluir_missao(String missao_id, double duracao_minutos, double distancia_km,
                                      boolean sucesso, String observacoes) {
            MissaoDrone missao = missoes.get(missao_id);
            if (missao == null || missao.status != StatusMissao.EM_VOO) {
                return null;
            }
            missao.status = sucesso ? StatusMissao.CONCLUIDA : StatusMissao.FALHOU;
            missao.concluida_em = Instant.now().toString();
            Drone drone = drones.get(missao.drone_id);
            if (drone != null && sucesso) {
                drone.missoes_concluidas++;
            }
            LogVoo log = new LogVoo(missao.id, missao.drone_id, missao.tipo.id, duracao_minutos,
                    distancia_km, missao.criada_em, missao.concluida_em,
                    missao.destino != null ? missao.destino.lat : null,
                    missao.destino != null ? missao.destino.lon : null,
                    sucesso, observacoes);
            logs.add(log);
            return log;
        }

        public String resolver_conflito_corredor(String missao_a_id, String missao_b_id) {
            MissaoDrone ma = missoes.get(missao_a_id);
            MissaoDrone mb = missoes.get(missao_b_id);
            if (ma == null || mb == null) return null;
            int pri_a = PRIORIDADE_POR_TIPO.getOrDefault(ma.tipo.id, 4);
            int pri_b = PRIORIDADE_POR_TIPO.getOrDefault(mb.tipo.id, 4);
            if (ma.urgencia && !mb.urgencia) return ma.id;
            if (mb.urgencia && !ma.urgencia) return mb.id;
            if (pri_a < pri_b) return ma.id;
            if (pri_b < pri_a) return mb.id;
            return null;
        }

        public MetricaFrota medir_frota(String regiao_id) {
            int total = drones.size();
            int ativos = (int) drones.values().stream().filter(d -> d.ativo).count();
            int concluidas = (int) missoes.values().stream().filter(m -> m.status == StatusMissao.CONCLUIDA).count();
            int rejeitadas = (int) missoes.values().stream().filter(m -> m.status == StatusMissao.REJEITADA).count();
            int entregas = (int) missoes.values().stream()
                    .filter(m -> m.status == StatusMissao.CONCLUIDA && m.tipo == TipoMissao.ENTREGA_SUPRIMENTOS).count();
            int resgates = (int) missoes.values().stream()
                    .filter(m -> m.status == StatusMissao.CONCLUIDA && m.tipo == TipoMissao.BUSCA_RESGATE).count();
            double horas = logs.stream().mapToDouble(l -> l.duracao_minutos).sum() / 60.0;
            int violacoes = missoes.values().stream().mapToInt(m -> m.proibicoes_violadas.size()).sum();
            double cobertura = zonas.values().stream().mapToDouble(z -> z.raio_metros * z.raio_metros * 3.14159).sum() / 1_000_000;
            return new MetricaFrota(regiao_id == null ? "default" : regiao_id, total, ativos, concluidas, rejeitadas,
                    entregas, resgates, Math.round(horas * 10.0) / 10.0, violacoes, Math.round(cobertura * 100.0) / 100.0);
        }

        public Map<String, Object> scorecard() {
            MetricaFrota f = medir_frota("default");
            Map<String, Object> sc = new LinkedHashMap<>();
            sc.put("drones_registrados", f.total_drones);
            sc.put("drones_ativos", f.drones_ativos);
            sc.put("drones_bloqueados", f.total_drones - f.drones_ativos);
            sc.put("missoes_concluidas", f.missoes_concluidas);
            sc.put("missoes_rejeitadas", f.missoes_rejeitadas);
            sc.put("entregas_criticas", f.entregas_criticas);
            sc.put("resgates_realizados", f.resgates);
            sc.put("horas_voo_total", f.horas_voo);
            sc.put("violacoes_detectadas", f.violacoes_detectadas);
            sc.put("cobertura_km2", f.cobertura_km2);
            int denom = Math.max(f.missoes_concluidas + f.missoes_rejeitadas, 1);
            sc.put("taxa_aprovacao", String.format("%.1f%%", (f.missoes_concluidas * 100.0 / denom)));
            return sc;
        }
    }

    // ============================================================================
    // 5. DEMO (main)
    // ============================================================================

    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("OpenDrone -- P10: Soberania Aerea Civica");
        System.out.println("=".repeat(70));

        DroneCivicoEngine e = new DroneCivicoEngine();

        // --- Registrar drones ---
        System.out.println("\n[FROTA] Registrando drones civicos");
        Drone d1 = e.registrar_drone("Teia-Entrega-1", 45, 2.0, true, false, false, false);
        System.out.printf("  %s: %s (carga %.1fkg, %dmin)%n", d1.id, d1.modelo, d1.carga_max_kg, d1.autonomia_minutos);

        Drone d2 = e.registrar_drone("Teia-Resgate-1", 60, 5.0, true, false, false, false);
        System.out.printf("  %s: %s (carga %.1fkg, %dmin)%n", d2.id, d2.modelo, d2.carga_max_kg, d2.autonomia_minutos);

        Drone d_vigia = e.registrar_drone("Teia-Vigia-ILEGAL", 90, 3.0, true, true, false, false);
        System.out.printf("  %s: %s -- DESATIVADO (viola P10: camera de vigilancia)%n", d_vigia.id, d_vigia.modelo);

        Drone d_arma = e.registrar_drone("Teia-Guerreiro-ILEGAL", 30, 1.0, true, false, true, false);
        System.out.printf("  %s: %s -- DESATIVADO (viola P10: armamento)%n", d_arma.id, d_arma.modelo);

        // --- Registrar zonas ---
        System.out.println("\n[ZONAS] Geofencing de areas de voo");
        ZonaVoo z_norte = e.registrar_zona(new Coordenada(-3.0, -60.0), 5000,
                "Comunidade ribeirinha Rio Negro (acesso so por barco/drone)", false, false);
        System.out.printf("  %s: %s (raio %.0fm)%n", z_norte.id, z_norte.descricao, z_norte.raio_metros);

        ZonaVoo z_privada = e.registrar_zona(new Coordenada(-23.5, -46.6), 2000,
                "Area urbana residencial (consentimento necessario)", true, false);
        System.out.printf("  %s: %s (SOBREVOA PRIVADO, sem consentimento)%n", z_privada.id, z_privada.descricao);

        // CENARIO 1
        System.out.println("\n" + "=".repeat(70));
        System.out.println("[CENARIO 1] Entrega de medicamentos em area isolada");
        System.out.println("=".repeat(70));
        MissaoDrone m1 = e.registrar_missao(d1.id, TipoMissao.ENTREGA_SUPRIMENTOS,
                "Entrega de insulina para comunidade ribeirinha isolada", z_norte,
                new Coordenada(-3.1, -60.1), "10 frascos de insulina + antibioticos", true);
        var v1 = e.aprovar_missao(m1.id);
        System.out.printf("  Missao: %s%n", m1.id);
        System.out.printf("  Veredito: %s%n", v1.getKey().rotulo);
        System.out.printf("  Detalhe: %s%n", v1.getValue());

        // CENARIO 2
        System.out.println("\n[CENARIO 2] Tentativa de missao de vigilancia (DEVE SER BLOQUEADA)");
        System.out.println("=".repeat(70));
        MissaoDrone m2 = e.registrar_missao(d_vigia.id, TipoMissao.MAPEAMENTO_AMBIENTAL,
                "Mapeamento (mas drone tem camera de vigilancia)", z_norte, null, "", false);
        var v2 = e.aprovar_missao(m2.id);
        System.out.printf("  Missao: %s (drone: %s)%n", m2.id, d_vigia.id);
        System.out.printf("  Veredito: %s%n", v2.getKey().rotulo);
        System.out.printf("  Detalhe: %s%n", v2.getValue());
        System.out.printf("  Proibicoes violadas: %s%n",
                m2.proibicoes_violadas.stream().map(p -> p.rotulo).collect(Collectors.joining(", ")));

        // CENARIO 3
        System.out.println("\n[CENARIO 3] Tentativa de missao com drone armado (BLOQUEIO ABSOLUTO)");
        System.out.println("=".repeat(70));
        MissaoDrone m3 = e.registrar_missao(d_arma.id, TipoMissao.BUSCA_RESGATE,
                "Resgate (mas drone esta armado -- mascara civica)", z_norte, null, "", true);
        var v3 = e.aprovar_missao(m3.id);
        System.out.printf("  Missao: %s (drone: %s)%n", m3.id, d_arma.id);
        System.out.printf("  Veredito: %s%n", v3.getKey().rotulo);
        System.out.printf("  Detalhe: %s%n", v3.getValue());
        System.out.printf("  Proibicoes violadas: %s%n",
                m3.proibicoes_violadas.stream().map(p -> p.rotulo).collect(Collectors.joining(", ")));

        // CENARIO 4
        System.out.println("\n[CENARIO 4] Missao sobre area privada sem consentimento");
        System.out.println("=".repeat(70));
        MissaoDrone m4 = e.registrar_missao(d1.id, TipoMissao.INSPECAO_INFRA,
                "Inspecao de instalacoes (mas sobrevoa casas sem consentimento)", z_privada, null, "", false);
        var v4 = e.aprovar_missao(m4.id);
        System.out.printf("  Missao: %s%n", m4.id);
        System.out.printf("  Veredito: %s%n", v4.getKey().rotulo);
        System.out.printf("  Detalhe: %s%n", v4.getValue());

        // CENARIO 5
        System.out.println("\n[CENARIO 5] Entrega comercial disfarcada de civica (DEVE SER REJEITADA)");
        System.out.println("=".repeat(70));
        MissaoDrone m5 = e.registrar_missao(d1.id, TipoMissao.ENTREGA_SUPRIMENTOS,
                "Entrega de brinde promocional de black friday", z_norte, null, "Caixa de marketing da empresa XYZ", false);
        var v5 = e.aprovar_missao(m5.id);
        System.out.printf("  Missao: %s%n", m5.id);
        System.out.printf("  Veredito: %s%n", v5.getKey().rotulo);
        System.out.printf("  Detalhe: %s%n", v5.getValue());

        // EXECUCAO
        System.out.println("\n[EXECUCAO] Concluindo missao aprovada do CENARIO 1");
        e.decolar(m1.id);
        LogVoo log1 = e.concluir_missao(m1.id, 18.5, 9.2, true, "Insulina entregue. Comunidade confirmou recebimento.");
        if (log1 != null) {
            System.out.printf("  Log gerado: %s | %.1fmin | %.1fkm%n", log1.missao_id, log1.duracao_minutos, log1.distancia_km);
        }

        // CORREDOR
        System.out.println("\n[CORREDOR AEREO] Resolvendo conflito entre duas missoes");
        MissaoDrone m_resgate = e.registrar_missao(d2.id, TipoMissao.BUSCA_RESGATE,
                "Resgate de crianca em enchente", z_norte, null, "", true);
        MissaoDrone m_inspecao = e.registrar_missao(d1.id, TipoMissao.INSPECAO_INFRA,
                "Inspecao de ponte de rotina", z_norte, null, "", false);
        String prioritario = e.resolver_conflito_corredor(m_resgate.id, m_inspecao.id);
        System.out.printf("  Conflito entre %s (resgate urgente) e %s (inspecao)%n", m_resgate.id, m_inspecao.id);
        System.out.printf("  Prioritario: %s (resgate de vida > inspecao de rotina)%n", prioritario);

        // SCORECARD
        System.out.println("\n" + "=".repeat(70));
        System.out.println("[SCORECARD P10]");
        System.out.println("=".repeat(70));
        Map<String, Object> sc = e.scorecard();
        for (Map.Entry<String, Object> entry : sc.entrySet()) {
            System.out.printf("  %s %s%n", String.format("%-28s", entry.getKey() + "."), entry.getValue());
        }

        // CATALOGO
        System.out.println("\n[CATALOGO DE PROIBICOES CONSTITUCIONAIS P10]");
        for (TipoProibicao p : TipoProibicao.values()) {
            String desc = DESCRICOES_PROIBICOES.getOrDefault(p.id, "");
            System.out.printf("\n  [%d] %s%n", p.gravidade, p.rotulo);
            System.out.printf("      %s%n", desc);
        }

        // LOGS
        System.out.println("\n[LOG PUBLICO DE VOOS (transparencia P10)]");
        for (LogVoo log : e.logs) {
            System.out.printf("  %s | %s | %.1fmin | %.1fkm | sucesso=%s%n",
                    log.missao_id, log.tipo_missao, log.duracao_minutos, log.distancia_km, log.sucesso);
        }

        // FILOSOFIA
        System.out.println("\n" + "=".repeat(70));
        System.out.println("FILOSOFIA -- P10: Por que o ceu nao vigia");
        System.out.println("=".repeat(70));
        System.out.println("""
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
""");
    }
}