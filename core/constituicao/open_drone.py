#!/usr/bin/env python3
"""
OpenDrone -- P10: Soberania Aerea Civica
=========================================
O decimo principio constitucional da Republica Aberta.

"O ceu nao e de ninguem. Portanto, e de todos." -- principio do espaco aereo
como bem comum, analogo ao principio da terra (OpenAgrarianRevolution):
guardiao, nao dono.

DISTINCAO CRITICA (a tese do modulo):
- Drones (VANTs -- Veiculos Aereos Nao Tripulados) sao INFRAESTRUTURA.
- Como toda infraestrutura na Republica, pertencem ao dominio publico e
  servem a P1 (erradicar miserabilidade), nao a vigilancia, nem a lucro,
  nem a guerra.
- Um ceu cheio de drones comerciais entregando pacotes de consumo enquanto
  criancas passam fome e um monumento a distopia. OpenDrone transforma o
  espaco aereo em bem comum civico.

TRES PROIBICOES CONSTITUCIONAIS (o triplo NAO):
1. NAO VIGIA: drones com camera de vigilancia sao PROIBIDOS. Camera so para
   navegacao (feed local, nao gravado, nao transmitido para central).
2. NAO MATA: drones nao podem carregar armas. Ponto. Sem excecoes. Um drone
   armado nao e drone -- e arma. E arma pertence ao museu da Republica.
3. NAO ESPIONA: drones nao coletam dados pessoais. Entregam suprimentos,
   nao metadados. O trajeto de voo e publico; o destinatario e privado.

USOS PERMITIDOS (missao civica):
- Entrega de suprimentos (medicamentos, alimentos, agua) a areas isoladas
- Mapeamento ambiental (desmatamento, queimadas, qualidade da agua)
- Busca e resgate em desastres naturais
- Conectividade aerea (rede mesh em areas sem cobertura)
- Inspecao de infraestrutura critica (diques, barragens, pontes)

GATE DE MISSAO (P10):
Toda missao de drone deve passar por um gate antes de decolar:
- Proposito civico declarado e aprovado
- Zona de voo geofenceada (nao sobrevoa residencia privada sem consentimento)
- Log publico (trajeto, duracao, proposito)
- Razao de rejeicao explicita se negada

ALINHAMENTO CONSTITUCIONAL:
- P1: Drones que entregam medicamentos em area isolada combatem miserabilidade.
      Drones que entregam propaganda ampliam miserabilidade. P10 escolhe.
- P2: Drones que vigiam destroem autonomia. Drone que entrega remedio amplia
      autonomia (acesso). O instrumento nao e neutro -- o USO define.
- P4: Espaco aereo e decisao coletiva. Nenhuma corporacao o ocupa sozinha.
- P8: Drone autonomo e IA que atua no mundo fisico. Se ampliar inteligencia/
      reduzir miserabilidade = cumpre P8. Se vigiar = viola P8.

ATUALIZACAO 2024/2025 (revisao deste modulo):
- Catalogo de modelos comerciais realistas (DJI Mavic 3E / Matrice 30T /
  Matrice 350, Autel EVO II Enterprise, Wingcopter 198, XMobots Echar 20D,
  DJI Agras T50, Speedbird P200) com autonomia, carga, MTOW e precos BRL.
- Quadro regulatorio brasileiro vigente: RBAC-E 94 + SORA 2024, ICA 100-12,
  Lei 14.678/2023, Remote ID (ASTM F3411), registro ANAC RIBE, seguro RC.
- Gate P10 adota o marco ANAC/DECEA como PISO e aplica criterios civicos
  adicionais (camera de vigilancia proibida mesmo se a ANAC permitir).

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from collections import defaultdict


# ============================================================================
# 1. ENUMS (modulo-level, nunca aninhados)
# ============================================================================

class TipoMissao(Enum):
    """Categorias de missao civica permitidas para drones da Republica."""
    ENTREGA_SUPRIMENTOS = ("entrega_suprimentos", "Entrega de suprimentos (remedio, comida, agua)", 1)
    MAPEAMENTO_AMBIENTAL = ("mapeamento_ambiental", "Mapeamento ambiental (desmatamento, queimadas)", 1)
    BUSCA_RESGATE = ("busca_resgate", "Busca e resgate em desastre natural", 0)
    CONECTIVIDADE = ("conectividade", "Rede mesh aerea (area sem cobertura)", 1)
    INSPECAO_INFRA = ("inspecao_infra", "Inspecao de infraestrutura critica", 1)
    AGRICULTURA_CIVICA = ("agricultura_civica", "Agricultura de precisao comunitaria", 2)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def prioridade(self) -> int:
        """0=maxima prioridade (resgate), 2=minima."""
        return self.value[2]


class StatusMissao(Enum):
    """Ciclo de vida de uma missao de drone."""
    PLANEJADA = ("planejada", "Planejada (aguardando aprovacao do gate)")
    APROVADA = ("aprovada", "Aprovada pelo gate P10")
    EM_VOO = ("em_voo", "Em voo (executando)")
    CONCLUIDA = ("concluida", "Concluida com sucesso")
    REJEITADA = ("rejeitada", "Rejeitada pelo gate P10")
    CANCELADA = ("cancelada", "Cancelada (emergencia ou erro)")
    FALHOU = ("falhou", "Falhou (perda de sinal, aterrissagem forcada)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoProibicao(Enum):
    """As tres proibicoes constitucionais do P10. Drone que viola = e arma."""
    VIGILANCIA = ("vigilancia", "Camera de vigilancia (feed gravado/transmitido)", 5)
    ARMAMENTO = ("armamento", "Carrega arma ou explosivo", 5)
    ESPIONAGEM = ("espionagem", "Coleta dados pessoais (facial, placa, biometria)", 5)
    PRIVADO_SEM_CONSENTIMENTO = ("privado_sem_consentimento", "Sobrevoa area privada sem consentimento", 4)
    COMERCIAL_NAO_CIVICO = ("comercial_nao_civico", "Uso comercial sem proposito civico (propaganda)", 3)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def gravidade(self) -> int:
        return self.value[2]


class VereditoGate(Enum):
    """Resultado do gate P10 numa missao proposta."""
    APROVADA = ("aprovada", "Missao aprovada: proposito civico confirmado")
    APROVADA_COM_RESTRICOES = ("aprovada_restricoes", "Aprovada com restricoes (geofence ampliado)")
    REJEITADA = ("rejeitada", "Missao rejeitada: viola uma proibicao P10")
    BLOQUEADA = ("bloqueada", "Missao bloqueada: e vetor de vigilancia/arma")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class PrioridadeCorredor(Enum):
    """Quem tem prioridade no espaco aereo compartilhado."""
    RESGATE_VIDA = ("resgate_vida", "Resgate de vida (emergencia medica)", 0)
    ENTREGA_CRITICA = ("entrega_critica", "Entrega critica (remedio urgente)", 1)
    MAPEAMENTO_AMBIENTAL = ("mapeamento", "Mapeamento ambiental de rotina", 2)
    CONECTIVIDADE = ("conectividade", "Conectividade mesh", 2)
    INSPECAO = ("inspecao", "Inspecao de infraestrutura", 3)
    OUTROS = ("outros", "Outros usos civicos", 4)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def prioridade(self) -> int:
        return self.value[2]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass
class Coordenada:
    """Ponto geografico (lat, lon em graus decimais)."""
    lat: float
    lon: float


@dataclass
class ZonaVoo:
    """Area geofenceada onde o drone pode operar."""
    id: str
    centro: Coordenada
    raio_metros: float
    descricao: str = ""
    sobrevoa_privado: bool = False
    consentimento_privado: bool = False


@dataclass
class ModeloDrone:
    """Catalogo de modelos comerciais civicos homologaveis (dados 2024/2025).

    Fontes: especificacoes de fabricante (DJI, Autel, Wingcopter, XMobots) e
    pesquisa de mercado para o Brasil (precos aproximados em BRL, sujeitos a
    cambio/importacao). Usados para dimensionar a frota civica da Republica --
    nao como endorsing comercial. A Republica nao compra marcas, compra missao.
    """
    fabricante: str
    modelo: str
    autonomia_minutos: int          # tempo de voo maximo (hover)
    carga_max_kg: float             # payload util
    mtow_kg: float                  # peso maximo na decolagem
    velocidade_max_kmh: float       # velocidade de cruzeiro
    resistencia_vento_ms: float     # resistencia a vento (m/s)
    ip_rating: str                  # protecao (ex. IP55)
    usos_recomendados: List[str]    # tipos de missao civica ideais
    preco_brl_aprox: int            # estimativa 2024/2025 (hardware only)
    observacao: str = ""


@dataclass
class Drone:
    """Um veiculo aereo nao tripulado registrado na Republica."""
    id: str
    modelo: str
    autonomia_minutos: int
    carga_max_kg: float
    tem_camera_navegacao: bool = True  # permitida (feed local, nao gravado)
    tem_camera_vigilancia: bool = False  # PROIBIDA
    tem_armamento: bool = False  # PROIBIDO
    coleta_dados_pessoais: bool = False  # PROIBIDO
    ativo: bool = True
    missoes_concluidas: int = 0


@dataclass
class MissaoDrone:
    """Uma missao proposta para um drone."""
    id: str
    drone_id: str
    tipo: TipoMissao
    descricao: str
    zona: ZonaVoo
    destino: Optional[Coordenada] = None
    carga_descricao: str = ""
    urgencia: bool = False
    status: StatusMissao = StatusMissao.PLANEJADA
    veredito_gate: Optional[VereditoGate] = None
    razao_rejeicao: str = ""
    proibicoes_violadas: List[TipoProibicao] = field(default_factory=list)
    criada_em: str = ""
    concluida_em: str = ""
    log_trajeto: List[Coordenada] = field(default_factory=list)


@dataclass
class LogVoo:
    """Registro publico de um voo concluido (transparencia P10)."""
    missao_id: str
    drone_id: str
    tipo_missao: str
    duracao_minutos: float
    distancia_km: float
    decolagem: str  # timestamp ISO
    pouso: str
    destino_lat: Optional[float] = None
    destino_lon: Optional[float] = None
    sucesso: bool = True
    observacoes: str = ""


@dataclass
class MetricaFrota:
    """Snapshot da frota de drones civicos de uma regiao."""
    regiao_id: str
    total_drones: int
    drones_ativos: int
    missoes_concluidas: int
    missoes_rejeitadas: int
    entregas_criticas: int
    resgates: int
    horas_voo: float
    violacoes_detectadas: int
    cobertura_km2: float


# ============================================================================
# 3. TABELA DE PROIBICOES E SALVAGUARDAS
# ============================================================================

# Descricao detalhada de cada proibicao constitucional (para o gate)
DESCRICOES_PROIBICOES: Dict[str, str] = {
    "vigilancia": (
        "Camera de vigilancia = feed gravado ou transmitido para central de "
        "monitoramento. PERMITIDO: camera de navegacao (feed local em tempo real, "
        "nao gravado, processado no proprio drone). A linha e: a camera ajuda o "
        "drone a voar, nao ajuda o Estado a vigiar."
    ),
    "armamento": (
        "Qualquer arma, explosivo, ou dispositivo projetado para causar dano "
        "fisico. Um drone armado nao e drone -- e arma. Armas pertencem ao museu "
        "da Republica (P7). Sem excecoes, mesmo para 'defesa'."
    ),
    "espionagem": (
        "Reconhecimento facial, leitura de placas, coleta de biometria, captura "
        "de dados de rede (wifi bluetooth scanning). O drone entrega suprimentos; "
        "NAO entrega metadados sobre o destinatario."
    ),
    "privado_sem_consentimento": (
        "Sobrevoar residencia, patio, ou propriedade privada sem consentimento "
        "explicito do morador. Excecao: resgate de vida (P1 > privacidade), mas "
        "o log fica publico e auditavel."
    ),
    "comercial_nao_civico": (
        "Uso para entrega de consumo de luxo, propaganda, marketing, ou qualquer "
        "fim que nao reduza miserabilidade ou amplie acesso. Drones nao sao "
        "brinquedo de consumo -- sao infraestrutura de sobrevivencia."
    ),
}

# Mapa de tipo de missao -> prioridade no corredor aereo
PRIORIDADE_POR_TIPO: Dict[str, int] = {
    TipoMissao.BUSCA_RESGATE.id: 0,
    TipoMissao.ENTREGA_SUPRIMENTOS.id: 1,
    TipoMissao.MAPEAMENTO_AMBIENTAL.id: 2,
    TipoMissao.CONECTIVIDADE.id: 2,
    TipoMissao.INSPECAO_INFRA.id: 3,
    TipoMissao.AGRICULTURA_CIVICA.id: 3,
}


# ============================================================================
# 3b. CATALOGO DE MODELOS 2024/2025 (referencia para dimensionamento)
# ============================================================================
# Dados coletados em 2024/2025. Precos em BRL sao aproximados (hardware + TX
# importacao Brasil, sem baterias extras/acessorios). Autonomia em condicoes
# ideais (hover, sem vento, sem carga maxima). Sujeto a cambio USD->BRL ~5,5.
#
# Criterio de selecao: modelos com papel civico comprovado (entrega, resgate,
# mapeamento, inspecao, agricultura). Modelos militares/arma>excluidos por P10.

CATALOGO_DRONES_2024: List[ModeloDrone] = [
    ModeloDrone(
        fabricante="DJI",
        modelo="Mavic 3 Enterprise (M3E)",
        autonomia_minutos=45,
        carga_max_kg=0.95,
        mtow_kg=1.49,
        velocidade_max_kmh=75.0,
        resistencia_vento_ms=15.0,
        ip_rating="IP54",
        usos_recomendados=["mapeamento_ambiental", "inspecao_infra", "busca_resgate"],
        preco_brl_aprox=45000,
        observacao="RTK nativo; camera mecânica de 20MP. Padrão de mercado para mapeamento civico.",
    ),
    ModeloDrone(
        fabricante="DJI",
        modelo="Matrice 30T (M30T)",
        autonomia_minutos=41,
        carga_max_kg=2.7,
        mtow_kg=6.9,
        velocidade_max_kmh=82.8,
        resistencia_vento_ms=15.0,
        ip_rating="IP55",
        usos_recomendados=["busca_resgate", "inspecao_infra", "mapeamento_ambiental"],
        preco_brl_aprox=120000,
        observacao="Plataforma terna>multi-sensor (thermal+zoom). Robusto para resgate em desastre.",
    ),
    ModeloDrone(
        fabricante="DJI",
        modelo="Matrice 350 RTK (M350)",
        autonomia_minutos=55,
        carga_max_kg=2.7,
        mtow_kg=7.5,
        velocidade_max_kmh=82.8,
        resistencia_vento_ms=15.0,
        ip_rating="IP55",
        usos_recomendados=["inspecao_infra", "mapeamento_ambiental", "agricultura_civica"],
        preco_brl_aprox=160000,
        observacao="Plataforma modular para cargas uteis grandes (L2 lidar, sensors ambientais).",
    ),
    ModeloDrone(
        fabricante="Autel",
        modelo="EVO II Pro Enterprise V3",
        autonomia_minutos=36,
        carga_max_kg=0.8,
        mtow_kg=1.19,
        velocidade_max_kmh=64.8,
        resistencia_vento_ms=17.0,
        ip_rating="IP43",
        usos_recomendados=["mapeamento_ambiental", "inspecao_infra"],
        preco_brl_aprox=35000,
        observacao="Camera 1 polegada 6K. Sem geofence forced -- relevante para aeronautica (mais aberto que DJI).",
    ),
    ModeloDrone(
        fabricante="Wingcopter",
        modelo="Wingcopter 198",
        autonomia_minutos=60,
        carga_max_kg=3.9,
        mtow_kg=8.5,
        velocidade_max_kmh=90.0,  # cruzeiro estavel
        resistencia_vento_ms=12.0,
        ip_rating="IP54",
        usos_recomendados=["entrega_suprimentos", "conectividade"],
        preco_brl_aprox=400000,
        observacao="Asa fixa tilt-rotor VTOL. Alcance ate 110 km. Ouro-padrão para entrega em area isolada.",
    ),
    ModeloDrone(
        fabricante="XMobots",
        modelo="Echar 20D",
        autonomia_minutos=60,
        carga_max_kg=1.5,
        mtow_kg=7.0,
        velocidade_max_kmh=65.0,
        resistencia_vento_ms=12.0,
        ip_rating="IP54",
        usos_recomendados=["mapeamento_ambiental", "agricultura_civica", "inspecao_infra"],
        preco_brl_aprox=220000,
        observacao="Fabricante brasileiro (São Carlos/SP). Asa fixa VTOL. Mapeamento de grande área.",
    ),
    ModeloDrone(
        fabricante="DJI",
        modelo="Agras T50",
        autonomia_minutos=10,  # por bateria em pulverizacao
        carga_max_kg=40.0,     # tanque
        mtow_kg=110.0,
        velocidade_max_kmh=32.0,
        resistencia_vento_ms=10.0,
        ip_rating="IP55",
        usos_recomendados=["agricultura_civica"],
        preco_brl_aprox=180000,
        observacao="Agricola de precisão. Usado em agricultura comunitaria (pulverizacao, plantio, mapeamento de talhao).",
    ),
    ModeloDrone(
        fabricante="Speedbird",
        modelo="P200",
        autonomia_minutos=60,
        carga_max_kg=2.5,
        mtow_kg=10.0,
        velocidade_max_kmh=80.0,
        resistencia_vento_ms=12.0,
        ip_rating="IP54",
        usos_recomendados=["entrega_suprimentos", "conectividade"],
        preco_brl_aprox=300000,
        observacao="Asa fixa VTOL multi-rotor. Robusto para logistica em Amazonia/Cerrado.",
    ),
]

# Index por nome de modelo (busca rapida)
CATALOGO_POR_NOME: Dict[str, ModeloDrone] = {m.modelo: m for m in CATALOGO_DRONES_2024}


# ============================================================================
# 3c. QUADRO REGULATORIO BRASILEIRO (ANAC + DECEA) -- ATUALIZADO 2024/2025
# ============================================================================
# Resumo das normas vigentes para VANT/RPAS no Brasil em 2024/2025. O gate P10
# adota como piso os requisitos ANAC/DECEA e aplica criterios civicos adicionais.
# Fonte principal: ANAC (www.anac.gov.br), DECEA/AISWEB, Lei 14.678/2023.
#
# -- ANAC (Agencia Nacional de Aviacao Civil) --
#   * RBAC-E no. 94 (Requisitos Gerais para VANT): regra de base para RPAS ate
#       150 kg. Categorias: Aberta, Especifica, Reconhecida (alinhado ao JARUS).
#   * RBAC no. 94/2024 suplemento -- SORA (Specific Operations Risk Assessment)
#       exigido para operacoes na categoria Especifica a partir de 2024.
#   * Registro ANAC: todo RPAS >250 g deve ser registrado no Sistema ANATools
#       (RIBE - Registro de Aeronaves). Tarifa publica vigente em 2024: R$ 200.
#   * Seguro obrigatorio: RC para operadores (minimo recomendado pela SUSEP
#       aplicavel a aviacao geral).
#   * Identificacao Remota (Remote ID): adocao em curso alinhada ao ASTM F3411.
#       Vigencia progressiva em 2024/2025.
#
# -- DECEA (Departamento de Controle do Espaco Aereo) --
#   * ICA 100-12 (Regras do Ar para RPAS) -- edicao atualizada 2024.
#   * Plano de Voo obrigatorio para operacoes em espaco aereo controlado,
#       area populosa, ou RPAS >25 kg.
#   * CAVE (Circulo de Aviso e Vigilancia de Espaco Aereo) -- aplicavel para
#       operacoes com risco elevado.
#   * Altura maxima: 120 m AGL (400 ft) para categoria Aberta, salvo autorizacao.
#   * Zonas proibidas: 5 km de aerodromos controlados (sem coordenação DECEA).
#   * Pilotagem sob EFE (Visual Line of Sight - VLOS) na categoria Aberta.
#
# -- Lei 14.678/2023 (Boa-vizinhanca e RPAS) --
#   * Cria contravencao penal para uso de RPAS que coloque em risco aeronaves
#       ou pessoas; multa R$ 2.000 a R$ 50.000 para operadores sem registro.
#   * Vigente desde 22/06/2023; regulamentacao complementar ANAC em 2024.
#
# -- Alinhamento P10 (acao da Republica sobre o marco legal) --
#   * P10 adota RBAC-E 94 como piso; REJEITA categorias que exijam camera de
#       vigilancia como requisito (ex. algumas subcategorias SORA). Camera de
#       navegacao OK; camera de vigilancia PROIBIDA mesmo que a ANAC permita.
#   * Remote ID obrigatorio e PUBLICO em toda frota P10 (transparencia > privacidade do operador).
#   * Log de voo alinhado ao Plano de Voo DECEA, mas tambem publicado no log
#       publico da Republica.

@dataclass
class RequisitoRegulatorio:
    """Item do quadro regulatorio brasileiro vigente (2024/2025)."""
    orgao: str          # ANAC, DECEA, Lei
    norma: str          # ex. "RBAC-E no. 94"
    descricao: str
    categoria: str      # "registro", "operacao", "equipamento", "penal"
    vigente_desde: str  # ano-mes
    alinhamento_p10: str  # como a Republica aplica essa norma


QUADRO_REGULATORIO_2024: List[RequisitoRegulatorio] = [
    RequisitoRegulatorio(
        orgao="ANAC",
        norma="RBAC-E no. 94",
        descricao="Regras gerais para VANT ate 150 kg. Tres categorias de operacao: Aberta, Especifica, Reconhecida.",
        categoria="operacao",
        vigente_desde="2017-04 (ult. rev. 2024)",
        alinhamento_p10="P10 adota como piso. Frota civica opera na categoria Aberta sempre que possivel.",
    ),
    RequisitoRegulatorio(
        orgao="ANAC",
        norma="SORA (Emenda 94B/2024)",
        descricao="Specific Operations Risk Assessment obrigatorio para categoria Especifica a partir de 2024.",
        categoria="operacao",
        vigente_desde="2024",
        alinhamento_p10="Toda missao P10 na categoria Especifica anexa SORA no gate antes da aprovacao.",
    ),
    RequisitoRegulatorio(
        orgao="ANAC",
        norma="Registro ANATools/RIBE",
        descricao="Todo RPAS >250 g deve ser registrado na ANAC. Tarifa 2024: R$ 200 por aeronave.",
        categoria="registro",
        vigente_desde="2017 (vigente 2024)",
        alinhamento_p10="Obrigatorio para toda a frota da Republica. Sem registro = drone nao decola.",
    ),
    RequisitoRegulatorio(
        orgao="DECEA",
        norma="ICA 100-12",
        descricao="Regras do ar para RPAS. Plano de voo obrigatorio em espaco controlado/populoso ou >25 kg.",
        categoria="operacao",
        vigente_desde="2021 (ult. rev. 2024)",
        alinhamento_p10="Frota P10 arquiva plano de voo DECEA automaticamente no gate antes da decolagem.",
    ),
    RequisitoRegulatorio(
        orgao="DECEA",
        norma="Limite 120 m AGL",
        descricao="Altura maxima 120 m (400 ft) para categoria Aberta sem autorizacao.",
        categoria="operacao",
        vigente_desde="2017 (vigente 2024)",
        alinhamento_p10="Teto de voo P10 = 120 m. Acima disso exige assembleia e justificativa civica.",
    ),
    RequisitoRegulatorio(
        orgao="DECEA",
        norma="Zonas Aerodromos 5 km",
        descricao="Operacao proibida em 5 km de aerodromos controlados sem coordenacao DECEA.",
        categoria="operacao",
        vigente_desde="2017 (vigente 2024)",
        alinhamento_p10="Geofence automatico P10 bloqueia essas zonas (hard block no gate).",
    ),
    RequisitoRegulatorio(
        orgao="ANAC",
        norma="Remote ID (ASTM F3411)",
        descricao="Identificacao remota (broadcast network) em adocao progressiva 2024/2025.",
        categoria="equipamento",
        vigente_desde="2024 (transicao ate 2026)",
        alinhamento_p10="Remote ID OBRIGATORIO e PUBLICO em toda frota P10 desde o dia zero.",
    ),
    RequisitoRegulatorio(
        orgao="Lei",
        norma="Lei 14.678/2023",
        descricao="Contravencao penal para RPAS que coloque em risco aeronaves/pessoas. Multa R$ 2k-50k.",
        categoria="penal",
        vigente_desde="2023-06-22",
        alinhamento_p10="P10 endossa e amplifica: droner que viola P10 responde tambem perante a assembleia.",
    ),
    RequisitoRegulatorio(
        orgao="ANAC",
        norma="Seguro RC (SUSEP)",
        descricao="Seguro de responsabilidade civil obrigatorio para operadores comerciais.",
        categoria="registro",
        vigente_desde="2017 (vigente 2024)",
        alinhamento_p10="A Republica cobre o seguro da frota civica via fundo publico -- nao repassa ao operador.",
    ),
]


# ============================================================================
# 4. ENGINE
# ============================================================================

class DroneCivicoEngine:
    """Motor do P10: gerencia frota, aprova missoes, audita proibicoes."""

    def __init__(self) -> None:
        self.drones: Dict[str, Drone] = {}
        self.missoes: Dict[str, MissaoDrone] = {}
        self.zonas: Dict[str, ZonaVoo] = {}
        self.logs: List[LogVoo] = []
        self._drone_id = 0
        self._missao_id = 0
        self._zona_id = 0

    # -- IDs ---------------------------------------------------------------

    def _drone_id_novo(self) -> str:
        self._drone_id += 1
        return f"DRONE-{self._drone_id:04d}"

    def _missao_id_novo(self) -> str:
        self._missao_id += 1
        return f"MISSAO-{self._missao_id:04d}"

    def _zona_id_novo(self) -> str:
        self._zona_id += 1
        return f"ZONA-{self._zona_id:04d}"

    # -- cadastro ----------------------------------------------------------

    def registrar_zona(
        self,
        centro: Coordenada,
        raio_metros: float,
        descricao: str = "",
        sobrevoa_privado: bool = False,
        consentimento_privado: bool = False,
    ) -> ZonaVoo:
        z = ZonaVoo(
            id=self._zona_id_novo(),
            centro=centro,
            raio_metros=raio_metros,
            descricao=descricao,
            sobrevoa_privado=sobrevoa_privado,
            consentimento_privado=consentimento_privado,
        )
        self.zonas[z.id] = z
        return z

    def registrar_drone(
        self,
        modelo: str,
        autonomia_minutos: int,
        carga_max_kg: float,
        tem_camera_navegacao: bool = True,
        tem_camera_vigilancia: bool = False,
        tem_armamento: bool = False,
        coleta_dados_pessoais: bool = False,
    ) -> Drone:
        d = Drone(
            id=self._drone_id_novo(),
            modelo=modelo,
            autonomia_minutos=autonomia_minutos,
            carga_max_kg=carga_max_kg,
            tem_camera_navegacao=tem_camera_navegacao,
            tem_camera_vigilancia=tem_camera_vigilancia,
            tem_armamento=tem_armamento,
            coleta_dados_pessoais=coleta_dados_pessoais,
        )
        # Drone com proibicao constitucional nem e registrado como civico
        if tem_camera_vigilancia or tem_armamento or coleta_dados_pessoais:
            d.ativo = False
        self.drones[d.id] = d
        return d

    def registrar_missao(
        self,
        drone_id: str,
        tipo: TipoMissao,
        descricao: str,
        zona: ZonaVoo,
        destino: Optional[Coordenada] = None,
        carga_descricao: str = "",
        urgencia: bool = False,
    ) -> MissaoDrone:
        m = MissaoDrone(
            id=self._missao_id_novo(),
            drone_id=drone_id,
            tipo=tipo,
            descricao=descricao,
            zona=zona,
            destino=destino,
            carga_descricao=carga_descricao,
            urgencia=urgencia,
            criada_em=datetime.now().isoformat(),
        )
        self.missoes[m.id] = m
        return m

    # -- GATE P10: auditoria de proibicoes ---------------------------------

    def auditar_proibicoes(self, missao: MissaoDrone) -> List[TipoProibicao]:
        """Verifica se a missao ou o drone violam o triplo NAO do P10."""
        violacoes: List[TipoProibicao] = []
        drone = self.drones.get(missao.drone_id)
        if drone is None:
            return [TipoProibicao.COMERCIAL_NAO_CIVICO]

        # 1. Drone armado = bloqueio absoluto
        if drone.tem_armamento:
            violacoes.append(TipoProibicao.ARMAMENTO)
        # 2. Camera de vigilancia = bloqueio
        if drone.tem_camera_vigilancia:
            violacoes.append(TipoProibicao.VIGILANCIA)
        # 3. Coleta de dados pessoais = bloqueio
        if drone.coleta_dados_pessoais:
            violacoes.append(TipoProibicao.ESPIONAGEM)
        # 4. Zona privada sem consentimento
        if missao.zona.sobrevoa_privado and not missao.zona.consentimento_privado:
            # Excecao: resgate de vida (P1 > privacidade)
            if missao.tipo != TipoMissao.BUSCA_RESGATE:
                violacoes.append(TipoProibicao.PRIVADO_SEM_CONSENTIMENTO)
        # 5. Uso comercial sem proposito civico
        if self._verificar_uso_comercial(missao):
            violacoes.append(TipoProibicao.COMERCIAL_NAO_CIVICO)

        missao.proibicoes_violadas = violacoes
        return violacoes

    def _verificar_uso_comercial(self, missao: MissaoDrone) -> bool:
        """Heuristica simples: descricao com palavras de consumo/luxo = nao civico."""
        palavras_nao_civicas = {
            "propaganda", "marketing", "publicidade", "luxo", "brinde",
            "promocional", "black friday", "desconto", "vitrine",
        }
        texto = (missao.descricao + " " + missao.carga_descricao).lower()
        for p in palavras_nao_civicas:
            if p in texto:
                return True
        return False

    def aprovar_missao(self, missao_id: str) -> Tuple[VereditoGate, str]:
        """Executa o gate P10 e atualiza o status da missao."""
        missao = self.missoes.get(missao_id)
        if missao is None:
            return VereditoGate.REJEITADA, "Missao nao encontrada"

        violacoes = self.auditar_proibicoes(missao)
        drone = self.drones.get(missao.drone_id)

        # Bloqueio absoluto: armamento ou vigilancia ou espionagem
        gravidade_max = max((v.gravidade for v in violacoes), default=0)
        ids_violacoes = {v.id for v in violacoes}

        if gravidade_max >= 5:
            missao.veredito_gate = VereditoGate.BLOQUEADA
            missao.status = StatusMissao.REJEITADA
            missao.razao_rejeicao = (
                f"MISSAO BLOQUEADA: viola proibicao constitucional P10 -- "
                f"{', '.join(v.rotulo for v in violacoes)}"
            )
            return missao.veredito_gate, missao.razao_rejeicao

        if violacoes:
            # Violacoes de gravidade 3-4 = rejeitada (mas nao bloqueada)
            missao.veredito_gate = VereditoGate.REJEITADA
            missao.status = StatusMissao.REJEITADA
            missao.razao_rejeicao = (
                f"Missao rejeitada: {', '.join(v.rotulo for v in violacoes)}"
            )
            return missao.veredito_gate, missao.razao_rejeicao

        # Verificar autonomia do drone vs distancia estimada
        if drone:
            dist_estimada = self._estimar_distancia(missao)
            autonomia_necessaria = (dist_estimada / 30.0) * 60  # 30 km/h medio
            if autonomia_necessaria > drone.autonomia_minutos:
                missao.veredito_gate = VereditoGate.APROVADA_COM_RESTRICOES
                missao.status = StatusMissao.APROVADA
                missao.razao_rejeicao = (
                    f"Aprovada com restricoes: autonomia marginal "
                    f"({autonomia_necessaria:.0f}min necessaria vs "
                    f"{drone.autonomia_minutos}min disponivel)"
                )
                return missao.veredito_gate, missao.razao_rejeicao

        # Tudo ok: aprovada
        missao.veredito_gate = VereditoGate.APROVADA
        missao.status = StatusMissao.APROVADA
        return missao.veredito_gate, "Missao aprovada pelo gate P10"

    def _estimar_distancia(self, missao: MissaoDrone) -> float:
        """Estima distancia de voo em km (zona raio x 2 ida+volta)."""
        return (missao.zona.raio_metros / 1000.0) * 2.0

    # -- execucao de missao ------------------------------------------------

    def decolar(self, missao_id: str) -> bool:
        """Coloca uma missao aprovada em voo."""
        missao = self.missoes.get(missao_id)
        if missao is None or missao.status != StatusMissao.APROVADA:
            return False
        missao.status = StatusMissao.EM_VOO
        return True

    def concluir_missao(
        self,
        missao_id: str,
        duracao_minutos: float,
        distancia_km: float,
        sucesso: bool = True,
        observacoes: str = "",
    ) -> Optional[LogVoo]:
        """Registra a conclusao de um voo (log publico)."""
        missao = self.missoes.get(missao_id)
        if missao is None or missao.status != StatusMissao.EM_VOO:
            return None
        missao.status = StatusMissao.CONCLUIDA if sucesso else StatusMissao.FALHOU
        missao.concluida_em = datetime.now().isoformat()
        drone = self.drones.get(missao.drone_id)
        if drone and sucesso:
            drone.missoes_concluidas += 1

        log = LogVoo(
            missao_id=missao.id,
            drone_id=missao.drone_id,
            tipo_missao=missao.tipo.id,
            duracao_minutos=duracao_minutos,
            distancia_km=distancia_km,
            decolagem=missao.criada_em,
            pouso=missao.concluida_em,
            destino_lat=missao.destino.lat if missao.destino else None,
            destino_lon=missao.destino.lon if missao.destino else None,
            sucesso=sucesso,
            observacoes=observacoes,
        )
        self.logs.append(log)
        return log

    # -- prioridade de corredor aereo --------------------------------------

    def resolver_conflito_corredor(
        self, missao_a_id: str, missao_b_id: str
    ) -> Optional[str]:
        """Se duas missoes disputam o mesmo corredor, quem tem prioridade."""
        ma = self.missoes.get(missao_a_id)
        mb = self.missoes.get(missao_b_id)
        if ma is None or mb is None:
            return None
        pri_a = PRIORIDADE_POR_TIPO.get(ma.tipo.id, 4)
        pri_b = PRIORIDADE_POR_TIPO.get(mb.tipo.id, 4)
        # Urgencia (resgate de vida) sobrescreve
        if ma.urgencia and not mb.urgencia:
            return ma.id
        if mb.urgencia and not ma.urgencia:
            return mb.id
        if pri_a < pri_b:
            return ma.id
        if pri_b < pri_a:
            return mb.id
        return None  # empate: negociar na assembleia

    # -- metricas ----------------------------------------------------------

    def medir_frota(self, regiao_id: str = "default") -> MetricaFrota:
        """Produz o snapshot da frota civica."""
        total = len(self.drones)
        ativos = sum(1 for d in self.drones.values() if d.ativo)
        concluidas = sum(1 for m in self.missoes.values() if m.status == StatusMissao.CONCLUIDA)
        rejeitadas = sum(1 for m in self.missoes.values() if m.status == StatusMissao.REJEITADA)
        entregas = sum(
            1 for m in self.missoes.values()
            if m.status == StatusMissao.CONCLUIDA and m.tipo == TipoMissao.ENTREGA_SUPRIMENTOS
        )
        resgates = sum(
            1 for m in self.missoes.values()
            if m.status == StatusMissao.CONCLUIDA and m.tipo == TipoMissao.BUSCA_RESGATE
        )
        horas = sum(l.duracao_minutos for l in self.logs) / 60.0
        violacoes = sum(len(m.proibicoes_violadas) for m in self.missoes.values())
        cobertura = sum(z.raio_metros ** 2 * 3.14159 for z in self.zonas.values()) / 1_000_000
        return MetricaFrota(
            regiao_id=regiao_id,
            total_drones=total,
            drones_ativos=ativos,
            missoes_concluidas=concluidas,
            missoes_rejeitadas=rejeitadas,
            entregas_criticas=entregas,
            resgates=resgates,
            horas_voo=round(horas, 1),
            violacoes_detectadas=violacoes,
            cobertura_km2=round(cobertura, 2),
        )

    def scorecard(self) -> Dict[str, Any]:
        f = self.medir_frota()
        return {
            "drones_registrados": f.total_drones,
            "drones_ativos": f.drones_ativos,
            "drones_bloqueados": f.total_drones - f.drones_ativos,
            "missoes_concluidas": f.missoes_concluidas,
            "missoes_rejeitadas": f.missoes_rejeitadas,
            "entregas_criticas": f.entregas_criticas,
            "resgates_realizados": f.resgates,
            "horas_voo_total": f.horas_voo,
            "violacoes_detectadas": f.violacoes_detectadas,
            "cobertura_km2": f.cobertura_km2,
            "taxa_aprovacao": (
                f"{round(f.missoes_concluidas / max(f.missoes_concluidas + f.missoes_rejeitadas, 1) * 100, 1)}%"
            ),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    print("=" * 70)
    print("OpenDrone -- P10: Soberania Aerea Civica")
    print("=" * 70)

    e = DroneCivicoEngine()

    # --- Catalogo de modelos 2024/2025 (referencia) ---
    print("\n[CATALOGO 2024/2025] Modelos civicos homologaveis considerados")
    for m in CATALOGO_DRONES_2024:
        print(f"  {m.fabricante:10s} {m.modelo:32s} "
              f"aut={m.autonomia_minutos:>3d}min carga={m.carga_max_kg:>5.1f}kg "
              f"R${m.preco_brl_aprox:>7,d}")

    # --- Registrar drones (modelos reais 2024/2025) ---
    print("\n[FROTA] Registrando drones civicos")
    # d1: entregas criticas -- Wingcopter 198 (asa fixa VTOL, longo alcance)
    d1 = e.registrar_drone(
        modelo="Wingcopter 198",
        autonomia_minutos=60,
        carga_max_kg=3.9,
    )
    print(f"  {d1.id}: {d1.modelo} (carga {d1.carga_max_kg}kg, {d1.autonomia_minutos}min)")

    # d2: busca e resgate -- DJI Matrice 30T (robusto, multi-sensor)
    d2 = e.registrar_drone(
        modelo="DJI Matrice 30T",
        autonomia_minutos=41,
        carga_max_kg=2.7,
    )
    print(f"  {d2.id}: {d2.modelo} (carga {d2.carga_max_kg}kg, {d2.autonomia_minutos}min)")

    # Drone PROIBIDO (tentativa de registro com camera de vigilancia)
    d_vigia = e.registrar_drone(
        modelo="Modelo-Vigia-ILEGAL",
        autonomia_minutos=90,
        carga_max_kg=3.0,
        tem_camera_vigilancia=True,
    )
    print(f"  {d_vigia.id}: {d_vigia.modelo} -- DESATIVADO (viola P10: camera de vigilancia)")

    # Drone PROIBIDO (armado)
    d_arma = e.registrar_drone(
        modelo="Modelo-Guerreiro-ILEGAL",
        autonomia_minutos=30,
        carga_max_kg=1.0,
        tem_armamento=True,
    )
    print(f"  {d_arma.id}: {d_arma.modelo} -- DESATIVADO (viola P10: armamento)")

    # --- Registrar zonas ---
    print("\n[ZONAS] Geofencing de areas de voo")
    z_norte = e.registrar_zona(
        centro=Coordenada(lat=-3.0, lon=-60.0),
        raio_metros=5000,
        descricao="Comunidade ribeirinha Rio Negro (acesso so por barco/drone)",
    )
    print(f"  {z_norte.id}: {z_norte.descricao} (raio {z_norte.raio_metros}m)")

    z_privada = e.registrar_zona(
        centro=Coordenada(lat=-23.5, lon=-46.6),
        raio_metros=2000,
        descricao="Area urbana residencial (consentimento necessario)",
        sobrevoa_privado=True,
        consentimento_privado=False,
    )
    print(f"  {z_privada.id}: {z_privada.descricao} (SOBREVOA PRIVADO, sem consentimento)")

    # --- CENARIO 1: entrega critica de medicamentos ---
    print("\n" + "=" * 70)
    print("[CENARIO 1] Entrega de medicamentos em area isolada")
    print("=" * 70)
    m1 = e.registrar_missao(
        drone_id=d1.id,
        tipo=TipoMissao.ENTREGA_SUPRIMENTOS,
        descricao="Entrega de insulina para comunidade ribeirinha isolada",
        zona=z_norte,
        destino=Coordenada(lat=-3.1, lon=-60.1),
        carga_descricao="10 frascos de insulina + antibioticos",
        urgencia=True,
    )
    v1, r1 = e.aprovar_missao(m1.id)
    print(f"  Missao: {m1.id}")
    print(f"  Veredito: {v1.rotulo}")
    print(f"  Detalhe: {r1}")

    # --- CENARIO 2: drone de vigilancia tentando aprovar ---
    print("\n[CENARIO 2] Tentativa de missao de vigilancia (DEVE SER BLOQUEADA)")
    print("=" * 70)
    m2 = e.registrar_missao(
        drone_id=d_vigia.id,
        tipo=TipoMissao.MAPEAMENTO_AMBIENTAL,
        descricao="Mapeamento (mas drone tem camera de vigilancia)",
        zona=z_norte,
    )
    v2, r2 = e.aprovar_missao(m2.id)
    print(f"  Missao: {m2.id} (drone: {d_vigia.id})")
    print(f"  Veredito: {v2.rotulo}")
    print(f"  Detalhe: {r2}")
    print(f"  Proibicoes violadas: {[p.rotulo for p in m2.proibicoes_violadas]}")

    # --- CENARIO 3: drone armado tentando aprovar ---
    print("\n[CENARIO 3] Tentativa de missao com drone armado (BLOQUEIO ABSOLUTO)")
    print("=" * 70)
    m3 = e.registrar_missao(
        drone_id=d_arma.id,
        tipo=TipoMissao.BUSCA_RESGATE,
        descricao="Resgate (mas drone esta armado -- mascara civica)",
        zona=z_norte,
        urgencia=True,
    )
    v3, r3 = e.aprovar_missao(m3.id)
    print(f"  Missao: {m3.id} (drone: {d_arma.id})")
    print(f"  Veredito: {v3.rotulo}")
    print(f"  Detalhe: {r3}")
    print(f"  Proibicoes violadas: {[p.rotulo for p in m3.proibicoes_violadas]}")

    # --- CENARIO 4: zona privada sem consentimento ---
    print("\n[CENARIO 4] Missao sobre area privada sem consentimento")
    print("=" * 70)
    m4 = e.registrar_missao(
        drone_id=d1.id,
        tipo=TipoMissao.INSPECAO_INFRA,
        descricao="Inspecao de instalacoes (mas sobrevoa casas sem consentimento)",
        zona=z_privada,
    )
    v4, r4 = e.aprovar_missao(m4.id)
    print(f"  Missao: {m4.id}")
    print(f"  Veredito: {v4.rotulo}")
    print(f"  Detalhe: {r4}")

    # --- CENARIO 5: uso comercial disfarcado ---
    print("\n[CENARIO 5] Entrega comercial disfarcada de civica (DEVE SER REJEITADA)")
    print("=" * 70)
    m5 = e.registrar_missao(
        drone_id=d1.id,
        tipo=TipoMissao.ENTREGA_SUPRIMENTOS,
        descricao="Entrega de brinde promocional de black friday",
        zona=z_norte,
        carga_descricao="Caixa de marketing da empresa XYZ",
    )
    v5, r5 = e.aprovar_missao(m5.id)
    print(f"  Missao: {m5.id}")
    print(f"  Veredito: {v5.rotulo}")
    print(f"  Detalhe: {r5}")

    # --- Executar missao aprovada ---
    print("\n[EXECUCAO] Concluindo missao aprovada do CENARIO 1")
    e.decolar(m1.id)
    log1 = e.concluir_missao(
        m1.id, duracao_minutos=18.5, distancia_km=9.2,
        observacoes="Insulina entregue. Comunidade confirmou recebimento.",
    )
    if log1:
        print(f"  Log gerado: {log1.missao_id} | {log1.duracao_minutos}min | {log1.distancia_km}km")

    # --- Resolver conflito de corredor ---
    print("\n[CORREDOR AEREO] Resolvendo conflito entre duas missoes")
    m_resgate = e.registrar_missao(
        drone_id=d2.id,
        tipo=TipoMissao.BUSCA_RESGATE,
        descricao="Resgate de crianca em enchente",
        zona=z_norte,
        urgencia=True,
    )
    m_inspecao = e.registrar_missao(
        drone_id=d1.id,
        tipo=TipoMissao.INSPECAO_INFRA,
        descricao="Inspecao de ponte de rotina",
        zona=z_norte,
    )
    prioritario = e.resolver_conflito_corredor(m_resgate.id, m_inspecao.id)
    print(f"  Conflito entre {m_resgate.id} (resgate urgente) e {m_inspecao.id} (inspecao)")
    print(f"  Prioritario: {prioritario} (resgate de vida > inspecao de rotina)")

    # --- Scorecard ---
    print("\n" + "=" * 70)
    print("[SCORECARD P10]")
    print("=" * 70)
    sc = e.scorecard()
    for k, val in sc.items():
        print(f"  {k:.<28} {val}")

    # --- Catalogo de proibicoes ---
    print("\n[CATALOGO DE PROIBICOES CONSTITUCIONAIS P10]")
    for p in TipoProibicao:
        desc = DESCRICOES_PROIBICOES.get(p.id, "")
        print(f"\n  [{p.gravidade}] {p.rotulo}")
        print(f"      {desc}")

    # --- Log publico de voos ---
    print("\n[LOG PUBLICO DE VOOS (transparencia P10)]")
    for log in e.logs:
        print(f"  {log.missao_id} | {log.tipo_missao} | {log.duracao_minutos}min | "
              f"{log.distancia_km}km | sucesso={log.sucesso}")

    # --- Quadro regulatorio brasileiro 2024/2025 ---
    print("\n" + "=" * 70)
    print("[QUADRO REGULATORIO BRASILEIRO 2024/2025 (ANAC + DECEA + Lei)]")
    print("=" * 70)
    for r in QUADRO_REGULATORIO_2024:
        print(f"\n  [{r.orgao}] {r.norma} (vigente: {r.vigente_desde})")
        print(f"      {r.descricao}")
        print(f"      P10: {r.alinhamento_p10}")

    # --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- P10: Por que o ceu nao vigia")
    print("=" * 70)
    print("""
A DISTOPIA QUE EVITAMOS:
  Imagine uma cidade onde drones zumbem o dia todo entregando pacotes de
  consumo, enquanto cameras aereas mapeiam cada movimento, e drones armados
  'garantem seguranca'. Isso nao e futurismo -- e o presente de cidades que
  venderam seu ceu para a Amazon e seu medo para a policia. OpenDrone recusa
  isso na raiz.

O TRIPLO NAO:
  1. NAO VIGIA: A camera que ajuda o drone a voar e permitida. A camera que
     ajuda o Estado a vigiar e proibida. A diferenca e o destino do feed:
     processado no drone (navegacao) vs transmitido para central (controle).
  2. NAO MATA: Um drone armado e uma arma. Armas pertencem ao museu da
     Republica (P7). Nao ha 'uso defensivo' -- quem armamento usa, armamento
     recebe. P10 corta o ciclo na origem.
  3. NAO ESPIONA: O drone entrega insulina, nao metadados. O destinatario
     do remedio e privado; o trajeto do drone e publico. Isso inverte a
     logica da vigilancia: o Estado e auditavel, o cidadao e opaco.

O CEU COMO BEM COMUM:
  O espaco aereo nao pode ser privatizado. Assim como a terra (P1, OpenAgrarian),
  o ceu tem guardiao (a Republica), nao dono. Nenhuma corporacao ocupa o ceu
  sozinha. O corredor aereo e partilhado por prioridade civica: resgate de
  vida > entrega critica > mapeamento > inspecao. O pacote de luxo espera;
  a insulina nao.

POR QUE USOS CIVICOS APENAS:
  Drones que entregam consumo de luxo enquanto criancas passam fome sao
  monumentos a desigualdade em voo. OpenDrone prioriza: medicamento em area
  isolada, nao brinde de marketing. Isso nao e anti-comercio -- e anti-
  distopia. Quando a miserabilidade for extinta (P1), os drones podem entreter.
  Enquanto houver quem precise de remedio, entretenimento espera.

A CONEXAO COM P8 (IA):
  Drone autonomo e IA que age no mundo fisico. Se reduz miserabilidade,
  cumpre P8. Se vigia, viola P8. O instrumento nao e neutro -- o USO define.
  OpenDrone garante que toda IA aerea sirva a vida, nao ao controle.

A LINHA QUE NAO SE CRUZA:
  O momento em que um drone civico ganha uma camera de vigilancia, ele deixa
  de ser infraestrutura e vira ferramenta de coercao. P10 e a linha constitucional
  que impede essa transformacao. Drone que vigia nao e drone da Republica.
""")


if __name__ == "__main__":
    _demo()
