// OpenTerminal -- Terminais da Republica em Todo Estabelecimento -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenTerminal -- Terminais da Republica em Todo Estabelecimento;
================================================================;
"Toda TV ociosa && um terminal da Republica.;
Todo computador parado && uma oportunidade de contribuir.;
Todo smartphone na mesa && trabalho esperando.;
O laborante ! espera trabalho -- ele encontra.";
CONCEITO:;
Cada estabelecimento (loja, hospital, escola, praca, transporte);
tem pelo menos 1 terminal (TV/PC/Smartphone) disponivel.;
O LABORANTE (cidadao trabalhador da Republica) usa o terminal;
no tempo ocioso para:;
- Trabalhar (OpenLaborRelay: pega tarefas, executa, ganha credito);
- Aprender (OpenGamesRealistic: simuladores que ensinam skills);
- Votar (OpenDemocracy: participacao democratica);
- Acessar servicos (OpenHealth, OpenVacine, OpenCredit);
Resultado: tempo morto vira tempo produtivo.;
Sem centro de trabalho. Sem deslocamento.;
O terminal esta ONDE a pessoa esta.;
TIPOS DE TERMINAL:;
TV SMART -- TV com app da Republica (OpenLite);
COMPUTADOR -- PC com OpenLinux/OpenDesktop;
SMARTPHONE -- celular com OpenMarketplace app;
TERMINAL BURRO -- tela+teclado minimo (OpenKit);
TABLET -- tablet com OpenLite;
KIOSK -- terminal publico em praca/rua;
ONDE FICAM:;
Mercados, farmacias, hospitais, escolas, pracas, onibus, trem,;
restaurantes, oficinas, FabLabs, postos de saude, bibliotecas.;
QUEM USA:;
TODO cidadao && LABORANTE. Todo laborante tem direito de usar;
qualquer terminal. Sem login corporativo. Sem senha de empresa.;
So precisa do ID nacional (OpenKit).;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime
// ============================================================================
// 1. TIPOS DE TERMINAL
// ============================================================================
class TerminalType {
    TV_SMART = "tv_smart"  // TV com app Republica;
    COMPUTER = "computador"  // PC completo;
    SMARTPHONE = "smartphone"  // celular;
    TERMINAL_BURRO = "terminal_burro"  // minimo (tela+teclado);
    TABLET = "tablet"  // tablet;
    KIOSK = "kiosk"  // terminal publico;
class EstablishmentType {
    // Onde o terminal fica.
    MARKET = "mercado";
    PHARMACY = "farmacia";
    HOSPITAL = "hospital";
    SCHOOL = "escola";
    UNIVERSITY = "universidade";
    SQUARE = "praca";
    BUS = "onibus";
    TRAIN = "trem";
    METRO = "metro";
    RESTAURANT = "restaurante";
    WORKSHOP = "oficina";
    FABLAB = "fablab";
    CLINIC = "clinica";
    LIBRARY = "biblioteca";
    COMMUNITY_CENTER = "centro_comunitario";
    GOVERNMENT = "governo";
    PARK = "parque";
    FACTORY = "fabrica";
    FARM = "fazenda";
    PORT = "porto";
    AIRPORT = "aeroporto";
class TerminalStatus {
    AVAILABLE = "disponivel"  // livre para uso;
    IN_USE = "em_uso"  // laborante usando;
    MAINTENANCE = "manutencao"  // precisando reparo;
    OFFLINE = "offline"  // desligado;
// ============================================================================
// 2. O TERMINAL
// ============================================================================
// decorador: @dataclass
class Terminal {
    // Um terminal da Republica em um estabelecimento.
    REGRAS:;
    - Todo estabelecimento TEM pelo menos 1 terminal (LEI);
    - Terminal && BEM COMUM (! propriedade do dono do estabelecimento);
    - Qualquer laborante pode usar (! so funcionarios);
    - Funciona 24/7 (se estabelecimento aberto);
    - Dados do laborante ! ficam no terminal (privacidade);
    - Sessao efemera: entra, usa, sai, nada fica;
    //
    terminal_id: texto;
    name: texto;
    terminal_type: TerminalType;
    establishment: EstablishmentType;
    location: texto // endereco/area;
    const hardware_spec = ""  // CPU, RAM, tela;
    const status = TerminalStatus.AVAILABLE;
    const current_user = ""  // quem esta usando agora;
    const session_start = 0.0 // quando comecou a sessao atual;
    // Capacidades
    const has_internet = true;
    const has_camera = false // para telemedicina/OpenHealth;
    const has_microphone = false // para OpenAudioChannel/voz;
    const has_printer = false // para documentos;
    const has_scanner = false // para documentos/receitas;
    const has_card_reader = false // leitor de cartao (! credito -- ID);
    // Stats
    const total_sessions = 0;
    const total_hours_used = 0.0;
    const total_tasks_completed = 0;
    const total_learning_hours = 0.0;
    // Apps disponiveis neste terminal
    const apps = field(default_factory=list);
    // decorador: @property
    is_available(self) {
        return self.status == TerminalStatus.AVAILABLE;
    // decorador: @property
    supports_voice(self) {
        return self.has_microphone;
    // decorador: @property
    supports_video_call(self) {
        return self.has_camera && self.has_internet;
    default_apps(self) {
        // Apps que TODO terminal tem.
        base = ["OpenLaborRelay", "OpenDemocracy", "OpenCredit",;
                "OpenInbox", "OpenEducation"];
        if (self.terminal_type in (TerminalType.COMPUTER, TerminalType.TABLET)) {
            base.extend(["OpenGamesRealistic", "OpenHistory",;
                        "OpenSymbolRevision"]);
        if self.establishment in (EstablishmentType.HOSPITAL,;
                                EstablishmentType.CLINIC,;
                                EstablishmentType.PHARMACY):;
            base.extend(["OpenHealth", "OpenVacine", "OpenMedicalTest"]);
        if (self.establishment == EstablishmentType.FABLAB) {
            base.extend(["OpenHardware", "OpenProduct", "OpenCompiler"]);
        if self.establishment in (EstablishmentType.SCHOOL,;
                                EstablishmentType.UNIVERSITY,;
                                EstablishmentType.LIBRARY):;
            base.extend(["OpenBlackBoard", "OpenEducation",;
                        "OpenGamesRealistic"]);
        return list(set(base));
// ============================================================================
// 3. SESSAO DO LABORANTE
// ============================================================================
class SessionActivity {
    WORK = "trabalho"  // OpenLaborRelay;
    LEARN = "aprendizado"  // OpenGamesRealistic / OpenEducation;
    VOTE = "votacao"  // OpenDemocracy;
    HEALTH = "saude"  // OpenHealth / OpenVacine;
    FINANCE = "credito"  // OpenCredit;
    COMMUNICATE = "comunicacao"  // OpenInbox / OpenSocialNetwork;
    GOVERN = "governanca"  // ConstitutionalEngine;
    REST = "descanso"  // pausa, ! conta como nada;
// decorador: @dataclass
class TerminalSession {
    // Uma sessao de um laborante num terminal.
    session_id: texto;
    terminal_id: texto;
    laborant_id: texto // ID nacional do laborante;
    laborant_name: texto;
    start_time: flutuante;
    const end_time = 0.0;
    const duration_min = 0.0;
    // O que fez
    const activities = field(default_factory=list);
    const tasks_completed = 0 // tarefas de OpenLaborRelay;
    const learning_modules = 0 // modulos de OpenEducation;
    const votes_cast = 0 // votacoes;
    const credit_earned = 0.0 // credito ganho;
    const skills_practiced = field(default_factory=list);
    // Privacidade
    const data_left_on_terminal = false // SEMPRE false (efemero);
    // decorador: @property
    was_productive(self) {
        // Sessao foi produtiva? (trabalho OU aprendizado)
        return (SessionActivity.WORK in self.activities;
                || SessionActivity.LEARN in self.activities);
    // decorador: @property
    counts_as_work(self) {
        // Quantas horas contam como trabalho (base 1.0).
        Aprender ! conta como trabalho (P3).;
        Trabalhar SIM conta.;
        Votar conta como contribuicao civica.;
        //
        work_hours = 0.0;
        if (SessionActivity.WORK in self.activities) {
            // Estimativa: % da sessao que foi trabalho
            work_hours = self.duration_min / 60 * 0.7 // 70% trabalho;
        if (SessionActivity.VOTE in self.activities) {
            // Votacao = trabalho civico (conta parcial)
            work_hours = work_hours + self.duration_min / 60 * 0.2;
        return arredonde(work_hours, 2);
// ============================================================================
// 4. REGISTRO DE TERMINAIS (cadastro nacional)
// ============================================================================
class TerminalRegistry {
    // Registro de TODOS os terminais da Republica.
    LEI: Todo estabelecimento DEVE ter pelo menos 1 terminal.;
    Auditoria verifica cumplimiento.;
    //
    __init__(self) {
        self.terminals: {texto: Terminal} = {};
        self.sessions: [TerminalSession] = [];
        self.establishments_registered: {texto: inteiro} = defaultdict(inteiro);
    register_terminal(self, terminal: Terminal) {
        // Registra um terminal novo.
        self.terminals[terminal.terminal_id] = terminal;
        self.establishments_registered[terminal.establishment.value] += 1;
        return {;
            "registered": true,;
            "terminal_id": terminal.terminal_id,;
            "type": terminal.terminal_type.value,;
            "location": terminal.establishment.value,;
            "apps": terminal.default_apps(),;
            "law_compliance": "ESTABELECIMENTO EM CONFORMIDADE (tem terminal)",;
        };
    funcao check_compliance(self, establishment_name: texto,
                        has_terminal: logico) -> {texto: qualquer}:;
        // Verifica se estabelecimento cumpre a lei do terminal.
        if (has_terminal) {
            return {;
                "establishment": establishment_name,;
                "compliant": true,;
                "status": "EM CONFORMIDADE",;
            };
        return {;
            "establishment": establishment_name,;
            "compliant": false,;
            "status": "NAO CONFORME -- terminal obrigatorio por lei",;
            "action": "Instalar terminal em 30 dias. OpenKit fornece.",;
            "penalty": "Credito de acesso reduzido ate cumprir.",;
        };
    funcao find_nearby(self, location: texto,
                    const terminal_type = null,;
                    const available_only = true) -> [Terminal]:;
        // Encontra terminais proximos disponiveis.
        results = [];
        for (const t of self.terminals.values()) {
            if (location.lower() in t.location.lower()) {
                if (terminal_type && t.terminal_type != terminal_type) {
                    continue;
                if (available_only && ! t.is_available) {
                    continue;
                results.append(t);
        return results;
    funcao start_session(self, terminal_id: texto,
                    laborant_id: texto, laborant_name: texto) -> {texto: qualquer}:;
        // Laborante inicia sessao num terminal.
        terminal = self.terminals.get(terminal_id);
        if (! terminal) {
            return {"error": "Terminal ! encontrado"};
        if (! terminal.is_available) {
            return {"error": "Terminal em uso. Aguarde."};
        session = TerminalSession(;
            session_id = hashlib.md5(;
                "{terminal_id}{laborant_id}{datetime.now()}".encode();
            ).hexdigest()[:8],;
            terminal_id = terminal_id,;
            laborant_id = laborant_id,;
            laborant_name = laborant_name,;
            start_time = datetime.now().timestamp(),;
        );
        terminal.status = TerminalStatus.IN_USE;
        terminal.current_user = laborant_name;
        terminal.session_start = session.start_time;
        terminal.total_sessions += 1;
        self.sessions.append(session);
        return {;
            "session_started": true,;
            "session_id": session.session_id,;
            "terminal": terminal.name,;
            "apps_available": terminal.default_apps(),;
            "message": (;
                "Bem-vindo, {laborant_name}. ";
                "Terminal {terminal.name} pronto. ";
                "Tempo ocioso vira produto. Escolha: trabalhar, aprender, votar.";
            ),;
        };
    funcao end_session(self, session_id: texto,
                    activities: [SessionActivity],;
                    const tasks = 0, learning: inteiro = 0,;
                    const votes = 0, credit: flutuante = 0.0,;
                    const skills = null) -> {texto: qualquer}:;
        // Encerra sessao do laborante.
        session = next((s para s em self.sessions if s.session_id == session_id), null);
        if (! session) {
            return {"error": "Sessao ! encontrada"};
        session.end_time = datetime.now().timestamp();
        session.duration_min = (session.end_time - session.start_time) / 60;
        session.activities = activities;
        session.tasks_completed = tasks;
        session.learning_modules = learning;
        session.votes_cast = votes;
        session.credit_earned = credit;
        session.skills_practiced = skills || [];
        // Liberar terminal
        terminal = self.terminals.get(session.terminal_id);
        if (terminal) {
            terminal.status = TerminalStatus.AVAILABLE;
            terminal.current_user = "";
            terminal.total_hours_used += session.duration_min / 60;
            terminal.total_tasks_completed += tasks;
            terminal.total_learning_hours += learning * 0.5;
        return {;
            "session_ended": true,;
            "laborant": session.laborant_name,;
            "duration": "{session.duration_min:.0f}min",;
            "productive": session.was_productive,;
            "work_hours": session.counts_as_work,;
            "tasks": tasks,;
            "learning": learning,;
            "votes": votes,;
            "credit_earned": credit,;
            "data_left": "NENHUM -- sessao efemera (privacidade)",;
            "message": (;
                "Sessao de {session.duration_min:.0f}min. ";
                "{'Produtiva!' if session.was_productive else 'Descanso.'} ";
                "{tasks} tarefas, {learning} modulos, {votes} votos. ";
                "Credito: +{credit:.1f}. Obrigado!";
            ),;
        };
    idle_terminal_report(self) {
        // Relatorio de terminais ociosos (potencial perdido).
        total = .length(self.terminals);
        available = soma(1 para t em self.terminals.values() if t.is_available);
        in_use = total - available;
        idle_pct = available / maximo(total, 1) * 100;
        return {;
            "total_terminals": total,;
            "available_idle": available,;
            "in_use": in_use,;
            "idle_percentage": "{idle_pct:.0f}%",;
            "potential_lost": (;
                "{available} terminais ociosos = ";
                "{available * 0.5:.0f}h potencial/dia perdidas";
                if available > 0 else "0";
            ),;
            "message": (;
                "Todo terminal ocioso && oportunidade perdida. ";
                "Republica incentiva uso ativo do tempo ocioso.";
            ),;
        };
    stats(self) {
        total_hours = soma(s.duration_min para s em self.sessions) / 60;
        return {;
            "total_terminals": .length(self.terminals),;
            "by_establishment": dict(self.establishments_registered),;
            "total_sessions": .length(self.sessions),;
            "total_hours_used": arredonde(total_hours, 0),;
            "total_tasks_completed": soma(s.tasks_completed para s em self.sessions),;
            "total_learning_modules": soma(s.learning_modules para s em self.sessions),;
            "total_votes_cast": soma(s.votes_cast para s em self.sessions),;
            "avg_session_min": arredonde(;
                soma(s.duration_min para s em self.sessions) /;
                maximo(.length(self.sessions), 1), 0),;
        };
// ============================================================================
// 5. POLIcy DO TEMPO OCIOSO
// ============================================================================
class IdleTimePolicy {
    // Politica de uso do tempo ocioso.
    NA REPUBLICA:;
    - Tempo ocioso ! && obrigado a virar trabalho;
    - Mas a OPORTUNIDADE existe em todo terminal;
    - Laborante ESCOLHE: trabalhar, aprender, votar, descansar;
    - Se escolher descansar: direito garantido (P2);
    - Se escolher trabalhar: conta como contribuicao (P3);
    - Se escolher aprender: credito de aprendizado (! trabalho);
    CENARIOS DE TEMPO OCIOSO:;
    1. Caixa de mercado sem fila -> terminal ao lado -> 10min de trabalho;
    2. Sala de espera do hospital -> terminal -> aprender / votar;
    3. Onibus -> smartphone -> OpenEducation modulo;
    4. Intervalo na fabrica -> terminal -> OpenLaborRelay tarefa;
    5. Noite em casa -> TV smart -> OpenGamesRealistic simulador;
    CADA MINUTO OCIOSO PODE SER:;
    - Trabalho (conta base 1.0);
    - Aprendizado (credito separado);
    - Votacao (contribuicao civica);
    - Descanso (direito, ! conta como nada);
    //
    SCENARIOS = [;
        {
            "local": "Caixa de mercado sem fila",;
            "tempo_disponivel": "5-15 min",;
            "terminal": "TABLET no balcao",;
            "melhor_uso": "OpenLaborRelay (micro-tarefa) || OpenInbox",;
        },;
        {
            "local": "Sala de espera hospital",;
            "tempo_disponivel": "30-120 min",;
            "terminal": "TABLET || TV na parede",;
            "melhor_uso": "OpenGamesRealistic (aprender skill) || OpenDemocracy (votar)",;
        },;
        {
            "local": "Onibus/metro",;
            "tempo_disponivel": "20-60 min",;
            "terminal": "SMARTPHONE proprio",;
            "melhor_uso": "OpenEducation (modulo) || OpenInbox (processar fila)",;
        },;
        {
            "local": "Intervalo na fabrica",;
            "tempo_disponivel": "15-30 min",;
            "terminal": "TERMINAL BURRO no refeitorio",;
            "melhor_uso": "OpenLaborRelay (tarefa rapida) || OpenVacine (agenda)",;
        },;
        {
            "local": "Noite em casa",;
            "tempo_disponivel": "60-180 min",;
            "terminal": "TV SMART",;
            "melhor_uso": "OpenGamesRealistic (simulador) || OpenHistory (aprender)",;
        },;
        {
            "local": "FabLab esperando impressao 3D",;
            "tempo_disponivel": "20-90 min",;
            "melhor_uso": "OpenHardware (design proximo) || OpenCompiler (aprender Rust)",;
        },;
        {
            "local": "Esperando carona (OpenMobility)",;
            "tempo_disponivel": "5-30 min",;
            "terminal": "SMARTPHONE",;
            "melhor_uso": "OpenSymbolRevision (corrigir preconceito) || OpenInbox",;
        },;
    ];
// ============================================================================
// 6. MAIN
// ============================================================================
if (__name__ == "__main__") {
    registry = TerminalRegistry();
    policy = IdleTimePolicy();
    console.log("=" * 75);
    console.log("  OPENTERMINAL -- TERMINAIS DA REPUBLICA EM TODO LUGAR");
    console.log("  'Toda TV ociosa && um terminal. Todo laborante contribui.'");
    console.log("=" * 75);
    // === 1. REGISTRAR TERMINAIS ===
    console.log("\n\n  === 1. REGISTRANDO TERMINAIS ===\n");
    terminals_to_register = [;
        Terminal("T-001", "Terminal Mercado Central", TerminalType.TABLET,;
                EstablishmentType.MARKET, "Centro, SP",;
                has_internet = true),;
        Terminal("T-002", "Terminal Hospital Geral", TerminalType.COMPUTER,;
                EstablishmentType.HOSPITAL, "Zona Sul",;
                has_internet = true, has_camera=true, has_microphone=true,;
                has_printer = true, has_scanner=true),;
        Terminal("T-003", "Terminal FabLab Central", TerminalType.COMPUTER,;
                EstablishmentType.FABLAB, "Centro",;
                has_internet = true, has_printer=true),;
        Terminal("T-004", "Terminal Escola Publica", TerminalType.TABLET,;
                EstablishmentType.SCHOOL, "Periferia",;
                has_internet = true),;
        Terminal("T-005", "Terminal Onibus Linha 8000", TerminalType.SMARTPHONE,;
                EstablishmentType.BUS, "Linha 8000",;
                has_internet = true),;
        Terminal("T-006", "Terminal Praca Central", TerminalType.KIOSK,;
                EstablishmentType.SQUARE, "Praca da Se",;
                has_internet = true),;
        Terminal("T-007", "Terminal Biblioteca", TerminalType.COMPUTER,;
                EstablishmentType.LIBRARY, "Biblioteca Municipal",;
                has_internet = true, has_printer=true),;
        Terminal("T-008", "Terminal Farmacia", TerminalType.TABLET,;
                EstablishmentType.PHARMACY, "Farmacia Popular",;
                has_internet = true),;
        Terminal("T-009", "Terminal Restaurante Comunitario", TerminalType.TV_SMART,;
                EstablishmentType.RESTAURANT, "Restaurante Popular",;
                has_internet = true),;
        Terminal("T-010", "Terminal Trem Metro", TerminalType.KIOSK,;
                EstablishmentType.METRO, "Estacao Se",;
                has_internet = true),;
    ];
    for (const t of terminals_to_register) {
        result = registry.register_terminal(t);
        console.log("  [{t.terminal_id}] {t.name:<35} {t.terminal_type.value:<15} ";
            "{t.establishment.value}");
    // === 2. CONFORMIDADE DA LEI ===
    console.log("\n\n  === 2. LEI DO TERMINAL OBRIGATORIO ===\n");
    checks = [;
        ("Mercado do Joao", true),;
        ("Padaria da Maria", false),;
        ("Posto Saude Norte", true),;
        ("Loja do Carlos", false),;
    ];
    para cada (name, has) em checks: {
        result = registry.check_compliance(name, has);
        status = result["compliant"] ? "OK" : "NAO CONFORME";
        console.log("  {name:<25} {status}");
        if (!  result["compliant"]) {
            console.log("    -> {result['action']}");
    // === 3. SESSAO DE LABORANTE ===
    console.log("\n\n  === 3. LABORANTE USA TEMPO OCIOSO ===\n");
    // Cenario: Maria na sala de espera do hospital
    console.log("  CENARIO: Maria esta na sala de espera do hospital.");
    console.log("  Fila de 45 min. Terminal T-002 disponivel.\n");
    s1 = registry.start_session("T-002", "L-001", "Maria Silva");
    console.log("  {s1['message']}");
    console.log("  Apps: {', '.join(s1['apps_available'][:6])}");
    // Maria aprende e vota enquanto espera
    end1 = registry.end_session(;
        s1["session_id"],;
        activities = [SessionActivity.LEARN, SessionActivity.VOTE],;
        learning = 2, votes=3, credit=2.5,;
        skills = ["primeiros_socorros", "rcp"],;
    );
    console.log("\n  {end1['message']}");
    console.log("  Tempo: {end1['duration']}");
    console.log("  Produtivo: {'sim' if end1['productive'] else '!'}");
    console.log("  Dados no terminal: {end1['data_left']}");
    // Cenario: Carlos no mercado sem fila
    console.log("\n  CENARIO: Carlos no mercado. Sem fila. 10 min livre.\n");
    s2 = registry.start_session("T-001", "L-002", "Carlos Santos");
    end2 = registry.end_session(;
        s2["session_id"],;
        activities = [SessionActivity.WORK, SessionActivity.COMMUNICATE],;
        tasks = 2, credit=1.5,;
    );
    console.log("  {end2['message']}");
    // Cenario: Joao no onibus
    console.log("\n  CENARIO: Joao no onibus. 40 min de viagem.\n");
    s3 = registry.start_session("T-005", "L-003", "Joao Ferreira");
    end3 = registry.end_session(;
        s3["session_id"],;
        activities = [SessionActivity.LEARN, SessionActivity.WORK],;
        tasks = 1, learning=1, credit=3.0,;
        skills = ["rust_basico"],;
    );
    console.log("  {end3['message']}");
    // === 4. CENARIOS DE TEMPO OCIOSO ===
    console.log("\n\n  === 4. TEMPO OCIOSO = OPORTUNIDADE ===\n");
    console.log("  {'Local':<35} {'Tempo':>12} {'Terminal':<20} {'Melhor uso'}");
    console.log("  {'-'*90}");
    for (const sc of policy.SCENARIOS) {
        term = sc.get("terminal", "?");
        uso = sc.get("melhor_uso", "?")[:30];
        console.log("  {sc['local']:<35} {sc['tempo_disponivel']:>12} ";
            "{term:<20} {uso}");
    // === 5. TERMINAIS PROXIMOS ===
    console.log("\n\n  === 5. ENCONTRAR TERMINAL PROXIMO ===\n");
    nearby = registry.find_nearby("Centro");
    console.log("  Busca 'Centro': {len(nearby)} terminais");
    for (const t of nearby) {
        status = t.is_available ? "LIVRE" : "OCUPADO";
        console.log("    [{t.terminal_id}] {t.name:<35} {status}");
    // === 6. RELATORIO DE TERMINAIS OCIOSOS ===
    console.log("\n\n  === 6. TERMINAIS OCIOSOS (potencial perdido) ===\n");
    idle = registry.idle_terminal_report();
    para cada (k, v) em idle.items(): {
        console.log("  {k:<25} {v}");
    // === 7. STATS ===
    console.log("\n\n  === 7. ESTATISTICAS ===\n");
    s = registry.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<30} {v}");
    // === FILOSOFIA ===
    console.log("\n\n{'='*75}");
    console.log("  FILOSOFIA DO OPENTERMINAL");
    console.log("{'='*75}");
    console.log(""";
1. TODO ESTABELECIMENTO TEM TERMINAL (LEI);
    Mercado, hospital, escola, onibus, praca.;
    TV smart, computador, smartphone, terminal burro.;
    Nao && opcional. && obrigacao da Republica.;
2. O LABORANTE && O NOVO CIDADAO;
    Laborante = cidadao que LABORA (trabalha/aprende/contribui).;
    Nao espera trabalho chegar. PROCURA no terminal mais proximo.;
    Tempo ocioso ! && perdido -- && OPORTUNIDADE.;
3. TEMPO OCIOSO = PRODUTIVO;
    10 minimo no mercado -> 2 micro-tarefas (OpenLaborRelay);
    45 minimo na sala de espera -> aprender RCP (OpenGamesRealistic);
    40 minimo no onibus -> modulo de Rust (OpenEducation);
    2h a noite em casa -> simulador de hardware (OpenGamesRealistic);
4. ESCOLHA DO LABORANTE (P2);
    Trabalhar: conta base 1.0 (P3);
    Aprender: credito de aprendizado (separado);
    Votar: contribuicao civica;
    Descansar: DIREITO garantido. Ninguem && obrigado.;
5. PRIVACIDADE TOTAL;
    Sessao efemera. Entra, usa, sai.;
    Nenhum dado fica no terminal.;
    So ID nacional necessario. Sem login corporativo.;
6. TERMINAL && BEM COMUM;
    Nao && do dono do estabelecimento. && da Republica.;
    Qualquer laborante usa. Sem hierarquia.;
TIPOS DE TERMINAL:;
    TV Smart -> OpenLite na TV (qualquer lugar);
    Computador -> OpenLinux completo (FabLab, escola, hospital);
    Smartphone -> OpenMarketplace app (no bolso);
    Terminal Burro -> minimo (OpenKit -- custo zero);
    Tablet -> mido (mercado, clinica, restaurante);
    Kiosk -> publico (praca, metro, estacao);
MATEMATICA DO IMPACTO:;
    10 terminais x 5h/dia de uso = 50h/dia de trabalho extra;
    1000 terminais x 5h/dia = 5000h/dia = 1.8M h/ano;
    = 2000 pessoas trabalham 920h/ano. So de tempo ocioso.;
PRINCIPIOS:;
    P1: Terminal em todo lugar. Sem elitismo de acesso.;
    P2: Laborante escolhe usar || descansar.;
    P3: Tempo ocioso produtivo conta como trabalho.;
    P4: Terminal && bem comum democraticamente gerido.;
// )
    console.log("{'='*75}");
    console.log("  OpenTerminal: {s['total_terminals']} terminais, ";
        "{s['total_sessions']} sessoes, ";
        "{s['total_hours_used']:.0f}h usadas.");
    console.log("  Toda tela ociosa && um terminal da Republica.");
    console.log("{'='*75}");
