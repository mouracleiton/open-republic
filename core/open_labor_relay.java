// OpenLaborRelay -- gerado de Portugol++
public class Openlaborrelay {

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
    OpenLaborRelay;
    ==============;
    Sistema de distribuicao de trabalho baseado em relay (revezamento).;
    Cada servico/sistema que ja faz excelente trabalho vira BENCHMARK -- parametro;
    de qualidade contra o qual novos sistemas sao medidos.;
    Fluxo:;
        1. BenchmarkRegistry registra os melhores sistemas existentes.;
        2. TaskRelay inicia com a tarefa + benchmark alvo.;
        3. SkillMatcher escolhe a proxima pessoa no relay.;
        4. RelayLeg: pessoa executa sua parte -> QualityGate compara contra benchmark.;
        5. Se passar: avanca. Se falhar: outra pessoa assume (anti-bottleneck).;
        6. Ao completar: BenchmarkRegistry atualiza o benchmark (continuous improvement).;
        7. RelayMetrics registra tudo para transparencia.;
    Uso:;
        >>> from open_labor_relay import LaborRelayEngine, Benchmark, TaskRelay;
        >>> engine = LaborRelayEngine();
        >>> engine.registrar_benchmark("build-python", tempo_segundos=120,;
        ...                             qualidade=0.92, autor="sistema-build-antigo");
        >>> relay = engine.criar_relay("build-python",;
        ...                            pessoas=["ana", "bruno", "carla"]);
        >>> resultado = engine.executar_relay(relay);
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
    logging.basicConfig(;
        level = logging.INFO,;
        format = "%(asctime)s [OpenLaborRelay] %(levelname)s %(message)s",;
    );
    log = logging.getLogger("OpenLaborRelay");
    // ===========================================================================
    // Enums
    // ===========================================================================
    public static class EstadoRelay {
        // Estados possiveis de um TaskRelay.
        CRIADO = "criado";
        EM_ANDAMENTO = "em_andamento";
        PAUSADO = "pausado";
        COMPLETO = "completo";
        FALHOU = "falhou";
        CANCELADO = "cancelado";
    public static class EstadoLeg {
        // Estados possiveis de uma perna (leg) do relay.
        AGUARDANDO = "aguardando";
        EM_EXECUCAO = "em_execucao";
        APROVADO = "aprovado";
        REPROVADO = "reprovado";
        PULADO = "pulado"  // anti-bottleneck;
        EXPIRADO = "expirado";
    public static class TipoWorkflow {
        // Tipos de workflow padrao suportados.
        BUILD = "build";
        REVIEW = "review";
        TEST = "test";
        DEPLOY = "deploy";
        GENERIC = "generic";
    public static class Prioridade {
        // Niveis de prioridade de uma tarefa.
        P1 = 1 // critico;
        P2 = 2 // alto;
        P3 = 3 // normal;
        P4 = 4 // baixo;
    // ===========================================================================
    // Benchmark
    // ===========================================================================
    // decorador: @dataclass
    public static class Benchmark {
        //
        Representa um sistema/servico que ja faz EXCELENTE trabalho.;
        Vira PARAMETRO de comparacao para novos sistemas. O benchmark guarda;
        metricas de qualidade, tempo && throughput. Evolui com continuous;
        improvement -- cada relay bem sucedido pode melhorar os valores.;
        //
        id: texto;
        nome: texto;
        String descricao = "";
        String autor = ""  // sistema/servico que originalmente entregou excelencia;
        double qualidade_esperada = 0.0 // 0.0 a 1.0;
        double tempo_segundos = 0.0 // tempo de referencia;
        double throughput_por_hora = 0.0 // itens por hora;
        double custo_referencia = 0.0 // custo de referencia (opcional);
        String categoria = "generic";
        {texto: qualquer} metadados = field(default_factory=dict);
        // historico de evolucao (continuous improvement)
        [flutuante] historico_qualidade = field(default_factory=list);
        [flutuante] historico_tempo = field(default_factory=list);
        double criado_em = field(default_factory=time.time);
        double atualizado_em = field(default_factory=time.time);
        public None __post_init__(self) {
            if (! self.historico_qualidade) {
                self.historico_qualidade.append(self.qualidade_esperada);
            if (! self.historico_tempo) {
                self.historico_tempo.append(self.tempo_segundos);
        // decorador: @classmethod
        funcao criar(cls, nome: texto, descricao: texto = "", autor: texto = "",
                double qualidade_esperada = 0.0, tempo_segundos: flutuante = 0.0,;
                double throughput_por_hora = 0.0, custo_referencia: flutuante = 0.0,;
                String categoria = "generic", **metadados: qualquer) -> "Benchmark":;
            // Cria um Benchmark com id gerado automaticamente.
            return cls(;
                id = "bench-{uuid.uuid4().hex[:8]}",;
                nome = nome,;
                descricao = descricao,;
                autor = autor,;
                qualidade_esperada = qualidade_esperada,;
                tempo_segundos = tempo_segundos,;
                throughput_por_hora = throughput_por_hora,;
                custo_referencia = custo_referencia,;
                categoria = categoria,;
                metadados = dict(metadados),;
            );
        public None melhorar(self, qualidade: flutuante, tempo: flutuante) {
            //
            Continuous improvement: se um relay superar o benchmark,;
            atualiza o benchmark para o novo melhor valor.;
            //
            if (qualidade > self.qualidade_esperada) {
                self.qualidade_esperada = arredonde(qualidade, 4);
                log.info(;
                    "Benchmark '%s' melhorado: qualidade -> %.4f",;
                    self.nome, self.qualidade_esperada,;
                );
            if (tempo > 0 && (self.tempo_segundos == 0 || tempo < self.tempo_segundos)) {
                self.tempo_segundos = arredonde(tempo, 2);
                log.info(;
                    "Benchmark '%s' melhorado: tempo -> %.2fs",;
                    self.nome, self.tempo_segundos,;
                );
            self.historico_qualidade.append(self.qualidade_esperada);
            self.historico_tempo.append(self.tempo_segundos);
            self.atualizado_em = time.time();
        public {texto: qualquer} comparar(self, qualidade: flutuante, tempo: flutuante) {
            // Compara um resultado contra o benchmark.
            delta_q = qualidade - self.qualidade_esperada;
            delta_t = self.tempo_segundos ? tempo - self.tempo_segundos : 0.0;
            return {;
                "benchmark": self.nome,;
                "qualidade_resultado": arredonde(qualidade, 4),;
                "qualidade_referencia": self.qualidade_esperada,;
                "delta_qualidade": arredonde(delta_q, 4),;
                "tempo_resultado": arredonde(tempo, 2),;
                "tempo_referencia": arredonde(self.tempo_segundos, 2),;
                "delta_tempo": arredonde(delta_t, 2),;
                "supera_benchmark": delta_q >= 0,;
            };
        public {texto: qualquer} resumo(self) {
            // Retorna resumo legivel do benchmark.
            return {;
                "id": self.id,;
                "nome": self.nome,;
                "autor": self.autor,;
                "qualidade_esperada": self.qualidade_esperada,;
                "tempo_segundos": self.tempo_segundos,;
                "throughput_por_hora": self.throughput_por_hora,;
                "categoria": self.categoria,;
                "evolucoes": tamanho(self.historico_qualidade),;
            };
    // ===========================================================================
    // RelayLeg (Perna do Relay)
    // ===========================================================================
    // decorador: @dataclass
    public static class RelayLeg {
        //
        Uma perna do relay: uma pessoa/sistema executa sua parte da tarefa.;
        Guarda quem fez, quando comecou/terminou, quanto tempo demorou, resultado;
        && decisao do quality gate.;
        //
        id: texto;
        relay_id: texto;
        executor: texto // pessoa || sistema;
        EstadoLeg estado = EstadoLeg.AGUARDANDO;
        flutuante? iniciado_em = null;
        flutuante? finalizado_em = null;
        double duracao_segundos = 0.0;
        {texto: qualquer} resultado = field(default_factory=dict);
        double nota_qualidade = 0.0;
        boolean aprovado = false;
        String comentario = "";
        int ordem = 0 // ordem no relay (0 = primeira perna);
        // anti-bottleneck
        int tentativas = 0;
        double timeout_segundos = 300.0 // 5 minimo default;
        // decorador: @classmethod
        funcao criar(cls, relay_id: texto, executor: texto, ordem: inteiro,
                double timeout_segundos = 300.0) -> "RelayLeg":;
            return cls(;
                id = "leg-{uuid.uuid4().hex[:8]}",;
                relay_id = relay_id,;
                executor = executor,;
                ordem = ordem,;
                timeout_segundos = timeout_segundos,;
            );
        public None iniciar(self) {
            self.estado = EstadoLeg.EM_EXECUCAO;
            self.iniciado_em = time.time();
            self.tentativas += 1;
            log.info("[Leg %s] Iniciada por '%s' (ordem=%d)", self.id, self.executor, self.ordem);
        funcao finalizar(self, resultado: {texto: qualquer}, nota_qualidade: flutuante,
                    aprovado: logico, comentario: texto = "") -> null:;
            self.finalizado_em = time.time();
            self.duracao_segundos = arredonde(self.finalizado_em - (self.iniciado_em || self.finalizado_em), 2);
            self.resultado = resultado;
            self.nota_qualidade = arredonde(nota_qualidade, 4);
            self.aprovado = aprovado;
            self.comentario = comentario;
            aprovado ? self.estado = EstadoLeg.APROVADO : EstadoLeg.REPROVADO;
            log.info(;
                "[Leg %s] Finalizada por '%s': %s (qualidade=%.3f, tempo=%.1fs)",;
                self.id, self.executor, self.estado.value, self.nota_qualidade, self.duracao_segundos,;
            );
        public None expirar(self) {
            // Anti-bottleneck: marca a perna como expirada (timeout).
            self.estado = EstadoLeg.EXPIRADO;
            log.warning(;
                "[Leg %s] Expirada (timeout) para '%s' apos %d tentativa(s)",;
                self.id, self.executor, self.tentativas,;
            );
        public None pular(self) {
            // Anti-bottleneck: pula esta perna e passa para a proxima.
            self.estado = EstadoLeg.PULADO;
            log.warning("[Leg %s] Pulada para '%s' (anti-bottleneck)", self.id, self.executor);
        public {texto: qualquer} to_dict(self) {
            return {;
                "id": self.id,;
                "relay_id": self.relay_id,;
                "executor": self.executor,;
                "estado": self.estado.value,;
                "iniciado_em": self.iniciado_em,;
                "finalizado_em": self.finalizado_em,;
                "duracao_segundos": self.duracao_segundos,;
                "resultado": self.resultado,;
                "nota_qualidade": self.nota_qualidade,;
                "aprovado": self.aprovado,;
                "comentario": self.comentario,;
                "ordem": self.ordem,;
                "tentativas": self.tentativas,;
            };
    // ===========================================================================
    // QualityGate
    // ===========================================================================
    public static class QualityGate {
        //
        Portao de qualidade: compara o resultado de cada perna do relay contra;
        o benchmark registrado. Decide se o resultado passa || se outra pessoa;
        precisa assumir.;
        //
        public None __init__(self, tolerancia: flutuante = 0.1) {
            // tolerancia: quanto abaixo do benchmark ainda e aceitavel
            self.tolerancia = tolerancia;
        funcao avaliar(self, benchmark: Benchmark, qualidade: flutuante,
                    tempo: flutuante, resultado: {texto: qualquer}) -> {texto: qualquer}:;
            //
            Avalia resultado da perna contra benchmark.;
            Returns:;
                dict com aprovado, nota, comentario, comparacao.;
            //
            comparacao = benchmark.comparar(qualidade, tempo);
            limite = benchmark.qualidade_esperada - self.tolerancia;
            aprovado = qualidade >= limite;
            if (aprovado) {
                comentario = "Qualidade {qualidade:.3f} >= limite {limite:.3f} (tol={self.tolerancia})";
            } else {
                comentario = "Qualidade {qualidade:.3f} < limite {limite:.3f} -- reprovado";
            return {;
                "aprovado": aprovado,;
                "nota": arredonde(qualidade, 4),;
                "comentario": comentario,;
                "comparacao": comparacao,;
                "avaliado_em": time.time(),;
            };
        funcao avaliar_leg(self, benchmark: Benchmark, leg: RelayLeg,
                        qualidade: flutuante, tempo: flutuante,;
                        resultado: {texto: qualquer}) -> {texto: qualquer}:;
            // Avalia e ja aplica resultado no RelayLeg.
            avaliacao = self.avaliar(benchmark, qualidade, tempo, resultado);
            leg.finalizar(;
                resultado = resultado,;
                nota_qualidade = qualidade,;
                aprovado = avaliacao["aprovado"],;
                comentario = avaliacao["comentario"],;
            );
            return avaliacao;
    // ===========================================================================
    // SkillMatcher
    // ===========================================================================
    // decorador: @dataclass
    public static class Pessoa {
        // Representa uma pessoa/sistema participante do relay.
        id: texto;
        nome: texto;
        {texto: flutuante} habilidades = field(default_factory=dict) // skill -> nivel 0-1;
        boolean disponivel = true;
        int carga_atual = 0 // numero de tarefas ativas;
        int carga_maxima = 5;
        texto? familia_id = null;
        int historico_relays = 0;
        double soma_qualidade = 0.0 // soma das qualidades (para media);
        public double nivel(self, skill: texto) {
            return self.habilidades.get(skill, 0.0);
        public double carga_pct(self) {
            // Percentual de carga (0.0 a 1.0).
            if (self.carga_maxima <= 0) {
                return 1.0;
            return minimo(self.carga_atual / self.carga_maxima, 1.0);
        public double disponibilidade_pct(self) {
            // 1.0 = totalmente livre, 0.0 = sem espaco.
            if (! self.disponivel) {
                return 0.0;
            return maximo(0.0, 1.0 - self.carga_pct());
        public double qualidade_media(self) {
            if (self.historico_relays == 0) {
                return 0.0;
            return self.soma_qualidade / self.historico_relays;
        public {texto: qualquer} to_dict(self) {
            return {;
                "id": self.id,;
                "nome": self.nome,;
                "habilidades": dict(self.habilidades),;
                "disponivel": self.disponivel,;
                "carga_atual": self.carga_atual,;
                "carga_maxima": self.carga_maxima,;
                "familia_id": self.familia_id,;
                "historico_relays": self.historico_relays,;
                "qualidade_media": arredonde(self.qualidade_media(), 4),;
            };
    public static class SkillMatcher {
        //
        Escolhe a proxima pessoa no relay baseando-se em:;
        - skill (habilidade na categoria do benchmark);
        - disponibilidade (esta livre?);
        - carga (tem espaco?);
        - qualidade historica;
        //
        public None __init__(self) {
            self.pessoas: {texto: Pessoa} = {};
        public None registrar(self, pessoa: Pessoa) {
            self.pessoas[pessoa.id] = pessoa;
            log.info("Pessoa registrada: '%s' (%s)", pessoa.nome, pessoa.id);
        funcao obter(self, pessoa_id: texto) retorna Pessoa?:
            return self.pessoas.get(pessoa_id);
        funcao _score(self, pessoa: Pessoa, skill: texto, skill_weight: flutuante = 0.5,
                double dispo_weight = 0.3, hist_weight: flutuante = 0.2) -> flutuante:;
            // Score composto: skill + disponibilidade + qualidade historica.
            nivel = pessoa.nivel(skill);
            dispo = pessoa.disponibilidade_pct();
            hist = minimo(pessoa.qualidade_media(), 1.0);
            return (nivel * skill_weight) + (dispo * dispo_weight) + (hist * hist_weight);
        funcao proximo(self, skill: texto, excluir: set? = nulo,
                    int limite = 5) -> List[(Pessoa, flutuante)]:;
            //
            Retorna as melhores pessoas para a skill, ordenadas por score.;
            Args:;
                skill: habilidade necessaria (categoria do benchmark).;
                excluir: ids de pessoas a excluir (ja fizeram parte do relay).;
                limite: maximo de pessoas a retornar.;
            //
            excluir = excluir || set();
            candidatos = [;
                (p, self._score(p, skill));
                /* para p em self.pessoas.values() */
                if p.id ! in excluir && p.disponibilidade_pct() > 0;
            ];
            candidatos.sort(key=(x) -> x[1], reverse=true);
            return candidatos[:limite];
        funcao melhor(self, skill: texto, excluir: set? = None) retorna Pessoa?:
            // Retorna a melhor pessoa para a skill.
            result = self.proximo(skill, excluir=excluir, limite=1);
            result ? retorne result[0][0] : null;
        public [Pessoa] listar_disponiveis(self, skill: texto? = None) {
            // Lista pessoas disponiveis, opcionalmente filtrando por skill > 0.
            result = [];
            /* TODO: for-each Java para p em self.pessoas.values() */
                if (p.disponibilidade_pct() <= 0) {
                    continue;
                if (skill && p.nivel(skill) <= 0) {
                    continue;
                result.append(p);
            return result;
        public {texto: qualquer} to_dict(self) {
            return {pid: p.to_dict() para pid, p in self.pessoas.items()};
    // ===========================================================================
    // TaskRelay
    // ===========================================================================
    // decorador: @dataclass
    public static class TaskRelay {
        //
        Representa uma tarefa distribuida como relay (revezamento).;
        A tarefa comeca com a pessoa A, passa para B, C, etc. Cada perna (leg);
        && avaliada contra o benchmark. O relay termina quando todas as pernas;
        necessarias sao completadas || quando uma perna && aprovada como;
        suficiente (modo single-leg).;
        //
        id: texto;
        nome: texto;
        benchmark_id: texto;
        TipoWorkflow workflow_tipo = TipoWorkflow.GENERIC;
        Prioridade prioridade = Prioridade.P3;
        EstadoRelay estado = EstadoRelay.CRIADO;
        String descricao = "";
        [RelayLeg] pernas = field(default_factory=list);
        texto? pessoa_inicial = null;
        [texto] pessoas_disponiveis = field(default_factory=list);
        // configuracao
        int max_pernas = 5 // limite de revezamento;
        int min_pernas = 1 // minimo para considerar completo;
        boolean parar_ao_aprovar = true // para se uma perna para aprovada;
        double timeout_por_perna = 300.0 // segundos;
        boolean anti_bottleneck = true // pula automaticamente se travar;
        int max_tentativas_por_perna = 2;
        // familia
        texto? familia_id = null // se relay familiar;
        // metricas
        double criado_em = field(default_factory=time.time);
        flutuante? iniciado_em = null;
        flutuante? finalizado_em = null;
        double duracao_total_segundos = 0.0;
        // resultado final
        {texto: qualquer} resultado_final = field(default_factory=dict);
        {texto: qualquer} metadados = field(default_factory=dict);
        // decorador: @classmethod
        funcao criar(cls, nome: texto, benchmark_id: texto,
                TipoWorkflow workflow_tipo = TipoWorkflow.GENERIC,;
                Prioridade prioridade = Prioridade.P3,;
                Optional[[texto]] pessoas = null,;
                texto? pessoa_inicial = null,;
                String descricao = "",;
                int max_pernas = 5,;
                texto? familia_id = null,;
                **metadados: qualquer) -> "TaskRelay":;
            return cls(;
                id = "relay-{uuid.uuid4().hex[:10]}",;
                nome = nome,;
                benchmark_id = benchmark_id,;
                workflow_tipo = workflow_tipo,;
                prioridade = prioridade,;
                descricao = descricao,;
                pessoas_disponiveis = list(pessoas || []),;
                pessoa_inicial = pessoa_inicial,;
                max_pernas = max_pernas,;
                familia_id = familia_id,;
                metadados = dict(metadados),;
            );
        funcao perna_atual(self) retorna RelayLeg?:
            // Retorna a perna em execucao ou aguardando.
            /* TODO: for-each Java para leg em self.pernas */
                if (leg.estado in (EstadoLeg.AGUARDANDO, EstadoLeg.EM_EXECUCAO)) {
                    return leg;
            return null;
        public [RelayLeg] pernas_completas(self) {
            return [l para l em self.pernas if l.estado == EstadoLeg.APROVADO];
        public [RelayLeg] pernas_reprovadas(self) {
            return [l para l em self.pernas if l.estado == EstadoLeg.REPROVADO];
        public [RelayLeg] pernas_puladas(self) {
            return [l para l em self.pernas if l.estado in (EstadoLeg.PULADO, EstadoLeg.EXPIRADO)];
        funcao ultima_aprovada(self) retorna RelayLeg?:
            aprovadas = self.pernas_completas();
            aprovadas ? retorne aprovadas[-1] : null;
        public [texto] executada_por(self) {
            // Lista de pessoas que executaram pernas (transparencia).
            return [l.executor para l em self.pernas if l.estado in (;
                EstadoLeg.APROVADO, EstadoLeg.REPROVADO;
            )];
        public RelayLeg adicionar_perna(self, executor: texto) {
            // Adiciona uma nova perna ao relay.
            ordem = tamanho(self.pernas);
            leg = RelayLeg.criar(;
                relay_id = self.id,;
                executor = executor,;
                ordem = ordem,;
                timeout_segundos = self.timeout_por_perna,;
            );
            self.pernas.append(leg);
            return leg;
        public None iniciar(self) {
            self.estado = EstadoRelay.EM_ANDAMENTO;
            self.iniciado_em = time.time();
        public None completar(self, resultado: {texto: qualquer}) {
            self.estado = EstadoRelay.COMPLETO;
            self.finalizado_em = time.time();
            self.duracao_total_segundos = arredonde(;
                self.finalizado_em - (self.iniciado_em || self.finalizado_em), 2;
            );
            self.resultado_final = resultado;
            log.info(;
                "[Relay %s] COMPLETO em %.1fs (%d pernas, %d aprovadas)",;
                self.id, self.duracao_total_segundos,;
                tamanho(self.pernas), tamanho(self.pernas_completas()),;
            );
        public None falhar(self, motivo: texto) {
            self.estado = EstadoRelay.FALHOU;
            self.finalizado_em = time.time();
            self.resultado_final = {"motivo": motivo};
            log.error("[Relay %s] FALHOU: %s", self.id, motivo);
        public None cancelar(self, motivo: texto = "cancelado pelo usuario") {
            self.estado = EstadoRelay.CANCELADO;
            self.finalizado_em = time.time();
            self.resultado_final = {"motivo": motivo};
            log.info("[Relay %s] CANCELADO: %s", self.id, motivo);
        public {texto: qualquer} to_dict(self) {
            return {;
                "id": self.id,;
                "nome": self.nome,;
                "benchmark_id": self.benchmark_id,;
                "workflow_tipo": self.workflow_tipo.value,;
                "prioridade": self.prioridade.name,;
                "estado": self.estado.value,;
                "descricao": self.descricao,;
                "pernas": [l.to_dict() para l em self.pernas],;
                "pessoa_inicial": self.pessoa_inicial,;
                "pessoas_disponiveis": list(self.pessoas_disponiveis),;
                "max_pernas": self.max_pernas,;
                "min_pernas": self.min_pernas,;
                "parar_ao_aprovar": self.parar_ao_aprovar,;
                "anti_bottleneck": self.anti_bottleneck,;
                "familia_id": self.familia_id,;
                "criado_em": self.criado_em,;
                "iniciado_em": self.iniciado_em,;
                "finalizado_em": self.finalizado_em,;
                "duracao_total_segundos": self.duracao_total_segundos,;
                "resultado_final": self.resultado_final,;
                "metadados": self.metadados,;
            };
    // ===========================================================================
    // BenchmarkRegistry
    // ===========================================================================
    public static class BenchmarkRegistry {
        //
        Registro central de benchmarks.;
        Cada servico/sistema que ja faz EXCELENTE trabalho && registrado aqui;
        como parametro de qualidade. Novos sistemas && novos relays sao medidos;
        contra esses benchmarks.;
        //
        public None __init__(self) {
            self.benchmarks: {texto: Benchmark} = {};
            self._por_categoria: Dict[texto, [texto]] = defaultdict(list);
        public Benchmark registrar(self, benchmark: Benchmark) {
            // Registra um novo benchmark.
            self.benchmarks[benchmark.id] = benchmark;
            if (benchmark.id ! in self._por_categoria[benchmark.categoria]) {
                self._por_categoria[benchmark.categoria].append(benchmark.id);
            log.info(;
                "Benchmark registrado: '%s' (cat=%s, qualidade=%.3f)",;
                benchmark.nome, benchmark.categoria, benchmark.qualidade_esperada,;
            );
            return benchmark;
        funcao registrar_rapido(self, nome: texto, descricao: texto = "", autor: texto = "",
                            double qualidade_esperada = 0.0, tempo_segundos: flutuante = 0.0,;
                            double throughput_por_hora = 0.0, custo_referencia: flutuante = 0.0,;
                            String categoria = "generic", **metadados: qualquer) -> Benchmark:;
            // Cria e registra um benchmark em um passo.
            bench = Benchmark.criar(;
                nome = nome, descricao=descricao, autor=autor,;
                qualidade_esperada = qualidade_esperada,;
                tempo_segundos = tempo_segundos,;
                throughput_por_hora = throughput_por_hora,;
                custo_referencia = custo_referencia,;
                categoria = categoria, **metadados,;
            );
            return self.registrar(bench);
        funcao obter(self, benchmark_id: texto) retorna Benchmark?:
            return self.benchmarks.get(benchmark_id);
        funcao obter_por_nome(self, nome: texto) retorna Benchmark?:
            /* TODO: for-each Java para b em self.benchmarks.values() */
                if (b.nome == nome) {
                    return b;
            return null;
        public [Benchmark] listar(self, categoria: texto? = None) {
            if (categoria) {
                ids = self._por_categoria.get(categoria, []);
                return [self.benchmarks[i] para i em ids if i in self.benchmarks];
            return list(self.benchmarks.values());
        public boolean remover(self, benchmark_id: texto) {
            bench = self.benchmarks.pop(benchmark_id, null);
            if (bench) {
                cat = bench.categoria;
                if (benchmark_id in self._por_categoria[cat]) {
                    self._por_categoria[cat].remove(benchmark_id);
                log.info("Benchmark removido: '%s'", bench.nome);
                return true;
            return false;
        public boolean melhorar(self, benchmark_id: texto, qualidade: flutuante, tempo: flutuante) {
            // Continuous improvement: atualiza benchmark se superado.
            bench = self.obter(benchmark_id);
            if (bench) {
                bench.melhorar(qualidade, tempo);
                return true;
            return false;
        funcao benchmark_categoria(self, categoria: texto) retorna Benchmark?:
            // Retorna o melhor benchmark de uma categoria.
            benchmarks = self.listar(categoria);
            if (! benchmarks) {
                return null;
            return maximo(benchmarks, key=(b) -> b.qualidade_esperada);
        public [texto] categorias(self) {
            return list(self._por_categoria.keys());
        public {texto: qualquer} resumo(self) {
            return {;
                "total_benchmarks": tamanho(self.benchmarks),;
                "categorias": {cat: tamanho(ids) para cat, ids in self._por_categoria.items()},;
                "benchmarks": [b.resumo() para b em self.benchmarks.values()],;
            };
        public {texto: qualquer} to_dict(self) {
            return {;
                bid: {
                    **b.resumo(),;
                    "descricao": b.descricao,;
                    "historico_qualidade": b.historico_qualidade,;
                    "historico_tempo": b.historico_tempo,;
                };
                /* para bid, b in self.benchmarks.items() */
            };
    // ===========================================================================
    // WorkflowTemplate
    // ===========================================================================
    // decorador: @dataclass
    public static class WorkflowTemplate {
        //
        Template de workflow: define o padrao de relay para um tipo de tarefa.;
        Exemplo: workflow de BUILD pode ter 3 pernas (compilar, testar, empacotar),;
        cada uma com skill necessaria && timeout diferente.;
        //
        id: texto;
        nome: texto;
        tipo: TipoWorkflow;
        String descricao = "";
        // lista de estagios: cada estagio e (skill_necessaria, descricao, timeout)
        List[{texto: qualquer}] estagios = field(default_factory=list);
        boolean parar_ao_aprovar = false // templates geralmente precisam de todas as pernas;
        String benchmark_categoria = "generic";
        Prioridade prioridade_padrao = Prioridade.P3;
        {texto: qualquer} metadados = field(default_factory=dict);
        // decorador: @classmethod
        funcao criar(cls, nome: texto, tipo: TipoWorkflow,
                Optional[List[{texto: qualquer}]] estagios = null,;
                String descricao = "",;
                boolean parar_ao_aprovar = false,;
                String benchmark_categoria = "generic",;
                Prioridade prioridade_padrao = Prioridade.P3,;
                **metadados: qualquer) -> "WorkflowTemplate":;
            return cls(;
                id = "wf-{uuid.uuid4().hex[:8]}",;
                nome = nome,;
                tipo = tipo,;
                estagios = list(estagios || []),;
                descricao = descricao,;
                parar_ao_aprovar = parar_ao_aprovar,;
                benchmark_categoria = benchmark_categoria,;
                prioridade_padrao = prioridade_padrao,;
                metadados = dict(metadados),;
            );
        funcao adicionar_estagio(self, skill: texto, descricao: texto = "",
                            double timeout = 300.0,;
                            boolean obrigatorio = true) -> null:;
            self.estagios.append({
                "skill": skill,;
                "descricao": descricao,;
                "timeout": timeout,;
                "obrigatorio": obrigatorio,;
            });
        public int num_estagios(self) {
            return tamanho(self.estagios);
        public {texto: qualquer} to_dict(self) {
            return {;
                "id": self.id,;
                "nome": self.nome,;
                "tipo": self.tipo.value,;
                "descricao": self.descricao,;
                "estagios": list(self.estagios),;
                "parar_ao_aprovar": self.parar_ao_aprovar,;
                "benchmark_categoria": self.benchmark_categoria,;
                "prioridade_padrao": self.prioridade_padrao.name,;
            };
    public static class WorkflowTemplateRegistry {
        // Registro de templates de workflow por tipo.
        public None __init__(self) {
            self.templates: {texto: WorkflowTemplate} = {};
            self._tipos: {TipoWorkflow: texto} = {};
            self._inicializar_padroes();
        public None _inicializar_padroes(self) {
            // Cria templates padrao para build, review, test, deploy.
            // BUILD
            build = WorkflowTemplate.criar(;
                nome = "Build Padrao",;
                tipo = TipoWorkflow.BUILD,;
                benchmark_categoria = "build",;
                parar_ao_aprovar = false,;
            );
            build.adicionar_estagio("compilacao", "Compilar codigo", timeout=120);
            build.adicionar_estagio("lint", "Rodar linter && analise estatica", timeout=60);
            build.adicionar_estagio("empacotamento", "Empacotar artefato", timeout=90);
            self.registrar(build);
            // REVIEW
            review = WorkflowTemplate.criar(;
                nome = "Code Review Padrao",;
                tipo = TipoWorkflow.REVIEW,;
                benchmark_categoria = "review",;
                parar_ao_aprovar = false,;
            );
            review.adicionar_estagio("revisao_seguranca", "Revisao de seguranca", timeout=180);
            review.adicionar_estagio("revisao_qualidade", "Revisao de qualidade", timeout=180);
            self.registrar(review);
            // TEST
            test = WorkflowTemplate.criar(;
                nome = "Test Padrao",;
                tipo = TipoWorkflow.TEST,;
                benchmark_categoria = "test",;
                parar_ao_aprovar = false,;
            );
            test.adicionar_estagio("teste_unitario", "Testes unitarios", timeout=120);
            test.adicionar_estagio("teste_integracao", "Testes de integracao", timeout=240);
            test.adicionar_estagio("teste_e2e", "Testes end-to-end", timeout=300);
            self.registrar(test);
            // DEPLOY
            deploy = WorkflowTemplate.criar(;
                nome = "Deploy Padrao",;
                tipo = TipoWorkflow.DEPLOY,;
                benchmark_categoria = "deploy",;
                parar_ao_aprovar = false,;
            );
            deploy.adicionar_estagio("pre_deploy", "Checagens pre-deploy", timeout=60);
            deploy.adicionar_estagio("deploy", "Executar deploy", timeout=180);
            deploy.adicionar_estagio("post_deploy", "Validacao post-deploy", timeout=120);
            self.registrar(deploy);
        public WorkflowTemplate registrar(self, template: WorkflowTemplate) {
            self.templates[template.id] = template;
            self._tipos[template.tipo] = template.id;
            log.info("Template registrado: '%s' (%s)", template.nome, template.tipo.value);
            return template;
        funcao obter(self, template_id: texto) retorna WorkflowTemplate?:
            return self.templates.get(template_id);
        funcao obter_por_tipo(self, tipo: TipoWorkflow) retorna WorkflowTemplate?:
            tid = self._tipos.get(tipo);
            tid ? retorne self.templates.get(tid) : null;
        public [WorkflowTemplate] listar(self) {
            return list(self.templates.values());
        public {texto: qualquer} to_dict(self) {
            return {tid: t.to_dict() para tid, t in self.templates.items()};
    // ===========================================================================
    // FamilyRelayIntegration (OpenFamilyLabor)
    // ===========================================================================
    // decorador: @dataclass
    public static class Familia {
        // Representa uma familia no OpenFamilyLabor.
        id: texto;
        nome: texto;
        [texto] membros = field(default_factory=list) // ids de pessoas;
        {texto: flutuante} especialidade_coletiva = field(default_factory=dict);
        boolean disponivel = true;
        funcao melhor_skill(self) retorna texto?:
            if (! self.especialidade_coletiva) {
                return null;
            return maximo(self.especialidade_coletiva, key=self.especialidade_coletiva.get);
        public {texto: qualquer} to_dict(self) {
            return {;
                "id": self.id,;
                "nome": self.nome,;
                "membros": list(self.membros),;
                "especialidade_coletiva": dict(self.especialidade_coletiva),;
                "disponivel": self.disponivel,;
            };
    public static class FamilyRelayIntegration {
        //
        Integracao com OpenFamilyLabor.;
        Permite que uma familia inteira reveze numa tarefa. O relay pode;
        passar de membro em membro da familia, respeitando especialidades.;
        //
        public None __init__(self, skill_matcher: SkillMatcher) {
            self.skill_matcher = skill_matcher;
            self.familias: {texto: Familia} = {};
        public Familia registrar_familia(self, familia: Familia) {
            self.familias[familia.id] = familia;
            log.info("Familia registrada: '%s' (%d membros)", familia.nome, tamanho(familia.membros));
            return familia;
        funcao obter_familia(self, familia_id: texto) retorna Familia?:
            return self.familias.get(familia_id);
        funcao membros_disponiveis(self, familia_id: texto,
                                texto? skill = null) -> [texto]:;
            // Retorna membros da familia disponiveis, opcionalmente com skill.
            fam = self.familias.get(familia_id);
            if (! fam) {
                return [];
            result = [];
            /* TODO: for-each Java para mid em fam.membros */
                p = self.skill_matcher.obter(mid);
                if (p && p.disponibilidade_pct() > 0) {
                    if (skill && null || p.nivel(skill) > 0) {
                        result.append(mid);
            return result;
        funcao proximo_membro(self, familia_id: texto, skill: texto,
                        set? excluir = null) -> texto?:;
            // Escolhe o proximo membro da familia para o relay.
            excluir = excluir || set();
            candidatos_ids = self.membros_disponiveis(familia_id, skill=skill);
            candidatos = [;
                (mid, self.skill_matcher._score(self.skill_matcher.obter(mid), skill));
                /* para mid em candidatos_ids */
                if mid ! in excluir;
            ];
            candidatos.sort(key=(x) -> x[1], reverse=true);
            candidatos ? retorne candidatos[0][0] : null;
        funcao criar_relay_familiar(self, benchmark_id: texto, familia_id: texto,
                                String nome = "", descricao: texto = "",;
                                TipoWorkflow workflow_tipo = TipoWorkflow.GENERIC,;
                                Prioridade prioridade = Prioridade.P3,;
                                int max_pernas = 5) -> TaskRelay:;
            // Cria um TaskRelay onde a familia inteira reveza.
            fam = self.familias.get(familia_id);
            if (! fam) {
                lance ValueError("Familia '{familia_id}' ! encontrada");
            relay = TaskRelay.criar(;
                nome = nome  ||  "Relay Familia {fam.nome}",;
                benchmark_id = benchmark_id,;
                workflow_tipo = workflow_tipo,;
                prioridade = prioridade,;
                pessoas = list(fam.membros),;
                descricao = descricao,;
                max_pernas = max_pernas,;
                familia_id = familia_id,;
            );
            log.info(;
                "Relay familiar criado: familia='%s', benchmark='%s'",;
                fam.nome, benchmark_id,;
            );
            return relay;
        public {texto: qualquer} to_dict(self) {
            return {fid: f.to_dict() para fid, f in self.familias.items()};
    // ===========================================================================
    // RelayMetrics
    // ===========================================================================
    public static class RelayMetrics {
        //
        Coleta && calcula metricas de todos os relays: tempo total, gargalos,;
        quem && melhor em que, taxa de aprovacao, etc.;
        //
        public None __init__(self) {
            self.relays: {texto: TaskRelay} = {};
            // index por executor
            self._por_executor: Dict[texto, [texto]] = defaultdict(list);
            // index por benchmark
            self._por_benchmark: Dict[texto, [texto]] = defaultdict(list);
        public None registrar_relay(self, relay: TaskRelay) {
            self.relays[relay.id] = relay;
            /* TODO: for-each Java para leg em relay.pernas */
                self._por_executor[leg.executor].append(relay.id);
            self._por_benchmark[relay.benchmark_id].append(relay.id);
        // --- Metricas globais --------------------------------------------------
        public int total_relays(self) {
            return tamanho(self.relays);
        public double taxa_completude(self) {
            if (! self.relays) {
                return 0.0;
            completos = soma(1 para r em self.relays.values() if r.estado == EstadoRelay.COMPLETO);
            return completos / tamanho(self.relays);
        public double tempo_medio(self) {
            tempos = [r.duracao_total_segundos para r em self.relays.values();
                    if r.duracao_total_segundos > 0];
            tempos ? retorne statistics.mean(tempos) : 0.0;
        public int total_pernas(self) {
            return soma(tamanho(r.pernas) para r em self.relays.values());
        public double taxa_aprovacao_pernas(self) {
            total = self.total_pernas();
            if (total == 0) {
                return 0.0;
            aprovadas = soma(tamanho(r.pernas_completas()) para r em self.relays.values());
            return aprovadas / total;
        // --- Metricas por executor --------------------------------------------
        public [TaskRelay] relays_por_executor(self, executor: texto) {
            ids = self._por_executor.get(executor, []);
            return [self.relays[i] para i em ids if i in self.relays];
        public [RelayLeg] pernas_por_executor(self, executor: texto) {
            result = [];
            /* TODO: for-each Java para relay em self.relays_por_executor(executor) */
                /* TODO: for-each Java para leg em relay.pernas */
                    if (leg.executor == executor) {
                        result.append(leg);
            return result;
        public {texto: qualquer} desempenho_executor(self, executor: texto) {
            // Retorna quem e melhor em que: metricas por executor.
            pernas = self.pernas_por_executor(executor);
            if (! pernas) {
                return {"executor": executor, "total_pernas": 0};
            aprovadas = [l para l em pernas if l.estado == EstadoLeg.APROVADO];
            tempos = [l.duracao_segundos para l em pernas if l.duracao_segundos > 0];
            qualidades = [l.nota_qualidade para l em pernas if l.nota_qualidade > 0];
            // quem e melhor em que: agrupar por benchmark
            Dict[texto, {texto: flutuante}] por_benchmark = defaultdict(() -> {"count": 0, "soma_q": 0.0});
            /* TODO: for-each Java para l em pernas */
                relay = self.relays.get(l.relay_id);
                if (relay) {
                    por_benchmark[relay.benchmark_id]["count"] += 1;
                    por_benchmark[relay.benchmark_id]["soma_q"] += l.nota_qualidade;
            melhor_em = null;
            melhor_media = 0.0;
            /* para cada (bid, dados) em por_benchmark.items(): */
                if (dados["count"] > 0) {
                    media = dados["soma_q"] / dados["count"];
                    if (media > melhor_media) {
                        melhor_media = media;
                        melhor_em = bid;
            return {;
                "executor": executor,;
                "total_pernas": tamanho(pernas),;
                "pernas_aprovadas": tamanho(aprovadas),;
                "taxa_aprovacao": arredonde(tamanho(aprovadas) / tamanho(pernas), 4),;
                tempos ? "tempo_medio": arredonde(statistics.mean(tempos), 2) : 0.0,;
                qualidades ? "qualidade_media": arredonde(statistics.mean(qualidades), 4) : 0.0,;
                "melhor_em_benchmark": melhor_em,;
                "melhor_em_media": arredonde(melhor_media, 4),;
            };
        funcao ranking_executores(self) retorna List[{texto: qualquer}]:
            // Ranking de executores por qualidade media.
            executores = list(self._por_executor.keys());
            dados = [self.desempenho_executor(&&) para && em executores];
            dados.sort(key=(x) -> x.get("qualidade_media", 0), reverse=true);
            return dados;
        // --- Metricas por benchmark -------------------------------------------
        funcao gargalos(self) retorna List[{texto: qualquer}]:
            //
            Identifica gargalos: pernas que demoraram mais, foram puladas;
            || expiradas com mais frequencia.;
            //
            gargalos = [];
            /* TODO: for-each Java para relay em self.relays.values() */
                /* TODO: for-each Java para leg em relay.pernas */
                    if (leg.estado in (EstadoLeg.EXPIRADO, EstadoLeg.PULADO)) {
                        gargalos.append({
                            "relay_id": relay.id,;
                            "leg_id": leg.id,;
                            "executor": leg.executor,;
                            "estado": leg.estado.value,;
                            "tentativas": leg.tentativas,;
                            "duracao": leg.duracao_segundos,;
                        });
                    elif leg.duracao_segundos > 600: // mais de 10 minimo;
                        gargalos.append({
                            "relay_id": relay.id,;
                            "leg_id": leg.id,;
                            "executor": leg.executor,;
                            "estado": "lento",;
                            "duracao": leg.duracao_segundos,;
                        });
            return gargalos;
        public {texto: qualquer} resumo(self) {
            return {;
                "total_relays": self.total_relays(),;
                "taxa_completude": arredonde(self.taxa_completude(), 4),;
                "tempo_medio_relays": arredonde(self.tempo_medio(), 2),;
                "total_pernas": self.total_pernas(),;
                "taxa_aprovacao_pernas": arredonde(self.taxa_aprovacao_pernas(), 4),;
                "total_gargalos": tamanho(self.gargalos()),;
                "ranking_executores": self.ranking_executores()[:10],;
            };
        public {texto: qualquer} to_dict(self) {
            return {;
                "relays": {rid: r.to_dict() para rid, r in self.relays.items()},;
                "resumo": self.resumo(),;
            };
    // ===========================================================================
    // LaborRelayEngine (Motor Principal)
    // ===========================================================================
    // Tipo para funcao de execucao de perna: recebe (relay, leg, benchmark) -> (qualidade, tempo, resultado)
    ExecutorPerna = Callable[[TaskRelay, RelayLeg, Benchmark], Tuple[flutuante, flutuante, {texto: qualquer}]];
    public static class LaborRelayEngine {
        //
        Motor principal do OpenLaborRelay.;
        Orquestra todo o sistema:;
        - BenchmarkRegistry (parametros de qualidade);
        - SkillMatcher (escolhe proxima pessoa);
        - QualityGate (avalia contra benchmark);
        - WorkflowTemplateRegistry (templates por tipo);
        - FamilyRelayIntegration (relay familiar);
        - RelayMetrics (transparencia && metricas);
        O engine executa relays aplicando anti-bottleneck, continuous improvement;
        && transparencia total.;
        //
        public None __init__(self, quality_tolerancia: flutuante = 0.1) {
            self.registry = BenchmarkRegistry();
            self.matcher = SkillMatcher();
            self.gate = QualityGate(tolerancia=quality_tolerancia);
            self.workflows = WorkflowTemplateRegistry();
            self.family = FamilyRelayIntegration(self.matcher);
            self.metrics = RelayMetrics();
            // funcao de execucao (injetavel para testes/simulacao)
            self._executor: ExecutorPerna? = null;
            // armazenamento de relays em execucao
            self.relays: {texto: TaskRelay} = {};
        // --- Configuracao ------------------------------------------------------
        public None set_executor(self, fn: ExecutorPerna) {
            // Define funcao customizada para executar pernas (simulacao/producao).
            self._executor = fn;
        public Benchmark registrar_benchmark(self, nome: texto, **kwargs: qualquer) {
            // Atalho para registrar benchmark no registry.
            return self.registry.registrar_rapido(nome=nome, **kwargs);
        funcao registrar_pessoa(self, pessoa_id: texto, nome: texto,
                            Optional[{texto: flutuante}] habilidades = null,;
                            boolean disponivel = true,;
                            int carga_maxima = 5,;
                            texto? familia_id = null) -> Pessoa:;
            // Atalho para registrar pessoa no matcher.
            p = Pessoa(;
                id = pessoa_id,;
                nome = nome,;
                habilidades = dict(habilidades || {}),;
                disponivel = disponivel,;
                carga_maxima = carga_maxima,;
                familia_id = familia_id,;
            );
            self.matcher.registrar(p);
            return p;
        funcao registrar_familia(self, familia_id: texto, nome: texto,
                            membros: [texto],;
                            Optional[{texto: flutuante}] especialidade_coletiva = null) -> Familia:;
            // Atalho para registrar familia.
            fam = Familia(;
                id = familia_id,;
                nome = nome,;
                membros = list(membros),;
                especialidade_coletiva = dict(especialidade_coletiva || {}),;
            );
            return self.family.registrar_familia(fam);
        // --- Criacao de relays -------------------------------------------------
        funcao criar_relay(self, benchmark_nome_ou_id: texto,
                        Optional[[texto]] pessoas = null,;
                        String nome = "",;
                        String descricao = "",;
                        TipoWorkflow workflow_tipo = TipoWorkflow.GENERIC,;
                        Prioridade prioridade = Prioridade.P3,;
                        texto? pessoa_inicial = null,;
                        int max_pernas = 5,;
                        texto? familia_id = null) -> TaskRelay:;
            // Cria um TaskRelay a partir de benchmark existente.
            // resolver benchmark
            bench = self.registry.obter(benchmark_nome_ou_id);
            if (! bench) {
                bench = self.registry.obter_por_nome(benchmark_nome_ou_id);
            if (! bench) {
                lance ValueError("Benchmark '{benchmark_nome_ou_id}' ! encontrado");
            relay = TaskRelay.criar(;
                nome = nome  ||  "Relay para {bench.nome}",;
                benchmark_id = bench.id,;
                workflow_tipo = workflow_tipo,;
                prioridade = prioridade,;
                pessoas = pessoas,;
                pessoa_inicial = pessoa_inicial,;
                descricao = descricao,;
                max_pernas = max_pernas,;
                familia_id = familia_id,;
            );
            self.relays[relay.id] = relay;
            log.info("Relay criado: '%s' (benchmark=%s)", relay.nome, bench.nome);
            return relay;
        funcao criar_relay_de_template(self, template_id: texto,
                                    String benchmark_nome_ou_id = "",;
                                    String nome = "",;
                                    String descricao = "") -> TaskRelay:;
            // Cria relay a partir de template de workflow.
            template = self.workflows.obter(template_id);
            if (! template) {
                lance ValueError("Template '{template_id}' ! encontrado");
            // resolver benchmark
            bench = null;
            if (benchmark_nome_ou_id) {
                bench = self.registry.obter(benchmark_nome_ou_id) || self.registry.obter_por_nome(benchmark_nome_ou_id);
            if (! bench) {
                bench = self.registry.benchmark_categoria(template.benchmark_categoria);
            if (! bench) {
                lance ValueError(;
                    "Nenhum benchmark encontrado para categoria '{template.benchmark_categoria}'";
                );
            relay = TaskRelay.criar(;
                nome = nome  ||  "Relay {template.nome}",;
                benchmark_id = bench.id,;
                workflow_tipo = template.tipo,;
                prioridade = template.prioridade_padrao,;
                descricao = descricao || template.descricao,;
                max_pernas = maximo(template.num_estagios(), 1),;
            );
            relay.parar_ao_aprovar = template.parar_ao_aprovar;
            self.relays[relay.id] = relay;
            log.info(;
                "Relay criado de template '%s' (benchmark=%s, %d estagios)",;
                template.nome, bench.nome, template.num_estagios(),;
            );
            return relay;
        // --- Execucao de relay -------------------------------------------------
        funcao _executar_perna(self, relay: TaskRelay, leg: RelayLeg,
                            benchmark: Benchmark) -> Tuple[flutuante, flutuante, {texto: qualquer}]:;
            // Executa uma perna: usa executor customizado ou simulacao.
            if (self._executor) {
                return self._executor(relay, leg, benchmark);
            // simulacao padrao
            return self._simular_perna(relay, leg, benchmark);
        funcao _simular_perna(self, relay: TaskRelay, leg: RelayLeg,
                        benchmark: Benchmark) -> Tuple[flutuante, flutuante, {texto: qualquer}]:;
            //
            Simulacao padrao: gera qualidade && tempo baseados na skill da pessoa;
            contra o benchmark. Usado quando nenhum executor real && definido.;
            //
            pessoa = self.matcher.obter(leg.executor);
            skill = benchmark.categoria;
            nivel = pessoa ? pessoa.nivel(skill) : 0.5;
            // qualidade depende do nivel + ruido
            base_q = benchmark.qualidade_esperada * nivel;
            ruido = random.uniform(-0.1, 0.15);
            qualidade = maximo(0.0, minimo(1.0, base_q + ruido));
            // tempo depende do nivel (mais habilidade = mais rapido)
            fator_tempo = nivel > 0 ? 2.0 - nivel : 2.0;
            tempo = benchmark.tempo_segundos * fator_tempo * random.uniform(0.7, 1.3);
            if (benchmark.tempo_segundos == 0) {
                tempo = random.uniform(30, 180);
            resultado = {
                "simulado": true,;
                "executor": leg.executor,;
                "skill": skill,;
                "nivel": arredonde(nivel, 3),;
            };
            return arredonde(qualidade, 4), arredonde(tempo, 2), resultado;
        funcao _encontrar_proxima_pessoa(self, relay: TaskRelay,
                                    benchmark: Benchmark,;
                                    set? excluir = null) -> texto?:;
            // Encontra a proxima pessoa para o relay (skill matching).
            excluir = excluir || set();
            // se relay familiar, usar integracao familiar
            if (relay.familia_id) {
                membro = self.family.proximo_membro(;
                    relay.familia_id, benchmark.categoria, excluir=excluir,;
                );
                if (membro) {
                    return membro;
            // se ha lista explicita de pessoas, usar skill matcher sobre elas
            if (relay.pessoas_disponiveis) {
                /* TODO: for-each Java para pid em relay.pessoas_disponiveis */
                    if (pid ! in excluir) {
                        p = self.matcher.obter(pid);
                        if (p && p.disponibilidade_pct() > 0) {
                            return pid;
                return null;
            // senao, buscar no matcher global
            pessoa = self.matcher.melhor(benchmark.categoria, excluir=excluir);
            pessoa ? retorne pessoa.id : null;
        funcao _executar_perna_com_retry(self, relay: TaskRelay, leg: RelayLeg,
                                    benchmark: Benchmark) -> logico:;
            //
            Executa perna com anti-bottleneck: se travar || reprovar,;
            tenta ate max_tentativas_por_perna, depois passa para proxima.;
            //
            /* TODO: for-each Java para tentativa em intervalo(relay.max_tentativas_por_perna) */
                leg.iniciar();
                tente:;
                    desempacote qualidade, tempo, resultado = self._executar_perna(relay, leg, benchmark);
                capture Exception como &&:;
                    log.error("[Leg %s] Erro na execucao: %s", leg.id, &&);
                    leg.comentario = "Erro: {&&}";
                    continue;
                avaliacao = self.gate.avaliar_leg(benchmark, leg, qualidade, tempo, resultado);
                if (avaliacao["aprovado"]) {
                    // atualizar carga da pessoa
                    self._atualizar_carga(leg.executor, delta=-1);
                    return true;
                } else {
                    log.info(;
                        "[Leg %s] Reprovada (tentativa %d/%d): %s",;
                        leg.id, tentativa + 1, relay.max_tentativas_por_perna,;
                        avaliacao["comentario"],;
                    );
            // esgotou tentativas: anti-bottleneck
            if (relay.anti_bottleneck) {
                leg.pular();
            } else {
                leg.expirar();
            self._atualizar_carga(leg.executor, delta=-1);
            return false;
        public None _atualizar_carga(self, executor: texto, delta: inteiro) {
            // Atualiza carga atual de uma pessoa.
            p = self.matcher.obter(executor);
            if (p) {
                p.carga_atual = maximo(0, p.carga_atual + delta);
                if (delta > 0) {
                    p.historico_relays += 1;
                    // qualidade sera somada externamente se necessario
        public {texto: qualquer} executar_relay(self, relay: TaskRelay) {
            //
            Executa um TaskRelay completo: aplica relay, quality gate,;
            anti-bottleneck, continuous improvement && registra metricas.;
            //
            benchmark = self.registry.obter(relay.benchmark_id);
            if (! benchmark) {
                relay.falhar("Benchmark '{relay.benchmark_id}' ! encontrado");
                return relay.to_dict();
            relay.iniciar();
            set ja_executaram = set();
            melhor_qualidade = 0.0;
            melhor_tempo = flutuante("inf");
            RelayLeg? leg_aprovada_final = null;
            /* TODO: for-each Java para perna_idx em intervalo(relay.max_pernas) */
                // escolher proxima pessoa
                executor = self._encontrar_proxima_pessoa(relay, benchmark, excluir=ja_executaram);
                // se nao tem ninguem, tentar liberar ja_executaram para retry
                if (! executor && ja_executaram && relay.anti_bottleneck) {
                    log.info("[Relay %s] Sem novos candidatos; resetando exclusoes para retry", relay.id);
                    ja_executaram.clear();
                    executor = self._encontrar_proxima_pessoa(relay, benchmark, excluir=ja_executaram);
                if (! executor) {
                    relay.falhar("Sem pessoas disponiveis para o relay");
                    self.metrics.registrar_relay(relay);
                    return relay.to_dict();
                // criar e executar perna
                leg = relay.adicionar_perna(executor);
                self._atualizar_carga(executor, delta=+1);
                ja_executaram.add(executor);
                aprovado = self._executar_perna_com_retry(relay, leg, benchmark);
                // registrar qualidade no historico da pessoa
                p = self.matcher.obter(executor);
                if (p) {
                    p.soma_qualidade += leg.nota_qualidade;
                // acompanhar melhor resultado
                if (leg.nota_qualidade > melhor_qualidade) {
                    melhor_qualidade = leg.nota_qualidade;
                    melhor_tempo = leg.duracao_segundos;
                    leg_aprovada_final = leg;
                if (aprovado && relay.parar_ao_aprovar) {
                    // continuous improvement: se superou benchmark, atualizar
                    if (melhor_qualidade > benchmark.qualidade_esperada) {
                        self.registry.melhorar(relay.benchmark_id, melhor_qualidade, melhor_tempo);
                    relay.completar({
                        "leg_aprovada": leg.to_dict(),;
                        "qualidade_final": melhor_qualidade,;
                        "executor_final": executor,;
                        "benchmark_nome": benchmark.nome,;
                    });
                    self.metrics.registrar_relay(relay);
                    return relay.to_dict();
                // se nao parar_ao_aprovar, continua ate max_pernas
            // apos max_pernas: verificar se pelo menos uma perna foi aprovada
            aprovadas = relay.pernas_completas();
            if (aprovadas) {
                // continuous improvement
                if (melhor_qualidade > benchmark.qualidade_esperada) {
                    self.registry.melhorar(relay.benchmark_id, melhor_qualidade, melhor_tempo);
                relay.completar({
                    "pernas_aprovadas": tamanho(aprovadas),;
                    "qualidade_final": melhor_qualidade,;
                    leg_aprovada_final ? "executor_melhor": leg_aprovada_final.executor : null,;
                    "benchmark_nome": benchmark.nome,;
                });
            } else {
                relay.falhar("Todas as {relay.max_pernas} pernas foram reprovadas/puladas");
            self.metrics.registrar_relay(relay);
            return relay.to_dict();
        // --- Consultas ---------------------------------------------------------
        funcao obter_relay(self, relay_id: texto) retorna TaskRelay?:
            return self.relays.get(relay_id);
        public [TaskRelay] listar_relays(self, estado: EstadoRelay? = None) {
            relays = list(self.relays.values());
            if (estado) {
                relays = [r para r em relays if r.estado == estado];
            return relays;
        public {texto: qualquer} relatorios(self) {
            // Relatorio completo do estado do engine (transparencia).
            return {;
                "benchmarks": self.registry.resumo(),;
                "pessoas": self.matcher.to_dict(),;
                "workflows": self.workflows.to_dict(),;
                "familias": self.family.to_dict(),;
                "metrics": self.metrics.resumo(),;
                "relays_ativos": tamanho(self.listar_relays(EstadoRelay.EM_ANDAMENTO)),;
                "relays_completos": tamanho(self.listar_relays(EstadoRelay.COMPLETO)),;
            };
        public String exportar_json(self, caminho: texto? = None) {
            // Exporta estado completo do engine como JSON.
            dados = self.relatorios();
            dados["relays"] = {rid: r.to_dict() para rid, r in self.relays.items()};
            texto = json.dumps(dados, indent=2, default=texto, ensure_ascii=false);
            if (caminho) {
                Path(caminho).write_text(texto, encoding="utf-8");
                log.info("Estado exportado para %s", caminho);
            return texto;
    // ===========================================================================
    // Demo / Teste
    // ===========================================================================
    public None _demo() {
        // Demonstracao do OpenLaborRelay em acao.
        System.out.println("=" * 70);
        System.out.println("OpenLaborRelay - Demonstracao");
        System.out.println("=" * 70);
        random.seed(42);
        engine = LaborRelayEngine(quality_tolerancia=0.15);
        // 1. Registrar benchmarks (sistemas que ja fazem excelente trabalho)
        System.out.println("\n[1] Registrando benchmarks...");
        engine.registrar_benchmark(;
            "Build Python Rapido", autor="make-legacy",;
            qualidade_esperada = 0.85, tempo_segundos=90,;
            throughput_por_hora = 40, categoria="build",;
            descricao = "Sistema de build Python legado, excelente trabalho.",;
        );
        engine.registrar_benchmark(;
            "Review Seguranca Profundo", autor="sonarqube-old",;
            qualidade_esperada = 0.90, tempo_segundos=120,;
            throughput_por_hora = 20, categoria="review",;
        );
        engine.registrar_benchmark(;
            "Test Suite Completa", autor="pytest-ci",;
            qualidade_esperada = 0.88, tempo_segundos=180,;
            throughput_por_hora = 15, categoria="test",;
        );
        engine.registrar_benchmark(;
            "Deploy Blue-Green", autor="ansible-deploy",;
            qualidade_esperada = 0.92, tempo_segundos=240,;
            throughput_por_hora = 10, categoria="deploy",;
        );
        // 2. Registrar pessoas com habilidades
        System.out.println("\n[2] Registrando pessoas...");
        engine.registrar_pessoa("ana", "Ana", habilidades={"build": 0.9, "test": 0.7}, carga_maxima=3);
        engine.registrar_pessoa("bruno", "Bruno", habilidades={"build": 0.6, "review": 0.8}, carga_maxima=3);
        engine.registrar_pessoa("carla", "Carla", habilidades={"test": 0.95, "review": 0.7}, carga_maxima=4);
        engine.registrar_pessoa("diego", "Diego", habilidades={"deploy": 0.85, "build": 0.5}, carga_maxima=2);
        engine.registrar_pessoa("elena", "Elena", habilidades={"deploy": 0.7, "review": 0.6}, carga_maxima=3);
        // 3. Registrar familia
        System.out.println("\n[3] Registrando familia (OpenFamilyLabor)...");
        engine.registrar_familia("fam-lima", "Familia Lima",;
                                membros = ["ana", "bruno", "carla"],;
                                especialidade_coletiva = {"build": 0.8, "test": 0.85});
        // 4. Executar relays
        System.out.println("\n[4] Executando relays...");
        bench_build = engine.registry.obter_por_nome("Build Python Rapido");
        bench_review = engine.registry.obter_por_nome("Review Seguranca Profundo");
        bench_test = engine.registry.obter_por_nome("Test Suite Completa");
        bench_deploy = engine.registry.obter_por_nome("Deploy Blue-Green");
        // Relay 1: build simples (parar ao aprovar)
        relay1 = engine.criar_relay(;
            bench_build.id, nome="Build do Modulo X",;
            pessoas = ["ana", "bruno", "diego"],;
            workflow_tipo = TipoWorkflow.BUILD,;
            prioridade = Prioridade.P2,;
        );
        relay1.parar_ao_aprovar = true;
        System.out.println("\n  -> Executando relay: {relay1.nome}");
        resultado1 = engine.executar_relay(relay1);
        System.out.println("     Estado: {resultado1['estado']}");
        System.out.println("     Duracao: {resultado1['duracao_total_segundos']}s");
        System.out.println("     Pernas: {len(resultado1['pernas'])}");
        // Relay 2: review
        relay2 = engine.criar_relay(;
            bench_review.id, nome="Review PR #42",;
            pessoas = ["bruno", "carla", "elena"],;
            workflow_tipo = TipoWorkflow.REVIEW,;
        );
        relay2.parar_ao_aprovar = true;
        System.out.println("\n  -> Executando relay: {relay2.nome}");
        resultado2 = engine.executar_relay(relay2);
        System.out.println("     Estado: {resultado2['estado']}");
        // Relay 3: relay familiar (familia Lima reveza no test)
        relay3 = engine.family.criar_relay_familiar(;
            benchmark_id = bench_test.id, familia_id="fam-lima",;
            nome = "Test Suite pela Familia Lima",;
            workflow_tipo = TipoWorkflow.TEST,;
        );
        relay3.parar_ao_aprovar = true;
        System.out.println("\n  -> Executando relay familiar: {relay3.nome}");
        engine.relays[relay3.id] = relay3;
        resultado3 = engine.executar_relay(relay3);
        System.out.println("     Estado: {resultado3['estado']}");
        // Relay 4: deploy via template
        System.out.println("\n  -> Criando relay de template de deploy...");
        relay4 = engine.criar_relay_de_template(;
            engine.workflows.obter_por_tipo(TipoWorkflow.DEPLOY).id,;
            nome = "Deploy Producao v2.0",;
        );
        relay4.pessoas_disponiveis = ["diego", "elena"];
        System.out.println("     Executando: {relay4.nome}");
        resultado4 = engine.executar_relay(relay4);
        System.out.println("     Estado: {resultado4['estado']}");
        // 5. Relatorio final (transparencia)
        System.out.println("\n" + "=" * 70);
        System.out.println("[5] RELATORIO DE METRICAS (Transparencia)");
        System.out.println("=" * 70);
        resumo = engine.metrics.resumo();
        System.out.println("  Total de relays:        {resumo['total_relays']}");
        System.out.println("  Taxa de completude:     {resumo['taxa_completude']:.1%}");
        System.out.println("  Tempo medio:            {resumo['tempo_medio_relays']:.1f}s");
        System.out.println("  Total de pernas:        {resumo['total_pernas']}");
        System.out.println("  Taxa aprovacao pernas:  {resumo['taxa_aprovacao_pernas']:.1%}");
        System.out.println("  Gargalos identificados: {resumo['total_gargalos']}");
        System.out.println("\n  Ranking de executores (quem && melhor em que):");
        /* para cada (i, exec_data) em enumere(resumo["ranking_executores"][:5], 1): */
            System.out.println("    {i}. {exec_data['executor']}: ";
                "qualidade={exec_data.get('qualidade_media', 0):.3f}, ";
                "aprovacao={exec_data.get('taxa_aprovacao', 0):.1%}, ";
                "melhor_em={exec_data.get('melhor_em_benchmark', '-')}");
        // 6. Evolucao dos benchmarks (continuous improvement)
        System.out.println("\n" + "=" * 70);
        System.out.println("[6] EVOLUCAO DOS BENCHMARKS (Continuous Improvement)");
        System.out.println("=" * 70);
        /* TODO: for-each Java para bench em engine.registry.listar() */
            System.out.println("  {bench.nome}:");
            System.out.println("    Qualidade atual: {bench.qualidade_esperada:.4f} ";
                "(historico: {len(bench.historico_qualidade)} pontos)");
            System.out.println("    Tempo atual:     {bench.tempo_segundos:.1f}s");
        System.out.println("\n" + "=" * 70);
        System.out.println("OpenLaborRelay - Demonstracao concluida.");
        System.out.println("=" * 70);
    // ===========================================================================
    // Entry point
    // ===========================================================================
    if (__name__ == "__main__") {
        _demo();
}
