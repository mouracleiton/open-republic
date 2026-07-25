// OpenLaborRelay -- gerado de Portugol++
package openlaborrelay

import "fmt"

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
type EstadoRelay int
const (
    // Estados possiveis de um TaskRelay.
    CRIADO = "criado"
    EM_ANDAMENTO = "em_andamento"
    PAUSADO = "pausado"
    COMPLETO = "completo"
    FALHOU = "falhou"
    CANCELADO = "cancelado"
type EstadoLeg int
const (
    // Estados possiveis de uma perna (leg) do relay.
    AGUARDANDO = "aguardando"
    EM_EXECUCAO = "em_execucao"
    APROVADO = "aprovado"
    REPROVADO = "reprovado"
    PULADO = "pulado"  // anti-bottleneck
    EXPIRADO = "expirado"
type TipoWorkflow int
const (
    // Tipos de workflow padrao suportados.
    BUILD = "build"
    REVIEW = "review"
    TEST = "test"
    DEPLOY = "deploy"
    GENERIC = "generic"
type Prioridade int
const (
    // Niveis de prioridade de uma tarefa.
    P1 = 1 // critico
    P2 = 2 // alto
    P3 = 3 // normal
    P4 = 4 // baixo
// ===========================================================================
// Benchmark
// ===========================================================================
// decorador: @dataclass
type Benchmark struct {
    //
    Representa um sistema/servico que ja faz EXCELENTE trabalho.
    Vira PARAMETRO de comparacao para novos sistemas. O benchmark guarda
    metricas de qualidade, tempo && throughput. Evolui com continuous
    improvement -- cada relay bem sucedido pode melhorar os valores.
    //
    id: texto
    nome: texto
    descricao := "" // string
    autor := ""  // sistema/servico que originalmente entregou excelencia // string
    qualidade_esperada := 0.0 // 0.0 a 1.0 // float64
    tempo_segundos := 0.0 // tempo de referencia // float64
    throughput_por_hora := 0.0 // itens por hora // float64
    custo_referencia := 0.0 // custo de referencia (opcional) // float64
    categoria := "generic" // string
    metadados := field(default_factory=dict) // {texto: qualquer}
    // historico de evolucao (continuous improvement)
    historico_qualidade := field(default_factory=list) // [flutuante]
    historico_tempo := field(default_factory=list) // [flutuante]
    criado_em := field(default_factory=time.time) // float64
    atualizado_em := field(default_factory=time.time) // float64
    func __post_init__(self) None {
        if ! self.historico_qualidade {
            self.historico_qualidade.append(self.qualidade_esperada)
        if ! self.historico_tempo {
            self.historico_tempo.append(self.tempo_segundos)
    // decorador: @classmethod
    funcao criar(cls, nome: texto, descricao: texto = "", autor: texto = "",
            qualidade_esperada := 0.0, tempo_segundos: flutuante = 0.0, // float64
            throughput_por_hora := 0.0, custo_referencia: flutuante = 0.0, // float64
            categoria := "generic", **metadados: qualquer) -> "Benchmark": // string
        // Cria um Benchmark com id gerado automaticamente.
        return cls(
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
    func melhorar(self, qualidade: flutuante, tempo: flutuante) None {
        //
        Continuous improvement: se um relay superar o benchmark,
        atualiza o benchmark para o novo melhor valor.
        //
        if qualidade > self.qualidade_esperada {
            self.qualidade_esperada = arredonde(qualidade, 4)
            log.info(
                "Benchmark '%s' melhorado: qualidade -> %.4f",
                self.nome, self.qualidade_esperada,
            )
        if tempo > 0 && (self.tempo_segundos == 0 || tempo < self.tempo_segundos) {
            self.tempo_segundos = arredonde(tempo, 2)
            log.info(
                "Benchmark '%s' melhorado: tempo -> %.2fs",
                self.nome, self.tempo_segundos,
            )
        self.historico_qualidade.append(self.qualidade_esperada)
        self.historico_tempo.append(self.tempo_segundos)
        self.atualizado_em = time.time()
    func comparar(self, qualidade: flutuante, tempo: flutuante) {texto: qualquer} {
        // Compara um resultado contra o benchmark.
        delta_q = qualidade - self.qualidade_esperada
        delta_t = self.tempo_segundos ? tempo - self.tempo_segundos : 0.0
        return {
            "benchmark": self.nome,
            "qualidade_resultado": arredonde(qualidade, 4),
            "qualidade_referencia": self.qualidade_esperada,
            "delta_qualidade": arredonde(delta_q, 4),
            "tempo_resultado": arredonde(tempo, 2),
            "tempo_referencia": arredonde(self.tempo_segundos, 2),
            "delta_tempo": arredonde(delta_t, 2),
            "supera_benchmark": delta_q >= 0,
        }
    func resumo(self) {texto: qualquer} {
        // Retorna resumo legivel do benchmark.
        return {
            "id": self.id,
            "nome": self.nome,
            "autor": self.autor,
            "qualidade_esperada": self.qualidade_esperada,
            "tempo_segundos": self.tempo_segundos,
            "throughput_por_hora": self.throughput_por_hora,
            "categoria": self.categoria,
            "evolucoes": len(self.historico_qualidade),
        }
// ===========================================================================
// RelayLeg (Perna do Relay)
// ===========================================================================
// decorador: @dataclass
type RelayLeg struct {
    //
    Uma perna do relay: uma pessoa/sistema executa sua parte da tarefa.
    Guarda quem fez, quando comecou/terminou, quanto tempo demorou, resultado
    && decisao do quality gate.
    //
    id: texto
    relay_id: texto
    executor: texto // pessoa || sistema
    estado := EstadoLeg.AGUARDANDO // EstadoLeg
    iniciado_em := nil // flutuante?
    finalizado_em := nil // flutuante?
    duracao_segundos := 0.0 // float64
    resultado := field(default_factory=dict) // {texto: qualquer}
    nota_qualidade := 0.0 // float64
    aprovado := false // bool
    comentario := "" // string
    ordem := 0 // ordem no relay (0 = primeira perna) // int64
    // anti-bottleneck
    tentativas := 0 // int64
    timeout_segundos := 300.0 // 5 minimo default // float64
    // decorador: @classmethod
    funcao criar(cls, relay_id: texto, executor: texto, ordem: inteiro,
            timeout_segundos := 300.0) -> "RelayLeg": // float64
        return cls(
            id = "leg-{uuid.uuid4().hex[:8]}",
            relay_id = relay_id,
            executor = executor,
            ordem = ordem,
            timeout_segundos = timeout_segundos,
        )
    func iniciar(self) None {
        self.estado = EstadoLeg.EM_EXECUCAO
        self.iniciado_em = time.time()
        self.tentativas += 1
        log.info("[Leg %s] Iniciada por '%s' (ordem=%d)", self.id, self.executor, self.ordem)
    funcao finalizar(self, resultado: {texto: qualquer}, nota_qualidade: flutuante,
                aprovado: logico, comentario: texto = "") -> nil:
        self.finalizado_em = time.time()
        self.duracao_segundos = arredonde(self.finalizado_em - (self.iniciado_em || self.finalizado_em), 2)
        self.resultado = resultado
        self.nota_qualidade = arredonde(nota_qualidade, 4)
        self.aprovado = aprovado
        self.comentario = comentario
        aprovado ? self.estado = EstadoLeg.APROVADO : EstadoLeg.REPROVADO
        log.info(
            "[Leg %s] Finalizada por '%s': %s (qualidade=%.3f, tempo=%.1fs)",
            self.id, self.executor, self.estado.value, self.nota_qualidade, self.duracao_segundos,
        )
    func expirar(self) None {
        // Anti-bottleneck: marca a perna como expirada (timeout).
        self.estado = EstadoLeg.EXPIRADO
        log.warning(
            "[Leg %s] Expirada (timeout) para '%s' apos %d tentativa(s)",
            self.id, self.executor, self.tentativas,
        )
    func pular(self) None {
        // Anti-bottleneck: pula esta perna e passa para a proxima.
        self.estado = EstadoLeg.PULADO
        log.warning("[Leg %s] Pulada para '%s' (anti-bottleneck)", self.id, self.executor)
    func to_dict(self) {texto: qualquer} {
        return {
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
type QualityGate struct {
    //
    Portao de qualidade: compara o resultado de cada perna do relay contra
    o benchmark registrado. Decide se o resultado passa || se outra pessoa
    precisa assumir.
    //
    func __init__(self, tolerancia: flutuante = 0.1) None {
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
        if aprovado {
            comentario = "Qualidade {qualidade:.3f} >= limite {limite:.3f} (tol={self.tolerancia})"
        } else {
            comentario = "Qualidade {qualidade:.3f} < limite {limite:.3f} -- reprovado"
        return {
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
        return avaliacao
// ===========================================================================
// SkillMatcher
// ===========================================================================
// decorador: @dataclass
type Pessoa struct {
    // Representa uma pessoa/sistema participante do relay.
    id: texto
    nome: texto
    habilidades := field(default_factory=dict) // skill -> nivel 0-1 // {texto: flutuante}
    disponivel := true // bool
    carga_atual := 0 // numero de tarefas ativas // int64
    carga_maxima := 5 // int64
    familia_id := nil // texto?
    historico_relays := 0 // int64
    soma_qualidade := 0.0 // soma das qualidades (para media) // float64
    func nivel(self, skill: texto) float64 {
        return self.habilidades.get(skill, 0.0)
    func carga_pct(self) float64 {
        // Percentual de carga (0.0 a 1.0).
        if self.carga_maxima <= 0 {
            return 1.0
        return minimo(self.carga_atual / self.carga_maxima, 1.0)
    func disponibilidade_pct(self) float64 {
        // 1.0 = totalmente livre, 0.0 = sem espaco.
        if ! self.disponivel {
            return 0.0
        return maximo(0.0, 1.0 - self.carga_pct())
    func qualidade_media(self) float64 {
        if self.historico_relays == 0 {
            return 0.0
        return self.soma_qualidade / self.historico_relays
    func to_dict(self) {texto: qualquer} {
        return {
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
type SkillMatcher struct {
    //
    Escolhe a proxima pessoa no relay baseando-se em:
    - skill (habilidade na categoria do benchmark)
    - disponibilidade (esta livre?)
    - carga (tem espaco?)
    - qualidade historica
    //
    func __init__(self) None {
        self.pessoas: {texto: Pessoa} = {}
    func registrar(self, pessoa: Pessoa) None {
        self.pessoas[pessoa.id] = pessoa
        log.info("Pessoa registrada: '%s' (%s)", pessoa.nome, pessoa.id)
    funcao obter(self, pessoa_id: texto) retorna Pessoa?:
        return self.pessoas.get(pessoa_id)
    funcao _score(self, pessoa: Pessoa, skill: texto, skill_weight: flutuante = 0.5,
            dispo_weight := 0.3, hist_weight: flutuante = 0.2) -> flutuante: // float64
        // Score composto: skill + disponibilidade + qualidade historica.
        nivel = pessoa.nivel(skill)
        dispo = pessoa.disponibilidade_pct()
        hist = minimo(pessoa.qualidade_media(), 1.0)
        return (nivel * skill_weight) + (dispo * dispo_weight) + (hist * hist_weight)
    funcao proximo(self, skill: texto, excluir: set? = nulo,
                limite := 5) -> List[(Pessoa, flutuante)]: // int64
        //
        Retorna as melhores pessoas para a skill, ordenadas por score.
        Args:
            skill: habilidade necessaria (categoria do benchmark).
            excluir: ids de pessoas a excluir (ja fizeram parte do relay).
            limite: maximo de pessoas a retornar.
        //
        excluir = excluir || set()
        candidatos = [
            (p, self._score(p, skill))
            para p em self.pessoas.values() {
            if p.id ! in excluir && p.disponibilidade_pct() > 0
        ]
        candidatos.sort(key=(x) -> x[1], reverse=true)
        return candidatos[:limite]
    funcao melhor(self, skill: texto, excluir: set? = None) retorna Pessoa?:
        // Retorna a melhor pessoa para a skill.
        result = self.proximo(skill, excluir=excluir, limite=1)
        result ? retorne result[0][0] : nil
    func listar_disponiveis(self, skill: texto? = None) [Pessoa] {
        // Lista pessoas disponiveis, opcionalmente filtrando por skill > 0.
        result = []
        for _, p := range self.pessoas.values() {
            if p.disponibilidade_pct() <= 0 {
                continue
            if skill && p.nivel(skill) <= 0 {
                continue
            result.append(p)
        return result
    func to_dict(self) {texto: qualquer} {
        return {pid: p.to_dict() para pid, p in self.pessoas.items()}
// ===========================================================================
// TaskRelay
// ===========================================================================
// decorador: @dataclass
type TaskRelay struct {
    //
    Representa uma tarefa distribuida como relay (revezamento).
    A tarefa comeca com a pessoa A, passa para B, C, etc. Cada perna (leg)
    && avaliada contra o benchmark. O relay termina quando todas as pernas
    necessarias sao completadas || quando uma perna && aprovada como
    suficiente (modo single-leg).
    //
    id: texto
    nome: texto
    benchmark_id: texto
    workflow_tipo := TipoWorkflow.GENERIC // TipoWorkflow
    prioridade := Prioridade.P3 // Prioridade
    estado := EstadoRelay.CRIADO // EstadoRelay
    descricao := "" // string
    pernas := field(default_factory=list) // [RelayLeg]
    pessoa_inicial := nil // texto?
    pessoas_disponiveis := field(default_factory=list) // [texto]
    // configuracao
    max_pernas := 5 // limite de revezamento // int64
    min_pernas := 1 // minimo para considerar completo // int64
    parar_ao_aprovar := true // para se uma perna para aprovada // bool
    timeout_por_perna := 300.0 // segundos // float64
    anti_bottleneck := true // pula automaticamente se travar // bool
    max_tentativas_por_perna := 2 // int64
    // familia
    familia_id := nil // se relay familiar // texto?
    // metricas
    criado_em := field(default_factory=time.time) // float64
    iniciado_em := nil // flutuante?
    finalizado_em := nil // flutuante?
    duracao_total_segundos := 0.0 // float64
    // resultado final
    resultado_final := field(default_factory=dict) // {texto: qualquer}
    metadados := field(default_factory=dict) // {texto: qualquer}
    // decorador: @classmethod
    funcao criar(cls, nome: texto, benchmark_id: texto,
            workflow_tipo := TipoWorkflow.GENERIC, // TipoWorkflow
            prioridade := Prioridade.P3, // Prioridade
            pessoas := nil, // Optional[[texto]]
            pessoa_inicial := nil, // texto?
            descricao := "", // string
            max_pernas := 5, // int64
            familia_id := nil, // texto?
            **metadados: qualquer) -> "TaskRelay":
        return cls(
            id = "relay-{uuid.uuid4().hex[:10]}",
            nome = nome,
            benchmark_id = benchmark_id,
            workflow_tipo = workflow_tipo,
            prioridade = prioridade,
            descricao = descricao,
            pessoas_disponiveis = list(pessoas || []),
            pessoa_inicial = pessoa_inicial,
            max_pernas = max_pernas,
            familia_id = familia_id,
            metadados = dict(metadados),
        )
    funcao perna_atual(self) retorna RelayLeg?:
        // Retorna a perna em execucao ou aguardando.
        for _, leg := range self.pernas {
            if leg.estado in (EstadoLeg.AGUARDANDO, EstadoLeg.EM_EXECUCAO) {
                return leg
        return nil
    func pernas_completas(self) [RelayLeg] {
        return [l para l em self.pernas if l.estado == EstadoLeg.APROVADO]
    func pernas_reprovadas(self) [RelayLeg] {
        return [l para l em self.pernas if l.estado == EstadoLeg.REPROVADO]
    func pernas_puladas(self) [RelayLeg] {
        return [l para l em self.pernas if l.estado in (EstadoLeg.PULADO, EstadoLeg.EXPIRADO)]
    funcao ultima_aprovada(self) retorna RelayLeg?:
        aprovadas = self.pernas_completas()
        aprovadas ? retorne aprovadas[-1] : nil
    func executada_por(self) [texto] {
        // Lista de pessoas que executaram pernas (transparencia).
        return [l.executor para l em self.pernas if l.estado in (
            EstadoLeg.APROVADO, EstadoLeg.REPROVADO
        )]
    func adicionar_perna(self, executor: texto) RelayLeg {
        // Adiciona uma nova perna ao relay.
        ordem = len(self.pernas)
        leg = RelayLeg.criar(
            relay_id = self.id,
            executor = executor,
            ordem = ordem,
            timeout_segundos = self.timeout_por_perna,
        )
        self.pernas.append(leg)
        return leg
    func iniciar(self) None {
        self.estado = EstadoRelay.EM_ANDAMENTO
        self.iniciado_em = time.time()
    func completar(self, resultado: {texto: qualquer}) None {
        self.estado = EstadoRelay.COMPLETO
        self.finalizado_em = time.time()
        self.duracao_total_segundos = arredonde(
            self.finalizado_em - (self.iniciado_em || self.finalizado_em), 2
        )
        self.resultado_final = resultado
        log.info(
            "[Relay %s] COMPLETO em %.1fs (%d pernas, %d aprovadas)",
            self.id, self.duracao_total_segundos,
            len(self.pernas), len(self.pernas_completas()),
        )
    func falhar(self, motivo: texto) None {
        self.estado = EstadoRelay.FALHOU
        self.finalizado_em = time.time()
        self.resultado_final = {"motivo": motivo}
        log.error("[Relay %s] FALHOU: %s", self.id, motivo)
    func cancelar(self, motivo: texto = "cancelado pelo usuario") None {
        self.estado = EstadoRelay.CANCELADO
        self.finalizado_em = time.time()
        self.resultado_final = {"motivo": motivo}
        log.info("[Relay %s] CANCELADO: %s", self.id, motivo)
    func to_dict(self) {texto: qualquer} {
        return {
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
type BenchmarkRegistry struct {
    //
    Registro central de benchmarks.
    Cada servico/sistema que ja faz EXCELENTE trabalho && registrado aqui
    como parametro de qualidade. Novos sistemas && novos relays sao medidos
    contra esses benchmarks.
    //
    func __init__(self) None {
        self.benchmarks: {texto: Benchmark} = {}
        self._por_categoria: Dict[texto, [texto]] = defaultdict(list)
    func registrar(self, benchmark: Benchmark) Benchmark {
        // Registra um novo benchmark.
        self.benchmarks[benchmark.id] = benchmark
        if benchmark.id ! in self._por_categoria[benchmark.categoria] {
            self._por_categoria[benchmark.categoria].append(benchmark.id)
        log.info(
            "Benchmark registrado: '%s' (cat=%s, qualidade=%.3f)",
            benchmark.nome, benchmark.categoria, benchmark.qualidade_esperada,
        )
        return benchmark
    funcao registrar_rapido(self, nome: texto, descricao: texto = "", autor: texto = "",
                        qualidade_esperada := 0.0, tempo_segundos: flutuante = 0.0, // float64
                        throughput_por_hora := 0.0, custo_referencia: flutuante = 0.0, // float64
                        categoria := "generic", **metadados: qualquer) -> Benchmark: // string
        // Cria e registra um benchmark em um passo.
        bench = Benchmark.criar(
            nome = nome, descricao=descricao, autor=autor,
            qualidade_esperada = qualidade_esperada,
            tempo_segundos = tempo_segundos,
            throughput_por_hora = throughput_por_hora,
            custo_referencia = custo_referencia,
            categoria = categoria, **metadados,
        )
        return self.registrar(bench)
    funcao obter(self, benchmark_id: texto) retorna Benchmark?:
        return self.benchmarks.get(benchmark_id)
    funcao obter_por_nome(self, nome: texto) retorna Benchmark?:
        for _, b := range self.benchmarks.values() {
            if b.nome == nome {
                return b
        return nil
    func listar(self, categoria: texto? = None) [Benchmark] {
        if categoria {
            ids = self._por_categoria.get(categoria, [])
            return [self.benchmarks[i] para i em ids if i in self.benchmarks]
        return list(self.benchmarks.values())
    func remover(self, benchmark_id: texto) bool {
        bench = self.benchmarks.pop(benchmark_id, nil)
        if bench {
            cat = bench.categoria
            if benchmark_id in self._por_categoria[cat] {
                self._por_categoria[cat].remove(benchmark_id)
            log.info("Benchmark removido: '%s'", bench.nome)
            return true
        return false
    func melhorar(self, benchmark_id: texto, qualidade: flutuante, tempo: flutuante) bool {
        // Continuous improvement: atualiza benchmark se superado.
        bench = self.obter(benchmark_id)
        if bench {
            bench.melhorar(qualidade, tempo)
            return true
        return false
    funcao benchmark_categoria(self, categoria: texto) retorna Benchmark?:
        // Retorna o melhor benchmark de uma categoria.
        benchmarks = self.listar(categoria)
        if ! benchmarks {
            return nil
        return maximo(benchmarks, key=(b) -> b.qualidade_esperada)
    func categorias(self) [texto] {
        return list(self._por_categoria.keys())
    func resumo(self) {texto: qualquer} {
        return {
            "total_benchmarks": len(self.benchmarks),
            "categorias": {cat: len(ids) para cat, ids in self._por_categoria.items()},
            "benchmarks": [b.resumo() para b em self.benchmarks.values()],
        }
    func to_dict(self) {texto: qualquer} {
        return {
            bid: {
                **b.resumo(),
                "descricao": b.descricao,
                "historico_qualidade": b.historico_qualidade,
                "historico_tempo": b.historico_tempo,
            }
            para bid, b in self.benchmarks.items() {
        }
// ===========================================================================
// WorkflowTemplate
// ===========================================================================
// decorador: @dataclass
type WorkflowTemplate struct {
    //
    Template de workflow: define o padrao de relay para um tipo de tarefa.
    Exemplo: workflow de BUILD pode ter 3 pernas (compilar, testar, empacotar),
    cada uma com skill necessaria && timeout diferente.
    //
    id: texto
    nome: texto
    tipo: TipoWorkflow
    descricao := "" // string
    // lista de estagios: cada estagio e (skill_necessaria, descricao, timeout)
    estagios := field(default_factory=list) // List[{texto: qualquer}]
    parar_ao_aprovar := false // templates geralmente precisam de todas as pernas // bool
    benchmark_categoria := "generic" // string
    prioridade_padrao := Prioridade.P3 // Prioridade
    metadados := field(default_factory=dict) // {texto: qualquer}
    // decorador: @classmethod
    funcao criar(cls, nome: texto, tipo: TipoWorkflow,
            estagios := nil, // Optional[List[{texto: qualquer}]]
            descricao := "", // string
            parar_ao_aprovar := false, // bool
            benchmark_categoria := "generic", // string
            prioridade_padrao := Prioridade.P3, // Prioridade
            **metadados: qualquer) -> "WorkflowTemplate":
        return cls(
            id = "wf-{uuid.uuid4().hex[:8]}",
            nome = nome,
            tipo = tipo,
            estagios = list(estagios || []),
            descricao = descricao,
            parar_ao_aprovar = parar_ao_aprovar,
            benchmark_categoria = benchmark_categoria,
            prioridade_padrao = prioridade_padrao,
            metadados = dict(metadados),
        )
    funcao adicionar_estagio(self, skill: texto, descricao: texto = "",
                        timeout := 300.0, // float64
                        obrigatorio := true) -> nil: // bool
        self.estagios.append({
            "skill": skill,
            "descricao": descricao,
            "timeout": timeout,
            "obrigatorio": obrigatorio,
        })
    func num_estagios(self) int64 {
        return len(self.estagios)
    func to_dict(self) {texto: qualquer} {
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo.value,
            "descricao": self.descricao,
            "estagios": list(self.estagios),
            "parar_ao_aprovar": self.parar_ao_aprovar,
            "benchmark_categoria": self.benchmark_categoria,
            "prioridade_padrao": self.prioridade_padrao.name,
        }
type WorkflowTemplateRegistry struct {
    // Registro de templates de workflow por tipo.
    func __init__(self) None {
        self.templates: {texto: WorkflowTemplate} = {}
        self._tipos: {TipoWorkflow: texto} = {}
        self._inicializar_padroes()
    func _inicializar_padroes(self) None {
        // Cria templates padrao para build, review, test, deploy.
        // BUILD
        build = WorkflowTemplate.criar(
            nome = "Build Padrao",
            tipo = TipoWorkflow.BUILD,
            benchmark_categoria = "build",
            parar_ao_aprovar = false,
        )
        build.adicionar_estagio("compilacao", "Compilar codigo", timeout=120)
        build.adicionar_estagio("lint", "Rodar linter && analise estatica", timeout=60)
        build.adicionar_estagio("empacotamento", "Empacotar artefato", timeout=90)
        self.registrar(build)
        // REVIEW
        review = WorkflowTemplate.criar(
            nome = "Code Review Padrao",
            tipo = TipoWorkflow.REVIEW,
            benchmark_categoria = "review",
            parar_ao_aprovar = false,
        )
        review.adicionar_estagio("revisao_seguranca", "Revisao de seguranca", timeout=180)
        review.adicionar_estagio("revisao_qualidade", "Revisao de qualidade", timeout=180)
        self.registrar(review)
        // TEST
        test = WorkflowTemplate.criar(
            nome = "Test Padrao",
            tipo = TipoWorkflow.TEST,
            benchmark_categoria = "test",
            parar_ao_aprovar = false,
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
            parar_ao_aprovar = false,
        )
        deploy.adicionar_estagio("pre_deploy", "Checagens pre-deploy", timeout=60)
        deploy.adicionar_estagio("deploy", "Executar deploy", timeout=180)
        deploy.adicionar_estagio("post_deploy", "Validacao post-deploy", timeout=120)
        self.registrar(deploy)
    func registrar(self, template: WorkflowTemplate) WorkflowTemplate {
        self.templates[template.id] = template
        self._tipos[template.tipo] = template.id
        log.info("Template registrado: '%s' (%s)", template.nome, template.tipo.value)
        return template
    funcao obter(self, template_id: texto) retorna WorkflowTemplate?:
        return self.templates.get(template_id)
    funcao obter_por_tipo(self, tipo: TipoWorkflow) retorna WorkflowTemplate?:
        tid = self._tipos.get(tipo)
        tid ? retorne self.templates.get(tid) : nil
    func listar(self) [WorkflowTemplate] {
        return list(self.templates.values())
    func to_dict(self) {texto: qualquer} {
        return {tid: t.to_dict() para tid, t in self.templates.items()}
// ===========================================================================
// FamilyRelayIntegration (OpenFamilyLabor)
// ===========================================================================
// decorador: @dataclass
type Familia struct {
    // Representa uma familia no OpenFamilyLabor.
    id: texto
    nome: texto
    membros := field(default_factory=list) // ids de pessoas // [texto]
    especialidade_coletiva := field(default_factory=dict) // {texto: flutuante}
    disponivel := true // bool
    funcao melhor_skill(self) retorna texto?:
        if ! self.especialidade_coletiva {
            return nil
        return maximo(self.especialidade_coletiva, key=self.especialidade_coletiva.get)
    func to_dict(self) {texto: qualquer} {
        return {
            "id": self.id,
            "nome": self.nome,
            "membros": list(self.membros),
            "especialidade_coletiva": dict(self.especialidade_coletiva),
            "disponivel": self.disponivel,
        }
type FamilyRelayIntegration struct {
    //
    Integracao com OpenFamilyLabor.
    Permite que uma familia inteira reveze numa tarefa. O relay pode
    passar de membro em membro da familia, respeitando especialidades.
    //
    func __init__(self, skill_matcher: SkillMatcher) None {
        self.skill_matcher = skill_matcher
        self.familias: {texto: Familia} = {}
    func registrar_familia(self, familia: Familia) Familia {
        self.familias[familia.id] = familia
        log.info("Familia registrada: '%s' (%d membros)", familia.nome, len(familia.membros))
        return familia
    funcao obter_familia(self, familia_id: texto) retorna Familia?:
        return self.familias.get(familia_id)
    funcao membros_disponiveis(self, familia_id: texto,
                            skill := nil) -> [texto]: // texto?
        // Retorna membros da familia disponiveis, opcionalmente com skill.
        fam = self.familias.get(familia_id)
        if ! fam {
            return []
        result = []
        for _, mid := range fam.membros {
            p = self.skill_matcher.obter(mid)
            if p && p.disponibilidade_pct() > 0 {
                if skill && nil || p.nivel(skill) > 0 {
                    result.append(mid)
        return result
    funcao proximo_membro(self, familia_id: texto, skill: texto,
                    excluir := nil) -> texto?: // set?
        // Escolhe o proximo membro da familia para o relay.
        excluir = excluir || set()
        candidatos_ids = self.membros_disponiveis(familia_id, skill=skill)
        candidatos = [
            (mid, self.skill_matcher._score(self.skill_matcher.obter(mid), skill))
            para mid em candidatos_ids {
            if mid ! in excluir
        ]
        candidatos.sort(key=(x) -> x[1], reverse=true)
        candidatos ? retorne candidatos[0][0] : nil
    funcao criar_relay_familiar(self, benchmark_id: texto, familia_id: texto,
                            nome := "", descricao: texto = "", // string
                            workflow_tipo := TipoWorkflow.GENERIC, // TipoWorkflow
                            prioridade := Prioridade.P3, // Prioridade
                            max_pernas := 5) -> TaskRelay: // int64
        // Cria um TaskRelay onde a familia inteira reveza.
        fam = self.familias.get(familia_id)
        if ! fam {
            lance ValueError("Familia '{familia_id}' ! encontrada")
        relay = TaskRelay.criar(
            nome = nome  ||  "Relay Familia {fam.nome}",
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
        return relay
    func to_dict(self) {texto: qualquer} {
        return {fid: f.to_dict() para fid, f in self.familias.items()}
// ===========================================================================
// RelayMetrics
// ===========================================================================
type RelayMetrics struct {
    //
    Coleta && calcula metricas de todos os relays: tempo total, gargalos,
    quem && melhor em que, taxa de aprovacao, etc.
    //
    func __init__(self) None {
        self.relays: {texto: TaskRelay} = {}
        // index por executor
        self._por_executor: Dict[texto, [texto]] = defaultdict(list)
        // index por benchmark
        self._por_benchmark: Dict[texto, [texto]] = defaultdict(list)
    func registrar_relay(self, relay: TaskRelay) None {
        self.relays[relay.id] = relay
        for _, leg := range relay.pernas {
            self._por_executor[leg.executor].append(relay.id)
        self._por_benchmark[relay.benchmark_id].append(relay.id)
    // --- Metricas globais --------------------------------------------------
    func total_relays(self) int64 {
        return len(self.relays)
    func taxa_completude(self) float64 {
        if ! self.relays {
            return 0.0
        completos = soma(1 para r em self.relays.values() if r.estado == EstadoRelay.COMPLETO)
        return completos / len(self.relays)
    func tempo_medio(self) float64 {
        tempos = [r.duracao_total_segundos para r em self.relays.values()
                if r.duracao_total_segundos > 0]
        tempos ? retorne statistics.mean(tempos) : 0.0
    func total_pernas(self) int64 {
        return soma(len(r.pernas) para r em self.relays.values())
    func taxa_aprovacao_pernas(self) float64 {
        total = self.total_pernas()
        if total == 0 {
            return 0.0
        aprovadas = soma(len(r.pernas_completas()) para r em self.relays.values())
        return aprovadas / total
    // --- Metricas por executor --------------------------------------------
    func relays_por_executor(self, executor: texto) [TaskRelay] {
        ids = self._por_executor.get(executor, [])
        return [self.relays[i] para i em ids if i in self.relays]
    func pernas_por_executor(self, executor: texto) [RelayLeg] {
        result = []
        for _, relay := range self.relays_por_executor(executor) {
            for _, leg := range relay.pernas {
                if leg.executor == executor {
                    result.append(leg)
        return result
    func desempenho_executor(self, executor: texto) {texto: qualquer} {
        // Retorna quem e melhor em que: metricas por executor.
        pernas = self.pernas_por_executor(executor)
        if ! pernas {
            return {"executor": executor, "total_pernas": 0}
        aprovadas = [l para l em pernas if l.estado == EstadoLeg.APROVADO]
        tempos = [l.duracao_segundos para l em pernas if l.duracao_segundos > 0]
        qualidades = [l.nota_qualidade para l em pernas if l.nota_qualidade > 0]
        // quem e melhor em que: agrupar por benchmark
        por_benchmark := defaultdict(() -> {"count": 0, "soma_q": 0.0}) // Dict[texto, {texto: flutuante}]
        for _, l := range pernas {
            relay = self.relays.get(l.relay_id)
            if relay {
                por_benchmark[relay.benchmark_id]["count"] += 1
                por_benchmark[relay.benchmark_id]["soma_q"] += l.nota_qualidade
        melhor_em = nil
        melhor_media = 0.0
        para cada (bid, dados) em por_benchmark.items(): {
            if dados["count"] > 0 {
                media = dados["soma_q"] / dados["count"]
                if media > melhor_media {
                    melhor_media = media
                    melhor_em = bid
        return {
            "executor": executor,
            "total_pernas": len(pernas),
            "pernas_aprovadas": len(aprovadas),
            "taxa_aprovacao": arredonde(len(aprovadas) / len(pernas), 4),
            tempos ? "tempo_medio": arredonde(statistics.mean(tempos), 2) : 0.0,
            qualidades ? "qualidade_media": arredonde(statistics.mean(qualidades), 4) : 0.0,
            "melhor_em_benchmark": melhor_em,
            "melhor_em_media": arredonde(melhor_media, 4),
        }
    funcao ranking_executores(self) retorna List[{texto: qualquer}]:
        // Ranking de executores por qualidade media.
        executores = list(self._por_executor.keys())
        dados = [self.desempenho_executor(&&) para && em executores]
        dados.sort(key=(x) -> x.get("qualidade_media", 0), reverse=true)
        return dados
    // --- Metricas por benchmark -------------------------------------------
    funcao gargalos(self) retorna List[{texto: qualquer}]:
        //
        Identifica gargalos: pernas que demoraram mais, foram puladas
        || expiradas com mais frequencia.
        //
        gargalos = []
        for _, relay := range self.relays.values() {
            for _, leg := range relay.pernas {
                if leg.estado in (EstadoLeg.EXPIRADO, EstadoLeg.PULADO) {
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
        return gargalos
    func resumo(self) {texto: qualquer} {
        return {
            "total_relays": self.total_relays(),
            "taxa_completude": arredonde(self.taxa_completude(), 4),
            "tempo_medio_relays": arredonde(self.tempo_medio(), 2),
            "total_pernas": self.total_pernas(),
            "taxa_aprovacao_pernas": arredonde(self.taxa_aprovacao_pernas(), 4),
            "total_gargalos": len(self.gargalos()),
            "ranking_executores": self.ranking_executores()[:10],
        }
    func to_dict(self) {texto: qualquer} {
        return {
            "relays": {rid: r.to_dict() para rid, r in self.relays.items()},
            "resumo": self.resumo(),
        }
// ===========================================================================
// LaborRelayEngine (Motor Principal)
// ===========================================================================
// Tipo para funcao de execucao de perna: recebe (relay, leg, benchmark) -> (qualidade, tempo, resultado)
ExecutorPerna = Callable[[TaskRelay, RelayLeg, Benchmark], Tuple[flutuante, flutuante, {texto: qualquer}]]
type LaborRelayEngine struct {
    //
    Motor principal do OpenLaborRelay.
    Orquestra todo o sistema:
    - BenchmarkRegistry (parametros de qualidade)
    - SkillMatcher (escolhe proxima pessoa)
    - QualityGate (avalia contra benchmark)
    - WorkflowTemplateRegistry (templates por tipo)
    - FamilyRelayIntegration (relay familiar)
    - RelayMetrics (transparencia && metricas)
    O engine executa relays aplicando anti-bottleneck, continuous improvement
    && transparencia total.
    //
    func __init__(self, quality_tolerancia: flutuante = 0.1) None {
        self.registry = BenchmarkRegistry()
        self.matcher = SkillMatcher()
        self.gate = QualityGate(tolerancia=quality_tolerancia)
        self.workflows = WorkflowTemplateRegistry()
        self.family = FamilyRelayIntegration(self.matcher)
        self.metrics = RelayMetrics()
        // funcao de execucao (injetavel para testes/simulacao)
        self._executor: ExecutorPerna? = nil
        // armazenamento de relays em execucao
        self.relays: {texto: TaskRelay} = {}
    // --- Configuracao ------------------------------------------------------
    func set_executor(self, fn: ExecutorPerna) None {
        // Define funcao customizada para executar pernas (simulacao/producao).
        self._executor = fn
    func registrar_benchmark(self, nome: texto, **kwargs: qualquer) Benchmark {
        // Atalho para registrar benchmark no registry.
        return self.registry.registrar_rapido(nome=nome, **kwargs)
    funcao registrar_pessoa(self, pessoa_id: texto, nome: texto,
                        habilidades := nil, // Optional[{texto: flutuante}]
                        disponivel := true, // bool
                        carga_maxima := 5, // int64
                        familia_id := nil) -> Pessoa: // texto?
        // Atalho para registrar pessoa no matcher.
        p = Pessoa(
            id = pessoa_id,
            nome = nome,
            habilidades = dict(habilidades || {}),
            disponivel = disponivel,
            carga_maxima = carga_maxima,
            familia_id = familia_id,
        )
        self.matcher.registrar(p)
        return p
    funcao registrar_familia(self, familia_id: texto, nome: texto,
                        membros: [texto],
                        especialidade_coletiva := nil) -> Familia: // Optional[{texto: flutuante}]
        // Atalho para registrar familia.
        fam = Familia(
            id = familia_id,
            nome = nome,
            membros = list(membros),
            especialidade_coletiva = dict(especialidade_coletiva || {}),
        )
        return self.family.registrar_familia(fam)
    // --- Criacao de relays -------------------------------------------------
    funcao criar_relay(self, benchmark_nome_ou_id: texto,
                    pessoas := nil, // Optional[[texto]]
                    nome := "", // string
                    descricao := "", // string
                    workflow_tipo := TipoWorkflow.GENERIC, // TipoWorkflow
                    prioridade := Prioridade.P3, // Prioridade
                    pessoa_inicial := nil, // texto?
                    max_pernas := 5, // int64
                    familia_id := nil) -> TaskRelay: // texto?
        // Cria um TaskRelay a partir de benchmark existente.
        // resolver benchmark
        bench = self.registry.obter(benchmark_nome_ou_id)
        if ! bench {
            bench = self.registry.obter_por_nome(benchmark_nome_ou_id)
        if ! bench {
            lance ValueError("Benchmark '{benchmark_nome_ou_id}' ! encontrado")
        relay = TaskRelay.criar(
            nome = nome  ||  "Relay para {bench.nome}",
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
        return relay
    funcao criar_relay_de_template(self, template_id: texto,
                                benchmark_nome_ou_id := "", // string
                                nome := "", // string
                                descricao := "") -> TaskRelay: // string
        // Cria relay a partir de template de workflow.
        template = self.workflows.obter(template_id)
        if ! template {
            lance ValueError("Template '{template_id}' ! encontrado")
        // resolver benchmark
        bench = nil
        if benchmark_nome_ou_id {
            bench = self.registry.obter(benchmark_nome_ou_id) || self.registry.obter_por_nome(benchmark_nome_ou_id)
        if ! bench {
            bench = self.registry.benchmark_categoria(template.benchmark_categoria)
        if ! bench {
            lance ValueError(
                "Nenhum benchmark encontrado para categoria '{template.benchmark_categoria}'"
            )
        relay = TaskRelay.criar(
            nome = nome  ||  "Relay {template.nome}",
            benchmark_id = bench.id,
            workflow_tipo = template.tipo,
            prioridade = template.prioridade_padrao,
            descricao = descricao || template.descricao,
            max_pernas = maximo(template.num_estagios(), 1),
        )
        relay.parar_ao_aprovar = template.parar_ao_aprovar
        self.relays[relay.id] = relay
        log.info(
            "Relay criado de template '%s' (benchmark=%s, %d estagios)",
            template.nome, bench.nome, template.num_estagios(),
        )
        return relay
    // --- Execucao de relay -------------------------------------------------
    funcao _executar_perna(self, relay: TaskRelay, leg: RelayLeg,
                        benchmark: Benchmark) -> Tuple[flutuante, flutuante, {texto: qualquer}]:
        // Executa uma perna: usa executor customizado ou simulacao.
        if self._executor {
            return self._executor(relay, leg, benchmark)
        // simulacao padrao
        return self._simular_perna(relay, leg, benchmark)
    funcao _simular_perna(self, relay: TaskRelay, leg: RelayLeg,
                    benchmark: Benchmark) -> Tuple[flutuante, flutuante, {texto: qualquer}]:
        //
        Simulacao padrao: gera qualidade && tempo baseados na skill da pessoa
        contra o benchmark. Usado quando nenhum executor real && definido.
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
        if benchmark.tempo_segundos == 0 {
            tempo = random.uniform(30, 180)
        resultado = {
            "simulado": true,
            "executor": leg.executor,
            "skill": skill,
            "nivel": arredonde(nivel, 3),
        }
        return arredonde(qualidade, 4), arredonde(tempo, 2), resultado
    funcao _encontrar_proxima_pessoa(self, relay: TaskRelay,
                                benchmark: Benchmark,
                                excluir := nil) -> texto?: // set?
        // Encontra a proxima pessoa para o relay (skill matching).
        excluir = excluir || set()
        // se relay familiar, usar integracao familiar
        if relay.familia_id {
            membro = self.family.proximo_membro(
                relay.familia_id, benchmark.categoria, excluir=excluir,
            )
            if membro {
                return membro
        // se ha lista explicita de pessoas, usar skill matcher sobre elas
        if relay.pessoas_disponiveis {
            for _, pid := range relay.pessoas_disponiveis {
                if pid ! in excluir {
                    p = self.matcher.obter(pid)
                    if p && p.disponibilidade_pct() > 0 {
                        return pid
            return nil
        // senao, buscar no matcher global
        pessoa = self.matcher.melhor(benchmark.categoria, excluir=excluir)
        pessoa ? retorne pessoa.id : nil
    funcao _executar_perna_com_retry(self, relay: TaskRelay, leg: RelayLeg,
                                benchmark: Benchmark) -> logico:
        //
        Executa perna com anti-bottleneck: se travar || reprovar,
        tenta ate max_tentativas_por_perna, depois passa para proxima.
        //
        for _, tentativa := range intervalo(relay.max_tentativas_por_perna) {
            leg.iniciar()
            tente:
                desempacote qualidade, tempo, resultado = self._executar_perna(relay, leg, benchmark)
            capture Exception como &&:
                log.error("[Leg %s] Erro na execucao: %s", leg.id, &&)
                leg.comentario = "Erro: {&&}"
                continue
            avaliacao = self.gate.avaliar_leg(benchmark, leg, qualidade, tempo, resultado)
            if avaliacao["aprovado"] {
                // atualizar carga da pessoa
                self._atualizar_carga(leg.executor, delta=-1)
                return true
            } else {
                log.info(
                    "[Leg %s] Reprovada (tentativa %d/%d): %s",
                    leg.id, tentativa + 1, relay.max_tentativas_por_perna,
                    avaliacao["comentario"],
                )
        // esgotou tentativas: anti-bottleneck
        if relay.anti_bottleneck {
            leg.pular()
        } else {
            leg.expirar()
        self._atualizar_carga(leg.executor, delta=-1)
        return false
    func _atualizar_carga(self, executor: texto, delta: inteiro) None {
        // Atualiza carga atual de uma pessoa.
        p = self.matcher.obter(executor)
        if p {
            p.carga_atual = maximo(0, p.carga_atual + delta)
            if delta > 0 {
                p.historico_relays += 1
                // qualidade sera somada externamente se necessario
    func executar_relay(self, relay: TaskRelay) {texto: qualquer} {
        //
        Executa um TaskRelay completo: aplica relay, quality gate,
        anti-bottleneck, continuous improvement && registra metricas.
        //
        benchmark = self.registry.obter(relay.benchmark_id)
        if ! benchmark {
            relay.falhar("Benchmark '{relay.benchmark_id}' ! encontrado")
            return relay.to_dict()
        relay.iniciar()
        ja_executaram := set() // set
        melhor_qualidade = 0.0
        melhor_tempo = flutuante("inf")
        leg_aprovada_final := nil // RelayLeg?
        for _, perna_idx := range intervalo(relay.max_pernas) {
            // escolher proxima pessoa
            executor = self._encontrar_proxima_pessoa(relay, benchmark, excluir=ja_executaram)
            // se nao tem ninguem, tentar liberar ja_executaram para retry
            if ! executor && ja_executaram && relay.anti_bottleneck {
                log.info("[Relay %s] Sem novos candidatos; resetando exclusoes para retry", relay.id)
                ja_executaram.clear()
                executor = self._encontrar_proxima_pessoa(relay, benchmark, excluir=ja_executaram)
            if ! executor {
                relay.falhar("Sem pessoas disponiveis para o relay")
                self.metrics.registrar_relay(relay)
                return relay.to_dict()
            // criar e executar perna
            leg = relay.adicionar_perna(executor)
            self._atualizar_carga(executor, delta=+1)
            ja_executaram.add(executor)
            aprovado = self._executar_perna_com_retry(relay, leg, benchmark)
            // registrar qualidade no historico da pessoa
            p = self.matcher.obter(executor)
            if p {
                p.soma_qualidade += leg.nota_qualidade
            // acompanhar melhor resultado
            if leg.nota_qualidade > melhor_qualidade {
                melhor_qualidade = leg.nota_qualidade
                melhor_tempo = leg.duracao_segundos
                leg_aprovada_final = leg
            if aprovado && relay.parar_ao_aprovar {
                // continuous improvement: se superou benchmark, atualizar
                if melhor_qualidade > benchmark.qualidade_esperada {
                    self.registry.melhorar(relay.benchmark_id, melhor_qualidade, melhor_tempo)
                relay.completar({
                    "leg_aprovada": leg.to_dict(),
                    "qualidade_final": melhor_qualidade,
                    "executor_final": executor,
                    "benchmark_nome": benchmark.nome,
                })
                self.metrics.registrar_relay(relay)
                return relay.to_dict()
            // se nao parar_ao_aprovar, continua ate max_pernas
        // apos max_pernas: verificar se pelo menos uma perna foi aprovada
        aprovadas = relay.pernas_completas()
        if aprovadas {
            // continuous improvement
            if melhor_qualidade > benchmark.qualidade_esperada {
                self.registry.melhorar(relay.benchmark_id, melhor_qualidade, melhor_tempo)
            relay.completar({
                "pernas_aprovadas": len(aprovadas),
                "qualidade_final": melhor_qualidade,
                leg_aprovada_final ? "executor_melhor": leg_aprovada_final.executor : nil,
                "benchmark_nome": benchmark.nome,
            })
        } else {
            relay.falhar("Todas as {relay.max_pernas} pernas foram reprovadas/puladas")
        self.metrics.registrar_relay(relay)
        return relay.to_dict()
    // --- Consultas ---------------------------------------------------------
    funcao obter_relay(self, relay_id: texto) retorna TaskRelay?:
        return self.relays.get(relay_id)
    func listar_relays(self, estado: EstadoRelay? = None) [TaskRelay] {
        relays = list(self.relays.values())
        if estado {
            relays = [r para r em relays if r.estado == estado]
        return relays
    func relatorios(self) {texto: qualquer} {
        // Relatorio completo do estado do engine (transparencia).
        return {
            "benchmarks": self.registry.resumo(),
            "pessoas": self.matcher.to_dict(),
            "workflows": self.workflows.to_dict(),
            "familias": self.family.to_dict(),
            "metrics": self.metrics.resumo(),
            "relays_ativos": len(self.listar_relays(EstadoRelay.EM_ANDAMENTO)),
            "relays_completos": len(self.listar_relays(EstadoRelay.COMPLETO)),
        }
    func exportar_json(self, caminho: texto? = None) string {
        // Exporta estado completo do engine como JSON.
        dados = self.relatorios()
        dados["relays"] = {rid: r.to_dict() para rid, r in self.relays.items()}
        texto = json.dumps(dados, indent=2, default=texto, ensure_ascii=false)
        if caminho {
            Path(caminho).write_text(texto, encoding="utf-8")
            log.info("Estado exportado para %s", caminho)
        return texto
// ===========================================================================
// Demo / Teste
// ===========================================================================
func _demo() None {
    // Demonstracao do OpenLaborRelay em acao.
    fmt.Println("=" * 70)
    fmt.Println("OpenLaborRelay - Demonstracao")
    fmt.Println("=" * 70)
    random.seed(42)
    engine = LaborRelayEngine(quality_tolerancia=0.15)
    // 1. Registrar benchmarks (sistemas que ja fazem excelente trabalho)
    fmt.Println("\n[1] Registrando benchmarks...")
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
    fmt.Println("\n[2] Registrando pessoas...")
    engine.registrar_pessoa("ana", "Ana", habilidades={"build": 0.9, "test": 0.7}, carga_maxima=3)
    engine.registrar_pessoa("bruno", "Bruno", habilidades={"build": 0.6, "review": 0.8}, carga_maxima=3)
    engine.registrar_pessoa("carla", "Carla", habilidades={"test": 0.95, "review": 0.7}, carga_maxima=4)
    engine.registrar_pessoa("diego", "Diego", habilidades={"deploy": 0.85, "build": 0.5}, carga_maxima=2)
    engine.registrar_pessoa("elena", "Elena", habilidades={"deploy": 0.7, "review": 0.6}, carga_maxima=3)
    // 3. Registrar familia
    fmt.Println("\n[3] Registrando familia (OpenFamilyLabor)...")
    engine.registrar_familia("fam-lima", "Familia Lima",
                            membros = ["ana", "bruno", "carla"],
                            especialidade_coletiva = {"build": 0.8, "test": 0.85})
    // 4. Executar relays
    fmt.Println("\n[4] Executando relays...")
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
    relay1.parar_ao_aprovar = true
    fmt.Println("\n  -> Executando relay: {relay1.nome}")
    resultado1 = engine.executar_relay(relay1)
    fmt.Println("     Estado: {resultado1['estado']}")
    fmt.Println("     Duracao: {resultado1['duracao_total_segundos']}s")
    fmt.Println("     Pernas: {len(resultado1['pernas'])}")
    // Relay 2: review
    relay2 = engine.criar_relay(
        bench_review.id, nome="Review PR #42",
        pessoas = ["bruno", "carla", "elena"],
        workflow_tipo = TipoWorkflow.REVIEW,
    )
    relay2.parar_ao_aprovar = true
    fmt.Println("\n  -> Executando relay: {relay2.nome}")
    resultado2 = engine.executar_relay(relay2)
    fmt.Println("     Estado: {resultado2['estado']}")
    // Relay 3: relay familiar (familia Lima reveza no test)
    relay3 = engine.family.criar_relay_familiar(
        benchmark_id = bench_test.id, familia_id="fam-lima",
        nome = "Test Suite pela Familia Lima",
        workflow_tipo = TipoWorkflow.TEST,
    )
    relay3.parar_ao_aprovar = true
    fmt.Println("\n  -> Executando relay familiar: {relay3.nome}")
    engine.relays[relay3.id] = relay3
    resultado3 = engine.executar_relay(relay3)
    fmt.Println("     Estado: {resultado3['estado']}")
    // Relay 4: deploy via template
    fmt.Println("\n  -> Criando relay de template de deploy...")
    relay4 = engine.criar_relay_de_template(
        engine.workflows.obter_por_tipo(TipoWorkflow.DEPLOY).id,
        nome = "Deploy Producao v2.0",
    )
    relay4.pessoas_disponiveis = ["diego", "elena"]
    fmt.Println("     Executando: {relay4.nome}")
    resultado4 = engine.executar_relay(relay4)
    fmt.Println("     Estado: {resultado4['estado']}")
    // 5. Relatorio final (transparencia)
    fmt.Println("\n" + "=" * 70)
    fmt.Println("[5] RELATORIO DE METRICAS (Transparencia)")
    fmt.Println("=" * 70)
    resumo = engine.metrics.resumo()
    fmt.Println("  Total de relays:        {resumo['total_relays']}")
    fmt.Println("  Taxa de completude:     {resumo['taxa_completude']:.1%}")
    fmt.Println("  Tempo medio:            {resumo['tempo_medio_relays']:.1f}s")
    fmt.Println("  Total de pernas:        {resumo['total_pernas']}")
    fmt.Println("  Taxa aprovacao pernas:  {resumo['taxa_aprovacao_pernas']:.1%}")
    fmt.Println("  Gargalos identificados: {resumo['total_gargalos']}")
    fmt.Println("\n  Ranking de executores (quem && melhor em que):")
    para cada (i, exec_data) em enumere(resumo["ranking_executores"][:5], 1): {
        fmt.Println("    {i}. {exec_data['executor']}: "
            "qualidade={exec_data.get('qualidade_media', 0):.3f}, "
            "aprovacao={exec_data.get('taxa_aprovacao', 0):.1%}, "
            "melhor_em={exec_data.get('melhor_em_benchmark', '-')}")
    // 6. Evolucao dos benchmarks (continuous improvement)
    fmt.Println("\n" + "=" * 70)
    fmt.Println("[6] EVOLUCAO DOS BENCHMARKS (Continuous Improvement)")
    fmt.Println("=" * 70)
    for _, bench := range engine.registry.listar() {
        fmt.Println("  {bench.nome}:")
        fmt.Println("    Qualidade atual: {bench.qualidade_esperada:.4f} "
            "(historico: {len(bench.historico_qualidade)} pontos)")
        fmt.Println("    Tempo atual:     {bench.tempo_segundos:.1f}s")
    fmt.Println("\n" + "=" * 70)
    fmt.Println("OpenLaborRelay - Demonstracao concluida.")
    fmt.Println("=" * 70)
// ===========================================================================
// Entry point
// ===========================================================================
if __name__ == "__main__" {
    _demo()
