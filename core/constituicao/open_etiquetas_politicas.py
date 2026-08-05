#!/usr/bin/env python3
"""
OpenEtiquetasPoliticas -- Sistema de Etiquetas por Impacto Real
==================================================================
"Nao e bonito nem feio. E #ProtetorVulneravel ou #ElitistaExcludente.
 O rotulo nao e opiniao. E padrao dominante nos dados."

Substitui a pergunta 'e bom?' por 16 etiquetas em 4 pilares.
Cada etiqueta é BINARIA: tem ou nao tem. O conjunto define o perfil.

Pilares:
  1. GESTAO FISCAL (como lida com dinheiro publico)
  2. TRANSPARENCIA E INTEGRIDADE (rastreabilidade)
  3. EFICIENCIA (entrega resultado ou so fala?)
  4. IMPACTO SOCIAL ( quem beneficia?)

Metodo:
  - Dados oficiais (TCU, Portal Transparencia, Diario Oficial)
  - Historico de votos (promessa vs execucao)
  - Indicadores de resultado (IBGE, IPEA) -- NAO usar percepcao

AVISO: Os inputs das etiquetas sao OPINIAO ate triangulacao com fonte externa.
O sistema de medicao é REAL. As etiquetas atribuidas sao HIPOTETICAS.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ETIQUETAS (16 rotulos em 4 pilares)
# ============================================================================

class Pilar(Enum):
    GESTAO_FISCAL = "gestao_fiscal"
    TRANSPARENCIA = "transparencia"
    EFICIENCIA = "eficiencia"
    IMPACTO_SOCIAL = "impacto_social"
    CAPACIDADE_TECNICA = "capacidade_tecnica"
    VERDADE_DADOS = "verdade_dados"
    SUSTENTABILIDADE = "sustentabilidade"
    DIALOGO = "dialogo"
    INOVACAO = "inovacao"


class Polaridade(Enum):
    POSITIVA = "positiva"   # ter esta etiqueta é BOM
    NEGATIVA = "negativa"   # ter esta etiqueta é RUIM


@dataclass(frozen=True)
class Etiqueta:
    """Um rotulo analitico aplicado a um politico."""
    id: str                    # identificador snake_case
    hashtag: str               # #ResponsavelFiscal
    nome: str                  # nome legivel
    pilar: Pilar               # qual pilar
    polaridade: Polaridade     # positiva ou negativa
    descricao: str             # o que significa
    criterio_objetivo: str     # como medir (dado, nao opiniao)
    fonte_dados: str           # onde buscar a evidencia
    impacto_score: float       # quanto afeta o score final (-1.0 a +1.0)


def _init_etiquetas() -> Dict[str, Etiqueta]:
    return {
        # ===== GESTAO FISCAL =====
        "responsavel_fiscal": Etiqueta(
            "responsavel_fiscal", "#ResponsavelFiscal",
            "Responsavel Fiscal",
            Pilar.GESTAO_FISCAL, Polaridade.POSITIVA,
            "Mantem contas equilibradas. Reduz divida/PIB ou apresenta superavit primario consistente.",
            "Divida liquida/receita corrente dentro da LRF com tendencia de queda OU superavit primario 3+ anos",
            "TCU, SICONFI, STN",
            +0.15),
        "gastador_compulsivo": Etiqueta(
            "gastador_compulsivo", "#GastadorCompulsivo",
            "Gastador Compulsivo",
            Pilar.GESTAO_FISCAL, Polaridade.NEGATIVA,
            "Aumenta despesas correntes sem contrapartida de eficiencia ou receita. Deficit estrutural.",
            "Gasto corrente cresce > inflation + PIB growth por 2+ anos sem nova receita",
            "SICONFI, STN",
            -0.20),
        "incentivador_produtivo": Etiqueta(
            "incentivador_produtivo", "#IncentivadorProdutivo",
            "Incentivador Produtivo",
            Pilar.GESTAO_FISCAL, Polaridade.POSITIVA,
            "Reduz burocracia. Facilita abertura de empresas. Aumenta competitividade setorial mensuravel.",
            "Reducao de tempo para abrir empresa OU aumento de empresas formais no mandato",
            "Receita Federal, CNPJ, Mapa do Mercado Geral",
            +0.10),
        "barreira_burocratica": Etiqueta(
            "barreira_burocratica", "#BarreiraBurocratica",
            "Barreira Burocratica",
            Pilar.GESTAO_FISCAL, Polaridade.NEGATIVA,
            "Cria normas que aumentam complexidade regulatoria sem justificativa tecnica de protecao social/ambiental.",
            "Aumento de normas reguladoras sem estudo de impacto + queda em indicadores de facilidade",
            "DOU, Congresso, Banco Mundial (Doing Business)",
            -0.10),

        # ===== TRANSPARENCIA E INTEGRIDADE =====
        "caixa_preta": Etiqueta(
            "caixa_preta", "#CaixaPreta",
            "Caixa Preta",
            Pilar.TRANSPARENCIA, Polaridade.NEGATIVA,
            "Vota contra transparencia. Patrimonio inconsistente. Beneficia empresas sem licitacao.",
            "Voto contra Lei de Acesso a Informacao OU patrimonio >30% do declarado OU licitacao dispensada >20%",
            "CGU, TCU, Portal da Transparencia, Conselho de Etica",
            -0.30),
        "vidro_transparente": Etiqueta(
            "vidro_transparente", "#VidroTransparente",
            "Vidro Transparente",
            Pilar.TRANSPARENCIA, Polaridade.POSITIVA,
            "Publica agenda completa. Reunioes com lobistas documentadas. Auditoria externa independente.",
            "Agenda publica + reunioes documentadas + auditoria voluntaria 100%",
            "Portal da Transparencia, CGU, ONGs (Transparencia Brasil)",
            +0.20),
        "conflito_interesse": Etiqueta(
            "conflito_interesse", "#ConflitoInteresseAtivo",
            "Conflito de Interesses",
            Pilar.TRANSPARENCIA, Polaridade.NEGATIVA,
            "Legisla em setor onde tem participacao acionaria direta ou indireta nao blindada.",
            "Voto/proposicao em setor de empresa familiar OU nao declarou vinculo societario",
            "CVM, Receita Federal, TSE (bens), Portal da Transparencia",
            -0.25),
        "blindado_etico": Etiqueta(
            "blindado_etico", "#BlindadoEtico",
            "Blindado Etico",
            Pilar.TRANSPARENCIA, Polaridade.POSITIVA,
            "Compliance rigoroso. Renuncia beneficios pessoais. Auditorias voluntarias frequentes.",
            "Compliance documentado + renuncia beneficio + auditoria voluntaria anual",
            "CGU, Conselho de Etica, declaracoes publicas verificaveis",
            +0.15),

        # ===== EFICIENCIA LEGISLATIVA E EXECUTIVA =====
        "fazedor_lei_util": Etiqueta(
            "fazedor_lei_util", "#FazedorDeLeiUtil",
            "Fazedor de Lei Util",
            Pilar.EFICIENCIA, Polaridade.POSITIVA,
            "Autor de leis aprovadas, implementadas e com impacto mensuravel positivo.",
            "2+ leis propres aprovadas com indicador de impacto melhorando pos-implementacao",
            "Congresso, DOU, indicadores IBGE/IPEA",
            +0.20),
        "autor_lei_simbolica": Etiqueta(
            "autor_lei_simbolica", "#AutorDeLeiSimbolica",
            "Autor de Lei Simbolica",
            Pilar.EFICIENCIA, Polaridade.NEGATIVA,
            "Muitos projetos nunca votados, inconstitucionais ou impacto nulo. Populismo legislativo.",
            "Proposicoes aprovadas <10% do total OU >50% inconstitucionais ou arquivadas",
            "Camara dos Deputados, Senado, STF (ADIs)",
            -0.10),
        "executor_eficiente": Etiqueta(
            "executor_eficiente", "#ExecutorEficiente",
            "Executor Eficiente",
            Pilar.EFICIENCIA, Polaridade.POSITIVA,
            "Entrega obras/servicos no prazo e orcamento. Baixa taxa de aditivos contratuais.",
            "Execucao fisica >90% do previsto + aditivos <5% do contrato",
            "TCU, Portal Obras, SICONFI",
            +0.15),
        "paralisado_cronico": Etiqueta(
            "paralisado_cronico", "#ParalisadoCronico",
            "Paralisado Cronico",
            Pilar.EFICIENCIA, Polaridade.NEGATIVA,
            "Obras paradas. Servicos interrompidos. Alta rotatividade de secretarios sem resultado.",
            "Obras paradas >12 meses OU execucao <60% do orcamento OU rotatividade >40%/ano",
            "TCU, Portal Obras, diarios oficiais",
            -0.20),

        # ===== IMPACTO SOCIAL E COERENCIA =====
        "coerente_programatico": Etiqueta(
            "coerente_programatico", "#CoerenteProgramatico",
            "Coerente Programatico",
            Pilar.IMPACTO_SOCIAL, Polaridade.POSITIVA,
            "Vota e age estritamente conforme plataforma eleitoral documentada.",
            "Concordancia voto-programa >85% em proposicoes-chave",
            "TSE (programa de governo), Congresso,合作协议 observatorios legislativos",
            +0.15),
        "camaleao_oportunista": Etiqueta(
            "camaleao_oportunista", "#CamaleaoOportunista",
            "Camaleao Oportunista",
            Pilar.IMPACTO_SOCIAL, Polaridade.NEGATIVA,
            "Muda posicionamentos fundamentais para se aliar ao poder. Sem justificativa tecnica.",
            "Troca de partido/banco >2x OU voto contrario a programa em >30% sem justificativa",
            "TSE, Congresso, observatorios (Pulso, Congresso em Foco)",
            -0.25),
        "protetor_vulneravel": Etiqueta(
            "protetor_vulneravel", "#ProtetorVulneravel",
            "Protetor do Vulneravel",
            Pilar.IMPACTO_SOCIAL, Polaridade.POSITIVA,
            "Politicas focadas em reduzir desigualdade com metricas melhorando ano a ano.",
            "Indicadores sociais (fome, mortalidade, escolaridade) do decil mais pobre melhorando > media nacional",
            "IBGE (PNAD/PNS), IPEA, UNICEF, VIGISAN",
            +0.25),
        "elitista_excludente": Etiqueta(
            "elitista_excludente", "#ElitistaExcludente",
            "Elitista Excludente",
            Pilar.IMPACTO_SOCIAL, Polaridade.NEGATIVA,
            "Beneficia desproporcionalmente grupos de alta renda enquanto base estagna ou piora.",
            "Gasto regressivo (subsidio ao topo > base) OU indicadores do decil rico crescendo > pobre por 3+ anos",
            "IBGE, IPEA,Politica Fiscal (ONS), PNAD",
            -0.30),

        # ===== CAPACIDADE TECNICA E GOVERNANCA =====
        "meritocratico_tecnico": Etiqueta(
            "meritocratico_tecnico", "#MeritocraticoTecnico",
            "Meritocratico Tecnico",
            Pilar.CAPACIDADE_TECNICA, Polaridade.POSITIVA,
            "Nomeia secretarios e diretores por curriculo comprovado e experiencia na area. Rotatividade baixa em cargos tecnicos.",
            "100% dos cargos tecnicos com perfil adequado + rotatividade <15%/ano",
            "DOU/diarios, curriculos Lattes, SIAPE",
            +0.15),
        "apadrinhado_politico": Etiqueta(
            "apadrinhado_politico", "#ApadrinhadoPolitico",
            "Apadrinhado Politico",
            Pilar.CAPACIDADE_TECNICA, Polaridade.NEGATIVA,
            "Preenche cargos-chave (saude, educacao, obras) com aliados ou familiares sem qualificacao. Alta rotatividade por troca de apoio.",
            "Cargos comissionados >50% do total OU rotatividade >40%/ano OU parente em cargo tecnico",
            "SIAPE, diarios, CGU (nepotismo)",
            -0.25),
        "gestor_de_crise": Etiqueta(
            "gestor_de_crise", "#GestorDeCrise",
            "Gestor de Crise",
            Pilar.CAPACIDADE_TECNICA, Polaridade.POSITIVA,
            "Reage bem a emergencias (enchentes, pandemias, colapsos). Bom em apagar fogo.",
            "Resposta a crise documentada com resultado positivo (ex: vacinacao >90% na pandemia)",
            "Relatorios de crise, OMS, Defesa Civil",
            +0.10),
        "planejador_estrategico": Etiqueta(
            "planejador_estrategico", "#PlanejadorEstrategico",
            "Planejador Estrategico",
            Pilar.CAPACIDADE_TECNICA, Polaridade.POSITIVA,
            "Plano de governo detalhado com metas de 4/8 anos, monitoramento publico de KPIs e ajustes baseados em dados.",
            "Plano com metas quantificaveis + relatorio anual publico + KPIs rastreaveis",
            "PPA, LDO, LOA, portal de metas",
            +0.15),

        # ===== VERDADE E DADOS =====
        "baseado_em_evidencias": Etiqueta(
            "baseado_em_evidencias", "#BaseadoEmEvidencias",
            "Baseado em Evidencias",
            Pilar.VERDADE_DADOS, Polaridade.POSITIVA,
            "Justifica decisoes citando estudos, dados e pareceres. Admite erros quando dados contradizem suas acoes.",
            "Decisoes com nota tecnica citando fonte verificavel + admissao publica de erro documentada",
            "Notas tecnicas, DOU, discursos protocolados",
            +0.15),
        "ideologico_rigido": Etiqueta(
            "ideologico_rigido", "#IdeologicoRigido",
            "Ideologico Rigido",
            Pilar.VERDADE_DADOS, Polaridade.NEGATIVA,
            "Mantem politicas mesmo quando dados mostram ineficacia. Prioriza dogma sobre resultado.",
            "Politica mantida apos dado oficial mostrar ineficacia OU veto a estudo solicitado",
            "Congresso, DOU, indicadores IBGE/IPEA",
            -0.15),
        "negacionista_dados": Etiqueta(
            "negacionista_dados", "#NegacionistaDados",
            "Negacionista de Dados",
            Pilar.VERDADE_DADOS, Polaridade.NEGATIVA,
            "Ignora ou distorce estatisticas oficiais quando contrariam narrativa. Cria dados alternativos sem metodologia.",
            "Contradicao publica com dado oficial + criacao de 'dado alternativo' sem metodologia",
            "Checagens (Agencia Lupa, UOL, Comprova), IBGE",
            -0.25),
        "populista_numerico": Etiqueta(
            "populista_numerico", "#PopulistaNumerico",
            "Populista Numerico",
            Pilar.VERDADE_DADOS, Polaridade.NEGATIVA,
            "Usa numeros reais fora de contexto para criar narrativas enganosas (ex: recorde sem ajustar por inflacao/populacao).",
            "Numero real citado sem contexto (sem ajuste inflacionario/per capita) repetido 3+ vezes",
            "Checagens, IBGE, BCB (deflatores)",
            -0.10),

        # ===== SUSTENTABILIDADE E LONGO PRAZO =====
        "visao_legado": Etiqueta(
            "visao_legado", "#VisaoLegado",
            "Visao de Legado",
            Pilar.SUSTENTABILIDADE, Polaridade.POSITIVA,
            "Inicia projetos estruturantes (saneamento, energia, educacao basica) com retorno pos-mandato. Assume custo politico imediato.",
            "Obra/projeto com retorno >4 anos iniciado e nao concluido no mandato mas com execucao >60%",
            "TCU, Portal Obras, PPA",
            +0.15),
        "curto_prazista": Etiqueta(
            "curto_prazista", "#CurtoPrazista",
            "Curto Prazista",
            Pilar.SUSTENTABILIDADE, Polaridade.NEGATIVA,
            "Foca em obras visiveis e rapidas (pavimentacao, eventos) para reeleicao. Deixa passivos ocultos.",
            "Orcamento >60% em obras de curto prazo + manutencao adiada + passivo crescente",
            "SICONFI, TCU, PPA",
            -0.15),
        "predador_recursos": Etiqueta(
            "predador_recursos", "#PredadorRecursos",
            "Predador de Recursos",
            Pilar.SUSTENTABILIDADE, Polaridade.NEGATIVA,
            "Esgota recursos naturais ou financeiros sem plano de reposicao ou sustentabilidade.",
            "Fundo soberano/reserva esgotado OU recurso natural explorado sem reposicao (desmatamento, aquifero)",
            "ANA, INPE, IBAMA, TCU",
            -0.25),

        # ===== DIALOGO E REPRESENTATIVIDADE =====
        "ouvidor_ativo": Etiqueta(
            "ouvidor_ativo", "#OuvidorAtivo",
            "Ouvidor Ativo",
            Pilar.DIALOGO, Polaridade.POSITIVA,
            "Realiza consultas publicas reais, incorpora sugestoes da sociedade civil e presta contas em linguagem acessivel.",
            "Consultas publicas com participacao >1000 + sugestoes incorporadas documentadas",
            "Portais de participacao, conselhos, diarios",
            +0.10),
        "surdo_institucional": Etiqueta(
            "surdo_institucional", "#SurdoInstitucional",
            "Surdo Institucional",
            Pilar.DIALOGO, Polaridade.NEGATIVA,
            "Ignora conselhos municipais/estaduais. Audiencias publicas sao mera formalidade.",
            "Decisao contraria a conselho + audiencia publica sem impacto na decisao final",
            "Atas de conselhos, diarios",
            -0.15),
        "polarizador_toxico": Etiqueta(
            "polarizador_toxico", "#PolarizadorToxico",
            "Polarizador Toxico",
            Pilar.DIALOGO, Polaridade.NEGATIVA,
            "Usa discurso de odio ou divisao social como ferramenta principal de mobilizacao.",
            "3+ discursos publicos com odio/divisao documentados OU associacao a grupo de odio",
            "Redes sociais (publicas), TSE (quejas), checagens",
            -0.30),
        "conciliador_pragmatico": Etiqueta(
            "conciliador_pragmatico", "#ConciliadorPragmatico",
            "Conciliador Pragmatico",
            Pilar.DIALOGO, Polaridade.POSITIVA,
            "Constroi coalizoes tecnicas transversais para aprovar medidas necessarias, mesmo sem maioria ideologica.",
            "Aprovacao de medida com voto transversal (esquerda+direita) documentada",
            "Congresso, diarios, observatorios",
            +0.10),

        # ===== EFICIENCIA DIGITAL E INOVACAO =====
        "estado_digital": Etiqueta(
            "estado_digital", "#EstadoDigital",
            "Estado Digital",
            Pilar.INOVACAO, Polaridade.POSITIVA,
            "Implementa servicos 100% online. Reduz deslocamento e filas. Dados abertos em formato machine-readable.",
            "100% dos servicos essenciais online + dados abertos em API + fila fisica reduzida >50%",
            "gov.br, dados.gov.br, ranking digital",
            +0.10),
        "analogico_obsoleto": Etiqueta(
            "analogico_obsoleto", "#AnalogicoObsoleto",
            "Analogico Obsoleto",
            Pilar.INOVACAO, Polaridade.NEGATIVA,
            "Mantem processos burocraticos em papel. Exige presenca fisica para servicos simples. Resiste a digitalizacao.",
            "Servico essencial sem opcao online OU exigencia de papel quando digital e possivel",
            "Levantamento de servicos, gov.br",
            -0.10),
    }


# ============================================================================
# 2. METRICAS TANGIVEIS (5 setores)
# ============================================================================

class SetorMetrica(Enum):
    SAUDE = "saude"
    EDUCACAO = "educacao"
    SEGURANCA = "seguranca"
    INFRAESTRUTURA = "infraestrutura"
    FISCAL = "fiscal"


@dataclass(frozen=True)
class MetricaTangivel:
    """Uma metrica objetiva que mede impacto na vida da populacao."""
    id: str
    setor: SetorMetrica
    nome: str
    descricao: str
    unidade: str              # "dias", "%", "por 100k hab"
    direcao_sucesso: str      # "reduzir" ou "aumentar"
    fonte: str                # onde obter o dado
    exemplo_sucesso: str      # o que conta como vitoria


def _init_metricas() -> List[MetricaTangivel]:
    return [
        # SAUDE
        MetricaTangivel("sau_espera", SetorMetrica.SAUDE,
            "Tempo Medio de Espera para Consulta Especializada",
            "Dias entre solicitacao e consulta. Mede acesso real.",
            "dias", "reduzir",
            "SIM/SIA-SUS, filas estaduais/municipais",
            "Reducao constante ano a ano"),
        MetricaTangivel("sau_mortalidade_infantil", SetorMetrica.SAUDE,
            "Taxa de Mortalidade Infantil e Materna",
            "Indicador bruto da qualidade da atencao basica e pre-natal.",
            "por 1000 nascidos vivos", "reduzir",
            "SIM (Sistema de Informacao sobre Mortalidade), DATASUS",
            "Tendencia de queda abaixo da media nacional/regional"),
        MetricaTangivel("sau_resolutividade", SetorMetrica.SAUDE,
            "Resolutividade da Atencao Basica",
            "% de casos resolvidos na UBS sem encaminhamento a especialista.",
            "%", "aumentar",
            "eSUS-AB, SIA-SUS",
            "Aumento da % indica prevencao eficaz"),
        MetricaTangivel("sau_medicamentos", SetorMetrica.SAUDE,
            "Disponibilidade de Medicamentos Essenciais",
            "% de dias do ano com estoque zero de medicamentos da lista essencial.",
            "% dias com estoque zero", "reduzir",
            "Farmacia municipal/estadual, SMS",
            "Estoque >95% do tempo = sucesso"),

        # EDUCACAO
        MetricaTangivel("edu_ideb", SetorMetrica.EDUCACAO,
            "Proficiencia Media no IDEB",
            "Nota combinada de fluxo (aprovacao) e desempenho (provas).",
            "nota 0-10", "aumentar",
            "INEP, SAEB, Censo Escolar",
            "Crescimento anual da nota"),
        MetricaTangivel("edu_abandono", SetorMetrica.EDUCACAO,
            "Taxa de Abandono Escolar",
            "% de alunos que deixam a escola antes de concluir o ciclo.",
            "%", "reduzir",
            "Censo Escolar, INEP",
            "Reducao proxima a zero"),
        MetricaTangivel("edu_alfabetizacao", SetorMetrica.EDUCACAO,
            "Alfabetizacao na Idade Certa",
            "% de criancas alfabetizadas ate o 2 ano do fundamental.",
            "%", "aumentar",
            "SAEB, INEP",
            ">80-90% conforme meta PNE"),
        MetricaTangivel("edu_infra", SetorMetrica.EDUCACAO,
            "Infraestrutura Minima Escolar",
            "% de escolas com agua tratada, esgoto, energia e internet.",
            "%", "aumentar",
            "Censo Escolar, INEP",
            "100%"),

        # SEGURANCA
        MetricaTangivel("seg_homicidios", SetorMetrica.SEGURANCA,
            "Taxa de Homicidios",
            "Homicidios por 100 mil habitantes. Alta notificacao.",
            "por 100k hab", "reduzir",
            "SUS (SIM), SSP estaduais, FBSP",
            "Reducao sustentada ano a ano"),
        MetricaTangivel("seg_elucidacao", SetorMetrica.SEGURANCA,
            "Taxa de Elucidacao de Crimes",
            "% de crimes solucionados pela policia.",
            "%", "aumentar",
            "SSP estaduais, CNCGP",
            "Aumento da % indica eficiencia investigativa"),
        MetricaTangivel("seg_roubo", SetorMetrica.SEGURANCA,
            "Roubo de Veiculos e Celulares",
            "Crimes contra patrimonio por 100 mil habitantes.",
            "por 100k hab", "reduzir",
            "SSP estaduais, SESPE",
            "Reducao absoluta e per capita"),

        # INFRAESTRUTURA
        MetricaTangivel("inf_deslocamento", SetorMetrica.INFRAESTRUTURA,
            "Tempo Medio de Deslocamento Casa-Trabalho",
            "Tempo medio de deslocamento diario.",
            "minutos", "reduzir",
            "PNAD Continua (IBGE)",
            "Reducao ou estabilizacao enquanto cidade cresce"),
        MetricaTangivel("inf_agua", SetorMetrica.INFRAESTRUTURA,
            "Continuidade do Abastecimento de Agua",
            "Horas de interrupcao por mes por residencia.",
            "horas/mes", "reduzir",
            "SNIS, concessionarias, ANA",
            "<4 horas/mes (padrao ANA)"),
        MetricaTangivel("inf_esgoto", SetorMetrica.INFRAESTRUTURA,
            "Coleta de Esgoto Tratado",
            "% da populacao com acesso a rede coletora e tratamento efetivo.",
            "%", "aumentar",
            "SNIS, ANA",
            "Nao confundir com rede instalada"),
        MetricaTangivel("inf_pavimento", SetorMetrica.INFRAESTRUTURA,
            "Qualidade do Pavimento",
            "Indice de qualidade de rodovias/vias urbanas.",
            "indice 0-5", "aumentar",
            "CNT, DNIT, DERs",
            ">80% da malha classificada como bom/excelente"),

        # FISCAL
        MetricaTangivel("fis_transparencia", SetorMetrica.FISCAL,
            "Indice de Transparencia",
            "Nota de orgaos de controle externo.",
            "nota 0-10", "aumentar",
            "TCU, CGU, Transparencia Brasil",
            "Nota maxima ou crescente"),
        MetricaTangivel("fis_execucao", SetorMetrica.FISCAL,
            "Execucao Orcamentaria de Investimentos",
            "% do orcamento previsto que foi efetivamente pago e entregue.",
            "%", "aumentar",
            "SICONFI, STN, LOA/LDO",
            ">90% de execucao fisica e financeira"),
        MetricaTangivel("fis_divida", SetorMetrica.FISCAL,
            "Divida Liquida / Receita Corrente",
            "Capacidade de pagamento.",
            "ratio", "reduzir",
            "SICONFI, STN",
            "Dentro da LRF com tendencia de queda"),
    ]


# ============================================================================
# 3. CAMADA 0: OMISSAO / COMISSAO
# ============================================================================

@dataclass
class RegistroOmissao:
    """Um registro de ter tido cargo + problema existia + resolveu ou nao."""
    politico: str
    cargo: str
    periodo: str             # "2011-2016"
    problema: str            # "fome", "desmatamento", etc
    indicador_inicio: str    # "33M em fome"
    indicador_fim: str       # "40M em fome"
    resolveu: bool           # melhorou?
    fonte: str


def _init_omissoes_exemplo() -> List[RegistroOmissao]:
    """Exemplos de registros de omissao (HIPOTETICOS ate verificacao)."""
    return [
        RegistroOmissao(
            "[MOCK - exemplo]", "Presidente", "2011-2016",
            "fome", "33M em 2011", "33M em 2016",
            False, "VIGISAN (mock)"),
        RegistroOmissao(
            "[MOCK - exemplo]", "Governador CE", "2015-2022",
            "IDEB", "IDEB 4.2 em 2015", "IDEB 5.8 em 2022",
            True, "INEP"),
    ]


# ============================================================================
# 4. CLASSIFICADOR
# ============================================================================

@dataclass
class PerfilPolitico:
    """O perfil completo de um politico com etiquetas e metricas."""
    nome: str
    cargo: str
    etiquetas: List[str] = field(default_factory=list)  # ids de Etiqueta
    omissao: Optional[RegistroOmissao] = None
    nota_fiscal: Optional[float] = None     # 0-10
    nota_transparencia: Optional[float] = None
    nota_eficiencia: Optional[float] = None
    nota_impacto: Optional[float] = None

    @property
    def etiquetas_positivas(self) -> List[str]:
        return [e for e in self.etiquetas if _ETIQUETAS[e].polaridade == Polaridade.POSITIVA]

    @property
    def etiquetas_negativas(self) -> List[str]:
        return [e for e in self.etiquetas if _ETIQUETAS[e].polaridade == Polaridade.NEGATIVA]

    @property
    def impacto_liquido(self) -> float:
        """Soma do impacto de todas as etiquetas no score."""
        return sum(_ETIQUETAS[e].impacto_score for e in self.etiquetas)

    @property
    def perfil_dominante(self) -> str:
        """Etiqueta mais impactante (positiva ou negativa)."""
        if not self.etiquetas:
            return "SEM_DADOS"
        return max(self.etiquetas, key=lambda e: abs(_ETIQUETAS[e].impacto_score))

    def resumo(self) -> str:
        has = self.etiquetas
        if not has:
            return f"{self.nome}: SEM ETIQUETAS (sem dados verificaveis)"
        pos = [f"+{_ETIQUETAS[e].hashtag}" for e in self.etiquetas_positivas]
        neg = [f"-{_ETIQUETAS[e].hashtag}" for e in self.etiquetas_negativas]
        partes = []
        if pos: partes.append(" ".join(pos))
        if neg: partes.append(" ".join(neg))
        impacto = f" (impacto: {self.impacto_liquido:+.2f})"
        omissao_str = ""
        if self.omissao and not self.omissao.resolveu:
            omissao_str = f" | OMISSAO: {self.omissao.problema} ({self.omissao.cargo})"
        return f"{self.nome}: {' | '.join(partes)}{impacto}{omissao_str}"


# ============================================================================
# 5. SISTEMA
# ============================================================================

_ETIQUETAS: Dict[str, Etiqueta] = {}
_METRICAS: List[MetricaTangivel] = []


def _init():
    global _ETIQUETAS, _METRICAS
    _ETIQUETAS = _init_etiquetas()
    _METRICAS = _init_metricas()


_init()


def classificar(
    nome: str,
    cargo: str,
    etiquetas: List[str],
    omissao: Optional[RegistroOmissao] = None,
) -> PerfilPolitico:
    """Cria um perfil politico com etiquetas."""
    # Validar etiquetas
    validas = [e for e in etiquetas if e in _ETIQUETAS]
    invalidas = [e for e in etiquetas if e not in _ETIQUETAS]
    if invalidas:
        raise ValueError(f"Etiquetas invalidas: {invalidas}. Validas: {list(_ETIQUETAS.keys())}")
    return PerfilPolitico(nome=nome, cargo=cargo, etiquetas=validas, omissao=omissao)


def aplicar_camada0(score_base: float, perfil: PerfilPolitico) -> Tuple[float, str]:
    """
    Aplica Camada 0 (Omissao/Comissao) ao score.

    Retorna (novo_score, explicacao).
    """
    score = score_base
    explicacoes = []

    # Impacto das etiquetas
    if perfil.etiquetas:
        ajuste = perfil.impacto_liquido
        score += ajuste
        explicacoes.append(f"Etiquetas: {ajuste:+.2f}")

    # Omissao punitiva
    if perfil.omissao and not perfil.omissao.resolveu:
        score -= 0.50
        explicacoes.append(
            f"Omissao: teve cargo ({perfil.omissao.cargo}), "
            f"problema '{perfil.omissao.problema}' existia e NAO resolveu. "
            f"({perfil.omissao.indicador_inicio} -> {perfil.omissao.indicador_fim}). -0.50")

    # Omissao bonus (resolveu)
    if perfil.omissao and perfil.omissao.resolveu:
        score += 0.30
        explicacoes.append(
            f"Comissao: teve cargo ({perfil.omissao.cargo}), "
            f"resolveu '{perfil.omissao.problema}'. "
            f"({perfil.omissao.indicador_inicio} -> {perfil.omissao.indicador_fim}). +0.30")

    # Clamp 0-5
    score = max(0.0, min(5.0, score))

    return score, " | ".join(explicacoes)


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo():
    print("=" * 70)
    print("OPEN ETIQUETAS POLITICAS")
    print("=" * 70)

    print(f"\n16 ETIQUETAS em 4 pilares:\n")
    for pilar in Pilar:
        ets = [e for e in _ETIQUETAS.values() if e.pilar == pilar]
        print(f"  {pilar.value.upper()}:")
        for e in ets:
            icon = "+" if e.polaridade == Polaridade.POSITIVA else "-"
            print(f"    {icon} {e.hashtag:25s} impacto: {e.impacto_score:+.2f}")
        print()

    print(f"18 METRICAS TANGIVEIS em 5 setores:\n")
    for setor in SetorMetrica:
        ms = [m for m in _METRICAS if m.setor == setor]
        print(f"  {setor.value.upper()}:")
        for m in ms:
            print(f"    {m.nome:45s} ({m.unidade}) -> {m.direcao_sucesso}")
        print()

    # Exemplos
    print("=" * 70)
    print("EXEMPLOS DE PERFIS (MOCK):\n")

    perfis = [
        classificar(
            "[MOCK A]", "Governador",
            ["responsavel_fiscal", "vidro_transparente", "executor_eficiente",
             "protetor_vulneravel"],
            omissao=RegistroOmissao(
                "[MOCK A]", "Governador", "2019-2022",
                "IDEB", "IDEB 4.2", "IDEB 5.8",
                True, "INEP")),
        classificar(
            "[MOCK B]", "Deputado Federal",
            ["caixa_preta", "camaleao_oportunista", "autor_lei_simbolica",
             "elitista_excludente"],
            omissao=RegistroOmissao(
                "[MOCK B]", "Deputado", "2019-2022",
                "fome", "33M", "40M",
                False, "VIGISAN")),
        classificar(
            "[MOCK C]", "Senador",
            ["conflito_interesse", "paralisado_cronico"]),
    ]

    for p in perfis:
        print(f"  {p.resumo()}")
        novo, exp = aplicar_camada0(3.5, p)
        print(f"    Score base 3.50 -> {novo:.2f} ({exp})")
        print()

    print("=" * 70)
    print("CAMADA 0 (OMISSAO/COMISSAO):")
    print("  Teve cargo + problema existia + nao resolveu = -0.50")
    print("  Teve cargo + problema existia + resolveu = +0.30")
    print("  Etiquetas negativas: -0.10 a -0.30 cada")
    print("  Etiquetas positivas: +0.10 a +0.25 cada")
    print("=" * 70)


if __name__ == "__main__":
    _demo()
