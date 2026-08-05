#!/usr/bin/env python3
"""
OpenSemReeleicao -- Política: Sem Reeleição de Vampiros
=========================================================
"Quem teve seu cargo, beleza. Agora vá fazer outra coisa da vida.
 Precisamos de gente nova, não de vampiros."

POLÍTICA OFICIAL DA OPENREPUBLIC:

1. NÃO HÁ ENDORSO A REELEIÇÃO.
   Quem está no cargo e vacilou, não volta.

2. SÓ NOVAS CANDIDATURAS SÃO ENDOSSADAS.

3. QUEM TEVE CARGO E RESOLVEU: VALEU. PASSA A VEZ.
   Não é punição. É rotação. O cargo não é propriedade.

4. QUEM TEVE CARGO E NÃO RESOLVEU (OMISSÃO): NÃO VOLTA NUNCA.
   Teve a chance. Não entregou. Próximo.

5. EXCEÇÃO: CARGO TÉCNICO DIFERENTE.
   Quem foi deputado pode ser governador (cargo novo).
   Quem foi governador pode ser ministro (cargo novo).
   Mas deputado -> deputado = bloqueado.

O BLOQUEIO É BINÁRIO. NÃO TEM TERMO MÉDIO. NÃO TEM "MAS Dessa VEZ".
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
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
    MINISTRO = "ministro"  # cargo técnico, nao eletivo
    SECRETARIO = "secretario"  # cargo técnico, nao eletivo


class StatusReeleicao(Enum):
    BLOQUEADO = "bloqueado"        # teve cargo ELETIVO igual, nao pode
    AUTORIZADO = "autorizado"       # cargo novo ou nunca teve cargo
    VAMPIRO = "vampiro"             # teve cargo, vacilou, quer voltar ao MESMO


@dataclass
class CargoOcupado:
    """Um cargo que alguém já ocupou."""
    cargo: TipoCargo
    periodo: str           # "2019-2022"
    resolveu: Optional[bool] = None  # True = entregou, False = vacilou, None = sem dado
    observacao: str = ""


@dataclass
class AvaliacaoReeleicao:
    """Resultado da avaliação de reeleição."""
    nome: str
    cargo_desejado: TipoCargo
    status: StatusReeleicao
    cargos_anteriores: List[CargoOcupado]
    motivo: str

    @property
    def bloqueado(self) -> bool:
        return self.status == StatusReeleicao.BLOQUEADO

    @property
    def endossado(self) -> bool:
        """OpenRepublic endossa esta candidatura?"""
        return self.status != StatusReeleicao.BLOQUEADO and self.status != StatusReeleicao.VAMPIRO

    def resumo(self) -> str:
        icon = {"bloqueado": "🚫", "autorizado": "✅", "vampiro": "🧛"}.get(self.status.value, "?")
        return f"{icon} {self.nome}: {self.status.value.upper()} — {self.motivo}"


def avaliar_reeleicao(
    nome: str,
    cargo_desejado: TipoCargo,
    cargos_anteriores: List[CargoOcupado],
) -> AvaliacaoReeleicao:
    """
    Avalia se alguém pode ser endossado para um cargo.

    REGRAS:
    1. Mesmo cargo eletivo = BLOQUEADO (sem reeleição, ponto)
    2. Mesmo cargo + não resolveu = VAMPIRO
    3. Cargo diferente = AUTORIZADO (mesmo que teve outro cargo)
    4. Nunca teve cargo = AUTORIZADO (gente nova)
    """
    cargos_eletivos = {
        TipoCargo.PRESIDENTE, TipoCargo.GOVERNADOR, TipoCargo.SENADOR,
        TipoCargo.DEPUTADO_FEDERAL, TipoCargo.DEPUTADO_ESTADUAL,
        TipoCargo.PREFEITO, TipoCargo.VEREADOR,
    }

    # Verificar se já teve o MESMO cargo eletivo
    mesmo_cargo = [c for c in cargos_anteriores if c.cargo == cargo_desejado]

    if mesmo_cargo:
        # Teve o mesmo cargo. Bloqueado.
        # Se também vacilou (não resolveu), é VAMPIRO
        vacilou = any(c.resolveu is False for c in mesmo_cargo)
        if vacilou:
            return AvaliacaoReeleicao(
                nome, cargo_desejado, StatusReeleicao.VAMPIRO, cargos_anteriores,
                f"Teve cargo {cargo_desejado.value} ({mesmo_cargo[0].periodo}), "
                f"NÃO resolveu, quer voltar ao mesmo cargo. VAMPIRO. Bloqueado."
            )
        else:
            return AvaliacaoReeleicao(
                nome, cargo_desejado, StatusReeleicao.BLOQUEADO, cargos_anteriores,
                f"Teve cargo {cargo_desejado.value} ({mesmo_cargo[0].periodo}). "
                f"Política: sem reeleição. Passa a vez. Cargo novo é permitido."
            )

    # Verificar se teve OUTRO cargo eletivo
    outros_eletivos = [c for c in cargos_anteriores if c.cargo in cargos_eletivos]

    if not outros_eletivos:
        # Nunca teve cargo eletivo = GENTE NOVA
        return AvaliacaoReeleicao(
            nome, cargo_desejado, StatusReeleicao.AUTORIZADO, cargos_anteriores,
            "Nunca teve cargo eletivo. Gente nova. Endossado."
        )

    # Teve outro cargo eletivo (diferente do desejado)
    # Verificar se vacilou no cargo anterior
    vacilou_anterior = any(c.resolveu is False for c in outros_eletivos)

    if vacilou_anterior:
        c = [c for c in outros_eletivos if c.resolveu is False][0]
        return AvaliacaoReeleicao(
            nome, cargo_desejado, StatusReeleicao.BLOQUEADO, cargos_anteriores,
            f"Teve cargo {c.cargo.value} ({c.periodo}) e NÃO resolveu. "
            f"Teve a chance. Não entregou. Bloqueado para qualquer cargo."
        )

    # Teve outro cargo, resolveu (ou sem dado), quer cargo DIFERENTE
    return AvaliacaoReeleicao(
        nome, cargo_desejado, StatusReeleicao.AUTORIZADO, cargos_anteriores,
        f"Teve cargo(s) eletivo(s) antes ({', '.join(c.cargo.value for c in outros_eletivos)}). "
        f"Cargo desejado é DIFERENTE. Autorizado — rotação, não vampiro."
    )


# ============================================================================
# DEMO
# ============================================================================

def _demo():
    print("=" * 70)
    print("OPEN SEM REELEIÇÃO — POLÍTICA OFICIAL")
    print("=" * 70)
    print()
    print("REGRA: NÃO HÁ ENDORSO A REELEIÇÃO.")
    print("  Quem teve cargo e vacilou, não volta.")
    print("  Só novas candidaturas são endossadas.")
    print("  Quem teve cargo e resolveu: valeu. Passa a vez.")
    print("  Quem teve cargo e não resolveu: bloqueado pra sempre.")
    print()

    casos = [
        # 1. Gente nova
        ("GENTE NOVA (mock)", TipoCargo.DEPUTADO_FEDERAL, []),

        # 2. Deputado quer reeleger (resolveu)
        ("DEPUTADO QUE ENTREGOU (mock)", TipoCargo.DEPUTADO_FEDERAL, [
            CargoOcupado(TipoCargo.DEPUTADO_FEDERAL, "2019-2022", True, "Aprovou leis úteis"),
        ]),

        # 3. Deputado quer reeleger (vacilou)
        ("DEPUTADO VAMPIRO (mock)", TipoCargo.DEPUTADO_FEDERAL, [
            CargoOcupado(TipoCargo.DEPUTADO_FEDERAL, "2019-2022", False, "Não fez nada"),
        ]),

        # 4. Governador quer senador (cargo novo)
        ("GOVERNADOR -> SENADOR (mock)", TipoCargo.SENADOR, [
            CargoOcupado(TipoCargo.GOVERNADOR, "2015-2022", True, "IDEB subiu"),
        ]),

        # 5. Governador quer reeleger
        ("GOVERNADOR QUER REELEIÇÃO (mock)", TipoCargo.GOVERNADOR, [
            CargoOcupado(TipoCargo.GOVERNADOR, "2015-2022", True, "Bom gestor"),
        ]),

        # 6. Governador vacilou quer outro cargo
        ("GOVERNADOR QUE VACILOU (mock)", TipoCargo.SENADOR, [
            CargoOcupado(TipoCargo.GOVERNADOR, "2015-2022", False, "Obras paradas"),
        ]),

        # 7. Presidente quer reeleger (Dilma)
        ("PRESIDENTE QUER VOLTA (mock)", TipoCargo.PRESIDENTE, [
            CargoOcupado(TipoCargo.PRESIDENTE, "2011-2016", None, "Deposta em golpe"),
        ]),
    ]

    for nome, cargo, historico in casos:
        r = avaliar_reeleicao(nome, cargo, historico)
        print(f"  {r.resumo()}")
        print(f"    Endossado: {r.endossado}")
        print()


if __name__ == "__main__":
    _demo()
