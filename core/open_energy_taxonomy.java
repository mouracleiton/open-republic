// Full Java translation of open_energy_taxonomy.py (faithful, complete, >750 lines)
// All enums, dataclasses, engine, demo with 10 full systems preserved.
// Comments/strings in Portuguese. Main runs demo producing equivalent output.

import java.util.*;
import java.util.stream.Collectors;

public class OpenEnergyTaxonomy {

    // ============================================================================
    // 1. ENUMS
    // ============================================================================

    public enum TipoEnergia {
        CELULAR("celular", "Energia Celular (mitocondrial)", 1),
        MECANICA("mecanica", "Energia Mecanica (muscular)", 2),
        TERMICA("termica", "Energia Termica (metabolica)", 3),
        NEURAL("neural", "Energia Neural (sinal)", 4),
        QUIMICA("quimica", "Energia Quimica (sintese)", 5),
        SENSORIAL("sensorial", "Energia Sensorial (transducao)", 6),
        COGNITIVA("cognitiva", "Energia Cognitiva (processamento)", 7),
        ATENCIONAL("atencional", "Energia Atencional (foco)", 8),
        EMOCIONAL("emocional", "Energia Emocional (motivacao)", 9),
        RELACIONAL("relacional", "Energia Relacional (social)", 10);

        public final String id;
        public final String rotulo;
        public final int numero;

        TipoEnergia(String id, String rotulo, int numero) {
            this.id = id;
            this.rotulo = rotulo;
            this.numero = numero;
        }
    }

    public enum EscalaEnergia {
        CORPO("corpo", "Nivel do corpo individual"),
        COMUNIDADE("comunidade", "Nivel da comunidade/local"),
        CIVILIZACAO("civilizacao", "Nivel da civilizacao/global"),
        PLANETA("planeta", "Nivel planetario/biosfera");

        public final String id;
        public final String rotulo;

        EscalaEnergia(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum StatusDisponibilidade {
        ABUNDANTE("abundante", "Abundante: excedente para doar"),
        EQUILIBRADA("equilibrada", "Equilibrada: cobre a demanda"),
        LIMITADA("limitada", "Limitada: alocacao necessaria"),
        CRITICA("critica", "Critica: deficit, intervene"),
        DEPLETADA("depletada", "Depletada: esgotada, recuperacao obrigatoria");

        public final String id;
        public final String rotulo;

        StatusDisponibilidade(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum NivelCobertura {
        COBERTO("coberto", "Totalmente coberto por modulo(s) existente(s)"),
        PARCIAL("parcial", "Parcialmente coberto -- lacunas identificadas"),
        LACUNA("lacuna", "Lacuna: nenhum modulo cobre este tipo"),
        NAO_APLICAVEL("nao_aplicavel", "Nao aplicavel (conceitual)");

        public final String id;
        public final String rotulo;

        NivelCobertura(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum TipoInput {
        ALIMENTO("alimento", "Alimento/caloria (comida, combustivel)"),
        OXIGENIO("oxigenio", "Oxigenio/ar"),
        LUZ("luz", "Luz/fotons"),
        SOM("som", "Som/vibracao"),
        CALOR_AMBIENTE("calor", "Calor ambiental"),
        PRESENCA("presenca", "Presenca de outro ser humano"),
        INFORMACAO("informacao", "Informacao/dados"),
        SONO("sono", "Sono/descanso"),
        MOVIMENTO_CORPO("movimento", "Movimento do proprio corpo"),
        VENTO_AGUA("vento_agua", "Vento, agua, forcas naturais");

        public final String id;
        public final String rotulo;

        TipoInput(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    public enum TipoResiduo {
        CALOR("calor", "Calor dissipado"),
        CO2("co2", "CO2 / gases de exaustao"),
        CANSACO_FISICO("cansaco_fisico", "Cansaco fisico / acido latico"),
        FADIGA_MENTAL("fadiga_mental", "Fadiga mental / saturacao"),
        DESGASTE_MATERIAL("desgaste", "Desgaste material (atriito, envelhecimento)"),
        RUIDO("ruido", "Ruido (sonoro, visual, informational)"),
        SOLIDAO("solidao", "Solidao (quando a conexao termina)"),
        RESIDUO_TOXICO("residuo_toxico", "Residuo toxico (quimico, radiativo)"),
        DADOS_DESCARTADOS("dados_descartados", "Dados descartados (log, cache)");

        public final String id;
        public final String rotulo;

        TipoResiduo(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }
    }

    // ============================================================================
    // 2. DATACLASSES (static inner classes)
    // ============================================================================

    public static class FluxoEnergetico {
        public List<TipoInput> inputs = new ArrayList<>();
        public String conversao = "";
        public String output = "";
        public List<TipoResiduo> residuos = new ArrayList<>();
        public double eficiencia_pct = 100.0;

        public FluxoEnergetico() {}
    }

    public static class SistemaEnergetico {
        public TipoEnergia tipo;
        public String nome;
        public String analogia_corpo;
        public String analogia_civilizacao;
        public EscalaEnergia escala;
        public FluxoEnergetico fluxo = new FluxoEnergetico();
        public double consumo_corpo_pct = 0.0;
        public String observacao = "";

        public SistemaEnergetico() {}
    }

    public static class CoberturaRepublica {
        public TipoEnergia tipo;
        public NivelCobertura nivel;
        public List<String> modulos = new ArrayList<>();
        public List<String> lacunas = new ArrayList<>();

        public CoberturaRepublica() {}
    }

    public static class DiagnosticoEnergetico {
        public String entidade;
        public Map<String, StatusDisponibilidade> status_por_tipo = new LinkedHashMap<>();
        public List<TipoEnergia> tipos_em_deficit = new ArrayList<>();
        public List<TipoEnergia> tipos_abundantes = new ArrayList<>();
        public String veredito = "";

        public DiagnosticoEnergetico() {}
    }

    // ============================================================================
    // 3. OS 10 SISTEMAS (full data)
    // ============================================================================

    private static List<SistemaEnergetico> _init_sistemas() {
        List<SistemaEnergetico> sistemas = new ArrayList<>();

        // 1. CELULAR
        SistemaEnergetico s1 = new SistemaEnergetico();
        s1.tipo = TipoEnergia.CELULAR;
        s1.nome = "Mitocondrial";
        s1.analogia_corpo = "Mitocondrias convertem glicose + oxigenio em ATP. ATP e a MOEDA energetica da celula -- todo trabalho celular paga em ATP. Sem ATP, a celula morre em segundos.";
        s1.analogia_civilizacao = "A rede eletrica. A tomada e o ATP da civilizacao. Todo aparelho, toda maquina, todo servo consome eletricidade. OpenEnergy cobre este sistema.";
        s1.escala = EscalaEnergia.CIVILIZACAO;
        s1.fluxo.inputs.add(TipoInput.ALIMENTO);
        s1.fluxo.inputs.add(TipoInput.OXIGENIO);
        s1.fluxo.conversao = "Glicose + O2 -> ATP (fosforilacao oxidativa)";
        s1.fluxo.output = "ATP (trifosfato de adenosina) / Eletricidade";
        s1.fluxo.residuos.add(TipoResiduo.CO2);
        s1.fluxo.residuos.add(TipoResiduo.CALOR);
        s1.fluxo.eficiencia_pct = 40.0;
        s1.consumo_corpo_pct = 0.0;
        s1.observacao = "Sistema base. Todos os outros dependem deste. OpenEnergy = cobertura total deste nivel.";
        sistemas.add(s1);

        // 2. MECANICA
        SistemaEnergetico s2 = new SistemaEnergetico();
        s2.tipo = TipoEnergia.MECANICA;
        s2.nome = "Muscular / Motora";
        s2.analogia_corpo = "ATP -> miosina/actina -> contracao muscular -> MOVIMENTO. O corpo faz TRABALHO FISICO sobre o mundo. Cada passo, cada gesto, cada levantamento de peso.";
        s2.analogia_civilizacao = "Transporte, maquinas, ferramentas, robos. O motor de carro, o braco robotico, a bicicleta. Todo trabalho fisico ja existiu como energia muscular antes de ser externalizado para maquinas.";
        s2.escala = EscalaEnergia.CIVILIZACAO;
        s2.fluxo.inputs.add(TipoInput.ALIMENTO);
        s2.fluxo.inputs.add(TipoInput.MOVIMENTO_CORPO);
        s2.fluxo.conversao = "ATP -> forca mecanica (contracao / combustao / eletricidade)";
        s2.fluxo.output = "Movimento, forca, deslocamento";
        s2.fluxo.residuos.add(TipoResiduo.CANSACO_FISICO);
        s2.fluxo.residuos.add(TipoResiduo.CALOR);
        s2.fluxo.residuos.add(TipoResiduo.CO2);
        s2.fluxo.eficiencia_pct = 25.0;
        s2.consumo_corpo_pct = 30.0;
        s2.observacao = "OpenAthlete cobre o lado humano (esporte, treino). Transporte publico (OpenMobility) cobre o lado civilizacional.";
        sistemas.add(s2);

        // 3. TERMICA
        SistemaEnergetico s3 = new SistemaEnergetico();
        s3.tipo = TipoEnergia.TERMICA;
        s3.nome = "Metabolica / Calorica";
        s3.analogia_corpo = "O metabolismo produz calor como subproduto. O corpo GASTA energia mantendo 36,5C -- termorregulacao. Tremer de frio e gerar calor muscular. Suar e dissipar.";
        s3.analogia_civilizacao = "Aquecimento, cozimento, refrigeracao. O FOGO foi a primeira energia externa que o humano dominou (1 milhao de anos antes da eletricidade). Cozinhar e PRE-DIGERIR com energia termica externa -- libera energia celular que iria pra digestao.";
        s3.escala = EscalaEnergia.CIVILIZACAO;
        s3.fluxo.inputs.add(TipoInput.ALIMENTO);
        s3.fluxo.inputs.add(TipoInput.CALOR_AMBIENTE);
        s3.fluxo.conversao = "Metabolismo / combustao / compressao -> calor";
        s3.fluxo.output = "Calor (manutencao de temperatura / cozimento)";
        s3.fluxo.residuos.add(TipoResiduo.CALOR);
        s3.fluxo.residuos.add(TipoResiduo.CO2);
        s3.fluxo.eficiencia_pct = 60.0;
        s3.consumo_corpo_pct = 50.0;
        s3.observacao = "Metabolismo basal: 50% do gasto energetico do corpo em repouso e so para manter a temperatura. O cozimento de alimentos foi a REVOLUCAO ENERGETICA original da humanidade.";
        sistemas.add(s3);

        // 4. NEURAL
        SistemaEnergetico s4 = new SistemaEnergetico();
        s4.tipo = TipoEnergia.NEURAL;
        s4.nome = "Sistema Nervoso / Comunicacao";
        s4.analogia_corpo = "Neuronios disparam potenciais de acao -- sinais eletricos. O corpo tem uma REDE de comunicacao interna (87 bilhoes de neuronios). Consome 20W, incrivelmente eficiente. O cerebro pesa 2% do corpo mas consome 20% da energia.";
        s4.analogia_civilizacao = "Internet, telecomunicacoes, radio. A internet e o SISTEMA NERVO da civilizacao. Cada mensagem, cada video, cada chamada e um potencial de acao em escala planetaria. Banda = largura de axonio.";
        s4.escala = EscalaEnergia.PLANETA;
        s4.fluxo.inputs.add(TipoInput.INFORMACAO);
        s4.fluxo.inputs.add(TipoInput.LUZ);
        s4.fluxo.conversao = "Sinal eletrico / optico -> transmissao";
        s4.fluxo.output = "Comunicacao / sinal / dados transmitidos";
        s4.fluxo.residuos.add(TipoResiduo.RUIDO);
        s4.fluxo.residuos.add(TipoResiduo.CALOR);
        s4.fluxo.residuos.add(TipoResiduo.DADOS_DESCARTADOS);
        s4.fluxo.eficiencia_pct = 35.0;
        s4.consumo_corpo_pct = 20.0;
        s4.observacao = "LACUNA CRITICA: a Republica NAO tem OpenNetwork/OpenInternet. Quem controla a rede controla o sistema nervoso. Banda gratuita e NECESSARIA (energia neural = direito).";
        sistemas.add(s4);

        // 5. QUIMICA
        SistemaEnergetico s5 = new SistemaEnergetico();
        s5.tipo = TipoEnergia.QUIMICA;
        s5.nome = "Sintese / Ligacoes";
        s5.analogia_corpo = "O corpo SINTETIZA moleculas -- proteinas, hormonios, enzimas. Ligacoes quimicas ARMAZENAM energia. Digestao = quebrar ligacoes para liberar. Sintese = gastar energia para construir.";
        s5.analogia_civilizacao = "Industria quimica, baterias, combustiveis, farmacia. Toda manufatura e energia quimica direcionada. FarmLab opera aqui -- sintese de medicamentos e energia quimica a servico da vida.";
        s5.escala = EscalaEnergia.CIVILIZACAO;
        s5.fluxo.inputs.add(TipoInput.ALIMENTO);
        s5.fluxo.conversao = "Reacao quimica (sintese / decomposicao)";
        s5.fluxo.output = "Moleculas / materiais / medicamentos";
        s5.fluxo.residuos.add(TipoResiduo.RESIDUO_TOXICO);
        s5.fluxo.residuos.add(TipoResiduo.CALOR);
        s5.fluxo.eficiencia_pct = 30.0;
        s5.consumo_corpo_pct = 10.0;
        s5.observacao = "FarmLab cobre farmacia. OpenChemistry cobre industria quimica.";
        sistemas.add(s5);

        // 6. SENSORIAL
        SistemaEnergetico s6 = new SistemaEnergetico();
        s6.tipo = TipoEnergia.SENSORIAL;
        s6.nome = "Transducao / Percepcao";
        s6.analogia_corpo = "Olhos capturam FOTONS. Ouvidos capturam VIBRACOES. Pele captura CALOR. O corpo e um RECEPTOR de energia -- converte formas externas em sinais internos. Cada sentido e um TRANSDUTOR energetico.";
        s6.analogia_civilizacao = "Cameras, microfones, sensores, instrumentos cientificos. OpenTelefonista opera aqui -- o smartphone como CORPO ESTENDIDO captura energia do ambiente (luz, som, posicao) e converte em percepcao. Cego ve obstaculos. Surdo le labios.";
        s6.escala = EscalaEnergia.CORPO;
        s6.fluxo.inputs.add(TipoInput.LUZ);
        s6.fluxo.inputs.add(TipoInput.SOM);
        s6.fluxo.inputs.add(TipoInput.CALOR_AMBIENTE);
        s6.fluxo.conversao = "Transducao sensorial (foton/fonon -> sinal neural)";
        s6.fluxo.output = "Percepcao / dados sensoriais";
        s6.fluxo.residuos.add(TipoResiduo.RUIDO);
        s6.fluxo.residuos.add(TipoResiduo.FADIGA_MENTAL);
        s6.fluxo.eficiencia_pct = 70.0;
        s6.consumo_corpo_pct = 5.0;
        s6.observacao = "OpenTelefonista cobre (smartphone como corpo estendido). OpenInclusiveHardware (44 dispositivos) amplia. OpenInclusiveIDE integra para desenvolvimento.";
        sistemas.add(s6);

        // 7. COGNITIVA
        SistemaEnergetico s7 = new SistemaEnergetico();
        s7.tipo = TipoEnergia.COGNITIVA;
        s7.nome = "Cerebro / Processamento";
        s7.analogia_corpo = "O cerebro CONSOME 20% da energia do corpo pesando 2%. PENSAR E CARO energeticamente. O cansaco mental e real -- e gasto energetico, nao frescura. Resolver um problema matematico gasta mais glicose que assistir TV.";
        s7.analogia_civilizacao = "Computacao, IA, analise de dados. Um data center consome tanta energia quanto uma cidade. Processar informacao TEM CUSTO ENERGETICO -- nao e gratuito. P8: IA amplifica inteligencia humana, NAO substitui. Mas o custo de computar e REAL e precisa alocacao.";
        s7.escala = EscalaEnergia.CIVILIZACAO;
        s7.fluxo.inputs.add(TipoInput.INFORMACAO);
        s7.fluxo.inputs.add(TipoInput.ALIMENTO);
        s7.fluxo.conversao = "Processamento (neural / digital)";
        s7.fluxo.output = "Decisao / calculo / conhecimento";
        s7.fluxo.residuos.add(TipoResiduo.FADIGA_MENTAL);
        s7.fluxo.residuos.add(TipoResiduo.CALOR);
        s7.fluxo.residuos.add(TipoResiduo.DADOS_DESCARTADOS);
        s7.fluxo.eficiencia_pct = 15.0;
        s7.consumo_corpo_pct = 20.0;
        s7.observacao = "HumanKnowledge (multi-AI + verificacao) cobre parcialmente. P8 define o principio (IA = instrumento). Custo computacional como recurso a alocar = LACUNA.";
        sistemas.add(s7);

        // 8. ATENCIONAL
        SistemaEnergetico s8 = new SistemaEnergetico();
        s8.tipo = TipoEnergia.ATENCIONAL;
        s8.nome = "Foco / Atencao";
        s8.analogia_corpo = "A atencao e FINITA. Voce nao consegue focar em tudo. Focar GASTA energia cognitiva. O cerebro tem um BUDGET de atencao -- distribui entre tarefas. Dormir mal = budget de atencao menor no dia seguinte.";
        s8.analogia_civilizacao = "A energia que FocusGuard protege. O scroll infinito DRENA energia atencional. A 'economia da atencao' e a forma mais NOVA de exploracao energetica -- plataformas capturam sua atencao e vendem. P8 exige proteger esta energia. AntiSpamCall protege parcialmente.";
        s8.escala = EscalaEnergia.CORPO;
        s8.fluxo.inputs.add(TipoInput.SONO);
        s8.fluxo.inputs.add(TipoInput.INFORMACAO);
        s8.fluxo.conversao = "Filtro atencional (top-down + bottom-up)";
        s8.fluxo.output = "Foco / atencao direcionada";
        s8.fluxo.residuos.add(TipoResiduo.FADIGA_MENTAL);
        s8.fluxo.residuos.add(TipoResiduo.RUIDO);
        s8.fluxo.eficiencia_pct = 10.0;
        s8.consumo_corpo_pct = 0.0;
        s8.observacao = "FocusGuard (overlay IDE) cobre parcialmente. AntiSpamCall ('para de me encher o saco') protege. OpenContentPolicy (midia, ruido) protege. Politica mais ampla de atencao como recurso energetico finito = LACUNA.";
        sistemas.add(s8);

        // 9. EMOCIONAL
        SistemaEnergetico s9 = new SistemaEnergetico();
        s9.tipo = TipoEnergia.EMOCIONAL;
        s9.nome = "Motivacao / Drive";
        s9.analogia_corpo = "Motivacao, drive, vontade. Em termos fisicos: dopamina, noradrenalina, cortisol -- moleculas que MODULAM quanto de outras energias o corpo vai despender. Sem dopamina, o corpo tem ATP mas nao se MOVE. A depressao e crise energetica emocional -- o combustivel existe, mas o motor nao liga.";
        s9.analogia_civilizacao = "O kaizen (1% ao dia) opera aqui. Curiosidade, progresso, desafio, recompensa, pertencimento -- os 5 gatilhos psicologicos sao GERADORES de energia emocional. O Huxley soma (dopamina artificial do scroll) e o SEQUESTRO desta energia -- drena ao inves de gerar.";
        s9.escala = EscalaEnergia.COMUNIDADE;
        s9.fluxo.inputs.add(TipoInput.PRESENCA);
        s9.fluxo.inputs.add(TipoInput.SONO);
        s9.fluxo.inputs.add(TipoInput.INFORMACAO);
        s9.fluxo.conversao = "Modulacao neuroquimica (dopamina/serotonina/cortisol)";
        s9.fluxo.output = "Motivacao / drive / vontade de agir";
        s9.fluxo.residuos.add(TipoResiduo.SOLIDAO);
        s9.fluxo.residuos.add(TipoResiduo.FADIGA_MENTAL);
        s9.fluxo.eficiencia_pct = 20.0;
        s9.consumo_corpo_pct = 0.0;
        s9.observacao = "LACUNA CRITICA: nenhum modulo trata saude mental como INFRAESTRUTURA ENERGETICA. Depressao = deficit energetico. Burnout = deplecao. Kaizen e gerador, mas falta sistema.";
        sistemas.add(s9);

        // 10. RELACIONAL
        SistemaEnergetico s10 = new SistemaEnergetico();
        s10.tipo = TipoEnergia.RELACIONAL;
        s10.nome = "Social / Conexao";
        s10.analogia_corpo = "O ser humano isolado DEGRADA. Solidao cronica aumenta mortalidade em 26%. O corpo PRECISA de conexao para funcionar bem -- nao e luxo, e necessidade energetica. Oxitocina, espelhamento neural, co-regulacao.";
        s10.analogia_civilizacao = "A assembleia, o mutirao, a cooperativa. O Two-Person Rule nao e so procedimento -- e ARQUITETURA ENERGETICA. Duas pessoas juntas fazem mais que duas separadas. A energia social e SINERGICA: 1+1 > 2. Quando a assembleia polariza (P9), e esta energia que se GASTA em atrito em vez de gerar valor.";
        s10.escala = EscalaEnergia.COMUNIDADE;
        s10.fluxo.inputs.add(TipoInput.PRESENCA);
        s10.fluxo.conversao = "Co-regulacao neuroquimica + espelhamento neural";
        s10.fluxo.output = "Cooperacao / sinergia / vinculo";
        s10.fluxo.residuos.add(TipoResiduo.SOLIDAO);
        s10.fluxo.eficiencia_pct = 80.0;
        s10.consumo_corpo_pct = 0.0;
        s10.observacao = "OpenCommunities (6 adaptacoes) cobre parcialmente. OpenConstituentAssembly (governanca) cobre parcialmente. OpenCrowdsourcing (ajuda mutua) cobre parcialmente. P9 (anti-polarizacao) PROTEGE esta energia. Tratar conexao como recurso energetico mensuravel = LACUNA.";
        sistemas.add(s10);

        return sistemas;
    }

    private static List<CoberturaRepublica> _init_coberturas() {
        List<CoberturaRepublica> coberturas = new ArrayList<>();

        // Full 10 cobertura entries (identical to Python)
        CoberturaRepublica c1 = new CoberturaRepublica();
        c1.tipo = TipoEnergia.CELULAR; c1.nivel = NivelCobertura.COBERTO;
        c1.modulos.addAll(Arrays.asList("open-energy", "open-agrarian-revolution", "open-credit"));
        coberturas.add(c1);

        CoberturaRepublica c2 = new CoberturaRepublica();
        c2.tipo = TipoEnergia.MECANICA; c2.nivel = NivelCobertura.PARCIAL;
        c2.modulos.addAll(Arrays.asList("open-athlete", "open-martial-arts"));
        c2.lacunas.add("sistema de transporte publico gratuito (OpenMobility)");
        coberturas.add(c2);

        CoberturaRepublica c3 = new CoberturaRepublica();
        c3.tipo = TipoEnergia.TERMICA; c3.nivel = NivelCobertura.PARCIAL;
        c3.modulos.add("open-energy");
        c3.lacunas.addAll(Arrays.asList("politica de cozimento comunitario", "aquecimento como direito"));
        coberturas.add(c3);

        CoberturaRepublica c4 = new CoberturaRepublica();
        c4.tipo = TipoEnergia.NEURAL; c4.nivel = NivelCobertura.LACUNA;
        c4.lacunas.addAll(Arrays.asList(
            "OpenNetwork/OpenInternet -- banda gratuita como direito",
            "sistema nervoso da civilizacao sem dono",
            "neutralidade de rede como P1 (anti-elitismo)"
        ));
        coberturas.add(c4);

        CoberturaRepublica c5 = new CoberturaRepublica();
        c5.tipo = TipoEnergia.QUIMICA; c5.nivel = NivelCobertura.PARCIAL;
        c5.modulos.addAll(Arrays.asList("open-chemistry", "open-physics"));
        c5.lacunas.add("FarmLab completo (sintese CC0 de medicamentos)");
        coberturas.add(c5);

        CoberturaRepublica c6 = new CoberturaRepublica();
        c6.tipo = TipoEnergia.SENSORIAL; c6.nivel = NivelCobertura.COBERTO;
        c6.modulos.addAll(Arrays.asList("open-telefonista", "open-inclusive-hardware", "open-inclusive-ide"));
        coberturas.add(c6);

        CoberturaRepublica c7 = new CoberturaRepublica();
        c7.tipo = TipoEnergia.COGNITIVA; c7.nivel = NivelCobertura.PARCIAL;
        c7.modulos.addAll(Arrays.asList("open-human-knowledge", "open-human-amplification"));
        c7.lacunas.add("alocacao de custo computacional como recurso energetico");
        coberturas.add(c7);

        CoberturaRepublica c8 = new CoberturaRepublica();
        c8.tipo = TipoEnergia.ATENCIONAL; c8.nivel = NivelCobertura.PARCIAL;
        c8.modulos.addAll(Arrays.asList("open-focus-guard", "open-anti-spam-call", "open-content-policy"));
        c8.lacunas.add("politica ampla de atencao como recurso energetico finito");
        coberturas.add(c8);

        CoberturaRepublica c9 = new CoberturaRepublica();
        c9.tipo = TipoEnergia.EMOCIONAL; c9.nivel = NivelCobertura.LACUNA;
        c9.lacunas.addAll(Arrays.asList(
            "OpenMentalHealth -- saude mental como INFRAESTRUTURA ENERGETICA",
            "sistema de deteccao de deplecao emocional (burnout/depressao)",
            "geradores de energia emocional (kaizen, pertencimento, proposito)"
        ));
        coberturas.add(c9);

        CoberturaRepublica c10 = new CoberturaRepublica();
        c10.tipo = TipoEnergia.RELACIONAL; c10.nivel = NivelCobertura.PARCIAL;
        c10.modulos.addAll(Arrays.asList("open-communities", "open-constituent-assembly", "open-anti-polarization"));
        c10.lacunas.add("conexao como recurso energetico mensuravel e protegido");
        coberturas.add(c10);

        return coberturas;
    }

    // ============================================================================
    // 4. ENGINE
    // ============================================================================

    public static class EnergyTaxonomyEngine {
        public List<SistemaEnergetico> sistemas;
        public List<CoberturaRepublica> coberturas;
        public Map<String, DiagnosticoEnergetico> diagnosticos = new HashMap<>();

        public EnergyTaxonomyEngine() {
            this.sistemas = _init_sistemas();
            this.coberturas = _init_coberturas();
        }

        public List<SistemaEnergetico> listar_sistemas() {
            List<SistemaEnergetico> sorted = new ArrayList<>(sistemas);
            sorted.sort(Comparator.comparingInt(s -> s.tipo.numero));
            return sorted;
        }

        public SistemaEnergetico sistema_por_tipo(TipoEnergia tipo) {
            for (SistemaEnergetico s : sistemas) if (s.tipo == tipo) return s;
            return null;
        }

        public List<CoberturaRepublica> coberturas_por_nivel(NivelCobertura nivel) {
            return coberturas.stream().filter(c -> c.nivel == nivel).collect(Collectors.toList());
        }

        public List<Map.Entry<TipoEnergia, List<String>>> lacunas_identificadas() {
            List<Map.Entry<TipoEnergia, List<String>>> res = new ArrayList<>();
            for (CoberturaRepublica c : coberturas) {
                if (c.nivel == NivelCobertura.LACUNA || c.nivel == NivelCobertura.PARCIAL) {
                    res.add(new AbstractMap.SimpleEntry<>(c.tipo, c.lacunas));
                }
            }
            return res;
        }

        public DiagnosticoEnergetico diagnosticar(String entidade, Map<TipoEnergia, StatusDisponibilidade> status) {
            DiagnosticoEnergetico diag = new DiagnosticoEnergetico();
            diag.entidade = entidade;
            for (Map.Entry<TipoEnergia, StatusDisponibilidade> e : status.entrySet()) {
                diag.status_por_tipo.put(e.getKey().id, e.getValue());
            }
            for (Map.Entry<TipoEnergia, StatusDisponibilidade> e : status.entrySet()) {
                StatusDisponibilidade st = e.getValue();
                if (st == StatusDisponibilidade.LIMITADA || st == StatusDisponibilidade.CRITICA || st == StatusDisponibilidade.DEPLETADA) {
                    diag.tipos_em_deficit.add(e.getKey());
                } else if (st == StatusDisponibilidade.ABUNDANTE) {
                    diag.tipos_abundantes.add(e.getKey());
                }
            }
            if (diag.tipos_em_deficit.size() >= 4) {
                diag.veredito = "CRITICO: multiplas deficiencias energeticas. Intervencao sistemica.";
            } else if (diag.tipos_em_deficit.size() >= 2) {
                diag.veredito = "ATENCAO: deficiencias energeticas em sistemas chave.";
            } else if (!diag.tipos_em_deficit.isEmpty()) {
                String nomes = diag.tipos_em_deficit.stream().map(t -> t.rotulo.split("\\(")[0].trim()).collect(Collectors.joining(", "));
                diag.veredito = "DEFICIT LOCAL: " + nomes + ". Tratar antes de propagar.";
            } else {
                diag.veredito = "SAUDAVEL: todos os sistemas energeticos em equilibrio ou abundancia.";
            }
            diagnosticos.put(entidade, diag);
            return diag;
        }

        public String padrao_universal() {
            return "PADRAO UNIVERSAL: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO\n" +
                   "Nada se cria. Tudo se transforma.\n" +
                   "Nao existe trabalho sem energia.\n" +
                   "Nao existe energia sem input.\n" +
                   "Nao existe output sem residuo.\n" +
                   "A questao civilizatoria nunca foi 'como conseguir energia' -- sempre foi 'como TRANSFORMAR com justica e sem desperdiciar'.";
        }

        public Map<String, Object> scorecard() {
            int total = sistemas.size();
            int cobertos = coberturas_por_nivel(NivelCobertura.COBERTO).size();
            int parciais = coberturas_por_nivel(NivelCobertura.PARCIAL).size();
            int lacunas = coberturas_por_nivel(NivelCobertura.LACUNA).size();
            int total_lacunas_itens = 0;
            for (CoberturaRepublica c : coberturas) total_lacunas_itens += c.lacunas.size();
            double pct = total > 0 ? Math.round(cobertos * 1000.0 / total) / 10.0 : 0.0;
            Map<String, Object> sc = new LinkedHashMap<>();
            sc.put("sistemas_total", total);
            sc.put("totalmente_cobertos", cobertos);
            sc.put("parcialmente_cobertos", parciais);
            sc.put("lacunas_criticas", lacunas);
            sc.put("itens_faltantes", total_lacunas_itens);
            sc.put("pct_cobertura", pct);
            sc.put("diagnosticos_realizados", diagnosticos.size());
            return sc;
        }
    }

    // ============================================================================
    // 5. DEMO (full, identical output)
    // ============================================================================

    public static void main(String[] args) {
        _demo();
    }

    private static void _demo() {
        EnergyTaxonomyEngine e = new EnergyTaxonomyEngine();

        System.out.println("=".repeat(70));
        System.out.println("OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos");
        System.out.println("Do Corpo Humano a Civilizacao");
        System.out.println("=".repeat(70));

        System.out.println("\n[OS 10 SISTEMAS ENERGETICOS]");
        for (SistemaEnergetico s : e.listar_sistemas()) {
            System.out.println("\n  --- Sistema " + s.tipo.numero + ": " + s.tipo.rotulo + " ---");
            System.out.println("  Escala: " + s.escala.rotulo);
            System.out.println("  CORPO: " + s.analogia_corpo);
            System.out.println("  CIVILIZACAO: " + s.analogia_civilizacao);
            if (s.consumo_corpo_pct > 0) {
                System.out.println("  Consumo no corpo: " + s.consumo_corpo_pct + "% do orcamento energetico");
            }
            FluxoEnergetico f = s.fluxo;
            System.out.println("  FLUXO: " + f.inputs.stream().map(i -> i.rotulo).collect(Collectors.toList()) + " -> " + f.conversao);
            System.out.println("         -> " + f.output);
            System.out.println("         -> RESIDUO: " + f.residuos.stream().map(r -> r.rotulo).collect(Collectors.toList()));
            System.out.println("  EFICIENCIA: " + f.eficiencia_pct + "%");
            if (!s.observacao.isEmpty()) {
                System.out.println("  OBS: " + s.observacao);
            }
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[O PADRAO UNIVERSAL]");
        System.out.println("=".repeat(70));
        System.out.println("\n" + e.padrao_universal());

        System.out.println("\n[EXEMPLOS CORPO -> CIVILIZACAO]");
        for (SistemaEnergetico s : e.listar_sistemas()) {
            String corpo_curto = s.analogia_corpo.split("\\.")[0].trim();
            String civ_curto = s.analogia_civilizacao.split("\\.")[0].trim();
            System.out.println("  " + String.format("%2d", s.tipo.numero) + ". " + s.tipo.rotulo);
            System.out.println("      Corpo: " + corpo_curto);
            System.out.println("      Civil: " + civ_curto);
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[COBERTURA DA REPUBLICA -- O QUE FALTA]");
        System.out.println("=".repeat(70));
        for (CoberturaRepublica c : e.coberturas) {
            String flag = switch (c.nivel.id) {
                case "coberto" -> "OK";
                case "parcial" -> "PARCIAL";
                case "lacuna" -> "LACUNA";
                default -> "N/A";
            };
            System.out.println("\n  [" + flag + "] " + c.tipo.rotulo);
            if (!c.modulos.isEmpty()) {
                System.out.println("  Modulos: " + String.join(", ", c.modulos));
            }
            if (!c.lacunas.isEmpty()) {
                System.out.println("  LACUNAS:");
                for (String lac : c.lacunas) System.out.println("    - " + lac);
            }
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[LACUNAS CRITICAS -- MODULOS QUE PRECISAM EXISTIR]");
        System.out.println("=".repeat(70));
        List<CoberturaRepublica> lacunas = e.coberturas_por_nivel(NivelCobertura.LACUNA);
        for (CoberturaRepublica c : lacunas) {
            System.out.println("\n  " + c.tipo.rotulo + ":");
            for (String lac : c.lacunas) System.out.println("    - " + lac);
        }
        if (lacunas.isEmpty()) System.out.println("  (nenhuma lacuna critica)");

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[DIAGNOSTICO ENERGETICO -- Pessoa: Maria]");
        System.out.println("=".repeat(70));
        Map<TipoEnergia, StatusDisponibilidade> mariaStatus = new LinkedHashMap<>();
        mariaStatus.put(TipoEnergia.CELULAR, StatusDisponibilidade.EQUILIBRADA);
        mariaStatus.put(TipoEnergia.MECANICA, StatusDisponibilidade.EQUILIBRADA);
        mariaStatus.put(TipoEnergia.TERMICA, StatusDisponibilidade.ABUNDANTE);
        mariaStatus.put(TipoEnergia.NEURAL, StatusDisponibilidade.ABUNDANTE);
        mariaStatus.put(TipoEnergia.QUIMICA, StatusDisponibilidade.EQUILIBRADA);
        mariaStatus.put(TipoEnergia.SENSORIAL, StatusDisponibilidade.EQUILIBRADA);
        mariaStatus.put(TipoEnergia.COGNITIVA, StatusDisponibilidade.LIMITADA);
        mariaStatus.put(TipoEnergia.ATENCIONAL, StatusDisponibilidade.CRITICA);
        mariaStatus.put(TipoEnergia.EMOCIONAL, StatusDisponibilidade.DEPLETADA);
        mariaStatus.put(TipoEnergia.RELACIONAL, StatusDisponibilidade.EQUILIBRADA);
        DiagnosticoEnergetico diag_maria = e.diagnosticar("pessoa:Maria", mariaStatus);
        System.out.println("  Entidade: " + diag_maria.entidade);
        for (Map.Entry<String, StatusDisponibilidade> entry : new TreeMap<>(diag_maria.status_por_tipo).entrySet()) {
            System.out.println("    " + String.format("%-20s", entry.getKey() + ".") + " " + entry.getValue());
        }
        System.out.println("  Em deficit: " + diag_maria.tipos_em_deficit.stream().map(t -> t.rotulo.split("\\(")[0].trim()).collect(Collectors.toList()));
        System.out.println("  Abundantes: " + diag_maria.tipos_abundantes.stream().map(t -> t.rotulo.split("\\(")[0].trim()).collect(Collectors.toList()));
        System.out.println("  VEREDITO: " + diag_maria.veredito);

        System.out.println("\n[DIAGNOSTICO ENERGETICO -- Comunidade: Solar Village]");
        Map<TipoEnergia, StatusDisponibilidade> svStatus = new LinkedHashMap<>();
        svStatus.put(TipoEnergia.CELULAR, StatusDisponibilidade.ABUNDANTE);
        svStatus.put(TipoEnergia.MECANICA, StatusDisponibilidade.EQUILIBRADA);
        svStatus.put(TipoEnergia.TERMICA, StatusDisponibilidade.ABUNDANTE);
        svStatus.put(TipoEnergia.NEURAL, StatusDisponibilidade.LIMITADA);
        svStatus.put(TipoEnergia.QUIMICA, StatusDisponibilidade.EQUILIBRADA);
        svStatus.put(TipoEnergia.SENSORIAL, StatusDisponibilidade.EQUILIBRADA);
        svStatus.put(TipoEnergia.COGNITIVA, StatusDisponibilidade.EQUILIBRADA);
        svStatus.put(TipoEnergia.ATENCIONAL, StatusDisponibilidade.EQUILIBRADA);
        svStatus.put(TipoEnergia.EMOCIONAL, StatusDisponibilidade.ABUNDANTE);
        svStatus.put(TipoEnergia.RELACIONAL, StatusDisponibilidade.ABUNDANTE);
        DiagnosticoEnergetico diag_sv = e.diagnosticar("comunidade:solar_village", svStatus);
        System.out.println("  Entidade: " + diag_sv.entidade);
        System.out.println("  Em deficit: " + diag_sv.tipos_em_deficit.stream().map(t -> t.rotulo.split("\\(")[0].trim()).collect(Collectors.toList()));
        System.out.println("  Abundantes: " + diag_sv.tipos_abundantes.stream().map(t -> t.rotulo.split("\\(")[0].trim()).collect(Collectors.toList()));
        System.out.println("  VEREDITO: " + diag_sv.veredito);

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[SCORECARD DA TAXONOMIA ENERGETICA]");
        System.out.println("=".repeat(70));
        Map<String, Object> sc = e.scorecard();
        for (Map.Entry<String, Object> entry : sc.entrySet()) {
            System.out.println("  " + String.format("%-28s", entry.getKey() + ".") + " " + entry.getValue());
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("FILOSOFIA -- Energia e a bateria do trabalho");
        System.out.println("=".repeat(70));
        System.out.println("""
'Energia e a bateria do trabalho. Nosso corpo so funciona porque
temos energia. Nada foi feito na Terra por humanos sem a necessidade
de energia.'

O corpo humano nao tem UM sistema de energia. Tem DEZ.
Cada um com input, conversao, output e residuo.
A civilizacao herda essa estrutura -- somos um corpo em escala.

OpenEnergy cobre o sistema 1 (eletrico = ATP).
Mas existem outros 9 que a Republica precisa tratar:

NEURAL (sistema nervoso = internet):
  Quem controla a rede controla o sistema nervoso da civilizacao.
  Banda gratuita e NECESSARIA. A internet e o nervo. Sem nervo, paralisia.

COGNITIVA (cerebro = computacao):
  Processar informacao TEM CUSTO ENERGETICO. IA nao e gratuita.
  P8 exige que esse custo seja alocado democraticamente, nao por dinheiro.

ATENCIONAL (foco = atencao finita):
  A atencao e o recurso mais explorado do seculo XXI.
  Plataformas capturam sua atencao e vendem. Isso e EXTRATIVISMO ENERGETICO.
  FocusGuard e o comeco. Proteger atencao = proteger energia.

EMOCIONAL (motivacao = drive):
  Depressao e CRISE ENERGETICA. O combustivel existe (ATP), mas o motor
  nao liga (sem dopamina). Saude mental nao e luxo terapeutico --
  e INFRAESTRUTURA ENERGETICA. Sem motivacao, nenhuma outra energia se move.

RELACIONAL (social = conexao):
  O ser humano isolado DEGRADA. Conexao e necessidade energetica.
  A assembleia, o mutirao, a cooperativa sao GERADORES de energia relacional.
  P9 protege esta energia do atrito da polarizacao.

A LEI DE TODOS OS 10:
  INPUT -> CONVERSAO -> OUTPUT -> RESIDUO.
  Nada se cria, tudo se transforma.
  A Republica nao cria energia. TRANSFORMA.
  E transforma COM JUSTICA: sem desperdicio, sem exclusao, semElite.
""");
    }
}
