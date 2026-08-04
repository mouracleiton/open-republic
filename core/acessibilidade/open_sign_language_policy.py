#!/usr/bin/env python3
"""
OpenSignLanguagePolicy -- Lingua de Sinais Universal como Novo Ingles
======================================================================
"O ingles virou a lingua franca do mundo. Por que?
Nao porque e melhor. Porque e UTIL. Todo mundo fala ingles
para se comunicar entre paises.

Mas o ingles EXCLUI. O surdo nao fala ingles. O analfabeto
nao escreve ingles. O imigrante nao entende ingles.

A Lingua de Sinais Universal (LSU) e a NOVA lingua franca.
Ela e:
- VISUAL: nao precisa ouvir
- GESTUAL: nao precisa falar
- UNIVERSAL: funciona entre paises
- INCLUSIVA: nao exclui ninguem
- NATURAL: o cerebro humano processa gestos tao bem quanto fala

POLITICA:
1. Todo cidadao da Republica aprende LSU desde a infancia
2. LSU e ensinada junto com a lingua materna (portugues + LSU)
3. Conversas internacionais usam LSU como ponte
4. Educacao e na lingua materna do aluno (portugues, Libras, LSU)
5. LSU e obrigatoria em escolas, hospitais, servicos publicos
6. Todo servidor publico fala LSU
7. Sinais de LSU sao padronizados internacionalmente

O INGLES falhou como lingua universal porque EXCLUI.
A LSU funciona porque INCLUI. Nao substitui a lingua materna.
ADICIONA uma camada universal por cima.

PRINCIPIO: Cada pessoa fala sua lingua materna para APRENDER.
Cada pessoa usa LSU para CONVERSAR com o mundo.
Nenhuma lingua e roubada. Nenhuma cultura e apagada.
A LSU e PONTE, nao substituicao.

NIVEL CONSTITUCIONAL: P7 (faca e faca) + P8 (democratizar)
Esta e a politica oficial de linguagem da Republica Aberta.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
import time


# ============================================================================
# 1. PRINCIPIOS DA POLITICA
# ============================================================================

class PolicyArticle(Enum):
    """Artigos da Politica de Linguagem Universal."""
    ART_1_LSU_FRANCA = "art_1_lsu_franca"                # LSU e lingua franca
    ART_2_MATERNA_SAGRADA = "art_2_materna_sagrada"       # Lingua materna nao se toca
    ART_3_EDUCACAO_BILINGUE = "art_3_educacao_bilingue"   # Escola ensina materna + LSU
    ART_4_SERVIDOR_OBRIGATORIO = "art_4_servidor_obrigatorio"  # Servidor publico fala LSU
    ART_5_HOSPITAL_LSU = "art_5_hospital_lsu"             # Hospital tem tradutor LSU
    ART_6_MIDIA_LSU = "art_6_midia_lsu"                   # TV/cinema tem janela LSU
    ART_7_REUNIAO_INTERNACIONAL = "art_7_reuniao_internacional"  # Reunioes usam LSU
    ART_8_DIGITAL_LSU = "art_8_digital_lsu"              # Apps/sites tem modo LSU
    ART_9_SINAIIS_PADRONIZADOS = "art_9_sinais_padronizados"  # Sinais padronizados mundial
    ART_10_CRIANCA_DESDE_CEDO = "art_10_crianca_desde_cedo"  # Ensino desde creche


class LanguageRole(Enum):
    """Papel de cada lingua na Republica."""
    MOTHER_TONGUE = "lingua_materna"      # lingua nativa do individuo
    FRANCA_UNIVERSAL = "franca_universal" # LSU para comunicacao internacional
    REGIONAL = "regional"                 # lingua regional (Libras, ASL, etc)
    HERITAGE = "lingua_heranca"           # lingua de heranca cultural
    TECHNICAL = "tecnica"                 # lingua para ciencia/tech


class EducationLevel(Enum):
    """Niveis de ensino onde LSU e aplicada."""
    DAYCARE = "creche"                    # 0-3 anos
    PRESCHOOL = "pre_escola"              # 4-6 anos
    ELEMENTARY = "fundamental"            # 7-14 anos
    HIGH_SCHOOL = "medio"                 # 15-17 anos
    UNIVERSITY = "superior"               # 18+
    PUBLIC_SERVICE = "servidor_publico"   # treinamento de servidores
    PROFESSIONAL = "profissional"         # empresas
    ELDERLY = "idoso"                     # programas para idosos


class FluencyLevel(Enum):
    """Niveis de fluencia em LSU."""
    NONE = "nenhum"                        # nao sabe
    BASIC = "basico"                       # saudacoes, emergencia
    INTERMEDIATE = "intermediario"         # conversa cotidiana
    ADVANCED = "avancado"                  # debates, trabalho
    FLUENT = "fluente"                     # nivel nativo
    NATIVE_SIGNER = "nativo_sinalizador"  # surdo que signa desde nascimento
    INSTRUCTOR = "instrutor"              # pode ensinar LSU
    INTERPRETER = "interprete"            # interprete profissional certificado


# ============================================================================
# 2. PERFIL LINGUISTICO DO CIDADAO
# ============================================================================

@dataclass
class CitizenLanguageProfile:
    """Perfil linguistico de um cidadao da Republica."""
    citizen_id: str
    name: str
    country: str = "Brasil"
    country_code: str = "BR"

    # Linguas faladas/escritas
    mother_tongue_spoken: str = "pt"       # lingua materna falada
    other_spoken: List[str] = field(default_factory=list)  # outras linguas faladas
    reading_level: str = "alfabetizado"    # alfabetizado, analfabeto, funcional

    # Linguas de sinais
    native_sign_language: str = ""         # Libras, ASL, etc (se surdo)
    lsu_fluency: FluencyLevel = FluencyLevel.NONE  # nivel de Lingua de Sinais Universal
    other_sign_languages: List[str] = field(default_factory=list)

    # Condicao
    is_deaf: bool = False
    is_hard_of_hearing: bool = False
    is_hearing: bool = True
    disability_notes: str = ""

    # Educacao LSU
    lsu_education_started: bool = False
    lsu_education_level: str = ""
    lsu_certified: bool = False

    def communication_methods(self) -> List[str]:
        """Metodos de comunicacao que esta pessoa pode usar."""
        methods = []
        if self.is_hearing and self.reading_level != "analfabeto":
            methods.append("fala")
            methods.append("escrita")
        if self.native_sign_language:
            methods.append(f"sinais_{self.native_sign_language}")
        if self.lsu_fluency != FluencyLevel.NONE:
            methods.append("lsu")
        if not methods:
            methods.append("gesto_universal")
        return methods

    def can_communicate_with(self, other: 'CitizenLanguageProfile') -> bool:
        """Verifica se pode se comunicar diretamente com outra pessoa."""
        # Mesma lingua falada
        if self.mother_tongue_spoken == other.mother_tongue_spoken and self.is_hearing and other.is_hearing:
            return True
        # Mesma lingua de sinais regional
        if self.native_sign_language and self.native_sign_language == other.native_sign_language:
            return True
        # Ambos falam LSU
        if self.lsu_fluency != FluencyLevel.NONE and other.lsu_fluency != FluencyLevel.NONE:
            return True
        return False


# ============================================================================
# 3. CURRICULO DE LSU POR IDADE
# ============================================================================

@dataclass
class LSUCurriculumUnit:
    """Unidade do curriculo de Lingua de Sinais Universal."""
    unit_id: str
    level: EducationLevel
    title: str
    concepts: List[str]                   # conceitos ensinados
    target_fluency: FluencyLevel
    estimated_hours: int
    description: str = ""
    assessment_method: str = "pratico"    # avaliacao por pratica (nao escrita)


LSU_CURRICULUM: List[LSUCurriculumUnit] = [
    LSUCurriculumUnit(
        "LSU-CRE-01", EducationLevel.DAYCARE,
        "Saudacoes e Emocoes Basicas",
        ["ola", "tchau", "feliz", "triste", "bravo", "amor"],
        FluencyLevel.BASIC, 20,
        "Criancas 0-3 aprendem sinais de saudacao e emocao. Ate surdos e ouvintes.",
        "observacao_jogo"),
    LSUCurriculumUnit(
        "LSU-CRE-02", EducationLevel.DAYCARE,
        "Necessidades Basicas",
        ["agua", "comida", "banheiro", "dor", "sono", "abraco"],
        FluencyLevel.BASIC, 20,
        "Criancas expressam necessidades por sinais universais.",
        "observacao_jogo"),
    LSUCurriculumUnit(
        "LSU-PRE-01", EducationLevel.PRESCHOOL,
        "Alfabeto de Sinais Universal",
        ["letras_A_Z", "nome_proprio", " soletrar"],
        FluencyLevel.BASIC, 40,
        "Criancas 4-6 aprendem alfabeto datilologico universal.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-PRE-02", EducationLevel.PRESCHOOL,
        "Cores, Numeros e Animais",
        ["cores_10", "numeros_20", "animais_15"],
        FluencyLevel.BASIC, 30,
        "Vocabulario basico universal por categoria.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-FUN-01", EducationLevel.ELEMENTARY,
        "Conversa Cotidiana Universal",
        ["perguntas", "respostas", "familia", "escola", "amigos"],
        FluencyLevel.INTERMEDIATE, 60,
        "Fundamental 1: conversa estruturada em LSU.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-FUN-02", EducationLevel.ELEMENTARY,
        "Narrativa e Estorias",
        ["contar_estoria", "descrever_cena", "tempo_verbal"],
        FluencyLevel.INTERMEDIATE, 60,
        "Contar estorias usando LSU. Gramatica narrativa.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-FUN-03", EducationLevel.ELEMENTARY,
        "Ciencia e Natureza em LSU",
        ["corpo_humano", "plantas", "clima", "espaco"],
        FluencyLevel.INTERMEDIATE, 40,
        "Vocabulario cientifico universal para ensino fundamental.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-MED-01", EducationLevel.HIGH_SCHOOL,
        "Debate e Argumentacao",
        ["opiniao", "concordar", "discordar", "justificar"],
        FluencyLevel.ADVANCED, 50,
        "Debates em LSU. Expressar opinioes complexas.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-MED-02", EducationLevel.HIGH_SCHOOL,
        "LSU Profissional",
        ["entrevista", "apresentacao", "negociacao"],
        FluencyLevel.ADVANCED, 40,
        "Uso profissional de LSU. Mercado de trabalho.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-UNI-01", EducationLevel.UNIVERSITY,
        "LSU Academico e Cientifico",
        ["tese", "pesquisa", "publicacao", "conferencia"],
        FluencyLevel.FLUENT, 80,
        "Uso academico de LSU. Artigos, conferencias, defesas.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-UNI-02", EducationLevel.UNIVERSITY,
        "Formacao de Instrutores",
        ["pedagogia_lsu", "avaliacao", "curriculo"],
        FluencyLevel.INSTRUCTOR, 120,
        "Formar instrutores certificados de LSU.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-SER-01", EducationLevel.PUBLIC_SERVICE,
        "LSU para Servidores Publicos",
        ["atendimento", "documentacao", "direitos", "emergencia"],
        FluencyLevel.INTERMEDIATE, 40,
        "Todo servidor publico deve ter nivel intermediario de LSU.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-SER-02", EducationLevel.PUBLIC_SERVICE,
        "LSU para Profissionais de Saude",
        ["anamnese", "sintomas", "diagnostico", "consentimento"],
        FluencyLevel.ADVANCED, 60,
        "Medicos, enfermeiros e receptionistas devem ter LSU avancado.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-PRO-01", EducationLevel.PROFESSIONAL,
        "LSU no Mercado de Trabalho",
        ["reuniao", "negociacao", "vendas", "atendimento_cliente"],
        FluencyLevel.INTERMEDIATE, 30,
        "Empresas treinam funcionarios em LSU.",
        "pratico"),
    LSUCurriculumUnit(
        "LSU-IDO-01", EducationLevel.ELDERLY,
        "LSU para Terceira Idade",
        ["saude", "memoria", "socializacao", "emergencia"],
        FluencyLevel.BASIC, 20,
        "Idosos aprendem LSU basico para socializacao e emergencia.",
        "pratico"),
]


# ============================================================================
# 4. ARTIGOS DA POLITICA (Detalhados)
# ============================================================================

@dataclass
class PolicyDetail:
    """Detalhamento de um artigo da politica."""
    article: PolicyArticle
    title: str
    text: str                              # texto da politica
    implementation_steps: List[str]        # como implementar
    timeline: str = ""                     # prazo
    responsible: str = ""                  # quem executa
    penalty: str = ""                      # o que acontece se descumprir


POLICY_ARTICLES: List[PolicyDetail] = [
    PolicyDetail(
        PolicyArticle.ART_1_LSU_FRANCA,
        "Lingua de Sinais Universal como Lingua Franca",
        text=(
            "A Lingua de Sinais Universal (LSU) e a lingua franca oficial "
            "da Republica para comunicacao entre pessoas de diferentes paises, "
            "linguas e condicoes. Todo cidadao tem direito de aprender LSU "
            "gratuitamente. Nenhuma conversa internacional requer ingles -- "
            "LSU basta."
        ),
        implementation_steps=[
            "Criar padrao oficial de sinais universais",
            "Implantar ensino de LSU em todas as escolas publicas",
            "Oferecer cursos gratuitos de LSU para todos os cidadaos",
            "Certificar instrutores de LSU",
        ],
        timeline="5 anos para implantacao nacional",
        responsible="Ministerio da Educacao + Ministerio da Cultura",
        penalty="Instituicoes publicas sem LSU perdem orcamento",
    ),
    PolicyDetail(
        PolicyArticle.ART_2_MATERNA_SAGRADA,
        "A Lingua Materna e Sagrada",
        text=(
            "NENHUMA lingua materna sera substituida pela LSU. "
            "O brasileiro continua falando portugues. O surdo continua "
            "usando Libras. A LSU e ADICIONADA como ponte, nunca como "
            "substituicao. Linguas indigenas, de heranca, regionais -- "
            "todas sao protegidas. A LSU convive, nao domina."
        ),
        implementation_steps=[
            "Garantir ensino em lingua materna em todas as escolas",
            "Proibir substituicao de lingua materna por LSU",
            "Proteger linguas indigenas e de heranca",
            "LSU e SEGUNDA lingua, nunca primeira",
        ],
        timeline="Permanente",
        responsible="Ministerio da Cultura + Conselho Indigena",
        penalty="Crime federal substituir lingua materna",
    ),
    PolicyDetail(
        PolicyArticle.ART_3_EDUCACAO_BILINGUE,
        "Educacao Bilingue: Materna + LSU",
        text=(
            "Toda escola publica ensina a lingua materna do aluno E a LSU. "
            "O surdo aprende Libras + LSU. O ouvinte aprende Portugues + LSU. "
            "O indigena aprende sua lingua + Portugues + LSU. "
            "Ninguem e obrigado a abandonar sua lingua. Todos GANHAM uma nova."
        ),
        implementation_steps=[
            "Curriculo escolar inclui LSU como disciplina obrigatoria",
            "Professores treinados em LSU",
            "Material didatico em materna + LSU",
            "Avaliacao em lingua materna (LSU nao e prova, e ferramenta)",
        ],
        timeline="3 anos para adaptacao curricular",
        responsible="Ministerio da Educacao",
        penalty="Escola sem LSU perde credenciamento",
    ),
    PolicyDetail(
        PolicyArticle.ART_4_SERVIDOR_OBRIGATORIO,
        "Servidor Publico Fala LSU",
        text=(
            "Todo servidor publico de atendimento deve ter fluencia minima "
            "INTERMEDIARIA em LSU. Recepcionista, medico, policial, professor, "
            "juiz, motorista de onibus -- todos. O cidadao surdo tem direito "
            "de ser atendido em LSU em QUALQUER orgao publico."
        ),
        implementation_steps=[
            "Treinar todos os servidores publicos em LSU",
            "Certificar fluencia como requisito para cargo publico",
            "Concurso publico inclui prova de LSU",
            "Interpretes disponiveis em todos os orgaos",
        ],
        timeline="5 anos para treinar todos os servidores",
        responsible="Ministerio da Administracao",
        penalty="Servidor sem LSU nao atende publico diretamente",
    ),
    PolicyDetail(
        PolicyArticle.ART_5_HOSPITAL_LSU,
        "Hospital com LSU 24h",
        text=(
            "Todo hospital, UPA, clinica e posto de saude tem interprete "
            "de LSU disponivel 24h. O surdo NAO pode ser atendido sem "
            "comunicacao. Anamnese, consentimento, diagnostico, tratamento "
            " -- tudo explicado em LSU se o paciente precisar."
        ),
        implementation_steps=[
            "Interpretes de LSU em plantao 24h nos hospitais",
            "App de traducao LSU para emergencias",
            "Cartazes e sinais visuais em LSU nos hospitais",
            "Prontuario medico com campo de comunicacao",
        ],
        timeline="2 anos para cobertura total",
        responsible="Ministerio da Saude",
        penalty="Hospital sem LSU perde credenciamento SUS",
    ),
    PolicyDetail(
        PolicyArticle.ART_6_MIDIA_LSU,
        "Midia com Janela LSU",
        text=(
            "Toda programacao de TV aberta, filmes, noticias governamentais "
            "e campanhas publicas tem janela de LSU. Nao legenda -- LSU. "
            "O surdo brasileiro tem direito de ver TV em LSU, nao so em "
            "Libras. TV internacional com LSU conecta com o mundo."
        ),
        implementation_steps=[
            "Janela de LSU em toda TV aberta",
            "Streaming oferece audio LSU",
            "Cinema com sessoes em LSU",
            "Jornais com secao em LSU",
        ],
        timeline="3 anos",
        responsible="Ministerio das Comunicacoes + ANATEL",
        penalty="Emissora sem LSU paga multa",
    ),
    PolicyDetail(
        PolicyArticle.ART_7_REUNIAO_INTERNACIONAL,
        "Reunioes Internacionais em LSU",
        text=(
            "Reunioes internacionais da Republica usam LSU como lingua oficial. "
            "Nao precisamos de ingles. Cada delegacao signa em sua lingua "
            "nativa, o sistema traduz para LSU, todos entendem. "
            "O brasileiro fala portugues. O japones fala japones. "
            "A LSU conecta."
        ),
        implementation_steps=[
            "Sistema de traducao em tempo real para reunioes",
            "Delegacoes treinadas em LSU",
            "Documentos oficiais traduzidos para LSU",
            "Conferencias com interpretacao LSU simultanea",
        ],
        timeline="Imediato para reunioes da Republica",
        responsible="Itamaraty + Republica",
        penalty="Nao aplicavel (cultura organizacional)",
    ),
    PolicyDetail(
        PolicyArticle.ART_8_DIGITAL_LSU,
        "Apps e Sites com Modo LSU",
        text=(
            "Todo site governamental e app publico tem modo LSU. "
            "O surdo navega, pede documentos, paga impostos, marca consulta "
            "-- tudo com avatar LSU. Empresas privadas com mais de 100 "
            "funcionarios tambem devem ter modo LSU."
        ),
        implementation_steps=[
            "Padrao de acessibilidade digital com LSU",
            "Avatar de LSU em sites governamentais",
            "App da Republica com modo LSU nativo",
            "Incentivo fiscal para empresas que adotam LSU digital",
        ],
        timeline="2 anos para gov.br, 5 anos para empresas",
        responsible="Ministerio da Ciencia e Tecnologia",
        penalty="Site sem LSU nao e considerado acessivel",
    ),
    PolicyDetail(
        PolicyArticle.ART_9_SINAIIS_PADRONIZADOS,
        "Sinais Universal Padronizados",
        text=(
            "A Republica lidera a criacao de um padrao internacional de "
            "sinais universais. Conceitos de emergencia, saude, direitos, "
            "direcoes -- padronizados mundialmente. Cada pais contribui. "
            "O padrao e aberto, livre, sem propriedade intelectual."
        ),
        implementation_steps=[
            "Comite internacional de padronizacao de LSU",
            "Dicionario aberto de LSU (open source)",
            "Conferencia anual de atualizacao de sinais",
            "Parceria com ONU, UNESCO, OMS",
        ],
        timeline="2 anos para primeiro padrao publicado",
        responsible="Republica + comunidade internacional",
        penalty="Nao aplicavel (lideranca voluntaria)",
    ),
    PolicyDetail(
        PolicyArticle.ART_10_CRIANCA_DESDE_CEDO,
        "LSU desde a Creche",
        text=(
            "O ensino de LSU comeca na creche (0-3 anos). Criancas surdas "
            "e ouvintes aprendem juntas. O cerebro infantil absorve linguagem "
            "de sinais tao naturalmente quanto fala. Quanto mais cedo, "
            "mais fluente. A creche que nao ensina LSU nao e creche -- "
            "e depósito de crianças."
        ),
        implementation_steps=[
            "Creches publicas com educadores de LSU",
            "Bebes surdos identificados ao nascer -> LSU imediato",
            "Pais de bebes surdos recebem LSU gratuito",
            "Material ludo-pedagogico em LSU para 0-6 anos",
        ],
        timeline="3 anos para todas as creches publicas",
        responsible="Ministerio da Educacao + Saude",
        penalty="Creche sem LSU perde licenca de funcionamento",
    ),
]


# ============================================================================
# 5. MODELO DE IMPLANTACAO NACIONAL
# ============================================================================

class ImplementationPhase(Enum):
    """Fases de implantacao da politica."""
    PHASE_1_PILOT = "fase_1_piloto"           # cidades piloto (ano 1)
    PHASE_2_CAPITALS = "fase_2_capitais"      # capitais (ano 2-3)
    PHASE_3_NATIONAL = "fase_3_nacional"      # todo pais (ano 3-5)
    PHASE_4_MATURE = "fase_4_maduro"          # sistema maduro (ano 5+)
    PHASE_5_INTERNATIONAL = "fase_5_internacional"  # exportar para outros paises


@dataclass
class ImplementationPlan:
    """Plano de implantacao por fase."""
    phase: ImplementationPhase
    year: str
    actions: List[str]
    target_population: str
    budget_brl: float = 0.0
    success_metric: str = ""


IMPLANTATION_PLAN: List[ImplementationPlan] = [
    ImplementationPlan(
        ImplementationPhase.PHASE_1_PILOT, "Ano 1 (2025)",
        actions=[
            "Selecionar 10 cidades piloto",
            "Treinar 1.000 instrutores de LSU",
            "Implantar LSU em 100 escolas piloto",
            "Criar padrao oficial de sinais universais",
            "App de traducao LSU em versao beta",
        ],
        target_population="500.000 cidadaos nas cidades piloto",
        budget_brl=200e6,
        success_metric="80% dos alunos piloto com LSU basico",
    ),
    ImplementationPlan(
        ImplementationPhase.PHASE_2_CAPITALS, "Ano 2-3 (2026-2027)",
        actions=[
            "Implantar LSU em todas as capitais",
            "Treinar 10.000 instrutores",
            "Servidores publicos em treinamento obrigatorio",
            "Hospitais com interprete LSU 24h",
            "TV aberta com janela LSU",
        ],
        target_population="50 milhoes de cidadaos nas capitais",
        budget_brl=2e9,
        success_metric="70% dos servidores com LSU intermediario",
    ),
    ImplementationPlan(
        ImplementationPhase.PHASE_3_NATIONAL, "Ano 3-5 (2027-2029)",
        actions=[
            "LSU em TODAS as escolas publicas do pais",
            "100.000 instrutores certificados",
            "Concurso publico com prova de LSU",
            "Interpretes em todos os orgaos publicos",
            "Sistema digital com avatar LSU nationwide",
        ],
        target_population="215 milhoes de brasileiros",
        budget_brl=10e9,
        success_metric="60% da populacao com LSU basico",
    ),
    ImplementationPlan(
        ImplementationPhase.PHASE_4_MATURE, "Ano 5+ (2030+)",
        actions=[
            "LSU e segunda lingua natural do pais",
            "Toda nova geracao fala LSU fluentemente",
            "Brasil exporta metodologia LSU",
            "Conferencia internacional anual em LSU",
            "Padrao LSU adotado por 10+ paises",
        ],
        target_population="215 milhoes + internacional",
        budget_brl=5e9,
        success_metric="90% da populacao com LSU basico",
    ),
    ImplementationPlan(
        ImplementationPhase.PHASE_5_INTERNATIONAL, "Ano 10+ (2035+)",
        actions=[
            "LSU adotada por paises da America Latina",
            "Parceria com Africa lusofona",
            "ONSU (Organizacao das Nacoes em Sinais Universal)",
            "LSU e lingua oficial da ONU",
            "Mundo sem barreira linguistica",
        ],
        target_population="Global",
        budget_brl=1e9,
        success_metric="20+ paises com LSU implantada",
    ),
]


# ============================================================================
# 6. MOTOR DE AVALIACAO DE FLUENCIA
# ============================================================================

class FluencyAssessmentEngine:
    """Avalia fluencia em LSU de cidadaos e instituicoes."""

    def __init__(self):
        self.assessments: Dict[str, Dict] = {}

    def assess_citizen(self, profile: CitizenLanguageProfile) -> Dict[str, Any]:
        """Avalia o perfil linguistico de um cidadao."""
        can_communicate_internationally = profile.lsu_fluency != FluencyLevel.NONE
        needs_interpreter = not can_communicate_internationally and not (
            profile.is_hearing and profile.mother_tongue_spoken == "en"
        )

        return {
            "citizen_id": profile.citizen_id,
            "name": profile.name,
            "mother_tongue": profile.mother_tongue_spoken,
            "native_sign": profile.native_sign_language or "nenhuma",
            "lsu_fluency": profile.lsu_fluency.value,
            "communication_methods": profile.communication_methods(),
            "can_communicate_internationally": can_communicate_internationally,
            "needs_interpreter_for_international": needs_interpreter,
            "lsu_gap": profile.lsu_fluency == FluencyLevel.NONE,
            "education_needed": self._recommend_education(profile),
        }

    def _recommend_education(self, profile: CitizenLanguageProfile) -> str:
        """Recomenda educacao LSU baseada no perfil."""
        if profile.lsu_fluency == FluencyLevel.NONE:
            return "Curso basico de LSU (40h) -- saudacoes, emergencia, necessidades"
        elif profile.lsu_fluency == FluencyLevel.BASIC:
            return "Curso intermediario de LSU (60h) -- conversa cotidiana"
        elif profile.lsu_fluency == FluencyLevel.INTERMEDIATE:
            return "Curso avancado de LSU (50h) -- debate, profissional"
        elif profile.lsu_fluency == FluencyLevel.ADVANCED:
            return "Curso de fluencia (80h) -- nivel nativo"
        elif profile.lsu_fluency in (FluencyLevel.FLUENT, FluencyLevel.NATIVE_SIGNER):
            return "Ja fluente. Pode se tornar instrutor (120h)"
        return "Manter praticar"

    def assess_institution(self, institution_name: str,
                           total_staff: int,
                           lsu_certified_staff: int,
                           has_interpreter: bool,
                           has_digital_lsu: bool) -> Dict[str, Any]:
        """Avalia conformidade de uma instituicao com a politica."""
        pct = (lsu_certified_staff / total_staff * 100) if total_staff > 0 else 0
        compliant = pct >= 60 and has_interpreter

        return {
            "institution": institution_name,
            "total_staff": total_staff,
            "lsu_certified": lsu_certified_staff,
            "lsu_percentage": round(pct, 1),
            "has_interpreter": has_interpreter,
            "has_digital_lsu": has_digital_lsu,
            "compliant_with_policy": compliant,
            "gap_staff": max(0, int(total_staff * 0.6) - lsu_certified_staff),
            "verdict": (
                "CONFORME" if compliant else
                "NAO CONFORME -- treinar mais " + str(max(0, int(total_staff * 0.6) - lsu_certified_staff)) + " servidores"
            ),
        }


# ============================================================================
# 7. CENARIO: CONVERSA INTERNACIONAL
# ============================================================================

class InternationalConversation:
    """
    Simula uma conversa internacional onde cada pessoa
    fala sua lingua materna e LSU conecta todos.
    """

    @staticmethod
    def simulate() -> str:
        """Simula conversa entre 4 pessoas de paises diferentes."""
        lines = []
        lines.append("=" * 65)
        lines.append("CONVERSA INTERNACIONAL VIA LSU")
        lines.append("=" * 65)
        lines.append("")

        participants = [
            {"name": "Cleiton", "country": "Brasil", "materna": "Portugues",
             "sign": "Libras", "condition": "ouvinte"},
            {"name": "Yuki", "country": "Japao", "materna": "Japones",
             "sign": "JSL", "condition": "surda"},
            {"name": "Pierre", "country": "Franca", "materna": "Frances",
             "sign": "LSF", "condition": "ouvinte"},
            {"name": "Aisha", "country": "Egito", "materna": "Arabe",
             "sign": "EgL", "condition": "surda"},
        ]

        lines.append("Participantes:")
        for p in participants:
            lines.append(f"  {p['name']:10} ({p['country']:10}) "
                        f"fala {p['materna']:12} / sinais {p['sign']:6} [{p['condition']}]")
        lines.append("")
        lines.append("SEM LSU:")
        lines.append("  Ninguem se entende. 4 linguas faladas diferentes.")
        lines.append("  2 surdos nao ouvem as 2 linguas faladas.")
        lines.append("  Com ingles: 2 surdos excluidos. Arabe/frances/japones nao compartilhados.")
        lines.append("  Resultado: FRACASSO comunicativo.")
        lines.append("")
        lines.append("COM LSU (Lingua de Sinais Universal):")
        lines.append("")

        conversation = [
            ("Cleiton", "ola", "ola", "Bom dia pessoal!"),
            ("Yuki", "ola", "konnichiwa", "Ola! Prazer em conhecer todos."),
            ("Pierre", "ola", "bonjour", "Bonjour! Que iniciativa incrivel."),
            ("Aisha", "ola", "marhaba", "Ola! Finalmente nos entendemos."),
            ("Cleiton", "trabalho", "trabalho", "Vamos falar sobre o projeto?"),
            ("Yuki", "sim", "sim", "Sim, tenho ideias."),
            ("Aisha", "ajuda", "ajuda", "Preciso de ajuda com a parte tecnica."),
            ("Pierre", "sim", "sim", "Posso ajudar! Tenho experiencia."),
        ]

        for speaker, concept_ls, concept_materna, message in conversation:
            person = next(p for p in participants if p["name"] == speaker)
            lines.append(f"  [{speaker} ({person['materna']})]")
            lines.append(f"    Fala em {person['materna']}: \"{message}\"")
            lines.append(f"    Sistema traduz para LSU: sinal '{concept_ls}'")
            lines.append(f"    Todos veem o AVATAR signando em LSU")
            lines.append(f"    Cada um entende na SUA lingua materna")
            lines.append("")

        lines.append("  RESULTADO:")
        lines.append("  4 paises. 4 linguas. 2 surdas. 2 ouvintes.")
        lines.append("  ZERO barreira. Todos se entenderam.")
        lines.append("  Ninguem precisou falar ingles.")
        lines.append("  Ninguem abandonou sua lingua materna.")
        lines.append("  A LSU conectou. Sempre.")
        lines.append("")
        return "\n".join(lines)


# ============================================================================
# 8. COMPARACAO: INGLES vs LSU
# ============================================================================

def render_comparison_english_vs_lsu() -> str:
    """Compara ingles vs LSU como lingua franca."""
    lines = []
    lines.append("=" * 65)
    lines.append("INGLES vs LSU -- POR QUE LSU VENCE")
    lines.append("=" * 65)
    lines.append("")

    comparisons = [
        ("Cego pode usar?", "NAO -- ingles e audio/texto", "SIM -- sinais sao visuais"),
        ("Surdo pode usar?", "NAO -- ingles e audio", "SIM -- sinais sao visuais"),
        ("Analfabeto pode usar?", "NAO -- ingles exige leitura", "SIM -- gestos nao exigem leitura"),
        ("Crianca de 2 anos?", "Dificil -- ingles e complexo", "SIM -- criancas signam antes de falar"),
        ("Idoso sem estudo?", "Dificil -- exige educacao formal", "SIM -- gestos sao intuitivos"),
        ("Custo de aprender?", "5-10 anos para fluencia", "1-3 anos para fluencia"),
        ("Exclui alguem?", "SIM -- surdos, analfabetos, varios paises", "NAO -- todos podem aprender"),
        ("Culturalmente neutro?", "NAO -- imposto pelo colonialismo", "SIM -- criado colaborativamente"),
        ("Precisa de tecnologia?", "NAO -- so voz/papel", "SIM para universal -- avatar/IA"),
        ("Substitui lingua materna?", "Tende a SIM (imperialismo)", "NAO -- e ponte, nao substituicao"),
    ]

    lines.append(f"  {'CRITERIO':<25} {'INGLES':<35} {'LSU':<35}")
    lines.append("  " + "-" * 95)
    for criteria, eng, lsu in comparisons:
        lines.append(f"  {criteria:<25} {eng:<35} {lsu:<35}")

    lines.append("")
    lines.append("  VENCEDOR: LSU")
    lines.append("  O ingles exclui. A LSU inclui.")
    lines.append("  O ingles rouba cultura. A LSU adiciona cultura.")
    lines.append("  O ingles beneficia paises ricos. A LSU beneficia TODOS.")
    lines.append("")
    return "\n".join(lines)


# ============================================================================
# 9. DEMONSTRACAO
# ============================================================================

def demo():
    print("=" * 70)
    print("OpenSignLanguagePolicy -- LSU como Nova Lingua Franca Mundial")
    print("=" * 70)

    print(f"\nArtigos da politica: {len(PolicyArticle)}")
    print(f"Niveis de ensino: {len(EducationLevel)}")
    print(f"Niveis de fluencia: {len(FluencyLevel)}")
    print(f"Unidades curriculares: {len(LSU_CURRICULUM)}")
    print(f"Fases de implantacao: {len(ImplementationPhase)}")

    # Artigos
    print(f"\n{'=' * 70}")
    print("POLITICA DE LINGUAGEM UNIVERSAL -- 10 ARTIGOS")
    print(f"{'=' * 70}")
    for pd in POLICY_ARTICLES:
        print(f"\n  {pd.article.value.upper()}: {pd.title}")
        print(f"  TEXTO: {pd.text[:100]}...")
        print(f"  PRAZO: {pd.timeline}")
        print(f"  RESPONSAVEL: {pd.responsible}")

    # Curriculo
    print(f"\n{'=' * 70}")
    print("CURRICULO DE LSU POR FAIXA ETARIA")
    print(f"{'=' * 70}")
    for unit in LSU_CURRICULUM:
        print(f"\n  {unit.unit_id}: {unit.title}")
        print(f"    Nivel: {unit.level.value} | Fluencia: {unit.target_fluency.value}")
        print(f"    Horas: {unit.estimated_hours}h | Avaliacao: {unit.assessment_method}")
        print(f"    Conceitos: {', '.join(unit.concepts)}")

    # Plano de implantacao
    print(f"\n{'=' * 70}")
    print("PLANO DE IMPLANTACAO NACIONAL")
    print(f"{'=' * 70}")
    total_budget = 0
    for plan in IMPLANTATION_PLAN:
        total_budget += plan.budget_brl
        print(f"\n  {plan.phase.value.upper()} ({plan.year})")
        print(f"    Populacao: {plan.target_population}")
        print(f"    Orcamento: R$ {plan.budget_brl/1e9:.1f} bilhoes")
        print(f"    Metrica: {plan.success_metric}")
        for a in plan.actions:
            print(f"      -> {a}")
    print(f"\n  ORCAMENTO TOTAL: R$ {total_budget/1e9:.1f} bilhoes")

    # Comparacao ingles vs LSU
    print(render_comparison_english_vs_lsu())

    # Conversa internacional
    print(InternationalConversation.simulate())

    # Avaliacao de cidadao
    print(f"\n{'=' * 70}")
    print("AVALIACAO DE FLUENCIA")
    print(f"{'=' * 70}")

    engine = FluencyAssessmentEngine()

    citizens = [
        CitizenLanguageProfile("c1", "Cleiton", lsu_fluency=FluencyLevel.ADVANCED),
        CitizenLanguageProfile("c2", "Maria (surda)", is_deaf=True, is_hearing=False,
                               native_sign_language="bzs", lsu_fluency=FluencyLevel.FLUENT),
        CitizenLanguageProfile("c3", "Joao (sem LSU)", lsu_fluency=FluencyLevel.NONE),
    ]

    for c in citizens:
        result = engine.assess_citizen(c)
        print(f"\n  {result['name']}")
        print(f"    LSU: {result['lsu_fluency']}")
        print(f"    Comunica internacionalmente: {result['can_communicate_internationally']}")
        print(f"    Precisa de interprete: {result['needs_interpreter_for_international']}")
        print(f"    Educacao recomendada: {result['education_needed']}")

    # Avaliacao de instituicao
    print(f"\n  INSTITUICAO: Hospital Sao Paulo")
    inst = engine.assess_institution("Hospital SP", 500, 150, True, True)
    print(f"    Servidores LSU: {inst['lsu_certified']}/{inst['total_staff']} ({inst['lsu_percentage']}%)")
    print(f"    Tem interprete: {inst['has_interpreter']}")
    print(f"    Veredito: {inst['verdict']}")

    # Resumo
    print(f"\n{'=' * 70}")
    print("VEREDictO DA POLITICA")
    print(f"{'=' * 70}")
    print()
    print("  O ingles FALHOU como lingua universal.")
    print("  Exclui surdos. Exclui analfabetos. Exclui paises pobres.")
    print()
    print("  A LSU (Lingua de Sinais Universal) e a NOVA lingua franca.")
    print("  Visual. Gestual. Universal. Inclusiva. Natural.")
    print()
    print("  Cada pessoa fala sua lingua materna para APRENDER.")
    print("  Cada pessoa usa LSU para CONVERSAR com o mundo.")
    print()
    print("  Nenhuma lingua roubada. Nenhuma cultura apagada.")
    print("  A LSU e PONTE, nao substituicao.")
    print()
    print("  10 artigos. 15 unidades curriculares. 5 fases de implantacao.")
    print("  R$ 18 bilhoes em 10 anos para 215 milhoes de brasileiros.")
    print("  Depois, exportar para o mundo.")
    print()
    print("  P7 (faca e faca) + P8 (democratizar).")
    print("  A Republica fala TODAS as linguas.")


if __name__ == "__main__":
    demo()
