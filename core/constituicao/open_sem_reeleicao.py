#!/usr/bin/env python3
"""
OpenSemReeleicao -- Reeleição é por Mérito
=============================================
"Teve cargo e entregou? Pode voltar.
 Teve cargo e vacilou? Nunca mais.
 Reeleição não é direito. É consequência de trabalho."

POLÍTICA OFICIAL DA OPENREPUBLIC:

1. QUEM NUNCA TEVE CARGO = AUTORIZADO (gente nova, sempre)

2. QUEM TEVE CARGO E ENTREGOU (mérito comprovado) = AUTORIZADO
   Resolveu problema. Indicador melhorou. Tem evidência.

3. QUEM TEVE CARGO E VACILOU = BLOQUEADO PRA SEMPRE
   Teve a chance. Não entregou. Não volta. Não troca. Não é indicado.

MÉRITO = resultado medido, não opinião.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional
from enum import Enum
from dataclasses import dataclass, field


class TipoCargo(Enum):
    PRESIDENTE = "presidente"
    GOVERNADOR = "governador"
    SENADOR = "senador"
    DEPUTADO_FEDERAL = "deputado_federal"
    DEPUTADO_ESTADUAL = "deputado_estadual"
    PREFEITO = "prefeito"
    VEREADOR = "vereador"
    MINISTRO = "ministro"
    SECRETARIO = "secretario"


class StatusEndosso(Enum):
    AUTORIZADO = "autorizado"     # gente nova ou mérito comprovado
    BLOQUEADO = "bloqueado"       # teve cargo e vacilou


@dataclass
class CargoOcupado:
    cargo: TipoCargo
    periodo: str
    resolveu: Optional[bool] = None   # True = entregou, False = vacilou, None = sem dado
    evidencia: str = ""               # "IDEB 4.2 -> 5.8 (INEP)"
    observacao: str = ""


@dataclass
class AvaliacaoCandidatura:
    nome: str
    cargo_desejado: TipoCargo
    status: StatusEndosso
    cargos_anteriores: List[CargoOcupado]
    motivo: str
    tem_merito: bool = False

    @property
    def endossado(self) -> bool:
        return self.status == StatusEndosso.AUTORIZADO

    def resumo(self) -> str:
        icon = "✅" if self.endossado else "🚫"
        merito = " [MÉRITO]" if self.tem_merito else ""
        return f"{icon} {self.nome}: {self.status.value.upper()}{merito} — {self.motivo}"


def avaliar_candidatura(
    nome: str,
    cargo_desejado: TipoCargo,
    cargos_anteriores: List[CargoOcupado],
) -> AvaliacaoCandidatura:
    """
    Avalia se alguém pode ser endossado.

    REGRAS:
    1. Sem cargos anteriores = AUTORIZADO (gente nova)
    2. Teve cargo + resolveu (mérito) = AUTORIZADO
    3. Teve cargo + vacilou = BLOQUEADO
    4. Teve cargo + sem dado = BLOQUEADO (sem evidência de mérito = sem endosso)
    """

    # 1. Gente nova
    if not cargos_anteriores:
        return AvaliacaoCandidatura(
            nome, cargo_desejado, StatusEndosso.AUTORIZADO, cargos_anteriores,
            "Nunca teve cargo político. Gente nova. Endossado.",
            tem_merito=False,
        )

    # 2. Verificar mérito: TODOS os cargos devem ter resolveu=True
    #    Se ALGUM cargo tem resolveu=False, bloqueado
    vacilou_em_algum = any(c.resolveu is False for c in cargos_anteriores)
    resolveu_todos = all(c.resolveu is True for c in cargos_anteriores) if cargos_anteriores else False

    if vacilou_em_algum:
        c_vacilou = [c for c in cargos_anteriores if c.resolveu is False][0]
        cargos_str = ", ".join(
            f"{c.cargo.value} ({c.periodo})" for c in cargos_anteriores
        )
        return AvaliacaoCandidatura(
            nome, cargo_desejado, StatusEndosso.BLOQUEADO, cargos_anteriores,
            f"Teve cargo(s): {cargos_str}. Vacilou em {c_vacilou.cargo.value} "
            f"({c_vacilou.periodo}). Teve a chance. Não entregou. Bloqueado.",
            tem_merito=False,
        )

    if resolveu_todos:
        evidencias = [c.evidencia for c in cargos_anteriores if c.evidencia]
        ev_str = " | ".join(evidencias) if evidencias else "sem evidência detalhada"
        return AvaliacaoCandidatura(
            nome, cargo_desejado, StatusEndosso.AUTORIZADO, cargos_anteriores,
            f"Teve cargo(s) e ENTREGOU. Mérito comprovado: {ev_str}. "
            f"Reeleição por mérito. Endossado.",
            tem_merito=True,
        )

    # 4. Teve cargo mas sem dado de resultado = bloqueado (sem evidência = sem endosso)
    cargos_str = ", ".join(
        f"{c.cargo.value} ({c.periodo})" for c in cargos_anteriores
    )
    return AvaliacaoCandidatura(
        nome, cargo_desejado, StatusEndosso.BLOQUEADO, cargos_anteriores,
        f"Teve cargo(s): {cargos_str}. Sem evidência de que resolveu. "
        f"Sem mérito comprovado = sem endosso. Bloqueado.",
        tem_merito=False,
    )


# ============================================================================
# DEMO
# ============================================================================

def _demo():
    print("=" * 70)
    print("OPEN REELEIÇÃO POR MÉRITO")
    print("=" * 70)
    print()
    print("REGRA:")
    print("  Gente nova = AUTORIZADO (sempre)")
    print("  Teve cargo + entregou = AUTORIZADO (mérito)")
    print("  Teve cargo + vacilou = BLOQUEADO (nunca mais)")
    print("  Teve cargo + sem evidência = BLOQUEADO (sem mérito = sem endosso)")
    print()

    casos = [
        ("GENTE NOVA", TipoCargo.DEPUTADO_FEDERAL, []),

        ("ENTREGOU (mérito)", TipoCargo.GOVERNADOR, [
            CargoOcupado(TipoCargo.GOVERNADOR, "2019-2022", True,
                         "IDEB 4.2 -> 5.8 (INEP)", "Educação melhorou"),
        ]),

        ("VACILOU", TipoCargo.GOVERNADOR, [
            CargoOcupado(TipoCargo.GOVERNADOR, "2019-2022", False,
                         "Obras paradas", "Não entregou"),
        ]),

        ("SEM EVIDÊNCIA", TipoCargo.SENADOR, [
            CargoOcupado(TipoCargo.DEPUTADO_FEDERAL, "2019-2022", None,
                         "", "Sem dado de resultado"),
        ]),

        ("ENTREGOU NUM, VACILOU NOUTRO", TipoCargo.SENADOR, [
            CargoOcupado(TipoCargo.DEPUTADO_FEDERAL, "2015-2018", True,
                         "Aprovou leis úteis", "Bom"),
            CargoOcupado(TipoCargo.GOVERNADOR, "2019-2022", False,
                         "Fome aumentou", "Ruim"),
        ]),

        ("DILMA (mérito misto)", TipoCargo.PRESIDENTE, [
            CargoOcupado(TipoCargo.PRESIDENTE, "2011-2016", False,
                         "Fome voltou no mandato", "Deposta em golpe"),
        ]),
    ]

    for nome, cargo, historico in casos:
        r = avaliar_candidatura(nome, cargo, historico)
        print(f"  {r.resumo()}")
        print(f"    Endossado: {r.endossado} | Mérito: {r.tem_merito}")
        print()


if __name__ == "__main__":
    _demo()
