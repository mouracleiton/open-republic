#!/usr/bin/env python3
"""
OpenCensoNacional -- Censo Nacional da Republica
==================================================
"Substituir o IBGE. Nao por orgao igual. Por sistema que ve o chao."

O IBGE FAZ:
  1. Censo Demografico (a cada 10 anos -- atrasado desde 2020)
  2. PNAD (emprego, renda -- mensal/trimestral)
  3. POF (orcamento familiar -- a cada 5 anos)
  4. IPCA (inflacao -- mensal)
  5. Contas Nacionais (PIB -- trimestral)
  6. Geografia e Cartografia
  7. Registro Civil (nascimentos, obitos, casamentos)
  8. Censo Agropecuario
  9. Censo Escolar (ja specado em open_censo_escolar.py)
  10. Indicadores sociais

O PROBLEMA:
  IBGE pergunta. Resposta vem de formulario.
  Censo demografico atrasado 4 anos.
  PNAD por telefone -- 30% respondem.
  IPCA nao mede periferia.
  POF nao alcanca sem-teto.
  Registro civil nao cobre indigena, ribeirinho, quilombola.

A SOLUCAO:
  Censo continuo. Cidadao coleta. OSINT cruza.
  Mesma metodologia do censo escolar, escalada pra TUDO.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime


# ============================================================================
# 1. ENUMS -- DOMINIOS DO CENSO NACIONAL
# ============================================================================

class DominioCenso(Enum):
    """Todos os dominios que o IBGE cobre. Nos cobrimos com metodo diferente."""
    POPULACAO = ("populacao", "Censo Demografico: quantos somos, quem somos, onde")
    HABITACAO = ("habitacao", "Habitacao: tipo, qualidade, ocupacao, servicos")
    SAUDE = ("saude", "Saude: acesso, qualidade, mortalidade, doencas")
    EDUCACAO = ("educacao", "Educacao: escolas, alunos, infraestrutura (open_censo_escolar)")
    EMPREGO = ("emprego", "Emprego e Renda: ocupacao, salario informal, precario")
    ALIMENTACAO = ("alimentacao", "Seguranca Alimentar: fome, inseguranca, mercado")
    INFLACAO = ("inflacao", "Inflacao Real: preco de cesta basica por regiao/periferia")
    AGROPECUARIA = ("agro", "Agropecuaria: producao, reforma agraria, quem planta")
    ENERGIA = ("energia", "Energia: quem tem luz, quem tem geladeira, quem paga")
    AGUA = ("agua", "Agua e Saneamento: quem tem agua potavel, quem tem esgoto")
    TRANSPORTE = ("transporte", "Transporte: mobilidade, deslocamento, onibus, bicicleta")
    VIOLENCIA = ("violencia", "Violencia: seguranca real, nao estatistica de delegacia")
    AMBIENTE = ("ambiente", "Ambiente: queimada, desmatamento, qualidade do ar, rio")
    REGISTRO_CIVIL = ("registro", "Registro Civil: nascimento, obito, sem cartorio")
    INDIGENA = ("indigena", "Indigena: populacao, terra, saude (IBGE ignora)")
    QUILOMBOLA = ("quilombola", "Quilombola: comunidade, territorio, direito")
    RIBEIRINHA = ("ribeirinha", "Ribeirinha: populacao do rio, isolada")
    GEOGRAFIA = ("geografia", "Geografia: mapa, territorio, coordenadas reais")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class FonteDado(Enum):
    """De onde vem cada dado do censo nacional."""
    CIDADAO_CAMPO = ("cidadao", "Cidadao fiscalizador no campo (coleta ostensiva)")
    COMUNIDADE = ("comunidade", "Lider comunitario / morador (depoimento + assinatura)")
    OSINT = ("osint", "OSINT: satelite, street view, mapbiomas, sentinel-2")
    IBGE_LEGADO = ("ibge", "IBGE legado (cruzamento, baseline, verificacao)")
    REGISTRO_CIVIL = ("registro", "Cartorio / registro civil / hospital")
    MEDICAO_FISICA = ("medicao", "Medicao fisica: PH agua, decibel, lux, velocidade internet")
    MERCADO = ("mercado", "Preco de mercado: cesta basica, combustivel, remedio")
    DENUNCIA = ("denuncia", "Denuncia cidadao (violencia, corrupcao, desvio)")
    SENSOR_IOT = ("sensor", "Sensor IoT instalado (agua, luz, ar, rio)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class FrequenciaColeta(Enum):
    """Frequencia de coleta de cada dominio. IBGE e lento. Nos somos continuos."""
    TEMPO_REAL = ("real", "Tempo real: evento registrado quando acontece (violencia, obito)")
    DIARIO = ("diario", "Diario: inflacao (preco de mercado), violencia")
    SEMANAL = ("semanal", "Semanal: saude (doencas, atendimento), ambiente (queimada)")
    MENSAL = ("mensal", "Mensal: emprego, renda, alimentacao (seguranca alimentar)")
    TRIMESTRAL = ("trimestral", "Trimestral: habitacao, transporte, energia")
    SEMESTRAL = ("semestral", "Semestral: educacao (censo escolar), agropecuaria")
    ANUAL = ("anual", "Anual: populacao, registro civil, geografia")
    DECADAL = ("decadal", "Decadal: IBGE faz assim. Nos fazemos anual.")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def dias(self) -> int:
        return {"real": 0, "diario": 1, "semanal": 7, "mensal": 30,
                "trimestral": 90, "semestral": 180, "anual": 365, "decadal": 3650}[self.id]


# ============================================================================
# 2. SPEC DE CADA DOMINIO
# ============================================================================

@dataclass
class EspecDominio:
    """Spec de coleta de um dominio do censo nacional."""
    dominio: DominioCenso
    frequencia: FrequenciaColeta
    indicadores: List[str]           # o que medir
    fonte_principal: FonteDado
    fonte_cruzamento: List[FonteDado]
    equivalente_ibge: str            # o que o IBGE faz hoje
    problema_ibge: str               # por que o IBGE falha aqui
    vantagem_republica: str          # por que nosso e melhor


def _init_especs() -> List[EspecDominio]:
    return [
        EspecDominio(
            DominioCenso.POPULACAO, FrequenciaColeta.ANUAL,
            ["contagem populacional por regiao", "faixa etaria", "genero",
             "raca/cor", "migracao", "deslocamento"],
            FonteDado.CIDADAO_CAMPO,
            [FonteDado.OSINT, FonteDado.IBGE_LEGADO, FonteDado.COMUNIDADE],
            "Censo Demografico (a cada 10 anos)",
            "Atrasado 4+ anos. So cobre domicilio formal. Indigena/ribeirinho subcontado.",
            "Contagem anual por comunidade. Ribeirinho, indigena, sem-teto contados.",
        ),
        EspecDominio(
            DominioCenso.HABITACAO, FrequenciaColeta.TRIMESTRAL,
            ["tipo de construcao", "material", "numero de comodos", "ocupacao",
             "propriedade vs aluguel", "favela vs formal", "sem-teto"],
            FonteDado.CIDADAO_CAMPO,
            [FonteDado.OSINT, FonteDado.SENSOR_IOT],
            "PNAD Continua (trimestral)",
            "Nao conta sem-teto. Nao entra em favela sem autorizacao. Nao mede qualidade.",
            "Triangulacao: cidadao entra + satelite ve + sensor mede umidade/temperatura.",
        ),
        EspecDominio(
            DominioCenso.SAUDE, FrequenciaColeta.SEMANAL,
            ["acesso a posto/medico", "fila SUS", "medicamento disponivel",
             "mortalidade infantil", "mortalidade materna", "doencas endemicas",
             "saude mental", "atendimento indigena/ribeirinho"],
            FonteDado.COMUNIDADE,
            [FonteDado.MEDICAO_FISICA, FonteDado.REGISTRO_CIVIL, FonteDado.DENUNCIA],
            "SIM/SINASC/DATASUS",
            "Mortalidade subnotificada. Interior nao reporta. Indigena invisivel.",
            "Posto visitado semanalmente. Medicamento fotografado. Fila cronometrada.",
        ),
        EspecDominio(
            DominioCenso.EDUCACAO, FrequenciaColeta.SEMESTRAL,
            ["ver open_censo_escolar.py -- spec completa"],
            FonteDado.CIDADAO_CAMPO,
            [FonteDado.OSINT, FonteDado.IBGE_LEGADO],
            "Censo Escolar INEP",
            "Autopreenchido pelo diretor. Ninguem verifica.",
            "Cidadao vai la. OSINT cruza. Discrepancia detectada.",
        ),
        EspecDominio(
            DominioCenso.EMPREGO, FrequenciaColeta.MENSAL,
            ["ocupacao formal vs informal", "salario real (nao carteira)",
             "trabalho infantil", "trabalho escravo", "precario/app",
             "desemprego real (nao so ativo em busca)"],
            FonteDado.COMUNIDADE,
            [FonteDado.DENUNCIA, FonteDado.IBGE_LEGADO],
            "PNAD Continua (mensal/trimestral)",
            "Informal subnotificado. App-worker invisivel. Trabalho escravo nao medido.",
            "Morador sabe quem trabalha e quanto ganha. IBGE nao.",
        ),
        EspecDominio(
            DominioCenso.ALIMENTACAO, FrequenciaColeta.MENSAL,
            ["inseguranca alimentar ( EBIA)", "fome (0 refeicoes/dia)",
             "acesso a cesta basica", "mercado na area", "feira livre",
             "merenda escolar (ver censo escolar)"],
            FonteDado.COMUNIDADE,
            [FonteDado.MERCADO, FonteDado.MEDICAO_FISICA],
            "PNAD (seguranca alimentar -- bienal)",
            "Bienal. Fome muda em dias, nao em 2 anos.",
            "Mensal: preco de arroz+feijao por bairro. Morador reporta fome.",
        ),
        EspecDominio(
            DominioCenso.INFLACAO, FrequenciaColeta.DIARIO,
            ["preco de arroz, feijao, oleo, leite, tomate, banana",
             "preco de gas, onibus, luz, remedio",
             "preco por bairro/periferia (nao so centro)",
             "cesta basica por cidade"],
            FonteDado.MERCADO,
            [FonteDado.CIDADAO_CAMPO, FonteDado.SENSOR_IOT],
            "IPCA (mensal, 16 capitais)",
            "Nao mede periferia. Nao mede interior. Nao mede realidade do pobre.",
            "Cidadao fotografa preco de mercado. Tag de local. Diario. Todo bairro.",
        ),
        EspecDominio(
            DominioCenso.AGROPECUARIA, FrequenciaColeta.SEMESTRAL,
            ["area plantada", "producao real", "quem planta (familiar vs agronegocio)",
             "uso de agrotoxico", "desmatamento pra pasto", "reforma agraria",
             "assentamento", "trabalho escravo rural"],
            FonteDado.OSINT,
            [FonteDado.CIDADAO_CAMPO, FonteDado.SENSOR_IOT, FonteDado.DENUNCIA],
            "Censo Agropecuario (a cada 10 anos)",
            "10 anos! Agronegocio muda em meses. Trabalho escravo invisivel.",
            "Satelite ve area plantada semanal. Sensor de agrotoxico no rio.",
        ),
        EspecDominio(
            DominioCenso.ENERGIA, FrequenciaColeta.TRIMESTRAL,
            ["quem tem luz", "quantas horas/dia", "qualidade (pisca?)",
             "preco da conta", "quem tem geladeira", "energia solar comunitaria",
             "roubo de energia (gato)"],
            FonteDado.SENSOR_IOT,
            [FonteDado.CIDADAO_CAMPO, FonteDado.OSINT],
            "PNAD + ANEEL",
            "Nao mede qualidade. Nao conta quem nao tem medidor.",
            "Sensor IoT: mede voltagem, frequencia, queda. Diario. Automático.",
        ),
        EspecDominio(
            DominioCenso.AGUA, FrequenciaColeta.SEMANAL,
            ["quem tem agua", "potavel (medido, nao relatado)",
             "quantos dias/semana chega", "tratamento (cloro medido)",
             "esgoto: rede? fossa? nada?", "rio: PH, turbidez, coliformes"],
            FonteDado.MEDICAO_FISICA,
            [FonteDado.SENSOR_IOT, FonteDado.CIDADAO_CAMPO],
            "SNIS + PNAD",
            "Relatado pela empresa. Auto-avaliacao. Ninguem mede.",
            "Sensor de PH/cloro na torneira. Cidadao mede. Dado fisico.",
        ),
        EspecDominio(
            DominioCenso.TRANSPORTE, FrequenciaColeta.TRIMESTRAL,
            ["tempo de deslocamento casa->trabalho",
             "frequencia de onibus", "lotacao",
             "bicicleta como transporte (nao lazer)",
             "estrada: asfalto? terra? rio? trilha?",
             "transporte escolar (ver censo escolar)"],
            FonteDado.CIDADAO_CAMPO,
            [FonteDado.SENSOR_IOT, FonteDado.OSINT],
            "PNAD + CNT",
            "Nao mede periferia -> centro. Nao conta lotacao real.",
            "GPS do cidadao: tempo real de deslocamento. Lotacao fotografada.",
        ),
        EspecDominio(
            DominioCenso.VIOLENCIA, FrequenciaColeta.TEMPO_REAL,
            ["homicidio", "tiroteio (localizacao, horario)",
             "violencia domestica", "violencia policial",
             "faccao/territorio", "estupro (denuncia anonima)",
             "desaparecido"],
            FonteDado.DENUNCIA,
            [FonteDado.COMUNIDADE, FonteDado.OSINT, FonteDado.SENSOR_IOT],
            "SINESP + SSP estaduais",
            "Subnotificacao absurda. Violencia domestica invisivel. Indigena nao conta.",
            "Denuncia anonima em tempo real. Comunidade assina. OSINT cruza.",
        ),
        EspecDominio(
            DominioCenso.AMBIENTE, FrequenciaColeta.SEMANAL,
            ["queimada (foco, area)", "desmatamento",
             "qualidade do ar (PM2.5)", "qualidade do rio (PH, turbidez)",
             "lixo (destino real, nao declarado)", "reciclagem real"],
            FonteDado.OSINT,
            [FonteDado.SENSOR_IOT, FonteDado.CIDADAO_CAMPO],
            "INPE + IBGE Ambiente",
            "INPE detecta mas governo nao age. Lixo real nao e medido.",
            "Sentinel-2 + sensor PM2.5 + cidadao fotografa lixo no rio.",
        ),
        EspecDominio(
            DominioCenso.REGISTRO_CIVIL, FrequenciaColeta.TEMPO_REAL,
            ["nascimento (com certidao digital)", "obito (causa real)",
             "casamento", "identidade",
             "SEM cartorio (indigena, ribeirinho, sem-teto)"],
            FonteDado.REGISTRO_CIVIL,
            [FonteDado.COMUNIDADE, FonteDado.CIDADAO_CAMPO],
            "Cartorio + SIM/SINASC",
            "Indigena nao tem certidao. Ribeirinho sem cartorio. Obito sem causa.",
            "Certidao digital no celular. Registro comunitario sem cartorio.",
        ),
        EspecDominio(
            DominioCenso.INDIGENA, FrequenciaColeta.SEMESTRAL,
            ["populacao por etnia", "terra demarcada vs invadida",
             "saude (malario, desnutricao)", "educacao (bilíngue?)",
             "garimpo ilegal", "madeireira ilegal",
             "violencia contra indigena"],
            FonteDado.COMUNIDADE,
            [FonteDado.OSINT, FonteDado.DENUNCIA, FonteDado.MEDICAO_FISICA],
            "Censo Indigena (parte do demografico)",
            "Subcontado. Lingua ignorada. Terra invadida nao mapeada.",
            "Lider indigena coleta. OSINT ve garimpo. Sensor de mercurio no rio.",
        ),
        EspecDominio(
            DominioCenso.QUILOMBOLA, FrequenciaColeta.SEMESTRAL,
            ["populacao", "territorio certificado vs ameacado",
             "acesso a saude, escola, agua, luz",
             "titulacao (palmares)", "ameaca (grileiro, madeireira)"],
            FonteDado.COMUNIDADE,
            [FonteDado.OSINT, FonteDado.CIDADAO_CAMPO],
            "Censo Quilombola (incompleto)",
            "IBGE nao lista todos. Titulacao parada ha anos.",
            "Lider quilombola coleta. OSINT ve ameaca. Dado publico.",
        ),
        EspecDominio(
            DominioCenso.RIBEIRINHA, FrequenciaColeta.SEMESTRAL,
            ["populacao por comunidade", "acesso (barco, dias ate cidade)",
             "saude (posto? malario?), escola (ver censo escolar)",
             "energia (solar? gerador? nenhum?)",
             "agua (rio? poço? potavel?)",
             "inundacao sazonal"],
            FonteDado.COMUNIDADE,
            [FonteDado.OSINT, FonteDado.SENSOR_IOT],
            "Censo (subcontagem ribeirinha)",
            "IBGE nao chega. Acesso so por barco. Invisivel.",
            "Lider ribeirinho coleta via app offline. Sincroniza quando chega rede.",
        ),
        EspecDominio(
            DominioCenso.GEOGRAFIA, FrequenciaColeta.ANUAL,
            ["mapa territorial atualizado", "rua aberta vs fechada",
             "ponte existente vs caida", "estrada transitavel vs intransitavel",
             "limite municipal real", "coordenada de comunidade",
             "area de risco (deslizamento, inundacao)"],
            FonteDado.OSINT,
            [FonteDado.CIDADAO_CAMPO, FonteDado.COMUNIDADE],
            "IBGE Cartografia",
            "Mapa desatualizado. Rua nova nao aparece. Ponte caida aparece como ok.",
            "OpenStreetMap + cidadao edita + satelite confirma.",
        ),
    ]


# ============================================================================
# 3. METODOLOGIA (igual censo escolar, escalada)
# ============================================================================

class MetodologiaCenso(Enum):
    """Os 4 pilares da metodologia do censo nacional."""
    CHAO = ("chao", "Coleta no campo: cidadao vai la, ve, registra")
    SATÉLITE = ("satelite", "OSINT: satelite, street view, sensor remoto")
    COMUNIDADE = ("comunidade", "Comunidade: lider local reporta + assina")
    MEDICAO = ("medicao", "Medicao fisica: sensor IoT, PH, decibel, lux, velocidade")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 4. SISTEMA DE CENSO NACIONAL
# ============================================================================

class CensoNacionalSistema:
    """
    Censo Nacional da Republica.

    Substitui o IBGE. Nao por orgao igual.
    Por sistema que ve o chao, nao o formulario.
    """

    NOME = "OpenCensoNacional"
    VERSAO = "0.1.0-spec"

    def __init__(self) -> None:
        self.especs: List[EspecDominio] = _init_especs()

    # -- catalogos ---------------------------------------------------------

    def todos_dominios(self) -> List[Dict[str, Any]]:
        return [
            {
                "dominio": e.dominio.id,
                "rotulo": e.dominio.rotulo,
                "frequencia": e.frequencia.id,
                "frequencia_dias": e.frequencia.dias,
                "indicadores": e.indicadores,
                "fonte_principal": e.fonte_principal.id,
                "fonte_cruzamento": [f.id for f in e.fonte_cruzamento],
                "equivalente_ibge": e.equivalente_ibge,
                "problema_ibge": e.problema_ibge,
                "vantagem_republica": e.vantagem_republica,
            }
            for e in self.especs
        ]

    def dominio(self, dom_id: str) -> Optional[EspecDominio]:
        for e in self.especs:
            if e.dominio.id == dom_id:
                return e
        return None

    # -- comparativo IBGE ---------------------------------------------------

    def comparativo_ibge(self) -> List[Dict[str, str]]:
        """Tabela: IBGE hoje vs Republica."""
        return [
            {
                "dominio": e.dominio.id,
                "ibge_frequencia": e.equivalente_ibge,
                "ibge_problema": e.problema_ibge,
                "republica_frequencia": e.frequencia.rotulo,
                "republica_fonte": e.fonte_principal.rotulo,
                "republica_vantagem": e.vantagem_republica,
            }
            for e in self.especs
        ]

    # -- escala nacional ----------------------------------------------------

    def escala_nacional(self) -> Dict[str, Any]:
        """Estimativa de esforco para censo nacional continuo."""
        return {
            "populacao_brasil": 215_000_000,
            "municipios": 5570,
            "comunidades_estimadas": 500_000,  # bairros, vilas, aldeias, comunidades
            "cidadaos_fiscalizadores_necessario": 10_000,
            "cobertura_minima_pct": 95,  # IBGE cobre ~70%
            "inclusao_total": True,  # indigena, ribeirinho, sem-teto, quilombola
            "atualizacao": "Continua (IBGE: a cada 10 anos)",
            "estimativa_dados_ano_tb": 500,
            "comparativo_ibge_prazo": "IBGE: censo 2020 publicado em 2024 (4 anos atraso)",
            "comparativo_ibge_custo": "IBGE Censo 2022: R$ 2.3 bilhoes",
            "custo_estimado_republica": "R$ 200 milhoes/ano (1/10 do IBGE por ano)",
            "metodologia": "Cidadao + OSINT + Sensor + Comunidade (nao formulario)",
        }

    # -- APIs ---------------------------------------------------------------

    def espec_api(self) -> Dict[str, Any]:
        """Spec da API publica do censo nacional."""
        return {
            "url_base": "https://censo.republica.org.br/api/v2",
            "formato": "JSON + Parquet + CSV",
            "licenca": "CC0 (dominio publico)",
            "atualizacao": "tempo real (apos sincronizacao)",
            "endpoints": [
                "GET /dominio/{dominio} -- dados de um dominio",
                "GET /dominio/{dominio}/uf/{uf} -- por estado",
                "GET /dominio/{dominio}/municipio/{cod} -- por municipio",
                "GET /dominio/{dominio}/comunidade/{id} -- por comunidade",
                "GET /discrepancias/{dominio} -- discrepancias vs IBGE",
                "GET /invisiveis -- populacao que IBGE nao conta",
                "GET /historico/{dominio}/{id} -- serie temporal",
                "GET /mapa/{dominio} -- dados georreferenciados (GeoJSON)",
                "GET /indicador/{nome} -- indicador especifico (IPCA, IDH, etc)",
                "POST /coleta/{dominio} -- enviar coleta (autenticado)",
                "POST /denuncia -- denuncia anonima (violencia, corrupcao)",
                "WS /tempo-real -- websocket de eventos em tempo real",
            ],
            "auditabilidade": "cada dado: hash + timestamp + coletor + nivel confianca",
            "privacidade": "dados pessoais anonimizados (LGPD + P2 + P14)",
        }

    # -- indicadores nacionais ----------------------------------------------

    def indicadores_disponiveis(self) -> List[Dict[str, str]]:
        """Indicadores que o sistema produz (substitui IBGE/INEP/IPEA)."""
        return [
            {"id": "pop_total", "nome": "Populacao Total Real", "dominio": "populacao",
             "ibge_equivalente": "Censo Demografico", "frequencia": "anual"},
            {"id": "idh_real", "nome": "IDH Real (com invisiveis)", "dominio": "populacao",
             "ibge_equivalente": "IDH PNUD/IBGE", "frequencia": "anual"},
            {"id": "ipca_real", "nome": "Inflacao Real (periferia + interior)", "dominio": "inflacao",
             "ibge_equivalente": "IPCA", "frequencia": "diario"},
            {"id": "desemprego_real", "nome": "Desemprego Real (com informal)", "dominio": "emprego",
             "ibge_equivalente": "PNAD Continua", "frequencia": "mensal"},
            {"id": "fome_real", "nome": "Inseguranca Alimentar Real", "dominio": "alimentacao",
             "ibge_equivalente": "PNAD EBIA", "frequencia": "mensal"},
            {"id": "analfabetismo_real", "nome": "Analfabetismo Funcional Real", "dominio": "educacao",
             "ibge_equivalente": "PNAD Educacao", "frequencia": "semestral"},
            {"id": "mortalidade_infantil_real", "nome": "Mortalidade Infantil Real", "dominio": "saude",
             "ibge_equivalente": "SIM/DATASUS", "frequencia": "semanal"},
            {"id": "violencia_real", "nome": "Violencia Real (subnotificada)", "dominio": "violencia",
             "ibge_equivalente": "SINESP/SSP", "frequencia": "tempo real"},
            {"id": "agua_potavel_real", "nome": "Agua Potavel Real (medida)", "dominio": "agua",
             "ibge_equivalente": "SNIS", "frequencia": "semanal"},
            {"id": "energia_real", "nome": "Acesso a Energia Real", "dominio": "energia",
             "ibge_equivalente": "ANEEL/PNAD", "frequencia": "trimestral"},
            {"id": "queimada_real", "nome": "Queimada Real (area, foco)", "dominio": "ambiente",
             "ibge_equivalente": "INPE", "frequencia": "semanal"},
            {"id": "indigena_pop", "nome": "Populacao Indigena Real", "dominio": "indigena",
             "ibge_equivalente": "Censo Indigena", "frequencia": "semestral"},
        ]

    # -- o que o IBGE nao ve ------------------------------------------------

    def populacao_invisivel(self) -> List[Dict[str, str]]:
        """Quem o IBGE NAO conta. Nos contamos."""
        return [
            {"grupo": "Indigena em terra remota", "estimativa": "100.000+",
             "motivo": "IBGE nao chega. Sem estrada, sem barco, sem heli."},
            {"grupo": "Ribeirinho amazônico", "estimativa": "500.000+",
             "motivo": "Acesso so por barco (dias). IBGE nao vai."},
            {"grupo": "Quilombola nao-certificado", "estimativa": "200.000+",
             "motivo": "Sem certificado Palmares = invisivel pro IBGE."},
            {"grupo": "Sem-teto", "estimativa": "200.000+",
             "motivo": "IBGE conta domicilio. Sem domicilio = sem conta."},
            {"grupo": "Crianca em trabalho infantil", "estimativa": "1.800.000",
             "motivo": "Nao declarado. IBGE estima por amostra."},
            {"grupo": "Trabalho escravo contemporaneo", "estimativa": "370.000",
             "motivo": "Invisivel. So aparece em operacao de fiscalizacao."},
            {"grupo": "Refugiado/imigrante informal", "estimativa": "600.000+",
             "motivo": "Haitiano, venezuelano, africano sem documento."},
            {"grupo": "Encarcerado", "estimativa": "800.000",
             "motivo": "IBGE nao conta como populacao ativa."},
        ]

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "dominios": len(self.especs),
            "fontes_dado": len(list(FonteDado)),
            "frequencias": len(list(FrequenciaColeta)),
            "metodologias": len(list(MetodologiaCenso)),
            "indicadores": len(self.indicadores_disponiveis()),
            "populacao_invisivel_grupos": len(self.populacao_invisivel()),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    sis = CensoNacionalSistema()

    print("=" * 70)
    print(f"{sis.NOME} v{sis.VERSAO} -- Censo Nacional da Republica")
    print("=" * 70)

    # --- Dominios ---
    print(f"\n[DOMINIOS DO CENSO ({len(sis.especs)})]\n")
    print(f"  {'DOMINIO':<18} {'FREQ':<14} {'IBGE EQUIVALENTE':<30}")
    print(f"  {'-'*70}")
    for d in sis.todos_dominios():
        print(f"  {d['dominio']:<18} {d['frequencia']:<14} {d['equivalente_ibge'][:28]}")

    # --- Comparativo ---
    print(f"\n\n[IBGE HOJE vs REPUBLICA]\n")
    for c in sis.comparativo_ibge():
        print(f"  [{c['dominio'].upper()}]")
        print(f"  IBGE:     {c['ibge_frequencia']}")
        print(f"            {c['ibge_problema'][:60]}")
        print(f"  Republica: {c['republica_frequencia']} | {c['republica_fonte']}")
        print(f"            {c['republica_vantagem'][:60]}")
        print()

    # --- Populacao invisivel ---
    print("[POPULACAO QUE O IBGE NAO VE]\n")
    invis = sis.populacao_invisivel()
    total_inv = 0
    for p in invis:
        est = int(p["estimativa"].replace("+", "").replace(".", ""))
        total_inv += est
        print(f"  {p['grupo']:<40} ~{p['estimativa']}")
        print(f"    {p['motivo']}")
    print(f"\n  TOTAL INVISIVEL: ~{total_inv:,} brasileiros que o IBGE nao conta")

    # --- Escala ---
    print(f"\n\n[ESCALA NACIONAL]\n")
    esc = sis.escala_nacional()
    for k, v in esc.items():
        print(f"  {k}: {v}")

    # --- API ---
    print(f"\n\n[API PUBLICA]\n")
    api = sis.espec_api()
    print(f"  URL: {api['url_base']}")
    print(f"  Licenca: {api['licenca']}")
    print(f"  Endpoints ({len(api['endpoints'])}):")
    for e in api["endpoints"]:
        print(f"    {e}")

    # --- Indicadores ---
    print(f"\n\n[INDICADORES NACIONAIS ({len(sis.indicadores_disponiveis())})]\n")
    for ind in sis.indicadores_disponiveis():
        print(f"  {ind['id']:<28} {ind['nome']:<40} ({ind['frequencia']})")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = sis.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
