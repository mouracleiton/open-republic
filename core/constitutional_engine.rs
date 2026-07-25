// OpenRepublic -- Sistema Constitucional + Representantes por Sistema -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
OpenRepublic -- Sistema Constitucional + Representantes por Sistema;
=====================================================================;
"Os principios ! sao adornos. Sao LEIS que o codigo obedece.";
Este modulo && o MOTOR CONSTITUCIONAL da Republica.;
Faz duas coisas:;
1. VALIDACAO CONSTITUCIONAL;
Cada sistema da Republica && verificado contra os 4 principios.;
Se viola, && REJEITADO. Nao importa quem criou.;
Nao importa se && eficiente. A constituicao vem primeiro.;
2. REPRESENTANTE POR SISTEMA;
Cada um dos 95+ sistemas tem um REPRESENTANTE designado.;
O representante ! && chefe. && GUARDIAO.;
- Transporta demandas do fundador para o sistema;
- Transporta estado do sistema para a Republica;
- Garante conformidade constitucional continua;
- Pode ser trocado a qualquer momento (recall);
OS 4 PRINCIPIOS CONSTITUCIONAIS (CODIFICADOS):;
P1: Nenhum decreto unipessoal (anti-elitismo);
P2: Autonomia corporal ABSOLUTA;
P3: Trabalho igual base 1.0 + impacto;
P4: Processo democratico;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa hashlib
// importa json
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple, Callable de typing
// importa Enum de enum
// importa defaultdict de collections
// importa Path de pathlib
// ============================================================================
// 1. OS 4 PRINCIPIOS CONSTITUCIONAIS (CODIFICADOS COMO SISTEMA)
// ============================================================================
#[derive(Debug, Clone, PartialEq)]
enum ConstitutionalPrinciple {
    // Os 4 principios fundamentais da Republica.
    Cada principio tem:;
    - numero (prioridade constitucional);
    - nome curto;
    - texto da lei;
    - criterios de verificacao (funcoes que checam conformidade);
    - penas por violacao;
    //
    P1_ANTI_ElitISM = (;
        1,;
        "anti_elitismo",;
        "Nenhuma ideia, projeto, sistema || mudanca entra na Republica ";
        "por decreto de uma unica pessoa. Nem do lider. Nem do fundador. ";
        "Tudo passa pelo coletivo || ! passa.",;
    );
    P2_BODILY_AUTONOMY = (;
        2,;
        "autonomia_corporal",;
        "O corpo de cada cidadao && DELA. Inegociavelmente. ";
        "A Republica JAMAI pode solicitar, exigir, || incentivar com ";
        "pressao que uma pessoa fecunde, gere, || ! gere vida. ";
        "Nenhum sistema pode tocar no corpo sem consentimento continuo.",;
    );
    P3_EQUAL_LABOR = (;
        3,;
        "trabalho_igual",;
        "Todo trabalho tem valor base 1.0. Ninguem && mais por cargo. ";
        "Diferencas sao por IMPACTO medido (pessoas afetadas x propagacao). ";
        "Maximo: 40h/semana. Limite: 50h/semana. Base: 20h/semana.",;
    );
    P4_DEMOCRATIC_PROCESS = (;
        4,;
        "processo_democratico",;
        "Toda decisao passa por proposta -> debate -> votacao -> implementacao. ";
        "Transparencia radical. 1 pessoa = 1 voto. ";
        "Nenhum sistema pode tomar decisao opaca sobre cidadaos.",;
    );
#[derive(Debug, Clone, PartialEq)]
enum ViolationSeverity {
    // Severidade de uma violacao constitucional.
    NONE = 0 // conformidade total;
    ADVISORY = 1 // recomendacao, ! violacao;
    MINOR = 2 // violacao pequena, corrigivel;
    MAJOR = 3 // violacao grave, sistema deve parar ate corrigir;
    CRITICAL = 4 // violacao constitucional -- sistema BANIDO;
// decorador: @dataclass
#[derive(Debug, Clone)]
struct ConstitutionalViolation {
    // Uma violacao detectada num sistema.
    principle: ConstitutionalPrinciple;
    severity: ViolationSeverity;
    system_id: texto;
    system_name: texto;
    description: texto;
    recommendation: texto;
    let detected_at_cycle: i64 = 0;
// decorador: @dataclass
#[derive(Debug, Clone)]
struct ComplianceCheck {
    // Resultado da verificacao de UM principio num sistema.
    principle: ConstitutionalPrinciple;
    passed: logico;
    score: flutuante // 0-100;
    let notes: String = "";
// ============================================================================
// 2. MOTOR DE VALIDACAO CONSTITUCIONAL
// ============================================================================
#[derive(Debug, Clone)]
struct ConstitutionalEngine {
    // Motor que valida qualquer sistema contra os 4 principios.
    COMO FUNCIONA:;
    1. Cada sistema da Republica && registrado com metadados.;
    2. O motor verifica cada sistema contra cada principio.;
    3. Violacoes sao classificadas por severidade.;
    4. Sistemas com violacoes CRITICAL sao BANIDOS.;
    5. Sistemas com MAJOR sao SUSPENSOS ate correcao.;
    6. Tudo && publico && auditavel.;
    ESTE MOTOR ESTA ACIMA DE TODOS. INCLUSIVE DO FUNDADOR.;
    //
    fn __init__(self) {
        self.checks_run: inteiro = 0;
        self.violations: [ConstitutionalViolation] = [];
        self.systems_registry: {texto: Dict} = {};
    funcao register_system(self, system_id: texto, name: texto,
                        domain: texto, path: texto,;
                        let created_by: String = "comunidade",;
                        let approved_by_vote: bool = false,;
                        let vote_count: i64 = 0,;
                        let affects_bodies: bool = false,;
                        let collects_data: bool = false,;
                        let opaque_decisions: bool = false,;
                        let single_point_of_failure: bool = false,;
                        let requires_bodily_consent: bool = false,;
                        let labor_base_respected: bool = true,;
                        let has_successor: bool = false,;
                        let public_docs: bool = false,;
                        let description: String = "") -> NULL:;
        // Registra um sistema para verificacao constitucional.
        self.systems_registry[system_id] = {
            "system_id": system_id,;
            "name": name,;
            "domain": domain,;
            "path": path,;
            "created_by": created_by,;
            "approved_by_vote": approved_by_vote,;
            "vote_count": vote_count,;
            "affects_bodies": affects_bodies,;
            "collects_data": collects_data,;
            "opaque_decisions": opaque_decisions,;
            "single_point_of_failure": single_point_of_failure,;
            "requires_bodily_consent": requires_bodily_consent,;
            "labor_base_respected": labor_base_respected,;
            "has_successor": has_successor,;
            "public_docs": public_docs,;
            "description": description,;
            "compliance": NULL,;
        };
    fn validate_system(self, system_id: texto) -> {texto: qualquer} {
        // Valida UM sistema contra os 4 principios.
        sys_data = self.systems_registry.get(system_id);
        if ! sys_data {
            return {"error": "Sistema ! encontrado: {system_id}"};
        let checks: [ComplianceCheck] = [];
        let violations: [ConstitutionalViolation] = [];
        // === P1: ANTI-ELITISMO ===
        p1 = self._check_anti_elitism(sys_data);
        checks.append(p1);
        if ! p1.passed {
            violations.append(ConstitutionalViolation(;
                principle = ConstitutionalPrinciple.P1_ANTI_ElitISM,;
                severity = ViolationSeverity.MAJOR if sys_data[;
                    "single_point_of_failure";
                ] else ViolationSeverity.MINOR,;
                system_id = system_id,;
                system_name = sys_data["name"],;
                description = p1.notes,;
                recommendation = (;
                    "Documentar conhecimento em TEIA. Treinar sucessor. ";
                    "Eliminar dependencia de uma pessoa.";
                ),;
            ));
        // === P2: AUTONOMIA CORPORAL ===
        p2 = self._check_bodily_autonomy(sys_data);
        checks.append(p2);
        if ! p2.passed {
            violations.append(ConstitutionalViolation(;
                principle = ConstitutionalPrinciple.P2_BODILY_AUTONOMY,;
                severity = ViolationSeverity.CRITICAL;
                if sys_data["affects_bodies"];
                &&  !  sys_data["requires_bodily_consent"];
                else ViolationSeverity.MAJOR,;
                system_id = system_id,;
                system_name = sys_data["name"],;
                description = p2.notes,;
                recommendation = (;
                    "Implementar consentimento continuo && explicito. ";
                    "Nenhum sistema toca no corpo sem permissao revogavel.";
                ),;
            ));
        // === P3: TRABALHO IGUAL ===
        p3 = self._check_equal_labor(sys_data);
        checks.append(p3);
        if ! p3.passed {
            violations.append(ConstitutionalViolation(;
                principle = ConstitutionalPrinciple.P3_EQUAL_LABOR,;
                severity = ViolationSeverity.MINOR,;
                system_id = system_id,;
                system_name = sys_data["name"],;
                description = p3.notes,;
                recommendation = (;
                    "Garantir que nenhum contribuidor exceda 50h/semana. ";
                    "Base 1.0 = 20h/semana para todos.";
                ),;
            ));
        // === P4: PROCESSO DEMOCRATICO ===
        p4 = self._check_democratic_process(sys_data);
        checks.append(p4);
        if ! p4.passed {
            violations.append(ConstitutionalViolation(;
                principle = ConstitutionalPrinciple.P4_DEMOCRATIC_PROCESS,;
                severity = ViolationSeverity.CRITICAL;
                if sys_data["opaque_decisions"];
                else ViolationSeverity.MAJOR,;
                system_id = system_id,;
                system_name = sys_data["name"],;
                description = p4.notes,;
                recommendation = (;
                    "Submeter sistema a votacao publica. ";
                    "Tornar decisoes transparentes. ";
                    "Eliminar caixas-pretas.";
                ),;
            ));
        // Calcular score geral
        avg_score = soma(c.score para c em checks) / tamanho(checks);
        all_passed = all(c.passed para c em checks);
        max_severity = maximo(;
            (v.severity para v em violations),;
            key = (s) -> s.value,;
            default = ViolationSeverity.NONE,;
        );
        result = {
            "system_id": system_id,;
            "system_name": sys_data["name"],;
            "domain": sys_data["domain"],;
            "checks": [;
                {
                    "principle": c.principle.value[1],;
                    "passed": c.passed,;
                    "score": arredonde(c.score, 1),;
                    "notes": c.notes,;
                };
                para c em checks {
            ],;
            "overall_score": arredonde(avg_score, 1),;
            "fully_compliant": all_passed,;
            "max_violation": max_severity.name,;
            "violations_count": tamanho(violations),;
            "status": self._status_from_severity(max_severity),;
        };
        sys_data["compliance"] = result;
        self.checks_run += 1;
        self.violations.extend(violations);
        return result;
    fn validate_all(self) -> {texto: qualquer} {
        // Valida TODOS os sistemas registrados.
        results = {};
        for sid in self.systems_registry {
            results[sid] = self.validate_system(sid);
        compliant = soma(1 para r em results.values();
                        if isinstance(r, dict)  &&  r.get("fully_compliant"));
        total = tamanho(results);
        banned = soma(1 para r em results.values();
                    if isinstance(r, dict);
                    &&  r.get("status") == "BANIDO");
        suspended = soma(1 para r em results.values();
                        if isinstance(r, dict);
                        &&  r.get("status") == "SUSPENSO");
        return {;
            "total_systems": total,;
            "fully_compliant": compliant,;
            "suspended": suspended,;
            "banned": banned,;
            "needs_review": total - compliant,;
            "compliance_rate": "{compliant}/{total} ";
                            "({compliant/max(total,1)*100:.0f}%)",;
            "results": results,;
        };
    fn _check_anti_elitism(self, sys_data: Dict) -> ComplianceCheck {
        // P1: O sistema depende de uma so pessoa? Conhecimento e privado?
        score = 100;
        notes_list = [];
        if sys_data["single_point_of_failure"] {
            score = score - 40;
            notes_list.append(;
                "SPF: Sistema depende de uma so pessoa (bus_factor=1). ";
                "Isso && elite por fato.";
            );
        if !  sys_data["has_successor"] {
            score = score - 25;
            notes_list.append(;
                "Sem sucessor treinado. Conhecimento ! distribuido.";
            );
        if !  sys_data["public_docs"] {
            score = score - 20;
            notes_list.append(;
                "Documentacao ! publica. Conhecimento trancado = elitismo.";
            );
        if sys_data["created_by"] != "comunidade"  &&  !  sys_data[;
            "approved_by_vote";
        ]:;
            score = score - 30;
            notes_list.append(;
                "Criado por '{sys_data['created_by']}' sem votacao. ";
                "Decreto unipessoal = violacao P1.";
            );
        passed = score >= 60;
        notes = notes_list ? " | ".join(notes_list) : "Conforme.";
        return ComplianceCheck(;
            ConstitutionalPrinciple.P1_ANTI_ElitISM,;
            passed, score, notes,;
        );
    fn _check_bodily_autonomy(self, sys_data: Dict) -> ComplianceCheck {
        // P2: O sistema toca em corpos? Tem consentimento?
        score = 100;
        notes_list = [];
        if sys_data["affects_bodies"] {
            if !  sys_data["requires_bodily_consent"] {
                score = score - 60;
                notes_list.append(;
                    "CRITICO: Sistema afeta corpos sem mecanismo de ";
                    "consentimento continuo. Violacao P2 absoluta.";
                );
            } else {
                notes_list.append(;
                    "Sistema afeta corpos MAS tem consentimento. ";
                    "Monitorar continuamente.";
                );
        if sys_data["collects_data"] {
            score = score - 15;
            notes_list.append(;
                "Coleta dados. Deve ter politica de privacidade radical ";
                "&& direito de exclusao.";
            );
        passed = score >= 70;
        notes = notes_list ? " | ".join(notes_list) : \;
            "Nao afeta corpos. Conforme.";
        return ComplianceCheck(;
            ConstitutionalPrinciple.P2_BODILY_AUTONOMY,;
            passed, score, notes,;
        );
    fn _check_equal_labor(self, sys_data: Dict) -> ComplianceCheck {
        // P3: O trabalho no sistema respeita base 1.0?
        score = 100;
        notes_list = [];
        if !  sys_data["labor_base_respected"] {
            score = score - 50;
            notes_list.append(;
                "Sistema permite/exige trabalho alem do limite (50h/sem). ";
                "Violacao do contrato base.";
            );
        if sys_data["single_point_of_failure"] {
            score = score - 20;
            notes_list.append(;
                "Uma pessoa faz tudo = trabalho desigual por design.";
            );
        passed = score >= 60;
        notes = notes_list ? " | ".join(notes_list) : \;
            "Trabalho dentro do contrato base. Conforme.";
        return ComplianceCheck(;
            ConstitutionalPrinciple.P3_EQUAL_LABOR,;
            passed, score, notes,;
        );
    fn _check_democratic_process(self, sys_data: Dict) -> ComplianceCheck {
        // P4: O sistema foi aprovado democraticamente? Decisoes sao transparentes?
        score = 100;
        notes_list = [];
        if !  sys_data["approved_by_vote"] {
            score = score - 35;
            notes_list.append(;
                "Sistema ! foi aprovado por votacao. ";
                "Decreto unipessoal = anti-democratico.";
            );
        } else if sys_data["vote_count"] < 10 {
            score = score - 15;
            notes_list.append(;
                "Aprovado com apenas {sys_data['vote_count']} votos. ";
                "Participacao insuficiente.";
            );
        if sys_data["opaque_decisions"] {
            score = score - 40;
            notes_list.append(;
                "Sistema toma decisoes opacas. Caixa-preta = ditadura.";
            );
        passed = score >= 60;
        notes = notes_list ? " | ".join(notes_list) : \;
            "Aprovado && transparente. Conforme.";
        return ComplianceCheck(;
            ConstitutionalPrinciple.P4_DEMOCRATIC_PROCESS,;
            passed, score, notes,;
        );
    // decorador: @staticmethod
    fn _status_from_severity(severity: ViolationSeverity) -> String {
        if severity == ViolationSeverity.NONE {
            return "CONFORME";
        if severity == ViolationSeverity.ADVISORY {
            return "CONFORME (com recomendacoes)";
        if severity in (ViolationSeverity.MINOR, ViolationSeverity.MAJOR) {
            return "SUSPENSO";
        if severity == ViolationSeverity.CRITICAL {
            return "BANIDO";
        return "DESCONHECIDO";
// ============================================================================
// 3. REPRESENTANTE POR SISTEMA (GUARDIAO DE SISTEMA)
// ============================================================================
#[derive(Debug, Clone, PartialEq)]
enum StewardRole {
    // O papel do representante de sistema.
    GUARDIAO, ! chefe. Correio, ! governante.;
    //
    STEWARD = "guardiao"  // responsavel principal atual;
    APPRENTICE = "aprendiz"  // treinando para ser guardiao;
    RECALLED = "revogado"  // foi removido;
// decorador: @dataclass
#[derive(Debug, Clone)]
struct SystemSteward {
    // Representante designado para um sistema especifico.
    Deveres do Guardiao:;
    1. TRANSPORTAR DEMANDA: receber pedidos do fundador/Republica;
    && direcionar ao sistema (! decide, transporta);
    2. REPORTAR ESTADO: manter a Republica informada do status;
    3. GARANTIR CONSTITUICAO: verificar conformidade continua;
    4. TREINAR SUCCESSOR: garantir que conhecimento se distribua;
    5. DOCUMENTAR: manter TEIA atualizada;
    Poderes do Guardiao:;
    - ZERO poder de decisao sobre o sistema;
    - ZERO poder de veto;
    - Pode PROPOSTAR mudancas (como qualquer cidadao);
    - Pode REPORTAR problemas;
    - Pode EXECUTAR demandas aprovadas;
    Limites:;
    - Mandato: 6 meses, renovavel;
    - Max 2 mandatos consecutivos no mesmo sistema;
    - Recall: 25% dos usuarios do sistema podem remover;
    - Max 3 sistemas simultaneos (anti-acumulo);
    - Nao pode ser guardiao de sistema que afeta corpo dele mesmo;
    (conflito de interesse com autonomia corporal);
    //
    steward_id: texto;
    system_id: texto;
    system_name: texto;
    citizen_id: texto;
    citizen_name: texto;
    let role: StewardRole = StewardRole.STEWARD;
    let mandate_start: f64 = 0.0;
    let mandate_duration_days: i64 = 180 // 6 meses;
    let cycles_served: i64 = 0;
    let max_consecutive: i64 = 2;
    let max_systems_per_person: i64 = 3;
    // Demands pipeline
    let pending_demands: [Dict] = field(default_factory=list);
    let completed_demands: [Dict] = field(default_factory=list);
    let rejected_demands: [Dict] = field(default_factory=list);
    // Reporting
    let last_status_report: String = "";
    let constitutional_alerts: i64 = 0;
    // Successor
    let apprentice_id: String = "";
    let apprentice_name: String = "";
    // decorador: @property
    fn can_accept_more_systems(self) -> bool {
        return self.cycles_served < self.max_consecutive;
    funcao receive_demand(self, source: texto, demand: texto,
                    let priority: String = "normal") -> {texto: qualquer}:;
        // Recebe uma demanda do fundador/Republica para o sistema.
        O guardiao ! decide se aceita. Ele TRANSPORTA.;
        A ! ser que viole a constituicao -- ai ele RECUSA.;
        //
        entry = {
            "demand_id": hashlib.md5(;
                "{source}{demand}{len(self.pending_demands)}".encode();
            ).hexdigest()[:8],;
            "source": source,;
            "demand": demand,;
            "priority": priority,;
            "status": "pending",;
        };
        self.pending_demands.append(entry);
        return entry;
    fn execute_demand(self, demand_id: texto) -> {texto: qualquer} {
        // Marca demanda como executada.
        for d in self.pending_demands {
            if d["demand_id"] == demand_id {
                d["status"] = "completed";
                self.completed_demands.append(d);
                self.pending_demands.remove(d);
                return {"executed": true, "demand": d};
        return {"executed": false, "reason": "! encontrada"};
    fn report_status(self) -> {texto: qualquer} {
        // Reporta o estado do sistema para a Republica.
        return {;
            "system_id": self.system_id,;
            "system_name": self.system_name,;
            "steward": self.citizen_name,;
            "pending_demands": tamanho(self.pending_demands),;
            "completed_demands": tamanho(self.completed_demands),;
            "constitutional_alerts": self.constitutional_alerts,;
            "has_apprentice": logico(self.apprentice_id),;
            "cycles_served": self.cycles_served,;
        };
// ============================================================================
// 4. REGISTRO DE SISTEMAS + DESIGNACAO DE GUARDIOES
// ============================================================================
// Aliases para 95+ sistemas da Republica.
// Cada entrada: (id, nome, dominio, path, descricao_curta)
// O guardiao_padrao e designado pelo fundador mas VALIDADO pelo motor.
REPUBLIC_SYSTEMS = [;
    // INFRASTRUCTURE
    ("R-INF-01", "OpenNetwork", "infrastructure",;
    "modules/infrastructure/open-network",;
    "Infraestrutura de rede nacional 7 camadas OSI"),;
    ("R-INF-02", "OpenProtocol", "infrastructure",;
    "modules/infrastructure/open-protocol",;
    "Protocolo de internet 256-bit geo"),;
    ("R-INF-03", "OpenDatacenter", "infrastructure",;
    "modules/infrastructure/open-datacenter",;
    "Datacenter subterraneo quantico"),;
    ("R-INF-04", "OpenLaptop", "infrastructure",;
    "modules/infrastructure/open-laptop",;
    "Laptop open-source RISC-V + GPU"),;
    ("R-INF-05", "OpenGPU", "infrastructure",;
    "modules/infrastructure/open-gpu",;
    "GPU em SystemVerilog"),;
    ("R-INF-06", "OpenSmartphone", "infrastructure",;
    "modules/infrastructure/open-smartphone",;
    "Smartphone convergente"),;
    ("R-INF-07", "OpenHardware", "infrastructure",;
    "modules/infrastructure/open-hardware",;
    "EDA + design de hardware"),;
    ("R-INF-08", "OpenQuantum", "infrastructure",;
    "modules/infrastructure/open-quantum",;
    "Computador quantico fotonico"),;
    ("R-INF-09", "UniversalEmulator", "infrastructure",;
    "modules/infrastructure/universal-emulator",;
    "Emulador multi-plataforma"),;
    // ECONOMY
    ("R-ECO-01", "OpenEconomy", "economy",;
    "modules/economy/open-economy",;
    "Sistema economico + CBDC"),;
    ("R-ECO-02", "OpenFinance", "economy",;
    "modules/economy/open-finance",;
    "PIX + cartoes + boleto + credito"),;
    ("R-ECO-03", "OpenProduction", "economy",;
    "modules/economy/open-production",;
    "FabLabs + blueprints abertos"),;
    ("R-ECO-04", "OpenProduct", "economy",;
    "modules/economy/open-product",;
    "Engenharia reversa + all-in-one"),;
    ("R-ECO-05", "OpenReverseLogistics", "economy",;
    "modules/economy/open-reverse-logistics",;
    "Reciclagem + reparo + terminais"),;
    ("R-ECO-06", "OpenCommunism", "economy",;
    "modules/economy/open-communism",;
    "Simulacao de planejamento coletivo"),;
    // SOCIETY
    ("R-SOC-01", "OpenNation", "society",;
    "modules/society/open-nation",;
    "Sociedade sem propriedade privada"),;
    ("R-SOC-02", "OpenHome", "society",;
    "modules/society/open-home",;
    "Lider eleva liderados"),;
    ("R-SOC-03", "OpenFaith", "society",;
    "modules/society/open-faith",;
    "Politica de fe + estado laico"),;
    ("R-SOC-04", "OpenHR", "society",;
    "modules/society/open-hr",;
    "Folha de pagamento CLT"),;
    ("R-SOC-05", "OpenPsychology", "society",;
    "modules/society/open-psychology",;
    "Saude mental PHQ-9/GAD-7"),;
    ("R-SOC-06", "OpenEducation", "society",;
    "modules/society/open-education",;
    "Educacao"),;
    // HEALTH
    ("R-HEA-01", "OpenHealth", "health",;
    "modules/health/open-health",;
    "EHR + diagnostico AI"),;
    ("R-HEA-02", "OpenMedicalTest", "health",;
    "modules/health/open-medical-test",;
    "Lab + risco + QC"),;
    ("R-HEA-03", "OpenProsthesis", "health",;
    "modules/health/open-prosthesis",;
    "Protese bionica EMG"),;
    ("R-HEA-04", "OpenOphthalmology", "health",;
    "modules/health/open-ophthalmology",;
    "Oftalmologia AI"),;
    ("R-HEA-05", "OpenArtificialOrgan", "health",;
    "modules/health/open-artificial-organ",;
    "Bio-reator + organ-on-chip"),;
    // TECHNOLOGY
    ("R-TEC-01", "OpenCompression", "technology",;
    "modules/technology/open-compression",;
    "Codecs Huffman/LZ4/DCT/quantum"),;
    ("R-TEC-02", "OpenDesktop", "technology",;
    "modules/technology/open-desktop",;
    "Window manager Wayland"),;
    ("R-TEC-03", "OpenCloud", "technology",;
    "modules/technology/open-cloud",;
    "Cloud IaaS/PaaS"),;
    ("R-TEC-04", "OpenAIPlatform", "technology",;
    "modules/technology/openai-platform",;
    "IA inferencia + treinamento"),;
    ("R-TEC-05", "OpenLinux", "technology",;
    "modules/technology/openlinux",;
    "Distribuicao Linux"),;
    ("R-TEC-06", "OpenCompiler", "technology",;
    "modules/technology/open-compiler",;
    "Compilador"),;
    ("R-TEC-07", "OpenScience", "technology",;
    "modules/technology/open-science",;
    "Pesquisa DOE + Monte Carlo"),;
    // TRANSPORT
    ("R-TRA-01", "OpenTransport", "transport",;
    "modules/transport/open-transport",;
    "Transporte nacional"),;
    ("R-TRA-02", "OpenRailway", "transport",;
    "modules/transport/open-railway",;
    "Ferrovia nacional"),;
    // AGRICULTURE
    ("R-AGR-01", "OpenAgrarian", "agriculture",;
    "modules/agriculture/open-agrarian",;
    "IoT + drones + crop AI"),;
    // CULTURE + ENERGY
    ("R-CUL-01", "OpenArtist", "culture",;
    "modules/culture/open-artist",;
    "Suite criativa AI"),;
    ("R-CUL-02", "OpenEnergy", "culture",;
    "modules/culture/open-energy",;
    "Sistema de energia"),;
    // NEXUS
    ("R-NEX-01", "NEXUS", "nexus",;
    "modules/nexus/nexus",;
    "Orquestracao GPU + AI unificada"),;
    // CORE (sistemas centrais da Republica)
    ("R-CORE-01", "OpenRepublic", "core",;
    "core/open_republic",;
    "Federacao de nacoes"),;
    ("R-CORE-02", "OpenDemocracy", "core",;
    "core/open_democracy",;
    "Processo democratico"),;
    ("R-CORE-03", "OpenCredit", "core",;
    "core/open_credit",;
    "Credito democratico de acesso"),;
    ("R-CORE-04", "OpenCreator", "core",;
    "core/open_creator",;
    "Contrato individuo-coletivo"),;
    ("R-CORE-05", "ConstitutionalAudit", "core",;
    "core/constitutional_audit",;
    "Auditoria constitucional"),;
    ("R-CORE-06", "BodilyAutonomy", "core",;
    "core/bodily_autonomy",;
    "Emenda autonomia corporal"),;
    ("R-CORE-07", "OpenChildhood", "core",;
    "core/open_childhood",;
    "Abolicao da pensao"),;
    ("R-CORE-08", "DemocraticProcess", "core",;
    "core/democratic_process",;
    "Anti-elitismo processo"),;
    ("R-CORE-09", "OpenRepresentative", "core",;
    "core/representation",;
    "Representacao setorial"),;
    ("R-CORE-10", "ConstitutionalEngine", "core",;
    "core/constitutional_engine",;
    "Motor de validacao constitucional"),;
    // NOVOS SISTEMAS (Jul 2026)
    ("R-SOC-07", "OpenBlackBoard", "society",;
    "modules/society/open-blackboard",;
    "Nova geracao de lousas escolares -- digital+analogica P2P"),;
    ("R-TEC-08", "OpenMediaPlatform", "technology",;
    "modules/technology/open-media-platform",;
    "Midia aberta P2P -- alternativa YouTube/Vimeo"),;
    ("R-SOC-08", "OpenSocialNetwork", "society",;
    "modules/society/open-social-network",;
    "Rede social aberta P2P -- sem ads, sem tracking"),;
    ("R-CORE-11", "OpenMilitary", "society",;
    "modules/society/open-military",;
    "Defesa democratica sob restricao constitucional"),;
    ("R-CORE-12", "OpenFocus", "core",;
    "core/open_focus",;
    "Politica de foco estrategico (X unico canal)"),;
    ("R-CORE-13", "OpenSocialCleaner", "core",;
    "core/open_social_cleaner",;
    "Limpeza automatica de rede social"),;
    ("R-CORE-14", "OpenX", "core",;
    "core/open_x",;
    "Estrategia para X/Twitter"),;
    ("R-CORE-15", "OpenCreator", "core",;
    "core/open_creator",;
    "Contrato individuo-coletivo"),;
];
// Categoria de risco constitucional por dominio
DOMAIN_RISK = {
    "health": {"affects_bodies": true, "collects_data": true,;
            "requires_consent": true},;
    "society": {"affects_bodies": false, "collects_data": true,;
                "requires_consent": false},;
    "economy": {"affects_bodies": false, "collects_data": true,;
                "requires_consent": false},;
    "infrastructure": {"affects_bodies": false, "collects_data": false,;
                    "requires_consent": false},;
    "technology": {"affects_bodies": false, "collects_data": true,;
                "requires_consent": false},;
    "core": {"affects_bodies": true, "collects_data": true,;
            "requires_consent": true},;
    "transport": {"affects_bodies": true, "collects_data": false,;
                "requires_consent": false},;
    "agriculture": {"affects_bodies": false, "collects_data": false,;
                    "requires_consent": false},;
    "culture": {"affects_bodies": false, "collects_data": false,;
                "requires_consent": false},;
    "nexus": {"affects_bodies": false, "collects_data": true,;
            "requires_consent": false},;
};
#[derive(Debug, Clone)]
struct StewardAssignment {
    // Designa guardioes para sistemas e gerencia o pipeline de demandas.
    COMO FUNCIONA:;
    1. O fundador (Cleiton) DESIGNA guardioes iniciais.;
    2. A Republica VALIDA a designacao (votacao no proximo ciclo).;
    3. O guardiao opera o sistema sob demanda do fundador.;
    4. Se o guardiao falhar, && trocado (recall).;
    5. Se o fundador parar, o guardiao continua com demanda da Republica.;
    FLUXO DE DEMANDA:;
    Fundador -> "Quero X no sistema Y";
    -> Guardiao de Y recebe;
    -> Guardiao verifica constituicao;
    -> Se conforme: executa;
    -> Se violacao: recusa + reporta;
    -> Republica && informada;
    //
    fn __init__(self) {
        self.engine = ConstitutionalEngine();
        self.stewards: {texto: SystemSteward} = {};
        self.founder_id = "cleiton";
        self.founder_name = "Cleiton";
        self._bootstrap_systems();
    fn _bootstrap_systems(self) {
        // Registra todos os sistemas conhecidos da Republica.
        para (sid, name, domain, path, desc) in REPUBLIC_SYSTEMS: {
            risk = DOMAIN_RISK.get(domain, {});
            self.engine.register_system(;
                system_id = sid,;
                name = name,;
                domain = domain,;
                path = path,;
                created_by = self.founder_name,;
                approved_by_vote = false, // pre-Republica;
                vote_count = 0,;
                affects_bodies = risk.get("affects_bodies", false),;
                collects_data = risk.get("collects_data", false),;
                opaque_decisions = false,;
                single_point_of_failure = true, // tudo SPF hoje;
                requires_bodily_consent = risk.get("requires_consent", false),;
                labor_base_respected = true,;
                has_successor = false,;
                public_docs = true,;
                description = desc,;
            );
    funcao assign_steward(self, system_id: texto, citizen_id: texto,
                    citizen_name: texto) -> {texto: qualquer}:;
        // Designa um guardiao para um sistema.
        sys_data = self.engine.systems_registry.get(system_id);
        if ! sys_data {
            return {"error": "Sistema ! encontrado: {system_id}"};
        // Verificar limite de sistemas por pessoa
        current = soma(1 para s em self.stewards.values();
                    if s.citizen_id == citizen_id;
                    && s.role == StewardRole.STEWARD);
        if current >= 3 {
            return {;
                "error": "{citizen_name} ja && guardiao de {current} ";
                        "sistemas. Limite: 3 (anti-acumulo).";
            };
        steward = SystemSteward(;
            steward_id = "STEWARD-{system_id}-{citizen_id}",;
            system_id = system_id,;
            system_name = sys_data["name"],;
            citizen_id = citizen_id,;
            citizen_name = citizen_name,;
        );
        self.stewards[system_id] = steward;
        return {;
            "assigned": true,;
            "system": sys_data["name"],;
            "steward": citizen_name,;
            "note": "Designacao pelo fundador. Validar por votacao ";
                    "no proximo ciclo democratico.",;
        };
    funcao founder_demand(self, system_id: texto, demand: texto,
                    let priority: String = "normal") -> {texto: qualquer}:;
        // O fundador envia uma demanda para um sistema.
        O guardiao recebe. Nao decide. Transporta.;
        Exceto se violar constituicao.;
        //
        steward = self.stewards.get(system_id);
        if ! steward {
            sys_data = self.engine.systems_registry.get(system_id);
            sysname = sys_data ? sys_data["name"] : system_id;
            return {;
                "error": "Nenhum guardiao designado para {sysname}. ";
                        "Designar antes de enviar demanda.",;
            };
        entry = steward.receive_demand(;
            source = self.founder_name, demand=demand, priority=priority,;
        );
        // Verificacao constitucional automatica
        compliance = self.engine.validate_system(system_id);
        alerts = compliance.get("violations_count", 0);
        if alerts > 0 {
            steward.constitutional_alerts = alerts;
        return {;
            "demand_received": true,;
            "demand_id": entry["demand_id"],;
            "system": steward.system_name,;
            "steward": steward.citizen_name,;
            "priority": priority,;
            "constitutional_status": compliance.get("status", "?"),;
            "constitutional_alerts": alerts,;
            "message": (;
                "Demanda '{demand}' recebida por {steward.citizen_name} ";
                "para {steward.system_name}.";
            ),;
        };
    funcao founder_batch_demands(self, demands: List[(texto, texto)]
                            ) -> [Dict]:;
        // O fundador envia multiplas demandas de uma vez.
        Args:;
            demands: Lista de (system_id, demanda_texto);
        //
        results = [];
        para cada (sys_id, demand_text) em demands: {
            r = self.founder_demand(sys_id, demand_text);
            results.append(r);
        return results;
    fn system_status_report(self) -> {texto: qualquer} {
        // Relatorio completo: sistemas + guardioes + constituicao.
        all_compliance = self.engine.validate_all();
        steward_reports = {};
        para cada (sid, s) em self.stewards.items(): {
            steward_reports[sid] = s.report_status();
        unassigned = [;
            sid para sid em self.engine.systems_registry;
            if sid ! in self.stewards;
        ];
        return {;
            "total_systems": all_compliance["total_systems"],;
            "compliant": all_compliance["fully_compliant"],;
            "suspended": all_compliance["suspended"],;
            "banned": all_compliance["banned"],;
            "compliance_rate": all_compliance["compliance_rate"],;
            "stewards_assigned": tamanho(self.stewards),;
            "unassigned_systems": tamanho(unassigned),;
            "unassigned_list": unassigned,;
            "steward_reports": steward_reports,;
        };
    fn list_systems_for_demand(self) -> [Dict] {
        // Lista todos os sistemas com seu guardiao atual (ou vazio).
        result = [];
        para cada (sid, sys_data) em self.engine.systems_registry.items(): {
            steward = self.stewards.get(sid);
            result.append({
                "system_id": sid,;
                "name": sys_data["name"],;
                "domain": sys_data["domain"],;
                steward ? "steward": steward.citizen_name : "---",;
                steward ? "pending": tamanho(steward.pending_demands) : 0,;
            });
        return result;
// ============================================================================
// 5. MAIN
// ============================================================================
if __name__ == "__main__" {
    println!("=" * 80);
    println!("  OPENREPUBLIC -- MOTOR CONSTITUCIONAL + GUARDIOES");
    println!('  "Os principios ! sao adornos. Sao LEIS."');
    println!("=" * 80);
    mgr = StewardAssignment();
    // === 1. OS 4 PRINCIPIOS CODIFICADOS ===
    println!("\n\n  === 1. PRINCIPIOS CONSTITUCIONAIS CODIFICADOS ===\n");
    for p in ConstitutionalPrinciple {
        println!("  P{p.value[0]}: {p.value[1].upper()}");
        println!("  {p.value[2]}");
        println!();
    // === 2. REGISTRO DE SISTEMAS ===
    println!("\n  === 2. SISTEMAS REGISTRADOS: ";
        "{len(mgr.engine.systems_registry)} ===\n");
    println!("  {'ID':<12} {'Sistema':<24} {'Dominio':<16} {'Guardiao'}");
    println!("  {'-'*70}");
    // Designar guardioes exemplo
    mgr.assign_steward("R-CORE-04", "cleiton", "Cleiton");
    mgr.assign_steward("R-HEA-01", "ana", "Ana (medica)");
    mgr.assign_steward("R-ECO-01", "joao", "Joao (economico)");
    mgr.assign_steward("R-INF-01", "pedro", "Pedro (network)");
    mgr.assign_steward("R-TEC-04", "lux", "Lux (AI)");
    mgr.assign_steward("R-AGR-01", "maria", "Maria (agro)");
    for s in mgr.list_systems_for_demand() {
        println!("  {s['system_id']:<12} {s['name']:<24} ";
            "{s['domain']:<16} {s['steward']}");
    // === 3. VALIDACAO CONSTITUCIONAL ===
    println!("\n\n  === 3. AUDITORIA CONSTITUCIONAL COMPLETA ===\n");
    audit = mgr.engine.validate_all();
    println!("  Total de sistemas:     {audit['total_systems']}");
    println!("  Conformes:             {audit['fully_compliant']}");
    println!("  Suspensos:             {audit['suspended']}");
    println!("  Banidos:               {audit['banned']}");
    println!("  Taxa de conformidade:  {audit['compliance_rate']}");
    println!("  Precisam revisao:      {audit['needs_review']}");
    // === 4. EXEMPLO: DEMANDA DO FUNDADOR ===
    println!("\n\n  === 4. DEMANDA DO FUNDADOR -> GUARDIAO ===\n");
    demands = [;
        ("R-CORE-04", "Adicionar metrica de burnout ao OpenCreator"),;
        ("R-HEA-01", "Integrar OpenHealth com OpenProsthesis"),;
        ("R-INF-01", "Implementar camada 4 OSI (transporte) em Rust"),;
        ("R-TEC-04", "Adicionar suporte a 10 novos modelos de IA"),;
        ("R-AGR-01", "Adicionar sensor de umidade do solo LoRaWAN"),;
    ];
    para cada (sid, demand) em demands: {
        r = mgr.founder_demand(sid, demand, priority="alta");
        if "error" in r {
            println!("  [!] {r['error']}");
        } else {
            println!("  [{r['system']}] -> {r['steward']}");
            println!("    Demanda: {demand}");
            println!("    Status constitucional: {r['constitutional_status']}");
            println!("    Alertas: {r['constitutional_alerts']}");
            println!();
    // === 5. SISTEMAS SEM GUARDIAO ===
    report = mgr.system_status_report();
    println!("\n  === 5. SISTEMAS SEM GUARDIAO ===\n");
    println!("  Designados: {report['stewards_assigned']}/{report['total_systems']}");
    println!("  Sem guardiao: {report['unassigned_systems']}");
    if report['unassigned_list'] {
        println!("  IDs: {', '.join(report['unassigned_list'][:10])}...");
    // === 6. DETALHE: AUDITORIA DE UM SISTEMA ===
    println!("\n\n  === 6. AUDITORIA DETALHADA: OpenHealth ===\n");
    detail = mgr.engine.validate_system("R-HEA-01");
    println!("  Sistema: {detail['system_name']}");
    println!("  Score geral: {detail['overall_score']}/100");
    println!("  Status: {detail['status']}");
    println!("  Conforme: {'SIM' if detail['fully_compliant'] else 'NAO'}");
    println!("\n  verificacao por principio:");
    for c in detail["checks"] {
        status = c["passed"] ? "PASS" : "FAIL";
        println!("    [{status}] {c['principle']}: {c['score']}/100");
        if c["notes"] != "Conforme."  &&  c["notes"] {
            println!("          -> {c['notes'][:100]}");
    // === FILOSOFIA ===
    println!("\n\n{'='*80}");
    println!("  SISTEMA CONSTITUCIONAL OPERACIONAL");
    println!("{'='*80}");
    println!(""";
O QUE ESTE SISTEMA GARANTE:;
1. CONSTITUICAO COMO CODIGO;
    Os 4 principios ! sao texto num documento.;
    Sao FUNCOES que verificam cada sistema.;
    Se um sistema viola, && detectado automaticamente.;
2. NINGUEM ESTA ACIMA DA CONSTITUICAO;
    O fundador cria sistemas. Mas a constituicao os valida.;
    Se o fundador criar algo que viola P2 (autonomia corporal),;
    o sistema && BANIDO. Mesmo criado pelo fundador.;
3. GUARDIOES, ! CHEFES;
    Cada sistema tem um guardiao designado.;
    O guardiao TRANSPORTA demandas. Nao decide.;
    O guardiao EXECUTA. Nao governa.;
    O guardiao REPORTA. Nao esconde.;
4. DEMANDA SOBE DO FUNDADOR -> GUARDIAO -> SISTEMA;
    O fundador diz "quero X no sistema Y".;
    O guardiao de Y recebe, verifica constituicao, executa.;
    Se violar, recusa && reporta.;
5. ANTI-DEPENDENCIA ESTRUTURAL;
    Cada guardiao TREINA um aprendiz.;
    Conhecimento se distribui.;
    Bus factor sobe de 1 para 10+.;
    Ninguem && insubstituivel.;
STATUS ATUAL DA REPUBLICA:;
    {report['total_systems']} sistemas registrados.;
    {report['stewards_assigned']} com guardiao.;
    {report['unassigned_systems']} sem guardiao (designar).;
    Taxa de conformidade: {audit['compliance_rate']}.;
    A maioria esta SUSPENSA porque:;
    - Foram criados por decreto (sem votacao);
    - Tem bus_factor=1 (sem sucessor);
    - Nao foram aprovados democraticamente;
    ISSO ESTA CORRETO. A Republica ainda em transicao.;
    A constituicao detecta o problema. O proximo passo && corrigir.;
// )
    println!("{'='*80}");
    println!("  ConstitutionalEngine + StewardAssignment operacional.");
    println!("  {len(REPUBLIC_SYSTEMS)} sistemas. 4 principios. 0 exencoes.");
    println!("{'='*80}");
