# OpenRepoPolicy + OpenSkills -- Repositorio Unico e Skills Comprovadas

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_repo_skills.py`

**Descricao:** ======================================================================
PARTE 1 -- OPENREPOPOLICY:
  "Nao ha mais clones. Nao ha mais forks.
   So o REPOSITORIO PRINCIPAL. Todo mundo pega o resultado.
   Forks que mutilam o projeto sao PROIBIDOS."
  COMO FUNCIONA:
  - Repositorio principal (main) e a UNICA fonte de verdade
  - Cidadaos PUXAM (pull) do main para local
  - Mudancas sao PROPOSTAS (merge request) e VOTADAS (P4)
  - Ninguem copia o projeto e faz versao propria
  - Tudo e UNICO. Tudo e bem comum (CC0)
PARTE 2 -- OPENSKILLS:
  "Curriculum vitae e PAPEL. OpenSkills e VIVO.
   Skills comprovadas pela INTERACAO com o sistema.
   Nao 'eu sei Rust'. 'O SISTEMA TESTOU e APROVOU'."
  COMO FUNCIONA:
  - Cada cidadao tem um repositorio de skills
  - Skills sao COMPROVADAS pelo sistema (nao auto-declaradas)
  - OpenGamesRealistic verifica conhecimento
  - OpenLaborRelay registra tarefas completadas
  - OpenUniversity certifica cursos
  - OpenProfessions valida nivel (aprendiz -> mestre)
  - Tudo publico. Tudo verificavel. Tudo CC0.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepoPolicy + OpenSkills -- Repositorio Unico e Skills Comprovadas
======================================================================

PARTE 1 -- OPENREPOPOLICY:
  "Nao ha mais clones. Nao ha mais forks.
   So o REPOSITORIO PRINCIPAL. Todo mundo pega o resultado.
   Forks que mutilam o projeto sao PROIBIDOS."

  COMO FUNCIONA:
  - Repositorio principal (main) e a UNICA fonte de verdade
  - Cidadaos PUXAM (pull) do main para local
  - Mudancas sao PROPOSTAS (merge request) e VOTADAS (P4)
  - Ninguem copia o projeto e faz versao propria
  - Tudo e UNICO. Tudo e bem comum (CC0)

PARTE 2 -- OPENSKILLS:
  "Curriculum vitae e PAPEL. OpenSkills e VIVO.
   Skills comprovadas pela INTERACAO com o sistema.
   Nao 'eu sei Rust'. 'O SISTEMA TESTOU e APROVOU'."

  COMO FUNCIONA:
  - Cada cidadao tem um repositorio de skills
  - Skills sao COMPROVADAS pelo sistema (nao auto-declaradas)
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

classe RepoAction herda de Enum:
    PULL = "puxar"  // pegar do main para local
    PROPOSE = "propor"  // propor mudanca no main
    VOTE = "votar"  // votar em proposta
    MERGE = "integrar"  // integrar proposta aprovada
    REJECT = "rejeitar"  // rejeitar proposta
    SYNC = "sincronizar"  // atualizar local com main


classe MergeStatus herda de Enum:
    DRAFT = "rascunho"
    PROPOSED = "proposta"  // proposta feita
    IN_REVIEW = "em_revisao"  // assembleia analisando
    VOTING = "votacao"  // votacao aberta
    APPROVED = "aprovada"  // assembleia aprovou
    REJECTED = "rejeitada"  // assembleia rejeitou
    MERGED = "integrada"  // integrada no main
    AUTO_REJECTED = "auto_rejeitada"  // viola principios (P1-P4)


// decorador: @dataclass
classe MergeProposal:
    // Uma proposta de mudanca no repositorio principal.
    proposal_id: texto
    title: texto
    author: texto // quem propos
    seja description: texto = ""
    seja files_changed: [texto] = field(default_factory=list)
    seja lines_added: inteiro = 0
    seja lines_removed: inteiro = 0

    seja status: MergeStatus = MergeStatus.DRAFT
    seja votes_for: inteiro = 0
    seja votes_against: inteiro = 0
    seja total_voters: inteiro = 10000
    seja quorum_needed: flutuante = 0.51 // 51% para aprovar

    // Validacao automatica
    seja passes_constitution: logico = verdadeiro
    seja fails_reason: texto = ""
    seja tested: logico = falso // rodou sem erro?
    seja test_result: texto = ""

    seja created_date: texto = ""
    seja merged_date: texto = ""


classe RepoEngine:
    // Motor do repositorio unico da Republica.

    REGRAS:
    1. UM repositorio. UMA fonte de verdade. SEM forks.
    2. Todo mundo PUXA do main (pull). Ninguem copia.
    3. Mudancas sao PROPOSTAS. VOTADAS. INTEGRADAS.
    4. Forks que mutilam sao PROIBIDOS (auto-rejeitados).
    5. Assembleia decide (P4) -- 51% para integrar.
    6. Tudo testado antes de integrar (sem quebrar).
    7. Tudo CC0 -- nao ha "propriedade" de codigo.

    O QUE e PROIBIDO:
    - Fork (copiar e fazer versao propria)
    - Mutilacao (pegar parte do projeto e descartar o resto)
    - Propriedade privada de codigo (tudo CC0)
    - Mudanca sem votacao
    - Mudanca que quebra principios (P1-P4)

    O QUE e PERMITIDO:
    - Pull (puxar para local, usar, aprender)
    - Propor mudanca (qualquer cidadao)
    - Votar em mudanca (assembleia)
    - Usar parte do codigo em OUTRO projeto (CC0 permite)
    - Mas o PROJETO PRINCIPAL e UNICO
    // 

    funcao __init__(self):
        self.proposals: {texto: MergeProposal} = {}
        self.repo_stats: {texto: qualquer} = {
            "total_files": 0,
            "total_lines": 0,
            "total_commits": 0,
            "last_sync": "",
        }
        self.forks_rejected: inteiro = 0
        self.proposals_merged: inteiro = 0

    funcao pull(self, citizen_id: texto) -> {texto: qualquer}:
        // Cidadao puxa repositorio principal para local.
        retorne {
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
                seja description: texto = "",
                seja files: [texto] = nulo,
                seja added: inteiro = 0, removed: inteiro = 0,
                seja passes_constitution: logico = verdadeiro,
                seja fails_reason: texto = "",
                seja tested: logico = verdadeiro) -> {texto: qualquer}:
        // Propor mudanca no repositorio principal.
        pid = hashlib.md5("{title}{author}".encode()).hexdigest()[:8]

        se nao passes_constitution entao:
            self.forks_rejected += 1
            retorne {
                "proposal_id": pid,
                "status": "AUTO_REJEITADA",
                "reason": fails_reason  ou  "Viola P1-P4",
                "message": (
                    "Proposta REJEITADA automaticamente: {fails_reason}. "
                    "A Republica NAO aceita mudancas que violam principios."
                ),
            }

        proposal = MergeProposal(
            proposal_id = pid, title=title, author=author,
            description = description, files_changed=files ou [],
            lines_added = added, lines_removed=removed,
            status = tested ? MergeStatus.PROPOSED : MergeStatus.DRAFT,
            passes_constitution = verdadeiro, tested=tested,
            test_result = tested ? "PASSOU" : "NAO TESTADO",
            created_date = datetime.now().isoformat(),
        )
        self.proposals[pid] = proposal

        retorne {
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
        se nao proposal entao:
            retorne {"error": "Proposta nao encontrada"}

        proposal.votes_for = votes_for
        proposal.votes_against = votes_against
        total = votes_for + votes_against
        pct_for = votes_for / maximo(total, 1)

        se pct_for >= proposal.quorum_needed entao:
            proposal.status = MergeStatus.APPROVED
            self._merge(proposal)
            retorne {
                "proposal": proposal.title,
                "result": "APROVADA",
                "votes": "{votes_for}/{total} ({pct_for:.0%})",
                "merged": verdadeiro,
                "message": "Proposta APROVADA por {pct_for:.0%}. Integrada ao main.",
            }
        senao:
            proposal.status = MergeStatus.REJECTED
            retorne {
                "proposal": proposal.title,
                "result": "REJEITADA",
                "votes": "{votes_for}/{total} ({pct_for:.0%})",
                "message": "Proposta REJEITADA. {pct_for:.0%} a favor (precisava {proposal.quorum_needed:.0%}).",
            }

    funcao _merge(self, proposal: MergeProposal) -> None:
        proposal.status = MergeStatus.MERGED
        proposal.merged_date = datetime.now().isoformat()
        self.repo_stats["total_lines"] += proposal.lines_added - proposal.lines_removed
        self.repo_stats["total_commits"] += 1
        self.proposals_merged += 1

    funcao reject_fork(self, citizen: texto, reason: texto) -> {texto: qualquer}:
        // Rejeita tentativa de fork.
        self.forks_rejected += 1
        retorne {
            "citizen": citizen,
            "action": "FORK REJEITADO",
            "reason": reason,
            "policy": (
                "A Republica PROIBE forks que mutilam o projeto. "
                "Existe UM repositorio. UM projeto. UMA fonte de verdade. "
                "Voce pode PROPOR mudancas (merge request). "
                "Nao pode COPIAR e fazer versao propria. "
                "P1 anti-elitismo: projeto e de TODOS, nao de cada um."
            ),
            "alternative": "Proponha sua mudanca. A assembleia vota.",
        }

    funcao repo_status(self) -> {texto: qualquer}:
        retorne {
            "repositorio": "UNICO (main)",
            "forks_permitidos": 0,
            "fonte_de_verdade": "REPOSITORIO PRINCIPAL",
            **self.repo_stats,
            "propostas_totais": tamanho(self.proposals),
            "propostas_integradas": self.proposals_merged,
            "forks_rejeitados": self.forks_rejected,
            "licenca": "CC0 universal",
            "propriedade": "BEM COMUM (ninguem e dono)",
        }


// ============================================================================
// 2. OPENSKILLS (substituto do curriculum vitae)
// ============================================================================

classe SkillProof herda de Enum:
    // Como uma skill e COMPROVADA (nao auto-declarada).
    SYSTEM_TESTED = "sistema_testou"  // OpenGamesRealistic / OpenLegoCode testou
    TASK_COMPLETED = "tarefa_completada"  // OpenLaborRelay registrou
    COURSE_CERTIFIED = "curso_certificado"  // OpenUniversity certificou
    PEER_VERIFIED = "pares_verificaram"  // outros cidadaos atestaram
    CONTRIBUTION = "contribuicao"  // codigo/arte/conteudo no repositorio
    MENTOR_ENDORSED = "mentor_endossou"  // mentor (senior/mestre) endossou
    DEMONSTRATED = "demonstrou"  // demonstrou ao vivo (evento, stream)


classe SkillLevel herda de Enum:
    NONE = ("nenhum", 0)
    AWARE = ("conhece", 1)  // ja ouviu falar
    BASIC = ("basico", 2)  // consegue fazer simples
    INTERMEDIATE = ("intermediario", 3)
    ADVANCED = ("avancado", 4)
    EXPERT = ("especialista", 5)
    MASTER = ("mestre", 6)


    // decorador: @property
    funcao label(self) -> texto:
        retorne self.value[0]

    // decorador: @property
    funcao level_num(self) -> inteiro:
        retorne self.value[1]


// decorador: @dataclass
classe VerifiedSkill:
    // Uma skill COMPROVADA pelo sistema.
    skill_id: texto
    skill_name: texto                  // ex: "programacao_rust", "cirurgia_dental"
    category: texto // software, saude, construcao, etc
    seja level: SkillLevel = SkillLevel.NONE
    seja proofs: [Dict] = field(default_factory=list)

    // Comprovacoes
    seja system_tests_passed: inteiro = 0
    seja tasks_completed: inteiro = 0
    seja courses_certified: inteiro = 0
    seja peer_verifications: inteiro = 0
    seja contributions: inteiro = 0
    seja mentor_endorsements: inteiro = 0
    seja demonstrations: inteiro = 0

    // Score de confianca
    seja confidence: flutuante = 0.0 // 0-1 (quao confiavel e a skill)

    // decorador: @property
    funcao is_verified(self) -> logico:
        retorne tamanho(self.proofs) > 0 e self.confidence > 0.3


// decorador: @dataclass
classe SkillProfile:
    // Perfil de skills de um cidadao -- SUBSTITUI o curriculum vitae.

    DIFERENCA vs CV tradicional:
    - CV: voce ESCREVE o que sabe. Ninguem verifica.
    - OpenSkills: o SISTEMA COMPROVA. Voce nao auto-declara.

    - CV: papel estatico. Desatualizado em 1 mes.
    - OpenSkills: VIVO. Atualiza toda vez que voce faz algo.

    - CV: "eu sei Rust". (menta? verdade? quem sabe?)
    - OpenSkills: "Sistema testou: Rust AVANCADO (8 testes, 12 tarefas, 3 contribuicoes)"

    - CV: usado para excluir (sem diploma = rejeitado)
    - OpenSkills: usado para CONECTAR (skill certa para tarefa certa)
    // 
    citizen_id: texto
    citizen_name: texto
    seja age: inteiro = 0
    seja profession: texto = ""
    seja profession_level: texto = ""  // OpenProfessions (aprendiz -> mestre)
    seja skills: {texto: VerifiedSkill} = field(default_factory=dict)
    seja created_date: texto = ""

    // Stats
    seja total_skills_verified: inteiro = 0
    seja total_tasks_completed: inteiro = 0
    seja total_contributions: inteiro = 0
    seja impact_score: flutuante = 0.0 // OpenCredit/OpenCreator

    // decorador: @property
    funcao skill_count(self) -> inteiro:
        retorne tamanho(self.skills)

    // decorador: @property
    funcao verified_count(self) -> inteiro:
        retorne soma(1 para s em self.skills.values() if s.is_verified)


classe SkillsEngine:
    // Motor de skills verificadas.

    COMO UMA SKILL e COMPROVADA:

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

    NENHUMA skill e auto-declarada.
    TUDO e comprovado por INTERACAO com o sistema.
    // 

    funcao __init__(self):
        self.profiles: {texto: SkillProfile} = {}

    funcao create_profile(self, citizen_id: texto, name: texto,
                       seja age: inteiro = 0, profession: texto = ""
                       ) -> {texto: qualquer}:
        profile = SkillProfile(
            citizen_id = citizen_id, citizen_name=name,
            age = age, profession=profession,
            created_date = datetime.now().isoformat(),
        )
        self.profiles[citizen_id] = profile
        retorne {"created": verdadeiro, "citizen": name, "message": "Perfil OpenSkills criado para {name}."}

    funcao add_proof(self, citizen_id: texto, skill_name: texto,
                  category: texto, proof_type: SkillProof,
                  seja proof_detail: texto = "",
                  seja level: SkillLevel = SkillLevel.BASIC) -> {texto: qualquer}:
        // Adiciona comprovacao de skill.
        profile = self.profiles.get(citizen_id)
        se nao profile entao:
            retorne {"error": "Perfil nao encontrado"}

        sid = hashlib.md5("{citizen_id}{skill_name}".encode()).hexdigest()[:8]

        se sid nao in profile.skills entao:
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
        se proof_type == SkillProof.SYSTEM_TESTED entao:
            skill.system_tests_passed += 1
        senao se proof_type == SkillProof.TASK_COMPLETED entao:
            skill.tasks_completed += 1
        senao se proof_type == SkillProof.COURSE_CERTIFIED entao:
            skill.courses_certified += 1
        senao se proof_type == SkillProof.PEER_VERIFIED entao:
            skill.peer_verifications += 1
        senao se proof_type == SkillProof.CONTRIBUTION entao:
            skill.contributions += 1
        senao se proof_type == SkillProof.MENTOR_ENDORSED entao:
            skill.mentor_endorsements += 1
        senao se proof_type == SkillProof.DEMONSTRATED entao:
            skill.demonstrations += 1

        // Recalcular nivel (mais provas = nivel maior)
        total_proofs = tamanho(skill.proofs)
        levels = [SkillLevel.NONE, SkillLevel.AWARE, SkillLevel.BASIC,
                  SkillLevel.INTERMEDIATE, SkillLevel.ADVANCED,
                  SkillLevel.EXPERT, SkillLevel.MASTER]
        skill.level = levels[minimo(total_proofs, tamanho(levels) - 1)]

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

        se skill.is_verified e skill.level.level_num >= 2 entao:
            profile.total_skills_verified += 1

        retorne {
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

    funcao get_profile(self, citizen_id: texto) -> {texto: qualquer}:
        // Retorna perfil de skills (substitui CV).
        profile = self.profiles.get(citizen_id)
        se nao profile entao:
            retorne {"error": "Perfil nao encontrado"}

        retorne {
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
                    "proofs": tamanho(s.proofs),
                    "proofs_detail": [
                        "{p['type']}: {p['detail']}" para p em s.proofs[:3]
                    ],
                }
                para s em ordene(profile.skills.values(),
                                key = (x) -> -x.level.level_num)
            ],
            "message": (
                "Perfil OpenSkills de {profile.citizen_name}: "
                "{profile.verified_count} skills verificadas de {profile.skill_count}. "
                "Tudo COMPROVADO pelo sistema."
            ),
        }

    funcao search_by_skill(self, skill_name: texto,
                        seja min_level: inteiro = 2) -> [Dict]:
        // Busca cidadaos com skill (para OpenLaborRelay).
        results = []
        para cada profile em self.profiles.values():
            para cada skill em profile.skills.values():
                if (skill.skill_name.lower() == skill_name.lower()
                     e skill.level.level_num >= min_level
                     e skill.is_verified):
                    results.append({
                        "citizen": profile.citizen_name,
                        "skill": skill.skill_name,
                        "level": skill.level.label,
                        "confidence": "{skill.confidence:.0%}",
                        "proofs": tamanho(skill.proofs),
                    })
        retorne results

    funcao compare_to_cv(self) retorna List[{texto: texto}]:
        // Compara OpenSkills com curriculum vitae tradicional.
        retorne [
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
             "cv_tradicional": "Baixa (quem sabe se e verdade?)",
             "openskills": "Alta (sistema testou, pares verificaram)"},
            {"aspecto": "Bias",
             "cv_tradicional": "Nome, idade, genero, aparencia influenciam",
             "openskills": "So skills importam. Sem bias visual."},
        ]

    funcao stats(self) -> {texto: qualquer}:
        all_skills = []
        para cada p em self.profiles.values():
            all_skills.extend(s.skill_name para s em p.skills.values())
        retorne {
            "total_perfis": tamanho(self.profiles),
            "total_skills_registradas": tamanho(all_skills),
            "skills_unicas": tamanho(set(all_skills)),
            "skills_mais_comuns": dict(Counter(all_skills).most_common(5)),
        }


// ============================================================================
// 3. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    repo = RepoEngine()
    skills = SkillsEngine()

    imprima("=" * 80)
    imprima("  OPENREPOPOLICY + OPENSKILLS")
    imprima("  Repositorio unico + Skills comprovadas pelo sistema")
    imprima("=" * 80)

    // === PARTE 1: REPOSITORIO ===
    imprima("\n\n  {'='*40}")
    imprima("  PARTE 1: OPENREPOPOLICY")
    imprima("  {'='*40}\n")

    // Status do repositorio
    repo.repo_stats = {
        "total_files": 130, "total_lines": 700000,
        "total_commits": 500, "last_sync": datetime.now().isoformat(),
    }

    // Pull
    imprima("  === PULL (pegar do main) ===\n")
    p = repo.pull("cleiton")
    imprima("  {p['message']}")

    // Proposta aprovada
    imprima("\n\n  === PROPOSTA APROVADA ===\n")
    r = repo.propose("cleiton", "Adicionar OpenMetaCognition",
                     "Novo sistema de auto-consciencia cognitiva",
                     ["open_metacognition.py"], 800, 0, verdadeiro, "", verdadeiro)
    imprima("  {r['message']}")
    vote = repo.vote(r["proposal_id"], 6500, 3500)
    imprima("  {vote['message']}")

    // Proposta rejeitada (viola P1-P4)
    imprima("\n\n  === PROPOSTA AUTO-REJEITADA (viola principios) ===\n")
    r2 = repo.propose("anonimo", "Criar sistema de pagamento privado",
                      "Sistema de dinheiro para elites",
                      passes_constitution = falso,
                      fails_reason = "Viola P1 anti-elitismo + cria moeda privada")
    imprima("  {r2['message']}")

    // Fork rejeitado
    imprima("\n\n  === FORK REJEITADO ===\n")
    fork = repo.reject_fork("joao", "Tentou copiar OpenHealth e remover modulos de saude mental")
    imprima("  {fork['citizen']}: {fork['action']}")
    imprima("  Politica: {fork['policy']}")
    imprima("  Alternativa: {fork['alternative']}")

    // Status repositorio
    imprima("\n\n  === STATUS DO REPOSITORIO ===\n")
    status = repo.repo_status()
    para cada (k, v) em status.items():
        imprima("  {k:<30} {v}")

    // === PARTE 2: OPENSKILLS ===
    imprima("\n\n  {'='*40}")
    imprima("  PARTE 2: OPENSKILLS")
    imprima("  {'='*40}\n")

    // Criar perfis
    imprima("  === CRIANDO PERFIS ===\n")
    skills.create_profile("C-001", "Cleiton", 35, "Programador/Fundador")
    skills.create_profile("C-002", "Maria", 28, "Medica")
    skills.create_profile("C-003", "Joao", 45, "Pedreiro (autodidata)")
    skills.create_profile("C-004", "Ana", 22, "Estudante")

    // Adicionar provas (COMPROVADAS pelo sistema)
    imprima("\n  === ADICIONANDO PROVAS COMPROVADAS ===\n")

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
    para skill, cat, proof, detail, level in proofs_cleiton:
        r = skills.add_proof("C-001", skill, cat, proof, detail, level)
        imprima("  {r['citizen']}: {r['skill']} -> {r['level']} "
              "(confianca: {r['confidence']})")

    // Cleiton: arquitetura modular
    r = skills.add_proof("C-001", "arquitetura_modular", "software",
                         SkillProof.CONTRIBUTION,
                         "Criou OpenModularArchitecture (51+ modulos)",
                         SkillLevel.MASTER)
    imprima("  {r['citizen']}: {r['skill']} -> {r['level']}")

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
    para skill, cat, proof, detail, level in proofs_maria:
        r = skills.add_proof("C-002", skill, cat, proof, detail, level)
        imprima("  {r['citizen']}: {r['skill']} -> {r['level']} "
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
    para skill, cat, proof, detail, level in proofs_joao:
        r = skills.add_proof("C-003", skill, cat, proof, detail, level)
        imprima("  {r['citizen']}: {r['skill']} -> {r['level']} "
              "(confianca: {r['confidence']})")

    // Ana: estudante aprendendo
    proofs_ana = [
        ("programacao_rust", "software", SkillProof.SYSTEM_TESTED,
         "OpenGamesRealistic: programador simulator (70%)", SkillLevel.BASIC),
        ("primeiros_socorros", "saude", SkillProof.SYSTEM_TESTED,
         "OpenGamesRealistic: simulador doutor (80%)", SkillLevel.BASIC),
    ]
    para skill, cat, proof, detail, level in proofs_ana:
        r = skills.add_proof("C-004", skill, cat, proof, detail, level)
        imprima("  {r['citizen']}: {r['skill']} -> {r['level']} "
              "(confianca: {r['confidence']})")

    // === PERFIL COMPLETO (substitui CV) ===
    imprima("\n\n  === PERFIL OPENSKILLS (substitui CV) ===\n")
    para cada cid em ["C-001", "C-002", "C-003", "C-004"]:
        profile = skills.get_profile(cid)
        imprima("\n  {profile['citizen']} ({profile['profession']})")
        imprima("  Skills verificadas: {profile['verified_skills']}/{profile['total_skills']}")
        para cada s em profile["skills"][:3]:
            imprima("    [{s['level']:<13}] {s['skill']:<25} "
                  "conf: {s['confidence']} provas: {s['proofs']}")
            para cada d em s["proofs_detail"][:1]:
                imprima("      -> {d[:60]}")

    // === BUSCAR POR SKILL ===
    imprima("\n\n  === BUSCAR: quem sabe Rust? ===\n")
    rust_devs = skills.search_by_skill("programacao_rust", min_level=2)
    para cada dev em rust_devs:
        imprima("  {dev['citizen']:<15} {dev['level']:<13} "
              "conf: {dev['confidence']} provas: {dev['proofs']}")

    imprima("\n  === BUSCAR: quem sabe alvenaria? ===\n")
    builders = skills.search_by_skill("alvenaria", min_level=2)
    para cada b em builders:
        imprima("  {b['citizen']:<15} {b['level']:<13} "
              "conf: {b['confidence']} provas: {b['proofs']}")

    // === COMPARACAO CV vs OPENSKILLS ===
    imprima("\n\n  === CV TRADICIONAL vs OPENSKILLS ===\n")
    comp = skills.compare_to_cv()
    imprima("  {'Aspecto':<15} {'CV Tradicional':<30} {'OpenSkills'}")
    imprima("  {'-'*75}")
    para cada c em comp:
        imprima("  {c['aspecto']:<15} {c['cv_tradicional'][:29]:<30} {c['openskills'][:35]}")

    // === STATS ===
    imprima("\n\n  === ESTATISTICAS ===\n")
    s = skills.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA: REPOSITORIO UNICO + SKILLS COMPROVADAS")
    imprima("{'='*80}")
    imprima("""
  REPOSITORIO UNICO (sem forks):
    Um projeto. Uma fonte de verdade. Sem copias.
    Forks que mutilam sao PROIBIDOS.
    Mudancas sao PROPOSTAS -> VOTADAS -> INTEGRADAS.
    Assembleia decide (P4). 51% para integrar.
    Tudo CC0. Ninguem e dono. Todos herdeiros.

    O que pode: PULL (puxar), PROPOR (merge request), VOTAR.
    O que nao pode: FORK (copiar), MUTILAR (descartar partes),
    PROPRIEDADE (codigo e bem comum).

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

    NENHUMA skill e auto-declarada.
    TUDO e comprovado por INTERACAO com o sistema.

    Joao (pedreiro autodidata):
    CV tradicional: "sem diploma" -> REJEITADO.
    OpenSkills: 20 anos de pratica, 150 obras, 5 verificacoes de pares,
    mentor endossou -> ALVENARIA EXPERT. APROVADO.

    Ana (22 anos, estudante):
    CV tradicional: "sem experiencia" -> REJEITADA.
    OpenSkills: simulador 70%, Rust BASICO -> em crescimento. CONECTADA.

  PRINCIPIOS:
    P1: Repositorio unico (sem elite de codigo). Skills por competencia (nao diploma).
    P2: Cidadao escolhe se perfil e publico. Skills sao suas.
    seja P3: Contribuir no repositorio = trabalho de alto impacto.
    P4: Assembleia vota mudancas. Skills verificadas por pares.
// )
    imprima("{'='*80}")
    rs = repo.repo_status()
    imprima("  Repo: {rs['repositorio']} | {rs['propostas_integradas']} integradas | "
          "{rs['forks_rejeitados']} forks rejeitados.")
    imprima("  Skills: {s['total_perfis']} perfis, {s['skills_unicas']} skills unicas.")
    imprima("  Sem fork. Sem CV. So Republica.")
    imprima("{'='*80}")

```
