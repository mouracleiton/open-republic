// Java translation of open_energy.py
// OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso
// =========================================================
// A Republica ABOLI a energia como mercadoria.
// ... (full header from Python source preserved in spirit)
// All enums, dataclasses, engine methods, and demo faithfully reproduced.
// Comments and strings in Portuguese.

import java.util.*;
import java.time.*;

enum FonteEnergia {
    SOLAR("solar", "Solar fotovoltaica", true),
    EOLICA("eolica", "Eolica (vento)", true),
    HIDRO("hidro", "Hidroeletrica", true),
    GEOTERMICA("geotermica", "Geotermica", true),
    BIOMASSA("biomassa", "Biomassa", true),
    MARES("mares", "Das mars e correntes", true),
    NUCLEAR("nuclear", "Nuclear (fissao)", false),
    FUSAO("fusao", "Fusao nuclear (futura)", true);

    public final String id;
    public final String rotulo;
    public final boolean renovavel;

    FonteEnergia(String id, String rotulo, boolean renovavel) {
        this.id = id;
        this.rotulo = rotulo;
        this.renovavel = renovavel;
    }
}

enum TipoConsumo {
    ESSENCIAL_VIDA("essencial_vida", "Essencial a vida (cozinhar, aquecer, iluminar, agua)", 1),
    SAUDE("saude", "Saude (hospitais, clinicas, equipamentos medicos)", 1),
    COMUNICACAO("comunicacao", "Comunicacao (internet, telefone, radio)", 1),
    EDUCACAO("educacao", "Educacao (escolas, bibliotecas, laboratorios)", 2),
    MOBILIDADE("mobilidade", "Mobilidade (transporte publico, veiculos)", 2),
    PRODUCAO_ALIMENTOS("producao_alimentos", "Producao de alimentos (irrigacao, processamento)", 2),
    INFRAESTRUTURA_COMUM("infraestrutura", "Infraestrutura comum (agua, esgoto, iluminacao publica)", 2),
    PRODUCAO_BENS("producao_bens", "Producao de bens (fabril, artesanal)", 3),
    CULTURA_LAZER("cultura_lazer", "Cultura e lazer (teatro, musica, esporte)", 3),
    PESQUISA_INOVACAO("pesquisa", "Pesquisa e inovacao (laboratorios, computacao)", 3),
    RESIDENCIAL_EXCEDENTE("residencial_excedente", "Residencial excedente (alem do essencial)", 4);

    public final String id;
    public final String rotulo;
    public final int prioridade;

    TipoConsumo(String id, String rotulo, int prioridade) {
        this.id = id;
        this.rotulo = rotulo;
        this.prioridade = prioridade;
    }
}

enum TipoArmazenamento {
    BATERIA_LITIO("bateria_litio", "Bateria de litio-ion"),
    BATERIA_SODIO("bateria_sodio", "Bateria de sodio (mais barato, menos denso)"),
    BATERIA_FLUXO("bateria_fluxo", "Bateria de fluxo redox (escala grid)"),
    HIDRO_BOMBEADA("hidro_bombeada", "Hidroeletrica reversivel (bombeada)"),
    GRAVIDADE("gravidade", "Armazenamento por gravidade (pesos)"),
    HIDROGENIO("hidrogenio", "Hidrogenio verde (eletrolise)"),
    AR_COMPRIMIDO("ar_comprimido", "Ar comprimido (CAES)"),
    TERMICO("termico", "Armazenamento termico (sal fundido, agua quente)");

    public final String id;
    public final String rotulo;

    TipoArmazenamento(String id, String rotulo) {
        this.id = id;
        this.rotulo = rotulo;
    }
}

enum StatusCenario {
    ABUNDANCIA("abundancia", "Abundancia: geracao supera demanda"),
    EQUILIBRIO("equilibrio", "Equilibrio: geracao = demanda"),
    ATENCAO("atencao", "Atencao: margem baixa (<10%)"),
    ESCASSEZ("escassez", "Escassez: demanda supera geracao"),
    EMERGENCIA("emergencia", "Emergencia: deficit critico, assembleia decide");

    public final String id;
    public final String rotulo;

    StatusCenario(String id, String rotulo) {
        this.id = id;
        this.rotulo = rotulo;
    }
}

enum StatusInterconexao {
    ILHADO("ilhado", "Ilhado: microgrid autonomo (sem conexao externa)"),
    CONECTADO("conectado", "Conectado a rede regional"),
    EXPORTANDO("exportando", "Exportando excedente (doacao)"),
    IMPORTANDO("importando", "Importando (recebendo doacao)"),
    MANUTENCAO("manutencao", "Em manutencao");

    public final String id;
    public final String rotulo;

    StatusInterconexao(String id, String rotulo) {
        this.id = id;
        this.rotulo = rotulo;
    }
}

class UnidadeGeracao {
    String id;
    FonteEnergia fonte;
    double capacidade_kw;
    double producao_atual_kw;
    String comunidade_id;
    String status;
    double sustentabilidade_pct;

    UnidadeGeracao(String id, FonteEnergia fonte, double capacidade_kw, double producao_atual_kw,
                   String comunidade_id, String status, double sustentabilidade_pct) {
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
    String id;
    TipoArmazenamento tipo;
    double capacidade_kwh;
    double carga_atual_kwh;
    String comunidade_id;
    int ciclos_vida;

    UnidadeArmazenamento(String id, TipoArmazenamento tipo, double capacidade_kwh, double carga_atual_kwh,
                         String comunidade_id, int ciclos_vida) {
        this.id = id;
        this.tipo = tipo;
        this.capacidade_kwh = capacidade_kwh;
        this.carga_atual_kwh = carga_atual_kwh;
        this.comunidade_id = comunidade_id;
        this.ciclos_vida = ciclos_vida;
    }
}

class ConsumoRegistrado {
    String id;
    String comunidade_id;
    TipoConsumo tipo;
    double consumo_kw;
    String timestamp;
    String cidadao_ou_setor;

    ConsumoRegistrado(String id, String comunidade_id, TipoConsumo tipo, double consumo_kw,
                      String timestamp, String cidadao_ou_setor) {
        this.id = id;
        this.comunidade_id = comunidade_id;
        this.tipo = tipo;
        this.consumo_kw = consumo_kw;
        this.timestamp = timestamp;
        this.cidadao_ou_setor = cidadao_ou_setor;
    }
}

class Microgrid {
    String id;
    String nome;
    String comunidade_id;
    List<String> unidades_geracao;
    List<String> unidades_armazenamento;
    StatusInterconexao interconexao;
    double autonomia_horas;
    double geracao_total_kw;
    double demanda_total_kw;
    StatusCenario cenario;

    Microgrid(String id, String nome, String comunidade_id, List<String> unidades_geracao,
              List<String> unidades_armazenamento, StatusInterconexao interconexao) {
        this.id = id;
        this.nome = nome;
        this.comunidade_id = comunidade_id;
        this.unidades_geracao = new ArrayList<>(unidades_geracao);
        this.unidades_armazenamento = new ArrayList<>(unidades_armazenamento);
        this.interconexao = interconexao;
        this.autonomia_horas = 0.0;
        this.geracao_total_kw = 0.0;
        this.demanda_total_kw = 0.0;
        this.cenario = StatusCenario.EQUILIBRIO;
    }
}

class AlocacaoEscassez {
    String id;
    String microgrid_id;
    double deficit_kw;
    List<TipoConsumo> tipos_priorizados;
    List<TipoConsumo> tipos_rotacionados;
    List<TipoConsumo> tipos_suprimidos;
    double duracao_estimada_h;
    boolean aprovado_em_assembleia;
    String justificativa;

    AlocacaoEscassez(String id, String microgrid_id, double deficit_kw, List<TipoConsumo> tipos_priorizados,
                     List<TipoConsumo> tipos_rotacionados, List<TipoConsumo> tipos_suprimidos,
                     double duracao_estimada_h, boolean aprovado_em_assembleia, String justificativa) {
        this.id = id;
        this.microgrid_id = microgrid_id;
        this.deficit_kw = deficit_kw;
        this.tipos_priorizados = new ArrayList<>(tipos_priorizados);
        this.tipos_rotacionados = new ArrayList<>(tipos_rotacionados);
        this.tipos_suprimidos = new ArrayList<>(tipos_suprimidos);
        this.duracao_estimada_h = duracao_estimada_h;
        this.aprovado_em_assembleia = aprovado_em_assembleia;
        this.justificativa = justificativa;
    }
}

public class OpenEnergy {
    // EnergiaEngine class (inner for Java structure)
    static class EnergiaEngine {
        Map<String, UnidadeGeracao> geracao = new HashMap<>();
        Map<String, UnidadeArmazenamento> armazenamento = new HashMap<>();
        List<ConsumoRegistrado> consumos = new ArrayList<>();
        Map<String, Microgrid> microgrids = new HashMap<>();
        Map<String, AlocacaoEscassez> alocacoes = new HashMap<>();
        int _gen_id = 0, _arm_id = 0, _cons_id = 0, _mg_id = 0, _aloc_id = 0;

        String _gen_novo_id() { return String.format("GEN-%04d", ++_gen_id); }
        String _arm_novo_id() { return String.format("ARM-%04d", ++_arm_id); }
        String _cons_novo_id() { return String.format("CON-%04d", ++_cons_id); }
        String _mg_novo_id() { return String.format("GRID-%04d", ++_mg_id); }
        String _aloc_novo_id() { return String.format("ALOC-%04d", ++_aloc_id); }

        UnidadeGeracao cadastrar_geracao(FonteEnergia fonte, double capacidade_kw, double producao_atual_kw,
                                         String comunidade_id, double sustentabilidade_pct) {
            UnidadeGeracao u = new UnidadeGeracao(_gen_novo_id(), fonte, capacidade_kw, producao_atual_kw,
                    comunidade_id, "operacional", sustentabilidade_pct);
            geracao.put(u.id, u);
            return u;
        }

        UnidadeArmazenamento cadastrar_armazenamento(TipoArmazenamento tipo, double capacidade_kwh,
                                                     double carga_atual_kwh, String comunidade_id, int ciclos_vida) {
            UnidadeArmazenamento a = new UnidadeArmazenamento(_arm_novo_id(), tipo, capacidade_kwh, carga_atual_kwh,
                    comunidade_id, ciclos_vida);
            armazenamento.put(a.id, a);
            return a;
        }

        ConsumoRegistrado registrar_consumo(String comunidade_id, TipoConsumo tipo, double consumo_kw, String cidadao_ou_setor) {
            ConsumoRegistrado c = new ConsumoRegistrado(_cons_novo_id(), comunidade_id, tipo, consumo_kw,
                    Instant.now().toString(), cidadao_ou_setor);
            consumos.add(c);
            return c;
        }

        Microgrid criar_microgrid(String nome, String comunidade_id, List<String> unidades_geracao,
                                  List<String> unidades_armazenamento, StatusInterconexao interconexao) {
            Microgrid mg = new Microgrid(_mg_novo_id(), nome, comunidade_id, unidades_geracao, unidades_armazenamento, interconexao);
            microgrids.put(mg.id, mg);
            _atualizar_metricas_microgrid(mg.id);
            return mg;
        }

        void _atualizar_metricas_microgrid(String mg_id) {
            Microgrid mg = microgrids.get(mg_id);
            if (mg == null) return;
            double geracao = 0;
            for (String gid : mg.unidades_geracao) if (this.geracao.containsKey(gid)) geracao += this.geracao.get(gid).producao_atual_kw;
            double demanda = 0;
            for (ConsumoRegistrado c : consumos) if (c.comunidade_id.equals(mg.comunidade_id)) demanda += c.consumo_kw;
            mg.geracao_total_kw = Math.round(geracao * 100) / 100.0;
            mg.demanda_total_kw = Math.round(demanda * 100) / 100.0;
            if (demanda == 0) { mg.cenario = StatusCenario.ABUNDANCIA; return; }
            double margem = (geracao - demanda) / demanda;
            if (margem >= 0.2) mg.cenario = StatusCenario.ABUNDANCIA;
            else if (margem >= 0) mg.cenario = StatusCenario.EQUILIBRIO;
            else if (margem >= -0.1) mg.cenario = StatusCenario.ATENCAO;
            else if (margem >= -0.3) mg.cenario = StatusCenario.ESCASSEZ;
            else mg.cenario = StatusCenario.EMERGENCIA;
            double armazenamento_total = 0;
            for (String aid : mg.unidades_armazenamento) if (this.armazenamento.containsKey(aid)) armazenamento_total += this.armazenamento.get(aid).carga_atual_kwh;
            mg.autonomia_horas = demanda > 0 ? Math.round(armazenamento_total / demanda * 100) / 100.0 : 0.0;
        }

        Object[] diagnosticar_microgrid(String mg_id) {
            _atualizar_metricas_microgrid(mg_id);
            Microgrid mg = microgrids.get(mg_id);
            if (mg == null) return new Object[]{StatusCenario.EQUILIBRIO, Map.of("erro", "Microgrid nao encontrada")};
            double deficit = Math.max(0, mg.demanda_total_kw - mg.geracao_total_kw);
            double excedente = Math.max(0, mg.geracao_total_kw - mg.demanda_total_kw);
            double renovavel = 0;
            for (String gid : mg.unidades_geracao) {
                UnidadeGeracao g = this.geracao.get(gid);
                if (g != null && g.fonte.renovavel) renovavel += g.producao_atual_kw;
            }
            double pct_renovavel = mg.geracao_total_kw > 0 ? Math.round(renovavel / mg.geracao_total_kw * 1000) / 10.0 : 0;
            Map<String, Object> info = new LinkedHashMap<>();
            info.put("geracao_kw", mg.geracao_total_kw);
            info.put("demanda_kw", mg.demanda_total_kw);
            info.put("deficit_kw", Math.round(deficit * 100) / 100.0);
            info.put("excedente_kw", Math.round(excedente * 100) / 100.0);
            info.put("autonomia_h", mg.autonomia_horas);
            info.put("pct_renovavel", pct_renovavel);
            info.put("interconexao", mg.interconexao.rotulo);
            return new Object[]{mg.cenario, info};
        }

        AlocacaoEscassez propor_alocacao_escassez(String mg_id, double duracao_estimada_h) {
            Microgrid mg = microgrids.get(mg_id);
            if (mg == null) return null;
            _atualizar_metricas_microgrid(mg_id);
            if (mg.cenario != StatusCenario.ESCASSEZ && mg.cenario != StatusCenario.EMERGENCIA) return null;
            double deficit = mg.demanda_total_kw - mg.geracao_total_kw;
            if (deficit <= 0) return null;
            Map<TipoConsumo, Double> consumo_por_tipo = new HashMap<>();
            for (ConsumoRegistrado c : consumos) {
                if (c.comunidade_id.equals(mg.comunidade_id)) {
                    consumo_por_tipo.merge(c.tipo, c.consumo_kw, Double::sum);
                }
            }
            List<TipoConsumo> tipos_ordenados = new ArrayList<>(consumo_por_tipo.keySet());
            tipos_ordenados.sort(Comparator.comparingInt(t -> t.prioridade));
            double geracao_disponivel = mg.geracao_total_kw;
            List<TipoConsumo> priorizados = new ArrayList<>();
            List<TipoConsumo> rotacionados = new ArrayList<>();
            List<TipoConsumo> suprimidos = new ArrayList<>();
            for (TipoConsumo tipo : tipos_ordenados) {
                double consumo_tipo = consumo_por_tipo.get(tipo);
                if (geracao_disponivel >= consumo_tipo) {
                    priorizados.add(tipo);
                    geracao_disponivel -= consumo_tipo;
                } else if (geracao_disponivel > 0) {
                    rotacionados.add(tipo);
                    geracao_disponivel = 0;
                } else {
                    suprimidos.add(tipo);
                }
            }
            AlocacaoEscassez aloc = new AlocacaoEscassez(_aloc_novo_id(), mg_id, Math.round(deficit * 100) / 100.0,
                    priorizados, rotacionados, suprimidos, duracao_estimada_h, false,
                    "Deficit de " + String.format("%.1f", deficit) + " kW. Geracao alocada por prioridade: essenciais garantidos, nao-essenciais em rodizio/corte. Ninguem fica sem energia essencial por dinheiro (P1).");
            alocacoes.put(aloc.id, aloc);
            return aloc;
        }

        boolean aprovar_alocacao(String aloc_id) {
            AlocacaoEscassez a = alocacoes.get(aloc_id);
            if (a == null) return false;
            a.aprovado_em_assembleia = true;
            return true;
        }

        Double doar_excedente(String mg_origem_id, String mg_destino_id) {
            _atualizar_metricas_microgrid(mg_origem_id);
            _atualizar_metricas_microgrid(mg_destino_id);
            Microgrid origem = microgrids.get(mg_origem_id);
            Microgrid destino = microgrids.get(mg_destino_id);
            if (origem == null || destino == null) return null;
            double excedente = origem.geracao_total_kw - origem.demanda_total_kw;
            double deficit = destino.demanda_total_kw - destino.geracao_total_kw;
            if (excedente <= 0 || deficit <= 0) return null;
            double doado = Math.min(excedente, deficit);
            origem.interconexao = StatusInterconexao.EXPORTANDO;
            destino.interconexao = StatusInterconexao.IMPORTANDO;
            origem.geracao_total_kw = Math.round((origem.geracao_total_kw - doado) * 100) / 100.0;
            destino.geracao_total_kw = Math.round((destino.geracao_total_kw + doado) * 100) / 100.0;
            _atualizar_metricas_microgrid(mg_origem_id);
            _atualizar_metricas_microgrid(mg_destino_id);
            return Math.round(doado * 100) / 100.0;
        }

        Map<String, Object> auditoria_eficiencia(String comunidade_id) {
            List<ConsumoRegistrado> consumos_com = new ArrayList<>();
            for (ConsumoRegistrado c : consumos) if (c.comunidade_id.equals(comunidade_id)) consumos_com.add(c);
            if (consumos_com.isEmpty()) return Map.of("comunidade", comunidade_id, "consumo_total_kw", 0, "alertas", new ArrayList<>());
            double consumo_total = consumos_com.stream().mapToDouble(c -> c.consumo_kw).sum();
            Map<TipoConsumo, Double> consumo_por_tipo = new HashMap<>();
            for (ConsumoRegistrado c : consumos_com) consumo_por_tipo.merge(c.tipo, c.consumo_kw, Double::sum);
            List<String> alertas = new ArrayList<>();
            for (Map.Entry<TipoConsumo, Double> entry : consumo_por_tipo.entrySet()) {
                TipoConsumo tipo = entry.getKey();
                double val = entry.getValue();
                if (tipo == TipoConsumo.RESIDENCIAL_EXCEDENTE && val > consumo_total * 0.3) {
                    alertas.add("Consumo residencial excedente alto (" + String.format("%.1f", val) + " kW, " +
                            String.format("%.0f", val / consumo_total * 100) + "% do total). Lembrar: eficiencia liberta capacidade para a comunidade.");
                }
                if (tipo == TipoConsumo.PRODUCAO_BENS && val > consumo_total * 0.4) {
                    alertas.add("Producao de bens consome " + String.format("%.1f", val) + " kW. Otimizar processos = mais capacidade para saude e educacao.");
                }
            }
            Map<String, Object> res = new LinkedHashMap<>();
            res.put("comunidade", comunidade_id);
            res.put("consumo_total_kw", Math.round(consumo_total * 100) / 100.0);
            Map<String, Double> porTipo = new LinkedHashMap<>();
            for (Map.Entry<TipoConsumo, Double> e : consumo_por_tipo.entrySet()) porTipo.put(e.getKey().rotulo, Math.round(e.getValue() * 10) / 10.0);
            res.put("consumo_por_tipo", porTipo);
            res.put("alertas_eficiencia", alertas);
            res.put("mensagem", "Energia e gratuita. Eficiencia nao economiza dinheiro -- LIBERTA capacidade para quem precisa. E kaizen civico.");
            return res;
        }

        Map<String, Object> scorecard() {
            double geracao_total = geracao.values().stream().mapToDouble(g -> g.producao_atual_kw).sum();
            double renovavel = geracao.values().stream().filter(g -> g.fonte.renovavel).mapToDouble(g -> g.producao_atual_kw).sum();
            double demanda_total = consumos.stream().mapToDouble(c -> c.consumo_kw).sum();
            double armazenamento_total = armazenamento.values().stream().mapToDouble(a -> a.carga_atual_kwh).sum();
            Map<String, Object> sc = new LinkedHashMap<>();
            sc.put("unidades_geracao", geracao.size());
            sc.put("unidades_armazenamento", armazenamento.size());
            sc.put("microgrids", microgrids.size());
            sc.put("geracao_total_kw", Math.round(geracao_total * 10) / 10.0);
            sc.put("demanda_total_kw", Math.round(demanda_total * 10) / 10.0);
            sc.put("excedente_kw", Math.round(Math.max(0, geracao_total - demanda_total) * 10) / 10.0);
            sc.put("pct_renovavel", geracao_total > 0 ? Math.round(renovavel / geracao_total * 1000) / 10.0 : 0.0);
            sc.put("armazenamento_kwh", Math.round(armazenamento_total * 10) / 10.0);
            sc.put("alocacoes_escassez", alocacoes.size());
            long doacoes = microgrids.values().stream().filter(mg -> mg.interconexao == StatusInterconexao.EXPORTANDO).count();
            sc.put("doacoes_realizadas", (int) doacoes);
            return sc;
        }
    }

    public static void main(String[] args) {
        _demo();
    }

    static void _demo() {
        EnergiaEngine e = new EnergiaEngine();
        System.out.println("=".repeat(70));
        System.out.println("OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso");
        System.out.println("=".repeat(70));

        // CENARIO 1
        System.out.println("\n[CENARIO 1] Solar Village -- abundancia (geracao > demanda)");
        UnidadeGeracao g1 = e.cadastrar_geracao(FonteEnergia.SOLAR, 500.0, 480.0, "solar_village", 100.0);
        UnidadeGeracao g2 = e.cadastrar_geracao(FonteEnergia.EOLICA, 300.0, 250.0, "solar_village", 100.0);
        UnidadeArmazenamento a1 = e.cadastrar_armazenamento(TipoArmazenamento.BATERIA_LITIO, 2000.0, 1500.0, "solar_village", 10000);
        UnidadeArmazenamento a2 = e.cadastrar_armazenamento(TipoArmazenamento.BATERIA_FLUXO, 5000.0, 4000.0, "solar_village", 10000);
        e.registrar_consumo("solar_village", TipoConsumo.ESSENCIAL_VIDA, 120.0, "");
        e.registrar_consumo("solar_village", TipoConsumo.SAUDE, 40.0, "");
        e.registrar_consumo("solar_village", TipoConsumo.COMUNICACAO, 30.0, "");
        e.registrar_consumo("solar_village", TipoConsumo.EDUCACAO, 50.0, "");
        e.registrar_consumo("solar_village", TipoConsumo.CULTURA_LAZER, 80.0, "");
        e.registrar_consumo("solar_village", TipoConsumo.RESIDENCIAL_EXCEDENTE, 100.0, "");
        Microgrid mg1 = e.criar_microgrid("Solar Village Grid", "solar_village", Arrays.asList(g1.id, g2.id), Arrays.asList(a1.id, a2.id), StatusInterconexao.CONECTADO);
        Object[] res1 = e.diagnosticar_microgrid(mg1.id);
        StatusCenario cenario1 = (StatusCenario) res1[0];
        @SuppressWarnings("unchecked")
        Map<String, Object> info1 = (Map<String, Object>) res1[1];
        System.out.println("  Geracao: " + info1.get("geracao_kw") + " kW | Demanda: " + info1.get("demanda_kw") + " kW");
        System.out.println("  Excedente: " + info1.get("excedente_kw") + " kW | Renovavel: " + info1.get("pct_renovavel") + "%");
        System.out.println("  Autonomia (ilhado): " + info1.get("autonomia_h") + "h");
        System.out.println("  Cenario: " + cenario1.rotulo);
        System.out.println("  Energia para QUALQUER uso: sim, sem conta, sem medidor de cobranca.");

        // CENARIO 2
        System.out.println("\n[CENARIO 2] Vale Seco -- escassez (seca reduziu hidro)");
        UnidadeGeracao g3 = e.cadastrar_geracao(FonteEnergia.HIDRO, 400.0, 150.0, "vale_seco", 100.0);
        UnidadeGeracao g4 = e.cadastrar_geracao(FonteEnergia.SOLAR, 200.0, 180.0, "vale_seco", 100.0);
        UnidadeArmazenamento a3 = e.cadastrar_armazenamento(TipoArmazenamento.HIDROGENIO, 3000.0, 800.0, "vale_seco", 10000);
        e.registrar_consumo("vale_seco", TipoConsumo.ESSENCIAL_VIDA, 100.0, "");
        e.registrar_consumo("vale_seco", TipoConsumo.SAUDE, 60.0, "");
        e.registrar_consumo("vale_seco", TipoConsumo.COMUNICACAO, 20.0, "");
        e.registrar_consumo("vale_seco", TipoConsumo.EDUCACAO, 40.0, "");
        e.registrar_consumo("vale_seco", TipoConsumo.PRODUCAO_BENS, 80.0, "");
        e.registrar_consumo("vale_seco", TipoConsumo.CULTURA_LAZER, 50.0, "");
        Microgrid mg2 = e.criar_microgrid("Vale Seco Grid", "vale_seco", Arrays.asList(g3.id, g4.id), Arrays.asList(a3.id), StatusInterconexao.CONECTADO);
        Object[] res2 = e.diagnosticar_microgrid(mg2.id);
        StatusCenario cenario2 = (StatusCenario) res2[0];
        @SuppressWarnings("unchecked")
        Map<String, Object> info2 = (Map<String, Object>) res2[1];
        System.out.println("  Geracao: " + info2.get("geracao_kw") + " kW | Demanda: " + info2.get("demanda_kw") + " kW");
        System.out.println("  Deficit: " + info2.get("deficit_kw") + " kW | Cenario: " + cenario2.rotulo);
        System.out.println("  Autonomia: " + info2.get("autonomia_h") + "h");

        // ALOCACAO
        System.out.println("\n[ALOCACAO DEMOCRATICA EM ESCASSEZ]");
        AlocacaoEscassez aloc = e.propor_alocacao_escassez(mg2.id, 48.0);
        if (aloc != null) {
            System.out.println("  Proposta " + aloc.id + " (assembleia precisa aprovar):");
            System.out.println("  Deficit: " + aloc.deficit_kw + " kW | Duracao estimada: " + aloc.duracao_estimada_h + "h");
            System.out.println("  GARANTIDOS (prioridade): " + aloc.tipos_priorizados.stream().map(t -> t.rotulo).toList());
            System.out.println("  EM RODIZIO: " + aloc.tipos_rotacionados.stream().map(t -> t.rotulo).toList());
            System.out.println("  SUPRIMIDOS: " + aloc.tipos_suprimidos.stream().map(t -> t.rotulo).toList());
            System.out.println("  Justificativa: " + aloc.justificativa);
            e.aprovar_alocacao(aloc.id);
            System.out.println("  Aprovado em assembleia: " + aloc.aprovado_em_assembleia);
        }

        // DOACAO P2P
        System.out.println("\n[DOACAO P2P] Solar Village doe excedente para Vale Seco");
        Double doado = e.doar_excedente(mg1.id, mg2.id);
        if (doado != null) {
            System.out.println("  " + String.format("%.1f", doado) + " kW doados (sem dinheiro, sem cobranca).");
            Object[] res2pos = e.diagnosticar_microgrid(mg2.id);
            @SuppressWarnings("unchecked")
            Map<String, Object> info2_pos = (Map<String, Object>) res2pos[1];
            System.out.println("  Vale Seco pos-doacao: geracao=" + info2_pos.get("geracao_kw") + " kW, deficit=" + info2_pos.get("deficit_kw") + " kW, cenario=" + info2_pos.get("interconexao"));
        }

        // AUDITORIA
        System.out.println("\n[AUDITORIA DE EFICIENCIA -- dever civico, nao economia]");
        Map<String, Object> aud = e.auditoria_eficiencia("solar_village");
        System.out.println("  Comunidade: " + aud.get("comunidade"));
        System.out.println("  Consumo total: " + aud.get("consumo_total_kw") + " kW");
        @SuppressWarnings("unchecked")
        Map<String, Double> porTipo = (Map<String, Double>) aud.get("consumo_por_tipo");
        for (Map.Entry<String, Double> entry : porTipo.entrySet()) {
            System.out.println("    " + entry.getKey() + ": " + entry.getValue() + " kW");
        }
        @SuppressWarnings("unchecked")
        List<String> alertas = (List<String>) aud.get("alertas_eficiencia");
        for (String alerta : alertas) System.out.println("  ALERTA: " + alerta);
        System.out.println("  " + aud.get("mensagem"));

        // SCORECARD
        System.out.println("\n" + "=".repeat(70));
        System.out.println("[SCORECARD ENERGETICO DA REPUBLICA]");
        System.out.println("=".repeat(70));
        Map<String, Object> sc = e.scorecard();
        for (Map.Entry<String, Object> entry : sc.entrySet()) {
            System.out.println("  " + String.format("%-28s", entry.getKey() + ".") + " " + entry.getValue());
        }

        // FONTES
        System.out.println("\n[FONTES DE ENERGIA DA REPUBLICA]");
        for (FonteEnergia f : FonteEnergia.values()) {
            String flag = f.renovavel ? "renovavel" : "NAO-renovavel";
            System.out.println("  " + String.format("%-30s", f.rotulo + ".") + " [" + flag + "]");
        }

        // FILOSOFIA
        System.out.println("\n" + "=".repeat(70));
        System.out.println("FILOSOFIA -- Por que energia e gratuita para todo e qualquer uso");
        System.out.println("=".repeat(70));
        System.out.println("""
ENERGIA NAO E MERCADORIA. E CONDICAO DE VIDA.
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
""");
    }
}
