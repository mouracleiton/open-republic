/* OpenRepublic -- Comunicacao por Proximidade (Proximity Mesh) -- gerado de Portugol++ */
#ifndef OPENREPUBLIC_COMUNICACAO_POR_PROXIMIDADE_PROXIMITY_MESH_H
#define OPENREPUBLIC_COMUNICACAO_POR_PROXIMIDADE_PROXIMITY_MESH_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenRepublic -- Comunicacao por Proximidade (Proximity Mesh);
================================================================;
"Hardware se conhece pelo corpo, ! pelo IP.";
Dois dispositivos da Republica, quando se aproximam, se comunicam;
INDEPENDENTEMENTE de WiFi, internet, || qualquer infraestrutura.;
O PROBLEMA:;
Hoje, dois celulares lado a lado precisam de:;
- Servidor na nuvem (WhatsApp);
- Ou pareamento manual (Bluetooth);
- Ou NFC tap (limitado a 4cm);
- Ou QR code (precisa camera);
NENHUM funciona offline sem setup.;
A SOLUCAO:;
Hardware da Republica usa TODOS os canais simultaneamente:;
- BLE (Bluetooth Low Energy) -- 100m, sempre scaneando;
- UWB (Ultra Wideband) -- 30m, direcional, preciso;
- NFC -- 4cm, toque;
- Ultrasound -- 10m, som inaudivel;
- Luz visivel/IR (LiFi) -- 5m, luz;
- Capacitivo (body coupling) -- toque no corpo;
- Magentic (NFMI) -- 2m, campo magnetico;
O dispositivo usa QUALQUER canal disponivel.;
Se BLE falhou, tenta ultrasound. Se ultrasound falhou, tenta luz.;
O conteudo && o mesmo. O canal && indiferente.;
Author: OpenRepublic Team;
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
typedef struct Channel {
    // Canais de comunicacao por proximidade.
    BLE = "ble"  // Bluetooth Low Energy (100m, baixa energia);
    UWB = "uwb"  // Ultra Wideband (30m, direcional, preciso);
    NFC = "nfc"  // Near Field Communication (4cm, toque);
    ULTRASOUND = "ultrassom"  // Som inaudivel (10m);
    LIFI = "lifi"  // Luz visivel/IR (5m, dados por luz);
    BODY = "corpo"  // Body coupling capacitivo (toque);
    MAGNETIC = "magnetico"  // NFMI campo magnetico (2m);
    WIFI_DIRECT = "wifi_direct"  // WiFi Direct (50m, alta velocidade);
// decorador: @dataclass
typedef struct ChannelSpec {
    // Especificacao de cada canal.
    channel: Channel;
    range_m: flutuante // alcance em metros;
    bandwidth_kbps: flutuante // largura de banda;
    latency_ms: flutuante // latencia;
    power_mw: flutuante // consumo energetico;
    directional: logico // && direcional?;
    needs_pairing: logico // precisa pareamento manual?;
    penetrate_walls: logico // atravessa parede?;
    secure: logico // && criptografado nativamente?;
{Channel: ChannelSpec} CHANNEL_SPECS = {;
    Channel.BLE: ChannelSpec(Channel.BLE, 100, 256, 8, 5, false, false, true, true),;
    Channel.UWB: ChannelSpec(Channel.UWB, 30, 8000, 1, 10, true, false, false, true),;
    Channel.NFC: ChannelSpec(Channel.NFC, 0.04, 424, 0.1, 15, false, true, false, true),;
    Channel.ULTRASOUND: ChannelSpec(Channel.ULTRASOUND, 10, 10, 20, 1, false, false, false, false),;
    Channel.LIFI: ChannelSpec(Channel.LIFI, 5, 100000, 2, 50, true, false, false, false),;
    Channel.BODY: ChannelSpec(Channel.BODY, 0.1, 100, 5, 0.1, false, true, false, true),;
    Channel.MAGNETIC: ChannelSpec(Channel.MAGNETIC, 2, 128, 3, 2, false, false, true, true),;
    Channel.WIFI_DIRECT: ChannelSpec(Channel.WIFI_DIRECT, 50, 54000, 5, 200, false, false, true, false),;
};
// decorador: @dataclass
typedef struct Device {
    // Um dispositivo da Republica.
    device_id: texto;
    name: texto;
    char* device_type = ""  // fone, oculos, terminal, tablet, ring, glove;
    // Canais suportados
    {Channel} channels = field(default_factory=set);
    // Posicao (para simulacao de proximidade)
    Tuple[flutuante, flutuante, flutuante] pos = (0, 0, 0);
    // Estado
    bool online = true;
    double battery_pct = 80.0;
    // Identidade
    char* owner = "";
    {texto} trusted = field(default_factory=set) // IDs de dispositivos confiaveis;
typedef struct ProximityMesh {
    // Mesh de comunicacao por proximidade.
    COMO FUNCIONA:;
    1. DISCOVERY (descoberta automatica);
    Cada dispositivo broadcasts "ESTOU AQUI" em TODOS os canais:;
    - BLE: beacon a cada 100ms (baixo consumo);
    - UWB: pulse a cada 500ms;
    - Ultrasound: chirp a cada 1s (inaudivel);
    - LiFi: flicker LED a cada 200ms;
    Qualquer dispositivo da Republica dentro do alcance de QUALQUER;
    canal detecta o outro. Sem pareamento. Sem setup.;
    2. AUTHENTICATION (identificacao automatica);
    Quando dois dispositivos se detectam:;
    - Trocam ID da Republica (chave publica);
    - Verificam na blockchain P2P: && da Republica?;
    - Se sim: sao irmaos. Comunicam livremente.;
    - Se !: ignoram (! && Republica).;
    3. CHANNEL SELECTION (melhor canal);
    Dos canais disponíveis, escolhe o MELHOR:;
    - Precisa de muita banda? WiFi Direct || LiFi;
    - Precisa de baixo consumo? BLE;
    - Precisa de direcao (apontar)? UWB;
    - Precisa de toque? NFC || body coupling;
    - Precisa de穿透 parede? BLE || magnetic;
    Se o melhor cai, fallback para proximo disponivel.;
    4. DATA TRANSFER (transferencia);
    O payload && INDEPENDENTE do canal.;
    Mesmo pacote. Qualquer canal.;
    ACK no melhor canal disponivel.;
    Se perdeu, reenvia em outro canal.;
    5. CONTEXT AWARE (contexto da proximidade);
    - 2 dispositivos a 4cm = NFC (provavelmente toque intencional);
    - 2 dispositivos a 2m = BLE (mesmo ambiente);
    - 2 dispositivos a 30m = UWB (mesmo predio);
    - 2 dispositivos tocando o mesmo corpo = body coupling;
    O canal escolhido depende da DISTANCIA = contexto.;
    //
    void __init__(self) {
        self.devices: {texto: Device} = {};
        self.connections: [Dict] = [];
        self._counter = 0;
    void register(self, device: Device) {
        self.devices[device.device_id] = device;
    {texto: qualquer} discover(self, device_a: texto, device_b: texto) {
        // Descobrir todos os canais disponíveis entre dois dispositivos.
        a = self.devices.get(device_a);
        b = self.devices.get(device_b);
        if (! a || ! b) {
            return {"error": "dispositivo ! encontrado"};
        // Calcular distancia
        dist = self._distance(a.pos, b.pos);
        // Encontrar canais comuns dentro do alcance
        common_channels = a.channels & b.channels;
        available = [];
        /* TODO: iterador C manual para ch em common_channels */
            spec = CHANNEL_SPECS.get(ch);
            if (spec && dist <= spec.range_m) {
                available.append((ch, spec));
        // Ordenar por prioridade (banda > latencia > consumo)
        available.sort(key=(x) -> (-x[1].bandwidth_kbps, x[1].latency_ms));
        return {;
            "device_a": a.name,;
            "device_b": b.name,;
            "distance_m": arredonde(dist, 2),;
            "common_channels": [ch.value para ch em common_channels],;
            "available_channels": [;
                {"channel": ch.value, "range": spec.range_m,;
                "bandwidth": spec.bandwidth_kbps,;
                "latency": spec.latency_ms,;
                "power": spec.power_mw};
                /* para ch, spec in available */
            ],;
            available ? "best_channel": available[0][0].value : NULL,;
        };
    funcao transfer(self, device_a: texto, device_b: texto,
                payload: texto, force_channel: Channel = NULL;
                ) -> {texto: qualquer}:;
        // Transferir dados entre dispositivos por qualquer canal.
        discovery = self.discover(device_a, device_b);
        if ("error" in discovery) {
            return discovery;
        if (!  discovery["available_channels"]) {
            return {"ok": false, "error": "fora de alcance de todos os canais"};
        // Selecionar canal
        if (force_channel) {
            matching = [c para c em discovery["available_channels"];
                    if c["channel"] == force_channel.value];
            if (! matching) {
                return {"ok": false, "error": "canal {force_channel.value} indisponivel nesta distancia"};
            channel = force_channel;
        } else {
            best = discovery["best_channel"];
            channel = next(c para c em Channel if c.value == best);
        spec = CHANNEL_SPECS[channel];
        // Calcular tempo de transferencia
        payload_bytes = sizeof(payload.encode("utf-8"));
        transfer_time_ms = payload_bytes / spec.bandwidth_kbps;
        // Simular falha e fallback
        failed = false;
        fallback_used = NULL;
        if random.random() < 0.1: // 10% chance de falha no canal primario;
            failed = true;
            // Fallback para proximo canal disponivel
            fallback_channels = [c para c em discovery["available_channels"];
                                if c["channel"] != channel.value];
            if (fallback_channels) {
                fb = fallback_channels[0];
                channel_name = fb["channel"];
                channel = next(c para c em Channel if c.value == channel_name);
                spec = CHANNEL_SPECS[channel];
                transfer_time_ms = payload_bytes / spec.bandwidth_kbps;
                fallback_used = channel.value;
        self._counter += 1;
        result = {
            "transfer_id": "XF-{self._counter:06d}",;
            "from": discovery["device_a"],;
            "to": discovery["device_b"],;
            "payload_size_bytes": payload_bytes,;
            "channel": channel.value,;
            "channel_fallback_from": fallback_used,;
            "bandwidth_kbps": spec.bandwidth_kbps,;
            "transfer_time_ms": arredonde(transfer_time_ms, 2),;
            "distance_m": discovery["distance_m"],;
            "ok": true,;
            "method": self._context_label(discovery["distance_m"], channel),;
        };
        self.connections.append(result);
        return result;
    // decorador: @staticmethod
    funcao _distance(a: Tuple[flutuante, flutuante, flutuante],
                b: Tuple[flutuante, flutuante, flutuante]) -> flutuante:;
        return math.sqrt(;
            (a[0]-b[0])**2 + (a[1]-b[0])**2 + (a[2]-b[2])**2);
    // decorador: @staticmethod
    char* _context_label(dist: flutuante, channel: Channel) {
        if (dist <= 0.05 && channel == Channel.NFC) {
            return "TOQUE (intencional, confirmar)";
        if (dist <= 0.1 && channel == Channel.BODY) {
            return "CORPO (mesma pessoa tocando)";
        if (dist <= 2 && channel == Channel.MAGNETIC) {
            return "PROXIMO (mesma mesa/abraco)";
        if (dist <= 5) {
            return "MESMO AMBIENTE (mesma sala)";
        if (dist <= 30) {
            return "MESMO PREDIO";
        return "LONGE (BLE longo alcance)";
// ============================================================================
// Main
// ============================================================================
if (__name__ == "__main__") {
    printf("=" * 75);
    printf("  COMUNICACAO POR PROXIMIDADE (PROXIMITY MESH)");
    printf("  'Hardware se conhece pelo corpo, ! pelo IP.'");
    printf("=" * 75);
    mesh = ProximityMesh();
    // === 1. Channels ===
    printf("\n\n  === CANAIS DE COMUNICACAO ===\n");
    printf("  {'Canal':<15} {'Alcance':>8} {'Banda':>10} {'Latencia':>9} ";
        "{'Energia':>8} {'Parede':>6} {'Setup'}");
    printf("  {'-'*75}");
    /* para cada (ch, spec) em CHANNEL_SPECS.items(): */
        wall = spec.penetrate_walls ? "sim" : "!";
        setup = !  spec.needs_pairing ? "auto" : "manual";
        printf("  {ch.value:<15} {spec.range_m:>7.2f}m {spec.bandwidth_kbps:>8.0f}kb/s ";
            "{spec.latency_ms:>7.0f}ms {spec.power_mw:>6.0f}mW {wall:>6} {setup}");
    // === 2. Devices ===
    printf("\n\n  === DISPOSITIVOS ===\n");
    devices = [;
        Device("DEV-001", "Fone Cleiton", "headphone",;
            {Channel.BLE, Channel.UWB, Channel.NFC, Channel.BODY,;
                Channel.MAGNETIC, Channel.WIFI_DIRECT, Channel.LIFI},;
            pos = (0, 0, 0), owner="C-001"),;
        Device("DEV-002", "Oculos Cleiton", "glasses",;
            {Channel.BLE, Channel.UWB, Channel.NFC, Channel.WIFI_DIRECT},;
            pos = (0.1, 0, 0), owner="C-001"),;
        Device("DEV-003", "Ring Cleiton", "ring",;
            {Channel.BLE, Channel.NFC, Channel.BODY, Channel.MAGNETIC},;
            pos = (0.15, 0, 0), owner="C-001"),;
        Device("DEV-004", "Terminal Praca", "terminal",;
            {Channel.BLE, Channel.UWB, Channel.NFC, Channel.WIFI_DIRECT, Channel.LIFI},;
            pos = (3, 0, 0), owner="comunidade"),;
        Device("DEV-005", "Fone Amina", "headphone",;
            {Channel.BLE, Channel.UWB, Channel.NFC, Channel.BODY,;
                Channel.MAGNETIC, Channel.WIFI_DIRECT},;
            pos = (2, 0, 0), owner="C-002"),;
        Device("DEV-006", "Tablet Comunitario", "tablet",;
            {Channel.BLE, Channel.UWB, Channel.NFC, Channel.WIFI_DIRECT},;
            pos = (20, 0, 0), owner="comunidade"),;
        Device("DEV-007", "Terminal Parede", "terminal_wall",;
            {Channel.BLE, Channel.NFC},;
            pos = (50, 0, 0), owner="comunidade"),;
    ];
    /* TODO: iterador C manual para d em devices */
        mesh.register(d);
        printf("  {d.name:<20} ({d.device_type}) @ {d.pos} | ";
            "{len(d.channels)} canais | dono: {d.owner}");
    // === 3. Discovery Scenarios ===
    printf("\n\n  === DESCOBERTA POR PROXIMIDADE ===\n");
    scenarios = [;
        ("Fone Cleiton + Oculos Cleiton", "DEV-001", "DEV-002"),;
        ("Fone Cleiton + Ring Cleiton", "DEV-001", "DEV-003"),;
        ("Fone Cleiton + Terminal Praca", "DEV-001", "DEV-004"),;
        ("Fone Cleiton + Fone Amina", "DEV-001", "DEV-005"),;
        ("Fone Cleiton + Tablet Comunitario", "DEV-001", "DEV-006"),;
        ("Fone Cleiton + Terminal Parede", "DEV-001", "DEV-007"),;
    ];
    /* para label, a, b in scenarios: */
        result = mesh.discover(a, b);
        printf("\n  {label}:");
        printf("    Distancia: {result['distance_m']}m");
        printf("    Canais disponiveis: {len(result['available_channels'])}");
        if (result["available_channels"]) {
            /* TODO: iterador C manual para ch em result["available_channels"][:3] */
                printf("      {ch['channel']:<12} {ch['bandwidth']:.0f}kb/s ";
                    "{ch['latency']:.0f}ms {ch['power']:.0f}mW");
            printf("    MELHOR: {result['best_channel']}");
        } else {
            printf("    Fora de alcance de todos os canais");
    // === 4. Transfers ===
    printf("\n\n  === TRANSFERENCIAS ===\n");
    transfers = [;
        ("Fone -> Oculos", "DEV-001", "DEV-002", "Config: tema=dark, font=large"),;
        ("Fone -> Ring (PIN unlock)", "DEV-001", "DEV-003", "UNLOCK:PIN=4827"),;
        ("Fone -> Terminal Praca (boot)", "DEV-001", "DEV-004",;
        "OPENLINUXLIVE:KERNEL:32MB+INITRAMFS:16MB+BASE:256MB"),;
        ("Fone -> Fone Amina (mensagem)", "DEV-001", "DEV-005",;
        "Ola Amina! Como vai o Sahel?"),;
        ("Fone -> Tablet (documento)", "DEV-001", "DEV-006",;
        "Documento constitucional: 50KB de texto da Republica..."),;
    ];
    /* para label, a, b, payload in transfers: */
        result = mesh.transfer(a, b, payload);
        printf("\n  {label}:");
        if (result.get("ok")) {
            fb = result.get("channel_fallback_from") ? " (fallback de {result['channel_fallback_from']})" : "";
            printf("    Canal: {result['channel']}{fb}");
            printf("    Tamanho: {result['payload_size_bytes']} bytes");
            printf("    Banda: {result['bandwidth_kbps']:.0f} kb/s");
            printf("    Tempo: {result['transfer_time_ms']}ms");
            printf("    Contexto: {result['method']}");
        } else {
            printf("    ERRO: {result.get('error', '?')}");
    // === Philosophy ===
    p = ("=== " "F" "I" "L" "O" "S" "O" "F" "I" "A" " ===");
    printf("\n\n{'='*75}");
    printf("  PRINCIPIOS");
    {p} // ! used, keeping clean;
    printf("{'='*75}");
    printf(""";
COMUNICACAO TRADICIONAL PROXIMITY MESH;
--------------------------------------- ---------------------------------------;
Precisa WiFi/internet Funciona SEM qualquer infraestrutura;
Precisa servidor na nuvem P2P direto, device-to-device;
Precisa pareamento manual Auto-descoberta em todos os canais;
1 canal por vez (WiFi || BT) TODOS os canais simultaneamente;
Se WiFi cai, comunicacao morre Se canal cai, fallback automatico;
Configuracao IP (DHCP, DNS) Zero configuracao;
Endereco logico (IP) Proximidade fisica (corpo/distancia);
Internet para vizinho Vizinho && direto, sem internet;
8 CANAIS QUE O HARDWARE USA:;
    1. BLE (Bluetooth LE): 100m, sempre scaneando, 5mW;
    -> descoberta + mensagens curtas;
    2. UWB (Ultra Wideband): 30m, direcional, preciso;
    -> saber DIRECAO do dispositivo (apontar);
    3. NFC: 4cm, toque;
    -> confirmacao intencional (tap to pay, tap to boot);
    4. ULTRASOUND: 10m, som inaudivel;
    -> quando BLE && bloqueado (agua, metal);
    5. LiFi: 5m, luz visivel/IR;
    -> alta velocidade em linha de visao;
    6. BODY COUPLING: toque no corpo;
    -> 2 dispositivos tocando a mesma pessoa comunicam pelo CORPO;
    7. MAGNETIC (NFMI): 2m, campo magnetico;
    -> atraves de paredes && corpo;
    8. WiFi Direct: 50m, alta velocidade;
    -> transferencia de arquivos grandes;
CONTEXTO = DISTANCIA:;
    4cm (toque) = NFC (confirmacao intencional);
    10cm (corpo) = body coupling (mesma pessoa);
    2m (abraco/mesa) = magnetic (atraves de parede/corpo);
    5m (sala) = LiFi/BLE (linha de visao);
    30m (predio) = UWB (direcional);
    100m (vizinho) = BLE (longo alcance);
POR QUE ISTO IMPORTA:;
    Voce chega num terminal. Nao precisa WiFi.;
    Fone + terminal se detectam por BLE.;
    Confirmam com NFC (tap).;
    OpenLinuxLive boot pelo body coupling (voce toca terminal, dados passam pelo corpo).;
    8 segundos depois: sua Republica carregada.;
    Voce encontra Amina na rua.;
    Fones se detectam por UWB (direcao).;
    Jarvis avisa: "Amina esta a 2m a direita.";
    Voce pinca (aceitar contato).;
    Mensagem vai por magnetic coupling.;
    Sem WiFi. Sem internet. Sem servidor.;
    Proximidade. Direto. P2P.;
"Hardware se conhece pelo corpo.;
Nao pelo IP.;
Toque, aproximidade, presenca.;
A rede && fisica. A rede && real.;
Sem servidor. Sem nuvem. Sem empresa.";
// )

#endif // OPENREPUBLIC_COMUNICACAO_POR_PROXIMIDADE_PROXIMITY_MESH_H
