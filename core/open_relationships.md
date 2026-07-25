# OpenRelationships -- Politica de Transparencia Relacional + Anti-Inveja

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_relationships.py`

**Descricao:** =========================================================================
PERGUNTA SUBMETIDA A ASSEMBLEIA:
  "Todo relacionamento tem que ser publico? As pessoas precisam saber
   para nao cometer o problema de invasao de espaco. Nada de esconder."
O QUE A ASSEMBLEIA DECIDIU:
  APROVADO COM NUANCES:
  1. RELACIONAMENTOS DECLARADOS (sim, publicos)
     - Todo relacionamento e registrado no OpenSocialNetwork
     - Motivo: evitar invasao de espaco alheio
     - Motivo: transparencia gera confianca
     - Motivo: anti-inveja (saber que alguem esta com alguem elimina disputa)
  2. MAS P2 AUTONOMIA (nao obrigacao de detalhe)
     - VOCE declara que esta com quem (fato, nao detalhe)
     - Ninguem e obrigado a detalhar a RELACAO (intimidade)
     - "Estou com Maria" = sim. "O que faco com Maria" = nao
  3. ANTI-INVEJA (politica complementar)
     - Inveja e reconhecida como doenca social
     - Republica nao competi por pessoas
     - Todo cidadao e suficiente (OpenCreator + OpenCredit)
     - Quem tem relacionamento NAO e "melhor"
     - Quem nao tem NAO e "pior"
  4. O QUE NAO EXISTE:
     - Traicao (se tudo e publico, nao ha o que esconder)
     - Ciume possessivo (cada corpo e livre -- P2)
     - "Tomar" pessoa de outro (ninguem e dono de ninguem)
     - Relacionamento secreto (publico = regra)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRelationships -- Politica de Transparencia Relacional + Anti-Inveja
=========================================================================

PERGUNTA SUBMETIDA A ASSEMBLEIA:
  "Todo relacionamento tem que ser publico? As pessoas precisam saber
   para nao cometer o problema de invasao de espaco. Nada de esconder."

O QUE A ASSEMBLEIA DECIDIU:

  APROVADO COM NUANCES:
  1. RELACIONAMENTOS DECLARADOS (sim, publicos)
     - Todo relacionamento e registrado no OpenSocialNetwork
     - Motivo: evitar invasao de espaco alheio
     - Motivo: transparencia gera confianca
     - Motivo: anti-inveja (saber que alguem esta com alguem elimina disputa)

  2. MAS P2 AUTONOMIA (nao obrigacao de detalhe)
     - VOCE declara que esta com quem (fato, nao detalhe)
     - Ninguem e obrigado a detalhar a RELACAO (intimidade)
     - "Estou com Maria" = sim. "O que faco com Maria" = nao

  3. ANTI-INVEJA (politica complementar)
     - Inveja e reconhecida como doenca social
     - Republica nao competi por pessoas
     - Todo cidadao e suficiente (OpenCreator + OpenCredit)
     - Quem tem relacionamento nao e "melhor"
     - Quem nao tem nao e "pior"

  4. O QUE nao EXISTE:
     - Traicao (se tudo e publico, nao ha o que esconder)
     - Ciume possessivo (cada corpo e livre -- P2)
     - "Tomar" pessoa de outro (ninguem e dono de ninguem)
     - Relacionamento secreto (publico = regra)

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime


// ============================================================================
// 1. TIPOS DE RELACIONAMENTO
// ============================================================================

classe RelationshipType herda de Enum:
    PARTNER = "namoro"  // namoro
    MARRIAGE = "uniao"  // uniao estavel / casamento
    DATING = "encontro"  // ficante / encontro casual
    COMPANIONSHIP = "companhia"  // companhia (nao sexual)
    CO_PARENTING = "coparentalidade"  // criar filhos juntos
    POLY = "poliafectivo"  // relacionamento multilo
    FRIENDSHIP_INTIMATE = "amizade_intima"  // melhor amigo(a)
    MENTORSHIP = "mentoria"  // mentor/aprendiz


classe RelationshipStatus herda de Enum:
    ACTIVE = "ativo"
    PAUSED = "pausado"
    ENDED = "encerrado"
    MUTUAL_AGREEMENT = "acordo_mutuo"


// decorador: @dataclass
classe Relationship:
    // Um relacionamento declarado publicamente.
    rel_id: texto
    person_a: texto
    person_b: texto
    rel_type: RelationshipType
    seja status: RelationshipStatus = RelationshipStatus.ACTIVE
    seja declared_date: texto = ""
    seja ended_date: texto = ""
    seja public: logico = verdadeiro // TODOS sao publicos (regra)
    seja children: inteiro = 0
    seja notes: texto = ""  // optional (P2 -- sem detalhar intimidade)

    // Anti-inveja
    seja public_recognition: texto = "relacao_normal"  // nao e "melhor" nem "pior"


// ============================================================================
// 2. ANTI-INVEJA
// ============================================================================

classe EnvyType herda de Enum:
    RELATIONAL = "relacional"  // inveja de quem tem relacionamento
    MATERIAL = "material"  // inveja de bens (nao existe -- CC0)
    STATUS = "status"  // inveja de reconhecimento
    PHYSICAL = "fisica"  // inveja de aparencia (anti--combate)


// decorador: @dataclass
classe EnvyCase:
    // Caso de inveja identificado para tratamento.
    case_id: texto
    person: texto
    envy_type: EnvyType
    target: texto // de quem tem inveja
    seja description: texto = ""
    seja treatment: texto = ""
    seja resolved: logico = falso


// ============================================================================
// 3. VOTACAO DA ASSEMBLEIA
// ============================================================================

funcao run_relationship_assembly(n_voters: inteiro = 10000) -> {texto: qualquer}:
    // Assembleia constituinte sobre transparencia relacional.

    PERGUNTA:
      "Todo relacionamento deve ser publico para evitar invasao de espaco?"

    OPCOES:
      A) SIM -- todo relacionamento publico (declarar no OpenSocialNetwork)
      B) PARCIAL -- publico o fato, privado os detalhes
      C) nao -- cada um decide o que revelar
    // 
    votes_a = 0 // publico total
    votes_b = 0 // parcial (fato sim, detalhe nao)
    votes_c = 0 // privado

    para cada _ em intervalo(n_voters):
        r = random.random()
        se r < 0.45 entao:
            votes_a = votes_a + 1 // 45% -- publico
        senao se r < 0.85 entao:
            votes_b = votes_b + 1 // 40% -- parcial (P2 protege detalhe)
        senao:
            votes_c = votes_c + 1 // 15% -- privado

    // Combinando A + B (ambos querem declaracao publica do FATO)
    want_public_fact = votes_a + votes_b

    retorne {
        "question": (
            "Todo relacionamento deve ser publico para evitar "
            "invasao de espaco e combater inveja?"
        ),
        "votes_public_total": votes_a,
        "votes_partial_p2": votes_b,
        "votes_private": votes_c,
        "total": n_voters,
        "want_public_fact_pct": "{want_public_fact/n_voters*100:.0f}%",
        want_public_fact > n_voters * 0.5 ? "result": "APROVADO" : "REJEITADO",
        "decision": {
            "declarar_relacionamento": verdadeiro,         // SIM (85%)
            "detalhar_intimidade": falso,             // nao (P2 protege)
            "evitar_invasao": verdadeiro,                   // SIM
            "combater_inveja": verdadeiro,                  // SIM
            "poliafetivo_aceito": verdadeiro,               // SIM (P2)
            "relacionamento_secreto": falso,          // PROIBIDO
            "tricao_conceito": falso,                 // nao EXISTE (tudo publico)
            "ciume_possessivo": falso,                // PROIBIDO (P2 corpo livre)
            "pessoa_e_possuida": falso,               // NINGUEM e DONO (P2)
        },
    }


// ============================================================================
// 4. MOTOR DE RELACIONAMENTOS
// ============================================================================

classe RelationshipEngine:
    // Motor de relacionamentos transparentes da Republica.

    PRINCIPIOS:
    1. PUBLICO: declarar relacionamento evita invasao de espaco
    2. P2: detalhes da intimidade sao PRIVADOS (ninguem obrigado)
    3. ANTI-INVEJA: ter relacionamento nao e status. Nao ter nao e falha.
    4. ANTI-POSSESSAO: ninguem e dono de ninguem. Corpo e livre (P2).
    5. ANTI-TRAICAO: se tudo e publico, nao ha o que esconder
    6. POLIAFETIVO: aceito (P2 autonomia corporal total)
    7. CO-PARENTALIDADE: criar filhos sem obrigacao romantica
    // 

    funcao __init__(self):
        self.relationships: {texto: Relationship} = {}
        self.envy_cases: {texto: EnvyCase} = {}
        self.stats_declared: inteiro = 0
        self.stats_ended: inteiro = 0
        self.stats_envy_resolved: inteiro = 0

    funcao declare_relationship(self, person_a: texto, person_b: texto,
                             rel_type: RelationshipType,
                             seja notes: texto = "") -> {texto: qualquer}:
        // Declara relacionamento publicamente.
        rel_id = hashlib.md5(
            "{person_a}{person_b}{datetime.now()}".encode()
        ).hexdigest()[:8]

        rel = Relationship(
            rel_id = rel_id, person_a=person_a, person_b=person_b,
            rel_type = rel_type,
            declared_date <- datetime.now().isoformat(),
            notes = notes,
        )
        self.relationships[rel_id] = rel
        self.stats_declared += 1

        retorne {
            "declared": verdadeiro,
            "rel_id": rel_id,
            "relationship": "{person_a} + {person_b}",
            "type": rel_type.value,
            "status": "PUBLICO",
            "intimacy_detail": "PRIVADO (P2 -- nao obrigado)",
            "message": (
                "Relacionamento declarado: {person_a} + {person_b} ({rel_type.value}). "
                "PUBLICO no OpenSocialNetwork. "
                "Comunidade sabe. Ninguem invade espaco. "
                "Sem inveja -- e vida normal."
            ),
        }

    funcao end_relationship(self, rel_id: texto,
                         seja mutual: logico = verdadeiro) -> {texto: qualquer}:
        // Encerra relacionamento publicamente.
        rel = self.relationships.get(rel_id)
        se nao rel entao:
            retorne {"error": "Relacionamento nao encontrado"}

        rel.status = RelationshipStatus.ENDED
        rel.ended_date = datetime.now().isoformat()
        self.stats_ended += 1

        retorne {
            "ended": verdadeiro,
            "relationship": "{rel.person_a} + {rel.person_b}",
            "mutual": mutual,
            "public_announcement": (
                "Relacionamento encerrado: {rel.person_a} + {rel.person_b}. "
                "Mutuo acordo. Ambos livres. "
                "Comunidade sabe. Ninguem invade."
            ),
            "message": (
                "Encerrado. Ambos voltam a estar disponiveis. "
                "Sem drama. Sem ciume. Sem possessao. P2 corpo livre."
            ),
        }

    funcao check_status(self, person: texto) -> {texto: qualquer}:
        // Verifica status relacional de uma pessoa (publico).
        active = []
        ended = []
        para cada rel em self.relationships.values():
            se person in (rel.person_a, rel.person_b) entao:
                partner = person == rel.person_a ? rel.person_b : rel.person_a
                se rel.status == RelationshipStatus.ACTIVE entao:
                    active.append({
                        "partner": partner,
                        "type": rel.rel_type.value,
                        "since": rel.declared_date[:10],
                    })
                senao:
                    ended.append({"partner": partner})

        retorne {
            "person": person,
            "current_relationships": active,
            "past_relationships": tamanho(ended),
            "available": tamanho(active) == 0,
            "message": (
                "{person}: {len(active)} relacionamento(s) ativo(s). "
                "{'DISPONIVEL' if not active else 'EM RELACIONAMENTO'}. "
                "Antes de se aproximar: VERIFIQUE. Nao invada."
            ),
        }

    funcao report_envy(self, person: texto, target: texto,
                    seja envy_type: EnvyType = EnvyType.RELATIONAL,
                    seja description: texto = "") -> {texto: qualquer}:
        // Trata caso de inveja relacional/material.

        ANTI-INVEJA:
        Na Republica, inveja e tratada como sinal de que a pessoa
        precisa de RECONHECIMENTO (OpenCreator) ou de AUTONOMIA (P2).

        Ninguem inveja quem tem relacionamento se voce e SUFICIENTE.
        A Republica garante que cada cidadao e suficiente.
        // 
        case_id = hashlib.md5(
            "{person}{target}{datetime.now()}".encode()
        ).hexdigest()[:8]

        treatments = {
            EnvyType.RELATIONAL: (
                "Tratamento: OpenPsychology (sem rotular). "
                "Construcao de auto-estima. "
                "Republica garante: relacionamento nao e status. "
                "Voce e SUFICIENTE sozinho."
            ),
            EnvyType.MATERIAL: (
                "Tratamento: Nao ha bens materiais para invejar (CC0). "
                "Tudo e bem comum. Inveja material e ILOGICA na Republica."
            ),
            EnvyType.STATUS: (
                "Tratamento: OpenCreator reconhecimento. "
                "Todo mundo e reconhecido pelo impacto. "
                "Voce tem impacto proprio. Compare consigo mesmo."
            ),
            EnvyType.PHYSICAL: (
                "Tratamento: OpenBeauty disponivel para todos (ZERO custo). "
                "Aparencia e ajustavel. Valor e interno."
            ),
        }

        case = EnvyCase(
            case_id = case_id, person=person, target=target,
            envy_type = envy_type, description=description,
            treatment = treatments.get(envy_type, ""),
        )
        self.envy_cases[case_id] = case
        self.stats_envy_resolved += 1

        retorne {
            "case_id": case_id,
            "person": person,
            "target": target,
            "envy_type": envy_type.value,
            "treatment": case.treatment,
            "message": (
                "Inveja identificada: {person} -> {target}. "
                "Nao e culpa. E sinal. {case.treatment}"
            ),
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_relationships": tamanho(self.relationships),
            "active": soma(1 para r em self.relationships.values()
                          if r.status == RelationshipStatus.ACTIVE),
            "ended": self.stats_ended,
            "envy_cases_treated": self.stats_envy_resolved,
            "secret_relationships": 0,   // nao EXISTEM
            "tracoes_registered": 0,      // nao EXISTE (tudo publico)
        }


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = RelationshipEngine()

    imprima("=" * 80)
    imprima("  OPENRELATIONSHIPS -- TRANSPARENCIA RELACIONAL + ANTI-INVEJA")
    imprima("  Assembleia Constituinte sobre relacionamentos publicos")
    imprima("=" * 80)

    // === 1. PERGUNTA A ASSEMBLEIA ===
    imprima("\n\n  === 1. PERGUNTA A ASSEMBLEIA ===\n")
    imprima('  "Todo relacionamento deve ser publico para evitar')
    imprima('   invasao de espaco e combater inveja?"')

    // === 2. VOTACAO ===
    imprima("\n\n  === 2. VOTACAO (10.000 cidadaos) ===\n")
    result = run_relationship_assembly(10000)
    imprima("  PUBLICO TOTAL (fato + detalhe): {result['votes_public_total']:>6} "
          "({result['votes_public_total']/100:.0f}%)")
    imprima("  PARCIAL (fato sim, detalhe nao): {result['votes_partial_p2']:>6} "
          "({result['votes_partial_p2']/100:.0f}%)")
    imprima("  PRIVADO (cada um decide):       {result['votes_private']:>6} "
          "({result['votes_private']/100:.0f}%)")
    imprima("\n  Querem fato publico (A+B): {result['want_public_fact_pct']}")
    imprima("  RESULTADO: {result['result']}")

    // === 3. DECISAO DA ASSEMBLEIA ===
    imprima("\n\n  === 3. DECISAO DA ASSEMBLEIA ===\n")
    d = result["decision"]
    para cada (key, val) em d.items():
        status = val ? "SIM" : "NAO"
        imprima("  {key:<30} {status}")

    // === 4. DECLARAR RELACIONAMENTOS ===
    imprima("\n\n  === 4. RELACIONAMENTOS DECLARADOS ===\n")
    rels = [
        ("Cleiton", "Maria", RelationshipType.PARTNER),
        ("Joao", "Ana", RelationshipType.MARRIAGE),
        ("Pedro", "Beatriz", RelationshipType.DATING),
        ("Lucas", "Sofia", RelationshipType.POLY),
        ("Tobias", "Dona Rita", RelationshipType.COMPANIONSHIP),
    ]
    para a, b, rtype in rels:
        result_decl = engine.declare_relationship(a, b, rtype)
        imprima("  {a:<12} + {b:<12} -> {rtype.value:<15} "
              "[{result_decl['status']}]")

    // === 5. VERIFICAR STATUS ===
    imprima("\n\n  === 5. VERIFICACAO DE STATUS (anti-invasao) ===\n")
    para cada person em ["Cleiton", "Carlos", "Joao", "Ana"]:
        status = engine.check_status(person)
        avail = status["available"] ? "DISPONIVEL" : "EM RELACIONAMENTO"
        imprima("  {person:<12} -> {avail}", end="")
        se status["current_relationships"] entao:
            para cada rel em status["current_relationships"]:
                imprima(" ({rel['partner']}, {rel['type']})", end="")
        imprima()

    // === 6. ENCERRAR RELACIONAMENTO ===
    imprima("\n\n  === 6. ENCERRAMENTO PUBLICO ===\n")
    rels_list = list(engine.relationships.keys())
    se rels_list entao:
        end_result = engine.end_relationship(rels_list[2], mutual=verdadeiro)
        imprima("  {end_result['public_announcement']}")
        imprima("  {end_result['message']}")

    // === 7. ANTI-INVEJA ===
    imprima("\n\n  === 7. ANTI-INVEJA ===\n")
    envies = [
        ("Carlos", "Cleiton", EnvyType.RELATIONAL,
         "Carlos tem inveja de Cleiton ter relacionamento"),
        ("Jose", "Pedro", EnvyType.STATUS,
         "Jose acha que Pedro e mais reconhecido"),
        ("Marcos", "Joao", EnvyType.PHYSICAL,
         "Marcos acha Joao mais bonito"),
    ]
    para person, target, etype, desc in envies:
        result_envy = engine.report_envy(person, target, etype, desc)
        imprima("\n  {result_envy['person']} -> {result_envy['target']} "
              "({result_envy['envy_type']})")
        imprima("  {result_envy['treatment'][:80]}")

    // === 8. STATS ===
    imprima("\n\n  === 8. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA DO OPENRELATIONSHIPS")
    imprima("{'='*80}")
    imprima("""
  ASSEMBLEIA DECIDIU (85% a favor do fato publico):

  1. RELACIONAMENTOS SAO PUBLICOS
     Todo relacionamento e declarado no OpenSocialNetwork.
     Motivo: evitar invasao de espaco alheio.
     Se Maria sabe que Joao esta com Ana, Maria nao se aproxima.
     Transparencia = respeito.

  2. MAS INTIMIDADE e PRIVADA (P2)
     "Estou com Maria" = PUBLICO (fato).
     "O que faco com Maria" = PRIVADO (detalhe).
     P2 autonomia corporal protege os DETALHES.
     Ninguem e obrigado a detalhar a relacao.

  3. O QUE ISSO ELIMINA:
     - TRAICAO: se tudo e publico, nao ha o que esconder.
       "Traicao" deixa de existir como conceito.
     - CIUME POSSESSIVO: ninguem e dono de ninguem (P2).
       Se a pessoa escolhe outro, e DIREITO DELA.
     - "TOMAR" PESSOA: nao se toma o que nao e possuido.
       Pessoas nao sao objetos.
     - INVASAO DE ESPACO: todo mundo sabe quem esta com quem.
       Ninguem "mete o nariz" por engano.

  4. ANTI-INVEJA (politica complementar):
     Inveja e SINAL de que a pessoa precisa:
     - Auto-estima (OpenPsychology sem rotular)
     - Reconhecimento (OpenCreator -- todo mundo tem impacto)
     - Autonomia (P2 -- voce e suficiente)
     - Aparencia (OpenBeauty ZERO custo)

     Na Republica:
     - Relacionamento nao e status (nao e "melhor" ter)
     - Solteiro nao e falha (nao e "pior" nao ter)
     - Bens materiais nao existem para invejar (CC0)
     - Status vem do IMPACTO (todo mundo tem)

  5. POLIAFETIVO ACEITO (P2):
     Relacionamento com mais de uma pessoa e ACEITO.
     Desde que TODOS sabem e CONSENTEM.
     Transparencia = ninguem e enganado.
     P2: corpo de cada um. Escolha de cada um.

  6. O QUE nao EXISTE:
     - Relacionamento secreto (PROIBIDO -- gera invasao)
     - Traicao (tudo publico, nada a esconder)
     - Ciume possessivo (P2 corpo livre)
     - Posse de pessoa (ninguem e dono)
     - Inveja de relacionamento (tratada)
     - Inveja material (ilologica -- CC0)

  PRINCIPIOS:
    P1: Relacionamento nao e status. Solteiro nao e inferior.
    P2: Corpo e de cada um. Escolha e de cada um. Detalhe e privado.
    P3: Relacionamento nao conta como trabalho (nao e contribuicao).
    P4: Assembleia votou. 85% a favor. Regra aplicada.
// )
    imprima("{'='*80}")
    imprima("  OpenRelationships: {s['total_relationships']} declarados, "
          "{s['active']} ativos, "
          "{s['envy_cases_treated']} casos de inveja tratados.")
    imprima("  Publico no fato. Privado na intimidade. Sem inveja.")
    imprima("{'='*80}")

```
