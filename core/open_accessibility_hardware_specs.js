// OpenAccessibilityHardwareSpecs.js
// Transpilacao fiel do Python para JavaScript (ES6)
// Especificacoes de Hardware COTS para Acessibilidade
// Todos os comentarios e strings em Portugues (conforme fonte)

const CategoriaDispositivo = {
    HEADPHONE_BT: { id: "headphone_bt", rotulo: "Headphone Bluetooth" },
    SMARTPHONE: { id: "smartphone", rotulo: "Smartphone" },
    SMARTWATCH: { id: "smartwatch", rotulo: "Smartwatch" },
    EYE_TRACKER: { id: "eye_tracker", rotulo: "Eye Tracker" },
    BRAILLE_DISPLAY: { id: "braille_display", rotulo: "Display Braille" },
    SWITCH: { id: "switch", rotulo: "Switch Button (botao de acesso)" },
    BONE_CONDUCTION: { id: "bone_conduction", rotulo: "Fone de Conducao Ossea" },
    MICROFONE: { id: "microfone", rotulo: "Microfone" },
    WEBCAM: { id: "webcam", rotulo: "Webcam" },
    TABLET: { id: "tablet", rotulo: "Tablet (CAA)" },
    E_READER: { id: "e_reader", rotulo: "E-reader (Leitor Digital)" },
    GPS_TRACKER: { id: "gps_tracker", rotulo: "GPS Tracker (Pessoal)" }
};

const DeficienciaAlvo = {
    CEGUEIRA: { id: "cegueira", rotulo: "Cego / Baixa visao" },
    SURDEZ: { id: "surdez", rotulo: "Surdo / Deficiente auditivo" },
    MOTORA: { id: "motora", rotulo: "Motora / Tetraplegia / Paralisia cerebral" },
    COGNITIVA: { id: "cognitiva", rotulo: "Cognitiva / Sindrome de Down" },
    AUTISMO: { id: "autismo", rotulo: "TEA / Autismo" },
    TDAH: { id: "tdah", rotulo: "TDAH / Dislexia" },
    COMUNICACAO: { id: "comunicacao", rotulo: "Comunicacao (nao-verbal / afasia)" },
    NEUROLOGICA: { id: "neurologica", rotulo: "Neurologica (ELA / Parkinson / Epilepsia)" },
    IDOSO: { id: "idoso", rotulo: "Idoso (demencia / mobilidade reduzida)" },
    CRIANCA: { id: "crianca", rotulo: "Crianca (seguranca / rastreamento)" },
    UNIVERSAL: { id: "universal", rotulo: "Uso universal (todas as deficiencias)" }
};

const NivelCusto = {
    GRATUITO: { id: "gratuito", rotulo: "Gratuito (doacao / biblioteca)", minReal: 0, maxReal: 0 },
    BAIXO: { id: "baixo", rotulo: "Baixo custo (< R$ 100)", minReal: 1, maxReal: 100 },
    MEDIO: { id: "medio", rotulo: "Custo medio (R$ 100-500)", minReal: 101, maxReal: 500 },
    ALTO: { id: "alto", rotulo: "Custo alto (R$ 500-2000)", minReal: 501, maxReal: 2000 },
    PREMIUM: { id: "premium", rotulo: "Premium (R$ 2000-10000)", minReal: 2001, maxReal: 10000 },
    ESPECIALIZADO: { id: "especializado", rotulo: "Especializado (> R$ 10000)", minReal: 10001, maxReal: 999999 }
};

const StatusSpec = {
    CONFORME: { id: "conforme", rotulo: "Conforme: atende todas as specs minimas" },
    PARCIAL: { id: "parcial", rotulo: "Parcial: atende a maioria, mas tem lacunas" },
    NAO_CONFORME: { id: "nao_conforme", rotulo: "Nao conforme: nao atende specs minimas" },
    RECOMENDADO: { id: "recomendado", rotulo: "Recomendado: excede as specs minimas" }
};

class Especificacao {
    constructor(parametro, valorMinimo, obrigatorio = true, justificativa = "") {
        this.parametro = parametro;
        this.valorMinimo = valorMinimo;
        this.obrigatorio = obrigatorio;
        this.justificativa = justificativa;
    }
}

class ProdutoSuportado {
    constructor(marca, modelo, categoria, precoAproxBrl, status,
                deficienciasAtendidas = [], pontosFortes = [], pontosFracos = [], notes = "") {
        this.marca = marca;
        this.modelo = modelo;
        this.categoria = categoria;
        this.precoAproxBrl = precoAproxBrl;
        this.status = status;
        this.deficienciasAtendidas = deficienciasAtendidas;
        this.pontosFortes = pontosFortes;
        this.pontosFracos = pontosFracos;
        this.notes = notes;
    }
}

class SpecDispositivo {
    constructor(categoria, descricao, deficienciasAtendidas,
                specs = [], produtos = [], custoMinimoBrl = 0.0, observacao = "") {
        this.categoria = categoria;
        this.descricao = descricao;
        this.deficienciasAtendidas = deficienciasAtendidas;
        this.specs = specs;
        this.produtos = produtos;
        this.custoMinimoBrl = custoMinimoBrl;
        this.observacao = observacao;
    }
}

function initSpecs() {
    const specs = [];

    // === 1. HEADPHONE BLUETOOTH ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.HEADPHONE_BT,
        "Headphone Bluetooth para acessibilidade auditiva. Usado para TTS (text-to-speech), audio descricao, legendas em audio, amplificacao para deficiente auditivo, e comunicacao com o Telefonista.",
        [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.UNIVERSAL, DeficienciaAlvo.IDOSO],
        [
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
        ],
        [
            new ProdutoSuportado("JBL", "Tune 510BT", CategoriaDispositivo.HEADPHONE_BT, 250, StatusSpec.CONFORME,
                [DeficienciaAlvo.UNIVERSAL], ["Bateria 40h", "Multiponto", "Custo acessivel", "Jack 3.5mm"], ["Sem anuncio de bateria por voz", "Controle touch (parcial)"]),
            new ProdutoSuportado("Sony", "WH-CH520", CategoriaDispositivo.HEADPHONE_BT, 350, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.UNIVERSAL, DeficienciaAlvo.SURDEZ], ["Bateria 50h", "Multiponto", "Anuncio de bateria por voz", "Controles fisicos"], ["Sem jack 3.5mm (USB-C apenas)"]),
            new ProdutoSuportado("Sennheiser", "HD 350BT", CategoriaDispositivo.HEADPHONE_BT, 500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.UNIVERSAL], ["Bateria 30h", "AAC + aptX", "Confortavel 8h+", "USB-C charge"], ["Sem jack 3.5mm"]),
            new ProdutoSuportado("Anker", "Soundcore Life Q20", CategoriaDispositivo.HEADPHONE_BT, 250, StatusSpec.CONFORME,
                [DeficienciaAlvo.UNIVERSAL], ["Bateria 40h", "ANC basico", "Custo baixo"], ["Multiponto instavel", "App requer visual"]),
            new ProdutoSuportado("Philips", "SHL3070BK", CategoriaDispositivo.HEADPHONE_BT, 150, StatusSpec.PARCIAL,
                [DeficienciaAlvo.UNIVERSAL], ["Custo muito baixo", "Jack 3.5mm"], ["Bateria 9h (minimo)", "Sem multiponto", "Latencia alta para TTS"]),
            new ProdutoSuportado("Apple", "AirPods (2nd gen)", CategoriaDispositivo.HEADPHONE_BT, 1500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL], ["Acessibilidade iOS nativa", "Live Listen (microfone remoto)", "Audio descricao integrada", "Detecao de sons (Porta, Cachorro, Sirene)"], ["Custo alto", "Sem controles fisicos (touch)", "Bateria ~5h por carga (24h com case)"]),
            new ProdutoSuportado("Apple", "AirPods Pro 2", CategoriaDispositivo.HEADPHONE_BT, 2500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL], ["Live Listen", "ANC adaptativo", "Modo Conversacao (transparencia)", "Detecao de sons ambiente"], ["Custo premium", "Sem jack 3.5mm"]),
            new ProdutoSuportado("Samsung", "Galaxy Buds FE", CategoriaDispositivo.HEADPHONE_BT, 600, StatusSpec.CONFORME,
                [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL], ["Live Listen no Android", "ANC", "Custo medio"], ["Bateria ~6h por carga", "Sem jack"])
        ],
        80.0,
        "O Headphone Bluetooth e o DISPOSITIVO MAIS UNIVERSAL da acessibilidade. Cego usa para TTS. Surdo usa para amplificacao e Live Listen. Tetraplegico usa para comando de voz. Idoso usa para amplificacao. A spec minima garante que QUALQUER headphone recomendado funciona para TODOS."
    ));

    // === 2. SMARTPHONE ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.SMARTPHONE,
        "Smartphone como CORPO ESTENDIDO (Telefonista). Camera=olhos, microfone=ouvidos, GPS=direcao, acelerometro=balance, smartwatch=biometria.",
        [DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.SURDEZ, DeficienciaAlvo.MOTORA, DeficienciaAlvo.AUTISMO, DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.IDOSO, DeficienciaAlvo.CRIANCA, DeficienciaAlvo.UNIVERSAL],
        [
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
        ],
        [
            new ProdutoSuportado("Samsung", "Galaxy A15 5G", CategoriaDispositivo.SMARTPHONE, 1000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.UNIVERSAL], ["Custo baixo", "Android 14", "Bateria 5000mAh", "TalkBack nativo", "Camera 50MP", "Slot microSD"], ["RAM 4GB (minimo)", "Sem OIS na camera"]),
            new ProdutoSuportado("Samsung", "Galaxy A55 5G", CategoriaDispositivo.SMARTPHONE, 2000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.UNIVERSAL], ["RAM 8GB", "Camera com OIS", "Bateria 5000mAh", "Bixby Vision (descricao de cena)", "Modo Live Listen"], ["Sem slot microSD (alguns mercados)"]),
            new ProdutoSuportado("Motorola", "Moto G84 5G", CategoriaDispositivo.SMARTPHONE, 1300, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.UNIVERSAL], ["RAM 8GB (otimo nesta faixa)", "Bateria 5000mAh", "Android limpo (TalkBack funciona bem)", "Slot microSD"], ["Camera sem OIS"]),
            new ProdutoSuportado("Apple", "iPhone SE (2022)", CategoriaDispositivo.SMARTPHONE, 3000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL], ["VoiceOver (melhor leitor de tela do mercado)", "Detecao de pessoas, portas, sons (Magnifier)", "Audio descricao", "Live Listen", "5 anos de update"], ["Bateria 2018mAh (fraca)", "Tela 4.7 polegadas (pequena)"]),
            new ProdutoSuportado("Apple", "iPhone 15", CategoriaDispositivo.SMARTPHONE, 5000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.UNIVERSAL], ["VoiceOver + Magnifier + Detecao de sons", "LiDAR (navegacao para cego)", "Camera 48MP", "USB-C", "Live Listen"], ["Custo premium"]),
            new ProdutoSuportado("Xiaomi", "Redmi Note 13", CategoriaDispositivo.SMARTPHONE, 1100, StatusSpec.CONFORME,
                [DeficienciaAlvo.UNIVERSAL], ["Custo baixo", "Bateria 5000mAh", "Camera 108MP", "Slot microSD"], ["MIUI tem bugs de acessibilidade", "TalkBack menos testado"])
        ],
        800.0,
        "O smartphone e o CORACAO da acessibilidade da Republica. E camera, microfone, GPS, acelerometro, TTS, leitor de tela -- tudo num so dispositivo. A spec garante que QUALQUER smartphone recomendado roda a stack do Telefonista."
    ));

    // === 3. SMARTWATCH ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.SMARTWATCH,
        "Smartwatch para biometria continua: estresse (frequencia cardiaca), predicao de convulsao (temperatura + HR), deteccao de queda (idoso), lembretes (TDAH, idoso com demencia).",
        [DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.IDOSO, DeficienciaAlvo.TDAH, DeficienciaAlvo.AUTISMO, DeficienciaAlvo.MOTORA],
        [
            new Especificacao("Sensor cardiaco", "Sim (PPG ou ECG)", true, "Deteccao de estresse, arritmia, taquicardia."),
            new Especificacao("Acelerometro", "Sim (3 eixos)", true, "Deteccao de queda (idoso), tremor (Parkinson)."),
            new Especificacao("GPS", "Sim (integrado)", true, "Rastreamento de crianca/idoso sem depender do smartphone."),
            new Especificacao("Bateria", "Minimo 3 dias (ideal 7+)", true, "Biometria continua requer uso 24h. Recarga diaria e falha."),
            new Especificacao("Resistencia", "IP68 (agua e poeira)", true, "Usa no banho, na chuva, na piscina. Biometria nao para."),
            new Especificacao("Vibracao", "Motor haptico forte", true, "Surdo nao ouve alerta. Cego nao ve. Vibration e universal."),
            new Especificacao("Tela sempre ligada", "Desejavel", false, "Idoso precisa ver as horas sem tocar na tela."),
            new Especificacao("Temperatura corporea", "Desejavel", false, "Predicao de convulsao epileptica (pesquisa Apple Watch)."),
            new Especificacao("SpO2 (oximetria)", "Desejavel", false, "Monitoramento respiratorio.")
        ],
        [
            new ProdutoSuportado("Amazfit", "Bip 5", CategoriaDispositivo.SMARTWATCH, 500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.IDOSO, DeficienciaAlvo.TDAH], ["Bateria 10 DIAS", "GPS", "Tela grande (1.69 polegadas)", "Custo baixo", "Vibracao forte"], ["Sem ECG", "Sem SpO2 confiavel"]),
            new ProdutoSuportado("Xiaomi", "Smart Band 8", CategoriaDispositivo.SMARTWATCH, 250, StatusSpec.CONFORME,
                [DeficienciaAlvo.IDOSO, DeficienciaAlvo.TDAH], ["Bateria 16 DIAS", "Custo muito baixo", "HR + SpO2", "Leve (27g)"], ["Sem GPS integrado (depende do telefone)", "Tela pequena para idoso com baixa visao"]),
            new ProdutoSuportado("Apple", "Apple Watch SE (2nd gen)", CategoriaDispositivo.SMARTWATCH, 2500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.IDOSO], ["Deteccao de queda (SOS automatico)", "ECG (aprovado FDA)", "GPS integrado", "Vibracao excelente", "Tela sempre ligada"], ["Bateria ~18h (1 dia)", "Custo alto"]),
            new ProdutoSuportado("Apple", "Apple Watch Series 9", CategoriaDispositivo.SMARTWATCH, 4500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.NEUROLOGICA], ["ECG + SpO2 + Temperatura", "Deteccao de queda + SOS", "GPS", "Health Records (compartilha com medico)"], ["Bateria ~18h", "Custo premium"]),
            new ProdutoSuportado("Samsung", "Galaxy Watch FE", CategoriaDispositivo.SMARTWATCH, 1000, StatusSpec.CONFORME,
                [DeficienciaAlvo.IDOSO], ["ECG (em alguns paises)", "Bateria 2-3 dias", "Deteccao de queda", "Android nativo"], ["ECG bloqueado em alguns mercados"]),
            new ProdutoSuportado("Garmin", "Forerunner 55", CategoriaDispositivo.SMARTWATCH, 1500, StatusSpec.CONFORME,
                [DeficienciaAlvo.IDOSO], ["Bateria 14 DIAS em modo watch", "GPS de precisao", "Vibracao forte"], ["Foco em esporte (menos features de saude)"])
        ],
        400.0,
        "Smartwatch = biometria PASSIVA. O usuario nao precisa fazer nada. O relogio detecta queda e chama socorro. Detecta arritmia e avisa. E o sensor do corpo que o corpo nao tem (ou perdeu)."
    ));

    // === 4. EYE TRACKER ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.EYE_TRACKER,
        "Eye tracker para tetraplegia, ELA, paralisia cerebral. O olho e o ultimo musculo voluntario em ELA. Eye tracker permite digitar, clicar, comunicar -- SO COM OS OLHOS.",
        [DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.COMUNICACAO],
        [
            new Especificacao("Precisao", "< 1 grau visual (ideal < 0.5)", true, "Para clicar em botoes pequenos na tela. Precisao baixa = frustracao."),
            new Especificacao("Frequencia", "Minimo 60Hz (ideal 120Hz+)", true, "Taxa de atualizacao. Baixa = lag entre olhar e clique."),
            new Especificacao("Calibracao", "Automatica ou 1-5 pontos", true, "Calibracao complexa (16 pontos) e exaustiva para quem tem mobilidade limitada."),
            new Especificacao("Compatibilidade", "Windows + macOS + Linux", true, "Nao pode prender o usuario num SO."),
            new Especificacao("Software inclusivo", "Teclado virtual + CAA", true, "Eye tracker sem software de comunicacao e so hardware inutil."),
            new Especificacao("Latencia", "< 50ms", true, "Entre o olhar e o cursor responder. Alto = nauseas."),
            new Especificacao("Trabalha com oculos", "Sim", true, "Muitos usuarios de eye tracker usam oculos."),
            new Especificacao("Headbox", "Minimo 25x25cm", true, "Area de liberdade de movimento da cabeca. Pequeno = usuario precisa ficar imovel.")
        ],
        [
            new ProdutoSuportado("Tobii", "Eye Tracker 5", CategoriaDispositivo.EYE_TRACKER, 3500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA], ["Precisao < 0.5 grau", "144Hz", "Headbox amplo", "Software Tobii Communicator (CAA)", "Trabalha com oculos"], ["Custo alto", "Windows-centric (Linux parcial)"]),
            new ProdutoSuportado("Tobii", "Dynavox", CategoriaDispositivo.EYE_TRACKER, 15000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.COMUNICACAO], ["Solucao completa (tablet + eye tracker + CAA)", "Snap Core First (CAA)", "Suporte clinico"], ["Custo ESPECIALIZADO", "Fornecedor unico"]),
            new ProdutoSuportado("IRISBOND", "Hiru", CategoriaDispositivo.EYE_TRACKER, 5000, StatusSpec.CONFORME,
                [DeficienciaAlvo.MOTORA], ["Precisao < 0.5 grau", "Multiplataforma", "Usado em hospitais brasileiros"], ["Disponibilidade limitada no Brasil"]),
            new ProdutoSuportado("Windows", "Eye Control (nativo)", CategoriaDispositivo.EYE_TRACKER, 0, StatusSpec.CONFORME,
                [DeficienciaAlvo.MOTORA], ["GRATUITO no Windows 10/11", "Funciona com Tobii 4C e EyeX"], ["So funciona com hardware Tobii", "Limitado a Windows"]),
            new ProdutoSuportado("Apple", "iPad com AssistiveTouch (olhos)", CategoriaDispositivo.EYE_TRACKER, 5000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.MOTORA], ["Eye Tracking nativo no iPadOS (2024+)", "GRATUITO (incluido no iPad)", "CAA integrada"], ["So funciona em iPad Pro/Air recentes", "Precisao pode variar"])
        ],
        2000.0,
        "Eye tracker e o DISPOSITIVO QUE DEVOLVE A VOZ. Pessoa com ELA perde tudo -- bracos, pernas, voz. Sobra o olhar. Eye tracker transforma olhar em palavras."
    ));

    // === 5. BRAILLE DISPLAY ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.BRAILLE_DISPLAY,
        "Display Braille para cegos. Converte texto digital em celas braille táteis. E o OUTPUT equivalente ao leitor de tela -- mas para quem prefere ou precisa ler pelo tato (surdos-cegos nao tem audio).",
        [DeficienciaAlvo.CEGUEIRA],
        [
            new Especificacao("Celas", "Minimo 8 celas (ideal 40+)", true, "8 celas = palavra por vez. 40+ = linha inteira. Mais celas = leitura fluida."),
            new Especificacao("Tipo de cela", "Piezoeletrica (8 pinos por cela)", true, "Braille de 8 pontos (computador). 6 pontos so perde informacao de formatacao."),
            new Especificacao("Conexao", "Bluetooth + USB", true, "Bluetooth para smartphone. USB para computador. Ambos necessarios."),
            new Especificacao("Bateria", "Minimo 10h", true, "Dia de trabalho/estudo. Recarga no meio do dia e falha."),
            new Especificacao("Botoes de navegacao", "Sim (pan, rota, cursor routing)", true, "Navegar pelo texto sem depender do smartphone."),
            new Especificacao("Compatibilidade", "TalkBack (Android) + VoiceOver (iOS) + NVDA/JAWS (PC)", true, "Display Braille sem leitor de tela e so pinos. Precisa do SOFTWARE.")
        ],
        [
            new ProdutoSuportado("Orbit Research", "Orbit Reader 20 Plus", CategoriaDispositivo.BRAILLE_DISPLAY, 4000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.CEGUEIRA], ["20 celas (bom para custo)", "BLUETOOTH + USB", "Bateria 20h", "Custo mais baixo do mercado para Braille", "Nota: armazenamento interno (le sem smartphone)"], ["20 celas limita leitura longa", "Sem teclado Perkins integrado"]),
            new ProdutoSuportado("Help Tech", "Active Star 40", CategoriaDispositivo.BRAILLE_DISPLAY, 12000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.CEGUEIRA], ["40 celas (leitura fluida)", "Bluetooth + USB", "Teclado Perkins integrado", "Bateria 20h+", "Wi-Fi (le RSS, email)"], ["Custo ESPECIALIZADO"]),
            new ProdutoSuportado("Freedom Scientific", "Focus 40 Blue", CategoriaDispositivo.BRAILLE_DISPLAY, 10000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.CEGUEIRA], ["40 celas", "Bluetooth + USB", "Compativel com JAWS + NVDA + VoiceOver + TalkBack"], ["Custo ESPECIALIZADO"]),
            new ProdutoSuportado("Seika", "Seika 40", CategoriaDispositivo.BRAILLE_DISPLAY, 6000, StatusSpec.CONFORME,
                [DeficienciaAlvo.CEGUEIRA], ["40 celas", "Custo mais baixo para 40 celas", "Bluetooth + USB"], ["Qualidade de build inferior", "Suporte limitado no Brasil"]),
            new ProdutoSuportado("Apple", "iPhone/iPad com Braille (software)", CategoriaDispositivo.BRAILLE_DISPLAY, 0, StatusSpec.PARCIAL,
                [DeficienciaAlvo.CEGUEIRA], ["GRATUITO no iOS", "Mostra Braille na tela (para videntes aprenderem)", "Conecta com display fisico via Bluetooth"], ["Nao e Braille TATIL (so visual)", "Para cego real, precisa do display fisico"])
        ],
        3000.0,
        "Display Braille e o UNICO OUTPUT para SURDO-CEGO. Surdo-cego nao tem audio (surdo) nem tela (cego). Sobra o TATO. Display Braille e a janela para o mundo digital. O custo e alto (R$ 4000-15000) -- a Republica precisa subsidiar."
    ));

    // === 6. SWITCH BUTTON ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.SWITCH,
        "Switch button: botao grande de 1 toque para acesso. Para tetraplegia severa, paralisia cerebral, ELA avancada. 1 toque = 1 acao. O computador escaneia opcoes e o usuario toca o switch na opcao certa.",
        [DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.COMUNICACAO],
        [
            new Especificacao("Forca de ativacao", "Maximo 100g (ideal < 50g)", true, "Usuario com paralisia cerebral pode nao conseguir apertar botao duro."),
            new Especificacao("Tamanho da superficie", "Minimo 5cm diametro", true, "Alvo grande para quem tem tremor ou movimento involuntario."),
            new Especificacao("Feedback", "Tatil (click) + auditivo (click) + visual (LED)", true, "O usuario PRECISA saber que ativou. Multi-modal."),
            new Especificacao("Conexao", "Bluetooth e/ou Jack 3.5mm", true, "Jack 3.5mm = compatibilidade universal (AT, switch-adapted toys). BT = sem fio."),
            new Especificacao("Resistencia", "A prova de impacto e saliva", true, "Usuario pode ter espasmo. Crianca pode morder/bater."),
            new Especificacao("Montagem", "Compativel com braços articulados e suportes", true, "Switch precisa ser posicionado onde o usuario tem movimento."),
            new Especificacao("Bateria", "Minimo 100h (ideal: meses)", true, "Switch com fio nao precisa. Switch BT precisa durar semanas.")
        ],
        [
            new ProdutoSuportado("Ablenet", "Big Red Switch", CategoriaDispositivo.SWITCH, 400, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.MOTORA], ["Padrao da industria de AT", "Superficie 12.7cm", "Forca ~57g", "Jack 3.5mm", "Resistente"], ["Custo alto para um botao"]),
            new ProdutoSuportado("Ablenet", "Spec Switch", CategoriaDispositivo.SWITCH, 350, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.MOTORA], ["Superficie 5cm", "Forca muito baixa (~21g)", "Ideal para ELA avancada"], ["Custo alto"]),
            new ProdutoSuportado("Enabling Devices", "Jelly Bean Switch", CategoriaDispositivo.SWITCH, 300, StatusSpec.CONFORME,
                [DeficienciaAlvo.MOTORA], ["Superficie 6.5cm", "Cores vivas (baixa visao)", "Jack 3.5mm"], ["Feedback menos firme que Ablenet"]),
            new ProdutoSuportado("DIY", "Switch caseiro (pizza box + foil)", CategoriaDispositivo.SWITCH, 20, StatusSpec.PARCIAL,
                [DeficienciaAlvo.MOTORA], ["Custo MUITO baixo", "Customizavel", "Tutorial aberto (CC0)"], ["Durabilidade baixa", "Precisa manutencao frequente", "Sem feedback de qualidade"]),
            new ProdutoSuportado("Logitech", "Adaptive Gaming Kit", CategoriaDispositivo.SWITCH, 600, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.MOTORA], ["3 switches grandes + 5 pequenos", "Abas de etiqueta (identificacao tatil)", "Custo razoavel para kit completo"], ["Foco em gaming (adaptavel para AT)"])
        ],
        100.0,
        "Switch e o DISPOSITIVO MAIS SIMPLES E MAIS PODEROSO. 1 botao. 1 acao. Para quem so move 1 musculo (cabeca, braco, pe, sopro). Scanning: o computador mostra opcoes uma a uma. Switch na opcao certa = SELECAO. Comunicacao, controle, autonomia."
    ));

    // === 7. BONE CONDUCTION ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.BONE_CONDUCTION,
        "Fone de conducao ossea: som viaja pelo osso (cranio) ate o nervo auditivo, bypassando o ouvido externo e medio. Para surdo CONDUTIVO (problema no ouvido medio), estenose do canal, otite cronica. NAO funciona para surdo NEUROSSENSORIAL severo.",
        [DeficienciaAlvo.SURDEZ],
        [
            new Especificacao("Bluetooth", "5.0+", true, "Conexao estavel para TTS e audio descricao."),
            new Especificacao("Orelha aberta", "Sim (nao bloqueia canal auditivo)", true, "Cego que usa conducao ossea PRECISA ouvir o ambiente tambem."),
            new Especificacao("Bateria", "Minimo 6h", true, "Dia de uso continuo."),
            new Especificacao("Microfone", "Sim", true, "Para comando de voz e chamadas."),
            new Especificacao("Conforto", "Ajustavel, leve (< 40g)", true, "Repouso na teca (osso temporal). Pressao inadequada = dor."),
            new Especificacao("Resistencia", "IPX4+ (suor)", true, "Uso em atividade fisica e mobilidade urbana.")
        ],
        [
            new ProdutoSuportado("Shokz", "OpenRun Pro", CategoriaDispositivo.BONE_CONDUCTION, 1200, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.SURDEZ], ["Lider em conducao ossea", "Bateria 10h", "Bluetooth 5.1", "Microfone", "IP67"], ["Custo alto"]),
            new ProdutoSuportado("Shokz", "OpenMove", CategoriaDispositivo.BONE_CONDUCTION, 600, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.SURDEZ], ["Custo medio", "Bateria 6h", "Bluetooth 5.1", "IP55"], ["Qualidade de som inferior ao OpenRun Pro"]),
            new ProdutoSuportado("Mojawa", "Run Plus", CategoriaDispositivo.BONE_CONDUCTION, 1000, StatusSpec.CONFORME,
                [DeficienciaAlvo.SURDEZ], ["Bateria 8h", "IP68", "MP3 integrado (16GB)"], ["Marca menos estabelecida"])
        ],
        500.0,
        "Conducao ossea e PARA SURDO CONDUTIVO especificamente. Surdo neurosensorial severo NAO beneficia. Importante: cego que tambem e surdo condutivo pode usar conducao ossea e AINDA ouvir o ambiente (orelha aberta)."
    ));

    // === 8. MICROFONE ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.MICROFONE,
        "Microfone para comando de voz, fala-para-texto, e captura de audio ambiente para o Telefonista. Para tetraplegico que so fala. Para surdo que precisa de legenda em tempo real. Para cego que interage por voz.",
        [DeficienciaAlvo.MOTORA, DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.COMUNICACAO],
        [
            new Especificacao("Cancelamento de ruido", "Sim (DSP ou cardiode)", true, "Comando de voz em ambiente ruidoso precisa de CNR."),
            new Especificacao("Conexao", "USB ou Bluetooth", true, "USB = zero latencia. BT = mobilidade."),
            new Especificacao("Padrao polar", "Cardiode ou unidirecional", true, "Captura a voz do usuario, nao o ambiente inteiro."),
            new Especificacao("Frequencia", "100Hz-10kHz minimo", true, "Cobre voz humana. Baixa frequencia = graves (homem). Alta = agudos (mulher/crianca)."),
            new Especificacao("Mute fisico", "Botao de mute REAL (nao software)", true, "Privacidade: usuario PRECISA saber que o microfone esta mudo.")
        ],
        [
            new ProdutoSuportado("Blue", "Yeti Nano", CategoriaDispositivo.MICROFONE, 500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.MOTORA, DeficienciaAlvo.CEGUEIRA], ["USB-C", "Cardiode + omnidirecional", "Mute fisico (botao na frente)", "Qualidade excelente"], ["Grande (ocupa espaco na mesa)"]),
            new ProdutoSuportado("Fifine", "K669B", CategoriaDispositivo.MICROFONE, 150, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.MOTORA], ["Custo MUITO baixo", "USB", "Cardiode", "Tripé incluido"], ["Sem mute fisico", "Qualidade decente mas nao premium"]),
            new ProdutoSuportado("Jabra", "Speak 510", CategoriaDispositivo.MICROFONE, 700, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.MOTORA, DeficienciaAlvo.SURDEZ], ["Bluetooth + USB", "CNR excelente", "Speakerphone (para reuniao com legenda)", "Mute fisico"], ["Custo medio-alto"]),
            new ProdutoSuportado("In_build", "Microfone do smartphone", CategoriaDispositivo.MICROFONE, 0, StatusSpec.PARCIAL,
                [DeficienciaAlvo.UNIVERSAL], ["GRATUITO", "Sempre presente", "Portatil"], ["Qualidade varia", "CNR limitado", "Nao ideal para texto longo"])
        ],
        50.0,
        "Microfone e a ENTRADA para quem SO FALA. Tetraplegico que nao digita, FALA. Precisa de microfone bom. Surdo que precisa de legenda em tempo real, precisa capturar audio. Cego que navega por voz, precisa de microfone confiavel."
    ));

    // === 9. WEBCAM ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.WEBCAM,
        "Webcam para Libras (surdo se comunica por sinais na camera), visao computacional (descricao de cena para cego), e rastreamento de mao (linguagem de sinais como input).",
        [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA],
        [
            new Especificacao("Resolucao", "Minimo 720p (ideal 1080p)", true, "Libras requer resolucao suficiente para ver expressoes faciais e maos."),
            new Especificacao("Frequencia", "Minimo 30fps (ideal 60fps)", true, "Libras e RAPIDO. 15fps perde sinais. 60fps captura tudo."),
            new Especificacao("Autofocus", "Sim (rapido)", true, "Surdo que se move ao sinais nao pode ficar borrado."),
            new Especificacao("Campo de visao", "Minimo 70 graus (ideal 90+)", true, "Libras requer espaco para maos e bracos. Webcam estreita corta os sinais."),
            new Especificacao("Baixa luz", "Funciona em < 50 lux", true, "Nem todos tem iluminacao de estudio. Sala de casa a noite."),
            new Especificacao("Microfone integrado", "Desejavel (backup)", false, "Para videochamada com surdo (audio + Libras simultaneo).")
        ],
        [
            new ProdutoSuportado("Logitech", "C920 HD Pro", CategoriaDispositivo.WEBCAM, 400, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA], ["1080p 30fps", "Autofocus rapido", "Campo 78 graus", "Excelente baixa luz", "Microfone stereo"], ["Sem 60fps em 1080p"]),
            new ProdutoSuportado("Logitech", "C922 Pro", CategoriaDispositivo.WEBCAM, 500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.SURDEZ], ["1080p 30fps / 720p 60fps", "Fundo substituivel", "Tripé incluido"], ["Custo medio-alto"]),
            new ProdutoSuportado("Microsoft", "LifeCam Studio", CategoriaDispositivo.WEBCAM, 600, StatusSpec.CONFORME,
                [DeficienciaAlvo.SURDEZ], ["1080p", "Campo 75 graus", "Alta qualidade de build"], ["Descontinuado pela Microsoft (suporte incerto)"]),
            new ProdutoSuportado("In_build", "Webcam do notebook/smartphone", CategoriaDispositivo.WEBCAM, 0, StatusSpec.PARCIAL,
                [DeficienciaAlvo.SURDEZ], ["GRATUITO", "Sempre presente"], ["Qualidade varia muito", "Campo de visao estreito em notebooks", "Autofocus lento em cameras baratas"])
        ],
        150.0,
        "Webcam e a JANELA para Libras. Surdo se comunica por SINAIS. Sinais precisam de FRAMES RAPIDOS e CAMPO AMPLO. Webcam ruim = comunicacao cortada = exclusao."
    ));

    // === 10. TABLET (CAA) ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.TABLET,
        "Tablet para CAA (Comunicacao Aumentativa e Alternativa). Para nao-verbal (autismo nao-verbal, afasia, ELA). Toca figura/simbolo -> fala a palavra. Ou digita -> fala.",
        [DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.AUTISMO, DeficienciaAlvo.COGNITIVA, DeficienciaAlvo.NEUROLOGICA],
        [
            new Especificacao("Tela", "Minimo 10 polegadas", true, "Espaco para grade de simbolos CAA (minimo 8x8)."),
            new Especificacao("Touch", "Multitoque capacitivo (sensivel)", true, "Usuario com motora fina comprometida precisa de tela responsiva."),
            new Especificacao("Bateria", "Minimo 8h", true, "Dia de uso (escola, trabalho, terapia)."),
            new Especificacao("Sintetizador de voz", "Nativo + apps CAA", true, "Tablet sem TTS e so uma tela. Precisa FALAR."),
            new Especificacao("Software CAA", "Compativel com: Avaz, Proloquo, TD Snap", true, "Apps de CAA sao OBRIGATORIOS. Tablet sem apps CAA nao serve."),
            new Especificacao("Case protetor", "Case resistente a queda (military-grade)", true, "Crianca com autismo pode ter comportamento de quebrar. Tablet = R$ 1000+."),
            new Especificacao("Suporte", "Compativel com suportes de mesa/mobiliario", true, "Cadeirante precisa do tablet montado na cadeira.")
        ],
        [
            new ProdutoSuportado("Apple", "iPad (10th gen)", CategoriaDispositivo.TABLET, 3000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.AUTISMO], ["Melhor ecossistema de CAA do mercado", "Proloquo2Go (padrao ouro CAA)", "Avaz", "AssistiveTouch + Eye Tracking nativo", "Bateria 10h", "Case Logitech Crayon"], ["Custo alto"]),
            new ProdutoSuportado("Samsung", "Galaxy Tab A9+", CategoriaDispositivo.TABLET, 1000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.AUTISMO], ["Custo baixo para tablet", "Tela 11 polegadas", "Android (Avaz, TD Snap)", "Bateria 10h+"], ["Menos apps CAA que iOS", "Case protetor menos disponivel"]),
            new ProdutoSuportado("Apple", "iPad Pro 11", CategoriaDispositivo.TABLET, 7000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.MOTORA], ["Eye Tracking nativo (2024+)", "Proloquo2Go + Voice Control", "M-series chip (rapido)", "LiDAR"], ["Custo PREMIUM"]),
            new ProdutoSuportado("Amazon", "Fire HD 10", CategoriaDispositivo.TABLET, 600, StatusSpec.PARCIAL,
                [DeficienciaAlvo.AUTISMO], ["Custo MUITO baixo", "Tela 10.1 polegadas"], ["Sem Google Play nativo (apps CAA limitados)", "Sem Proloquo2Go (iOS only)", "Android fork (Fire OS)"])
        ],
        800.0,
        "Tablet CAA e a VOZ de quem nao fala. Crianca autista nao-verbal toca 'QUERO AGUA'. Tablet FALA: 'Quero agua'. Pessoa com ELA digita com os olhos. Tablet FALA a mensagem. Sem tablet CAA, a pessoa e PRISIONEIRA do silencio."
    ));

    // === 11. E-READER ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.E_READER,
        "E-reader (tela e-ink) para dislexia, baixa visao, daltonismo. Tela e-ink nao emite luz (nao cansa). Fonte pode ser ampliada sem limite. OpenDyslexic font ajuda dislexico a distinguir letras.",
        [DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.AUTISMO, DeficienciaAlvo.IDOSO],
        [
            new Especificacao("Tela", "E-ink (nao LCD/LED)", true, "E-ink nao emite luz azul. Nao cansa. Dislexico e TDAH sao sensivel a luz."),
            new Especificacao("Fonte ajustavel", "Sim (tamanho + familia + espacamento)", true, "OpenDyslexic, Atkinson Hyperlegible, espacamento entre linhas."),
            new Especificacao("Tamanho de fonte", "Ate minimo 36pt", true, "Baixa visao precisa de fonte grande. E-reader permite sem limite fisico."),
            new Especificacao("TTS", "Sim (text-to-speech integrado)", true, "Dislexico que cansa de ler pode OUVIR. Cego pode ouvir o livro todo."),
            new Especificacao("Contraste", "Ajustavel (escuro sobre claro, claro sobre escuro)", true, "Modo escuro (fundo preto, texto branco) para baixa visao e sensibilidade a luz."),
            new Especificacao("Suporte a formatos", "EPUB, PDF, TXT, HTML", true, "Nao pode prender o usuario num formato proprietario."),
            new Especificacao("Bateria", "Minimo 4 semanas", true, "E-ink consome quase nada. Meses de uso sem recarregar.")
        ],
        [
            new ProdutoSuportado("Amazon", "Kindle Paperwhite", CategoriaDispositivo.E_READER, 600, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA], ["E-ink 300ppi", "Fonte ajustavel + OpenDyslexic", "TTS (VoiceView)", "Contraste ajustavel", "Bateria semanas", "Iluminacao frontal (nao irrita)"], ["Formato proprietario (AZW3)", "Suporte a EPUB limitado"]),
            new ProdutoSuportado("Kobo", "Clara 2E", CategoriaDispositivo.E_READER, 700, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.TDAH], ["E-ink 300ppi", "Suporte nativo a EPUB", "OpenDyslexic nativo", "OverDrive (biblioteca publica)"], ["TTS limitado"]),
            new ProdutoSuportado("Kobo", "Libra H2O", CategoriaDispositivo.E_READER, 1000, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA], ["Tela 7 polegadas", "Botoes fisicos (virar pagina)", "EPUB nativo", "Resistente a agua"], ["Custo medio-alto"]),
            new ProdutoSuportado("Onyx", "Boox Note Air", CategoriaDispositivo.E_READER, 2500, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA], ["E-ink GRANDE (10.3 polegadas)", "Android (apps TTS, OpenDyslexic)", "Caneta (anotar)", "Todos formatos"], ["Custo alto", "Mais pesado que Kindle"])
        ],
        300.0,
        "E-reader e para QUEM LER Dói. Dislexico que desiste de livro impresso LE no e-reader (fonte OpenDyslexic, espacamento ajustado). Baixa visao que nao ve letra pequena AMPLIA sem limite. TDAH que se distrai com tela colorida FOCa no e-ink monocromatico."
    ));

    // === 12. GPS TRACKER ===
    specs.push(new SpecDispositivo(
        CategoriaDispositivo.GPS_TRACKER,
        "GPS tracker pessoal para criancas (perdida/abduzida), idosos (demencia/fuga), e pessoas com deficiencia cognitiva. Nao e smartphone -- e um RASTREADOR dedicado, simples, longa bateria.",
        [DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO, DeficienciaAlvo.COGNITIVA],
        [
            new Especificacao("GPS", "Sim (com A-GPS)", true, "Localizacao precisa (< 10m em externo)."),
            new Especificacao("Bateria", "Minimo 5 dias (ideal 15+)", true, "Crianca/idoso NAO vai lembrar de recarregar todo dia. Bateria longa e CRITICA."),
            new Especificacao("Botao SOS", "Sim (1 toque = alerta)", true, "Crianca aperta = pais recebem localizacao + alerta. Idoso aperta = socorro."),
            new Especificacao("Cerca virtual", "Sim (geofencing)", true, "Pais definem area segura. Crianca sai = alerta automatico."),
            new Especificacao("Resistencia", "IPX7+ (agua e impacto)", true, "Crianca derruba, molha, perde. Tracker precisa sobreviver."),
            new Especificacao("Conectividade", "4G LTE (chip SIM integrado)", true, "Nao depende de WiFi. Funciona em qualquer lugar com sinal celular."),
            new Especificacao("Tamanho", "Pequeno e discreto (< 50g)", true, "Crianca nao quer usar algo grande/visivel. Discreto = uso continuo."),
            new Especificacao("Audio bidirecional", "Sim (microfone + alto-falante)", false, "Pais podem FALAR com a crianca pelo tracker. Crianca pode chamar.")
        ],
        [
            new ProdutoSuportado("Apple", "AirTag", CategoriaDispositivo.GPS_TRACKER, 400, StatusSpec.PARCIAL,
                [DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO], ["Custo baixo", "Bateria 1 ANO", "Rede Find My (milhoes de iPhones)", "Discreto (31g)"], ["SEM GPS proprio (usa BLE + iPhones proximos)", "SEM botao SOS", "SEM audio bidirecional", "Nao funciona onde nao ha iPhone proximo"]),
            new ProdutoSuportado("Samsung", "Galaxy SmartTag2", CategoriaDispositivo.GPS_TRACKER, 200, StatusSpec.PARCIAL,
                [DeficienciaAlvo.CRIANCA], ["Custo baixo", "Bateria 500 dias", "Rede SmartThings Find", "Botao (chama IFTTT)"], ["Sem GPS proprio (BLE)", "Sem SOS direto", "Sem audio bidirecional"]),
            new ProdutoSuportado("Tuya", "Smart GPS Tracker (4G)", CategoriaDispositivo.GPS_TRACKER, 200, StatusSpec.CONFORME,
                [DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO], ["GPS REAL (com 4G)", "Botao SOS", "Audio bidirecional", "Cerca virtual", "Bateria 7-15 dias", "Custo baixo"], ["Qualidade de build variavel", "App generico (menos polido)"]),
            new ProdutoSuportado("GlobalSat", "TR-600", CategoriaDispositivo.GPS_TRACKER, 600, StatusSpec.CONFORME,
                [DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO], ["GPS + 4G", "Bateria 15 dias", "SOS + audio", "Cerca virtual", "Industrial (resistente)"], ["Grande (nao discreto para crianca)"]),
            new ProdutoSuportado("Angel Watch", "Angel Watch Co", CategoriaDispositivo.GPS_TRACKER, 1200, StatusSpec.RECOMENDADO,
                [DeficienciaAlvo.CRIANCA], ["RELOGIO GPS para crianca", "GPS + 4G + WiFi", "Chamada de voz (2 vias)", "SOS", "Cerca virtual", "Videochamada"], ["Bateria 2-3 dias (smartwatch = curta)", "Custo medio"])
        ],
        200.0,
        "GPS tracker e para QUEM NAO PODE PEDIR AJUDA. Crianca de 5 anos perdida no shopping nao liga para os pais. Idoso com Alzheimer nao lembra o proprio nome. Tracker = os pais ENCONTRAM sem depender do perdido. O Telefonista usa GPS do smartphone -- mas tracker dedicado e BACKUP."
    ));

    return specs;
}

class AccessibilityHardwareSpecEngine {
    constructor() {
        this.specs = initSpecs();
    }

    listarCategorias() {
        return this.specs.map(s => s.categoria);
    }

    specPorCategoria(cat) {
        return this.specs.find(s => s.categoria === cat) || null;
    }

    produtosPorCategoria(cat) {
        const s = this.specPorCategoria(cat);
        return s ? s.produtos : [];
    }

    produtosPorDeficiencia(defic) {
        const resultado = [];
        for (const s of this.specs) {
            for (const p of s.produtos) {
                if (p.deficienciasAtendidas.includes(defic)) {
                    resultado.push([p, s]);
                }
            }
        }
        return resultado;
    }

    produtosPorStatus(status) {
        const resultado = [];
        for (const s of this.specs) {
            for (const p of s.produtos) {
                if (p.status === status) resultado.push(p);
            }
        }
        return resultado;
    }

    produtosRecomendados() {
        return this.produtosPorStatus(StatusSpec.RECOMENDADO);
    }

    verificarProduto(cat, marca, modelo, specsAtendidas) {
        const s = this.specPorCategoria(cat);
        if (!s) return StatusSpec.NAO_CONFORME;
        const obrigatorios = s.specs.filter(sp => sp.obrigatorio);
        const todosAtendidos = obrigatorios.every(sp => specsAtendidas[sp.parametro] === true);
        if (todosAtendidos) {
            const opcionais = s.specs.filter(sp => !sp.obrigatorio);
            const opcAtendidos = opcionais.filter(sp => specsAtendidas[sp.parametro] === true).length;
            if (opcAtendidos === opcionais.length && opcionais.length > 0) return StatusSpec.RECOMENDADO;
            return StatusSpec.CONFORME;
        }
        const falhas = obrigatorios.filter(sp => specsAtendidas[sp.parametro] !== true).length;
        if (falhas <= 2) return StatusSpec.PARCIAL;
        return StatusSpec.NAO_CONFORME;
    }

    catalogoPorFaixaCusto() {
        const resultado = {};
        Object.values(NivelCusto).forEach(n => { resultado[n.rotulo] = []; });
        for (const s of this.specs) {
            for (const p of s.produtos) {
                const nivel = this._classificarCusto(p.precoAproxBrl);
                resultado[nivel.rotulo].push(p);
            }
        }
        return resultado;
    }

    _classificarCusto(preco) {
        for (const n of Object.values(NivelCusto)) {
            if (n.minReal <= preco && preco <= n.maxReal) return n;
        }
        return NivelCusto.ESPECIALIZADO;
    }

    scorecard() {
        const totalProdutos = this.specs.reduce((sum, s) => sum + s.produtos.length, 0);
        const recomendados = this.produtosRecomendados().length;
        const conformes = this.produtosPorStatus(StatusSpec.CONFORME).length;
        const parciais = this.produtosPorStatus(StatusSpec.PARCIAL).length;
        const naoConformes = this.produtosPorStatus(StatusSpec.NAO_CONFORME).length;
        const totalSpecs = this.specs.reduce((sum, s) => sum + s.specs.length, 0);
        const totalObrigatorias = this.specs.reduce((sum, s) => sum + s.specs.filter(sp => sp.obrigatorio).length, 0);
        return {
            "categorias_dispositivos": this.specs.length,
            "produtos_catalogados": totalProdutos,
            "produtos_recomendados": recomendados,
            "produtos_conformes": conformes,
            "produtos_parciais": parciais,
            "produtos_nao_conformes": naoConformes,
            "specs_totais": totalSpecs,
            "specs_obrigatorias": totalObrigatorias,
            "deficiencias_cobertas": Object.keys(DeficienciaAlvo).length
        };
    }
}

function _demo() {
    const e = new AccessibilityHardwareSpecEngine();

    console.log("=".repeat(70));
    console.log("OpenAccessibilityHardwareSpecs -- Hardware COTS para Acessibilidade");
    console.log("=".repeat(70));

    console.log(`\n[${e.specs.length} DISPOSITIVOS COTS ESPECIFICADOS]`);
    for (const s of e.specs) {
        const defs = s.deficienciasAtendidas.slice(0, 3).map(d => d.rotulo).join(", ");
        console.log(`  ${s.categoria.rotulo.padEnd(35, ".")} Custo min: R$ ${Math.round(s.custoMinimoBrl)}`);
        console.log(`  ${"".padEnd(35)} Atende: ${defs}...`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("[DETALHE] HEADPHONE BLUETOOTH -- Especificacoes");
    console.log("=".repeat(70));
    const hp = e.specPorCategoria(CategoriaDispositivo.HEADPHONE_BT);
    if (hp) {
        console.log(`\n  Descricao: ${hp.descricao}`);
        console.log(`\n  ESPECIFICACOES MINIMAS (${hp.specs.length} specs):`);
        for (const spec of hp.specs) {
            const flag = spec.obrigatorio ? "OBRIG" : "opc";
            console.log(`    [${flag}] ${spec.parametro}: ${spec.valorMinimo}`);
            console.log(`          -> ${spec.justificativa}`);
        }
        console.log(`\n  PRODUTOS SUPORTADOS (${hp.produtos.length}):`);
        for (const p of hp.produtos) {
            console.log(`\n    [${p.status.rotulo}] ${p.marca} ${p.modelo} -- R$ ${Math.round(p.precoAproxBrl)}`);
            console.log(`      Fortes: ${p.pontosFortes.slice(0, 3).join(", ")}`);
            console.log(`      Fracos: ${p.pontosFracos.slice(0, 3).join(", ")}`);
        }
    }

    console.log("\n" + "=".repeat(70));
    console.log("[CATALOGO COMPLETO -- Todos os dispositivos e produtos]");
    console.log("=".repeat(70));
    for (const s of e.specs) {
        console.log(`\n  --- ${s.categoria.rotulo} ---`);
        for (const p of s.produtos) {
            const flagMap = { "conforme": "OK", "parcial": "PARC", "nao_conforme": "NAO", "recomendado": "REC" };
            const flag = flagMap[p.status.id];
            console.log(`    [${flag}] ${p.marca} ${p.modelo.padEnd(30)} R$ ${p.precoAproxBrl.toFixed(0).padStart(6)}`);
        }
    }

    console.log("\n" + "=".repeat(70));
    console.log("[PRODUTOS POR DEFICIENCIA]");
    console.log("=".repeat(70));
    for (const defic of Object.values(DeficienciaAlvo)) {
        const prods = e.produtosPorDeficiencia(defic);
        if (prods.length > 0) {
            const nomes = prods.slice(0, 4).map(([p, _]) => `${p.marca} ${p.modelo}`);
            console.log(`\n  ${defic.rotulo} (${prods.length} produtos):`);
            for (const n of nomes) console.log(`    - ${n}`);
        }
    }

    console.log("\n" + "=".repeat(70));
    console.log("[CATALOGO POR FAIXA DE CUSTO]");
    console.log("=".repeat(70));
    const cat = e.catalogoPorFaixaCusto();
    for (const [faixa, prods] of Object.entries(cat)) {
        if (prods.length > 0) {
            console.log(`\n  ${faixa} (${prods.length} produtos):`);
            for (const p of prods.slice(0, 3)) {
                console.log(`    - ${p.marca} ${p.modelo} (R$ ${Math.round(p.precoAproxBrl)})`);
            }
        }
    }

    console.log("\n" + "=".repeat(70));
    console.log("[SCORECARD]");
    console.log("=".repeat(70));
    const sc = e.scorecard();
    for (const [k, v] of Object.entries(sc)) {
        console.log(`  ${k.padEnd(30, ".")} ${v}`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("FILOSOFIA -- Dispositivos que nao precisam ser feitos do zero");
    console.log("=".repeat(70));
    console.log(`
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
`);
}

if (require.main === module) {
    _demo();
}

module.exports = { AccessibilityHardwareSpecEngine, CategoriaDispositivo, DeficienciaAlvo, StatusSpec, NivelCusto };