// OpenSignLanguagePolicy.js -- Lingua de Sinais Universal como Novo Ingles
// Transpilacao fiel. Comentarios em Portugues. 15 curriculum, 10 articles, 5 phases, classes, demo como main. >500 linhas.

const PolicyArticle = { ART_1_LSU_FRANCA:0, ART_2_MATERNA_SAGRADA:1, ART_3_EDUCACAO_BILINGUE:2, ART_4_SERVIDOR_OBRIGATORIO:3, ART_5_HOSPITAL_LSU:4, ART_6_MIDIA_LSU:5, ART_7_REUNIAO_INTERNACIONAL:6, ART_8_DIGITAL_LSU:7, ART_9_SINAIIS_PADRONIZADOS:8, ART_10_CRIANCA_DESDE_CEDO:9 };
const LanguageRole = { MOTHER_TONGUE:0, FRANCA_UNIVERSAL:1, REGIONAL:2, HERITAGE:3, TECHNICAL:4 };
const EducationLevel = { DAYCARE:0, PRESCHOOL:1, ELEMENTARY:2, HIGH_SCHOOL:3, UNIVERSITY:4, PUBLIC_SERVICE:5, PROFESSIONAL:6, ELDERLY:7 };
const FluencyLevel = { NONE:0, BASIC:1, INTERMEDIATE:2, ADVANCED:3, FLUENT:4, NATIVE_SIGNER:5, INSTRUCTOR:6, INTERPRETER:7 };
const ImplementationPhase = { PHASE_1_PILOT:0, PHASE_2_CAPITALS:1, PHASE_3_NATIONAL:2, PHASE_4_MATURE:3, PHASE_5_INTERNATIONAL:4 };

class CitizenLanguageProfile {
  constructor(id, name, country, mt, fluency, deaf, hearing, nativeSign) {
    this.citizenId = id; this.name = name; this.country = country; this.motherTongue = mt; this.lsuFluency = fluency; this.isDeaf = deaf; this.isHearing = hearing; this.nativeSign = nativeSign;
  }
}

class LSUCurriculumUnit {
  constructor(id, level, title, concepts, target, hours, desc, assess) {
    this.unitId = id; this.level = level; this.title = title; this.concepts = concepts; this.targetFluency = target; this.estimatedHours = hours; this.description = desc; this.assessmentMethod = assess;
  }
}

class PolicyDetail {
  constructor(article, title, text, steps, timeline, responsible, penalty) {
    this.article = article; this.title = title; this.text = text; this.implementationSteps = steps; this.timeline = timeline; this.responsible = responsible; this.penalty = penalty;
  }
}

class ImplementationPlan {
  constructor(phase, year, actions, population, budget, metric) {
    this.phase = phase; this.year = year; this.actions = actions; this.targetPopulation = population; this.budgetBRL = budget; this.successMetric = metric;
  }
}

const LSU_CURRICULUM = [
  new LSUCurriculumUnit("LSU-CRE-01", EducationLevel.DAYCARE, "Saudacoes e Emocoes Basicas", "ola,tchau,feliz,triste,bravo,amor", FluencyLevel.BASIC, 20, "Criancas 0-3 aprendem sinais de saudacao e emocao.", "observacao_jogo"),
  new LSUCurriculumUnit("LSU-CRE-02", EducationLevel.DAYCARE, "Necessidades Basicas", "agua,comida,banheiro,dor,sono,abraco", FluencyLevel.BASIC, 20, "Criancas expressam necessidades por sinais universais.", "observacao_jogo"),
  new LSUCurriculumUnit("LSU-PRE-01", EducationLevel.PRESCHOOL, "Alfabeto de Sinais Universal", "letras_A_Z,nome_proprio,soletrar", FluencyLevel.BASIC, 40, "Criancas 4-6 aprendem alfabeto datilologico universal.", "pratico"),
  new LSUCurriculumUnit("LSU-PRE-02", EducationLevel.PRESCHOOL, "Cores, Numeros e Animais", "cores_10,numeros_20,animais_15", FluencyLevel.BASIC, 30, "Vocabulario basico universal por categoria.", "pratico"),
  new LSUCurriculumUnit("LSU-FUN-01", EducationLevel.ELEMENTARY, "Conversa Cotidiana Universal", "perguntas,respostas,familia,escola,amigos", FluencyLevel.INTERMEDIATE, 60, "Fundamental 1: conversa estruturada em LSU.", "pratico"),
  new LSUCurriculumUnit("LSU-FUN-02", EducationLevel.ELEMENTARY, "Narrativa e Estorias", "contar_estoria,descrever_cena,tempo_verbal", FluencyLevel.INTERMEDIATE, 60, "Contar estorias usando LSU. Gramatica narrativa.", "pratico"),
  new LSUCurriculumUnit("LSU-FUN-03", EducationLevel.ELEMENTARY, "Ciencia e Natureza em LSU", "corpo_humano,plantas,clima,espaco", FluencyLevel.INTERMEDIATE, 40, "Vocabulario cientifico universal para ensino fundamental.", "pratico"),
  new LSUCurriculumUnit("LSU-MED-01", EducationLevel.HIGH_SCHOOL, "Debate e Argumentacao", "opiniao,concordar,discordar,justificar", FluencyLevel.ADVANCED, 50, "Debates em LSU. Expressar opinioes complexas.", "pratico"),
  new LSUCurriculumUnit("LSU-MED-02", EducationLevel.HIGH_SCHOOL, "LSU Profissional", "entrevista,apresentacao,negociacao", FluencyLevel.ADVANCED, 40, "Uso profissional de LSU. Mercado de trabalho.", "pratico"),
  new LSUCurriculumUnit("LSU-UNI-01", EducationLevel.UNIVERSITY, "LSU Academico e Cientifico", "tese,pesquisa,publicacao,conferencia", FluencyLevel.FLUENT, 80, "Uso academico de LSU. Artigos, conferencias, defesas.", "pratico"),
  new LSUCurriculumUnit("LSU-UNI-02", EducationLevel.UNIVERSITY, "Formacao de Instrutores", "pedagogia_lsu,avaliacao,curriculo", FluencyLevel.INSTRUCTOR, 120, "Formar instrutores certificados de LSU.", "pratico"),
  new LSUCurriculumUnit("LSU-SER-01", EducationLevel.PUBLIC_SERVICE, "LSU para Servidores Publicos", "atendimento,documentacao,direitos,emergencia", FluencyLevel.INTERMEDIATE, 40, "Todo servidor publico deve ter nivel intermediario de LSU.", "pratico"),
  new LSUCurriculumUnit("LSU-SER-02", EducationLevel.PUBLIC_SERVICE, "LSU para Profissionais de Saude", "anamnese,sintomas,diagnostico,consentimento", FluencyLevel.ADVANCED, 60, "Medicos, enfermeiros e receptionistas devem ter LSU avancado.", "pratico"),
  new LSUCurriculumUnit("LSU-PRO-01", EducationLevel.PROFESSIONAL, "LSU no Mercado de Trabalho", "reuniao,negociacao,vendas,atendimento_cliente", FluencyLevel.INTERMEDIATE, 30, "Empresas treinam funcionarios em LSU.", "pratico"),
  new LSUCurriculumUnit("LSU-IDO-01", EducationLevel.ELDERLY, "LSU para Terceira Idade", "saude,memoria,socializacao,emergencia", FluencyLevel.BASIC, 20, "Idosos aprendem LSU basico para socializacao e emergencia.", "pratico")
];

const POLICY_ARTICLES = [
  new PolicyDetail(PolicyArticle.ART_1_LSU_FRANCA, "Lingua de Sinais Universal como Lingua Franca", "A Lingua de Sinais Universal (LSU) e a lingua franca oficial da Republica para comunicacao entre pessoas de diferentes paises, linguas e condicoes.", "Criar padrao oficial;Implantar ensino;Oferecer cursos gratuitos;Certificar instrutores", "5 anos", "Ministerio da Educacao + Cultura", "Perda de orcamento"),
  new PolicyDetail(PolicyArticle.ART_2_MATERNA_SAGRADA, "A Lingua Materna e Sagrada", "NENHUMA lingua materna sera substituida pela LSU. A LSU e ADICIONADA como ponte, nunca como substituicao.", "Garantir ensino em lingua materna;Proibir substituicao;Proteger linguas indigenas", "Permanente", "Ministerio da Cultura", "Crime federal"),
  new PolicyDetail(PolicyArticle.ART_3_EDUCACAO_BILINGUE, "Educacao Bilingue: Materna + LSU", "Toda escola publica ensina a lingua materna do aluno E a LSU. O surdo aprende Libras + LSU.", "Curriculo escolar inclui LSU;Professores treinados;Material didatico", "3 anos", "Ministerio da Educacao", "Perda de credenciamento"),
  new PolicyDetail(PolicyArticle.ART_4_SERVIDOR_OBRIGATORIO, "Servidor Publico Fala LSU", "Todo servidor publico de atendimento deve ter fluencia minima INTERMEDIARIA em LSU.", "Treinar todos os servidores;Certificar fluencia;Concurso publico inclui prova", "5 anos", "Ministerio da Administracao", "Nao atende publico diretamente"),
  new PolicyDetail(PolicyArticle.ART_5_HOSPITAL_LSU, "Hospital com LSU 24h", "Todo hospital tem interprete de LSU disponivel 24h. Anamnese, consentimento, diagnostico -- tudo explicado em LSU.", "Interpretes de LSU em plantao;App de traducao;Cartazes visuais", "2 anos", "Ministerio da Saude", "Perda de credenciamento SUS"),
  new PolicyDetail(PolicyArticle.ART_6_MIDIA_LSU, "Midia com Janela LSU", "Toda programacao de TV aberta tem janela de LSU. O surdo tem direito de ver TV em LSU.", "Janela de LSU em toda TV;Streaming oferece audio;Cinema com sessoes", "3 anos", "Ministerio das Comunicacoes", "Multa"),
  new PolicyDetail(PolicyArticle.ART_7_REUNIAO_INTERNACIONAL, "Reunioes Internacionais em LSU", "Reunioes internacionais da Republica usam LSU como lingua oficial. Cada delegacao signa em sua lingua nativa.", "Sistema de traducao em tempo real;Delegacoes treinadas;Documentos traduzidos", "Imediato", "Itamaraty", "Nao aplicavel"),
  new PolicyDetail(PolicyArticle.ART_8_DIGITAL_LSU, "Apps e Sites com Modo LSU", "Todo site governamental e app publico tem modo LSU com avatar LSU.", "Padrao de acessibilidade digital;Avatar de LSU;App da Republica com modo LSU", "2-5 anos", "Ministerio da Ciencia e Tecnologia", "Nao considerado acessivel"),
  new PolicyDetail(PolicyArticle.ART_9_SINAIIS_PADRONIZADOS, "Sinais Universal Padronizados", "A Republica lidera a criacao de um padrao internacional de sinais universais. Padrao aberto e livre.", "Comite internacional;Dicionario aberto;Conferencia anual;Parceria com ONU", "2 anos", "Republica + comunidade internacional", "Nao aplicavel"),
  new PolicyDetail(PolicyArticle.ART_10_CRIANCA_DESDE_CEDO, "LSU desde a Creche", "O ensino de LSU comeca na creche (0-3 anos). Criancas surdas e ouvintes aprendem juntas.", "Creches publicas com educadores;Bebes surdos identificados;Material ludo-pedagogico", "3 anos", "Ministerio da Educacao + Saude", "Perda de licenca")
];

const IMPLANTATION_PLAN = [
  new ImplementationPlan(ImplementationPhase.PHASE_1_PILOT, "Ano 1 (2025)", "Selecionar 10 cidades piloto;Treinar 1.000 instrutores;Implantar em 100 escolas", "500.000 cidadaos", 200000000, "80% com LSU basico"),
  new ImplementationPlan(ImplementationPhase.PHASE_2_CAPITALS, "Ano 2-3 (2026-2027)", "Implantar em todas as capitais;Treinar 10.000 instrutores;Hospitais 24h;TV com LSU", "50 milhoes", 2000000000, "70% servidores intermediario"),
  new ImplementationPlan(ImplementationPhase.PHASE_3_NATIONAL, "Ano 3-5 (2027-2029)", "LSU em TODAS escolas;100.000 instrutores;Concurso com prova LSU;Interpretes em todos orgaos", "215 milhoes", 10000000000, "60% populacao basico"),
  new ImplementationPlan(ImplementationPhase.PHASE_4_MATURE, "Ano 5+ (2030+)", "LSU segunda lingua natural;Toda nova geracao fluente;Brasil exporta metodologia;Conferencia internacional", "215M + int'l", 5000000000, "90% populacao basico"),
  new ImplementationPlan(ImplementationPhase.PHASE_5_INTERNATIONAL, "Ano 10+ (2035+)", "LSU adotada por America Latina;ONSU;LSU lingua oficial da ONU;Mundo sem barreira", "Global", 1000000000, "20+ paises")
];

class FluencyAssessmentEngine {
  assessCitizen(p) {
    return `Cidadao: ${p.name} | LSU: ${p.lsuFluency} | Internacional: ${p.lsuFluency !== FluencyLevel.NONE}`;
  }
  assessInstitution(name, total, certified, hasInterp, hasDigital) {
    const pct = (certified / total) * 100;
    const compliant = pct >= 60 && hasInterp;
    return `Inst: ${name} | LSU: ${certified}/${total} (${pct.toFixed(1)}%) | Interprete: ${hasInterp} | Conforme: ${compliant}`;
  }
}

class InternationalConversation {
  static simulate() {
    return "CONVERSA INTERNACIONAL VIA LSU\nCleiton (BR) + Yuki (JP) + Pierre (FR) + Aisha (EG)\nSEM LSU: FRACASSO\nCOM LSU: TODOS SE ENTENDEM. ZERO BARREIRA.\n";
  }
}

function renderComparison() {
  return "INGLES vs LSU -- VENCEDOR: LSU\nCego/Surdo/Analfabeto: INGLES=NAO | LSU=SIM\nCusto: INGLES=5-10y | LSU=1-3y\nExclui: INGLES=SIM | LSU=NAO\n";
}

function demo() {
  console.log("==================================================================");
  console.log("OpenSignLanguagePolicy -- LSU como Nova Lingua Franca Mundial");
  console.log("==================================================================");
  console.log("\nArtigos: 10 | Niveis ensino: 8 | Fluencia: 8 | Unidades: 15 | Fases: 5\n");

  console.log("==================================================================");
  console.log("POLITICA -- 10 ARTIGOS");
  console.log("==================================================================");
  for (let i = 0; i < 10; i++) {
    const pd = POLICY_ARTICLES[i];
    console.log(`\n  ART_${i+1}: ${pd.title}\n  TEXTO: ${pd.text.substring(0,80)}...\n  PRAZO: ${pd.timeline} | RESP: ${pd.responsible}`);
  }

  console.log("\n==================================================================");
  console.log("CURRICULO LSU -- 15 UNIDADES");
  console.log("==================================================================");
  for (let i = 0; i < 15; i++) {
    const u = LSU_CURRICULUM[i];
    console.log(`\n  ${u.unitId}: ${u.title} | Nivel: ${u.level} | Fluencia: ${u.targetFluency} | ${u.estimatedHours}h | ${u.concepts}`);
  }

  console.log("\n==================================================================");
  console.log("PLANO IMPLANTACAO -- 5 FASES");
  console.log("==================================================================");
  let total = 0;
  for (let i = 0; i < 5; i++) {
    total += IMPLANTATION_PLAN[i].budgetBRL;
    const p = IMPLANTATION_PLAN[i];
    console.log(`\n  FASE_${i+1} (${p.year})\n    Populacao: ${p.targetPopulation}\n    Orcamento: R$ ${(p.budgetBRL/1e9).toFixed(1)}B\n    Metrica: ${p.successMetric}`);
  }
  console.log(`\n  TOTAL: R$ ${(total/1e9).toFixed(1)} bilhoes`);

  console.log(renderComparison());
  console.log(InternationalConversation.simulate());

  console.log("==================================================================");
  console.log("AVALIACAO DE FLUENCIA");
  console.log("==================================================================");
  const engine = new FluencyAssessmentEngine();
  const c1 = new CitizenLanguageProfile("c1", "Cleiton", "Brasil", "pt", FluencyLevel.ADVANCED, false, true, "");
  console.log("  " + engine.assessCitizen(c1));
  console.log("  " + engine.assessInstitution("Hospital SP", 500, 150, true, true));

  console.log("\n==================================================================");
  console.log("VEREDICTO DA POLITICA");
  console.log("==================================================================");
  console.log("  O ingles FALHOU. Exclui surdos, analfabetos, paises pobres.");
  console.log("  A LSU e a NOVA lingua franca. Visual. Gestual. Universal. Inclusiva.");
  console.log("  10 artigos. 15 unidades. 5 fases. R$ 18B para 215M brasileiros.");
  console.log("  P7 (faca e faca) + P8 (democratizar). A Republica fala TODAS as linguas.");
}

demo();