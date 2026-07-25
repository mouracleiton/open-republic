// OpenRepoPolicy + OpenSkills -- Repositorio Unico e Skills Comprovadas -- gerado de Portugol++
package openrepopolicy_openskills_repositorio_unico_e_skills_comprovadas

import "fmt"

// !/usr/bin/env python3
//
OpenRepoPolicy + OpenSkills -- Repositorio Unico && Skills Comprovadas
======================================================================
PARTE 1 -- OPENREPOPOLICY:
"Nao ha mais clones. Nao ha mais forks.
So o REPOSITORIO PRINCIPAL. Todo mundo pega o resultado.
Forks que mutilam o projeto sao PROIBIDOS."
COMO FUNCIONA:
- Repositorio principal (main) && a UNICA fonte de verdade
- Cidadaos PUXAM (pull) do main para local
- Mudancas sao PROPOSTAS (merge request) && VOTADAS (P4)
- Ninguem copia o projeto && faz versao propria
- Tudo && UNICO. Tudo && bem comum (CC0)
PARTE 2 -- OPENSKILLS:
"Curriculum vitae && PAPEL. OpenSkills && VIVO.
Skills comprovadas pela INTERACAO com o sistema.
Nao 'eu sei Rust'. 'O SISTEMA TESTOU && APROVOU'."
COMO FUNCIONA:
- Cada cidadao tem um repositorio de skills
- Skills sao COMPROVADAS pelo sistema (! auto-declaradas)
- OpenGamesRealistic verifica conhecimento
- OpenLaborRelay registra tarefas completadas
- OpenUniversity certifica cursos
- OpenProfessions valida nivel (aprendiz -> mestre)
- Tudo publico. Tudo verificavel. Tudo CC0.
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime
// ============================================================================
// 1. POLITICA DE REPOSITORIO (OpenRepoPolicy)
// ============================================================================
type RepoAction int
const (
    PULL = "puxar"  // pegar do main para local
    PROPOSE = "propor"  // propor mudanca no main
    VOTE = "votar"  // votar em proposta
    MERGE = "integrar"  // integrar proposta aprovada
    REJECT = "rejeitar"  // rejeitar proposta
    SYNC = "sincronizar"  // atualizar local com main
type MergeStatus int
const (
    DRAFT = "rascunho"
    PROPOSED = "proposta"  // proposta feita
    IN_REVIEW = "em_revisao"  // assembleia analisando
    VOTING = "votacao"  // votacao aberta
    APPROVED = "aprovada"  // assembleia aprovou
    REJECTED = "rejeitada"  // assembleia rejeitou
    MERGED = "integrada"  // integrada no main
    AUTO_REJECTED = "auto_rejeitada"  // viola principios (P1-P4)
// decorador: @dataclass
type MergeProposal struct {
    // Uma proposta de mudanca no repositorio principal.
    proposal_id: texto
    title: texto
    author: texto // quem propos
    description := "" // string
    files_changed := field(default_factory=list) // [texto]
    lines_added := 0 // int64
    lines_removed := 0 // int64
    status := MergeStatus.DRAFT // MergeStatus
    votes_for := 0 // int64
    votes_against := 0 // int64
    total_voters := 10000 // int64
    quorum_needed := 0.51 // 51% para aprovar // float64
    // Validacao automatica
    passes_constitution := true // bool
    fails_reason := "" // string
    tested := false // rodou sem erro? // bool
    test_result := "" // string
    created_date := "" // string
    merged_date := "" // string
type RepoEngine struct {
    // Motor do repositorio unico da Republica.
    REGRAS:
    1. UM repositorio. UMA fonte de verdade. SEM forks.
    2. Todo mundo PUXA do main (pull). Ninguem copia.
    3. Mudancas sao PROPOSTAS. VOTADAS. INTEGRADAS.
    4. Forks que mutilam sao PROIBIDOS (auto-rejeitados).
    5. Assembleia decide (P4) -- 51% para integrar.
    6. Tudo testado antes de integrar (sem quebrar).
    7. Tudo CC0 -- ! ha "propriedade" de codigo.
    O QUE && PROIBIDO:
    - Fork (copiar && fazer versao propria)
    - Mutilacao (pegar parte do projeto && descartar o resto)
    - Propriedade privada de codigo (tudo CC0)
    - Mudanca sem votacao
    - Mudanca que quebra principios (P1-P4)
    O QUE && PERMITIDO:
    - Pull (puxar para local, usar, aprender)
    - Propor mudanca (qualquer cidadao)
    - Votar em mudanca (assembleia)
    - Usar parte do codigo em OUTRO projeto (CC0 permite)
    - Mas o PROJETO PRINCIPAL && UNICO
    //
    func __init__(self) {
        self.proposals: {texto: MergeProposal} = {}
        self.repo_stats: {texto: qualquer} = {
            "total_files": 0,
            "total_lines": 0,
            "total_commits": 0,
            "last_sync": "",
        }
        self.forks_rejected: inteiro = 0
        self.proposals_merged: inteiro = 0
    func pull(self, citizen_id: texto) {texto: qualquer} {
        // Cidadao puxa repositorio principal para local.
        return {
            "action": "PULL",
            "citizen": citizen_id,
            "source": "REPOSITORIO PRINCIPAL (main)",
            "destination": "local",
            "files_synced": self.repo_stats["total_files"],
            "lines_synced": self.repo_stats["total_lines"],
            "message": (
                "{citizen_id} puxou o repositorio principal. "
                "Tudo atualizado. Sem fork. Sem copia. "
                "E o PROJETO OFICIAL da Republica."
            ),
        }
    funcao propose(self, author: texto, title: texto,
                description := "", // string
                files := nil, // [texto]
                added := 0, removed: inteiro = 0, // int64
                passes_constitution := true, // bool
                fails_reason := "", // string
                tested := true) -> {texto: qualquer}: // bool
        // Propor mudanca no repositorio principal.
        pid = hashlib.md5("{title}{author}".encode()).hexdigest()[:8]
        if ! passes_constitution {
            self.forks_rejected += 1
            return {
                "proposal_id": pid,
                "status": "AUTO_REJEITADA",
                "reason": fails_reason  ||  "Viola P1-P4",
                "message": (
                    "Proposta REJEITADA automaticamente: {fails_reason}. "
                    "A Republica NAO aceita mudancas que violam principios."
                ),
            }
        proposal = MergeProposal(
            proposal_id = pid, title=title, author=author,
            description = description, files_changed=files || [],
            lines_added = added, lines_removed=removed,
            status = tested ? MergeStatus.PROPOSED : MergeStatus.DRAFT,
            passes_constitution = true, tested=tested,
            test_result = tested ? "PASSOU" : "NAO TESTADO",
            created_date = datetime.now().isoformat(),
        )
        self.proposals[pid] = proposal
        return {
            "proposal_id": pid,
            "title": title,
            "author": author,
            "status": proposal.status.value,
            "tested": tested,
            "test_result": proposal.test_result,
            "message": (
                "Proposta '{title}' criada por {author}. "
                "{'Pronta para votacao.' if tested else 'Precisa testar antes de votar.'} "
                "Assembleia vai votar."
            ),
        }
    funcao vote(self, proposal_id: texto, votes_for: inteiro,
            votes_against: inteiro) -> {texto: qualquer}:
        // Assembleia vota na proposta.
        proposal = self.proposals.get(proposal_id)
        if ! proposal {
            return {"error": "Proposta ! encontrada"}
        proposal.votes_for = votes_for
        proposal.votes_against = votes_against
        total = votes_for + votes_against
        pct_for = votes_for / maximo(total, 1)
        if pct_for >= proposal.quorum_needed {
            proposal.status = MergeStatus.APPROVED
            self._merge(proposal)
            return {
                "proposal": proposal.title,
                "result": "APROVADA",
                "votes": "{votes_for}/{total} ({pct_for:.0%})",
                "merged": true,
                "message": "Proposta APROVADA por {pct_for:.0%}. Integrada ao main.",
            }
        } else {
            proposal.status = MergeStatus.REJECTED
            return {
                "proposal": proposal.title,
                "result": "REJEITADA",
                "votes": "{votes_for}/{total} ({pct_for:.0%})",
                "message": "Proposta REJEITADA. {pct_for:.0%} a favor (precisava {proposal.quorum_needed:.0%}).",
            }
    func _merge(self, proposal: MergeProposal) None {
        proposal.status = MergeStatus.MERGED
        proposal.merged_date = datetime.now().isoformat()
        self.repo_stats["total_lines"] += proposal.lines_added - proposal.lines_removed
        self.repo_stats["total_commits"] += 1
        self.proposals_merged += 1
    func reject_fork(self, citizen: texto, reason: texto) {texto: qualquer} {
        // Rejeita tentativa de fork.
        self.forks_rejected += 1
        return {
            "citizen": citizen,
            "action": "FORK REJEITADO",
            "reason": reason,
            "policy": (
                "A Republica PROIBE forks que mutilam o projeto. "
                "Existe UM repositorio. UM projeto. UMA fonte de verdade. "
                "Voce pode PROPOR mudancas (merge request). "
                "Nao pode COPIAR && fazer versao propria. "
                "P1 anti-elitismo: projeto && de TODOS, ! de cada um."
            ),
            "alternative": "Proponha sua mudanca. A assembleia vota.",
        }
    func repo_status(self) {texto: qualquer} {
        return {
            "repositorio": "UNICO (main)",
            "forks_permitidos": 0,
            "fonte_de_verdade": "REPOSITORIO PRINCIPAL",
            **self.repo_stats,
            "propostas_totais": len(self.proposals),
            "propostas_integradas": self.proposals_merged,
            "forks_rejeitados": self.forks_rejected,
            "licenca": "CC0 universal",
            "propriedade": "BEM COMUM (ninguem && dono)",
        }
// ============================================================================
// 2. OPENSKILLS (substituto do curriculum vitae)
// ============================================================================
type SkillProof int
const (
    // Como uma skill e COMPROVADA (nao auto-declarada).
    SYSTEM_TESTED = "sistema_testou"  // OpenGamesRealistic / OpenLegoCode testou
    TASK_COMPLETED = "tarefa_completada"  // OpenLaborRelay registrou
    COURSE_CERTIFIED = "curso_certificado"  // OpenUniversity certificou
    PEER_VERIFIED = "pares_verificaram"  // outros cidadaos atestaram
    CONTRIBUTION = "contribuicao"  // codigo/arte/conteudo no repositorio
    MENTOR_ENDORSED = "mentor_endossou"  // mentor (senior/mestre) endossou
    DEMONSTRATED = "demonstrou"  // demonstrou ao vivo (evento, stream)
type SkillLevel int
const (
    NONE = ("nenhum", 0)
    AWARE = ("conhece", 1)  // ja ouviu falar
    BASIC = ("basico", 2)  // consegue fazer simples
    INTERMEDIATE = ("intermediario", 3)
    ADVANCED = ("avancado", 4)
    EXPERT = ("especialista", 5)
    MASTER = ("mestre", 6)
    // decorador: @property
    func label(self) string {
        return self.value[0]
    // decorador: @property
    func level_num(self) int64 {
        return self.value[1]
// decorador: @dataclass
type VerifiedSkill struct {
    // Uma skill COMPROVADA pelo sistema.
    skill_id: texto
    skill_name: texto                  // ex: "programacao_rust", "cirurgia_dental"
    category: texto // software, saude, construcao, etc
    level := SkillLevel.NONE // SkillLevel
    proofs := field(default_factory=list) // [Dict]
    // Comprovacoes
    system_tests_passed := 0 // int64
    tasks_completed := 0 // int64
    courses_certified := 0 // int64
    peer_verifications := 0 // int64
    contributions := 0 // int64
    mentor_endorsements := 0 // int64
    demonstrations := 0 // int64
    // Score de confianca
    confidence := 0.0 // 0-1 (quao confiavel && a skill) // float64
    // decorador: @property
    func is_verified(self) bool {
        return len(self.proofs) > 0 && self.confidence > 0.3
// decorador: @dataclass
type SkillProfile struct {
    // Perfil de skills de um cidadao -- SUBSTITUI o curriculum vitae.
    DIFERENCA vs CV tradicional:
    - CV: voce ESCREVE o que sabe. Ninguem verifica.
    - OpenSkills: o SISTEMA COMPROVA. Voce ! auto-declara.
    - CV: papel estatico. Desatualizado em 1 mes.
    - OpenSkills: VIVO. Atualiza toda vez que voce faz algo.
    - CV: "eu sei Rust". (menta? verdade? quem sabe?)
    - OpenSkills: "Sistema testou: Rust AVANCADO (8 testes, 12 tarefas, 3 contribuicoes)"
    - CV: usado para excluir (sem diploma = rejeitado)
    - OpenSkills: usado para CONECTAR (skill certa para tarefa certa)
    //
    citizen_id: texto
    citizen_name: texto
    age := 0 // int64
    profession := "" // string
    profession_level := ""  // OpenProfessions (aprendiz -> mestre) // string
    skills := field(default_factory=dict) // {texto: VerifiedSkill}
    created_date := "" // string
    // Stats
    total_skills_verified := 0 // int64
    total_tasks_completed := 0 // int64
    total_contributions := 0 // int64
    impact_score := 0.0 // OpenCredit/OpenCreator // float64
    // decorador: @property
    func skill_count(self) int64 {
        return len(self.skills)
    // decorador: @property
    func verified_count(self) int64 {
        return soma(1 para s em self.skills.values() if s.is_verified)
type SkillsEngine struct {
    // Motor de skills verificadas.
    COMO UMA SKILL && COMPROVADA:
    1. SISTEMA TESTOU (OpenGamesRealistic / OpenLegoCode)
    Cidadao faz quiz de Rust no simulador -> passou?
    Sistema registra: Rust INTERMEDIARIO (prova: quiz 85%)
    2. TAREFA COMPLETADA (OpenLaborRelay)
    Cidadao completa tarefa de programar modulo em Rust?
    Sistema registra: Rust AVANCADO (prova: 12 tarefas)
    3. CURSO CERTIFICADO (OpenUniversity)
    Cidadao completa curso de cirurgia?
    Sistema registra: Cirurgia INTERMEDIARIO (prova: curso certificado)
    4. PARES VERIFICARAM (OpenSocialNetwork)
    Outros cidadaos atestam: "esta pessoa sabe costurar"
    Sistema registra: Costura BASICO (3 verificacoes de pares)
    5. CONTRIBUICAO (repositorio principal)
    Cidadao contribuiu com codigo no repositorio?
    Sistema registra: Rust EXPERT (prova: 3 contribuicoes integradas)
    6. MENTOR ENDOSSOU (OpenProfessions)
    Mestre de obra viu pedreiro trabalhar?
    Sistema registra: Alvenaria AVANCADO (prova: mentor endossou)
    7. DEMONSTROU (evento ao vivo / OpenTV)
    Cidadao cozinhou no programa de TV?
    Sistema registra: Culinaria INTERMEDIARIO (demonstracao publica)
    NENHUMA skill && auto-declarada.
    TUDO && comprovado por INTERACAO com o sistema.
    //
    func __init__(self) {
        self.profiles: {texto: SkillProfile} = {}
    funcao create_profile(self, citizen_id: texto, name: texto,
                    age := 0, profession: texto = "" // int64
                    ) -> {texto: qualquer}:
        profile = SkillProfile(
            citizen_id = citizen_id, citizen_name=name,
            age = age, profession=profession,
            created_date = datetime.now().isoformat(),
        )
        self.profiles[citizen_id] = profile
        return {"created": true, "citizen": name, "message": "Perfil OpenSkills criado para {name}."}
    funcao add_proof(self, citizen_id: texto, skill_name: texto,
                category: texto, proof_type: SkillProof,
                proof_detail := "", // string
                level := SkillLevel.BASIC) -> {texto: qualquer}: // SkillLevel
        // Adiciona comprovacao de skill.
        profile = self.profiles.get(citizen_id)
        if ! profile {
            return {"error": "Perfil ! encontrado"}
        sid = hashlib.md5("{citizen_id}{skill_name}".encode()).hexdigest()[:8]
        if sid ! in profile.skills {
            profile.skills[sid] = VerifiedSkill(
                skill_id = sid, skill_name=skill_name, category=category)
        skill = profile.skills[sid]
        proof = {
            "type": proof_type.value,
            "detail": proof_detail,
            "date": datetime.now().isoformat(),
            "level_at_proof": level.label,
        }
        skill.proofs.append(proof)
        // Atualizar contadores
        if proof_type == SkillProof.SYSTEM_TESTED {
            skill.system_tests_passed += 1
        } else if proof_type == SkillProof.TASK_COMPLETED {
            skill.tasks_completed += 1
        } else if proof_type == SkillProof.COURSE_CERTIFIED {
            skill.courses_certified += 1
        } else if proof_type == SkillProof.PEER_VERIFIED {
            skill.peer_verifications += 1
        } else if proof_type == SkillProof.CONTRIBUTION {
            skill.contributions += 1
        } else if proof_type == SkillProof.MENTOR_ENDORSED {
            skill.mentor_endorsements += 1
        } else if proof_type == SkillProof.DEMONSTRATED {
            skill.demonstrations += 1
        // Recalcular nivel (mais provas = nivel maior)
        total_proofs = len(skill.proofs)
        levels = [SkillLevel.NONE, SkillLevel.AWARE, SkillLevel.BASIC,
                SkillLevel.INTERMEDIATE, SkillLevel.ADVANCED,
                SkillLevel.EXPERT, SkillLevel.MASTER]
        skill.level = levels[minimo(total_proofs, len(levels) - 1)]
        // Confianca
        weights = {
            SkillProof.SYSTEM_TESTED: 0.25,
            SkillProof.TASK_COMPLETED: 0.20,
            SkillProof.COURSE_CERTIFIED: 0.20,
            SkillProof.PEER_VERIFIED: 0.10,
            SkillProof.CONTRIBUTION: 0.15,
            SkillProof.MENTOR_ENDORSED: 0.15,
            SkillProof.DEMONSTRATED: 0.10,
        }
        skill.confidence = minimo(1.0, soma(
            weights.get(SkillProof(p["type"]), 0.05) para p em skill.proofs
        ))
        if skill.is_verified && skill.level.level_num >= 2 {
            profile.total_skills_verified += 1
        return {
            "citizen": profile.citizen_name,
            "skill": skill_name,
            "level": skill.level.label,
            "proof_added": proof_type.value,
            "total_proofs": total_proofs,
            "confidence": "{skill.confidence:.0%}",
            "verified": skill.is_verified,
            "message": (
                "{profile.citizen_name}: skill '{skill_name}' atualizada. "
                "Nivel: {skill.level.label}. "
                "Prova: {proof_type.value}. "
                "Confianca: {skill.confidence:.0%}. "
                "COMPROVADO pelo sistema. Nao auto-declarado."
            ),
        }
    func get_profile(self, citizen_id: texto) {texto: qualquer} {
        // Retorna perfil de skills (substitui CV).
        profile = self.profiles.get(citizen_id)
        if ! profile {
            return {"error": "Perfil ! encontrado"}
        return {
            "citizen": profile.citizen_name,
            "age": profile.age,
            "profession": profile.profession,
            "total_skills": profile.skill_count,
            "verified_skills": profile.verified_count,
            "skills": [
                {
                    "skill": s.skill_name,
                    "category": s.category,
                    "level": s.level.label,
                    "level_num": s.level.level_num,
                    "confidence": "{s.confidence:.0%}",
                    "verified": s.is_verified,
                    "proofs": len(s.proofs),
                    "proofs_detail": [
                        "{p['type']}: {p['detail']}" para p em s.proofs[:3]
                    ],
                }
                para s em ordene(profile.skills.values(), {
                                key = (x) -> -x.level.level_num)
            ],
            "message": (
                "Perfil OpenSkills de {profile.citizen_name}: "
                "{profile.verified_count} skills verificadas de {profile.skill_count}. "
                "Tudo COMPROVADO pelo sistema."
            ),
        }
    funcao search_by_skill(self, skill_name: texto,
                        min_level := 2) -> [Dict]: // int64
        // Busca cidadaos com skill (para OpenLaborRelay).
        results = []
        for _, profile := range self.profiles.values() {
            for _, skill := range profile.skills.values() {
                if (skill.skill_name.lower() == skill_name.lower()
                    && skill.level.level_num >= min_level
                    && skill.is_verified):
                    results.append({
                        "citizen": profile.citizen_name,
                        "skill": skill.skill_name,
                        "level": skill.level.label,
                        "confidence": "{skill.confidence:.0%}",
                        "proofs": len(skill.proofs),
                    })
        return results
    funcao compare_to_cv(self) retorna List[{texto: texto}]:
        // Compara OpenSkills com curriculum vitae tradicional.
        return [
            {"aspecto": "Declaracao",
            "cv_tradicional": "Voce ESCREVE o que sabe",
            "openskills": "SISTEMA COMPROVA por interacao"},
            {"aspecto": "Verificacao",
            "cv_tradicional": "Nenhuma. Pode mentir.",
            "openskills": "Multiplas provas (testes, tarefas, cursos)"},
            {"aspecto": "Atualizacao",
            "cv_tradicional": "Estatico. Desatualiza em 1 mes.",
            "openskills": "VIVO. Atualiza toda vez que voce faz algo."},
            {"aspecto": "Diploma",
            "cv_tradicional": "Precisa de papel de instituicao",
            "openskills": "Precisa de COMPETENCIA (P1 anti-elitismo)"},
            {"aspecto": "Uso",
            "cv_tradicional": "Excluir (sem diploma = rejeitado)",
            "openskills": "CONECTAR (skill certa para tarefa certa)"},
            {"aspecto": "Privacidade",
            "cv_tradicional": "Documento privado que voce envia",
            "openskills": "Publico na Republica (CC0, verificavel)"},
            {"aspecto": "Confianca",
            "cv_tradicional": "Baixa (quem sabe se && verdade?)",
            "openskills": "Alta (sistema testou, pares verificaram)"},
            {"aspecto": "Bias",
            "cv_tradicional": "Nome, idade, genero, aparencia influenciam",
            "openskills": "So skills importam. Sem bias visual."},
        ]
    func stats(self) {texto: qualquer} {
        all_skills = []
        for _, p := range self.profiles.values() {
            all_skills.extend(s.skill_name para s em p.skills.values())
        return {
            "total_perfis": len(self.profiles),
            "total_skills_registradas": len(all_skills),
            "skills_unicas": len(set(all_skills)),
            "skills_mais_comuns": dict(Counter(all_skills).most_common(5)),
        }
// ============================================================================
// 3. MAIN
// ============================================================================
if __name__ == "__main__" {
    repo = RepoEngine()
    skills = SkillsEngine()
    fmt.Println("=" * 80)
    fmt.Println("  OPENREPOPOLICY + OPENSKILLS")
    fmt.Println("  Repositorio unico + Skills comprovadas pelo sistema")
    fmt.Println("=" * 80)
    // === PARTE 1: REPOSITORIO ===
    fmt.Println("\n\n  {'='*40}")
    fmt.Println("  PARTE 1: OPENREPOPOLICY")
    fmt.Println("  {'='*40}\n")
    // Status do repositorio
    repo.repo_stats = {
        "total_files": 130, "total_lines": 700000,
        "total_commits": 500, "last_sync": datetime.now().isoformat(),
    }
    // Pull
    fmt.Println("  === PULL (pegar do main) ===\n")
    p = repo.pull("cleiton")
    fmt.Println("  {p['message']}")
    // Proposta aprovada
    fmt.Println("\n\n  === PROPOSTA APROVADA ===\n")
    r = repo.propose("cleiton", "Adicionar OpenMetaCognition",
                    "Novo sistema de auto-consciencia cognitiva",
                    ["open_metacognition.py"], 800, 0, true, "", true)
    fmt.Println("  {r['message']}")
    vote = repo.vote(r["proposal_id"], 6500, 3500)
    fmt.Println("  {vote['message']}")
    // Proposta rejeitada (viola P1-P4)
    fmt.Println("\n\n  === PROPOSTA AUTO-REJEITADA (viola principios) ===\n")
    r2 = repo.propose("anonimo", "Criar sistema de pagamento privado",
                    "Sistema de dinheiro para elites",
                    passes_constitution = false,
                    fails_reason = "Viola P1 anti-elitismo + cria moeda privada")
    fmt.Println("  {r2['message']}")
    // Fork rejeitado
    fmt.Println("\n\n  === FORK REJEITADO ===\n")
    fork = repo.reject_fork("joao", "Tentou copiar OpenHealth && remover modulos de saude mental")
    fmt.Println("  {fork['citizen']}: {fork['action']}")
    fmt.Println("  Politica: {fork['policy']}")
    fmt.Println("  Alternativa: {fork['alternative']}")
    // Status repositorio
    fmt.Println("\n\n  === STATUS DO REPOSITORIO ===\n")
    status = repo.repo_status()
    para cada (k, v) em status.items(): {
        fmt.Println("  {k:<30} {v}")
    // === PARTE 2: OPENSKILLS ===
    fmt.Println("\n\n  {'='*40}")
    fmt.Println("  PARTE 2: OPENSKILLS")
    fmt.Println("  {'='*40}\n")
    // Criar perfis
    fmt.Println("  === CRIANDO PERFIS ===\n")
    skills.create_profile("C-001", "Cleiton", 35, "Programador/Fundador")
    skills.create_profile("C-002", "Maria", 28, "Medica")
    skills.create_profile("C-003", "Joao", 45, "Pedreiro (autodidata)")
    skills.create_profile("C-004", "Ana", 22, "Estudante")
    // Adicionar provas (COMPROVADAS pelo sistema)
    fmt.Println("\n  === ADICIONANDO PROVAS COMPROVADAS ===\n")
    // Cleiton: Rust (multiple proofs)
    proofs_cleiton = [
        ("programacao_rust", "software", SkillProof.SYSTEM_TESTED,
        "OpenLegoCode: teste de ownership passado (85%)", SkillLevel.INTERMEDIATE),
        ("programacao_rust", "software", SkillProof.TASK_COMPLETED,
        "Completou 50 tarefas OpenLaborRelay em Rust", SkillLevel.ADVANCED),
        ("programacao_rust", "software", SkillProof.CONTRIBUTION,
        "3 contribuicoes integradas no repositorio principal", SkillLevel.EXPERT),
        ("programacao_rust", "software", SkillProof.DEMONSTRATED,
        "Demonstrou no OpenTV: como programar em LEGO", SkillLevel.EXPERT),
    ]
    para skill, cat, proof, detail, level in proofs_cleiton: {
        r = skills.add_proof("C-001", skill, cat, proof, detail, level)
        fmt.Println("  {r['citizen']}: {r['skill']} -> {r['level']} "
            "(confianca: {r['confidence']})")
    // Cleiton: arquitetura modular
    r = skills.add_proof("C-001", "arquitetura_modular", "software",
                        SkillProof.CONTRIBUTION,
                        "Criou OpenModularArchitecture (51+ modulos)",
                        SkillLevel.MASTER)
    fmt.Println("  {r['citizen']}: {r['skill']} -> {r['level']}")
    // Maria: medicina
    proofs_maria = [
        ("medicina_diagnostico", "saude", SkillProof.COURSE_CERTIFIED,
        "OpenUniversity: medicina 6 anos + residencia", SkillLevel.EXPERT),
        ("medicina_diagnostico", "saude", SkillProof.TASK_COMPLETED,
        "2000 diagnosticos no OpenHealth", SkillLevel.EXPERT),
        ("cirurgia", "saude", SkillProof.MENTOR_ENDORSED,
        "Medico senior endossou: cirurgia competente", SkillLevel.ADVANCED),
        ("primeiros_socorros", "saude", SkillProof.SYSTEM_TESTED,
        "OpenGamesRealistic: simulador doutor (95%)", SkillLevel.ADVANCED),
    ]
    para skill, cat, proof, detail, level in proofs_maria: {
        r = skills.add_proof("C-002", skill, cat, proof, detail, level)
        fmt.Println("  {r['citizen']}: {r['skill']} -> {r['level']} "
            "(confianca: {r['confidence']})")
    // Joao: pedreiro autodidata (sem diploma)
    proofs_joao = [
        ("alvenaria", "construcao", SkillProof.MENTOR_ENDORSED,
        "Mestre de obra endossou: 20 anos de pratica", SkillLevel.EXPERT),
        ("alvenaria", "construcao", SkillProof.TASK_COMPLETED,
        "150 obras no OpenLaborRelay", SkillLevel.EXPERT),
        ("alvenaria", "construcao", SkillProof.PEER_VERIFIED,
        "5 cidadaos atestaram: trabalho excelente", SkillLevel.ADVANCED),
        ("eletrica_basica", "construcao", SkillProof.TASK_COMPLETED,
        "30 instalacoes no OpenLaborRelay", SkillLevel.INTERMEDIATE),
    ]
    para skill, cat, proof, detail, level in proofs_joao: {
        r = skills.add_proof("C-003", skill, cat, proof, detail, level)
        fmt.Println("  {r['citizen']}: {r['skill']} -> {r['level']} "
            "(confianca: {r['confidence']})")
    // Ana: estudante aprendendo
    proofs_ana = [
        ("programacao_rust", "software", SkillProof.SYSTEM_TESTED,
        "OpenGamesRealistic: programador simulator (70%)", SkillLevel.BASIC),
        ("primeiros_socorros", "saude", SkillProof.SYSTEM_TESTED,
        "OpenGamesRealistic: simulador doutor (80%)", SkillLevel.BASIC),
    ]
    para skill, cat, proof, detail, level in proofs_ana: {
        r = skills.add_proof("C-004", skill, cat, proof, detail, level)
        fmt.Println("  {r['citizen']}: {r['skill']} -> {r['level']} "
            "(confianca: {r['confidence']})")
    // === PERFIL COMPLETO (substitui CV) ===
    fmt.Println("\n\n  === PERFIL OPENSKILLS (substitui CV) ===\n")
    for _, cid := range ["C-001", "C-002", "C-003", "C-004"] {
        profile = skills.get_profile(cid)
        fmt.Println("\n  {profile['citizen']} ({profile['profession']})")
        fmt.Println("  Skills verificadas: {profile['verified_skills']}/{profile['total_skills']}")
        for _, s := range profile["skills"][:3] {
            fmt.Println("    [{s['level']:<13}] {s['skill']:<25} "
                "conf: {s['confidence']} provas: {s['proofs']}")
            for _, d := range s["proofs_detail"][:1] {
                fmt.Println("      -> {d[:60]}")
    // === BUSCAR POR SKILL ===
    fmt.Println("\n\n  === BUSCAR: quem sabe Rust? ===\n")
    rust_devs = skills.search_by_skill("programacao_rust", min_level=2)
    for _, dev := range rust_devs {
        fmt.Println("  {dev['citizen']:<15} {dev['level']:<13} "
            "conf: {dev['confidence']} provas: {dev['proofs']}")
    fmt.Println("\n  === BUSCAR: quem sabe alvenaria? ===\n")
    builders = skills.search_by_skill("alvenaria", min_level=2)
    for _, b := range builders {
        fmt.Println("  {b['citizen']:<15} {b['level']:<13} "
            "conf: {b['confidence']} provas: {b['proofs']}")
    // === COMPARACAO CV vs OPENSKILLS ===
    fmt.Println("\n\n  === CV TRADICIONAL vs OPENSKILLS ===\n")
    comp = skills.compare_to_cv()
    fmt.Println("  {'Aspecto':<15} {'CV Tradicional':<30} {'OpenSkills'}")
    fmt.Println("  {'-'*75}")
    for _, c := range comp {
        fmt.Println("  {c['aspecto']:<15} {c['cv_tradicional'][:29]:<30} {c['openskills'][:35]}")
    // === STATS ===
    fmt.Println("\n\n  === ESTATISTICAS ===\n")
    s = skills.stats()
    para cada (k, v) em s.items(): {
        fmt.Println("  {k:<30} {v}")
    // === FILOSOFIA ===
    fmt.Println("\n\n{'='*80}")
    fmt.Println("  FILOSOFIA: REPOSITORIO UNICO + SKILLS COMPROVADAS")
    fmt.Println("{'='*80}")
    fmt.Println("""
REPOSITORIO UNICO (sem forks):
    Um projeto. Uma fonte de verdade. Sem copias.
    Forks que mutilam sao PROIBIDOS.
    Mudancas sao PROPOSTAS -> VOTADAS -> INTEGRADAS.
    Assembleia decide (P4). 51% para integrar.
    Tudo CC0. Ninguem && dono. Todos herdeiros.
    O que pode: PULL (puxar), PROPOR (merge request), VOTAR.
    O que ! pode: FORK (copiar), MUTILAR (descartar partes),
    PROPRIEDADE (codigo && bem comum).
OPENSKILLS (substitui curriculum vitae):
    CV tradicional: voce ESCREVE o que sabe. Pode mentir.
    OpenSkills: SISTEMA COMPROVA por interacao.
    7 formas de comprovar:
    1. SISTEMA TESTOU: OpenGamesRealistic / OpenLegoCode (quiz, simulador)
    2. TAREFA COMPLETADA: OpenLaborRelay registrou
    3. CURSO CERTIFICADO: OpenUniversity certificou
    4. PARES VERIFICARAM: outros cidadaos atestaram
    5. CONTRIBUICAO: codigo/arte no repositorio principal
    6. MENTOR ENDOSSOU: senior/mestre validou
    7. DEMONSTROU: ao vivo (OpenTV, evento)
    NENHUMA skill && auto-declarada.
    TUDO && comprovado por INTERACAO com o sistema.
    Joao (pedreiro autodidata):
    CV tradicional: "sem diploma" -> REJEITADO.
    OpenSkills: 20 anos de pratica, 150 obras, 5 verificacoes de pares,
    mentor endossou -> ALVENARIA EXPERT. APROVADO.
    Ana (22 anos, estudante):
    CV tradicional: "sem experiencia" -> REJEITADA.
    OpenSkills: simulador 70%, Rust BASICO -> em crescimento. CONECTADA.
PRINCIPIOS:
    P1: Repositorio unico (sem elite de codigo). Skills por competencia (! diploma).
    P2: Cidadao escolhe se perfil && publico. Skills sao suas.
    P3 := trabalho de alto impacto. // Contribuir no repositorio
    P4: Assembleia vota mudancas. Skills verificadas por pares.
// )
    fmt.Println("{'='*80}")
    rs = repo.repo_status()
    fmt.Println("  Repo: {rs['repositorio']} | {rs['propostas_integradas']} integradas | "
        "{rs['forks_rejeitados']} forks rejeitados.")
    fmt.Println("  Skills: {s['total_perfis']} perfis, {s['skills_unicas']} skills unicas.")
    fmt.Println("  Sem fork. Sem CV. So Republica.")
    fmt.Println("{'='*80}")
