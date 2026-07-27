#!/usr/bin/env python3
"""
OpenWeaponsPolicy -- Politica de Porte de Armas da Republica -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenWeaponsPolicy -- Politica de Porte de Armas da Republica
===============================================================
"A Republica PREFERE paz. Mas P2 diz: corpo and seu.
Voce tem direito de se defender.
OpenMartialArts primeiro. Sempre.
Arma de fogo? ULTIMO recurso. Condicoes EXTREMAS.
Armas de guerra? not existem nas maos de cidadaos.
Assembleia decide."
ASSEMBLEIA CONSTITUINTE CONVOCADA:
"Qual a politica de porte de armas na Republica?"
O QUE ESTE SISTEMA FAZ:
1. Define 5 categorias de itens (proibido, restrito, ferramenta,(defesa, livre)
2. Estabelece condicoes EXTREMAS para porte de arma de fogo
3. Prioriza OpenMartialArts sobre arma
4. Proibe armas de guerra para cidadaos
5. Regula ferramentas que podem ser armas (faca, machado)
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa random
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional de typing
# importa Enum de enum
# importa Counter, defaultdict de collections
# importa datetime de datetime
# ============================================================================
# 1. CATEGORIAS DE ITENS
# ============================================================================
class ItemCategory(Enum):
    # Categoria de item baseado em potencial de dano.
    PROHIBITED = ("proibido", 0)  // arma de guerra, bomba
    RESTRICTED_FIREARM = ("arma_fogo_restrita", 1)  // pistola, revolver
    TOOL_WEAPON = ("ferramenta_arma", 2)  // faca, machado, foice
    DEFENSE_ONLY = ("defesa_apenas", 3)  // spray pimenta, taser
    FREE = ("livre", 4)  // sem restricao
class WeaponPermit(Enum):
    # Niveis de permisso de porte.
    NONE = ("nenhum", 0)  // sem porte
    SELF_DEFENSE = ("autodefesa", 1)  // spray, taser
    TOOL = ("ferramenta", 2)  // faca de trabalho
    FIREARM_RESTRICTED = ("arma_fogo", 3)  // arma de fogo (extremo)
    SECURITY = ("seguranca", 4)  // patrulha comunitaria
class PermitRequirement(Enum):
    # Requisitos para conseguir porte.
    OPEN_MARTIAL_ARTS = "cinto_verde_martial_arts"
    PSYCH_EVAL = "avaliacao_psicologica"
    NO_CRIMINAL_RECORD = "sem_prontuario_violento"
    ASSEMBLY_APPROVAL = "aprovacao_assembleia"
    ANNUAL_RENEWAL = "renovacao_anual"
    SAFE_STORAGE = "guarda_segura"
    PROFICIENCY_TEST = "teste_proficiencia"
    COMMUNITY_ENDORSEMENT = "endorsement_comunitario"
# ============================================================================
# 2. ITENS CATALOGADOS
# ============================================================================
# decorador: @dataclass
class WeaponItem:
    # Um item classificado por potencial de dano.
    item_id: texto
    name: texto
    category: ItemCategory
    description: str = ""
    legitimate_use: str = ""  // uso legitimo (trabalho, defesa)
    permit_needed: WeaponPermit = WeaponPermit.NONE
    requirements: [PermitRequirement] = field(default_factory=list)
    # Restricoes
    max_per_person: int = 0 // 0 = proibido, 1 = uma unidade
    open_carry: bool = False // pode portar visivel?
    concealed_carry: bool = False // pode portar escondido?
    home_only: bool = False // so em casa?
WEAPONS_CATALOG: [WeaponItem] = [
    # === PROIBIDOS (categoria 0) ===
    WeaponItem("WPN-WAR1", "Fuzil de Assalto", ItemCategory.PROHIBITED,
            "Arma de guerra. NENHUM cidadao precisa. So militar em ativo.",
            permit_needed = WeaponPermit.NONE, max_per_person=0),
    WeaponItem("WPN-WAR2", "Metralhadora", ItemCategory.PROHIBITED,
            "Arma de guerra. PROIBIDA para cidadaos.",
            permit_needed = WeaponPermit.NONE, max_per_person=0),
    WeaponItem("WPN-WAR3", "Bomba/Explosivo", ItemCategory.PROHIBITED,
            "Explosivo. PROIBIDO. So FabLab controlado.",
            permit_needed = WeaponPermit.NONE, max_per_person=0),
    WeaponItem("WPN-WAR4", "Lanca-foguete", ItemCategory.PROHIBITED,
            "Arma de guerra. PROIBIDO.",
            permit_needed = WeaponPermit.NONE, max_per_person=0),
    WeaponItem("WPN-WAR5", "Arma Quimica/Biologica", ItemCategory.PROHIBITED,
            "PROIBIDO. Crime contra humanidade.",
            permit_needed = WeaponPermit.NONE, max_per_person=0),
    # === ARMA DE FOGO RESTRITA (categoria 1) ===
    WeaponItem("WPN-GUN1", "Pistola (calibre limitado)", ItemCategory.RESTRICTED_FIREARM,
            "Pistola. ULTIMO recurso de autodefesa. Condicoes extremas.",
            legitimate_use = "Autodefesa domiciliar (extremo)",
            permit_needed = WeaponPermit.FIREARM_RESTRICTED,
            max_per_person = 1, home_only=True,
            requirements = [
                PermitRequirement.OPEN_MARTIAL_ARTS,
                PermitRequirement.PSYCH_EVAL,
                PermitRequirement.NO_CRIMINAL_RECORD,
                PermitRequirement.ASSEMBLY_APPROVAL,
                PermitRequirement.ANNUAL_RENEWAL,
                PermitRequirement.SAFE_STORAGE,
                PermitRequirement.PROFICIENCY_TEST,
                PermitRequirement.COMMUNITY_ENDORSEMENT,
            ]),
    WeaponItem("WPN-GUN2", "Revolver (calibre limitado)", ItemCategory.RESTRICTED_FIREARM,
            "Revolver. Mesmas restricoes que pistola.",
            legitimate_use = "Autodefesa domiciliar (extremo)",
            permit_needed = WeaponPermit.FIREARM_RESTRICTED,
            max_per_person = 1, home_only=True,
            requirements = [
                PermitRequirement.OPEN_MARTIAL_ARTS,
                PermitRequirement.PSYCH_EVAL,
                PermitRequirement.NO_CRIMINAL_RECORD,
                PermitRequirement.ASSEMBLY_APPROVAL,
                PermitRequirement.ANNUAL_RENEWAL,
                PermitRequirement.SAFE_STORAGE,
                PermitRequirement.PROFICIENCY_TEST,
                PermitRequirement.COMMUNITY_ENDORSEMENT,
            ]),
    # === FERRAMENTA QUE PODE SER ARMA (categoria 2) ===
    WeaponItem("WPN-TOOL1", "Faca de Cozinha", ItemCategory.TOOL_WEAPON,
            "Ferramenta de cozinha. Uso legitimo: cozinhar.",
            legitimate_use = "Cozinha",
            permit_needed = WeaponPermit.NONE, max_per_person=99,
            home_only = True),
    WeaponItem("WPN-TOOL2", "Faca de Trabalho (agricola/caca)", ItemCategory.TOOL_WEAPON,
            "Faca de trabalho. Uso legitimo: agricultura, FabLab.",
            legitimate_use = "Trabalho agricola/industrial",
            permit_needed = WeaponPermit.TOOL, max_per_person=2),
    WeaponItem("WPN-TOOL3", "Machado", ItemCategory.TOOL_WEAPON,
            "Ferramenta. Uso legitimo: lenha, construcao.",
            legitimate_use = "Lenha, construcao, FabLab",
            permit_needed = WeaponPermit.TOOL, max_per_person=1),
    WeaponItem("WPN-TOOL4", "Foice/Enxada", ItemCategory.TOOL_WEAPON,
            "Ferramenta agricola. Uso legitimo: agricultura.",
            legitimate_use = "Agricultura (OpenAgrarian)",
            permit_needed = WeaponPermit.NONE, max_per_person=2),
    # === DEFESA APENAS (categoria 3) ===
    WeaponItem("WPN-DEF1", "Spray de Pimenta", ItemCategory.DEFENSE_ONLY,
            "Defesa not-letal. Cega temporariamente. Permite fugir.",
            legitimate_use = "Autodefesa (not letal)",
            permit_needed = WeaponPermit.SELF_DEFENSE, max_per_person=1,
            concealed_carry = True,
            requirements = [
                PermitRequirement.PSYCH_EVAL,
            ]),
    WeaponItem("WPN-DEF2", "Taser (choque)", ItemCategory.DEFENSE_ONLY,
            "Defesa not-letal. Incapacita temporariamente.",
            legitimate_use = "Autodefesa (not letal)",
            permit_needed = WeaponPermit.SELF_DEFENSE, max_per_person=1,
            concealed_carry = True,
            requirements = [
                PermitRequirement.PSYCH_EVAL,
                PermitRequirement.PROFICIENCY_TEST,
            ]),
    # === LIVRE (categoria 4) ===
    WeaponItem("WPN-FREE1", "Bastao de Madeira", ItemCategory.FREE,
            "Bastao. Ferramenta de treino OpenMartialArts.",
            legitimate_use = "Treino Kali/Escrima",
            permit_needed = WeaponPermit.NONE, max_per_person=5),
    WeaponItem("WPN-FREE2", "Apito de Emergencia", ItemCategory.FREE,
            "Apito. Alerta comunitario.",
            legitimate_use = "Sinalizar emergencia",
            permit_needed = WeaponPermit.NONE, max_per_person=3),
]
# ============================================================================
# 3. VOTACAO DA ASSEMBLEIA
# ============================================================================
def run_weapons_assembly(n_voters: inteiro = 10000) -> {texto: qualquer}:
    # Assembleia vota politica de armas.
    votes = {
        "proibir_todo_porte": 0,            // zero armas para cidadaos
        "permitir_apenas_defesa": 0,         // so spray/taser
        "permitir_restrito_extremo": 0,      // arma de fogo com condicoes
        "permitir_livre": 0,                 // armamento livre (EUA-style)
    }
    for _ in intervalo(n_voters):
        r = random.random()
        if r < 0.35:
            votes["proibir_todo_porte"] += 1
        elif r < 0.50:
            votes["permitir_livre"] += 1
        elif r < 0.80:
            votes["permitir_apenas_defesa"] += 1
        else:
            votes["permitir_restrito_extremo"] += 1
    # Maioria
    winner = max(votes, key=votes.get)
    return {
        "question": (
            "Qual a politica de porte de armas na Republica?"
        ),
        "votes": votes,
        "total": n_voters,
        "winner": winner,
        "pct": "{votes[winner]/n_voters*100:.0f}%",
        "decisions": {
            "armas_de_guerra": "PROIBIDAS para cidadaos (unanime)",
            "armas_de_fogo": (
                "RESTRITAS. Condicoes extremas: "
                "OpenMartialArts cinto verde + psicologica + "
                "sem prontuario violento + assembleia aprova + "
                "renovacao anual + guarda segura + proficiencia + "
                "endorsement comunitario. SO domicilio."
            ),
            "armas_nao_letais": "PERMITIDAS (spray, taser) com psicologica",
            "ferramentas": "PERMITIDAS para trabalho (not para porte como arma)",
            "open_martial_arts": "PRIORIDADE. Todo cidadao treina. Arma and ultimo recurso.",
            "porte_visivel": "PROIBIDO (exceto seguraca em patrulha)",
            "porte_escondido": "SO spray/taser (not letal)",
            "comercio_armas": "PROIBIDO (OpenProhibitedBusiness). FabLab fabrica.",
            "calibre_maximo": "Limitado pela assembleia",
            "renovacao": "ANUAL. Pode perder a qualquer momento.",
        },
    }
# ============================================================================
# 4. MOTOR DE ARMAS
# ============================================================================
class WeaponsEngine:
    # Motor que gere politica de armas da Republica.
    FILOSOFIA:
    1. OpenMartialArts PRIMEIRO. Sempre.
    Cidadao que sabe se defender SEM arma not precisa de arma.
    Todo cidadao treina OpenMartialArts (cinto azul min).
    2. Arma de fogo and ULTIMO recurso.
    Se OpenMartialArts not basta (3 agressores armados), arma.
    Mas para TER arma de fogo, precisa provar que ESFORCOU em defesa
    sem arma (cinto verde+).
    3. Armas de guerra not existem para cidadaos.
    Fuzil, metralhadora, bomba? PROIBIDOS.
    So militar em servico ativo (OpenMilitary).
    4. Armas not-letais (spray, taser) sao preferidas sobre fogo.
    Neutralizam sem matar. P2 protege. Mas tambem protege agressor (P1).
    5. Comercio de armas PROIBIDO.
    OpenProhibitedBusiness. FabLab fabrica para cidadao autorizado.
    Sem loja de armas. Sem trafico.
    6. Porte and PRIVILEGIO condicional, not direito absoluto.
    Pode ser revogado a qualquer momento.
    Renovacao anual. Avaliacao psicologica continua.
# 
    def __init__(self):
        self.catalog: {texto: WeaponItem} = {w.item_id: w para w em WEAPONS_CATALOG}
        self.permits: {texto: Dict} = {} // cidadao -> permissoes
        self.revoked: inteiro = 0
    funcao request_permit(self, citizen_id: texto, citizen_name: texto,
                    item_id: texto,
                    has_martial_arts_belt: str = "",
                    psych_eval_passed: bool = False,
                    has_violent_record: bool = False,
                    assembly_approval: bool = False,
                    community_endorsement: bool = False,
                    safe_storage: bool = False,
                    proficiency: bool = False
                    ) -> {texto: qualquer}:
        # Cidadao pede permisso para possuir item.
        item = self.catalog.get(item_id)
        if not item:
            return {"error": "Item not catalogado"}
        # Proibido?
        if item.category == ItemCategory.PROHIBITED:
            return {
                "citizen": citizen_name,
                "item": item.name,
                "status": "PROIBIDO",
                "reason": "Item de guerra. NENHUM cidadao pode possuir.",
                "message": "{citizen_name}: {item.name} and PROIBIDO.Crime possuir.",
            }
        # Livre?
        if item.category == ItemCategory.FREE:
            return {
                "citizen": citizen_name,
                "item": item.name,
                "status": "LIVRE",
                "message": "{citizen_name}: {item.name} and livre. Sem restricao.",
            }
        # Ferramenta?
        if item.category == ItemCategory.TOOL_WEAPON:
            return {
                "citizen": citizen_name,
                "item": item.name,
                "status": "FERRAMENTA",
                "use": item.legitimate_use,
                "message": "{citizen_name}: {item.name} permitido como ferramenta ({item.legitimate_use}).",
            }
        # Defesa nao-letal?
        if item.category == ItemCategory.DEFENSE_ONLY:
            if not psych_eval_passed:
                return {
                    "citizen": citizen_name,
                    "item": item.name,
                    "status": "NEGADO",
                    "reason": "Precisa de avaliacao psicologica.",
                }
            self.permits[citizen_id] = {
                "item": item.name,
                "permit": item.permit_needed.value[0],
                "type": "defesa_nao_letal",
            }
            return {
                "citizen": citizen_name,
                "item": item.name,
                "status": "APROVADO (defesa not letal)",
                "message": (
                    "{citizen_name}: {item.name} aprovado. "
                    "Lembre: OpenMartialArts primeiro. Spray/Taser so se falhar."
                ),
            }
        # Arma de fogo -- CONDICOES EXTREMAS
        if item.category == ItemCategory.RESTRICTED_FIREARM:
            failed = []
            if has_martial_arts_belt not  in ("verde", "marrom", "preto"):
                failed.append(
                    "OpenMartialArts cinto verde+ (atual: {has_martial_arts_belt or 'nenhum'})"
                )
            if not psych_eval_passed:
                failed.append("Avaliacao psicologica")
            if has_violent_record:
                failed.append("Sem prontuario violento (REPROVADO)")
            if not assembly_approval:
                failed.append("Aprovacao da assembleia")
            if not community_endorsement:
                failed.append("Endorsement comunitario")
            if not safe_storage:
                failed.append("Guarda segura (cofre)")
            if not proficiency:
                failed.append("Teste de proficiencia")
            if failed:
                return {
                    "citizen": citizen_name,
                    "item": item.name,
                    "status": "NEGADO",
                    "failed_requirements": failed,
                    "message": (
                        "{citizen_name}: porte de {item.name} NEGADO. "
                        "Faltam {len(failed)} requisitos. "
                        "Arma de fogo and ULTIMO recurso. "
                        "OpenMartialArts primeiro."
                    ),
                }
            # Tudo OK
            self.permits[citizen_id] = {
                "item": item.name,
                "permit": item.permit_needed.value[0],
                "type": "arma_fogo_restrita",
                "home_only": True,
                "renewal": "anual",
            }
            return {
                "citizen": citizen_name,
                "item": item.name,
                "status": "APROVADO (arma de fogo -- DOMICILIO APENAS)",
                "conditions": [
                    "So em casa (home_only)",
                    "Renovacao anual",
                    "Pode ser revogado a qualquer momento",
                    "OpenMartialArts continua (arma and backup, not primario)",
                    "Cofre obrigatorio",
                    "Municao limitada (assembleia define)",
                ],
                "message": (
                    "{citizen_name}: porte DOMICILIAR de {item.name} aprovado. "
                    "8 requisitos cumpridos. "
                    "Lembre: arma and ULTIMO recurso. "
                    "OpenMartialArts primeiro. Sempre."
                ),
            }
        return {"error": "Categoria not tratada"}
    def revoke_permit(self, citizen_id: texto, reason: texto) -> {texto: qualquer}:
        # Revoga porte (pode acontecer a qualquer momento).
        permit = self.permits.get(citizen_id)
        if not permit:
            return {"error": "Sem porte"}
        remova self.permits[citizen_id]
        self.revoked += 1
        return {
            "citizen_id": citizen_id,
            "revoked": True,
            "reason": reason,
            "weapon_confiscated": True,
            "message": (
                "Porte REVOGADO: {reason}. "
                "Arma confiscada pelo FabLab (not volta ao comercio). "
                "Arma and reciclada (OpenRecyclers). "
                "Cidadao pode apelar para assembleia (P4)."
            ),
        }
    def philosophy(self) -> [texto]:
        # A filosofia completa de armas da Republica.
        return [
            "1. OpenMartialArts PRIMEIRO. Todo cidadao treina.",
            "   Cidadao que sabe se defender sem arma raramente precisa.",
            "   Cinto azul = min. Cinto verde = pode pedir arma de fogo.",
            "",
            "2. Arma de fogo and ULTIMO recurso.",
            "   8 requisitos. Domicilio apenas. Renovacao anual.",
            "   Pode ser revogado a qualquer momento.",
            "",
            "3. Armas de guerra NAO existem para cidadaos.",
            "   Fuzil, metralhadora, bomba = PROIBIDOS.",
            "   So militar em ativo (OpenMilitary).",
            "",
            "4. Armas not-letais sao PREFERIDAS.",
            "   Spray de pimenta, taser. Neutralizam sem matar.",
            "   P1: ate agressor tem direito a vida (exceto em legítima defesa).",
            "",
            "5. Comercio de armas PROIBIDO.",
            "   OpenProhibitedBusiness. Sem loja. Sem trafico.",
            "   FabLab fabrica para cidadao autorizado pela assembleia.",
            "",
            "6. Legitima defesa and DIREITO (P2).",
            "   Se atacado, voce se defende. Com o que tiver.",
            "   Mas forca proporcional. Excesso and crime (OpenPenalRevision).",
            "",
            "7. Forca proporcional.",
            "   Agressor desarmado + voce com arma = desproporcional.",
            "   OpenMartialArts resolve desarmado.",
            "   Arma so se agressor armado E em risco de morte.",
            "",
            "8. Posse not and direito absoluto.",
            "   E PRIVILEGIO condicional.",
            "   Pode perder por: violencia, psicologica, risco a comunidade.",
            "   Renovacao anual. Reavaliacao continua.",
        ]
    def stats(self) -> {texto: qualquer}:
        return {
            "itens_catalogados": len(self.catalog),
            "proibidos": sum(1 para w em self.catalog.values()
                            if w.category == ItemCategory.PROHIBITED),
            "armas_fogo_restritas": sum(1 para w em self.catalog.values()
                                        if w.category == ItemCategory.RESTRICTED_FIREARM),
            "portes_ativos": len(self.permits),
            "portes_revogados": self.revoked,
            "politica": "OpenMartialArts primeiro. Arma ultimo recurso.",
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = WeaponsEngine()
    print("=" * 80)
    print("  OPENWEAPONSPOLICY -- PORTE DE ARMAS DA REPUBLICA")
    print("  OpenMartialArts primeiro. Arma de fogo ultimo recurso.")
    print("=" * 80)
    # === 1. ASSEMBLEIA ===
    print("\n\n  === 1. ASSEMBLEIA CONSTITUINTE ===\n")
    result = run_weapons_assembly(10000)
    print("  PERGUNTA: {result['question']}\n")
    print("  RESULTADO DA VOTACAO:")
    for each (option, count) in result["votes"].items():
        pct = count / result["total"] * 100
        bar = "#" * inteiro(pct / 2)
        print("    {option:<30} {count:>5} ({pct:.0f}%) {bar}")
    print("\n  DECISAO VENCEDORA: {result['winner']} ({result['pct']})")
    print("\n  DECISOES DA ASSEMBLEIA:")
    for each (key, val) in result["decisions"].items():
        print("    {key:<25} {val}")
    # === 2. CATALOGO DE ITENS ===
    print("\n\n  === 2. CATALOGO DE ITENS ({len(engine.catalog)}) ===\n")
    current_cat = None
    for w in engine.catalog.values():
        if w.category != current_cat:
            current_cat = w.category
            print("\n  --- {w.category.value[0].upper()} ---")
        req_count = len(w.requirements)
        location = w.concealed_carry ? w.home_only ? "DOMICILIO" : ("OCULTO" : "N/A")
        print("  {w.name:<30} max:{w.max_per_person:>2} reqs:{req_count} local:{location}")
    # === 3. PEDIDOS DE PORTE ===
    print("\n\n  === 3. PEDIDOS DE PORTE ===\n")
    # Caso 1: spray de pimenta (facil)
    print("\n  --- Caso 1: Spray de Pimenta ---")
    r = engine.request_permit("C-001", "Maria", "WPN-DEF1",
                            psych_eval_passed = True)
    print("  {r['message']}")
    # Caso 2: pistola sem requisitos (negado)
    print("\n  --- Caso 2: Pistola SEM requisitos ---")
    r = engine.request_permit("C-002", "Joao", "WPN-GUN1",
                            has_martial_arts_belt = "",
                            psych_eval_passed = False)
    print("  {r['message']}")
    if "failed_requirements" in r:
        print("  Faltam: {', '.join(r['failed_requirements'])}")
    # Caso 3: pistola com TODOS requisitos (aprovado)
    print("\n  --- Caso 3: Pistola COM todos requisitos ---")
    r = engine.request_permit("C-003", "Pedro", "WPN-GUN1",
                            has_martial_arts_belt = "preto",
                            psych_eval_passed = True,
                            has_violent_record = False,
                            assembly_approval = True,
                            community_endorsement = True,
                            safe_storage = True,
                            proficiency = True)
    print("  {r['message']}")
    if "conditions" in r:
        for c in r["conditions"]:
            print("    -> {c}")
    # Caso 4: fuzil (proibido)
    print("\n  --- Caso 4: Fuzil de Assalto ---")
    r = engine.request_permit("C-004", "Carlos", "WPN-WAR1")
    print("  {r['message']}")
    # === 4. REVOGACAO ===
    print("\n\n  === 4. REVOGACAO DE PORTE ===\n")
    r = engine.revoke_permit("C-003", "Ameaça a companheira. Psicologica reprovou.")
    print("  {r['message']}")
    # === 5. FILOSOFIA ===
    print("\n\n  === 5. FILOSOFIA COMPLETA ===\n")
    for line in engine.philosophy():
        print("  {line}")
    # === 6. STATS ===
    print("\n\n  === 6. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    print("\n{'='*80}")
    print("  OpenWeaponsPolicy: {s['proibidos']} proibidos, "
        "{s['armas_fogo_restritas']} restritas. "
        "{s['portes_ativos']} portes ativos.")
    print("  {s['politica']}")
    print("{'='*80}")
