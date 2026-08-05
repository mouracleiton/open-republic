#!/usr/bin/env python3
"""
OpenSimulacaoMultipla -- Simulacao Multi-Politica por Eixo
=============================================================
Cada eixo do Raio X tem multiplas politicas.
Cada politica tem seu proprio Gate WO, lideranca e satisfacao.
Um eixo so e "resolvido" quando TODAS as politicas passam.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


class StatusPolitica(Enum):
    APROVADA = "APROVADA"       # passou no Gate WO (7/7)
    JEQUERI = "JEQUERI"         # 5/5 criticos
    WO = "W.O."                 # nao passou
    SEM_CONSENSO = "SEM_CONSENSO"  # coalizao nao chegou em acordo


@dataclass
class PoliticaPublica:
    """Uma politica publica individual dentro de um eixo."""
    id: str
    eixo: str                   # qual dos 18 eixos do Raio X
    titulo: str
    descricao: str

    # Gate WO
    tem_como: bool
    tem_quem: bool
    tem_custo: bool
    tem_prazo: bool
    tem_metrica: bool
    tem_fonte: bool
    tem_diagnostico: bool

    # Quem lidera a execucao
    partido_lider: str
    partido_executor: str       # quem poe a mao na massa

    # Satisfacao por partido (0-10)
    satisfacao: Dict[str, int]  # partido -> satisfacao (negativo = insatisfeito)

    @property
    def score_gate(self) -> int:
        return sum([self.tem_como, self.tem_quem, self.tem_custo,
                    self.tem_prazo, self.tem_metrica, self.tem_fonte, self.tem_diagnostico])

    @property
    def status(self) -> StatusPolitica:
        # Verifica consenso primeiro
        negativos = sum(1 for v in self.satisfacao.values() if v < 0)
        if negativos > 3:
            return StatusPolitica.SEM_CONSENSO
        if self.score_gate == 7:
            return StatusPolitica.APROVADA
        elif self.score_gate >= 5:
            return StatusPolitica.JEQUERI
        else:
            return StatusPolitica.WO


def _init_politicas() -> List[PoliticaPublica]:
    return [

        # ================================================================
        # EIXO 1: VIOLENCIA (5 politicas)
        # ================================================================
        PoliticaPublica("vio1", "violencia", "Desmilitarizacao da PM",
            "Transicao em 4 fases: PM -> Policia Comunitaria Civil. Reciclagem. Conselhos populares.",
            True, True, True, True, True, True, True,
            "PCB", "PT",
            {"UP": 10, "PCB": 10, "PSOL": 10, "PSTU": 10, "PT": -5, "PDT": 0, "REDE": 3, "PCdoB": 5, "PCO": 8}),

        PoliticaPublica("vio2", "violencia", "Prevencao > Repressao",
            "Investir R$20bi/ano em esporte, cultura, emprego juvenil. Reduz homicidios 50% em 4 anos.",
            True, True, True, True, True, True, True,
            "PSOL", "PCdoB",
            {"UP": 9, "PCB": 8, "PSOL": 10, "PT": 7, "PDT": 6, "REDE": 8, "PCdoB": 9, "PSTU": 7, "PCO": 5}),

        PoliticaPublica("vio3", "violencia", "Controle de armas (desarmamento total)",
            "Compra compulsoria de armas. Fim do acesso civil. Recolhimento em 2 anos.",
            True, True, True, True, True, True, True,
            "PSOL", "PT",
            {"UP": 8, "PCB": 9, "PSOL": 10, "PT": 7, "PDT": -2, "REDE": 9, "PCdoB": 8, "PSTU": 9, "PCO": 7}),

        PoliticaPublica("vio4", "violencia", "Julgamento de corruptos com confisco",
            "Lei do Confisco Automatico. Cadeia hash. Canal de denuncia tamper-proof.",
            True, True, True, True, True, True, True,
            "UP", "PCdoB",
            {"UP": 10, "PCB": 9, "PSOL": 9, "PT": 5, "PDT": 6, "REDE": 8, "PCdoB": 9, "PSTU": 8, "PCO": 9}),

        PoliticaPublica("vio5", "violencia", "Punicao de torturadores da ditadura",
            "Revisao Lei da Anistia. Comissao da Verdade reativada.",
            False, True, True, False, False, True, True,
            "PCB", "PSOL",
            {"UP": 8, "PCB": 10, "PSOL": 10, "PT": 3, "PDT": 4, "REDE": 7, "PCdoB": 8, "PSTU": 10, "PCO": 10}),

        # ================================================================
        # EIXO 2: SAUDE (6 politicas)
        # ================================================================
        PoliticaPublica("sau1", "saude", "SUS 8% PIB",
            "Dobrar investimento: 4% -> 8% PIB. Fonte: ISF + fim subsidio planos.",
            True, True, True, True, True, True, True,
            "PCdoB", "PT",
            {"UP": 10, "PCB": 9, "PSOL": 10, "PT": 9, "PDT": 8, "REDE": 9, "PCdoB": 10, "PSTU": 9, "PCO": 8}),

        PoliticaPublica("sau2", "saude", "Fim dos planos privados",
            "Absorcao pelo SUS. Fim da exploracao. Modelo Cuba/chileno.",
            True, True, True, True, True, True, True,
            "UP", "PCdoB",
            {"UP": 10, "PCB": 10, "PSOL": 9, "PT": -3, "PDT": -2, "REDE": 4, "PCdoB": 9, "PSTU": 10, "PCO": 10}),

        PoliticaPublica("sau3", "saude", "Mais Medicos expandido",
            "Medico de familia em cada comunidade. Cooperacao Cuba.",
            True, True, True, True, True, True, True,
            "PCdoB", "PT",
            {"UP": 8, "PCB": 7, "PSOL": 9, "PT": 10, "PDT": 7, "REDE": 8, "PCdoB": 10, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("sau4", "saude", "Combate a dengue (vigilancia + vacina)",
            "Vacinacao massiva. Agente comunitario. Censo proprio de vetores.",
            True, True, True, True, True, True, True,
            "PCdoB", "PT",
            {"UP": 9, "PCB": 8, "PSOL": 9, "PT": 9, "PDT": 9, "REDE": 10, "PCdoB": 10, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("sau5", "saude", "Cannabis medicinal e canabidiol",
            "Prescricao pelo SUS. Producao estatal. Pesquisa ampliada.",
            True, True, True, True, True, True, True,
            "PSOL", "PCdoB",
            {"UP": 7, "PCB": 6, "PSOL": 10, "PT": 5, "PDT": 4, "REDE": 0, "PCdoB": 8, "PSTU": 6, "PCO": 5}),

        PoliticaPublica("sau6", "saude", "Triagem por urgencia (Raio X triage)",
            "Sistema de triagem em todo SUS. Fila <30 dias para eletivas.",
            True, True, True, True, True, True, True,
            "PT", "PCdoB",
            {"UP": 8, "PCB": 7, "PSOL": 8, "PT": 9, "PDT": 8, "REDE": 8, "PCdoB": 9, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 3: ALIMENTACAO (4 politicas)
        # ================================================================
        PoliticaPublica("ali1", "alimentacao", "PAA ampliado (R$5bi)",
            "Compra da agricultura familiar. CONSEA reativado. VIGISAN.",
            True, True, True, True, True, True, True,
            "REDE", "PT",
            {"UP": 10, "PCB": 9, "PSOL": 9, "PT": 10, "PDT": 8, "REDE": 10, "PCdoB": 9, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("ali2", "alimentacao", "Rastreio individual (crianca ate prato)",
            "Foto do prato + peso + frequencia escolar. Comprovacao multipla.",
            True, True, True, True, True, True, True,
            "UP", "PCdoB",
            {"UP": 10, "PCB": 8, "PSOL": 9, "PT": 8, "PDT": 7, "REDE": 9, "PCdoB": 9, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("ali3", "alimentacao", "Merenda escolar 100% local",
            "Compra direta de agricultor familiar. Fim de processados.",
            True, True, True, True, True, True, True,
            "REDE", "PT",
            {"UP": 9, "PCB": 9, "PSOL": 10, "PT": 8, "PDT": 7, "REDE": 10, "PCdoB": 9, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("ali4", "alimentacao", "BF R$700 + cesta garantida",
            "Bolsa Familia ampliado + cesta basica de direito.",
            True, True, True, True, True, True, True,
            "PT", "UP",
            {"UP": 9, "PCB": 8, "PSOL": 8, "PT": 10, "PDT": 7, "REDE": 8, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 4: AGUA (3 politicas)
        # ================================================================
        PoliticaPublica("agu1", "agua", "1M cisternas (R$3bi)",
            "Programa Cisternas ampliado. ASA Brasil. Semi-arido.",
            True, True, True, True, True, True, True,
            "REDE", "PT",
            {"UP": 9, "PCB": 8, "PSOL": 9, "PT": 9, "PDT": 8, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("agu2", "agua", "Saneamento estatizado",
            "Marco Legal revertido. Estatizacao. 90% esgoto em 4 anos.",
            True, True, True, True, True, True, True,
            "PT", "PDT",
            {"UP": 9, "PCB": 9, "PSOL": 8, "PT": 9, "PDT": 9, "REDE": 9, "PCdoB": 8, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("agu3", "agua", "Fim do mercúrio (garimpos)",
            "Desativacao de garimpos. Remediação. Forca Nacional.",
            True, True, True, True, True, True, True,
            "REDE", "PSOL",
            {"UP": 9, "PCB": 8, "PSOL": 10, "PT": 7, "PDT": 6, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 5: SOBERANIA ALIMENTAR (3 politicas)
        # ================================================================
        PoliticaPublica("sob1", "soberania_alimentar", "Producao nacional de trigo",
            "Centro-Oeste. Pesquisa EMBRAPA. Meta: 50% nacional em 4 anos.",
            True, True, True, True, True, True, True,
            "UP", "PT",
            {"UP": 10, "PCB": 9, "PSOL": 8, "PT": 9, "PDT": 8, "REDE": 9, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("sob2", "soberania_alimentar", "Fertilizantes nacionais",
            "Fosfato e potassio nacional. Fim da importacao (80% hoje).",
            True, True, True, True, True, True, True,
            "PCB", "PDT",
            {"UP": 9, "PCB": 10, "PSOL": 7, "PT": 8, "PDT": 9, "REDE": 8, "PCdoB": 7, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("sob3", "soberania_alimentar", "Banco de sementes crioulas",
            "Banco publico de sementes. Fim do monopoly de transgenicos.",
            True, True, True, True, True, True, True,
            "UP", "REDE",
            {"UP": 10, "PCB": 8, "PSOL": 9, "PT": 6, "PDT": 5, "REDE": 9, "PCdoB": 7, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 6: EDUCACAO (5 politicas)
        # ================================================================
        PoliticaPublica("edu1", "educacao", "Escola integral 7h-17h",
            "Dia integral com alimentacao. 50% das escolas em 2 anos.",
            True, True, True, True, True, True, True,
            "PCdoB", "PT",
            {"UP": 10, "PCB": 9, "PSOL": 10, "PT": 9, "PDT": 8, "REDE": 9, "PCdoB": 10, "PSTU": 9, "PCO": 8}),

        PoliticaPublica("edu2", "educacao", "Piso nacional professor R$8k",
            "Professor com salário base R$8.000. Uma escola só.",
            True, True, True, True, True, True, True,
            "PT", "PCdoB",
            {"UP": 9, "PCB": 10, "PSOL": 10, "PT": 9, "PDT": 7, "REDE": 8, "PCdoB": 10, "PSTU": 10, "PCO": 9}),

        PoliticaPublica("edu3", "educacao", "Fim do vestibular",
            "Acesso livre a universidade. Cotas raciais e de classe.",
            True, True, True, True, True, True, True,
            "UP", "PSOL",
            {"UP": 10, "PCB": 9, "PSOL": 10, "PT": 7, "PDT": 5, "REDE": 7, "PCdoB": 9, "PSTU": 9, "PCO": 8}),

        PoliticaPublica("edu4", "educacao", "Censo escolar proprio",
            "Verificar cada escola. Ghost detection. 178.459 escolas.",
            True, True, True, True, True, True, True,
            "REDE", "PT",
            {"UP": 9, "PCB": 8, "PSOL": 8, "PT": 8, "PDT": 8, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("edu5", "educacao", "Educacao politico-popular",
            "Cordel, capoeira, antropofagia no curriculo. P1-P14.",
            True, True, True, True, True, True, True,
            "PCB", "PSOL",
            {"UP": 9, "PCB": 10, "PSOL": 10, "PT": 5, "PDT": 4, "REDE": 7, "PCdoB": 8, "PSTU": 9, "PCO": 8}),

        # ================================================================
        # EIXO 7: EMPREGO (4 politicas)
        # ================================================================
        PoliticaPublica("emp1", "emprego", "Emprego garantido pelo Estado",
            "Programa Nacional de Emprego Popular. Obras de infraestrutura.",
            True, True, True, True, True, True, True,
            "PCB", "PT",
            {"UP": 10, "PCB": 10, "PSOL": 9, "PT": 7, "PDT": 3, "REDE": 7, "PCdoB": 8, "PSTU": 10, "PCO": 9}),

        PoliticaPublica("emp2", "emprego", "Jornada 6h + aumento salarial",
            "Reducao gradual 44h -> 30h. Salario minimo indexado ao PIB.",
            True, True, True, True, True, True, True,
            "PCB", "PSTU",
            {"UP": 10, "PCB": 10, "PSOL": 9, "PT": 6, "PDT": 2, "REDE": 7, "PCdoB": 8, "PSTU": 10, "PCO": 9}),

        PoliticaPublica("emp3", "emprego", "Fim da terceirizacao",
            "Proibicao total. CLT reformada. Trabalho digno.",
            True, True, True, True, True, True, True,
            "PSTU", "PCdoB",
            {"UP": 9, "PCB": 9, "PSOL": 10, "PT": 5, "PDT": -2, "REDE": 7, "PCdoB": 9, "PSTU": 10, "PCO": 8}),

        PoliticaPublica("emp4", "emprego", "Renda minima R$2.600",
            "Quem trabalha recebe no minimo R$2.600. Estado complementa.",
            True, True, True, True, True, True, True,
            "UP", "PT",
            {"UP": 10, "PCB": 9, "PSOL": 9, "PT": 8, "PDT": 6, "REDE": 8, "PCdoB": 9, "PSTU": 9, "PCO": 8}),

        # ================================================================
        # EIXO 8: ECONOMIA (6 politicas)
        # ================================================================
        PoliticaPublica("eco1", "economia", "Nacionalizacao bancaria",
            "BNDES + Caixa absorvem. Fim do oligopolio. Spread <5%.",
            True, True, True, True, True, True, True,
            "PCB", "UP",
            {"UP": 10, "PCB": 10, "PSOL": 9, "PT": -5, "PDT": -3, "REDE": 3, "PCdoB": 5, "PSTU": 10, "PCO": 10}),

        PoliticaPublica("eco2", "economia", "Imposto sobre grandes fortunas",
            "ISF: 1% sobre patrimonio > R$10M. Lucros/dividendos tributados.",
            True, True, True, True, True, True, True,
            "PCB", "PT",
            {"UP": 10, "PCB": 10, "PSOL": 10, "PT": 7, "PDT": 5, "REDE": 8, "PCdoB": 9, "PSTU": 10, "PCO": 10}),

        PoliticaPublica("eco3", "economia", "Auditoria da divida publica",
            "Auditoria cidada (modelo Equador). Suspensao durante auditoria.",
            True, True, True, True, True, True, True,
            "UP", "PCB",
            {"UP": 10, "PCB": 10, "PSOL": 9, "PT": 3, "PDT": 2, "REDE": 6, "PCdoB": 7, "PSTU": 10, "PCO": 10}),

        PoliticaPublica("eco4", "economia", "Planificacao economica",
            "Conselhos populares setoriais. Plano qüinqüenal. Dados abertos.",
            True, True, True, True, True, True, True,
            "PCB", "UP",
            {"UP": 10, "PCB": 10, "PSOL": 8, "PT": -2, "PDT": -1, "REDE": 5, "PCdoB": 6, "PSTU": 9, "PCO": 10}),

        PoliticaPublica("eco5", "economia", "Fim das remessas de lucro",
            "Anulacao de acordos com credores estrangeiros. Comercio Sul-Sul.",
            True, True, True, True, True, True, True,
            "PCB", "PDT",
            {"UP": 10, "PCB": 10, "PSOL": 8, "PT": -3, "PDT": 3, "REDE": 6, "PCdoB": 6, "PSTU": 10, "PCO": 10}),

        PoliticaPublica("eco6", "economia", "Reforma agraria popular",
            "Nacionalizacao da terra. Fim do latifundio. Cooperativas.",
            True, True, True, True, True, True, True,
            "UP", "PCB",
            {"UP": 10, "PCB": 10, "PSOL": 9, "PT": 4, "PDT": -3, "REDE": 8, "PCdoB": 7, "PSTU": 9, "PCO": 8}),

        # ================================================================
        # EIXO 9: AMBIENTE (4 politicas)
        # ================================================================
        PoliticaPublica("amb1", "ambiente", "PPCDAm reativado",
            "Comando unificado. Fiscalizacao por satelite. Desmatamento zero.",
            True, True, True, True, True, True, True,
            "REDE", "PSOL",
            {"UP": 9, "PCB": 8, "PSOL": 10, "PT": 8, "PDT": 7, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("amb2", "ambiente", "Controle popular da Amazonia",
            "Ribeirinhos e indigenas no comando. Garimpos desativados.",
            True, True, True, True, True, True, True,
            "PSOL", "REDE",
            {"UP": 9, "PCB": 8, "PSOL": 10, "PT": 7, "PDT": 6, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("amb3", "ambiente", "Economia extrativista sustentavel",
            "Castanha, borracha, acai. Cooperativas. R$5bi/ano.",
            True, True, True, True, True, True, True,
            "REDE", "UP",
            {"UP": 9, "PCB": 8, "PSOL": 9, "PT": 8, "PDT": 7, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("amb4", "ambiente", "Transicao energetica",
            "Solar + eolica. Fim termoeletricas. R$30bi investimento.",
            True, True, True, True, True, True, True,
            "REDE", "PDT",
            {"UP": 9, "PCB": 8, "PSOL": 9, "PT": 8, "PDT": 9, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 10: INDIGENA (3 politicas)
        # ================================================================
        PoliticaPublica("ind1", "indigena", "Demarcacao das 251 terras",
            "Aceleracao. Forca Nacional. 2 anos.",
            True, True, True, True, True, True, True,
            "PSOL", "REDE",
            {"UP": 10, "PCB": 9, "PSOL": 10, "PT": 7, "PDT": 6, "REDE": 9, "PCdoB": 8, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("ind2", "indigena", "Saude indigena (DSEI)",
            "DSEI fortalecido. Yanomami emergencia. Mercurio zero.",
            True, True, True, True, True, True, True,
            "PSOL", "PCdoB",
            {"UP": 9, "PCB": 8, "PSOL": 10, "PT": 8, "PDT": 7, "REDE": 9, "PCdoB": 10, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("ind3", "indigena", "Educacao bilíngue",
            "Escolas indigenas com curriculo proprio. 274 línguas.",
            True, True, True, True, True, True, True,
            "PSOL", "PCdoB",
            {"UP": 9, "PCB": 8, "PSOL": 10, "PT": 7, "PDT": 6, "REDE": 9, "PCdoB": 9, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 11: AGROPECUARIA (3 politicas)
        # ================================================================
        PoliticaPublica("agr1", "agropecuaria", "Reforma agraria (nacionalizacao)",
            "Fim do latifundio. 500 mil familias assentadas. Cooperativas.",
            True, True, True, True, True, True, True,
            "UP", "PCB",
            {"UP": 10, "PCB": 10, "PSOL": 9, "PT": 5, "PDT": -3, "REDE": 8, "PCdoB": 7, "PSTU": 9, "PCO": 8}),

        PoliticaPublica("agr2", "agropecuaria", "Agricultura familiar (PAA+)",
            "Compra garantida. Crédito. Cooperativas. Sem agrotóxico.",
            True, True, True, True, True, True, True,
            "REDE", "PT",
            {"UP": 9, "PCB": 8, "PSOL": 9, "PT": 9, "PDT": 7, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("agr3", "agropecuaria", "Fim dos agrotóxicos",
            "Proibicao gradual. Agroecologia. EMBRAPA organico.",
            True, True, True, True, True, True, True,
            "REDE", "PSOL",
            {"UP": 9, "PCB": 8, "PSOL": 10, "PT": 6, "PDT": -2, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 12: ENERGIA (3 politicas)
        # ================================================================
        PoliticaPublica("ene1", "energia", "Reestatização (Petrobras 100%)",
            "Recompra de ações. Fim dos leilões. R$80bi.",
            True, True, True, True, True, True, True,
            "PCB", "PT",
            {"UP": 10, "PCB": 10, "PSOL": 9, "PT": -2, "PDT": 7, "REDE": 8, "PCdoB": 7, "PSTU": 10, "PCO": 9}),

        PoliticaPublica("ene2", "energia", "Tarifa social universal",
            "Energia como direito. Tarifa subsidiada para baixa renda.",
            True, True, True, True, True, True, True,
            "PT", "PCdoB",
            {"UP": 9, "PCB": 8, "PSOL": 9, "PT": 10, "PDT": 9, "REDE": 9, "PCdoB": 10, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("ene3", "energia", "Solar comunitária (favelas)",
            "Painéis solares em telhados de favela. Cooperativa de energia.",
            True, True, True, True, True, True, True,
            "REDE", "PSOL",
            {"UP": 9, "PCB": 7, "PSOL": 10, "PT": 8, "PDT": 8, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 13: TRANSPORTE (3 politicas)
        # ================================================================
        PoliticaPublica("tra1", "transporte", "Estatização + tarifa zero",
            "Municipios assumem onibus. Federalizacao trens. R$40bi/ano.",
            True, True, True, True, True, True, True,
            "UP", "PDT",
            {"UP": 10, "PCB": 9, "PSOL": 9, "PT": 7, "PDT": 8, "REDE": 8, "PCdoB": 8, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("tra2", "transporte", "Frota elétrica nacional",
            "Onibus eletrico BR. Cobalt/Comil. R$15bi.",
            True, True, True, True, True, True, True,
            "PDT", "PCB",
            {"UP": 8, "PCB": 9, "PSOL": 9, "PT": 8, "PDT": 10, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("tra3", "transporte", "Ferrovias (carga + passageiro)",
            "Recuperacao da malha ferroviria. 10mil km novos.",
            True, True, True, True, True, True, True,
            "PDT", "PT",
            {"UP": 8, "PCB": 8, "PSOL": 8, "PT": 9, "PDT": 10, "REDE": 8, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 14: HABITACAO (3 politicas)
        # ================================================================
        PoliticaPublica("hab1", "habitacao", "Imoveis vazios para deficit",
            "Notificacao (uso ou perda). 2 milhoes de imoveis em capitais.",
            True, True, True, True, True, True, True,
            "UP", "PT",
            {"UP": 10, "PCB": 10, "PSOL": 10, "PT": 5, "PDT": 4, "REDE": 8, "PCdoB": 8, "PSTU": 9, "PCO": 8}),

        PoliticaPublica("hab2", "habitacao", "4 milhoes de moradias",
            "Construcao popular. Cooperativas. Caixa financiando.",
            True, True, True, True, True, True, True,
            "PT", "PDT",
            {"UP": 9, "PCB": 8, "PSOL": 9, "PT": 10, "PDT": 9, "REDE": 8, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("hab3", "habitacao", "Reforma urbana",
            "Plano diretor popular. Fim de especulação imobiliaria.",
            True, True, True, True, True, True, True,
            "UP", "PSOL",
            {"UP": 10, "PCB": 9, "PSOL": 10, "PT": 6, "PDT": 5, "REDE": 8, "PCdoB": 8, "PSTU": 8, "PCO": 7}),

        # ================================================================
        # EIXO 15: SANEAMENTO (2 politicas)
        # ================================================================
        PoliticaPublica("san1", "saneamento", "Estatização (reverter Marco Legal)",
            "Fim das concessoes privadas. Estatizacao. 90% em 4 anos.",
            True, True, True, True, True, True, True,
            "PT", "PDT",
            {"UP": 9, "PCB": 10, "PSOL": 9, "PT": 9, "PDT": 9, "REDE": 9, "PCdoB": 9, "PSTU": 9, "PCO": 8}),

        PoliticaPublica("san2", "saneamento", "Coleta de lixo universal",
            "Coleta seletiva. Compostagem. Reciclagem cooperativada.",
            True, True, True, True, True, True, True,
            "REDE", "PT",
            {"UP": 9, "PCB": 8, "PSOL": 9, "PT": 9, "PDT": 8, "REDE": 10, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        # ================================================================
        # EIXO 16: DROGAS (3 politicas)
        # ================================================================
        PoliticaPublica("dro1", "drogas", "Reducao de danos",
            "Caps AD expandidos. Equipes de rua. Naloxona gratuita.",
            True, True, True, True, True, True, True,
            "PSOL", "PCdoB",
            {"UP": 8, "PCB": 7, "PSOL": 10, "PT": 6, "PDT": 5, "REDE": 4, "PCdoB": 9, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("dro2", "drogas", "Descriminalizacao do uso",
            "Fim da criminalizacao. Tratamento, nao prisao.",
            True, True, True, True, True, True, True,
            "PSOL", "PCdoB",
            {"UP": 8, "PCB": 7, "PSOL": 10, "PT": 5, "PDT": 3, "REDE": 0, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("dro3", "drogas", "Legalizacao da maconha",
            "Producao regulada. Venda em farmacia. Sem trafico armado.",
            False, True, True, False, True, True, True,
            "PSOL", "UP",
            {"UP": 7, "PCB": 6, "PSOL": 10, "PT": 3, "PDT": 2, "REDE": -2, "PCdoB": 7, "PSTU": 6, "PCO": 5}),

        # ================================================================
        # EIXO 17: CULTURA (3 politicas)
        # ================================================================
        PoliticaPublica("cul1", "cultura", "Cotizacao 40% nacional",
            "Lei de conteudo nacional. Radio/TV/streaming. 40% minimo.",
            True, True, True, True, True, True, True,
            "PCB", "PSOL",
            {"UP": 9, "PCB": 10, "PSOL": 10, "PT": 6, "PDT": 5, "REDE": 8, "PCdoB": 9, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("cul2", "cultura", "Financiamento publico direto",
            "Fim das leis de incentivo (renuncia fiscal). Bolsa direta.",
            True, True, True, True, True, True, True,
            "PSOL", "PCB",
            {"UP": 9, "PCB": 9, "PSOL": 10, "PT": 7, "PDT": 6, "REDE": 8, "PCdoB": 9, "PSTU": 8, "PCO": 7}),

        PoliticaPublica("cul3", "cultura", "Cordel + capoeira no curriculo",
            "Antropofagia. P1-P14. Identidade nacional popular.",
            True, True, True, True, True, True, True,
            "PCB", "PSOL",
            {"UP": 9, "PCB": 10, "PSOL": 10, "PT": 5, "PDT": 4, "REDE": 7, "PCdoB": 8, "PSTU": 9, "PCO": 8}),

        # ================================================================
        # EIXO 18: COMUNICACAO (3 politicas)
        # ================================================================
        PoliticaPublica("com1", "comunicacao", "Democratizacao da mídia",
            "Fim do monopolio. Quebra de 6 grupos. Concessoes publicas.",
            True, True, True, True, True, True, True,
            "PCB", "PSOL",
            {"UP": 10, "PCB": 10, "PSOL": 10, "PT": 4, "PDT": 5, "REDE": 8, "PCdoB": 7, "PSTU": 9, "PCO": 8}),

        PoliticaPublica("com2", "comunicacao", "Internet universal (5G rural)",
            "35% da zona rural sem internet. 5G gratuito. R$5bi.",
            True, True, True, True, True, True, True,
            "PT", "PDT",
            {"UP": 9, "PCB": 8, "PSOL": 9, "PT": 9, "PDT": 9, "REDE": 9, "PCdoB": 8, "PSTU": 7, "PCO": 6}),

        PoliticaPublica("com3", "comunicacao", "Fim das doacoes empresariais",
            "Financiamento 100% publico de campanhas. Fim PJ.",
            True, True, True, True, True, True, True,
            "UP", "PSOL",
            {"UP": 10, "PCB": 9, "PSOL": 10, "PT": 5, "PDT": 4, "REDE": 8, "PCdoB": 8, "PSTU": 9, "PCO": 8}),
    ]


class SimulacaoMultipla:
    """Simula satisfacao com multiplas politicas por eixo."""

    def __init__(self):
        self.politicas = _init_politicas()

    def politicas_por_eixo(self) -> Dict[str, List[PoliticaPublica]]:
        resultado = defaultdict(list)
        for p in self.politicas:
            resultado[p.eixo].append(p)
        return dict(resultado)

    def satisfacao_por_partido(self) -> Dict[str, Dict[str, Any]]:
        """Satisfacao agregada por partido em todas as politicas."""
        todos_partidos = set()
        for p in self.politicas:
            todos_partidos.update(p.satisfacao.keys())

        resultado = {}
        for partido in todos_partidos:
            scores = []
            cedeu_count = 0
            ganhou_count = 0
            for p in self.politicas:
                s = p.satisfacao.get(partido, 0)
                scores.append(s)
                if s < 0:
                    cedeu_count += 1
                elif s >= 8:
                    ganhou_count += 1

            media = sum(scores) / len(scores) if scores else 0
            total_positivo = sum(1 for s in scores if s > 0)
            pct_satisfacao = (total_positivo / len(scores) * 100) if scores else 0

            resultado[partido] = {
                "media_satisfacao": round(media, 1),
                "ganhou": ganhou_count,
                "neutro": sum(1 for s in scores if 1 <= s < 8),
                "cede": cedeu_count,
                "pct_satisfacao": round(pct_satisfacao, 1),
                "n_politicas": len(scores),
            }

        return dict(sorted(resultado.items(), key=lambda x: x[1]["media_satisfacao"], reverse=True))

    def status_por_eixo(self) -> Dict[str, Dict[str, Any]]:
        """Status de cada eixo: quantas aprovadas, quantas WO."""
        por_eixo = self.politicas_por_eixo()
        resultado = {}
        for eixo, pols in por_eixo.items():
            aprovadas = sum(1 for p in pols if p.status == StatusPolitica.APROVADA)
            jequeri = sum(1 for p in pols if p.status == StatusPolitica.JEQUERI)
            wo = sum(1 for p in pols if p.status == StatusPolitica.WO)
            sem_consenso = sum(1 for p in pols if p.status == StatusPolitica.SEM_CONSENSO)
            resolvido = aprovadas == len(pols)
            resultado[eixo] = {
                "total": len(pols),
                "aprovadas": aprovadas,
                "jequeri": jequeri,
                "wo": wo,
                "sem_consenso": sem_consenso,
                "resolvido": resolvido,
            }
        return resultado

    def scorecard(self) -> Dict[str, Any]:
        n_pol = len(self.politicas)
        n_aprov = sum(1 for p in self.politicas if p.status == StatusPolitica.APROVADA)
        n_wo = sum(1 for p in self.politicas if p.status == StatusPolitica.WO)
        sat = self.satisfacao_por_partido()
        sat_media = sum(s["media_satisfacao"] for s in sat.values()) / len(sat) if sat else 0
        eixos = self.status_por_eixo()
        n_resolvidos = sum(1 for e in eixos.values() if e["resolvido"])
        return {
            "modulo": "open_simulacao_multipla",
            "versao": "0.1.0-spec",
            "politicas_total": n_pol,
            "aprovadas": n_aprov,
            "wo": n_wo,
            "eixos_resolvidos": n_resolvidos,
            "eixos_total": len(eixos),
            "satisfacao_media": round(sat_media, 1),
            "partidos": len(sat),
        }


def _demo():
    sim = SimulacaoMultipla()
    sc = sim.scorecard()
    sat = sim.satisfacao_por_partido()
    eixos = sim.status_por_eixo()

    print("=" * 90)
    print("SIMULACAO MULTI-POLITICA — FRENTE COMUNISTA UNIDA")
    print(f"{sc['politicas_total']} politicas x {sc['eixos_total']} eixos x {sc['partidos']} partidos")
    print("=" * 90)

    print(f"\nPoliticas aprovadas: {sc['aprovadas']}/{sc['politicas_total']}")
    print(f"Eixos resolvidos (100%): {sc['eixos_resolvidos']}/{sc['eixos_total']}")
    print(f"Satisfacao media: {sc['satisfacao_media']}/10")

    print(f"\n{'='*90}")
    print("SATISFACAO POR PARTIDO")
    print(f"{'='*90}")
    print(f"\n{'PARTIDO':<10} {'MEDIA':>6} {'GANHOU':>8} {'NEUTRO':>8} {'CEDEU':>6} {'%SAT':>6}")
    print("-" * 50)
    for partido, s in sat.items():
        flag = " *** TENSAO" if s["media_satisfacao"] < 5 else ""
        print(f"  {partido:<8} {s['media_satisfacao']:>6.1f} {s['ganhou']:>8} {s['neutro']:>8} {s['cede']:>6} {s['pct_satisfacao']:>5.1f}%{flag}")

    print(f"\n{'='*90}")
    print("STATUS POR EIXO")
    print(f"{'='*90}")
    print(f"\n{'EIXO':<25} {'TOTAL':>6} {'APROV':>6} {'JEQ':>5} {'WO':>5} {'RESOLVIDO':>10}")
    print("-" * 65)
    for eixo, st in eixos.items():
        flag = " *** SIM" if st["resolvido"] else " *** NAO"
        print(f"  {eixo:<23} {st['total']:>6} {st['aprovadas']:>6} {st['jequeri']:>5} {st['wo']:>5} {flag}")

    print(f"\n{'='*90}")
    print("POLITICAS COM TENSAO (alguem cedeu, satisfacao < 0)")
    print(f"{'='*90}")
    for p in sim.politicas:
        cededores = [(partido, sat_v) for partido, sat_v in p.satisfacao.items() if sat_v < 0]
        if cededores:
            print(f"\n  [{p.eixo.upper()}] {p.titulo}")
            print(f"    Status: {p.status.value} | Lider: {p.partido_lider} | Executor: {p.partido_executor}")
            for partido, sat_v in cededores:
                print(f"    CEDEU: {partido} (satisfacao: {sat_v})")

    print(f"\n{'='*90}")
    print("VEREDITO")
    print(f"{'='*90}")
    print(f"""
  {sc['politicas_total']} politicas publicas avaliadas.
  {sc['aprovadas']} aprovadas no Gate WO (7/7).
  {sc['eixos_resolvidos']} de {sc['eixos_total']} eixos RESOLVIDOS (100% politicas aprovadas).
  Satisfacao media da coalizao: {sc['satisfacao_media']}/10

  QUEM FICA MAIS FELIZ:
""")
    for partido, s in list(sat.items())[:3]:
        print(f"    {partido:<8} media={s['media_satisfacao']:.1f} ({s['ganhou']} ganhou, {s['cede']} cedeu)")

    print(f"""
  QUEM ENGOLE SAPO:
""")
    for partido, s in list(sat.items())[-3:]:
        print(f"    {partido:<8} media={s['media_satisfacao']:.1f} ({s['ganhou']} ganhou, {s['cede']} cedeu)")

    # Ruptura
    risco = [p for p, s in sat.items() if s["media_satisfacao"] < 4]
    print(f"""
  RISCO DE RUPTURA:
""")
    if risco:
        for p in risco:
            print(f"    *** {p} -- ALTO RISCO")
    else:
        print(f"    Nenhum partido abaixo de 4.0. Coalizao estavel.")


if __name__ == "__main__":
    _demo()
