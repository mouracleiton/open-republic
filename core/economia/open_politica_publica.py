#!/usr/bin/env python3
"""
OpenPoliticaPublica -- Mapeamento de Politicas Publicas vs Raio X
==================================================================
"Cada exame do Raio X tem uma (ou varias) politicas publicas
 que deveriam resolver o problema. Funcionam?"
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple


class Eficiencia(Enum):
    """Eficiencia: o programa entrega o prometido com os recursos que tem?"""
    ALTA = "alta"          # baixo custo, alto resultado
    MEDIA = "media"        # custo razoavel, resultado razoavel
    BAIXA = "baixa"        # caro, pouco resultado
    NULA = "nula"          # dinheiro gasto, zero resultado observavel
    CONTRAPRODUTIVA = "contra"  # piora o problema

    @property
    def rotulo(self) -> str:
        return {
            "alta": "Eficiente (baixo custo, alto impacto)",
            "media": "Razoavel (custo proporcional ao impacto)",
            "baixa": "Ineficiente (caro, pouco resultado)",
            "nula": "Nulo (dinheiro gasto, sem resultado)",
            "contra": "Contraprodutiva (piora o problema)",
        }[self.value]


class Eficacia(Enum):
    """Eficacia: o programa resolve o problema de fato?"""
    RESOLVE = "resolve"              # resolve ou quase resolve
    PARCIAL = "parcial"              # resolve em parte
    MINIMA = "minima"               # pouco impacto
    NAO_RESOLVE = "nao_resolve"      # nao resolve
    PIORA = "piora"                 # problema piorou

    @property
    def rotulo(self) -> str:
        return {
            "resolve": "Resolve (problema diminuiu significativamente)",
            "parcial": "Parcial (ajuda mas nao resolve)",
            "minima": "Minima (impacto marginal)",
            "nao_resolve": "Nao resolve (problema persiste)",
            "piora": "Piorou (problema aumentou)",
        }[self.value]


@dataclass
class PoliticaPublica:
    """Uma politica/programa/publico do governo mapeado a um exame do Raio X."""
    nome: str
    dominio_raiox: str          # qual dos 18 dominios
    esfera: str                  # federal, estadual, municipal
    orcamento_anual: str         # R$ estimado
    publico_alvo: str            # quem deveria atingir
    alcance_real: str            # quem realmente atinge
    eficiencia: Eficiencia
    eficacia: Eficacia
    dado_impacto: str            # o que o dado diz sobre resultado
    gap: str                     # o que nao cobre
    ano_criacao: int
    status: str = "ativo"        # ativo, suspenso, extinto


@dataclass
class DiagnosticoPolitica:
    """Veredito por dominio do Raio X."""
    dominio: str
    politicas: List[PoliticaPublica] = field(default_factory=list)

    @property
    def veredito(self) -> str:
        if not self.politicas:
            return "SEM POLITICA PUBLICA"
        ef = [p.eficacia for p in self.politicas]
        if any(e == Eficacia.PIORA for e in ef):
            return "FALHOU (problema piorou)"
        if all(e == Eficacia.RESOLVE for e in ef):
            return "RESOLVE"
        if any(e == Eficacia.RESOLVE for e in ef):
            return "PARCIAL (alguma funciona)"
        if any(e == Eficacia.PARCIAL for e in ef):
            return "PARCIAL"
        if all(e in (Eficacia.NAO_RESOLVE, Eficacia.MINIMA) for e in ef):
            return "FALHOU (nao resolve)"
        return "INDEFINIDO"

    @property
    def orcamento_total(self) -> str:
        return f"ver orcamento_individual"


class PoliticaPublicaMapper:
    """
    Mapeia os 18 dominios do Raio X as politicas publicas existentes.
    """

    def __init__(self):
        self.diagnosticos: Dict[str, DiagnosticoPolitica] = {}
        self._init_diagnosticos()

    def _init_diagnosticos(self):
        dados = self._dados_completos()
        for d in dados:
            dom = d["dominio"]
            if dom not in self.diagnosticos:
                self.diagnosticos[dom] = DiagnosticoPolitica(dominio=dom)
            self.diagnosticos[dom].politicas.append(PoliticaPublica(
                nome=d["nome"], dominio_raiox=dom,
                esfera=d["esfera"], orcamento_anual=d["orcamento"],
                publico_alvo=d["publico"], alcance_real=d["alcance"],
                eficiencia=Eficiencia(d["eficiencia"]),
                eficacia=Eficacia(d["eficacia"]),
                dado_impacto=d["impacto"], gap=d["gap"],
                ano_criacao=d["ano"], status=d.get("status", "ativo"),
            ))

    def _dados_completos(self) -> List[Dict[str, Any]]:
        return [

            # === 1. VIOLENCIA ===
            {"dominio": "violencia", "nome": "SINESP (Sistema Nacional de Informacoes de Seguranca Publica)",
             "esfera": "Federal", "orcamento": "R$ 300M/ano",
             "publico": "Toda populacao (dados de seguranca em tempo real)",
             "alcance": "Dados com 6-12h de atraso. 40% dos municipios nao alimentam o sistema.",
             "eficiencia": "baixa", "eficacia": "minima",
             "impacto": "Taxa de homicidios: 21.7/100k (2023). Caiu 3% em 5 anos. SINESP nao previne, so conta.",
             "gap": "NAO da alerta em tempo real. NAO cobre violencia domestica (subnotificada ~70%).",
             "ano": 2004},
            {"dominio": "violencia", "nome": "PRONASCI / Mais Seguranca",
             "esfera": "Federal", "orcamento": "R$ 3.8 bi (total historico)",
             "publico": "Jovens em situacao de risco + forcas de seguranca",
             "alcance": "Descontinuado em varios estados. Cobertura <10% do publico alvo.",
             "eficiencia": "baixa", "eficacia": "minima",
             "impacto": "Estudos mostram zero impacto em homicidios nas areas atendidas.",
             "gap": "Foco em repressao, nao em prevencao. Ignora causas (fome, escola, emprego).",
             "ano": 2007, "status": "reformulado"},
            {"dominio": "violencia", "nome": "Lei Maria da Penha (Lei 11.340/2006)",
             "esfera": "Federal", "orcamento": "~R$ 500M/ano (implementacao)",
             "publico": "Mulheres em situacao de violencia",
             "alcance": "1.8 milhoes de medidas protetivas/ano. Mas so 30% dos casos sao denunciados.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Homicidio de mulheres subiu 4% (2019-2023). Lei e boa, execucao falha.",
             "gap": "Faltam abrigos (so 198 no Brasil). Cumprimento de medidas protetivas ~40%.",
             "ano": 2006},
            {"dominio": "violencia", "nome": "Brasil Seguro (Plano Nacional)",
             "esfera": "Federal", "orcamento": "R$ 4.5 bi/ano",
             "publico": "Estados com altos indices de violencia",
             "alcance": "Repasse a estados. Sem metricas claras de resultado.",
             "eficiencia": "baixa", "eficacia": "minima",
             "impacto": "Norte/Nordeste continuam com homicidios subindo. Dinheiro sem accountability.",
             "gap": "Sem meta mensuravel. Dinheiro entra, violencia continua.",
             "ano": 2022},

            # === 2. SAUDE ===
            {"dominio": "saude", "nome": "SUS (Sistema Unico de Saude)",
             "esfera": "Federal/Estadual/Municipal", "orcamento": "R$ 280 bi/ano",
             "publico": "215 milhoes de brasileiros",
             "alcance": "75% da populacao DEPENDE exclusivamente do SUS. 25% tem plano.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Cobertura vacinal caiu de 95% (2015) para 68% (2023). Fila SUS nao existe como metrica. Dengue 2024: 6M casos.",
             "gap": "Subfinanciamento cronico (gasta 4% do PIB vs 8% OCDE). Faltam medicos no interior.",
             "ano": 1988},
            {"dominio": "saude", "nome": "Mais Medicos",
             "esfera": "Federal", "orcamento": "R$ 5 bi/ano",
             "publico": "Areas remotas e periferias",
             "alcance": "~18 mil medicos em ~4 mil municipos.",
             "eficiencia": "alta", "eficacia": "parcial",
             "impacto": "Reduziu mortalidade infantil nas areas atendidas em ~15%.",
             "gap": "Programa interrompido em 2023 (expulsao de medicos cubanos). Retomado parcial.",
             "ano": 2013, "status": "ativo"},
            {"dominio": "saude", "nome": "Programa Nacional de Imunizacoes (PNI)",
             "esfera": "Federal", "orcamento": "R$ 8 bi/ano",
             "publico": "215 milhoes",
             "alcance": "Historicamente >90%. 2023: 68% (calendario basico).",
             "eficiencia": "alta", "eficacia": "parcial",
             "impacto": "Eradicou polio, sarampo (reapareceu 2018-2020). Queda de cobertura e emergencia.",
             "gap": "Anti-vax + desinformacao + falta de campanha. Cobertura caindo desde 2016.",
             "ano": 1973},

            # === 3. ALIMENTACAO ===
            {"dominio": "alimentacao", "nome": "Bolsa Familia (novo)",
             "esfera": "Federal", "orcamento": "R$ 36 bi/ano",
             "publico": "~21 milhoes de familias (~55 milhoes)",
             "alcance": "~80% das familias elegiveis. 20% ainda sem cadastrar.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Fome caiu de 33M (2022) para ~33M (2024). NAo mudou. Dinheiro entra, fome continua.",
             "gap": "NAO garante que dinheiro vire comida. ~17% das familias ainda passam fome.",
             "ano": 2003},
            {"dominio": "alimentacao", "nome": "PNAE (Merenda Escolar)",
             "esfera": "Federal", "orcamento": "R$ 2.5 bi/ano",
             "publico": "~40 milhoes de alunos",
             "alcance": "Cobre todas escolas publicas. Mas 1.6M criancas fora da escola = sem merenda.",
             "eficiencia": "alta", "eficacia": "parcial",
             "impacto": "Garante 1 refeicao/dia para 40M criancas. Custo R$0.36/aluno/dia.",
             "gap": "Crianca que falta nao come. Terceirizacao em 70% dos municipios. Qualidade duvidosa.",
             "ano": 1955},

            # === 4. AGUA ===
            {"dominio": "agua", "nome": "Novo Marco Legal do Saneamento (Lei 14.026/2020)",
             "fera": "Federal", "esfera": "Federal",
             "orcamento": "R$ 700 bi (meta 20 anos)",
             "publico": "Toda populacao",
             "alcance": "84% agua tratada (urbano). Rural: ~40%. Sertao: <30%.",
             "eficiencia": "baixa", "eficacia": "minima",
             "impacto": "Meta: 99% agua ate 2033. Ritmo atual: 0.5%/ano. Chegara em 2050.",
             "gap": "Privatizou sem fiscalizar. Tarifa subiu. Rural IGNORADO pela lei.",
             "ano": 2020},
            {"dominio": "agua", "nome": "Programa Agua Doce / Cisternas",
             "esfera": "Federal", "orcamento": "R$ 500M/ano",
             "publico": "Sertao nordestino",
             "alcance": "~1 milhoao de cisternas instaladas (P1MC + P1+2). Demanda: ~3 milhoes.",
             "eficiencia": "alta", "eficacia": "parcial",
             "impacto": "Cisterna garante agua potavel por 8 meses de seca para uma familia.",
             "gap": "Cobre ~33% da demanda. Programa oscila com mudanca de governo.",
             "ano": 2003},

            # === 5. EDUCACAO ===
            {"dominio": "educacao", "nome": "FUNDEB (Fundo de Manutencao da Educacao Basica)",
             "esfera": "Federal/Estadual/Municipal", "orcamento": "R$ 165 bi/ano",
             "publico": "40 milhoes de alunos da rede publica",
             "alcance": "Todas escolas publicas recebem repasse.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Brasil gasta R$5.500/aluno/ano. Finlandia gasta R$60k. PISA 2022: BR 393/410/403 vs OCDE 472/476/485.",
             "gap": "Dinheiro entra mas IDEB estagnou. 7o ano: 50% nao sabem ler.",
             "ano": 1996},
            {"dominio": "educacao", "nome": "ProUNI / FIES / Enem",
             "esfera": "Federal", "orcamento": "R$ 12 bi/ano",
             "publico": "Estudantes de baixa renda para ensino superior",
             "alcance": "~3 milhoes de bolsas concedidas historico.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Ampliou acesso ao superior. Mas evasao ~50% nos primeiros 2 anos.",
             "gap": "So 18% dos jovens 18-24 chegam a universidade. Majoritariamente brancos.",
             "ano": 2004},

            # === 6. EMPREGO ===
            {"dominio": "emprego", "nome": "Seguro-Desemprego",
             "esfera": "Federal", "orcamento": "R$ 60 bi/ano",
             "publico": "Trabalhadores formais demitidos",
             "alcance": "~8 milhoes de beneficiarios/ano.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Socorro temporario. NAO reconecta ao mercado de trabalho.",
             "gap": "So cobre trabalhador FORMAL. ~40M informais nao tem direito.",
             "ano": 1986},
            {"dominio": "emprego", "nome": "Programa Emprega + Mulheres / Renova Mais",
             "esfera": "Federal", "orcamento": "R$ 1 bi/ano",
             "publico": "Mulheres, jovens, pretos/pardos",
             "alcance": "~100 mil insercoes/ano vs 10M desempregados.",
             "eficiencia": "baixa", "eficacia": "minima",
             "impacto": "Cobertura <1% do publico alvo.",
             "gap": "Gota no oceano. Nao atende escala.",
             "ano": 2022},

            # === 7. INFLACAO ===
            {"dominio": "inflacao", "nome": "Meta de Inflacao (Copom/BCB)",
             "esfera": "Federal", "orcamento": "N/A (politica monetaria)",
             "publico": "Toda populacao (precos)",
             "alcance": "Afeta todos os precos da economia.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "IPCA 2023: 4.62%. Meta: 3.25%. Mas cesta basica subiu 8% (pesa mais no pobre).",
             "gap": "Juros altos (10.75%) matam emprego. Inflacao de alimentos > inflaCAO geral.",
             "ano": 1999},
            {"dominio": "inflacao", "nome": "Cesta Basica Brasil / Subsidio de Alimentos",
             "esfera": "Federal", "orcamento": "R$ 0 (extinto)",
             "publico": "Populacao de baixa renda",
             "alcance": "0 (programa nao existe mais)",
             "eficiencia": "nula", "eficacia": "nao_resolve",
             "impacto": "Nenhum. Nao existe controle de preco de alimentos basicos no Brasil.",
             "gap": "Arroz +50%, feijao +30% em 2024. Zero politica de controle.",
             "ano": 1980, "status": "extinto"},

            # === 8. AGROPECUARIA ===
            {"dominio": "agropecuaria", "nome": "Plano Safra (Crédito Rural)",
             "esfera": "Federal", "orcamento": "R$ 400 bi/ano (2024/2025)",
             "publico": "Produtores rurais (grande e pequeno)",
             "alcance": "~70% vai para grande produtor. ~30% para agricultura familiar.",
             "eficiencia": "baixa", "eficacia": "parcial",
             "impacto": "Brasil e 2o maior exportador de alimentos. Mas 33M passam fome.",
             "gap": "Produz comida PRA EXPORTAR. Familiar recebe 30% do credito, produz 70% da comida DO BR.",
             "ano": 1965},
            {"dominio": "agropecuaria", "nome": "PRONAF (Agricultura Familiar)",
             "esfera": "Federal", "orcamento": "R$ 60 bi/ano (dentro do Plano Safra)",
             "publico": "4 milhoes de familias de agricultores familiares",
             "alcance": "~2 milhoes de contratos ativos.",
             "eficiencia": "alta", "eficacia": "parcial",
             "impacto": "Agricultura familiar produz 70% da comida consumida no BR com 30% do credito.",
             "gap": "Subfinanciado. Demanda e 4x maior que oferta de credito.",
             "ano": 1995},

            # === 9. ENERGIA ===
            {"dominio": "energia", "nome": "Luz para Todos",
             "esfera": "Federal", "orcamento": "R$ 8 bi (total historico)",
             "publico": "Comunidades rurais sem energia",
             "alcance": "~3.5 milhoes de ligacoes realizadas desde 2003.",
             "eficiencia": "alta", "eficacia": "parcial",
             "impacto": "Levou luz a 16 milhoes de pessoas. Mas ainda ha ~200 mil sem luz.",
             "gap": "Areas remotas (Amazonia, sertao) ainda sem. Energia solar nao incluida.",
             "ano": 2003},
            {"dominio": "energia", "nome": "Tarifa Social de Energia Eletrica",
             "esfera": "Federal", "orcamento": "R$ 8 bi/ano (subsidio)",
             "publico": "Familias de baixa renda",
             "alcance": "~22 milhoes de familias beneficiadas.",
             "eficiencia": "alta", "eficacia": "parcial",
             "impacto": "Desconto de 10-65% na conta de luz. Evita corte.",
             "gap": "Nao cobre quem NAO tem rede eletrica. Subsidio a consumo, nao a geracao.",
             "ano": 2010},
            {"dominio": "energia", "nome": "ProGD (Geracao Distribuida Solar)",
             "esfera": "Federal", "orcamento": "N/A (incentivo tributario)",
             "publico": "Quem pode instalar paineis",
             "alcance": "~2 milhoes de sistemas instalados (2024). Concentrado em classe media.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Solar cresceu 80%/ano. Mas pobre nao tem dinheiro pro painel.",
             "gap": "Beneficia quem tem telhado + credito. Pobre alugado fica de fora.",
             "ano": 2012},

            # === 10. SANEAMENTO ===
            {"dominio": "saneamento", "nome": "Novo Marco Saneamento (Lei 14.026/2020)",
             "esfera": "Federal", "orcamento": "R$ 700 bi (meta 20 anos)",
             "publico": "Toda populacao",
             "alcance": "Coleta de esgoto: 53% (urbano). Rural: ~15%.",
             "eficiencia": "baixa", "eficacia": "minima",
             "impacto": "Meta: 90% esgoto ate 2033. Ritmo atual: 0.8%/ano. Chegara em 2050.",
             "gap": "Privatizou sem metas reais. Crianca continua morrendo de diarreia no Norte.",
             "ano": 2020},

            # === 11. TRANSPORTE ===
            {"dominio": "transporte", "nome": "PAC Mobilidade Urbana",
             "esfera": "Federal", "orcamento": "R$ 40 bi/ano",
             "publico": "Populacao urbana",
             "alcance": "Metros/VLT em ~20 cidades. Onibus sem subsídio federal direto.",
             "eficiencia": "baixa", "eficacia": "minima",
             "impacto": "Brasil tem 10 linhas de metro vs 200+ em paises equivalentes.",
             "gap": "Pobre gasta 2h+ em transporte. Tarifa cara. Bicicleta ignorada.",
             "ano": 2007},
            {"dominio": "transporte", "nome": "Vale-Transporte",
             "esfera": "Federal", "orcamento": "R$ 12 bi/ano (empresas)",
             "publico": "Trabalhador formal CLT",
             "alcance": "~30 milhoes de trabalhadores.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Subsidia passagem do trabalhador formal.",
             "gap": "Trabalhador informal (40M) nao tem. Idoso e estudante por leis separadas.",
             "ano": 1987},

            # === 12. HABITACAO ===
            {"dominio": "habitacao", "nome": "Minha Casa Minha Vida",
             "esfera": "Federal", "orcamento": "R$ 20 bi/ano",
             "publico": "Familias de baixa renda (até R$2.600)",
             "alcance": "~5 milhoes de unidades entregues desde 2009.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Reduziu deficit habitacional ~20%. Mas casas longe do centro = sem servicos.",
             "gap": "Casas no meio do nada. Sem escola, posto, onibus. Virou dormitorio.",
             "ano": 2009},

            # === 13. COMUNICACAO ===
            {"dominio": "comunicacao", "nome": "Programa Nacional de Banda Larga (PNBL)",
             "esfera": "Federal", "orcamento": "R$ 4 bi (total historico)",
             "publico": "Areas nao atendidas",
             "alcance": "Descontinuado em 2019. Cobertura rural: ~30%.",
             "eficiencia": "nula", "eficacia": "nao_resolve",
             "impacto": "Projeto abandonado. 70% das areas rurais sem internet em 2024.",
             "gap": "Internet chega pelo mercado (caro), nao por politica. Escola rural sem internet.",
             "ano": 2010, "status": "extinto"},

            # === 14. MEIO AMBIENTE ===
            {"dominio": "ambiente", "nome": "PPCDAm (Plano Prevencao Desmatamento Amazonia)",
             "esfera": "Federal", "orcamento": "R$ 2 bi/ano",
             "publico": "Amazonia Legal",
             "alcance": "Desmatamento: 13.235 km2 (2023). Caiu 22% vs 2022, mas ainda 2x meta.",
             "eficiencia": "media", "eficacia": "parcial",
             "impacto": "Reduziu desmatamento 22% (2022->2023). Meta: eliminar ate 2027.",
             "gap": "Sobe e desce com governo. Ibama multa mas 80% das multas nao sao pagas.",
             "ano": 2004},
            {"dominio": "ambiente", "nome": "MapBiomas / INPE (Monitoramento)",
             "esfera": "Federal/ONG", "orcamento": "R$ 500M/ano",
             "publico": "Toda populacao (dados publicos)",
             "alcance": "Cobertura nacional. DETER/PRODES alerta quase em tempo real.",
             "eficiencia": "alta", "eficacia": "resolve",
             "impacto": "MapBiomas e referencia mundial. INPE detecta desmatamento em 1-7 dias.",
             "gap": "Detecta, mas fiscalizacao e fraca. Sabe onde queima, nao apaga o fogo.",
             "ano": 1988},

            # === 15. SEGURANCA ALIMENTARIA ===
            {"dominio": "seguranca_alimentar", "nome": "VIGISAN (Vigilancia de Seguranca Alimentar)",
             "esfera": "Federal", "orcamento": "R$ 20M/ano",
             "publico": "Amostra nacional",
             "alcance": "Pesquisa bienal. ~100 mil entrevistados.",
             "eficiencia": "alta", "eficacia": "resolve",
             "impacto": "VIGISAN 2022: 33M com fome, 125M em inseguranca alimentar. DADO REAL.",
             "gap": "Bienal. Fome muda em dias, VIGISAN mede a cada 2 anos. Volume insuficiente.",
             "ano": 2012},

            # === 16. DROGAS ===
            {"dominio": "drogas", "nome": "Política Nacional sobre Drogas (SENAD)",
             "esfera": "Federal", "orcamento": "R$ 1 bi/ano",
             "publico": "Usuarios dependentes + prevencao",
             "alcance": "~500 CAPS-AD (centros de atendimento). Demanda: ~3000.",
             "eficiencia": "baixa", "eficacia": "minima",
             "impacto": "Drogas sinteticas cresceram 400% (2019-2024). Crack persiste.",
             "gap": "So 17% dos dependentes tem acesso a tratamento. Lei de drogas eca racial.",
             "ano": 2002},

            # === 17. INDIGENA ===
            {"dominio": "indigena", "nome": "SASI-SUS (Subsistema Indigena de Saude)",
             "esfera": "Federal (SESAI)", "orcamento": "R$ 3 bi/ano",
             "publico": "~800 mil indigenas",
             "alcance": "34 Distritos Sanitarios Especiais Indigenas (DSEI).",
             "eficiencia": "baixa", "eficacia": "minima",
             "impacto": "Mortalidade infantil indigena 2x nacional. Desnutricao crônica Yanomami.",
             "gap": "Sem medicos, sem estrutura. Yanomami: 570 criancas morreram de fome (2022-2023).",
             "ano": 2010},

            # === 18. CULTURA ===
            {"dominio": "cultura", "nome": "Lei Paulo Gustavo / Lei Aldir Blanc",
             "esfera": "Federal", "orcamento": "R$ 3.8 bi (Aldir Blanc) + R$ 3.8 bi (Paulo Gustavo)",
             "publico": "Trabalhadores da cultura",
             "alcance": "~500 mil beneficiarios.",
             "eficiencia": "alta", "eficacia": "parcial",
             "impacto": "Manteve setor cultural vivo durante pandemia. Mas e emergencial, nao continuo.",
             "gap": "Lei Rouanet concentra 90% em 10% (ricos). Cultura periferica sem acesso.",
             "ano": 2020},
        ]

    def scorecard(self) -> Dict[str, Any]:
        d = self.diagnosticos
        total_pol = sum(len(diag.politicas) for diag in d.values())

        ef_counts = {"alta": 0, "media": 0, "baixa": 0, "nula": 0, "contra": 0}
        efc_counts = {"resolve": 0, "parcial": 0, "minima": 0, "nao_resolve": 0, "piora": 0}
        for diag in d.values():
            for p in diag.politicas:
                ef_counts[p.eficiencia.value] += 1
                efc_counts[p.eficacia.value] += 1

        vereditos = {}
        for dom, diag in sorted(d.items()):
            vereditos[dom] = diag.veredito

        return {
            "modulo": "open_politica_publica",
            "versao": "0.1.0-spec",
            "dominios_mapeados": len(d),
            "politicas_total": total_pol,
            "eficiencia": ef_counts,
            "eficacia": efc_counts,
            "veredito_por_dominio": vereditos,
            "pct_eficaz": f"{efc_counts['resolve']}/{total_pol} resolvem ({efc_counts['resolve']/total_pol*100:.0f}%)",
            "pct_ineficaz": f"{efc_counts['nao_resolve']+efc_counts['minima']}/{total_pol} nao resolvem ({(efc_counts['nao_resolve']+efc_counts['minima'])/total_pol*100:.0f}%)",
        }

    def to_dict(self) -> List[Dict[str, Any]]:
        """Exporta dados para dashboard."""
        out = []
        for dom, diag in sorted(self.diagnosticos.items()):
            for p in diag.politicas:
                out.append({
                    "dominio": dom,
                    "veredito": diag.veredito,
                    "nome": p.nome,
                    "esfera": p.esfera,
                    "orcamento": p.orcamento_anual,
                    "publico": p.publico_alvo,
                    "alcance": p.alcance_real,
                    "eficiencia": p.eficiencia.value,
                    "eficiencia_rotulo": p.eficiencia.rotulo,
                    "eficacia": p.eficacia.value,
                    "eficacia_rotulo": p.eficacia.rotulo,
                    "impacto": p.dado_impacto,
                    "gap": p.gap,
                    "ano": p.ano_criacao,
                    "status": p.status,
                })
        return out


def _demo():
    m = PoliticaPublicaMapper()
    sc = m.scorecard()

    print("=" * 70)
    print("MAPEAMENTO DE POLITICAS PUBLICAS vs RAIO X DO BRASIL")
    print("=" * 70)

    print(f"\n{sc['politicas_total']} politicas mapeadas em {sc['dominios_mapeados']} dominios\n")

    print("VEREDITO POR DOMINIO:")
    for dom, v in sc["veredito_por_dominio"].items():
        print(f"  {dom:<25} {v}")

    print(f"\n{'=' * 70}")
    print(f"EFICIENCIA (custo vs resultado):")
    for k, v in sc["eficiencia"].items():
        bar = "#" * v
        print(f"  {k:<8} {v:>2} {bar}")

    print(f"\n{'=' * 70}")
    print(f"EFICACIA (resolve o problema?):")
    for k, v in sc["eficacia"].items():
        bar = "#" * v
        print(f"  {k:<14} {v:>2} {bar}")

    print(f"\n{'=' * 70}")
    print(f"RESUMO:")
    print(f"  {sc['pct_eficaz']}")
    print(f"  {sc['pct_ineficaz']}")


if __name__ == "__main__":
    _demo()
