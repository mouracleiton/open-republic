// OpenRepublic -- Emenda Constitucional: Autonomia Corporal -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
OpenRepublic -- Emenda Constitucional: Autonomia Corporal;
============================================================;
"O corpo && a fronteira ultima da liberdade.;
Tudo antes do corpo pode ser negociado coletivamente.;
O corpo, nunca.";
PRINCIPIO CONSTITUCIONAL NUMERO 2:;
"A Republica JAMAS pode solicitar, exigir, || incentivar com;
pressao que uma pessoa fecunde, gere, || ! gere vida.;
O corpo de cada cidadao && DELA. Inegociavelmente.;
Reproducao && escolha pessoal, nunca politica de Estado.";
Esta emenda formaliza a AUTONOMIA CORPORAL como direito;
absoluto && inegociavel da Republica.;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Set de typing
// importa Enum de enum
#[derive(Debug, Clone, PartialEq)]
enum BodilyRight {
    // Direitos corporais absolutos.
    REPRODUCTION = "reproducao"  // decidir ter || ! ter filhos;
    CONTRACEPTION = "anticoncepcional"  // acesso a prevencao;
    ABORTION = "aborto"  // aborto seguro;
    MEDICAL = "medico"  // recusar tratamento;
    ORGAN_DONATION = "orgaos"  // doacao voluntaria;
    GENETIC = "genetico"  // ! ser geneticamente modificado;
    MUTILATION = "mutilacao"  // zero mutilacao forçada;
    CONSENT = "consentimento"  // consentimento continuo;
    SEXUALITY = "sexualidade"  // autonomia sexual;
    SUBSTANCES = "substanca"  // o que coloca no corpo;
    DEATH = "morte"  // direito a morte digna (eutanasia);
    IDENTITY = "identidade"  // genero, nome, aparencia;
#[derive(Debug, Clone, PartialEq)]
enum StateAction {
    // O que o Estado PODE e NAO PODE fazer em relacao ao corpo.
    // PERMITIDO
    GUARANTEE_ACCESS = "garantir_acesso";
    PROTECT_FROM_HARM = "proteger_dano";
    EDUCATE = "educar";
    OFFER_SERVICES = "oferecer_servicos";
    // PROIBIDO
    DEMAND_REPRODUCTION = "exigir_reproducao";
    FORBID_REPRODUCTION = "proibir_reproducao";
    FORCE_TREATMENT = "forcar_tratamento";
    SELECT_WHO_REPRODUCES = "selecionar_reproducao";
    GENETIC_MODIFY = "modificar_genetica";
    FORCE_MUTILATION = "forcar_mutilacao";
    OWN_BODY = "possuir_corpo";
// decorador: @dataclass
#[derive(Debug, Clone)]
struct ConstitutionalRight {
    // Um direito constitucional de autonomia corporal.
    right: BodilyRight;
    what_it_means: texto;
    what_state_must_do: texto;
    what_state_cannot_do: texto;
    historical_violation: texto // exemplo real de quando Estado violou;
let RIGHTS: [ConstitutionalRight] = [;
    ConstitutionalRight(;
        BodilyRight.REPRODUCTION,;
        "Cada pessoa decide livremente se quer || ! ter filhos.",;
        "Garantir que quem QUER ter filhos tenha: creche, comida, saude, ";
        "educacao, apoio comunitario (OpenChildhood). Garantir que quem ";
        "NAO QUER tenha: anticoncepcional gratuito, aborto seguro, ";
        "laqueadura voluntaria.",;
        "Exigir que alguem gere filho ('dever reprodutivo'). ";
        "Incentivar com pressao. Selecionar quem deve reproduzir. ";
        "Limitar quem pode reproduzir. Usar corpo como instrumento ";
        "de politica populacional.",;
        "Ceaucescu (Romania 1966): Decreto 770 obrigou mulheres a ter ";
        "filhos. Policia menstrual. Mortalidade materna triplicou. ";
        "9.000 mulheres morreram em abortos clandestinos."),;
    ConstitutionalRight(;
        BodilyRight.CONTRACEPTION,;
        "Todo cidadao tem direito a metodos anticoncepcionais gratuitos.",;
        "Oferecer TODOS os metodos: pilula, DIU, implante, preservativo, ";
        "laqueadura voluntaria, vasectomia voluntaria. Sem cobranca. ";
        "Sem julgamento. Sem exigencia de autorizacao do parceiro.",;
        "Negar anticoncepcional. Exigir autorizacao de marido/pai. ";
        "Julgar escolha reprodutiva. Descontinuar metodo por motivo ";
        "religioso || politico.",;
        "Brasil: ate 1996, mulher casada precisava autorizacao do ";
        "marido para laqueadura. Lei 9.263/96 acabou com exigencia."),;
    ConstitutionalRight(;
        BodilyRight.ABORTION,;
        "Aborto seguro && direito de saude. Nao && crime.",;
        "Oferecer aborto seguro em qualquer OpenHealth clinica. ";
        "Sem julgamento. Sem policia. Apos aborto: apoio psicologico ";
        "(OpenPsychology) se desejado. Sem registro publico.",;
        "Criminalizar aborto. Forcar maternidade. Exigir justificativa. ";
        "Negar aborto em caso de estupro. Negar aborto em risco de vida. ";
        "Exigir espera obrigatória. Exigir ultrassom obrigatório.",;
        "El Salvador: aborto proibido em TODOS os casos. Mulheres ";
        "presas por aborto espontaneo (perderam o bebe). 200+ mulheres ";
        "presas por 'homicidio' apos miscarriage."),;
    ConstitutionalRight(;
        BodilyRight.CONSENT,;
        "Consentimento && continuo, explicito, entusiasta && revogavel.",;
        "Ensinar consentimento desde a infancia (OpenEducation). ";
        "Registrar consentimento em interacoes intimas (OpenRelationship). ";
        "Permitir revogacao a qualquer momento, sem burocracia.",;
        "Assumir consentimento. Aceitar silencio como sim. Aceitar ";
        "'sim' passado como 'sim' presente. Punir revogacao.",;
        "Estupros em casamento eram legais no Brasil ate 2006 ";
        "(Lei Maria da Penha). Marido ! podia estuprar esposa na lei."),;
    ConstitutionalRight(;
        BodilyRight.MUTILATION,;
        "Nenhum corpo pode ser mutilado sem consentimento informado.",;
        "Proibir mutilacao genital feminina. Proibir circuncisao ";
        "infantil masculina sem necessidade medica. Proibir ";
        "cirurgia intersexo em bebes.",;
        "Permitir mutilacao cultural/religiosa em criancas. ";
        "Operar bebes intersexo sem consentimento. Forcar cirurgia ";
        "estetica. Negar cirurgia de afirmacao de genero.",;
        "Mutilacao Genital Feminina: 200 milhoes de mulheres vivas ";
        "foram mutiladas. Praticada em 30 paises. Sem consentimento."),;
    ConstitutionalRight(;
        BodilyRight.GENETIC,;
        "Ninguem pode ser geneticamente modificado sem consentimento.",;
        "Proibir edicao genetica germinativa (CRISPR em embrioes). ";
        "Proibir testes geneticos sem consentimento. Proibir ";
        "discriminacao por perfil genetico.",;
        "Permitir eugenia genetica (design de bebes). Modificar ";
        "embrioes sem consentimento. Selecionar embrioes por sexo. ";
        "Discriminar por predisposicao genetica.",;
        "He Jiankui (China 2018): modificou geneticamente 2 bebes ";
        "CRISPR sem consentimento informado. Condenado. Mas precedente ";
        "criado."),;
    ConstitutionalRight(;
        BodilyRight.ORGAN_DONATION,;
        "Doacao de orgaos && voluntaria. Nunca obrigatoria.",;
        "Oferecer registro de doador voluntario. Priorizar quem ";
        "necessita (OpenHealth matching). Nao comercializar orgaos ";
        "(orgaos ! sao mercadoria).",;
        "Tornar doacao obrigatoria (presumed consent problemático). ";
        "Comercializar orgaos. Pegar orgaos sem consentimento familiar. ";
        "Priorizar rico sobre pobre.",;
        "China: colheita de orgaos de presos politicos/prisioneiros ";
        "(Falun Gong, uigures). Investigado pela ONU."),;
    ConstitutionalRight(;
        BodilyRight.MEDICAL,;
        "Cada pessoa decide o que entra no seu corpo.",;
        "Oferecer tratamento gratuito. Informar riscos && beneficios. ";
        "Respeitar recusa (Testemunha de Jeova && sangue, etc). ";
        "EXCECAO: criancas -- vida > crenca dos pais (OpenFaith).",;
        "Forcar tratamento em adulto consciente. Negar tratamento ";
        "por motivo religioso/politico. Forcar medicação psiquiatrica ";
        "(exceto risco imediato de vida a outrem).",;
        "EUA (1927): Buck v. Bell. Suprema Corte permitiu esterilizacao ";
        "forçada de 'imbecis'. 60.000 americanos esterilizados sem ";
        "consentimento. Decisao nunca foi oficialmente revertida."),;
    ConstitutionalRight(;
        BodilyRight.SUBSTANCES,;
        "Cada pessoa decide o que coloca no proprio corpo.",;
        "Tratar dependencia como DOENCA (OpenHealth), ! crime. ";
        "Oferecer tratamento gratuito. Reducao de danos. ";
        "Estudar substancias com potencial medico (OpenMedicine).",;
        "Encarcerar por uso pessoal. Forcar abstinencia. Negar ";
        "tratamento por dependencia. Criminalizar doenca.",;
        "Guerra as Drogas (EUA, 1971-presente): milhoes de pessoas ";
        "(predominantemente negras && hispanicas) encarceradas por ";
        "posse de substancias. Racismo institucional documentado."),;
    ConstitutionalRight(;
        BodilyRight.DEATH,;
        "Direito a morte digna (eutanasia/assistencia ao suicidio).",;
        "Oferecer cuidados paliativos de excelencia. Permitir ";
        "eutanasia/assistencia voluntaria em doenca terminal com ";
        "consentimento informado && avaliacao psicologica.",;
        "Negar morte digna (obrigar sofrimento). Forcar eutanasia ";
        "(inverso: matar sem consentimento). Aplicar em doencas ";
        "trataveis. Aplicar em criancas sem consentimento.",;
        "Nazismo (Aktion T4): 300.000 pessoas com deficiencia ";
        "assassinadas sem consentimento. 'Eutanasia' usada como ";
        "cobertura para assassinato. Crime contra humanidade."),;
    ConstitutionalRight(;
        BodilyRight.IDENTITY,;
        "Cada pessoa define propria identidade (genero, nome, aparencia).",;
        "Reconhecer identidade de genero autodeclarada. Oferecer ";
        "cuidados de afirmacao (hormonio, cirurgia) a quem desejar. ";
        "Usar pronome && nome escolhido. Zero discriminacao.",;
        "Forcar genero binario. Negar tratamento de afirmacao. ";
        "Patologizar identidade. Exigir diagnose psiquiatrica para ";
        "reconhecimento. Operar bebes intersexo para 'normalizar'.",;
        "Brasil: ate 2018, pessoas trans precisavam de processo ";
        "judicial + laudo psiquiatrico + cirurgia para retificar ";
        "nome/genero. STF decidiu: retificacao administrativa, ";
        "autodeclarada, sem cirurgia."),;
];
// ============================================================================
// Historical Violations Database
// ============================================================================
#[derive(Debug, Clone)]
struct HistoricalViolation {
    // Base de dados de violacoes historicas de autonomia corporal.
    PARA QUE NUNCA ESQUECAMOS.;
    Para que nunca se repitam.;
    //
    VIOLATIONS = [;
        {"perpetrator": "Nazismo (Aktion T4)", "country": "Alemanha",;
        "era": "1939-1945", "victims": "300.000+ pessoas com deficiência",;
        "violation": "Assassinato disfarcado de eutanásia",;
        "lesson": "Estado nunca deve decidir quem 'merece viver'"},;
        {"perpetrator": "Ceaucescu (Decreto 770)", "country": "Romania",;
        "era": "1966-1989", "victims": "9.000+ mulheres mortas",;
        "violation": "Obrigação reprodutiva forçada",;
        "lesson": "Corpo da mulher não é instrumento demográfico"},;
        {"perpetrator": "Política do Filho Único", "country": "China",;
        "era": "1979-2015", "victims": "Milhões de abortos forçados",;
        "violation": "Proibição de reprodução",;
        "lesson": "Estado não pode limitar reprodução"},;
        {"perpetrator": "Buck v. Bell", "country": "EUA",;
        "era": "1927-1970s", "victims": "60.000+ esterilizados",;
        "violation": "Esterilização forçada de 'imbećis'",;
        "lesson": "Eugenia é crime contra humanidade"},;
        {"perpetrator": "Mutilação Genital Feminina", "country": "30+ países",;
        "era": "até hoje", "victims": "200+ milhões de mulheres",;
        "violation": "Mutilação sem consentimento",;
        "lesson": "Tradição não justifica violência"},;
        {"perpetrator": "Colheita de Órgãos", "country": "China",;
        "era": "2000-presente", "victims": "Prisioneiros políticos",;
        "violation": "Colheita de órgãos sem consentimento",;
        "lesson": "Órgãos não são mercadoria"},;
        {"perpetrator": "Guerra às Drogas", "country": "EUA + Global",;
        "era": "1971-presente", "victims": "Milhões encarcerados",;
        "violation": "Encarceramento por posse de substância",;
        "lesson": "Dependência é doença, não crime"},;
        {"perpetrator": "CRISPR Babies (He Jiankui)", "country": "China",;
        "era": "2018", "victims": "2 bebês geneticamente modificados",;
        "violation": "Edição genética germinativa sem consentimento",;
        "lesson": "Genética humana não é experimento"},;
    ];
// ============================================================================
// Main
// ============================================================================
if __name__ == "__main__" {
    println!("=" * 80);
    println!("  EMENDA CONSTITUCIONAL: AUTONOMIA CORPORAL");
    println!("  'O corpo && a fronteira ultima da liberdade.'");
    println!("=" * 80);
    // === 1. The Amendment ===
    println!(""";
PRINCIPIO CONSTITUCIONAL NUMERO 2:;
    "A Republica JAMAS pode solicitar, exigir, || incentivar com;
    pressao que uma pessoa fecunde, gere, || ! gere vida.;
    O corpo de cada cidadao && DELA. Inegociavelmente.;
    Reproducao && escolha pessoal, nunca politica de Estado.;
    Tudo antes do corpo pode ser negociado coletivamente.;
    O corpo, nunca.";
// )
    // === 2. Rights ===
    println!("\n  === 11 DIREITOS CORPORAIS ABSOLUTOS ===\n");
    for r in RIGHTS {
        println!("\n  {'='*70}");
        println!("  DIREITO: {r.right.value.upper()}");
        println!("  {'='*70}");
        println!("\n  O QUE SIGNIFICA:\n  {r.what_it_means}");
        println!("\n  A REPUBLICA DEVE:\n  {r.what_state_must_do}");
        println!("\n  A REPUBLICA NÃO PODE:\n  {r.what_state_cannot_do}");
        println!("\n  VIOLAÇÃO HISTÓRICA:\n  {r.historical_violation}");
    // === 3. Historical Violations ===
    println!("\n\n  === NUNCA ESQUECER: VIOLAÇÕES HISTÓRICAS ===\n");
    for v in HistoricalViolation.VIOLATIONS {
        println!("\n  {v['perpetrator']} ({v['country']}, {v['era']})");
        println!("    Vitimas: {v['victims']}");
        println!("    Violacao: {v['violation']}");
        println!("    Licao: {v['lesson']}");
    // === Philosophy ===
    println!("\n\n{'='*80}");
    println!("  POR QUE ISSO É CONSTITUCIONAL");
    println!("{'='*80}");
    println!(""";
A historia humana é trágica em um tema específico:;
Estados decidindo o que fazer com os corpos das pessoas.;
Toda vez que o Estado ganha poder sobre o corpo:;
- Eugenia nazista (quem merece viver);
- Ceaucescu (quem deve ter filhos);
- China (quem NÃO deve ter filhos);
- Buck v Bell (quem deve ser esterilizado);
- MGF (o que deve ser cortado);
- Colheita de órgãos (o que pode ser tirado);
- Guerra às Drogas (o que pode ser colocado);
- CRISPR babies (o que pode ser modificado);
Cada uma dessas violações começou com uma "boa justificativa":;
- "Pelo bem da pátria" (Ceaucescu);
- "Pelo bem da raça" (Nazismo);
- "Pelo controle populacional" (China);
- "Pela segurança pública" (Guerra às Drogas);
A resposta da República é simples && absoluta:;
    NÃO.;
    O corpo não é instrumento de política.;
    O corpo não é recurso demográfico.;
    O corpo não é propriedade do Estado.;
    O corpo não é estatística.;
    O corpo não é meio de produção.;
    O corpo não é mercadoria.;
    O corpo é VOCÊ.;
    && você pertence a você.;
    A República pode pedir seu trabalho.;
    A República pode pedir sua opinião.;
    A República pode pedir seu voto.;
    A República pode pedir sua contribuição.;
    Mas a República NÃO pode pedir seu corpo.;
    Nunca.;
    "O corpo é a fronteira última da liberdade.;
    Tudo antes do corpo pode ser negociado coletivamente.;
    O corpo, nunca.";
// )
