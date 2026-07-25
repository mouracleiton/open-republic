// OpenWeaponsPolicy -- Politica de Porte de Armas da Republica -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenWeaponsPolicy -- Politica de Porte de Armas da Republica;
===============================================================;
"A Republica PREFERE paz. Mas P2 diz: corpo && seu.;
Voce tem direito de se defender.;
OpenMartialArts primeiro. Sempre.;
Arma de fogo? ULTIMO recurso. Condicoes EXTREMAS.;
Armas de guerra? ! existem nas maos de cidadaos.;
Assembleia decide.";
ASSEMBLEIA CONSTITUINTE CONVOCADA:;
"Qual a politica de porte de armas na Republica?";
O QUE ESTE SISTEMA FAZ:;
1. Define 5 categorias de itens (proibido, restrito, ferramenta,(defesa, livre);
2. Estabelece condicoes EXTREMAS para porte de arma de fogo;
3. Prioriza OpenMartialArts sobre arma;
4. Proibe armas de guerra para cidadaos;
5. Regula ferramentas que podem ser armas (faca, machado);
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa Counter, defaultdict de collections
// importa datetime de datetime
// ============================================================================
// 1. CATEGORIAS DE ITENS
// ============================================================================
class ItemCategory {
    // Categoria de item baseado em potencial de dano.
    PROHIBITED = ("proibido", 0)  // arma de guerra, bomba;
    RESTRICTED_FIREARM = ("arma_fogo_restrita", 1)  // pistola, revolver;
    TOOL_WEAPON = ("ferramenta_arma", 2)  // faca, machado, foice;
    DEFENSE_ONLY = ("defesa_apenas", 3)  // spray pimenta, taser;
    FREE = ("livre", 4)  // sem restricao;
class WeaponPermit {
    // Niveis de permisso de porte.
    NONE = ("nenhum", 0)  // sem porte;
    SELF_DEFENSE = ("autodefesa", 1)  // spray, taser;
    TOOL = ("ferramenta", 2)  // faca de trabalho;
    FIREARM_RESTRICTED = ("arma_fogo", 3)  // arma de fogo (extremo);
    SECURITY = ("seguranca", 4)  // patrulha comunitaria;
class PermitRequirement {
    // Requisitos para conseguir porte.
    OPEN_MARTIAL_ARTS = "cinto_verde_martial_arts";
    PSYCH_EVAL = "avaliacao_psicologica";
    NO_CRIMINAL_RECORD = "sem_prontuario_violento";
    ASSEMBLY_APPROVAL = "aprovacao_assembleia";
    ANNUAL_RENEWAL = "renovacao_anual";
    SAFE_STORAGE = "guarda_segura";
    PROFICIENCY_TEST = "teste_proficiencia";
    COMMUNITY_ENDORSEMENT = "endorsement_comunitario";
// ============================================================================
// 2. ITENS CATALOGADOS
// ============================================================================
// decorador: @dataclass
class WeaponItem {
    // Um item classificado por potencial de dano.
    item_id: texto;
    name: texto;
    category: ItemCategory;
    const description = "";
    const legitimate_use = ""  // uso legitimo (trabalho, defesa);
    const permit_needed = WeaponPermit.NONE;
    const requirements = field(default_factory=list);
    // Restricoes
    const max_per_person = 0 // 0 = proibido, 1 = uma unidade;
    const open_carry = false // pode portar visivel?;
    const concealed_carry = false // pode portar escondido?;
    const home_only = false // so em casa?;
const WEAPONS_CATALOG = [;
    // === PROIBIDOS (categoria 0) ===
    WeaponItem("WPN-WAR1", "Fuzil de Assalto", ItemCategory.PROHIBITED,;
            "Arma de guerra. NENHUM cidadao precisa. So militar em ativo.",;
            permit_needed = WeaponPermit.NONE, max_per_person=0),;
    WeaponItem("WPN-WAR2", "Metralhadora", ItemCategory.PROHIBITED,;
            "Arma de guerra. PROIBIDA para cidadaos.",;
            permit_needed = WeaponPermit.NONE, max_per_person=0),;
    WeaponItem("WPN-WAR3", "Bomba/Explosivo", ItemCategory.PROHIBITED,;
            "Explosivo. PROIBIDO. So FabLab controlado.",;
            permit_needed = WeaponPermit.NONE, max_per_person=0),;
    WeaponItem("WPN-WAR4", "Lanca-foguete", ItemCategory.PROHIBITED,;
            "Arma de guerra. PROIBIDO.",;
            permit_needed = WeaponPermit.NONE, max_per_person=0),;
    WeaponItem("WPN-WAR5", "Arma Quimica/Biologica", ItemCategory.PROHIBITED,;
            "PROIBIDO. Crime contra humanidade.",;
            permit_needed = WeaponPermit.NONE, max_per_person=0),;
    // === ARMA DE FOGO RESTRITA (categoria 1) ===
    WeaponItem("WPN-GUN1", "Pistola (calibre limitado)", ItemCategory.RESTRICTED_FIREARM,;
            "Pistola. ULTIMO recurso de autodefesa. Condicoes extremas.",;
            legitimate_use = "Autodefesa domiciliar (extremo)",;
            permit_needed = WeaponPermit.FIREARM_RESTRICTED,;
            max_per_person = 1, home_only=true,;
            requirements = [;
                PermitRequirement.OPEN_MARTIAL_ARTS,;
                PermitRequirement.PSYCH_EVAL,;
                PermitRequirement.NO_CRIMINAL_RECORD,;
                PermitRequirement.ASSEMBLY_APPROVAL,;
                PermitRequirement.ANNUAL_RENEWAL,;
                PermitRequirement.SAFE_STORAGE,;
                PermitRequirement.PROFICIENCY_TEST,;
                PermitRequirement.COMMUNITY_ENDORSEMENT,;
            ]),;
    WeaponItem("WPN-GUN2", "Revolver (calibre limitado)", ItemCategory.RESTRICTED_FIREARM,;
            "Revolver. Mesmas restricoes que pistola.",;
            legitimate_use = "Autodefesa domiciliar (extremo)",;
            permit_needed = WeaponPermit.FIREARM_RESTRICTED,;
            max_per_person = 1, home_only=true,;
            requirements = [;
                PermitRequirement.OPEN_MARTIAL_ARTS,;
                PermitRequirement.PSYCH_EVAL,;
                PermitRequirement.NO_CRIMINAL_RECORD,;
                PermitRequirement.ASSEMBLY_APPROVAL,;
                PermitRequirement.ANNUAL_RENEWAL,;
                PermitRequirement.SAFE_STORAGE,;
                PermitRequirement.PROFICIENCY_TEST,;
                PermitRequirement.COMMUNITY_ENDORSEMENT,;
            ]),;
    // === FERRAMENTA QUE PODE SER ARMA (categoria 2) ===
    WeaponItem("WPN-TOOL1", "Faca de Cozinha", ItemCategory.TOOL_WEAPON,;
            "Ferramenta de cozinha. Uso legitimo: cozinhar.",;
            legitimate_use = "Cozinha",;
            permit_needed = WeaponPermit.NONE, max_per_person=99,;
            home_only = true),;
    WeaponItem("WPN-TOOL2", "Faca de Trabalho (agricola/caca)", ItemCategory.TOOL_WEAPON,;
            "Faca de trabalho. Uso legitimo: agricultura, FabLab.",;
            legitimate_use = "Trabalho agricola/industrial",;
            permit_needed = WeaponPermit.TOOL, max_per_person=2),;
    WeaponItem("WPN-TOOL3", "Machado", ItemCategory.TOOL_WEAPON,;
            "Ferramenta. Uso legitimo: lenha, construcao.",;
            legitimate_use = "Lenha, construcao, FabLab",;
            permit_needed = WeaponPermit.TOOL, max_per_person=1),;
    WeaponItem("WPN-TOOL4", "Foice/Enxada", ItemCategory.TOOL_WEAPON,;
            "Ferramenta agricola. Uso legitimo: agricultura.",;
            legitimate_use = "Agricultura (OpenAgrarian)",;
            permit_needed = WeaponPermit.NONE, max_per_person=2),;
    // === DEFESA APENAS (categoria 3) ===
    WeaponItem("WPN-DEF1", "Spray de Pimenta", ItemCategory.DEFENSE_ONLY,;
            "Defesa !-letal. Cega temporariamente. Permite fugir.",;
            legitimate_use = "Autodefesa (! letal)",;
            permit_needed = WeaponPermit.SELF_DEFENSE, max_per_person=1,;
            concealed_carry = true,;
            requirements = [;
                PermitRequirement.PSYCH_EVAL,;
            ]),;
    WeaponItem("WPN-DEF2", "Taser (choque)", ItemCategory.DEFENSE_ONLY,;
            "Defesa !-letal. Incapacita temporariamente.",;
            legitimate_use = "Autodefesa (! letal)",;
            permit_needed = WeaponPermit.SELF_DEFENSE, max_per_person=1,;
            concealed_carry = true,;
            requirements = [;
                PermitRequirement.PSYCH_EVAL,;
                PermitRequirement.PROFICIENCY_TEST,;
            ]),;
    // === LIVRE (categoria 4) ===
    WeaponItem("WPN-FREE1", "Bastao de Madeira", ItemCategory.FREE,;
            "Bastao. Ferramenta de treino OpenMartialArts.",;
            legitimate_use = "Treino Kali/Escrima",;
            permit_needed = WeaponPermit.NONE, max_per_person=5),;
    WeaponItem("WPN-FREE2", "Apito de Emergencia", ItemCategory.FREE,;
            "Apito. Alerta comunitario.",;
            legitimate_use = "Sinalizar emergencia",;
            permit_needed = WeaponPermit.NONE, max_per_person=3),;
];
// ============================================================================
// 3. VOTACAO DA ASSEMBLEIA
// ============================================================================
run_weapons_assembly(n_voters: inteiro = 10000) {
    // Assembleia vota politica de armas.
    votes = {
        "proibir_todo_porte": 0,            // zero armas para cidadaos;
        "permitir_apenas_defesa": 0,         // so spray/taser;
        "permitir_restrito_extremo": 0,      // arma de fogo com condicoes;
        "permitir_livre": 0,                 // armamento livre (EUA-style);
    };
    for (const _ of intervalo(n_voters)) {
        r = random.random();
        if (r < 0.35) {
            votes["proibir_todo_porte"] += 1;
        } else if (r < 0.50) {
            votes["permitir_livre"] += 1;
        } else if (r < 0.80) {
            votes["permitir_apenas_defesa"] += 1;
        } else {
            votes["permitir_restrito_extremo"] += 1;
    // Maioria
    winner = maximo(votes, key=votes.get);
    return {;
        "question": (;
            "Qual a politica de porte de armas na Republica?";
        ),;
        "votes": votes,;
        "total": n_voters,;
        "winner": winner,;
        "pct": "{votes[winner]/n_voters*100:.0f}%",;
        "decisions": {
            "armas_de_guerra": "PROIBIDAS para cidadaos (unanime)",;
            "armas_de_fogo": (;
                "RESTRITAS. Condicoes extremas: ";
                "OpenMartialArts cinto verde + psicologica + ";
                "sem prontuario violento + assembleia aprova + ";
                "renovacao anual + guarda segura + proficiencia + ";
                "endorsement comunitario. SO domicilio.";
            ),;
            "armas_nao_letais": "PERMITIDAS (spray, taser) com psicologica",;
            "ferramentas": "PERMITIDAS para trabalho (! para porte como arma)",;
            "open_martial_arts": "PRIORIDADE. Todo cidadao treina. Arma && ultimo recurso.",;
            "porte_visivel": "PROIBIDO (exceto seguraca em patrulha)",;
            "porte_escondido": "SO spray/taser (! letal)",;
            "comercio_armas": "PROIBIDO (OpenProhibitedBusiness). FabLab fabrica.",;
            "calibre_maximo": "Limitado pela assembleia",;
            "renovacao": "ANUAL. Pode perder a qualquer momento.",;
        },;
    };
// ============================================================================
// 4. MOTOR DE ARMAS
// ============================================================================
class WeaponsEngine {
    // Motor que gere politica de armas da Republica.
    FILOSOFIA:;
    1. OpenMartialArts PRIMEIRO. Sempre.;
    Cidadao que sabe se defender SEM arma ! precisa de arma.;
    Todo cidadao treina OpenMartialArts (cinto azul minimo).;
    2. Arma de fogo && ULTIMO recurso.;
    Se OpenMartialArts ! basta (3 agressores armados), arma.;
    Mas para TER arma de fogo, precisa provar que ESFORCOU em defesa;
    sem arma (cinto verde+).;
    3. Armas de guerra ! existem para cidadaos.;
    Fuzil, metralhadora, bomba? PROIBIDOS.;
    So militar em servico ativo (OpenMilitary).;
    4. Armas !-letais (spray, taser) sao preferidas sobre fogo.;
    Neutralizam sem matar. P2 protege. Mas tambem protege agressor (P1).;
    5. Comercio de armas PROIBIDO.;
    OpenProhibitedBusiness. FabLab fabrica para cidadao autorizado.;
    Sem loja de armas. Sem trafico.;
    6. Porte && PRIVILEGIO condicional, ! direito absoluto.;
    Pode ser revogado a qualquer momento.;
    Renovacao anual. Avaliacao psicologica continua.;
//
    __init__(self) {
        self.catalog: {texto: WeaponItem} = {w.item_id: w para w em WEAPONS_CATALOG};
        self.permits: {texto: Dict} = {} // cidadao -> permissoes;
        self.revoked: inteiro = 0;
    funcao request_permit(self, citizen_id: texto, citizen_name: texto,
                    item_id: texto,;
                    const has_martial_arts_belt = "",;
                    const psych_eval_passed = false,;
                    const has_violent_record = false,;
                    const assembly_approval = false,;
                    const community_endorsement = false,;
                    const safe_storage = false,;
                    const proficiency = false;
                    ) -> {texto: qualquer}:;
        // Cidadao pede permisso para possuir item.
        item = self.catalog.get(item_id);
        if (! item) {
            return {"error": "Item ! catalogado"};
        // Proibido?
        if (item.category == ItemCategory.PROHIBITED) {
            return {;
                "citizen": citizen_name,;
                "item": item.name,;
                "status": "PROIBIDO",;
                "reason": "Item de guerra. NENHUM cidadao pode possuir.",;
                "message": "{citizen_name}: {item.name} && PROIBIDO.Crime possuir.",;
            };
        // Livre?
        if (item.category == ItemCategory.FREE) {
            return {;
                "citizen": citizen_name,;
                "item": item.name,;
                "status": "LIVRE",;
                "message": "{citizen_name}: {item.name} && livre. Sem restricao.",;
            };
        // Ferramenta?
        if (item.category == ItemCategory.TOOL_WEAPON) {
            return {;
                "citizen": citizen_name,;
                "item": item.name,;
                "status": "FERRAMENTA",;
                "use": item.legitimate_use,;
                "message": "{citizen_name}: {item.name} permitido como ferramenta ({item.legitimate_use}).",;
            };
        // Defesa nao-letal?
        if (item.category == ItemCategory.DEFENSE_ONLY) {
            if (! psych_eval_passed) {
                return {;
                    "citizen": citizen_name,;
                    "item": item.name,;
                    "status": "NEGADO",;
                    "reason": "Precisa de avaliacao psicologica.",;
                };
            self.permits[citizen_id] = {
                "item": item.name,;
                "permit": item.permit_needed.value[0],;
                "type": "defesa_nao_letal",;
            };
            return {;
                "citizen": citizen_name,;
                "item": item.name,;
                "status": "APROVADO (defesa ! letal)",;
                "message": (;
                    "{citizen_name}: {item.name} aprovado. ";
                    "Lembre: OpenMartialArts primeiro. Spray/Taser so se falhar.";
                ),;
            };
        // Arma de fogo -- CONDICOES EXTREMAS
        if (item.category == ItemCategory.RESTRICTED_FIREARM) {
            failed = [];
            if (has_martial_arts_belt !  in ("verde", "marrom", "preto")) {
                failed.append(;
                    "OpenMartialArts cinto verde+ (atual: {has_martial_arts_belt or 'nenhum'})";
                );
            if (! psych_eval_passed) {
                failed.append("Avaliacao psicologica");
            if (has_violent_record) {
                failed.append("Sem prontuario violento (REPROVADO)");
            if (! assembly_approval) {
                failed.append("Aprovacao da assembleia");
            if (! community_endorsement) {
                failed.append("Endorsement comunitario");
            if (! safe_storage) {
                failed.append("Guarda segura (cofre)");
            if (! proficiency) {
                failed.append("Teste de proficiencia");
            if (failed) {
                return {;
                    "citizen": citizen_name,;
                    "item": item.name,;
                    "status": "NEGADO",;
                    "failed_requirements": failed,;
                    "message": (;
                        "{citizen_name}: porte de {item.name} NEGADO. ";
                        "Faltam {len(failed)} requisitos. ";
                        "Arma de fogo && ULTIMO recurso. ";
                        "OpenMartialArts primeiro.";
                    ),;
                };
            // Tudo OK
            self.permits[citizen_id] = {
                "item": item.name,;
                "permit": item.permit_needed.value[0],;
                "type": "arma_fogo_restrita",;
                "home_only": true,;
                "renewal": "anual",;
            };
            return {;
                "citizen": citizen_name,;
                "item": item.name,;
                "status": "APROVADO (arma de fogo -- DOMICILIO APENAS)",;
                "conditions": [;
                    "So em casa (home_only)",;
                    "Renovacao anual",;
                    "Pode ser revogado a qualquer momento",;
                    "OpenMartialArts continua (arma && backup, ! primario)",;
                    "Cofre obrigatorio",;
                    "Municao limitada (assembleia define)",;
                ],;
                "message": (;
                    "{citizen_name}: porte DOMICILIAR de {item.name} aprovado. ";
                    "8 requisitos cumpridos. ";
                    "Lembre: arma && ULTIMO recurso. ";
                    "OpenMartialArts primeiro. Sempre.";
                ),;
            };
        return {"error": "Categoria ! tratada"};
    revoke_permit(self, citizen_id: texto, reason: texto) {
        // Revoga porte (pode acontecer a qualquer momento).
        permit = self.permits.get(citizen_id);
        if (! permit) {
            return {"error": "Sem porte"};
        remova self.permits[citizen_id];
        self.revoked += 1;
        return {;
            "citizen_id": citizen_id,;
            "revoked": true,;
            "reason": reason,;
            "weapon_confiscated": true,;
            "message": (;
                "Porte REVOGADO: {reason}. ";
                "Arma confiscada pelo FabLab (! volta ao comercio). ";
                "Arma && reciclada (OpenRecyclers). ";
                "Cidadao pode apelar para assembleia (P4).";
            ),;
        };
    philosophy(self) {
        // A filosofia completa de armas da Republica.
        return [;
            "1. OpenMartialArts PRIMEIRO. Todo cidadao treina.",;
            "   Cidadao que sabe se defender sem arma raramente precisa.",;
            "   Cinto azul = minimo. Cinto verde = pode pedir arma de fogo.",;
            "",;
            "2. Arma de fogo && ULTIMO recurso.",;
            "   8 requisitos. Domicilio apenas. Renovacao anual.",;
            "   Pode ser revogado a qualquer momento.",;
            "",;
            "3. Armas de guerra NAO existem para cidadaos.",;
            "   Fuzil, metralhadora, bomba = PROIBIDOS.",;
            "   So militar em ativo (OpenMilitary).",;
            "",;
            "4. Armas !-letais sao PREFERIDAS.",;
            "   Spray de pimenta, taser. Neutralizam sem matar.",;
            "   P1: ate agressor tem direito a vida (exceto em legítima defesa).",;
            "",;
            "5. Comercio de armas PROIBIDO.",;
            "   OpenProhibitedBusiness. Sem loja. Sem trafico.",;
            "   FabLab fabrica para cidadao autorizado pela assembleia.",;
            "",;
            "6. Legitima defesa && DIREITO (P2).",;
            "   Se atacado, voce se defende. Com o que tiver.",;
            "   Mas forca proporcional. Excesso && crime (OpenPenalRevision).",;
            "",;
            "7. Forca proporcional.",;
            "   Agressor desarmado + voce com arma = desproporcional.",;
            "   OpenMartialArts resolve desarmado.",;
            "   Arma so se agressor armado E em risco de morte.",;
            "",;
            "8. Posse ! && direito absoluto.",;
            "   E PRIVILEGIO condicional.",;
            "   Pode perder por: violencia, psicologica, risco a comunidade.",;
            "   Renovacao anual. Reavaliacao continua.",;
        ];
    stats(self) {
        return {;
            "itens_catalogados": .length(self.catalog),;
            "proibidos": soma(1 para w em self.catalog.values();
                            if w.category == ItemCategory.PROHIBITED),;
            "armas_fogo_restritas": soma(1 para w em self.catalog.values();
                                        if w.category == ItemCategory.RESTRICTED_FIREARM),;
            "portes_ativos": .length(self.permits),;
            "portes_revogados": self.revoked,;
            "politica": "OpenMartialArts primeiro. Arma ultimo recurso.",;
        };
// ============================================================================
// 5. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = WeaponsEngine();
    console.log("=" * 80);
    console.log("  OPENWEAPONSPOLICY -- PORTE DE ARMAS DA REPUBLICA");
    console.log("  OpenMartialArts primeiro. Arma de fogo ultimo recurso.");
    console.log("=" * 80);
    // === 1. ASSEMBLEIA ===
    console.log("\n\n  === 1. ASSEMBLEIA CONSTITUINTE ===\n");
    result = run_weapons_assembly(10000);
    console.log("  PERGUNTA: {result['question']}\n");
    console.log("  RESULTADO DA VOTACAO:");
    para cada (option, count) em result["votes"].items(): {
        pct = count / result["total"] * 100;
        bar = "#" * inteiro(pct / 2);
        console.log("    {option:<30} {count:>5} ({pct:.0f}%) {bar}");
    console.log("\n  DECISAO VENCEDORA: {result['winner']} ({result['pct']})");
    console.log("\n  DECISOES DA ASSEMBLEIA:");
    para cada (key, val) em result["decisions"].items(): {
        console.log("    {key:<25} {val}");
    // === 2. CATALOGO DE ITENS ===
    console.log("\n\n  === 2. CATALOGO DE ITENS ({len(engine.catalog)}) ===\n");
    current_cat = null;
    for (const w of engine.catalog.values()) {
        if (w.category != current_cat) {
            current_cat = w.category;
            console.log("\n  --- {w.category.value[0].upper()} ---");
        req_count = .length(w.requirements);
        location = w.concealed_carry ? w.home_only ? "DOMICILIO" : ("OCULTO" : "N/A");
        console.log("  {w.name:<30} max:{w.max_per_person:>2} reqs:{req_count} local:{location}");
    // === 3. PEDIDOS DE PORTE ===
    console.log("\n\n  === 3. PEDIDOS DE PORTE ===\n");
    // Caso 1: spray de pimenta (facil)
    console.log("\n  --- Caso 1: Spray de Pimenta ---");
    r = engine.request_permit("C-001", "Maria", "WPN-DEF1",;
                            psych_eval_passed = true);
    console.log("  {r['message']}");
    // Caso 2: pistola sem requisitos (negado)
    console.log("\n  --- Caso 2: Pistola SEM requisitos ---");
    r = engine.request_permit("C-002", "Joao", "WPN-GUN1",;
                            has_martial_arts_belt = "",;
                            psych_eval_passed = false);
    console.log("  {r['message']}");
    if ("failed_requirements" in r) {
        console.log("  Faltam: {', '.join(r['failed_requirements'])}");
    // Caso 3: pistola com TODOS requisitos (aprovado)
    console.log("\n  --- Caso 3: Pistola COM todos requisitos ---");
    r = engine.request_permit("C-003", "Pedro", "WPN-GUN1",;
                            has_martial_arts_belt = "preto",;
                            psych_eval_passed = true,;
                            has_violent_record = false,;
                            assembly_approval = true,;
                            community_endorsement = true,;
                            safe_storage = true,;
                            proficiency = true);
    console.log("  {r['message']}");
    if ("conditions" in r) {
        for (const c of r["conditions"]) {
            console.log("    -> {c}");
    // Caso 4: fuzil (proibido)
    console.log("\n  --- Caso 4: Fuzil de Assalto ---");
    r = engine.request_permit("C-004", "Carlos", "WPN-WAR1");
    console.log("  {r['message']}");
    // === 4. REVOGACAO ===
    console.log("\n\n  === 4. REVOGACAO DE PORTE ===\n");
    r = engine.revoke_permit("C-003", "Ameaça a companheira. Psicologica reprovou.");
    console.log("  {r['message']}");
    // === 5. FILOSOFIA ===
    console.log("\n\n  === 5. FILOSOFIA COMPLETA ===\n");
    for (const line of engine.philosophy()) {
        console.log("  {line}");
    // === 6. STATS ===
    console.log("\n\n  === 6. ESTATISTICAS ===\n");
    s = engine.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<30} {v}");
    console.log("\n{'='*80}");
    console.log("  OpenWeaponsPolicy: {s['proibidos']} proibidos, ";
        "{s['armas_fogo_restritas']} restritas. ";
        "{s['portes_ativos']} portes ativos.");
    console.log("  {s['politica']}");
    console.log("{'='*80}");
