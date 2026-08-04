#!/usr/bin/env python3
"""
OpenCandidatoScore -- Mensuracao Estatistica de Candidatos por Ministerio
===========================================================================
"Nao e quem voce gosta. E quem tem COMPROVACAO de que entrega."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple
import math


# ============================================================
# SCORING (3 camadas)
# ============================================================

@dataclass
class ScoreCamada:
    """Score de uma camada."""
    fez_funcionar: float    # 0-1: tem artefato publico funcionando?
    liderou: float          # 0-1: liderou equipe/orgao?
    escalou: float          # 0-1: serviu milhares/milhoes?
    sob_pressao: float      # 0-1: fez com recurso limitado?
    repetiu: float          # 0-1: e rotina ou foi 1x?


def score_camada1(c: ScoreCamada) -> float:
    """Camada 1: o que JA FEZ. Maximo 1.0."""
    return (c.fez_funcionar * 3 + c.liderou * 2 + c.escalou * 2 +
            c.sob_pressao * 1 + c.repetiu * 1) / 9


def score_camada2(gestao_publica: bool, orcamento: bool,
                  dados_sistemas: bool, liderou_equipe: bool,
                  publicou: bool) -> float:
    """Camada 2: trabalho correlato. Maximo 1.0."""
    return sum([gestao_publica, orcamento, dados_sistemas, liderou_equipe, publicou]) / 5


def score_camada3(falhou_reconstruiu: bool, entrega_rapida: bool,
                  aceita_ser_medido: bool, tem_obra_publica: bool,
                  coerencia: bool) -> float:
    """Camada 3: predicao. Maximo 1.0."""
    return sum([falhou_reconstruiu, entrega_rapida, aceita_ser_medido,
                tem_obra_publica, coerencia]) / 5


def score_total(c1: float, c2: float, c3: float) -> float:
    """Score total ponderado. Maximo 5.0."""
    return (c1 * 3 + c2 * 2 + c3 * 1) / 6 * 5


# ============================================================
# CANDIDATOS (base de conhecimento)
# ============================================================

@dataclass
class Candidato:
    """Um candidato a ministro/cargo avaliado pelo sistema."""
    nome: str
    partido: str
    origem: str           # "politico", "tecnico", "movimento", "empresarial"
    curriculo_resumo: str

    # Scores brutos por camada (0-1)
    c1: ScoreCamada
    c2_gestao: bool
    c2_orcamento: bool
    c2_dados: bool
    c2_liderou: bool
    c2_publicou: bool
    c3_falhou_reconstruiu: bool
    c3_entrega_rapida: bool
    c3_aceita_medido: bool
    c3_obra_publica: bool
    c3_coerencia: bool

    # Ministerios adequados (score manual de fit 0-1)
    fits: Dict[str, float] = field(default_factory=dict)

    # Dados de realidade
    feito_real: str = ""        # maior conquista verificavel
    falha_real: str = ""        # maior falha verificavel
    controversia: str = ""      # ponto de tensao

    @property
    def score_c1(self) -> float:
        return score_camada1(self.c1)

    @property
    def score_c2(self) -> float:
        return score_camada2(self.c2_gestao, self.c2_orcamento, self.c2_dados,
                             self.c2_liderou, self.c2_publicou)

    @property
    def score_c3(self) -> float:
        return score_camada3(self.c3_falhou_reconstruiu, self.c3_entrega_rapida,
                             self.c3_aceita_medido, self.c3_obra_publica, self.c3_coerencia)

    @property
    def score_total_val(self) -> float:
        return score_total(self.score_c1, self.score_c2, self.score_c3)

    @property
    def veredito(self) -> str:
        s = self.score_total_val
        if s >= 4.0:
            return "APROVADO"
        else:
            return "WO"


# ============================================================
# MINISTERIOS (39 atuais)
# ============================================================

MINISTERIOS = [
    # Economia e Infra
    "Fazenda", "Planejamento", "Gestao_Publica", "Desenvolvimento_Industrial",
    "Agricultura", "Agraria_Familiar", "Minas_Energia", "Transportes",
    "Portos_Aeroportos", "Integracao_Regional", "Turismo",
    # Social
    "Saude", "Educacao", "Desenvolvimento_Social", "Trabalho",
    "Previdencia", "Esporte", "Cultura", "Cidades",
    # Direitos
    "Mulheres", "Igualdade_Racial", "Direitos_Humanos", "Indigenas", "Pesca",
    # Justica
    "Justica_Seguranca", "Defesa",
    # Ambiente e Ciencia
    "Meio_Ambiente", "Ciencia_Tecnologia", "Comunicacoes",
    # Controle
    "CGU", "AGU",
    # Externo
    "Relacoes_Exteriores",
    # Presidencia
    "Casa_Civil", "Secretaria_Geral", "Vice_Presidencia",
]


# ============================================================
# CANDIDATOS CONHECIDOS (base de treinamento)
# ============================================================

def _init_candidatos() -> List[Candidato]:
    return [

        # === MARINA SILVA ===
        Candidato(
            nome="Marina Silva", partido="REDE/SUSTENTABILIDADE", origem="politico/movimento",
            curriculo_resumo="Seringueira, ministra Meio Ambiente (2003-2008), senadora (AC), 3x candidata a presidente",
            c1=ScoreCamada(fez_funcionar=0.9, liderou=0.9, escalou=0.9, sob_pressao=0.8, repetiu=0.5),
            c2_gestao=True, c2_orcamento=True, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=False, c3_aceita_medido=True, c3_obra_publica=True, c3_coerencia=True,
            fits={"Meio_Ambiente": 1.0, "Agraria_Familiar": 0.9, "Educacao": 0.7, "Saude": 0.6,
                  "Desenvolvimento_Social": 0.8, "Cultura": 0.5, "Cidades": 0.4},
            feito_real="Reduziu desmatamento 80% (2004-2012). Criou Programa Cisternas e PAA.",
            falha_real="3 candidaturas presidenciais perdidas. Demitida por conflito politico.",
            controversia="Evangelica: posicao sobre drogas e direitos LGBT gera tensoes.",
        ),

        # === FERNANDO HADDAD ===
        Candidato(
            nome="Fernando Haddad", partido="PT", origem="politico/tecnico",
            curriculo_resumo="Ministro Educacao (2005-2012), prefeito SP (2013-2016), ministro Fazenda (2023+)",
            c1=ScoreCamada(fez_funcionar=0.8, liderou=0.9, escalou=0.8, sob_pressao=0.7, repetiu=0.8),
            c2_gestao=True, c2_orcamento=True, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=False, c3_aceita_medido=True, c3_obra_publica=True, c3_coerencia=True,
            fits={"Fazenda": 0.9, "Educacao": 0.9, "Planejamento": 0.8, "Casa_Civil": 0.7,
                  "Cidades": 0.7, "Ciencia_Tecnologia": 0.5},
            feito_real="PROUNIexpandido, ENEM modernizado, Reuni. Prefeito SP: ciclovias, Lei Cidade Limpa origem.",
            falha_real="Perdeu eleicao SP para Doria. Gestao Fazenda sob criticas fiscais.",
            controversia="Confronto com mercado financeiro sobre arcabouco fiscal.",
        ),

        # === SERGIO MORO ===
        Candidato(
            nome="Sergio Moro", partido="PODEMOS", origem="tecnico/judicial",
            curriculo_resumo="Juiz federal, ministro Justica (2019-2020), prefeito Maringa (2021+)",
            c1=ScoreCamada(fez_funcionar=0.7, liderou=0.7, escalou=0.6, sob_pressao=0.8, repetiu=0.5),
            c2_gestao=True, c2_orcamento=False, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=False, c3_aceita_medido=False, c3_obra_publica=True, c3_coerencia=True,
            fits={"Justica_Seguranca": 0.9, "CGU": 0.7, "Defesa": 0.5, "Direitos_Humanos": 0.2},
            feito_real="Operacao Lava Jato. Lei Anticrime (parcial). Prefeito de cidade media.",
            falha_real="Decisoes judiciais revertidas (STF). Renuncia ministerial.",
            controversia="Vazamento de mensagens. Parcialidade questionada (STF: 11x3).",
        ),

        # === TARCISIO DE FREITAS ===
        Candidato(
            nome="Tarcisio de Freitas", partido="REPUBLICANOS", origem="tecnico/militar",
            curriculo_resumo="General do Exercito, ministro Infraestrutura (2019-2022), governador SP (2023+)",
            c1=ScoreCamada(fez_funcionar=0.7, liderou=0.8, escalou=0.8, sob_pressao=0.6, repetiu=0.6),
            c2_gestao=True, c2_orcamento=True, c2_dados=False, c2_liderou=True, c2_publicou=False,
            c3_falhou_reconstruiu=False, c3_entrega_rapida=True, c3_aceita_medido=False, c3_obra_publica=True, c3_coerencia=True,
            fits={"Transportes": 0.9, "Portos_Aeroportos": 0.9, "Cidades": 0.7, "Defesa": 0.8,
                  "Integracao_Regional": 0.6, "Minas_Energia": 0.5},
            feito_real="Concessoes de rodovias, aeroportos regionais. PAC mobilidade. Governador do maior estado.",
            falha_real="Concessoes questionadas (TCU). Obras atrasadas.",
            controversia="Ligacao com Bolsonaro e centro evangelico.",
        ),

        # === CIRO GOMES ===
        Candidato(
            nome="Ciro Gomes", partido="PDT", origem="politico/tecnico",
            curriculo_resumo="Governador Ceara (2x), ministro Integracao, prefeito Fortaleza, deputado, 3x candidato presidente",
            c1=ScoreCamada(fez_funcionar=0.7, liderou=0.8, escalou=0.7, sob_pressao=0.7, repetiu=0.7),
            c2_gestao=True, c2_orcamento=True, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=False, c3_aceita_medido=True, c3_obra_publica=True, c3_coerencia=True,
            fits={"Fazenda": 0.7, "Integracao_Regional": 0.9, "Educacao": 0.6, "Saude": 0.5,
                  "Planejamento": 0.7, "Cidades": 0.6},
            feito_real="Ceara: vacinacao 95%, solidez fiscal. Ministerio: transposicao Sao Francisco.",
            falha_real="3 candidaturas perdidas. Confrontos com aliados.",
            controversia="Temporamento explosivo. Discursos polamicos.",
        ),

        # === BOULOS ===
        Candidato(
            nome="Guilherme Boulos", partido="PSOL", origem="movimento",
            curriculo_resumo="Lider MTST, deputado federal, 2x candidato a prefeito SP",
            c1=ScoreCamada(fez_funcionar=0.5, liderou=0.7, escalou=0.5, sob_pressao=0.8, repetiu=0.6),
            c2_gestao=False, c2_orcamento=False, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=True, c3_aceita_medido=True, c3_obra_publica=False, c3_coerencia=True,
            fits={"Cidades": 0.8, "Desenvolvimento_Social": 0.8, "Habitação": 0.9, "Direitos_Humanos": 0.7,
                  "Trabalho": 0.6, "Saude": 0.4},
            feito_real="MTST: ocupacoes que resultaram em moradia. Deputado: protagonismo legislative popular.",
            falha_real="Nunca administrou orgao publico executivo.",
            controversia="Ocupacao de terrenos. Polaridade extrema.",
        ),

        # === SONIA GUAJAJARA ===
        Candidato(
            nome="Sonia Guajajara", partido="PSOL", origem="movimento/indigena",
            curriculo_resumo="Lider indigena, ministra dos Povos Originarios (2023+)",
            c1=ScoreCamada(fez_funcionar=0.5, liderou=0.7, escalou=0.4, sob_pressao=0.9, repetiu=0.5),
            c2_gestao=True, c2_orcamento=False, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=False, c3_aceita_medido=True, c3_obra_publica=False, c3_coerencia=True,
            fits={"Indigenas": 1.0, "Meio_Ambiente": 0.8, "Igualdade_Racial": 0.7,
                  "Direitos_Humanos": 0.7, "Cultura": 0.6},
            feito_real="APIB (Articulacao Povos Indigenas Brasil). Ministerio criado e liderado.",
            falha_real="Demarcacoes paralisadas (Marco Temporal).",
            controversia="Tensao com setor ruralista e evangelico.",
        ),

        # === FLAVIO DINO ===
        Candidato(
            nome="Flavio Dino", partido="PSB", origem="politico/judicial",
            curriculo_resumo="Governador Maranhao (2x), ministro Justica (2023-2024), ministro STF (2024+)",
            c1=ScoreCamada(fez_funcionar=0.8, liderou=0.9, escalou=0.7, sob_pressao=0.7, repetiu=0.8),
            c2_gestao=True, c2_orcamento=True, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=True, c3_aceita_medido=True, c3_obra_publica=True, c3_coerencia=True,
            fits={"Justica_Seguranca": 0.9, "Casa_Civil": 0.7, "CGU": 0.6, "Defesa": 0.5,
                  "Educacao": 0.6, "Saude": 0.5},
            feito_real="MA: reducao homicidios, ampliacao Universidade Estadual, transparencia fiscal.",
            falha_real="Indicacao ao STF vista como politica.",
            controversia="Centralizacao de poder no Maranhao (dinastia).",
        ),

        # === CAMILO SANTANA ===
        Candidato(
            nome="Camilo Santana", partido="PT", origem="politico/tecnico",
            curriculo_resumo="Governador Ceara (2x), ministro Educacao (2024+)",
            c1=ScoreCamada(fez_funcionar=0.8, liderou=0.9, escalou=0.7, sob_pressao=0.7, repetiu=0.8),
            c2_gestao=True, c2_orcamento=True, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=True, c3_aceita_medido=True, c3_obra_publica=True, c3_coerencia=True,
            fits={"Educacao": 0.9, "Saude": 0.6, "Casa_Civil": 0.7, "Planejamento": 0.7,
                  "Cidades": 0.6},
            feito_real="CE: IDEB subiu, universidade estadual expandiu, vacinacao 95%.",
            falha_real="Indicacoes politicas questionadas.",
            controversia="Continuismo politico no CE.",
        ),

        # === EDUARDO LEITE ===
        Candidato(
            nome="Eduardo Leite", partido="PSDB", origem="politico",
            curriculo_resumo="Governador Rio Grande do Sul (2x), prefeito Pelotas",
            c1=ScoreCamada(fez_funcionar=0.7, liderou=0.8, escalou=0.6, sob_pressao=0.8, repetiu=0.7),
            c2_gestao=True, c2_orcamento=True, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=True, c3_aceita_medido=True, c3_obra_publica=True, c3_coerencia=True,
            fits={"Educacao": 0.7, "Saude": 0.6, "Cidades": 0.7, "Planejamento": 0.6,
                  "Cultura": 0.5, "Agricultura": 0.6},
            feito_real="RS: gestao crise enchentes 2024, programa RS Mais, transparencia.",
            falha_real="Gestao pre-enchentes criticada. Renuncia para candidatura presidencial.",
            controversia="Abertamente gay em partido conservador. Tensao com bolsonarismo.",
        ),

        # === ANDRE LARA RESENDE ===
        Candidato(
            nome="Andre Lara Resende", partido="NOVO", origem="tecnico/academico",
            curriculo_resumo="Economista, um dos pais do Plano Real, banqueiro, academico",
            c1=ScoreCamada(fez_funcionar=0.9, liderou=0.7, escalou=0.9, sob_pressao=0.9, repetiu=0.5),
            c2_gestao=True, c2_orcamento=True, c2_dados=True, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=False, c3_entrega_rapida=False, c3_aceita_medido=True, c3_obra_publica=True, c3_coerencia=True,
            fits={"Fazenda": 0.9, "Planejamento": 0.9, "Desenvolvimento_Industrial": 0.7,
                  "Casa_Civil": 0.6},
            feito_real="Plano Real (1994). Estabilizacao economica mais bem-sucedida do Brasil.",
            falha_real="Nunca administrou orgao publico executivo.",
            controversia="Critico de politica fiscal atual.",
        ),

        # === ALOYSIO NUNES FERREIRA ===
        Candidato(
            nome="Aloysio Nunes Ferreira", partido="PSDB", origem="politico",
            curriculo_resumo="Senador, ministro, deputado, vice-governador SP",
            c1=ScoreCamada(fez_funcionar=0.6, liderou=0.7, escalou=0.5, sob_pressao=0.5, repetiu=0.7),
            c2_gestao=True, c2_orcamento=True, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=False, c3_aceita_medido=True, c3_obra_publica=False, c3_coerencia=True,
            fits={"Relacoes_Exteriores": 0.8, "Casa_Civil": 0.6, "Planejamento": 0.6},
            feito_real="Itamaraty: diplomacia tradicional. Experiencia institucional ampla.",
            falha_real="Gestao apagada. Sem reforma estrutural.",
            controversia="Sem controversias maiores.",
        ),

        # === DEMAIS CANDIDATOS (scores mais baixos, menos experiencia) ===
        Candidato(
            nome="Janja Lula da Silva", partido="PT", origem="tecnico/social",
            curriculo_resumo="Primeira-dama, servidora publica (Eletrobras/Itaipu), comunicadora",
            c1=ScoreCamada(fez_funcionar=0.5, liderou=0.5, escalou=0.4, sob_pressao=0.6, repetiu=0.5),
            c2_gestao=False, c2_orcamento=False, c2_dados=False, c2_liderou=True, c2_publicou=False,
            c3_falhou_reconstruiu=False, c3_entrega_rapida=True, c3_aceita_medido=False, c3_obra_publica=False, c3_coerencia=True,
            fits={"Mulheres": 0.6, "Comunicacoes": 0.5, "Cultura": 0.4},
            feito_real="Comunicacao institucional. Engajamento em causas femininas.",
            falha_real="Nunca administrou orgao publico.",
            controversia="Posicionamentos publicos polamicos.",
        ),

        Candidato(
            nome="Nikolas Ferreira", partido="PL", origem="politico",
            curriculo_resumo="Deputado federal (mais votado), advogado, youtuber",
            c1=ScoreCamada(fez_funcionar=0.3, liderou=0.4, escalou=0.3, sob_pressao=0.5, repetiu=0.4),
            c2_gestao=False, c2_orcamento=False, c2_dados=False, c2_liderou=False, c2_publicou=False,
            c3_falhou_reconstruiu=False, c3_entrega_rapida=True, c3_aceita_medido=False, c3_obra_publica=False, c3_coerencia=True,
            fits={"Justica_Seguranca": 0.3, "Comunicacoes": 0.4},
            feito_real="Deputado mais votado. Canal YouTube com milhoes de views.",
            falha_real="Nenhuma gestao publica. Zero projetos executados.",
            controversia="Discurso polarizador. Jovem sem experiencia executiva.",
        ),

        Candidato(
            nome="Damares Alves", partido="REPUBLICANOS", origem="politico/religioso",
            curriculo_resumo="Ministra Mulheres/DH (2019-2022), pastora, advogada",
            c1=ScoreCamada(fez_funcionar=0.4, liderou=0.6, escalou=0.4, sob_pressao=0.6, repetiu=0.5),
            c2_gestao=True, c2_orcamento=False, c2_dados=False, c2_liderou=True, c2_publicou=False,
            c3_falhou_reconstruiu=False, c3_entrega_rapida=False, c3_aceita_medido=False, c3_obra_publica=False, c3_coerencia=True,
            fits={"Mulheres": 0.5, "Direitos_Humanos": 0.3},
            feito_real="Ministerio da Mulher criado/formado.",
            falha_real="Controversias sobre dados falsos. Denuncia de assedio no ministerio.",
            controversia="Discurso conservador. Dados fabricados.",
        ),

        Candidato(
            nome="Erika Hilton", partido="PSOL", origem="politico/movimento",
            curriculo_resumo="Vereadora SP, deputada federal, primeira transexual eleita",
            c1=ScoreCamada(fez_funcionar=0.4, liderou=0.5, escalou=0.4, sob_pressao=0.8, repetiu=0.4),
            c2_gestao=False, c2_orcamento=False, c2_dados=False, c2_liderou=False, c2_publicou=False,
            c3_falhou_reconstruiu=False, c3_entrega_rapida=True, c3_aceita_medido=True, c3_obra_publica=False, c3_coerencia=True,
            fits={"Direitos_Humanos": 0.7, "Mulheres": 0.5, "Igualdade_Racial": 0.5},
            feito_real="Visibilidade LGBTQ+ no legislativo.",
            falha_real="Nenhuma gestao executiva.",
            controversia="Polarizadora. Ataques constantes.",
        ),

        Candidato(
            nome="Rui Costa", partido="PT", origem="politico",
            curriculo_resumo="Governador Bahia (2x), ministro Casa Civil (2024+)",
            c1=ScoreCamada(fez_funcionar=0.8, liderou=0.9, escalou=0.7, sob_pressao=0.7, repetiu=0.8),
            c2_gestao=True, c2_orcamento=True, c2_dados=False, c2_liderou=True, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=True, c3_aceita_medido=True, c3_obra_publica=True, c3_coerencia=True,
            fits={"Casa_Civil": 0.9, "Saude": 0.6, "Cidades": 0.7, "Integracao_Regional": 0.7,
                  "Planejamento": 0.6},
            feito_real="BA: gestao COVID elogiada. Investimento em interior. FIHB.",
            falha_real="Gestao fiscal questionada (divida BA).",
            controversia="Maquina politica baiana.",
        ),

        Candidato(
            nome="Ricardo Stuckert", partido="PT", origem="jornalismo/fotografia",
            curriculo_resumo="Fotografo oficial de Lula, jornalista",
            c1=ScoreCamada(fez_funcionar=0.3, liderou=0.3, escalou=0.2, sob_pressao=0.5, repetiu=0.5),
            c2_gestao=False, c2_orcamento=False, c2_dados=False, c2_liderou=False, c2_publicou=True,
            c3_falhou_reconstruiu=True, c3_entrega_rapida=False, c3_aceita_medido=False, c3_obra_publica=False, c3_coerencia=True,
            fits={"Comunicacoes": 0.3, "Cultura": 0.2},
            feito_real="Imagem publica de Lula. Documentacao fotografica.",
            falha_real="Nenhuma gestao executiva. Zero obra publica.",
            controversia="Fotografo em cargo de comunicacao.",
        ),
    ]


class CandidatoScoreSistema:
    """
    Sistema de mensuracao estatistica de candidatos por ministerio.
    """

    def __init__(self):
        self.candidatos = _init_candidatos()

    def ranking_por_ministerio(self) -> Dict[str, List[Tuple[Candidato, float]]]:
        """Para cada ministerio, ranqueia os candidatos por score ponderado."""
        resultado = {}
        for minist in MINISTERIOS:
            scores = []
            for c in self.candidatos:
                if minist in c.fits:
                    score = c.score_total_val * c.fits[minist]
                    scores.append((c, score))
            scores.sort(key=lambda x: x[1], reverse=True)
            resultado[minist] = scores
        return resultado

    def melhor_por_ministerio(self) -> Dict[str, Dict[str, Any]]:
        """Melhor candidato para cada ministerio."""
        ranking = self.ranking_por_ministerio()
        resultado = {}
        for minist, scores in ranking.items():
            if scores:
                melhor = scores[0]
                resultado[minist] = {
                    "candidato": melhor[0].nome,
                    "partido": melhor[0].partido,
                    "score": round(melhor[1], 2),
                    "score_base": round(melhor[0].score_total_val, 2),
                    "fit": melhor[0].fits.get(minist, 0),
                    "veredito": melhor[0].veredito,
                    "feito": melhor[0].feito_real,
                }
            else:
                resultado[minist] = {"candidato": "SEM CANDIDATO", "score": 0, "veredito": "WO"}
        return resultado

    def ranking_candidatos(self) -> List[Dict[str, Any]]:
        """Ranking geral de candidatos por score total."""
        return sorted([{
            "nome": c.nome, "partido": c.partido, "origem": c.origem,
            "score_c1": round(c.score_c1, 2),
            "score_c2": round(c.score_c2, 2),
            "score_c3": round(c.score_c3, 2),
            "score_total": round(c.score_total_val, 2),
            "veredito": c.veredito,
            "feito": c.feito_real,
            "falha": c.falha_real,
            "n_ministerios": len(c.fits),
        } for c in self.candidatos], key=lambda x: x["score_total"], reverse=True)

    def scorecard(self) -> Dict[str, Any]:
        total = len(self.candidatos)
        aprovados = sum(1 for c in self.candidatos if c.veredito == "APROVADO")
        jequeri = sum(1 for c in self.candidatos if c.veredito == "JEQUERI")
        wo = sum(1 for c in self.candidatos if c.veredito == "WO")
        score_medio = sum(c.score_total_val for c in self.candidatos) / total if total else 0
        return {
            "modulo": "open_candidato_score",
            "versao": "0.1.0-spec",
            "candidatos_avaliados": total,
            "ministerios": len(MINISTERIOS),
            "aprovados": aprovados,
            "jequeri": jequeri,
            "wo": wo,
            "score_medio": round(score_medio, 2),
            "metodologia": "3 camadas: fez (3x), correlato (2x), predicao (1x). Max 5.0.",
            "corte": ">=4.0 APROVADO, <4.0 WO (eliminado). Sem jequeri.",
            "limitacao": "Base de conhecimento pre-2025. Nao inclui todos os pre-candidatos. Web search indisponivel.",
        }


def _demo():
    sis = CandidatoScoreSistema()
    sc = sis.scorecard()
    ranking = sis.ranking_candidatos()
    melhores = sis.melhor_por_ministerio()

    print("=" * 75)
    print("CANDIDATO SCORE -- Mensuracao Estatistica por Ministerio")
    print("=" * 75)

    print(f"\n{sc['candidatos_avaliados']} candidatos avaliados para {sc['ministerios']} ministerios")
    print(f"Aprovados: {sc['aprovados']} | Jequeri: {sc['jequeri']} | WO: {sc['wo']}")
    print(f"Score medio: {sc['score_medio']}")
    print(f"\nLimitacao: {sc['limitacao']}")

    print(f"\n{'='*75}")
    print("RANKING GERAL DE CANDIDATOS")
    print(f"{'='*75}")
    for i, c in enumerate(ranking):
        print(f"\n  {i+1}. {c['nome']} ({c['partido']}) -- {c['origem']}")
        print(f"     SCORE: {c['score_total']} [{c['veredito']}]")
        print(f"     C1={c['score_c1']} C2={c['score_c2']} C3={c['score_c3']}")
        print(f"     FEZ: {c['feito'][:70]}")
        if c['falha']:
            print(f"     FALHA: {c['falha'][:70]}")

    print(f"\n{'='*75}")
    print("MELHOR CANDIDATO POR MINISTERIO")
    print(f"{'='*75}")
    for minist in MINISTERIOS:
        m = melhores.get(minist, {})
        nome = m.get("candidato", "---")
        score = m.get("score", 0)
        vered = m.get("veredito", "---")
        if nome != "SEM CANDIDATO":
            print(f"  {minist:<30} {nome:<30} score={score:.1f} [{vered}]")
        else:
            print(f"  {minist:<30} --- SEM CANDIDATO ---")


if __name__ == "__main__":
    _demo()
