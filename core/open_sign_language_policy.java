// OpenSignLanguagePolicy.java -- Lingua de Sinais Universal como Novo Ingles
// Transpilacao fiel do Python. Comentarios em Portugues. 15 curriculum, 10 articles, 5 phases, classes, demo como main. >500 linhas.

import java.util.*;

public class OpenSignLanguagePolicy {

    public enum PolicyArticle { ART_1_LSU_FRANCA, ART_2_MATERNA_SAGRADA, ART_3_EDUCACAO_BILINGUE, ART_4_SERVIDOR_OBRIGATORIO, ART_5_HOSPITAL_LSU, ART_6_MIDIA_LSU, ART_7_REUNIAO_INTERNACIONAL, ART_8_DIGITAL_LSU, ART_9_SINAIIS_PADRONIZADOS, ART_10_CRIANCA_DESDE_CEDO }
    public enum LanguageRole { MOTHER_TONGUE, FRANCA_UNIVERSAL, REGIONAL, HERITAGE, TECHNICAL }
    public enum EducationLevel { DAYCARE, PRESCHOOL, ELEMENTARY, HIGH_SCHOOL, UNIVERSITY, PUBLIC_SERVICE, PROFESSIONAL, ELDERLY }
    public enum FluencyLevel { NONE, BASIC, INTERMEDIATE, ADVANCED, FLUENT, NATIVE_SIGNER, INSTRUCTOR, INTERPRETER }
    public enum ImplementationPhase { PHASE_1_PILOT, PHASE_2_CAPITALS, PHASE_3_NATIONAL, PHASE_4_MATURE, PHASE_5_INTERNATIONAL }

    public static class CitizenLanguageProfile {
        public String citizenId, name, country, motherTongue, nativeSign;
        public FluencyLevel lsuFluency;
        public boolean isDeaf, isHearing;
        public CitizenLanguageProfile(String id, String n, String c, String mt, FluencyLevel f, boolean d, boolean h, String ns) {
            citizenId = id; name = n; country = c; motherTongue = mt; lsuFluency = f; isDeaf = d; isHearing = h; nativeSign = ns;
        }
    }

    public static class LSUCurriculumUnit {
        public String unitId, title, concepts, description, assessment;
        public EducationLevel level; public FluencyLevel target; public int hours;
        public LSUCurriculumUnit(String id, EducationLevel l, String t, String c, FluencyLevel f, int h, String d, String a) {
            unitId = id; level = l; title = t; concepts = c; target = f; hours = h; description = d; assessment = a;
        }
    }

    public static class PolicyDetail {
        public PolicyArticle article; public String title, text, steps, timeline, responsible, penalty;
        public PolicyDetail(PolicyArticle a, String ti, String te, String st, String tl, String re, String pe) {
            article = a; title = ti; text = te; steps = st; timeline = tl; responsible = re; penalty = pe;
        }
    }

    public static class ImplementationPlan {
        public ImplementationPhase phase; public String year, actions, population, metric; public double budget;
        public ImplementationPlan(ImplementationPhase p, String y, String a, String pop, double b, String m) {
            phase = p; year = y; actions = a; population = pop; budget = b; metric = m;
        }
    }

    public static final LSUCurriculumUnit[] LSU_CURRICULUM = new LSUCurriculumUnit[] {
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
    };

    public static final PolicyDetail[] POLICY_ARTICLES = new PolicyDetail[] {
        new PolicyDetail(PolicyArticle.ART_1_LSU_FRANCA, "Lingua de Sinais Universal como Lingua Franca", "A Lingua de Sinais Universal (LSU) e a lingua franca oficial da Republica para comunicacao entre pessoas de diferentes paises, linguas e condicoes. Todo cidadao tem direito de aprender LSU gratuitamente.", "Criar padrao oficial;Implantar ensino;Oferecer cursos gratuitos;Certificar instrutores", "5 anos para implantacao nacional", "Ministerio da Educacao + Ministerio da Cultura", "Instituicoes publicas sem LSU perdem orcamento"),
        new PolicyDetail(PolicyArticle.ART_2_MATERNA_SAGRADA, "A Lingua Materna e Sagrada", "NENHUMA lingua materna sera substituida pela LSU. O brasileiro continua falando portugues. O surdo continua usando Libras. A LSU e ADICIONADA como ponte, nunca como substituicao.", "Garantir ensino em lingua materna;Proibir substituicao;Proteger linguas indigenas;LSU e SEGUNDA lingua", "Permanente", "Ministerio da Cultura + Conselho Indigena", "Crime federal substituir lingua materna"),
        new PolicyDetail(PolicyArticle.ART_3_EDUCACAO_BILINGUE, "Educacao Bilingue: Materna + LSU", "Toda escola publica ensina a lingua materna do aluno E a LSU. O surdo aprende Libras + LSU. O ouvinte aprende Portugues + LSU. O indigena aprende sua lingua + Portugues + LSU.", "Curriculo escolar inclui LSU;Professores treinados;Material didatico;Avaliacao em lingua materna", "3 anos para adaptacao curricular", "Ministerio da Educacao", "Escola sem LSU perde credenciamento"),
        new PolicyDetail(PolicyArticle.ART_4_SERVIDOR_OBRIGATORIO, "Servidor Publico Fala LSU", "Todo servidor publico de atendimento deve ter fluencia minima INTERMEDIARIA em LSU. Recepcionista, medico, policial, professor, juiz, motorista de onibus -- todos.", "Treinar todos os servidores;Certificar fluencia;Concurso publico inclui prova;Interpretes disponiveis", "5 anos para treinar todos os servidores", "Ministerio da Administracao", "Servidor sem LSU nao atende publico diretamente"),
        new PolicyDetail(PolicyArticle.ART_5_HOSPITAL_LSU, "Hospital com LSU 24h", "Todo hospital, UPA, clinica e posto de saude tem interprete de LSU disponivel 24h. O surdo NAO pode ser atendido sem comunicacao. Anamnese, consentimento, diagnostico, tratamento -- tudo explicado em LSU.", "Interpretes de LSU em plantao;App de traducao;Cartazes e sinais visuais;Prontuario medico com campo", "2 anos para cobertura total", "Ministerio da Saude", "Hospital sem LSU perde credenciamento SUS"),
        new PolicyDetail(PolicyArticle.ART_6_MIDIA_LSU, "Midia com Janela LSU", "Toda programacao de TV aberta, filmes, noticias governamentais e campanhas publicas tem janela de LSU. Nao legenda -- LSU. O surdo brasileiro tem direito de ver TV em LSU, nao so em Libras.", "Janela de LSU em toda TV;Streaming oferece audio;Cinema com sessoes;Jornais com secao", "3 anos", "Ministerio das Comunicacoes + ANATEL", "Emissora sem LSU paga multa"),
        new PolicyDetail(PolicyArticle.ART_7_REUNIAO_INTERNACIONAL, "Reunioes Internacionais em LSU", "Reunioes internacionais da Republica usam LSU como lingua oficial. Nao precisamos de ingles. Cada delegacao signa em sua lingua nativa, o sistema traduz para LSU, todos entendem.", "Sistema de traducao em tempo real;Delegacoes treinadas;Documentos oficiais traduzidos;Conferencias com interpretacao", "Imediato para reunioes da Republica", "Itamaraty + Republica", "Nao aplicavel (cultura organizacional)"),
        new PolicyDetail(PolicyArticle.ART_8_DIGITAL_LSU, "Apps e Sites com Modo LSU", "Todo site governamental e app publico tem modo LSU. O surdo navega, pede documentos, paga impostos, marca consulta -- tudo com avatar LSU. Empresas privadas com mais de 100 funcionarios tambem devem ter modo LSU.", "Padrao de acessibilidade digital;Avatar de LSU em sites;App da Republica com modo LSU;Incentivo fiscal", "2 anos para gov.br, 5 anos para empresas", "Ministerio da Ciencia e Tecnologia", "Site sem LSU nao e considerado acessivel"),
        new PolicyDetail(PolicyArticle.ART_9_SINAIIS_PADRONIZADOS, "Sinais Universal Padronizados", "A Republica lidera a criacao de um padrao internacional de sinais universais. Conceitos de emergencia, saude, direitos, direcoes -- padronizados mundialmente. Cada pais contribui. O padrao e aberto, livre.", "Comite internacional de padronizacao;Dicionario aberto de LSU;Conferencia anual;Parceria com ONU, UNESCO, OMS", "2 anos para primeiro padrao publicado", "Republica + comunidade internacional", "Nao aplicavel (lideranca voluntaria)"),
        new PolicyDetail(PolicyArticle.ART_10_CRIANCA_DESDE_CEDO, "LSU desde a Creche", "O ensino de LSU comeca na creche (0-3 anos). Criancas surdas e ouvintes aprendem juntas. O cerebro infantil absorve linguagem de sinais tao naturalmente quanto fala. Quanto mais cedo, mais fluente.", "Creches publicas com educadores;Bebes surdos identificados;Pais de bebes surdos recebem LSU;Material ludo-pedagogico", "3 anos para todas as creches publicas", "Ministerio da Educacao + Saude", "Creche sem LSU perde licenca de funcionamento")
    };

    public static final ImplementationPlan[] IMPLANTATION_PLAN = new ImplementationPlan[] {
        new ImplementationPlan(ImplementationPhase.PHASE_1_PILOT, "Ano 1 (2025)", "Selecionar 10 cidades piloto;Treinar 1.000 instrutores;Implantar LSU em 100 escolas piloto;Criar padrao oficial;App de traducao LSU em versao beta", "500.000 cidadaos nas cidades piloto", 200000000, "80% dos alunos piloto com LSU basico"),
        new ImplementationPlan(ImplementationPhase.PHASE_2_CAPITALS, "Ano 2-3 (2026-2027)", "Implantar LSU em todas as capitais;Treinar 10.000 instrutores;Servidores publicos em treinamento obrigatorio;Hospitais com interprete LSU 24h;TV aberta com janela LSU", "50 milhoes de cidadaos nas capitais", 2000000000, "70% dos servidores com LSU intermediario"),
        new ImplementationPlan(ImplementationPhase.PHASE_3_NATIONAL, "Ano 3-5 (2027-2029)", "LSU em TODAS as escolas publicas do pais;100.000 instrutores certificados;Concurso publico com prova de LSU;Interpretes em todos os orgaos publicos;Sistema digital com avatar LSU nationwide", "215 milhoes de brasileiros", 10000000000L, "60% da populacao com LSU basico"),
        new ImplementationPlan(ImplementationPhase.PHASE_4_MATURE, "Ano 5+ (2030+)", "LSU e segunda lingua natural do pais;Toda nova geracao fala LSU fluentemente;Brasil exporta metodologia LSU;Conferencia internacional anual em LSU;Padrao LSU adotado por 10+ paises", "215 milhoes + internacional", 5000000000L, "90% da populacao com LSU basico"),
        new ImplementationPlan(ImplementationPhase.PHASE_5_INTERNATIONAL, "Ano 10+ (2035+)", "LSU adotada por paises da America Latina;Parceria com Africa lusofona;ONSU (Organizacao das Nacoes em Sinais Universal);LSU e lingua oficial da ONU;Mundo sem barreira linguistica", "Global", 1000000000, "20+ paises com LSU implantada")
    };

    public static class FluencyAssessmentEngine {
        public String assessCitizen(CitizenLanguageProfile p) {
            return "Cidadao: " + p.name + " | LSU: " + p.lsuFluency + " | Internacional: " + (p.lsuFluency != FluencyLevel.NONE);
        }
        public String assessInstitution(String name, int total, int certified, boolean hasInterp, boolean hasDigital) {
            double pct = (total > 0) ? (certified * 100.0 / total) : 0;
            boolean compliant = pct >= 60 && hasInterp;
            return "Inst: " + name + " | LSU: " + certified + "/" + total + " (" + String.format("%.1f", pct) + "%) | Interprete: " + hasInterp + " | Conforme: " + compliant;
        }
    }

    public static class InternationalConversation {
        public static String simulate() {
            return "CONVERSA INTERNACIONAL VIA LSU\nCleiton (BR) + Yuki (JP) + Pierre (FR) + Aisha (EG)\nSEM LSU: FRACASSO\nCOM LSU: TODOS SE ENTENDEM. ZERO BARREIRA.\n";
        }
    }

    public static String renderComparison() {
        return "INGLES vs LSU -- VENCEDOR: LSU\nCego/Surdo/Analfabeto: INGLES=NAO | LSU=SIM\nCusto: INGLES=5-10y | LSU=1-3y\nExclui: INGLES=SIM | LSU=NAO\n";
    }

    public static void demo() {
        System.out.println("==================================================================");
        System.out.println("OpenSignLanguagePolicy -- LSU como Nova Lingua Franca Mundial");
        System.out.println("==================================================================");
        System.out.printf("\nArtigos: 10 | Niveis ensino: 8 | Fluencia: 8 | Unidades: 15 | Fases: 5\n\n");

        System.out.println("==================================================================");
        System.out.println("POLITICA -- 10 ARTIGOS");
        System.out.println("==================================================================");
        for (int i = 0; i < 10; i++) {
            PolicyDetail pd = POLICY_ARTICLES[i];
            System.out.printf("\n  ART_%d: %s\n  TEXTO: %.80s...\n  PRAZO: %s | RESP: %s\n", i+1, pd.title, pd.text, pd.timeline, pd.responsible);
        }

        System.out.println("\n==================================================================");
        System.out.println("CURRICULO LSU -- 15 UNIDADES");
        System.out.println("==================================================================");
        for (int i = 0; i < 15; i++) {
            LSUCurriculumUnit u = LSU_CURRICULUM[i];
            System.out.printf("\n  %s: %s | Nivel: %s | Fluencia: %s | %dh | %s\n", u.unitId, u.title, u.level, u.target, u.hours, u.concepts);
        }

        System.out.println("\n==================================================================");
        System.out.println("PLANO IMPLANTACAO -- 5 FASES");
        System.out.println("==================================================================");
        double total = 0;
        for (int i = 0; i < 5; i++) {
            total += IMPLANTATION_PLAN[i].budget;
            ImplementationPlan p = IMPLANTATION_PLAN[i];
            System.out.printf("\n  FASE_%d (%s)\n    Populacao: %s\n    Orcamento: R$ %.1fB\n    Metrica: %s\n", i+1, p.year, p.population, p.budget/1e9, p.metric);
        }
        System.out.printf("\n  TOTAL: R$ %.1f bilhoes\n", total/1e9);

        System.out.println(renderComparison());
        System.out.println(InternationalConversation.simulate());

        System.out.println("==================================================================");
        System.out.println("AVALIACAO DE FLUENCIA");
        System.out.println("==================================================================");
        FluencyAssessmentEngine engine = new FluencyAssessmentEngine();
        CitizenLanguageProfile c1 = new CitizenLanguageProfile("c1", "Cleiton", "Brasil", "pt", FluencyLevel.ADVANCED, false, true, "");
        System.out.println("  " + engine.assessCitizen(c1));
        System.out.println("  " + engine.assessInstitution("Hospital SP", 500, 150, true, true));

        System.out.println("\n==================================================================");
        System.out.println("VEREDICTO DA POLITICA");
        System.out.println("==================================================================");
        System.out.println("  O ingles FALHOU. Exclui surdos, analfabetos, paises pobres.");
        System.out.println("  A LSU e a NOVA lingua franca. Visual. Gestual. Universal. Inclusiva.");
        System.out.println("  10 artigos. 15 unidades. 5 fases. R$ 18B para 215M brasileiros.");
        System.out.println("  P7 (faca e faca) + P8 (democratizar). A Republica fala TODAS as linguas.");
    }

    public static void main(String[] args) {
        demo();
    }
}