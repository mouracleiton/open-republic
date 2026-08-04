#!/usr/bin/env python3
"""
OpenFatoDadoOpiniao -- Gate Epistemologico da Republica
=========================================================
"Opiniao e opiniao. Dados sao dados. Fato exige dado real
 + amostra representativa + analise rigorosa. Sem atalho."

O PROBLEMA:
  Jornal diz 'a economia melhora' com dado de 16 capitais.
  Politico diz 'crime caiu' com dado de delegacia.
  Influencer diz 'remedio cura' com dado de laboratorio da fabrica.
  Todos apresentam OPINIAO ou DADO BRUTO como se fosse FATO.

A SOLUCAO:
  Toda afirmação no sistema da Republica tem CLASSIFICACAO:
    DADO  -- numero bruto, observacao, medicao
    FATO  -- dado + analise + amostra representativa + reproduzivel
    OPINIAO -- interpretacao, pode citar dados, mas e interpretacao

  Nivel 0: so FATO vira politica publica.
  Nivel 1: DADO suporta decisao com ressalva.
  Nivel 2: OPINIAO nao vira nada. Nunca. So debate.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional
from enum import Enum
from dataclasses import dataclass, field


class ClassificacaoEpistemica(Enum):
    """Classificacao de toda afirmação no sistema."""
    DADO = (
        "dado",
        "Dado: numero bruto, observacao, medicao. Sem interpretacao.",
        "Precisa de analise para virar fato.",
        1,
    )
    FATO = (
        "fato",
        "Fato: dado + analise + amostra representativa + reproduzivel.",
        "Pode fundamentar politica publica.",
        0,
    )
    OPINIAO = (
        "opiniao",
        "Opiniao: interpretacao. Pode citar dados. Continua sendo opiniao.",
        "Nao vira politica. Vira debate.",
        2,
    )

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def limite(self) -> str:
        return self.value[2]

    @property
    def nivel(self) -> int:
        """0=fato (maximo), 1=dado, 2=opiniao (minimo)."""
        return self.value[3]


class CriterioFato(Enum):
    """Os 7 criterios para um DADO virar FATO."""
    AMOSTRA_REPRESENTATIVA = ("amostra", "Amostra representa a populacao (nao so 16 capitais)")
    METODO_REPRODUZIVEL = ("reproduzivel", "Outra pessoa coleta o mesmo dado e chega no mesmo resultado")
    FONTE_INDEPENDENTE = ("independente", "Fonte nao tem interesse no resultado")
    CRUZAMENTO_TRIANGULAR = ("triangular", "2+ fontes independentes convergem")
    AUSENCIA_VIES = ("vies", "Metodo nao seleciona a favor de conclusao")
    MAGNITUDE_RELEVANTE = ("magnitude", "Diferenca e grande o suficiente pra importar")
    TEMPORAL_CONSISTENTE = ("temporal", "Resultado se mantem no tempo, nao e ruido")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class FalaciaComum(Enum):
    """Falacias que transformam dado/opiniao em 'fato falso'."""
    DADO_PARCIAL = ("parcial", "Dado real mas incompleto (IPCA sem periferia)")
    AMOSTRA_ENVIESADA = ("enviesada", "Amostra nao representa (PNAD por telefone)")
    FONTE_INTERESSADA = ("interessada", "Fonte lucra com o resultado (lab da fabrica)")
    CORRELACAO_CAUSALIDADE = ("correlacao", "Correlacao nao e causalidade")
    MEDIA_ENGENHARIA = ("media_eng", "Media esconde desigualdade (PIB per capita)")
    DADO_DESCONTEXTUALIZADO = ("sem_contexto", "Numero sem contexto (homicidios cairam... menos denuncias)")
    OPINIAO_COMO_FATO = ("opiniao_fato", "Apresentar interpretacao como fato")
    DADO_OBSOLETO = ("obsoleto", "Dado de 2020 apresentado como atual")

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
class Afirmação:
    """Uma afirmação classificada epistemologicamente."""
    texto: str
    classificacao: ClassificacaoEpistemica
    dados_base: List[str] = field(default_factory=list)
    criterios_cumpridos: List[CriterioFato] = field(default_factory=list)
    criterios_faltantes: List[CriterioFato] = field(default_factory=list)
    falacias_detectadas: List[FalaciaComum] = field(default_factory=list)
    fonte: str = ""
    representatividade: float = 0.0  # 0-1, quao representativo
    reproduzivel: bool = False
    confidence: float = 0.0           # 0-1, confidence final


# ============================================================================
# 3. GATE EPISTEMICO
# ============================================================================

class GateEpistemico:
    """
    Gate que classifica toda afirmação.

    DADO nao e FATO.
    OPINIAO nao e DADO.
    FATO exige os 7 criterios.
    """

    NOME = "OpenFatoDadoOpiniao"
    VERSAO = "0.1.0-spec"

    def classificar(
        self,
        texto: str,
        tem_dado: bool = False,
        tem_analise: bool = False,
        amostra_representativa: bool = False,
        reproduzivel: bool = False,
        fonte_independente: bool = False,
        cruzamento_triangular: bool = False,
        ausencia_vies: bool = False,
        magnitude_relevante: bool = False,
        temporal_consistente: bool = False,
    ) -> Afirmação:
        """Classifica uma afirmação."""

        criterios_map = {
            CriterioFato.AMOSTRA_REPRESENTATIVA: amostra_representativa,
            CriterioFato.METODO_REPRODUZIVEL: reproduzivel,
            CriterioFato.FONTE_INDEPENDENTE: fonte_independente,
            CriterioFato.CRUZAMENTO_TRIANGULAR: cruzamento_triangular,
            CriterioFato.AUSENCIA_VIES: ausencia_vies,
            CriterioFato.MAGNITUDE_RELEVANTE: magnitude_relevante,
            CriterioFato.TEMPORAL_CONSISTENTE: temporal_consistente,
        }

        cumpridos = [c for c, v in criterios_map.items() if v]
        faltantes = [c for c, v in criterios_map.items() if not v]

        # FATO exige TODOS os 7
        if tem_dado and tem_analise and len(cumpridos) == 7:
            classe = ClassificacaoEpistemica.FATO
            confidence = 1.0
        elif tem_dado:
            classe = ClassificacaoEpistemica.DADO
            confidence = len(cumpridos) / 7.0
        else:
            classe = ClassificacaoEpistemica.OPINIAO
            confidence = 0.0

        # Representatividade
        rep = 1.0 if amostra_representativa else 0.3

        return Afirmação(
            texto=texto,
            classificacao=classe,
            criterios_cumpridos=cumpridos,
            criterios_faltantes=faltantes,
            fonte="",
            representatividade=rep,
            reproduzivel=reproduzivel,
            confidence=confidence,
        )

    # -- detectar falacias ------------------------------------------------

    def detectar_falacias(
        self,
        af: Afirmação,
        amostra_cobertura: Optional[float] = None,
        fonte_tem_lucro: bool = False,
        dado_antigo_anos: Optional[int] = None,
    ) -> List[FalaciaComum]:
        falacias = []

        if amostra_cobertura is not None and amostra_cobertura < 0.5:
            falacias.append(FalaciaComum.AMOSTRA_ENVIESADA)
        if fonte_tem_lucro:
            falacias.append(FalaciaComum.FONTE_INTERESSADA)
        if dado_antigo_anos is not None and dado_antigo_anos > 2:
            falacias.append(FalaciaComum.DADO_OBSOLETO)
        if af.classificacao == ClassificacaoEpistemica.OPINIAO and af.criterios_cumpridos:
            falacias.append(FalaciaComum.OPINIAO_COMO_FATO)

        af.falacias_detectadas = falacias
        return falacias

    # -- pode virar politica? ----------------------------------------------

    def pode_virar_politica(self, af: Afirmação) -> bool:
        """So FATO vira politica publica."""
        return (
            af.classificacao == ClassificacaoEpistemica.FATO
            and len(af.criterios_faltantes) == 0
            and not af.falacias_detectadas
        )

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "classificacoes": len(list(ClassificacaoEpistemica)),
            "criterios_fato": len(list(CriterioFato)),
            "falacias": len(list(FalaciaComum)),
        }


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    gate = GateEpistemico()

    print("=" * 70)
    print(f"{gate.NOME} v{gate.VERSAO} -- Gate Epistemologico")
    print("=" * 70)

    # --- Classificacao ---
    print("\n[CLASSIFICACAO EPISTEMICA]\n")
    for c in ClassificacaoEpistemica:
        print(f"  {c.id.upper()} (nivel {c.nivel})")
        print(f"    {c.rotulo}")
        print(f"    {c.limite}\n")

    # --- 7 criterios ---
    print(f"\n[OS 7 CRITERIOS PARA DADO -> FATO]\n")
    for c in CriterioFato:
        print(f"  {c.id:<16} {c.rotulo}")

    # --- Falacias ---
    print(f"\n\n[FALACIAS COMUNS ({len(list(FalaciaComum))})]\n")
    for f in FalaciaComum:
        print(f"  {f.id:<20} {f.rotulo}")

    # --- Simulacao 1: IPCA (DADO, nao FATO) ---
    print("\n\n[SIMULACAO 1: 'Inflacao foi 4.1%']\n")
    af1 = gate.classificar(
        "Inflacao foi 4.1%",
        tem_dado=True,
        tem_analise=True,
        amostra_representativa=False,  # so 16 capitais
        reproduzivel=True,
        fonte_independente=True,
        cruzamento_triangular=True,
        ausencia_vies=False,           # nao mede periferia
        magnitude_relevante=True,
        temporal_consistente=True,
    )
    fal1 = gate.detectar_falacias(af1, amostra_cobertura=0.30)
    print(f"  Classificacao: {af1.classificacao.id.upper()}")
    print(f"  Confidence: {af1.confidence:.0%}")
    print(f"  Representatividade: {af1.representatividade:.0%}")
    print(f"  Criterios cumpridos: {len(af1.criterios_cumpridos)}/7")
    print(f"  Faltantes: {[c.id for c in af1.criterios_faltantes]}")
    print(f"  Falacias: {[f.id for f in fal1]}")
    print(f"  Pode virar politica: {gate.pode_virar_politica(af1)}")

    # --- Simulacao 2: Censo proprio (FATO) ---
    print("\n\n[SIMULACAO 2: 'Escola X nao tem agua (censo proprio, 3 fontes)']\n")
    af2 = gate.classificar(
        "Escola X nao tem agua potavel",
        tem_dado=True,
        tem_analise=True,
        amostra_representativa=True,   # foi la, mediu
        reproduzivel=True,             # outro cidadao reproduce
        fonte_independente=True,       # cidadao nao tem interesse
        cruzamento_triangular=True,    # 3 fontes
        ausencia_vies=True,            # medicao fisica
        magnitude_relevante=True,      # sem agua = sem agua
        temporal_consistente=True,     # verificavel a qualquer momento
    )
    fal2 = gate.detectar_falacias(af2, amostra_cobertura=1.0)
    print(f"  Classificacao: {af2.classificacao.id.upper()}")
    print(f"  Confidence: {af2.confidence:.0%}")
    print(f"  Criterios cumpridos: {len(af2.criterios_cumpridos)}/7")
    print(f"  Faltantes: {[c.id for c in af2.criterios_faltantes]}")
    print(f"  Falacias: {[f.id for f in fal2] or 'nenhuma'}")
    print(f"  Pode virar politica: {gate.pode_virar_politica(af2)}")

    # --- Simulacao 3: Opiniao ---
    print("\n\n[SIMULACAO 3: 'Escola publicas estao melhores']\n")
    af3 = gate.classificar(
        "Escolas publicas estao melhores",
        tem_dado=False,
        tem_analise=False,
    )
    print(f"  Classificacao: {af3.classificacao.id.upper()}")
    print(f"  Confidence: {af3.confidence:.0%}")
    print(f"  Pode virar politica: {gate.pode_virar_politica(af3)}")

    # --- Filosofia ---
    print("\n\n" + "=" * 70)
    print("FILOSOFIA")
    print("=" * 70)
    print("""
  Opiniao e opiniao.
  Dados sao dados.
  Fato exige os 7 criterios. Sem atalho.

  O jornal que diz 'economia melhora' com IPCA de 16 capitais
  emite DADO PARCIAL como se fosse FATO. Nao e. E opiniao com dado.

  O politico que diz 'crime caiu' com dado de delegacia
  emite DADO ENVIESADO (menos denuncia != menos crime).

  O influencer que diz 'remedio cura' com dado do laboratorio
  emite DADO DE FONTE INTERESSADA.

  Todos apresentam OPINIAO como FATO.

  A Republica nao faz isso. Classifica. Declara. Separou.

  So FATO vira politica publica.
  DADO fundamenta com ressalva.
  OPINIAO nao vira nada. So debate.
""")


if __name__ == "__main__":
    _demo()
