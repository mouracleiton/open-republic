#!/usr/bin/env python3
"""
OpenSemReeleicao -- Política: Uma Só Passagem
================================================
"Quem teve seu cargo, beleza. Agora vá fazer outra coisa da vida.
 Não volta. Não troca. Não é indicado pra nada. Acabou."

POLÍTICA OFICIAL DA OPENREPUBLIC — DEFINITIVA:

1. QUEM TEVE CARGO POLÍTICO NÃO VOLTA.
   Não reeleição. Não outro cargo. Não comissionado. Nada.

2. SÓ QUEM NUNCA TEVE CARGO É ENDOSSADO.
   Gente nova. Sem sangues sugadores.

3. NÃO É PUNIÇÃO. É ROTAÇÃO.
   O cargo não é propriedade. Quem cumpriu, cumpriu. Obrigado. Próximo.

O BLOQUEIO É ABSOLUTO. NÃO TEM EXCEÇÃO. NÃO TERMO MÉDIO. NÃO "MAS DESSA VEZ".
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
    AUTORIZADO = "autorizado"   # nunca teve cargo -> gente nova
    BLOQUEADO = "bloqueado"     # teve qualquer cargo -> acabou


@dataclass
class CargoOcupado:
    cargo: TipoCargo
    periodo: str
    observacao: str = ""


@dataclass
class AvaliacaoCandidatura:
    nome: str
    cargo_desejado: TipoCargo
    status: StatusEndosso
    cargos_anteriores: List[CargoOcupado]
    motivo: str

    @property
    def endossado(self) -> bool:
        return self.status == StatusEndosso.AUTORIZADO

    def resumo(self) -> str:
        icon = {"autorizado": "✅", "bloqueado": "🚫"}.get(self.status.value, "?")
        return f"{icon} {self.nome}: {self.status.value.upper()} — {self.motivo}"


def avaliar_candidatura(
    nome: str,
    cargo_desejado: TipoCargo,
    cargos_anteriores: List[CargoOcupado],
) -> AvaliacaoCandidatura:
    """
    Avalia se alguém pode ser endossado.

    REGRA ÚNICA: teve QUALQUER cargo político ou comissionado = BLOQUEADO.
    Nunca teve = AUTORIZADO.
    """
    if cargos_anteriores:
        cargos_str = ", ".join(
            f"{c.cargo.value} ({c.periodo})" for c in cargos_anteriores
        )
        return AvaliacaoCandidatura(
            nome, cargo_desejado, StatusEndosso.BLOQUEADO, cargos_anteriores,
            f"Teve cargo(s): {cargos_str}. Política: uma só passagem. "
            f"Não volta, não troca, não é indicado. Acabou."
        )

    return AvaliacaoCandidatura(
        nome, cargo_desejado, StatusEndosso.AUTORIZADO, cargos_anteriores,
        "Nunca teve cargo político. Gente nova. Endossado."
    )


# ============================================================================
# DEMO
# ============================================================================

def _demo():
    print("=" * 70)
    print("OPEN SEM REELEIÇÃO — UMA SÓ PASSAGEM")
    print("=" * 70)
    print()
    print("REGRA ÚNICA:")
    print("  Quem teve cargo NÃO VOLTA.")
    print("  Não reeleição. Não outro cargo. Não comissionado. Nada.")
    print("  Só gente nova é endossada.")
    print()

    casos = [
        ("GENTE NOVA", TipoCargo.DEPUTADO_FEDERAL, []),
        ("EX-DEPUTADO QUER SENADOR", TipoCargo.SENADOR, [
            CargoOcupado(TipoCargo.DEPUTADO_FEDERAL, "2019-2022"),
        ]),
        ("EX-GOVERNADOR QUER MINISTRO", TipoCargo.MINISTRO, [
            CargoOcupado(TipoCargo.GOVERNADOR, "2015-2022"),
        ]),
        ("EX-VEREADOR QUER DEPUTADO", TipoCargo.DEPUTADO_FEDERAL, [
            CargoOcupado(TipoCargo.VEREADOR, "2017-2020"),
        ]),
        ("EX-PRESIDENTE QUER QUALQUER COISA", TipoCargo.SENADOR, [
            CargoOcupado(TipoCargo.PRESIDENTE, "2011-2016"),
        ]),
        ("EX-SECRETARIO QUER DEPUTADO", TipoCargo.DEPUTADO_FEDERAL, [
            CargoOcupado(TipoCargo.SECRETARIO, "2019-2022"),
        ]),
    ]

    for nome, cargo, historico in casos:
        r = avaliar_candidatura(nome, cargo, historico)
        print(f"  {r.resumo()}")
        print(f"    Endossado: {r.endossado}")
        print()


if __name__ == "__main__":
    _demo()
