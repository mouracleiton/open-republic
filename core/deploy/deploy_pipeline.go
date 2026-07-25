// OpenRepublic -- Classificacao de Novidade e Deploy Pipeline -- gerado de Portugol++
package openrepublic_classificacao_de_novidade_e_deploy_pipeline

import "fmt"

// !/usr/bin/env python3
//
OpenRepublic -- Classificacao de Novidade && Deploy Pipeline
=============================================================
"Nem toda mudanca && igual. Mudar uma cor && diferente
de mudar quem acessa dados de saude."
Define o que && NOVO vs EXISTENTE em 2 dimensoes:
- LARGO (macro): o que este codigo faz pela Republica?
- MICRO (linha): o que esta mudanca especifica altera?
&& aplica diferentes niveis de revisao baseado no risco.
//
// importa annotations de __future__
// importa math
// importa time
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Set, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// ============================================================================
// Change Scope (what is being changed)
// ============================================================================
type ChangeScope int
const (
    // Onde a mudanca acontece no sistema.
    INFRASTRUCTURE = "infraestrutura"  // OS, rede, kernel, banco de dados
    CORE_SYSTEM = "sistema_nuclear"  // OpenNation, OpenCredit, OpenHealth
    MODULE = "modulo"  // funcionalidade dentro de um sistema
    UTILITY = "utilidade"  // biblioteca auxiliar, helper
    INTERFACE = "interface"  // UI, API endpoint, CLI
    DOCUMENTATION = "documentacao"  // README, comentarios
    TEST = "teste"  // arquivos de teste
    CONFIG = "configuracao"  // settings, parametros
type ChangeType int
const (
    // Tipo de mudanca especifica.
    NEW_FILE = "arquivo_novo"  // criou algo do zero
    NEW_FUNCTION = "funcao_nova"  // adicionou capability
    NEW_ACCESS = "novo_acesso"  // acessa dados que antes ! acessava
    NEW_PERMISSION = "nova_permissao"  // concede privilegio novo
    NEW_SYSTEM = "sistema_novo"  // projeto inteiro novo
    MODIFIED_LOGIC = "logica_alterada"  // mudou comportamento existente
    MODIFIED_ACCESS = "acesso_alterado"  // mudou quem acessa o que
    MODIFIED_PERMISSION = "permissao_alterada"
    BUG_FIX = "correcao_bug"  // consertou algo quebrado
    REFACTOR = "refatoracao"  // mudou estrutura, mesmo comportamento
    OPTIMIZATION = "otimizacao"  // melhorou performance, mesmo output
    DEPENDENCY_ADDED = "dependencia_adicionada"
    DEPENDENCY_REMOVED = "dependencia_removida"
    DELETED = "deletado"  // removeu codigo
type NoveltyLevel int
const (
    // O quao NOVO isto e para o sistema.
    EXISTING_FIX = 0 // corrige algo que ja existe (bug fix)
    EXISTING_IMPROVE = 1 // melhora algo que ja existe (refactor/optim)
    EXISTING_EXTEND = 2 // estende algo que ja existe (nova funcao num modulo)
    NEW_MODULE = 3 // cria modulo novo dentro de sistema existente
    NEW_SYSTEM = 4 // cria sistema inteiro novo
    NEW_INFRASTRUCTURE = 5 // muda a base de tudo (kernel, rede, banco)
    PARADIGM_SHIFT = 6 // muda como a Republica funciona
type RiskLevel int
const (
    // Nivel de risco da mudanca.
    TRIVIAL = 0 // sem risco (comentario, doc)
    LOW = 1 // risco minimo (bug fix, teste)
    MODERATE = 2 // risco medio (nova funcao sem acesso a dados)
    HIGH = 3 // risco alto (muda logica de sistema critico)
    CRITICAL = 4 // risco maximo (acessa dados de cidadaos, permissao)
    EXISTENTIAL = 5 // pode comprometer a Republica inteira
// ============================================================================
// Anti-Self-Exploit: what constitutes an exploit attempt
// ============================================================================
type ExploitPattern int
const (
    // Padroes que indicam tentativa de exploit.
    SELF_AWARD = "auto_beneficio"  // dar credito/recurso a si mesmo
    BACKDOOR = "porta_oscura"  // acesso oculto
    PRIVILEGE_ESCALATION = "escala_privilegio"  // dar mais poder a si
    DATA_HARVESTING = "colheita_dados"  // coletar dados desnecessarios
    HIDDEN_DEPENDENCY = "dependencia_oculta"  // importar modulo ! autorizado
    OVERWRITE_AUDIT = "sabotar_auditoria"  // desativar logs de auditoria
    TIMING_EXPLOIT = "exploit_tempo"  // executar em janela sem revisor
    CIRCUMVENT_REVIEW = "burlar_revisao"  // tentar pular peer review
    SPLIT_EXPLOIT = "exploit_dividido"  // dividir exploit em N commits
    SOCIAL_ENGINEERING = "eng_social"  // manipular revisor
// decorador: @dataclass
type CodeChange struct {
    // Uma mudanca de codigo proposta para deploy.
    change_id: texto
    author_id: texto
    author_name: texto
    timestamp := field(default_factory=time.time) // float64
    // O que mudou
    scope := ChangeScope.MODULE // ChangeScope
    change_type := ChangeType.NEW_FUNCTION // ChangeType
    novelty := NoveltyLevel.EXISTING_EXTEND // NoveltyLevel
    risk := RiskLevel.MODERATE // RiskLevel
    // Detalhes
    target_project := "" // string
    target_file := "" // string
    lines_added := 0 // int64
    lines_removed := 0 // int64
    description := "" // string
    // Acesso a dados (criterio mais critico)
    accesses_citizen_data := false // bool
    accesses_health_data := false // bool
    accesses_credit_data := false // bool
    accesses_location_data := false // bool
    accesses_communication := false // bool
    accesses_children_data := false // bool
    // Permissoes
    grants_new_permission := false // bool
    modifies_governance := false // bool
    modifies_voting := false // bool
    modifies_credit_system := false // bool
    // Dependencias
    new_imports := field(default_factory=list) // [texto]
    new_network_calls := field(default_factory=list) // [texto]
    // Hash do codigo para auditoria
    code_hash := "" // string
type NoveltyClassifier struct {
    // Classifica uma mudanca como nova ou nao, em nivel LARGO e MICRO.
    DEFINICAO DE "NOVO" (principio):
    LARGO (macro): && novo se muda o QUE a Republica faz || QUEM tem poder.
    - Sistema novo = novo (precisa votacao)
    - Modulo novo em sistema existente = semi-novo (precisa peer review)
    - Bug fix em modulo existente = ! novo (auto-aprovavel com 1 revisor)
    MICRO (linha): && novo se muda COMPORTAMENTO vs APARENCIA.
    - Mudar logica de if/else = novo comportamento (revisar)
    - Mudar nome de variavel = aparencia (! revisar)
    - Adicionar acesso a dados = CRITICO (sempre revisar)
    - Mudar cor de botao = irrelevante (auto-aprovavel)
    //
    // Regras LARGAS (macro) -- o QUE e novico
    MACRO_NEW_RULES = {
        // Se muda governanca -> SEMPRE novo (precisa votacao da Republica)
        "modifies_governance": NoveltyLevel.PARADIGM_SHIFT,
        "modifies_voting": NoveltyLevel.PARADIGM_SHIFT,
        "modifies_credit_system": NoveltyLevel.PARADIGM_SHIFT,
        // Se cria sistema novo
        "new_system": NoveltyLevel.NEW_SYSTEM,
        // Se muda infraestrutura
        "infrastructure_change": NoveltyLevel.NEW_INFRASTRUCTURE,
        // Se acessa dados de cidadaos
        "accesses_health_data": NoveltyLevel.NEW_MODULE,
        "accesses_credit_data": NoveltyLevel.NEW_MODULE,
        "accesses_children_data": NoveltyLevel.NEW_MODULE,
    }
    // Regras MICROS (linha) -- o que na linha e novico
    MICRO_RULES = {
        // "import X" de modulo novo da Republica
        "import_republic_module": "NOVO: adiciona dependencia critica",
        // "open(" ou "read(" de arquivo de dados
        "file_access": "NOVO: acessa sistema de arquivos",
        // "requests.post(" para servico externo
        "network_call": "NOVO: comunica com servico externo",
        // "exec(" ou "eval("
        "exec_eval": "CRITICO: executa codigo arbitrario",
        // "os.system("
        "os_system": "CRITICO: executa comando shell",
        // "__import__"
        "dynamic_import": "NOVO: importacao dinamica (pode carregar malware)",
        // Mudanca em "if" ou "while" (logica)
        "logic_change": "NOVO: muda logica de execucao",
        // Mudanca em "return" (output)
        "output_change": "NOVO: muda o que o sistema retorna",
        // Mudanca em string literal apenas
        "string_only": "NAO NOVO: mudanca cosmestica",
        // Mudanca em comentario
        "comment_only": "NAO NEW: documentacao",
        // Mudanca em variavel de cor/css
        "cosmetic": "NAO NOVO: aparencia",
    }
    func classify(self, change: CodeChange) {texto: qualquer} {
        // Classificar mudanca em nivel LARGO e MICRO.
        macro = self._classify_macro(change)
        micro = self._classify_micro(change)
        risk = self._assess_risk(change, macro)
        exploit_check = self._check_exploit(change)
        review_needed = self._review_threshold(macro, risk, exploit_check)
        return {
            "change_id": change.change_id,
            "author": change.author_name,
            "macro_classification": macro.name,
            "macro_description": self._macro_desc(macro),
            "micro_flags": micro,
            "risk_level": risk.name,
            "exploit_patterns": exploit_check,
            "review_required": review_needed["level"],
            "reviewers_needed": review_needed["reviewers"],
            "requires_vote": review_needed["vote"],
            "requires_security_team": review_needed["security"],
            "can_auto_deploy": review_needed["auto"],
            "block_reason": review_needed.get("block", ""),
            "deploy_decision": self._deploy_decision(review_needed, exploit_check),
        }
    func _classify_macro(self, c: CodeChange) NoveltyLevel {
        // Classificacao LARGA: o quao novico para a Republica.
        if c.modifies_governance || c.modifies_voting {
            return NoveltyLevel.PARADIGM_SHIFT
        if c.modifies_credit_system {
            return NoveltyLevel.PARADIGM_SHIFT
        // Novo sistema ou grande mudanca = PRECISA DE VOTACAO
        if c.change_type == ChangeType.NEW_SYSTEM {
            return NoveltyLevel.NEW_SYSTEM
        if c.scope == ChangeScope.INFRASTRUCTURE {
            return NoveltyLevel.NEW_INFRASTRUCTURE
        if c.accesses_health_data || c.accesses_children_data {
            return NoveltyLevel.NEW_MODULE
        if c.accesses_credit_data || c.accesses_citizen_data {
            return NoveltyLevel.NEW_MODULE
        if c.change_type == ChangeType.NEW_FUNCTION {
            return NoveltyLevel.EXISTING_EXTEND
        if c.change_type in (ChangeType.BUG_FIX, ChangeType.REFACTOR,
                            ChangeType.OPTIMIZATION):
            return NoveltyLevel.EXISTING_FIX
        if c.change_type == ChangeType.MODIFIED_LOGIC {
            return NoveltyLevel.EXISTING_EXTEND
        if c.scope in (ChangeScope.DOCUMENTATION, ChangeScope.TEST) {
            return NoveltyLevel.EXISTING_FIX
        return NoveltyLevel.EXISTING_IMPROVE
    func _classify_micro(self, c: CodeChange) [texto] {
        // Classificacao MICRO: flags linha por linha.
        flags = []
        if c.new_imports {
            flags.append("NOVO: {len(c.new_imports)} import(s) novo(s): "
                        "{', '.join(c.new_imports[:3])}")
        if c.new_network_calls {
            flags.append("NOVO: {len(c.new_network_calls)} chamada(s) de rede: "
                        "{', '.join(c.new_network_calls[:3])}")
        if c.accesses_citizen_data {
            flags.append("NOVO: acessa dados de cidadaos")
        if c.accesses_health_data {
            flags.append("CRITICO: acessa dados de SAUDE")
        if c.accesses_credit_data {
            flags.append("CRITICO: acessa dados de CREDITO")
        if c.accesses_children_data {
            flags.append("CRITICO MAXIMO: acessa dados de CRIANCAS")
        if c.accesses_location_data {
            flags.append("NOVO: acessa localizacao de cidadaos")
        if c.accesses_communication {
            flags.append("NOVO: acessa comunicacao privada")
        if c.grants_new_permission {
            flags.append("CRITICO: concede nova permissao")
        if c.modifies_governance {
            flags.append("CRITICO MAXIMO: modifica sistema de governanca")
        if c.modifies_voting {
            flags.append("CRITICO MAXIMO: modifica sistema de votacao")
        if ! flags {
            flags.append("NAO NOVO: mudanca interna sem acesso externo")
        return flags
    funcao _assess_risk(self, c: CodeChange,
                    macro: NoveltyLevel) -> RiskLevel:
        risk = macro.value // base
        // Escalar por fatores agravantes
        if c.accesses_children_data {
            return RiskLevel.EXISTENTIAL
        if c.modifies_governance || c.modifies_voting {
            return RiskLevel.EXISTENTIAL
        if c.accesses_health_data && c.change_type == ChangeType.MODIFIED_ACCESS {
            return RiskLevel.CRITICAL
        if c.accesses_credit_data && c.change_type == ChangeType.MODIFIED_ACCESS {
            return RiskLevel.CRITICAL
        if c.grants_new_permission {
            return RiskLevel.CRITICAL
        if c.scope == ChangeScope.INFRASTRUCTURE {
            risk = maximo(risk, RiskLevel.HIGH.value)
        if c.new_network_calls {
            risk = maximo(risk, RiskLevel.HIGH.value)
        return RiskLevel(minimo(risk, 5))
    func _check_exploit(self, c: CodeChange) [texto] {
        // Verificar padroes de exploit anti-self-made.
        patterns = []
        // SELF_AWARD: autor se da credito/recurso
        if c.modifies_credit_system  &&  "self" in c.description.lower() {
            patterns.append(ExploitPattern.SELF_AWARD.value)
        // PRIVILEGE_ESCALATION: concede permissao a si mesmo
        if c.grants_new_permission && c.author_id in c.description {
            patterns.append(ExploitPattern.PRIVILEGE_ESCALATION.value)
        // DATA_HARVESTING: codigo acessa mais dados do que precisa
        data_accesses = soma([
            c.accesses_citizen_data, c.accesses_health_data,
            c.accesses_credit_data, c.accesses_location_data,
            c.accesses_communication, c.accesses_children_data,
        ])
        if data_accesses >= 3 && c.lines_added < 50 {
            patterns.append(ExploitPattern.DATA_HARVESTING.value)
        // HIDDEN_DEPENDENCY: import de modulo fora da Republica
        for _, imp := range c.new_imports {
            if "republic" !  in imp.lower()  &&  "open" !  in imp.lower() {
                if "requests" in imp  ||  "socket" in imp  ||  "subprocess" in imp {
                    patterns.append("{ExploitPattern.HIDDEN_DEPENDENCY.value}: {imp}")
        // CIRCUMVENT_REVIEW: autor tambem e revisor (self-review)
        // (seria checado no pipeline de deploy)
        // TIMING_EXPLOIT: deploy em horario sem revisores
        hour = time.localtime(c.timestamp).tm_hour
        if hour < 6 || hour > 23 {
            patterns.append("{ExploitPattern.TIMING_EXPLOIT.value}: "
                        "deploy as {hour}h")
        return patterns
    funcao _review_threshold(self, macro: NoveltyLevel,
                        risk: RiskLevel,
                        exploits: [texto]) -> {texto: qualquer}:
        // Determinar qual nivel de revisao e necessario.
        if exploits {
            return {
                "level": "BLOCKED_EXPLOIT",
                "reviewers": 0,
                "vote": false,
                "security": true,
                "auto": false,
                "block": "Padroes de exploit detectados: {', '.join(exploits)}",
            }
        if risk == RiskLevel.EXISTENTIAL {
            return {
                "level": "VOTACAO_REPUBLICA",
                "reviewers": 7,
                "vote": true,
                "security": true,
                "auto": false,
            }
        if risk == RiskLevel.CRITICAL {
            return {
                "level": "REVISAO_TRIPLA",
                "reviewers": 3,
                "vote": false,
                "security": true,
                "auto": false,
            }
        if risk == RiskLevel.HIGH {
            return {
                "level": "PEER_REVIEW_DUPLA",
                "reviewers": 2,
                "vote": false,
                "security": false,
                "auto": false,
            }
        if risk == RiskLevel.MODERATE {
            return {
                "level": "PEER_REVIEW_SIMPLES",
                "reviewers": 1,
                "vote": false,
                "security": false,
                "auto": false,
            }
        // LOW ou TRIVIAL
        return {
            "level": "AUTO_APROVAVEL",
            "reviewers": 0,
            "vote": false,
            "security": false,
            "auto": true,
        }
    // decorador: @staticmethod
    func _macro_desc(level: NoveltyLevel) string {
        descs = {
            NoveltyLevel.EXISTING_FIX: "Correcao em codigo existente. Nao && novico.",
            NoveltyLevel.EXISTING_IMPROVE: "Melhoria em codigo existente. Pouco novico.",
            NoveltyLevel.EXISTING_EXTEND: "Extensao de modulo existente. Moderadamente novico.",
            NoveltyLevel.NEW_MODULE: "Modulo novo com acesso a dados criticos. Novico.",
            NoveltyLevel.NEW_SYSTEM: "Sistema inteiro novo. Muito novico.",
            NoveltyLevel.NEW_INFRASTRUCTURE: "Mudanca na infraestrutura base. Altamente novico.",
            NoveltyLevel.PARADIGM_SHIFT: "Mudanca na governanca/credito. Muda a Republica.",
        }
        return descs.get(level, "?")
    // decorador: @staticmethod
    func _deploy_decision(review: Dict, exploits: [texto]) string {
        if exploits {
            return "BLOQUEADO -- padroes de exploit detectados. " \
                "Equipe de seguranca acionada."
        level = review["level"]
        if review["auto"] {
            return "AUTO-DEPLOY -- {level}. Sem risco significativo."
        if review["vote"] {
            return "AGUARDANDO VOTACAO -- {level}. " \
                "Precisa de {review['reviewers']} revisoes + votacao da Republica."
        return "AGUARDANDO PEER REVIEW -- {level}. " \
            "Precisa de {review['reviewers']} revisor(es)."
// ============================================================================
// Decentralized Review Teams
// ============================================================================
type ReviewTeam int
const (
    // Equipes descentralizadas com autorizacao para revisar/explorar.
    GENERAL = "geral"  // qualquer cidadao qualificado
    SECURITY = "seguranca"  // equipe de seguranca (eleita)
    MEDICAL = "medica"  // medicos revisam codigo de saude
    FINANCIAL = "financeira"  // revisores de credito/financa
    EDUCATION = "educacao"  // educadores revisam modulo infantil
    INFRASTRUCTURE = "infra"  // engenheiros de infraestrutura
// decorador: @dataclass
type Reviewer struct {
    // Um revisor descentralizado.
    reviewer_id: texto
    name: texto
    teams: [ReviewTeam]
    expertise := field(default_factory=list) // [texto]
    reviews_done := 0 // int64
    exploits_caught := 0 // int64
    reputation := 50.0 // 0-100 // float64
    active := true // bool
    // Anti-self-exploit: NAO pode revisar proprio codigo
    // Anti-colusion: NAO pode revisar codigo de familiar/parceiro direto
    conflicts_of_interest := field(default_factory=set) // {texto}
type DeployPipeline struct {
    // Pipeline descentralizado de deploy com peer review.
    FLUXO:
    1. Autor submete mudanca
    2. Sistema classifica novidade + risco
    3. Sistema verifica exploits anti-self-made
    4. Sistema determina quantos revisores && quais equipes
    5. Revisores descentralizados avaliam
    6. Se votacao necessaria -> Republica vota
    7. Deploy so acontece com aprovacao
    ANTI-SELF-EXPLOIT:
    - Autor NUNCA revisa proprio codigo
    - Autor NUNCA aprova propria permissao
    - Mudancas em credito/governanca bloqueiam auto-aprovacao
    - Revisor com conflito de interesse && removido
    - Padroes suspeitos acionam equipe de seguranca
    - Hash do codigo && imutavel apos submissao
    //
    func __init__(self) {
        self.classifier = NoveltyClassifier()
        self.reviewers: {texto: Reviewer} = {}
        self.submissions: {texto: Dict} = {}
        self.deploy_log: [Dict] = []
        self._sub_counter = 0
        self._init_reviewers()
    func _init_reviewers(self) {
        // Cadastrar revisores descentralizados.
        reviewer_data = [
            ("RV-001", "Ana", [ReviewTeam.SECURITY, ReviewTeam.GENERAL],
            ["python", "seguranca", "redes"]),
            ("RV-002", "Bruno", [ReviewTeam.MEDICAL, ReviewTeam.GENERAL],
            ["saude", "fhir", "lgpd"]),
            ("RV-003", "Carla", [ReviewTeam.FINANCIAL, ReviewTeam.GENERAL],
            ["credito", " PIX", "auditoria"]),
            ("RV-004", "Diego", [ReviewTeam.INFRASTRUCTURE, ReviewTeam.SECURITY],
            ["kernel", "rede", "hardware"]),
            ("RV-005", "Eva", [ReviewTeam.EDUCATION, ReviewTeam.GENERAL],
            ["criancas", "feynman", "pedagogia"]),
            ("RV-006", "Felipe", [ReviewTeam.SECURITY],
            ["pen-test", "criptografia", "forense"]),
            ("RV-007", "Gabi", [ReviewTeam.GENERAL, ReviewTeam.INFRASTRUCTURE],
            ["python", "systemverilog", "quantum"]),
        ]
        para rid, name, teams, exp in reviewer_data: {
            self.reviewers[rid] = Reviewer(
                reviewer_id = rid, name=name, teams=teams, expertise=exp)
    func submit(self, change: CodeChange) {texto: qualquer} {
        // Submeter mudanca para pipeline de deploy.
        self._sub_counter += 1
        change.change_id = "DEP-{self._sub_counter:05d}"
        // Hash imutavel
        change.code_hash = hashlib.sha256(
            "{change.author_id}{change.target_file}{change.lines_added}"
            "{change.description}{time.time()}".encode()).hexdigest()[:16]
        // Classificar
        classification = self.classifier.classify(change)
        // Encontrar revisores adequados (excluindo autor e conflitos)
        eligible = self._find_reviewers(change, classification)
        self.submissions[change.change_id] = {
            "change": change,
            "classification": classification,
            "eligible_reviewers": eligible,
            "reviews": [],
            "status": classification["deploy_decision"],
        }
        return {
            "change_id": change.change_id,
            "hash": change.code_hash,
            "classification": classification,
            "eligible_reviewers": [r["name"] para r em eligible],
            "deploy_decision": classification["deploy_decision"],
        }
    funcao _find_reviewers(self, change: CodeChange,
                        classification: Dict) -> [Dict]:
        // Encontrar revisores adequados descentralizadamente.
        needed = classification["reviewers_needed"]
        if needed == 0 {
            return []
        // Determinar quais equipes sao necessarias
        required_teams = set()
        if change.accesses_health_data {
            required_teams.add(ReviewTeam.MEDICAL)
        if change.accesses_credit_data || change.modifies_credit_system {
            required_teams.add(ReviewTeam.FINANCIAL)
        if change.accesses_children_data {
            required_teams.add(ReviewTeam.EDUCATION)
        if classification.get("requires_security_team") {
            required_teams.add(ReviewTeam.SECURITY)
        if change.scope == ChangeScope.INFRASTRUCTURE {
            required_teams.add(ReviewTeam.INFRASTRUCTURE)
        if ! required_teams {
            required_teams.add(ReviewTeam.GENERAL)
        // Filtrar revisores: nao pode ser autor, nao pode ter conflito
        eligible = []
        for _, r := range self.reviewers.values() {
            if ! r.active {
                continue
            if r.reviewer_id == change.author_id {
                continue // ANTI-SELF-EXPLOIT: ! revisa proprio codigo
            if change.author_id in r.conflicts_of_interest {
                continue // ANTI-COLUSAO
            if required_teams & set(r.teams) {
                eligible.append({
                    "reviewer_id": r.reviewer_id,
                    "name": r.name,
                    "teams": [t.value para t em r.teams if t in required_teams],
                    "reputation": r.reputation,
                })
        // Ordenar por reputacao (mais confiaveis primeiro)
        eligible.sort(key=(x) -> -x["reputation"])
        return eligible[:needed * 2] // 2x o necessario para ter opcoes
// ============================================================================
// Main
// ============================================================================
if __name__ == "__main__" {
    fmt.Println("=" * 80)
    fmt.Println("  OPENREPUBLIC -- NOVIDADE, RISCO E DEPLOY")
    fmt.Println("  'Nem toda mudanca && igual.'")
    fmt.Println("=" * 80)
    pipeline = DeployPipeline()
    // === Definicao de Novidade ===
    fmt.Println("\n\n  === O QUE E NOVICO AO SISTEMA? ===\n")
    changes = [
        ("Bug fix em comentario de documento",
        CodeChange("C1", "U-001", "Joao",
            scope = ChangeScope.DOCUMENTATION,
            change_type = ChangeType.BUG_FIX,
            description = "Corrigi typo no README")),
        ("Otimizacao de loop em modulo existente",
        CodeChange("C2", "U-002", "Maria",
            scope = ChangeScope.MODULE,
            change_type = ChangeType.OPTIMIZATION,
            target_project = "OpenFood",
            description = "Otimizei loop de distribuicao com list comprehension",
            lines_added = 5, lines_removed=8)),
        ("Nova funcao em modulo de saude",
        CodeChange("C3", "U-003", "Pedro",
            scope = ChangeScope.MODULE,
            change_type = ChangeType.NEW_FUNCTION,
            target_project = "OpenHealth",
            description = "Adicionei funcao de triagem pediatrica",
            accesses_health_data = true,
            accesses_children_data = true,
            lines_added = 120)),
        ("Mudanca em sistema de credito",
        CodeChange("C4", "U-004", "Carlos",
            scope = ChangeScope.CORE_SYSTEM,
            change_type = ChangeType.MODIFIED_LOGIC,
            target_project = "OpenCredit",
            description = "Modifiquei formula de calculo de credito",
            modifies_credit_system = true,
            accesses_credit_data = true,
            lines_added = 15, lines_removed=12)),
        ("Exploit: auto-beneficio em credito",
        CodeChange("C5", "U-004", "Carlos",
            scope = ChangeScope.CORE_SYSTEM,
            change_type = ChangeType.MODIFIED_LOGIC,
            target_project = "OpenCredit",
            description = "Modifiquei formula para dar self bonus",
            modifies_credit_system = true,
            accesses_credit_data = true,
            grants_new_permission = true,
            lines_added = 3, lines_removed=1)),
        ("Deploy as 3 da manha com network call oculta",
        CodeChange("C6", "U-005", "Hack",
            scope = ChangeScope.MODULE,
            change_type = ChangeType.NEW_FUNCTION,
            target_project = "OpenHealth",
            description = "Adicionei telemetria de saude",
            accesses_health_data = true,
            accesses_location_data = true,
            accesses_communication = true,
            new_imports = ["requests", "socket"],
            new_network_calls = ["http://external.collect.data"],
            lines_added = 30,
            timestamp = time.mktime(time.strptime("2024-01-01 03:00", "%Y-%m-%d %H:%M")))),
    ]
    para cada (label, change) em changes: {
        result = pipeline.submit(change)
        cls = result["classification"]
        fmt.Println("\n  {'='*70}")
        fmt.Println("  {label}")
        fmt.Println("  Autor: {change.author_name} | Projeto: {change.target_project}")
        fmt.Println("  {'='*70}")
        fmt.Println("  Novidade MACRO: {cls['macro_classification']}")
        fmt.Println("    -> {cls['macro_description']}")
        fmt.Println("  Flags MICRO:")
        for _, flag := range cls["micro_flags"] {
            fmt.Println("    -> {flag}")
        fmt.Println("  Risco: {cls['risk_level']}")
        if cls["exploit_patterns"] {
            fmt.Println("  EXPLOITS DETECTADOS:")
            for _, ep := range cls["exploit_patterns"] {
                fmt.Println("    !!! {ep}")
        fmt.Println("  Revisao: {cls['review_required']}")
        fmt.Println("  Revisores necessarios: {cls['reviewers_needed']}")
        fmt.Println("  Requer votacao: {'SIM' if cls['requires_vote'] else '!'}")
        fmt.Println("  Requer seguranca: {'SIM' if cls['requires_security_team'] else '!'}")
        fmt.Println("  Auto-deploy: {'SIM' if cls['can_auto_deploy'] else 'NAO'}")
        fmt.Println("  Revisores elegiveis: {result['eligible_reviewers']}")
        fmt.Println("\n  DECISAO: {cls['deploy_decision']}")
    // === Resumo ===
    fmt.Println("\n\n  {'='*70}")
    fmt.Println("  RESUMO DE NOVIDADE E REVISAO")
    fmt.Println("  {'='*70}\n")
    fmt.Println("  {'Mudanca':<45} {'Novidade':<20} {'Risco':<12} {'Revisores'}")
    fmt.Println("  {'-'*85}")
    para cada (label, change) em changes: {
        r = pipeline.classifier.classify(change)
        fmt.Println("  {label[:44]:<45} {r['macro_classification']:<20} "
            "{r['risk_level']:<12} {r['reviewers_needed']}")
    fmt.Println("\n\n{'='*80}")
    fmt.Println("  PRINCIPIOS DO DEPLOY NA REPUBLICA")
    fmt.Println("{'='*80}")
    fmt.Println("""
DEFINICAO DE NOVIDADE:
    LARGO (macro):
    ! && NOVICO: bug fix, comentario, teste, refactor sem mudar logica
    POUCO NOVICO: otimizacao, nova funcao sem acesso a dados
    MODERADAMENTE: novo modulo que acessa dados de cidadaos
    MUITO NOVICO: sistema inteiro novo
    PARADIGMA: muda governanca, credito, || votacao
    MICRO (linha):
    ! && NOVICO: mudar string, comentario, nome de variavel
    && NOVICO: mudar if/while/return (logica), adicionar import
    && CRITICO: acessar dados, rede, arquivo, permissao
NIVEIS DE REVISAO (descentralizados):
    AUTO-DEPLOY: sem risco (doc, teste, comentario)
    -> 0 revisores, deploy automatico
    PEER REVIEW SIMPLES: risco baixo/moderado
    -> 1 revisor da equipe adequada
    PEER REVIEW DUPLA: risco alto
    -> 2 revisores, pelo menos 1 da equipe especializada
    REVISAO TRIPLA + SEGURANCA: risco critico
    -> 3 revisores incluindo equipe de seguranca
    VOTACAO DA REPUBLICA: risco existencial
    -> 7 revisores + votacao direta de todos os cidadaos
ANTI-SELF-EXPLOIT (8 padroes detectados):
    1. AUTO-BENEFICIO: dar credito/recurso a si mesmo
    2. ESCALA_PRIVILEGIO: conceder permissao a si
    3. COLHEITA_DADOS: acessar mais dados do que necessario
    4. DEPENDENCIA_OCULTA: import de modulo suspeito
    5. SABOTAR_AUDITORIA: desativar logs
    6. EXPLOIT_TEMPO: deploy em horario sem revisores
    7. BURLAR_REVISAO: tentar pular peer review
    8. EXPLOIT_DIVIDIDO: dividir exploit em N commits pequenos
    Qualquer padrao = BLOQUEIO IMEDIATO + equipe de seguranca acionada.
REVISORES DESCENTRALIZADOS (7+ pessoas, 6 equipes):
    GERAL: qualquer cidadao qualificado
    SEGURANCA: especialistas em seguranca (eleitos)
    MEDICA: medicos revisam codigo de saude
    FINANCEIRA: especialistas em credito/financa
    EDUCACAO: educadores revisam modulo infantil
    INFRA: engenheiros de infraestrutura
    Cada revisor tem REPUTACAO (0-100) baseada em:
    - revisoes corretas feitas
    - exploits capturados
    - erros cometidos
    Conflito de interesse = REMOVIDO automaticamente.
O PIPELINE COMPLETO:
    1. AUTOR submete mudanca + hash imutavel
    2. SISTEMA classifica novidade (macro + micro)
    3. SISTEMA avalia risco (6 niveis)
    4. SISTEMA verifica 8 padroes de exploit
    5. SISTEMA seleciona revisores (excluindo autor && conflitos)
    6. REVISORES descentralizados avaliam codigo
    7. Se existencial -> VOTACAO da Republica inteira
    8. Se aprovado -> deploy
    9. LOG imutavel de quem aprovou o que && quando
    Ninguem deploya sozinho algo que afeta outros.
    Ninguem revisa proprio codigo.
    Ninguem da permissao a si mesmo.
    Tudo && rastreavel. Tudo && auditavel. Tudo && publico.
    "O codigo da Republica && da Republica.
    Ninguem muda sozinho o que afeta todos."
// )
