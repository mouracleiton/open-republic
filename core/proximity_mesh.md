# OpenRepublic -- Comunicacao por Proximidade (Proximity Mesh)

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/proximity_mesh.py`

**Descricao:** ================================================================
"Hardware se conhece pelo corpo, nao pelo IP."
Dois dispositivos da Republica, quando se aproximam, se comunicam
INDEPENDENTEMENTE de WiFi, internet, ou qualquer infraestrutura.
O PROBLEMA:
  Hoje, dois celulares lado a lado precisam de:
  - Servidor na nuvem (WhatsApp)
  - Ou pareamento manual (Bluetooth)
  - Ou NFC tap (limitado a 4cm)
  - Ou QR code (precisa camera)
  NENHUM funciona offline sem setup.
A SOLUCAO:
  Hardware da Republica usa TODOS os canais simultaneamente:
  - BLE (Bluetooth Low Energy) -- 100m, sempre scaneando
  - UWB (Ultra Wideband) -- 30m, direcional, preciso
  - NFC -- 4cm, toque
  - Ultrasound -- 10m, som inaudivel
  - Luz visivel/IR (LiFi) -- 5m, luz
  - Capacitivo (body coupling) -- toque no corpo
  - Magentic (NFMI) -- 2m, campo magnetico
  O dispositivo usa QUALQUER canal disponivel.
  Se BLE falhou, tenta ultrasound. Se ultrasound falhou, tenta luz.
  O conteudo e o mesmo. O canal e indiferente.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Comunicacao por Proximidade (Proximity Mesh)
================================================================

"Hardware se conhece pelo corpo, nao pelo IP."

Dois dispositivos da Republica, quando se aproximam, se comunicam
INDEPENDENTEMENTE de WiFi, internet, ou qualquer infraestrutura.

O PROBLEMA:
  Hoje, dois celulares lado a lado precisam de:
  - Servidor na nuvem (WhatsApp)
  - Ou pareamento manual (Bluetooth)
  - Ou NFC tap (limitado a 4cm)
  - Ou QR code (precisa camera)
  NENHUM funciona offline sem setup.

A SOLUCAO:
  Hardware da Republica usa TODOS os canais simultaneamente:
  - BLE (Bluetooth Low Energy) -- 100m, sempre scaneando
  - UWB (Ultra Wideband) -- 30m, direcional, preciso
  - NFC -- 4cm, toque
  - Ultrasound -- 10m, som inaudivel
  - Luz visivel/IR (LiFi) -- 5m, luz
  - Capacitivo (body coupling) -- toque no corpo
  - Magentic (NFMI) -- 2m, campo magnetico

  O dispositivo usa QUALQUER canal disponivel.
  Se BLE falhou, tenta ultrasound. Se ultrasound falhou, tenta luz.
  O conteudo e o mesmo. O canal e indiferente.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa defaultdict de collections
// importa random


// ============================================================================
// Communication Channels
// ============================================================================

classe Channel herda de Enum:
    // Canais de comunicacao por proximidade.
    BLE = "ble"  // Bluetooth Low Energy (100m, baixa energia)
    UWB = "uwb"  // Ultra Wideband (30m, direcional, preciso)
    NFC = "nfc"  // Near Field Communication (4cm, toque)
    ULTRASOUND = "ultrassom"  // Som inaudivel (10m)
    LIFI = "lifi"  // Luz visivel/IR (5m, dados por luz)
    BODY = "corpo"  // Body coupling capacitivo (toque)
    MAGNETIC = "magnetico"  // NFMI campo magnetico (2m)
    WIFI_DIRECT = "wifi_direct"  // WiFi Direct (50m, alta velocidade)


// decorador: @dataclass
classe ChannelSpec:
    // Especificacao de cada canal.
    channel: Channel
    range_m: flutuante // alcance em metros
    bandwidth_kbps: flutuante // largura de banda
    latency_ms: flutuante // latencia
    power_mw: flutuante // consumo energetico
    directional: logico // e direcional?
    needs_pairing: logico // precisa pareamento manual?
    penetrate_walls: logico // atravessa parede?
    secure: logico // e criptografado nativamente?


seja CHANNEL_SPECS: {Channel: ChannelSpec} = {
    Channel.BLE: ChannelSpec(Channel.BLE, 100, 256, 8, 5, falso, falso, verdadeiro, verdadeiro),
    Channel.UWB: ChannelSpec(Channel.UWB, 30, 8000, 1, 10, verdadeiro, falso, falso, verdadeiro),
    Channel.NFC: ChannelSpec(Channel.NFC, 0.04, 424, 0.1, 15, falso, verdadeiro, falso, verdadeiro),
    Channel.ULTRASOUND: ChannelSpec(Channel.ULTRASOUND, 10, 10, 20, 1, falso, falso, falso, falso),
    Channel.LIFI: ChannelSpec(Channel.LIFI, 5, 100000, 2, 50, verdadeiro, falso, falso, falso),
    Channel.BODY: ChannelSpec(Channel.BODY, 0.1, 100, 5, 0.1, falso, verdadeiro, falso, verdadeiro),
    Channel.MAGNETIC: ChannelSpec(Channel.MAGNETIC, 2, 128, 3, 2, falso, falso, verdadeiro, verdadeiro),
    Channel.WIFI_DIRECT: ChannelSpec(Channel.WIFI_DIRECT, 50, 54000, 5, 200, falso, falso, verdadeiro, falso),
}


// decorador: @dataclass
classe Device:
    // Um dispositivo da Republica.
    device_id: texto
    name: texto
    seja device_type: texto = ""  // fone, oculos, terminal, tablet, ring, glove
    // Canais suportados
    seja channels: {Channel} = field(default_factory=set)
    // Posicao (para simulacao de proximidade)
    seja pos: Tuple[flutuante, flutuante, flutuante] = (0, 0, 0)
    // Estado
    seja online: logico = verdadeiro
    seja battery_pct: flutuante = 80.0
    // Identidade
    seja owner: texto = ""
    seja trusted: {texto} = field(default_factory=set) // IDs de dispositivos confiaveis


classe ProximityMesh:
    // Mesh de comunicacao por proximidade.

    COMO FUNCIONA:

    1. DISCOVERY (descoberta automatica)
       Cada dispositivo broadcasts "ESTOU AQUI" em TODOS os canais:
       - BLE: beacon a cada 100ms (baixo consumo)
       - UWB: pulse a cada 500ms
       - Ultrasound: chirp a cada 1s (inaudivel)
       - LiFi: flicker LED a cada 200ms

       Qualquer dispositivo da Republica dentro do alcance de QUALQUER
       canal detecta o outro. Sem pareamento. Sem setup.

    2. AUTHENTICATION (identificacao automatica)
       Quando dois dispositivos se detectam:
       - Trocam ID da Republica (chave publica)
       - Verificam na blockchain P2P: e da Republica?
       - Se sim: sao irmaos. Comunicam livremente.
       - Se nao: ignoram (nao e Republica).

    3. CHANNEL SELECTION (melhor canal)
       Dos canais disponíveis, escolhe o MELHOR:
       - Precisa de muita banda? WiFi Direct ou LiFi
       - Precisa de baixo consumo? BLE
       - Precisa de direcao (apontar)? UWB
       - Precisa de toque? NFC ou body coupling
       - Precisa de穿透 parede? BLE ou magnetic

       Se o melhor cai, fallback para proximo disponivel.

    4. DATA TRANSFER (transferencia)
       O payload e INDEPENDENTE do canal.
       Mesmo pacote. Qualquer canal.
       ACK no melhor canal disponivel.
       Se perdeu, reenvia em outro canal.

    5. CONTEXT AWARE (contexto da proximidade)
       - 2 dispositivos a 4cm = NFC (provavelmente toque intencional)
       - 2 dispositivos a 2m = BLE (mesmo ambiente)
       - 2 dispositivos a 30m = UWB (mesmo predio)
       - 2 dispositivos tocando o mesmo corpo = body coupling
       O canal escolhido depende da DISTANCIA = contexto.
    // 

    funcao __init__(self):
        self.devices: {texto: Device} = {}
        self.connections: [Dict] = []
        self._counter = 0

    funcao register(self, device: Device):
        self.devices[device.device_id] = device

    funcao discover(self, device_a: texto, device_b: texto) -> {texto: qualquer}:
        // Descobrir todos os canais disponíveis entre dois dispositivos.
        a = self.devices.get(device_a)
        b = self.devices.get(device_b)
        se nao a ou nao b entao:
            retorne {"error": "dispositivo nao encontrado"}

        // Calcular distancia
        dist = self._distance(a.pos, b.pos)

        // Encontrar canais comuns dentro do alcance
        common_channels = a.channels & b.channels
        available = []
        para cada ch em common_channels:
            spec = CHANNEL_SPECS.get(ch)
            se spec e dist <= spec.range_m entao:
                available.append((ch, spec))

        // Ordenar por prioridade (banda > latencia > consumo)
        available.sort(key=(x) -> (-x[1].bandwidth_kbps, x[1].latency_ms))

        retorne {
            "device_a": a.name,
            "device_b": b.name,
            "distance_m": arredonde(dist, 2),
            "common_channels": [ch.value para ch em common_channels],
            "available_channels": [
                {"channel": ch.value, "range": spec.range_m,
                 "bandwidth": spec.bandwidth_kbps,
                 "latency": spec.latency_ms,
                 "power": spec.power_mw}
                para ch, spec in available
            ],
            available ? "best_channel": available[0][0].value : nulo,
        }

    funcao transfer(self, device_a: texto, device_b: texto,
                 payload: texto, force_channel: Channel = nulo
                 ) -> {texto: qualquer}:
        // Transferir dados entre dispositivos por qualquer canal.
        discovery = self.discover(device_a, device_b)
        se "error" in discovery entao:
            retorne discovery
        se nao  discovery["available_channels"] entao:
            retorne {"ok": falso, "error": "fora de alcance de todos os canais"}

        // Selecionar canal
        se force_channel entao:
            matching = [c para c em discovery["available_channels"]
                       if c["channel"] == force_channel.value]
            se nao matching entao:
                retorne {"ok": falso, "error": "canal {force_channel.value} indisponivel nesta distancia"}
            channel = force_channel
        senao:
            best = discovery["best_channel"]
            channel = next(c para c em Channel if c.value == best)

        spec = CHANNEL_SPECS[channel]

        // Calcular tempo de transferencia
        payload_bytes = tamanho(payload.encode("utf-8"))
        transfer_time_ms = payload_bytes / spec.bandwidth_kbps

        // Simular falha e fallback
        failed = falso
        fallback_used = nulo
        if random.random() < 0.1: // 10% chance de falha no canal primario
            failed = verdadeiro
            // Fallback para proximo canal disponivel
            fallback_channels = [c para c em discovery["available_channels"]
                                if c["channel"] != channel.value]
            se fallback_channels entao:
                fb = fallback_channels[0]
                channel_name = fb["channel"]
                channel = next(c para c em Channel if c.value == channel_name)
                spec = CHANNEL_SPECS[channel]
                transfer_time_ms = payload_bytes / spec.bandwidth_kbps
                fallback_used = channel.value

        self._counter += 1
        result = {
            "transfer_id": "XF-{self._counter:06d}",
            "from": discovery["device_a"],
            "to": discovery["device_b"],
            "payload_size_bytes": payload_bytes,
            "channel": channel.value,
            "channel_fallback_from": fallback_used,
            "bandwidth_kbps": spec.bandwidth_kbps,
            "transfer_time_ms": arredonde(transfer_time_ms, 2),
            "distance_m": discovery["distance_m"],
            "ok": verdadeiro,
            "method": self._context_label(discovery["distance_m"], channel),
        }

        self.connections.append(result)
        retorne result

    // decorador: @staticmethod
    funcao _distance(a: Tuple[flutuante, flutuante, flutuante],
                  b: Tuple[flutuante, flutuante, flutuante]) -> flutuante:
        retorne math.sqrt(
            (a[0]-b[0])**2 + (a[1]-b[0])**2 + (a[2]-b[2])**2)

    // decorador: @staticmethod
    funcao _context_label(dist: flutuante, channel: Channel) -> texto:
        se dist <= 0.05 e channel == Channel.NFC entao:
            retorne "TOQUE (intencional, confirmar)"
        se dist <= 0.1 e channel == Channel.BODY entao:
            retorne "CORPO (mesma pessoa tocando)"
        se dist <= 2 e channel == Channel.MAGNETIC entao:
            retorne "PROXIMO (mesma mesa/abraco)"
        se dist <= 5 entao:
            retorne "MESMO AMBIENTE (mesma sala)"
        se dist <= 30 entao:
            retorne "MESMO PREDIO"
        retorne "LONGE (BLE longo alcance)"


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 75)
    imprima("  COMUNICACAO POR PROXIMIDADE (PROXIMITY MESH)")
    imprima("  'Hardware se conhece pelo corpo, nao pelo IP.'")
    imprima("=" * 75)

    mesh = ProximityMesh()

    // === 1. Channels ===
    imprima("\n\n  === CANAIS DE COMUNICACAO ===\n")
    imprima("  {'Canal':<15} {'Alcance':>8} {'Banda':>10} {'Latencia':>9} "
          "{'Energia':>8} {'Parede':>6} {'Setup'}")
    imprima("  {'-'*75}")
    para cada (ch, spec) em CHANNEL_SPECS.items():
        wall = spec.penetrate_walls ? "sim" : "nao"
        setup = nao  spec.needs_pairing ? "auto" : "manual"
        imprima("  {ch.value:<15} {spec.range_m:>7.2f}m {spec.bandwidth_kbps:>8.0f}kb/s "
              "{spec.latency_ms:>7.0f}ms {spec.power_mw:>6.0f}mW {wall:>6} {setup}")

    // === 2. Devices ===
    imprima("\n\n  === DISPOSITIVOS ===\n")

    devices = [
        Device("DEV-001", "Fone Cleiton", "headphone",
               {Channel.BLE, Channel.UWB, Channel.NFC, Channel.BODY,
                Channel.MAGNETIC, Channel.WIFI_DIRECT, Channel.LIFI},
               pos = (0, 0, 0), owner="C-001"),
        Device("DEV-002", "Oculos Cleiton", "glasses",
               {Channel.BLE, Channel.UWB, Channel.NFC, Channel.WIFI_DIRECT},
               pos = (0.1, 0, 0), owner="C-001"),
        Device("DEV-003", "Ring Cleiton", "ring",
               {Channel.BLE, Channel.NFC, Channel.BODY, Channel.MAGNETIC},
               pos = (0.15, 0, 0), owner="C-001"),
        Device("DEV-004", "Terminal Praca", "terminal",
               {Channel.BLE, Channel.UWB, Channel.NFC, Channel.WIFI_DIRECT, Channel.LIFI},
               pos = (3, 0, 0), owner="comunidade"),
        Device("DEV-005", "Fone Amina", "headphone",
               {Channel.BLE, Channel.UWB, Channel.NFC, Channel.BODY,
                Channel.MAGNETIC, Channel.WIFI_DIRECT},
               pos = (2, 0, 0), owner="C-002"),
        Device("DEV-006", "Tablet Comunitario", "tablet",
               {Channel.BLE, Channel.UWB, Channel.NFC, Channel.WIFI_DIRECT},
               pos = (20, 0, 0), owner="comunidade"),
        Device("DEV-007", "Terminal Parede", "terminal_wall",
               {Channel.BLE, Channel.NFC},
               pos = (50, 0, 0), owner="comunidade"),
    ]

    para cada d em devices:
        mesh.register(d)
        imprima("  {d.name:<20} ({d.device_type}) @ {d.pos} | "
              "{len(d.channels)} canais | dono: {d.owner}")

    // === 3. Discovery Scenarios ===
    imprima("\n\n  === DESCOBERTA POR PROXIMIDADE ===\n")

    scenarios = [
        ("Fone Cleiton + Oculos Cleiton", "DEV-001", "DEV-002"),
        ("Fone Cleiton + Ring Cleiton", "DEV-001", "DEV-003"),
        ("Fone Cleiton + Terminal Praca", "DEV-001", "DEV-004"),
        ("Fone Cleiton + Fone Amina", "DEV-001", "DEV-005"),
        ("Fone Cleiton + Tablet Comunitario", "DEV-001", "DEV-006"),
        ("Fone Cleiton + Terminal Parede", "DEV-001", "DEV-007"),
    ]

    para label, a, b in scenarios:
        result = mesh.discover(a, b)
        imprima("\n  {label}:")
        imprima("    Distancia: {result['distance_m']}m")
        imprima("    Canais disponiveis: {len(result['available_channels'])}")
        se result["available_channels"] entao:
            para cada ch em result["available_channels"][:3]:
                imprima("      {ch['channel']:<12} {ch['bandwidth']:.0f}kb/s "
                      "{ch['latency']:.0f}ms {ch['power']:.0f}mW")
            imprima("    MELHOR: {result['best_channel']}")
        senao:
            imprima("    Fora de alcance de todos os canais")

    // === 4. Transfers ===
    imprima("\n\n  === TRANSFERENCIAS ===\n")

    transfers = [
        ("Fone -> Oculos", "DEV-001", "DEV-002", "Config: tema=dark, font=large"),
        ("Fone -> Ring (PIN unlock)", "DEV-001", "DEV-003", "UNLOCK:PIN=4827"),
        ("Fone -> Terminal Praca (boot)", "DEV-001", "DEV-004",
         "OPENLINUXLIVE:KERNEL:32MB+INITRAMFS:16MB+BASE:256MB"),
        ("Fone -> Fone Amina (mensagem)", "DEV-001", "DEV-005",
         "Ola Amina! Como vai o Sahel?"),
        ("Fone -> Tablet (documento)", "DEV-001", "DEV-006",
         "Documento constitucional: 50KB de texto da Republica..."),
    ]

    para label, a, b, payload in transfers:
        result = mesh.transfer(a, b, payload)
        imprima("\n  {label}:")
        se result.get("ok") entao:
            fb = result.get("channel_fallback_from") ? " (fallback de {result['channel_fallback_from']})" : ""
            imprima("    Canal: {result['channel']}{fb}")
            imprima("    Tamanho: {result['payload_size_bytes']} bytes")
            imprima("    Banda: {result['bandwidth_kbps']:.0f} kb/s")
            imprima("    Tempo: {result['transfer_time_ms']}ms")
            imprima("    Contexto: {result['method']}")
        senao:
            imprima("    ERRO: {result.get('error', '?')}")

    // === Philosophy ===
    p = ("=== " "F" "I" "L" "O" "S" "O" "F" "I" "A" " ===")
    imprima("\n\n{'='*75}")
    imprima("  PRINCIPIOS")
    {p} // nao used, keeping clean
    imprima("{'='*75}")
    imprima("""
  COMUNICACAO TRADICIONAL PROXIMITY MESH
  --------------------------------------- ---------------------------------------
  Precisa WiFi/internet Funciona SEM qualquer infraestrutura
  Precisa servidor na nuvem P2P direto, device-to-device
  Precisa pareamento manual Auto-descoberta em todos os canais
  1 canal por vez (WiFi ou BT) TODOS os canais simultaneamente
  Se WiFi cai, comunicacao morre Se canal cai, fallback automatico
  Configuracao IP (DHCP, DNS) Zero configuracao
  Endereco logico (IP) Proximidade fisica (corpo/distancia)
  Internet para vizinho Vizinho e direto, sem internet

  8 CANAIS QUE O HARDWARE USA:

    1. BLE (Bluetooth LE): 100m, sempre scaneando, 5mW
       -> descoberta + mensagens curtas

    2. UWB (Ultra Wideband): 30m, direcional, preciso
       -> saber DIRECAO do dispositivo (apontar)

    3. NFC: 4cm, toque
       -> confirmacao intencional (tap to pay, tap to boot)

    4. ULTRASOUND: 10m, som inaudivel
       -> quando BLE e bloqueado (agua, metal)

    5. LiFi: 5m, luz visivel/IR
       -> alta velocidade em linha de visao

    6. BODY COUPLING: toque no corpo
       -> 2 dispositivos tocando a mesma pessoa comunicam pelo CORPO

    7. MAGNETIC (NFMI): 2m, campo magnetico
       -> atraves de paredes e corpo

    8. WiFi Direct: 50m, alta velocidade
       -> transferencia de arquivos grandes

  CONTEXTO = DISTANCIA:

    4cm (toque) = NFC (confirmacao intencional)
    10cm (corpo) = body coupling (mesma pessoa)
    2m (abraco/mesa) = magnetic (atraves de parede/corpo)
    5m (sala) = LiFi/BLE (linha de visao)
    30m (predio) = UWB (direcional)
    100m (vizinho) = BLE (longo alcance)

  POR QUE ISTO IMPORTA:

    Voce chega num terminal. Nao precisa WiFi.
    Fone + terminal se detectam por BLE.
    Confirmam com NFC (tap).
    OpenLinuxLive boot pelo body coupling (voce toca terminal, dados passam pelo corpo).
    8 segundos depois: sua Republica carregada.

    Voce encontra Amina na rua.
    Fones se detectam por UWB (direcao).
    Jarvis avisa: "Amina esta a 2m a direita."
    Voce pinca (aceitar contato).
    Mensagem vai por magnetic coupling.
    Sem WiFi. Sem internet. Sem servidor.
    Proximidade. Direto. P2P.

  "Hardware se conhece pelo corpo.
   Nao pelo IP.
   Toque, aproximidade, presenca.
   A rede e fisica. A rede e real.
   Sem servidor. Sem nuvem. Sem empresa."
// )

```
