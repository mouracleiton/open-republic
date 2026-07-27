# OpenRepublic -- Manifest Central

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/manifest.py`

**Descricao:** ==================================
Registro de TODOS os projetos como bens comuns da Republica.
Cada projeto e uma entidade com metadados: dominio, funcao, local, responsaveis.
"Na Republica, tudo e bem publico. Tudo e cadastrado."

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Manifest Central
==================================

Registro de TODOS os projetos como bens comuns da Republica.
Cada projeto e uma entidade com metadados: dominio, funcao, local, responsaveis.

"Na Republica, tudo e bem publico. Tudo e cadastrado."
// 

// importa annotations de __future__
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa Path de pathlib


classe Domain herda de Enum:
    INFRASTRUCTURE = "infrastructure"
    ECONOMY = "economy"
    SOCIETY = "society"
    HEALTH = "health"
    TECHNOLOGY = "technology"
    TRANSPORT = "transport"
    AGRICULTURE = "agriculture"
    CULTURE = "culture"
    NEXUS = "nexus"


// decorador: @dataclass
classe RepublicAsset:
    // Um projeto/sistema cadastrado como bem da Republica.
    asset_id: texto
    name: texto
    domain: Domain
    path: texto
    description: texto
    seja files: inteiro = 0
    seja lines: inteiro = 0
    seja languages: [texto] = field(default_factory=list)
    seja status: texto = "operational"
    seja dependencies: [texto] = field(default_factory=list)
    seja provides: [texto] = field(default_factory=list)
    seja maintainer: texto = "comunidade"


// Registry of all assets
seja REPUBLIC_REGISTRY: [RepublicAsset] = [
    // INFRASTRUCTURE
    RepublicAsset("R-INF-01", "OpenNetwork", Domain.INFRASTRUCTURE,
        "modules/infrastructure/open-network",
        "Infraestrutura de rede nacional -- 7 camadas OSI completas"),
    RepublicAsset("R-INF-02", "OpenProtocol", Domain.INFRASTRUCTURE,
        "modules/infrastructure/open-protocol",
        "Novo protocolo de internet -- 256-bit geo addressing"),
    RepublicAsset("R-INF-03", "OpenDatacenter", Domain.INFRASTRUCTURE,
        "modules/infrastructure/open-datacenter",
        "Datacenter subterraneo quantico 50m"),
    RepublicAsset("R-INF-04", "OpenLaptop", Domain.INFRASTRUCTURE,
        "modules/infrastructure/open-laptop",
        "Laptop open-source RISC-V + Open-GPU + NPU"),
    RepublicAsset("R-INF-05", "OpenGPU", Domain.INFRASTRUCTURE,
        "modules/infrastructure/open-gpu",
        "GPU open-source em SystemVerilog (RTL completo)"),
    RepublicAsset("R-INF-06", "OpenSmartphone", Domain.INFRASTRUCTURE,
        "modules/infrastructure/open-smartphone",
        "Smartphone convergente phone->desktop->laptop"),
    RepublicAsset("R-INF-07", "OpenHardware", Domain.INFRASTRUCTURE,
        "modules/infrastructure/open-hardware",
        "EDA + design de hardware"),
    RepublicAsset("R-INF-08", "OpenQuantum", Domain.INFRASTRUCTURE,
        "modules/infrastructure/open-quantum",
        "Computador quantico fotonico + bridge classico-quantum"),
    RepublicAsset("R-INF-09", "UniversalEmulator", Domain.INFRASTRUCTURE,
        "modules/infrastructure/universal-emulator",
        "Emulador multi-plataforma (CHIP-8 a NDS)"),

    // ECONOMY
    RepublicAsset("R-ECO-01", "OpenEconomy", Domain.ECONOMY,
        "modules/economy/open-economy",
        "Sistema economico macro + CBDC"),
    RepublicAsset("R-ECO-02", "OpenFinance", Domain.ECONOMY,
        "modules/economy/open-finance",
        "PIX + cartoes + boleto + credito + banking"),
    RepublicAsset("R-ECO-03", "OpenProduction", Domain.ECONOMY,
        "modules/economy/open-production",
        "FabLabs + blueprints abertos + pesquisa de materiais"),
    RepublicAsset("R-ECO-04", "OpenProduct", Domain.ECONOMY,
        "modules/economy/open-product",
        "Engenharia reversa + produtos all-in-one"),
    RepublicAsset("R-ECO-05", "OpenReverseLogistics", Domain.ECONOMY,
        "modules/economy/open-reverse-logistics",
        "Reciclagem + reparo first + terminais burros"),
    RepublicAsset("R-ECO-06", "OpenCommunism", Domain.ECONOMY,
        "modules/economy/open-communism",
        "Simulacao de planejamento coletivo"),

    // SOCIETY
    RepublicAsset("R-SOC-01", "OpenNation", Domain.SOCIETY,
        "modules/society/open-nation",
        "Sociedade sem propriedade privada"),
    RepublicAsset("R-SOC-02", "OpenHome", Domain.SOCIETY,
        "modules/society/open-home",
        "Lider eleva liderados -- QoL aditivo"),
    RepublicAsset("R-SOC-03", "OpenFaith", Domain.SOCIETY,
        "modules/society/open-faith",
        "Politica de fe + estado laico"),
    RepublicAsset("R-SOC-04", "OpenHR", Domain.SOCIETY,
        "modules/society/open-hr",
        "Folha de pagamento CLT"),
    RepublicAsset("R-SOC-05", "OpenPsychology", Domain.SOCIETY,
        "modules/society/open-psychology",
        "Saude mental + PHQ-9/GAD-7"),
    RepublicAsset("R-SOC-06", "OpenEducation", Domain.SOCIETY,
        "modules/society/open-education",
        "Educacao"),

    // HEALTH
    RepublicAsset("R-HEA-01", "OpenHealth", Domain.HEALTH,
        "modules/health/open-health",
        "EHR + diagnostico AI + SUS-scale"),
    RepublicAsset("R-HEA-02", "OpenMedicalTest", Domain.HEALTH,
        "modules/health/open-medical-test",
        "Lab + calculadora de risco + Westgard QC"),
    RepublicAsset("R-HEA-03", "OpenProsthesis", Domain.HEALTH,
        "modules/health/open-prosthesis",
        "Protese bionica EMG (100% classificacao)"),
    RepublicAsset("R-HEA-04", "OpenOphthalmology", Domain.HEALTH,
        "modules/health/open-ophthalmology",
        "Oftalmologia AI + IOL"),
    RepublicAsset("R-HEA-05", "OpenArtificialOrgan", Domain.HEALTH,
        "modules/health/open-artificial-organ",
        "Bio-reator + organ-on-chip + transplante"),

    // TECHNOLOGY
    RepublicAsset("R-TEC-01", "OpenCompression", Domain.TECHNOLOGY,
        "modules/technology/open-compression",
        "Codecs: Huffman, LZ4, DCT, VQ, quantum"),
    RepublicAsset("R-TEC-02", "OpenDesktop", Domain.TECHNOLOGY,
        "modules/technology/open-desktop",
        "Window manager Wayland"),
    RepublicAsset("R-TEC-03", "OpenCloud", Domain.TECHNOLOGY,
        "modules/technology/open-cloud",
        "Plataforma cloud IaaS/PaaS"),
    RepublicAsset("R-TEC-04", "OpenAIPlatform", Domain.TECHNOLOGY,
        "modules/technology/openai-platform",
        "IA: inferencia + treinamento + avaliacao"),
    RepublicAsset("R-TEC-05", "OpenLinux", Domain.TECHNOLOGY,
        "modules/technology/openlinux",
        "Distribuicao Linux (kernel + package manager)"),
    RepublicAsset("R-TEC-06", "OpenCompiler", Domain.TECHNOLOGY,
        "modules/technology/open-compiler",
        "Compilador"),
    RepublicAsset("R-TEC-07", "OpenScience", Domain.TECHNOLOGY,
        "modules/technology/open-science",
        "Plataforma de pesquisa (DOE + Monte Carlo + stats)"),

    // TRANSPORT
    RepublicAsset("R-TRA-01", "OpenTransport", Domain.TRANSPORT,
        "modules/transport/open-transport",
        "Transporte nacional (rodoviario + simulacao)"),
    RepublicAsset("R-TRA-02", "OpenRailway", Domain.TRANSPORT,
        "modules/transport/open-railway",
        "Ferrovia nacional (sinalizacao + scheduling)"),

    // AGRICULTURE
    RepublicAsset("R-AGR-01", "OpenAgrarian", Domain.AGRICULTURE,
        "modules/agriculture/open-agrarian",
        "IoT sensores + crop AI + LoRaWAN"),

    // CULTURE + ENERGY
    RepublicAsset("R-CUL-01", "OpenArtist", Domain.CULTURE,
        "modules/culture/open-artist",
        "Suite criativa AI"),
    RepublicAsset("R-CUL-02", "OpenEnergy", Domain.CULTURE,
        "modules/culture/open-energy",
        "Sistema de energia"),

    // NEXUS
    RepublicAsset("R-NEX-01", "NEXUS", Domain.NEXUS,
        "modules/nexus/nexus",
        "Orquestracao unificada GPU + AI (68 modelos)"),
]


funcao count_asset(asset: RepublicAsset, base_path: Path) -> {texto: qualquer}:
    // Conta arquivos e linhas de um asset.
    real_path = base_path / asset.path
    se nao real_path.exists() entao:
        retorne {"files": 0, "lines": 0, "exists": falso}

    code_exts = {".py", ".js", ".sv", ".md", ".html", ".yaml", ".yml"}
    files = [f para f em real_path.rglob("*") if f.is_file()
              e  "__pycache__" nao  in texto(f)  e  nao  f.name.startswith(".")]
    code_files = [f para f em files if f.suffix in code_exts e f.stat().st_size > 50]
    total_lines = soma(tamanho(f.read_text(errors="ignore").splitlines())
                      para f em code_files)
    langs = ordene(set(f.suffix para f em code_files))

    asset.files = tamanho(code_files)
    asset.lines = total_lines
    asset.languages = [l.lstrip(".") para l em langs]
    retorne {"files": tamanho(code_files), "lines": total_lines, "exists": verdadeiro}


funcao full_inventory(base_path: Path = None) -> {texto: qualquer}:
    // Inventario completo da Republica.
    se base_path e nulo entao:
        base_path = Path("/Users/cleitonmouraloura/Documents/open-republic")

    by_domain = {}
    total_files = 0
    total_lines = 0

    para cada asset em REPUBLIC_REGISTRY:
        info = count_asset(asset, base_path)
        d = asset.domain.value
        se d nao in by_domain entao:
            by_domain[d] = {"assets": [], "total_lines": 0, "total_files": 0}
        by_domain[d]["assets"].append({
            "id": asset.asset_id,
            "name": asset.name,
            "files": asset.files,
            "lines": asset.lines,
            "description": asset.description,
            "languages": asset.languages,
            "status": asset.status,
        })
        by_domain[d]["total_lines"] += asset.lines
        by_domain[d]["total_files"] += asset.files
        total_files = total_files + asset.files
        total_lines = total_lines + asset.lines

    retorne {
        "total_assets": tamanho(REPUBLIC_REGISTRY),
        "total_files": total_files,
        "total_lines": total_lines,
        "domains": tamanho(by_domain),
        "by_domain": by_domain,
    }


se __name__ == "__main__" entao:
    imprima("=" * 75)
    imprima("  OPENREPUBLIC -- REGISTRO CENTRAL DE BENS COMUNS")
    imprima("  'Tudo que existe na Republica e bem publico e cadastrado.'")
    imprima("=" * 75)

    inv = full_inventory()

    imprima("\n  TOTAL: {inv['total_assets']} sistemas | "
          "{inv['total_files']} arquivos | "
          "{inv['total_lines']:,} linhas\n")

    imprima("  {'Dominio':<16} {'Sistemas':>8} {'Arquivos':>8} {'Linhas':>8}")
    imprima("  {'-'*44}")
    para cada (domain, data) em ordene(inv["by_domain"].items()):
        imprima("  {domain:<16} {len(data['assets']):>8} "
              "{data['total_files']:>8} {data['total_lines']:>8,}")

    imprima("\n  {'SISTEMA':<28} {'DOMINIO':<14} {'LINHAS':>7}")
    imprima("  {'-'*52}")
    para cada (domain, data) em ordene(inv["by_domain"].items()):
        para cada asset em ordene(data["assets"], key=(x) -> -x["lines"]):
            marker = asset["lines"] == 0 ? " <== VAZIO" : ""
            imprima("  {asset['name']:<28} {domain:<14} "
                  "{asset['lines']:>7,}{marker}")

    imprima("\n{'='*75}")
    imprima("  8 dominios. {inv['total_assets']} sistemas integrados.")
    imprima("  {inv['total_lines']:,} linhas de codigo aberto.")
    imprima("  Tudo bem comum. Tudo da Republica.")
    imprima("{'='*75}")

```
