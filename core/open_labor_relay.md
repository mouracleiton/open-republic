# OpenLaborRelay

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_labor_relay.py`

**Descricao:** ==============
Sistema de distribuicao de trabalho baseado em relay (revezamento).
Cada servico/sistema que ja faz excelente trabalho vira BENCHMARK -- parametro
de qualidade contra o qual novos sistemas sao medidos.
Fluxo:
    1. BenchmarkRegistry registra os melhores sistemas existentes.
    2. TaskRelay inicia com a tarefa + benchmark alvo.
    3. SkillMatcher escolhe a proxima pessoa no relay.
    4. RelayLeg: pessoa executa sua parte -> QualityGate compara contra benchmark.
    5. Se passar: avanca. Se falhar: outra pessoa assume (anti-bottleneck).
    6. Ao completar: BenchmarkRegistry atualiza o benchmark (continuous improvement).
    7. RelayMetrics registra tudo para transparencia.
Uso:
    >>> from open_labor_relay import LaborRelayEngine, Benchmark, TaskRelay
    >>> engine = LaborRelayEngine()
    >>> engine.registrar_benchmark("build-python", tempo_segundos=120,
    ...                             qualidade=0.92, autor="sistema-build-antigo")
    >>> relay = engine.criar_relay("build-python",
    ...                            pessoas=["ana", "bruno", "carla"])
    >>> resultado = engine.executar_relay(relay)

---

```portugol++

// !/usr/bin/env python3
// -*- coding: utf-8 -*-
// =============================================================================
// open_labor_relay.py
// OpenLaborRelay - Sistema de Distribuicao / Relay de Trabalho na Republica
// =============================================================================
// 
// CONCEITO
// --------
// Todo servico/sistema que ja faz EXCELENTE trabalho vira PARAMETRO (benchmark).
// Novos sistemas sao medidos contra os melhores existentes. Trabalho e distribuido
// como relay: passa de pessoa para pessoa ate completar, como revezamento.
// 
// PRINCIPIOS
// - Excelencia existente vira parametro de comparacao (Benchmark Registry)
// - Trabalho flui como relay (Task Relay)
// - Cada perna do relay passa por Quality Gate contra o benchmark
// - Proxima pessoa escolhida por skill + disponibilidade + carga
// - Familia inteira pode revezar (Family Relay via OpenFamilyLabor)
// - Benchmark evolui com cada relay bem sucedido (Continuous Improvement)
// - Anti-Bottleneck: se alguem trava, relay avanca automaticamente
// - Transparencia total: quem fez o que, quanto tempo, qualidade
// - Templates de workflow por tipo de tarefa
// - Metricas: gargalos, tempo total, quem e melhor em quC0 (Dominio Publico)
// https://creativecommons.org/publicdomain/zero/1.0/
// 
// =============================================================================

// 
OpenLaborRelay
==============

Sistema de distribuicao de trabalho baseado em relay (revezamento).
Cada servico/sistema que ja faz excelente trabalho vira BENCHMARK -- parametro
de qualidade contra o qual novos sistemas sao medidos.

Fluxo:
    1. BenchmarkRegistry registra os melhores sistemas existentes.
    2. TaskRelay inicia com a tarefa + benchmark alvo.
    3. SkillMatcher escolhe a proxima pessoa no relay.
    4. RelayLeg: pessoa executa sua parte -> QualityGate compara contra benchmark.
    5. Se passar: avanca. Se falhar: outra pessoa assume (anti-bottleneck).
    6. Ao completar: BenchmarkRegistry atualiza o benchmark (continuous improvement).
    7. RelayMetrics registra tudo para transparencia.

Uso:
    >>> from open_labor_relay import LaborRelayEngine, Benchmark, TaskRelay
    >>> engine = LaborRelayEngine()
    >>> engine.registrar_benchmark("build-python", tempo_segundos=120,
    ...                             qualidade=0.92, autor="sistema-build-antigo")
    >>> relay = engine.criar_relay("build-python",
    ...                            pessoas=["ana", "bruno", "carla"])
    >>> resultado = engine.executar_relay(relay)
// 

// importa annotations de __future__

// importa json
// importa logging
// importa random
// importa statistics
// importa time
// importa uuid
// importa defaultdict, deque de collections
// importa dataclass, field, asdict de dataclasses
// importa Enum de enum
// importa Path de pathlib
// importa Any, Callable, Dict, List, Optional, Tuple de typing

// ---------------------------------------------------------------------------
// Logging
// ---------------------------------------------------------------------------
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s [OpenLaborRelay] %(levelname)s %(message)s",
)
log = logging.getLogger("OpenLaborRelay")


// ===========================================================================
// Enums
// ===========================================================================

classe EstadoRelay herda de Enum:
    // Estados possiveis de um TaskRelay.
    CRIADO = "criado"
    EM_ANDAMENTO = "em_andamento"
    PAUSADO = "pausado"
    COMPLETO = "completo"
    FALHOU = "falhou"
    CANCELADO = "cancelado"


classe EstadoLeg herda de Enum:
    // Estados possiveis de uma perna (leg) do relay.
    AGUARDANDO = "aguardando"
    EM_EXECUCAO = "em_execucao"
    APROVADO = "aprovado"
    REPROVADO = "reprovado"
    PULADO = "pulado"  // anti-bottleneck
    EXPIRADO = "expirado"


classe TipoWorkflow herda de Enum:
    // Tipos de workflow padrao suportados.
    BUILD = "build"
    REVIEW = "review"
    TEST = "test"
    DEPLOY = "deploy"
    GENERIC = "generic"


classe Prioridade herda de Enum:
    // Niveis de prioridade de uma tarefa.
    P1 = 1 // critico
    P2 = 2 // alto
    P3 = 3 // normal
    P4 = 4 // baixo


// ===========================================================================
// Benchmark
// ===========================================================================

// decorador: @dataclass
classe Benchmark:
    // 
    Representa um sistema/servico que ja faz EXCELENTE trabalho.

    Vira PARAMETRO de comparacao para novos sistemas. O benchmark guarda
    metricas de qualidade, tempo e throughput. Evolui com continuous
    improvement -- cada relay bem sucedido pode melhorar os valores.
    // 
    id: texto
    nome: texto
    seja descricao: texto = ""
    seja autor: texto = ""  // sistema/servico que originalmente entregou excelencia
    seja qualidade_esperada: flutuante = 0.0 // 0.0 a 1.0
    seja tempo_segundos: flutuante = 0.0 // tempo de referencia
    seja throughput_por_hora: flutuante = 0.0 // itens por hora
    seja custo_referencia: flutuante = 0.0 // custo de referencia (opcional)
    seja categoria: texto = "generic"
    seja metadados: {texto: qualquer} = field(default_factory=dict)
    // historico de evolucao (continuous improvement)
    seja historico_qualidade: [flutuante] = field(default_factory=list)
    seja historico_tempo: [flutuante] = field(default_factory=list)
    seja criado_em: flutuante = field(default_factory=time.time)
    seja atualizado_em: flutuante = field(default_factory=time.time)

    funcao __post_init__(self) -> None:
        se nao self.historico_qualidade entao:
            self.historico_qualidade.append(self.qualidade_esperada)
        se nao self.historico_tempo entao:
            self.historico_tempo.append(self.tempo_segundos)

    // decorador: @classmethod
    funcao criar(cls, nome: texto, descricao: texto = "", autor: texto = "",
              seja qualidade_esperada: flutuante = 0.0, tempo_segundos: flutuante = 0.0,
              seja throughput_por_hora: flutuante = 0.0, custo_referencia: flutuante = 0.0,
              seja categoria: texto = "generic", **metadados: qualquer) -> "Benchmark":
        // Cria um Benchmark com id gerado automaticamente.
        retorne cls(
            id = "bench-{uuid.uuid4().hex[:8]}",
            nome = nome,
            descricao = descricao,
            autor = autor,
            qualidade_esperada = qualidade_esperada,
            tempo_segundos = tempo_segundos,
            throughput_por_hora = throughput_por_hora,
            custo_referencia = custo_referencia,
            categoria = categoria,
            metadados = dict(metadados),
        )

    funcao melhorar(self, qualidade: flutuante, tempo: flutuante) -> None:
        // 
        Continuous improvement: se um relay superar o benchmark,
        atualiza o benchmark para o novo melhor valor.
        // 
        se qualidade > self.qualidade_esperada entao:
            self.qualidade_esperada = arredonde(qualidade, 4)
            log.info(
                "Benchmark '%s' melhorado: qualidade -> %.4f",
                self.nome, self.qualidade_esperada,
            )
        se tempo > 0 e (self.tempo_segundos == 0 ou tempo < self.tempo_segundos) entao:
            self.tempo_segundos = arredonde(tempo, 2)
            log.info(
                "Benchmark '%s' melhorado: tempo -> %.2fs",
                self.nome, self.tempo_segundos,
            )
        self.historico_qualidade.append(self.qualidade_esperada)
        self.historico_tempo.append(self.tempo_segundos)
        self.atualizado_em = time.time()

    funcao comparar(self, qualidade: flutuante, tempo: flutuante) -> {texto: qualquer}:
        // Compara um resultado contra o benchmark.
        delta_q = qualidade - self.qualidade_esperada
        delta_t = self.tempo_segundos ? tempo - self.tempo_segundos : 0.0
        retorne {
            "benchmark": self.nome,
            "qualidade_resultado": arredonde(qualidade, 4),
            "qualidade_referencia": self.qualidade_esperada,
            "delta_qualidade": arredonde(delta_q, 4),
            "tempo_resultado": arredonde(tempo, 2),
            "tempo_referencia": arredonde(self.tempo_segundos, 2),
            "delta_tempo": arredonde(delta_t, 2),
            "supera_benchmark": delta_q >= 0,
        }

    funcao resumo(self) -> {texto: qualquer}:
        // Retorna resumo legivel do benchmark.
        retorne {
            "id": self.id,
            "nome": self.nome,
            "autor": self.autor,
            "qualidade_esperada": self.qualidade_esperada,
            "tempo_segundos": self.tempo_segundos,
            "throughput_por_hora": self.throughput_por_hora,
            "categoria": self.categoria,
            "evolucoes": tamanho(self.historico_qualidade),
        }


// ===========================================================================
// RelayLeg (Perna do Relay)
// ===========================================================================

// decorador: @dataclass
classe RelayLeg:
    // 
    Uma perna do relay: uma pessoa/sistema executa sua parte da tarefa.

    Guarda quem fez, quando comecou/terminou, quanto tempo demorou, resultado
    e decisao do quality gate.
    // 
    id: texto
    relay_id: texto
    executor: texto // pessoa ou sistema
    seja estado: EstadoLeg = EstadoLeg.AGUARDANDO
    seja iniciado_em: flutuante? = nulo
    seja finalizado_em: flutuante? = nulo
    seja duracao_segundos: flutuante = 0.0
    seja resultado: {texto: qualquer} = field(default_factory=dict)
    seja nota_qualidade: flutuante = 0.0
    seja aprovado: logico = falso
    seja comentario: texto = ""
    seja ordem: inteiro = 0 // ordem no relay (0 = primeira perna)
    // anti-bottleneck
    seja tentativas: inteiro = 0
    seja timeout_segundos: flutuante = 300.0 // 5 minimo default

    // decorador: @classmethod
    funcao criar(cls, relay_id: texto, executor: texto, ordem: inteiro,
              seja timeout_segundos: flutuante = 300.0) -> "RelayLeg":
        retorne cls(
            id = "leg-{uuid.uuid4().hex[:8]}",
            relay_id = relay_id,
            executor = executor,
            ordem = ordem,
            timeout_segundos = timeout_segundos,
        )

    funcao iniciar(self) -> None:
        self.estado = EstadoLeg.EM_EXECUCAO
        self.iniciado_em = time.time()
        self.tentativas += 1
        log.info("[Leg %s] Iniciada por '%s' (ordem=%d)", self.id, self.executor, self.ordem)

    funcao finalizar(self, resultado: {texto: qualquer}, nota_qualidade: flutuante,
                  aprovado: logico, comentario: texto = "") -> nulo:
        self.finalizado_em = time.time()
        self.duracao_segundos = arredonde(self.finalizado_em - (self.iniciado_em ou self.finalizado_em), 2)
        self.resultado = resultado
        self.nota_qualidade = arredonde(nota_qualidade, 4)
        self.aprovado = aprovado
        self.comentario = comentario
        aprovado ? self.estado = EstadoLeg.APROVADO : EstadoLeg.REPROVADO
        log.info(
            "[Leg %s] Finalizada por '%s': %s (qualidade=%.3f, tempo=%.1fs)",
            self.id, self.executor, self.estado.value, self.nota_qualidade, self.duracao_segundos,
        )

    funcao expirar(self) -> None:
        // Anti-bottleneck: marca a perna como expirada (timeout).
        self.estado = EstadoLeg.EXPIRADO
        log.warning(
            "[Leg %s] Expirada (timeout) para '%s' apos %d tentativa(s)",
            self.id, self.executor, self.tentativas,
        )

    funcao pular(self) -> None:
        // Anti-bottleneck: pula esta perna e passa para a proxima.
        self.estado = EstadoLeg.PULADO
        log.warning("[Leg %s] Pulada para '%s' (anti-bottleneck)", self.id, self.executor)

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {
            "id": self.id,
            "relay_id": self.relay_id,
            "executor": self.executor,
            "estado": self.estado.value,
            "iniciado_em": self.iniciado_em,
            "finalizado_em": self.finalizado_em,
            "duracao_segundos": self.duracao_segundos,
            "resultado": self.resultado,
            "nota_qualidade": self.nota_qualidade,
            "aprovado": self.aprovado,
            "comentario": self.comentario,
            "ordem": self.ordem,
            "tentativas": self.tentativas,
        }


// ===========================================================================
// QualityGate
// ===========================================================================

classe QualityGate:
    // 
    Portao de qualidade: compara o resultado de cada perna do relay contra
    o benchmark registrado. Decide se o resultado passa ou se outra pessoa
    precisa assumir.
    // 

    funcao __init__(self, tolerancia: flutuante = 0.1) -> None:
        // tolerancia: quanto abaixo do benchmark ainda e aceitavel
        self.tolerancia = tolerancia

    funcao avaliar(self, benchmark: Benchmark, qualidade: flutuante,
                tempo: flutuante, resultado: {texto: qualquer}) -> {texto: qualquer}:
        // 
        Avalia resultado da perna contra benchmark.

        Returns:
            dict com aprovado, nota, comentario, comparacao.
        // 
        comparacao = benchmark.comparar(qualidade, tempo)
        limite = benchmark.qualidade_esperada - self.tolerancia
        aprovado = qualidade >= limite

        se aprovado entao:
            comentario = "Qualidade {qualidade:.3f} >= limite {limite:.3f} (tol={self.tolerancia})"
        senao:
            comentario = "Qualidade {qualidade:.3f} < limite {limite:.3f} -- reprovado"

        retorne {
            "aprovado": aprovado,
            "nota": arredonde(qualidade, 4),
            "comentario": comentario,
            "comparacao": comparacao,
            "avaliado_em": time.time(),
        }

    funcao avaliar_leg(self, benchmark: Benchmark, leg: RelayLeg,
                    qualidade: flutuante, tempo: flutuante,
                    resultado: {texto: qualquer}) -> {texto: qualquer}:
        // Avalia e ja aplica resultado no RelayLeg.
        avaliacao = self.avaliar(benchmark, qualidade, tempo, resultado)
        leg.finalizar(
            resultado = resultado,
            nota_qualidade = qualidade,
            aprovado = avaliacao["aprovado"],
            comentario = avaliacao["comentario"],
        )
        retorne avaliacao


// ===========================================================================
// SkillMatcher
// ===========================================================================

// decorador: @dataclass
classe Pessoa:
    // Representa uma pessoa/sistema participante do relay.
    id: texto
    nome: texto
    seja habilidades: {texto: flutuante} = field(default_factory=dict) // skill -> nivel 0-1
    seja disponivel: logico = verdadeiro
    seja carga_atual: inteiro = 0 // numero de tarefas ativas
    seja carga_maxima: inteiro = 5
    seja familia_id: texto? = nulo
    seja historico_relays: inteiro = 0
    seja soma_qualidade: flutuante = 0.0 // soma das qualidades (para media)

    funcao nivel(self, skill: texto) -> flutuante:
        retorne self.habilidades.get(skill, 0.0)

    funcao carga_pct(self) -> flutuante:
        // Percentual de carga (0.0 a 1.0).
        se self.carga_maxima <= 0 entao:
            retorne 1.0
        retorne minimo(self.carga_atual / self.carga_maxima, 1.0)

    funcao disponibilidade_pct(self) -> flutuante:
        // 1.0 = totalmente livre, 0.0 = sem espaco.
        se nao self.disponivel entao:
            retorne 0.0
        retorne maximo(0.0, 1.0 - self.carga_pct())

    funcao qualidade_media(self) -> flutuante:
        se self.historico_relays == 0 entao:
            retorne 0.0
        retorne self.soma_qualidade / self.historico_relays

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {
            "id": self.id,
            "nome": self.nome,
            "habilidades": dict(self.habilidades),
            "disponivel": self.disponivel,
            "carga_atual": self.carga_atual,
            "carga_maxima": self.carga_maxima,
            "familia_id": self.familia_id,
            "historico_relays": self.historico_relays,
            "qualidade_media": arredonde(self.qualidade_media(), 4),
        }


classe SkillMatcher:
    // 
    Escolhe a proxima pessoa no relay baseando-se em:
      - skill (habilidade na categoria do benchmark)
      - disponibilidade (esta livre?)
      - carga (tem espaco?)
      - qualidade historica
    // 

    funcao __init__(self) -> None:
        self.pessoas: {texto: Pessoa} = {}

    funcao registrar(self, pessoa: Pessoa) -> None:
        self.pessoas[pessoa.id] = pessoa
        log.info("Pessoa registrada: '%s' (%s)", pessoa.nome, pessoa.id)

    funcao obter(self, pessoa_id: texto) retorna Pessoa?:
        retorne self.pessoas.get(pessoa_id)

    funcao _score(self, pessoa: Pessoa, skill: texto, skill_weight: flutuante = 0.5,
               seja dispo_weight: flutuante = 0.3, hist_weight: flutuante = 0.2) -> flutuante:
        // Score composto: skill + disponibilidade + qualidade historica.
        nivel = pessoa.nivel(skill)
        dispo = pessoa.disponibilidade_pct()
        hist = minimo(pessoa.qualidade_media(), 1.0)
        retorne (nivel * skill_weight) + (dispo * dispo_weight) + (hist * hist_weight)

    funcao proximo(self, skill: texto, excluir: set? = nulo,
                seja limite: inteiro = 5) -> List[(Pessoa, flutuante)]:
        // 
        Retorna as melhores pessoas para a skill, ordenadas por score.

        Args:
            skill: habilidade necessaria (categoria do benchmark).
            excluir: ids de pessoas a excluir (ja fizeram parte do relay).
            limite: maximo de pessoas a retornar.
        // 
        excluir = excluir ou set()
        candidatos = [
            (p, self._score(p, skill))
            para p em self.pessoas.values()
            if p.id nao in excluir e p.disponibilidade_pct() > 0
        ]
        candidatos.sort(key=(x) -> x[1], reverse=verdadeiro)
        retorne candidatos[:limite]

    funcao melhor(self, skill: texto, excluir: set? = None) retorna Pessoa?:
        // Retorna a melhor pessoa para a skill.
        result = self.proximo(skill, excluir=excluir, limite=1)
        result ? retorne result[0][0] : nulo

    funcao listar_disponiveis(self, skill: texto? = None) -> [Pessoa]:
        // Lista pessoas disponiveis, opcionalmente filtrando por skill > 0.
        result = []
        para cada p em self.pessoas.values():
            se p.disponibilidade_pct() <= 0 entao:
                continue
            se skill e p.nivel(skill) <= 0 entao:
                continue
            result.append(p)
        retorne result

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {pid: p.to_dict() para pid, p in self.pessoas.items()}


// ===========================================================================
// TaskRelay
// ===========================================================================

// decorador: @dataclass
classe TaskRelay:
    // 
    Representa uma tarefa distribuida como relay (revezamento).

    A tarefa comeca com a pessoa A, passa para B, C, etc. Cada perna (leg)
    e avaliada contra o benchmark. O relay termina quando todas as pernas
    necessarias sao completadas ou quando uma perna e aprovada como
    suficiente (modo single-leg).
    // 
    id: texto
    nome: texto
    benchmark_id: texto
    seja workflow_tipo: TipoWorkflow = TipoWorkflow.GENERIC
    seja prioridade: Prioridade = Prioridade.P3
    seja estado: EstadoRelay = EstadoRelay.CRIADO
    seja descricao: texto = ""
    seja pernas: [RelayLeg] = field(default_factory=list)
    seja pessoa_inicial: texto? = nulo
    seja pessoas_disponiveis: [texto] = field(default_factory=list)
    // configuracao
    seja max_pernas: inteiro = 5 // limite de revezamento
    seja min_pernas: inteiro = 1 // minimo para considerar completo
    seja parar_ao_aprovar: logico = verdadeiro // para se uma perna para aprovada
    seja timeout_por_perna: flutuante = 300.0 // segundos
    seja anti_bottleneck: logico = verdadeiro // pula automaticamente se travar
    seja max_tentativas_por_perna: inteiro = 2
    // familia
    seja familia_id: texto? = nulo // se relay familiar
    // metricas
    seja criado_em: flutuante = field(default_factory=time.time)
    seja iniciado_em: flutuante? = nulo
    seja finalizado_em: flutuante? = nulo
    seja duracao_total_segundos: flutuante = 0.0
    // resultado final
    seja resultado_final: {texto: qualquer} = field(default_factory=dict)
    seja metadados: {texto: qualquer} = field(default_factory=dict)

    // decorador: @classmethod
    funcao criar(cls, nome: texto, benchmark_id: texto,
              seja workflow_tipo: TipoWorkflow = TipoWorkflow.GENERIC,
              seja prioridade: Prioridade = Prioridade.P3,
              seja pessoas: Optional[[texto]] = nulo,
              seja pessoa_inicial: texto? = nulo,
              seja descricao: texto = "",
              seja max_pernas: inteiro = 5,
              seja familia_id: texto? = nulo,
              **metadados: qualquer) -> "TaskRelay":
        retorne cls(
            id = "relay-{uuid.uuid4().hex[:10]}",
            nome = nome,
            benchmark_id = benchmark_id,
            workflow_tipo = workflow_tipo,
            prioridade = prioridade,
            descricao = descricao,
            pessoas_disponiveis = list(pessoas ou []),
            pessoa_inicial = pessoa_inicial,
            max_pernas = max_pernas,
            familia_id = familia_id,
            metadados = dict(metadados),
        )

    funcao perna_atual(self) retorna RelayLeg?:
        // Retorna a perna em execucao ou aguardando.
        para cada leg em self.pernas:
            se leg.estado in (EstadoLeg.AGUARDANDO, EstadoLeg.EM_EXECUCAO) entao:
                retorne leg
        retorne nulo

    funcao pernas_completas(self) -> [RelayLeg]:
        retorne [l para l em self.pernas if l.estado == EstadoLeg.APROVADO]

    funcao pernas_reprovadas(self) -> [RelayLeg]:
        retorne [l para l em self.pernas if l.estado == EstadoLeg.REPROVADO]

    funcao pernas_puladas(self) -> [RelayLeg]:
        retorne [l para l em self.pernas if l.estado in (EstadoLeg.PULADO, EstadoLeg.EXPIRADO)]

    funcao ultima_aprovada(self) retorna RelayLeg?:
        aprovadas = self.pernas_completas()
        aprovadas ? retorne aprovadas[-1] : nulo

    funcao executada_por(self) -> [texto]:
        // Lista de pessoas que executaram pernas (transparencia).
        retorne [l.executor para l em self.pernas if l.estado in (
            EstadoLeg.APROVADO, EstadoLeg.REPROVADO
        )]

    funcao adicionar_perna(self, executor: texto) -> RelayLeg:
        // Adiciona uma nova perna ao relay.
        ordem = tamanho(self.pernas)
        leg = RelayLeg.criar(
            relay_id = self.id,
            executor = executor,
            ordem = ordem,
            timeout_segundos = self.timeout_por_perna,
        )
        self.pernas.append(leg)
        retorne leg

    funcao iniciar(self) -> None:
        self.estado = EstadoRelay.EM_ANDAMENTO
        self.iniciado_em = time.time()

    funcao completar(self, resultado: {texto: qualquer}) -> None:
        self.estado = EstadoRelay.COMPLETO
        self.finalizado_em = time.time()
        self.duracao_total_segundos = arredonde(
            self.finalizado_em - (self.iniciado_em ou self.finalizado_em), 2
        )
        self.resultado_final = resultado
        log.info(
            "[Relay %s] COMPLETO em %.1fs (%d pernas, %d aprovadas)",
            self.id, self.duracao_total_segundos,
            tamanho(self.pernas), tamanho(self.pernas_completas()),
        )

    funcao falhar(self, motivo: texto) -> None:
        self.estado = EstadoRelay.FALHOU
        self.finalizado_em = time.time()
        self.resultado_final = {"motivo": motivo}
        log.error("[Relay %s] FALHOU: %s", self.id, motivo)

    funcao cancelar(self, motivo: texto = "cancelado pelo usuario") -> None:
        self.estado = EstadoRelay.CANCELADO
        self.finalizado_em = time.time()
        self.resultado_final = {"motivo": motivo}
        log.info("[Relay %s] CANCELADO: %s", self.id, motivo)

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {
            "id": self.id,
            "nome": self.nome,
            "benchmark_id": self.benchmark_id,
            "workflow_tipo": self.workflow_tipo.value,
            "prioridade": self.prioridade.name,
            "estado": self.estado.value,
            "descricao": self.descricao,
            "pernas": [l.to_dict() para l em self.pernas],
            "pessoa_inicial": self.pessoa_inicial,
            "pessoas_disponiveis": list(self.pessoas_disponiveis),
            "max_pernas": self.max_pernas,
            "min_pernas": self.min_pernas,
            "parar_ao_aprovar": self.parar_ao_aprovar,
            "anti_bottleneck": self.anti_bottleneck,
            "familia_id": self.familia_id,
            "criado_em": self.criado_em,
            "iniciado_em": self.iniciado_em,
            "finalizado_em": self.finalizado_em,
            "duracao_total_segundos": self.duracao_total_segundos,
            "resultado_final": self.resultado_final,
            "metadados": self.metadados,
        }


// ===========================================================================
// BenchmarkRegistry
// ===========================================================================

classe BenchmarkRegistry:
    // 
    Registro central de benchmarks.

    Cada servico/sistema que ja faz EXCELENTE trabalho e registrado aqui
    como parametro de qualidade. Novos sistemas e novos relays sao medidos
    contra esses benchmarks.
    // 

    funcao __init__(self) -> None:
        self.benchmarks: {texto: Benchmark} = {}
        self._por_categoria: Dict[texto, [texto]] = defaultdict(list)

    funcao registrar(self, benchmark: Benchmark) -> Benchmark:
        // Registra um novo benchmark.
        self.benchmarks[benchmark.id] = benchmark
        se benchmark.id nao in self._por_categoria[benchmark.categoria] entao:
            self._por_categoria[benchmark.categoria].append(benchmark.id)
        log.info(
            "Benchmark registrado: '%s' (cat=%s, qualidade=%.3f)",
            benchmark.nome, benchmark.categoria, benchmark.qualidade_esperada,
        )
        retorne benchmark

    funcao registrar_rapido(self, nome: texto, descricao: texto = "", autor: texto = "",
                         seja qualidade_esperada: flutuante = 0.0, tempo_segundos: flutuante = 0.0,
                         seja throughput_por_hora: flutuante = 0.0, custo_referencia: flutuante = 0.0,
                         seja categoria: texto = "generic", **metadados: qualquer) -> Benchmark:
        // Cria e registra um benchmark em um passo.
        bench = Benchmark.criar(
            nome = nome, descricao=descricao, autor=autor,
            qualidade_esperada = qualidade_esperada,
            tempo_segundos = tempo_segundos,
            throughput_por_hora = throughput_por_hora,
            custo_referencia = custo_referencia,
            categoria = categoria, **metadados,
        )
        retorne self.registrar(bench)

    funcao obter(self, benchmark_id: texto) retorna Benchmark?:
        retorne self.benchmarks.get(benchmark_id)

    funcao obter_por_nome(self, nome: texto) retorna Benchmark?:
        para cada b em self.benchmarks.values():
            se b.nome == nome entao:
                retorne b
        retorne nulo

    funcao listar(self, categoria: texto? = None) -> [Benchmark]:
        se categoria entao:
            ids = self._por_categoria.get(categoria, [])
            retorne [self.benchmarks[i] para i em ids if i in self.benchmarks]
        retorne list(self.benchmarks.values())

    funcao remover(self, benchmark_id: texto) -> logico:
        bench = self.benchmarks.pop(benchmark_id, nulo)
        se bench entao:
            cat = bench.categoria
            se benchmark_id in self._por_categoria[cat] entao:
                self._por_categoria[cat].remove(benchmark_id)
            log.info("Benchmark removido: '%s'", bench.nome)
            retorne verdadeiro
        retorne falso

    funcao melhorar(self, benchmark_id: texto, qualidade: flutuante, tempo: flutuante) -> logico:
        // Continuous improvement: atualiza benchmark se superado.
        bench = self.obter(benchmark_id)
        se bench entao:
            bench.melhorar(qualidade, tempo)
            retorne verdadeiro
        retorne falso

    funcao benchmark_categoria(self, categoria: texto) retorna Benchmark?:
        // Retorna o melhor benchmark de uma categoria.
        benchmarks = self.listar(categoria)
        se nao benchmarks entao:
            retorne nulo
        retorne maximo(benchmarks, key=(b) -> b.qualidade_esperada)

    funcao categorias(self) -> [texto]:
        retorne list(self._por_categoria.keys())

    funcao resumo(self) -> {texto: qualquer}:
        retorne {
            "total_benchmarks": tamanho(self.benchmarks),
            "categorias": {cat: tamanho(ids) para cat, ids in self._por_categoria.items()},
            "benchmarks": [b.resumo() para b em self.benchmarks.values()],
        }

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {
            bid: {
                **b.resumo(),
                "descricao": b.descricao,
                "historico_qualidade": b.historico_qualidade,
                "historico_tempo": b.historico_tempo,
            }
            para bid, b in self.benchmarks.items()
        }


// ===========================================================================
// WorkflowTemplate
// ===========================================================================

// decorador: @dataclass
classe WorkflowTemplate:
    // 
    Template de workflow: define o padrao de relay para um tipo de tarefa.

    Exemplo: workflow de BUILD pode ter 3 pernas (compilar, testar, empacotar),
    cada uma com skill necessaria e timeout diferente.
    // 
    id: texto
    nome: texto
    tipo: TipoWorkflow
    seja descricao: texto = ""
    // lista de estagios: cada estagio e (skill_necessaria, descricao, timeout)
    seja estagios: List[{texto: qualquer}] = field(default_factory=list)
    seja parar_ao_aprovar: logico = falso // templates geralmente precisam de todas as pernas
    seja benchmark_categoria: texto = "generic"
    seja prioridade_padrao: Prioridade = Prioridade.P3
    seja metadados: {texto: qualquer} = field(default_factory=dict)

    // decorador: @classmethod
    funcao criar(cls, nome: texto, tipo: TipoWorkflow,
              seja estagios: Optional[List[{texto: qualquer}]] = nulo,
              seja descricao: texto = "",
              seja parar_ao_aprovar: logico = falso,
              seja benchmark_categoria: texto = "generic",
              seja prioridade_padrao: Prioridade = Prioridade.P3,
              **metadados: qualquer) -> "WorkflowTemplate":
        retorne cls(
            id = "wf-{uuid.uuid4().hex[:8]}",
            nome = nome,
            tipo = tipo,
            estagios = list(estagios ou []),
            descricao = descricao,
            parar_ao_aprovar = parar_ao_aprovar,
            benchmark_categoria = benchmark_categoria,
            prioridade_padrao = prioridade_padrao,
            metadados = dict(metadados),
        )

    funcao adicionar_estagio(self, skill: texto, descricao: texto = "",
                          seja timeout: flutuante = 300.0,
                          seja obrigatorio: logico = verdadeiro) -> nulo:
        self.estagios.append({
            "skill": skill,
            "descricao": descricao,
            "timeout": timeout,
            "obrigatorio": obrigatorio,
        })

    funcao num_estagios(self) -> inteiro:
        retorne tamanho(self.estagios)

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo.value,
            "descricao": self.descricao,
            "estagios": list(self.estagios),
            "parar_ao_aprovar": self.parar_ao_aprovar,
            "benchmark_categoria": self.benchmark_categoria,
            "prioridade_padrao": self.prioridade_padrao.name,
        }


classe WorkflowTemplateRegistry:
    // Registro de templates de workflow por tipo.

    funcao __init__(self) -> None:
        self.templates: {texto: WorkflowTemplate} = {}
        self._tipos: {TipoWorkflow: texto} = {}
        self._inicializar_padroes()

    funcao _inicializar_padroes(self) -> None:
        // Cria templates padrao para build, review, test, deploy.
        // BUILD
        build = WorkflowTemplate.criar(
            nome = "Build Padrao",
            tipo = TipoWorkflow.BUILD,
            benchmark_categoria = "build",
            parar_ao_aprovar = falso,
        )
        build.adicionar_estagio("compilacao", "Compilar codigo", timeout=120)
        build.adicionar_estagio("lint", "Rodar linter e analise estatica", timeout=60)
        build.adicionar_estagio("empacotamento", "Empacotar artefato", timeout=90)
        self.registrar(build)

        // REVIEW
        review = WorkflowTemplate.criar(
            nome = "Code Review Padrao",
            tipo = TipoWorkflow.REVIEW,
            benchmark_categoria = "review",
            parar_ao_aprovar = falso,
        )
        review.adicionar_estagio("revisao_seguranca", "Revisao de seguranca", timeout=180)
        review.adicionar_estagio("revisao_qualidade", "Revisao de qualidade", timeout=180)
        self.registrar(review)

        // TEST
        test = WorkflowTemplate.criar(
            nome = "Test Padrao",
            tipo = TipoWorkflow.TEST,
            benchmark_categoria = "test",
            parar_ao_aprovar = falso,
        )
        test.adicionar_estagio("teste_unitario", "Testes unitarios", timeout=120)
        test.adicionar_estagio("teste_integracao", "Testes de integracao", timeout=240)
        test.adicionar_estagio("teste_e2e", "Testes end-to-end", timeout=300)
        self.registrar(test)

        // DEPLOY
        deploy = WorkflowTemplate.criar(
            nome = "Deploy Padrao",
            tipo = TipoWorkflow.DEPLOY,
            benchmark_categoria = "deploy",
            parar_ao_aprovar = falso,
        )
        deploy.adicionar_estagio("pre_deploy", "Checagens pre-deploy", timeout=60)
        deploy.adicionar_estagio("deploy", "Executar deploy", timeout=180)
        deploy.adicionar_estagio("post_deploy", "Validacao post-deploy", timeout=120)
        self.registrar(deploy)

    funcao registrar(self, template: WorkflowTemplate) -> WorkflowTemplate:
        self.templates[template.id] = template
        self._tipos[template.tipo] = template.id
        log.info("Template registrado: '%s' (%s)", template.nome, template.tipo.value)
        retorne template

    funcao obter(self, template_id: texto) retorna WorkflowTemplate?:
        retorne self.templates.get(template_id)

    funcao obter_por_tipo(self, tipo: TipoWorkflow) retorna WorkflowTemplate?:
        tid = self._tipos.get(tipo)
        tid ? retorne self.templates.get(tid) : nulo

    funcao listar(self) -> [WorkflowTemplate]:
        retorne list(self.templates.values())

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {tid: t.to_dict() para tid, t in self.templates.items()}


// ===========================================================================
// FamilyRelayIntegration (OpenFamilyLabor)
// ===========================================================================

// decorador: @dataclass
classe Familia:
    // Representa uma familia no OpenFamilyLabor.
    id: texto
    nome: texto
    seja membros: [texto] = field(default_factory=list) // ids de pessoas
    seja especialidade_coletiva: {texto: flutuante} = field(default_factory=dict)
    seja disponivel: logico = verdadeiro

    funcao melhor_skill(self) retorna texto?:
        se nao self.especialidade_coletiva entao:
            retorne nulo
        retorne maximo(self.especialidade_coletiva, key=self.especialidade_coletiva.get)

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {
            "id": self.id,
            "nome": self.nome,
            "membros": list(self.membros),
            "especialidade_coletiva": dict(self.especialidade_coletiva),
            "disponivel": self.disponivel,
        }


classe FamilyRelayIntegration:
    // 
    Integracao com OpenFamilyLabor.

    Permite que uma familia inteira reveze numa tarefa. O relay pode
    passar de membro em membro da familia, respeitando especialidades.
    // 

    funcao __init__(self, skill_matcher: SkillMatcher) -> None:
        self.skill_matcher = skill_matcher
        self.familias: {texto: Familia} = {}

    funcao registrar_familia(self, familia: Familia) -> Familia:
        self.familias[familia.id] = familia
        log.info("Familia registrada: '%s' (%d membros)", familia.nome, tamanho(familia.membros))
        retorne familia

    funcao obter_familia(self, familia_id: texto) retorna Familia?:
        retorne self.familias.get(familia_id)

    funcao membros_disponiveis(self, familia_id: texto,
                            seja skill: texto? = nulo) -> [texto]:
        // Retorna membros da familia disponiveis, opcionalmente com skill.
        fam = self.familias.get(familia_id)
        se nao fam entao:
            retorne []
        result = []
        para cada mid em fam.membros:
            p = self.skill_matcher.obter(mid)
            se p e p.disponibilidade_pct() > 0 entao:
                se skill e nulo ou p.nivel(skill) > 0 entao:
                    result.append(mid)
        retorne result

    funcao proximo_membro(self, familia_id: texto, skill: texto,
                       seja excluir: set? = nulo) -> texto?:
        // Escolhe o proximo membro da familia para o relay.
        excluir = excluir ou set()
        candidatos_ids = self.membros_disponiveis(familia_id, skill=skill)
        candidatos = [
            (mid, self.skill_matcher._score(self.skill_matcher.obter(mid), skill))
            para mid em candidatos_ids
            if mid nao in excluir
        ]
        candidatos.sort(key=(x) -> x[1], reverse=verdadeiro)
        candidatos ? retorne candidatos[0][0] : nulo

    funcao criar_relay_familiar(self, benchmark_id: texto, familia_id: texto,
                             seja nome: texto = "", descricao: texto = "",
                             seja workflow_tipo: TipoWorkflow = TipoWorkflow.GENERIC,
                             seja prioridade: Prioridade = Prioridade.P3,
                             seja max_pernas: inteiro = 5) -> TaskRelay:
        // Cria um TaskRelay onde a familia inteira reveza.
        fam = self.familias.get(familia_id)
        se nao fam entao:
            lance ValueError("Familia '{familia_id}' nao encontrada")
        relay = TaskRelay.criar(
            nome = nome  ou  "Relay Familia {fam.nome}",
            benchmark_id = benchmark_id,
            workflow_tipo = workflow_tipo,
            prioridade = prioridade,
            pessoas = list(fam.membros),
            descricao = descricao,
            max_pernas = max_pernas,
            familia_id = familia_id,
        )
        log.info(
            "Relay familiar criado: familia='%s', benchmark='%s'",
            fam.nome, benchmark_id,
        )
        retorne relay

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {fid: f.to_dict() para fid, f in self.familias.items()}


// ===========================================================================
// RelayMetrics
// ===========================================================================

classe RelayMetrics:
    // 
    Coleta e calcula metricas de todos os relays: tempo total, gargalos,
    quem e melhor em que, taxa de aprovacao, etc.
    // 

    funcao __init__(self) -> None:
        self.relays: {texto: TaskRelay} = {}
        // index por executor
        self._por_executor: Dict[texto, [texto]] = defaultdict(list)
        // index por benchmark
        self._por_benchmark: Dict[texto, [texto]] = defaultdict(list)

    funcao registrar_relay(self, relay: TaskRelay) -> None:
        self.relays[relay.id] = relay
        para cada leg em relay.pernas:
            self._por_executor[leg.executor].append(relay.id)
        self._por_benchmark[relay.benchmark_id].append(relay.id)

    // --- Metricas globais --------------------------------------------------

    funcao total_relays(self) -> inteiro:
        retorne tamanho(self.relays)

    funcao taxa_completude(self) -> flutuante:
        se nao self.relays entao:
            retorne 0.0
        completos = soma(1 para r em self.relays.values() if r.estado == EstadoRelay.COMPLETO)
        retorne completos / tamanho(self.relays)

    funcao tempo_medio(self) -> flutuante:
        tempos = [r.duracao_total_segundos para r em self.relays.values()
                  if r.duracao_total_segundos > 0]
        tempos ? retorne statistics.mean(tempos) : 0.0

    funcao total_pernas(self) -> inteiro:
        retorne soma(tamanho(r.pernas) para r em self.relays.values())

    funcao taxa_aprovacao_pernas(self) -> flutuante:
        total = self.total_pernas()
        se total == 0 entao:
            retorne 0.0
        aprovadas = soma(tamanho(r.pernas_completas()) para r em self.relays.values())
        retorne aprovadas / total

    // --- Metricas por executor --------------------------------------------

    funcao relays_por_executor(self, executor: texto) -> [TaskRelay]:
        ids = self._por_executor.get(executor, [])
        retorne [self.relays[i] para i em ids if i in self.relays]

    funcao pernas_por_executor(self, executor: texto) -> [RelayLeg]:
        result = []
        para cada relay em self.relays_por_executor(executor):
            para cada leg em relay.pernas:
                se leg.executor == executor entao:
                    result.append(leg)
        retorne result

    funcao desempenho_executor(self, executor: texto) -> {texto: qualquer}:
        // Retorna quem e melhor em que: metricas por executor.
        pernas = self.pernas_por_executor(executor)
        se nao pernas entao:
            retorne {"executor": executor, "total_pernas": 0}

        aprovadas = [l para l em pernas if l.estado == EstadoLeg.APROVADO]
        tempos = [l.duracao_segundos para l em pernas if l.duracao_segundos > 0]
        qualidades = [l.nota_qualidade para l em pernas if l.nota_qualidade > 0]

        // quem e melhor em que: agrupar por benchmark
        seja por_benchmark: Dict[texto, {texto: flutuante}] = defaultdict(() -> {"count": 0, "soma_q": 0.0})
        para cada l em pernas:
            relay = self.relays.get(l.relay_id)
            se relay entao:
                por_benchmark[relay.benchmark_id]["count"] += 1
                por_benchmark[relay.benchmark_id]["soma_q"] += l.nota_qualidade

        melhor_em = nulo
        melhor_media = 0.0
        para cada (bid, dados) em por_benchmark.items():
            se dados["count"] > 0 entao:
                media = dados["soma_q"] / dados["count"]
                se media > melhor_media entao:
                    melhor_media = media
                    melhor_em = bid

        retorne {
            "executor": executor,
            "total_pernas": tamanho(pernas),
            "pernas_aprovadas": tamanho(aprovadas),
            "taxa_aprovacao": arredonde(tamanho(aprovadas) / tamanho(pernas), 4),
            tempos ? "tempo_medio": arredonde(statistics.mean(tempos), 2) : 0.0,
            qualidades ? "qualidade_media": arredonde(statistics.mean(qualidades), 4) : 0.0,
            "melhor_em_benchmark": melhor_em,
            "melhor_em_media": arredonde(melhor_media, 4),
        }

    funcao ranking_executores(self) retorna List[{texto: qualquer}]:
        // Ranking de executores por qualidade media.
        executores = list(self._por_executor.keys())
        dados = [self.desempenho_executor(e) para e em executores]
        dados.sort(key=(x) -> x.get("qualidade_media", 0), reverse=verdadeiro)
        retorne dados

    // --- Metricas por benchmark -------------------------------------------

    funcao gargalos(self) retorna List[{texto: qualquer}]:
        // 
        Identifica gargalos: pernas que demoraram mais, foram puladas
        ou expiradas com mais frequencia.
        // 
        gargalos = []
        para cada relay em self.relays.values():
            para cada leg em relay.pernas:
                se leg.estado in (EstadoLeg.EXPIRADO, EstadoLeg.PULADO) entao:
                    gargalos.append({
                        "relay_id": relay.id,
                        "leg_id": leg.id,
                        "executor": leg.executor,
                        "estado": leg.estado.value,
                        "tentativas": leg.tentativas,
                        "duracao": leg.duracao_segundos,
                    })
                elif leg.duracao_segundos > 600: // mais de 10 minimo
                    gargalos.append({
                        "relay_id": relay.id,
                        "leg_id": leg.id,
                        "executor": leg.executor,
                        "estado": "lento",
                        "duracao": leg.duracao_segundos,
                    })
        retorne gargalos

    funcao resumo(self) -> {texto: qualquer}:
        retorne {
            "total_relays": self.total_relays(),
            "taxa_completude": arredonde(self.taxa_completude(), 4),
            "tempo_medio_relays": arredonde(self.tempo_medio(), 2),
            "total_pernas": self.total_pernas(),
            "taxa_aprovacao_pernas": arredonde(self.taxa_aprovacao_pernas(), 4),
            "total_gargalos": tamanho(self.gargalos()),
            "ranking_executores": self.ranking_executores()[:10],
        }

    funcao to_dict(self) -> {texto: qualquer}:
        retorne {
            "relays": {rid: r.to_dict() para rid, r in self.relays.items()},
            "resumo": self.resumo(),
        }


// ===========================================================================
// LaborRelayEngine (Motor Principal)
// ===========================================================================

// Tipo para funcao de execucao de perna: recebe (relay, leg, benchmark) -> (qualidade, tempo, resultado)
ExecutorPerna = Callable[[TaskRelay, RelayLeg, Benchmark], Tuple[flutuante, flutuante, {texto: qualquer}]]


classe LaborRelayEngine:
    // 
    Motor principal do OpenLaborRelay.

    Orquestra todo o sistema:
      - BenchmarkRegistry (parametros de qualidade)
      - SkillMatcher (escolhe proxima pessoa)
      - QualityGate (avalia contra benchmark)
      - WorkflowTemplateRegistry (templates por tipo)
      - FamilyRelayIntegration (relay familiar)
      - RelayMetrics (transparencia e metricas)

    O engine executa relays aplicando anti-bottleneck, continuous improvement
    e transparencia total.
    // 

    funcao __init__(self, quality_tolerancia: flutuante = 0.1) -> None:
        self.registry = BenchmarkRegistry()
        self.matcher = SkillMatcher()
        self.gate = QualityGate(tolerancia=quality_tolerancia)
        self.workflows = WorkflowTemplateRegistry()
        self.family = FamilyRelayIntegration(self.matcher)
        self.metrics = RelayMetrics()
        // funcao de execucao (injetavel para testes/simulacao)
        self._executor: ExecutorPerna? = nulo
        // armazenamento de relays em execucao
        self.relays: {texto: TaskRelay} = {}

    // --- Configuracao ------------------------------------------------------

    funcao set_executor(self, fn: ExecutorPerna) -> None:
        // Define funcao customizada para executar pernas (simulacao/producao).
        self._executor = fn

    funcao registrar_benchmark(self, nome: texto, **kwargs: qualquer) -> Benchmark:
        // Atalho para registrar benchmark no registry.
        retorne self.registry.registrar_rapido(nome=nome, **kwargs)

    funcao registrar_pessoa(self, pessoa_id: texto, nome: texto,
                         seja habilidades: Optional[{texto: flutuante}] = nulo,
                         seja disponivel: logico = verdadeiro,
                         seja carga_maxima: inteiro = 5,
                         seja familia_id: texto? = nulo) -> Pessoa:
        // Atalho para registrar pessoa no matcher.
        p = Pessoa(
            id = pessoa_id,
            nome = nome,
            habilidades = dict(habilidades ou {}),
            disponivel = disponivel,
            carga_maxima = carga_maxima,
            familia_id = familia_id,
        )
        self.matcher.registrar(p)
        retorne p

    funcao registrar_familia(self, familia_id: texto, nome: texto,
                          membros: [texto],
                          seja especialidade_coletiva: Optional[{texto: flutuante}] = nulo) -> Familia:
        // Atalho para registrar familia.
        fam = Familia(
            id = familia_id,
            nome = nome,
            membros = list(membros),
            especialidade_coletiva = dict(especialidade_coletiva ou {}),
        )
        retorne self.family.registrar_familia(fam)

    // --- Criacao de relays -------------------------------------------------

    funcao criar_relay(self, benchmark_nome_ou_id: texto,
                    seja pessoas: Optional[[texto]] = nulo,
                    seja nome: texto = "",
                    seja descricao: texto = "",
                    seja workflow_tipo: TipoWorkflow = TipoWorkflow.GENERIC,
                    seja prioridade: Prioridade = Prioridade.P3,
                    seja pessoa_inicial: texto? = nulo,
                    seja max_pernas: inteiro = 5,
                    seja familia_id: texto? = nulo) -> TaskRelay:
        // Cria um TaskRelay a partir de benchmark existente.
        // resolver benchmark
        bench = self.registry.obter(benchmark_nome_ou_id)
        se nao bench entao:
            bench = self.registry.obter_por_nome(benchmark_nome_ou_id)
        se nao bench entao:
            lance ValueError("Benchmark '{benchmark_nome_ou_id}' nao encontrado")

        relay = TaskRelay.criar(
            nome = nome  ou  "Relay para {bench.nome}",
            benchmark_id = bench.id,
            workflow_tipo = workflow_tipo,
            prioridade = prioridade,
            pessoas = pessoas,
            pessoa_inicial = pessoa_inicial,
            descricao = descricao,
            max_pernas = max_pernas,
            familia_id = familia_id,
        )
        self.relays[relay.id] = relay
        log.info("Relay criado: '%s' (benchmark=%s)", relay.nome, bench.nome)
        retorne relay

    funcao criar_relay_de_template(self, template_id: texto,
                                seja benchmark_nome_ou_id: texto = "",
                                seja nome: texto = "",
                                seja descricao: texto = "") -> TaskRelay:
        // Cria relay a partir de template de workflow.
        template = self.workflows.obter(template_id)
        se nao template entao:
            lance ValueError("Template '{template_id}' nao encontrado")
        // resolver benchmark
        bench = nulo
        se benchmark_nome_ou_id entao:
            bench = self.registry.obter(benchmark_nome_ou_id) ou self.registry.obter_por_nome(benchmark_nome_ou_id)
        se nao bench entao:
            bench = self.registry.benchmark_categoria(template.benchmark_categoria)
        se nao bench entao:
            lance ValueError(
                "Nenhum benchmark encontrado para categoria '{template.benchmark_categoria}'"
            )

        relay = TaskRelay.criar(
            nome = nome  ou  "Relay {template.nome}",
            benchmark_id = bench.id,
            workflow_tipo = template.tipo,
            prioridade = template.prioridade_padrao,
            descricao = descricao ou template.descricao,
            max_pernas = maximo(template.num_estagios(), 1),
        )
        relay.parar_ao_aprovar = template.parar_ao_aprovar
        self.relays[relay.id] = relay
        log.info(
            "Relay criado de template '%s' (benchmark=%s, %d estagios)",
            template.nome, bench.nome, template.num_estagios(),
        )
        retorne relay

    // --- Execucao de relay -------------------------------------------------

    funcao _executar_perna(self, relay: TaskRelay, leg: RelayLeg,
                        benchmark: Benchmark) -> Tuple[flutuante, flutuante, {texto: qualquer}]:
        // Executa uma perna: usa executor customizado ou simulacao.
        se self._executor entao:
            retorne self._executor(relay, leg, benchmark)
        // simulacao padrao
        retorne self._simular_perna(relay, leg, benchmark)

    funcao _simular_perna(self, relay: TaskRelay, leg: RelayLeg,
                       benchmark: Benchmark) -> Tuple[flutuante, flutuante, {texto: qualquer}]:
        // 
        Simulacao padrao: gera qualidade e tempo baseados na skill da pessoa
        contra o benchmark. Usado quando nenhum executor real e definido.
        // 
        pessoa = self.matcher.obter(leg.executor)
        skill = benchmark.categoria
        nivel = pessoa ? pessoa.nivel(skill) : 0.5

        // qualidade depende do nivel + ruido
        base_q = benchmark.qualidade_esperada * nivel
        ruido = random.uniform(-0.1, 0.15)
        qualidade = maximo(0.0, minimo(1.0, base_q + ruido))

        // tempo depende do nivel (mais habilidade = mais rapido)
        fator_tempo = nivel > 0 ? 2.0 - nivel : 2.0
        tempo = benchmark.tempo_segundos * fator_tempo * random.uniform(0.7, 1.3)
        se benchmark.tempo_segundos == 0 entao:
            tempo = random.uniform(30, 180)

        resultado = {
            "simulado": verdadeiro,
            "executor": leg.executor,
            "skill": skill,
            "nivel": arredonde(nivel, 3),
        }
        retorne arredonde(qualidade, 4), arredonde(tempo, 2), resultado

    funcao _encontrar_proxima_pessoa(self, relay: TaskRelay,
                                  benchmark: Benchmark,
                                  seja excluir: set? = nulo) -> texto?:
        // Encontra a proxima pessoa para o relay (skill matching).
        excluir = excluir ou set()
        // se relay familiar, usar integracao familiar
        se relay.familia_id entao:
            membro = self.family.proximo_membro(
                relay.familia_id, benchmark.categoria, excluir=excluir,
            )
            se membro entao:
                retorne membro

        // se ha lista explicita de pessoas, usar skill matcher sobre elas
        se relay.pessoas_disponiveis entao:
            para cada pid em relay.pessoas_disponiveis:
                se pid nao in excluir entao:
                    p = self.matcher.obter(pid)
                    se p e p.disponibilidade_pct() > 0 entao:
                        retorne pid
            retorne nulo

        // senao, buscar no matcher global
        pessoa = self.matcher.melhor(benchmark.categoria, excluir=excluir)
        pessoa ? retorne pessoa.id : nulo

    funcao _executar_perna_com_retry(self, relay: TaskRelay, leg: RelayLeg,
                                  benchmark: Benchmark) -> logico:
        // 
        Executa perna com anti-bottleneck: se travar ou reprovar,
        tenta ate max_tentativas_por_perna, depois passa para proxima.
        // 
        para cada tentativa em intervalo(relay.max_tentativas_por_perna):
            leg.iniciar()
            tente:
                desempacote qualidade, tempo, resultado = self._executar_perna(relay, leg, benchmark)
            capture Exception como e:
                log.error("[Leg %s] Erro na execucao: %s", leg.id, e)
                leg.comentario = "Erro: {e}"
                continue

            avaliacao = self.gate.avaliar_leg(benchmark, leg, qualidade, tempo, resultado)

            se avaliacao["aprovado"] entao:
                // atualizar carga da pessoa
                self._atualizar_carga(leg.executor, delta=-1)
                retorne verdadeiro
            senao:
                log.info(
                    "[Leg %s] Reprovada (tentativa %d/%d): %s",
                    leg.id, tentativa + 1, relay.max_tentativas_por_perna,
                    avaliacao["comentario"],
                )

        // esgotou tentativas: anti-bottleneck
        se relay.anti_bottleneck entao:
            leg.pular()
        senao:
            leg.expirar()
        self._atualizar_carga(leg.executor, delta=-1)
        retorne falso

    funcao _atualizar_carga(self, executor: texto, delta: inteiro) -> None:
        // Atualiza carga atual de uma pessoa.
        p = self.matcher.obter(executor)
        se p entao:
            p.carga_atual = maximo(0, p.carga_atual + delta)
            se delta > 0 entao:
                p.historico_relays += 1
                // qualidade sera somada externamente se necessario

    funcao executar_relay(self, relay: TaskRelay) -> {texto: qualquer}:
        // 
        Executa um TaskRelay completo: aplica relay, quality gate,
        anti-bottleneck, continuous improvement e registra metricas.
        // 
        benchmark = self.registry.obter(relay.benchmark_id)
        se nao benchmark entao:
            relay.falhar("Benchmark '{relay.benchmark_id}' nao encontrado")
            retorne relay.to_dict()

        relay.iniciar()
        seja ja_executaram: set = set()
        melhor_qualidade = 0.0
        melhor_tempo = flutuante("inf")
        seja leg_aprovada_final: RelayLeg? = nulo

        para cada perna_idx em intervalo(relay.max_pernas):
            // escolher proxima pessoa
            executor = self._encontrar_proxima_pessoa(relay, benchmark, excluir=ja_executaram)

            // se nao tem ninguem, tentar liberar ja_executaram para retry
            se nao executor e ja_executaram e relay.anti_bottleneck entao:
                log.info("[Relay %s] Sem novos candidatos; resetando exclusoes para retry", relay.id)
                ja_executaram.clear()
                executor = self._encontrar_proxima_pessoa(relay, benchmark, excluir=ja_executaram)

            se nao executor entao:
                relay.falhar("Sem pessoas disponiveis para o relay")
                self.metrics.registrar_relay(relay)
                retorne relay.to_dict()

            // criar e executar perna
            leg = relay.adicionar_perna(executor)
            self._atualizar_carga(executor, delta=+1)
            ja_executaram.add(executor)

            aprovado = self._executar_perna_com_retry(relay, leg, benchmark)

            // registrar qualidade no historico da pessoa
            p = self.matcher.obter(executor)
            se p entao:
                p.soma_qualidade += leg.nota_qualidade

            // acompanhar melhor resultado
            se leg.nota_qualidade > melhor_qualidade entao:
                melhor_qualidade = leg.nota_qualidade
                melhor_tempo = leg.duracao_segundos
                leg_aprovada_final = leg

            se aprovado e relay.parar_ao_aprovar entao:
                // continuous improvement: se superou benchmark, atualizar
                se melhor_qualidade > benchmark.qualidade_esperada entao:
                    self.registry.melhorar(relay.benchmark_id, melhor_qualidade, melhor_tempo)
                relay.completar({
                    "leg_aprovada": leg.to_dict(),
                    "qualidade_final": melhor_qualidade,
                    "executor_final": executor,
                    "benchmark_nome": benchmark.nome,
                })
                self.metrics.registrar_relay(relay)
                retorne relay.to_dict()

            // se nao parar_ao_aprovar, continua ate max_pernas

        // apos max_pernas: verificar se pelo menos uma perna foi aprovada
        aprovadas = relay.pernas_completas()
        se aprovadas entao:
            // continuous improvement
            se melhor_qualidade > benchmark.qualidade_esperada entao:
                self.registry.melhorar(relay.benchmark_id, melhor_qualidade, melhor_tempo)
            relay.completar({
                "pernas_aprovadas": tamanho(aprovadas),
                "qualidade_final": melhor_qualidade,
                leg_aprovada_final ? "executor_melhor": leg_aprovada_final.executor : nulo,
                "benchmark_nome": benchmark.nome,
            })
        senao:
            relay.falhar("Todas as {relay.max_pernas} pernas foram reprovadas/puladas")

        self.metrics.registrar_relay(relay)
        retorne relay.to_dict()

    // --- Consultas ---------------------------------------------------------

    funcao obter_relay(self, relay_id: texto) retorna TaskRelay?:
        retorne self.relays.get(relay_id)

    funcao listar_relays(self, estado: EstadoRelay? = None) -> [TaskRelay]:
        relays = list(self.relays.values())
        se estado entao:
            relays = [r para r em relays if r.estado == estado]
        retorne relays

    funcao relatorios(self) -> {texto: qualquer}:
        // Relatorio completo do estado do engine (transparencia).
        retorne {
            "benchmarks": self.registry.resumo(),
            "pessoas": self.matcher.to_dict(),
            "workflows": self.workflows.to_dict(),
            "familias": self.family.to_dict(),
            "metrics": self.metrics.resumo(),
            "relays_ativos": tamanho(self.listar_relays(EstadoRelay.EM_ANDAMENTO)),
            "relays_completos": tamanho(self.listar_relays(EstadoRelay.COMPLETO)),
        }

    funcao exportar_json(self, caminho: texto? = None) -> texto:
        // Exporta estado completo do engine como JSON.
        dados = self.relatorios()
        dados["relays"] = {rid: r.to_dict() para rid, r in self.relays.items()}
        texto = json.dumps(dados, indent=2, default=texto, ensure_ascii=falso)
        se caminho entao:
            Path(caminho).write_text(texto, encoding="utf-8")
            log.info("Estado exportado para %s", caminho)
        retorne texto


// ===========================================================================
// Demo / Teste
// ===========================================================================

funcao _demo() -> None:
    // Demonstracao do OpenLaborRelay em acao.
    imprima("=" * 70)
    imprima("OpenLaborRelay - Demonstracao")
    imprima("=" * 70)

    random.seed(42)
    engine = LaborRelayEngine(quality_tolerancia=0.15)

    // 1. Registrar benchmarks (sistemas que ja fazem excelente trabalho)
    imprima("\n[1] Registrando benchmarks...")
    engine.registrar_benchmark(
        "Build Python Rapido", autor="make-legacy",
        qualidade_esperada = 0.85, tempo_segundos=90,
        throughput_por_hora = 40, categoria="build",
        descricao = "Sistema de build Python legado, excelente trabalho.",
    )
    engine.registrar_benchmark(
        "Review Seguranca Profundo", autor="sonarqube-old",
        qualidade_esperada = 0.90, tempo_segundos=120,
        throughput_por_hora = 20, categoria="review",
    )
    engine.registrar_benchmark(
        "Test Suite Completa", autor="pytest-ci",
        qualidade_esperada = 0.88, tempo_segundos=180,
        throughput_por_hora = 15, categoria="test",
    )
    engine.registrar_benchmark(
        "Deploy Blue-Green", autor="ansible-deploy",
        qualidade_esperada = 0.92, tempo_segundos=240,
        throughput_por_hora = 10, categoria="deploy",
    )

    // 2. Registrar pessoas com habilidades
    imprima("\n[2] Registrando pessoas...")
    engine.registrar_pessoa("ana", "Ana", habilidades={"build": 0.9, "test": 0.7}, carga_maxima=3)
    engine.registrar_pessoa("bruno", "Bruno", habilidades={"build": 0.6, "review": 0.8}, carga_maxima=3)
    engine.registrar_pessoa("carla", "Carla", habilidades={"test": 0.95, "review": 0.7}, carga_maxima=4)
    engine.registrar_pessoa("diego", "Diego", habilidades={"deploy": 0.85, "build": 0.5}, carga_maxima=2)
    engine.registrar_pessoa("elena", "Elena", habilidades={"deploy": 0.7, "review": 0.6}, carga_maxima=3)

    // 3. Registrar familia
    imprima("\n[3] Registrando familia (OpenFamilyLabor)...")
    engine.registrar_familia("fam-lima", "Familia Lima",
                             membros = ["ana", "bruno", "carla"],
                             especialidade_coletiva = {"build": 0.8, "test": 0.85})

    // 4. Executar relays
    imprima("\n[4] Executando relays...")
    bench_build = engine.registry.obter_por_nome("Build Python Rapido")
    bench_review = engine.registry.obter_por_nome("Review Seguranca Profundo")
    bench_test = engine.registry.obter_por_nome("Test Suite Completa")
    bench_deploy = engine.registry.obter_por_nome("Deploy Blue-Green")

    // Relay 1: build simples (parar ao aprovar)
    relay1 = engine.criar_relay(
        bench_build.id, nome="Build do Modulo X",
        pessoas = ["ana", "bruno", "diego"],
        workflow_tipo = TipoWorkflow.BUILD,
        prioridade = Prioridade.P2,
    )
    relay1.parar_ao_aprovar = verdadeiro
    imprima("\n  -> Executando relay: {relay1.nome}")
    resultado1 = engine.executar_relay(relay1)
    imprima("     Estado: {resultado1['estado']}")
    imprima("     Duracao: {resultado1['duracao_total_segundos']}s")
    imprima("     Pernas: {len(resultado1['pernas'])}")

    // Relay 2: review
    relay2 = engine.criar_relay(
        bench_review.id, nome="Review PR #42",
        pessoas = ["bruno", "carla", "elena"],
        workflow_tipo = TipoWorkflow.REVIEW,
    )
    relay2.parar_ao_aprovar = verdadeiro
    imprima("\n  -> Executando relay: {relay2.nome}")
    resultado2 = engine.executar_relay(relay2)
    imprima("     Estado: {resultado2['estado']}")

    // Relay 3: relay familiar (familia Lima reveza no test)
    relay3 = engine.family.criar_relay_familiar(
        benchmark_id = bench_test.id, familia_id="fam-lima",
        nome = "Test Suite pela Familia Lima",
        workflow_tipo = TipoWorkflow.TEST,
    )
    relay3.parar_ao_aprovar = verdadeiro
    imprima("\n  -> Executando relay familiar: {relay3.nome}")
    engine.relays[relay3.id] = relay3
    resultado3 = engine.executar_relay(relay3)
    imprima("     Estado: {resultado3['estado']}")

    // Relay 4: deploy via template
    imprima("\n  -> Criando relay de template de deploy...")
    relay4 = engine.criar_relay_de_template(
        engine.workflows.obter_por_tipo(TipoWorkflow.DEPLOY).id,
        nome = "Deploy Producao v2.0",
    )
    relay4.pessoas_disponiveis = ["diego", "elena"]
    imprima("     Executando: {relay4.nome}")
    resultado4 = engine.executar_relay(relay4)
    imprima("     Estado: {resultado4['estado']}")

    // 5. Relatorio final (transparencia)
    imprima("\n" + "=" * 70)
    imprima("[5] RELATORIO DE METRICAS (Transparencia)")
    imprima("=" * 70)
    resumo = engine.metrics.resumo()
    imprima("  Total de relays:        {resumo['total_relays']}")
    imprima("  Taxa de completude:     {resumo['taxa_completude']:.1%}")
    imprima("  Tempo medio:            {resumo['tempo_medio_relays']:.1f}s")
    imprima("  Total de pernas:        {resumo['total_pernas']}")
    imprima("  Taxa aprovacao pernas:  {resumo['taxa_aprovacao_pernas']:.1%}")
    imprima("  Gargalos identificados: {resumo['total_gargalos']}")

    imprima("\n  Ranking de executores (quem e melhor em que):")
    para cada (i, exec_data) em enumere(resumo["ranking_executores"][:5], 1):
        imprima("    {i}. {exec_data['executor']}: "
              "qualidade={exec_data.get('qualidade_media', 0):.3f}, "
              "aprovacao={exec_data.get('taxa_aprovacao', 0):.1%}, "
              "melhor_em={exec_data.get('melhor_em_benchmark', '-')}")

    // 6. Evolucao dos benchmarks (continuous improvement)
    imprima("\n" + "=" * 70)
    imprima("[6] EVOLUCAO DOS BENCHMARKS (Continuous Improvement)")
    imprima("=" * 70)
    para cada bench em engine.registry.listar():
        imprima("  {bench.nome}:")
        imprima("    Qualidade atual: {bench.qualidade_esperada:.4f} "
              "(historico: {len(bench.historico_qualidade)} pontos)")
        imprima("    Tempo atual:     {bench.tempo_segundos:.1f}s")

    imprima("\n" + "=" * 70)
    imprima("OpenLaborRelay - Demonstracao concluida.")
    imprima("=" * 70)


// ===========================================================================
// Entry point
// ===========================================================================

se __name__ == "__main__" entao:
    _demo()

```
