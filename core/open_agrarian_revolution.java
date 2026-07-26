// OpenAgrarianRevolution.java
// Transpilacao fiel do Python para Java
// Comentarios e strings em Portugues (conforme fonte)

import java.util.*;
import java.util.stream.Collectors;

public class OpenAgrarianRevolution {

    // ============================================================================
    // 1. ENUMS
    // ============================================================================

    public enum TipoTenencia {
        GUARDIAO_FAMILIAR("guardiao_familiar", "Guardiao familiar", 1),
        COOPERATIVA("cooperativa", "Cooperativa agricola", 5),
        COMUNIDADE_TRADICIONAL("comunidade_tradicional", "Comunidade tradicional (quilombo/ribeirinho/aldeia)", 10),
        ASSENTAMENTO_COLETIVO("assentamento_coletivo", "Assentamento coletivo da Republica", 8),
        RESERVA_REGENERACAO("reserva_regeneracao", "Reserva de regeneracao do solo (repouso)", 0),
        USO_PUBLICO("uso_publico", "Uso publico (escola, enfermaria, mercado)", 0);

        public final String id;
        public final String rotulo;
        public final int familias_max;

        TipoTenencia(String id, String rotulo, int familias_max) {
            this.id = id;
            this.rotulo = rotulo;
            this.familias_max = familias_max;
        }
    }

    public enum UsoSolo {
        LAVOURA_ALIMENTACAO("lavoura_alimentacao", "Lavoura de alimentos basicos"),
        LAVOURA_DIVERSIFICADA("lavoura_diversificada", "Policultivo diversificado"),
        PASTAGEM_REGENERATIVA("pastagem_regenerativa", "Pastagem rotativa regenerativa"),
        AGROFLORESTA("agrofloresta", "Sistema agroflorestal (SAF)"),
        HORTA_COMUNITARIA("horta_comunitaria", "Horta comunitaria de bairro"),
        POMAR("pomar", "Pomar frutifero"),
        RESERVA_NATIVA("reserva_nativa", "Reserva de vegetacao nativa"),
        CULTURA_TRADICIONAL("cultura_tradicional", "Cultivo tradicional ancestral"),
        INFRAESTRUTURA("infraestrutura", "Infraestrutura (casa, galpao, escola)"),
        OCIOSO("ocioso", "Ocioso (sem funcao social)");

        public final String id;
        public final String rotulo;

        UsoSolo(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum StatusReforma {
        DIAGNOSTICO("diagnostico", "Diagnostico fundiario em curso"),
        NOTIFICACAO("notificacao", "Latifundio notificado (funcao social cobrada)"),
        DESAPROPRIACAO("desapropriacao", "Desapropriacao decidida em assembleia"),
        ASSENTAMENTO("assentamento", "Familias assentadas como guardias"),
        REGULARIZACAO("regularizacao", "Regularizacao cooperativa ativa"),
        CONSOLIDADO("consolidado", "Territorio consolidado (auto-gestionario)"),
        CONFLITO("conflito", "Conflito fundiario ativo (grileiro/invasao)");

        public final String id;
        public final String rotulo;

        StatusReforma(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum TipoConflito {
        GRILAGEM("grilagem", "Grilagem (falsificacao de titulo)", 4),
        INVASAO_LATIFUNDIO("invasao_latifundio", "Trabalhador expulso por latifundio", 5),
        TRABALHO_ESCRAVO("trabalho_escravo", "Trabalho analogo a escravidao", 5),
        DESPEJO("despejo", "Despejo de familia guardi", 4),
        CONFLITO_FRONTEIRA("conflito_fronteira", "Disputa de fronteira entre comunidades", 2),
        MINERACAO_ILEGAL("mineracao_ilegal", "Mineracao/predacao ilegal em terra guardia", 4),
        AGROTOXICO("agrotoxico", "Contaminacao por agrotoxico vizinho", 3),
        QUEIMADA_CRIMINOSA("queimada_criminosa", "Queimada criminosa / desmatamento", 4);

        public final String id;
        public final String rotulo;
        public final int gravidade;

        TipoConflito(String id, String rotulo, int gravidade) {
            this.id = id;
            this.rotulo = rotulo;
            this.gravidade = gravidade;
        }
    }

    public enum TamanhoImovel {
        MINIFUNDIO("minifundio", "Minifundio (insuficiente, < 1 modulo)", 0, 50),
        PEQUENO("pequeno", "Pequena area (1-4 modulos)", 50, 200),
        MEDIO("medio", "Media area (4-15 modulos)", 200, 750),
        LATIFUNDIO_DIMENSAO("latifundio_dimensao", "Latifundio por dimensao (>15 modulos)", 750, 99999),
        LATIFUNDIO_EXPLORACAO("latifundio_exploracao", "Latifundio por exploracao (ocioso/grilado)", 0, 99999);

        public final String id;
        public final String rotulo;
        public final double area_min;
        public final double area_max;

        TamanhoImovel(String id, String rotulo, double area_min, double area_max) {
            this.id = id;
            this.rotulo = rotulo;
            this.area_min = area_min;
            this.area_max = area_max;
        }
    }

    public enum FuncaoSocialStatus {
        CUMPRE("cumpre", "Cumpre funcao social"),
        PARCIAL("parcial", "Cumpre parcialmente"),
        DESCUMPRE("descumpre", "Descumpre funcao social");

        public final String id;
        public final String rotulo;

        FuncaoSocialStatus(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum PlanoAgrologia {
        PLANTIO_DIRETO("plantio_direto", "Plantio direto (nao revolver solo)"),
        ADUBACAO_VERDE("adubacao_verde", "Adubacao verde (leguminosas)"),
        COMPOSTAGEM("compostagem", "Compostagem comunitaria"),
        ROTACAO_CULTURAS("rotacao_culturas", "Rotacao de culturas"),
        CICLO_FECHADO("ciclo_fechado", "Ciclo fechado (zero insumo externo)"),
        AGROFLORESTA_SUCSSIONAL("agrofloresta_sucessional", "Agrofloresta sucessional"),
        CAPTACAO_CHUVA("captacao_chuva", "Captacao de agua de chuva"),
        BIOINSUMOS("bioinsumos", "Bioinsumos (proibido agrotoxico sintetico)"),
        INTEGRACAO_ANIMAL("integracao_animal", "Integracao lavoura-pecuaria-floresta");

        public final String id;
        public final String rotulo;

        PlanoAgrologia(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    // ============================================================================
    // 2. DATACLASSES (static inner classes)
    // ============================================================================

    public static class ImovelRural {
        public String id;
        public String nome;
        public double area_hectares;
        public String municipio;
        public String bioma;
        public TipoTenencia tipo_tenencia;
        public List<UsoSolo> usos_solo = new ArrayList<>();
        public int familias_guardias = 0;
        public FuncaoSocialStatus funcao_social = FuncaoSocialStatus.DESCUMPRE;
        public double produtividade_pct = 0.0;
        public List<PlanoAgrologia> plano_agrologia = new ArrayList<>();
        public StatusReforma status = StatusReforma.DIAGNOSTICO;
        public String historico_antigo = "";

        public ImovelRural(String id, String nome, double area_hectares, String municipio, String bioma,
                           TipoTenencia tipo_tenencia, List<UsoSolo> usos_solo, int familias_guardias,
                           FuncaoSocialStatus funcao_social, double produtividade_pct,
                           List<PlanoAgrologia> plano_agrologia, StatusReforma status, String historico_antigo) {
            this.id = id;
            this.nome = nome;
            this.area_hectares = area_hectares;
            this.municipio = municipio;
            this.bioma = bioma;
            this.tipo_tenencia = tipo_tenencia;
            if (usos_solo != null) this.usos_solo = new ArrayList<>(usos_solo);
            this.familias_guardias = familias_guardias;
            this.funcao_social = funcao_social;
            this.produtividade_pct = produtividade_pct;
            if (plano_agrologia != null) this.plano_agrologia = new ArrayList<>(plano_agrologia);
            this.status = status;
            this.historico_antigo = historico_antigo;
        }
    }

    public static class FamiliaGuardia {
        public String id;
        public String nome_referencia;
        public int pessoas;
        public double parcela_hectares;
        public String cooperativa_id = null;
        public String chegada_de = "";
        public boolean conhecimento_tradicional = false;

        public FamiliaGuardia(String id, String nome_referencia, int pessoas, double parcela_hectares,
                              String cooperativa_id, String chegada_de, boolean conhecimento_tradicional) {
            this.id = id;
            this.nome_referencia = nome_referencia;
            this.pessoas = pessoas;
            this.parcela_hectares = parcela_hectares;
            this.cooperativa_id = cooperativa_id;
            this.chegada_de = chegada_de;
            this.conhecimento_tradicional = conhecimento_tradicional;
        }
    }

    public static class ConflitoFundiario {
        public String id;
        public TipoConflito tipo;
        public String territorio_id;
        public int vitimas = 0;
        public int familias_afetadas = 0;
        public String descricao = "";
        public String resolucao_proposta = "";
        public boolean resolvido = false;

        public ConflitoFundiario(String id, TipoConflito tipo, String territorio_id, int vitimas,
                                 int familias_afetadas, String descricao) {
            this.id = id;
            this.tipo = tipo;
            this.territorio_id = territorio_id;
            this.vitimas = vitimas;
            this.familias_afetadas = familias_afetadas;
            this.descricao = descricao;
        }
    }

    public static class CooperativaAgricola {
        public String id;
        public String nome;
        public List<String> familia_ids = new ArrayList<>();
        public List<String> territorio_ids = new ArrayList<>();
        public String excedente_destino = "";
        public List<String> ferramentas_compartilhadas = new ArrayList<>();

        public CooperativaAgricola(String id, String nome, List<String> familia_ids, List<String> territorio_ids,
                                   String excedente_destino, List<String> ferramentas_compartilhadas) {
            this.id = id;
            this.nome = nome;
            if (familia_ids != null) this.familia_ids = new ArrayList<>(familia_ids);
            if (territorio_ids != null) this.territorio_ids = new ArrayList<>(territorio_ids);
            this.excedente_destino = excedente_destino;
            if (ferramentas_compartilhadas != null) this.ferramentas_compartilhadas = new ArrayList<>(ferramentas_compartilhadas);
        }
    }

    public static class DiagnosticoFundiario {
        public String territorio;
        public double total_area;
        public int num_imoveis;
        public double indice_gini;
        public double pct_area_latifundio;
        public int familias_sem_terra;
        public int familias_guardias;
        public String veredito = "";

        public DiagnosticoFundiario(String territorio, double total_area, int num_imoveis, double indice_gini,
                                    double pct_area_latifundio, int familias_sem_terra, int familias_guardias, String veredito) {
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

    // ============================================================================
    // 3. ENGINE
    // ============================================================================

    public static class ReformaAgrariaEngine {
        public Map<String, ImovelRural> imoveis = new HashMap<>();
        public Map<String, FamiliaGuardia> familias = new HashMap<>();
        public Map<String, CooperativaAgricola> cooperativas = new HashMap<>();
        public Map<String, ConflitoFundiario> conflitos = new HashMap<>();
        private int _im_id = 0;
        private int _fam_id = 0;
        private int _coop_counter = 0;
        private int _conf_id = 0;

        private String _imovel_id() {
            _im_id++;
            return String.format("TER-%04d", _im_id);
        }

        private String _familia_id() {
            _fam_id++;
            return String.format("FAM-%04d", _fam_id);
        }

        private String _coop_id() {
            _coop_counter++;
            return String.format("COOP-%04d", _coop_counter);
        }

        private String _conflito_id() {
            _conf_id++;
            return String.format("CONF-%04d", _conf_id);
        }

        public ImovelRural cadastrar_imovel(String nome, double area_hectares, String municipio, String bioma,
                                            TipoTenencia tipo_tenencia, List<UsoSolo> usos_solo, int familias_guardias,
                                            FuncaoSocialStatus funcao_social, double produtividade_pct,
                                            List<PlanoAgrologia> plano, StatusReforma status, String historico_antigo) {
            ImovelRural im = new ImovelRural(_imovel_id(), nome, area_hectares, municipio, bioma, tipo_tenencia,
                    usos_solo, familias_guardias, funcao_social, produtividade_pct, plano, status, historico_antigo);
            imoveis.put(im.id, im);
            return im;
        }

        public FamiliaGuardia cadastrar_familia(String nome_referencia, int pessoas, double parcela_hectares,
                                                String cooperativa_id, String chegada_de, boolean conhecimento_tradicional) {
            FamiliaGuardia f = new FamiliaGuardia(_familia_id(), nome_referencia, pessoas, parcela_hectares,
                    cooperativa_id, chegada_de, conhecimento_tradicional);
            familias.put(f.id, f);
            return f;
        }

        public CooperativaAgricola criar_cooperativa(String nome, List<String> familia_ids, List<String> territorio_ids,
                                                     String excedente_destino, List<String> ferramentas) {
            CooperativaAgricola c = new CooperativaAgricola(_coop_id(), nome, familia_ids, territorio_ids,
                    excedente_destino, ferramentas);
            cooperativas.put(c.id, c);
            for (String fid : familia_ids) {
                if (familias.containsKey(fid)) {
                    familias.get(fid).cooperativa_id = c.id;
                }
            }
            return c;
        }

        public ConflitoFundiario registrar_conflito(TipoConflito tipo, String territorio_id, int vitimas,
                                                    int familias_afetadas, String descricao) {
            ConflitoFundiario c = new ConflitoFundiario(_conflito_id(), tipo, territorio_id, vitimas, familias_afetadas, descricao);
            conflitos.put(c.id, c);
            return c;
        }

        public TamanhoImovel classificar_tamanho(double area, boolean ocioso) {
            if (ocioso && area >= TamanhoImovel.PEQUENO.area_min) {
                return TamanhoImovel.LATIFUNDIO_EXPLORACAO;
            }
            for (TamanhoImovel t : new TamanhoImovel[]{TamanhoImovel.MINIFUNDIO, TamanhoImovel.PEQUENO,
                    TamanhoImovel.MEDIO, TamanhoImovel.LATIFUNDIO_DIMENSAO}) {
                if (t.area_min <= area && area < t.area_max) {
                    return t;
                }
            }
            return TamanhoImovel.LATIFUNDIO_DIMENSAO;
        }

        public double indice_gini_areas() {
            List<Double> areas = new ArrayList<>();
            for (ImovelRural im : imoveis.values()) areas.add(im.area_hectares);
            int n = areas.size();
            if (n == 0) return 0.0;
            double total = 0.0;
            for (double a : areas) total += a;
            if (total == 0) return 0.0;
            double soma_pond = 0.0;
            for (int i = 0; i < n; i++) {
                soma_pond += (i + 1) * areas.get(i);
            }
            double gini = (2 * soma_pond) / (n * total) - (n + 1.0) / n;
            return Math.round(gini * 10000.0) / 10000.0;
        }

        public DiagnosticoFundiario diagnosticar(String territorio) {
            List<ImovelRural> ims = new ArrayList<>();
            for (ImovelRural im : imoveis.values()) {
                if (im.municipio.equals(territorio)) ims.add(im);
            }
            double total_area = 0.0;
            for (ImovelRural im : ims) total_area += im.area_hectares;
            int num = ims.size();
            if (num == 0) {
                return new DiagnosticoFundiario(territorio, 0.0, 0, 0.0, 0.0, 0, 0, "Territorio vazio no cadastro.");
            }
            double gini = indice_gini_areas();
            double area_lat = 0.0;
            for (ImovelRural im : ims) {
                boolean ocioso = (im.funcao_social == FuncaoSocialStatus.DESCUMPRE);
                TamanhoImovel tam = classificar_tamanho(im.area_hectares, ocioso);
                if (tam == TamanhoImovel.LATIFUNDIO_DIMENSAO || tam == TamanhoImovel.LATIFUNDIO_EXPLORACAO) {
                    area_lat += im.area_hectares;
                }
            }
            double pct_lat = (total_area > 0) ? (area_lat / total_area * 100.0) : 0.0;
            int familias_guardias = 0;
            for (ImovelRural im : ims) familias_guardias += im.familias_guardias;
            int familias_sem_terra = Math.max(0, (int) ((pct_lat / 100.0) * familias_guardias / 4));
            String veredito;
            if (gini > 0.7 || pct_lat > 50) {
                veredito = "CONCENTRACAO CRITICA: revolicao agraria URGENTE.";
            } else if (gini > 0.4 || pct_lat > 25) {
                veredito = "CONCENTRACAO ALTA: notificar latifundios, cobrar funcao social.";
            } else if (gini > 0.2) {
                veredito = "CONCENTRACAO MODERADA: regularizar e cooperativizar.";
            } else {
                veredito = "TERRITORIO EQUITATIVO: consolidar cooperativas.";
            }
            return new DiagnosticoFundiario(territorio, total_area, num, gini, Math.round(pct_lat * 10.0) / 10.0,
                    familias_sem_terra, familias_guardias, veredito);
        }

        public Object[] auditar_funcao_social(String imovel_id) {
            ImovelRural im = imoveis.get(imovel_id);
            if (im == null) {
                return new Object[]{FuncaoSocialStatus.DESCUMPRE, Collections.singletonList("Imovel nao encontrado.")};
            }
            List<String> faltas = new ArrayList<>();
            if (im.produtividade_pct < 40) {
                faltas.add(String.format("Produtividade baixa (%.0f%% do potencial).", im.produtividade_pct));
            }
            if (im.plano_agrologia.isEmpty()) {
                faltas.add("Sem plano de agrologia (solo sendo exaurido).");
            }
            for (ConflitoFundiario conf : conflitos.values()) {
                if (conf.tipo == TipoConflito.TRABALHO_ESCRAVO && conf.territorio_id.equals(im.id) && !conf.resolvido) {
                    faltas.add("Trabalho analogo a escravidao detectado (BLOQUEANTE).");
                    break;
                }
            }
            if (im.familias_guardias == 0 && im.tipo_tenencia != TipoTenencia.RESERVA_REGENERACAO) {
                faltas.add("Nenhuma familia guardia: terra abandonada.");
            }
            if (!faltas.isEmpty()) {
                im.funcao_social = (faltas.size() == 1) ? FuncaoSocialStatus.PARCIAL : FuncaoSocialStatus.DESCUMPRE;
            } else {
                im.funcao_social = FuncaoSocialStatus.CUMPRE;
            }
            return new Object[]{im.funcao_social, faltas};
        }

        public String notificar_latifundio(String imovel_id) {
            ImovelRural im = imoveis.get(imovel_id);
            if (im == null) return null;
            boolean ocioso = (im.funcao_social == FuncaoSocialStatus.DESCUMPRE);
            TamanhoImovel tam = classificar_tamanho(im.area_hectares, ocioso);
            if (tam != TamanhoImovel.LATIFUNDIO_DIMENSAO && tam != TamanhoImovel.LATIFUNDIO_EXPLORACAO) {
                return im.id + " nao e latifundio (" + tam.rotulo + ").";
            }
            Object[] audit = auditar_funcao_social(im.id);
            FuncaoSocialStatus status = (FuncaoSocialStatus) audit[0];
            @SuppressWarnings("unchecked")
            List<String> faltas = (List<String>) audit[1];
            if (status == FuncaoSocialStatus.CUMPRE) {
                im.status = StatusReforma.REGULARIZACAO;
                return im.id + " cumpre funcao social -> regularizar como cooperativa.";
            }
            im.status = StatusReforma.NOTIFICACAO;
            String faltasStr = faltas.isEmpty() ? "none" : String.join("; ", faltas);
            return "NOTIFICADO " + im.id + " (" + tam.rotulo + ", " + String.format("%.0f", im.area_hectares) + " ha). " +
                    "Faltas: " + faltasStr + ". Prazo para regularizar.";
        }

        public String desaproropriar(String imovel_id, List<String> familias_assentar) {
            ImovelRural im = imoveis.get(imovel_id);
            if (im == null) return null;
            if (im.status != StatusReforma.NOTIFICACAO && im.status != StatusReforma.DIAGNOSTICO) {
                return im.id + " em status " + im.status.rotulo + " -- nao elegivel para desapropriacao agora.";
            }
            im.historico_antigo = (im.historico_antigo == null || im.historico_antigo.isEmpty()) ? im.nome : im.historico_antigo;
            im.nome = "Territorio Livre " + im.id;
            im.tipo_tenencia = TipoTenencia.ASSENTAMENTO_COLETIVO;
            if (!familias_assentar.isEmpty()) {
                double parcela = im.area_hectares / familias_assentar.size();
                for (String fid : familias_assentar) {
                    FamiliaGuardia fam = familias.get(fid);
                    if (fam != null) {
                        fam.parcela_hectares = Math.round(parcela * 100.0) / 100.0;
                        fam.chegada_de = "assentamento";
                    }
                }
                im.familias_guardias = familias_assentar.size();
            }
            im.status = StatusReforma.ASSENTAMENTO;
            im.funcao_social = FuncaoSocialStatus.PARCIAL;
            return "DESAPROPRIVADO " + im.id + ": " + familias_assentar.size() + " familias guardias assentadas, " +
                    String.format("%.0f", im.area_hectares) + " ha sob cuidado coletivo.";
        }

        public CooperativaAgricola consolidar_cooperativa(String nome, List<String> territorio_ids, List<String> familias_ids,
                                                          String excedente, List<String> ferramentas) {
            CooperativaAgricola coop = criar_cooperativa(nome, familias_ids, territorio_ids, excedente, ferramentas);
            for (String tid : territorio_ids) {
                ImovelRural im = imoveis.get(tid);
                if (im != null) {
                    im.tipo_tenencia = TipoTenencia.COOPERATIVA;
                    im.status = StatusReforma.CONSOLIDADO;
                    im.funcao_social = FuncaoSocialStatus.CUMPRE;
                }
            }
            return coop;
        }

        public List<ConflitoFundiario> conflitos_por_gravidade() {
            List<ConflitoFundiario> list = new ArrayList<>(conflitos.values());
            list.sort((c1, c2) -> {
                int g = Integer.compare(c2.tipo.gravidade, c1.tipo.gravidade);
                if (g != 0) return g;
                return Integer.compare(c2.familias_afetadas, c1.familias_afetadas);
            });
            return list;
        }

        public boolean resolver_conflito(String conflito_id, String resolucao) {
            ConflitoFundiario c = conflitos.get(conflito_id);
            if (c == null) return false;
            c.resolucao_proposta = resolucao;
            c.resolvido = true;
            return true;
        }

        public double area_total() {
            double total = 0.0;
            for (ImovelRural im : imoveis.values()) total += im.area_hectares;
            return total;
        }

        public double area_ociosa() {
            double total = 0.0;
            for (ImovelRural im : imoveis.values()) {
                if (im.funcao_social == FuncaoSocialStatus.DESCUMPRE) total += im.area_hectares;
            }
            return total;
        }

        public int familias_atendidas() {
            int total = 0;
            for (ImovelRural im : imoveis.values()) total += im.familias_guardias;
            return total;
        }

        public int pessoas_atendidas() {
            int total = 0;
            for (ImovelRural im : imoveis.values()) {
                total += im.familias_guardias * 4;
            }
            return total;
        }

        public Map<String, Object> scorecard() {
            Map<String, Object> sc = new LinkedHashMap<>();
            sc.put("imoveis_cadastrados", imoveis.size());
            sc.put("area_total_ha", Math.round(area_total() * 10.0) / 10.0);
            sc.put("area_ociosa_ha", Math.round(area_ociosa() * 10.0) / 10.0);
            double pct = (area_total() > 0) ? Math.round((area_ociosa() / area_total() * 100) * 10.0) / 10.0 : 0.0;
            sc.put("pct_ociosa", pct);
            sc.put("familias_guardias", familias_atendidas());
            sc.put("cooperativas", cooperativas.size());
            long conflitos_abertos = conflitos.values().stream().filter(c -> !c.resolvido).count();
            sc.put("conflitos_abertos", (int) conflitos_abertos);
            sc.put("indice_gini", indice_gini_areas());
            long consolidados = imoveis.values().stream().filter(im -> im.status == StatusReforma.CONSOLIDADO).count();
            sc.put("consolidados", (int) consolidados);
            return sc;
        }
    }

    // ============================================================================
    // 4. DEMO (main)
    // ============================================================================

    public static void main(String[] args) {
        ReformaAgrariaEngine e = new ReformaAgrariaEngine();

        System.out.println("=".repeat(70));
        System.out.println("OpenAgrarianRevolution -- A Terra e de Quem a Cuida");
        System.out.println("=".repeat(70));

        // Cadastro
        List<UsoSolo> usosLatif = Arrays.asList(UsoSolo.PASTAGEM_REGENERATIVA, UsoSolo.OCIOSO);
        List<PlanoAgrologia> planoVazio = Collections.emptyList();
        ImovelRural latif = e.cadastrar_imovel(
                "Fazenda Boa Vista (ex-latifundio)", 2500.0, "Sertao do Sao Francisco", "caatinga",
                TipoTenencia.GUARDIAO_FAMILIAR, usosLatif, 3, FuncaoSocialStatus.DESCUMPRE, 15.0,
                planoVazio, StatusReforma.DIAGNOSTICO, "Familia herdeira de titulo duvidoso"
        );

        List<UsoSolo> usosPequeno = Arrays.asList(UsoSolo.LAVOURA_ALIMENTACAO, UsoSolo.POMAR);
        List<PlanoAgrologia> planoPequeno = Arrays.asList(PlanoAgrologia.COMPOSTAGEM, PlanoAgrologia.ROTACAO_CULTURAS);
        ImovelRural pequeno_a = e.cadastrar_imovel(
                "Sitio Aconchego", 30.0, "Sertao do Sao Francisco", "caatinga",
                TipoTenencia.GUARDIAO_FAMILIAR, usosPequeno, 1, FuncaoSocialStatus.PARCIAL, 70.0,
                planoPequeno, StatusReforma.DIAGNOSTICO, ""
        );

        List<UsoSolo> usosReserva = Collections.singletonList(UsoSolo.RESERVA_NATIVA);
        List<PlanoAgrologia> planoReserva = Collections.singletonList(PlanoAgrologia.CICLO_FECHADO);
        ImovelRural reserva = e.cadastrar_imovel(
                "Reserva Caatinga Viva", 800.0, "Sertao do Sao Francisco", "caatinga",
                TipoTenencia.RESERVA_REGENERACAO, usosReserva, 0, FuncaoSocialStatus.CUMPRE, 0.0,
                planoReserva, StatusReforma.DIAGNOSTICO, ""
        );

        // Diagnostico
        DiagnosticoFundiario diag = e.diagnosticar("Sertao do Sao Francisco");
        System.out.println("\n[DIAGNOSTICO] " + diag.territorio);
        System.out.printf("  Area total: %.0f ha | Imoveis: %d%n", diag.total_area, diag.num_imoveis);
        System.out.printf("  Indice de Gini: %.3f (0=igual, 1=concentrado)%n", diag.indice_gini);
        System.out.printf("  %% area em latifundios: %.1f%%%n", diag.pct_area_latifundio);
        System.out.println("  Familias guardias: " + diag.familias_guardias);
        System.out.println("  VEREDITO: " + diag.veredito);

        // Notificacao
        System.out.println("\n[NOTIFICACAO]");
        String msg = e.notificar_latifundio(latif.id);
        System.out.println("  " + msg);

        // Auditoria
        System.out.println("\n[AUDITORIA DE FUNCAO SOCIAL]");
        for (String iid : Arrays.asList(latif.id, pequeno_a.id, reserva.id)) {
            Object[] audit = e.auditar_funcao_social(iid);
            FuncaoSocialStatus status = (FuncaoSocialStatus) audit[0];
            @SuppressWarnings("unchecked")
            List<String> faltas = (List<String>) audit[1];
            ImovelRural im = e.imoveis.get(iid);
            System.out.println("  " + iid + " (" + im.nome.substring(0, Math.min(30, im.nome.length())) + "): " + status.rotulo);
            for (String f : faltas) {
                System.out.println("      - " + f);
            }
        }

        // Conflito
        ConflitoFundiario conflito = e.registrar_conflito(
                TipoConflito.TRABALHO_ESCRAVO, latif.id, 2, 8,
                "Trabalhadores resgatados em condicoes analogas a escravidao."
        );
        System.out.println("\n[CONFLITO REGISTRADO] " + conflito.id + ": " + conflito.tipo.rotulo);
        System.out.println("  Gravidade: " + conflito.tipo.gravidade + "/5 | Familias afetadas: " + conflito.familias_afetadas);

        // Desapropriacao
        System.out.println("\n[DESAPROPRIACAO POR ASSEMBLEIA]");
        List<FamiliaGuardia> fams = new ArrayList<>();
        fams.add(e.cadastrar_familia("Familia Maria das Dores", 5, 0.0, null, "despejado", false));
        fams.add(e.cadastrar_familia("Familia Jose Pereira", 4, 0.0, null, "despejado", false));
        fams.add(e.cadastrar_familia("Familia Ana Beatriz", 6, 0.0, null, "voluntario", false));
        fams.add(e.cadastrar_familia("Familia Severino", 5, 0.0, null, "despejado", true));
        List<String> famIds = fams.stream().map(f -> f.id).collect(Collectors.toList());
        String res = e.desaproropriar(latif.id, famIds);
        System.out.println("  " + res);

        e.resolver_conflito(conflito.id, "Ex-dono removido; familias guardias assumem; recuperacao das vitimas via OpenPsychologyReparation.");
        System.out.println("  Conflito " + conflito.id + " resolvido: " + conflito.resolucao_proposta);

        // Consolidacao
        System.out.println("\n[CONSOLIDACAO COOPERATIVA]");
        List<String> ferramentas = Arrays.asList("trator_compartilhado", "casa_de_farinha", "cisterna_coletiva");
        CooperativaAgricola coop = e.consolidar_cooperativa(
                "Cooperativa Terra Livre Sertao", Collections.singletonList(latif.id), famIds,
                "mercado_aberto", ferramentas
        );
        System.out.println("  " + coop.id + ": " + coop.nome);
        System.out.println("  Familias: " + coop.familia_ids.size() + " | Territorios: " + coop.territorio_ids.size());
        System.out.println("  Ferramentas compartilhadas: " + String.join(", ", coop.ferramentas_compartilhadas));

        // Pos-revolucao
        latif.usos_solo = Arrays.asList(UsoSolo.AGROFLORESTA, UsoSolo.LAVOURA_DIVERSIFICADA, UsoSolo.POMAR);
        latif.plano_agrologia = Arrays.asList(
                PlanoAgrologia.AGROFLORESTA_SUCSSIONAL, PlanoAgrologia.CAPTACAO_CHUVA,
                PlanoAgrologia.BIOINSUMOS, PlanoAgrologia.CICLO_FECHADO
        );
        latif.produtividade_pct = 65.0;
        Object[] auditFinal = e.auditar_funcao_social(latif.id);
        FuncaoSocialStatus status_final = (FuncaoSocialStatus) auditFinal[0];
        System.out.println("\n[POS-REVOLUCAO] " + latif.id + " funcao social: " + status_final.rotulo);
        System.out.println("  Status: " + latif.status.rotulo + " | Tenencia: " + latif.tipo_tenencia.rotulo);

        // Scorecard
        System.out.println("\n" + "=".repeat(70));
        System.out.println("[SCORECARD DA REVOLUCAO AGRARIA]");
        System.out.println("=".repeat(70));
        Map<String, Object> sc = e.scorecard();
        for (Map.Entry<String, Object> entry : sc.entrySet()) {
            System.out.printf("  %s %s%n", String.format("%-28s", entry.getKey() + "."), entry.getValue());
        }

        // Conflitos
        System.out.println("\n[CONFLITOS POR GRAVIDADE]");
        for (ConflitoFundiario c : e.conflitos_por_gravidade()) {
            String flag = c.resolvido ? "OK" : "ABERTO";
            System.out.printf("  [%s] %s %s (grav=%d) vitimas=%d familias=%d%n",
                    flag, c.id, c.tipo.rotulo, c.tipo.gravidade, c.vitimas, c.familias_afetadas);
        }

        // Filosofia
        System.out.println("\n" + "=".repeat(70));
        System.out.println("FILOSOFIA -- Por que a Republica ABOLI a propriedade da terra");
        System.out.println("=".repeat(70));
        System.out.println("""
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
""");
    }
}
