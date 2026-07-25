#!/usr/bin/env python3
"""
OpenDescriminalize -- Descriminalizacao Popular via Assembleia -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenDescriminalize -- Descriminalizacao Popular via Assembleia
================================================================
"A Republica not prende por saude.
A Republica not prende por escolha corporal.
Maconha? Descriminalizada. Usuario and PACIENTE, not criminoso.
Crack? Doenca. Tratamento, not prisao.
A assembleia DECIDE. O povo VOTA. A Republica OBEDECE."
O QUE ISTO FAZ:
1. CONVOCA assembleia constituinte para votar descriminalizacao
2. Define CADA substancia com politica propria (not tudo igual)
3. Separa USUARIO (saude) de TRAFICANTE (crime real)
4. Tratamento OBRIGATORIO disponivel, prisao ABOLIDA para usuario
5. Integracao com OpenHealth, OpenPsychology, OpenPenalRevision
PRINCIPIO FUNDAMENTAL (P2):
O corpo and SOBERANO. O que a pessoa poe no proprio corpo
and escolha DELA. A Republica EDUCA. TRATA. AMA.
not PUNE. Nunca mais.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa random
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa Counter, defaultdict de collections
# importa datetime de datetime
# ============================================================================
# 1. CLASSIFICACAO DE SUBSTANCIAS
# ============================================================================
class SubstanceCategory(Enum):
    NATURAL_MILD = "natural_leve"  // maconha, cafe, cha
    NATURAL_PSYCHEDELIC = "natural_psicodelico"  // psilocibina, ayahuasca, peyote
    SYNTHETIC_MILD = "sintetico_leve"  // MDMA (pesquisa)
    SYNTHETIC_HARD = "sintetico_pesado"  // crack, metaanfetamina
    PHARMACEUTICAL = "farmaceutico"  // calmantes, opioides (lucro farmaceutica)
    ALCOHOL = "alcool"
    TOBACCO = "tabaco"
class DecriminalizationStatus(Enum):
    LEGAL_REGULATED = "legal_regulado"  // livre para adultos + regulado
    DECRIMINALIZED = "descriminalizado"  // sem prisao, tratamento
    MEDICAL_ONLY = "medicinal_apenas"  // so com receita
    TREATMENT_REQUIRED = "tratamento_obrigatorio"  // uso = tratamento (not prisao)
    RESTRICTED = "restrito"  // pesquisa controlada
    PROHIBITED_TRAFFICKING = "trafico_proibido"  // trafico = crime, uso = saude
class PolicyApproach(Enum):
    # Como a Republica trata cada substancia.
    EDUCATE = "educar"  // informar, deixar escolher
    TREAT = "tratar"  // tratamento disponivel, not obrigatorio
    REGULATE = "regular"  // regular producao/distribuicao
    BAN_TRAFFIC = "banir_trafico"  // traficante = crime, usuario = saude
    RESEARCH = "pesquisar"  // estudo cientifico aberto
# ============================================================================
# 2. SUBSTANCIA
# ============================================================================
# decorador: @dataclass
class Substance:
    # Uma substancia e sua politica na Republica.
    substance_id: texto
    name: texto
    category: SubstanceCategory
    description: str = ""
    # Politica
    status: DecriminalizationStatus = DecriminalizationStatus.DECRIMINALIZED
    approach: [PolicyApproach] = field(default_factory=list)
    # Danos (0-10, base cientifica)
    physical_harm: int = 0
    addiction_potential: int = 0
    social_harm: int = 0
    therapeutic_potential: int = 0 // potencial medicinal
    # Regras
    min_age: int = 18
    public_use: bool = False // pode usar em publico?
    driving_after: bool = False // pode dirigir apos uso?
    production_allowed: bool = False // pode cultivar/produzir?
    commerce_allowed: bool = False // pode vender?
    # Razao da politica
    rationale: str = ""
SUBSTANCES: [Substance] = [
    # === MACONHA ===
    Substance(
        "SUB-CAN", "Maconha (Cannabis)",
        SubstanceCategory.NATURAL_MILD,
        description = (
            "Planta natural usada ha milhares de anos. "
            "Medicinal (dor, nauseia, epilepsia, ansiedade). "
            "Recreativa (relaxamento). "
            "Criminalizada por POLITICA (guerra as drogas), not ciencia."
        ),
        status = DecriminalizationStatus.LEGAL_REGULATED,
        approach = [PolicyApproach.EDUCATE, PolicyApproach.REGULATE,
                PolicyApproach.TREAT, PolicyApproach.BAN_TRAFFIC],
        physical_harm = 2,
        addiction_potential = 3,
        social_harm = 2,
        therapeutic_potential = 8,
        min_age = 18,
        public_use = False,
        driving_after = False,
        production_allowed = True, // pode cultivar para uso proprio
        commerce_allowed = True, // comercio regulado (cooperativas)
        rationale = (
            "Maconha and MENOS danosa que alcool and tabaco (estudo Lancet 2010). "
            "Criminalizacao LOTOU prisoes (OpenPenalRevision: 30% presos por drogas). "
            "Descriminalizacao (Portugal 2001): uso caiu, morte caiu, crime caiu. "
            "Usuario é PACIENTE or CIDADANO. Nao criminoso. "
            "Traficante CONTINUA sendo crime (vitimiza outros). "
            "P2: corpo and soberano. O que poe no corpo and escolha."
        ),
    ),
    # === ALCOHOL ===
    Substance(
        "SUB-ALC", "Alcool",
        SubstanceCategory.ALCOHOL,
        description = (
            "Droga legal mais danosa do mundo. Causa violencia, "
            "doenca, morte. Mas and ACEITO socialmente. "
            "Hipocrisia criminalizar maconha and liberar alcool."
        ),
        status = DecriminalizationStatus.LEGAL_REGULATED,
        approach = [PolicyApproach.EDUCATE, PolicyApproach.REGULATE,
                PolicyApproach.TREAT],
        physical_harm = 6,
        addiction_potential = 7,
        social_harm = 8,
        therapeutic_potential = 1,
        min_age = 18,
        public_use = True, // ja and aceito em festas/restaurantes
        driving_after = False,
        production_allowed = True,
        commerce_allowed = True,
        rationale = (
            "Alcool causa MAIS dano que maconha em TUDO (Lancet 2010). "
            "Mas and legal. A Republica mantem legal (not proibe) mas EDUCA. "
            "OpenNightLife: festas sem obrigacao de beber. "
            "Tratamento para alcoolismo (OpenHealth). "
            "NAO proibe: P2 autonomia. MAS educa and trata."
        ),
    ),
    # === TABACO ===
    Substance(
        "SUB-TOB", "Tabaco",
        SubstanceCategory.TOBACCO,
        "Mata 8 milhoes/ano no mundo. Mais que todas drogas ilicitas juntas.",
        status = DecriminalizationStatus.LEGAL_REGULATED,
        approach = [PolicyApproach.EDUCATE, PolicyApproach.TREAT],
        physical_harm = 8,
        addiction_potential = 8,
        social_harm = 3,
        therapeutic_potential = 0,
        min_age = 18,
        public_use = False, // not em locais fechados
        driving_after = True,
        production_allowed = True,
        commerce_allowed = True,
        rationale = (
            "Tabaco mata mais que TODAS as outras drogas COMBINADAS. "
            "A Republica NAO proibe (P2 corpo soberano). "
            "MAS educa FORTE. Tratamento gratuito (OpenHealth). "
            "OpenBeauty: regeneracao pulmonar (stem cells em pesquisa)."
        ),
    ),
    # === PSILOCIBINA (magic mushrooms) ===
    Substance(
        "SUB-PSI", "Psilocibina (cogumelos)",
        SubstanceCategory.NATURAL_PSYCHEDELIC,
        description = (
            "Psicodelico natural. Estudos (Johns Hopkins, Imperial College) "
            "mostram: trata depressao RESISTENTE, ansiedade terminal, "
            "TOC, adicao. 80% efficacia em depressao terminal. "
            "Nao causa adicao fisica. Nao causa danos cerebrais."
        ),
        status = DecriminalizationStatus.MEDICAL_ONLY,
        approach = [PolicyApproach.RESEARCH, PolicyApproach.TREAT,
                PolicyApproach.EDUCATE],
        physical_harm = 1,
        addiction_potential = 1,
        social_harm = 1,
        therapeutic_potential = 9,
        min_age = 21,
        public_use = False,
        driving_after = False,
        production_allowed = False, // so para pesquisa/tratamento
        commerce_allowed = False,
        rationale = (
            "Psilocibina and PROMISSORA para saude mental (OpenPsychology). "
            "Estudos rigorosos (Nature, Lancet) comprovam eficacia. "
            "A Republica INVESTE em pesquisa. Tratamento supervisionado. "
            "NAO livre (potencial de uso irresponsavel). MAS medicinal."
        ),
    ),
    # === AYAHUASCA ===
    Substance(
        "SUB-AYA", "Ayahuasca",
        SubstanceCategory.NATURAL_PSYCHEDELIC,
        "Cha sagrado amazonico. Tradicao milenar (OpenTradition). Uso ritual.",
        status = DecriminalizationStatus.LEGAL_REGULATED,
        approach = [PolicyApproach.REGULATE, PolicyApproach.RESEARCH],
        physical_harm = 2,
        addiction_potential = 1,
        social_harm = 1,
        therapeutic_potential = 7,
        min_age = 18,
        public_use = False,
        driving_after = False,
        production_allowed = True, // tradicao cultural
        commerce_allowed = False, // so uso ritual/comunitario
        rationale = (
            "Ayahuasca and TRADICAO CULTURAL (OpenTradition). "
            "Uso milenar por povos amazonicos. "
            "Estudos mostram beneficio para depressao and adicao. "
            "Republica protege TRADICAO (P1 respeita cultura). "
            "Uso ritual regulado. Nao comercio."
        ),
    ),
    # === CRACK / COCAINA ===
    Substance(
        "SUB-CRA", "Crack / Cocaina",
        SubstanceCategory.SYNTHETIC_HARD,
        description = (
            "Droga de alta adicao. Destroi vidas. "
            "Usuario NAO and criminoso -- and DOENTE. "
            "Traficante and CRIMINOSO (explora vulneraveis)."
        ),
        status = DecriminalizationStatus.TREATMENT_REQUIRED,
        approach = [PolicyApproach.TREAT, PolicyApproach.BAN_TRAFFIC,
                PolicyApproach.EDUCATE],
        physical_harm = 8,
        addiction_potential = 10,
        social_harm = 9,
        therapeutic_potential = 1,
        min_age = 0, // ninguem deveria usar
        public_use = False,
        driving_after = False,
        production_allowed = False,
        commerce_allowed = False,
        rationale = (
            "Crack and DOENCA, not crime. "
            "Usuario precisa de TRATAMENTO (OpenDignity + OpenHealth). "
            "NAO prisao. Prisao NAO cura adicao. "
            "Traficante and CRIMINOSO que explora vulneraveis (OpenPenalRevision). "
            "Diferenca clara: usuario = paciente. Traficante = crime. "
            "OpenReintegration: tratamento de adicao na colonia de dignidade."
        ),
    ),
    # === MDMA (pesquisa) ===
    Substance(
        "SUB-MDMA", "MDMA (Ecstasy)",
        SubstanceCategory.SYNTHETIC_MILD,
        "Pesquisas (MAPS) mostram: trata TEPT (trauma). 67% efficacia.",
        status = DecriminalizationStatus.RESTRICTED,
        approach = [PolicyApproach.RESEARCH],
        physical_harm = 3,
        addiction_potential = 3,
        social_harm = 2,
        therapeutic_potential = 8,
        min_age = 21,
        production_allowed = False,
        commerce_allowed = False,
        rationale = (
            "MDMA em pesquisa para TEPT (OpenPsychology). "
            "Resultados promissores (MAPS Phase 3). "
            "Republica investe em pesquisa cientifica. "
            "Nao recreativo ainda. Medicinal em estudo."
        ),
    ),
    # === OPIOIDES FARMACEUTICOS ===
    Substance(
        "SUB-OPIO", "Opioides Farmaceuticos",
        SubstanceCategory.PHARMACEUTICAL,
        "Dolores. Fabricados por industria. Causam epidemia de adicao.",
        status = DecriminalizationStatus.MEDICAL_ONLY,
        approach = [PolicyApproach.REGULATE, PolicyApproach.TREAT],
        physical_harm = 7,
        addiction_potential = 9,
        social_harm = 7,
        therapeutic_potential = 5,
        min_age = 0,
        production_allowed = True, // so farmaceutico
        commerce_allowed = False, // so com receita
        rationale = (
            "Opioides sao ARMAS da industria farmaceutica. "
            "Epidemia nos EUA: 500mil mortos. "
            "Republica: receita ESTREITA. Monitoramento (OpenHealth). "
            "OpenPsychologyReparation: repara dependentes. "
            "OpenMentalHygiene: bloqueia lobby farmaceutico."
        ),
    ),
]
# ============================================================================
# 3. VOTACAO DA ASSEMBLEIA
# ============================================================================
def run_decrim_assembly(n_voters: inteiro = 10000) -> {texto: qualquer}:
    # Convoca assembleia para votar descriminalizacao.
    PERGUNTA: "Usuario de drogas deve ser tratado como paciente (saude)
            or criminoso (prisao)?"
    + pergunta especifica para cada substancia.
    # 
    # Votacao geral: paciente vs criminoso
    votes_patient = 0 // tratamento, not prisao
    votes_criminal = 0 // manter criminalizacao
    votes_regulate = 0 // regular + taxar
    for _ in intervalo(n_voters):
        r = random.random()
        if r < 0.72:
            votes_patient = votes_patient + 1 // 72% -- tratamento
        elif r < 0.90:
            votes_regulate = votes_regulate + 1 // 18% -- regular
        else:
            votes_criminal = votes_criminal + 1 // 10% -- manter crime
    # Votacao por substancia
    substance_votes = {}
    for sub in SUBSTANCES:
        # Simular votacao especifica
        if sub.category == SubstanceCategory.NATURAL_MILD:
            yes = random.randint(6500, 8500) // maconha: maioria a favor
        elif sub.category == SubstanceCategory.NATURAL_PSYCHEDELIC:
            yes = random.randint(5000, 7000) // psicodelicos: moderado
        elif sub.category == SubstanceCategory.SYNTHETIC_HARD:
            yes = random.randint(7000, 9000) // crack: tratamento (not legalizar)
        elif sub.category == SubstanceCategory.ALCOHOL:
            yes = random.randint(8000, 9500) // alcool: manter legal
        elif sub.category == SubstanceCategory.TOBACCO:
            yes = random.randint(7500, 9000) // tabaco: manter legal
        else:
            yes = random.randint(4000, 6000)
        no = n_voters - yes
        substance_votes[sub.substance_id] = {
            "name": sub.name,
            "yes": yes,
            "no": no,
            "approved": yes > no,
            "pct": "{yes/n_voters*100:.0f}%",
            "status": sub.status.value,
        }
    return {
        "question": (
            "Usuario de drogas deve ser tratado como PACIENTE (saude) "
            "or CRIMINOSO (prisao)?"
        ),
        "votes_patient": votes_patient,
        "votes_regulate": votes_regulate,
        "votes_criminal": votes_criminal,
        "total": n_voters,
        "winner": "PACIENTE (TRATAMENTO)" if votes_patient > votes_criminal
                else "CRIMINOSO (PRISAO)",
        "pct_patient": "{votes_patient/n_voters*100:.0f}%",
        "substance_votes": substance_votes,
        "decision": {
            "usuario_e_paciente": True,         // APROVADO (72%)
            "usuario_e_criminoso": False,        // REJEITADO
            "traficante_e_criminoso": True,      // MANTIDO
            "tratamento_obrigatorio_disponivel": True,
            "prisao_para_usuario": False,        // ABOLIDA
            "maconha_legal_regulada": True,      // APROVADO
            "psicodelicos_medicinais": True,     // APROVADO (pesquisa)
            "crack_tratamento_nao_prisao": True,   // APROVADO
            "producao_pessoal_maconha": True,    // pode cultivar
            "open_dignity_para_dependentes": True,   // colonia de tratamento
        },
    }
# ============================================================================
# 4. MOTOR DE DESCRIMINALIZACAO
# ============================================================================
class DecrimEngine:
    # Motor que executa a descriminalizacao aprovada pela assembleia.
    O QUE MUDA IMEDIATAMENTE:
    1. Usuario preso por drogas -> LIBERADO (OpenPenalRevision revisa)
    2. Usuario not preso mais -> encaminhado a OpenHealth (se quiser)
    3. Traficante CONTINUA preso (crime real)
    4. Maconha: legal regulado (producao propria + cooperativas)
    5. Psicodelicos: pesquisa medicinal aberta
    6. Crack: tratamento compulsorio em OpenDignity (not prisao)
    O QUE not MUDA:
    - Dirigir alcoolado continua proibido (P2 protege OUTROS)
    - Usar em publico continua restrito (respeitar espaco alheio)
    - Trafico continua crime (vitimiza outros)
    - Venda para menores continua crime (protege criancas)
    # 
    def __init__(self):
        self.substances: {texto: Substance} = {s.substance_id: s para s em SUBSTANCES}
        self.reviews: [Dict] = []
        self.liberated_prisoners: inteiro = 0
        self.treated_users: inteiro = 0
    funcao check_arrest_type(self, arrest_reason: texto,
                        quantity_grams: float = 0,
                        is_trafficking: bool = False) -> {texto: qualquer}:
        # Verifica se prisao e valida ou deve ser revertida.
        CRITERIO USER vs TRAFFICKER (Brasil atual):
        - < quantidade para uso pessoal: usuario (not crime)
        - > quantidade or com provas de venda: traficante (crime)
        Na Republica:
        - Usuario: not PRENDE. Tratamento se quiser.
        - Traficante: PRENDE (vitimiza outros). OpenPenalRevision transforma.
        # 
        if is_trafficking:
            return {
                "type": "TRAFICANTE",
                "action": "MANTER PRISAO (vitimiza outros)",
                "process": "OpenPenalRevision: transformar em forca produtiva",
                "note": "Traficante and crime REAL. Explota vulneraveis.",
            }
        # Usuario -- LIBERAR
        self.liberated_prisoners += 1
        return {
            "type": "USUARIO",
            "action": "LIBERAR IMEDIATAMENTE",
            "reason": (
                "Usuario de drogas and PACIENTE, not criminoso. "
                "Assembleia aprovou: tratamento, not prisao. "
                "Prisao not cura adicao. Tratamento cura."
            ),
            "referral": "OpenHealth (tratamento VOLUNTARIO)",
            "referral_optional": (
                "Se NAO quiser tratamento, and DIREITO (P2 autonomia corporal). "
                "A Republica so OFERECE. Nao obriga."
            ),
            "record": "PRONTUARIO LIMPO (sem marcador de drogas)",
            "message": (
                "Usuario preso por '{arrest_reason}' LIBERADO. "
                "Prisao por uso and INCONSTITUCIONAL na Republica. "
                "Tratamento disponivel. Nao obrigatorio. P2."
            ),
        }
    funcao offer_treatment(self, person: texto,
                        substance_id: texto) -> {texto: qualquer}:
        # Oferece tratamento (VOLUNTARIO).
        sub = self.substances.get(substance_id)
        if not sub:
            return {"error": "Substancia not encontrada"}
        self.treated_users += 1
        return {
            "person": person,
            "substance": sub.name,
            "treatment_type": (
                "OpenDignity (colonia de tratamento)" if sub.addiction_potential >= 8
                else "OpenHealth (ambulatorial)" if sub.addiction_potential >= 4
                else "OpenPsychology (terapia)" if sub.addiction_potential >= 2
                else "OpenEducation (informacao)"
            ),
            "voluntary": True,
            "can_refuse": True,
            "p2": "Corpo and soberano. Tratamento and oferta, not obrigacao.",
            "message": (
                "{person}: tratamento para {sub.name} disponivel. "
                "Custo: ZERO. Nivel: Sirio-Libanes. "
                "VOLUNTARIO. Pode recusar (P2)."
            ),
        }
    def prison_impact_report(self) -> {texto: qualquer}:
        # Impacto da descriminalizacao no sistema prisional.
        return {
            "brasil_atual": {
                "total_presos": 800000,
                "presos_por_drogas": 240000,   // 30%
                "presos_por_USO": 70000,       // 9% so por uso
                "presos_por_TRAFICO": 170000,   // 21% trafico
                "custo_anual": "R$ 42 bi",
            },
            "republica": {
                "presos_por_USO": 0,            // ZERO -- abolido
                "presos_por_TRAFICO": 170000,   // mantido (crime real)
                "liberados": 70000,             // usuarios liberados
                "economizada": "R$ 3.7 bi/ano",
                "tratamento_oferecido": "OpenDignity + OpenHealth",
                "message": (
                    "70.000 pessoas presas SO por uso -> LIBERADAS. "
                    "Traficantes MANTIDOS (crime real). "
                    "Economia: R$ 3.7 bi/ano redirecionada para tratamento."
                ),
            },
        }
    def substance_policy(self, substance_id: texto) -> {texto: qualquer}:
        # Politica completa de uma substancia.
        sub = self.substances.get(substance_id)
        if not sub:
            return {"error": "not encontrada"}
        return {
            "substance": sub.name,
            "category": sub.category.value,
            "status": sub.status.value,
            "approach": [a.value para a em sub.approach],
            "harms": {
                "physical": "{sub.physical_harm}/10",
                "addiction": "{sub.addiction_potential}/10",
                "social": "{sub.social_harm}/10",
                "therapeutic": "{sub.therapeutic_potential}/10",
            },
            "rules": {
                "min_age": sub.min_age,
                sub.public_use ? "public_use": "permitido" : "proibido",
                sub.driving_after ? "driving": "permitido" : "proibido",
                sub.production_allowed ? "production": "permitido" : "proibido",
                sub.commerce_allowed ? "commerce": "permitido" : "proibido",
            },
            "rationale": sub.rationale,
        }
    def stats(self) -> {texto: qualquer}:
        return {
            "total_substancias": len(self.substances),
            "legal_regulado": sum(1 para s em self.substances.values()
                                if s.status == DecriminalizationStatus.LEGAL_REGULATED),
            "medicinal": sum(1 para s em self.substances.values()
                            if s.status == DecriminalizationStatus.MEDICAL_ONLY),
            "tratamento_obrigatorio": sum(1 para s em self.substances.values()
                                        if s.status == DecriminalizationStatus.TREATMENT_REQUIRED),
            "presos_liberados": self.liberated_prisoners,
            "usuarios_tratados": self.treated_users,
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = DecrimEngine()
    print("=" * 80)
    print("  OPENDESCRIMINALIZE -- ASSEMBLEIA CONSTITUINTE")
    print("  'Usuario and PACIENTE. Nao criminoso. Nunca mais.'")
    print("=" * 80)
    # === 1. PERGUNTA A ASSEMBLEIA ===
    print("\n\n  === 1. PERGUNTA A ASSEMBLEIA ===\n")
    result = run_decrim_assembly(10000)
    print("  {result['question']}")
    print("\n  PACIENTE (tratamento):    {result['votes_patient']:>6} "
        "({result['pct_patient']})")
    print("  REGULAR (taxar):          {result['votes_regulate']:>6} "
        "({result['votes_regulate']/100:.0f}%)")
    print("  CRIMINOSO (prisao):       {result['votes_criminal']:>6} "
        "({result['votes_criminal']/100:.0f}%)")
    print("\n  RESULTADO: {result['winner']}")
    # === 2. VOTACAO POR SUBSTANCIA ===
    print("\n\n  === 2. VOTACAO POR SUBSTANCIA ===\n")
    for each (sid, vote) in result["substance_votes"].items():
        icon = vote["approved"] ? "APR" : "REJ"
        print("  [{icon}] {vote['name']:<25} {vote['yes']:>5} sim / "
            "{vote['no']:>5} not ({vote['pct']})")
        print("       Status: {vote['status']}")
    # === 3. DECISAO DA ASSEMBLEIA ===
    print("\n\n  === 3. DECISAO DA ASSEMBLEIA ===\n")
    for each (key, val) in result["decision"].items():
        status = val ? "SIM" : "NAO"
        print("  {key:<40} {status}")
    # === 4. POLITICA POR SUBSTANCIA ===
    print("\n\n  === 4. POLITICA DETALHADA POR SUBSTANCIA ===\n")
    for sid in engine.substances:
        policy = engine.substance_policy(sid)
        print("\n  {policy['substance'].upper()} ({policy['category']})")
        print("  Status: {policy['status']}")
        print("  Danos: fisico {policy['harms']['physical']}, "
            "adicao {policy['harms']['addiction']}, "
            "social {policy['harms']['social']}, "
            "terapeutico {policy['harms']['therapeutic']}")
        print("  Regras: idade {policy['rules']['min_age']}, "
            "publico: {policy['rules']['public_use']}, "
            "producao: {policy['rules']['production']}")
        print("  Razao: {policy['rationale'][:100]}...")
    # === 5. REVISAO DE PRISOES ===
    print("\n\n  === 5. REVISAO DE PRISOES (usuario vs traficante) ===\n")
    cases = [
        ("porte de maconha 5g (uso pessoal)", 5.0, False),
        ("porte de crack 0.5g (uso)", 0.5, False),
        ("trafico de maconha 5kg (venda)", 5000.0, True),
        ("porte de cocaina 2g (uso)", 2.0, False),
        ("trafico de crack (vendendo em esquina)", 50.0, True),
        ("cultivo de 3 pes de maconha (uso proprio)", 300.0, False),
    ]
    para reason, qty, trafficking in cases:
        check = engine.check_arrest_type(reason, qty, trafficking)
        action = check["action"]
        print("  [{check['type']:<11}] {reason:<45} -> {action}")
    # === 6. OFERECER TRATAMENTO ===
    print("\n\n  === 6. TRATAMENTO OFERECIDO (VOLUNTARIO) ===\n")
    treatments = [
        ("Carlos", "SUB-CRA"),    // crack
        ("Ana", "SUB-CAN"),       // maconha (leve -- so terapia)
        ("Pedro", "SUB-OPIO"),    // opioide
    ]
    for each (person, sub_id) in treatments:
        t = engine.offer_treatment(person, sub_id)
        print("  {t['person']:<12} {t['substance']:<20} -> {t['treatment_type']}")
        print("    Voluntario: {t['voluntary']}. P2: {t['p2']}")
    # === 7. IMPACTO PRISIONAL ===
    print("\n\n  === 7. IMPACTO DA DESCRIMINALIZACAO NO SISTEMA PRISIONAL ===\n")
    impact = engine.prison_impact_report()
    print("\n  BRASIL ATUAL:")
    for each (k, v) in impact["brasil_atual"].items():
        print("    {k:<25} {v}")
    print("\n  REPUBLICA:")
    for each (k, v) in impact["republica"].items():
        if k != "message":
            print("    {k:<25} {v}")
    print("\n  {impact['republica']['message']}")
    # === 8. STATS ===
    print("\n\n  === 8. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA DO OPENDESCRIMINALIZE")
    print("{'='*80}")
    print("""
USUARIO and PACIENTE. not CRIMINOSO.
    A assembleia votou: 72% a favor de tratamento, not prisao.
    Usuario de drogas tem ADICAO. Adicao and DOENCA.
    Prisao not cura doenca. Tratamento cura.
    Prender usuario and PUNIR DOENTE. A Republica not faz isso.
TRAFICANTE and CRIMINOSO. CONTINUA PRESO.
    Quem vende droga EXPLORA vulneraveis.
    Quem financia adicao alheia por lucro COMETE CRIME.
    Traficante vai para OpenPenalRevision (transformacao).
    Diferenca clara: usuario = paciente. Traficante = crime.
MACONHA: LEGAL REGULADO.
    Menos danosa que alcool and tabaco (Lancet 2010).
    Criminalizacao lotou prisoes (30% presos por drogas).
    Descriminalizacao funciona (Portugal 2001: uso caiu, morte caiu).
    Producao pessoal PERMITIDA (pode cultivar).
    Comercio REGULADO (cooperativas, not traficante).
    Medicinal GARANTIDO (dor, epilepsia, ansiedade).
    P2: corpo soberano. O que poe no corpo and escolha.
PSICOdelicos: MEDICINAL (PESQUISA).
    Psilocibina: 80% efficacia em depressao terminal (Johns Hopkins).
    Ayahuasca: tradicao milenar (OpenTradition protege).
    MDMA: trata TEPT (MAPS Phase 3).
    A Republica INVESTE em ciencia. Nao bloqueia por preconceito.
CRACK: TRATAMENTO, not PRISAO.
    Crack and adicao SEVERA. Usuario esta DOENTE.
    OpenDignity: colonia de tratamento para dependentes.
    Moradia + comida + tratamento + oficio + comunidade.
    not prisao. not abandono. TRATAMENTO.
OPIoides: ARMAS FARMACEUTICAS.
    Industria fabrica adicao por lucro (500mil mortos EUA).
    Republica: receita ESTREITA. Monitoramento OpenHealth.
    OpenPsychologyReparation: repara dependentes.
    OpenMentalHygiene: bloqueia lobby farmaceutico.
O QUE MUDA IMEDIATAMENTE:
    1. 70.000 presos SO por uso -> LIBERADOS
    2. Usuario not and mais preso -> tratamento voluntario
    3. Maconha: cultivar proprio liberado
    4. Prontuario: LIMPO (sem marcador de drogas)
    5. Traficante: CONTINUA preso (crime real)
    6. Economia: R$ 3.7 bi/ano redirecionada para tratamento
O QUE not MUDA:
    - Dirigir drogado continua proibido (protege OUTROS)
    - Vender para menor continua crime (protege criancas)
    - Trafico continua crime (vitimiza)
    - Usar em publico continua restrito (respeito ao espaco alheio)
DADOS CIENTIFICOS:
    - Lancet 2010: alcool mais danoso que heroina (Nutt et al.)
    - Portugal 2001: descriminalizacao -> uso caiu, morte caiu, crime caiu
    - Johns Hopkins: psilocibina 80% efficacia depressao terminal
    - MAPS: MDMA 67% efficacia TEPT
    - OpenHistory: fact-check de todas afirmacoes
PRINCIPIOS:
    P1: Tratamento para todos. Sem classe. Sem estigma.
    P2: Corpo and SOBERANO. O que poe nele and escolha. Tratamento and oferta.
    P3: Tratar adicao = trabalho de alto impacto (medicos, terapeutas).
    P4: Assembleia DECIDE. 72% votou tratamento. Republica obedece.
# )
    print("{'='*80}")
    print("  OpenDescriminalize: {s['presos_liberados']} presos liberados, "
        "{s['usuarios_tratados']} usuarios em tratamento.")
    print("  Usuario and paciente. Nao criminoso. Nunca mais.")
    print("{'='*80}")
