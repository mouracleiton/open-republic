#!/usr/bin/env python3
"""
OpenCensoEscolar -- Censo Escolar Proprio da Republica
========================================================
"O INEP pergunta ao diretor. Nos perguntamos ao chao."

O PROBLEMA:
  179.534 escolas no Censo INEP. Dado autopreenchido.
  Ninguem verifica. Ninguem vai la. Ninguem confia.

A SOLUCAO:
  Censo proprio. Cidadao fiscalizador vai la.
  Coleta, verifica, evidencia, publica.
  Offline-first. Funciona sem internet.
  Dado real, cruzado, com niveis de confianca.

DIFERENCA DO INEP:
  INEP:  diretor preenche -> sistema -> publico (ninguem verifica)
  NOSSO: cidadao vai la -> coleta + foto + GPS -> sincroniza -> publico
         OSINT cruza -> comunidade assina -> niveis de confianca

ARQUITETURA:
  1. COLETOR (app mobile, offline-first)
  2. SINCRONIZADOR (upload quando tem rede)
  3. CRUZADOR (INEP vs campo vs OSINT)
  4. VERIFICADOR (discrepancias automaticas)
  5. PUBLICADOR (dado aberto, auditavel, API)

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime


# ============================================================================
# 1. ENUMS
# ============================================================================

class TipoColetor(Enum):
    """Quem coleta o dado no campo."""
    CIDADAO_FISCALIZADOR = ("cidadao", "Cidadao voluntario treinado (P13)")
    PROFESSOR = ("professor", "Professor da propria escola (auto-coleta honesta)")
    COMUNIDADE = ("comunidade", "Lider comunitario, morador, pai de aluno")
    EQUIPE_REPUBLICA = ("equipe", "Equipe oficial da Republica (paga)")
    PARCEIRO = ("parceiro", "ONG, universidade, movimento social")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoDadoColeta(Enum):
    """Tipos de dado coletados no censo proprio."""
    # Identificacao
    GPS = ("gps", "GPS preciso (+/- 3m)")
    FOTO_FACHADA = ("foto_fachada", "Foto da fachada com placa")
    FOTO_INTERIOR = ("foto_interior", "Foto de sala, banheiro, cozinha")
    VIDEO_PERCURSO = ("video", "Video do percurso entrada->sala")
    # Infraestrutura
    AGUA = ("agua", "Agua: tem? potavel? origem?")
    ENERGIA = ("energia", "Energia: tem? origem? quantas horas/dia?")
    ESGOTO = ("esgoto", "Esgoto: rede? fossa? nada?")
    BANHEIRO = ("banheiro", "Banheiro: tem? funciona? tem porta/agua/papel?")
    COZINHA = ("cozinha", "Cozinha: tem? fogao funciona?")
    REFEITORIO = ("refeitorio", "Refeitorio: tem? quantos sentam?")
    INTERNET = ("internet", "Internet: tem? velocidade testada?")
    COMPUTADORES = ("computadores", "Computadores: quantos? quantos ligam?")
    BIBLIOTECA = ("biblioteca", "Biblioteca: tem? quantos livros?")
    QUADRA = ("quadra", "Quadra: tem? coberta?")
    ACESSIBILIDADE = ("a11y", "Acessibilidade: rampa? banheiro PNE?")
    SALAS = ("salas", "Salas: quantas existem? quantas em uso?")
    TELHADO = ("telhado", "Telhado: goteira? buraco? conservado?")
    # Pessoas
    ALUNOS_PRESENTES = ("alunos_presentes", "Contagem de alunos presentes HOJE")
    PROFESSORES_PRESENTES = ("prof_presentes", "Contagem de professores presentes HOJE")
    FUNCIONARIOS = ("funcionarios", "Funcionarios: quantos? quais?")
    # Comida
    MERENDA = ("merenda", "Merenda: tem hoje? tipo? ultima entrega?")
    CARDADIO = ("cardapio", "Cardapio fotografado (evidence)")
    # Seguranca
    VIOLANCIA = ("violencia", "Violencia na area? escola ja fechou por isso?")
    TRANSPORTE = ("transporte", "Transporte escolar funciona? que tipo?")
    # Comunidade
    DEPOIMENTO = ("depoimento", "Depoimento de 3+ moradores independentes")
    ASSINATURA = ("assinatura", "Assinatura digital de morador")
    # Documentos
    DOCUMENTO = ("documento", "Documento fotografado: portaria, ata, cardapio")
    # Medicoes
    MEDICAO_INTERNET = ("medicao_net", "Speedtest: download, upload, latencia")
    MEDICAO_AGUA = ("medicao_agua", "PH da agua, turbidez, cloro")
    MEDICAO_RUIDO = ("medicao_ruido", "Decibeis dentro da sala de aula")
    MEDICAO_LUZ = ("medicao_luz", "Lux dentro da sala (suficiente pra ler?)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusSincronizacao(Enum):
    """Status da sincronizacao do dado coletado."""
    PENDENTE = ("pendente", "Coletado, aguardando rede")
    SINCRONIZANDO = ("sincronizando", "Enviando")
    SINCRONIZADO = ("sincronizado", "No servidor, processado")
    CONFLITO = ("conflito", "Conflita com dado existente")
    REJEITADO = ("rejeitado", "Invalidado por revisao")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelCenso(Enum):
    """Nivel de profundidade do censo de uma escola."""
    RASO = ("raso", "Censo raso: GPS + foto + status (5 min)")
    PADRAO = ("padrao", "Censo padrao: infraestrutura + pessoas (30 min)")
    PROFUNDO = ("profundo", "Censo profundo: tudo + medicoes + depoimentos (90 min)")
    COMUNITARIO = ("comunitario", "Censo comunitario: profundo + 3 assinaturas (120 min)")
    OSINT_ONLY = ("osint_only", "So OSINT: nao foi la, cruzou satelite (0 min)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def tempo_min(self) -> int:
        return {"raso": 5, "padrao": 30, "profundo": 90,
                "comunitario": 120, "osint_only": 0}[self.id]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass
class ColetaCampo:
    """Uma coleta de campo de uma escola."""
    id: str
    cod_inep: str
    escola_nome: str
    coletor_tipo: TipoColetor
    coletor_id: str                   # identidade do cidadao fiscalizador
    timestamp_coleta: str             # ISO datetime
    latitude: float
    longitude: float
    nivel: NivelCenso
    dados: Dict[str, Any] = field(default_factory=dict)
    evidencias: List[str] = field(default_factory=list)    # hashes
    assinaturas: List[str] = field(default_factory=list)
    status_sync: StatusSincronizacao = StatusSincronizacao.PENDENTE
    observacoes: str = ""


@dataclass
class CruzamentoFontes:
    """Resultado do cruzamento INEP vs campo vs OSINT."""
    cod_inep: str
    campo: Dict[str, Any] = field(default_factory=dict)    # do cidadao
    inep: Dict[str, Any] = field(default_factory=dict)     # do INEP
    osint: Dict[str, Any] = field(default_factory=dict)    # do satelite
    discrepancias: List[Dict[str, str]] = field(default_factory=list)
    confianca_final: float = 0.0


# ============================================================================
# 3. COLETOR OFFLINE-FIRST
# ============================================================================

@dataclass
class SpecColetorApp:
    """Spec do app coletor (mobile, offline-first)."""
    nome: str = "Republica Censo"
    plataforma: List[str] = field(default_factory=lambda: ["android", "linux", "web"])
    tamanho_mb: int = 15
    offline: bool = True
    armazenamento_local_mb: int = 500  # fotos, videos, GPS
    compressao_foto: str = "webp 80%"
    compressao_video: str = "h264 480p 15fps"
    bateria_alvo_horas: int = 8
    permissões: List[str] = field(default_factory=lambda: [
        "GPS (preciso)",
        "Camera",
        "Microfone (video/depoimento)",
        "Armazenamento",
        "Internet (so pra sincronizar)",
    ])

    # Hardware minimo
    android_min_sdk: int = 24  # Android 7.0 (cobertura 95%+)
    ram_min_mb: int = 2048
    storage_min_mb: int = 1000

    # Funciona em hardware BR barato
    hardwares_testados: List[str] = field(default_factory=lambda: [
        "Moto G10 (Snapdragon 460, 4GB)",
        "Samsung A03 (Helio P35, 3GB)",
        "Redmi 9A (Helio G25, 2GB)",
        "Positivo Twist (chipset spreadtrum, 1GB)",
        "Tablet Positivo T7 (Android Go)",
    ])


def _init_checklist_censo() -> Dict[str, List[str]]:
    """Checklist do que cada nivel de censo coleta."""
    return {
        "raso": [
            "gps", "foto_fachada", "status_ativa_fechada",
            "alunos_presentes", "prof_presentes",
        ],
        "padrao": [
            "gps", "foto_fachada", "foto_interior", "status",
            "agua", "energia", "esgoto", "banheiro", "cozinha",
            "salas", "telhado", "alunos_presentes", "prof_presentes",
            "merenda", "transporte",
        ],
        "profundo": [
            "gps", "foto_fachada", "foto_interior", "video",
            "agua", "energia", "esgoto", "banheiro", "cozinha", "refeitorio",
            "internet", "computadores", "biblioteca", "quadra", "a11y",
            "salas", "telhado", "alunos_presentes", "prof_presentes",
            "funcionarios", "merenda", "cardapio", "transporte",
            "violencia", "medicao_net", "medicao_agua", "medicao_ruido",
            "documento",
        ],
        "comunitario": [
            "TUDO de profundo +",
            "depoimento (3 moradores independentes)",
            "assinatura (3+ moradores)",
            "video percurso completo",
            "medicao_luz",
        ],
        "osint_only": [
            "street_view (4 direcoes)",
            "satellite",
            "sentinel2",
            "mapbiomas",
            "osm",
            "comparacao_temporal",
        ],
    }


# ============================================================================
# 4. SISTEMA DE CENSO PROPRIO
# ============================================================================

class CensoEscolarSistema:
    """
    Sistema de Censo Escolar Proprio da Republica.

    O INEP pergunta ao diretor. Nos perguntamos ao chao.
    """

    NOME = "OpenCensoEscolar"
    VERSAO = "0.1.0-spec"

    def __init__(self) -> None:
        self.app: SpecColetorApp = SpecColetorApp()
        self.checklist: Dict[str, List[str]] = _init_checklist_censo()

    # -- coleta ------------------------------------------------------------

    def criar_coleta(
        self,
        cod_inep: str,
        escola_nome: str,
        coletor_tipo: TipoColetor,
        coletor_id: str,
        lat: float,
        lon: float,
        nivel: NivelCenso,
    ) -> ColetaCampo:
        """Cria nova coleta de campo."""
        return ColetaCampo(
            id=f"CENSO-{cod_inep}-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            cod_inep=cod_inep,
            escola_nome=escola_nome,
            coletor_tipo=coletor_tipo,
            coletor_id=coletor_id,
            timestamp_coleta=datetime.now().isoformat(),
            latitude=lat,
            longitude=lon,
            nivel=nivel,
        )

    def checklist_do_nivel(self, nivel: NivelCenso) -> List[str]:
        return self.checklist.get(nivel.id, [])

    # -- cruzamento ---------------------------------------------------------

    def cruzar_inep_vs_campo(
        self,
        coleta: ColetaCampo,
        dados_inep: Dict[str, Any],
    ) -> CruzamentoFontes:
        """Cruza dado de campo com dado do INEP."""
        cruz = CruzamentoFontes(
            cod_inep=coleta.cod_inep,
            campo=coleta.dados,
            inep=dados_inep,
        )

        # Campos para comparar
        comparacoes = [
            ("num_salas", "salas", "numero de salas"),
            ("num_alunos", "alunos_presentes", "alunos"),
            ("num_professores", "prof_presentes", "professores"),
            ("tem_agua", "agua", "agua potavel"),
            ("tem_energia", "energia", "energia"),
            ("tem_banheiro", "banheiro", "banheiro"),
            ("tem_internet", "internet", "internet"),
            ("num_computadores", "computadores", "computadores"),
            ("tem_biblioteca", "biblioteca", "biblioteca"),
        ]

        for campo_inep, campo_campo, descricao in comparacoes:
            val_inep = dados_inep.get(campo_inep)
            val_campo = coleta.dados.get(campo_campo)

            if val_inep is not None and val_campo is not None:
                if isinstance(val_inep, (int, float)) and isinstance(val_campo, (int, float)):
                    if val_inep > 0 and abs(val_inep - val_campo) / val_inep > 0.15:
                        cruz.discrepancias.append({
                            "campo": descricao,
                            "inep": str(val_inep),
                            "realidade": str(val_campo),
                            "diferenca": f"{abs(val_inep - val_campo) / val_inep * 100:.0f}%",
                        })
                elif isinstance(val_inep, bool) and isinstance(val_campo, bool):
                    if val_inep != val_campo:
                        cruz.discrepancias.append({
                            "campo": descricao,
                            "inep": "SIM" if val_inep else "NAO",
                            "realidade": "SIM" if val_campo else "NAO",
                            "diferenca": "CONFLITO",
                        })

        # Calcular confianca
        if cruz.discrepancias:
            cruz.confianca_final = max(0.0, 1.0 - len(cruz.discrepancias) * 0.1)
        else:
            cruz.confianca_final = 1.0

        return cruz

    # -- sincronizacao -------------------------------------------------------

    def espec_sincronizacao(self) -> Dict[str, Any]:
        """Spec do processo de sincronizacao offline."""
        return {
            "protocolo": "store-and-forward",
            "formato": "JSON + imagens comprimidas (webp/h264)",
            "tamanho_por_escola_mb": {
                "raso": 2,
                "padrao": 15,
                "profundo": 50,
                "comunitario": 80,
            },
            "conexao_minima": "2G (9.6 kbps) -- sync incremental, so mudancas",
            "compressao_transporte": "gzip + base64",
            "retry": "exponential backoff (1s, 2s, 4s, 8s...)",
            "confito": "ultimo-ganha + flag de conflito pra revisao manual",
            "seguranca": "hash SHA-256 + assinatura digital do coletor",
            "privacidade": "rostos borrados automaticamente (P2 autonomia corporal)",
        }

    # -- escala nacional -----------------------------------------------------

    def escala_nacional(self) -> Dict[str, Any]:
        """Estimativa de esforco para censo nacional completo."""
        total_escolas = 179534

        # Por nivel
        tempo_comunitario = 120  # min
        tempo_profundo = 90
        tempo_padrao = 30
        tempo_raso = 5

        # 10% comunitario, 30% profundo, 40% padrao, 20% raso
        n_comunitario = int(total_escolas * 0.10)
        n_profundo = int(total_escolas * 0.30)
        n_padrao = int(total_escolas * 0.40)
        n_raso = int(total_escolas * 0.20)

        horas_total = (
            (n_comunitario * tempo_comunitario) +
            (n_profundo * tempo_profundo) +
            (n_padrao * tempo_padrao) +
            (n_raso * tempo_raso)
        ) / 60

        return {
            "total_escolas": total_escolas,
            "distribuicao": {
                "comunitario (120min)": n_comunitario,
                "profundo (90min)": n_profundo,
                "padrao (30min)": n_padrao,
                "raso (5min)": n_raso,
            },
            "horas_total": int(horas_total),
            "horas_por_cidadao_1_escola_dia": int(horas_total / 1),  # se 1 cidadao fizer 1 escola/dia
            "cenario_1000_cidadaos_dias": int(total_escolas / 1000),  # se 1000 cidadaos fizerem 1/dia
            "cenario_100_cidadaos_dias": int(total_escolas / 100),
            "comparativo_inep": "INEP coleta 1 vez/ano. Censo proprio: continuo.",
            "estimativa_dados_tb": f"{(total_escolas * 0.025):.0f} TB",  # 25GB media por escola
        }

    # -- publicacao ----------------------------------------------------------

    def espec_publicacao(self) -> Dict[str, Any]:
        """Spec da publicacao dos dados do censo proprio."""
        return {
            "formato": "CSV + JSON + Parquet",
            "licenca": "CC0 (dominio publico)",
            "api": "REST + GraphQL",
            "url_base": "https://censo.republica.org.br/api/v1",
            "endpoints": [
                "GET /escola/{cod_inep} -- dados de uma escola",
                "GET /escola/{cod_inep}/historico -- todas as coletas",
                "GET /discrepancias -- todas as discrepancias vs INEP",
                "GET /fantasmas -- escolas que nao existem",
                "GET /estadouf/{uf} -- todas as escolas de um estado",
                "GET /municipio/{cod_mun} -- todas de um municipio",
                "GET /evidencia/{hash} -- foto/video/medicao",
                "POST /coleta -- enviar nova coleta (autenticado)",
            ],
            "atualizacao": "tempo real (apos sincronizacao)",
            "auditabilidade": "cada dado tem hash, timestamp, coletor, nivel confianca",
            "comparativo_inep": "INEP atualiza 1x/ano. Nosso: continuo.",
        }

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "niveis_censo": len(list(NivelCenso)),
            "tipos_dado": len(list(TipoDadoColeta)),
            "tipos_coletor": len(list(TipoColetor)),
            "status_sync": len(list(StatusSincronizacao)),
            "app_plataformas": len(self.app.plataforma),
            "checklist_itens": sum(len(v) for v in self.checklist.values()),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    sis = CensoEscolarSistema()

    print("=" * 70)
    print(f"{sis.NOME} v{sis.VERSAO} -- Censo Escolar Proprio")
    print("=" * 70)

    # --- App coletor ---
    print(f"\n[APP COLETOR]\n")
    print(f"  Nome: {sis.app.nome}")
    print(f"  Plataformas: {', '.join(sis.app.plataforma)}")
    print(f"  Offline-first: {sis.app.offline}")
    print(f"  Tamanho: {sis.app.tamanho_mb}MB")
    print(f"  Storage local: {sis.app.armazenamento_local_mb}MB")
    print(f"  Bateria alvo: {sis.app.bateria_alvo_horas}h")
    print(f"  Android min: SDK {sis.app.android_min_sdk} (7.0+)")
    print(f"  RAM min: {sis.app.ram_min_mb}MB")
    print(f"  Hardwares testados:")
    for h in sis.app.hardwares_testados:
        print(f"    - {h}")

    # --- Niveis ---
    print(f"\n\n[NIVEIS DE CENSO ({len(list(NivelCenso))})]\n")
    for n in NivelCenso:
        items = sis.checklist_do_nivel(n)
        print(f"  {n.id:<14} ({n.tempo_min:>3}min) {len(items):>2} itens")
        for item in items[:5]:
            print(f"    - {item}")
        if len(items) > 5:
            print(f"    ... +{len(items) - 5} mais")
        print()

    # --- Tipos de dado ---
    print(f"\n[TIPOS DE DADO COLETADO ({len(list(TipoDadoColeta))})]\n")
    for d in TipoDadoColeta:
        print(f"  {d.id:<20} {d.rotulo}")

    # --- Tipos de coletor ---
    print(f"\n\n[QUEM COLETA ({len(list(TipoColetor))})]\n")
    for c in TipoColetor:
        print(f"  {c.id:<12} {c.rotulo}")

    # --- Sincronizacao ---
    print(f"\n\n[SINCRONIZACAO OFFLINE]\n")
    sync = sis.espec_sincronizacao()
    for k, v in sync.items():
        if isinstance(v, dict):
            print(f"  {k}:")
            for k2, v2 in v.items():
                print(f"    {k2}: {v2}")
        else:
            print(f"  {k}: {v}")

    # --- Simulacao: coleta + cruzamento ---
    print(f"\n\n[SIMULACAO: Coleta de campo + cruzamento INEP]\n")
    coleta = sis.criar_coleta(
        "26123456", "Escola Municipal Joao Pereira",
        TipoColetor.CIDADAO_FISCALIZADOR, "cidadao_001",
        -3.7234, -40.4122, NivelCenso.COMUNITARIO,
    )
    coleta.dados = {
        "salas": 3,
        "alunos_presentes": 47,
        "prof_presentes": 2,
        "agua": False,
        "energia": True,
        "banheiro": True,
        "internet": False,
        "computadores": 0,
        "biblioteca": False,
    }
    coleta.assinaturas = ["morador_1", "morador_2", "morador_3"]
    coleta.evidencias = ["hash_foto_1", "hash_foto_2", "hash_gps"]

    dados_inep = {
        "num_salas": 6,
        "num_alunos": 180,
        "num_professores": 8,
        "tem_agua": True,
        "tem_energia": True,
        "tem_banheiro": True,
        "tem_internet": True,
        "num_computadores": 12,
        "tem_biblioteca": True,
    }

    cruz = sis.cruzar_inep_vs_campo(coleta, dados_inep)

    print(f"  Escola: {coleta.escola_nome} ({coleta.cod_inep})")
    print(f"  Coletor: {coleta.coletor_tipo.rotulo}")
    print(f"  Nivel: {coleta.nivel.id}")
    print(f"  Confianca final: {cruz.confianca_final:.0%}")
    print(f"\n  DISCREPANCIAS ({len(cruz.discrepancias)}):\n")
    for d in cruz.discrepancias:
        print(f"    [{d['campo']}] INEP={d['inep']} | CAMPO={d['realidade']} | dif={d['diferenca']}")

    # --- Escala nacional ---
    print(f"\n\n[ESCALA NACIONAL]\n")
    escala = sis.escala_nacional()
    print(f"  Total escolas: {escala['total_escolas']:,}")
    print(f"\n  Distribuicao:")
    for nivel, qtd in escala["distribuicao"].items():
        print(f"    {nivel}: {qtd:,}")
    print(f"\n  Horas totais: {escala['horas_total']:,}")
    print(f"  1000 cidadaos (1 escola/dia): {escala['cenario_1000_cidadaos_dias']} dias")
    print(f"  100 cidadaos (1 escola/dia): {escala['cenario_100_cidadaos_dias']} dias")
    print(f"  Estimativa dados: {escala['estimativa_dados_tb']}")

    # --- Publicacao ---
    print(f"\n\n[PUBLICACAO]\n")
    pub = sis.espec_publicacao()
    print(f"  Formato: {pub['formato']}")
    print(f"  Licenca: {pub['licenca']}")
    print(f"  URL: {pub['url_base']}")
    print(f"  Endpoints ({len(pub['endpoints'])}):")
    for e in pub["endpoints"]:
        print(f"    {e}")

    # --- Scorecard ---
    print(f"\n\n[SCORECARD]")
    sc = sis.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
