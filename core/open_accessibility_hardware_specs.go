// OpenAccessibilityHardwareSpecs -- Hardware COTS para Acessibilidade
// 12 dispositivos. Specs minimas. Lista de equipamentos suportados.
// Author: OpenRepublic Team
package main

import (
    "fmt"
    "strings"
)

// ============================================================================
// 1. TIPOS
// ============================================================================

const (
    CatHeadphone_bt = "headphone_bt"  // Headphone Bluetooth
    CatSmartphone = "smartphone"  // Smartphone
    CatSmartwatch = "smartwatch"  // Smartwatch
    CatEye_tracker = "eye_tracker"  // Eye Tracker
    CatBraille_display = "braille_display"  // Display Braille
    CatSwitch = "switch"  // Switch Button (botao de acesso)
    CatBone_conduction = "bone_conduction"  // Fone de Conducao Ossea
    CatMicrofone = "microfone"  // Microfone
    CatWebcam = "webcam"  // Webcam
    CatTablet = "tablet"  // Tablet (CAA)
    CatE_reader = "e_reader"  // E-reader (Leitor Digital)
    CatGps_tracker = "gps_tracker"  // GPS Tracker (Pessoal)
)

var catRotulo = map[string]string{
    "headphone_bt": "Headphone Bluetooth",
    "smartphone": "Smartphone",
    "smartwatch": "Smartwatch",
    "eye_tracker": "Eye Tracker",
    "braille_display": "Display Braille",
    "switch": "Switch Button (botao de acesso)",
    "bone_conduction": "Fone de Conducao Ossea",
    "microfone": "Microfone",
    "webcam": "Webcam",
    "tablet": "Tablet (CAA)",
    "e_reader": "E-reader (Leitor Digital)",
    "gps_tracker": "GPS Tracker (Pessoal)",
}

const (
    StatusConforme = "conforme"
    StatusParcial = "parcial"
    StatusNao_conforme = "nao_conforme"
    StatusRecomendado = "recomendado"
)

// ============================================================================
// 2. STRUCTS
// ============================================================================

type Especificacao struct {
    Parametro    string
    ValorMinimo  string
    Obrigatorio  bool
    Justificativa string
}

type ProdutoCOTS struct {
    Marca     string
    Modelo    string
    CatID     string
    PrecoBRL  float64
    StatusID  string
    Fortes    []string
    Fracos    []string
}

type SpecDispositivo struct {
    CatID         string
    CatRotulo     string
    Descricao     string
    Deficiencias  []string
    CustoMinimo   float64
    Specs         []Especificacao
    Produtos      []ProdutoCOTS
    Observacao    string
}

// ============================================================================
// 3. DADOS: AS 12 ESPECIFICACOES
// ============================================================================

var todasSpecs = []SpecDispositivo{
    {
        CatID: "headphone_bt",
        CatRotulo: "Headphone Bluetooth",
        Descricao: "Headphone Bluetooth para acessibilidade auditiva. Usado para TTS (text-to-speech), audio descricao, legendas em audio, a...",
        Deficiencias: []string{"Surdo / Deficiente auditivo", "Cego / Baixa visao", "Uso universal (todas as deficiencias)", "Idoso (demencia / mobilidade reduzida)"},
        CustoMinimo: 80.0,
        Specs: []Especificacao{
            {Parametro: "Bluetooth", ValorMinimo: "5.0 ou superior (LE Audio / aptX Adaptive)", Obrigatorio: true, Justificativa: "LE Audio reduz latencia e permite multi-stream (2 fones no mesmo dispositivo)...."},
            {Parametro: "Latencia", ValorMinimo: "< 200ms (ideal < 150ms)", Obrigatorio: true, Justificativa: "Latencia alta quebra TTS em tempo real e audio descricao sincronizada...."},
            {Parametro: "Bateria", ValorMinimo: "Minimo 8h uso continuo", Obrigatorio: true, Justificativa: "Dia de trabalho/estudo sem recarregar. Cego depende do fone o dia todo...."},
            {Parametro: "Microfone integrado", ValorMinimo: "Sim, com cancelamento de ruido", Obrigatorio: true, Justificativa: "Para comando de voz, chamadas, e Libras por contexto de audio...."},
            {Parametro: "Perfil Bluetooth", ValorMinimo: "A2DP + HFP + AVRCP", Obrigatorio: true, Justificativa: "A2DP = audio de qualidade. HFP = viva-voz. AVRCP = controle remoto...."},
            {Parametro: "Multiponto", ValorMinimo: "Sim (conectar 2 dispositivos simultaneamente)", Obrigatorio: true, Justificativa: "Cego pode estar conectado ao smartphone E ao computador ao mesmo tempo...."},
            {Parametro: "Controles fisicos", ValorMinimo: "Botoes reais (nao touch)", Obrigatorio: true, Justificativa: "Cego nao pode usar controles capacitivos sem feedback visual...."},
            {Parametro: "Feedback de bateria", ValorMinimo: "Anuncio de bateria por voz ou tom", Obrigatorio: true, Justificativa: "Cego precisa saber quando vai acabar sem ver o LED...."},
            {Parametro: "Conforto", ValorMinimo: "Ajustavel, leve (< 300g), alcolchoado", Obrigatorio: true, Justificativa: "Uso prolongado (8h+) requer conforto. Pessoas com sensibilidade sensorial (TEA) ..."},
            {Parametro: "Codec", ValorMinimo: "SBC minimo. AAC/SBC/LDAC desejavel", Obrigatorio: false, Justificativa: "AAC melhora qualidade para usuarios de iPhone...."},
            {Parametro: "Resistencia", ValorMinimo: "IPX4 (suor e chuva)", Obrigatorio: false, Justificativa: "Para uso em mobilidade urbana...."},
            {Parametro: "Jack 3.5mm", ValorMinimo: "Sim (backup com fio)", Obrigatorio: true, Justificativa: "Se Bluetooth falha, fio e backup. Cego nao pode ficar sem audio...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "JBL", Modelo: "Tune 510BT", CatID: "headphone_bt", PrecoBRL: 250, StatusID: "conforme", Fortes: []string{"Bateria 40h", "Multiponto", "Custo acessivel"}, Fracos: []string{"Sem anuncio de bateria por voz", "Controle touch (parcial)"}},
            {Marca: "Sony", Modelo: "WH-CH520", CatID: "headphone_bt", PrecoBRL: 350, StatusID: "recomendado", Fortes: []string{"Bateria 50h", "Multiponto", "Anuncio de bateria por voz"}, Fracos: []string{"Sem jack 3.5mm (USB-C apenas)"}},
            {Marca: "Sennheiser", Modelo: "HD 350BT", CatID: "headphone_bt", PrecoBRL: 500, StatusID: "recomendado", Fortes: []string{"Bateria 30h", "AAC + aptX", "Confortavel 8h+"}, Fracos: []string{"Sem jack 3.5mm"}},
            {Marca: "Anker", Modelo: "Soundcore Life Q20", CatID: "headphone_bt", PrecoBRL: 250, StatusID: "conforme", Fortes: []string{"Bateria 40h", "ANC basico", "Custo baixo"}, Fracos: []string{"Multiponto instavel", "App requer visual"}},
            {Marca: "Philips", Modelo: "SHL3070BK", CatID: "headphone_bt", PrecoBRL: 150, StatusID: "parcial", Fortes: []string{"Custo muito baixo", "Jack 3.5mm"}, Fracos: []string{"Bateria 9h (minimo)", "Sem multiponto", "Latencia alta para TTS"}},
            {Marca: "Apple", Modelo: "AirPods (2nd gen)", CatID: "headphone_bt", PrecoBRL: 1500, StatusID: "recomendado", Fortes: []string{"Acessibilidade iOS nativa", "Live Listen (microfone remoto)", "Audio descricao integrada"}, Fracos: []string{"Custo alto", "Sem controles fisicos (touch)", "Bateria ~5h por carga (24h com case)"}},
            {Marca: "Apple", Modelo: "AirPods Pro 2", CatID: "headphone_bt", PrecoBRL: 2500, StatusID: "recomendado", Fortes: []string{"Live Listen", "ANC adaptativo", "Modo Conversacao (transparencia)"}, Fracos: []string{"Custo premium", "Sem jack 3.5mm"}},
            {Marca: "Samsung", Modelo: "Galaxy Buds FE", CatID: "headphone_bt", PrecoBRL: 600, StatusID: "conforme", Fortes: []string{"Live Listen no Android", "ANC", "Custo medio"}, Fracos: []string{"Bateria ~6h por carga", "Sem jack"}},
        },
        Observacao: "O Headphone Bluetooth e o DISPOSITIVO MAIS UNIVERSAL da acessibilidade. Cego usa...",
    },
    {
        CatID: "smartphone",
        CatRotulo: "Smartphone",
        Descricao: "Smartphone como CORPO ESTENDIDO (Telefonista). Camera=olhos, microfone=ouvidos, GPS=direcao, acelerometro=balance, smart...",
        Deficiencias: []string{"Cego / Baixa visao", "Surdo / Deficiente auditivo", "Motora / Tetraplegia / Paralisia cerebral", "TEA / Autismo"},
        CustoMinimo: 800.0,
        Specs: []Especificacao{
            {Parametro: "Sistema operacional", ValorMinimo: "Android 13+ ou iOS 16+", Obrigatorio: true, Justificativa: "Versoes antigas nao tem features de acessibilidade criticas...."},
            {Parametro: "RAM", ValorMinimo: "Minimo 4GB (ideal 6GB+)", Obrigatorio: true, Justificativa: "Apps de acessibilidade (TalkBack, VoiceOver, Libras) consomem RAM...."},
            {Parametro: "Armazenamento", ValorMinimo: "Minimo 64GB", Obrigatorio: true, Justificativa: "Modelos de IA local + apps de CAA + mapas offline precisam de espaco...."},
            {Parametro: "Camera", ValorMinimo: "Minimo 12MP com autofocus + OIS", Obrigatorio: true, Justificativa: "Visao computacional (OCR, descricao de cena, Libras) precisa de camera decente...."},
            {Parametro: "Bateria", ValorMinimo: "Minimo 4000mAh", Obrigatorio: true, Justificativa: "Dia inteiro de uso com acessibilidade ativa (TTS + GPS + camera)...."},
            {Parametro: "TalkBack/VoiceOver", ValorMinimo: "Nativo e funcional", Obrigatorio: true, Justificativa: "Leitor de tela nativo e OBRIGATORIO. Sem ele, cego nao usa o telefone...."},
            {Parametro: "Bluetooth", ValorMinimo: "5.0+", Obrigatorio: true, Justificativa: "Para conectar headphones, hearing aids, braille displays...."},
            {Parametro: "GPS", ValorMinimo: "Sim, com A-GPS", Obrigatorio: true, Justificativa: "Navegacao para cego, rastreamento de crianca/idoso...."},
            {Parametro: "NFC", ValorMinimo: "Sim", Obrigatorio: false, Justificativa: "Pagamento sem QR code (OpenAntiQRPayment)...."},
            {Parametro: "Acelerometro/Giroscopio", ValorMinimo: "Sim", Obrigatorio: true, Justificativa: "Deteccao de queda (idoso), bussola para navegacao (cego)...."},
            {Parametro: "Slot microSD", ValorMinimo: "Desejavel", Obrigatorio: false, Justificativa: "Armazenamento expansivel para mapas offline e modelos de IA...."},
            {Parametro: "Radio FM", ValorMinimo: "Desejavel (com fone como antena)", Obrigatorio: false, Justificativa: "Emergencias: FM nao depende de internet...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Samsung", Modelo: "Galaxy A15 5G", CatID: "smartphone", PrecoBRL: 1000, StatusID: "recomendado", Fortes: []string{"Custo baixo", "Android 14", "Bateria 5000mAh"}, Fracos: []string{"RAM 4GB (minimo)", "Sem OIS na camera"}},
            {Marca: "Samsung", Modelo: "Galaxy A55 5G", CatID: "smartphone", PrecoBRL: 2000, StatusID: "recomendado", Fortes: []string{"RAM 8GB", "Camera com OIS", "Bateria 5000mAh"}, Fracos: []string{"Sem slot microSD (alguns mercados)"}},
            {Marca: "Motorola", Modelo: "Moto G84 5G", CatID: "smartphone", PrecoBRL: 1300, StatusID: "recomendado", Fortes: []string{"RAM 8GB (otimo nesta faixa)", "Bateria 5000mAh", "Android limpo (TalkBack funciona bem)"}, Fracos: []string{"Camera sem OIS"}},
            {Marca: "Apple", Modelo: "iPhone SE (2022)", CatID: "smartphone", PrecoBRL: 3000, StatusID: "recomendado", Fortes: []string{"VoiceOver (melhor leitor de tela do mercado)", "Detecao de pessoas, portas, sons (Magnifier)", "Audio descricao"}, Fracos: []string{"Bateria 2018mAh (fraca)", "Tela 4.7 polegadas (pequena)"}},
            {Marca: "Apple", Modelo: "iPhone 15", CatID: "smartphone", PrecoBRL: 5000, StatusID: "recomendado", Fortes: []string{"VoiceOver + Magnifier + Detecao de sons", "LiDAR (navegacao para cego)", "Camera 48MP"}, Fracos: []string{"Custo premium"}},
            {Marca: "Xiaomi", Modelo: "Redmi Note 13", CatID: "smartphone", PrecoBRL: 1100, StatusID: "conforme", Fortes: []string{"Custo baixo", "Bateria 5000mAh", "Camera 108MP"}, Fracos: []string{"MIUI tem bugs de acessibilidade", "TalkBack menos testado"}},
        },
        Observacao: "O smartphone e o CORACAO da acessibilidade da Republica. E camera, microfone, GP...",
    },
    {
        CatID: "smartwatch",
        CatRotulo: "Smartwatch",
        Descricao: "Smartwatch para biometria continua: estresse (frequencia cardiaca), predicao de convulsao (temperatura + HR), deteccao d...",
        Deficiencias: []string{"Neurologica (ELA / Parkinson / Epilepsia)", "Idoso (demencia / mobilidade reduzida)", "TDAH / Dislexia", "TEA / Autismo"},
        CustoMinimo: 400.0,
        Specs: []Especificacao{
            {Parametro: "Sensor cardiaco", ValorMinimo: "Sim (PPG ou ECG)", Obrigatorio: true, Justificativa: "Deteccao de estresse, arritmia, taquicardia...."},
            {Parametro: "Acelerometro", ValorMinimo: "Sim (3 eixos)", Obrigatorio: true, Justificativa: "Deteccao de queda (idoso), tremor (Parkinson)...."},
            {Parametro: "GPS", ValorMinimo: "Sim (integrado)", Obrigatorio: true, Justificativa: "Rastreamento de crianca/idoso sem depender do smartphone...."},
            {Parametro: "Bateria", ValorMinimo: "Minimo 3 dias (ideal 7+)", Obrigatorio: true, Justificativa: "Biometria continua requer uso 24h. Recarga diaria e falha...."},
            {Parametro: "Resistencia", ValorMinimo: "IP68 (agua e poeira)", Obrigatorio: true, Justificativa: "Usa no banho, na chuva, na piscina. Biometria nao para...."},
            {Parametro: "Vibracao", ValorMinimo: "Motor haptico forte", Obrigatorio: true, Justificativa: "Surdo nao ouve alerta. Cego nao ve. Vibration e universal...."},
            {Parametro: "Tela sempre ligada", ValorMinimo: "Desejavel", Obrigatorio: false, Justificativa: "Idoso precisa ver as horas sem tocar na tela...."},
            {Parametro: "Temperatura corporea", ValorMinimo: "Desejavel", Obrigatorio: false, Justificativa: "Predicao de convulsao epileptica (pesquisa Apple Watch)...."},
            {Parametro: "SpO2 (oximetria)", ValorMinimo: "Desejavel", Obrigatorio: false, Justificativa: "Monitoramento respiratorio...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Amazfit", Modelo: "Bip 5", CatID: "smartwatch", PrecoBRL: 500, StatusID: "recomendado", Fortes: []string{"Bateria 10 DIAS", "GPS", "Tela grande (1.69 polegadas)"}, Fracos: []string{"Sem ECG", "Sem SpO2 confiavel"}},
            {Marca: "Xiaomi", Modelo: "Smart Band 8", CatID: "smartwatch", PrecoBRL: 250, StatusID: "conforme", Fortes: []string{"Bateria 16 DIAS", "Custo muito baixo", "HR + SpO2"}, Fracos: []string{"Sem GPS integrado (depende do telefone)", "Tela pequena para idoso com baixa visao"}},
            {Marca: "Apple", Modelo: "Apple Watch SE (2nd gen)", CatID: "smartwatch", PrecoBRL: 2500, StatusID: "recomendado", Fortes: []string{"Deteccao de queda (SOS automatico)", "ECG (aprovado FDA)", "GPS integrado"}, Fracos: []string{"Bateria ~18h (1 dia)", "Custo alto"}},
            {Marca: "Apple", Modelo: "Apple Watch Series 9", CatID: "smartwatch", PrecoBRL: 4500, StatusID: "recomendado", Fortes: []string{"ECG + SpO2 + Temperatura", "Deteccao de queda + SOS", "GPS"}, Fracos: []string{"Bateria ~18h", "Custo premium"}},
            {Marca: "Samsung", Modelo: "Galaxy Watch FE", CatID: "smartwatch", PrecoBRL: 1000, StatusID: "conforme", Fortes: []string{"ECG (em alguns paises)", "Bateria 2-3 dias", "Deteccao de queda"}, Fracos: []string{"ECG bloqueado em alguns mercados"}},
            {Marca: "Garmin", Modelo: "Forerunner 55", CatID: "smartwatch", PrecoBRL: 1500, StatusID: "conforme", Fortes: []string{"Bateria 14 DIAS em modo watch", "GPS de precisao", "Vibracao forte"}, Fracos: []string{"Foco em esporte (menos features de saude)"}},
        },
        Observacao: "Smartwatch = biometria PASSIVA. O usuario nao precisa fazer nada. O relogio dete...",
    },
    {
        CatID: "eye_tracker",
        CatRotulo: "Eye Tracker",
        Descricao: "Eye tracker para tetraplegia, ELA, paralisia cerebral. O olho e o ultimo musculo voluntario em ELA. Eye tracker permite ...",
        Deficiencias: []string{"Motora / Tetraplegia / Paralisia cerebral", "Neurologica (ELA / Parkinson / Epilepsia)", "Comunicacao (nao-verbal / afasia)"},
        CustoMinimo: 2000.0,
        Specs: []Especificacao{
            {Parametro: "Precisao", ValorMinimo: "< 1 grau visual (ideal < 0.5)", Obrigatorio: true, Justificativa: "Para clicar em botoes pequenos na tela. Precisao baixa = frustracao...."},
            {Parametro: "Frequencia", ValorMinimo: "Minimo 60Hz (ideal 120Hz+)", Obrigatorio: true, Justificativa: "Taxa de atualizacao. Baixa = lag entre olhar e clique...."},
            {Parametro: "Calibracao", ValorMinimo: "Automatica ou 1-5 pontos", Obrigatorio: true, Justificativa: "Calibracao complexa (16 pontos) e exaustiva para quem tem mobilidade limitada...."},
            {Parametro: "Compatibilidade", ValorMinimo: "Windows + macOS + Linux", Obrigatorio: true, Justificativa: "Nao pode prender o usuario num SO...."},
            {Parametro: "Software inclusivo", ValorMinimo: "Teclado virtual + CAA", Obrigatorio: true, Justificativa: "Eye tracker sem software de comunicacao e so hardware inutil...."},
            {Parametro: "Latencia", ValorMinimo: "< 50ms", Obrigatorio: true, Justificativa: "Entre o olhar e o cursor responder. Alto = nauseas...."},
            {Parametro: "Trabalha com oculos", ValorMinimo: "Sim", Obrigatorio: true, Justificativa: "Muitos usuarios de eye tracker usam oculos...."},
            {Parametro: "Headbox", ValorMinimo: "Minimo 25x25cm", Obrigatorio: true, Justificativa: "Area de liberdade de movimento da cabeca. Pequeno = usuario precisa ficar imovel..."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Tobii", Modelo: "Eye Tracker 5", CatID: "eye_tracker", PrecoBRL: 3500, StatusID: "recomendado", Fortes: []string{"Precisao < 0.5 grau", "144Hz", "Headbox amplo"}, Fracos: []string{"Custo alto", "Windows-centric (Linux parcial)"}},
            {Marca: "Tobii", Modelo: "Dynavox", CatID: "eye_tracker", PrecoBRL: 15000, StatusID: "recomendado", Fortes: []string{"Solucao completa (tablet + eye tracker + CAA)", "Snap Core First (CAA)", "Suporte clinico"}, Fracos: []string{"Custo ESPECIALIZADO", "Fornecedor unico"}},
            {Marca: "IRISBOND", Modelo: "Hiru", CatID: "eye_tracker", PrecoBRL: 5000, StatusID: "conforme", Fortes: []string{"Precisao < 0.5 grau", "Multiplataforma", "Usado em hospitais brasileiros"}, Fracos: []string{"Disponibilidade limitada no Brasil"}},
            {Marca: "Windows", Modelo: "Eye Control (nativo)", CatID: "eye_tracker", PrecoBRL: 0, StatusID: "conforme", Fortes: []string{"GRATUITO no Windows 10/11", "Funciona com Tobii 4C e EyeX"}, Fracos: []string{"So funciona com hardware Tobii", "Limitado a Windows"}},
            {Marca: "Apple", Modelo: "iPad com AssistiveTouch (olhos)", CatID: "eye_tracker", PrecoBRL: 5000, StatusID: "recomendado", Fortes: []string{"Eye Tracking nativo no iPadOS (2024+)", "GRATUITO (incluido no iPad)", "CAA integrada"}, Fracos: []string{"So funciona em iPad Pro/Air recentes", "Precisao pode variar"}},
        },
        Observacao: "Eye tracker e o DISPOSITIVO QUE DEVOLVE A VOZ. Pessoa com ELA perde tudo -- braç...",
    },
    {
        CatID: "braille_display",
        CatRotulo: "Display Braille",
        Descricao: "Display Braille para cegos. Converte texto digital em celas braille táteis. E o OUTPUT equivalente ao leitor de tela -- ...",
        Deficiencias: []string{"Cego / Baixa visao"},
        CustoMinimo: 3000.0,
        Specs: []Especificacao{
            {Parametro: "Celas", ValorMinimo: "Minimo 8 celas (ideal 40+)", Obrigatorio: true, Justificativa: "8 celas = palavra por vez. 40+ = linha inteira. Mais celas = leitura fluida...."},
            {Parametro: "Tipo de cela", ValorMinimo: "Piezoeletrica (8 pinos por cela)", Obrigatorio: true, Justificativa: "Braille de 8 pontos (computador). 6 pontos so perde informacao de formatacao...."},
            {Parametro: "Conexao", ValorMinimo: "Bluetooth + USB", Obrigatorio: true, Justificativa: "Bluetooth para smartphone. USB para computador. Ambos necessarios...."},
            {Parametro: "Bateria", ValorMinimo: "Minimo 10h", Obrigatorio: true, Justificativa: "Dia de trabalho/estudo. Recarga no meio do dia e falha...."},
            {Parametro: "Botoes de navegacao", ValorMinimo: "Sim (pan, rota, cursor routing)", Obrigatorio: true, Justificativa: "Navegar pelo texto sem depender do smartphone...."},
            {Parametro: "Compatibilidade", ValorMinimo: "TalkBack (Android) + VoiceOver (iOS) + NVDA/JAWS (PC)", Obrigatorio: true, Justificativa: "Display Braille sem leitor de tela e so pinos. Precisa do SOFTWARE...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Orbit Research", Modelo: "Orbit Reader 20 Plus", CatID: "braille_display", PrecoBRL: 4000, StatusID: "recomendado", Fortes: []string{"20 celas (bom para custo)", "BLUETOOTH + USB", "Bateria 20h"}, Fracos: []string{"20 celas limita leitura longa", "Sem teclado Perkins integrado"}},
            {Marca: "Help Tech", Modelo: "Active Star 40", CatID: "braille_display", PrecoBRL: 12000, StatusID: "recomendado", Fortes: []string{"40 celas (leitura fluida)", "Bluetooth + USB", "Teclado Perkins integrado"}, Fracos: []string{"Custo ESPECIALIZADO"}},
            {Marca: "Freedom Scientific", Modelo: "Focus 40 Blue", CatID: "braille_display", PrecoBRL: 10000, StatusID: "recomendado", Fortes: []string{"40 celas", "Bluetooth + USB", "Compativel com JAWS + NVDA + VoiceOver + TalkBack"}, Fracos: []string{"Custo ESPECIALIZADO"}},
            {Marca: "Seika", Modelo: "Seika 40", CatID: "braille_display", PrecoBRL: 6000, StatusID: "conforme", Fortes: []string{"40 celas", "Custo mais baixo para 40 celas", "Bluetooth + USB"}, Fracos: []string{"Qualidade de build inferior", "Suporte limitado no Brasil"}},
            {Marca: "Apple", Modelo: "iPhone/iPad com Braille (software)", CatID: "braille_display", PrecoBRL: 0, StatusID: "parcial", Fortes: []string{"GRATUITO no iOS", "Mostra Braille na tela (para videntes aprenderem)", "Conecta com display fisico via Bluetooth"}, Fracos: []string{"Nao e Braille TATIL (so visual)", "Para cego real, precisa do display fisico"}},
        },
        Observacao: "Display Braille e o UNICO OUTPUT para SURDO-CEGO. Surdo-cego nao tem audio (surd...",
    },
    {
        CatID: "switch",
        CatRotulo: "Switch Button (botao de acesso)",
        Descricao: "Switch button: botao grande de 1 toque para acesso. Para tetraplegia severa, paralisia cerebral, ELA avancada. 1 toque =...",
        Deficiencias: []string{"Motora / Tetraplegia / Paralisia cerebral", "Neurologica (ELA / Parkinson / Epilepsia)", "Comunicacao (nao-verbal / afasia)"},
        CustoMinimo: 100.0,
        Specs: []Especificacao{
            {Parametro: "Forca de ativacao", ValorMinimo: "Maximo 100g (ideal < 50g)", Obrigatorio: true, Justificativa: "Usuario com paralisia cerebral pode nao conseguir apertar botao duro...."},
            {Parametro: "Tamanho da superficie", ValorMinimo: "Minimo 5cm diametro", Obrigatorio: true, Justificativa: "Alvo grande para quem tem tremor ou movimento involuntario...."},
            {Parametro: "Feedback", ValorMinimo: "Tatil (click) + auditivo (click) + visual (LED)", Obrigatorio: true, Justificativa: "O usuario PRECISA saber que ativou. Multi-modal...."},
            {Parametro: "Conexao", ValorMinimo: "Bluetooth e/ou Jack 3.5mm", Obrigatorio: true, Justificativa: "Jack 3.5mm = compatibilidade universal (AT, switch-adapted toys). BT = sem fio...."},
            {Parametro: "Resistencia", ValorMinimo: "A prova de impacto e saliva", Obrigatorio: true, Justificativa: "Usuario pode ter espasmo. Crianca pode morder/bater...."},
            {Parametro: "Montagem", ValorMinimo: "Compativel com braços articulados e suportes", Obrigatorio: true, Justificativa: "Switch precisa ser posicionado onde o usuario tem movimento...."},
            {Parametro: "Bateria", ValorMinimo: "Minimo 100h (ideal: meses)", Obrigatorio: true, Justificativa: "Switch com fio nao precisa. Switch BT precisa durar semanas...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Ablenet", Modelo: "Big Red Switch", CatID: "switch", PrecoBRL: 400, StatusID: "recomendado", Fortes: []string{"Padrao da industria de AT", "Superficie 12.7cm", "Forca ~57g"}, Fracos: []string{"Custo alto para um botao"}},
            {Marca: "Ablenet", Modelo: "Spec Switch", CatID: "switch", PrecoBRL: 350, StatusID: "recomendado", Fortes: []string{"Superficie 5cm", "Forca muito baixa (~21g)", "Ideal para ELA avancada"}, Fracos: []string{"Custo alto"}},
            {Marca: "Enabling Devices", Modelo: "Jelly Bean Switch", CatID: "switch", PrecoBRL: 300, StatusID: "conforme", Fortes: []string{"Superficie 6.5cm", "Cores vivas (baixa visao)", "Jack 3.5mm"}, Fracos: []string{"Feedback menos firme que Ablenet"}},
            {Marca: "DIY", Modelo: "Switch caseiro (pizza box + foil)", CatID: "switch", PrecoBRL: 20, StatusID: "parcial", Fortes: []string{"Custo MUITO baixo", "Customizavel", "Tutorial aberto (CC0)"}, Fracos: []string{"Durabilidade baixa", "Precisa manutencao frequente", "Sem feedback de qualidade"}},
            {Marca: "Logitech", Modelo: "Adaptive Gaming Kit", CatID: "switch", PrecoBRL: 600, StatusID: "recomendado", Fortes: []string{"3 switches grandes + 5 pequenos", "Abas de etiqueta (identificacao tatil)", "Custo razoavel para kit completo"}, Fracos: []string{"Foco em gaming (adaptavel para AT)"}},
        },
        Observacao: "Switch e o DISPOSITIVO MAIS SIMPLES E MAIS PODEROSO. 1 botao. 1 acao. Para quem ...",
    },
    {
        CatID: "bone_conduction",
        CatRotulo: "Fone de Conducao Ossea",
        Descricao: "Fone de conducao ossea: som viaja pelo osso (cranio) ate o nervo auditivo, bypassando o ouvido externo e medio. Para sur...",
        Deficiencias: []string{"Surdo / Deficiente auditivo"},
        CustoMinimo: 500.0,
        Specs: []Especificacao{
            {Parametro: "Bluetooth", ValorMinimo: "5.0+", Obrigatorio: true, Justificativa: "Conexao estavel para TTS e audio descricao...."},
            {Parametro: "Orelha aberta", ValorMinimo: "Sim (nao bloqueia canal auditivo)", Obrigatorio: true, Justificativa: "Cego que usa conducao ossea PRECISA ouvir o ambiente tambem...."},
            {Parametro: "Bateria", ValorMinimo: "Minimo 6h", Obrigatorio: true, Justificativa: "Dia de uso continuo...."},
            {Parametro: "Microfone", ValorMinimo: "Sim", Obrigatorio: true, Justificativa: "Para comando de voz e chamadas...."},
            {Parametro: "Conforto", ValorMinimo: "Ajustavel, leve (< 40g)", Obrigatorio: true, Justificativa: "Repouso na teca (osso temporal). Pressao inadequada = dor...."},
            {Parametro: "Resistencia", ValorMinimo: "IPX4+ (suor)", Obrigatorio: true, Justificativa: "Uso em atividade fisica e mobilidade urbana...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Shokz", Modelo: "OpenRun Pro", CatID: "bone_conduction", PrecoBRL: 1200, StatusID: "recomendado", Fortes: []string{"Lider em conducao ossea", "Bateria 10h", "Bluetooth 5.1"}, Fracos: []string{"Custo alto"}},
            {Marca: "Shokz", Modelo: "OpenMove", CatID: "bone_conduction", PrecoBRL: 600, StatusID: "recomendado", Fortes: []string{"Custo medio", "Bateria 6h", "Bluetooth 5.1"}, Fracos: []string{"Qualidade de som inferior ao OpenRun Pro"}},
            {Marca: "Mojawa", Modelo: "Run Plus", CatID: "bone_conduction", PrecoBRL: 1000, StatusID: "conforme", Fortes: []string{"Bateria 8h", "IP68", "MP3 integrado (16GB)"}, Fracos: []string{"Marca menos estabelecida"}},
        },
        Observacao: "Conducao ossea e PARA SURDO CONDUTIVO especificamente. Surdo neurosensorial seve...",
    },
    {
        CatID: "microfone",
        CatRotulo: "Microfone",
        Descricao: "Microfone para comando de voz, fala-para-texto, e captura de audio ambiente para o Telefonista. Para tetraplegico que so...",
        Deficiencias: []string{"Motora / Tetraplegia / Paralisia cerebral", "Surdo / Deficiente auditivo", "Cego / Baixa visao", "Comunicacao (nao-verbal / afasia)"},
        CustoMinimo: 50.0,
        Specs: []Especificacao{
            {Parametro: "Cancelamento de ruido", ValorMinimo: "Sim (DSP ou cardiode)", Obrigatorio: true, Justificativa: "Comando de voz em ambiente ruidoso precisa de CNR...."},
            {Parametro: "Conexao", ValorMinimo: "USB ou Bluetooth", Obrigatorio: true, Justificativa: "USB = zero latencia. BT = mobilidade...."},
            {Parametro: "Padrao polar", ValorMinimo: "Cardiode ou unidirecional", Obrigatorio: true, Justificativa: "Captura a voz do usuario, nao o ambiente inteiro...."},
            {Parametro: "Frequencia", ValorMinimo: "100Hz-10kHz minimo", Obrigatorio: true, Justificativa: "Cobre voz humana. Baixa frequencia = graves (homem). Alta = agudos (mulher/crian..."},
            {Parametro: "Mute fisico", ValorMinimo: "Botao de mute REAL (nao software)", Obrigatorio: true, Justificativa: "Privacidade: usuario PRECISA saber que o microfone esta mudo...."},
            {Parametro: "LED indicador", ValorMinimo: "Sim (LED mostra se esta captando)", Obrigatorio: true, Justificativa: "Surdo nao ouve o proprio audio. Precisa VER que o microfone esta ativo...."},
            {Parametro: "Filtro pop", ValorMinimo: "Sim (espuma ou malha)", Obrigatorio: false, Justificativa: "Reduz 'p' e 't' que estouram o reconhecimento de voz...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Blue", Modelo: "Yeti Nano", CatID: "microfone", PrecoBRL: 500, StatusID: "recomendado", Fortes: []string{"USB-C", "Cardiode + omnidirecional", "Mute fisico (botao na frente)"}, Fracos: []string{"Grande (ocupa espaco na mesa)"}},
            {Marca: "Fifine", Modelo: "K669B", CatID: "microfone", PrecoBRL: 150, StatusID: "recomendado", Fortes: []string{"Custo MUITO baixo", "USB", "Cardiode"}, Fracos: []string{"Sem mute fisico", "Qualidade decente mas nao premium"}},
            {Marca: "Jabra", Modelo: "Speak 510", CatID: "microfone", PrecoBRL: 700, StatusID: "recomendado", Fortes: []string{"Bluetooth + USB", "CNR excelente", "Speakerphone (para reuniao com legenda)"}, Fracos: []string{"Custo medio-alto"}},
            {Marca: "In_build", Modelo: "Microfone do smartphone", CatID: "microfone", PrecoBRL: 0, StatusID: "parcial", Fortes: []string{"GRATUITO", "Sempre presente", "Portatil"}, Fracos: []string{"Qualidade varia", "CNR limitado", "Nao ideal para texto longo"}},
        },
        Observacao: "Microfone e a ENTRADA para quem SO FALA. Tetraplegico que nao digita, FALA. Prec...",
    },
    {
        CatID: "webcam",
        CatRotulo: "Webcam",
        Descricao: "Webcam para Libras (surdo se comunica por sinais na camera), visao computacional (descricao de cena para cego), e rastre...",
        Deficiencias: []string{"Surdo / Deficiente auditivo", "Cego / Baixa visao"},
        CustoMinimo: 150.0,
        Specs: []Especificacao{
            {Parametro: "Resolucao", ValorMinimo: "Minimo 720p (ideal 1080p)", Obrigatorio: true, Justificativa: "Libras requer resolucao suficiente para ver expressoes faciais e maos...."},
            {Parametro: "Frequencia", ValorMinimo: "Minimo 30fps (ideal 60fps)", Obrigatorio: true, Justificativa: "Libras e RAPIDO. 15fps perde sinais. 60fps captura tudo...."},
            {Parametro: "Autofocus", ValorMinimo: "Sim (rapido)", Obrigatorio: true, Justificativa: "Surdo que se move ao sinais nao pode ficar borrado...."},
            {Parametro: "Campo de visao", ValorMinimo: "Minimo 70 graus (ideal 90+)", Obrigatorio: true, Justificativa: "Libras requer espaco para maos e bracos. Webcam estreita corta os sinais...."},
            {Parametro: "Baixa luz", ValorMinimo: "Funciona em < 50 lux", Obrigatorio: true, Justificativa: "Nem todos tem iluminacao de estudio. Sala de casa a noite...."},
            {Parametro: "Microfone integrado", ValorMinimo: "Desejavel (backup)", Obrigatorio: false, Justificativa: "Para videochamada com surdo (audio + Libras simultaneo)...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Logitech", Modelo: "C920 HD Pro", CatID: "webcam", PrecoBRL: 400, StatusID: "recomendado", Fortes: []string{"1080p 30fps", "Autofocus rapido", "Campo 78 graus"}, Fracos: []string{"Sem 60fps em 1080p"}},
            {Marca: "Logitech", Modelo: "C922 Pro", CatID: "webcam", PrecoBRL: 500, StatusID: "recomendado", Fortes: []string{"1080p 30fps / 720p 60fps", "Fundo substituivel", "Tripé incluido"}, Fracos: []string{"Custo medio-alto"}},
            {Marca: "Microsoft", Modelo: "LifeCam Studio", CatID: "webcam", PrecoBRL: 600, StatusID: "conforme", Fortes: []string{"1080p", "Campo 75 graus", "Alta qualidade de build"}, Fracos: []string{"Descontinuado pela Microsoft (suporte incerto)"}},
            {Marca: "In_build", Modelo: "Webcam do notebook/smartphone", CatID: "webcam", PrecoBRL: 0, StatusID: "parcial", Fortes: []string{"GRATUITO", "Sempre presente"}, Fracos: []string{"Qualidade varia muito", "Campo de visao estreito em notebooks", "Autofocus lento em cameras baratas"}},
        },
        Observacao: "Webcam e a JANELA para Libras. Surdo se comunica por SINAIS. Sinais precisam de ...",
    },
    {
        CatID: "tablet",
        CatRotulo: "Tablet (CAA)",
        Descricao: "Tablet para CAA (Comunicacao Aumentativa e Alternativa). Para nao-verbal (autismo nao-verbal, afasia, ELA). Toca figura/...",
        Deficiencias: []string{"Comunicacao (nao-verbal / afasia)", "TEA / Autismo", "Cognitiva / Sindrome de Down", "Neurologica (ELA / Parkinson / Epilepsia)"},
        CustoMinimo: 800.0,
        Specs: []Especificacao{
            {Parametro: "Tela", ValorMinimo: "Minimo 10 polegadas", Obrigatorio: true, Justificativa: "Espaco para grade de simbolos CAA (minimo 8x8)...."},
            {Parametro: "Touch", ValorMinimo: "Multitoque capacitivo (sensivel)", Obrigatorio: true, Justificativa: "Usuario com motora fina comprometida precisa de tela responsiva...."},
            {Parametro: "Bateria", ValorMinimo: "Minimo 8h", Obrigatorio: true, Justificativa: "Dia de uso (escola, trabalho, terapia)...."},
            {Parametro: "Sintetizador de voz", ValorMinimo: "Nativo + apps CAA", Obrigatorio: true, Justificativa: "Tablet sem TTS e so uma tela. Precisa FALAR...."},
            {Parametro: "Software CAA", ValorMinimo: "Compativel com: Avaz, Proloquo, TD Snap", Obrigatorio: true, Justificativa: "Apps de CAA sao OBRIGATORIOS. Tablet sem apps CAA nao serve...."},
            {Parametro: "Case protetor", ValorMinimo: "Case resistente a queda (military-grade)", Obrigatorio: true, Justificativa: "Crianca com autismo pode ter comportamento de quebrar. Tablet = R$ 1000+...."},
            {Parametro: "Suporte", ValorMinimo: "Compativel com suportes de mesa/mobiliario", Obrigatorio: true, Justificativa: "Cadeirante precisa do tablet montado na cadeira...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Apple", Modelo: "iPad (10th gen)", CatID: "tablet", PrecoBRL: 3000, StatusID: "recomendado", Fortes: []string{"Melhor ecossistema de CAA do mercado", "Proloquo2Go (padrao ouro CAA)", "Avaz"}, Fracos: []string{"Custo alto"}},
            {Marca: "Samsung", Modelo: "Galaxy Tab A9+", CatID: "tablet", PrecoBRL: 1000, StatusID: "recomendado", Fortes: []string{"Custo baixo para tablet", "Tela 11 polegadas", "Android (Avaz, TD Snap)"}, Fracos: []string{"Menos apps CAA que iOS", "Case protetor menos disponivel"}},
            {Marca: "Apple", Modelo: "iPad Pro 11", CatID: "tablet", PrecoBRL: 7000, StatusID: "recomendado", Fortes: []string{"Eye Tracking nativo (2024+)", "Proloquo2Go + Voice Control", "M-series chip (rapido)"}, Fracos: []string{"Custo PREMIUM"}},
            {Marca: "Amazon", Modelo: "Fire HD 10", CatID: "tablet", PrecoBRL: 600, StatusID: "parcial", Fortes: []string{"Custo MUITO baixo", "Tela 10.1 polegadas"}, Fracos: []string{"Sem Google Play nativo (apps CAA limitados)", "Sem Proloquo2Go (iOS only)", "Android fork (Fire OS)"}},
        },
        Observacao: "Tablet CAA e a VOZ de quem nao fala. Crianca autista nao-verbal toca 'QUERO AGUA...",
    },
    {
        CatID: "e_reader",
        CatRotulo: "E-reader (Leitor Digital)",
        Descricao: "E-reader (tela e-ink) para dislexia, baixa visao, daltonismo. Tela e-ink nao emite luz (nao cansa). Fonte pode ser ampli...",
        Deficiencias: []string{"TDAH / Dislexia", "Cego / Baixa visao", "TEA / Autismo", "Idoso (demencia / mobilidade reduzida)"},
        CustoMinimo: 300.0,
        Specs: []Especificacao{
            {Parametro: "Tela", ValorMinimo: "E-ink (nao LCD/LED)", Obrigatorio: true, Justificativa: "E-ink nao emite luz azul. Nao cansa. Dislexico e TDAH sao sensivel a luz...."},
            {Parametro: "Fonte ajustavel", ValorMinimo: "Sim (tamanho + familia + espacamento)", Obrigatorio: true, Justificativa: "OpenDyslexic, Atkinson Hyperlegible, espacamento entre linhas...."},
            {Parametro: "Tamanho de fonte", ValorMinimo: "Ate minimo 36pt", Obrigatorio: true, Justificativa: "Baixa visao precisa de fonte grande. E-reader permite sem limite fisico...."},
            {Parametro: "TTS", ValorMinimo: "Sim (text-to-speech integrado)", Obrigatorio: true, Justificativa: "Dislexico que cansa de ler pode OUVIR. Cego pode ouvir o livro todo...."},
            {Parametro: "Contraste", ValorMinimo: "Ajustavel (escuro sobre claro, claro sobre escuro)", Obrigatorio: true, Justificativa: "Modo escuro (fundo preto, texto branco) para baixa visao e sensibilidade a luz...."},
            {Parametro: "Suporte a formatos", ValorMinimo: "EPUB, PDF, TXT, HTML", Obrigatorio: true, Justificativa: "Nao pode prender o usuario num formato proprietario...."},
            {Parametro: "Bateria", ValorMinimo: "Minimo 4 semanas", Obrigatorio: true, Justificativa: "E-ink consome quase nada. Meses de uso sem recarregar...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Amazon", Modelo: "Kindle Paperwhite", CatID: "e_reader", PrecoBRL: 600, StatusID: "recomendado", Fortes: []string{"E-ink 300ppi", "Fonte ajustavel + OpenDyslexic", "TTS (VoiceView)"}, Fracos: []string{"Formato proprietario (AZW3)", "Suporte a EPUB limitado"}},
            {Marca: "Kobo", Modelo: "Clara 2E", CatID: "e_reader", PrecoBRL: 700, StatusID: "recomendado", Fortes: []string{"E-ink 300ppi", "Suporte nativo a EPUB", "OpenDyslexic nativo"}, Fracos: []string{"TTS limitado"}},
            {Marca: "Kobo", Modelo: "Libra H2O", CatID: "e_reader", PrecoBRL: 1000, StatusID: "recomendado", Fortes: []string{"Tela 7 polegadas", "Botoes fisicos (virar pagina)", "EPUB nativo"}, Fracos: []string{"Custo medio-alto"}},
            {Marca: "Onyx", Modelo: "Boox Note Air", CatID: "e_reader", PrecoBRL: 2500, StatusID: "recomendado", Fortes: []string{"E-ink GRANDE (10.3 polegadas)", "Android (apps TTS, OpenDyslexic)", "Caneta (anotar)"}, Fracos: []string{"Custo alto", "Mais pesado que Kindle"}},
        },
        Observacao: "E-reader e para QUEM LER Dói. Dislexico que desiste de livro impresso LE no e-re...",
    },
    {
        CatID: "gps_tracker",
        CatRotulo: "GPS Tracker (Pessoal)",
        Descricao: "GPS tracker pessoal para criancas (perdida/abduzida), idosos (demencia/fuga), e pessoas com deficiencia cognitiva. Nao e...",
        Deficiencias: []string{"Crianca (seguranca / rastreamento)", "Idoso (demencia / mobilidade reduzida)", "Cognitiva / Sindrome de Down"},
        CustoMinimo: 200.0,
        Specs: []Especificacao{
            {Parametro: "GPS", ValorMinimo: "Sim (com A-GPS)", Obrigatorio: true, Justificativa: "Localizacao precisa (< 10m em externo)...."},
            {Parametro: "Bateria", ValorMinimo: "Minimo 5 dias (ideal 15+)", Obrigatorio: true, Justificativa: "Crianca/idoso NAO vai lembrar de recarregar todo dia. Bateria longa e CRITICA...."},
            {Parametro: "Botao SOS", ValorMinimo: "Sim (1 toque = alerta)", Obrigatorio: true, Justificativa: "Crianca aperta = pais recebem localizacao + alerta. Idoso aperta = socorro...."},
            {Parametro: "Cerca virtual", ValorMinimo: "Sim (geofencing)", Obrigatorio: true, Justificativa: "Pais definem area segura. Crianca sai = alerta automatico...."},
            {Parametro: "Resistencia", ValorMinimo: "IPX7+ (agua e impacto)", Obrigatorio: true, Justificativa: "Crianca derruba, molha, perde. Tracker precisa sobreviver...."},
            {Parametro: "Conectividade", ValorMinimo: "4G LTE (chip SIM integrado)", Obrigatorio: true, Justificativa: "Nao depende de WiFi. Funciona em qualquer lugar com sinal celular...."},
            {Parametro: "Tamanho", ValorMinimo: "Pequeno e discreto (< 50g)", Obrigatorio: true, Justificativa: "Crianca nao quer usar algo grande/visivel. Discreto = uso continuo...."},
            {Parametro: "Audio bidirecional", ValorMinimo: "Sim (microfone + alto-falante)", Obrigatorio: false, Justificativa: "Pais podem FALAR com a crianca pelo tracker. Crianca pode chamar...."},
        },
        Produtos: []ProdutoCOTS{
            {Marca: "Apple", Modelo: "AirTag", CatID: "gps_tracker", PrecoBRL: 400, StatusID: "parcial", Fortes: []string{"Custo baixo", "Bateria 1 ANO", "Rede Find My (milhoes de iPhones)"}, Fracos: []string{"SEM GPS proprio (usa BLE + iPhones proximos)", "SEM botao SOS", "SEM audio bidirecional"}},
            {Marca: "Samsung", Modelo: "Galaxy SmartTag2", CatID: "gps_tracker", PrecoBRL: 200, StatusID: "parcial", Fortes: []string{"Custo baixo", "Bateria 500 dias", "Rede SmartThings Find"}, Fracos: []string{"Sem GPS proprio (BLE)", "Sem SOS direto", "Sem audio bidirecional"}},
            {Marca: "Tuya", Modelo: "Smart GPS Tracker (4G)", CatID: "gps_tracker", PrecoBRL: 200, StatusID: "conforme", Fortes: []string{"GPS REAL (com 4G)", "Botao SOS", "Audio bidirecional"}, Fracos: []string{"Qualidade de build variavel", "App generico (menos polido)"}},
            {Marca: "GlobalSat", Modelo: "TR-600", CatID: "gps_tracker", PrecoBRL: 600, StatusID: "conforme", Fortes: []string{"GPS + 4G", "Bateria 15 dias", "SOS + audio"}, Fracos: []string{"Grande (nao discreto para crianca)"}},
            {Marca: "Angel Watch", Modelo: "Angel Watch Co", CatID: "gps_tracker", PrecoBRL: 1200, StatusID: "recomendado", Fortes: []string{"RELOGIO GPS para crianca", "GPS + 4G + WiFi", "Chamada de voz (2 vias)"}, Fracos: []string{"Bateria 2-3 dias (smartwatch = curta)", "Custo medio"}},
        },
        Observacao: "GPS tracker e para QUEM NAO PODE PEDIR AJUDA. Crianca de 5 anos perdida no shopp...",
    },
}

// ============================================================================
// 4. DEMO
// ============================================================================

func main() {
    fmt.Println(strings.Repeat("=", 70))
    fmt.Println("OpenAccessibilityHardwareSpecs -- Hardware COTS para Acessibilidade")
    fmt.Println(strings.Repeat("=", 70))

    numCat := 12
    totalProd := 59
    totalSpecs := 95
    totalRecs := 0

    fmt.Printf("\n[%d DISPOSITIVOS COTS ESPECIFICADOS]\n", numCat)
    for _, s := range todasSpecs {
        fmt.Printf("  %s (Custo min: R$ %.0f)\n", s.CatRotulo, s.CustoMinimo)
    }

    // CATALOGO COMPLETO
    fmt.Println("\n" + strings.Repeat("=", 70))
    fmt.Println("[CATALOGO COMPLETO]")
    fmt.Println(strings.Repeat("=", 70))
    for _, s := range todasSpecs {
        fmt.Printf("\n  --- %s ---\n", s.CatRotulo)
        for _, p := range s.Produtos {
            fmt.Printf("    [%s] %s %s -- R$ %.0f\n", p.StatusID, p.Marca, p.Modelo, p.PrecoBRL)
            if p.StatusID == "recomendado" { totalRecs++ }
        }
    }

    // DETALHE: HEADPHONE
    fmt.Println("\n" + strings.Repeat("=", 70))
    fmt.Println("[DETALHE] HEADPHONE BLUETOOTH")
    fmt.Println(strings.Repeat("=", 70))
    hp := todasSpecs[0]
    fmt.Printf("\n  ESPECIFICACOES MINIMAS (%d specs):\n", len(hp.Specs))
    for _, sp := range hp.Specs {
        flag := "opc"
        if sp.Obrigatorio { flag = "OBRIG" }
        fmt.Printf("    [%s] %s: %s\n", flag, sp.Parametro, sp.ValorMinimo)
    }
    fmt.Printf("\n  PRODUTOS SUPORTADOS (%d):\n", len(hp.Produtos))
    for _, p := range hp.Produtos {
        fmt.Printf("\n    [%s] %s %s -- R$ %.0f\n", p.StatusID, p.Marca, p.Modelo, p.PrecoBRL)
        fmt.Printf("      Fortes: %s\n", strings.Join(p.Fortes, "; "))
        fmt.Printf("      Fracos: %s\n", strings.Join(p.Fracos, "; "))
    }

    // SCORECARD
    fmt.Println("\n" + strings.Repeat("=", 70))
    fmt.Println("[SCORECARD]")
    fmt.Println(strings.Repeat("=", 70))
    fmt.Printf("  categorias_dispositivos........ %d\n", numCat)
    fmt.Printf("  produtos_catalogados........... %d\n", totalProd)
    fmt.Printf("  produtos_recomendados.......... %d\n", totalRecs)
    fmt.Printf("  specs_totais................... %d\n", totalSpecs)
    fmt.Println("  deficiencias_cobertas.......... 11")

    // FILOSOFIA
    fmt.Println("\n" + strings.Repeat("=", 70))
    fmt.Println("FILOSOFIA -- Dispositivos que nao precisam ser feitos do zero")
    fmt.Println(strings.Repeat("=", 70))
    fmt.Println("\nO computador RISC-V e fabricado do zero.")
    fmt.Println("Mas headphones, smartwatches, eye-trackers -- esses sao COTS.")
    fmt.Println("A Republica define ESPECIFICACOES MINIMAS. Vendors implementam.")
    fmt.Println("\"A especificacao nao pode ser alterada por um vendor.\"")
    fmt.Println("\nSem spec, o mercado fabrica o que quer.")
    fmt.Println("Com spec, o mercado fabrica o que PRECISA.")
}
