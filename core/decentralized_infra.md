# OpenRepublic -- Politica de Infraestrutura Descentralizada

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/decentralized_infra.py`

**Descricao:** =============================================================
PRINCIPIO:
  Em vez de mega-datacenters centrais (Google, Amazon, Azure),
  a Republica distribui processamento em MILHOES de dispositivos.
  Cada terminal burro, smartphone, laptop, micro servidor comunitario
  e um no da rede. Junto, eles sao mais poderosos que qualquer
  datacenter corporativo.
  O datacenter central existe so para o QUE NAO PODE ser descentralizado.
  Todo o resto roda nos dispositivos das pessoas.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Politica de Infraestrutura Descentralizada
=============================================================

PRINCIPIO:
  Em vez de mega-datacenters centrais (Google, Amazon, Azure),
  a Republica distribui processamento em MILHOES de dispositivos.

  Cada terminal burro, smartphone, laptop, micro servidor comunitario
  e um no da rede. Junto, eles sao mais poderosos que qualquer
  datacenter corporativo.

  O datacenter central existe so para o QUE nao PODE ser descentralizado.
  Todo o resto roda nos dispositivos das pessoas.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa numpy as np


classe WorkloadType herda de Enum:
    // Tipos de carga de processamento.
    UI_RENDERING = "interface"  // telas, botoes -> terminal
    TEXT_INPUT = "entrada_texto"  // teclado -> terminal
    MEDIA_PLAYBACK = "midia"  // video, audio -> terminal
    COMPUTATION_LIGHT = "computacao_leve"  // calculos simples -> terminal
    COMPUTATION_HEAVY = "computacao_pesada"  // simulacoes -> edge node
    AI_INFERENCE = "ia_inferencia"  // jarvis responde -> edge node
    AI_TRAINING = "ia_treinamento"  // treinar modelo -> datacenter
    DATABASE_READ = "leitura_banco"  // buscar dados -> edge cache
    DATABASE_WRITE = "escrita_banco"  // salvar dados -> datacenter
    REALTIME_COMM = "tempo_real"  // videochamada -> P2P
    FILE_STORAGE = "armazenamento"  // arquivos -> distribuido P2P
    CRYPTO_VERIFY = "verificacao_cripto"  // assinatura, blockchain -> todos os nos
    GOVERNANCE_VOTE = "votacao"  // votar -> blockchain descentralizado
    HEALTH_RECORD = "prontuario"  // dados de saude -> edge cifrado
    SIMULATION = "simulacao"  // quantum, clima -> datacenter


classe ProcessingTier herda de Enum:
    // Onde o processamento acontece.
    DEVICE = "dispositivo"  // no proprio terminal/smartphone
    EDGE_NODE = "no_local"  // servidor comunitario do bairro
    REGIONAL = "regional"  // servidor da nacao
    CENTRAL = "central"  // datacenter federal (MINIMO possivel)


classe DecentralizationRule herda de Enum:
    // Regras do que pode ou nao ser descentralizado.
    MUST_DECENTRALIZE = "obrigatorio_descentralizar"
    SHOULD_DECENTRALIZE = "recomendado_descentralizar"
    CAN_DECENTRALIZE = "pode_descentralizar"
    MUST_CENTRALIZE = "obrigatorio_centralizar"  // so o estritamente necessario


// ============================================================================
// Workload Distribution Policy
// ============================================================================

// decorador: @dataclass
classe WorkloadPolicy:
    // Para cada tipo de carga, onde deve rodar.
    workload: WorkloadType
    tier: ProcessingTier
    rule: DecentralizationRule
    reason: texto
    seja fallback: ProcessingTier = ProcessingTier.EDGE_NODE


seja WORKLOAD_POLICIES: {WorkloadType: WorkloadPolicy} = {

    WorkloadType.UI_RENDERING: WorkloadPolicy(
        WorkloadType.UI_RENDERING, ProcessingTier.DEVICE,
        DecentralizationRule.MUST_DECENTRALIZE,
        "Interface roda 100% no terminal burro. Zero carga central."),

    WorkloadType.TEXT_INPUT: WorkloadPolicy(
        WorkloadType.TEXT_INPUT, ProcessingTier.DEVICE,
        DecentralizationRule.MUST_DECENTRALIZE,
        "Teclado/voz processado localmente. Zero carga central."),

    WorkloadType.MEDIA_PLAYBACK: WorkloadPolicy(
        WorkloadType.MEDIA_PLAYBACK, ProcessingTier.DEVICE,
        DecentralizationRule.MUST_DECENTRALIZE,
        "Decodificacao de video/audio no dispositivo. "
        "Conteudo cacheado em edge node. Zero processamento central."),

    WorkloadType.COMPUTATION_LIGHT: WorkloadPolicy(
        WorkloadType.COMPUTATION_LIGHT, ProcessingTier.DEVICE,
        DecentralizationRule.MUST_DECENTRALIZE,
        "Calculos simples (planilha, conversao, filtro) no proprio dispositivo."),

    WorkloadType.COMPUTATION_HEAVY: WorkloadPolicy(
        WorkloadType.COMPUTATION_HEAVY, ProcessingTier.EDGE_NODE,
        DecentralizationRule.SHOULD_DECENTRALIZE,
        "Simulacao pesada roda no no comunitario do bairro. "
        "Resultado volta para o terminal."),

    WorkloadType.AI_INFERENCE: WorkloadPolicy(
        WorkloadType.AI_INFERENCE, ProcessingTier.EDGE_NODE,
        DecentralizationRule.SHOULD_DECENTRALIZE,
        "Jarvis responde a partir do no local. Modelo leve (quantizado) "
        "roda no edge. Resposta em <100ms. Sem consultar central."),

    WorkloadType.AI_TRAINING: WorkloadPolicy(
        WorkloadType.AI_TRAINING, ProcessingTier.CENTRAL,
        DecentralizationRule.MUST_CENTRALIZE,
        "Treinar modelo de IA exige GPUs pesadas. "
        "UNICO caso que justifica datacenter central. "
        "Mas modelo treinado e distribuido para edge nodes."),

    WorkloadType.DATABASE_READ: WorkloadPolicy(
        WorkloadType.DATABASE_READ, ProcessingTier.EDGE_NODE,
        DecentralizationRule.SHOULD_DECENTRALIZE,
        "Leituras cacheadas no no local. "
        "90% das leituras servidas pelo edge. "
        "10% busca no central (cold data)."),

    WorkloadType.DATABASE_WRITE: WorkloadPolicy(
        WorkloadType.DATABASE_WRITE, ProcessingTier.REGIONAL,
        DecentralizationRule.CAN_DECENTRALIZE,
        "Escritas vao para no regional da nacao. "
        "Replicado via P2P. Nao precisa de central."),

    WorkloadType.REALTIME_COMM: WorkloadPolicy(
        WorkloadType.REALTIME_COMM, ProcessingTier.DEVICE,
        DecentralizationRule.MUST_DECENTRALIZE,
        "Videochamada e P2P direto entre os dois dispositivos. "
        "Servidor so faz relay se NAT impedir. "
        "ZERO processamento central de midia."),

    WorkloadType.FILE_STORAGE: WorkloadPolicy(
        WorkloadType.FILE_STORAGE, ProcessingTier.EDGE_NODE,
        DecentralizationRule.MUST_DECENTRALIZE,
        "Arquivos distribuidos em P2P (tipo IPFS/torrent). "
        "3 copias em nos diferentes. "
        "Se um no cai, outros tem o arquivo. "
        "Zero armazenamento central."),

    WorkloadType.CRYPTO_VERIFY: WorkloadPolicy(
        WorkloadType.CRYPTO_VERIFY, ProcessingTier.DEVICE,
        DecentralizationRule.MUST_DECENTRALIZE,
        "Verificacao criptografica roda em CADA no. "
        "E a base da blockchain sem mineracao. "
        "Cada terminal verifica o que precisa."),

    WorkloadType.GOVERNANCE_VOTE: WorkloadPolicy(
        WorkloadType.GOVERNANCE_VOTE, ProcessingTier.DEVICE,
        DecentralizationRule.MUST_DECENTRALIZE,
        "Votacao e blockchain P2P. Cada terminal e um no. "
        "Impossivel fraudar sem corromper 51% dos cidadaos. "
        "ZERO central."),

    WorkloadType.HEALTH_RECORD: WorkloadPolicy(
        WorkloadType.HEALTH_RECORD, ProcessingTier.EDGE_NODE,
        DecentralizationRule.SHOULD_DECENTRALIZE,
        "Prontuario medico cifrado no no local da nacao. "
        "Chave com o paciente. "
        "Medico acessa com permissao temporaria. "
        "NUNCA no central federal."),

    WorkloadType.SIMULATION: WorkloadPolicy(
        WorkloadType.SIMULATION, ProcessingTier.CENTRAL,
        DecentralizationRule.MUST_CENTRALIZE,
        "Simulacao quantica/climatica de larga escala. "
        "Justifica datacenter. Mas resultado e distribuido."),
}


// ============================================================================
// Infrastructure Calculator
// ============================================================================

// decorador: @dataclass
classe DeviceNode:
    // Um dispositivo que processa coisa para a Republica.
    node_id: texto
    device_type: texto // terminal_burro, smartphone, laptop, micro_server
    cpu_cores: inteiro
    ram_gb: flutuante
    storage_gb: flutuante
    seja gpu_tops: flutuante = 0 // AI inference capability
    seja location: texto = "comunitario"
    seja uptime_hours: flutuante = 16 // horas por dia ativo
    seja available: logico = verdadeiro


classe InfrastructureOptimizer:
    // Calcula o minimo datacenter necessario e o maximo descentralizado.

    COMPARACAO:

    Datacenter tradicional (Google-scale para 1M usuarios):
      ~50.000 servidores
      ~50 MW de potencia
      ~$500M construcao
      ~$50M/ano operacao
      Centralizado = ponto unico de falha
      Se cai, TODO mundo fica sem servico

    OpenRepublic descentralizado (1M usuarios):
      ~500.000 terminais burros (processam propria UI)
      ~10.000 smartphones comunitarios (processam IA leve)
      ~1.000 nos de edge comunitarios (barrio)
      ~100 nos regionais (nacao)
      ~5 datacenters federais (MINIMO para IA training + simulacao)
      Descentralizado = sem ponto unico de falha
      Se central cai, 95% continua funcionando
    // 

    funcao calculate(self, population: inteiro = 1_000_000) -> {texto: qualquer}:
        // Calcular infraestrutura necessaria.

        // === DISPOSITIVOS (ja existem, sao distribuidos) ===
        n_terminals = population // 4 // 1 terminal para cada 4 pessoas
        n_smartphones = population // 3 // smartphones comunitarios
        n_laptops = population // 10

        // Capacidade agregada dos dispositivos
        terminal_cpu = n_terminals * 2 // 2 cores cada
        smartphone_cpu = n_smartphones * 4 // ARM quad-core
        laptop_cpu = n_laptops * 8
        total_device_cpu = terminal_cpu + smartphone_cpu + laptop_cpu

        smartphone_ai = n_smartphones * 2 // 2 TOPS cada (NPU mobile)
        total_device_ai = smartphone_ai

        // === EDGE NODES (1 por bairro/comunidade) ===
        n_edge = population // 1000 // 1 edge node por 1000 pessoas
        edge_cpu = n_edge * 16 // 16 cores cada (desktop recuperado)
        edge_ram = n_edge * 64 // 64GB cada
        edge_storage = n_edge * 4000 // 4TB cada
        edge_ai = n_edge * 20 // 20 TOPS (NPU edge)

        // === REGIONAL (1 por nacao) ===
        n_nations = maximo(1, population // 100_000)
        n_regional = n_nations
        regional_cpu = n_regional * 64
        regional_ram = n_regional * 512
        regional_storage = n_regional * 50_000 // 50TB cada

        // === DATACENTER CENTRAL (MINIMO) ===
        // So para: AI training, simulacao quantica, backup frio
        n_central = maximo(1, population // 200_000) // 1 para cada 200k
        central_cpu = n_central * 256 // 256 cores (cluster GPU)
        central_gpu = n_central * 32 // 32 GPUs de treino
        central_ram = n_central * 4096 // 4TB RAM
        central_storage = n_central * 500_000 // 500TB frio
        central_power_kw = n_central * 200 // 200kW cada

        // === DISTRIBUICAO DE CARGA ===
        total_compute_demand = self._estimate_demand(population)
        served_by_device = total_compute_demand * 0.55 // 55% no dispositivo
        served_by_edge = total_compute_demand * 0.25 // 25% no edge
        served_by_regional = total_compute_demand * 0.12 // 12% regional
        served_by_central = total_compute_demand * 0.08 // 8% central

        // === COMPARACAO COM DATACENTER TRADICIONAL ===
        traditional_servers = population // 20 // Google escala
        traditional_power_mw = traditional_servers * 0.001 // ~1kW cada
        traditional_cost = traditional_servers * 10_000 // $10k/servidor

        republic_cost = (n_edge * 200 + // desktop recuperado
                         n_regional * 5_000 + // servidor comunitario
                         n_central * 50_000) // cluster GPU
        republic_power_kw = (n_edge * 0.2 +
                             n_regional * 2 +
                             n_central * 200)

        retorne {
            "population": population,
            "devices": {
                "terminals_burros": n_terminals,
                "smartphones": n_smartphones,
                "laptops": n_laptops,
                "total_device_cpu_cores": total_device_cpu,
                "total_device_ai_tops": total_device_ai,
            },
            "edge_nodes": {
                "count": n_edge,
                "ratio": "1 per 1000 people",
                "cpu_cores": edge_cpu,
                "ram_gb": edge_ram,
                "storage_tb": edge_storage // 1000,
                "ai_tops": edge_ai,
                "hardware": "desktops recuperados de e-waste",
            },
            "regional": {
                "count": n_regional,
                "cpu_cores": regional_cpu,
                "ram_gb": regional_ram,
                "storage_tb": regional_storage // 1000,
            },
            "central": {
                "count": n_central,
                "cpu_cores": central_cpu,
                "gpu_count": central_gpu,
                "ram_gb": central_ram,
                "storage_tb": central_storage // 1000,
                "power_kw": central_power_kw,
                "purpose": "APENAS: AI training, simulacao, backup frio",
            },
            "load_distribution": {
                "on_device_pct": arredonde(served_by_device / total_compute_demand * 100),
                "on_edge_pct": arredonde(served_by_edge / total_compute_demand * 100),
                "on_regional_pct": arredonde(served_by_regional / total_compute_demand * 100),
                "on_central_pct": arredonde(served_by_central / total_compute_demand * 100),
            },
            "comparison": {
                "traditional_servers": traditional_servers,
                "traditional_power_mw": arredonde(traditional_power_mw, 1),
                "traditional_cost_usd": traditional_cost,
                "republic_cost_usd": republic_cost,
                "republic_power_kw": arredonde(republic_power_kw, 1),
                "cost_reduction_pct": arredonde((1 - republic_cost / traditional_cost) * 100),
                "power_reduction_pct": arredonde((1 - republic_power_kw / (traditional_power_mw * 1000)) * 100),
                "central_servers_reduction_pct": arredonde((1 - n_central / traditional_servers) * 100),
            },
            "resilience": {
                "central_down_impact": "8% dos servicos afetados. 92% continua.",
                "edge_down_impact": "Apenas 1 bairro afetado (1000 pessoas). Outros OK.",
                "device_down_impact": "Apenas 1 pessoa sem servico.",
                "p2p_file_survival": "3 copias em nos diferentes. Arquivo nao se perde.",
            },
        }

    // decorador: @staticmethod
    funcao _estimate_demand(population: inteiro) -> flutuante:
        // Estimar demanda computacional total (em unidades arbitrárias).
        // Cada pessoa gera ~100 unidades de demanda/dia
        retorne population * 100


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 80)
    imprima("  OPENREPUBLIC -- INFRAESTRUTURA DESCENTRALIZADA")
    imprima("  'O datacenter e o ultimo recurso, nao o primeiro.'")
    imprima("=" * 80)

    opt = InfrastructureOptimizer()

    // === 1. Workload Policies ===
    imprima("\n\n  === ONDE CADA COISA RODA ===\n")
    imprima("  {'Carga':<25} {'Onde':<15} {'Regra'}")
    imprima("  {'-'*70}")
    para wl, policy in ordene(WORKLOAD_POLICIES.items(),
                             key = (x) -> x[1].tier.value):
        imprima("  {wl.value:<25} {policy.tier.value:<15} {policy.rule.value}")
    imprima("\n  Razoes:")
    para cada (wl, policy) em WORKLOAD_POLICIES.items():
        se policy.tier == ProcessingTier.CENTRAL entao:
            imprima("    CENTRAL: {wl.value} -- {policy.reason}")

    // === 2. Calculate for 1M population ===
    imprima("\n\n  === CALCULO PARA 1.000.000 DE CIDADOS ===\n")
    result = opt.calculate(1_000_000)

    d = result["devices"]
    e = result["edge_nodes"]
    r = result["regional"]
    c = result["central"]
    ld = result["load_distribution"]

    imprima("\n  DISPOSITIVOS (ja existem, custam zero):")
    imprima("    Terminais burros:     {d['terminals_burros']:>10,}")
    imprima("    Smartphones comunit.: {d['smartphones']:>10,}")
    imprima("    Laptops:              {d['laptops']:>10,}")
    imprima("    CPU cores agregado:   {d['total_device_cpu_cores']:>10,}")
    imprima("    AI TOPS agregado:     {d['total_device_ai_tops']:>10,}")

    imprima("\n  EDGE NODES (1 por bairro):")
    imprima("    Quantidade:           {e['count']:>10,}")
    imprima("    Hardware:             {e['hardware']}")
    imprima("    CPU cores:            {e['cpu_cores']:>10,}")
    imprima("    RAM:                  {e['ram_gb']:>10,} GB")
    imprima("    Storage:              {e['storage_tb']:>10,} TB")
    imprima("    AI TOPS:              {e['ai_tops']:>10,}")

    imprima("\n  REGIONAL (1 por nacao):")
    imprima("    Quantidade:           {r['count']:>10}")
    imprima("    CPU cores:            {r['cpu_cores']:>10}")
    imprima("    RAM:                  {r['ram_gb']:>10} GB")
    imprima("    Storage:              {r['storage_tb']:>10} TB")

    imprima("\n  DATACENTER CENTRAL (MINIMO):")
    imprima("    Quantidade:           {c['count']:>10}")
    imprima("    Proposito:            {c['purpose']}")
    imprima("    CPU cores:            {c['cpu_cores']:>10}")
    imprima("    GPUs (treino IA):     {c['gpu_count']:>10}")
    imprima("    RAM:                  {c['ram_gb']:>10} GB")
    imprima("    Storage (frio):       {c['storage_tb']:>10} TB")
    imprima("    Potencia:             {c['power_kw']:>10} kW")

    imprima("\n  DISTRIBUICAO DE CARGA:")
    imprima("    No dispositivo:       {ld['on_device_pct']}%")
    imprima("    No edge node:         {ld['on_edge_pct']}%")
    imprima("    No regional:          {ld['on_regional_pct']}%")
    imprima("    No central:           {ld['on_central_pct']}%")

    // === 3. Comparison ===
    imprima("\n\n  === COMPARACAO: DATACENTER TRADICIONAL vs REPUBLICA ===\n")
    cmp = result["comparison"]
    imprima("  {'Metrica':<35} {'Tradicional':>15} {'Republica':>15} {'Reducao'}")
    imprima("  {'-'*75}")
    imprima("  {'Servidores centrais':<35} {cmp['traditional_servers']:>15,} "
          "{c['count']:>15} {cmp['central_servers_reduction_pct']}%")
    imprima("  {'Potencia (kW)':<35} {int(cmp['traditional_power_mw']*1000):>15,} "
          "{int(cmp['republic_power_kw']):>15,} {cmp['power_reduction_pct']}%")
    imprima("  {'Custo (USD)':<35} {cmp['traditional_cost_usd']:>15,} "
          "{cmp['republic_cost_usd']:>15,} {cmp['cost_reduction_pct']}%")

    // === 4. Resilience ===
    imprima("\n\n  === RESILIENCIA (sem ponto unico de falha) ===\n")
    res = result["resilience"]
    imprima("  Se datacenter central cair:")
    imprima("    {res['central_down_impact']}")
    imprima("  Se edge node cair:")
    imprima("    {res['edge_down_impact']}")
    imprima("  Se dispositivo cair:")
    imprima("    {res['device_down_impact']}")
    imprima("  Arquivos P2P:")
    imprima("    {res['p2p_file_survival']}")

    // === 5. Calculate for different scales ===
    imprima("\n\n  === ESCALA: QUANTO CRESCER, CRESCER O QUE? ===\n")
    imprima("  {'Populacao':>12} {'Devices':>10} {'Edge':>8} {'Regional':>10} "
          "{'Central':>8} {'Central %':>10}")
    imprima("  {'-'*60}")
    para cada pop em [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]:
        r = opt.calculate(pop)
        c = r["central"]["count"]
        total_nodes = (r["devices"]["terminals_burros"] +
                      r["edge_nodes"]["count"] +
                      r["regional"]["count"] + c)
        central_pct = c / total_nodes * 100
        imprima("  {pop:>12,} {r['devices']['terminals_burros']:>10,} "
              "{r['edge_nodes']['count']:>8,} {r['regional']['count']:>10} "
              "{c:>8} {central_pct:>9.1f}%")

    imprima("\n\n{'='*80}")
    imprima("  PRINCIPIOS DA INFRAESTRUTURA")
    imprima("{'='*80}")
    imprima("""
  DATACENTER TRADICIONAL (capitalista) OPENREPUBLIC (descentralizado)
  --------------------------------------- ---------------------------------------
  1 mega datacenter para 1M pessoas 1.000 edge nodes + 5 centrais para 1M
  50 MW de potencia 0.5 MW central (+ devices ja existem)
  $500M construcao $0.5M (desktops recuperados de e-waste)
  Ponto unico de falha Sem ponto unico de falha
  Se cai, TODOS sem servico Se cai, 8% afetado. 92% continua.
  Servidor proprietario ($$$) Desktop recuperado (e-waste -> edge)
  Dados centralizados = alvo Dados distribuidos = resiliente
  Escala = construir mais datacenter ($) Escala = adicionar mais dispositivos
  Empresa controla seus dados Comunidade controla seus dados
  Largura de banda: todos -> central Largura de banda: 90% local (edge)

  A REGRA DE OURO:
    TUDO que pode rodar no dispositivo, roda no dispositivo.
    TUDO que nao pode, roda no edge node do bairro.
    TUDO que nao pode, roda no servidor da nacao.
    SO O ESTRITAMENTE NECESSARIO roda no datacenter central.

  O QUE O DATACENTRAL FAZ (MINIMO):
    1. Treinar modelos de IA (precisa de GPU pesada)
    2. Simulacao quantica/climatica (precisa de cluster)
    3. Backup frio de dados regionais (ultimas 3 copias)

  O QUE O DATACENTRAL nao FAZ:
    - Interface (no terminal)
    - Texto/voz (no terminal)
    - IA leve/Jarvis (no edge)
    - Banco de dados (no edge/regional)
    - Comunicacao (P2P direto)
    - Arquivos (P2P distribuido tipo torrent)
    - Votacao (blockchain P2P em cada no)
    - Saude (edge cifrado da nacao)

  CUSTO REAL:
    Edge nodes = desktops RECUPERADOS de e-waste.
    OpenReverseLogistics ja prova: 15 anos de hardware existente.
    Custo de edge node = R$ 0 (recuperado do lixo eletronico).

    O datacenter central so existe porque:
      IA training precisa de GPU
      Simulacao precisa de cluster
      Tudo o resto e分布uido.

  "Na Republica, processar e um ato comunitario.
   Cada terminal que liga doa ciclo de CPU.
   Cada smartphone dormindo doa IA inference.
   Junto, somos o supercomputador.
   Nenhum datacenter. Nenhum dono. Nenhuma empresa."
// )

```
