# OpenAccessibilityHardwareSpecs -- Especificacoes de Hardware COTS para Acessibilidade

**Arquivo original:** `open-republic/core/open_accessibility_hardware_specs.py`

**Descricao:** =====================================================================================
"Dispositivos que nao precisam ser feitos do zero. Precisam ser ESPECIFICADOS."
O computador RISC-V e fabricado do zero (OpenSovereignTech).
Mas headphones, smartwatches, eye-trackers, braille displays -- esses sao COTS
(Commercial Off-The-Shelf). A Republica NAO precisa reinventar todos.
O que a Republica faz: define ESPECIFICACOES MINIMAS de acessibilidade.
Quem fabricar, segue a spec. Quem comprar, sabe o que esperar.
PRINCIPIO: "A especificacao nao pode ser alterada por um vendor."
A Republica define o padrao. Vendors implementam.
Se um produto nao atende a spec, NAO e comprado. NAO e recomendado.
OS 12 DISPOSITIVOS COTS ESPECIFICADOS:
1. HEADPHONE BLUETOOTH (acessibilidade auditiva, TTS, audio descricao)
2. SMARTPHONE (corpo estendido -- Telefonista)
3. SMARTWATCH (biometria, estresse, convulsao, queda)
4. EYE TRACKER (tetraplegia, ELA, mobilidade reduzida)
5. BRAILLE DISPLAY (cego, baixa visao)
6. SWITCH BUTTON (tetraplegia, paralisia cerebral, acesso por 1 toque)
7. BONE CONDUCTION (surdo unilateral, condutiva -- ouve pelo osso)
8. MICROFONE (comando de voz, fala-para-texto, Libras contexto)
9. WEBCAM (Libras, visao computacional, descricao de cena)
10. TABLET (CAA - Comunicacao Aumentativa e Alternativa)
11. E-READER (dislexia, baixa visao, Daltonismo)
12. GPS TRACKER (crianca perdida, idoso com demencia)
ALINHAMENTO CONSTITUCIONAL:
- P1: Dispositivo de acessibilidade e DIREITO, nao luxo. Spec minima garante.
- P2: Autonomia corporal -- o dispositivo e extensao do corpo.
- P6: Acesso universal = acesso ao hardware que permite acesso.
- P9 (Soberania): Spec imutavel. Vendor nao altera. Republica define.
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenAccessibilityHardwareSpecs -- Especificacoes de Hardware COTS para Acessibilidade
=====================================================================================
"Dispositivos que nao precisam ser feitos do zero. Precisam ser ESPECIFICADOS."

O computador RISC-V e fabricado do zero (OpenSovereignTech).
Mas headphones, smartwatches, eye-trackers, braille displays -- esses sao COTS
(Commercial Off-The-Shelf). A Republica NAO precisa reinventar todos.

O que a Republica faz: define ESPECIFICACOES MINIMAS de acessibilidade.
Quem fabricar, segue a spec. Quem comprar, sabe o que esperar.

PRINCIPIO: "A especificacao nao pode ser alterada por um vendor."
A Republica define o padrao. Vendors implementam.
Se um produto nao atende a spec, NAO e comprado. NAO e recomendado.

OS 12 DISPOSITIVOS COTS ESPECIFICADOS:

1. HEADPHONE BLUETOOTH (acessibilidade auditiva, TTS, audio descricao)
2. SMARTPHONE (corpo estendido -- Telefonista)
3. SMARTWATCH (biometria, estresse, convulsao, queda)
4. EYE TRACKER (tetraplegia, ELA, mobilidade reduzida)
5. BRAILLE DISPLAY (cego, baixa visao)
6. SWITCH BUTTON (tetraplegia, paralisia cerebral, acesso por 1 toque)
7. BONE CONDUCTION (surdo unilateral, condutiva -- ouve pelo osso)
8. MICROFONE (comando de voz, fala-para-texto, Libras contexto)
9. WEBCAM (Libras, visao computacional, descricao de cena)
10. TABLET (CAA - Comunicacao Aumentativa e Alternativa)
11. E-READER (dislexia, baixa visao, Daltonismo)
12. GPS TRACKER (crianca perdida, idoso com demencia)

ALINHAMENTO CONSTITUCIONAL:
- P1: Dispositivo de acessibilidade e DIREITO, nao luxo. Spec minima garante.
- P2: Autonomia corporal -- o dispositivo e extensao do corpo.
- P6: Acesso universal = acesso ao hardware que permite acesso.
- P9 (Soberania): Spec imutavel. Vendor nao altera. Republica define.

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. ENUMS (modulo-level)
// ============================================================================

classe CategoriaDispositivo herda de Enum:
    // Categorias de dispositivos COTS para acessibilidade.
    HEADPHONE_BT <- ("headphone_bt", "Headphone Bluetooth")
    SMARTPHONE <- ("smartphone", "Smartphone")
    SMARTWATCH <- ("smartwatch", "Smartwatch")
    EYE_TRACKER <- ("eye_tracker", "Eye Tracker")
    BRAILLE_DISPLAY <- ("braille_display", "Display Braille")
    SWITCH <- ("switch", "Switch Button (botao de acesso)")
    BONE_CONDUCTION <- ("bone_conduction", "Fone de Conducao Ossea")
    MICROFONE <- ("microfone", "Microfone")
    WEBCAM <- ("webcam", "Webcam")
    TABLET <- ("tablet", "Tablet (CAA)")
    E_READER <- ("e_reader", "E-reader (Leitor Digital)")
    GPS_TRACKER <- ("gps_tracker", "GPS Tracker (Pessoal)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe DeficienciaAlvo herda de Enum:
    // Quais deficiencias cada dispositivo atende.
    CEGUEIRA <- ("cegueira", "Cego / Baixa visao")
    SURDEZ <- ("surdez", "Surdo / Deficiente auditivo")
    MOTORA <- ("motora", "Motora / Tetraplegia / Paralisia cerebral")
    COGNITIVA <- ("cognitiva", "Cognitiva / Sindrome de Down")
    AUTISMO <- ("autismo", "TEA / Autismo")
    TDAH <- ("tdah", "TDAH / Dislexia")
    COMUNICACAO <- ("comunicacao", "Comunicacao (nao-verbal / afasia)")
    NEUROLOGICA <- ("neurologica", "Neurologica (ELA / Parkinson / Epilepsia)")
    IDOSO <- ("idoso", "Idoso (demencia / mobilidade reduzida)")
    CRIANCA <- ("crianca", "Crianca (seguranca / rastreamento)")
    UNIVERSAL <- ("universal", "Uso universal (todas as deficiencias)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe NivelCusto herda de Enum:
    // Faixa de custo do dispositivo.
    GRATUITO <- ("gratuito", "Gratuito (doacao / biblioteca)", 0, 0)
    BAIXO <- ("baixo", "Baixo custo (< R$ 100)", 1, 100)
    MEDIO <- ("medio", "Custo medio (R$ 100-500)", 101, 500)
    ALTO <- ("alto", "Custo alto (R$ 500-2000)", 501, 2000)
    PREMIUM <- ("premium", "Premium (R$ 2000-10000)", 2001, 10000)
    ESPECIALIZADO <- ("especializado", "Especializado (> R$ 10000)", 10001, 999999)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao min_real(self) retorna int:
        retorne self.value[2]

    // decorador: @property
    funcao max_real(self) retorna int:
        retorne self.value[3]


classe StatusSpec herda de Enum:
    // Status de conformidade de um produto com a spec da Republica.
    CONFORME <- ("conforme", "Conforme: atende todas as specs minimas")
    PARCIAL <- ("parcial", "Parcial: atende a maioria, mas tem lacunas")
    NAO_CONFORME <- ("nao_conforme", "Nao conforme: nao atende specs minimas")
    RECOMENDADO <- ("recomendado", "Recomendado: excede as specs minimas")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


// ============================================================================
// 2. DATACLASSES
// ============================================================================

// decorador: @dataclass
classe Especificacao:
    // Uma especificacao minima de hardware.
    parametro: str         // ex: "Bluetooth", "Bateria", "Latencia"
    valor_minimo: str      // ex: "5.0 (LE Audio)", "8h", "< 150ms"
    declare obrigatorio: bool  <- VERDADEIRO
    declare justificativa: str  <- ""  // por que esta spec importa para acessibilidade


// decorador: @dataclass
classe ProdutoSuportado:
    // Um produto COTS especifico que atende (ou nao) a spec.
    marca: str
    modelo: str
    categoria: CategoriaDispositivo
    preco_aprox_brl: float
    status: StatusSpec
    declare deficiencias_atendidas: List[DeficienciaAlvo]  <- field(default_factory=list)
    declare pontos_fortes: List[str]  <- field(default_factory=list)
    declare pontos_fracos: List[str]  <- field(default_factory=list)
    declare notes: str  <- ""


// decorador: @dataclass
classe SpecDispositivo:
    // Especificacao completa de um categoria de dispositivo.
    categoria: CategoriaDispositivo
    descricao: str
    deficiencias_atendidas: List[DeficienciaAlvo]
    declare specs: List[Especificacao]  <- field(default_factory=list)
    declare produtos: List[ProdutoSuportado]  <- field(default_factory=list)
    declare custo_minimo_brl: float  <- 0.0
    declare observacao: str  <- ""


// ============================================================================
// 3. DADOS: AS 12 ESPECIFICACOES
// ============================================================================

funcao _init_specs() retorna List[SpecDispositivo]:
    // Cria as 12 especificacoes de dispositivos COTS.
    retorne [

        // === 1. HEADPHONE BLUETOOTH ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.HEADPHONE_BT,
            descricao <- (
                "Headphone Bluetooth para acessibilidade auditiva. "
                "Usado para TTS (text-to-speech), audio descricao, legendas em audio, "
                "amplificacao para deficiente auditivo, e comunicacao com o Telefonista."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA,
                                    DeficienciaAlvo.UNIVERSAL, DeficienciaAlvo.IDOSO],
            custo_minimo_brl <- 80.0,
            specs <- [
                Especificacao("Bluetooth", "5.0 ou superior (LE Audio / aptX Adaptive)",
                              VERDADEIRO, "LE Audio reduz latencia e permite multi-stream (2 fones no mesmo dispositivo)."),
                Especificacao("Latencia", "< 200ms (ideal < 150ms)",
                              VERDADEIRO, "Latencia alta quebra TTS em tempo real e audio descricao sincronizada."),
                Especificacao("Bateria", "Minimo 8h uso continuo",
                              VERDADEIRO, "Dia de trabalho/estudo sem recarregar. Cego depende do fone o dia todo."),
                Especificacao("Microfone integrado", "Sim, com cancelamento de ruido",
                              VERDADEIRO, "Para comando de voz, chamadas, e Libras por contexto de audio."),
                Especificacao("Perfil Bluetooth", "A2DP + HFP + AVRCP",
                              VERDADEIRO, "A2DP = audio de qualidade. HFP = viva-voz. AVRCP = controle remoto."),
                Especificacao("Multiponto", "Sim (conectar 2 dispositivos simultaneamente)",
                              VERDADEIRO, "Cego pode estar conectado ao smartphone E ao computador ao mesmo tempo."),
                Especificacao("Controles fisicos", "Botoes reais (nao touch)",
                              VERDADEIRO, "Cego nao pode usar controles capacitivos sem feedback visual."),
                Especificacao("Feedback de bateria", "Anuncio de bateria por voz ou tom",
                              VERDADEIRO, "Cego precisa saber quando vai acabar sem ver o LED."),
                Especificacao("Conforto", "Ajustavel, leve (< 300g), alcolchoado",
                              VERDADEIRO, "Uso prolongado (8h+) requer conforto. Pessoas com sensibilidade sensorial (TEA) precisam de materiais suaves."),
                Especificacao("Codec", "SBC minimo. AAC/SBC/LDAC desejavel",
                              FALSO, "AAC melhora qualidade para usuarios de iPhone."),
                Especificacao("Resistencia", "IPX4 (suor e chuva)",
                              FALSO, "Para uso em mobilidade urbana."),
                Especificacao("Jack 3.5mm", "Sim (backup com fio)",
                              VERDADEIRO, "Se Bluetooth falha, fio e backup. Cego nao pode ficar sem audio."),
            ],
            produtos <- [
                ProdutoSuportado("JBL", "Tune 510BT", CategoriaDispositivo.HEADPHONE_BT, 250,
                    StatusSpec.CONFORME, [DeficienciaAlvo.UNIVERSAL],
                    ["Bateria 40h", "Multiponto", "Custo acessivel", "Jack 3.5mm"],
                    ["Sem anuncio de bateria por voz", "Controle touch (parcial)"]),
                ProdutoSuportado("Sony", "WH-CH520", CategoriaDispositivo.HEADPHONE_BT, 350,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.UNIVERSAL, DeficienciaAlvo.SURDEZ],
                    ["Bateria 50h", "Multiponto", "Anuncio de bateria por voz", "Controles fisicos"],
                    ["Sem jack 3.5mm (USB-C apenas)"]),
                ProdutoSuportado("Sennheiser", "HD 350BT", CategoriaDispositivo.HEADPHONE_BT, 500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.UNIVERSAL],
                    ["Bateria 30h", "AAC + aptX", "Confortavel 8h+", "USB-C charge"],
                    ["Sem jack 3.5mm"]),
                ProdutoSuportado("Anker", "Soundcore Life Q20", CategoriaDispositivo.HEADPHONE_BT, 250,
                    StatusSpec.CONFORME, [DeficienciaAlvo.UNIVERSAL],
                    ["Bateria 40h", "ANC basico", "Custo baixo"],
                    ["Multiponto instavel", "App requer visual"]),
                ProdutoSuportado("Philips", "SHL3070BK", CategoriaDispositivo.HEADPHONE_BT, 150,
                    StatusSpec.PARCIAL, [DeficienciaAlvo.UNIVERSAL],
                    ["Custo muito baixo", "Jack 3.5mm"],
                    ["Bateria 9h (minimo)", "Sem multiponto", "Latencia alta para TTS"]),
                ProdutoSuportado("Apple", "AirPods (2nd gen)", CategoriaDispositivo.HEADPHONE_BT, 1500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL],
                    ["Acessibilidade iOS nativa", "Live Listen (microfone remoto)",
                     "Audio descricao integrada", "Detecao de sons (Porta, Cachorro, Sirene)"],
                    ["Custo alto", "Sem controles fisicos (touch)",
                     "Bateria ~5h por carga (24h com case)"]),
                ProdutoSuportado("Apple", "AirPods Pro 2", CategoriaDispositivo.HEADPHONE_BT, 2500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL],
                    ["Live Listen", "ANC adaptativo",
                     "Modo Conversacao (transparencia)", "Detecao de sons ambiente"],
                    ["Custo premium", "Sem jack 3.5mm"]),
                ProdutoSuportado("Samsung", "Galaxy Buds FE", CategoriaDispositivo.HEADPHONE_BT, 600,
                    StatusSpec.CONFORME, [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.UNIVERSAL],
                    ["Live Listen no Android", "ANC", "Custo medio"],
                    ["Bateria ~6h por carga", "Sem jack"]),
            ],
            observacao <- (
                "O Headphone Bluetooth e o DISPOSITIVO MAIS UNIVERSAL da acessibilidade. "
                "Cego usa para TTS. Surdo usa para amplificacao e Live Listen. "
                "Tetraplegico usa para comando de voz. Idoso usa para amplificacao. "
                "A spec minima garante que QUALQUER headphone recomendado funciona para TODOS."
            ),
        ),

        // === 2. SMARTPHONE ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.SMARTPHONE,
            descricao <- (
                "Smartphone como CORPO ESTENDIDO (Telefonista). Camera=olhos, "
                "microfone=ouvidos, GPS=direcao, acelerometro=balance, smartwatch=biometria."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.SURDEZ,
                                    DeficienciaAlvo.MOTORA, DeficienciaAlvo.AUTISMO,
                                    DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.IDOSO,
                                    DeficienciaAlvo.CRIANCA, DeficienciaAlvo.UNIVERSAL],
            custo_minimo_brl <- 800.0,
            specs <- [
                Especificacao("Sistema operacional", "Android 13+ ou iOS 16+",
                              VERDADEIRO, "Versoes antigas nao tem features de acessibilidade criticas."),
                Especificacao("RAM", "Minimo 4GB (ideal 6GB+)",
                              VERDADEIRO, "Apps de acessibilidade (TalkBack, VoiceOver, Libras) consomem RAM."),
                Especificacao("Armazenamento", "Minimo 64GB",
                              VERDADEIRO, "Modelos de IA local + apps de CAA + mapas offline precisam de espaco."),
                Especificacao("Camera", "Minimo 12MP com autofocus + OIS",
                              VERDADEIRO, "Visao computacional (OCR, descricao de cena, Libras) precisa de camera decente."),
                Especificacao("Bateria", "Minimo 4000mAh",
                              VERDADEIRO, "Dia inteiro de uso com acessibilidade ativa (TTS + GPS + camera)."),
                Especificacao("TalkBack/VoiceOver", "Nativo e funcional",
                              VERDADEIRO, "Leitor de tela nativo e OBRIGATORIO. Sem ele, cego nao usa o telefone."),
                Especificacao("Bluetooth", "5.0+",
                              VERDADEIRO, "Para conectar headphones, hearing aids, braille displays."),
                Especificacao("GPS", "Sim, com A-GPS",
                              VERDADEIRO, "Navegacao para cego, rastreamento de crianca/idoso."),
                Especificacao("NFC", "Sim",
                              FALSO, "Pagamento sem QR code (OpenAntiQRPayment)."),
                Especificacao("Acelerometro/Giroscopio", "Sim",
                              VERDADEIRO, "Deteccao de queda (idoso), bussola para navegacao (cego)."),
                Especificacao("Slot microSD", "Desejavel",
                              FALSO, "Armazenamento expansivel para mapas offline e modelos de IA."),
                Especificacao("Radio FM", "Desejavel (com fone como antena)",
                              FALSO, "Emergencias: FM nao depende de internet."),
            ],
            produtos <- [
                ProdutoSuportado("Samsung", "Galaxy A15 5G", CategoriaDispositivo.SMARTPHONE, 1000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.UNIVERSAL],
                    ["Custo baixo", "Android 14", "Bateria 5000mAh",
                     "TalkBack nativo", "Camera 50MP", "Slot microSD"],
                    ["RAM 4GB (minimo)", "Sem OIS na camera"]),
                ProdutoSuportado("Samsung", "Galaxy A55 5G", CategoriaDispositivo.SMARTPHONE, 2000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.UNIVERSAL],
                    ["RAM 8GB", "Camera com OIS", "Bateria 5000mAh",
                     "Bixby Vision (descricao de cena)", "Modo Live Listen"],
                    ["Sem slot microSD (alguns mercados)"]),
                ProdutoSuportado("Motorola", "Moto G84 5G", CategoriaDispositivo.SMARTPHONE, 1300,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.UNIVERSAL],
                    ["RAM 8GB (otimo nesta faixa)", "Bateria 5000mAh",
                     "Android limpo (TalkBack funciona bem)", "Slot microSD"],
                    ["Camera sem OIS"]),
                ProdutoSuportado("Apple", "iPhone SE (2022)", CategoriaDispositivo.SMARTPHONE, 3000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.SURDEZ,
                                              DeficienciaAlvo.UNIVERSAL],
                    ["VoiceOver (melhor leitor de tela do mercado)",
                     "Detecao de pessoas, portas, sons (Magnifier)",
                     "Audio descricao", "Live Listen", "5 anos de update"],
                    ["Bateria 2018mAh (fraca)", "Tela 4.7 polegadas (pequena)"]),
                ProdutoSuportado("Apple", "iPhone 15", CategoriaDispositivo.SMARTPHONE, 5000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.UNIVERSAL],
                    ["VoiceOver + Magnifier + Detecao de sons",
                     "LiDAR (navegacao para cego)", "Camera 48MP",
                     "USB-C", "Live Listen"],
                    ["Custo premium"]),
                ProdutoSuportado("Xiaomi", "Redmi Note 13", CategoriaDispositivo.SMARTPHONE, 1100,
                    StatusSpec.CONFORME, [DeficienciaAlvo.UNIVERSAL],
                    ["Custo baixo", "Bateria 5000mAh", "Camera 108MP", "Slot microSD"],
                    ["MIUI tem bugs de acessibilidade", "TalkBack menos testado"]),
            ],
            observacao <- (
                "O smartphone e o CORACAO da acessibilidade da Republica. "
                "E camera, microfone, GPS, acelerometro, TTS, leitor de tela -- tudo num so dispositivo. "
                "A spec garante que QUALQUER smartphone recomendado roda a stack do Telefonista."
            ),
        ),

        // === 3. SMARTWATCH ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.SMARTWATCH,
            descricao <- (
                "Smartwatch para biometria continua: estresse (frequencia cardiaca), "
                "predicao de convulsao (temperatura + HR), deteccao de queda (idoso), "
                "lembretes (TDAH, idoso com demencia)."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.IDOSO,
                                    DeficienciaAlvo.TDAH, DeficienciaAlvo.AUTISMO,
                                    DeficienciaAlvo.MOTORA],
            custo_minimo_brl <- 400.0,
            specs <- [
                Especificacao("Sensor cardiaco", "Sim (PPG ou ECG)",
                              VERDADEIRO, "Deteccao de estresse, arritmia, taquicardia."),
                Especificacao("Acelerometro", "Sim (3 eixos)",
                              VERDADEIRO, "Deteccao de queda (idoso), tremor (Parkinson)."),
                Especificacao("GPS", "Sim (integrado)",
                              VERDADEIRO, "Rastreamento de crianca/idoso sem depender do smartphone."),
                Especificacao("Bateria", "Minimo 3 dias (ideal 7+)",
                              VERDADEIRO, "Biometria continua requer uso 24h. Recarga diaria e falha."),
                Especificacao("Resistencia", "IP68 (agua e poeira)",
                              VERDADEIRO, "Usa no banho, na chuva, na piscina. Biometria nao para."),
                Especificacao("Vibracao", "Motor haptico forte",
                              VERDADEIRO, "Surdo nao ouve alerta. Cego nao ve. Vibration e universal."),
                Especificacao("Tela sempre ligada", "Desejavel",
                              FALSO, "Idoso precisa ver as horas sem tocar na tela."),
                Especificacao("Temperatura corporea", "Desejavel",
                              FALSO, "Predicao de convulsao epileptica (pesquisa Apple Watch)."),
                Especificacao("SpO2 (oximetria)", "Desejavel",
                              FALSO, "Monitoramento respiratorio."),
            ],
            produtos <- [
                ProdutoSuportado("Amazfit", "Bip 5", CategoriaDispositivo.SMARTWATCH, 500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.IDOSO, DeficienciaAlvo.TDAH],
                    ["Bateria 10 DIAS", "GPS", "Tela grande (1.69 polegadas)",
                     "Custo baixo", "Vibracao forte"],
                    ["Sem ECG", "Sem SpO2 confiavel"]),
                ProdutoSuportado("Xiaomi", "Smart Band 8", CategoriaDispositivo.SMARTWATCH, 250,
                    StatusSpec.CONFORME, [DeficienciaAlvo.IDOSO, DeficienciaAlvo.TDAH],
                    ["Bateria 16 DIAS", "Custo muito baixo", "HR + SpO2",
                     "Leve (27g)"],
                    ["Sem GPS integrado (depende do telefone)",
                     "Tela pequena para idoso com baixa visao"]),
                ProdutoSuportado("Apple", "Apple Watch SE (2nd gen)", CategoriaDispositivo.SMARTWATCH, 2500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.NEUROLOGICA, DeficienciaAlvo.IDOSO],
                    ["Deteccao de queda (SOS automatico)",
                     "ECG (aprovado FDA)", "GPS integrado",
                     "Vibracao excelente", "Tela sempre ligada"],
                    ["Bateria ~18h (1 dia)", "Custo alto"]),
                ProdutoSuportado("Apple", "Apple Watch Series 9", CategoriaDispositivo.SMARTWATCH, 4500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.NEUROLOGICA],
                    ["ECG + SpO2 + Temperatura",
                     "Deteccao de queda + SOS", "GPS",
                     "Health Records (compartilha com medico)"],
                    ["Bateria ~18h", "Custo premium"]),
                ProdutoSuportado("Samsung", "Galaxy Watch FE", CategoriaDispositivo.SMARTWATCH, 1000,
                    StatusSpec.CONFORME, [DeficienciaAlvo.IDOSO],
                    ["ECG (em alguns paises)", "Bateria 2-3 dias",
                     "Deteccao de queda", "Android nativo"],
                    ["ECG bloqueado em alguns mercados"]),
                ProdutoSuportado("Garmin", "Forerunner 55", CategoriaDispositivo.SMARTWATCH, 1500,
                    StatusSpec.CONFORME, [DeficienciaAlvo.IDOSO],
                    ["Bateria 14 DIAS em modo watch",
                     "GPS de precisao", "Vibracao forte"],
                    ["Foco em esporte (menos features de saude)"]),
            ],
            observacao <- (
                "Smartwatch = biometria PASSIVA. O usuario nao precisa fazer nada. "
                "O relogio detecta queda e chama socorro. Detecta arritmia e avisa. "
                "E o sensor do corpo que o corpo nao tem (ou perdeu)."
            ),
        ),

        // === 4. EYE TRACKER ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.EYE_TRACKER,
            descricao <- (
                "Eye tracker para tetraplegia, ELA, paralisia cerebral. "
                "O olho e o ultimo musculo voluntario em ELA. "
                "Eye tracker permite digitar, clicar, comunicar -- SO COM OS OLHOS."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA,
                                    DeficienciaAlvo.COMUNICACAO],
            custo_minimo_brl <- 2000.0,
            specs <- [
                Especificacao("Precisao", "< 1 grau visual (ideal < 0.5)",
                              VERDADEIRO, "Para clicar em botoes pequenos na tela. Precisao baixa = frustracao."),
                Especificacao("Frequencia", "Minimo 60Hz (ideal 120Hz+)",
                              VERDADEIRO, "Taxa de atualizacao. Baixa = lag entre olhar e clique."),
                Especificacao("Calibracao", "Automatica ou 1-5 pontos",
                              VERDADEIRO, "Calibracao complexa (16 pontos) e exaustiva para quem tem mobilidade limitada."),
                Especificacao("Compatibilidade", "Windows + macOS + Linux",
                              VERDADEIRO, "Nao pode prender o usuario num SO."),
                Especificacao("Software inclusivo", "Teclado virtual + CAA",
                              VERDADEIRO, "Eye tracker sem software de comunicacao e so hardware inutil."),
                Especificacao("Latencia", "< 50ms",
                              VERDADEIRO, "Entre o olhar e o cursor responder. Alto = nauseas."),
                Especificacao("Trabalha com oculos", "Sim",
                              VERDADEIRO, "Muitos usuarios de eye tracker usam oculos."),
                Especificacao("Headbox", "Minimo 25x25cm",
                              VERDADEIRO, "Area de liberdade de movimento da cabeca. Pequeno = usuario precisa ficar imovel."),
            ],
            produtos <- [
                ProdutoSuportado("Tobii", "Eye Tracker 5", CategoriaDispositivo.EYE_TRACKER, 3500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA],
                    ["Precisao < 0.5 grau", "144Hz", "Headbox amplo",
                     "Software Tobii Communicator (CAA)", "Trabalha com oculos"],
                    ["Custo alto", "Windows-centric (Linux parcial)"]),
                ProdutoSuportado("Tobii", "Dynavox", CategoriaDispositivo.EYE_TRACKER, 15000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA,
                                              DeficienciaAlvo.COMUNICACAO],
                    ["Solucao completa (tablet + eye tracker + CAA)",
                     "Snap Core First (CAA)", "Suporte clinico"],
                    ["Custo ESPECIALIZADO", "Fornecedor unico"]),
                ProdutoSuportado("IRISBOND", "Hiru", CategoriaDispositivo.EYE_TRACKER, 5000,
                    StatusSpec.CONFORME, [DeficienciaAlvo.MOTORA],
                    ["Precisao < 0.5 grau", "Multiplataforma",
                     "Usado em hospitais brasileiros"],
                    ["Disponibilidade limitada no Brasil"]),
                ProdutoSuportado("Windows", "Eye Control (nativo)", CategoriaDispositivo.EYE_TRACKER, 0,
                    StatusSpec.CONFORME, [DeficienciaAlvo.MOTORA],
                    ["GRATUITO no Windows 10/11",
                     "Funciona com Tobii 4C e EyeX"],
                    ["So funciona com hardware Tobii",
                     "Limitado a Windows"]),
                ProdutoSuportado("Apple", "iPad com AssistiveTouch (olhos)", CategoriaDispositivo.EYE_TRACKER, 5000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.MOTORA],
                    ["Eye Tracking nativo no iPadOS (2024+)",
                     "GRATUITO (incluido no iPad)", "CAA integrada"],
                    ["So funciona em iPad Pro/Air recentes",
                     "Precisao pode variar"]),
            ],
            observacao <- (
                "Eye tracker e o DISPOSITIVO QUE DEVOLVE A VOZ. "
                "Pessoa com ELA perde tudo -- braços, pernas, voz. "
                "Sobra o olhar. Eye tracker transforma olhar em palavras."
            ),
        ),

        // === 5. BRAILLE DISPLAY ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.BRAILLE_DISPLAY,
            descricao <- (
                "Display Braille para cegos. Converte texto digital em celas braille "
                "táteis. E o OUTPUT equivalente ao leitor de tela -- mas para quem "
                "prefere ou precisa ler pelo tato (surdos-cegos nao tem audio)."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.CEGUEIRA],
            custo_minimo_brl <- 3000.0,
            specs <- [
                Especificacao("Celas", "Minimo 8 celas (ideal 40+)",
                              VERDADEIRO, "8 celas = palavra por vez. 40+ = linha inteira. Mais celas = leitura fluida."),
                Especificacao("Tipo de cela", "Piezoeletrica (8 pinos por cela)",
                              VERDADEIRO, "Braille de 8 pontos (computador). 6 pontos so perde informacao de formatacao."),
                Especificacao("Conexao", "Bluetooth + USB",
                              VERDADEIRO, "Bluetooth para smartphone. USB para computador. Ambos necessarios."),
                Especificacao("Bateria", "Minimo 10h",
                              VERDADEIRO, "Dia de trabalho/estudo. Recarga no meio do dia e falha."),
                Especificacao("Botoes de navegacao", "Sim (pan, rota, cursor routing)",
                              VERDADEIRO, "Navegar pelo texto sem depender do smartphone."),
                Especificacao("Compatibilidade", "TalkBack (Android) + VoiceOver (iOS) + NVDA/JAWS (PC)",
                              VERDADEIRO, "Display Braille sem leitor de tela e so pinos. Precisa do SOFTWARE."),
            ],
            produtos <- [
                ProdutoSuportado("Orbit Research", "Orbit Reader 20 Plus", CategoriaDispositivo.BRAILLE_DISPLAY, 4000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.CEGUEIRA],
                    ["20 celas (bom para custo)", "BLUETOOTH + USB",
                     "Bateria 20h", "Custo mais baixo do mercado para Braille",
                     "Nota: armazenamento interno (le sem smartphone)"],
                    ["20 celas limita leitura longa",
                     "Sem teclado Perkins integrado"]),
                ProdutoSuportado("Help Tech", "Active Star 40", CategoriaDispositivo.BRAILLE_DISPLAY, 12000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.CEGUEIRA],
                    ["40 celas (leitura fluida)", "Bluetooth + USB",
                     "Teclado Perkins integrado", "Bateria 20h+",
                     "Wi-Fi (le RSS, email)"],
                    ["Custo ESPECIALIZADO"]),
                ProdutoSuportado("Freedom Scientific", "Focus 40 Blue", CategoriaDispositivo.BRAILLE_DISPLAY, 10000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.CEGUEIRA],
                    ["40 celas", "Bluetooth + USB",
                     "Compativel com JAWS + NVDA + VoiceOver + TalkBack"],
                    ["Custo ESPECIALIZADO"]),
                ProdutoSuportado("Seika", "Seika 40", CategoriaDispositivo.BRAILLE_DISPLAY, 6000,
                    StatusSpec.CONFORME, [DeficienciaAlvo.CEGUEIRA],
                    ["40 celas", "Custo mais baixo para 40 celas",
                     "Bluetooth + USB"],
                    ["Qualidade de build inferior",
                     "Suporte limitado no Brasil"]),
                ProdutoSuportado("Apple", "iPhone/iPad com Braille (software)", CategoriaDispositivo.BRAILLE_DISPLAY, 0,
                    StatusSpec.PARCIAL, [DeficienciaAlvo.CEGUEIRA],
                    ["GRATUITO no iOS",
                     "Mostra Braille na tela (para videntes aprenderem)",
                     "Conecta com display fisico via Bluetooth"],
                    ["Nao e Braille TATIL (so visual)",
                     "Para cego real, precisa do display fisico"]),
            ],
            observacao <- (
                "Display Braille e o UNICO OUTPUT para SURDO-CEGO. "
                "Surdo-cego nao tem audio (surdo) nem tela (cego). "
                "Sobra o TATO. Display Braille e a janela para o mundo digital. "
                "O custo e alto (R$ 4000-15000) -- a Republica precisa subsidiar."
            ),
        ),

        // === 6. SWITCH BUTTON ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.SWITCH,
            descricao <- (
                "Switch button: botao grande de 1 toque para acesso. "
                "Para tetraplegia severa, paralisia cerebral, ELA avancada. "
                "1 toque = 1 acao. O computador escaneia opcoes e o usuario "
                "toca o switch na opcao certa."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.MOTORA, DeficienciaAlvo.NEUROLOGICA,
                                    DeficienciaAlvo.COMUNICACAO],
            custo_minimo_brl <- 100.0,
            specs <- [
                Especificacao("Forca de ativacao", "Maximo 100g (ideal < 50g)",
                              VERDADEIRO, "Usuario com paralisia cerebral pode nao conseguir apertar botao duro."),
                Especificacao("Tamanho da superficie", "Minimo 5cm diametro",
                              VERDADEIRO, "Alvo grande para quem tem tremor ou movimento involuntario."),
                Especificacao("Feedback", "Tatil (click) + auditivo (click) + visual (LED)",
                              VERDADEIRO, "O usuario PRECISA saber que ativou. Multi-modal."),
                Especificacao("Conexao", "Bluetooth e/ou Jack 3.5mm",
                              VERDADEIRO, "Jack 3.5mm = compatibilidade universal (AT, switch-adapted toys). BT = sem fio."),
                Especificacao("Resistencia", "A prova de impacto e saliva",
                              VERDADEIRO, "Usuario pode ter espasmo. Crianca pode morder/bater."),
                Especificacao("Montagem", "Compativel com braços articulados e suportes",
                              VERDADEIRO, "Switch precisa ser posicionado onde o usuario tem movimento."),
                Especificacao("Bateria", "Minimo 100h (ideal: meses)",
                              VERDADEIRO, "Switch com fio nao precisa. Switch BT precisa durar semanas."),
            ],
            produtos <- [
                ProdutoSuportado("Ablenet", "Big Red Switch", CategoriaDispositivo.SWITCH, 400,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.MOTORA],
                    ["Padrao da industria de AT", "Superficie 12.7cm",
                     "Forca ~57g", "Jack 3.5mm", "Resistente"],
                    ["Custo alto para um botao"]),
                ProdutoSuportado("Ablenet", "Spec Switch", CategoriaDispositivo.SWITCH, 350,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.MOTORA],
                    ["Superficie 5cm", "Forca muito baixa (~21g)",
                     "Ideal para ELA avancada"],
                    ["Custo alto"]),
                ProdutoSuportado("Enabling Devices", "Jelly Bean Switch", CategoriaDispositivo.SWITCH, 300,
                    StatusSpec.CONFORME, [DeficienciaAlvo.MOTORA],
                    ["Superficie 6.5cm", "Cores vivas (baixa visao)",
                     "Jack 3.5mm"],
                    ["Feedback menos firme que Ablenet"]),
                ProdutoSuportado("DIY", "Switch caseiro (pizza box + foil)", CategoriaDispositivo.SWITCH, 20,
                    StatusSpec.PARCIAL, [DeficienciaAlvo.MOTORA],
                    ["Custo MUITO baixo", "Customizavel",
                     "Tutorial aberto (CC0)"],
                    ["Durabilidade baixa", "Precisa manutencao frequente",
                     "Sem feedback de qualidade"]),
                ProdutoSuportado("Logitech", "Adaptive Gaming Kit", CategoriaDispositivo.SWITCH, 600,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.MOTORA],
                    ["3 switches grandes + 5 pequenos",
                     "Abas de etiqueta (identificacao tatil)",
                     "Custo razoavel para kit completo"],
                    ["Foco em gaming (adaptavel para AT)"]),
            ],
            observacao <- (
                "Switch e o DISPOSITIVO MAIS SIMPLES E MAIS PODEROSO. "
                "1 botao. 1 acao. Para quem so move 1 musculo (cabeca, braco, pe, sopro). "
                "Scanning: o computador mostra opcoes uma a uma. "
                "Switch na opcao certa = SELECAO. Comunicacao, controle, autonomia."
            ),
        ),

        // === 7. BONE CONDUCTION ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.BONE_CONDUCTION,
            descricao <- (
                "Fone de conducao ossea: som viaja pelo osso (cranio) ate o nervo auditivo, "
                "bypassando o ouvido externo e medio. Para surdo CONDUTIVO (problema no ouvido medio), "
                "estenose do canal, otite cronica. NAO funciona para surdo NEUROSSENSORIAL severo."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.SURDEZ],
            custo_minimo_brl <- 500.0,
            specs <- [
                Especificacao("Bluetooth", "5.0+",
                              VERDADEIRO, "Conexao estavel para TTS e audio descricao."),
                Especificacao("Orelha aberta", "Sim (nao bloqueia canal auditivo)",
                              VERDADEIRO, "Cego que usa conducao ossea PRECISA ouvir o ambiente tambem."),
                Especificacao("Bateria", "Minimo 6h",
                              VERDADEIRO, "Dia de uso continuo."),
                Especificacao("Microfone", "Sim",
                              VERDADEIRO, "Para comando de voz e chamadas."),
                Especificacao("Conforto", "Ajustavel, leve (< 40g)",
                              VERDADEIRO, "Repouso na teca (osso temporal). Pressao inadequada = dor."),
                Especificacao("Resistencia", "IPX4+ (suor)",
                              VERDADEIRO, "Uso em atividade fisica e mobilidade urbana."),
            ],
            produtos <- [
                ProdutoSuportado("Shokz", "OpenRun Pro", CategoriaDispositivo.BONE_CONDUCTION, 1200,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.SURDEZ],
                    ["Lider em conducao ossea", "Bateria 10h",
                     "Bluetooth 5.1", "Microfone", "IP67"],
                    ["Custo alto"]),
                ProdutoSuportado("Shokz", "OpenMove", CategoriaDispositivo.BONE_CONDUCTION, 600,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.SURDEZ],
                    ["Custo medio", "Bateria 6h",
                     "Bluetooth 5.1", "IP55"],
                    ["Qualidade de som inferior ao OpenRun Pro"]),
                ProdutoSuportado("Mojawa", "Run Plus", CategoriaDispositivo.BONE_CONDUCTION, 1000,
                    StatusSpec.CONFORME, [DeficienciaAlvo.SURDEZ],
                    ["Bateria 8h", "IP68", "MP3 integrado (16GB)"],
                    ["Marca menos estabelecida"]),
            ],
            observacao <- (
                "Conducao ossea e PARA SURDO CONDUTIVO especificamente. "
                "Surdo neurosensorial severo NAO beneficia. "
                "Importante: cego que tambem e surdo condutivo pode usar "
                "conducao ossea e AINDA ouvir o ambiente (orelha aberta)."
            ),
        ),

        // === 8. MICROFONE ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.MICROFONE,
            descricao <- (
                "Microfone para comando de voz, fala-para-texto, e captura de audio ambiente "
                "para o Telefonista. Para tetraplegico que so fala. Para surdo que precisa "
                "de legenda em tempo real. Para cego que interage por voz."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.MOTORA, DeficienciaAlvo.SURDEZ,
                                    DeficienciaAlvo.CEGUEIRA, DeficienciaAlvo.COMUNICACAO],
            custo_minimo_brl <- 50.0,
            specs <- [
                Especificacao("Cancelamento de ruido", "Sim (DSP ou cardiode)",
                              VERDADEIRO, "Comando de voz em ambiente ruidoso precisa de CNR."),
                Especificacao("Conexao", "USB ou Bluetooth",
                              VERDADEIRO, "USB = zero latencia. BT = mobilidade."),
                Especificacao("Padrao polar", "Cardiode ou unidirecional",
                              VERDADEIRO, "Captura a voz do usuario, nao o ambiente inteiro."),
                Especificacao("Frequencia", "100Hz-10kHz minimo",
                              VERDADEIRO, "Cobre voz humana. Baixa frequencia = graves (homem). Alta = agudos (mulher/crianca)."),
                Especificacao("Mute fisico", "Botao de mute REAL (nao software)",
                              VERDADEIRO, "Privacidade: usuario PRECISA saber que o microfone esta mudo."),
                Especificacao("LED indicador", "Sim (LED mostra se esta captando)",
                              VERDADEIRO, "Surdo nao ouve o proprio audio. Precisa VER que o microfone esta ativo."),
                Especificacao("Filtro pop", "Sim (espuma ou malha)",
                              FALSO, "Reduz 'p' e 't' que estouram o reconhecimento de voz."),
            ],
            produtos <- [
                ProdutoSuportado("Blue", "Yeti Nano", CategoriaDispositivo.MICROFONE, 500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.MOTORA, DeficienciaAlvo.CEGUEIRA],
                    ["USB-C", "Cardiode + omnidirecional",
                     "Mute fisico (botao na frente)", "Qualidade excelente"],
                    ["Grande (ocupa espaco na mesa)"]),
                ProdutoSuportado("Fifine", "K669B", CategoriaDispositivo.MICROFONE, 150,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.MOTORA],
                    ["Custo MUITO baixo", "USB", "Cardiode",
                     "Tripé incluido"],
                    ["Sem mute fisico", "Qualidade decente mas nao premium"]),
                ProdutoSuportado("Jabra", "Speak 510", CategoriaDispositivo.MICROFONE, 700,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.MOTORA, DeficienciaAlvo.SURDEZ],
                    ["Bluetooth + USB", "CNR excelente",
                     "Speakerphone (para reuniao com legenda)", "Mute fisico"],
                    ["Custo medio-alto"]),
                ProdutoSuportado("In_build", "Microfone do smartphone", CategoriaDispositivo.MICROFONE, 0,
                    StatusSpec.PARCIAL, [DeficienciaAlvo.UNIVERSAL],
                    ["GRATUITO", "Sempre presente", "Portatil"],
                    ["Qualidade varia", "CNR limitado",
                     "Nao ideal para texto longo"]),
            ],
            observacao <- (
                "Microfone e a ENTRADA para quem SO FALA. "
                "Tetraplegico que nao digita, FALA. Precisa de microfone bom. "
                "Surdo que precisa de legenda em tempo real, precisa capturar audio. "
                "Cego que navega por voz, precisa de microfone confiavel."
            ),
        ),

        // === 9. WEBCAM ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.WEBCAM,
            descricao <- (
                "Webcam para Libras (surdo se comunica por sinais na camera), "
                "visao computacional (descricao de cena para cego), e "
                "rastreamento de mao (linguagem de sinais como input)."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA],
            custo_minimo_brl <- 150.0,
            specs <- [
                Especificacao("Resolucao", "Minimo 720p (ideal 1080p)",
                              VERDADEIRO, "Libras requer resolucao suficiente para ver expressoes faciais e maos."),
                Especificacao("Frequencia", "Minimo 30fps (ideal 60fps)",
                              VERDADEIRO, "Libras e RAPIDO. 15fps perde sinais. 60fps captura tudo."),
                Especificacao("Autofocus", "Sim (rapido)",
                              VERDADEIRO, "Surdo que se move ao sinais nao pode ficar borrado."),
                Especificacao("Campo de visao", "Minimo 70 graus (ideal 90+)",
                              VERDADEIRO, "Libras requer espaco para maos e bracos. Webcam estreita corta os sinais."),
                Especificacao("Baixa luz", "Funciona em < 50 lux",
                              VERDADEIRO, "Nem todos tem iluminacao de estudio. Sala de casa a noite."),
                Especificacao("Microfone integrado", "Desejavel (backup)",
                              FALSO, "Para videochamada com surdo (audio + Libras simultaneo)."),
            ],
            produtos <- [
                ProdutoSuportado("Logitech", "C920 HD Pro", CategoriaDispositivo.WEBCAM, 400,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.SURDEZ, DeficienciaAlvo.CEGUEIRA],
                    ["1080p 30fps", "Autofocus rapido", "Campo 78 graus",
                     "Excelente baixa luz", "Microfone stereo"],
                    ["Sem 60fps em 1080p"]),
                ProdutoSuportado("Logitech", "C922 Pro", CategoriaDispositivo.WEBCAM, 500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.SURDEZ],
                    ["1080p 30fps / 720p 60fps", "Fundo substituivel",
                     "Tripé incluido"],
                    ["Custo medio-alto"]),
                ProdutoSuportado("Microsoft", "LifeCam Studio", CategoriaDispositivo.WEBCAM, 600,
                    StatusSpec.CONFORME, [DeficienciaAlvo.SURDEZ],
                    ["1080p", "Campo 75 graus",
                     "Alta qualidade de build"],
                    ["Descontinuado pela Microsoft (suporte incerto)"]),
                ProdutoSuportado("In_build", "Webcam do notebook/smartphone", CategoriaDispositivo.WEBCAM, 0,
                    StatusSpec.PARCIAL, [DeficienciaAlvo.SURDEZ],
                    ["GRATUITO", "Sempre presente"],
                    ["Qualidade varia muito", "Campo de visao estreito em notebooks",
                     "Autofocus lento em cameras baratas"]),
            ],
            observacao <- (
                "Webcam e a JANELA para Libras. Surdo se comunica por SINAIS. "
                "Sinais precisam de FRAMES RAPIDOS e CAMPO AMPLO. "
                "Webcam ruim = comunicacao cortada = exclusao."
            ),
        ),

        // === 10. TABLET (CAA) ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.TABLET,
            descricao <- (
                "Tablet para CAA (Comunicacao Aumentativa e Alternativa). "
                "Para nao-verbal (autismo nao-verbal, afasia, ELA). "
                "Toca figura/simbolo -> fala a palavra. Ou digita -> fala."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.AUTISMO,
                                    DeficienciaAlvo.COGNITIVA, DeficienciaAlvo.NEUROLOGICA],
            custo_minimo_brl <- 800.0,
            specs <- [
                Especificacao("Tela", "Minimo 10 polegadas",
                              VERDADEIRO, "Espaco para grade de simbolos CAA (minimo 8x8)."),
                Especificacao("Touch", "Multitoque capacitivo (sensivel)",
                              VERDADEIRO, "Usuario com motora fina comprometida precisa de tela responsiva."),
                Especificacao("Bateria", "Minimo 8h",
                              VERDADEIRO, "Dia de uso (escola, trabalho, terapia)."),
                Especificacao("Sintetizador de voz", "Nativo + apps CAA",
                              VERDADEIRO, "Tablet sem TTS e so uma tela. Precisa FALAR."),
                Especificacao("Software CAA", "Compativel com: Avaz, Proloquo, TD Snap",
                              VERDADEIRO, "Apps de CAA sao OBRIGATORIOS. Tablet sem apps CAA nao serve."),
                Especificacao("Case protetor", "Case resistente a queda (military-grade)",
                              VERDADEIRO, "Crianca com autismo pode ter comportamento de quebrar. Tablet = R$ 1000+."),
                Especificacao("Suporte", "Compativel com suportes de mesa/mobiliario",
                              VERDADEIRO, "Cadeirante precisa do tablet montado na cadeira."),
            ],
            produtos <- [
                ProdutoSuportado("Apple", "iPad (10th gen)", CategoriaDispositivo.TABLET, 3000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.AUTISMO],
                    ["Melhor ecossistema de CAA do mercado",
                     "Proloquo2Go (padrao ouro CAA)", "Avaz",
                     "AssistiveTouch + Eye Tracking nativo",
                     "Bateria 10h", "Case Logitech Crayon"],
                    ["Custo alto"]),
                ProdutoSuportado("Samsung", "Galaxy Tab A9+", CategoriaDispositivo.TABLET, 1000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.AUTISMO],
                    ["Custo baixo para tablet", "Tela 11 polegadas",
                     "Android (Avaz, TD Snap)", "Bateria 10h+"],
                    ["Menos apps CAA que iOS",
                     "Case protetor menos disponivel"]),
                ProdutoSuportado("Apple", "iPad Pro 11", CategoriaDispositivo.TABLET, 7000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.COMUNICACAO, DeficienciaAlvo.MOTORA],
                    ["Eye Tracking nativo (2024+)",
                     "Proloquo2Go + Voice Control",
                     "M-series chip (rapido)", "LiDAR"],
                    ["Custo PREMIUM"]),
                ProdutoSuportado("Amazon", "Fire HD 10", CategoriaDispositivo.TABLET, 600,
                    StatusSpec.PARCIAL, [DeficienciaAlvo.AUTISMO],
                    ["Custo MUITO baixo", "Tela 10.1 polegadas"],
                    ["Sem Google Play nativo (apps CAA limitados)",
                     "Sem Proloquo2Go (iOS only)",
                     "Android fork (Fire OS)"]),
            ],
            observacao <- (
                "Tablet CAA e a VOZ de quem nao fala. "
                "Crianca autista nao-verbal toca 'QUERO AGUA'. Tablet FALA: 'Quero agua'. "
                "Pessoa com ELA digita com os olhos. Tablet FALA a mensagem. "
                "Sem tablet CAA, a pessoa e PRISIONEIRA do silencio."
            ),
        ),

        // === 11. E-READER ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.E_READER,
            descricao <- (
                "E-reader (tela e-ink) para dislexia, baixa visao, daltonismo. "
                "Tela e-ink nao emite luz (nao cansa). Fonte pode ser ampliada sem limite. "
                "OpenDyslexic font ajuda dislexico a distinguir letras."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA,
                                    DeficienciaAlvo.AUTISMO, DeficienciaAlvo.IDOSO],
            custo_minimo_brl <- 300.0,
            specs <- [
                Especificacao("Tela", "E-ink (nao LCD/LED)",
                              VERDADEIRO, "E-ink nao emite luz azul. Nao cansa. Dislexico e TDAH sao sensivel a luz."),
                Especificacao("Fonte ajustavel", "Sim (tamanho + familia + espacamento)",
                              VERDADEIRO, "OpenDyslexic, Atkinson Hyperlegible, espacamento entre linhas."),
                Especificacao("Tamanho de fonte", "Ate minimo 36pt",
                              VERDADEIRO, "Baixa visao precisa de fonte grande. E-reader permite sem limite fisico."),
                Especificacao("TTS", "Sim (text-to-speech integrado)",
                              VERDADEIRO, "Dislexico que cansa de ler pode OUVIR. Cego pode ouvir o livro todo."),
                Especificacao("Contraste", "Ajustavel (escuro sobre claro, claro sobre escuro)",
                              VERDADEIRO, "Modo escuro (fundo preto, texto branco) para baixa visao e sensibilidade a luz."),
                Especificacao("Suporte a formatos", "EPUB, PDF, TXT, HTML",
                              VERDADEIRO, "Nao pode prender o usuario num formato proprietario."),
                Especificacao("Bateria", "Minimo 4 semanas",
                              VERDADEIRO, "E-ink consome quase nada. Meses de uso sem recarregar."),
            ],
            produtos <- [
                ProdutoSuportado("Amazon", "Kindle Paperwhite", CategoriaDispositivo.E_READER, 600,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA],
                    ["E-ink 300ppi", "Fonte ajustavel + OpenDyslexic",
                     "TTS (VoiceView)", "Contraste ajustavel",
                     "Bateria semanas", "Iluminacao frontal (nao irrita)"],
                    ["Formato proprietario (AZW3)",
                     "Suporte a EPUB limitado"]),
                ProdutoSuportado("Kobo", "Clara 2E", CategoriaDispositivo.E_READER, 700,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.TDAH],
                    ["E-ink 300ppi", "Suporte nativo a EPUB",
                     "OpenDyslexic nativo", "OverDrive (biblioteca publica)"],
                    ["TTS limitado"]),
                ProdutoSuportado("Kobo", "Libra H2O", CategoriaDispositivo.E_READER, 1000,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA],
                    ["Tela 7 polegadas", "Botoes fisicos (virar pagina)",
                     "EPUB nativo", "Resistente a agua"],
                    ["Custo medio-alto"]),
                ProdutoSuportado("Onyx", "Boox Note Air", CategoriaDispositivo.E_READER, 2500,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.TDAH, DeficienciaAlvo.CEGUEIRA],
                    ["E-ink GRANDE (10.3 polegadas)",
                     "Android (apps TTS, OpenDyslexic)", "Caneta (anotar)",
                     "Todos formatos"],
                    ["Custo alto", "Mais pesado que Kindle"]),
            ],
            observacao <- (
                "E-reader e para QUEM LER Dói. "
                "Dislexico que desiste de livro impresso LE no e-reader "
                "(fonte OpenDyslexic, espacamento ajustado). "
                "Baixa visao que nao ve letra pequena AMPLIA sem limite. "
                "TDAH que se distrai com tela colorida FOCa no e-ink monocromatico."
            ),
        ),

        // === 12. GPS TRACKER ===
        SpecDispositivo(
            categoria <- CategoriaDispositivo.GPS_TRACKER,
            descricao <- (
                "GPS tracker pessoal para criancas (perdida/abduzida), "
                "idosos (demencia/fuga), e pessoas com deficiencia cognitiva. "
                "Nao e smartphone -- e um RASTREADOR dedicado, simples, longa bateria."
            ),
            deficiencias_atendidas <- [DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO,
                                    DeficienciaAlvo.COGNITIVA],
            custo_minimo_brl <- 200.0,
            specs <- [
                Especificacao("GPS", "Sim (com A-GPS)",
                              VERDADEIRO, "Localizacao precisa (< 10m em externo)."),
                Especificacao("Bateria", "Minimo 5 dias (ideal 15+)",
                              VERDADEIRO, "Crianca/idoso NAO vai lembrar de recarregar todo dia. Bateria longa e CRITICA."),
                Especificacao("Botao SOS", "Sim (1 toque = alerta)",
                              VERDADEIRO, "Crianca aperta = pais recebem localizacao + alerta. Idoso aperta = socorro."),
                Especificacao("Cerca virtual", "Sim (geofencing)",
                              VERDADEIRO, "Pais definem area segura. Crianca sai = alerta automatico."),
                Especificacao("Resistencia", "IPX7+ (agua e impacto)",
                              VERDADEIRO, "Crianca derruba, molha, perde. Tracker precisa sobreviver."),
                Especificacao("Conectividade", "4G LTE (chip SIM integrado)",
                              VERDADEIRO, "Nao depende de WiFi. Funciona em qualquer lugar com sinal celular."),
                Especificacao("Tamanho", "Pequeno e discreto (< 50g)",
                              VERDADEIRO, "Crianca nao quer usar algo grande/visivel. Discreto = uso continuo."),
                Especificacao("Audio bidirecional", "Sim (microfone + alto-falante)",
                              FALSO, "Pais podem FALAR com a crianca pelo tracker. Crianca pode chamar."),
            ],
            produtos <- [
                ProdutoSuportado("Apple", "AirTag", CategoriaDispositivo.GPS_TRACKER, 400,
                    StatusSpec.PARCIAL, [DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO],
                    ["Custo baixo", "Bateria 1 ANO",
                     "Rede Find My (milhoes de iPhones)", "Discreto (31g)"],
                    ["SEM GPS proprio (usa BLE + iPhones proximos)",
                     "SEM botao SOS", "SEM audio bidirecional",
                     "Nao funciona onde nao ha iPhone proximo"]),
                ProdutoSuportado("Samsung", "Galaxy SmartTag2", CategoriaDispositivo.GPS_TRACKER, 200,
                    StatusSpec.PARCIAL, [DeficienciaAlvo.CRIANCA],
                    ["Custo baixo", "Bateria 500 dias",
                     "Rede SmartThings Find", "Botao (chama IFTTT)"],
                    ["Sem GPS proprio (BLE)", "Sem SOS direto",
                     "Sem audio bidirecional"]),
                ProdutoSuportado("Tuya", "Smart GPS Tracker (4G)", CategoriaDispositivo.GPS_TRACKER, 200,
                    StatusSpec.CONFORME, [DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO],
                    ["GPS REAL (com 4G)", "Botao SOS",
                     "Audio bidirecional", "Cerca virtual",
                     "Bateria 7-15 dias", "Custo baixo"],
                    ["Qualidade de build variavel",
                     "App generico (menos polido)"]),
                ProdutoSuportado("GlobalSat", "TR-600", CategoriaDispositivo.GPS_TRACKER, 600,
                    StatusSpec.CONFORME, [DeficienciaAlvo.CRIANCA, DeficienciaAlvo.IDOSO],
                    ["GPS + 4G", "Bateria 15 dias",
                     "SOS + audio", "Cerca virtual",
                     "Industrial (resistente)"],
                    ["Grande (nao discreto para crianca)"]),
                ProdutoSuportado("Angel Watch", "Angel Watch Co", CategoriaDispositivo.GPS_TRACKER, 1200,
                    StatusSpec.RECOMENDADO, [DeficienciaAlvo.CRIANCA],
                    ["RELOGIO GPS para crianca", "GPS + 4G + WiFi",
                     "Chamada de voz (2 vias)", "SOS",
                     "Cerca virtual", "Videochamada"],
                    ["Bateria 2-3 dias (smartwatch = curta)",
                     "Custo medio"]),
            ],
            observacao <- (
                "GPS tracker e para QUEM NAO PODE PEDIR AJUDA. "
                "Crianca de 5 anos perdida no shopping nao liga para os pais. "
                "Idoso com Alzheimer nao lembra o proprio nome. "
                "Tracker = os pais ENCONTRAM sem depender do perdido. "
                "O Telefonista usa GPS do smartphone -- mas tracker dedicado e BACKUP."
            ),
        ),
    ]


// ============================================================================
// 4. ENGINE
// ============================================================================

classe AccessibilityHardwareSpecEngine:
    // Motor de especificacoes de hardware COTS para acessibilidade.

    funcao __init__(self) retorna None:
        self.specs: List[SpecDispositivo] = _init_specs()

    // -- consulta ----------------------------------------------------------

    funcao listar_categorias(self) retorna List[CategoriaDispositivo]:
        retorne [s.categoria for s in self.specs]

    funcao spec_por_categoria(self, cat: CategoriaDispositivo) retorna Optional[SpecDispositivo]:
        para cada s em self.specs:
            se s.categoria == cat entao:
                retorne s
        retorne nulo

    funcao produtos_por_categoria(self, cat: CategoriaDispositivo) retorna List[ProdutoSuportado]:
        s <- self.spec_por_categoria(cat)
        retorne s.produtos if s else []

    funcao produtos_por_deficiencia(self, defic: DeficienciaAlvo) retorna List[Tuple[ProdutoSuportado, SpecDispositivo]]:
        // Retorna produtos que atendem uma deficiencia especifica.
        declare resultado: List[Tuple[ProdutoSuportado, SpecDispositivo]]  <- []
        para cada s em self.specs:
            para cada p em s.produtos:
                se defic in p.deficiencias_atendidas entao:
                    resultado.append((p, s))
        retorne resultado

    funcao produtos_por_status(self, status: StatusSpec) retorna List[ProdutoSuportado]:
        declare resultado: List[ProdutoSuportado]  <- []
        para cada s em self.specs:
            para cada p em s.produtos:
                se p.status == status entao:
                    resultado.append(p)
        retorne resultado

    funcao produtos_recomendados(self) retorna List[ProdutoSuportado]:
        retorne self.produtos_por_status(StatusSpec.RECOMENDADO)

    // -- verificar conformidade -------------------------------------------

    def verificar_produto(
        self,
        cat: CategoriaDispositivo,
        marca: str,
        modelo: str,
        specs_atendidas: Dict[str, bool],
    ) -> StatusSpec:
        // Verifica se um produto atende as specs minimas de uma categoria.
        s <- self.spec_por_categoria(cat)
        se s e nulo entao:
            retorne StatusSpec.NAO_CONFORME
        obrigatorios <- [spec for spec in s.specs if spec.obrigatorio]
        todos_atendidos <- all(specs_atendidas.get(spec.parametro, FALSO) for spec in obrigatorios)
        se todos_atendidos entao:
            // verificar se tambem atende os opcionais
            opcionais <- [spec for spec in s.specs if NAO  spec.obrigatorio]
            opc_atendidos <- sum(1 for spec in opcionais if specs_atendidas.get(spec.parametro, FALSO))
            se opc_atendidos == len(opcionais)  E  len(opcionais) > 0 entao:
                retorne StatusSpec.RECOMENDADO
            retorne StatusSpec.CONFORME
        // contar quantos obrigatorios falham
        falhas <- sum(1 for spec in obrigatorios if NAO  specs_atendidas.get(spec.parametro, FALSO))
        se falhas <= 2 entao:
            retorne StatusSpec.PARCIAL
        retorne StatusSpec.NAO_CONFORME

    // -- catalogo por custo -----------------------------------------------

    funcao catalogo_por_faixa_custo(self) retorna Dict[str, List[ProdutoSuportado]]:
        // Agrupa produtos por faixa de custo.
        declare resultado: Dict[str, List[ProdutoSuportado]]  <- defaultdict(list)
        para cada s em self.specs:
            para cada p em s.produtos:
                nivel <- self._classificar_custo(p.preco_aprox_brl)
                resultado[nivel.rotulo].append(p)
        retorne dict(resultado)

    funcao _classificar_custo(self, preco: float) retorna NivelCusto:
        para cada n em NivelCusto:
            se n.min_real <= preco <= n.max_real entao:
                retorne n
        retorne NivelCusto.ESPECIALIZADO

    // -- scorecard ---------------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        total_produtos <- sum(len(s.produtos) for s in self.specs)
        recomendados <- len(self.produtos_recomendados())
        conformes <- len(self.produtos_por_status(StatusSpec.CONFORME))
        parciais <- len(self.produtos_por_status(StatusSpec.PARCIAL))
        nao_conformes <- len(self.produtos_por_status(StatusSpec.NAO_CONFORME))
        total_specs <- sum(len(s.specs) for s in self.specs)
        total_obrigatorias <- sum(len([sp for sp in s.specs if sp.obrigatorio]) for s in self.specs)
        retorne {
            "categorias_dispositivos": len(self.specs),
            "produtos_catalogados": total_produtos,
            "produtos_recomendados": recomendados,
            "produtos_conformes": conformes,
            "produtos_parciais": parciais,
            "produtos_nao_conformes": nao_conformes,
            "specs_totais": total_specs,
            "specs_obrigatorias": total_obrigatorias,
            "deficiencias_cobertas": len(list(DeficienciaAlvo)),
        }


// ============================================================================
// 5. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- AccessibilityHardwareSpecEngine()

    print("=" * 70)
    print("OpenAccessibilityHardwareSpecs -- Hardware COTS para Acessibilidade")
    print("=" * 70)

    // --- Lista de categorias ---
    print(f"\n[{len(e.specs)} DISPOSITIVOS COTS ESPECIFICADOS]")
    para cada s em e.specs:
        defs <- ", ".join(d.rotulo for d in s.deficiencias_atendidas[:3])
        print(f"  {s.categoria.rotulo:.<35} Custo min: R$ {s.custo_minimo_brl:.0f}")
        print(f"  {'':35} Atende: {defs}...")

    // --- Detalhe: Headphone Bluetooth ---
    print("\n" + "=" * 70)
    print("[DETALHE] HEADPHONE BLUETOOTH -- Especificacoes")
    print("=" * 70)
    hp <- e.spec_por_categoria(CategoriaDispositivo.HEADPHONE_BT)
    se hp entao:
        print(f"\n  Descricao: {hp.descricao}")
        print(f"\n  ESPECIFICACOES MINIMAS ({len(hp.specs)} specs):")
        para cada spec em hp.specs:
            flag <- "OBRIG" if spec.obrigatorio else "opc"
            print(f"    [{flag}] {spec.parametro}: {spec.valor_minimo}")
            print(f"          -> {spec.justificativa}")
        print(f"\n  PRODUTOS SUPORTADOS ({len(hp.produtos)}):")
        para cada p em hp.produtos:
            print(f"\n    [{p.status.rotulo}] {p.marca} {p.modelo} -- R$ {p.preco_aprox_brl:.0f}")
            print(f"      Fortes: {', '.join(p.pontos_fortes[:3])}")
            print(f"      Fracos: {', '.join(p.pontos_fracos[:3])}")

    // --- Catalogo completo ---
    print("\n" + "=" * 70)
    print("[CATALOGO COMPLETO -- Todos os dispositivos e produtos]")
    print("=" * 70)
    para cada s em e.specs:
        print(f"\n  --- {s.categoria.rotulo} ---")
        para cada p em s.produtos:
            flag <- {"conforme": "OK", "parcial": "PARC", "nao_conforme": "NAO",
                    "recomendado": "REC"}[p.status.id]
            print(f"    [{flag}] {p.marca} {p.modelo:<30} R$ {p.preco_aprox_brl:>6.0f}")

    // --- Por deficiencia ---
    print("\n" + "=" * 70)
    print("[PRODUTOS POR DEFICIENCIA]")
    print("=" * 70)
    para cada defic em DeficienciaAlvo:
        prods <- e.produtos_por_deficiencia(defic)
        se prods entao:
            nomes <- [f"{p.marca} {p.modelo}" for p, _ in prods[:4]]
            print(f"\n  {defic.rotulo} ({len(prods)} produtos):")
            para cada n em nomes:
                print(f"    - {n}")

    // --- Catalogo por faixa de custo ---
    print("\n" + "=" * 70)
    print("[CATALOGO POR FAIXA DE CUSTO]")
    print("=" * 70)
    cat <- e.catalogo_por_faixa_custo()
    para cada (faixa, prods) em cat.items():
        print(f"\n  {faixa} ({len(prods)} produtos):")
        para cada p em prods[:3]:
            print(f"    - {p.marca} {p.modelo} (R$ {p.preco_aprox_brl:.0f})")

    // --- Scorecard ---
    print("\n" + "=" * 70)
    print("[SCORECARD]")
    print("=" * 70)
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<30} {v}")

    // --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Dispositivos que nao precisam ser feitos do zero")
    print("=" * 70)
    print("""
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
  Produto na lista <- atende spec minima. Produto fora da lista = NAO comprar.
  A Republica NAO ganha comissao. NAO tem 'parceiro preferido'.
  Tem CRITERIO TECNICO. Objetivo. Auditavel.

O PRINCIPIO:
  Todo cidadao tem direito ao hardware que permite acessar o mundo.
  Cego precisa de leitor de tela + headphone. Surdo precisa de Libras + webcam.
  Tetraplegico precisa de eye tracker + switch. Dislexico precisa de e-reader.
  A Republica garante NAO o hardware (isso e COTS), mas a SPEC que faz
  o hardware SER acessivel. Sem spec, o mercado fabrica o que quer.
  Com spec, o mercado fabrica o que PRECISA.
// )


se __name__ == "__main__" entao:
    _demo()

```
