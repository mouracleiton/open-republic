# OpenRepublic -- Emenda Constitucional: Autonomia Corporal

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/bodily_autonomy.py`

**Descricao:** ============================================================
"O corpo e a fronteira ultima da liberdade.
 Tudo antes do corpo pode ser negociado coletivamente.
 O corpo, nunca."
PRINCIPIO CONSTITUCIONAL NUMERO 2:
  "A Republica JAMAS pode solicitar, exigir, ou incentivar com
   pressao que uma pessoa fecunde, gere, ou nao gere vida.
   O corpo de cada cidadao e DELA. Inegociavelmente.
   Reproducao e escolha pessoal, nunca politica de Estado."
Esta emenda formaliza a AUTONOMIA CORPORAL como direito
absoluto e inegociavel da Republica.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Emenda Constitucional: Autonomia Corporal
============================================================

"O corpo e a fronteira ultima da liberdade.
 Tudo antes do corpo pode ser negociado coletivamente.
 O corpo, nunca."

PRINCIPIO CONSTITUCIONAL NUMERO 2:

  "A Republica JAMAS pode solicitar, exigir, ou incentivar com
   pressao que uma pessoa fecunde, gere, ou nao gere vida.

   O corpo de cada cidadao e DELA. Inegociavelmente.

   Reproducao e escolha pessoal, nunca politica de Estado."

Esta emenda formaliza a AUTONOMIA CORPORAL como direito
absoluto e inegociavel da Republica.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Set de typing
// importa Enum de enum


classe BodilyRight herda de Enum:
    // Direitos corporais absolutos.
    REPRODUCTION = "reproducao"  // decidir ter ou nao ter filhos
    CONTRACEPTION = "anticoncepcional"  // acesso a prevencao
    ABORTION = "aborto"  // aborto seguro
    MEDICAL = "medico"  // recusar tratamento
    ORGAN_DONATION = "orgaos"  // doacao voluntaria
    GENETIC = "genetico"  // nao ser geneticamente modificado
    MUTILATION = "mutilacao"  // zero mutilacao forçada
    CONSENT = "consentimento"  // consentimento continuo
    SEXUALITY = "sexualidade"  // autonomia sexual
    SUBSTANCES = "substanca"  // o que coloca no corpo
    DEATH = "morte"  // direito a morte digna (eutanasia)
    IDENTITY = "identidade"  // genero, nome, aparencia


classe StateAction herda de Enum:
    // O que o Estado PODE e NAO PODE fazer em relacao ao corpo.
    // PERMITIDO
    GUARANTEE_ACCESS = "garantir_acesso"
    PROTECT_FROM_HARM = "proteger_dano"
    EDUCATE = "educar"
    OFFER_SERVICES = "oferecer_servicos"
    // PROIBIDO
    DEMAND_REPRODUCTION = "exigir_reproducao"
    FORBID_REPRODUCTION = "proibir_reproducao"
    FORCE_TREATMENT = "forcar_tratamento"
    SELECT_WHO_REPRODUCES = "selecionar_reproducao"
    GENETIC_MODIFY = "modificar_genetica"
    FORCE_MUTILATION = "forcar_mutilacao"
    OWN_BODY = "possuir_corpo"


// decorador: @dataclass
classe ConstitutionalRight:
    // Um direito constitucional de autonomia corporal.
    right: BodilyRight
    what_it_means: texto
    what_state_must_do: texto
    what_state_cannot_do: texto
    historical_violation: texto // exemplo real de quando Estado violou


seja RIGHTS: [ConstitutionalRight] = [

    ConstitutionalRight(
        BodilyRight.REPRODUCTION,
        "Cada pessoa decide livremente se quer ou nao ter filhos.",
        "Garantir que quem QUER ter filhos tenha: creche, comida, saude, "
        "educacao, apoio comunitario (OpenChildhood). Garantir que quem "
        "NAO QUER tenha: anticoncepcional gratuito, aborto seguro, "
        "laqueadura voluntaria.",
        "Exigir que alguem gere filho ('dever reprodutivo'). "
        "Incentivar com pressao. Selecionar quem deve reproduzir. "
        "Limitar quem pode reproduzir. Usar corpo como instrumento "
        "de politica populacional.",
        "Ceaucescu (Romania 1966): Decreto 770 obrigou mulheres a ter "
        "filhos. Policia menstrual. Mortalidade materna triplicou. "
        "9.000 mulheres morreram em abortos clandestinos."),

    ConstitutionalRight(
        BodilyRight.CONTRACEPTION,
        "Todo cidadao tem direito a metodos anticoncepcionais gratuitos.",
        "Oferecer TODOS os metodos: pilula, DIU, implante, preservativo, "
        "laqueadura voluntaria, vasectomia voluntaria. Sem cobranca. "
        "Sem julgamento. Sem exigencia de autorizacao do parceiro.",
        "Negar anticoncepcional. Exigir autorizacao de marido/pai. "
        "Julgar escolha reprodutiva. Descontinuar metodo por motivo "
        "religioso ou politico.",
        "Brasil: ate 1996, mulher casada precisava autorizacao do "
        "marido para laqueadura. Lei 9.263/96 acabou com exigencia."),

    ConstitutionalRight(
        BodilyRight.ABORTION,
        "Aborto seguro e direito de saude. Nao e crime.",
        "Oferecer aborto seguro em qualquer OpenHealth clinica. "
        "Sem julgamento. Sem policia. Apos aborto: apoio psicologico "
        "(OpenPsychology) se desejado. Sem registro publico.",
        "Criminalizar aborto. Forcar maternidade. Exigir justificativa. "
        "Negar aborto em caso de estupro. Negar aborto em risco de vida. "
        "Exigir espera obrigatória. Exigir ultrassom obrigatório.",
        "El Salvador: aborto proibido em TODOS os casos. Mulheres "
        "presas por aborto espontaneo (perderam o bebe). 200+ mulheres "
        "presas por 'homicidio' apos miscarriage."),

    ConstitutionalRight(
        BodilyRight.CONSENT,
        "Consentimento e continuo, explicito, entusiasta e revogavel.",
        "Ensinar consentimento desde a infancia (OpenEducation). "
        "Registrar consentimento em interacoes intimas (OpenRelationship). "
        "Permitir revogacao a qualquer momento, sem burocracia.",
        "Assumir consentimento. Aceitar silencio como sim. Aceitar "
        "'sim' passado como 'sim' presente. Punir revogacao.",
        "Estupros em casamento eram legais no Brasil ate 2006 "
        "(Lei Maria da Penha). Marido nao podia estuprar esposa na lei."),

    ConstitutionalRight(
        BodilyRight.MUTILATION,
        "Nenhum corpo pode ser mutilado sem consentimento informado.",
        "Proibir mutilacao genital feminina. Proibir circuncisao "
        "infantil masculina sem necessidade medica. Proibir "
        "cirurgia intersexo em bebes.",
        "Permitir mutilacao cultural/religiosa em criancas. "
        "Operar bebes intersexo sem consentimento. Forcar cirurgia "
        "estetica. Negar cirurgia de afirmacao de genero.",
        "Mutilacao Genital Feminina: 200 milhoes de mulheres vivas "
        "foram mutiladas. Praticada em 30 paises. Sem consentimento."),

    ConstitutionalRight(
        BodilyRight.GENETIC,
        "Ninguem pode ser geneticamente modificado sem consentimento.",
        "Proibir edicao genetica germinativa (CRISPR em embrioes). "
        "Proibir testes geneticos sem consentimento. Proibir "
        "discriminacao por perfil genetico.",
        "Permitir eugenia genetica (design de bebes). Modificar "
        "embrioes sem consentimento. Selecionar embrioes por sexo. "
        "Discriminar por predisposicao genetica.",
        "He Jiankui (China 2018): modificou geneticamente 2 bebes "
        "CRISPR sem consentimento informado. Condenado. Mas precedente "
        "criado."),

    ConstitutionalRight(
        BodilyRight.ORGAN_DONATION,
        "Doacao de orgaos e voluntaria. Nunca obrigatoria.",
        "Oferecer registro de doador voluntario. Priorizar quem "
        "necessita (OpenHealth matching). Nao comercializar orgaos "
        "(orgaos nao sao mercadoria).",
        "Tornar doacao obrigatoria (presumed consent problemático). "
        "Comercializar orgaos. Pegar orgaos sem consentimento familiar. "
        "Priorizar rico sobre pobre.",
        "China: colheita de orgaos de presos politicos/prisioneiros "
        "(Falun Gong, uigures). Investigado pela ONU."),

    ConstitutionalRight(
        BodilyRight.MEDICAL,
        "Cada pessoa decide o que entra no seu corpo.",
        "Oferecer tratamento gratuito. Informar riscos e beneficios. "
        "Respeitar recusa (Testemunha de Jeova e sangue, etc). "
        "EXCECAO: criancas -- vida > crenca dos pais (OpenFaith).",
        "Forcar tratamento em adulto consciente. Negar tratamento "
        "por motivo religioso/politico. Forcar medicação psiquiatrica "
        "(exceto risco imediato de vida a outrem).",
        "EUA (1927): Buck v. Bell. Suprema Corte permitiu esterilizacao "
        "forçada de 'imbecis'. 60.000 americanos esterilizados sem "
        "consentimento. Decisao nunca foi oficialmente revertida."),

    ConstitutionalRight(
        BodilyRight.SUBSTANCES,
        "Cada pessoa decide o que coloca no proprio corpo.",
        "Tratar dependencia como DOENCA (OpenHealth), nao crime. "
        "Oferecer tratamento gratuito. Reducao de danos. "
        "Estudar substancias com potencial medico (OpenMedicine).",
        "Encarcerar por uso pessoal. Forcar abstinencia. Negar "
        "tratamento por dependencia. Criminalizar doenca.",
        "Guerra as Drogas (EUA, 1971-presente): milhoes de pessoas "
        "(predominantemente negras e hispanicas) encarceradas por "
        "posse de substancias. Racismo institucional documentado."),

    ConstitutionalRight(
        BodilyRight.DEATH,
        "Direito a morte digna (eutanasia/assistencia ao suicidio).",
        "Oferecer cuidados paliativos de excelencia. Permitir "
        "eutanasia/assistencia voluntaria em doenca terminal com "
        "consentimento informado e avaliacao psicologica.",
        "Negar morte digna (obrigar sofrimento). Forcar eutanasia "
        "(inverso: matar sem consentimento). Aplicar em doencas "
        "trataveis. Aplicar em criancas sem consentimento.",
        "Nazismo (Aktion T4): 300.000 pessoas com deficiencia "
        "assassinadas sem consentimento. 'Eutanasia' usada como "
        "cobertura para assassinato. Crime contra humanidade."),

    ConstitutionalRight(
        BodilyRight.IDENTITY,
        "Cada pessoa define propria identidade (genero, nome, aparencia).",
        "Reconhecer identidade de genero autodeclarada. Oferecer "
        "cuidados de afirmacao (hormonio, cirurgia) a quem desejar. "
        "Usar pronome e nome escolhido. Zero discriminacao.",
        "Forcar genero binario. Negar tratamento de afirmacao. "
        "Patologizar identidade. Exigir diagnose psiquiatrica para "
        "reconhecimento. Operar bebes intersexo para 'normalizar'.",
        "Brasil: ate 2018, pessoas trans precisavam de processo "
        "judicial + laudo psiquiatrico + cirurgia para retificar "
        "nome/genero. STF decidiu: retificacao administrativa, "
        "autodeclarada, sem cirurgia."),
]


// ============================================================================
// Historical Violations Database
// ============================================================================

classe HistoricalViolation:
    // Base de dados de violacoes historicas de autonomia corporal.

    PARA QUE NUNCA ESQUECAMOS.
    Para que nunca se repitam.
    // 

    VIOLATIONS = [
        {"perpetrator": "Nazismo (Aktion T4)", "country": "Alemanha",
         "era": "1939-1945", "victims": "300.000+ pessoas com deficiência",
         "violation": "Assassinato disfarcado de eutanásia",
         "lesson": "Estado nunca deve decidir quem 'merece viver'"},

        {"perpetrator": "Ceaucescu (Decreto 770)", "country": "Romania",
         "era": "1966-1989", "victims": "9.000+ mulheres mortas",
         "violation": "Obrigação reprodutiva forçada",
         "lesson": "Corpo da mulher não é instrumento demográfico"},

        {"perpetrator": "Política do Filho Único", "country": "China",
         "era": "1979-2015", "victims": "Milhões de abortos forçados",
         "violation": "Proibição de reprodução",
         "lesson": "Estado não pode limitar reprodução"},

        {"perpetrator": "Buck v. Bell", "country": "EUA",
         "era": "1927-1970s", "victims": "60.000+ esterilizados",
         "violation": "Esterilização forçada de 'imbećis'",
         "lesson": "Eugenia é crime contra humanidade"},

        {"perpetrator": "Mutilação Genital Feminina", "country": "30+ países",
         "era": "até hoje", "victims": "200+ milhões de mulheres",
         "violation": "Mutilação sem consentimento",
         "lesson": "Tradição não justifica violência"},

        {"perpetrator": "Colheita de Órgãos", "country": "China",
         "era": "2000-presente", "victims": "Prisioneiros políticos",
         "violation": "Colheita de órgãos sem consentimento",
         "lesson": "Órgãos não são mercadoria"},

        {"perpetrator": "Guerra às Drogas", "country": "EUA + Global",
         "era": "1971-presente", "victims": "Milhões encarcerados",
         "violation": "Encarceramento por posse de substância",
         "lesson": "Dependência é doença, não crime"},

        {"perpetrator": "CRISPR Babies (He Jiankui)", "country": "China",
         "era": "2018", "victims": "2 bebês geneticamente modificados",
         "violation": "Edição genética germinativa sem consentimento",
         "lesson": "Genética humana não é experimento"},
    ]


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 80)
    imprima("  EMENDA CONSTITUCIONAL: AUTONOMIA CORPORAL")
    imprima("  'O corpo e a fronteira ultima da liberdade.'")
    imprima("=" * 80)

    // === 1. The Amendment ===
    imprima("""
  PRINCIPIO CONSTITUCIONAL NUMERO 2:

    "A Republica JAMAS pode solicitar, exigir, ou incentivar com
     pressao que uma pessoa fecunde, gere, ou nao gere vida.

     O corpo de cada cidadao e DELA. Inegociavelmente.

     Reproducao e escolha pessoal, nunca politica de Estado.

     Tudo antes do corpo pode ser negociado coletivamente.
     O corpo, nunca."
// )

    // === 2. Rights ===
    imprima("\n  === 11 DIREITOS CORPORAIS ABSOLUTOS ===\n")
    para cada r em RIGHTS:
        imprima("\n  {'='*70}")
        imprima("  DIREITO: {r.right.value.upper()}")
        imprima("  {'='*70}")
        imprima("\n  O QUE SIGNIFICA:\n  {r.what_it_means}")
        imprima("\n  A REPUBLICA DEVE:\n  {r.what_state_must_do}")
        imprima("\n  A REPUBLICA NÃO PODE:\n  {r.what_state_cannot_do}")
        imprima("\n  VIOLAÇÃO HISTÓRICA:\n  {r.historical_violation}")

    // === 3. Historical Violations ===
    imprima("\n\n  === NUNCA ESQUECER: VIOLAÇÕES HISTÓRICAS ===\n")
    para cada v em HistoricalViolation.VIOLATIONS:
        imprima("\n  {v['perpetrator']} ({v['country']}, {v['era']})")
        imprima("    Vitimas: {v['victims']}")
        imprima("    Violacao: {v['violation']}")
        imprima("    Licao: {v['lesson']}")

    // === Philosophy ===
    imprima("\n\n{'='*80}")
    imprima("  POR QUE ISSO É CONSTITUCIONAL")
    imprima("{'='*80}")
    imprima("""
  A historia humana é trágica em um tema específico:
  Estados decidindo o que fazer com os corpos das pessoas.

  Toda vez que o Estado ganha poder sobre o corpo:
  - Eugenia nazista (quem merece viver)
  - Ceaucescu (quem deve ter filhos)
  - China (quem NÃO deve ter filhos)
  - Buck v Bell (quem deve ser esterilizado)
  - MGF (o que deve ser cortado)
  - Colheita de órgãos (o que pode ser tirado)
  - Guerra às Drogas (o que pode ser colocado)
  - CRISPR babies (o que pode ser modificado)

  Cada uma dessas violações começou com uma "boa justificativa":
  - "Pelo bem da pátria" (Ceaucescu)
  - "Pelo bem da raça" (Nazismo)
  - "Pelo controle populacional" (China)
  - "Pela segurança pública" (Guerra às Drogas)

  A resposta da República é simples e absoluta:

    NÃO.

    O corpo não é instrumento de política.
    O corpo não é recurso demográfico.
    O corpo não é propriedade do Estado.
    O corpo não é estatística.
    O corpo não é meio de produção.
    O corpo não é mercadoria.

    O corpo é VOCÊ.

    e você pertence a você.

    A República pode pedir seu trabalho.
    A República pode pedir sua opinião.
    A República pode pedir seu voto.
    A República pode pedir sua contribuição.

    Mas a República NÃO pode pedir seu corpo.

    Nunca.

    "O corpo é a fronteira última da liberdade.
     Tudo antes do corpo pode ser negociado coletivamente.
     O corpo, nunca."
// )

```
