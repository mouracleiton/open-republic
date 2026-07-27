// OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos do Corpo e da Civilizacao
// ============================================================================
// "Energia e a bateria do trabalho. Nada foi feito na Terra por humanos
// sem a necessidade de energia."
//
// O corpo humano nao tem UM sistema de energia. Tem DEZ.
// Cada um com input, conversao, output e residuo.
// A civilizacao herda essa estrutura.
//
// OpenEnergy cobre o sistema 1 (eletrico = ATP).
// Esta taxonomia revela os outros 9 -- e onde a Republica tem lacunas.
//
// A LEI QUE PERMEIA TODOS OS 10:
//   INPUT -> CONVERSAO -> OUTPUT -> RESIDUO
//   Nada se cria. Tudo se transforma.
//   Nao existe trabalho sem energia.
//   Nao existe energia sem input.
//   Nao existe output sem residuo.
//
// OS 10 SISTEMAS:
//   1. CELULAR (mitocondrial)  -- ATP, a moeda da celula
//   2. MECANICA (muscular)     -- movimento, trabalho fisico
//   3. TERMICA (metabolica)    -- calor, regulacao
//   4. NEURAL (sinal)          -- sistema nervoso, comunicacao
//   5. QUIMICA (sintese)       -- ligacoes, armazenamento molecular
//   6. SENSORIAL (transducao)  -- receptores, captura ambiental
//   7. COGNITIVA (processamento)-- cerebro, computacao
//   8. ATENCIONAL (foco)       -- atencao finita, budget cognitivo
//   9. EMOCIONAL (motivacao)   -- dopamina, drive, vontade
//   10. RELACIONAL (social)    -- conexao, co-regulacao, sinergia
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1: Cada tipo de energia e DIREITO. Nenhum e privilégio.
// - P2: Autonomia corporal inclui autonomia ENERGETICA (todos os 10 tipos).
// - P6: Acesso universal ao conhecimento = acesso a energia cognitiva/atencional.
// - P8: IA amplifica energia cognitiva, NAO substitui. Protege atencao humana.
//
// Author: OpenRepublic Team (transpilado de Python)

use std::collections::HashMap;
use std::fmt;

// ============================================================================
// 1. ENUMS (modulo-level)
// ============================================================================

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoEnergia {
    /// Os 10 sistemas energeticos do corpo e da civilizacao.
    CELULAR,
    MECANICA,
    TERMICA,
    NEURAL,
    QUIMICA,
    SENSORIAL,
    COGNITIVA,
    ATENCIONAL,
    EMOCIONAL,
    RELACIONAL,
}

impl TipoEnergia {
    pub fn id(&self) -> &'static str {
        match self {
            TipoEnergia::CELULAR => "celular",
            TipoEnergia::MECANICA => "mecanica",
            TipoEnergia::TERMICA => "termica",
            TipoEnergia::NEURAL => "neural",
            TipoEnergia::QUIMICA => "quimica",
            TipoEnergia::SENSORIAL => "sensorial",
            TipoEnergia::COGNITIVA => "cognitiva",
            TipoEnergia::ATENCIONAL => "atencional",
            TipoEnergia::EMOCIONAL => "emocional",
            TipoEnergia::RELACIONAL => "relacional",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoEnergia::CELULAR => "Energia Celular (mitocondrial)",
            TipoEnergia::MECANICA => "Energia Mecanica (muscular)",
            TipoEnergia::TERMICA => "Energia Termica (metabolica)",
            TipoEnergia::NEURAL => "Energia Neural (sinal)",
            TipoEnergia::QUIMICA => "Energia Quimica (sintese)",
            TipoEnergia::SENSORIAL => "Energia Sensorial (transducao)",
            TipoEnergia::COGNITIVA => "Energia Cognitiva (processamento)",
            TipoEnergia::ATENCIONAL => "Energia Atencional (foco)",
            TipoEnergia::EMOCIONAL => "Energia Emocional (motivacao)",
            TipoEnergia::RELACIONAL => "Energia Relacional (social)",
        }
    }

    pub fn numero(&self) -> i32 {
        match self {
            TipoEnergia::CELULAR => 1,
            TipoEnergia::MECANICA => 2,
            TipoEnergia::TERMICA => 3,
            TipoEnergia::NEURAL => 4,
            TipoEnergia::QUIMICA => 5,
            TipoEnergia::SENSORIAL => 6,
            TipoEnergia::COGNITIVA => 7,
            TipoEnergia::ATENCIONAL => 8,
            TipoEnergia::EMOCIONAL => 9,
            TipoEnergia::RELACIONAL => 10,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum EscalaEnergia {
    /// Em que nivel esta energia opera.
    CORPO,
    COMUNIDADE,
    CIVILIZACAO,
    PLANETA,
}

impl EscalaEnergia {
    pub fn id(&self) -> &'static str {
        match self {
            EscalaEnergia::CORPO => "corpo",
            EscalaEnergia::COMUNIDADE => "comunidade",
            EscalaEnergia::CIVILIZACAO => "civilizacao",
            EscalaEnergia::PLANETA => "planeta",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            EscalaEnergia::CORPO => "Nivel do corpo individual",
            EscalaEnergia::COMUNIDADE => "Nivel da comunidade/local",
            EscalaEnergia::CIVILIZACAO => "Nivel da civilizacao/global",
            EscalaEnergia::PLANETA => "Nivel planetario/biosfera",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum StatusDisponibilidade {
    /// Disponibilidade/estoque de um tipo de energia.
    ABUNDANTE,
    EQUILIBRADA,
    LIMITADA,
    CRITICA,
    DEPLETADA,
}

impl StatusDisponibilidade {
    pub fn id(&self) -> &'static str {
        match self {
            StatusDisponibilidade::ABUNDANTE => "abundante",
            StatusDisponibilidade::EQUILIBRADA => "equilibrada",
            StatusDisponibilidade::LIMITADA => "limitada",
            StatusDisponibilidade::CRITICA => "critica",
            StatusDisponibilidade::DEPLETADA => "depletada",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            StatusDisponibilidade::ABUNDANTE => "Abundante: excedente para doar",
            StatusDisponibilidade::EQUILIBRADA => "Equilibrada: cobre a demanda",
            StatusDisponibilidade::LIMITADA => "Limitada: alocacao necessaria",
            StatusDisponibilidade::CRITICA => "Critica: deficit, intervene",
            StatusDisponibilidade::DEPLETADA => "Depletada: esgotada, recuperacao obrigatoria",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum NivelCobertura {
    /// Quanto da Republica cobre este tipo de energia.
    COBERTO,
    PARCIAL,
    LACUNA,
    NAO_APLICAVEL,
}

impl NivelCobertura {
    pub fn id(&self) -> &'static str {
        match self {
            NivelCobertura::COBERTO => "coberto",
            NivelCobertura::PARCIAL => "parcial",
            NivelCobertura::LACUNA => "lacuna",
            NivelCobertura::NAO_APLICAVEL => "nao_aplicavel",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            NivelCobertura::COBERTO => "Totalmente coberto por modulo(s) existente(s)",
            NivelCobertura::PARCIAL => "Parcialmente coberto -- lacunas identificadas",
            NivelCobertura::LACUNA => "Lacuna: nenhum modulo cobre este tipo",
            NivelCobertura::NAO_APLICAVEL => "Nao aplicavel (conceitual)",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoInput {
    /// Categorias de input energetico (o que alimenta cada sistema).
    ALIMENTO,
    OXIGENIO,
    LUZ,
    SOM,
    CALOR_AMBIENTE,
    PRESENCA,
    INFORMACAO,
    SONO,
    MOVIMENTO_CORPO,
    VENTO_AGUA,
}

impl TipoInput {
    pub fn id(&self) -> &'static str {
        match self {
            TipoInput::ALIMENTO => "alimento",
            TipoInput::OXIGENIO => "oxigenio",
            TipoInput::LUZ => "luz",
            TipoInput::SOM => "som",
            TipoInput::CALOR_AMBIENTE => "calor",
            TipoInput::PRESENCA => "presenca",
            TipoInput::INFORMACAO => "informacao",
            TipoInput::SONO => "sono",
            TipoInput::MOVIMENTO_CORPO => "movimento",
            TipoInput::VENTO_AGUA => "vento_agua",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoInput::ALIMENTO => "Alimento/caloria (comida, combustivel)",
            TipoInput::OXIGENIO => "Oxigenio/ar",
            TipoInput::LUZ => "Luz/fotons",
            TipoInput::SOM => "Som/vibracao",
            TipoInput::CALOR_AMBIENTE => "Calor ambiental",
            TipoInput::PRESENCA => "Presenca de outro ser humano",
            TipoInput::INFORMACAO => "Informacao/dados",
            TipoInput::SONO => "Sono/descanso",
            TipoInput::MOVIMENTO_CORPO => "Movimento do proprio corpo",
            TipoInput::VENTO_AGUA => "Vento, agua, forcas naturais",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoResiduo {
    /// O que cada sistema energetico produz como residuo (2a lei).
    CALOR,
    CO2,
    CANSACO_FISICO,
    FADIGA_MENTAL,
    DESGASTE_MATERIAL,
    RUIDO,
    SOLIDAO,
    RESIDUO_TOXICO,
    DADOS_DESCARTADOS,
}

impl TipoResiduo {
    pub fn id(&self) -> &'static str {
        match self {
            TipoResiduo::CALOR => "calor",
            TipoResiduo::CO2 => "co2",
            TipoResiduo::CANSACO_FISICO => "cansaco_fisico",
            TipoResiduo::FADIGA_MENTAL => "fadiga_mental",
            TipoResiduo::DESGASTE_MATERIAL => "desgaste",
            TipoResiduo::RUIDO => "ruido",
            TipoResiduo::SOLIDAO => "solidao",
            TipoResiduo::RESIDUO_TOXICO => "residuo_toxico",
            TipoResiduo::DADOS_DESCARTADOS => "dados_descartados",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoResiduo::CALOR => "Calor dissipado",
            TipoResiduo::CO2 => "CO2 / gases de exaustao",
            TipoResiduo::CANSACO_FISICO => "Cansaco fisico / acido latico",
            TipoResiduo::FADIGA_MENTAL => "Fadiga mental / saturacao",
            TipoResiduo::DESGASTE_MATERIAL => "Desgaste material (atriito, envelhecimento)",
            TipoResiduo::RUIDO => "Ruido (sonoro, visual, informational)",
            TipoResiduo::SOLIDAO => "Solidao (quando a conexao termina)",
            TipoResiduo::RESIDUO_TOXICO => "Residuo toxico (quimico, radiativo)",
            TipoResiduo::DADOS_DESCARTADOS => "Dados descartados (log, cache)",
        }
    }
}

// ============================================================================
// 2. STRUCTS (dataclasses)
// ============================================================================

#[derive(Debug, Clone)]
pub struct FluxoEnergetico {
    /// Estrutura universal: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO.
    pub inputs: Vec<TipoInput>,
    pub conversao: String,        // como se converte input em output
    pub output: String,           // o que o sistema PRODUZ
    pub residuos: Vec<TipoResiduo>,
    pub eficiencia_pct: f64,      // % do input que vira output util
}

impl Default for FluxoEnergetico {
    fn default() -> Self {
        FluxoEnergetico {
            inputs: Vec::new(),
            conversao: String::new(),
            output: String::new(),
            residuos: Vec::new(),
            eficiencia_pct: 100.0,
        }
    }
}

#[derive(Debug, Clone)]
pub struct SistemaEnergetico {
    /// Um dos 10 sistemas de energia, com mapeamento corpo <-> civilizacao.
    pub tipo: TipoEnergia,
    pub nome: String,
    pub analogia_corpo: String,        // como funciona no corpo humano
    pub analogia_civilizacao: String,  // como funciona na civilizacao
    pub escala: EscalaEnergia,
    pub fluxo: FluxoEnergetico,
    pub consumo_corpo_pct: f64,        // % do orcamento energetico do corpo (se aplicavel)
    pub observacao: String,
}

#[derive(Debug, Clone)]
pub struct CoberturaRepublica {
    /// Quais modulos da Republica cobrem cada tipo de energia.
    pub tipo: TipoEnergia,
    pub nivel: NivelCobertura,
    pub modulos: Vec<String>,          // modulos que cobrem
    pub lacunas: Vec<String>,          // o que falta
}

#[derive(Debug, Clone)]
pub struct DiagnosticoEnergetico {
    /// Snapshot da saude energetica de uma pessoa ou comunidade.
    pub entidade: String, // "pessoa:Maria" ou "comunidade:Solar Village"
    pub status_por_tipo: HashMap<String, StatusDisponibilidade>,
    pub tipos_em_deficit: Vec<TipoEnergia>,
    pub tipos_abundantes: Vec<TipoEnergia>,
    pub veredito: String,
}

// ============================================================================
// 3. OS 10 SISTEMAS (dados canonicos)
// ============================================================================

fn init_sistemas() -> Vec<SistemaEnergetico> {
    /// Cria os 10 sistemas energeticos com dados completos.
    vec![
        SistemaEnergetico {
            tipo: TipoEnergia::CELULAR,
            nome: "Mitocondrial".to_string(),
            analogia_corpo: "Mitocondrias convertem glicose + oxigenio em ATP. ATP e a MOEDA energetica da celula -- todo trabalho celular paga em ATP. Sem ATP, a celula morre em segundos.".to_string(),
            analogia_civilizacao: "A rede eletrica. A tomada e o ATP da civilizacao. Todo aparelho, toda maquina, todo servo consome eletricidade. OpenEnergy cobre este sistema.".to_string(),
            escala: EscalaEnergia::CIVILIZACAO,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::ALIMENTO, TipoInput::OXIGENIO],
                conversao: "Glicose + O2 -> ATP (fosforilacao oxidativa)".to_string(),
                output: "ATP (trifosfato de adenosina) / Eletricidade".to_string(),
                residuos: vec![TipoResiduo::CO2, TipoResiduo::CALOR],
                eficiencia_pct: 40.0,
            },
            consumo_corpo_pct: 0.0,
            observacao: "Sistema base. Todos os outros dependem deste. OpenEnergy = cobertura total deste nivel.".to_string(),
        },
        SistemaEnergetico {
            tipo: TipoEnergia::MECANICA,
            nome: "Muscular / Motora".to_string(),
            analogia_corpo: "ATP -> miosina/actina -> contracao muscular -> MOVIMENTO. O corpo faz TRABALHO FISICO sobre o mundo. Cada passo, cada gesto, cada levantamento de peso.".to_string(),
            analogia_civilizacao: "Transporte, maquinas, ferramentas, robos. O motor de carro, o braco robotico, a bicicleta. Todo trabalho fisico ja existiu como energia muscular antes de ser externalizado para maquinas.".to_string(),
            escala: EscalaEnergia::CIVILIZACAO,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::ALIMENTO, TipoInput::MOVIMENTO_CORPO],
                conversao: "ATP -> forca mecanica (contracao / combustao / eletricidade)".to_string(),
                output: "Movimento, forca, deslocamento".to_string(),
                residuos: vec![TipoResiduo::CANSACO_FISICO, TipoResiduo::CALOR, TipoResiduo::CO2],
                eficiencia_pct: 25.0,
            },
            consumo_corpo_pct: 30.0,
            observacao: "OpenAthlete cobre o lado humano (esporte, treino). Transporte publico (OpenMobility) cobre o lado civilizacional.".to_string(),
        },
        SistemaEnergetico {
            tipo: TipoEnergia::TERMICA,
            nome: "Metabolica / Calorica".to_string(),
            analogia_corpo: "O metabolismo produz calor como subproduto. O corpo GASTA energia mantendo 36,5C -- termorregulacao. Tremer de frio e gerar calor muscular. Suar e dissipar.".to_string(),
            analogia_civilizacao: "Aquecimento, cozimento, refrigeracao. O FOGO foi a primeira energia externa que o humano dominou (1 milhao de anos antes da eletricidade). Cozinhar e PRE-DIGERIR com energia termica externa -- libera energia celular que iria pra digestao.".to_string(),
            escala: EscalaEnergia::CIVILIZACAO,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::ALIMENTO, TipoInput::CALOR_AMBIENTE],
                conversao: "Metabolismo / combustao / compressao -> calor".to_string(),
                output: "Calor (manutencao de temperatura / cozimento)".to_string(),
                residuos: vec![TipoResiduo::CALOR, TipoResiduo::CO2],
                eficiencia_pct: 60.0,
            },
            consumo_corpo_pct: 50.0,
            observacao: "Metabolismo basal: 50% do gasto energetico do corpo em repouso e so para manter a temperatura. O cozimento de alimentos foi a REVOLUCAO ENERGETICA original da humanidade.".to_string(),
        },
        SistemaEnergetico {
            tipo: TipoEnergia::NEURAL,
            nome: "Sistema Nervoso / Comunicacao".to_string(),
            analogia_corpo: "Neuronios disparam potenciais de acao -- sinais eletricos. O corpo tem uma REDE de comunicacao interna (87 bilhoes de neuronios). Consome 20W, incrivelmente eficiente. O cerebro pesa 2% do corpo mas consome 20% da energia.".to_string(),
            analogia_civilizacao: "Internet, telecomunicacoes, radio. A internet e o SISTEMA NERVO da civilizacao. Cada mensagem, cada video, cada chamada e um potencial de acao em escala planetaria. Banda = largura de axonio.".to_string(),
            escala: EscalaEnergia::PLANETA,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::INFORMACAO, TipoInput::LUZ],
                conversao: "Sinal eletrico / optico -> transmissao".to_string(),
                output: "Comunicacao / sinal / dados transmitidos".to_string(),
                residuos: vec![TipoResiduo::RUIDO, TipoResiduo::CALOR, TipoResiduo::DADOS_DESCARTADOS],
                eficiencia_pct: 35.0,
            },
            consumo_corpo_pct: 20.0,
            observacao: "LACUNA CRITICA: a Republica NAO tem OpenNetwork/OpenInternet. Quem controla a rede controla o sistema nervoso. Banda gratuita e NECESSARIA (energia neural = direito).".to_string(),
        },
        SistemaEnergetico {
            tipo: TipoEnergia::QUIMICA,
            nome: "Sintese / Ligacoes".to_string(),
            analogia_corpo: "O corpo SINTETIZA moleculas -- proteinas, hormonios, enzimas. Ligacoes quimicas ARMAZENAM energia. Digestao = quebrar ligacoes para liberar. Sintese = gastar energia para construir.".to_string(),
            analogia_civilizacao: "Industria quimica, baterias, combustiveis, farmacia. Toda manufatura e energia quimica direcionada. FarmLab opera aqui -- sintese de medicamentos e energia quimica a servico da vida.".to_string(),
            escala: EscalaEnergia::CIVILIZACAO,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::ALIMENTO],
                conversao: "Reacao quimica (sintese / decomposicao)".to_string(),
                output: "Moleculas / materiais / medicamentos".to_string(),
                residuos: vec![TipoResiduo::RESIDUO_TOXICO, TipoResiduo::CALOR],
                eficiencia_pct: 30.0,
            },
            consumo_corpo_pct: 10.0,
            observacao: "FarmLab cobre farmacia. OpenChemistry cobre industria quimica.".to_string(),
        },
        SistemaEnergetico {
            tipo: TipoEnergia::SENSORIAL,
            nome: "Transducao / Percepcao".to_string(),
            analogia_corpo: "Olhos capturam FOTONS. Ouvidos capturam VIBRACOES. Pele captura CALOR. O corpo e um RECEPTOR de energia -- converte formas externas em sinais internos. Cada sentido e um TRANSDUTOR energetico.".to_string(),
            analogia_civilizacao: "Cameras, microfones, sensores, instrumentos cientificos. OpenTelefonista opera aqui -- o smartphone como CORPO ESTENDIDO captura energia do ambiente (luz, som, posicao) e converte em percepcao. Cego ve obstaculos. Surdo le labios.".to_string(),
            escala: EscalaEnergia::CORPO,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::LUZ, TipoInput::SOM, TipoInput::CALOR_AMBIENTE],
                conversao: "Transducao sensorial (foton/fonon -> sinal neural)".to_string(),
                output: "Percepcao / dados sensoriais".to_string(),
                residuos: vec![TipoResiduo::RUIDO, TipoResiduo::FADIGA_MENTAL],
                eficiencia_pct: 70.0,
            },
            consumo_corpo_pct: 5.0,
            observacao: "OpenTelefonista cobre (smartphone como corpo estendido). OpenInclusiveHardware (44 dispositivos) amplia. OpenInclusiveIDE integra para desenvolvimento.".to_string(),
        },
        SistemaEnergetico {
            tipo: TipoEnergia::COGNITIVA,
            nome: "Cerebro / Processamento".to_string(),
            analogia_corpo: "O cerebro CONSOME 20% da energia do corpo pesando 2%. PENSAR E CARO energeticamente. O cansaco mental e real -- e gasto energetico, nao frescura. Resolver um problema matematico gasta mais glicose que assistir TV.".to_string(),
            analogia_civilizacao: "Computacao, IA, analise de dados. Um data center consome tanta energia quanto uma cidade. Processar informacao TEM CUSTO ENERGETICO -- nao e gratuito. P8: IA amplifica inteligencia humana, NAO substitui. Mas o custo de computar e REAL e precisa alocacao.".to_string(),
            escala: EscalaEnergia::CIVILIZACAO,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::INFORMACAO, TipoInput::ALIMENTO],
                conversao: "Processamento (neural / digital)".to_string(),
                output: "Decisao / calculo / conhecimento".to_string(),
                residuos: vec![TipoResiduo::FADIGA_MENTAL, TipoResiduo::CALOR, TipoResiduo::DADOS_DESCARTADOS],
                eficiencia_pct: 15.0,
            },
            consumo_corpo_pct: 20.0,
            observacao: "HumanKnowledge (multi-AI + verificacao) cobre parcialmente. P8 define o principio (IA = instrumento). Custo computacional como recurso a alocar = LACUNA.".to_string(),
        },
        SistemaEnergetico {
            tipo: TipoEnergia::ATENCIONAL,
            nome: "Foco / Atencao".to_string(),
            analogia_corpo: "A atencao e FINITA. Voce nao consegue focar em tudo. Focar GASTA energia cognitiva. O cerebro tem um BUDGET de atencao -- distribui entre tarefas. Dormir mal = budget de atencao menor no dia seguinte.".to_string(),
            analogia_civilizacao: "A energia que FocusGuard protege. O scroll infinito DRENA energia atencional. A 'economia da atencao' e a forma mais NOVA de exploracao energetica -- plataformas capturam sua atencao e vendem. P8 exige proteger esta energia. AntiSpamCall protege parcialmente.".to_string(),
            escala: EscalaEnergia::CORPO,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::SONO, TipoInput::INFORMACAO],
                conversao: "Filtro atencional (top-down + bottom-up)".to_string(),
                output: "Foco / atencao direcionada".to_string(),
                residuos: vec![TipoResiduo::FADIGA_MENTAL, TipoResiduo::RUIDO],
                eficiencia_pct: 10.0,
            },
            consumo_corpo_pct: 0.0,
            observacao: "FocusGuard (overlay IDE) cobre parcialmente. AntiSpamCall ('para de me encher o saco') protege. OpenContentPolicy (midia, ruido) protege. Politica mais ampla de atencao como recurso energetico finito = LACUNA.".to_string(),
        },
        SistemaEnergetico {
            tipo: TipoEnergia::EMOCIONAL,
            nome: "Motivacao / Drive".to_string(),
            analogia_corpo: "Motivacao, drive, vontade. Em termos fisicos: dopamina, noradrenalina, cortisol -- moleculas que MODULAM quanto de outras energias o corpo vai despender. Sem dopamina, o corpo tem ATP mas nao se MOVE. A depressao e crise energetica emocional -- o combustivel existe, mas o motor nao liga.".to_string(),
            analogia_civilizacao: "O kaizen (1% ao dia) opera aqui. Curiosidade, progresso, desafio, recompensa, pertencimento -- os 5 gatilhos psicologicos sao GERADORES de energia emocional. O Huxley soma (dopamina artificial do scroll) e o SEQUESTRO desta energia -- drena ao inves de gerar.".to_string(),
            escala: EscalaEnergia::COMUNIDADE,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::PRESENCA, TipoInput::SONO, TipoInput::INFORMACAO],
                conversao: "Modulacao neuroquimica (dopamina/serotonina/cortisol)".to_string(),
                output: "Motivacao / drive / vontade de agir".to_string(),
                residuos: vec![TipoResiduo::SOLIDAO, TipoResiduo::FADIGA_MENTAL],
                eficiencia_pct: 20.0,
            },
            consumo_corpo_pct: 0.0,
            observacao: "LACUNA CRITICA: nenhum modulo trata saude mental como INFRAESTRUTURA ENERGETICA. Depressao = deficit energetico. Burnout = deplecao. Kaizen e gerador, mas falta sistema.".to_string(),
        },
        SistemaEnergetico {
            tipo: TipoEnergia::RELACIONAL,
            nome: "Social / Conexao".to_string(),
            analogia_corpo: "O ser humano isolado DEGRADA. Solidao cronica aumenta mortalidade em 26%. O corpo PRECISA de conexao para funcionar bem -- nao e luxo, e necessidade energetica. Oxitocina, espelhamento neural, co-regulacao.".to_string(),
            analogia_civilizacao: "A assembleia, o mutirao, a cooperativa. O Two-Person Rule nao e so procedimento -- e ARQUITETURA ENERGETICA. Duas pessoas juntas fazem mais que duas separadas. A energia social e SINERGICA: 1+1 > 2. Quando a assembleia polariza (P9), e esta energia que se GASTA em atrito em vez de gerar valor.".to_string(),
            escala: EscalaEnergia::COMUNIDADE,
            fluxo: FluxoEnergetico {
                inputs: vec![TipoInput::PRESENCA],
                conversao: "Co-regulacao neuroquimica + espelhamento neural".to_string(),
                output: "Cooperacao / sinergia / vinculo".to_string(),
                residuos: vec![TipoResiduo::SOLIDAO],
                eficiencia_pct: 80.0,
            },
            consumo_corpo_pct: 0.0,
            observacao: "OpenCommunities (6 adaptacoes) cobre parcialmente. OpenConstituentAssembly (governanca) cobre parcialmente. OpenCrowdsourcing (ajuda mutua) cobre parcialmente. P9 (anti-polarizacao) PROTEGE esta energia. Tratar conexao como recurso energetico mensuravel = LACUNA.".to_string(),
        },
    ]
}

fn init_coberturas() -> Vec<CoberturaRepublica> {
    /// Mapeia quais modulos cobrem cada tipo de energia.
    vec![
        CoberturaRepublica {
            tipo: TipoEnergia::CELULAR,
            nivel: NivelCobertura::COBERTO,
            modulos: vec!["open-energy".to_string(), "open-agrarian-revolution".to_string(), "open-credit".to_string()],
            lacunas: vec![],
        },
        CoberturaRepublica {
            tipo: TipoEnergia::MECANICA,
            nivel: NivelCobertura::PARCIAL,
            modulos: vec!["open-athlete".to_string(), "open-martial-arts".to_string()],
            lacunas: vec!["sistema de transporte publico gratuito (OpenMobility)".to_string()],
        },
        CoberturaRepublica {
            tipo: TipoEnergia::TERMICA,
            nivel: NivelCobertura::PARCIAL,
            modulos: vec!["open-energy".to_string()],
            lacunas: vec!["politica de cozimento comunitario".to_string(), "aquecimento como direito".to_string()],
        },
        CoberturaRepublica {
            tipo: TipoEnergia::NEURAL,
            nivel: NivelCobertura::LACUNA,
            modulos: vec![],
            lacunas: vec![
                "OpenNetwork/OpenInternet -- banda gratuita como direito".to_string(),
                "sistema nervoso da civilizacao sem dono".to_string(),
                "neutralidade de rede como P1 (anti-elitismo)".to_string(),
            ],
        },
        CoberturaRepublica {
            tipo: TipoEnergia::QUIMICA,
            nivel: NivelCobertura::PARCIAL,
            modulos: vec!["open-chemistry".to_string(), "open-physics".to_string()],
            lacunas: vec!["FarmLab completo (sintese CC0 de medicamentos)".to_string()],
        },
        CoberturaRepublica {
            tipo: TipoEnergia::SENSORIAL,
            nivel: NivelCobertura::COBERTO,
            modulos: vec!["open-telefonista".to_string(), "open-inclusive-hardware".to_string(), "open-inclusive-ide".to_string()],
            lacunas: vec![],
        },
        CoberturaRepublica {
            tipo: TipoEnergia::COGNITIVA,
            nivel: NivelCobertura::PARCIAL,
            modulos: vec!["open-human-knowledge".to_string(), "open-human-amplification".to_string()],
            lacunas: vec!["alocacao de custo computacional como recurso energetico".to_string()],
        },
        CoberturaRepublica {
            tipo: TipoEnergia::ATENCIONAL,
            nivel: NivelCobertura::PARCIAL,
            modulos: vec!["open-focus-guard".to_string(), "open-anti-spam-call".to_string(), "open-content-policy".to_string()],
            lacunas: vec!["politica ampla de atencao como recurso energetico finito".to_string()],
        },
        CoberturaRepublica {
            tipo: TipoEnergia::EMOCIONAL,
            nivel: NivelCobertura::LACUNA,
            modulos: vec![],
            lacunas: vec![
                "OpenMentalHealth -- saude mental como INFRAESTRUTURA ENERGETICA".to_string(),
                "sistema de deteccao de deplecao emocional (burnout/depressao)".to_string(),
                "geradores de energia emocional (kaizen, pertencimento, proposito)".to_string(),
            ],
        },
        CoberturaRepublica {
            tipo: TipoEnergia::RELACIONAL,
            nivel: NivelCobertura::PARCIAL,
            modulos: vec!["open-communities".to_string(), "open-constituent-assembly".to_string(), "open-anti-polarization".to_string()],
            lacunas: vec!["conexao como recurso energetico mensuravel e protegido".to_string()],
        },
    ]
}

// ============================================================================
// 4. ENGINE
// ============================================================================

pub struct EnergyTaxonomyEngine {
    /// Motor da Taxonomia Energetica: os 10 sistemas, coberturas, diagnosticos.
    pub sistemas: Vec<SistemaEnergetico>,
    pub coberturas: Vec<CoberturaRepublica>,
    pub diagnosticos: HashMap<String, DiagnosticoEnergetico>,
}

impl EnergyTaxonomyEngine {
    pub fn new() -> Self {
        EnergyTaxonomyEngine {
            sistemas: init_sistemas(),
            coberturas: init_coberturas(),
            diagnosticos: HashMap::new(),
        }
    }

    // -- consulta ----------------------------------------------------------

    pub fn listar_sistemas(&self) -> Vec<&SistemaEnergetico> {
        let mut sistemas: Vec<&SistemaEnergetico> = self.sistemas.iter().collect();
        sistemas.sort_by_key(|s| s.tipo.numero());
        sistemas
    }

    pub fn sistema_por_tipo(&self, tipo: &TipoEnergia) -> Option<&SistemaEnergetico> {
        self.sistemas.iter().find(|s| s.tipo == *tipo)
    }

    pub fn coberturas_por_nivel(&self, nivel: &NivelCobertura) -> Vec<&CoberturaRepublica> {
        self.coberturas.iter().filter(|c| c.nivel == *nivel).collect()
    }

    pub fn lacunas_identificadas(&self) -> Vec<(TipoEnergia, Vec<String>)> {
        /// Retorna tipos com lacunas e o que falta.
        self.coberturas
            .iter()
            .filter(|c| c.nivel == NivelCobertura::LACUNA || c.nivel == NivelCobertura::PARCIAL)
            .map(|c| (c.tipo.clone(), c.lacunas.clone()))
            .collect()
    }

    // -- diagnostico -------------------------------------------------------

    pub fn diagnosticar(
        &mut self,
        entidade: &str,
        status: HashMap<TipoEnergia, StatusDisponibilidade>,
    ) -> DiagnosticoEnergetico {
        /// Produz diagnostico energetico de uma pessoa ou comunidade.
        let mut status_por_id = HashMap::new();
        for (t, s) in &status {
            status_por_id.insert(t.id().to_string(), s.clone());
        }

        let mut em_deficit = Vec::new();
        let mut abundantes = Vec::new();
        for (t, s) in &status {
            if *s == StatusDisponibilidade::LIMITADA
                || *s == StatusDisponibilidade::CRITICA
                || *s == StatusDisponibilidade::DEPLETADA
            {
                em_deficit.push(t.clone());
            }
            if *s == StatusDisponibilidade::ABUNDANTE {
                abundantes.push(t.clone());
            }
        }

        let veredito = if em_deficit.len() >= 4 {
            "CRITICO: multiplas deficiencias energeticas. Intervencao sistemica.".to_string()
        } else if em_deficit.len() >= 2 {
            "ATENCAO: deficiencias energeticas em sistemas chave.".to_string()
        } else if !em_deficit.is_empty() {
            let nomes: Vec<String> = em_deficit
                .iter()
                .map(|t| t.rotulo().split('(').next().unwrap_or("").trim().to_string())
                .collect();
            format!("DEFICIT LOCAL: {}. Tratar antes de propagar.", nomes.join(", "))
        } else {
            "SAUDAVEL: todos os sistemas energeticos em equilibrio ou abundancia.".to_string()
        };

        let diag = DiagnosticoEnergetico {
            entidade: entidade.to_string(),
            status_por_tipo: status_por_id,
            tipos_em_deficit: em_deficit,
            tipos_abundantes: abundantes,
            veredito,
        };
        self.diagnosticos.insert(entidade.to_string(), diag.clone());
        diag
    }

    // -- padrao universal --------------------------------------------------

    pub fn padrao_universal(&self) -> String {
        /// A lei que permeia todos os 10 sistemas.
        "PADRAO UNIVERSAL: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO\n\
         Nada se cria. Tudo se transforma.\n\
         Nao existe trabalho sem energia.\n\
         Nao existe energia sem input.\n\
         Nao existe output sem residuo.\n\
         A questao civilizatoria nunca foi 'como conseguir energia' \
         -- sempre foi 'como TRANSFORMAR com justica e sem desperdicar'."
            .to_string()
    }

    // -- scorecard ---------------------------------------------------------

    pub fn scorecard(&self) -> HashMap<String, String> {
        let total = self.sistemas.len();
        let cobertos = self.coberturas_por_nivel(&NivelCobertura::COBERTO).len();
        let parciais = self.coberturas_por_nivel(&NivelCobertura::PARCIAL).len();
        let lacunas = self.coberturas_por_nivel(&NivelCobertura::LACUNA).len();
        let total_lacunas_itens: usize = self.coberturas.iter().map(|c| c.lacunas.len()).sum();
        let pct_coberto = if total > 0 {
            (cobertos as f64 / total as f64 * 100.0).round()
        } else {
            0.0
        };

        let mut map = HashMap::new();
        map.insert("sistemas_total".to_string(), total.to_string());
        map.insert("totalmente_cobertos".to_string(), cobertos.to_string());
        map.insert("parcialmente_cobertos".to_string(), parciais.to_string());
        map.insert("lacunas_criticas".to_string(), lacunas.to_string());
        map.insert("itens_faltantes".to_string(), total_lacunas_itens.to_string());
        map.insert("pct_cobertura".to_string(), format!("{:.1}", pct_coberto));
        map.insert("diagnosticos_realizados".to_string(), self.diagnosticos.len().to_string());
        map
    }
}

// ============================================================================
// 5. DEMO (main)
// ============================================================================

fn main() {
    let mut e = EnergyTaxonomyEngine::new();

    println!("{}", "=".repeat(70));
    println!("OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos");
    println!("Do Corpo Humano a Civilizacao");
    println!("{}", "=".repeat(70));

    // --- Os 10 sistemas ---
    println!("\n[OS 10 SISTEMAS ENERGETICOS]");
    for s in e.listar_sistemas() {
        println!("\n  --- Sistema {}: {} ---", s.tipo.numero(), s.tipo.rotulo());
        println!("  Escala: {}", s.escala.rotulo());
        println!("  CORPO: {}", s.analogia_corpo);
        println!("  CIVILIZACAO: {}", s.analogia_civilizacao);
        if s.consumo_corpo_pct > 0.0 {
            println!("  Consumo no corpo: {}% do orcamento energetico", s.consumo_corpo_pct);
        }
        let f = &s.fluxo;
        let inputs: Vec<&str> = f.inputs.iter().map(|i| i.rotulo()).collect();
        println!("  FLUXO: {:?} -> {}", inputs, f.conversao);
        println!("         -> {}", f.output);
        let residuos: Vec<&str> = f.residuos.iter().map(|r| r.rotulo()).collect();
        println!("         -> RESIDUO: {:?}", residuos);
        println!("  EFICIENCIA: {}%", f.eficiencia_pct);
        if !s.observacao.is_empty() {
            println!("  OBS: {}", s.observacao);
        }
    }

    // --- Padrao universal ---
    println!("\n{}", "=".repeat(70));
    println!("[O PADRAO UNIVERSAL]");
    println!("{}", "=".repeat(70));
    println!("\n{}", e.padrao_universal());

    // --- Exemplo: cada sistema em uma linha ---
    println!("\n[EXEMPLOS CORPO -> CIVILIZACAO]");
    for s in e.listar_sistemas() {
        let corpo_curto = s.analogia_corpo.split('.').next().unwrap_or("").trim();
        let civ_curto = s.analogia_civilizacao.split('.').next().unwrap_or("").trim();
        println!("  {:2}. {}", s.tipo.numero(), s.tipo.rotulo());
        println!("      Corpo: {}", corpo_curto);
        println!("      Civil: {}", civ_curto);
    }

    // --- Cobertura da Republica ---
    println!("\n{}", "=".repeat(70));
    println!("[COBERTURA DA REPUBLICA -- O QUE FALTA]");
    println!("{}", "=".repeat(70));
    for c in &e.coberturas {
        let flag = match c.nivel.id() {
            "coberto" => "OK",
            "parcial" => "PARCIAL",
            "lacuna" => "LACUNA",
            _ => "N/A",
        };
        println!("\n  [{}] {}", flag, c.tipo.rotulo());
        if !c.modulos.is_empty() {
            println!("  Modulos: {}", c.modulos.join(", "));
        }
        if !c.lacunas.is_empty() {
            println!("  LACUNAS:");
            for lac in &c.lacunas {
                println!("    - {}", lac);
            }
        }
    }

    // --- Lacunas criticas ---
    println!("\n{}", "=".repeat(70));
    println!("[LACUNAS CRITICAS -- MODULOS QUE PRECISAM EXISTIR]");
    println!("{}", "=".repeat(70));
    let lacunas = e.coberturas_por_nivel(&NivelCobertura::LACUNA);
    for c in &lacunas {
        println!("\n  {}:", c.tipo.rotulo());
        for lac in &c.lacunas {
            println!("    - {}", lac);
        }
    }
    if lacunas.is_empty() {
        println!("  (nenhuma lacuna critica)");
    }

    // --- Diagnostico de exemplo ---
    println!("\n{}", "=".repeat(70));
    println!("[DIAGNOSTICO ENERGETICO -- Pessoa: Maria]");
    println!("{}", "=".repeat(70));

    let mut status_maria = HashMap::new();
    status_maria.insert(TipoEnergia::CELULAR, StatusDisponibilidade::EQUILIBRADA);
    status_maria.insert(TipoEnergia::MECANICA, StatusDisponibilidade::EQUILIBRADA);
    status_maria.insert(TipoEnergia::TERMICA, StatusDisponibilidade::ABUNDANTE);
    status_maria.insert(TipoEnergia::NEURAL, StatusDisponibilidade::ABUNDANTE);
    status_maria.insert(TipoEnergia::QUIMICA, StatusDisponibilidade::EQUILIBRADA);
    status_maria.insert(TipoEnergia::SENSORIAL, StatusDisponibilidade::EQUILIBRADA);
    status_maria.insert(TipoEnergia::COGNITIVA, StatusDisponibilidade::LIMITADA);
    status_maria.insert(TipoEnergia::ATENCIONAL, StatusDisponibilidade::CRITICA);
    status_maria.insert(TipoEnergia::EMOCIONAL, StatusDisponibilidade::DEPLETADA);
    status_maria.insert(TipoEnergia::RELACIONAL, StatusDisponibilidade::EQUILIBRADA);

    let diag_maria = e.diagnosticar("pessoa:Maria", status_maria);
    println!("  Entidade: {}", diag_maria.entidade);
    let mut sorted_status: Vec<_> = diag_maria.status_por_tipo.iter().collect();
    sorted_status.sort_by_key(|(k, _)| k.as_str());
    for (tid, st) in sorted_status {
        println!("    {:.<20} {:?}", tid, st);
    }
    let deficit_nomes: Vec<String> = diag_maria
        .tipos_em_deficit
        .iter()
        .map(|t| t.rotulo().split('(').next().unwrap_or("").trim().to_string())
        .collect();
    println!("  Em deficit: {:?}", deficit_nomes);
    let abund_nomes: Vec<String> = diag_maria
        .tipos_abundantes
        .iter()
        .map(|t| t.rotulo().split('(').next().unwrap_or("").trim().to_string())
        .collect();
    println!("  Abundantes: {:?}", abund_nomes);
    println!("  VEREDITO: {}", diag_maria.veredito);

    // --- Diagnostico: comunidade ---
    println!("\n[DIAGNOSTICO ENERGETICO -- Comunidade: Solar Village]");
    let mut status_sv = HashMap::new();
    status_sv.insert(TipoEnergia::CELULAR, StatusDisponibilidade::ABUNDANTE);
    status_sv.insert(TipoEnergia::MECANICA, StatusDisponibilidade::EQUILIBRADA);
    status_sv.insert(TipoEnergia::TERMICA, StatusDisponibilidade::ABUNDANTE);
    status_sv.insert(TipoEnergia::NEURAL, StatusDisponibilidade::LIMITADA);
    status_sv.insert(TipoEnergia::QUIMICA, StatusDisponibilidade::EQUILIBRADA);
    status_sv.insert(TipoEnergia::SENSORIAL, StatusDisponibilidade::EQUILIBRADA);
    status_sv.insert(TipoEnergia::COGNITIVA, StatusDisponibilidade::EQUILIBRADA);
    status_sv.insert(TipoEnergia::ATENCIONAL, StatusDisponibilidade::EQUILIBRADA);
    status_sv.insert(TipoEnergia::EMOCIONAL, StatusDisponibilidade::ABUNDANTE);
    status_sv.insert(TipoEnergia::RELACIONAL, StatusDisponibilidade::ABUNDANTE);

    let diag_sv = e.diagnosticar("comunidade:solar_village", status_sv);
    println!("  Entidade: {}", diag_sv.entidade);
    let deficit_nomes: Vec<String> = diag_sv
        .tipos_em_deficit
        .iter()
        .map(|t| t.rotulo().split('(').next().unwrap_or("").trim().to_string())
        .collect();
    println!("  Em deficit: {:?}", deficit_nomes);
    let abund_nomes: Vec<String> = diag_sv
        .tipos_abundantes
        .iter()
        .map(|t| t.rotulo().split('(').next().unwrap_or("").trim().to_string())
        .collect();
    println!("  Abundantes: {:?}", abund_nomes);
    println!("  VEREDITO: {}", diag_sv.veredito);

    // --- Scorecard ---
    println!("\n{}", "=".repeat(70));
    println!("[SCORECARD DA TAXONOMIA ENERGETICA]");
    println!("{}", "=".repeat(70));
    let sc = e.scorecard();
    for (k, v) in &sc {
        println!("  {:.<28} {}", k, v);
    }

    // --- FILOSOFIA ---
    println!("\n{}", "=".repeat(70));
    println!("FILOSOFIA -- Energia e a bateria do trabalho");
    println!("{}", "=".repeat(70));
    println!(
        "'Energia e a bateria do trabalho. Nosso corpo so funciona porque\n\
         temos energia. Nada foi feito na Terra por humanos sem a necessidade\n\
         de energia.'\n\
         \n\
         O corpo humano nao tem UM sistema de energia. Tem DEZ.\n\
         Cada um com input, conversao, output e residuo.\n\
         A civilizacao herda essa estrutura -- somos um corpo em escala.\n\
         \n\
         OpenEnergy cobre o sistema 1 (eletrico = ATP).\n\
         Mas existem outros 9 que a Republica precisa tratar:\n\
         \n\
         NEURAL (sistema nervoso = internet):\n\
           Quem controla a rede controla o sistema nervoso da civilizacao.\n\
           Banda gratuita e NECESSARIA. A internet e o nervo. Sem nervo, paralisia.\n\
         \n\
         COGNITIVA (cerebro = computacao):\n\
           Processar informacao TEM CUSTO ENERGETICO. IA nao e gratuita.\n\
           P8 exige que esse custo seja alocado democraticamente, nao por dinheiro.\n\
         \n\
         ATENCIONAL (foco = atencao finita):\n\
           A atencao e o recurso mais explorado do seculo XXI.\n\
           Plataformas capturam sua atencao e vendem. Isso e EXTRATIVISMO ENERGETICO.\n\
           FocusGuard e o comeco. Proteger atencao = proteger energia.\n\
         \n\
         EMOCIONAL (motivacao = drive):\n\
           Depressao e CRISE ENERGETICA. O combustivel existe (ATP), mas o motor\n\
           nao liga (sem dopamina). Saude mental nao e luxo terapeutico --\n\
           e INFRAESTRUTURA ENERGETICA. Sem motivacao, nenhuma outra energia se move.\n\
         \n\
         RELACIONAL (social = conexao):\n\
           O ser humano isolado DEGRADA. Conexao e necessidade energetica.\n\
           A assembleia, o mutirao, a cooperativa sao GERADORES de energia relacional.\n\
           P9 protege esta energia do atrito da polarizacao.\n\
         \n\
         A LEI DE TODOS OS 10:\n\
           INPUT -> CONVERSAO -> OUTPUT -> RESIDUO.\n\
           Nada se cria, tudo se transforma.\n\
           A Republica nao cria energia. TRANSFORMA.\n\
           E transforma COM JUSTICA: sem desperdicio, sem exclusao, semElite."
    );
}