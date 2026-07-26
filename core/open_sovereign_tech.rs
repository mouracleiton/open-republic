// OpenSovereignTech -- Soberania Tecnologica da Republica
// =========================================================
// "GPS proprio. RISC-V local. Rede configurada. Teste e o basico do basico.
// Sistemas sao feitos para humanos. Todos tem acesso ao codigo.
// A especificacao nao pode ser alterada por um vendor.
// Todos os produtos sao iguais -- muda a marca e as cores."

// A Republica NAO depende de tecnologia estrangeira para existir.
// GPS estrangeiro = quem controla o satelite controla onde voce chega.
// Chip estrangeiro = quem fabrica o silicio controla o que voce computa.
// Rede estrangeira = quem roteia o pacote controla o que voce comunica.

// SOBERANIA TECNOLOGICA = SOBERANIA DE FATO.

// OS 7 PILARES DA SOBERANIA TECNOLOGICA:

// 1. GPS SOBERANO
//    O Brasil tem territorio continental. Depender do GPS americano (NAVSTAR),
//    do Galileu europeu ou do BeiDou chines e DEPENDENCIA ESTRATEGICA.
//    Quem controla o posicionamento controla a logistica, a defesa,
//    a agricultura de precisao, a navegacao, a drones civica.
//    A Republica constela seus proprios satelites de posicionamento.

// 2. COMPUTADORES RISC-V
//    RISC-V e uma ISA (Instruction Set Architecture) ABERTA e LIVRE.
//    Nenhum vendor (Intel, AMD, ARM) pode fechar ou alterar a especificacao.
//    A Republica fabrica (ou manda fabricar) seus proprios chips RISC-V.
//    Capazes de rodar modelos de IA LOCAIS -- sem nuvem, sem Big Tech.
//    Seu processador, seus dados, seu poder de computacao.

// 3. REDE SOBERANA
//    A rede da Republica e bem configurada: roteamento local-first,
//    DNS proprio, caching distribuido, CRDT para operacao offline.
//    Nao depende de backbone estrangeiro para funcionar entre comunidades.
//    Se a conexao externa cai, a Republica CONTINUA operando.

// 4. TESTE E O BASICO DO BASICO
//    "Sistemas sao feitos para humanos." Humano testa. Sistema que nao foi
//    testado com humanos REAIS (incluindo deficientes) NAO existe na Republica.
//    Nao existe "release depois corrige". Teste e pre-requisito, nao pos-requisito.

// 5. CODIGO ABERTO RADICAL
//    "Todos tem acesso ao codigo." Sem excecao. Sem "premium tier".
//    Sem "enterprise only". O codigo e da Republica, e da humanidade.
//    CC0. Sem patente. Sem propriedade intelectual sobre software basico.

// 6. SPEC IMUTAVEL (zero vendor lock-in)
//    "A especificacao nao pode ser alterada por um vendor."
//    RISC-V nao pode ser "estendido" por uma empresa e fechado.
//    HTML/CSS/JS nao podem ser "melhorados" por um browser e trancados.
//    O padrao e DA REPUBLICA. Vendors implementam; nao inventam.

// 7. HARDWARE COMMODITIZADO
//    "Todos os produtos sao iguais. Muda a marca e as cores e coisas cosmeticas."
//    O chip RISC-V e o MESMO. A placa-mae e a MESMA. O sistema e o MESMO.
//    O que muda: cor da carcaa, logo, embalagem. Nao o que importa.
//    Acaba a distincao artificial entre "premium" e "basico" que cria elite.

// ALINHAMENTO CONSTITUCIONAL:
// - P1: Tecnologia estrangeira = elite externa controlando. Soberania = anti-elitismo.
// - P2: Seus dados, seu chip, seu processamento = autonomia corporal digital.
// - P4: Codigo aberto = transparencia radical. Ninguem governe o que nao pode ver.
// - P6: Acesso universal = codigo + hardware + rede. Nao so conhecimento.

// Author: OpenRepublic Team

use std::collections::{HashMap, HashSet};

// ============================================================================
// 1. ENUMS (module-level)
// ============================================================================

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum PilarSoberania {
    GpsSoberano,
    RiscV,
    RedeSoberana,
    TesteHumano,
    CodigoAberto,
    SpecImutavel,
    HardwareCommoditizado,
}

impl PilarSoberania {
    pub fn id(&self) -> &'static str {
        match self {
            PilarSoberania::GpsSoberano => "gps_soberano",
            PilarSoberania::RiscV => "risc_v",
            PilarSoberania::RedeSoberana => "rede_soberana",
            PilarSoberania::TesteHumano => "teste_humano",
            PilarSoberania::CodigoAberto => "codigo_aberto",
            PilarSoberania::SpecImutavel => "spec_imutavel",
            PilarSoberania::HardwareCommoditizado => "hardware_commoditizado",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            PilarSoberania::GpsSoberano => "GPS Soberano (posicionamento nacional)",
            PilarSoberania::RiscV => "Computadores RISC-V (ISA aberta, IA local)",
            PilarSoberania::RedeSoberana => "Rede Soberana (local-first, offline-capable)",
            PilarSoberania::TesteHumano => "Teste e o basico (teste com humanos reais)",
            PilarSoberania::CodigoAberto => "Codigo aberto radical (CC0, sem excecao)",
            PilarSoberania::SpecImutavel => "Spec imutavel (zero vendor lock-in)",
            PilarSoberania::HardwareCommoditizado => "Hardware commoditizado (produtos iguais)",
        }
    }

    pub fn numero(&self) -> u8 {
        match self {
            PilarSoberania::GpsSoberano => 1,
            PilarSoberania::RiscV => 2,
            PilarSoberania::RedeSoberana => 3,
            PilarSoberania::TesteHumano => 4,
            PilarSoberania::CodigoAberto => 5,
            PilarSoberania::SpecImutavel => 6,
            PilarSoberania::HardwareCommoditizado => 7,
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum StatusSoberania {
    Dependente,
    Parcial,
    Transicao,
    Soberano,
    Autarquico,
}

impl StatusSoberania {
    pub fn id(&self) -> &'static str {
        match self {
            StatusSoberania::Dependente => "dependente",
            StatusSoberania::Parcial => "parcial",
            StatusSoberania::Transicao => "transicao",
            StatusSoberania::Soberano => "soberano",
            StatusSoberania::Autarquico => "autarquico",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            StatusSoberania::Dependente => "Dependente: 100% estrangeiro, zero controle",
            StatusSoberania::Parcial => "Parcial: algum controle, nucleo estrangeiro",
            StatusSoberania::Transicao => "Em transicao: infraestrutura propria em construcao",
            StatusSoberania::Soberano => "Soberano: controla o stack completo",
            StatusSoberania::Autarquico => "Autarquico: nao so controla, como fabrica e doa",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoVendorLockIn {
    ExtensaoProprietaria,
    DriverFechado,
    PatenteTrucada,
    CertificacaoObrigatoria,
    FormatoIncompativel,
    BackdoorFirmware,
    ObsolescenciaForcada,
    UpdateBloqueado,
}

impl TipoVendorLockIn {
    pub fn id(&self) -> &'static str {
        match self {
            TipoVendorLockIn::ExtensaoProprietaria => "extensao_proprietaria",
            TipoVendorLockIn::DriverFechado => "driver_fechado",
            TipoVendorLockIn::PatenteTrucada => "patente_trucada",
            TipoVendorLockIn::CertificacaoObrigatoria => "certificacao_obrigatoria",
            TipoVendorLockIn::FormatoIncompativel => "formato_incompativel",
            TipoVendorLockIn::BackdoorFirmware => "backdoor_firmware",
            TipoVendorLockIn::ObsolescenciaForcada => "obsolescencia_forcada",
            TipoVendorLockIn::UpdateBloqueado => "update_bloqueado",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoVendorLockIn::ExtensaoProprietaria => "Extensao proprietaria ao padrao aberto",
            TipoVendorLockIn::DriverFechado => "Driver/firmware fechado (hardware funciona so com SW da vendor)",
            TipoVendorLockIn::PatenteTrucada => "Patente sobre o padrao aberto (trucada juridica)",
            TipoVendorLockIn::CertificacaoObrigatoria => "Certificacao obrigatoria paga (toll booth)",
            TipoVendorLockIn::FormatoIncompativel => "Formato proprietario incompativel com padrao",
            TipoVendorLockIn::BackdoorFirmware => "Backdoor/firmware opaco (seguranca invisivel)",
            TipoVendorLockIn::ObsolescenciaForcada => "Obsolescencia forcada (quebra sem atualizacao)",
            TipoVendorLockIn::UpdateBloqueado => "Update bloqueado em hardware antigo (sem motivo real)",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum TipoTeste {
    Unitario,
    Integracao,
    HumanoReal,
    HumanoDeficiente,
    Stress,
    Seguranca,
    Campo,
    Regressao,
}

impl TipoTeste {
    pub fn id(&self) -> &'static str {
        match self {
            TipoTeste::Unitario => "unitario",
            TipoTeste::Integracao => "integracao",
            TipoTeste::HumanoReal => "humano_real",
            TipoTeste::HumanoDeficiente => "humano_deficiente",
            TipoTeste::Stress => "stress",
            TipoTeste::Seguranca => "seguranca",
            TipoTeste::Campo => "campo",
            TipoTeste::Regressao => "regressao",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            TipoTeste::Unitario => "Teste unitario (cada funcao isolada)",
            TipoTeste::Integracao => "Teste de integracao (componentes juntos)",
            TipoTeste::HumanoReal => "Teste com humano real (nao simulacao)",
            TipoTeste::HumanoDeficiente => "Teste com pessoa com deficiencia (CEGO/SURDO/TETRA/TEA)",
            TipoTeste::Stress => "Teste de stress (carga, offline, falha)",
            TipoTeste::Seguranca => "Teste de seguranca (pen-test, auditoria)",
            TipoTeste::Campo => "Teste de campo (uso real, nao laboratorio)",
            TipoTeste::Regressao => "Teste de regressao (update nao quebra o que funciona)",
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum ComponenteStack {
    Silicio,
    Isa,
    Firmware,
    Kernel,
    Sistema,
    Rede,
    IaLocal,
    Gps,
    Aplicacao,
    Interface,
}

impl ComponenteStack {
    pub fn id(&self) -> &'static str {
        match self {
            ComponenteStack::Silicio => "silicio",
            ComponenteStack::Isa => "isa",
            ComponenteStack::Firmware => "firmware",
            ComponenteStack::Kernel => "kernel",
            ComponenteStack::Sistema => "sistema",
            ComponenteStack::Rede => "rede",
            ComponenteStack::IaLocal => "ia_local",
            ComponenteStack::Gps => "gps",
            ComponenteStack::Aplicacao => "aplicacao",
            ComponenteStack::Interface => "interface",
        }
    }

    pub fn rotulo(&self) -> &'static str {
        match self {
            ComponenteStack::Silicio => "Silicio / fab de chips (RISC-V)",
            ComponenteStack::Isa => "ISA RISC-V (instruction set)",
            ComponenteStack::Firmware => "Firmware (boot, drivers base)",
            ComponenteStack::Kernel => "Kernel (Linux/BSD custom)",
            ComponenteStack::Sistema => "Sistema operacional da Republica",
            ComponenteStack::Rede => "Camada de rede (DNS, roteamento, CRDT)",
            ComponenteStack::IaLocal => "Modelos de IA rodando localmente",
            ComponenteStack::Gps => "Sistema de posicionamento (constelacao de satelites)",
            ComponenteStack::Aplicacao => "Aplicacoes (Republic app suite)",
            ComponenteStack::Interface => "Interface (acessivel a TODAS as deficiencias)",
        }
    }
}

// ============================================================================
// 2. STRUCTS (dataclasses)
// ============================================================================

#[derive(Debug, Clone)]
pub struct HardwareSoberano {
    pub id: String,
    pub nome: String,
    pub componente: ComponenteStack,
    pub arquitetura: String,
    pub capacidade_ia_local: bool,
    pub ram_gb: u32,
    pub armazenamento_gb: u32,
    pub consumo_watts: f64,
    pub custo_producao_cred: f64,
    pub spec_imutavel: bool,
    pub codigo_aberto: bool,
    pub testado_humano: bool,
}

#[derive(Debug, Clone)]
pub struct ConstelacaoGPS {
    pub nome_sistema: String,
    pub num_satelites: u32,
    pub cobertura: String,
    pub precisao_metros: f64,
    pub status: StatusSoberania,
    pub lancados: u32,
    pub planejados: u32,
    pub backup_estrangeiro: String,
}

#[derive(Debug, Clone)]
pub struct VendorLockInDetectado {
    pub componente: ComponenteStack,
    pub tipo: TipoVendorLockIn,
    pub vendor: String,
    pub descricao: String,
    pub severidade: u8,
    pub acao_recomendada: String,
}

#[derive(Debug, Clone)]
pub struct TesteRealizado {
    pub tipo: TipoTeste,
    pub componente: ComponenteStack,
    pub passou: bool,
    pub detalhes: String,
    pub data: String,
    pub participantes_humanos: u32,
}

#[derive(Debug, Clone)]
pub struct MatrizSoberania {
    pub componente: ComponenteStack,
    pub status: StatusSoberania,
    pub pct_soberano: f64,
    pub dependencias_estrangeiras: Vec<String>,
    pub bloqueadores: Vec<String>,
}

// ============================================================================
// 3. ENGINE
// ============================================================================

pub struct SoberaniaTechEngine {
    pub hardwares: HashMap<String, HardwareSoberano>,
    pub constelacao: Option<ConstelacaoGPS>,
    pub lockins: Vec<VendorLockInDetectado>,
    pub testes: Vec<TesteRealizado>,
    pub matriz: HashMap<String, MatrizSoberania>,
    hw_id: u32,
}

impl SoberaniaTechEngine {
    pub fn new() -> Self {
        SoberaniaTechEngine {
            hardwares: HashMap::new(),
            constelacao: None,
            lockins: Vec::new(),
            testes: Vec::new(),
            matriz: HashMap::new(),
            hw_id: 0,
        }
    }

    fn hw_novo_id(&mut self) -> String {
        self.hw_id += 1;
        format!("HW-{:04}", self.hw_id)
    }

    pub fn cadastrar_hardware(
        &mut self,
        nome: &str,
        componente: ComponenteStack,
        arquitetura: &str,
        capacidade_ia_local: bool,
        ram_gb: u32,
        armazenamento_gb: u32,
        consumo_watts: f64,
        custo_producao_cred: f64,
    ) -> String {
        let id = self.hw_novo_id();
        let hw = HardwareSoberano {
            id: id.clone(),
            nome: nome.to_string(),
            componente,
            arquitetura: arquitetura.to_string(),
            capacidade_ia_local,
            ram_gb,
            armazenamento_gb,
            consumo_watts,
            custo_producao_cred,
            spec_imutavel: true,
            codigo_aberto: true,
            testado_humano: false,
        };
        self.hardwares.insert(id.clone(), hw);
        id
    }

    pub fn configurar_gps(
        &mut self,
        nome: &str,
        num_satelites: u32,
        cobertura: &str,
        precisao_metros: f64,
        lancados: u32,
        planejados: u32,
        status: StatusSoberania,
        backup: &str,
    ) -> &ConstelacaoGPS {
        self.constelacao = Some(ConstelacaoGPS {
            nome_sistema: nome.to_string(),
            num_satelites,
            cobertura: cobertura.to_string(),
            precisao_metros,
            status,
            lancados,
            planejados,
            backup_estrangeiro: backup.to_string(),
        });
        self.constelacao.as_ref().unwrap()
    }

    pub fn detectar_lockin(
        &mut self,
        componente: ComponenteStack,
        tipo: TipoVendorLockIn,
        vendor: &str,
        descricao: &str,
        severidade: u8,
    ) -> usize {
        let acao = self.acao_lockin(&tipo);
        let li = VendorLockInDetectado {
            componente,
            tipo,
            vendor: vendor.to_string(),
            descricao: descricao.to_string(),
            severidade,
            acao_recomendada: acao,
        };
        self.lockins.push(li);
        self.lockins.len() - 1
    }

    fn acao_lockin(&self, tipo: &TipoVendorLockIn) -> String {
        match tipo {
            TipoVendorLockIn::ExtensaoProprietaria => {
                "Rejeitar extensao. Exigir conformidade com spec padrao RISC-V.".to_string()
            }
            TipoVendorLockIn::DriverFechado => {
                "Firmware deve ser aberto (CC0). Hardware sem driver aberto NAO e comprado.".to_string()
            }
            TipoVendorLockIn::PatenteTrucada => {
                "RISC-V e livre de royalties. Contestar patente em corte. Nao pagar.".to_string()
            }
            TipoVendorLockIn::CertificacaoObrigatoria => {
                "Certificacao e da Republica, gratuita. Nenhum vendor cobra toll.".to_string()
            }
            TipoVendorLockIn::FormatoIncompativel => {
                "Formato proprietario PROIBIDO. Tudo deve seguir padrao aberto.".to_string()
            }
            TipoVendorLockIn::BackdoorFirmware => {
                "Firmware opaco PROIBIDO. Auditoria de seguranca radical.".to_string()
            }
            TipoVendorLockIn::ObsolescenciaForcada => {
                "Hardware deve funcionar por minimo 10 anos. Update garantido.".to_string()
            }
            TipoVendorLockIn::UpdateBloqueado => {
                "Bloqueio sem motivo real e CRIME. Hardware atualizavel indefinidamente.".to_string()
            }
        }
    }

    pub fn lockins_por_severidade(&self) -> Vec<&VendorLockInDetectado> {
        let mut sorted = self.lockins.iter().collect::<Vec<_>>();
        sorted.sort_by(|a, b| {
            b.severidade.cmp(&a.severidade).then_with(|| a.componente.id().cmp(b.componente.id()))
        });
        sorted
    }

    pub fn lockins_criticos(&self) -> Vec<&VendorLockInDetectado> {
        self.lockins.iter().filter(|li| li.severidade >= 4).collect()
    }

    pub fn registrar_teste(
        &mut self,
        tipo: TipoTeste,
        componente: ComponenteStack,
        passou: bool,
        detalhes: &str,
        participantes_humanos: u32,
    ) -> usize {
        let data = String::from("now");  // sem chrono -- timestamp simplificado
        let t = TesteRealizado {
            tipo,
            componente,
            passou,
            detalhes: detalhes.to_string(),
            data,
            participantes_humanos,
        };
        self.testes.push(t);
        self.testes.len() - 1
    }

    pub fn cobertura_testes(&self, componente: ComponenteStack) -> (u32, u32, f64, Vec<String>, bool, String) {
        let tipos_testados: HashSet<_> = self
            .testes
            .iter()
            .filter(|t| t.componente == componente && t.passou)
            .map(|t| t.tipo.clone())
            .collect();
        let tipos_faltando: Vec<_> = [
            TipoTeste::Unitario,
            TipoTeste::Integracao,
            TipoTeste::HumanoReal,
            TipoTeste::HumanoDeficiente,
            TipoTeste::Stress,
            TipoTeste::Seguranca,
            TipoTeste::Campo,
            TipoTeste::Regressao,
        ]
        .iter()
        .filter(|t| !tipos_testados.contains(t))
        .map(|t| t.rotulo().to_string())
        .collect();
        let total = 8u32;
        let feitos = tipos_testados.len() as u32;
        let pct = (feitos as f64 / total as f64 * 100.0).round();
        let aprovado = tipos_faltando.is_empty();
        let mensagem = if aprovado {
            format!("COBERTURA COMPLETA: {}/{} tipos.", feitos, total)
        } else {
            format!(
                "INCOMPLETO: falta {} tipo(s). Teste e o basico do basico.",
                tipos_faltando.len()
            )
        };
        (feitos, total, pct, tipos_faltando, aprovado, mensagem)
    }

    pub fn construir_matriz(&mut self) -> HashMap<String, MatrizSoberania> {
        self.matriz.clear();
        for comp in [
            ComponenteStack::Silicio,
            ComponenteStack::Isa,
            ComponenteStack::Firmware,
            ComponenteStack::Kernel,
            ComponenteStack::Sistema,
            ComponenteStack::Rede,
            ComponenteStack::IaLocal,
            ComponenteStack::Gps,
            ComponenteStack::Aplicacao,
            ComponenteStack::Interface,
        ] {
            let hws: Vec<_> = self
                .hardwares
                .values()
                .filter(|h| h.componente == comp)
                .collect();
            if hws.is_empty() {
                self.matriz.insert(
                    comp.id().to_string(),
                    MatrizSoberania {
                        componente: comp,
                        status: StatusSoberania::Dependente,
                        pct_soberano: 0.0,
                        dependencias_estrangeiras: vec![],
                        bloqueadores: vec!["Nenhum hardware soberano cadastrado.".to_string()],
                    },
                );
                continue;
            }
            let soberanos = hws
                .iter()
                .filter(|h| h.spec_imutavel && h.codigo_aberto)
                .count();
            let pct = (soberanos as f64 / hws.len() as f64 * 100.0).round();
            let lockins_comp: Vec<_> = self
                .lockins
                .iter()
                .filter(|li| li.componente == comp)
                .collect();
            let deps_estrangeiras: Vec<String> = lockins_comp
                .iter()
                .map(|li| li.vendor.clone())
                .collect::<HashSet<_>>()
                .into_iter()
                .collect();
            let bloqueadores: Vec<String> = lockins_comp
                .iter()
                .map(|li| format!("{} (vendor: {})", li.tipo.rotulo(), li.vendor))
                .collect();
            let status = if pct == 100.0 && lockins_comp.is_empty() {
                StatusSoberania::Soberano
            } else if pct >= 50.0 {
                StatusSoberania::Transicao
            } else if pct > 0.0 {
                StatusSoberania::Parcial
            } else {
                StatusSoberania::Dependente
            };
            self.matriz.insert(
                comp.id().to_string(),
                MatrizSoberania {
                    componente: comp,
                    status,
                    pct_soberano: pct,
                    dependencias_estrangeiras: deps_estrangeiras,
                    bloqueadores,
                },
            );
        }
        self.matriz.clone()
    }

    pub fn manifesto_hardware_igual(&self) -> String {
        "MANIFESTO DO HARDWARE IGUAL:\n  O chip RISC-V e o MESMO em todos os produtos.\n  A placa-mae e a MESMA.\n  O firmware e o MESMO (CC0, aberto).\n  O sistema operacional e o MESMO.\n  O que pode diferir: cor da carcaca, logo, embalagem.\n  O que NAO pode diferir: performance, seguranca, acessibilidade.\n  NAO existe 'premium' vs 'basico'. Existe UM produto.\n  Quem tenta criar tiers artificiais para extrair mais dinheiro\n  esta RECRINANDO ELITE (P1). A Republica nao permite.".to_string()
    }

    pub fn scorecard(&mut self) -> HashMap<String, String> {
        let matriz = self.construir_matriz();
        let soberanos = matriz
            .values()
            .filter(|m| m.status == StatusSoberania::Soberano || m.status == StatusSoberania::Autarquico)
            .count();
        let total = 10usize;
        let pct = (soberanos as f64 / total as f64 * 100.0).round();
        let mut sc = HashMap::new();
        sc.insert("componentes_stack".to_string(), total.to_string());
        sc.insert("totalmente_soberanos".to_string(), soberanos.to_string());
        sc.insert("pct_soberania_global".to_string(), pct.to_string());
        sc.insert("hardwares_cadastrados".to_string(), self.hardwares.len().to_string());
        sc.insert(
            "hardwares_capazes_ia_local".to_string(),
            self.hardwares.values().filter(|h| h.capacidade_ia_local).count().to_string(),
        );
        sc.insert("vendor_lockins_detectados".to_string(), self.lockins.len().to_string());
        sc.insert("lockins_criticos".to_string(), self.lockins_criticos().len().to_string());
        sc.insert("testes_realizados".to_string(), self.testes.len().to_string());
        sc.insert(
            "testes_com_humano_real".to_string(),
            self.testes
                .iter()
                .filter(|t| t.tipo == TipoTeste::HumanoReal || t.tipo == TipoTeste::HumanoDeficiente)
                .count()
                .to_string(),
        );
        sc.insert(
            "constelacao_gps_status".to_string(),
            self.constelacao.as_ref().map(|c| c.status.rotulo().to_string()).unwrap_or_else(|| "Nao configurada".to_string()),
        );
        sc
    }
}

// ============================================================================
// 4. DEMO (main equivalent)
// ============================================================================

fn main() {
    let mut e = SoberaniaTechEngine::new();

    println!("{}", "=".repeat(70));
    println!("OpenSovereignTech -- Soberania Tecnologica da Republica");
    println!("{}", "=".repeat(70));

    // --- OS 7 PILARES ---
    println!("\n[OS 7 PILARES DA SOBERANIA TECNOLOGICA]");
    for p in [
        PilarSoberania::GpsSoberano,
        PilarSoberania::RiscV,
        PilarSoberania::RedeSoberana,
        PilarSoberania::TesteHumano,
        PilarSoberania::CodigoAberto,
        PilarSoberania::SpecImutavel,
        PilarSoberania::HardwareCommoditizado,
    ] {
        println!("\n  Pilar {}: {}", p.numero(), p.rotulo());
    }

    // --- GPS Soberano ---
    println!("\n{}", "=".repeat(70));
    println!("[PILAR 1] GPS SOBERANO -- Constelacao Nacional");
    println!("{}", "=".repeat(70));
    e.configurar_gps(
        "RepublicaNav",
        35,
        "Brasil + America do Sul equatorial",
        1.5,
        3,
        35,
        StatusSoberania::Transicao,
        "GPS/Galileo (transitorio ate constelacao completa)",
    );
    let gps = e.constelacao.as_ref().unwrap();
    println!("\n  Sistema: {}", gps.nome_sistema);
    println!("  Satelites: {} lancados / {} planejados", gps.lancados, gps.planejados);
    println!("  Cobertura: {}", gps.cobertura);
    println!("  Precisao alvo: {}m", gps.precisao_metros);
    println!("  Status: {}", gps.status.rotulo());
    println!("  Backup estrangeiro: {}", gps.backup_estrangeiro);
    println!("\n  POR QUE GPS SOBERANO:");
    println!("    - Logistica brasileira nao pode depender de satelite americano.");
    println!("    - Agricultura de precisao nao pode depender de sinal chines.");
    println!("    - Drones civica (OpenDrone) precisam de posicionamento proprio.");
    println!("    - Defesa do territorio exige constelacao nacional.");
    println!("    - Quem controla o GPS controla ONDE voce chega.");

    // --- RISC-V Hardware ---
    println!("\n{}", "=".repeat(70));
    println!("[PILAR 2] COMPUTADORES RISC-V -- IA Local, Zero Vendor Lock-in");
    println!("{}", "=".repeat(70));

    e.cadastrar_hardware(
        "RepublicaPort Avancado",
        ComponenteStack::Silicio,
        "RISC-V RV64GC (64-bit, vetorial)",
        true,
        32,
        512,
        65.0,
        800.0,
    );
    e.cadastrar_hardware(
        "RepublicaPort Padrao",
        ComponenteStack::Silicio,
        "RISC-V RV64GC (64-bit)",
        true,
        16,
        256,
        35.0,
        400.0,
    );
    e.cadastrar_hardware(
        "RepublicaPort Essencial",
        ComponenteStack::Silicio,
        "RISC-V RV32IMAC (32-bit, baixo consumo)",
        false,
        4,
        64,
        5.0,
        150.0,
    );
    e.cadastrar_hardware(
        "RepublicaAcelerador IA",
        ComponenteStack::IaLocal,
        "RISC-V + NPU dedicada",
        true,
        64,
        1024,
        120.0,
        1200.0,
    );

    println!("\n  Catalogo de Hardware Soberano ({} produtos):", e.hardwares.len());
    for hw in e.hardwares.values() {
        let ia = if hw.capacidade_ia_local { "IA-LOCAL" } else { "basico" };
        println!("\n    {}: {}", hw.id, hw.nome);
        println!("      Arquitetura: {}", hw.arquitetura);
        println!("      RAM: {}GB | Storage: {}GB", hw.ram_gb, hw.armazenamento_gb);
        println!("      Consumo: {}W | Custo: {}c", hw.consumo_watts, hw.custo_producao_cred);
        println!("      Capacidade: {}", ia);
        println!("      Spec imutavel: {} | Codigo aberto: {}", hw.spec_imutavel, hw.codigo_aberto);
    }

    println!("\n  POR QUE RISC-V:");
    println!("    - ISA ABERTA: ninguem 'possui' a especificacao.");
    println!("    - Nenhum vendor pode fechar ou alterar o padrao.");
    println!("    - Modelos de IA rodam LOCAL: sem nuvem, sem Big Tech, sem spyware.");
    println!("    - Fabricavel em qualquer foundry (TSMC, SMIC, governo brasileiro).");
    println!("    - Acaba com dependencia de Intel/AMD/ARM/NVIDIA.");

    // --- Manifesto: produtos iguais ---
    println!("\n{}", "=".repeat(70));
    println!("[PILAR 7] HARDWARE COMMODITIZADO -- Produtos Iguais");
    println!("{}", "=".repeat(70));
    println!("\n{}", e.manifesto_hardware_igual());

    // --- Deteccao de Vendor Lock-in ---
    println!("\n{}", "=".repeat(70));
    println!("[AUDITORIA] Deteccao de Vendor Lock-in no stack atual");
    println!("{}", "=".repeat(70));
    e.detectar_lockin(
        ComponenteStack::Firmware,
        TipoVendorLockIn::DriverFechado,
        "Qualcomm",
        "Modem cellular so funciona com firmware fechado da Qualcomm.",
        5,
    );
    e.detectar_lockin(
        ComponenteStack::Firmware,
        TipoVendorLockIn::BackdoorFirmware,
        "Intel",
        "Intel ME (Management Engine): processador oculto com acesso total ao sistema.",
        5,
    );
    e.detectar_lockin(
        ComponenteStack::Gps,
        TipoVendorLockIn::FormatoIncompativel,
        "NAVSTAR (US)",
        "Formato de sinal GPS proprietario. Sem documentacao completa.",
        4,
    );
    e.detectar_lockin(
        ComponenteStack::IaLocal,
        TipoVendorLockIn::PatenteTrucada,
        "NVIDIA",
        "CUDA e proprietario. Roda IA so em GPU NVIDIA.",
        5,
    );
    e.detectar_lockin(
        ComponenteStack::Silicio,
        TipoVendorLockIn::CertificacaoObrigatoria,
        "ARM",
        "Licenca ARM cobra royalties por chip fabricado.",
        4,
    );
    e.detectar_lockin(
        ComponenteStack::Sistema,
        TipoVendorLockIn::ObsolescenciaForcada,
        "Apple",
        "iPhone recebe update por ~5 anos depois e obsoleto por design.",
        4,
    );

    println!("\n  {} lock-ins detectados ({} criticos):", e.lockins.len(), e.lockins_criticos().len());
    for li in e.lockins_por_severidade() {
        let flag = if li.severidade >= 4 { "CRITICO" } else { "ALTO" };
        println!("\n    [{}] {} -> {}", flag, li.componente.rotulo(), li.vendor);
        println!("    Tipo: {}", li.tipo.rotulo());
        println!("    Descricao: {}", li.descricao);
        println!("    Acao: {}", li.acao_recomendada);
    }

    // --- Sistema de testes ---
    println!("\n{}", "=".repeat(70));
    println!("[PILAR 4] TESTE E O BASICO DO BASICO");
    println!("{}", "=".repeat(70));
    println!("\n  'Sistemas sao feitos para humanos.'");
    println!("  'Teste e o basico do basico.'\n");
    e.registrar_teste(TipoTeste::Unitario, ComponenteStack::Silicio, true, "5000 testes unitarios passaram.", 0);
    e.registrar_teste(TipoTeste::Integracao, ComponenteStack::Silicio, true, "Stack completo integrado.", 0);
    e.registrar_teste(TipoTeste::HumanoReal, ComponenteStack::Interface, true, "50 cidadaos testaram por 2 semanas.", 50);
    e.registrar_teste(TipoTeste::HumanoDeficiente, ComponenteStack::Interface, true, "10 pessoas cegas/surdas/cadeirantes testaram.", 10);
    e.registrar_teste(TipoTeste::Stress, ComponenteStack::Rede, true, "Rede suportou 10000 nos offline.", 0);
    e.registrar_teste(TipoTeste::Seguranca, ComponenteStack::Firmware, true, "Pen-test por OpenCybersecurityMuralha.", 0);

    println!("\n  Cobertura de testes por componente:");
    for comp in [ComponenteStack::Silicio, ComponenteStack::Interface, ComponenteStack::Rede] {
        let (feitos, total, pct, faltando, aprovado, mensagem) = e.cobertura_testes(comp.clone());
        println!("\n    {}: {}% ({})", comp.rotulo(), pct, mensagem);
        if !faltando.is_empty() {
            println!("    Faltando: {}", faltando.join(", "));
        }
        println!("    APROVADO: {}", if aprovado { "SIM" } else { "NAO -- teste e o basico do basico" });
    }

    // --- Matriz de Soberania ---
    println!("\n{}", "=".repeat(70));
    println!("[MATRIZ DE SOBERANIA POR COMPONENTE]");
    println!("{}", "=".repeat(70));
    let matriz = e.construir_matriz();
    let lockins_snapshot = e.lockins.clone();
    println!("\n  {:.<25} {:>12} {:>12} {:>10}", "Componente", "Status", "% Soberano", "Lock-ins");
    println!("  {}", "-".repeat(61));
    for comp in [
        ComponenteStack::Silicio,
        ComponenteStack::Isa,
        ComponenteStack::Firmware,
        ComponenteStack::Kernel,
        ComponenteStack::Sistema,
        ComponenteStack::Rede,
        ComponenteStack::IaLocal,
        ComponenteStack::Gps,
        ComponenteStack::Aplicacao,
        ComponenteStack::Interface,
    ] {
        if let Some(m) = matriz.get(comp.id()) {
            let n_locks = lockins_snapshot.iter().filter(|li| li.componente == comp).count();
            println!("  {:.<25} {:>12} {:>11}% {:>10}", comp.rotulo(), m.status.id(), m.pct_soberano, n_locks);
        }
    }

    // --- Scorecard ---
    println!("\n{}", "=".repeat(70));
    println!("[SCORECARD DA SOBERANIA TECNOLOGICA]");
    println!("{}", "=".repeat(70));
    let sc = e.scorecard();
    for (k, v) in &sc {
        println!("  {:.<30} {}", k, v);
    }

    // --- FILOSOFIA ---
    println!("\n{}", "=".repeat(70));
    println!("FILOSOFIA -- Soberania Tecnologica = Soberania de Fato");
    println!("{}", "=".repeat(70));
    println!(
        r#"GPS PROPRIO:
  O Brasil tem territorio continental. Depender do GPS americano
  e DEPENDENCIA ESTRATEGICA. Quem controla o satelite controla
  onde voce chega. Logistica, defesa, agricultura, navegacao,
  drones civica -- tudo depende de posicionamento.
  A Republica constela seus proprios satelites. RepublicaNav.

RISC-V LOCAL:
  RISC-V e ISA aberta. Nenhum vendor pode fechar.
  Modelos de IA rodam LOCAL: sem nuvem, sem Big Tech, sem spyware.
  Seu processador, seus dados, seu poder de computacao.
  Acaba com Intel/AMD/ARM/NVIDIA como pedagios sobre computacao.

REDE CONFIGURADA:
  Local-first. DNS proprio. CRDT offline. Caching distribuido.
  Se a conexao externa cai, a Republica CONTINUA operando.
  A rede nao e servico de empresa. E INFRAESTRUTURA DE ESTADO.

TESTE E O BASICO DO BASICO:
  "Sistemas sao feitos para humanos." Humano testa.
  Sistema nao testado com humano REAL (incluindo deficiente) NAO existe.
  Nao existe "release depois corrige". Teste e pre-requisito.
  Inclui: cego, surdo, tetraplegico, TEA, TDAH, Down.
  Se uma pessoa com deficiencia nao consegue usar, FALHOU.

CODIGO ABERTO RADICAL:
  "Todos tem acesso ao codigo." Sem excecao. Sem premium tier.
  CC0. Sem patente. Sem propriedade intelectual sobre software basico.
  O codigo e da humanidade.

SPEC IMUTAVEL:
  "A especificacao nao pode ser alterada por um vendor."
  RISC-V nao pode ser 'estendido' e fechado.
  HTML nao pode ser 'melhorado' por um browser e trancado.
  O padrao e DA REPUBLICA. Vendors implementam; nao inventam.

HARDWARE COMMODITIZADO:
  "Todos os produtos sao iguais. Muda a marca e as cores."
  O chip e o MESMO. A placa e a MESMO. O sistema e o MESMO.
  O que muda: cor, logo, embalagem. Cosmetica.
  Acaba a elite artificial de 'premium' vs 'basico'.
  Um produto. Para todos. Igual.

A SOBERANIA TECNOLOGICA E A UNICA SOBERANIA REAL:
  Sem GPS proprio, voce nao chega onde quer.
  Sem chip proprio, voce nao computa o que quer.
  Sem rede propria, voce nao comunica o que quer.
  Sem codigo aberto, voce nao confia no que usa.
  Sem teste humano, voce nao sabe se funciona.
  Sem spec imutavel, voce nao controla o futuro.
  Sem hardware igual, voce recria elite.

  A Republica nao e soberana se sua tecnologia nao e.
"#
    );
}