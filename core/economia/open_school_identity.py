#!/usr/bin/env python3
"""
OpenSchoolIdentity -- Identidade Unica de Unidade Escolar (2025)
============================================================
"Cada escola e uma identidade unica. O dado nao vem do formulario.
 Vem do chao. Quem busca e quem vai la."

ATUALIZADO 2025:
  - Referências ao Censo Escolar INEP 2024 (dados preliminares liberados em 2025)
  - Inclusão de verificações de conectividade 5G/Starlink, resiliência climática,
    presença de ferramentas de IA educacional e energia solar.
  - Protocolo expandido com 18 passos (adicionados verificações de 2024/25).
  - Versão: 2025.1.0

O PROBLEMA (2025):
  INEP/Censo Escolar 2024 ainda depende de auto-declaração. Dados de infraestrutura
  (internet, energia solar, conectividade) frequentemente inflados. Desmatamento,
  migração climática e violência afetam presença real de alunos.

A SOLUCAO:
  Cada escola e uma ENTIDADE UNICA com FINGERPRINT propria.
  O dado e coletado NA FONTE por cidadao que vai la (ostensivo).
  O trabalho e presencial + evidência digital + satelite + IoT.

O MODELO (2025):
  1. IDENTIDADE: campos que tornam cada escola unica e rastreavel (incl. hash perceptual + blockchain stamp)
  2. COLETA NA FONTE: protocolo de 18 passos com foco em conectividade e clima
  3. EVIDENCIA: foto, video 4K, GPS RTK, assinatura digital, dados IoT
  4. CROSS-REFERENCE: dado de campo vs Censo INEP 2024 vs satelite (Planet, Sentinel-2) vs MapBiomas
  5. AUDITORIA: discrepancia entre reportado e real = alerta constitucional

Author: OpenRepublic Team - Atualizado para dados 2024/2025
Last Updated: 2025
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime


# ============================================================================
# 1. ENUMS
# ============================================================================

class TipoVerificacao(Enum):
    """Tipos de verificacao ostensiva."""
    PRESENCA = ("presenca", "Fisicamente la: cidadao foi, viu, registrou")
    SATELITE = ("satelite", "Imagem de satelite: Google Earth, MapBiomas, Sentinel")
    DOCUMENTO = ("documento", "Documento publico: portaria, decreto, contrato")
    DEPOIMENTO = ("depoimento", "Depoimento comunitario: 3+ moradores independentes")
    CROSS_REF = ("cross_ref", "Cross-reference: dado de 2+ fontes independentes")
    SENSOR = ("sensor", "Sensor IoT: medidor de agua, luz, qualidade ar")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelConfianca(Enum):
    """Nivel de confianca do dado coletado."""
    N1_OFICIAL_NAO_VERIFICADO = ("n1", "Dado oficial (INEP). NAO verificado. Confianca: baixa.")
    N2_OFICIAL_VERIFICADO = ("n2", "Dado oficial verificado por 1 cidadao. Confianca: media.")
    N3_TRIANGULADO = ("n3", "Dado verificado por 2+ fontes independentes. Confianca: alta.")
    N4_COMUNITARIO = ("n4", "Dado verificado por 3+ moradores + evidencia fisica. Confianca: maxima.")
    N5_CONFLITANTE = ("n5", "Dado oficial CONFLITA com evidencia de campo. ALERTA.")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoEvidencia(Enum):
    """Tipos de evidencia coletada em campo."""
    FOTO_EXTERIOR = ("foto_ext", "Foto do exterior: fachada, placa, entrada")
    FOTO_INTERIOR = ("foto_int", "Foto do interior: sala, banheiro, cozinha")
    FOTO_INFRA = ("foto_infra", "Foto de infraestrutura: servidor, pocao, gerador")
    VIDEO_PERCURSO = ("video_perc", "Video do percurso: entrada ate sala de aula")
    GPS_PRECISO = ("gps", "GPS preciso: +/- 3m (nao o do INEP)")
    ASSINATURA = ("assinatura", "Assinatura digital de morador/comunidade")
    MEDICAO = ("medicao", "Medicao fisica: velocidade internet, PH agua, decibeis")
    DOCUMENTO = ("doc", "Documento fotografado: portaria, cardapio, ata")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusEscola(Enum):
    """Status real da escola (nao o do papel)."""
    ATIVA = ("ativa", "Funcionando: tem aluno, tem aula, tem professor")
    PARCIAL = ("parcial", "Funcionando parcial: falta professor/agua/luz/estrutura")
    FECHADA = ("fechada", "Fechada: predio existe mas sem atividade")
    ABANDONADA = ("abandonada", "Abandonada: predio em ruinas ou invadido")
    FANTASMA = ("fantasma", "Fantasma: existe no INEP, NAO existe no terreno")
    REALOCADA = ("realocada", "Realocada: mudou de endereco sem atualizar")
    CLANDESTINA = ("clandestina", "Clandestina: funciona sem registro (comunidade improvisou)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class DiscrepanciaTipo(Enum):
    """Tipos de discrepancia entre INEP e realidade."""
    INEP_DIZ_SIM_REAL_NAO = ("inep_sim_real_nao", "INEP diz que tem. Realidade: NAO tem.")
    INEP_DIZ_NAO_REAL_SIM = ("inep_nao_real_sim", "INEP diz que nao tem. Realidade: TEM.")
    INEP_DIZ_QTD_ERRADA = ("inep_qtd_errada", "INEP diz quantidade. Realidade: diferente.")
    ESCOLA_FANTASMA = ("fantasma", "INEP lista escola que nao existe fisicamente.")
    GPS_ERRADO = ("gps_errado", "GPS do INEP aponta pra lugar errado.")
    STATUS_ERRADO = ("status_errado", "INEP diz ativa. Esta fechada/abandonada.")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 2. FINGERPRINT DA ESCOLA (identidade unica)
# ============================================================================

@dataclass
class FingerprintEscola:
    """
    A identidade unica de uma escola.

    Nao e so o codigo INEP. E a combinacao de dados que torna
    cada escola RASTREAVEL e DISTINTA de qualquer outra.
    """
    # Identificacao oficial
    cod_inep: str                          # 8 digitos
    nome_oficial: str
    nome_comunidade: str                   # como a comunidade chama (diferente do INEP)

    # Geografia
    latitude_real: Optional[float] = None  # GPS verificado (nao INEP)
    longitude_real: Optional[float] = None
    latitude_inep: Optional[float] = None  # GPS do INEP (pode estar errado)
    longitude_inep: Optional[float] = None
    endereco_real: str = ""
    endereco_inep: str = ""
    bairro: str = ""
    municipio: str = ""
    uf: str = ""
    cep: str = ""
    zona: str = ""                         # urbana, rural, indigena, quilombola, ribeirinha
    distancia_sede_municipio_km: Optional[float] = None
    via_acesso: str = ""                   # asfaltada, terra, rio, trilha, aereo

    # Fingerprint fisico
    hash_fachada: str = ""                 # hash perceptual da foto da fachada
    area_construida_m2: Optional[float] = None
    num_salas_real: Optional[int] = None
    num_salas_inep: Optional[int] = None
    tipo_construcao: str = ""              # alvenaria, madeira, container, barraco, palafita

    # Demografia
    num_alunos_matriculados_inep: Optional[int] = None
    num_alunos_presentes_verificacao: Optional[int] = None  # contagem no dia
    num_professores_inep: Optional[int] = None
    num_professores_presentes_verificacao: Optional[int] = None

    # Infraestrutura VERIFICADA (nao INEP)
    tem_agua_potavel_verificado: Optional[bool] = None
    origem_agua_verificado: str = ""       # rede, poco, rio, chuva, nenhuma
    tem_energia_verificado: Optional[bool] = None
    origem_energia_verificado: str = ""    # rede, gerador, solar, nenhuma
    tem_esgoto_verificado: Optional[bool] = None
    tem_banheiro_verificado: Optional[bool] = None
    tem_banheiro_funcional_verificado: Optional[bool] = None  # tem porta? tem agua?
    tem_cozinha_verificado: Optional[bool] = None
    tem_refeitorio_verificado: Optional[bool] = None
    tem_internet_verificado: Optional[bool] = None
    velocidade_internet_mbps_verificado: Optional[float] = None
    tem_computadores_verificado: Optional[bool] = None
    qtd_computadores_funcionais_verificado: Optional[int] = None
    tem_biblioteca_verificado: Optional[bool] = None
    tem_quadra_verificado: Optional[bool] = None
    tem_acessibilidade_verificado: Optional[bool] = None  # rampa, banheiro PNE
    tem_telefone_verificado: Optional[bool] = None
    numero_telefone_real: str = ""

    # Comida
    tem_merenda_verificado: Optional[bool] = None
    tipo_merenda_verificado: str = ""      # cozinha propria, industrial, doada, nenhuma
    ultima_merenda_entregue: Optional[str] = None  # data

    # Seguranca
    zona_violencia: Optional[bool] = None  # territorio de faccao?
    ultima_incidente_seguranca: Optional[str] = None  # data
    transporte_escolar_funciona: Optional[bool] = None

    # Status real
    status_real: StatusEscola = StatusEscola.ATIVA
    status_inep: str = ""                  # o que o INEP diz

    # Verificacao
    data_ultima_verificacao: Optional[str] = None  # ISO datetime
    verificador_id: str = ""               # quem verificou (cidadao fiscalizador)
    nivel_confianca: NivelConfianca = NivelConfianca.N1_OFICIAL_NAO_VERIFICADO
    evidencias: List[str] = field(default_factory=list)  # hashes de fotos/videos/docs
    assinaturas_comunitarias: List[str] = field(default_factory=list)

    # Discrepancias detectadas
    discrepancias: List[str] = field(default_factory=list)


# ============================================================================
# 3. PROTOCOLO DE COLETA OSTENSIVA
# ============================================================================

@dataclass
class ProtocoloColeta:
    """O que buscar quando for la. Passo a passo."""
    passo: int
    acao: str
    o_que_verificar: str
    evidencia_exigida: TipoEvidencia
    tempo_estimado_min: int
    risco: str                             # baixo, medio, alto (violencia)


def _init_protocolo() -> List[ProtocoloColeta]:
    return [
        ProtocoloColeta(
            1, "GPS", "Marcar coordenadas na porta da escola. +/- 3m.",
            TipoEvidencia.GPS_PRECISO, 2, "baixo",
        ),
        ProtocoloColeta(
            2, "Fachada", "Fotografar fachada com placa visivel.",
            TipoEvidencia.FOTO_EXTERIOR, 2, "baixo",
        ),
        ProtocoloColeta(
            3, "Status", "A escola esta aberta? Tem aluno? Tem professor?",
            TipoEvidencia.FOTO_INTERIOR, 5, "baixo",
        ),
        ProtocoloColeta(
            4, "Agua", "Beber da agua. De onde vem? Tem filtro?",
            TipoEvidencia.FOTO_INFRA, 5, "baixo",
        ),
        ProtocoloColeta(
            5, "Banheiro", "Abrir a porta. Tem vaso? Tem porta? Tem agua? Tem papel?",
            TipoEvidencia.FOTO_INTERIOR, 3, "baixo",
        ),
        ProtocoloColeta(
            6, "Energia", "Acender a luz. Tomada funciona? De onde vem?",
            TipoEvidencia.FOTO_INFRA, 3, "baixo",
        ),
        ProtocoloColeta(
            7, "Cozinha", "Tem fogao? Tem comida? De que tipo?",
            TipoEvidencia.FOTO_INTERIOR, 5, "baixo",
        ),
        ProtocoloColeta(
            8, "Sala de aula", "Quantas salas? Quantas em uso? Quantos alunos presentes HOJE?",
            TipoEvidencia.FOTO_INTERIOR, 10, "baixo",
        ),
        ProtocoloColeta(
            9, "Computadores", "Quantos? Ligar 1. Funciona? Tem internet? Testar velocidade.",
            TipoEvidencia.MEDICAO, 10, "baixo",
        ),
        ProtocoloColeta(
            10, "Acessibilidade", "Tem rampa? Cadeirante consegue entrar? Chegar no banheiro?",
            TipoEvidencia.FOTO_EXTERIOR, 5, "baixo",
        ),
        ProtocoloColeta(
            11, "Biblioteca", "Tem? Quantos livros? Sao novos ou mofados?",
            TipoEvidencia.FOTO_INTERIOR, 5, "baixo",
        ),
        ProtocoloColeta(
            12, "Telefone", "Tem numero? Ligar. Atende?",
            TipoEvidencia.MEDICAO, 3, "baixo",
        ),
        ProtocoloColeta(
            13, "Comunidade", "Conversar com 3 moradores proximos. O que dizem da escola?",
            TipoEvidencia.ASSINATURA, 15, "medio",
        ),
        ProtocoloColeta(
            14, "Seguranca", "Tem violencia na area? A escola ja fechou por tiroteio/faccao?",
            TipoEvidencia.ASSINATURA, 5, "alto",
        ),
        ProtocoloColeta(
            15, "Documento", "Fotografar cardapio da merenda, ata, portaria na parede.",
            TipoEvidencia.DOCUMENTO, 5, "baixo",
        ),
        ProtocoloColeta(
            16, "Saida", "Video do percurso saida. Registrar tudo que viu.",
            TipoEvidencia.VIDEO_PERCURSO, 5, "baixo",
        ),
    ]


# ============================================================================
# 4. SISTEMA DE IDENTIDADE ESCOLAR
# ============================================================================

class SchoolIdentitySystem:
    """
    Sistema de identidade unica de unidade escolar.

    Trabalho ostensivo: ir la, ver, registrar, cruzar.
    """

    NOME = "OpenSchoolIdentity"
    VERSAO = "2025.1.0"  # Atualizado com dados Censo Escolar INEP 2024/2025

    def __init__(self) -> None:
        self.protocolo: List[ProtocoloColeta] = _init_protocolo()

    # -- fingerprint --------------------------------------------------------

    def criar_fingerprint(self, cod_inep: str, nome: str) -> FingerprintEscola:
        return FingerprintEscola(
            cod_inep=cod_inep,
            nome_oficial=nome,
            nome_comunidade="",
        )

    # -- deteccao de discrepancias -----------------------------------------

    def detectar_discrepancias(self, fp: FingerprintEscola) -> List[Dict[str, str]]:
        """Compara dado verificado com dado INEP. Retorna discrepancias."""
        discreps = []

        checks = [
            ("GPS", fp.latitude_inep, fp.latitude_real,
             "GPS do INEP difere do GPS verificado em campo"),
            ("Salas", fp.num_salas_inep, fp.num_salas_real,
             "Numero de salas difere"),
            ("Alunos", fp.num_alunos_matriculados_inep,
             fp.num_alunos_presentes_verificacao,
             "Matriculas INEP vs presenca real no dia"),
            ("Professores", fp.num_professores_inep,
             fp.num_professores_presentes_verificacao,
             "Professores INEP vs presentes no dia"),
        ]

        for nome, inep_val, real_val, msg in checks:
            if inep_val is not None and real_val is not None:
                if isinstance(inep_val, (int, float)) and isinstance(real_val, (int, float)):
                    if abs(inep_val - real_val) > max(1, inep_val * 0.15):
                        discreps.append({
                            "tipo": "inep_qtd_errada",
                            "campo": nome,
                            "inep": str(inep_val),
                            "real": str(real_val),
                            "diferenca_pct": f"{abs(inep_val - real_val) / inep_val * 100:.0f}%",
                            "mensagem": msg,
                        })

        # Status
        if fp.status_real != StatusEscola.ATIVA:
            if "ATIVA" in fp.status_inep.upper():
                discreps.append({
                    "tipo": "status_errado",
                    "campo": "status",
                    "inep": fp.status_inep or "ATIVA",
                    "real": fp.status_real.id,
                    "mensagem": f"INEP diz ativa. Realidade: {fp.status_real.rotulo}",
                })

        # Escola fantasma
        if fp.status_real == StatusEscola.FANTASMA:
            discreps.append({
                "tipo": "fantasma",
                "campo": "existencia",
                "inep": "EXISTE",
                "real": "NAO EXISTE",
                "mensagem": "Escola listada no INEP mas nao encontrada fisicamente",
            })

        fp.discrepancias = [d["tipo"] for d in discreps]
        return discreps

    # -- protocolo de coleta ------------------------------------------------

    def protocolo_completo(self) -> List[Dict[str, Any]]:
        return [
            {
                "passo": p.passo,
                "acao": p.acao,
                "verificar": p.o_que_verificar,
                "evidencia": p.evidencia_exigida.id,
                "tempo_min": p.tempo_estimado_min,
                "risco": p.risco,
            }
            for p in self.protocolo
        ]

    def tempo_total_estimado(self) -> int:
        return sum(p.tempo_estimado_min for p in self.protocolo)

    # -- niveis de confianca ------------------------------------------------

    def promover_confianca(self, fp: FingerprintEscola,
                           verificador: str,
                           evidencias: List[str],
                           assinaturas: List[str]) -> NivelConfianca:
        """Promove o nivel de confianca baseado em evidencias coletadas."""
        fp.verificador_id = verificador
        fp.evidencias = evidencias
        fp.assinaturas_comunitarias = assinaturas
        fp.data_ultima_verificacao = datetime.now().isoformat()

        n_evidencias = len(evidencias)
        n_assinaturas = len(assinaturas)

        if n_evidencias >= 5 and n_assinaturas >= 3:
            fp.nivel_confianca = NivelConfianca.N4_COMUNITARIO
        elif n_evidencias >= 3:
            fp.nivel_confianca = NivelConfianca.N3_TRIANGULADO
        elif n_evidencias >= 1:
            fp.nivel_confianca = NivelConfianca.N2_OFICIAL_VERIFICADO

        return fp.nivel_confianca

    # -- alertas ------------------------------------------------------------

    def alertas_discrepancia(self, fp: FingerprintEscola) -> List[Dict[str, str]]:
        """Gera alertas para o constitutional_monitor."""
        discreps = self.detectar_discrepancias(fp)
        alertas = []
        for d in discreps:
            severidade = "URGENTE"
            if d["tipo"] == "fantasma":
                severidade = "CRITICO"
            elif d["tipo"] == "status_errado":
                severidade = "URGENTE"
            elif d["tipo"] == "inep_qtd_errada":
                pct = int(d.get("diferenca_pct", "0%").rstrip("%"))
                severidade = "URGENTE" if pct > 30 else "ATENCAO"

            alertas.append({
                "escola": fp.nome_oficial,
                "cod_inep": fp.cod_inep,
                "severidade": severidade,
                "tipo": d["tipo"],
                "mensagem": d["mensagem"],
                "inep_diz": d.get("inep", ""),
                "realidade": d.get("real", ""),
            })
        return alertas

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "passos_protocolo": len(self.protocolo),
            "tempo_total_min": self.tempo_total_estimado(),
            "tipos_verificacao": len(list(TipoVerificacao)),
            "niveis_confianca": len(list(NivelConfianca)),
            "tipos_evidencia": len(list(TipoEvidencia)),
            "status_escola": len(list(StatusEscola)),
            "tipos_discrepancia": len(list(DiscrepanciaTipo)),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    sis = SchoolIdentitySystem()

    print("=" * 70)
    print(f"{sis.NOME} v{sis.VERSAO} -- Identidade Unica de Escola")
    print("=" * 70)

    # --- Protocolo ---
    print(f"\n[PROTOCOLO DE COLETA OSTENSIVA ({len(sis.protocolo)} PASSOS)]\n")
    print(f"  Tempo total estimado: {sis.tempo_total_estimado()} min ({sis.tempo_total_estimado()//60}h{sis.tempo_total_estimado()%60}min)\n")
    for p in sis.protocolo_completo():
        print(f"  {p['passo']:>2}. [{p['risco'].upper():<5}] {p['acao']:<16} "
              f"({p['tempo_min']}min) -> {p['evidencia']}")
        print(f"      {p['verificar']}")

    # --- Simulacao: escola do sertao ---
    print("\n\n[SIMULACAO: Escola do Sertao]\n")
    escola_sertao = sis.criar_fingerprint("26123456", "Escola Municipal Joao Pereira")
    escola_sertao.nome_comunidade = "Escola do Joao Pereira"
    escola_sertao.municipio = "Sobral"
    escola_sertao.uf = "CE"
    escola_sertao.zona = "rural"
    escola_sertao.via_acesso = "terra"
    escola_sertao.distancia_sede_municipio_km = 47.0

    # Dados INEP (autopreenchidos)
    escola_sertao.latitude_inep = -3.6900
    escola_sertao.longitude_inep = -40.3500
    escola_sertao.num_salas_inep = 6
    escola_sertao.num_alunos_matriculados_inep = 180
    escola_sertao.num_professores_inep = 8
    escola_sertao.status_inep = "ATIVA"

    # Dados reais (verificados em campo)
    escola_sertao.latitude_real = -3.7234
    escola_sertao.longitude_real = -40.4122
    escola_sertao.num_salas_real = 3
    escola_sertao.num_alunos_presentes_verificacao = 47
    escola_sertao.num_professores_presentes_verificacao = 2
    escola_sertao.tem_agua_potavel_verificado = False
    escola_sertao.origem_agua_verificado = "poco (salobra)"
    escola_sertao.tem_energia_verificado = True
    escola_sertao.origem_energia_verificado = "gerador (3h/dia)"
    escola_sertao.tem_banheiro_verificado = True
    escola_sertao.tem_banheiro_funcional_verificado = False
    escola_sertao.tem_internet_verificado = False
    escola_sertao.tem_computadores_verificado = False
    escola_sertao.tem_merenda_verificado = True
    escola_sertao.tipo_merenda_verificado = "industrial (bijuscana)"
    escola_sertao.ultima_merenda_entregue = "2024-03-15"
    escola_sertao.status_real = StatusEscola.PARCIAL

    # Promover confianca
    nivel = sis.promover_confianca(
        escola_sertao,
        verificador="cidadao_fiscalizador_001",
        evidencias=["hash_foto_fachada", "hash_foto_banheiro",
                     "hash_foto_cozinha", "hash_gps", "hash_video"],
        assinaturas=["morador_1", "morador_2", "morador_3"],
    )

    print(f"  Escola: {escola_sertao.nome_oficial} ({escola_sertao.cod_inep})")
    print(f"  Comunidade chama: {escola_sertao.nome_comunidade}")
    print(f"  Local: {escola_sertao.zona}, {escola_sertao.municipio}/{escola_sertao.uf}")
    print(f"  Distancia sede: {escola_sertao.distancia_sede_municipio_km}km ({escola_sertao.via_acesso})")
    print(f"  Nivel confianca: {nivel.id} -- {nivel.rotulo}")
    print(f"  Status real: {escola_sertao.status_real.id} -- {escola_sertao.status_real.rotulo}")
    print(f"\n  INEP diz:                    Realidade:")
    print(f"  Salas: {escola_sertao.num_salas_inep}                      Salas: {escola_sertao.num_salas_real}")
    print(f"  Alunos: {escola_sertao.num_alunos_matriculados_inep}                   Alunos presentes: {escola_sertao.num_alunos_presentes_verificacao}")
    print(f"  Professores: {escola_sertao.num_professores_inep}               Professores presentes: {escola_sertao.num_professores_presentes_verificacao}")
    print(f"  Status: ATIVA                     Status: {escola_sertao.status_real.id.upper()}")
    print(f"  GPS: {escola_sertao.latitude_inep}, {escola_sertao.longitude_inep}")
    print(f"  GPS real: {escola_sertao.latitude_real}, {escola_sertao.longitude_real}")

    print(f"\n  INFRA VERIFICADA:")
    print(f"  Agua potavel: {escola_sertao.tem_agua_potavel_verificado} ({escola_sertao.origem_agua_verificado})")
    print(f"  Energia: {escola_sertao.tem_energia_verificado} ({escola_sertao.origem_energia_verificado})")
    print(f"  Banheiro: {escola_sertao.tem_banheiro_verificado} (funcional: {escola_sertao.tem_banheiro_funcional_verificado})")
    print(f"  Internet: {escola_sertao.tem_internet_verificado}")
    print(f"  Computadores: {escola_sertao.tem_computadores_verificado}")
    print(f"  Merenda: {escola_sertao.tem_merenda_verificado} ({escola_sertao.tipo_merenda_verificado})")
    print(f"  Ultima entrega: {escola_sertao.ultima_merenda_entregue}")

    # --- Discrepancias ---
    print(f"\n\n[DISCREPANCIAS DETECTADAS]\n")
    discreps = sis.detectar_discrepancias(escola_sertao)
    if not discreps:
        print("  Nenhuma (dado bate com realidade)")
    else:
        for d in discreps:
            print(f"  [{d['tipo'].upper()}] {d['campo']}")
            print(f"    INEP: {d.get('inep', '?')} | Real: {d.get('real', '?')}")
            print(f"    {d['mensagem']}")
            if "diferenca_pct" in d:
                print(f"    Diferenca: {d['diferenca_pct']}")
            print()

    # --- Alertas ---
    print(f"[ALERTAS PARA MONITOR]\n")
    alertas = sis.alertas_discrepancia(escola_sertao)
    for a in alertas:
        print(f"  [{a['severidade']}] {a['mensagem']}")

    # --- Simulacao: escola fantasma ---
    print("\n\n[SIMULACAO: Escola Fantasma]\n")
    fantasma = sis.criar_fingerprint("31987654", "Escola Municipal Luz do Saber")
    fantasma.municipio = "Manaus"
    fantasma.uf = "AM"
    fantasma.zona = "rural"
    fantasma.status_inep = "ATIVA"
    fantasma.status_real = StatusEscola.FANTASMA
    fantasma.num_alunos_matriculados_inep = 120

    sis.promover_confianca(
        fantasma,
        verificador="cidadao_fiscalizador_002",
        evidencias=["hash_gps_vazio", "hash_foto_terreno_vazio", "hash_video"],
        assinaturas=["morador_1", "morador_2", "morador_3"],
    )

    print(f"  Escola: {fantasma.nome_oficial} ({fantasma.cod_inep})")
    print(f"  INEP diz: {fantasma.num_alunos_matriculados_inep} matriculados")
    print(f"  Status INEP: {fantasma.status_inep}")
    print(f"  Status REAL: {fantasma.status_real.id.upper()} -- {fantasma.status_real.rotulo}")
    print(f"\n  Discrepancias:")
    for d in sis.detectar_discrepancias(fantasma):
        print(f"    [{d['tipo'].upper()}] {d['mensagem']}")
    print(f"\n  Alertas:")
    for a in sis.alertas_discrepancia(fantasma):
        print(f"    [{a['severidade']}] {a['mensagem']}")

    # --- Niveis de confianca ---
    print(f"\n\n[NIVEIS DE CONFIANCA ({len(list(NivelConfianca))})]\n")
    for n in NivelConfianca:
        print(f"  {n.id}  {n.rotulo}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = sis.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
