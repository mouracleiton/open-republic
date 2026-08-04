#!/usr/bin/env python3
"""
OpenDenuncia -- Canal de Denuncias da Republica
=================================================
"P13 diz: cidadao vigia Estado. P2 diz: corpo e teu.
 Juntando: denuncia protegida, denunciante anonimo."

O PROBLEMA:
  Denuncia hoje: ouvidoria governamental (ninguem confia),
  disque-denuncia (numero rastreavel), delegacia (medo),
  jornalista (depende de editor), ONG (capacidade limitada).

  Resultado: cidadao cala. Predador segue. 4.570.000 invisiveis.

A SOLUCAO:
  Canal proprio. Anonimo por design. Offline-capable.
  Cadeia hash (tamper-proof). Multi-canal. Verificavel.

PRINCIPIOS:
  P2  -- denunciante e anonimo. Identidade protegida.
  P5  -- denuncia verificada e publica. Log auditavel.
  P9  -- nao polariza. Fato, nao opiniao.
  P13 -- ferramenta de contravigilancia.
  P14 -- denunciante controla o proprio dado.

SEGURANCA (prioridade maxima):
  - Nenhum IP logado
  - Nenhum telefone logado
  - Tor/onion por padrao
  - Metadados EXIF removidos de fotos automaticamente
  - Rostos borrados automaticamente (P2)
  - Criptografia ponta-a-ponta
  - Cadeia hash (cada denuncia linka com a anterior, tipo blockchain)
  - Sem servidor central (distribuido, torrent-style sync)

CANAIS DE ENTRADA:
  1. App mobile (offline-first, Tor embedded)
  2. Web (.onion + clearnet)
  3. SMS (numero descartavel, sem retorno)
  4. Voz (ligaçao, transcreve, deleta voz)
  5. Correio (caixa postal fisica, escaneado)
  6. QR code (cola na rua, foto envia)
  7. Mesh radio (LoRa, sem internet)
  8. Papel (boletim de ocorrencia cidadao impresso)

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import hashlib


# ============================================================================
# 1. ENUMS
# ============================================================================

class TipoDenuncia(Enum):
    """Tipos de denuncia que o sistema aceita."""
    CORRUPCAO = ("corrupcao", "Corrupcao: desvio, propina, lavagem")
    TRABALHO_ESCRAVO = ("escravo", "Trabalho escravo contemporaneo")
    TRABALHO_INFANTIL = ("infantil", "Trabalho infantil")
    VIOLENCIA_DOMESTICA = ("domestica", "Violencia domestica")
    VIOLENCIA_POLICIAL = ("policial", "Violencia policial / abuso de autoridade")
    FACCAO = ("faccao", "Faccao: territorio, extorsao, trafico")
    DESVIO_RECURSO = ("desvio", "Desvio de recurso publico (merenda, obra, saude)")
    FRAUDE_ELEITORAL = ("fraude", "Fraude eleitoral / compra de voto")
    DESMATAMENTO = ("desmatamento", "Desmatamento ilegal / garimpo")
    AGROTOXICO = ("agrotoxico", "Contaminacao por agrotoxico / rio")
    NEGLIGENCIA_SAUDE = ("saude", "Negligencia em saude (SUS, posto, hospital)")
    NEGLIGENCIA_EDUCACAO = ("educacao", "Negligencia em educacao (escola sem agua/luz/prof)")
    ESPECULACAO = ("especulacao", "Especulacao imobiliaria / despejo ilegal")
    HATE_CRIME = ("hate", "Crime de odio (raca, genero, religiao, LGBT)")
    PEDOFILIA = ("pedofilia", "Pedofilia / exploracao de crianca")
    LAVAGEM = ("lavagem", "Lavagem de dinheiro")
    CONTRABANDO = ("contrabando", "Contrabando / pirataria")
    ENVENENAMENTO = ("veneno", "Adulteracao de agua/alimento/medicamento")
    OUTRO = ("outro", "Outro (especificar)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class CanalEntrada(Enum):
    """Canais por onde a denuncia entra no sistema."""
    APP_TOR = ("app_tor", "App mobile com Tor embedded (anonimo)")
    WEB_ONION = ("onion", "Site .onion (Tor, anonimo)")
    WEB_CLEAR = ("clear", "Site clearnet (menos anonimo)")
    SMS = ("sms", "SMS para numero descartavel (sem retorno)")
    VOZ = ("voz", "Ligacao telefonia (transcreve, deleta voz)")
    CORREIO = ("correio", "Caixa postal fisica (escaneado, OCR)")
    QR_RUA = ("qr", "QR code colado na rua (foto envia)")
    MESH_LORA = ("lora", "Mesh radio LoRa (sem internet)")
    PAPEL = ("papel", "Boletim impresso depositado em ponto")
    P2P_APP = ("p2p", "App P2P (Briar, sem servidor)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def anonimato_nivel(self) -> int:
        """1=baixo, 5=maximo."""
        return {"app_tor": 5, "onion": 5, "clear": 2,
                "sms": 3, "voz": 1, "correio": 4,
                "qr": 4, "lora": 5, "papel": 5, "p2p": 5}[self.id]


class SeveridadeDenuncia(Enum):
    """Severidade da denuncia (define prioridade de verificacao)."""
    S1_BAIXA = ("s1", "Baixa: irregularidade administrativa")
    S2_MEDIA = ("s2", "Media: violacao de direito individual")
    S3_ALTA = ("s3", "Alta: crime continuado, multiplos atingidos")
    S4_CRITICA = ("s4", "Critica: risco de vida, violencia em andamento")
    S5_EMERGENCIA = ("s5", "Emergencia: vidas em risco AGORA")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusDenuncia(Enum):
    """Ciclo de vida da denuncia."""
    RECEBIDA = ("recebida", "Recebida. Anonima. Sem rastro.")
    TRIAGEM = ("triagem", "Em triagem: categoria, severidade, duplicata")
    VERIFICACAO = ("verificacao", "Em verificacao: cidadao fiscalizador ou OSINT")
    TRIANGULADA = ("triangulada", "Verificada por 2+ fontes independentes")
    PUBLICADA = ("publicada", "Publicada com evidencia. Log permanente.")
    ENCAMINHADA = ("encaminhada", "Encaminhada para autoridade (MP, PF, ONU)")
    ARQUIVADA = ("arquivada", "Arquivada: nao verificavel ou falsa")
    RETIRADA = ("retirada", "Retirada pelo denunciante (P14: dado e teu)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoEvidencia(Enum):
    """Tipos de evidencia anexados a denuncia."""
    FOTO = ("foto", "Foto (EXIF removido, rostos borrados)")
    VIDEO = ("video", "Video (metadata removido, rostos borrados)")
    AUDIO = ("audio", "Audio (metadata removido)")
    DOCUMENTO = ("documento", "Documento fotografado (nota, contrato, portaria)")
    GPS = ("gps", "Localizacao aproximada (raio, nao ponto exato)")
    SCREENSHOT = ("screenshot", "Screenshot (metadata removido)")
    TESTEMUNHO = ("testemunho", "Testemunho de 3+ pessoas independentes")
    MEDICAO = ("medicao", "Medicao fisica (PH, decibel, lux)")

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
class Denuncia:
    """Uma denuncia anonima."""
    hash_id: str                    # hash SHA-256 (anonimo, sem ID sequencial)
    timestamp: str                  # ISO (data sem hora exata = +/- 1h)
    tipo: TipoDenuncia
    severidade: SeveridadeDenuncia
    canal: CanalEntrada
    descricao: str                  # texto livre
    localizacao_aprox: Optional[str] = None  # "bairro X, cidade Y" (nao GPS exato)
    localizacao_raio_m: Optional[int] = None  # raio de incerteza
    evidencias: List[str] = field(default_factory=list)  # hashes de arquivos
    cadeia_hash_anterior: str = ""  # link para denuncia anterior (blockchain)
    hash_proprio: str = ""          # hash desta denuncia
    status: StatusDenuncia = StatusDenuncia.RECEBIDA
    verificacoes: List[Dict[str, Any]] = field(default_factory=list)
    nivel_confianca: float = 0.0
    denuncias_relacionadas: List[str] = field(default_factory=list)
    encaminhamento: Optional[str] = None  # "MP", "PF", "ONU", "publico"


@dataclass
class ProtecaoAnonimato:
    """Medidas de protecao aplicadas automaticamente."""
    exif_removido: bool = True
    rostos_borrados: bool = True
    gps_preciso_removido: bool = True     # so guarda raio, nao ponto
    ip_logado: bool = False               # NUNCA
    telefone_logado: bool = False         # NUNCA
    timestamp_arredondado: bool = True    # +/- 1h
    voz_deletada: bool = True             # transcreve e deleta
    metadata_arquivo_removido: bool = True
    tor_obrigatorio: bool = True          # web/app


# ============================================================================
# 3. SEGURANCA: cadeia hash (blockchain simples)
# ============================================================================

def _gerar_hash(denuncia_data: str, anterior: str = "") -> str:
    """Gera hash SHA-256 linkando com a denuncia anterior."""
    conteudo = f"{anterior}{denuncia_data}"
    return hashlib.sha256(conteudo.encode()).hexdigest()


# ============================================================================
# 4. SISTEMA DE DENUNCIAS
# ============================================================================

class DenunciaSistema:
    """
    Canal de denuncias da Republica.

    Anonimo por design. Tamper-proof por cadeia hash.
    Multi-canal. Verificavel. Publico quando verificado.
    """

    NOME = "OpenDenuncia"
    VERSAO = "0.1.0-spec"

    def __init__(self) -> None:
        self.ultima_hash: str = "0" * 64  # genesis
        self.protecoes: ProtecaoAnonimato = ProtecaoAnonimato()

    # -- criar denuncia ----------------------------------------------------

    def criar_denuncia(
        self,
        tipo: TipoDenuncia,
        severidade: SeveridadeDenuncia,
        canal: CanalEntrada,
        descricao: str,
        localizacao_aprox: Optional[str] = None,
        localizacao_raio_m: Optional[int] = None,
        evidencias: Optional[List[str]] = None,
    ) -> Denuncia:
        """Cria nova denuncia anonima."""
        timestamp = datetime.now().replace(minute=0, second=0, microsecond=0).isoformat()

        # Hash ID: SHA-256 do conteudo + timestamp arredondado
        conteudo = f"{tipo.id}{severidade.id}{canal.id}{timestamp}{descricao}"
        hash_id = hashlib.sha256(conteudo.encode()).hexdigest()[:16]

        # Cadeia: linka com anterior
        hash_proprio = _gerar_hash(conteudo, self.ultima_hash)

        den = Denuncia(
            hash_id=hash_id,
            timestamp=timestamp,
            tipo=tipo,
            severidade=severidade,
            canal=canal,
            descricao=descricao,
            localizacao_aprox=localizacao_aprox,
            localizacao_raio_m=localizacao_raio_m,
            evidencias=evidencias or [],
            cadeia_hash_anterior=self.ultima_hash,
            hash_proprio=hash_proprio,
        )

        self.ultima_hash = hash_proprio
        return den

    # -- protecoes ---------------------------------------------------------

    def checklist_protecao(self) -> List[Dict[str, Any]]:
        """Checklist de protecoes aplicadas a cada denuncia."""
        p = self.protecoes
        return [
            {"item": "EXIF removido de fotos", "ativo": p.exif_removido,
             "principio": "P2 (nao rastreia)"},
            {"item": "Rostos borrados automaticamente", "ativo": p.rostos_borrados,
             "principio": "P2 (protege vitima/testemunha)"},
            {"item": "GPS preciso removido (so raio)", "ativo": p.gps_preciso_removido,
             "principio": "P2 (nao rastreia local exato)"},
            {"item": "IP NUNCA logado", "ativo": not p.ip_logado,
             "principio": "P2/P13 (anonimato)"},
            {"item": "Telefone NUNCA logado", "ativo": not p.telefone_logado,
             "principio": "P2/P13"},
            {"item": "Timestamp arredondado (+/-1h)", "ativo": p.timestamp_arredondado,
             "principio": "P2 (nao correlaciona horario)"},
            {"item": "Voz deletada apos transcricao", "ativo": p.voz_deletada,
             "principio": "P2 (biometria vocal destruida)"},
            {"item": "Metadata de arquivo removido", "ativo": p.metadata_arquivo_removido,
             "principio": "P2/P14"},
            {"item": "Tor obrigatorio (web/app)", "ativo": p.tor_obrigatorio,
             "principio": "P2/P13"},
        ]

    # -- canais ------------------------------------------------------------

    def canais_disponiveis(self) -> List[Dict[str, Any]]:
        return [
            {"id": c.id, "rotulo": c.rotulo, "anonimato": c.anonimato_nivel}
            for c in CanalEntrada
        ]

    # -- verificacao --------------------------------------------------------

    def verificar_denuncia(
        self,
        den: Denuncia,
        verificador: str,
        fonte: str,
        conclusao: str,
        confianca: float,
    ) -> Denuncia:
        """Adiciona verificacao a denuncia."""
        den.verificacoes.append({
            "verificador": verificador,
            "fonte": fonte,
            "conclusao": conclusao,
            "confianca": confianca,
            "timestamp": datetime.now().isoformat(),
        })

        # Atualizar nivel de confianca agregado
        if den.verificacoes:
            den.nivel_confianca = sum(
                v["confianca"] for v in den.verificacoes  # type: ignore
            ) / len(den.verificacoes)

        # Atualizar status
        if len(den.verificacoes) >= 2 and den.nivel_confianca >= 0.7:
            den.status = StatusDenuncia.TRIANGULADA
        elif len(den.verificacoes) >= 1:
            den.status = StatusDenuncia.VERIFICACAO

        return den

    # -- publicar -----------------------------------------------------------

    def publicar(self, den: Denuncia) -> Denuncia:
        """Publica denuncia verificada (P5 transparencia)."""
        if den.nivel_confianca >= 0.7 or den.severidade == SeveridadeDenuncia.S5_EMERGENCIA:
            den.status = StatusDenuncia.PUBLICADA
        return den

    # -- cadeia hash --------------------------------------------------------

    def validar_cadeia(self, denuncias: List[Denuncia]) -> bool:
        """Valida que a cadeia de hash nao foi adulterada."""
        for i, d in enumerate(denuncias):
            if i == 0:
                if d.cadeia_hash_anterior != "0" * 64:
                    return False
            else:
                if d.cadeia_hash_anterior != denuncias[i - 1].hash_proprio:
                    return False
            # Recalcular hash
            conteudo = f"{d.tipo.id}{d.severidade.id}{d.canal.id}{d.timestamp}{d.descricao}"
            esperado = _gerar_hash(conteudo, d.cadeia_hash_anterior)
            if d.hash_proprio != esperado:
                return False
        return True

    # -- roteamento ---------------------------------------------------------

    def rotear_encaminhamento(self, den: Denuncia) -> str:
        """Define para onde encaminhar baseado no tipo."""
        rota = {
            TipoDenuncia.CORRUPCAO: "MP (Ministerio Publico)",
            TipoDenuncia.TRABALHO_ESCRAVO: "MPT + Policia Federal",
            TipoDenuncia.TRABALHO_INFANTIL: "MP + Conselho Tutelar",
            TipoDenuncia.VIOLENCIA_DOMESTICA: "MP + Rede de Protecao (NAO delegacia sem Lei Maria da Penha)",
            TipoDenuncia.VIOLENCIA_POLICIAL: "MP + Ouvidoria da PM (publicar PRIMEIRO)",
            TipoDenuncia.FACCAO: "publicar primeiro, MP depois",
            TipoDenuncia.DESVIO_RECURSO: "MP + TCM",
            TipoDenuncia.FRAUDE_ELEITORAL: "TSE + MP Eleitoral",
            TipoDenuncia.DESMATAMENTO: "IBAMA + MP + publicar",
            TipoDenuncia.AGROTOXICO: "ANVISA + IBAMA + MP",
            TipoDenuncia.NEGLIGENCIA_SAUDE: "MP + publicar",
            TipoDenuncia.NEGLIGENCIA_EDUCACAO: "MP + publicar (cruzar com censo escolar)",
            TipoDenuncia.PEDOFILIA: "Policia Federal + Interpol",
            TipoDenuncia.HATE_CRIME: "MP + publicar",
            TipoDenuncia.LAVAGEM: "COAF + MP + PF",
            TipoDenuncia.ENVENENAMENTO: "ANVISA + Policia Civil + publicar (URGENTE)",
        }
        return rota.get(den.tipo, "MP + publicar")

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "tipos_denuncia": len(list(TipoDenuncia)),
            "canais_entrada": len(list(CanalEntrada)),
            "severidades": len(list(SeveridadeDenuncia)),
            "status_ciclo": len(list(StatusDenuncia)),
            "tipos_evidencia": len(list(TipoEvidencia)),
            "protecoes_ativas": sum(1 for p in self.checklist_protecao() if p["ativo"]),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    sis = DenunciaSistema()

    print("=" * 70)
    print(f"{sis.NOME} v{sis.VERSAO} -- Canal de Denuncias")
    print("=" * 70)

    # --- Protecoes ---
    print(f"\n[PROTECOES DE ANONIMATO ({len(sis.checklist_protecao())})]\n")
    for p in sis.checklist_protecao():
        status = "ATIVO" if p["ativo"] else "INATIVO"
        print(f"  [{status}] {p['item']}")
        print(f"         {p['principio']}")

    # --- Canais ---
    print(f"\n\n[CANAIS DE ENTRADA ({len(list(CanalEntrada))})]\n")
    for c in sis.canais_disponiveis():
        barra = "*" * c["anonimato"] + "." * (5 - c["anonimato"])
        print(f"  {c['id']:<12} [{barra}] {c['rotulo']}")

    # --- Tipos ---
    print(f"\n\n[TIPOS DE DENUNCIA ({len(list(TipoDenuncia))})]\n")
    for t in TipoDenuncia:
        print(f"  {t.id:<16} {t.rotulo}")

    # --- Simulacao: denuncia de corrupcao ---
    print("\n\n[SIMULACAO: Denuncia de Desvio de Merenda]\n")
    d1 = sis.criar_denuncia(
        tipo=TipoDenuncia.DESVIO_RECURSO,
        severidade=SeveridadeDenuncia.S3_ALTA,
        canal=CanalEntrada.APP_TOR,
        descricao=(
            "Escola Municipal X recebe R$ 50.000/mes de merenda "
            "mas alunos comem bolacha 3x/semana. Diretor compra "
            "de fornecedor que e cunhado dele. NF fiscalizada "
            "mas produto nao chega."
        ),
        localizacao_aprox="Zona Norte, Sao Paulo/SP",
        localizacao_raio_m=2000,
        evidencias=["hash_foto_nota", "hash_foto_cozinha_vazia", "hash_foto_cardapio"],
    )

    print(f"  Hash ID: {d1.hash_id}")
    print(f"  Tipo: {d1.tipo.rotulo}")
    print(f"  Severidade: {d1.severidade.rotulo}")
    print(f"  Canal: {d1.canal.rotulo} (anonimato {d1.canal.anonimato_nivel}/5)")
    print(f"  Local: {d1.localizacao_aprox} (+/-{d1.localizacao_raio_m}m)")
    print(f"  Status: {d1.status.id}")
    print(f"  Cadeia anterior: {d1.cadeia_hash_anterior[:16]}...")
    print(f"  Hash proprio: {d1.hash_proprio[:16]}...")

    # Verificacao 1: cidadao fiscalizador
    d1 = sis.verificar_denuncia(
        d1, verificador="cidadao_001",
        fonte="campo: visitou escola, fotografou cozinha vazia",
        conclusao="CONFIRMA: cozinha sem estoque, cozinha nao funciona",
        confianca=0.85,
    )
    print(f"\n  Apos verificacao 1: status={d1.status.id} conf={d1.nivel_confianca:.0%}")

    # Verificacao 2: OSINT
    d1 = sis.verificar_denuncia(
        d1, verificador="osint_bot",
        fonte="osint: street view mostra entregas em endereco diferente",
        conclusao="CONFIRMA: fornecedor entrega em galpao privado, nao na escola",
        confianca=0.75,
    )
    print(f"  Apos verificacao 2: status={d1.status.id} conf={d1.nivel_confianca:.0%}")

    # Publicar
    d1 = sis.publicar(d1)
    print(f"  Apos publicar: status={d1.status.id}")

    # Encaminhar
    rota = sis.rotear_encaminhamento(d1)
    print(f"  Encaminhamento: {rota}")

    # --- Simulacao: violencia policial (emergencia) ---
    print("\n\n[SIMULACAO: Violencia Policial -- Emergencia]\n")
    d2 = sis.criar_denuncia(
        tipo=TipoDenuncia.VIOLENCIA_POLICIAL,
        severidade=SeveridadeDenuncia.S5_EMERGENCIA,
        canal=CanalEntrada.QR_RUA,
        descricao="PM em operacao na favela, tiroteio, criancas na escola. Agora.",
        localizacao_aprox="Complexo, Rio de Janeiro/RJ",
        localizacao_raio_m=500,
        evidencias=["hash_video_ao_vivo"],
    )

    print(f"  Hash ID: {d2.hash_id}")
    print(f"  Severidade: {d2.severidade.rotulo}")
    print(f"  Canal: {d2.canal.rotulo}")
    print(f"  Status: {d2.status.id}")

    # Emergencia publica imediatamente
    d2 = sis.publicar(d2)
    print(f"  Publicada imediatamente (emergencia): {d2.status.id}")
    print(f"  Encaminhamento: {sis.rotear_encaminhamento(d2)}")

    # --- Cadeia hash ---
    print("\n\n[CADEIA HASH (TAMPER-PROOF)]\n")
    print(f"  Denuncia 1: ...{d1.hash_proprio[-16:]}")
    print(f"    anterior: {d1.cadeia_hash_anterior[:16]}...")
    print(f"  Denuncia 2: ...{d2.hash_proprio[-16:]}")
    print(f"    anterior: {d2.cadeia_hash_anterior[:16]}...")
    print(f"\n  Cadeia valida: {sis.validar_cadeia([d1, d2])}")

    # --- Severidades ---
    print(f"\n\n[NIVEIS DE SEVERIDADE ({len(list(SeveridadeDenuncia))})]\n")
    for s in SeveridadeDenuncia:
        print(f"  {s.id}  {s.rotulo}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = sis.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
