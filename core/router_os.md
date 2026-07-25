# OpenLinuxLive Router Edition

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/router_os.py`

**Descricao:** ==============================
"Todo roteador da Republica roda OpenLinuxLive.
 Velho ou novo. Legado ou FabLab. Sem excecao."
O PROBLEMA DOS ROTEADORES ATUAIS:
  1. Firmware proprietario (TP-Link, Cisco, Netgear)
  2. Sem atualizacao de seguranca apos 2 anos
  3. Backdoors conhecidos de fabricante (NSA, etc)
  4. Hardware fechado, bootloader bloqueado
  5. Interface web lenta e cheia de bugs
  6. Obsolescencia planejada (nao aguenta mais firmware novo)
A SOLUCAO:
  Todo roteador -- seja um TP-Link de 2008 recuperado de e-waste
  ou um roteador FabLab novo -- roda OpenLinuxLive Router Edition.
  - Linux 6.12 LTS (kernel estavel, com patches de seguranca)
  - OpenWrt base (rotagem, firewall, WiFi, DHCP, DNS)
  - OpenProtocol nativo (protocolo da Republica)
  - Mesh networking P2P (roteadores se conectam entre si)
  - OpenLinuxLive pendrive = mesmo OS do cidadao, adaptado
COMO FUNCIONA:
  1. Roteador recuperado de e-waste (OpenReverseLogistics)
  2. Flashear OpenLinuxLive Router Edition
  3. Roteador entra na mesh da Republica automaticamente
  4. Auto-configura (zero configura manual)
  5. Recebe atualizacoes P2P (sem servidor central)
  6. E monitorado por Jarvis (healthcheck da rede)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenLinuxLive Router Edition
==============================

"Todo roteador da Republica roda OpenLinuxLive.
 Velho ou novo. Legado ou FabLab. Sem excecao."

O PROBLEMA DOS ROTEADORES ATUAIS:
  1. Firmware proprietario (TP-Link, Cisco, Netgear)
  2. Sem atualizacao de seguranca apos 2 anos
  3. Backdoors conhecidos de fabricante (NSA, etc)
  4. Hardware fechado, bootloader bloqueado
  5. Interface web lenta e cheia de bugs
  6. Obsolescencia planejada (nao aguenta mais firmware novo)

A SOLUCAO:
  Todo roteador -- seja um TP-Link de 2008 recuperado de e-waste
  ou um roteador FabLab novo -- roda OpenLinuxLive Router Edition.

  - Linux 6.12 LTS (kernel estavel, com patches de seguranca)
  - OpenWrt base (rotagem, firewall, WiFi, DHCP, DNS)
  - OpenProtocol nativo (protocolo da Republica)
  - Mesh networking P2P (roteadores se conectam entre si)
  - OpenLinuxLive pendrive = mesmo OS do cidadao, adaptado

COMO FUNCIONA:
  1. Roteador recuperado de e-waste (OpenReverseLogistics)
  2. Flashear OpenLinuxLive Router Edition
  3. Roteador entra na mesh da Republica automaticamente
  4. Auto-configura (zero configura manual)
  5. Recebe atualizacoes P2P (sem servidor central)
  6. e monitorado por Jarvis (healthcheck da rede)

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections


// ============================================================================
// Router Hardware Tiers
// ============================================================================

classe RouterTier herda de Enum:
    // Niveis de hardware de roteador.
    LEGACY_LOW = "legado_baixo"  // 4MB flash, 32MB RAM (muito antigo)
    LEGACY_MID = "legado_medio"  // 8MB flash, 64MB RAM
    LEGACY_HIGH = "legado_alto"  // 16MB flash, 128MB RAM
    MODERN = "moderno"  // 32MB+ flash, 256MB+ RAM
    FABLAB = "fablab"  // produzido na Republica
    HIGH_END = "high_end"  // multi-radio, server-class


classe RouterRole herda de Enum:
    // Papel na rede da Republica.
    EDGE_MESH = "mesh_borda"  // borda da mesh, WiFi para dispositivos
    BACKBONE = "backbone"  // backbone da mesh (inter-conexao)
    GATEWAY = "gateway"  // gateway para outra rede/nacao
    STARPOINT = "starpoint"  // repetidor/isolado
    COMMUNITY_HUB = "hub_comunitario"  // roteador + edge node (computa + roteia)


classe WirelessStandard herda de Enum:
    WIFI_4 = "802.11n"  // legado, 150-600 Mbps
    WIFI_5 = "802.11ac"  // moderno, 433-1733 Mbps
    WIFI_6 = "802.11ax"  // atual, 600-9600 Mbps
    WIFI_7 = "802.11be"  // futuro, 46Gbps
    OPENPROTOCOL = "OpenProtocol"  // protocolo proprio da Republica


// decorador: @dataclass
classe RouterHardware:
    // Hardware de um roteador.
    seja name: texto = ""
    seja tier: RouterTier = RouterTier.LEGACY_MID
    seja cpu_mhz: inteiro = 400
    seja cpu_cores: inteiro = 1
    seja ram_mb: inteiro = 64
    seja flash_mb: inteiro = 8
    // Radios wireless
    seja wifi_radios: [WirelessStandard] = field(default_factory=() -> [WirelessStandard.WIFI_4])
    seja antenna_count: inteiro = 2
    seja max_clients: inteiro = 32
    // Ports
    seja ethernet_ports: inteiro = 4
    seja ethernet_speed_mbps: inteiro = 100
    seja has_sfp: logico = falso // fibre
    seja has_usb: logico = verdadeiro // USB para pendrive OpenLinuxLive
    // Power
    seja power_draw_w: flutuante = 5.0
    seja poe_supported: logico = falso // Power over Ethernet
    seja solar_capable: logico = falso // pode rodar solar
    // Source
    seja source: texto = "e-waste"
    seja repairability: inteiro = 60


// ============================================================================
// Router OS (OpenLinuxLive Router Edition)
// ============================================================================

classe RouterFeature herda de Enum:
    MESH = "mesh_p2p"  // auto-conexao com outros roteadores
    OPENPROTOCOL = "openprotocol"  // protocolo da Republica
    FIREWALL = "firewall"  // iptables/nftables
    DHCP = "dhcp"  // atribuicao de IP
    DNS = "dns_caching"  // DNS local cache
    VLAN = "vlan"  // redes virtuais
    QOS = "qos"  // priorizacao de trafego
    CAPTIVE_PORTAL = "portal"  // tela de login (se necessario)
    VPN = "vpn_mesh"  // VPN entre roteadores
    IPv6 = "ipv6"  // IPv6 nativo
    BGP = "bgp"  // roteamento inter-nacao
    BANDWIDTH_SHAPING = "shape"  // controle de largura de banda
    INTRUSION_DETECT = "ids"  // deteccao de intrusao
    AUTO_UPDATE = "auto_update"  // atualizacao P2P
    HEALTH_REPORT = "health"  // reporta status ao Jarvis
    TRAFFIC_ANALYSIS = "traffic"  // analise de trafego (anonimizada)
    PENDRIVE_BOOT = "pendrive"  // boot via OpenLinuxLive pendrive


// decorador: @dataclass
classe RouterOS:
    // OpenLinuxLive Router Edition.
    seja kernel: texto = "Linux 6.12 LTS"
    seja base: texto = "OpenWrt 24 (open-source)"
    // Features
    seja features: [RouterFeature] = field(default_factory=() -> [
        RouterFeature.MESH, RouterFeature.OPENPROTOCOL,
        RouterFeature.FIREWALL, RouterFeature.DHCP,
        RouterFeature.DNS, RouterFeature.QOS,
        RouterFeature.IPv6, RouterFeature.AUTO_UPDATE,
        RouterFeature.HEALTH_REPORT,
    ])
    // Boot
    seja boot_from: texto = "flash interna OU pendrive USB"
    seja boot_time_sec: flutuante = 25.0
    // Networking
    seja mesh_protocol: texto = "batman-adv (Layer 2 mesh)"
    seja routing_protocol: texto = "B.A.T.M.A.N. + BGP inter-nacao"
    seja ip_version: texto = "IPv6 nativo + IPv4 legacy"
    seja dns: texto = "dnsmasq (caching resolver)"
    seja firewall: texto = "nftables (stateful, stateles, NAT)"
    // Security
    seja open_ports: [texto] = field(default_factory=() -> []) // ZERO portas abertas por padrao
    seja ssh_access: texto = "chave publica apenas (sem password)"
    seja web_interface: texto = "desativada por padrao (CLI only)"
    // Updates
    seja update_method: texto = "P2P delta (sem servidor central)"
    seja update_frequency: texto = "automatico, noturno"
    seja update_verified: texto = "assinatura criptografica (Ed25519)"
    // Telemetry
    seja telemetry: texto = "ZERO"
    // Compatibility
    seja supported_devices: inteiro = 5000 // 5000+ modelos suportados


// ============================================================================
// Mesh Network Simulator
// ============================================================================

// decorador: @dataclass
classe MeshNode:
    // Um no da mesh network (roteador).
    node_id: texto
    name: texto
    hardware: RouterHardware
    role: RouterRole
    seja os: RouterOS = field(default_factory=RouterOS)
    // Estado
    seja online: logico = verdadeiro
    seja uptime_hours: flutuante = 0
    seja clients_connected: inteiro = 0
    // Mesh
    seja neighbors: [texto] = field(default_factory=list)
    seja hop_count_to_gateway: inteiro = 0
    seja throughput_mbps: flutuante = 0
    // Saude
    seja cpu_usage_pct: flutuante = 0
    seja ram_usage_pct: flutuante = 0
    seja temp_c: flutuante = 0
    seja errors_24h: inteiro = 0


classe MeshNetwork:
    // Rede mesh de roteadores rodando OpenLinuxLive.

    A mesh network da Republica:
    - Cada roteador e um no
    - Roteadores se conectam entre si (WiFi ou cabo)
    - Trafego salta de no em no ate destino
    - Se um no cai, outros assumem (auto-healing)
    - ZERO configuracao manual -- auto-organiza

    Protocolo: B.A.T.M.A.N. (Better Approach To Mobile Adhoc Networking)
    - Layer 2 mesh (parece que todos estao na mesma rede)
    - Auto-descoberta de vizinhos
    - Auto-healing (se no cai, reroteia)
    - Escala para milhares de nos
    // 

    funcao __init__(self):
        self.nodes: {texto: MeshNode} = {}
        self._counter = 0

    funcao add_node(self, name: texto, hardware: RouterHardware,
                 role: RouterRole) -> MeshNode:
        self._counter += 1
        nid = "NODE-{self._counter:04d}"
        node = MeshNode(
            node_id = nid, name=name, hardware=hardware, role=role)
        self.nodes[nid] = node
        retorne node

    funcao connect(self, node_a: texto, node_b: texto):
        // Conectar dois nos da mesh.
        se node_a in self.nodes e node_b in self.nodes entao:
            se node_b nao in self.nodes[node_a].neighbors entao:
                self.nodes[node_a].neighbors.append(node_b)
            se node_a nao in self.nodes[node_b].neighbors entao:
                self.nodes[node_b].neighbors.append(node_a)

    funcao auto_discover(self):
        // Auto-descoberta de vizinhos (simulacao).
        // Em implementacao real: batman-adv faz isso automaticamente
        node_list = list(self.nodes.values())
        para cada (i, node) em enumere(node_list):
            // Conectar com proximos nos na lista (simulacao de proximidade fisica)
            para cada j em intervalo(i + 1, minimo(i + 4, tamanho(node_list))):
                other = node_list[j]
                se other.node_id nao in node.neighbors entao:
                    node.neighbors.append(other.node_id)
                    other.neighbors.append(node.node_id)

    funcao health_check(self) -> {texto: qualquer}:
        // Verificar saude da mesh.
        online = soma(1 para n em self.nodes.values() if n.online)
        offline = soma(1 para n em self.nodes.values() if nao n.online)
        total_clients = soma(n.clients_connected para n em self.nodes.values())
        total_throughput = soma(n.throughput_mbps para n em self.nodes.values())
        avg_hops = nao self.nodes ? np : arredonde(
            soma(n.hop_count_to_gateway para n em self.nodes.values()) /
            maximo(1, tamanho(self.nodes)), 1)

        retorne {
            "total_nodes": tamanho(self.nodes),
            "online": online,
            "offline": offline,
            "uptime_pct": arredonde(online / maximo(1, tamanho(self.nodes)) * 100, 1),
            "total_clients": total_clients,
            "total_throughput_mbps": arredonde(total_throughput, 1),
            "avg_hops_to_gateway": avg_hops,
            "mesh_protocol": "B.A.T.M.A.N.",
            "self_healing": verdadeiro,
        }

    funcao simulate_node_failure(self, node_id: texto) -> {texto: qualquer}:
        // Simular queda de no (auto-healing).
        node = self.nodes.get(node_id)
        se nao node entao:
            retorne {"error": "nao encontrado"}

        node.online = falso
        affected_clients = node.clients_connected

        // Encontrar nos que dependiam deste
        dependents = [n.node_id para n em self.nodes.values()
                     if node_id in n.neighbors e n.online]

        // Auto-healing: nos dependentes buscam nova rota
        rerouted = 0
        para cada did em dependents:
            dep = self.nodes.get(did)
            se dep entao:
                // Encontrar novo vizinho
                para cada other em self.nodes.values():
                    if (other.node_id != did e 
                        other.node_id != node_id e 
                        other.online e 
                        other.node_id nao in dep.neighbors):
                        dep.neighbors.append(other.node_id)
                        rerouted = rerouted + 1
                        interrompa

        retorne {
            "failed_node": node.name,
            "affected_clients": affected_clients,
            "dependent_nodes": tamanho(dependents),
            "rerouted": rerouted,
            "self_healed": rerouted == tamanho(dependents),
            "time_to_heal_sec": 3.0,   // batman-adv converte em ~3s
        }


// ============================================================================
// Legacy Router Flashing
// ============================================================================

classe RouterFlasher:
    // Flasheia roteadores legados com OpenLinuxLive Router Edition.

    PROCESSO:
    1. Roteador recuperado de e-waste (OpenReverseLogistics)
    2. Identificar modelo (OpenHardware database)
    3. Baixar build OpenLinuxLive Router Edition para o modelo
    4. Flashear (via TFTP, serial, ou bootloader exploit)
    5. Roteador entra na mesh automaticamente

    ROTEADORES SUPORTADOS (exemplos):
    - TP-Link: TL-WR841N (2008), Archer C7, TL-WR703N
    - Netgear: R6220, R7000, WNR3500L
    - ASUS: RT-AC68U, RT-N16
    - Linksys: WRT54G (classico!), WRT1900ACS
    - D-Link: DIR-825, DIR-615
    - GL.iNet: AR150, AR300M, B1300 (ja vem com OpenWrt!)
    - Plus 5000+ outros modelos
    // 

    SUPPORTED_ROUTERS = {
        "TP-Link TL-WR841N": {"tier": RouterTier.LEGACY_LOW,
                              "flash": 4, "ram": 32, "year": 2008,
                              "method": "web_interface"},
        "TP-Link Archer C7": {"tier": RouterTier.LEGACY_HIGH,
                              "flash": 16, "ram": 128, "year": 2013,
                              "method": "web_interface"},
        "Linksys WRT54G": {"tier": RouterTier.LEGACY_LOW,
                           "flash": 4, "ram": 16, "year": 2002,
                           "method": "tftp"},
        "Netgear R7000": {"tier": RouterTier.LEGACY_HIGH,
                          "flash": 128, "ram": 256, "year": 2013,
                          "method": "serial_tftp"},
        "GL.iNet AR300M": {"tier": RouterTier.MODERN,
                           "flash": 128, "ram": 128, "year": 2017,
                           "method": "already_openwrt"},
        "FabLab Router v1": {"tier": RouterTier.FABLAB,
                             "flash": 256, "ram": 512, "year": 2026,
                             "method": "native"},
    }

    funcao flash_router(self, model: texto) -> {texto: qualquer}:
        // Simular flash de roteador legado.
        info = self.SUPPORTED_ROUTERS.get(model)
        se nao info entao:
            retorne {"ok": falso, "error": "modelo '{model}' nao suportado"}

        retorne {
            "model": model,
            "ok": verdadeiro,
            "hardware_tier": info["tier"].value,
            "flash_mb": info["flash"],
            "ram_mb": info["ram"],
            "year": info["year"],
            "flash_method": info["method"],
            "new_os": "OpenLinuxLive Router Edition",
            "kernel": "Linux 6.12 LTS",
            "mesh_protocol": "B.A.T.M.A.N.",
            "openprotocol": verdadeiro,
            "telemetry": "ZERO",
            info["flash"] < 16 ? "boot_time_sec": 25 : 15,
            "message": ("{model} ({info['year']}) flasheado com sucesso. "
                       "Entrou na mesh da Republica automaticamente."),
        }


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    // importa numpy as np

    imprima("=" * 80)
    imprima("  OPENLINUXLIVE ROUTER EDITION")
    imprima("  'Todo roteador roda OpenLinuxLive. Sem excecao.'")
    imprima("=" * 80)

    // === 1. OS ===
    imprima("\n\n  === OPENLINUXLIVE ROUTER EDITION ===\n")
    os_spec = RouterOS()
    imprima("  Kernel: {os_spec.kernel}")
    imprima("  Base: {os_spec.base}")
    imprima("  Mesh: {os_spec.mesh_protocol}")
    imprima("  Routing: {os_spec.routing_protocol}")
    imprima("  IP: {os_spec.ip_version}")
    imprima("  DNS: {os_spec.dns}")
    imprima("  Firewall: {os_spec.firewall}")
    imprima("  Boot: {os_spec.boot_from}")
    imprima("  Update: {os_spec.update_method}")
    imprima("  SSH: {os_spec.ssh_access}")
    imprima("  Web UI: {os_spec.web_interface}")
    imprima("  Telemetry: {os_spec.telemetry}")
    imprima("  Dispositivos suportados: {os_spec.supported_devices}+")
    imprima("\n  Features:")
    para cada f em os_spec.features:
        imprima("    - {f.value}")

    // === 2. Legacy Flashing ===
    imprima("\n\n  === FLASH DE ROTEADORES LEGADOS ===\n")

    flasher = RouterFlasher()
    para cada model em flasher.SUPPORTED_ROUTERS:
        result = flasher.flash_router(model)
        imprima("\n  {model}:")
        imprima("    HW: {result['hardware_tier']} ({result['flash_mb']}MB flash, {result['ram_mb']}MB RAM)")
        imprima("    Ano: {result['year']} | Metodo: {result['flash_method']}")
        imprima("    OS: {result['new_os']}")
        imprima("    {result['message']}")

    // === 3. Mesh Network Simulation ===
    imprima("\n\n  === SIMULACAO DE MESH NETWORK ===\n")

    mesh = MeshNetwork()

    // Adicionar roteadores (mistura de legado + FabLab)
    routers_data = [
        ("Gateway Amazonia", RouterTier.MODERN, RouterRole.GATEWAY, 250),
        ("Hub Comunitario 1", RouterTier.FABLAB, RouterRole.COMMUNITY_HUB, 180),
        ("Hub Comunitario 2", RouterTier.FABLAB, RouterRole.COMMUNITY_HUB, 160),
        ("Mesh Norte", RouterTier.LEGACY_HIGH, RouterRole.EDGE_MESH, 45),
        ("Mesh Sul", RouterTier.LEGACY_HIGH, RouterRole.EDGE_MESH, 38),
        ("Mesh Leste", RouterTier.LEGACY_MID, RouterRole.EDGE_MESH, 32),
        ("Mesh Oeste", RouterTier.LEGACY_MID, RouterRole.EDGE_MESH, 28),
        ("Repetidor Colina", RouterTier.LEGACY_LOW, RouterRole.STARPOINT, 18),
    ]

    para name, tier, role, clients in routers_data:
        hw = RouterHardware(tier=tier)
        node = mesh.add_node(name, hw, role)
        node.clients_connected = clients
        node.throughput_mbps = random_throughput(tier)
        node.hop_count_to_gateway = random.randint(0, 4)

    funcao random_throughput(tier):
        retorne {"legado_baixo": 50, "legado_medio": 100, "legado_alto": 300,
                "moderno": 800, "fablab": 1200}.get(tier.value, 100)

    // importa random
    random.seed(42)
    para name, tier, role, clients in routers_data:
        pass // already added

    mesh.auto_discover()

    health = mesh.health_check()
    imprima("  Nos: {health['total_nodes']}")
    imprima("  Online: {health['online']} ({health['uptime_pct']}%)")
    imprima("  Clientes conectados: {health['total_clients']}")
    imprima("  Throughput total: {health['total_throughput_mbps']} Mbps")
    imprima("  Hops medios: {health['avg_hops_to_gateway']}")
    imprima("  Protocolo: {health['mesh_protocol']}")
    imprima("  Auto-healing: {health['self_healing']}")

    imprima("\n  Topologia:")
    para cada node em mesh.nodes.values():
        status = node.online ? "ONLINE" : "OFFLINE"
        imprima("    {node.name:<25} {node.role.value:<20} "
              "{status} | {node.clients_connected} clientes | "
              "{node.throughput_mbps} Mbps | {len(node.neighbors)} vizinhos")

    // === 4. Node Failure + Self-Healing ===
    imprima("\n\n  === AUTO-HEALING (queda de no) ===\n")
    imprima("  Cenário: 'Hub Comunitario 2' cai (160 clientes afetados)")

    // Find hub comunitario 2
    hub2_id = nulo
    para cada (nid, node) em mesh.nodes.items():
        se node.name == "Hub Comunitario 2" entao:
            hub2_id = nid
            interrompa

    se hub2_id entao:
        result = mesh.simulate_node_failure(hub2_id)
        imprima("  No caido: {result['failed_node']}")
        imprima("  Clientes afetados: {result['affected_clients']}")
        imprima("  Nos dependentes: {result['dependent_nodes']}")
        imprima("  Re-roteados: {result['rerouted']}")
        imprima("  Auto-recuperado: {'SIM' if result['self_healed'] else 'PARCIAL'}")
        imprima("  Tempo de recuperacao: {result['time_to_heal_sec']}s")

    health_after = mesh.health_check()
    imprima("\n  Mesh apos falha:")
    imprima("    Online: {health_after['online']}/{health_after['total_nodes']}")
    imprima("    Clientes ainda servidos: {health_after['total_clients']}")

    // === Philosophy ===
    ISP = "provedor de internet"
    imprima("\n\n{'='*80}")
    ISP = "provedor de internet"
    imprima("  FILOSOFIA: ROTEADOR COMO NO DA REPUBLICA")
    imprima("{'='*80}")
    imprima("""
  ROTEADOR TRADICIONAL ROTEADOR OPENLINUXLIVE
  --------------------------------------- ---------------------------------------
  Firmware proprietario OpenLinuxLive (open-source)
  Sem update apos 2 anos Update P2P automatico (noturno)
  Backdoor de fabricante Zero backdoor (codigo aberto)
  Interface web lenta e bugada CLI (configuravel, scriptavel)
  Obsolescencia planejada 5000+ modelos suportados
  Configuracao manual tediosa Auto-configura (mesh auto-descoberta)
  1 roteador por casa (isolado) Mesh: todos se conectam (resiliente)
  ISP controla o roteador Roteador e da Republica
  Se ISP cai, todos fora Se um no cai, outros assumem
  Hardware fechado (bloqueado) Hardware aberto (bootloader livre)

  TODO ROTEADOR DA REPUBLICA:
    1. Recuperado de e-waste (OpenReverseLogistics)
    2. Flasheado com OpenLinuxLive Router Edition
    3. Auto-conecta na mesh (B.A.T.M.A.N.)
    4. Auto-configura (zero setup manual)
    5. Auto-atualiza (P2P delta, noturno)
    4. Auto-atualiza (P2P delta, noturno)
    5. Reporta saude ao Jarvis
    6. Auto-recupera se vizinho cai (3s)

  MESH NETWORK (sem ISP, sem servidor):
    Cada roteador e um NO.
    Nos se conectam entre si.
    Trafego salta de no em no.
    Se um cai, outros reroteiam.
    ZERO configuracao manual.
    Escala para milhares de nos.
    Protocolo: B.A.T.M.A.N. (open-source)

  POR QUE nao PRECISA DE ISP:
    A mesh e a rede.
    Cada roteador encaminha trafego do vizinho.
    Gateways conectam mesh com outras nacoes (fibra escura/satelite).
    Sem provedor. Sem mensalidade. Sem empresa.
    A rede e do povo. A rede e da Republica.

  "Todo roteador da Republica roda OpenLinuxLive.
   Velho ou novo. Legado ou FabLab.
   Sem excecao. Sem firmware proprietario.
   Sem backdoor. Sem ISP.
   A rede e do povo."
// )

```
