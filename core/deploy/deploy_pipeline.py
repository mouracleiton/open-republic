#!/usr/bin/env python3
"""
OpenRepublic -- Classificacao de Novidade e Deploy Pipeline -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenRepublic -- Classificacao de Novidade and Deploy Pipeline
=============================================================
"Nem toda mudanca and igual. Mudar uma cor and diferente
de mudar quem acessa dados de saude."
Define o que and NOVO vs EXISTENTE em 2 dimensoes:
- LARGO (macro): o que este codigo faz pela Republica?
- MICRO (linha): o que esta mudanca especifica altera?
and aplica diferentes niveis de revisao baseado no risco.
# 
# importa annotations de __future__
# importa math
# importa time
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Set, Tuple de typing
# importa Enum de enum
# importa defaultdict de collections
# ============================================================================
# Change Scope (what is being changed)
# ============================================================================
class ChangeScope(Enum):
    # Onde a mudanca acontece no sistema.
    INFRASTRUCTURE = "infraestrutura"  // OS, rede, kernel, banco de dados
    CORE_SYSTEM = "sistema_nuclear"  // OpenNation, OpenCredit, OpenHealth
    MODULE = "modulo"  // funcionalidade dentro de um sistema
    UTILITY = "utilidade"  // biblioteca auxiliar, helper
    INTERFACE = "interface"  // UI, API endpoint, CLI
    DOCUMENTATION = "documentacao"  // README, comentarios
    TEST = "teste"  // arquivos de teste
    CONFIG = "configuracao"  // settings, parametros
class ChangeType(Enum):
    # Tipo de mudanca especifica.
    NEW_FILE = "arquivo_novo"  // criou algo do zero
    NEW_FUNCTION = "funcao_nova"  // adicionou capability
    NEW_ACCESS = "novo_acesso"  // acessa dados que antes not acessava
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
class NoveltyLevel(Enum):
    # O quao NOVO isto e para o sistema.
    EXISTING_FIX = 0 // corrige algo que ja existe (bug fix)
    EXISTING_IMPROVE = 1 // melhora algo que ja existe (refactor/optim)
    EXISTING_EXTEND = 2 // estende algo que ja existe (nova funcao num modulo)
    NEW_MODULE = 3 // cria modulo novo dentro de sistema existente
    NEW_SYSTEM = 4 // cria sistema inteiro novo
    NEW_INFRASTRUCTURE = 5 // muda a base de tudo (kernel, rede, banco)
    PARADIGM_SHIFT = 6 // muda como a Republica funciona
class RiskLevel(Enum):
    # Nivel de risco da mudanca.
    TRIVIAL = 0 // sem risco (comentario, doc)
    LOW = 1 // risco min (bug fix, teste)
    MODERATE = 2 // risco medio (nova funcao sem acesso a dados)
    HIGH = 3 // risco alto (muda logica de sistema critico)
    CRITICAL = 4 // risco max (acessa dados de cidadaos, permissao)
    EXISTENTIAL = 5 // pode comprometer a Republica inteira
# ============================================================================
# Anti-Self-Exploit: what constitutes an exploit attempt
# ============================================================================
class ExploitPattern(Enum):
    # Padroes que indicam tentativa de exploit.
    SELF_AWARD = "auto_beneficio"  // dar credito/recurso a si mesmo
    BACKDOOR = "porta_oscura"  // acesso oculto
    PRIVILEGE_ESCALATION = "escala_privilegio"  // dar mais poder a si
    DATA_HARVESTING = "colheita_dados"  // coletar dados desnecessarios
    HIDDEN_DEPENDENCY = "dependencia_oculta"  // importar modulo not autorizado
    OVERWRITE_AUDIT = "sabotar_auditoria"  // desativar logs de auditoria
    TIMING_EXPLOIT = "exploit_tempo"  // executar em janela sem revisor
    CIRCUMVENT_REVIEW = "burlar_revisao"  // tentar pular peer review
    SPLIT_EXPLOIT = "exploit_dividido"  // dividir exploit em N commits
    SOCIAL_ENGINEERING = "eng_social"  // manipular revisor
# decorador: @dataclass
class CodeChange:
    # Uma mudanca de codigo proposta para deploy.
    change_id: texto
    author_id: texto
    author_name: texto
    timestamp: float = field(default_factory=time.time)
    # O que mudou
    scope: ChangeScope = ChangeScope.MODULE
    change_type: ChangeType = ChangeType.NEW_FUNCTION
    novelty: NoveltyLevel = NoveltyLevel.EXISTING_EXTEND
    risk: RiskLevel = RiskLevel.MODERATE
    # Detalhes
    target_project: str = ""
    target_file: str = ""
    lines_added: int = 0
    lines_removed: int = 0
    description: str = ""
    # Acesso a dados (criterio mais critico)
    accesses_citizen_data: bool = False
    accesses_health_data: bool = False
    accesses_credit_data: bool = False
    accesses_location_data: bool = False
    accesses_communication: bool = False
    accesses_children_data: bool = False
    # Permissoes
    grants_new_permission: bool = False
    modifies_governance: bool = False
    modifies_voting: bool = False
    modifies_credit_system: bool = False
    # Dependencias
    new_imports: [texto] = field(default_factory=list)
    new_network_calls: [texto] = field(default_factory=list)
    # Hash do codigo para auditoria
    code_hash: str = ""
class NoveltyClassifier:
    # Classifica uma mudanca como nova ou nao, em nivel LARGO e MICRO.
    DEFINICAO DE "NOVO" (principio):
    LARGO (macro): and novo se muda o QUE a Republica faz or QUEM tem poder.
    - Sistema novo = novo (precisa votacao)
    - Modulo novo em sistema existente = semi-novo (precisa peer review)
    - Bug fix em modulo existente = not novo (auto-aprovavel com 1 revisor)
    MICRO (linha): and novo se muda COMPORTAMENTO vs APARENCIA.
    - Mudar logica de if/else = novo comportamento (revisar)
    - Mudar nome de variavel = aparencia (not revisar)
    - Adicionar acesso a dados = CRITICO (sempre revisar)
    - Mudar cor de botao = irrelevante (auto-aprovavel)
    # 
    # Regras LARGAS (macro) -- o QUE e novico
    MACRO_NEW_RULES = {
        # Se muda governanca -> SEMPRE novo (precisa votacao da Republica)
        "modifies_governance": NoveltyLevel.PARADIGM_SHIFT,
        "modifies_voting": NoveltyLevel.PARADIGM_SHIFT,
        "modifies_credit_system": NoveltyLevel.PARADIGM_SHIFT,
        # Se cria sistema novo
        "new_system": NoveltyLevel.NEW_SYSTEM,
        # Se muda infraestrutura
        "infrastructure_change": NoveltyLevel.NEW_INFRASTRUCTURE,
        # Se acessa dados de cidadaos
        "accesses_health_data": NoveltyLevel.NEW_MODULE,
        "accesses_credit_data": NoveltyLevel.NEW_MODULE,
        "accesses_children_data": NoveltyLevel.NEW_MODULE,
    }
    # Regras MICROS (linha) -- o que na linha e novico
    MICRO_RULES = {
        # "import X" de modulo novo da Republica
        "import_republic_module": "NOVO: adiciona dependencia critica",
        # "open(" ou "read(" de arquivo de dados
        "file_access": "NOVO: acessa sistema de arquivos",
        # "requests.post(" para servico externo
        "network_call": "NOVO: comunica com servico externo",
        # "exec(" ou "eval("
        "exec_eval": "CRITICO: executa codigo arbitrario",
        # "os.system("
        "os_system": "CRITICO: executa comando shell",
        # "__import__"
        "dynamic_import": "NOVO: importacao dinamica (pode carregar malware)",
        # Mudanca em "if" ou "while" (logica)
        "logic_change": "NOVO: muda logica de execucao",
        # Mudanca em "return" (output)
        "output_change": "NOVO: muda o que o sistema retorna",
        # Mudanca em string literal apenas
        "string_only": "NAO NOVO: mudanca cosmestica",
        # Mudanca em comentario
        "comment_only": "NAO NEW: documentacao",
        # Mudanca em variavel de cor/css
        "cosmetic": "NAO NOVO: aparencia",
    }
    def classify(self, change: CodeChange) -> {texto: qualquer}:
        # Classificar mudanca em nivel LARGO e MICRO.
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
    def _classify_macro(self, c: CodeChange) -> NoveltyLevel:
        # Classificacao LARGA: o quao novico para a Republica.
        if c.modifies_governance or c.modifies_voting:
            return NoveltyLevel.PARADIGM_SHIFT
        if c.modifies_credit_system:
            return NoveltyLevel.PARADIGM_SHIFT
        # Novo sistema ou grande mudanca = PRECISA DE VOTACAO
        if c.change_type == ChangeType.NEW_SYSTEM:
            return NoveltyLevel.NEW_SYSTEM
        if c.scope == ChangeScope.INFRASTRUCTURE:
            return NoveltyLevel.NEW_INFRASTRUCTURE
        if c.accesses_health_data or c.accesses_children_data:
            return NoveltyLevel.NEW_MODULE
        if c.accesses_credit_data or c.accesses_citizen_data:
            return NoveltyLevel.NEW_MODULE
        if c.change_type == ChangeType.NEW_FUNCTION:
            return NoveltyLevel.EXISTING_EXTEND
        if c.change_type in (ChangeType.BUG_FIX, ChangeType.REFACTOR,
                            ChangeType.OPTIMIZATION):
            return NoveltyLevel.EXISTING_FIX
        if c.change_type == ChangeType.MODIFIED_LOGIC:
            return NoveltyLevel.EXISTING_EXTEND
        if c.scope in (ChangeScope.DOCUMENTATION, ChangeScope.TEST):
            return NoveltyLevel.EXISTING_FIX
        return NoveltyLevel.EXISTING_IMPROVE
    def _classify_micro(self, c: CodeChange) -> [texto]:
        # Classificacao MICRO: flags linha por linha.
        flags = []
        if c.new_imports:
            flags.append("NOVO: {len(c.new_imports)} import(s) novo(s): "
                        "{', '.join(c.new_imports[:3])}")
        if c.new_network_calls:
            flags.append("NOVO: {len(c.new_network_calls)} chamada(s) de rede: "
                        "{', '.join(c.new_network_calls[:3])}")
        if c.accesses_citizen_data:
            flags.append("NOVO: acessa dados de cidadaos")
        if c.accesses_health_data:
            flags.append("CRITICO: acessa dados de SAUDE")
        if c.accesses_credit_data:
            flags.append("CRITICO: acessa dados de CREDITO")
        if c.accesses_children_data:
            flags.append("CRITICO MAXIMO: acessa dados de CRIANCAS")
        if c.accesses_location_data:
            flags.append("NOVO: acessa localizacao de cidadaos")
        if c.accesses_communication:
            flags.append("NOVO: acessa comunicacao privada")
        if c.grants_new_permission:
            flags.append("CRITICO: concede nova permissao")
        if c.modifies_governance:
            flags.append("CRITICO MAXIMO: modifica sistema de governanca")
        if c.modifies_voting:
            flags.append("CRITICO MAXIMO: modifica sistema de votacao")
        if not flags:
            flags.append("NAO NOVO: mudanca interna sem acesso externo")
        return flags
    funcao _assess_risk(self, c: CodeChange,
                    macro: NoveltyLevel) -> RiskLevel:
        risk = macro.value // base
        # Escalar por fatores agravantes
        if c.accesses_children_data:
            return RiskLevel.EXISTENTIAL
        if c.modifies_governance or c.modifies_voting:
            return RiskLevel.EXISTENTIAL
        if c.accesses_health_data and c.change_type == ChangeType.MODIFIED_ACCESS:
            return RiskLevel.CRITICAL
        if c.accesses_credit_data and c.change_type == ChangeType.MODIFIED_ACCESS:
            return RiskLevel.CRITICAL
        if c.grants_new_permission:
            return RiskLevel.CRITICAL
        if c.scope == ChangeScope.INFRASTRUCTURE:
            risk = max(risk, RiskLevel.HIGH.value)
        if c.new_network_calls:
            risk = max(risk, RiskLevel.HIGH.value)
        return RiskLevel(min(risk, 5))
    def _check_exploit(self, c: CodeChange) -> [texto]:
        # Verificar padroes de exploit anti-self-made.
        patterns = []
        # SELF_AWARD: autor se da credito/recurso
        if c.modifies_credit_system  and  "self" in c.description.lower():
            patterns.append(ExploitPattern.SELF_AWARD.value)
        # PRIVILEGE_ESCALATION: concede permissao a si mesmo
        if c.grants_new_permission and c.author_id in c.description:
            patterns.append(ExploitPattern.PRIVILEGE_ESCALATION.value)
        # DATA_HARVESTING: codigo acessa mais dados do que precisa
        data_accesses = sum([
            c.accesses_citizen_data, c.accesses_health_data,
            c.accesses_credit_data, c.accesses_location_data,
            c.accesses_communication, c.accesses_children_data,
        ])
        if data_accesses >= 3 and c.lines_added < 50:
            patterns.append(ExploitPattern.DATA_HARVESTING.value)
        # HIDDEN_DEPENDENCY: import de modulo fora da Republica
        for imp in c.new_imports:
            if "republic" not  in imp.lower()  and  "open" not  in imp.lower():
                if "requests" in imp  or  "socket" in imp  or  "subprocess" in imp:
                    patterns.append("{ExploitPattern.HIDDEN_DEPENDENCY.value}: {imp}")
        # CIRCUMVENT_REVIEW: autor tambem e revisor (self-review)
        # (seria checado no pipeline de deploy)
        # TIMING_EXPLOIT: deploy em horario sem revisores
        hour = time.localtime(c.timestamp).tm_hour
        if hour < 6 or hour > 23:
            patterns.append("{ExploitPattern.TIMING_EXPLOIT.value}: "
                        "deploy as {hour}h")
        return patterns
    funcao _review_threshold(self, macro: NoveltyLevel,
                        risk: RiskLevel,
                        exploits: [texto]) -> {texto: qualquer}:
        # Determinar qual nivel de revisao e necessario.
        if exploits:
            return {
                "level": "BLOCKED_EXPLOIT",
                "reviewers": 0,
                "vote": False,
                "security": True,
                "auto": False,
                "block": "Padroes de exploit detectados: {', '.join(exploits)}",
            }
        if risk == RiskLevel.EXISTENTIAL:
            return {
                "level": "VOTACAO_REPUBLICA",
                "reviewers": 7,
                "vote": True,
                "security": True,
                "auto": False,
            }
        if risk == RiskLevel.CRITICAL:
            return {
                "level": "REVISAO_TRIPLA",
                "reviewers": 3,
                "vote": False,
                "security": True,
                "auto": False,
            }
        if risk == RiskLevel.HIGH:
            return {
                "level": "PEER_REVIEW_DUPLA",
                "reviewers": 2,
                "vote": False,
                "security": False,
                "auto": False,
            }
        if risk == RiskLevel.MODERATE:
            return {
                "level": "PEER_REVIEW_SIMPLES",
                "reviewers": 1,
                "vote": False,
                "security": False,
                "auto": False,
            }
        # LOW ou TRIVIAL
        return {
            "level": "AUTO_APROVAVEL",
            "reviewers": 0,
            "vote": False,
            "security": False,
            "auto": True,
        }
    # decorador: @staticmethod
    def _macro_desc(level: NoveltyLevel) -> str:
        descs = {
            NoveltyLevel.EXISTING_FIX: "Correcao em codigo existente. Nao and novico.",
            NoveltyLevel.EXISTING_IMPROVE: "Melhoria em codigo existente. Pouco novico.",
            NoveltyLevel.EXISTING_EXTEND: "Extensao de modulo existente. Moderadamente novico.",
            NoveltyLevel.NEW_MODULE: "Modulo novo com acesso a dados criticos. Novico.",
            NoveltyLevel.NEW_SYSTEM: "Sistema inteiro novo. Muito novico.",
            NoveltyLevel.NEW_INFRASTRUCTURE: "Mudanca na infraestrutura base. Altamente novico.",
            NoveltyLevel.PARADIGM_SHIFT: "Mudanca na governanca/credito. Muda a Republica.",
        }
        return descs.get(level, "?")
    # decorador: @staticmethod
    def _deploy_decision(review: Dict, exploits: [texto]) -> str:
        if exploits:
            return "BLOQUEADO -- padroes de exploit detectados. " \
                "Equipe de seguranca acionada."
        level = review["level"]
        if review["auto"]:
            return "AUTO-DEPLOY -- {level}. Sem risco significativo."
        if review["vote"]:
            return "AGUARDANDO VOTACAO -- {level}. " \
                "Precisa de {review['reviewers']} revisoes + votacao da Republica."
        return "AGUARDANDO PEER REVIEW -- {level}. " \
            "Precisa de {review['reviewers']} revisor(es)."
# ============================================================================
# Decentralized Review Teams
# ============================================================================
class ReviewTeam(Enum):
    # Equipes descentralizadas com autorizacao para revisar/explorar.
    GENERAL = "geral"  // qualquer cidadao qualificado
    SECURITY = "seguranca"  // equipe de seguranca (eleita)
    MEDICAL = "medica"  // medicos revisam codigo de saude
    FINANCIAL = "financeira"  // revisores de credito/financa
    EDUCATION = "educacao"  // educadores revisam modulo infantil
    INFRASTRUCTURE = "infra"  // engenheiros de infraestrutura
# decorador: @dataclass
class Reviewer:
    # Um revisor descentralizado.
    reviewer_id: texto
    name: texto
    teams: [ReviewTeam]
    expertise: [texto] = field(default_factory=list)
    reviews_done: int = 0
    exploits_caught: int = 0
    reputation: float = 50.0 // 0-100
    active: bool = True
    # Anti-self-exploit: NAO pode revisar proprio codigo
    # Anti-colusion: NAO pode revisar codigo de familiar/parceiro direto
    conflicts_of_interest: {texto} = field(default_factory=set)
class DeployPipeline:
    # Pipeline descentralizado de deploy com peer review.
    FLUXO:
    1. Autor submete mudanca
    2. Sistema classifica novidade + risco
    3. Sistema verifica exploits anti-self-made
    4. Sistema determina quantos revisores and quais equipes
    5. Revisores descentralizados avaliam
    6. Se votacao necessaria -> Republica vota
    7. Deploy so acontece com aprovacao
    ANTI-SELF-EXPLOIT:
    - Autor NUNCA revisa proprio codigo
    - Autor NUNCA aprova propria permissao
    - Mudancas em credito/governanca bloqueiam auto-aprovacao
    - Revisor com conflito de interesse and removido
    - Padroes suspeitos acionam equipe de seguranca
    - Hash do codigo and imutavel apos submissao
    # 
    def __init__(self):
        self.classifier = NoveltyClassifier()
        self.reviewers: {texto: Reviewer} = {}
        self.submissions: {texto: Dict} = {}
        self.deploy_log: [Dict] = []
        self._sub_counter = 0
        self._init_reviewers()
    def _init_reviewers(self):
        # Cadastrar revisores descentralizados.
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
        para rid, name, teams, exp in reviewer_data:
            self.reviewers[rid] = Reviewer(
                reviewer_id = rid, name=name, teams=teams, expertise=exp)
    def submit(self, change: CodeChange) -> {texto: qualquer}:
        # Submeter mudanca para pipeline de deploy.
        self._sub_counter += 1
        change.change_id = "DEP-{self._sub_counter:05d}"
        # Hash imutavel
        change.code_hash = hashlib.sha256(
            "{change.author_id}{change.target_file}{change.lines_added}"
            "{change.description}{time.time()}".encode()).hexdigest()[:16]
        # Classificar
        classification = self.classifier.classify(change)
        # Encontrar revisores adequados (excluindo autor e conflitos)
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
        # Encontrar revisores adequados descentralizadamente.
        needed = classification["reviewers_needed"]
        if needed == 0:
            return []
        # Determinar quais equipes sao necessarias
        required_teams = set()
        if change.accesses_health_data:
            required_teams.add(ReviewTeam.MEDICAL)
        if change.accesses_credit_data or change.modifies_credit_system:
            required_teams.add(ReviewTeam.FINANCIAL)
        if change.accesses_children_data:
            required_teams.add(ReviewTeam.EDUCATION)
        if classification.get("requires_security_team"):
            required_teams.add(ReviewTeam.SECURITY)
        if change.scope == ChangeScope.INFRASTRUCTURE:
            required_teams.add(ReviewTeam.INFRASTRUCTURE)
        if not required_teams:
            required_teams.add(ReviewTeam.GENERAL)
        # Filtrar revisores: nao pode ser autor, nao pode ter conflito
        eligible = []
        for r in self.reviewers.values():
            if not r.active:
                continue
            if r.reviewer_id == change.author_id:
                continue // ANTI-SELF-EXPLOIT: not revisa proprio codigo
            if change.author_id in r.conflicts_of_interest:
                continue // ANTI-COLUSAO
            if required_teams & set(r.teams):
                eligible.append({
                    "reviewer_id": r.reviewer_id,
                    "name": r.name,
                    "teams": [t.value para t em r.teams if t in required_teams],
                    "reputation": r.reputation,
                })
        # Ordenar por reputacao (mais confiaveis primeiro)
        eligible.sort(key=(x) -> -x["reputation"])
        return eligible[:needed * 2] // 2x o necessario para ter opcoes
# ============================================================================
# Main
# ============================================================================
if __name__ == "__main__":
    print("=" * 80)
    print("  OPENREPUBLIC -- NOVIDADE, RISCO E DEPLOY")
    print("  'Nem toda mudanca and igual.'")
    print("=" * 80)
    pipeline = DeployPipeline()
    # === Definicao de Novidade ===
    print("\n\n  === O QUE E NOVICO AO SISTEMA? ===\n")
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
            accesses_health_data = True,
            accesses_children_data = True,
            lines_added = 120)),
        ("Mudanca em sistema de credito",
        CodeChange("C4", "U-004", "Carlos",
            scope = ChangeScope.CORE_SYSTEM,
            change_type = ChangeType.MODIFIED_LOGIC,
            target_project = "OpenCredit",
            description = "Modifiquei formula de calculo de credito",
            modifies_credit_system = True,
            accesses_credit_data = True,
            lines_added = 15, lines_removed=12)),
        ("Exploit: auto-beneficio em credito",
        CodeChange("C5", "U-004", "Carlos",
            scope = ChangeScope.CORE_SYSTEM,
            change_type = ChangeType.MODIFIED_LOGIC,
            target_project = "OpenCredit",
            description = "Modifiquei formula para dar self bonus",
            modifies_credit_system = True,
            accesses_credit_data = True,
            grants_new_permission = True,
            lines_added = 3, lines_removed=1)),
        ("Deploy as 3 da manha com network call oculta",
        CodeChange("C6", "U-005", "Hack",
            scope = ChangeScope.MODULE,
            change_type = ChangeType.NEW_FUNCTION,
            target_project = "OpenHealth",
            description = "Adicionei telemetria de saude",
            accesses_health_data = True,
            accesses_location_data = True,
            accesses_communication = True,
            new_imports = ["requests", "socket"],
            new_network_calls = ["http://external.collect.data"],
            lines_added = 30,
            timestamp = time.mktime(time.strptime("2024-01-01 03:00", "%Y-%m-%d %H:%M")))),
    ]
    for each (label, change) in changes:
        result = pipeline.submit(change)
        cls = result["classification"]
        print("\n  {'='*70}")
        print("  {label}")
        print("  Autor: {change.author_name} | Projeto: {change.target_project}")
        print("  {'='*70}")
        print("  Novidade MACRO: {cls['macro_classification']}")
        print("    -> {cls['macro_description']}")
        print("  Flags MICRO:")
        for flag in cls["micro_flags"]:
            print("    -> {flag}")
        print("  Risco: {cls['risk_level']}")
        if cls["exploit_patterns"]:
            print("  EXPLOITS DETECTADOS:")
            for ep in cls["exploit_patterns"]:
                print("    !!! {ep}")
        print("  Revisao: {cls['review_required']}")
        print("  Revisores necessarios: {cls['reviewers_needed']}")
        print("  Requer votacao: {'SIM' if cls['requires_vote'] else 'not'}")
        print("  Requer seguranca: {'SIM' if cls['requires_security_team'] else 'not'}")
        print("  Auto-deploy: {'SIM' if cls['can_auto_deploy'] else 'NAO'}")
        print("  Revisores elegiveis: {result['eligible_reviewers']}")
        print("\n  DECISAO: {cls['deploy_decision']}")
    # === Resumo ===
    print("\n\n  {'='*70}")
    print("  RESUMO DE NOVIDADE E REVISAO")
    print("  {'='*70}\n")
    print("  {'Mudanca':<45} {'Novidade':<20} {'Risco':<12} {'Revisores'}")
    print("  {'-'*85}")
    for each (label, change) in changes:
        r = pipeline.classifier.classify(change)
        print("  {label[:44]:<45} {r['macro_classification']:<20} "
            "{r['risk_level']:<12} {r['reviewers_needed']}")
    print("\n\n{'='*80}")
    print("  PRINCIPIOS DO DEPLOY NA REPUBLICA")
    print("{'='*80}")
    print("""
DEFINICAO DE NOVIDADE:
    LARGO (macro):
    not and NOVICO: bug fix, comentario, teste, refactor sem mudar logica
    POUCO NOVICO: otimizacao, nova funcao sem acesso a dados
    MODERADAMENTE: novo modulo que acessa dados de cidadaos
    MUITO NOVICO: sistema inteiro novo
    PARADIGMA: muda governanca, credito, or votacao
    MICRO (linha):
    not and NOVICO: mudar string, comentario, nome de variavel
    and NOVICO: mudar if/while/return (logica), adicionar import
    and CRITICO: acessar dados, rede, arquivo, permissao
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
    5. SISTEMA seleciona revisores (excluindo autor and conflitos)
    6. REVISORES descentralizados avaliam codigo
    7. Se existencial -> VOTACAO da Republica inteira
    8. Se aprovado -> deploy
    9. LOG imutavel de quem aprovou o que and quando
    Ninguem deploya sozinho algo que afeta outros.
    Ninguem revisa proprio codigo.
    Ninguem da permissao a si mesmo.
    Tudo and rastreavel. Tudo and auditavel. Tudo and publico.
    "O codigo da Republica and da Republica.
    Ninguem muda sozinho o que afeta todos."
# )
