// OpenAccessibilityHardwareSpecs -- Especificacoes de Hardware COTS para Acessibilidade
// =====================================================================================
// "Dispositivos que nao precisam ser feitos do zero. Precisam ser ESPECIFICADOS."
//
// O computador RISC-V e fabricado do zero (OpenSovereignTech).
// Mas headphones, smartwatches, eye-trackers, braille displays -- esses sao COTS
// (Commercial Off-The-Shelf). A Republica NAO precisa reinventar todos.
//
// O que a Republica faz: define ESPECIFICACOES MINIMAS de acessibilidade.
// Quem fabricar, segue a spec. Quem comprar, sabe o que esperar.
//
// PRINCIPIO: "A especificacao nao pode ser alterada por um vendor."
// A Republica define o padrao. Vendors implementam.
// Se um produto nao atende a spec, NAO e comprado. NAO e recomendado.
//
// OS 12 DISPOSITIVOS COTS ESPECIFICADOS:
//
// 1. HEADPHONE BLUETOOTH (acessibilidade auditiva, TTS, audio descricao)
// 2. SMARTPHONE (corpo estendido -- Telefonista)
// 3. SMARTWATCH (biometria, estresse, convulsao, queda)
// 4. EYE TRACKER (tetraplegia, ELA, mobilidade reduzida)
// 5. BRAILLE DISPLAY (cego, baixa visao)
// 6. SWITCH BUTTON (tetraplegia, paralisia cerebral, acesso por 1 toque)
// 7. BONE CONDUCTION (surdo unilateral, condutiva -- ouve pelo osso)
// 8. MICROFONE (comando de voz, fala-para-texto, Libras contexto)
// 9. WEBCAM (Libras, visao computacional, descricao de cena)
// 10. TABLET (CAA - Comunicacao Aumentativa e Alternativa)
// 11. E-READER (dislexia, baixa visao, Daltonismo)
// 12. GPS TRACKER (crianca perdida, idoso com demencia)
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1: Dispositivo de acessibilidade e DIREITO, nao luxo. Spec minima garante.
// - P2: Autonomia corporal -- o dispositivo e extensao do corpo.
// - P6: Acesso universal = acesso ao hardware que permite acesso.
// - P9 (Soberania): Spec imutavel. Vendor nao altera. Republica define.
//
// Author: OpenRepublic Team

use std::collections::HashMap;
use std::fmt;

// ============================================================================
// 1. ENUMS (module-level)
// ============================================================================

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum CategoriaDispositivo {
    HeadphoneBt,
    Smartphone,
    Smartwatch,
    EyeTracker,
    BrailleDisplay,
    Switch,
    BoneConduction,
    Microfone,
    Webcam,
    Tablet,
    EReader,
    GpsTracker,
}

impl CategoriaDispositivo {
    pub fn id(&self) -> &'static str {
        match self {
            CategoriaDispositivo::HeadphoneBt => "headphone_bt",
            CategoriaDispositivo::Smartphone => "smartphone",
            CategoriaDispositivo::Smartwatch => "smartwatch",
            CategoriaDispositivo::EyeTracker => "eye_tracker",
            CategoriaDispositivo::BrailleDisplay => "braille_display",
            CategoriaDispositivo::Switch => "switch",
            CategoriaDispositivo::BoneConduction => "bone_conduction",
            CategoriaDispositivo::Microfone => "microfone",
            CategoriaDispositivo::Webcam => "webcam",
            CategoriaDispositivo::Tablet => "tablet",
            CategoriaDispositivo::EReader => "e_reader",
            CategoriaDispositivo::GpsTracker => "gps_tracker",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            CategoriaDispositivo::HeadphoneBt => "Headphone Bluetooth",
            CategoriaDispositivo::Smartphone => "Smartphone",
            CategoriaDispositivo::Smartwatch => "Smartwatch",
            CategoriaDispositivo::EyeTracker => "Eye Tracker",
            CategoriaDispositivo::BrailleDisplay => "Display Braille",
            CategoriaDispositivo::Switch => "Switch Button (botao de acesso)",
            CategoriaDispositivo::BoneConduction => "Fone de Conducao Ossea",
            CategoriaDispositivo::Microfone => "Microfone",
            CategoriaDispositivo::Webcam => "Webcam",
            CategoriaDispositivo::Tablet => "Tablet (CAA)",
            CategoriaDispositivo::EReader => "E-reader (Leitor Digital)",
            CategoriaDispositivo::GpsTracker => "GPS Tracker (Pessoal)",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum DeficienciaAlvo {
    Cegueira,
    Surdez,
    Motora,
    Cognitiva,
    Autismo,
    Tdah,
    Comunicacao,
    Neurologica,
    Idoso,
    Crianca,
    Universal,
}

impl DeficienciaAlvo {
    pub fn id(&self) -> &'static str {
        match self {
            DeficienciaAlvo::Cegueira => "cegueira",
            DeficienciaAlvo::Surdez => "surdez",
            DeficienciaAlvo::Motora => "motora",
            DeficienciaAlvo::Cognitiva => "cognitiva",
            DeficienciaAlvo::Autismo => "autismo",
            DeficienciaAlvo::Tdah => "tdah",
            DeficienciaAlvo::Comunicacao => "comunicacao",
            DeficienciaAlvo::Neurologica => "neurologica",
            DeficienciaAlvo::Idoso => "idoso",
            DeficienciaAlvo::Crianca => "crianca",
            DeficienciaAlvo::Universal => "universal",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            DeficienciaAlvo::Cegueira => "Cego / Baixa visao",
            DeficienciaAlvo::Surdez => "Surdo / Deficiente auditivo",
            DeficienciaAlvo::Motora => "Motora / Tetraplegia / Paralisia cerebral",
            DeficienciaAlvo::Cognitiva => "Cognitiva / Sindrome de Down",
            DeficienciaAlvo::Autismo => "TEA / Autismo",
            DeficienciaAlvo::Tdah => "TDAH / Dislexia",
            DeficienciaAlvo::Comunicacao => "Comunicacao (nao-verbal / afasia)",
            DeficienciaAlvo::Neurologica => "Neurologica (ELA / Parkinson / Epilepsia)",
            DeficienciaAlvo::Idoso => "Idoso (demencia / mobilidade reduzida)",
            DeficienciaAlvo::Crianca => "Crianca (seguranca / rastreamento)",
            DeficienciaAlvo::Universal => "Uso universal (todas as deficiencias)",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum NivelCusto {
    Gratuito,
    Baixo,
    Medio,
    Alto,
    Premium,
    Especializado,
}

impl NivelCusto {
    pub fn id(&self) -> &'static str {
        match self {
            NivelCusto::Gratuito => "gratuito",
            NivelCusto::Baixo => "baixo",
            NivelCusto::Medio => "medio",
            NivelCusto::Alto => "alto",
            NivelCusto::Premium => "premium",
            NivelCusto::Especializado => "especializado",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            NivelCusto::Gratuito => "Gratuito (doacao / biblioteca)",
            NivelCusto::Baixo => "Baixo custo (< R$ 100)",
            NivelCusto::Medio => "Custo medio (R$ 100-500)",
            NivelCusto::Alto => "Custo alto (R$ 500-2000)",
            NivelCusto::Premium => "Premium (R$ 2000-10000)",
            NivelCusto::Especializado => "Especializado (> R$ 10000)",
        }
    }

    pub fn min_real(&self) -> i32 {
        match self {
            NivelCusto::Gratuito => 0,
            NivelCusto::Baixo => 1,
            NivelCusto::Medio => 101,
            NivelCusto::Alto => 501,
            NivelCusto::Premium => 2001,
            NivelCusto::Especializado => 10001,
        }
    }

    pub fn max_real(&self) -> i32 {
        match self {
            NivelCusto::Gratuito => 0,
            NivelCusto::Baixo => 100,
            NivelCusto::Medio => 500,
            NivelCusto::Alto => 2000,
            NivelCusto::Premium => 10000,
            NivelCusto::Especializado => 999999,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum StatusSpec {
    Conforme,
    Parcial,
    NaoConforme,
    Recomendado,
}

impl StatusSpec {
    pub fn id(&self) -> &'static str {
        match self {
            StatusSpec::Conforme => "conforme",
            StatusSpec::Parcial => "parcial",
            StatusSpec::NaoConforme => "nao_conforme",
            StatusSpec::Recomendado => "recomendado",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            StatusSpec::Conforme => "Conforme: atende todas as specs minimas",
            StatusSpec::Parcial => "Parcial: atende a maioria, mas tem lacunas",
            StatusSpec::NaoConforme => "Nao conforme: nao atende specs minimas",
            StatusSpec::Recomendado => "Recomendado: excede as specs minimas",
        }
    }
}

// ============================================================================
// 2. STRUCTS (dataclasses equivalent)
// ============================================================================

#[derive(Debug, Clone)]
pub struct Especificacao {
    pub parametro: String,
    pub valor_minimo: String,
    pub obrigatorio: bool,
    pub justificativa: String,
}

#[derive(Debug, Clone)]
pub struct ProdutoSuportado {
    pub marca: String,
    pub modelo: String,
    pub categoria: CategoriaDispositivo,
    pub preco_aprox_brl: f64,
    pub status: StatusSpec,
    pub deficiencias_atendidas: Vec<DeficienciaAlvo>,
    pub pontos_fortes: Vec<String>,
    pub pontos_fracos: Vec<String>,
    pub notes: String,
}

#[derive(Debug, Clone)]
pub struct SpecDispositivo {
    pub categoria: CategoriaDispositivo,
    pub descricao: String,
    pub deficiencias_atendidas: Vec<DeficienciaAlvo>,
    pub specs: Vec<Especificacao>,
    pub produtos: Vec<ProdutoSuportado>,
    pub custo_minimo_brl: f64,
    pub observacao: String,
}

// ============================================================================
// 3. DADOS: AS 12 ESPECIFICACOES
// ============================================================================

fn init_specs() -> Vec<SpecDispositivo> {
    vec![
        // === 1. HEADPHONE BLUETOOTH ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::HeadphoneBt,
            descricao: "Headphone Bluetooth para acessibilidade auditiva. Usado para TTS (text-to-speech), audio descricao, legendas em audio, amplificacao para deficiente auditivo, e comunicacao com o Telefonista.".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Surdez,
                DeficienciaAlvo::Cegueira,
                DeficienciaAlvo::Universal,
                DeficienciaAlvo::Idoso,
            ],
            custo_minimo_brl: 80.0,
            specs: vec![
                Especificacao { parametro: "Bluetooth".to_string(), valor_minimo: "5.0 ou superior (LE Audio / aptX Adaptive)".to_string(), obrigatorio: true, justificativa: "LE Audio reduz latencia e permite multi-stream (2 fones no mesmo dispositivo).".to_string() },
                Especificacao { parametro: "Latencia".to_string(), valor_minimo: "< 200ms (ideal < 150ms)".to_string(), obrigatorio: true, justificativa: "Latencia alta quebra TTS em tempo real e audio descricao sincronizada.".to_string() },
                Especificacao { parametro: "Bateria".to_string(), valor_minimo: "Minimo 8h uso continuo".to_string(), obrigatorio: true, justificativa: "Dia de trabalho/estudo sem recarregar. Cego depende do fone o dia todo.".to_string() },
                Especificacao { parametro: "Microfone integrado".to_string(), valor_minimo: "Sim, com cancelamento de ruido".to_string(), obrigatorio: true, justificativa: "Para comando de voz, chamadas, e Libras por contexto de audio.".to_string() },
                Especificacao { parametro: "Perfil Bluetooth".to_string(), valor_minimo: "A2DP + HFP + AVRCP".to_string(), obrigatorio: true, justificativa: "A2DP = audio de qualidade. HFP = viva-voz. AVRCP = controle remoto.".to_string() },
                Especificacao { parametro: "Multiponto".to_string(), valor_minimo: "Sim (conectar 2 dispositivos simultaneamente)".to_string(), obrigatorio: true, justificativa: "Cego pode estar conectado ao smartphone E ao computador ao mesmo tempo.".to_string() },
                Especificacao { parametro: "Controles fisicos".to_string(), valor_minimo: "Botoes reais (nao touch)".to_string(), obrigatorio: true, justificativa: "Cego nao pode usar controles capacitivos sem feedback visual.".to_string() },
                Especificacao { parametro: "Feedback de bateria".to_string(), valor_minimo: "Anuncio de bateria por voz ou tom".to_string(), obrigatorio: true, justificativa: "Cego precisa saber quando vai acabar sem ver o LED.".to_string() },
                Especificacao { parametro: "Conforto".to_string(), valor_minimo: "Ajustavel, leve (< 300g), alcolchoado".to_string(), obrigatorio: true, justificativa: "Uso prolongado (8h+) requer conforto. Pessoas com sensibilidade sensorial (TEA) precisam de materiais suaves.".to_string() },
                Especificacao { parametro: "Codec".to_string(), valor_minimo: "SBC minimo. AAC/SBC/LDAC desejavel".to_string(), obrigatorio: false, justificativa: "AAC melhora qualidade para usuarios de iPhone.".to_string() },
                Especificacao { parametro: "Resistencia".to_string(), valor_minimo: "IPX4 (suor e chuva)".to_string(), obrigatorio: false, justificativa: "Para uso em mobilidade urbana.".to_string() },
                Especificacao { parametro: "Jack 3.5mm".to_string(), valor_minimo: "Sim (backup com fio)".to_string(), obrigatorio: true, justificativa: "Se Bluetooth falha, fio e backup. Cego nao pode ficar sem audio.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "JBL".to_string(), modelo: "Tune 510BT".to_string(), categoria: CategoriaDispositivo::HeadphoneBt, preco_aprox_brl: 250.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["Bateria 40h".to_string(), "Multiponto".to_string(), "Custo acessivel".to_string(), "Jack 3.5mm".to_string()], pontos_fracos: vec!["Sem anuncio de bateria por voz".to_string(), "Controle touch (parcial)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Sony".to_string(), modelo: "WH-CH520".to_string(), categoria: CategoriaDispositivo::HeadphoneBt, preco_aprox_brl: 350.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Universal, DeficienciaAlvo::Surdez], pontos_fortes: vec!["Bateria 50h".to_string(), "Multiponto".to_string(), "Anuncio de bateria por voz".to_string(), "Controles fisicos".to_string()], pontos_fracos: vec!["Sem jack 3.5mm (USB-C apenas)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Sennheiser".to_string(), modelo: "HD 350BT".to_string(), categoria: CategoriaDispositivo::HeadphoneBt, preco_aprox_brl: 500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["Bateria 30h".to_string(), "AAC + aptX".to_string(), "Confortavel 8h+".to_string(), "USB-C charge".to_string()], pontos_fracos: vec!["Sem jack 3.5mm".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Anker".to_string(), modelo: "Soundcore Life Q20".to_string(), categoria: CategoriaDispositivo::HeadphoneBt, preco_aprox_brl: 250.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["Bateria 40h".to_string(), "ANC basico".to_string(), "Custo baixo".to_string()], pontos_fracos: vec!["Multiponto instavel".to_string(), "App requer visual".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Philips".to_string(), modelo: "SHL3070BK".to_string(), categoria: CategoriaDispositivo::HeadphoneBt, preco_aprox_brl: 150.0, status: StatusSpec::Parcial, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["Custo muito baixo".to_string(), "Jack 3.5mm".to_string()], pontos_fracos: vec!["Bateria 9h (minimo)".to_string(), "Sem multiponto".to_string(), "Latencia alta para TTS".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "AirPods (2nd gen)".to_string(), categoria: CategoriaDispositivo::HeadphoneBt, preco_aprox_brl: 1500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez, DeficienciaAlvo::Universal], pontos_fortes: vec!["Acessibilidade iOS nativa".to_string(), "Live Listen (microfone remoto)".to_string(), "Audio descricao integrada".to_string(), "Detecao de sons (Porta, Cachorro, Sirene)".to_string()], pontos_fracos: vec!["Custo alto".to_string(), "Sem controles fisicos (touch)".to_string(), "Bateria ~5h por carga (24h com case)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "AirPods Pro 2".to_string(), categoria: CategoriaDispositivo::HeadphoneBt, preco_aprox_brl: 2500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez, DeficienciaAlvo::Universal], pontos_fortes: vec!["Live Listen".to_string(), "ANC adaptativo".to_string(), "Modo Conversacao (transparencia)".to_string(), "Detecao de sons ambiente".to_string()], pontos_fracos: vec!["Custo premium".to_string(), "Sem jack 3.5mm".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Samsung".to_string(), modelo: "Galaxy Buds FE".to_string(), categoria: CategoriaDispositivo::HeadphoneBt, preco_aprox_brl: 600.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez, DeficienciaAlvo::Universal], pontos_fortes: vec!["Live Listen no Android".to_string(), "ANC".to_string(), "Custo medio".to_string()], pontos_fracos: vec!["Bateria ~6h por carga".to_string(), "Sem jack".to_string()], notes: "".to_string() },
            ],
            observacao: "O Headphone Bluetooth e o DISPOSITIVO MAIS UNIVERSAL da acessibilidade. Cego usa para TTS. Surdo usa para amplificacao e Live Listen. Tetraplegico usa para comando de voz. Idoso usa para amplificacao. A spec minima garante que QUALQUER headphone recomendado funciona para TODOS.".to_string(),
        },

        // === 2. SMARTPHONE ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::Smartphone,
            descricao: "Smartphone como CORPO ESTENDIDO (Telefonista). Camera=olhos, microfone=ouvidos, GPS=direcao, acelerometro=balance, smartwatch=biometria.".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Cegueira,
                DeficienciaAlvo::Surdez,
                DeficienciaAlvo::Motora,
                DeficienciaAlvo::Autismo,
                DeficienciaAlvo::Comunicacao,
                DeficienciaAlvo::Idoso,
                DeficienciaAlvo::Crianca,
                DeficienciaAlvo::Universal,
            ],
            custo_minimo_brl: 800.0,
            specs: vec![
                Especificacao { parametro: "Sistema operacional".to_string(), valor_minimo: "Android 13+ ou iOS 16+".to_string(), obrigatorio: true, justificativa: "Versoes antigas nao tem features de acessibilidade criticas.".to_string() },
                Especificacao { parametro: "RAM".to_string(), valor_minimo: "Minimo 4GB (ideal 6GB+)".to_string(), obrigatorio: true, justificativa: "Apps de acessibilidade (TalkBack, VoiceOver, Libras) consomem RAM.".to_string() },
                Especificacao { parametro: "Armazenamento".to_string(), valor_minimo: "Minimo 64GB".to_string(), obrigatorio: true, justificativa: "Modelos de IA local + apps de CAA + mapas offline precisam de espaco.".to_string() },
                Especificacao { parametro: "Camera".to_string(), valor_minimo: "Minimo 12MP com autofocus + OIS".to_string(), obrigatorio: true, justificativa: "Visao computacional (OCR, descricao de cena, Libras) precisa de camera decente.".to_string() },
                Especificacao { parametro: "Bateria".to_string(), valor_minimo: "Minimo 4000mAh".to_string(), obrigatorio: true, justificativa: "Dia inteiro de uso com acessibilidade ativa (TTS + GPS + camera).".to_string() },
                Especificacao { parametro: "TalkBack/VoiceOver".to_string(), valor_minimo: "Nativo e funcional".to_string(), obrigatorio: true, justificativa: "Leitor de tela nativo e OBRIGATORIO. Sem ele, cego nao usa o telefone.".to_string() },
                Especificacao { parametro: "Bluetooth".to_string(), valor_minimo: "5.0+".to_string(), obrigatorio: true, justificativa: "Para conectar headphones, hearing aids, braille displays.".to_string() },
                Especificacao { parametro: "GPS".to_string(), valor_minimo: "Sim, com A-GPS".to_string(), obrigatorio: true, justificativa: "Navegacao para cego, rastreamento de crianca/idoso.".to_string() },
                Especificacao { parametro: "NFC".to_string(), valor_minimo: "Sim".to_string(), obrigatorio: false, justificativa: "Pagamento sem QR code (OpenAntiQRPayment).".to_string() },
                Especificacao { parametro: "Acelerometro/Giroscopio".to_string(), valor_minimo: "Sim".to_string(), obrigatorio: true, justificativa: "Deteccao de queda (idoso), bussola para navegacao (cego).".to_string() },
                Especificacao { parametro: "Slot microSD".to_string(), valor_minimo: "Desejavel".to_string(), obrigatorio: false, justificativa: "Armazenamento expansivel para mapas offline e modelos de IA.".to_string() },
                Especificacao { parametro: "Radio FM".to_string(), valor_minimo: "Desejavel (com fone como antena)".to_string(), obrigatorio: false, justificativa: "Emergencias: FM nao depende de internet.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Samsung".to_string(), modelo: "Galaxy A15 5G".to_string(), categoria: CategoriaDispositivo::Smartphone, preco_aprox_brl: 1000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["Custo baixo".to_string(), "Android 14".to_string(), "Bateria 5000mAh".to_string(), "TalkBack nativo".to_string(), "Camera 50MP".to_string(), "Slot microSD".to_string()], pontos_fracos: vec!["RAM 4GB (minimo)".to_string(), "Sem OIS na camera".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Samsung".to_string(), modelo: "Galaxy A55 5G".to_string(), categoria: CategoriaDispositivo::Smartphone, preco_aprox_brl: 2000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["RAM 8GB".to_string(), "Camera com OIS".to_string(), "Bateria 5000mAh".to_string(), "Bixby Vision (descricao de cena)".to_string(), "Modo Live Listen".to_string()], pontos_fracos: vec!["Sem slot microSD (alguns mercados)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Motorola".to_string(), modelo: "Moto G84 5G".to_string(), categoria: CategoriaDispositivo::Smartphone, preco_aprox_brl: 1300.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["RAM 8GB (otimo nesta faixa)".to_string(), "Bateria 5000mAh".to_string(), "Android limpo (TalkBack funciona bem)".to_string(), "Slot microSD".to_string()], pontos_fracos: vec!["Camera sem OIS".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "iPhone SE (2022)".to_string(), categoria: CategoriaDispositivo::Smartphone, preco_aprox_brl: 3000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Cegueira, DeficienciaAlvo::Surdez, DeficienciaAlvo::Universal], pontos_fortes: vec!["VoiceOver (melhor leitor de tela do mercado)".to_string(), "Detecao de pessoas, portas, sons (Magnifier)".to_string(), "Audio descricao".to_string(), "Live Listen".to_string(), "5 anos de update".to_string()], pontos_fracos: vec!["Bateria 2018mAh (fraca)".to_string(), "Tela 4.7 polegadas (pequena)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "iPhone 15".to_string(), categoria: CategoriaDispositivo::Smartphone, preco_aprox_brl: 5000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["VoiceOver + Magnifier + Detecao de sons".to_string(), "LiDAR (navegacao para cego)".to_string(), "Camera 48MP".to_string(), "USB-C".to_string(), "Live Listen".to_string()], pontos_fracos: vec!["Custo premium".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Xiaomi".to_string(), modelo: "Redmi Note 13".to_string(), categoria: CategoriaDispositivo::Smartphone, preco_aprox_brl: 1100.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["Custo baixo".to_string(), "Bateria 5000mAh".to_string(), "Camera 108MP".to_string(), "Slot microSD".to_string()], pontos_fracos: vec!["MIUI tem bugs de acessibilidade".to_string(), "TalkBack menos testado".to_string()], notes: "".to_string() },
            ],
            observacao: "O smartphone e o CORACAO da acessibilidade da Republica. E camera, microfone, GPS, acelerometro, TTS, leitor de tela -- tudo num so dispositivo. A spec garante que QUALQUER smartphone recomendado roda a stack do Telefonista.".to_string(),
        },

        // === 3. SMARTWATCH ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::Smartwatch,
            descricao: "Smartwatch para biometria continua: estresse (frequencia cardiaca), predicao de convulsao (temperatura + HR), deteccao de queda (idoso), lembretes (TDAH, idoso com demencia).".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Neurologica,
                DeficienciaAlvo::Idoso,
                DeficienciaAlvo::Tdah,
                DeficienciaAlvo::Autismo,
                DeficienciaAlvo::Motora,
            ],
            custo_minimo_brl: 400.0,
            specs: vec![
                Especificacao { parametro: "Sensor cardiaco".to_string(), valor_minimo: "Sim (PPG ou ECG)".to_string(), obrigatorio: true, justificativa: "Deteccao de estresse, arritmia, taquicardia.".to_string() },
                Especificacao { parametro: "Acelerometro".to_string(), valor_minimo: "Sim (3 eixos)".to_string(), obrigatorio: true, justificativa: "Deteccao de queda (idoso), tremor (Parkinson).".to_string() },
                Especificacao { parametro: "GPS".to_string(), valor_minimo: "Sim (integrado)".to_string(), obrigatorio: true, justificativa: "Rastreamento de crianca/idoso sem depender do smartphone.".to_string() },
                Especificacao { parametro: "Bateria".to_string(), valor_minimo: "Minimo 3 dias (ideal 7+)".to_string(), obrigatorio: true, justificativa: "Biometria continua requer uso 24h. Recarga diaria e falha.".to_string() },
                Especificacao { parametro: "Resistencia".to_string(), valor_minimo: "IP68 (agua e poeira)".to_string(), obrigatorio: true, justificativa: "Usa no banho, na chuva, na piscina. Biometria nao para.".to_string() },
                Especificacao { parametro: "Vibracao".to_string(), valor_minimo: "Motor haptico forte".to_string(), obrigatorio: true, justificativa: "Surdo nao ouve alerta. Cego nao ve. Vibration e universal.".to_string() },
                Especificacao { parametro: "Tela sempre ligada".to_string(), valor_minimo: "Desejavel".to_string(), obrigatorio: false, justificativa: "Idoso precisa ver as horas sem tocar na tela.".to_string() },
                Especificacao { parametro: "Temperatura corporea".to_string(), valor_minimo: "Desejavel".to_string(), obrigatorio: false, justificativa: "Predicao de convulsao epileptica (pesquisa Apple Watch).".to_string() },
                Especificacao { parametro: "SpO2 (oximetria)".to_string(), valor_minimo: "Desejavel".to_string(), obrigatorio: false, justificativa: "Monitoramento respiratorio.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Amazfit".to_string(), modelo: "Bip 5".to_string(), categoria: CategoriaDispositivo::Smartwatch, preco_aprox_brl: 500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Idoso, DeficienciaAlvo::Tdah], pontos_fortes: vec!["Bateria 10 DIAS".to_string(), "GPS".to_string(), "Tela grande (1.69 polegadas)".to_string(), "Custo baixo".to_string(), "Vibracao forte".to_string()], pontos_fracos: vec!["Sem ECG".to_string(), "Sem SpO2 confiavel".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Xiaomi".to_string(), modelo: "Smart Band 8".to_string(), categoria: CategoriaDispositivo::Smartwatch, preco_aprox_brl: 250.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Idoso, DeficienciaAlvo::Tdah], pontos_fortes: vec!["Bateria 16 DIAS".to_string(), "Custo muito baixo".to_string(), "HR + SpO2".to_string(), "Leve (27g)".to_string()], pontos_fracos: vec!["Sem GPS integrado (depende do telefone)".to_string(), "Tela pequena para idoso com baixa visao".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "Apple Watch SE (2nd gen)".to_string(), categoria: CategoriaDispositivo::Smartwatch, preco_aprox_brl: 2500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Neurologica, DeficienciaAlvo::Idoso], pontos_fortes: vec!["Deteccao de queda (SOS automatico)".to_string(), "ECG (aprovado FDA)".to_string(), "GPS integrado".to_string(), "Vibracao excelente".to_string(), "Tela sempre ligada".to_string()], pontos_fracos: vec!["Bateria ~18h (1 dia)".to_string(), "Custo alto".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "Apple Watch Series 9".to_string(), categoria: CategoriaDispositivo::Smartwatch, preco_aprox_brl: 4500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Neurologica], pontos_fortes: vec!["ECG + SpO2 + Temperatura".to_string(), "Deteccao de queda + SOS".to_string(), "GPS".to_string(), "Health Records (compartilha com medico)".to_string()], pontos_fracos: vec!["Bateria ~18h".to_string(), "Custo premium".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Samsung".to_string(), modelo: "Galaxy Watch FE".to_string(), categoria: CategoriaDispositivo::Smartwatch, preco_aprox_brl: 1000.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Idoso], pontos_fortes: vec!["ECG (em alguns paises)".to_string(), "Bateria 2-3 dias".to_string(), "Deteccao de queda".to_string(), "Android nativo".to_string()], pontos_fracos: vec!["ECG bloqueado em alguns mercados".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Garmin".to_string(), modelo: "Forerunner 55".to_string(), categoria: CategoriaDispositivo::Smartwatch, preco_aprox_brl: 1500.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Idoso], pontos_fortes: vec!["Bateria 14 DIAS em modo watch".to_string(), "GPS de precisao".to_string(), "Vibracao forte".to_string()], pontos_fracos: vec!["Foco em esporte (menos features de saude)".to_string()], notes: "".to_string() },
            ],
            observacao: "Smartwatch = biometria PASSIVA. O usuario nao precisa fazer nada. O relogio detecta queda e chama socorro. Detecta arritmia e avisa. E o sensor do corpo que o corpo nao tem (ou perdeu).".to_string(),
        },

        // === 4. EYE TRACKER ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::EyeTracker,
            descricao: "Eye tracker para tetraplegia, ELA, paralisia cerebral. O olho e o ultimo musculo voluntario em ELA. Eye tracker permite digitar, clicar, comunicar -- SO COM OS OLHOS.".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Motora,
                DeficienciaAlvo::Neurologica,
                DeficienciaAlvo::Comunicacao,
            ],
            custo_minimo_brl: 2000.0,
            specs: vec![
                Especificacao { parametro: "Precisao".to_string(), valor_minimo: "< 1 grau visual (ideal < 0.5)".to_string(), obrigatorio: true, justificativa: "Para clicar em botoes pequenos na tela. Precisao baixa = frustracao.".to_string() },
                Especificacao { parametro: "Frequencia".to_string(), valor_minimo: "Minimo 60Hz (ideal 120Hz+)".to_string(), obrigatorio: true, justificativa: "Taxa de atualizacao. Baixa = lag entre olhar e clique.".to_string() },
                Especificacao { parametro: "Calibracao".to_string(), valor_minimo: "Automatica ou 1-5 pontos".to_string(), obrigatorio: true, justificativa: "Calibracao complexa (16 pontos) e exaustiva para quem tem mobilidade limitada.".to_string() },
                Especificacao { parametro: "Compatibilidade".to_string(), valor_minimo: "Windows + macOS + Linux".to_string(), obrigatorio: true, justificativa: "Nao pode prender o usuario num SO.".to_string() },
                Especificacao { parametro: "Software inclusivo".to_string(), valor_minimo: "Teclado virtual + CAA".to_string(), obrigatorio: true, justificativa: "Eye tracker sem software de comunicacao e so hardware inutil.".to_string() },
                Especificacao { parametro: "Latencia".to_string(), valor_minimo: "< 50ms".to_string(), obrigatorio: true, justificativa: "Entre o olhar e o cursor responder. Alto = nauseas.".to_string() },
                Especificacao { parametro: "Trabalha com oculos".to_string(), valor_minimo: "Sim".to_string(), obrigatorio: true, justificativa: "Muitos usuarios de eye tracker usam oculos.".to_string() },
                Especificacao { parametro: "Headbox".to_string(), valor_minimo: "Minimo 25x25cm".to_string(), obrigatorio: true, justificativa: "Area de liberdade de movimento da cabeca. Pequeno = usuario precisa ficar imovel.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Tobii".to_string(), modelo: "Eye Tracker 5".to_string(), categoria: CategoriaDispositivo::EyeTracker, preco_aprox_brl: 3500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Motora, DeficienciaAlvo::Neurologica], pontos_fortes: vec!["Precisao < 0.5 grau".to_string(), "144Hz".to_string(), "Headbox amplo".to_string(), "Software Tobii Communicator (CAA)".to_string(), "Trabalha com oculos".to_string()], pontos_fracos: vec!["Custo alto".to_string(), "Windows-centric (Linux parcial)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Tobii".to_string(), modelo: "Dynavox".to_string(), categoria: CategoriaDispositivo::EyeTracker, preco_aprox_brl: 15000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Motora, DeficienciaAlvo::Neurologica, DeficienciaAlvo::Comunicacao], pontos_fortes: vec!["Solucao completa (tablet + eye tracker + CAA)".to_string(), "Snap Core First (CAA)".to_string(), "Suporte clinico".to_string()], pontos_fracos: vec!["Custo ESPECIALIZADO".to_string(), "Fornecedor unico".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "IRISBOND".to_string(), modelo: "Hiru".to_string(), categoria: CategoriaDispositivo::EyeTracker, preco_aprox_brl: 5000.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Motora], pontos_fortes: vec!["Precisao < 0.5 grau".to_string(), "Multiplataforma".to_string(), "Usado em hospitais brasileiros".to_string()], pontos_fracos: vec!["Disponibilidade limitada no Brasil".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Windows".to_string(), modelo: "Eye Control (nativo)".to_string(), categoria: CategoriaDispositivo::EyeTracker, preco_aprox_brl: 0.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Motora], pontos_fortes: vec!["GRATUITO no Windows 10/11".to_string(), "Funciona com Tobii 4C e EyeX".to_string()], pontos_fracos: vec!["So funciona com hardware Tobii".to_string(), "Limitado a Windows".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "iPad com AssistiveTouch (olhos)".to_string(), categoria: CategoriaDispositivo::EyeTracker, preco_aprox_brl: 5000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Motora], pontos_fortes: vec!["Eye Tracking nativo no iPadOS (2024+)".to_string(), "GRATUITO (incluido no iPad)".to_string(), "CAA integrada".to_string()], pontos_fracos: vec!["So funciona em iPad Pro/Air recentes".to_string(), "Precisao pode variar".to_string()], notes: "".to_string() },
            ],
            observacao: "Eye tracker e o DISPOSITIVO QUE DEVOLVE A VOZ. Pessoa com ELA perde tudo -- bracos, pernas, voz. Sobra o olhar. Eye tracker transforma olhar em palavras.".to_string(),
        },

        // === 5. BRAILLE DISPLAY ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::BrailleDisplay,
            descricao: "Display Braille para cegos. Converte texto digital em celas braille tateis. E o OUTPUT equivalente ao leitor de tela -- mas para quem prefere ou precisa ler pelo tato (surdos-cegos nao tem audio).".to_string(),
            deficiencias_atendidas: vec![DeficienciaAlvo::Cegueira],
            custo_minimo_brl: 3000.0,
            specs: vec![
                Especificacao { parametro: "Celas".to_string(), valor_minimo: "Minimo 8 celas (ideal 40+)".to_string(), obrigatorio: true, justificativa: "8 celas = palavra por vez. 40+ = linha inteira. Mais celas = leitura fluida.".to_string() },
                Especificacao { parametro: "Tipo de cela".to_string(), valor_minimo: "Piezoeletrica (8 pinos por cela)".to_string(), obrigatorio: true, justificativa: "Braille de 8 pontos (computador). 6 pontos so perde informacao de formatacao.".to_string() },
                Especificacao { parametro: "Conexao".to_string(), valor_minimo: "Bluetooth + USB".to_string(), obrigatorio: true, justificativa: "Bluetooth para smartphone. USB para computador. Ambos necessarios.".to_string() },
                Especificacao { parametro: "Bateria".to_string(), valor_minimo: "Minimo 10h".to_string(), obrigatorio: true, justificativa: "Dia de trabalho/estudo. Recarga no meio do dia e falha.".to_string() },
                Especificacao { parametro: "Botoes de navegacao".to_string(), valor_minimo: "Sim (pan, rota, cursor routing)".to_string(), obrigatorio: true, justificativa: "Navegar pelo texto sem depender do smartphone.".to_string() },
                Especificacao { parametro: "Compatibilidade".to_string(), valor_minimo: "TalkBack (Android) + VoiceOver (iOS) + NVDA/JAWS (PC)".to_string(), obrigatorio: true, justificativa: "Display Braille sem leitor de tela e so pinos. Precisa do SOFTWARE.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Orbit Research".to_string(), modelo: "Orbit Reader 20 Plus".to_string(), categoria: CategoriaDispositivo::BrailleDisplay, preco_aprox_brl: 4000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Cegueira], pontos_fortes: vec!["20 celas (bom para custo)".to_string(), "BLUETOOTH + USB".to_string(), "Bateria 20h".to_string(), "Custo mais baixo do mercado para Braille".to_string(), "Nota: armazenamento interno (le sem smartphone)".to_string()], pontos_fracos: vec!["20 celas limita leitura longa".to_string(), "Sem teclado Perkins integrado".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Help Tech".to_string(), modelo: "Active Star 40".to_string(), categoria: CategoriaDispositivo::BrailleDisplay, preco_aprox_brl: 12000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Cegueira], pontos_fortes: vec!["40 celas (leitura fluida)".to_string(), "Bluetooth + USB".to_string(), "Teclado Perkins integrado".to_string(), "Bateria 20h+".to_string(), "Wi-Fi (le RSS, email)".to_string()], pontos_fracos: vec!["Custo ESPECIALIZADO".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Freedom Scientific".to_string(), modelo: "Focus 40 Blue".to_string(), categoria: CategoriaDispositivo::BrailleDisplay, preco_aprox_brl: 10000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Cegueira], pontos_fortes: vec!["40 celas".to_string(), "Bluetooth + USB".to_string(), "Compativel com JAWS + NVDA + VoiceOver + TalkBack".to_string()], pontos_fracos: vec!["Custo ESPECIALIZADO".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Seika".to_string(), modelo: "Seika 40".to_string(), categoria: CategoriaDispositivo::BrailleDisplay, preco_aprox_brl: 6000.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Cegueira], pontos_fortes: vec!["40 celas".to_string(), "Custo mais baixo para 40 celas".to_string(), "Bluetooth + USB".to_string()], pontos_fracos: vec!["Qualidade de build inferior".to_string(), "Suporte limitado no Brasil".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "iPhone/iPad com Braille (software)".to_string(), categoria: CategoriaDispositivo::BrailleDisplay, preco_aprox_brl: 0.0, status: StatusSpec::Parcial, deficiencias_atendidas: vec![DeficienciaAlvo::Cegueira], pontos_fortes: vec!["GRATUITO no iOS".to_string(), "Mostra Braille na tela (para videntes aprenderem)".to_string(), "Conecta com display fisico via Bluetooth".to_string()], pontos_fracos: vec!["Nao e Braille TATIL (so visual)".to_string(), "Para cego real, precisa do display fisico".to_string()], notes: "".to_string() },
            ],
            observacao: "Display Braille e o UNICO OUTPUT para SURDO-CEGO. Surdo-cego nao tem audio (surdo) nem tela (cego). Sobra o TATO. Display Braille e a janela para o mundo digital. O custo e alto (R$ 4000-15000) -- a Republica precisa subsidiar.".to_string(),
        },

        // === 6. SWITCH BUTTON ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::Switch,
            descricao: "Switch button: botao grande de 1 toque para acesso. Para tetraplegia severa, paralisia cerebral, ELA avancada. 1 toque = 1 acao. O computador escaneia opcoes e o usuario toca o switch na opcao certa.".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Motora,
                DeficienciaAlvo::Neurologica,
                DeficienciaAlvo::Comunicacao,
            ],
            custo_minimo_brl: 100.0,
            specs: vec![
                Especificacao { parametro: "Forca de ativacao".to_string(), valor_minimo: "Maximo 100g (ideal < 50g)".to_string(), obrigatorio: true, justificativa: "Usuario com paralisia cerebral pode nao conseguir apertar botao duro.".to_string() },
                Especificacao { parametro: "Tamanho da superficie".to_string(), valor_minimo: "Minimo 5cm diametro".to_string(), obrigatorio: true, justificativa: "Alvo grande para quem tem tremor ou movimento involuntario.".to_string() },
                Especificacao { parametro: "Feedback".to_string(), valor_minimo: "Tatil (click) + auditivo (click) + visual (LED)".to_string(), obrigatorio: true, justificativa: "O usuario PRECISA saber que ativou. Multi-modal.".to_string() },
                Especificacao { parametro: "Conexao".to_string(), valor_minimo: "Bluetooth e/ou Jack 3.5mm".to_string(), obrigatorio: true, justificativa: "Jack 3.5mm = compatibilidade universal (AT, switch-adapted toys). BT = sem fio.".to_string() },
                Especificacao { parametro: "Resistencia".to_string(), valor_minimo: "A prova de impacto e saliva".to_string(), obrigatorio: true, justificativa: "Usuario pode ter espasmo. Crianca pode morder/bater.".to_string() },
                Especificacao { parametro: "Montagem".to_string(), valor_minimo: "Compativel com bracos articulados e suportes".to_string(), obrigatorio: true, justificativa: "Switch precisa ser posicionado onde o usuario tem movimento.".to_string() },
                Especificacao { parametro: "Bateria".to_string(), valor_minimo: "Minimo 100h (ideal: meses)".to_string(), obrigatorio: true, justificativa: "Switch com fio nao precisa. Switch BT precisa durar semanas.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Ablenet".to_string(), modelo: "Big Red Switch".to_string(), categoria: CategoriaDispositivo::Switch, preco_aprox_brl: 400.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Motora], pontos_fortes: vec!["Padrao da industria de AT".to_string(), "Superficie 12.7cm".to_string(), "Forca ~57g".to_string(), "Jack 3.5mm".to_string(), "Resistente".to_string()], pontos_fracos: vec!["Custo alto para um botao".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Ablenet".to_string(), modelo: "Spec Switch".to_string(), categoria: CategoriaDispositivo::Switch, preco_aprox_brl: 350.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Motora], pontos_fortes: vec!["Superficie 5cm".to_string(), "Forca muito baixa (~21g)".to_string(), "Ideal para ELA avancada".to_string()], pontos_fracos: vec!["Custo alto".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Enabling Devices".to_string(), modelo: "Jelly Bean Switch".to_string(), categoria: CategoriaDispositivo::Switch, preco_aprox_brl: 300.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Motora], pontos_fortes: vec!["Superficie 6.5cm".to_string(), "Cores vivas (baixa visao)".to_string(), "Jack 3.5mm".to_string()], pontos_fracos: vec!["Feedback menos firme que Ablenet".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "DIY".to_string(), modelo: "Switch caseiro (pizza box + foil)".to_string(), categoria: CategoriaDispositivo::Switch, preco_aprox_brl: 20.0, status: StatusSpec::Parcial, deficiencias_atendidas: vec![DeficienciaAlvo::Motora], pontos_fortes: vec!["Custo MUITO baixo".to_string(), "Customizavel".to_string(), "Tutorial aberto (CC0)".to_string()], pontos_fracos: vec!["Durabilidade baixa".to_string(), "Precisa manutencao frequente".to_string(), "Sem feedback de qualidade".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Logitech".to_string(), modelo: "Adaptive Gaming Kit".to_string(), categoria: CategoriaDispositivo::Switch, preco_aprox_brl: 600.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Motora], pontos_fortes: vec!["3 switches grandes + 5 pequenos".to_string(), "Abas de etiqueta (identificacao tatil)".to_string(), "Custo razoavel para kit completo".to_string()], pontos_fracos: vec!["Foco em gaming (adaptavel para AT)".to_string()], notes: "".to_string() },
            ],
            observacao: "Switch e o DISPOSITIVO MAIS SIMPLES E MAIS PODEROSO. 1 botao. 1 acao. Para quem so move 1 musculo (cabeca, braco, pe, sopro). Scanning: o computador mostra opcoes uma a uma. Switch na opcao certa = SELECAO. Comunicacao, controle, autonomia.".to_string(),
        },

        // === 7. BONE CONDUCTION ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::BoneConduction,
            descricao: "Fone de conducao ossea: som viaja pelo osso (cranio) ate o nervo auditivo, bypassando o ouvido externo e medio. Para surdo CONDUTIVO (problema no ouvido medio), estenose do canal, otite cronica. NAO funciona para surdo NEUROSSENSORIAL severo.".to_string(),
            deficiencias_atendidas: vec![DeficienciaAlvo::Surdez],
            custo_minimo_brl: 500.0,
            specs: vec![
                Especificacao { parametro: "Bluetooth".to_string(), valor_minimo: "5.0+".to_string(), obrigatorio: true, justificativa: "Conexao estavel para TTS e audio descricao.".to_string() },
                Especificacao { parametro: "Orelha aberta".to_string(), valor_minimo: "Sim (nao bloqueia canal auditivo)".to_string(), obrigatorio: true, justificativa: "Cego que usa conducao ossea PRECISA ouvir o ambiente tambem.".to_string() },
                Especificacao { parametro: "Bateria".to_string(), valor_minimo: "Minimo 6h".to_string(), obrigatorio: true, justificativa: "Dia de uso continuo.".to_string() },
                Especificacao { parametro: "Microfone".to_string(), valor_minimo: "Sim".to_string(), obrigatorio: true, justificativa: "Para comando de voz e chamadas.".to_string() },
                Especificacao { parametro: "Conforto".to_string(), valor_minimo: "Ajustavel, leve (< 40g)".to_string(), obrigatorio: true, justificativa: "Repouso na teca (osso temporal). Pressao inadequada = dor.".to_string() },
                Especificacao { parametro: "Resistencia".to_string(), valor_minimo: "IPX4+ (suor)".to_string(), obrigatorio: true, justificativa: "Uso em atividade fisica e mobilidade urbana.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Shokz".to_string(), modelo: "OpenRun Pro".to_string(), categoria: CategoriaDispositivo::BoneConduction, preco_aprox_brl: 1200.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez], pontos_fortes: vec!["Lider em conducao ossea".to_string(), "Bateria 10h".to_string(), "Bluetooth 5.1".to_string(), "Microfone".to_string(), "IP67".to_string()], pontos_fracos: vec!["Custo alto".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Shokz".to_string(), modelo: "OpenMove".to_string(), categoria: CategoriaDispositivo::BoneConduction, preco_aprox_brl: 600.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez], pontos_fortes: vec!["Custo medio".to_string(), "Bateria 6h".to_string(), "Bluetooth 5.1".to_string(), "IP55".to_string()], pontos_fracos: vec!["Qualidade de som inferior ao OpenRun Pro".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Mojawa".to_string(), modelo: "Run Plus".to_string(), categoria: CategoriaDispositivo::BoneConduction, preco_aprox_brl: 1000.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez], pontos_fortes: vec!["Bateria 8h".to_string(), "IP68".to_string(), "MP3 integrado (16GB)".to_string()], pontos_fracos: vec!["Marca menos estabelecida".to_string()], notes: "".to_string() },
            ],
            observacao: "Conducao ossea e PARA SURDO CONDUTIVO especificamente. Surdo neurosensorial severo NAO beneficia. Importante: cego que tambem e surdo condutivo pode usar conducao ossea e AINDA ouvir o ambiente (orelha aberta).".to_string(),
        },

        // === 8. MICROFONE ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::Microfone,
            descricao: "Microfone para comando de voz, fala-para-texto, e captura de audio ambiente para o Telefonista. Para tetraplegico que so fala. Para surdo que precisa de legenda em tempo real. Para cego que interage por voz.".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Motora,
                DeficienciaAlvo::Surdez,
                DeficienciaAlvo::Cegueira,
                DeficienciaAlvo::Comunicacao,
            ],
            custo_minimo_brl: 50.0,
            specs: vec![
                Especificacao { parametro: "Cancelamento de ruido".to_string(), valor_minimo: "Sim (DSP ou cardiode)".to_string(), obrigatorio: true, justificativa: "Comando de voz em ambiente ruidoso precisa de CNR.".to_string() },
                Especificacao { parametro: "Conexao".to_string(), valor_minimo: "USB ou Bluetooth".to_string(), obrigatorio: true, justificativa: "USB = zero latencia. BT = mobilidade.".to_string() },
                Especificacao { parametro: "Padrao polar".to_string(), valor_minimo: "Cardiode ou unidirecional".to_string(), obrigatorio: true, justificativa: "Captura a voz do usuario, nao o ambiente inteiro.".to_string() },
                Especificacao { parametro: "Frequencia".to_string(), valor_minimo: "100Hz-10kHz minimo".to_string(), obrigatorio: true, justificativa: "Cobre voz humana. Baixa frequencia = graves (homem). Alta = agudos (mulher/crianca).".to_string() },
                Especificacao { parametro: "Mute fisico".to_string(), valor_minimo: "Botao de mute REAL (nao software)".to_string(), obrigatorio: true, justificativa: "Privacidade: usuario PRECISA saber que o microfone esta mudo.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Blue".to_string(), modelo: "Yeti Nano".to_string(), categoria: CategoriaDispositivo::Microfone, preco_aprox_brl: 500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Motora, DeficienciaAlvo::Cegueira], pontos_fortes: vec!["USB-C".to_string(), "Cardiode + omnidirecional".to_string(), "Mute fisico (botao na frente)".to_string(), "Qualidade excelente".to_string()], pontos_fracos: vec!["Grande (ocupa espaco na mesa)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Fifine".to_string(), modelo: "K669B".to_string(), categoria: CategoriaDispositivo::Microfone, preco_aprox_brl: 150.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Motora], pontos_fortes: vec!["Custo MUITO baixo".to_string(), "USB".to_string(), "Cardiode".to_string(), "Tripé incluido".to_string()], pontos_fracos: vec!["Sem mute fisico".to_string(), "Qualidade decente mas nao premium".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Jabra".to_string(), modelo: "Speak 510".to_string(), categoria: CategoriaDispositivo::Microfone, preco_aprox_brl: 700.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Motora, DeficienciaAlvo::Surdez], pontos_fortes: vec!["Bluetooth + USB".to_string(), "CNR excelente".to_string(), "Speakerphone (para reunicao com legenda)".to_string(), "Mute fisico".to_string()], pontos_fracos: vec!["Custo medio-alto".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "In_build".to_string(), modelo: "Microfone do smartphone".to_string(), categoria: CategoriaDispositivo::Microfone, preco_aprox_brl: 0.0, status: StatusSpec::Parcial, deficiencias_atendidas: vec![DeficienciaAlvo::Universal], pontos_fortes: vec!["GRATUITO".to_string(), "Sempre presente".to_string(), "Portatil".to_string()], pontos_fracos: vec!["Qualidade varia".to_string(), "CNR limitado".to_string(), "Nao ideal para texto longo".to_string()], notes: "".to_string() },
            ],
            observacao: "Microfone e a ENTRADA para quem SO FALA. Tetraplegico que nao digita, FALA. Precisa de microfone bom. Surdo que precisa de legenda em tempo real, precisa capturar audio. Cego que navega por voz, precisa de microfone confiavel.".to_string(),
        },

        // === 9. WEBCAM ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::Webcam,
            descricao: "Webcam para Libras (surdo se comunica por sinais na camera), visao computacional (descricao de cena para cego), e rastreamento de mao (linguagem de sinais como input).".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Surdez,
                DeficienciaAlvo::Cegueira,
            ],
            custo_minimo_brl: 150.0,
            specs: vec![
                Especificacao { parametro: "Resolucao".to_string(), valor_minimo: "Minimo 720p (ideal 1080p)".to_string(), obrigatorio: true, justificativa: "Libras requer resolucao suficiente para ver expressoes faciais e maos.".to_string() },
                Especificacao { parametro: "Frequencia".to_string(), valor_minimo: "Minimo 30fps (ideal 60fps)".to_string(), obrigatorio: true, justificativa: "Libras e RAPIDO. 15fps perde sinais. 60fps captura tudo.".to_string() },
                Especificacao { parametro: "Autofocus".to_string(), valor_minimo: "Sim (rapido)".to_string(), obrigatorio: true, justificativa: "Surdo que se move ao sinais nao pode ficar borrado.".to_string() },
                Especificacao { parametro: "Campo de visao".to_string(), valor_minimo: "Minimo 70 graus (ideal 90+)".to_string(), obrigatorio: true, justificativa: "Libras requer espaco para maos e bracos. Webcam estreita corta os sinais.".to_string() },
                Especificacao { parametro: "Baixa luz".to_string(), valor_minimo: "Funciona em < 50 lux".to_string(), obrigatorio: true, justificativa: "Nem todos tem iluminacao de estudio. Sala de casa a noite.".to_string() },
                Especificacao { parametro: "Microfone integrado".to_string(), valor_minimo: "Desejavel (backup)".to_string(), obrigatorio: false, justificativa: "Para videochamada com surdo (audio + Libras simultaneo).".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Logitech".to_string(), modelo: "C920 HD Pro".to_string(), categoria: CategoriaDispositivo::Webcam, preco_aprox_brl: 400.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez, DeficienciaAlvo::Cegueira], pontos_fortes: vec!["1080p 30fps".to_string(), "Autofocus rapido".to_string(), "Campo 78 graus".to_string(), "Excelente baixa luz".to_string(), "Microfone stereo".to_string()], pontos_fracos: vec!["Sem 60fps em 1080p".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Logitech".to_string(), modelo: "C922 Pro".to_string(), categoria: CategoriaDispositivo::Webcam, preco_aprox_brl: 500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez], pontos_fortes: vec!["1080p 30fps / 720p 60fps".to_string(), "Fundo substituivel".to_string(), "Tripé incluido".to_string()], pontos_fracos: vec!["Custo medio-alto".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Microsoft".to_string(), modelo: "LifeCam Studio".to_string(), categoria: CategoriaDispositivo::Webcam, preco_aprox_brl: 600.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez], pontos_fortes: vec!["1080p".to_string(), "Campo 75 graus".to_string(), "Alta qualidade de build".to_string()], pontos_fracos: vec!["Descontinuado pela Microsoft (suporte incerto)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "In_build".to_string(), modelo: "Webcam do notebook/smartphone".to_string(), categoria: CategoriaDispositivo::Webcam, preco_aprox_brl: 0.0, status: StatusSpec::Parcial, deficiencias_atendidas: vec![DeficienciaAlvo::Surdez], pontos_fortes: vec!["GRATUITO".to_string(), "Sempre presente".to_string()], pontos_fracos: vec!["Qualidade varia muito".to_string(), "Campo de visao estreito em notebooks".to_string(), "Autofocus lento em cameras baratas".to_string()], notes: "".to_string() },
            ],
            observacao: "Webcam e a JANELA para Libras. Surdo se comunica por SINAIS. Sinais precisam de FRAMES RAPIDOS e CAMPO AMPLO. Webcam ruim = comunicacao cortada = exclusao.".to_string(),
        },

        // === 10. TABLET (CAA) ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::Tablet,
            descricao: "Tablet para CAA (Comunicacao Aumentativa e Alternativa). Para nao-verbal (autismo nao-verbal, afasia, ELA). Toca figura/simbolo -> fala a palavra. Ou digita -> fala.".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Comunicacao,
                DeficienciaAlvo::Autismo,
                DeficienciaAlvo::Cognitiva,
                DeficienciaAlvo::Neurologica,
            ],
            custo_minimo_brl: 800.0,
            specs: vec![
                Especificacao { parametro: "Tela".to_string(), valor_minimo: "Minimo 10 polegadas".to_string(), obrigatorio: true, justificativa: "Espaco para grade de simbolos CAA (minimo 8x8).".to_string() },
                Especificacao { parametro: "Touch".to_string(), valor_minimo: "Multitoque capacitivo (sensivel)".to_string(), obrigatorio: true, justificativa: "Usuario com motora fina comprometida precisa de tela responsiva.".to_string() },
                Especificacao { parametro: "Bateria".to_string(), valor_minimo: "Minimo 8h".to_string(), obrigatorio: true, justificativa: "Dia de uso (escola, trabalho, terapia).".to_string() },
                Especificacao { parametro: "Sintetizador de voz".to_string(), valor_minimo: "Nativo + apps CAA".to_string(), obrigatorio: true, justificativa: "Tablet sem TTS e so uma tela. Precisa FALAR.".to_string() },
                Especificacao { parametro: "Software CAA".to_string(), valor_minimo: "Compativel com: Avaz, Proloquo, TD Snap".to_string(), obrigatorio: true, justificativa: "Apps de CAA sao OBRIGATORIOS. Tablet sem apps CAA nao serve.".to_string() },
                Especificacao { parametro: "Case protetor".to_string(), valor_minimo: "Case resistente a queda (military-grade)".to_string(), obrigatorio: true, justificativa: "Crianca com autismo pode ter comportamento de quebrar. Tablet = R$ 1000+.".to_string() },
                Especificacao { parametro: "Suporte".to_string(), valor_minimo: "Compativel com suportes de mesa/mobiliario".to_string(), obrigatorio: true, justificativa: "Cadeirante precisa do tablet montado na cadeira.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "iPad (10th gen)".to_string(), categoria: CategoriaDispositivo::Tablet, preco_aprox_brl: 3000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Comunicacao, DeficienciaAlvo::Autismo], pontos_fortes: vec!["Melhor ecossistema de CAA do mercado".to_string(), "Proloquo2Go (padrao ouro CAA)".to_string(), "Avaz".to_string(), "AssistiveTouch + Eye Tracking nativo".to_string(), "Bateria 10h".to_string(), "Case Logitech Crayon".to_string()], pontos_fracos: vec!["Custo alto".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Samsung".to_string(), modelo: "Galaxy Tab A9+".to_string(), categoria: CategoriaDispositivo::Tablet, preco_aprox_brl: 1000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Comunicacao, DeficienciaAlvo::Autismo], pontos_fortes: vec!["Custo baixo para tablet".to_string(), "Tela 11 polegadas".to_string(), "Android (Avaz, TD Snap)".to_string(), "Bateria 10h+".to_string()], pontos_fracos: vec!["Menos apps CAA que iOS".to_string(), "Case protetor menos disponivel".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "iPad Pro 11".to_string(), categoria: CategoriaDispositivo::Tablet, preco_aprox_brl: 7000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Comunicacao, DeficienciaAlvo::Motora], pontos_fortes: vec!["Eye Tracking nativo (2024+)".to_string(), "Proloquo2Go + Voice Control".to_string(), "M-series chip (rapido)".to_string(), "LiDAR".to_string()], pontos_fracos: vec!["Custo PREMIUM".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Amazon".to_string(), modelo: "Fire HD 10".to_string(), categoria: CategoriaDispositivo::Tablet, preco_aprox_brl: 600.0, status: StatusSpec::Parcial, deficiencias_atendidas: vec![DeficienciaAlvo::Autismo], pontos_fortes: vec!["Custo MUITO baixo".to_string(), "Tela 10.1 polegadas".to_string()], pontos_fracos: vec!["Sem Google Play nativo (apps CAA limitados)".to_string(), "Sem Proloquo2Go (iOS only)".to_string(), "Android fork (Fire OS)".to_string()], notes: "".to_string() },
            ],
            observacao: "Tablet CAA e a VOZ de quem nao fala. Crianca autista nao-verbal toca 'QUERO AGUA'. Tablet FALA: 'Quero agua'. Pessoa com ELA digita com os olhos. Tablet FALA a mensagem. Sem tablet CAA, a pessoa e PRISIONEIRA do silencio.".to_string(),
        },

        // === 11. E-READER ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::EReader,
            descricao: "E-reader (tela e-ink) para dislexia, baixa visao, daltonismo. Tela e-ink nao emite luz (nao cansa). Fonte pode ser ampliada sem limite. OpenDyslexic font ajuda dislexico a distinguir letras.".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Tdah,
                DeficienciaAlvo::Cegueira,
                DeficienciaAlvo::Autismo,
                DeficienciaAlvo::Idoso,
            ],
            custo_minimo_brl: 300.0,
            specs: vec![
                Especificacao { parametro: "Tela".to_string(), valor_minimo: "E-ink (nao LCD/LED)".to_string(), obrigatorio: true, justificativa: "E-ink nao emite luz azul. Nao cansa. Dislexico e TDAH sao sensivel a luz.".to_string() },
                Especificacao { parametro: "Fonte ajustavel".to_string(), valor_minimo: "Sim (tamanho + familia + espacamento)".to_string(), obrigatorio: true, justificativa: "OpenDyslexic, Atkinson Hyperlegible, espacamento entre linhas.".to_string() },
                Especificacao { parametro: "Tamanho de fonte".to_string(), valor_minimo: "Ate minimo 36pt".to_string(), obrigatorio: true, justificativa: "Baixa visao precisa de fonte grande. E-reader permite sem limite fisico.".to_string() },
                Especificacao { parametro: "TTS".to_string(), valor_minimo: "Sim (text-to-speech integrado)".to_string(), obrigatorio: true, justificativa: "Dislexico que cansa de ler pode OUVIR. Cego pode ouvir o livro todo.".to_string() },
                Especificacao { parametro: "Contraste".to_string(), valor_minimo: "Ajustavel (escuro sobre claro, claro sobre escuro)".to_string(), obrigatorio: true, justificativa: "Modo escuro (fundo preto, texto branco) para baixa visao e sensibilidade a luz.".to_string() },
                Especificacao { parametro: "Suporte a formatos".to_string(), valor_minimo: "EPUB, PDF, TXT, HTML".to_string(), obrigatorio: true, justificativa: "Nao pode prender o usuario num formato proprietario.".to_string() },
                Especificacao { parametro: "Bateria".to_string(), valor_minimo: "Minimo 4 semanas".to_string(), obrigatorio: true, justificativa: "E-ink consome quase nada. Meses de uso sem recarregar.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Amazon".to_string(), modelo: "Kindle Paperwhite".to_string(), categoria: CategoriaDispositivo::EReader, preco_aprox_brl: 600.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Tdah, DeficienciaAlvo::Cegueira], pontos_fortes: vec!["E-ink 300ppi".to_string(), "Fonte ajustavel + OpenDyslexic".to_string(), "TTS (VoiceView)".to_string(), "Contraste ajustavel".to_string(), "Bateria semanas".to_string(), "Iluminacao frontal (nao irrita)".to_string()], pontos_fracos: vec!["Formato proprietario (AZW3)".to_string(), "Suporte a EPUB limitado".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Kobo".to_string(), modelo: "Clara 2E".to_string(), categoria: CategoriaDispositivo::EReader, preco_aprox_brl: 700.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Tdah], pontos_fortes: vec!["E-ink 300ppi".to_string(), "Suporte nativo a EPUB".to_string(), "OpenDyslexic nativo".to_string(), "OverDrive (biblioteca publica)".to_string()], pontos_fracos: vec!["TTS limitado".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Kobo".to_string(), modelo: "Libra H2O".to_string(), categoria: CategoriaDispositivo::EReader, preco_aprox_brl: 1000.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Tdah, DeficienciaAlvo::Cegueira], pontos_fortes: vec!["Tela 7 polegadas".to_string(), "Botoes fisicos (virar pagina)".to_string(), "EPUB nativo".to_string(), "Resistente a agua".to_string()], pontos_fracos: vec!["Custo medio-alto".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Onyx".to_string(), modelo: "Boox Note Air".to_string(), categoria: CategoriaDispositivo::EReader, preco_aprox_brl: 2500.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Tdah, DeficienciaAlvo::Cegueira], pontos_fortes: vec!["E-ink GRANDE (10.3 polegadas)".to_string(), "Android (apps TTS, OpenDyslexic)".to_string(), "Caneta (anotar)".to_string(), "Todos formatos".to_string()], pontos_fracos: vec!["Custo alto".to_string(), "Mais pesado que Kindle".to_string()], notes: "".to_string() },
            ],
            observacao: "E-reader e para QUEM LER Dói. Dislexico que desiste de livro impresso LE no e-reader (fonte OpenDyslexic, espacamento ajustado). Baixa visao que nao ve letra pequena AMPLIA sem limite. TDAH que se distrai com tela colorida FOCa no e-ink monocromatico.".to_string(),
        },

        // === 12. GPS TRACKER ===
        SpecDispositivo {
            categoria: CategoriaDispositivo::GpsTracker,
            descricao: "GPS tracker pessoal para criancas (perdida/abduzida), idosos (demencia/fuga), e pessoas com deficiencia cognitiva. Nao e smartphone -- e um RASTREADOR dedicado, simples, longa bateria.".to_string(),
            deficiencias_atendidas: vec![
                DeficienciaAlvo::Crianca,
                DeficienciaAlvo::Idoso,
                DeficienciaAlvo::Cognitiva,
            ],
            custo_minimo_brl: 200.0,
            specs: vec![
                Especificacao { parametro: "GPS".to_string(), valor_minimo: "Sim (com A-GPS)".to_string(), obrigatorio: true, justificativa: "Localizacao precisa (< 10m em externo).".to_string() },
                Especificacao { parametro: "Bateria".to_string(), valor_minimo: "Minimo 5 dias (ideal 15+)".to_string(), obrigatorio: true, justificativa: "Crianca/idoso NAO vai lembrar de recarregar todo dia. Bateria longa e CRITICA.".to_string() },
                Especificacao { parametro: "Botao SOS".to_string(), valor_minimo: "Sim (1 toque = alerta)".to_string(), obrigatorio: true, justificativa: "Crianca aperta = pais recebem localizacao + alerta. Idoso aperta = socorro.".to_string() },
                Especificacao { parametro: "Cerca virtual".to_string(), valor_minimo: "Sim (geofencing)".to_string(), obrigatorio: true, justificativa: "Pais definem area segura. Crianca sai = alerta automatico.".to_string() },
                Especificacao { parametro: "Resistencia".to_string(), valor_minimo: "IPX7+ (agua e impacto)".to_string(), obrigatorio: true, justificativa: "Crianca derruba, molha, perde. Tracker precisa sobreviver.".to_string() },
                Especificacao { parametro: "Conectividade".to_string(), valor_minimo: "4G LTE (chip SIM integrado)".to_string(), obrigatorio: true, justificativa: "Nao depende de WiFi. Funciona em qualquer lugar com sinal celular.".to_string() },
                Especificacao { parametro: "Tamanho".to_string(), valor_minimo: "Pequeno e discreto (< 50g)".to_string(), obrigatorio: true, justificativa: "Crianca nao quer usar algo grande/visivel. Discreto = uso continuo.".to_string() },
                Especificacao { parametro: "Audio bidirecional".to_string(), valor_minimo: "Sim (microfone + alto-falante)".to_string(), obrigatorio: false, justificativa: "Pais podem FALAR com a crianca pelo tracker. Crianca pode chamar.".to_string() },
            ],
            produtos: vec![
                ProdutoSuportado { marca: "Apple".to_string(), modelo: "AirTag".to_string(), categoria: CategoriaDispositivo::GpsTracker, preco_aprox_brl: 400.0, status: StatusSpec::Parcial, deficiencias_atendidas: vec![DeficienciaAlvo::Crianca, DeficienciaAlvo::Idoso], pontos_fortes: vec!["Custo baixo".to_string(), "Bateria 1 ANO".to_string(), "Rede Find My (milhoes de iPhones)".to_string(), "Discreto (31g)".to_string()], pontos_fracos: vec!["SEM GPS proprio (usa BLE + iPhones proximos)".to_string(), "SEM botao SOS".to_string(), "SEM audio bidirecional".to_string(), "Nao funciona onde nao ha iPhone proximo".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Samsung".to_string(), modelo: "Galaxy SmartTag2".to_string(), categoria: CategoriaDispositivo::GpsTracker, preco_aprox_brl: 200.0, status: StatusSpec::Parcial, deficiencias_atendidas: vec![DeficienciaAlvo::Crianca], pontos_fortes: vec!["Custo baixo".to_string(), "Bateria 500 dias".to_string(), "Rede SmartThings Find".to_string(), "Botao (chama IFTTT)".to_string()], pontos_fracos: vec!["Sem GPS proprio (BLE)".to_string(), "Sem SOS direto".to_string(), "Sem audio bidirecional".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Tuya".to_string(), modelo: "Smart GPS Tracker (4G)".to_string(), categoria: CategoriaDispositivo::GpsTracker, preco_aprox_brl: 200.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Crianca, DeficienciaAlvo::Idoso], pontos_fortes: vec!["GPS REAL (com 4G)".to_string(), "Botao SOS".to_string(), "Audio bidirecional".to_string(), "Cerca virtual".to_string(), "Bateria 7-15 dias".to_string(), "Custo baixo".to_string()], pontos_fracos: vec!["Qualidade de build variavel".to_string(), "App generico (menos polido)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "GlobalSat".to_string(), modelo: "TR-600".to_string(), categoria: CategoriaDispositivo::GpsTracker, preco_aprox_brl: 600.0, status: StatusSpec::Conforme, deficiencias_atendidas: vec![DeficienciaAlvo::Crianca, DeficienciaAlvo::Idoso], pontos_fortes: vec!["GPS + 4G".to_string(), "Bateria 15 dias".to_string(), "SOS + audio".to_string(), "Cerca virtual".to_string(), "Industrial (resistente)".to_string()], pontos_fracos: vec!["Grande (nao discreto para crianca)".to_string()], notes: "".to_string() },
                ProdutoSuportado { marca: "Angel Watch".to_string(), modelo: "Angel Watch Co".to_string(), categoria: CategoriaDispositivo::GpsTracker, preco_aprox_brl: 1200.0, status: StatusSpec::Recomendado, deficiencias_atendidas: vec![DeficienciaAlvo::Crianca], pontos_fortes: vec!["RELOGIO GPS para crianca".to_string(), "GPS + 4G + WiFi".to_string(), "Chamada de voz (2 vias)".to_string(), "SOS".to_string(), "Cerca virtual".to_string(), "Videochamada".to_string()], pontos_fracos: vec!["Bateria 2-3 dias (smartwatch = curta)".to_string(), "Custo medio".to_string()], notes: "".to_string() },
            ],
            observacao: "GPS tracker e para QUEM NAO PODE PEDIR AJUDA. Crianca de 5 anos perdida no shopping nao liga para os pais. Idoso com Alzheimer nao lembra o proprio nome. Tracker = os pais ENCONTRAM sem depender do perdido. O Telefonista usa GPS do smartphone -- mas tracker dedicado e BACKUP.".to_string(),
        },
    ]
}

// ============================================================================
// 4. ENGINE
// ============================================================================

pub struct AccessibilityHardwareSpecEngine {
    pub specs: Vec<SpecDispositivo>,
}

impl AccessibilityHardwareSpecEngine {
    pub fn new() -> Self {
        AccessibilityHardwareSpecEngine {
            specs: init_specs(),
        }
    }

    // -- consulta ----------------------------------------------------------

    pub fn listar_categorias(&self) -> Vec<CategoriaDispositivo> {
        self.specs.iter().map(|s| s.categoria.clone()).collect()
    }

    pub fn spec_por_categoria(&self, cat: &CategoriaDispositivo) -> Option<&SpecDispositivo> {
        self.specs.iter().find(|s| &s.categoria == cat)
    }

    pub fn produtos_por_categoria(&self, cat: &CategoriaDispositivo) -> Vec<&ProdutoSuportado> {
        self.spec_por_categoria(cat)
            .map(|s| s.produtos.iter().collect())
            .unwrap_or_default()
    }

    pub fn produtos_por_deficiencia(
        &self,
        defic: &DeficienciaAlvo,
    ) -> Vec<(&ProdutoSuportado, &SpecDispositivo)> {
        let mut resultado = Vec::new();
        for s in &self.specs {
            for p in &s.produtos {
                if p.deficiencias_atendidas.contains(defic) {
                    resultado.push((p, s));
                }
            }
        }
        resultado
    }

    pub fn produtos_por_status(&self, status: &StatusSpec) -> Vec<&ProdutoSuportado> {
        let mut resultado = Vec::new();
        for s in &self.specs {
            for p in &s.produtos {
                if &p.status == status {
                    resultado.push(p);
                }
            }
        }
        resultado
    }

    pub fn produtos_recomendados(&self) -> Vec<&ProdutoSuportado> {
        self.produtos_por_status(&StatusSpec::Recomendado)
    }

    // -- verificar conformidade -------------------------------------------

    pub fn verificar_produto(
        &self,
        cat: &CategoriaDispositivo,
        _marca: &str,
        _modelo: &str,
        specs_atendidas: &HashMap<String, bool>,
    ) -> StatusSpec {
        let s = match self.spec_por_categoria(cat) {
            Some(spec) => spec,
            None => return StatusSpec::NaoConforme,
        };
        let obrigatorios: Vec<_> = s.specs.iter().filter(|spec| spec.obrigatorio).collect();
        let todos_atendidos = obrigatorios
            .iter()
            .all(|spec| specs_atendidas.get(&spec.parametro).copied().unwrap_or(false));
        if todos_atendidos {
            let opcionais: Vec<_> = s.specs.iter().filter(|spec| !spec.obrigatorio).collect();
            let opc_atendidos = opcionais
                .iter()
                .filter(|spec| specs_atendidas.get(&spec.parametro).copied().unwrap_or(false))
                .count();
            if opc_atendidos == opcionais.len() && !opcionais.is_empty() {
                return StatusSpec::Recomendado;
            }
            return StatusSpec::Conforme;
        }
        let falhas = obrigatorios
            .iter()
            .filter(|spec| !specs_atendidas.get(&spec.parametro).copied().unwrap_or(false))
            .count();
        if falhas <= 2 {
            StatusSpec::Parcial
        } else {
            StatusSpec::NaoConforme
        }
    }

    // -- catalogo por custo -----------------------------------------------

    pub fn catalogo_por_faixa_custo(&self) -> HashMap<String, Vec<&ProdutoSuportado>> {
        let mut resultado: HashMap<String, Vec<&ProdutoSuportado>> = HashMap::new();
        for s in &self.specs {
            for p in &s.produtos {
                let nivel = self.classificar_custo(p.preco_aprox_brl);
                resultado
                    .entry(nivel.rotulo().to_string())
                    .or_default()
                    .push(p);
            }
        }
        resultado
    }

    fn classificar_custo(&self, preco: f64) -> NivelCusto {
        for n in [
            NivelCusto::Gratuito,
            NivelCusto::Baixo,
            NivelCusto::Medio,
            NivelCusto::Alto,
            NivelCusto::Premium,
            NivelCusto::Especializado,
        ] {
            if (n.min_real() as f64) <= preco && preco <= (n.max_real() as f64) {
                return n;
            }
        }
        NivelCusto::Especializado
    }

    // -- scorecard ---------------------------------------------------------

    pub fn scorecard(&self) -> HashMap<String, i32> {
        let total_produtos: i32 = self.specs.iter().map(|s| s.produtos.len() as i32).sum();
        let recomendados = self.produtos_recomendados().len() as i32;
        let conformes = self.produtos_por_status(&StatusSpec::Conforme).len() as i32;
        let parciais = self.produtos_por_status(&StatusSpec::Parcial).len() as i32;
        let nao_conformes = self.produtos_por_status(&StatusSpec::NaoConforme).len() as i32;
        let total_specs: i32 = self.specs.iter().map(|s| s.specs.len() as i32).sum();
        let total_obrigatorias: i32 = self
            .specs
            .iter()
            .map(|s| s.specs.iter().filter(|sp| sp.obrigatorio).count() as i32)
            .sum();
        let mut map = HashMap::new();
        map.insert("categorias_dispositivos".to_string(), self.specs.len() as i32);
        map.insert("produtos_catalogados".to_string(), total_produtos);
        map.insert("produtos_recomendados".to_string(), recomendados);
        map.insert("produtos_conformes".to_string(), conformes);
        map.insert("produtos_parciais".to_string(), parciais);
        map.insert("produtos_nao_conformes".to_string(), nao_conformes);
        map.insert("specs_totais".to_string(), total_specs);
        map.insert("specs_obrigatorias".to_string(), total_obrigatorias);
        map.insert("deficiencias_cobertas".to_string(), 11);
        map
    }
}

// ============================================================================
// 5. DEMO (main equivalent)
// ============================================================================

fn main() {
    let e = AccessibilityHardwareSpecEngine::new();

    println!("{}", "=".repeat(70));
    println!("OpenAccessibilityHardwareSpecs -- Hardware COTS para Acessibilidade");
    println!("{}", "=".repeat(70));

    // --- Lista de categorias ---
    println!("\n[{} DISPOSITIVOS COTS ESPECIFICADOS]", e.specs.len());
    for s in &e.specs {
        let defs: Vec<_> = s.deficiencias_atendidas.iter().take(3).map(|d| d.rotulo()).collect();
        println!(
            "  {:.<35} Custo min: R$ {:.0}",
            s.categoria.rotulo(),
            s.custo_minimo_brl
        );
        println!("  {:35} Atende: {}...", "", defs.join(", "));
    }

    // --- Detalhe: Headphone Bluetooth ---
    println!("\n{}", "=".repeat(70));
    println!("[DETALHE] HEADPHONE BLUETOOTH -- Especificacoes");
    println!("{}", "=".repeat(70));
    if let Some(hp) = e.spec_por_categoria(&CategoriaDispositivo::HeadphoneBt) {
        println!("\n  Descricao: {}", hp.descricao);
        println!("\n  ESPECIFICACOES MINIMAS ({} specs):", hp.specs.len());
        for spec in &hp.specs {
            let flag = if spec.obrigatorio { "OBRIG" } else { "opc" };
            println!("    [{}] {}: {}", flag, spec.parametro, spec.valor_minimo);
            println!("          -> {}", spec.justificativa);
        }
        println!("\n  PRODUTOS SUPORTADOS ({}):", hp.produtos.len());
        for p in &hp.produtos {
            println!(
                "\n    [{}] {} {} -- R$ {:.0}",
                p.status.rotulo(),
                p.marca,
                p.modelo,
                p.preco_aprox_brl
            );
            println!("      Fortes: {}", p.pontos_fortes.iter().take(3).cloned().collect::<Vec<_>>().join(", "));
            println!("      Fracos: {}", p.pontos_fracos.iter().take(3).cloned().collect::<Vec<_>>().join(", "));
        }
    }

    // --- Catalogo completo ---
    println!("\n{}", "=".repeat(70));
    println!("[CATALOGO COMPLETO -- Todos os dispositivos e produtos]");
    println!("{}", "=".repeat(70));
    for s in &e.specs {
        println!("\n  --- {} ---", s.categoria.rotulo());
        for p in &s.produtos {
            let flag = match p.status.id() {
                "conforme" => "OK",
                "parcial" => "PARC",
                "nao_conforme" => "NAO",
                "recomendado" => "REC",
                _ => "?",
            };
            println!(
                "    [{}] {:<30} R$ {:>6.0}",
                flag, p.modelo, p.preco_aprox_brl
            );
        }
    }

    // --- Por deficiencia ---
    println!("\n{}", "=".repeat(70));
    println!("[PRODUTOS POR DEFICIENCIA]");
    println!("{}", "=".repeat(70));
    for defic in [
        DeficienciaAlvo::Cegueira,
        DeficienciaAlvo::Surdez,
        DeficienciaAlvo::Motora,
        DeficienciaAlvo::Cognitiva,
        DeficienciaAlvo::Autismo,
        DeficienciaAlvo::Tdah,
        DeficienciaAlvo::Comunicacao,
        DeficienciaAlvo::Neurologica,
        DeficienciaAlvo::Idoso,
        DeficienciaAlvo::Crianca,
        DeficienciaAlvo::Universal,
    ] {
        let prods = e.produtos_por_deficiencia(&defic);
        if !prods.is_empty() {
            let nomes: Vec<_> = prods
                .iter()
                .take(4)
                .map(|(p, _)| format!("{} {}", p.marca, p.modelo))
                .collect();
            println!("\n  {} ({} produtos):", defic.rotulo(), prods.len());
            for n in nomes {
                println!("    - {}", n);
            }
        }
    }

    // --- Catalogo por faixa de custo ---
    println!("\n{}", "=".repeat(70));
    println!("[CATALOGO POR FAIXA DE CUSTO]");
    println!("{}", "=".repeat(70));
    let cat = e.catalogo_por_faixa_custo();
    for (faixa, prods) in &cat {
        println!("\n  {} ({} produtos):", faixa, prods.len());
        for p in prods.iter().take(3) {
            println!("    - {} {} (R$ {:.0})", p.marca, p.modelo, p.preco_aprox_brl);
        }
    }

    // --- Scorecard ---
    println!("\n{}", "=".repeat(70));
    println!("[SCORECARD]");
    println!("{}", "=".repeat(70));
    let sc = e.scorecard();
    for (k, v) in &sc {
        println!("  {:.<30} {}", k, v);
    }

    // --- FILOSOFIA ---
    println!("\n{}", "=".repeat(70));
    println!("FILOSOFIA -- Dispositivos que nao precisam ser feitos do zero");
    println!("{}", "=".repeat(70));
    println!(
        r#"
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
"#
    );
}