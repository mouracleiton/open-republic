#!/usr/bin/env python3
"""
OpenRelationships -- Politica de Transparencia Relacional + Anti-Inveja -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenRelationships -- Politica de Transparencia Relacional + Anti-Inveja
=========================================================================
PERGUNTA SUBMETIDA A ASSEMBLEIA:
"Todo relacionamento tem que ser publico? As pessoas precisam saber
para nao cometer o problema de invasao de espaco. Nada de esconder."
O QUE A ASSEMBLEIA DECIDIU:
APROVADO COM NUANCES:
1. RELACIONAMENTOS DECLARADOS (sim, publicos)
    - Todo relacionamento and registrado no OpenSocialNetwork
    - Motivo: evitar invasao de espaco alheio
    - Motivo: transparencia gera confianca
    - Motivo: anti-inveja (saber que alguem esta com alguem elimina disputa)
2. MAS P2 AUTONOMIA (not obrigacao de detalhe)
    - VOCE declara que esta com quem (fato, not detalhe)
    - Ninguem and obrigado a detalhar a RELACAO (intimidade)
    - "Estou com Maria" = sim. "O que faco com Maria" = not
3. ANTI-INVEJA (politica complementar)
    - Inveja and reconhecida como doenca social
    - Republica not competi por pessoas
    - Todo cidadao and suficiente (OpenCreator + OpenCredit)
    - Quem tem relacionamento not and "melhor"
    - Quem not tem not and "pior"
4. O QUE not EXISTE:
    - Traicao (se tudo and publico, not ha o que esconder)
    - Ciume possessivo (cada corpo and livre -- P2)
    - "Tomar" pessoa de outro (ninguem and dono de ninguem)
    - Relacionamento secreto (publico = regra)
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa random
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict, Counter de collections
# importa datetime de datetime
# ============================================================================
# 1. TIPOS DE RELACIONAMENTO
# ============================================================================
class RelationshipType(Enum):
    PARTNER = "namoro"  // namoro
    MARRIAGE = "uniao"  // uniao estavel / casamento
    DATING = "encontro"  // ficante / encontro casual
    COMPANIONSHIP = "companhia"  // companhia (not sexual)
    CO_PARENTING = "coparentalidade"  // criar filhos juntos
    POLY = "poliafectivo"  // relacionamento multilo
    FRIENDSHIP_INTIMATE = "amizade_intima"  // melhor amigo(a)
    MENTORSHIP = "mentoria"  // mentor/aprendiz
class RelationshipStatus(Enum):
    ACTIVE = "ativo"
    PAUSED = "pausado"
    ENDED = "encerrado"
    MUTUAL_AGREEMENT = "acordo_mutuo"
# decorador: @dataclass
class Relationship:
    # Um relacionamento declarado publicamente.
    rel_id: texto
    person_a: texto
    person_b: texto
    rel_type: RelationshipType
    status: RelationshipStatus = RelationshipStatus.ACTIVE
    declared_date: str = ""
    ended_date: str = ""
    public: bool = True // TODOS sao publicos (regra)
    children: int = 0
    notes: str = ""  // optional (P2 -- sem detalhar intimidade)
    # Anti-inveja
    public_recognition: str = "relacao_normal"  // not and "melhor" nem "pior"
# ============================================================================
# 2. ANTI-INVEJA
# ============================================================================
class EnvyType(Enum):
    RELATIONAL = "relacional"  // inveja de quem tem relacionamento
    MATERIAL = "material"  // inveja de bens (not existe -- CC0)
    STATUS = "status"  // inveja de reconhecimento
    PHYSICAL = "fisica"  // inveja de aparencia (anti--combate)
# decorador: @dataclass
class EnvyCase:
    # Caso de inveja identificado para tratamento.
    case_id: texto
    person: texto
    envy_type: EnvyType
    target: texto // de quem tem inveja
    description: str = ""
    treatment: str = ""
    resolved: bool = False
# ============================================================================
# 3. VOTACAO DA ASSEMBLEIA
# ============================================================================
def run_relationship_assembly(n_voters: inteiro = 10000) -> {texto: qualquer}:
    # Assembleia constituinte sobre transparencia relacional.
    PERGUNTA:
    "Todo relacionamento deve ser publico para evitar invasao de espaco?"
    OPCOES:
    A) SIM -- todo relacionamento publico (declarar no OpenSocialNetwork)
    B) PARCIAL -- publico o fato, privado os detalhes
    C) not -- cada um decide o que revelar
    # 
    votes_a = 0 // publico total
    votes_b = 0 // parcial (fato sim, detalhe not)
    votes_c = 0 // privado
    for _ in intervalo(n_voters):
        r = random.random()
        if r < 0.45:
            votes_a = votes_a + 1 // 45% -- publico
        elif r < 0.85:
            votes_b = votes_b + 1 // 40% -- parcial (P2 protege detalhe)
        else:
            votes_c = votes_c + 1 // 15% -- privado
    # Combinando A + B (ambos querem declaracao publica do FATO)
    want_public_fact = votes_a + votes_b
    return {
        "question": (
            "Todo relacionamento deve ser publico para evitar "
            "invasao de espaco and combater inveja?"
        ),
        "votes_public_total": votes_a,
        "votes_partial_p2": votes_b,
        "votes_private": votes_c,
        "total": n_voters,
        "want_public_fact_pct": "{want_public_fact/n_voters*100:.0f}%",
        want_public_fact > n_voters * 0.5 ? "result": "APROVADO" : "REJEITADO",
        "decision": {
            "declarar_relacionamento": True,         // SIM (85%)
            "detalhar_intimidade": False,             // not (P2 protege)
            "evitar_invasao": True,                   // SIM
            "combater_inveja": True,                  // SIM
            "poliafetivo_aceito": True,               // SIM (P2)
            "relacionamento_secreto": False,          // PROIBIDO
            "tricao_conceito": False,                 // not EXISTE (tudo publico)
            "ciume_possessivo": False,                // PROIBIDO (P2 corpo livre)
            "pessoa_e_possuida": False,               // NINGUEM and DONO (P2)
        },
    }
# ============================================================================
# 4. MOTOR DE RELACIONAMENTOS
# ============================================================================
class RelationshipEngine:
    # Motor de relacionamentos transparentes da Republica.
    PRINCIPIOS:
    1. PUBLICO: declarar relacionamento evita invasao de espaco
    2. P2: detalhes da intimidade sao PRIVADOS (ninguem obrigado)
    3. ANTI-INVEJA: ter relacionamento not and status. Nao ter not and falha.
    4. ANTI-POSSESSAO: ninguem and dono de ninguem. Corpo and livre (P2).
    5. ANTI-TRAICAO: se tudo and publico, not ha o que esconder
    6. POLIAFETIVO: aceito (P2 autonomia corporal total)
    7. CO-PARENTALIDADE: criar filhos sem obrigacao romantica
    # 
    def __init__(self):
        self.relationships: {texto: Relationship} = {}
        self.envy_cases: {texto: EnvyCase} = {}
        self.stats_declared: inteiro = 0
        self.stats_ended: inteiro = 0
        self.stats_envy_resolved: inteiro = 0
    funcao declare_relationship(self, person_a: texto, person_b: texto,
                            rel_type: RelationshipType,
                            notes: str = "") -> {texto: qualquer}:
        # Declara relacionamento publicamente.
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
        return {
            "declared": True,
            "rel_id": rel_id,
            "relationship": "{person_a} + {person_b}",
            "type": rel_type.value,
            "status": "PUBLICO",
            "intimacy_detail": "PRIVADO (P2 -- not obrigado)",
            "message": (
                "Relacionamento declarado: {person_a} + {person_b} ({rel_type.value}). "
                "PUBLICO no OpenSocialNetwork. "
                "Comunidade sabe. Ninguem invade espaco. "
                "Sem inveja -- and vida normal."
            ),
        }
    funcao end_relationship(self, rel_id: texto,
                        mutual: bool = True) -> {texto: qualquer}:
        # Encerra relacionamento publicamente.
        rel = self.relationships.get(rel_id)
        if not rel:
            return {"error": "Relacionamento not encontrado"}
        rel.status = RelationshipStatus.ENDED
        rel.ended_date = datetime.now().isoformat()
        self.stats_ended += 1
        return {
            "ended": True,
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
    def check_status(self, person: texto) -> {texto: qualquer}:
        # Verifica status relacional de uma pessoa (publico).
        active = []
        ended = []
        for rel in self.relationships.values():
            if person in (rel.person_a, rel.person_b):
                partner = person == rel.person_a ? rel.person_b : rel.person_a
                if rel.status == RelationshipStatus.ACTIVE:
                    active.append({
                        "partner": partner,
                        "type": rel.rel_type.value,
                        "since": rel.declared_date[:10],
                    })
                else:
                    ended.append({"partner": partner})
        return {
            "person": person,
            "current_relationships": active,
            "past_relationships": len(ended),
            "available": len(active) == 0,
            "message": (
                "{person}: {len(active)} relacionamento(s) ativo(s). "
                "{'DISPONIVEL' if not active else 'EM RELACIONAMENTO'}. "
                "Antes de se aproximar: VERIFIQUE. Nao invada."
            ),
        }
    funcao report_envy(self, person: texto, target: texto,
                    envy_type: EnvyType = EnvyType.RELATIONAL,
                    description: str = "") -> {texto: qualquer}:
        # Trata caso de inveja relacional/material.
        ANTI-INVEJA:
        Na Republica, inveja and tratada como sinal de que a pessoa
        precisa de RECONHECIMENTO (OpenCreator) or de AUTONOMIA (P2).
        Ninguem inveja quem tem relacionamento se voce and SUFICIENTE.
        A Republica garante que cada cidadao and suficiente.
        # 
        case_id = hashlib.md5(
            "{person}{target}{datetime.now()}".encode()
        ).hexdigest()[:8]
        treatments = {
            EnvyType.RELATIONAL: (
                "Tratamento: OpenPsychology (sem rotular). "
                "Construcao de auto-estima. "
                "Republica garante: relacionamento not and status. "
                "Voce and SUFICIENTE sozinho."
            ),
            EnvyType.MATERIAL: (
                "Tratamento: Nao ha bens materiais para invejar (CC0). "
                "Tudo and bem comum. Inveja material and ILOGICA na Republica."
            ),
            EnvyType.STATUS: (
                "Tratamento: OpenCreator reconhecimento. "
                "Todo mundo and reconhecido pelo impacto. "
                "Voce tem impacto proprio. Compare consigo mesmo."
            ),
            EnvyType.PHYSICAL: (
                "Tratamento: OpenBeauty disponivel para todos (ZERO custo). "
                "Aparencia and ajustavel. Valor and interno."
            ),
        }
        case = EnvyCase(
            case_id = case_id, person=person, target=target,
            envy_type = envy_type, description=description,
            treatment = treatments.get(envy_type, ""),
        )
        self.envy_cases[case_id] = case
        self.stats_envy_resolved += 1
        return {
            "case_id": case_id,
            "person": person,
            "target": target,
            "envy_type": envy_type.value,
            "treatment": case.treatment,
            "message": (
                "Inveja identificada: {person} -> {target}. "
                "Nao and culpa. E sinal. {case.treatment}"
            ),
        }
    def stats(self) -> {texto: qualquer}:
        return {
            "total_relationships": len(self.relationships),
            "active": sum(1 para r em self.relationships.values()
                        if r.status == RelationshipStatus.ACTIVE),
            "ended": self.stats_ended,
            "envy_cases_treated": self.stats_envy_resolved,
            "secret_relationships": 0,   // not EXISTEM
            "tracoes_registered": 0,      // not EXISTE (tudo publico)
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = RelationshipEngine()
    print("=" * 80)
    print("  OPENRELATIONSHIPS -- TRANSPARENCIA RELACIONAL + ANTI-INVEJA")
    print("  Assembleia Constituinte sobre relacionamentos publicos")
    print("=" * 80)
    # === 1. PERGUNTA A ASSEMBLEIA ===
    print("\n\n  === 1. PERGUNTA A ASSEMBLEIA ===\n")
    print('  "Todo relacionamento deve ser publico para evitar')
    print('   invasao de espaco and combater inveja?"')
    # === 2. VOTACAO ===
    print("\n\n  === 2. VOTACAO (10.000 cidadaos) ===\n")
    result = run_relationship_assembly(10000)
    print("  PUBLICO TOTAL (fato + detalhe): {result['votes_public_total']:>6} "
        "({result['votes_public_total']/100:.0f}%)")
    print("  PARCIAL (fato sim, detalhe not): {result['votes_partial_p2']:>6} "
        "({result['votes_partial_p2']/100:.0f}%)")
    print("  PRIVADO (cada um decide):       {result['votes_private']:>6} "
        "({result['votes_private']/100:.0f}%)")
    print("\n  Querem fato publico (A+B): {result['want_public_fact_pct']}")
    print("  RESULTADO: {result['result']}")
    # === 3. DECISAO DA ASSEMBLEIA ===
    print("\n\n  === 3. DECISAO DA ASSEMBLEIA ===\n")
    d = result["decision"]
    for each (key, val) in d.items():
        status = val ? "SIM" : "NAO"
        print("  {key:<30} {status}")
    # === 4. DECLARAR RELACIONAMENTOS ===
    print("\n\n  === 4. RELACIONAMENTOS DECLARADOS ===\n")
    rels = [
        ("Cleiton", "Maria", RelationshipType.PARTNER),
        ("Joao", "Ana", RelationshipType.MARRIAGE),
        ("Pedro", "Beatriz", RelationshipType.DATING),
        ("Lucas", "Sofia", RelationshipType.POLY),
        ("Tobias", "Dona Rita", RelationshipType.COMPANIONSHIP),
    ]
    para a, b, rtype in rels:
        result_decl = engine.declare_relationship(a, b, rtype)
        print("  {a:<12} + {b:<12} -> {rtype.value:<15} "
            "[{result_decl['status']}]")
    # === 5. VERIFICAR STATUS ===
    print("\n\n  === 5. VERIFICACAO DE STATUS (anti-invasao) ===\n")
    for person in ["Cleiton", "Carlos", "Joao", "Ana"]:
        status = engine.check_status(person)
        avail = status["available"] ? "DISPONIVEL" : "EM RELACIONAMENTO"
        print("  {person:<12} -> {avail}", end="")
        if status["current_relationships"]:
            for rel in status["current_relationships"]:
                print(" ({rel['partner']}, {rel['type']})", end="")
        print()
    # === 6. ENCERRAR RELACIONAMENTO ===
    print("\n\n  === 6. ENCERRAMENTO PUBLICO ===\n")
    rels_list = list(engine.relationships.keys())
    if rels_list:
        end_result = engine.end_relationship(rels_list[2], mutual=True)
        print("  {end_result['public_announcement']}")
        print("  {end_result['message']}")
    # === 7. ANTI-INVEJA ===
    print("\n\n  === 7. ANTI-INVEJA ===\n")
    envies = [
        ("Carlos", "Cleiton", EnvyType.RELATIONAL,
        "Carlos tem inveja de Cleiton ter relacionamento"),
        ("Jose", "Pedro", EnvyType.STATUS,
        "Jose acha que Pedro and mais reconhecido"),
        ("Marcos", "Joao", EnvyType.PHYSICAL,
        "Marcos acha Joao mais bonito"),
    ]
    para person, target, etype, desc in envies:
        result_envy = engine.report_envy(person, target, etype, desc)
        print("\n  {result_envy['person']} -> {result_envy['target']} "
            "({result_envy['envy_type']})")
        print("  {result_envy['treatment'][:80]}")
    # === 8. STATS ===
    print("\n\n  === 8. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA DO OPENRELATIONSHIPS")
    print("{'='*80}")
    print("""
ASSEMBLEIA DECIDIU (85% a favor do fato publico):
1. RELACIONAMENTOS SAO PUBLICOS
    Todo relacionamento and declarado no OpenSocialNetwork.
    Motivo: evitar invasao de espaco alheio.
    Se Maria sabe que Joao esta com Ana, Maria not se aproxima.
    Transparencia = respeito.
2. MAS INTIMIDADE and PRIVADA (P2)
    "Estou com Maria" = PUBLICO (fato).
    "O que faco com Maria" = PRIVADO (detalhe).
    P2 autonomia corporal protege os DETALHES.
    Ninguem and obrigado a detalhar a relacao.
3. O QUE ISSO ELIMINA:
    - TRAICAO: se tudo and publico, not ha o que esconder.
    "Traicao" deixa de existir como conceito.
    - CIUME POSSESSIVO: ninguem and dono de ninguem (P2).
    Se a pessoa escolhe outro, and DIREITO DELA.
    - "TOMAR" PESSOA: not se toma o que not and possuido.
    Pessoas not sao objetos.
    - INVASAO DE ESPACO: todo mundo sabe quem esta com quem.
    Ninguem "mete o nariz" por engano.
4. ANTI-INVEJA (politica complementar):
    Inveja and SINAL de que a pessoa precisa:
    - Auto-estima (OpenPsychology sem rotular)
    - Reconhecimento (OpenCreator -- todo mundo tem impacto)
    - Autonomia (P2 -- voce and suficiente)
    - Aparencia (OpenBeauty ZERO custo)
    Na Republica:
    - Relacionamento not and status (not and "melhor" ter)
    - Solteiro not and falha (not and "pior" not ter)
    - Bens materiais not existem para invejar (CC0)
    - Status vem do IMPACTO (todo mundo tem)
5. POLIAFETIVO ACEITO (P2):
    Relacionamento com mais de uma pessoa and ACEITO.
    Desde que TODOS sabem and CONSENTEM.
    Transparencia = ninguem and enganado.
    P2: corpo de cada um. Escolha de cada um.
6. O QUE not EXISTE:
    - Relacionamento secreto (PROIBIDO -- gera invasao)
    - Traicao (tudo publico, nada a esconder)
    - Ciume possessivo (P2 corpo livre)
    - Posse de pessoa (ninguem and dono)
    - Inveja de relacionamento (tratada)
    - Inveja material (ilologica -- CC0)
PRINCIPIOS:
    P1: Relacionamento not and status. Solteiro not and inferior.
    P2: Corpo and de cada um. Escolha and de cada um. Detalhe and privado.
    P3: Relacionamento not conta como trabalho (not and contribuicao).
    P4: Assembleia votou. 85% a favor. Regra aplicada.
# )
    print("{'='*80}")
    print("  OpenRelationships: {s['total_relationships']} declarados, "
        "{s['active']} ativos, "
        "{s['envy_cases_treated']} casos de inveja tratados.")
    print("  Publico no fato. Privado na intimidade. Sem inveja.")
    print("{'='*80}")
