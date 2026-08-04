#!/usr/bin/env python3
"""
OpenSchoolOSINT -- Verificacao por Fontes Abertas (OSINT)
============================================================
"Nem todo mundo pode ir la. Mas todo mundo pode OLHAR."

O PROBLEMA:
  179 mil escolas. Nem todo cidadao fiscalizador chega no sertao.
  Mas o Google Street View ja foi. O satelite tirou foto. O MapBiomas mapeou.

A SOLUCAO:
  Cross-reference de fontes abertas (OSINT) pra verificar escola
  SEM precisar ir la fisicamente.

  Street View: a fachada existe? Tem placa? O predio e real?
  Satelite: tem construcao nas coordenadas? Qual o tamanho?
  MapBiomas: a area e urbana? Rural? Floresta?
  OpenStreetMap: a escola esta mapeada? Fotos da comunidade?

  Cada fonte independente que confirma = +1 nivel de confianca.

FONTES OSINT MAPEADAS:
  1. Google Street View Static API
  2. Google Satellite (Earth)
  3. MapBiomas (satelite brasileiro, usos do solo)
  4. Sentinel-2 (ESA Copernicus, gratuito)
  5. OpenStreetMap / Mapillary
  6. Bing Maps Bird's Eye
  7. INPE (satelite nacional, QUEIMADAS, DEGRAD)

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ENUMS
# ============================================================================

class FonteOSINT(Enum):
    """Fontes de dados abertos para verificacao."""
    GOOGLE_STREET_VIEW = (
        "street_view",
        "Google Street View",
        "https://maps.googleapis.com/maps/api/streetview",
        "Fachada a nivel de rua. Resolve existencia, tipo de construcao.",
        "gratuito_parcial",
    )
    GOOGLE_SATELLITE = (
        "g_satellite",
        "Google Earth/Maps Satellite",
        "https://www.google.com/maps/@?api=1&map_action=map",
        "Vista aerea. Resolve area construida, contexto urbano/rural.",
        "gratuito",
    )
    GOOGLE_STATIC = (
        "g_static",
        "Google Static Maps API",
        "https://maps.googleapis.com/maps/api/staticmap",
        "Mapa estatico com marcador nas coordenadas.",
        "gratuito_parcial",
    )
    MAPBIOMAS = (
        "mapbiomas",
        "MapBiomas (Brasil)",
        "https://plataforma.brasil.mapbiomas.org",
        "Uso do solo. Floresta? Pasto? Cidade? Queimada?",
        "gratuito_total",
    )
    SENTINEL_2 = (
        "sentinel2",
        "Sentinel-2 (ESA Copernicus)",
        "https://scihub.copernicus.eu",
        "Imagem de satelite 10m resolucao. Atualizada a cada 5 dias.",
        "gratuito_total",
    )
    OPENSTREETMAP = (
        "osm",
        "OpenStreetMap",
        "https://overpass-api.de",
        "Comunidade mapeou? Tem foto? Tem tag amenity=school?",
        "gratuito_total",
    )
    MAPILLARY = (
        "mapillary",
        "Mapillary",
        "https://www.mapillary.com",
        "Street view colaborativo. Mais cobertura rural que Google.",
        "gratuito_total",
    )
    BING_BIRDSEYE = (
        "bing",
        "Bing Maps Bird's Eye",
        "https://www.bing.com/maps",
        "Vista obliqua (45graus). Resolve altura, telhado, janelas.",
        "gratuito",
    )
    INPE_QUEIMADAS = (
        "inpe",
        "INPE Queimadas / Deter",
        "http://terrabrasilis.dpi.inpe.br",
        "Satelite nacional. Queimada proxima? Desmatamento?",
        "gratuito_total",
    )
    OSM_PHOTO = (
        "osm_photo",
        "WikiCommons / OSM Photos",
        "https://commons.wikimedia.org",
        "Fotos da comunidade. Nem sempre tem mas quando tem e OURO.",
        "gratuito_total",
    )

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def nome(self) -> str:
        return self.value[1]

    @property
    def url(self) -> str:
        return self.value[2]

    @property
    def resolve(self) -> str:
        return self.value[3]

    @property
    def custo(self) -> str:
        return self.value[4]


class TipoVerificacaoOSINT(Enum):
    """O que cada fonte OSINT consegue verificar."""
    EXISTENCIA = ("existencia", "O predio existe fisicamente?")
    TIPO_CONSTRUCAO = ("construcao", "Alvenaria? Madeira? Barraco?")
    FAZENDA_STATUS = ("fachada", "Fachada conservada? Abandonada?")
    AREA_CONSTRUIDA = ("area", "Tamanho da construcao visivel do ceu")
    CONTEXTO = ("contexto", "Urbano? Rural? Isolado? Floresta?")
    RODOVIA = ("rodovia", "Tem estrada chegando? Asfalto? Terra?")
    PROXIMIDADE_PERIGO = ("perigo", "Queimada? Desmatamento? Rio?")
    COMUNIDADE = ("comunidade", "Tem casas proximas? E habitado?")
    SAZONALIDADE = ("sazonal", "Muda entre seca e chuva? Escola inunda?")
    COMPARACAO_TEMPORAL = ("temporal", "Como era em 2015 vs 2024?")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class ConclusaoOSINT(Enum):
    """Conclusao da analise OSINT de uma escola."""
    CONFIRMA_EXISTENCIA = ("confirma", "OSINT confirma: escola existe e parece ativa")
    CONFIRMA_EXISTENCIA_DEGRADADA = ("degrada", "Existe mas em estado degradado")
    DIVERGE_STATUS = ("diverge", "Existe mas parece fechada/abandonada")
    NAO_ENCONTRADA = ("nao_achou", "Coordenadas nao mostram construcao")
    DUVIDOSA = ("duvidosa", "Tem algo nas coordenadas mas nao parece escola")
    SEM_COBERTURA = ("sem_cobertura", "Fonte OSINT nao tem cobertura da area")
    CONFLITO_FONTE = ("conflito", "Fontes OSINT conflitam entre si")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass
class VerificacaoOSINT:
    """Resultado de uma verificacao OSINT de uma escola."""
    cod_inep: str
    escola_nome: str
    latitude: float
    longitude: float
    fonte: FonteOSINT
    tipo_verificacao: TipoVerificacaoOSINT
    timestamp_coleta: str
    conclusao: ConclusaoOSINT
    evidencia_url: str             # URL da imagem/dado
    hash_evidencia: str            # hash da imagem baixada
    observacao: str = ""
    confianca_fonte: float = 0.0   # 0-1, quao confiavel esta verificacao
    recencia_dias: int = 0         # quantos dias desde a imagem/dado original


@dataclass
class PipelineOSINT:
    """Pipeline de verificacao OSINT para uma escola."""
    cod_inep: str
    verificacoes: List[VerificacaoOSINT] = field(default_factory=list)
    conclusao_agregada: Optional[ConclusaoOSINT] = None
    confianca_agregada: float = 0.0
    discrepancias_vs_inep: List[str] = field(default_factory=list)


# ============================================================================
# 3. MAPEAMENTO: O QUE CADA FONTE RESOLVE
# ============================================================================

def _init_capacidades() -> Dict[str, List[str]]:
    """O que cada fonte OSINT consegue verificar."""
    return {
        "street_view": [
            "existencia", "construcao", "fachada", "comunidade",
        ],
        "g_satellite": [
            "existencia", "area", "contexto", "rodovia",
            "perigo", "comunidade", "sazonal", "temporal",
        ],
        "mapbiomas": [
            "contexto", "perigo", "sazonal", "temporal",
        ],
        "sentinel2": [
            "existencia", "area", "contexto", "sazonal", "temporal",
        ],
        "osm": [
            "existencia", "comunidade",
        ],
        "mapillary": [
            "existencia", "construcao", "fachada", "rodovia",
        ],
        "bing": [
            "existencia", "construcao", "area", "fachada",
        ],
        "inpe": [
            "perigo", "sazonal",
        ],
        "osm_photo": [
            "existencia", "construcao", "fachada",
        ],
    }


# ============================================================================
# 4. SISTEMA OSINT
# ============================================================================

class SchoolOSINT:
    """
    Verificacao de escola por fontes abertas (OSINT).

    Nem todo mundo chega no sertao. Mas o satelite ja foi.
    O Street View ja passou. O MapBiomas ja mapeou.
    """

    NOME = "OpenSchoolOSINT"
    VERSAO = "0.1.0-spec"

    def __init__(self) -> None:
        self.fontes: List[FonteOSINT] = list(FonteOSINT)
        self.capacidades: Dict[str, List[str]] = _init_capacidades()

    # -- fontes ------------------------------------------------------------

    def todas_fontes(self) -> List[Dict[str, str]]:
        return [
            {"id": f.id, "nome": f.nome, "url": f.url,
             "resolve": f.resolve, "custo": f.custo}
            for f in self.fontes
        ]

    def fontes_gratuitas_total(self) -> List[FonteOSINT]:
        return [f for f in self.fontes if f.custo == "gratuito_total"]

    def fontes_por_verificacao(self, tipo: str) -> List[FonteOSINT]:
        """Quais fontes conseguem fazer este tipo de verificacao."""
        return [
            f for f in self.fontes
            if tipo in self.capacidades.get(f.id, [])
        ]

    # -- URLs de coleta -----------------------------------------------------

    def url_street_view(self, lat: float, lon: float,
                        heading: int = 0, pitch: int = 0,
                        size: str = "640x640") -> str:
        """
        Gera URL do Google Street View Static API.

        heading: 0=Norte, 90=Leste, 180=Sul, 270=Oeste
        pitch: 0=horizontal, 90=cima, -90=baixo
        size: max 640x640 no tier gratuito
        """
        return (
            f"https://maps.googleapis.com/maps/api/streetview"
            f"?size={size}&location={lat},{lon}"
            f"&heading={heading}&pitch={pitch}&fov=90"
            f"&key=${{GOOGLE_MAPS_API_KEY}}"
        )

    def url_street_view_4_direcoes(self, lat: float, lon: float) -> List[str]:
        """Gera 4 URLs olhando para N/S/L/O. Multiplos angulos = mais dados."""
        return [
            self.url_street_view(lat, lon, heading=h)
            for h in [0, 90, 180, 270]
        ]

    def url_satellite(self, lat: float, lon: float, zoom: int = 18) -> str:
        """Google Satellite via static maps."""
        return (
            f"https://maps.googleapis.com/maps/api/staticmap"
            f"?center={lat},{lon}&zoom={zoom}&size=640x640"
            f"&maptype=satellite"
            f"&key=${{GOOGLE_MAPS_API_KEY}}"
        )

    def url_sentinel2(self, lat: float, lon: float) -> str:
        """Sentinel-2 via Copernicus. 10m resolucao, atualizado 5 dias."""
        return (
            f"https://apps.sentinel-hub.com/eo-browser/"
            f"?zoom=16&lat={lat}&lng={lon}"
            f"&themeId=DEFAULT-THEME"
            f"&dataSource=S2_L2A"
        )

    def url_mapbiomas(self, lat: float, lon: float) -> str:
        """MapBiomas: uso do solo brasileiro."""
        return (
            f"https://plataforma.brasil.mapbiomas.org/mapa"
            f"?lat={lat}&lng={lon}&zoom=16"
        )

    def url_osm_overpass(self, lat: float, lon: float, raio_m: int = 500) -> str:
        """OpenStreetMap via Overpass: escolas em raio."""
        return (
            f"https://overpass-api.de/api/interpreter"
            f"?data=[out:json];"
            f"node[amenity=school](around:{raio_m},{lat},{lon});out;"
        )

    def url_mapillary(self, lat: float, lon: float) -> str:
        """Mapillary: street view colaborativo. Mais cobertura rural."""
        return (
            f"https://www.mapillary.com/app/"
            f"?lat={lat}&lng={lon}&z=16"
        )

    def url_inpe_queimadas(self, lat: float, lon: float) -> str:
        """INPE: queimadas e desmatamento proximo."""
        return (
            f"http://terrabrasilis.dpi.inpe.br/queimadas/portal-static"
            f"?lat={lat}&lng={lon}"
        )

    # -- pipeline -----------------------------------------------------------

    def pipeline_completo(self, lat: float, lon: float,
                          cod_inep: str) -> List[Dict[str, Any]]:
        """
        Pipeline completo de verificacao OSINT para uma escola.
        Ordem: do barato/confiavel pro caro/duvidoso.
        """
        return [
            {
                "passo": 1,
                "fonte": "osm",
                "acao": "Verificar se comunidade mapeou a escola",
                "url": self.url_osm_overpass(lat, lon),
                "esperado": "tag amenity=school proxima das coordenadas",
                "custo": "gratis",
            },
            {
                "passo": 2,
                "fonte": "g_satellite",
                "acao": "Satelite: tem construcao nas coordenadas?",
                "url": self.url_satellite(lat, lon),
                "esperado": "Estrutura visivel do ceu",
                "custo": "gratis",
            },
            {
                "passo": 3,
                "fonte": "sentinel2",
                "acao": "Sentinel-2: imagem recente (5 dias)",
                "url": self.url_sentinel2(lat, lon),
                "esperado": "Imagem atualizada confirma construcao",
                "custo": "gratis",
            },
            {
                "passo": 4,
                "fonte": "street_view",
                "acao": "Street View: fachada da escola",
                "url": self.url_street_view(lat, lon),
                "esperado": "Predio visivel, placa, entrada",
                "custo": "gratis (API key)",
            },
            {
                "passo": 5,
                "fonte": "street_view",
                "acao": "Street View: 4 direcoes (N/S/L/O)",
                "url": ",".join(self.url_street_view_4_direcoes(lat, lon)),
                "esperado": "Contexto: casas? vegetacao? estrada?",
                "custo": "gratis (API key)",
            },
            {
                "passo": 6,
                "fonte": "mapillary",
                "acao": "Mapillary: cobertura colaborativa (rural)",
                "url": self.url_mapillary(lat, lon),
                "esperado": "Street view onde Google nao foi",
                "custo": "gratis",
            },
            {
                "passo": 7,
                "fonte": "bing",
                "acao": "Bing Bird's Eye: vista 45graus",
                "url": f"https://www.bing.com/maps?cp={lat}~{lon}&lvl=16&style=b",
                "esperado": "Altura, telhado, numero de pavimentos",
                "custo": "gratis",
            },
            {
                "passo": 8,
                "fonte": "mapbiomas",
                "acao": "MapBiomas: uso do solo ao redor",
                "url": self.url_mapbiomas(lat, lon),
                "esperado": "Area urbana? Rural? Floresta? Queimada?",
                "custo": "gratis",
            },
            {
                "passo": 9,
                "fonte": "inpe",
                "acao": "INPE: queimada/desmatamento proximo",
                "url": self.url_inpe_queimadas(lat, lon),
                "esperado": "Risco ambiental identificado",
                "custo": "gratis",
            },
            {
                "passo": 10,
                "fonte": "g_satellite",
                "acao": "Comparacao temporal: 2015 vs 2024",
                "url": self.url_satellite(lat, lon) + "&hist=2015",
                "esperado": "Mudanca na construcao ao longo do tempo",
                "custo": "gratis",
            },
        ]

    # -- analise agregada ---------------------------------------------------

    def analisar_pipeline(self, pipeline: PipelineOSINT) -> Dict[str, Any]:
        """Agrega conclusoes de multiplas fontes OSINT."""
        if not pipeline.verificacoes:
            return {
                "conclusao": ConclusaoOSINT.SEM_COBERTURA,
                "confianca": 0.0,
                "n_fontes": 0,
            }

        conclusoes = [v.conclusao for v in pipeline.verificacoes]
        confiancas = [v.confianca_fonte for v in pipeline.verificacoes]

        # Se 2+ fontes confirmam existencia
        n_confirma = sum(1 for c in conclusoes if c == ConclusaoOSINT.CONFIRMA_EXISTENCIA)
        n_degrada = sum(1 for c in conclusoes if c == ConclusaoOSINT.CONFIRMA_EXISTENCIA_DEGRADADA)
        n_nao = sum(1 for c in conclusoes if c == ConclusaoOSINT.NAO_ENCONTRADA)
        n_conflito = sum(1 for c in conclusoes if c == ConclusaoOSINT.CONFLITO_FONTE)

        if n_confirma >= 2:
            conclusao = ConclusaoOSINT.CONFIRMA_EXISTENCIA
        elif n_confirma >= 1 and n_degrada >= 1:
            conclusao = ConclusaoOSINT.CONFIRMA_EXISTENCIA_DEGRADADA
        elif n_nao >= 2:
            conclusao = ConclusaoOSINT.NAO_ENCONTRADA
        elif n_conflito >= 1:
            conclusao = ConclusaoOSINT.CONFLITO_FONTE
        elif n_confirma == 1:
            conclusao = ConclusaoOSINT.DUVIDOSA
        else:
            conclusao = ConclusaoOSINT.SEM_COBERTURA

        confianca = sum(confiancas) / len(confiancas) if confiancas else 0.0

        pipeline.conclusao_agregada = conclusao
        pipeline.confianca_agregada = confianca

        return {
            "conclusao": conclusao,
            "confianca": round(confianca, 2),
            "n_fontes": len(pipeline.verificacoes),
            "n_confirma": n_confirma,
            "n_degrada": n_degrada,
            "n_nao_achou": n_nao,
        }

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "fontes_osint": len(self.fontes),
            "fontes_gratuitas_total": len(self.fontes_gratuitas_total()),
            "tipos_verificacao": len(list(TipoVerificacaoOSINT)),
            "conclusoes_possiveis": len(list(ConclusaoOSINT)),
            "passos_pipeline": 10,
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    osint = SchoolOSINT()

    print("=" * 70)
    print(f"{osint.NOME} v{osint.VERSAO} -- Verificacao por Fontes Abertas")
    print("=" * 70)

    # --- Fontes ---
    print(f"\n[FONTES OSINT ({len(osint.fontes)})]\n")
    print(f"  {'ID':<16} {'NOME':<30} {'CUSTO':<18} {'RESOLVE'}")
    print(f"  {'-'*100}")
    for f in osint.fontes:
        print(f"  {f.id:<16} {f.nome:<30} {f.custo:<18} {f.resolve[:40]}")

    # --- Capatices ---
    print(f"\n\n[CAPACIDADES POR FONTE]\n")
    for fonte_id, caps in sorted(osint.capacidades.items()):
        print(f"  {fonte_id:<16} -> {', '.join(caps)}")

    # --- Pipeline exemplo ---
    lat, lon = -3.7234, -40.4122  # escola do sertao (Sobral/CE)
    print(f"\n\n[PIPELINE OSINT -- Escola Sertao Sobral/CE]\n")
    print(f"  Coordenadas: {lat}, {lon}\n")
    pipeline = osint.pipeline_completo(lat, lon, "26123456")
    for p in pipeline:
        print(f"  Passo {p['passo']:>2}: [{p['fonte']}] {p['acao']}")
        print(f"    URL: {p['url'][:80]}...")
        print(f"    Esperado: {p['esperado']}")
        print()

    # --- Simulacao: analise agregada ---
    print("[SIMULACAO: 3 fontes confirmam, 1 diverge]\n")
    pl = PipelineOSINT(cod_inep="26123456")
    pl.verificacoes = [
        VerificacaoOSINT(
            "26123456", "Escola Joao Pereira", lat, lon,
            FonteOSINT.GOOGLE_SATELLITE, TipoVerificacaoOSINT.EXISTENCIA,
            "2024-07-04T10:00:00", ConclusaoOSINT.CONFIRMA_EXISTENCIA,
            "url_satellite", "abc123",
            "Construcao visivel nas coordenadas",
            0.85, 365,
        ),
        VerificacaoOSINT(
            "26123456", "Escola Joao Pereira", lat, lon,
            FonteOSINT.OPENSTREETMAP, TipoVerificacaoOSINT.EXISTENCIA,
            "2024-07-04T10:01:00", ConclusaoOSINT.CONFIRMA_EXISTENCIA,
            "url_osm", "def456",
            "Tag amenity=school encontrada a 50m",
            0.70, 100,
        ),
        VerificacaoOSINT(
            "26123456", "Escola Joao Pereira", lat, lon,
            FonteOSINT.SENTINEL_2, TipoVerificacaoOSINT.EXISTENCIA,
            "2024-07-04T10:02:00", ConclusaoOSINT.CONFIRMA_EXISTENCIA,
            "url_sentinel", "ghi789",
            "Imagem recente (5 dias) mostra construcao",
            0.80, 5,
        ),
        VerificacaoOSINT(
            "26123456", "Escola Joao Pereira", lat, lon,
            FonteOSINT.GOOGLE_STREET_VIEW, TipoVerificacaoOSINT.FAZENDA_STATUS,
            "2024-07-04T10:03:00", ConclusaoOSINT.CONFIRMA_EXISTENCIA_DEGRADADA,
            "url_street_view", "jkl012",
            "Predio existe mas fachada degradada, teto com problemas",
            0.90, 730,  # imagem de 2 anos atras
        ),
    ]
    resultado = osint.analisar_pipeline(pl)
    print(f"  Conclusao: {resultado['conclusao'].id} -- {resultado['conclusao'].rotulo}")
    print(f"  Confianca: {resultado['confianca']}")
    print(f"  Fontes: {resultado['n_fontes']} ({resultado['n_confirma']} confirmam, "
          f"{resultado['n_degrada']} degradada)")

    # --- Simulacao: escola fantasma ---
    print("\n\n[SIMULACAO: Escola Fantasma -- 2 fontes nao acham]\n")
    pl2 = PipelineOSINT(cod_inep="31987654")
    pl2.verificacoes = [
        VerificacaoOSINT(
            "31987654", "Escola Luz do Saber", -3.1, -60.0,
            FonteOSINT.GOOGLE_SATELLITE, TipoVerificacaoOSINT.EXISTENCIA,
            "2024-07-04T11:00:00", ConclusaoOSINT.NAO_ENCONTRADA,
            "url_sat", "xyz999",
            "Nenhuma construcao nas coordenadas. Floresta.",
            0.85, 365,
        ),
        VerificacaoOSINT(
            "31987654", "Escola Luz do Saber", -3.1, -60.0,
            FonteOSINT.SENTINEL_2, TipoVerificacaoOSINT.EXISTENCIA,
            "2024-07-04T11:01:00", ConclusaoOSINT.NAO_ENCONTRADA,
            "url_sent", "www888",
            "Imagem recente confirma: area sem construcao",
            0.80, 5,
        ),
    ]
    resultado2 = osint.analisar_pipeline(pl2)
    print(f"  Conclusao: {resultado2['conclusao'].id} -- {resultado2['conclusao'].rotulo}")
    print(f"  Confianca: {resultado2['confianca']}")
    print(f"  Fontes: {resultado2['n_fontes']} ({resultado2['n_nao_achou']} NAO acharam)")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = osint.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
