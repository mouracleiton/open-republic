// ConstituentAssembly -- A Voz do Povo Sobre a Lei Matematica -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
ConstituentAssembly -- A Voz do Povo Sobre a Lei Matematica;
=============================================================;
"O fundador propoe. O povo dispoe.;
12 das 13 propostas do fundador foram REJEITADAS.;
Isso ! && falha. && DEMOCRACIA funcionando.";
A Assembleia Constituinte && o ORGAO MAXO da Republica.;
Acima do fundador. Acima do motor constitucional. Acima de tudo.;
Ela vota sobre:;
1. Parametros economicos (horas, credito, excedente);
2. Principios constitucionais (P1-P4);
3. Qualquer mudanca fundamental;
O fundador PROPOE. A Assembleia DECIDE.;
Modelo de votacao:;
- Simulacao com N cidadaos (representando setores da Republica);
- Cada cidadao tem 1 voto;
- Quorum: 50% + 1 para aprovacao;
- Para emendas constitucionais: 60%;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa math
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// ============================================================================
// 1. CIDADAOS DA ASSEMBLEIA (representantes dos setores)
// ============================================================================
#[derive(Debug, Clone, PartialEq)]
enum Sector {
    // Setores da Republica que enviam representantes.
    ENGINEERING = "engenharia";
    EDUCATION = "educacao";
    HEALTH = "saude";
    AGRICULTURE = "agricultura";
    TRANSPORT = "transporte";
    CULTURE = "cultura";
    ECONOMY = "economia";
    SOCIETY = "sociedade";
    INFRASTRUCTURE = "infraestrutura";
    TECHNOLOGY = "tecnologia";
    CORE = "nucleo_republica";
    COMMUNITY = "comunidades_reais";
// decorador: @dataclass
#[derive(Debug, Clone)]
struct Citizen {
    // Um cidadao da Assembleia Constituinte.
    citizen_id: texto;
    name: texto;
    sector: Sector;
    age: inteiro;
    background: texto // quem && na vida real;
    // Tendencias de voto (0-1)
    let pragmatism: f64 = 0.5 // quao pragmatico vs idealista;
    let risk_tolerance: f64 = 0.5 // tolerancia a risco;
    let equity_focus: f64 = 0.5 // foco em igualdade vs meritocracia;
    let autonomy_focus: f64 = 0.5 // foco em autonomia individual;
    funcao vote(self, proposal: 'AssemblyProposal',
            rng: random.Random) -> 'Vote':;
        // Decide como votar numa proposta.
        // Calcula alinhamento da proposta com as tendencias do cidadao
        alignment = 0.0;
        para cada (stance, weight) em proposal.stances.items(): {
            trait_value = getattr(self, stance, 0.5);
            alignment = alignment + trait_value * weight;
        // Ruido (pessoas nao sao deterministicas)
        noise = rng.uniform(-0.15, 0.15);
        score = alignment + noise;
        if score > 0.55 {
            choice = VoteChoice.YES;
            reasoning = "Alinhado com meus valores && setor.";
        } else if score < 0.35 {
            choice = VoteChoice.NO;
            reasoning = "Conflita com meus valores || setor.";
        } else {
            choice = VoteChoice.ABSTAIN;
            reasoning = "Preciso de mais informacao || sou ambivalente.";
        return Vote(;
            citizen_id = self.citizen_id,;
            citizen_name = self.name,;
            sector = self.sector,;
            proposal_id = proposal.proposal_id,;
            choice = choice,;
            reasoning = reasoning,;
        );
// ============================================================================
// 2. PROPOSTAS E VOTOS
// ============================================================================
#[derive(Debug, Clone, PartialEq)]
enum VoteChoice {
    YES = "sim";
    NO = "!";
    ABSTAIN = "abstencao";
// decorador: @dataclass
#[derive(Debug, Clone)]
struct Vote {
    citizen_id: texto;
    citizen_name: texto;
    sector: Sector;
    proposal_id: texto;
    choice: VoteChoice;
    reasoning: texto;
// decorador: @dataclass
#[derive(Debug, Clone)]
struct AssemblyProposal {
    // Uma proposta submetida a votacao da Assembleia.
    proposal_id: texto;
    title: texto;
    description: texto;
    proposer: texto // quem propoe;
    proposed_value: qualquer // valor proposto;
    // Stances: qual traco de cidadao favorece esta proposta
    // (traco, peso) -> soma ponderada determina alinhamento
    let stances: {texto: flutuante} = field(default_factory=dict);
    // Parametros da votacao
    let quorum_pct: f64 = 0.50 // 50% + 1 para aprovar;
    let constitutional: bool = false // se true, quorum = 60%;
    // Resultado
    let votes: [Vote] = field(default_factory=list);
    result: 'VoteResult'? = NULL;
    fn cast_votes(self, citizens: [Citizen], rng: random.Random) {
        // Todos os cidadaos votam.
        self.votes = [c.vote(self, rng) para c em citizens];
    // decorador: @property
    fn yes_count(self) -> i64 {
        return soma(1 para v em self.votes if v.choice == VoteChoice.YES);
    // decorador: @property
    fn no_count(self) -> i64 {
        return soma(1 para v em self.votes if v.choice == VoteChoice.NO);
    // decorador: @property
    fn abstain_count(self) -> i64 {
        return soma(1 para v em self.votes if v.choice == VoteChoice.ABSTAIN);
    // decorador: @property
    fn total_votes(self) -> i64 {
        return tamanho(self.votes);
    // decorador: @property
    fn decided_votes(self) -> i64 {
        return self.yes_count + self.no_count;
    // decorador: @property
    fn approved(self) -> bool {
        if self.decided_votes == 0 {
            return false;
        threshold = self.constitutional ? 0.60 : 0.50;
        return (self.yes_count / self.decided_votes) >= threshold;
    // decorador: @property
    fn yes_pct(self) -> f64 {
        self.decided_votes ? retorne self.yes_count / self.decided_votes * 100 : 0;
    // decorador: @property
    fn margin(self) -> String {
        diff = self.yes_count - self.no_count;
        if diff > 0 {
            return "+{diff}";
        } else if diff < 0 {
            return "{diff}";
        return "EMPATE";
// decorador: @dataclass
#[derive(Debug, Clone)]
struct VoteResult {
    proposal_id: texto;
    title: texto;
    approved: logico;
    yes: inteiro;
    no: inteiro;
    abstain: inteiro;
    total: inteiro;
    margin: texto;
    let by_sector: Dict[texto, {texto: inteiro}] = field(default_factory=dict);
    let note: String = "";
// ============================================================================
// 3. A ASSEMBLEIA
// ============================================================================
#[derive(Debug, Clone)]
struct ConstituentAssembly {
    // A Assembleia Constituinte da OpenRepublic.
    ORGAO MAXO. Acima do fundador. Acima de tudo.;
    //
    fn __init__(self, seed: inteiro = 42) {
        self.rng = random.Random(seed);
        self.citizens: [Citizen] = [];
        self.proposals: [AssemblyProposal] = [];
        self.results: [VoteResult] = [];
        self._populate_citizens();
    fn _populate_citizens(self) {
        // Cria os representantes de cada setor da Republica.
        Cada setor envia cidadaos com tendencias diferentes.;
        Sao ficticios mas representam arquetipos reais:;
        - engenheiro pragmatico;
        - professora idealista;
        - lider comunitario focado em igualdade;
        - medico focado em autonomia;
        - agricultor tradicional;
        - jovem tecnico;
        - idoso sabio;
        - etc.;
        //
        archetypes = [;
            // (nome, setor, idade, background, pragmatismo, risco, igualdade, autonomia)
            ("Ana (engenheira)", Sector.ENGINEERING, 32, "Data Engineer, ex-FAANG",;
            0.8, 0.7, 0.4, 0.6),;
            ("Bruno (programador)", Sector.TECHNOLOGY, 28, "Full-stack, Rust evangelista",;
            0.7, 0.8, 0.3, 0.7),;
            ("Carla (professora)", Sector.EDUCATION, 45, "Professora rede publica 20 anos",;
            0.3, 0.4, 0.9, 0.5),;
            ("Diego (medico)", Sector.HEALTH, 38, "Medico familia, SUS",;
            0.6, 0.3, 0.7, 0.8),;
            ("Eva (agricultora)", Sector.AGRICULTURE, 52, "Agricultura familiar, assentamento",;
            0.2, 0.2, 0.8, 0.4),;
            ("Felipe (pedreiro)", Sector.INFRASTRUCTURE, 41, "Pedreiro, sindicalista",;
            0.4, 0.3, 0.8, 0.6),;
            ("Gabriela (juza)", Sector.SOCIETY, 50, "Juiza, ativista direitos humanos",;
            0.5, 0.5, 0.7, 0.9),;
            ("Haroldo (idoso)", Sector.CORE, 68, "Aposentado, lider comunitario",;
            0.3, 0.2, 0.7, 0.5),;
            ("Iara (quilombola)", Sector.COMMUNITY, 35, "Lider quilombo, Banco Palmas",;
            0.2, 0.4, 0.9, 0.6),;
            ("Joao (jovem dev)", Sector.TECHNOLOGY, 22, "Estagiario, idealista",;
            0.3, 0.9, 0.7, 0.6),;
            ("Karla (enfermeira)", Sector.HEALTH, 33, "Enfermeira, maesolo",;
            0.5, 0.3, 0.8, 0.7),;
            ("Leandro (artista)", Sector.CULTURE, 29, "Musico, ativista cultural",;
            0.2, 0.6, 0.8, 0.7),;
            ("Marcia (economista)", Sector.ECONOMY, 40, "Economista heterodoxa",;
            0.7, 0.5, 0.7, 0.4),;
            ("Nelson (transporte)", Sector.TRANSPORT, 44, "Motorista aplicativo, coop",;
            0.6, 0.4, 0.7, 0.6),;
            ("Olivia (crianca)", Sector.SOCIETY, 12, "Representante infanto-juvenil",;
            0.1, 0.7, 0.9, 0.8),;
            ("Paulo (pescador)", Sector.COMMUNITY, 47, "Pescador artesanal, ribeirinho",;
            0.2, 0.3, 0.7, 0.5),;
            ("Rosa (indigena)", Sector.COMMUNITY, 30, "Lider aldeia, APIB",;
            0.1, 0.3, 0.9, 0.6),;
            ("Sergio (cientista)", Sector.CORE, 55, "Pesquisador, PhD",;
            0.8, 0.6, 0.5, 0.5),;
            ("Tania (advogada)", Sector.SOCIETY, 36, "Advogada popular",;
            0.5, 0.4, 0.8, 0.8),;
            ("Ulisses (favela)", Sector.COMMUNITY, 26, "Lider favela, coletivo",;
            0.4, 0.6, 0.9, 0.6),;
        ];
        para i, (name, sector, age, bg, prag, risk, equity, autonomy) in enumere(archetypes): {
            self.citizens.append(Citizen(;
                citizen_id = "C-{i+1:03d}",;
                name = name,;
                sector = sector,;
                age = age,;
                background = bg,;
                pragmatism = prag,;
                risk_tolerance = risk,;
                equity_focus = equity,;
                autonomy_focus = autonomy,;
            ));
    fn submit_proposal(self, proposal: AssemblyProposal) {
        // Submete proposta para votacao.
        if proposal.constitutional {
            proposal.quorum_pct = 0.60;
        self.proposals.append(proposal);
    fn run_election(self) -> {texto: qualquer} {
        // Executa a votacao em TODAS as propostas. Retorna constituicao aprovada.
        constitution = {};
        for prop in self.proposals {
            prop.cast_votes(self.citizens, self.rng);
            // Analise por setor
            let by_sector: Dict[texto, {texto: inteiro}] = {};
            for v in prop.votes {
                sname = v.sector.value;
                if sname ! in by_sector {
                    by_sector[sname] = {"sim": 0, "!": 0, "abstencao": 0};
                by_sector[sname][v.choice.value] += 1;
            result = VoteResult(;
                proposal_id = prop.proposal_id,;
                title = prop.title,;
                approved = prop.approved,;
                yes = prop.yes_count,;
                no = prop.no_count,;
                abstain = prop.abstain_count,;
                total = prop.total_votes,;
                margin = prop.margin,;
                by_sector = by_sector,;
                note = prop.approved ? "APROVADO" : "REJEITADO",;
            );
            self.results.append(result);
            if prop.approved {
                constitution[prop.title] = {
                    "value": prop.proposed_value,;
                    "yes_pct": prop.yes_pct,;
                    "margin": prop.margin,;
                    "votes": "{prop.yes_count}-{prop.no_count}",;
                };
        return constitution;
    fn print_results(self) -> String {
        // Relatorio completo da votacao.
        lines = [];
        lines.append("=" * 100);
        lines.append("ASSEMBLEIA CONSTITUINTE DA OPENREPUBLIC");
        lines.append("O Povo Decide. O Fundador Propoe.");
        lines.append("=" * 100);
        lines.append("Representantes: {len(self.citizens)}");
        lines.append("Propostas: {len(self.proposals)}");
        lines.append("");
        // Lista de cidadaos
        lines.append("-" * 100);
        lines.append("REPRESENTANTES NA ASSEMBLEIA:");
        lines.append("-" * 100);
        for c in self.citizens {
            lines.append("  {c.citizen_id} {c.name:<28} [{c.sector.value:<18}] {c.background}");
        lines.append("");
        // Resultado de cada proposta
        lines.append("-" * 100);
        lines.append("VOTACAO:");
        lines.append("-" * 100);
        approved_count = 0;
        rejected_count = 0;
        para cada (i, result) em enumere(self.results, 1): {
            status = result.approved ? "APROVADA" : "REJEITADA";
            pct = (result.yes + result.no) ? result.yes / (result.yes + result.no) * 100 : 0;
            quorum = self.proposals[i-1].constitutional ? "60%" : "50%";
            lines.append("");
            lines.append("  PROPOSTA {i}: {result.title}");
            lines.append("  STATUS: {status} ({result.yes} sim, {result.no} !, {result.abstain} abstencao)");
            lines.append("  MARGEM: {result.margin} | Quorum: {quorum}");
            // Breakdown por setor
            lines.append("  POR SETOR:");
            para cada (sector_name, counts) em result.by_sector.items(): {
                s = counts["sim"];
                n = counts["!"];
                a = counts["abstencao"];
                total = s + n + a;
                if total > 0 {
                    lines.append("    {sector_name:<20} sim={s} !={n} abst={a}");
            if result.approved {
                approved_count = approved_count + 1;
            } else {
                rejected_count = rejected_count + 1;
        lines.append("");
        lines.append("-" * 100);
        lines.append("RESULTADO GERAL: {approved_count} aprovadas, {rejected_count} rejeitadas");
        lines.append("Taxa de aprovacao: {approved_count/len(self.results)*100:.0f}%");
        lines.append("");
        // A mensagem filosofica
        lines.append("=" * 100);
        lines.append("MENSAGEM DA ASSEMBLEIA:");
        lines.append("");
        if rejected_count > approved_count {
            lines.append("  O fundador propoe. O povo dispoe.");
            lines.append("  {rejected_count} de {len(self.results)} propostas foram REJEITADAS.");
            lines.append("  Isso NAO && fracasso. E DEMOCRACIA.");
            lines.append("  O povo sabe o que quer. O fundador aprende.");
        } else {
            lines.append("  {approved_count} de {len(self.results)} propostas APROVADAS.");
            lines.append("  O fundador ouviu o povo && o povo concordou.");
        lines.append("");
        lines.append("  Nenhum decreto. Nenhuma imposicao.");
        lines.append("  A constituicao pertence a quem vive nela.");
        lines.append("=" * 100);
        return "\n".join(lines);
// ============================================================================
// 4. SESSAO: FINANCIAMENTO DA REPUBLICA
// ============================================================================
fn session_financing() -> ConstituentAssembly {
    // Sessao da Assembleia sobre a PERGUNTA CRITICA:
    'Como financiar a Republica && seus cidadaos durante a transicao?';
    O fundador (Cleiton) PROPOE. A Assembleia DECIDE.;
    //
    assembly = ConstituentAssembly(seed=42);
    // === PROPOSTA 1: Aceitar vaga FAANG (Google/Airbnb/Amazon) ===
    assembly.submit_proposal(AssemblyProposal(;
        proposal_id = "FIN-001",;
        title = "Aceitar vaga FAANG para financiar a Republica",;
        description = (;
            "O fundador aceita oferta de $600-800k/ano na Google/Airbnb/Amazon. ";
            "40h/semana para a empresa. 10h/semana + parte do salario para OpenRepublic. ";
            "A Republica && financiada pelo salario do fundador durante a transicao.";
        ),;
        proposer = "cleiton (fundador)",;
        proposed_value = "aceitar_faang",;
        stances = {
            "pragmatism": 0.7,;
            "risk_tolerance": 0.3,;
            "equity_focus": -0.3,;
            "autonomy_focus": 0.2,;
        },;
    ));
    // === PROPOSTA 2: Republica se autofinancia (TEIA/consultoria/credito) ===
    assembly.submit_proposal(AssemblyProposal(;
        proposal_id = "FIN-002",;
        title = "Republica se autofinancia (produtos + consultoria + credito)",;
        description = (;
            "Sem FAANG. A Republica gera propria receita: ";
            "TEIA como produto pago para governos/ONGs, ";
            "consultoria tecnica para cooperativas, ";
            "OpenCredit como cooperativa financeira. ";
            "Renda instavel no inicio mas independente.";
        ),;
        proposer = "cleiton (fundador)",;
        proposed_value = "autofinanciamento",;
        stances = {
            "pragmatism": 0.3,;
            "risk_tolerance": 0.8,;
            "equity_focus": 0.5,;
            "autonomy_focus": 0.8,;
        },;
    ));
    // === PROPOSTA 3: Hibrido (part-time FAANG + Republica) ===
    assembly.submit_proposal(AssemblyProposal(;
        proposal_id = "FIN-003",;
        title = "Hibrido: consultoria part-time + Republica",;
        description = (;
            "Contrato part-time || consultoria ($300-400k/ano). ";
            "20h/semana mercado, 20h/semana Republica. ";
            "Base financeira garantida + impacto mantido. ";
            "Nem full FAANG, nem sem renda.";
        ),;
        proposer = "cleiton (fundador)",;
        proposed_value = "hibrido",;
        stances = {
            "pragmatism": 0.6,;
            "risk_tolerance": 0.5,;
            "equity_focus": 0.3,;
            "autonomy_focus": 0.5,;
        },;
    ));
    // === PROPOSTA 4: Cooperativa de engenharia (modelo Republica) ===
    assembly.submit_proposal(AssemblyProposal(;
        proposal_id = "FIN-004",;
        title = "Cooperativa de engenharia open-source (sem dono, sem excedente)",;
        description = (;
            "Fundar cooperativa que vende servicos de engenharia de dados/software. ";
            "Sem dono. 5% excedente vai para pool da Republica. ";
            "95% fica com quem trabalha. ";
            "Cliente paga em R$ mas estrutura interna && da Republica. ";
            "Modelo Banco Palmas aplicado a software.";
        ),;
        proposer = "cleiton (fundador)",;
        proposed_value = "cooperativa",;
        stances = {
            "pragmatism": 0.5,;
            "risk_tolerance": 0.6,;
            "equity_focus": 0.9,;
            "autonomy_focus": 0.6,;
        },;
    ));
    // === PROPOSTA 5: Piloto em comunidade (modelo Palmas) ===
    assembly.submit_proposal(AssemblyProposal(;
        proposal_id = "FIN-005",;
        title = "Piloto real em comunidade isolada (Banco Palmas modelo)",;
        description = (;
            "Nao buscar FAANG nem autofinanciamento abstrato. ";
            "Ir para UMA comunidade real (quilombo/assentamento/favela). ";
            "Implementar OpenCredit + OpenProduction la. ";
            "Provar que funciona. Documentar. Replicar. ";
            "Modelo Palmas: 26 anos de sucesso comecou com 1 comunidade.";
        ),;
        proposer = "cleiton (fundador)",;
        proposed_value = "piloto_comunitario",;
        stances = {
            "pragmatism": 0.4,;
            "risk_tolerance": 0.5,;
            "equity_focus": 0.8,;
            "autonomy_focus": 0.7,;
        },;
    ));
    return assembly;
// ============================================================================
// 5. EXECUCAO
// ============================================================================
if __name__ == "__main__" {
    assembly = session_financing();
    constitution = assembly.run_election();
    println!(assembly.print_results());
    println!();
    println!("=" * 100);
    println!("DECISOES APROVADAS PELA ASSEMBLEIA:");
    println!("=" * 100);
    if constitution {
        para cada (title, details) em constitution.items(): {
            println!("  >> {title}");
            println!("     Valor: {details['value']}");
            println!("     Votos: {details['votes']} ({details['yes_pct']:.0f}% sim)");
            println!();
    } else {
        println!("  Nenhuma proposta aprovada. O povo rejeitou tudo.");
        println!("  O fundador precisa ouvir && reformular.");
    println!("=" * 100);
