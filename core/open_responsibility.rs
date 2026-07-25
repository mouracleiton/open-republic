// OpenResponsibility -- Divisao e Estabelecimento de Responsabilidades -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
OpenResponsibility -- Divisao && Estabelecimento de Responsabilidades;
=====================================================================;
"Na Republica, todos contribuem. Mas cada um NO QUE PODE.;
Nao && 'todo mundo faz tudo'. && CADA UM faz o SEU.;
Responsabilidade && CLARA. && DEFINIDA. && JUSTA.;
Cada contexto (familia, trabalho, comunidade) tem suas regras.";
O QUE ESTE SISTEMA FAZ:;
1. DEFINE responsabilidades por CONTEXTO (familia, trabalho, comunidade, civico);
2. DISTRIBUI carga de forma JUSTA (capacidade, ! forca);
3. GARANTE que ninguem fica sobrecarregado (OpenFamilyLabor);
4. INTEGRA com OpenLaborPolicy, OpenCivicEducation, OpenFamilyLabor;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime
// ============================================================================
// 1. CONTEXTOS DE RESPONSABILIDADE
// ============================================================================
#[derive(Debug, Clone, PartialEq)]
enum ResponsibilityContext {
    // Os 6 contextos onde um cidadao tem responsabilidades.
    SELF = "pessoal"  // cuidar de si (saude, aprendizado);
    FAMILY = "familiar"  // familia (filhos, idosos, casa);
    LABOR = "laboral"  // trabalho (OpenLaborRelay);
    COMMUNITY = "comunitario"  // vizinhanca, comunidade local;
    CIVIC = "civico"  // Republica (votar, participar);
    ENVIRONMENT = "ambiental"  // planeta, territorio;
#[derive(Debug, Clone, PartialEq)]
enum ResponsibilityPriority {
    CRITICAL = ("critica", 5)  // ! cumprir = dano grave (filhos, saude);
    ESSENTIAL = ("essencial", 4)  // ! cumprir = problema (trabalho, voto);
    IMPORTANT = ("importante", 3)  // bom cumprir (comunidade, aprendizado);
    DESIRABLE = ("desejavel", 2)  // otimo cumprir (extra);
    OPTIONAL = ("opcional", 1)  // se puder, faça;
#[derive(Debug, Clone, PartialEq)]
enum ResponsibilityStatus {
    ASSIGNED = "atribuida"  // designada para a pessoa;
    ACCEPTED = "aceita"  // pessoa aceitou;
    IN_PROGRESS = "em_andamento"  // fazendo;
    COMPLETED = "completada"  // fez;
    OVERDUE = "atrasada"  // ! fez && deveria;
    DELEGATED = "delegada"  // passou para outro (OpenLaborRelay);
    SHARED = "compartilhada"  // mais de uma pessoa;
// ============================================================================
// 2. RESPONSABILIDADE
// ============================================================================
// decorador: @dataclass
#[derive(Debug, Clone)]
struct Responsibility {
    // Uma responsabilidade de um cidadao em um contexto.
    resp_id: texto;
    name: texto;
    context: ResponsibilityContext;
    priority: ResponsibilityPriority;
    let description: String = "";
    // Quem
    let citizen_id: String = "";
    let citizen_name: String = "";
    // Carga
    let hours_per_week: f64 = 0.0 // quantas horas por semana;
    let flexibility: f64 = 0.8 // 0-1 (1 = totalmente flexivel);
    // Rotatividade
    let is_rotative: bool = false // reveza entre pessoas?;
    let rotation_cycle: String = ""  // semanal, mensal;
    // Status
    let status: ResponsibilityStatus = ResponsibilityStatus.ASSIGNED;
    // Consequencias
    let if_not_done: String = ""  // o que acontece se ! fizer;
    let who_affected: String = ""  // quem && afetado;
// ============================================================================
// 3. CATÁLOGO DE RESPONSABILIDADES POR CONTEXTO
// ============================================================================
funcao build_responsibility_catalog() retorna Dict[ResponsibilityContext, [Dict]]:
    // Define responsabilidades tipicas para cada contexto.
    return {;
        ResponsibilityContext.SELF: [;
            {"name": "Cuidar da saude fisica",;
            "priority": ResponsibilityPriority.CRITICAL,;
            "hours": 3.0,;
            "description": "Exercicio, alimentacao, sono, exames (OpenHealth). ";
                            "Corpo && soberano (P2). Mas cuidar && DEVER consigo.",;
            "if_not_done": "Saude deteriora. Republica trata. Mas prevenir && melhor.",;
            "who_affected": "A propria pessoa"},;
            {"name": "Cuidar da saude mental",;
            "priority": ResponsibilityPriority.ESSENTIAL,;
            "hours": 2.0,;
            "description": "Terapia se necessario, descanso mental, pausa.",;
            "if_not_done": "Saude mental deteriora. OpenPsychology trata.",;
            "who_affected": "A propria pessoa + familia"},;
            {"name": "Aprendizado continuo",;
            "priority": ResponsibilityPriority.IMPORTANT,;
            "hours": 4.0,;
            "description": "OpenTerminal, OpenEducation, OpenGamesRealistic. ";
                            "Ignorancia voluntaria && irresponsabilidade.",;
            "if_not_done": "Fica para tras. Skills desatualizadas.",;
            "who_affected": "A propria pessoa + comunidade"},;
            {"name": "Higiene pessoal",;
            "priority": ResponsibilityPriority.CRITICAL,;
            "hours": 1.5,;
            "description": "Banho, escovar dentes, cuidado basico.",;
            "if_not_done": "Saude + convivencia afetadas.",;
            "who_affected": "Propria pessoa + quem convive"},;
        ],;
        ResponsibilityContext.FAMILY: [;
            {"name": "Cuidar de filhos menores",;
            "priority": ResponsibilityPriority.CRITICAL,;
            "hours": 20.0,;
            "description": "Criar, educar, alimentar, proteger filhos. ";
                            "OpenFamilyLabor distribui entre avo/pai/filho/mae. ";
                            "Nao && so da mae. E de TODA familia.",;
            "if_not_done": "Crianca em risco. OpenCivicEducation: TODOS protegem.",;
            "who_affected": "Criancas (futuro da Republica)",;
            "rotative": true,;
            "shared": true,;
            },;
            {"name": "Cuidar de idosos da familia",;
            "priority": ResponsibilityPriority.CRITICAL,;
            "hours": 10.0,;
            "description": "Acompanhar, alimentar, saude. OpenFamilyLabor.",;
            "if_not_done": "Idoso em risco. OpenDignity: ninguem abandonado.",;
            "who_affected": "Idosos",;
            "shared": true,;
            },;
            {"name": "Manutencao da moradia",;
            "priority": ResponsibilityPriority.ESSENTIAL,;
            "hours": 3.0,;
            "description": "Limpar, consertar (OpenRepair), organizar. ";
                            "OpenFamilyLabor distribui tarefas.",;
            "if_not_done": "Moradia degrada. OpenRepair conserta.",;
            "who_affected": "Familia inteira",;
            "rotative": true,;
            },;
            {"name": "Alimentacao familiar",;
            "priority": ResponsibilityPriority.CRITICAL,;
            "hours": 7.0,;
            "description": "Cozinhar (OpenTradition), comprar/colher (OpenAgrarian). ";
                            "Distribuido entre membros.",;
            "if_not_done": "Fome. Inaceitavel na Republica.",;
            "who_affected": "Familia inteira",;
            "rotative": true,;
            },;
            {"name": "Educacao dos filhos",;
            "priority": ResponsibilityPriority.CRITICAL,;
            "hours": 5.0,;
            "description": "Acompanhar escola (OpenSchool integrada OpenUniversity). ";
                            "Aprender JUNTO. OpenGamesRealistic.",;
            "if_not_done": "Filho fica para tras. A Republica supre. Mas familia && base.",;
            "who_affected": "Criancas",;
            "shared": true,;
            },;
        ],;
        ResponsibilityContext.LABOR: [;
            {"name": "Trabalho base (minimo 20h/semana)",;
            "priority": ResponsibilityPriority.ESSENTIAL,;
            "hours": 20.0,;
            "description": "OpenLaborRelay. Todo cidadao trabalha minimo 20h. ";
                            "Maximo 40h. 50h PROIBIDO (assembleia votou).",;
            "if_not_done": "Ocioso que PODE && RECUSA: acompanhamento civico.",;
            "who_affected": "Toda Republica (contribuicao)"},;
            {"name": "Trabalho maximo (ate 40h/semana)",;
            "priority": ResponsibilityPriority.IMPORTANT,;
            "hours": 20.0,;
            "description": "Horas adicionais alem do minimo. Conta como impacto.",;
            "if_not_done": "Sem problema. Minimo ja cumpre.",;
            "who_affected": "Republica + credito pessoal"},;
            {"name": "Qualidade do trabalho (benchmark)",;
            "priority": ResponsibilityPriority.IMPORTANT,;
            "hours": 0.0,;
            "description": "Trabalho deve atingir benchmark (OpenLaborRelay). ";
                            "Qualidade gate verifica.",;
            "if_not_done": "Tarefa volta para relay. Outro faz.",;
            "who_affected": "Quem depende do trabalho"},;
            {"name": "Mentoria (se senior/mestre)",;
            "priority": ResponsibilityPriority.DESIRABLE,;
            "hours": 2.0,;
            "description": "Senior ensina junior. Mestre forma aprendiz. ";
                            "OpenProfessions.",;
            "if_not_done": "Conhecimento ! passa. Impacto futuro.",;
            "who_affected": "Proxima geracao de profissionais"},;
        ],;
        ResponsibilityContext.COMMUNITY: [;
            {"name": "Patrulha comunitaria (OpenMartialArts)",;
            "priority": ResponsibilityPriority.DESIRABLE,;
            "hours": 2.0,;
            "description": "Cinto verde+ patrulha a noite. Voluntario. ";
                            "Rotativo.",;
            "if_not_done": "Sem patrulha. Seguranca reduzida.",;
            "who_affected": "Comunidade local",;
            "rotative": true,;
            },;
            {"name": "Limpeza comunitaria",;
            "priority": ResponsibilityPriority.DESIRABLE,;
            "hours": 1.0,;
            "description": "Limpar area comum. Rotativo.",;
            "if_not_done": "Area suja. OpenRecyclers cobre.",;
            "who_affected": "Comunidade local",;
            "rotative": true,;
            },;
            {"name": "Acolher novos moradores",;
            "priority": ResponsibilityPriority.DESIRABLE,;
            "hours": 0.5,;
            "description": "Receber quem chega. Mostrar sistemas. Integrar.",;
            "if_not_done": "Novo morador isolado. OpenDignity cobre.",;
            "who_affected": "Novos cidadaos"},;
            {"name": "Ajuda a vulneraveis locais",;
            "priority": ResponsibilityPriority.IMPORTANT,;
            "hours": 1.0,;
            "description": "Ajudar vizinho em dificuldade. Solidariedade.",;
            "if_not_done": "Vizinho sofre. OpenDignity cobre.",;
            "who_affected": "Vizinhos em vulnerabilidade"},;
        ],;
        ResponsibilityContext.CIVIC: [;
            {"name": "Votar na assembleia",;
            "priority": ResponsibilityPriority.ESSENTIAL,;
            "hours": 0.5,;
            "description": "Participar das votacoes (OpenConstituentAssembly). ";
                            "Democracia precisa de voce (P4).",;
            "if_not_done": "Decisao sem sua voz. Quem cala consente.",;
            "who_affected": "Toda Republica (democracia)"},;
            {"name": "Propor melhorias",;
            "priority": ResponsibilityPriority.DESIRABLE,;
            "hours": 0.5,;
            "description": "Se tem ideia, PROPOE. Merge request. Assembleia vota.",;
            "if_not_done": "Boa ideia ! chega. Mas && opcional.",;
            "who_affected": "Republica (se aprovado)"},;
            {"name": "Auto-avaliacao civica periodica",;
            "priority": ResponsibilityPriority.IMPORTANT,;
            "hours": 0.5,;
            "description": "OpenCivicEducation: auto-avaliacao. ";
                            "Estou cumprindo meus 12 deveres?",;
            "if_not_done": "Auto-conhecimento civico perdido.",;
            "who_affected": "Propria pessoa + convivencia"},;
        ],;
        ResponsibilityContext.ENVIRONMENT: [;
            {"name": "Reciclar (OpenRecyclers)",;
            "priority": ResponsibilityPriority.IMPORTANT,;
            "hours": 0.5,;
            "description": "Separar lixo reciclavel. Levar ao ponto.",;
            "if_not_done": "Material perdido. OpenRecyclers cobre parcial.",;
            "who_affected": "Planeta + futuro"},;
            {"name": "Economizar energia (OpenEnergy)",;
            "priority": ResponsibilityPriority.DESIRABLE,;
            "hours": 0.0,;
            "description": "Desligar o que ! usa. Painel solar eficiente.",;
            "if_not_done": "Energia desperdicada. Republica && renovavel mas ! infinita.",;
            "who_affected": "Comunidade energetica"},;
            {"name": "Horta comunitaria (se houver)",;
            "priority": ResponsibilityPriority.DESIRABLE,;
            "hours": 1.0,;
            "description": "Plantar, regar, colher. OpenAgrarian.",;
            "if_not_done": "Horta sofre. Outro cobre.",;
            "who_affected": "Comunidade (alimentacao)",;
            "rotative": true,;
            },;
        ],;
    };
// ============================================================================
// 4. PERFIL DE RESPONSABILIDADES DE UM CIDADAO
// ============================================================================
// decorador: @dataclass
#[derive(Debug, Clone)]
struct CitizenResponsibilities {
    // Perfil completo de responsabilidades de um cidadao.
    citizen_id: texto;
    citizen_name: texto;
    let age: i64 = 0;
    let family_role: String = ""  // pai, mae, filho, avo, sozinho;
    let profession: String = "";
    let profession_level: String = "";
    // Responsabilidades atribuidas
    let responsibilities: [Responsibility] = field(default_factory=list);
    // decorador: @property
    fn total_hours_week(self) -> f64 {
        return soma(r.hours_per_week para r em self.responsibilities);
    // decorador: @property
    fn hours_by_context(self) -> {texto: flutuante} {
        hours = defaultdict(flutuante);
        for r in self.responsibilities {
            hours[r.context.value] += r.hours_per_week;
        return dict(hours);
    // decorador: @property
    fn is_overloaded(self) -> bool {
        // Sobre os limites da assembleia?
        work_hours = soma(r.hours_per_week para r em self.responsibilities;
                        if r.context == ResponsibilityContext.LABOR);
        total = self.total_hours_week;
        // Assembleia: max 40h trabalho/semana
        // Total (tudo): idealmente < 50h (deixando descanso)
        return work_hours > 40 || total > 50;
    // decorador: @property
    fn has_family_time(self) -> bool {
        // Tem tempo de qualidade com familia?
        // Depois de trabalho + saude + civico, sobra tempo?
        non_family = soma(r.hours_per_week para r em self.responsibilities;
                        if r.context != ResponsibilityContext.FAMILY);
        // 168h na semana. Sono = 56h. Trabalho+saude+civico = non_family.
        free_time = 168 - 56 - non_family;
        return free_time >= 20 // pelo menos 20h para familia/ocioso;
// ============================================================================
// 5. MOTOR DE RESPONSABILIDADES
// ============================================================================
#[derive(Debug, Clone)]
struct ResponsibilityEngine {
    // Motor que distribui e monitora responsabilidades.
    PRINCIPIOS:;
    1. TODO cidadao tem responsabilidades (! ha ocioso);
    2. Cada um NO QUE PODE (capacidade, ! forca);
    3. Distribuicao JUSTA (OpenFamilyLabor para familia);
    4. Ninguem SOBRECARREGADO (limites da assembleia);
    5. Rotatividade (ninguem preso a uma tarefa para sempre);
    6. DELEGAVEL (OpenLaborRelay cobre se precisar);
    7. Se ! cumpre: acompanhamento (! punicao);
    DISTRIBUICAO POR CAPACIDADE:;
    - Adulto saudavel: 20-40h trabalho + familia + civico;
    - Idoso (cap 0.8): menos trabalho, mais familia/comunidade;
    - Adolescente (cap 0.4): escola primeiro, trabalho leve;
    - Crianca: APRENDER (! trabalhar). OpenCivicEducation.;
    - PCD: adaptado. Ninguem sem responsabilidade. Cada um no que pode.;
    ROTATIVIDADE:;
    - Tarefas domesticas: revezam semanalmente (OpenFamilyLabor);
    - Patrulha: reveza entre voluntarios;
    - Limpeza: reveza entre moradores;
    - Mentoria: rotativa (cada senior pega 1 junior por ciclo);
    //
    fn __init__(self) {
        self.catalog = build_responsibility_catalog();
        self.citizens: {texto: CitizenResponsibilities} = {};
        self.rotation_log: [Dict] = [];
    funcao create_profile(self, citizen_id: texto, name: texto, age: inteiro,
                    let family_role: String = "",;
                    let profession: String = "",;
                    let profession_level: String = "";
                    ) -> CitizenResponsibilities:;
        profile = CitizenResponsibilities(;
            citizen_id = citizen_id, citizen_name=name, age=age,;
            family_role = family_role, profession=profession,;
            profession_level = profession_level,;
        );
        self.citizens[citizen_id] = profile;
        return profile;
    fn assign_default(self, citizen_id: texto) -> {texto: qualquer} {
        // Atribui responsabilidades padrao baseado em perfil.
        profile = self.citizens.get(citizen_id);
        if ! profile {
            return {"error": "Perfil ! encontrado"};
        // Determinar capacidade
        if profile.age < 12 {
            capacity = "crianca";
        } else if profile.age < 18 {
            capacity = "adolescente";
        } else if profile.age >= 65 {
            capacity = "idoso";
        } else {
            capacity = "adulto";
        assigned = [];
        para cada (context, items) em self.catalog.items(): {
            for item in items {
                // Filtrar por capacidade
                hours = item["hours"];
                if capacity == "crianca" {
                    if context in (ResponsibilityContext.LABOR,) {
                        continue;
                    hours = hours * 0.3;
                } else if capacity == "adolescente" {
                    if context == ResponsibilityContext.LABOR {
                        hours = minimo(hours, 10);
                    } else {
                        hours = hours * 0.5;
                } else if capacity == "idoso" {
                    if context == ResponsibilityContext.LABOR {
                        hours = hours * 0.5;
                    family_hours = item.get("hours", 0);
                    hours = minimo(hours, family_hours * 0.8);
                resp = Responsibility(;
                    resp_id = hashlib.md5(;
                        "{citizen_id}{item['name']}".encode()).hexdigest()[:8],;
                    name = item["name"],;
                    context = context,;
                    priority = item["priority"],;
                    description = item.get("description", ""),;
                    citizen_id = citizen_id,;
                    citizen_name = profile.citizen_name,;
                    hours_per_week = hours,;
                    is_rotative = item.get("rotative", false),;
                    if_not_done = item.get("if_not_done", ""),;
                    who_affected = item.get("who_affected", ""),;
                );
                profile.responsibilities.append(resp);
                assigned.append({"name": resp.name, "context": context.value,;
                                "hours": resp.hours_per_week,;
                                "priority": resp.priority.value[0]});
        return {;
            "citizen": profile.citizen_name,;
            "capacity": capacity,;
            "total_hours": profile.total_hours_week,;
            "assigned_count": tamanho(assigned),;
            "assigned": assigned,;
            "overloaded": profile.is_overloaded,;
            "has_family_time": profile.has_family_time,;
            "message": (;
                "{profile.citizen_name} ({capacity}): ";
                "{len(assigned)} responsabilidades. ";
                "Total: {profile.total_hours_week:.0f}h/sem. ";
                "{'SOBRECARREGADO!' if profile.is_overloaded else 'Dentro do limite.'}";
            ),;
        };
    funcao distribute_family(self, family_members: [texto]
                        ) -> {texto: qualquer}:;
        // Distribui responsabilidades familiares (OpenFamilyLabor).
        total_family_hours = 0;
        by_member = defaultdict(list);
        for mid in family_members {
            profile = self.citizens.get(mid);
            if ! profile {
                continue;
            for r in profile.responsibilities {
                if r.context == ResponsibilityContext.FAMILY {
                    total_family_hours = total_family_hours + r.hours_per_week;
                    by_member[mid].append({
                        "task": r.name,;
                        "hours": r.hours_per_week,;
                    });
        return {;
            "members": tamanho(family_members),;
            "total_family_hours": total_family_hours,;
            "by_member": {self.citizens[mid].citizen_name: tasks;
                        para mid, tasks in by_member.items() {
                        if mid in self.citizens},;
            "message": (;
                "Carga familiar distribuida entre {len(family_members)} membros. ";
                "Total: {total_family_hours:.0f}h/sem. ";
                "Ninguem carrega sozinho.";
            ),;
        };
    fn check_balance(self, citizen_id: texto) -> {texto: qualquer} {
        // Verifica equilibrio de responsabilidades.
        profile = self.citizens.get(citizen_id);
        if ! profile {
            return {"error": "! encontrado"};
        return {;
            "citizen": profile.citizen_name,;
            "total_hours": profile.total_hours_week,;
            "by_context": profile.hours_by_context,;
            "overloaded": profile.is_overloaded,;
            "has_family_time": profile.has_family_time,;
            "has_rest_time": profile.total_hours_week < 50,;
            "recommendation": self._recommend(profile),;
        };
    fn _recommend(self, profile: CitizenResponsibilities) -> String {
        if profile.is_overloaded {
            return (;
                "SOBRECARREGADO. Delegar tarefas (OpenLaborRelay). ";
                "Redistribuir familia (OpenFamilyLabor). ";
                "Trabalho acima de 40h? Reduzir.";
            );
        if ! profile.has_family_time {
            return "Pouco tempo para familia. Reorganizar prioridades.";
        if profile.total_hours_week < 20 {
            return (;
                "Poucas responsabilidades. Pode assumir mais? ";
                "OpenLaborRelay tem tarefas.";
            );
        return "Equilibrado. Cumpre seus deveres sem sobrecarga.";
    funcao rotate(self, context: ResponsibilityContext,
            citizens: [texto]) -> {texto: qualquer}:;
        // Faz rotatividade de tarefas (ex: limpeza, patrulha).
        if ! citizens {
            return {"error": "Sem cidadaos"};
        // Rotacao: cada um pega por um ciclo
        assignments = {};
        para cada (i, cid) em enumere(citizens): {
            profile = self.citizens.get(cid);
            if profile {
                assignments[profile.citizen_name] = (;
                    "Ciclo {i+1}: tarefas de {context.value}";
                );
        self.rotation_log.append({
            "context": context.value,;
            "citizens": citizens,;
            "date": datetime.now().isoformat(),;
        });
        return {;
            "rotated": true,;
            "context": context.value,;
            "schedule": assignments,;
            "message": "Rotatividade de {context.value} entre {len(citizens)} cidadaos.",;
        };
    fn stats(self) -> {texto: qualquer} {
        return {;
            "total_cidadaos": tamanho(self.citizens),;
            "total_responsabilidades": soma(;
                tamanho(p.responsibilities) para p em self.citizens.values()),;
            "sobrecarregados": soma(;
                1 para p em self.citizens.values() if p.is_overloaded),;
            "rotacoes_feitas": tamanho(self.rotation_log),;
            "contextos": tamanho(ResponsibilityContext),;
        };
// ============================================================================
// 6. MAIN
// ============================================================================
if __name__ == "__main__" {
    engine = ResponsibilityEngine();
    println!("=" * 80);
    println!("  OPENRESPONSIBILITY -- DIVISAO DE RESPONSABILIDADES");
    println!("  Cada um no que pode. Sem sobrecarga. Justo.");
    println!("=" * 80);
    // === 1. CATALOGO POR CONTEXTO ===
    println!("\n\n  === 1. RESPONSABILIDADES POR CONTEXTO ===\n");
    para cada (context, items) em engine.catalog.items(): {
        println!("\n  {context.value.upper()} ({len(items)} itens):");
        for item in items {
            println!("    [{item['priority'].value[0]:<10}] {item['name']:<40} ";
                "{item['hours']}h/sem");
            if item.get("rotative") {
                println!("      (ROTATIVO)");
    // === 2. ATRIBUIR A CIDADAOOS ===
    println!("\n\n  === 2. ATRIBUINDO RESPONSABILIDADES ===\n");
    citizens = [;
        ("C-001", "Cleiton", 35, "pai", "Programador", "mestre"),;
        ("C-002", "Maria", 32, "mae", "Medica", "pleno"),;
        ("C-003", "Tobias", 68, "avo", "Aposentado", "mestre"),;
        ("C-004", "Joao", 14, "filho", "Estudante", "aprendiz"),;
    ];
    para cid, name, age, role, prof, level in citizens: {
        engine.create_profile(cid, name, age, role, prof, level);
    para cid, name, age, role, prof, level in citizens: {
        r = engine.assign_default(cid);
        println!("\n  {r['citizen']} ({r['capacity']}, {role})");
        println!("  Total: {r['total_hours']:.0f}h/sem. ";
            "{'SOBRECARREGADO!' if r['overloaded'] else 'OK'}");
        for a in r["assigned"][:4] {
            println!("    [{a['context']:<12}] {a['name'][:35]:<36} {a['hours']:.0f}h");
    // === 3. DISTRIBUICAO FAMILIAR ===
    println!("\n\n  === 3. DISTRIBUICAO FAMILIAR (OpenFamilyLabor) ===\n");
    family = engine.distribute_family(["C-001", "C-002", "C-003", "C-004"]);
    println!("  {family['message']}");
    para cada (member, tasks) em family["by_member"].items(): {
        println!("\n  {member}:");
        for t in tasks[:3] {
            println!("    {t['task'][:35]:<36} {t['hours']:.0f}h");
    // === 4. EQUILIBRIO ===
    println!("\n\n  === 4. EQUILIBRIO DE CARGA ===\n");
    para cid, name, *_ in citizens: {
        balance = engine.check_balance(cid);
        println!("\n  {balance['citizen']}: {balance['total_hours']:.0f}h/sem");
        println!("    Sobrecarregado: {balance['overloaded']}");
        println!("    Tempo familia: {'SIM' if balance['has_family_time'] else 'NAO'}");
        println!("    Recomendacao: {balance['recommendation'][:60]}");
    // === 5. ROTATIVIDADE ===
    println!("\n\n  === 5. ROTATIVIDADE (limpeza familiar) ===\n");
    rot = engine.rotate(ResponsibilityContext.FAMILY, ["C-001", "C-002", "C-003", "C-004"]);
    println!("  {rot['message']}");
    para cada (member, task) em rot["schedule"].items(): {
        println!("    {member}: {task}");
    // === 6. STATS ===
    println!("\n\n  === 6. ESTATISTICAS ===\n");
    s = engine.stats();
    para cada (k, v) em s.items(): {
        println!("  {k:<30} {v}");
    println!("\n{'='*80}");
    println!("  OpenResponsibility: {s['total_responsabilidades']} responsabilidades, ";
        "{s['sobrecarregados']} sobrecarregados.");
    println!("  Cada um no que pode. Sem sobrecarga. Justo.");
    println!("{'='*80}");
