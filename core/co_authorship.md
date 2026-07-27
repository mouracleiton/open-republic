# CoAuthorship -- Two-Person Rule para Produção

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/co_authorship.py`

**Descricao:** ==============================================
"Para ser justo, precisa das duas mãos.
 Uma escreve. A outra revisa.
 Nenhuma publica sozinha."
COMO FUNCIONA:
  1. TODO pull request precisa de 2 aprovações
  2. Um Autor (quem escreve o código)
  3. Um Revisor (quem revisa e aprova/rejeita)
  4. Autor NÃO pode aprovar próprio PR
  5. Sem os dois: não entra em produção
ISTRUMENTOS DE COAUTORIA:
  - Pair Programming: autor + revisor escrevem juntos
  - Code Review: revisor lê, comenta, aprova/rejeita
  - Production Gate: PR só deploya com 2 assinaturas
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50, ver open_cofounder_reparation)

---

```portugol++

// !/usr/bin/env python3
// 
CoAuthorship -- Two-Person Rule para Produção
==============================================

"Para ser justo, precisa das duas mãos.
 Uma escreve. A outra revisa.
 Nenhuma publica sozinha."

COMO FUNCIONA:
  1. TODO pull request precisa de 2 aprovações
  2. Um Autor (quem escreve o código)
  3. Um Revisor (quem revisa e aprova/rejeita)
  4. Autor NÃO pode aprovar próprio PR
  5. Sem os dois: não entra em produção

ISTRUMENTOS DE COAUTORIA:
  - Pair Programming: autor + revisor escrevem juntos
  - Code Review: revisor lê, comenta, aprova/rejeita
  - Production Gate: PR só deploya com 2 assinaturas

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50, ver open_cofounder_reparation)
// 

// importa annotations de __future__

// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa datetime de datetime


// ============================================================================
// 1. CONTRIBUIDORES
// ============================================================================

// decorador: @dataclass
classe Contributor:
    // Um co-autor do sistema.
    contributor_id: texto
    name: texto
    email: texto
    role: texto   // "cofundador", "socio", "desenvolvedor", "comunidade"
    seja full_access: logico = falso
    seja can_author: logico = verdadeiro
    seja can_review: logico = verdadeiro
    seja joined_at: flutuante = 0.0


// Os 2 cofundadores com FULL ACCESS
// IMPORTANTE: O 'CO' de cofundador NAO e subordinacao.
// E REPARACAO HISTORICA. Sao DOIS fundadores iguais (50/50).
// Ver modulo: open_cofounder_reparation
COFOUNDERS = {
    "cleiton": Contributor(
        contributor_id = "cleiton",
        name = "Cleiton Moura Loura",
        email = "cleiton@teia.dev",
        role = "cofundador",
        full_access = verdadeiro,
        can_author = verdadeiro,
        can_review = verdadeiro,
    ),
    "ming": Contributor(
        contributor_id = "ming",
        name = "MING",
        email = "ming@teia.dev",
        role = "cofundadora",
        full_access = verdadeiro,
        can_author = verdadeiro,
        can_review = verdadeiro,
    ),
}


// ============================================================================
// 2. PULL REQUEST (o artefato)
// ============================================================================

classe PRStatus herda de Enum:
    DRAFT = "rascunho"
    AUTHORED = "autor_escreveu"
    IN_REVIEW = "em_revisao"
    APPROVED_BY_AUTHOR = "autor_aprovou"
    APPROVED_BY_REVIEWER = "revisor_aprovou"
    APPROVED_BOTH = "ambos_aprovaram"  // = pode deployar
    REJECTED = "rejeitado"
    MERGED = "em_producao"
    BLOCKED = "bloqueado_desacordo"


// decorador: @dataclass
classe CodeChange:
    // Uma mudança no código que vira PR.
    change_id: texto
    title: texto
    description: texto
    seja files_changed: [texto] = field(default_factory=list)
    seja author_id: texto = ""
    seja reviewer_id: texto = ""
    seja author_approved: logico = falso
    seja reviewer_approved: logico = falso
    seja status: PRStatus = PRStatus.DRAFT
    seja comments: [Dict] = field(default_factory=list)
    seja created_at: flutuante = 0.0
    seja updated_at: flutuante = 0.0

    // decorador: @property
    funcao can_deploy(self) -> logico:
        // Só deploya se AMBOS aprovaram E não é o mesmo banco de pessoa.
        retorne (
            self.author_approved
             e self.reviewer_approved
             e self.author_id != self.reviewer_id
             e self.status == PRStatus.APPROVED_BOTH
        )

    // decorador: @property
    funcao needs_author(self) -> logico:
        retorne nao self.author_approved

    // decorador: @property
    funcao needs_reviewer(self) -> logico:
        retorne nao self.reviewer_approved


// ============================================================================
// 3. MOTOR DE COAUTORIA (Two-Person Rule)
// ============================================================================

classe CoAuthorshipEngine:
    // Gerencia PRs com two-person rule.

    REGRA DE OURO:
      NENHUMA mudança entra em produção sem 2 assinaturas.
      NENHUMA pessoa assina 2x (autor e revisor devem ser diferentes).

    PAIR PROGRAMMING:
      Quando author_id e reviewer_id escrevem juntos,
      ambos são creditados como co-autores.
    // 

    funcao __init__(self):
        self.contributors: {texto: Contributor} = dict(COFOUNDERS)
        self.prs: {texto: CodeChange} = {}
        self.deploy_log: [Dict] = []

    funcao add_contributor(self, c: Contributor):
        self.contributors[c.contributor_id] = c

    funcao create_pr(
        self,
        change_id: texto,
        title: texto,
        description: texto,
        author_id: texto,
        reviewer_id: texto,
        seja files_changed: [texto] = nulo,
    ) -> CodeChange:
        // Cria um PR novo. Autor e revisor já definidos.

        se author_id nao in self.contributors entao:
            lance ValueError("Autor {author_id} não registrado")
        se reviewer_id nao in self.contributors entao:
            lance ValueError("Revisor {reviewer_id} não registrado")

        se author_id == reviewer_id entao:
            lance ValueError(
                "VIOLAÇÃO DE COAUTORIA: autor e revisor NÃO PODEM ser a mesma pessoa. "
                "Two-person rule exige duas assinaturas diferentes."
            )

        pr = CodeChange(
            change_id = change_id,
            title = title,
            description = description,
            author_id = author_id,
            reviewer_id = reviewer_id,
            files_changed = files_changed ou [],
        )
        self.prs[change_id] = pr
        retorne pr

    funcao author_approve(self, change_id: texto, contributor_id: texto) -> {texto: qualquer}:
        // Autor aprova o PR (confirma que o código está pronto para revisão).

        pr = self.prs[change_id]
        se nao pr entao:
            retorne {"error": "PR não encontrado"}

        se contributor_id != pr.author_id entao:
            retorne {"error": "Só o autor ({pr.author_id}) pode auto-aprovar"}

        pr.author_approved = verdadeiro
        pr.status = PRStatus.IN_REVIEW
        pr.updated_at = datetime.now().timestamp()

        retorne self._check_both_approved(pr)

    funcao reviewer_approve(self, change_id: texto, contributor_id: texto) -> {texto: qualquer}:
        // Revisor aprova o PR após code review.

        pr = self.prs[change_id]
        se nao pr entao:
            retorne {"error": "PR não encontrado"}

        se contributor_id != pr.reviewer_id entao:
            retorne {"error": "Só o revisor ({pr.reviewer_id}) pode revisar"}

        se nao pr.author_approved entao:
            retorne {"error": "Autor ainda não submeteu para revisão"}

        pr.reviewer_approved = verdadeiro
        pr.updated_at = datetime.now().timestamp()

        retorne self._check_both_approved(pr)

    funcao reject(self, change_id: texto, contributor_id: texto, reason: texto) -> {texto: qualquer}:
        // Qualquer um dos dois pode rejeitar com justificativa.

        pr = self.prs[change_id]
        se nao pr entao:
            retorne {"error": "PR não encontrado"}

        se contributor_id nao in (pr.author_id, pr.reviewer_id) entao:
            retorne {"error": "Só autor ou revisor podem rejeitar"}

        pr.status = PRStatus.REJECTED
        pr.comments.append({
            "by": contributor_id,
            "type": "reject",
            "reason": reason,
            "timestamp": datetime.now().timestamp(),
        })

        retorne {
            "rejected": verdadeiro,
            "by": contributor_id,
            "reason": reason,
            "status": pr.status.value,
        }

    funcao add_comment(self, change_id: texto, contributor_id: texto, comment: texto):
        // Adiciona comentário ao PR (code review).

        pr = self.prs[change_id]
        se nao pr entao:
            retorne nulo

        pr.comments.append({
            "by": contributor_id,
            "type": "comment",
            "text": comment,
            "timestamp": datetime.now().timestamp(),
        })

    funcao deploy(self, change_id: texto, requested_by: texto) -> {texto: qualquer}:
        // Deploy para produção. SÓ se ambos aprovaram.

        pr = self.prs[change_id]
        se nao pr entao:
            retorne {"error": "PR não encontrado"}

        se nao pr.can_deploy entao:
            missing = []
            se pr.needs_author entao:
                missing.append("aprovação do autor ({pr.author_id})")
            se pr.needs_reviewer entao:
                missing.append("aprovação do revisor ({pr.reviewer_id})")

            retorne {
                "error": "DEPLOY BLOQUEADO",
                "reason": "Falta: {', '.join(missing)}",
                "two_person_rule": "Ambos devem aprovar. Uma pessoa não basta.",
            }

        pr.status = PRStatus.MERGED

        deploy_record = {
            "change_id": change_id,
            "title": pr.title,
            "author": pr.author_id,
            "reviewer": pr.reviewer_id,
            "deployed_by": requested_by,
            "timestamp": datetime.now().timestamp(),
            "files_changed": pr.files_changed,
        }
        self.deploy_log.append(deploy_record)

        retorne {
            "deployed": verdadeiro,
            "change_id": change_id,
            "co_authors": [pr.author_id, pr.reviewer_id],
            "message": "Deploy autorizado por {pr.author_id} + {pr.reviewer_id}.",
        }

    funcao _check_both_approved(self, pr: CodeChange) -> {texto: qualquer}:
        // Verifica se ambos já aprovaram.

        se pr.author_approved e pr.reviewer_approved entao:
            pr.status = PRStatus.APPROVED_BOTH
            retorne {
                "both_approved": verdadeiro,
                "can_deploy": verdadeiro,
                "author": pr.author_id,
                "reviewer": pr.reviewer_id,
                "message": (
                    "PR aprovado por {pr.author_id} (autor) e "
                    "{pr.reviewer_id} (revisor). Pronto para deploy."
                ),
            }

        retorne {
            "both_approved": falso,
            "author_approved": pr.author_approved,
            "reviewer_approved": pr.reviewer_approved,
            "waiting_for": (
                "revisor ({pr.reviewer_id})" if pr.author_approved  e  nao  pr.reviewer_approved
                else "autor ({pr.author_id})" if nao  pr.author_approved
                else "ninguém (erro)"
            ),
        }

    funcao status_report(self) -> texto:
        // Relatório de todos os PRs.

        lines = []
        lines.append("=" * 100)
        lines.append("COAUTORIA -- STATUS DOS PULL REQUESTS")
        lines.append("Two-Person Rule: nada em produção sem 2 assinaturas")
        lines.append("=" * 100)
        lines.append("")

        lines.append("{'ID':<12} {'TÍTULO':<35} {'AUTOR':<10} {'REVISOR':<10} {'AUTOR?':>7} {'REV?':>7} {'STATUS':<20}")
        lines.append("-" * 100)

        para cada pr em self.prs.values():
            aut = pr.author_approved ? "✓" : "---"
            rev = pr.reviewer_approved ? "✓" : "---"
            lines.append(
                "{pr.change_id:<12} "
                "{pr.title[:35]:<35} "
                "{pr.author_id:<10} "
                "{pr.reviewer_id:<10} "
                "{aut:>7} "
                "{rev:>7} "
                "{pr.status.value:<20}"
            )

        lines.append("")
        lines.append("DEPLOYS EM PRODUÇÃO: {len(self.deploy_log)}")
        para cada d em self.deploy_log:
            lines.append(
                "  {d['change_id']}: {d['title']} "
                "(autor: {d['author']}, revisor: {d['reviewer']})"
            )

        retorne "\n".join(lines)


// ============================================================================
// 4. DEMO: COMO FUNCIONA NA PRÁTICA
// ============================================================================

se __name__ == "__main__" entao:
    engine = CoAuthorshipEngine()

    // PR #1: MING escreve, Cleiton revisa
    engine.create_pr(
        change_id = "PR-001",
        title = "Adicionar P5: Princípio Anti-Subalternização",
        description = (
            "Novo princípio constitucional: nenhuma pessoa é reduzida "
            "a marcador de identidade (sexo, sexualidade, raça, classe). "
            "Subalternização = violação constitucional. "
            "Autora: MING. Revisor: Cleiton."
        ),
        author_id = "ming",
        reviewer_id = "cleiton",
        files_changed = ["core/constitutional_engine.py", "core/constituent_assembly.py"],
    )

    // PR #2: Cleiton escreve, MING revisa
    engine.create_pr(
        change_id = "PR-002",
        title = "Adicionar dados de trabalho do cuidado (econômia invisível)",
        description = (
            "Incluir métricas de trabalho não-pago (cuidado de filhos, "
            "idosos, doentes, trabalho doméstico). "
            "P3 (trabalho igual) deve reconhecer trabalho invisível. "
            "Autor: Cleiton. Revisora: MING."
        ),
        author_id = "cleiton",
        reviewer_id = "ming",
        files_changed = ["core/open_labor_policy.py", "core/open_value_simulation.py"],
    )

    // PR #3: MING escreve, Cleiton revisa (crédito de coautoria)
    engine.create_pr(
        change_id = "PR-003",
        title = "Refatorar UX do Terminal: perspectiva de usabilidade feminina",
        description = (
            "Redesenhar fluxos do Terminal baseado em como mulheres "
            "navegam interfaces. Em vez de command-palette-only, "
            "adicionar caminhos visuais intuitivos. "
            "Autora: MING. Revisor: Cleiton."
        ),
        author_id = "ming",
        reviewer_id = "cleiton",
        files_changed = ["teia-terminal/templates/dashboard.html"],
    )

    // PR #4: TENTATIVA de uma pessoa aprovar tudo (DEVE FALHAR)
    imprima("=" * 100)
    imprima("TESTE: UM SÓ NÃO PUBLICA")
    imprima("=" * 100)
    imprima()

    // Autor aprova PR-001
    r = engine.author_approve("PR-001", "ming")
    imprima("PR-001: MING (autora) aprova -> {r}")
    imprima()

    // Tenta deployar com SÓ UM
    r = engine.deploy("PR-001", "ming")
    imprima("TENTATIVA DE DEPLOY COM UM SÓ: {r}")
    imprima()

    // Revisor aprova PR-001
    r = engine.reviewer_approve("PR-001", "cleiton")
    imprima("PR-001: Cleiton (revisor) aprova -> {r}")
    imprima()

    // Agora deploy funciona
    r = engine.deploy("PR-001", "cleiton")
    imprima("DEPLOY PR-001 (ambos aprovaram): {r}")
    imprima()

    // PR-002: Cleiton escreveu, mas MING ainda não revisou
    engine.author_approve("PR-002", "cleiton")
    r = engine.deploy("PR-002", "cleiton")
    imprima("TENTATIVA DE DEPLOY PR-002 sem MING: {r}")
    imprima()

    // PR-003: MING rejeita PR de UX sem revisão
    r = engine.reject("PR-002", "ming", "Faltou considerar fluxo de cuidado. Quem usa o terminal enquanto amamenta não pode depender de duas mãos no teclado.")
    imprima("PR-002: MING rejeita -> {r}")
    imprima()

    // Relatório final
    imprima()
    imprima(engine.status_report())

    // Tentar criar PR com mesma pessoa como autor E revisor
    imprima()
    imprima("=" * 100)
    imprima("TESTE: AUTOR = REVISOR (DEVE FALHAR)")
    imprima("=" * 100)
    tente:
        engine.create_pr(
            change_id = "PR-FAIL",
            title = "Tentativa de uma pessoa fazer tudo",
            description = "Isso deve falhar.",
            author_id = "cleiton",
            reviewer_id = "cleiton",
        )
    capture ValueError como e:
        imprima("BLOQUEADO: {e}")

    imprima()
    imprima("=" * 100)
    imprima("PRINCÍPIO DE COAUTORIA")
    imprima("=" * 100)
    imprima("""
  1. TODO pull request tem 2 pessoas: Autor + Revisor
  2. Autor e Revisor são PESSOAS DIFERENTES (two-person rule)
  3. Autor NÃO publica sem Revisor aprovar
  4. Revisor NÃO publica sem Autor submeter
  5. Ambos têm FULL ACCESS ao código
  6. NENHUMA mudança entra em produção sem 2 assinaturas
  7. Qualquer um dos dois pode REJEITAR com justificativa
  8. Co-autoria é creditada: git commit --author="Cleiton + MING"

  Isto NÃO é revisão técnica.
  Isto é COAUTORIA CONSTITUCIONAL.

  O sistema foi idealizado por um HOMEM.
  Para ser justo, precisa da CONTRAPARTE feminina.
  Não como diversidade. Como METADE DA FUNDAÇÃO.

  Pair Programming = escrever junto
  Code Review = revisar junto
  Production Gate = publicar junto (ou não publica)

  "Para ser justo, precisa das duas mãos.
   Uma escreve. A outra revisa.
   Nenhuma publica sozinha."
// )

```
