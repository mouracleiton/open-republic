#!/usr/bin/env python3
"""
OpenAgrarianRevolution -- A Terra e de Quem a Cuida
=====================================================
A Revolucao Agraria da Republica Aberta vai alem da "reforma agraria" classica.
Nao redistribui propriedade. ABOLI a propriedade da terra como mercadoria.
A terra nao se compra, nao se vende, nao se herda, nao se acumula.
A terra se CUIDA. Quem cuida, colhe o fruto. Quem abandona, devolve.

ALINHAMENTO CONSTITUCIONAL:
- P1 (Anti-elitismo): Latifundio = mecanismo original de elite. Concentrar
  terra = concentrar vida. A Republica extingue a raiz da desigualdade rural.
- P2 (Autonomia corporal): Quem trabalha a terra tem direito ao fruto do
  trabalho. Ninguem morre de fome cercando terra que nao cultiva.
- P3 (Trabalho igual): Crislto vem de IMPACTO (alimentar gente), nao de
  aluguel de terra. Latifundio improdutivo = roubo sistêmico.
- P4 (Democracia radical): Assembleia local decide o uso da terra. Nao
  existe "dono". Existe GUARDIAO com mandato revogavel.

OS 5 PILARES DA REVOLUCAO AGRARIA:
1. ABOLICAO da propriedade privada da terra (ninguem "possui" hectares)
2. GUARDIAO em vez de dono (quem cultiva cuida, mandato revogavel)
3. FUNCAO SOCIAL obrigatoria (terra ociosa = devolvida)
4. COOPERATIVISMO (nenhuma familia sozinha; mutirao como padrao)
5. AGROLOGIA (agricultura que regenera o solo, nao que o exaure)

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime


# ============================================================================
# 1. ENUMS (modulo-level, nunca aninhados)
# ============================================================================

class TipoTenencia(Enum):
    """Como a terra e cuidada na Republica (depois da abolicao da propriedade)."""
    GUARDIAO_FAMILIAR = ("guardiao_familiar", "Guardiao familiar", 1)
    COOPERATIVA = ("cooperativa", "Cooperativa agricola", 5)
    COMUNIDADE_TRADICIONAL = ("comunidade_tradicional", "Comunidade tradicional (quilombo/ribeirinho/aldeia)", 10)
    ASSENTAMENTO_COLETIVO = ("assentamento_coletivo", "Assentamento coletivo da Republica", 8)
    RESERVA_REGENERACAO = ("reserva_regeneracao", "Reserva de regeneracao do solo (repouso)", 0)
    USO_PUBLICO = ("uso_publico", "Uso publico (escola, enfermaria, mercado)", 0)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def familias_max(self) -> int:
        return self.value[2]


class UsoSolo(Enum):
    """Categorias de uso da terra."""
    LAVOURA_ALIMENTACAO = ("lavoura_alimentacao", "Lavoura de alimentos basicos")
    LAVOURA_DIVERSIFICADA = ("lavoura_diversificada", "Policultivo diversificado")
    PASTAGEM_REGENERATIVA = ("pastagem_regenerativa", "Pastagem rotativa regenerativa")
    AGROFLORESTA = ("agrofloresta", "Sistema agroflorestal (SAF)")
    HORTA_COMUNITARIA = ("horta_comunitaria", "Horta comunitaria de bairro")
    POMAR = ("pomar", "Pomar frutifero")
    RESERVA_NATIVA = ("reserva_nativa", "Reserva de vegetacao nativa")
    CULTURA_TRADICIONAL = ("cultura_tradicional", "Cultivo tradicional ancestral")
    INFRAESTRUTURA = ("infraestrutura", "Infraestrutura (casa, galpao, escola)")
    OCIOSO = ("ocioso", "Ocioso (sem funcao social)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusReforma(Enum):
    """Estagio da revolucao agraria num territorio."""
    DIAGNOSTICO = ("diagnostico", "Diagnostico fundiario em curso")
    NOTIFICACAO = ("notificacao", "Latifundio notificado (funcao social cobrada)")
    DESAPROPRIACAO = ("desapropriacao", "Desapropriacao decidida em assembleia")
    ASSENTAMENTO = ("assentamento", "Familias assentadas como guardias")
    REGULARIZACAO = ("regularizacao", "Regularizacao cooperativa ativa")
    CONSOLIDADO = ("consolidado", "Territorio consolidado (auto-gestionario)")
    CONFLITO = ("conflito", "Conflito fundiario ativo (grileiro/invasao)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoConflito(Enum):
    """Tipos de conflito fundiario que a Republica precisa resolver."""
    GRILAGEM = ("grilagem", "Grilagem (falsificacao de titulo)")
    INVASAO_LATIFUNDIO = ("invasao_latifundio", "Trabalhador expulso por latifundio")
    TRABALHO_ESCRAVO = ("trabalho_escravo", "Trabalho analogo a escravidao")
    DESPEJO = ("despejo", "Despejo de familia guardi")
    CONFLITO_FRONTEIRA = ("conflito_fronteira", "Disputa de fronteira entre comunidades")
    MINERACAO_ILEGAL = ("mineracao_ilegal", "Mineracao/predacao ilegal em terra guardia")
    AGROTOXICO = ("agrotoxico", "Contaminacao por agrotoxico vizinho")
    QUEIMADA_CRIMINOSA = ("queimada_criminosa", "Queimada criminosa / desmatamento")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def gravidade(self) -> int:
        return {
            "grilagem": 4,
            "invasao_latifundio": 5,
            "trabalho_escravo": 5,
            "despejo": 4,
            "conflito_fronteira": 2,
            "mineracao_ilegal": 4,
            "agrotoxico": 3,
            "queimada_criminosa": 4,
        }[self.value[0]]


class TamanhoImovel(Enum):
    """Faixas de area (modulo fiscal referencia: ~50 ha em media)."""
    MINIFUNDIO = ("minifundio", "Minifundio (insuficiente, < 1 modulo)", 0, 50)
    PEQUENO = ("pequeno", "Pequena area (1-4 modulos)", 50, 200)
    MEDIO = ("medio", "Media area (4-15 modulos)", 200, 750)
    LATIFUNDIO_DIMENSAO = ("latifundio_dimensao", "Latifundio por dimensao (>15 modulos)", 750, 99999)
    LATIFUNDIO_EXPLORACAO = ("latifundio_exploracao", "Latifundio por exploracao (ocioso/grilado)", 0, 99999)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def area_min(self) -> float:
        return self.value[2]

    @property
    def area_max(self) -> float:
        return self.value[3]


class FuncaoSocialStatus(Enum):
    """Cumprimento da funcao social da terra (Art. 186 CF/88, radicalizado)."""
    CUMPRE = ("cumpre", "Cumpre funcao social")
    PARCIAL = ("parcial", "Cumpre parcialmente")
    DESCUMPRE = ("descumpre", "Descumpre funcao social")

    @property
    def rotulo(self) -> str:
        return self.value[1]


class PlanoAgrologia(Enum):
    """Praticas regenerativas (a Republica PROIBE agricultura que exaure solo)."""
    PLANTIO_DIRETO = ("plantio_direto", "Plantio direto (nao revolver solo)")
    ADUBACAO_VERDE = ("adubacao_verde", "Adubacao verde (leguminosas)")
    COMPOSTAGEM = ("compostagem", "Compostagem comunitaria")
    ROTACAO_CULTURAS = ("rotacao_culturas", "Rotacao de culturas")
    CICLO_FECHADO = ("ciclo_fechado", "Ciclo fechado (zero insumo externo)")
    AGROFLORESTA_SUCSSIONAL = ("agrofloresta_sucessional", "Agrofloresta sucessional")
    CAPTACAO_CHUVA = ("captacao_chuva", "Captacao de agua de chuva")
    BIOINSUMOS = ("bioinsumos", "Bioinsumos (proibido agrotoxico sintetico)")
    INTEGRACAO_ANIMAL = ("integracao_animal", "Integracao lavoura-pecuaria-floresta")

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
class ImovelRural:
    """Um imovel rural no cadastro da Republica (depois da abolicao, e 'terra guardia')."""
    id: str
    nome: str
    area_hectares: float
    municipio: str
    bioma: str
    tipo_tenencia: TipoTenencia
    usos_solo: List[UsoSolo] = field(default_factory=list)
    familias_guardias: int = 0
    funcao_social: FuncaoSocialStatus = FuncaoSocialStatus.DESCUMPRE
    produtividade_pct: float = 0.0  # 0-100, vs potencial do bioma
    plano_agrologia: List[PlanoAgrologia] = field(default_factory=list)
    status: StatusReforma = StatusReforma.DIAGNOSTICO
    historico_antigo: str = ""  # quem "possuia" antes (registro historico, nao direito)


@dataclass
class FamiliaGuardia:
    """Uma familia que cuida de uma parcela de terra."""
    id: str
    nome_referencia: str
    pessoas: int
    parcela_hectares: float
    cooperativa_id: Optional[str] = None
    chegada_de: str = ""  # origem: "assentamento", "tradicional", "despejado", "voluntario"
    conhecimento_tradicional: bool = False


@dataclass
class ConflitoFundiario:
    """Conflito que a Republica precisa resolver para a revolucao avancar."""
    id: str
    tipo: TipoConflito
    territorio_id: str
    vitimas: int = 0
    familias_afetadas: int = 0
    descricao: str = ""
    resolucao_proposta: str = ""
    resolvido: bool = False


@dataclass
class CooperativaAgricola:
    """Unidade cooperativa de familias guardias (mutirao como padrao)."""
    id: str
    nome: str
    familia_ids: List[str] = field(default_factory=list)
    territorio_ids: List[str] = field(default_factory=list)
    excedente_destino: str = ""  # para onde vai o excedente (mercado aberto, outra comunidade)
    ferramentas_compartilhadas: List[str] = field(default_factory=list)


@dataclass
class DiagnosticoFundiario:
    """Snapshot da concentracao de terra num territorio."""
    territorio: str
    total_area: float
    num_imoveis: int
    indice_gini: float  # 0=igualdade, 1=concentracao absoluta
    pct_area_latifundio: float  # % da area em maos de <10% dos "ex-donos"
    familias_sem_terra: int
    familias_guardias: int
    veredito: str = ""  # DiagnosticoEngine preenche


# ============================================================================
# 3. ENGINE
# ============================================================================

class ReformaAgrariaEngine:
    """Motor da Revolucao Agraria: diagnostica, redistribui, cuida, audita."""

    def __init__(self) -> None:
        self.imoveis: Dict[str, ImovelRural] = {}
        self.familias: Dict[str, FamiliaGuardia] = {}
        self.cooperativas: Dict[str, CooperativaAgricola] = {}
        self.conflitos: Dict[str, ConflitoFundiario] = {}
        self._im_id = 0
        self._fam_id = 0
        self._coop_counter = 0
        self._conf_id = 0

    # -- cadastro ----------------------------------------------------------

    def _imovel_id(self) -> str:
        self._im_id += 1
        return f"TER-{self._im_id:04d}"

    def _familia_id(self) -> str:
        self._fam_id += 1
        return f"FAM-{self._fam_id:04d}"

    def _coop_id(self) -> str:
        self._coop_counter += 1
        return f"COOP-{self._coop_counter:04d}"

    def _conflito_id(self) -> str:
        self._conf_id += 1
        return f"CONF-{self._conf_id:04d}"

    def cadastrar_imovel(
        self,
        nome: str,
        area_hectares: float,
        municipio: str,
        bioma: str,
        tipo_tenencia: TipoTenencia,
        usos_solo: Optional[List[UsoSolo]] = None,
        familias_guardias: int = 0,
        funcao_social: FuncaoSocialStatus = FuncaoSocialStatus.DESCUMPRE,
        produtividade_pct: float = 0.0,
        plano: Optional[List[PlanoAgrologia]] = None,
        status: StatusReforma = StatusReforma.DIAGNOSTICO,
        historico_antigo: str = "",
    ) -> ImovelRural:
        im = ImovelRural(
            id=self._imovel_id(),
            nome=nome,
            area_hectares=area_hectares,
            municipio=municipio,
            bioma=bioma,
            tipo_tenencia=tipo_tenencia,
            usos_solo=usos_solo or [],
            familias_guardias=familias_guardias,
            funcao_social=funcao_social,
            produtividade_pct=produtividade_pct,
            plano_agrologia=plano or [],
            status=status,
            historico_antigo=historico_antigo,
        )
        self.imoveis[im.id] = im
        return im

    def cadastrar_familia(
        self,
        nome_referencia: str,
        pessoas: int,
        parcela_hectares: float,
        cooperativa_id: Optional[str] = None,
        chegada_de: str = "voluntario",
        conhecimento_tradicional: bool = False,
    ) -> FamiliaGuardia:
        f = FamiliaGuardia(
            id=self._familia_id(),
            nome_referencia=nome_referencia,
            pessoas=pessoas,
            parcela_hectares=parcela_hectares,
            cooperativa_id=cooperativa_id,
            chegada_de=chegada_de,
            conhecimento_tradicional=conhecimento_tradicional,
        )
        self.familias[f.id] = f
        return f

    def criar_cooperativa(
        self,
        nome: str,
        familia_ids: List[str],
        territorio_ids: List[str],
        excedente_destino: str = "mercado_aberto",
        ferramentas: Optional[List[str]] = None,
    ) -> CooperativaAgricola:
        c = CooperativaAgricola(
            id=self._coop_id(),
            nome=nome,
            familia_ids=list(familia_ids),
            territorio_ids=list(territorio_ids),
            excedente_destino=excedente_destino,
            ferramentas_compartilhadas=ferramentas or [],
        )
        self.cooperativas[c.id] = c
        # vincular familias a coop
        for fid in familia_ids:
            if fid in self.familias:
                self.familias[fid].cooperativa_id = c.id
        return c

    def registrar_conflito(
        self,
        tipo: TipoConflito,
        territorio_id: str,
        vitimas: int = 0,
        familias_afetadas: int = 0,
        descricao: str = "",
    ) -> ConflitoFundiario:
        c = ConflitoFundiario(
            id=self._conflito_id(),
            tipo=tipo,
            territorio_id=territorio_id,
            vitimas=vitimas,
            familias_afetadas=familias_afetadas,
            descricao=descricao,
        )
        self.conflitos[c.id] = c
        return c

    # -- diagnostico -------------------------------------------------------

    def classificar_tamanho(self, area: float, ocioso: bool = False) -> TamanhoImovel:
        """Classifica imovel por area e exploracao."""
        if ocioso and area >= TamanhoImovel.PEQUENO.area_min:
            return TamanhoImovel.LATIFUNDIO_EXPLORACAO
        for t in [TamanhoImovel.MINIFUNDIO, TamanhoImovel.PEQUENO,
                  TamanhoImovel.MEDIO, TamanhoImovel.LATIFUNDIO_DIMENSAO]:
            if t.area_min <= area < t.area_max:
                return t
        return TamanhoImovel.LATIFUNDIO_DIMENSAO

    def indice_gini_areas(self) -> float:
        """Gini de concentracao de area entre imoveis (0=igual, 1=concentrado)."""
        areas = sorted(im.area_hectares for im in self.imoveis.values())
        n = len(areas)
        if n == 0:
            return 0.0
        total = sum(areas)
        if total == 0:
            return 0.0
        cum = 0.0
        soma_pond = 0.0
        for i, a in enumerate(areas, start=1):
            soma_pond += i * a
        gini = (2 * soma_pond) / (n * total) - (n + 1) / n
        return round(gini, 4)

    def diagnosticar(self, territorio: str) -> DiagnosticoFundiario:
        """Produz o diagnostico fundiario de um territorio."""
        ims = [im for im in self.imoveis.values() if im.municipio == territorio]
        total_area = sum(im.area_hectares for im in ims)
        num = len(ims)
        if num == 0:
            return DiagnosticoFundiario(
                territorio=territorio,
                total_area=0.0,
                num_imoveis=0,
                indice_gini=0.0,
                pct_area_latifundio=0.0,
                familias_sem_terra=0,
                familias_guardias=0,
                veredito="Territorio vazio no cadastro.",
            )
        gini = self.indice_gini_areas()
        # % da area em maos de latifundios
        area_lat = sum(
            im.area_hectares for im in ims
            if self.classificar_tamanho(im.area_hectares, ocioso=(im.funcao_social == FuncaoSocialStatus.DESCUMPRE))
            in (TamanhoImovel.LATIFUNDIO_DIMENSAO, TamanhoImovel.LATIFUNDIO_EXPLORACAO)
        )
        pct_lat = (area_lat / total_area * 100.0) if total_area else 0.0
        familias_guardias = sum(im.familias_guardias for im in ims)
        familias_sem_terra = max(0, int((pct_lat / 100.0) * familias_guardias / 4) if familias_guardias else 0)

        if gini > 0.7 or pct_lat > 50:
            veredito = "CONCENTRACAO CRITICA: revolicao agraria URGENTE."
        elif gini > 0.4 or pct_lat > 25:
            veredito = "CONCENTRACAO ALTA: notificar latifundios, cobrar funcao social."
        elif gini > 0.2:
            veredito = "CONCENTRACAO MODERADA: regularizar e cooperativizar."
        else:
            veredito = "TERRITORIO EQUITATIVO: consolidar cooperativas."

        return DiagnosticoFundiario(
            territorio=territorio,
            total_area=total_area,
            num_imoveis=num,
            indice_gini=gini,
            pct_area_latifundio=round(pct_lat, 1),
            familias_sem_terra=familias_sem_terra,
            familias_guardias=familias_guardias,
            veredito=veredito,
        )

    # -- funcao social -----------------------------------------------------

    def auditar_funcao_social(self, imovel_id: str) -> Tuple[FuncaoSocialStatus, List[str]]:
        """Verifica os 4 requisitos radicais da funcao social."""
        im = self.imoveis.get(imovel_id)
        if im is None:
            return FuncaoSocialStatus.DESCUMPRE, ["Imovel nao encontrado."]
        faltas: List[str] = []
        e_reserva = im.tipo_tenencia == TipoTenencia.RESERVA_REGENERACAO
        # 1. aproveitamento racional (reserva de regeneracao e terra em descanso -- produtividade 0 e correto)
        if not e_reserva and im.produtividade_pct < 40:
            faltas.append(f"Produtividade baixa ({im.produtividade_pct:.0f}% do potencial).")
        # 2. uso adequado dos recursos naturais (agrologia)
        if not im.plano_agrologia:
            faltas.append("Sem plano de agrologia (solo sendo exaurido).")
        # 3. observancia da legislacao trabalhista (sem trabalho escravo)
        #    conflitos do tipo TRABALHO_ESCRAVO no territorio = descumpre
        for conf in self.conflitos.values():
            if (conf.tipo == TipoConflito.TRABALHO_ESCRAVO
                    and conf.territorio_id == im.id and not conf.resolvido):
                faltas.append("Trabalho analogo a escravidao detectado (BLOQUEANTE).")
                break
        # 4. bem-estar de quem trabalha (densidade de familias razoavel)
        if im.familias_guardias == 0 and im.tipo_tenencia != TipoTenencia.RESERVA_REGENERACAO:
            faltas.append("Nenhuma familia guardia: terra abandonada.")
        if faltas:
            im.funcao_social = FuncaoSocialStatus.PARCIAL if len(faltas) == 1 else FuncaoSocialStatus.DESCUMPRE
        else:
            im.funcao_social = FuncaoSocialStatus.CUMPRE
        return im.funcao_social, faltas

    # -- revolucao (pipeline) ----------------------------------------------

    def notificar_latifundio(self, imovel_id: str) -> Optional[str]:
        """Notifica um latifundio: cumpra funcao social ou sera devolvido."""
        im = self.imoveis.get(imovel_id)
        if im is None:
            return None
        tam = self.classificar_tamanho(im.area_hectares, ocioso=(im.funcao_social == FuncaoSocialStatus.DESCUMPRE))
        if tam not in (TamanhoImovel.LATIFUNDIO_DIMENSAO, TamanhoImovel.LATIFUNDIO_EXPLORACAO):
            return f"{im.id} nao e latifundio ({tam.rotulo})."
        status, faltas = self.auditar_funcao_social(im.id)
        if status == FuncaoSocialStatus.CUMPRE:
            im.status = StatusReforma.REGULARIZACAO
            return f"{im.id} cumpre funcao social -> regularizar como cooperativa."
        im.status = StatusReforma.NOTIFICACAO
        return (f"NOTIFICADO {im.id} ({tam.rotulo}, {im.area_hectares:.0f} ha). "
                f"Faltas: {'; '.join(faltas) if faltas else 'none'}. Prazo para regularizar.")

    def desaproropriar(self, imovel_id: str, familias_assentar: List[str]) -> Optional[str]:
        """Desapropria (assembleia decide) e assenta familias guardias."""
        im = self.imoveis.get(imovel_id)
        if im is None:
            return None
        if im.status not in (StatusReforma.NOTIFICACAO, StatusReforma.DIAGNOSTICO):
            return f"{im.id} em status {im.status.rotulo} -- nao elegivel para desapropriacao agora."
        # parar de reconhecer o "ex-dono": a terra volta ao territorio
        im.historico_antigo = im.historico_antigo or im.nome
        im.nome = f"Territorio Livre {im.id}"
        im.tipo_tenencia = TipoTenencia.ASSENTAMENTO_COLETIVO
        # parcelar entre familias
        if familias_assentar:
            parcela = im.area_hectares / len(familias_assentar)
            for fid in familias_assentar:
                fam = self.familias.get(fid)
                if fam:
                    fam.parcela_hectares = round(parcela, 2)
                    fam.chegada_de = "assentamento"
            im.familias_guardias = len(familias_assentar)
        im.status = StatusReforma.ASSENTAMENTO
        im.funcao_social = FuncaoSocialStatus.PARCIAL
        return (f"DESAPROPRIVADO {im.id}: {len(familias_assentar)} familias guardias assentadas, "
                f"{im.area_hectares:.0f} ha sob cuidado coletivo.")

    def consolidar_cooperativa(
        self,
        nome: str,
        territorio_ids: List[str],
        familias_ids: List[str],
        excedente: str = "mercado_aberto",
        ferramentas: Optional[List[str]] = None,
    ) -> CooperativaAgricola:
        """Transforma assentamento em cooperativa auto-gestionaria."""
        coop = self.criar_cooperativa(nome, familias_ids, territorio_ids, excedente, ferramentas)
        for tid in territorio_ids:
            im = self.imoveis.get(tid)
            if im:
                im.tipo_tenencia = TipoTenencia.COOPERATIVA
                im.status = StatusReforma.CONSOLIDADO
                im.funcao_social = FuncaoSocialStatus.CUMPRE
        return coop

    # -- resolucao de conflitos --------------------------------------------

    def conflitos_por_gravidade(self) -> List[ConflitoFundiario]:
        return sorted(
            self.conflitos.values(),
            key=lambda c: (-c.tipo.gravidade, -c.familias_afetadas),
        )

    def resolver_conflito(self, conflito_id: str, resolucao: str) -> bool:
        c = self.conflitos.get(conflito_id)
        if c is None:
            return False
        c.resolucao_proposta = resolucao
        c.resolvido = True
        return True

    # -- metricas ----------------------------------------------------------

    def area_total(self) -> float:
        return sum(im.area_hectares for im in self.imoveis.values())

    def area_ociosa(self) -> float:
        return sum(
            im.area_hectares for im in self.imoveis.values()
            if im.funcao_social == FuncaoSocialStatus.DESCUMPRE
        )

    def familias_atendidas(self) -> int:
        return sum(im.familias_guardias for im in self.imoveis.values())

    def pessoas_atendidas(self) -> int:
        ids = {f.id: f for f in self.familias.values()}
        total = 0
        for im in self.imoveis.values():
            total += im.familias_guardias * 4  # media 4 pessoas/familia
        return total

    def scorecard(self) -> Dict[str, Any]:
        return {
            "imoveis_cadastrados": len(self.imoveis),
            "area_total_ha": round(self.area_total(), 1),
            "area_ociosa_ha": round(self.area_ociosa(), 1),
            "pct_ociosa": round(self.area_ociosa() / self.area_total() * 100, 1) if self.area_total() else 0.0,
            "familias_guardias": self.familias_atendidas(),
            "cooperativas": len(self.cooperativas),
            "conflitos_abertos": sum(1 for c in self.conflitos.values() if not c.resolvido),
            "indice_gini": self.indice_gini_areas(),
            "consolidados": sum(1 for im in self.imoveis.values() if im.status == StatusReforma.CONSOLIDADO),
        }


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    e = ReformaAgrariaEngine()

    print("=" * 70)
    print("OpenAgrarianRevolution -- A Terra e de Quem a Cuida")
    print("=" * 70)

    # --- Contexto: territorio "Sertao do Sao Francisco" ---
    # Cadastro: um latifundio ocioso (caso classico), uma reserva, pequenas areas
    latif = e.cadastrar_imovel(
        nome="Fazenda Boa Vista (ex-latifundio)",
        area_hectares=2500.0,
        municipio="Sertao do Sao Francisco",
        bioma="caatinga",
        tipo_tenencia=TipoTenencia.GUARDIAO_FAMILIAR,  # ainda herdado do antigo
        usos_solo=[UsoSolo.PASTAGEM_REGENERATIVA, UsoSolo.OCIOSO],
        familias_guardias=3,
        funcao_social=FuncaoSocialStatus.DESCUMPRE,
        produtividade_pct=15.0,
        plano=[],  # sem agrologia
        historico_antigo="Familia herdeira de titulo duvidoso",
    )

    pequeno_a = e.cadastrar_imovel(
        nome="Sitio Aconchego",
        area_hectares=30.0,
        municipio="Sertao do Sao Francisco",
        bioma="caatinga",
        tipo_tenencia=TipoTenencia.GUARDIAO_FAMILIAR,
        usos_solo=[UsoSolo.LAVOURA_ALIMENTACAO, UsoSolo.POMAR],
        familias_guardias=1,
        funcao_social=FuncaoSocialStatus.PARCIAL,
        produtividade_pct=70.0,
        plano=[PlanoAgrologia.COMPOSTAGEM, PlanoAgrologia.ROTACAO_CULTURAS],
    )

    reserva = e.cadastrar_imovel(
        nome="Reserva Caatinga Viva",
        area_hectares=800.0,
        municipio="Sertao do Sao Francisco",
        bioma="caatinga",
        tipo_tenencia=TipoTenencia.RESERVA_REGENERACAO,
        usos_solo=[UsoSolo.RESERVA_NATIVA],
        familias_guardias=0,
        funcao_social=FuncaoSocialStatus.CUMPRE,
        produtividade_pct=0.0,
        plano=[PlanoAgrologia.CICLO_FECHADO],
    )

    # --- Diagnostico ---
    diag = e.diagnosticar("Sertao do Sao Francisco")
    print(f"\n[DIAGNOSTICO] {diag.territorio}")
    print(f"  Area total: {diag.total_area:.0f} ha | Imoveis: {diag.num_imoveis}")
    print(f"  Indice de Gini: {diag.indice_gini:.3f} (0=igual, 1=concentrado)")
    print(f"  % area em latifundios: {diag.pct_area_latifundio:.1f}%")
    print(f"  Familias guardias: {diag.familias_guardias}")
    print(f"  VEREDITO: {diag.veredito}")

    # --- Notificar latifundio ---
    print("\n[NOTIFICACAO]")
    msg = e.notificar_latifundio(latif.id)
    print(f"  {msg}")

    # --- Auditar funcao social ---
    print("\n[AUDITORIA DE FUNCAO SOCIAL]")
    for iid in [latif.id, pequeno_a.id, reserva.id]:
        status, faltas = e.auditar_funcao_social(iid)
        im = e.imoveis[iid]
        print(f"  {iid} ({im.nome[:30]}): {status.rotulo}")
        for f in faltas:
            print(f"      - {f}")

    # --- Conflito: trabalho escravo detectado no latifundio ---
    conflito = e.registrar_conflito(
        tipo=TipoConflito.TRABALHO_ESCRAVO,
        territorio_id=latif.id,
        vitimas=2,
        familias_afetadas=8,
        descricao="Trabalhadores resgatados em condicoes analogas a escravidao.",
    )
    print(f"\n[CONFLITO REGISTRADO] {conflito.id}: {conflito.tipo.rotulo}")
    print(f"  Gravidade: {conflito.tipo.gravidade}/5 | Familias afetadas: {conflito.familias_afetadas}")

    # --- Desapropriar: assembleia decide ---
    print("\n[DESAPROPRIACAO POR ASSEMBLEIA]")
    fams = [
        e.cadastrar_familia("Familia Maria das Dores", 5, 0.0, chegada_de="despejado"),
        e.cadastrar_familia("Familia Jose Pereira", 4, 0.0, chegada_de="despejado"),
        e.cadastrar_familia("Familia Ana Beatriz", 6, 0.0, chegada_de="voluntario"),
        e.cadastrar_familia("Familia Severino", 5, 0.0, chegada_de="despejado", conhecimento_tradicional=True),
    ]
    res = e.desaproropriar(latif.id, [f.id for f in fams])
    print(f"  {res}")

    # Resolver o conflito de trabalho escravo
    e.resolver_conflito(conflito.id, "Ex-dono removido; familias guardias assumem; recuperacao das vitimas via OpenPsychologyReparation.")
    print(f"  Conflito {conflito.id} resolvido: {conflito.resolucao_proposta}")

    # --- Consolidar cooperativa ---
    print("\n[CONSOLIDACAO COOPERATIVA]")
    coop = e.consolidar_cooperativa(
        nome="Cooperativa Terra Livre Sertao",
        territorio_ids=[latif.id],
        familias_ids=[f.id for f in fams],
        excedente="mercado_aberto",
        ferramentas=["trator_compartilhado", "casa_de_farinha", "cisterna_coletiva"],
    )
    print(f"  {coop.id}: {coop.nome}")
    print(f"  Familias: {len(coop.familia_ids)} | Territorios: {len(coop.territorio_ids)}")
    print(f"  Ferramentas compartilhadas: {', '.join(coop.ferramentas_compartilhadas)}")

    # --- Plano de agrologia no novo territorio livre ---
    latif.usos_solo = [UsoSolo.AGROFLORESTA, UsoSolo.LAVOURA_DIVERSIFICADA, UsoSolo.POMAR]
    latif.plano_agrologia = [
        PlanoAgrologia.AGROFLORESTA_SUCSSIONAL,
        PlanoAgrologia.CAPTACAO_CHUVA,
        PlanoAgrologia.BIOINSUMOS,
        PlanoAgrologia.CICLO_FECHADO,
    ]
    latif.produtividade_pct = 65.0
    status_final, _ = e.auditar_funcao_social(latif.id)
    print(f"\n[POS-REVOLUCAO] {latif.id} funcao social: {status_final.rotulo}")
    print(f"  Status: {latif.status.rotulo} | Tenencia: {latif.tipo_tenencia.rotulo}")

    # --- Scorecard final ---
    print("\n" + "=" * 70)
    print("[SCORECARD DA REVOLUCAO AGRARIA]")
    print("=" * 70)
    sc = e.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- Conflitos ordenados por gravidade ---
    print("\n[CONFLITOS POR GRAVIDADE]")
    for c in e.conflitos_por_gravidade():
        flag = "OK" if c.resolvido else "ABERTO"
        print(f"  [{flag}] {c.id} {c.tipo.rotulo} (grav={c.tipo.gravidade}) "
              f"vitimas={c.vitimas} familias={c.familias_afetadas}")

    # --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Por que a Republica ABOLI a propriedade da terra")
    print("=" * 70)
    print("""
P1 (Anti-elitismo): O latifundio e o mecanismo ORIGINAL de elite.
   Antes do banco, antes da empresa, antes da midia: a TERRA.
   Quem cerca a terra cerca a VIDA de quem precisa dela pra comer.
   Abolir a propriedade da terra = extirpar a raiz da desigualdade.

P2 (Autonomia): Quem planta colhe. Quem cuida decide.
   Ninguem morre de fome vigiando cerca de terra que nao cultiva.
   O corpo que sua na roca e dono do fruto -- nao de hectares.

P3 (Trabalho = impacto): "Dono de terra" nao e trabalho. E RENDA.
   Renda de propriedade e extrativismo puro: tirar sem botar.
   A Republica so reconhece credito por IMPACTO (alimentar gente).
   Latifundio improdutivo e roubo sistemico, nao "investimento".

P4 (Democracia): A assembleia do territorio decide o uso da terra.
   Nao ha "dono" para negociar as escuras com madeireira/mineradora.
   O guardiao tem MANDATO REVOGAVEL: abandona, devolve.
   Ninguem herda hectares. Herda-se o oficio, nao a propriedade.

A REVOLUCAO AGRARIA NAO E "REFORMA". E ABOLICAO.
Reforma distribui propriedade. Abolicao extingue a categoria.
A terra volta a ser o que sempre foi: CONDICAO DE VIDA,
nao ativo no balanco patrimonial de ninguem.
""")


if __name__ == "__main__":
    _demo()
