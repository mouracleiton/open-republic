/********************************************************************************
 * OpenAccessibilityHardwareSpecs -- Hardware COTS para Acessibilidade
 * 12 dispositivos. Specs minimas. Lista de equipamentos suportados.
 * Author: OpenRepublic Team
 *******************************************************************************/
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

// ============================================================================
// 1. ENUMS
// ============================================================================

typedef enum {
    CAT_HEADPHONE_BT,  // Headphone Bluetooth
    CAT_SMARTPHONE,  // Smartphone
    CAT_SMARTWATCH,  // Smartwatch
    CAT_EYE_TRACKER,  // Eye Tracker
    CAT_BRAILLE_DISPLAY,  // Display Braille
    CAT_SWITCH,  // Switch Button (botao de acesso)
    CAT_BONE_CONDUCTION,  // Fone de Conducao Ossea
    CAT_MICROFONE,  // Microfone
    CAT_WEBCAM,  // Webcam
    CAT_TABLET,  // Tablet (CAA)
    CAT_E_READER,  // E-reader (Leitor Digital)
    CAT_GPS_TRACKER  // GPS Tracker (Pessoal)
} CategoriaDispositivo;

static const char* cat_rotulo[] = {
    "Headphone Bluetooth",
    "Smartphone",
    "Smartwatch",
    "Eye Tracker",
    "Display Braille",
    "Switch Button (botao de acesso)",
    "Fone de Conducao Ossea",
    "Microfone",
    "Webcam",
    "Tablet (CAA)",
    "E-reader (Leitor Digital)",
    "GPS Tracker (Pessoal)",
};

static const char* cat_id[] = {
    "headphone_bt",
    "smartphone",
    "smartwatch",
    "eye_tracker",
    "braille_display",
    "switch",
    "bone_conduction",
    "microfone",
    "webcam",
    "tablet",
    "e_reader",
    "gps_tracker",
};

typedef enum {
    DEF_CEGUEIRA,  // Cego / Baixa visao
    DEF_SURDEZ,  // Surdo / Deficiente auditivo
    DEF_MOTORA,  // Motora / Tetraplegia / Paralisia cerebral
    DEF_COGNITIVA,  // Cognitiva / Sindrome de Down
    DEF_AUTISMO,  // TEA / Autismo
    DEF_TDAH,  // TDAH / Dislexia
    DEF_COMUNICACAO,  // Comunicacao (nao-verbal / afasia)
    DEF_NEUROLOGICA,  // Neurologica (ELA / Parkinson / Epilepsia)
    DEF_IDOSO,  // Idoso (demencia / mobilidade reduzida)
    DEF_CRIANCA,  // Crianca (seguranca / rastreamento)
    DEF_UNIVERSAL  // Uso universal (todas as deficiencias)
} DeficienciaAlvo;

typedef enum {
    STATUS_CONFORME,
    STATUS_PARCIAL,
    STATUS_NAO_CONFORME,
    STATUS_RECOMENDADO
} StatusSpec;

// ============================================================================
// 2. STRUCTS
// ============================================================================

typedef struct {
    const char* parametro;
    const char* valor_minimo;
    bool obrigatorio;
    const char* justificativa;
} Especificacao;

typedef struct {
    const char* marca;
    const char* modelo;
    const char* cat_id;
    float preco_brl;
    const char* status_id;
    const char* pontos_fortes;
    const char* pontos_fracos;
} ProdutoCOTS;

typedef struct {
    const char* cat_id;
    const char* cat_rotulo;
    const char* descricao;
    const char* deficiencias;
    float custo_minimo_brl;
    int num_specs;
    Especificacao* specs;
    int num_produtos;
    ProdutoCOTS* produtos;
    const char* observacao;
} SpecDispositivo;

// --- Headphone Bluetooth ---
static Especificacao specs_0[] = {
    {"Bluetooth", "5.0 ou superior (LE Audio / aptX Adaptive)", true, "LE Audio reduz latencia e permite multi-stream (2 fones no mesmo dispositivo)."},
    {"Latencia", "< 200ms (ideal < 150ms)", true, "Latencia alta quebra TTS em tempo real e audio descricao sincronizada."},
    {"Bateria", "Minimo 8h uso continuo", true, "Dia de trabalho/estudo sem recarregar. Cego depende do fone o dia todo."},
    {"Microfone integrado", "Sim, com cancelamento de ruido", true, "Para comando de voz, chamadas, e Libras por contexto de audio."},
    {"Perfil Bluetooth", "A2DP + HFP + AVRCP", true, "A2DP = audio de qualidade. HFP = viva-voz. AVRCP = controle remoto."},
    {"Multiponto", "Sim (conectar 2 dispositivos simultaneamente)", true, "Cego pode estar conectado ao smartphone E ao computador ao mesmo tempo."},
    {"Controles fisicos", "Botoes reais (nao touch)", true, "Cego nao pode usar controles capacitivos sem feedback visual."},
    {"Feedback de bateria", "Anuncio de bateria por voz ou tom", true, "Cego precisa saber quando vai acabar sem ver o LED."},
    {"Conforto", "Ajustavel, leve (< 300g), alcolchoado", true, "Uso prolongado (8h+) requer conforto. Pessoas com sensibilidade sensorial (TEA) precisam de materiais suaves."},
    {"Codec", "SBC minimo. AAC/SBC/LDAC desejavel", false, "AAC melhora qualidade para usuarios de iPhone."},
    {"Resistencia", "IPX4 (suor e chuva)", false, "Para uso em mobilidade urbana."},
    {"Jack 3.5mm", "Sim (backup com fio)", true, "Se Bluetooth falha, fio e backup. Cego nao pode ficar sem audio."},
};
static ProdutoCOTS produtos_0[] = {
    {"JBL", "Tune 510BT", "headphone_bt", 250.0f, "conforme", "Bateria 40h; Multiponto; Custo acessivel", "Sem anuncio de bateria por voz; Controle touch (parcial)"},
    {"Sony", "WH-CH520", "headphone_bt", 350.0f, "recomendado", "Bateria 50h; Multiponto; Anuncio de bateria por voz", "Sem jack 3.5mm (USB-C apenas)"},
    {"Sennheiser", "HD 350BT", "headphone_bt", 500.0f, "recomendado", "Bateria 30h; AAC + aptX; Confortavel 8h+", "Sem jack 3.5mm"},
    {"Anker", "Soundcore Life Q20", "headphone_bt", 250.0f, "conforme", "Bateria 40h; ANC basico; Custo baixo", "Multiponto instavel; App requer visual"},
    {"Philips", "SHL3070BK", "headphone_bt", 150.0f, "parcial", "Custo muito baixo; Jack 3.5mm", "Bateria 9h (minimo); Sem multiponto; Latencia alta para TTS"},
    {"Apple", "AirPods (2nd gen)", "headphone_bt", 1500.0f, "recomendado", "Acessibilidade iOS nativa; Live Listen (microfone remoto); Audio descricao integrada", "Custo alto; Sem controles fisicos (touch); Bateria ~5h por carga (24h com case)"},
    {"Apple", "AirPods Pro 2", "headphone_bt", 2500.0f, "recomendado", "Live Listen; ANC adaptativo; Modo Conversacao (transparencia)", "Custo premium; Sem jack 3.5mm"},
    {"Samsung", "Galaxy Buds FE", "headphone_bt", 600.0f, "conforme", "Live Listen no Android; ANC; Custo medio", "Bateria ~6h por carga; Sem jack"},
};

// --- Smartphone ---
static Especificacao specs_1[] = {
    {"Sistema operacional", "Android 13+ ou iOS 16+", true, "Versoes antigas nao tem features de acessibilidade criticas."},
    {"RAM", "Minimo 4GB (ideal 6GB+)", true, "Apps de acessibilidade (TalkBack, VoiceOver, Libras) consomem RAM."},
    {"Armazenamento", "Minimo 64GB", true, "Modelos de IA local + apps de CAA + mapas offline precisam de espaco."},
    {"Camera", "Minimo 12MP com autofocus + OIS", true, "Visao computacional (OCR, descricao de cena, Libras) precisa de camera decente."},
    {"Bateria", "Minimo 4000mAh", true, "Dia inteiro de uso com acessibilidade ativa (TTS + GPS + camera)."},
    {"TalkBack/VoiceOver", "Nativo e funcional", true, "Leitor de tela nativo e OBRIGATORIO. Sem ele, cego nao usa o telefone."},
    {"Bluetooth", "5.0+", true, "Para conectar headphones, hearing aids, braille displays."},
    {"GPS", "Sim, com A-GPS", true, "Navegacao para cego, rastreamento de crianca/idoso."},
    {"NFC", "Sim", false, "Pagamento sem QR code (OpenAntiQRPayment)."},
    {"Acelerometro/Giroscopio", "Sim", true, "Deteccao de queda (idoso), bussola para navegacao (cego)."},
    {"Slot microSD", "Desejavel", false, "Armazenamento expansivel para mapas offline e modelos de IA."},
    {"Radio FM", "Desejavel (com fone como antena)", false, "Emergencias: FM nao depende de internet."},
};
static ProdutoCOTS produtos_1[] = {
    {"Samsung", "Galaxy A15 5G", "smartphone", 1000.0f, "recomendado", "Custo baixo; Android 14; Bateria 5000mAh", "RAM 4GB (minimo); Sem OIS na camera"},
    {"Samsung", "Galaxy A55 5G", "smartphone", 2000.0f, "recomendado", "RAM 8GB; Camera com OIS; Bateria 5000mAh", "Sem slot microSD (alguns mercados)"},
    {"Motorola", "Moto G84 5G", "smartphone", 1300.0f, "recomendado", "RAM 8GB (otimo nesta faixa); Bateria 5000mAh; Android limpo (TalkBack funciona bem)", "Camera sem OIS"},
    {"Apple", "iPhone SE (2022)", "smartphone", 3000.0f, "recomendado", "VoiceOver (melhor leitor de tela do mercado); Detecao de pessoas, portas, sons (Magnifier); Audio descricao", "Bateria 2018mAh (fraca); Tela 4.7 polegadas (pequena)"},
    {"Apple", "iPhone 15", "smartphone", 5000.0f, "recomendado", "VoiceOver + Magnifier + Detecao de sons; LiDAR (navegacao para cego); Camera 48MP", "Custo premium"},
    {"Xiaomi", "Redmi Note 13", "smartphone", 1100.0f, "conforme", "Custo baixo; Bateria 5000mAh; Camera 108MP", "MIUI tem bugs de acessibilidade; TalkBack menos testado"},
};

// --- Smartwatch ---
static Especificacao specs_2[] = {
    {"Sensor cardiaco", "Sim (PPG ou ECG)", true, "Deteccao de estresse, arritmia, taquicardia."},
    {"Acelerometro", "Sim (3 eixos)", true, "Deteccao de queda (idoso), tremor (Parkinson)."},
    {"GPS", "Sim (integrado)", true, "Rastreamento de crianca/idoso sem depender do smartphone."},
    {"Bateria", "Minimo 3 dias (ideal 7+)", true, "Biometria continua requer uso 24h. Recarga diaria e falha."},
    {"Resistencia", "IP68 (agua e poeira)", true, "Usa no banho, na chuva, na piscina. Biometria nao para."},
    {"Vibracao", "Motor haptico forte", true, "Surdo nao ouve alerta. Cego nao ve. Vibration e universal."},
    {"Tela sempre ligada", "Desejavel", false, "Idoso precisa ver as horas sem tocar na tela."},
    {"Temperatura corporea", "Desejavel", false, "Predicao de convulsao epileptica (pesquisa Apple Watch)."},
    {"SpO2 (oximetria)", "Desejavel", false, "Monitoramento respiratorio."},
};
static ProdutoCOTS produtos_2[] = {
    {"Amazfit", "Bip 5", "smartwatch", 500.0f, "recomendado", "Bateria 10 DIAS; GPS; Tela grande (1.69 polegadas)", "Sem ECG; Sem SpO2 confiavel"},
    {"Xiaomi", "Smart Band 8", "smartwatch", 250.0f, "conforme", "Bateria 16 DIAS; Custo muito baixo; HR + SpO2", "Sem GPS integrado (depende do telefone); Tela pequena para idoso com baixa visao"},
    {"Apple", "Apple Watch SE (2nd gen)", "smartwatch", 2500.0f, "recomendado", "Deteccao de queda (SOS automatico); ECG (aprovado FDA); GPS integrado", "Bateria ~18h (1 dia); Custo alto"},
    {"Apple", "Apple Watch Series 9", "smartwatch", 4500.0f, "recomendado", "ECG + SpO2 + Temperatura; Deteccao de queda + SOS; GPS", "Bateria ~18h; Custo premium"},
    {"Samsung", "Galaxy Watch FE", "smartwatch", 1000.0f, "conforme", "ECG (em alguns paises); Bateria 2-3 dias; Deteccao de queda", "ECG bloqueado em alguns mercados"},
    {"Garmin", "Forerunner 55", "smartwatch", 1500.0f, "conforme", "Bateria 14 DIAS em modo watch; GPS de precisao; Vibracao forte", "Foco em esporte (menos features de saude)"},
};

// --- Eye Tracker ---
static Especificacao specs_3[] = {
    {"Precisao", "< 1 grau visual (ideal < 0.5)", true, "Para clicar em botoes pequenos na tela. Precisao baixa = frustracao."},
    {"Frequencia", "Minimo 60Hz (ideal 120Hz+)", true, "Taxa de atualizacao. Baixa = lag entre olhar e clique."},
    {"Calibracao", "Automatica ou 1-5 pontos", true, "Calibracao complexa (16 pontos) e exaustiva para quem tem mobilidade limitada."},
    {"Compatibilidade", "Windows + macOS + Linux", true, "Nao pode prender o usuario num SO."},
    {"Software inclusivo", "Teclado virtual + CAA", true, "Eye tracker sem software de comunicacao e so hardware inutil."},
    {"Latencia", "< 50ms", true, "Entre o olhar e o cursor responder. Alto = nauseas."},
    {"Trabalha com oculos", "Sim", true, "Muitos usuarios de eye tracker usam oculos."},
    {"Headbox", "Minimo 25x25cm", true, "Area de liberdade de movimento da cabeca. Pequeno = usuario precisa ficar imovel."},
};
static ProdutoCOTS produtos_3[] = {
    {"Tobii", "Eye Tracker 5", "eye_tracker", 3500.0f, "recomendado", "Precisao < 0.5 grau; 144Hz; Headbox amplo", "Custo alto; Windows-centric (Linux parcial)"},
    {"Tobii", "Dynavox", "eye_tracker", 15000.0f, "recomendado", "Solucao completa (tablet + eye tracker + CAA); Snap Core First (CAA); Suporte clinico", "Custo ESPECIALIZADO; Fornecedor unico"},
    {"IRISBOND", "Hiru", "eye_tracker", 5000.0f, "conforme", "Precisao < 0.5 grau; Multiplataforma; Usado em hospitais brasileiros", "Disponibilidade limitada no Brasil"},
    {"Windows", "Eye Control (nativo)", "eye_tracker", 0.0f, "conforme", "GRATUITO no Windows 10/11; Funciona com Tobii 4C e EyeX", "So funciona com hardware Tobii; Limitado a Windows"},
    {"Apple", "iPad com AssistiveTouch (olhos)", "eye_tracker", 5000.0f, "recomendado", "Eye Tracking nativo no iPadOS (2024+); GRATUITO (incluido no iPad); CAA integrada", "So funciona em iPad Pro/Air recentes; Precisao pode variar"},
};

// --- Display Braille ---
static Especificacao specs_4[] = {
    {"Celas", "Minimo 8 celas (ideal 40+)", true, "8 celas = palavra por vez. 40+ = linha inteira. Mais celas = leitura fluida."},
    {"Tipo de cela", "Piezoeletrica (8 pinos por cela)", true, "Braille de 8 pontos (computador). 6 pontos so perde informacao de formatacao."},
    {"Conexao", "Bluetooth + USB", true, "Bluetooth para smartphone. USB para computador. Ambos necessarios."},
    {"Bateria", "Minimo 10h", true, "Dia de trabalho/estudo. Recarga no meio do dia e falha."},
    {"Botoes de navegacao", "Sim (pan, rota, cursor routing)", true, "Navegar pelo texto sem depender do smartphone."},
    {"Compatibilidade", "TalkBack (Android) + VoiceOver (iOS) + NVDA/JAWS (PC)", true, "Display Braille sem leitor de tela e so pinos. Precisa do SOFTWARE."},
};
static ProdutoCOTS produtos_4[] = {
    {"Orbit Research", "Orbit Reader 20 Plus", "braille_display", 4000.0f, "recomendado", "20 celas (bom para custo); BLUETOOTH + USB; Bateria 20h", "20 celas limita leitura longa; Sem teclado Perkins integrado"},
    {"Help Tech", "Active Star 40", "braille_display", 12000.0f, "recomendado", "40 celas (leitura fluida); Bluetooth + USB; Teclado Perkins integrado", "Custo ESPECIALIZADO"},
    {"Freedom Scientific", "Focus 40 Blue", "braille_display", 10000.0f, "recomendado", "40 celas; Bluetooth + USB; Compativel com JAWS + NVDA + VoiceOver + TalkBack", "Custo ESPECIALIZADO"},
    {"Seika", "Seika 40", "braille_display", 6000.0f, "conforme", "40 celas; Custo mais baixo para 40 celas; Bluetooth + USB", "Qualidade de build inferior; Suporte limitado no Brasil"},
    {"Apple", "iPhone/iPad com Braille (software)", "braille_display", 0.0f, "parcial", "GRATUITO no iOS; Mostra Braille na tela (para videntes aprenderem); Conecta com display fisico via Bluetooth", "Nao e Braille TATIL (so visual); Para cego real, precisa do display fisico"},
};

// --- Switch Button (botao de acesso) ---
static Especificacao specs_5[] = {
    {"Forca de ativacao", "Maximo 100g (ideal < 50g)", true, "Usuario com paralisia cerebral pode nao conseguir apertar botao duro."},
    {"Tamanho da superficie", "Minimo 5cm diametro", true, "Alvo grande para quem tem tremor ou movimento involuntario."},
    {"Feedback", "Tatil (click) + auditivo (click) + visual (LED)", true, "O usuario PRECISA saber que ativou. Multi-modal."},
    {"Conexao", "Bluetooth e/ou Jack 3.5mm", true, "Jack 3.5mm = compatibilidade universal (AT, switch-adapted toys). BT = sem fio."},
    {"Resistencia", "A prova de impacto e saliva", true, "Usuario pode ter espasmo. Crianca pode morder/bater."},
    {"Montagem", "Compativel com braços articulados e suportes", true, "Switch precisa ser posicionado onde o usuario tem movimento."},
    {"Bateria", "Minimo 100h (ideal: meses)", true, "Switch com fio nao precisa. Switch BT precisa durar semanas."},
};
static ProdutoCOTS produtos_5[] = {
    {"Ablenet", "Big Red Switch", "switch", 400.0f, "recomendado", "Padrao da industria de AT; Superficie 12.7cm; Forca ~57g", "Custo alto para um botao"},
    {"Ablenet", "Spec Switch", "switch", 350.0f, "recomendado", "Superficie 5cm; Forca muito baixa (~21g); Ideal para ELA avancada", "Custo alto"},
    {"Enabling Devices", "Jelly Bean Switch", "switch", 300.0f, "conforme", "Superficie 6.5cm; Cores vivas (baixa visao); Jack 3.5mm", "Feedback menos firme que Ablenet"},
    {"DIY", "Switch caseiro (pizza box + foil)", "switch", 20.0f, "parcial", "Custo MUITO baixo; Customizavel; Tutorial aberto (CC0)", "Durabilidade baixa; Precisa manutencao frequente; Sem feedback de qualidade"},
    {"Logitech", "Adaptive Gaming Kit", "switch", 600.0f, "recomendado", "3 switches grandes + 5 pequenos; Abas de etiqueta (identificacao tatil); Custo razoavel para kit completo", "Foco em gaming (adaptavel para AT)"},
};

// --- Fone de Conducao Ossea ---
static Especificacao specs_6[] = {
    {"Bluetooth", "5.0+", true, "Conexao estavel para TTS e audio descricao."},
    {"Orelha aberta", "Sim (nao bloqueia canal auditivo)", true, "Cego que usa conducao ossea PRECISA ouvir o ambiente tambem."},
    {"Bateria", "Minimo 6h", true, "Dia de uso continuo."},
    {"Microfone", "Sim", true, "Para comando de voz e chamadas."},
    {"Conforto", "Ajustavel, leve (< 40g)", true, "Repouso na teca (osso temporal). Pressao inadequada = dor."},
    {"Resistencia", "IPX4+ (suor)", true, "Uso em atividade fisica e mobilidade urbana."},
};
static ProdutoCOTS produtos_6[] = {
    {"Shokz", "OpenRun Pro", "bone_conduction", 1200.0f, "recomendado", "Lider em conducao ossea; Bateria 10h; Bluetooth 5.1", "Custo alto"},
    {"Shokz", "OpenMove", "bone_conduction", 600.0f, "recomendado", "Custo medio; Bateria 6h; Bluetooth 5.1", "Qualidade de som inferior ao OpenRun Pro"},
    {"Mojawa", "Run Plus", "bone_conduction", 1000.0f, "conforme", "Bateria 8h; IP68; MP3 integrado (16GB)", "Marca menos estabelecida"},
};

// --- Microfone ---
static Especificacao specs_7[] = {
    {"Cancelamento de ruido", "Sim (DSP ou cardiode)", true, "Comando de voz em ambiente ruidoso precisa de CNR."},
    {"Conexao", "USB ou Bluetooth", true, "USB = zero latencia. BT = mobilidade."},
    {"Padrao polar", "Cardiode ou unidirecional", true, "Captura a voz do usuario, nao o ambiente inteiro."},
    {"Frequencia", "100Hz-10kHz minimo", true, "Cobre voz humana. Baixa frequencia = graves (homem). Alta = agudos (mulher/crianca)."},
    {"Mute fisico", "Botao de mute REAL (nao software)", true, "Privacidade: usuario PRECISA saber que o microfone esta mudo."},
    {"LED indicador", "Sim (LED mostra se esta captando)", true, "Surdo nao ouve o proprio audio. Precisa VER que o microfone esta ativo."},
    {"Filtro pop", "Sim (espuma ou malha)", false, "Reduz 'p' e 't' que estouram o reconhecimento de voz."},
};
static ProdutoCOTS produtos_7[] = {
    {"Blue", "Yeti Nano", "microfone", 500.0f, "recomendado", "USB-C; Cardiode + omnidirecional; Mute fisico (botao na frente)", "Grande (ocupa espaco na mesa)"},
    {"Fifine", "K669B", "microfone", 150.0f, "recomendado", "Custo MUITO baixo; USB; Cardiode", "Sem mute fisico; Qualidade decente mas nao premium"},
    {"Jabra", "Speak 510", "microfone", 700.0f, "recomendado", "Bluetooth + USB; CNR excelente; Speakerphone (para reuniao com legenda)", "Custo medio-alto"},
    {"In_build", "Microfone do smartphone", "microfone", 0.0f, "parcial", "GRATUITO; Sempre presente; Portatil", "Qualidade varia; CNR limitado; Nao ideal para texto longo"},
};

// --- Webcam ---
static Especificacao specs_8[] = {
    {"Resolucao", "Minimo 720p (ideal 1080p)", true, "Libras requer resolucao suficiente para ver expressoes faciais e maos."},
    {"Frequencia", "Minimo 30fps (ideal 60fps)", true, "Libras e RAPIDO. 15fps perde sinais. 60fps captura tudo."},
    {"Autofocus", "Sim (rapido)", true, "Surdo que se move ao sinais nao pode ficar borrado."},
    {"Campo de visao", "Minimo 70 graus (ideal 90+)", true, "Libras requer espaco para maos e bracos. Webcam estreita corta os sinais."},
    {"Baixa luz", "Funciona em < 50 lux", true, "Nem todos tem iluminacao de estudio. Sala de casa a noite."},
    {"Microfone integrado", "Desejavel (backup)", false, "Para videochamada com surdo (audio + Libras simultaneo)."},
};
static ProdutoCOTS produtos_8[] = {
    {"Logitech", "C920 HD Pro", "webcam", 400.0f, "recomendado", "1080p 30fps; Autofocus rapido; Campo 78 graus", "Sem 60fps em 1080p"},
    {"Logitech", "C922 Pro", "webcam", 500.0f, "recomendado", "1080p 30fps / 720p 60fps; Fundo substituivel; Tripé incluido", "Custo medio-alto"},
    {"Microsoft", "LifeCam Studio", "webcam", 600.0f, "conforme", "1080p; Campo 75 graus; Alta qualidade de build", "Descontinuado pela Microsoft (suporte incerto)"},
    {"In_build", "Webcam do notebook/smartphone", "webcam", 0.0f, "parcial", "GRATUITO; Sempre presente", "Qualidade varia muito; Campo de visao estreito em notebooks; Autofocus lento em cameras baratas"},
};

// --- Tablet (CAA) ---
static Especificacao specs_9[] = {
    {"Tela", "Minimo 10 polegadas", true, "Espaco para grade de simbolos CAA (minimo 8x8)."},
    {"Touch", "Multitoque capacitivo (sensivel)", true, "Usuario com motora fina comprometida precisa de tela responsiva."},
    {"Bateria", "Minimo 8h", true, "Dia de uso (escola, trabalho, terapia)."},
    {"Sintetizador de voz", "Nativo + apps CAA", true, "Tablet sem TTS e so uma tela. Precisa FALAR."},
    {"Software CAA", "Compativel com: Avaz, Proloquo, TD Snap", true, "Apps de CAA sao OBRIGATORIOS. Tablet sem apps CAA nao serve."},
    {"Case protetor", "Case resistente a queda (military-grade)", true, "Crianca com autismo pode ter comportamento de quebrar. Tablet = R$ 1000+."},
    {"Suporte", "Compativel com suportes de mesa/mobiliario", true, "Cadeirante precisa do tablet montado na cadeira."},
};
static ProdutoCOTS produtos_9[] = {
    {"Apple", "iPad (10th gen)", "tablet", 3000.0f, "recomendado", "Melhor ecossistema de CAA do mercado; Proloquo2Go (padrao ouro CAA); Avaz", "Custo alto"},
    {"Samsung", "Galaxy Tab A9+", "tablet", 1000.0f, "recomendado", "Custo baixo para tablet; Tela 11 polegadas; Android (Avaz, TD Snap)", "Menos apps CAA que iOS; Case protetor menos disponivel"},
    {"Apple", "iPad Pro 11", "tablet", 7000.0f, "recomendado", "Eye Tracking nativo (2024+); Proloquo2Go + Voice Control; M-series chip (rapido)", "Custo PREMIUM"},
    {"Amazon", "Fire HD 10", "tablet", 600.0f, "parcial", "Custo MUITO baixo; Tela 10.1 polegadas", "Sem Google Play nativo (apps CAA limitados); Sem Proloquo2Go (iOS only); Android fork (Fire OS)"},
};

// --- E-reader (Leitor Digital) ---
static Especificacao specs_10[] = {
    {"Tela", "E-ink (nao LCD/LED)", true, "E-ink nao emite luz azul. Nao cansa. Dislexico e TDAH sao sensivel a luz."},
    {"Fonte ajustavel", "Sim (tamanho + familia + espacamento)", true, "OpenDyslexic, Atkinson Hyperlegible, espacamento entre linhas."},
    {"Tamanho de fonte", "Ate minimo 36pt", true, "Baixa visao precisa de fonte grande. E-reader permite sem limite fisico."},
    {"TTS", "Sim (text-to-speech integrado)", true, "Dislexico que cansa de ler pode OUVIR. Cego pode ouvir o livro todo."},
    {"Contraste", "Ajustavel (escuro sobre claro, claro sobre escuro)", true, "Modo escuro (fundo preto, texto branco) para baixa visao e sensibilidade a luz."},
    {"Suporte a formatos", "EPUB, PDF, TXT, HTML", true, "Nao pode prender o usuario num formato proprietario."},
    {"Bateria", "Minimo 4 semanas", true, "E-ink consome quase nada. Meses de uso sem recarregar."},
};
static ProdutoCOTS produtos_10[] = {
    {"Amazon", "Kindle Paperwhite", "e_reader", 600.0f, "recomendado", "E-ink 300ppi; Fonte ajustavel + OpenDyslexic; TTS (VoiceView)", "Formato proprietario (AZW3); Suporte a EPUB limitado"},
    {"Kobo", "Clara 2E", "e_reader", 700.0f, "recomendado", "E-ink 300ppi; Suporte nativo a EPUB; OpenDyslexic nativo", "TTS limitado"},
    {"Kobo", "Libra H2O", "e_reader", 1000.0f, "recomendado", "Tela 7 polegadas; Botoes fisicos (virar pagina); EPUB nativo", "Custo medio-alto"},
    {"Onyx", "Boox Note Air", "e_reader", 2500.0f, "recomendado", "E-ink GRANDE (10.3 polegadas); Android (apps TTS, OpenDyslexic); Caneta (anotar)", "Custo alto; Mais pesado que Kindle"},
};

// --- GPS Tracker (Pessoal) ---
static Especificacao specs_11[] = {
    {"GPS", "Sim (com A-GPS)", true, "Localizacao precisa (< 10m em externo)."},
    {"Bateria", "Minimo 5 dias (ideal 15+)", true, "Crianca/idoso NAO vai lembrar de recarregar todo dia. Bateria longa e CRITICA."},
    {"Botao SOS", "Sim (1 toque = alerta)", true, "Crianca aperta = pais recebem localizacao + alerta. Idoso aperta = socorro."},
    {"Cerca virtual", "Sim (geofencing)", true, "Pais definem area segura. Crianca sai = alerta automatico."},
    {"Resistencia", "IPX7+ (agua e impacto)", true, "Crianca derruba, molha, perde. Tracker precisa sobreviver."},
    {"Conectividade", "4G LTE (chip SIM integrado)", true, "Nao depende de WiFi. Funciona em qualquer lugar com sinal celular."},
    {"Tamanho", "Pequeno e discreto (< 50g)", true, "Crianca nao quer usar algo grande/visivel. Discreto = uso continuo."},
    {"Audio bidirecional", "Sim (microfone + alto-falante)", false, "Pais podem FALAR com a crianca pelo tracker. Crianca pode chamar."},
};
static ProdutoCOTS produtos_11[] = {
    {"Apple", "AirTag", "gps_tracker", 400.0f, "parcial", "Custo baixo; Bateria 1 ANO; Rede Find My (milhoes de iPhones)", "SEM GPS proprio (usa BLE + iPhones proximos); SEM botao SOS; SEM audio bidirecional"},
    {"Samsung", "Galaxy SmartTag2", "gps_tracker", 200.0f, "parcial", "Custo baixo; Bateria 500 dias; Rede SmartThings Find", "Sem GPS proprio (BLE); Sem SOS direto; Sem audio bidirecional"},
    {"Tuya", "Smart GPS Tracker (4G)", "gps_tracker", 200.0f, "conforme", "GPS REAL (com 4G); Botao SOS; Audio bidirecional", "Qualidade de build variavel; App generico (menos polido)"},
    {"GlobalSat", "TR-600", "gps_tracker", 600.0f, "conforme", "GPS + 4G; Bateria 15 dias; SOS + audio", "Grande (nao discreto para crianca)"},
    {"Angel Watch", "Angel Watch Co", "gps_tracker", 1200.0f, "recomendado", "RELOGIO GPS para crianca; GPS + 4G + WiFi; Chamada de voz (2 vias)", "Bateria 2-3 dias (smartwatch = curta); Custo medio"},
};

static SpecDispositivo todas_specs[12] = {
    {
        .cat_id = "headphone_bt",
        .cat_rotulo = "Headphone Bluetooth",
        .descricao = "Headphone Bluetooth para acessibilidade auditiva. Usado para TTS (text-to-speech), audio descricao, ...",
        .deficiencias = "Surdo / Deficiente auditivo, Cego / Baixa visao, Uso universal (todas as deficiencias)",
        .custo_minimo_brl = 80.0f,
        .num_specs = 12,
        .specs = specs_0,
        .num_produtos = 8,
        .produtos = produtos_0,
        .observacao = "O Headphone Bluetooth e o DISPOSITIVO MAIS UNIVERSAL da acessibilidade. Cego usa para TTS. Surdo usa...",
    },
    {
        .cat_id = "smartphone",
        .cat_rotulo = "Smartphone",
        .descricao = "Smartphone como CORPO ESTENDIDO (Telefonista). Camera=olhos, microfone=ouvidos, GPS=direcao, acelero...",
        .deficiencias = "Cego / Baixa visao, Surdo / Deficiente auditivo, Motora / Tetraplegia / Paralisia cerebral",
        .custo_minimo_brl = 800.0f,
        .num_specs = 12,
        .specs = specs_1,
        .num_produtos = 6,
        .produtos = produtos_1,
        .observacao = "O smartphone e o CORACAO da acessibilidade da Republica. E camera, microfone, GPS, acelerometro, TTS...",
    },
    {
        .cat_id = "smartwatch",
        .cat_rotulo = "Smartwatch",
        .descricao = "Smartwatch para biometria continua: estresse (frequencia cardiaca), predicao de convulsao (temperatu...",
        .deficiencias = "Neurologica (ELA / Parkinson / Epilepsia), Idoso (demencia / mobilidade reduzida), TDAH / Dislexia",
        .custo_minimo_brl = 400.0f,
        .num_specs = 9,
        .specs = specs_2,
        .num_produtos = 6,
        .produtos = produtos_2,
        .observacao = "Smartwatch = biometria PASSIVA. O usuario nao precisa fazer nada. O relogio detecta queda e chama so...",
    },
    {
        .cat_id = "eye_tracker",
        .cat_rotulo = "Eye Tracker",
        .descricao = "Eye tracker para tetraplegia, ELA, paralisia cerebral. O olho e o ultimo musculo voluntario em ELA. ...",
        .deficiencias = "Motora / Tetraplegia / Paralisia cerebral, Neurologica (ELA / Parkinson / Epilepsia), Comunicacao (nao-verbal / afasia)",
        .custo_minimo_brl = 2000.0f,
        .num_specs = 8,
        .specs = specs_3,
        .num_produtos = 5,
        .produtos = produtos_3,
        .observacao = "Eye tracker e o DISPOSITIVO QUE DEVOLVE A VOZ. Pessoa com ELA perde tudo -- braços, pernas, voz. Sob...",
    },
    {
        .cat_id = "braille_display",
        .cat_rotulo = "Display Braille",
        .descricao = "Display Braille para cegos. Converte texto digital em celas braille táteis. E o OUTPUT equivalente a...",
        .deficiencias = "Cego / Baixa visao",
        .custo_minimo_brl = 3000.0f,
        .num_specs = 6,
        .specs = specs_4,
        .num_produtos = 5,
        .produtos = produtos_4,
        .observacao = "Display Braille e o UNICO OUTPUT para SURDO-CEGO. Surdo-cego nao tem audio (surdo) nem tela (cego). ...",
    },
    {
        .cat_id = "switch",
        .cat_rotulo = "Switch Button (botao de acesso)",
        .descricao = "Switch button: botao grande de 1 toque para acesso. Para tetraplegia severa, paralisia cerebral, ELA...",
        .deficiencias = "Motora / Tetraplegia / Paralisia cerebral, Neurologica (ELA / Parkinson / Epilepsia), Comunicacao (nao-verbal / afasia)",
        .custo_minimo_brl = 100.0f,
        .num_specs = 7,
        .specs = specs_5,
        .num_produtos = 5,
        .produtos = produtos_5,
        .observacao = "Switch e o DISPOSITIVO MAIS SIMPLES E MAIS PODEROSO. 1 botao. 1 acao. Para quem so move 1 musculo (c...",
    },
    {
        .cat_id = "bone_conduction",
        .cat_rotulo = "Fone de Conducao Ossea",
        .descricao = "Fone de conducao ossea: som viaja pelo osso (cranio) ate o nervo auditivo, bypassando o ouvido exter...",
        .deficiencias = "Surdo / Deficiente auditivo",
        .custo_minimo_brl = 500.0f,
        .num_specs = 6,
        .specs = specs_6,
        .num_produtos = 3,
        .produtos = produtos_6,
        .observacao = "Conducao ossea e PARA SURDO CONDUTIVO especificamente. Surdo neurosensorial severo NAO beneficia. Im...",
    },
    {
        .cat_id = "microfone",
        .cat_rotulo = "Microfone",
        .descricao = "Microfone para comando de voz, fala-para-texto, e captura de audio ambiente para o Telefonista. Para...",
        .deficiencias = "Motora / Tetraplegia / Paralisia cerebral, Surdo / Deficiente auditivo, Cego / Baixa visao",
        .custo_minimo_brl = 50.0f,
        .num_specs = 7,
        .specs = specs_7,
        .num_produtos = 4,
        .produtos = produtos_7,
        .observacao = "Microfone e a ENTRADA para quem SO FALA. Tetraplegico que nao digita, FALA. Precisa de microfone bom...",
    },
    {
        .cat_id = "webcam",
        .cat_rotulo = "Webcam",
        .descricao = "Webcam para Libras (surdo se comunica por sinais na camera), visao computacional (descricao de cena ...",
        .deficiencias = "Surdo / Deficiente auditivo, Cego / Baixa visao",
        .custo_minimo_brl = 150.0f,
        .num_specs = 6,
        .specs = specs_8,
        .num_produtos = 4,
        .produtos = produtos_8,
        .observacao = "Webcam e a JANELA para Libras. Surdo se comunica por SINAIS. Sinais precisam de FRAMES RAPIDOS e CAM...",
    },
    {
        .cat_id = "tablet",
        .cat_rotulo = "Tablet (CAA)",
        .descricao = "Tablet para CAA (Comunicacao Aumentativa e Alternativa). Para nao-verbal (autismo nao-verbal, afasia...",
        .deficiencias = "Comunicacao (nao-verbal / afasia), TEA / Autismo, Cognitiva / Sindrome de Down",
        .custo_minimo_brl = 800.0f,
        .num_specs = 7,
        .specs = specs_9,
        .num_produtos = 4,
        .produtos = produtos_9,
        .observacao = "Tablet CAA e a VOZ de quem nao fala. Crianca autista nao-verbal toca 'QUERO AGUA'. Tablet FALA: 'Que...",
    },
    {
        .cat_id = "e_reader",
        .cat_rotulo = "E-reader (Leitor Digital)",
        .descricao = "E-reader (tela e-ink) para dislexia, baixa visao, daltonismo. Tela e-ink nao emite luz (nao cansa). ...",
        .deficiencias = "TDAH / Dislexia, Cego / Baixa visao, TEA / Autismo",
        .custo_minimo_brl = 300.0f,
        .num_specs = 7,
        .specs = specs_10,
        .num_produtos = 4,
        .produtos = produtos_10,
        .observacao = "E-reader e para QUEM LER Dói. Dislexico que desiste de livro impresso LE no e-reader (fonte OpenDysl...",
    },
    {
        .cat_id = "gps_tracker",
        .cat_rotulo = "GPS Tracker (Pessoal)",
        .descricao = "GPS tracker pessoal para criancas (perdida/abduzida), idosos (demencia/fuga), e pessoas com deficien...",
        .deficiencias = "Crianca (seguranca / rastreamento), Idoso (demencia / mobilidade reduzida), Cognitiva / Sindrome de Down",
        .custo_minimo_brl = 200.0f,
        .num_specs = 8,
        .specs = specs_11,
        .num_produtos = 5,
        .produtos = produtos_11,
        .observacao = "GPS tracker e para QUEM NAO PODE PEDIR AJUDA. Crianca de 5 anos perdida no shopping nao liga para os...",
    },
};

// ============================================================================
// 3. DEMO
// ============================================================================

int main(void) {
    int num_categorias = 12;
    int total_produtos = 59;
    int total_specs = 95;
    int total_recs = 0;

    printf("======================================================================\n");
    printf("OpenAccessibilityHardwareSpecs -- Hardware COTS para Acessibilidade\n");
    printf("======================================================================\n");

    printf("\n[%d DISPOSITIVOS COTS ESPECIFICADOS]\n", num_categorias);
    for (int i = 0; i < num_categorias; i++) {
        printf("  %s (Custo min: R$ %.0f)\n", todas_specs[i].cat_rotulo, todas_specs[i].custo_minimo_brl);
    }

    // CATALOGO COMPLETO
    printf("\n======================================================================\n");
    printf("[CATALOGO COMPLETO]\n");
    printf("======================================================================\n");
    for (int i = 0; i < num_categorias; i++) {
        printf("\n  --- %s ---\n", todas_specs[i].cat_rotulo);
        for (int j = 0; j < todas_specs[i].num_produtos; j++) {
            ProdutoCOTS* p = &todas_specs[i].produtos[j];
            printf("    [%s] %s %s -- R$ %.0f\n", p->status_id, p->marca, p->modelo, p->preco_brl);
            if (strcmp(p->status_id, "recomendado") == 0) total_recs++;
        }
    }

    // DETALHE: HEADPHONE
    printf("\n======================================================================\n");
    printf("[DETALHE] HEADPHONE BLUETOOTH\n");
    printf("======================================================================\n");
    int hp_idx = 0;  // headphone_bt = primeiro
    printf("\n  ESPECIFICACOES MINIMAS (%d specs):\n", todas_specs[hp_idx].num_specs);
    for (int j = 0; j < todas_specs[hp_idx].num_specs; j++) {
        Especificacao* sp = &todas_specs[hp_idx].specs[j];
        printf("    [%s] %s: %s\n", sp->obrigatorio ? "OBRIG" : "opc", sp->parametro, sp->valor_minimo);
    }
    printf("\n  PRODUTOS SUPORTADOS (%d):\n", todas_specs[hp_idx].num_produtos);
    for (int j = 0; j < todas_specs[hp_idx].num_produtos; j++) {
        ProdutoCOTS* p = &todas_specs[hp_idx].produtos[j];
        printf("\n    [%s] %s %s -- R$ %.0f\n", p->status_id, p->marca, p->modelo, p->preco_brl);
        printf("      Fortes: %s\n", p->pontos_fortes);
        printf("      Fracos: %s\n", p->pontos_fracos);
    }

    // SCORECARD
    printf("\n======================================================================\n");
    printf("[SCORECARD]\n");
    printf("======================================================================\n");
    printf("  categorias_dispositivos........ %d\n", num_categorias);
    printf("  produtos_catalogados........... %d\n", total_produtos);
    printf("  produtos_recomendados.......... %d\n", total_recs);
    printf("  specs_totais................... %d\n", total_specs);
    printf("  deficiencias_cobertas.......... 11\n");

    // FILOSOFIA
    printf("\n======================================================================\n");
    printf("FILOSOFIA -- Dispositivos que nao precisam ser feitos do zero\n");
    printf("======================================================================\n");
    printf("\n");
    printf("O computador RISC-V e fabricado do zero.\n");
    printf("Mas headphones, smartwatches, eye-trackers -- esses sao COTS.\n");
    printf("A Republica define ESPECIFICACOES MINIMAS. Vendors implementam.\n");
    printf("\"A especificacao nao pode ser alterada por um vendor.\"\n");
    printf("\nA lista de equipamentos suportados e CONFORMIDADE TECNICA.\n");
    printf("Sem spec, o mercado fabrica o que quer.\n");
    printf("Com spec, o mercado fabrica o que PRECISA.\n");
    return 0;
}
