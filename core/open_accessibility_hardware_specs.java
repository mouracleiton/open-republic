// OpenAccessibilityHardwareSpecs.java
// Transpilacao fiel do Python para Java
// Especificacoes de Hardware COTS para Acessibilidade
// Todos os comentarios e strings em Portugues (conforme fonte)

import java.util.*;
import java.util.stream.Collectors;

public class OpenAccessibilityHardwareSpecs {

    // ========================================================================
    // 1. ENUMS
    // ========================================================================

    public enum CategoriaDispositivo {
        HEADPHONE_BT("headphone_bt", "Headphone Bluetooth"),
        SMARTPHONE("smartphone", "Smartphone"),
        SMARTWATCH("smartwatch", "Smartwatch"),
        EYE_TRACKER("eye_tracker", "Eye Tracker"),
        BRAILLE_DISPLAY("braille_display", "Display Braille"),
        SWITCH("switch", "Switch Button (botao de acesso)"),
        BONE_CONDUCTION("bone_conduction", "Fone de Conducao Ossea"),
        MICROFONE("microfone", "Microfone"),
        WEBCAM("webcam", "Webcam"),
        TABLET("tablet", "Tablet (CAA)"),
        E_READER("e_reader", "E-reader (Leitor Digital)"),
        GPS_TRACKER("gps_tracker", "GPS Tracker (Pessoal)");

        private final String id;
        private final String rotulo;

        CategoriaDispositivo(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
    }

    public enum DeficienciaAlvo {
        CEGUEIRA("cegueira", "Cego / Baixa visao"),
        SURDEZ("surdez", "Surdo / Deficiente auditivo"),
        MOTORA("motora", "Motora / Tetraplegia / Paralisia cerebral"),
        COGNITIVA("cognitiva", "Cognitiva / Sindrome de Down"),
        AUTISMO("autismo", "TEA / Autismo"),
        TDAH("tdah", "TDAH / Dislexia"),
        COMUNICACAO("comunicacao", "Comunicacao (nao-verbal / afasia)"),
        NEUROLOGICA("neurologica", "Neurologica (ELA / Parkinson / Epilepsia)"),
        IDOSO("idoso", "Idoso (demencia / mobilidade reduzida)"),
        CRIANCA("crianca", "Crianca (seguranca / rastreamento)"),
        UNIVERSAL("universal", "Uso universal (todas as deficiencias)");

        private final String id;
        private final String rotulo;

        DeficienciaAlvo(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
    }

    public enum NivelCusto {
        GRATUITO("gratuito", "Gratuito (doacao / biblioteca)", 0, 0),
        BAIXO("baixo", "Baixo custo (< R$ 100)", 1, 100),
        MEDIO("medio", "Custo medio (R$ 100-500)", 101, 500),
        ALTO("alto", "Custo alto (R$ 500-2000)", 501, 2000),
        PREMIUM("premium", "Premium (R$ 2000-10000)", 2001, 10000),
        ESPECIALIZADO("especializado", "Especializado (> R$ 10000)", 10001, 999999);

        private final String id;
        private final String rotulo;
        private final int minReal;
        private final int maxReal;

        NivelCusto(String id, String rotulo, int minReal, int maxReal) {
            this.id = id;
            this.rotulo = rotulo;
            this.minReal = minReal;
            this.maxReal = maxReal;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
        public int getMinReal() { return minReal; }
        public int getMaxReal() { return maxReal; }
    }

    public enum StatusSpec {
        CONFORME("conforme", "Conforme: atende todas as specs minimas"),
        PARCIAL("parcial", "Parcial: atende a maioria, mas tem lacunas"),
        NAO_CONFORME("nao_conforme", "Nao conforme: nao atende specs minimas"),
        RECOMENDADO("recomendado", "Recomendado: excede as specs minimas");

        private final String id;
        private final String rotulo;

        StatusSpec(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
    }

    // ========================================================================
    // 2. DATACLASSES (static inner classes)
    // ========================================================================

    public static class Especificacao {
        public final String parametro;
        public final String valorMinimo;
        public final boolean obrigatorio;
        public final String justificativa;

        public Especificacao(String parametro, String valorMinimo, boolean obrigatorio, String justificativa) {
            this.parametro = parametro;
            this.valorMinimo = valorMinimo;
            this.obrigatorio = obrigatorio;
            this.justificativa = justificativa;
        }
    }

    public static class ProdutoSuportado {
        public final String marca;
        public final String modelo;
        public final CategoriaDispositivo categoria;
        public final double precoAproxBrl;
        public final StatusSpec status;
        public final List<DeficienciaAlvo> deficienciasAtendidas;
        public final List<String> pontosFortes;
        public final List<String> pontosFracos;
        public final String notes;

        public ProdutoSuportado(String marca, String modelo, CategoriaDispositivo categoria,
                                double precoAproxBrl, StatusSpec status,
                                List<DeficienciaAlvo> deficienciasAtendidas,
                                List<String> pontosFortes, List<String> pontosFracos, String notes) {
            this.marca = marca;
            this.modelo = modelo;
            this.categoria = categoria;
            this.precoAproxBrl = precoAproxBrl;
            this.status = status;
            this.deficienciasAtendidas = deficienciasAtendidas != null ? deficienciasAtendidas : new ArrayList<>();
            this.pontosFortes = pontosFortes != null ? pontosFortes : new ArrayList<>();
            this.pontosFracos = pontosFracos != null ? pontosFracos : new ArrayList<>();
            this.notes = notes != null ? notes : "";
        }
    }

    public static class SpecDispositivo {
        public final CategoriaDispositivo categoria;
        public final String descricao;
        public final List<DeficienciaAlvo> deficienciasAtendidas;
        public final List<Especificacao> specs;
        public final List<ProdutoSuportado> produtos;
        public final double custoMinimoBrl;
        public final String observacao;

        public SpecDispositivo(CategoriaDispositivo categoria, String descricao,
                               List<DeficienciaAlvo> deficienciasAtendidas,
                               List<Especificacao> specs, List<ProdutoSuportado> produtos,
                               double custoMinimoBrl, String observacao) {
            this.categoria = categoria;
            this.descricao = descricao;
            this.deficienciasAtendidas = deficienciasAtendidas != null ? deficienciasAtendidas : new ArrayList<>();
            this.specs = specs != null ? specs : new ArrayList<>();
            this.produtos = produtos != null ? produtos : new ArrayList<>();
            this.custoMinimoBrl = custoMinimoBrl;
            this.observacao = observacao != null ? observacao : "";
        }
    }

    // ========================================================================
    // 3. DADOS: AS 12 ESPECIFICACOES (metodo estatico)
    // ========================================================================

    private static List<SpecDispositivo> initSpecs() {
        List<SpecDispositivo> specs = new ArrayList<>();

        // === 1. HEADPHONE BLUETOOTH ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.HEADPHONE_BT,
            "Headphone Bluetooth para acessibilidade auditiva. Usado para TTS (text-to-speech), audio descricao, legendas em audio, amplificacao para deficiente auditivo, e comunicacao com o Telefonista.",
            Arrays.asList(DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.UNIVERSAL, DeficienciaAlvo.IDOSO),
            Arrays.asList(
                new Especificacao("Bluetooth", "5.0 ou superior (LE Audio / aptX Adaptive)", true, "LE Audio reduz latencia e permite multi-stream (2 fones no mesmo dispositivo)."),
                new Especificacao("Latencia", "< 200ms (ideal < 150ms)", true, "Latencia alta quebra TTS em tempo real e audio descricao sincronizada."),
                new Especificacao("Bateria", "Minimo 8h uso continuo", true, "Dia de trabalho/estudo sem recarregar. Cego depende do fone o dia todo."),
                new Especificacao("Microfone integrado", "Sim, com cancelamento de ruido", true, "Para comando de voz, chamadas, e Libras por contexto de audio."),
                new Especificacao("Perfil Bluetooth", "A2DP + HFP + AVRCP", true, "A2DP = audio de qualidade. HFP = viva-voz. AVRCP = controle remoto."),
                new Especificacao("Multiponto", "Sim (conectar 2 dispositivos simultaneamente)", true, "Cego pode estar conectado ao smartphone E ao computador ao mesmo tempo."),
                new Especificacao("Controles fisicos", "Botoes reais (nao touch)", true, "Cego nao pode usar controles capacitivos sem feedback visual."),
                new Especificacao("Feedback de bateria", "Anuncio de bateria por voz ou tom", true, "Cego precisa saber quando vai acabar sem ver o LED."),
                new Especificacao("Conforto", "Ajustavel, leve (< 300g), alcolchoado", true, "Uso prolongado (8h+) requer conforto. Pessoas com sensibilidade sensorial (TEA) precisam de materiais suaves."),
                new Especificacao("Codec", "SBC minimo. AAC/SBC/LDAC desejavel", false, "AAC melhora qualidade para usuarios de iPhone."),
                new Especificacao("Resistencia", "IPX4 (suor e chuva)", false, "Para uso em mobilidade urbana."),
                new Especificacao("Jack 3.5mm", "Sim (backup com fio)", true, "Se Bluetooth falha, fio e backup. Cego nao pode ficar sem audio.")
            ),
            Arrays.asList(
                new ProdutoSuportado("JBL", "Tune 510BT", CategoriaDispositivo.HEADPHONE_BT, 250, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("Bateria 40h", "Multiponto", "Custo acessivel", "Jack 3.5mm"),
                    Arrays.asList("Sem anuncio de bateria por voz", "Controle touch (parcial)"), ""),
                new ProdutoSuportado("Sony", "WH-CH520", CategoriaDispositivo.HEADPHONE_BT, 350, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL, DeficienciaAlvo.SURDEZ),
                    Arrays.asList("Bateria 50h", "Multiponto", "Anuncio de bateria por voz", "Controles fisicos"),
                    Arrays.asList("Sem jack 3.5mm (USB-C apenas)"), ""),
                new ProdutoSuportado("Sennheiser", "HD 350BT", CategoriaDispositivo.HEADPHONE_BT, 500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("Bateria 30h", "AAC + aptX", "Confortavel 8h+", "USB-C charge"),
                    Arrays.asList("Sem jack 3.5mm"), ""),
                new ProdutoSuportado("Anker", "Soundcore Life Q20", CategoriaDispositivo.HEADPHONE_BT, 250, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("Bateria 40h", "ANC basico", "Custo baixo"),
                    Arrays.asList("Multiponto instavel", "App requer visual"), ""),
                new ProdutoSuportado("Philips", "SHL3070BK", CategoriaDispositivo.HEADPHONE_BT, 150, StatusSpec.PARCIAL,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("Custo muito baixo", "Jack 3.5mm"),
                    Arrays.asList("Bateria 9h (minimo)", "Sem multiponto", "Latencia alta para TTS"), ""),
                new ProdutoSuportado("Apple", "AirPods (2nd gen)", CategoriaDispositivo.HEADPHONE_BT, 1500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("Acessibilidade iOS nativa", "Live Listen (microfone remoto)", "Audio descricao integrada", "Detecao de sons (Porta, Cachorro, Sirene)"),
                    Arrays.asList("Custo alto", "Sem controles fisicos (touch)", "Bateria ~5h por carga (24h com case)"), ""),
                new ProdutoSuportado("Apple", "AirPods Pro 2", CategoriaDispositivo.HEADPHONE_BT, 2500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("Live Listen", "ANC adaptativo", "Modo Conversacao (transparencia)", "Detecao de sons ambiente"),
                    Arrays.asList("Custo premium", "Sem jack 3.5mm"), ""),
                new ProdutoSuportado("Samsung", "Galaxy Buds FE", CategoriaDispositivo.HEADPHONE_BT, 600, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("Live Listen no Android", "ANC", "Custo medio"),
                    Arrays.asList("Bateria ~6h por carga", "Sem jack"), "")
            ),
            80.0,
            "O Headphone Bluetooth e o DISPOSITIVO MAIS UNIVERSAL da acessibilidade. Cego usa para TTS. Surdo usa para amplificacao e Live Listen. Tetraplegico usa para comando de voz. Idoso usa para amplificacao. A spec minima garante que QUALQUER headphone recomendado funciona para TODOS."
        ));

        // === 2. SMARTPHONE ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.SMARTPHONE,
            "Smartphone como CORPO ESTENDIDO (Telefonista). Camera=olhos, microfone=ouvidos, GPS=direcao, acelerometro=balance, smartwatch=biometria.",
            Arrays.asList(DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.SURDEZ, DeficienciaAlvo.MOTORA, DeficienciaAlvo.AUTISMO, DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.IDOSO, DeficienciaAlvo.CRIANCA, DeficienciaAlvo.UNIVERSAL),
            Arrays.asList(
                new Especificacao("Sistema operacional", "Android 13+ ou iOS 16+", true, "Versoes antigas nao tem features de acessibilidade criticas."),
                new Especificacao("RAM", "Minimo 4GB (ideal 6GB+)", true, "Apps de acessibilidade (TalkBack, VoiceOver, Libras) consomem RAM."),
                new Especificacao("Armazenamento", "Minimo 64GB", true, "Modelos de IA local + apps de CAA + mapas offline precisam de espaco."),
                new Especificacao("Camera", "Minimo 12MP com autofocus + OIS", true, "Visao computacional (OCR, descricao de cena, Libras) precisa de camera decente."),
                new Especificacao("Bateria", "Minimo 4000mAh", true, "Dia inteiro de uso com acessibilidade ativa (TTS + GPS + camera)."),
                new Especificacao("TalkBack/VoiceOver", "Nativo e funcional", true, "Leitor de tela nativo e OBRIGATORIO. Sem ele, cego nao usa o telefone."),
                new Especificacao("Bluetooth", "5.0+", true, "Para conectar headphones, hearing aids, braille displays."),
                new Especificacao("GPS", "Sim, com A-GPS", true, "Navegacao para cego, rastreamento de crianca/idoso."),
                new Especificacao("NFC", "Sim", false, "Pagamento sem QR code (OpenAntiQRPayment)."),
                new Especificacao("Acelerometro/Giroscopio", "Sim", true, "Deteccao de queda (idoso), bussola para navegacao (cego)."),
                new Especificacao("Slot microSD", "Desejavel", false, "Armazenamento expansivel para mapas offline e modelos de IA."),
                new Especificacao("Radio FM", "Desejavel (com fone como antena)", false, "Emergencias: FM nao depende de internet.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Samsung", "Galaxy A15 5G", CategoriaDispositivo.SMARTPHONE, 1000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("Custo baixo", "Android 14", "Bateria 5000mAh", "TalkBack nativo", "Camera 50MP", "Slot microSD"),
                    Arrays.asList("RAM 4GB (minimo)", "Sem OIS na camera"), ""),
                new ProdutoSuportado("Samsung", "Galaxy A55 5G", CategoriaDispositivo.SMARTPHONE, 2000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("RAM 8GB", "Camera com OIS", "Bateria 5000mAh", "Bixby Vision (descricao de cena)", "Modo Live Listen"),
                    Arrays.asList("Sem slot microSD (alguns mercados)"), ""),
                new ProdutoSuportado("Motorola", "Moto G84 5G", CategoriaDispositivo.SMARTPHONE, 1300, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("RAM 8GB (otimo nesta faixa)", "Bateria 5000mAh", "Android limpo (TalkBack funciona bem)", "Slot microSD"),
                    Arrays.asList("Camera sem OIS"), ""),
                new ProdutoSuportado("Apple", "iPhone SE (2022)", CategoriaDispositivo.SMARTPHONE, 3000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("VoiceOver (melhor leitor de tela do mercado)", "Detecao de pessoas, portas, sons (Magnifier)", "Audio descricao", "Live Listen", "5 anos de update"),
                    Arrays.asList("Bateria 2018mAh (fraca)", "Tela 4.7 polegadas (pequena)"), ""),
                new ProdutoSuportado("Apple", "iPhone 15", CategoriaDispositivo.SMARTPHONE, 5000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("VoiceOver + Magnifier + Detecao de sons", "LiDAR (navegacao para cego)", "Camera 48MP", "USB-C", "Live Listen"),
                    Arrays.asList("Custo premium"), ""),
                new ProdutoSuportado("Xiaomi", "Redmi Note 13", CategoriaDispositivo.SMARTPHONE, 1100, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("Custo baixo", "Bateria 5000mAh", "Camera 108MP", "Slot microSD"),
                    Arrays.asList("MIUI tem bugs de acessibilidade", "TalkBack menos testado"), "")
            ),
            800.0,
            "O smartphone e o CORACAO da acessibilidade da Republica. E camera, microfone, GPS, acelerometro, TTS, leitor de tela -- tudo num so dispositivo. A spec garante que QUALQUER smartphone recomendado roda a stack do Telefonista."
        ));

        // === 3. SMARTWATCH ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.SMARTWATCH,
            "Smartwatch para biometria continua: estresse (frequencia cardiaca), predicao de convulsao (temperatura + HR), deteccao de queda (idoso), lembretes (TDAH, idoso com demencia).",
            Arrays.asList(DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.IDOSO, DeficienciaAlvo.TDAH, DeficienciaAlvo.AUTISMO, DeficienciaAlvo.MOTORA),
            Arrays.asList(
                new Especificacao("Sensor cardiaco", "Sim (PPG ou ECG)", true, "Deteccao de estresse, arritmia, taquicardia."),
                new Especificacao("Acelerometro", "Sim (3 eixos)", true, "Deteccao de queda (idoso), tremor (Parkinson)."),
                new Especificacao("GPS", "Sim (integrado)", true, "Rastreamento de crianca/idoso sem depender do smartphone."),
                new Especificacao("Bateria", "Minimo 3 dias (ideal 7+)", true, "Biometria continua requer uso 24h. Recarga diaria e falha."),
                new Especificacao("Resistencia", "IP68 (agua e poeira)", true, "Usa no banho, na chuva, na piscina. Biometria nao para."),
                new Especificacao("Vibracao", "Motor haptico forte", true, "Surdo nao ouve alerta. Cego nao ve. Vibration e universal."),
                new Especificacao("Tela sempre ligada", "Desejavel", false, "Idoso precisa ver as horas sem tocar na tela."),
                new Especificacao("Temperatura corporea", "Desejavel", false, "Predicao de convulsao epileptica (pesquisa Apple Watch)."),
                new Especificacao("SpO2 (oximetria)", "Desejavel", false, "Monitoramento respiratorio.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Amazfit", "Bip 5", CategoriaDispositivo.SMARTWATCH, 500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.IDOSO, DeficienciaAlvo.TDAH),
                    Arrays.asList("Bateria 10 DIAS", "GPS", "Tela grande (1.69 polegadas)", "Custo baixo", "Vibracao forte"),
                    Arrays.asList("Sem ECG", "Sem SpO2 confiavel"), ""),
                new ProdutoSuportado("Xiaomi", "Smart Band 8", CategoriaDispositivo.SMARTWATCH, 250, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.IDOSO, DeficienciaAlvo.TDAH),
                    Arrays.asList("Bateria 16 DIAS", "Custo muito baixo", "HR + SpO2", "Leve (27g)"),
                    Arrays.asList("Sem GPS integrado (depende do telefone)", "Tela pequena para idoso com baixa visao"), ""),
                new ProdutoSuportado("Apple", "Apple Watch SE (2nd gen)", CategoriaDispositivo.SMARTWATCH, 2500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.IDOSO),
                    Arrays.asList("Deteccao de queda (SOS automatico)", "ECG (aprovado FDA)", "GPS integrado", "Vibracao excelente", "Tela sempre ligada"),
                    Arrays.asList("Bateria ~18h (1 dia)", "Custo alto"), ""),
                new ProdutoSuportado("Apple", "Apple Watch Series 9", CategoriaDispositivo.SMARTWATCH, 4500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.NEUROLOGICA),
                    Arrays.asList("ECG + SpO2 + Temperatura", "Deteccao de queda + SOS", "GPS", "Health Records (compartilha com medico)"),
                    Arrays.asList("Bateria ~18h", "Custo premium"), ""),
                new ProdutoSuportado("Samsung", "Galaxy Watch FE", CategoriaDispositivo.SMARTWATCH, 1000, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.IDOSO),
                    Arrays.asList("ECG (em alguns paises)", "Bateria 2-3 dias", "Deteccao de queda", "Android nativo"),
                    Arrays.asList("ECG bloqueado em alguns mercados"), ""),
                new ProdutoSuportado("Garmin", "Forerunner 55", CategoriaDispositivo.SMARTWATCH, 1500, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.IDOSO),
                    Arrays.asList("Bateria 14 DIAS em modo watch", "GPS de precisao", "Vibracao forte"),
                    Arrays.asList("Foco em esporte (menos features de saude)"), "")
            ),
            400.0,
            "Smartwatch = biometria PASSIVA. O usuario nao precisa fazer nada. O relogio detecta queda e chama socorro. Detecta arritmia e avisa. E o sensor do corpo que o corpo nao tem (ou perdeu)."
        ));

        // === 4. EYE TRACKER ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.EYE_TRACKER,
            "Eye tracker para tetraplegia, ELA, paralisia cerebral. O olho e o ultimo musculo voluntario em ELA. Eye tracker permite digitar, clicar, comunicar -- SO COM OS OLHOS.",
            Arrays.asList(DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.COMUNICACAO),
            Arrays.asList(
                new Especificacao("Precisao", "< 1 grau visual (ideal < 0.5)", true, "Para clicar em botoes pequenos na tela. Precisao baixa = frustracao."),
                new Especificacao("Frequencia", "Minimo 60Hz (ideal 120Hz+)", true, "Taxa de atualizacao. Baixa = lag entre olhar e clique."),
                new Especificacao("Calibracao", "Automatica ou 1-5 pontos", true, "Calibracao complexa (16 pontos) e exaustiva para quem tem mobilidade limitada."),
                new Especificacao("Compatibilidade", "Windows + macOS + Linux", true, "Nao pode prender o usuario num SO."),
                new Especificacao("Software inclusivo", "Teclado virtual + CAA", true, "Eye tracker sem software de comunicacao e so hardware inutil."),
                new Especificacao("Latencia", "< 50ms", true, "Entre o olhar e o cursor responder. Alto = nauseas."),
                new Especificacao("Trabalha com oculos", "Sim", true, "Muitos usuarios de eye tracker usam oculos."),
                new Especificacao("Headbox", "Minimo 25x25cm", true, "Area de liberdade de movimento da cabeca. Pequeno = usuario precisa ficar imovel.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Tobii", "Eye Tracker 5", CategoriaDispositivo.EYE_TRACKER, 3500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA),
                    Arrays.asList("Precisao < 0.5 grau", "144Hz", "Headbox amplo", "Software Tobii Communicator (CAA)", "Trabalha com oculos"),
                    Arrays.asList("Custo alto", "Windows-centric (Linux parcial)"), ""),
                new ProdutoSuportado("Tobii", "Dynavox", CategoriaDispositivo.EYE_TRACKER, 15000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.COMUNICACAO),
                    Arrays.asList("Solucao completa (tablet + eye tracker + CAA)", "Snap Core First (CAA)", "Suporte clinico"),
                    Arrays.asList("Custo ESPECIALIZADO", "Fornecedor unico"), ""),
                new ProdutoSuportado("IRISBOND", "Hiru", CategoriaDispositivo.EYE_TRACKER, 5000, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.MOTORA),
                    Arrays.asList("Precisao < 0.5 grau", "Multiplataforma", "Usado em hospitais brasileiros"),
                    Arrays.asList("Disponibilidade limitada no Brasil"), ""),
                new ProdutoSuportado("Windows", "Eye Control (nativo)", CategoriaDispositivo.EYE_TRACKER, 0, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.MOTORA),
                    Arrays.asList("GRATUITO no Windows 10/11", "Funciona com Tobii 4C e EyeX"),
                    Arrays.asList("So funciona com hardware Tobii", "Limitado a Windows"), ""),
                new ProdutoSuportado("Apple", "iPad com AssistiveTouch (olhos)", CategoriaDispositivo.EYE_TRACKER, 5000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.MOTORA),
                    Arrays.asList("Eye Tracking nativo no iPadOS (2024+)", "GRATUITO (incluido no iPad)", "CAA integrada"),
                    Arrays.asList("So funciona em iPad Pro/Air recentes", "Precisao pode variar"), "")
            ),
            2000.0,
            "Eye tracker e o DISPOSITIVO QUE DEVOLVE A VOZ. Pessoa com ELA perde tudo -- bracos, pernas, voz. Sobra o olhar. Eye tracker transforma olhar em palavras."
        ));

        // === 5. BRAILLE DISPLAY ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.BRAILLE_DISPLAY,
            "Display Braille para cegos. Converte texto digital em celas braille táteis. E o OUTPUT equivalente ao leitor de tela -- mas para quem prefere ou precisa ler pelo tato (surdos-cegos nao tem audio).",
            Arrays.asList(DeficienciaAlvo.CEGUEIRA),
            Arrays.asList(
                new Especificacao("Celas", "Minimo 8 celas (ideal 40+)", true, "8 celas = palavra por vez. 40+ = linha inteira. Mais celas = leitura fluida."),
                new Especificacao("Tipo de cela", "Piezoeletrica (8 pinos por cela)", true, "Braille de 8 pontos (computador). 6 pontos so perde informacao de formatacao."),
                new Especificacao("Conexao", "Bluetooth + USB", true, "Bluetooth para smartphone. USB para computador. Ambos necessarios."),
                new Especificacao("Bateria", "Minimo 10h", true, "Dia de trabalho/estudo. Recarga no meio do dia e falha."),
                new Especificacao("Botoes de navegacao", "Sim (pan, rota, cursor routing)", true, "Navegar pelo texto sem depender do smartphone."),
                new Especificacao("Compatibilidade", "TalkBack (Android) + VoiceOver (iOS) + NVDA/JAWS (PC)", true, "Display Braille sem leitor de tela e so pinos. Precisa do SOFTWARE.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Orbit Research", "Orbit Reader 20 Plus", CategoriaDispositivo.BRAILLE_DISPLAY, 4000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("20 celas (bom para custo)", "BLUETOOTH + USB", "Bateria 20h", "Custo mais baixo do mercado para Braille", "Nota: armazenamento interno (le sem smartphone)"),
                    Arrays.asList("20 celas limita leitura longa", "Sem teclado Perkins integrado"), ""),
                new ProdutoSuportado("Help Tech", "Active Star 40", CategoriaDispositivo.BRAILLE_DISPLAY, 12000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("40 celas (leitura fluida)", "Bluetooth + USB", "Teclado Perkins integrado", "Bateria 20h+", "Wi-Fi (le RSS, email)"),
                    Arrays.asList("Custo ESPECIALIZADO"), ""),
                new ProdutoSuportado("Freedom Scientific", "Focus 40 Blue", CategoriaDispositivo.BRAILLE_DISPLAY, 10000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("40 celas", "Bluetooth + USB", "Compativel com JAWS + NVDA + VoiceOver + TalkBack"),
                    Arrays.asList("Custo ESPECIALIZADO"), ""),
                new ProdutoSuportado("Seika", "Seika 40", CategoriaDispositivo.BRAILLE_DISPLAY, 6000, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("40 celas", "Custo mais baixo para 40 celas", "Bluetooth + USB"),
                    Arrays.asList("Qualidade de build inferior", "Suporte limitado no Brasil"), ""),
                new ProdutoSuportado("Apple", "iPhone/iPad com Braille (software)", CategoriaDispositivo.BRAILLE_DISPLAY, 0, StatusSpec.PARCIAL,
                    Arrays.asList(DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("GRATUITO no iOS", "Mostra Braille na tela (para videntes aprenderem)", "Conecta com display fisico via Bluetooth"),
                    Arrays.asList("Nao e Braille TATIL (so visual)", "Para cego real, precisa do display fisico"), "")
            ),
            3000.0,
            "Display Braille e o UNICO OUTPUT para SURDO-CEGO. Surdo-cego nao tem audio (surdo) nem tela (cego). Sobra o TATO. Display Braille e a janela para o mundo digital. O custo e alto (R$ 4000-15000) -- a Republica precisa subsidiar."
        ));

        // === 6. SWITCH BUTTON ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.SWITCH,
            "Switch button: botao grande de 1 toque para acesso. Para tetraplegia severa, paralisia cerebral, ELA avancada. 1 toque = 1 acao. O computador escaneia opcoes e o usuario toca o switch na opcao certa.",
            Arrays.asList(DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.COMUNICACAO),
            Arrays.asList(
                new Especificacao("Forca de ativacao", "Maximo 100g (ideal < 50g)", true, "Usuario com paralisia cerebral pode nao conseguir apertar botao duro."),
                new Especificacao("Tamanho da superficie", "Minimo 5cm diametro", true, "Alvo grande para quem tem tremor ou movimento involuntario."),
                new Especificacao("Feedback", "Tatil (click) + auditivo (click) + visual (LED)", true, "O usuario PRECISA saber que ativou. Multi-modal."),
                new Especificacao("Conexao", "Bluetooth e/ou Jack 3.5mm", true, "Jack 3.5mm = compatibilidade universal (AT, switch-adapted toys). BT = sem fio."),
                new Especificacao("Resistencia", "A prova de impacto e saliva", true, "Usuario pode ter espasmo. Crianca pode morder/bater."),
                new Especificacao("Montagem", "Compativel com braços articulados e suportes", true, "Switch precisa ser posicionado onde o usuario tem movimento."),
                new Especificacao("Bateria", "Minimo 100h (ideal: meses)", true, "Switch com fio nao precisa. Switch BT precisa durar semanas.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Ablenet", "Big Red Switch", CategoriaDispositivo.SWITCH, 400, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.MOTORA),
                    Arrays.asList("Padrao da industria de AT", "Superficie 12.7cm", "Forca ~57g", "Jack 3.5mm", "Resistente"),
                    Arrays.asList("Custo alto para um botao"), ""),
                new ProdutoSuportado("Ablenet", "Spec Switch", CategoriaDispositivo.SWITCH, 350, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.MOTORA),
                    Arrays.asList("Superficie 5cm", "Forca muito baixa (~21g)", "Ideal para ELA avancada"),
                    Arrays.asList("Custo alto"), ""),
                new ProdutoSuportado("Enabling Devices", "Jelly Bean Switch", CategoriaDispositivo.SWITCH, 300, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.MOTORA),
                    Arrays.asList("Superficie 6.5cm", "Cores vivas (baixa visao)", "Jack 3.5mm"),
                    Arrays.asList("Feedback menos firme que Ablenet"), ""),
                new ProdutoSuportado("DIY", "Switch caseiro (pizza box + foil)", CategoriaDispositivo.SWITCH, 20, StatusSpec.PARCIAL,
                    Arrays.asList(DeficienciaAlvo.MOTORA),
                    Arrays.asList("Custo MUITO baixo", "Customizavel", "Tutorial aberto (CC0)"),
                    Arrays.asList("Durabilidade baixa", "Precisa manutencao frequente", "Sem feedback de qualidade"), ""),
                new ProdutoSuportado("Logitech", "Adaptive Gaming Kit", CategoriaDispositivo.SWITCH, 600, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.MOTORA),
                    Arrays.asList("3 switches grandes + 5 pequenos", "Abas de etiqueta (identificacao tatil)", "Custo razoavel para kit completo"),
                    Arrays.asList("Foco em gaming (adaptavel para AT)"), "")
            ),
            100.0,
            "Switch e o DISPOSITIVO MAIS SIMPLES E MAIS PODEROSO. 1 botao. 1 acao. Para quem so move 1 musculo (cabeca, braco, pe, sopro). Scanning: o computador mostra opcoes uma a uma. Switch na opcao certa = SELECAO. Comunicacao, controle, autonomia."
        ));

        // === 7. BONE CONDUCTION ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.BONE_CONDUCTION,
            "Fone de conducao ossea: som viaja pelo osso (cranio) ate o nervo auditivo, bypassando o ouvido externo e medio. Para surdo CONDUTIVO (problema no ouvido medio), estenose do canal, otite cronica. NAO funciona para surdo NEUROSSENSORIAL severo.",
            Arrays.asList(DeficienciaAlvo.SURDEZ),
            Arrays.asList(
                new Especificacao("Bluetooth", "5.0+", true, "Conexao estavel para TTS e audio descricao."),
                new Especificacao("Orelha aberta", "Sim (nao bloqueia canal auditivo)", true, "Cego que usa conducao ossea PRECISA ouvir o ambiente tambem."),
                new Especificacao("Bateria", "Minimo 6h", true, "Dia de uso continuo."),
                new Especificacao("Microfone", "Sim", true, "Para comando de voz e chamadas."),
                new Especificacao("Conforto", "Ajustavel, leve (< 40g)", true, "Repouso na teca (osso temporal). Pressao inadequada = dor."),
                new Especificacao("Resistencia", "IPX4+ (suor)", true, "Uso em atividade fisica e mobilidade urbana.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Shokz", "OpenRun Pro", CategoriaDispositivo.BONE_CONDUCTION, 1200, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.SURDEZ),
                    Arrays.asList("Lider em conducao ossea", "Bateria 10h", "Bluetooth 5.1", "Microfone", "IP67"),
                    Arrays.asList("Custo alto"), ""),
                new ProdutoSuportado("Shokz", "OpenMove", CategoriaDispositivo.BONE_CONDUCTION, 600, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.SURDEZ),
                    Arrays.asList("Custo medio", "Bateria 6h", "Bluetooth 5.1", "IP55"),
                    Arrays.asList("Qualidade de som inferior ao OpenRun Pro"), ""),
                new ProdutoSuportado("Mojawa", "Run Plus", CategoriaDispositivo.BONE_CONDUCTION, 1000, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.SURDEZ),
                    Arrays.asList("Bateria 8h", "IP68", "MP3 integrado (16GB)"),
                    Arrays.asList("Marca menos estabelecida"), "")
            ),
            500.0,
            "Conducao ossea e PARA SURDO CONDUTIVO especificamente. Surdo neurosensorial severo NAO beneficia. Importante: cego que tambem e surdo condutivo pode usar conducao ossea e AINDA ouvir o ambiente (orelha aberta)."
        ));

        // === 8. MICROFONE ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.MICROFONE,
            "Microfone para comando de voz, fala-para-texto, e captura de audio ambiente para o Telefonista. Para tetraplegico que so fala. Para surdo que precisa de legenda em tempo real. Para cego que interage por voz.",
            Arrays.asList(DeficienciaAlvo.MOTORA, DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.COMUNICACAO),
            Arrays.asList(
                new Especificacao("Cancelamento de ruido", "Sim (DSP ou cardiode)", true, "Comando de voz em ambiente ruidoso precisa de CNR."),
                new Especificacao("Conexao", "USB ou Bluetooth", true, "USB = zero latencia. BT = mobilidade."),
                new Especificacao("Padrao polar", "Cardiode ou unidirecional", true, "Captura a voz do usuario, nao o ambiente inteiro."),
                new Especificacao("Frequencia", "100Hz-10kHz minimo", true, "Cobre voz humana. Baixa frequencia = graves (homem). Alta = agudos (mulher/crianca)."),
                new Especificacao("Mute fisico", "Botao de mute REAL (nao software)", true, "Privacidade: usuario PRECISA saber que o microfone esta mudo.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Blue", "Yeti Nano", CategoriaDispositivo.MICROFONE, 500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.MOTORA, DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("USB-C", "Cardiode + omnidirecional", "Mute fisico (botao na frente)", "Qualidade excelente"),
                    Arrays.asList("Grande (ocupa espaco na mesa)"), ""),
                new ProdutoSuportado("Fifine", "K669B", CategoriaDispositivo.MICROFONE, 150, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.MOTORA),
                    Arrays.asList("Custo MUITO baixo", "USB", "Cardiode", "Tripé incluido"),
                    Arrays.asList("Sem mute fisico", "Qualidade decente mas nao premium"), ""),
                new ProdutoSuportado("Jabra", "Speak 510", CategoriaDispositivo.MICROFONE, 700, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.MOTORA, DeficienciaAlvo.SURDEZ),
                    Arrays.asList("Bluetooth + USB", "CNR excelente", "Speakerphone (para reuniao com legenda)", "Mute fisico"),
                    Arrays.asList("Custo medio-alto"), ""),
                new ProdutoSuportado("In_build", "Microfone do smartphone", CategoriaDispositivo.MICROFONE, 0, StatusSpec.PARCIAL,
                    Arrays.asList(DeficienciaAlvo.UNIVERSAL),
                    Arrays.asList("GRATUITO", "Sempre presente", "Portatil"),
                    Arrays.asList("Qualidade varia", "CNR limitado", "Nao ideal para texto longo"), "")
            ),
            50.0,
            "Microfone e a ENTRADA para quem SO FALA. Tetraplegico que nao digita, FALA. Precisa de microfone bom. Surdo que precisa de legenda em tempo real, precisa capturar audio. Cego que navega por voz, precisa de microfone confiavel."
        ));

        // === 9. WEBCAM ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.WEBCAM,
            "Webcam para Libras (surdo se comunica por sinais na camera), visao computacional (descricao de cena para cego), e rastreamento de mao (linguagem de sinais como input).",
            Arrays.asList(DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA),
            Arrays.asList(
                new Especificacao("Resolucao", "Minimo 720p (ideal 1080p)", true, "Libras requer resolucao suficiente para ver expressoes faciais e maos."),
                new Especificacao("Frequencia", "Minimo 30fps (ideal 60fps)", true, "Libras e RAPIDO. 15fps perde sinais. 60fps captura tudo."),
                new Especificacao("Autofocus", "Sim (rapido)", true, "Surdo que se move ao sinais nao pode ficar borrado."),
                new Especificacao("Campo de visao", "Minimo 70 graus (ideal 90+)", true, "Libras requer espaco para maos e bracos. Webcam estreita corta os sinais."),
                new Especificacao("Baixa luz", "Funciona em < 50 lux", true, "Nem todos tem iluminacao de estudio. Sala de casa a noite."),
                new Especificacao("Microfone integrado", "Desejavel (backup)", false, "Para videochamada com surdo (audio + Libras simultaneo).")
            ),
            Arrays.asList(
                new ProdutoSuportado("Logitech", "C920 HD Pro", CategoriaDispositivo.WEBCAM, 400, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("1080p 30fps", "Autofocus rapido", "Campo 78 graus", "Excelente baixa luz", "Microfone stereo"),
                    Arrays.asList("Sem 60fps em 1080p"), ""),
                new ProdutoSuportado("Logitech", "C922 Pro", CategoriaDispositivo.WEBCAM, 500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.SURDEZ),
                    Arrays.asList("1080p 30fps / 720p 60fps", "Fundo substituivel", "Tripé incluido"),
                    Arrays.asList("Custo medio-alto"), ""),
                new ProdutoSuportado("Microsoft", "LifeCam Studio", CategoriaDispositivo.WEBCAM, 600, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.SURDEZ),
                    Arrays.asList("1080p", "Campo 75 graus", "Alta qualidade de build"),
                    Arrays.asList("Descontinuado pela Microsoft (suporte incerto)"), ""),
                new ProdutoSuportado("In_build", "Webcam do notebook/smartphone", CategoriaDispositivo.WEBCAM, 0, StatusSpec.PARCIAL,
                    Arrays.asList(DeficienciaAlvo.SURDEZ),
                    Arrays.asList("GRATUITO", "Sempre presente"),
                    Arrays.asList("Qualidade varia muito", "Campo de visao estreito em notebooks", "Autofocus lento em cameras baratas"), "")
            ),
            150.0,
            "Webcam e a JANELA para Libras. Surdo se comunica por SINAIS. Sinais precisam de FRAMES RAPIDOS e CAMPO AMPLO. Webcam ruim = comunicacao cortada = exclusao."
        ));

        // === 10. TABLET (CAA) ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.TABLET,
            "Tablet para CAA (Comunicacao Aumentativa e Alternativa). Para nao-verbal (autismo nao-verbal, afasia, ELA). Toca figura/simbolo -> fala a palavra. Ou digita -> fala.",
            Arrays.asList(DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.AUTISMO, DeficienciaAlvo.COGNITIVA, DeficienciaAlvo.NEUROLOGICA),
            Arrays.asList(
                new Especificacao("Tela", "Minimo 10 polegadas", true, "Espaco para grade de simbolos CAA (minimo 8x8)."),
                new Especificacao("Touch", "Multitoque capacitivo (sensivel)", true, "Usuario com motora fina comprometida precisa de tela responsiva."),
                new Especificacao("Bateria", "Minimo 8h", true, "Dia de uso (escola, trabalho, terapia)."),
                new Especificacao("Sintetizador de voz", "Nativo + apps CAA", true, "Tablet sem TTS e so uma tela. Precisa FALAR."),
                new Especificacao("Software CAA", "Compativel com: Avaz, Proloquo, TD Snap", true, "Apps de CAA sao OBRIGATORIOS. Tablet sem apps CAA nao serve."),
                new Especificacao("Case protetor", "Case resistente a queda (military-grade)", true, "Crianca com autismo pode ter comportamento de quebrar. Tablet = R$ 1000+."),
                new Especificacao("Suporte", "Compativel com suportes de mesa/mobiliario", true, "Cadeirante precisa do tablet montado na cadeira.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Apple", "iPad (10th gen)", CategoriaDispositivo.TABLET, 3000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.AUTISMO),
                    Arrays.asList("Melhor ecossistema de CAA do mercado", "Proloquo2Go (padrao ouro CAA)", "Avaz", "AssistiveTouch + Eye Tracking nativo", "Bateria 10h", "Case Logitech Crayon"),
                    Arrays.asList("Custo alto"), ""),
                new ProdutoSuportado("Samsung", "Galaxy Tab A9+", CategoriaDispositivo.TABLET, 1000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.AUTISMO),
                    Arrays.asList("Custo baixo para tablet", "Tela 11 polegadas", "Android (Avaz, TD Snap)", "Bateria 10h+"),
                    Arrays.asList("Menos apps CAA que iOS", "Case protetor menos disponivel"), ""),
                new ProdutoSuportado("Apple", "iPad Pro 11", CategoriaDispositivo.TABLET, 7000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.MOTORA),
                    Arrays.asList("Eye Tracking nativo (2024+)", "Proloquo2Go + Voice Control", "M-series chip (rapido)", "LiDAR"),
                    Arrays.asList("Custo PREMIUM"), ""),
                new ProdutoSuportado("Amazon", "Fire HD 10", CategoriaDispositivo.TABLET, 600, StatusSpec.PARCIAL,
                    Arrays.asList(DeficienciaAlvo.AUTISMO),
                    Arrays.asList("Custo MUITO baixo", "Tela 10.1 polegadas"),
                    Arrays.asList("Sem Google Play nativo (apps CAA limitados)", "Sem Proloquo2Go (iOS only)", "Android fork (Fire OS)"), "")
            ),
            800.0,
            "Tablet CAA e a VOZ de quem nao fala. Crianca autista nao-verbal toca 'QUERO AGUA'. Tablet FALA: 'Quero agua'. Pessoa com ELA digita com os olhos. Tablet FALA a mensagem. Sem tablet CAA, a pessoa e PRISIONEIRA do silencio."
        ));

        // === 11. E-READER ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.E_READER,
            "E-reader (tela e-ink) para dislexia, baixa visao, daltonismo. Tela e-ink nao emite luz (nao cansa). Fonte pode ser ampliada sem limite. OpenDyslexic font ajuda dislexico a distinguir letras.",
            Arrays.asList(DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.AUTISMO, DeficienciaAlvo.IDOSO),
            Arrays.asList(
                new Especificacao("Tela", "E-ink (nao LCD/LED)", true, "E-ink nao emite luz azul. Nao cansa. Dislexico e TDAH sao sensivel a luz."),
                new Especificacao("Fonte ajustavel", "Sim (tamanho + familia + espacamento)", true, "OpenDyslexic, Atkinson Hyperlegible, espacamento entre linhas."),
                new Especificacao("Tamanho de fonte", "Ate minimo 36pt", true, "Baixa visao precisa de fonte grande. E-reader permite sem limite fisico."),
                new Especificacao("TTS", "Sim (text-to-speech integrado)", true, "Dislexico que cansa de ler pode OUVIR. Cego pode ouvir o livro todo."),
                new Especificacao("Contraste", "Ajustavel (escuro sobre claro, claro sobre escuro)", true, "Modo escuro (fundo preto, texto branco) para baixa visao e sensibilidade a luz."),
                new Especificacao("Suporte a formatos", "EPUB, PDF, TXT, HTML", true, "Nao pode prender o usuario num formato proprietario."),
                new Especificacao("Bateria", "Minimo 4 semanas", true, "E-ink consome quase nada. Meses de uso sem recarregar.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Amazon", "Kindle Paperwhite", CategoriaDispositivo.E_READER, 600, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("E-ink 300ppi", "Fonte ajustavel + OpenDyslexic", "TTS (VoiceView)", "Contraste ajustavel", "Bateria semanas", "Iluminacao frontal (nao irrita)"),
                    Arrays.asList("Formato proprietario (AZW3)", "Suporte a EPUB limitado"), ""),
                new ProdutoSuportado("Kobo", "Clara 2E", CategoriaDispositivo.E_READER, 700, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.TDAH),
                    Arrays.asList("E-ink 300ppi", "Suporte nativo a EPUB", "OpenDyslexic nativo", "OverDrive (biblioteca publica)"),
                    Arrays.asList("TTS limitado"), ""),
                new ProdutoSuportado("Kobo", "Libra H2O", CategoriaDispositivo.E_READER, 1000, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("Tela 7 polegadas", "Botoes fisicos (virar pagina)", "EPUB nativo", "Resistente a agua"),
                    Arrays.asList("Custo medio-alto"), ""),
                new ProdutoSuportado("Onyx", "Boox Note Air", CategoriaDispositivo.E_READER, 2500, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA),
                    Arrays.asList("E-ink GRANDE (10.3 polegadas)", "Android (apps TTS, OpenDyslexic)", "Caneta (anotar)", "Todos formatos"),
                    Arrays.asList("Custo alto", "Mais pesado que Kindle"), "")
            ),
            300.0,
            "E-reader e para QUEM LER Dói. Dislexico que desiste de livro impresso LE no e-reader (fonte OpenDyslexic, espacamento ajustado). Baixa visao que nao ve letra pequena AMPLIA sem limite. TDAH que se distrai com tela colorida FOCa no e-ink monocromatico."
        ));

        // === 12. GPS TRACKER ===
        specs.add(new SpecDispositivo(
            CategoriaDispositivo.GPS_TRACKER,
            "GPS tracker pessoal para criancas (perdida/abduzida), idosos (demencia/fuga), e pessoas com deficiencia cognitiva. Nao e smartphone -- e um RASTREADOR dedicado, simples, longa bateria.",
            Arrays.asList(DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO, DeficienciaAlvo.COGNITIVA),
            Arrays.asList(
                new Especificacao("GPS", "Sim (com A-GPS)", true, "Localizacao precisa (< 10m em externo)."),
                new Especificacao("Bateria", "Minimo 5 dias (ideal 15+)", true, "Crianca/idoso NAO vai lembrar de recarregar todo dia. Bateria longa e CRITICA."),
                new Especificacao("Botao SOS", "Sim (1 toque = alerta)", true, "Crianca aperta = pais recebem localizacao + alerta. Idoso aperta = socorro."),
                new Especificacao("Cerca virtual", "Sim (geofencing)", true, "Pais definem area segura. Crianca sai = alerta automatico."),
                new Especificacao("Resistencia", "IPX7+ (agua e impacto)", true, "Crianca derruba, molha, perde. Tracker precisa sobreviver."),
                new Especificacao("Conectividade", "4G LTE (chip SIM integrado)", true, "Nao depende de WiFi. Funciona em qualquer lugar com sinal celular."),
                new Especificacao("Tamanho", "Pequeno e discreto (< 50g)", true, "Crianca nao quer usar algo grande/visivel. Discreto = uso continuo."),
                new Especificacao("Audio bidirecional", "Sim (microfone + alto-falante)", false, "Pais podem FALAR com a crianca pelo tracker. Crianca pode chamar.")
            ),
            Arrays.asList(
                new ProdutoSuportado("Apple", "AirTag", CategoriaDispositivo.GPS_TRACKER, 400, StatusSpec.PARCIAL,
                    Arrays.asList(DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO),
                    Arrays.asList("Custo baixo", "Bateria 1 ANO", "Rede Find My (milhoes de iPhones)", "Discreto (31g)"),
                    Arrays.asList("SEM GPS proprio (usa BLE + iPhones proximos)", "SEM botao SOS", "SEM audio bidirecional", "Nao funciona onde nao ha iPhone proximo"), ""),
                new ProdutoSuportado("Samsung", "Galaxy SmartTag2", CategoriaDispositivo.GPS_TRACKER, 200, StatusSpec.PARCIAL,
                    Arrays.asList(DeficienciaAlvo.CRIANCA),
                    Arrays.asList("Custo baixo", "Bateria 500 dias", "Rede SmartThings Find", "Botao (chama IFTTT)"),
                    Arrays.asList("Sem GPS proprio (BLE)", "Sem SOS direto", "Sem audio bidirecional"), ""),
                new ProdutoSuportado("Tuya", "Smart GPS Tracker (4G)", CategoriaDispositivo.GPS_TRACKER, 200, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO),
                    Arrays.asList("GPS REAL (com 4G)", "Botao SOS", "Audio bidirecional", "Cerca virtual", "Bateria 7-15 dias", "Custo baixo"),
                    Arrays.asList("Qualidade de build variavel", "App generico (menos polido)"), ""),
                new ProdutoSuportado("GlobalSat", "TR-600", CategoriaDispositivo.GPS_TRACKER, 600, StatusSpec.CONFORME,
                    Arrays.asList(DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO),
                    Arrays.asList("GPS + 4G", "Bateria 15 dias", "SOS + audio", "Cerca virtual", "Industrial (resistente)"),
                    Arrays.asList("Grande (nao discreto para crianca)"), ""),
                new ProdutoSuportado("Angel Watch", "Angel Watch Co", CategoriaDispositivo.GPS_TRACKER, 1200, StatusSpec.RECOMENDADO,
                    Arrays.asList(DeficienciaAlvo.CRIANCA),
                    Arrays.asList("RELOGIO GPS para crianca", "GPS + 4G + WiFi", "Chamada de voz (2 vias)", "SOS", "Cerca virtual", "Videochamada"),
                    Arrays.asList("Bateria 2-3 dias (smartwatch = curta)", "Custo medio"), "")
            ),
            200.0,
            "GPS tracker e para QUEM NAO PODE PEDIR AJUDA. Crianca de 5 anos perdida no shopping nao liga para os pais. Idoso com Alzheimer nao lembra o proprio nome. Tracker = os pais ENCONTRAM sem depender do perdido. O Telefonista usa GPS do smartphone -- mas tracker dedicado e BACKUP."
        ));

        return specs;
    }

    // ========================================================================
    // 4. ENGINE
    // ========================================================================

    public static class AccessibilityHardwareSpecEngine {
        public final List<SpecDispositivo> specs;

        public AccessibilityHardwareSpecEngine() {
            this.specs = initSpecs();
        }

        public List<CategoriaDispositivo> listarCategorias() {
            return specs.stream().map(s -> s.categoria).collect(Collectors.toList());
        }

        public SpecDispositivo specPorCategoria(CategoriaDispositivo cat) {
            return specs.stream().filter(s -> s.categoria == cat).findFirst().orElse(null);
        }

        public List<ProdutoSuportado> produtosPorCategoria(CategoriaDispositivo cat) {
            SpecDispositivo s = specPorCategoria(cat);
            return s != null ? s.produtos : new ArrayList<>();
        }

        public List<Map.Entry<ProdutoSuportado, SpecDispositivo>> produtosPorDeficiencia(DeficienciaAlvo defic) {
            List<Map.Entry<ProdutoSuportado, SpecDispositivo>> resultado = new ArrayList<>();
            for (SpecDispositivo s : specs) {
                for (ProdutoSuportado p : s.produtos) {
                    if (p.deficienciasAtendidas.contains(defic)) {
                        resultado.add(new AbstractMap.SimpleEntry<>(p, s));
                    }
                }
            }
            return resultado;
        }

        public List<ProdutoSuportado> produtosPorStatus(StatusSpec status) {
            List<ProdutoSuportado> resultado = new ArrayList<>();
            for (SpecDispositivo s : specs) {
                for (ProdutoSuportado p : s.produtos) {
                    if (p.status == status) resultado.add(p);
                }
            }
            return resultado;
        }

        public List<ProdutoSuportado> produtosRecomendados() {
            return produtosPorStatus(StatusSpec.RECOMENDADO);
        }

        public StatusSpec verificarProduto(CategoriaDispositivo cat, String marca, String modelo, Map<String, Boolean> specsAtendidas) {
            SpecDispositivo s = specPorCategoria(cat);
            if (s == null) return StatusSpec.NAO_CONFORME;
            List<Especificacao> obrigatorios = s.specs.stream().filter(sp -> sp.obrigatorio).collect(Collectors.toList());
            boolean todosAtendidos = obrigatorios.stream().allMatch(sp -> specsAtendidas.getOrDefault(sp.parametro, false));
            if (todosAtendidos) {
                List<Especificacao> opcionais = s.specs.stream().filter(sp -> !sp.obrigatorio).collect(Collectors.toList());
                long opcAtendidos = opcionais.stream().filter(sp -> specsAtendidas.getOrDefault(sp.parametro, false)).count();
                if (opcAtendidos == opcionais.size() && !opcionais.isEmpty()) return StatusSpec.RECOMENDADO;
                return StatusSpec.CONFORME;
            }
            long falhas = obrigatorios.stream().filter(sp -> !specsAtendidas.getOrDefault(sp.parametro, false)).count();
            if (falhas <= 2) return StatusSpec.PARCIAL;
            return StatusSpec.NAO_CONFORME;
        }

        public Map<String, List<ProdutoSuportado>> catalogoPorFaixaCusto() {
            Map<String, List<ProdutoSuportado>> resultado = new LinkedHashMap<>();
            for (NivelCusto n : NivelCusto.values()) resultado.put(n.getRotulo(), new ArrayList<>());
            for (SpecDispositivo s : specs) {
                for (ProdutoSuportado p : s.produtos) {
                    NivelCusto nivel = classificarCusto(p.precoAproxBrl);
                    resultado.get(nivel.getRotulo()).add(p);
                }
            }
            return resultado;
        }

        private NivelCusto classificarCusto(double preco) {
            for (NivelCusto n : NivelCusto.values()) {
                if (n.getMinReal() <= preco && preco <= n.getMaxReal()) return n;
            }
            return NivelCusto.ESPECIALIZADO;
        }

        public Map<String, Object> scorecard() {
            int totalProdutos = specs.stream().mapToInt(s -> s.produtos.size()).sum();
            int recomendados = produtosRecomendados().size();
            int conformes = produtosPorStatus(StatusSpec.CONFORME).size();
            int parciais = produtosPorStatus(StatusSpec.PARCIAL).size();
            int naoConformes = produtosPorStatus(StatusSpec.NAO_CONFORME).size();
            int totalSpecs = specs.stream().mapToInt(s -> s.specs.size()).sum();
            int totalObrigatorias = specs.stream().mapToInt(s -> (int) s.specs.stream().filter(sp -> sp.obrigatorio).count()).sum();
            Map<String, Object> sc = new LinkedHashMap<>();
            sc.put("categorias_dispositivos", specs.size());
            sc.put("produtos_catalogados", totalProdutos);
            sc.put("produtos_recomendados", recomendados);
            sc.put("produtos_conformes", conformes);
            sc.put("produtos_parciais", parciais);
            sc.put("produtos_nao_conformes", naoConformes);
            sc.put("specs_totais", totalSpecs);
            sc.put("specs_obrigatorias", totalObrigatorias);
            sc.put("deficiencias_cobertas", DeficienciaAlvo.values().length);
            return sc;
        }
    }

    // ========================================================================
    // 5. DEMO (main)
    // ========================================================================

    public static void main(String[] args) {
        AccessibilityHardwareSpecEngine e = new AccessibilityHardwareSpecEngine();

        System.out.println("=".repeat(70));
        System.out.println("OpenAccessibilityHardwareSpecs -- Hardware COTS para Acessibilidade");
        System.out.println("=".repeat(70));

        System.out.println("\n[" + e.specs.size() + " DISPOSITIVOS COTS ESPECIFICADOS]");
        for (SpecDispositivo s : e.specs) {
            String defs = s.deficienciasAtendidas.stream().limit(3).map(DeficienciaAlvo::getRotulo).collect(Collectors.joining(", "));
            System.out.printf("  %s Custo min: R$ %.0f%n", String.format("%-35s", s.categoria.getRotulo() + "."), s.custoMinimoBrl);
            System.out.printf("  %35s Atende: %s...%n", "", defs);
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[DETALHE] HEADPHONE BLUETOOTH -- Especificacoes");
        System.out.println("=".repeat(70));
        SpecDispositivo hp = e.specPorCategoria(CategoriaDispositivo.HEADPHONE_BT);
        if (hp != null) {
            System.out.println("\n  Descricao: " + hp.descricao);
            System.out.println("\n  ESPECIFICACOES MINIMAS (" + hp.specs.size() + " specs):");
            for (Especificacao spec : hp.specs) {
                String flag = spec.obrigatorio ? "OBRIG" : "opc";
                System.out.println("    [" + flag + "] " + spec.parametro + ": " + spec.valorMinimo);
                System.out.println("          -> " + spec.justificativa);
            }
            System.out.println("\n  PRODUTOS SUPORTADOS (" + hp.produtos.size() + "):");
            for (ProdutoSuportado p : hp.produtos) {
                System.out.println("\n    [" + p.status.getRotulo() + "] " + p.marca + " " + p.modelo + " -- R$ " + (int) p.precoAproxBrl);
                System.out.println("      Fortes: " + String.join(", ", p.pontosFortes.subList(0, Math.min(3, p.pontosFortes.size()))));
                System.out.println("      Fracos: " + String.join(", ", p.pontosFracos.subList(0, Math.min(3, p.pontosFracos.size()))));
            }
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[CATALOGO COMPLETO -- Todos os dispositivos e produtos]");
        System.out.println("=".repeat(70));
        for (SpecDispositivo s : e.specs) {
            System.out.println("\n  --- " + s.categoria.getRotulo() + " ---");
            for (ProdutoSuportado p : s.produtos) {
                String flag = Map.of("conforme", "OK", "parcial", "PARC", "nao_conforme", "NAO", "recomendado", "REC").get(p.status.getId());
                System.out.printf("    [%s] %s %s R$ %6.0f%n", flag, p.marca, String.format("%-30s", p.modelo), p.precoAproxBrl);
            }
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[PRODUTOS POR DEFICIENCIA]");
        System.out.println("=".repeat(70));
        for (DeficienciaAlvo defic : DeficienciaAlvo.values()) {
            List<Map.Entry<ProdutoSuportado, SpecDispositivo>> prods = e.produtosPorDeficiencia(defic);
            if (!prods.isEmpty()) {
                List<String> nomes = prods.stream().limit(4).map(entry -> entry.getKey().marca + " " + entry.getKey().modelo).collect(Collectors.toList());
                System.out.println("\n  " + defic.getRotulo() + " (" + prods.size() + " produtos):");
                for (String n : nomes) System.out.println("    - " + n);
            }
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[CATALOGO POR FAIXA DE CUSTO]");
        System.out.println("=".repeat(70));
        Map<String, List<ProdutoSuportado>> cat = e.catalogoPorFaixaCusto();
        for (Map.Entry<String, List<ProdutoSuportado>> entry : cat.entrySet()) {
            if (!entry.getValue().isEmpty()) {
                System.out.println("\n  " + entry.getKey() + " (" + entry.getValue().size() + " produtos):");
                for (ProdutoSuportado p : entry.getValue().subList(0, Math.min(3, entry.getValue().size()))) {
                    System.out.println("    - " + p.marca + " " + p.modelo + " (R$ " + (int) p.precoAproxBrl + ")");
                }
            }
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[SCORECARD]");
        System.out.println("=".repeat(70));
        Map<String, Object> sc = e.scorecard();
        for (Map.Entry<String, Object> entry : sc.entrySet()) {
            System.out.printf("  %s %s%n", String.format("%-30s", entry.getKey() + "."), entry.getValue());
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("FILOSOFIA -- Dispositivos que nao precisam ser feitos do zero");
        System.out.println("=".repeat(70));
        System.out.println("""
O COMPUTADOR RISC-V e fabricado do zero (OpenSovereignTech).
Mas headphones, smartwatches, eye-trackers, braille displays -- esses
SAO fabricados pela industria. A Republica NAO precisa reinventar todos.

O que a Republica faz: define ESPECIFICACOES MINIMAS de acessibilidade.
Quem fabricar, segue a spec. Quem comprar, sabe o que esperar.
'A especificacao nao pode ser alterada por um vendor.'

POR QUE ESPECIFICAR (e nao fabricar):
  Fabricar do zero e CARO e LENTO. O cidadao precisa de acessibilidade
  HOJE, nao em 10 anos quando a fabrica da Republica estiver pronta.
  COTS (Commercial Off-The-Shelf) permite usar o que JA EXISTE.
  A spec garante que o que existe ATENDE o cidadao.

A SPEC E IMUTAVEL:
  O vendor nao pode 'adicionar features' que quebram acessibilidade.
  O vendor nao pode 'remover' o jack 3.5mm porque 'e antigo'.
  O vendor nao pode trocar botao fisico por touch porque 'e mais bonito'.
  A spec e DA REPUBLICA. O vendor IMPLEMENTA. Nao inventa.

A LISTA DE EQUIPAMENTOS SUPORTADOS:
  Nao e 'recomendacao de marca'. E CONFORMIDADE TECNICA.
  Produto na lista = atende spec minima. Produto fora da lista = NAO comprar.
  A Republica NAO ganha comissao. NAO tem 'parceiro preferido'.
  Tem CRITERIO TECNICO. Objetivo. Auditavel.

O PRINCIPIO:
  Todo cidadao tem direito ao hardware que permite acessar o mundo.
  Cego precisa de leitor de tela + headphone. Surdo precisa de Libras + webcam.
  Tetraplegico precisa de eye tracker + switch. Dislexico precisa de e-reader.
  A Republica garante NAO o hardware (isso e COTS), mas a SPEC que faz
  o hardware SER acessivel. Sem spec, o mercado fabrica o que quer.
  Com spec, o mercado fabrica o que PRECISA.
""");
    }
}