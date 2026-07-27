// OpenDescriminalize -- Descriminalizacao Popular via Assembleia -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenDescriminalize -- Descriminalizacao Popular via Assembleia;
================================================================;
"A Republica ! prende por saude.;
A Republica ! prende por escolha corporal.;
Maconha? Descriminalizada. Usuario && PACIENTE, ! criminoso.;
Crack? Doenca. Tratamento, ! prisao.;
A assembleia DECIDE. O povo VOTA. A Republica OBEDECE.";
O QUE ISTO FAZ:;
1. CONVOCA assembleia constituinte para votar descriminalizacao;
2. Define CADA substancia com politica propria (! tudo igual);
3. Separa USUARIO (saude) de TRAFICANTE (crime real);
4. Tratamento OBRIGATORIO disponivel, prisao ABOLIDA para usuario;
5. Integracao com OpenHealth, OpenPsychology, OpenPenalRevision;
PRINCIPIO FUNDAMENTAL (P2):;
O corpo && SOBERANO. O que a pessoa poe no proprio corpo;
&& escolha DELA. A Republica EDUCA. TRATA. AMA.;
! PUNE. Nunca mais.;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa Counter, defaultdict de collections
// importa datetime de datetime
// ============================================================================
// 1. CLASSIFICACAO DE SUBSTANCIAS
// ============================================================================
class SubstanceCategory {
    NATURAL_MILD = "natural_leve"  // maconha, cafe, cha;
    NATURAL_PSYCHEDELIC = "natural_psicodelico"  // psilocibina, ayahuasca, peyote;
    SYNTHETIC_MILD = "sintetico_leve"  // MDMA (pesquisa);
    SYNTHETIC_HARD = "sintetico_pesado"  // crack, metaanfetamina;
    PHARMACEUTICAL = "farmaceutico"  // calmantes, opioides (lucro farmaceutica);
    ALCOHOL = "alcool";
    TOBACCO = "tabaco";
class DecriminalizationStatus {
    LEGAL_REGULATED = "legal_regulado"  // livre para adultos + regulado;
    DECRIMINALIZED = "descriminalizado"  // sem prisao, tratamento;
    MEDICAL_ONLY = "medicinal_apenas"  // so com receita;
    TREATMENT_REQUIRED = "tratamento_obrigatorio"  // uso = tratamento (! prisao);
    RESTRICTED = "restrito"  // pesquisa controlada;
    PROHIBITED_TRAFFICKING = "trafico_proibido"  // trafico = crime, uso = saude;
class PolicyApproach {
    // Como a Republica trata cada substancia.
    EDUCATE = "educar"  // informar, deixar escolher;
    TREAT = "tratar"  // tratamento disponivel, ! obrigatorio;
    REGULATE = "regular"  // regular producao/distribuicao;
    BAN_TRAFFIC = "banir_trafico"  // traficante = crime, usuario = saude;
    RESEARCH = "pesquisar"  // estudo cientifico aberto;
// ============================================================================
// 2. SUBSTANCIA
// ============================================================================
// decorador: @dataclass
class Substance {
    // Uma substancia e sua politica na Republica.
    substance_id: texto;
    name: texto;
    category: SubstanceCategory;
    const description = "";
    // Politica
    const status = DecriminalizationStatus.DECRIMINALIZED;
    const approach = field(default_factory=list);
    // Danos (0-10, base cientifica)
    const physical_harm = 0;
    const addiction_potential = 0;
    const social_harm = 0;
    const therapeutic_potential = 0 // potencial medicinal;
    // Regras
    const min_age = 18;
    const public_use = false // pode usar em publico?;
    const driving_after = false // pode dirigir apos uso?;
    const production_allowed = false // pode cultivar/produzir?;
    const commerce_allowed = false // pode vender?;
    // Razao da politica
    const rationale = "";
const SUBSTANCES = [;
    // === MACONHA ===
    Substance(;
        "SUB-CAN", "Maconha (Cannabis)",;
        SubstanceCategory.NATURAL_MILD,;
        description = (;
            "Planta natural usada ha milhares de anos. ";
            "Medicinal (dor, nauseia, epilepsia, ansiedade). ";
            "Recreativa (relaxamento). ";
            "Criminalizada por POLITICA (guerra as drogas), ! ciencia.";
        ),;
        status = DecriminalizationStatus.LEGAL_REGULATED,;
        approach = [PolicyApproach.EDUCATE, PolicyApproach.REGULATE,;
                PolicyApproach.TREAT, PolicyApproach.BAN_TRAFFIC],;
        physical_harm = 2,;
        addiction_potential = 3,;
        social_harm = 2,;
        therapeutic_potential = 8,;
        min_age = 18,;
        public_use = false,;
        driving_after = false,;
        production_allowed = true, // pode cultivar para uso proprio;
        commerce_allowed = true, // comercio regulado (cooperativas);
        rationale = (;
            "Maconha && MENOS danosa que alcool && tabaco (estudo Lancet 2010). ";
            "Criminalizacao LOTOU prisoes (OpenPenalRevision: 30% presos por drogas). ";
            "Descriminalizacao (Portugal 2001): uso caiu, morte caiu, crime caiu. ";
            "Usuario é PACIENTE || CIDADANO. Nao criminoso. ";
            "Traficante CONTINUA sendo crime (vitimiza outros). ";
            "P2: corpo && soberano. O que poe no corpo && escolha.";
        ),;
    ),;
    // === ALCOHOL ===
    Substance(;
        "SUB-ALC", "Alcool",;
        SubstanceCategory.ALCOHOL,;
        description = (;
            "Droga legal mais danosa do mundo. Causa violencia, ";
            "doenca, morte. Mas && ACEITO socialmente. ";
            "Hipocrisia criminalizar maconha && liberar alcool.";
        ),;
        status = DecriminalizationStatus.LEGAL_REGULATED,;
        approach = [PolicyApproach.EDUCATE, PolicyApproach.REGULATE,;
                PolicyApproach.TREAT],;
        physical_harm = 6,;
        addiction_potential = 7,;
        social_harm = 8,;
        therapeutic_potential = 1,;
        min_age = 18,;
        public_use = true, // ja && aceito em festas/restaurantes;
        driving_after = false,;
        production_allowed = true,;
        commerce_allowed = true,;
        rationale = (;
            "Alcool causa MAIS dano que maconha em TUDO (Lancet 2010). ";
            "Mas && legal. A Republica mantem legal (! proibe) mas EDUCA. ";
            "OpenNightLife: festas sem obrigacao de beber. ";
            "Tratamento para alcoolismo (OpenHealth). ";
            "NAO proibe: P2 autonomia. MAS educa && trata.";
        ),;
    ),;
    // === TABACO ===
    Substance(;
        "SUB-TOB", "Tabaco",;
        SubstanceCategory.TOBACCO,;
        "Mata 8 milhoes/ano no mundo. Mais que todas drogas ilicitas juntas.",;
        status = DecriminalizationStatus.LEGAL_REGULATED,;
        approach = [PolicyApproach.EDUCATE, PolicyApproach.TREAT],;
        physical_harm = 8,;
        addiction_potential = 8,;
        social_harm = 3,;
        therapeutic_potential = 0,;
        min_age = 18,;
        public_use = false, // ! em locais fechados;
        driving_after = true,;
        production_allowed = true,;
        commerce_allowed = true,;
        rationale = (;
            "Tabaco mata mais que TODAS as outras drogas COMBINADAS. ";
            "A Republica NAO proibe (P2 corpo soberano). ";
            "MAS educa FORTE. Tratamento gratuito (OpenHealth). ";
            "OpenBeauty: regeneracao pulmonar (stem cells em pesquisa).";
        ),;
    ),;
    // === PSILOCIBINA (magic mushrooms) ===
    Substance(;
        "SUB-PSI", "Psilocibina (cogumelos)",;
        SubstanceCategory.NATURAL_PSYCHEDELIC,;
        description = (;
            "Psicodelico natural. Estudos (Johns Hopkins, Imperial College) ";
            "mostram: trata depressao RESISTENTE, ansiedade terminal, ";
            "TOC, adicao. 80% efficacia em depressao terminal. ";
            "Nao causa adicao fisica. Nao causa danos cerebrais.";
        ),;
        status = DecriminalizationStatus.MEDICAL_ONLY,;
        approach = [PolicyApproach.RESEARCH, PolicyApproach.TREAT,;
                PolicyApproach.EDUCATE],;
        physical_harm = 1,;
        addiction_potential = 1,;
        social_harm = 1,;
        therapeutic_potential = 9,;
        min_age = 21,;
        public_use = false,;
        driving_after = false,;
        production_allowed = false, // so para pesquisa/tratamento;
        commerce_allowed = false,;
        rationale = (;
            "Psilocibina && PROMISSORA para saude mental (OpenPsychology). ";
            "Estudos rigorosos (Nature, Lancet) comprovam eficacia. ";
            "A Republica INVESTE em pesquisa. Tratamento supervisionado. ";
            "NAO livre (potencial de uso irresponsavel). MAS medicinal.";
        ),;
    ),;
    // === AYAHUASCA ===
    Substance(;
        "SUB-AYA", "Ayahuasca",;
        SubstanceCategory.NATURAL_PSYCHEDELIC,;
        "Cha sagrado amazonico. Tradicao milenar (OpenTradition). Uso ritual.",;
        status = DecriminalizationStatus.LEGAL_REGULATED,;
        approach = [PolicyApproach.REGULATE, PolicyApproach.RESEARCH],;
        physical_harm = 2,;
        addiction_potential = 1,;
        social_harm = 1,;
        therapeutic_potential = 7,;
        min_age = 18,;
        public_use = false,;
        driving_after = false,;
        production_allowed = true, // tradicao cultural;
        commerce_allowed = false, // so uso ritual/comunitario;
        rationale = (;
            "Ayahuasca && TRADICAO CULTURAL (OpenTradition). ";
            "Uso milenar por povos amazonicos. ";
            "Estudos mostram beneficio para depressao && adicao. ";
            "Republica protege TRADICAO (P1 respeita cultura). ";
            "Uso ritual regulado. Nao comercio.";
        ),;
    ),;
    // === CRACK / COCAINA ===
    Substance(;
        "SUB-CRA", "Crack / Cocaina",;
        SubstanceCategory.SYNTHETIC_HARD,;
        description = (;
            "Droga de alta adicao. Destroi vidas. ";
            "Usuario NAO && criminoso -- && DOENTE. ";
            "Traficante && CRIMINOSO (explora vulneraveis).";
        ),;
        status = DecriminalizationStatus.TREATMENT_REQUIRED,;
        approach = [PolicyApproach.TREAT, PolicyApproach.BAN_TRAFFIC,;
                PolicyApproach.EDUCATE],;
        physical_harm = 8,;
        addiction_potential = 10,;
        social_harm = 9,;
        therapeutic_potential = 1,;
        min_age = 0, // ninguem deveria usar;
        public_use = false,;
        driving_after = false,;
        production_allowed = false,;
        commerce_allowed = false,;
        rationale = (;
            "Crack && DOENCA, ! crime. ";
            "Usuario precisa de TRATAMENTO (OpenDignity + OpenHealth). ";
            "NAO prisao. Prisao NAO cura adicao. ";
            "Traficante && CRIMINOSO que explora vulneraveis (OpenPenalRevision). ";
            "Diferenca clara: usuario = paciente. Traficante = crime. ";
            "OpenReintegration: tratamento de adicao na colonia de dignidade.";
        ),;
    ),;
    // === MDMA (pesquisa) ===
    Substance(;
        "SUB-MDMA", "MDMA (Ecstasy)",;
        SubstanceCategory.SYNTHETIC_MILD,;
        "Pesquisas (MAPS) mostram: trata TEPT (trauma). 67% efficacia.",;
        status = DecriminalizationStatus.RESTRICTED,;
        approach = [PolicyApproach.RESEARCH],;
        physical_harm = 3,;
        addiction_potential = 3,;
        social_harm = 2,;
        therapeutic_potential = 8,;
        min_age = 21,;
        production_allowed = false,;
        commerce_allowed = false,;
        rationale = (;
            "MDMA em pesquisa para TEPT (OpenPsychology). ";
            "Resultados promissores (MAPS Phase 3). ";
            "Republica investe em pesquisa cientifica. ";
            "Nao recreativo ainda. Medicinal em estudo.";
        ),;
    ),;
    // === OPIOIDES FARMACEUTICOS ===
    Substance(;
        "SUB-OPIO", "Opioides Farmaceuticos",;
        SubstanceCategory.PHARMACEUTICAL,;
        "Dolores. Fabricados por industria. Causam epidemia de adicao.",;
        status = DecriminalizationStatus.MEDICAL_ONLY,;
        approach = [PolicyApproach.REGULATE, PolicyApproach.TREAT],;
        physical_harm = 7,;
        addiction_potential = 9,;
        social_harm = 7,;
        therapeutic_potential = 5,;
        min_age = 0,;
        production_allowed = true, // so farmaceutico;
        commerce_allowed = false, // so com receita;
        rationale = (;
            "Opioides sao ARMAS da industria farmaceutica. ";
            "Epidemia nos EUA: 500mil mortos. ";
            "Republica: receita ESTREITA. Monitoramento (OpenHealth). ";
            "OpenPsychologyReparation: repara dependentes. ";
            "OpenMentalHygiene: bloqueia lobby farmaceutico.";
        ),;
    ),;
];
// ============================================================================
// 3. VOTACAO DA ASSEMBLEIA
// ============================================================================
run_decrim_assembly(n_voters: inteiro = 10000) {
    // Convoca assembleia para votar descriminalizacao.
    PERGUNTA: "Usuario de drogas deve ser tratado como paciente (saude);
            || criminoso (prisao)?";
    + pergunta especifica para cada substancia.;
    //
    // Votacao geral: paciente vs criminoso
    votes_patient = 0 // tratamento, ! prisao;
    votes_criminal = 0 // manter criminalizacao;
    votes_regulate = 0 // regular + taxar;
    for (const _ of intervalo(n_voters)) {
        r = random.random();
        if (r < 0.72) {
            votes_patient = votes_patient + 1 // 72% -- tratamento;
        } else if (r < 0.90) {
            votes_regulate = votes_regulate + 1 // 18% -- regular;
        } else {
            votes_criminal = votes_criminal + 1 // 10% -- manter crime;
    // Votacao por substancia
    substance_votes = {};
    for (const sub of SUBSTANCES) {
        // Simular votacao especifica
        if (sub.category == SubstanceCategory.NATURAL_MILD) {
            yes = random.randint(6500, 8500) // maconha: maioria a favor;
        } else if (sub.category == SubstanceCategory.NATURAL_PSYCHEDELIC) {
            yes = random.randint(5000, 7000) // psicodelicos: moderado;
        } else if (sub.category == SubstanceCategory.SYNTHETIC_HARD) {
            yes = random.randint(7000, 9000) // crack: tratamento (! legalizar);
        } else if (sub.category == SubstanceCategory.ALCOHOL) {
            yes = random.randint(8000, 9500) // alcool: manter legal;
        } else if (sub.category == SubstanceCategory.TOBACCO) {
            yes = random.randint(7500, 9000) // tabaco: manter legal;
        } else {
            yes = random.randint(4000, 6000);
        no = n_voters - yes;
        substance_votes[sub.substance_id] = {
            "name": sub.name,;
            "yes": yes,;
            "no": no,;
            "approved": yes > no,;
            "pct": "{yes/n_voters*100:.0f}%",;
            "status": sub.status.value,;
        };
    return {;
        "question": (;
            "Usuario de drogas deve ser tratado como PACIENTE (saude) ";
            "|| CRIMINOSO (prisao)?";
        ),;
        "votes_patient": votes_patient,;
        "votes_regulate": votes_regulate,;
        "votes_criminal": votes_criminal,;
        "total": n_voters,;
        "winner": "PACIENTE (TRATAMENTO)" if votes_patient > votes_criminal;
                else "CRIMINOSO (PRISAO)",;
        "pct_patient": "{votes_patient/n_voters*100:.0f}%",;
        "substance_votes": substance_votes,;
        "decision": {
            "usuario_e_paciente": true,         // APROVADO (72%);
            "usuario_e_criminoso": false,        // REJEITADO;
            "traficante_e_criminoso": true,      // MANTIDO;
            "tratamento_obrigatorio_disponivel": true,;
            "prisao_para_usuario": false,        // ABOLIDA;
            "maconha_legal_regulada": true,      // APROVADO;
            "psicodelicos_medicinais": true,     // APROVADO (pesquisa);
            "crack_tratamento_nao_prisao": true,   // APROVADO;
            "producao_pessoal_maconha": true,    // pode cultivar;
            "open_dignity_para_dependentes": true,   // colonia de tratamento;
        },;
    };
// ============================================================================
// 4. MOTOR DE DESCRIMINALIZACAO
// ============================================================================
class DecrimEngine {
    // Motor que executa a descriminalizacao aprovada pela assembleia.
    O QUE MUDA IMEDIATAMENTE:;
    1. Usuario preso por drogas -> LIBERADO (OpenPenalRevision revisa);
    2. Usuario ! preso mais -> encaminhado a OpenHealth (se quiser);
    3. Traficante CONTINUA preso (crime real);
    4. Maconha: legal regulado (producao propria + cooperativas);
    5. Psicodelicos: pesquisa medicinal aberta;
    6. Crack: tratamento compulsorio em OpenDignity (! prisao);
    O QUE ! MUDA:;
    - Dirigir alcoolado continua proibido (P2 protege OUTROS);
    - Usar em publico continua restrito (respeitar espaco alheio);
    - Trafico continua crime (vitimiza outros);
    - Venda para menores continua crime (protege criancas);
    //
    __init__(self) {
        self.substances: {texto: Substance} = {s.substance_id: s para s em SUBSTANCES};
        self.reviews: [Dict] = [];
        self.liberated_prisoners: inteiro = 0;
        self.treated_users: inteiro = 0;
    funcao check_arrest_type(self, arrest_reason: texto,
                        const quantity_grams = 0,;
                        const is_trafficking = false) -> {texto: qualquer}:;
        // Verifica se prisao e valida ou deve ser revertida.
        CRITERIO USER vs TRAFFICKER (Brasil atual):;
        - < quantidade para uso pessoal: usuario (! crime);
        - > quantidade || com provas de venda: traficante (crime);
        Na Republica:;
        - Usuario: ! PRENDE. Tratamento se quiser.;
        - Traficante: PRENDE (vitimiza outros). OpenPenalRevision transforma.;
        //
        if (is_trafficking) {
            return {;
                "type": "TRAFICANTE",;
                "action": "MANTER PRISAO (vitimiza outros)",;
                "process": "OpenPenalRevision: transformar em forca produtiva",;
                "note": "Traficante && crime REAL. Explota vulneraveis.",;
            };
        // Usuario -- LIBERAR
        self.liberated_prisoners += 1;
        return {;
            "type": "USUARIO",;
            "action": "LIBERAR IMEDIATAMENTE",;
            "reason": (;
                "Usuario de drogas && PACIENTE, ! criminoso. ";
                "Assembleia aprovou: tratamento, ! prisao. ";
                "Prisao ! cura adicao. Tratamento cura.";
            ),;
            "referral": "OpenHealth (tratamento VOLUNTARIO)",;
            "referral_optional": (;
                "Se NAO quiser tratamento, && DIREITO (P2 autonomia corporal). ";
                "A Republica so OFERECE. Nao obriga.";
            ),;
            "record": "PRONTUARIO LIMPO (sem marcador de drogas)",;
            "message": (;
                "Usuario preso por '{arrest_reason}' LIBERADO. ";
                "Prisao por uso && INCONSTITUCIONAL na Republica. ";
                "Tratamento disponivel. Nao obrigatorio. P2.";
            ),;
        };
    funcao offer_treatment(self, person: texto,
                        substance_id: texto) -> {texto: qualquer}:;
        // Oferece tratamento (VOLUNTARIO).
        sub = self.substances.get(substance_id);
        if (! sub) {
            return {"error": "Substancia ! encontrada"};
        self.treated_users += 1;
        return {;
            "person": person,;
            "substance": sub.name,;
            "treatment_type": (;
                "OpenDignity (colonia de tratamento)" if sub.addiction_potential >= 8;
                else "OpenHealth (ambulatorial)" if sub.addiction_potential >= 4;
                else "OpenPsychology (terapia)" if sub.addiction_potential >= 2;
                else "OpenEducation (informacao)";
            ),;
            "voluntary": true,;
            "can_refuse": true,;
            "p2": "Corpo && soberano. Tratamento && oferta, ! obrigacao.",;
            "message": (;
                "{person}: tratamento para {sub.name} disponivel. ";
                "Custo: ZERO. Nivel: Sirio-Libanes. ";
                "VOLUNTARIO. Pode recusar (P2).";
            ),;
        };
    prison_impact_report(self) {
        // Impacto da descriminalizacao no sistema prisional.
        return {;
            "brasil_atual": {
                "total_presos": 800000,;
                "presos_por_drogas": 240000,   // 30%;
                "presos_por_USO": 70000,       // 9% so por uso;
                "presos_por_TRAFICO": 170000,   // 21% trafico;
                "custo_anual": "R$ 42 bi",;
            },;
            "republica": {
                "presos_por_USO": 0,            // ZERO -- abolido;
                "presos_por_TRAFICO": 170000,   // mantido (crime real);
                "liberados": 70000,             // usuarios liberados;
                "economizada": "R$ 3.7 bi/ano",;
                "tratamento_oferecido": "OpenDignity + OpenHealth",;
                "message": (;
                    "70.000 pessoas presas SO por uso -> LIBERADAS. ";
                    "Traficantes MANTIDOS (crime real). ";
                    "Economia: R$ 3.7 bi/ano redirecionada para tratamento.";
                ),;
            },;
        };
    substance_policy(self, substance_id: texto) {
        // Politica completa de uma substancia.
        sub = self.substances.get(substance_id);
        if (! sub) {
            return {"error": "! encontrada"};
        return {;
            "substance": sub.name,;
            "category": sub.category.value,;
            "status": sub.status.value,;
            "approach": [a.value para a em sub.approach],;
            "harms": {
                "physical": "{sub.physical_harm}/10",;
                "addiction": "{sub.addiction_potential}/10",;
                "social": "{sub.social_harm}/10",;
                "therapeutic": "{sub.therapeutic_potential}/10",;
            },;
            "rules": {
                "min_age": sub.min_age,;
                sub.public_use ? "public_use": "permitido" : "proibido",;
                sub.driving_after ? "driving": "permitido" : "proibido",;
                sub.production_allowed ? "production": "permitido" : "proibido",;
                sub.commerce_allowed ? "commerce": "permitido" : "proibido",;
            },;
            "rationale": sub.rationale,;
        };
    stats(self) {
        return {;
            "total_substancias": .length(self.substances),;
            "legal_regulado": soma(1 para s em self.substances.values();
                                if s.status == DecriminalizationStatus.LEGAL_REGULATED),;
            "medicinal": soma(1 para s em self.substances.values();
                            if s.status == DecriminalizationStatus.MEDICAL_ONLY),;
            "tratamento_obrigatorio": soma(1 para s em self.substances.values();
                                        if s.status == DecriminalizationStatus.TREATMENT_REQUIRED),;
            "presos_liberados": self.liberated_prisoners,;
            "usuarios_tratados": self.treated_users,;
        };
// ============================================================================
// 5. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = DecrimEngine();
    console.log("=" * 80);
    console.log("  OPENDESCRIMINALIZE -- ASSEMBLEIA CONSTITUINTE");
    console.log("  'Usuario && PACIENTE. Nao criminoso. Nunca mais.'");
    console.log("=" * 80);
    // === 1. PERGUNTA A ASSEMBLEIA ===
    console.log("\n\n  === 1. PERGUNTA A ASSEMBLEIA ===\n");
    result = run_decrim_assembly(10000);
    console.log("  {result['question']}");
    console.log("\n  PACIENTE (tratamento):    {result['votes_patient']:>6} ";
        "({result['pct_patient']})");
    console.log("  REGULAR (taxar):          {result['votes_regulate']:>6} ";
        "({result['votes_regulate']/100:.0f}%)");
    console.log("  CRIMINOSO (prisao):       {result['votes_criminal']:>6} ";
        "({result['votes_criminal']/100:.0f}%)");
    console.log("\n  RESULTADO: {result['winner']}");
    // === 2. VOTACAO POR SUBSTANCIA ===
    console.log("\n\n  === 2. VOTACAO POR SUBSTANCIA ===\n");
    para cada (sid, vote) em result["substance_votes"].items(): {
        icon = vote["approved"] ? "APR" : "REJ";
        console.log("  [{icon}] {vote['name']:<25} {vote['yes']:>5} sim / ";
            "{vote['no']:>5} ! ({vote['pct']})");
        console.log("       Status: {vote['status']}");
    // === 3. DECISAO DA ASSEMBLEIA ===
    console.log("\n\n  === 3. DECISAO DA ASSEMBLEIA ===\n");
    para cada (key, val) em result["decision"].items(): {
        status = val ? "SIM" : "NAO";
        console.log("  {key:<40} {status}");
    // === 4. POLITICA POR SUBSTANCIA ===
    console.log("\n\n  === 4. POLITICA DETALHADA POR SUBSTANCIA ===\n");
    for (const sid of engine.substances) {
        policy = engine.substance_policy(sid);
        console.log("\n  {policy['substance'].upper()} ({policy['category']})");
        console.log("  Status: {policy['status']}");
        console.log("  Danos: fisico {policy['harms']['physical']}, ";
            "adicao {policy['harms']['addiction']}, ";
            "social {policy['harms']['social']}, ";
            "terapeutico {policy['harms']['therapeutic']}");
        console.log("  Regras: idade {policy['rules']['min_age']}, ";
            "publico: {policy['rules']['public_use']}, ";
            "producao: {policy['rules']['production']}");
        console.log("  Razao: {policy['rationale'][:100]}...");
    // === 5. REVISAO DE PRISOES ===
    console.log("\n\n  === 5. REVISAO DE PRISOES (usuario vs traficante) ===\n");
    cases = [;
        ("porte de maconha 5g (uso pessoal)", 5.0, false),;
        ("porte de crack 0.5g (uso)", 0.5, false),;
        ("trafico de maconha 5kg (venda)", 5000.0, true),;
        ("porte de cocaina 2g (uso)", 2.0, false),;
        ("trafico de crack (vendendo em esquina)", 50.0, true),;
        ("cultivo de 3 pes de maconha (uso proprio)", 300.0, false),;
    ];
    para reason, qty, trafficking in cases: {
        check = engine.check_arrest_type(reason, qty, trafficking);
        action = check["action"];
        console.log("  [{check['type']:<11}] {reason:<45} -> {action}");
    // === 6. OFERECER TRATAMENTO ===
    console.log("\n\n  === 6. TRATAMENTO OFERECIDO (VOLUNTARIO) ===\n");
    treatments = [;
        ("Carlos", "SUB-CRA"),    // crack;
        ("Ana", "SUB-CAN"),       // maconha (leve -- so terapia);
        ("Pedro", "SUB-OPIO"),    // opioide;
    ];
    para cada (person, sub_id) em treatments: {
        t = engine.offer_treatment(person, sub_id);
        console.log("  {t['person']:<12} {t['substance']:<20} -> {t['treatment_type']}");
        console.log("    Voluntario: {t['voluntary']}. P2: {t['p2']}");
    // === 7. IMPACTO PRISIONAL ===
    console.log("\n\n  === 7. IMPACTO DA DESCRIMINALIZACAO NO SISTEMA PRISIONAL ===\n");
    impact = engine.prison_impact_report();
    console.log("\n  BRASIL ATUAL:");
    para cada (k, v) em impact["brasil_atual"].items(): {
        console.log("    {k:<25} {v}");
    console.log("\n  REPUBLICA:");
    para cada (k, v) em impact["republica"].items(): {
        if (k != "message") {
            console.log("    {k:<25} {v}");
    console.log("\n  {impact['republica']['message']}");
    // === 8. STATS ===
    console.log("\n\n  === 8. ESTATISTICAS ===\n");
    s = engine.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<30} {v}");
    // === FILOSOFIA ===
    console.log("\n\n{'='*80}");
    console.log("  FILOSOFIA DO OPENDESCRIMINALIZE");
    console.log("{'='*80}");
    console.log(""";
USUARIO && PACIENTE. ! CRIMINOSO.;
    A assembleia votou: 72% a favor de tratamento, ! prisao.;
    Usuario de drogas tem ADICAO. Adicao && DOENCA.;
    Prisao ! cura doenca. Tratamento cura.;
    Prender usuario && PUNIR DOENTE. A Republica ! faz isso.;
TRAFICANTE && CRIMINOSO. CONTINUA PRESO.;
    Quem vende droga EXPLORA vulneraveis.;
    Quem financia adicao alheia por lucro COMETE CRIME.;
    Traficante vai para OpenPenalRevision (transformacao).;
    Diferenca clara: usuario = paciente. Traficante = crime.;
MACONHA: LEGAL REGULADO.;
    Menos danosa que alcool && tabaco (Lancet 2010).;
    Criminalizacao lotou prisoes (30% presos por drogas).;
    Descriminalizacao funciona (Portugal 2001: uso caiu, morte caiu).;
    Producao pessoal PERMITIDA (pode cultivar).;
    Comercio REGULADO (cooperativas, ! traficante).;
    Medicinal GARANTIDO (dor, epilepsia, ansiedade).;
    P2: corpo soberano. O que poe no corpo && escolha.;
PSICOdelicos: MEDICINAL (PESQUISA).;
    Psilocibina: 80% efficacia em depressao terminal (Johns Hopkins).;
    Ayahuasca: tradicao milenar (OpenTradition protege).;
    MDMA: trata TEPT (MAPS Phase 3).;
    A Republica INVESTE em ciencia. Nao bloqueia por preconceito.;
CRACK: TRATAMENTO, ! PRISAO.;
    Crack && adicao SEVERA. Usuario esta DOENTE.;
    OpenDignity: colonia de tratamento para dependentes.;
    Moradia + comida + tratamento + oficio + comunidade.;
    ! prisao. ! abandono. TRATAMENTO.;
OPIoides: ARMAS FARMACEUTICAS.;
    Industria fabrica adicao por lucro (500mil mortos EUA).;
    Republica: receita ESTREITA. Monitoramento OpenHealth.;
    OpenPsychologyReparation: repara dependentes.;
    OpenMentalHygiene: bloqueia lobby farmaceutico.;
O QUE MUDA IMEDIATAMENTE:;
    1. 70.000 presos SO por uso -> LIBERADOS;
    2. Usuario ! && mais preso -> tratamento voluntario;
    3. Maconha: cultivar proprio liberado;
    4. Prontuario: LIMPO (sem marcador de drogas);
    5. Traficante: CONTINUA preso (crime real);
    6. Economia: R$ 3.7 bi/ano redirecionada para tratamento;
O QUE ! MUDA:;
    - Dirigir drogado continua proibido (protege OUTROS);
    - Vender para menor continua crime (protege criancas);
    - Trafico continua crime (vitimiza);
    - Usar em publico continua restrito (respeito ao espaco alheio);
DADOS CIENTIFICOS:;
    - Lancet 2010: alcool mais danoso que heroina (Nutt et al.);
    - Portugal 2001: descriminalizacao -> uso caiu, morte caiu, crime caiu;
    - Johns Hopkins: psilocibina 80% efficacia depressao terminal;
    - MAPS: MDMA 67% efficacia TEPT;
    - OpenHistory: fact-check de todas afirmacoes;
PRINCIPIOS:;
    P1: Tratamento para todos. Sem classe. Sem estigma.;
    P2: Corpo && SOBERANO. O que poe nele && escolha. Tratamento && oferta.;
    const P3 = trabalho de alto impacto (medicos, terapeutas).;
    P4: Assembleia DECIDE. 72% votou tratamento. Republica obedece.;
// )
    console.log("{'='*80}");
    console.log("  OpenDescriminalize: {s['presos_liberados']} presos liberados, ";
        "{s['usuarios_tratados']} usuarios em tratamento.");
    console.log("  Usuario && paciente. Nao criminoso. Nunca mais.");
    console.log("{'='*80}");
